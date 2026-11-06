# 机器人/具身智能每日速递 — 2026-11-07 / Robotics & Embodied AI Daily — 2026-11-07

## 检查窗口与来源状态 / Window & Source Status

- **窗口 / Window**:台北时间 2026-11-06 07:40 – 2026-11-07 07:40(UTC 2026-11-05 23:40 – 2026-11-06 23:40;周五,无需覆盖周末)。
- **arXiv cs.RO 列表**:[cs.RO new, Fri 6 Nov 2026](https://arxiv.org/list/cs.RO/new) — New 68 + Cross-lists 13 + Replacements 34 = 115 条,全部逐条分类;其中主题相关者已展开或列名(Replacements 仅保留窗口内更新且与主题相关者)。
- **arXiv API 关键词检索**(cs.RO/cs.AI/cs.LG/cs.CV,submittedDate 2026-11-05~06,降序)命中数 / hits:embodied 16;VLA 6;vision-language-action 8;VLN 0;vision-language navigation 0;humanoid 8;legged locomotion 0;whole-body control 0;MPC 0;reinforcement learning robot 0;sim-to-real 2;dexterous manipulation 1;robot foundation model 1;world model 10;world action model 4;WAM 4;video world model 1;spatial intelligence 0;spatial reasoning 3;SLAM 1;visual SLAM 0;LiDAR SLAM 0;gaussian splatting SLAM 0;3D reconstruction 3;motion tracking 0;motion imitation 0。去重后共 45 篇,其中 13 篇不在 cs.RO 列表;这 13 篇中仅 WAM-Sim0.1、FreeOcc(自动驾驶)、PlayGen2、CST-Bench 与主题弱相关,均已在对应类别的列名行中收录,其余为无关内容(医疗、安全、通用 agent 等)。(多个多词关键词 0 命中是因为 API 短语匹配较严,并非请求被拦截。)
- **完整摘要 / Full abstracts**:对所有展开条目通过 arXiv API(id_list,https)取得完整摘要与 Comments,119/119 篇均取到非空摘要。
- **GitHub radar**:`data/latest.json` 的 date_taipei = 2026-11-07(已更新);star 基准 2026-11-05T23:13Z 已存在;new_repos 150 条(counts: 281),star_growth_top 60 条,watchlist_releases 2 条,oss_watch 1 条(signal 全为 false)。
- **Hugging Face Daily Papers API**:本次未单独查询,开源状态以 arXiv Comments、摘要、radar 与项目页为准(注明)。
- **仓库推送权限**:`git push --dry-run` 通过。
- 注:GitHub MCP 无法读取 watchlist 仓库(未授权),release 内容改用 WebFetch 读取发布页。

---

## 今日必读 / Top Picks

1. **[STEP](https://arxiv.org/abs/2611.08097)**(运动控制·RL)— 人形感知 locomotion,真机 98/100 次成功(楼梯、40 cm 平台、70 cm 沟、踏石、倒退上楼)。 / Perceptive humanoid locomotion with 98/100 real-robot successes. ❓
2. **[Terrain-Indexed Motion Priors and Geometric Support for Extreme Humanoid Parkour](https://arxiv.org/abs/2611.08056)**(运动控制·RL)— 三阶段模仿 + 地形索引对抗运动先验,手-膝支撑自适应,真机 29/30 单障碍。 / Staged imitation + terrain-indexed AMP for extreme parkour with hand–knee support. ❓
3. **[GigaBrain-WBC-0.5 (InterTrack)](https://arxiv.org/abs/2608.18234)**(运动控制·RL,v5 更新)— 行为世界模型做带环境交互的全身跟踪,地形交互成功率 81.3%,✅ 已开源。 / Behavior world model for whole-body tracking with terrain interaction; code released. ✅
4. **[Social Humanoid](https://arxiv.org/abs/2611.08407)**(运动控制·RL,CoRL 2026)— G1 上的人-人形交互,260 小时 HHI 基准。 / Human–humanoid interaction on G1 with a 260-hour benchmark. 🕒
5. **[MuJoCo 4.0.0](https://github.com/google-deepmind/mujoco/releases/tag/4.0.0)** 与 **[LeRobot v0.7.0](https://github.com/huggingface/lerobot/releases/tag/v0.7.0)** 同日发布重大版本(详见 GitHub 动态)。 / Major simulator and LeRobot releases landed in the window.

---

## 运动控制·RL / Motion Control · RL

### [STEP: Spatiotemporal Training with Explicit Prediction for Perceptive Humanoid Locomotion](https://arxiv.org/abs/2611.08097) — Noetix 相关团队(Youhao Lyu 等)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 均无代码链接或承诺
- 🇨🇳 感知型人形 locomotion 中,地形几何的相关性取决于机身状态及其随动作的演化,而现有方法只做特征融合,未显式约束跨模态关系与动作相关的状态演化。STEP 是一阶段框架:多个可学习 query 将深度与本体 token 聚合为紧凑策略状态;双向掩码预测用一种模态预测另一种模态的潜特征;动作条件预测器在策略表征空间(EMA 目标)预测下一融合状态。仿真中地形通过率整体优于融合基线与消融,深度丢失/延迟实验证明两种预测目标均有益;23 自由度 Noetix E1 真机在楼梯、40 cm 平台、70 cm 沟、踏石及无后方地形视野的倒退上楼中取得 98/100 次成功。
- 🇬🇧 Terrain relevance in perceptive humanoid locomotion depends on body state and its action-dependent evolution, which pure feature fusion does not constrain. STEP is a one-stage framework: learned queries fuse depth and proprioceptive tokens, bidirectional masked prediction supervises terrain–body relations, and an action-conditioned predictor with an EMA target models next-state evolution in policy space. It improves terrain traversal over fusion alternatives in simulation and under depth dropout and delay. On a 23-DoF Noetix E1 it succeeds in 98 of 100 hardware trials (stairs, 40 cm platform, 70 cm gap, stepping stones, backward stairs).

### [Terrain-Indexed Motion Priors and Geometric Support for Extreme Humanoid Parkour](https://arxiv.org/abs/2611.08056) — Chenghao Sun 等
开源状态 / Code: ❓ 未知 / Unknown — 摘要无链接,无Comments
- 🇨🇳 人类示范的接触模式未必适合机器人的体型与支撑面。本文提出渐进式模仿框架:特权模仿生成可执行的机器人参考,地形索引的对抗运动先验(AMP)引导技能学习,再用几何支撑引导并降低运动先验权重以适配接触(手-膝支撑),不预设接触序列。部署策略仅用机载深度、本体和速度指令,无需外部技能标签。Noetix E1 上仿真混合成功率 96.34%,无需真机微调,29/30 次单障碍与 4/5 条混合赛道成功。
- 🇬🇧 Human demonstrations carry contact patterns that may not suit a robot's proportions. The framework uses privileged imitation for executable references, terrain-indexed adversarial motion priors for skill acquisition, and geometric support guidance with reduced prior weight to adapt hand–knee contacts without prescribing contact order. The policy runs from onboard depth, proprioception and velocity commands. On the Noetix E1 it reaches 96.34% hybrid success in simulation and transfers without real-world fine-tuning (29/30 obstacle trials, 4/5 hybrid courses).

### [GigaBrain-WBC-0.5: A Behavior World Model for Robust Humanoid Whole-Body Tracking with Environment Interaction](https://arxiv.org/abs/2608.18234) — GigaAI(v5 更新)
🏷️ 交叉方向 / Also: 世界模型 / World Model(按规则归入运动控制)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/open-gigaai/giga-brain-wbc);另有[地形数据集](https://huggingface.co/datasets/open-gigaai/GigaBrain-WBC-0.5-TerrainData)和[项目页](https://shepherd1226.github.io/gigabrain-wbc-0.5/);匿名 ls-remote 验证存在
- 🇨🇳 通用动作跟踪器只在平地训练,无法利用地形;跨地形控制器又是任务特定或只接受低维指令。InterTrack 是首个用于带环境交互的鲁棒全身跟踪的行为世界模型(BWM),Transformer 联合预测下一动作、状态与行为分布,并用自动标注管线从重定向动作重建 3D 支撑几何以扩充数据;部署时对环境中不可行的指令"尽力而为"。地形交互成功率 81.3%(最佳基线的 4.3 倍),跌倒恢复率 99.3%,且自由空间跟踪也优于三个主流基线;首次演示人形跨地形实时全身遥操作。
- 🇬🇧 General motion trackers are trained on flat ground and cross-terrain controllers are task-specific. InterTrack, a behavior world model, jointly predicts action, state and behavior distribution with a Transformer, and an automatic pipeline reconstructs 3D support geometry from retargeted motions; infeasible commands are handled best-effort. It reaches 81.3% terrain-interaction success (4.3× the best baseline) and 99.3% fall recovery, beating three tracking baselines, and shows real-time cross-terrain whole-body teleoperation on a humanoid.

### [SONIC-K1: Porting a Universal Humanoid Motion Tracker to a Small Humanoid on a Single GPU](https://arxiv.org/abs/2610.39327) — Kolesnichenko 等(v3 更新)
开源状态 / Code: ✅ 已开源 / Released — [项目页](https://kyry.me/sonic-k1);摘要称代码、策略权重和评测工具公开,但未取得仓库 URL,待核实
- 🇨🇳 问题:将 SONIC 全身动作跟踪框架迁移到更小的 Booster K1 人形且算力有限。方法:在单张共享 GPU 上从零训练,首版真机腿部抖动且对驱动延迟敏感,于是用部署力矩限制、随机驱动延迟和增益随机化做后训练。结果:MuJoCo 中几乎跟踪全部留出片段;后训练的 v1.0 在真机力矩限制与大延迟下保持稳健,可行走转向且不再抖腿;宣称为首个 K1 开放权重全身跟踪器。
- 🇬🇧 The goal is porting SONIC whole-body tracking to the smaller Booster K1 on a modest compute budget. The policy is trained from scratch on one shared GPU; the first release shook its legs and was sensitive to actuation delay, so it was post-trained with torque limits, delay and gain randomization. In MuJoCo it tracks nearly all held-out clips, and v1.0 walks and turns on the real K1 without leg shaking under torque limits and large delays. It is claimed as the first open-weights K1 whole-body tracker.

### [PFM-HR: Pose Flow Matching for Humanoid Robots](https://arxiv.org/abs/2608.03227) — Yukang Gao 等(v4 更新)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 运动先验可改善物理人形跟踪的 RL,但时序先验需要有序片段,姿态先验对策略诱导的姿态转移指导有限。PFM-HR 是在大规模无序姿态数据上训练的可复用 flow matching 先验,并提出姿态几何分数(PGS)衡量 rollout 中关节变化与先验局部几何的一致性,用 PGS 调制跟踪奖励、保持先验冻结。实验表明单动作与通用动作跟踪均有提升,尤其是高动态动作;摘要未给出具体数值。
- 🇬🇧 Temporal motion priors need ordered clips while pose priors give weak guidance for policy-induced transitions. PFM-HR is a reusable flow-matching prior trained on unordered pose data, with a Pose Geometry Score measuring how joint changes align with the prior's local geometry; PGS modulates the tracking reward while the prior stays frozen. It improves single-motion and general motion tracking, especially for highly dynamic motions. The preprint abstract gives no quantitative results.

### [Keeping Jerk in Check: Jointly Trained Perception-Gated Experts for Smooth Terrain Transitions (CTS-MoE)](https://arxiv.org/abs/2606.19633) — Francisco Affonso 等(v2 更新)
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://cts-moe.github.io/)标注 "Code (soon)",暂无仓库
- 🇨🇳 感知式足式 locomotion 的现有方法独立训练专家再用分层选择器或蒸馏组合,地形边界行为不受控。CTS-MoE 将多地形 locomotion 表述为多任务 RL,联合训练感知门控的稠密混合专家 actor 与任务专属 critic,并用并发师生训练把特权地形信息迁移到机载深度,部署时无需地形标签、选择器或蒸馏。连通赛道成功率由 73.3%/53.3% 提升到 93.3%,平均动作 jerk 降低约三分之一;Go1 真机长室外赛道 10/10,迁移到四类室外地形。
- 🇬🇧 Prior perceptive legged locomotion trains specialists independently and composes them via selectors or distillation, leaving terrain-boundary behavior uncontrolled. CTS-MoE frames it as multi-task RL with a jointly trained perception-gated mixture-of-experts actor, task-specific critics and a concurrent teacher–student scheme, so routing is inferred from depth alone. Connected-course success rises to 93.3% from 73.3% and 53.3%, mean action jerk drops by about a third, and a Unitree Go1 completes an outdoor course 10/10 and transfers to four terrain types.

### [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation (WholeBodyMem)](https://arxiv.org/abs/2610.31166) — Chenyuan Chen 等(v2 更新)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/crystalccy1/MemoryBeforeGoal)(匿名 ls-remote 验证存在);[项目页](https://memory-before-goal.github.io)
- 🇨🇳 人形 loco-manipulation 具有非马尔可夫性(线索消失或离开视野),而全身 VLA 策略只看当前帧。WholeBodyMem 用 SAM3 跟踪任务物体,由物体事件因果地选取自适应预算内的关键帧,动作专家通过交叉注意力读取,并提出 HuMeGo 基准(6 个仿真 + 6 个 G1 真机任务)。基础策略成功率仿真 29.1%→72.6%,真机 36.7%→88.3%,标准 SIMPLE 任务 70.2%→86.9%。
- 🇬🇧 Humanoid loco-manipulation is non-Markovian, yet whole-body VLA policies see only the present. WholeBodyMem tracks task objects with SAM3, selects key frames causally from object events under an adaptive budget, and feeds them to the action expert via cross-attention; the HuMeGo benchmark has six simulated and six real Unitree G1 tasks. Success rises from 29.1% to 72.6% in simulation and 36.7% to 88.3% on the real robot, and SIMPLE tasks from 70.2% to 86.9%.

### [PartiGen: Part-Aware Representations for Language-Conditioned Humanoid Motion Generation](https://arxiv.org/abs/2610.13373) — Chuxuan Huang 等(v3 更新)
🏷️ 交叉方向 / Also: 具身智能 / 运动生成(贡献为动作参考生成,配合冻结 GRIT 跟踪器执行)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 语言到人形动作需要协调肢体、确定时长并生成机器人可执行参考。PartiGen 是部位感知潜扩散框架:解剖掩码注意力处理各部位特征并与全身上下文融合,自回归生成动作基元,前向运动学监督保证一致性,并学习结束符预测器。HumanML3D 重定向到 G1 上片段级 FID 3.165(比 TextOp 降低 16.8%),R@1 提高 1.4 个百分点;时长误差由 12.471 降至 3.080 帧;冻结 GRIT 跟踪器在 MuJoCo 中 409/500(81.8%)通过稳定性筛选,真机 27 条尝试中 26 条成功。
- 🇬🇧 Language-to-humanoid motion needs body-part coordination, duration control and robot-executable references. PartiGen is a part-aware latent diffusion model with anatomically masked attention, FK supervision and a learned end-of-sequence predictor. On HumanML3D retargeted to the G1 it reaches segment FID 3.165 (16.8% below TextOp), R@1 +1.4 points, duration error 12.471→3.080 frames; with a frozen GRIT tracker 409/500 references pass the MuJoCo stability screen and 26 of 27 motions succeed on the real G1.

### [Why Koopman Structure Does Not Help Differentiable World Models for Humanoid Whole-Body Tracking](https://arxiv.org/abs/2611.00951) — Haizhou Ge 等(v2 更新)
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅 "8 pages, 3 figures, 2 tables. Preprint"
- 🇨🇳 检验 Koopman 结构是否有助于用反向传播穿过想象 rollout 训练 G1 全身跟踪策略的可微世界模型。结果为否:回报至多持平(0.823 对 0.830),同数据单步误差为 MLP 的 1.3–1.6 倍,训练慢约 15%,提升的 rollout 会发散或无法训练。原因在于该类模型对动作仿射,仅在策略动作处的切线上准确(平均动作处差 31 倍);给模型提供策略动作可去掉大部分差距,在 G1、Ant、Humanoid 上均如此;结论是 MLP 世界模型仍更优。
- 🇬🇧 The paper tests whether Koopman structure helps a differentiable world model used to train a G1 whole-body tracker by backpropagating through imagined rollouts. It does not: return is at best equal (0.823 vs 0.830), one-step error is 1.3–1.6× the MLP's, training is ~15% slower, and lifted rollouts diverge. The action-affine model class is accurate only as a tangent at the policy's operating point (31× worse at the mean action); supplying the policy's action closes most of the gap on G1, Ant and Humanoid. The MLP world model remains the better choice.

### [Social Humanoid: Socially Responsive Human-Humanoid Interaction](https://arxiv.org/abs/2611.08407) — Vongani H. Maluleke 等(CoRL 2026)
🏷️ 交叉方向 / Also: 具身智能(运动生成 + 数据集)
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://von31.github.io/social-humanoid/)标注 "Code Soon"、"Data Soon",无仓库
- 🇨🇳 人形机器人通常作为孤立智能体训练,无法与会预判并调整的人类伙伴物理协调。Social Humanoid 是分层系统:高层用共享 token 表示对人和人形运动做序列建模,生成反应式动作并在伙伴被遮挡时预判其动作,低层是全身跟踪控制器,在 29 自由度 Unitree G1 上执行;并提出两阶段自适应重定向,将一方重定向到机器人、另一方形变以保持接触、可达性与相对体型。跨五个动捕数据集构建 260 小时 HHI 基准;仿真与真机均展示出协调、与人对齐的行为(摘要未给出其他定量指标)。
- 🇬🇧 Humanoids are usually trained as solitary agents and cannot physically coordinate with partners. Social Humanoid is hierarchical: a high-level policy models human and humanoid motion in a shared token space (reactive generation, anticipating occluded partners) and a low-level whole-body tracking controller runs it on a 29-DoF G1. A two-phase adaptive retargeting procedure preserves contact, reachability and body scale, yielding a 260-hour HHI benchmark from five mocap datasets. It produces coordinated behavior in simulation and the real world; the abstract gives no other quantitative metrics.

### [HITCH: Teaching a Vision-Language Model to Operate a Humanoid through a Whole-Body Harness](https://arxiv.org/abs/2611.08039) — Qingzhou Lu 等
🏷️ 交叉方向 / Also: VLA / 具身智能(VLM 作为高层;学习式全身跟踪器为执行层)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://hitch.axell.top/)抓取仅得标题,未见代码链接
- 🇨🇳 让 VLM 控制人形需要可靠的全身接口与可跨任务迁移的身体使用知识。HITCH 的 harness 让感知返回 VLM 所选图像点的 3D 位置,执行层用学习式跟踪器把骨盆、躯干、手、行走和注视指令变为全身运动;随后用教师策略通过 HITCH 解决五个基础任务的轨迹微调 VLM。无任务轨迹时在 SIMPLE 和 HumanoidArena 上分别完成 51% 和 42.5%,每个 SIMPLE 任务加 5 条轨迹后 SIMPLE 达 95%;真机 G1 无真实训练数据即可搬箱并走到目标。
- 🇬🇧 VLMs controlling humanoids need a reliable whole-body interface and transferable body-use knowledge. HITCH returns 3D positions for any image point the VLM picks and converts pelvis, torso, hand, walking and gaze commands into whole-body motion with a learned tracker; a VLM is then fine-tuned on teacher trajectories from five base tasks. Without task data it completes 51% of SIMPLE and 42.5% of HumanoidArena episodes, rising to 95% on SIMPLE with five extra trajectories per task; on a real G1 it carries a box to a goal with no real training data.

### [PhySA: Decoupling Aesthetic and Physical Rewards for Humanoid Locomotion](https://arxiv.org/abs/2611.07679) — Yunwan Fu 等(CoRL 2026 R2RL Workshop)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 无平滑目标训练的人形策略步态抖动、高能耗,而 VLM 美学评分与物理平滑性方向相反(四个 VLM 上关节加速度与分数的平均 Pearson r=+0.66)。PhySA 将二者放在独立可移除的奖励通道:稀疏异步 VLM 评分与根据仿真状态调节物理惩罚权重的相位触发修正通道。MuJoCo Humanoid-v5 2.6M 步时关节加速度比 PPO、Text2Reward、Eureka 降低 26–32%(三个种子,代价是回合变短);单次长跑比 Prompt2Policy 降 59.5%,但三种子复现仅降 7.2%且不显著;增益无法迁移到 IsaacLab 或 Unitree G1。
- 🇬🇧 Humanoid policies without smoothness objectives gait jerkily, and VLM aesthetic scores correlate positively with joint acceleration (mean Pearson r=+0.66 across four VLMs). PhySA keeps a sparse asynchronous VLM score and a phase-triggered physical-penalty correction on separate, removable channels. On MuJoCo Humanoid-v5 at 2.6M steps it cuts joint acceleration 26–32% vs PPO, Text2Reward and Eureka (three seeds, shorter episodes); one long run gives −59.5% vs Prompt2Policy but a three-seed replication gives a non-significant −7.2%, and the gain does not transfer to IsaacLab or the Unitree G1.

### [LMGN: A Unified Policy Learning Model for Last-Mile Grasp-Navigation](https://arxiv.org/abs/2611.07515) — Xuenmin Hu 等
🏷️ 交叉方向 / Also: 具身智能(导航 + 抓取)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 带机械臂四足机器人现有方法分别处理全局导航与操作,忽视"最后一公里"的底座摆放、接近方向与抓取联合决策。LMGN 引入显式距离与方向可达性表示(ED-DR),语义对齐的分层混合专家(HMoE)策略建模底座调整、预抓取对齐、抓取与抬升阶段,并提出联合对齐导航与操作、阶段专家路由和动作一致性的优化方法。在 Habitat 和 Isaac Gym 的大量实验中一致优于现有方法;摘要未给出具体数值。
- 🇬🇧 Legged manipulators lack joint reasoning over base placement, approach direction and grasp execution in the last-mile phase. LMGN adds an explicit distance-and-direction reachability representation (ED-DR), a semantically aligned hierarchical mixture-of-experts policy over base adjustment, pre-grasp alignment, grasp and lift, and an optimization aligning navigation, manipulation, expert routing and action consistency. It consistently beats state-of-the-art methods on Habitat and Isaac Gym; the abstract gives no numbers.

### [Efficient Diffusion Policy Fine Tuning with Latent Noise Representation Bridging (LARBRID)](https://arxiv.org/abs/2611.07275) — Yuanchu Liang 等(NeurIPS 2026)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/Maincode-Research/LARBRID)(匿名 ls-remote 验证存在)
- 🇨🇳 用 RL 微调预训练扩散/流策略代价高、样本效率低、缺乏理论保证;微调初始噪声的方法存在"噪声混叠"(噪声空间价值与动作空间价值无自然联系)。作者提出潜噪声线性 MDP(LNL-MDP)及桥接方程,通过共享表示对齐两空间价值,具有 FineTuneRL 近最优保证,算法 LARBRID 学习表示以优化初始分布。在机器人 locomotion 与操作任务上最多取得 2–3 倍性能提升。
- 🇬🇧 RL fine-tuning of diffusion/flow policies is costly and lacks guarantees, and noise-initial fine-tuning suffers noise aliasing. The Latent Noise Linear MDP and its Bridge Equation align noise- and action-space values through a shared representation with near-optimal FineTuneRL guarantees; LARBRID learns this representation to steer the initial distribution. It yields up to 2–3× performance gains across robotic locomotion and manipulation tasks.

### [Latent RL Priors for Data-Efficient Dexterous Manipulation](https://arxiv.org/abs/2611.08458) — Yixiao Wang, Mustafa Mukadam 等
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://yixiaowang7.github.io/latent-rl-prior-page/)称 "Code coming soon",并写明 "Will be released, as stated in the manuscript"
- 🇨🇳 从有限视觉示范学灵巧操作既要感知又要精细控制,而仿真 RL 能借助特权信息获得丰富控制行为。Latent RL Prior 分两阶段:特权预训练将大规模 RL rollout 蒸馏为条件于本体和潜任务上下文的 flow-matching 动作解码器;视觉适配时冻结解码器,仅用动作监督学习从图像到潜上下文的视觉接口,同一解码器还可跨手臂共享做双臂操作。三个仿真任务低数据下优于全参数微调的 π0.5 与 GR00T N1.7;开门抬起与双臂装配分别用 10 倍和 5 倍更少示范超越全数据基线。
- 🇬🇧 Visual dexterous policies need both perception and precise control, while privileged simulation RL supplies rich control behavior. Latent RL Prior distills RL rollouts into a flow-matching action decoder conditioned on proprioception and latent task context, then freezes it and learns an image-to-latent interface from action supervision only; the decoder can be shared across arms for bimanual tasks. In three simulated tasks it beats full fine-tuning of π0.5 and GR00T N1.7 in the low-data regime and surpasses full-data baselines with 10× and 5× fewer demonstrations on door lifting and bimanual assembly.

### [TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation](https://arxiv.org/abs/2611.07881) — Yijiong Lin 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 含剪切的触觉仿真对接触丰富操作很重要,但软体仿真太慢,难以支撑大规模 RL。TactileLab 基于 IsaacLab,用刚体仿真估计接触面切向运动,生成"仿真触觉流"并与接触深度场互补,同时提出联合处理长时程本体信号与触觉观测的策略架构;还提出把真实触觉图像流映射到仿真触觉流/深度场的 real-to-sim 转换及数据采集方法,覆盖多种传感器。多个接触丰富任务中策略可规模化高效学习并涌现接触感知行为,真机展示双臂与灵巧手内操作;摘要未给出具体数值。
- 🇬🇧 Shear-aware tactile simulation matters for contact-rich manipulation, but soft-body simulation is too slow for large-scale RL. TactileLab, built on IsaacLab, estimates tangential contact motion with rigid-body simulation to produce simulated tactile flow plus a contact depth field, with a policy architecture for proprioception and tactile streams and a real-to-sim tactile translation method across sensor designs. Policies learn efficiently at scale with emergent contact-aware behavior and are deployed on real dual-arm and in-hand dexterous tasks; no numbers are given in the abstract.

### [An Empirical Study of Reinforcement Learning for Keypoint Positioning of Deformable Linear Objects](https://arxiv.org/abs/2611.07261) — Vinay Rodrigues 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 可变形线性物体(DLO)操作难建模且数据密集。本文研究单端抓取平面 DLO 的 RL,比较三套 PPO 训练栈,发现 GPU 并行的 MuJoCo Playground 在同等时间下收敛更快更稳;相对关键点观测与非对称 actor-critic 进一步提升效率。带噪声、延迟、域随机化与扰动训练的策略仿真成功率:单点跟踪 96.4%、扰动恢复 98.0%、双点跟踪 88.8%;用无标记 RGB-D 关键点估计零样本迁移真机,分别为 9/10、10/10、8/10。
- 🇬🇧 DLO manipulation is hard to model and data-hungry. The study compares three PPO stacks (GPU-parallel MuJoCo Playground converges fastest and most consistently) and shows relative keypoint observations and asymmetric actor-critic help. With noise, delay, domain randomization and disturbances, simulation success is 96.4% (single point), 98.0% (disturbance recovery) and 88.8% (two points); zero-shot real transfer with markerless RGB-D succeeds 9/10, 10/10 and 8/10.

### [Semantics-to-Contact: A Stagewise Framework for Robust Contact-Rich Manipulation (S2C)](https://arxiv.org/abs/2611.07532) — Guanren Qiao 等(NeurIPS 2026)
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://edem-ai.github.io/S2C/)标注 "Code (soon)"
- 🇨🇳 真实世界 RL 常对训练场景外观过拟合。S2C 分两阶段:VLM 在视觉多样场景中定位任务相关区域给出粗略空间引导;随后真实世界人在回路的残差 RL 在该区域内用力反馈学习精细接触行为,并用保留机器人和任务物体、随机化背景的以物体为中心增强。六个真实接触丰富操作任务上持续优于强基线,在显著视觉与位置变化下保持可靠;摘要未给出具体数值。
- 🇬🇧 Real-world RL tends to overfit training-scene appearance. S2C first uses a VLM to localize task-relevant regions, then a human-in-the-loop residual RL policy learns fine contact behavior with force feedback inside that region, plus object-centric background randomization. On six real contact-rich tasks it consistently beats strong baselines and stays reliable under large visual and positional variations; the abstract gives no numbers.

### [Training-Independent Validation of a Learning-Based Controller for Stunt Maneuvers (G-Maneuver)](https://arxiv.org/abs/2611.07516) — Kiruthiga Chandra Shekar 等
开源状态 / Code: ❓ 未知 / Unknown — 仅有[演示视频](https://youtu.be/dN1Oes8pNIo)
- 🇨🇳 学习式车辆机动控制器通常在训练条件与目标下验证,看起来非常可靠,但真实道路上变化的参数并非训练时所见。论文主张验证应独立于训练:改变训练中固定的物理参数并采用训练目标之外的验收准则。对成功率 90.11% 的 G-Maneuver 测试发现,较宽松的末端航向评分会把最差设置排为最佳;用 Sim2Real2Sim 回路选择安全区后实车试验接受率为 16.9%;航向变化、侧滑、归一化横摆率等运动学指标仿真与真实一致,而力和侧倾指标不一致。
- 🇬🇧 Learned vehicle controllers are usually validated under their training conditions and objectives. The paper argues validation must vary parameters fixed during training and use criteria absent from the training objective. For G-Maneuver (90.11% success), a looser heading score ranks the worst setting best; a Sim2Real2Sim loop selects safe zones for real trials with 16.9% acceptance, and kinematic indicators (heading change, sideslip, normalized yaw rate) match between simulation and reality while force and roll indicators do not.

**未展开的更新条目 / Updated papers not expanded**(未见其更新内容的证据,不属本类实质更新):[DenseReward](https://arxiv.org/abs/2607.13033)、[VIGOR](https://arxiv.org/abs/2610.02801)、[AnyDexRT](https://arxiv.org/abs/2607.08341)(radar 新仓库 [chenxi-wang/anydexrt](https://github.com/chenxi-wang/anydexrt),3 star)、[CoDiMAD](https://arxiv.org/abs/2607.09587)、[World Models as Adversaries](https://arxiv.org/abs/2607.10630)。共 5 篇。

---

## 运动控制·传统 / Motion Control · Classical

### [CRISP: Constraint-Resolved Interactions between Subsystems for Predictive Whole-Body Cooperation](https://arxiv.org/abs/2611.07268) — Dario Valenzuela, Jeeseop Kim
开源状态 / Code: ❓ 未知 / Unknown — Comments:7 pages, 8 figures
- 🇨🇳 高维人形动力学下的动态双臂协同操作难以统一建模。CRISP 将人形分解为躯干单刚体(SRB)与手臂、下肢浮动基模型,肩部刚性连接及协同操作时的闭链用完整约束表示,拉格朗日乘子参数化交互力旋量;高层 NMPC 联合优化各子系统轨迹、手臂力矩、地面反力(GRF)和交互力旋量,手臂力矩直接执行,GRF 映射为下肢关节力矩。仿真和 G1 真机验证:交互力旋量与仿真接触测量一致,可在线运行 NMPC 实现双臂协同轨迹跟踪与稳定全身协调。
- 🇬🇧 Dynamic dual-arm cooperation on a humanoid is hard to model monolithically. CRISP decomposes the robot into a torso single rigid body plus floating-base arm and lower-body models, with holonomic constraints for shoulder links and the closed end-effector chain whose multipliers parametrize interaction wrenches. A high-level NMPC jointly optimizes subsystem trajectories, arm torques, GRFs and wrenches; arm torques are applied directly and GRFs are mapped to leg joint torques. Simulation and G1 hardware show wrenches consistent with measured contact, cooperative trajectory tracking and stable whole-body coordination with online NMPC.

### [ZipDrift: Generating Multimodal Short-Horizon MPC Costs with One-Step Drifting Models](https://arxiv.org/abs/2611.05793) — Ke Zhang(v2 更新)
开源状态 / Code: ❓ 未知 / Unknown — Comments:Preliminary simulation study
- 🇨🇳 短视野 MPC 快但近视;ZipMPC 学习代价修正去模仿长视野专家,但最优修正常是多模态的,确定性回归会平均模态。ZipDrift 训练一步"漂移"生成器产生 MPC 代价修正,偏向低闭环代价、仅用候选修正的代价评估学习(不穿过优化器求导),少量候选由学习的 critic 排序,仍由基于模型的 MPC 保证动力学与约束。运动学超车基准上超过半数上下文为双峰,手工短视野 MPC 在 28% 中碰撞;8 个候选的 ZipDrift 碰撞率 0.74%,对比理想 ZipMPC 式回归器 3.4%、critic 排序随机候选 2.1%、MDN 0.76%;单样本时漂移 8.7% 对 MDN 13.2%。候选很多时所有方法都会因 critic 误差被利用而退化。
- 🇬🇧 Short-horizon MPC is fast but myopic, and the optimal cost correction is often multimodal so regression averages modes. ZipDrift trains a one-step drifting generator over MPC cost corrections tilted toward low closed-loop cost, learned only from cost evaluations; a learned critic ranks a few candidates and MPC still enforces dynamics and constraints. In a kinematic overtaking benchmark where over half the contexts are bimodal and manual MPC crashes in 28%, eight candidates give 0.74% crashes vs 3.4% (ZipMPC-style regressor), 2.1% (random critic-ranked) and 0.76% (MDN); a single sample crashes 8.7% vs 13.2% for the MDN. All methods degrade with many candidates as the critic is exploited.

### [A Unified Fractal Impedance Control Framework](https://arxiv.org/abs/2611.08009) — Adnan Takriti 等
开源状态 / Code: ✅ 已开源 / Released(部分)— 摘要称提供含 ROS2、MuJoCo 与真机集成的开源软件套件,但未给出仓库链接,待核实
- 🇨🇳 物理人机交互需要本质有界的交互控制;分形阻抗控制器(FIC)已证明可按设计保证安全特性。本文给出其最先进架构 H-PMP(Harmonic-Passive Motion Paradigm)的机器人实现与实验验证,以及统一的 FIC 部署框架。在 Kinova Gen3 上做轨迹跟踪、墙面按压并突然失去接触、示教学习三个实验,与早期 FIC 架构比较,H-PMP 在导纳与阻抗行为间无缝权衡且无额外计算开销;摘要未给出定量数字。
- 🇬🇧 Physical human–robot interaction needs controllers with intrinsically bounded interaction; the Fractal Impedance Controller has proven safety by design. This paper presents the robotic implementation and validation of its most advanced architecture, the Harmonic-Passive Motion Paradigm, plus a unified deployment framework with an open-source suite (ROS2, MuJoCo, hardware). On a Kinova Gen3 across trajectory tracking, a wall press with sudden contact loss and learning from demonstration, H-PMP trades off admittance and impedance seamlessly with no computational overhead; no numbers are given.

### [Fault-Geometry-Aware Control Allocation for Emergency Quadrotor Landing under Single-Motor Loss of Effectiveness](https://arxiv.org/abs/2611.08259) — Suhas S P 等
开源状态 / Code: ❓ 未知 / Unknown — Comments:6 pages
- 🇨🇳 单电机部分失效会改变剩余控制权限几何,进而改变最佳控制分配器。作者在 Crazyflie SIL 仿真中比较有界加权最小二乘(PINV)、有限候选残差分配器(QP-lite)及用 CEM 离线调参的版本。η=0.496 时按电机选择分配器并冻结路由,新种子上 117/120 安全首次触地,集成监督器随机顺序评估 115/120;±10% 单因素扰动使 η50 最多偏移 0.05495(推力系数)和 0.04974(质量),固定 η 时 PINV 在 9/11 个受测状态下安全数更高。结论:区分电机条件化分配器选择与对模型失配的敏感性。
- 🇬🇧 Single-motor loss of effectiveness changes control-authority geometry and the best allocator. In Crazyflie SIL, bounded weighted least squares (PINV), a finite-candidate residual allocator (QP-lite) and a CEM-tuned variant are compared. After freezing a motor-conditioned routing map at η=0.496, 117/120 fresh-seed landings and 115/120 integrated-supervisor landings are safe; ±10% plant perturbations shift η50 by up to 0.05495 (thrust coefficient) and 0.04974 (mass), and PINV beats frozen CEM in 9/11 tested plant states at fixed η. The study separates allocator selection from plant-mismatch sensitivity.

### [Unified Overview of Safety Certificate Functions: Techniques from Hamilton–Jacobi Reachability and Control Barrier Functions](https://arxiv.org/abs/2611.07537) — Hao Wang, Max Cohen 等
开源状态 / Code: ❓ 未知 / Unknown(教程/综述类)
- 🇨🇳 内容:安全证书综合方法分散在各研究领域,缺少选用指导。本教程以 HJ 可达性与控制障碍函数(CBF)两大族为中心,介绍一般形式、经典与学习式综合工具,并设计两个不同复杂度的车辆系统基准,比较各方法的证书质量与安全关键控制效果,给出实用选型建议。结论:提供两类方法的统一对照与选择指导;摘要未给出定量结果。
- 🇬🇧 Content: safety-certificate synthesis methods are scattered across fields. This tutorial treats HJ reachability and control barrier functions, covering formulations and classical and learning-based synthesis tools, and compares methods on two vehicle benchmarks of differing complexity. Conclusion: it offers practical guidance for choosing an approach; the preprint gives no quantitative results.

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models(展开 7 / 另列 13)

### [RoboARCade: Benchmarking Agentic Robot Control](https://arxiv.org/abs/2611.08209) — Satvik Sharma, Hengyuan Hu 等
开源状态 / Code: ✅ 已开源 / Released — 摘要称代码、视频与完整 trace 在 roboarcade.org;未取得仓库 URL,待核实
- 🇨🇳 多模态 agent 可直接充当机器人策略(agentic robot control, ARC),需要评测其情境适应、记忆与推理。RoboARCade 基于现有开源基准、拓宽初始条件,覆盖三种本体的长时程操作任务,全部在 MuJoCo 单一后端运行。领先 agent 得分 GPT-6 Astra 49.8%、Claude Fable 5.1 为 43.6%;更丰富的视觉接口仅增加 1.5–6.8 点却贵 1.7–2.3 倍;失败多为策略选择差或执行不精确,24%–39% 的子任务被错误宣称成功;一次上下文示范可使 Astra 在五任务子集由 53.5% 升至 73.0%。
- 🇬🇧 Multimodal agents can act directly as robot policies (agentic robot control). RoboARCade offers harder long-horizon manipulation tasks across three embodiments on a single MuJoCo backend. GPT-6 Astra scores 49.8% vs 43.6% for Claude Fable 5.1; a richer visual interface adds only 1.5–6.8 points at 1.7–2.3× cost, failures are mostly poor strategy or imprecise execution, and agents falsely claim success on 24–39% of subtasks. One in-context demonstration lifts Astra from 53.5% to 73.0% on a five-task subset.

### [MessyNav: Zero-Shot Navigation via Manipulation in Messy Environments](https://arxiv.org/abs/2611.07417) — Kenneth Llontop 等(CoRL 2026)
🏷️ 交叉方向 / Also: VLN/导航
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 真实环境杂乱,路径常被椅子、玩具堵住,现有方法依赖大量仿真学习或逐场景指令,难以泛化到易碎推车 vs 空推车等情境。MessyNav 将其表述为开放世界交互导航,在任务规划前先做基于 VLM 的可供性推理,决定扫开、拾起或避开,再产生高层计划。在移动操作机器人的室内外真机中成功率比最强基线高 27 个百分点,更大规模离线评估也显著提升,且无需任务特定训练。
- 🇬🇧 Cluttered real environments block paths, and existing methods need heavy simulation learning or per-scene instructions. MessyNav formalizes open-world interactive navigation and performs VLM affordance reasoning (swipe, pick up or avoid) before planning. On a mobile manipulator in real indoor and outdoor scenes it improves success by 27 percentage points over the strongest baseline, with significant gains in larger offline evaluation and no task-specific training.

### [VREgo: Consumer VR Headsets for Learning Robot Manipulation from Egocentric Demonstrations](https://arxiv.org/abs/2611.07272) — Liuchuan Yu
开源状态 / Code: ✅ 已开源 / Released — 摘要称 VREgo 可在 vrego.chuange.org 获取;未取得仓库 URL,待核实
- 🇨🇳 用消费级 VR 头显(PICO 4 Ultra)记录示范训练操作策略,基于 EgoKit 与 HumanEgo 预处理(逐录制估计抓取阈值、释放后更新物体位置、关键帧间传播掩码)。仿真两个桌面任务:40 条示范下放置方块成功 67/74/60(三个种子,每种子 100 个布局),Aria 为 73/78/0;堆叠任务基线 94/100 放第一块但两次放置仅 2 次。调整轨迹并加入使用仿真物体位置的任务规则后,四个噪声种子下 93.8% 的回合满足两次放置准则(规则开发与评估使用同一批 100 个布局)。
- 🇬🇧 VREgo trains manipulation policies from demonstrations recorded on a consumer VR headset (PICO 4 Ultra) using EgoKit and an adapted HumanEgo pipeline. With 40 demonstrations, PICO policies place the cube in 67, 74 and 60 of 100 layouts across three seeds (Aria: 73, 78, 0); for stacking, the baseline places the first block in 94/100 but both in only 2. After trajectory adaptation and task rules using simulator object positions, 93.8% of episodes meet both criteria across four noise seeds, though the same 100 layouts informed rule development and evaluation.

### [Embodied RAG++: Retrieval-Augmented Generation From What Exists to What Works in Embodied Scenes](https://arxiv.org/abs/2611.07517) — Fan Yang 等(SII 2027)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 场景图记录物体及位置,但常缺少仅在产品手册中的能力信息,现有 RAG 也难以联合推理物体能力、实例、机器人状态与动态连通性。论文提出 E2W-Bench,把动态混合场景图与真实产品手册关联,评估满足可用性、移动性、垂直可达与接口约束的能力-机器人-物体分配;并提出 Embodied RAG++:检索限定在候选物体手册、按产品型号缓存能力、用确定性空间推理判定可行性。E2W-Bench 上配对准确率 Qwen2.5-32B 为 0.90、Llama3.3-70B 为 1.00,基线至多 0.30 和 0.55,预处理时间最短之一。
- 🇬🇧 Scene graphs omit capabilities documented only in product manuals, and RAG rarely reasons jointly over capabilities, instances, robot states and connectivity. E2W-Bench links dynamic hybrid scene graphs with real manuals to test capability-grounded robot–object assignment, and Embodied RAG++ scopes retrieval to candidate objects' manuals, caches capabilities per model and resolves feasibility by deterministic spatial reasoning. Pair accuracy reaches 0.90 (Qwen2.5-32B) and 1.00 (Llama3.3-70B) vs at most 0.30 and 0.55 for baselines.

### [Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement](https://arxiv.org/abs/2611.08318) — Wenbo Huang 等
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://dagroup-pku.github.io/PyRUA-Lean/RSIJudge);radar 中相关仓库 [DAGroup-PKU/PyRUA-Lean](https://github.com/DAGroup-PKU/PyRUA-Lean)(213 star,+14)是否对应本文待核实
- 🇨🇳 自我改进的具身 agent 常把基准成功准则暴露给学习者(Criteria Exposure, CE),而这些准则常比语言指令要求更多。受控实验显示,有 CE 时 agent 在给定准则下很快得到更高成功率,但准则稍作改动(不偏离指令)后优势消失,所学技能跨任务迁移差。作者提出忠实于指令的准则,更能反映 agent 生成程序的真实表现;摘要未给出具体数值。
- 🇬🇧 Self-improving embodied agents often see the benchmark's success criteria (Criteria Exposure, CE), which demand more than the instructions. Controlled experiments show CE agents quickly gain under the given criteria, but the advantage vanishes when criteria are slightly altered and skills transfer poorly across tasks. Instruction-faithful criteria are proposed and better reflect agent-generated program performance; no numbers are given.

### [Closed-Loop Physics-Based Manipulation Evaluation at a Commodity Price](https://arxiv.org/abs/2611.07441) — Rohun Kshirsagar, Diana Rypkema(IROS 2026 Workshop)
开源状态 / Code: ❓ 未知 / Unknown — 摘要称"可复现评测 harness",未给链接
- 🇨🇳 接触丰富操作的大规模评测一直只有资源充足的实验室能做。作者提供可复现评测 harness 包装器,在无服务器商用 GPU 上做 200 次 rollout 规模的评测,约 3.50 美元、每次复现 38 分钟(8 个并行分片共 4.4 L4-GPU 小时)。稀疏数据下的负面结果:三个分块(chunked)检查点在 780 次 rollout 中零次真正成功,三个单步检查点成功率 2.6%–11.8%;逐步重规划对照表明失败定位于训练形式与多步预测,而非开环块执行。
- 🇬🇧 Statistically meaningful contact-rich manipulation evaluation has been limited to well-resourced labs. The authors provide a reproducible harness on serverless commodity GPUs: 200-rollout evaluation for about $3.50 and 38 minutes (4.4 L4-GPU-hours across 8 shards). A negative result: three chunked checkpoints yield zero genuine successes in 780 rollouts versus 2.6%–11.8% for three single-step checkpoints, and a per-step-replanning control localizes failure to the training formulation and multi-step prediction.

### [Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents](https://arxiv.org/abs/2611.07825) — Jisen Lei, Huizhi Liang(ECC 2026)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 目标解释需把自然语言指令转成规划器可执行的形式化符号目标,错误会传导到后续所有规划与动作。作者提出两阶段方法:监督微调让 LLM 适应 EAI 输出规范,再用 Candidate-Output Ranking from Errors(CORE)从模型自身生成的候选中学习完整输出偏好。在 Embodied Agent Interface 基准家庭场景上,对 DeepSeek-V3、DeepSeek-Reasoner、Qwen2.5-7B/72B 等多个开源 LLM,优于简单提示、思维链与知识图谱基线;摘要未给具体数值。
- 🇬🇧 Goal interpretation turns instructions into formal symbolic goals, and errors propagate through planning. A two-stage approach fine-tunes an LLM to the EAI output convention and then learns preferences over complete outputs from its own alternatives (CORE). On the household scenes of the Embodied Agent Interface benchmark it beats prompting, chain-of-thought and knowledge-graph baselines across several open-source LLMs; no numbers are given.

另列 / Also listed(13):[GraspBench](https://arxiv.org/abs/2611.07651)、[Time-Indexed Skill Success Models](https://arxiv.org/abs/2611.07964)、[Dual-Arm Tabletop Rearrangement](https://arxiv.org/abs/2611.07726)、[AffordJEV](https://arxiv.org/abs/2611.07896)、[Fast and Reliable Open-Vocabulary Object Search](https://arxiv.org/abs/2611.07493)、[Leave It Better Than Found](https://arxiv.org/abs/2611.08075)、[MOMASPLAT](https://arxiv.org/abs/2611.08372)、[VisionSIM](https://arxiv.org/abs/2611.08368)、[SCALE](https://arxiv.org/abs/2611.08390)、[Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](https://arxiv.org/abs/2611.05163)、[Evo-DexBench](https://arxiv.org/abs/2610.21180)、[RoboCurate](https://arxiv.org/abs/2602.18742)、[EgoKit](https://arxiv.org/abs/2605.16797)。(共 13 条,另 [Detecting Silent Faults at the Environment-Trainer Boundary in RL](https://arxiv.org/abs/2611.08144)(RL 训练基础设施,代码组织 PlugRL)也归此类。)
另见 / See also: [Social Humanoid](https://arxiv.org/abs/2611.08407)、[HITCH](https://arxiv.org/abs/2611.08039)(已归入 运动控制·RL)。

---

## VLA(展开 5 / 另列 4)

### [Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model](https://arxiv.org/abs/2611.07513) — Chengcheng Wang 等
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/lose4578/Concertina)(匿名 ls-remote 验证存在),权重见 HF 集合(摘要给出)
- 🇨🇳 多数 VLA 把动作机制外挂在 VLM 上(离散化动作 token 或独立动作专家),二者梯度相互竞争或被阻断。Concertina 提出具身 VLM(eVLM):把连续轨迹表示、分块生成与物理坐标监督直接放在共享扩散 VLM 骨干上,每个控制步编码为一个连续潜动作 token,零独立动作生成层,动作投影仅占 4.46B 模型 0.21% 参数(连续 VLA 的动作专家占 16.5%–35.1%)。常规 LIBERO 平均成功率 98.15%,10,030 任务的 LIBERO-Plus 为 85.9%,CALVIN ABC-D 平均完成链长 4.142。
- 🇬🇧 Most VLAs bolt an action mechanism onto a VLM, via discrete tokens or a separate action expert whose gradients compete or are blocked. Concertina is an embodied VLM that places continuous trajectory representation, blockwise generation and physical-coordinate supervision on a shared diffusion VLM backbone, one continuous latent action token per control step, with action projections only 0.21% of the 4.46B parameters (16.5–35.1% for action experts in comparable VLAs). It reaches 98.15% on LIBERO, 85.9% on the 10,030-task LIBERO-Plus and 4.142 average chain length on CALVIN ABC-D.

### [SLA: Scaling Spatial-Language-Action Model via Continual Pre-training](https://arxiv.org/abs/2611.08373) — Fuhao Li, Wenxuan Song 等
🏷️ 交叉方向 / Also: 空间智能 / Spatial Intelligence
开源状态 / Code: ✅ 已开源 / Released — [代码](https://github.com/OpenHelix-Team/Spatial-Forcing/tree/master/SLA)(所在仓库 Spatial-Forcing 匿名 ls-remote 验证存在;SLA 子目录内容未核对);[项目页](https://SLA.github.io/)
- 🇨🇳 VLA 基础模型多继承 2D 视觉语言预训练表示,空间监督通常只在下游适配时引入。SLA 从预训练 π0.5 出发,在持续预训练中联合优化动作预测与中间视觉嵌入和冻结 3D 感知模型空间表示的对齐,并在下游后训练中保持;整合多本体异构机器人数据,用特征依赖门自适应聚合多层嵌入,教师可利用部分深度与相机标定,概率状态 dropout 缓解对示范轨迹过拟合。辅助组件仅训练时使用,推理架构不变;摘要未给出定量结果。
- 🇬🇧 VLA foundations inherit 2D vision-language representations and add spatial supervision only at task adaptation. SLA, initialized from π0.5, jointly optimizes action prediction and alignment of intermediate visual embeddings with a frozen 3D perception model during continual pre-training and post-training, using unified heterogeneous robot data, feature-dependent gates over multiple layers, partial depth/calibration, and probabilistic state dropout. Auxiliary parts are training-only so inference is unchanged; the abstract gives no quantitative results.

### [T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models](https://arxiv.org/abs/2611.08413) — Mohammed Hassan 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 VLA 推理昂贵且背景内容会在分布偏移下干扰动作预测。T3R 免训练:先用分割引导剪除无关视觉块,再用显著性引导的注意力偏置把注意力重新分配到动作关键区域和语言指令。LIBERO-Spatial 上去除 85% 场景相机视觉 token 而成功率基本持平,物体摆放扰动下最多提升 7 个百分点;剪枝与注意力偏置每次推理 7.8 ms,LLM 前向最高 3.3 倍加速;在 LIBERO、SIMPLER、RoboTwin 三种 VLA 骨干上多相机设置收益最大。
- 🇬🇧 VLA inference is expensive and background tokens distract action prediction under shift. T3R is training-free: segmentation-guided token pruning followed by saliency-guided attention biasing toward action-critical regions and language. On LIBERO-Spatial it removes 85% of scene-camera tokens at essentially the same success and improves OOD placement by up to 7 points, costs 7.8 ms per call and gives up to 3.3× LLM-forward speedup; it is evaluated on LIBERO, SIMPLER and RoboTwin with three backbones.

### [Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing (VLA-Tug)](https://arxiv.org/abs/2611.08425) — Michal P. Podolinsky 等
开源状态 / Code: ✅ 已开源 / Released(Comments 声明代码、视频、数据集在 [项目页](https://vla-tug.github.io);仓库 URL 未取得,待核实)
- 🇨🇳 VLA 在分布偏移下脆弱,需要及时、校准且高效的运行时监控。VLA-Tug 是对 VLA 骨干潜层的轻量探针,在失败前片段上监督以提高早期检测并约束漏检/误报率。匹配误报率下早期失败检测比最强学习基线最多提高 30%;面对未见任务,漏检/误报界在最多 86% 的运行中有效(基线至多 21%);失败模式预测在未见任务上 top-3 准确率最多比多数基线高 44%,并支持轻量转向提升成功率;发布 3,180 条标注操作回合数据集。
- 🇬🇧 VLAs are brittle under distribution shift and need a timely, calibrated, efficient runtime monitor. VLA-Tug is a lightweight probe over VLA latent layers trained on pre-failure segments that bounds missed-detection and false-alarm rates. It improves early detection at matched false-positive rates by up to 30%, keeps its bounds valid in up to 86% of runs under unseen-task shift (vs ≤21%), raises top-3 failure-mode accuracy by up to 44% over a majority baseline, supports lightweight steering, and releases 3,180 annotated episodes.

### [OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions](https://arxiv.org/abs/2611.08462) — Arpit Bahety 等
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://robin-lab.cs.utexas.edu/oopsierecover)摘要仅称有视频
- 🇨🇳 VLA 部署时常失败,DAgger 式微调需要数十到数百次交互且难以泛化。OopsieRecover 假设语义可抓住失败原因及纠正,用溯因推断少量纠正示范背后的意图,编码为稠密空间表示和条件代价,标示何时行为不可取并把策略引向更优动作区域。6 个任务及物体位姿、场景和相关任务变化上,少量纠正示范即可让 VLA 克服广泛新情境的失败,无需为每种变化提供新数据;摘要未给具体数值。
- 🇬🇧 VLAs often fail at deployment, and DAgger-style fine-tuning needs tens to hundreds of interactions and generalizes poorly. OopsieRecover uses abduction to infer intent from a handful of corrective demonstrations and encodes it as dense spatial representations and conditional costs that mark undesirable behavior and steer the policy. Across 6 tasks with pose, scene and task variations, a few corrections let a VLA recover from failures in novel situations without new data per variation; no numbers are given.

另列 / Also listed(4):[AffectiveVLA](https://arxiv.org/abs/2611.07712)(G1 社交触碰 VLA:意图门控使 GR00T macro-F1 由 0.75 升至 0.90;非 locomotion/全身控制/RL,故归此类)、[Event-Grounded Sparse Autoencoders for VLA Policies](https://arxiv.org/abs/2605.17204)、[When Vision Overrides Language](https://arxiv.org/abs/2602.17659)、[Vision-Language Models Are Joint Denoisers in Robotic Action Generation](https://arxiv.org/abs/2611.01215)。(共 4 条)
另见 / See also: [Memory before Goal](https://arxiv.org/abs/2610.31166)(已归入 运动控制·RL)。

---

## VLN

今日无严格意义的 VLN 论文(API 关键词 VLN / vision-language navigation 命中 0)。/ No strict VLN papers today (0 API hits).
列名 / Listed(1):[ProCompNav](https://arxiv.org/abs/2605.06223)(v5 更新,主动实例导航,摘要未展开)。
另见 / See also: [MessyNav](https://arxiv.org/abs/2611.07417)(已归入 具身智能)、[OpenNWM](https://arxiv.org/abs/2611.01844)、[Seeing Beyond the Next Step](https://arxiv.org/abs/2611.07730)(已归入 世界模型与 WAM)。

---

## 世界模型与 WAM / World Models & WAM(展开 7 / 另列 5)

### [Spatial-UMI-Dream: Scaling World Action Models with Metric Geometry for UMI Manipulation](https://arxiv.org/abs/2611.07229) — Weiduo Yuan 等
🏷️ 交叉方向 / Also: 空间智能 / VLA
开源状态 / Code: ❓ 未知 / Unknown — 仅[项目页](https://weiduoyuan.com/spatial-umi-dream/)
- 🇨🇳 UMI 的近距移动腕部相机把相机与物体运动纠缠,精确操作所需的度量几何在 RGB 中是隐式的。Spatial-UMI-Dream 是 5B 空间世界动作模型(WAM),在 605 小时 RGB-D UMI 数据上两阶段(仅世界适配→世界-动作联合学习)预训练,联合预测未来 RGB、鱼眼对齐度量深度与动作;并提出 20 任务的 RoboTwin-UMI 基准。域内成功率 79.10%,本体+环境组合偏移下 72.15%,分别比最强基线高 4.65 和 10.30 个百分点;纯 RGB 预训练使域内降 5.75 点;六个真机任务平均 85.0%,比最强基线高 24.2 点。
- 🇬🇧 UMI's moving close-range wrist cameras entangle camera and object motion and leave metric geometry implicit. Spatial-UMI-Dream is a 5B World Action Model pretrained on 605 h of RGB-D UMI data (world-only adaptation, then joint world-action learning) predicting future RGB, metric depth and actions, evaluated on the new 20-task RoboTwin-UMI benchmark. It reaches 79.10% in-domain and 72.15% under combined shifts (+4.65 and +10.30 points over the best baseline), RGB-only pretraining costs 5.75 points, and six real tasks average 85.0% (+24.2 points).

### [La-JEPA: Compact Robot Policies with Latent World Modeling](https://arxiv.org/abs/2611.08156) — Mateo Clémente 等
🏷️ 交叉方向 / Also: VLA / 具身基础模型
开源状态 / Code: ✅ 已开源 / Released(Comments 给出 [代码仓库](https://github.com/mt-clemente/lajepa));匿名 ls-remote 无返回,链接匿名不可访问,待核实
- 🇨🇳 WAM 与 VLA 把策略架构及推理成本绑在为生成设计的大 Transformer 上。La-JEPA 是紧凑 WAM:策略 Transformer 在预训练 V-JEPA 2.1 编码器的特征空间从零训练,沿用 Fast-WAM,训练时联合预测未来特征与动作,推理时只生成动作。无具身预训练的策略中,在干净与随机化 RoboTwin 2.0 及指令正确的 LIBERO-Plus 上达到最优,参数远少于最强对手;比 Fast-WAM 明显更快且性能相当;四个真机任务平均成功率与 π0.5 相当、高于无具身预训练基线;JEPA 特征优于视频 VAE 潜变量(分布外更明显);并修正了 LIBERO-Plus 官方评测器对多数变体指令的破坏。
- 🇬🇧 WAMs and VLAs tie policy architecture and inference cost to large generation-oriented transformers. La-JEPA is a compact WAM whose policy transformer is trained from scratch in V-JEPA 2.1 feature space, predicting future features with actions in training (as Fast-WAM) and generating only actions at inference. Among policies without embodied pretraining it is state-of-the-art on clean/randomized RoboTwin 2.0 and LIBERO-Plus with far fewer parameters, much faster than Fast-WAM at comparable performance, matches π0.5 on four real tasks on average, shows JEPA features beat video-VAE latents, and corrects the LIBERO-Plus evaluator's corrupted instructions.

### [GPWM: Modeling the World as 3D Particle Motion](https://arxiv.org/abs/2611.08338) — Robert Ren, Matthew Bronars 等
🏷️ 交叉方向 / Also: 空间智能
开源状态 / Code: ❓ 未知 / Unknown — 仅[项目页](https://robertren1122.github.io/gpwm/)
- 🇨🇳 视频世界模型生成外观,GPWM(生成式粒子世界模型)直接在 3D 物理空间生成粒子与刚体运动,单一架构覆盖刚体、可变形、布料、颗粒及被动物理与机器人交互。对象感知多分辨率 Transformer 结合 flow matching 与 diffusion forcing,在 2550 万帧 ParticleWorlds 上训练;六个物理领域均优于最佳学习动力学基线,平均误差降低 31%,统一模型单套权重超过逐域基线,并泛化到未见几何、物性、物体数和更长时域。还可通过在潜噪声空间规划,在推与抓取上显著优于动作空间搜索,开环仿真实现无参考轨迹的目标导向操作。
- 🇬🇧 Unlike video world models, GPWM generates particle and rigid-body motion directly in 3D, with one architecture for rigid, deformable, cloth and granular materials, passive and interactive. An object-aware multi-resolution transformer with flow matching and diffusion forcing is trained on ParticleWorlds (25.5M frames); it cuts prediction error by 31% on average across six domains, a unified model outperforms per-domain baselines and generalizes to unseen geometries, properties, object counts and horizons. Noise-space planning substantially beats action-space search on pushing and picking, achieving goal-directed open-loop manipulation in simulation.

### [Learning Robotic World Models with Semantic and Visual Feedback (RoboImagine)](https://arxiv.org/abs/2611.07850) — Hao Wu 等
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/Alexander-wu/RoboImagine)(匿名 ls-remote 验证存在);[权重与数据](https://huggingface.co/easylearning/RoboImagine)
- 🇨🇳 机器人世界模型仅靠视觉重建无法反映任务进度,仅语义评价又对细粒度视觉误差约束不足。RoboImagine 通过候选未来对比后训练自回归世界模型:多样搜索产生候选,冻结多模态评估器做双向顺序成对视频比较给出语义偏好,并以像素/感知级一致性反馈约束局部误差,经组相对优势做策略优化;固定初始上下文与分支滚动历史支持有界上下文的长序列生成。RT-1 上相同初始化与更新数下,PSNR 比持续监督微调高 1.26 dB,LPIPS 降低 11.93%;RT-1、BridgeV2、RoboCasa 均验证。
- 🇬🇧 Visual reconstruction alone misses task progress and semantic evaluation alone under-constrains fine visual errors. RoboImagine post-trains autoregressive robotic world models by comparing candidate futures: diverse search, pairwise video comparison by a frozen multimodal evaluator in both orders, plus pixel- and perceptual-level consistency feedback, optimized with group-relative advantages and rolling branch histories for long sequences. On RT-1 under matched settings it improves PSNR by 1.26 dB and reduces LPIPS by 11.93% over continued supervised fine-tuning, with experiments also on BridgeV2 and RoboCasa.

### [OpenNWM: A Generalist Navigation World Model with Latent Action Pretraining](https://arxiv.org/abs/2611.01844) — Dujun Nie 等(v2 更新)
🏷️ 交叉方向 / Also: VLN/导航
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/OpenSpace-Lab/OpenNWM)(匿名 ls-remote 验证存在);[项目页](https://openspace-lab.github.io/OpenNWM/)
- 🇨🇳 导航世界模型受限于带动作标注数据覆盖不足,而无动作视频缺少动作。OpenNWM 通过视觉预测预训练从大规模无动作视频学习通用潜动作,再用动作条件后训练对齐物理运动,并整理 NavAnywhere 数据集(15 个来源、1750 万视觉观测,覆盖地面机器人、人和无人机,五类场景)。域内和域外基准视觉预测均改善,导航性能也提升;摘要未给具体数值。
- 🇬🇧 Navigation world models are limited by scarce action-labeled data while action-free videos lack actions. OpenNWM learns universal latent actions from large-scale action-free video via visual-prediction pretraining and aligns them with physical motion through action-conditioned post-training, supported by NavAnywhere (17.5M observations from 15 sources across robots, humans and drones). It improves visual prediction in- and out-of-domain and navigation performance; no numbers are given.

### [Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes](https://arxiv.org/abs/2611.07730) — Seong-Eun Hong 等(NeurIPS 2026)
🏷️ 交叉方向 / Also: VLN/导航(人感知导航)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://seoneun.github.io/-NeurIPS-2026-Seeing-Beyond-the-Next-Step/)未核对代码
- 🇨🇳 人群场景中下一步动作局部可行但可能越上马路或切入人流,在线用世界模型推演代价太高。作者主张把世界模型放在训练时作偏好预言机:离散视觉动作先验配两个任务对齐的世界模型(近处社会动态、未来场景语义),按预测后果给候选动作打分,经组相对偏好蒸馏优化策略;部署时移除世界模型,单次前向。五个留出场景中比反应式和学习式基线更安全、更符合社会与群体、更朝向目标,观察者评价更像人类;摘要未给具体数值。
- 🇬🇧 In crowded scenes an action can be locally feasible yet unsafe or socially disruptive, and online world-model rollouts are too costly. The authors use world models at training time as preference oracles: a discrete visual action prior plus two task-aligned world models (social dynamics, future scene semantics) score candidate actions and group-relative preference distillation refines the policy; both are removed at deployment for single-forward-pass inference. Across five held-out scenarios it is safer, more socially and group-coherent and more goal-directed than baselines, and naive observers rate it more human-like; no numbers are given.

### [Reinforcing End-to-End Autonomous Driving Safety via Negative-Aware Planning in a Unified World-Action Model (NegWAM)](https://arxiv.org/abs/2611.08111) — Zihao Zhang 等
🏷️ 交叉方向 / Also: 自动驾驶(非机器人本体)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/Zizizi-hao/NegWAM)(匿名 ls-remote 验证存在)
- 🇨🇳 WAM 的动作学习主要靠专家轨迹模仿,对接近专家的不安全轨迹约束不足。NegWAM 为统一 WAM 的安全后训练框架:构造与专家几何接近但有风险的负轨迹作排斥锚点,并编码为场景条件 rider token 学习场景-轨迹兼容性;联合优化 flow matching 与近专家负目标,rider 分支推理时丢弃。NAVSIM v2 的 navhard 上 EPDMS 40.4(比最强无打分器 WAM 基线相对提高 4.1%),navtest 93.3;HUGSIM 零样本闭环验证泛化。
- 🇬🇧 WAM action learning is dominated by expert imitation, leaving near-expert unsafe trajectories under-constrained. NegWAM builds geometrically close but risky negative trajectories as repulsive anchors and scene-conditioned rider tokens, jointly optimizing flow matching and near-expert negative objectives; the rider branch is discarded at inference. It reaches 40.4 EPDMS on NAVSIM v2 navhard (4.1% relative gain over the strongest scorer-free WAM) and 93.3 on navtest, with zero-shot closed-loop generalization on HUGSIM.

另列 / Also listed(5):[When Does Test-Time Search Help World Action Models?](https://arxiv.org/abs/2610.41970)(审计:学习价值选择器比随机差 1.66 pp,token 剪枝端到端至多 1.15× 加速)、[GuidedWAM](https://arxiv.org/abs/2611.07912)、[WAM-Sim0.1](https://arxiv.org/abs/2611.07939)、[WoVR](https://arxiv.org/abs/2602.13977)、[VTAM](https://arxiv.org/abs/2603.23481)。(另有 [PlayGen2](https://arxiv.org/abs/2611.07867) 为游戏/世界生成,与机器人弱相关。)
另见 / See also: [GigaBrain-WBC-0.5](https://arxiv.org/abs/2608.18234)、[Why Koopman Structure Does Not Help…](https://arxiv.org/abs/2611.00951)(均已归入 运动控制·RL)。

---

## 空间智能与 SLAM / Spatial Intelligence & SLAM(展开 3 / 另列 7)

### [FREE-LIVO: Physically Decoupled Yet Tightly Coupled LiDAR-Inertial-Visual Odometry](https://arxiv.org/abs/2611.07463) — Reon Tabata, Kenji Koide, Shuji Oishi
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 多数 LIVO 假设 LiDAR 与相机刚性固定且时间同步,不利于模块化异构系统。FREE-LIVO 用预训练图像特征匹配器建立相机图像与由生成模型从单次 LiDAR 扫描生成的稠密强度图之间的对应,构造重投影因子约束不同时刻采集的 LiDAR 与相机位姿,并与点云配准、视觉特征跟踪和 IMU 约束联合因子图优化。M3DGR 六个序列平均 ATE RMSE 0.45 m,无需外参,同步误差达 0.5 s 时精度几乎不降;LiDAR 与相机装在不同机器人上也能联合估计两条轨迹。
- 🇬🇧 Most LIVO assumes a rigid LiDAR–camera rig and time synchronization. FREE-LIVO matches camera images to dense LiDAR intensity images generated from a single scan by a generative model using a pretrained matcher, builds reprojection factors across acquisition times, and optimizes them in a factor graph with registration, visual tracking and IMU constraints. On six M3DGR sequences it achieves 0.45 m average ATE RMSE without extrinsics, with minimal degradation under up to 0.5 s sync error, and can jointly estimate trajectories when sensors are on separate robots.

### [XM4D: 4D Reconstruction through Certifiable Geometric Optimization](https://arxiv.org/abs/2611.07902) — Haoyu Han 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 4D 重建联合估计相机运动、场景几何和非刚性形变,非凸优化难保证全局最优。XM4D 把相机运动估计与非刚性形变分开,均表述为结构化 QCQP,可做 SDP 松弛并带可验证全局最优证书:基础深度模型提升静态点轨迹到 3D,解缩放束调整,解析消元后约化为缩放旋转 QCQP;非刚性部分用嵌入式形变图,约化为仅旋转 QCQP,用 GPU 加速 Burer-Monteiro 黎曼优化求解,再初始化动态 Gaussian splatting 做光度精修。七个基准上静态与动态场景相机估计准确,优化可扩展到数千帧,新视角渲染质量达最优。
- 🇬🇧 4D reconstruction jointly estimates camera motion, geometry and non-rigid deformation, which is nonconvex. XM4D separates camera motion (scaled bundle adjustment with foundation-depth-lifted tracks) from non-rigid deformation (embedded deformation graph), casts both as QCQPs with SDP relaxations and global optimality certificates, solves them with a GPU Burer–Monteiro Riemannian solver, and initializes dynamic Gaussian splatting. Across seven benchmarks it gives accurate camera estimation on static and dynamic scenes, scales to thousands of frames and achieves state-of-the-art novel-view rendering.

### [Which Objects Stay? Learning Hierarchical Persistence Beliefs for Lifelong Open-Vocabulary Object Maps (HiPer)](https://arxiv.org/abs/2611.07662) — Thanh Nguyen Canh 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 终身物体地图需估计物体离开视野后是否仍在原位,现有持久性滤波依赖类别先验,难以用于开放词汇。HiPer 不依赖类别,检索视觉与几何相似的训练实例,由其历史估计初始存活率,初始化共轭 Beta 信念并在 Rosen 持久性滤波框架下闭式更新,重识别到新位置时迁移信念。120 个留出仿真序列上优于所有对比方法;检索先验优于 CLIP 标签先验;47 个 3RScan 真实环境同样优于最先进基线。
- 🇬🇧 Lifelong object maps must estimate whether an object persists after leaving view, and class-based survival priors do not suit open vocabulary. HiPer retrieves visually and geometrically similar training instances to initialize a conjugate Beta persistence belief, updated in closed form under Rosen's filter and transferred on re-identification. It is best among competing methods on 120 held-out simulated sequences, retrieval priors beat CLIP label priors, and it also outperforms state-of-the-art baselines on 47 held-out 3RScan environments.

另列 / Also listed(7):[Not Losing Your Way (VIO drift)](https://arxiv.org/abs/2611.07687)、[MetricTrail](https://arxiv.org/abs/2611.07555)、[Georeferenced Cross-View 3D Reconstruction](https://arxiv.org/abs/2611.07575)、[Structure from Collision](https://arxiv.org/abs/2611.07900)、[CST-Bench](https://arxiv.org/abs/2611.07541)、[Rotation Is Token-Blind](https://arxiv.org/abs/2611.07955)、[PVDepth](https://arxiv.org/abs/2611.07873)。(共 7 条)
另见 / See also: [SLA](https://arxiv.org/abs/2611.08373)、[Spatial-UMI-Dream](https://arxiv.org/abs/2611.07229)、[GPWM](https://arxiv.org/abs/2611.08338)(分别归入 VLA / 世界模型与 WAM)。

---

## 其他值得关注 / Other Notable

列名 / Listed(3):[SHORE: Stability-Hybrid On-Policy RL for Online Bin Packing](https://arxiv.org/abs/2611.08364)(RL,非机器人控制)、[Detecting Silent Faults at the Environment-Trainer Boundary in RL](https://arxiv.org/abs/2611.08144)、[Kinematic Hypothesis Context](https://arxiv.org/abs/2611.07411)。

---

## GitHub 动态 / GitHub Highlights

### Star 增长(相对 2026-11-05 快照)/ Star growth
| 仓库 / Repo | Stars | 增长 / Δ | 说明 / Note |
|---|---|---|---|
| [dexmal/opendm](https://github.com/dexmal/opendm) | 2326 | +60 | 通用具身智能开放世界基础模型(VLA) / Open-world embodied foundation model |
| [SkyworkAI/Matrix-Game](https://github.com/SkyworkAI/Matrix-Game) | 2872 | +29 | Matrix-Game 4.0 流式神经渲染世界模型 / Streaming neural-rendering world model |
| [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) | 524 | +14 | SuperMimic 实现与资源合集(第三方) / Third-party SuperMimic collection |
| [fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic) | 168 | +13 | G1 全身动作跟踪,单卡约 3 分钟 / G1 whole-body tracking in ~3 min on one GPU |
| [DAGroup-PKU/PyRUA-Lean](https://github.com/DAGroup-PKU/PyRUA-Lean) | 213 | +14 | 机器人 agent 令牌/动作效率 / Robot agents, fewer tokens |
| [nv-tlabs/vipe](https://github.com/nv-tlabs/vipe) | 2183 | +15 | 视频位姿引擎,3D 几何感知 / Video pose engine |
| [Junchao-cs/SolarWM](https://github.com/Junchao-cs/SolarWM) | 891 | +12 | 长时程视频世界模型开源数据与训练 / Long-horizon video world models |
| [Ropedia/ropedia-w0](https://github.com/Ropedia/ropedia-w0) | 270 | +11 | 跨本体 loco-manipulation 世界模型 / Loco-manipulation world models |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28722 | +14 | v0.7.0 发布 / v0.7.0 release |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 14564 | +13 | — |
| [Genesis-Embodied-AI/genesis-world](https://github.com/Genesis-Embodied-AI/genesis-world) | 30190 | +7 | 仿真平台 / Simulation platform |

(榜首的 gods-eye-view、RuView、text-to-cad 等增长大户与机器人无直接关系,略。)

### 新仓库(筛选)/ New repos
- [lasgroup/generalist-improvement](https://github.com/lasgroup/generalist-improvement)(13 star):"Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement" 论文代码 / companion code,属运动控制·RL 方向的值得关注项。
- [vernerobotics/v0.5](https://github.com/vernerobotics/v0.5)(11 star):面向工业机器人的开放权重世界动作模型 / open-weight WAM for industrial robotics。
- [flyingbitac/FlowPilot](https://github.com/flyingbitac/FlowPilot)(6):无人机敏捷导航的实时世界-动作建模 / real-time WAM for agile UAV navigation。
- [EGalahad/boltrt](https://github.com/EGalahad/boltrt)(5):MuJoCo 与真机共用的 C++ 策略循环 / one C++ policy loop for MuJoCo and hardware。
- [yusenthebot/macmimic](https://github.com/yusenthebot/macmimic)(6):Apple Silicon 上 SuperMimic 风格人形全身控制训练(第三方)。

### 新 Release / New releases
- **[huggingface/lerobot v0.7.0](https://github.com/huggingface/lerobot/releases/tag/v0.7.0)**(2026-11-05):重建安装/训练/推理/硬件层。主要更新:Linux 默认 CUDA 13 的 torch(需驱动 ≥580.65);W&B 换为 Trackio;FSDP2/HSDP、梯度累积、DCP 检查点与 PEFT 并用;可选 EMA、fp16、WSD 调度;交互式 rollout 与远程推理引擎(含 G1 的 SONIC 远程推理);LanceDB 数据集后端与无盘视频流(多 worker 最高 2.5 倍加速);GPU 图像变换;评测报告成功数与 95% Wilson 区间;新增策略 FLUX 3 Action、FineART-VLA、DM05、LaWAM、Wall-OSS-0.5、LingBot-VLA 2.0、Cosmos3、G0.5、Long-WAM 与 SONIC 解码器;批量仿真核心与 NVIDIA RoboLab 基准(Isaac Lab);新增 YAM 机械臂与 reBot B601 电机支持;ROCm/Jetson Dockerfile。破坏性变更:`--policy.use_peft=true` 现在只训练 LoRA;≤0.6.x 的 FSDP 检查点不可续训。
- **[google-deepmind/mujoco 4.0.0](https://github.com/google-deepmind/mujoco/releases/tag/4.0.0)**(2026-11-06):新增 speculative contacts 标志(防止快速凸体穿过薄障碍)、弹塑性(`mjData.plastic`,覆盖关节/肌腱弹簧与 2D/3D flex)、Python 包拆分为 mujoco-core / mujoco-studio / mujoco、MuJoCo Studio 与调参文档、渲染改进(逐 geom 阴影、地平线雾、后处理标志)。行为变更:肌腱 sidesite 缠绕规则改变、RK4 球/自由关节姿态达四阶精度(结果会变)、1D flexcomp 增加扭转关节而改变 nq/nv/qpos 布局、flex 刚度修正、移除 cable 插件/composite 元素/Python 3.10、饱和执行器不再贡献隐式导数。对 RL 训练的影响:升级后既有 MJCF 模型需检查,RK4 与 flex 结果会改变。

---

## 今日趋势 / Today's Trends

1. **人形感知 locomotion 与跑酷走向"先模仿、再放松"+ 预测式表征。** 🇨🇳 STEP 用跨模态/动作条件预测监督策略状态,极限跑酷论文三阶段逐步放松示范先验以适配机器人接触;两者均有真机成功率(98/100、29/30)。🇬🇧 STEP supervises policy state with cross-modal and action-conditioned prediction, while the parkour paper relaxes demonstration priors in stages to fit robot-specific contacts; both report real-robot success (98/100, 29/30). 代表:[STEP](https://arxiv.org/abs/2611.08097)、[Humanoid Parkour](https://arxiv.org/abs/2611.08056)、[CTS-MoE](https://arxiv.org/abs/2606.19633)。
2. **全身跟踪器成为通用执行层。** 🇨🇳 SONIC 被移植到 K1、被 LeRobot 加入解码器/远程推理,HITCH 与 Social Humanoid 都把学习式跟踪器置于 VLM/高层生成器之下;GigaBrain-WBC 则把行为世界模型引入跟踪。🇬🇧 SONIC is ported to the K1 and added to LeRobot, while HITCH and Social Humanoid put a learned tracker under a VLM or motion generator, and GigaBrain-WBC brings a behavior world model into tracking. 代表:[SONIC-K1](https://arxiv.org/abs/2610.39327)、[HITCH](https://arxiv.org/abs/2611.08039)、[Social Humanoid](https://arxiv.org/abs/2611.08407)。
3. **WAM 走向紧凑与度量几何。** 🇨🇳 La-JEPA 在 JEPA 特征空间从零训练、推理只出动作;Spatial-UMI-Dream 用 RGB-D 度量几何;WAM 测试时搜索审计显示收益有限。🇬🇧 La-JEPA trains a compact WAM in JEPA feature space that outputs only actions, Spatial-UMI-Dream adds metric RGB-D geometry, and an audit finds test-time search gains limited. 代表:[La-JEPA](https://arxiv.org/abs/2611.08156)、[Spatial-UMI-Dream](https://arxiv.org/abs/2611.07229)、[Test-Time Search Audit](https://arxiv.org/abs/2610.41970)。
4. **VLA 的可靠性:剪枝、监控、纠错。** 🇨🇳 T3R 免训练剪枝、VLA-Tug 潜层探针、OopsieRecover 语义纠正都关注部署时的效率与失败恢复。🇬🇧 T3R, VLA-Tug and OopsieRecover all target deployment-time efficiency and failure recovery. 代表:[T3R](https://arxiv.org/abs/2611.08413)、[VLA-Tug](https://arxiv.org/abs/2611.08425)、[OopsieRecover](https://arxiv.org/abs/2611.08462)。
5. **SuperMimic 生态在第三方复现中升温。** 🇨🇳 radar 中出现多个第三方 SuperMimic 复现/合集(awesome-supermimic 524 star),但官方代码仍未出现。🇬🇧 Several third-party SuperMimic reproductions appear (awesome-supermimic, 524 stars) while no official code has surfaced. 见监测小节。

---

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
- `agentic robot control`(arXiv + GitHub topic)— 🇨🇳 多模态 agent 直接当机器人策略成为独立设定,见 [RoboARCade](https://arxiv.org/abs/2611.08209)(1 篇)与 [PyRUA-Lean](https://github.com/DAGroup-PKU/PyRUA-Lean)(star +14);信号偏弱但跨基准/仓库各出现一次。🇬🇧 Agents acting directly as robot policies appear as a distinct setting in RoboARCade and PyRUA-Lean.
- `JEPA world action model`(arXiv)— 🇨🇳 当日 La-JEPA 摘要提及 LeapBot-WA、JEPA-WAM、Fast-WAM 等同类方法,说明 JEPA 式 WAM 是成串出现的子方向。🇬🇧 La-JEPA cites LeapBot-WA, JEPA-WAM and Fast-WAM, indicating a cluster. 代表:[La-JEPA](https://arxiv.org/abs/2611.08156)。

**建议观察 / Watch**
- `tactile simulation sim-to-real` — 🇨🇳 TactileLab 与 DLO/灵巧 RL 论文同日出现,再观察几天。🇬🇧 TactileLab and dexterous RL papers co-occur; watch a few more days. 代表:[TactileLab](https://arxiv.org/abs/2611.07881)。

**建议移除/收窄 / Remove or Narrow**
- 今日无建议 / No suggestions today。(多个多词短语在 arXiv API 中 0 命中,属短语匹配所致,而非关键词失效;无需移除。)

---

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 | 当前状态 | 今日检查结果 | 备注 |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 | oss_watch signal=false;无 candidate_repos;[项目页](https://supermimic.github.io)抓取未见 GitHub 链接或开源承诺(仅提及 "SONIC's released checkpoint") | 状态不变。search_hits 全为第三方(如 [Uni-SuperMimic](https://github.com/HUSTforever/Uni-SuperMimic)、[OpenSprite-SuperMimic](https://github.com/BeijingDynamics/OpenSprite-SuperMimic)、[awesome-supermimic](https://github.com/miao-org/awesome-supermimic) 等),不算官方开源 |

**建议加入监测 / Suggested additions**(运动控制优先;已开源者不再建议)
1. **STEP** — 🇨🇳 真机 98/100 的人形感知 locomotion,无代码链接;🇬🇧 98/100 real-robot perceptive humanoid locomotion with no code yet.
```json
{"name": "STEP", "title": "STEP: Spatiotemporal Training with Explicit Prediction for Perceptive Humanoid Locomotion", "arxiv_id": "2611.08097", "search_terms": ["STEP humanoid locomotion", "Noetix E1"], "owners": [], "project_pages": [], "known_repos": []}
```
2. **Social Humanoid** — 🇨🇳 项目页明确写 "Code Soon / Data Soon",且含 260 小时 HHI 基准;🇬🇧 Project page promises code and data; includes a 260-hour HHI benchmark.
```json
{"name": "Social Humanoid", "title": "Social Humanoid: Socially Responsive Human-Humanoid Interaction", "arxiv_id": "2611.08407", "search_terms": ["Social Humanoid", "HHI benchmark"], "owners": [], "project_pages": ["https://von31.github.io/social-humanoid/"], "known_repos": []}
```
3. **CTS-MoE** — 🇨🇳 足式多地形 locomotion,项目页 "Code (soon)";🇬🇧 Multi-terrain legged locomotion, code marked soon.
```json
{"name": "CTS-MoE", "title": "Keeping Jerk in Check: Jointly Trained Perception-Gated Experts for Smooth Terrain Transitions", "arxiv_id": "2606.19633", "search_terms": ["CTS-MoE"], "owners": [], "project_pages": ["https://cts-moe.github.io/"], "known_repos": []}
```
4. **Latent RL Prior** — 🇨🇳 以 RL 先验提升灵巧操作数据效率,项目页承诺开源;🇬🇧 RL-prior for data-efficient dexterous manipulation, release promised.
```json
{"name": "Latent RL Prior", "title": "Latent RL Priors for Data-Efficient Dexterous Manipulation", "arxiv_id": "2611.08458", "search_terms": ["Latent RL Prior"], "owners": [], "project_pages": ["https://yixiaowang7.github.io/latent-rl-prior-page/"], "known_repos": []}
```

**建议移出 / Suggested removals**:今日无 / None today。
