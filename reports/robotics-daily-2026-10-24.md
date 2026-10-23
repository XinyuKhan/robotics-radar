# 机器人/具身智能每日速递 — 2026-10-24 / Robotics & Embodied AI Daily — 2026-10-24

**检查窗口 / Window:** 台北时间 2026-10-23 ~07:40 → 2026-10-24 ~07:40(arXiv 取 2026-10-23(周五)cs.RO 公告列表,对应提交日约 10-21~10-22 UTC;GitHub 取 radar 数据 `date_taipei=2026-10-24`,生成于 2026-10-24 07:19 台北时间)。 / Taipei time, arXiv announce list of Fri 23 Oct 2026 (submissions ≈ 21–22 Oct UTC); GitHub from the radar snapshot dated 2026-10-24.

**来源状态 / Source status**
- arXiv cs.RO `new` 列表:共 106 条可解析(New 63 + Cross-lists 6 + Replacements 37;列表头标注 63 / 6 / 38)。逐条分类后连同关键词检索与 HF/radar 补充,共入选约 85 篇,其中详细展开 67 篇;入选论文均已用 arXiv API `id_list` 取得完整摘要(0 篇失败)。 / ~85 papers selected incl. keyword search and HF/radar additions, 67 expanded; all abstracts fetched in full via the API (0 failures).
- arXiv API 关键词检索(cs.RO/cs.AI/cs.LG/cs.CV,按 submittedDate 降序,保留 updated ≥ 2026-10-22 00:00 UTC)命中数 / hits: embodied 12, VLA 12, vision-language-action 11, VLN 1, vision-language navigation 1, humanoid 5, legged locomotion 0, whole-body control 0, MPC 0, reinforcement learning robot 0, sim-to-real 1, dexterous manipulation 3, robot foundation model 1, world model 11, world action model 4, WAM 3, video world model 2, spatial intelligence 1, spatial reasoning 2, SLAM 2, visual SLAM 1, LiDAR SLAM 0, gaussian splatting SLAM 0, 3D reconstruction 2, motion tracking 3, motion imitation 0。合并去重后共 50 条,其中 21 条不在 cs.RO 列表内(多为 cs.CV/cs.AI 的世界模型、VLA、VLN、重建工作),相关者已并入。 / 50 unique after merge, 21 of them not on the cs.RO list.
- GitHub radar `data/latest.json`:已更新(date_taipei=2026-10-24);new_repos 150 条(counts 报 277 条新建),star_growth_top 有基准(2026-10-22 23:20 UTC),watchlist_releases 2 条,oss_watch 1 项(signal=false,无错误)。 / Radar data fresh.
- Hugging Face Daily Papers:获取成功(100 篇,其中带 githubRepo 者经筛选后相关项已并入)。 / HF Daily Papers OK.
- 备注 / Note:`MPC`、`legged locomotion` 等短语检索窗口内 0 命中(API 全文短语匹配较严),类别 1–2 主要依赖 cs.RO 列表与 radar 发现。

---

## 今日必读 / Top Picks

