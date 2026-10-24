# 机器人/具身智能每日速递 — 2026-10-25 / Robotics & Embodied AI Daily — 2026-10-25

**检查窗口 / Window:** 台北时间 2026-10-24 ~07:40 → 2026-10-25 ~07:40(周日)。arXiv 周末不发布新列表;GitHub 取 radar 数据 `date_taipei=2026-10-25`(生成于 2026-10-24 23:17 UTC,star 基准 2026-10-23 23:19 UTC)。 / Taipei time; arXiv publishes no list on weekends; GitHub from radar snapshot dated 2026-10-25.

**来源状态 / Source status**
- arXiv cs.RO `new` 列表:页面仍显示 2026-10-23(周五)列表(New 63 / Cross 6 / Replacements 38),与昨日报告完全相同,**本窗口 0 条新增**,不重复展开。 / The cs.RO page still shows Friday 23 Oct (63/6/38), identical to yesterday's report: 0 new entries in this window.
- arXiv API 关键词检索(cs.RO/cs.AI/cs.LG/cs.CV,按 submittedDate 降序,保留 max(published, updated) ≥ 2026-10-22 18:00 UTC,即昨日列表截止之后)命中数 / hits: embodied 0, VLA 0, vision-language-action 0, VLN 0, vision-language navigation 0, humanoid 0, legged locomotion 0, whole-body control 0, MPC 0, model predictive control 0, reinforcement learning robot 0, sim-to-real 0, dexterous manipulation 0, robot foundation model 0, world model 0, world action model 0, WAM 0, video world model 0, spatial intelligence 0, spatial reasoning 0, SLAM 0, visual SLAM 0, LiDAR SLAM 0, gaussian splatting SLAM 0, 3D reconstruction 0, motion tracking 0, motion imitation 0, locomotion 0, quadruped 0, robot manipulation policy 0。核对:`cat:cs.RO` 按提交时间降序,API 中最新一条为 2026-10-22 17:59 UTC,说明周五之后的提交尚未入库,将出现在周一列表中。 / Sanity check: the newest cs.RO entry in the API is 2026-10-22 17:59 UTC, so post-Friday submissions are not yet indexed and will appear on Monday's list.
- Hugging Face Daily Papers:获取成功(100 篇,最新发布日期 2026-10-22,周末无新增)。筛出 5 篇与关注主题相关、但昨日报告未覆盖的 10-20/21 日论文(下文「补充」),均已用 arXiv API 取得完整摘要与 Comments(5/5,0 失败)。 / HF OK; 5 relevant carry-over papers not in yesterday's report, all with full abstracts (5/5).
- GitHub radar:已更新(`date_taipei=2026-10-25`);new_repos 150 条(counts 报 267 条),tracked 1662,with_growth 296,watchlist_releases **0 条**,oss_watch 1 项(signal=false,errors 空)。 / Radar fresh; no watchlist releases in window.
- 入选篇数 / Selected: 5(全部为补充项,全部取得完整摘要)。

---

## 今日必读 / Top Picks

