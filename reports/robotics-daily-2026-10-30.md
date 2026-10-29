# 机器人/具身智能每日速递 — 2026-10-30 / Robotics & Embodied AI Daily — 2026-10-30

**检查窗口 / Window:** 台北时间 2026-10-29 ~07:40 → 2026-10-30 ~07:40(UTC 10-28 23:40 → 10-29 23:40)。 / Taipei time, last ~24 h.

> 本期无监测项开源,故无「🔔 监测项已开源」区块。 / No watchlist item was released today.

## 来源状态 / Source Status

| 来源 / Source | 状态 / Status |
|---|---|
| arXiv cs.RO 列表 / listing | ⚠️ 抓取时(UTC 10-29 23:41)列表仍是 2026-10-28(周三)那一期(76 New + 9 Cross + 40 Replacements),已在昨日报告中完整处理;周四(10-29)的新列表尚未发布。本期不重复展开。 / At fetch time (23:41 UTC on 29 Oct) the listing was still the Wednesday 28 Oct one, already fully covered in yesterday's report; the Thursday listing was not yet published. Not re-expanded. |
| arXiv API 检索 / keyword search | ⚠️ 对 cs.RO / cs.AI / cs.LG / cs.CV 使用 submittedDate 窗口 2026-10-28 14:00 UTC 之后查询,命中 0 条;cs.RO 最新一条提交时间为 2026-10-27 17:59 UTC([ThinkWorld](https://arxiv.org/abs/2610.37666)),与昨日一致。关键词逐词检索未运行(窗口内无任何条目,无需逐词)。入选 0 篇,取得完整摘要 0 篇。 / Date-window query returned 0 entries in all four categories; newest cs.RO submission is 27 Oct 17:59 UTC, same as yesterday. Per-keyword searches not run since the window is empty. 0 papers selected. |
| Hugging Face Daily Papers | ✅ 100 条,与昨日基本相同;窗口内无新增机器人相关且带仓库的论文(已在昨日涉及:[RynnWorld-Latent](https://arxiv.org/abs/2610.36791)、[JAM](https://arxiv.org/abs/2610.37219)、[Hy-Nomas](https://arxiv.org/abs/2610.36729))。 |
| GitHub radar(`data/latest.json`,date_taipei = 2026-10-30) | ✅ 已更新;new_repos 150 条、star_growth_top 60 条、watchlist_releases 1 项、oss_watch 1 项。star 基线 2026-10-28。 |

## 今日必读 / Top Picks

今日无新论文。GitHub 上最值得关注的是围绕 [SuperMimic](https://arxiv.org/abs/2610.28480)(运动控制·RL)爆发的第三方复现生态,以及 rsl_rl 的 v5.5.2 发布。 / No new papers today. The GitHub highlights are the burst of third-party SuperMimic reproductions (Motion Control · RL) and the rsl_rl v5.5.2 release.

## 运动控制·RL / Motion Control · RL

今日无新论文。 / No new papers today.

### 第三方 SuperMimic 复现仓库 / Third-party SuperMimic reproductions
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown — 官方代码仍未见;以下均为第三方,不算官方开源。

- 🇨🇳 radar 的 search_hits 显示 10-26 至 10-29 间出现至少 15 个以 SuperMimic 命名或描述的仓库,星数多数为 0。其中 [instantTrack](https://github.com/Huy-Quang-Dao/instantTrack)(53★,10-29 新建)称在单 GPU 上 15 分钟内完成 Unitree G1 全身跟踪训练,思路为「SuperMimic 风格世界模型 + InstantMimic 风格 GPU 循环」;[Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic)(205★,今日 +15)称是在 UniLab 上的独立复现;[awesome-supermimic](https://github.com/miao-org/awesome-supermimic)(340★,今日 +50)是资源汇总。这些数字与说明均来自仓库描述,未做运行验证。
- 🇬🇧 The radar's search hits show at least 15 repositories named after or describing SuperMimic created between 26 and 29 Oct, most with 0 stars. [instantTrack](https://github.com/Huy-Quang-Dao/instantTrack) (53★, created 29 Oct) claims Unitree G1 whole-body tracking in 15 minutes on one GPU, combining a SuperMimic-style world model with an InstantMimic-style GPU loop; [Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) (205★, +15 today) describes itself as an independent reproduction on UniLab; [awesome-supermimic](https://github.com/miao-org/awesome-supermimic) (340★, +50 today) is a resource list. All figures come from repo descriptions and were not run or verified.

## 运动控制·传统 / Motion Control · Classical

今日无新论文。 / No new papers today.

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

今日无新论文。仓库:[openlambda](https://github.com/LambdaHumanoid/openlambda)(λ_0,人形 loco-manipulation 的开放世界第一视角人类数据,128★,+16)。 / No new papers. Repo: [openlambda](https://github.com/LambdaHumanoid/openlambda) (λ_0, egocentric human data for humanoid loco-manipulation; 128★, +16).

## VLA / VLN

今日无新论文。新仓库:[ForesightSafety-VLA](https://github.com/tuotuoLyu/ForesightSafety-VLA)(IROS 2026 VLA 安全诊断基准,官方代码,2★);[FPO](https://github.com/tuotuoLyu/FPO)(VLA 的 flow-matching 策略强化微调,ICRA 2026 官方代码,2★)。 / No new papers. New repos: ForesightSafety-VLA (IROS 2026 VLA safety benchmark, official code, 2★) and FPO (RL fine-tuning of flow-matching VLA policies, ICRA 2026, official code, 2★).

## 世界模型与 WAM / World Models & WAM

今日无新论文。新仓库:[ga-wm](https://github.com/gaoxiang12/ga-wm)(面向 VLA 任务的几何感知世界模型,11★);[e05](https://github.com/X-EraAI/e05)(对应 E0.5,世界-动作模型,8★);[Looking-Ahead](https://github.com/TencentARC/Looking-Ahead)(自回归视频生成中建模未来演化,157★,+13)。 / No new papers. New repos: ga-wm (geometry-aware world model for VLA, 11★), e05 (E0.5 world-action model, 8★), Looking-Ahead (future-evolution modelling for autoregressive video generation, 157★, +13).
另见 / See also: [SuperMimic 复现](https://github.com/Motphys/Uni-SuperMimic)(已归入 运动控制·RL)。

## 空间智能与 SLAM / Spatial Intelligence & SLAM

今日无新论文。新仓库:[RESPLE2](https://github.com/ASIG-X/RESPLE2)(递归非均匀 B 样条多传感器里程计框架,26★,+21,对应 [arXiv 2610.37602](https://arxiv.org/abs/2610.37602))。 / No new papers. New repo: RESPLE2 (recursive non-uniform B-spline multi-sensor odometry, 26★, +21).

## GitHub 动态 / GitHub Highlights

| 仓库 / Repo | ★ | 增长 / Δ | 说明 / Note |
|---|---|---|---|
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | 101565 | +561 | 用 WiFi 信号做空间感知,通用项目,与机器人关联较弱 / WiFi-based spatial sensing, loosely related |
| [Gen-Verse/RSI-Anything](https://github.com/Gen-Verse/RSI-Anything) | 1056 | +70 | 世界模型驱动的递归自我改进 / World-model-based recursive self-improvement |
| [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) | 340 | +50 | SuperMimic 资源汇总 / SuperMimic resource list |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28577 | +24 | 端到端机器人学习 / end-to-end robot learning |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 15968 | +21 | 物理仿真 / physics simulator |
| [ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2) | 26 | +21 | 多传感器里程计 / multi-sensor odometry |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 14459 | +18 | π 系列 VLA / π VLA models |
| [LambdaHumanoid/openlambda](https://github.com/LambdaHumanoid/openlambda) | 128 | +16 | 人形 loco-manipulation 数据 / humanoid loco-manip data |
| [Motphys/Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) | 205 | +15 | SuperMimic 第三方复现 / third-party reproduction |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 8523 | +14 | 机器人学习框架 / robot learning framework |

**新 release / New releases(监测重点项目 / watchlist projects):**

- [leggedrobotics/rsl_rl v5.5.2](https://github.com/leggedrobotics/rsl_rl/releases/tag/v5.5.2)(2026-10-28 16:03 UTC):均为修复类更新——PPO 优势归一化跳过单样本批次、保留 mini-batch 生成器的 rollout 余量、从 PPO 检查点恢复 RND 探索调度、actor 与 critic 共享的 CNN 编码器每次更新只前向一次、循环教师网络在蒸馏更新间保留隐状态、检测环境输出中的无穷值、修复日志 writer 生命周期与重复上传,以及文档/工作流适配新的 extras 分支。release body 在 radar 中被截断,以上为可见部分。 / Fixes only: skip advantage normalization for singleton PPO batches, keep rollout remainders in mini-batch generators, resume RND schedules from PPO checkpoints, step shared actor/critic CNN encoders once per update, keep the recurrent teacher's hidden state across distillation updates, detect infinite values in env outputs, fix logging writer lifecycle and duplicate uploads, and adapt docs/workflows to the new extras branch. The body was truncated in the radar; this is the visible part.

## 今日趋势 / Today's Trends

1. **SuperMimic 复现热潮 / SuperMimic reproduction wave.** 官方代码尚未发布,社区在 4 天内已出现至少 15 个复现或改编仓库(G1、Go2W、T800、足球策略等)。 / With no official code yet, at least 15 reproduction or adaptation repos appeared within four days, targeting G1, Go2W, T800 and soccer policies. 代表:[instantTrack](https://github.com/Huy-Quang-Dao/instantTrack)、[Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic)。
2. **arXiv 空窗 / arXiv gap.** 周四列表在检查时尚未发布,下期报告将覆盖。 / The Thursday listing was not out at check time; tomorrow's report should cover it.

## 关键词建议 / Keyword Suggestions

今日无建议 / No suggestions today(没有足够的新证据;「supermimic」已在 GitHub 搜索中命中,无需新增)。

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 / Added | 当前状态 / Status | 今日检查 / Today's check | 备注 / Notes |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 / Unknown(无变化) | radar `signal: false`;candidate_repos、project_page_github_links、project_page_release_claims、arxiv_github_links 均为空;arXiv 仍为 v1;errors 为空。[项目页](https://supermimic.github.io)HTML 中未见仓库链接或「coming soon」类承诺;`git ls-remote https://github.com/qiayuanl/SuperMimic` 匿名不可访问 | 15 个第三方复现仓库见上文,均非官方,不据此判定已开源 |

**建议加入监测 / Suggested additions:** 无(今日无新论文)。 / None (no new papers).
**建议移出 / Suggested removals:** 无。 / None.