1. **[NEXUS: Perceptive Whole-Body Control for Terrain-Adaptive Teleoperation](https://arxiv.org/abs/2609.39000)** — 运动控制·RL。✅ 已开源(代码 + G1 ONNX 权重)。 / 当日新开源的人形感知全身控制,约 1000 小时配对地形动作 + 教师-学生训练,零样本真机遥操作;仓库今天刚上线。 / Freshly released perceptive humanoid WBC with ~1000 h of terrain-paired motions and zero-shot real-robot teleop; repo went live this week.
2. **[Humanoid Mobility via Attention-based Contacts](https://arxiv.org/abs/2610.31608)** — 运动控制·RL。❓ 未知。 / 把接触作为感知与控制之间的接口,动作数据只作先验,部署时无需参考输入。 / Contact as the interface between perception and control; motion data used only as a training prior, no references at deployment.
3. **[DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations](https://arxiv.org/abs/2610.29997)** — 运动控制·RL。✅ 部分开源(BiHOI 处理管线;训练代码/权重/数据 coming soon)。 / 首个通用双手灵巧跟踪器,单一检查点在未见轨迹上成功率 86.79%。 / First generalist bimanual dexterous tracker; one checkpoint reaches 86.79% on unseen trajectories.
4. **[WholeBodyMem(Memory before Goal)](https://arxiv.org/abs/2610.31166)** — 运动控制·RL(人形全身 VLA 策略,交叉 VLA)。❓ 未知。 / 真机 Unitree G1 成功率 36.7%→88.3%,说明记忆对人形移动操作至关重要。 / Real G1 success 36.7%→88.3%; memory matters for humanoid loco-manipulation.
5. **[UniFlowWAM](https://arxiv.org/abs/2610.30991)** — 世界模型与 WAM。🕒 计划开源(项目页 Code coming soon)。 / 把 3D scene flow 作为与视觉、动作并列的第三模态,真机平均成功率 87.0% vs 最强基线 68.5%。 / Makes 3D scene flow a third modality beside vision and action; 87.0% real-robot success vs 68.5%.

---

## 运动控制·RL / Motion Control · RL

*本类共 18 条,全部展开。 / 18 items, all expanded.*

### [NEXUS: Perceptive Whole-Body Control for Terrain-Adaptive Teleoperation](https://arxiv.org/abs/2609.39000)(Gamma-Robot;arXiv 2026-09-30,GitHub 仓库 2026-10-23 新建,3★)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(遥操作 / teleoperation)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Gamma-Robot/NEXUS);含地形动作适配代码、PPO 与蒸馏训练管线、Unitree G1 感知行为基础模型 ONNX 权重和少量示例动作;人机重定向需自备,sim-to-sim/sim-to-real 部署代码未见(`git ls-remote` 验证仓库存在)
- 🇨🇳 全身遥操作要求人形机器人在操作者与机器人地形不一致时仍能感知局部地形并调整姿态与接触,而跨地形的配对动作数据极其稀缺。NEXUS 先设计可扩展的地形感知动作适配算法,无需逐动作/逐地形调参地生成平地与不同地形的配对动作;再用总计近 1000 小时的配对语料,通过教师-学生学习训练融合人类动作指令与机载感知的全身控制器。实验显示数据生成高效、可扩展,并在评测基准上行为覆盖、地形适应性与跟踪精度均优于现有全身控制器,零样本真机部署实现了未见地形上的实时全身遥操作。
- 🇬🇧 Whole-body teleoperation needs a humanoid to adapt posture and contacts to its own terrain rather than copy the operator, but paired flat/rough-terrain motion data are scarce. NEXUS introduces a scalable terrain-aware motion adaptation algorithm that generates such pairs without per-motion or per-terrain tuning, then trains a perceptive whole-body controller by teacher–student learning on a ~1,000-hour paired corpus. It outperforms existing whole-body controllers on the evaluated benchmarks in behavior coverage, terrain adaptability and tracking fidelity, and deploys zero-shot on real unseen terrains for real-time teleoperation.

### [Humanoid Mobility via Attention-based Contacts](https://arxiv.org/abs/2610.31608)(机构未在摘要给出;Comments: under review)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接或承诺
- 🇨🇳 复杂地形上的人形移动需要精确落脚和协调的全身动作:无参考 RL 泛化好但难以靠奖励设计得到自然的全身协调,基于参考的方法动作自然却难以适应轨迹之外的环境。本文把动作数据严格用作训练先验,用自监督的注意力接触规划器预测未来身体-环境接触,再由接触条件跟踪器把规划转成协调的全身动作,使"接触"成为感知与控制的接口。随后的微调阶段利用已习得能力探索原动作数据未覆盖的环境变化;部署时完全依赖机载观测、无需参考输入。摘要未给出定量结果。
- 🇬🇧 RL without references generalizes across terrain but struggles to elicit whole-body coordination, while reference-based methods look natural but cannot adapt beyond their data. The paper uses motion data strictly as a prior: a self-supervised attention-based contact planner predicts future body–environment contacts and a contact-conditioned tracker turns them into coordinated whole-body motion, so contact becomes the interface between perception and control. A fine-tuning stage then explores environment variations beyond the motion data, and deployment uses only onboard observations with no reference inputs. The abstract reports no quantitative results.

### [DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations](https://arxiv.org/abs/2610.29997)(Ropedia;arXiv 2026-10-21,HF Daily 149 upvotes)
开源状态 / Code: ✅ 部分开源 / Partially released — [仓库](https://github.com/Ropedia/DONIC);目前只有 BiHOI 多视角处理管线,`donic/` 训练与评测代码、策略检查点、BiHOI 数据集均标注 coming soon(WebFetch 核对 README)
- 🇨🇳 现有灵巧参考跟踪多针对单手,而接触丰富的双手操作数据稀缺、接触协调更复杂。DONIC 是首个跨操作类别与人类动作来源联合训练的通用双手跟踪器,并配套 BiHOI 数据集(1,575 条序列、229 个物体)。方法把 PPO 与行为克隆放入反馈回路,将验证成功的执行回收为训练示范;以物体为中心的逐手奖励按各手的参考接触角色监督,Clip-Centered Advantages 去除依赖参考的优势偏置。不微调时,单个检查点在训练物体的未见轨迹上成功率 86.79%,在留出物体上 57.32%,分别比最先进双手跟踪基线高 77.36 与 45.73 个百分点。
- 🇬🇧 Existing dexterous reference tracking mostly targets single hands, and contact-rich bimanual data are scarce. DONIC is the first generalist bimanual tracker trained jointly across operation categories and human-motion sources, with the BiHOI dataset (1,575 sequences, 229 objects). It couples PPO with behavioral cloning in a loop that recycles verified successes as demonstrations, uses an object-centered per-hand reward by contact role, and Clip-Centered Advantages to remove reference-dependent offsets. Without finetuning, one checkpoint reaches 86.79% on unseen trajectories of training objects and 57.32% on held-out objects, beating bimanual tracking baselines by 77.36 and 45.73 points.

### [Robot Motion Transition with Human Motion Prior (STAMP)](https://arxiv.org/abs/2610.30817)(Comments: 9 pages, 4 figures)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://childtoy.github.io/STAMP-project)有 "Code" 标签但无链接、无发布承诺
- 🇨🇳 人形动作跟踪策略能复现多样行为,但把独立获得的动作连接成连续序列仍困难:插值不考虑边界的相对位置、朝向与时序,生成式先验又可能产生多余的行走或转向。STAMP 通过"机器人→人→机器人"流程:把两段动作重定向到人体骨架,由学习到的对齐模型对候选位置、朝向与过渡时长排序,再用人体动作先验生成过渡,最后重定向回机器人并训练动作跟踪策略。在 Unitree G1 与 ROBOTIS K1 上评估了过渡的跟踪成功率,并在真机上演示把独立动作连成长时序序列;摘要未给出具体数值。
- 🇬🇧 Humanoid tracking policies reproduce diverse behaviors, but chaining independently acquired motions is hard: interpolation ignores boundary conditions and generative priors may add unintended locomotion. STAMP uses a Robot-to-Human-to-Robot process: motions are retargeted to a human rig, a learned alignment model ranks candidate positions, headings and durations, a human motion prior generates the transition, and the result is retargeted to train a tracking policy. It is evaluated by tracking success on Unitree G1 and ROBOTIS K1 and demonstrated on hardware for long-horizon sequences; the abstract gives no numeric results.

### [MPBRS: Multi-Potential-Based Reward Shaping for Unified Reward Configuration in Humanoid Locomotion](https://arxiv.org/abs/2610.30334)
开源状态 / Code: ❓ 未知 / Unknown — 摘要无代码链接,Comments 为空
- 🇨🇳 人形 locomotion 的 RL 流水线中,奖励设计与调参是主要难点:朴素塑形项常与目标行为冲突、过拟合特定机器人,或对权重微小变化不稳定。本文研究 Multi-PBRS(基于势函数差分的多势塑形,不改变最优策略),并提出统一奖励配置。同一套奖励结构与权重在九种人形机器人上评估,只需提供机器人元数据(关节/连杆映射与默认姿态)。结果显示相比标准塑形,MPBRS 的缩放行为更一致、调参敏感性更低;摘要未给出具体数值。
- 🇬🇧 Reward design and tuning is a main bottleneck in humanoid-locomotion RL: naive shaping terms conflict with desired behavior, overfit to a robot, or are unstable under small weight changes. The paper studies Multi-PBRS, potential-based shaping that leaves the optimal policy unchanged, and proposes a unified reward configuration evaluated with identical structure and weights across nine humanoid robots, needing only robot metadata (joint/link mappings, default poses). Compared with standard shaping it shows more consistent scaling and lower tuning sensitivity; no numeric results are given in the abstract.

### [Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation (STR / STRL)](https://arxiv.org/abs/2610.30540)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码信息
- 🇨🇳 人类动作重定向为全身控制和移动操作提供参考,但对物体交互任务,关键阶段的身体-物体关系必须精确,而逐帧均匀的迭代预算效率低。STR 让视觉语言模型选择相关运动信号和身体部位、据变化识别关键帧,对关键帧分配更多求解迭代并提高选定部位的交互权重;MCA 用近似物体 wrench 模型修正物体表面接触位置;STRL 结合自适应关键阶段采样与基于目标接近度和物体接触力的接触奖励进行下游 RL 控制。Unitree G1 仿真与 Unitree R1 真机实验表明 STR 以更低计算成本提升几何接触覆盖与连续性,所得参考提升了多种物体交互动作的下游任务完成率(摘要未给出具体数值)。
- 🇬🇧 Retargeting supplies references for humanoid loco-manipulation, but object interaction needs accurate body–object relations at critical stages and uniform per-frame iteration budgets are wasteful. STR has a VLM pick relevant signals and body parts, finds keyframes, allocates extra solver iterations and higher interaction weights there; Mechanics-Aware Contact Anchoring refines contact positions with an approximate wrench model; STRL adds adaptive key-stage sampling and a contact reward on proximity and contact force for downstream RL. Simulation on Unitree G1 and real tests on Unitree R1 show better contact coverage and continuity at lower compute and improved downstream task completion; no numbers are in the abstract.

### [ReactiveBFM: Reactive Closed-Loop Motion Planning Towards Universal Humanoid Whole-Body Control](https://arxiv.org/abs/2606.30362)(Replacement;Comments: Accepted by CoRL 2026)
🏷️ 交叉方向 / Also: 具身智能与机器人基础模型(行为基础模型 / BFM)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/zjwzcx/ReactiveBFM);由[项目页](https://xiao-chen.tech/reactivebfm/)的 Code 链接给出,匿名 `git ls-remote` 验证存在
- 🇨🇳 行为基础模型(BFM)只执行预定义参考动作,难以应对环境变化;直接级联生成式规划器则因跟踪偏差积累产生曝光偏差。ReactiveBFM 提出实时闭环规划-控制框架:用计划前缀采样课程让生成式规划器从不完美物理状态学习纠错,用异步重规划与轨迹分块的时间集成化解自回归规划与高频跟踪的延迟失配。在 Unitree G1 上实现文本条件闭环动作和零样本移动目标触达;在严重扰动的 sim-to-sim 基准中成功率 93.1%,比级联开环基线高 28.6%。
- 🇬🇧 Behavior foundation models only execute pre-defined references and are brittle to environment shifts; naively cascading them with generative planners suffers cumulative exposure bias. ReactiveBFM is a real-time closed-loop planning–control framework using a scheduled prefix-sampling curriculum so the planner learns error recovery from imperfect states, plus asynchronous replanning and trajectory chunking with temporal ensembling to reconcile latency mismatch. On a Unitree G1 it performs text-conditioned closed-loop motions and zero-shot moving-target reaching, and reaches 93.1% success in severely perturbed sim-to-sim tests, 28.6% above cascaded open-loop baselines.

### [Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation (ALMA)](https://arxiv.org/abs/2610.30810)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 空中移动操作中,机械臂运动与环境交互会不断改变质心、惯量并带来力/力矩扰动;控制奖励没有直接目标来约束从历史中保留的响应信息,固定任务采样也会遗漏持续的跟踪难点。ALMA 使用从近期测量与动作中自适应的上下文飞行策略,借助动作条件的未来测量表征预测来训练上下文;并用进化过程让 LLM 分析观察到的控制困难,提出新的机械臂运动结构用于后续训练。仿真中位置 RMSE 比最强基线最多降低 24.7%;同一策略零样本迁移到真机空中机械臂,周期性臂运动下悬停位置 RMSE 比真机基线降低 79.6%。
- 🇬🇧 In aerial loco-manipulation, arm motion and contact shift the center of mass and inertia and inject disturbances; control rewards give no direct target for response information kept from history, and fixed task sampling leaves tracking difficulties unexplored. ALMA uses a contextual flight policy adapting from recent measurements and actions, trained with action-conditioned prediction of future measurement representations, and an evolutionary loop where an LLM analyzes control difficulties and proposes new arm-motion structures. In simulation it cuts position RMSE by up to 24.7% versus the strongest baseline, and the policy transfers zero-shot to a real aerial manipulator, reducing hover position RMSE by 79.6% under periodic arm motion.

### [DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control](https://arxiv.org/abs/2610.31617)
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 四旋翼动态过门竞速既要预测外部运动又要精确高频控制;基于世界模型的 RL 常把环境演化与机器人自身动力学纠缠在同一个学习到的 rollout 中,模型偏差会拖累策略优化。DiffDreamer 在一个优化步内让学习的世界模型传播捕获外部动态与历史特征的隐状态,让可微模拟器传播机器人显式物理状态,并把 actor 目标拆为处理不可微任务奖励的 critic 通路和处理可微运动奖励的模拟器通路。在激进跟踪与动态过门任务上,训练收敛优于无模型、基于模型和可微 RL 基线,最终性能还优于上述基线及经典规划与控制方法,并给出概念验证级真机飞行(摘要未给出具体数值)。
- 🇬🇧 Dynamic-gate racing needs anticipating external motion and precise high-frequency control, yet world-model RL entangles environment evolution and robot dynamics in one learned rollout, so model bias hurts policy optimization. DiffDreamer propagates latent states with a learned world model for external dynamics and a differentiable simulator for the robot's physical state in one step, and splits the actor objective into a critic-driven path for non-differentiable rewards and a simulator-driven path for differentiable motion rewards. It improves convergence over model-free, model-based and differentiable-RL baselines and final performance over those and classical planning/control, with proof-of-concept real flights; no numbers in the abstract.

### [PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning](https://arxiv.org/abs/2610.31299)(MPI-INF Virtual Humans)
开源状态 / Code: 🕒 计划开源 / Planned — 摘要写 "We will release the processed data and model checkpoints";[项目页](https://virtualhumans.mpi-inf.mpg.de/PiHand/)无代码链接
- 🇨🇳 合成物理上合理的灵巧手-物体交互需同时满足接触动力学、物体几何和目标轨迹;现有方法要么跟踪 mocap 但难迁移到新物体,要么依赖仅手部的生成先验而丢失接触保真。PiHand 先在仿真中训练跟踪 mocap 的专家策略,用目标条件 VAE 蒸馏为统一的手-物体交互先验,再通过隐空间中的有界残差探索求解多样灵巧操作,仅需单一奖励且无需复杂课程。在 GRAB 与 DexYCB 上泛化到未见物体与轨迹,并迁移到接球与双手交接;摘要称在所有任务和指标上持续优于基线(未给出具体数值)。
- 🇬🇧 Physically grounded dexterous hand–object synthesis must respect contact dynamics, object geometry and target trajectories; mocap tracking transfers poorly to new objects and hand-only priors lose contact fidelity. PiHand trains expert policies tracking mocap in simulation, distills them into a goal-conditioned VAE interaction prior, then solves tasks by bounded residual exploration in latent space with a single reward and no complex curriculum. It generalizes to unseen objects and trajectories on GRAB and DexYCB and transfers to catching and bimanual handover, consistently outperforming baselines on all metrics (no numbers in the abstract).

### [LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.30876)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(基准测试平台;因涉及人形移动操作控制器与部署,依规则归入运动控制 / benchmark paper kept here because it covers humanoid loco-manipulation controllers and deployment)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无链接
- 🇨🇳 人形机器人移动操作的进展难以横向比较。LocoManiLab 提供覆盖数据采集/生成、策略训练、评测与真机部署的测试平台,任务集含 234 个原子/组合任务、5 类家居场景,以及 51.5 小时仿真遥操作数据。评测涵盖 12 种策略(共享控制器)、2 种策略 × 5 种控制器,以及示范规模与数据来源混合研究。结果:未见任务/场景上成功率下降、视觉扰动加大时普遍下降;三项仿真任务与真机设置匹配,策略排名相近,支持基于仿真评估的可靠性。
- 🇬🇧 Progress in humanoid loco-manipulation is hard to compare. LocoManiLab is an integrated testbed spanning data generation, policy training, evaluation and deployment, with 234 atomic/compositional tasks over five household scene categories and 51.5 hours of simulated teleoperation. It evaluates twelve policies with a shared controller, two policies across five controllers, and demonstration-scale/data-mix studies. Success falls on unseen tasks/scenes and under stronger visual perturbations, and three simulated tasks matched to real setups show similar policy rankings, supporting simulation-based evaluation.

### [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation (WholeBodyMem)](https://arxiv.org/abs/2610.31166)(Comments: submitted to RA-L)
🏷️ 交叉方向 / Also: VLA, 具身智能 / Embodied AI(归入运动控制:目标任务是人形全身移动操作策略)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://memory-before-goal.github.io)无代码链接,也无发布承诺(WebFetch 核对)
- 🇨🇳 动态场景下人形移动操作是非马尔可夫的:线索会因物体变化、遮挡或转身离开视野而消失,而全身 VLA 策略只看当前。WholeBodyMem 是以物体为引导的感知记忆:SAM3 跟踪任务物体,物体事件因果地在自适应预算内选出关键帧,动作专家通过交叉注意力读取这些帧及编码外观、几何与时间的物体 token。同时提出 HuMeGo 基准(6 个仿真 + 6 个真机 Unitree G1 任务)。基础策略成功率在仿真中从 29.1% 升至 72.6%、真机从 36.7% 升至 88.3%,标准 SIMPLE 任务从 70.2% 升至 86.9%。
- 🇬🇧 Humanoid loco-manipulation in dynamic scenes is non-Markovian, yet whole-body VLA policies see only the present. WholeBodyMem keeps an object-guided perceptual memory: SAM3 tracks task objects, object events causally select key frames under an adaptive budget, and the action expert reads them by cross-attention together with object tokens encoding appearance, geometry and time. With the new HuMeGo benchmark (6 simulated and 6 real Unitree G1 tasks), it raises the base policy's success from 29.1% to 72.6% in simulation and 36.7% to 88.3% on the real robot, and from 70.2% to 86.9% on SIMPLE tasks.

### [HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation](https://arxiv.org/abs/2604.07993)(Replacement,首次提交 2026-04-09;摘要给出的是原有结果,本次更新内容未知)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Open-X-Humanoid/HEX);[项目页](https://hex-humanoid.github.io/)的 Code 链接给出,匿名 `git ls-remote` 验证存在
- 🇨🇳 多数 VLA 把机器人身体部位近似独立处理,使高自由度人形控制不稳定。HEX 提出以状态为中心的全尺寸双足人形协调操作框架:人形对齐的通用状态表示用于跨异构本体学习,MoE 统一本体感觉预测器建模全身协调与时序动态,轻量历史 token 汇总过去观测,残差门控融合加 flow-matching 动作头自适应整合视觉语言与本体动力学。真机人形操作实验显示 HEX 在任务成功率与泛化上达到最优,尤其在快速反应与长时序场景;摘要未给出具体数值。
- 🇬🇧 Most VLAs treat body parts largely independently, making high-DoF humanoid control unstable. HEX is a state-centric framework for full-size bipedal humanoids with a humanoid-aligned universal state representation, a Mixture-of-Experts proprioceptive predictor for whole-body coordination, lightweight history tokens, and residual-gated fusion with a flow-matching action head. Real-world humanoid manipulation experiments show state-of-the-art success and generalization, especially in fast-reaction and long-horizon scenarios; no numbers in the abstract.

### [What Does It Take For A Generalist Robot Policy To Adapt Using Minimal Data? (MiDAS)](https://arxiv.org/abs/2608.11363)(Replacement,首次提交 2026-08-11)
🏷️ 交叉方向 / Also: VLA, 具身智能与机器人基础模型
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码信息
- 🇨🇳 完全自主学习受稀疏奖励和零样本探索弱的限制。本文提出"最小数据适应"设定:预训练策略仅凭一条示范加自主在线交互学习新任务,并总结三条设计原则:预训练 VLA 表征支持样本高效的价值学习、残差策略学习足以学到纠正行为、需要谨慎的数据平衡以防探索崩溃。据此提出 MiDAS:少量示范行为克隆 + 冻结 VLA 表征上基于价值的残差学习。在 LIBERO 与 RoboCasa 上显著提升单示范初始化策略;在双臂 YAM 平台上,从脆弱初始策略出发,约 6 小时在线交互后成功率提升(摘要未给出具体数值)。
- 🇬🇧 Autonomous learning is limited by sparse rewards and weak zero-shot exploration. The paper defines a minimal-data adaptation regime (one demonstration plus autonomous online interaction) and identifies three principles: pretrained VLA representations support sample-efficient value learning, residual policy learning suffices for corrections, and careful data balancing prevents exploration collapse. MiDAS combines few-demo behavior cloning with value-based residual RL over frozen VLA features, substantially improving single-demo initializations on LIBERO and RoboCasa and improving success on a bimanual YAM after ~6 hours of online interaction; no numbers in the abstract.

### [Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models (RL-Co)](https://arxiv.org/abs/2602.12628)(Replacement,首次提交 2026-02-13)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码信息
- 🇨🇳 现有仿真-真机联合训练多基于 SFT,把仿真当静态示范源,未利用大规模闭环交互,真机增益有限。RL-Co 采用两阶段:先用真实与仿真示范混合做 SFT 热启动,再在仿真中做 RL 微调,并对真实数据加辅助监督损失以锚定策略、缓解灾难性遗忘。在 4 个真机桌面操作任务、OpenVLA 与 π0.5 两种架构上,相比仅真机微调与基于 SFT 的联合训练取得一致提升,真机成功率 OpenVLA +24%、π0.5 +20%,并带来更好的泛化与真机数据效率。
- 🇬🇧 Most sim–real co-training uses SFT and treats simulation as static demonstrations, ignoring closed-loop interaction. RL-Co warm-starts with SFT on mixed real and simulated demonstrations, then fine-tunes with RL in simulation while an auxiliary supervised loss on real data anchors the policy against forgetting. On four real tabletop tasks with OpenVLA and π0.5 it consistently beats real-only fine-tuning and SFT co-training, with +24% real success on OpenVLA and +20% on π0.5, plus better generalization and data efficiency.

### [DRILL: Training World Models to Improve Policies, Not Predict Pixels](https://arxiv.org/abs/2610.30814)(Comments: NeurIPS 2026)
🏷️ 交叉方向 / Also: 世界模型 / World Model, VLA(归入运动控制:贡献在于 VLA 策略的 RL 后训练)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接
- 🇨🇳 用世界模型减少 VLA 策略 RL 后训练的交互时,世界模型通常按单步像素预测训练,但其作用是为想象 rollout 提供能改进策略的学习信号;像素 MSE 更低反而可能产生更差的策略梯度。DRILL 是双层框架,更新世界模型以最大化策略在想象 rollout 上经 GRPO 内层更新后的回报,有闭式代理 DRILL-VWI 与元梯度全量方法 DRILL-IMG(截断 Hessian-向量积)。世界模型为策略效用训练时,即便下一帧像素 MSE 高 17%,下游策略仍更好;在 5 个操作仿真器、2 种 VLA 骨干上,DRILL-IMG 平均成功率比 WMPO 高 13.1 个点、比 RLVR-World 高 7.9 个点。
- 🇬🇧 World models used to cut interaction when RL-post-training VLAs are usually trained for one-step pixel prediction, yet their job is to give learning signals from imagined rollouts; lower pixel MSE can yield worse policy gradients. DRILL is a bilevel framework that updates the world model to maximize policy return after an inner GRPO update on imagined rollouts, with a closed-form surrogate (DRILL-VWI) and a full meta-gradient method (DRILL-IMG, truncated Hessian-vector products). A world model trained for policy utility yields better policies despite 17% higher next-frame pixel MSE, and across five manipulation simulators and two VLA backbones DRILL-IMG raises mean success by 13.1 points over WMPO and 7.9 over RLVR-World.

### [RangeNav: Task-Aligned LiDAR Range-Image Pretraining for Robot Navigation](https://arxiv.org/abs/2610.29845)(Replacement,仅补充项目页与作者单位)
🏷️ 交叉方向 / Also: 空间智能与 SLAM(感知表征)
开源状态 / Code: 🕒 计划开源 / Planned — 摘要 "Code and models will be open-sourced";[项目页](https://rangenav.github.io/)写 "Code & models coming soon",无链接
- 🇨🇳 密集人群与杂乱场地中的移动机器人需要 360° 感知,但 RL 中学习表征在稀疏奖励下样本效率低,现有 3D 预训练点云编码器对大规模并行 RL 仿真太占内存。RangeNav 是仅在合成数据上预训练的紧凑(183k 参数)LiDAR 距离图像编码器,用各向异性卷积和环向填充处理极端长宽比与方位角接缝,以距离重建、语义分割和 BEV 预测的导航对齐目标预训练后冻结用于策略学习。仿真中加入语义和 BEV 监督使成功率比仅重建基线平均提升 32.03(训练分布)和 23.73(分布外)个百分点;在 Unitree B2-W 四足上零样本真机部署,能在密集人群、低光和施工区稳健导航。
- 🇬🇧 Mobile robots in dense crowds need 360° perception, but learning representations inside RL is sample-inefficient and existing 3D encoders are too heavy for massively parallel simulation. RangeNav is a compact (183k-parameter) LiDAR range-image encoder pretrained on synthetic data with anisotropic convolutions and circular padding, using a navigation-aligned objective of range reconstruction, semantic segmentation and BEV prediction, then frozen for policy learning. Semantic and BEV supervision raise success over a reconstruction-only baseline by 32.03 and 23.73 points on average (training / out-of-distribution environments), and zero-shot deployment on a Unitree B2-W quadruped navigates dense crowds, low light and construction zones.

### [Revisiting Distribution Matching for State-to-Vision Policy Distillation in Laparoscopic Robotic Manipulation](https://arxiv.org/abs/2610.31010)(Comments: 8 pages)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 腹腔镜手术中基于特权状态的 RL 策略难以获得可靠状态,纯视觉 RL 难训练,模仿学习又需要大量难获取的专家示范。本文提出状态到视觉的策略蒸馏:特权状态策略作教师,视觉策略基于 RGB 与本体感觉学习,所需示范少于 IL,性能优于 RL。仿真多种手术操作任务显示,通用 RL 方法训练视觉策略很困难,而该蒸馏方案使各任务表现更一致、更稳定;摘要未给出具体数值。
- 🇬🇧 In laparoscopic manipulation, privileged-state RL policies need states that are hard to obtain, pure vision RL is hard to train, and imitation learning needs scarce expert demos. The paper distills a privileged state-based teacher into a vision policy using RGB and proprioception, needing fewer demonstrations than IL and performing better than RL. In simulated surgical tasks, general-purpose RL struggles on vision inputs while distillation gives more consistent and stable performance; no numbers in the abstract.

---

## 运动控制·传统 / Motion Control · Classical

*本类共 7 条,全部展开。 / 7 items, all expanded.*

### [Whole-Body Motion Guided Reference Generation for Uncertainty-Aware Compliant Assistance](https://arxiv.org/abs/2610.31302)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 外骨骼辅助需应对人体运动模式与交互需求的巨大差异。本文提出双环辅助策略:外环用去噪生成器以全身人体运动、外骨骼本体感觉(任务描述为辅助语义)合成未来轨迹(三阶段训练),内环采样多条未来轨迹估计均值与方差,均值作控制参考,方差作可靠性度量并进入刚度调节律,实现可变导纳控制,并在有界交互输入下证明输入-状态稳定。实验显示相比标准基线显著降低肌肉激活水平,并相对无辅助降低使用者代谢能耗(摘要未给出具体数值)。
- 🇬🇧 Exoskeleton assistance must cope with large variation in human motion and interaction. A dual-loop strategy couples a denoising trajectory generator (whole-body human motion plus exoskeleton proprioception, task text as auxiliary cue, three-stage training) with variable admittance control: the inner loop samples future trajectories, uses their mean as reference and variance as an uncertainty measure in a stiffness law, with input-to-state stability under bounded interaction input. Experiments show markedly lower muscle activation than baselines and lower metabolic expenditure than unassisted walking; no numbers in the abstract.

### [Real-Time Disturbance-Aware Koopman Model Predictive Control for Quadrotors in Spatially Varying Winds](https://arxiv.org/abs/2610.27414)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 四旋翼在扰动环境中需要随气动效应变化而保持准确的预测模型。DA-KCF 保留离线辨识的名义 Koopman 模型,部署时只在线学习由扰动引起的修正:由仿真数据学习参考相关的 KCF 并用少量硬件数据校准,在线用轻量残差集成从状态-指令-状态转移学习低维扰动修正,并沿预测时域嵌入 MPC 以优化发给机载稳定控制器的位置与偏航参考。纳米四旋翼在均匀风与空间变化尾流中的硬件实验表明,模型失配增大时在线适应改善多步预测与轨迹跟踪,同时满足实时性。
- 🇬🇧 Quadrotors in disturbed air need models that stay accurate as aerodynamics change. DA-KCF keeps an offline-identified nominal Koopman model and learns only a disturbance correction online with a lightweight residual ensemble from state–command–state transitions, evaluated along the MPC horizon to optimize position/yaw references for the onboard stabilizer. Hardware tests on a nano-quadrotor in uniform wind and a spatially varying wake show online adaptation improves multi-step prediction and tracking as mismatch grows, within real-time limits.

### [Prior Evolution and Task Alignment for Aerial Grasping](https://arxiv.org/abs/2609.18153)(Replacement,首次提交 2026-09-16;Comments: 20 pages)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 空中抓取的轨迹优化高度非凸、对初始化敏感,且人为设计的数值目标未必反映抓取成败。本文在解析规划器内引入学习:先从优化轨迹学得轨迹先验,再用基于 CEM 的过程以实际优化器评估采样初始值并保留好的作为新监督;执行感知评论家从接触、抬升与完成结果学习判断轨迹能否成功,其冻结能量还可作为可微抓取代价。仿真与真机实验显示优化可靠性、轨迹一致性与抓取性能均有提升(摘要未给出具体数值)。
- 🇬🇧 Trajectory optimization for aerial grasping is highly nonconvex, initialization-sensitive, and its hand-designed objectives may not capture what makes grasps succeed. The paper learns a trajectory prior from optimized motions and evolves it via CEM using the deployed optimizer, while an Execution-Aware Critic learns from contact, lift and completion outcomes and its frozen energy serves as a differentiable grasping cost. Simulation and real experiments show better optimization reliability, trajectory consistency and grasping performance; no numbers in the abstract.

### [Dual-Arm Box Manipulation via Online Inertial Estimation and Convex Wrench Optimization](https://arxiv.org/abs/2605.22021)(Replacement,首次提交 2026-05-21)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 双臂搬运质量与质心未知的物体时,接触 wrench 调节不当会导致滑移、掉落或过度挤压。本文把在线惯性估计(由测得接触 wrench 估计质量与质心)与凸接触 wrench 优化结合:在椭球摩擦极限面约束下用二阶锥规划(SOCP)计算满足摩擦可行性的接触力与扭转力矩,并含离线轨迹精修以减少物体-环境接触。真实双臂系统在不同质心配置下的实验表明可稳定抬起未知惯性的物体并保持稳定摩擦接触。
- 🇬🇧 Dual-arm lifting of objects with unknown mass/CoM risks slip, drop or over-squeezing. The framework estimates mass and center of mass online from measured contact wrenches and solves a second-order cone program for friction-feasible contact forces and torsional moments under ellipsoidal limit-surface constraints, with offline trajectory refinement. Real dual-arm experiments across CoM configurations show stable lifting with maintained frictional contact.

### [Tilt-Rotor Quadcopter with Learned Residual Control and Mode-Dependent State Estimation](https://arxiv.org/abs/2610.31051)(Comments: 5 figures)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 倾转旋翼四旋翼可在不倾斜机身时平移,但使建模、状态估计和抗扰复杂化。本文给出 2.00 kg 倾转旋翼的仿真飞行栈:6 自由度非线性模型、级联 PD 控制、跨悬停/过渡模式的 14 状态 EKF(施密特触发分类器防协方差跳变),并在 PD 之上加入由有特权风信息的教师行为克隆得到的有界神经残差(部署时网络不观测风)。EKF 稳定后水平位置 RMSE 0.226 m、垂直 0.03 m、姿态 RMSE 小于 0.8°,风速估计误差每轴在 0.15 m/s 内;残差使风下定点误差约降低 49%(1.5 m/s 时 0.117→0.060 m,分布外 3.9 m/s 时 0.319→0.162 m)。
- 🇬🇧 Tilt-rotor quadcopters translate without banking but complicate modeling, estimation and disturbance rejection. The paper presents a simulated flight stack for a 2.00 kg vehicle with a 6-DoF model, cascaded PD control, a 14-state EKF across hover/transition modes with a Schmitt-trigger classifier, and a small bounded neural residual cloned from a wind-privileged teacher. The EKF reaches 0.226 m horizontal / 0.03 m vertical RMSE, <0.8° attitude RMSE and wind estimates within 0.15 m/s; the residual cuts station-keeping error under wind by ~49% (0.117→0.060 m at 1.5 m/s; 0.319→0.162 m at out-of-distribution 3.9 m/s).

### [PhysibleMDM: Enforcing Inference-Time Physical Feasibility Constraints on Motion Diffusion Models via Noise Optimization](https://arxiv.org/abs/2610.30500)
🏷️ 交叉方向 / Also: 具身智能(运动生成 / motion generation)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 动作扩散模型生成的人体动作常违反物理约束,限制其在仿真与控制中的使用。PhysibleMDM 在推理时优化扩散噪声(无需重训),使用代理可行性约束:运动学检查(穿地、滑动、自碰撞)与通过逆动力学内循环(锥规划)评估的动力学可行性,用 Sep-CMA-ES 求解黑箱优化,并自回归拼接长序列。100 种风格的 SMPL 人形上,平均穿地、自碰撞穿透、滑动分别降低 75%、92%、74%;在自定义双足机器人 11 条序列上,逐序列平均加速度重建误差中位数降低 89.5%,逆动力学残差平均降低 79.5%。
- 🇬🇧 Motion diffusion models often violate physics, limiting use in simulation and control. PhysibleMDM optimizes the diffusion noise at inference (no retraining) with surrogate feasibility constraints — kinematic checks plus dynamic feasibility via an inverse-dynamics cone program — solved with Sep-CMA-ES, chaining segments autoregressively. On 100 SMPL motion styles it reduces ground penetration, self-collision penetration and slip by 75%, 92% and 74%; on 11 sequences for a bipedal robot it cuts median acceleration-reconstruction error by 89.5% and mean inverse-dynamics residual by 79.5%.

### [TRACE: Typed Reference-Aware Conversational Editing for Humanoid Motion Diffusion](https://arxiv.org/abs/2610.21515)(arXiv 2026-10-15;Replacement/Cross 列表项)
🏷️ 交叉方向 / Also: 具身智能(语言条件动作生成;因目标是 Unitree G1 人形动作参考,归入运动控制 / G1 humanoid motion references)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Multimodal-Perception-Action/TRACE);摘要给出,匿名 `git ls-remote` 验证存在
- 🇨🇳 语言条件的人形动作生成需把含糊请求连接到可修订的具体动作结构。TRACE 围绕类型化、可度量的运动学量构建生成与编辑:语言模型学习预测支撑、根部与手部事件,其时间对齐编码补充文本进入扩散生成器;重力参考状态和轨迹-接触目标提升运动学一致性;编辑时用类型化请求定义身体-时间范围与相对源动作的目标,由参考条件扩散编辑器实现修改,并在采样时投影以保护不改动的状态坐标。定量与人工评估显示语义对齐与动作质量优于对比方法,多轮编辑下对连续相对请求的执行更可靠(摘要未给出具体数值)。
- 🇬🇧 Language-conditioned humanoid motion generation must tie underspecified requests to concrete, revisable motion structure. TRACE, for the Unitree G1, grounds generation in typed measurable kinematic quantities: a language model predicts support, root and hand events whose time-aligned encodings complement text in a diffusion generator, with gravity-referenced states and trajectory–contact objectives; a reference-conditioned diffusion editor realizes typed body–time-scoped edits with sampling-time projection preserving protected coordinates. Quantitative and human evaluations show better semantic alignment and motion quality, and multi-turn editing is more reliable; no numbers in the abstract.

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

*本类共 20 条:详细展开 10 条,其余 10 条列名。 / 20 items: 10 expanded, 10 listed.*

### [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://arxiv.org/abs/2610.31670)
🏷️ 交叉方向 / Also: VLA, 世界模型与 WAM
开源状态 / Code: ✅ 已开源 / Released — [项目页](https://yunfeixie233.github.io/s2/)(Comments 称项目页与代码可获取;未能确认具体仓库 URL,待核实)
- 🇨🇳 机器人基础模型通常要靠昂贵的闭环 rollout 评估。本文受柏拉图表征假说启发,提出免训练的离线指标 Sensorimotor Alignment(S²),衡量模型感觉表征与物理运动几何的对齐程度。S² 与多个具身模型家族的下游任务成功率正相关,可作为在闭环评估前筛选模型的低成本代理,还能在 VLM 微调为 VLA 之前识别有潜力的骨干,并为 VLA 与 WAM 的现象提供表征层面的解释。摘要未给出具体相关系数。
- 🇬🇧 Robot foundation models are evaluated by costly closed-loop rollouts. Inspired by the Platonic Representation Hypothesis, the paper proposes S², a training-free offline metric of how well a model's sensory representation aligns with the geometry of physical motion. S² correlates positively with downstream task success across embodied model families, serves as a cheap proxy to prioritize models, can identify promising VLM backbones before VLA fine-tuning, and explains phenomena seen in VLAs and WAMs; no correlation values are given in the abstract.

### [Learning Robot Behavior Priors from Non-Robotic Synthetic Data](https://arxiv.org/abs/2610.31275)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 真实机器人数据常被视为瓶颈。本文问:无本体的廉价程序化合成数据能否在模型见到真实行为前提供有用先验?设计三条建模机器人控制数学抽象的数据生成管线,用其预训练 Transformer 做机器人动作预测。仅用非机器人数据训练的模型通过上下文学习在未见真实机器人任务上取得非平凡的零样本预测,专门的控制先验明显优于通用因果先验;与算力匹配的真实机器人数据基线相比,后者只在其训练过的数据集上更好。
- 🇬🇧 Real robot data is often seen as the bottleneck. The paper tests whether cheap procedurally generated data from systems without embodiment gives useful priors, using three pipelines that model mathematical abstractions of control to pretrain a Transformer for action prediction. The model trained purely on non-robotic data attains non-trivial zero-shot prediction on unseen physical robot tasks via in-context learning, control-specific priors beat generic causal priors, and a compute-matched real-robot baseline wins only on the datasets it was trained on.

### [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](https://arxiv.org/abs/2610.28589)(HF Daily 37 upvotes)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/xinxinliu-ai/AgenticRoboRL);HF 字段给出,匿名 `git ls-remote` 验证存在;摘要称将发布框架与训练好的规划器检查点
- 🇨🇳 现有智能体机器人系统依赖闭源强模型作规划器,未提升规划器本身。AgenticRoboRL 用监督微调加多轮强化学习对不同 harness(VLA 技能调用、控制代码生成)下的机器人规划器做后训练,通过 harness 专用适配器把规划交互与任务结果连接起来,共用一套 RL 流水线。在 LIBERO-PRO 上,9B 规划器成功率从 18.1% 提升到 71.0%(无外部记忆),接近带外部记忆的 Codex(GPT-5.5)的 72.1%。
- 🇬🇧 Agentic robot systems rely on closed-source planners and do not improve the planner itself. AgenticRoboRL post-trains robot planners with SFT plus multi-turn RL across harnesses (VLA skill invocation, control-code generation), using harness-specific adapters that link recorded interactions with outcomes in one RL pipeline. On LIBERO-PRO it lifts a 9B planner from 18.1% to 71.0% without external memory, approaching 72.1% for Codex (GPT-5.5) with external memory.

### [TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models](https://arxiv.org/abs/2610.25376)(Comments: 项目页 hku-sail.github.io/TILDE)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/hku-sail/TILDE);HF 字段给出,匿名 `git ls-remote` 验证存在
- 🇨🇳 复现具身基础模型的大规模动作预训练需要大量数据与算力。TILDE 结合学生诱导状态下的在线蒸馏与教师执行的恢复轨迹学习;AutoDAgger 用机器人奖励模型监测任务进度并触发教师介入,无需人工监控即可收集恢复经验,收集速度比人在回路快 2 倍以上。统一示范学习、在线教师监督和教师纠正行为后,在三个真机任务上相比行为克隆最高提升 4.1 倍,并支持跨架构蒸馏。
- 🇬🇧 Reproducing large-scale action pretraining of embodied foundation models is costly. TILDE combines on-policy distillation at student-induced states with learning from teacher-executed recovery trajectories; AutoDAgger uses a robotic reward model to monitor progress and trigger teacher intervention, collecting recovery data over 2× faster than human-in-the-loop. Across three real-world tasks it improves performance by up to 4.1× over behavior cloning and supports cross-architecture distillation.

### [ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models](https://arxiv.org/abs/2610.27040)
🏷️ 交叉方向 / Also: 空间智能 / Spatial Intelligence
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/DAXIAORobotics/ACE-Brain-0.6);HF 字段给出(未单独做 `git ls-remote` 验证)
- 🇨🇳 通用多模态模型的具身操作能力伴随强空间感知。本文构建统一数据管线,把机器人操作录像与多来源视觉数据结合,自动标注后转为可验证的 grounding 监督;在约 150 万样本上微调 Qwen3.5-9B 得到 ACE-Brain-0.6,在 7 个公开 grounding 基准中的 4 个上超过 GPT-6 Astra,总体平均分 75.41 对 73.68;随数据版本扩展,聚合 grounding 表现稳步提升。
- 🇬🇧 General multimodal models' embodied manipulation comes with strong spatial perception. The paper builds a unified pipeline combining robot manipulation recordings and diverse visual data, auto-annotates them into verifiable grounding supervision, and fine-tunes Qwen3.5-9B on ~1.5M samples to get ACE-Brain-0.6. It beats GPT-6 Astra on four of seven public grounding benchmarks (average 75.41 vs 73.68), with performance rising steadily as data releases expand.

### [The Bitter Lesson Comes to Robotics](https://arxiv.org/abs/2610.25287)(Comments: Submitted to TAG workshop at CoRL 2026)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码信息
- 🇨🇳 评估前沿多模态 LM 直接控制真实机械臂的能力。在 RoboDojo 的 6 个操作任务上评估 9 个模型(多种推理强度与服务档位),为实物上首个广泛的系统比较。结论:前沿模型已能直接控制真实机械臂完成多种任务,但精度与效率尚不足以在合理动作预算内完成;7–10 月间性能翻倍时间为 53.9 天,最佳执行率提高 4.4 倍,最低执行成本降低 6.2 倍。
- 🇬🇧 The paper evaluates nine frontier multimodal LMs directly controlling physical arms on six RoboDojo manipulation tasks, the first broad hardware comparison. Models can control real arms for varied tasks but are not yet precise or efficient enough within a practical action budget; between July and October 2026 performance doubled every 53.9 days, the best execution rate rose 4.4× and the lowest cost fell 6.2×.

### [Know When to Escalate: Critic-Guided Adaptive Execution for Cloud-Local Embodied Agents (CARE)](https://arxiv.org/abs/2610.30587)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 云端强智能体让平台在动作间空等数秒,本地轻量模型快但易错,固定角色分工或无状态路由都不理想。CARE 用轻量评论家监测执行可靠性,在本地执行不可靠时把控制升级到云端强模型,升级后持续直至恢复,并用共享交接记忆保留上下文。在多个具身基准上任务成功率比最强协作基线高 6.3–18.3 个百分点,接近或超过仅云端成功率,同时中位动作间隔延迟降低 28.8–82.6%。
- 🇬🇧 Cloud agents idle the platform between actions while local models are fast but error-prone; fixed roles or stateless routers are suboptimal. CARE uses a lightweight critic to escalate from a local executor to a stronger cloud model when execution becomes unreliable, persisting until recovery, with shared handoff memory. Across embodied benchmarks it improves success by 6.3–18.3 points over the strongest collaboration baseline, approaches or exceeds cloud-only success and cuts median time-between-action latency by 28.8–82.6%.

### [Replan for Error Recovery: Training Embodied VLMs through Verifiable Interaction with Action-Grouped Turn-GSPO](https://arxiv.org/abs/2610.27003)(Replacement)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 执行错误会让环境进入需要重规划的状态,现有恢复方法依赖固定策略的推理时机制或参考纠正而非已验证的动作结果。本文提出 ERR-Env(提供任务进度与执行错误反馈)与 ERR-Bench,并提出 AGT-GSPO(轮级奖励 + 动作分组优势估计的在线 RL),训练 2B 的 ERR-VLM。在 ERR-Bench 上,AGT-GSPO 使无错完成的 Strict Success Rate 提升 10.25 个百分点、Recovery Rate 提升 22.95 个百分点。
- 🇬🇧 Execution errors leave environments needing replanning, yet recovery methods rely on fixed-policy inference mechanisms or reference corrections. The paper introduces ERR-Env (task progress and error feedback), ERR-Bench, and AGT-GSPO, an online RL method with turn-level rewards and action-grouped advantage estimation, to train the compact 2B ERR-VLM. On ERR-Bench it improves Strict Success Rate by 10.25 points and Recovery Rate by 22.95 points.

### [Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents](https://arxiv.org/abs/2609.39304)(Replacement)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 把现成编码智能体当机器人策略时,harness(提示、工具、控制规则)决定成败且需手写。本文表明可由另一个优化器智能体自动改进:每轮 rollout 数越多(5→100)留出成功率越高;必须用 Champion-Challenger 规则仅在固定用例上优于现任时才接受修订,否则几轮内退化。该规则在 LIBERO 上 30 轮把留出成功率从 51% 提升到 67%;蒸馏后的独立策略在 RoboCasa365 达 62.2%(+4.8 点),叠加演化 harness 达 71.2%,比最佳已发表结果高 13.1 点。
- 🇬🇧 When a coding agent acts as a robot policy, the harness largely determines success and has been hand-written. An optimizer agent can improve it: held-out success rises with rollouts per round (5→100), and a Champion-Challenger rule (accept a revision only if it beats the incumbent on fixed cases) is needed to avoid degradation, raising LIBERO held-out success from 51% to 67% in 30 rounds. Distilling back yields a standalone policy at 62.2% on RoboCasa365 (+4.8 points) and the evolved harness on top reaches 71.2%, 13.1 points above the best published entry.

### [From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation (SERA)](https://arxiv.org/abs/2610.29560)(HF Daily 24 upvotes)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/StevenKKXS/SERA);HF 字段给出(未单独 `git ls-remote` 验证)
- 🇨🇳 长时序任务存在非马尔可夫依赖,部分可观测与执行错误会累积。SERA 把高层 VLM 组织为带可编辑 harness 的机器人智能体,用固定 VLA 执行器做低层控制;harness 依据观测和执行反馈维护任务上下文,并通过环境 rollout 提出并评估修订、在留出测试前固定配置。在 RoboMME 上自主选择的 SERA 总体成功率 51.38%,无自演化为 44.38%。
- 🇬🇧 Long-horizon tasks have non-Markovian dependencies with partial observability and compounding errors. SERA organizes a high-level VLM as a robotic agent with an editable harness over a fixed VLA executor; the harness maintains task context from observations and feedback, and self-evolution proposes and evaluates revisions via rollouts, fixing the configuration before held-out testing. On RoboMME it reaches 51.38% overall success with autonomous selection versus 44.38% without self-evolution.

**其余 10 条(列名)/ Remaining 10:** [Externalise the Memory](https://arxiv.org/abs/2610.30478) · [Robot Generalization Beyond Volume](https://arxiv.org/abs/2610.29829) · [Alpha](https://arxiv.org/abs/2610.30197) · [HiSTEVE 1.0](https://arxiv.org/abs/2610.31162) · [Scaling in Games (GameScaling)](https://arxiv.org/abs/2610.28698) · [Toward Recursive Self-Improvement in Physical AI](https://arxiv.org/abs/2610.29677) · [V2-STRep](https://arxiv.org/abs/2609.20582) · [Learning Cooperative Bimanual Dexterous Grasp of Large Objects with Tactile Sensing](https://arxiv.org/abs/2608.10383) · [To Route or to Adapt?](https://arxiv.org/abs/2610.31095) · [Live Thread Reconstruction for Autonomous Manipulation](https://arxiv.org/abs/2610.30694)

另见 / See also: [DONIC](https://arxiv.org/abs/2610.29997)、[WholeBodyMem](https://arxiv.org/abs/2610.31166)、[MiDAS](https://arxiv.org/abs/2608.11363)(均已归入运动控制·RL)。

---

## VLA

*本类共 13 条:详细展开 10 条,其余 3 条列名。 / 13 items: 10 expanded, 3 listed.*

### [Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models](https://arxiv.org/abs/2610.31569)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://lyfeng001.github.io/Echo/)由 Comments 给出,未核查代码链接
- 🇨🇳 VLA 需识别任务完成与失败,但现有方法需要细粒度监督、外部监控模型或复杂结构,且状态信号对动作生成的引导作用未被充分探索。Echo 把停止与失败信号作为动作块的两个额外维度,与机器人动作一起去噪;无需帧级进度标注,通过构造成功、失败与恢复轨迹提供互补监督,并让状态信号去噪快于动作,使后续动作去噪依赖更干净的状态估计。大量真机操作实验表明可准确预测任务状态并持续提升策略性能(摘要未给出具体数值)。
- 🇬🇧 VLAs need to recognize completion and failure, but existing approaches require fine-grained supervision, external monitors or complex designs, and status signals' role in guiding actions is underexplored. Echo adds stop and failure signals as two extra dimensions of each action chunk, denoised jointly with actions, learns them without frame-level progress labels from constructed success/failure/recovery trajectories, and denoises signals faster than actions so later action steps condition on cleaner status. Real-world experiments show accurate status prediction and consistent policy gains; no numbers in the abstract.

### [FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models](https://arxiv.org/abs/2610.31423)(Comments: Accepted at CoRL 2026)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 现有 VLA 未充分利用多视角互补性,策略持续依赖腕部视角,缺乏跨阶段调整全局-局部依赖的能力。FocusVLA 由历史动作预测未来交互意图,并以之引导动作生成时的动态视角路由,且可无需改动核心架构集成进现有 VLA。RoboTwin 2.0 上平均成功率比最强基线 π0.5 高 10.10 个百分点;真机成功率从 71.7% 提升到 85.0%(+13.3%)。
- 🇬🇧 VLAs underuse multi-view complementarity, persistently relying on the wrist view. FocusVLA predicts future interaction intent from historical actions and uses it to route views dynamically during action generation, pluggable into existing VLAs without core changes. It beats π0.5 by 10.10 points average on RoboTwin 2.0 and raises real-world success from 71.7% to 85.0%.

### [Progress Probes P²: Lightweight Runtime Monitoring for Vision-Language-Action Models](https://arxiv.org/abs/2610.31613)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 VLA 易出错,现有运行时监控依赖外部 VLM,复杂且昂贵。本文用线性探针读取 VLA 自身内部激活估计任务进度,并标记偏离预期进度的执行。在开源 VLA π0.5、仿真与真机操作任务上,故障检测与基于 VLM 的监控器相当或更好,也优于需要失败数据训练的方法;摘要未给出具体数值。
- 🇬🇧 VLAs make mistakes and existing monitors rely on external VLMs, adding complexity and cost. The method trains linear probes on the VLA's own activations from demonstrations to estimate progress and flags deviations. With π0.5 across simulated and real tasks it is competitive with or better than VLM-based monitors and methods needing failure data; no numbers in the abstract.

### [FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies](https://arxiv.org/abs/2610.31427)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/FastHarness/fast-harness);Comments 给出,匿名 `git ls-remote` 验证存在
- 🇨🇳 智能体机器人系统每个动作块都审查开销很大。FastHarness 用经验驱动的执行 harness,自适应调度 GPT-6 Astra 对 π0.5 的监督:快路径用阶段记忆和已审查结果降低审查频率,恢复路径专注纠错,策略保持冻结。四个仿真操作任务上,审查 token 用量从首个评估回合到最后五个回合平均降低 57.2%,单回合平均时间从 85.5 降到 52.0 分钟,平均成功率从 GPT-as-Policy 的 80% 升至 97.19%。
- 🇬🇧 Reviewing every action chunk of an agentic robot is costly. FastHarness adaptively schedules GPT-6 Astra supervision of a frozen π0.5 policy with a fast path using stage memory and reviewed outcomes and a recovery path for errors. On four simulated tasks, reviewer tokens drop by 57.2% on average from the first to the last five episodes, episode time falls from 85.5 to 52.0 minutes, and mean success rises from 80% (GPT-as-Policy) to 97.19%.

### [When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies](https://arxiv.org/abs/2610.30735)(Comments: Accepted at CoRL 2026)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无代码链接(radar 中有名称相近但未能确认对应的第三方仓库 [let-it-be-simple](https://github.com/bondtesty/let-it-be-simple),不算官方开源)
- 🇨🇳 flow matching VLA 推理需迭代求解 ODE,限制控制频率。本文问额外的单步生成目标是否必要,发现在六个 flow matching VLA 上,只要训练充分且容量足够,单步动作生成与多步采样大体相当,多步积分几乎没有一致优势。因此大型 VLA 的单步策略几乎"免费"得自多步模型,无需重训、蒸馏或辅助目标即可低延迟部署。
- 🇬🇧 Flow-matching VLAs need iterative ODE solving, limiting control frequency. Across six flow-matching VLAs, one-step action generation largely matches multi-step sampling when models are sufficiently trained and have enough capacity, so the single-step policy comes essentially for free from the multi-step model, enabling low-latency deployment without retraining, distillation or auxiliary objectives.

### [SmolVLA-MoE: Sparse Mixture-of-Experts for Efficient Multi-Task Robotic Manipulation](https://arxiv.org/abs/2610.30732)(Comments: IROS2027 prepared)
开源状态 / Code: ✅ 声称已开源 / Claimed — [仓库](https://github.com/dudu435/smolvla-moe);摘要给出,但匿名 `git ls-remote` 失败,链接匿名不可访问,待核实
- 🇨🇳 轻量 VLA 的单一稠密动作专家限制多任务能力。SmolVLA-MoE 在动作专家的 FFN 层引入稀疏 MoE:多个并行专家 FFN 加 token 级路由器,并用权重可调的共享专家平衡预训练继承与专家特化;推理只激活一个专家 FFN,激活参数约 5 亿(含冻结 VLM),存储约 8 亿。LIBERO 四个任务套件平均成功率 84.25%,高于 SmolVLA 的 82.75% 与 OpenVLA-7B 的 76.5%。
- 🇬🇧 Lightweight VLAs use a single dense action expert, limiting multi-task capability. SmolVLA-MoE replaces dense FFNs in the action expert with parallel expert FFNs and a token-level router plus a shared expert with tunable weight, activating one expert FFN at inference (~500M activated, ~800M stored parameters). On four LIBERO suites it averages 84.25%, above SmolVLA (82.75%) and OpenVLA-7B (76.5%).

### [MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models](https://arxiv.org/abs/2610.22951)(arXiv 2026-10-16;HF Daily)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/giakhuyendihoc/MambaAct);摘要给出代码与权重,匿名 `git ls-remote` 验证存在
- 🇨🇳 flow-matching VLA(如 π0.5)的动作专家在迭代去噪中被反复评估,推理成本成为实时控制瓶颈。MambaAct 保留 π0.5 的预训练视觉语言前缀编码器,把 Transformer 动作专家换成紧凑的 Mamba 动作专家,并用轻量 Context Compressor 把 VLM 前缀 token 映射为紧凑条件信号来门控、调制每个 Mamba 块。动作专家小 10 倍,flow-matching 去噪延迟在 LIBERO 上降低 64.8%、真机部署降低 58.8%,三个种子平均 LIBERO 成功率还提升 1.08 个百分点。
- 🇬🇧 In flow-matching VLAs such as π0.5 the action expert runs repeatedly during denoising, a real-time bottleneck. MambaAct keeps the pretrained prefix encoder but swaps the Transformer action expert for a compact Mamba one, with a Context Compressor turning VLM prefix tokens into a compact signal that gates and modulates each block. The expert is 10× smaller, denoising latency drops 64.8% on LIBERO and 58.8% in real deployment, and mean LIBERO success improves 1.08 points over three seeds.

### [UniMem: Unifying Visual and Textual Memory in VLAs for Non-Markovian Tasks](https://arxiv.org/abs/2608.22869)(Replacement)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://losterberg3.github.io/unimem-vla/)由摘要给出,未核查代码链接
- 🇨🇳 VLA 在需要记忆的非马尔可夫任务上表现不佳,现有记忆方案依赖额外 VLM,造成瓶颈和割裂的训练流程。UniMem 在单一骨干下统一高层视觉/文本记忆与低层控制:事件分类器触发记忆更新,关键帧编码器负责稠密视觉记忆,关键帧缓存降低 rollout 开销。5 个仿真和 4 个真机任务上,仿真中 93.4% 对固定间隔采样基线 68.2%,真机 80.0% 对层级 VLM-VLA 基线 43.5%,且推理更快、训练更简单。
- 🇬🇧 VLAs struggle with non-Markovian tasks; existing memory uses extra VLMs, creating a bottleneck and fractured pipelines. UniMem unifies visual/textual memory and low-level control under one backbone using an event classifier to trigger updates, a keyframe encoder for dense visual memory, and keyframe caching. Across five simulated and four hardware tasks it scores 93.4% vs 68.2% for fixed-interval sampling in simulation and 80.0% vs 43.5% for hierarchical VLM–VLA baselines on hardware, with faster inference.

### [Where Success Breaks: Failure-Boundary Learning for Robust Vision-Language-Action Models (DLS)](https://arxiv.org/abs/2609.06114)(Replacement)
🏷️ 交叉方向 / Also: 运动控制·RL 相关的 RL 后训练;因目标为操作 VLA 的鲁棒性微调而留在 VLA / manipulation VLA robustness, kept here
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 SFT 适配的 VLA 只知成功行为在哪,不知可靠性何处终止。DLS 把鲁棒适配视为"失败边界学习":基于少量真实示范与仿真联合训练的先验,用数字孪生在线 rollout 大规模发现失败边界;用特权仿真状态做语义进度定位给出带进度的信号;再在流动力学中做方向性边界塑形(强化成功去噪方向、抑制失败方向),无需动作似然或辅助评论家。真机操作任务上鲁棒性优于 SFT 与在线 RL 基线,尤其在随机初始状态和未见视觉条件下;摘要未给出具体数值。
- 🇬🇧 SFT-adapted VLAs know where success lies but not where reliability ends. DLS frames robust adaptation as failure-boundary learning: it discovers boundaries at scale with on-policy digital-twin rollouts (from a real-grounded prior with sim co-training), localizes them with progress-aware signals from privileged simulator states, and shapes flow dynamics directionally (reinforce success, suppress failure denoising directions) without action likelihoods or critics. It improves robustness over SFT and online RL baselines on real manipulation tasks, especially under randomized initial states and unseen visuals; no numbers in the abstract.

### [Do VLAs Really Follow Instructions? Diagnosing How-Level Instruction Following in Vision-Language-Action Models](https://arxiv.org/abs/2610.21251)(Comments: Preprint)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 VLA 被期望像语言骨干那样遵循指令,但此前关注指定任务的 What 级指令,忽视指定做法的 How 级指令。诊断发现 How 级指令对当前 VLA 无益且降低成功率;用片段级增强指令训练可使动作响应这类指令,但不一定提升成功率。提出 SIMPLER-IN(成功需要仅在指令中给出的条件),显示获得的响应性不能推广到更苛刻或分布外的 How 级指令,该问题仍是开放挑战。摘要未给出具体数值。
- 🇬🇧 VLAs are expected to follow instructions, but prior work targets What-level rather than How-level instructions. Diagnoses show How-level instructions don't help and lower success; training with segment-level enriched instructions makes actions responsive without consistently raising success. The proposed SIMPLER-IN requires conditions given only in the instruction and shows the gained responsiveness doesn't extend to demanding or out-of-distribution How-level instructions; no numbers in the abstract.

**其余 3 条(列名)/ Remaining 3:** [FluxVLA Engine](https://arxiv.org/abs/2609.17210)(✅ [仓库](https://github.com/FluxVLA/FluxVLA))· [RoboCasa-Shift](https://arxiv.org/abs/2610.27861)(✅ [仓库](https://github.com/HaochengWang23/RoboCasa-Shift))· [ThermoAct](https://arxiv.org/abs/2603.25044)

另见 / See also: [HEX](https://arxiv.org/abs/2604.07993)、[RL-Co](https://arxiv.org/abs/2602.12628)、[DRILL](https://arxiv.org/abs/2610.30814)、[WholeBodyMem](https://arxiv.org/abs/2610.31166)(均已归入运动控制·RL)。

---

## VLN

*本类共 5 条,全部展开。 / 5 items, all expanded.*

### [NavBind: Diagnosing Instruction-Action Binding at Route Forks in Navigation VLAs](https://arxiv.org/abs/2610.29203)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 导航成功不能说明模型真正遵循指令。NavBind 在固定导航上下文下检验改变指令是否改变动作分布:重组 R2R-CE 与 RxR-CE 中路线对齐的指令片段,构造 3,252 个路线分叉上下文,比较生成的局部动作序列、固定参考动作序列在两条指令下的似然,以及视觉注意力与归因变化。在评测模型中,更高的导航成功率并不意味着更忠实地遵循指令。
- 🇬🇧 Navigation success does not show a model follows instructions. NavBind fixes the navigation context and checks whether changing the instruction changes the action distribution, using 3,252 route-fork contexts recombined from R2R-CE and RxR-CE and comparing generated local actions, likelihoods of reference actions under both instructions, and attention/attribution changes. Across evaluated models, higher reported success does not imply more faithful instruction following.

### [Asking Less, Adapting Better: Feedback-Efficient Test-Time Adaptation for Vision-and-Language Navigation (FETA)](https://arxiv.org/abs/2610.30643)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 VLN 智能体在未见环境中因分布偏移性能骤降;熵最小化会传播错误,人工反馈方法又对所有步统一监督、效率低。FETA 先按归一化策略熵波动筛选轨迹,再用熵梯度显著性选出关键动作并只询问一次二值正确性反馈,仅在被询问步更新策略,并按预测-反馈差异自适应加权。多个基准上以更少人工干预取得最先进性能,对噪声反馈与持续适应保持鲁棒;摘要未给出具体数值。
- 🇬🇧 VLN agents degrade under distribution shift; entropy minimization propagates errors and human-feedback methods supervise all steps uniformly. FETA filters trajectories by normalized policy-entropy fluctuation, picks the critical action via entropy-gradient saliency, asks one binary feedback, and updates only at the queried step with discrepancy-aware adaptive scaling. It reaches state-of-the-art on multiple benchmarks with fewer interventions and stays robust under noisy feedback and continual adaptation; no numbers in the abstract.

### [KinoUAV: A Benchmark for Safe and Stable UAV Vision-Language Navigation with Kinodynamic Modeling](https://arxiv.org/abs/2610.30609)
🏷️ 交叉方向 / Also: 运动控制·传统(运动学动力学约束轨迹生成;因主贡献为 VLN 基准与智能体而留在 VLN / kept here as the main contribution is a VLN benchmark)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 现有无人机 VLN 方法没有显式纳入运动动力学和安全距离,导致偏航率高、碰撞多、成功率低。KinoUAV 包含数据集与 KinoUAV-Agent:分层运动动力学轨迹生成在速度/加速度/jerk 约束下逐段生成轨迹,数据集带有方向性自由空间距离(DFD)标签;智能体预测 DFD 并据此生成安全动作,并提出 Cruise-Seek 任务。实验显示其成功率最高,同时绝对偏航率与碰撞率更低(摘要未给出具体数值)。
- 🇬🇧 Existing UAV VLN methods ignore kinodynamics and safety distances, causing high yaw rates, collisions and low success. KinoUAV provides a dataset and agent: a hierarchical kinodynamic trajectory pipeline under velocity/acceleration/jerk limits, directional free-space distance (DFD) labels, an agent that predicts DFDs to generate safe actions, and a Cruise-Seek task. It achieves the highest success with lower absolute yaw rates and collision rates; no numbers in the abstract.

### [OASIS: Online Anchor-centric Scene Inference System for Open-Vocabulary Retrieval and Navigation in Dynamic Environments](https://arxiv.org/abs/2610.30589)(Comments: ACM MM 2026 oral)
🏷️ 交叉方向 / Also: 空间智能与 SLAM
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 轻量在线建图语义有限,稠密建图成本高且易受干扰,场景变化后也难以重定位物体。OASIS 用稀疏语义锚点节点表示环境,每个节点维护整合语义描述、视觉特征与几何状态的多模态表示,紧凑的锚点记忆支持按需取证和分层检索,并复用导航中的瞬时观测重定位被移动的物体。仿真与真机、静态与动态设置下的检索与导航实验表明可完成复杂开放词汇检索与导航,并能在场景变化后重定位物体;摘要未给出具体数值。
- 🇬🇧 Lightweight online maps lack semantics, dense maps are costly and distractor-prone, and objects are hard to relocalize after changes. OASIS represents the scene with sparse anchor nodes carrying multimodal representations (semantics, visual features, geometry), supports on-demand evidence extraction and hierarchical retrieval, and reuses transient observations to relocalize moved objects. Simulation and real-world retrieval and navigation experiments in static and dynamic settings show complex open-vocabulary retrieval/navigation and relocation of displaced objects; no numbers in the abstract.

### [CMAR-search: Commonsense and Memory Augmented Reasoning for Object Search in Dynamic Interactive Environments](https://arxiv.org/abs/2610.30606)(Comments: ICRA 2026)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/starry-curry-30/CMAR-search);radar new_repos 对应,匿名 `git ls-remote` 验证存在
- 🇨🇳 大规模人类环境中的交互式物体搜索,3D 场景图只提供粗粒度分割,无法识别功能区域,只能穷举探索并难以适应物体被移动。CMAR-search 利用区域功能常识并聚合环境记忆构建功能 3D 场景图(F3DSG),在宏观区域与微观容器两级做层次化行动规划,并持续整合实时感知、记忆与常识重定位物体。仿真和真机实验表明成功率与搜索效率显著超过最先进基线(摘要未给出具体数值)。
- 🇬🇧 In large interactive environments, 3D scene graphs give only coarse segmentation, forcing exhaustive search and poor adaptation to relocated objects. CMAR-search builds a Functional 3D Scene Graph from area-function commonsense and aggregated memory, plans hierarchically at area and container levels, and relocalizes objects from perception, memory and commonsense. Simulation and real-world experiments show markedly higher success rate and search efficiency than state-of-the-art baselines; no numbers in the abstract.

另见 / See also: [RangeNav](https://arxiv.org/abs/2610.29845)(已归入运动控制·RL)。

---

## 世界模型与 WAM / World Models & WAM

*本类共 14 条:详细展开 9 条,其余 5 条列名。 / 14 items: 9 expanded, 5 listed.*

### [UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry](https://arxiv.org/abs/2610.30991)
🏷️ 交叉方向 / Also: VLA, 具身智能(操作策略,非运动控制类)
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://kksham111.github.io/UniFlowWAM_ProjectPage/)写 "Code coming soon"(WebFetch 核对),尚无可用链接
- 🇨🇳 示范只记录看到什么和做了什么,不描述 3D 世界在其间如何变化;以往工作中 3D flow 只是独立模块或额外预测头。UniFlowWAM 把 3D 场景 flow 作为与视觉、动作并列的第三模态:每个模态一个专家的扩散 Transformer,通过联合注意力交换信息,并在十目标"角色网格"下训练,使同一模型既可作策略,也可作前向/逆动力学及未来视觉特征/3D flow 预测器。RoboCasa-GR1 成功率从无 flow 基座的 52.1% 提升至 56.4%;LIBERO 保持 98.1%,LIBERO-Plus 零样本 87.7%;四个真机双臂任务平均成功率 87.0%,最强基线 68.5%。
- 🇬🇧 Demonstrations record what the robot saw and did, not how the 3D world changed between; prior work kept flow as a separate module or head. UniFlowWAM makes 3D scene flow a third modality on par with vision and action in a diffusion transformer with one expert per modality exchanging information via joint attention, trained under a ten-objective role grid so one model serves as policy, forward/inverse dynamics and future-feature/flow predictor. It lifts RoboCasa-GR1 success from 52.1% to 56.4%, keeps 98.1% on LIBERO, reaches 87.7% zero-shot on LIBERO-Plus, and 87.0% average on four real bimanual tasks versus 68.5% for the strongest baseline.

### [Self-Distilling Future Video Representations for World Action Models (FRED)](https://arxiv.org/abs/2610.30320)(Comments: 27 pages;HF Daily 23 upvotes)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/suhyeok-jang/FRED);HF 字段给出,匿名 `git ls-remote` 验证存在(radar new_repos 亦收录)
- 🇨🇳 近期 WAM 通过单步去噪提取的中间未来视频表征来条件化动作解码器以提升推理效率,使动作预测直接取决于这些未来表征的质量。FRED 用自蒸馏让 WAM 从噪声预测未来表征(以真实未来观测提取的表征作目标),并让视频模型以历史观测为时间上下文。多种真实操作场景中 FRED 持续优于其他 WAM,在长时序和域外零样本环境泛化任务上增益尤大;对仅在人类视频中演示、机器人训练数据缺失的任务,成功率达 50.0%,最强竞争 WAM 为 19.4%。
- 🇬🇧 Recent WAMs condition an action decoder on future video representations from a single denoising step for efficiency, so action quality depends on those representations. FRED trains the WAM to predict future representations from noise via self-distillation (targets from ground-truth futures) and conditions the video model on history. Across real manipulation scenarios it consistently beats competing WAMs, especially on long-horizon and out-of-domain zero-shot tasks, and reaches 50.0% on tasks only demonstrated in human videos versus 19.4% for the best competing WAM.

### [Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation (P³-WAM)](https://arxiv.org/abs/2610.22363)(Replacement)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://p3-wam.pages.dev/)由摘要给出,未核查
- 🇨🇳 P³-WAM 通过三种模式学习 3D 感知、动作条件预测和目标导向规划:Perceive(从视频重建手部与相机轨迹)、Predict(在给定动作下生成视觉未来)、Plan(联合生成动作轨迹及预期视觉后果)。用混合 Transformer 架构把紧凑的结构化 3D 动作表示融入预训练视频扩散 Transformer,随机模态可见性让视频与 3D 动作可作条件或目标。统一训练提升三种能力,在四个数据集上 3D 手重建和动作条件视频预测优于专用基线,生成的目标导向操作视频指令遵循更强;摘要未给出具体数值。
- 🇬🇧 P³-WAM learns 3D perception, action-conditioned prediction and goal-directed planning through three modes — Perceive (reconstruct hand motion and camera trajectories), Predict (visual futures under prescribed actions), Plan (jointly generate actions and anticipated visuals). It integrates a compact structured 3D action representation into a pretrained video diffusion transformer via mixture-of-transformers with randomized modality visibility. Unified training improves all three capabilities, beats specialized baselines on 3D hand reconstruction and video prediction across four datasets and yields stronger instruction adherence; no numbers in the abstract.

### [Skeleton-Grounded Latent Action Model for Robot World Models (SkeLAM)](https://arxiv.org/abs/2610.31474)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://aopolin-lv.github.io/SkeLAM/)由 Comments 给出,未核查
- 🇨🇳 重建驱动的潜在动作把机器人运动与物体响应等场景变化混在一起,难以与机器人控制对应。SkeLAM 把潜在动作分解为由机器人骨架监督的运动学分量和保留互补视觉动态的残差分量,用跨模态交换重建使 RGB 与骨架导出的运动学表示可互换,分支 dropout 降低对未来残差信息的依赖,轻量适配器把机器人动作映射到运动学空间。DROID 上相比 DreamDojo,末端执行器 ADE 降低 19.5%,LPIPS 降低 11.1%;策略评估显示预测成功率与真机测得一致。
- 🇬🇧 Reconstruction-driven latent actions mix robot motion with object responses, complicating correspondence with controls. SkeLAM decomposes latent actions into a skeleton-supervised kinematic component and a residual component, uses cross-modal swap reconstruction and branch dropout, and a lightweight adapter maps robot actions to the kinematic space. On DROID it reduces end-effector ADE by 19.5% and LPIPS by 11.1% versus DreamDojo, and policy evaluation shows predicted success rates agree with real executions.

### [DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models](https://arxiv.org/abs/2610.30781)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://dexplicit.github.io)由 Comments 给出,未核查
- 🇨🇳 现有方法把动作条件动力学、相机运动和视觉合成纠缠在视频生成模型中,或用缺乏物体结构的点轨迹表示动力学。DeXplicit 先在度量 3D 中显式预测世界演化(轻量 3D 动力学网络预测物体中心运动与形变),再将外观沿预测的 3D 运动搬运并投影到未来视图,渲染器只需补全不确定和新可见的内容;该分解支持高效因果生成,每块仅需两步去噪。HOT3D、OakInk2、PhysTwin 上相对 PointWorld 移动点误差降低 27–40%,HOT3D 上物体保真 IoU+ 提升 47%;两步因果生成相对 14B 双向配置在视频合成上加速 57 倍。
- 🇬🇧 Existing approaches entangle dynamics, camera motion and synthesis in video generators or use point trajectories without object structure. DeXplicit first predicts world evolution explicitly in metric 3D (a lightweight 3D dynamics network for object-centric motion and deformation), then transports appearance through the predicted motion into future views so the renderer only completes uncertain content, enabling causal generation with two denoising steps per block. It reduces moved-point error by 27–40% versus PointWorld, improves object-fidelity IoU+ by 47% on HOT3D, and gives a 57× video-synthesis speedup over the 14B bidirectional configuration.

### [LaLa-World: Scaling Latent World Models with Natural Language Actions](https://arxiv.org/abs/2610.27851)(HF Daily 27 upvotes)
🏷️ 交叉方向 / Also: VLA / 策略学习(LaLa-Policy)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/junha1125/LaLa-World);摘要与 HF 给出,匿名 `git ls-remote` 验证存在;[项目页](https://june-page.github.io/lala-world/)
- 🇨🇳 本文表明 JEPA 式隐世界模型可采用视频生成模型的语言条件接口,跨领域学习并用于想象规划和下游策略微调。LaLa-World 把数值动作和视觉变化都用语言描述,使单一未来预测器能联合训练异构数据集,并以语言模型为骨干。其 MPC 规划的平均性能高于按领域/任务分别训练的隐世界模型;与基于 RAEv2 的视频生成基线相比,规划性能相当但训练成本低 6 倍、规划快 13.9 倍;预训练模型初始化的 LaLa-Policy 在 LIBERO 与 RoboCasa 上与 Cosmos Policy 相当,推理最高快 5.5 倍。
- 🇬🇧 The paper shows JEPA-style latent world models can adopt the language-conditioned interface of video generators to learn across domains, supporting imagination planning and policy fine-tuning. LaLa-World describes both numeric actions and visual changes in language, enabling joint training across heterogeneous datasets with a language-model predictor. Its MPC planning beats per-domain latent world models, matches an RAEv2-based video-generation baseline with 6× less training cost and 13.9× faster planning, and LaLa-Policy is competitive with Cosmos Policy on LIBERO and RoboCasa with up to 5.5× faster inference.

### [In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations](https://arxiv.org/abs/2610.30988)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 软体衣物操作状态维度高且依赖材料,学习型世界模型需要大量难采集的真实数据。本文提出软体世界模型:在大规模软体物体仿真交互上训练 Transformer,做生成式全状态估计与动作条件动力学预测,并有缓解 sim-to-real 差距的措施;通过对变长部分点云历史的上下文学习推断隐含形状与材料线索,无需更新权重即可泛化到不同本体、材料参数、衣物类型与形状。世界模型再与目标条件动作规划器集成,在仿真与真机双臂叠衣任务中重建精度、预测精度与任务成功率均有提升(摘要未给出具体数值)。
- 🇬🇧 Soft-garment manipulation has high-dimensional, material-dependent states, and learned world models usually need large real datasets. The Soft-Object World Model is a Transformer trained on large-scale simulated soft-object interactions for generative full-state estimation and action-conditioned dynamics, with sim-to-real measures, inferring latent shape/material through in-context learning over variable-length partial point-cloud histories and generalizing across embodiments, materials and garments without weight updates. Integrated with a goal-conditioned planner, it improves reconstruction fidelity, prediction accuracy and task success in simulated and real bimanual folding; no numbers in the abstract.

### [Inside-JEPA: From Prediction to Relational Grounding in Latent World Models](https://arxiv.org/abs/2610.31194)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 JEPA 在隐空间学习世界模型,利于规划但状态不透明。Inside-JEPA 在隐状态内放置有序实体对的关系通道,并表明当逆动力学头读取这些通道时,逆动力学损失可以在无关系标签下使通道落地。Something-Something V2 上仅隐预测不优于随机关系头,逆动力学监督使关系 AUROC 在十种设置下提高 0.065–0.103,RH20T 机器人留出任务上提高 0.081;给定动作时预测的关系变化接近观察到的未来关系质量(AUROC 0.599 对 0.621);一步关系目标上,16 个通道的监督读出在 65 个动作中将正确动作排进前五的比例为 43%(仅预测隐变量为 24%)。
- 🇬🇧 JEPAs learn latent world models good for planning but with opaque states. Inside-JEPA places relational channels for ordered entity pairs in the latent state and shows an inverse-dynamics loss grounds them without relation labels when its head reads them. On Something-Something V2 latent prediction alone is no better than a random head, while inverse-dynamics supervision lifts relational AUROC by 0.065–0.103 across ten settings and 0.081 on RH20T held-out robot tasks; predicted relational changes approach observed future quality (0.599 vs 0.621), and for one-step goals the readout ranks the correct action in the top five of 65 in 43% of cases versus 24% for prediction-only latents.

### [An Introduction to World Models for Generalist Agents](https://arxiv.org/abs/2610.30789)(综述 / introduction)
开源状态 / Code: ❓ 未知 / Unknown — 综述,无代码
- 🇨🇳 内容:世界模型概念定义松散,涵盖预测动力学、学习型模拟器和联合生成未来观测与动作的模型。本文从 POMDP 出发,将世界建模与经典控制、动力系统、信号处理和强化学习联系起来,介绍不同世界建模方法所捕获的知识、学习目标及其如何支持决策,并探讨通过条件预测统一世界建模与策略学习。结论:侧重基本概念、建模原则与联系,而非穷尽式综述。
- 🇬🇧 Content: the concept of a world model is loosely defined. Starting from POMDPs, the paper connects world modeling to classical control, dynamical systems, signal processing and RL, introduces approaches in terms of captured knowledge, learning objectives and support for decision-making, and shows policy learning and world modeling can be unified via conditional prediction. Takeaway: an accessible introduction to fundamentals and connections rather than an exhaustive survey.

**其余 5 条(列名)/ Remaining 5:** [Anticipating Social Consequences with Distributional World Models](https://arxiv.org/abs/2610.30657) · [RGraph-Eval](https://arxiv.org/abs/2610.31121)(代码 will be released) · [Looking Ahead](https://github.com/TencentARC/Looking-Ahead)(仓库,86★,自回归视频生成) · [OSWAM](https://github.com/PolyU-VCLab/OSWAM)(仓库,3★) · [World-in-Context](https://github.com/aigc3d/World-in-Context)(仓库,4★)

另见 / See also: [DiffDreamer](https://arxiv.org/abs/2610.31617)、[DRILL](https://arxiv.org/abs/2610.30814)、[SuperMimic](https://arxiv.org/abs/2610.28480)(可微世界模型用于人形全身控制;均已归入运动控制·RL / 监测项,SuperMimic 见 OSS Watchlist)。

---

## 空间智能与 SLAM / Spatial Intelligence & SLAM

*本类共 9 条:详细展开 8 条,其余 1 条列名。 / 9 items: 8 expanded, 1 listed.*

### [SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?](https://arxiv.org/abs/2610.26659)(HF Daily 147 upvotes)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/JesseZZZZZ/SpatialScout);摘要给出,匿名 `git ls-remote` 验证存在
- 🇨🇳 空间问答难以说明模型能否通过自主探索构建准确度量地图。SpatialScout 是主动物体级 3D 建图基准:80 个室内场景、3,140 个目标物体,智能体控制相机探索并估计共享坐标系下的物体中心,需协调视角选择、跨视图关联、几何估计与地图修正。最强评测模型(Claude Opus 5.5)平均重叠得分 41.71%,47.23% 的目标 IoU 超过 0.5,仅 3.25% 超过 0.9,说明从粗略布局到完整精确度量地图之间仍有很大差距。
- 🇬🇧 Spatial QA gives limited evidence of whether models can build accurate metric maps by exploring. SpatialScout benchmarks active object-level 3D mapping on 80 indoor scenes with 3,140 targets, where agents control a camera and estimate object centers in a shared frame, coordinating viewpoint selection, cross-view association, geometry and map revision. The strongest model (Claude Opus 5.5) gets a mean overlap score of 41.71%, with 47.23% of targets above IoU 0.5 and only 3.25% above 0.9.

### [Point-Level Refinable Semantic Mapping for Spatial Understanding](https://arxiv.org/abs/2610.31476)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 现有物体中心语义地图多为静态场景、只追加点,感知误差累积,物体移动或消失后过时点仍保留。本文提出在线可精化语义建图:每个物体点维护置信度,由多视角时序证据更新(一致观测增强可靠点,不一致的分割掩码、深度和可见性线索抑制虚假与过时点),并结合跟踪与重识别保持实例身份。建图精度在 Replica 上比先前方法提高 3.46%、ScanNet 上提高 2.55%,作为空间记忆在物体导航与具身问答上的成功率分别为 82.4% 和 76.7%。
- 🇬🇧 Object-centric semantic maps are mostly static and append-only, so perception errors accumulate and outdated points persist. The framework maintains a per-point confidence updated from multi-view temporal evidence plus tracking and re-identification. Mapping accuracy improves by 3.46% on Replica and 2.55% on ScanNet over the previous method, and as spatial memory it reaches 82.4% success on object navigation and 76.7% on embodied QA.

### [Consistent Distributed Invariant EKF SLAM with Point and Object Features (Joint-CI)](https://arxiv.org/abs/2610.31221)(Comments: submitted to RA-L)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 多机器人 SLAM 反复交换地图会产生未知相关性;协方差交叉(CI)可融合而无需追踪相关,但在右不变 EKF SLAM 中邻居的地图估计在其自身误差坐标中且与位姿相关,无法直接 CI。Joint-CI 构造接收机器人位姿与共有特征在其误差坐标中的联合估计,保留机器人-特征与特征-特征相关,再用部分状态 CI 融合。证明统一形式和融合保持与全局旋转/平移相关的六个不可观方向,并保持一阶协方差一致性;蒙特卡洛仿真与真实数据集实验显示估计精度提高且不确定性保持一致、略保守。
- 🇬🇧 Multi-robot SLAM map exchange creates unknown correlations; covariance intersection fuses without tracking them, but in right-invariant EKF SLAM a neighbor's map is in its own error coordinates and correlated with its pose. Joint-CI builds a joint estimate of the receiver's pose and common features in its error coordinates and fuses it by partial-state CI, preserving the six unobservable directions and first-order covariance consistency. Monte Carlo simulation and a real-dataset experiment show improved accuracy with consistent, mildly conservative uncertainty.

### [HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction](https://arxiv.org/abs/2610.31635)(Comments: Technical Report)
开源状态 / Code: ✅ 声称已开源 / Claimed — 摘要给出 [项目页/代码地址](https://kkakkkka.github.io/HiP3R);指向项目页而非 GitHub 仓库,待核实
- 🇨🇳 前馈模型能从短视频窗口估计相机运动与 3D 几何,但数千帧序列只能分块处理,各块坐标系不一致。HiP3R 用层次位姿图:先优化鲁棒的块级 Sim(3) 图确定全局布局与尺度,再固定该布局为每帧估计一个共享 SE(3) 相机,把重叠窗口预测合并成单一轨迹。无需额外训练或微调,适用于块式与流式后端,多个基准上改善相机轨迹和 3D 重建;摘要未给出具体数值。
- 🇬🇧 Feed-forward models estimate pose and geometry for short windows, but long videos must be chunked with inconsistent frames. HiP3R first optimizes a robust chunk-level Sim(3) graph for global layout and scale, then fixes it and estimates one shared SE(3) camera per frame, merging overlapping predictions into one trajectory. It needs no extra training, works with chunk-based and streaming backends, and improves trajectories and reconstruction across benchmarks; no numbers in the abstract.

### [OmniRay: Camera-Agnostic Monocular 3D Reconstruction with Composite Ray Fields](https://arxiv.org/abs/2610.31645)
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://nam1410.github.io/omniray/)由 Comments 给出,未核查
- 🇨🇳 多数单目模型假设针孔相机,在鱼眼与全景图像上几何失真;相机感知模型用单一固定基表示射线场,难兼顾整体投影和细微变化。OmniRay 的 Ray Module 由单调径向基、球谐残差和自由形式残差三部分按球面连续旋转组合,给定单张图像预测每个像素的射线方向与尺度未知的径向距离,无需推理时的相机信息即可恢复点云。多种相机配置下的实验显示其在相机无关单目 3D 重建上达到新的最先进水平;摘要未给出具体数值。
- 🇬🇧 Monocular models mostly assume pinhole cameras and distort on fisheye/panoramic images; camera-aware ones use one fixed basis for rays. OmniRay's Ray Module composes a monotone radial base, a spherical-harmonic residual and a free-form residual as successive rotations on the sphere, predicting per-pixel ray directions and up-to-scale radial distance from one image without camera information at inference. Experiments across camera configurations claim a new state of the art; no numbers in the abstract.

### [A Sparse Topometric Graph for Scalable Cross-Session Indoor Navigation](https://arxiv.org/abs/2610.31432)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 稠密细粒度匹配计算与内存开销大、易受环境变化影响。本文提出稀疏拓扑度量图:节点编码局部 3D 几何,距离加权边表示可通行连接,学习的图匹配网络结合节点几何描述子与邻域连接寻找跨会话一致子图。在跨会话点目标导航中成功率最高(Gibson 77.1%,3D-FRONT 场景变化下 40.0%),内存比点级表示降低两个数量级以上,并支持跨会话对齐与真机迁移。
- 🇬🇧 Dense fine-grained matching is costly and fragile to scene changes. The sparse topometric graph encodes local 3D geometry at nodes and traversable connectivity on distance-weighted edges, with a learned graph-matching network finding consistent subgraphs across sessions. It achieves the highest cross-session point-goal navigation success (77.1% on Gibson, 40.0% under 3D-FRONT scene changes) with over two orders of magnitude less memory than point-level representations, plus cross-session alignment and real-world transfer.

### [Evaluation of Front-End Feature Matching for Lunar Visual SLAM](https://arxiv.org/abs/2610.30774)(Comments: submitted to 2027 IEEE Aerospace Conference)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 月球车在低纹理、强光照对比地形上的帧间特征匹配及其对 VO 的影响尚未被系统比较。本文在 9 个合成、月球试验场与地球类比数据集上基准测试 11 种经典/学习检测-匹配组合及一个特征跟踪器。纯旋转指标下 SuperPoint 组合在两个月球试验场和一个类比场地优于 SIFT+FLANN;联合评分旋转和平移方向时 SIFT 在四个合成数据集上超过两个 SuperPoint 组合;立体 VO 中只有 SuperPoint 组合在全部 8 个序列数据集上保持跟踪;SuperPoint+LightGlue 是最快的学习组合(每帧 16 ms)。
- 🇬🇧 Frame-to-frame matching on low-texture, harshly lit lunar terrain and its effect on VO has not been compared. The paper benchmarks 11 classical and learned detector–matcher combinations plus a tracker on nine synthetic, lunar-testbed and analogue datasets. Under a rotation-only metric SuperPoint pairings beat SIFT+FLANN on both lunar testbeds and one analogue site, but with joint rotation+translation scoring SIFT wins on four synthetic datasets; in stereo VO only SuperPoint pairings keep tracking on all eight sequential datasets, and SuperPoint+LightGlue is fastest (16 ms/frame).

### [Event-based SLAM Benchmark for High-Speed Maneuvers (EvSLAM)](https://arxiv.org/abs/2604.24033)(Replacement)
开源状态 / Code: ❓ 未知 / Unknown
- 🇨🇳 已有事件相机方法多针对近距快速抖动或纯 3 自由度旋转,未证明任意激进机动下基于事件的状态估计已被解决。本文分析最先进事件 VO/VIO 方法并报告现有公开数据集的缺陷,提出基准框架 EvSLAM,覆盖多种采集平台、极端光照与具挑战的运动模式,给出高速机动的严格定义和评估操作极限的新指标,并对最先进方法基准测试,总结最优架构与持续挑战(摘要未给出具体数值)。
- 🇬🇧 Event-camera methods target near-structure shaking or pure 3-DoF rotation, so arbitrary aggressive maneuvers are not shown solved. The paper analyzes SOTA event VO/VIO, reports dataset shortcomings, and introduces EvSLAM with varied platforms, extreme lighting, challenging motions, a rigorous definition of high-speed maneuvers and a new metric for operational limits, benchmarking SOTA methods; no numbers in the abstract.

**其余 1 条(列名)/ Remaining 1:** [AIM-SLAM(仓库,2★,密集单目 SLAM)](https://github.com/url-kaist/aim-slam) · 另见 radar new_repos:[z-localization](https://github.com/mozihe/z-localization)(62★,RoboMaster LiDAR-IMU 定位,非论文)

另见 / See also: [OASIS](https://arxiv.org/abs/2610.30589)(已归入 VLN)、[RangeNav](https://arxiv.org/abs/2610.29845)(已归入运动控制·RL)。

---

## 其他值得关注 / Other Notable

- [CENIC: Convex Error-controlled Numerical Integration for Contact](https://arxiv.org/abs/2511.08771)(Replacement,Comments: submitted to T-RO)— 变步长、误差受控的凸接触积分器,速度可比 MuJoCo/Drake/Isaac Sim 这类离散时间模拟器并提供精度与收敛保证。 / Variable-step error-controlled convex contact integrator running at real-time rates comparable to MuJoCo/Drake/Isaac Sim with accuracy and convergence guarantees. ❓ 开源未知 / code unknown.
- [AstroBench](https://arxiv.org/abs/2610.31064) — 自由漂浮捕获与太空机器人操作基准;冻结 π0.5 DROID 策略静态目标 2/200、运动目标 4/200,ACT 专用策略静态 8/10、运动 6/10。✅ [仓库](https://github.com/AstroUpLab/AstroBench)。
- [TerraTransfer++](https://arxiv.org/abs/2610.30319) — 无示范端到端驾驶规划;NAVSIM navhard 59.4 EPDMS、navtest 95.5 PDMS。❓。
- [To Route or to Adapt?](https://arxiv.org/abs/2610.31095)(已在具身类列名)。
- [PATH](https://arxiv.org/abs/2610.30605) · [ProTrav](https://arxiv.org/abs/2610.30839) · [TRACE(traversability)](https://arxiv.org/abs/2610.30994) — 越野/可通行性估计。 / off-road traversability.
- [Tactile-Based Robotic Manipulation: From Mechanics-Driven to Data-Driven Perspectives](https://arxiv.org/abs/2610.30438) · [GelSlim 5.0](https://arxiv.org/abs/2610.31334) · [OpenTac](https://arxiv.org/abs/2610.31661) · [VecTile](https://arxiv.org/abs/2610.31472) — 触觉感知与传感器。 / tactile sensing.
- 本类共约 14 条,不再展开。 / ~14 items, not expanded.

---

## GitHub 动态 / GitHub Highlights

**Star 增长最明显的相关仓库(radar `star_growth_top`,相对 2026-10-22 23:20 UTC 快照)/ Top star growth**

| 仓库 / Repo | Stars | 增长 / Δ | 说明 / Note |
|---|---|---|---|
| [Motphys/Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) | 80 | +50 | SuperMimic 的独立复现(UniLab,MuJoCo Warp),**第三方,非官方 / unofficial reproduction** |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28,435 | +31 | 端到端机器人学习框架 / end-to-end robot learning |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 8,447 | +27 | 多物理/多渲染器机器人学习框架 / unified robot learning framework |
| [suniique/assembly-nist](https://github.com/suniique/assembly-nist) | 33 | +29 | Franka 装配 PPO,AlphaNIST 的独立实现(第三方) |
| [TencentARC/Looking-Ahead](https://github.com/TencentARC/Looking-Ahead) | 86 | +27 | 自回归视频生成的未来演化建模(世界模型相关) |
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | 99,309 | +117 | WiFi 感知"空间智能"(与机器人弱相关,噪声) |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 59,360 | +251 | 浏览器空间数据可视化(与机器人无关,噪声) |

**新仓库精选 / Notable new repos(radar `new_repos`)**:[NEXUS](https://github.com/Gamma-Robot/NEXUS)(已入运动控制·RL)· [FRED](https://github.com/suhyeok-jang/FRED)(已入 WAM)· [CMAR-search](https://github.com/starry-curry-30/CMAR-search)(已入 VLN)· [TARSphere](https://github.com/xuyicheng-zju/TARSphere)(16★,长时序具身智能体全栈框架)· [RoboDoctor](https://github.com/THUSI-Lab/RoboDoctor)(12★,机器人策略免训练递归自改进)· [CofactVLA](https://github.com/zhangy0822/CofactVLA)(16★)· [ALPS](https://github.com/UCSC-VLAA/ALPS)(20★,世界模型视觉状态编码器)· [mjx-go2-training](https://github.com/TC635807/mjx-go2-training)(Go2 地形 locomotion,MJX+Brax PPO,个人项目)。多数为个人作业/学习项目,已忽略。

**新 Release / Releases(48 小时内,仅 2 条)**
- **[MuJoCo 3.17.0](https://github.com/google-deepmind/mujoco/releases/tag/3.17.0)**(2026-10-22):新增批量 API `mujoco.batch`(线程池并行步进同一模型的多个仿真,结果与顺序循环逐位一致);Flex 增加 1D 弹性杆弯曲弹性及插值 flex 自碰撞;`mj_setConst` 仅计算派生量;求解器终止准则改用惯量矩阵迹(`meaninertia` 弃用);`mju_boxQP` 增量 Cholesky 更快;多接触支持正 margin;含若干 API 变更(`mjs_fuseStatic`/`mjs_discardVisual` 返回计数,`mjs_addTexture` 增加默认类参数,`mjNEQDATA` 11→12)与纹理按引用、资产去重等。 / Batch API, 1D flex bending elasticity, interpolated-flex self-collision, faster `mju_boxQP`, several breaking API changes, texture/asset handling, bug fixes.
- **[Genesis v1.4.5](https://github.com/Genesis-Embodied-AI/genesis-world/releases/tag/v1.4.5)**(2026-10-22):显著加速精细凸分解/非凸几何的刚体仿真,轨迹录制开销降到多数情况 <20%,缓存改进(编译 kernel 跨会话保留、资产重载更快、SDF 约快 8 倍);破坏性变更:可微仿真支持普通 torch 张量与闭环策略、移除自定义 Genesis 张量;新增运行时连杆间解析螺旋约束;修复 AMD GPU(含 RDNA4)问题、CUDA 随机崩溃、碰撞 MPR→GJK 回退等。 / Faster rigid sim and recording, caching, differentiable-sim API changes, screw constraints, AMD/CUDA fixes.
- 其他重点项目(LeRobot、openpi、Isaac Lab、GR00T、ManiSkill 等)窗口内无新 release。 / No new releases for other watched projects in the window.

---

## 今日趋势 / Today's Trends

1. **接触 / 参考作为先验而非约束的人形控制。** 🇨🇳 [Humanoid Mobility via Attention-based Contacts](https://arxiv.org/abs/2610.31608)、[NEXUS](https://arxiv.org/abs/2609.39000)、[ReactiveBFM](https://arxiv.org/abs/2606.30362) 都把动作数据当先验,用接触规划、感知或闭环重规划让策略在偏离参考时仍能适应;[STAMP](https://arxiv.org/abs/2610.30817) 与 [STR](https://arxiv.org/abs/2610.30540) 则聚焦于参考本身的质量与衔接。 🇬🇧 Several humanoid works treat motion data as a prior rather than a constraint — contact planning, terrain perception or closed-loop replanning keep policies adaptive off-reference — while STAMP and STR improve the references themselves.
2. **灵巧手/双手跟踪走向"通用"。** 🇨🇳 [DONIC](https://arxiv.org/abs/2610.29997)(PPO + BC 回路)与 [PiHand](https://arxiv.org/abs/2610.31299)(潜在交互先验 + 残差 RL)都在把单任务灵巧跟踪推向跨物体、跨轨迹泛化。 🇬🇧 DONIC and PiHand push dexterous tracking from single tasks to generalist, cross-object policies.
3. **世界模型被"训练成对策略有用"。** 🇨🇳 [DRILL](https://arxiv.org/abs/2610.30814)、[DiffDreamer](https://arxiv.org/abs/2610.31617) 以及监测项 [SuperMimic](https://arxiv.org/abs/2610.28480) 都把世界模型与策略优化(GRPO、可微模拟)耦合;[UniFlowWAM](https://arxiv.org/abs/2610.30991)、[FRED](https://arxiv.org/abs/2610.30320)、[P³-WAM](https://arxiv.org/abs/2610.22363) 则强化 WAM 的几何与未来表征。 🇬🇧 World models are being trained for policy utility (DRILL, DiffDreamer, SuperMimic), while WAMs get richer geometry and future representations (UniFlowWAM, FRED, P³-WAM).
4. **Agent harness 自演化与 VLA 监控。** 🇨🇳 [Scale and Selection](https://arxiv.org/abs/2609.39304)、[SERA](https://arxiv.org/abs/2610.29560)、[FastHarness](https://arxiv.org/abs/2610.31427)、[AgenticRoboRL](https://arxiv.org/abs/2610.28589) 围绕 harness/规划器的自动改进;[Progress Probes](https://arxiv.org/abs/2610.31613)、[Echo](https://arxiv.org/abs/2610.31569) 关注运行时进度/失败监测。 🇬🇧 Harness self-evolution and planner post-training (Scale and Selection, SERA, FastHarness, AgenticRoboRL) plus runtime progress/failure monitoring (Progress Probes, Echo).
5. **VLA 推理提速与记忆。** 🇨🇳 [When One Step Is Enough](https://arxiv.org/abs/2610.30735)、[MambaAct](https://arxiv.org/abs/2610.22951)、[SmolVLA-MoE](https://arxiv.org/abs/2610.30732) 降低延迟;[UniMem](https://arxiv.org/abs/2608.22869)、[WholeBodyMem](https://arxiv.org/abs/2610.31166) 为非马尔可夫任务加记忆。 🇬🇧 VLA latency reduction (one-step, Mamba, MoE) and memory for non-Markovian tasks.

---

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
1. `agent harness` / `harness evolution`(arXiv 检索 + GitHub topic)— 🇨🇳 当日至少 5 篇([FastHarness](https://arxiv.org/abs/2610.31427)、[Scale and Selection](https://arxiv.org/abs/2609.39304)、[SERA](https://arxiv.org/abs/2610.29560)、[AgenticRoboRL](https://arxiv.org/abs/2610.28589)、[ERR-VLM](https://arxiv.org/abs/2610.27003))围绕"机器人智能体 harness/规划器自改进",现有关键词未覆盖。 🇬🇧 At least five papers today center on robot-agent harnesses and planner self-improvement, which current keywords miss.
2. `behavior foundation model`(arXiv 检索)— 🇨🇳 [ReactiveBFM](https://arxiv.org/abs/2606.30362) 与 [NEXUS](https://arxiv.org/abs/2609.39000)(感知行为基础模型)均以此命名人形通用控制器,属最高优先级主题。 🇬🇧 ReactiveBFM and NEXUS both frame generalist humanoid controllers as behavior foundation models, a top-priority topic.
3. `one-step action generation`(arXiv + GitHub)— 🇨🇳 [When One Step Is Enough](https://arxiv.org/abs/2610.30735)、[MambaAct](https://arxiv.org/abs/2610.22951),以及 radar 中的 [let-it-be-simple](https://github.com/bondtesty/let-it-be-simple)、[OSWAM](https://github.com/PolyU-VCLab/OSWAM) 都在做 VLA/WAM 的低延迟动作生成。 🇬🇧 Four items today pursue low-latency one-step action generation for VLAs/WAMs.

**建议观察 / Watch**
4. `recursive self-improvement`(物理 AI)— 🇨🇳 [Toward Recursive Self-Improvement in Physical AI](https://arxiv.org/abs/2610.29677)(HF 46 赞)与 [RoboDoctor](https://github.com/THUSI-Lab/RoboDoctor) 出现,信号尚弱,再看几天。 🇬🇧 A survey and a repo appeared; signal still weak.
5. `memory VLA` / 非马尔可夫记忆 — 🇨🇳 [UniMem](https://arxiv.org/abs/2608.22869)、[WholeBodyMem](https://arxiv.org/abs/2610.31166)、[Externalise the Memory](https://arxiv.org/abs/2610.30478) 三篇相关,尚未形成稳定术语。 🇬🇧 Three related papers, terminology not yet settled.

**建议移除/收窄 / Remove or Narrow:** 今日无建议(注:`legged locomotion`、`whole-body control`、`MPC`、`reinforcement learning robot` 的 API 短语检索当日 0 命中,但 cs.RO 列表中相关论文充足,说明是检索方式而非主题无产出;建议改用词干化或 `abs:` 字段检索而不是删除)。 / No removals; the 0-hit phrases reflect search mechanics rather than lack of output.

---

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 / Added | 当前状态 / Status | 今日检查 / Today | 备注 / Notes |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480)(CoRL 2026 Oral) | 2026-10-22 | ❓ 未知 / Unknown | signal=false;candidate_repos、项目页 GitHub 链接、release 声明、arXiv GitHub 链接均为空,errors 为空 | search_hits 15 条均为第三方复现(如 [Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) 80★ +50、[SuperMimicKit](https://github.com/OMEGA-i/SuperMimicKit)、[supermimic-m5](https://github.com/WXyuany/supermimic-m5) 等),不能据此判定官方开源;[项目页](https://supermimic.github.io)本次未能确认代码链接 |

**状态变化 / Changes:** 无。 / None.

**建议加入监测 / Suggested additions**

1. **[Humanoid Mobility via Attention-based Contacts](https://arxiv.org/abs/2610.31608)** — 🇨🇳 人形地形移动 RL 且完全依赖机载观测,价值高,当前无代码线索。 🇬🇧 High-value humanoid terrain-mobility RL with onboard-only deployment; no code signal yet.
2. **[STAMP](https://arxiv.org/abs/2610.30817)** — 🇨🇳 项目页已有 "Code" 标签但无链接,很可能即将放出。 🇬🇧 The project page already has an unlinked "Code" label, suggesting an imminent release.
3. **[RangeNav](https://arxiv.org/abs/2610.29845)** — 🇨🇳 已承诺 "Code and models will be open-sourced",尚无链接。 🇬🇧 Code and models promised, no link yet.

可直接粘贴的条目 / Ready-to-paste entries:

```json
[
  {
    "name": "Humanoid Mobility via Attention-based Contacts",
    "title": "Humanoid Mobility via Attention-based Contacts",
    "arxiv_id": "2610.31608",
    "search_terms": ["Humanoid Mobility via Attention-based Contacts", "attention-based contact planner humanoid"],
    "owners": [],
    "project_pages": [],
    "known_repos": []
  },
  {
    "name": "STAMP",
    "title": "Robot Motion Transition with Human Motion Prior",
    "arxiv_id": "2610.30817",
    "search_terms": ["STAMP humanoid motion transition", "Robot Motion Transition with Human Motion Prior"],
    "owners": ["childtoy"],
    "project_pages": ["https://childtoy.github.io/STAMP-project"],
    "known_repos": []
  },
  {
    "name": "RangeNav",
    "title": "RangeNav: Task-Aligned LiDAR Range-Image Pretraining for Robot Navigation",
    "arxiv_id": "2610.29845",
    "search_terms": ["RangeNav LiDAR range image", "RangeNav robot navigation"],
    "owners": [],
    "project_pages": ["https://rangenav.github.io/"],
    "known_repos": []
  }
]
```

**建议移出 / Suggested removals:** 无。 / None.

---

*自检 / Self-check:* ① 类别 1–2 全部展开(18 + 7);② 无"未读"占位;③ 展开条目均含开源状态行;④ 优先级 3–7 类别逐条核对:UniFlowWAM、FRED、P³-WAM、SkeLAM、DeXplicit、LaLa-World 等均为操作/表征层面的 WAM/世界模型,不涉及 locomotion/全身控制;DRILL、DiffDreamer、RangeNav、WholeBodyMem、HEX 已移入运动控制·RL;KinoUAV 与 OASIS 主贡献为 VLN 基准/地图,留在 VLN 并标注交叉;⑤ 已运行 arXiv API 关键词检索并记录命中数;⑥ release 条目已写主要更新;⑦ 已用脚本扫描链接格式。
