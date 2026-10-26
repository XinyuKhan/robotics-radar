# 机器人/具身智能每日速递 — 2026-10-27 / Robotics & Embodied AI Daily — 2026-10-27

**检查窗口 / Window:** 台北时间 2026-10-26 ~07:40 → 2026-10-27 ~07:40(周二)。arXiv 本期为 "Monday, 26 October 2026" 的 cs.RO 新列表(周末后的首个新列表)。 / Taipei time, Tue 2026-10-27; the arXiv page is the Monday 26 Oct cs.RO announcement, the first new batch after the weekend.

**来源状态 / Source status**
- arXiv cs.RO `new`:页面标题 "Monday, 26 October 2026",New 53 / Cross 11 / Replacements 43(页面合计 107,脚本解析出 106 条,1 条解析遗漏)。全部逐条分类:New+Cross 共 64 条中 **45 条相关**(类别 1–7),其余为无人机/集群/车道保持/医疗/定位等不相关;Replacements 只看相关且无法确认有实质更新者,仅列名。 / 107 listed, 106 parsed; all New+Cross entries triaged (45 of 64 relevant).
- arXiv API 关键词检索(cs.RO/cs.AI/cs.LG/cs.CV,按 submittedDate 降序,仅保留 2026-10-23 12:00 UTC 之后提交)命中数 / hits: embodied 5, VLA 2, vision-language-action 4, VLN 0, vision-language navigation 1, humanoid 3, legged locomotion 0, whole-body control 1, MPC 1, reinforcement learning robot 0, sim-to-real 1, dexterous manipulation 1, robot foundation model 0, world model 4, world action model 0, WAM 0, video world model 0, spatial intelligence 0, spatial reasoning 1, SLAM 0, visual SLAM 0, LiDAR SLAM 0, gaussian splatting SLAM 0, 3D reconstruction 1, motion tracking 1, motion imitation 0;去重后 17 篇,其中 4 篇不在 cs.RO 列表内(DT-JEPA、SP-Guide、UniAction、CompMVR),前三篇相关并已纳入,CompMVR(多视角图像恢复)与机器人关系弱,未纳入。 / 17 unique hits, 4 outside the cs.RO list; 3 of those added.
- 入选与摘要:共 56 篇已通过 arXiv API `id_list` 取得完整摘要与 Comments(0 篇失败、0 篇摘要为空;其中 30 篇 Comments 非空,已核对)。 / 56 abstracts fetched in full, 0 failures.
- Hugging Face Daily Papers:获取成功(100 篇)。本期相关且带 githubRepo 的有 [FLORA](https://arxiv.org/abs/2610.31779)、[RynnUnify](https://arxiv.org/abs/2610.32965);另有不在本期 cs.RO 列表的相关论文,仅记名不展开:[TARSphere](https://arxiv.org/abs/2610.30043)(带仓库)、[Echo](https://arxiv.org/abs/2610.31569)(VLA,带仓库)、[Skeleton-Grounded Latent Action Model for Robot World Models](https://arxiv.org/abs/2610.31474)、[FocusVLA](https://arxiv.org/abs/2610.31423)(均无仓库字段)。 / HF fetched OK.
- GitHub radar:已更新(`date_taipei=2026-10-27`,star 基准 2026-10-25 23:18 UTC);counts: new_repos 262, tracked 1660, with_growth 382, **watchlist_releases 0**, **oss_signals 1**(SuperMimic,经核实为误报,见末节)。 / Radar fresh; the single signal is a false positive.
- 推送权限:`git push --dry-run origin HEAD:main` 成功(无 403)。 / Push permission OK.
- Google Drive 连接器:见保存步骤说明(报告生成后上传)。

---

## 今日必读 / Top Picks

1. **[ViT-H](https://arxiv.org/abs/2610.32966)** — 运动控制·RL。✅ 已开源。🇨🇳 以扩散模型直接从单目视频生成人形参考动作,并用动作跟踪结果做 DPO 后训练,绕开重建-重定向流程,在 Unitree G1 上优于 RTR 流水线。 🇬🇧 Generates humanoid references directly from video and post-trains the generator with motion-tracking feedback (DPO); beats reconstruction-retargeting-tracking pipelines on Unitree G1.
2. **[Delay Randomization Widens the Delay Margin of Learned Humanoid Motion Trackers](https://arxiv.org/abs/2610.32277)** — 运动控制·RL。❓ 未知。🇨🇳 实证清晰:40 ms 指令延迟下未随机化策略平均存活率仅 15%,延迟随机化(0–50 ms)后升至 95%。 🇬🇧 Clean sim-to-sim evidence: survival at 40 ms delay rises from 15% to 95% with delay randomization.
3. **[HoloBoxing](https://arxiv.org/abs/2610.32909)** — 运动控制·RL。❓ 未知。🇨🇳 冻结预训练全身控制器、仅训练上层规划器,额外约 7 分钟单 GPU 训练学会人形拳击。 🇬🇧 Humanoid boxing on top of a frozen whole-body controller with ~7 extra minutes of single-GPU training.
4. **[FLORA](https://arxiv.org/abs/2610.31779)** — 具身智能与机器人基础模型(NVIDIA)。✅ 已开源。🇨🇳 用于训练 GR00T 的工业级数据引擎(字幕+结果/过程奖励),每天标注 20 万小时数据,已开放。 🇬🇧 The industrial data engine behind GR00T training, now open-sourced.
5. **[RynnUnify](https://arxiv.org/abs/2610.32965)** — 具身智能与机器人基础模型(阿里达摩院)。✅ 已开源。🇨🇳 16B 统一具身模型,融合理解、视觉规划与世界-动作扩展,真机三任务平均成功率 46.7%。 🇬🇧 16B unified embodied model with a world-action extension; 46.7% average success over three real-robot tasks.

---

## 运动控制·RL / Motion Control · RL

### [ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback](https://arxiv.org/abs/2610.32966)
🏷️ 交叉方向 / Also: 世界模型/视频生成 / Video Generation(扩散模型是核心技术,但目标任务是人形控制,故归入本类)
开源状态 / Code: ✅ 已开源 / Released — [awfuact/vit-h](https://github.com/awfuact/vit-h)、[mileret/ViT-H-release](https://github.com/mileret/ViT-H-release);项目页 [vit-h](https://awfuact.github.io/vit-h/) 链接这两个仓库,匿名 `git ls-remote` 均可访问,具体包含训练/推理/权重的哪些未逐项核实
- 🇨🇳 现有「重建-重定向-跟踪」流水线各阶段分别优化,系统层面难以扩展,且无法用下游跟踪结果反向优化参考动作的可执行性。ViT-H 采用「生成-跟踪」范式:用扩散模型直接从视频生成人形参考动作,跳过人体动作重建与重定向,并用动作跟踪结果通过直接偏好优化(DPO)后训练生成器;还给出自回归变体,实现延迟低于 400 ms 的实时人形视频遥操作。在 Unitree G1 上,动作质量与可执行性均优于最先进的重建-重定向-跟踪流水线,并随模型规模、预训练/后训练数据规模提升,跟踪反馈对不同动作跟踪器都能提升可执行性(摘要未给出更具体的数值)。
- 🇬🇧 Reconstruction-retargeting-tracking pipelines optimize each stage separately and cannot use downstream tracking outcomes to improve reference executability. ViT-H generates humanoid reference motions directly from video with a diffusion model (no reconstruction or retargeting) and post-trains it with direct preference optimization on motion-tracking outcomes; an autoregressive variant gives real-time video teleoperation with sub-400 ms latency. On Unitree G1 it beats state-of-the-art reconstruction-retargeting-tracking pipelines in motion quality and executability, scales with model size and with pre-/post-training data, and tracking feedback improves executability across different trackers (the abstract gives no further numbers).

### [Delay Randomization Widens the Delay Margin of Learned Humanoid Motion Trackers](https://arxiv.org/abs/2610.32277)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅 "8 pages, 1 figure",摘要无代码链接
- 🇨🇳 问题:人形运动跟踪策略常在一个模拟器训练、在另一个模拟器检查后才上真机,但这种检查对指令延迟说明了什么并不清楚。方法:对 24 关节人形在 5 段单目视频动作上训练跟踪策略,在独立 CPU MuJoCo 测试环境中评估,并在训练中随机化 0–50 ms 延迟。结果:训练随机化下每个策略在 30 回合中至少完成 26 回合,但 40 ms 恒定延迟时平均存活率降至 15%(0%–45%),延迟裕度仅 20–30 ms;延迟随机化把 40 ms 处存活率提到平均 95%(75%–100%),裕度扩大到 50–70 ms,代价是跟踪略松(四个动作上 0.02–0.06 rad);同等额外迭代但无延迟随机化的对照无提升,PhysX 训练的策略表现相同。作者建议按机器人实测延迟设定随机化范围,并把延迟裕度作为 sim-to-sim 指标。
- 🇬🇧 Problem: learned humanoid motion trackers are validated in a second simulator before hardware, but what that check says about command delay is unclear. Method: train tracking policies for a 24-joint humanoid on five video-derived motions, test in an independent CPU MuJoCo harness, and randomize delay (0–50 ms) in training. Results: every policy completes ≥26/30 episodes under training randomization, but at 40 ms constant delay survival falls to 15% on average (0%–45%) with a 20–30 ms margin; delay randomization lifts survival at 40 ms to 95% (75%–100%) and the margin to 50–70 ms at the cost of 0.02–0.06 rad looser tracking on four motions; a control with equal extra iterations does not improve and a PhysX-trained policy behaves the same. They recommend setting the range from measured latency and reporting delay margin as a sim-to-sim metric.

### [HoloBoxing: A Simple Recipe for Humanoid Boxing with 7 Minutes of Single-GPU Training](https://arxiv.org/abs/2610.32909)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,HF Daily Papers 无 githubRepo 字段,摘要无链接
- 🇨🇳 问题:为每个新任务重新学习全身控制代价高昂。方法:在预训练全身控制器之上,将可复用运动技能与任务决策分离——紧凑的上层规划器请求未来身体点目标,冻结控制器负责关节级执行;学习到的解码器把 32 维动作映射为结构化目标窗口,并用实测状态模仿初始化规划器,再用强化学习精修交互行为。结果:从现成控制器出发,额外训练约 7 分钟(含复用表征拟合与单 GPU 任务运行,不含控制器预训练、数据准备、评估和搜索);仅在仿真中评估拳击行为及模仿初始化、目标表示的作用,预印本摘要未给出具体成功率数值。
- 🇬🇧 Problem: relearning whole-body control for each new task is expensive. Method: build on a pretrained whole-body controller, separating reusable motor skills from task decisions — a compact planner requests future body-point targets, the frozen controller executes joints; a learned decoder maps 32-D actions to structured target windows, measured-state imitation initializes the planner, then RL refines interaction. Results: ~7 minutes of extra training (representation fitting plus a single-GPU task run; excluding controller pretraining, data preparation, evaluation, search); evaluated in simulated boxing with component controls, and the abstract reports no quantitative success numbers.

### [Regularised RL improves sim-to-real transfer](https://arxiv.org/abs/2610.32855)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为 "Under submission",无代码链接
- 🇨🇳 问题:正则化 RL 有可证明的鲁棒性保证,但 sim-to-real 流程仍以弱正则化的 PPO 为主,正则化的实际收益缺乏刻画。方法:推导基于 soft mellowmax 价值函数的新算法 Soft MellowMax Actor-Critic(SMM-AC),并系统比较常用 RL 算法的 sim-to-real 表现。结果:在 MuJoCo 连续控制基准上与 SAC 等基线相当;在真实机器人上回报更高,并对观测、环境和动力学扰动更鲁棒(摘要未给出具体数值)。
- 🇬🇧 Problem: regularised RL has provable robustness guarantees, yet weakly regularised PPO remains the default in sim-to-real pipelines and the benefit of regularisation is poorly characterised. Method: derive Soft MellowMax Actor-Critic (SMM-AC) from the soft mellowmax value function and compare common RL algorithms for sim-to-real. Results: competitive with SAC on MuJoCo benchmarks; on real robots it gets higher return and is more robust to observation, environment and dynamics perturbations (no numbers in the abstract).

### [CoCarry: Contact-Support-Structured Retargeting for Dual-Humanoid Cooperative Carrying](https://arxiv.org/abs/2610.32460)
🏷️ 交叉方向 / Also: 数据集 / Dataset(含数据集贡献,但核心为服务双人形控制的动作重定向,故归入本类)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为 "8 pages, 6 figures, 2 tables",无代码链接
- 🇨🇳 问题:协作搬运要求个体动作合理,同时保持跨智能体与物体的关系一致(共享抓取、相对构型、全身支撑)。方法:提出 CoCarry 数据集(220 条同步双人序列、21 种任务方案、5 种物体几何、4 种地形,约 61 分钟),并提出接触-支撑结构化重定向,围绕同一物体轨迹联合精修两个人形,用物体局部手部锚点保持四手抓取关系。结果:220 条序列重定向到两台 A3 人形,接触保持率 0.9995,穿透时长相对 GMR 和 OmniRetarget 分别降低 67.0% 和 71.0%,重定向成功率 100%;在 CORE4D 的 Unitree G1 上接触保持 0.9906 且零滑动;并经物理仿真和两台真实 A3 人形的多次协作搬运实验验证。
- 🇬🇧 Problem: cooperative carrying needs not only plausible individual motion but consistent cross-agent and agent-object relations (shared grasp, relative configuration, whole-body support). Method: the CoCarry dataset (220 synchronized two-person sequences, 21 task schemes, 5 object geometries, 4 terrains, ~61 min) plus Contact-Support-Structured Retargeting that jointly refines both humanoids around one object trajectory with object-local hand anchors. Results: on all 220 sequences retargeted to two A3 humanoids, contact preservation 0.9995, penetration duration reduced by 67.0% and 71.0% versus GMR and OmniRetarget, 100% success; on CORE4D with Unitree G1, 0.9906 contact preservation and zero sliding; validated in simulation and on two physical A3 humanoids.

### [Move, don't think: sample-efficient collision avoidance with lossy proximity sensors](https://arxiv.org/abs/2610.31891)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接
- 🇨🇳 问题:数据驱动机器人应以尽可能少的样本学会避碰,避免收集大量破坏性碰撞数据。方法:研究全身接近觉传感器作为学习反射式闪避行为的归纳偏置,在强化学习环境中比较八种候选表征(潜变量压缩、未来接触预测、有损损坏、特权状态估计),在受限样本与算力预算下训练 200 多个人形机器人玩简化躲避球。结果:低分辨率的有损传感器比高分辨率覆盖是更强的偏置;出乎意料的是,预测接触发生的时间和部位反而降低样本效率。预印本摘要未给出定量数值。
- 🇬🇧 Problem: data-driven robots must learn collision avoidance from few examples to avoid collecting destructive collision data. Method: use whole-body proximity sensors as inductive biases for reflexive dodging, comparing eight representations (latent compression, future contact anticipation, lossy corruption, privileged state estimation) in an RL environment by training 200+ humanoids on a simplified dodgeball task under a constrained sample/compute budget. Results: low-resolution lossy sensors are a stronger bias than high-resolution coverage, and anticipating where/when contact happens lowers sample efficiency; the abstract gives no quantitative results.

### [PrefO2O: Zero-Shot Preference-Based Reinforcement Learning via Offline-to-Online Latent Preference Transfer](https://arxiv.org/abs/2610.31812)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接
- 🇨🇳 问题:偏好强化学习(PbRL)每个新任务都需要昂贵的人类偏好标注。方法:从源任务的少量离线偏好数据学习任务不变的潜在偏好空间,用置信度加权的最优传输对齐生成伪偏好监督,实现目标任务上无需人类反馈的零样本 PbRL。结果:在机器人操作与运动基准上显著优于现有偏好迁移基线,并与使用真人反馈的 PbRL 持平或更好,可跨多对一、一对一设置及不同机器人形态泛化(摘要未给出具体数值)。
- 🇬🇧 Problem: preference-based RL needs costly human labels for every new task. Method: learn a task-invariant latent preference space from a little offline preference data on source tasks and use confidence-weighted optimal-transport alignment to produce pseudo-preference supervision for online reward adaptation, enabling zero-shot PbRL. Results: on manipulation and locomotion benchmarks it substantially beats preference-transfer baselines, matches or exceeds PbRL with real human feedback, and generalizes across transfer settings and embodiments (no numbers in the abstract).

### [SEVI: Safe Evidential Real-World Reinforcement Learning](https://arxiv.org/abs/2610.31829)
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://sevi-safe.github.io/)写有 "Code · coming soon";Comments:RA-L 2026 已接收
- 🇨🇳 问题:真机强化学习可直接训练接触丰富的操作,但在线学习中的不安全交互是主要障碍。方法:提出证据安全评论家,单次前向同时估计未来约束违反风险与认知不确定性;执行前评估每个动作,若预测不安全或证据不足,则由离线训练的恢复策略接管。结果:在两个仿真操作任务和真实 USB 插入任务(含分布内与分布偏移)上,取得最强的轨迹级安全预测、最高最终任务成功率和最少不安全事件;相对基于恢复的安全 RL,不安全事件减少 13.4%–57.1%,且保持低延迟过滤。
- 🇬🇧 Problem: real-world RL can train contact-rich manipulation directly on hardware, but unsafe online interactions remain a barrier. Method: an Evidential Safety Critic estimates constraint-violation risk and epistemic uncertainty in one forward pass; each task-policy action is checked before execution and overridden by an offline-trained recovery policy when unsafe or insufficiently supported. Results: on two simulated manipulation tasks and a real USB insertion (in-distribution and shifted), SEVI has the best trajectory-level safety prediction, highest final success and fewest unsafe events, reducing unsafe events by 13.4–57.1% versus recovery-based safe RL with low-latency filtering. (Accepted at RA-L 2026.)

### [Geometry-Aware Reinforcement Learning for Close-Fitting Wearable Insertion](https://arxiv.org/abs/2610.32143)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接
- 🇨🇳 问题:机器人辅助穿戴开口窄、肢体铰接,相对位姿的小误差就会造成卡住或漏插。方法:把穿戴表述为几何感知的插入问题(表示身体部位与物体开口的相对空间关系,而非完整可变形物体状态),用分阶段课程(粗对准 → 插入 → 最终放置)和逐指插入软门控的 RL 框架。结果:在刚性与可变形手镯穿戴任务上,可变形后训练评估成功率 84.7 ± 1.2%;插入门控贡献最大增益,再叠加课程达到最高分;在人体模型手上同一策略真机 15/20 次成功。
- 🇬🇧 Problem: robot-assisted dressing has narrow openings and articulated limbs, so small relative-pose errors cause snagging or missed insertion. Method: formulate dressing as geometry-aware insertion (body-part/opening spatial relations instead of full deformable state) and train with RL using a staged curriculum plus a finger-wise insertion soft gate. Results: on rigid and deformable bracelet dressing the full method reaches 84.7 ± 1.2% post-training deformable success; the gate gives the largest gain, the curriculum on top gives the top score; 15/20 real-robot trials on a mannequin hand.

### [R²E: A Role-driven Reward Evolutionary Framework for Automated Reward Function Design](https://arxiv.org/abs/2610.32439)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接
- 🇨🇳 问题:基于 LLM 的奖励设计存在无差别采样、历史反馈利用不足,导致奖励空间探索不足和优化不稳定。方法:多个 LLM 角色分工——Explorer 扩大搜索、Guardian 保守精修、Evolver 通过交叉和变异重组高分奖励,配合动态调度(由探索到利用)和保存最优奖励的全局精英池。结果:在多个机器人任务上验证有效;预印本摘要未给出定量结果。
- 🇬🇧 Problem: LLM-based reward design suffers from undifferentiated sampling and weak use of history, leaving the reward space under-explored and optimization unstable. Method: specialized LLM roles — Explorer (novelty), Guardian (conservative refinement), Evolver (crossover/mutation) — coordinated by dynamic scheduling and a Global Elite Pool. Results: effective on multiple robotic tasks; the abstract gives no quantitative results.

### [RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms](https://arxiv.org/abs/2610.32971)
🏷️ 交叉方向 / Also: VLA(评测含 VLA 任务)
开源状态 / Code: ✅ 已开源 / Released — [robustrl-lib/robustrllib](https://github.com/robustrl-lib/robustrllib);Comments 与项目页 [robustrl-lib.github.io](https://robustrl-lib.github.io/) 给出代码与教程,匿名 `git ls-remote` 可访问
- 🇨🇳 问题:鲁棒 RL 算法复用性差,经验能力边界不清。方法:提供算法为中心的库与基准,在统一接口下集成 17 种代表性鲁棒在线、离线和安全 RL 算法,评测平台覆盖多样现实偏移以及先进的人形与 VLA 任务。结果:在 273 种扰动配置上系统评测,给出当前鲁棒 RL 算法的能力图谱,指出有效范围与仍存在的显著鲁棒性缺口。
- 🇬🇧 Problem: robust RL algorithms are hard to reuse and their empirical capability boundary is unclear. Method: an algorithm-centric library and benchmark integrating 17 robust online, offline and safe RL algorithms under one interface, with an evaluation platform spanning real-world shifts plus humanoid and VLA tasks. Results: a capability map over 273 perturbation configurations showing where methods work and where substantial robustness gaps remain.

### [From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot](https://arxiv.org/abs/2610.32271)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接
- 🇨🇳 问题:VLA 在固定基座机械臂上最成熟,装到四足上需同时协调底盘导航、机身姿态和末端运动(归入本类因目标任务是足式 loco-manipulation 控制)。方法:在 Unitree Go2 + AgileX Piper 上研究数据采集、模型适配与推理设计,报告使真机闭环部署可行的选择(模型变体、动作视野、示教约定),并在抓放任务上区分数据覆盖与模型容量。结果:扩大示教覆盖使留出集末端误差降低 30%,加入推、而非抓等次要技能能引入新行为模式而不损害基线性能;闭环真机实验表明数据集构成决定成败。
- 🇬🇧 Problem: VLAs are most mature on fixed-base arms; on a quadruped the policy must jointly coordinate base navigation, posture and end-effector (placed here because the target task is legged loco-manipulation control). Method: study data collection, adaptation and inference design on a Unitree Go2 with an AgileX Piper arm, reporting the choices (model variant, action horizon, demonstration conventions) that made closed-loop deployment feasible, with a pick-and-place study separating data coverage from capacity. Results: broader demonstration coverage cuts held-out end-effector error by 30%; secondary skills (pushing instead of grasping) add behavior modes without degrading the baseline; real-world closed-loop runs show how dataset composition shapes success and failure.

### [DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning](https://arxiv.org/abs/2610.32093)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ✅ 已开源 / Released — [DAVIAN-Robotics/DiscoDemo](https://github.com/DAVIAN-Robotics/DiscoDemo);项目页 [DiscoDemo](https://davian-robotics.github.io/DiscoDemo) 链接该仓库,匿名 `git ls-remote` 可访问
- 🇨🇳 问题:行为克隆对数据覆盖敏感,而收集多样成功示教成本高。方法:把 RL 当作下游模仿学习的数据生成器而非部署控制器——训练带并行反向课程和「成功门控多样性」目标的特权潜变量条件 RL 生成器,发现多种成功解法,经安全过滤后导出静态数据集。结果:四个操作任务上成功状态覆盖更广;下游成功率在仿真中由最强基线的 40% 升至 62%,真机由 39% 升至 78%,对预训练流匹配 VLA 的模仿学习也有帮助,且与纠正式数据收集互补。
- 🇬🇧 Problem: behavior cloning is sensitive to data coverage and diverse successful demonstrations are costly. Method: use RL as a data generator rather than a deployed controller — a privileged latent-conditioned RL generator with a parallel reverse curriculum and a success-gated diversity objective discovers multiple solution modes, which are safety-filtered and exported as a static dataset. Results: broader successful-state coverage on four manipulation tasks; downstream success rises from 40% (strongest baseline) to 62% in simulation and from 39% to 78% on a real robot, helping a pretrained flow-matching VLA and complementing corrective data collection.

### [Optimization, Optimal Control, and Reinforcement Learning for Robotics](https://arxiv.org/abs/2610.32538)
🏷️ 交叉方向 / Also: 运动控制·传统 / Classical(讲义,综合 OC 与 RL;含 RL,按规则归入 RL 类)
开源状态 / Code: ❓ 未知 / Unknown — 讲义,无代码链接;Comments 说明为初版讲义并将修订
- 🇨🇳 内容:面向机器人学的优化、最优控制与强化学习入门讲义,强调三者的数学联系与实践相关性。结论:内容为已有成熟材料的整理(非新研究),由作者与 AI 协作写作完成,为初版,暂无图表,后续将修订扩充。
- 🇬🇧 Content: lecture notes introducing optimization, optimal control and RL for robotics, emphasizing their mathematical connections. Conclusion: established material compiled rather than new research, written in human-AI collaboration; a preliminary first version without figures, to be revised and expanded.

**未展开(仅更新版本,摘要未显示实质更新,共 4 条)/ Replacements, not expanded (4):** [SMR](https://arxiv.org/abs/2610.29169)(人形流式动作重定向)、[LocoManiLab](https://arxiv.org/abs/2610.30876)(人形 loco-manipulation 测试平台)、[Robot Motion Transition with a Human Motion Prior (STAMP)](https://arxiv.org/abs/2610.30817)、[Revisiting Temporal Regularization for Smooth Control in Deep RL (CATS)](https://arxiv.org/abs/2610.07910)(项目页链接 [dmach1ne/CATS](https://github.com/dmach1ne/CATS),匿名可访问)。 / Updated versions of earlier papers; no evidence of substantive change, so not re-expanded.

---

## 运动控制·传统 / Motion Control · Classical

### [Multimodal MPC via Bayesian Set Optimization for Dynamic Manipulation of Deformable Linear Objects](https://arxiv.org/abs/2610.31852)
开源状态 / Code: ✅ 已开源 / Released — [Longyouyuan/BM2PC](https://github.com/Longyouyuan/BM2PC);摘要给出核心实现与视频,匿名 `git ls-remote` 可访问
- 🇨🇳 问题:可变形线状物(DLO)动态操作存在欠驱动高维动力学、变形响应延迟,以及障碍约束下存在多个可行运动。方法:提出 BM2PC(贝叶斯多模态 MPC),在 control-as-inference 后验基础上把多模态规划表述为兼顾控制质量与行为多样性的集合优化,增量更新维持多个控制模态,并加入执行动力学模型补偿快速操作下的执行失配。结果:无需任务特定策略训练,在轨迹跟踪上比学习型基线更好地泛化到未见轨迹;真机最长任务 RMSE 降低 44.0%;避障性能与现有多模态 MPC 相当而规划时间减少 29%–66%。
- 🇬🇧 Problem: dynamic manipulation of deformable linear objects is hard due to underactuated high-dimensional dynamics, delayed responses and multiple feasible motions under obstacles. Method: BM2PC formulates multimodal planning as set optimization over the control-as-inference posterior, balancing control quality and diversity with an incremental update that maintains several modes, plus an execution dynamics model compensating execution mismatch. Results: generalizes to unseen trajectories better than a learning-based baseline without task-specific training; real-world RMSE reduced by 44.0% on the longest task; matches multimodal-MPC baselines in obstacle avoidance with 29%–66% less planning time.

### [Graphs of Trajectory Bundles for Nonlinear Motion Planning](https://arxiv.org/abs/2610.32365)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为 "8 pages, 4 figures",无代码链接
- 🇨🇳 问题:非线性乃至黑箱动力学系统的运动规划难以同时满足动力学可行与复杂约束。方法:提出轨迹束图(GTB),在工作空间凸集图分解上,结合采样规划、轨迹优化与图搜索,迭代构建刻画各顶点局部动力学的轨迹束图,通过最短路径求解得到极限下满足系统动力学的最大动力学可行迭代解,碰撞避免、安全或规范约束由图构造本身保证。结果:可处理高度非线性、不稳定甚至黑箱动力学与复杂碰撞/规范约束;预印本摘要未给出定量结果。
- 🇬🇧 Problem: motion planning for nonlinear or black-box dynamics must satisfy dynamics and complex constraints together. Method: GTB combines sampling-based planning, trajectory optimization and graph search over a graph-of-convex-sets decomposition, iteratively building a graph of trajectory bundles that captures local dynamics, then solving a shortest-path problem to get maximally dynamically feasible iterates that satisfy dynamics in the limit; collision/safety/specification constraints hold by construction. Results: handles highly nonlinear, unstable and black-box dynamics with complex constraints; the abstract gives no quantitative results.

### [Not an Accident: Exploiting Safety Filter Inadequacy in Humanoid Robots](https://arxiv.org/abs/2610.31923)
🏷️ 交叉方向 / Also: 安全 / Security(cs.RO 交叉列表)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接
- 🇨🇳 问题:人形机器人用安全滤波器提供「控制动作不致碰撞」的数学保证,但保证仅在安全参数配置正确时成立,而正确参数因任务和环境而异、没有通用确定方法。方法:提出「目标插入攻击」——攻击者仅通过正常用户交互即可利用滤波器缺陷,并开发自动化工具 SIREN 为给定任务与环境寻找易受攻击的插入目标。结果:SIREN 在 SPARK 数据集的所有存在漏洞的场景中都找到攻击,发现的攻击数是基线的三倍;并能对真实人形生成攻击,使其在执行任务时发生碰撞。
- 🇬🇧 Problem: humanoid safety filters give collision-avoidance guarantees only when safety parameters are configured correctly, and no general method exists to choose them per task/environment. Method: goal-insertion attacks that need only normal user interactions, and SIREN, an automated tool that finds vulnerable inserted goals for a given task and environment. Results: SIREN finds attacks in all vulnerable scenarios of the SPARK dataset, three times as many as a baseline, and generates attacks that make a real humanoid collide during tasks.

### [FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation](https://arxiv.org/abs/2610.31841)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(LLM 编码智能体;目标任务为接触丰富操作的力反馈控制逻辑,按任务归入控制类)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅给项目页 [FORCA](https://tanoom.github.io/forca/),页面未发现自有代码仓库链接
- 🇨🇳 问题:接触丰富的操作需要生成并改进对物理交互有响应的控制逻辑。方法:编码智能体以视觉观测和腕部力/力矩读数为输入,编写接触探测与力响应运动的 Python 程序,并在两次执行之间对照力记录与视觉结果诊断失败、修改运动与力反馈控制逻辑;无需示教、任务特定训练或仿真。结果:在 5 个真机任务上展示了提升操作精度、适应物体/表面属性变化、在表面变化和物体运动下调节接触三类能力;相比同一智能体的纯视觉变体,提高了抓取精度与任务成功率,并减少了擦拭和削皮中的接触丢失(摘要未给出具体数值)。
- 🇬🇧 Problem: contact-rich manipulation needs control logic that responds to physical interaction. Method: a coding agent takes vision and wrist force/torque readings, writes Python programs for contact probing and force-responsive motion, and between executions inspects force records with visual outcomes to revise motion and force-feedback logic — no demonstrations, task-specific training or simulation. Results: across five real-robot tasks it improves accuracy, adapts to object/surface changes and regulates contact under surface variation and object motion; versus a vision-only variant it raises grasp accuracy and success and reduces contact loss in wiping and peeling (no numbers in the abstract).

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

### [FLORA: An Open Model Suite for Scaling Robotics Data Engines](https://arxiv.org/abs/2610.31779) — NVIDIA(据仓库 / per repo)
🏷️ 交叉方向 / Also: VLA(服务 GR00T 训练)
开源状态 / Code: ✅ 已开源 / Released — [NVIDIA/Flora](https://github.com/NVIDIA/Flora);README 链接项目页、论文及 Hugging Face 模型集合,HF Daily Papers 的 githubRepo 字段一致,匿名 `git ls-remote` 可访问
- 🇨🇳 问题:机器人基础模型的全生命周期依赖数据标签——部署监控需要结果奖励,RL 后训练需要过程奖励,预训练数据过滤需要带时间戳的字幕。方法:提出 Flora,训练 GR00T 所用的工业级数据引擎,同时覆盖字幕、结果奖励和过程奖励三种能力。结果:在字幕基准 WGO-Bench 与奖励基准 RoboReward、Robometer 上达到 SOTA;内部基准上与 GPT-6 Astra 相当且优于其他前沿模型,成本约为其 1/125;已在 512 块 GB300 上每天标注 20 万小时数据,并开源。
- 🇬🇧 Problem: the robotics foundation-model life cycle depends on labels — outcome rewards for deployment monitoring, process rewards for RL post-training, timestamped captions for pretraining data. Method: Flora, the industrial data engine used to train GR00T, covering all three. Results: SOTA on WGO-Bench (captioning) and RoboReward / Robometer (reward); competitive with GPT-6 Astra internally while ~125x cheaper; labels 200,000 hours of data per day on 512 GB300s; open-sourced.

### [RynnUnify: Towards Unified Embodied Brain](https://arxiv.org/abs/2610.32965) — 阿里达摩院(据仓库 / Alibaba DAMO per repo)
🏷️ 交叉方向 / Also: 世界模型与 WAM / World Model & WAM、空间智能 / Spatial、VLA(世界-动作扩展控制的是操作,而非运动控制主贡献)
开源状态 / Code: ✅ 已开源 / Released — [alibaba-damo-academy/RynnUnify](https://github.com/alibaba-damo-academy/RynnUnify);HF Daily Papers githubRepo 字段与 radar new_repos(18★)一致,匿名 `git ls-remote` 可访问
- 🇨🇳 问题:需要把对物理世界的理解与对其演化的视觉预期统一在一个具身「大脑」中。方法:16B 统一具身模型,通过交错视频-语言推理结合具身理解与长时程视觉规划;通过 RL 做智能体扩展,选择性使用视频预测推理未观测状态;并给出世界-动作扩展把理解/预测转为机器人控制;提出 Rynn-VP 与 Rynn-GEU 基准。结果:在评测的统一多模态模型中具身理解平均分最高,Rynn-VP 总分比 Cosmos 3 Nano 高 9.75 分;智能体扩展使 Rynn-GEU 平均提升 6.0 分;世界-动作扩展在 20 个 RoboCasa365 复合任务上成功率 51.5%,三项真机任务平均 46.7%。
- 🇬🇧 Problem: unify understanding of the physical world with visual anticipation of how it evolves. Method: a 16B unified embodied model combining embodied understanding with long-horizon visual planning via interleaved video-language reasoning, an RL-based agentic extension that selectively uses video predictions, and a world-action extension for robot control; introduces Rynn-VP and Rynn-GEU benchmarks. Results: highest average embodied understanding score among evaluated unified models; +9.75 on Rynn-VP over Cosmos 3 Nano; +6.0 on Rynn-GEU average from the agentic extension; 51.5% on 20 composite RoboCasa365 tasks and 46.7% average over three real-robot tasks.

### [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://arxiv.org/abs/2610.31670)
🏷️ 交叉方向 / Also: VLA、世界模型与 WAM / WAM
开源状态 / Code: ✅ 已开源 / Released — [yunfeixie233/sensorimotor-alignment](https://github.com/yunfeixie233/sensorimotor-alignment);Comments 称项目页与代码可用,匿名 `git ls-remote` 可访问
- 🇨🇳 问题:机器人基础模型通常靠昂贵的闭环 rollout 评估,需要低成本离线代理。方法:受柏拉图表征假说启发,提出训练无关的离线指标 Sensorimotor Alignment(S²),衡量模型感知表征与物理运动几何的对齐程度。结果:S² 与跨模型家族的下游机器人任务成功率正相关,可在闭环评估前筛选模型,并能在昂贵微调成 VLA 之前识别有前景的 VLM 骨干,还可为 VLA 与 WAM 中观察到的现象提供表征层面的解释(摘要未给出具体相关系数)。
- 🇬🇧 Problem: robot foundation models are evaluated with costly closed-loop rollouts and need cheap offline proxies. Method: inspired by the Platonic Representation Hypothesis, S² is a training-free offline metric of how well a model's sensory representation aligns with the geometry of physical motion. Results: S² correlates positively with downstream task success across model families, helps prioritize models before closed-loop evaluation, identifies promising VLM backbones before fine-tuning into VLAs, and explains phenomena in VLAs and WAMs (no coefficients in the abstract).

### [WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations](https://arxiv.org/abs/2610.31834)
🏷️ 交叉方向 / Also: 空间智能与 SLAM / 3D 重建、世界模型 / Simulation
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接
- 🇨🇳 问题:仿真中的机器人学习需大量人工搭建场景与任务,而真实示教提供了多样的真实观测。方法:提出智能体式 real-to-sim 框架,把构建过程表述为迭代精修「可执行世界程序」——编码智能体分解场景、规划重建步骤、编排图像与 3D 生成工具,并以相机位姿锚定的场景表示(静态视觉上下文、支撑几何、可编辑交互资产)诊断和修正重建误差。结果:在 DROID 上能重建视觉忠实且几何一致的交互世界,并保持记录的机器人轨迹的物理有效性(摘要未给出具体数值)。
- 🇬🇧 Problem: robot learning in simulation needs heavy manual scene/task construction while in-the-wild demonstrations offer diverse real observations. Method: an agentic real-to-sim framework treating construction as iterative refinement of an executable world program — a coding agent decomposes the scene, plans reconstruction and orchestrates image/3D generation tools, using a camera-pose-anchored representation (static context, support geometry, editable interactive assets) to diagnose errors. Results: on DROID it reconstructs visually faithful, geometrically consistent interactive worlds while preserving the physical validity of recorded trajectories (no numbers in the abstract).

### [DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection](https://arxiv.org/abs/2610.32969) — Amazon FAR(据仓库名 / per repo name)
开源状态 / Code: ✅ 已开源 / Released — [amazon-far/dexport](https://github.com/amazon-far/dexport);项目页 [DexPort](https://amberxie88.github.io/dexport/) 链接该仓库,匿名 `git ls-remote` 可访问
- 🇨🇳 问题:灵巧操作的示教采集是瓶颈——遥操作需完整机器人且手指协调负担重,人类示教又需估计并重定向动作。方法:便携式手持接口,采集与部署使用同一灵巧手硬件,同时记录指令关节目标与实测关节状态;操作者移动手持接口指定手腕运动,并选择/调整技能来协调手指,再用行为克隆训练视觉运动策略。结果:在 4 个任务上评估,采集 2500 多条示教;使用记录的机器人指令而非状态,成功率由 11% 提升到 64%;使用野外数据,任务成功率由 36% 提升到 78%。
- 🇬🇧 Problem: dexterous demonstration collection is a bottleneck — teleoperation needs a full robot and burdens finger coordination, human demos need estimation and retargeting. Method: a portable hand-held interface using the same robot hand for collection and deployment, recording commanded targets and measured states; operators move the wrist and select/adjust skills coordinating the fingers, then behavior cloning trains visuomotor policies. Results: over 4 tasks and 2,500+ demonstrations, using recorded commands instead of states improves success from 11% to 64%, and in-the-wild data lifts success from 36% to 78%.

### [DynaSlots: Slot-Centric 3D Dynamics Pretraining for Robot Manipulation](https://arxiv.org/abs/2610.32330)
开源状态 / Code: ❓ 未知 / Unknown — 摘要称 "Code is available",但链接是匿名化项目页(`zhucezhanghao12345-source.github.io/DynaSlots-Anonymous`),非可核实的官方仓库,待核实
- 🇨🇳 问题:现有 3D 视觉预训练在场景级建模状态转移,把多个运动部件压成单个全局潜动作,混淆语义不同的转移。方法:无动作、无标签的预训练框架 DynaSlots,将点云帧分解为少量时间一致的槽位,时序槽位传播保证一致性,逆动力学模型为每个槽位提取潜动作,扩散式前向动力学模型加自监督交互头预测每个槽位的未来状态。结果:在 Meta-World、Adroit 和 RealMan RM65-B 机器人上优于场景级基线,仿真成功率更高,真机上对杂乱场景和未见物体表现出较强鲁棒性(摘要未给出具体数值)。
- 🇬🇧 Problem: existing 3D visual pretraining models transitions at scene level, compressing all motion into one global latent action. Method: DynaSlots, action- and label-free, decomposes point-cloud frames into temporally consistent slots (temporal slot propagation), extracts one latent action per slot with an inverse dynamics model, and predicts each slot's future with a diffusion forward model plus a self-supervised interaction head. Results: outperforms scene-level baselines on Meta-World, Adroit and a RealMan RM65-B robot, with higher simulated success and robustness to clutter and unseen objects in real-world manipulation (no numbers in the abstract).

### [Predictive Long-Horizon Progress Modeling with Action-Aware Quantification](https://arxiv.org/abs/2610.32776)
🏷️ 交叉方向 / Also: 运动控制·RL(进度评论家可用于 RL 过程奖励,但本文贡献为数据/基准/评论家模型)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接
- 🇨🇳 问题:稠密任务进度反馈对数据整理、策略评估和 RL 至关重要,但现有标注依赖稀疏关键帧和主观人工判断。方法:提出动作感知量化——用 VLM 把长时程轨迹分解为物体级子任务并分配加权动作信用,构建 800+ 小时训练视频数据集和含 19,618 个人工校准评估帧的基准 LOOM,并提出预测式进度评论家 NimCritic(联合视频-进度学习、历史进度扰动、对比式视频-进度对齐)。结果:NimCritic 在 VPB 与 LOOM 上持平或超过最先进过程奖励模型,VPB 终端成功准确率比 GVL (GPT-6-Sol) 高约 65%;在 RoboArena 上检索人工选择的成功 rollout 总体召回约 97%。
- 🇬🇧 Problem: dense progress feedback matters for data curation, policy evaluation and RL, but existing annotations rely on sparse, subjective keyframes. Method: action-aware quantification (VLM decomposes trajectories into object-level subtasks with weighted action credits), an 800+ hour dataset, the LOOM benchmark (19,618 human-calibrated frames), and NimCritic, a predictive progress critic trained with joint video-progress learning, historical progress perturbation and contrastive alignment. Results: matches or beats process reward models on VPB and LOOM, ~65% above GVL (GPT-6-Sol) in terminal success accuracy on VPB, and ~97% overall recall retrieving human-selected successful rollouts on RoboArena.

### [RoboCode: Learning Reusable Action Primitives for Robot Manipulation](https://arxiv.org/abs/2610.32225)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为 "12 pages, 5 figures",无代码链接
- 🇨🇳 问题:现有操作策略直接预测连续动作块,未显式建模跨任务共享的短时程运动模式。方法:RoboCode 通过共享的软门控原语动作接口,把每个动作块表示为多个学习到的原语的软组合;接口从多任务动作块中学得并冻结,再训练任务特定状态编码器映射到共享隐空间。结果:在 5 个 ManiSkill 任务上,动作块重建平均 MSE 为 0.0187,代码激活显示结构化的跨任务复用,闭环成功率在所有任务上最高或并列最高,平均 75.6%,对比 ACT 的 68.8% 与更大的 Diffusion Policy 基线的 41.6%。
- 🇬🇧 Problem: manipulation policies usually predict continuous action chunks without modeling reusable short-horizon patterns shared across tasks. Method: RoboCode represents each action chunk as a soft composition of learned primitives via a shared soft-gated interface, learned from pooled multi-task chunks and frozen while task-specific state encoders map into the shared latent. Results: on five ManiSkill tasks, average reconstruction MSE 0.0187, structured code reuse across tasks, and highest or tied closed-loop success on all tasks — 75.6% average versus 68.8% for ACT and 41.6% for the larger Diffusion Policy baseline.

### [SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning](https://arxiv.org/abs/2610.32978)
🏷️ 交叉方向 / Also: 空间智能 / Spatial(3D 场景生成;cs.RO 交叉列表)
开源状态 / Code: ✅ 已开源 / Released — [Tinaliu0123/scenebloom](https://github.com/Tinaliu0123/scenebloom);摘要给出该链接,匿名 `git ls-remote` 可访问
- 🇨🇳 问题:训练可泛化具身智能体需要真实、多样、可仿真的室内环境;语言引导方法空间落地不足,视觉生成模型的输出又需几何推理才能成为物理有效的 3D 场景。方法:SceneBloom 把视觉布局采样与契约引导的 3D 编译结合——分层采样器用扩散先验在功能区内生成家具布局,编译器依据每个提案提取的关系引导几何拟合与局部位姿校正。结果:在五种房间类型上视觉质量与物理稳定性最高,是唯一没有检测到网格碰撞和越界物体的方法,布局分布更接近真实房间;在这些场景中训练的物体导航策略在留出真实扫描上的成功率高于用等量真实训练扫描训练的策略。
- 🇬🇧 Problem: embodied agents need realistic, varied, simulation-ready indoor scenes; language-guided methods lack spatial grounding and visual generative outputs need geometric reasoning to become valid 3D scenes. Method: SceneBloom combines visual layout sampling (hierarchical diffusion-prior sampler within functional zones) with contract-guided 3D compilation (relations drive geometric fitting and pose correction). Results: best visual quality and physical stability over five room types, the only method with no mesh collisions or out-of-bounds objects, layouts closest to real rooms; object-navigation policies trained on these scenes beat those trained on an equal number of real scans on held-out real scans.

### [LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners](https://arxiv.org/abs/2610.32348)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为 "19 pages, 11 figures, 10 tables",无代码链接
- 🇨🇳 问题:基于前沿 VLM 的机器人规划器如何记忆整个操作回合是开放问题——每帧都消耗 token,每步重写笔记效果差。方法:LogLook 的执行落地记忆保留执行日志与模型先前笔记,由模型决定看哪里:仅在预期有变化处返回帧,先浏览示教再检查自选部分。结果:用基准自带运动规划器测量时,以少 43% 的 token 和不到一半的图像匹配仅笔记记忆的成功率,并减少因记忆/观察导致的失败;直接控制下解决 RoboMME 测试集的 93.5%。
- 🇬🇧 Problem: how a frontier-VLM robot planner should remember an episode is open — frames cost tokens and rewriting notes each step is poor. Method: LogLook keeps an execution log and earlier notes while the model decides where to look (frames returned only where change is expected; demonstrations skimmed first). Results: with the benchmark's motion planner it matches note-only memory with 43% fewer tokens and under half the images, with fewer memory/perception failures; with direct control it solves 93.5% of the RoboMME test set.

### [KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations](https://arxiv.org/abs/2610.31801)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空;摘要给出项目页 [KiRoSe](https://berkeleyautomation.github.io/kirose/),未核对页面是否含代码链接
- 🇨🇳 问题:机器人示教分割多靠人工,直接把多相机视频喂给 MLLM 又昂贵、易耗尽上下文。方法:KiRoSe 聚焦伴随的运动学数据流,借鉴熵编码思想提出稀疏运动 token(SMT),一种紧凑表示重复出现的、时间局部的运动学事件的离散词表,并用子任务标注监督开源语言模型解读 token 序列。结果:对人工标注分割的 F1 质量显著优于基线,并可零样本迁移到未见机器人形态和第一视角人类运动,同时保留语言模型的开放词汇知识,还能在未见机器人上跟踪任务进度并检测动作被反向(摘要未给出具体数值)。
- 🇬🇧 Problem: demonstration segmentation is manual, and feeding multi-camera video to MLLMs is costly. Method: KiRoSe uses the kinematic stream with Sparse Motion Tokens (SMTs), a discrete vocabulary of recurring kinematic events inspired by entropy coding, and supervises an open language model with subtask annotations to interpret token sequences. Results: substantially better F1 than baselines against human labels, zero-shot transfer to unseen embodiments and egocentric human motion while keeping open-vocabulary knowledge, plus progress tracking and reversal detection (no numbers in the abstract).

**未展开 / Listed only (1,共 12 条相关):** [Conditional Neural Processes for Self-Supervised Goal Discovery in Action Imitation](https://arxiv.org/abs/2610.32688)(IROS 2023 研讨会海报,仅给出注意力促进目标表示涌现的定性结论)。 / 1 workshop-poster paper listed by name; 11 of 12 expanded.

---

## VLA

### [EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions](https://arxiv.org/abs/2610.31845)
开源状态 / Code: ✅ 已开源 / Released — [LinShan-Bin/EgoForesight](https://github.com/LinShan-Bin/EgoForesight);项目页 [EgoForesight](https://lin-shan.com/EgoForesight) 链接该仓库,匿名 `git ls-remote` 可访问
- 🇨🇳 问题:机器人示教质量高但昂贵,第一视角视频覆盖广但重建/重定向引入噪声动作标签。方法:VLA 框架联合学习两类数据——可靠性条件化的损坏与可靠性加权回归降低不可靠标签影响,并通过联合视觉-动作流耦合未来视觉表征预测与动作生成,用特权未来表征蒸馏(EMA 教师)提供结果监督。结果:缩放斜率更陡;在 30,000 小时预训练数据下,真实世界开环动作 MSE 降低 20.5%,RoboCasa 少样本成功率提高 8.1 个百分点,后训练在仿真与真机灵巧操作上也有强表现。
- 🇬🇧 Problem: robot demos are high quality but costly; egocentric video is broad but retargeting adds noisy action labels. Method: a VLA framework with reliability-conditioned corruption and reliability-weighted regression to down-weight unreliable labels, a joint vision-action flow coupling future-representation prediction with action generation, and privileged-future representation distillation from an EMA teacher. Results: steeper scaling slopes; at 30,000 hours of pretraining, real-world open-loop action MSE −20.5% and RoboCasa few-shot success +8.1 points, with strong post-trained simulated and real dexterous manipulation.

### [Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies](https://arxiv.org/abs/2610.32102)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空;项目页 [Horizon-Depth-VLA](https://jiabingyang01.github.io/Horizon-Depth-VLA/) 未检出代码链接
- 🇨🇳 问题:流匹配 VLA 需要在实时响应与执行稳定性间平衡,而求解器深度与执行视野通常被当作独立选择。方法:揭示二者存在由「符号反转」支配的耦合——粗数值积分在快速重规划下降低精度,但在长开环执行下显著提升表现;几何上数值截断收缩围绕不变轨迹质心的横向动作离散度,起到抑制开环漂移的隐式正则作用。结果:在 LIBERO、RoboTwin 2.0 和 Franka 真机上,对 π0、π0.5、GR00T 等骨干,免训练、无需改架构即可一致提升任务成功率并大幅降低推理延迟(摘要未给出具体数值)。
- 🇬🇧 Problem: flow-matching VLAs must balance responsiveness and stability, yet solver depth and execution horizon are treated as independent. Method: reveals a compute-execution coupling with a sign reversal — coarse integration hurts precision under rapid replanning but helps under extended open-loop commitment, since truncation contracts lateral action dispersion around an invariant centroid (implicit regularizer against drift). Results: across LIBERO, RoboTwin 2.0 and real Franka on π0, π0.5 and GR00T, training-free joint tuning gives higher success and much lower latency (no numbers in the abstract).

### [Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates](https://arxiv.org/abs/2610.31859)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接(修复为 LeRobot SmolVLA 的一行改动)
- 🇨🇳 问题:VLA 以 bf16 微调且无 fp32 主副本时,AdamW 的小于权重 1/512 的更新会被舍入抹去。方法:审计 12 个开源 VLA 代码库,其中 9 个默认或文档化配方这样训练(4 个为全权重矩阵,含 LeRobot 的 SmolVLA 默认及 π0/π0.5 指南);在 LIBERO 上每 100 步探测更新被抹去比例。结果:无主副本时至少 79% 的更新被抹去;LIBERO-Object 上 fp32 副本使 SmolVLA 成功率由 4.3% 升至 49.3%、π0.5 由 5.1% 升至 80.9%(学习率低十倍),默认学习率下 π0.5 由 89.0% 升至 97.7%;HF Hub 抽样中 99% 的 SmolVLA 全权重微调以 bf16 存储动作专家。
- 🇬🇧 Problem: fine-tuning VLAs in bf16 without an fp32 master copy rounds away AdamW updates smaller than 1/512 of a weight. Method: audit 12 open VLA codebases (9 default to such recipes, 4 on full weight matrices incl. LeRobot's SmolVLA default and π0/π0.5 guides) and probe erased updates every 100 steps on LIBERO. Results: ≥79% of updates erased; on LIBERO-Object an fp32 copy raises SmolVLA from 4.3% to 49.3% and π0.5 from 5.1% to 80.9% (10x lower LR), and π0.5 at its default rate from 89.0% to 97.7%; 99% of sampled full-weight SmolVLA fine-tunes on the Hub store the action expert in bf16.

### [Retiming Robot Demonstrations with a Learned Speed Prior](https://arxiv.org/abs/2610.32676)
🏷️ 交叉方向 / Also: 运动控制·传统(带实时最优控制层)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空;项目页 [learned_speed_prior](https://mllab.snu.ac.kr/projects/learned_speed_prior) 未检出代码链接
- 🇨🇳 问题:示教速度由遥操作者而非任务决定,策略会继承操作者特有的节奏。方法:直接从大规模示教数据学习速度先验——给定指令、运动路径和沿途图像,预测沿路径的执行速度分布,按所选分位数定义一致时钟来重新定时示教,再微调 VLA;执行时配合实时最优控制层按预测节奏跟踪动作块。结果:在 120 个 RoboLab 任务上,用学习时钟微调的策略成功率更高,抖动最多减半;真机叠杯 3.50 s,比默认策略的 6.02 s 快 1.72 倍,成功次数同为 29/30。
- 🇬🇧 Problem: demonstration pace is set by the teleoperator, and policies inherit operator-specific timing. Method: learn a speed prior from large-scale data (instruction, path, images → speed distribution), pick a quantile as a consistent clock to retime demos before fine-tuning a VLA, and execute with a real-time optimal-control layer tracking action chunks at the predicted pace. Results: on 120 RoboLab tasks, fine-tuning on learned clocks gives higher success and up to half the jerk; on a real robot, cup stacking takes 3.50 s versus 6.02 s (1.72x faster) with 29/30 successes in both.

### [MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation](https://arxiv.org/abs/2610.32312)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为 "Accepted to CoRL 2026",无代码链接
- 🇨🇳 问题:多技能 VLA 对「执行哪个原语技能」和「在哪里/如何接触并移动物体」建模不足。方法:MAST-VLA 在 LLM 骨干中加入技能条件的 LoRA-MoE 适配器(技能查询 token 与路由偏置引导专家特化),并把预测的可供性热图转换为面向动作头的 patch 级轨迹-可供性空间先验。结果:在 CALVIN ABC→D 长时程多技能跨场景泛化设定上达到 SOTA,五子任务序列平均长度 4.65;真机多技能序列实验验证了对真实感知和控制噪声的可部署性。
- 🇬🇧 Problem: multi-skill VLAs under-model which primitive skill to run and where/how to contact and move objects. Method: skill-conditioned LoRA-MoE adapters in the LLM backbone (skill-query tokens and routing biases) plus a patch-level trajectory-affordance prior derived from a predicted affordance heatmap for the action head. Results: SOTA on CALVIN ABC→D with average length 4.65 over five-subtask sequences; real-robot multi-skill sequences confirm deployability under perception and control noise. (CoRL 2026.)

### [If at First You Don't Succeed, Backtrack: Lightweight Recovery for Frozen VLAs](https://arxiv.org/abs/2610.32941)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为 "17 pages, 1 figure, 14 tables",无代码链接
- 🇨🇳 问题:VLA 进入训练数据罕见状态后易失败,恢复通常需要恢复示教、重训或额外模型。方法:Backtrack 在冻结 VLA 上加一个小型失败预测头(只用带结果标签的 rollout 训练,读取 VLA 内部表征,仅增加 0.48%–0.88% 参数);失败概率超过阈值时控制器暂停策略、回溯机械臂近期已实现的运动,再交还给未改动的策略重试。结果:在 LIBERO-Long 上对 SmolVLA、π0.5、π0-FAST 三个 VLA 失败率降低 19%–48%,成功率最多提升 7.4 个百分点;较短套件(基线已 85%–99%)效果较小;MetaWorld 上 SmolVLA 的全部 12 种控制器配置均优于无辅助策略。
- 🇬🇧 Problem: VLAs are brittle once their own actions lead to poorly covered states, and recovery usually needs recovery demos, retraining or a separate model. Method: Backtrack adds a small failure-prediction head (trained on outcome-labeled rollouts, reading internal representations, +0.48–0.88% parameters); above a threshold a controller pauses the policy, retraces recently achieved arm motion and hands control back to retry. Results: on LIBERO-Long it cuts failure rates by 19–48% for SmolVLA, π0.5 and π0-FAST (up to +7.4 points success), with smaller effects on shorter suites (85–99% baseline); all twelve controller configurations beat unassisted SmolVLA on MetaWorld.

### [Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems](https://arxiv.org/abs/2610.32208)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为 CoRL 2026 研讨会(非归档),无代码链接
- 🇨🇳 问题:VLA 的成败难以诊断和理解。方法:对 OpenVLA 激活做稀疏自编码器(SAE)表征,识别与成败特定阶段相关的单个 SAE 特征,定位特征激活显著变化的时间区间,并用 VLM 解释流水线生成行为描述并在留出区间验证。结果:SAE 表征含有可预测结果的信息,可在机器人到达不可恢复状态前预测任务失败;预印本摘要未给出定量结果。
- 🇬🇧 Problem: VLA successes and failures are hard to diagnose. Method: sparse-autoencoder representations of OpenVLA activations, identification of SAE features tied to stages of success/failure, localization of temporal intervals with significant activation changes, and a VLM-based pipeline describing the patterns, validated on held-out intervals. Results: SAE features contain outcome-predictive information and can predict failure before an unrecoverable state; the abstract gives no quantitative results.

### [TTT in VLA Models: Exploring Training with Human Demonstrations](https://arxiv.org/abs/2610.32094)
开源状态 / Code: ❓ 未知 / Unknown — Comments:来自 standard-robots 公司的技术报告,无代码链接
- 🇨🇳 问题:长时程任务需要保留并利用过去信息。方法:把测试时训练(TTT,用快速权重存储上下文)接入 InternVLA-A1 与 π0.5,通过配对示教-机器人轨迹训练研究以人类示教为条件的动作生成,实现两阶段间记忆迁移与截断反向传播,并考察训练目标、梯度覆盖和对比正则。结果(负面):在当前规模下加入 TTT 与配对训练并未带来一致的基于示教的目标选择;更短序列、全轨迹梯度连通和对比正则也未明显提升对示教的响应;示教降为单帧线索时,真机仍偏好固定位置的杯子。
- 🇬🇧 Problem: long-horizon tasks need retained past information. Method: integrate test-time training (fast-weight context) into InternVLA-A1 and π0.5, training on paired demonstrations and robot trajectories with memory transfer and truncated backpropagation, and varying objectives, gradient coverage and contrastive regularization. Results (negative): at the tested scale, TTT and paired training did not give consistent demonstration-based target selection; shorter sequences, full gradient connectivity and contrastive regularization did not clearly help; with single-frame cues the real robot still preferred cups at fixed positions.

### [When Human Corrections Travel: Safety in Federated VLA Adaptation](https://arxiv.org/abs/2610.32888)
开源状态 / Code: ❓ 未知 / Unknown — 立场论文,Comments 为 CoRL 2026 SPAIS 研讨会,无代码链接
- 🇨🇳 内容:探讨 VLA 对本地人类干预的适应与联邦学习结合时,跨任务、环境、人和机器人形态共享人类纠正的风险——共享更新可能提升平均成功率却抑制罕见的安全干预或在另一机器人上产生不安全响应。结论:提出三点要求(保留多模态纠正的上下文与不确定性、在接收机器人闭环中评估候选更新、同时评估泄露与安全关键证据的保留),给出反例和可证伪的评估议程,不含实验结果。
- 🇬🇧 Content: examines combining VLA adaptation to local human interventions with federated learning, where a shared update may raise mean success yet suppress a rare safety intervention or be unsafe on another robot. Conclusion: three requirements — preserve context/uncertainty of multimodal corrections, assess updates in each receiving robot's closed loop, evaluate leakage alongside retention of safety evidence — with counterexamples and a falsifiable agenda; no experimental results.

另见 / See also: [From Tabletop to Walking Bot](https://arxiv.org/abs/2610.32271)(已归入 运动控制·RL / Motion Control · RL)、[DiscoDemo](https://arxiv.org/abs/2610.32093)(已归入 运动控制·RL)、[RobustRLlib](https://arxiv.org/abs/2610.32971)(已归入 运动控制·RL)。本类共 9 条相关,全部已展开。 / 9 relevant, all expanded.

---

## VLN

### [See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space (RepresentNav)](https://arxiv.org/abs/2610.31762)
🏷️ 交叉方向 / Also: 世界模型 / World Model(潜在 CoT 的 JEPA 预测涌现为紧凑世界模型)、具身基础模型
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://wang-yinxi.github.io/representnav/)写有 "Code: coming soon"
- 🇨🇳 问题:导航策略应基于什么视觉表征行动——现有做法把表征设计留给编码器预训练目标。方法:RepresentNav 用「表征残差」(三层 Transformer,关注多个视觉基础模型的全深度特征)构建由策略自身目标塑造的表征空间,并在每步动作前通过潜在思维链预测一小段时间后的场景表征,以 JEPA 方式与策略端到端训练。结果:在 VLNVerse、VLN-CE R2R、EVT-Bench 和两个点目标基准上刷新 SOTA,真机在杂乱和移动人群中也有收益;VLNVerse fine-grained 成功率 83.80%,比此前最佳高 20.05 个百分点,EVT-Bench 干扰跟踪单相机达 85.5%(+10.1);「梦」使碰撞减少四分之一,且单个梦潜变量可解码未来深度、语义和 3D 占据(占据从未被监督)。
- 🇬🇧 Problem: what visual representation should a navigation policy act on — current systems leave representation design to encoder pretraining. Method: RepresentNav builds a self-constructed space with Representation Residuals (a three-layer transformer over multi-depth features of several vision foundation models) and, before each action, a latent chain-of-thought predicts the next-moment scene representation, trained end-to-end as a JEPA. Results: new SOTA on VLNVerse, VLN-CE R2R, EVT-Bench and two point-goal benchmarks, with gains on a physical robot among clutter and people; 83.80% on VLNVerse fine-grained (+20.05 points), 85.5% on EVT-Bench distracted tracking with a single camera (+10.1); dreaming cuts collisions by a quarter and the latent decodes future depth, semantics and 3D occupancy (never supervised).

### [HGWM: Hierarchical Graph-Guided World Model for Zero-Shot Object Navigation via Graph Matching](https://arxiv.org/abs/2610.32554)
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空;摘要提到实现已修复并通过离线测试,但无代码链接
- 🇨🇳 问题:零样本物体导航需要选择搜索方向并保留先前观测的证据。方法:HGWM 将 LLM 生成的房间锚点先验与持久的空间-语义记忆耦合——粗阶段给候选朝向打 0–10 的视觉语义分,细阶段度量观测物体、房间上下文与目标先验的符号相容性,阶段相关融合后结合 LLM 方向建议选择局部动作。结果:HM3D v0.1 上 SR 62.6%、SPL 31.5%(WMNav 为 58.1%/31.2%);MP3D 上 46.8%/17.9%(45.4%/17.2%);HM3D v0.2 上 74.4%/31.9%;消融使 SR 降 0.9–2.3 点、SPL 降 0.6–1.5 点;均为作者报告的聚合数,仅在仿真中评估,无逐回合记录。
- 🇬🇧 Problem: zero-shot object navigation must choose where to search while retaining evidence from past observations. Method: HGWM couples an LLM-generated room-anchor prior with persistent spatial-semantic memory — a coarse stage scores candidate headings (0–10), a fine stage measures symbolic compatibility of objects, room context and goal prior, fused phase-dependently with an LLM direction recommendation. Results: HM3D v0.1 SR 62.6% / SPL 31.5% (WMNav 58.1% / 31.2%); MP3D 46.8% / 17.9% (45.4% / 17.2%); HM3D v0.2 74.4% / 31.9%; ablations cut SR by 0.9–2.3 and SPL by 0.6–1.5; author-reported aggregates, simulation only, no episode-level records.

### [SP-Guide: Enhancing Aerial Vision-Language Navigation with Spatial Priors](https://arxiv.org/abs/2610.32697)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接
- 🇨🇳 问题:空中视觉语言导航(AVLN)中,现有方法把以视角为中心的 RGB 观测与全局锚定的历史地图当作通用视觉嵌入融合,跨模态空间对齐只能从稀疏导航监督中学习。方法:SP-Guide 是基于 Transformer 的目标预测框架,包含空间先验跨模态编码器、指令增强解码器和用于终端目标精修的目标收敛过滤器。结果:在 CityNav 基准上成功率优于代表性基线,在未见环境中增益最大;预印本摘要未给出具体数值。
- 🇬🇧 Problem: in aerial VLN, view-centered RGB and globally anchored history maps are fused as generic embeddings, leaving cross-modal spatial alignment to sparse supervision. Method: SP-Guide, a transformer goal-prediction framework with a Spatial Prior Cross-Modal Encoder, an Instruction Enhanced Decoder and a Goal Convergence Filter. Results: higher success rate than representative baselines on CityNav, largest on unseen environments; no specific numbers in the abstract.

### [OWLS: Open-world Language-conditioned Speed Fields for Zero-Shot Rover Navigation](https://arxiv.org/abs/2610.32596)
🏷️ 交叉方向 / Also: 空间智能 / Spatial
开源状态 / Code: ❓ 未知 / Unknown — Comments 为 "8 pages. 6 figures",无代码链接
- 🇨🇳 问题:语义可作为物理可通行性的代理,但需要开放词汇的地形推理。方法:OWLS 直接在 VLM 稠密特征图上规划——用可通行地形描述提示 VLM 为单张相机图像每个像素打分,投影到地面并用两个形态学操作适配平台,作为最短时间规划器的速度场;无需任务训练、地形标注、持久地图或相机以外的外部传感器。结果:在室内外真实漫游车、200 个程序生成地形上的模拟火星/月球车以及真实行星影像上评估;预印本摘要未给出定量结果。
- 🇬🇧 Problem: semantics can proxy physical traversability but needs open-vocabulary terrain reasoning. Method: OWLS plans over a VLM's dense feature map — a prompt describing traversable terrain scores every pixel, scores are projected to the ground and adapted with two morphological operations to form the speed field of a minimum-time planner; no task training, annotation, persistent map or extra sensors. Results: evaluated on a physical rover indoors/off-road, simulated Mars and Moon rovers over 200 generated terrains, and real planetary imagery; the abstract gives no quantitative results.

### [Natural-Language to Nav2: Operational Policies for Costmap-Based Navigation](https://arxiv.org/abs/2610.32633)
开源状态 / Code: ❓ 未知 / Unknown — 摘要给出项目页 [项目页](https://a56239637-dot.github.io/Natural-Language-to-Nav2-Project-Page/),未核对是否含代码链接
- 🇨🇳 问题:仓库等场景的导航需遵守传感器看不到的临时通行规则、路线偏好和例外。方法:本地 LLM 把自然语言指令转为 JSON 策略(目的地、空间约束、时间/事件条件),确定性检查把关任务接受,三个代价地图适配器在不改动规划器与控制器的前提下将策略投影到 ROS 2 Nav2。结果:150 条英文指令上,四个本地模型产生 107–142 条正确接受的策略(规则解析器为 44),错误接受 3–20 条;故障注入拒绝了 8 个端点/JSON 故障和 29 个验证器阶段故障;任务 1–3 的平均行驶时间仿真中降低 18.4%–24.5%,TurtleBot3 实机降低 23.1%–35.0%。
- 🇬🇧 Problem: warehouse navigation must follow temporary access rules and exceptions that sensors cannot see. Method: a local LLM converts instructions into JSON policies (destinations, spatial constraints, temporal/event conditions), deterministic checks gate acceptance, and three costmap adapters project policies into ROS 2 Nav2 without changing planner or controller. Results: on 150 commands, four local models give 107–142 correctly accepted policies versus 44 for a rule-based parser (3–20 incorrect acceptances); fault injection rejects 8 endpoint/JSON and 29 validator-stage faults; mean travel time falls 18.4–24.5% in simulation and 23.1–35.0% on a TurtleBot3.

本类共 5 条相关,全部已展开。 / 5 relevant, all expanded.

---

## 世界模型与 WAM / World Models & WAM

### [UniAction: Unified Action Conditioning for World Models](https://arxiv.org/abs/2610.32977)
开源状态 / Code: ✅ 已开源 / Released — [KBRASK/UniAction](https://github.com/KBRASK/UniAction);项目页 [UniAction](https://uniaction.github.io/) 链接该仓库,匿名 `git ls-remote` 可访问(账号名与作者无直接对应,以项目页链接为准)
- 🇨🇳 问题:动作条件世界模型通常为单一动作类型构建,使有限的带动作标注数据被分散在不同模型中。方法:UniAction 把任意动作表示为稀疏动作元素集合,每个元素有离散语义身份和连续时空落地坐标,并将坐标映射到预训练视频模型的原生位置空间,使异构动作条件化同一个共享世界模型;还提出基数校准注意力以消除表示粒度差异带来的偏置。结果:在力、相机控制、手部姿态和机器人姿态四种动作形式上,动作跟随优于其他条件化方案,单个联合训练模型超过各动作专用专家模型(摘要未给出具体数值)。
- 🇬🇧 Problem: action-conditioned world models are built per action type, fragmenting scarce action-annotated data. Method: UniAction represents any action as a sparse set of elements with a discrete semantic identity and a continuous spatiotemporal coordinate mapped into the pretrained video model's positional space, plus cardinality-calibrated attention to correct granularity bias. Results: on force, camera control, hand pose and robot pose, it beats other conditioning schemes in action following, and one jointly trained model surpasses action-specific experts (no numbers in the abstract).

### [Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection](https://arxiv.org/abs/2610.32742)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接
- 🇨🇳 问题:关键基础设施中的异常若未被识别可能引发级联故障,而传统检测依赖电机编码器等内部传感器,老旧设备常无此类传感器或禁止访问。方法:AWARE 世界模型框架仅用外部相机,通过系统动力学估计与状态预测进行异常检测。结果:在 240 条真实机器人起重机轨迹(含载荷碰撞与电机退化)上,噪声相机状态估计下的异常分类比最强基线提升 26%;推断的动力学参数可解码出故障源,定位退化电机的准确率为 88%。
- 🇬🇧 Problem: unrecognized anomalies in critical infrastructure can cascade, and detectors relying on onboard sensors fail on legacy or access-restricted hardware. Method: AWARE, a world-model framework detecting anomalies from external cameras only via dynamics estimation and state prediction. Results: on 240 real robotic crane trajectories (payload collisions, motor degradation) it improves anomaly classification by 26% over the strongest baseline under noisy camera-only estimation, and the inferred dynamics parameter localizes the degrading motor with 88% accuracy.

### [Does LeWorldModel Preserve Local Action Geometry?](https://arxiv.org/abs/2610.31716)
开源状态 / Code: ❓ 未知 / Unknown — Comments:NeurIPS 2026 NeurReps 研讨会扩展摘要,无代码链接
- 🇨🇳 内容:用匹配的模拟器与模型响应,通过三个扰动尺度的 Gram 矩阵,度量预训练 LeWorldModel(LeWM)对小动作变化效应的复现程度。结论:在 Reacher 与 OGBench Cube 近千个状态上,最小尺度时最敏感动作方向的中位夹角约 36° 与 42°;扰动放大十倍后中位归一化 Gram 差异分别降低约 70% 和 47%;留出方向上环境 Gram 的嵌入响应误差中位数为 17%/28%,低于同迹各向同性参考的 26%/38%,即 LeWM 在此尺度误差更高;支持按尺度评估动作敏感性,对控制的影响仍是开放问题。
- 🇬🇧 Content: measures how closely pretrained LeWorldModel reproduces effects of small action changes via Gram matrices at three perturbation scales against matched simulator responses. Conclusion: over ~1,000 states on Reacher and OGBench Cube the most sensitive action directions differ by median angles of ~36° and ~42° at the smallest scale; a tenfold larger perturbation lowers median normalized Gram discrepancy by ~70% and ~47%; held-out embedding response errors are 17%/28% for environment Grams versus 26%/38% for an isotropic reference, so LeWM errs more at this scale; effect on control remains open.

### [DT-JEPA: Learning to Predict Future Representations for Decision-Making](https://arxiv.org/abs/2610.32657)
🏷️ 交叉方向 / Also: 运动控制·RL(离线 RL 决策;未涉及具体机器人运动控制任务,故留在本类)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,无代码链接
- 🇨🇳 问题:Decision Transformer 以期望回报为条件对未来描述不完整,且依赖任务特定奖励,限制向相似但未见奖励任务的扩展。方法:受 JEPA 启发提出 DT-JEPA,从无奖励离线轨迹预训练、在线微调,用概率预测器建模潜空间中未来表征的条件分布,同时捕获预测信息与不确定性;理论上证明 JEPA 目标最大化历史表征与未来轨迹互信息的变分下界,且未来条件策略学习有带 O(N^-1/4) 估计项的有限样本性能界。结果:在 D4RL 基准上能高效适应不同离线 RL 任务,优于传统 DT 类及其他离线 RL 方法(摘要未给出具体数值)。
- 🇬🇧 Problem: Decision Transformer conditions on expected return, an incomplete and reward-dependent description of the future, limiting transfer to similar tasks with unseen rewards. Method: DT-JEPA pretrains offline on reward-free trajectories and fine-tunes online, with a probabilistic predictor of the conditional distribution of future latent representations capturing both information and uncertainty; theory shows the JEPA objective maximizes a variational lower bound on mutual information between historical representations and future trajectories, and future-conditioned policy learning has a finite-sample bound with an O(N^-1/4) estimation term. Results: on D4RL it adapts efficiently across offline RL tasks and outperforms DT-based and other offline RL methods (no numbers in the abstract).

另见 / See also: [HGWM](https://arxiv.org/abs/2610.32554)(已归入 VLN)、[RepresentNav](https://arxiv.org/abs/2610.31762)(已归入 VLN)、[RynnUnify](https://arxiv.org/abs/2610.32965)(已归入 具身智能与机器人基础模型)、[Sensorimotor Alignment](https://arxiv.org/abs/2610.31670)(已归入 具身智能)、[ViT-H](https://arxiv.org/abs/2610.32966)(已归入 运动控制·RL)、[WAM-TTT](https://arxiv.org/abs/2607.06988)(旧论文的更新版本,摘要显示为测试时用人类视频调整世界-动作模型,未再展开)。本类共 4 条,全部已展开。 / 4 relevant, all expanded.

---

## 空间智能与 SLAM / Spatial Intelligence & SLAM

### [PnP*: A certifiable solver for Perspective-n-Point](https://arxiv.org/abs/2610.31797)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为 "28 pages, 3 figures",无代码链接
- 🇨🇳 问题:由 3D-2D 对应估计相机位姿(PnP)是基础问题,现有方法要么解最小问题、要么替换为更易的目标,尚无可扩展且可认证的真实最大似然估计(MLE)求解器。方法:提出 PnP*,证明其凸松弛在中等噪声下是精确的(PnP MLE 松弛的首个稳定性保证),并利用弦稀疏模式和商环约简使松弛可处理、可扩展。结果:数值上验证了稳定性与可扩展性,返回可证明正确的相机位姿,速度超过 10 Hz。
- 🇬🇧 Problem: PnP camera pose estimation lacks a scalable certifiable solver for the true maximum-likelihood objective. Method: PnP* proves the convex relaxation exact under moderate noise (the first stability guarantee for any relaxation of the PnP MLE) and exploits chordal sparsity and quotient-ring reduction to make it tractable and scalable. Results: numerically verified stability and scalability, returning a provably correct pose at over 10 Hz.

### [StackGen3D: Stable 3D Block Stack Generation from Multiview Silhouettes](https://arxiv.org/abs/2610.31803)
开源状态 / Code: ❓ 未知 / Unknown — Comments 给出 IROS 2026 研讨会海报与项目页 [StackGen3D](https://ripl.github.io/StackGen3D-web/),未核对是否含代码链接
- 🇨🇳 问题:由视觉规格生成物理稳定的 3D 结构需解决几何歧义并考虑物体间物理作用。方法:两阶段——先用物理信息图神经网络(PI-GNN)建模块间支撑关系,作为快速稳定性预测器整理多样稳定结构数据集;再训练条件流匹配模型捕获与三个正交轮廓一致的多模态块配置,推理时用轻量几何选择与精修减少块间穿透。结果:初步实验显示 PI-GNN 从简单堆叠泛化到复杂结构明显优于参数量匹配的 MLP;Best-of-10 选择使物理稳定性由 45.3% 提高到 72.4%,轮廓 IoU 0.970。
- 🇬🇧 Problem: generating physically stable 3D structures from visual specs needs resolving geometric ambiguity and object interactions. Method: a physics-informed GNN predicts stability to curate a dataset, then a conditional flow-matching model captures multimodal block configurations matching three orthographic silhouettes, with lightweight geometric selection/refinement reducing penetration. Results: PI-GNN generalizes from simple to complex stacks better than a parameter-matched MLP; Best-of-10 raises stability from 45.3% to 72.4% with silhouette IoU 0.970 (preliminary experiments).

另见 / See also: [WorldMirror](https://arxiv.org/abs/2610.31834)、[SceneBloom](https://arxiv.org/abs/2610.32978)(均已归入 具身智能与机器人基础模型)。未展开的更新版本 / Replacement, not expanded: [Rethinking Densification in Gaussian SLAM](https://arxiv.org/abs/2601.00705)。本类共 2 条新论文(+1 更新),新论文全部已展开。 / 2 new papers expanded.

---

## 其他值得关注 / Other Notable

本期 cs.RO 中其余约 19 条新增/交叉条目(无人机集群、月球集群热调节、车道保持、GNSS/IMU、接触镜测量、超声/OCT 医疗机器人、分子/自组装等)与关注主题无关,未纳入;未发现需单列的其他重点条目。 / The remaining ~19 New/Cross entries (swarms, lane keeping, GNSS/IMU, medical robotics, etc.) are off-topic; nothing else notable.

---

## GitHub 动态 / GitHub Highlights

**Star 增长(相对 2026-10-25 23:18 UTC 快照;仅列相关项)/ Star growth (relevant only)**

| 仓库 / Repo | Stars | Δ | 说明 / Note |
|---|---|---|---|
| [mujoco](https://github.com/google-deepmind/mujoco) | 15909 | +33 | 物理仿真器 / physics simulator |
| [Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide) | 16691 | +33 | 具身智能技术指南(Lumina 社区)/ embodied AI guide |
| [Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) | 157 | +29 | SuperMimic 的独立复现(非官方)/ independent reproduction, unofficial |
| [lerobot](https://github.com/huggingface/lerobot) | 28490 | +26 | 端到端机器人学习 / end-to-end robot learning |
| [openlambda](https://github.com/LambdaHumanoid/openlambda) | 52 | +22 | λ_0:为人形 loco-manipulation 扩展开放世界第一视角人类数据 / egocentric human data for humanoid loco-manipulation |
| [openpi](https://github.com/Physical-Intelligence/openpi) | 14412 | +22 | π 系列 VLA / π-series VLAs |
| [Isaac Lab](https://github.com/isaac-sim/IsaacLab) | 8482 | +14 | 机器人学习框架 / robot learning framework |
| [spirula-studio](https://github.com/harry7557558/spirula-studio) | 1927 | +46 | 跨厂商 3D Gaussian Splatting 训练器 / cross-vendor 3DGS trainer |

(radar 前列的 gods-eye-view、text-to-cad、RuView 等与本关注主题关联较弱,未列入;RuView 描述为 WiFi 空间感知。)

**新仓库(筛选后)/ Notable new repos:** [alibaba-damo-academy/RynnUnify](https://github.com/alibaba-damo-academy/RynnUnify)(18★,对应论文 RynnUnify,见具身智能类);SuperMimic 第三方复现仍在增长,如 [Dex-Supermimic](https://github.com/CumulusAlpha/Dex-Supermimic)(26★,灵巧手复现)、[SuperMimic-Repro-Sim2Real](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real)(8★,Unitree G1 非官方复现)、[awesome-supermimic](https://github.com/DiaoOrg/awesome-supermimic)(144★,资源汇总);[RePIC](https://github.com/H-EmbodVis/RePIC)(2★,跨重规划复用去噪轨迹、免训练加速,描述标称 2.66–2.75 倍)。

**新 Release / New releases:** radar `watchlist_releases` 为 0:LeRobot、openpi、Isaac Lab、MuJoCo、GR00T、Genesis、ManiSkill、ORB-SLAM3、VGGT 等在 48 小时窗口内无新 release。 / None in the window.

---

## 今日趋势 / Today's Trends

1. **人形控制的「可部署性」细节成为焦点 / Deployment realism for humanoids.** 🇨🇳 [Delay Randomization](https://arxiv.org/abs/2610.32277) 量化了延迟裕度,[Regularised RL](https://arxiv.org/abs/2610.32855) 与 [RobustRLlib](https://arxiv.org/abs/2610.32971) 强调鲁棒性与评测基准,[Not an Accident](https://arxiv.org/abs/2610.31923) 指出安全滤波器参数配置的脆弱性。 🇬🇧 Delay margin, robustness regularisation, a robust-RL benchmark and safety-filter attacks all target the gap between simulation and real humanoids.
2. **复用冻结控制器 + 上层学习 / Reuse a frozen controller.** 🇨🇳 [HoloBoxing](https://arxiv.org/abs/2610.32909) 在冻结全身控制器上用约 7 分钟学会新任务,[ViT-H](https://arxiv.org/abs/2610.32966) 把视频生成与跟踪器反馈闭环。 🇬🇧 HoloBoxing and ViT-H both treat a pretrained tracker as a fixed substrate and learn upper-level behavior or references on top.
3. **机器人数据引擎与奖励/进度模型 / Data engines and reward models.** 🇨🇳 [FLORA](https://arxiv.org/abs/2610.31779) 与 [NimCritic](https://arxiv.org/abs/2610.32776) 都在为机器人数据提供字幕与过程奖励,[DiscoDemo](https://arxiv.org/abs/2610.32093) 则用 RL 生成多样示教。 🇬🇧 FLORA and NimCritic provide captions and process rewards at scale; DiscoDemo uses RL as a demonstration generator.
4. **VLA 的可靠性与部署调优 / VLA reliability.** 🇨🇳 bf16 微调静默抹去更新([paper](https://arxiv.org/abs/2610.31859))、失败预测与回溯([Backtrack](https://arxiv.org/abs/2610.32941))、执行视野与采样深度耦合([paper](https://arxiv.org/abs/2610.32102))均属免训练或工程层面的改进。 🇬🇧 Precision bugs, failure prediction/recovery and a free deployment knob dominate VLA work today.
5. **统一具身模型走向世界-动作 / Unified embodied models.** 🇨🇳 [RynnUnify](https://arxiv.org/abs/2610.32965) 与 [RepresentNav](https://arxiv.org/abs/2610.31762) 都把潜在预测(世界模型式)嵌入决策。 🇬🇧 Both embed latent future prediction inside decision-making.

---

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
- `process reward model robot` / `robot reward model` / `progress critic`(arXiv 检索 + GitHub 关键词 / both)— 🇨🇳 奖励/进度标注正成为机器人数据引擎的独立模块。 🇬🇧 Reward and progress labelling is becoming its own robotics component. 证据 / Evidence: 2 篇 — [FLORA](https://arxiv.org/abs/2610.31779)、[NimCritic](https://arxiv.org/abs/2610.32776)。
- `delay margin` / `latency robustness`(arXiv)— 🇨🇳 sim-to-real 失效的具体机制值得单独追踪。 🇬🇧 A concrete sim-to-real failure mechanism worth tracking. 证据:1 篇 — [Delay Randomization](https://arxiv.org/abs/2610.32277);信号偏弱。

**建议观察 / Watch**
- `generation-and-tracking`(视频 → 人形参考动作 + 跟踪反馈,arXiv)— 🇨🇳 仅 [ViT-H](https://arxiv.org/abs/2610.32966) 一篇,再观察几天。 🇬🇧 One paper so far ([ViT-H](https://arxiv.org/abs/2610.32966)); watch a few more days.
- `SuperMimic`(GitHub 搜索)— 🇨🇳 第三方复现数量持续增加,但已由监测列表覆盖,不必加入关键词。 🇬🇧 Reproductions keep appearing but the watchlist already covers it.

**建议移除/收窄 / Remove or Narrow:** 今日无建议 / None.

---

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 | 当前状态 | 今日检查 | 备注 |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 | radar `signal=true`,但唯一候选为 [qiayuanl/claude-meter](https://github.com/qiayuanl/claude-meter)(owner_recent 来源,描述为 macOS 菜单栏 Claude Code 用量应用,与 SuperMimic 无关),判定为**误报**;project_page_github_links / release_claims / arxiv_github_links 均空,arXiv 最新版 v1,errors 空;预设 known_repos 匿名 `git ls-remote` 均不可访问;[项目页](https://supermimic.github.io)无代码链接 | 状态不变。多个第三方复现(如 [Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) 157★、[Dex-Supermimic](https://github.com/CumulusAlpha/Dex-Supermimic) 26★、[go2-supermimic](https://github.com/Zhengtianjin/go2-supermimic) 50★),均非官方,不据此判定已开源 |

**建议加入监测 / Suggested additions**
- **HoloBoxing** — 🇨🇳 运动控制·RL,人形拳击的 7 分钟训练配方,尚无代码链接。 🇬🇧 Motion-control RL recipe for humanoid boxing; no code link yet.
```json
{"name": "HoloBoxing", "title": "HoloBoxing: A Simple Recipe for Humanoid Boxing with 7 Minutes of Single-GPU Training", "arxiv_id": "2610.32909", "search_terms": ["HoloBoxing"], "owners": [], "project_pages": [], "known_repos": []}
```
- **SEVI** — 🇨🇳 真机强化学习的安全框架,项目页已承诺 "Code · coming soon"。 🇬🇧 Safe real-world RL; project page promises code ("coming soon").
```json
{"name": "SEVI", "title": "SEVI: Safe Evidential Real-World Reinforcement Learning", "arxiv_id": "2610.31829", "search_terms": ["SEVI"], "owners": [], "project_pages": ["https://sevi-safe.github.io/"], "known_repos": []}
```
- **CoCarry** — 🇨🇳 双人形协作搬运的数据集与重定向,真机验证,代码未提及。 🇬🇧 Dual-humanoid carrying dataset and retargeting with real-robot validation; no code mentioned.
```json
{"name": "CoCarry", "title": "CoCarry: Contact-Support-Structured Retargeting for Dual-Humanoid Cooperative Carrying", "arxiv_id": "2610.32460", "search_terms": ["CoCarry"], "owners": [], "project_pages": [], "known_repos": []}
```

**建议移出 / Suggested removals:** 无 / None(SuperMimic 仍未开源)。

---
*自检 / Self-check:* ① 类别 1–2 条目均已完整展开(RL 14 条 + 传统 4 条,另列 4 条更新版本仅列名);② 无"未读/仅标题"占位,所有入选摘要均已完整读取;③ 每条均有开源状态行;④ 优先级 3–7 类别已自查,FORCA 移入传统控制,CoCarry/DiscoDemo/Tabletop-to-Walking 归入 RL,其余条目不涉及运动控制;⑤ 已运行 arXiv API 检索并记录命中数;⑥ 本期无 release;⑦ 已按链接格式规范用脚本扫描。
