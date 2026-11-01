# 机器人/具身智能每日速递 — 2026-11-02 / Robotics & Embodied AI Daily — 2026-11-02

**检查窗口 / Window:** 台北时间 2026-11-01 ~07:40 → 2026-11-02 ~07:40(UTC 10-31 23:40 → 11-01 23:40)。今天是周一,但运行时 arXiv 周一的 cs.RO 新列表尚未发布。 / Today is Monday, but arXiv's Monday cs.RO listing was not yet published at run time.

> 本期无监测项开源,故无「🔔 监测项已开源」区块。 / No watchlist item was released, so no "🔔 Watchlist Item Released" block.

## 今日必读 / Top Picks

今日无新论文可入选:arXiv 尚无新内容。最近的重点工作(SuperMimic 等)见 [2026-10-31 报告](robotics-daily-2026-10-31.md) 与 [2026-11-01 报告](robotics-daily-2026-11-01.md)。 / No new papers to pick: arXiv has nothing newer. For recent highlights (e.g. SuperMimic) see the [2026-10-31](robotics-daily-2026-10-31.md) and [2026-11-01](robotics-daily-2026-11-01.md) reports.

## 来源状态 / Source Status

| 来源 / Source | 状态 / Status |
|---|---|
| arXiv cs.RO 列表 / listing | ⚠️ 最新期仍是 2026-10-30(New 109 + Cross 20 + Replacements 60),已在前几日报告处理;新列表尚未发布。 / Newest issue still 2026-10-30, already processed; the new one is not out yet. |
| arXiv API 关键词检索 / keyword search | ✅ 已运行:28 个关键词(embodied、VLA、vision-language-action、VLN、humanoid、legged locomotion、whole-body control、MPC、RL robot、sim-to-real、dexterous manipulation、robot foundation model、world model、WAM、spatial intelligence、SLAM、gaussian splatting SLAM、3D reconstruction、motion tracking、motion imitation、quadruped 等),窗口内各词命中均为 0。核对:`cat:cs.RO` 按提交时间降序,最新一篇发布于 2026-10-29 17:59 UTC,即 API 索引中暂无更新条目。入选 0 篇,完整摘要 0 篇。 / All 28 keywords returned 0 hits in the window. Sanity check: the newest cs.RO entry in the API is dated 2026-10-29 17:59 UTC, so nothing newer is indexed. 0 selected, 0 abstracts. |
| HF Daily Papers | ✅ 取到 100 条,最新日期为 2026-10-28,无窗口内新条目(带 githubRepo 的相关旧条目已在前几日处理)。 / 100 fetched; newest dated 2026-10-28; nothing new in window. |
| GitHub radar | ✅ `date_taipei` = 2026-11-02(新鲜)。new_repos 239 个,watchlist_releases 为空(0)。 / Fresh; 239 new repos; no watchlist releases. |

## GitHub 动态 / GitHub Highlights

本窗口无重点项目 release。/ No watchlist releases in window.

**新仓库(筛选后,均为小型/个人项目,star ≤ 13) / New repos (filtered, all small):**

- [lose4578/Auriga](https://github.com/lose4578/Auriga) — 13★:具身操作的 agent harness(Codex 会话 + 单一机器人执行网关)。 / Agent harness for embodied manipulation.
- [J1dan/MiniWAM-release](https://github.com/J1dan/MiniWAM-release) — 2★:MiniWAM,面向高效 World-Action Modeling 的紧凑未来目标学习(世界模型与 WAM;未核实是否为官方实现)。 / MiniWAM compact future targets for world-action modeling (unverified as official).
- [gaetanotorella/H1_2_Squat_Locomotion_RL](https://github.com/gaetanotorella/H1_2_Squat_Locomotion_RL) — 1★:Unitree H1_2 下蹲 locomotion RL,Isaac Lab 训练 + MuJoCo sim2sim + 真机部署(运动控制·RL,个人项目)。 / H1_2 squat locomotion RL with Isaac Lab, sim2sim and real deployment (personal project).
- [ProActRobot/ProAct-Official](https://github.com/ProActRobot/ProAct-Official) — 2★:流式动作生成与 agentic 推理用于实时具身交互。 / Streaming motion generation + agentic reasoning.
- [kkt94/self-calibrating-vla](https://github.com/kkt94/self-calibrating-vla) — 1★:Self-Calibrating VLAs(TEA)测试时具身对齐。 / Test-time embodiment alignment for VLAs.

**star 增长(相对前一日) / Star growth:** 相关榜单以通用库为主,与机器人关联较弱。 / The list is dominated by general-purpose repos.

| 仓库 / Repo | ★ | Δ | 说明 / Note |
|---|---|---|---|
| [kornia/kornia](https://github.com/kornia/kornia) | 11763 | +242 | 几何计算机视觉库 / Geometric CV library |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | 24730 | +212 | AI 设计实体产品 / AI-driven CAD |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 16021 | +19 | 物理仿真器 / Physics simulator |
| [tuotuoLyu/FPO](https://github.com/tuotuoLyu/FPO) | 106 | +18 | pi0 的 Flow Policy Optimization(VLA 的 RL 微调,ICRA 2026 官方代码) / RL fine-tuning of flow-matching VLA |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28630 | +17 | 端到端机器人学习 / End-to-end robot learning |
| [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) | 412 | +15 | SuperMimic 相关资源汇总(非官方) / Unofficial SuperMimic list |

## 趋势与关键词 / Trends & Keywords

- 今日无足够新信号,无关键词建议。 / No suggestions today.
- 观察:SuperMimic 发布后,GitHub 上持续出现第三方复现(见下表搜索命中),反映社区对「可微世界模型 + 人形全身控制」的关注。 / Third-party SuperMimic reproductions keep appearing on GitHub, showing community interest.

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 / Added | 当前状态 / Status | 今日检查 / Today | 备注 / Notes |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 / Unknown | `signal`=false;无官方候选仓库;项目页 [supermimic.github.io](https://supermimic.github.io) 无 GitHub 链接或开源承诺;预设 known_repos(qiayuanl/SuperMimic、HybridRobotics/SuperMimic)匿名访问失败 / No official repo; project page has no code link or promise; known repos not anonymously reachable. | 仅有第三方复现,如 [xuejun7777/SuperMimic-Decoupled-WBC](https://github.com/xuejun7777/SuperMimic-Decoupled-WBC)、[yezheng04/supermimic-g1-23dof](https://github.com/yezheng04/supermimic-g1-23dof),均 0★,不算官方。 / Third-party only, not official. |

建议加入 / Suggested additions: 无 / none. 建议移出 / Suggested removals: 无 / none.
