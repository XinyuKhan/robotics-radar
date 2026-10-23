# 机器人/具身智能每日速递 — 2026-10-23 / Robotics & Embodied AI Daily — 2026-10-23

> 本日无监测项开源:SuperMimic 仍无官方代码(radar `signal=false`,项目页无仓库/承诺)。详见文末「开源监测」。
> No watchlist item released today: SuperMimic still has no official code (radar `signal=false`; project page has no repo link or promise). See OSS Watchlist at the end.

## 检查窗口与来源状态 / Window & Source Status

- 窗口 / Window:2026-10-22 ~11:00 → 2026-10-23 ~11:00(台北时间 UTC+8;今天周五,无周末覆盖问题)。arXiv cs.RO 周五列表覆盖周三晚至周四提交,故少数条目提交于 10-21。 / Taipei time; the Friday cs.RO list spans Wed-evening to Thu submissions, so a few items are dated 10-21.
- arXiv cs.RO `/new`:63 New + 6 Cross + 38 Replacements = 107 条;已逐条分类。 / 107 entries, all classified.
- arXiv API 关键词检索(cs.RO/cs.AI/cs.LG/cs.CV,submittedDate 10-22 03:00 → 10-23 04:00 UTC)命中数 / hits: embodied 10, VLA 11, vision-language-action 10, VLN 1, vision-language navigation 0, humanoid 4, legged locomotion 0, whole-body control 0, MPC 0, reinforcement learning robot 0, sim-to-real 1, dexterous manipulation 2, robot foundation model 1, world model 11, world action model 3, WAM 2, video world model 2, spatial intelligence 0, spatial reasoning 2, SLAM 2, visual SLAM 1, LiDAR SLAM 0, gaussian splatting SLAM 0, 3D reconstruction 2, motion tracking 3, motion imitation 0(去重后 43 篇,另外补出 cs.CV/cs.AI 中 11 篇 cs.RO 列表之外的相关条目)。注:API 为短语匹配(`all:"…"`),"reinforcement learning robot / whole-body control" 等多词短语命中为 0 属正常,控制类工作主要靠 cs.RO 列表发现。 / Phrase matching, so multi-word control phrases return 0; control work was found via the cs.RO list.
- 入选并展开/列名 / selected:展开 33 篇 + 列名若干;**全部 61+4+11 篇候选均已通过 arXiv API id_list 取得非空完整摘要与 Comments(0 失败)**。 / All fetched candidates have non-empty full abstracts.
- radar:`date_taipei = 2026-10-23`(已更新);new_repos 291、tracked 1686、star 增长 290、release 2、oss_signals 0。star 基准时间 2026-10-22 08:41 UTC。
- Hugging Face Daily Papers:已读取(100 条),与主题相关且带 githubRepo 的见各条目。
- 局限 / Limits:radar 的 release `body` 在 JSON 中被截断为 1500 字符(MuJoCo、Genesis),下文仅据可见部分;本会话 GitHub 权限仅限本仓库,无法读取 mujoco 完整 release。cs.RO Replacements 仅核对了与主题相关者的更新日期与 Comments,未对比版本差异,故不作展开。

## 今日必读 / Top Picks

1. **DONIC**(运动控制·RL,✅ 已开源)— 首个通用双手灵巧参考跟踪器,PPO+BC 反馈回路,单一 checkpoint 在未见轨迹上 86.79%、未见物体 57.32%。 / First generalist bimanual dexterous tracker; one checkpoint reaches 86.79% on unseen trajectories and 57.32% on held-out objects.
2. **Humanoid Mobility via Attention-based Contacts**(运动控制·RL,❓)— 以"接触"为接口,把动作数据仅作训练先验的人形复杂地形 locomotion。 / Contact as the interface between perception and control; motion data used only as a training prior for humanoid terrain mobility.
3. **DiffDreamer**(运动控制·RL,❓)— 学习式世界模型 + 可微仿真联合优化 actor,用于敏捷四旋翼竞速。 / Couples a learned world model with differentiable simulation for agile quadrotor control.
4. **λ₀ (HumanVerse)**(运动控制·RL,✅)— 500 小时第一视角人类全身操作数据 + 人形 loco-manipulation 基础模型,SIMPLE 90.0%。 / 500-hour egocentric human loco-manipulation data and a humanoid foundation model; 90.0% on SIMPLE.
5. **UniFlowWAM**(世界模型与 WAM,❓)— 把 3D 场景流作为与视觉、动作并列的第三模态,真机 87.0% vs 68.5%。 / 3D scene flow as a third modality in a WAM; 87.0% real-robot success vs 68.5%.

---

## 运动控制·RL / Motion Control · RL(共 11 条,全部展开 / all 11 expanded)

