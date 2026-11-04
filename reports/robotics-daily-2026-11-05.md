# 机器人/具身智能每日速递 — 2026-11-05 / Robotics & Embodied AI Daily — 2026-11-05

> **检查窗口 / Window**:台北时间 2026-11-04 07:40 → 2026-11-05 07:40(UTC+8,周四)。arXiv 取最新一期 cs.RO new 列表(列表日期 Wednesday, 4 November 2026);radar 数据 `date_taipei = 2026-11-05`(已更新)。
> **监测项状态 / Watchlist**:SuperMimic 今日 `signal=false`,仍未发现官方代码,状态保持「未知」;GitHub 上已出现多个第三方复现/衍生仓库(见末节)。无监测项开源。

## 来源状态 / Source Status

| 来源 / Source | 状态 / Status |
|---|---|
| arXiv cs.RO new 列表 | ✅ 成功:New 56 + Cross-lists 16 = 72 条已逐条分类;Replacements 53 条仅扫描、未逐条展开(按规则只看与主题相关且有实质更新者,仅凭列表无法判断实质更新)。 / 72 new+cross entries classified; 53 replacements not expanded. |
| arXiv API 取摘要/Comments | ✅ 73 篇(72 + 1 篇 API 额外命中)全部取得非空完整摘要(73/73);其中 41 篇 Comments 非空,已用 `<arxiv:comment>` 字段核对。 |
| arXiv API 关键词检索(cs.RO/AI/LG/CV,submittedDate 2026-11-03 18:00 → 2026-11-04 23:40 UTC) | ✅ 已运行。命中数:embodied 3, vision-language-action 1, VLA 1, humanoid 1, 3D reconstruction 1,其余 vision-language navigation / legged locomotion / whole-body control / model predictive control / reinforcement learning robot / sim-to-real / dexterous manipulation / robot foundation model / world model / world action model / video world model / spatial intelligence / spatial reasoning / SLAM / visual SLAM / LiDAR SLAM / gaussian splatting SLAM / motion tracking / motion imitation 均为 0。合并去重后仅新增 1 篇([2611.05376](https://arxiv.org/abs/2611.05376),非机器人核心,不展开)。说明:当天 arXiv API 的最新提交时间止于 2026-11-03 18:13 UTC,与本期 cs.RO 列表一致,故关键词检索命中很少,主要依据 cs.RO 列表。 |
| 入选篇数 | 约 55 篇判定相关(类别 1–7 及其他),其中详细展开 45 条(含 3 个 GitHub 仓库),其余列名。 |
| GitHub radar(`data/latest.json`) | ✅ new_repos 150 条(counts 显示共 285 条)、star_growth_top 60 条;star 基准 2026-11-03T23:12Z;watchlist_releases 1 条;oss_watch 1 项。 |
| Hugging Face Daily Papers | ✅ 100 条,机器人相关带 githubRepo 的仅 [RoboTryOn](https://arxiv.org/abs/2611.05163)(已开源),另有无仓库的高赞 [DreamX](https://arxiv.org/abs/2611.05377)(49 赞)。 |
| 项目主页 / git ls-remote | ✅ 已逐一核对声称开源的仓库(匿名 `git ls-remote`),均可访问。 |

## 今日必读 / Top Picks

1. **[ReflexArc](https://arxiv.org/abs/2611.04424)** — 运动控制·RL | 🕒 计划开源。把 10 ms 级触觉反射与 50 Hz 学习型人形全身控制结合,在 Unitree G1 上将接触冲量从 0.2632 N·s 降到 0.1225 N·s。 / Tactile reflex under 10 ms fused with a learned humanoid whole-body policy; contact impulse 0.2632 → 0.1225 N·s on G1.
2. **[HLO-AMP](https://arxiv.org/abs/2611.05113)** — 运动控制·RL | ❓ 未知。把底层 WBC 本身训练成"带物体的运动先验"(动作模仿 + 真实搬运负载),CoRL 2026,G1 双臂搬箱可泛化到不同质量/尺寸并能从中途掉落恢复。 / Trains the low-level WBC as an object-aware motion prior via imitation with the payload in the scene; CoRL 2026.
3. **[Online iLQR-MPC with Whole-Body Control for Robust Humanoid Locomotion](https://arxiv.org/abs/2611.04204)** — 运动控制·传统 | ❓ 未知。单刚体模型 iLQR-MPC 同时优化接触力与落脚点,100 Hz 重规划,G1 在仿真中承受 245 N / 175 N 推力恢复。 / Single-rigid-body iLQR-MPC jointly optimizes forces and footsteps; G1 recovers from 245 N / 175 N pushes in simulation.
4. **[GSBR](https://arxiv.org/abs/2611.05295)** — 运动控制·RL(manipulation 控制策略)| ✅ 已开源。Levine 组的在线 RL 正则化,19 个任务平均成功率 33% → 95%。 / Online-RL regularizer toward a base policy's support; average success 33% → 95% on 19 tasks.
5. **[PrimeSim](https://arxiv.org/abs/2611.04870)** — 世界模型与 WAM | 🕒 声称发布(无链接)。30,110 小时、22 个平台训练的动作条件多视角世界模型模拟器,可用于 GRPO 策略优化。 / Action-conditioned multiview world-model simulator trained on 30,110 h across 22 platforms.

---

## 运动控制·RL / Motion Control · RL

本类共 9 篇论文(ReflexArc、HLO-AMP、Latent Foresight、GSBR、CRONOS、PolicyIK、DexHOT、ARPG、WayTrace)+ 3 个 GitHub 仓库,全部展开。

### [ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control](https://arxiv.org/abs/2611.04424)
作者:Mingyu Wang, Si Li, Ziqing Chen, He Wang 等(机构摘要未给出)。Comments:8 pages, 6 figures。
🏷️ 交叉方向 / Also: 触觉感知 / Tactile sensing
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://minusmodulo.github.io/reflexarc-website/)上 Code 与 Paper 均标注 "Coming soon"
- 🇨🇳 人形机器人在杂乱环境中需要在首个冲击峰值(数十毫秒内)之前对意外接触作出反应,而 50 Hz 的学习型全身策略存在策略周期延迟,还可能把保护性撤回当作跟踪误差而压制。作者提出 ARC(Ascending Reflex Control):反射通路利用全身触觉检测危险接触、求解全身撤回姿态,并在 10 ms 内直接下发到电机;自底向上的反射整合包含 reflex-in-the-loop 策略学习、reflex-transparent 策略对齐和 reflex-informed 策略适应,使策略维持撤回、保持平衡并完成长时程恢复。在 Unitree G1 上评估三类危险接触:相比延迟 20 ms 的同款反射,首个力峰值降低 34.1%,接触冲量从 0.2632 N·s 降至 0.1225 N·s(2.15 倍)。还演示了受保护的动作跟踪、遥操作和基于足底触觉的无视觉越障。
- 🇬🇧 Humanoids in clutter must react to unexpected contact before the first impact peak, which arrives within tens of milliseconds, while 50 Hz learned whole-body policies add a policy-cycle delay and may treat a protective withdrawal as tracking error. ARC (Ascending Reflex Control) adds an instantaneous reflex pathway that detects hazardous contact from full-body tactile sensing, solves a withdrawal pose and sends it to the motors within 10 ms, plus bottom-up integration (reflex-in-the-loop policy learning, reflex-transparent alignment, reflex-informed adaptation) so the policy sustains the withdrawal and keeps balance. On a Unitree G1 across three hazardous-contact categories, it cuts the first force peak by 34.1% and the contact impulse from 0.2632 to 0.1225 N·s (2.15x) versus the same reflex delayed by 20 ms. Demos include protected motion tracking, teleoperation and vision-free obstacle traversal using foot tactile sensing.

### [HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors](https://arxiv.org/abs/2611.05113)
作者:Jean-Pierre Sleiman, Bilal Hammoud, He Li, Jonathan Foster 等。Comments:Accepted at CoRL 2026。
🏷️ 交叉方向 / Also: 动作模仿 / Motion imitation
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅给出视频链接,摘要无代码链接或承诺
- 🇨🇳 人形 loco-manipulation 的分层方案通常把任务无关的 WBC 与下游任务策略搭配,但 WBC 靠手工奖励塑形,动作机械,且训练时场景里没有被操作物体,只能用随机末端力扰动近似,无法复现真实负载在双臂与躯干上的分布式多接触力,在接近负载极限时差距尤其大。本文把底层控制器本身训练成"物体感知的运动先验":在重定向的动捕参考上做动作模仿、且物体真实存在于场景中,同时保留与命令跟踪 WBC 相同的紧凑任务空间接口;再训练无参考的高层策略,其动作通道被锚定在底层训练数据的经验包络内,从结构上避免查询导致底层越界。在 Unitree G1 双臂搬箱任务上,同一部署策略可泛化到不同物体质量与尺寸、初始与目标位姿,并能在搬运中途故意掉落后反应式恢复(摘要未给出具体成功率数字)。
- 🇬🇧 Hierarchical humanoid loco-manipulation usually pairs a task-agnostic WBC with a task policy, but such WBCs rely on manual reward shaping (machine-like motion) and are trained without the object, approximating payloads with random end-effector forces that miss the distributed multi-contact wrench, especially near payload limits. The paper trains the low-level controller itself as an object-aware motion prior via imitation of retargeted MoCap with the object physically present, keeping the same compact task-space command interface; a reference-free high-level policy is then trained on top with its action channel anchored to the empirical envelope of the low-level data. On a Unitree G1 bimanual box pick-and-place, the same deployed policy generalizes across object masses and dimensions and initial/goal poses and recovers reactively from intentional mid-carry drops; the abstract gives no quantitative success rates.

### [Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight](https://arxiv.org/abs/2611.04839)
作者:Ju Dong, Xinyu Xiao, Yiming Zhou, Tianshuo Yang 等。Comments:10 pages, including supplementary material。
🏷️ 交叉方向 / Also: 世界模型与 WAM / World Model & WAM
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://ju6276.github.io/Action-Grounded-Foresight/)标注 "Code coming soon"
- 🇨🇳 人形 loco-manipulation 需要身体运动与手部交互的时间协调,看似合理的命令序列仍可能掉落物体或交互未完成。作者提出动作条件潜空间前瞻:一个潜空间 WAM 在执行前评估候选命令序列——动作生成器从视觉、语言和机器人状态提出关节运动-手部命令序列;动作条件终点预测器估计各序列前缀到达的视觉特征并度量朝示教子目标的进度,联合时序先验给出时间一致性评分;机器人执行得分最高序列的前几步并重规划,训练时用动作一致性正则保留与动作相关的信息。在人形 loco-manipulation 仿真基准 SIMPLE 的 10 个任务上平均成功率 89.7%(Psi-Zero 73.7%,DiT4DiT 82.0%);7 个真机任务标准条件 85.7%、未见物体配置 65.7%,而 GR00T N1.7 分别为 70.0% 和 48.6%。
- 🇬🇧 Humanoid loco-manipulation needs coordinated body motion and hand interaction over time, and plausible-looking command sequences can still drop an object. The paper proposes action-conditioned latent foresight, a latent world-action model that scores candidate command sequences before execution: an action generator proposes joint-hand sequences, an action-conditioned endpoint predictor estimates reached visual features and progress toward a demonstration-derived subgoal, a temporal prior scores consistency, and the robot executes the first commands of the best sequence and replans, with action-consistency regularization in training. On 10 tasks of the SIMPLE humanoid benchmark it reaches 89.7% average success (Psi-Zero 73.7%, DiT4DiT 82.0%); on 7 real-robot tasks 85.7% standard and 65.7% unseen configurations versus 70.0% and 48.6% for GR00T N1.7.

### [GSBR: Geometric Support Behavior Regularization for Online RL](https://arxiv.org/abs/2611.05295)
作者:Charles Xu, Jacob Berg, Liyiming Ke, Sergey Levine 等。
🏷️ 交叉方向 / Also: 机器人基础模型 / Robot foundation models(预训练基策略)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/charlesxu0124/gsbr);摘要声明开源,匿名 `git ls-remote` 验证可访问;[项目页](https://charlesxu0124.github.io/gsbr/)
- 🇨🇳 把在线 RL 正则化到预训练基策略(通常是模仿学习得到的扩散/流匹配模型)可提升样本效率与稳定性,但现有正则要么(BC 正则)把 actor 拉向整个基策略分布、惩罚其舍弃次优模态,要么(硬支持约束)禁止刚好处在支持集之外的改进。GSBR 按动作到基策略支持集的距离施加惩罚:支持集内无惩罚,支持集外惩罚随距离平滑增长,但当价值增益足够大时仍允许改进;距离由有限个基策略样本估计,只需样本访问。在四个机器人基准的 19 个任务上,平均成功率从基策略的 33% 提升到 95%,在所有对比方法中成功率和吞吐最高,归一化吞吐比次优 RL 方法高约 23%。
- 🇬🇧 Regularizing online RL toward a pretrained base policy (typically an imitation-trained diffusion or flow-matching model) helps sample efficiency, but BC regularizers pull the actor toward the whole distribution and penalize dropping suboptimal modes, while hard support constraints forbid improvements just outside the support. GSBR penalizes actions by their distance from the base policy's support: no penalty inside, a smoothly growing penalty outside that still allows improvement when value gain outweighs it, estimated from a finite set of base-policy samples. Across 19 tasks on four robotic benchmarks it raises average success from 33% (base policy) to 95%, with the highest success and throughput among compared methods and about 23% higher normalized throughput than the next-best RL method.

### [CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation](https://arxiv.org/abs/2611.05080)
作者:Po-Yi Wu, Djengo Cyun-Jyun Fang, Dian Cheng, Tsung-Wei Ke 等。
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://embodiedai-ntu.github.io/cronos/),摘要与页面均未见代码链接或承诺
- 🇨🇳 现实世界 RL 常受限于频繁的场景重置需要人工介入;已有非回合式 RL 研究多针对从零训练的小策略,对微调大型预训练 VLA 的行为了解不足。CRONOS 是在非回合式场景重置下对 VLA 做 RL 微调的仿真基准,基于高保真物理模拟器并采用共享场景多任务设置。结果显示:在非回合式设置下朴素微调会因物体构型与末端位姿漂移而失败,但可通过有针对性的重置分配和处理预训练模型的偏置来缓解;非回合式训练还能增强长时程操作并改善对未见物体构型与任务序列的泛化。摘要未给出具体定量数字。
- 🇬🇧 Real-world RL is impractical with frequent scene resets that need human help, and prior non-episodic RL studied small policies trained from scratch rather than fine-tuning large pretrained VLAs. CRONOS is a simulation benchmark for RL fine-tuning of VLAs under non-episodic resets, built on high-fidelity physics simulators with shared-scene multi-task settings. Naive fine-tuning fails because object configurations and end-effector poses drift, but targeted reset allocation and correcting biases in pretrained models mitigate this; non-episodic training also improves long-horizon manipulation and generalization to unseen configurations and task sequences. The abstract gives no quantitative results.

### [PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning](https://arxiv.org/abs/2611.05372)
作者:Yuhan Liu, Xinqi Liu, Zixuan Dong, Keith W. Ross 等。
🏷️ 交叉方向 / Also: VLA(执行 π0.5 的末端指令)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/Tinaliu0123/PolicyIK);摘要声明,匿名 `git ls-remote` 验证可访问(radar new_repos 亦收录)
- 🇨🇳 精确 IK 因冗余与奇异性、依赖手调控制器以及真机数据昂贵而繁琐,而许多 VLA 依赖 IK 来跨本体迁移。PolicyIK 是目标条件 RL 策略:根据位姿反馈更新关节位置参考,并观测累积参考相对实测关节的偏移以保留静止时位置控制器所需的偏置;两尺度位姿误差配合与误差相关的动作增益解决毫米级残差,进度奖励与驻留奖励教会策略既到达容差又保持在容差内。仿真中 PPO 策略单次尝试在 93.5% 的留出任务上末段 1 秒平均误差保持在 1 mm 与 0.2° 以内,部署协议将成功率提高到 98.9%;直接在实体机械臂上用离策略 RL 训练,到达与保持成功率高于四种经典 IK 控制器;在仿真抓放中执行 π0.5 的末端指令成功率 95.7%。
- 🇬🇧 Precise IK is laborious due to redundancy and singularities, hand-tuned controllers and costly real-robot data, yet many VLAs rely on it. PolicyIK is a goal-conditioned RL policy that updates joint-position references from pose feedback and observes its accumulated reference relative to measured joints, uses two-scale pose errors with an error-dependent action gain for millimeter residuals, and progress/dwell rewards to reach and stay within tolerance. In simulation a single PPO attempt keeps final-second mean errors within 1 mm and 0.2° on 93.5% of held-out tasks (98.9% with a deployment protocol); trained directly on a physical arm with an off-policy learner it beats four classical IK controllers, and it executes π0.5 end-effector commands in simulated pick-and-place with 95.7% success.

### [DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation](https://arxiv.org/abs/2611.05119)
作者:Zhewei Gui, Anthony Bolton, Jiyao Zhang 等。Comments:9 pages, 4 figures。
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/dex-hot/DexHOT-Code);由[项目页](https://dex-hot.github.io/)链接,匿名 `git ls-remote` 验证可访问(摘要与 Comments 未单独给出链接)
- 🇨🇳 许多学习式灵巧操作系统只用物体位姿或轨迹指定目标,手-物构型只能隐式涌现。DexHOT 将灵巧操作表述为"手-物构型迁移":在联合描述手部关节与相对腕部物体位姿的可行构型之间移动;它从合成的可行构型对中学习可复用的关系条件迁移原语,无需人类参考动作,并通过对构型子目标的闭环跟踪组合长时程行为(摘要未说明具体训练算法)。在含 120 个物体的 DexHOTBench 上,单一策略对已见物体迁移成功率 80.5%、未见物体 69.4%;真实灵巧手 200 次迁移成功率 61.5%,六个示教引导任务的任务成功率 90%。
- 🇬🇧 Most learning-based dexterous systems specify goals by object pose or trajectory, leaving hand-object configurations to emerge implicitly. DexHOT casts manipulation as hand-object configuration transfer between feasible configurations jointly specifying hand articulation and object pose relative to the wrist, learns a reusable relation-conditioned transfer primitive from synthetic feasible pairs without human reference motion (the training algorithm is not stated in the abstract), and composes long-horizon behavior via closed-loop tracking of configuration subgoals. On DexHOTBench (120 objects) a single policy reaches 80.5% transfer success on seen and 69.4% on unseen objects; on a real dexterous hand it achieves 61.5% over 200 transfers and 90% task success over six demonstration-guided tasks.

### [LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation](https://arxiv.org/abs/2611.04974)
作者:Hong Je-Gal, Jinwoo Kim, Chanbin Yi, Hyun-Suk Lee。Comments:NeurIPS 2026。
开源状态 / Code: ❓ 未知 / Unknown — Comments 与摘要均无代码链接或承诺
- 🇨🇳 问题:从自然语言任务描述自动生成可执行的机器人 RL 策略;LLM 写出的代码即使可执行,也可能因状态、动作、奖励、终止条件语义不一致而得到"不可学习"的策略。方法:让 LLM 在部署前充当设计者,提出依赖感知的智能体框架 ARPG——MDP 建模按依赖顺序进行,配合局部验证与修正,并在建模固定后按模块化方式实现仿真器,同时外化中间产物。结果:在 Isaac Sim 中,ARPG 在建模正确性、环境可执行性和策略生成成功率上均优于整体式 LLM 基线与现成智能体系统(摘要未给出具体数字),并在自定义机器人、标准 RL 与工程领域 MDP 上演示了可复用性。
- 🇬🇧 Problem: generating executable robot RL policies from natural-language task descriptions, where executable code can still yield non-learnable policies when state, action, reward and termination artifacts are semantically misaligned. Method: LLMs act as pre-deployment designers in ARPG, a dependency-aware agentic framework that does sequential MDP modeling with localized verification and correction, then modular simulator implementation, externalizing intermediate artifacts. Results: in Isaac Sim it improves modeling correctness, environment executability and policy-generation success over monolithic LLM baselines and off-the-shelf agentic systems (no numbers in the abstract), with demos on custom robotics, standard RL and engineering MDPs.

### [WayTrace: A Map-to-Language-to-Trace Hierarchy for Embodied Urban Navigation](https://arxiv.org/abs/2611.05129)
作者:机构摘要未给出。Comments:Under Review。
🏷️ 交叉方向 / Also: VLN、具身智能 / Embodied AI(归入此类的理由:轮足机器人真机部署,底层由 RL 策略跟踪轨迹 / placed here because an RL tracking policy drives a wheeled-legged robot)
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://way-trace.github.io)仅标注 "Hugging Face Space · coming soon",未见代码链接
- 🇨🇳 网络地图提供几乎所有城市的步行导航,但自主机器人长距离可靠执行仍困难:点目标导航严重依赖准确 GNSS,多数 VLN 模型连室外短指令都难以执行。WayTrace 为分层系统:现成 VLM 读取逐向导航、卫星图与近期图像,逐条发出原子语言指令(如"向左过马路");机载轨迹预测器(在 100 多万自动标注的街景样本上训练)在图像中画出该指令的路径,再由强化学习策略跟踪。长程仿真任务中对 GNSS 噪声保持鲁棒,违规(离开人行横道/人行道)约比点目标基线少十倍;在轮足机器人上完成最长 1.37 km、约 1.1 m/s 的真实任务,覆盖繁忙市区、乡间小路与校园,可处理人行横道、楼梯和施工区。
- 🇬🇧 Web maps give walking directions for nearly every city, but following them over long routes is hard: point-goal policies need accurate GNSS and most VLN models struggle even with short outdoor instructions. WayTrace has an off-the-shelf VLM read turn-by-turn directions, a satellite map and recent images and issue one atomic language command at a time; an onboard trace predictor trained on over one million automatically labelled street-level samples draws the path in the image, and an RL policy tracks it. In long-range simulation it stays robust to GNSS noise with about ten times fewer violations than point-goal baselines, and on a wheeled-legged robot it completes real missions up to 1.37 km at about 1.1 m/s across a city centre, rural trails and a campus, handling crosswalks, staircases and construction sites.

### GitHub:[fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic)(★132,当日 +33;新建于 11-02)
🏷️ 交叉方向 / Also: 世界模型 / World model(可微世界模型)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/fuyichen0725/blinkmimic);匿名 `git ls-remote` 可访问;关联论文未见(第三方对 SuperMimic 范式的实现,非 SuperMimic 官方代码)
- 🇨🇳 问题:人形全身动作跟踪训练耗时长。方法:README 称其与 SuperMimic、InstantTrack 一样学习一个可微世界模型并对想象 rollout 反向传播训练策略,在 mjlab / MuJoCo Warp 上运行,并改变了策略优化方式与重置预算的分配。结果(README 自述):一个覆盖全部 40 段 LAFAN1(2.45 小时)的策略,在单张 RTX 4090 上 2.9 分钟(3 个种子均值)达到评估归一化回报 0.82,3.4 分钟达到 0.82 且 0/40 段失败。
- 🇬🇧 Problem: humanoid whole-body motion tracking is slow to train. Method: per the README, like SuperMimic and InstantTrack it learns one differentiable world model and trains the policy by backpropagating through imagined rollouts on mjlab / MuJoCo Warp, changing how the policy is optimized and where resets are spent. Results (self-reported in the README): one policy for all 40 LAFAN1 clips (2.45 h) reaches normalized evaluation return 0.82 in 2.9 min on one RTX 4090 (mean of 3 seeds) and 0.82 with 0/40 clips failed in 3.4 min.

### GitHub:[leggedrobotics/terrain-grounded-imagination](https://github.com/leggedrobotics/terrain-grounded-imagination)(★21;ETH 足式机器人组;新建于 11-03)
🏷️ 交叉方向 / Also: 世界模型 / World model
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/leggedrobotics/terrain-grounded-imagination);匿名 `git ls-remote` 可访问;README 称为论文 "Terrain-Grounded Imagination: A Recipe for Humanoid Locomotion on Sparse Terrain through World Models" 的代码(本期 arXiv 列表未见该论文)
- 🇨🇳 问题:稀疏地形(楼梯、间隙、踏石)上的人形行走训练。方法:世界模型只学习机器人对脚下地面的响应,地面、奖励与感知通过可微高度图查找从模拟器读取;策略使用足点门控感知(Watch Your Step)与足点预测模型,想象中在想象状态上运行以保持观测一致;策略通过 32 步想象反向传播回报并接 critic,并在支撑不良的着地处切断梯度。结果:README 描述训练 Unitree G1 完全通过学习到的世界模型在楼梯、间隙与踏石上行走;摘录中未给出定量数字。
- 🇬🇧 Problem: training humanoid walking on sparse terrain (stairs, gaps, stepping stones). Method: the world model learns only how the robot responds to the ground beneath it, while terrain, rewards and perception are read from the simulator heightmap through cheap differentiable lookups; the policy uses foothold-gated perception (Watch Your Step) with a foothold prediction model run on imagined states, backpropagates return through 32 imagined steps with a critic, and cuts gradients at poorly supported touchdowns. Results: the README describes a Unitree G1 learning to walk over stairs, gaps and stepping stones entirely through the learned world model; no quantitative numbers in the excerpt I read.

### GitHub:[lasgroup/generalist-improvement](https://github.com/lasgroup/generalist-improvement)(★1;新建于 11-04)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/lasgroup/generalist-improvement);匿名 `git ls-remote` 可访问
- 🇨🇳 问题:通用机器人策略的 RL 式持续改进。方法:该仓库是论文 "Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement" 的伴随代码,README 称为 π0.5 在 LIBERO-90 与 MolmoSpaces 上进行多任务后训练的最小实现,支持 filtered SFT(FSFT)、Best-of-N(BoN)与 OGPO 三种方式,基于 openpi 与 molmospaces 的 fork。结果:README 未给出定量结果;每个作业需要一个 4×GPU 节点(每卡约 100GB 显存)。
- 🇬🇧 Problem: RL-style improvement of generalist robot policies. Method: the repo accompanies "Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement" and, per its README, is a minimal implementation of multi-task post-training for π0.5 on LIBERO-90 and MolmoSpaces using filtered SFT (FSFT), Best-of-N (BoN) or OGPO, built on forks of openpi and molmospaces. Results: the README reports no quantitative results; each job needs one 4-GPU node with about 100 GB VRAM per GPU.

---

## 运动控制·传统 / Motion Control · Classical

本类共 11 篇,全部展开。 / 11 papers, all expanded.

### [Online iLQR-MPC with Whole-Body Control for Robust Humanoid Locomotion](https://arxiv.org/abs/2611.04204)
作者:Xiang Li, Linlin Ou, Ruihan Wu, Xinyi Yu。
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接或承诺
- 🇨🇳 人形行走需要同时决定落脚点与接触力分配,扰动会使名义规划失效,且约束随每次落脚切换。作者采用保留姿态动力学与完整接触力旋量的单刚体模型,用 iLQR-MPC 在单一滚动时域问题中联合优化接触力与落脚位置(无需独立步态规划器),通过增广拉格朗日与松弛障碍惩罚把接触与运动约束纳入后向传递;随后全身控制器以 500 Hz 将规划映射为关节力矩并保持接触可行。MuJoCo 仿真中 iLQR-MPC 以 100 Hz 重规划(平均求解 8.9 ms),Unitree G1 保持稳态行走并能从 245 N 前向与 175 N 侧向冲击推力中恢复;该方法无需平台特定的策略训练。
- 🇬🇧 Humanoid locomotion must decide where to step and how to distribute contact forces, yet disturbances invalidate the nominal plan and constraints switch with every footfall. The approach uses a single-rigid-body model with attitude dynamics and full contact wrench, and an iLQR-MPC that jointly optimizes contact forces and footstep locations in one receding-horizon problem without a separate step planner, with contact/motion constraints handled by augmented-Lagrangian and relaxed-barrier penalties in the backward pass; a whole-body controller maps the plan to joint torques at 500 Hz. In MuJoCo the MPC replans at 100 Hz (mean solve 8.9 ms) and the Unitree G1 sustains steady walking and recovers from 245 N forward and 175 N lateral impulsive pushes, with no platform-specific policy training.

### [Caging Vision-Language Navigation for Legged Robots via Barrier-Certified Safety Architecture](https://arxiv.org/abs/2611.04972)
作者:Abhijeet M. Kulkarni, Saimouli Katragadda, Yuze Du, Zijun Sha 等。
🏷️ 交叉方向 / Also: VLN、VLA(归入此类的理由:核心贡献是带可证明避碰的 MPPI+屏障函数规划,并在人形/四足真机验证 / placed here because the core contribution is MPPI + barrier-function planning validated on humanoid and quadruped hardware)
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接或承诺
- 🇨🇳 面向足式机器人的 VLA 式语言导航缺乏物理落地与显式安全保证。作者的思路是不放弃端到端 VLA 规划,而是"关笼子":高层 VLA 规划器之下接物理接地层,利用高效状态估计、原位 3D 空间感知与有符号距离场(SDF)生成可执行轨迹;导航规划器结合低维 Bezier 参数化 MPPI 与离散指数屏障函数(dEBF)约束,在所述假设下提供可证明的避碰保证。系统模块化,兼容多种 VLM/VLA 且与平台无关;在人形与四足机器人上做了大量真实实验,展示了高效、安全的视觉语言驱动导航(摘要未给出定量数字)。
- 🇬🇧 VLA-style language navigation for legged robots lacks physical grounding and explicit safety assurance. The paper augments rather than replaces end-to-end VLA planning: a high-level VLA planner sits above a physical-grounding layer using state estimation, in-situ 3D perception and an SDF to generate executable trajectories, with a Bezier-parameterized MPPI planner plus discrete exponential barrier function (dEBF) constraints giving provable collision avoidance under stated assumptions. The system is modular, compatible with various VLM/VLA models and platform-agnostic, and is validated in extensive real-world experiments on humanoid and quadrupedal robots (no numbers in the abstract).

### [Self-Consistent Neural Control: Learning Trajectories for Implicit Equilibrium](https://arxiv.org/abs/2611.03885)
作者:Hengyi Zhou, Haobo Fang, Xiaonan Huang, Dezhong Tong。
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接或承诺
- 🇨🇳 隐式平衡系统(如可变形物体)的响应多稳态、路径相关且对长时域敏感;伴随学习依赖"冻结切线"近似,在局部平衡快速变化时误差大。SCNC 在敏感度变化被显式控制的轨迹上做优化,推导了梯度误差的数学界并给出有限差分近似。在弹性杆、薄壁管、卷尺、Slinky 类结构上,相比伴随学习和无梯度 iCEM,收敛更快更稳定:稳定优化率从 41.7% 提升到 83.3%(翻倍),薄壁管上平均损失降低超过 1.5 个数量级。
- 🇬🇧 Systems with implicit equilibrium (e.g., deformable objects) are multistable, path-dependent and sensitive over long horizons, and adjoint learning's frozen-tangent approximation becomes inaccurate when the local equilibrium varies quickly. SCNC optimizes trajectories along which sensitivity variations are explicitly controlled, with a derived gradient-error bound and a practical finite-difference approximation. On elastic rods, thin-walled tubes, measuring tapes and Slinky-like structures it converges faster and more stably than adjoint learning and gradient-free iCEM, doubling the stable optimization rate (83.3% vs 41.7%) and cutting average loss by over 1.5 orders of magnitude on thin-walled tubes.

### [Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy](https://arxiv.org/abs/2611.04096)
作者:Kevin Weekly, Alexandre M. Bayen。Comments:12 pages, 4 figures, 5 tables。
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接或承诺
- 🇨🇳 HJ 可达性能给出带认证的后向可达管,但水平集计算随状态维度指数增长,历史上只能离线;而 ADAS/AV、人形机器人和 VLA 越来越依赖黑盒概率策略,需要带形式化保证的确定性安全层。作者实现了 WENO5 + TVD-RK3 + Lax-Friedrichs 水平集 HJI 求解器的 CUDA 版本(2D/3D/4D)。FP32 下在 RTX 4000 Ada 上 3D Air3D BRT 达 112 Hz、4D 追逃 61 Hz、2D 风漂浮体 74–147 Hz,比 JAX 参考实现 hj_reachability 快 5.9–17.5 倍;Jetson AGX Thor 上 Air3D 66 Hz;并在 6 架四旋翼的野火响应闭环仿真中以每步 4.0 ms 恢复多智能体捕获盆地 Voronoi 剖分。
- 🇬🇧 HJ reachability gives certified backward reachable tubes, but level-set computation scales exponentially with state dimension and was historically offline, while ADAS/AV, humanoid and VLA stacks increasingly use black-box probabilistic policies that need a deterministic safety layer. The paper presents a CUDA implementation of the WENO5 + TVD-RK3 + Lax-Friedrichs HJI solver for 2D/3D/4D dynamics. In FP32 on an RTX 4000 Ada it computes the 3D Air3D BRT at 112 Hz, a 4D pursuit-evasion BRT at 61 Hz and a 2D drifter BRT at 74–147 Hz (5.9–17.5x faster than JAX hj_reachability), 66 Hz for Air3D on a Jetson AGX Thor, and recovers the K-agent capture-basin Voronoi tessellation at 4.0 ms per tick in a six-quadcopter wildfire simulation.

### [Computing Invariant Reachable Sets through Sum-of-Squares Programming](https://arxiv.org/abs/2611.04325)
作者:Mohamed Khalid M Jaffar。Comments:8 pages; submitted to IEEE TCST。
开源状态 / Code: ✅ 已开源 / Released — [computeSOSFunnels](https://github.com/khalid2696/computeSOSFunnels);Comments 给出,匿名 `git ls-remote` 验证可访问
- 🇨🇳 漏斗(funnel,围绕名义轨迹的时变不变集)可证明闭环跟踪规划并可组合成验证过的运动规划,但 SOS 计算对初值、Lyapunov 函数归一化与终止规则等实现细节敏感,文献记载甚少。本文给出自包含的 SOS 漏斗计算流程,提出带入口/出口约束的最小体积形式,使端点重合的漏斗按构造可组合。独轮车上的数值实验显示:每个漏斗的 39,000 个边界样本在真实动力学下无违反证书;在 cart-pole 与 12 状态四旋翼上的计时表明构造 SDP 而非求解占主要耗时,且不可行初值部分可在求解前判定。
- 🇬🇧 Funnels (time-varying invariant sets around nominal trajectories) certify closed-loop tracking and compose into verified plans, but SOS-based computation depends on implementation choices (initial guess, Lyapunov normalization, termination rule) that the literature documents only briefly. The paper gives a self-contained SOS funnel pipeline with a minimum-volume formulation with inlet/outlet constraints so funnels with coinciding endpoints compose by construction. On a unicycle the certificate shows no violations among 39,000 boundary samples per funnel under true dynamics; timing studies on a cart-pole and a 12-state quadrotor show that constructing the SDP, not solving it, dominates computation time, and infeasible initial guesses are partly decidable before solving.

### [Grasping and Stabilizing Tumbling Objects with Rotating-Base Multi-Arm Space Manipulators](https://arxiv.org/abs/2611.04176)
作者:Farhad Aghili。
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接或承诺
- 🇨🇳 空间机械臂近距离操作中,翻滚目标使运动规划复杂且碰撞风险高。本文提出主动机动基座的制导控制方法,使基座相对翻滚物体保持静止:抓取前阶段用同步控制将目标质心对准系统瞬时转动中心,使目标-服务器系统"虚拟刚化";抓取后阶段用基于哈密顿动力学的最优控制,在满足基座力矩上限与多抓取约束下最小化时间、燃料或能量,结构化目标的力/力矩保持在界内,非结构化目标由摩擦约束防滑。一个案例研究演示了随后的抓取与消旋阶段可行;摘要未给出定量数字。
- 🇬🇧 Tumbling targets complicate motion planning and raise collision risk in space-manipulator proximity operations. The paper proposes guidance and control in which the servicer actively maneuvers its base to hold the object stationary: a pre-grasp synchronization control aligns the target's CoM with the system's instantaneous center of rotation to virtually rigidize the system, and a post-grasp Hamiltonian optimal-control strategy minimizes time, fuel or energy under base-torque limits and grasp constraints (force/torque bounds for structured targets, friction constraints for unstructured ones). A case study demonstrates grasping and detumbling; no quantitative results in the abstract.

### [h-NESDF: An Infinitely Differentiable Signed Distance Between Two Sets with Robotic Applications](https://arxiv.org/abs/2611.03944)
作者:Vinicius Mariano Gonçalves, Pedro Antonio de Souza Campos Rodrigues。
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接或承诺
- 🇨🇳 运动规划与控制常需要集合间距离及其导数,而欧氏距离并非处处可微。作者引入两个一般(可非凸)集合间的法向欧氏有符号距离函数 NESDF,并给出带平滑参数 h 的推广 h-NESDF:对所有 h>0 无限可微,h→0 时退化为 NESDF,且适合 GPU 并行高效计算。通过大量仿真评估其在运动规划中的可行性(摘要未给出定量数字)。
- 🇬🇧 Motion planning and control often need distances between sets and their derivatives, but Euclidean distance is not always differentiable. The paper introduces NESDF, a normal Euclidean signed distance between two general (possibly non-convex) sets, and its generalization h-NESDF with a smoothing parameter h that is infinitely differentiable for all h>0 and reduces to NESDF as h→0, amenable to GPU parallelization. Extensive simulations evaluate its viability in motion planning; the abstract gives no numeric results.

### [Nested Field-of-View Barriers for Teleoperated Multi-Robot Relay Chains](https://arxiv.org/abs/2611.05074)
作者:机构摘要未给出。Comments:8 pages, submitted to ACC。
开源状态 / Code: ❓ 未知 / Unknown — Comments 与摘要无代码链接
- 🇨🇳 通信受限环境中遥操作需保持通信链路。作者提出共享自主框架:遥操作领队后跟一串自主机器人以中继到固定基站的视线,用基于可见性的 CBF 并以二次规划局部计算控制;严格约束保证连通但无独立目标的跟随者会静止并卡住领队,放宽则失去保证。方案用嵌套硬/软可见性约束:严格全视场约束保证连通,收缩视场约束作为放松的行为目标将跟随者向内拉。证明了局部 QP 的可行性与连通无碰集合的前向不变性;在运动学积分器与 Crazyflie 软件在环仿真中,相比为同等到达时间调参的基线,链路更接近连通集合且跟随者移动更少(摘要未给具体数字)。
- 🇬🇧 Teleoperation in communication-denied environments must maintain a link. The framework has a teleoperated leader followed by autonomous relays enforcing line of sight via visibility-based CBFs, each solving a local QP; strict constraints stall leaderless followers while relaxing them loses the guarantee. Nested hard-soft visibility constraints resolve this: a strict full-FoV constraint guarantees connectivity and a contracted FoV acts as a relaxed behavioral objective pulling followers inward, with proven QP feasibility and forward invariance of the connected, collision-free set. In simulation (kinematic integrator and software-in-the-loop Crazyflies) it keeps links much closer to the connected set and moves followers less than a baseline tuned for comparable arrival time (no numbers given).

### [Haptic Shared Control for Multi-Robot Systems](https://arxiv.org/abs/2611.05027)
作者:机构摘要未给出(法国 Rennes 大学 IRISA/Inria 博士论文)。Comments:PhD thesis, 134 pages。
🏷️ 交叉方向 / Also: 人机交互 / HRI
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 多机器人系统需要先进控制策略保证自主体与操作者协作。论文修改全局连通性保持算法,使其可使用视场受限传感器在各自局部坐标系下的测量,并与三种自适应监督策略结合:单体控制(S)、钉扎控制(P)、质心控制(C),在满足机器人间约束的同时通过触觉反馈告知用户连通状态。通过用户研究在多种场景下对比有无触觉反馈的表现(摘要未给出定量数字)。
- 🇬🇧 Multi-robot systems need control strategies for cooperation between autonomous agents and human operators. The thesis modifies global connectivity maintenance to use measurements in each agent's local frame from limited-FoV sensors, and combines it with three adaptive supervision modes — single-agent (S), pinning (P) and centroid (C) control — ensuring inter-agent constraints while giving haptic feedback on connectivity. A user study compares performance with and without haptics across scenarios; the abstract gives no numeric results.

### [A Tutorial on Shape Servoing of Deformable Objects — Part II: Advanced Concepts](https://arxiv.org/abs/2611.03825)
作者:机构摘要未给出。Comments:Part II of two; 10 pages。
开源状态 / Code: ✅ 已开源 / Released — [教程代码](https://github.com/nachocz/tutorial_on_shape_servoing_of_deformable_objects),Comments 给出,另有[交互演示](https://nachocz.github.io/tutorial_on_shape_servoing_of_deformable_objects/)
- 🇨🇳 内容:这是数据驱动、基于雅可比的形状控制教程的第二部分(第一部分构建了形状伺服回路并推导局部稳定条件)。本文先用形变雅可比的奇异值分解区分小幅运动可产生的、需大幅运动的以及局部不可达的形状变化,再分析形状特征选择如何决定控制器调节形状的方式与形变程度,描述三类失效(可控性丧失、可观性丧失、机械不稳定),最后扩展到时变目标、次级任务和三维物体。结论:教程性质,无定量结果。
- 🇬🇧 Content: second part of a tutorial on data-driven, Jacobian-based shape control (Part I built the loop and a local stability condition). It uses the SVD of the deformation Jacobian to separate shape changes reachable by small, large or no robot motions, analyses how feature choice determines regulation and deformation en route, describes three failure modes (loss of controllability, loss of observability, mechanical instabilities), and extends to time-varying targets, secondary tasks and 3D objects. Conclusion: a tutorial without quantitative results.

### [Mass Scaling Laws for Energy-Optimal Horizontal Multirotor Flight](https://arxiv.org/abs/2611.04748)
作者:机构摘要未给出。Comments:Accepted to IEEE RA-L, October 2026。
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接
- 🇨🇳 多旋翼续航受限,载荷变化导致质量频繁变化。本文推导能量最优稳态水平飞行与整机质量的闭式缩放关系,并在两个多旋翼平台上实验验证。对仅质量变化:(1) 能量最优速度正比于质量平方根;(2) 能量最优俯仰角与质量无关;(3) 单位距离最优能耗正比于质量,三者源于稳态飞行与旋翼气动方程的共同质量相似性。这些关系支持简单有效的巡航速度规划,以提升续航。
- 🇬🇧 Multicopter range and endurance are limited and payload changes vary mass frequently. The work derives closed-form scaling relationships between energy-optimal steady horizontal flight and vehicle mass and validates them on two platforms. For mass-only variation: (1) optimal velocity scales with the square root of mass; (2) optimal pitch is constant in mass; (3) optimal energy per meter is proportional to mass, all arising from a common mass-similarity property of the steady-flight and rotor-aerodynamic equations. This enables simple cruise-speed planning to extend range and endurance.

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

本类共 18 条:详细展开 8 条 + 列名 10 条。 / 8 expanded + 10 listed.

### [AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data](https://arxiv.org/abs/2611.03815)
作者:Yueh-Hua Wu, Kei Ota, Hanlong Li 等。Comments:18 pages。
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://a-0.airoa.io)对数据集等标注 "Coming soon";摘要称将发布数据集、预训练权重与后训练配方,但尚无可用链接;YUBI 手持夹爪已开源(摘要)
- 🇨🇳 问题:不依赖任何机器人数据,仅用手持示教学习双臂操作。方法:AIRoA-0 (A-0) 在 16,151 小时手持示教上训练,示教用开源手持夹爪 YUBI 采集;系统仅用每个腕部相机,学习每个腕部视图的相关区域、预测任务所处阶段,并以连续流解码动作;不使用遥操作数据、强化学习或机器人纠正。结果:十个任务平均成功率 78%,而在相同任务示教上后训练的其他四个 VLA 中最强者为 27%;可在装有 YUBI 的 bimanual Franka、TX-G2、OpenArm、UR 上运行。
- 🇬🇧 Problem: learn bimanual manipulation purely from handheld demonstrations with no robot data. Method: A-0 is trained on 16,151 hours of demonstrations recorded with the open-source handheld YUBI gripper, uses only a wrist camera per arm, learns which wrist-view regions matter, predicts task stage and decodes actions as a continuous stream, with no teleoperation, RL or on-robot corrections. Results: 78% average success over ten tasks versus 27% for the strongest of four other VLAs post-trained on the same demonstrations, running on robots mounting YUBI such as bimanual Franka, TX-G2, OpenArm and UR; dataset, weights and recipe are announced for release.

### [RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](https://arxiv.org/abs/2611.05163)
作者:Seungyong Lee, Suhyeok Jang, Minyoung Kim 等。Comments:29 pages;[项目页](https://ryan-seungyong-lee.github.io/RoboTryOn)。
🏷️ 交叉方向 / Also: 世界模型(视频生成)/ video generation
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/ryan-seungyong-lee/RoboTryOn);HF Daily Papers githubRepo 字段给出,匿名 `git ls-remote` 验证可访问
- 🇨🇳 机器人基础模型适配新任务仍依赖遥操作示教;第一视角人类视频可替代,但叠加渲染机器人或位姿重定向在高自由度本体上有视觉/动作差距。RoboTryOn 把人到机器人翻译视为"虚拟试穿":保留示教动作,把人换成机器人——将人类视频转换为由参考图指定的目标机器人视频,自回归翻译关键帧并以手部骨架运动条件引导视频合成,再用含深度特征的逆动力学模型从合成视频推断动作标签。在多种人形本体上,用合成数据训练的策略在新任务(含双臂操作)上平均成功率从 2% 提升到 60%,且无需这些任务的真机示教;性能可匹配纯遥操作数据训练的策略,而采集成本约为三分之一。
- 🇬🇧 Adapting robot foundation models to new tasks still relies on teleoperation, and overlaying rendered robots on human videos or retargeting poses leaves visual or action gaps for high-DoF embodiments. RoboTryOn treats human-to-robot translation as virtual try-on: keep the motion, swap the human for the robot, translating keyframes autoregressively and guiding video synthesis with hand-skeleton-conditioned motion, then inferring action labels with a depth-aware inverse dynamics model. Across humanoid embodiments, policies trained on the synthetic data raise average success on novel tasks (including bimanual) from 2% to 60% with no real demonstrations of those tasks, and match teleoperation-trained policies at about a third of the collection cost.

### [PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](https://arxiv.org/abs/2611.05320)
作者:Kewei Zhang, Juncheng Ma, Guodong Lv, Duomin Wang 等(DAGroup-PKU)。Comments:22 pages;含项目页与代码。
开源状态 / Code: ✅ 已开源 / Released — [PyRUA-Lean 仓库(DataFarm 分支)](https://github.com/DAGroup-PKU/PyRUA-Lean/tree/DataFarm);Comments 给出,匿名 `git ls-remote` 验证仓库可访问
- 🇨🇳 遥操作示教每集都耗费机器人与操作员时间。DataFarm 让编码智能体接管遥操作者:接收数据请求和一集目标场景校准示教,在仿真中重建任务(写出场景、专家控制器和成功判定器),仿真提供精确动作,以真实图像为条件的视频模型把每条 rollout 渲染成多视角一致的写实视频,独立裁判在入库前认证。五个真机任务上,仅用 farm 数据训练的策略与同样数量遥操作示教训练的策略相当(100 次试验中 93 对 84 次成功),在未见桌布和彩色灯光下 farm 策略仍保持 87 次成功,而遥操作训练策略降到 46 次。任务适配全自动,每任务平均 21 美元 API 费用(另加 5 美元渲染合同),之后每集平均 0.80 美元;一小时三视角数据平均 107 美元,略低于中国遥操作报价 117 美元。
- 🇬🇧 Teleoperated demonstrations cost robot and operator time per episode. DataFarm lets a coding agent act as teleoperator: given a data request and one calibration episode it rebuilds the task in simulation (scene, expert controller, success judge), the simulator supplies exact actions, a video model conditioned on real images renders consistent multi-view photographic video, and independent judges certify the expert and each rendered episode. On five real-robot tasks, policies trained only on farm data match policies trained on as many teleoperated episodes (93 vs 84 successes in 100 trials) and keep 87 successes under an unseen tablecloth and coloured light where teleoperation-trained policies fall to 46. Adapting a task costs about $21 of API usage plus $5 for a render contract, each further episode about $0.80, and one hour of three-view data about $107 versus a $117 teleoperation quote in China.

### [Spectrally Routed Diffusion Policy for Multi-Task Robotic Manipulation](https://arxiv.org/abs/2611.04477)
作者:Mingcong Li, Yihan Zhou, Jiayu Qu 等。Comments:8 pages;RA-L。
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接
- 🇨🇳 多任务联合训练的扩散策略不及单任务专家:卷积编码器视觉条件区分度不足,且不兼容动作模态的梯度在共享去噪器稠密参数上相互干扰。SR-DP 用冻结的 VGGT 编码器加空间压缩适配器得到紧凑多尺度语义-几何 token;先训练标准扩散去噪器,再对选定线性层做 SVD 分解为冻结的正交秩一专家基,通过谱路由与 Householder 输入旋转适配。RoboTwin 六个任务平均成功率 68.4%,比多任务 VO-DP 高 21.8 点、比最强单任务基线高 3.8 点;四个真实双臂任务第二阶段平均 43.0%,较第一阶段提高 19.0 点。
- 🇬🇧 Jointly trained multi-task diffusion policies underperform per-task specialists because convolutional encoders give weakly discriminative visual conditions and incompatible action modes interfere in shared dense denoiser parameters. SR-DP uses a frozen VGGT encoder with a spatial-compression adapter for compact semantic-geometric tokens, trains a standard diffusion policy, then SVD-decomposes selected linear layers into frozen orthogonal rank-one experts adapted by spectral routing and Householder rotations. It averages 68.4% on six RoboTwin tasks (21.8 points above multi-task VO-DP, 3.8 above the best per-task baseline) and 43.0% on four real bimanual tasks, 19.0 points above Stage 1.

### [All-For-One: Distilling Visual Foundation Models to a Fast, Memory-Efficient Visuomotor Policy](https://arxiv.org/abs/2611.04485)
作者:Byungkun Lee, Minho Park, Hojoon Lee 等。
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接
- 🇨🇳 视觉基础模型(VFM)的深度/分割语义对操作有用,但直接用于闭环控制计算昂贵、时间不一致且存在分布偏移。AFO 两阶段蒸馏:All 阶段教师策略融合 RGB 与多个 VFM 输出学习语义增强表示;For-One 阶段将其在分布内蒸馏为轻量 RGB-only 学生策略(VFM 仅作训练期特权信息)。在 2 个 Adroit、5 个 MetaWorld 仿真任务和 3 个真实任务上优于以往基于基础模型的方法,参数比 VFM 编码器少 30 倍以上,仿真中延迟比其教师低 50 倍。
- 🇬🇧 VFM semantics (depth, segmentation) help manipulation, but deploying them in closed loop is costly, temporally inconsistent and distribution-shifted. AFO uses two-stage privileged distillation: a teacher fuses RGB with several VFM outputs, then a lightweight RGB-only student is distilled in-distribution. On two Adroit and five MetaWorld tasks plus three real tasks it beats prior foundation-model approaches with over 30x fewer parameters than VFM-based encoders and 50x lower latency than its own teacher in simulation.

### [Action Intent as a Bridge: Transferring Manipulation Knowledge from Human-Centric Videos to Robots](https://arxiv.org/abs/2611.04522)
作者:Zhiqian Xia, Lianyang Ma, Haifeng Xia 等。Comments:12 pages。
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接
- 🇨🇳 VLA 依赖昂贵真机数据;从人类视频迁移知识是替代,但已有潜在动作表示与场景噪声纠缠。AIT 两阶段:先提取显式动作意图并解耦隐式动作意图,再在共享意图空间中对齐人类与机器人域并解码为可执行机器人动作。仿真与真实环境实验中迁移人类知识更有效,并持续优于已有基线(摘要未给出具体数字)。
- 🇬🇧 VLAs depend on costly real-robot data and transferring from human videos is attractive, but existing latent-action representations are entangled with scene noise. AIT first extracts explicit action intents and disentangles the implicit intent, then aligns human and robot domains in the shared intent space and decodes to executable robot actions. In simulation and real-world experiments it transfers human knowledge more effectively and consistently outperforms baselines (no numbers in the abstract).

### [FEIJOA: Task-Driven Grounding and Execution for Mobile Manipulation](https://arxiv.org/abs/2611.04080)
作者:Aditya Agarwal, William Shen, Sahit Chintalapudi 等。
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://williamshen-nz.github.io/feijoa/),摘要未给代码链接
- 🇨🇳 场景表示在指令已知前构建,可能缺少解析任务所需的属性、可供性或概念。FEIJOA 是在测试时对指令做落地的语言模型智能体:对带位姿 RGB-D 扫描查询落地工具、检查候选并细化查询;具身感知外壳检查技能前置条件、采样可达基座位姿并用执行前后观测验证效果。103 个开放式落地查询上精确解析 94.2%(最佳预构建表示 68.0%);Spot 上 50 次真机试验完成 35 个,其中 17 个成功是从失败工具调用或验证中恢复后取得;15 次失败中 13 次源于物理技能,仅 2 次源于落地或推理。
- 🇬🇧 Scene representations built before the instruction is known may lack the needed attributes or affordances. FEIJOA is an LM agent that grounds the instruction at test time via a grounding tool over a posed RGB-D scan, refining queries, with an embodiment-aware harness checking skill preconditions, sampling reachable base poses and verifying effects. It resolves 94.2% of 103 open-ended queries exactly (best prebuilt representation 68.0%); over 50 real Spot trials it completes 35, 17 of them after recovery, and 13 of 15 failures come from physical skills and only 2 from grounding or reasoning.

### [Robot-Matched Soft Fingers for UMI Data Collection: Lessons from 100 Hours of Pick and Place](https://arxiv.org/abs/2611.03779)
作者:Kobi Kelemen, Tomasz Niedziałkowski, Marcin Paszczak, Victoriano Montesinos。Comments:CoRL 2026 UMI Arena Workshop 海报。
开源状态 / Code: ✅ 已开源 / Released(部分)— [项目页](https://lute-corp.github.io/soft-yubi-site/)(摘要称手指设计、数据集与数据处理代码均在该页发布;未单独核验仓库)
- 🇨🇳 现有 UMI 依赖外部基站、刚性指无力反馈或平行夹爪限制抓力。本文在 YUBI 上做电池供电手持接口,软质倾斜手指包裹物体、受力可见形变并与机器人夹爪匹配;收集 99.7 小时、53 个物体的数据集,在其中 49 个物体上训练 π0.5 策略并留出 4 个未见物体。顶部相机即使只有约一半数据含有也使成功率提高 13 点;在多任务数据上中期训练使未见物体微调后成功率从 35% 升到 57%。
- 🇬🇧 Existing UMIs need base stations, give no contact-force signal with rigid fingers, or limit grip strength with parallel jaws. The paper builds a battery-powered handheld interface on YUBI with soft angled fingers that wrap objects, deform visibly as a force proxy and match robot grippers; it collects a 99.7-hour, 53-object dataset, trains π0.5 on 49 objects and holds out 4. A top camera adds 13 points even when only about half of the data has it, and mid-training on the multi-task data lifts success on unseen objects after fine-tuning from 35% to 57%.

**其余列名 / Others (10 of 18)**:[RoboScope Kit](https://arxiv.org/abs/2611.03850)(评估工具,代码[已开源](https://github.com/MINT-SJTU/RoboScope-Kit))· [MABEL](https://arxiv.org/abs/2611.04083)(开源移动双臂平台,[open_mabel](https://github.com/robotmabel/open_mabel))· [GUILD](https://arxiv.org/abs/2611.05368) · [Physical Diffusion Policy via MPM-Guided 3D Gaussian Simulation](https://arxiv.org/abs/2611.04493) · [Asynchronous Robot Policies](https://arxiv.org/abs/2611.05155)(项目页标注 Code/Models soon)· [Do Agentic Policies Need to Look at Every Step?](https://arxiv.org/abs/2611.05058)([代码](https://github.com/Spectraorder/geometric-abstraction))· [DiMuRe](https://arxiv.org/abs/2611.04226) · [VARP](https://arxiv.org/abs/2611.04093) · [ActOR](https://arxiv.org/abs/2611.04255)(人形手术室智能体编排)· [DRAP](https://arxiv.org/abs/2611.05029)(物理 AI 持续学习)。(硬件与其他低相关条目见「其他值得关注」。)
另见 / See also: [ReflexArc](https://arxiv.org/abs/2611.04424)、[HLO-AMP](https://arxiv.org/abs/2611.05113)、[Coordinating Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.04839)、[WayTrace](https://arxiv.org/abs/2611.05129)(已归入 运动控制·RL);[Caging VLN](https://arxiv.org/abs/2611.04972)(已归入 运动控制·传统)。

---

## VLA

本类共 6 条,全部展开(不含已让出者)。

### [RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training](https://arxiv.org/abs/2611.04368)
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接
- 🇨🇳 用少量示教把通用 VLA 适配到目标任务会降低对外观、物体与指令变化的鲁棒性。RAFT 两阶段后训练:先在任务相关推理标注上训练低秩适配器,再冻结它们并在动作示教上微调策略。真机 DROID 上分布外成功率 75.0%(普通微调 27.9%);多阶段双臂 YAM 任务平均 70.0%(最强基线 36.0%);仿真抓放与开抽屉的视觉/物体/指令偏移下也有提升,且策略更关注标注的任务区域、后期层物体身份线性探针精度更高。
- 🇬🇧 Adapting a generalist VLA with limited demonstrations raises nominal success but reduces robustness to appearance, object and instruction changes. RAFT is a two-stage post-training: train low-rank adapters on task-relevant reasoning annotations, then freeze them while fine-tuning on action demonstrations. On a physical DROID robot it reaches 75.0% out-of-distribution success versus 27.9% for plain fine-tuning, and 70.0% on a multi-stage bimanual YAM task versus 36.0% for the strongest baseline, with gains under shifts in simulation and more attention on annotated regions.

### [Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training](https://arxiv.org/abs/2611.04873)
🏷️ 交叉方向 / Also: 世界模型 / World model
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接
- 🇨🇳 视频世界模型能通过想象结果评估候选动作,但高预测奖励可能偏向执行质量差的轨迹。TIF 是 VLA 后训练的离线监督选择方法:多维奖励模型预测效用分数与五个执行质量维度,审计器利用奖励预测与不确定性识别高估模式;候选效用优势超过边际且审计风险通过阈值才被采纳,否则保留已有监督,保留的真实轨迹再用于行为克隆。四个 LIBERO 套件、三个种子平均成功率 76.25%,比用已有轨迹训练提高 3.00 个百分点;审计门控额外带来 1.47 点;三个真机任务的录像上,被选轨迹的干净完成率从 58.33% 升到 70.00%。
- 🇬🇧 Video world models can score candidate actions through imagined outcomes, but high predicted rewards can favor poor execution. TIF is an offline supervision-selection method for VLA post-training: a multidimensional reward model predicts utility and five execution-quality dimensions, an auditor uses predictions and uncertainty to flag overestimation, and a candidate replaces existing supervision only if its advantage exceeds a margin and audit risk passes a threshold; retained real trajectories supervise behavior cloning. It reaches a 76.25% mean success on four LIBERO suites over three seeds (+3.00 points), audit gating adds 1.47 points, and on three real-robot tasks clean completion among selected trajectories rises from 58.33% to 70.00%.

### [Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs](https://arxiv.org/abs/2611.05249)
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接
- 🇨🇳 当前 VLA 常把预训练 VLM 与流匹配动作专家配对,主流配方阻断专家到 VLM 的梯度(隔离)以保护 VLM 能力,同时对 VLM 做视觉语言数据与动作 token 监督。作者在自动驾驶与操作中独立改变"动作 token 监督"与"专家损失是否更新 VLM"。开环驾驶中,有动作 token 监督时隔离与耦合相当,无时耦合使轨迹预测误差降约 25%;两者从头联合训练时,耦合使闭环驾驶路线进度在有/无动作 token 监督下分别提升约 17%/40%,机器人操作也类似改善,说明梯度隔离不应作为默认配方。
- 🇬🇧 VLAs pair a pretrained VLM with a flow-matching expert, and common recipes block expert-to-VLM gradients (insulation) while supervising the VLM on vision-language data and action tokens. The authors vary action-token supervision and gradient coupling independently in driving and manipulation. In open-loop driving, insulation matches coupling when action tokens are supervised and coupling cuts trajectory error by about 25% otherwise; trained jointly from the outset, coupling raises closed-loop route progress by about 17% (with action tokens) and 40% (without) and also improves manipulation, challenging insulation as a default.

### [LoopQ: Fair, Closed-Loop Evaluation of Quantized Vision-Language-Action Models](https://arxiv.org/abs/2611.05093)
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接
- 🇨🇳 内容:LoopQ 在同一检查点、层和引擎上闭环比较 RTN、AWQ、GPTQ、ActQuant、QuantVLA,覆盖四个 VLA、18 万余个 LIBERO/LIBERO-plus 回合,在 H100、L4、Jetson AGX Thor 上测试,并检验四个公开 VLA 量化发布能否复现。结论:量化可靠节省 2–3 倍内存,但 VLA 专用 PTQ 不如简单通用基线;4 比特下 RTN/AWQ/GPTQ 匹配或超过 ActQuant/QuantVLA;标准 LIBERO 会掩盖损失(无显著损失的配置在 LIBERO-plus 扰动下损失 1.5–4.3 点);H100 batch 1 上量化版 π0.5 / OpenVLA-OFT 均不比 16 位快(慢 1.06–1.58 倍)。
- 🇬🇧 Content: LoopQ compares RTN, AWQ, GPTQ, ActQuant and QuantVLA closed-loop on the same checkpoint, layers and engine over four VLAs and 180,000+ LIBERO/LIBERO-plus episodes on H100, L4 and Jetson AGX Thor, and tests reproducibility of four public VLA-quantization releases. Conclusions: quantization saves 2–3x memory but VLA-specific PTQ underperforms simple generic baselines (at 4 bits RTN/AWQ/GPTQ match or exceed ActQuant/QuantVLA); standard LIBERO hides 1.5–4.3 point losses under LIBERO-plus perturbations; and on an H100 at batch 1 no quantized π0.5 or OpenVLA-OFT is faster than 16-bit (1.06–1.58x slower).

### [Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs](https://arxiv.org/abs/2611.04166)
Comments:NeurIPS 2026。开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 推理型 VLA 让监督者通过语言理由监测安全,而已有攻击会破坏理由文本本身。作者表明视觉扰动可以在理由逐字不变的情况下改变物理动作,提出文本中性动作子空间(TNAS)诊断:在 Alpamayo(驾驶)与 InstructVLA(操作)接口上,动作最敏感方向与文本损失梯度近乎正交(范数重叠 1.87%/5.28%),沿该方向干预使动作位移是文本梯度扰动的 4.64–47.8 倍。在 154 个标注障碍的驾驶场景中,TNAS 引导攻击在理由逐字相同下于整图扰动 52.6%、局部补丁 35.1% 的场景造成新碰撞(无引导动作攻击 4.55%)。结论:不变的理由不能证明动作安全,监测应直接验证动作通道。
- 🇬🇧 Reasoning VLAs let supervisors monitor safety through rationales, but prior attacks corrupt the rationale itself. The paper shows visual perturbations can alter physical action while the rationale stays word-for-word identical, using a text-neutral action-subspace (TNAS) diagnostic: at Alpamayo (driving) and InstructVLA (manipulation) the most action-sensitive direction is nearly orthogonal to text-loss gradients (1.87% and 5.28% norm overlap) and interventions along it shift actions 4.64x–47.8x more than text-gradient ones. Across 154 driving scenes TNAS-guided attacks cause a new collision under an identical rationale in 52.6% (full-image) and 35.1% (patch) of scenes versus 4.55% unguided; an unchanged rationale cannot certify a safe action.

### [Aero-VPA: Few-Step Flow-Matching Control over Non-Reconstructive JEPA Latents for Agile Flight on Edge Hardware](https://arxiv.org/abs/2611.04392)
作者:Yeonseok Lee。Comments:仿真研究(PX4 SITL + Gazebo);v2。
🏷️ 交叉方向 / Also: 世界模型(JEPA 潜空间预测)、无人机控制 / Aerial control
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/ylee-sling/Aero-VPA),另有[训练策略](https://huggingface.co/ylee-sling/aero-vpa)与基准数据集;Comments 给出,匿名 `git ls-remote` 验证可访问
- 🇨🇳 VLA 自回归解码在嵌入式空中平台上受限于内存带宽。Aero-VPA 为轻量 Vision-Predictor-Action 架构:紧凑 RGB-D ViT 与五头集成预测器无像素重建地预测下一潜状态,条件流匹配求解器两步欧拉生成速度/偏航率块,集成离散度驱动不确定性回退。PX4 SITL 森林任务中,行为克隆在全部 60 个任务上失败(复制上一指令的因果混淆);DAgger 初期成功但停在 11.1–21.1%;加入无地图运行时屏蔽(15 s 深度记忆、屏障约束、视场外运动上限、沿飞行路径回退)后,180 个配对任务成功率从 21.1% 提高到 52.2%,碰撞率从 72.2% 降到 22.2%,超时从 2.8% 升到 23.3%。纯仿真研究。
- 🇬🇧 Autoregressive VLA decoders are bound by memory streaming on embedded aerial platforms. Aero-VPA is a lightweight Vision-Predictor-Action architecture: a compact RGB-D ViT and five-head ensemble predictor forecast the next latent without pixel reconstruction, a conditional flow-matching solver produces a velocity/yaw-rate chunk in two Euler steps, and ensemble dispersion triggers an uncertainty fallback. In PX4 SITL forests behaviour cloning failed all 60 missions (copycat causal confusion), DAgger plateaued at 11.1–21.1%, and a map-free runtime shield raised success on 180 paired missions from 21.1% to 52.2% and cut crashes from 72.2% to 22.2% while timeouts rose from 2.8% to 23.3%. Simulation only.

**其余列名 / Others (0)**:无,共 6 条均已展开。
另见 / See also: [CRONOS](https://arxiv.org/abs/2611.05080)、[PolicyIK](https://arxiv.org/abs/2611.05372)(已归入 运动控制·RL);[Cycle WAM](https://arxiv.org/abs/2611.04711)、[DreamFree](https://arxiv.org/abs/2611.04527)(归入 世界模型与 WAM)。

---

## VLN

本类今日无独立展开条目(今日 VLN 相关的两篇均涉及控制,已按优先级让出)。 / No standalone VLN entries today; both VLN-related papers involve control and were placed in higher-priority categories.
另见 / See also: [Caging VLN for Legged Robots](https://arxiv.org/abs/2611.04972)(已归入 运动控制·传统);[WayTrace](https://arxiv.org/abs/2611.05129)(已归入 运动控制·RL)。

---

## 世界模型与 WAM / World Models & WAM

本类共 9 条:详细展开 7 条 + 列名 2 条。 / 7 expanded + 2 listed.

### [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](https://arxiv.org/abs/2611.04870)
开源状态 / Code: 🕒 计划开源 / Planned — 摘要称 "We release the model weights, inference code, and training code",但未给链接,HF Daily Papers 无 githubRepo,尚不可验证
- 🇨🇳 机器人世界模型要当模拟器,必须忠实跟随动作、保持多视角一致、支持长时程。PrimeSim 从预训练视频生成器出发,在 22 个平台共 30,110 小时机器人示教上中期训练,引入统一跨本体动作表示与帧对齐双路径条件,并用带显式相机身份的视角感知交错注意力保证多视角一致;"快视频-慢记忆"后训练将双向生成器变成高效自回归模拟器。运行速度 10.1 FPS,刚体和可变形操作的长时程 rollout 稳定,新平台只需 100–200 步梯度微调;对比五个开源动作条件世界模型,在五个 WorldSimProbe 套件中领先四个并取得最佳 EWMBench 总分,细粒度局部校准仍落后;rollout 可支持 GRPO 策略优化。
- 🇬🇧 A robot world-model simulator must follow actions faithfully, stay multiview consistent and remain coherent over long horizons. PrimeSim midtrains a pretrained video generator on 30,110 hours from 22 platforms with a unified cross-embodiment action representation, frame-aligned dual-path conditioning and view-aware interleaved attention with camera identities, then a fast-video, slow-memory posttraining turns it into an efficient autoregressive simulator. It runs at 10.1 FPS, is stable over long rigid/deformable rollouts, transfers to held-out platforms in 100–200 gradient steps, leads four of five WorldSimProbe suites against five open-source world models with the best EWMBench score (fine-grained local calibration still trails), and supports GRPO policy optimization.

### [Future Representation Distillation for Imagination-Free World Action Models (DreamFree)](https://arxiv.org/abs/2611.04527)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接
- 🇨🇳 WAM 借预训练视频扩散模型预测未来用于控制,但迭代去噪昂贵,不准确的视觉预测还会损害动作预测。DreamFree 通过表示蒸馏把预训练视频扩散模型改造成预测式视觉编码器:编码器仅凭当前观测预测冻结视频扩散模型的表示,动作模块再从中提取动作相关信息,无需生成未来视频。真实与仿真任务上成功率高于最先进 VLA 与 WAM,并以 14B 视频扩散骨干实现 11 Hz 实时闭环控制;还可从含不同本体的无动作标注视频中学习新任务。
- 🇬🇧 WAMs use video diffusion priors for control via future video prediction, but iterative denoising is costly and inaccurate predictions hurt actions. DreamFree distills a frozen video diffusion model's representation into a visual encoder that predicts it from the current observation only, and an action module extracts action-relevant information, so no future video is generated. It beats state-of-the-art VLAs and WAMs on real and simulated tasks, runs closed-loop at 11 Hz with a 14B backbone, and learns new tasks from action-free videos, including other embodiments.

### [HiLo-WAM: Decoupling Long-Horizon Task Evolution and Local Dynamics in World Action Models](https://arxiv.org/abs/2611.05023)
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接
- 🇨🇳 多数 WAM 建模稠密短时视觉动力学,长程任务上下文有限,拉长预测视野又增加不确定性与计算。HiLo-WAM 在统一双 DiT 架构中解耦两路:稀疏长时程视觉流捕获历史与未来任务演化,稠密局部动力学流建模短时机器人-物体交互,通过结构化跨流注意力引导动作;渐进推理用分流部分去噪、联合去噪与动态跳过降低计算。RoboTwin 2.0 平均成功率 93.70%,RoboDojo 长时程任务进度分 17.43,并在 Fourier GR-3 机器人上域内与分布外均表现稳健。
- 🇬🇧 Most WAMs model dense short-horizon dynamics with limited long-range context, and longer horizons add uncertainty and cost. HiLo-WAM decouples a sparse long-horizon visual stream (history and future task evolution) from a dense local-dynamics stream in a dual-DiT architecture linked by structured cross-stream attention, with progressive inference (stream-wise partial denoising, joint denoising, dynamic skipping). It reaches 93.70% average success on RoboTwin 2.0, a 17.43 progress score on RoboDojo long-horizon tasks, and robust in-domain and OOD results on a Fourier GR-3.

### [Cycle WAM: Coupling Action and Video through Cycle Consistency](https://arxiv.org/abs/2611.04711)
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接
- 🇨🇳 现有 WAM 训练并不保证动作与其预测的视觉后果一致,限制了预训练视频先验的利用。Cycle WAM 把视频与动作视为因果相联的成对模态:先用双向转换增强视频-动作联合训练以恢复前向/逆动力学,再引入可微循环重建目标进一步耦合两个映射。在 LIBERO-Pro 上取得可比方法中的最优,并显著改进 DROID 上的 DreamZero;与 UWM 的比较表征了其逆动力学性能(摘要此处未给具体百分比)。
- 🇬🇧 Existing WAM training does not ensure actions and their predicted visual consequences are consistent, limiting use of pretrained video priors. Cycle WAM treats video and action as causally linked paired modalities, first augmenting co-training with bidirectional conversion to recover forward and inverse dynamics, then adding a differentiable cycle-reconstruction objective. It achieves state-of-the-art among comparable methods on LIBERO-Pro and substantially improves DreamZero on DROID; no specific percentages in the abstract.

### [DreamX: Video Diffusion Model is a Universal Latent Action Learner](https://arxiv.org/abs/2611.05377)
Comments:项目页。HF Daily Papers 49 赞。
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://cvlab-kaist.github.io/DreamX/)标注 "Code soon"
- 🇨🇳 已有潜在动作模型的表示与无关视觉变化纠缠,限制跨本体迁移。DreamX 将预训练视频扩散模型重用为通用潜在动作学习器,从视频模型时空特征中提取紧凑潜在动作,每个潜在视频帧压缩 300 倍(1,200→4 token),利用生成先验解耦外观。LARY-Bench 上达到潜在动作模型中的最优;潜空间支持任意到任意视频迁移与跨本体/环境的零样本动作迁移,并可在紧凑潜在动作空间中学习策略,降低视频扩散策略的计算成本。
- 🇬🇧 Existing latent action models entangle actions with irrelevant visual variation, limiting cross-embodiment transfer. DreamX repurposes a pretrained video diffusion model as a universal latent action learner, extracting compact latent actions from its spatiotemporal features with 300x compression per latent frame (1,200→4 tokens) and using the generative prior to disentangle appearance. It achieves state-of-the-art on LARY-Bench among latent action models, supports any-to-any video transfer and zero-shot action transfer across embodiments, and enables policy learning in a compact latent action space.

### [Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation](https://arxiv.org/abs/2611.04492)
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接
- 🇨🇳 许多动作条件世界模型在 2D 空间预测,缺乏显式 3D 建模,长时程跨视角一致性困难。3D World Simulator 用混合粒子-体素自编码器把点云压缩为紧凑 3D 体素潜变量,配合动作条件潜动力学模型,联合预测外观、几何与触觉观测,支持任意视角渲染与对齐触觉信号。实现 50 Hz 的交互式长时程多模态预测,可为策略训练与评估生成数据(含腕部与新视角),并在大数据上扩展,展示了对未见物体与机器人构型的基于模型的规划(摘要未给其他定量数字)。
- 🇬🇧 Many action-conditioned world models predict in 2D without explicit 3D structure, hurting cross-view and long-horizon consistency. The 3D World Simulator uses a hybrid particle-voxel autoencoder that compresses point clouds into 3D voxel latents with an action-conditioned latent dynamics model, jointly predicting appearance, geometry and tactile observations with arbitrary-view rendering. It delivers interactive long-horizon multimodal prediction at 50 Hz, scalable data generation for policy training/evaluation (including wrist and novel views), and model-based planning with unseen objects and robot configurations; no other numbers in the abstract.

### [Physical Experience Builds Continual Spatial World Models](https://arxiv.org/abs/2611.04016)
🏷️ 交叉方向 / Also: 空间智能 / Spatial intelligence
开源状态 / Code: ❓ 未知 / Unknown — 无 Comments,摘要无代码链接
- 🇨🇳 内容:研究持续运行中的空间世界模型应从重复物理经验中获得什么。在物理接地的动态迷宫中,跨回合"空间变化记忆"学习环境变换之间的关系,状态-动作-结果经验细化运动预测。结论:结构化经验逐步减少后续路线修正,并迁移到未见过的空间转换;当过去变化不含未来信息时优势消失;连续导航显示预测记忆在先前决策失效时改变行为;物理测试暴露局限——拓扑正确不保证动作预测正确,累积经验在建模动力学内缓解这一不匹配。摘要无标准基准数字。
- 🇬🇧 Content: studies what repeated physical experience must contribute for a continual spatial world model. In a physics-grounded dynamic maze, cross-episode Spatial Change Memory learns relations among environmental transformations while state-action-outcome experience refines motion prediction. Conclusions: structured experience progressively reduces route corrections and transfers to unseen transitions; the advantage vanishes when past changes carry no information about future ones; predictive memory changes behavior only when a previous decision becomes invalid; and correct topology does not guarantee correct action prediction, though accumulated experience reduces the mismatch. No standard benchmark numbers in the abstract.

**其余列名 / Others (2)**:[Physical Diffusion Policy via MPM-Guided 3D Gaussian Simulation](https://arxiv.org/abs/2611.04493)(已在具身类列名,不重复)· [Trajectory Evaluation via Rollout-Free World Model (RFWorld)](https://arxiv.org/abs/2611.05072)(自动驾驶轨迹评估,NAVSIM/Bench2Drive SOTA;与机器人控制无关)。
另见 / See also: [Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight](https://arxiv.org/abs/2611.04839)(已归入 运动控制·RL);[Trusting Imagined Futures](https://arxiv.org/abs/2611.04873)(归入 VLA)。

---

## 空间智能与 SLAM / Spatial Intelligence & SLAM

本类相关 5 篇,全部展开。

### [CoReMatch: Recurrent Continuous Coordinate Refinement for Real-Time Robotic Feature Matching](https://arxiv.org/abs/2611.03932)
Comments:CoRL 2026。开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 半稠密匹配器在固定网格上预测置信度,限制对应位置并需昂贵的高分辨率网格。CoReMatch 是在连续坐标空间直接细化对应的循环框架:粗阶段由 Deep Aggregated Transformer 捕获全局上下文并迭代更新对应坐标,轻量回归头进一步锐化定位。室内外基准上精度优于 Efficient LoFTR,在嵌入式边缘硬件上快 10 倍以上。
- 🇬🇧 Semi-dense matchers predict confidence on fixed grids, limiting correspondence locations and needing costly high-resolution grids. CoReMatch refines correspondences directly in continuous coordinate space with a recurrent framework: a Deep Aggregated Transformer captures global context and iteratively updates coordinates, and a lightweight regression head sharpens them. On indoor and outdoor benchmarks it beats Efficient LoFTR in accuracy while running over 10x faster on embedded edge hardware.

### [Sparse Anchors for Visual Multi-Session Registration in Changing Environments](https://arxiv.org/abs/2611.05084)
开源状态 / Code: ❓ 未知 / Unknown — 无代码链接
- 🇨🇳 重复监测需要跨次访问定位,环境变化与重复结构导致跨会话对应错误。方法:通过视觉位置识别、局部特征匹配和几何验证估计绝对对齐假设,用序列一致性剔除不一致假设,保留的位姿作为绝对锚点,再通过对高斯特征场的 featuremetric 对齐细化,并与会话内相对位姿约束一起做鲁棒位姿图优化。在 HILTI26 工地数据集 15 个跨会话实验中,1 m 内召回 94.4%、5 m 内 100.0%,而独立图像定位仅 65.3% 与 70.7%。
- 🇬🇧 Repeated monitoring needs localization across visits despite scene changes and repetitive structure. The method estimates absolute alignment hypotheses via place recognition, local matching and geometric verification, rejects inconsistent ones by sequence consensus, refines the retained anchors by featuremetric alignment against a Gaussian feature field, and fuses them with within-session relative poses in robust pose-graph optimization. On 15 cross-session HILTI26 construction-site experiments it reaches 94.4% recall within 1 m and 100.0% within 5 m versus 65.3% and 70.7% for independent image localization.

### [PadLoc: Training-Free Floor-Plan Localization by Sparse Geometric Matching](https://arxiv.org/abs/2611.05172)
Comments:WACV 2027。开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/mbookhahn/padloc);Comments 给出,匿名 `git ls-remote` 验证可访问
- 🇨🇳 近期学习式深度方法通过稠密 (x,y,θ) 位姿网格对每帧深度滤波来对平面图定位。PadLoc 保留可替换的深度前端,以稀疏几何匹配取代稠密网格后端:主导墙方向定义小的候选位姿集,掩码归一化互相关将观测自由空间与平面图打分,移动位姿高斯混合贝叶斯滤波加共识读出解码轨迹。在 Gibson 各轨迹长度上匹配或优于 UnLoc 与 F3Loc;Bonn LiLocBench 上在轮式里程计下比 UnLoc 的 SR@1m 高 23–32 个百分点;全视场 LiDAR+轮式里程计在静态序列达 100% SR@1m、中位误差 9–10 cm;Hilti-Trimble 挑战上纯相机鱼眼装置在五个会话中三个达在线 SR@2m 0.90–0.98。
- 🇬🇧 Recent learned-depth methods localize against floor plans by filtering per-frame depth through dense (x,y,θ) pose grids. PadLoc keeps a swappable depth front-end and replaces the grid back-end with sparse geometric matching: dominant wall orientations give a small candidate set, masked normalized cross-correlation scores free space against the plan, and a moving-pose Gaussian-mixture Bayes filter with consensus readout decodes the trajectory. It matches or beats UnLoc and F3Loc on Gibson, improves SR@1m over UnLoc by 23–32 points on Bonn LiLocBench with wheel odometry, reaches 100% SR@1m at 9–10 cm median error with full-FOV LiDAR, and gets 0.90–0.98 online SR@2m on three of five Hilti-Trimble sessions with a camera-only fisheye rig.

### [Visibility-Aware Reference Generation for Benchmarking Visual 3D Reconstruction in Vegetation-Rich Environments](https://arxiv.org/abs/2611.05361)
开源状态 / Code: 🕒 计划开源 / Planned — 摘要称 "The benchmark toolkit and datasets will be released",无可用链接
- 🇨🇳 内容:植被丰富户外环境缺乏几何真值。作者提出基于 LiDAR 的参考生成管线,复用多传感器定位数据集的图像、扫描与参考位姿生成逐视图深度图和可见参考点云;为解决累积 LiDAR 扫描的可见性误差,引入 LDGVS 做点级可见性过滤和 HPR 自动尺度选择。结论:在 BotanicGarden 上系统比较,前馈方法能高效给出稠密深度但三维重建可能含重复结构,传统 SfM 几何更连贯但稀疏且在困难植被场景更易失败;相比适用于完整扫描调查的方法,HPR+LDGVS 过滤保留约三倍点密度且绝对相对误差相当。
- 🇬🇧 Content: vegetation-rich outdoor scenes lack geometric ground truth. A LiDAR-based pipeline reuses images, scans and poses from multi-sensor localization datasets to generate per-view depth and visible reference clouds, with the LargeDepth-Gap Visibility Score (LDGVS) for point-wise visibility filtering and automatic scale selection in Hidden Point Removal. Conclusions: on BotanicGarden, feed-forward methods give dense depth efficiently but reconstructions can duplicate structures, while SfM is more coherent but sparse and fails more in challenging vegetation; HPR+LDGVS retains about three times the point density at comparable error versus a method suited to complete scans.

### [Physical Experience Builds Continual Spatial World Models](https://arxiv.org/abs/2611.04016) — 见世界模型类 / see World Models
另见 / See also: 该条已在 世界模型与 WAM 中展开,此处不重复。

自查:本类(及 VLA、世界模型、具身)条目已逐条核对;涉及人形/足式 locomotion、全身控制、控制策略 RL 的条目(ReflexArc、HLO-AMP、Latent Foresight、WayTrace、Caging VLN)均已移入运动控制类。Aero-VPA(四旋翼飞行,模仿学习+屏蔽,非 RL)与 DRAP/ActOR 留在 VLA/具身类,理由已在条目标注。

---

## 其他值得关注 / Other Notable

- [RoboScope Kit](https://arxiv.org/abs/2611.03850):统一 Policy/benchmark 适配器与并行调度,LIBERO-Long 上 500 回合评估比官方 StarVLA 评估器快 4.45 倍。 / Unified evaluation adapters and scheduling; 4.45x faster than the official StarVLA evaluator on LIBERO-Long (500 episodes).
- [MABEL](https://arxiv.org/abs/2611.04083):56 自由度开源移动双臂平台,零件成本 8.1k 美元,Apple Vision Pro 遥操作,仓库 [open_mabel](https://github.com/robotmabel/open_mabel)。 / Open 56-DoF mobile bimanual platform, US$8.1k parts cost.
- [RAIPAL](https://arxiv.org/abs/2611.04334):人形手臂硬件,峰值负载 20 kg(2.25 倍自重)、末端速度 20.6 m/s,RA-L 2026。 / Humanoid arm hardware: 20 kg peak payload (2.25x own mass), 20.6 m/s endpoint speed.
- [PACT](https://arxiv.org/abs/2611.05302):腿式灵巧手肌腱驱动共设计,八个姿态任务力覆盖 0.88–1.00。 / Tendon-driven hand co-design with task-force coverage 0.88–1.00.
- [DRAP](https://arxiv.org/abs/2611.05029)(物理 AI 持续学习)、[ActOR](https://arxiv.org/abs/2611.04255)(手术室人形智能体:闭环反馈使成功率 46.7%→83.3%,物理模拟手术室 14/20)、[CLARA](https://arxiv.org/abs/2611.04708)、[DiMuRe](https://arxiv.org/abs/2611.04226)、[Practical Causal Framework](https://arxiv.org/abs/2611.04027)、[VARP](https://arxiv.org/abs/2611.04093)(重排规划 98.3% 成功率、0.4 s)等。

另有群体机器人与 RAM 编译类论文(如 [Reality and Perceptual Gaps in Expressive Swarm Robotics](https://arxiv.org/abs/2611.05244)、[blockchain DAO swarm](https://arxiv.org/abs/2611.03975)、[te-comp](https://arxiv.org/abs/2611.03710))、车辆/感知类(V2X LiDAR sim2real 两篇、[ReSMap](https://arxiv.org/abs/2611.04352)、[iMED](https://arxiv.org/abs/2611.04755)、[MARL+CBF for CAV](https://arxiv.org/abs/2611.04957))与主题关联度低,仅列名。

---

## GitHub 动态 / GitHub Highlights

### Star 增长(相对 2026-11-03T23:12Z 快照) / Star growth

| 仓库 / Repo | ★ | 日增 Δ | 说明 / Note |
|---|---|---|---|
| [fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic) | 132 | +33 | G1 全身动作跟踪,单卡 3 分钟训练(见运动控制·RL)/ G1 whole-body tracking trained in minutes |
| [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) | 490 | +27 | SuperMimic 实现/扩展/演示的精选列表(第三方) / Curated third-party SuperMimic list |
| [Vottivott/microduck-playground](https://github.com/Vottivott/microduck-playground) | 115 | +26 | Microduck 双足机器人 RL 实验、策略与硬件扩展 / Biped RL experiments |
| [Motphys/Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) | 254 | +18 | 在 UniLab 上对 SuperMimic 的独立复现(第三方,非官方) / Independent reproduction, not official |
| [Ropedia/ropedia-w0](https://github.com/Ropedia/ropedia-w0) | 240 | +15 | 跨本体 loco-manipulation 世界模型 W0 / Cross-embodiment loco-manipulation world models |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28683 | +17 | 端到端机器人学习库 / End-to-end robot learning |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 14537 | +15 | π0 / π0.5 开源 / π0 family |
| [RLinf/RLinf](https://github.com/RLinf/RLinf) | 5591 | +10 | 具身与智能体 RL 基础设施 / RL infra for embodied AI |
| [Junchao-cs/SolarWM](https://github.com/Junchao-cs/SolarWM) | 863 | +14 | 长时程视频世界模型的开放数据与训练 / Open data & training for video world models |
| [Genesis-Embodied-AI/genesis-world](https://github.com/Genesis-Embodied-AI/genesis-world) | 30175 | +11 | 通用机器人仿真平台 / General robotics simulation |

另有高增长但与机器人关联较弱者(如 [ruvnet/RuView](https://github.com/ruvnet/RuView) +162、[bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) +234、[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) +188)不展开。

### 新仓库精选 / Notable new repos
- [leggedrobotics/terrain-grounded-imagination](https://github.com/leggedrobotics/terrain-grounded-imagination)(★21)、[fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic)(★132)、[lasgroup/generalist-improvement](https://github.com/lasgroup/generalist-improvement):已在运动控制·RL 展开。
- [vernerobotics/v0.5](https://github.com/vernerobotics/v0.5)(★5):自述 "open-weight world action model for general-purpose industrial robotics"(新建于 11-04,README 未核对,可信度待核实)。 / Self-described open-weight WAM; unverified.
- [SIPAIR-Elastic/DexArena](https://github.com/SIPAIR-Elastic/DexArena)(★5):长时程灵巧操作统一基准。 / Long-horizon dexterous benchmark.
- [yusenthebot/macmimic](https://github.com/yusenthebot/macmimic):在 Apple Silicon 上做 SuperMimic 风格人形全身控制训练(第三方)。 / SuperMimic-style training on Apple Silicon (third party).
- [Tinaliu0123/PolicyIK](https://github.com/Tinaliu0123/PolicyIK):见 PolicyIK 条目。

### 新 release / Releases(窗口内 1 条)
- [newton-physics/newton v1.8.0rc1](https://github.com/newton-physics/newton/releases/tag/v1.8.0rc1)(预发布,2026-11-04T01:21Z)。主要更新(radar 保存的 body 被截断,以下为可见部分):试验性 **Steel 关节刚体求解器**(SolverSteel:Featherstone 关节体动力学 + 带耦合 Coulomb 摩擦的投影 Gauss-Seidel 接触求解,支持摩擦块、闭环/mimic 关节、关节摩擦、可选逐次运行确定性、被动岛休眠、CUDA graph 捕获);XPBD/VBD 新增试验性无质量路径肌腱(锚点、针孔、滚轮、capstan 摩擦);SolverMuJoCo 增加肌腱等式约束、DC 电机与肌肉驱动器导入;新增 Kamino 动力学后端、可变形工作流增强、核心被动关节弹簧、碰撞与建模性能优化;迁移提示:XPBD 刚度调参、Rod 关节、导入的关节弹簧、MuJoCo 运动学根与走 `newton` logger 的控制台输出。 / Experimental Steel articulated rigid-body solver, routed tendons for XPBD/VBD, MuJoCo tendon/actuator import, Kamino backend, passive joint springs, collision/model-building speedups; see migration notes (body truncated in radar data, remainder not seen).

### Hugging Face Daily Papers
机器人相关且带 githubRepo:[RoboTryOn](https://arxiv.org/abs/2611.05163)(已开源,4 赞)。无仓库的高赞:[DreamX](https://arxiv.org/abs/2611.05377)(49 赞,Code soon)、[PrimeSim](https://arxiv.org/abs/2611.04870)(9 赞)。其他本期 HF 机器人向仓库:[RoboColosseum](https://github.com/RoboColosseum/robocolosseum-client)(43 赞,真实世界物理智能评测客户端)、[Democratizing Robot-Use Agents](https://github.com/Open-RUA/uni-robot-agent)(43 赞)。

---

## 今日趋势 / Today's Trends

1. **可微世界模型 + 想象 rollout 训练人形控制成为开源热点 / Differentiable world models for humanoid control are a GitHub hotspot.** SuperMimic 之后,GitHub 上出现 [BlinkMimic](https://github.com/fuyichen0725/blinkmimic)(3 分钟训练)、[Terrain-Grounded Imagination](https://github.com/leggedrobotics/terrain-grounded-imagination)(稀疏地形)、[Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) 与 [macmimic](https://github.com/yusenthebot/macmimic) 等衍生/复现,官方代码仍未出现。 / After SuperMimic, several derivatives and reproductions appeared while official code is still absent.
2. **人形控制的分层与反射 / Hierarchy and reflexes in humanoid control.** [ReflexArc](https://arxiv.org/abs/2611.04424)、[HLO-AMP](https://arxiv.org/abs/2611.05113)、[Latent Foresight](https://arxiv.org/abs/2611.04839)、[iLQR-MPC+WBC](https://arxiv.org/abs/2611.04204) 都在 G1 上围绕"快速底层 + 慢速高层(或模型先验)"设计,且多数代码"即将发布"。 / Fast low level plus slow high level on G1; most code "coming soon".
3. **WAM 走向"免想象"与更长视野 / WAMs go imagination-free and long-horizon.** [DreamFree](https://arxiv.org/abs/2611.04527)、[HiLo-WAM](https://arxiv.org/abs/2611.05023)、[Cycle WAM](https://arxiv.org/abs/2611.04711)、[DreamX](https://arxiv.org/abs/2611.05377) 同日出现,围绕"如何高效利用视频扩散先验"。 / Four papers on efficiently exploiting video-diffusion priors for control.
4. **VLA 后训练:RL、推理对齐与审计 / VLA post-training.** [GSBR](https://arxiv.org/abs/2611.05295)、[CRONOS](https://arxiv.org/abs/2611.05080)、[RAFT](https://arxiv.org/abs/2611.04368)、[TIF](https://arxiv.org/abs/2611.04873) 与 [generalist-improvement](https://github.com/lasgroup/generalist-improvement) 都在探讨在线/离线 RL 与监督选择如何改善预训练策略。 / RL and supervision selection to improve pretrained policies.
5. **手持/低成本数据采集 / Handheld data collection.** [AIRoA-0](https://arxiv.org/abs/2611.03815)(16,151 小时)与 [Soft UMI fingers](https://arxiv.org/abs/2611.03779)(99.7 小时)均基于 YUBI。 / Both build on the YUBI handheld gripper.

---

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
1. `differentiable world model` / `imagination rollouts` — 适用于 arXiv 检索与 GitHub topic。理由:SuperMimic 衍生仓库集中涌现,且 topic 中已出现 `world-model`、`supermimic`。 / Reason: a cluster of SuperMimic derivatives. 证据:至少 4 个仓库(如 [blinkmimic](https://github.com/fuyichen0725/blinkmimic)、[terrain-grounded-imagination](https://github.com/leggedrobotics/terrain-grounded-imagination))。
2. `VLA post-training` / `RL fine-tuning VLA` — 适用于 arXiv。理由:今日 5 篇/仓库围绕该问题(见趋势 4)。 / Reason: five items today. 证据:[CRONOS](https://arxiv.org/abs/2611.05080)、[RAFT](https://arxiv.org/abs/2611.04368)。

**建议观察 / Watch**
- `handheld demonstration` / `UMI`:今日 2 篇([AIRoA-0](https://arxiv.org/abs/2611.03815)、[Soft UMI](https://arxiv.org/abs/2611.03779)),信号尚弱。 / Two papers today, signal still weak.

**建议移除/收窄 / Remove or Narrow**:今日无建议 / No suggestions today.(今日关键词检索命中很少属于 API 窗口滞后,不据此移除词。)

---

## 开源监测 / OSS Watchlist

| 工作 | 加入日期 | 当前状态 | 今日检查结果 | 备注 |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | 未知 / Unknown | `signal=false`,candidate_repos 为空;匿名 `git ls-remote` 对 known_repos(qiayuanl/SuperMimic、HybridRobotics/SuperMimic)不可访问;[项目页](https://supermimic.github.io)未发现 GitHub 链接或发布承诺 | search_hits 多为第三方复现/衍生:[Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic)(★254,独立复现)、[awesome-supermimic](https://github.com/miao-org/awesome-supermimic)(★490,列表)、[blinkmimic](https://github.com/fuyichen0725/blinkmimic),不能据此判定已开源 |

**建议加入监测 / Suggested additions**(均为运动控制类,状态为计划开源):
- **ReflexArc** — 人形触觉反射 + 学习型全身控制,项目页 Code/Paper "Coming soon"。 / Humanoid tactile reflex + learned WBC; code listed as coming soon.
- **Coordinating Humanoid Loco-Manipulation (Action-Conditioned Latent Foresight)** — 人形 loco-manip WAM,项目页 "Code coming soon"。 / Humanoid loco-manipulation WAM; code coming soon.

```json
{
  "name": "ReflexArc",
  "title": "ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control",
  "arxiv_id": "2611.04424",
  "search_terms": ["ReflexArc", "Ascending Reflex Control"],
  "owners": [],
  "project_pages": ["https://minusmodulo.github.io/reflexarc-website/"],
  "known_repos": []
},
{
  "name": "ActionGroundedForesight",
  "title": "Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight",
  "arxiv_id": "2611.04839",
  "search_terms": ["Action-Grounded-Foresight", "action-conditioned latent foresight"],
  "owners": [],
  "project_pages": ["https://ju6276.github.io/Action-Grounded-Foresight/"],
  "known_repos": []
}
```

**建议移出 / Suggested removals**:无 / None.
