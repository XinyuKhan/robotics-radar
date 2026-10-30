# 机器人/具身智能每日速递 — 2026-10-31 / Robotics & Embodied AI Daily — 2026-10-31

**检查窗口 / Window:** 台北时间 2026-10-30 ~07:40 → 2026-10-31 ~07:40(UTC 10-29 23:40 → 10-30 23:40)。今天是周六,arXiv 周末不发布新列表;本期处理的是 2026-10-30(周五)发布的 cs.RO 列表(提交时间 UTC 10-27 18:21 → 10-29 17:59),该列表在昨日报告抓取时尚未发布,故为首次处理。 / Taipei time, last ~24 h. Today is Saturday (no arXiv listing); this report processes the cs.RO listing announced Fri 30 Oct (submissions 27 Oct 18:21 → 29 Oct 17:59 UTC), which was not yet out when yesterday's report was fetched.

> 本期无监测项开源,故无「🔔 监测项已开源」区块。SuperMimic 的 `signal` 为 false,仅有第三方复现仓库。 / No watchlist item was released today; SuperMimic `signal` = false, only third-party reproductions.

## 来源状态 / Source Status

| 来源 / Source | 状态 / Status |
|---|---|
| arXiv cs.RO 列表 / listing | ✅ 2026-10-30 期:New 109 + Cross 20 + Replacements 60。New + Cross 共 129 条全部逐条分类,87 条判定为相关并入选(含各类别「列名」条目);42 条不相关(医疗/硬件/纯规划/人机交互等)。Replacements 60 条仅按标题扫描,未做「实质更新」核查,其中与主题相关者:[OmniVIC](https://arxiv.org/abs/2510.17150)、[LocoManiLab](https://arxiv.org/abs/2610.30876)、[HumiMimic](https://arxiv.org/abs/2610.36615)、[CALM](https://arxiv.org/abs/2610.18425)、[GlanceWAM](https://arxiv.org/abs/2608.23927)。 / 129 New+Cross entries all classified; 87 selected; Replacements scanned by title only. |
| arXiv API 完整摘要 / full abstracts | ✅ 87/87 篇均取得非空完整摘要;47 篇有 Comments,1 篇有 journal_ref。 / 87/87 full abstracts retrieved; 47 with comments. |
| arXiv API 关键词检索 / keyword search | ✅ 已运行(cs.RO/cs.AI/cs.LG/cs.CV,submittedDate 2026-10-28 22:00 → 10-30 23:40 UTC)。命中数:embodied 17;vision-language-action 12;VLA 10;VLN 1;vision-language navigation 1;humanoid 4;legged locomotion 0;whole-body control 0;model predictive control 2;reinforcement learning robot 0;sim-to-real 2;dexterous manipulation 5;robot foundation model 1;world model 20;world action model 5;video world model 7;spatial intelligence 0;spatial reasoning 4;SLAM 2;visual SLAM 0;LiDAR SLAM 1;gaussian splatting SLAM 0;3D reconstruction 2;motion tracking 1;motion imitation 0。去重后 55 个 ID,其中 19 个不在 cs.RO 列表中(均为 cs.CV/cs.AI/cs.LG 的世界模型/3D 论文,与机器人关系弱,仅在「世界模型」末尾列名)。 / Keyword queries run; 55 unique IDs, 19 outside the cs.RO listing (mostly cs.CV world-model papers, listed by name only). |
| Hugging Face Daily Papers | ✅ 100 条;窗口内机器人相关且带仓库的新条目仅 [OpenFlyV2](https://arxiv.org/abs/2610.39287)(已纳入);其余([PDRVLA](https://arxiv.org/abs/2610.37381)、[RynnWorld-Latent](https://arxiv.org/abs/2610.36791)、[JAM](https://arxiv.org/abs/2610.37219)、[Hy-Nomas](https://arxiv.org/abs/2610.36729) 等)已在前几期报告涉及。 |
| GitHub radar(`data/latest.json`,date_taipei = 2026-10-31) | ✅ 已更新;new_repos 150 条、star_growth_top 60 条、watchlist_releases 0 项、oss_watch 1 项(无错误)。star 基线 2026-10-29。 |

## 今日必读 / Top Picks

1. **[METATRON](https://arxiv.org/abs/2610.38027)**(NVIDIA;运动控制·RL;❓ 未知)— 冻结的生成式人形基础策略 + 可编程「技能」层,由 coding agent 用代码合成新技能,真机 Unitree G1 单一检查点完成行走、恢复、取物、坐椅。 / A frozen generative humanoid policy plus a programmable skill layer that coding agents extend through code; one checkpoint does walking, recovery, pickup and sitting on a real G1.
2. **[FORGE](https://arxiv.org/abs/2610.37974)**(Caltech;运动控制·RL;❓ 未知)— 降阶模型(ROM)在线参考生成 + 全身跟踪的两阶段学习框架,G1 上单一参考策略 + 单一跟踪策略覆盖 −2.0~2.8 m/s 速度及单腿跳。 / Two-stage ROM reference generation + whole-body tracking; one unified pair of policies on G1 covers −2.0–2.8 m/s and one-legged hopping.
3. **[Catch It All!](https://arxiv.org/abs/2610.39044)**(运动控制·RL;❓ 未知)— 单个第一视角相机、零样本部署到 Unitree G1,对 9 种未见物体完成上手/下手接球,含腕部力矩低至 5 Nm 的安全课程。 / Zero-shot sim-to-real catching on G1 with one egocentric camera on 9 unseen objects.
4. **[SONIC-K1](https://arxiv.org/abs/2610.39327)**(运动控制·RL;✅ 已开源)— 首个面向 Booster K1 的开放权重全身运动跟踪器,代码与权重均已公开,可在单卡上复现。 / First open-weights whole-body motion tracker for Booster K1; code and weights public.
5. **[ELEVATE](https://arxiv.org/abs/2610.38388)**(运动控制·RL;❓ 未知)— coding agent 从任务失败中自动构造 RL 问题并获取四足操作新控制器,真机 18/20、16/20 成功。 / Coding agent turns task failures into RL problems and acquires new quadruped loco-manipulation controllers; 18/20 and 16/20 on hardware.

## 运动控制·RL / Motion Control · RL

共 22 条,全部展开(按重要性排序)。 / 22 items, all expanded.

### [METATRON: A Promptable Whole-Body Execution Layer for Humanoids](https://arxiv.org/abs/2610.38027) — NVIDIA(Chen Tessler, Yifeng Jiang, Alec Otto, Yi Shi 等)
🏷️ 交叉方向 / Also: 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models(coding agent)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://research.nvidia.com/labs/par/projects/metatron/);项目页未提供代码仓库或开源承诺,仅有浏览器内交互演示([demo](https://nvlabs.github.io/ProtoMotions/demos/metatron/))
- 🇨🇳 人形控制器通常需要针对每个任务单独训练,尽管平衡与全身协调是共通需求。METATRON 提出可提示(promptable)的全身执行层:生成式基础策略接收由限时的身体部位目标、速度指令和风格线索组成的「提示」,输出与之一致的多样化全身动作;训练数据包括动捕、合成恢复轨迹与重定向的场景交互动作,训练后策略冻结。任务意图由有状态的「技能」程序(普通代码)逐控制步生成提示,并由 coding agent 分析运动数据后拟合紧凑规则,无需任务专属策略训练。真机 Unitree G1 上同一冻结检查点支持行走、恢复、遥操作取物和坐到家具上;对比评估显示其到达成功率和抗推力鲁棒性高于所测的参考跟踪流水线,同一配方还在仿真角色上产生攀爬与杂技动作。
- 🇬🇧 Humanoid controllers usually need task-specific training although they share balance and whole-body coordination needs. Metatron is a promptable execution layer: a generative base policy takes prompts combining timed body-part targets, velocity commands and style cues and produces consistent whole-body motion, trained on mocap, synthetic recovery trajectories and retargeted scene-interaction motions, then frozen. Stateful skills written as ordinary code emit prompts at each control step and are refined by coding agents that fit compact rules to motion data, without task-specific policy training. On a physical Unitree G1 one frozen checkpoint supports walking, recovery, teleoperated pickup and sitting on furniture, with higher reaching success and push robustness than the tested reference-tracking pipelines; the same recipe yields climbing and acrobatics on a simulated character.

### [FORGE: Feasible Online Reduced-Order Reference Generation and Whole-Body Execution for Agile Humanoid Locomotion](https://arxiv.org/abs/2610.37974) — Caltech(Adrian B. Ghansah, Yujin An, Jeeseop Kim, Soon-Jo Chung)
🏷️ 交叉方向 / Also: 运动控制·传统(降阶模型 / reduced-order model)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接(Comments:Humanoids 2026 接收)
- 🇨🇳 要让人形机器人覆盖宽广的指令空间与多种步态,单一端到端策略难以同时保证动力学一致性。FORGE 采用两阶段学习:第一阶段用单刚体动力学结合完整人形运动学,训练指令条件的全身参考生成器;第二阶段把冻结的 ROM 策略在线滚动生成参考,用于在全阶动力学上训练全身跟踪策略。在降阶空间学习运动-动力学一致的参考,使单一统一框架即可覆盖多种移动策略。在 Unitree G1 上,仅用一个统一参考策略和一个全身跟踪策略,实现 −2.0 至 2.8 m/s 纵向速度、横向最高 ±1.0 m/s、角速度最高 ±3.0 rad/s、单腿跳以及指令间的连续切换。
- 🇬🇧 Covering a wide command space and several gaits with one end-to-end policy struggles to stay kino-dynamically consistent. FORGE is a two-stage framework: first a command-conditioned whole-body reference generator is trained using single-rigid-body dynamics with full humanoid kinematics; then the frozen ROM policy is rolled out online to generate references for training a whole-body tracking policy on the full-order model. Learning references in the reduced space lets one framework cover multiple locomotion strategies. On a Unitree G1, a single reference policy and a single tracking policy achieve −2.0 to 2.8 m/s longitudinal speed, up to ±1.0 m/s lateral, up to ±3.0 rad/s yaw, one-legged hopping and smooth transitions between commands.

### [Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand](https://arxiv.org/abs/2610.39044) — (Arth Shukla, Kehlani Fay, Huaze Liu, Darin Djapri 等)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 均无代码链接或承诺
- 🇨🇳 抓取任意物体需要对新投射物泛化,并在含噪视觉下实时适应不可预测的接触动力学。该工作给出面向人形机器人的 sim-to-real 接球框架,仅用一个第一视角相机,支持下手与上手接球;通过精心设计的抓取奖励学习能随物体位姿与形状实时调整的抓取,并提供「安全感知课程」,使高频动作可在硬件极限(腕部力矩低至 5 Nm)附近安全执行。零样本部署到 Unitree G1,对 9 种训练中未见的物体(低回弹毛绒玩具、半可变形玩具、薯片袋、高回弹刚弹性物体等)成功完成上手和下手接球。
- 🇬🇧 Catching arbitrary objects needs generalization to novel projectiles and real-time adaptation to unpredictable contact under noisy vision. This sim-to-real framework for humanoids uses a single egocentric camera for underhand and overhand catches; grasps that adapt to object pose and shape are learned via careful grasp-reward design, and safety-aware curricula enable high-frequency actions near hardware limits (wrist torque limits as low as 5 Nm). Deployed zero-shot on a Unitree G1, it catches 9 unseen objects, including low-rebound plushes, semi-deformable toys, chip bags and high-rebound rigid-elastic objects.

### [SONIC-K1: Porting a Universal Humanoid Motion Tracker to a Small Humanoid on a Single GPU](https://arxiv.org/abs/2610.39327) — (Kyrylo Kolesnichenko, Jong-Hoon Kim)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Kyk0/sonic-k1);[权重](https://huggingface.co/Kyry10/sonic-k1) 与 [K1 USD 数据集](https://huggingface.co/datasets/Kyry10/booster-k1-usd) 见[项目页](https://kyry.me/sonic-k1);仓库已用匿名 git ls-remote 验证存在
- 🇨🇳 通用人形运动跟踪器 SONIC 此前并无面向较小人形 Booster K1 的开放版本。作者将 SONIC 框架适配到 K1,在单张共享 GPU 上从零训练,算力只占 SONIC 报告值的一小部分。MuJoCo 仿真中,策略能跟踪几乎所有留出的动作片段,并在外部基准上按 SONIC 的成功标准表现良好;真机 K1 上可跟踪上半身和慢速动作,但迈步和转向仍不可靠,仿真显示对动作延迟敏感。作者指出定量的真机评估是下一步重点;代码、策略权重和评估工具均已公开。
- 🇬🇧 No open version of the universal humanoid tracker SONIC existed for the smaller Booster K1. The authors adapt SONIC to the K1, training from scratch on a single shared GPU with a small fraction of SONIC's reported compute. In MuJoCo it tracks nearly all held-out clips and performs well on external benchmarks under SONIC's success criterion; on the real K1 it tracks upper-body and slow motions, while stepping and turning remain unreliable and simulation shows sensitivity to action latency. Quantitative hardware evaluation is named as the main next step; code, weights and evaluation tools are public.

### [ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation](https://arxiv.org/abs/2610.38388) — (Shiqi Liu, Radu Corcodel, Ding Zhao)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(agentic)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://agentic-quad-elevate.github.io/public/)仅抓取到标题,未见代码链接
- 🇨🇳 四足操作机器人可通过全身交互扩展工作空间,但任务规划智能体受限于已有控制器。ELEVATE 利用任务程序反复修正中的持续失败来识别缺失的全身控制能力:当失败提示缺少物理能力时,coding agent 构造并迭代细化一个 RL 问题(行为专属奖励、课程、终止条件),通过验证的控制器加入能力库并与既有控制器组合后重试。从单一预训练 loco-manipulation 控制器出发,在七个仿真任务序列中自主获得「墙面支撑抬升」「支撑操作」「墙面下降」等控制器;在初始控制器工作空间之外的五个任务上平均成功率为 98.4%–100%(五次独立运行),固定控制器库的 coding-agent 基线均无法完成。合成的任务程序与新控制器无需真机训练即可迁移到实体四足操作机器人,货架取物 18/20、地面到货架放置 16/20。
- 🇬🇧 Quadrupedal manipulators can extend their workspace via whole-body interaction, but task-planning agents are limited by the controllers they have. ELEVATE uses persistent failures during task-program refinement to detect missing whole-body capabilities; a coding agent then formulates and iteratively refines an RL problem (behavior-specific rewards, curricula, termination conditions), and validated controllers join a capability library for composition and retry. Starting from one pretrained loco-manipulation controller, it autonomously acquires controllers for wall-supported elevation, supported manipulation and wall descent over seven simulated tasks; on the five tasks beyond the initial workspace it reaches 98.4%–100% mean success over five runs while fixed-library coding-agent baselines fail. Programs and controllers transfer to a physical quadruped manipulator without real-robot training, with 18/20 rack-retrieval and 16/20 floor-to-rack successes.

### [Humanoid Dodgeball: Learning Fast Dynamic Obstacle Avoidance Motions for Humanoids](https://arxiv.org/abs/2610.40003) — (Aoqian Zhang, Chunzheng Wang, Haoran Chen, Annan Tang 等)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接
- 🇨🇳 人形机器人要在动态场景中安全运行,必须在保持稳定与物理可行的前提下快速躲避高速障碍,而高维动力学、反应式避障、动作自然性与控制鲁棒性难以同时兼顾。该工作提出强化学习框架 Humanoid Dodgeball:用威胁感知的奖励塑形驱动高动态的全身闪避动作,并用多个方向专属的对抗运动先验(AMP)把行为正则到稳定、多样且类人的动作上。大量仿真与硬件实验表明,在不同障碍速度与发射距离下避障性能显著提升,同时保持鲁棒且物理合理的动作;预印本摘要未给出具体数值。
- 🇬🇧 Humanoids must dodge fast-moving obstacles while staying stable and physically feasible, which is hard to balance with reactive avoidance, motion naturalness and robustness. Humanoid Dodgeball is an RL framework that uses threat-aware reward shaping to drive highly dynamic whole-body evasive maneuvers, with multiple direction-specific adversarial motion priors regularizing behavior toward stable, diverse, human-like motion. Simulation and hardware experiments show substantially improved avoidance across obstacle speeds and launch distances while keeping motions robust and plausible; the preprint abstract gives no quantitative numbers.

### [Echo: Scaling Visual Reinforcement Learning with Off-policy Experience](https://arxiv.org/abs/2610.37865) — (Gagan Khandate)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments(Report. 16 pages)无代码链接
- 🇨🇳 GPU 加速仿真中扩展视觉 RL 受渲染和视觉策略推理开销限制,常用的师生蒸馏又带来模仿差距。Echo 是单阶段 off-policy RL 框架:通过「逆向蒸馏」让基于状态的辅助策略模仿不断演化的视觉策略,以低成本采集不渲染的经验,再经共享的特权 critic 做 off-policy 价值学习以直接改进视觉策略。以 FastTD3 实例化,在 Genesis 的三项视觉控制(运动)任务和两项灵巧手任务上,相对基线达到参考回报的时间平均减少 60%(三项运动任务)和 56%(两项手部任务),峰值平均回报分别提升 62% 和 12%;这是一项初步研究。
- 🇬🇧 Scaling visual RL in GPU simulation is limited by rendering and visual-inference cost, and two-stage teacher–student distillation introduces an imitation gap. Echo is a single-stage off-policy framework: via "inverse distillation" a state-based auxiliary policy imitates the evolving visual policy and collects cheap unrendered experience, which feeds off-policy value learning through a shared privileged critic. Instantiated with FastTD3 on three visual control tasks and two dexterous manipulation tasks in Genesis, it cuts time to reference returns by 60% on average across the locomotion tasks and 56% across the hand tasks, and raises peak mean returns by 62% and 12%; this is a preliminary study.

### [Force-Driven Hook Disassembly via Constraint-Aware Object-Centric Reinforcement Learning](https://arxiv.org/abs/2610.38513) — (Nadeen Elhadad, Takuya Kiyokawa, Kensuke Harada)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接
- 🇨🇳 报废产品自动拆解中,卡扣连接的方向多变、受力会形变且几何被遮挡,仅靠视觉难以确定可行的无损拆卸方向。该工作提出约束感知强化学习框架,从接触力在线推断可行抽出方向:策略在与机器人无关、以物体为中心的简化插销-孔仿真中训练并零样本部署到真机,又与粒子滤波信念耦合,提供时间积分的方向信息并减少冗余探索。四个真实任务(从插销孔到报废空调内部螺旋桨与前盖)成功率分别为 100%、100%、90%、75%,所有任务路径效率最高;空调盖上成功率由无信念策略的 45% 提升到 75%。
- 🇬🇧 Hook-type connections in end-of-life products have variable orientation, deform under load and hide their geometry, so vision alone cannot find a feasible non-destructive disassembly direction. This work proposes a constraint-aware RL framework that infers feasible extraction directions online from contact forces; the policy is trained in a robot-agnostic object-centric simulation of a simplified peg-in-hole pair and deployed zero-shot, coupled with a particle-filter belief that integrates noisy forces over time and cuts redundant exploration. On four real tasks it achieves 100%, 100%, 90% and 75% success with the best path efficiency on every task, and raises success on the air-conditioner cover from 45% to 75% versus a policy without the belief.

### [Learning Event-based Obstacle Avoidance via Differentiable Simulation](https://arxiv.org/abs/2610.38967) — RPG(Chenlu Shou, Yunfan Ren, Jiaxu Xing, Davide Scaramuzza 等)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接
- 🇨🇳 事件相机延迟低、动态范围高、几乎无运动模糊,但用于闭环控制仍困难:级联「深度估计 + 控制」会累积误差,端到端方法又需昂贵的离线预训练。该工作实现基于 CUDA 的事件仿真器,可在训练回路中并行渲染事件,并接入可微仿真管线,使梯度能直接穿过可微物理模型反传,提高样本效率,从而训练从事件帧直接到控制指令的端到端策略,无需中间深度估计。四旋翼零样本真机部署在有里程计和无里程计两种设置下均稳健避障,包括传统相机易失效的低光条件;预印本摘要未给出具体百分比。
- 🇬🇧 Event cameras offer low latency, high dynamic range and little motion blur, yet closed-loop control with them is hard: cascaded depth-then-control pipelines propagate errors and end-to-end methods need costly offline pretraining. The authors build a CUDA event simulator that renders events inside the training loop and integrate it with a differentiable-simulation pipeline so gradients flow through the differentiable physics model, improving sample efficiency and training an end-to-end policy from event frames to control commands without depth estimation. Zero-shot real quadrotor deployment achieves robust avoidance both with and without odometry, including low light where conventional cameras fail; the abstract gives no quantitative figures.

### [Cross-Controller Transfer via In-Context Behavior Adaptation](https://arxiv.org/abs/2610.39280) — Stanford(Jonathan Yang, Chelsea Finn, Dorsa Sadigh 等)
🏷️ 交叉方向 / Also: 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://controller-transfer.github.io)已给出,代码链接未核实
- 🇨🇳 通用机器人策略假定每个机器人只有一种控制器,但不同控制器会给同一动作赋予不同物理含义,限制跨本体、跨控制器的数据迁移。该工作研究如何在不让冲突的动作解释相互干扰的前提下迁移数据,覆盖六种控制器类型及控制增益/柔顺度变化:用一组「指令动作—实际运动」示例编码控制器下的行为交互,由 Transformer 上下文编码器汇总,使单一策略在上下文中自适应。真机实验中平均成功率比朴素数据混合高 33 个百分点,未见控制器模式达 50%、未见控制增益达 52%;在 USB 插入和表面擦拭等接触丰富任务上,策略不仅调整动作也调整策略。
- 🇬🇧 Generalist policies usually assume one controller per robot, but controllers give the same action different physical meanings, limiting transfer across embodiments and controllers. The authors encode a controller's behavior through examples of commanded actions and resulting motions summarized by a transformer context encoder, letting one policy adapt in context across six controller types and varied gains/compliance. In real-world tests it improves average success by 33 percentage points over naive pooling, reaching 50% on unseen controller modes and 52% on unseen gains, and on contact-rich tasks such as USB insertion and wiping it adapts both actions and strategy.

### [LLM-guided Planar Loco-Manipulation for Quadruped Robots](https://arxiv.org/abs/2610.40248) — (Georges Jetti, Michael Khayyat, Jean-Pierre Sleiman, Stefano Arrigoni)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(LLM 规划)
开源状态 / Code: ❓ 未知 / Unknown — 摘要给出匿名[项目页](https://anonymousprojects-dev.github.io/LLM-guided-LocoManipulation-Quadrupeds/),代码链接未核实
- 🇨🇳 在有可移动障碍的杂乱环境中,到达目标可能需要物理交互;经典方法依赖几何规则,学习方法常把决策空间限制为低维运动指令。该工作让语言条件任务规划器(LoRA 在合成数据上微调)把自然语言任务和结构化场景表示映射为变长参数化动作序列,由底层 RL 策略执行,联合选择技能、目标物体与几何目标。规划器在交互式导航任务上优于经典规划器和提示式前沿模型;底层端到端全身平面推动策略仿真成功率 93.3%(分层基线 83.5%)且完成时间缩短超 60%。硬件上分层方案技能组合正确 44/45 次,端到端成功 34/45 次。
- 🇬🇧 In cluttered scenes with movable obstacles, reaching the goal may require physical interaction; classical solutions rely on geometric rules while learned ones often restrict decisions to low-dimensional commands. A LoRA-fine-tuned language-conditioned planner maps natural-language tasks and structured scenes to variable-length parameterized action sequences executed by low-level RL policies, jointly choosing skill, object and geometric target. It outperforms a classical planner and a prompted frontier model; the end-to-end whole-body planar pushing policy reaches 93.3% in simulation versus 83.5% for a hierarchical baseline with over 60% shorter completion time, and on hardware the hierarchy gives correct skill composition in 44/45 trials and end-to-end success in 34/45.

### [Event2Reward: Learning Robotic Rewards from Progress Relations](https://arxiv.org/abs/2610.39212) — (Junnan Nie, Zitian Fan, Jiachen Zhang, Junyi Lao 等)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments(44 pages)无代码链接
- 🇨🇳 用归一化演示时间作进度标签构造 RL 稠密奖励时,隐含进度单调递增的假设,而探索中进度会停滞甚至倒退,模型可能把倒退当作进展。Event2Reward 利用停滞、倒退、恢复建立的局部相对进度关系,与归一化时间标签锚定的绝对进度共同监督,预测值作为奖励塑形势函数;并从约 10 万条真机执行记录构建含成功/次优/失败的事件标注数据集,无需逐帧进度标签。LIBERO 四个套件 40 个任务上平均策略成功率比仅稀疏奖励基线高 18.16 个百分点;真机 30 分钟训练后三项精密插入任务平均成功率 60.0%、三项物体操作任务 90.0%,分别高出稀疏奖励基线 36.7 和 23.3 个百分点。
- 🇬🇧 Dense RL rewards built from normalized demonstration time assume monotonic progress, yet exploration stalls or regresses and such models may reward regressions. Event2Reward uses relative progress relations from stalls, regressions and recoveries together with absolute progress anchored by normalized time, and uses predictions as shaping potentials; it curates an event-annotated dataset from ~100K real-robot records without framewise labels. Across 40 tasks in four LIBERO suites it improves average success by 18.16 points over a sparse-reward baseline; on real robots, after 30 minutes of training, success reaches 60.0% on three insertion tasks and 90.0% on three manipulation tasks, 36.7 and 23.3 points above the sparse baseline.

### [CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization](https://arxiv.org/abs/2610.38357) — (Zhiyuan Xiang, Xiang Deng, Wanjie Tao, Xu Chen)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments(NeurIPS 2026 接收)无代码链接
- 🇨🇳 用 VQ-VAE 把连续动作离散成技能的范式存在量化误差导致技能先验次优,而直接用 RL 精调又面临编码器更新不稳和重要性采样粒度难题。CSO 是两阶段后训练框架:先用拒绝采样监督微调让「观测→技能」映射对齐成功在线轨迹分布,再冻结观测编码器,用 Skills Policy Optimization 对每个完整技能计算独立的裁剪重要性比,实现稳定高效更新。轻量 QueST 式策略上,LIBERO 总成功率由 80.1% 提升到 97.5%,RoboTwin2.0 亦有提升,五个真实单臂任务成功率 61.0%;并与 FAST、离散 BEAST、固定缓冲 IQL 对比验证。
- 🇬🇧 Discretizing actions into skills with VQ-VAE suffers quantization errors that give a suboptimal skill prior, and direct RL refinement faces unstable encoder updates and an importance-sampling granularity dilemma. CSO is a two-stage post-training framework: rejection-sampling SFT aligns the observation-to-skill mapping with successful online trajectories, then with the encoder frozen, Skills Policy Optimization computes an independent clipped importance ratio per complete skill. With a lightweight QueST-style policy it raises LIBERO success from 80.1% to 97.5%, improves RoboTwin2.0, and reaches 61.0% on five physical single-arm tasks, with comparisons to FAST, discrete BEAST and fixed-buffer IQL.

### [Learning from Relative Action Credit for Escaping Local Minima](https://arxiv.org/abs/2610.38034) — IIT(Giovanni Minelli, Giulio Turrisi, Lorenzo Amatucci, Victor Barasuol)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 在长时域、接触丰富的操作任务上,PPO 常常停滞:状态价值 critic 只依据回合结果判断进展,策略收敛到部分解后所有结果相同,没有动作能证明自己更优。该工作给 PPO 增加动作条件价值 critic,可在同一状态把已执行动作与采样的替代动作比较,补充学习信号;结合 GAE 与对探索噪声的上界。结果显示扩展后的算法能逃离平台期并完成精确插销,而探索设置相同的 PPO 在同等训练预算内失败;预印本摘要未给出更多数值。
- 🇬🇧 On long-horizon, contact-rich tasks PPO stalls: a state-value critic judges progress only by episode outcomes, so once the policy converges to a partial solution all outcomes coincide and no action can prove better. The paper extends PPO with an action-conditioned value critic that compares the executed action with alternatives sampled at the same state, combined with GAE and a bound on exploration noise. The extended algorithm escapes the plateau and completes precise peg insertion within a budget where PPO with identical exploration fails; the abstract gives no further numbers.

### [Is It the Curriculum or Just the Easy Start? Benchmarking Unsupervised Environment Design on Quadrupeds](https://arxiv.org/abs/2610.40364) — (Jakub Gilewicz, Dominik Galus, Piotr Wojdas 等)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(基准)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Solvro/ml-wojtek-ued);含关卡空间与评估套件,已用 git ls-remote 验证存在
- 🇨🇳 无监督环境设计(UED)方法多在 2D 迷宫等简单环境比较,足式机器人的地形课程则多为手工设计且基线很少。该工作给出基准:在 MuJoCo MJX 的五种 3D 四足机器人(W01-TEK、Go1、Go2、Barkour vB、Spot)上,用统一协议、相同 PPO 学生和匹配的环境步数运行十四种 UED/域随机化/机器人课程,地形关卡由八个可解释参数构成,报告 IQM、分层自助置信区间等。结论:没有任何方法在所有机器人与关卡集上都位居第一梯队;来自足式机器人实践的「成功驱动地形课程」最常进入第一梯队,均匀域随机化从未进入;三个机器人上,分布内随机关卡的领先者并非留出地形的领先者。
- 🇬🇧 UED methods are mostly compared on 2D mazes and grid worlds while legged terrain curricula are hand-designed with few baselines. This benchmark runs fourteen UED, domain-randomisation and robotics curricula under one protocol on five 3D quadrupeds in MuJoCo MJX (W01-TEK, Go1, Go2, Barkour vB, Spot) with the same PPO student and matched step budgets, with levels given by eight interpretable terrain parameters and IQM/bootstrap statistics. No method is in the top group on every robot and level set; the success-driven terrain curriculum from legged practice appears in a top group most often, uniform domain randomisation in none, and on three robots the leader on in-distribution random levels is not the leader on held-out terrain.

### [Explore Where It Matters: Targeted Exploration for Efficient Rover Adaptation](https://arxiv.org/abs/2610.38657) — (Jacob Levy, Arthur Bouton, Tristan D. Hassler, Hari Nayar 等)
🏷️ 交叉方向 / Also: 世界模型 / World Model;运动控制·传统(MPC)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://terra-explore.github.io)已给出,代码链接未核实(Comments:CoRL 2026)
- 🇨🇳 行星车在陡峭可变形地形上会遇到滑移与沉陷,仿真无法覆盖所有效应,需要部署时适应,但试错余地很小。TERRA 在线适应框架用奖励加权预测损失调整仿真训练的世界模型,并训练损失预测器估计未来与性能相关误差的出现位置,用该信号在 MPC 中引导探索。仿真中在严重分布外预训练条件下,五次试验内达到约 90% 爬坡成功率,在奖励、完成时间和首次成功能耗上优于探索基线;ERNEST 行星车在火星模拟土壤斜坡上,三到五次真机试验内恢复协调的主动悬架运动。
- 🇬🇧 Planetary rovers on steep deformable terrain face slip and sinkage that simulation cannot fully capture, so deployment-time adaptation is needed with little trial-and-error budget. TERRA adapts a simulation-trained world model with a reward-weighted prediction loss and trains a loss predictor to estimate where performance-relevant errors will occur, using it to guide exploration during MPC. In simulation it reaches ~90% slope-climbing success within five trials under severe out-of-distribution pretraining, beating exploration baselines in reward, completion time and energy to first success; on the ERNEST rover it recovers coordinated active-suspension locomotion on a Mars-simulant slope within three to five real trials.

### [SimRetract: Zero-Shot Sim-to-Real Robotic Assistance for Retractor Take-Over in Open Surgery](https://arxiv.org/abs/2610.38234) — (Xucheng Wang, Zhizhou Yang, Sung Eun Kim, Romain Hardy 等)
开源状态 / Code: ✅ 已开源 / Released — [匿名评审仓库](https://anonymous.4open.science/r/simretract-58D2);匿名评审镜像,未能用 git ls-remote 验证,待正式仓库
- 🇨🇳 开放手术中的拉钩接手任务若用真实示教做模仿学习,成本高且环境变化时性能下降。SimRetract 仅用仿真示教生成面向迁移设计的数据:策略观察被遮罩的器械图像和抓取几何,学习从偏离名义状态中恢复,并为执行漂移留出余量,零样本部署。在 50 次外科医生定义的体模递送中抓取成功 90%,交接时保持牵拉 78%;跨十种策略配置、1200 次仿真与真实试验定位 sim-to-real 差距,真机上仅去掉器械遮罩就使抓取降到 22%、保持降到 12%。
- 🇬🇧 Imitation from real demonstrations for open-surgery retractor take-over is costly and degrades under environment changes. SimRetract generates simulated demonstrations designed for transfer: the policy sees masked instrument images and grasp geometry, learns to recover from off-nominal states and acts with margin for execution drift, deployed zero-shot. It grasps the retractor in 90% of 50 surgeon-defined phantom presentations and preserves retraction at handoff in 78%; across ten configurations and 1,200 trials, removing the instrument mask alone drops real-robot performance to 22% grasped and 12% held.

### [Gaussian Distillation of Flow Policies](https://arxiv.org/abs/2610.40271) — (Youssef Saied, Ziyad Sheebaelhamd, Claire Vernade, François Fleuret)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 流策略是最强的机器人控制器之一,擅长建模多模态动作分布,但推理代价较高。作者分析发现所研究流策略的连续动作分布可很好地用高斯近似,据此提出 Gaussian Action Readout(GAR):用高斯读出层替换流策略最终层,仅在 0.02% 的可用状态上训练,其余网络冻结。它一次动作网络前向即可采样,给出闭式似然,在推理速度最高提升两倍的情况下达到接近教师的任务成功率。
- 🇬🇧 Flow policies are among the strongest robot controllers and model multimodal action distributions but are costly at inference. The authors find the studied policies' continuous-action distributions are well approximated by Gaussians and propose the Gaussian Action Readout (GAR), replacing the final layer with a Gaussian readout trained on just 0.02% of eligible states while freezing the rest. It samples with one action-network pass, gives closed-form likelihoods, and achieves near-teacher task success at up to twice the inference speed.

### [Learning Safe Flow Matching Robot Policies from Binary Feasibility Oracles](https://arxiv.org/abs/2610.40075) — (Jianming Ma, Rongjun Jin, Yizhi Chen, Yue Gao)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 机器人基础模型常用流匹配生成动作,但无法保证满足关节限位、避碰等物理约束,尤其当可行集只能通过黑箱二值可行性预言机访问时。作者提出「预言机引导的可微保护层」:前向用二值可行性查询修正不安全更新,反向提取局部边界信息提供约束感知的学习信号,并与离散时间流匹配结合,训练与推理使用同一保护层,实现前后向一致的策略学习,无需显式或可微约束模型。障碍感知操作实验中达到 100% 约束满足同时保持任务性能。
- 🇬🇧 Flow-based robot foundation models generate actions without guarantees of joint limits or collision avoidance, especially when the feasible set is only reachable through a black-box binary feasibility oracle. The authors propose an oracle-guided differentiable safeguard: binary queries correct unsafe updates in the forward pass while local boundary information gives constraint-aware learning signals in the backward pass, used in both training and inference with discrete-time flow matching and no explicit constraint model. Obstacle-aware manipulation experiments show 100% constraint satisfaction while preserving task performance.

### [AcrossDEX 1.0: From Human Motion Pretraining to Bimanual Dexterous Manipulation across Hand Embodiments](https://arxiv.org/abs/2610.40210) — (Xiaoyu Yang, Nan Wu)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(人类动作预训练)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接
- 🇨🇳 双手灵巧操作需要手腕运动、指尖接触和物体运动的连续协调;利用人类视频需对齐人体姿态与机器人指令并考虑本体差异。AcrossDEX 1.0 连接人类动作预训练(HOT3D Aria 上由五帧图像和三十个手部状态预测一秒双手运动)、仿真专家学习、机器人示教采集与视觉闭环执行;机器人适配保留视觉编码器、时序骨干和腕部参数,共享腕部表示、分离手指场并用有效性掩码同时支持六通道 Inspire 手和十六关节 Allegro 手。直接回归在开盖并归位上成功率 40.6%,Inspire 重定向 100.0%,Allegro 93.3%;流匹配在 Allegro 重定向上 90.0%;用上一计划约束重规划可改善生成式策略的连续执行。
- 🇬🇧 Bimanual dexterous manipulation needs continuous coordination of wrist motion, finger contact and object motion, and using human video requires aligning human poses to robot commands across embodiments. AcrossDEX 1.0 links human motion pretraining (predicting one second of bimanual motion from five images and thirty hand states on HOT3D Aria), simulation expert learning, robot demonstration collection and visual closed-loop execution; adaptation keeps the encoder, temporal backbone and wrist parameters, with shared wrist representations, separate finger fields and validity masks for six-channel Inspire and sixteen-joint Allegro hands. Direct regression reaches 40.6% on lid opening-and-return, 100.0% on Inspire reorientation and 93.3% on Allegro; flow matching reaches 90.0% on Allegro, and constraining replanning with the previous plan improves continuous execution of generative policies.

### [Kinematic-Tactile Aligned Dexterous Retargeting with Contact Wrench Space Alignment](https://arxiv.org/abs/2610.39582) — (Xinyuan He, Ziheng Xu, Yueyuan Chen, Yufan Ye 等)
🏷️ 交叉方向 / Also: 运动控制·传统(优化 / optimization)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments(8 pages)无代码链接
- 🇨🇳 现有重定向方法主要迁移人手运动学,触觉信息很少在本体间保留。该工作提出分层三阶段框架,以物体中心的接触力旋量空间(contact wrench space)作为触觉对齐的物理表示:先对齐手部运动学与接触几何,再由触觉力和接触几何构建人类旋量支撑轮廓,随后优化机器人指尖力目标以覆盖该支撑并转为关节位置修正,得到可直接回放的轨迹。仿真和三种倒水条件的真机实验中,回放成功率 96.7%,旋量迁移保真度高于代表性重定向基线。
- 🇬🇧 Existing retargeting mostly transfers human kinematics and rarely preserves tactile information across embodiments. This hierarchical three-stage framework uses object-centric contact wrench space as the physical representation: it aligns hand kinematics and contact geometry, builds a human wrench support profile from tactile forces and contact geometry, then optimizes robot fingertip force targets to cover that support and converts them to joint corrections, yielding directly replayable trajectories. In simulation and real pouring experiments under three conditions it achieves a 96.7% replay success rate and higher wrench-transfer fidelity than representative baselines.

### [An Empirical Study of Wrist-Target Construction and Joint-Angle Limits in Humanoid Arm Retargeting](https://arxiv.org/abs/2610.37801) — (MinJun Chang)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接(Comments:提交至 ICRA 2027)
- 🇨🇳 动作重定向把人体动作映射到机器人关节运动,但「期望手腕位置」的构造方式会影响计算出的手臂关节角是否触及限位。该实证研究在 Unitree H1-2 上比较「重建目标」(由示教手臂方向与机器人连杆长度构成,肩-腕距离依赖示教的连杆夹角)和「归一化到可达范围的目标」(保持方向、重缩放距离)。前伸扫描中重建目标在 20 次重复中有 10 次使关节角到达边界,归一化目标为 0 次;25 段记录中到达边界的计数在运动臂上为 8 对 6、支撑臂上为 14 对 5;硬件回放中 16 条方向匹配记录有 12 条关节被命令到边界,归一化记录为 0 条,且这些帧的跟踪误差和执行力矩更高。
- 🇬🇧 Motion retargeting maps human movement to robot joint motion, but how the desired wrist position is constructed affects whether computed arm joint angles hit limits. This empirical study on a Unitree H1-2 compares a reconstructed target (built from demonstrated arm directions and robot segment lengths) with a reach-normalized target (same direction, rescaled distance). In a forward-reach sweep the reconstructed target puts a joint at a bound in 10 of 20 repetitions versus none for the normalized one; over 25 recordings counts are 8 vs 6 (reaching arm) and 14 vs 5 (supporting arm); in hardware replay a joint is commanded to a bound in 12 of 16 direction-matching records and none of 16 normalized records, with higher tracking error and torque at those frames.

## 运动控制·传统 / Motion Control · Classical

共 7 条(含 [TACOS](https://arxiv.org/abs/2610.37806),见下),全部展开。 / 7 items, all expanded.

### [TACOS: Terrain-Aware COntact Supervision for Visual Footstep Planning](https://arxiv.org/abs/2610.37806) — Norlab, Université Laval(Jean-Michel Fortin, William Larrivée-Hardy, Gabriel Jeanson, Olivier Gamache 等)
🏷️ 交叉方向 / Also: 空间智能与 SLAM / Spatial Intelligence & SLAM(因子图状态估计 / factor-graph state estimation)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/norlab-ulaval/TACOS);已用 git ls-remote 验证存在(Comments:提交 ICRA 2027)
- 🇨🇳 足式机器人可通过自监督学习获得「踏步前预判地面反应」的能力,但监督信号常凭直觉选择且其影响鲜被检验。TACOS 基于足式状态估计因子图的残差给出一致的「落脚不稳定性分数」,并把连续分数投影到之前的图像上监督稠密视觉预测器;提供利用事后信息的硬分数和可即时因果计算的软分数两个变体。在 1716 个人工标注接触上,两种变体检测不稳定及排序严重度均优于所有对比方法,汇总严重度排序比最强基线提升 28%;三次户外测试中训练出的视觉预测器等级相关性比最强替代高 58%,加入机载上下文后再提升 25%;50 米森林轨迹真机实验中能处理泥地、植被等非几何地形属性并绕开倒木。
- 🇬🇧 Self-supervised learning could give legged robots the human ability to anticipate ground response before stepping, but the supervisory signal is usually chosen by intuition. TACOS defines a consistent footstep instability score from the residual of a factor graph in legged state estimation and projects it into preceding images to supervise a dense visual predictor, with a hindsight "hard" variant and a causal "soft" variant. On 1,716 manually annotated contacts both variants beat all alternatives, improving pooled severity ranking by 28% over the strongest baseline; on three outdoor runs the trained predictor improves rank correlation by 58% (a further 25% with onboard context), and on a 50 m forest trajectory it handles mud and vegetation while stepping around fallen branches.

### [RAIBO-Wagon: Real-Time Navigation System for a Legged Robot Towing a Wagon](https://arxiv.org/abs/2610.39267) — (Insung Yang, Eunchae Kim, Jungwoo Hur, Seunghun Jeon 等)
🏷️ 交叉方向 / Also: 运动控制·RL(学习的前向动力学 / learned FDM)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://insungyang.github.io/raibo-wagon/)已给出,代码链接未核实
- 🇨🇳 足式机器人与欠驱动外物(如拖车)耦合后动力学更复杂,在狭窄空间中要在严格实时约束下找到窄可行路径。该工作把条件流匹配(CFM)与基于学习的前向动力学模型(FDM)上的 MPPI 控制结合:CFM 缓解 MPPI 初始化问题并加速收敛,MPPI 经迭代细化恢复 CFM 训练分布之外的可行解,并集成为 RAIBO-Wagon(四足拖拽定制拖车)的全栈导航系统。在 15 米长的受限空间户外实验中,所有感知与计算均在机载完成,40 次试验成功率 85%,拖拽总载荷最高 40 kg,接近机器人自重的 100%。
- 🇬🇧 Coupling a legged robot to an underactuated object such as a wagon makes dynamics harder, and confined spaces demand finding narrow feasible paths in real time. The system combines Conditional Flow Matching with MPPI over a learned forward dynamics model: CFM fixes MPPI's initialization and speeds convergence while MPPI refines to feasible solutions beyond CFM's training distribution, integrated in a full-stack navigation system for RAIBO-Wagon. In 15 m confined outdoor courses with fully onboard sensing and computation it achieves 85% success over 40 trials while towing up to 40 kg, nearly 100% of the robot's body weight.

### [Value Function-Guided MPPI for Hierarchical Planning and Control in Off-Road Autonomous Navigation](https://arxiv.org/abs/2610.38731) — CMU(Anoushka Alavilli, Raymond Song, Guanya Shi, Jeff Schneider)
🏷️ 交叉方向 / Also: 运动控制·RL(RL 价值函数 / RL value function)。归入传统类的理由:核心贡献为 MPPI 规划/控制层,RL 控制器为预训练组件。
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接
- 🇨🇳 越野导航的分层架构依赖显式代价地图和自上而下的单向信息流,规划与底层真实执行代价脱节。该工作提出双向信息流的分层框架:顶层 MPPI 式规划器输出路点给预训练的底层 RL 控制器,并以 RL 控制器的价值函数作隐式代价,不再使用显式代价地图;还提出在线策略评估以适应训练与评估间的价值函数分布偏移。在高保真越野驾驶模拟器的多种地形下,相比基线 MPPI 控制器,导航更安全有效,并免去显式代价地图;预印本摘要未给出具体数值。
- 🇬🇧 Hierarchical off-road navigation relies on explicit cost maps and one-way information flow from planner to controller, decoupling planning from true execution cost. The authors propose bidirectional flow: a top-level MPPI-style planner passes waypoints to a pretrained low-level RL controller and uses that controller's value function as an implicit cost, with an online policy-evaluation process to adapt the value function to distribution shift. In a high-fidelity off-road simulator across challenging terrains it navigates more safely and effectively than a baseline MPPI controller without explicit cost maps; the abstract gives no numeric results.

### [Learned Terminal Costs for Short-Horizon Model Predictive Control of Autonomous Trucks in Interactive Highway Traffic](https://arxiv.org/abs/2610.40257) — (Hooman Hamze, Benjamin Houshmand, Deepthi Pathare, Erik Börve)
🏷️ 交叉方向 / Also: 运动控制·RL(RL + MPC 混合;按规则本应归 RL 类,但任务为公路卡车驾驶而非机器人 locomotion/操作控制,故置于传统类并注明)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments(13 pages)无代码链接
- 🇨🇳 重型卡车公路驾驶需在安全约束与长时域决策间平衡:MPC 有约束保证但短时域受终端代价限制,纯 RL 无约束保证且稀疏碰撞惩罚下过于保守。该工作提出 MPC 与 RL 混合框架:有限时域 MPC 经动态规划求解,用预训练 RL 模型估计终端代价。在带反应式周围交通的仿真中与零终端代价的纯 MPC、基线策略 rollout 终端代价及纯 RL 对比,混合方法达到零碰撞且代价为所有配置中最低。
- 🇬🇧 Highway driving for heavy trucks must balance safety constraints and long-horizon decisions: MPC guarantees constraints but is limited by its terminal cost at short horizons, while pure RL has no guarantees and turns conservative under sparse collision penalties. The authors propose a hybrid in which a finite-horizon MPC solved by dynamic programming uses a pretrained RL model to estimate terminal cost. In simulation with reactive traffic, compared with pure MPC with zero terminal cost, base-policy rollout terminal cost and pure RL, the hybrid achieves zero collisions with the lowest cost of all configurations.

### [socx: GPU-Accelerated Chance-Constrained Stochastic Optimal Control using JAX](https://arxiv.org/abs/2610.40427) — (Tanmay Dokania, Yashwanth Kumar Nakka)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 线性随机最优控制的机会约束提升凸重构规模大、求解慢。socx 是 JAX 实现的 GPU 加速求解器:利用问题稀疏且独立的结构,通过分布式优化把问题化为相互独立的线性二次跟踪(LQT)子问题和欧氏投影,并行求解后由约束耦合。在悬停线性化三维四旋翼上,相对 MOSEK 加速最高 98 倍、相对 SCS 最高 2224 倍;可求解时域 N=1120,而 MOSEK 在 N=320 时内存耗尽;并给出消融实验分离关键加速因素。
- 🇬🇧 Lifted convex reformulations of chance-constrained linear stochastic optimal control are large and slow to solve. socx is a JAX GPU solver that exploits the sparse, independent structure so distributed optimization reduces the problem to independent LQT problems and Euclidean projections solved in parallel and coupled via constraints. On a hover-linearized 3D quadrotor it is up to 98× faster than MOSEK and up to 2224× faster than SCS, solves horizons up to N=1120 where MOSEK runs out of memory at N=320, and ablations isolate the key speed-up components.

### [Selective Sliding Mode Control Enhances Robustness of Aerial Robots Under Disturbances](https://arxiv.org/abs/2610.38930) — (Anoop Kiran, Thales C. Silva, Nora Ayanian)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接
- 🇨🇳 四旋翼在阵风与载荷变化等扰动下的控制仍具挑战,一阶滑模控制(SMC)等经典方法并未说明级联控制器中哪些回路应做鲁棒化、如何整定、嵌入式代价如何。该工作提出判定鲁棒控制应放在级联架构何处的方法:通过反演运动方程从扰动下的 PID 悬停飞行恢复作用扰动,识别并量化被激励的轴,只在关键处部署鲁棒控制,全部在机载运行。Crazyflie 2.1 在吊挂载荷和斜向风扰动下,跟踪提升集中在规则选出的轴上;增益扫描证实切换增益能减小匹配轴误差,但对被激励的不匹配轴无效,与分析预测一致。
- 🇬🇧 Quadrotor control under gusts and payload changes remains hard, and classical SMC does not say which loops of a cascaded controller should be made robust, how to tune them, or what they cost onboard. The authors infer the acting disturbance from PID hover flights by inverting the equations of motion, identify and quantify the excited axes, and deploy robust control only where it counts, all onboard. On a Crazyflie 2.1 under slung-payload and oblique-wind disturbances, tracking gains concentrate on the selected axes, and gain sweeps confirm the switching gain reduces error on matched axes but not on an excited unmatched axis, as predicted.

### [Actuator-Aware Observer Inputs for Cascade ADRC of Quadrotors Under Rotor Lag, Measurement Delay and Sensor Noise](https://arxiv.org/abs/2610.39126) — (Xuan-Quy Dao, Ngoc-Bich Le, Le-Minh Nguyen)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Quang61123/actuator-aware-cas);Comments 给出代码、增益与随机种子,但匿名 git ls-remote 返回需要认证,链接匿名不可访问,待核实
- 🇨🇳 级联线性自抗扰控制(LADRC)中扩张状态观测器通常接收瞬时指令,而延迟的测量反映的是更早的、经转子滤波的加速度。该工作提出「执行器感知」观测器输入:高度与姿态观测器使用经假定转子模型滤波并与测量延迟对齐的受限虚拟输入,水平观测器使用由测得姿态重构的加速度;增益在离散时间模型上依灵敏度、阶跃响应和平稳协方差上限选取。成对设定点试验中 PID-Budget、AA-Budget、AA-HalfGain 的平均 RMSE 为 65.5、19.2、16.9 mm;更严格的共同上限下 AA 设计为 29.9 与 26.4 mm,对比 72.3 mm 的 PID;PX4 SITL 复现结果;EKF2 后端下 AA-Budget-E 将设定点 RMSE 由 59.1 mm 降到 44.0 mm。证据基于仿真。
- 🇬🇧 In sampled cascade LADRC the extended-state observer typically receives the instantaneous command although the delayed measurement reflects an earlier, rotor-filtered acceleration. The paper proposes actuator-aware observer inputs (limited virtual inputs filtered by an assumed rotor model and aligned with the measurement delay; horizontal observers use acceleration reconstructed from measured attitude), with fixed gains chosen on the discrete-time model under sensitivity, step-response and covariance-ceiling requirements. In paired set-point trials PID-Budget, AA-Budget and AA-HalfGain reach mean RMSE 65.5, 19.2 and 16.9 mm; under a stricter ceiling the AA designs reach 29.9 and 26.4 mm versus 72.3 mm for PID; PX4 SITL reproduces this, and behind EKF2 AA-Budget-E cuts set-point RMSE from 59.1 to 44.0 mm. Evidence is simulation-based.

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

候选共 30 条,详细展开 11 条,其余 19 条列名。 / 30 candidates; 11 expanded, 19 listed by name.

### [Gym-Anything for Robotics: Scaling physical simulations with digital agents](https://arxiv.org/abs/2610.40565) — (Pranjal Aggarwal, Sean Welleck)
🏷️ 交叉方向 / Also: 运动控制·RL(RL 环境生成;贡献在仿真/环境构建而非控制算法,故归入本类) / VLA
开源状态 / Code: ✅ 已开源 / Released — [项目页](https://gym-anything.github.io/robotics);摘要称发布流水线、RL 环境与基准,未核实 GitHub 仓库地址
- 🇨🇳 现有机器人仿真覆盖的任务与物理现象有限,构建更好的仿真需要大量专家工作而难以扩展。该工作把仿真创建视为 coding agent 任务,以美国 GDP 数据选取覆盖有经济价值体力劳动的仿真,并设计对抗式「创建-审计」循环检查仿真与任务,构建 RoboWorld:25 个仿真、25 个测试和 175 个训练 RL 环境。最强前沿模型在每个 RoboWorld 测试任务上均失败,平均奖励仅 0.06;作者进一步提出上下文内重复学习、特权教师、自助特权经验学习以及用代码策略生成演示训练 π0.5 等 VLA 的方法,均显著提升性能。
- 🇬🇧 Existing robot simulations cover few tasks and phenomena, and building better ones needs scarce expert effort. The authors treat simulation creation as a coding-agent task, choose simulations from U.S. GDP data to cover valuable physical work, and run an adversarial creation–audit loop, producing RoboWorld: 25 simulations with 25 test and 175 training RL environments. Even the best frontier models fail every test task (average reward 0.06); in-context learning across attempts, a privileged teacher, self-assisted learning from privileged experience and code policies that generate demonstrations to train VLAs such as π0.5 each substantially improve performance.

### [Recursive Self-Improvement in Physical AI: Mechanisms, Evidence, and Evaluation](https://arxiv.org/abs/2610.38266) — (Xiaofeng Han, Kaize Luo, Zenghuang Fu, Zichong Zhu 等)
开源状态 / Code: ✅ 已开源 / Released — [综述论文列表仓库](https://github.com/nkd-lkz/physical-ai-rsi-survey);已用 git ls-remote 验证存在(仅为文献清单)
- 🇨🇳 具身系统可从部署经验更新策略、世界模型、技能和可执行程序,当系统还修订并重用数据获取、反馈或学习流程时便引入递归自我改进。这篇综述围绕「持久能力与其改进过程」的联系,比较策略学习、想象经验、记忆与技能积累、可执行 harness 等路线,并提出 L0–L3 分级(任务局部适应、持久能力增益、继承的流程修订、经验证的改进器增益);进一步提出从共享学习器起点比较参考与修订改进器的公共数据与交互式评估。纯综述,无定量结果。
- 🇬🇧 Embodied systems can update policies, world models, skills and programs from deployment experience, and recursive self-improvement arises when they also revise the procedures producing data, feedback or learning. This survey links persistent capability to its improvement process, compares policy learning, imagined experience, memory/skill accumulation and executable harnesses, proposes an L0–L3 rubric (task-local adaptation, persistent capability gain, inherited process revision, verified improver gain) and common-data/interactive comparisons from shared learner starts. It is a survey without quantitative results.

### [RoboAtom: Large-scale Atomic-Action Supervision for Robot Learning](https://arxiv.org/abs/2610.40207) — (Xueyuan Wei, Xuanxu Wang, Xudong Li, Yuping He 等)
开源状态 / Code: 🕒 计划开源 / Planned — 摘要承诺「We will release the data, benchmark, model, and construction pipeline」,尚无链接
- 🇨🇳 机器人数据集通常只有任务级指令,子任务标注格式不一,阻碍跨源联合训练。RoboAtom-Data 为多来源数据添加统一、时间对齐的原子动作标注,覆盖 145 万条轨迹、688 万个技能标注片段、16,882.1 小时;流程结合统一协议、大规模人工标注、同序技能重复执行间传播和多阶段质检,并构建 RoboAtom-Bench。RoboAtom-Anno 在 RoboAtom-Bench 与外部 WGO-Bench 上自动标注性能优于所有被评估的开源/闭源模型;配合分层执行,在 LIBERO-Long、LIBERO-Plus 和 RoboTwin 上任务成功率高于任务级基线。
- 🇬🇧 Robot datasets typically carry task-level instructions only, with inconsistent subtask labels hindering joint training. RoboAtom-Data adds unified, time-aligned atomic-action annotations to multi-source data covering 1.45M trajectories, 6.88M skill-labeled segments and 16,882.1 hours via a unified protocol, large-scale manual annotation, propagation across repeated executions and multi-stage QC, plus RoboAtom-Bench. RoboAtom-Anno beats all evaluated open and closed models on RoboAtom-Bench and WGO-Bench, and atomic supervision with hierarchical execution improves success over task-level baselines on LIBERO-Long, LIBERO-Plus and RoboTwin.

### [UMI-Live for In-The-Wild Bimanual Robotics Data Collection](https://arxiv.org/abs/2610.39385) — (Govind Velamoor, Adrian Lin, Sam Jung, Spencer Mateega 等)
🏷️ 交叉方向 / Also: 空间智能与 SLAM / SLAM(并行 SLAM 重建)、VLA
开源状态 / Code: ✅ 已开源 / Released — [项目页](https://umi-live.github.io/);摘要称发布完整硬件设计、软件、复现指南与 40 小时数据,未核实仓库地址
- 🇨🇳 UMI 设备允许专家无需遥操作机器人即可示教,但使用这些数据仍需一致的硬件、标定和数据处理。UMI-Live 是全栈开源双手 UMI 系统:自研硬件集成相机与 LiDAR-惯性传感、机载计算和供电,环境内无需外部追踪或标定;异步管线并行做 SLAM 重建并输出训练就绪数据集,并提供双 YAM 遥操作与 VLA 训练/推理软件。微调 π0.5 与 MolmoAct2 在双手抓放任务上分别成功 10/10 和 8/10;同时发布涵盖三项任务的 40 小时数据。
- 🇬🇧 UMI devices let experts demonstrate without teleoperating robots, but using the data still needs consistent hardware, calibration and processing. UMI-Live is a full-stack open-source bimanual system with custom hardware integrating camera and LiDAR-inertial sensing, onboard compute and power, no external tracking or calibration, and an asynchronous pipeline doing parallel SLAM reconstruction and publishing training-ready datasets, plus dual-YAM teleoperation and VLA training/inference software. Fine-tuning π0.5 and MolmoAct2 gives 10/10 and 8/10 on a bimanual pick-and-place task, and 40 hours of data over three tasks are released.

### [Embodied at Sea: Imitation Learning for Multi-Task Underwater Manipulation](https://arxiv.org/abs/2610.38199) — NYU(Greta Perez-Haiek, Luca Macesanu, Kevin Angers, Mohammed Imam 等)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ✅ 已开源 / Released — [项目页](https://lair-research-nyu.github.io/Embodied-at-Sea/);摘要称 BLUEMBODIED KIT 已开源,未核实仓库地址
- 🇨🇳 行为克隆在陆上操作中泛化良好,但海洋视觉畸变与动态水流造成严重域偏移。作者在平静与湍流水域收集 1616 条水下操作数据,训练 14 个不同本体感知配置的通用 VLA(DynamicVLA);三项任务、1260 次池中硬件试验中 10 个模型优于基线,最佳模型总成功率(含部分成功)93.3%。另在 WWII 沉船 Coralita X127 与 Manoel Island 码头的 ROV 案例中,单任务 ACT 显著优于通用 VLA SmolVLA(汇总成功率 47.9% 对 7.9%),海洋考古现场最成功任务达 66.7%。
- 🇬🇧 Behavior cloning generalizes well on land but marine visual distortion and currents cause severe domain shift. 1,616 underwater episodes (calm and turbulent) trained 14 generalist VLA models (DynamicVLA) with different proprioception configurations; across three tasks and 1,260 on-hardware pool rollouts 10 models beat the baseline, the best at 93.3% overall (including partial success). In ROV case studies at the WWII wreck Coralita X127 and Manoel Island Marina, single-task ACT clearly beat generalist SmolVLA (47.9% vs 7.9% pooled), with 66.7% on the best archaeology task.

### [Same Label, Different Interface: Beyond Action-Space Labels in Robot Learning](https://arxiv.org/abs/2610.38104) — (Arshia Sangwan, Zhongyang Zhang)
🏷️ 交叉方向 / Also: 运动控制·RL(PPO 策略的动作接口;贡献为评估方法论,故归入本类)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 机器人学习常把位置与速度动作当作单一实验处理,但策略输出还要经过滤波、物理缩放、参考构造、反馈、时序与力矩限制。在 Factory 的 PegInsert、GearMesh、NutThread 三个接触丰富任务上,以同一学习器和训练预算比较五种关节空间接口(每条件十个独立策略)。仅改变物理动作缩放,各任务样本中位评估成功率变化 0.645–1.000;去掉指数滑动平均的影响因任务而异;把速度缩放校准到与位置接口的局部原始力矩增益相等后,GearMesh 与 NutThread 的中位数上升,但 PegInsert 与 GearMesh 仍有明显残差差距,结论是动作接口比较应报告实际执行通路。
- 🇬🇧 Robot-learning studies treat position and velocity actions as single treatments, yet policy output passes through filtering, scaling, reference construction, feedback, timing and effort limits. On three contact-rich Factory tasks (PegInsert, GearMesh, NutThread), five joint-space interfaces are compared with one learner and budget (ten policies per condition). Changing only the physical action scale shifts median success by 0.645–1.000; removing the EMA has task-dependent effects; calibrating the velocity scale to match the position interface's raw-torque gain raises medians on GearMesh and NutThread, yet clear residual gaps remain on PegInsert and GearMesh, so comparisons should report the executed pathway.

### [CuraEval: Evaluating Demonstration Curation on Mixed-Skill Robot Data](https://arxiv.org/abs/2610.38221) — (Jiuyi Xu, Meida Chen, Yang Ye, Yangming Shi 等)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/jiuyixu25/CuraEval);已用 git ls-remote 验证存在(Comments:CoRL 2026 Workshop)
- 🇨🇳 模仿学习数据质量不一,现有示教筛选方法的评估协议各异,难以判断是否优于简单基线。CuraEval 结合对示教分数的数学分析与在 robomimic 混合技能数据上(Diffusion Policy 与 BC-RNN)对固定大小随机子集及全数据训练的受控对比。PSD 分数只取决于回合长度与位置平方幅值,在 square 上与长度排序几乎相同(ρ=0.999);选最短 50% 示教使 square 成功率由随机的 70.7% 升到 76.5%;而几何熵 LOO 选择器在 25% 保留时 can 成功率由 94.7% 降到 74.0%。经 Holm 校正后没有任何被评估的筛选条件显著优于全数据训练。
- 🇬🇧 Imitation data quality varies and curation methods are evaluated under inconsistent protocols. CuraEval combines mathematical analysis of demonstration scores with controlled comparisons against fixed-size random subsets and full-data training on mixed-skill robomimic data (Diffusion Policy, BC-RNN). The PSD score depends only on episode length and squared position magnitudes (ρ=0.999 with length on square); keeping the shortest 50% raises square success from 70.7% to 76.5%, while a geometric-entropy LOO selector drops can success at 25% retention from 94.7% to 74.0%. After Holm correction no curated condition significantly beats full-data training.

### [ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning](https://arxiv.org/abs/2610.39429) — UT Austin(Neel Jawale, Stephan Pleines, Soha Pouya, Yuke Zhu 等)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://schedulegen.github.io/)已给出,代码链接未核实
- 🇨🇳 多臂机器人(双手、人形)完成任务周期短,但受多臂约束难以安全控制,且大规模多臂数据采集是瓶颈;现有自动示教生成算法忽略多臂约束,易生成不安全且失败的行为。ScheduleGen 是面向多臂示教生成的集成规划与调度算法,在 28 个仿真任务变体(含 7 个外部 RoboDojo 任务)上数据生成平均成功率 79.6%,训练出的策略平均成功率 65.5%,优于最先进数据生成基线,并通过零样本 sim-to-real 与 real-to-sim-to-real 在八个真实变体上达到 50–80% 成功率。
- 🇬🇧 Multi-arm platforms finish tasks faster but are harder to control safely and lack large datasets; existing demonstration-generation algorithms ignore multi-arm constraints and yield unsafe, failing behavior. ScheduleGen is an integrated planning-and-scheduling algorithm for multi-arm demonstration generation: on 28 simulated task variants (including 7 external RoboDojo tasks) it reaches 79.6% mean data-generation success and trains policies with 65.5% mean success, beating a state-of-the-art baseline, and gets 50–80% success on eight real variants via zero-shot sim-to-real and real-to-sim-to-real.

### [Self-Labeled Preference Transfer for Steerable Robot Manipulation](https://arxiv.org/abs/2610.38000) — (Kaiwen Hong, Shaoting Peng, Xiangyu Zeng, Pengcheng Wang 等)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 VLA 可学习遵循抓取位置、绕障方式等执行偏好,但为每个新任务提供偏好标注代价高。作者发现:带偏好标注训练的策略在新任务上能遵循偏好但任务成功率有限,用无偏好标注的目标示教微调提升成功率却削弱偏好控制。据此提出 SPT:在带标注源示教上联合训练共享视觉语言骨干的偏好条件动作预测与偏好识别,再冻结识别器为目标示教自标注并微调策略。仿真五类偏好上识别器准确率 96.4%,SPT 偏好遵循 84.8%、任务成功 89.2%(朴素微调 59.4%、88.0%);多偏好 93.8% 对基线 42.5%;真机两个任务迁移中偏好遵循由 52.5% 升到 92.5%。
- 🇬🇧 VLAs can learn execution preferences (grasp location, obstacle detours) but annotating each new task is costly. A policy trained with annotations follows preferences on a new task with limited success, while fine-tuning on unannotated target demos improves success but weakens preference control. SPT jointly trains preference-conditioned action prediction and preference recognition on annotated source demos, freezes the recognizer and self-labels target demos for fine-tuning. In simulation the recognizer reaches 96.4%, SPT 84.8% preference following and 89.2% success versus 59.4% and 88.0% for naive fine-tuning; multi-preference 93.8% vs 42.5%; on real robots preference following rises from 52.5% to 92.5%.

### [JEDI: Joint-Embedding Demonstration Compression for In-Context Imitation Learning](https://arxiv.org/abs/2610.40356) — (Jiazhao Liang, Zhewen He, Shuaihang Yuan, Hao Huang 等)
🏷️ 交叉方向 / Also: 世界模型 / World Model(video-JEPA)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 上下文模仿学习用测试时示教自适应,但长多模态轨迹限制上下文中可放入的示例数。JEDI 把示教压缩成潜在槽,训练目标是在冻结的 video-JEPA 空间中预测查询回合的下一阶段关键帧;任务与过程反事实帮助槽保留执行细节,预测器从示教库中选择示教,关键点 token 后训练支持人手条件。LIBERO 与真机实验显示支持多示例上下文,在 LIBERO 目标对照中比仅动作压缩成功率和示教遵循度更高;预印本摘要未给出具体数值。
- 🇬🇧 In-context imitation learning adapts policies via test-time demonstrations, but long multimodal trajectories limit how many fit in context. JEDI compresses demonstrations into latent slots trained to predict the query episode's next-stage keyframe in a frozen video-JEPA space, with task and process counterfactuals preserving execution detail, a predictor selecting demonstrations from a bank, and keypoint-token post-training enabling human-hand conditioning. LIBERO and real robots show many-shot context support and improved success and demonstration following over action-only compression in LIBERO controls; the abstract gives no numbers.

### [EmbodiExp: Compositional Experience Transfer for Embodied Agents](https://arxiv.org/abs/2610.39180) — (Zhifeng Gu, Ying Chen, Rui Jiang, Lei Yi 等)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 经验可帮助具身智能体把高层计划落地为动作,但跨任务迁移时先前策略可能不适用于当前状态或达不到预期结果。EmbodiExp 利用「任务常共享可独立判定完成与否的子目标」这一观察,引入结果落地的子目标经验(含子目标、适用条件、可调策略与可验证结果),执行时由适用经验指导动作生成,已验证的结果可为后续经验建立条件,实现在线组合;子目标级结果归因还让失败轨迹也能贡献已验证的局部成功及需避免的动作。多个具身基准、固定经验库的折叠协议下实验证明有效;预印本摘要未给出具体数值。
- 🇬🇧 Experience can ground high-level plans into actions but transfers poorly across tasks when old strategies are inapplicable or fail. EmbodiExp builds on shared, independently verifiable subgoals: outcome-grounded subgoal experiences (subgoal, applicability conditions, adaptable policy, verifiable outcome) guide action generation, verified outcomes establish conditions for later experiences enabling online composition, and subgoal-level attribution lets failed trajectories contribute verified local successes and actions to avoid. Experiments on multiple embodied benchmarks with frozen experience banks show effectiveness; no numbers are given in the abstract.

**其余 19 条列名 / Remaining 19 listed by name:** [Robotic Data Inoculation](https://arxiv.org/abs/2610.39054)、[Tactus](https://arxiv.org/abs/2610.39076)、[TouchBridge](https://arxiv.org/abs/2610.40349)、[Improving Fine-Grained Manipulation through Demonstration Expansion and Execution Design](https://arxiv.org/abs/2610.40430)、[Smooth Action Chunking Via Movement-Primitive Representations](https://arxiv.org/abs/2610.39451)、[Tracking Task Progress Through Errors and Recovery](https://arxiv.org/abs/2610.39125)、[ProLoop](https://arxiv.org/abs/2610.39319)、[LOGIV](https://arxiv.org/abs/2610.40016)、[AtomTree](https://arxiv.org/abs/2610.38744)、[Teaching a Tree to Recover](https://arxiv.org/abs/2610.39775)、[BURGER](https://arxiv.org/abs/2610.40532)、[EgoContact](https://arxiv.org/abs/2610.39167)、[When "No Worries" Went Wrong](https://arxiv.org/abs/2610.38400)、[Coupled Guidance for Flow Matching](https://arxiv.org/abs/2610.40109)、[Compositional Diffusion Planning with Chunk Selection and Reachability Measure](https://arxiv.org/abs/2610.38291)、[Language-Grounded Force/Torque Pretraining](https://arxiv.org/abs/2610.39314)、[DAWN](https://arxiv.org/abs/2610.40537)、[SwapBot](https://arxiv.org/abs/2610.40646)、[DexSuite](https://arxiv.org/abs/2610.37799)(Genesis 灵巧操作框架,30 任务/4,700 条仿真示教,摘要称开源,[项目页](https://dexsuiteorg.github.io);🏷️ 交叉方向:运动控制·RL 的仿真基础设施,因贡献为框架/数据集而归入本类)。共 19 条。 / 19 items in total.

## VLA / VLA

共 9 条,全部展开。 / 9 items, all expanded.

### [HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model](https://arxiv.org/abs/2610.40373) — (Rongxing Ding, Hongyu Qu, Kehong Wu, Xudong Wang 等)
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 现有融合未来预测的 VLA 常把短期动力学与长期任务目标分开建模,又未充分考虑预测未来与当前动作需求的相关性。HiFOR 通过层次依赖掩码联合预测短期状态演化、语义里程碑和最终目标状态,按时域、视角、空间维度组织未来潜变量,并在去噪过程中依据不断演化的动作表示做动作引导的分解式世界检索,为动作生成提供针对性指导。在两个仿真基准和六个真实操作任务上验证有效;预印本摘要未给出具体数值。
- 🇬🇧 VLAs with future prediction often model short-term dynamics and long-term goals separately and inject predicted futures without regard to relevance to current actions. HiFOR jointly predicts short-term evolution, semantic milestones and final goals through a Hierarchical Dependency Mask, organizes future latents along horizon, view and space, and retrieves relevant future information guided by evolving action representations during denoising. It is validated on two simulation benchmarks and six real manipulation tasks; the abstract gives no numbers.

### [CoRAct: From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2610.39543) — (Yixue Zhang, Wenke Xia, Kun Wu, Wenbo Yu 等)
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown — [项目页与数据集](https://onlyxingxingzyx.github.io/CoRAct/)已给出,代码链接未核实
- 🇨🇳 带具身思维链(ECoT)的 VLA 对动作的引导是隐式的,动作只以 ECoT 为条件而未被显式优化去对齐。CoRAct 通过在动作噪声空间的奖励引导优化显式对齐推理与动作:把「运动」与「路点」两个物理 ECoT 成分作为可验证信号,统一的 MoT 联合建模 ECoT 推理、动作生成与动作条件未来预测;对噪声采样的候选动作计算运动一致性与预测结果-路点一致性奖励,以组相对优化更新初始噪声分布。RoboCasa、VLABench 与真实操作上,任务成功率、泛化与推理-执行对齐均优于强 ECoT VLA 基线,并支持借助外部 ECoT 零样本适应;预印本摘要未给出具体数值。
- 🇬🇧 ECoT-based VLAs guide actions only implicitly, conditioning on reasoning without optimizing alignment. CoRAct aligns reasoning and action through reward-guided optimization in action noise space, using movement and waypoints as verifiable signals; a Mixture-of-Transformers jointly models ECoT, action generation and action-conditioned future prediction, and alignment rewards on movement consistency and predicted-outcome/waypoint agreement drive group-relative optimization of the initial noise distribution. On RoboCasa, VLABench and real tasks it improves success, generalization and reasoning–execution alignment over strong ECoT VLAs and enables zero-shot adaptation with externally provided ECoTs; no numbers in the abstract.

### [OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation](https://arxiv.org/abs/2610.39287) — (Junli Liu, Zhongrui You, Chenhui Li, Zhen Li 等)
🏷️ 交叉方向 / Also: VLN(空中导航 / aerial navigation)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Ideal-ljl/AeroBrain)(HF Daily Papers 的 githubRepo,已验证仓库存在);摘要称「Code will be made publicly available」,具体已放出内容未核实
- 🇨🇳 空中机器人的现有系统常专用于单项能力、依赖机外计算或难以在资源受限平台持续闭环运行。OpenFlyV2 是统一的机载 VLA:共享视觉语言表示支持语义理解、语言落地感知、空间推理与连续飞行控制,紧凑动作专家把多模态上下文转为短时域航点,运动感知时序记忆与动作先验降低闭环开销;构建约 7 万条导航轨迹与 6 万条图文指令-响应对的仿真数据集。在 Jetson Orin NX 上以 10 Hz 完全机载生成每块 12 个航点的动作块,零样本从仿真迁移到实体四旋翼,在四个真实环境中导航成功率 48%,无需真实空中训练数据。
- 🇬🇧 Aerial systems are often specialized, offboard, or unable to run closed-loop on constrained platforms. OpenFlyV2 is a unified onboard VLA using a shared vision-language representation for semantic understanding, language-grounded perception, spatial reasoning and continuous flight control, with a compact action expert producing short-horizon waypoints and motion-aware temporal memory plus action priors reducing closed-loop cost; a simulation dataset has ~70k navigation trajectories and 60k instruction–response pairs. It generates 12-waypoint chunks entirely onboard at 10 Hz on a Jetson Orin NX and transfers zero-shot to a physical quadrotor with 48% navigation success across four real environments without real aerial training data.

### [SaiVLA-JEPA: Evaluating Future Latent Prediction in JEPA-Conditioned VLA Control](https://arxiv.org/abs/2610.38508) — (Rufeng Xiao, Ruihao Xiao, Wei Chen, Xinhai Sun 等)
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 研究当 VLA 已使用 V-JEPA 特征时,预测未来表示的目标是否进一步改善闭环控制。SaiVLA-JEPA 由 VLM 加扩散 Transformer 动作专家、冻结 V-JEPA 编码器特征组成,训练时两个轻量辅助头预测未来表示、推理时去掉。在 10,030 条成对 LIBERO-Plus 回合上,当前 JEPA 条件使成功率约 82.5%(无 JEPA 为 71.6%),而未来监督在评估训练预算下无可检测的总体增益;潜变量上下文重试的增益是更大尝试预算下的系统级结果,参数自适应无一致优势。
- 🇬🇧 The paper asks whether predicting future representations improves closed-loop control when a VLA already uses V-JEPA features. SaiVLA-JEPA combines a VLM and diffusion-transformer action expert with frozen V-JEPA features, with two auxiliary heads predicting future representations in training and omitted at inference. On 10,030 paired LIBERO-Plus episodes current JEPA conditioning reaches about 82.5% success versus 71.6% without, while future supervision gives no detectable aggregate gain; the context-retry gain is a system-level result under a larger attempt budget and parameter adaptation shows no consistent advantage.

### [What Actually Matters? A Paired Evaluation of Inference Settings for π0.5 on BEHAVIOR-1K](https://arxiv.org/abs/2610.37917) — (Ruben Hammele, Samira Huber, Mohammad Nazeri, Amirreza Payandeh 等)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://rubenhammele.github.io/behavior2026)含视频与分析,代码链接未核实
- 🇨🇳 小规模场景中部署的推理与数据采集策略未必能推广到大规模多样任务集。作者对已提出的策略在全部 100 个任务上做系统的成对评估,使用基于 2025 BEHAVIOR Challenge 冠军微调的 π0.5 模型(公开测试集 Q-score 0.39)。结论:这些策略并不能均匀地迁移到新环境与任务,纯评估类论文。
- 🇬🇧 Inference and data-collection strategies deployed at small scale may not generalize to large, diverse task suites. The authors run a systematic paired evaluation of proposed strategies across all 100 tasks using a π0.5 model fine-tuned from the 2025 BEHAVIOR Challenge winner (Q-score 0.39 on the public test set). Result: the proposed strategies do not transfer uniformly to new environments and tasks; an evaluation-only study.

### [How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function](https://arxiv.org/abs/2610.40002) — (Dabin Seo, Eunhyek Joa)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 推理型 VLA 先写推理轨迹再解码动作,错误或误导的轨迹会导致错误动作。CoC-CFG 在策略上下文与去掉推理片段的上下文之间做无分类器引导,每个 Euler 步一个权重,把权重选择视为动作价值被「测量」而非自举的 MDP,用小 critic 拟合并保守地改进控制器。在 Alpasim 驾驶仿真中开环优于所有固定权重及在线 RL(SAC、GRPO),闭环通过 300 个场景中的 262 个(原策略 252);在 Waymo 端到端驾驶基准隐藏测试集上,冻结 Alpamayo 1.5 配合 Q-adaptive 引导得到评分 8.135159,高于最佳已发表方法的 8.079。注:应用场景为自动驾驶。
- 🇬🇧 Reasoning VLAs write a trace then decode the action, so a wrong or misleading trace yields a wrong action. CoC-CFG applies classifier-free guidance between the policy context and the context without the reasoning span, with one weight per Euler step, treating weight choice as an MDP whose action values are measured rather than bootstrapped and fitted by small critics. In Alpasim it beats every fixed weight and online RL (SAC, GRPO) in open loop and passes 262 of 300 scenes in closed loop versus 252 for the original policy; on the hidden Waymo end-to-end test set, frozen Alpamayo 1.5 with Q-adaptive guidance scores 8.135159 versus 8.079 for the best published method. The application is autonomous driving.

### [Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models](https://arxiv.org/abs/2610.38661) — (Jiuyi Xu, Xiao Hu, Meida Chen, Song Wang)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/jiuyixu25/QbD-VLA);已用 git ls-remote 验证存在
- 🇨🇳 VLA 的训练后量化降低位宽时难以保持任务性能,而用任务成功率直接指导混合精度因闭环评估昂贵且组件间相互影响而少被探索。QbD-VLA 用短时闭环评估的任务成功率分配权重和激活位宽并考虑组件交互。四个 VLA 模型、LIBERO 全部四个套件上,在平均约 4 比特权重、少于 6 比特激活下任务表现良好;SIMPLER 上相对均匀量化增益较小;Franka Research 3 真机上仿真选出的分配在 X-VLA 上未检出成功率损失,但在 π0.5 上失败。
- 🇬🇧 PTQ of VLAs struggles to keep task performance at lower bit widths, and using task success directly to guide mixed precision is underexplored because closed-loop evaluation is costly and components interact. QbD-VLA assigns weight and activation bit widths from short closed-loop task-success evaluations while accounting for component interactions. Across four VLA models and all four LIBERO suites it performs well at ~4-bit weights and under 6-bit activations; the SIMPLER gain over uniform quantization is small; on a Franka Research 3, simulation-selected allocations show no detected loss on X-VLA but fail on π0.5.

### [Decoding Geometry, Not Tokens: Efficient VLMs for Robot Affordance and Trajectory Prediction](https://arxiv.org/abs/2610.39416) — (Akila Ayanthi, Darshana Priyasad, Tharindu Fernando, Dimity Miller)
🏷️ 交叉方向 / Also: 空间智能 / Spatial Intelligence
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接(Comments:WACV 2027)
- 🇨🇳 VLM 把抓取位置与运动预测当作语言生成,逐 token 自回归解码坐标,忽略空间结构并截断连续精度。作者表明 0.5–2B 参数的小型 VLM 中间隐藏层已含丰富空间信息,自回归解码是轨迹预测的主要瓶颈;提出附加在冻结骨干上的轻量几何兼容预测头,读取中间层特征,以任务指令条件的可学习查询对视觉 token 做交叉注意力,直接回归可供性框与轨迹路点。在 ShareRobot-Bench 和 AGD20K 上,2B 变体轨迹误差降低超过 60%,可供性 mAP 比自回归基线提升 85%,轨迹预测接近 RoboBrain(DFD 0.251 对 0.191),吞吐提高 3.8 倍。
- 🇬🇧 VLMs treat grasp and motion prediction as language generation, autoregressively decoding coordinate tokens, which ignores spatial structure and truncates precision. The authors show 0.5–2B VLMs already encode rich spatial information in intermediate hidden states and that autoregressive decoding is the main trajectory bottleneck; a lightweight head on a frozen backbone reads an intermediate layer, uses an instruction-conditioned learned query with cross-attention over visual tokens, and regresses affordance boxes and waypoints directly. On ShareRobot-Bench and AGD20K the 2B variant cuts trajectory error by over 60% and raises affordance mAP by 85% over the autoregressive baseline, approaches RoboBrain on trajectories (DFD 0.251 vs 0.191) at 3.8× throughput.

### [RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models: Capability, Resource Affordability, and Research Evidence](https://arxiv.org/abs/2610.40026) — (Xin Ma, Furong Chen, Xinlong Man, Bo Zhang 等)
🏷️ 交叉方向 / Also: 世界模型与 WAM / World Models & WAM
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/PrimitiveX/RoboSeed);已用 git ls-remote 验证存在,含评分代码与机器可读证据
- 🇨🇳 选择机器人动作模型需要能力、适配成本、部署需求和结论可靠性的证据,仅看成功率指导有限。RoboSeed 提出面向 VLA 与 WAM 的五维评估框架(能力、下游训练可负担性、部署可负担性、本地验证的研究价值、复现证据),用固定归一化锚点映射到 0–100 档案,提供均衡、训练受限、部署受限三种偏好设置;缺失测量显式保留,不完整的总分被拒绝给出。应用于代表性 VLA/WAM 模型,揭示了预算相关的骨干选择、对适配配方的敏感性以及语言与视觉任务接口的差异;因服务轨迹不全、协议异构,无法给出总体数值排名。
- 🇬🇧 Choosing a robot action model needs evidence on capability, adaptation cost, deployment needs and reliability, and success rates alone guide little. RoboSeed defines a five-dimension framework for VLA and WAM (capability, training affordability, deployment affordability, locally verified research value, reproduction evidence) mapped to 0–100 profiles with fixed anchors under balanced, training-constrained and deployment-constrained preferences; missing measurements stay explicit and incomplete aggregates are withheld. Applied to representative VLA/WAM models it reveals budget-dependent backbone choices, sensitivity to adaptation recipes and language-vs-visual interface differences; heterogeneous protocols preclude overall numerical rankings.

## VLN / VLN

共 3 条,全部展开。 / 3 items, all expanded.

### [MATCH: Execution-Aware Hierarchical Reinforcement Learning for Vision-and-Language Navigation in Continuous Environment](https://arxiv.org/abs/2610.38248) — (Shuhao Ye, Yufei Wei, Demao Wang, Shichao Zhai 等)
🏷️ 交叉方向 / Also: 运动控制·RL(分层 RL 执行器;主要贡献为 VLN 规划-执行联合学习,经自查仍归入本类并注明)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 VLN-CE 需要指令一致的规划与碰撞约束下的可靠执行,许多分层方法只优化规划器而固定执行。MATCH 联合学习语言条件规划器与目标条件原语动作执行器:执行感知拓扑图整合执行器价值估计和已实现结果记忆,使规划器选择执行请求并通过有界连续偏移细化目标;转移感知的稠密宏奖励在沿参考路线的有序进展与执行残差之间权衡;分阶段课程最终同步在线策略更新。仅 0.5B 参数即在 R2R-CE 与 RxR-CE 上达到最优,并有初步真机部署;预印本摘要未给出具体数值。
- 🇬🇧 VLN-CE needs instruction-consistent planning and reliable collision-constrained execution, yet many hierarchical methods optimize the planner while keeping execution fixed. MATCH jointly learns a language-conditioned planner and a goal-conditioned primitive-action executor: an execution-aware topological graph integrates executor value estimates with outcome memory so the planner selects execution requests and refines targets with bounded continuous offsets; a transition-aware dense macro reward balances ordered route progress against execution residual; a staged curriculum ends in synchronized on-policy updates. With 0.5B parameters it achieves state-of-the-art on R2R-CE and RxR-CE with preliminary real-robot deployment; no numbers in the abstract.

### [What Should a Navigator Remember? Spatiotemporal Memory for Zero-Shot Vision-Language Navigation](https://arxiv.org/abs/2610.38318) — (Yuhang Peng, Zhikai Wang, Ziyi Wang, Jiaru Zhong 等)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments(20 pages)无代码链接
- 🇨🇳 零样本 VLN 需要在没有导航专门训练的情况下利用历史观测;作者研究 8B 级导航系统应保留什么信息及如何组织。智能体结合指令进度、以位姿锚定的层次压缩观测历史和累积几何三类记忆:8B 观察器总结观测,8B 推理器据记忆选择路点意图或请求更多视角,几何控制器执行。R2R-CE val-unseen 上完整系统在所评估的 Qwen3 零样本基线中最优;去掉时间记忆使平均路径长度由 16.9 升到 39.1 m;Unitree Go2 在走廊与办公室中成功率高于后训练基线;另提出 LAW2 用成对指令干预评估指令遵循。
- 🇬🇧 Zero-shot VLN must use past observations without navigation-specific training; the authors study what an 8B-scale system should retain and how. The agent combines instruction progress, hierarchically compressed pose-anchored observation history and accumulated geometry as task, temporal and spatial memories; an 8B observer summarizes, an 8B reasoner selects waypoint intents or asks for more views, and a geometric controller executes. On R2R-CE val-unseen it is best among evaluated Qwen3-based zero-shot baselines; removing temporal memory raises average path length from 16.9 to 39.1 m; on a Unitree Go2 it beats a post-trained baseline in corridors and offices, and LAW2 uses paired instruction interventions to assess instruction following.

### [Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory](https://arxiv.org/abs/2610.39446) — (Kai Sheng, Liuyi Wang, Jinlong Li, Haojie Dai 等)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 让具身智能体自主行动、主动交互并从经验中理解环境,需要行动、交互与记忆协同。EvoLife 是统一导航 harness:混合动作空间支持路点导航、局部离散调整、像素导航和目标导向导航;主动交互让智能体在歧义时请求澄清或协助;持久空间记忆把观测和对话绑定到地点。在八个基准、四类任务上,平均每回合仅 1.87 次主动交互,四个各 100 回合的 VLN 与物体导航集合首次访问成功率 100%;LHPR-VLN 50 序列完整序列成功率 98%,GOAT-Bench 50 序列 94%;R2R 重访设置下 SPL 由 82.23% 升到 93.31%;并有多日实体导航验证。
- 🇬🇧 Autonomous embodied agents need action, interaction and memory to work together. EvoLife is a unified navigation harness: a hybrid action space (waypoint, local discrete, pixel-based, object-directed navigation), active interaction to ask for clarification, and persistent spatial memory binding observations and dialogue to places. Across eight benchmarks and four task families it needs only 1.87 interactions per episode on average, reaches 100% first-visit SR on four 100-episode VLN/object-navigation sets, 98% complete-sequence SR on 50 LHPR-VLN sequences and 94% on 50 GOAT-Bench sequences, raises R2R-revisit SPL from 82.23% to 93.31%, and is validated in multi-day physical navigation.

## 世界模型与 WAM / World Models & WAM

候选共 11 条(本期集中在评测/鲁棒性),展开 7 条,其余列名。 / 7 expanded, rest by name.

### [Utility-WAM: Correcting Future-Induced Action Changes](https://arxiv.org/abs/2610.39367) — (Feihong Zhang, Xi Lin, Yulong Shi, Zuxing Lu 等)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 世界-动作模型(WAM)可让动作以生成的视觉未来为条件,但这不是无代价也不一定有益:同一共享检查点下,未来条件对平均成功率几乎无影响(LIBERO +0.8、RoboTwin 2.0 −0.8),推理延迟却增加 1.7–1.9 倍,并在精度任务上出现「未来诱发的负迁移」(Press Stapler 和 Place Can Basket 分别损失 54.0 和 34.0 个点)。Utility-WAM 用残差适配器在冻结共享 WAM 下修复未来诱发的速度偏差,并以预生成门控跳过视频生成。适配器把严重下降降到 6.0 和 14.0 点;门控在 75.5% 的 RoboTwin 查询上跳过视频生成,延迟降低 38%,RoboTwin 2.0 平均成功率 93.3%、LIBERO 98.9%;三项真实双手任务成功 53/60,对比 FAST-WAM 的 43/60。
- 🇬🇧 World Action Models condition actions on generated visual futures, which is neither free nor uniformly beneficial: with a shared checkpoint the future barely shifts average success (+0.8 LIBERO, −0.8 RoboTwin 2.0) yet raises latency 1.7–1.9×, and causes "future-induced negative transfer" on precision tasks (Press Stapler −54.0, Place Can Basket −34.0 points). Utility-WAM adds a residual adapter that repairs future-induced velocity deltas under a frozen WAM plus a pre-generation gate that skips video generation. Losses drop to 6.0 and 14.0 points; the gate bypasses video on 75.5% of RoboTwin queries, cutting latency by 38% with 93.3% on RoboTwin 2.0 and 98.9% on LIBERO; on three real bimanual tasks it succeeds 53/60 versus 43/60 for FAST-WAM.

### [PASA-KV: Attacking Action-Facing Visual Routes in World Action Models](https://arxiv.org/abs/2610.39816) — (Zhongbo Wu, Jiakai Huang, Zheng Zhang, Siyu Xu 等)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 WAM 把内部视觉/世界表示与动作生成耦合,其世界到动作通路的鲁棒性来源不明。作者发现表示可扰动性与闭环脆弱性明显错配:不同视觉 K/V 路径的攻击效果差异很大,更大的表示位移不一定带来更强控制失败,归因于动作条件读出(键决定动作查询读取位置,值决定读到的内容)。据此提出 Tail-AV 短探针信号识别脆弱路径,并在 PASA-KV 中先选取动作面向的 K/V 目标再训练任务共享攻击;多个 WAM 系统及实体机器人上验证了强闭环攻击,并揭示系统间抗攻击差异;预印本摘要未给出具体数值。
- 🇬🇧 WAMs couple internal visual/world representations with action generation, but the robustness of this pathway is poorly understood. The authors find a mismatch between perturbability and closed-loop vulnerability: effectiveness varies sharply across visual K/V routes and larger displacement does not imply stronger failure, attributed to the action-conditioned readout (keys decide where queries read, values what they receive). They propose Tail-AV, a short-probe signal for vulnerable routes, and PASA-KV, which selects action-facing K/V targets before training a task-shared attack; experiments across multiple WAM systems and a physical robot show strong closed-loop attacks and system-level differences in resistance; no numbers in the abstract.

### [PRIME W0: Physical Priors from World Models for Embodied Manipulation](https://arxiv.org/abs/2610.39528) — (Huabin Peng, Fagang Jin, Yancong Wei, Tengfei Ma 等)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 多数 VLA 为前馈结构,仅依据当前观测,丢弃长时域时序上下文和 VLM 表示的层次结构。PRIME W0 是分层条件流匹配框架:(1)预训练 VLM 的逐层 KV 注入到自适应 MoE 动作专家;(2)通过异步世界模型子目标图像预测和 DINOv2 历史帧语义桥实现动力学感知条件;(3)采用协方差结构化噪声、尊重机器人运动学耦合的动作动力学流形(ADM)流匹配。四阶段训练后在 LIBERO 与真机基准上达到最先进结果并有逐组件消融;预印本摘要未给出具体数值。
- 🇬🇧 Most VLAs are feed-forward, conditioning on the current observation and discarding long-horizon context and the hierarchy of VLM representations. PRIME W0 is a hierarchical conditional flow-matching framework with (1) per-layer KV injection from a pretrained VLM into an adaptive-MoE action expert, (2) dynamics-aware conditioning via asynchronous world-model subgoal-image prediction and a DINOv2 historical-frame bridge, and (3) Action Dynamic Manifold flow matching with covariance-structured noise respecting kinematic coupling. After four training stages it reports state-of-the-art results on LIBERO and real-robot benchmarks with ablations; no numbers in the abstract.

### [Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors](https://arxiv.org/abs/2610.40401) — (Liangyu Li, Qingwen Liu)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 CoAWM 学习支持跨本体、跨执行频率动作生成的时空动力学先验,核心是捕捉机器人动作时空结构的共享潜在函数空间。第一阶段函数预训练把不同本体与采样频率的轨迹映射到共同表示,通过动作重构及跨时间采样视角一致性学习共享动力学先验;第二阶段把预训练函数空间接入世界模型骨干,使观测、语言指令和机器人状态条件化预测潜在动作函数,单一解码器接受任意查询时间返回末端动作。预印本摘要未给出定量结果。
- 🇬🇧 CoAWM learns cross-embodiment spatiotemporal dynamics priors for action generation across embodiments and execution frequencies via a shared latent function space of action structure. Stage one maps trajectories from different embodiments and sampling rates into a common representation through action reconstruction and temporal-view consistency; stage two connects it to a world-model backbone so observations, language and robot state condition the prediction of a latent action function, decoded at any query time into an end-effector action. The preprint abstract gives no quantitative results.

### [Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](https://arxiv.org/abs/2610.39232) — (Haitang Feng, Zhuoman Liu, Zhennan Wang, Sheng Wang)
🏷️ 交叉方向 / Also: 空间智能 / Spatial Intelligence
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://gensight-rbs.github.io/)已给出,代码链接未核实
- 🇨🇳 具身世界模型不仅要想象未来,还应感知演化世界的几何、语义与运动。GenSight 把未来视频生成与稠密感知统一到单一预训练视频扩散 Transformer 中,用统一时空表示覆盖视频、深度、本体分割和首帧相对 2D 光流,轻量任务调制在同一架构预测所有模态,并在统一速度预测空间联合优化。支持多步未来视频生成配对稠密预测和单步稠密感知两种模式;在多本体操作数据和人手交互数据上训练,视频生成与稠密 4D 感知均表现强;预印本摘要未给出具体数值。
- 🇬🇧 Embodied world models should both imagine futures and perceive geometry, semantics and motion. GenSight unifies future video generation and dense perception in one pretrained video diffusion transformer with a shared spatiotemporal representation for video, depth, embodiment segmentation and first-frame-relative 2D flow, lightweight task modulation and a unified velocity-prediction objective. It supports multi-step generation with aligned dense predictions and single-step dense perception, trained on multi-embodiment manipulation and human-hand data; the abstract reports strong performance without numbers.

### [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](https://arxiv.org/abs/2610.39278) — (Yuhao Lu, Jiongxu Chen, Hexiang Wei, Jiajin Wu 等)
🏷️ 交叉方向 / Also: 空间智能 / Spatial Intelligence
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://worldflow-rbs.github.io/)已给出,代码链接未核实
- 🇨🇳 现有视频世界模型把 3D 动力学隐含化,基于动作的表述绑定特定机器人,纯光流监督的 3D 运动预测学习信号有限。WorldFlow 是联合预测未来视频与基于查询的 3D 轨迹的生成式世界模型:把 3D 运动参数化为与视频网格对齐的连续位移 token,统一的 MoT 骨干在 rectified-flow 目标下联合去噪两种模态。在 144 万个仿真与真实对象级样本上训练,并提出含 1,678 个样本的 WorldFlowBench;在三个评测集上 ADE/FDE 均为被评估学习方法中最低,SpatialCog 集上 ADE 0.060 m,比最强外部基线降低 54.2%,相对仅光流变体 ADE/FDE 分别降低 55.9% 与 68.5%。
- 🇬🇧 Video world models leave 3D dynamics implicit, action-based formulations are robot-specific, and flow-only 3D motion supervision is limited. WorldFlow jointly predicts future video and query-based 3D trajectories by parameterizing 3D motion as continuous displacement tokens aligned with the video grid, denoised jointly by a Mixture-of-Transformers under rectified flow, trained on 1.44M simulated and real object-level samples with a new 1,678-sample WorldFlowBench. It has the lowest ADE/FDE among evaluated learning methods on all three sets; on SpatialCog ADE is 0.060 m, 54.2% below the strongest external baseline, and 55.9%/68.5% lower in ADE/FDE than its flow-only variant.

### [When More Planning Hurts: Learned Planners for World Models](https://arxiv.org/abs/2610.37891) — (Josef Chen)
开源状态 / Code: ❓ 未知 / Unknown — 摘要称代码、权重、评估器、执行轨迹与成本核算随文提供,但未给出链接
- 🇨🇳 在 PushT 上,作者固定的动作更新器(1,505 参数)在留出的 16 个场景中解出 8 个;对比规划器:选定的 Adam 解出 7 个(总规划+编码时间 218.440 s)、改造的 iCEM 解出 2 个(49.309 s)、已发布的 LePlanner 解出 16 个(5.652 s),作者的更新器耗时 59.079 s,且未满足事先固定的任务代价标准。在另一个匹配实验中,允许下一次求解多做 4、8、12 次更新,16 个上下文中成功数分别为 9、8、7;额外更新没有挽救任何失败任务,在一个场景簇中潜在世界模型轨迹代价下降却使原本成功的任务失败。
- 🇬🇧 On PushT the authors' fixed action updater (1,505 parameters) solves 8 of 16 held-out scenes; comparison planners: selected Adam 7 tasks (218.440 s total planning+encoding), adapted iCEM 2 (49.309 s), released LePlanner 16 (5.652 s), while the updater takes 59.079 s and fails the task-cost criterion fixed before evaluation. In a matched experiment giving the next solve 4, 8 or 12 updates, successes are 9, 8 and 7 out of 16 contexts; extra updates rescued no failing task, and in one scene cluster lower latent-trajectory costs turned prior successes into failures.

**其余 4 条列名(cs.CV/cs.AI 关键词命中,机器人关系较弱)/ Remaining 4 by name:** [WorldProbe](https://arxiv.org/abs/2610.39721)、[L3G-World](https://arxiv.org/abs/2610.40614)、[Generating Critic-Guided Synthetic Experience in Latent World Models](https://arxiv.org/abs/2610.39100)、[GROME](https://arxiv.org/abs/2610.39812)。共 11 条。 / 11 in total.

**另见 / See also:** [HiFOR](https://arxiv.org/abs/2610.40373)、[CoRAct](https://arxiv.org/abs/2610.39543)、[SaiVLA-JEPA](https://arxiv.org/abs/2610.38508)(已归入 VLA);[Explore Where It Matters / TERRA](https://arxiv.org/abs/2610.38657)(已归入 运动控制·RL)。

## 空间智能与 SLAM / Spatial Intelligence & SLAM

共 8 条,全部展开。 / 8 items, all expanded.

### [SKiD-SLAM: Resource-Aware Distributed Multi-Robot LiDAR SLAM for Planetary Missions with Field Deployments at Analog Sites](https://arxiv.org/abs/2610.38141) — SPARO Lab(Hogyun Kim, Juwon Kim, Dongjin Cho, Jiwon Choi 等)
开源状态 / Code: ✅ 已开源 / Released — [项目页](https://sparolab.github.io/research/skid_slam/);摘要称项目页含代码与现场数据,未核实仓库地址(IEEE Transactions on Field Robotics 已发表)
- 🇨🇳 未来行星探索要求机器人团队在通信受限、算力受限、无中心设施下协同建图。该现场报告提出分布式多机器人 LiDAR SLAM 系统 SKiD-SLAM:调研实际行星任务的通信与计算预算后,选择适配预算的机器人间地点识别、相对位姿估计与分布式轨迹融合模块;先在公开数据集与基于 NASA JPL 开源漫游车的模拟器验证,再于济州岛 Majang 熔岩洞(轮式漫游车)和 KICT 行星模拟地形(四足机器人)实地部署。两次部署均在 250 kbps 机器人间通信预算内可靠完成分布式多机器人 LiDAR SLAM。
- 🇬🇧 Future planetary missions need robot teams to map collaboratively under severe communication and compute limits with no central infrastructure. This field report presents SKiD-SLAM, a distributed multi-robot LiDAR SLAM system whose modules for inter-robot place recognition, relative pose estimation and distributed trajectory fusion are chosen to fit surveyed planetary-mission budgets; it is verified on public datasets and a simulator built on NASA JPL's Open Source Rover, then deployed with wheeled rovers in the Majang lava-tube cave on Jeju and with quadrupeds on a planetary analog terrain at KICT. Both deployments ran reliably within a 250 kbps inter-robot communication budget.

### [GOFish: Full Field-of-View Gaussian Splatting and Mesh Extraction](https://arxiv.org/abs/2610.37818) — (Allen Tu, Meher Gitika Karumuri, Shifan Zhu, Hailing Wang 等)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://3dgofish.github.io/)已给出,代码链接未核实
- 🇨🇳 机器人、自动驾驶与 360° 相机使用鱼眼镜头,仿真就绪数字孪生需要全视场真实感渲染与对齐的碰撞网格,但已有鱼眼高斯泼溅只栅格化到 180° 且不产生网格,高斯表面重建方法又假设针孔图像。GOFish 是首个直接在鱼眼图像上训练、可栅格化超过 180° 视场并提取对齐网格的 3DGS 表面重建方法,用校准致密化、校准 Mip 滤波和广角外观建模。在 200° FIORD 与 205° FullCircle 基准上 PSNR 分别比最佳先前方法高 2.28 和 1.97 dB,并在 FIORD 与 ScanNet++ 主集上取得最高网格 F-score。
- 🇬🇧 Robots, vehicles and 360° cameras use fisheye lenses, and simulation-ready digital twins need full-FoV photorealistic rendering plus an aligned collision mesh, but prior fisheye Gaussian Splatting rasterizes only up to 180° without meshes, and Gaussian surface methods assume pinhole images. GOFish is the first 3DGS surface reconstruction method trained directly on fisheye images, rasterizing beyond 180° and extracting an aligned mesh via calibrated densification, calibrated mip filtering and wide-angle appearance modeling. On the 200° FIORD and 205° FullCircle benchmarks it improves PSNR by 2.28 and 1.97 dB over the best prior method and achieves the highest mesh F-score on FIORD and the ScanNet++ main set.

### [Self-Supervised Doppler-Guided RF Odometry](https://arxiv.org/abs/2610.39005) — (Kunzhe Song, Jialuo Du, Jingkai Lin, Huacheng Zeng 等)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments(NeurIPS 2026 接收)无代码链接
- 🇨🇳 射频(RF)感知可在黑暗、烟雾、雾中估计机器人自运动,但多径与移动反射体使跨帧匹配歧义,现有方法依赖惯性传感器或真值位姿监督。RFWalk 是自监督、仅 RF 的里程计:把距离-方位帧之间的稠密对应建模为时空图上的随机游走,用时间循环一致性从无标签序列学习;并引入多普勒一致性损失,用传感器自测径向速度排除循环一致但物理不合理的对应,再经稳健 SE(2) 配准恢复自运动。无位姿标签与辅助传感器下,静态场景与监督基线相当,有行人移动的动态场景中绝对轨迹误差降低 58%。
- 🇬🇧 RF sensing estimates ego-motion in darkness, smoke and fog, but multipath and moving reflectors make cross-frame matching ambiguous, and existing methods use inertial sensors or pose supervision. RFWalk is a self-supervised RF-only odometry framework that models dense range-azimuth correspondences as random walks on a space-time graph learned through temporal cycle consistency, adds a Doppler consistency loss using the sensor's own radial velocity to rule out physically implausible matches, and recovers ego-motion through robust SE(2) registration. With no pose labels or auxiliary sensors it is competitive with supervised baselines in static scenes and cuts absolute trajectory error by 58% in dynamic scenes with pedestrians.

### [3D Occupancy-Language Fields from mmWave Radar](https://arxiv.org/abs/2610.37929) — (Haowen Lai, Zhiwei Zheng, Mingmin Zhao)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 雷达能恢复场景几何并识别预定义类别,但无法提供支持开放式语言查询的持久空间表示。TextRadar 由全景雷达观测构建场景级 3D 占据-语言场,在表面位置结合占据与尺度相关的语言特征;单帧雷达蒸馏模型预测对齐的距离和语言特征,再用雷达估计位姿配准以仅凭雷达重建新场景的场。约 2 万帧同步观测、七栋建筑上的实验展示了场景级自然语言查询与无提示语义可视化;相机到雷达概念迁移分析显示结构、材料与人体姿态一致性高于颜色与印刷文字。
- 🇬🇧 Radar can recover geometry and recognize predefined categories but lacks a persistent representation for open-ended language queries. TextRadar builds a scene-level 3D occupancy-language field from panoramic radar, combining occupancy with scale-dependent language features at surfaces; a single-frame distillation model predicts aligned ranges and language features and radar-estimated poses register them into a field from radar alone. Experiments on ~20k synchronized observations across seven buildings show natural-language querying and prompt-free semantic visualization, with camera-to-radar concept transfer stronger for structures, materials and human poses than for colors and printed text.

### [SpaceAct: Benchmarking 3D Spatial and Temporal Reasoning via Closed-Loop Action and Active Perception](https://arxiv.org/abs/2610.38405) — (Chenglong Shi, Zekai Yuan, Yue Song, Jon Pu)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 现有研究在静态图像上做被动 VQA 或符号规划,不要求执行,也忽略碰撞、静力学与时序。SpaceAct 是通过闭环物理动作与主动感知评估 3D 时空推理的交互式基准,配套 SAPA 智能体框架;基于互锁积木与机械谜题,含 6 类 36 个任务族共 108 个已验证实例,无特权坐标。10 个前沿 MLLM 在 44 个最难实例上得分 4.8–79.1,七个模型最多解出 27.3% 的 6-DoF 任务;对前三名,参考计划(+plan)补上 44% 差距但每回合仍有 5.2 次碰撞,而提供精确 3D 状态(+state)补上 90% 并把碰撞降到 0.5;46% 失败是碰撞或观测循环。结论:即便计划有效,MLLM 仍受 3D 视觉落地和动作精修限制。
- 🇬🇧 Prior work tests passive VQA or symbolic planning without execution, ignoring collision, statics and timing. SpaceAct is an interactive benchmark for 3D spatiotemporal reasoning through closed-loop physical action and active perception, with the SAPA agent framework; it has 108 verified instances across 36 task families in six categories built on interlocking bricks and mechanical puzzles, with no privileged coordinates. Ten frontier MLLMs score 4.8–79.1 on the 44 hardest instances (seven solve at most 27.3% of 6-DoF tasks); for the top three a reference plan closes 44% of the gap with 5.2 collisions per episode while exact 3D state closes 90% and cuts collisions to 0.5, and 46% of failures are collision or observation loops.

### [PhysVLMM: Interaction-Conditioned Physical Belief Maps for Articulated Objects in Robot Scene Maps](https://arxiv.org/abs/2610.40539) — (Dibyendu Ghosh)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 移动机器人要开门开抽屉,但场景地图只记录物体是什么、是否移动过,不记录拉动时如何响应。PhysVLMM 为视觉-语言-运动地图中每个关节部件维护物理信念,含地图更新和查询两个算法:把拉力方向保留为后验而非点估计,把每次拉动的证据以闭式传给地图中未被触碰的相似部件,并以给定风险回答动作是否会成功或拒答。在 18 个家庭的真实门和抽屉上,保留拉动中关节类型识别率 86%(学习型单视图方法 48%),对拉动响应的预测误差比可微仿真低 41%(CRPS 0.323 对 0.544),速度快四个数量级(13 ms 对 230 s);后验把最终位置误差由 0.460 降到 0.270。
- 🇬🇧 Mobile robots must open doors and drawers, but scene maps record what objects are and whether they moved, not how they respond to a pull. PhysVLMM keeps a physical belief for every articulated part with a map update and a query algorithm, retaining the pull direction as a posterior, passing each pull's evidence in closed form to untouched look-alike parts, and answering whether an action will succeed at a stated risk or abstaining. On real doors and drawers in 18 homes it identifies joint type in 86% of held-out pulls (48% for a learned single-view method) and predicts pull response with 41% lower error than differentiable simulation (CRPS 0.323 vs 0.544), four orders of magnitude faster (13 ms vs 230 s); the posterior lowers final-position error from 0.460 to 0.270.

### [Efficacy of Monocular Depth Estimation in Lunar Environments](https://arxiv.org/abs/2610.38080) — (Michael W. Lanighan, Kenji Brameld, Seth Gee)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接(Comments:iSpaRo 2026 接收)
- 🇨🇳 单目深度估计在分布内的地球场景已很准确,但对分布外的月面环境效果未知。作者用 NASA Ames POLAR 立体数据集与 Apollo 17 地表影像评估多种最先进方法,建立「类比到现场」验证流程,以真值物理类比数据做定量评估、以历史现场数据做定性评估。结论:部分最先进技术能泛化到非结构化月面并生成高保真的相对 3D 重建;摘要未给出具体数值。
- 🇬🇧 Monocular depth estimation is accurate in-distribution on Earth but unproven on out-of-distribution lunar scenes. The authors evaluate several state-of-the-art approaches on the NASA Ames POLAR stereo dataset and Apollo 17 surface imagery with an analog-to-field validation pipeline (quantitative against ground-truth analogs, qualitative against historical field data). Select methods generalize to produce high-fidelity relative 3D reconstructions of the unstructured lunar surface; the abstract gives no numbers.

### [A Fast Robot Localization Method Based on Monte Carlo Sampling](https://arxiv.org/abs/2610.39708) — (He Zhaoqing, Hang Li, Xian Pu, Li Wang)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接
- 🇨🇳 受限环境中机器人常无法依赖外部定位系统。该工作提出基于蒙特卡洛采样的在线粒子滤波定位方法,应用于迷宫中的移动机器人,仅需前后左右四个测距传感器、无需任何航向信息。仿真表明即使在局部区域高度相似的迷宫里,小车仍能较准确地定位;预印本摘要未给出定量结果。
- 🇬🇧 Robots in constrained environments often cannot rely on external localization. This paper proposes an online particle-filter localization method based on Monte Carlo sampling for a maze-navigating mobile robot, needing only four range sensors (front, rear, left, right) and no heading information. Simulations show relatively accurate localization even where local regions of the maze are highly similar; the abstract gives no quantitative results.

**另见 / See also:** [TACOS](https://arxiv.org/abs/2610.37806)(已归入 运动控制·传统);[UMI-Live](https://arxiv.org/abs/2610.39385)(已归入 具身智能)。

## 其他值得关注 / Other Notable

今日无需展开的其他条目。硬件/医疗/多机器人等不相关或弱相关 cs.RO 条目未入选,例如 [OmniQuad](https://arxiv.org/abs/2610.38502)(轮足混合机器人硬件)、[CAPTURER](https://arxiv.org/abs/2610.39119)(灵巧空中操作臂)。 / Nothing else expanded; unrelated hardware/medical/multi-robot entries not selected (e.g. OmniQuad, CAPTURER).

**自查 / Self-check:** 已逐条检查优先级 3–7 类别条目。[Gym-Anything](https://arxiv.org/abs/2610.40565)、[Same Label, Different Interface](https://arxiv.org/abs/2610.38104)、[DexSuite](https://arxiv.org/abs/2610.37799) 涉及 RL 环境/动作接口/仿真框架,贡献为环境、评估与数据而非控制算法,已在条目下注明;[MATCH](https://arxiv.org/abs/2610.38248) 含分层 RL 执行器,但主任务为 VLN 规划-执行联合学习,保留在 VLN 并注明。其余条目均不涉及人形/足式 locomotion、全身控制或动作跟踪。 / Categories 3–7 re-checked; borderline items annotated.

## GitHub 动态 / GitHub Highlights

radar 数据日期 2026-10-31,star 基线 2026-10-29(增长为两日增量)。watchlist_releases 为空:过去 48 小时重点项目无新 release。 / Radar dated 2026-10-31; growth is vs the 29 Oct baseline. `watchlist_releases` is empty — no releases for watched projects in the last 48 h.

| 仓库 / Repo | Stars(增长 / Δ)| 说明 / Note |
|---|---|---|
| [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) | 387(+47) | 🇨🇳 SuperMimic 实现/扩展/演示合集(第三方,非官方)。 / 🇬🇧 Curated third-party SuperMimic implementations and demos (unofficial). |
| [leggedrobotics/foothold-prediction-model](https://github.com/leggedrobotics/foothold-prediction-model) | 111(+25) | 🇨🇳 ETH RSL:Watch Your Step 的代码,面向人形 locomotion 的预期感知(运动控制,与「运动控制·RL」相关)。 / 🇬🇧 ETH RSL code for "Watch Your Step: Anticipated Perception for Humanoid Locomotion". |
| [tuotuoLyu/ForesightSafety-VLA](https://github.com/tuotuoLyu/ForesightSafety-VLA) | 80(+78) | 🇨🇳 IROS 2026 的 VLA 安全诊断基准官方代码(新仓库)。 / 🇬🇧 Official code of an IROS 2026 VLA safety diagnostic benchmark (new repo). |
| [tuotuoLyu/FPO](https://github.com/tuotuoLyu/FPO) | 38(+36) | 🇨🇳 视觉-语言流匹配策略的强化微调官方代码(新仓库)。 / 🇬🇧 Official code for RL fine-tuning of flow-matching VLA policies (new repo). |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28,599(+22) | 🇨🇳 LeRobot,日常增长。 / 🇬🇧 LeRobot, steady growth. |
| [deeplethe/utopia](https://github.com/deeplethe/utopia) | 8,644(+21) | 🇨🇳 自称「首个开源企业世界模型」,与机器人世界模型关联有待核实。 / 🇬🇧 Self-described open-source enterprise world model; robotics relevance unverified. |
| [NVIDIA/skills](https://github.com/NVIDIA/skills) | 3,800(+18) | 🇨🇳 面向 NVIDIA 产品的 Agent Skills。 / 🇬🇧 Agent skills for NVIDIA products. |

其余增长榜靠前仓库(gods-eye-view、text-to-cad、RuView 等)与机器人研究关联弱,忽略。新仓库中另有:[keivalya/pico-wam](https://github.com/keivalya/pico-wam)(紧凑 WAM 教学实现,1 star)、[TusharBajaj07/wam-imagination-patching](https://github.com/TusharBajaj07/wam-imagination-patching)(Fast-WAM 想象补丁分析,0 star)、[ApurvK032/pi-wbc](https://github.com/ApurvK032/pi-wbc)(G1 的 PPO 全身控制 + GR00T/π0.5,0 star),均为个人项目。 / Other new repos are individual projects.

## 今日趋势 / Today's Trends

1. **人形/足式控制走向「可提示的冻结基础策略 + 代码层」 / Promptable frozen base policies plus a code layer.** [METATRON](https://arxiv.org/abs/2610.38027) 与 [ELEVATE](https://arxiv.org/abs/2610.38388) 都让 coding agent 在冻结或已有控制器之上用代码/RL 问题合成新技能;[FORGE](https://arxiv.org/abs/2610.37974) 则用降阶参考加全身跟踪覆盖宽指令空间。 / METATRON and ELEVATE let coding agents synthesize new skills on top of frozen or existing controllers via code or RL problem specs, while FORGE pairs a reduced-order reference with whole-body tracking.
2. **动态、高风险的零样本 sim-to-real / Dynamic zero-shot sim-to-real.** [Catch It All!](https://arxiv.org/abs/2610.39044)、[Humanoid Dodgeball](https://arxiv.org/abs/2610.40003)、[事件相机避障](https://arxiv.org/abs/2610.38967)、[SimRetract](https://arxiv.org/abs/2610.38234) 均强调接近硬件极限的零样本部署与安全课程。 / These papers stress zero-shot deployment near hardware limits with safety-aware curricula.
3. **评估与方法学反思 / Methodological self-scrutiny.** [Same Label, Different Interface](https://arxiv.org/abs/2610.38104)、[CuraEval](https://arxiv.org/abs/2610.38221)、[UED 四足基准](https://arxiv.org/abs/2610.40364)、[RoboSeed](https://arxiv.org/abs/2610.40026)、[SaiVLA-JEPA](https://arxiv.org/abs/2610.38508) 都报告「简单基线/未匹配的接口解释了大部分差异」。 / Several papers show simple baselines or unmatched interfaces explain much of the reported gains.
4. **WAM 的代价与脆弱性 / Cost and fragility of WAMs.** [Utility-WAM](https://arxiv.org/abs/2610.39367) 显示未来条件在精度任务上负迁移并增加 1.7–1.9× 延迟,[PASA-KV](https://arxiv.org/abs/2610.39816) 显示世界到动作通路易被攻击。 / Utility-WAM shows negative transfer and 1.7–1.9× latency; PASA-KV exposes attackable world-to-action routes.
5. **SuperMimic 复现热 / SuperMimic reproduction wave.** radar 对 [SuperMimic](https://arxiv.org/abs/2610.28480) 搜到 15 个第三方复现仓库(多为 0–7 star),官方代码仍未出现。 / 15 third-party reproductions found; no official code yet.

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
- **coding agent / agentic(机器人控制)**:适用 arXiv 检索与 GitHub 关键词。 本期 [METATRON](https://arxiv.org/abs/2610.38027)、[ELEVATE](https://arxiv.org/abs/2610.38388)、[Gym-Anything for Robotics](https://arxiv.org/abs/2610.40565) 共 3 篇都以 coding agent 合成控制技能/环境,现有关键词未覆盖。 / Three papers today use coding agents to synthesize controllers or simulators, which current keywords miss.
- **promptable whole-body / motion tracker 开放权重**:适用 arXiv 与 GitHub。 [METATRON](https://arxiv.org/abs/2610.38027) 与 [SONIC-K1](https://arxiv.org/abs/2610.39327) 都围绕通用/可提示人形跟踪器。 / Both papers revolve around general or promptable humanoid trackers.

**建议观察 / Watch**
- **action interface / controller transfer(动作接口与控制器)**:[Cross-Controller Transfer](https://arxiv.org/abs/2610.39280) 与 [Same Label, Different Interface](https://arxiv.org/abs/2610.38104) 同日出现,信号尚弱。 / Two papers today, signal still weak.

**建议移除/收窄 / Remove or Narrow**
- GitHub 搜索词 **SuperMimic**(若用于 new_repos 发现):今日 15 个命中几乎全是个人复现、0–7 star,噪声大;建议保留在监测列表检查而非通用搜索。 / The SuperMimic GitHub search yields mostly 0–7-star personal reproductions; keep it in the watchlist check, not general discovery.

## 开源监测 / OSS Watchlist

| 工作名称 / Work | 加入日期 | 当前状态 | 今日检查结果 | 备注 |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 / Unknown | `signal` = false;candidate_repos 为空;project_page_release_claims 为空;arxiv 最新版本 v1;errors 为空 | 无变化。search_hits 共 15 个第三方复现,如 [XZDang13/supermimic](https://github.com/XZDang13/supermimic)、[NPCLEI/mjlab_supermimic](https://github.com/NPCLEI/mjlab_supermimic)(7 star)、[OpenLegged/supermimic_AMP](https://github.com/OpenLegged/supermimic_AMP),均非官方,不能据此判定已开源。 |

**建议加入监测 / Suggested additions**

1. [METATRON](https://arxiv.org/abs/2610.38027) — 🇨🇳 NVIDIA 的可提示人形全身执行层,真机验证扎实,项目页无代码承诺,值得盯开源。 / 🇬🇧 NVIDIA's promptable humanoid execution layer with solid hardware results; the page makes no code promise, worth tracking.
```json
{"name": "METATRON", "title": "METATRON: A Promptable Whole-Body Execution Layer for Humanoids", "arxiv_id": "2610.38027", "search_terms": ["METATRON", "Metatron humanoid"], "owners": ["NVlabs"], "project_pages": ["https://research.nvidia.com/labs/par/projects/metatron/"], "known_repos": ["NVlabs/ProtoMotions"]}
```
2. [FORGE](https://arxiv.org/abs/2610.37974) — 🇨🇳 Caltech 的降阶参考 + 全身跟踪,G1 上统一覆盖多步态,暂无代码线索。 / 🇬🇧 Caltech's ROM reference + whole-body tracking on G1 across gaits; no code signal yet.
```json
{"name": "FORGE", "title": "FORGE: Feasible Online Reduced-Order Reference Generation and Whole-Body Execution for Agile Humanoid Locomotion", "arxiv_id": "2610.37974", "search_terms": ["FORGE humanoid"], "owners": [], "project_pages": [], "known_repos": []}
```
3. [Catch It All!](https://arxiv.org/abs/2610.39044) — 🇨🇳 G1 单相机零样本动态接球,强 sim-to-real 结果,暂无代码线索。 / 🇬🇧 Zero-shot dynamic catching on G1 with one camera; strong sim-to-real, no code signal yet.
```json
{"name": "Catch It All", "title": "Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand", "arxiv_id": "2610.39044", "search_terms": ["Catch It All", "dynamic catching humanoid"], "owners": [], "project_pages": [], "known_repos": []}
```

**建议移出 / Suggested removals:** 无(SuperMimic 仍未开源)。 / None (SuperMimic still unreleased).
