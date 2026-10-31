# 机器人/具身智能每日速递 — 2026-11-01 / Robotics & Embodied AI Daily — 2026-11-01

**检查窗口 / Window:** 台北时间 2026-10-31 ~07:40 → 2026-11-01 ~07:40(UTC 10-30 23:40 → 10-31 23:40)。今天是周日,arXiv 周末不发布新列表;最新的 cs.RO 列表仍是 2026-10-30(周五)期,已在 [昨日报告](robotics-daily-2026-10-31.md) 中完整处理。 / Today is Sunday; arXiv publishes no new listing on weekends. The newest cs.RO listing is still the 2026-10-30 issue, already fully processed in yesterday's report.

> 本期无监测项开源,故无「🔔 监测项已开源」区块。SuperMimic 的 `signal` 为 false,仅有第三方复现仓库。 / No watchlist item was released; SuperMimic `signal` = false, only third-party reproductions.

## 来源状态 / Source Status

| 来源 / Source | 状态 / Status |
|---|---|
| arXiv cs.RO 列表 / listing | ✅ 最新期仍为 2026-10-30(New 109 + Cross 20),无新列表,无需重复处理。 / Latest issue unchanged (10-30); nothing new to classify. |
| arXiv API 关键词检索 / keyword search | ✅ 已运行(cs.RO/cs.AI/cs.LG/cs.CV,submittedDate 2026-10-30 23:40 → 2026-11-01 00:00 UTC)。26 个关键词(embodied、vision-language-action、VLA、VLN、vision-language navigation、humanoid、legged locomotion、whole-body control、model predictive control、reinforcement learning robot、sim-to-real、dexterous manipulation、robot foundation model、world model、world action model、WAM、video world model、spatial intelligence、spatial reasoning、SLAM、visual SLAM、LiDAR SLAM、gaussian splatting SLAM、3D reconstruction、motion tracking、motion imitation)命中数全部为 0。核验:API 中 cs.RO 最新一篇提交时间为 2026-10-29 17:59 UTC,即周末确实没有新提交入库,并非查询错误。入选 0 篇。 / All 26 keywords returned 0 hits; verified the newest cs.RO paper in the API is dated 2026-10-29 17:59 UTC, so this is a genuine weekend gap, not a query error. 0 papers selected. |
| Hugging Face Daily Papers | ✅ 取得 100 条;其中未在往期报告出现的条目均与机器人无关(LLM agent、图像/视频生成等),无新的机器人论文。 / 100 fetched; the ones not seen in earlier reports are non-robotics. |
| GitHub radar(`data/latest.json`,date_taipei = 2026-11-01) | ✅ 已更新;new_repos 150、star_growth_top 60、watchlist_releases 0、oss_watch 1(无错误);star 基线 2026-10-30。 / Fresh; baseline 2026-10-30. |

## 今日必读 / Top Picks

今日无新的 arXiv 论文可选。以下为 GitHub 侧新出现的值得关注项。 / No new arXiv papers today; the picks below come from GitHub.

