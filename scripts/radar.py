#!/usr/bin/env python3
"""Daily GitHub radar for robotics / embodied AI.

Runs inside GitHub Actions. Writes:
  data/YYYY-MM-DD.json   (Taipei date) - today's report
  data/latest.json       - copy of the latest report
  data/stars_snapshot.json - star counts used for next day's diff
Only uses the Python standard library.
"""
import datetime as dt
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"
TPE = dt.timezone(dt.timedelta(hours=8))

# Topics: used both to find new repos and to track star growth
TOPICS = [
    "robotics", "embodied-ai", "vision-language-action", "vla",
    "vision-language-navigation", "vln", "humanoid", "humanoid-robot",
    "legged-robots", "legged-robot", "locomotion", "robot-learning",
    "isaac-lab", "isaaclab", "mujoco", "sim-to-real", "dexterous-manipulation",
    "robot-manipulation", "imitation-learning", "model-predictive-control",
    # world models / WAM
    "world-model", "world-models", "video-world-model",
    # spatial intelligence / SLAM
    "spatial-intelligence", "spatial-reasoning", "slam", "visual-slam",
    "lidar-slam", "gaussian-splatting-slam", "3d-reconstruction",
]

# Keyword searches (name/description) for brand-new repos
KEYWORDS = [
    '"vision-language-action"', '"vision language action"', "VLA robot",
    '"vision-language navigation"', "embodied agent", "humanoid locomotion",
    "whole-body control", "legged locomotion", "sim-to-real robot",
    "dexterous manipulation", "robot foundation model", "robot policy",
    # world models / WAM
    '"world model" robot', '"world model" embodied', '"world action model"',
    '"world-action model"', "WAM robot", '"video world model"',
    # spatial intelligence / SLAM
    '"spatial intelligence"', '"spatial reasoning" 3D', "SLAM",
    '"visual SLAM"', '"LiDAR SLAM"', '"gaussian splatting" SLAM',
]

# Well-known projects: always track stars + releases
WATCHLIST = [
    "huggingface/lerobot", "Physical-Intelligence/openpi",
    "isaac-sim/IsaacLab", "isaac-sim/IsaacSim", "google-deepmind/mujoco",
    "google-deepmind/mujoco_playground", "google-deepmind/mujoco_menagerie",
    "NVIDIA/Isaac-GR00T", "openvla/openvla", "newton-physics/newton",
    "Genesis-Embodied-AI/Genesis", "haosulab/ManiSkill", "facebookresearch/habitat-lab",
    "unitreerobotics/unitree_rl_gym", "leggedrobotics/rsl_rl",
    "OpenDriveLab/UniVLA", "TRI-ML/prismatic-vlms", "real-stanford/diffusion_policy",
    # spatial intelligence / SLAM / 3D
    "UZ-SLAMLab/ORB_SLAM3", "facebookresearch/vggt", "naver/dust3r",
    "nerfstudio-project/gsplat",
]

MIN_STARS_TRACK = 30  # ignore tiny repos when tracking star growth


def get(path, params=None):
    url = API + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "robotics-radar",
    })
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (403, 429) and attempt < 2:
                time.sleep(30)
                continue
            if e.code == 404:
                return None
            raise


def search(q, sort="stars", per_page=50):
    time.sleep(2.5)  # search API limit: 30 req/min
    res = get("/search/repositories",
              {"q": q, "sort": sort, "order": "desc", "per_page": per_page})
    return (res or {}).get("items", [])


def slim(r):
    return {
        "full_name": r["full_name"],
        "url": r["html_url"],
        "description": (r.get("description") or "")[:300],
        "stars": r["stargazers_count"],
        "language": r.get("language"),
        "topics": r.get("topics", []),
        "created_at": r["created_at"],
        "pushed_at": r.get("pushed_at"),
    }


def main():
    now = dt.datetime.now(dt.timezone.utc)
    today_tpe = now.astimezone(TPE).date()
    since = (now - dt.timedelta(days=2)).date().isoformat()  # 48h buffer
    os.makedirs("data", exist_ok=True)

    # 1) New repos
    new = {}
    for t in TOPICS:
        for r in search(f"topic:{t} created:>={since}"):
            new[r["full_name"]] = slim(r)
    for k in KEYWORDS:
        for r in search(f"{k} in:name,description created:>={since}"):
            new[r["full_name"]] = slim(r)
    new_repos = sorted(new.values(), key=lambda x: -x["stars"])

    # 2) Star snapshot (topic top repos + watchlist + new repos)
    tracked = {}
    for t in TOPICS:
        for r in search(f"topic:{t} stars:>={MIN_STARS_TRACK}", per_page=100):
            tracked[r["full_name"]] = slim(r)
    for name in WATCHLIST:
        r = get(f"/repos/{name}")
        if r:
            tracked[r["full_name"]] = slim(r)
    for r in new_repos:
        tracked.setdefault(r["full_name"], r)

    snap_path = "data/stars_snapshot.json"
    prev = {}
    prev_time = None
    if os.path.exists(snap_path):
        with open(snap_path) as f:
            old = json.load(f)
        prev = old.get("stars", {})
        prev_time = old.get("taken_at")

    growth = []
    for name, r in tracked.items():
        if name in prev:
            d = r["stars"] - prev[name]
            if d > 0:
                growth.append({**r, "stars_delta": d})
    growth.sort(key=lambda x: -x["stars_delta"])

    with open(snap_path, "w") as f:
        json.dump({"taken_at": now.isoformat(),
                   "stars": {n: r["stars"] for n, r in tracked.items()}}, f)

    # 3) Releases of watchlist within last 48h
    releases = []
    cutoff = now - dt.timedelta(hours=48)
    for name in WATCHLIST:
        rels = get(f"/repos/{name}/releases", {"per_page": 5}) or []
        for rel in rels:
            pub = rel.get("published_at")
            if pub and dt.datetime.fromisoformat(pub.replace("Z", "+00:00")) >= cutoff:
                releases.append({
                    "repo": name, "tag": rel["tag_name"], "name": rel.get("name"),
                    "url": rel["html_url"], "published_at": pub,
                    "prerelease": rel.get("prerelease"),
                    "body": (rel.get("body") or "")[:1500],
                })

    report = {
        "generated_at": now.isoformat(),
        "date_taipei": today_tpe.isoformat(),
        "new_repos_since": since,
        "star_baseline_taken_at": prev_time,
        "new_repos": new_repos[:150],
        "star_growth_top": growth[:60],
        "watchlist_releases": releases,
        "counts": {"new_repos": len(new_repos), "tracked": len(tracked),
                   "with_growth": len(growth), "releases": len(releases)},
    }
    for p in (f"data/{today_tpe.isoformat()}.json", "data/latest.json"):
        with open(p, "w") as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
    print(json.dumps(report["counts"]))


if __name__ == "__main__":
    main()
