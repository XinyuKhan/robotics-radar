# 机器人/具身智能每日速递 — 2026-10-28 / Robotics & Embodied AI Daily — 2026-10-28

**检查窗口 / Window:** 台北时间 2026-10-27 ~07:40 → 2026-10-28 ~07:40(arXiv 取 2026-10-27 周二 cs.RO 列表,覆盖 10-26/27 提交)。 / Taipei time, roughly the last 24 h; arXiv Tuesday 27 Oct cs.RO listing.

> 本期无监测项开源,故无「🔔 监测项已开源」区块。radar 对 SuperMimic 报 `signal: true`,但唯一候选仓库是 `qiayuanl/claude-meter`(与该工作无关的 macOS 菜单栏应用),判定为误报,状态保持「未知」。详见末节。 / No watchlist item was released. The radar flagged SuperMimic (`signal: true`) only because of an unrelated repo (`qiayuanl/claude-meter`); treated as a false positive, status stays Unknown.

## 来源状态 / Source Status

| 来源 / Source | 状态 / Status |
|---|---|
| arXiv cs.RO new 列表 / listing | ✅ 118 New + 20 Cross-lists = 138 条已逐条分类;Replacements 82 条(未发现与关注主题相关且有实质更新者,未展开)。 / 138 classified; 82 replacements skipped (no substantive relevant update spotted). |
| arXiv API 批量取全文摘要 / full abstracts | ✅ 138/138 取到非空摘要;81 条有 Comments(非抓取问题,其余确实为空)。 / 138/138 non-empty abstracts; 81 with comments. |
| arXiv API 关键词检索 / keyword search(cs.RO/AI/LG/CV,2026-10-26 15:00 UTC 起) | ✅ 命中数 / hits: embodied 3, VLA 3, vision-language-action 2, VLN 0, vision-language navigation 0, humanoid 1, legged locomotion 1, whole-body control 1, MPC 1, reinforcement learning robot 0, sim-to-real 1, dexterous manipulation 0, robot foundation model 0, world model 1, world action model 2, WAM 3, video world model 0, spatial intelligence 0, spatial reasoning 0, SLAM 1, visual SLAM 0, LiDAR SLAM 0, gaussian splatting SLAM 0, 3D reconstruction 2, motion tracking 0, motion imitation 0。合计去重 13 篇,其中 3 篇不在 cs.RO 列表(VGGT 不确定性、鲁棒 Q-learning、可变形管状数据集)。 |
| Hugging Face Daily Papers | ✅ 100 条,与主题相关且带 githubRepo 者:RynnVLA-Latent、EmbodiedLab、RynnUnify(论文 10-22,窗口外)等。 |
| GitHub radar(`data/latest.json`,date_taipei = 2026-10-28) | ✅ 已更新;new_repos 150(筛选后少量入选)、star_growth_top、oss_watch 1 项;`watchlist_releases` 为空(48 小时内无重点项目 release)。 |
| 入选篇数 / Selected | 约 93 篇相关(详细展开 70 篇,其余列名)。 |

## 今日必读 / Top Picks