1. **[Ropedia W0](https://github.com/Ropedia/ropedia-w0)**(世界模型;✅ 已开源,star 186,日增 14)— 首个覆盖人类与多种机器人的第一视角 loco-manipulation 世界基础模型,5B 推理代码、权重与 Xp-Teleop 数据已发布。 / First egocentric loco-manipulation world foundation model spanning humans and robots; 5B inference code, weights and Xp-Teleop data released.
2. **[MiniWAM](https://arxiv.org/abs/2610.12194)**(WAM;🕒 计划开源)— 预测紧凑未来表征的世界-动作模型,训练最多加速 8 倍。 / A world-action model predicting compact future targets, up to 8× faster training.

## 运动控制·RL / Motion Control · RL

今日无新增论文。第三方 SuperMimic 复现持续涌现(监测项见文末),均非官方。 / No new papers. Third-party SuperMimic reproductions keep appearing (see the watchlist section); none is official.

## 运动控制·传统 / Motion Control · Classical

今日无新增论文。 / No new papers.

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

今日无新增论文。 / No new papers. GitHub: [GroundingPI](https://github.com/groundingpi/GroundingPI)(star 274,日增 20)是面向物理智能的 4B grounding 基础模型,覆盖检测、指代、指点、OCR、GUI 与版面 grounding,描述称在 34 个基准上整体领先;开源状态:✅ 已开源 / Released — [仓库](https://github.com/groundingpi/GroundingPI);未对应到具体 arXiv 论文,指标仅来自仓库描述。 / A 4B grounding foundation model for physical intelligence; the repo description claims SOTA overall across 34 benchmarks (repo description only, no matching paper checked).

## VLA / VLN

今日无新增论文。 / No new papers. GitHub: [FPO](https://github.com/tuotuoLyu/FPO)(star 88,日增 50;ICRA 2026,面向 pi0 的 Flow Policy Optimization 强化微调)与 [ForesightSafety-VLA](https://github.com/tuotuoLyu/ForesightSafety-VLA)(star 87,IROS 2026 VLA 安全诊断基准)均已在往期报告出现。 / Both already covered in earlier reports.

## 世界模型与 WAM / World Models & WAM

### [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855) — Ropedia
🏷️ 交叉方向 / Also: 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models(目标为世界预测、策略评估与规划,而非训练控制策略,故不归入运动控制;the target is world prediction/policy evaluation/planning, not control-policy training)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Ropedia/ropedia-w0);已发布 5B 推理代码、预训练与中期训练检查点([HF 模型](https://huggingface.co/ropedia-ai/Ropedia-W0))和 Xp-Teleop 数据([HF 数据](https://huggingface.co/datasets/ropedia-ai/Xp-Teleop)),A14B 检查点、评测代码与后训练代码仍在 To-Do(依据仓库 README;已用 `git ls-remote` 匿名验证仓库存在)。
- 🇨🇳 问题:联合建模 locomotion 与 manipulation 的世界模型难以跨具身泛化,原因是动作空间异构且多模态监督有限。方法:构建 Xp-Data(1 万小时第一视角人类数据 + 3 千小时机器人数据),用「相机位姿表示 locomotion、投影骨架表示 manipulation」的统一运动学表示,并提出 Xp-Teleop 长时程灵巧人形遥操作基准。结果:在五个跨具身基准(DreamDojo、Ψ0、ω-HOME、Xp-Teleop、AgiBot)及人类第一视角视频上达到摘要所称的 SOTA;人类预训练数据越多,人类与机器人评测都越好;蒸馏后支持实时、分钟级 rollout 与 VR 交互,并用于策略评估、基于模型的规划与世界-动作建模。摘要未给出具体数值。
- 🇬🇧 Problem: jointly modeling locomotion and manipulation across embodiments is hard due to heterogeneous action spaces and limited multimodal supervision. Method: Xp-Data (10k h egocentric human + 3k h robot data) with a unified kinematic interface (camera poses for locomotion, projected skeletons for manipulation) plus the Xp-Teleop long-horizon benchmark. Results: claimed state of the art on five cross-embodiment benchmarks (DreamDojo, Ψ0, ω-HOME, Xp-Teleop, AgiBot) and held-out human video; scaling human pre-training improves both human and robot evaluation; after distillation it supports real-time minute-long rollouts for live VR, and is applied to policy evaluation, model-based planning and world-action modeling. The abstract gives no specific numbers.

### [MiniWAM: Learning Compact Future Targets for Efficient World-Action Modeling](https://arxiv.org/abs/2610.12194)
开源状态 / Code: 🕒 计划开源 / Planned — GitHub 出现 [MiniWAM-release](https://github.com/J1dan/MiniWAM-release)(2026-10-31 创建,仅一次推送,star 2),项目页为 [j1dan.github.io/MiniWAM](https://j1dan.github.io/MiniWAM);仓库内容尚未核验,暂不判定为已开源。
- 🇨🇳 问题:多数 WAM 在预训练视觉骨干的原生表示空间中预测未来状态,目标维度高、训练成本大。方法:MiniWAM 改为预测由特权的当前-未来转移学得的紧凑未来表征,构造目标的 PRISM 结合逆动力学监督与特征重建,PRISM 编码器冻结后联合预测目标与动作。结果:原生未来特征 token 减少 65 倍,在 DINOv3 与 WAN2.1 VAE 特征上均优于原生未来特征预测,世界-动作训练最多加速 8 倍;0.25B 参数即在 LIBERO、LIBERO-Plus、RoboTwin 2.0 仿真基准上与更大的 WAM 相当(摘要未给出真机结果)。
- 🇬🇧 Problem: most WAMs predict futures in the native feature space of pretrained visual backbones, giving high-dimensional, costly targets. Method: MiniWAM predicts compact future representations learned from privileged current–future transitions via PRISM (inverse-dynamics supervision plus feature reconstruction), then trains jointly on targets and actions with the encoder frozen. Results: 65× fewer future feature tokens, better than native-feature prediction with DINOv3 and WAN2.1 VAE features, up to 8× faster training, and a 0.25B model competitive with larger WAMs on LIBERO, LIBERO-Plus and RoboTwin 2.0 (no real-robot results in the abstract).

另见 / See also: [SolarWM](https://github.com/Junchao-cs/SolarWM)(star 823,日增 14;长时程视频世界模型的开放数据与训练,描述无机器人专属内容)。 / long-horizon video world model, general rather than robot-specific.

## 空间智能与 SLAM / Spatial Intelligence & SLAM

今日无新增论文。GitHub:[lidar_slam_ros2](https://github.com/rsasaki0109/lidar_slam_ros2)(star 884,日增 14,ROS 2 LiDAR SLAM 点云地图制作与基准)、[kornia](https://github.com/kornia/kornia)(star 11521,日增 60,几何视觉库)。 / No new papers.

## 其他值得关注 / Other Notable

[ProAct](https://arxiv.org/abs/2602.14048)(SIGGRAPH ASIA 2026;流式运动生成 + 智能体推理的实时具身社交交互,部署于人形机器人;官方仓库 [ProAct-Official](https://github.com/ProActRobot/ProAct-Official) 昨日创建,star 2,内容未核验)——其目标为社交交互行为生成,非 locomotion/全身控制,故未归入运动控制。 / Social-interaction behavior generation on a humanoid, not locomotion or whole-body control.

## GitHub 动态 / GitHub Highlights

**Star 增长 / Star growth(相对 2026-10-30 基线 / vs. 10-30 baseline)**

| 仓库 / Repo | Stars | Δ | 说明 / Note |
|---|---|---|---|
| [tuotuoLyu/FPO](https://github.com/tuotuoLyu/FPO) | 88 | +50 | pi0 的 Flow Policy Optimization RL 微调(ICRA 2026)/ RL fine-tuning of pi0 flow policies |
| [groundingpi/GroundingPI](https://github.com/groundingpi/GroundingPI) | 274 | +20 | 4B 物理智能 grounding 基础模型 / 4B grounding model |
| [cocacola-lab/awesome-embodied-rsi](https://github.com/cocacola-lab/awesome-embodied-rsi) | 242 | +15 | 具身递归自我改进资源列表 / Embodied recursive self-improvement list |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 14488 | +15 | pi0 / pi0.5 官方框架 / official pi0 framework |
| [Ropedia/ropedia-w0](https://github.com/Ropedia/ropedia-w0) | 186 | +14 | 见上文世界模型 / see above |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28613 | +14 | 端到端机器人学习 / end-to-end robot learning |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 16002 | +22 | 物理仿真器 / physics simulator |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 8543 | +10 | 机器人学习框架 / robot learning framework |
| [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) | 397 | +10 | SuperMimic 复现与资源汇总(第三方)/ third-party SuperMimic collection |

(榜内另有 gods-eye-view、RuView、text-to-cad 等增长更快但与关注主题关系较弱的仓库,不列入。 / Faster-growing but off-topic repos omitted.)

**新 Release / New releases:** watchlist_releases 为 0,窗口内重点项目无新 release。 / None in the window.

## 今日趋势 / Today's Trends

1. **SuperMimic 复现热潮 / SuperMimic reproduction wave。** 官方代码尚未发布,但 GitHub 上一日内出现多个第三方复现(如 [XZDang13/supermimic](https://github.com/XZDang13/supermimic)、[xuejun7777/SuperMimic-Decoupled-WBC](https://github.com/xuejun7777/SuperMimic-Decoupled-WBC)、[Houserz/supermimic-quadruped](https://github.com/Houserz/supermimic-quadruped)),涉及 G1、四足等平台。 / No official code yet, but several third-party reproductions appeared within a day, targeting G1 and quadrupeds.
2. **世界模型走向跨具身与高效化 / World models go cross-embodiment and efficient。** [Ropedia W0](https://arxiv.org/abs/2610.26855) 用人类第一视角数据做跨具身预训练,[MiniWAM](https://arxiv.org/abs/2610.12194) 用紧凑目标降低 WAM 训练成本。 / W0 pre-trains on human egocentric data across embodiments; MiniWAM shrinks WAM targets.
3. **周末静默 / Weekend lull。** arXiv 无新提交,HF Daily Papers 无新机器人论文。 / No new arXiv submissions or robotics HF papers.

## 关键词建议 / Keyword Suggestions

今日无建议 / No suggestions today(信号不足,仅一天且为周末 / insufficient signal on a weekend).

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 / Added | 当前状态 / Status | 今日检查 / Today's check | 备注 / Notes |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 / Unknown(无变化) | signal = false;candidate_repos 空;项目页无 GitHub 链接与发布承诺;arXiv 最新版 v1;errors 为空 | 15 个 search_hits 均为第三方复现(如 [XZDang13/supermimic](https://github.com/XZDang13/supermimic)),不算官方开源 / 15 search hits are third-party reproductions |

**建议加入监测 / Suggested additions:** 无(今日无新的运动控制论文)/ none. [MiniWAM](https://arxiv.org/abs/2610.12194) 属世界模型类、价值次之,暂不建议。

**建议移出 / Suggested removals:** 无 / none.
