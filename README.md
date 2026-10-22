# robotics-radar
Daily GitHub radar for robotics / embodied AI (`scripts/radar.py`, run by `.github/workflows/radar.yml` at 07:07 Taipei). Output: `data/latest.json`.

## OSS watchlist / 开源监测列表

`oss_watchlist.json` lists works whose code is not released yet. Edit only this file to add or remove items. Fields per item:

| field | meaning |
|---|---|
| `name` | short name, also the default search term |
| `title`, `arxiv_id`, `added`, `status` | paper title, arXiv id, date added, current status (`unknown` / `planned`) |
| `search_terms` | strings searched in repo name / description / README |
| `owners` | GitHub accounts of authors or the lab, scanned every day |
| `project_pages` | pages scanned for github.com links and "code coming soon"-style claims |
| `known_repos` | exact repo names probed directly |

Each day the radar writes one entry per item to `oss_watch` in `data/latest.json`: `signal` (true only for trusted evidence: a candidate repo, a project-page link or an arXiv link), `candidate_repos` with their `sources` (`known_repo`, `owner:<acct>` for a name match, `owner_recent:<acct>` for any repo created in the last 3 days), `search_hits` (name/description search matches outside those accounts, e.g. third-party reproductions; never set `signal`), `project_page_github_links`, `project_page_release_claims`, `arxiv_github_links` and `errors`. Failures are recorded in `errors` and never break the rest of the radar.
