# 机器人/具身智能每日速递 — 2026-11-06 / Robotics & Embodied AI Daily — 2026-11-06

> 本日监测项 SuperMimic 仍未发现官方开源(signal=false),故无「🔔 监测项已开源」区块。 / No watchlist item released today (SuperMimic: signal=false).

## 检查窗口与来源状态 / Window & Source Status

- **窗口 / Window**:台北时间 2026-11-05 ~ 11-06 07:40(arXiv 周四列表,覆盖 UTC 11-03 18:00 ~ 11-04 18:00 提交)。 / Taipei time; arXiv Thursday listing.
- **arXiv cs.RO new 列表 / list**:New 53 + Cross-lists 9 + Replacements 40 = 102 条,全部逐条分类;102/102 条通过 API id_list 取得非空摘要与 Comments。
- **arXiv API 关键词检索 / keyword searches**(cs.RO/AI/LG/CV,按 submittedDate 降序,每词取前 40):embodied 40、vision-language-action 40、VLA 40、vision-language navigation 40、humanoid 40、legged locomotion 40(最新 10-28,窗口内 0)、whole-body control 40、model predictive control robot 1、reinforcement learning robot 12(陈旧)、sim-to-real 40、dexterous manipulation 40、robot foundation model 40、world model 40、world action model 40、video world model 40、spatial intelligence 40、spatial reasoning 40、SLAM 40、visual SLAM 40、LiDAR SLAM 40、gaussian splatting SLAM 40、3D reconstruction 40、motion tracking 40、motion imitation 40。窗口内且不在 cs.RO 列表中的新增唯一论文 25 篇,其中与关注主题相关并入选 7 篇。
- **入选 / Selected**:本报告详细展开 53 篇,均已取得完整摘要(0 篇获取失败)。
- **GitHub radar**:`data/latest.json` date_taipei = 2026-11-06(已更新);new_repos 150 条、star_growth_top 60 条、watchlist_releases 2 条、oss_watch 1 项。star 基准为前一日,有效。
- **Hugging Face Daily Papers**:API 返回 100 条,与机器人相关且带 githubRepo 的见「其他值得关注」。
- 推送权限检查:`git push --dry-run` 通过。

## 今日必读 / Top Picks