1. **[MimicAll](https://arxiv.org/abs/2610.33508)** — ❓ 未知 / Unknown · 运动控制·RL。一个 RL 策略跨 16 个人形家族、4,096 种本体变体做全身动作跟踪,并给出 464 个本体的基准。 / One RL tracker shared across 16 humanoid families and 4,096 body variants, plus a 464-body benchmark.
2. **[HumanoidNDM](https://arxiv.org/abs/2610.34126)** — ❓ 未知 / Unknown · 运动控制·RL。无需动捕、用真实数据训练的神经动力学模型对人形动作跟踪策略在线微调,CoRL 2026 接收,G1 真机验证。 / MoCap-free online fine-tuning of humanoid tracking policies through a neural dynamics model; CoRL 2026; real G1.
3. **[AdaDexTrack](https://arxiv.org/abs/2610.33852)** — ✅ 已开源 / Released · 运动控制·RL。CVPR 2026,调制器在环的语言条件灵巧手跟踪,零样本 sim-to-real,代码已可匿名访问。 / CVPR 2026 modulated dexterous tracking with zero-shot sim-to-real; code is public.
4. **[Differentiable Contact Dynamics for Legged Locomotion](https://arxiv.org/abs/2610.35852)** — ❓ 未知 / Unknown · 运动控制·RL(兼含传统轨迹优化)。穿越接触模式切换的平滑解析梯度,不到 2 分钟训练出可直接上真机的小跑策略。 / A smooth analytic contact gradient: a trotting policy trained in under 2 minutes transfers to hardware.
5. **[RynnVLA-Latent](https://arxiv.org/abs/2610.34356)** — ✅ 已开源 / Released · VLA。30.1K 小时视频学 3D 感知潜在动作,4B 策略 LIBERO 98.8%。 / 3D-grounded latent actions from 30.1K h of video; 98.8% on LIBERO.

---

## 运动控制·RL / Motion Control · RL(全部展开 / all expanded:18)

### [MimicAll: Structured Embodiment Conditioning for Cross-Humanoid Whole-Body Motion Tracking](https://arxiv.org/abs/2610.33508)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 人形动作跟踪器通常按单一本体训练,跨身体共享策略需要处理结构、形态与动力学差异。MimicAll 把结构化本体描述符编码为全局与关节对齐条件,与观测历史和身体匹配的动作参考一起预测关节目标偏移;训练覆盖 16 个人形家族的 4,096 个变体,并提出 464 个本体、五个分布层的基准。等量训练样本下,共享训练在随机化 G1 本体的 100STYLE 上 30 秒成功率 99.4%,单本体专家为 42.9%;LAFAN1 子集上,错配本体条件使自注意力编码的成功率从 61.7% 降到 47.0%。
- 🇬🇧 Humanoid motion trackers are usually trained per body, but sharing one policy needs to handle structural, morphological and dynamic differences. MimicAll encodes a structured embodiment descriptor into global and joint-aligned conditions and combines it with observation history and body-matched references to predict joint-target offsets, training over 4,096 variants from 16 humanoid families and introducing a 464-body benchmark. At equal training transitions, shared training reaches 99.4% 30-second success on randomized G1 bodies in 100STYLE versus 42.9% for a single-body specialist. On a LAFAN1 subset, mismatched body conditions drop self-attention's success from 61.7% to 47.0%.

### [HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model](https://arxiv.org/abs/2610.34126)
开源状态 / Code: ❓ 未知 / Unknown(CoRL 2026 接收;无代码链接)
- 🇨🇳 人形动作跟踪在真机上会遇到外部扰动和仿真建模误差造成的动力学差距,用真实数据微调是部署的最后一公里。该工作先用带自适应强度的低频参考扰动采集数据,再用可微正运动学训练基于历史的本体感知神经动力学模型(不依赖动捕),最后通过模型梯度反传直接微调策略。在 Unitree G1 真机上实现对多种扰动的快速适应,作者称这是首个在线、无需动捕的人形跟踪策略微调框架;预印本摘要未给出具体数值。
- 🇬🇧 Humanoid tracking policies face dynamics gaps from disturbances and simulation error, so fine-tuning on real data is the last mile. HumanoidNDM collects data with low-frequency, adaptive-intensity reference perturbations, trains a history-based proprioceptive neural dynamics model with differentiable forward kinematics (no MoCap), and fine-tunes the policy by backpropagating model gradients. On a Unitree G1 it adapts quickly to various perturbations and is claimed to be the first online, MoCap-free fine-tuning framework for humanoid tracking; the abstract gives no quantitative numbers.

### [AdaDexTrack: Dynamic Modulation for Adaptive and Generalizable Dexterous Manipulation Tracking](https://arxiv.org/abs/2610.33852)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/Janebek/AdaDexTrack);项目页标注 Code,已用匿名 `git ls-remote` 验证;[项目页](https://janebek.github.io/AdaDexTrack/)
- 🇨🇳 语言指令生成的灵巧手—物体交互参考带噪,人到机器人重定向又有本体偏差,固定参考跟踪的小误差会滚雪球。AdaDexTrack 用「专家到通才」蒸馏得到通用跟踪器,再用同一任务目标下 RL 训练的调制器做三种反馈修正:参考调制、物体潜变量调制与位置目标微调。大规模评测中,在未见轨迹和未见物体上的平均跟踪误差与成功率均优于此前 SOTA;零样本 sim-to-real 真机上,加入调制器相对仅跟踪器有明显提升(CVPR 2026;摘要未给出具体数值)。
- 🇬🇧 Language-generated hand–object references are noisy, retargeting adds embodiment bias, and fixed-reference tracking lets small errors snowball. AdaDexTrack distills a generalist tracker from specialists and adds an RL-trained modulator that corrects the reference, the object latent and the positional target in the loop. It beats prior SOTA in tracking error and success on unseen trajectories and objects, and the modulator gives clear gains over the tracker-only variant in zero-shot sim-to-real on hardware (CVPR 2026; no numbers in the abstract).

### [Differentiable Contact Dynamics for Legged Locomotion: Policy Learning and Contact-Implicit Trajectory Optimization](https://arxiv.org/abs/2610.35852)
🏷️ 交叉方向 / Also: 运动控制·传统(接触隐式轨迹优化)/ Motion Control · Classical
开源状态 / Code: ❓ 未知 / Unknown([项目页](https://diffcontact.github.io)仅链接论文,无代码或承诺)
- 🇨🇳 精确的摩擦接触灵敏度只描述当前接触模式内的变化,对相邻模式没有一阶信息,不利于基于梯度的策略学习与轨迹优化。该工作对 Coulomb 摩擦的二阶锥互补问题做中心路径松弛,仅在反向传播中替换为平滑解析梯度,前向仍是硬接触求解,所以 rollout 可行。用 10 万样本、台式机不到 2 分钟训练出的策略无需微调即可上真机,小跑策略能承受推扰并通过碎石与湿滑地面;在轨迹优化中能到达精确梯度和 Signorini 松弛梯度错过的接触丰富解(已投 T-RO)。
- 🇬🇧 Exact frictional-contact sensitivity only describes changes within the current contact mode and gives no first-order information toward neighboring modes. The paper relaxes the Coulomb-friction second-order-cone complementarity along the central path and swaps in the smooth analytic gradient only in the backward pass, leaving the hard-contact forward solve and feasible rollouts unchanged. With 100,000 samples and under 2 minutes of desktop training, the policy transfers to hardware without fine-tuning, withstanding pushes and crossing debris and slippery ground; in trajectory optimization it reaches contact-rich solutions missed by exact and Signorini-relaxed gradients (submitted to T-RO).

### [MOTIO: Agentic Skill Engineering for Reality-Grounded Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.33446)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(agentic 系统)
开源状态 / Code: ❓ 未知 / Unknown([项目页](https://iiiiqiiii.github.io/motio/)仅有论文、补充材料与视频,无代码链接或承诺)
- 🇨🇳 人形 loco-manipulation 技能通常依赖遥操作或机器人演示采集。MOTIO 让 agent 利用人类动作视频、真实感 3D 资产、动作参考和可复用机器人技能,通过上下文任务/接触推理构造分阶段交互,并借助物理执行、多帧反馈和人工验证迭代改进,底层调用现有全身控制、逆运动学与灵巧手接口。33 次首次通过的中位 agent 回合耗时 97.0 分钟,请求到通过 2.80 小时;在扫描办公室中完成连续 101.75 秒的 G1 瓶子丢弃真机执行,物理微调使拧螺丝残差降低 76.0%;agent 技能还监督 BC/DAgger 蒸馏出共享策略,在同一检查点完成 18 个仿真任务。
- 🇬🇧 Humanoid loco-manipulation skills usually need teleoperation or robot demonstrations. MOTIO has an agent turn human-action videos, reality-grounded 3D assets, motion references and reusable skills into staged interaction programs via in-context task and contact reasoning, refined with physics execution, multi-frame feedback and human validation, on top of existing whole-body, IK and dexterous-hand interfaces. Across 33 first approvals the median agent-turn time is 97.0 minutes (2.80 h request-to-approval); a continuous 101.75-second bottle-disposal runs on a physical G1 in a scanned office, physical refinement cuts screw-tightening thread residual by 76.0%, and agent skills supervise BC/DAgger distillation into one shared policy completing 18 simulated tasks.

### [Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data](https://arxiv.org/abs/2610.35075)
🏷️ 交叉方向 / Also: VLA(GR00T N1.7 训练)、空间智能与 SLAM(Gaussian 实到仿)
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://young-bit.github.io/zero-hlm/)导航栏标注「Code (coming soon)」,尚无仓库链接
- 🇨🇳 人形 loco-manipulation 的泛化受限于昂贵的真机演示。Zero-HLM 是实到仿到实框架:用手机拍摄加仿真源演示,通过高斯引导的 agentic 实到仿重建对齐视觉与物理场景,并用 rollout 反馈共同修正全身参考与交互几何。生成 4,800 条物理验证演示,在三个 Unitree G1 任务上零样本迁移;仿真训练的 GR00T N1.7 平均全任务成功率 66.7%,真机数据训练为 46.7%;泛化配置上,扩展仿真训练把汇总成功率从真机数据基线的 23% 提到 69%。
- 🇬🇧 Humanoid loco-manipulation is bottlenecked by costly real demonstrations. Zero-HLM is a real-to-sim-to-real framework that turns smartphone captures and simulated source demonstrations into training data, using Gaussian-guided agentic real-to-sim reconstruction and motion–environment co-adaptation with rollout feedback to fix whole-body references and interaction geometry. It yields 4,800 physically validated demonstrations for zero-shot transfer across three Unitree G1 tasks: simulation-trained GR00T N1.7 reaches 66.7% mean full-task success versus 46.7% with real-data training, and on generalized configurations pooled success rises from 23% to 69% without extra real demonstrations.

### [Learning Force-Reactive Humanoid Loco-Manipulation (FLORE)](https://arxiv.org/abs/2610.35862)
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://louis-leee.github.io/FLoRe/)标注「Code (coming soon)」
- 🇨🇳 许多日常任务要同时控制接触力与运动,人形需要双手加全身协调施力,而仅靠运动学轨迹无法表达。FLORE 用两个带力传感的 UMI 式手持夹爪与可穿戴追踪器采集免机器人演示,训练以视觉、本体感知和实测力矩为输入的力反应扩散策略,输出动作和每只手的力指令,再由带力跟踪的混合柔顺全身控制器在保持平衡的同时执行。仿真中控制器能跟踪不同大小方向的力指令且全身运动精度损失很小;三个接触丰富的真机任务上力反应策略成功率 80%,同样演示和控制器下的纯位置策略为 26.7%。
- 🇬🇧 Everyday tasks require controlling contact force as well as motion, coordinated across both hands and the whole body, which kinematic trajectories cannot specify. FLORE collects robot-free demonstrations with two force-sensing UMI-style grippers plus body trackers, trains a force-reactive diffusion policy on vision, proprioception and measured wrenches that outputs actions and per-hand force commands, and executes them with a hybrid-compliance whole-body controller that keeps balance. In simulation the controller tracks per-hand force commands with little loss in motion accuracy, and across three real contact-rich tasks the policy succeeds in 80% of rollouts versus 26.7% for a position-only policy on the same demonstrations and controller.

### [HuGe: Scaling Humanoid Generalist Vision-Language-Action Models with Egocentric Experience](https://arxiv.org/abs/2610.34186)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 把 VLA 扩展到人形需要协调的全身控制和昂贵的多样演示;第一视角人类演示可补充,但视觉本体差异与缺失本体感知使迁移困难。HuGe 在三种现有 VLA 架构上预测给定预训练全身控制器的潜在动作 token 和手部控制信号,经「第一视角预训练—人形适配—下游微调」三阶段,预训练用 2,000+ 小时人类与机器人数据,并通过仿真回放构造伪本体状态、重渲染手臂外观来缩小差距。在 HumanoidArena 仿真基准上达到 SOTA,Unitree G1 真机上加入视觉适配后的第一视角演示显著提升取放任务成功率(摘要未给出具体数值)。
- 🇬🇧 Extending VLAs to humanoids needs coordinated whole-body control and diverse demonstrations, and egocentric human data helps but suffers from visual embodiment gaps and missing proprioception. HuGe applies three existing VLA architectures to predict latent motion tokens for a pretrained whole-body controller plus hand-control signals, using a three-stage pipeline (egocentric pre-training on 2,000+ hours, humanoid adaptation, downstream fine-tuning) with simulation-replayed pseudo-proprioception and re-rendered arm appearance. It achieves state-of-the-art on the HumanoidArena benchmark, and on a Unitree G1 adding visually adapted egocentric demonstrations significantly improves a pick-and-drop task (no numbers in the abstract).

### [Active Reachability Learning for Humanoid Recoverability Monitoring](https://arxiv.org/abs/2610.33317)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 部署人形任务策略需要能提前预判不可恢复摔倒、触发回退策略的运行时监测器,而现有方法假设训练数据已覆盖可恢复包络,在接触丰富系统上会对分布外输入「乐观幻觉」。该工作把监测器学习表述为价值学习与主动探索交替迭代,探索被重述为到达—规避问题,由不确定性引导的探索器在避开确定不可恢复区域的同时覆盖未见状态,并用 TD 加 Monte Carlo 的组合目标,把高不确定区域保守视为不可恢复。在随机基准和 29 自由度 Unitree G1 上显著提高监测器覆盖与精度,并零样本迁移到真机(摘要未给出具体数值)。
- 🇬🇧 Deploying humanoid policies needs runtime monitors that anticipate unrecoverable falls in time to trigger a fallback, but existing methods assume the data already covers the recoverability envelope and hallucinate optimistically out of distribution. The paper iterates between value learning and active exploration reframed as a reach-avoid problem, with an uncertainty-guided explorer and a combined TD and Monte Carlo objective, treating residual high-uncertainty regions as unrecoverable. On stochastic benchmarks and a 29-DoF Unitree G1 it substantially improves monitor coverage and accuracy and transfers zero-shot to hardware (no numbers in the abstract).

### [RAIWAY: A Large-Wheeled Bipedal Robot with Contact-Informed Blind Locomotion](https://arxiv.org/abs/2610.33172)
开源状态 / Code: ❓ 未知 / Unknown(RA-L 接收;仅有[视频](https://youtu.be/Ch0divLg64w))
- 🇨🇳 大轮轮足机器人在不规则、不连续地形上的滚动运动由局部轮—地接触主导,难以直接布置传感器。RAIWAY 利用仿真中可得的接触信息,把多接触事件蒸馏成潜在表示,部署时仅凭本体感知在线推断该表示,无需接触传感。真机在陡坡、碎石床、钉面和岩石地形上通行,并在最高 15 cm 台阶高度的室外楼梯上连续攀爬;在挑战性室内外场景中优于没有接触感知机制的基线(摘要未给出具体数值)。
- 🇬🇧 Rolling locomotion of a large-wheeled biped over irregular, discontinuous terrain is dominated by local wheel–terrain contact that is hard to instrument. RAIWAY distills multi-contact events available in simulation into a latent representation that the controller infers online from proprioception alone, with no contact sensing at deployment. The real robot crosses steep slopes, gravel, studded surfaces and rocks and climbs outdoor stairs with riser heights up to 15 cm continuously, outperforming baselines without the contact-informed mechanism (no numbers in the abstract).

### [ThinkLocoManip: A Whole-Body Control Agentic Harness for Legged Loco-Manipulation](https://arxiv.org/abs/2610.34370)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(agentic harness)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 长时程足式 loco-manipulation 的直接动作生成与「先规划后执行」范式在泛化和错误恢复上都吃力。ThinkLocoManip 采用交错推理—行动范式,编排感知、导航、操作与运动(locomotion)等工具,并首次把 locomotion 显式作为 agent 的工具域,设计跨域协同技能和用于错误恢复的关键帧思考机制。真机长时程任务成功率 77%,是最强先规划后执行基线(37.1%)的两倍多。
- 🇬🇧 Direct action generation and plan-then-act paradigms struggle with generalization and error recovery in long-horizon legged loco-manipulation. ThinkLocoManip interleaves reasoning and acting, orchestrates perception, navigation, manipulation and locomotion tools (explicitly treating locomotion as a tool domain), adds cross-domain skills and a keyframe-thinking mechanism for recovery. In real-world long-horizon tasks it reaches 77% success, more than twice the strongest plan-then-act baseline (37.1%).

### [HA-DiPO: Diffusion Policy Optimization for Heterogeneous Cooperative Transport](https://arxiv.org/abs/2610.33584)
开源状态 / Code: ✅ 已开源 / Released(部分)— [仓库(sim-to-sim)](https://github.com/ha-dipo/ha-dipo-sim2sim);已验证仓库存在,项目页未说明内容范围,可能仅含 sim-to-sim 部分;[项目页](https://ha-dipo.github.io/)
- 🇨🇳 异构足式机器人协同搬运需要协调不同运动能力并支撑非固定的共享载荷。HA-DiPO 是 CTDE 下的分层多智能体 RL:高层用中心化 critic 的团队价值联合训练各机器人的扩散协调策略,低层是各本体专用的鲁棒运动策略;协调策略从零通过奖励驱动的仿真交互学习,执行时每个机器人只用本地机器人与载荷观测,无伙伴状态和通信。仿真中最终平均回报与速度跟踪成功率更高、速度误差更低;真机演示了四足—轮足及人机协同搬运(RA-L 在投;摘要未给出具体数值)。
- 🇬🇧 Cooperative transport by heterogeneous legged robots must coordinate different motion capabilities around an unfixed shared payload. HA-DiPO is a hierarchical multi-agent RL framework under CTDE: a centralized critic trains per-robot diffusion coordination policies at the high level, while embodiment-specific robust motion policies track their commands; coordination is learned from scratch without demonstrations and executes with only local observations and no messages. It beats baselines in final return, velocity-tracking success and velocity error in simulation, and real experiments show quadruped–wheeled-legged and human–robot transport (submitted to RA-L; no numbers in the abstract).

### [RoboLongR: Causally Consistent Rewards Teach Robots to Progressively Master Long-Horizon Manipulation](https://arxiv.org/abs/2610.33863)
开源状态 / Code: ❓ 未知([项目页](https://chenzixuan99.github.io/RoboLongR-public/)无代码链接,也声明非数据/基准实现发布)
- 🇨🇳 长时程操作中视觉进度会掩盖缺失的任务前提。RoboLongR 是离线到在线框架,学习依赖历史的奖励来引导策略适应新任务,核心目标是因果一致:用阶段打乱监督、循环记忆和两轮训练使奖励与执行历史支持的前提对齐,并把稀疏终止反馈接入奖励学习,从行为克隆过渡到在线 RL。在 88 个 RLBench 任务与 Open-X 上预训练后,18 个未参与奖励预训练的长时程任务平均成功率 31.8%,比最强基线高 9.2 个百分点;4 个真机任务成功率 57.5%,提升 32.5 个百分点。
- 🇬🇧 In long-horizon manipulation, visual progress can hide missing prerequisites. RoboLongR is an offline-to-online framework learning history-dependent rewards with causal consistency (stage-shuffle supervision, recurrent memory, two-round training, sparse terminal feedback) to guide stage-conditioned refinement from behavior cloning to online RL. Pretrained on 88 RLBench tasks and Open-X data, it reaches 31.8% average success on 18 held-out long-horizon tasks, 9.2 points above the strongest baseline, and 57.5% on four real-robot tasks, a 32.5-point gain.

### [MDPO: Multi-constraint Dexterous Policy Optimization with Reinforcement Learning](https://arxiv.org/abs/2610.33480)
开源状态 / Code: ❓ 未知(摘要写「Our code is available at this link」,但摘要与 Comments 中未见可访问的 URL,待核实)
- 🇨🇳 灵巧操作策略需同时满足关节限位、手指危险构型、手臂碰撞与物体不稳定交互等多种安全要求,而现有约束 RL 主要处理累计成本约束,难以同时处理多种异质约束。MDPO 把灵巧操作形式化为同时含累计成本约束与逐状态成本约束的多约束策略优化,并在策略优化中引入约束专属的策略投影,把最大化任务性能的中间策略映射到各约束可行域。在 ReDMan 的安全关节控制、手指安全和抓取任务上,约束满足度更优,同时任务性能与基线相当(摘要未给出具体数值)。
- 🇬🇧 Dexterous policies must satisfy joint limits, unsafe finger configurations, arm collisions and unstable object interactions simultaneously, while existing constrained RL mainly handles cumulative-cost constraints. MDPO formulates dexterous manipulation as multi-constraint policy optimization with both cumulative and state-wise cost constraints and adds constraint-specific policy projections that map the task-maximizing intermediate policy onto each feasible region. On ReDMan (safe joint control, finger safety, grasping) it achieves better constraint satisfaction with competitive task performance (no numbers in the abstract).

### [Pretraining Knows What, Simulation Teaches How (ZAP)](https://arxiv.org/abs/2610.35817)
🏷️ 交叉方向 / Also: 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models(VLM agent harness)
开源状态 / Code: ❓ 未知
- 🇨🇳 机器人策略既要理解任务也要知道怎么动。ZAP 用工具 harness 让一个 27B 预训练 VLM 控制机器人,只在简单仿真任务上做 SFT 与 GRPO 来教它「怎么动」,训练中不使用任何真机数据。真机任务成功率 96.7%,与 GPT-6 Astra 在同一 harness 下持平,优于 MolmoAct2 VLA(33.3%),速度快 3 倍、成本低 17 倍;可泛化到新物体、目标与策略(试管入架、双臂递接、井字棋、下棋),并迁移到未见本体,单臂 Franka 在 RoboLab-120 上 55.9%,领先最佳 VLA/WAM 基线 4.9 个百分点。
- 🇬🇧 A robot policy must understand what a task asks and how to move. ZAP gives a pretrained 27B VLM a simple tool harness and teaches it how to move with SFT and GRPO on simple simulated tasks, using no real-robot data. It reaches 96.7% success on real tasks, matching GPT-6 Astra in the harness and beating the MolmoAct2 VLA (33.3%) while running 3x faster and 17x cheaper; it generalizes to new objects, goals and strategies and transfers to an unseen Franka embodiment, scoring 55.9% on RoboLab-120, 4.9 points above the leading VLA/WAM baseline.

### [Enhancing Deep Reinforcement Learning for Robotic Motion Planning via Task Decomposition](https://arxiv.org/abs/2610.35494)
开源状态 / Code: ❓ 未知(IEEE MSN 2026 接收)
- 🇨🇳 含障碍物的机械臂任务在 DRL 中表现不佳且收敛慢。该工作提出任务分解框架,把迁移学习(只迁移结构相关任务的首层 critic 参数)与奖励重设计(分阶段子目标提供更密集信号)结合。PyBullet Panda 上带障碍 Push 达 0.83±0.05,高于最强基线 TQC 的 0.77±0.06;带障碍 Slide 达 0.95±0.02,比 SAC 的 0.84±0.06 高约 11%;前向迁移最多缩短 70% 收敛时间,奖励重设计把 Pick-and-Place 训练从约 0.75M 步减到 0.20M 步;最优策略在真机 Franka FR3 上作定性可行性演示。
- 🇬🇧 DRL for obstacle-laden manipulation is slow and underperforms. The paper combines transfer learning (transferring only first-layer critic parameters between related tasks) with reward redesign (staged sub-objectives for denser signals). On PyBullet Panda it reaches 0.83±0.05 on Push with obstacle versus 0.77±0.06 for TQC and 0.95±0.02 on Slide with obstacle versus 0.84±0.06 for SAC, cuts convergence time by up to 70%, shortens Pick-and-Place from about 0.75M to 0.20M steps, and shows a qualitative deployment on a real Franka FR3 (IEEE MSN 2026).

### [Learning Dexterous Manipulation: Hands, Simulators, Training, and Evaluation](https://arxiv.org/abs/2610.33486)
🏷️ 交叉方向 / Also: VLA(综述涉及)。因是综述而非控制方法,仍按「RL 为主流配方」归入本类。
开源状态 / Code: ❓ 未知(综述,未声明自有代码)
- 🇨🇳 综述覆盖 113 个基于学习的灵巧手内操作方法、所用手、仿真器与结果汇报方式。领域主流配方是在 GPU 仿真器里用特权状态做 RL,再蒸馏成纯视觉学生迁移到真机,近一半方法如此,且几乎都在同一个仿真器;另一条增长更快的分支从遥操作演示学习(VLA、扩散策略与采集设备)。通过对照已发布代码和厂商规格发现,有 8 款可购买或可复现的手没有出现在任何方法论文中,物体穿透深度即便报告也不在产生动作的物理中测量,并给出未报告量的报告协议。
- 🇬🇧 This survey covers 113 learning-based in-hand dexterous methods, their hands, simulators and reporting. The field converged on RL with privileged state in a GPU simulator, distilled into a vision-only student for hardware, used by almost half the corpus and nearly all in one simulator, while a faster-growing branch learns from teleoperated demonstrations (VLAs, diffusion policies, collection rigs). Reading released code and vendor specs beside the papers shows eight buyable or buildable hands appear in no method paper here and penetration depth is not measured in the physics that produced the motion; Section VII proposes a reporting protocol.

### [Learning Functional Specialisation for Bimanual Robotic Control](https://arxiv.org/abs/2610.33947)
开源状态 / Code: ❓ 未知
- 🇨🇳 研究在带通信的双循环控制器的肌骨骼仿真系统中,双臂控制的学习职责应如何在模块化控制器和两条手臂之间分配,在运动噪声、能耗和通信延迟下。2×2 设计比较差异化与共享控制器目标、固定与平衡的手—任务分配。差异化目标加固定、与对侧控制路径对齐的分配效果最好,双臂成功率 81.33%,优势随运动噪声增大而增大、在更强能耗惩罚下缩小;交换手角色使该条件成功率下降 80.46 个百分点,而共享—平衡训练只下降 1.51 个百分点。
- 🇬🇧 The paper studies how learning responsibility should be organised across modular controllers and two arms in a simulated musculoskeletal bimanual system under motor noise, energy cost and communication delay, using a 2×2 design of differential vs shared objectives and fixed vs balanced hand-task assignment. Differential objectives with fixed contralateral-aligned assignment work best, reaching 81.33% bimanual success, with an advantage that grows with motor noise and narrows under stronger energy penalties. Reversing hand roles drops its success by 80.46 points versus 1.51 points for Shared-Balanced training.

**另见 / See also(本类相关 GitHub 仓库):** [DiaoOrg/awesome-supermimic](https://github.com/DiaoOrg/awesome-supermimic) 等 SuperMimic 第三方复现,见「GitHub 动态」。

---

## 运动控制·传统 / Motion Control · Classical(全部展开 / all expanded:13)

### [Continuous-Time Safe Planning and Control for Agile Quadrupeds](https://arxiv.org/abs/2610.35670)
开源状态 / Code: ❓ 未知
- 🇨🇳 敏捷四足在动态环境中的轨迹既要动力学可行又要可证无碰撞,但多数实时规划为了易解而简化运动学模型,并只在离散点上保证安全。该工作保留四足完整驱动的 SE(2) 模型及其各向异性、与朝向耦合的速度界,接受非凸性,把轨迹参数化为复合 Bernstein 多项式,利用凸包性质在整个规划时域内认证避碰与输入界,并以在线重规划速率向运动控制器输出机体速度。仿真对消融与外部基线验证,真机在未知移动障碍中恢复了简化模型排除的侧向与朝向耦合运动(摘要未给出具体数值)。
- 🇬🇧 Agile quadruped planning needs dynamically feasible, provably collision-free trajectories, yet most real-time planners simplify the kinematics and certify safety only at discretization points. The method keeps the fully actuated SE(2) model with anisotropic, heading-coupled velocity bounds, accepts the nonconvexity, parameterizes trajectories as composite Bernstein polynomials to certify collision avoidance and input bounds over the whole horizon via the convex hull property, and commands body velocities to the locomotion controller at replanning rate. Simulation against ablations and baselines and hardware runs among unknown moving obstacles recover lateral and heading-coupled motion that simplified models exclude (no numbers in the abstract).

### [RoKON: Efficient and Adaptive Data-Enabled Predictive Control for Robotic Manipulation](https://arxiv.org/abs/2610.35458)
开源状态 / Code: ❓ 未知
- 🇨🇳 数据使能预测控制无需显式学习动力学模型,但距实时机器人应用还有距离。RoKON 沿用基于高斯核的非线性预测器,提出利用最小二乘结构的阻尼 Gauss-Newton 方法以实现实时控制,并设计混合缓冲区管理,把有信息量的在线数据与相关离线数据一并保留以适应动力学变化。在 MuJoCo 中用 Franka Research 3 推块、且不预知摩擦变化的实验里展示了跟踪性能与计算适用性(摘要未给出具体数值,仅仿真)。
- 🇬🇧 Data-enabled predictive control needs no explicit dynamics model but is far from real-time robotics. RoKON keeps a Gaussian-kernel nonlinear predictor, adds a damped Gauss-Newton method exploiting the least-squares structure for real-time control, and a hybrid buffer that keeps informative online data alongside relevant offline data to track changing dynamics. It demonstrates tracking performance and computational suitability in MuJoCo with a Franka Research 3 pushing a block under unknown, changing friction (simulation only; no numbers in the abstract).

### [ISB-NMPC: Interception-Oriented Spherical-Bearing Nonlinear Model Predictive Control for Quadrotors](https://arxiv.org/abs/2610.34789)
开源状态 / Code: ✅ 已开源 / Released(待核实)— 摘要给出 [软件仓库](https://github.com/HOLYNOTBAD/ISB-NMPC) 与 [硬件仓库](https://github.com/HOLYNOTBAD/holydrone);匿名 `git ls-remote` 未能访问,链接匿名不可访问,待核实
- 🇨🇳 带捷联相机的四旋翼拦截器中,机动与相机指向耦合,快速逼近与保持目标可见相互冲突。ISB-NMPC 将球面方位预测与非线性四旋翼动力学耦合,联合优化朝目标逼近和可见性,并用 S² 上姿态补偿 EKF 估计目标方位运动、补偿感知延迟并指导尺度自适应检测。30 次成对仿真拦截成功率 86.7%(评测控制器中最高),目标可见时间 99.11%;室外飞行在约 150 m 处捕获 30 cm 目标,长距飞行速度达 17 m/s,追击被拖曳机动目标约 14 m/s(已投 IEEE/ASME T-Mech)。
- 🇬🇧 For a quadrotor interceptor with a strapdown camera, maneuvering and camera pointing are coupled, so fast closing conflicts with keeping the target visible. ISB-NMPC couples spherical-bearing prediction with nonlinear quadrotor dynamics to jointly optimize closing motion and visibility, with an attitude-compensated EKF on S² estimating bearing motion, compensating perception delay and guiding scale-adaptive detection. Over 30 paired simulations it reaches 86.7% interception success (highest of the controllers) with 99.11% target-visible time; outdoors it acquires a 30 cm target at about 150 m at up to 17 m/s and about 14 m/s pursuing a towed maneuvering target (submitted to IEEE/ASME T-Mech).

### [Quantile-Based Command-Reserve MPC for Current-Command Gimbal Pointing](https://arxiv.org/abs/2610.34913)
开源状态 / Code: ✅ 已开源 / Released(部分)— 按 Comments,重算脚本与硬件试验数据作为 arXiv ancillary files 提供,无独立仓库
- 🇨🇳 两轴电流指令云台在摩擦、力矩脉动、电流响应滞后与模型失配下的约束视线指向控制困难。该工作提出分位数扰动预测器(用历史学习中位数与外层分位数)补偿可预测加速度残差并刻画剩余不确定性,再用 tube 启发的 MPC 按预测不确定度预留指令余量;并给出线性误差模型与固定辅助策略下的有限时域 tube 包含结果。嵌入式两轴平台上 4 种配置各 7 次重复试验,所提配置二维指向 RMSE 为 3.94±0.10 mrad,评估窗口内无指令越限样本(名义 100 Hz;已投 Journal of the Franklin Institute)。
- 🇬🇧 Constrained line-of-sight pointing of a current-command two-axis gimbal is hard under friction, torque ripple, current lag and model mismatch. A quantile disturbance predictor (learned median and outer quantiles) compensates predictable acceleration residuals and describes remaining uncertainty, and a tube-inspired MPC reserves command headroom according to that uncertainty, with a finite-horizon tube inclusion result for a specified linear error model and fixed ancillary policy. On an embedded two-axis platform (four configurations, seven trials each), the proposed one reaches 3.94±0.10 mrad 2-D pointing RMSE with no command-limit samples at a nominal 100 Hz (submitted to Journal of the Franklin Institute).

### [Physics-Informed and Data-Driven Composite Disturbance Separation and Predictive Control for Airborne Electro-Optical Gimbals with Multiple Constraints](https://arxiv.org/abs/2610.34849)
开源状态 / Code: ✅ 已开源 / Released(部分)— Comments 称演示视频为 arXiv ancillary file;未见代码仓库
- 🇨🇳 机载光电云台在周期与非周期复合扰动、载体振动、输入延迟和执行器约束下做视线稳定与跟踪很困难。方案是扰动分离 MPC:自适应周期观测器用线性回归频率估计预测多谐波振动并嵌入 MPC 模型,线性观测器估计非周期扰动,有界 LSTM 预测其在输入延迟内的变化并在优化器外补偿;给出输入集收紧下的可行性与区域实用跟踪界。UAV 悬停室内试验中偏航/俯仰相对角 RMSE 为 0.770°/0.350°,比线性自抗扰控制分别降低 25.1% 和 45.9%。
- 🇬🇧 Airborne EO gimbals must stabilize and track under composite periodic and aperiodic disturbances, carrier vibration, input delay and actuator limits. The disturbance-separated MPC embeds adaptive-observer multi-harmonic vibration predictions in the MPC model, estimates aperiodic disturbance with a linear observer and predicts its change over the delay with a bounded LSTM applied outside the optimizer, with input-set tightening and a regional practical tracking bound. In UAV-mounted indoor hover trials yaw/pitch relative-angle RMSE are 0.770°/0.350°, reducing error by 25.1% and 45.9% versus linear ADRC.

### [Dual Gradient Consensus for Adaptive Learning to Transient Out-of-Distribution Disturbances in Quadrotor Control](https://arxiv.org/abs/2610.34538)
🏷️ 交叉方向 / Also: 运动控制·RL(学习型残差策略,但无 RL 训练,故归传统自适应控制)
开源状态 / Code: ❓ 未知
- 🇨🇳 四旋翼轨迹跟踪的在线残差自适应中,短暂的域外残差会在常步长更新下污染已学的扰动模型。DGC 保留先前 DAPL 的随机傅里叶特征模型、离线 BPTT 策略与最小二乘自适应,只修改在线步长:把当前残差梯度与长/短期梯度记忆比较,判定适应状态,用置信图抑制不可靠更新并在持续域漂移后恢复适应。四种混合域内/域外残差的数值仿真中,DGC 的平均位置 RMSE 在全部四种情形下都低于 L1 增强 MPC、RFF-MPC、常步长 DAPL 与冻结参数基线(摘要未给出具体数值)。
- 🇬🇧 In online residual adaptation for quadrotor tracking, short out-of-domain residuals corrupt the learned disturbance model under constant-step updates. DGC keeps the prior DAPL's random-Fourier-feature model, offline BPTT policy and least-squares adaptation, and only changes the step size: it compares each residual gradient with long- and short-term gradient memories, classifies the adaptation regime, suppresses unreliable updates with a confidence map and restores adaptation after persistent shifts. In numerical tracking under four mixed in-/out-of-domain residuals, it achieves the lowest mean position RMSE in all four cases versus L1-augmented MPC, RFF-MPC, constant-step DAPL and a frozen baseline (no numbers in the abstract).

### [Learning Direct Control from Optimization for Dynamic Target Tracking (LECO)](https://arxiv.org/abs/2610.34929)
🏷️ 交叉方向 / Also: 运动控制·RL(学习控制策略,但通过可微运动学模型监督,非 RL)
开源状态 / Code: ❓ 未知
- 🇨🇳 动态目标跟踪要求移动机器人在避障的同时保持目标可见并输出平滑可行的控制;在线轨迹优化要反复求解,基于路点的神经策略又把几何预测与控制执行分离。LECO 把跟踪优化迁移为直接控制策略的离线学习:预测控制序列并经可微运动学模型映射为轨迹,使轨迹级目标直接指导控制学习,配以衰减的专家引导课程和在预测不安全时回退经典规划控制的预测安全锁。三种仿真障碍密度下,线性加加速度 RMS 比该指标最优的竞争方法低 14.1–31.2%,跟踪成功率最高,每周期计算 4.25–5.63 ms;两个机器人平台在室内窄通道和室外森林中验证。
- 🇬🇧 Dynamic target tracking needs visibility, obstacle avoidance and smooth feasible controls; online trajectory optimization needs repeated solving while waypoint-based neural policies separate geometry from control. LECO moves the tracking optimization into offline learning of a direct-control policy that predicts control sequences mapped through a differentiable kinematic model so trajectory-level objectives guide learning, with a decaying expert-guidance curriculum and a predictive safety lock that falls back to classical planning and control. Across three simulated obstacle densities it cuts RMS linear jerk by 14.1–31.2% relative to the best competitor on that metric, has the highest tracking success and runs in 4.25–5.63 ms per cycle, with indoor narrow-passage and outdoor forest tests on two platforms.

### [A Differentiable Chassis Safety Layer for Intelligent Vehicle Motion Control](https://arxiv.org/abs/2610.33476)
开源状态 / Code: ❓ 未知
- 🇨🇳 学习型车辆运动控制需要在任务目标与随状态变化的底盘安全约束间协调,级联式安全滤波器独立修改名义指令会损害任务性能。该文提出可微底盘安全层,把执行器限制、单轮胎力约束和车辆操稳包络并入序列二次规划,各投影指令推进预测动力学并更新后续约束,借助隐式微分实现时间梯度耦合,并用专家模仿加风险引导监督与条件干预引导的两阶段学习。在未见场景、紧急机动和消融的闭环评估中改善安全—性能协调并利用车辆动态潜力,同时保持操稳(摘要未给出具体数值)。
- 🇬🇧 Learning-based vehicle control must coordinate task objectives with state-dependent chassis safety constraints, but cascaded safety filters that modify nominal commands independently hurt performance. The paper proposes a differentiable chassis safety layer embedding actuator limits, per-tire force limits and handling envelopes in sequential QPs whose projected commands propagate predicted dynamics and update later constraints, with implicit differentiation providing temporal gradient coupling and a two-stage learning strategy (expert imitation, then risk-guided supervision with conditional intervention guidance). Closed-loop tests in unseen scenarios, emergency maneuvers and ablations show better safety–performance coordination and use of vehicle dynamic potential while keeping handling stable (no numbers in the abstract).

### [How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons](https://arxiv.org/abs/2610.35165)
开源状态 / Code: ❓ 未知(自称可复现仿真研究,但摘要与 Comments 未给出仓库链接)
- 🇨🇳 四旋翼控制器比较通常只报告单一跟踪误差,而排名还取决于调参力度、参考信息、执行器预测、优化器回退与指令时序。该研究在含旋翼陀螺耦合、电机滞后与饱和的公共非线性模型上比较级联 PID、悬停 LQR、边界层滑模、带 LQR 回退的线性 MPC(含预览版)与几何 SO(3) 控制器:主研究 556 个回合(50 Hz),验证研究 1462 个回合。匹配的 12 候选调参把固定基线下的排序改变(边界层滑模从末位到首位),新排序在新实现上重现,48 候选预算也不改变;参考预览显著降低 MPC 误差;回放测得的指令调用延迟使桌面机上四个名义 MPC 配置中的三个终止、树莓派 5 上全部终止,而把求解器限制在 100 次迭代消除了所有测试时序下的超时;最后提出报告清单。
- 🇬🇧 Quadrotor controller comparisons usually report one tracking error, yet rankings depend on tuning effort, reference information, actuator prediction, fallback behavior and command timing. The study compares cascade PID, hover LQR, boundary-layer SMC, linear MPC with LQR fallback (plus a preview version) and a geometric SO(3) controller on a common nonlinear plant with gyroscopic coupling, motor lag and saturation (556 primary episodes at 50 Hz, 1462 confirmation episodes). Matched twelve-candidate tuning reordered the fixed-baseline ranking (BL-SMC from last to first, recurring on fresh realizations and unchanged at 48 candidates), preview substantially cut MPC error, replaying measured command delays terminated three of four nominal MPC configurations on a desktop and all four on a Raspberry Pi 5 while a 100-iteration solver cap removed every deadline miss, and a reporting checklist is proposed.

### [Nonprehensile Robotic Catching Using Virtual Constraints](https://arxiv.org/abs/2610.35851)
开源状态 / Code: ❓ 未知
- 🇨🇳 非抓取式接物的主流方法需要预测物体轨迹并生成时变机器人轨迹。该工作用虚拟非完整约束(VNHC)直接在物体接触前的状态空间里设计并控制末端执行器运动,无需轨迹预测,VNHC 函数只依赖期望接物高度,同一 VNHC 可适用于一批初始条件。在平面情形下可使物体以最小相对法向速度在期望高度被接住,接触后用 MPC 使物体与末端静止于目标位置;仅在仿真中验证(摘要未给出具体数值;拟投 ACC 2027)。
- 🇬🇧 Mainstream nonprehensile catching predicts the object trajectory and generates time-varying robot trajectories. This work designs and controls the end-effector motion directly in terms of the object's state with virtual nonholonomic constraints, avoiding trajectory prediction; the VNHC depends only on the desired catching height and one VNHC serves a range of initial conditions. In the planar case the object is caught at the desired height with minimal relative normal velocity, then MPC brings object and end-effector to rest at a target location; validated in simulation only (no numbers; abridged version submitted to ACC 2027).

### [Nonlinear Control of Aerial Manipulator](https://arxiv.org/abs/2610.34454)
开源状态 / Code: ❓ 未知
- 🇨🇳 带两自由度机械臂并与环境物理交互的四旋翼需要鲁棒的控制器。文中建立完整动力学模型,实现笛卡尔阻抗与自适应滑模两种控制器,在有界扰动下的简单悬停任务中以相同初始条件和期望位置比较。预印本摘要未给出定量结果。
- 🇬🇧 A quadrotor with a two-DOF manipulator that physically interacts with the environment needs robust control. The paper builds a full dynamic model and implements Cartesian impedance and adaptive sliding-mode controllers, compared on a simple hovering task under bounded disturbance with identical initial conditions and desired position. The preprint abstract gives no quantitative results.

### [Trajectory Generation and Control for Quadrotors](https://arxiv.org/abs/2610.34456)
开源状态 / Code: ❓ 未知
- 🇨🇳 该课程项目式工作研究四旋翼的控制器设计与轨迹生成:用微分平坦性,基于路点导航生成最小 snap 轨迹,再用简单 PD 控制器跟踪。仿真给出了平滑的位置与速度轨迹。预印本摘要未给出定量结果。
- 🇬🇧 This project-style paper explores quadrotor controller design and trajectory generation, using differential flatness to produce minimum-snap waypoint trajectories tracked by a simple PD controller. Simulations show smooth position and velocity trajectories. The preprint abstract gives no quantitative results.

### [VisGeo-PipeTrack: A Visual Geometric Servo Control Framework with MPC-RCAPID Control for UAV-Based Dynamic Pipes Tracking](https://arxiv.org/abs/2610.35342)
开源状态 / Code: ❓ 未知
- 🇨🇳 管道巡检 UAV 研究多假设管道静止,而工业场景中管道会振动,对自适应控制与计算效率要求更高。VisGeo-PipeTrack 用 YOLOv5 检测管道标签并由视觉几何约束定位,控制上提出 MPC-RCAPID:用递推最小二乘做实时模型估计并结合滚动时域优化动态调整 PID 参数。AirSim 仿真中,MPC-RCAPID 的调节时间最短(3.26 s)、平均跟踪误差最低(3.52%);Tello 真机上三个维度的平均跟踪误差比标准 PID 分别降低 55.52%、26.72% 和 26.52%(拟投 IEEE TITS)。
- 🇬🇧 UAV pipeline-inspection research mostly assumes static pipes, while real pipes vibrate and demand adaptive, efficient control. VisGeo-PipeTrack detects pipe labels with YOLOv5 to localize via visual geometric constraints and proposes MPC-RCAPID, which uses recursive least squares for real-time model estimation and rolling-horizon optimization to adjust PID parameters. In AirSim it achieves the shortest settling time (3.26 s) and lowest mean tracking error (3.52%), and on a Tello it cuts mean error versus standard PID by 55.52%, 26.72% and 26.52% across three dimensions (submitted to IEEE TITS).

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models(展开 12 / 12 expanded)

### [VISTA: Active Exploration for Self-Improvement in Embodied Agents](https://arxiv.org/abs/2610.35051)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/AgenticEI/VISTA);已匿名验证;[项目页](https://agenticei.github.io/VISTA-page/)
- 🇨🇳 以往方法把 rollout 当作静态日志做事后反思,生成 harness 更新却不自主测试与改进。VISTA 是元 agent 框架,维护记录 harness 谱系的 harness 图,让元 agent 检索先前假设、复用有效机制、避开失败方向,并在环境中主动生成 rollout、探测失败与恢复行为后再修改 harness,新 harness 重新评估后加入图中。在 LIBERO-Pro、RoboCasa、RoboTwin 上持续提升任务成功率,且比静态反思用更少的仿真 rollout 达到更高成功率(摘要未给出具体数值)。
- 🇬🇧 Prior work treats rollouts as static logs for post-hoc reflection and updates harnesses without autonomously testing them. VISTA is a meta-agent framework with a harness graph recording proposal lineage; each iteration actively explores in the environment, probing failures and recoveries before revising the harness, which is then re-evaluated and added to the graph. It progressively improves success on LIBERO-Pro, RoboCasa and RoboTwin and is more rollout-efficient than static reflection (no numbers in the abstract).

### [EmbodiedLab: Benchmarking Embodied Agents That Act to Know](https://arxiv.org/abs/2610.35385)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/HexaFuture/EmbodiedLab)(基准与评测代码,已匿名验证);[项目页](https://hexafuture.ai/benchmarks/embodiedlab/)
- 🇨🇳 现有操作基准只评估「为改变而行动」,科学发现基准又以符号动作取代物理实验。EmbodiedLab 要求机器人「为知而行动」:在基于物理的仿真实验室中,30 个实验、5 个学科、14 种仪器平台,每个实例参数重采样、结果不可预知但可精确评分,通过相机读数,评价 agent 学到了什么及所需物理状态。在六个前沿模型的编码 agent 上评测,原生控制下最强 agent 成功率也不到一半,多数失败发生在与仪器的交互上,蒸馏出的操作技能对较弱 agent 的帮助比增加感知与规划更大。
- 🇬🇧 Manipulation benchmarks stop at acting to change, while scientific-discovery benchmarks replace physical experiments with symbolic actions. EmbodiedLab asks robots to act to know: 30 experiments in five disciplines on 14 apparatus platforms in a physics-based simulated lab, with parameters resampled per instance so results can't be known in advance but are exactly scorable, observed through cameras and evaluated on both what was learned and the required physical state. Across six frontier models in their native coding agents, even the strongest succeeds less than half the time with native control, most failures come from interacting with the apparatus, and distilled manipulation skills help weaker agents more than added perception and planning.

### [RobotAgentBench: Towards Open-world Robot Autonomy](https://arxiv.org/abs/2610.34649)
开源状态 / Code: ❓ 未知([项目页](https://aetherlabsai.github.io/RobotAgentBench/)未核实代码)
- 🇨🇳 VLA 与 WAM 提升了操作能力,但开放世界需要任务发现、上下文推理、物理执行与自适应恢复的闭环自主性,而现有基准只评估孤立能力。RAB 通过 agent 辅助、人在环的实到仿流程构建 50 个家庭布局,含 90 个原子任务、18 个短时程、8 个长时程与 4 个开放场景,分任务级(任务发现、上下文推理、操作、失败恢复、鲁棒性)与场景级评估,并在统一的规划—执行—验证框架下比较独立 VLA/WAM 和不同 agent 架构。实验显示操作与自主性之间有巨大差距,并证明 agentic 架构与递归自我改进的优势(摘要未给出具体数值)。
- 🇬🇧 VLAs and WAMs improve manipulation, but open-world deployment needs closed-loop autonomy spanning task discovery, contextual reasoning, execution and recovery, while existing benchmarks test isolated capabilities. RAB builds 50 household layouts via an agent-assisted human-in-the-loop real-to-sim pipeline with 90 atomic, 18 short-horizon, 8 long-horizon tasks and 4 open-ended scenarios, evaluating five task-level dimensions and scenario-level integration, and compares standalone VLA/WAM and agent architectures in a unified planning–execution–verification framework. Experiments reveal large gaps between manipulation and autonomy and show the advantages of agentic architectures and recursive self-improvement (no numbers in the abstract).

### [Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy](https://arxiv.org/abs/2610.35832)
开源状态 / Code: ❓ 未知([项目页](https://internrobotics.github.io/EBench-Astra-Tech-Report/)为技术报告页)
- 🇨🇳 前沿 MLLM 无需机器人特定训练即可控制机器人,但与后训练 VLA/WAM 策略的能力对比和互动尚未充分评估。该技术报告在 EBench 上以 GPT-6-Astra 为核心,在相同观测协议下研究直接控制(生成路点命令)与「harness + 策略」(还可调用后训练 VLA 或 WAM)两种配置。直接控制总体上与后训练策略相当,在短时程任务上领先、跨泛化维度波动最小,但在长时程、桌面操作和高精度接触任务上较弱;调用策略后总体成功率达到最强对比策略水平并大幅降低 token 成本,但仍低于各组件逐任务上限,原因是调用时机欠佳、无子目标的固定指令执行、以及 agent 接管时破坏抓取。
- 🇬🇧 Frontier MLLMs can control robots without robot-specific training, but their comparison and interaction with post-trained VLA/WAM policies remains under-evaluated. This report evaluates GPT-6-Astra on EBench in two configurations under the same observation protocol: direct waypoint control, and a harness that can also invoke a post-trained VLA or WAM. Direct control is competitive overall (leading on short-horizon tasks and most stable across generalization dimensions, weaker on long-horizon, tabletop and high-precision contact-rich tasks); invoking a policy raises success to the strongest post-trained policies while substantially cutting token cost, yet stays below per-task upper bounds because of suboptimal invocation, fixed-instruction execution without subgoals and grasp disruption on resuming control.

### [How High Can GPT-6 Astra Climb in Contact-Rich Manipulation? PhysLadder](https://arxiv.org/abs/2610.34527)
开源状态 / Code: ❓ 未知
- 🇨🇳 PhysLadder 是分层的仿真—真机配对基准,16 个家居任务分三个累进层级:接触选择与几何对齐(L1)、持续接触中的力调节(L2)、协调的接触重构与力调节(L3),每个任务有物理与视觉匹配的仿真和真实环境及相同成功标准。对 GPT-6 Astra 做零样本评测(每任务各环境 3 次),真机成功率从 L1 的 80.0% 降到 L2 的 47.6% 和 L3 的 0.0%,仿真对应为 66.7%、47.6%、0.0%;16 个任务中 10 个两环境成功次数完全相同,其余 6 个只差 1 次。常见困难在空间推理、接触选择、力调节与协调,说明匹配仿真可作为可重复的测试台。
- 🇬🇧 PhysLadder is a hierarchical matched sim–real benchmark of 16 household tasks over three cumulative levels: contact selection and alignment (L1), force regulation in sustained contact (L2), and coordinated contact reconfiguration with force regulation (L3). Zero-shot GPT-6 Astra (three trials per task per environment) drops from 80.0% (L1) to 47.6% (L2) to 0.0% (L3) in the real world, versus 66.7%, 47.6% and 0.0% in simulation; ten of 16 tasks have identical success counts and six differ by one trial. Recurring difficulties in spatial reasoning, contact selection, force regulation and coordination support matched simulation as a repeatable testbed.

### [ReSight: Task-Driven Self-Improving Memory for Embodied Agents](https://arxiv.org/abs/2610.33487)
🏷️ 交叉方向 / Also: 空间智能与 SLAM / Spatial Intelligence & SLAM(时空记忆)
开源状态 / Code: ❓ 未知
- 🇨🇳 机器人可用历史观测回答时空查询,但相关证据存在不代表现有工具支持任务需要的操作。ReSight 保留关键帧及其时空关联,把观测证据与可扩展的衍生字段分离;执行 agent 在有界在线预算内调用已注册工具,编码 agent 则用可编程工作区和更大探索预算检查证据、写程序、按需获取模型。其 Explore-Distill-Mount 从执行与探索记录中识别能力缺口并转成可复用的记忆构建器、查询工具与技能:OC-NaVQA 平均位置误差从 33.10 m 降到 24.72 m,FindingDory 高层成功率从 38.3% 升到 63.8%,冻结工具后在未参与探索的 FindingDory 回合仍提升 28.3 个百分点,真机巡逻记忆实验中在线工具调用更少。
- 🇬🇧 Robots can use historical observations to answer spatiotemporal queries, but relevant evidence does not mean existing tools support the needed operations. ReSight keeps keyframes with spatiotemporal associations, separates evidence from extensible derived fields, and lets an execution agent call tools within a bounded budget while a coding agent explores in a programmable workspace; Explore-Distill-Mount converts exploration-derived solutions into reusable memory builders, query tools and skills. It reduces mean position error on OC-NaVQA from 33.10 m to 24.72 m, raises FindingDory high-level success from 38.3% to 63.8%, improves by 28.3 points on held-out FindingDory episodes with tools frozen, and uses fewer online tool calls on real-robot patrol memories.

### [RoboReason: Boosting Robotics-Relevant VLM Reasoning Through Scalable Data Generation](https://arxiv.org/abs/2610.33778)
🏷️ 交叉方向 / Also: 空间智能与 SLAM / Spatial Intelligence & SLAM
开源状态 / Code: ❓ 未知(EMNLP 2026 Main)
- 🇨🇳 VLM 已融入机器人操作流水线,但其下游能力的真实评估昂贵。该工作用立体与腕部相机图像定义三类排序任务(按任务描述给打乱的帧排序、按距离给物体深度排序、按像素坐标左右排序),复杂度可由集合大小调节。多个最先进 VLM 在排序任务上表现不佳;提出可扩展的自主训练数据生成流水线,SFT 与 RL 均显著改善时空排序以及下游机器人与视觉推理任务(摘要未给出具体数值)。
- 🇬🇧 VLMs are integrated into manipulation pipelines, but evaluating their downstream ability on real robots is expensive. The paper defines three ordering tasks on stereo and wrist-camera images (ordering shuffled frames given a task description, ordering objects by depth, ordering left-to-right in pixel coordinates) whose difficulty scales with set size; several state-of-the-art VLMs struggle. A scalable autonomous data-generation pipeline lets both SFT and RL significantly improve spatiotemporal ordering and downstream robotics and visual reasoning tasks (EMNLP 2026 Main; no numbers in the abstract).

### [POD-RoPE: Rotary Position Encoding over Physical Observation Distributions for Embodied AI](https://arxiv.org/abs/2610.33745)
开源状态 / Code: ❓ 未知
- 🇨🇳 具身感知需要既捕捉物理几何又捕捉观测的空间与时间范围的位置表示。POD-RoPE 把 token 的观测足迹表示为相机中心、观察方向与采样时间上的分布,期望旋转编码分布间相对关系,分布退化为单点时回到逐点 RoPE;逐 token 预聚合不增加序列长度。把它加入 Fast-WAM 后,RoboTwin 2.0 全部 50 个任务平均成功率从 91.83% 提到 92.88%,Sharpa North 两个真机任务从 32.5% 提到 52.5%;H20 上相对 P-RoPE 与 RayRoPE 的中位前后向加速分别为 1.91 倍与 5.34 倍,相对标准 RoPE 的中位延迟开销 17.4%。
- 🇬🇧 Embodied perception needs positional representations capturing both physical geometry and the spatial/temporal extent of observations. POD-RoPE represents each token's observation footprint as a distribution over camera centers, viewing directions and sampling times, with expected rotations encoding relative relations and recovering pointwise RoPE when distributions collapse; per-token pre-aggregation avoids lengthening sequences. Integrated into Fast-WAM it raises mean success on all 50 RoboTwin 2.0 tasks from 91.83% to 92.88% and on two real-robot tasks on Sharpa North from 32.5% to 52.5%, with median forward-plus-backward speedups of 1.91x over P-RoPE and 5.34x over RayRoPE and 17.4% latency overhead over standard RoPE on H20.

### [Scaling Dexterous Manipulation via Action Representation Pretraining (ARPG)](https://arxiv.org/abs/2610.34453)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知([项目页](https://arpg-project.github.io/)未核实代码)
- 🇨🇳 灵巧操作的动作生成受限于机器人演示稀缺:有限演示既要学动作表示又要学任务条件动作分布。ARPG 把动作表示学习与动作生成分开:先在大规模人类操作数据上预训练动作表示编码器,再冻结编码器、训练一个 130M 参数的紧凑生成骨干来学习编码器空间中的任务条件分布。在 DexJoCo 基准达到 SOTA,双臂灵巧操作平均成功率从 π0.5 的 10.1% 提升到 44.7%;缩放实验表明人类操作行为覆盖越广,下游表现越好。
- 🇬🇧 Dexterous action generation is limited by scarce robot demonstrations that must teach both action representations and task-conditioned distributions. ARPG separates the two: pretrain an action-representation encoder on large-scale human manipulation data, then freeze it and train a compact 130M-parameter generative backbone for task-conditioned distributions in that space. It achieves state-of-the-art on DexJoCo and lifts average bimanual dexterous success from 10.1% for π0.5 to 44.7%, with scaling results showing broader human-behavior coverage improves downstream performance.

### [RoboDoctor: Training-Free Recursive Self-Improvement for Robot Policies](https://arxiv.org/abs/2610.35604)
开源状态 / Code: ❓ 未知([项目页](https://robodoctor-rsi.github.io/)未核实代码)
- 🇨🇳 通才机器人策略与语言模型 agent 能力互补,但完成任务还需根据物理交互后果调整使用方式。RoboDoctor 是免训练框架,把诊断、落地动作与持久经验连接到三个修订目标:harness 分配策略与 agent 之间的控制,干预判断何时介入并保留有用的策略行为,操作根据观测效果改进物理方法;关联的经验记录保留决策原因、尝试方法、结果与复用条件。在 54 个 RoboDojo-Sim 任务条目上五维平均得分 57.10,原生成功率 49.44%;作者指出跨回合经验的贡献仍需受控试验分离。
- 🇬🇧 Generalist robot policies and LM agents are complementary, but completing tasks also requires adapting their use to the consequences of physical interaction. RoboDoctor is a training-free framework linking diagnosis, grounded action and persistent experience across three revision targets: the harness allocates control between policy and agent, intervention decides when to assist while preserving useful policy behavior, and operation refines physical methods from observed effects, with linked experience records keeping reasons, attempts, outcomes and reuse conditions. On 54 RoboDojo-Sim task entries it scores 57.10 on a five-dimension mean with a 49.44% native success rate; controlled trials are still needed to isolate the contribution of cross-episode experience.

### [Tiny Recursive Policy: Recursive Latent Refinement for Visuomotor Control](https://arxiv.org/abs/2610.33288)
开源状态 / Code: ❓ 未知
- 🇨🇳 许多行为克隆策略在每次预测时从固定观测窗口重建内部表示,不保持贯穿执行的持久潜在上下文。TRP 是参数高效的行为克隆策略,结合持久时间状态与递归潜在精炼:每个控制步用共享计算模块反复更新高/低层潜在状态后再解码动作序列,并把状态传给后续预测。在 LIBERO-100、MetaWorld ML45 与 LIBERO-Mem 上多任务与少样本表现有竞争力,在长时程和上下文依赖任务上有显著提升,参数量远少于大型生成基线;消融显示持久状态与递归精炼强相互作用,收益不能由参数量解释(摘要未给出具体数值)。
- 🇬🇧 Many behavior-cloning policies rebuild internal representations from a fixed observation window at every prediction and keep no persistent latent context. TRP is a parameter-efficient BC policy combining persistent temporal state with recursive latent refinement: each control step repeatedly updates high- and low-level latents with a shared module before decoding an action sequence and carries the state forward. It is competitive on LIBERO-100, MetaWorld ML45 and LIBERO-Mem multi-task and few-shot settings and substantially better on long-horizon, context-dependent tasks with far fewer parameters than large generative baselines; ablations show persistent state and recursive refinement interact strongly and the gains are not explained by parameter count alone (no numbers in the abstract).

### [Networked Humanoid Intelligence: Communication, Coordination, Collaboration, and Social Interaction](https://arxiv.org/abs/2610.34740)
🏷️ 交叉方向 / Also: 运动控制 / Motion Control(综述,非控制方法贡献,故留在本类)
开源状态 / Code: ❓ 未知(综述)
- 🇨🇳 综述从通信、协调、协作与社会智能四类信息交换功能,审视互联人形机器人群体,以工厂场景串联,并按交互架构、交换信息、物理耦合、运行时间尺度、系统规模与本体六个维度回顾文献,把物理/仿真人形的结果与其他平台或无实体 agent 的结果分开(后者不能反映平衡、全身运动、接触等人形特有约束)。同时讨论硬件、数据集与基准,区分本地风险与联网引入的风险(如信息过时、不安全知识传播)。结论指出开放问题:控制感知网络、紧凑的以身体为中心的消息、物理落地的协调、网络与本体感知的知识共享、机队级社会一致性、可问责的人类监督。35 页。
- 🇬🇧 This survey examines networked humanoid fleets through four information-exchange functions (communication, coordination, collaboration, social intelligence), tied together by a factory scenario and reviewed along six dimensions (interaction architecture, exchanged information, physical coupling, timescale, scale, embodiment), separating results from physical/simulated humanoids from other platforms or disembodied agents since the latter miss balance, whole-body motion and contact constraints. It also covers hardware, datasets and benchmarks and distinguishes locally handled risks from networking-induced ones such as stale information or unsafe knowledge propagation. It concludes with open problems in control-aware networking, compact body-centric messages, physically grounded coordination, network- and embodiment-aware knowledge sharing, fleet-level social consistency and accountable human oversight (35 pages).

**其余列名 / Also in this category(共 20 条,含上列 12 条)**:[RoboJev](https://arxiv.org/abs/2610.33718)、[AdaPolicy](https://arxiv.org/abs/2610.34280)、[ElevateHead](https://arxiv.org/abs/2610.34031)、[I Won't Know Until I Try](https://arxiv.org/abs/2610.33959)、[Behavioural Quality Is Not Learning Utility](https://arxiv.org/abs/2610.34839)、[FERRET / Environment Edits](https://arxiv.org/abs/2610.35659)、[EAST](https://arxiv.org/abs/2610.34358)、[Labference](https://arxiv.org/abs/2610.35252)。 / 8 more listed by name.

**另见 / See also:** [HuGe](https://arxiv.org/abs/2610.34186)、[ZAP](https://arxiv.org/abs/2610.35817)(已归入 运动控制·RL / filed under Motion Control · RL)。

---

## VLA(展开 7 / 7 expanded)

### [RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions](https://arxiv.org/abs/2610.34356)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/alibaba-damo-academy/RynnVLA-Latent)(已匿名验证);[项目页](https://alibaba-damo-academy.github.io/RynnVLA-Latent.github.io/);HF Daily Papers 9 赞
- 🇨🇳 VLA 受限于带动作标签的演示稀缺与各本体控制空间不兼容。RynnLAM 从视觉转移学习连续的 3D 感知潜在动作,无需原生机器人控制,结合残差未来特征预测、相机补偿 3D 流监督与相机运动解耦;应用于 30.1K 小时人类、机器人与仿真视频,产生 7.4552 亿个潜在动作描述符。随后通过流匹配预测潜在动作块,再适配到具体本体。4B 策略在 LIBERO 上 98.8%,LIBERO-Plus 上 84.7%,五条 VLABench 赛道平均 51.9%,RoboTwin 2.0 双臂平均 88.6%,并在灵巧手与移动夹爪的六个真机任务上成功率最高。
- 🇬🇧 VLAs are limited by scarce action-labeled demonstrations and incompatible control spaces. RynnLAM learns continuous 3D-grounded latent actions from visual transitions without native robot controls, using residual future-feature prediction, camera-compensated 3D-flow supervision and camera-motion decoupling, applied to 30.1K hours of human, robot and simulation videos (745.52M latent-action descriptors); RynnVLA-Latent then predicts latent-action chunks by flow matching and adapts to embodiment-specific actions. The 4B policy gets 98.8% on LIBERO, 84.7% on LIBERO-Plus without benchmark-specific adaptation, 51.9% average across five VLABench tracks and 88.6% on RoboTwin 2.0, and the highest success among compared methods on six real tasks across dexterous-hand and mobile-gripper platforms.

### [EXE: Egocentric Cross-Embodiment Pretraining via Factorized Latent Actions for VLA Models](https://arxiv.org/abs/2610.33685)
开源状态 / Code: ❓ 未知
- 🇨🇳 VLA 受限于机器人数据稀缺,第一视角人类操作视频丰富,但存在本体差距。EXE 从人类视频学习分解的潜在动作表示,把共享操作先验(够取、抓取、放置)与本体特有信号分离,避免人类特有运动模式干扰机器人策略学习,同一预训练同时惠及平行夹爪与灵巧手。相对无预训练基线,在 RoboTwin 2.0、RoboCasa GR1 和真机操作任务上都取得一致提升(摘要未给出具体数值)。
- 🇬🇧 VLAs are bottlenecked by robot data scarcity, and egocentric human videos are abundant but suffer an embodiment gap. EXE learns a factorized latent action representation from human videos that separates shared manipulation priors (reaching, grasping, placing) from embodiment-specific signals so human-specific kinematics don't bias the robot policy, benefiting both parallel grippers and dexterous hands. It yields consistent gains over no-pretraining baselines on RoboTwin 2.0, RoboCasa GR1 and real manipulation tasks (no numbers in the abstract).

### [VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware](https://arxiv.org/abs/2610.34717)
开源状态 / Code: ❓ 未知
- 🇨🇳 VLA 在机器人边缘设备上的推理延迟限制闭环控制,但如何设计模型、软件与硬件仍不清楚。该基准在 Jetson AGX Thor 与 AMD Ryzen AI Max+ PRO 395 上用七阶段推理分解测试 18 个开源 VLA。发现:动作生成策略比模型大小更重要(在 19 个 Jetson 配置中的 14 个起主导,延迟在 Jetson 上差 82 倍、AMD 上差 157 倍,参数量至多解释 15% 的延迟方差);核融合加 4-bit 权重收益最大,使 π0.5 与 GR00T N1.7 比 torch.compile 快 2.6–2.9 倍,但只覆盖这两款模型且仅限 Jetson;优化后 CPU 预处理占比从 12% 升到 39%。结论是低延迟边缘 VLA 应使用少量动作生成迭代。
- 🇬🇧 VLA inference latency on robot edge devices constrains closed-loop control, yet design guidance is unclear. The benchmark profiles 18 open VLA models on Jetson AGX Thor and AMD Ryzen AI Max+ PRO 395 with a seven-stage breakdown: action-generation strategy matters more than model size (dominating 14 of 19 Jetson configurations, with latency varying 82x on Jetson and 157x on AMD and parameter count explaining at most 15% of variance); kernel fusion with 4-bit weights helps most, running π0.5 and GR00T N1.7 2.6–2.9x faster than torch.compile but only for these two models on Jetson, and CPU preprocessing grows from 12% to 39% of the GR00T N1.7 call after optimization. Low-latency edge VLAs should use few action-generation iterations.

### [TRIAGE: Efficient Vision-Language-Action Inference Needs Both Reuse and Pruning](https://arxiv.org/abs/2610.34519)
开源状态 / Code: ❓ 未知
- 🇨🇳 板载嵌入式设备上 VLA 的预填充延迟随每个控制步数百个视觉 token 增长,现有免训练加速要么剪枝要么复用 KV 缓存,对所有跳过的 token 只用其一。通过逐 token 诊断发现,哪种选择更接近完全重算取决于 token 的漂移(浅层 value 相对缓存时的变化):低于阈值时复用不差于剪枝,超过后复用的动作误差最高达剪枝的 4.4 倍。TRIAGE 据此在固定预算内重算重要且缓存无效的 token,复用缓存有效者,剪掉其余。LIBERO 与 SimplerEnv 上平均成功率与完全重算相差不超过 3 个百分点,Jetson AGX Orin 预填充延迟最多降低 48%;只重算 7% 视觉 token 时比最强基线在 LIBERO-Object 上高 24.4 个百分点。
- 🇬🇧 On embedded boards, VLA prefill latency grows with the hundreds of visual tokens per control step, and training-free accelerators either prune or reuse cached KV states for all skipped tokens. A token-level diagnostic shows the better option depends on token drift (change in shallow-layer value since caching): below a threshold reuse is no worse than pruning, above it reuse gives up to 4.4x the action error. TRIAGE recomputes a fixed budget of important tokens with invalid caches, reuses valid ones and prunes the rest; on LIBERO and SimplerEnv it stays within 3 pp of full recomputation while cutting Jetson AGX Orin prefill latency by up to 48%, and with only 7% of tokens recomputed beats the strongest baseline by 24.4 pp on LIBERO-Object.

### [RoboDuo: Attempt, Check and Atomic Recovery through Code for Vision-Language-Action Models](https://arxiv.org/abs/2610.34108)
开源状态 / Code: ❓ 未知
- 🇨🇳 VLA 不检查指令是否完成,长时程任务中单步失败无人察觉,但失败回合常已部分完成,未完成步骤是可复用的原子技能。RoboDuo 是闭环双系统框架,以代码为接口:编码 agent 写程序,让全任务 VLA 尝试整个任务并检查是否完成,失败时由原子 VLA 完成剩余步骤;agent 不输出动作,故可不更新权重地包装现有 VLA,并从一套 LIBERO 演示构建 LIBERO-Atomic/Code/Judge 训练数据。在 LIBERO 与 LIBERO-PRO 上一致提升 X-VLA 与 π0.5,长时程任务提升最大,真机上可恢复冻结全任务 VLA 的失败回合(摘要未给出具体数值)。
- 🇬🇧 VLAs never check whether an instruction was completed, so a failed step in a long-horizon task goes unnoticed, yet failed episodes often end partially complete with unfinished steps being reusable atomic skills. RoboDuo is a closed-loop dual-system framework using code as the interface: a coding agent writes a program letting a full-task VLA attempt the task and check completion, and an atomic VLA finishes remaining steps on failure; since the agent emits no actions it wraps existing VLAs without weight updates, with LIBERO-Atomic/Code/Judge built from one set of LIBERO demonstrations. It consistently improves X-VLA and π0.5 on LIBERO and LIBERO-PRO (largest on long-horizon tasks) and recovers failed rollouts of a frozen VLA on a real robot (no numbers in the abstract).

### [JevVLA: Jev-Inspired Energy-Based Adaptation for Vision-Language-Action Policies](https://arxiv.org/abs/2610.35010)
开源状态 / Code: ✅ 仓库已可访问 / Repo reachable — [仓库](https://github.com/ZJU4EmbodiedAI/JevVLA)(匿名 `git ls-remote` 成功;摘要称 will be open-sourced,实际含哪些内容待核实)
- 🇨🇳 需要在保留预训练能力的前提下,用统一机制同时改进 VLA 的离散候选选择和连续动作块生成。JevVLA 冻结基础策略,学习以观测、任务上下文和动作为条件的可微标量能量,建模动作提议的相对质量(来自执行反馈、专家纠正或演示偏好),能量值比较离散候选,动作梯度修正或引导连续动作,核心网络约 8 万可训练参数。留出测试集上相对匹配基线在 MetaWorld MT50、VIMA、LanguageTable、LIBERO Plus、CLIPort 上分别提升 1.28、2.31、1.60、1.52、1.28 个百分点。
- 🇬🇧 The goal is to improve both discrete candidate selection and continuous action-chunk generation of a VLA through one mechanism while retaining pretrained capabilities. JevVLA freezes the base policy and learns a differentiable scalar energy over observations, task context and actions that models relative action-proposal quality (from execution feedback, expert corrections or demonstration preferences); energy values compare discrete candidates and action gradients correct or guide continuous actions, with about 80,000 trainable parameters. On held-out sets it improves success over matched base-policy controls by 1.28, 2.31, 1.60, 1.52 and 1.28 pp on MetaWorld MT50, VIMA, LanguageTable, LIBERO Plus and CLIPort.

### [Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies](https://arxiv.org/abs/2610.35626)
🏷️ 交叉方向 / Also: 空间智能与 SLAM / Spatial Intelligence & SLAM(3DGS)
开源状态 / Code: ❓ 未知([项目页](https://001-wang.github.io/PrecisionReach-GS/)未核实代码)
- 🇨🇳 电子垃圾拆解中,机器人需精确末端定位,而全数字孪生仿真难以获得薄、反光、结构复杂零件的网格与接触模型。该工作聚焦接触前够取,用 3DGS 重建真实工作空间,从机器人对齐位姿渲染多样腕部相机观测并配以平滑结构化的够取轨迹,为 VLA 微调提供视觉—动作监督,再加指令条件的够取验证器估计目标接近度并提供可靠终止。主板拆解实验中,π0.5 用 1,500 条生成轨迹达到 80.0% 精确够取成功率,而 150 条遥操作演示为 58.7%,且主动人工采集不到 10 分钟。
- 🇬🇧 In e-waste disassembly robots need accurate end-effector positioning, but full digital twins are hard for thin, reflective, complex parts. The work focuses on pre-contact reaching: it reconstructs the workspace with 3DGS, renders diverse wrist-camera observations from robot-aligned poses paired with smooth structured reaching trajectories as VLA fine-tuning supervision, and adds an instruction-conditioned reach verifier estimating target proximity for reliable termination. In motherboard disassembly, π0.5 with 1,500 generated trajectories reaches 80.0% precise-reaching success versus 58.7% with 150 teleoperated demonstrations, with under 10 minutes of active human capture.

**其余列名 / Also:** [PS-DLO](https://arxiv.org/abs/2610.34147)(可变形线性物体操作策略)、本类共 8 条,其中 7 条已展开。 / 8 total, 7 expanded.

---

## VLN(展开 5 / 5 expanded)

### [MOON: Learning When to Forget and How to Move On in Vision-and-Language Navigation](https://arxiv.org/abs/2610.33546)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/AutoLab-SAI-SJTU/MOON)(已匿名验证)
- 🇨🇳 VLN 策略依赖视觉历史,一次错误动作会使其偏离路线;成对干预显示偏离初期清空历史使汇总成功率翻倍,但在路线上会降低,而偏离后期只删除偏航帧收益小得多,作者称之为「行为惯性」。MOON 给冻结 VLN 策略加两个轻量模块(参数不到 1%):偏离判断器决定何时遗忘并清空历史,恢复策略用 GRPO 从告警状态训练学会如何继续前进。R2R-CE 与 RxR-CE 上成功率分别比冻结基础提高 5.2 和 6.0 个百分点,R2R-CE 上取得对比方法中最高成功率,无需重训即可提升 HM3D-OVON 零样本物体目标导航;随机触发的消融说明收益取决于清空历史的时机。
- 🇬🇧 VLN policies act on visual history, so a wrong action can take them off route; paired interventions show clearing history doubles pooled success at deviation onset but lowers it on route, and later removing only off-route frames helps much less ("behavioral inertia"). MOON adds two lightweight modules (under 1% of parameters) to a frozen policy: a deviation judge that decides when to forget and a recovery policy trained with GRPO from alarm states to learn how to move on. It raises R2R-CE and RxR-CE success of its frozen base by 5.2 and 6.0 points, reaches the highest R2R-CE success among compared methods, improves zero-shot object-goal navigation on HM3D-OVON without retraining, and a random-trigger ablation shows the gain depends on timing.

### [One Scan is Enough: Demonstration-Free Adaptation for Language-Guided Navigation](https://arxiv.org/abs/2610.33794)
开源状态 / Code: ❓ 未知(NeurIPS 2026;无代码链接)
- 🇨🇳 在新建筑中部署语言导航策略通常要先看它失败,再靠现场遥操作采集轨迹,难以扩展。该工作用一次简短 iPhone 扫描代替人类演示:Scan2Instruction 把扫描编译成完整训练环境并自动合成可执行导航回合与落地指令,PRPT-KS 则通过直接从重建场景读出的闭式 Pareto 效用适配策略,无需学习的 critic 或人工标签。五个真实环境中 RealNav 真机成功率 85%,而用人类演示后训练的基线为 49%;同一建筑未扫描区域仍有 82%,基线为 41%。
- 🇬🇧 Deploying a language-guided navigation policy in a new building usually means watching it fail and teleoperating fresh trajectories on site. Scan2Instruction compiles a single brief iPhone scan into a full training environment with automatically synthesized executable episodes and grounded instructions, and PRPT-KS adapts the policy via a closed-form Pareto utility read directly from the reconstructed scene, with no learned critic or human labels. Across five real environments RealNav reaches 85% real-robot success versus 49% for a baseline post-trained on human demonstrations, and 82% versus 41% in unscanned regions of the same buildings (NeurIPS 2026).

### [RetroNav: Scene-Grounded Retrospection and Retry for Self-Evolving Lifelong Navigation](https://arxiv.org/abs/2610.35172)
开源状态 / Code: 🕒 计划开源 / Planned — 摘要称「will be open-sourced at」[计划仓库](https://github.com/3dv-casia/RetroNav);匿名访问不到,尚无可用代码
- 🇨🇳 现有终身导航方法侧重场景知识积累,却忽视历史导航经验及其与场景证据的联系,难以反思过去错误。RetroNav 是免训练的自进化导航框架,把导航、记忆积累与失败反思结合:统一记忆系统连接几何与语义场景知识和历史导航经验,并区分客观观测与任务相关解读;每次尝试后独立评估器判断是否需要重试,回顾 agent 结合场景知识与导航记录重审历史决策,生成基于证据的重试简报。在五个导航基准上取得 SOTA(摘要未给出具体数值)。
- 🇬🇧 Lifelong navigation methods focus on scene knowledge and neglect historical navigation experience and its link to scene evidence, limiting reflection on past mistakes. RetroNav is a training-free self-evolving framework combining navigation, memory accumulation and failure reflection: a unified memory connects geometric and semantic scene knowledge with navigation history while separating objective observations from task-dependent interpretations, an independent evaluator decides on retry, and a Retrospection Agent revisits past decisions to write an evidence-grounded retry brief. It achieves state-of-the-art on five navigation benchmarks (no numbers in the abstract).

### [ScheNav: Schematic-Guided Object Goal Navigation](https://arxiv.org/abs/2610.34286)
开源状态 / Code: ❓ 未知
- 🇨🇳 人类常借助粗略草图或方向标注等低成本示意图导航,而物体目标导航缺乏利用它们的方法。该工作提出数据生成流水线(把 2D 户型图变为导航训练环境,得到 3.3 万+ 带家具布局的 Furnished-RPLAN 及配对回合与可控噪声示意图)和闭环框架 ScheNav,其 SchemaField 学习型空间模块融合示意引导与累积观测并预测空间价值场,配合轨迹级训练与跨帧一致性目标。完全在仿真户型图上学会使用示意引导并迁移到未见具身环境;在多种示意图、目标椭圆和指向方向上提升成功率与路径效率,并容忍所测的示意图扰动与缺失(摘要未给出具体数值)。
- 🇬🇧 Humans navigate with cheap schematic maps such as sketches or directional annotations, but object-goal navigation lacks ways to use them. The paper builds a data pipeline turning 2D floorplans into navigation environments (Furnished-RPLAN, 33k+ furnished layouts with paired episodes and noise-controllable schematics) and ScheNav, a closed-loop framework whose learned SchemaField fuses guidance with accumulated observations to predict spatial value fields, trained with trajectory-based learning and a cross-frame consistency objective. It learns to use schematics entirely from simulated floorplans and transfers to unseen environments, improving success and path efficiency across schematic maps, goal ellipses and pointed directions with tolerance to tested perturbations and omissions (no numbers in the abstract).

### [Preemptive Instruction Following with Resumption (PIFR)](https://arxiv.org/abs/2610.35576)
开源状态 / Code: ❓ 未知
- 🇨🇳 长时程具身导航可能被更高优先级指令打断,agent 必须完成当前原子任务、执行插入任务,再在视角与可用导航候选已变化的环境状态下恢复原序列。PIFR 基准涵盖单次、重复与嵌套打断,并给出插入任务完成、原任务恢复与整序列完成的分阶段指标。评测显示恢复表现随打断条件而异,总体成功率会掩盖打断处理与恢复上的差异;并提出轻量候选排序基线改善打断后的目标重落地(摘要未给出具体数值)。
- 🇬🇧 Long-horizon embodied navigation can be interrupted by higher-priority instructions: the agent must finish its current atomic task, execute the inserted task, and resume the remaining sequence where the viewpoint and navigation candidates may have changed. The PIFR benchmark covers single, repeated and nested interruptions with stage-specific metrics for inserted-task completion, resumption and full-sequence completion. Evaluations show recovery varies across interruption conditions and aggregate success obscures these differences; a lightweight candidate-ranking baseline improves target re-grounding after interruption (no numbers in the abstract).

**其余列名 / Also:** [Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation](https://arxiv.org/abs/2610.34674)、[SCET-CBF](https://arxiv.org/abs/2610.33471)(动态导航,共 7 条含上列 5 条)。

---

## 世界模型与 WAM / World Models & WAM(展开 8 / 8 expanded)

### [What Does World Modeling Actually Improve in Robot Action Learning?](https://arxiv.org/abs/2610.34593)
开源状态 / Code: ❓ 未知
- 🇨🇳 WAM 把未来视频预测与机器人动作学习结合,但仅看成功率无法说明预测监督如何体现在执行行为上、收益在任务与环境变化下是否持续。该研究在 FastWAM 与 OpenWAM 内做受控的未来视频预测损失消融,保持架构、初始化、数据和训练步数不变。干净条件下已见任务上,预测监督使成功率分别提高 24.38 和 72.91 个百分点,但在分布偏移下收益不一致;把未来视频预测作为 π0.5 的辅助训练目标(仅训练时用的轻量 Transformer 预测器)使成功率从 82.94% 升到 89.19%,说明收益不一定依赖大型预训练视频 DiT。
- 🇬🇧 WAMs combine future-video prediction with action learning, but success alone doesn't show how predictive supervision changes execution or whether benefits persist under shifts. Controlled future-video-loss ablations within FastWAM and OpenWAM (fixed architecture, initialization, data, steps) show predictive supervision raises seen-task success by 24.38 and 72.91 percentage points respectively, while benefits on unseen tasks and environmental randomizations are inconsistent. Adding future-video prediction as an auxiliary objective for π0.5 via a train-time-only lightweight Transformer raises success from 82.94% to 89.19%, so such gains need not rely on a large pretrained video DiT.

### [OSWAM: An Effective World Action Model with One-Step Action Generation](https://arxiv.org/abs/2610.35850)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(也用于自动驾驶)
开源状态 / Code: ❓ 未知([项目页](https://gwenzhang.github.io/OSWAM/)未核实代码)
- 🇨🇳 直接策略 WAM 需要数十步去噪才能得到有竞争力的动作,延迟大;简单减少步数会使非线性去噪轨迹塌缩为粗略更新。作者认为问题在于随机噪声初始化缺少结构化动作先验,于是构造「想象 token」初始化扩散过程,提供物理先验与动作条件表示,并引入带未来条件的特权信息蒸馏。OSWAM 一步扩散即可生成高质量动作,在自动驾驶与具身控制上达到或优于需要数十步的直接策略 WAM 与联合 WAM,相对直接策略 WAM 基线约 3 倍加速,在 RTX 5090 上编译推理延迟低至 40 ms。
- 🇬🇧 Direct-policy WAMs need tens of denoising steps for competitive actions, adding latency, and simply cutting steps collapses the nonlinear denoising trajectory. The authors argue random noise initialization lacks structured action priors, so they initialize diffusion with imagination tokens providing physical priors and action-conditioned representations and add privileged-information distillation with future conditioning. OSWAM generates high-quality actions in one diffusion step, matching or beating direct-policy and joint WAMs that need tens of steps in both autonomous driving and embodied control, with about 3x speedup over direct-policy WAM baselines and latency as low as 40 ms on an RTX 5090.

### [Video World Models Need Predictable Latents](https://arxiv.org/abs/2610.34663)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/mattia-scardecchia/predictable-latents)(已匿名验证,radar new_repos 中出现)
- 🇨🇳 视频世界模型常在重建训练的自编码器潜空间中预测,未针对动力学建模优化;潜在规划的世界模型虽优化可预测性,却放弃像素空间预测。该文表明时间性表示学习目标配合以过去为条件的解码器架构,能在同等训练预算下一致改进生成式视频世界模型:推理最多便宜 5 倍、训练快 7 倍以上、分布外和长时程像素与感知误差降低 15–24%。其世界模型与用 VLM 从像素预测判断任务成功的真实策略评估也更一致(54 页;cs.LG 交叉列表)。
- 🇬🇧 Video world models usually predict in the latent space of a reconstruction-trained autoencoder not optimized for dynamics, while latent-planning world models optimize predictability but forgo pixel-space prediction. The paper shows temporal representation-learning objectives paired with a past-conditioned decoder consistently improve generative video world models at the same training budget: up to 5x cheaper inference, over 7x faster training and 15–24% lower pixel and perceptual errors out of distribution and over long horizons. The resulting models also agree more closely with real-world policy evaluation when a VLM judges task success from pixel predictions (54 pages; cs.LG cross-list).

### [RoboWorM: Evaluating Movement Realism, Consistency and Acceleration Affects in Embodied Video World Models](https://arxiv.org/abs/2610.33807)
开源状态 / Code: ❓ 未知
- 🇨🇳 视频世界模型正成为操作的可扩展神经模拟器,但多数基准把它们当开放世界视频生成器,用缺乏严格 3D 与运动学推理的 VLM 评估。RoboWorM 利用机器人运动学树与固定相机配置等硬件先验,整理单臂、双臂与人形 1,605 个回合,并提出无 VLM 的确定性指标 KIVA(单视角运动学稳定性)与 RIGIS(多视角几何一致性)。KIVA 的幻觉检测与人工标注的一致性比最强前沿 VLM 提高 25.8%,RIGIS 与人类偏好的 Spearman 相关高 130%;对 3 个世界模型上 9 种加速技术(超过 29,000 次 rollout)的审计显示它们可能保持表面视觉质量却悄悄损害物理约束,最大 2.3 倍加速且质量损失小。
- 🇬🇧 Video world models are emerging as scalable neural simulators for manipulation, but benchmarks mostly score them as open-world video generators with VLMs lacking strict 3D and kinematic reasoning. RoboWorM uses hardware priors (robot kinematic trees, fixed cameras) over 1,605 single-arm, bimanual and humanoid episodes and proposes VLM-free deterministic metrics KIVA (intra-view kinematic stability) and RIGIS (multi-view geometric consistency). KIVA improves hallucination-detection alignment with human annotation by 25.8% over the strongest frontier VLMs and RIGIS gets 130% higher Spearman correlation with human preference; auditing 9 acceleration techniques on 3 world models (29,000+ rollouts) shows they can keep superficial quality while silently compromising physical constraints, with up to 2.3x speed-up at minimal loss.

### [WorldFailBench: Do World Models Understand Policy Failures?](https://arxiv.org/abs/2610.33565)
开源状态 / Code: ❓ 未知
- 🇨🇳 世界模型可通过生成环境中的闭环交互评估机器人策略,但仅看成败不能证明其忠实再现策略如何失败。WorldFailBench 设三类任务:失败原因(是否复现可观测错误)、失败阶段(失败是否集中于相同阶段)、失败边界(受控场景变化下成败转换的条件);覆盖 LIBERO、RoboTwin 仿真操作及 G1 人形真实操作任务。对七个世界模型的实验显示,它们对策略失败的理解存在显著差距(摘要未给出具体数值)。
- 🇬🇧 World models can evaluate robot policies through closed-loop interaction in generated environments, but outcome-only evaluation doesn't show whether they faithfully simulate how policies fail. WorldFailBench has three tasks (failure reason, failure stage, failure boundary under controlled scene changes) over LIBERO and RoboTwin simulation and real G1 humanoid manipulation. Experiments on seven world models reveal substantial gaps in understanding policy failures (no numbers in the abstract).

### [X-World: Transferring Video Priors to Variable-View Robot Control](https://arxiv.org/abs/2610.34105)
开源状态 / Code: ❓ 未知
- 🇨🇳 视频扩散模型能为机器人控制提供交互表示,但迁移需协调可变相机输入、异构动作接口与闭环执行。X-World 通过固定长度 token 序列把视频先验传给共享动作专家:残差跨视角注意力分支把预训练视频骨干扩展到 1–3 个视角,层对齐 Q-Former 聚合特征,数据集专属模块映射原生状态与动作接口;训练分视频适配与冻结骨干的纯动作预训练两阶段,再联合目标域后训练,推理单次骨干前向并用异步动作分块。LIBERO 平均 98.5%,LIBERO 训练检查点在 LIBERO-Plus 上 76.5%;六个双臂真机任务每任务 20 次试验平均 81.7%;相机、背景和噪声偏移下相对 OpenVLA-OFT 有弱点。
- 🇬🇧 Video diffusion models offer interaction representations for robot control, but transfer must reconcile variable camera inputs, heterogeneous action interfaces and closed-loop execution. X-World passes a video prior through a fixed-length token sequence to a shared action expert, with a residual cross-view attention branch extending the backbone to one to three views, a layer-aligned Q-Former, dataset-specific state/action modules, two-stage training (video adaptation, then action-only pretraining with a frozen backbone) plus joint post-training, and a single backbone pass with asynchronous action chunking. It reaches 98.5% mean success on LIBERO, 76.5% on LIBERO-Plus from its LIBERO checkpoint, and 81.7% mean success over 20 trials on six real dual-arm tasks, with weaknesses under camera, background and noise shifts relative to OpenVLA-OFT.

### [Adapt for Planning, Not just Prediction: Optimistic Test-Time World Model Adaptation (OpTTA)](https://arxiv.org/abs/2610.35636)
开源状态 / Code: ❓ 未知(CoRL 2026 Workshop)
- 🇨🇳 潜在世界模型离线预训练并在测试时冻结,分布偏移下规划会退化;仅用预测损失做测试时适应,模型只拟合自己动作的结果,可能仍不了解能达成目标的动作。OpTTA 受自适应控制中奖励偏置极大似然启发,目标含观测转移预测损失和规划器候选 rollout 的目标到达代价两项,使适应偏向对到达目标乐观的模型,无需额外交互。在操作、到达和导航的视觉/环境偏移上,仅适应预测器时规划成功率平均比冻结模型高 13.5 个百分点,预测-only 目标(AdaJEPA)为 6.9;同时适应编码器时分别为 13.5 和 7.5,涵盖三种 JEPA 世界模型及 CEM 与基于梯度的规划器。
- 🇬🇧 Latent world models are pretrained offline and frozen at test time, so planning degrades under shift, and a prediction-only adaptation objective fits only the outcomes of the model's own actions. Inspired by reward-biased maximum likelihood from adaptive control, OpTTA minimizes the prediction loss on observed transitions plus the planner's goal-reaching cost on candidate rollouts, biasing adaptation toward models optimistic about reaching the goal without extra interaction. Across visual and environment shifts on manipulation, reaching and navigation, adapting only the predictor raises planning success over the frozen model by 13.5 pp on average versus 6.9 for prediction-only AdaJEPA (13.5 vs 7.5 when the encoder is adapted too), across three JEPA world models and CEM and gradient-based planners (CoRL 2026 Workshop).

### [DriveUniTok: A Unified Multimodal Tokenizer for Driving World-Action Models](https://arxiv.org/abs/2610.35044)
开源状态 / Code: ❓ 未知(驾驶领域,与机器人相关度较低,仅作世界—动作模型参考)
- 🇨🇳 现有方法对外观、投影 LiDAR 深度表示的度量几何和自车运动往往部分或独立建模,导致信息损失与跨模态不一致。DriveUniTok 把这些模态编码进单一可解码连续潜变量;冻结后适配预训练扩散模型 DriveUniWAM 预测未来统一潜变量,再解码为未来外观、投影 LiDAR 深度与自车轨迹。在 NAVSIM 上统一设计比分离流以更低下游计算获得更好的未来预测与规划;经 RL 后训练,DriveUniWAM 的 PDMS 达 91.54,是所评基于 WAM 的规划器中最佳。
- 🇬🇧 Existing approaches model appearance, projected-LiDAR metric geometry and ego motion partially or independently, causing information loss and cross-modal inconsistency. DriveUniTok encodes them in a single decodable continuous latent; with it frozen, a pretrained diffusion model (DriveUniWAM) predicts future unified latents decoded into appearance, projected LiDAR depth and ego trajectories. On NAVSIM the unified design gives better future prediction and planning at lower downstream cost than separate streams, and with RL post-training DriveUniWAM reaches a PDMS of 91.54, state-of-the-art among evaluated WAM-based planners.

**其余列名 / Also:** [Dream to Assist](https://arxiv.org/abs/2610.34650)(意图条件世界模型,车辆共享控制,model-based RL)。共 9 条(8 条已展开)。 / 9 total.

**另见 / See also:** [HumanoidNDM](https://arxiv.org/abs/2610.34126)(神经动力学模型,已归入 运动控制·RL / filed under Motion Control · RL)。

---

## 空间智能与 SLAM / Spatial Intelligence & SLAM(展开 7 / 7 expanded)

### [Behavior Spatial Benchmark: Evaluating Spatial Understanding for Robotics (BEHAVIOR-Spatial)](https://arxiv.org/abs/2610.34051)
开源状态 / Code: ❓ 未知([项目页](https://arielchen07.github.io/behavior-spatial/)未核实代码)
- 🇨🇳 机器人任务需要把空间语言落地到物理场景,但仅看任务成功无法证明空间指令被遵循。基于 BEHAVIOR-1K,该基准度量空间问答、基于点的目标落地与机器人动作,以研究 VLM 空间理解与 VLA 行为的关系:3,256 个跨 49 个活动的空间问题、1,240 个跨 14 个操作任务的落地查询,以及覆盖 14 个操作与 10 个导航任务的动作评估。基线在留出配置上 41.6%,指令改变时仅 16.1%;VLM 适配与机器人数据预训练提升有限,而提供真值视觉目标线索可把这两个数分别提到 60.3% 和 38.0%。
- 🇬🇧 Robot tasks require grounding spatial language in physical scenes, but task success alone doesn't show spatial instructions are followed. Built on BEHAVIOR-1K, the benchmark measures spatial QA, point-based grounding and robot action to relate VLM spatial understanding to VLA behavior: 3,256 questions over 49 activities, 1,240 grounding queries over 14 manipulation tasks, and action evaluations over those 14 plus 10 navigation tasks. The baseline gets 41.6% on held-out configurations but only 16.1% when the requested target changes; VLM adaptation and robot-data pretraining help little while oracle visual target cues raise these to 60.3% and 38.0%.

### [Bracketing Shows the Way: Adaptive Multi-Exposure Policy as Input for Robust Visual SLAM](https://arxiv.org/abs/2610.33174)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/norlab-ulaval/bracketing-shows-the-way)(已匿名验证)
- 🇨🇳 快速光照过渡会在自动曝光策略适应前使图像饱和,破坏视觉 SLAM 所需的对应。B-Adapt 采集自适应曝光包围以覆盖场景动态范围并促进光度重叠,BVSLAM 则把多曝光序列作为因子图状态估计器的约束,不依赖 HDR 合成。在 32 m/s 模拟车速的隧道出口过渡中,B-Adapt 与 BVSLAM 结合使状态估计误差比自动曝光图像降低 78%,常规环境下误差仍低(ICRA 2027 投稿)。
- 🇬🇧 Rapid illumination transitions saturate images before auto-exposure adapts, removing correspondences visual SLAM needs. B-Adapt acquires adaptive exposure brackets covering the scene dynamic range while promoting photometric overlap, and BVSLAM uses the multi-exposure sequence directly as factor-graph constraints without HDR merging. In a repeated tunnel-exit transition at an emulated 32 m/s, combining them reduces state-estimation error by 78% versus auto-exposure images while keeping low error in nominal conditions (submitted to ICRA 2027).

### [Memory-Aware Keyframe Management for Dense Maps on Memory-Constrained Robots](https://arxiv.org/abs/2610.33574)
开源状态 / Code: ❓ 未知(ICRA 2027 投稿)
- 🇨🇳 语言模型与稠密 3D 地图共用一台设备的内存,超限会 OOM,而按关键帧数量限制的工作集无法控制实际占用。该工作直接限定常驻地图内存,用离线计算的逐关键帧驻留大小在读取前已知每次准入的代价,并以房间和走廊等语义空间单元为粒度准入/释放关键帧。两块 NVIDIA Jetson 板上预算每次运行都成立,模型吞吐至多损失 0.8%,而无此机制时操作系统会杀掉模型或地图;在同等预算下按语义区域准入比同区域数的几何划分多定位 6–9 个点的查询帧,约为 RTAB-Map 检索的两倍且 ATE 更低。
- 🇬🇧 When a language model and a dense 3D map share one device's memory, exceeding the limit causes OOM, and keyframe-count bounds don't control actual occupancy. The method bounds resident map memory directly using offline per-keyframe resident sizes so admission cost is known before reading, and admits/releases keyframes by semantic spatial unit (rooms, corridors). On two Jetson boards the budget holds in every run with at most 0.8% throughput loss for the model (without it the OS kills the model or map), and under that budget semantic-zone admission localizes 6–9 points more query frames than a geometric partition and about twice as many as RTAB-Map retrieval, at lower ATE (submitted to ICRA 2027).

### [Resilient Decentralized Radar-LiDAR-Inertial Odometry in Challenging Subterranean Environments](https://arxiv.org/abs/2610.35363)
开源状态 / Code: ❓ 未知
- 🇨🇳 烟、尘、雾下 LiDAR 性能下降,FMCW 雷达稳健但稀疏且含离群点。该文提出去中心化 LiDAR–雷达–惯性里程计:自适应残差阈值(ART)自动检测传感器暂时退化并选择性调整融合,鲁棒容错最优信息滤波器(RETOIF)在去中心化架构中以故障感知方式融合 LiDAR-惯性与多路雷达-惯性里程计估计。真实地下隧道无烟实验中 RMSE 为 2.1733,传统集中式 LRIO 为 2.9929(降低 27.4%),并在烟雾退化下保持位姿估计。
- 🇬🇧 LiDAR degrades under smoke, dust and fog while FMCW radar is robust but sparse and outlier-prone. The decentralized LiDAR-radar-inertial odometry framework uses Adaptive Residual Thresholding (ART) to detect temporal sensor degradation and adjust fusion selectively, and a Robust Error-Tolerant Optimal Information Filter (RETOIF) to fuse LiDAR-inertial and multiple radar-inertial estimates in a fault-aware decentralized architecture. In real subterranean tunnels without smoke its RMSE is 2.1733 versus 2.9929 for conventional centralized LRIO (27.4% lower), and it maintains pose estimation under smoke-induced degradation.

### [Gaussian Episodic Memory for Long-Term Spatiotemporal Reasoning (GEMS)](https://arxiv.org/abs/2610.33158)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(机器人记忆)
开源状态 / Code: ❓ 未知(Comments 称代码与数据见[项目页](https://abwerby.github.io/GEMS/),页面内容未核实)
- 🇨🇳 现实环境持续发生半静态变化,现有机器人时空记忆要么受限于构建时捕获的实体,要么受限于已观察过的视角。GEMS 把持久的时空 3DGS 地图(只重建一次、仅更新变化区域并只存储修改)与 agentic 推理流水线结合,按需渲染新视角、迭代累积证据来回答时空问题并落地物体。同时提出含 3 个真实、12 个合成环境、473 个问答对的 GEMS-Bench;GEMS 在 3D 物体落地与时空问答上优于近期基线,新视角渲染质量与专门的场景更新方法相当(cs.CV 交叉列表)。
- 🇬🇧 Real environments change semi-statically, while existing robot spatio-temporal memories are limited to entities captured at construction or previously observed viewpoints. GEMS pairs a persistent spatio-temporal 3DGS map (reconstructed once, updated only where the scene changes, storing only modifications) with an agentic reasoning pipeline that renders novel views on demand and accumulates evidence to answer spatiotemporal questions and ground objects. With GEMS-Bench (3 real and 12 synthetic environments, 473 QA pairs), it outperforms recent baselines in 3D object grounding and spatiotemporal QA while matching dedicated scene-update methods in rendering quality (cs.CV cross-list).

### [Does VGGT Know What It Does Not Know?](https://arxiv.org/abs/2610.35806)
开源状态 / Code: ❓ 未知(仅 API 检索命中,不在 cs.RO 列表)
- 🇨🇳 VGGT 等前馈 3D 重建模型一次前向回归相机与几何,却不给出位姿不确定性。该文在含 1,000 对刻意困难图像对的 HardMatch(VGGT 在 35% 的对上失败)上,用冻结特征上的线性探针预测位姿失败,在留出类别上 ROC-AUC 为 93.5%,VGGT 自身点图置信度为 79.7%,用全部输出训练的分类器为 77.7%。探针能捕捉 VGGT 自信的失败、支持下游放弃不可信对,并无需重训迁移到 PhotoTourism 与 ScanNet-1500 的旋转失败;该信息并非来自单图像编码器,而是在融合两视图的层中间形成,第二个模型 π³ 同样如此。
- 🇬🇧 Feed-forward 3D reconstruction models such as VGGT regress cameras and geometry in one pass but report no pose uncertainty. On HardMatch (1,000 hard image pairs where VGGT fails on 35%), a linear probe on frozen features predicts pose failure on held-out categories with ROC-AUC 93.5%, versus 79.7% for VGGT's own point-map confidence and 77.7% for a classifier on all outputs; it catches failures VGGT is confident about, lets downstream systems abstain, and transfers without retraining to rotation failures on PhotoTourism and ScanNet-1500. The knowledge is computed partway through the two-view fusion layers rather than in the per-image encoder, and the same holds for π³.

### [SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://arxiv.org/abs/2610.34745)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(策略学习仿真环境)
开源状态 / Code: ❓ 未知
- 🇨🇳 把视觉捕获变成可交互仿真环境需要物体重建、物理建模与中间错误修正。SceneAgent 是 agentic 流水线,通过基于仿真器的视觉检查与修复协调这些步骤,处理 3DGS、摄影测量、LiDAR、AI 生成的 3DGS 场景与动态场景 4D 视频,结合物体分割、物理参数估计、部件分解、关节化与可变形模拟,并为策略学习生成多样物体变体与脚本化演示。GraspClutter6D 杂乱料箱场景中,每个有可评分输出的编码 agent 的 1 cm F1 都得到提高,最佳 60.75%,SimFoundry 为 6.9%;4DCodeBench 三个动态场景上平均动态 IoU 从 0.86% 提升到 99.09%,并展示初步真机策略迁移。
- 🇬🇧 Turning visual captures into interactive simulation requires object reconstruction, physical modeling and error correction. SceneAgent coordinates these through simulator-based visual inspection and repair, handling 3DGS, photogrammetry, LiDAR, AI-generated 3DGS scenes and 4D videos, combining segmentation, physical-parameter estimation, part decomposition, articulation and deformable simulation, and generating object variants and scripted demonstrations for policy learning. On a GraspClutter6D cluttered bin it improves F1 at 1 cm for every coding agent with scorable outputs (best 60.75% vs 6.9% for SimFoundry) and on three 4DCodeBench dynamic scenes raises mean dynamic IoU from 0.86% to 99.09%, with preliminary real-robot policy transfer.

**其余列名 / Also:** [T-ConSG](https://arxiv.org/abs/2610.34041)(LiDAR 时序施工场景图)、[VPR-Space](https://arxiv.org/abs/2610.35642)(空间类比域视觉位置识别基准)。共 9 条含上列 7 条。

---

## 其他值得关注 / Other Notable

仅列名(共 10 条,不展开):[Multi-Objective RL Using Routed Ensembles](https://arxiv.org/abs/2610.35733)(通用 MORL 理论,NeurIPS 2026)、[IntNet](https://arxiv.org/abs/2610.34466)(自动驾驶 MARL)、[Replicate What Varies / Patchwork](https://arxiv.org/abs/2610.33582)(域随机化仿真资源共享,robosuite+MuJoCo,32 副本 CPU RSS 降 88–92%)、[Execution Logs Sway VLM Judges](https://arxiv.org/abs/2610.34151)、[RoboJev](https://arxiv.org/abs/2610.33718)、[High-resolution tactile observation…racket-control](https://arxiv.org/abs/2610.35563)、[ORBIT 多指手](https://arxiv.org/abs/2610.33241)、[DEX-PHD](https://arxiv.org/abs/2610.35462)、[SPECOLA](https://arxiv.org/abs/2610.35730)、[Quantum Closed Loop IK](https://arxiv.org/abs/2610.33715)。 / 10 items listed by name only.

**分类自查 / Misclassification check:** 已逐条检查类别 3–7:ReSight、RoboReason、POD-RoPE、ARPG、RoboDoctor、TRP、Networked Humanoid(综述)、各 VLA/VLN/世界模型/SLAM 条目均不以运动控制为目标任务或主要贡献;HuGe、ZAP、Zero-HLM、MOTIO、ThinkLocoManip 已移入运动控制·RL。

---

## GitHub 动态 / GitHub Highlights

radar 数据日期 2026-10-28(已更新);`star_baseline_taken_at` = 2026-10-26。

**star 增长(相关仓库)/ Star growth**

| 仓库 / Repo | Stars | Δ | 说明 / Note |
|---|---|---|---|
| [DiaoOrg/awesome-supermimic](https://github.com/DiaoOrg/awesome-supermimic) | 231 | +87 | SuperMimic 第三方资源合集,非官方代码。 / Curated third-party list for SuperMimic, not official code. |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28,526 | +36 | 机器人学习库,今日无 release。 / LeRobot; no release today. |
| [LambdaHumanoid/openlambda](https://github.com/LambdaHumanoid/openlambda) | 87 | +35 | λ_0:面向人形 loco-manipulation 的开放世界第一视角人类数据。 / Egocentric human data for humanoid loco-manipulation. |
| [CumulusAlpha/Dex-Supermimic](https://github.com/CumulusAlpha/Dex-Supermimic) | 47 | +21 | SuperMimic 灵巧手操作的第三方复现。 / Third-party dexterous-hand reproduction. |
| [emoPointer/supermimic_manipulation](https://github.com/emoPointer/supermimic_manipulation) | 20 | +19 | mjlab 上的 SuperMimic 世界模型策略优化(操作),第三方。 / Third-party, in mjlab. |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 15,928 | +19 | 物理仿真器。 / Physics simulator. |
| [RLinf/RLinf](https://github.com/RLinf/RLinf) | 5,527 | +18 | 具身与 agentic AI 的 RL 基础设施。 / RL infra for embodied/agentic AI. |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 14,428 | +16 | π0 系列开源。 / π0-family open source. |

**新仓库(筛选)/ Notable new repos:** [alibaba-damo-academy/RynnUnify](https://github.com/alibaba-damo-academy/RynnUnify)(26 stars,统一具身大脑,对应 HF Daily Papers 论文 2610.32965,窗口外)、[kaibohex/muscle-supermimic](https://github.com/kaibohex/muscle-supermimic)(20 stars,第三方,肌肉驱动人形)、[NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real)(17 stars,Unitree G1 第三方复现)、[H-EmbodVis/RePIC](https://github.com/H-EmbodVis/RePIC)(2 stars,免训练复用去噪轨迹,Fast-WAM 在 RoboTwin 上加速 2.66–2.75 倍)。其余新仓库多为个人作业、爱好硬件或与主题无关,已忽略。

**重点项目 release / Watchlist releases:** 过去 48 小时内无(`watchlist_releases` 为空,LeRobot、openpi、Isaac Lab、MuJoCo、GR00T 等均无新 release)。 / None in the last 48 h.

---

## 今日趋势 / Today's Trends

1. **人形动作跟踪:从单本体走向跨本体与真机在线适应。** [MimicAll](https://arxiv.org/abs/2610.33508) 一个策略覆盖 16 个人形家族,[HumanoidNDM](https://arxiv.org/abs/2610.34126) 用神经动力学模型无动捕地微调真机策略,[AdaDexTrack](https://arxiv.org/abs/2610.33852) 以 RL 调制器给灵巧手跟踪加闭环反馈。 / Humanoid motion tracking is moving from single-body specialists to cross-embodiment and real-world online adaptation: MimicAll, HumanoidNDM and AdaDexTrack.
2. **前沿 LLM/VLM 作为带工具 harness 的机器人 agent。** [ThinkLocoManip](https://arxiv.org/abs/2610.34370)、[MOTIO](https://arxiv.org/abs/2610.33446)、[ZAP](https://arxiv.org/abs/2610.35817)、[EBench 报告](https://arxiv.org/abs/2610.35832)、[VISTA](https://arxiv.org/abs/2610.35051)、[RoboDoctor](https://arxiv.org/abs/2610.35604) 与 [RobotAgentBench](https://arxiv.org/abs/2610.34649) 都围绕 harness 做文章,评测也开始在 GPT-6 Astra 上对比 VLA/WAM。 / Frontier models as tool-harness robot agents, with benchmarks pitting them against VLA/WAM policies.
3. **从人类第一视角视频学潜在动作。** [RynnVLA-Latent](https://arxiv.org/abs/2610.34356)、[EXE](https://arxiv.org/abs/2610.33685)、[HuGe](https://arxiv.org/abs/2610.34186)、[ARPG](https://arxiv.org/abs/2610.34453) 都把人类数据转成可迁移的动作表示,RynnVLA-Latent 在 LIBERO 达 98.8%。 / Latent actions from egocentric human video as the scaling lever.
4. **世界模型/WAM 的评估与加速。** [What Does World Modeling Actually Improve](https://arxiv.org/abs/2610.34593) 发现未来视频预测在已见任务上提升大、在分布偏移下不稳,[OSWAM](https://arxiv.org/abs/2610.35850) 追求一步动作生成,[RoboWorM](https://arxiv.org/abs/2610.33807) 与 [WorldFailBench](https://arxiv.org/abs/2610.33565) 质疑世界模型的物理与失败忠实度。 / World models/WAMs are being audited and accelerated.
5. **SuperMimic 生态在论文发布数日内出现大量第三方复现。** 官方代码未发布时,[awesome-supermimic](https://github.com/DiaoOrg/awesome-supermimic) 一天 +87 star,另有灵巧手、肌肉驱动人形、G1 sim2real 等复现。 / Within days of release, many third-party SuperMimic reproductions appear while official code is still absent.

---

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
- `agentic harness` / `robot agent harness`(arXiv 与 GitHub 皆适用)。中:今日至少 8 篇论文把「harness」作为核心概念,现有关键词覆盖不到。 / EN: at least eight papers center on harnesses. 证据:[ThinkLocoManip](https://arxiv.org/abs/2610.34370)、[VISTA](https://arxiv.org/abs/2610.35051)、[EBench 报告](https://arxiv.org/abs/2610.35832)、[RoboDoctor](https://arxiv.org/abs/2610.35604)、[RobotAgentBench](https://arxiv.org/abs/2610.34649)、[ZAP](https://arxiv.org/abs/2610.35817),HF 另有 RoboHarness(2610.14018)。
- `latent action`(arXiv)。中:多篇 VLA 预训练工作用潜在动作从视频学习。 / EN: recurring VLA pretraining device. 证据:[RynnVLA-Latent](https://arxiv.org/abs/2610.34356)、[EXE](https://arxiv.org/abs/2610.33685)、HuGe 的潜在运动 token。

**建议观察 / Watch**
- `Fast-WAM` / `OpenWAM`(arXiv、GitHub)。中:出现在 POD-RoPE、WAM 消融与 RePIC 仓库,尚属早期信号。 / EN: weak but recurring. 证据:[POD-RoPE](https://arxiv.org/abs/2610.33745)、[What Does World Modeling Actually Improve](https://arxiv.org/abs/2610.34593)、[RePIC](https://github.com/H-EmbodVis/RePIC)。

**建议移除/收窄 / Remove or Narrow**
- GitHub 关键词 `SLAM`:中:今日 new_repos 中大量命中是 BTS SIO "SLAM" 学校作品集等噪声,建议限定 `visual slam`/`lidar slam` 或要求 topic。 / EN: noisy hits from unrelated "SLAM" school portfolios. 证据:emme-mouad/emme-mouad.github.io、emme-mouad/cinema-pathe-macon、esmith443/Better-Wooting-Cyberpunk77-Analog-Controls(同一份 radar new_repos)。

---

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 / Added | 当前状态 / Status | 今日检查 / Today's check | 备注 / Notes |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | 未知 / Unknown(无变化) | radar `signal: true`,唯一候选为 `qiayuanl/claude-meter`(无关的 macOS 菜单栏应用,来源 owner_recent);`project_page_github_links`、`project_page_release_claims`、`arxiv_github_links` 均为空;arXiv 仍为 v1;预设 known_repos 匿名均不可访问;[项目页](https://supermimic.github.io)无代码链接也无发布承诺;errors 为空 | 误报,不触发。第三方复现很多(awesome-supermimic 231 stars,另有 Dex-Supermimic、Sim2Real 复现等),均不算官方开源。 |

**建议加入监测 / Suggested additions**(均为运动控制·RL,代码状态为计划开源或未知)

1. **Zero-HLM** — 项目页明确标注「Code (coming soon)」,人形 loco-manipulation 的真机数据-free 路线。 / Project page says code is coming soon; real-data-free humanoid loco-manipulation.
2. **FLORE** — 项目页标注「Code (coming soon)」,力反应人形全身控制。 / Code coming soon; force-reactive humanoid whole-body control.
3. **HumanoidNDM** — CoRL 2026 接收的首个无动捕在线微调人形跟踪框架,目前无代码链接。 / CoRL 2026 online MoCap-free tracking fine-tuning, no code yet.
4. **MimicAll** — 464 本体基准与跨人形动作跟踪,尚无代码。 / Cross-humanoid tracking with a 464-body benchmark, no code yet.

```json
[
  {"name": "Zero-HLM", "title": "Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data", "arxiv_id": "2610.35075", "search_terms": ["Zero-HLM"], "owners": [], "project_pages": ["https://young-bit.github.io/zero-hlm/"], "known_repos": []},
  {"name": "FLORE", "title": "Learning Force-Reactive Humanoid Loco-Manipulation", "arxiv_id": "2610.35862", "search_terms": ["FLORE", "FLoRe"], "owners": [], "project_pages": ["https://louis-leee.github.io/FLoRe/"], "known_repos": []},
  {"name": "HumanoidNDM", "title": "HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model", "arxiv_id": "2610.34126", "search_terms": ["HumanoidNDM"], "owners": [], "project_pages": [], "known_repos": []},
  {"name": "MimicAll", "title": "MimicAll: Structured Embodiment Conditioning for Cross-Humanoid Whole-Body Motion Tracking", "arxiv_id": "2610.33508", "search_terms": ["MimicAll"], "owners": [], "project_pages": [], "known_repos": []}
]
```

**建议移出 / Suggested removals:** 无(SuperMimic 尚未官方开源)。 / None.
