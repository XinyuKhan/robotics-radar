# 机器人/具身智能每日速递 — 2026-10-29 / Robotics & Embodied AI Daily — 2026-10-29

**检查窗口 / Window:** 台北时间 2026-10-28 ~07:40 → 2026-10-29 ~07:40(arXiv 取周三 10-28 的 cs.RO 列表,覆盖 10-26/27 UTC 提交)。 / Taipei time, roughly the last 24 h; arXiv Wednesday 28 Oct cs.RO listing (submissions of 26/27 Oct UTC).

> 本期无监测项开源,故无「🔔 监测项已开源」区块。radar 对 SuperMimic 再次报 `signal: true`,但唯一候选仍是与该工作无关的 `qiayuanl/claude-meter`(macOS 菜单栏应用),判定为误报;项目页与 arXiv 均无代码链接或承诺,状态保持「未知」。详见末节。 / No watchlist item was released. The radar again flagged SuperMimic only because of the unrelated `qiayuanl/claude-meter` repo; neither the project page nor arXiv gives a code link or promise, so the status stays Unknown (see last section).

## 来源状态 / Source Status

| 来源 / Source | 状态 / Status |
|---|---|
| arXiv cs.RO new 列表 / listing | ✅ 76 New + 9 Cross-lists = 85 条已逐条分类(其中约 60 条与主题相关);Replacements 40 条(其中与主题相关者列名,更新内容未逐条比对)。 / 85 classified; 40 replacements, relevant ones listed by name only (changes not diffed). |
| arXiv API 批量取全文摘要 / full abstracts | ✅ 116/116 取到非空摘要(85 条列表 + 18 条 API 额外命中 + 13 条替换版本);71 条有 Comments。 / 116/116 non-empty abstracts; 71 with comments. |
| arXiv API 关键词检索 / keyword search(cs.RO/AI/LG/CV;submittedDate ≥ 2026-10-27 00:00 UTC) | ✅ 命中数 / hits: embodied 11, VLA 9, vision-language-action 9, vision-language navigation 0, humanoid 8, legged locomotion 0, whole-body control 0, model predictive control 0, reinforcement learning robot 0, sim-to-real 3, dexterous manipulation 3, robot foundation model 1, world model 11, world action model 8, video world model 3, spatial intelligence 0, spatial reasoning 3, SLAM 4, visual SLAM 0, LiDAR SLAM 0, gaussian splatting SLAM 1, 3D reconstruction 4, motion tracking 1, motion imitation 0(短语精确匹配,故多个术语为 0)。合并去重后独有 51 篇,其中 18 篇不在 cs.RO 列表中。首次用「最近 24 小时」窗口得到 0 命中——因为所有新提交的日期均为 10-27,已改为日期窗口并重跑。 / Phrase-exact matching, hence several zeros; 51 unique hits, 18 not in the cs.RO list. A first run with a strict 24 h window returned 0 because all new papers are dated 27 Oct; re-run with a date window. |
| Hugging Face Daily Papers | ✅ 100 条;与主题相关且窗口内的:PDRVLA(138 赞,无仓库)、Hy-Nomas(104 赞,✅)、Rollback(50 赞,无仓库)、ThinkWorld(47 赞,无仓库)、RynnWorld-Latent(8 赞,✅)、JAM(3 赞,✅)。窗口外但带仓库:[ChronoReplay](https://arxiv.org/abs/2610.34283)(344 赞,流式空间智能,10-24)。 |
| GitHub radar(`data/latest.json`,date_taipei = 2026-10-29) | ✅ 已更新;new_repos 150 条(筛选后少量入选)、star_growth_top、oss_watch 1 项;star 基线为 2026-10-27,增长为相对前一日快照;`watchlist_releases` 1 项。 |
| 项目页核验 / Project pages (WebFetch) | ✅ 已查 SuperMimic、GRAFT、REACH、DexSafe、CARD、MyoAcross、TAPESTRY、Trace-WAM、ThinkWorld、R2A、MoGAP、RoboAuto、Rollback 项目页;`git ls-remote` 验证了 11 个声称的仓库。 |
| 入选篇数 / Selected | 约 95 条相关(含替换版本);详细展开 70 篇,其余约 25 条列名。 |

## 今日必读 / Top Picks

1. **[Whole-Body Humanoid Control via Stochastic Motion Tokenization](https://arxiv.org/abs/2610.36452)** — ❓ 未知 / Unknown · 运动控制·RL。随机运动 tokenizer 超过 FSQ/VQ-VAE,离散接口驱动 G1 真机执行 16.8 s 的舞蹈/格斗/行走与 35 s 格斗转舞蹈序列。 / A stochastic motion tokenizer beating FSQ and VQ-VAE drives a physical G1 through 16.8 s dance/fight/walk clips and a 35 s fight-to-dance sequence.
2. **[GRAFT](https://arxiv.org/abs/2610.36507)** — ❓ 未知 / Unknown · 运动控制·RL。冻结的人形行为基础模型(含 SONIC)加轻量残差适配器即可过楼梯/间隙/平台,G1 真机仅用机载深度。 / A lightweight residual adapter on frozen humanoid behavior trackers (incl. SONIC) enables terrain traversal on a real G1 with onboard depth only.
3. **[Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well](https://arxiv.org/abs/2610.37652)** — 🕒 计划开源 / Planned · 运动控制·RL。LEAP 手纯仿真训练零样本上真机,13.3 小时、4,800 个目标上 95.2% 达成,安全滤波器将掉落减少 75%。 / Sim-only LEAP-hand policy, zero-shot to real: 95.2% of 4,800 goals reached in 13.3 h; the safety filter cuts drops by 75%.
4. **[Rollback](https://arxiv.org/abs/2610.36068)** — ❓ 未知 / Unknown · 运动控制·RL(交叉:世界模型)。把世界模型当「反事实引擎」回溯到关键决策点做策略改进,三个真机任务绝对提升约 10.7–11.9 个百分点。 / A world model used as a counterfactual engine for policy improvement; +10.67/11.11/11.85 points on three real-robot tasks.
5. **[Just Action Models (JAM)](https://arxiv.org/abs/2610.37219)** — ✅ 已开源 / Released · VLA(交叉:WAM)。把 VLA 与 WAM 之争拆成三个独立选择,无需视觉生成即超过 FastWAM,训练 FLOPs 降 73%。 / Decouples the VLA-vs-WAM debate into three choices; beats FastWAM without visual generation at 73% fewer training FLOPs.

---

## 运动控制·RL / Motion Control · RL(全部展开 / all expanded:23)

### [Whole-Body Humanoid Control via Stochastic Motion Tokenization](https://arxiv.org/abs/2610.36452) — Drolet, Arenz, Peters(Humanoids 2026 接收)
开源状态 / Code: ❓ 未知 / Unknown(Comments 仅注明会议接收,无代码链接或承诺)
- 🇨🇳 速度指令 RL 策略对人形而言接口过窄,而全身动作跟踪策略又缺乏未来动作信息,难以做受控偏离以服务长期任务。该工作用高层控制器按行为标签或文本生成紧凑的运动表示(token),直接喂给跟踪策略作为详细参考。在同等容量下,随机运动 tokenizer 对 Unitree G1 动作的重建优于 FSQ 与 VQ-VAE;该离散接口驱动的跟踪策略在 G1 真机上执行了各 16.8 秒的舞蹈、格斗、行走以及 35 秒的格斗转舞蹈序列。
- 🇬🇧 Velocity-commanded RL policies are a narrow interface for humanoids, and whole-body tracking policies see little of the future motion, limiting controlled deviations. The paper generates compact motion tokens from a behavior label or text command with a high-level controller and feeds them to a tracking policy as a detailed reference. At matched capacity, the stochastic tokenizer reconstructs Unitree G1 motions better than FSQ and VQ-VAE, and the discrete interface drives tracking policies through 16.8 s dance, fight and walk motions and a 35 s fight-to-dance sequence on a physical G1.

### [GRAFT: Geometry-Aware Residual Adaptation for Foundation Trackers](https://arxiv.org/abs/2610.36507) — Li, Zhang, Chen 等
🏷️ 交叉方向 / Also: 具身智能与机器人基础模型(行为基础模型)/ Behavior foundation models
开源状态 / Code: ❓ 未知 / Unknown(已核查[项目页](https://graft-humanoid.github.io/),无代码链接或承诺)
- 🇨🇳 人形行为基础模型(BFM)多在平地动作上训练,缺少按地形调整落脚、摆动离地与接触时序的机制;现有地形感知方案要联合重训跟踪器与感知,代价高。GRAFT 冻结 BFM 参数与动作参考接口,仅用轻量适配器对下肢执行目标加地形条件修正,以任务与足部几何奖励训练,在平地上正则化抑制多余修正,并把特权地形观测蒸馏到机载深度。在四个冻结跟踪器上于仿真中评测楼梯、间隙与平台,并在 Unitree G1 真机上让适配后的 SONIC 跟踪器仅凭机载深度与未修改的参考完成地形穿越;摘要未给出具体数值。
- 🇬🇧 Humanoid behavior foundation models (BFMs) are trained mostly on flat-ground motion and lack a way to adapt foot placement, swing clearance and contact timing to terrain; retraining them jointly with perception is costly. GRAFT freezes the BFM and its reference interface and adds a lightweight adapter that corrects only lower-body execution targets, trained with task and foot-geometry rewards, regularized to stay silent on flat ground, and distilled from privileged terrain observations to onboard depth. It is instantiated on four frozen trackers and tested on stairs, gaps and platforms in simulation, and on a real Unitree G1 the adapted SONIC tracker traverses terrain with onboard depth and unmodified references; the abstract gives no numbers.

### [REACH: An RL-based Hierarchical Humanoid Crawling Framework for Adaptable Confined Space Traversal](https://arxiv.org/abs/2610.36546) — Xu, Guo, Hu, Xu 等(Humanoids 2026)
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://aislab-sustech.github.io/REACH/)标注「Code To be released」,无仓库链接(摘要写「Code and videos are available at」项目页,但页面本身只有承诺)
- 🇨🇳 受限空间中的人形运动需要连续调节身高并跨多种运动模式,现有方法多局限于变高度双足行走。REACH 是分层 RL 框架:变高度双足行走(身高指令 1.27–0.50 m)与爬行(0.50–0.20 m)两组策略,用历史条件隐表示从本体感觉中捕获地形与交互上下文,双向过渡策略连接屈膝行走与爬行,并接入基于 LiDAR 点云的三维无碰撞规划器(含主动身高目标)。Unitree G1 真机实验展示了准确的身高/速度跟踪、稳健的地形穿越、可靠的模式切换与受限空间穿越。
- 🇬🇧 Confined-space humanoid locomotion needs continuous height adaptation across modes, yet most work is limited to height-adjustable bipedal walking. REACH is a hierarchical RL framework: policies for variable-height walking (1.27–0.50 m command range) and crawling (0.50–0.20 m), a history-conditioned latent capturing terrain and contact context from proprioception, a bidirectional transition policy, and a LiDAR-based 3D planner issuing paths and proactive height targets. Real Unitree G1 experiments show accurate height/velocity tracking, robust terrain traversal, reliable mode transitions and confined-space traversal.

### [Learning Multi-Phase Robot Loco-Manipulation via Phase-Conditioned Policy Optimization](https://arxiv.org/abs/2610.36270) — Manni, Wollschläger, Bellicoso, Gawel
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 蹲伏、抓取、行走交织的长时程全身 loco-manipulation 目前多依赖人类动作数据与人形平台,限制了平台通用性并带来数据处理开销。该工作扩展 PPO:相位条件化 critic、相位门控奖励与多相位重置课程来引导探索,并用解耦的分层控制架构把底层平衡动力学与高层相位执行分开,以支持不同硬件。在 Unitree G1 与带机械臂的 Boston Dynamics Spot 两个真机上演示了多阶段 loco-manipulation 技能,并通过消融验证设计;摘要未给出定量结果。
- 🇬🇧 Long-horizon whole-body loco-manipulation (crouching, grasping, walking) usually relies on human motion data and humanoid platforms, limiting generality. The paper extends PPO with a phase-conditioned critic, phase-gated rewards and a multi-phase reset curriculum, plus a decoupled hierarchical controller separating low-level balance from high-level phase execution. Multi-stage skills are demonstrated on hardware on both a Unitree G1 and a Spot with an arm, with ablations; the abstract reports no numeric results.

### [HC2Robot: Hyper-Connection Transformers with Predicted Foresight for Multi-Terrain Humanoid Parkour](https://arxiv.org/abs/2610.36825) — Xu, Mai, Fu, Zheng 等
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 感知式人形跑酷中,非对称 actor-critic 的 critic 使用仿真特权信号而可部署的 actor 仅有机载感知,存在信息差。HC2Robot 的思路不是把特权信息给 actor,而是学习其可部署近似:预测足部落地的时机、位置与支撑质量的 Predicted Foresight Module,加上具备可学习多流路由的 Hyper-Connection Transformer 和未来动作预测头作正则。在楼梯、间隙、高平台、斜坡上平均仿真穿越成功率 97.60%,且安全落脚率持续高于强感知式基线;摘要未提真机。
- 🇬🇧 In perceptive humanoid parkour, asymmetric actor-critic gives the critic privileged simulator signals while the deployable actor only has onboard perception. HC2Robot learns a deployable approximation instead: a Predicted Foresight Module forecasts each foot's next touchdown timing, location and support quality, a Hyper-Connection Transformer adds learnable multi-stream routing, and a future-motion head regularizes. It reaches 97.60% mean simulated traversal success across stairs, gaps, platforms and slopes with higher safe-foothold rates than strong baselines; no hardware results are stated.

### [Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well](https://arxiv.org/abs/2610.37652) — Chuang, Shah, Chilamkur, Soltani
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://ian-chuang.github.io/dexsafe/)标注「Code: coming soon」,无仓库链接与检查点说明
- 🇨🇳 已有灵巧手技能多限于简单抓取或旋转,且「不掉物」这类安全性很少被度量。该工作研究任意手腕朝向下把物体移到任意位姿的连续多目标任务,给出无人类数据的 LEAP 手仿真训练配方(生成抓取数据集带来的多样重置与目标、自适应摩擦课程),配合系统辨识零样本迁移真机,并在任务策略上叠加可调保守度的学习型残差安全滤波器。13.3 小时、4,800 个未见目标、4 种物体的真机评测中,状态策略在 2 cm/0.4 rad 内达成 95.2%;滤波器将掉落减少 75% 同时仍达成 91.5%;仅需腕部相机还能拧灯泡。
- 🇬🇧 Learned dexterous skills are mostly simple grasps or repeated motions, and safety (not dropping the object) is rarely measured. The paper tackles in-hand pose reaching to arbitrary poses at any wrist orientation with a human-data-free LEAP-hand sim recipe (diverse resets/goals from generated grasps, adaptive friction curriculum), zero-shot transfer after careful system identification, and a learned residual safety filter with adjustable conservativeness. Over 13.3 h and 4,800 unseen goals on 4 objects, the state-based policy reaches 95.2% within 2 cm and 0.4 rad; the filter cuts drops by 75% while still reaching 91.5%; a wrist camera suffices for tasks like screwing in a lightbulb.

### [Learning Visuomotor Quadrotor Flight Through Dynamic Narrow Gaps via Differentiable Simulation](https://arxiv.org/abs/2610.37557) — Bianco, Ren, Xing, Scaramuzza(CoRL 2026)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 穿越移动窄缝要求厘米级对准与精确时序,现有方法依赖特权状态、教师、规划器或蒸馏,从零直接学习仍是开放问题。该工作提出可微的移动缝隙形式化:用到时变缝隙平面的有符号距离门控居中、对齐与平滑碰撞项,把稀疏的穿越事件变成稠密路径目标,并训练从视觉特征到推力/机体角速度指令的单阶段策略。受控基准中路径梯度显著优于 score-function 梯度,单 GPU 训练几分钟后仿真成功率 99.3%;策略直接迁移到真机,10 次物理试验成功 80%。
- 🇬🇧 Threading a quadrotor through a moving narrow gap needs centimeter-level alignment and precise timing; prior work relies on privileged state, teachers, planners or distillation. The paper builds a differentiable moving-gap formulation that gates centering, alignment and smooth collision terms by signed distance to the time-varying gap plane, turning a sparse event into a dense pathwise objective, and trains a visual-feature-to-command policy in one stage from scratch. Pathwise gradients beat score-function gradients, reaching 99.3% success in simulation after minutes on one GPU, and the policy transfers to a real quadrotor with 80% success over 10 trials.

### [Rendering-Free Event Frame Simulation for Fast Reinforcement Learning of Autonomous Robot Navigation](https://arxiv.org/abs/2610.37543) — Ou, Lopez, Missinne, De Wagter 等
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/tudelft/rendering-free-event-nav);摘要给出,已用匿名 `git ls-remote` 验证
- 🇨🇳 事件相机适合微型无人机,但现有模拟器先渲染真实感图像再转事件,使大规模 RL 极慢。该工作利用事件相机本质上测量运动对比度边缘,直接由场景几何与自运动解析合成事件流,在单 GPU 上 17 微秒生成 64×64 事件观测,比最先进渲染管线快 400 倍以上,避障 RL 在 30 分钟内收敛。策略零样本迁移到光线追踪的 Isaac Sim,在未见杂乱场景成功率 83%(平均目标速度 2.4 m/s);量化为 1.2 MB int8 后在 56 克 Crazyflie 上全机载运行,三条真实赛道平均成功率 82%。
- 🇬🇧 Event cameras suit tiny drones, but simulators render photorealistic frames before converting to events, making large-scale RL prohibitively slow. The analytic simulator synthesizes events directly from scene geometry and ego-motion (a 64×64 observation in 17 µs on one GPU, >400× faster than a rendering pipeline), so obstacle-avoidance RL converges in under 30 minutes. Policies transfer zero-shot to ray-traced Isaac Sim with 83% success on unseen cluttered courses at 2.4 m/s, and a 1.2 MB int8 policy runs fully onboard a 56 g Crazyflie, achieving 82% average success over three real courses.

### [A Trainable CPG Framework for Quadruped Locomotion](https://arxiv.org/abs/2610.36537) — Liu, Liu, Mao, Qu
🏷️ 交叉方向 / Also: 运动控制·传统(CPG)/ Classical (CPG)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 四足多步态控制通常需要为各步态或步态转换单独设计学习控制器与奖励。CPG-ENN 用基于对称性的八神经元 CPG 提供步态节律,由预训练、腿间共享的执行网络把节律信号与轨迹参数映射为关节角参考(无需在线逆运动学),单一反馈策略调制六个物理可解释的轨迹变量,覆盖 walk、trot、pace、bound、pronk。仿真中 20 个有向步态对在 {0.5,1.0,1.5,2.0} m/s 组合上转换成功率 99.39%,与 AllGaits、Walk These Ways 对比速度调节精确,Unitree Go2 真机验证了五种步态及转换。
- 🇬🇧 Multi-gait quadruped control usually needs separate learned controllers or transition rewards per gait. CPG-ENN uses a symmetry-based eight-neuron CPG for rhythm and a pretrained leg-shared execution network mapping rhythm and trajectory parameters to joint references without online IK, with a single feedback policy modulating six interpretable trajectory variables across walk, trot, pace, bound and pronk. Simulation shows 99.39% transition success over all 20 directed gait pairs and speed combinations from {0.5,1.0,1.5,2.0} m/s, it compares favorably with AllGaits and Walk These Ways, and Unitree Go2 experiments validate five gaits and transitions.

### [Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos](https://arxiv.org/abs/2610.36615) — Le, Nguyen, Tran, Pham 等
🏷️ 交叉方向 / Also: 数据集 / Dataset(HumiMimic)——归入运动控制因其目标是人形动作模仿的可执行参考,但核心贡献是重定向与数据,非策略训练。
开源状态 / Code: ❓ 未知 / Unknown(摘要提到 HumiMimic 数据集,未给出链接或承诺)
- 🇨🇳 让人形与人类伙伴自然交互(拥抱、跳舞、握手)需保留动作之间的空间、语义与接触关系,并能跨不同人形本体泛化。HumiTransfer 从野外双人交互视频重建带一致足地接触的 3D 人体动作,通过加权关节相对方向与解剖偏移的交互建模迁移到目标人形,并用后重定向优化强制平衡、接触与避碰。应用于 1,200 个视频得到约 50 万帧、面向 26-DoF Unitree R1 Edu 与 23-DoF HighTorque Mini-hi 的 HumiMimic 数据集;两机上动作保真度、身体间关系与接触精度均优于基线,真机部署确认了可执行性。
- 🇬🇧 Natural human–humanoid interaction (hugging, dancing, hand-shaking) must preserve spatial, semantic and contact relations and generalize across embodiments. HumiTransfer reconstructs 3D human motion with consistent foot-ground contact from in-the-wild two-person videos, transfers one participant to a target humanoid via interaction modeling (weighted joint-relative directions, anatomical offsets), and refines with balance, contact and collision constraints. Applied to 1,200 videos it yields ~500,000 frames (HumiMimic) for the 26-DoF Unitree R1 Edu and 23-DoF HighTorque Mini-hi, beats baselines in fidelity, inter-body relations and contact accuracy, and real deployments confirm executability.

### [Remember Where You Walk: Learning Spatial Memory for End-to-End Legged Robot Exploration](https://arxiv.org/abs/2610.37203) — Magnus, Bohlinger, Peters, Arenz
🏷️ 交叉方向 / Also: 空间智能与 SLAM(空间记忆、探索)/ Spatial memory & exploration
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 足式/人形机器人需要记住已离开视野、很久以后才相关的信息,而 LSTM 等记忆网络在长时程上常保留不足。该工作提出基于 Hadamard 记忆的 Local Spatial Matrix Memory(LSMM),让 RL 智能体把任务相关信息存入按位置寻址的记忆单元,实现空间落地的灵活记忆。在自主迷宫探索任务上,LSMM 与强循环/有限历史基线的迷宫覆盖率相当,但是唯一能记住迷宫布局的架构,重建误差降低三倍;摘要未提真机。
- 🇬🇧 Legged robots must remember information that left the field of view and matters much later, but LSTM-style memories often fail over long horizons. The paper proposes Local Spatial Matrix Memory (LSMM), a Hadamard-memory architecture letting RL agents store task-relevant information at position-based memory cells. On autonomous maze exploration it matches the coverage of strong recurrent and finite-history baselines while being the only architecture that remembers the layout, cutting reconstruction error threefold; no hardware results are stated.

### [Multi-Agent Reinforcement Learning of Co-Adaptive Hip Exoskeleton Control (MARL-Exo) for Metabolic Energy Reduction](https://arxiv.org/abs/2610.37441) — Yuan, Wolf, Androwis, Zhou
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 髋外骨骼的助力通常需逐用户人在回路调参。MARL-Exo 用多智能体 RL 在仿真中让全身人体模型(304 个肌肉驱动,随机化解剖、步态与速度)与双侧髋外骨骼策略两阶段并发训练,奖励含肌肉代谢功率(可加机械功率塑形),外骨骼只观测延迟的髋运动学和自身历史指令。仿真中代谢策略使建模肌肉代谢功率降低 13.8%(加功率塑形为 8.8%);8 名健康成人以 1.25 m/s 行走的间接量热测试中,无需重训即相对被动模式净代谢率降低 18.3±6.6%(全部 8 人),相对不穿戴降低 7.4±10.0%。
- 🇬🇧 Hip-exoskeleton assistance usually needs per-user human-in-the-loop tuning. MARL-Exo trains, in two stages, a 304-muscle full-body human model (randomized anatomy, gait, speed) and a bilateral hip-exoskeleton policy concurrently with a metabolic-energy reward (optionally with mechanical-power shaping); the exoskeleton sees only delayed hip kinematics and its past commands. In simulation the Metabolic policy cut modeled metabolic power by 13.8% (8.8% with power shaping); on 8 adults walking at 1.25 m/s without retraining it reduced net metabolic rate by 18.3±6.6% vs. Passive in all eight and 7.4±10.0% vs. No-Exo.

### [A generalist policy for muscle-driven control across individual musculoskeletal models (MyoAcross)](https://arxiv.org/abs/2610.36535) — Wang, Zhu, Li, Zhang 等
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://woodater-thu.github.io/MyoAcross/)标注「Code (Coming soon)」,无仓库链接
- 🇨🇳 肌肉骨骼形态差异使控制策略难以在个体模型间复用。MyoAcross 结合个体肌肉骨骼模型构建、形态条件化策略学习与虚拟模型增广,实现无需个体微调的肌肉驱动参考动作跟踪。在 31 个留出的个体模型上完成率 99.24%、跟踪误差比无条件 MLP 降低 22.60%;可复用到由单图形状估计、身高体重构建的 22 个留出个体,加不对称增广后可扩展到单侧下肢缩短的模型,并与 120 名额外个体的垂直地面反力波形及肌电做了对比。
- 🇬🇧 Morphological differences across individuals hinder policy reuse across musculoskeletal models. MyoAcross combines individual model construction, morphology-conditioned policy learning and virtual model augmentation for muscle-driven reference-motion tracking without per-individual fine-tuning. On 31 held-out individual models it achieves 99.24% completion and 22.60% lower tracking error than an unconditioned MLP; reuse extends to 22 held-out individuals built from single-image shape estimates, height and mass and, with asymmetry augmentation, to unilateral lower-limb shortening, with agreement to ground reaction force waveforms and EMG from 120 additional individuals.

### [CARD: Contact-Anchored Retargeting for Dexterous Manipulation](https://arxiv.org/abs/2610.36539) — Dai, He, Hogan, Pan
🏷️ 交叉方向 / Also: 具身智能(人类数据迁移)/ Embodied data transfer
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://card-retargeting.github.io/)的「Code」按钮为占位链接,提示「Link to come」
- 🇨🇳 现有灵巧手重定向只平移运动学、忽略接触动力学,导致任务失败。CARD 是无需仿真器与物体的框架,通过共享手—接触表示统一视频、动捕与触觉手套数据,在运动学之外生成显式接触力目标,并用触觉跟踪控制器在硬件开环回放时维持接触;视频端提出 Vid-HACO 视频到接触模型(自称新 SOTA)。在视频、手套、动捕与 GRAB 数据上维持 43–78% 的接触帧,而运动学与物体感知重定向分别 <10% 与 22.5%;融入物理重定向后 GRAB 严格任务成功率由 12% 升至 32%。
- 🇬🇧 Existing dexterous retargeting translates kinematics but ignores contact dynamics. CARD is a simulator- and object-free framework that unifies video, mocap and tactile-glove data through a shared hand–contact representation, generates explicit contact-force targets, and adds a tactile tracking controller for open-loop hardware replay; Vid-HACO is its video-to-contact model. It maintains contact on 43–78% of contact frames vs. <10% (kinematic) and 22.5% (object-aware) baselines, raises strict task success on GRAB from 12% to 32% when integrated into physics-based retargeting, and the tactile tracker is critical for reproducing forces on hardware.

### [Rollback: Experience Backtracking in World Models for Policy Improvement](https://arxiv.org/abs/2610.36068) — Luo, Zhang, Chen, Wang 等
🏷️ 交叉方向 / Also: 世界模型与 WAM / World Models
开源状态 / Code: ❓ 未知 / Unknown(已核查[项目页](https://rollback-wm.github.io/),只有论文链接,无代码或承诺)
- 🇨🇳 动作条件世界模型可替代昂贵的真实交互来改进机器人策略,但现有方法只把它当前向模拟器,浪费了「回退到过去决策点探索反事实」这一真实环境不具备的能力。Rollback 把世界模型变成反事实引擎:回退到关键决策点,分支到不同动作并对比结果,把成败归因到单个决策,无需单独的价值模型即得到动作级监督;并构建了分布式世界模型搜索与异步真机执行的训练系统,用轻量 LoRA 以真实转移修正世界模型动力学(「测试时物理落地」)。三个真机任务(block extraction、ball tossing、tabletop curling)相对最强基线分别绝对提升 10.67%、11.11%、11.85%,且在 8 小时内在 ball tossing 与 curling 上超过人类玩家平均成功率。
- 🇬🇧 Action-conditioned world models can replace costly real interaction for policy improvement, but existing methods treat them as forward-only simulators, ignoring the ability to rewind to past decision points. Rollback rolls back to critical decisions, branches into alternative actions and contrasts outcomes to attribute success to individual decisions, yielding action-level supervision without a learned value model; a distributed system couples world-model search with asynchronous real-robot execution, and a lightweight LoRA pipeline corrects the world model with real transitions. On three real tasks it improves on the strongest baseline by an absolute 10.67%, 11.11% and 11.85%, and surpasses average human success on ball tossing and tabletop curling within 8 hours of training.

### [VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning](https://arxiv.org/abs/2610.37378) — Zou, Yu, Li, Lin 等
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 多数 VLA 面向静态操作,忽略空间约束与动态障碍;在避障数据上微调成本高且可能损害原任务能力。VLA-Stem 不微调底层 VLA,而是把其动作块转为运动参考,以轨迹级引导保留空间意图,Stem 策略再结合参考、本体感觉与局部障碍信息在推理时自适应修改执行,训练结合师生蒸馏与课程学习(RL)。六个受约束仿真设置中无碰撞任务成功率平均 52.8%,最强安全基线为 23.7%,且无障碍场景下保持基础策略性能;真机实验在静态与动态障碍下碰撞一致减少。
- 🇬🇧 Most VLAs target static manipulation and ignore spatial constraints and dynamic obstacles; fine-tuning on obstacle-avoidance data is costly and can degrade original skills. VLA-Stem leaves the VLA frozen, converts its action chunks into motion references with trajectory-level guidance, and an RL-trained Stem policy conditioned on the reference, proprioception and local obstacle information modifies execution at inference time (teacher-student distillation plus curriculum). Across six constrained simulation settings it reaches 52.8% collision-free task success vs. 23.7% for the strongest safety baseline while preserving base performance without obstacles, and real-world runs show consistent collision reductions.

### [When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies (ARC)](https://arxiv.org/abs/2610.37547) — Singh, Caniot, Tokekar, Abi-Farraj
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 模仿策略常在局部区域需要「最后一厘米」精度时失败,而更新整个策略或处处探索残差是把局部问题当全局问题。ARC 是轻量后训练模块:用 RL 在冻结策略之上学习残差修正,稀疏的人类纠正不当作模仿目标,而是用干预前状态决定「何时」激活残差、纠正几何决定「何处」探索,任务奖励决定最终「执行什么」。三个真机精密操作任务的平均成功率由 33.3% 提升到 75.0%;人类纠正定义的 2–3 维子空间保留七关节残差空间中 96.0–97.7% 的平方纠正量。
- 🇬🇧 Imitation policies often fail in localized regions needing last-mile precision, and updating the whole policy or exploring residuals everywhere treats a local failure as a global problem. ARC learns, with RL, a residual correction on top of a frozen policy, using sparse human corrections not as imitation targets but to decide when the residual activates (pre-intervention states) and where to explore (correction geometry), while task reward decides what residual is executed. On three real precision tasks average success rises from 33.3% to 75.0%, and the corrections define 2–3-D subspaces of the seven-joint residual space retaining 96.0–97.7% of squared correction magnitude.

### [Autonomous fixed-wing interception using reinforcement learning](https://arxiv.org/abs/2610.37470) — van Hamersveld, Smeur, Kriachko(MSc 论文,TU Delft)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 固定翼拦截机目前仍靠人工操纵,四旋翼拦截器续航太短。该工作训练一个把滤波后的单目视觉观测直接映射到执行器指令的神经网络策略,在自定义 Python 环境中用 PPO 训练,并开发了两种经典制导控制器作基线。策略在仿真中多数条件下优于经典控制器,并在真机飞行中成功拦截了机动的固定翼目标;摘要未给出具体拦截率数值。
- 🇬🇧 Fixed-wing interceptors are still flown manually while quadcopter interceptors lack endurance. The thesis trains a neural policy mapping filtered monocular vision directly to actuator commands with PPO in a custom Python environment, with two classical guidance controllers as baselines. The policy beats the classical controllers in most simulated conditions and was validated in real flights by intercepting maneuvering fixed-wing targets; the abstract gives no numeric rates.

### [Predict the Swing, Match the Speed: Robotic Pipe Stabbing With Learned Stereo Vision and Residual Reinforcement Learning](https://arxiv.org/abs/2610.37535) — Mostafa, El-Fakharany, Khaled
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 钻井管柱摆动着撞向固定对接导向器,传统固定导向器常有冲击。StabBot 用摆锤卡尔曼滤波在立体图像中跟踪管柱,六轴机械臂以匹配速度逼近并触觉确认,ResNet-18 关键点网络做 3D 定位,残差 RL 策略精修捕获。200 个随机任务上全部对接成功(管只接触滚轮),而固定导向器为 74%;中位接触速度从 18.4 降到 2.3 cm/s,中位峰值力从 11.3 降到 1.4 kN;网络定位中位误差 0.4 mm、每对立体图 2.3 ms;所有结果来自 1:4 Froude 缩比 MuJoCo 模型(仿真,无真机)。
- 🇬🇧 Swinging drill pipe strikes a fixed stabbing guide at whatever speed the swing has. StabBot tracks the joint with a pendulum Kalman filter on stereo images, closes in with a six-axis arm at matched velocity, confirms by touch, locates the pipe with a ResNet-18 keypoint network, and refines capture with a residual RL policy. On 200 paired random jobs it seated every joint with the pipe touching only rollers (vs. 74% for a fixed guide), cutting median contact speed from 18.4 to 2.3 cm/s and median peak force from 11.3 to 1.4 kN, with 0.4 mm median localization error at 2.3 ms; all results come from a 1:4 Froude-scaled MuJoCo model, i.e. simulation only.

### [When Black-Box Robot Policies Fail: Online Sensor Diagnosis and Repair with a Transparent Surrogate](https://arxiv.org/abs/2610.36852) — Ziegler, Özen, Mentes, Waschulzik(CoRL 2026 SPAIS 研讨会)
开源状态 / Code: ❓ 未知 / Unknown(Comments 仅注明研讨会接收,无代码链接或承诺)
- 🇨🇳 机器人基础模型依赖可能失效的传感器,当策略冻结或不可访问时,外部监控器能否诊断并修复被污染的输入?该工作测试一种把周期步态与传感器相关修正分离的结构化透明代理,用于指导围绕冻结运动策略的输入修复。仿真 Go2 上离线诊断使行走成功由 259/640 提升到 429/640,在线修复达 382/640,64 个无故障留出回合无误触发;同等预测精度的提升树代理却没有可检测的修复收益;单独拟合也改善了 Go1 与 ANYmal C。作者指出证据仅限一个策略与部分筛选过的仿真故障集,真机验证尚待开展。
- 🇬🇧 Robot foundation models depend on sensors that can fail; when the policy is frozen, can an external monitor diagnose and repair corrupted inputs? A structured surrogate separating periodic gait from sensor-dependent corrections guides input repair around a frozen locomotion policy. On simulated Go2, offline diagnosis raises walking success from 259/640 to 429/640 and online repair reaches 382/640 with no triggers in 64 fault-free episodes, whereas a matched boosted-tree surrogate yields no repair gain; separate fits also help Go1 and ANYmal C. The authors note evidence is limited to one policy and a partly screened simulated fault suite, with hardware validation open.

### [Bridging Exploration and Loss of Plasticity in On-Policy Reinforcement Learning](https://arxiv.org/abs/2610.36309) — Grieco, D'Elia, Caldarelli, Camoriano(cross-list)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 深度 RL 会丧失对新数据的适应能力(Loss of Plasticity, LoP),其因果机制与几何条件尚不清楚。该工作分析各向同性高斯策略下 PPO 的 LoP,报告多项刻画策略标准差 σ 影响的指标,并对常用缓解技术的有效性给出解释。结果显示 σ 对 LoP 程度有显著影响,并有理论与实验支持;实验包括 LoP 基准对比以及 7-DoF 机械臂的真机策略部署(摘要未给出具体数值)。
- 🇬🇧 Deep RL loses the ability to learn from new data (Loss of Plasticity, LoP), and its causal mechanism is unclear. The paper analyzes LoP in PPO with isotropic Gaussian policies, reports metrics showing the effect of the policy standard deviation σ, and explains why common mitigations work. σ has a significant effect on LoP, backed by theory and experiments including LoP benchmarks and real-world deployment on a 7-DoF arm; the abstract gives no numbers.

### [Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent (ZAP)](https://arxiv.org/abs/2610.35817) — Pikus, Saunders, Mironenco 等(替换版本 / revised version)
🏷️ 交叉方向 / Also: VLA / 具身基础模型(以 VLM 控制机器人)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 机器人策略既要理解任务也要知道如何移动。Zero-real Agent Policy (ZAP) 用一个 27B 预训练模型提供世界理解与推理,再通过简单工具接口,在仿真简单任务上做监督微调加 GRPO 教它如何移动机器人,全程不使用真机数据。真实世界任务成功率 96.7%,与 GPT-6 Astra(在同一接口中)持平并超过 MolmoAct2 VLA 的 33.3%,速度快 3 倍、成本低 17 倍;还能泛化到未见本体、新物体与策略;单臂 Franka 在 RoboLab-120 上 55.9%,比领先的 VLA/WAM 基线高 4.9 个百分点。
- 🇬🇧 A robot policy must understand the task and know how to move. ZAP bootstraps world understanding with a pretrained 27B model, then uses a simple tool harness plus supervised fine-tuning and GRPO on simple simulated tasks to teach it how to move, with no real-world robot data. It reaches 96.7% on real-world tasks, matching GPT-6 Astra in the same harness and beating the MolmoAct2 VLA (33.3%) while running 3× faster and 17× cheaper; it generalizes to an unseen embodiment and new objects/goals, and scores 55.9% on RoboLab-120 with a Franka, 4.9 points above the leading VLA/WAM baseline.

### [Omni-IGN: Onboard Image-Goal Navigation for Drones with Omnidirectional Vision](https://arxiv.org/abs/2610.36968) — Yan, Huang, Wang, Wang 等
🏷️ 交叉方向 / Also: VLN / 视觉导航(图像目标导航)
开源状态 / Code: 🕒 计划开源 / Planned — 摘要:「The code and model checkpoints will be released upon acceptance」
- 🇨🇳 无人机图像目标导航在算力受限下需要探索、目标导向导航与避障,而现有方法多基于单视角,需额外旋转搜索视野外线索。Omni-IGN 是全机载系统,集成四鱼眼感知、基于注意力的 RL 策略(自适应融合多视角目标相关特征,给出连续导航的方向引导)与碰撞感知安全层;四鱼眼 RGB 同时支持导航与避障而无需专用深度传感器。在 Habitat 基准上达到连续动作基线中最佳,IsaacSim 飞行测试验证了学习式深度估计加动作安全层的避障效果,真机实验展示了无需微调、无需外部定位的零样本 sim-to-real 迁移;摘要未给出具体数值。
- 🇬🇧 Aerial image-goal navigation must explore, navigate and avoid obstacles under limited compute, yet single-view methods need extra rotation to find cues outside the field of view. Omni-IGN is a fully onboard system combining quad-fisheye perception, an attention-based RL policy fusing goal-relevant features across views, and a collision-aware safety layer, with the fisheye RGB serving both navigation and avoidance without a depth sensor. It achieves the best performance among continuous-action baselines on Habitat, IsaacSim flights validate learned depth plus the safety layer, and real-world tests show zero-shot sim-to-real transfer without fine-tuning or external localization; the abstract gives no numbers.

**替换版本(仅列名,更新内容未逐条核对)/ Replacements (names only; changes not diffed):2** — [Informationally Decoupled Trajectory Design for Sim-to-Real System Identification (IDTD)](https://arxiv.org/abs/2610.10905)(sim-to-real 系统辨识,Go2/G1/Crazyflie,真机 K1;[代码](https://github.com/jsw7460/IDTD),`git ls-remote` 已验证 ✅)· [MO-Playground](https://arxiv.org/abs/2603.09237)(GPU 多目标 RL,BRUCE 人形 locomotion;[项目页](https://dynamicmobility.github.io/moplayground/))。

---

## 运动控制·传统 / Motion Control · Classical(全部展开 / all expanded:7)

### [A Bi-level Co-design Framework for Lunar Monoped with 2D Jump and Landing Control](https://arxiv.org/abs/2610.37199) — Ramkumar, Kumar
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 月球重力(1.625 m/s²)下接触力小、腾空长,腿形态与控制器选择相互依赖。该工作用双层协同设计:外层差分进化搜索连杆长度,内层用基于二次规划的任务空间控制器(QP-TSC)或直接配点轨迹优化评估垂直跳。两种控制器给出不同的最优连杆长度,轨迹优化在大部分设计空间优于 QP-TSC,最优点处运输成本(COT)低 17%;扩展到 2D 跳跃时,带质心角动量调节的轨迹优化产生稳定的原地与前向跳跃,LQR 吸收冲击并稳定着陆(基线形态两连杆均 0.3 m)。仅仿真。
- 🇬🇧 In lunar gravity (1.625 m/s²), reduced contact forces and long flight phases couple leg morphology and controller choice. A bi-level co-design uses differential evolution over link lengths and evaluates each candidate on a vertical jump with either a QP-based task-space controller (QP-TSC) or direct-collocation trajectory optimization. The controllers yield different optimal link lengths and trajectory optimization wins over most of the space, with 17% lower Cost of Transport at the optima; extended to 2D jumps, trajectory optimization with centroidal angular momentum regulation gives stable in-place and forward jumps and an LQR absorbs touchdown impact (baseline: both links 0.3 m). Simulation only.

### [Keeping Contact: Task-Adaptive Friction Margins for Bimanual Non-Prehensile Manipulation](https://arxiv.org/abs/2610.36961) — Lee, Yang, Campolo(RA-L 接收)
开源状态 / Code: ❓ 未知 / Unknown(摘要仅给[项目页](https://keeping-contact.github.io/),未见代码链接或承诺)
- 🇨🇳 非抓握操作中,仅满足摩擦锥可行性不足以抵御滑移与接触丢失,不同的摩擦余量安全性不同。该工作用有符号摩擦距离度量力空间的摩擦余量,并由双臂倾斜中平衡枢轴力矩偏差所需的力修正推导任务自适应余量,把余量嵌入一系列二阶锥规划(SOCP),每个倾角下得到全局最优接触力解。优化器层面结果显示了可解释的力重分配与对物体属性变化的适应;真机实验在物体属性变化和模型失配下成功执行,固定余量与无余量对比说明了按任务需求自适应余量的重要性;摘要未给出具体数值。
- 🇬🇧 In non-prehensile manipulation, feasibility inside the friction cone does not guarantee robustness to slip or contact loss. The paper measures friction margin in force space with signed friction distance, derives a task-adaptive margin from the force correction needed to balance pivot-moment deviations in bimanual tilting, and embeds it in a sequence of second-order cone programs yielding a globally optimal contact force at each tilt angle. Optimizer-level results show interpretable force redistribution and adaptation to object property changes; real-world runs succeed under property variation and model mismatch, and fixed/no-margin comparisons show the value of adapting the margin; no numbers in the abstract.

### [Spiking Neuromorphic Control for Periodic Orbits Stabilization in Underactuated Robots: A Greedy Lyapunov-Based Approach](https://arxiv.org/abs/2610.37310) — Surov, Sumenkov
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 研究用脉冲神经网络实现的事件驱动控制器,为欠驱动机器人稳定给定周期轨道。通过横向线性化,机器人动力学在周期轨迹邻域近似为周期系数的线性时变(LTV)系统,轨道稳定化即稳定该 LTV 系统的平凡解。作者证明此前针对 LTI 系统提出的基于 Lyapunov 的贪心设计可扩展到这种周期 LTV 横向动力学,从而构造轨道镇定反馈控制器,并在「蝴蝶机器人」的轨迹镇定问题上演示了有效性;摘要未给出定量结果。
- 🇬🇧 The paper studies event-based spiking controllers for stabilizing a prescribed periodic orbit of underactuated robots. By transverse linearization, the dynamics near the orbit become a periodic linear time-varying system, so orbital stabilization reduces to stabilizing its trivial solution. A previously proposed Lyapunov-based greedy design for LTI systems is shown to extend to this periodic LTV system, yielding an orbital-stabilizing feedback controller, demonstrated on the butterfly robot; the abstract reports no quantitative results.

### [cuArms: GPU-Accelerated Conflict-Based Planning for Multi-Arm Manipulation](https://arxiv.org/abs/2610.36250) — Huang, Ramos, Li, Garrett
🏷️ 交叉方向 / Also: 运动规划 / Motion planning(未直接涉及 MPC/WBC,按轨迹/运动规划归入此类)
开源状态 / Code: ❓ 未知 / Unknown(摘要仅给[项目页](https://cuarms.github.io/),未见代码链接或承诺)
- 🇨🇳 多臂协作可大幅提升吞吐,但现有任务分配调度、联合运动规划或直接学习多臂策略的方法要么太慢、依赖领域假设,要么随机器人数与任务时域扩展性差。cuArms 是与 GPU 并行共同设计的基于冲突的规划器:用可复用的多模态路线图分解单机器人搜索空间,以惰性搜索消解冲突与死锁,并接入高层调度器提出候选骨架,联合优化任务分配、调度、运动与操作技能。实验称其确立新的 SOTA,可实时给出初始解并持续改进运动质量与调度,无需数天的领域训练;摘要未给出具体数值。
- 🇬🇧 Multi-arm manipulation can raise throughput, but existing allocation/scheduling, joint motion planning or learned multi-arm policies are too slow, domain-specific, or scale poorly with robots and horizon. cuArms is a conflict-based planner co-designed with GPU parallelism: reusable multi-modal roadmaps decompose each robot's search space, lazy search resolves conflicts and deadlocks, and a high-level scheduler proposes skeletons grounded into coordinated plans. It claims a new state of the art with real-time initial solutions and anytime improvements in motion quality and scheduling, without days of domain-specific training; no numbers in the abstract.

### [A 2-DOF MultiBody Track Joint for Race Car Optimization](https://arxiv.org/abs/2610.36407) — (American Modelica & FMI Conference 2026)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 赛车最小圈速优化需要既能仿真又能优化的路面约束模型。TrackJoint 是 Modelica 多体组件,把三维路面变成两自由度关节(沿参考线的行驶距离与侧向偏移),路面几何以周期分段五次样条表示,用 d'Alembert 原理闭合约束(两个广义力为零,无需拉格朗日乘子)。关节接到 Dymola 多体赛车后整体导出为 FMI 3.0 FMU,同一个 FMU 既用于时域仿真,也用于 CasADi/IPOPT 最小圈速优化而无需改模型(关键在于保留弧长坐标为真实状态并发布其时间导数);在新加坡 F1 赛道上报告了最小圈速仿真结果,摘要未给出具体圈速数值。
- 🇬🇧 Minimum lap-time optimization needs a road-constraint model usable for both simulation and optimization. TrackJoint is a Modelica MultiBody component turning a 3D road surface into a 2-DOF joint (distance along a reference line and lateral offset), with geometry as periodic piecewise-quintic splines and the constraint closed by d'Alembert's principle (zero generalized forces, no Lagrange multipliers). Attached to a Dymola race car and exported as one FMI 3.0 FMU, the same model serves time-domain simulation and CasADi/IPOPT minimum lap-time optimization unchanged (the arc-length coordinate is kept as a real state with its time derivative published); results are reported on the Singapore F1 circuit, with no numeric lap times in the abstract.

### [A Singularity Avoiding Track Model for Race Car Optimization](https://arxiv.org/abs/2610.36430) — (American Modelica & FMI Conference 2026)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 以几何中心线为参考的赛道曲面在急弯处相邻法线可能在可行驶区内相交,导致参数化失效。该工作给出把测量赛道点云转换成闭合、C⁴ 可微三维曲面模型(Monge patch)的拟合流程,以最小曲率线(MCL)作参考线,MCL 由带赛道边界、周期性与 jerk 正则约束的二次规划求得。在所研究的全部赛道上,MCL 使参数化失效区域移出可行驶带,法线映射在全宽度内保持单射,并使时间—弧长变换更线性,利于最小圈速问题;曲面与赛道宽度以周期分段五次 C⁴ B 样条导出,供非线性规划使用。
- 🇬🇧 Surfaces anchored on the geometric centre-line can have adjacent normals crossing inside the drivable strip on tight corners, breaking the parametrisation. The paper fits a measured racetrack point cloud into a closed C⁴ three-dimensional Monge-patch surface referenced to the minimum-curvature line (MCL), obtained from a quadratic program with track-boundary, periodicity and jerk-regularisation constraints. On all circuits studied the MCL moves the breakdown region outside the strip, keeps the normal map injective across the full width, and yields a more linear time-to-arc-length transformation; the surface and widths are exported as periodic piecewise-quintic C⁴ B-splines for nonlinear programs.

### [Learning Side-by-Side Navigation for Personal Mobility Vehicles from Human Drivers](https://arxiv.org/abs/2610.36726) — (摘要未列作者机构)
🏷️ 交叉方向 / Also: 导航 / Navigation(逆强化学习拟合代价参数)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 一对个人移动车(PMV)需在给定全局路径上协作保持可交谈的社交队形,同时安全平稳。每辆车运行自己的基于采样的模型预测规划器,仅交换对方可观测的里程计,联合决策表示为一对候选轨迹的效用矩阵并按共同规则求解;行为参数由十对驾驶者 409 分钟的人类驾驶数据经逆强化学习拟合,可用车道由走廊自动推导,并设有代价无法覆盖的安全层(整车制动余量检查,卡住时沿原路倒车)。在 24 次原条件和 24 次生成障碍布局的闭环仿真中无车辆撞墙或撞锥,队形保持时间在障碍中为 60.5%/68.9%、空旷通道 81.2%/91.5%,高于驾驶者的 34.0%/36.0% 与 52.9%/56.0%,且速度与之相当(仅在 ROS 2 差速运动学仿真中)。
- 🇬🇧 A pair of personal mobility vehicles must hold a conversational formation along a global path while staying safe and smooth. Each runs a sampling-based model-predictive planner and exchanges only observed odometry; the joint decision is a pair of utility matrices over candidate trajectory pairs resolved by a common rule, with behavioural parameters fitted by inverse RL from 409 minutes of driving by ten pairs, lanes derived from the corridor, and a safety layer the cost cannot override. In 24 + 24 closed-loop runs no vehicle hit a wall or cone; formation is held 60.5/68.9% of the time among obstacles and 81.2/91.5% in a clear aisle vs. 34.0/36.0% and 52.9/56.0% for the drivers, at matching speed (ROS 2 kinematic simulation only).

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models(展开 10 / 另列 8,共 18)

### [RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding](https://arxiv.org/abs/2610.36533) — Liu, Ye, Yuan 等
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://roboauto-ai.github.io/)标注「Code coming soon」
- 🇨🇳 Code-as-Policy 让 LLM 智能体搜索可编辑的机器人程序,但仅靠执行反馈难以回答物体如何操作、场景几何如何约束、交互为何成败等物理问题。RoboAuto 在物体、场景、交互三个层次组织物理理解:含可执行技能与物体中心知识(可供性、空间关系、动作效果)的层次知识库、把知识落到当前环境的场景接地、以及带自设计实验验证各阶段物理效果并主动检验竞争假设的多阶段规划。在 LIBERO-PRO 短时程任务上成功率 89.1%,在 LIBERO-PRO Long 与 LIBERO-Plus 上平均成功率超过 ASPIRE 的两倍,并在三个长时程精密真机任务上优于 ASPIRE 与 π0.5;知识库可跨模拟器与本体迁移,性能随其规模增长。
- 🇬🇧 Code-as-Policy lets LLM agents search over editable robot programs, but execution feedback alone leaves physical questions unresolved. RoboAuto organizes physical understanding at object, scene and interaction levels: a hierarchical knowledge base of executable skills and object-centric knowledge (affordances, spatial relations, action effects), scene grounding, and multi-stage planning with self-designed experiments that test competing hypotheses. It reaches 89.1% on short-horizon LIBERO-PRO, more than twice ASPIRE's mean success on LIBERO-PRO Long and LIBERO-Plus, and beats ASPIRE and π0.5 on three long-horizon real-robot tasks; the knowledge base transfers across simulators and embodiments and performance scales with its size.

### [HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning](https://arxiv.org/abs/2610.36374) — Yu, Tiezzi, Beyan(NeurIPS 2026)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/yfqi/HIDRA);摘要给出,已用匿名 `git ls-remote` 验证
- 🇨🇳 在无回放、单遍的终身模仿学习中,顺序更新会扭曲表示空间,使基于专家混合的路由随时间退化。HIDRA 用层次双注意力把指令级专家检索与上下文相关的细化解耦,并引入键级几何正则,同时强制任务内对齐与任务间分离,以支持可扩展的专家集合。在 LIBERO 多个套件(含更难的异构任务序列与改写指令变体)上,AUC 与前向迁移优于无回放与基于回放的基线,同时保持低遗忘,高干扰与语言变化下收益更强;摘要未给出具体百分比。
- 🇬🇧 In replay-free single-pass lifelong imitation learning, sequential updates distort the representation space and degrade expert routing. HIDRA uses hierarchical dual attention to decouple instruction-level expert retrieval from context-dependent refinement, plus key-level geometric regularization enforcing within-task alignment and cross-task separation, supporting an expandable expert set. On several LIBERO suites, including harder heterogeneous sequences and paraphrased instructions, it beats replay-free and replay-based baselines in AUC and forward transfer with low forgetting, with larger gains under high interference; no exact percentages in the abstract.

### [From 12 to 200 Demonstrations: How ACT, Diffusion Policy, SmolVLA and π0.5 Scale on a Low-Cost Arm](https://arxiv.org/abs/2610.37170) — Cowling
🏷️ 交叉方向 / Also: VLA(基准性实证研究)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 这是一项在 SO-101 低成本机械臂上的实证研究:用 12、25、50、100、200 条遥操作演示分别训练 ACT、Diffusion Policy、SmolVLA、π0.5,共 1,340 个计分真机回合(126 个区块)。ACT 从 12 条时 40 回合中 1 次成功升到 100 条时 37 次;π0.5(微调动作专家)数据稀缺时最好(12 条 16/40、25 条 28/40)后稳定在约 70%,100 条以后 ACT 领先;SmolVLA 与 Diffusion Policy 峰值约 50%,前者 47% 回合手臂从未启动;π0.5 的微调配方比数据量更重要(LoRA 110 回合成功 4 次,对比动作专家微调 200 回合成功 130 次)。作者还量化了十回合区块的测量噪声并说明哪些结论受训练长度混淆。
- 🇬🇧 An empirical study on a low-cost SO-101 arm: ACT, Diffusion Policy, SmolVLA and π0.5 trained on 12–200 teleoperated demonstrations, scored on 1,340 real episodes in 126 blocks. ACT rises from 1/40 at 12 demos to 37/40 at 100; π0.5 with action-expert fine-tuning is best when data is scarce (16/40 at 12, 28/40 at 25) then plateaus near 70%, with ACT ahead from 100 demos; SmolVLA and Diffusion Policy peak near 50% (SmolVLA's arm never started in 47% of episodes). For π0.5 the recipe mattered more than data (LoRA 4/110 vs. 130/200 for action-expert tuning); the study also quantifies block-level noise and states which conclusions survive the training-length confound.

### [Ego-CEVR: Learning Cross-Embodiment Visual Representations from Human Egocentric Videos](https://arxiv.org/abs/2610.37509) — Zhou, Fang, Xu 等
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 如何把低成本、可扩展的第一视角视频变成机器人操作能力。Ego-CEVR 为全局与交互表示分配不同学习目标:全局模块通过第一视角视频的未来预测学习物体关系、任务状态与时间进度;交互模块在全局上下文下解读腕部观测,用机器人动作监督学习局部对齐与接触线索;两条残差通路同时把两种表示提供给动作策略。全局视频模块可在大规模人类第一视角视频与多种机器人本体视频上独立预训练,无需动作标签或成对腕部观测;预印本摘要未给出定量结果。
- 🇬🇧 How to turn scalable egocentric video into robot manipulation capability. Ego-CEVR assigns different objectives to global and interaction representations: a global module learns object relations, task state and temporal progress via future prediction on egocentric video, an interaction module interprets wrist observations in global context to learn local alignment and contact cues from action supervision, and separate residual paths expose both to the policy. The global module can be pretrained independently on human egocentric and diverse robot videos without action labels or paired wrist views; the abstract reports no quantitative results.

### [ActiveAlign: Aligning Egocentric Manipulation via Active Perception](https://arxiv.org/abs/2610.36859) — Qiu, Wen, Jiang 等
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 Real2Sim2Real 多依赖被动感知,不完美观测造成 real2sim 差距。ActiveAlign 用主动感知从交互中对齐该差距,含两个模块:ActiveAlign-Waving 利用主动手部运动与可微渲染做手眼标定,ActiveAlign-Touching 用触觉反馈把物体对齐细化到毫米级。前者可为开源的未标定机器人操作数据集构建仿真环境,并在 Unitree G1 真机上实现按按钮、移滑块等毫米级物体的精细操作;摘要未给出更多数值。
- 🇬🇧 Real2Sim2Real mostly relies on passive perception, leaving real2sim gaps from imperfect observation. ActiveAlign aligns the gap through interaction: ActiveAlign-Waving does hand-eye calibration from active hand motion and differentiable rendering, and ActiveAlign-Touching refines object alignment to millimeter precision with tactile feedback. Waving can curate simulation environments for open uncalibrated manipulation datasets, and on a real Unitree G1 the system enables fine manipulation of millimeter-scale objects such as pressing buttons and moving sliders; no further numbers are given.

### [TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation](https://arxiv.org/abs/2610.36694) — An, Zhou, Dong, Li 等
🏷️ 交叉方向 / Also: VLA(可迁移到 π0.5)
开源状态 / Code: ❓ 未知 / Unknown(Comments 仅「Under review」,无代码链接或承诺)
- 🇨🇳 语言条件多任务操作中,流匹配策略通常共享单一高斯源先验与线性传输路径,难以兼顾差异化的运动需求。TOPS 不改网络结构,按任务调整流的源先验与插值调度:先由反向映射的专家动作序列构造多模态任务源,让语言选择生成的起点;再根据源—目标协方差失配在去噪早期放慢向专家动作的过渡、后期沿需要扩展的方向加速,并在高斯端点模型下给出可降低速度预测风险上界的分析。单步 TOPS 使 LIBERO-10 成功率由十步标准 FM 的 53.44% 提升到 69.67%,推理时间约为六分之一;迁移到 π0.5 在四个设置上均有增益;真机上抽屉打开由 20% 提升到 80%。
- 🇬🇧 Flow-based multi-task policies share one Gaussian source prior and a linear path across tasks, which struggles with distinct motion needs. TOPS adapts the source prior and interpolation schedule per task without changing the network: multimodal task sources from reverse-mapped expert actions, and a schedule that slows early denoising and accelerates later along directions needing expansion, with an analysis lowering an upper bound on velocity-prediction risk. With one integration step it lifts LIBERO-10 from 53.44% (ten-step FM) to 69.67% at ~1/6 inference time, gains transfer to π0.5 across all four settings, and a real drawer-opening task goes from 20% to 80%.

### [Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling (QCP)](https://arxiv.org/abs/2610.37393) — Kang, Shin, Kim, Lee 等
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 机器人策略评估常只看二值成功信号,而实际部署还关心执行速度、动作平滑等质量属性且需动态调节。Quality-Controllable Policy (QCP) 支持推理时对单个质量属性及其组合的控制;为把可控范围扩展到初始演示之外,采用迭代事后(hindsight)重标注循环:在目标质量标签下在线 rollout,把成功轨迹加入数据集,按实测质量事后重标注并微调。Robomimic 与 RoboEval 上任务执行质量与成功率逐轮提升,产生的成功 rollout 质量超过初始演示;真机上控制速度提高了传送带吞吐,控制搬运稳定性提高了搬运红酒杯的成功率。
- 🇬🇧 Policy evaluation often relies on a binary success signal, but deployment also cares about speed and smoothness that must be controlled dynamically. QCP offers inference-time control over individual quality attributes and their combinations, and an iterative hindsight relabeling loop (online rollouts under target quality labels, add successes, relabel by measured quality, fine-tune) extends the controllable range beyond the demonstrations. On Robomimic and RoboEval quality and success improve across iterations with rollouts exceeding the initial demonstrations; on real tasks, speed control raises conveyor throughput and stability control improves wine-glass carrying.

### [SO-101 Bench: Accessible Spatial Manipulation](https://arxiv.org/abs/2610.36420) — Hickok
🏷️ 交叉方向 / Also: VLA / 世界模型与 WAM(基准)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/5hadytru/so101_bench);Comments 给出,已用匿名 `git ls-remote` 验证;另有[项目页](https://so101-bench.github.io/)
- 🇨🇳 低成本 SO-101 机械臂缺少能完成空间约束、语言条件任务的开箱即用策略,现有 SO-101 基准只能在实体上跑且任务简单。SO-101 Bench 基于 Isaac Lab 数字孪生,含 4 个任务(5 个族)、138 个物体(已见/未见实例/未见类别拆分)、916 个评测回合及 3,629 条仿真演示,所有学习式策略在等算力下微调。五个无真机数据训练的策略(四个 VLA 与一个 LLM 智能体)在真机未见环境中保持与仿真完全一致的排名(Spearman ρ=1.00,MMRV=0.000),尽管仿真高估成功率;九个 VLA/WAM 中最好的约 61%,空间放置、未见类别与旋转适配规划仍是开放问题;写代码并调用抓取接口的 LLM 智能体得分 83.2%。
- 🇬🇧 Low-cost SO-101 arms lack out-of-the-box policies for spatially constrained language-conditioned tasks, and existing benchmarks run only on hardware with simple tasks. SO-101 Bench is an Isaac Lab digital-twin benchmark with 4 tasks (5 families), 138 objects in seen/unseen-instance/unseen-class splits, 916 evaluation episodes and 3,629 simulated demonstrations, all policies fine-tuned under equal compute. Five policies trained without real data (four VLAs, one LLM agent) keep their exact ranking on the physical arm in an unseen environment (Spearman ρ = 1.00, MMRV = 0.000) though simulation overestimates success; the best of nine VLAs/WAMs scores near 61%, and an LLM agent writing code over a grasping interface scores 83.2%.

### [OpenJaws: An Open Hardware UMI Framework with Stereo Localization for Generalist Manipulation](https://arxiv.org/abs/2610.36598) — Murali, Oza, Chahal 等
开源状态 / Code: ✅ 已开源 / Released — 摘要声明硬件、软件与数据以商业宽松许可发布,并指向[项目页](https://open-jaws.github.io/);具体仓库链接未单独核验
- 🇨🇳 手持数据采集接口(UMI)的动作标签质量受视觉定位精度限制,单目 VIO 有尺度模糊与漂移,闭源模块又增加成本。OpenJaws 是完全开源的软硬件框架:模块化 3D 打印夹爪带标准 ISO 适配器,搭配低成本立体相机恢复公制相机轨迹;并提出 UMI-Loc-Bench-v1 基准量化手持采集设备的真实定位精度,显示立体定位显著优于单目;用 OpenJaws 采集的数据训练的策略可在真机多任务上部署;摘要未给出具体误差数值。
- 🇬🇧 The quality of handheld-interface (UMI) action labels is bounded by localization accuracy; monocular VIO suffers scale ambiguity and drift, while closed-source tracking adds cost. OpenJaws is a fully open hardware/software framework: a modular 3D-printed gripper with a standard ISO adapter plus a low-cost stereo camera recovering metric trajectories, a UMI-Loc-Bench-v1 localization benchmark showing stereo substantially beats monocular, and policies trained on its data deployed on a real robot across tasks; no error figures in the abstract.

### [RoboSTD: Zero-Shot Single-to-Dual Transfer via Sagittal Mirroring for Bimanual Learning](https://arxiv.org/abs/2610.36685) — Wu, Liu, Xie 等
开源状态 / Code: ❓ 未知 / Unknown(摘要仅给[项目页](https://huahungy.github.io/RoboSTD/),未见代码链接或承诺)
- 🇨🇳 双臂演示采集昂贵,现有单臂数据因动作空间、协调需求与手臂偏侧差异难以直接迁移。RoboSTD 先对观测、本体感觉与动作做矢状面镜像,构造可执行的对侧伪演示;再用 LLM 生成结构化时空协调约束,指导跨工作空间区域和任务阶段重建伪双臂监督。在 AgileX ALOHA 的 RoboTwin 仿真与真机中评测,无需额外双臂演示,在收集杯子任务上平均收集杯数达到单臂基线的 2.11 倍。
- 🇬🇧 Bimanual demonstrations are costly and single-arm data transfer poorly due to action-space, coordination and arm-side-preference gaps. RoboSTD mirrors observations, proprioception and actions across the sagittal plane to construct executable contralateral pseudo-demonstrations, then uses an LLM to produce spatio-temporal coordination constraints guiding pseudo-bimanual supervision across workspace regions and task stages. On AgileX ALOHA in RoboTwin and the real world, without extra bimanual demonstrations, it raises the average number of cups collected to 2.11× the single-arm baseline.

**其余 8 条(列名)/ Remaining 8 (names only):** [Which Hand Was Late?](https://arxiv.org/abs/2610.37533)(双臂工具使用失败诊断)· [Kinematic Constraint-Referenced Evaluation for Articulated Object Manipulation](https://arxiv.org/abs/2610.37550) · [QuadPose / Camera-to-Quadruped Robot Pose Estimation](https://arxiv.org/abs/2610.36599) · [Torch-Hand 21-DoF 灵巧手](https://arxiv.org/abs/2610.36789) · 替换版本:[DeFM](https://arxiv.org/abs/2601.18923) · [FTP-1](https://arxiv.org/abs/2606.13102) · [From Grasps to Dexterity](https://arxiv.org/abs/2606.30749) · [BiDex-100](https://arxiv.org/abs/2610.25459)。

---

## VLA / VLA(展开 7)

### [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381) — Wang, Cai, An, Zeng 等
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown(HF Daily Papers 无 githubRepo,Comments 为空)
- 🇨🇳 VLA 对物理动力学理解有限,而视频世界模型生成未来视频会给控制回路引入高延迟。PDRVLA 的轻量 Physical Dynamics Module 从视觉—语言特征中提取物理 token 来条件化动作生成,无需在线生成视频;模块通过直接预测未来 RGB、深度与光流特征来学习,并辅以冻结的预训练视频世界模型监督;训练仅用公开数据,并通过人到机器人合成、子任务标注与具身思维链(ECoT)标注扩充。四个仿真基准成功率:LIBERO 99.3%、LIBERO-Plus 89.9%、RoboTwin 2.0 93.6%、SimplerEnv 81.5%。
- 🇬🇧 VLAs understand physical dynamics poorly, while video world models add latency by generating future video. PDRVLA's lightweight Physical Dynamics Module extracts physical tokens from vision–language features to condition action generation without online video generation, learned by predicting future RGB, depth and optical-flow features with auxiliary supervision from a frozen video world model; training uses only public data expanded by human-to-robot synthesis, subtask and ECoT annotation. It reaches 99.3% on LIBERO, 89.9% on LIBERO-Plus, 93.6% on RoboTwin 2.0 and 81.5% on SimplerEnv.

### [Vision-Language-Action or World-Action? Just Action Models (JAM)](https://arxiv.org/abs/2610.37219) — Yu, Huang, Li, Yamasaki(cross-list)
🏷️ 交叉方向 / Also: 世界模型与 WAM / WAM
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/y0urOy/JAM);HF Daily Papers 给出,已用匿名 `git ls-remote` 验证;[项目页](https://y0uroy.github.io/JAM/)
- 🇨🇳 VLA 与 WAM 社区争论策略应继承 VLM 还是视觉生成器的预训练知识,但这一争论捆绑了主干初始化、未来观测目标、推理时是否保留未来损失机制三个可分离的选择。作者将其解耦为统一框架 Just Action Model (JAM):预训练视觉主干加动作专家,用动作损失与前瞻(foresight)损失训练,前瞻损失通过训练后丢弃的预测头预测冻结的未来编码,全程无需视觉生成。JAM 在 LIBERO 与 LIBERO-Plus 上超过匹配的 FastWAM/ImageWAM,在 RoboTwin 上持平或略高;相对 FastWAM 成功率由 97.0%/55.3%/91.2% 提升到 98.2%/64.5%/91.4%,缓存前瞻目标时估计在线训练 FLOPs 降低 73%。
- 🇬🇧 The VLA vs. WAM debate bundles three separable choices: backbone initialization, the future-observation objective, and whether the future-loss machinery stays at inference. JAM decouples them: a pretrained visual backbone with an action expert trained with an action loss and a foresight loss, where the foresight loss predicts frozen encodings of the recorded future through a head discarded after training, so no visual generation is involved. JAM beats matched FastWAM/ImageWAM on LIBERO and LIBERO-Plus and is similar or slightly higher on RoboTwin; vs. FastWAM, success goes from 97.0%/55.3%/91.2% to 98.2%/64.5%/91.4%, with 73% lower estimated online training FLOPs using cached foresight targets.

### [Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution (R2A)](https://arxiv.org/abs/2610.37215) — Pham, Dao, Nguyen, Nguyen 等
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://retrieve2act.github.io/r2a/)的「Code」只指向匿名评审镜像 `anonymous.4open.science`,非公开仓库,无开源承诺
- 🇨🇳 VLA 语义泛化强,但对分布外视觉扰动很脆弱;现有测试时方法抑制伪视觉线索,却忽视策略自身训练经验中干净的运动学先验。R2A 把 OOD 鲁棒性形式化为纯几何的运动基元检索问题:将成功演示组织成离线时空运动基元图,推理时由查询相关的 GNN 定位执行位置并检索结构兼容的后续基元,再用学得的逐维门控与冻结 VLA 的预测动作融合,无需微调。在 GR00T N1.7、π0.5、StableVLA 三种架构上,仿真(LIBERO-Plus、RoboTwin2.0-Plus)绝对成功率最高 +12%,真机最高 +40%。
- 🇬🇧 VLAs generalize semantically but are fragile under OOD visual shifts, and test-time methods suppress spurious cues while ignoring clean kinematic priors in the policy's own training experience. R2A casts OOD robustness as geometric motion-primitive retrieval: successful demonstrations form an offline spatiotemporal primitive graph, a query-dependent GNN localizes execution in it and retrieves compatible future primitives, which a learned dimension-wise gate blends with the frozen VLA's actions without fine-tuning. Across GR00T N1.7, π0.5 and StableVLA it yields up to +12% absolute success in simulation (LIBERO-Plus, RoboTwin2.0-Plus) and +40% in real-world deployment.

### [Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer](https://arxiv.org/abs/2610.37330) — Ren, Zheng, Cui, Planche 等
🏷️ 交叉方向 / Also: ⚠️ 标题与摘要不一致:标题指向人形技能迁移(若属实应归运动控制),但 arXiv 摘要实际描述 VLA 失败轨迹学习(AFIL);此处按摘要归入 VLA,请以全文为准。
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments「12 pages」均无代码链接或承诺)
- 🇨🇳 摘要称,依赖仅成功样本行为克隆的 VLA 缺少纠正信号,微小执行误差会累积成不可恢复的分布外失败。提出 Adaptive Failure-Informed Learning (AFIL):用预训练 VLA 在线生成失败 rollout 作为自适应负向引导,无需手工设计失败模式或人在回路;联合训练分别面向成功与失败行为的 Dual Action Generators,共享视觉—语言主干;采样时失败生成器依据每个扩散步成功/失败分布的距离自适应调节引导强度,把动作推离易失败区域。在领域内/外、短/长时程操作任务上一致提升成功率与鲁棒性;摘要未给出具体数值。
- 🇬🇧 Per the abstract (which does not match the title), VLAs trained with success-only behavioral cloning lack corrective signals, so small errors compound into unrecoverable OOD failures. Adaptive Failure-Informed Learning (AFIL) generates failure rollouts online with a pretrained VLA as adaptive negative guidance, trains Dual Action Generators for successful and failed behaviors on a shared vision-language backbone, and at sampling time steers actions away from failure-prone regions with strength set by the per-step distance between success and failure distributions. It consistently improves success and robustness over VLA baselines on in- and out-of-domain, short- and long-horizon manipulation; no numbers in the abstract.

### [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](https://arxiv.org/abs/2610.37666) — Kim, Huang, Kim, Chen 等
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown(已核查[项目页](https://thinkworld-project.github.io/),「Code」为占位链接,无承诺)
- 🇨🇳 VLA 的泛化受限于带动作标注机器人演示的多样性,而人类视频覆盖更广但缺少显式动作落地。ThinkWorld 把每个动作思考表示为 Chain-of-Dynamics (CoD)——连接当前世界与未来状态的离散运动 token 序列,作为跨本体通用的动作表示;先用带动作标注的演示初始化 CoD,再预测每个 CoD 诱导的未来,并强化那些预测更贴近实际结果的 CoD,使无动作标注的视频也能从观测到的状态转移获得直接监督。仿真与真机实验展示了有效的人到机器人迁移以及对未见任务与环境的强泛化;摘要未给出具体数值。
- 🇬🇧 VLA generalization is limited by the diversity of action-labeled demonstrations, while human videos are broad but lack action grounding. ThinkWorld represents each action thought as a Chain-of-Dynamics (CoD), a sequence of discrete motion tokens linking the current world to a future state and shared across embodiments; CoD is initialized on action-labeled demos, then the future each CoD induces is predicted and CoDs whose predictions better match the outcome are reinforced, letting action-free videos supervise via observed transitions. Simulation and real-robot experiments show human-to-robot transfer and strong generalization to unseen tasks and environments; no numbers in the abstract.

### [ASPEN: Adaptive Semantic Reasoning via Command Persistence Prediction for Efficient Navigation VLAs](https://arxiv.org/abs/2610.36285) — Akustia, Hu
🏷️ 交叉方向 / Also: VLN
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 导航 VLA 即使下一条指令不变也反复调用昂贵的语义推理;复用指令能省算力,却可能漏掉依赖指令的转弯或停止。ASPEN 是事件触发调度器,基于「指令持续性预测」估计冻结基础策略是否会重复上一条指令:轻量多模态预测器融合时序观测、语言指令、执行历史与缓存的 VLA 置信度,在符合条件的指令边界上预测持续性足够就复用,否则触发新的语义推理。在冻结 NaVILA、跨数据集 RxR-CE val-unseen 上,VLA 调用减少 9.5%、估计推理时间减少 8.1%(含调度开销),导航表现相当,92.1% 的回合动作序列与基线完全一致。
- 🇬🇧 Navigation VLAs repeatedly invoke costly semantic reasoning even when the next command is unchanged; reuse saves compute but may miss instruction-dependent turns or stops. ASPEN is an event-triggered scheduler predicting command persistence, i.e. whether the frozen policy would reissue its previous command, with a lightweight multimodal predictor over temporal observations, language, execution history and cached VLA confidence; high predicted persistence permits reuse, otherwise fresh reasoning is triggered. With frozen NaVILA on RxR-CE val-unseen it cuts VLA calls by 9.5% and estimated inference time by 8.1% (incl. overhead) at comparable navigation performance, with identical action sequences on 92.1% of episodes.

### [Evaluation-Guided Demonstration Refinement for Vision-Language-Action Policies: The Winning Entry in the MetaFine Open Competition](https://arxiv.org/abs/2610.36765) — Zheng, Chen, Li 等
开源状态 / Code: ❓ 未知 / Unknown(Comments 注明 CoRL 2026 RoboFineMani 研讨会冠军,无代码链接或承诺)
- 🇨🇳 MetaFine 公开赛含五个任务,参赛者需微调 VLA。团队为每个任务单独微调 π0.5,采用任务专属训练混合与每次预测执行的动作数,从官方演示与专家流程出发;本地评估暴露了反复出现的抓取、推动与插入失败,于是修订演示动作,并加入策略所到达状态下的专家续写,同时保留名义演示;检查点在每条指令上逐一比较,避免一条指令的提升掩盖另一条的退化。提交的 MAI 以 96.66 分总分排名第一。
- 🇬🇧 The MetaFine Open Competition has five tasks for fine-tuned VLAs. The team fine-tuned a separate π0.5 per task with task-specific training mixtures and executed-action counts, starting from official demonstrations; local evaluation exposed recurring grasping, pushing and insertion failures, addressed by revising demonstrated motions and adding expert continuations from states the policy reached while keeping nominal demos, with checkpoints compared on every instruction so gains could not hide losses. The submission, MAI, ranked first overall with a score of 96.66.

**其余(列名)/ Names only (replacements, 4):** [RePO-VLA](https://arxiv.org/abs/2605.09410) · [AWARE](https://arxiv.org/abs/2602.18020) · [VLA-HWBench](https://arxiv.org/abs/2610.34717) · [When Do Discrete Actions Make Good Continuous Controllers?](https://arxiv.org/abs/2610.20429)。另见 / See also: [VLA-Stem](https://arxiv.org/abs/2610.37378)(已归入 运动控制·RL)· [ZAP / Pretraining Knows What, Simulation Teaches How](https://arxiv.org/abs/2610.35817)(已归入 运动控制·RL)· [TOPS](https://arxiv.org/abs/2610.36694)(已归入 具身智能与机器人基础模型)。

---

## VLN / VLN(展开 0)

今日窗口内无新的纯 VLN 论文。 / No new pure VLN papers in the window.
替换版本(列名,共 3)/ Replacements (names only, 3): [Goal2Pixel](https://arxiv.org/abs/2606.01621)(VLN)· [HGWM](https://arxiv.org/abs/2610.32554)(零样本物体导航世界模型)· [From Language to Navigation Goals](https://arxiv.org/abs/2607.13624)。
另见 / See also: [ASPEN](https://arxiv.org/abs/2610.36285)(已归入 VLA)· [Omni-IGN](https://arxiv.org/abs/2610.36968)(已归入 运动控制·RL)。

---

## 世界模型与 WAM / World Models & WAM(展开 12 / 另列 7,共 19)

### [E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling](https://arxiv.org/abs/2610.36011) — X-Era AI Lab Team, Lai, Zhan 等
🏷️ 交叉方向 / Also: 空间智能 / Spatial Intelligence(3D 基础模型)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 主流 WAM 以视频基础模型或 VLM 为主干,即使引入 VGGT 等 3D 特征也只是辅助输入或预测目标。E0.5 是直接建立在 3D 基础模型上的几何原生 WAM:以 3D 基础模型为主干,使 3D 几何成为世界建模与动作预测的原生表示,并显式联合预测未来 3D 状态与动作。无具身预训练时在 RoboTwin 2.0 干净/随机化设置成功率 89.90%/50.09%;在 AgiBotWorld-Beta 逾 16 万条机器人轨迹上预训练后,真机操作平均成功率在 AgileX Piper 与 Zerith H1 上分别提升约 15 与 7 个百分点。
- 🇬🇧 Mainstream WAMs use video foundation models or VLMs as backbones, with 3D features from models like VGGT only as auxiliary inputs. E0.5 is a geometry-native WAM built directly on a 3D foundation model, making 3D geometry the native representation for world modeling and action prediction and explicitly predicting future 3D states with actions. Without embodied pretraining it reaches 89.90% (clean) and 50.09% (randomized) on RoboTwin 2.0; pretraining on 160k+ AgiBotWorld-Beta trajectories improves real-world manipulation success by about 15 and 7 points on AgileX Piper and Zerith H1.

### [RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](https://arxiv.org/abs/2610.36791) — Zhao, Tang, Wang, Zhu 等(Alibaba DAMO Academy)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/alibaba-damo-academy/RynnWorld-Latent);Comments 与 HF 给出,已用匿名 `git ls-remote` 验证;[项目页](https://alibaba-damo-academy.github.io/RynnWorld-Latent.github.io/)
- 🇨🇳 不同本体的动作空间互不兼容、人类视频又无控制标签,难以从异构交互视频学习可控动力学。RynnWorld-Latent 以 RynnLAM 的 3D 接地潜在动作作为共享条件接口,基于预训练视频 Transformer,结合全局动作 token 与恒等初始化的局部通路对齐动作和未来视频潜变量,在 23 个数据集约 5.535 亿帧上预训练再后训练到目标机器人;并支持数字遥操作与潜在动作合成两条数据生成路线。公开基准与两个真机平台上视频预测指标提升,合成数据中期训练提升 LIBERO 与 LIBERO-Plus 成功率,两条路线都使真机策略成功率优于仅真实演示。
- 🇬🇧 Embodiments have incompatible action spaces and human videos lack control labels, hindering controllable dynamics learning. RynnWorld-Latent uses the 3D-grounded latent actions of RynnLAM as a shared conditioning interface on a pretrained video transformer, combining global action tokens with an identity-initialized local pathway, pretrained on 23 datasets (~553.5M frames) and post-trained per robot, with digital teleoperation and latent-action synthesis as data-generation routes. It improves video-prediction metrics on public benchmarks and two real platforms, synthetic mid-training raises LIBERO/LIBERO-Plus success, and both routes beat real-demo-only training on real robots.

### [Trace-WAM: Learning to Act via 3D Motion Prediction for World Action Models](https://arxiv.org/abs/2610.36840) — Hu, Wu, Shi, Zhang 等
开源状态 / Code: ❓ 未知 / Unknown(已核查[项目页](https://trace-wam.github.io/),无代码链接或承诺)
- 🇨🇳 操作成功主要取决于机器人与任务相关物体如何演化,而未来视频预测还要重建整个场景外观与背景。Trace-WAM 用未来 3D 运动预测作辅助目标(监督时间点对应、图像平面位移与深度变化),采用三分支 Mixture-of-Transformer(Tri-MoT)联合学习视频预测、运动预测与动作生成;动作专家不消费预测轨迹,推理时保留当前观测策略路径(一次视觉前向加动作去噪)。在 RoboCasa-GR1、LIBERO、LIBERO-Plus 上取得强的分布内表现与分布外泛化,在有限演示与分布偏移下相对 Fast-WAM 增益尤其明显;摘要未给出具体数值。
- 🇬🇧 Manipulation depends on how the robot and task-relevant objects evolve, while future-video prediction must reconstruct the whole scene. Trace-WAM adds future 3D motion prediction (temporal point correspondence, image-plane displacement, depth change) as an auxiliary objective via a three-branch Mixture-of-Transformer jointly learning video prediction, motion prediction and action generation; the action expert does not consume predicted trajectories, so inference stays a single visual pass plus action denoising. It shows strong in-distribution and OOD results on RoboCasa-GR1, LIBERO and LIBERO-Plus, with clear gains over Fast-WAM under limited demonstrations and shifts; no numbers in the abstract.

### [GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation](https://arxiv.org/abs/2610.37091) — Liu, Liu, Li, Song 等
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/gaoxiang12/ga-wm);摘要给出,已用匿名 `git ls-remote` 验证(radar new_repos:8★)
- 🇨🇳 多数 WAM 建立在十亿参数级 VLM/视频生成主干上,训练与推理代价高。GAWM 是紧凑的多任务 WAM:在冻结 DINOv3 编码器的潜空间预测未来观测,把每个相机视角压缩为少量 token,由以任务(而非动作)为条件的轻量预测器预测两个未来时域的 token,并以未来帧稠密 patch 特征监督;动作解码器直接回归动作块。参数少于 1 亿且无机器人/视频预训练,在 RoboTwin 2.0 上优于十亿参数 WAM,在 LIBERO 上与十亿参数 VLA 相当;双臂真机上留出演示的动作预测误差低于微调的十亿参数 VLA,推理延迟显著更低。
- 🇬🇧 Most WAMs rely on billion-parameter VLM or video-generation backbones with high cost and latency. GAWM predicts future observations in the latent space of a frozen DINOv3 encoder: each camera view is compressed to a few tokens, a lightweight task-conditioned predictor forecasts tokens at two horizons supervised by dense patch features of future frames, and an action decoder regresses an action chunk. With <100M parameters and no robot or video pretraining it beats billion-parameter WAMs on RoboTwin 2.0, matches billion-parameter VLAs on LIBERO, and on a dual-arm robot has lower held-out action-prediction error than a fine-tuned billion-parameter VLA at much lower latency.

### [How Much Can Best-of-N Help a World Action Model? Measuring Selectable Headroom and Realizing It in Closed Loop](https://arxiv.org/abs/2610.37196) — Gao, Cao, Liu, Que 等
开源状态 / Code: ❓ 未知 / Unknown(Comments 仅页数,无代码链接或承诺)
- 🇨🇳 WAM 能想象候选动作的未来,因此适合做测试时选择,但「执行每个候选一次取最好」的标准估计把候选质量与后续随机性混在一起。作者提出去噪反事实协议(可逐比特复现的分支、重复续写、留出 oracle 与共同随机数)来测量选择器可实现的余量,并据此构建失败门控选择器。跨四个 WAM、两个基准、逾 10 万次分支 rollout:标准估计高估了原生样本的可选余量(三个 WAM 的可选份额在 24%–66%);结构化动作扰动最多制造 16 点余量;想象的未来携带的候选结果信息与真实未来相比无可检测损失。仅当 WAM 读出预测失败时才偏离策略块的选择器,把留出回合成功率由 76.9% 提至 81.6%,未见任务由 62.6% 提至 69.8%。
- 🇬🇧 WAMs can imagine futures of candidate actions, making test-time selection natural, but the standard "execute each candidate once and keep the best" estimate conflates candidate quality with downstream randomness. A denoised counterfactual protocol (bitwise-reproducible branching, repeated continuations, held-out oracles, common random numbers) measures realizable headroom and builds a fail-gated selector. Across four WAMs, two benchmarks and >100,000 branched rollouts the standard estimate overstates headroom (selectable share 24–66% for three WAMs), structured perturbations create up to 16 points of headroom, and imagined futures carry candidate-outcome information with no detectable loss vs. real futures; deviating only when failure is predicted raises success from 76.9% to 81.6% on held-out episodes and from 62.6% to 69.8% on unseen tasks.

### [World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer](https://arxiv.org/abs/2610.37518) — Wu, Cai, Zhang, Liu 等
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 多机器人控制需整合分布式相机视图并预测各自动作序列,而多数 VLA/WAM 只面向单机器人,且仅拼接多视图不能建立空间对应。World Dreamer v5-lite 围绕共享世界状态构建:预训练视频编码器的标定特征在工作空间坐标中填充该状态(视图增多时空间尺寸不变),VLM 提供场景上下文与每个机器人一个查询,查询读取共享状态并交换位姿感知信息、动作流保持独立;掩码视图协同训练让模型利用其他机器人的观测。预训练用 20 种仿真机器人、RoboFactory 与真机共逾 1 万小时轨迹;RoboFactory 平均成功率 74.0%(比最强基线高 23.7 个百分点),四个真机任务 78.8%(领先 13.8 点),RoboCasa365 总体 58.08%。
- 🇬🇧 Multi-robot control must integrate distributed camera views and predict separate action sequences, yet most VLAs/WAMs target one robot and merely concatenating views does not establish spatial correspondence. World Dreamer v5-lite builds a shared world state populated by calibrated pretrained-video-encoder features in workspace coordinates (fixed spatial size as views are added); a VLM supplies context and one query per robot, queries read the state and exchange pose-aware information while action streams stay separate, and masked-view cooperative training encourages using other robots' observations. Pretrained on >10,000 hours from 20 simulated robot types, RoboFactory and real robots, it gets 74.0% on RoboFactory (+23.7 points over the best baseline), 78.8% on four real tasks (+13.8) and 58.08% on RoboCasa365.

### [Adapting Video Models for Robot Control via Motion-guided Asymmetric Prediction (MoGAP)](https://arxiv.org/abs/2610.36624) — Kim, Sung, Kwon, Kim 等
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://ismty0805.github.io/mogap/)标注「Code (Coming Soon)」与「Checkpoints (Coming Soon)」
- 🇨🇳 WAM 借助预训练视频生成模型,通过联合预测未来视觉观测与动作来控制机器人,但继承自视频预训练的视觉预测对所有区域一视同仁。作者发现把视觉监督集中在动态区域可显著提升策略性能,并提出 MoGAP:在 WAM 训练中增加运动聚焦的视觉预测,对区域非对称加噪(动态区域噪声更重,用噪声较轻的静态区域作上下文重建),通过共享视频扩散主干内仅训练时使用的辅助路径,与标准视频—动作预测一起训练,运动线索直接取自训练视频。GR-1 桌面基准上 Fast-WAM(Wan2.2-5B)成功率由 38.8% 升到 47.5%,Cosmos3-Nano 由 52.3% 升到 62.3%。
- 🇬🇧 WAMs adapt pretrained video generators to robot control by jointly predicting future observations and actions, but video-pretraining-style prediction treats all regions uniformly. Focusing visual supervision on dynamic regions substantially helps, so MoGAP adds motion-focused prediction: noise is allocated asymmetrically (more corrupted dynamic regions reconstructed from less corrupted static context) through a training-only auxiliary path in the shared video-diffusion backbone, with motion cues taken from the training videos. On the GR-1 tabletop benchmark it raises success from 38.8% to 47.5% for Fast-WAM (Wan2.2-5B) and from 52.3% to 62.3% for Cosmos3-Nano.

### [TAPESTRY: A Single Backbone for Video Generation and Robot Control](https://arxiv.org/abs/2610.36823) — Collins, Lee, Wachakorn, Srinivasan 等(CoRL 2026)
开源状态 / Code: ❓ 未知 / Unknown(已核查[项目页](https://tapestry-wam.github.io),「Code」为占位链接,无承诺)
- 🇨🇳 利用预训练视频生成模型做机器人控制,要么需要测试时昂贵的视频生成,要么用从零训练的动作头而未充分利用预训练主干。TAPESTRY 把机器人动作视为视频潜空间中的单 patch token:轻量线性投影把每个动作时间步映射到预训练 VAE 的 patch 维度,由同一套 patchify 层与 Transformer 主干处理,并用视频扩散、视频+动作联合扩散(耦合时间步与非对称注意力掩码)、仅动作扩散三种目标训练。测试时从纯噪声一步 DDIM 生成紧凑动作 token 序列,消费级硬件上每个动作块 84 ms;仿真与真机实验表现强,推理成本显著低于同类联合视频—动作策略。
- 🇬🇧 Using pretrained video generators for control needs costly test-time video generation or action heads trained from scratch. TAPESTRY treats robot actions as single-patch tokens in the video model's latent space via a linear projection into the VAE patch dimension, processed by the same patchifying layers and transformer, trained with video diffusion, joint video+action diffusion (coupled timestep, asymmetric attention mask) and action-only diffusion. At test time it generates compact action tokens in a single DDIM step from pure noise at 84 ms per action chunk on consumer hardware, with strong simulation and real-robot results and much lower inference cost than comparable joint video–action policies.

### [SWIM: Learning What Matters from Behaviors for JEPA World Models](https://arxiv.org/abs/2610.36662) — Hu, Bo, Zheng, Wang 等
开源状态 / Code: ❓ 未知 / Unknown(Comments 仅页数,无代码链接或承诺)
- 🇨🇳 JEPA 世界模型通过预测未来嵌入从图像规划,但视觉预测目标不显式包含任务相关的状态信息;用仿真器状态监督虽有帮助,却需要决定哪些状态特征重要,手选或均匀加权会让冗余坐标重复计数、无关特征掩盖任务相关差异。SWIM 从离线轨迹学习状态权重:用逆动力学模型由当前状态与观测到的未来位移预测记录的动作,据此量化各特征对动作预测的贡献,并定义加权状态度量用于对齐潜空间与状态距离;逆动力学模型仅训练时使用,规划时无额外计算。五个仿真机器人操作任务上规划成功率持续优于均匀状态加权。
- 🇬🇧 JEPA world models plan from images by predicting future embeddings, but their objectives do not explicitly include task-relevant state, and supervising with simulator state requires choosing which features matter (hand-picked or uniform weights overcount redundant coordinates and let irrelevant ones obscure differences). SWIM learns state weights from offline trajectories with an inverse-dynamics model predicting recorded actions from current states and observed future displacements; the weights define a weighted state metric aligning latent and state distances, and the inverse model is used only in training so planning cost is unchanged. It consistently improves planning success over uniform weighting on five simulated manipulation tasks.

### [Understanding the limits of latent world models](https://arxiv.org/abs/2610.37588) — Gonzalez Laiz, Schneider
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 世界模型评估常强调任务表现,却很少检验所学潜在动力学是否反映环境结构。该工作提出「忠实潜在世界模型」概念——环境转移映射与学得潜在动力学之间的等变条件,并给出潜在 rollout 一致性(LRC)指标评估动作条件的潜在预测。结论醒目:所研究的最先进潜在世界模型没有一个是通过真正忠实地建模环境动力学来完成任务的;摘要未给出具体数值。
- 🇬🇧 World-model evaluation emphasizes task performance and rarely checks whether learned latent dynamics reflect the environment's structure. The paper defines faithful latent world models as an equivariance condition between the environment's transition map and the latent dynamics, and proposes latent rollout consistency (LRC) to evaluate action-conditioned latent prediction. The striking finding is that none of the studied state-of-the-art latent world models solves the task by faithfully modeling the environment's dynamics; no numbers in the abstract.

### [Calibrated for Which Policy? Conformal Uncertainty for Fixed World Models Under Intervention](https://arxiv.org/abs/2610.35877) — Mittal, Gupta(cross-list)
开源状态 / Code: ✅ 已开源 / Released(部分)— [Lean 4 形式化仓库](https://github.com/noumenal-ai/conformal-realrobot-lab);Comments 给出,已用匿名 `git ls-remote` 验证;仅覆盖形式化验证部分,实验代码范围未核验
- 🇨🇳 更换部署策略会使世界模型的不确定性失效,而物理转移机制与预测器并未改变。当源/目标分布共享条件机制时,干预由结果前的测度变换 w(X)=dQ_X/dP_X 识别;对策略控制的动力学,该比值可分解为状态占用与动作倾向项。加权 conformal 校准把边际覆盖率迁移到目标分布,估计比值时覆盖损失被 TV 距离及分类器对数损失遗憾所界,精确抵消把依赖由 γ^-2 阶改进到 (ργ)^-1。使用公开的 DINO 特征世界模型与 Franka 真实轨迹:最强受控状态—动作偏移下,普通 90% conformal 集合只覆盖 55.0%,而 oracle 与学得比值校准分别覆盖 91.0% 与 90.9%,并在 Lean 4 中机器检验了相关恒等式。
- 🇬🇧 Changing the deployment policy can invalidate a world model's uncertainty while the physical mechanism and predictor stay fixed. When source and target share the conditional mechanism, the intervention is identified by the pre-outcome change of measure w(X)=dQ_X/dP_X, which factors into state-occupancy and action-propensity terms for policy-controlled dynamics. Weighted conformal calibration transports marginal coverage with loss bounded by total variation and the domain classifier's log-loss regret, improving the dependence from γ^-2 to (ργ)^-1. With a released DINO-feature world model and physical Franka trajectories, ordinary 90% conformal sets cover only 55.0% under the strongest state-action shift while oracle and learned-ratio calibration cover 91.0% and 90.9%; the finite-support identities are machine-checked in Lean 4.

### [Hy-Nomas: Towards Free-form Interactive World Generation](https://arxiv.org/abs/2610.36729) — Chen, Cheng, Deng 等(Tencent Hunyuan)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Tencent-Hunyuan/Hy-Nomas);摘要称发布权重、代码与基准,HF 给出,已用匿名 `git ls-remote` 验证;[项目页](https://hy-nomas.hy.tencent.com/)
- 🇨🇳 交互式世界生成需要在多轮交互中遵循连续指令,同时保留相关历史与动作后果。Hy-Nomas 是 8B 扩散主干的视频世界模型,支持自由文本指令与连续相机控制,按当前输入和缓存历史生成变长片段;核心设计是把结构化视频字幕与动作感知因果注意力对齐(描述性上下文跨片段可见,动作指令限定在其时间窗内),视觉语言 Prompt Enhancer 把用户请求与多模态交互历史转成下一片段的结构化条件,多阶段课程逐步引入因果生成、文本交互、相机控制与模型生成历史训练,最后扩散蒸馏。人工评测中优于现有世界模型;模型权重、代码与基准及轻量适配流程均已发布。(游戏/通用世界生成,非机器人专用。)
- 🇬🇧 Interactive world generation must follow successive commands while preserving relevant history and action consequences. Hy-Nomas is an 8B diffusion video world model supporting free-form text instructions and continuous camera control across turns, generating variable-length segments from current inputs and cached history; its core design aligns structured captions with action-aware causal attention, a vision-language Prompt Enhancer turns requests and histories into structured conditions, and a multi-stage curriculum adds causal generation, text interaction, camera control and training on model-generated histories before diffusion distillation. In human evaluation it beats existing world models, and weights, code, benchmarks and a lightweight adaptation workflow are released. (General/game-style world generation, not robot-specific.)

**其余 7 条(列名)/ Remaining 7 (names only):** [Vision-Language Agents Can Learn in Their Own Latent Worlds (Dwell)](https://arxiv.org/abs/2610.36925)(VLM 作世界模型的模型式 RL;[代码](https://github.com/Tom111-lhx/Dwell))· [GameVerse](https://arxiv.org/abs/2610.37257)(分钟级游戏视频数据集,NeurIPS 2026)· [LabWorld](https://arxiv.org/abs/2610.36592)(单目视频重建交互式 4D 实验室世界)· 替换版本:[What Does World Modeling Actually Improve in Robot Action Learning?](https://arxiv.org/abs/2610.34593) · [FAWAM](https://arxiv.org/abs/2606.08555) · [Semantic World Models](https://arxiv.org/abs/2510.19818) · [DreamTacVLA](https://arxiv.org/abs/2512.23864)。
另见 / See also: [Rollback](https://arxiv.org/abs/2610.36068)(已归入 运动控制·RL)· [JAM](https://arxiv.org/abs/2610.37219)(已归入 VLA)· [ThinkWorld](https://arxiv.org/abs/2610.37666)(已归入 VLA)· [PDRVLA](https://arxiv.org/abs/2610.37381)(已归入 VLA)。

---

## 空间智能与 SLAM / Spatial Intelligence & SLAM(展开 11)

### [SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation](https://arxiv.org/abs/2610.36312) — Guo, Seyidov, Zhou 等
开源状态 / Code: 🕒 计划开源 / Planned — 摘要:「Code will be made publicly available upon acceptance」
- 🇨🇳 单目室外导航需要稳健的相机运动估计与稠密可导航地图;模块化 3DGS SLAM 把 2D 像素与 3D 点关联的跟踪误差吸收进地图,导致级联退化。SG²SLAM 将流式空间几何(用分块的公制先验取代逐帧跨维度对应,同一来源监督跟踪与建图)与射线条件 3DGS 核(为每个基元扩展感知单目视角的观察方向子空间)结合,联合优化空间几何与位姿以保证全局一致的地图与轨迹。在 KITTI 与 Waymo Open 上超过逐帧关联基线;摘要未给出具体数值。
- 🇬🇧 Monocular outdoor navigation needs robust motion estimation and a dense navigable map, but modular 3DGS SLAM absorbs tracking error from 2D–3D association into the map, causing cascading degradation. SG²SLAM couples streaming spatial geometry (chunk-level metric priors supervising tracking and mapping from one source) with a ray-conditioned 3DGS kernel that adds a viewing-direction subspace per primitive, optimizing geometry and poses jointly for a globally consistent map and trajectory. It surpasses per-frame association baselines on KITTI and Waymo Open; no numbers in the abstract.

### [LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM](https://arxiv.org/abs/2610.36853) — Li, Zang, Viola 等
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 单目 RGB 高斯泼溅 SLAM 在有限优化预算下很难兼顾高质量重建与响应迅速的相机跟踪。LingGS 把学习到的几何先验与显式几何相机跟踪结合:冻结的流式 3D 基础模型充当虚拟 RGB-D 传感器,由单目视频提供深度;显式几何求解器通过特征重投影估计相机运动;流式高斯建图器将观测整合为稠密场景表示。几何跟踪在不同流式几何主干上均提升位姿精度;室内外数据集上显著改善重建质量,单张 RTX 4090 约 7 FPS,吞吐为所评估现有 SLAM 系统的 2–3 倍。
- 🇬🇧 Monocular RGB Gaussian-splatting SLAM struggles to deliver high-quality reconstruction and responsive tracking under a limited optimization budget. LingGS combines learned geometric priors with explicit geometric tracking: a frozen streaming 3D foundation model acts as a virtual RGB-D sensor, an explicit solver estimates camera motion by feature reprojection, and a streaming Gaussian mapper builds a dense scene. Geometric tracking improves pose accuracy across several streaming geometry backbones, reconstruction quality improves significantly on indoor/outdoor datasets, and the system runs ~7 FPS on one RTX 4090 with 2–3× the throughput of the evaluated prior SLAM systems.

### [RAVEN: A Unified Active SLAM System for Rapid Autonomous Visual Exploration with Aerial Robots under Localization Uncertainty](https://arxiv.org/abs/2610.37111) — Chen, Zhang, Jiang 等(IEEE T-RO 有条件接收)
开源状态 / Code: 🕒 计划开源 / Planned — 摘要:「The source code will be released」,尚无仓库链接
- 🇨🇳 主动 SLAM 需在探索未知空间与利用已访问区域做主动回环间权衡,空中机器人敏捷但传感器受限,定位漂移更严重,且缺少随任务优先级调节的统一策略。RAVEN 先识别前沿与主动回环候选并生成全局路径候选,以分别量化探索效率与定位精度的效用向量评估,并按 [0,1] 的优先级参数选路;最后感知感知的导航规划器基于在线 Fisher 信息场生成最小化视觉状态估计误差的平滑轨迹。基准评测优于最先进主动 SLAM,并在定制立体—惯性四旋翼上完成全机载外场实验;摘要未给出具体数值。
- 🇬🇧 Active SLAM trades off exploring unknown space against active loop closure; aerial robots are agile but sensor-limited, drift more, and lack a unified strategy adapting to task priorities. RAVEN identifies frontiers and active-loop-closure candidates, generates global tours scored by a utility vector separating exploration efficiency from localization accuracy and chosen via a prioritization parameter in [0,1], then plans smooth perception-aware trajectories minimizing visual state-estimation error using an online Fisher information field. It outperforms state-of-the-art active SLAM on benchmarks and was validated in fully onboard field experiments on a custom stereo-inertial quadrotor; no numbers in the abstract.

### [RESPLE2: Inertial-Informed Recursive Non-Uniform Spline Estimation for Multi-Sensor Odometry with Global Refinement](https://arxiv.org/abs/2610.37602) — Cao, Talbot, Li 等
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/ASIG-X/RESPLE2);摘要给出,已用匿名 `git ls-remote` 验证(radar new_repos:5★);代码与实验数据集均公开
- 🇨🇳 多传感器里程计需要灵活融合 LiDAR、相机、IMU 与腿式运动学。RESPLE2 是基于非均匀 B 样条表示 6-DoF 运动的递归多传感器状态估计框架:利用节点钳制边界性质,由惯性运动学精确预测控制点(节点按运动与测量可用性自适应),在迭代扩展卡尔曼滤波中完成预测,随后重置保持轨迹一致;更新步以连续时间观测模型在原生时间戳融合异构传感器;并提供轻量全局优化模块,基于 LiDAR—视觉线索的回环约束直接精修样条控制点。在手持、履带、足式、空地混合平台的公开与自采数据集(含极端加速度)上,精度与鲁棒性具有竞争力或更优,尤其在激烈运动下,并保持实时。
- 🇬🇧 Multi-sensor odometry needs flexible fusion of LiDAR, cameras, IMU and leg kinematics. RESPLE2 is a recursive estimator using non-uniform B-splines for 6-DoF motion: knot clamping gives exact control-point prediction from inertial kinematics (knots adapted to motion and measurement availability) inside an iterated EKF with a consistency-preserving reset, continuous-time observation models fuse heterogeneous sensors at native timestamps, and a lightweight global module refines control points with LiDAR-visual loop closures. On public and own datasets across handheld, tracked, legged and hybrid aerial-legged platforms with extreme accelerations it is competitive or better in accuracy and robustness, especially under aggressive motion, in real time.

### [SVIn+: Multi-Modal Framework for Robust Underwater State Estimation using 3D Sonar, Visual-Inertial, Water-Pressure, and DVL](https://arxiv.org/abs/2610.36454) — Burgul, Zhao, Huang 等(IROS 2026)
开源状态 / Code: ✅ 已开源 / Released — 摘要称代码与数据集见[项目页](https://dartmouthrobotics.github.io/svin-plus);具体仓库链接未单独核验
- 🇨🇳 水下自主作业的状态估计在低能见度下尤其困难。SVIn+ 面向装有 IMU、相机、水压传感器、多普勒计程仪(DVL)与紧凑 3D 声纳的 AUV,扩展开源视觉惯性 SLAM SVIn,把水压与 DVL 测量紧耦合进非线性优化;为利用 3D 声纳的结构信息并保持效率,引入分层架构,由 KISS-ICP 解耦前端的估计作为相对位姿因子并入因子图。在沉船与珊瑚礁的外场部署中展示了漂移抑制与全局一致性;摘要未给出具体误差数值。
- 🇬🇧 State estimation is hard for underwater autonomy, especially in low visibility. SVIn+ targets AUVs with IMU, cameras, a water-pressure sensor, a DVL and a compact 3D sonar, extending the open-source visual-inertial SLAM SVIn by tightly coupling pressure and DVL measurements in nonlinear optimization, and adding a hierarchical architecture where a decoupled KISS-ICP front-end supplies relative-pose factors to the factor graph. Field deployments in a shipwreck and coral reef show drift mitigation and global consistency; no numeric errors in the abstract.

### [HoloRecon: Incremental Reconstruction of Long-Range Panoramas with Global Consistency](https://arxiv.org/abs/2610.36876) — Li, Liu, Hou 等
开源状态 / Code: ❓ 未知 / Unknown(摘要仅给[项目页](https://zhuoxiaoli.github.io/HoloRecon_page/),未见代码链接或承诺)
- 🇨🇳 长序列全景重建需要精细几何与远距重访间全局一致的相机位姿;全景 SLAM 与增量 SfM 依赖特征对应,重复结构与小重叠使远距连接难以建立,前馈模型局部几何好但窗口受限。HoloRecon 把基于 ORB 的稀疏全景建图前端与微调的前馈模型耦合:预测的局部几何支持对远距重访特征匹配做 3D 验证,得到长程相机约束;用稀疏地标校准预测深度,以验证过的连接优化全局位姿图并据此更新稠密几何。作者还提出七场景 PanoRecon 基准(重复建筑、大小回环、参考位姿与 LiDAR 几何),方法在所比较方法中取得最低平均绝对轨迹误差和较高 F1。
- 🇬🇧 Long panoramic reconstruction needs fine geometry and globally consistent poses across distant revisits; panoramic SLAM and incremental SfM struggle with repeated structures and small overlap, and feed-forward models have limited windows. HoloRecon couples an ORB-based sparse panoramic mapping front-end with a fine-tuned feed-forward model: predicted local geometry enables 3D verification of distant feature matches, depths are calibrated with sparse landmarks, verified links optimize a global pose graph, and dense geometry is updated. A seven-scene PanoRecon benchmark (repetitive architecture, loops, reference poses and LiDAR geometry) is introduced, and the method achieves the lowest mean absolute trajectory error and a high F-1 among compared methods.

### [Representing the Unseen: Rethinking Visual Imagination for Spatial Reasoning (ImagiRep)](https://arxiv.org/abs/2610.37437) — Zhao, Wang, Yu 等
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown(摘要仅给[项目页](https://imagirep.github.io/),未见代码链接或承诺)
- 🇨🇳 视觉世界模型常生成 RGB 视图来支持空间推理,但 RGB 只是因适合生成而成为默认接口,未必最利于推理。ImagiRep 是仿真器接地基准,含 922 个问题、七种题型、两种设置(视角想象、跨视图整合),对同一未观测状态提供 oracle RGB 与六种替代表示(深度、全景、俯视几何等)。结果表明即使准确的想象 RGB 也不保证准确空间推理,不同问题受益于不同表示;世界模型估计的状态上趋势类似,估计的 RGB 单独使用甚至会误导。据此提出轻量测试时表示选择策略 GEARS,优于现有空间想象方法;摘要未给出具体数值。
- 🇬🇧 Visual world models support spatial reasoning by generating RGB views, but RGB is the default mainly because it suits generation. ImagiRep is a simulator-grounded benchmark of 922 questions across seven types and two settings (Viewpoint Imagination, Cross-view Integration) with oracle RGB and six alternative representations (depth, panoramas, top-down geometry) of the same unobserved state. Even accurate imagined RGB does not guarantee accurate spatial reasoning, different questions benefit from different representations, and estimated RGB alone can mislead; the proposed test-time strategy GEARS adaptively selects representations and outperforms existing spatial imagination methods; no numbers in the abstract.

### [Zhengrong-Spatial-Aware 1.0: Advancing 3D Multimodal Intelligence](https://arxiv.org/abs/2610.37216) — Zhang, Wang, Cheng 等(技术报告)
开源状态 / Code: ❓ 未知 / Unknown(摘要与 Comments 均无代码链接或承诺)
- 🇨🇳 技术报告,介绍在自定义空间数据集上做 3D 感知视觉问答的两条端到端多模态适配流水线:微调用公制 3D 点图增强 RGB 的 HiSpatial-3B,以及用显存高效 QLoRA 监督微调 Qwen3-VL。工程栈覆盖数据转换、图像—标注对齐、单目几何预处理、指令构造、混合领域训练、检查点管理、批量推理与自动评测。HiSpatial 适配使整体准确率由微调前 1.73% 升到 3,600 步时 79.89%,独立风格化划分上由 14.9% 升到 55.1%;Qwen3-VL-8B 由 20.74% 升到 45.27%,32B 由 30.79% 升到 47.60%;并指出训练数据构成是专门化时保持通用多模态能力的关键因素。
- 🇬🇧 A technical report on two end-to-end adaptation pipelines for 3D-aware visual question answering on a custom spatial dataset: fine-tuning HiSpatial-3B (RGB augmented with metric-scale 3D point maps) and QLoRA-based supervised fine-tuning of Qwen3-VL. The stack covers dataset conversion, image–annotation alignment, monocular geometry preprocessing, instruction construction, mixed-domain training, checkpointing, batch inference and automated evaluation. HiSpatial rises from 1.73% to 79.89% at 3,600 steps (14.9% → 55.1% on a styled split); Qwen3-VL-8B from 20.74% to 45.27% and 32B from 30.79% to 47.60%, with training-data composition identified as central to preserving general multimodal capability.

### [Learning to Code the World: Harness Evolution for Compositional 3D Reconstruction (SceneEvolve)](https://arxiv.org/abs/2610.37046) — Yao, Lin, Du 等
开源状态 / Code: ❓ 未知 / Unknown(摘要仅给[项目页](https://haoyu-agent.github.io/SceneEvolve),未见代码链接或承诺)
- 🇨🇳 从真实图像重建可编辑的组合式 3D 场景需要联合推理几何、物体结构与空间关系。SceneEvolve 把 3D 场景表示为可执行代码,并围绕小型开源智能体演化「外壳」(harness):SceneAct 是由参数化基元、层次组合与语义空间关系构成的组合式语义动作接口,SceneHarness-RSI 利用更强教师智能体依据开发集重建反馈迭代演化 harness,期间模型参数、动作语义与执行后端保持固定。紧凑的 Qwen3.8-27B 在两个域内与一个域外数据集上改善全部四项重建指标,平均推理时间比基础模型降低 47.0%,重建质量比大型闭源 GPT-5.6-Sol 高 32.3%、等效部署成本降低 59.8%,演化出的 harness 还可迁移到 Kimi-K3。
- 🇬🇧 Reconstructing editable compositional 3D scenes from an image needs joint reasoning about geometry, object structure and spatial relations. SceneEvolve represents scenes as executable code and evolves the harness around a small open-source agent: SceneAct is a compositional semantic action interface (parameterized primitives, hierarchical composition, semantic spatial relations) and SceneHarness-RSI uses a stronger teacher to iteratively evolve the harness from development-set feedback while model parameters, action semantics and backend stay fixed. With compact Qwen3.8-27B it improves all four reconstruction metrics across two in-domain and one out-of-domain dataset, cuts mean inference time by 47.0%, achieves 32.3% higher reconstruction quality than the proprietary GPT-5.6-Sol with 59.8% lower deployment cost, and the harness transfers to Kimi-K3.

### [GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting](https://arxiv.org/abs/2610.36760) — Wang, Zhao, Zhang 等
开源状态 / Code: ❓ 未知 / Unknown(摘要仅给[项目页](https://comedy0913.github.io/projects/geogsplat),未见代码链接或承诺)
- 🇨🇳 前馈高斯泼溅的像素对齐预测使基元数随分辨率和视图数增长而冗余;非像素对齐方法预测固定数量高斯,但缺乏射线与深度约束,会导致高斯中心错位与大视角变化下的渲染伪影。GeoGSplat 把几何先验显式引入非像素对齐框架:双分支编码器构建 Anchors 与 Triplane 以获取粗 3D 结构和细粒度场景特征,层次解码器逐步解码稠密 3D 点与高斯基元,实现 3D 重建与新视角合成。在 DTU 与 NRGBD 上新视角合成与重建均超过最先进的像素对齐与非像素对齐方法,且目标视角离输入相机越远优势越大;摘要未给出具体数值。
- 🇬🇧 Pixel-aligned feed-forward Gaussian Splatting makes primitive counts grow with resolution and views; non-pixel-aligned methods predict a fixed number of Gaussians but, lacking ray and depth constraints, misplace centers and produce artifacts under large viewpoint changes. GeoGSplat injects geometric priors: a dual-branch encoder builds Anchors and a Triplane for coarse structure and fine features, and a hierarchical decoder progressively decodes dense 3D points and Gaussian primitives for reconstruction and novel view synthesis. It beats state-of-the-art pixel-aligned and non-pixel-aligned methods on DTU and NRGBD, with the advantage growing as target views move farther from the inputs; no numbers in the abstract.

### [Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction](https://arxiv.org/abs/2610.37668) — Kaushik, Paul, Yuille 等
开源状态 / Code: ❓ 未知 / Unknown(摘要仅给[项目页](https://honeycomb-surfels.github.io/),未见代码链接或承诺)
- 🇨🇳 辐射场与泼溅的内存与计算需求限制了其在资源受限场景的应用。该工作提出 Hexels:带一阶空间颜色场的平面六边形面元,用更少更大的基元利用局部平面区域与平滑变化的外观,六边形支撑域在面积与边界上更高效。34 个场景上相比内存匹配的 2DGS,PSNR 提升 4.53–7.38 dB 且训练显存更低;逐基元比较最多高 4.74 dB、FPS 快 2.31 倍;DTU 15 个扫描的表面重建误差降低 28.9%;Tanks and Temples 6 个表面场景平均 F1 34.38%(2DGS 为 31.72%),并在 2D 图像表示上优于 Image-GS。
- 🇬🇧 Memory and compute demands of radiance fields and splatting limit resource-constrained use. Hexels are planar hexagonal surface elements with a first-order spatial color field, using fewer, larger primitives that exploit locally planar regions, with hexagonal support efficient in area and boundary. Over 34 scenes they improve PSNR over memory-matched 2DGS by 4.53–7.38 dB with lower training VRAM, per primitive up to 4.74 dB higher with 2.31× faster FPS, cut DTU surface-reconstruction error by 28.9% across 15 scans, reach the highest mean F1 on 6 Tanks and Temples scenes (34.38% vs. 31.72% for 2DGS), and improve 2D image representation over Image-GS.

**另见 / See also:** [Remember Where You Walk](https://arxiv.org/abs/2610.37203)(已归入 运动控制·RL)· [E0.5](https://arxiv.org/abs/2610.36011)(已归入 世界模型与 WAM)。

---

## 其他值得关注 / Other Notable(列名,共 12)

[CLAP: Closed-Loop Aware Planning via Imitation-Free Speed Scoring for End-to-End Autonomous Driving](https://arxiv.org/abs/2610.36079)(WACV 2027)· [ExecDiffuser](https://arxiv.org/abs/2610.36837)(扩散规划,NAVSIM 92.6 PDMS)· [KEPT: Conformal Keepouts Kept in Planning](https://arxiv.org/abs/2610.37217) · [On Shaky Ground: Non-Rigid Base Effects in Mobile Manipulation](https://arxiv.org/abs/2610.36725)(ACRA 2026)· [Structure-Actuation Co-Design of All-Electric Heavy-Duty Manipulators](https://arxiv.org/abs/2610.36996) · [Ground Sample Distance Constrained k-Coverage Viewpoint Planning](https://arxiv.org/abs/2610.36450) · [EgoThumb](https://arxiv.org/abs/2610.37582) · [From Biological Curves to Soft Modular Robots](https://arxiv.org/abs/2610.36681) · [State estimation for a hybrid rigid-continuum space manipulator](https://arxiv.org/abs/2610.37043) · [Generalizable Target-Less Camera-LiDAR Calibration](https://arxiv.org/abs/2610.37350) · [FastBEVFusion](https://arxiv.org/abs/2610.37153) · [Understanding Human-Robot Collaboration through Joint Action](https://arxiv.org/abs/2610.37298)。

---

## GitHub 动态 / GitHub Highlights

### 新 release / New releases(watchlist_releases:1)

| 仓库 / Repo | 版本 / Tag | 发布时间 / Published | 主要更新 / Main changes |
|---|---|---|---|
| [leggedrobotics/rsl_rl](https://github.com/leggedrobotics/rsl_rl/releases/tag/v5.5.2) | v5.5.2 | 2026-10-28 16:03 UTC | 仅 Fixed(13 项):工作流/文档适配新的 extras 分支;折扣奖励历史不再依赖调用方存储;PPO checkpoint 恢复时续接 RND 探索调度;澄清 VecEnv 观测缓冲区生命周期;检测环境输出中的无穷值;mini-batch 生成器保留 rollout 余量;跳过单样本 PPO 优势归一化;actor/critic 共享的 CNN 编码器每次更新只前向一次;蒸馏更新间保留循环教师隐状态;纯图像 CNN 模型跳过观测归一化更新;修复日志 writer 生命周期与重复上传;循环 PPO 代理损失保留环境维度;测试清理并移除 ONNX 类中未用的 `verbose` 参数。 / 13 fixes, no new features: workflow/docs for the extras branch, reward-history/RND-resume/VecEnv-buffer fixes, infinite-value detection, mini-batch remainders, singleton advantage normalization, shared-CNN stepping, recurrent teacher hidden state, image-only normalizer skip, logging-writer fixes, env-dim preservation in recurrent PPO loss, test cleanup and removal of the unused `verbose` ONNX argument. |

其他重点项目(LeRobot、openpi、Isaac Lab、MuJoCo、GR00T、Genesis、ManiSkill、ORB-SLAM3、VGGT 等)窗口内无 release。 / No releases for the other watched projects in the window.

### star 增长明显的相关仓库 / Notable star growth (vs. 2026-10-27 baseline)

| 仓库 / Repo | ★ | Δ | 说明 / Note |
|---|---|---|---|
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | 101,004 | +694 | WiFi 信号做「空间智能」感知/生命体征,与机器人关联较弱。 / WiFi-based sensing marketed as spatial intelligence; weak robotics link. |
| [Gen-Verse/RSI-Anything](https://github.com/Gen-Verse/RSI-Anything) | 986 | +142 | 以世界模型实现递归自我改进(偏通用智能体)。 / Recursive self-improvement with world models (agent-oriented). |
| [LambdaHumanoid/openlambda](https://github.com/LambdaHumanoid/openlambda) | 112 | +25 | λ₀:开放世界第一视角人类数据用于人形 loco-manipulation;已发布训练代码与配置、G1/人类采集工具、动作对齐流水线与 Stage II 检查点(完整预训练数据未公开)。 / Open release for λ₀ egocentric-human-data humanoid loco-manipulation: training code/configs, G1 collection tools, alignment pipeline, Stage II checkpoint; full datasets withheld. |
| [Motphys/Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) | 190 | +21 | SuperMimic 在 UniLab 上的**独立复现**(非官方),G1 全身动作跟踪;README 报告 LAFAN1 40 条归一化回报 0.827。 / Independent SuperMimic reproduction (not official); G1 whole-body tracking. |
| [TianxingChen/Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide) | 16,737 | +24 | 具身智能技术指南(Lumina 社区)。 / Embodied-AI guide. |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28,553 | +27 | 常规增长。 / Steady growth. |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 15,947 | +19 | 常规增长。 / Steady growth. |
| [TencentARC/Looking-Ahead](https://github.com/TencentARC/Looking-Ahead) | 144 | +15 | 自回归视频生成中建模未来演化。 / Modeling future evolution in autoregressive video generation. |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) / [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) / [facebookresearch/vggt](https://github.com/facebookresearch/vggt) / [RLinf/RLinf](https://github.com/RLinf/RLinf) | 8,509 / 14,441 / 14,581 / 5,539 | +13 / +13 / +11 / +12 | 常规增长。 / Steady growth. |
| [ros-navigation/navigation2](https://github.com/ros-navigation/navigation2) / [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio) | 4,931 / 2,000 | +40 / +37 | Nav2;跨厂商 3DGS 训练器(视频→splat→mesh)。 / Nav2; cross-vendor 3DGS trainer. |

### 新仓库精选 / New repos worth a look(new_repos 150 条,筛选后)

- [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic)(290★,10-26):SuperMimic 相关实现/资源的汇总列表,**非官方代码**。 / A curated list of SuperMimic implementations; not official code.
- 其他 SuperMimic 第三方复现:[CumulusAlpha/Dex-Supermimic](https://github.com/CumulusAlpha/Dex-Supermimic)(63★,灵巧手)、[kaibohex/muscle-supermimic](https://github.com/kaibohex/muscle-supermimic)(26★,肌肉驱动人形/mjlab)、[RadiantForever/supermimic_wheelbipe](https://github.com/RadiantForever/supermimic_wheelbipe)(轮腿)、[Fancomi/humanoid-getup-wmbptt](https://github.com/Fancomi/humanoid-getup-wmbptt)(世界模型 BPTT 起身)。 / More third-party reproductions.
- 论文官方仓库(与上文对应):[gaoxiang12/ga-wm](https://github.com/gaoxiang12/ga-wm)(GAWM,8★)、[ASIG-X/RESPLE2](https://github.com/ASIG-X/RESPLE2)(5★)。 / Official repos of papers above.
- [H-EmbodVis/RePIC](https://github.com/H-EmbodVis/RePIC)(2★):跨重规划复用去噪轨迹,无训练地将 Fast-WAM 在 RoboTwin 2.0 与 LIBERO 上加速 2.66–2.75 倍。 / Training-free 2.66–2.75× Fast-WAM speedup by reusing denoising trajectories.
- [ApurvK032/pi-wbc](https://github.com/ApurvK032/pi-wbc)、[topsun-bot/lingxi-x2-ppo](https://github.com/topsun-bot/lingxi-x2-ppo)、[raycast-trail/go2-genesis-patrol](https://github.com/raycast-trail/go2-genesis-patrol):个人级 G1 PPO 全身控制 / 灵犀 X2 PPO 行走 / Go2 Genesis RL 巡逻,0★,仅供参考。 / Hobby-level locomotion RL repos.
- 噪声提示 / Noise: `Alpha-Park` 与 `alphaparkinc` 两账号批量创建的「GenPark embodied … skill」仓库(各 7★,内容雷同);「SLAM」一词匹配到多个法语 BTS SIO(Solutions Logicielles et Applications Métiers)课程仓库。 / Duplicate "GenPark skill" spam repos and "SLAM" collisions with French BTS SIO coursework.

---

## 今日趋势 / Today's Trends

1. **冻结基础模型 + 残差适配(运动控制)/ Frozen foundation policy + residual adaptation.** 今日至少四项工作都不重训主干,而是在冻结策略之上学习小模块:[GRAFT](https://arxiv.org/abs/2610.36507)(冻结人形跟踪器 + 地形残差)、[ARC](https://arxiv.org/abs/2610.37547)(冻结模仿策略 + RL 残差)、[VLA-Stem](https://arxiv.org/abs/2610.37378)(冻结 VLA + RL 避障干预)、[StabBot](https://arxiv.org/abs/2610.37535)(残差 RL 精修捕获)。 / At least four papers leave the backbone frozen and learn a small module on top: GRAFT, ARC, VLA-Stem and StabBot.
2. **WAM 去视频生成化 / WAMs without video generation.** [JAM](https://arxiv.org/abs/2610.37219)、[Trace-WAM](https://arxiv.org/abs/2610.36840)、[MoGAP](https://arxiv.org/abs/2610.36624)、[GAWM](https://arxiv.org/abs/2610.37091)、[PDRVLA](https://arxiv.org/abs/2610.37381) 都把未来预测作为训练期辅助目标(潜变量/3D 运动/动态区域),推理时不生成视频,并与 [TAPESTRY](https://arxiv.org/abs/2610.36823) 的单步动作 token 一起,把推理成本压下来;替换版本 [What Does World Modeling Actually Improve?](https://arxiv.org/abs/2610.34593) 也在检验这类辅助监督的真实收益。 / Several papers use future prediction purely as a training-time auxiliary and drop video generation at inference, cutting cost.
3. **世界模型用于策略改进与可信度 / World models for policy improvement and trust.** [Rollback](https://arxiv.org/abs/2610.36068) 用反事实回溯做真机策略改进,[Best-of-N WAM](https://arxiv.org/abs/2610.37196) 测量测试时选择的真实余量,[Calibrated for Which Policy?](https://arxiv.org/abs/2610.35877) 与 [Understanding the limits of latent world models](https://arxiv.org/abs/2610.37588) 则追问世界模型的不确定性与忠实度。 / World models are used for counterfactual policy improvement while others measure their headroom, calibration and faithfulness.
4. **SuperMimic 复现潮 / SuperMimic reproduction wave.** radar 在 SuperMimic 之后 3 天内发现十余个第三方复现/扩展仓库(灵巧手、肌肉驱动、轮腿、起身、G1/Go2),其中 [Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) 190★、[awesome-supermimic](https://github.com/miao-org/awesome-supermimic) 290★;官方代码仍未出现。 / A dozen-plus third-party reproductions appeared within days, while the official code has not.
5. **真机/人体层面的 RL 控制 / RL control reaching hardware and people.** [Pushing Dexterity and Safety](https://arxiv.org/abs/2610.37652)(LEAP 手 95.2%)、[MARL-Exo](https://arxiv.org/abs/2610.37441)(8 名受试者代谢降低)、[Rendering-Free Event Frame Simulation](https://arxiv.org/abs/2610.37543)(56 克无人机)、[Visuomotor Quadrotor Flight](https://arxiv.org/abs/2610.37557) 都以真机验证为终点。 / Several RL control papers end on hardware or human trials.

---

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
1. `residual policy` / `residual reinforcement learning` / `frozen policy adapter` — 适用于 arXiv 检索与 GitHub 关键词。 理由:冻结策略加残差已成为人形/操作/VLA 的通用后训练范式。 / Why: frozen-policy-plus-residual is now a common post-training pattern. 证据:GRAFT、ARC、VLA-Stem、StabBot 共 4 篇([GRAFT](https://arxiv.org/abs/2610.36507)、[ARC](https://arxiv.org/abs/2610.37547))。
2. `differentiable world model` / `world model BPTT` — 适用于 GitHub topic 与 arXiv。 理由:SuperMimic 范式正被大量复现并迁移到轮腿、起身、肌肉驱动等场景。 / Why: the SuperMimic recipe is being reproduced and transferred widely. 证据:radar 中 ≥6 个仓库,如 [humanoid-getup-wmbptt](https://github.com/Fancomi/humanoid-getup-wmbptt)、[supermimic_wheelbipe](https://github.com/RadiantForever/supermimic_wheelbipe)、[muscle-supermimic](https://github.com/kaibohex/muscle-supermimic)。

**建议观察 / Watch**
3. `musculoskeletal` / `muscle-driven control` — 适用于 arXiv。 理由:信号尚弱,但肌肉骨骼策略与外骨骼 RL 开始出现。 / Why: weak but growing signal. 证据:[MyoAcross](https://arxiv.org/abs/2610.36535)、[MARL-Exo](https://arxiv.org/abs/2610.37441)、仓库 [muscle-supermimic](https://github.com/kaibohex/muscle-supermimic)(共 3 项)。

**建议移除/收窄 / Remove or Narrow**
4. GitHub 关键词 `SLAM` 单独使用 — 理由:今日 new_repos 中大量命中法语 BTS SIO 课程项目与游戏模组而非机器人 SLAM。 / Why: bare "SLAM" matches French BTS SIO coursework and game mods; require co-terms like `visual-slam`, `lidar`, `ros`. 证据:[cinema-pathe-macon](https://github.com/emme-mouad/cinema-pathe-macon)、[brit-hotel-macon](https://github.com/emme-mouad/brit-hotel-macon)(同一账号 3 条)。

---

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 / Added | 当前状态 / Status | 今日检查 / Today's check | 备注 / Notes |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 / Unknown(无变化) | radar `signal: true`,唯一候选为 `qiayuanl/claude-meter`(macOS 菜单栏应用,与该工作无关,误报);`project_page_github_links` / `project_page_release_claims` / `arxiv_github_links` 均为空;arXiv 仍为 v1;[项目页](https://supermimic.github.io)经 WebFetch 确认无仓库链接且无「coming soon」类承诺;预设 known_repos 三个 `git ls-remote` 均不可访问;errors 为空 | 第三方复现:[Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic)(190★,独立复现)、[awesome-supermimic](https://github.com/miao-org/awesome-supermimic)(290★,资源列表)、[Dex-Supermimic](https://github.com/CumulusAlpha/Dex-Supermimic) 等;均非官方,不据此判定已开源。 |

**建议加入监测 / Suggested additions**(均为运动控制·RL,状态为「计划开源」或「未知」)

1. **REACH** — 人形 G1 爬行/变高行走的分层 RL,项目页仅承诺「Code To be released」。 / Hierarchical RL crawling for G1; the page only promises a release.
```json
{"name": "REACH", "title": "REACH: An RL-based Hierarchical Humanoid Crawling Framework for Adaptable Confined Space Traversal", "arxiv_id": "2610.36546", "search_terms": ["REACH humanoid crawling"], "owners": ["aislab-sustech"], "project_pages": ["https://aislab-sustech.github.io/REACH/"], "known_repos": []}
```
2. **Pushing Dexterity and Safety (DexSafe)** — LEAP 手 sim-only 配方与真机 95.2%,摘要称将发布完整配方,页面「Code: coming soon」。 / Sim-only LEAP recipe with 95.2% real-robot success; abstract says the recipe will be released, page says "coming soon".
```json
{"name": "DexSafe", "title": "Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well", "arxiv_id": "2610.37652", "search_terms": ["dexsafe", "in-hand object pose reaching LEAP"], "owners": ["ian-chuang"], "project_pages": ["https://ian-chuang.github.io/dexsafe/"], "known_repos": []}
```
3. **GRAFT** — 冻结人形行为基础模型(SONIC 等)的地形残差适配,G1 真机,尚无代码线索,值得跟踪是否随 SONIC 生态发布。 / Terrain residual adapter for frozen humanoid trackers with G1 hardware validation; no code signal yet.
```json
{"name": "GRAFT", "title": "GRAFT: Geometry-Aware Residual Adaptation for Foundation Trackers", "arxiv_id": "2610.36507", "search_terms": ["GRAFT humanoid", "foundation tracker residual"], "owners": ["graft-humanoid"], "project_pages": ["https://graft-humanoid.github.io/"], "known_repos": []}
```

**建议移出 / Suggested removals:** 无(SuperMimic 仍未开源)。 / None (SuperMimic is still unreleased).

---

*数据与方法说明 / Notes:* arXiv 周三列表仅 76 条新提交(较昨日少),已全部分类;所有数字均取自摘要;凡标「摘要未给出」者表示预印本摘要无定量结果。HF/radar/项目页核验见「来源状态」。 / All numbers come from abstracts; "abstract gives no numbers" means the preprint abstract has none.