### [DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations](https://arxiv.org/abs/2610.29997) — Ropedia 等(HF 上 132 upvotes;提交于 10-21 16:36 UTC,略早于窗口,因 HF 热度收录)
🏷️ 交叉方向 / Also: 灵巧操作 / dexterous manipulation(归入控制,因主要贡献为跟踪控制策略)
开源状态 / Code: ✅ 已开源 / Released — [github.com/Ropedia/DONIC](https://github.com/Ropedia/DONIC)(HF githubRepo;仓库存在,具体含训练代码还是仅推理未核对)
- 🇨🇳 现有灵巧参考跟踪多针对单手与有限交互,双手灵巧行为缺少接触丰富的数据且协调接触复杂。作者提出 DONIC,首个跨操作类别与人体运动来源联合训练的通用双手跟踪器,并构建 BiHOI 数据集(1,575 条序列、229 个物体,重构后重定向为机器人参考)。方法把 PPO 与行为克隆放入反馈回路,将验证成功的执行回收为训练示范;配合以物体为中心的逐手奖励与 Clip-Centered Advantages(去除与参考相关的优势偏置)。无需微调,单个 checkpoint 在已见物体的未见轨迹上成功率 86.79%、留出物体上 57.32%,分别超过最优双手跟踪基线 77.36 和 45.73 个百分点。
- 🇬🇧 Prior dexterous tracking mostly handles single hands and limited interactions, and bimanual contact-rich data is scarce. DONIC is the first generalist bimanual tracker trained jointly across operation categories and motion sources, alongside BiHOI (1,575 sequences, 229 objects, retargeted to robot references). It combines PPO with behavioral cloning in a loop that recycles verified successes as demonstrations, with an object-centered per-hand reward and Clip-Centered Advantages. Without finetuning one checkpoint achieves 86.79% on unseen trajectories and 57.32% on held-out objects, beating bimanual tracking baselines by 77.36 and 45.73 points.

### [Humanoid Mobility via Attention-based Contacts](https://arxiv.org/abs/2610.31608) — Junzhe He, Kehan Wen, Chong Zhang, Clemens Schwarke 等(机构摘要未给出)
开源状态 / Code: ❓ 未知 / Unknown(Comments 仅 "under review")
- 🇨🇳 无参考的 RL 在地形上泛化好但难以靠奖励设计得到协调全身动作;基于参考的方法动作自然却难以适应轨迹之外。本文用动作数据"仅作训练先验":自监督、基于注意力的接触规划器预测未来身体—环境接触,接触条件跟踪器把接触计划转成全身动作,使接触成为感知与控制之间的接口;随后微调阶段探索原始数据未覆盖的环境变化。部署时仅依赖机载观测、不需任何参考输入。预印本摘要未给出定量结果。
- 🇬🇧 RL without references generalizes across terrain but struggles to elicit whole-body coordination, while reference-based methods look natural but cannot adapt beyond their data. The paper uses motion data strictly as a prior: a self-supervised attention-based contact planner predicts future body-environment contacts and a contact-conditioned tracker turns them into whole-body motion, with a later fine-tuning stage exploring variations beyond the data. At deployment it uses only onboard observations with no reference input. The abstract reports no quantitative results.

### [DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control](https://arxiv.org/abs/2610.31617) — Fanxing Li 等
🏷️ 交叉方向 / Also: 世界模型 / World Model(归入控制:任务为四旋翼敏捷控制策略学习)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 基于世界模型的 RL 常把环境演化与机器人自身动力学混在同一个学习式 rollout 里,模型偏差会拖累策略优化。DiffDreamer 在一步优化中让学习式世界模型传播捕捉外部动态与历史特征的隐状态,可微仿真器传播机器人显式物理状态;并把 actor 目标拆成"critic 驱动(不可微任务奖励)"与"仿真器驱动(可微运动奖励)"两条路径。在激进跟踪与动态门竞速上,收敛速度优于无模型、基于模型和可微 RL 基线,最终性能还优于经典规划与控制方法,并给出概念验证级真机飞行。具体数值摘要未给出。
- 🇬🇧 World-model RL often entangles environment evolution and the robot's own dynamics in one learned rollout, so model bias hurts policy optimization. DiffDreamer propagates latent states for external dynamics with a learned world model and the robot's physical state with a differentiable simulator in the same step, and splits the actor objective into a critic pathway (non-differentiable rewards) and a simulator pathway (differentiable motion rewards). On aggressive tracking and dynamic-gate racing it converges faster than model-free, model-based and differentiable-RL baselines and beats classical planning/control, with proof-of-concept real flights. Exact numbers are not in the abstract.

### [λ₀: Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.18950) — Lambda-humanoid Team(v2 更新于 10-21;Comments:Tech report, 24 pages)
🏷️ 交叉方向 / Also: 具身基础模型 / Embodied foundation model;数据集 / dataset(含控制与模型贡献,归入控制)
开源状态 / Code: ✅ 已开源 / Released — [github.com/LambdaHumanoid/openlambda](https://github.com/LambdaHumanoid/openlambda)(HF githubRepo;仓库存在,开源范围未核对);主页 [lambdahumanoid.github.io](https://lambdahumanoid.github.io/)
- 🇨🇳 人形 loco-manipulation 的机器人示范采集昂贵,而现有第一视角人类数据常缺少行走与姿态,且存在本体差异与控制器动力学问题。作者发布 HumanVerse(500 小时开放世界人类 loco-manipulation,第一视角视频与同步身体/手部动作配对),人到人形管线对齐相机视角与手臂外观,并离线细化运动参考与控制器输入以降低末端误差。以此为基础训练人形全身 loco-manipulation 基础模型 λ₀,用机器人对齐的人类示范做中期训练监督;在 Unitree G1 上零目标任务机器人示范迁移。λ₀ 在 SIMPLE 上成功率 90.0%,真实世界 loco-manipulation 任务 62.5%,且增加全身人类数据持续提升任务进度。
- 🇬🇧 Robot demonstrations for humanoid loco-manipulation are costly, and egocentric human data often omits locomotion and posture. The authors release HumanVerse (500 hours of open-world human loco-manipulation with egocentric video and synchronized body/hand motion) and a human-to-humanoid pipeline that aligns viewpoints and refines motion references and controller inputs offline. They train λ₀, a humanoid whole-body foundation model, using robot-aligned human demonstrations for mid-training, with zero-shot transfer to Unitree G1. λ₀ reaches 90.0% on SIMPLE and 62.5% across real-world loco-manipulation tasks, and more whole-body human data consistently helps.

### [Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.30540) — Xiongbo Shi 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 对物体交互任务,重定向必须在关键阶段保持身体—物体关系,但逐帧均匀的迭代预算无视局部精度需求,效率低。提出 STR:视觉语言模型挑选相关运动信号与身体部位,据此识别关键帧,为关键帧分配更多求解迭代、为选定部位赋更高交互权重;再用 Mechanics-Aware Contact Anchoring(基于近似物体 wrench 模型)优化接触位置;并提出 STRL,以自适应关键阶段采样和基于目标邻近度与接触力的接触奖励做下游控制 RL。在 Unitree G1 仿真与 Unitree R1 真机上,STR 以更低计算成本提升几何接触覆盖和连续性,生成的参考提升了多种物体交互动作的下游任务完成度(摘要未给出具体数字)。
- 🇬🇧 Retargeting for object interaction must preserve body–object relations at critical stages, but uniform per-frame solver budgets ignore this. STR uses a VLM to pick relevant signals and body parts, identifies keyframes, and allocates extra solver iterations and higher interaction weights there, plus Mechanics-Aware Contact Anchoring using an approximate object-wrench model; STRL then adds adaptive key-stage sampling and a contact reward (target proximity and contact force) for downstream RL control. On Unitree G1 in simulation and Unitree R1 in the real world, STR improves contact coverage and continuity at lower compute and the references raise downstream task completion. No numeric values are given in the abstract.

### [Robot Motion Transition with Human Motion Prior (STAMP)](https://arxiv.org/abs/2610.30817) — Taehyun Byun 等(Comments:9 pages, 4 figures)
开源状态 / Code: ❓ 未知 / Unknown — 项目页 [childtoy.github.io/STAMP-project](https://childtoy.github.io/STAMP-project)(摘要给出,未核对是否含代码)
- 🇨🇳 人形动作跟踪策略能复现多样行为,但把独立获得的动作连成连续序列仍困难:插值不考虑相对位置、朝向和时序是否合适,生成式先验又可能在边界安排不当时产生多余行走或转身。STAMP 通过"机器人→人→机器人"流程:把两段动作重定向到人体骨架,学习的对齐模型对下一段动作的候选位置、朝向、过渡时长排序,人类运动先验在选定对齐下生成过渡,再重定向回机器人并用作训练跟踪策略的参考。在 Unitree G1 与 ROBOTIS K1 上评估过渡的跟踪成功率,并有真机演示把独立动作连成长程序列(摘要未给出具体成功率)。
- 🇬🇧 Humanoid tracking policies reproduce diverse behaviors, but chaining independent motions is hard: interpolation ignores alignment, and generative priors may add unintended locomotion. STAMP retargets both motions to a human rig, where a learned alignment model ranks candidate positions, headings and durations, a human motion prior generates the transition, and the result is retargeted and used to train a tracking policy. It is evaluated on Unitree G1 and ROBOTIS K1 with real-robot demos of long-horizon sequences; the abstract gives no success-rate numbers.

### [Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation (ALMA)](https://arxiv.org/abs/2610.30810) — Jingyu Ru 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 空中机械臂的机械臂运动与交互会持续改变质心、惯量并带来力/力矩扰动,传统控制依赖显式模型与估计,学习式控制的奖励又无法直接约束历史响应信息,固定任务采样也会遗漏困难情形。ALMA 使用基于近期测量与动作自适应的上下文飞行策略,以动作条件的未来测量表征预测来训练上下文;并用进化过程让 LLM 分析观察到的控制困难、提出新的机械臂运动结构用于后续训练。仿真中位置 RMSE 比最强基线最多降低 24.7%,同一策略零样本迁移到真实空中机械臂,在周期性机械臂运动下悬停位置 RMSE 比真实基线降低 79.6%。
- 🇬🇧 Arm motion on an aerial manipulator keeps shifting mass, inertia and disturbances, so explicit-model controllers struggle and fixed task sampling leaves hard cases unexplored. ALMA uses a contextual flight policy adapting from recent measurements and actions, trained with action-conditioned prediction of future measurement representations, plus an evolutionary loop where an LLM analyzes control difficulties and proposes new arm-motion structures. In simulation it cuts position RMSE by up to 24.7% versus the strongest baseline, and the policy transfers zero-shot to a real aerial manipulator, reducing hover position RMSE by 79.6% under periodic arm motion.

### [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation (WholeBodyMem)](https://arxiv.org/abs/2610.31166) — Chenyuan Chen, Yoshihiko Nakamura 等(Comments:RA-L 投稿)
🏷️ 交叉方向 / Also: VLA(全身 VLA 策略;按规则默认归入运动控制)
开源状态 / Code: ❓ 未知 / Unknown — 仅项目页 [memory-before-goal.github.io](https://memory-before-goal.github.io)
- 🇨🇳 动态场景中的人形 loco-manipulation 是非马尔可夫的:线索可能消失、被遮挡或随机器人转身离开视野,而全身 VLA 策略只看当前帧。WholeBodyMem 是以物体为引导的感知记忆:SAM3 跟踪任务物体,物体事件在自适应预算内因果地选出关键帧,动作专家通过交叉注意力读取这些帧及编码外观、几何、时间的物体 token;同时贡献 HuMeGo 基准(6 个仿真 + 6 个真实 Unitree G1 任务)。基础策略成功率在仿真中由 29.1% 升至 72.6%,真机由 36.7% 升至 88.3%,标准 SIMPLE 任务由 70.2% 升至 86.9%。
- 🇬🇧 Humanoid loco-manipulation in dynamic scenes is non-Markovian, yet whole-body VLA policies see only the present. WholeBodyMem keeps an object-guided perceptual memory: SAM3 tracks task objects, object events causally select key frames under an adaptive budget, and the action expert reads them via cross-attention with object tokens; the HuMeGo benchmark adds six simulated and six real Unitree G1 tasks. It raises the base policy from 29.1% to 72.6% in simulation and from 36.7% to 88.3% on the real robot, and from 70.2% to 86.9% on SIMPLE.

### [LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.30876) — Dewei Wang 等
🏷️ 交叉方向 / Also: 基准 / Benchmark(非控制算法贡献的基准/测试台,但覆盖人形控制器评测,按规则默认留在控制类)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 人形 loco-manipulation 的进展难以跨策略、控制器与任务比较。LocoManiLab 提供覆盖数据采集/生成、策略训练、评测与物理部署的测试台:234 个原子与组合任务、五类家庭场景、51.5 小时仿真遥操作;评测 12 个策略(共享控制器)、2 个策略 × 5 个控制器,并研究示范规模与数据源混合。结果显示成功率在未见任务/场景上下降,并随视觉扰动增大而下降;3 个仿真任务与真实设置对应,仿真与真机上的策略排名相近,支持仿真评测的可靠性。
- 🇬🇧 Progress in humanoid loco-manipulation is hard to compare across policies, controllers and tasks. LocoManiLab is a testbed spanning data collection/generation, training, evaluation and deployment, with 234 atomic and compositional tasks over five household scene categories and 51.5 hours of simulated teleoperation. It evaluates twelve policies with a shared controller and two policies across five controllers; success drops on unseen tasks/scenes and under visual perturbation, and policy rankings agree between three matched sim/real tasks, supporting simulation-based evaluation.

### [PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning](https://arxiv.org/abs/2610.31299) — Niklas Berndt, Gerard Pons-Moll 等(cs.CV)
开源状态 / Code: 🕒 计划开源 / Planned — 摘要:"We will release the processed data and model checkpoints";项目页 [virtualhumans.mpi-inf.mpg.de/PiHand](https://virtualhumans.mpi-inf.mpg.de/PiHand/)(未见代码仓库)
- 🇨🇳 灵巧手物体交互需同时满足接触动力学、物体几何与目标轨迹;现有方法或跟踪 mocap 但难迁移到新物体,或使用仅手的生成先验而丢失接触保真。PiHand 先训练跟踪 mocap 的仿真专家策略,用目标条件 VAE 蒸馏成统一的手—物交互先验,再在其潜空间内做有界残差探索来解决任务,只需单一奖励、无复杂课程。在 GRAB 和 DexYCB 上得到可泛化到未见物体和轨迹的桌面操作策略,并迁移到物体接球和双手递交接,所有任务指标均优于基线(摘要未给出具体数值)。
- 🇬🇧 Dexterous hand-object synthesis must respect contact dynamics, geometry and target trajectories; mocap tracking transfers poorly and hand-only priors lose contact fidelity. PiHand trains simulated expert tracking policies, distills them into a goal-conditioned VAE hand-object prior, and solves tasks via bounded residual exploration in the latent space with one reward and no curriculum. It yields tabletop policies that generalize to unseen objects/trajectories on GRAB and DexYCB and transfer to catching and bimanual handover, consistently outperforming baselines; specific numbers are not in the abstract.

### [MPBRS: Multi-Potential-Based Reward Shaping for Unified Reward Configuration in Humanoid Locomotion](https://arxiv.org/abs/2610.30334) — Van Chung Nguyen, Hung Manh La
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 人形 locomotion 的 RL 奖励设计与调参困难:朴素塑形项可能与期望行为冲突、过拟合特定机器人或对权重敏感。本文研究 Multi-PBRS(基于势函数差分的塑形,不改变最优策略),提出统一奖励配置,并用同一奖励结构和权重在九种人形机器人上评测,仅需机器人特定元数据(关节/连杆映射和默认姿态)。相比标准塑形,MPBRS 的缩放行为更一致、调参敏感度更低;摘要未给出具体数值。
- 🇬🇧 Reward design and tuning is a core difficulty for humanoid locomotion RL; naive shaping terms can conflict with desired behavior, overfit a robot, or be weight-sensitive. The paper studies Multi-PBRS (potential-difference shaping that preserves the optimal policy) and proposes a unified reward configuration evaluated with identical structure and weights on nine humanoids, needing only robot metadata (joint/link mappings, default poses). Versus standard shaping it gives more consistent scaling and less tuning sensitivity; no numbers are in the abstract.

### [TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion](https://arxiv.org/abs/2610.21515) — Zejian Kang 等(v 更新于 10-22)
🏷️ 交叉方向 / Also: 动作生成(扩散)/ motion generation(贡献为 G1 机器人动作的生成与编辑,与控制紧密相关,按规则留在控制类)
开源状态 / Code: ✅ 已开源 / Released — [github.com/Multimodal-Perception-Action/TRACE](https://github.com/Multimodal-Perception-Action/TRACE)(摘要给出,仓库存在)
- 🇨🇳 语言条件的人形动作生成难以把含糊请求对应到可修改的具体动作结构。TRACE 面向 Unitree G1,围绕类型化、可度量的运动学量:语言模型从动作监督中预测支撑、根、手部事件,其时间对齐编码与文本一起条件化扩散生成器,并用重力参照状态与轨迹—接触目标提升运动学一致性;编辑端用类型化请求定义身体—时间范围和相对源动作的目标,由参考条件扩散编辑器实现修改,并在采样时投影以保护不应变动的状态坐标。定量与人工评估显示语义对齐和动作质量优于对比方法,多轮编辑更可靠(摘要未给出数值)。
- 🇬🇧 Language-conditioned humanoid motion generation struggles to map underspecified requests to editable motion structure. TRACE, for Unitree G1, predicts support/root/hand events with a language model, feeds their time-aligned encodings to a diffusion generator with gravity-referenced states and trajectory–contact objectives, and edits via typed body–time scopes and source-relative goals with a reference-conditioned diffusion editor and sampling-time projection. Quantitative and human evaluations show better semantic alignment and motion quality and more reliable multi-turn editing; the abstract gives no numbers.

---

## 运动控制·传统 / Motion Control · Classical(共 7 条,全部展开 / all 7 expanded)

### [Real-Time Disturbance-Aware Koopman Model Predictive Control for Quadrotors in Spatially Varying Winds](https://arxiv.org/abs/2610.27414) — Stella Kombo 等(v 更新于 10-21)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 扰动环境下的四旋翼飞行需要预测模型随未建模气动效应变化而保持准确。提出 DA-KCF:保留离线辨识的名义 Koopman 模型,仅在线学习扰动引起的修正;参考相关的 KCF 先由仿真数据学习并用有限硬件数据校准,部署时名义模型固定,轻量残差集成从因果的状态—指令—状态转移学习低维扰动修正,并沿预测时域纳入 MPC,优化发给机载稳定控制器的位置/偏航参考。纳米四旋翼在均匀风和空间变化尾流下的硬件实验表明,模型失配增大时在线适应能改善多步预测与轨迹跟踪,并满足实时要求(摘要未给出数值)。
- 🇬🇧 Quadrotor flight in disturbed air needs predictive models that stay accurate as aerodynamics change. DA-KCF keeps an offline-identified nominal Koopman model fixed and learns only a disturbance correction online with a lightweight residual ensemble from causal state-command-state transitions, evaluated along the MPC horizon to optimize position/yaw references for the onboard stabilizer. Nano-quadrotor hardware experiments under uniform wind and a spatially varying wake show online adaptation improves multi-step prediction and tracking as mismatch grows while meeting real-time limits; no numbers are given.

### [PhysibleMDM: Enforcing Inference-Time Physical Feasibility Constraints on Motion Diffusion Models via Noise Optimization](https://arxiv.org/abs/2610.30500) — Maximilian Stölzle, Agon Serifi, Ruben Grandia, Espen Knoop 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 运动扩散模型生成的轨迹常违反物理约束,限制其用于仿真与控制。PhysibleMDM 不重训模型,在推理时优化扩散噪声:代理可行性约束结合运动学检查(穿地、滑动、自碰撞)与通过锥规划(cone program)内环计算的逆动力学可行性,以 Sep-CMA-ES 求解黑盒噪声优化,并用自回归方式拼接长序列。在 SMPL 人形 100 种风格上,平均穿地、自碰撞穿透和滑动分别降低 75%、92%、74%;在自定义双足机器人 11 条序列上,加速度重建误差中位数降低 89.5%,逆动力学残差平均降低 79.5%。
- 🇬🇧 Motion diffusion outputs often violate physics, limiting use in simulation and control. PhysibleMDM optimizes the diffusion noise at inference without retraining, using surrogate constraints (ground penetration, slip, self-collision plus an inverse-dynamics cone-program inner loop) solved with Sep-CMA-ES and chained autoregressively. On an SMPL humanoid across 100 styles it cuts mean ground penetration, self-collision penetration and slip by 75%, 92% and 74%; on 11 sequences for a custom biped it reduces median acceleration-reconstruction error by 89.5% and inverse-dynamics residual by 79.5%.

### [ProTrav: Probabilistic Traversability with Elevation Uncertainty Propagation for Risk-aware Off-road Navigation](https://arxiv.org/abs/2610.30839) — Chuanlin Zuo, Miloš Prágr, Arun Kumar Singh 等
开源状态 / Code: ❓ 未知 / Unknown(Comments:9 pages, 7 figures)
- 🇨🇳 现有可通行性估计基于确定性高程,忽略地形空间相关性及高程不确定性在非线性映射中的传播。ProTrav 用稀疏变分高斯过程重建概率高程场,通过后验函数空间采样得到空间相关的地形实现,把高程不确定性传播为可通行成本分布,并以矩基 UCB 风险项接入 MPPI 控制器。仿真中不同地形的导航成功率超过 90%(基线低于 40%)且姿态变化更小,并在真实越野地形上验证。
- 🇬🇧 Deterministic-elevation traversability ignores spatial correlation and uncertainty propagation. ProTrav reconstructs a probabilistic elevation field with a sparse variational GP, samples spatially correlated terrain realizations to propagate elevation uncertainty into a traversability-cost distribution, and feeds a UCB risk term into an MPPI controller. Simulation success exceeds 90% across terrains versus below 40% for a baseline with smaller attitude variation, validated on a real robot off-road.

### [TRACE: Traversability-aware Reactive Navigation via VLM-driven Adaptive Constraints Estimation](https://arxiv.org/abs/2610.30994) — Mario A. V. Saucedo 等(IFAC 2026)
🏷️ 交叉方向 / Also: VLN/导航 / navigation(VLM 可通行性;主体为 NMPC 约束控制,归入传统控制)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 针对森林等非结构化环境的地面机器人自主运行。TRACE 用 VLM 对正/负自然语言提示集生成置信图,经证据融合得到偏重已行驶路径迹象的稠密可通行性图;提取标注点后用百分位分箱加样条/正则多项式拟合出可通行路径左右边界,并作为软障碍约束放入 NMPC,实现安全自适应路径跟随。在真实森林环境的试验中,在杂乱、可形变、视觉歧义地形中实现平滑导航(摘要未给出定量指标)。
- 🇬🇧 For ground robots in unstructured forests, TRACE builds VLM confidence maps from positive/negative language prompts, fuses them by evidence fusion into a dense traversability map favoring traversed-path cues, fits left/right path boundaries via percentile binning and spline/polynomial fitting, and injects them as soft barrier constraints in an NMPC. Real forest trials show smooth navigation in cluttered, deformable, visually ambiguous terrain; no quantitative metrics are in the abstract.

### [Continuous-Time Motion Planning and Steering with Global Convergence (GlobMP)](https://arxiv.org/abs/2610.30607) — Mohsen Amiri, Davoud Ataee Tarzanagh 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 运动规划越来越多地用于修正学习式规划器/策略的动作,约束需在任意时刻成立,但尚无算法在平滑代价加此类约束下可证明收敛到全局最优。作者把规划与"转向"(steering)统一为一个连续时间程序,提出 GlobMP:在分段多项式曲线上做梯度投影,每个约束成为每段上必须非负的多项式,交替降低代价与恢复可行性;理论上从细网格初值出发,随段数增加代价趋近全局最优且约束满足到任意容差。实验涵盖多达 200 个机器人、Robotarium 多机规划、迷宫导航,以及对双臂人形上触觉反应策略的转向,表现优于强基线(摘要未给出具体数值)。
- 🇬🇧 Planning is increasingly used to correct learned planners and policies, with constraints needing to hold at every instant, yet no algorithm provably reaches a global optimum with smoothness cost plus such constraints. GlobMP casts planning and steering as one continuous-time program and applies gradient projection over piecewise-polynomial curves (each constraint a nonnegative polynomial per piece), alternating cost reduction and feasibility restoration, with a proof of approach to the global optimum as pieces grow. Experiments include up to 200 robots, Robotarium multi-robot planning, maze navigation and steering tactile-reactive policies on a bimanual humanoid, outperforming strong baselines; no numbers in the abstract.

### [Dispersive Tree Agreements for Multi-Robot Coordination (WarpWeaver)](https://arxiv.org/abs/2610.31540) — Shashank A. Deshpande 等(Comments:Submitted to T-RO)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 多机协调本质是带约束的联合空间最优控制,但现有方法多为集中式离线且限于无碰撞规划。本文把单机"分散树"(针对微分平坦系统的前向传播指令搜索)框架扩展到多机:证明机间耦合可由局部约束替代,并通过去中心化列生成在共享空间上协商"租金"以引导各机搜索树,收敛到可证明近最优的协议;WarpWeaver 将其实现为滚动时域异步实时环路。仿真中在 Dynobench 上总行程时间比集中式离线规划器最多降低 22%,比去中心化实时基线最多降低 37%,在图连通性任务上把专用规划器成功率几乎翻倍;六机硬件实验验证机载规划。
- 🇬🇧 Multi-robot coordination is joint-space optimal control, but existing methods are centralized/offline or decentralized without pursuing joint optimality. The paper extends single-robot dispersive-tree search for differentially flat systems, showing coupling can be replaced by local constraints and negotiating "rents" via decentralized column generation to reach certified near-optimal agreements; WarpWeaver runs this asynchronously over a receding horizon. In simulation it cuts total travel time by up to 22% versus centralized offline planners on Dynobench and 37% versus a decentralized real-time baseline, nearly doubling a task-specific planner's success on graph connectivity, with six-robot hardware experiments.

### [Whole-Body Motion Guided Reference Generation for Uncertainty-Aware Compliant Assistance](https://arxiv.org/abs/2610.31302) — Muyuan Ma, Long Cheng 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 外骨骼辅助难以适应人体运动与交互需求的多样性。提出双环辅助策略:外环通过去噪生成多模态外骨骼轨迹(以全身人体运动与外骨骼本体感觉为主、任务描述为辅,三阶段训练以缓解跨模态表示不匹配),内环从生成器采样多条未来轨迹得到均值(控制参考)与方差(不确定性),方差进入刚度调节律,实现在有界集总交互输入下输入—状态稳定的柔顺辅助。实验表明相对标准基线显著降低肌肉激活水平,并相对无辅助降低使用者代谢能耗(摘要未给出具体数值)。
- 🇬🇧 Exoskeleton assistance must adapt to varied human motion. A dual-loop strategy couples a denoising trajectory generator (whole-body human motion and exoskeleton proprioception, task text as auxiliary cue, three-stage training) with variable admittance control: sampled trajectories yield a mean reference and a variance used in a stiffness-regulation law with input-to-state stability under bounded interaction. Experiments show significantly lower muscle activation than standard baselines and lower metabolic expenditure than unassisted walking; the abstract gives no numbers.

*另见 / See also(已展开于上,不重复):无。其余传统控制相关弱相关条目(仅列名,共 4 / 4 name-only):[Tilt-Rotor Quadcopter with Learned Residual Control and Mode-Dependent State Estimation](https://arxiv.org/abs/2610.31051)(仿真;PD+EKF+BC 残差,风下定点误差约 -49% / sim; PD+EKF+BC residual, ~49% lower station-keeping error under wind)、[Extending Harmonic Function Methods via Root Locus for Coordinated Path Generation](https://arxiv.org/abs/2610.31625)、[Demonstration-Based Robotic Feeding Using Dynamic Movement Primitives](https://arxiv.org/abs/2610.31020)、[Probabilistic Energy Modeling Unifies Versatile Swarm Control](https://arxiv.org/abs/2610.31371)(空中集群 RL 控制 / aerial swarm control)。*

*Replacements 中的控制类更新(仅列名,未核对版本差异 / name-only, version diffs not checked):[HEX](https://arxiv.org/abs/2604.07993)、[ReactiveBFM](https://arxiv.org/abs/2606.30362)(CoRL 2026)、[CENIC](https://arxiv.org/abs/2511.08771)、[Dual-Arm Box Manipulation](https://arxiv.org/abs/2605.22021)、[Learning Cooperative Bimanual Dexterous Grasp](https://arxiv.org/abs/2608.10383)(IROS 2026)、[Prior Evolution and Task Alignment for Aerial Grasping](https://arxiv.org/abs/2609.18153)、[Beyond Imitation: RL-Based Sim-Real Co-Training for VLA](https://arxiv.org/abs/2602.12628)、[Principles of Robot Autonomy](https://arxiv.org/abs/2608.03496)。*

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models(共 9 条,展开 5 / 9 total, 5 expanded)

### [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://arxiv.org/abs/2610.31670) — Yunfei Xie, Chen Wei 等(cs.CV 交叉)
🏷️ 交叉方向 / Also: VLA、世界模型 / VLA, WAM
开源状态 / Code: ✅ 已开源 / Released — Comments 称 "Project page and code available at [yunfeixie233.github.io/s2](https://yunfeixie233.github.io/s2/)"(仅核对到项目页链接,未核对仓库)
- 🇨🇳 机器人基础模型通常需昂贵的闭环 rollout 评估,需要廉价的离线代理。作者把柏拉图表征假说延伸到运动轨迹,提出免训练的离线指标 Sensorimotor Alignment(S²),衡量模型感知表征与物理运动几何的对齐程度。S² 与跨具身模型家族的下游机器人任务成功率正相关,可在闭环评测前排序模型,也能在昂贵的 VLA 微调前筛选有前景的 VLM 主干,并为 VLA 与 WAM 中观察到的现象提供表征层面的解释(摘要未给出具体相关系数)。
- 🇬🇧 Robot foundation models need costly closed-loop rollouts, so cheap offline proxies are wanted. The paper extends the Platonic Representation Hypothesis to motion and proposes S², a training-free metric of how well a model's sensory representation aligns with physical motion geometry. S² correlates positively with downstream task success across embodied model families, can pre-screen VLM backbones before VLA fine-tuning, and offers representation-level explanations for VLA and WAM phenomena; correlation values are not in the abstract.

### [Learning Robot Behavior Priors from Non-Robotic Synthetic Data](https://arxiv.org/abs/2610.31275) — Mateusz Odrowaz-Sypniewski, Michael Amir 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 真实机器人数据常被视为瓶颈,作者检验无本体系统的廉价程序化合成数据能否在见到真实机器人行为前提供有用先验。设计三条对机器人控制数学抽象建模的数据生成管线,用它们预训练 Transformer 做机器人动作预测。仅用该非机器人数据训练的模型通过上下文学习在未见物理机器人任务上达到非平凡的零样本预测,专门的控制先验明显优于通用因果先验;与计算量匹配的真实机器人数据基线相比,后者仅在其训练过的数据集上更好。
- 🇬🇧 Real robot data is treated as the bottleneck, so the paper tests whether procedurally generated non-robotic data gives useful priors. Three pipelines modeling mathematical abstractions of control pretrain a Transformer for action prediction. A model trained purely on this data attains non-trivial zero-shot prediction on unseen physical robot tasks via in-context learning, specialized control priors beat generic causal priors, and a compute-matched real-data baseline wins only on its own training datasets.

### [Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents (CARE)](https://arxiv.org/abs/2610.30587) — Wei Zhang, Lirong Xiang, Charles Fleming
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 云端强模型使平台在动作间空闲数秒,本地轻量模型快但易错;现有层级架构角色固定,路由器则是无状态逐请求决策。CARE 用轻量 critic 监控执行可靠性,在本地执行变得不可靠时将控制升级到云端模型,且控制权持续到恢复为止以避免逐步切换,并以共享交接记忆保存执行上下文与任务进度。在多个具身基准上,任务成功率比最强协作基线高 6.3–18.3 个百分点,接近或超过纯云端成功率,同时中位动作间延迟降低 28.8–82.6%。
- 🇬🇧 Cloud models leave the platform idle between actions while local models are fast but error-prone; existing hierarchies fix roles and routers are stateless. CARE uses a lightweight critic to escalate control from a local executor to a cloud model when execution turns unreliable, keeps control until recovery, and shares handoff memory for context. Across embodied benchmarks it improves success by 6.3–18.3 points over the strongest collaboration baseline, approaching or exceeding cloud-only success while cutting median time-between-action latency by 28.8–82.6%.

### [ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models](https://arxiv.org/abs/2610.27040) — Yinhe Wang, Yao Mu 等(DAXIAO Robotics)
🏷️ 交叉方向 / Also: 空间智能 / Spatial intelligence
开源状态 / Code: ✅ 已开源 / Released — [github.com/DAXIAORobotics/ACE-Brain-0.6](https://github.com/DAXIAORobotics/ACE-Brain-0.6)(HF githubRepo,radar new_repos 8 stars;仓库存在)
- 🇨🇳 通用多模态模型的空间感知把高层推理与物理场景连接起来,作者研究扩展视觉 grounding 以强化具身通用操作的感知基础。构建统一数据管线,结合机器人操作录像与多源视觉数据,自动标注后转成可验证的 grounding 监督;在约 150 万样本上微调 Qwen3.5-9B 得到 ACE-Brain-0.6。它在七个公开 grounding 基准中四个超过 GPT-6 Astra,总体平均 75.41 对 73.68;且随数据发布逐步扩充,聚合 grounding 性能持续提升。
- 🇬🇧 Spatial perception links high-level reasoning to the physical scene, so the authors scale visual grounding for embodied operation. A unified pipeline combines auto-annotated robot manipulation recordings with diverse visual data into verifiable grounding supervision; fine-tuning Qwen3.5-9B on ~1.5M samples yields ACE-Brain-0.6, which beats GPT-6 Astra on four of seven public grounding benchmarks (average 75.41 vs 73.68), improving steadily as data releases grow.

### [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](https://arxiv.org/abs/2610.28589) — Xinxin Liu 等(HF 21 upvotes;v 更新于 10-21)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ✅ 已开源 / Released — [github.com/xinxinliu-ai/AgenticRoboRL](https://github.com/xinxinliu-ai/AgenticRoboRL)(HF githubRepo,仓库存在;摘要写 "We will release the framework and trained planner checkpoints",检查点是否已放出未核对)
- 🇨🇳 智能体机器人系统依赖闭源强模型做规划器,且不提升规划器自身能力。AgenticRoboRL 面向不同执行机制(VLA 技能调用、控制代码生成)后训练规划器:SFT 加多轮 RL,通过 harness 特定适配器把记录的规划交互与任务结果连接成统一 RL 管线。在 LIBERO-PRO 上将 9B 规划器成功率从 18.1% 提升到 71.0%(无外部记忆),接近带外部记忆的 Codex(GPT-5.5)的 72.1%。
- 🇬🇧 Agentic robot systems rely on closed-source planners and don't improve the planner itself. AgenticRoboRL post-trains planners across harnesses (VLA skill invocation, control-code generation) with SFT plus multi-turn RL via harness-specific adapters feeding a common pipeline. On LIBERO-PRO it lifts a 9B planner from 18.1% to 71.0% without external memory, near Codex (GPT-5.5) with memory at 72.1%.

**其余 4 条仅列名 / remaining 4, name only(总计 9):** [Alpha: Fault Injection for LLM-Driven Embodied Manipulation](https://arxiv.org/abs/2610.30197)(✅ [代码](https://github.com/jonajoy142/embodied-agent-chaos);Oracle 64.0% vs LLM 44.0%)、[Externalise the Memory](https://arxiv.org/abs/2610.30478)(检索外挂记忆使学生策略 +34 pp)、[TEAR](https://arxiv.org/abs/2610.30819)(遥操作/自主权限路由,遥操作占比 19.8–27.4%)、[Scale and Selection: Automatic Harness Evolution](https://arxiv.org/abs/2609.39304)(replacement)。另见 / See also: λ₀、WholeBodyMem、LocoManiLab(已归入 运动控制·RL / filed under Motion Control · RL)。

---

## VLA(共 7 条,展开 6 / 7 total, 6 expanded)

### [FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models](https://arxiv.org/abs/2610.31423) — Huixin Xu, Ziya Yu, Peng Li(Comments:CoRL 2026)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 现有 VLA 的多视角输入未被充分利用,策略倾向于持续依赖腕部视角,不能随操作阶段动态调整全局/局部依赖。FocusVLA 从历史动作预测未来交互意图,并以此引导动作生成中的动态视角路由,其意图预测与路由模块可插入现有 VLA 而无需改动核心架构。RoboTwin 2.0 上平均成功率比最强基线 π0.5 高 10.10 个百分点;真实世界成功率由 71.7% 升至 85.0%。
- 🇬🇧 Existing VLAs under-use multi-view inputs and over-rely on the wrist view regardless of stage. FocusVLA predicts future interaction intent from historical actions to drive dynamic view routing, and its modules plug into existing VLAs without changing core architecture. On RoboTwin 2.0 it beats the strongest baseline π0.5 by 10.10 points on average; real-world success rises from 71.7% to 85.0%.

### [When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies](https://arxiv.org/abs/2610.30735) — Shivakanth Sujit, Kai Arulkumaran 等(Comments:CoRL 2026)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 流匹配是 VLA 策略的主流方法,但推理需迭代求解 ODE,限制控制频率;已有工作提出单步生成新目标。作者追问这些额外目标是否必要。在六个流匹配 VLA 上发现,只要模型训练充分且容量足够,单步生成基本能匹配多步采样,多步积分没有一致优势。结论:大型 VLA 的单步策略可由多步模型"免费"得到,无需重训、蒸馏或辅助目标即可低延迟部署(摘要未给出具体数值)。
- 🇬🇧 Flow matching dominates VLA policies but needs iterative ODE solving, limiting control frequency; many works add single-shot objectives. Across six flow-matching VLAs, one-step generation largely matches multi-step sampling as long as models are sufficiently trained with enough capacity. So large VLAs get a single-step policy for free, enabling low-latency deployment without retraining, distillation or auxiliary objectives; no numbers in the abstract.

### [FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies](https://arxiv.org/abs/2610.31427) — Tao Lin, Bo Zhao 等
开源状态 / Code: ✅ 已开源 / Released — [github.com/FastHarness/fast-harness](https://github.com/FastHarness/fast-harness)(Comments 给出,仓库存在)
- 🇨🇳 智能体机器人系统用语言模型监督策略,但逐动作块审查开销大。FastHarness 自适应调度 GPT-6 Astra 对 π0.5 的监督:快速路径用阶段记忆与已审查结果随经验累积降低审查频率,恢复路径专注纠错,验证恢复后回到常规执行,策略保持冻结。四个仿真任务中审查 token 平均降低 57.2%,平均回合时间由 85.5 降到 52.0 分钟,平均成功率由 GPT-as-Policy 的 80% 升至 97.19%。
- 🇬🇧 Reviewing every action chunk with an LM supervisor is expensive. FastHarness schedules GPT-6 Astra supervision of a frozen π0.5: a fast path with stage memory lowers review frequency as experience accumulates, and a recovery path focuses on corrections. On four simulated tasks reviewer tokens drop 57.2% on average, episode time falls from 85.5 to 52.0 minutes, and mean success rises from 80% (GPT-as-Policy) to 97.19%.

### [Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models](https://arxiv.org/abs/2610.31569) — Yufeng Liu 等
开源状态 / Code: ❓ 未知 / Unknown — 仅项目页 [lyfeng001.github.io/Echo](https://lyfeng001.github.io/Echo/)
- 🇨🇳 让 VLA 识别任务完成/失败以便停止、恢复或重规划,现有方法需细粒度监督、外部监控模型或复杂架构。Echo 把停止与失败信号作为每个动作块的两个额外维度,与动作一同去噪;无需逐帧进度标注,通过构造成功/失败/恢复轨迹提供互补监督,并让状态信号比动作更快去噪,使后续动作去噪以更干净的状态估计为条件。大量真机操作实验表明它能准确预测任务状态并持续提升策略表现(摘要未给出数值)。
- 🇬🇧 Task-status prediction for VLAs usually needs fine-grained supervision, external monitors or complex designs. Echo adds stop and failure signals as two extra dimensions of each action chunk denoised with the actions, learns them without frame-level progress labels from constructed successful/failed/recovery trajectories, and denoises signals faster than actions so later steps condition on cleaner status. Extensive real-world experiments show accurate status prediction and consistently better policy performance; no numbers are in the abstract.

### [Progress Probes P²: Lightweight Runtime Monitoring for Vision-Language-Action Models](https://arxiv.org/abs/2610.31613) — Atiksh Bhardwaj, Wei-Chiu Ma 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 部署 VLA 需要运行时监控,现有监控依赖外部 VLM,复杂且昂贵。作者研究 VLA 自身激活能否提供监控信息:在示范上对策略激活训练线性探针估计进度,并标记偏离期望进度的执行。基于开源 π0.5,在仿真与真机操作任务上,该方法在失败检测上与基于 VLM 的监控相当或更好,也优于需要失败数据训练的方法。
- 🇬🇧 VLA deployment needs runtime monitors, but VLM-based monitors are costly. P² trains linear probes on a VLA's own activations from demonstrations to estimate progress and flags deviations. With open-source π0.5 across simulated and real manipulation tasks it is competitive with or better than VLM-based monitors and methods requiring failure data.

### [SmolVLA-MoE: Sparse Mixture-of-Experts for Efficient Multi-Task Robotic Manipulation](https://arxiv.org/abs/2610.30732) — Shiyang Zhang 等(cs.CV)
开源状态 / Code: ❓ 未知 / Unknown — 摘要称 "Our code is publicly available at [github.com/dudu435/smolvla-moe](https://github.com/dudu435/smolvla-moe)",但匿名 `git ls-remote` 失败(仓库不可访问或不存在),待核实
- 🇨🇳 轻量 VLA 的单一稠密动作专家限制多任务能力。SmolVLA-MoE 在动作专家的 FFN 层引入稀疏 MoE,用 token 级路由器选专家,并加入权重可调的共享专家以平衡预训练能力继承与任务特化;推理只激活一个专家 FFN,激活参数约 5 亿(含冻结 VLM),总存储约 8 亿。LIBERO 四个任务套件平均成功率 84.25%,高于 SmolVLA 的 82.75% 和 OpenVLA-7B 的 76.5%,推理效率相当。
- 🇬🇧 A single dense action expert limits lightweight VLAs in multi-task settings. SmolVLA-MoE puts sparse MoE into the action expert's FFN layers with a token-level router and a tunable shared expert, activating one expert FFN (≈500M activated, ≈800M stored parameters including the frozen VLM). On four LIBERO suites it averages 84.25% versus SmolVLA 82.75% and OpenVLA-7B 76.5% at comparable efficiency.

**其余 1 条仅列名(总计 7):** [Do VLAs Really Follow Instructions?](https://arxiv.org/abs/2610.21251)(replacement)。另见 / See also: WholeBodyMem(已归入 运动控制·RL)。*(HF 另有 [RoboCasa-Shift](https://github.com/HaochengWang23/RoboCasa-Shift) VLA 鲁棒性评测,仅据标题。)*

---

## VLN(共 4 条,展开 3 / 4 total, 3 expanded)

### [Asking Less, Adapting Better: Feedback-Efficient Test-Time Adaptation for Vision-and-Language Navigation (FETA)](https://arxiv.org/abs/2610.30643) — Zixu Wang 等(cs.CV)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 VLN 智能体在未见环境中性能退化;无监督熵最小化会传播错误,人类反馈方法又对所有步骤均匀监督、反馈利用低效。FETA 用分层样本选择:先筛选归一化策略熵波动大的轨迹,再用熵梯度显著性选出关键动作,仅就其对错查询一次二值反馈;差异感知熵优化目标只在被查询步更新策略,并对预测—反馈差异更大的样本自适应加权。多个基准上以更少人工干预达到最优性能,并对噪声反馈与持续适应保持稳健(摘要未给出具体数值)。
- 🇬🇧 VLN agents degrade in unseen environments; entropy minimization propagates errors and trajectory-level human feedback is applied uniformly and inefficiently. FETA filters trajectories by entropy fluctuation, picks the critical action via entropy-gradient saliency, asks one binary feedback, and updates only at the queried step with discrepancy-aware adaptive weighting. It reaches state-of-the-art on multiple benchmarks with fewer interventions and stays robust under noisy feedback and continual adaptation; no numbers in the abstract.

### [OASIS: Online Anchor-centric Scene Inference System for Open-Vocabulary Retrieval and Navigation in Dynamic Environments](https://arxiv.org/abs/2610.30589) — Kaiyao Liao 等(Comments:ACM MM 2026 oral)
🏷️ 交叉方向 / Also: 空间智能与语义建图 / Spatial intelligence & semantic mapping
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 在线轻量建图语义有限、稠密建图开销高且易受干扰,且难在场景变化后重新定位物体。OASIS 用稀疏锚点节点表示环境,每个节点整合语义描述、视觉特征与几何状态,紧凑的锚点记忆支持按需取证与分层检索,并复用导航中的瞬时观测来重定位被移动的物体。在仿真与真实环境中,包括标准检索基准以及静态/动态导航,能完成复杂开放词汇检索与导航,并实现场景变化后的物体重定位(摘要未给出数值)。
- 🇬🇧 Online lightweight maps lack semantics while dense maps are costly and distractor-prone, and both struggle to relocalize objects after changes. OASIS represents scenes with sparse anchor nodes carrying semantic, visual and geometric state, supports on-demand evidence extraction and hierarchical retrieval, and reuses transient observations to relocalize moved objects. It performs open-vocabulary retrieval and navigation in simulation and the real world under static and dynamic settings; no numbers in the abstract.

### [CMAR-search: Commonsense and Memory Augmented Reasoning for Object Search in Dynamic Interactive Environments](https://arxiv.org/abs/2610.30606) — Kaiyao Liao 等(Comments:ICRA 2026)
开源状态 / Code: ✅ 已开源 / Released — radar new_repos 中 [github.com/starry-curry-30/CMAR-search](https://github.com/starry-curry-30/CMAR-search)(名称/描述与论文一致;1 star,内容未核对)
- 🇨🇳 3D 场景图只提供粗粒度分割、无法识别储物/休闲等功能区,导致大场景中低效的穷举探索,也不适应物体被移动。CMAR-search 用关于区域功能的常识与环境记忆构建功能性 3D 场景图 F3DSG,将环境组织为功能区及其容器,支持宏观区域和微观容器两级分层规划,并持续融合实时感知、记忆与常识来重定位物体。仿真与真机实验显示成功率和搜索效率显著超过最先进基线(摘要未给出数值)。
- 🇬🇧 3D scene graphs are coarse and lack functional areas, forcing exhaustive search and failing under object relocation. CMAR-search builds a Functional 3D Scene Graph from area-function commonsense and memory, plans hierarchically over areas and containers, and keeps integrating perception, memory and commonsense to relocalize objects. Simulation and real-world experiments show significantly higher success and search efficiency than baselines; no numbers in the abstract.

**其余 1 条仅列名(总计 4):** [NavBind: Diagnosing Instruction-Action Binding at Route Forks in Navigation VLAs](https://arxiv.org/abs/2610.29203)(replacement);另见 / See also: TRACE traversability(已归入 运动控制·传统)、[RangeNav](https://arxiv.org/abs/2610.29845)(replacement,LiDAR 导航预训练)。

---

## 世界模型与 WAM / World Models & WAM(共 10 条,展开 8 / 10 total, 8 expanded)

### [UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry](https://arxiv.org/abs/2610.30991) — Jialin Tian, Zhuofan Li, Xinkai Wang 等
开源状态 / Code: ❓ 未知 / Unknown — 仅项目页 [kksham111.github.io/UniFlowWAM_ProjectPage](https://kksham111.github.io/UniFlowWAM_ProjectPage/)
- 🇨🇳 机器人示范未说明两帧之间 3D 世界如何变化,以往工作把流作为外部模块或额外预测头。UniFlowWAM 把 3D 场景流作为与视觉、动作并列的第三模态:每个模态一个专家的扩散 Transformer,经联合注意力交换信息,并在十目标"角色网格"下训练(每个模态为目标/条件/缺席),同一模型可作策略、前向/逆向动力学及未来视觉特征或 3D 流预测器。RoboCasa-GR1 上成功率由无流基础模型的 52.1% 升至 56.4%,LIBERO 保持 98.1%、LIBERO-Plus 零样本 87.7%,真机四个双手任务平均 87.0%,最强基线 68.5%。
- 🇬🇧 Demonstrations don't say how the 3D world changed between frames, and prior work kept flow outside the policy. UniFlowWAM makes 3D scene flow a third modality beside vision and action in a diffusion transformer with one expert per modality and joint attention, trained under a ten-objective role grid so one model serves as policy, forward/inverse dynamics and future feature/flow predictor. On RoboCasa-GR1 success rises from 52.1% to 56.4%, LIBERO stays at 98.1%, LIBERO-Plus zero-shot reaches 87.7%, and real-robot average is 87.0% versus 68.5% for the best baseline.

### [Self-Distilling Future Video Representations for World Action Models (FRED)](https://arxiv.org/abs/2610.30320) — Huiwon Jang, Jinwoo Shin 等
开源状态 / Code: ❓ 未知 / Unknown — 仅项目页 [huiwon-jang.github.io/FRED](https://huiwon-jang.github.io/FRED/)
- 🇨🇳 一类 WAM 以单步去噪得到的中间未来视频表征条件化动作解码器来提高推理效率,使动作预测依赖这些表征的质量。FRED 通过自蒸馏,以真实未来观测提取的表征为目标,训练模型从噪声一步预测未来表征,并以历史观测提供时间上下文。多种真实操作场景中持续优于其他 WAM,在长时程与域外零样本任务增益尤其大;对仅在人类视频中演示、机器人训练数据中缺失的任务,成功率 50.0%,最佳对比 WAM 为 19.4%。
- 🇬🇧 Efficient WAMs condition an action decoder on future video representations from one denoising step, so action quality depends on those representations. FRED self-distills, predicting future representations from noise with targets from ground-truth future observations and adding historical context. It consistently beats competing WAMs in real manipulation, especially long-horizon and zero-shot out-of-domain tasks, reaching 50.0% on tasks demonstrated only in human videos versus 19.4% for the best competing WAM.

### [Agentic World Action Models (AW-0)](https://arxiv.org/abs/2610.30136) — Zhuoyang Liu, Dantong Niu 等
开源状态 / Code: ❓ 未知 / Unknown — 项目页 [agentic-wam.github.io](https://agentic-wam.github.io/)(未见代码)
- 🇨🇳 现有 WAM 缺乏组合式技能复用,智能体机器人又缺少物理动力学预测基础。AW-0 把代码、未来视频、机器人动作作为三条耦合生成流,在统一混合 Transformer 中联合建模:代码专家生成参数化技能例程与控制逻辑,视频与动作专家生成未来视觉状态和底层电机指令;并提出自动化管线为机器人与人类视频轨迹标注对齐程序,把重复例程整合为可复用技能库。RoboTwin 2.0 与真实双手任务上优于 VLA 与 WAM 基线,语言遵循、语义推理和鲁棒性也有提升(摘要未给出数值)。
- 🇬🇧 WAMs lack compositional skill reuse and agentic robotics lacks predictive grounding. AW-0 jointly models code, future video and actions as three coupled streams in a mixture-of-transformers: a code expert emits parameterized skills and control logic while video and action experts generate future states and low-level commands, with an automated pipeline labeling trajectories with programs and consolidating a skill library. It improves over VLA and WAM baselines on RoboTwin 2.0 and real bimanual tasks, with gains in language following, reasoning and robustness; no numbers are given.

### [Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation (P³-WAM)](https://arxiv.org/abs/2610.22363) — Zirui Wu 等(v 更新于 10-22)
开源状态 / Code: ❓ 未知 / Unknown — 项目页 [p3-wam.pages.dev](https://p3-wam.pages.dev/)
- 🇨🇳 P³-WAM 统一学习 3D 感知、动作条件预测与目标导向规划三种模式:Perceive 从视频重建手部与相机轨迹,Predict 在指定动作下生成视觉未来,Plan 联合生成动作轨迹及其预期视觉后果。通过混合 Transformer 把紧凑的结构化 3D 动作表示注入预训练视频扩散 Transformer,随机的模态可见性使视频与 3D 动作可作条件或预测目标。统一训练提升三种能力,四个数据集上 3D 手部重建与动作条件视频预测优于专用基线,规划视频的指令遵循和动作进展强于视频生成基线(摘要未给出数值)。
- 🇬🇧 P³-WAM unifies Perceive (reconstruct hand motion and camera trajectories), Predict (generate visual futures under given actions) and Plan (jointly generate actions and their anticipated visuals). A compact structured 3D action representation is injected into a pretrained video diffusion transformer via a mixture-of-transformers with randomized modality visibility. Unified training improves all three modes, beats specialized baselines on 3D hand reconstruction and action-conditioned video prediction across four datasets, and gives stronger instruction adherence than video-generation baselines; no numbers in the abstract.

### [Skeleton-Grounded Latent Action Model for Robot World Models (SkeLAM)](https://arxiv.org/abs/2610.31474) — Qi Lv, Mike Shou 等(HF 1 upvote)
开源状态 / Code: ❓ 未知 / Unknown — 仅项目页 [aopolin-lv.github.io/SkeLAM](https://aopolin-lv.github.io/SkeLAM/)
- 🇨🇳 重建驱动的潜在动作把机器人运动与物体响应混在一起,难以对应机器人控制。SkeLAM 把潜在动作分解为由机器人骨架监督的运动学分量和保留互补视觉动力学的残差分量,以跨模态交换重建让 RGB 与骨架导出的运动学表示可互换,世界模型通过独立路径引入两者并用分支 dropout 降低对未来残差信息的依赖;轻量适配器把机器人动作映射到运动学空间。DROID 上末端执行器 ADE 比 DreamDojo 降低 19.5%、LPIPS 降低 11.1%,并支持零样本人到机器人动作迁移,策略评估中预测成功率与真机一致。
- 🇬🇧 Reconstruction-driven latent actions mix robot motion with object responses. SkeLAM splits latent actions into a skeleton-supervised kinematic part and a residual part, uses cross-modal swap reconstruction and branch dropout, and a lightweight adapter maps robot actions to the kinematic space. On DROID it cuts end-effector ADE by 19.5% and LPIPS by 11.1% versus DreamDojo, shows zero-shot human-to-robot motion transfer, and its predicted success rates agree with real executions.

### [DRILL: Training World Models to Improve Policies, Not Predict Pixels](https://arxiv.org/abs/2610.30814) — Zhaolu Kang 等(cs.CV;NeurIPS 2026)
🏷️ 交叉方向 / Also: VLA、RL(目标是 VLA 的 RL 后训练;面向操作策略,非 locomotion/全身控制,保留在世界模型类)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 用世界模型做 VLA 的 RL 后训练时,模型通常训练为预测像素,与"产生改进策略的学习信号"的目标不一致:像素 MSE 更低可能带来更差的策略梯度。DRILL 是双层框架,更新世界模型以最大化策略在想象 rollout 上做一次内层 GRPO 更新后的回报,有两种实例:闭式代理 DRILL-VWI(按策略访问、组相对优势、模型置信度重加权误差)和完整元梯度方法 DRILL-IMG(截断 Hessian-向量积)。五个操作模拟器、两种 VLA 主干上,DRILL-IMG 平均成功率比 WMPO 高 13.1 点、比 RLVR-World 高 7.9 点;为策略效用训练的世界模型即使下一帧像素 MSE 高 17% 仍产生更好策略。
- 🇬🇧 World models used for VLA RL post-training are trained to predict pixels, yet lower pixel MSE can yield worse policy gradients. DRILL is a bilevel framework that updates the world model to maximize return after an inner GRPO update on imagined rollouts, via a closed-form surrogate (DRILL-VWI) and a full meta-gradient method (DRILL-IMG). Across five manipulation simulators and two VLA backbones, DRILL-IMG raises mean success by 13.1 points over WMPO and 7.9 over RLVR-World, and a policy-utility world model wins despite 17% higher next-frame pixel MSE.

### [DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models](https://arxiv.org/abs/2610.30781) — Adam Lee, Ziwei Liu 等(cs.CV)
开源状态 / Code: ❓ 未知 / Unknown — 项目页 [dexplicit.github.io](https://dexplicit.github.io)
- 🇨🇳 现有灵巧操作世界模型把动作条件动力学、相机运动与视觉合成纠缠在视频生成里,或只用无物体结构的点轨迹。DeXplicit 先在度量 3D 中显式预测世界演化:轻量 3D 动力学网络从初始场景与未来手部轨迹预测物体级运动与形变,再把外观沿预测运动传输并投影到未来视角,渲染器只需补全不确定和新可见内容;还支持每块仅两步去噪的因果生成。HOT3D、OakInk2、PhysTwin 上移动点误差比 PointWorld 低 27–40%,HOT3D 物体保真 IoU+ 提升 47%,两步因果生成相比 14B 双向配置加速 57 倍。
- 🇬🇧 Existing dexterous world models entangle dynamics, camera motion and synthesis in video generation or use object-agnostic point trajectories. DeXplicit first predicts explicit metric-3D object motion and deformation from the scene and future hand trajectory, then transports appearance through that motion so the renderer only completes uncertain content, with two-step causal generation per block. It reduces moved-point error by 27–40% versus PointWorld across HOT3D, OakInk2 and PhysTwin, improves object IoU+ by 47% on HOT3D, and is 57× faster than the 14B bidirectional configuration.

### [In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations](https://arxiv.org/abs/2610.30988) — Hengyi Sim, Fei Chen 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 软体衣物操作状态维度高且形变依赖材料,学习式世界模型需大量真实数据与推断潜在属性的机制。作者提出 Soft-Object World Model:在大规模仿真软体交互上训练的 Transformer,做生成式全状态估计与动作条件动力学预测,并采取措施缓解 sim-to-real 差距;通过对可变长度部分点云历史的上下文学习推断潜在形状与材料线索,无需更新权重即可泛化到不同机器人本体、材料参数、衣物类型与协调模式,并与目标条件动作规划器集成。在仿真与真实双臂叠衣中,重建保真、预测精度和任务成功率均有提升(摘要未给出数值)。
- 🇬🇧 Garment manipulation has high-dimensional, material-dependent dynamics, and learned world models need much real data plus a way to infer latent properties. The Soft-Object World Model is a transformer trained on large-scale simulated soft-object interactions that performs generative full-state estimation and action-conditioned prediction, using in-context learning over partial point-cloud history to infer shape and material without weight updates, then pairs with a goal-conditioned planner. Simulation and real bimanual folding show better reconstruction, prediction accuracy and success; no numbers in the abstract.

**其余 2 条仅列名(总计 10):** [RGraph-Eval](https://arxiv.org/abs/2610.31121)(机器人视频生成评测,场景图;代码"将公开" 🕒)、[Inside-JEPA](https://arxiv.org/abs/2610.31194)(JEPA 潜空间关系 grounding;RH20T 关系 AUROC +.081)。HF/radar 另见:[LaLa-World](https://github.com/junha1125/LaLa-World)、[ALPS](https://github.com/UCSC-VLAA/ALPS)、[Looking Ahead](https://github.com/TencentARC/Looking-Ahead)、[LeWAM](https://github.com/MinghaoFu/lewam)(star +8)——均未读取论文摘要,仅作线索。另见 / See also: DiffDreamer(已归入 运动控制·RL)、SuperMimic(监测项,运动控制·RL)。

---

## 空间智能与 SLAM / Spatial Intelligence & SLAM(共 8 条,展开 5 / 8 total, 5 expanded)

### [SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?](https://arxiv.org/abs/2610.26659) — Zhaoxi Zhang 等(HF 131 upvotes;v 更新于 10-22)
开源状态 / Code: ✅ 已开源 / Released — [github.com/JesseZZZZZ/SpatialScout](https://github.com/JesseZZZZZ/SpatialScout)(摘要给出,仓库存在)
- 🇨🇳 空间问答难以说明模型能否通过自主探索构建准确度量地图。SpatialScout 基准含 80 个室内场景、3,140 个目标物体,VLM 智能体在给定物体清单、RGB、相机标定与位姿下控制相机探索并估计共享坐标系中的物体中心,需协调视角选择、跨视角关联、几何估计与地图修订,评测联合衡量定位精度与覆盖率。前沿 VLM 表现有限:最强的 Claude Opus 5.5 平均重叠分数 41.71%,47.23% 的目标 IoU 超过 0.5,仅 3.25% 超过 0.9。
- 🇬🇧 Spatial QA doesn't show whether models can build accurate metric maps by exploring. SpatialScout has 80 indoor scenes with 3,140 targets; VLM agents control a camera under bounded budgets and estimate object centers in a shared frame, scored on localization accuracy and coverage. Frontier VLMs are limited: the best, Claude Opus 5.5, gets a mean overlap score of 41.71%, with 47.23% of targets above IoU 0.5 and only 3.25% above 0.9.

### [Point-Level Refinable Semantic Mapping for Spatial Understanding](https://arxiv.org/abs/2610.31476) — Taimeng Fu 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 物体中心语义地图多为只追加点的集成,感知误差累积且物体移动后旧点残留。作者提出在线可精炼语义建图:每个物体点维护置信度,由多视角时间证据在线更新(一致观测强化可靠点,不一致的分割、深度、可见性线索抑制伪点与过期点),并结合目标跟踪与重识别在运动和重定位下保持实例身份。建图精度在 Replica 上比先前方法高 3.46%、ScanNet 上高 2.55%,动态与感知噪声下稳健,并在物体导航和具身问答中取得 82.4% 与 76.7% 的成功率。
- 🇬🇧 Object-centric semantic maps append points and never re-evaluate them, so errors accumulate and stale points persist. The method keeps a per-point confidence updated from multi-view temporal evidence (consistent observations reinforce, inconsistent masks/depth/visibility suppress) with tracking and re-identification. Mapping accuracy improves by 3.46% on Replica and 2.55% on ScanNet, it is robust in dynamic scenes and noise, and gives 82.4% object-navigation and 76.7% embodied-QA success.

### [Consistent Distributed Invariant EKF SLAM with Point and Object Features (Joint-CI)](https://arxiv.org/abs/2610.31221) — Mengya Xu, Shoudong Huang 等(Comments:RA-L 投稿)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 多机器人 SLAM 交换地图会产生未知相关性;协方差交叉(CI)可避免跟踪相关,但在右不变 EKF SLAM 中邻居的地图估计表示在自身误差坐标下且与位姿相关,不能直接 CI 融合。Joint-CI 利用邻居局部后验与机器人间观测,在接收方误差坐标下构造位姿与共同特征的联合估计,保留机器人—特征及特征—特征相关,再用部分状态 CI 融合。证明统一公式与融合保持与全局旋转/平移对应的六个不可观方向,通信与融合保持一阶协方差一致性;蒙特卡洛仿真与真实数据集实验显示估计精度提升且不确定性保持一致、略保守。
- 🇬🇧 In multi-robot RI-EKF SLAM, a neighbor's map is in its own error coordinates and correlated with its pose, so covariance intersection can't fuse it directly. Joint-CI builds a joint pose-and-common-feature estimate in the receiver's error coordinates from the neighbor's posterior and an inter-robot observation, then fuses it by partial-state CI. It preserves the six unobservable directions and first-order covariance consistency; Monte Carlo and real-dataset experiments show better accuracy with consistent, mildly conservative uncertainty.

### [A Sparse Topometric Graph for Scalable Cross-Session Indoor Navigation](https://arxiv.org/abs/2610.31432) — Eun Sun Lee 等
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 精细测量建图在场景或传感器变化下昂贵且脆弱。作者提出稀疏拓扑度量图:节点编码局部 3D 几何、边为按距离加权的可通行连接,学习式图匹配网络同时利用节点几何描述子与邻域连接找到跨会话一致的子图结构,对局部歧义、重复结构、场景变化、不同传感器模态或有限重叠稳健。在跨会话点目标导航中成功率最高(Gibson 77.1%,3D-FRONT 场景变化下 40.0%),相比点级表示内存降低两个数量级以上。
- 🇬🇧 Fine-grained maps are costly and brittle to scene or sensor changes. A sparse topometric graph (nodes with local 3D geometry, distance-weighted traversability edges) and a learned graph-matching network find consistent subgraphs across sessions despite ambiguity, repetition or scene change. It achieves the highest success (77.1% on Gibson, 40.0% under 3D-FRONT scene changes) and cuts memory by over two orders of magnitude versus point-level representations.

### [HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction](https://arxiv.org/abs/2610.31635) — Zunnan Xu, Chen Change Loy 等(cs.CV)
开源状态 / Code: ✅ 已开源 / Released — 摘要称 "The codes are available at [kkakkkka.github.io/HiP3R](https://kkakkkka.github.io/HiP3R)"(项目页链接,未核对仓库)
- 🇨🇳 前馈模型能由短视频窗口准确估计相机运动与 3D 几何,但数千帧长序列需分块,导致各块坐标系不一致且重复估计共享相机。HiP3R 用层次化位姿图:先优化鲁棒的块级 Sim(3) 图确定全局布局与尺度,再固定布局、为每帧估计一个共享 SE(3) 相机,将重叠窗口预测合并为单一轨迹。无需额外训练或微调,可用于块式与流式后端,多个基准上改善相机轨迹与 3D 重建(摘要未给出数值)。
- 🇬🇧 Feed-forward models handle short windows, but thousands of frames require chunks with inconsistent frames and duplicate cameras. HiP3R optimizes a chunk-level Sim(3) pose graph for global layout and scale, then fixes it and estimates one shared SE(3) camera per frame. It needs no training or fine-tuning, works with chunk-based and streaming backends, and improves trajectories and reconstruction across benchmarks; no numbers in the abstract.

**其余 3 条仅列名(总计 8):** [OmniRay: Camera-Agnostic Monocular 3D Reconstruction](https://arxiv.org/abs/2610.31645)(项目页 [nam1410.github.io/omniray](https://nam1410.github.io/omniray/))、[Evaluation of Front-End Feature Matching for Lunar Visual SLAM](https://arxiv.org/abs/2610.30774)(11 种检测器—匹配器组合基准;SuperPoint+LightGlue 16 ms/帧)、[Event-based SLAM Benchmark for High-Speed Maneuvers](https://arxiv.org/abs/2604.24033)(replacement)。HF 线索:[CompactSplat](https://github.com/hebing-sjtu/CompactSplat)、[Awesome-Multimodal-Embodied-Agent](https://github.com/showlab/Awesome-Multimodal-Embodied-Agent)。另见 / See also: ACE-Brain-0.6(已归入 具身智能与机器人基础模型)。

---

## 其他值得关注 / Other Notable(仅列名 / names only,共 3)

- [AstroBench](https://arxiv.org/abs/2610.31064)(✅ [代码](https://github.com/AstroUpLab/AstroBench);冻结 π0.5 DROID 策略静态目标捕获 2/200、运动目标 4/200;ACT 立方体专用策略 8/10 与 6/10 / free-floating capture benchmark)
- [To Route or to Adapt?](https://arxiv.org/abs/2610.31095)(自动驾驶多专家扩散规划,CoRL 2026,✅ 代码与权重 [github.com/tlab-wide/RouteOrAdapt;20](https://github.com/tlab-wide/RouteOrAdapt;20) 个目标区域场景奖励微调,联合重放均值偏移 6.9 m vs 静态默认 12.4 m)
- [TerraTransfer++](https://arxiv.org/abs/2610.30319)(自动驾驶,无示范端到端规划;NAVSIM navhard 59.4 EPDMS,navtest 95.5 PDMS)

---

## GitHub 动态 / GitHub Highlights

### Star 增长(radar,相对 10-22 08:41 UTC 快照)/ Star growth

| 仓库 / Repo | Stars | 增长 / Δ | 说明 / Note |
|---|---|---|---|
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28,404 | +21 | 机器人学习框架 / end-to-end robot learning |
| [SkyworkAI/Matrix-Game](https://github.com/SkyworkAI/Matrix-Game) | 2,728 | +12 | 流式神经渲染可玩世界(世界模型)/ streaming neural rendering |
| [datawhalechina/every-embodied](https://github.com/datawhalechina/every-embodied) | 4,189 | +13 | 从零构建 VLA/具身教程 / embodied tutorial |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 15,827 | +11 | 物理引擎,3.17.0 发布 / physics engine, 3.17.0 released |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 8,420 | +10 | 机器人学习框架 / robot learning framework |
| [MinghaoFu/lewam](https://github.com/MinghaoFu/lewam) | 310 | +8 | LeWAM:JEPA 端到端世界与动作建模 / JEPA world-action model |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 14,353 | +8 | π0/π0.5 开源 / open π models |
| [TencentARC/Looking-Ahead](https://github.com/TencentARC/Looking-Ahead) | 59 | +18(新建 / new) | 自回归视频生成中的未来演化建模 / future-evolution modeling |

(noise:gods-eye-view +227、RuView、Sana、text-to-cad 等与主题关系弱,不列。)

### 新仓库精选(radar new_repos,291 个中筛选)/ Notable new repos

- [Motphys/Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic)(30★):SuperMimic 在 UniLab 上的**独立复现**,人形全身动作跟踪;**非官方**。同类第三方复现:[zita-ch/supermimic_vibed](https://github.com/zita-ch/supermimic_vibed)(250★)、[CuboiLeo/SuperMimic-Reproduced](https://github.com/CuboiLeo/SuperMimic-Reproduced)(88★)、[JackMin7/supermimic_whole_body_tracking](https://github.com/JackMin7/supermimic_whole_body_tracking)(9★)。
- [eth-siplab/HumanoidPose](https://github.com/eth-siplab/HumanoidPose)(4★):"Vision as Proprioception: Estimating Humanoid Robot Pose from Video" 官方代码(未读论文)。
- [zhangy0822/CofactVLA](https://github.com/zhangy0822/CofactVLA)(15★)、[PolyU-VCLab/OSWAM](https://github.com/PolyU-VCLab/OSWAM)(3★,单步动作生成 WAM)、[bondtesty/let-it-be-simple](https://github.com/bondtesty/let-it-be-simple)(VLA 单步动作生成)、[UCSC-VLAA/ALPS](https://github.com/UCSC-VLAA/ALPS)(7★)、[Kai-Sheng-caesar/NavJev-Code](https://github.com/Kai-Sheng-caesar/NavJev-Code)(VLN)、[PyyWill/ReStruct](https://github.com/PyyWill/ReStruct)(CoRL 2026,推理时策略引导)。均未读对应论文,仅据仓库描述。
- 值得留意的控制类个人项目:[TC635807/mjx-go2-training](https://github.com/TC635807/mjx-go2-training)(Go2 地形 locomotion,MJX + Brax PPO)、[Ziyeeee/openpi_rlt](https://github.com/Ziyeeee/openpi_rlt)(openpi 上的 RL Token + RTC 实现)。

### 新 Release / New releases(窗口内 / within window)

- **google-deepmind/mujoco [3.17.0](https://github.com/google-deepmind/mujoco/releases/tag/3.17.0)**(10-22 21:45 UTC):新增批量 API `mujoco/mjbatch.h`(Python `mujoco.batch`),在自带线程池上并行步进同一模型的多个仿真,内存随线程数而非仿真数增长,结果与普通循环逐位一致;支持逐仿真模型/选项字段、状态后观测、轨迹记录、持久仿真(sleep 所需)与任意逐仿真函数,设计参照 kevinzakka/mjbatch。Engine:flex 改进,新增 1D flex 弯曲弹性(无扭转各向同性离散弹性杆模型,`section` 属性选圆或矩形截面)。(radar 保存的 body 被截断,后续条目未见 / body truncated in radar JSON.)
- **Genesis-Embodied-AI/Genesis [v1.4.5](https://github.com/Genesis-Embodied-AI/genesis-world/releases/tag/v1.4.5)**(10-22 21:38 UTC):显著加速精细凸分解/非凸几何场景的刚体仿真,轨迹录制开销大幅降低(多数情况 <20%),缓存改进减少重编译并加快资产重载。Breaking:可微仿真支持普通 torch 张量与闭环策略;移除可微仿真用的自定义 Genesis tensor。新特性:运行时连杆间解析螺旋约束。修复:AMDGPU 增量 Hessian 更新、AMD GPU 场景构建与共享内存模型、CUDA 重建场景崩溃、渲染随精度变化、地面纹理闪烁、RDNA4 挂起、休眠连杆 armature 处理、交互 viewer 下 setter 被降速、MPR 失败时才回退 GJK。

(lerobot / openpi / Isaac Lab / GR00T 等重点项目窗口内无新 release。)

---

## 今日趋势 / Today's Trends

1. **运动跟踪的规模化与"先验—接触"接口 / Scaling tracking and prior/contact interfaces.** SuperMimic 的可微世界模型(监测项)、DONIC 的 PPO+BC 回路、Humanoid Mobility via Attention-based Contacts 与 STR/STAMP 都在把人类动作数据当作训练先验或参考来源,而不是直接复制。SuperMimic 有 4 个以上第三方复现仓库在一天内出现,说明社区复现速度极快。 / Several papers use human motion as a prior or reference rather than a target to copy (DONIC, Attention-based Contacts, STR, STAMP), and SuperMimic spawned 4+ third-party reproductions within a day.
2. **世界模型进入控制优化回路 / World models inside the control loop.** DiffDreamer(世界模型 + 可微仿真)、DRILL(为策略效用而非像素训练世界模型)、SuperMimic 都把世界模型当作策略梯度来源。 / DiffDreamer, DRILL and SuperMimic treat the world model as a source of policy gradients rather than a pixel predictor.
3. **WAM 向多模态与自蒸馏扩展 / WAMs gain modalities and self-distillation.** UniFlowWAM(3D 流)、FRED(未来表征自蒸馏)、AW-0(代码+视频+动作)、P³-WAM 四篇同日出现,开源仓库(如 OSWAM、LeWAM)也在增长。 / UniFlowWAM, FRED, AW-0 and P³-WAM landed the same day; WAM repos such as OSWAM and LeWAM are appearing.
4. **VLA 的运行时监控与低延迟 / VLA runtime monitoring and latency.** Echo、Progress Probes、FastHarness 做执行监督,One-Step Euler 研究指出大型流匹配 VLA 单步推理即可。 / Echo, Progress Probes and FastHarness supervise execution, while the Euler study shows one-step inference suffices for large flow-matching VLAs.

---

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
1. `world action model` 的 GitHub 侧 topic:`world-action-model`、`WAM`(GitHub topic/关键词)。radar 今日 new_repos 中 OSWAM、WAM-OPD、LeWAM 等带 WAM 字样的仓库;今日 arXiv 有 UniFlowWAM、FRED、AW-0、P³-WAM 4 篇。 / Several WAM repos and 4 WAM papers appeared today.
2. `humanoid loco-manipulation`(arXiv 检索):今日出现 STR、WholeBodyMem、LocoManiLab、λ₀ 共 4 篇,而现有 `whole-body control` 短语命中为 0。 / Four papers today, while the existing whole-body control phrase returned 0 hits.

**建议观察 / Watch**
- `agentic robotics harness`:AgenticRoboRL、FastHarness、CARE 等 3 篇,及 radar 中 `awesome-agentic-robotics`、`robouse`;信号尚弱,再看几天。 / 3 papers and 2 repos today; signal still weak.

**建议移除/收窄 / Remove or Narrow**
- 今日无建议 / No suggestions today(注:API 多词短语如 `reinforcement learning robot` 命中为 0,可考虑改用 AND 查询而非短语,属检索方式建议 / consider AND queries instead of exact phrases).

---

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 / Added | 当前状态 / Status | 今日检查 / Today's check | 备注 / Notes |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480)(CoRL 2026 Oral,Berkeley) | 2026-10-22 | ❓ 未知 / Unknown(无变化) | radar `signal=false`;candidate_repos 空;项目页 [supermimic.github.io](https://supermimic.github.io) 经 WebFetch 查看:无 GitHub 链接、无开源承诺,仅有论文、视频与浏览器 demo;arXiv 无代码链接;预设 known_repos 匿名 `git ls-remote` 均不可访问;errors 空 | 第三方复现已出现(非官方):zita-ch/supermimic_vibed 250★、CuboiLeo/SuperMimic-Reproduced 88★、Motphys/Uni-SuperMimic 30★ 等,不能据此判为已开源 |

**建议加入监测 / Suggested additions**(状态为未知/计划开源、运动控制优先)

1. **Humanoid Mobility via Attention-based Contacts** — 人形复杂地形 locomotion 的接触接口框架,目前无代码线索。 / Contact-interface humanoid terrain locomotion with no code signal yet.
```json
{"name": "HumanoidContacts", "title": "Humanoid Mobility via Attention-based Contacts", "arxiv_id": "2610.31608", "search_terms": ["Humanoid Mobility via Attention-based Contacts", "attention-based contacts humanoid"], "owners": [], "project_pages": [], "known_repos": []}
```
2. **DiffDreamer** — 世界模型 + 可微仿真的敏捷四旋翼控制,方法新颖,暂无代码。 / Novel world-model + differentiable-sim quadrotor RL, no code yet.
```json
{"name": "DiffDreamer", "title": "DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control", "arxiv_id": "2610.31617", "search_terms": ["DiffDreamer"], "owners": [], "project_pages": [], "known_repos": []}
```
3. **PiHand** — 摘要明确承诺 "We will release the processed data and model checkpoints"(🕒 计划开源),作者来自 MPI(Pons-Moll 组),值得追踪何时放出。 / Abstract promises data and checkpoints.
```json
{"name": "PiHand", "title": "PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning", "arxiv_id": "2610.31299", "search_terms": ["PiHand"], "owners": [], "project_pages": ["https://virtualhumans.mpi-inf.mpg.de/PiHand/"], "known_repos": []}
```

**建议移出 / Suggested removals:** 无 / None.

---

## 交付前自检 / Pre-delivery Checklist

① 类别 1–2 条目已全部展开(11 + 7);类别 2 另有 4 条弱相关仅列名,已说明。 ② 无"未读/仅标题"占位;未给出的数值均写"摘要未给出"。 ③ 每个展开条目均有开源状态行。 ④ 错归自查:优先级 3–7 类别中,DRILL(VLA RL 后训练世界模型,操作策略)、P³-WAM/DeXplicit(操作世界模型)、Echo/FocusVLA 等不涉及 locomotion/全身控制,保留;WholeBodyMem、LocoManiLab、λ₀、TRACE(G1 动作)已移入运动控制·RL;TRACE(traversability,NMPC)、ProTrav(MPPI)已移入运动控制·传统。 ⑤ arXiv API 检索已运行并记录各词命中数。 ⑥ release 条目已写主要更新(MuJoCo 受 radar 截断限制,已注明)。
