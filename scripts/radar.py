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
import re
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


OSS_WATCHLIST = "oss_watchlist.json"
OWNER_RECENT_DAYS = 3  # owner repos created this recently are candidates even without a name match
GH_LINK = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
RELEASE_CLAIM = re.compile(
    r"(code (?:will be|is going to be) (?:released|available|open-sourced)"
    r"|coming soon|to be released|release (?:the )?code)[^<\n]{0,80}", re.I)
# common project-page template repos, not the paper's code
TEMPLATE_REPOS = {"nerfies/nerfies.github.io", "eliahuhorwitz/academic-project-page-template",
                  "keunhong/nerfies"}


def fetch_text(url):
    req = urllib.request.Request(url, headers={"User-Agent": "robotics-radar"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def gh_links(text):
    out = []
    for owner, repo in GH_LINK.findall(text):
        repo = re.sub(r"\.git$", "", repo.rstrip("."))
        name = f"{owner}/{repo}"
        if name.lower() not in TEMPLATE_REPOS and name not in out:
            out.append(name)
    return out


def check_oss_item(item, now):
    """Look for an official code release of one watchlist item.

    Every check records its own errors, so one failure never hides the others.
    """
    terms = [t.lower() for t in item.get("search_terms") or [item["name"]]]
    norm = lambda s: re.sub(r"[^a-z0-9]", "", (s or "").lower())
    matches = lambda r: any(norm(t) in norm(r.get("name")) or norm(t) in norm(r.get("description"))
                            for t in terms)
    cands, errors = {}, []

    def add(r, source):
        c = cands.setdefault(r["full_name"], {**slim(r), "sources": []})
        if source not in c["sources"]:
            c["sources"].append(source)

    # 1) exact repo names we expect the authors to use
    for name in item.get("known_repos", []):
        try:
            r = get(f"/repos/{name}")
            if r:
                add(r, "known_repo")
        except Exception as e:
            errors.append(f"known_repo {name}: {e}")

    # 2) authors' / lab accounts: name match, or brand-new repo with any name
    recent = now - dt.timedelta(days=OWNER_RECENT_DAYS)
    for owner in item.get("owners", []):
        try:
            repos = get(f"/users/{owner}/repos", {"sort": "created", "per_page": 50}) or []
            for r in repos:
                created = dt.datetime.fromisoformat(r["created_at"].replace("Z", "+00:00"))
                if matches(r):
                    add(r, f"owner:{owner}")
                elif created >= recent:
                    add(r, f"owner_recent:{owner}")
        except Exception as e:
            errors.append(f"owner {owner}: {e}")

    # 3) GitHub search on name and description (README hits are mostly paper lists).
    # Third-party reproductions show up here too, so search alone never sets signal.
    for t in item.get("search_terms") or [item["name"]]:
        try:
            for r in search(f'"{t}" in:name,description', sort="updated", per_page=20):
                add(r, "search")
        except Exception as e:
            errors.append(f"search {t}: {e}")

    # 4) project pages: github links and release promises
    page_links, claims = [], []
    for url in item.get("project_pages", []):
        try:
            html = fetch_text(url)
            page_links += [l for l in gh_links(html) if l not in page_links]
            claims += [m.group(0).strip() for m in RELEASE_CLAIM.finditer(html)][:5]
        except Exception as e:
            errors.append(f"project_page {url}: {e}")

    # 5) latest arXiv version: abstract + comments
    arxiv_links, arxiv_version = [], None
    if item.get("arxiv_id"):
        try:
            xml = fetch_text("https://export.arxiv.org/api/query?id_list=" + item["arxiv_id"])
            m = re.search(r"<id>https?://arxiv\.org/abs/([^<]+)</id>", xml)
            arxiv_version = m.group(1) if m else None
            entry = xml.split("<entry>", 1)[-1]
            arxiv_links = gh_links(entry)
        except Exception as e:
            errors.append(f"arxiv {item['arxiv_id']}: {e}")

    trusted = lambda c: any(s != "search" for s in c["sources"])
    candidates = sorted((c for c in cands.values() if trusted(c)),
                        key=lambda c: ("known_repo" not in c["sources"], -c["stars"]))
    search_hits = sorted((c for c in cands.values() if not trusted(c)),
                         key=lambda c: c["created_at"], reverse=True)
    return {
        "name": item["name"],
        "title": item.get("title"),
        "arxiv_id": item.get("arxiv_id"),
        "added": item.get("added"),
        "status": item.get("status", "unknown"),
        "signal": bool(candidates or page_links or arxiv_links),
        "candidate_repos": candidates[:20],
        "search_hits": search_hits[:15],
        "project_page_github_links": page_links,
        "project_page_release_claims": claims,
        "arxiv_github_links": arxiv_links,
        "arxiv_latest_version": arxiv_version,
        "errors": errors,
    }


def oss_watch(now):
    if not os.path.exists(OSS_WATCHLIST):
        return []
    try:
        with open(OSS_WATCHLIST) as f:
            items = json.load(f).get("items", [])
    except Exception as e:
        return [{"name": OSS_WATCHLIST, "signal": False, "errors": [f"load: {e}"]}]
    out = []
    for item in items:
        try:
            out.append(check_oss_item(item, now))
        except Exception as e:
            out.append({"name": item.get("name"), "signal": False, "errors": [f"check: {e}"]})
    return out


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

    # 4) OSS watchlist: has any watched work released its code?
    watch = oss_watch(now)

    report = {
        "generated_at": now.isoformat(),
        "date_taipei": today_tpe.isoformat(),
        "new_repos_since": since,
        "star_baseline_taken_at": prev_time,
        "new_repos": new_repos[:150],
        "star_growth_top": growth[:60],
        "watchlist_releases": releases,
        "oss_watch": watch,
        "counts": {"new_repos": len(new_repos), "tracked": len(tracked),
                   "with_growth": len(growth), "releases": len(releases),
                   "oss_signals": sum(1 for w in watch if w.get("signal"))},
    }
    for p in (f"data/{today_tpe.isoformat()}.json", "data/latest.json"):
        with open(p, "w") as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
    print(json.dumps(report["counts"]))


if __name__ == "__main__":
    main()