1. **[Ctrl-F](https://arxiv.org/abs/2611.05507)** — 运动控制·RL ❓。把「力」作为人形动作跟踪与物体交互之间的命令接口,真机可推/踢 20kg 箱子。 / Force as a command channel for humanoid motion tracking; real-robot pushing/kicking 20 kg boxes where force-blind trackers fail.
2. **[Playing Soccer Like Humans Do (soccerbot)](https://arxiv.org/abs/2611.06564)** — 运动控制·RL ❓。人类足球动捕蒸馏的潜在运动先验 + 分层 RL,零样本迁移到 Unitree G1。 / Latent-motion-prior hierarchical RL, zero-shot to Unitree G1.
3. **[Perceptive Humanoid Motion from Simulation (HALO)](https://arxiv.org/abs/2611.06908)** — 运动控制·RL ✅。完全仿真合成视觉-语言-动作数据,真机零样本 360 次试验成功率 91%,代码已发布。 / Fully simulated vision-language-motion data; 91% zero-shot real-world success over 360 trials; code released.
4. **[GRASP](https://arxiv.org/abs/2611.05754)** — 运动控制·RL ❓。无需可微仿真器的接触丰富动作重定向,1352 条 OakInk2 双手演示成功率 92.8%。 / Contact-rich retargeting without a differentiable simulator; 92.8% on 1352 OakInk2 demos.
5. **[Open-HumanScale](https://arxiv.org/abs/2611.06817)** — 具身基础模型 ✅。5 万小时第一视角人类视频预训练的 World-Action Model,数据/代码/权重全部开源。 / 50k-hour egocentric pretraining of a world-action model; data, code and checkpoints all open.

---

## 运动控制·RL / Motion Control · RL(全部展开 / all expanded)

### [Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.05507)
🏷️ 交叉方向 / Also: 动作模仿与跟踪(同属本类)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅给出[项目页](https://forcectrl.github.io/),未见代码仓库
- 🇨🇳 现有人形运动跟踪策略只知道「身体应在哪」,不知道「与环境交互要多大力」,难以完成重载搬运类 loco-manipulation。Ctrl-F 提出分层的运动-力框架:统一的运动-力控制器在跟踪参考动作的同时,对指定接触体(手、脚)施加三维力命令;上层力规划器根据物体状态与本体感知在线下发力命令。仿真与真机上都完成了需要大而持续作用力的任务,真机包括手部拖/推/举与脚部踢,可操作最重 20kg 的箱子,且能在任务中途加载时在线调整,而不感知力的基线失败。
- 🇬🇧 Motion trackers for humanoids know where the body should be but not how hard to interact. Ctrl-F augments tracking with an explicit 3-D force command per contact body (hand/foot), via a unified motion-force controller plus a high-level force planner that issues commands online from object state and proprioception. In simulation and on hardware it completes loco-manipulation needing large, sustained forces—dragging, pushing, lifting, kicking boxes up to 20 kg—and adapts online to loads added mid-task, where a force-blind tracker fails.

### [Playing Soccer Like Humans Do: Learning Versatile and Agile Humanoid Soccer via Latent Motion Priors](https://arxiv.org/abs/2611.06564)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接
- 🇨🇳 人形足球需同时具备敏捷移动、触球操控与高冲击接触,现有方法要么技能有限,要么没有运动先验而动作不自然。soccerbot 是分层 RL 框架,从大规模人类足球动捕数据蒸馏出结构化的潜在运动先验,把策略学习约束在动力学可行的运动流形内,单个技能条件策略即可统一完成移动、运球、停球与踢球,并实现流畅切换。结合面向鲁棒性的仿真设计,零样本迁移到 Unitree G1,真机展示了完整足球技能库;摘要未给出定量指标。
- 🇬🇧 Humanoid soccer demands agile locomotion, ball manipulation and impact-rich contact, yet prior work covers few skills or yields unnatural motion. soccerbot is a hierarchical RL framework with a latent motion prior distilled from large-scale human soccer mocap, constraining learning to a dynamically plausible manifold so one skill-conditioned policy performs moving, dribbling, trapping and kicking with human-like transitions. With robustness-oriented simulation design it transfers zero-shot to Unitree G1 and executes the full skill set; the abstract reports no quantitative numbers.

### [Perceptive Humanoid Motion from Simulation (HALO)](https://arxiv.org/abs/2611.06908) — Apple
🏷️ 交叉方向 / Also: 具身基础模型(视觉-语言-动作数据)、VLN(导航到命名物体)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/apple-aiml-research/ml-halo);Comments 指向[项目页](https://apple-aiml-research.github.io/ml-halo/)提供代码与视频,仓库匿名 `git ls-remote` 可访问,具体开源内容(训练/推理/数据)未逐项核对
- 🇨🇳 人形自主的瓶颈是缺少「像素/语言 → 关节指令」的大规模配对数据,遥操作与穿戴采集需要与数据时长相当的人力。HALO 在一千个程序化生成的家庭场景中合成视觉-语言-运动数据,数据规模随算力而非人力增长,习得坐椅子、导航到指定物体、侧身过半开门、蹲/爬桌下、推箱子等技能并串联完成长时程任务。训练中从未见过真实住宅,零样本迁移到真实世界,在六个未建图环境的 360 次试验中成功率 91%。
- 🇬🇧 Humanoid autonomy is bottlenecked by paired pixel/language-to-joint-command data that teleoperation cannot scale. HALO synthesizes vision-language-motion data across a thousand procedurally generated homes (scaling with compute, not labor), learning sitting, navigating to named objects, side-stepping through half-open doors, crouching/crawling under tables and pushing boxes, and composing them into long-horizon tasks. Without ever seeing a real home in training, it transfers zero-shot with a 91% success rate over 360 trials in six unmapped real environments.

### [GRASP: Gradient-Guided Sampling for Contact-Rich Physics-Based Motion Retargeting](https://arxiv.org/abs/2611.05754) — Harvard
🏷️ 交叉方向 / Also: 运动控制·传统(采样式 MPC/轨迹优化,同属运动控制);按「RL 参与」归入本类(提升 PPO 跟踪)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅给出[项目页](https://computationalrobotics.seas.harvard.edu/GRASP/)
- 🇨🇳 基于物理的人类示范重定向需要在接触动力学下找到能复现参考动作的机器人控制,但可微仿真器并不总是可用。GRASP 把采样探索与梯度引导精修结合:GRASP-TO 在回火序贯蒙特卡洛上用存档 rollout 拟合局部二次代价模型,以其梯度引导 MCMC 复苏并用 Metropolis-Hastings 修正;GRASP-MPC 用热启动滚动时域规划扩展到长示范。灵巧手与人形实验在共享跟踪目标且无任务特定接触奖励下准确重定向,1352 条双手 OakInk2 示范成功率 92.8%,精修后的参考提升了转笔与人形-物体交互的 PPO 跟踪,并有真机灵巧操作与人形全身动作演示。
- 🇬🇧 Physics-based retargeting must find robot controls reproducing reference motions under contact, without always having a differentiable simulator. GRASP-TO extends tempered sequential Monte Carlo by fitting local quadratic cost models to archived rollouts and using their gradients in MH-corrected MCMC rejuvenation; GRASP-MPC scales it to long demonstrations via warm-started receding-horizon planning. With a shared tracking objective and no task-specific contact rewards it reaches 92.8% success on 1352 bimanual OakInk2 demos, its refined references improve PPO tracking for pen spinning and humanoid-object interaction, and it is demonstrated on real dexterous and humanoid hardware.

### [H^2MARL: Hierarchical Heterogeneous Multi-agent Reinforcement Learning for Humanoid Robot Control](https://arxiv.org/abs/2611.06523)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 人形全身控制的关节自由度(JDoF)高维耦合且物理异质,现有多智能体 RL 要么粗粒度划分,要么直接套用通用异质算法,分层控制器又常独立优化高低层而导致动作不协调。H^2MARL 提出 JDoF 级、感知物理异质性的策略分解(每个力矩驱动关节以执行器/运动学/动力学描述符为条件),并用共享交互轨迹闭环联合优化高层姿态规划器与低层关节执行器以减小规划-执行分布失配。MuJoCo 与 Isaac Gym 实验表明其在步态稳定性、协调性和动作质量上稳定优于同构、粗粒度及独立优化基线;摘要未给出具体数值,也未见真机。
- 🇬🇧 Humanoid whole-body control suffers from coupled high-dimensional dynamics and joint heterogeneity; prior MARL uses coarse partitions or generic algorithms, and hierarchical controllers optimize levels independently. H^2MARL factorizes the policy at joint-DoF level conditioned on actuation/kinematic/dynamic descriptors, and co-optimizes the high-level pose planner and low-level joint executor on shared trajectories to reduce planning-execution mismatch. In MuJoCo and Isaac Gym it improves locomotion stability, gait coordination and motion quality over homogeneous, coarse and independently optimized baselines; no numbers or hardware results are given in the abstract.

### [Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement](https://arxiv.org/abs/2611.06905) — ETH LAS Group(据仓库组织 / by repo owner)
🏷️ 交叉方向 / Also: 具身智能与机器人基础模型 / VLA(π0.5);因目标是用 RL 做操作策略改进,归入本类
开源状态 / Code: ✅ 部分开源 / Partial — [仓库](https://github.com/lasgroup/generalist-improvement);当前含 π0.5 在 LIBERO-90 与 MolmoSpaces 上的 FSFT、Best-of-N 多任务后训练,README 称 OGPO 实现「即将发布」
- 🇨🇳 通用机器人策略部署时仍需适应,但在线 RL 自我改进多在单任务设定下研究,与基础策略的多任务能力脱节。本文构建结构化评测,系统比较价值估计、策略提取与资源分配等设计选择,表明通用策略可跨多任务在线改进,且正确配方还能提升未参与在线训练任务的表现。结果显示训练任务分布与基于价值的 RL 是关键;预印本摘要未给出具体定量数字。
- 🇬🇧 Generalist robot policies need adaptation in deployment, yet online RL self-improvement has mostly been studied on single tasks. The authors build structured evaluations and compare design choices for value estimation, policy extraction and resource allocation, showing generalist policies can be improved online across many tasks and that the right recipe also boosts held-out tasks. The training task distribution and value-based RL are critical; the abstract gives no quantitative numbers.

### [TwinBridge: Digital Twin-Driven Policy and Reward Transfer for Real-World Reinforcement Learning in Laboratory Robotics](https://arxiv.org/abs/2611.06442)
🏷️ 交叉方向 / Also: 空间智能(3D Gaussian Splatting 数字孪生)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 实验室精密操作的在线 RL 受限于昂贵的真机示范与稠密过程奖励缺失。TwinBridge 用 3D Gaussian Splatting 结合物理仿真构建数字孪生,仿真状态给出任务事件与几何进度奖励,用于仿真示范预训练和 RL,并蒸馏为视觉奖励模型,真机交互时结合执行历史产生稠密奖励做人在回路精修。五个真实实验室任务上每任务至多 25 分钟真机交互即达到平均 98% 自主成功率,稠密奖励优于稀疏奖励,仿真初始化进一步加速学习。
- 🇬🇧 Online RL for precise lab manipulation is hampered by costly demonstrations and missing dense rewards. TwinBridge builds digital twins from 3D Gaussian splatting plus physics simulation, derives event/geometric-progress rewards for pretraining and RL, distills them into a visual reward model, and uses it with execution history for dense-reward human-in-the-loop refinement. On five real lab tasks it reaches a 98% mean autonomous success rate with at most 25 minutes of real interaction per task; dense rewards beat sparse ones and sim initialization speeds learning.

### [Compounding Physical RSI: Turning Execution Failure into Inherited Capability](https://arxiv.org/abs/2611.06654)
🏷️ 交叉方向 / Also: 具身基础模型(RoboDojo)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 通用操作策略在静态离线数据上训练,下游阶段的弱点要等通过前序阶段才暴露,且真机反馈难以定位失败阶段、失败轨迹不提供纠正动作、更新共享参数会损伤已掌握技能。该文提出自进化框架:先自动定位失败阶段并形成改进目标,再用经验证的阶段相关经验做行为正则化离线 RL 精修,最后在参考策略与精修策略间构造权重空间候选并跨任务评估后择优传承。在 RoboDojo-Sim 全部 42 个任务上,三种子平均总分 26.15、成功率 20.70%,排名榜首,领先次优提交 5.92 分和 5.82 个百分点。
- 🇬🇧 Generalist policies trained offline hide downstream weaknesses behind earlier stages, and physical feedback rarely localizes failures, supplies corrections or protects old skills. The framework traces failed rollouts to the breaking stage, refines the policy with behavior-regularized offline RL on curated stage-relevant experience, and picks the best weight-space interpolation between reference and refined policy as the next generation. On all 42 RoboDojo-Sim tasks it ranks first (three-seed mean Overall Score 26.15, success 20.70%), beating the runner-up by 5.92 points and 5.82 percentage points.

### [Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation](https://arxiv.org/abs/2611.05979)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅给出 AAAI 论文页(AAAI 2026 Oral)
- 🇨🇳 多指灵巧手操作维度高、动力学复杂,且 RL 依赖任务特定奖励工程。该方法利用 HOI 数据集学习整体预测未来手-物状态,预测的物体未来状态可作为通用奖励项用于 RL,减少奖励工程并提升泛化。三个操作任务的仿真与真机实验中,成功率与对新物体的泛化均优于现有 SOTA,并成功部署到不同机器人手上验证跨本体兼容;摘要未给出具体数值。
- 🇬🇧 Dexterous multi-finger manipulation is high-dimensional and RL needs hand-engineered rewards. The method learns to holistically predict future hand-object states from HOI datasets, and the predicted future object states serve as a general-purpose RL reward. On three tasks in simulation and the real world it beats SOTA methods in success rate and novel-object generalization and transfers across robot hands; no numbers are given in the abstract.

### [Asymmetric On-Policy Distillation Learns In-Context Exploration (ASTEROID)](https://arxiv.org/abs/2610.30105) — 替换版 / replacement
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 部分可观测下,纯在线 RL 学探索样本效率低,离线模仿又会对隐藏状态平均化。ASTEROID 让带历史的学生先在线采集上下文,再模仿以该上下文为条件的特权专家动作,从而学到先搜索、揭示隐藏状态后利用的测试时探索。在 11 个环境(含机器人操作、导航、Procgen)中固定探索预算下回报约 2 倍、交互量比 RL 基线少约 100 倍,并将仿真训练策略迁移到无视觉的真机操作,成功率比标准蒸馏高 40 个百分点。
- 🇬🇧 Learning exploration under partial observability by online RL is sample-inefficient while offline imitation averages over hidden states. ASTEROID has a history-conditioned student collect on-policy context and imitate a privileged expert conditioned on it, learning search-then-exploit behavior. Across eleven environments (incl. manipulation and navigation) it achieves ~2x return at fixed budgets with ~100x fewer interactions than RL, and transfers sim-trained policies to vision-denied real manipulation with +40% success over standard distillation.

### [AcroRL: Learning Aggressive Quadrotor Inversion using Bidirectional Thrust](https://arxiv.org/abs/2605.24301) — 替换版 / replacement(CoRL 2026 接收)
开源状态 / Code: ❓ 未知 / Unknown — 摘要称「提供开源实现」,但摘要/Comments 无链接,待核实
- 🇨🇳 双向推力四旋翼可倒飞,但几何控制在电机反转延迟与执行器饱和下需要启发式调度。AcroRL 用 RL 分别训练「正常→倒飞」「倒飞→正常」转换策略,调制一条恒定参考轨迹,与传统轨迹生成/跟踪兼容。JAX 仿真中相对最强的基于优化的基线,位置 RMSE 降 32%、稳定时间降 57%;真机倒飞位置 RMSE 低于 0.35m,并能在两种飞行模式下完成圆周飞行。
- 🇬🇧 Bidirectional-thrust quadrotors can fly inverted, but geometric control struggles with saturation and motor-reversal delay. AcroRL trains separate RL policies for nominal→inverted and inverted→nominal transitions that modulate a constant reference trajectory, staying compatible with standard planners/trackers. In JAX simulation it cuts position RMSE by 32% and settling time by 57% versus the strongest optimization baseline; on hardware it inverts with position RMSE below 0.35 m and flies circles in both regimes.

### [PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting](https://arxiv.org/abs/2610.12642) — 替换版 / replacement
🏷️ 交叉方向 / Also: 运动控制·传统(优化式重定向)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 多角色/物体交互动作重定向常用加权多目标优化,权重难调且会牺牲关键特性。PriMoRetarget 用显式优先级层次替代相对权重,低优先级更新被约束以保持高优先级目标(如脚部落点、交互接触)。在四个数据集(单角色、角色-物体、角色-角色)上更好地保持任务相关交互,生成的参考轨迹比常用方法更易被可靠跟踪;摘要未给数值。
- 🇬🇧 Retargeting multi-character/object interactions via weighted multi-objective optimization needs tuning and can compromise key traits. PriMoRetarget replaces weights with an explicit priority hierarchy where lower-priority updates preserve higher-priority objectives such as foot placement and contacts. On four datasets it preserves task-relevant interactions better and yields references that are tracked more reliably than widely used retargeting; no numbers in the abstract.

### [FLAG: Flow Policy MaxEnt-RL by Latent Augmented Guidance](https://arxiv.org/abs/2605.30749) — 替换版 / replacement(NeurIPS 2026)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅有[项目页](https://flag-rl.github.io/)
- 🇨🇳 MaxEnt-RL 常把策略限制为高斯,而用重要性加权监督学习的生成式策略在高维动作空间会权重塌缩。FLAG 通过用流潜变量增广状态空间并优化可证明一致的代理 MaxEnt 目标,将采样区域局部化。在基于状态的高维控制基准上用有限重要性样本实现富有表达力的策略优化,并在表达式策略的 MaxEnt 在线 RL 方法中达到 SOTA。
- 🇬🇧 MaxEnt-RL often restricts policies to Gaussians, while generative policies trained with importance weighting suffer weight collapse in high-dimensional actions. FLAG augments the state space with a flow latent variable and optimizes a provably consistent proxy objective, localizing sampling. It scales expressive-policy optimization with limited importance samples and achieves SOTA among expressive-policy MaxEnt online RL on high-dimensional state-based control benchmarks.

### [Provably Safe, Yet Scalable Reinforcement Learning (PS2-RL)](https://arxiv.org/abs/2606.14536) — 替换版 / replacement
🏷️ 交叉方向 / Also: 运动控制·传统(控制不变集)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 安全 RL 要么只有软约束而无形式保证,要么依赖难以扩展的显式证书(控制不变集合成)。PS2-RL 用学习到的备份策略前向积分隐式生成在线控制不变集:第一阶段训练备份策略并最大化隐式不变集体积,第二阶段通过可微投影层端到端训练、严格保证安全,且不限制底层 RL 算法。理论上给出保证,并在状态维度至多 10 的机器人控制任务上评估,而先前可证明安全的方法在该区间难以工作;摘要无具体数值。
- 🇬🇧 Safe RL typically lacks formal guarantees or relies on explicit invariant-set certificates that scale poorly. PS2-RL uses a learned backup policy to forward-integrate dynamics and build an implicit control-invariant set online, then trains the task policy end-to-end through a differentiable projection layer enforcing the guarantees, compatible with any RL algorithm. It has theoretical guarantees and is evaluated on robotic control tasks up to 10 state dimensions where prior provably-safe methods struggle; no numbers in the abstract.

### [When Robots Outweigh Objects: How Inertia Mismatch Shapes Robot Policy Learning](https://arxiv.org/abs/2611.03501) — 替换版 / replacement
开源状态 / Code: ❓ 未知 / Unknown — 仅[项目页](https://younghyopark.me/inertia-mismatch/)
- 🇨🇳 重型机械臂操作轻物体存在惯量失配,不清楚是否给学习带来隐性代价。受控仿真变化机器人/物体质量发现:RL 在很宽的质量组合下成功,而行为克隆在轻机器人操作重物体时更可靠;重机器人需要更多示范才能达到同等性能。通过选择低惯量工作区或引导示范者走低惯量构型,所得示范更易被模仿。
- 🇬🇧 Heavy arms manipulating light objects create inertia mismatch of unknown learning cost. Controlled simulation varying robot/object masses shows RL succeeds across a broad range while behavior cloning is more reliable when the robot is lighter than the object, and heavier robots need more demonstrations. Choosing a lower-inertia workspace or steering demonstrators toward low-inertia configurations makes demonstrations more imitable.

### [Warp: Structured Output-Space Adaptation for Frozen Robot Policies](https://arxiv.org/abs/2606.31043) — 替换版 / replacement
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 部署后动力学/接触/感知变化会使冻结策略退化。Warp 是上下文条件的单调双射样条输出空间适配器,对冻结基础策略的动作样本做非线性重塑并保持逐维顺序。在四个带受控部署偏移的 ManiSkill 任务上,于匹配的进化策略适配器研究中恢复效果最强;PPO 下排序则依任务而异。真机 SO101 插销在受限交互的 RLPD/SAC 流程中与强随机残差基线成功率相当,中位成功周期时间缩短约 30%。
- 🇬🇧 Deployment shifts degrade frozen policies. Warp is a context-conditioned monotone bijective spline adapter reshaping action samples of a frozen policy while preserving per-dimension order. On four ManiSkill tasks with controlled shifts it gives the strongest recovery in a matched ES study (PPO ordering is task dependent); on physical SO101 peg insertion in an RLPD/SAC pipeline it matches a strong residual baseline while cutting median successful cycle time by ~30%.

### [Diversity-Aware Experience Replay via Statistical Leverage Scores](https://arxiv.org/abs/2611.05929)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 离策略 RL 在真机上回放缓冲区被常规转移占据,稀有事件很少被采样。该文用统计杠杆分数给每条转移打分(无需标签、奖励或价值网络),与均匀采样混合抽样;指出按方差选列会对 one-hot 动作失效,改用最大峰度列,并发现重要性权重修正会完全抵消该方法故弃之。对关系型稀有情形用相对目标的短轨迹窗口恢复信号;三关节臂绕障推物任务稀有任务成功率从 0.49 提升到 0.69(标注 oracle 上限 0.74)。
- 🇬🇧 Off-policy RL buffers on robots are dominated by routine transitions. The paper scores transitions by statistical leverage (no labels, rewards or value network) and mixes it with uniform sampling, selecting heavy-tailed (high-kurtosis) feature columns because variance ranking fails on one-hot actions, dropping importance correction (which would cancel the effect), and using goal-relative trajectory windows for relational rarity. On a three-joint arm pushing an object around an obstacle, rare-task success rises from 0.49 to 0.69 (labeled-oracle ceiling 0.74).

### GitHub 仓库 / Repos(运动控制·RL)
- **[leggedrobotics/terrain-grounded-imagination](https://github.com/leggedrobotics/terrain-grounded-imagination)**(ETH RSL,62★,+41):地形接地想象——仅靠学习到的世界模型训练 Unitree G1 人形在楼梯、缺口、踏石上行走;世界模型只学机器人对地面的响应,地形、奖励与感知由仿真器高度图通过廉价可微查找读取。 ✅ 已开源 / Released(代码仓库,配套论文未在今日窗口列表中)。 / Trains a G1 humanoid to traverse stairs, gaps and stepping stones purely through a terrain-conditioned world model; rewards/perception read from the heightmap via differentiable lookups. 🏷️ 世界模型(已按「控制任务优先」归入本类)。
- **[fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic)**(155★,+23):Unitree G1 全身动作跟踪,README 称单张 RTX 4090 约 2.9 分钟训练即在 40 条 LAFAN1 片段上达到归一化回报 0.82;与 SuperMimic/InstantTrack 同样通过可微世界模型想象 rollout 反传训练策略,基于 mjlab/MuJoCo Warp。 ✅ 已开源。 / Whole-body motion tracking for G1 trained in ~3 min on one RTX 4090 via backprop through a differentiable world model.
- 第三方 SuperMimic 相关(**非官方**,不触发监测信号):[miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic)(510★,+20,资源汇总)、[Quangvuisme/Acp_supermimic_vibed](https://github.com/Quangvuisme/Acp_supermimic_vibed)、[yusenthebot/macmimic](https://github.com/yusenthebot/macmimic)。
- 另见 / See also(来源:new_repos):[EGalahad/boltrt](https://github.com/EGalahad/boltrt)(4★,C++ 策略循环,MuJoCo/真机,ONNX,humanoid sim2real 部署)。

**条目总数 / Total**:论文 15 + 仓库 2(均展开)。 / 15 papers + 2 repos, all expanded.

---

## 运动控制·传统 / Motion Control · Classical(全部展开 / all expanded)

### [Contact-Implicit Whole-Body Trajectory Optimization for Dynamic Humanoid Locomotion on Parameterizable Uneven Terrain](https://arxiv.org/abs/2611.05585) — IIT(ErgoCub),IEEE RA-L 10(11) 2025
开源状态 / Code: ❓ 未知 / Unknown — 作者修订版,摘要/Comments 无代码链接
- 🇨🇳 在复杂地形上做动态人形动作需要无预设接触序列的全动力学规划。本文提出接触隐式全身优化,用光滑曲面近似地形几何并设计新的接触约束,把适用域从平坦水平面扩展到任意光滑曲面,以非线性规划在台阶、斜坡等地形上规划步态,并通过代价函数与初值嵌入高层需求。在非共面地形上于仿真与真机 ErgoCub 做了初步可行性验证;摘要未给出定量指标。
- 🇬🇧 Dynamic humanoid motion on uneven terrain needs full-dynamics planning without prescribed contact sequences. The letter proposes contact-implicit whole-body optimization with a smooth-surface terrain model and new contact constraints extending applicability from flat ground to arbitrary smooth surfaces, solved by nonlinear programming for steps, ramps and more, with high-level requirements in the cost and initial guess. Preliminary feasibility tests on non-coplanar terrain were run in simulation and on the real ErgoCub; no quantitative metrics are given.

### [ZipDrift: Generating Multimodal Short-Horizon MPC Costs with One-Step Drifting Models](https://arxiv.org/abs/2611.05793)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 短时域 MPC 快但短视;ZipMPC 学习代价修正去模仿长时域专家,而最优修正常为多模态,确定性回归会平均模式。ZipDrift 训练一步漂移生成器输出 MPC 代价修正,偏向低闭环代价、仅用候选修正的代价评估学习而不需对优化器求导,由评论器排序少量候选,再由基于模型的 MPC 保证动力学与约束。在运动学超车基准(53% 的情境为双峰,手工短时域 MPC 碰撞率 28.5%)中,八维分阶段修正下 600 个测试回合无碰撞,而理想化 ZipMPC 式回归器碰撞 4.0%(专家标签不一致时 16.0%)。仅为初步仿真研究。
- 🇬🇧 Short-horizon MPC is fast but myopic, and the optimal cost correction is often multimodal so regression averages modes. ZipDrift trains a one-step drifting generator over MPC cost corrections, tilted toward low closed-loop cost and learned from cost evaluations alone without differentiating through the optimizer, with a learned critic ranking candidates and MPC enforcing dynamics/constraints. On a kinematic overtaking benchmark (53% bimodal contexts; manual MPC crashes 28.5%), it is collision-free in all 600 test episodes versus 4.0% crashes (16.0% with inconsistent labels) for an idealized ZipMPC-style regressor; this is a preliminary simulation study.

### [SCRUB: Contact-Based Surface-Frame Estimation for Force-Motion Control with an Armless Quadruped](https://arxiv.org/abs/2611.06649)
🏷️ 交叉方向 / Also: 足式机器人(Unitree Go1)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 擦拭、打磨类任务需要表面法向来控制接触力,而在未建图表面上法向未知,且行走使现有估计器的「速度沿表面」假设失效。SCRUB 让无臂四足用机身工具沿近垂直表面滑动:预测控制器用卡尔曼滤波的法向估计压/滑工具,融合力线索(摩擦与运动相反时对任意摩擦系数在倾斜为零时线索为零)与速度线索(减去指令压入速率并按步态周期平均)。Go1 真机在标称速度与载荷下完成了所有墙面遍历与立柱环绕;去掉任一线索、去掉步态平均或使用固定法向,环绕均无法完成。
- 🇬🇧 Force control for wiping/sanding needs the surface normal, which is unknown on unmapped surfaces, and walking violates estimators' tool-velocity-along-surface assumption. SCRUB lets an armless quadruped slide a body-mounted tool along near-vertical surfaces, with a predictive controller using a Kalman-filter normal estimate from a force cue (zero at zero tilt for any friction coefficient) and a gait-averaged velocity cue after subtracting commanded press rate. On Unitree Go1 hardware it completed every wall traverse and column orbit; no orbit completed with either cue removed, without gait averaging, or with a fixed normal.

### [Beyond Terminal Constraints: Reliable Robot Control with Learned Safe Sets](https://arxiv.org/abs/2611.06196)
🏷️ 交叉方向 / Also: 安全 RL
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 MPC 与 RL 的安全保证通常依赖难以精确计算的控制不变集。作者提出比经典控制不变集更宽的新型安全集,并分析在预测时域的不同节点(而非仅终端状态)施加约束的 MPC 方案以保证递归可行;当安全集是不变集的内逼近时,可通过安全中止策略在无递归可行性时仍保证安全。6 关节机械臂大量仿真显示约束违反少于现有方法且跟踪性能与计算效率相当,并有真机实验验证。
- 🇬🇧 Safety for MPC and RL usually relies on control-invariant sets that are intractable to compute exactly. The paper introduces safe-set classes broader than invariant sets and MPC schemes constraining intermediate horizon nodes (not only the terminal state) to guarantee recursive feasibility, plus a safe-abort strategy when the set is an inner approximation. Simulations on a 6-joint manipulator show fewer constraint violations than state of the art with comparable tracking and computation, and hardware experiments confirm practicality.

### [cuRoboV2-Fast: Fast Torque-Limited Collision-Free Motion Planning](https://arxiv.org/abs/2611.06913) — NVIDIA
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/NVlabs/curobo);摘要声明 Apache 2.0,仓库匿名可访问(是否已含 V2-Fast 代码未核对),另有[项目页](https://www.research.nvidia.com/labs/lpr/curobov2-fast)
- 🇨🇳 需要降低无碰撞、考虑载荷、力矩受限运动的规划延迟与执行时间。cuRoboV2-Fast 用 B 样条轨迹优化减少迭代,加速机器人计算与可微逆动力学以适应变载荷,并用 TimeOpt 在固定路径上对采样的速度/加速度/加加速度/力矩约束优化通过速度,利用局部样条支撑在 GPU 上高效求解带状牛顿系统。3kg 载荷下 RTX 5090 平均规划时间 4.4 ms,比 cuRoboV2 快 14.7 倍;Jetson AGX Orin 上比 RTX 5090 上的 cuRoboV1+TOPPRA 还快;YAM 立体相机部署平均取放周期 5.93 s,比 cuRoboV2 缩短 34.6%。
- 🇬🇧 Collision-free, payload-aware, torque-limited planning needs lower latency and execution time. cuRoboV2-Fast uses B-spline trajectory optimization, accelerated robot computations and differentiable inverse dynamics, plus TimeOpt that optimizes traversal speed under sampled velocity/acceleration/jerk/torque limits with GPU banded Newton solves. With a 3 kg payload it plans in 4.4 ms on RTX 5090 (14.7x faster than cuRoboV2), on Jetson AGX Orin it outpaces cuRoboV1+TOPPRA on RTX 5090, and a stereo-camera YAM deployment completes pick-and-drop cycles in 5.93 s (34.6% shorter).

### [C∞ Smooth Trajectory Planning with Application to Soft Robots](https://arxiv.org/abs/2611.05615)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 软体连续体机器人的平滑度需求未知,可能远超工业机器人 C4 或四旋翼 C5。作者提出 C∞ 平滑的轨迹生成器,在满足运动学限制的同时生成无穷可导轨迹(速度、加速度、jerk、snap 等均连续),特别针对零边界条件。方法在仿真与硬件上得到验证;摘要未给出定量数字。
- 🇬🇧 Smoothness needs for soft continuum robots are unknown and may exceed C4 (industrial) or C5 (quadrotors). The paper introduces a C∞-smooth trajectory generator respecting kinematic limits with all derivatives continuous, notably under null boundary conditions. It is verified in simulation and on hardware; no quantitative figures in the abstract.

### [Riemannian Optimization-based Whole-body Obstacle Avoidance for Mobile Continuum Robots in Cluttered Environments](https://arxiv.org/abs/2611.06214)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 移动连续体机器人的全局规划与局部控制常被割裂,限制了底座-臂协同、运动学一致与避障。框架全局层用 A* 与最小 jerk 规划生成平滑参考轨迹,局部层用几何一致逆运动学求解器与黎曼优化协调底座运动和连续体形变并避障。管道穿行仿真对比多种规划器、真实实验涵盖密集障碍导航与受限空间操作,显示运动一致性、可行性和适应性提升;摘要未给数值。
- 🇬🇧 Planning and local control for mobile continuum robots are usually separate, hurting base-arm coordination, kinematic consistency and collision avoidance. The framework pairs a global A* + minimum-jerk layer with a local layer using geometry-consistent IK and Riemannian optimization for coordinated base motion and continuum deformation. Pipe-traversal simulations against multiple planners and real experiments in dense obstacles and confined manipulation show better motion consistency, feasibility and adaptability; no numbers are given.

**条目总数 / Total**:6 篇均展开。 / 6 expanded.

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

### [Open-HumanScale: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models](https://arxiv.org/abs/2611.06817) — PKU DAGroup
🏷️ 交叉方向 / Also: 世界模型与 WAM / World Models & WAM(HumanWAM)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/DAGroup-PKU/HumanNet);Comments 称含 Open-HumanScale-50K 语料、数据清洗与预训练流水线、预训练/后训练 HumanWAM 权重、推理代码与仿真评测套件;[项目页](https://dagroup-pku.github.io/open-humanscale/)
- 🇨🇳 第一视角人类视频是机器人操作先验的可扩展来源,但需要严格的数据整理与训练配方。作者发布首个完全开放的 5 万小时第一视角预训练配方(带手部运动与语言标注),发现下游机器人成功率与预训练小时数呈对数线性缩放律,并训练仅用人类视频的 World-Action Model HumanWAM-Vanilla。机器人后训练后 RoboTwin 2.0 Clean2Clean 92.08%、Clean2Random 68.88%,RoboDojo 平均成功率 14.17%;人机联合预训练的 HumanWAM-Goal 把 RoboTwin 2.0 提升到 92.70% / 84.60%,真机展现无需更新参数的具身上下文学习。
- 🇬🇧 Egocentric human video is a scalable manipulation prior but needs careful curation and recipes. The authors release a fully open 50,000-hour egocentric pretraining recipe with hand-motion and language annotations, find a log-linear scaling law between pretraining hours and robot success, and train HumanWAM-Vanilla, a world-action model on human video only. After robot post-training it reaches 92.08% (Clean2Clean) and 68.88% (Clean2Random) on RoboTwin 2.0 and 14.17% on RoboDojo; joint human-robot HumanWAM-Goal raises RoboTwin 2.0 to 92.70% / 84.60% and shows emergent in-context adaptation to unseen visual goals on real robots.

### [ELA: End-to-End Latent Action Policy Learning from Video Demonstrations](https://arxiv.org/abs/2611.05571)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://end2end-latent-action.github.io/)
- 🇨🇳 模仿学习受限于带动作标签数据,而现有潜在动作方法没有为下游控制优化潜在动作,难以建模也难以解码为连续动作。ELA 联合训练潜在动作模型、潜在动作策略与动作解码器,只需少量带动作标注的机器人演示即可利用大量视频。仿真与真机操作任务上一致优于先前潜在动作基线,并以轻量 4M 参数解码器无缝集成到现有模仿学习方法;摘要未给具体数值。
- 🇬🇧 Imitation learning is limited by action-labeled data; existing latent-action methods do not optimize latent actions for control. ELA jointly trains a latent action model, latent action policy and action decoder so policies can exploit video with only a few action-labeled demos. It consistently beats latent-action baselines in simulated and real manipulation and plugs into existing imitation methods through 4M-parameter decoders; no numbers in the abstract.

### [MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics](https://arxiv.org/abs/2611.05567) — CoRL 2026
开源状态 / Code: ✅ 已发布 / Released(基准)— 摘要称发布单臂 MESA 与双臂 BiMESA 套件,见[项目页](https://pairlab.github.io/MESA);未核对仓库链接
- 🇨🇳 基础模型操作能力缺乏系统评测:现有基准要么饱和,要么缺乏受控性。MESA 提供五个评测套件,隔离分布内性能与空间配置、物体实例、物体类别、子任务组合四个泛化轴,并用改进 MimicGen 的 MESA-Gen 规模化生成任务与示范,发布单臂 MESA 与首个大规模双臂泛化基准 BiMESA。七个基线(扩散策略、VLM 方法、预训练 VLA)中最强模型在 MESA 仅 52%、BiMESA 49%,排名与 RoboArena 大体一致。
- 🇬🇧 Foundation-model manipulation lacks systematic evaluation. MESA has five suites isolating in-distribution performance and four generalization axes (spatial configuration, object instance, object category, subtask composition), populated by MESA-Gen (built on improved MimicGen), and releases single-arm MESA plus BiMESA, the first large-scale bimanual generalization benchmark. Across seven baselines the best reaches only 52% on MESA and 49% on BiMESA, with rankings broadly consistent with RoboArena.

### [Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2611.06475)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 现有基准对移动操作中依赖记忆的决策评测有限。RoboCasa-Mem 含九个任务,涵盖环境记忆(位置、属性、关系)与过程记忆(进度、多任务调度),提出行为条件评测(由机器人先前行为推导后续约束),提供 1,800 条成功示范和基线 HMAP(高层规划器使用结构化实体/过程记忆生成子任务,低层 VLA 控制器用子目标条件查询融入 VGGT-Omega 几何)。摘要未报告 HMAP 的具体成绩。
- 🇬🇧 Existing benchmarks poorly test memory-dependent mobile manipulation. RoboCasa-Mem offers nine tasks across environment memory (locations, attributes, relations) and process memory (progress, scheduling), a behavior-conditioned evaluation deriving later constraints from the robot's earlier actions, 1,800 demonstrations and the HMAP baseline (memory-based high-level planner plus subgoal-conditioned VLA with VGGT-Omega geometry). The abstract reports no HMAP numbers.

### [Correct Robots Before They Make Mistakes: Proactive Human-in-the-Loop Intervention via Preference Learning (PHIL)](https://arxiv.org/abs/2611.05667)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://intuitive-robots.github.io/PHIL-page/)
- 🇨🇳 人在回路纠错通常在错误发生后介入。PHIL 让操作员通过 XR 预览策略预测的未来运动并在错误前接管,把被拒绝的预测与同一状态、同一时域内随后执行的纠正动作块配对,做基于偏好的后训练。四个真机操作任务、每条件 5 个纠正回合时,相对 HG-DAgger,扩散策略平均成功率 44.0%→70.3%,X-VLA 57.8%→76.9%,且成功回合中不必要的恢复行为更少。
- 🇬🇧 Human-in-the-loop correction usually happens after errors. PHIL lets operators preview predicted motion via XR and intervene early, pairing rejected predictions with corrective chunks from the same state/horizon for preference-based post-training. On four real tasks with five correction episodes, versus HG-DAgger it raises mean success from 44.0% to 70.3% (diffusion policy) and 57.8% to 76.9% (X-VLA), with fewer unnecessary recoveries.

### [PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real World](https://arxiv.org/abs/2611.06768)
开源状态 / Code: ❓ 未知 / Unknown(同组[PyRUA-Lean 仓库](https://github.com/DAGroup-PKU/PyRUA-Lean)在 radar 中出现,未确认对应本文)
- 🇨🇳 研究编码智能体如何通过真机交互产生持久的机器人能力提升。PyRUA-REAL 让编码智能体将交互经验保留为持久记忆与可复用可执行技能,并研究协作方式、执行反馈类型、任务说明与已有技能对鲁棒性和迁移的影响,以及无需在线智能体的部署效率。八个真实任务平均成功率 91.1%,RoboDojo 的 42 个任务上平均 84.4%。
- 🇬🇧 The paper studies how coding agents can make lasting robot improvements from physical interaction. PyRUA-REAL retains experience as persistent memory and reusable executable skills, examining agent collaboration, feedback types, task specs and prior skills, and deployment without an online agent. It averages 91.1% success on eight real tasks and 84.4% on 42 RoboDojo tasks.

### [Dexterous Robotic Hands in the Foundation-Model Era: A Full-Stack Survey](https://arxiv.org/abs/2611.06724)
开源状态 / Code: 不适用(综述)/ N/A (survey)
- 🇨🇳 综述 2024 年 1 月至 2026 年 11 月初灵巧手的硬件、数据、跨本体迁移、学习与基础模型、评测五层文献,辅以人手-物体理解与触觉两个横切视角。结论:人类数据价值取决于运动学/视觉/接触对齐而非数据量;共享动作表示与基础策略不能消除力、延迟与接触上的本体约束;仅任务完成不足以证明物理正确与部署就绪。提出十一个开放问题。
- 🇬🇧 A 45-page structured review of dexterous hands (Jan 2024–early Nov 2026) across hardware, data, cross-embodiment transfer, learning/foundation models and evaluation, with human hand-object understanding and tactile sensing as cross-cutting lenses. It concludes that human-data value depends on kinematic/visual/contact alignment, shared action representations do not remove embodiment constraints on force/latency/contact, and task completion alone does not establish physical correctness; eleven open problems are identified.

### [RACE: Calibrated Cumulative Scoring for Rollout-Free Robot Policy Checkpoint Selection](https://arxiv.org/abs/2611.05838)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://changyeon.site/race)
- 🇨🇳 真机评估每个检查点成本高,平均验证损失与部署成功率排序不一致。RACE 用保留的成功轨迹,以相似状态下动作差异导出的状态条件阈值校准动作偏差,并用连乘累积分数使大偏差削弱后续参考预测权重。仿真中优于基线且在验证集变化时更稳,真机上的排名与多种策略骨干和不同难度任务的部署成功一致;摘要未给数值。
- 🇬🇧 Real-robot checkpoint evaluation is costly and validation loss ranks poorly. RACE calibrates action deviations against state-conditional thresholds from held-out successful trajectories and aggregates by a running product so large deviations discount later predictions. It beats baselines in simulation (robust to validation-set changes) and aligns with deployment success on real robots across backbones and tasks; no numbers in the abstract.

### [Can Astra Solve RoboMME without Breaking the Bank?](https://arxiv.org/abs/2611.06184) — CoRL 2026 workshop
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://bingaochen.github.io/Astra-on-RoboMME/)
- 🇨🇳 记忆型操作需要记住不可见信息,但每个动作块前都调用大型规划器慢且贵。三层系统:GPT-6 Astra(System 2)从视觉历史选定子任务,π0.5 VLA(System 1)执行,微调的 Qwen3-VL-4B 监视器(System 1.5)判断子任务是否完成。RoboMME 上成功率 79.13%,平均每回合 3.63 次 Astra 调用、80.84 秒,比最佳已发表非 oracle 基线高 34.62 个点,仅比用真值子目标的 GroundSG+Oracle 低 4.95 点。
- 🇬🇧 Memory-dependent manipulation needs remembered information, but calling a large planner before every action chunk is slow and costly. A three-tier system pairs GPT-6 Astra (System 2) picking subtasks from visual history, a π0.5 VLA (System 1) executing them, and a fine-tuned Qwen3-VL-4B monitor (System 1.5) judging completion. On RoboMME it reaches 79.13% success with 3.63 Astra calls and 80.84 s per episode, 34.62 points above the best published non-oracle baseline and 4.95 below GroundSG+Oracle.

**列名 / Also listed (总数 / total 14 = 9 展开 + 5 列名)**:[VABAR](https://arxiv.org/abs/2611.06881)(Newton 引擎的变体自动化基准,33 个技能 / benchmark on Newton with 33 skills)、[Which Physical Tactile Cues Matter for Contact-Rich Imitation Learning?](https://arxiv.org/abs/2611.06673)(触觉将成功率 57.8%→78.9%,720 次真机试验)、[Online Adaptation to Latent Physical Properties for LfD](https://arxiv.org/abs/2611.06118)、[Rethinking Self-Repair in Code-as-Policy Agents](https://arxiv.org/abs/2611.06863)、[Detecting Silent Action-Interface Mismatch with Calibrated Relational World Models](https://arxiv.org/abs/2611.06653)。
另见 / See also:[Open-HumanScale](https://arxiv.org/abs/2611.06817) 的 WAM 部分见世界模型小节(已归入本类)。

---

## VLA

### [From Pixels to Actions - Towards Native Vision-Language-Action Policies (NEO-VLA)](https://arxiv.org/abs/2611.06918)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/EvolvingLMMs-Lab/NEO)(Comments 指向 `VLAKit` 子目录;仓库匿名可访问)。HF Daily Papers 56 upvotes
- 🇨🇳 常规 VLA 先用视觉编码器压缩感知再做动作推理,而操作依赖易被抽象损失的局部几何、边界、深度等信号。NEO-VLA 为无编码器结构:轻量 patch 卷积分词,图像与语言在骨干中共同演化,流匹配动作专家可读取不同深度的指令条件视觉表示。受控比较中原生架构优于有编码器的对应模型,完全微调缩小但不能消除差距,仅靠增大规模也无法弥补;逐层探测显示动作关键信号常在最终视觉表示之前就达峰;摘要未给出具体基准数字。
- 🇬🇧 Standard VLAs compress perception with a visual encoder before action reasoning, though manipulation hinges on local geometry, boundaries and depth. NEO-VLA is encoder-free: patch-conv tokenization with images evolving jointly with language in the backbone, and a flow-matching action expert reading instruction-conditioned features at multiple depths. Native architectures beat encoder-based ones under controlled comparisons, full fine-tuning narrows but does not close the gap, scale alone does not recover it, and probing shows action-critical signals peak before the final visual layer; no benchmark numbers in the abstract.

### [A³-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation](https://arxiv.org/abs/2611.06447)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 VLA 的动作预测目标缺乏细粒度感知监督,容易依赖无关视觉捷径。A³-VLA 从交互引起的视觉变化生成目标与机器人候选区域并用分割模型离线精修,通过注意力分配损失和区域-语言对比损失显式引导。仿真与真机上稳定提升多个 VLA 骨干,不同基准平均成功率增益 6.5%–25.2%。
- 🇬🇧 VLA action objectives lack fine-grained perceptual supervision and attend to shortcuts. A³-VLA derives candidate target/robot regions from interaction-induced visual changes, refines them offline with a segmentation model, and applies an attention allocation loss plus a region-language contrastive loss. It improves multiple VLA backbones in simulation and the real world with average success gains of 6.5%–25.2%.

### [Where Is VLA Inference Time Spent? Bottlenecks and Optimization Interactions Across GPUs](https://arxiv.org/abs/2611.06710)
开源状态 / Code: ❓ 未知 / Unknown(基准/测量研究)
- 🇨🇳 VLA 推理常慢于实时需求,既有优化多在单一 GPU、少数模型上报告。本文对七类推理优化(CUDA graph、编译、token 剪枝、量化等)在七个 SOTA VLA、四类 GPU(H100 到 Jetson Thor)上做测量,分析 CPU 启动开销、显存带宽与内核效率及优化间的相互作用,并总结出 VLA-Triage 指南。结论为在延迟预算下叠加优化的实用准则;摘要未给具体加速数字。
- 🇬🇧 VLA inference often misses real-time budgets and optimizations are reported on one GPU. This measurement study covers seven families of optimizations (CUDA graphs, compilation, token pruning, quantization…) on seven VLAs across four GPUs (H100 to Jetson Thor), analyzing launch overhead, memory bandwidth and kernel efficiency and their interactions, distilled into VLA-Triage guidelines for stacking under latency budgets; no speedup numbers in the abstract.

### [Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection (B2FF)](https://arxiv.org/abs/2606.09258) — 替换版,CoRL 2026
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 VLA 偏离标称轨迹后,直接重规划常使动作序列不稳。B2FF 在执行前由 VLA 基于干净初始观测生成「熟悉未来状态」里程碑库,恢复时由可恢复性感知选择器选一个里程碑作为固定视觉目标,无需微调底层动作生成器。在注入失败的 LIBERO 上,基线 VLA 平均成功率 56.3%→74.0%。
- 🇬🇧 After deviating, direct re-planning destabilizes VLA actions. B2FF pre-generates a bank of familiar future milestones from the clean initial observation and a recoverability-aware selector enforces one as a fixed visual goal at recovery time, with no fine-tuning of the low-level generator. On failure-injected LIBERO it raises a baseline VLA from 56.3% to 74.0% average success.

### [Bridging the Morphology Gap: Adapting VLA Models to Dexterous Manipulation via Intent-Conditioned Fine-Tuning (InDex)](https://arxiv.org/abs/2606.12109) — 替换版
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 平行夹爪 VLA 的接口使多指接触协调隐式。InDex 用重定向示范导出的归一化开合信号监督标量抓取意图,第一阶段学习同步的末端-意图块,第二阶段让扩散手部解码器以这些预测、视觉语言上下文与本体感知为条件。四个仿真任务上 InDex+π0.5 平均成功率 85.8%(比原生策略高 35.5 个点),相似几何的保留物体 69.0%;跨三种 VLA 骨干成立,真机平均 71.0%→83.0%。
- 🇬🇧 Parallel-gripper VLAs leave multi-finger coordination implicit. InDex supervises a scalar grasp-intent from retargeted demonstrations, learns synchronized end-effector–intent chunks, then conditions a diffusion hand decoder on them plus visual-language context and proprioception. With π0.5 it hits 85.8% mean success on four sim tasks (+35.5 points), 69.0% on held-out similar objects, holds across three backbones, and real-world success rises from 71.0% to 83.0%.

### [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381) — 替换版
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 VLA 对物理动力学理解有限,而视频世界模型在控制环内生成未来视频延迟高。PDRVLA 的轻量物理动力学模块从视觉-语言特征提取物理 token 条件化动作生成,无需在线视频生成,通过预测未来 RGB、深度与光流特征学习并辅以冻结视频世界模型监督,训练仅用公开数据。四个仿真基准成功率:LIBERO 99.3%、LIBERO-Plus 89.9%、RoboTwin 2.0 93.6%、SimplerEnv 81.5%。
- 🇬🇧 VLAs understand physical dynamics poorly, while video world models add latency by generating future video. PDRVLA's lightweight Physical Dynamics Module extracts physical tokens from vision-language features to condition action generation without online video generation, learning via future RGB/depth/flow feature prediction with auxiliary frozen video-world-model supervision, trained on public data only. It reaches 99.3% on LIBERO, 89.9% on LIBERO-Plus, 93.6% on RoboTwin 2.0 and 81.5% on SimplerEnv.

**列名**:[Test-Time Improvement of VLA Policies via Selected Diffusion Noise](https://arxiv.org/abs/2606.14084)。共 7 条(6 展开 + 1 列名)。
另见 / See also:[HALO](https://arxiv.org/abs/2611.06908)(已归入 运动控制·RL)、[Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement](https://arxiv.org/abs/2611.06905)(已归入 运动控制·RL)。

---

## VLN

### [X-Fly: Learning to Reach and Stop in Full-Chunk Aerial Vision-Language Navigation](https://arxiv.org/abs/2610.21450) — 替换版
🏷️ 交叉方向 / Also: 运动控制·RL(Flow-GRPO 精修;任务为空中视觉语言导航,判为 VLN 主任务)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://juliusju572.github.io/x-fly/)
- 🇨🇳 空中 VLN 基于大视觉语言模型查询昂贵,执行完整动作块再重规划可摊销成本,但使策略查询状态偏离专家示范,缺乏恢复与自主终止监督;OpenFly test-seen 上完整块行为克隆的失败中 47.78% 是不停止。X-Fly 采用分阶段训练:Recovery DAgger 标注学习者访问的状态,再用 Flow-GRPO 联合精修分块流控制器与伯努利 STOP 策略。每决策八次控制时,test-seen / test-unseen 成功率 74.18% / 51.73%,而完整块 BC 为 16.45% / 18.43%,DreamFly 为 32.04% / 29.46%。
- 🇬🇧 Aerial VLN with large VLMs is expensive to query; executing whole action chunks amortizes cost (195→42 ms per waypoint) but pushes states off expert demonstrations; no-stop failures are 47.78% of full-chunk BC on OpenFly test-seen. X-Fly uses Recovery DAgger labels at learner-visited states, then Flow-GRPO to jointly refine the chunked flow controller and a Bernoulli STOP policy. With eight controls per decision it reaches 74.18% / 51.73% SR on test-seen / unseen versus 16.45% / 18.43% (full-chunk BC) and 32.04% / 29.46% (DreamFly).

### [EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation](https://arxiv.org/abs/2610.27616) — 替换版
🏷️ 交叉方向 / Also: 空间智能(VGGT-Omega)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 杂乱环境视觉导航需恢复已观测结构并推断被遮挡的障碍与自由空间。EchoNav 在证据式鸟瞰(BEV)表示中结合时间聚合与占据补全,解码器适配冻结的 VGGT-Omega 特征,无需深度或位姿输入或显式几何变换,并预测带置信度的占据。仿真连续双目标导航成功率 86.3%,比最强基线高 32.2 个点;轮式机器人 20 个场景 60 次试验成功率 73.3%(最强基线 33.3%),并在四足与人形上演示。
- 🇬🇧 Cluttered-environment navigation needs recovering seen structure and inferring occluded space. EchoNav combines temporal aggregation and occupancy completion in an evidential BEV from short RGB sequences, adapting frozen VGGT-Omega features without depth/pose inputs or explicit warping and predicting occupancy with confidence. It achieves 86.3% success in simulated two-goal navigation (+32.2 points over the strongest baseline), 73.3% over 60 wheeled-robot trials in 20 scenes (baseline 33.3%), with quadruped/humanoid demos.

### [OdorSpaces: Visual-Olfactory Embodied Navigation in 3D Environments](https://arxiv.org/abs/2611.05738) — CoRL 2026
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 嗅觉在具身 AI 中研究不足。OdorSpaces 为 Habitat-Sim 增加由 FDS 模拟的 3D 气味传输与扩散,提供不可见气体泄漏定位与早期火源定位两个视觉-嗅觉导航场景,并给出融合视觉与随时间嗅觉测量的多模态 RL 初始策略,在多种基线上表现更优(摘要无数值)。
- 🇬🇧 Olfaction is underexplored in embodied AI. OdorSpaces augments Habitat-Sim with FDS-simulated 3D odor transport for gas-leak and fire localization, and an initial multimodal RL policy fusing vision and temporal olfactory measurements outperforms diverse baselines (no numbers in the abstract).

**列名**:[When to Ask for Help: Uncertainty-Triggered Aerial Refinement for Off-Road Navigation](https://arxiv.org/abs/2611.06702)、[KEPT: Conformal Keepouts](https://arxiv.org/abs/2610.37217)。共 5 条。

---

## 世界模型与 WAM / World Models & WAM

### [Future Representation Distillation for Imagination-free World Action Models (DreamFree)](https://arxiv.org/abs/2611.04527) — 替换版
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://harryjo97.github.io/dreamfree/)
- 🇨🇳 WAM 通过未来视频预测借用视频扩散模型知识,但迭代去噪昂贵且不准的视觉预测会损害动作。DreamFree 通过表示蒸馏把预训练视频扩散模型改造为预测性视觉编码器:编码器只用当前观测预测冻结视频模型的表示,再训练动作模块。真机与仿真上成功率高于 SOTA VLA 与 WAM,14B 视频扩散骨干下以 11Hz 实时闭环控制,并能用无动作标注的视频(含不同本体)学习新任务。
- 🇬🇧 WAMs borrow video-diffusion knowledge via future video prediction, but denoising is costly and inaccurate frames hurt actions. DreamFree distills a frozen video diffusion model's representation into an encoder that predicts it from the current observation alone, then trains an action module. It outperforms SOTA VLAs and WAMs in real/simulated tasks, runs closed-loop at 11 Hz with a 14B backbone, and learns new tasks from action-free videos, including from other embodiments.

### [Gnomon4D: Learning Where and When to Focus for Geometric Motion-Grounded World-Action Modeling](https://arxiv.org/abs/2611.02474)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://droliven.github.io/Gnomon4D)
- 🇨🇳 现有 WAM 的 RGB 未来纠缠外观且缺 3D 几何,动作注意力低估本体-物体交互。Gnomon4D 联合生成未来视频、动作与 GeoDelta(像面位移+深度变化的 4D 几何运动场),用交互显著注意力(InSAttn)选择动作读取位置、转换锚定聚合(TransAgg)选择抓取/释放附近时刻;GeoDelta 作为人-机准动作连接 EgoManip-5000H 无动作预训练与 Robot-30H 中训练。在 RoboTwin 2.0、VLABench、RoboDojo 领先,并在视觉偏移下优于真机基线。
- 🇬🇧 RGB futures in WAMs entangle appearance and lack 3D geometry, and action attention underweights embodiment-object interactions. Gnomon4D jointly generates future video, actions and GeoDelta (a 4D motion field of image displacement and depth change), with Interaction-Salient Attention choosing where and Transition-Anchored Aggregation choosing when (around grasp/release); GeoDelta links action-free pretraining on EgoManip-5000H with robot mid-training on Robot-30H. It leads on RoboTwin 2.0, VLABench and RoboDojo and beats real-robot baselines under visual shifts.

### [DreamX: Video Diffusion Model is a Universal Latent Action Learner](https://arxiv.org/abs/2611.05377) — HF 54 upvotes
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://cvlab-kaist.github.io/DreamX/)
- 🇨🇳 现有潜在动作模型的表示与视觉变化纠缠,限制跨本体迁移。DreamX 把预训练视频扩散模型用作通用潜在动作学习器,从其时空特征提取紧凑潜在动作(每帧 1,200→4 个 token,压缩 300 倍),利用生成先验与外观解耦。在 LARY-Bench 上潜在动作模型中达到 SOTA,支持任意到任意视频迁移与跨本体/环境零样本动作迁移,并降低基于视频扩散的策略计算成本。
- 🇬🇧 Latent-action models entangle action with visual variation, hurting cross-embodiment transfer. DreamX repurposes a pretrained video diffusion model as a universal latent action learner, extracting compact latent actions (1,200→4 tokens per frame, 300x) disentangled from appearance by the generative prior. It sets SOTA among latent-action models on LARY-Bench, enables any-to-any video transfer and zero-shot cross-embodiment action transfer, and cuts the cost of video-diffusion policies.

### [ReactWorld: Structuring Interaction Responses for Embodied Video Generation](https://arxiv.org/abs/2611.06120)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://metaengine-world.github.io/ReactWorld/)
- 🇨🇳 具身视频世界模型生成的物体响应常与任务意图和接触动力学不一致。ReactWorld 在生成骨干特征空间用交互响应场预测器预测参与者角色、未来运动响应强度与局部运动变化,并用响应反馈适配器改变物体特征更新和跨帧检索。RBench 平均 77.51,比 PhysisForcing 高 3.29 且九类全部提升;EZS-Bench 领域分 86.98、平均 81.87。
- 🇬🇧 Embodied video world models often produce object responses inconsistent with intent and contact. ReactWorld predicts an interaction response field (roles, response intensity, local motion) in feature space and uses a response feedback adapter to guide object feature updates and temporal attention. It scores 77.51 on RBench (+3.29 over PhysisForcing, all nine categories improved) and 86.98 / 81.87 on EZS-Bench.

### [Interactive World Simulation with Cosmos for Physical AI](https://arxiv.org/abs/2611.06627) — NVIDIA
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/nvidia/cosmos),[检查点集合](https://huggingface.co/collections/nvidia/cosmos3-examples)
- 🇨🇳 将 Cosmos 世界基础模型适配为面向 Physical AI 的实时交互世界模拟:按动作和场景控制流式输出视觉观测,既能预测动作的视觉后果,也能依据外部模拟器维护的物理状态生成观测。演示覆盖相机导航、机器人操作、可控视频迁移和多视角自动驾驶仿真。摘要为系统/框架描述,未给定量结果。
- 🇬🇧 The framework adapts Cosmos world foundation models for real-time interactive simulation, streaming observations in response to actions and scene controls, both predicting action consequences and rendering from external simulator state. Demos span camera navigation, robot manipulation, controllable video transfer and multi-view AV simulation. The abstract gives no quantitative results.

### [SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models](https://arxiv.org/abs/2610.06598) — 替换版
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Wang-Xiaodong1899/SimForcing)(匿名可访问)
- 🇨🇳 动作条件机器人世界模型需精确响应轨迹又保持真实动态,而仿真与真实外观差异阻碍迁移。SimForcing 用潜在运动蒸馏从仿真教师迁移运动先验,并以多块仿真条件加条件丢弃利用预测的仿真轨迹,统一的仿真条件 CFG 平衡两者;学生联合生成仿真条件与真实视频,推理无需额外世界模型。在 Bridge 上 PSNR、SSIM、LPIPS、FVD 均为对比方法最佳(无外部具身预训练),并在 InternData-A1 上进一步验证。
- 🇬🇧 Action-conditioned robot world models must follow trajectories precisely while staying realistic, but sim–real appearance gaps hinder transfer. SimForcing distills motion priors from a simulation teacher via latent-motion distillation and uses multi-block simulation conditioning with condition dropout under a unified sim-conditioning CFG; the student generates both and needs no extra world model at inference. It achieves the best PSNR/SSIM/LPIPS/FVD on Bridge without external embodied pretraining and is further validated on InternData-A1.

### [Time-to-Goal: Learned Temporal Metrics for Long-Horizon Planning with JEPA World Models](https://arxiv.org/abs/2611.05847)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 JEPA 规划比较预测潜在状态与目标编码,但训练并不保证「越接近目标代价越低」。T2G 用边际排序损失在离线轨迹的潜在三元组上学习时间距离度量,冻结 JEPA 编码器和预测器,替换欧氏规划代价,无需奖励或策略标签。四个导航/操作基准上平均规划成功率从 flat LeWM 的 32.7% 提高到 63.0%,接近甚至超过层次化 H-JEPA 基线。
- 🇬🇧 JEPA planning compares predicted latents to a goal embedding, but training does not enforce temporal ordering in the cost. T2G learns a time-to-goal metric with a margin ranking loss on latent triples from offline trajectories, replacing the Euclidean cost while the encoder/predictor stay frozen, with no rewards or policy labels. Across four navigation and manipulation benchmarks it raises average planning success from 32.7% (flat LeWM) to 63.0%, approaching or surpassing hierarchical H-JEPA baselines.

### [TouchéWorld tech report](https://arxiv.org/abs/2611.06061)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 视频世界模型允许相机探索,但缺乏连续手部运动这一细粒度交互通道。TouchéWorld 将手势驱动交互整合进相机控制的视频世界模型:从异构第一视角视频构建相机-手联合数据,在预训练模型上结合手骨架条件与手运动数值特征做参数高效适配,并通过因果适配与少步蒸馏实现分块在线生成,同时提出 TouchéBench。技术报告,摘要无定量结果。
- 🇬🇧 Camera-controlled video world models lack a fine-grained hand-motion channel. TouchéWorld integrates gesture-driven interaction by building joint camera-hand data from egocentric videos, adapting a pretrained model with hand-skeleton conditioning and hand-motion features, and supporting chunk-level online generation via causal adaptation and few-step distillation, plus TouchéBench. As a tech report, the abstract has no quantitative results.

### [Jev with Foresight: Safe Language-Guided Autonomous Driving via a Language World Model](https://arxiv.org/abs/2611.05448)
🏷️ 交叉方向 / Also: 自动驾驶
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://ys-qu.github.io/jev-ad-website)
- 🇨🇳 LLM 驾驶代理用生成文本推理耗时且隐式推断动作后果。Jev-AD 将给出概率的类型化决策模型 Jev 与语言世界模型结合,后者预测每个候选动作下周围车辆 2 秒内运动,由代码转为可预见后果供比较。高速公路并线仿真(500 车次)碰撞率 26.0%→2.4%,每次决策 0.25 s,自由语言指令意图达成 93%;500 个 NGSIM 回放碰撞率 48.2%→2.8%,世界模型预见 93% 的危险动作。
- 🇬🇧 LLM driving agents reason slowly in text and infer consequences implicitly. Jev-AD pairs a typed probabilistic decision model with a language world model predicting nearby vehicles' 2-second motion per candidate action, turned into foreseen consequences by code. In highway merging (500 episodes) collisions fall 26.0%→2.4% at 0.25 s/decision with 93% intent fulfillment; on 500 NGSIM replays 48.2%→2.8%, foreseeing 93% of dangerous actions.

**列名**:[Motion-guided Contrastive Regularization For Latent World Models](https://arxiv.org/abs/2611.06901)。共 10 条(9 展开 + 1 列名)。radar 中相关仓库见 GitHub 小节(Ropedia W0、Verne V0.5、FlowPilot)。
另见 / See also:[Terrain-Grounded Imagination](https://github.com/leggedrobotics/terrain-grounded-imagination)、[BlinkMimic](https://github.com/fuyichen0725/blinkmimic)(均已归入 运动控制·RL)、[Open-HumanScale](https://arxiv.org/abs/2611.06817)(已归入 具身智能与机器人基础模型)。

---

## 空间智能与 SLAM / Spatial Intelligence & SLAM

### [Scale Anchoring via Implicit Semantics and Sequence-Consistent Loop Closure for VGGT-Based SLAM](https://arxiv.org/abs/2611.06308)
开源状态 / Code: ❓ 未知 / Unknown(投稿 ICRA 2027)
- 🇨🇳 前馈几何基础模型使无标定稠密单目重建成为可能,但独立重建的子图会累积尺度漂移,有效回环也可能产生不一致的跨子图测量。作者在 VGGT-SLAM 2.0 上加入固定根尺度锚定与短序列辅助的直接回环连接:SALAD 选图像对,联合 VGGT 推理给出仅尺度的锚,回环通过邻近图像对一致性检验和平移尺度对齐产生 Sim(3) 因子。TUM 九个序列的平均 Sim(3) ATE 从 0.1018 m 降到 0.0451 m,七个无回环模块消融均改进。
- 🇬🇧 Feed-forward geometric foundation models enable calibration-free dense monocular reconstruction, but submaps accumulate scale drift and valid revisits can give inconsistent cross-submap measurements. The authors extend VGGT-SLAM 2.0 with fixed-root scale anchoring (SALAD-selected pairs, joint VGGT inference) and short-sequence-assisted direct loop connections yielding robust Sim(3) factors. Mean Sim(3) ATE on nine TUM sequences drops from 0.1018 m to 0.0451 m and anchoring improves all seven no-loop ablations.

### [UniLoop: Unified Loop Closure Detection from Retrieval to Geometric Verification and Relative Pose Estimation](https://arxiv.org/abs/2611.06378)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 传统回环检测级联检索、几何验证、相对位姿三个模型,计算冗余且表示割裂。UniLoop 复用预训练几何基础模型的层次表示:共享编码器提供全局描述子,同特征送入跨视图解码器做成对验证,并用其几何预测提供位姿图约束。MSLS Recall@10 96.6、Pitts30k 99.3 为对比方法最佳,验证分支 95.63 AP / 96.29 ROC-AUC,超越现有几何验证基线。
- 🇬🇧 Loop closure cascades separate retrieval, verification and pose models with redundant computation. UniLoop reuses a pretrained geometric foundation model's hierarchy: a shared encoder for global descriptors, a cross-view decoder for pairwise verification, and its geometric predictions as pose-graph constraints. It reaches the best Recall@10 on MSLS (96.6) and Pitts30k (99.3), and 95.63 AP / 96.29 ROC-AUC in verification, surpassing existing baselines.

### [Reflection-Robust Stereo Visual-Inertial Odometry via Kalman-Filtered Ground-Height Estimation](https://arxiv.org/abs/2611.05938) — ICCAS 2026
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 反光地面会产生低于真实地平面的虚拟特征,使 VIO 残差不一致。该文提出轻量的反射感知前端:实时估计地面高度,仅拒绝推断三维位置低于地面高度的特征;用地面掩膜限制验证区域,以立体高度/位姿不确定性构造高度测量,标量卡尔曼滤波加 NIS 门控得到稳定估计,并用不确定性安全裕度选择性剔除。真实反光地面室内序列上总体改善轨迹精度并能从真实地面高度变化中恢复(摘要无数值)。
- 🇬🇧 Reflective floors create virtual features below the true ground plane, corrupting VIO residuals. The lightweight front-end estimates ground height in real time, rejects only features inferred below it, restricts checks to a floor mask, builds measurements from stereo/pose uncertainty, and applies a scalar Kalman filter with NIS gating and an uncertainty-aware margin. On real reflective-floor indoor sequences it generally improves trajectory accuracy and recovers from real height changes (no numbers in the abstract).

### [Event-based SLAM Benchmark for High-Speed Maneuvers (EvSLAM)](https://arxiv.org/abs/2604.24033) — 替换版
开源状态 / Code: ❓ 未知 / Unknown(摘要未给出链接)
- 🇨🇳 事件相机的已有成功多限于近距快摇或纯 3 自由度旋转,任意剧烈 6 自由度机动下的事件状态估计远未解决。作者系统分析 SOTA 事件 VO/VIO 并指出公开数据集不足,提出 EvSLAM 基准框架,覆盖多种采集平台、极端光照与挑战性运动模式。摘要被截取处为基准描述,未见具体定量结果。
- 🇬🇧 Event-camera successes are mostly near-structure fast shaking or pure 3-DoF rotation; arbitrary aggressive 6-DoF maneuvers remain unsolved. The authors analyze SOTA event VO/VIO, expose dataset shortcomings, and introduce the EvSLAM benchmark with varied platforms, extreme lighting and challenging motion patterns. The abstract gives no quantitative results.

### [USI-Brain: Enhancing Underwater Spatial Intelligence via Spatial Data-Driven Vision-Language Modeling](https://arxiv.org/abs/2611.06040)
开源状态 / Code: 🕒 计划开源 / Planned — 摘要称「Model weights and USI-Bench will be released」于 `github.com/SKY-Zhu-91/USI-Brain`,该仓库匿名尚不可访问
- 🇨🇳 水下空间推理受散射、色偏、低能见度所限,现有资源对 VLM 监督碎片化。作者构建空间数据引擎生成 427 万 QA 对(五类能力),训练 USI-Brain 并引入水下先验引导的门控修正器 UPR,同时提出含 6,525 个保留 QA 的 USI-Bench。15 个任务指标上 USI-Brain 与 USI-Brain+UPR 相对 Qwen3-VL-8B-Instruct 平均提升 5.76 与 7.63 点,在 NautData、UWBench、MarineEval 的 32 项指标中 28 项最优或并列最优。
- 🇬🇧 Underwater spatial reasoning suffers from scattering and low visibility, and existing resources give fragmented VLM supervision. A spatial data engine produces 4.27M QA pairs across five capability groups to train USI-Brain with an Underwater Prior-guided Rectifier (UPR), evaluated on the 6,525-QA USI-Bench. Across 15 metrics it improves over Qwen3-VL-8B-Instruct by 5.76 / 7.63 points on average (without / with UPR), and is best or joint-best on 28 of 32 metrics across NautData, UWBench and MarineEval.

**列名**:[RegimeVGGT](https://arxiv.org/abs/2606.18439)、[WayPOP](https://arxiv.org/abs/2611.05801)、[Does RRT* Work on Uneven Terrain Meshes?](https://arxiv.org/abs/2611.05885)(规划类,归入此处仅为地形网格相关)。共 8 条。

---

## 其他值得关注 / Other Notable

- HF Daily Papers(带 githubRepo):[RoboTryOn](https://arxiv.org/abs/2611.05163)([仓库](https://github.com/ryan-seungyong-lee/RoboTryOn),人类视频→灵巧机器人示范)、[Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs](https://arxiv.org/abs/2611.04391)([仓库](https://github.com/jun-brro/h2rb-code))、[PrimeSim](https://arxiv.org/abs/2611.04870)([仓库](https://github.com/PrimebotTech/PrimeSim),通用跨本体世界模型模拟器)、[RoboColosseum](https://arxiv.org/abs/2611.02497)([客户端仓库](https://github.com/RoboColosseum/robocolosseum-client))、[Are Frontier VLM Agents Ready to Be Robot Generalists?](https://arxiv.org/abs/2610.00854)([仓库](https://github.com/embodied-agent-arena/embodied-agent-arena),70 upvotes)。以上仅据 HF 元数据列出,未读正文。
- 其余未归类的 cs.RO 条目(触觉、软体、人机交互、驾驶安全等)已逐条检查,与关注主题无实质关联。 / Remaining cs.RO items (tactile hardware, soft robots, HRI, driving safety, etc.) were checked and are off-topic.

## GitHub 动态 / GitHub Highlights

### 当日 star 增长 / Star Growth(相关项)
| 仓库 / Repo | ★ | Δ | 说明 / Note |
|---|---|---|---|
| [leggedrobotics/terrain-grounded-imagination](https://github.com/leggedrobotics/terrain-grounded-imagination) | 62 | +41 | G1 人形世界模型想象训练稀疏地形行走 / G1 humanoid locomotion via terrain-grounded imagination |
| [groundingpi/GroundingPI](https://github.com/groundingpi/GroundingPI) | 359 | +31 | 4B 物理智能 grounding 基础模型 / 4B grounding model for physical intelligence |
| [fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic) | 155 | +23 | G1 动作跟踪 3 分钟训练 / G1 tracking in ~3 min |
| [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) | 510 | +20 | SuperMimic 第三方资源汇总 / third-party SuperMimic list |
| [Ropedia/ropedia-w0](https://github.com/Ropedia/ropedia-w0) | 259 | +19 | 从 1 万小时人类经验学习 loco-manipulation 世界模型,含 HF 模型与遥操作数据 / loco-manipulation world model, HF weights + teleop data (arXiv 2610.26855) |
| [Junchao-cs/SolarWM](https://github.com/Junchao-cs/SolarWM) | 879 | +16 | 长时程视频世界模型的开放数据与训练 / open data & training for long-horizon video WMs |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28708 | +25 | v0.7.0 发布 / release |
| [dexmal/opendm](https://github.com/dexmal/opendm) | 2266 | +14 | 通用具身基础模型 / open-world embodied FM |
| [mujocolab/mjlab](https://github.com/mujocolab/mjlab) | 3339 | +9 | MuJoCo-Warp 版 Isaac Lab API / Isaac Lab API on MuJoCo-Warp |
| [RLinf/RLinf](https://github.com/RLinf/RLinf) | 5600 | +9 | 具身 RL 基础设施 / RL infra for embodied AI |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 16074 | +14 | |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 14551 | +14 | |

(无关高增长仓库如 gods-eye-view、RuView 等已忽略。)

### 值得一提的新仓库 / Notable New Repos
- [vernerobotics/v0.5](https://github.com/vernerobotics/v0.5)(8★):Verne V0.5 开放权重 World Action Model,输入三路相机、状态与指令,输出未来 1.07 秒的 32 个 30Hz 末端/夹爪/底盘目标;含模型代码、HF 权重加载器与参考推理循环。✅ 已开源。 / Open-weight WAM with model code and inference loop.
- [flyingbitac/FlowPilot](https://github.com/flyingbitac/FlowPilot)(4★):实时世界-动作建模的无人机敏捷导航(论文 [2608.00635](https://arxiv.org/abs/2608.00635));仅含 Flightmare 闭环仿真与推理代码,不含训练代码与数据。 / Inference + sim only; no training code/data.
- [lasgroup/generalist-improvement](https://github.com/lasgroup/generalist-improvement):见运动控制·RL 条目。
- [Quangvuisme/Acp_supermimic_vibed](https://github.com/Quangvuisme/Acp_supermimic_vibed)、[Robot-Nav/SuperMimic-Agent-WFArm](https://github.com/Robot-Nav/SuperMimic-Agent-WFArm):第三方 SuperMimic 衍生,非官方。

### 新 Release / Releases(窗口内)
- **[huggingface/lerobot v0.7.0](https://github.com/huggingface/lerobot/releases/tag/v0.7.0)**(2026-11-05 17:13 UTC):破坏性变更——Linux 上 torch 默认 CUDA 13(驱动 ≥580.65)、依赖版本上调(transformers 5.22 等);Weights & Biases 换为 Trackio;FSDP1 换为 FSDP2/HSDP(旧 FSDP 检查点无法续训);`--policy.use_peft=true` 现在真正训练 LoRA。新功能:并行训练框架(FSDP2/HSDP、梯度累积、DCP 检查点、EMA、fp16、WSD 调度)、交互式 rollout 会话与远程推理引擎、LanceDB 原生数据集与视频流式读取、GPU 图像变换、评测报告 95% Wilson 区间、新策略(FLUX 3 Action、FineART-VLA、DM05、LaWAM、Wall-OSS-0.5、LingBot-VLA 2.0、Cosmos3、OpenGalaxea G0.5、Long-WAM,π0.5 增加 memory 与训练期 RTC)、统一仿真核心与 NVIDIA RoboLab(Isaac Lab)基准、YAM 机械臂驱动与 Unitree G1-23 + SONIC 远程推理支持。
- **[newton-physics/newton v1.8.0rc1](https://github.com/newton-physics/newton/releases/tag/v1.8.0rc1)**(预发布,2026-11-04 01:21 UTC,超出 24 小时但在 48 小时内):实验性 Steel 铰接刚体求解器 `SolverSteel`(Featherstone + 带耦合库仑摩擦的投影高斯-赛德尔接触求解,支持摩擦面片、闭环/mimic 关节、可选确定性、被动岛休眠、CUDA graph);XPBD/VBD 新增实验性路由肌腱(锚点、销孔、滚轮、绞盘摩擦);`SolverMuJoCo` 新增肌腱等式约束、DC 电机与肌肉执行器导入;核心被动关节弹簧、新的 Kamino 动力学后端、碰撞与建模性能优化。迁移注意:XPBD 刚度调参、Rod 关节、导入的关节弹簧、MuJoCo 运动学根、控制台输出改走 `newton` logger。
- 其他 watchlist 项目(openpi、Isaac Lab、MuJoCo、GR00T 等)窗口内无 release。

---

## 今日趋势 / Today's Trends

1. **人形全身控制从「跟踪位置」走向「跟踪力/接触」与可微世界模型训练。** Ctrl-F 引入力命令,soccerbot 用潜在运动先验,GRASP 改进接触丰富的参考;同时 BlinkMimic、Terrain-Grounded Imagination 延续 SuperMimic 式「在可微世界模型里反传想象 rollout」的路线。
   *Humanoid control moves from pose tracking to force/contact and differentiable-world-model training.* Ctrl-F adds force commands, soccerbot a latent motion prior, GRASP better contact-rich references; BlinkMimic and Terrain-Grounded Imagination continue the SuperMimic-style backprop-through-imagination line.
2. **仿真合成数据替代遥操作。** HALO 在千个程序化住宅中合成视觉-语言-运动数据,零样本真机 91%;Open-HumanScale 则以 5 万小时人类视频走规模化路线。
   *Synthetic data replaces teleoperation.* HALO (91% zero-shot real) vs. Open-HumanScale's 50k-hour human-video scaling.
3. **WAM 去「想象」化:从未来视频生成转向表示蒸馏与几何运动场。** DreamFree 蒸馏视频模型表示以 11Hz 控制,Gnomon4D 用 4D 几何运动场,DreamX 用视频扩散做潜在动作,PDRVLA 在 VLA 中去掉在线视频生成。
   *WAMs drop explicit imagination for representation distillation and geometric motion fields* (DreamFree, Gnomon4D, DreamX, PDRVLA).
4. **递归自我改进(RSI)与智能体式机器人。** PyRUA-REAL、Compounding Physical RSI、VABAR/GaP 等都围绕编码智能体或自演化策略;RL 用于通用策略多任务后训练(lasgroup)。
   *Recursive self-improvement and agentic robotics* (PyRUA-REAL, Compounding Physical RSI, VABAR, generalist RL post-training).
5. **基于 VGGT 的几何基础模型进入 SLAM/导航。** VGGT-SLAM 尺度锚定、UniLoop、EchoNav 均复用几何基础模型。
   *Geometric foundation models (VGGT) enter SLAM and navigation* (VGGT-SLAM scale anchoring, UniLoop, EchoNav).

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
- **"recursive self-improvement" / "RSI"**(arXiv + GitHub)— 今日出现 ≥3 次:[PyRUA-REAL](https://arxiv.org/abs/2611.06768)、[Compounding Physical RSI](https://arxiv.org/abs/2611.06654),HF 另有 PyRUA-DataFarm,radar 有 PyRUA-Lean 仓库。 / A recurring new paradigm for self-improving robot policies/agents (3+ items today).
- **"differentiable world model" + "motion tracking"**(GitHub topic + arXiv)— [BlinkMimic](https://github.com/fuyichen0725/blinkmimic)、[Terrain-Grounded Imagination](https://github.com/leggedrobotics/terrain-grounded-imagination)、多个 SuperMimic 衍生仓库同时出现。 / Backprop through imagined rollouts is spreading across repos.
- **"agentic robotics" / "coding agent robot"**(arXiv)— [VABAR](https://arxiv.org/abs/2611.06881)、[PyRUA-REAL](https://arxiv.org/abs/2611.06768)、HexaShell、GaP(replacement)共 4 篇。 / Coding agents as robot programmers appear in 4 papers.

**建议观察 / Watch**
- **"world action model" 下的 "representation distillation"** — DreamFree、DreamX、PDRVLA 三篇,信号需再看几天。 / Three papers, needs a few more days.

**建议移除/收窄 / Remove or Narrow**
- **"model predictive control robot"** 在 arXiv API 中仅命中 1 条陈旧结果(因短语检索过严);建议改用 `all:MPC AND all:robot` 或依赖 cs.RO 列表。 / Phrase query returned a single stale hit; loosen the query.

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 | 当前状态 | 今日检查结果 | 备注 |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 | signal=false;候选官方仓库为空;`qiayuanl/SuperMimic` 匿名不可访问 | search_hits 多为第三方实现/资源汇总(如 [awesome-supermimic](https://github.com/miao-org/awesome-supermimic) 510★、[Embodied-SuperMimic](https://github.com/FBddcz/Embodied-SuperMimic)),不构成官方开源;BlinkMimic README 把 SuperMimic 作为对比方法。 |

**建议加入监测 / Suggested additions**(均为运动控制·RL 且状态未知):
- **Ctrl-F** — 人形力命令 loco-manipulation,真机 20kg,今日必读。 / Force-commanded humanoid loco-manipulation, a Top Pick.
```json
{"name":"Ctrl-F","title":"Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation","arxiv_id":"2611.05507","search_terms":["Ctrl-F humanoid","forcectrl"],"owners":[],"project_pages":["https://forcectrl.github.io/"],"known_repos":[]}
```
- **soccerbot** — 人形足球潜在运动先验 RL,零样本上 G1。 / Humanoid soccer with latent motion priors, zero-shot on G1.
```json
{"name":"soccerbot","title":"Playing Soccer Like Humans Do: Learning Versatile and Agile Humanoid Soccer via Latent Motion Priors","arxiv_id":"2611.06564","search_terms":["soccerbot humanoid"],"owners":[],"project_pages":[],"known_repos":[]}
```
- **GRASP** — 无需可微仿真器的接触丰富重定向。 / Contact-rich retargeting without differentiable simulators.
```json
{"name":"GRASP","title":"GRASP: Gradient-Guided Sampling for Contact-Rich Physics-Based Motion Retargeting","arxiv_id":"2611.05754","search_terms":["GRASP retargeting"],"owners":[],"project_pages":["https://computationalrobotics.seas.harvard.edu/GRASP/"],"known_repos":[]}
```

**建议移出 / Suggested removals**:无 / None.
