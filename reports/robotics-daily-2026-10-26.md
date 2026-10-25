# 机器人/具身智能每日速递 — 2026-10-26 / Robotics & Embodied AI Daily — 2026-10-26

**检查窗口 / Window:** 台北时间 2026-10-25 ~07:40 → 2026-10-26 ~07:40(周一,按规则覆盖周末)。 / Taipei time, Mon 2026-10-26 07:40, covering the weekend.

**今日概况 / Overview:** 🇨🇳 arXiv 周末不发布新列表,cs.RO 页面仍是 2026-10-23(周五)那一期(第三天相同),**本窗口 arXiv 无新增论文**;该期 107 篇已在 [10-24 日报](robotics-daily-2026-10-24.md) 逐条处理,此处不重复展开。本期只报告增量:开源状态核查、GitHub 新仓库与 star 增长、监测项。 🇬🇧 arXiv does not announce over the weekend; the cs.RO page still shows the Fri 23 Oct batch (third day running), so there are **no new arXiv papers in this window**. That batch was fully processed in the [10-24 report](robotics-daily-2026-10-24.md); only deltas (code-release checks, GitHub, watchlist) are reported here.

**来源状态 / Source status**
- arXiv cs.RO `new`:页面标题 "Friday, 23 October 2026",New 63 / Cross 6 / Replacements 38,共 107 条可解析,全部已在 10-24 日报分类。 / Same 107 entries as 10-24; nothing new.
- arXiv API 关键词检索(cs.RO/cs.AI/cs.LG/cs.CV,submittedDate 2026-10-22 ~ 10-26,按提交日降序,以下为窗口内含 10-22 之后提交的条目数,与 10-24 日报有重叠)命中数 / hits: embodied 12, VLA 11, vision-language-action 10, VLN 1, vision-language navigation 1, humanoid 5, legged locomotion 0, whole-body control 0, MPC 0, reinforcement learning robot 0, sim-to-real 1, dexterous manipulation 2, robot foundation model 1, world model 11, world action model 3, WAM 2, video world model 2, spatial intelligence 0, spatial reasoning 2, SLAM 2, visual SLAM 1, LiDAR SLAM 0, gaussian splatting SLAM 0, 3D reconstruction 2, motion tracking 3, motion imitation 0;去重后 47 篇,其中 20 篇不在 cs.RO 列表内(主要为 cs.CV/cs.AI),相关者已在 10-24 日报覆盖,其余与机器人关系较弱,本次未逐篇复核。 / 47 unique hits; none newer than the Friday batch.
- 完整摘要:本次为核对开源状态与分类,重新用 arXiv API `id_list` 取回 77 篇(0 篇失败、0 篇摘要为空);分类结论与 10-24 日报一致,无变化。 / 77 abstracts re-fetched via `id_list`, 0 failures; classification unchanged.
- Hugging Face Daily Papers:获取成功(100 篇),带 githubRepo 的相关论文均已在前两日报告覆盖(如 [DONIC](https://arxiv.org/abs/2610.29997)、[FRED](https://arxiv.org/abs/2610.30320)、[AgenticRoboRL](https://arxiv.org/abs/2610.28589)、[MambaAct](https://arxiv.org/abs/2610.22951)、[SpatialScout](https://arxiv.org/abs/2610.26659)、[LaLa-World](https://arxiv.org/abs/2610.27851))。 / No new relevant HF papers.
- GitHub radar:已更新(`date_taipei=2026-10-26`,star 基准 2026-10-24 23:17 UTC);counts: new_repos 254, tracked 1652, with_growth 266, **watchlist_releases 0**, **oss_signals 0**。 / Radar fresh.
- 推送权限:`git push --dry-run origin HEAD:main` 成功。 / Push permission OK.
- 入选论文 / Selected: 0 篇新论文。

---

## 今日必读 / Top Picks

🇨🇳 今日无新论文;以下为值得关注的开源进展。 / No new papers; below are the notable code-release updates.

1. **[NEXUS](https://arxiv.org/abs/2609.39000)** — 运动控制·RL。✅ 已开源(训练管线与 G1 预训练模型已在仓库;sim-to-sim / sim-to-real 部署模块似乎尚未上线)。 / Perceptive whole-body teleoperation for humanoids: terrain-aware motion adaptation package, teacher-student training pipeline and a G1 ONNX policy are in the repo; deployment code looks pending.
2. **[DONIC](https://arxiv.org/abs/2610.29997)** — 运动控制·RL。✅ 部分开源(仅 BiHOI 处理管线,训练/评测代码、检查点、数据集仍标 coming soon),状态与 10-24 相同。 / Still partial: only the BiHOI pipeline is out.
3. **[Memory before Goal (WholeBodyMem)](https://arxiv.org/abs/2610.31166)** — 运动控制·RL。🕒 计划开源:HuMeGo 数据集已上线,代码与模型仍 "Coming soon",状态与 10-25 相同。 / Dataset out, code and models still "Coming soon".

---

## 运动控制·RL / Motion Control · RL

*本类今日无新论文,仅更新开源状态(详细内容见 10-24 日报)。 / No new papers; code-status updates only (full write-ups in the 10-24 report).*

### [NEXUS: Perceptive Whole-Body Control for Terrain-Adaptive Teleoperation](https://arxiv.org/abs/2609.39000)(Gamma-Robot;arXiv 2026-09-30;GitHub 仓库 2026-10-23 新建,9★)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Gamma-Robot/NEXUS);匿名 `git ls-remote` 验证存在;README "Release Status" 列出地形运动适配包、训练管线、G1 ONNX 预训练模型、文档、sim-to-sim/sim-to-real 部署五项,从页面内容看前四项已提供,部署项未见相应目录;输入的重定向运动数据需自备(仅含示例动作)
- 🇨🇳 问题:人形全身遥操作需要机器人在与操作者不同的地形上复现其行为,而同一行为跨平地与不同地形的配对运动数据稀缺。方法:提出可扩展的地形感知运动适配算法自动生成配对数据,用约 1000 小时语料以教师—学生学习训练感知式全身控制器。结果:摘要称其在行为覆盖、地形适应与跟踪精度上优于现有全身控制器,并在真机上零样本实现多种未见地形的实时全身遥操作。
- 🇬🇧 Problem: whole-body humanoid teleoperation across mismatched terrains lacks paired motion data. Method: a scalable terrain-aware adaptation algorithm generates paired data (~1,000 hours) used to train a perceptive whole-body controller via teacher–student learning. Results: the abstract reports better behavioral coverage, terrain adaptability and tracking fidelity than existing controllers, plus zero-shot real-world real-time teleoperation on unseen terrains.

### [DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations](https://arxiv.org/abs/2610.29997)(Ropedia;状态更新)
开源状态 / Code: ✅ 部分开源 / Partially released — [仓库](https://github.com/Ropedia/DONIC);目前仅 `bihoi_pipeline/` 处理管线;DONIC 训练与评测代码、策略检查点、BiHOI 数据集仍标 coming soon(WebFetch 核对,与 10-24 一致)
- 🇨🇳 摘要要点:首个跨操作类别与人体运动来源联合训练的通用双手灵巧跟踪器,配套 BiHOI 数据集(1,575 条序列、229 个物体);PPO 与行为克隆形成反馈闭环,单一检查点在训练物体的未见轨迹上成功率 86.79%、在留出物体上 57.32%,分别比最优基线高 77.36 与 45.73 个百分点。
- 🇬🇧 Abstract recap: the first generalist bimanual dexterous tracker, trained with PPO plus behavioral cloning in a feedback loop on the new BiHOI dataset (1,575 sequences, 229 objects); one checkpoint reaches 86.79% on unseen trajectories of training objects and 57.32% on held-out objects, beating the best baselines by 77.36 and 45.73 points.

### [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation (WholeBodyMem)](https://arxiv.org/abs/2610.31166)(状态更新)
🏷️ 交叉方向 / Also: VLA, 具身智能 / Embodied AI(归入运动控制:目标任务是人形全身移动操作策略)
开源状态 / Code: 🕒 计划开源 / Planned — [仓库](https://github.com/crystalccy1/MemoryBeforeGoal);HuMeGo 数据集(LeRobot v2.1 格式,CC BY 4.0,6 个仿真任务 + 6 个 Unitree G1 真机任务)已在 Hugging Face 提供,README 的 "Code and models" 一节仅写 "Coming soon"
- 🇨🇳 摘要要点:对象引导的感知记忆让全身 VLA 策略保留动作前的物体事件关键帧,基础策略成功率在仿真中由 29.1% 提升到 72.6%,真机由 36.7% 提升到 88.3%。
- 🇬🇧 Abstract recap: object-guided perceptual memory raises the base whole-body VLA policy from 29.1% to 72.6% in simulation and from 36.7% to 88.3% on the real robot.

另已核实、无状态变化 / Verified, unchanged: [ReactiveBFM](https://arxiv.org/abs/2606.30362) ✅ [zjwzcx/ReactiveBFM](https://github.com/zjwzcx/ReactiveBFM);[HEX](https://arxiv.org/abs/2604.07993) ✅ [Open-X-Humanoid/HEX](https://github.com/Open-X-Humanoid/HEX)(187★,+12/日);[STAMP](https://arxiv.org/abs/2610.30817) ❓ 项目页 "Code" 无链接;[AgenticRoboRL](https://arxiv.org/abs/2610.28589) ✅ [仓库](https://github.com/xinxinliu-ai/AgenticRoboRL);[RangeNav](https://arxiv.org/abs/2610.29845) 🕒 "will be open-sourced"。运动控制·RL 类共 19 条已在 10-24 日报展开。 / The 19 motion-control·RL items were expanded on 10-24.

## 运动控制·传统 / Motion Control · Classical

今日无新论文。该类 7 条已在 10-24 日报展开。 / No new papers; 7 items were expanded on 10-24.

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

今日无新论文。 / No new papers.

## VLA

今日无新论文。另:[FluxVLA](https://github.com/FluxVLA/FluxVLA)、[FastHarness](https://github.com/FastHarness/fast-harness)、[MambaAct](https://github.com/giakhuyendihoc/MambaAct) 仓库匿名可访问;[SmolVLA-MoE](https://arxiv.org/abs/2610.30732) 声称的仓库 `dudu435/smolvla-moe` 匿名不可访问,待核实。 / No new papers. The SmolVLA-MoE repo link is not anonymously accessible (to be verified).

## VLN

今日无新论文。 / No new papers.

## 世界模型与 WAM / World Models & WAM

今日无新论文。GitHub 侧:[MinghaoFu/lewam](https://github.com/MinghaoFu/lewam)(LeWAM,基于 JEPA 的世界-动作建模,339★,+11)与 [PedroMarinhoDev/ComfyUI-Hy-Nomas](https://github.com/PedroMarinhoDev/ComfyUI-Hy-Nomas)(Hy-Nomas 视频世界模型的 ComfyUI 封装,9★,第三方)有动静。 / GitHub only: LeWAM (+11★) and a third-party ComfyUI wrapper for Hy-Nomas.

另见 / See also: [DiffDreamer](https://arxiv.org/abs/2610.31617)(已归入运动控制·RL);[DRILL](https://arxiv.org/abs/2610.30814)(世界模型用于 VLA 的 RL 后训练,10-24 日报归入运动控制·RL)。

## 空间智能与 SLAM / Spatial Intelligence & SLAM

今日无新论文。新仓库:[dotb1ue/GenSfm](https://github.com/dotb1ue/GenSfm)(标注 NeurIPS 2026,生成式 SfM,3★)。 / No new papers; one new repo (GenSfm).

## 其他值得关注 / Other Notable

- 第三方复现潮 / Reproduction wave: 围绕 SuperMimic 出现多个非官方复现仓库(见下方监测小节),其中 [Motphys/Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic)(128★,+18/日)最活跃。 / Many unofficial SuperMimic reproductions.

---

## GitHub 动态 / GitHub Highlights

**star 增长(相对 2026-10-24 23:17 UTC 基准,仅列相关)/ Star growth (relevant only)**

| 仓库 / Repo | ★ | Δ | 说明 / Note |
|---|---|---|---|
| [Motphys/Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) | 128 | +18 | 🇨🇳 SuperMimic 在 UniLab 上的独立复现(人形全身运动跟踪)。 🇬🇧 Independent SuperMimic reproduction on UniLab. |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28464 | +20 | 🇨🇳 无 release,持续增长。 🇬🇧 No release in window. |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 15876 | +19 | 🇨🇳 无 release。 🇬🇧 No release in window. |
| [Open-X-Humanoid/HEX](https://github.com/Open-X-Humanoid/HEX) | 187 | +12 | 🇨🇳 人形全身 VLA 框架。 🇬🇧 Whole-body humanoid VLA framework. |
| [MinghaoFu/lewam](https://github.com/MinghaoFu/lewam) | 339 | +11 | 🇨🇳 JEPA 世界与动作联合建模。 🇬🇧 JEPA world+action modeling. |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 8468 | +11 | 🇨🇳 无 release。 🇬🇧 No release in window. |
| [JethroJames/awesome-robots-icl](https://github.com/JethroJames/awesome-robots-icl) | 192 | +18 | 🇨🇳 机器人上下文学习综述配套清单。 🇬🇧 Companion list for an in-context-learning-for-robots survey. |

(榜首的 gods-eye-view、oomwoo、text-to-cad、RuView 等与本关注主题关系弱,忽略。 / Top-ranked unrelated repos ignored.)

**新仓库(48 小时内,筛选后)/ New repos (filtered)**
- [Gamma-Robot/NEXUS](https://github.com/Gamma-Robot/NEXUS)(9★)— 见上。 / See above.
- [crystalccy1/MemoryBeforeGoal](https://github.com/crystalccy1/MemoryBeforeGoal)(3★)— 见上。 / See above.
- [jackzedgar/SuperDex](https://github.com/jackzedgar/SuperDex)(2★)— 受 SuperMimic 启发的可微世界模型灵巧操作探索,非官方。 / SuperMimic-inspired differentiable-world-model dexterous manipulation, unofficial.
- [StefanoCapezzone/cadi-rialzati-cammina](https://github.com/StefanoCapezzone/cadi-rialzati-cammina)(1★)— Unitree G1 在 MuJoCo 中用 RL 学走路,个人项目。 / Personal G1 RL-walking project.
- [chao142857/legged-robot-learning](https://github.com/chao142857/legged-robot-learning)(1★)— 足式 locomotion/全身控制 RL 学习仓库。 / Legged RL learning repo.
- 其余新仓库多为个人作业或营销,忽略。 / The rest is noise.

**新 release / New releases:** 监测列表 releases 0 条(watchlist_releases 为空),无可报告的更新。 / None in window.

---

## 今日趋势 / Today's Trends

1. **SuperMimic 复现潮 / SuperMimic reproduction wave。** 🇨🇳 radar 的监测检索在 3 天内找到 15+ 个名称含 SuperMimic 的第三方仓库(Isaac Lab、MuJoCo、Apple M5、LocoMuJoCo 等多平台),说明社区在快速验证"可微世界模型 + 人形全身控制"。 🇬🇧 The radar found 15+ third-party SuperMimic repos across platforms in three days, showing fast community validation of differentiable-world-model humanoid control. 代表:[Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic)、[allmimic](https://github.com/Shimingyi/allmimic)。
2. **开源节奏 / Release cadence。** 🇨🇳 多个运动控制工作采用"先放数据/管线,代码稍后"的分批开源(DONIC、WholeBodyMem),NEXUS 则已放出训练管线与预训练模型。 🇬🇧 Staged releases (data/pipeline first) are common; NEXUS already ships training code and a pretrained policy.

---

## 关键词建议 / Keyword Suggestions

**建议新增 / Add:** 今日无建议 / No suggestions today(无新增论文,不足以支撑新词)。

**建议观察 / Watch:**
- `differentiable world model` — 🇨🇳 适用于 arXiv 与 GitHub:SuperMimic 复现潮及 [SuperDex](https://github.com/jackzedgar/SuperDex)、[DiffDreamer](https://arxiv.org/abs/2610.31617) 同时出现,再看几天。 🇬🇧 For arXiv and GitHub: SuperMimic repros, SuperDex and DiffDreamer all use it; watch a few more days.

**建议移除/收窄 / Remove or Narrow:** 无 / None.

---

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 | 当前状态 | 今日检查 | 备注 |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 | signal=false,errors 空,arXiv 最新版 v1,项目页无发布声明 | 15+ 第三方复现(如 [allmimic](https://github.com/Shimingyi/allmimic) 9★、[Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) 128★),均非官方,不据此判定已开源 |

**建议加入监测 / Suggested additions**
- **DONIC** — 🇨🇳 运动控制·RL 高价值,训练代码与检查点仍 coming soon。 🇬🇧 High-value motion-control work; training code and checkpoints pending.
```json
{"name": "DONIC", "title": "DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations", "arxiv_id": "2610.29997", "search_terms": ["DONIC", "BiHOI"], "owners": ["Ropedia"], "project_pages": [], "known_repos": ["Ropedia/DONIC"]}
```
- **WholeBodyMem (Memory before Goal)** — 🇨🇳 人形移动操作,代码与模型 "Coming soon"。 🇬🇧 Humanoid loco-manipulation; code and models "Coming soon".
```json
{"name": "WholeBodyMem", "title": "Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation", "arxiv_id": "2610.31166", "search_terms": ["WholeBodyMem", "HuMeGo"], "owners": ["crystalccy1"], "project_pages": ["https://memory-before-goal.github.io"], "known_repos": ["crystalccy1/MemoryBeforeGoal"]}
```

**建议移出 / Suggested removals:** 无 / None.

---
*自检 / Self-check:* ① 今日无新增论文,无需展开;② 无"未读"占位;③ 展开条目均含开源状态行;④ 优先级 3–7 类别无新增条目;⑤ 已运行 arXiv API 检索并记录命中数;⑥ 无 release;⑦ 链接格式已脚本扫描。