1. **[Memory before Goal (WholeBodyMem)](https://arxiv.org/abs/2610.31166)** — 运动控制·RL。🕒 计划开源(状态更新:数据集已上线,代码与模型 "Coming soon")。 / 昨日标"未知",今日官方仓库与 HuMeGo 数据集已发布,代码待放出。 / Status change: dataset and official repo are now live, code and models still "coming soon".
2. **[HyperDrone](https://arxiv.org/abs/2610.28950)** — 运动控制·RL(sim-to-real)。❓ 未知。 / 比现有批量四旋翼仿真器快 20 倍以上,纯仿真训练的视觉偏航策略直接上真机 Crazyflie(CoRL 2026)。 / 20× faster batch quadrotor simulator; vision-based policy trained purely in sim runs onboard a real Crazyflie (CoRL 2026).
3. **[Agentic World Action Models (AW-0)](https://arxiv.org/abs/2610.30136)** — 世界模型与 WAM。❓ 未知。 / 把代码规划与视频+动作联合预测放进同一个 WAM,在 RoboTwin 2.0 与真机双臂任务上优于 VLA/WAM 基线。 / Unifies code-based planning with joint video-action prediction in one WAM.

---

## 运动控制·RL / Motion Control · RL

*本类今日共 2 条详细条目(无 arXiv 新论文;1 条状态更新、1 条补充论文),另有第三方复现见监测小节。 / 2 expanded items today.*

### [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation (WholeBodyMem)](https://arxiv.org/abs/2610.31166)(MBZUAI 等;昨日已详述,今日为开源状态更新)
🏷️ 交叉方向 / Also: VLA, 具身智能 / Embodied AI(归入运动控制:目标任务是人形全身移动操作策略)
开源状态 / Code: 🕒 计划开源 / Planned — [仓库](https://github.com/crystalccy1/MemoryBeforeGoal);README 的 "Code and models" 一节写 "Coming soon";HuMeGo 数据集(6 个仿真 + 6 个真机 Unitree G1 任务,LeRobot v2.1 格式,CC BY 4.0)已发布在 [Hugging Face 集合](https://huggingface.co/collections/ChenyuanC/humego-6ada5cbea74d4cc678c91c68);匿名 `git ls-remote` 验证仓库存在
- 🇨🇳 问题:动态场景下人形移动操作是非马尔可夫的,线索会因物体变化、遮挡或转身离开视野而消失,而全身 VLA 策略只看当前观测。方法:WholeBodyMem 用 SAM3 跟踪任务物体,由物体事件在自适应预算内因果地选出关键帧,动作专家通过交叉注意力读取这些帧及编码外观、几何与时间的物体 token,并提出 HuMeGo 基准。结果(昨日摘要):基础策略成功率在仿真中从 29.1% 升至 72.6%,真机 Unitree G1 从 36.7% 升至 88.3%,标准 SIMPLE 任务从 70.2% 升至 86.9%。今日变化:官方仓库与数据集上线,训练/推理代码和模型仍未放出。
- 🇬🇧 Problem: humanoid loco-manipulation in dynamic scenes is non-Markovian, yet whole-body VLA policies see only the present. Method: WholeBodyMem tracks task objects with SAM3, causally selects key frames under an adaptive budget from object events, and lets the action expert read them via cross-attention with object tokens; the HuMeGo benchmark is introduced. Results (from the abstract): success rises from 29.1% to 72.6% in simulation, from 36.7% to 88.3% on a real Unitree G1, and from 70.2% to 86.9% on SIMPLE tasks. Change today: the official repo and datasets are live, while code and models are still marked "coming soon".

### [HyperDrone: Simulation-to-Reality Transfer at Millions of Frames per Second](https://arxiv.org/abs/2610.28950)(机构摘要未给出;Comments: Accepted at CoRL 2026;arXiv 2026-10-20,HF Daily 2 upvotes)
🏷️ 交叉方向 / Also: 空间智能与 SLAM(高保真光线追踪渲染)。归入运动控制·RL:核心用途是批量仿真训练视觉控制策略并 sim-to-real,非单纯渲染工作。
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 均无代码链接或承诺
- 🇨🇳 问题:基于视觉的四旋翼策略需要海量带高保真渲染的仿真数据,现有批量四旋翼仿真器渲染速度成为瓶颈。方法:HyperDrone 把高度优化的多旋翼动力学与新的光线追踪引擎 HyperLux 全部放在 GPU 上运行,HyperLux 支持 Nvidia OptiX、Vulkan、Apple Metal 和 WebGPU 后端,可渲染 RGB、深度、语义/实例分割、法线与光流,并支持反射、光照、运动模糊、PBR 等。结果:比现有最先进批量四旋翼仿真器快 20 倍以上,在最高保真设置下于消费级 GPU 上仍达每秒百万帧;完全在仿真中训练视觉偏航控制策略,并迁移到带相机、全程机载运行的小型真机 Crazyflie。预印本摘要未给出更多定量结果。
- 🇬🇧 Problem: vision-based quadrotor policies need huge amounts of high-fidelity simulated data, and rendering throughput in existing batch quadrotor simulators is the bottleneck. Method: HyperDrone runs optimized multirotor dynamics and the new ray-tracing engine HyperLux entirely on the GPU, with OptiX, Vulkan, Metal and WebGPU backends and RGB, depth, segmentation, normals and optical-flow outputs with reflections, motion blur and PBR. Results: more than 20× faster than the state-of-the-art batch quadrotor simulators, with millions of FPS on consumer GPUs even at the highest fidelity; a vision-based yaw-control policy trained purely in simulation transfers to a real Crazyflie with an onboard camera running fully onboard. No further quantitative results in the abstract.

---

## 运动控制·传统 / Motion Control · Classical

今日无新条目。 / No new items today.

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

*本类今日共 2 条,全部展开。 / 2 items, all expanded.*

### [TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments](https://arxiv.org/abs/2610.30043)(浙江大学等;arXiv 2026-10-21)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/xuyicheng-zju/TARSphere);Comments 给出代码与[项目页](https://xuyicheng-zju.github.io/TARSphere/);匿名 `git ls-remote` 验证存在
- 🇨🇳 问题:现有具身智能体系统多聚焦既定目标或把执行抽象成符号动作,难以在不断变化的物理与社会环境中评测。方法:TARSphere-Infra 在物理仿真器中运行机器人策略,带具身 NPC 与受限对话,并用事件驱动有限状态机更新任务状态;TARSphere-Harness 让冻结的多模态大模型通过多层可执行技能、分层记忆与执行反馈修正决策;据此构建 TARSphere-Bench(30 个室内场景共 360 个 episode,5 种配对条件)。结果:评测 8 个 MLLM,发现通用模型可优于具身模型,任务更新与人机交互仍困难,频繁碰撞和跌倒说明应同时评测执行安全性。
- 🇬🇧 Problem: embodied-agent systems often target fixed goals or reduce execution to symbolic actions, so evolving physical and social settings go unevaluated. Method: TARSphere-Infra runs robot policies in a physics simulator with embodied NPCs and an event-driven FSM; TARSphere-Harness lets a frozen MLLM act through multi-level skills, hierarchical memory and execution feedback; TARSphere-Bench has 360 episodes over 30 indoor scenes under five paired conditions. Results: across 8 MLLMs, general-purpose models can beat embodied ones, task updates and human interaction remain hard, and frequent collisions and falls motivate evaluating execution safety alongside success.

### [Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use](https://arxiv.org/abs/2610.30108)(showlab;综述;arXiv 2026-10-21,HF Daily 22 upvotes)
🏷️ 交叉方向 / Also: 其他 / Other(综述,无控制贡献)
开源状态 / Code: ✅ 已开源 / Released — [Awesome 列表仓库](https://github.com/showlab/Awesome-Multimodal-Embodied-Agent);仅为文献整理(Comments: Project website 给出[项目页](https://showlab.github.io/Awesome-Multimodal-Embodied-Agent/))
- 🇨🇳 内容:提出 PAPAV 框架(感知、预判动作效应、规划、行动、验证五种能力),以此比较计算机使用智能体、机器人系统与多模态具身智能体(MMEA),并总结从部分可观测到结果难验证的五种物理约束。结论:在 64 个基准中,显式评测集中在 Act,仅 5 个评测 Anticipate、3 个评测 Verify,这两项被任务成功率掩盖;文中据此给出开放挑战。
- 🇬🇧 Content: the survey proposes PAPAV (Perceive, Anticipate, Plan, Act, Verify) to compare computer-use agents, robotic systems and multimodal embodied agents, and lists five physical constraints from partial observability to unverifiable outcomes. Conclusion: across 64 benchmarks evaluation centers on Act, with only 5 assessing Anticipate and 3 assessing Verify, so both are hidden behind task success; open challenges follow.

---

## VLA

今日无新条目。 / No new items today.

## VLN

仅 1 条列名(1 条总计)/ 1 item, name only: [NavJev](https://github.com/Kai-Sheng-caesar/NavJev-Code)(同济大学;高效 VLN,论文 [2609.34969](https://arxiv.org/abs/2609.34969);官方代码仓库今日出现在 radar new_repos,未取摘要,不展开)。

---

## 世界模型与 WAM / World Models & WAM

*展开 1 条;另列名 3 条(共 4 条)。 / 1 expanded, 3 name-only (4 total).*

### [Agentic World Action Models (AW-0)](https://arxiv.org/abs/2610.30136)(机构摘要未给出;arXiv 2026-10-21,HF Daily 22 upvotes)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI, VLA。未归运动控制:贡献是双臂操作的 WAM 规划-预测框架,摘要未涉及人形/足式控制策略 RL。
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅给出[项目页](https://agentic-wam.github.io/),无代码链接或承诺
- 🇨🇳 问题:世界动作模型提供视觉预见,却缺少可复用技能的组合机制;而基于代码规划的 agentic 机器人又缺少对物理动态的预测。方法:AW-0 在统一 mixture-of-transformers 中把代码、未来视频、机器人动作作为三个耦合生成流,代码专家生成参数化技能例程和控制逻辑,视频与动作专家生成未来视觉状态与底层电机指令;另有自动标注管线把机器人与人类视频轨迹对齐到程序并整合成技能库。结果:在 RoboTwin 2.0 和真机双臂任务上优于 VLA 与 WAM 基线,并在语言跟随、语义推理与鲁棒性上有提升;预印本摘要未给出具体数值。
- 🇬🇧 Problem: world action models give visual foresight but lack compositional skill reuse, while agentic code-planning robots lack predictive grounding. Method: AW-0 models code, future video and actions as three coupled streams in a mixture-of-transformers, with a code expert for parameterized skill routines, video and action experts for future states and motor commands, and an automatic pipeline that aligns programs to robot/human videos into skill libraries. Results: better than VLA and WAM baselines on RoboTwin 2.0 and real bimanual tasks, with gains in language following, semantic reasoning and robustness; the abstract gives no numbers.

**列名 / Name only(3):** [LeWAM](https://github.com/MinghaoFu/lewam)(JEPA 端到端世界-动作建模,论文 [2610.12818](https://arxiv.org/abs/2610.12818),仓库 328★ +10)· [World-in-Context](https://github.com/aigc3d/World-in-Context)(Alibaba,交互式视频世界模型的 In-Context Conditioning,新仓库)· [FRED](https://github.com/suhyeok-jang/FRED)(昨日已详述)

---

## 空间智能与 SLAM / Spatial Intelligence & SLAM

*展开 1 条;另列名 1 条(共 2 条)。 / 1 expanded, 1 name-only.*

### [SpatialBrain: Spatial Intelligence Growing from Experience](https://arxiv.org/abs/2610.29317)(机构未给出;cs.AI;arXiv 2026-10-21,HF Daily 17 upvotes)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接或承诺
- 🇨🇳 问题:空间推理不仅需要几何工具,还要决定何时直接观察、何时重建、测量或换参考系。方法:SpatialBrain 固定视觉-语言骨干,用 3DFusionMemory 把当前场景观测融合为可查询的空间关系,用空间技能库提供可复用工具流程,再用 Spatial Cognition 把任务条件与"何时、如何使用记忆和技能"的经验关联,并把已完成轨迹抽象成过程记录、在任务块之间整合。结果:在五个空间推理基准上,四个优于同一骨干的直接回答,一个持平;摘要未给出具体数值。
- 🇬🇧 Problem: spatial reasoning needs a decision on when direct observation suffices and when to reconstruct, measure or change reference frames. Method: with a frozen vision-language backbone, SpatialBrain fuses observations into queryable relations (3DFusionMemory), keeps a Spatial Skill Library, and uses Spatial Cognition to link task conditions to experience, consolidating trajectories into process records. Results: better than the same backbone's direct answers on four of five spatial-reasoning benchmarks and tied on the fifth; no numbers in the abstract.

**列名 / Name only(1):** [GenSfM](https://github.com/dotb1ue/GenSfm)(HKU,NeurIPS 2026,原生 3D 扩散的生成式 SfM;仓库与 [HF 模型](https://huggingface.co/dotblue/GenSfm)已发布,arXiv 链接 coming soon)

---

## 其他值得关注 / Other Notable

今日无新条目。 / None.

---

## GitHub 动态 / GitHub Highlights

**Star 增长(相对 2026-10-23 23:19 UTC 基准)/ Star growth**

| 仓库 / Repo | Stars | 增长 / Δ | 说明 / Note |
|---|---|---|---|
| [Motphys/Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) | 110 | +30 | SuperMimic 的第三方复现(UniLab,G1 动作跟踪,mjwarp/MuJoCo/Motrix 后端,含可微世界模型与策略);非官方 / third-party reproduction of SuperMimic |
| [dexmal/opendw](https://github.com/dexmal/opendw) | 979 | +18 | 面向动作条件具身智能的开源世界模型 / open-source action-conditioned world model |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 15857 | +19 | 通用物理仿真器 / physics simulator |
| [JethroJames/awesome-robots-icl](https://github.com/JethroJames/awesome-robots-icl) | 174 | +18 | 机器人 In-Context Learning 综述配套列表 / survey companion list |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 14379 | +10 | 监测重点项目 / watchlist project |
| [MinghaoFu/lewam](https://github.com/MinghaoFu/lewam) | 328 | +10 | JEPA 世界-动作模型 / JEPA world-action model |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 8457 | +10 | 监测重点项目 / watchlist project |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28444 | +9 | 监测重点项目 / watchlist project |

**新 release / New releases:** 窗口内监测重点项目 0 个 release(`watchlist_releases` 为空)。 / No watchlist releases in the window.

**新仓库精选 / Notable new repos(radar `new_repos`):** [MemoryBeforeGoal](https://github.com/crystalccy1/MemoryBeforeGoal)(已入运动控制·RL)· [TC635807/mjx-go2-training](https://github.com/TC635807/mjx-go2-training)(Go2 地形 locomotion,MJX + Brax PPO,个人项目)· [only-one-over/robocasa-control](https://github.com/only-one-over/robocasa-control)(个人插件)。其余多为个人作业或无实质内容,已忽略。 / Rest ignored as personal/low-content.

---

## 今日趋势 / Today's Trends

1. **SuperMimic 第三方复现井喷 / Third-party SuperMimic reproductions.** 官方代码尚未放出,但 radar 搜索已命中 15 个复现/适配仓库(如 [Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic)、[allmimic](https://github.com/Shimingyi/allmimic)),社区需求强烈。 / No official code yet, yet 15 reproduction repos already exist; demand is strong.
2. **运动控制论文开放数据先行 / Datasets before code.** WholeBodyMem 与 DONIC 均先放数据集或处理管线,训练代码"coming soon"。 / WholeBodyMem and DONIC both release data/pipelines first.
3. **周末静默 / Weekend lull.** arXiv 无新列表,周一将集中出现周五之后的提交。 / Expect a burst on Monday's list.

---

## 关键词建议 / Keyword Suggestions

今日无建议 / No suggestions today(无足够新信号;仅有一天周末数据)。

---

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 | 当前状态 | 今日检查结果 | 备注 |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 | signal=false;candidate_repos 空,项目页无 GitHub 链接/发布承诺,arXiv 最新版 v1,errors 空 | search_hits 15 个均为第三方复现(如 [Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic)、[allmimic](https://github.com/Shimingyi/allmimic)),不能据此判定为已开源 |

**建议加入监测 / Suggested additions**
- **WholeBodyMem(Memory before Goal)** — 昨日未知、今日变为"计划开源"(README: Code and models coming soon),运动控制·RL 高价值。 / Moved from unknown to planned; high-value humanoid control work.
```json
{"name": "WholeBodyMem", "title": "Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation", "arxiv_id": "2610.31166", "added": "2026-10-25", "status": "planned", "search_terms": ["WholeBodyMem", "MemoryBeforeGoal", "HuMeGo"], "owners": ["crystalccy1"], "project_pages": ["https://memory-before-goal.github.io"], "known_repos": ["crystalccy1/MemoryBeforeGoal"]}
```
- **DONIC** — 仓库仅放出 BiHOI 处理管线,训练代码/权重/数据 coming soon(见昨日报告)。 / Only the data pipeline is out; training code and weights are coming soon.
```json
{"name": "DONIC", "title": "DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations", "arxiv_id": "2610.29997", "added": "2026-10-25", "status": "planned", "search_terms": ["DONIC", "BiHOI"], "owners": ["Ropedia"], "project_pages": [], "known_repos": ["Ropedia/DONIC"]}
```

**建议移出 / Suggested removals:** 无 / None.
