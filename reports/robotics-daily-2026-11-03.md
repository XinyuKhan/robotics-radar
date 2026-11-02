# 机器人/具身智能每日速递 — 2026-11-03 / Robotics & Embodied AI Daily — 2026-11-03

**检查窗口 / Window:** 台北时间 2026-11-02 ~07:40 → 2026-11-03 ~07:40(UTC 11-01 23:40 → 11-02 23:40)。arXiv 周一(11-02)的 cs.RO 列表覆盖周末(周五至周一)提交,本期首次处理。 / arXiv's Monday 2 Nov cs.RO listing covers Fri–Mon submissions and is processed here for the first time.

> 本期无监测项开源(SuperMimic 官方代码仍未出现),故无「🔔 监测项已开源」区块。 / No watchlist item was released (official SuperMimic code still absent), so no "🔔 Watchlist Item Released" block.

## 今日必读 / Top Picks

1. 🅰️ **[∇Mimic](https://arxiv.org/abs/2610.41654)**(运动控制·RL / Motion Control · RL;🕒 计划开源 / Planned)— 用模拟器的精确梯度 + 梯度裁剪做人形全身跟踪,在 G1 上 20 分钟达到此前世界模型方法 1.2 小时的得分。 / First-order humanoid tracking with exact simulator gradients reaches in 20 min what the prior world-model method needs 1.2 h for.
2. 🅰️ **[DiffWBC](https://arxiv.org/abs/2610.41354)**(运动控制·RL;🕒 计划开源 / Planned)— 一步扩散的通用人形动作跟踪控制器,支持测试时 steering 并已部署到 Unitree G1。 / One-step-diffusion general humanoid motion tracker with test-time steering, deployed on a Unitree G1.
3. 🅰️ **[ROOF](https://arxiv.org/abs/2610.42097)**(运动控制·RL;❓ 未知 / Unknown)— 人形在头顶障碍下的跌倒恢复,G1 真机 150 次尝试成功 95 次。 / Humanoid fall recovery under overhead obstacles; 95/150 real-robot successes on G1.
4. **[WorldBridge](https://arxiv.org/abs/2610.40748)**(世界模型与 WAM;❓ 未知 / Unknown)— 系统拆解 WAM 中视频泛化与动作泛化的各自贡献,RoboTwin 2.0 全数据设定达 96.23%。 / Disentangles video vs. action generalization in WAMs; 96.23% on RoboTwin 2.0.
5. **[Learning from Fleet Experience (CEL)](https://arxiv.org/abs/2610.25736)**(具身智能与机器人基础模型 / Embodied AI;❓ 未知 / Unknown)— 96 台真机用自身部署经验改进共享策略,多阶段包装任务成功率 79.2% → 98.3%。 / 96 real robots improve a shared policy from their own deployment experience; 79.2% → 98.3% on multi-stage packaging.

## 来源状态 / Source Status

| 来源 / Source | 状态 / Status |
|---|---|
| arXiv cs.RO 列表 / listing | ✅ 2026-11-02(周一)期:New 60 + Cross 12 + Replacements 38 = 110 条,已逐条分类(相关 ≈ 66 / 不相关其余)。 / Monday issue: 60 new + 12 cross + 38 replacements = 110, all classified. |
| arXiv API 关键词检索 / keyword search | ✅ 已运行 26 个关键词(cs.RO/AI/LG/CV,2026-10-30 14:00 UTC 起)。命中数 / hits: embodied 6, VLA 2, vision-language-action 1, humanoid 3, whole-body control 1, MPC 2, world model 2, world action model 3, WAM 1, SLAM 1;VLN、vision-language navigation、legged locomotion、reinforcement learning robot、sim-to-real、dexterous manipulation、robot foundation model、video world model、spatial intelligence、spatial reasoning、visual SLAM、LiDAR SLAM、gaussian splatting SLAM、3D reconstruction、motion tracking、motion imitation 均为 0。去重后 13 篇,其中 3 篇不在 cs.RO 列表中,仅 1 篇相关([2610.41970](https://arxiv.org/abs/2610.41970))已并入。 / 26 keywords run; 13 unique hits, 3 not in the listing, 1 relevant and merged. API 严格窗口过滤导致命中偏少。 |
| 完整摘要 / Full abstracts | ✅ 62/62 篇入选论文均通过 arXiv API `id_list` 取得完整摘要与 Comments(含 Zero-HLM);29/56 篇首批有非空 Comments。 / 62 of 62 retrieved. |
| HF Daily Papers | ✅ 取到 100 条,最新日期 2026-10-30;窗口内仅 3 条,其中带 githubRepo 的([ReLift](https://github.com/ReLift3D/ReLift)、SketchDirector)与本主题无关。 / 100 fetched; newest 2026-10-30; nothing relevant in window. |
| GitHub radar | ✅ `date_taipei` = 2026-11-03(新鲜)。new_repos 150,star_growth_top 60,watchlist_releases 为 0,oss_watch 1 项。 / Fresh; 150 new repos; no watchlist releases. |
| 开源核验 / Verification | 用匿名 `git ls-remote` 验证了 14 个仓库;[zebehn/vla-start-suppression](https://github.com/zebehn/vla-start-suppression) 与 [3dv-casia/PGGT-Loc](https://github.com/3dv-casia/PGGT-Loc) 匿名不可访问,待核实。 |

---

## 运动控制·RL / Motion Control · RL

共 14 条,全部展开。 / 14 items, all expanded.

### 1. [∇Mimic: Ultra-Efficient Humanoid Control with Differentiable Simulation](https://arxiv.org/abs/2610.41654) — Weyl Lu, Yubei Chen 等(机构未知)
🏷️ 交叉方向 / Also: 可微仿真 / Differentiable Simulation
开源状态 / Code: 🕒 计划开源 / Planned — 摘要写明 "We release NablaEngine and ∇Mimic as open-source infrastructure",但 Comments(26 pages, 7 figures)与摘要均无仓库链接,radar 也未见对应仓库。
- 🇨🇳 **问题:** PPO 等零阶方法把仿真器当黑盒,样本代价巨大;而对接触丰富的全身控制做一阶(可微)策略学习,梯度容易爆炸,此前仅有世界模型的替代梯度方案。**方法:** 作者证明仿真器的精确梯度更优:一是用逐步反传中的"中位数相对逐样本梯度裁剪"限制接触导致的无界梯度,二是对梯度导出的动作目标做多步回归以复用昂贵的仿真窗口;并实现 NablaEngine——面向 Unitree G1 的可微 GPU 仿真引擎,计算 MuJoCo 完整接触动力学,整步伴随用单个 megakernel,梯度与 float64 有限差分一致,比现有 MuJoCo Warp 伴随快 11.5 倍。**结果:** 在 LAFAN1 全部 40 个片段的单策略全身跟踪上,20 分钟达到此前世界模型方法的 0.82 分(后者需 1.2 小时),1.8 小时达到 0.874;标准一阶基线 SHAC 数分钟内即因梯度爆炸停止。
- 🇬🇧 **Problem:** Zeroth-order methods like PPO treat the simulator as a black box and need enormous sample counts, while first-order policy learning on contact-rich whole-body control usually suffers exploding gradients; a recent world-model method used surrogate gradients. **Method:** ∇Mimic shows exact simulator gradients do better once two obstacles are removed: median-relative per-sample gradient clipping at every backward step bounds rare unbounded contact gradients, and multistep regression onto gradient-derived action targets reuses each costly simulated window. NablaEngine, a differentiable GPU engine for the Unitree G1, computes MuJoCo's full contact dynamics with a single-megakernel step adjoint, matches float64 finite differences and is 11.5× faster than the MuJoCo Warp adjoint. **Results:** Tracking all 40 LAFAN1 clips with one policy, ∇Mimic reaches the prior world-model score of 0.82 in 20 minutes instead of 1.2 h, and 0.874 in 1.8 h, while SHAC stops on exploding gradients within minutes.

### 2. [DiffWBC: Unlocking Steerable General Humanoid Motion Tracking via One-Step Diffusion Whole-Body Control](https://arxiv.org/abs/2610.41354) — Yifei Huang, Yazhao Yang 等(机构未知)
🏷️ 交叉方向 / Also: 扩散模型 / Diffusion
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://diffwbc.github.io)出现 "coming soon" 字样(具体指代码/演示未核实);Comments 为空。
- 🇨🇳 **问题:** 通用人形动作跟踪器多为确定性策略,无法在线适应,需要脆弱的参考编辑或昂贵重训。**方法:** DiffWBC 把全身控制改为生成式范式:一步扩散模型建模未来轨迹分布,每个 50 Hz 控制步仅一次前向,可从 RL 教师蒸馏或用 model-based RL 从零训练;同一控制器统一了通用跟踪、测试时 steering(可微代价梯度 + 身体分组掩码)和无需仿真的失败发现(生成噪声下的计划离散度)。**结果:** 在六个通用跟踪器中取得最低局部跟踪误差(BONES 上 20.1 mm),并部署于 Unitree G1;steering 在 1.25 m 天花板场景通过率 0.84 对运动学参考编辑的 0.10;失败发现在前 2% 中精度 91%,针对性微调解决 50% 的失败片段。
- 🇬🇧 **Problem:** General humanoid motion trackers are typically deterministic and cannot adapt online without brittle reference editing or costly retraining. **Method:** DiffWBC makes whole-body control generative: a one-step diffusion model over future trajectories needs one forward pass per 50 Hz step, can be distilled from an RL teacher or trained from scratch with model-based RL, and unifies general tracking, test-time steering (differentiable cost gradients and body-group masks) and simulation-free failure discovery via plan dispersion. **Results:** Lowest local tracking error among six general trackers (20.1 mm on BONES) with deployment on a Unitree G1; steering reaches 0.84 clean pass at a 1.25 m ceiling vs. 0.10 for kinematic reference editing; failure discovery has 91% precision in the top 2%, and fine-tuning on flagged clips fixes 50% of failures.

### 3. [ROOF: Learning Humanoid Fall Recovery under Overhead Constraints](https://arxiv.org/abs/2610.42097) — Yidan Lu, Jiayuan Yu 等(机构未知)
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://lu-yidan.github.io/ROOF/),但未发现代码链接或开源承诺。
- 🇨🇳 **问题:** 人形在头顶障碍物下跌倒时,需要先腾出空间再建立支撑起身,过早站立会加剧遮挡。**方法:** 提出带"接触支撑几何逃逸引导"的 RL:奖励机器人与障碍重叠的逐步减少而不规定逃逸路径;结合学习到的动作先验、姿态相关支撑代价与关节卡滞代价,让单一策略仅凭本体感知学会何时清障、如何建立支撑、何时完成起身。**结果:** 仿真中,在只能被抬起的板下恢复率 88.5%(无几何引导为 18.9%),在随机大小/质量/位置的自由板下 98.6%;Unitree G1 真机在七个训练外的真实障碍场景(含家具与多物体)150 次尝试中恢复 95 次。
- 🇬🇧 **Problem:** A fallen humanoid under an overhead obstacle must create clearance and organize support before rising; standing too early worsens obstruction. **Method:** An RL method with contact-supported geometric escape guidance rewards incremental reduction of robot-obstacle overlap without prescribing a path, plus a learned motion prior and posture-dependent support and joint-stall costs, yielding one proprioception-only policy that decides when to clear, how to support and when to rise. **Results:** In simulation it recovers in 88.5% of trials under lift-only plates (18.9% without guidance) and 98.6% under free plates with randomized size, mass and placement; on a Unitree G1 it recovered in 95 of 150 attempts over seven unseen real-world scenes including furniture.

### 4. [HIPC: Humanoid Iterative Planning and Control via Goal-Conditioned Motion Closure](https://arxiv.org/abs/2610.41334) — Yi Han, Xingyu Chen 等(机构未知)
🏷️ 交叉方向 / Also: 生成式运动规划 / Generative Motion Planning
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://hipc-humanoid.github.io/)出现 "coming soon" 字样(具体指代码未核实)。
- 🇨🇳 **问题:** 生成式动作规划器 + 跟踪控制器通常开环耦合,跟踪误差累积成空间漂移,规划器也无法响应扰动;直接闭环回灌实际状态又因分布外导致不连续、抖动甚至摔倒。**方法:** HIPC 把生成模型与动作跟踪统一成实时迭代规划控制:用避免万向锁的规范动作表示做目标条件规划,采用"偏差衰减恢复"与"历史重锚定"缓解分布外偏移,并以带延迟补偿的异步规划-控制系统运行。**结果:** 摘要称在多种条件切换与组合下达到现有方法中最优的目标到达精度,同时对物理扰动鲁棒并能从跌倒中恢复;预印本摘要未给出具体数值。
- 🇬🇧 **Problem:** Generative motion planners paired with trackers run open-loop, so tracking errors accumulate into drift and the planner cannot react to disturbances; naively feeding realized states back is out-of-distribution and causes jitter or falls. **Method:** HIPC couples a generative planner with motion tracking in a real-time iterative loop: goal-conditioned planning with a gimbal-lock-free canonical motion representation, deviation-decayed recovery and history re-anchoring against OOD feedback, and an asynchronous system with latency compensation. **Results:** The abstract reports state-of-the-art goal-reaching accuracy among existing methods plus robustness to perturbations and fall recovery; the preprint abstract gives no quantitative numbers.

### 5. [Movens-Zero: Scaling Humanoid Motion Foundation Models with Large-Scale Human Videos](https://arxiv.org/abs/2610.41877) — Wendong Bu, Tinghong Ye 等(机构未知)
🏷️ 交叉方向 / Also: 具身基础模型 / Robot Foundation Models;数据集 / Dataset
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://movens-zero.github.io),未核实是否发布代码/数据;Comments:技术报告,86 页。
- 🇨🇳 **问题:** 人形动作基础模型受限于多样且机器人可执行数据的稀缺,以及难以在实时闭环下联合学习异构多模态输入。**方法:** 构建 Movens-5M:从互联网视频经生成片段、质量过滤、语义标注、动作恢复、物理精修(人形重定向 + 执行验证),含 1500 万人体动作序列与 500 万条物理可执行人形动作序列(超 1 万小时,对齐文本/RGB/语音/音乐);Movens-Zero 采用理解-生成-执行架构,单个动作专家以任务混合 flow matching 联合优化七类生成任务,并用多模态实时分块(Multimodal Real-Time Chunking)衔接重叠动作块实现持续闭环执行;另提出 8,192 对的 Movens-Intent 基准。**结果:** 数据从 1% 扩到 100%、动作专家从 64M 扩到 911M 参数时,四种模态均持续提升;摘要未给出单一汇总数字。
- 🇬🇧 **Problem:** Humanoid motion foundation models are limited by scarce diverse robot-executable data and by the difficulty of jointly learning from heterogeneous modalities under real-time closed-loop control. **Method:** Movens-5M is built from Internet videos via clip generation, filtering, annotation, motion recovery and physical refinement with humanoid retargeting and execution verification (15M human and 5M executable humanoid sequences, >10,000 hours, aligned with text, RGB, speech and music). Movens-Zero uses a single action expert trained with task-mixed flow matching across seven generation tasks and Multimodal Real-Time Chunking for continuous closed-loop execution, plus the 8,192-pair Movens-Intent benchmark. **Results:** Scaling execution-verified data from 1% to 100% and the action expert from 64M to 911M parameters gives consistent gains across all four modalities; no single headline number is given in the abstract.

### 6. [Joint-Health-Aware Reinforcement Learning for Robust Robot Control Under Actuator Degradation](https://arxiv.org/abs/2610.41348) — Haifa Zhang, Yijing Wang 等
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,摘要无链接。
- 🇨🇳 **问题:** 执行器权限退化会让名义动力学下训练的 RL 策略失效,现有鲁棒方法依赖离散故障标签、宽泛域随机化或全局隐变量,未显式建模逐关节的连续剩余能力。**方法:** 用连续的关节健康向量表示执行器状态,把退化建模为执行动作的乘性衰减;HealthNet 从近期观测与动作估计逐关节健康,使策略能在健康与退化关节间重新分配控制力。**结果:** 在 Walker、Go2、Cassie 与 Panda(ManiSkill)任务上优于名义与无健康估计的退化训练基线:locomotion 回报最多提升 250.1%,操作成功率最多提升 15.2 个百分点;Cassie 高退化组回报从 3.94 升至 40.50(+928.0%);仅为仿真评估。
- 🇬🇧 **Problem:** Actuator-authority degradation breaks RL policies trained under nominal dynamics, and existing robustness methods use discrete fault labels, broad domain randomization or global latents without modeling continuous per-joint residual capability. **Method:** A continuous joint-health vector models degradation as multiplicative action attenuation; a HealthNet estimator infers per-joint health from recent observations and actions so the policy can redistribute effort across healthy and degraded joints. **Results:** On Walker, Go2, Cassie and Panda ManiSkill tasks it beats nominal and no-health baselines, with locomotion returns up to +250.1%, manipulation success up to +15.2 points, and Cassie's high-degradation return rising from 3.94 to 40.50 (+928.0%); simulation only.

### 7. [FOCUS: First-Order Control Using Optimal Transport Supervision for Imitation from Observations](https://arxiv.org/abs/2610.41540) — João A. Cândido Ramos, Lionel Blondé 等
🏷️ 交叉方向 / Also: 可微仿真 / Differentiable Simulation
开源状态 / Code: ❓ 未知 / Unknown — Comments:NeurIPS 2026 Workshop;无代码链接。
- 🇨🇳 **问题:** 从仅含状态的演示做模仿学习需要恢复行为且无已知时间对应;可微仿真器给出路径梯度,但对长接触序列求导不稳定。**方法:** FOCUS 把局部最优传输对齐与短视界可微 actor-critic 结合:用软 best-of-K 目标把 rollout 窗口匹配到多个采样专家片段,传输代价作为可微模仿奖励,critic 引导超出视界的价值;不需要时间对齐轨迹、专家对齐初始化或 teacher forcing。**结果:** 在 DFlex 的接触丰富 locomotion 任务(含由 152 个肌肉激活控制的肌骨人形)上,样本效率和训练稳定性优于对抗式 imitation-from-observation 与先前可微模仿基线;摘要未给出具体数值。
- 🇬🇧 **Problem:** Imitation from state-only demonstrations lacks temporal correspondence, and differentiating through long contact-rich rollouts in differentiable simulators is unstable. **Method:** FOCUS combines local optimal-transport alignment with short-horizon differentiable actor-critic learning, matching rollout windows to several sampled expert segments with a soft best-of-K objective; transport costs act as differentiable rewards and a critic bootstraps beyond the horizon, with no need for aligned trajectories or teacher forcing. **Results:** On contact-rich DFlex locomotion tasks, including a musculoskeletal humanoid with 152 muscle activations, it improves sample efficiency and stability over adversarial imitation-from-observation and prior differentiable imitation baselines; no numbers in the abstract.

### 8. [Online Learning of Heterogeneous Locomotion Dynamics under Reinforcement Learning Policies for Precise Loco-Manipulation](https://arxiv.org/abs/2610.41892) — Tianlin Zhang, Weipeng Xia 等
🏷️ 交叉方向 / Also: 运动控制·传统(MPC)/ Classical (MPC)——RL + MPC 混合,按规则归入 RL。
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅有补充视频链接。
- 🇨🇳 **问题:** 如何复用预训练 locomotion 策略做精确 loco-manipulation;冻结策略下未观测的隐含条件使同一观测产生不同响应(异质性),直接学习会带来偏差与抖动。**方法:** 在线学习冻结 locomotion 策略下的闭环动力学:用"污染高斯"模型(两个高斯分量表示可预测/不可预测响应)结合随机傅里叶特征高斯过程,估计每个响应属于可预测分量的概率并据此加权更新;再用 MPC 预测浮动基座运动,并给出有限样本误差界。**结果:** 仿真与硬件实验在不同机械臂构型和任务下实现一致的末端跟踪,误差约 0.01 m。
- 🇬🇧 **Problem:** Reusing a pretrained locomotion policy for precise loco-manipulation is hard because unobserved latent conditions make the same observed state yield different motions, biasing direct learning. **Method:** A contaminated Gaussian model (predictable vs. unpredictable components) is combined with a random-Fourier-feature Gaussian process to weight online updates of the closed-loop dynamics under the frozen policy, and MPC then predicts floating-base motion; a finite-sample error bound is proved. **Results:** Simulation and hardware experiments show consistent end-effector tracking across manipulator configurations and tasks with errors of about 0.01 m.

### 9. [Do Earth-Trained Humanoid Controllers Walk on the Moon? Gravity, Terrain, and Soil Transfer](https://arxiv.org/abs/2610.30080) — Guillem Casadesus Vila, Sri Aditya Deevi, Grace X. Gao(替换版本 / Replacement)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,摘要无链接。
- 🇨🇳 **问题:** 月面人形作业应如何针对月球重力、地形与土壤训练 locomotion 控制器尚不清楚。**方法:** 在仿真 Unitree G1 上比较 12 种训练策略,覆盖重力、地形以及刚性/颗粒 3D 阻力理论(3D RFT)接触。**结果:** 地球训练策略在月面平坦刚性地面 10 秒回合中保持 0.64–0.75 存活率但仍持续摔倒;月球训练/微调策略在地球上全部摔倒(几乎都在 2 秒内);只有"重力随机化 + 粗糙地形 + 3D RFT 土壤"训练在所有关键测试(至多 20°)中保持地球 >0.83、月球 >0.95 的平均存活率;结论依赖接触模型与土壤刚度。
- 🇬🇧 **Problem:** How to train humanoid locomotion controllers for lunar gravity, terrain and soil is unclear. **Method:** Twelve training strategies are compared on a simulated Unitree G1 across gravity, terrain and rigid or granular 3D resistive force theory (3D RFT) contact. **Results:** Earth-trained policies keep 0.64–0.75 survival on the Moon on flat rigid ground (10 s episodes) but keep falling; Moon-trained policies fall in every Earth episode, nearly all within 2 s; only gravity-randomized rough 3D RFT training keeps mean survival above 0.83 on Earth and 0.95 on the Moon on all key tests up to 20°, with conclusions depending on contact model and soil stiffness.

### 10. [HandMimicX: Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos](https://arxiv.org/abs/2610.41336) — Zihao Gao, Yufei Liu 等
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** 从人类视频学灵巧操作时,难以把单个演示变成空间可泛化的技能并保持物理合理、拟人的手-物交互。**方法:** 提出以物体为中心的框架:从第一视角 RGB-D 视频出发,用物体运动定义 RL 目标,使技能与具体手部轨迹解耦,并对手-物交互状态施加约束以得到更自然的手部构型。**结果:** 摘要称仿真与真机实验验证了高效的视频学习与跨新空间配置的技能迁移;预印本摘要未给出定量结果。
- 🇬🇧 **Problem:** Learning dexterous manipulation from human videos struggles to turn one demonstration into a spatially generalizable skill with physically plausible, human-like interaction. **Method:** An object-centric framework from egocentric RGB-D videos defines the RL objective in terms of object motion, decoupling the skill from the hand trajectory, and constrains hand-object interaction states for anatomically natural hand configurations. **Results:** Simulation and real-robot experiments are said to show efficient learning from videos and transfer across novel spatial configurations; the abstract gives no quantitative results.

### 11. [AC-SMPC: Differentiable Actor–Critic MPC with State Constraints for Safe and Fast Robot Navigation](https://arxiv.org/abs/2610.41477) — Chaoran Wu, Jiayu Fan 等
🏷️ 交叉方向 / Also: 运动控制·传统(MPC)/ Classical (MPC)——RL + MPC 混合,归入 RL。
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** 现有 actor–critic MPC 的可微 MPC 层难以显式处理状态约束,无法把避障纳入学习式规划。**方法:** 用顶点表示机器人与障碍、半空间表示工作空间,将非线性动力学局部线性化并把超平面避碰约束凸化进可微 MPC 层;actor 利用闭环反馈调整 MPC 目标参数,critic 评估长期性能,并用带界惩罚松弛变量形成弹性 QP。**结果:** 仿真与多机器人窄环境动态避碰实验显示在保持运动安全的同时提升导航效率;摘要未给出具体数值。
- 🇬🇧 **Problem:** Differentiable MPC layers in actor–critic MPC cannot readily accommodate explicit state constraints, blocking collision avoidance in learned planning. **Method:** Robot and obstacles are vertex sets and the workspace is half-spaces; dynamics are linearized and hyperplane collision constraints convexified into the differentiable MPC layer, with the actor tuning MPC objective parameters from closed-loop feedback, a critic evaluating long-term performance, and bounded penalized slack variables forming an elastic QP. **Results:** Simulation and multi-robot narrow-space experiments show better navigation efficiency while maintaining safety; no numbers in the abstract.

### 12. [π-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs](https://arxiv.org/abs/2603.02083) — Siting Wang, Xiaofeng Wang 等(替换版本 / Replacement)
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ❓ 未知 / Unknown — 仅有[项目页](https://wangst0181.github.io/pi-StepNFT/),未发现代码仓库。
- 🇨🇳 **问题:** 基于流的 VLA 多步去噪使策略梯度式在线 RL 困难,因为采样器诱导的最终动作似然不可直接计算,且探索与监督存在错配。**方法:** π-StepNFT(逐步负感知微调)把观察到的 SDE 转移当作监督单元,用方差归一化的转移误差对镜像的正/负速度分支排序,把 rollout 反馈映射为局部速度更新,无需最终动作似然。**结果:** LIBERO 上从共享少样本 SFT 初始化出发,π0 平均成功率从 57.6% 升至 92.0%,π0.5 从 77.1% 升至 94.0%;在 ManiSkill 的五种仅测试视觉扰动上取得已评估 RL 基线中最高的平均成功率。
- 🇬🇧 **Problem:** Multi-step denoising makes policy-gradient online RL for flow-based VLAs hard: the final-action likelihood is intractable and exploration and supervision are mismatched. **Method:** π-StepNFT treats observed SDE transitions as supervision units, ranking mirrored positive/negative velocity branches by variance-normalized transition errors and mapping rollout feedback to local velocity updates, without final-action likelihood. **Results:** On LIBERO from shared few-shot SFT initializations, π0 rises from 57.6% to 92.0% and π0.5 from 77.1% to 94.0%; on ManiSkill it has the highest mean success among evaluated RL baselines on five test-only visual perturbations.

### 13. [ResMerge: Residual Policy Learning and Merging for Continual Adaptation of Pre-trained Robot Policies](https://arxiv.org/abs/2610.41663) — Kefei Zhu, Lingyun Xu 等
🏷️ 交叉方向 / Also: VLA / 持续学习 / Continual Learning
开源状态 / Code: ✅ 已开源 / Released — [官方仓库](https://github.com/ResMerge/resmerge-official);Comments 给出链接,匿名 `git ls-remote` 验证可访问;另有[项目页](https://resmerge.github.io/)。
- 🇨🇳 **问题:** 机器人持续适应新任务时,参数增长与持续采集演示是障碍;每任务一个适配器的 PECFT 仍需演示且随任务数增长。**方法:** 两阶段:在冻结预训练策略上用残差 RL 获得任务修正(适应阶段无需专家演示),再对兼容残差做参数空间合并以减少存储参数;提出 Residual-Field Consistency(RFC)指标,在残差动作场空间比较修正方向与幅度来评估兼容性。**结果:** 在 LIBERO(两种骨干)与真实 Franka 机器人上,持续学习表现优于强 PECFT 基线,选择性合并降低残差参数量;摘要未给出具体数值。
- 🇬🇧 **Problem:** Continual adaptation of pre-trained robot policies is hampered by parameter growth and repeated demonstration collection; adapter-per-task PECFT needs demos and grows with tasks. **Method:** Residual RL learns task-specific corrections on a frozen policy without extra demonstrations, then parameter-space merging consolidates compatible residuals; the Residual-Field Consistency (RFC) metric measures compatibility via correction direction and magnitude. **Results:** On LIBERO with two backbones and a real Franka robot it outperforms strong PECFT baselines and selective merging shrinks the residual footprint; no numbers in the abstract.

### 14. [Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data](https://arxiv.org/abs/2610.35075) — GitHub 新仓库 / New repo [BIGAI-General-Vision-Lab/Zero-HLM](https://github.com/BIGAI-General-Vision-Lab/Zero-HLM)(8★,2026-10-31 创建)
🏷️ 交叉方向 / Also: 具身基础模型 / Robot Foundation Models(GR00T N1.7)
开源状态 / Code: ✅ 已开源 / Released — [官方仓库](https://github.com/BIGAI-General-Vision-Lab/Zero-HLM);仓库描述称目前包含 Zero-HLM-Bench、仿真训练数据集与策略检查点(训练/生成代码是否包含未核实);论文发布于 2026-10-26,仓库为本窗口前一两日创建;匿名 `git ls-remote` 验证可访问。
- 🇨🇳 **问题:** 人形 loco-manipulation 受限于昂贵的真机演示;仿真虽可扩展,但需要视觉逼真、可物理仿真的场景和可执行的全身动作。**方法:** Zero-HLM 是 real-to-sim-to-real 框架:Gaussian 引导的 agentic 实景重建对齐视觉与物理场景,运动-环境协同适配利用 rollout 反馈修正全身参考与交互几何,把手机拍摄与仿真源演示转为训练数据。**结果:** 生成 4,800 条经物理验证的演示,在三个 Unitree G1 任务上零样本迁移;仿真训练的 GR00T N1.7 平均整任务成功率 66.7%(真机数据训练为 46.7%);泛化配置上,扩展仿真训练使合并成功率从真机数据基策略的 23% 升至 69%,且无需额外真机演示。
- 🇬🇧 **Problem:** Humanoid loco-manipulation is bottlenecked by costly real demonstrations, and simulation needs visually faithful, physics-ready scenes and executable whole-body motions. **Method:** Zero-HLM is a real-to-sim-to-real framework: Gaussian-guided agentic reconstruction aligns visual and physical scenes, and motion-environment co-adaptation uses rollout feedback to correct whole-body references and interaction geometry, turning smartphone captures and simulated source demos into training data. **Results:** It generates 4,800 physically validated demonstrations for zero-shot transfer across three Unitree G1 tasks; simulation-trained GR00T N1.7 reaches 66.7% mean full-task success versus 46.7% with real-data training, and on generalized configurations pooled success rises from 23% to 69% without extra real demonstrations.

---

## 运动控制·传统 / Motion Control · Classical

共 8 条,全部展开。 / 8 items, all expanded.

### 1. [Geometry-Aware Humanoid Retargeting via Manifold ODEs](https://arxiv.org/abs/2610.41349) — Pengyu Zhu, Heye Wang 等
🏷️ 交叉方向 / Also: 动作模仿的重定向前端 / Retargeting for motion imitation
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** 保持与物体/地形空间关系的交互保持型重定向(如 OmniRetarget)逐帧需反复 SQP 迭代,代价高。**方法:** 把逐帧 KKT 条件的连续时间极限建模为机器人构型流形上的 ODE:既将 OmniRetarget 的 SQP 解释为其后向离散并给出局部收敛性,又得到前向离散的新方法 TaSP-KKT,每步只需一次加权切锥投影和闭式流形更新。**结果:** 数值实验显示重定向质量与 OmniRetarget 相当(略低),速度约为其两倍。
- 🇬🇧 **Problem:** Interaction-preserving retargeting such as OmniRetarget needs repeated SQP iterations per frame. **Method:** The continuous-time limit of framewise KKT conditions is modeled as an ODE on the robot configuration manifold, interpreting OmniRetarget's SQP as a backward discretization (with local convergence) and yielding TaSP-KKT, a forward scheme needing one weighted tangent-cone projection and a closed-form manifold update per step. **Results:** Retargeting quality is comparable to, though slightly below, OmniRetarget while running about twice as fast.

### 2. [CuPIQP: A Batched and Differentiable QP Solver on GPUs for Robot Learning and Control](https://arxiv.org/abs/2610.41021) — Fenglong Song, Roland Schwan 等
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,摘要无链接。
- 🇨🇳 **问题:** 逆运动学、WBC、MPC 都依赖 QP,大规模机器人学习需要并发求解大量 QP 并可微。**方法:** 基于近端内点法的 GPU 批量可微 QP 求解器,统一支持稠密、稀疏与多阶段问题,利用独立 QP 间并行并保留每个问题各自的数值更新与终止判据。**结果:** 每批至多 16384 个 QP 时,求解时间最多比 Moreau 快 18.8 倍、比八核 PIQP 快 4.26 倍;端到端学习任务中训练比 QPAX 快 4.6 倍、比 Moreau 快 7.8 倍。
- 🇬🇧 **Problem:** IK, whole-body control and MPC rely on QPs, and large-scale robot learning needs many concurrent, differentiable QP solves. **Method:** A batched differentiable GPU QP solver based on a proximal interior-point method supports dense, sparse and multistage problems, exploiting cross-problem parallelism while keeping per-problem numerical updates and termination. **Results:** With up to 16384 QPs per batch it is up to 18.8× faster than Moreau and 4.26× faster than eight-core PIQP; end-to-end training is 4.6× faster than QPAX and 7.8× faster than Moreau.

### 3. [Confidence-Modulated Safety Filtering for End-to-End Policies](https://arxiv.org/abs/2610.40922) — Javier Borquez, Jaime F. Fisac
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** 端到端策略不保证安全,常被安全滤波器包裹,但滤波器保守程度固定,不随策略能力变化。**方法:** 提出与滤波器无关的流程,运行时用策略置信度调节保守度:在滤波器运行设计域(ODD)内置信度换性能,域外低置信度增加裕度。**结果:** 初步 F1TENTH 仿真显示调制后的滤波器兼具宽松与保守滤波器的优点;仅为初步结果,无具体数值。
- 🇬🇧 **Problem:** End-to-end policies lack safety guarantees and are wrapped in safety filters whose conservativeness is fixed regardless of the policy's competence. **Method:** A filter-agnostic pipeline modulates conservativeness at runtime using policy confidence: inside the operational design domain confidence buys performance, beyond it low confidence adds margin. **Results:** Preliminary F1TENTH simulations show the modulated filter combining strengths of permissive and conservative filters; no numbers given.

### 4. [Capability-Conditioned Graph Control Barrier Functions for Zero-Shot Safe Navigation of Heterogeneous Mobile Robot Teams](https://arxiv.org/abs/2610.41214) — 作者见 arXiv
开源状态 / Code: ❓ 未知 / Unknown — Comments:9 页,无链接。
- 🇨🇳 **问题:** 图控制障碍函数(GCBF)通常假设同质机器人动力学,对异构、未见机器人模型难以零样本迁移。**方法:** 提出 CC-HGCBF,在共享二阶参考点操作空间中定义安全,并引入"径向能力场"(RCF)表示各机器人随状态变化的有限视界可达速度集,将屏障函数与去中心化策略以 RCF 为条件,用主动安全标注与神经 CBF-QP 监督联合训练。**结果:** 在含已见/未见机器人的混合队伍上展示可扩展的安全协同与对训练中未见机器人模型的零样本迁移,物理机器人实验也零样本部署到未见运动学模型;摘要未给出具体数值。
- 🇬🇧 **Problem:** GCBF methods assume homogeneous dynamics and transfer poorly to unseen heterogeneous robots. **Method:** CC-HGCBF defines safety in a shared second-order reference-point space and introduces the Radial Capability Field (RCF), a compact representation of each robot's state-dependent reachable velocity set; barrier and decentralized policy are conditioned on it and trained jointly with proactive safety labels and neural CBF-QP supervision. **Results:** Mixed seen/unseen teams show scalable safe coordination and zero-shot transfer, and physical experiments deploy zero-shot to unseen kinematic models; no numbers in the abstract.

### 5. [Contact-based optimization for collision-free motion planning for a million robots](https://arxiv.org/abs/2610.41548) — 作者见 arXiv
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** 多机器人双积分器轨迹的最小能量规划受非凸避碰约束耦合,整条轨迹离散优化在大规模机群上代价过高。**方法:** 围绕"接触"(机器人达到最小间距的时刻)组织优化,对接触变量建立耦合代数系统并解析重建接触间轨迹;算法 SCI 从无约束轨迹出发,在违反间距处插入接触并联合调整时间与状态。**结果:** 一百万机器人规划需数分钟,数千机器人只需几分之一秒;在固定网格序列凸规划基线可行的问题上,中位数加速达数个数量级且精度相当。
- 🇬🇧 **Problem:** Minimum-energy double-integrator planning for large fleets is expensive because collision constraints couple trajectories nonconvexly. **Method:** Sequential contact insertion (SCI) organizes optimization around contacts, forms a coupled algebraic system in contact variables, reconstructs inter-contact trajectories analytically, and inserts contacts at separation violations while jointly adjusting their times and states. **Results:** One million robots are planned in minutes and thousands in fractions of a second, with median speedups of several orders of magnitude over fixed-grid sequential convex programming at matching accuracy.

### 6. [A complete analytical characterization of optimal collision-free motion for two robots](https://arxiv.org/abs/2610.41558) — 作者见 arXiv
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空;理论类论文。
- 🇨🇳 **内容:** 针对从静止出发并静止到达的两个机器人,在双积分器动力学与平方加速度目标下,推导最优无碰轨迹的完整解析刻画。**结论:** 证明最优轨迹属于八个不同的接触族,并确定各起终点配置对应的族,分析其几何性质并给出数值算法,讨论如何改进现有数值轨迹优化器;无定量基准结果。
- 🇬🇧 **Content:** For two robots starting and ending at rest under double-integrator dynamics and a squared-acceleration objective, the paper derives a complete analytical characterization of optimal collision-free trajectories. **Conclusion:** The optimal trajectories fall into eight contact families, with a rule for which applies per start/goal configuration, plus geometric analysis and a numerical algorithm; no quantitative benchmark results.

### 7. [Higher-Order Kinematic Derivatives for Aspect-Preserving Real-Time Numerical Inverse Kinematics](https://arxiv.org/abs/2610.41752) — 作者见 arXiv
开源状态 / Code: 🕒 计划开源 / Planned — 摘要称"A C++ library is released with ROS 2 integration",但未给链接,未核实。
- 🇨🇳 **问题:** 实时数值逆运动学需要高效且能保持构型"aspect"、避免奇异。**方法:** 推导高阶求解器族(QuIK4/QuIK5,四/五阶收敛,含朝向误差修正映射);以雅可比行列式外推的步长限制器仅在朝奇异方向时缩短步长;用 Hermite 插值认证器验证 aspect,并由认证重启算法从已证同 aspect 种子恢复失败。**结果:** 失败次数最多降低四个数量级,在跟踪级误差下几乎消除 aspect 切换。
- 🇬🇧 **Problem:** Real-time numerical IK needs efficiency while preserving aspect and avoiding singularities. **Method:** Higher-order solvers (QuIK4/QuIK5, fourth/fifth-order convergence with an orientation-error correction map), an aspect-preserving step limiter extrapolating the Jacobian determinant, and a Hermite-interpolation certifier with certified restarts. **Results:** Failures drop by up to four orders of magnitude and aspect switching is nearly eliminated at tracking-level errors.

### 8. [Actuator-Aware Observer Inputs for Cascade ADRC of Quadrotors Under Rotor Lag, Measurement Delay and Sensor Noise](https://arxiv.org/abs/2610.39126) — 作者见 arXiv(替换版本 / Replacement)
开源状态 / Code: ✅ 已开源 / Released — 摘要给出[代码仓库](https://github.com/Quang61123/actuator-aware-cascade-adrc)(控制器增益、随机种子、逐种子结果);匿名 ls-remote 验证可访问。
- 🇨🇳 **问题:** 采样级联 LADRC 中扩张状态观测器常接收瞬时指令,而延迟测量反映的是更早、经旋翼滤波的加速度。**方法:** 提出执行器感知(AA)观测器输入:高度/姿态观测器使用经假设旋翼模型滤波并与测量延迟对齐的受限虚拟输入,水平观测器用由测量姿态重建的加速度;增益在离散模型上按灵敏度、阶跃响应及各通道控制方差的平稳协方差上限选取。**结果:** 配对设定点试验中 PID-Budget、AA-Budget、AA-HalfGain 平均 RMSE 为 65.5、19.2、16.9 mm;PX4 SITL 重现;在 EKF2 后 AA-Budget-E 把 RMSE 从 59.1 mm 降到 44.0 mm;证据仅来自仿真。
- 🇬🇧 **Problem:** In sampled cascade LADRC the observer gets the instantaneous command though the delayed measurement reflects earlier, rotor-filtered acceleration. **Method:** Actuator-aware observer inputs use limited virtual inputs filtered by a rotor model and aligned with measurement delay (attitude-reconstructed acceleration for horizontal channels), with fixed gains chosen under sensitivity, step-response and stationary covariance ceilings. **Results:** Set-point mean RMSE is 65.5 / 19.2 / 16.9 mm for PID-Budget / AA-Budget / AA-HalfGain, reproduced in PX4 SITL; behind EKF2, AA-Budget-E cuts RMSE from 59.1 to 44.0 mm; simulation-based evidence only.

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

共 19 条,详细展开 12 条,其余列名。 / 19 items; 12 expanded, 7 listed.

### 1. [Learning from Fleet Experience: Collective Experience Learning Across 96 Robots](https://arxiv.org/abs/2610.25736) — Chao Yu, Shu'ang Yu 等(替换版本 / Replacement)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** 机器人部署会产生经验,但依赖专家纠正动作难以随机群规模扩展。**方法:** 提出集体经验学习(CEL):机器人汇集自身执行经验更新共享策略;通过失败引导的经验检索微调(FERT)用失败上下文检索成功轨迹片段并优先监督其动作,无需额外专家演示,仅需操作员的二元结果标签与环境复位;容错异步训练系统 FATS 协调执行、云端推理与优化。**结果:** 五个真机操作任务上成功率 93.3–99.2%(每任务 120 次试验,机器人未参与训练采集);每机采集时间固定时更大机群普遍更好;多阶段手机包装任务 96 台机器人使成功率从 79.2% 升至 98.3%。
- 🇬🇧 **Problem:** Deployment generates experience, but relying on expert corrections does not scale with fleet size. **Method:** Collective Experience Learning pools execution experience into a shared policy; FERT retrieves successful-trajectory segments using failure contexts and prioritizes their actions for supervised updates without extra expert corrections (only binary outcome labels and resets), with the fault-tolerant asynchronous system FATS coordinating robots, cloud inference and training. **Results:** Five real-world tasks reach 93.3–99.2% success (120 trials each, on robots excluded from data collection), larger fleets generally help, and 96 robots raise multi-stage phone packaging from 79.2% to 98.3%.

### 2. [I3L: Iterative Interactive Imitation Learning for Whole-Body Mobile Manipulation](https://arxiv.org/abs/2610.17748) — Wensi Ai, Christopher Luey 等(替换版本 / Replacement)
🏷️ 交叉方向 / Also: 运动控制(模仿学习为主,非 RL / imitation, not RL)。归类理由:贡献是纠正数据采集硬件 + 迭代 HG-DAgger,非 RL 控制策略学习。
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://i-3l.github.io/)(JoyLo+ 称低成本开源接口,仓库链接未核实)。
- 🇨🇳 **问题:** 离线遥操作演示训练的策略在分布外退化,长时程全身移动操作中误差累积且难以穷尽覆盖。**方法:** I3L 将全身纠正与迭代策略精炼结合:低成本开源 JoyLo+ 接口(跟随策略的主臂 + 触摸触发接管)支持跨身体部位协调纠正,迭代部署与重训使操作员针对更新后策略的失败。**结果:** 三种机器人形态、八个仿真/真实任务(含四个长时程全身移动操作)上,四轮 HG-DAgger 使自主成功率较基础策略平均提高 68.3 个百分点,每个任务至少 90%,比同轨迹数的仅演示训练平均高 35.6 个百分点;每回合接管时长四轮下降 72%。
- 🇬🇧 **Problem:** Offline teleoperation-trained policies degrade out of distribution, especially in long-horizon whole-body mobile manipulation. **Method:** I3L pairs whole-body correction (the low-cost open-source JoyLo+ with policy-tracking leader arms and touch-triggered takeover) with iterative deployment and retraining that targets the updated policy's failures. **Results:** Over three embodiments and eight tasks, four-round HG-DAgger raises autonomous success by 68.3 points on average, reaches ≥90% on every task, beats demonstration-only training by 35.6 points, and cuts takeover duration per episode by 72%.

### 3. [REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control](https://arxiv.org/abs/2610.42053) — Pengfei Zhou, Yixing Ma 等
🏷️ 交叉方向 / Also: VLA;运动控制(摘要含 G1 人形与全身控制器)。归类理由:贡献是脑-小脑运行时与调度,非控制策略学习。
开源状态 / Code: ✅ 已开源 / Released — radar new_repos 中的 [InfRec-Cardinal/REA](https://github.com/InfRec-Cardinal/REA)(2★,描述为 "Official repository for REA");ls-remote 验证可访问;HF Daily Papers 44 upvotes,githubRepo 字段为空。
- 🇨🇳 **问题:** 基础模型推理强但太慢,VLA/全身控制器反应快但泛化弱;脑-小脑组合缺乏统一栈,异步协调困难(代理调用 VLA 会阻塞,VLA 调用代理易重复触发或漏掉静默失败)。**方法:** REA 是统一运行时:System 2 深思、System 1 路由、System 0 反应策略,遵循"运行中的策略不等待大脑"原则,用预先测得成功率的路由记忆、边界触发的评判门与共享预算的升级阶梯。**结果:** LIBERO-Pro 60 任务 3,000 回合成功率 95.9%(池内最佳单智能体 94.7%),控制步数减少 25%、控制时间减少 17%;RoboTwin 2.0 100 回合 VLA 84%、VLA+代码 86%(最强单 VLA 基线 MEDex 80%);并迁移到 BEHAVIOR-1K 与 Unitree G1 真机。
- 🇬🇧 **Problem:** Foundation models reason well but are too slow for fine control, while fast VLAs and whole-body controllers generalize poorly; brain-cerebellum pairings lack a common stack and asynchronous coordination. **Method:** REA is a runtime with a deliberative System 2, a router System 1 and reactive System 0 policies under the rule that no running policy waits on the brain, using route memory of measured success, a boundary-triggered judge gate and a shared-budget escalation ladder. **Results:** 95.9% success on 3,000 LIBERO-Pro episodes (best single-agent in pool 94.7%) with 25% fewer control steps and 17% less control time; 84% / 86% (VLA / VLA+code) on RoboTwin 2.0 vs. 80% for MEDex; it also transfers to BEHAVIOR-1K and a real Unitree G1.

### 4. [CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents](https://arxiv.org/abs/2610.40799) — Yijia Fan, Xilin He 等
开源状态 / Code: 🕒 计划开源 / Planned — 摘要称 "We release all code, data, and model weights",无链接,未核实。
- 🇨🇳 **问题:** 现有 code-as-policy 智能体要么提示闭源前沿模型,要么依赖预训练 VLA,小型开源 VLM 直接失败。**方法:** CaPtain 先在合成轨迹上 SFT,再做多轮 RL;为解决数十次请求的信用分配,引入读取策略不可见的特权仿真状态的物理 critic,按每次请求对成功概率预测的改变量记功;在 CaPtain-Harness 中暴露感知、几何与受保护运动原语。**结果:** 从 Qwen3.5-4B(零样本 0%)出发,LIBERO 留出集 SFT 后 55.4%、RL 后 73.8%;LIBERO-PRO 78.5%,超过若干前沿模型智能体,三个扰动套件 RL 增益 +17.6 至 +21.2 点;SimplerEnv WidowX 无目标域训练 83.3%,并在仅仿真适配后上真机。
- 🇬🇧 **Problem:** Code-as-policy agents prompt closed frontier models or rely on pretrained VLAs, and small open VLMs fail outright. **Method:** CaPtain does SFT on synthetic trajectories then multi-turn RL, with a physical critic that reads privileged simulator state (unseen by the policy) to credit each request by its change in predicted success chance, inside a harness of perception, geometry and guarded-motion primitives. **Results:** From Qwen3.5-4B (0% zero-shot), held-out LIBERO success is 55.4% after SFT and 73.8% after RL; LIBERO-PRO 78.5%, beating several frontier-model agents (+17.6 to +21.2 points RL gains over three perturbation suites); 83.3% on SimplerEnv WidowX without target-domain training, and it runs on a real robot after sim-only adaptation.

### 5. [TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents](https://arxiv.org/abs/2610.41216) — Kehong Gong, Xiaoxu Zheng 等
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://garfield-kh.github.io/TinyAstral/),未发现代码链接。
- 🇨🇳 **问题:** 基于 VLM 的机器人智能体依赖规划器及其外围 harness(工具、反馈、记忆、恢复逻辑),能否把大教师的 harness 改进带入低算力小模型?**方法:** 两阶段:先冻结开源教师,通过递归自我改进(RSI)改进其 harness(前沿 LLM 智能体读取轨迹提出修改,经配对统计检验才接受);再冻结 harness,收集带推理与失败恢复的教师轨迹,蒸馏小学生模型。**结果:** RoboTwin 上教师成功率 33.4% → 63.6%,4B 学生达 62.8%;在三个未用于 RSI 的基准上接近 552B 规划器,部署回合中仅用教师约五分之一加速器时间。
- 🇬🇧 **Problem:** VLM robot agents depend on both planner and harness (tools, feedback, memory, recovery); can a large teacher's harness gains be carried into a cheap compact agent? **Method:** Freeze an open-weight teacher and improve its harness via recursive self-improvement (edits accepted only after a paired statistical test), then freeze the harness and distill a small student from teacher trajectories with reasoning and recovery. **Results:** On RoboTwin the teacher rises 33.4% → 63.6% and the 4B student reaches 62.8%; on three benchmarks unused for RSI it is close to a 552B planner, using about one fifth of the teacher's accelerator time.

### 6. [Learning from Physical Experience: Context-Space Adaptation for Robotic Manipulation (LEXP)](https://arxiv.org/abs/2610.41320) — Yihan Zeng, Yisu Li 等
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** 多模态基础模型感知与推理强,但转化为物理动作仍难。**方法:** 发现通用推理模型可作为情境响应的操作策略,并提出 LEXP:任务级规划 + 经验模块(解读执行证据、保留带适用条件的教训并复用于后续反馈),模型权重与动作接口固定。**结果:** 12 个真机操作任务 23/36 成功(63.9%),仅记忆为 19/36(52.8%),原始模型 2/36(5.6%);三任务消融显示去掉规划从 7/9 降到 4/9,去掉保留经验降到 3/9。
- 🇬🇧 **Problem:** Multimodal foundation models perceive and reason well but struggle to turn this into physical action. **Method:** LEXP wraps a general reasoner used as a manipulation policy in task-level planning and an experience module that interprets execution evidence, retains lessons with applicability conditions and reuses them as feedback, with weights and action interface fixed. **Results:** Across 12 real-world tasks LEXP gets 23/36 (63.9%) vs. 19/36 (52.8%) with memory only and 2/36 (5.6%) for the vanilla model; removing planning drops three-task success from 7/9 to 4/9 and removing retained experience to 3/9.

### 7. [Contact Imitation Interface: Transferring Dexterous Skills by Showing How Contact Unfolds (CIMI)](https://arxiv.org/abs/2610.41028) — Zhixuan Xu, Yichen Li 等
开源状态 / Code: ✅ 已开源 / Released — [项目页](https://nus-lins-lab.github.io/CIMIWeb/)(Comments 称含代码与硬件设计);仓库直链未核实。
- 🇨🇳 **问题:** 无机器人的人类演示可扩展灵巧数据,但需保留人的自然灵巧性并产生可迁移的接触落地观测与动作。**方法:** CIMI 含接触落地演示接口(共享接触几何与指尖 RGB,接触对齐优先重定向并重投影更宽场景视图)和学习接口(分层策略:接触面规划器预测相对接触面轨迹,控制器协调腕与手指指令)。**结果:** 在 LEAP 与 Wuji 手的六个手-任务对上,平均最终阶段成功率比基线至少提升 50 个百分点。
- 🇬🇧 **Problem:** Robot-free human demonstrations scale dexterous data but must preserve natural dexterity and yield contact-grounded observations and actions that transfer. **Method:** CIMI has a demonstration interface (shared contact geometry, fingertip RGB, contact-alignment-first retargeting) and a hierarchical policy where a contact-surface planner predicts relative contact trajectories and a controller coordinates wrist and finger commands. **Results:** Mean final-stage success improves by at least 50 points over baselines across six hand-task pairs on LEAP and Wuji hands.

### 8. [Direct Action-Manifold Modeling for Efficient and Robust Bimanual Manipulation (DMAT)](https://arxiv.org/abs/2610.41643) — Hongren Wang, Mingyu You 等
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** 扩散/flow matching 视觉运动策略需迭代去噪,带来延迟与执行失配。**方法:** DMAT 将动作生成改为从随机插值直接建模干净、观测条件的关节空间动作块,实现单步推理;局部 3D 几何锚定预测,状态一致谱-时间精炼(STR)使其与本体感知一致并抑制高频残差。**结果:** 每方法 567 次标准与 OOD 试验中,相对 IDP3 与 DiTFlow3D 的总体成功率相对提升 129.1% 和 95.7%,动作块生成快 2.06× 与 1.34×,并在重复 50 N 干预下保持鲁棒。
- 🇬🇧 **Problem:** Diffusion and flow-matching visuomotor policies need iterative denoising, adding latency and execution mismatch. **Method:** DMAT directly models clean observation-conditioned joint-space action chunks from stochastic interpolants for single-step inference, with local 3D geometry anchoring and State-Consistent Spectral-Time Refinement reconciling chunks with proprioception. **Results:** Over 567 standard and OOD trials per method it improves aggregate success by 129.1% and 95.7% relative to IDP3 and DiTFlow3D, generates chunks 2.06× and 1.34× faster, and stays robust under repeated 50 N interventions.

### 9. [RTPolicy: Real-Time (32.9 Hz) Multi-View Visuomotor Policy for Robotic Manipulation on Edge Devices](https://arxiv.org/abs/2610.41625) — Xianbao Hou, Zehao Ni 等
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://d-robotics-ai-lab.github.io/RTPolicy.project),未发现代码链接。
- 🇨🇳 **问题:** 现有视觉运动策略视觉骨干昂贵,异步推理下延迟与部署开销高。**方法:** 视角感知特征融合 + 视觉压缩,把多视角信息聚合成紧凑 token,条件化 flow-matching 动作生成器以降低成本。**结果:** RoboTwin 2.0 单任务 50 任务平均成功率 52.26%,高于最强榜单基线 π0(46.4%);真机双臂异步流式推理 72.0%,RDK S600 上 30.35 ms(32.9 Hz)、RDK S100 上 149.72 ms(6.7 Hz,INT16)。
- 🇬🇧 **Problem:** Existing visuomotor policies use costly visual backbones, giving high latency and deployment cost under asynchronous inference. **Method:** View-aware feature fusion with visual compression aggregates multi-view information into compact tokens conditioning a flow-matching action generator. **Results:** 52.26% mean success on 50 RoboTwin 2.0 tasks vs. 46.4% for π0; on a real bimanual platform 72.0% success with 30.35 ms (32.9 Hz) on RDK S600 and 149.72 ms (6.7 Hz) on RDK S100, both INT16.

### 10. [MolmoSpaces-CommonSense: Evaluating Commonsense in Robotic Manipulation Policies](https://arxiv.org/abs/2610.41377) — Arjun Guru, Max Argus, Jae Sung Park, Jiafei Duan 等
开源状态 / Code: ✅ 已开源 / Released — [allenai/molmospaces](https://github.com/allenai/molmospaces)(代码与榜单,Comments 给出,ls-remote 验证可访问)。
- 🇨🇳 **内容:** 基于发展认知科学提出机器人操作推理分类法,并构建 MolmoSpaces-CommonSense 基准,要求对遮挡、包含、支撑、语义正确抓取点、空间可供性与隐藏物体做推理。**结论:** 零样本通用策略普遍失败:杂乱场景随干扰物增加成功率下降超 50%,30% 情形操作了错误物体,可供性敏感抓取的物体部位选择仅约 50% 正确;VLM 成功判定也不可靠,说明现有基准可能高估真实世界就绪度。
- 🇬🇧 **Content:** A taxonomy of manipulation reasoning from developmental cognitive science is operationalized in MolmoSpaces-CommonSense, requiring reasoning about occlusion, containment, support, semantically correct grasp points, affordances and hidden objects. **Conclusion:** Zero-shot generalist policies fail consistently: success drops by over 50% as distractors grow, incorrect objects are acted on 30% of the time, and correct part selection for affordance-sensitive grasping is only about 50%; VLM-based success estimation is also unreliable, so existing benchmarks may overestimate readiness.

### 11. [When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks (SimuGuard)](https://arxiv.org/abs/2610.41857) — Alex Zhou, Junhao Wu 等
开源状态 / Code: ✅ 已开源 / Released — [ALEXander22568/simuguard](https://github.com/ALEXander22568/simuguard);Comments 给出,ls-remote 验证可访问。
- 🇨🇳 **问题:** 仿真基准以成功率评分,但许多失败源于仿真器而非策略(物体被放置后被引擎弹飞,基准自带脚本演示也同样失败)。**方法:** SimuGuard 审计插件(LIBERO、RoboTwin、RoboCasa、RoboDojo)逐物理步记录状态、标记超出接触/重力解释的加速,支持逐位重放与单参数变更重跑;将 RoboTwin 问题追溯到物理引擎碰撞检测中丢弃小面积三角形的一个常量。**结果:** 仅改此常量,含伪影回合从 100 中 12 降为 0,五个容器任务成功率从 89% 升至 98%;LingBot-VA 报告的 83.1% 对应 75.8%–98.5% 的区间。
- 🇬🇧 **Problem:** Simulation benchmarks count simulator-caused failures against policies: placed objects get ejected, even in the benchmark's own scripted demos. **Method:** SimuGuard (a plugin for LIBERO, RoboTwin, RoboCasa and RoboDojo) records state each physics step, flags unexplained contact accelerations, replays bit-for-bit and reruns with one parameter changed, tracing RoboTwin artifacts to a distance-algorithm constant that discards small triangles. **Results:** Changing only that constant drops artifact episodes from 12 in 100 to none and raises five container tasks from 89% to 98%; a reported 83.1% for LingBot-VA spans 75.8%–98.5%.

### 12. [From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation](https://arxiv.org/abs/2610.40828) — Ammar N. Abbas, Aayush Jain 等
开源状态 / Code: ❓ 未知 / Unknown — Comments:CoRL 2026 Workshop;无代码链接。
- 🇨🇳 **内容:** 在 RJ45 连接器抓取与插入任务上,用五指机器人手评估七个策略族的 281 个模仿学习策略(约 1,700 次真机试验)。**结论:** 观测与动作表示的影响远大于优化器与采样选择:点云策略的 ROI 裁剪、基座系表示与点编码器归一化各提升成功率 70–100 个百分点,VLA 的绝对(而非相对)动作预测使插入成功率最多提升 70 个百分点;67 个离线指标中仅 5 个(预测动作的平滑度与直接性)与插入成功率相关(r = −0.70 至 −0.80),且仅限单一策略族,离线指标只能筛选不能替代真机评估。
- 🇬🇧 **Content:** 281 imitation-learning policies from seven families were evaluated in about 1,700 real-robot RJ45 grasp-and-insert trials with a five-fingered hand. **Conclusion:** Observation and action representations dominate optimizer and sampling choices (point-cloud ROI cropping, base-frame representation and encoder normalization each add 70–100 points; absolute rather than relative actions raise a VLA's insertion success by up to 70 points), and of 67 offline metrics only five smoothness/directness measures correlate with success (r = −0.70 to −0.80), within one policy family, so offline metrics can shortlist but not replace real-robot evaluation.

**其余 7 条(列名)/ Remaining 7 (listed):** [TRACE](https://arxiv.org/abs/2610.41275)(PPO 后训练 VLA 跟踪器的执行时风险门,分心场景碰撞率 −3.96 点)· [When the Past Shapes Action: Understanding Embodied Memory](https://arxiv.org/abs/2610.41688)(具身记忆综述)· [UniCross](https://arxiv.org/abs/2607.28198)(统一跨技能灵巧操作合成)· [TacClaw-Infinity](https://arxiv.org/abs/2610.20320)(视觉-触觉-语言-动作数据集,>1 万小时/100 万回合)· [META-Robot](https://arxiv.org/abs/2610.41868) · [SketchMate](https://arxiv.org/abs/2610.41844)(零样本精密插入,69 个仿真回合插入 88%)· [Cross-Embodiment Motion Planning (Hourglass)](https://arxiv.org/abs/2610.41330)(见世界模型小节 / see World Models)。

另见 / See also: [Movens-Zero](https://arxiv.org/abs/2610.41877)(已归入 运动控制·RL)、[Zero-HLM](https://arxiv.org/abs/2610.35075)(已归入 运动控制·RL)。

---

## VLA / VLN

VLA 6 条 + VLN 2 条,全部展开。 / 6 VLA + 2 VLN, all expanded.

### 1. [VLA Policies Do Not Know When Not to Act: Unintended Task Execution and Start Suppression](https://arxiv.org/abs/2610.41609) — Minsu Jang, Jae-Woo Choi 等
开源状态 / Code: ✅ 已开源 / Released — Comments 给出 [zebehn/vla-start-suppression](https://github.com/zebehn/vla-start-suppression);链接匿名不可访问,待核实。
- 🇨🇳 **内容:** 在 LIBERO-Goal 仿真中,对六个 VLA 检查点用空、中性、无意义、不可行与错误任务指令的配对协议,考察机器人是否启动、完成哪个任务。**结论:** 即使指令为空,六个检查点在每个回合都开始运动,其中五个常常完成未被指定的任务;两个 GR00T 检查点中指令决定做哪个任务但不决定是否运动。三种抑制方法:提示前缀对六个检查点均无效,门控(首个动作块与空指令近似相等则保持不动)在五个上有效,微调从不完成非任务输入但不能可靠保持静止且对不可行指令失败。
- 🇬🇧 **Content:** Six VLA checkpoints were probed on LIBERO-Goal with empty, neutral, nonsense, infeasible and wrong-task instructions. **Conclusion:** Even with an empty instruction all six checkpoints started moving in every episode and five often completed an unspecified task; on two GR00T checkpoints the instruction chose the task but not whether to move. A prompt prefix stopped none of the six, a gate comparing the first action chunk with the empty-instruction one held five of six, and fine-tuning never completed a task on non-task inputs but did not reliably stay still and failed on infeasible instructions.

### 2. [STAR: Steering Action Representations during Inference](https://arxiv.org/abs/2610.41009) — Guangyu Zhao, Yongchang Zhang 等
开源状态 / Code: ✅ 已开源 / Released — [PKU-VaLuE-Lab/STAR](https://github.com/PKU-VaLuE-Lab/STAR);摘要给出,ls-remote 验证可访问。
- 🇨🇳 **问题:** 探测实验发现 VLA 靠近动作输出的表示未充分保留任务相关的视觉落地(后层落地缺口)。**方法:** STAR 是免训练推理方法:对后层残差更新做指数滑动平均,让后层动作表示继承前层的物体感知更新方向,并按近期本体感知状态调节混合强度(动力学变化快时保守混合)。**结果:** 提高后层物体感知,在机器人操作基准上平均任务成功率提升 4.0 个百分点。
- 🇬🇧 **Problem:** Probing shows action representations near the VLA output do not fully preserve task-relevant visual grounding. **Method:** STAR is training-free: an exponential moving average over late-layer residual updates lets later representations inherit object-aware directions from earlier layers, with mixing strength adapted to recent proprioception. **Results:** It improves late-layer object awareness and raises average manipulation success by 4.0 points.

### 3. [Nexus-VLA: Bridging Human and Robot Experiences via a Shared Hierarchical Semantic Latent Space](https://arxiv.org/abs/2610.42021) — Biaoliang Guan, Tingyu Yuan 等
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** 第一视角人类视频提供丰富操作经验,但视觉外观、运动学与动作空间存在具身差距,现有方法把跨具身对齐与策略学习割裂。**方法:** 端到端的人-机联合训练,分层跨具身语义对齐(从任务意图到细粒度交互),并设计直接用于连续动作生成的共享操作隐表示。**结果:** RoboCasa-GR1 任务成功率 80.5%,并在 OOD 设定与真机实验中展现人类数据利用、学习效率与跨场景泛化优势。
- 🇬🇧 **Problem:** Egocentric human videos offer rich manipulation experience, but embodiment gaps in appearance, kinematics and action spaces hinder transfer, and existing methods decouple alignment from policy learning. **Method:** End-to-end human-robot joint training with hierarchical cross-embodiment semantic alignment (task intent to fine interactions) and a shared manipulation latent used directly for continuous action generation. **Results:** 80.5% task success on RoboCasa-GR1, with advantages in human-data use, learning efficiency and cross-scenario generalization in OOD and real-robot experiments.

### 4. [SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models](https://arxiv.org/abs/2610.41408) — Haesung Lee, Insu Han
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** VLA 内存占用大,沿用 LLM 的超低比特 PTQ 在 VLA 上退化,且未考虑下游运算结构与对动作的影响。**方法:** SACQ 为权重向量码本量化:结构感知码本拟合(角色特定二次度量)、基于最终动作误差增量的动作感知混合比特分配、两阶段量化后精炼(带二阶误差补偿的码字重分配 + 对解码动作校准码本)。**结果:** 以 GR00T N1.7 为例,语言/动作权重 1.5 bit 时 LIBERO 四套件平均成功率 93.85%,内存减少 4.83×;加 INT8 激活与低精度注意力保持 93.55% 且比 BF16 快 1.51×;SimplER 上 2 bit 达 63.76% 与 52.27%(BF16 为 58.90% 与 53.45%)。
- 🇬🇧 **Problem:** VLAs have large memory footprints and LLM-derived ultra-low-bit PTQ degrades on them, ignoring downstream structure and action impact. **Method:** SACQ is weight-only vector-codebook quantization with structure-aware codebook fitting, action-aware mixed-bit allocation from final-action error increase, and two-stage refinement (second-order index reassignment, codebook calibration against decoded actions). **Results:** On GR00T N1.7, 1.5-bit weights keep 93.85% average on four LIBERO suites with 4.83× less memory; with INT8 activations 93.55% at 1.51× speed over BF16; on SimplER at 2 bits 63.76% / 52.27% vs. BF16 58.90% / 53.45%.

### 5. [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381) — Hanqing Wang, Zhaotian Cai 等(替换版本 / Replacement)
🏷️ 交叉方向 / Also: 世界模型 / World Model
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** VLA 对物理动力学理解有限,视频世界模型能捕获动力学但生成未来视频会给控制回路带来高延迟。**方法:** 轻量物理动力学模块从视觉-语言特征提取物理 token 来条件化动作生成,无需在线视频生成;通过直接预测未来 RGB、深度与光流特征学习,并以冻结的预训练视频世界模型提供辅助监督;训练全用公开数据(人到机器人合成、子任务与 ECoT 标注)。**结果:** 四个仿真基准成功率 LIBERO 99.3%、LIBERO-Plus 89.9%、RoboTwin 2.0 93.6%、SimplerEnv 81.5%。
- 🇬🇧 **Problem:** VLAs understand physical dynamics poorly, while video world models capture it but generating future video adds latency to control. **Method:** A lightweight Physical Dynamics Module extracts physical tokens from vision-language features to condition action generation without online video generation, learned by predicting future RGB, depth and optical-flow features with auxiliary supervision from a frozen video world model, trained on public data expanded with human-to-robot synthesis, subtask and ECoT annotations. **Results:** 99.3% LIBERO, 89.9% LIBERO-Plus, 93.6% RoboTwin 2.0 and 81.5% SimplerEnv.

### 6. [OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation](https://arxiv.org/abs/2610.39287) — Junli Liu, Zhongrui You 等(替换版本 / Replacement)
🏷️ 交叉方向 / Also: VLN / 空中机器人
开源状态 / Code: 🕒 计划开源 / Planned — 摘要称 "Code will be made publicly available";Comments 中 [Ideal-ljl/AeroBrain](https://github.com/Ideal-ljl/AeroBrain) 仓库经 ls-remote 已可访问(内容完整度未核实)。
- 🇨🇳 **问题:** 空中机器人的感知、指代、空间推理与控制系统多为专用、依赖离线算力,难在资源受限平台闭环运行。**方法:** 统一的机载 VLA 架构,共享视觉-语言表示支撑语义理解、语言落地感知、空间推理与连续飞行控制;紧凑动作专家输出短视界航点,运动感知时间记忆与动作先验降低计算;构建约 7 万条导航轨迹与 6 万对视觉-语言指令-回答的仿真数据集。**结果:** 在 Jetson Orin NX 上完全机载以 10 Hz 生成 12 航点动作块;无真实飞行训练数据即零样本迁移到真实四旋翼,四个真实环境导航成功率 48%。
- 🇬🇧 **Problem:** Aerial robots' perception, grounding, spatial reasoning and control are usually specialized, offboard and hard to run closed-loop on constrained hardware. **Method:** A unified onboard VLA with a shared vision-language representation, a compact action expert emitting short-horizon waypoints, motion-aware temporal memory and action priors, plus a simulated dataset of ~70,000 trajectories and 60,000 instruction-response pairs. **Results:** It generates 12-waypoint chunks fully onboard at 10 Hz on a Jetson Orin NX and transfers zero-shot to a real quadrotor with 48% navigation success across four real environments without real aerial training data.

### VLN 1. [MOON: Learning When to Forget and How to Move On in Vision-and-Language Navigation](https://arxiv.org/abs/2610.33546) — Jingmeng Zhou, Seson Sun 等(替换版本 / Replacement)
开源状态 / Code: ✅ 已开源 / Released — [AutoLab-SAI-SJTU/MOON](https://github.com/AutoLab-SAI-SJTU/MOON);摘要给出,ls-remote 验证可访问。
- 🇨🇳 **问题:** VLN 策略依赖视觉历史,错误动作会偏离路线,偏离后保留的历史造成"行为惯性"。**方法:** MOON 给冻结的 VLN 策略加两个轻量模块(<1% 参数):偏离判别器判断何时清空历史,以及用 GRPO 从警报状态训练的恢复策略学习如何继续。**结果:** R2R-CE 上取得对比方法中最高成功率,并把冻结基础策略的成功率在 R2R-CE 和 RxR-CE 上分别提高 5.2 和 6.0 个点;随机触发消融表明增益取决于清空时机;无需再训练即可提升 HM3D-OVON 零样本物体目标导航。
- 🇬🇧 **Problem:** VLN policies act on visual history, so a wrong action can derail them, and retained history then causes behavioral inertia. **Method:** MOON adds two modules (<1% parameters) to a frozen policy: a deviation judge deciding when to clear history and a recovery policy trained with GRPO from alarm states. **Results:** Highest R2R-CE success among compared methods, +5.2 and +6.0 points over the frozen base on R2R-CE and RxR-CE, a random-trigger ablation showing timing matters, and gains on zero-shot HM3D-OVON object-goal navigation without retraining.

### VLN 2. [VEGA: Learning Navigation VLAs from In-the-Wild Egocentric Video with Geometric Trajectory Supervision](https://arxiv.org/abs/2606.18426) — Gershom Seneviratne, Yohan Abeysinghe 等(替换版本 / Replacement)
🏷️ 交叉方向 / Also: VLA;空间智能 / Spatial Intelligence
开源状态 / Code: 🕒 计划开源 / Planned — 摘要称 "The code and benchmark will be released at the time of publication"。
- 🇨🇳 **问题:** 互联网第一视角视频缺少以机器人坐标系表示、受导航目标约束的避障轨迹,无法直接训练策略。**方法:** VEGA 从单目视频重建局部场景几何,采样文本/图像/空间航点目标并生成避障轨迹,用以训练 flow-matching 导航 VLA(几何仅用于训练);并提出含 25 万场景、约 500 万导航目标的 VEGA-Bench。**结果:** 在 VEGABench 上目标进度有竞争力,碰撞比最强基线减少 33.0%、障碍间隙提升 17.9%;真机试验成功率至少提升 150.0%、碰撞至少减少 66.7%、间隙至少提升 60.0%。
- 🇬🇧 **Problem:** In-the-wild egocentric videos lack obstacle-aware, goal-conditioned trajectories in the robot frame, so they cannot directly train policies. **Method:** VEGA reconstructs local geometry from monocular video, samples text/image/waypoint goals, generates obstacle-aware trajectories and trains a flow-matching navigation VLA (geometry only at training time), with the 250k-scene, ~5M-goal VEGA-Bench. **Results:** Competitive goal progress with 33.0% fewer collisions and 17.9% better clearance than the strongest baseline on VEGABench, and in real-world trials ≥150.0% higher success, ≥66.7% fewer collisions and ≥60.0% better clearance.

另见 / See also: [π-StepNFT](https://arxiv.org/abs/2603.02083)、[ResMerge](https://arxiv.org/abs/2610.41663)(均已归入 运动控制·RL)。
**其他 VLA 相关(列名)/ Other VLA-related (listed, 1):** [Detect and Suppress](https://arxiv.org/abs/2610.03498)(用稀疏自编码器检测并条件抑制 VLA 对抗补丁特征,LIBERO-10;Comments:CoRL 2026 Workshop;替换版本)。

---

## 世界模型与 WAM / World Models & WAM

共 8 条,全部展开。 / 8 items, all expanded.

### 1. [WorldBridge: Bridging Video and Action for Task Generalization in World Action Models](https://arxiv.org/abs/2610.40748) — Jun Cen, Yubo Guo 等
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://worldbridge-jd.github.io/),未发现代码链接。
- 🇨🇳 **问题:** 具身模型的广义任务泛化是核心挑战;WAM 中视频泛化与动作泛化各贡献多少?**方法:** 在 RoboTwin 2.0 上改变域外任务的视频与动作监督;据此提出 WorldBridge:独立视频专家与动作专家通过结构化注意力连接并联合 flow matching 训练,含双时间尺度视觉记忆、动作强迫及统一的数据处理管线。**结果:** 仅用分布内视频-动作监督,域外任务成功率 25.07%;加入无动作标签的任务视频升至 55.90%;每任务再加一条带动作示范升至 70.70%;WorldBridge 在 RoboTwin 2.0 全数据达 96.23%(clean→random 80.9%),RoboCasa GR1 TableTop 82.8%,DOMINO Level-1 57.6%。
- 🇬🇧 **Problem:** Broad task generalization is central for embodied models; how much do video vs. action generalization contribute in WAMs? **Method:** Varying video and action supervision for out-of-distribution tasks on RoboTwin 2.0 motivates WorldBridge, with separate video and action experts linked by structured attention and trained with joint flow matching, two-scale visual memory, action forcing and a unified data pipeline. **Results:** In-distribution supervision alone gives 25.07% OOD success, adding action-free task videos 55.90%, plus one action demonstration per task 70.70%; WorldBridge reaches 96.23% on RoboTwin 2.0 full data (80.9% clean-to-random), 82.8% on RoboCasa GR1 TableTop and 57.6% on DOMINO Level-1.

### 2. [CausalWAM: Learning the Causes of Actions in World Action Models](https://arxiv.org/abs/2610.42096) — Juntao Cheng, Jinzhou Tang, Fan Feng, Henrik I. Christensen
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** WAM 预测整个场景,但只有一部分导致动作;拟合演示不保证动作只来自动作相关隐变量,可能与干扰变量纠缠。**方法:** 证明在稀疏约束下,生成动作的隐变量是动作相关隐变量的可逆函数且结构可辨识(至排列);CWAM 在预训练 WAM 的动作头加稀疏路由路径,世界建模目标不变。**结果:** 合成数据与真机实验验证理论并显示闭环成功效率提升;摘要未给出具体数值。
- 🇬🇧 **Problem:** WAMs predict the whole scene though only part of it causes actions, and fitting demonstrations does not ensure actions come only from action-relevant latents. **Method:** Under a sparsity constraint, action-generating latents are provably an invertible function of the action-relevant latents (identified up to permutation); CWAM adds a sparse routing path to a pretrained WAM's action head, leaving the world-modeling objective unchanged. **Results:** Synthetic and real-robot experiments validate the theory and show improved closed-loop efficiency; no numbers in the abstract.

### 3. [When Does Test-Time Search Help World Action Models? An Empirical Audit of Candidate Selection and Simulator Integrity](https://arxiv.org/abs/2610.41970) — Jun Liu, Dajie Sun 等
开源状态 / Code: ❓ 未知 / Unknown — 摘要称发布检测器、修复与脚本,未给链接。
- 🇨🇳 **内容:** 在 Cosmos Policy 与 RoboCasa 上以预注册方法审计 WAM 测试时扩展的三个前提:候选信号、效率、评测可靠性。**结论:** 干净数据上学习的价值选择器比随机差 1.66 个百分点,事后最优仅提升 1.40 点(置信区间跨零),82% 状态候选结果相同;token 剪枝减少至多 47% FLOPs 但端到端最多只快 1.15×(未达 1.5× 目标),自适应分配实验不确定;并发现一种随规划计算增加而升高的静默渲染损坏并给出修复。
- 🇬🇧 **Content:** A pre-registered audit of three premises of test-time scaling for WAMs on Cosmos Policy and RoboCasa. **Conclusion:** On clean data a learned value selector is 1.66 points worse than random, a hindsight oracle gains only 1.40 points (interval spanning zero) and 82% of states have identical candidate outcomes; token pruning cuts FLOPs by up to 47% but yields at most 1.15× end-to-end speedup (target 1.5×), adaptive allocation is inconclusive, and a silent rendering corruption is identified and fixed.

### 4. [Hierarchical World Models with Implicit Dynamics (ID-WM)](https://arxiv.org/abs/2610.42146) — Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui, Nicolas Ballas 等
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://id-wm.github.io),未发现代码链接。
- 🇨🇳 **问题:** 世界模型规划在长时程任务中受累积误差与搜索复杂度限制,现有分层方法的宏动作/隐技能脆弱。**方法:** ID-WM 将状态空间可达性与局部控制解耦:高层模型在状态流形上采样可行转移,低层世界模型作为逆动力学求解器将转移落地为精确动作。**结果:** 三个导航与操作套件上比最先进的策略与扩散规划器高 38.5%,相对单层世界模型 MPC 性能提升 135%。
- 🇬🇧 **Problem:** World-model planning on long-horizon tasks suffers from compounding errors and search complexity, and hierarchical methods use brittle macro-actions or latent skills. **Method:** ID-WM decouples state-space reachability from local control: a high-level model samples feasible transitions on the state manifold and a low-level world model acts as an inverse-dynamics solver to ground them in actions. **Results:** On three navigation and manipulation suites it improves 38.5% over state-of-the-art policy and diffusion planners and 135% over single-level world-model MPC.

### 5. [Cross-Embodiment Motion Planning by Coupling Body-Agnostic World Model with Differentiable Ego-Dynamics (Hourglass)](https://arxiv.org/abs/2610.41330) — Zhidong Wang, Zirui Li 等
🏷️ 交叉方向 / Also: 运动控制(MPPI 教师、想象训练策略)。归类理由:任务是杂乱场景中的跨具身运动规划/导航命令(平地、相机自运动),非人形/足式 locomotion 控制策略 RL。
开源状态 / Code: ❓ 未知 / Unknown — Comments:8 页,无链接。
- 🇨🇳 **问题:** 杂乱环境运动规划与具身相关,跨具身策略输出归一化命令忽略差异,世界模型的潜在动力学又绑定单一动作空间。**方法:** Hourglass 以相机自运动为接口:与具身无关的世界模型(跨具身数据训练)+ 各机器人的可微自运动动力学(低阶模板);在该接口学习一次参数条件通用策略,想象训练时先过模板再过世界模型。**结果:** 七个仿真机器人、五种运动类型上,比同世界模型的模仿学习与扩散策略基线高 3.8–10.6 个百分点,匹配逐机器人专家,逼近其 MPPI 教师(差 1.4–2.8 点);经三分钟遥操作辨识后,仅合成数据训练的模型零样本迁移到未见的真实滑移转向机器人。
- 🇬🇧 **Problem:** Motion planning in clutter is embodiment-specific; cross-embodiment policies output normalized commands and command-conditioned world models bind latent dynamics to one action space. **Method:** Hourglass couples a body-agnostic world model (trained on pooled data) with each robot's differentiable reduced-order ego-dynamics through camera ego-motion, learning one parameter-conditioned generalist policy by imagination through template then world model. **Results:** On seven simulated robots of five locomotion types it beats imitation and diffusion baselines on the same world model by 3.8–10.6 points, matches per-robot specialists, comes within 1.4–2.8 points of its MPPI teacher, and after three minutes of teleoperated identification transfers zero-shot to an unseen real skid-steer robot.

### 6. [Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling (GenSight)](https://arxiv.org/abs/2610.39232) — Haitang Feng, Zhuoman Liu 等(替换版本 / Replacement)
🏷️ 交叉方向 / Also: 空间智能 / Spatial Intelligence(4D 感知)
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://gensight-rbs.github.io/),未发现代码链接。
- 🇨🇳 **问题:** 具身世界模型不仅要想象未来,还应感知演化世界的几何、语义与运动。**方法:** GenSight 在单个预训练视频 DiT 中统一未来视频生成与密集感知(视频、深度、具身体分割、首帧相对 2D 光流),轻量任务调制、统一速度预测空间;推理支持多步未来视频生成(含对齐密集预测)与单步密集感知。**结果:** 在跨多机器人形态与人手交互的操作数据上,视频生成与密集 4D 感知均表现强;摘要未给出具体数值。
- 🇬🇧 **Problem:** Embodied world models should also perceive geometry, semantics and motion of the evolving world. **Method:** GenSight unifies future video generation and dense perception (video, depth, embodiment segmentation, first-frame-relative 2D flow) in one pretrained video DiT with lightweight task modulation and a unified velocity-prediction space; inference supports multi-step video generation with aligned dense outputs and single-step dense perception. **Results:** Trained on multi-embodiment and human-hand manipulation data it shows strong video generation and 4D perception; the abstract gives no numbers.

### 7. [SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.03602) — Jinyang Wang, Shiwei Li 等(替换版本 / Replacement;自动驾驶 / driving)
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://jinyangwang427.github.io/SV-WAM/),未发现代码链接。
- 🇨🇳 **问题:** 驾驶世界模型生成未来视频开销大,多采用单前视相机,限制变道、并线等机动的空间覆盖。**方法:** SV-WAM 保留六相机输入,把未来视频预测作为联合生成模型的稠密训练监督而非推理输出;动作中心因果掩码阻止动作 token 注意未来视频 token,部署时可丢弃视频分支;另加可微可行驶区域合规正则。**结果:** 在闭环 NAVSIMv2 与开环 nuScenes 上达到最先进规划性能,低推理延迟并有竞争力的零样本迁移;摘要未给具体数值。
- 🇬🇧 **Problem:** Driving world models avoid video generation cost by using only a front camera, limiting spatial coverage for lane changes, merges and turns. **Method:** SV-WAM keeps six cameras and uses future-video prediction as dense training supervision, with an action-centered causal mask so the video branch can be dropped at deployment, plus a differentiable drivable-area compliance regularizer. **Results:** State-of-the-art planning on closed-loop NAVSIMv2 and open-loop nuScenes with low latency and competitive zero-shot transfer; no numbers in the abstract.

### 8. [Adaptive-WAM: Quality-Guided Early-Exit Planning from Intermediate Video-Diffusion Features](https://arxiv.org/abs/2608.06008) — Sining Ang, Yuguang Yang, Yan Wang(替换版本 / Replacement;自动驾驶 / driving)
开源状态 / Code: 🕒 计划开源 / Planned — 摘要称 "Code will be released"。
- 🇨🇳 **问题:** 驾驶 WAM 继承迭代未来视频生成的成本,而部署只需自车轨迹。**方法:** 对视频去噪时间步与 DiT 深度的受控研究发现规划对视频噪声水平不敏感、中间层即可解码强轨迹;据此在 Wan2.2-5B 上建质量感知多出口规划器,在选定 DiT 块接轨迹扩散头,轻量轨迹质量评分器达到阈值即终止。**结果:** NAVSIM 单轨迹 90.8 PDMS(64 提议固定出口 92.6),NAVSIM v2 89.9 EPDMS;零样本迁移 nuScenes 平均 L2 0.88 m、碰撞率 0.08%;A100 上平均 170 ms,比固定第 15 块(190 ms)低约 10%,比全深度(320 ms)低 47%。
- 🇬🇧 **Problem:** Driving WAMs inherit the cost of iterative future-video generation although deployment needs only an ego trajectory. **Method:** A study of denoising timesteps and DiT depth shows planning is insensitive to video noise and strong trajectories decode from intermediate layers, so a Wan2.2-5B multi-exit planner attaches trajectory diffusion heads to selected blocks and exits once a trajectory-quality scorer passes a threshold. **Results:** 90.8 PDMS on NAVSIM (92.6 with a fixed-exit 64-proposal variant), 89.9 EPDMS on NAVSIM v2, 0.88 m L2 and 0.08% collision on nuScenes zero-shot, and 170 ms average latency on an A100 (~10% below fixed block-15 at 190 ms, 47% below full depth at 320 ms).

---

## 空间智能与 SLAM / Spatial Intelligence & SLAM

共 4 条,全部展开。 / 4 items, all expanded.

### 1. [DrawSplat: Atlanta World-Guided Implicit Gaussian SLAM for Indoor Reconstruction](https://arxiv.org/abs/2610.41602) — Fan Zhu, Zhisong Xu 等
🏷️ 交叉方向 / Also: 3D 重建 / 3D Reconstruction
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 **问题:** 室内弱纹理、大平面、深度噪声与长轨迹下,现有 Gaussian SLAM 的光度/深度约束不足,地图出现漂移、表面增厚与法向噪声。**方法:** 先用点线联合跟踪估计位姿、稀疏几何与重力方向,再用 Atlanta World 先验的共享重力分量从跟踪线推断结构平面,转化为对高斯中心与法向的可微正则;结合基于锚点的隐式神经高斯表示与自适应结构采样。**结果:** 多个数据集上跟踪鲁棒、渲染高保真、几何重建强,并在质量、效率与模型大小间取得平衡;摘要未给具体数值。
- 🇬🇧 **Problem:** Indoor weak texture, large planes, noisy depth and long trajectories leave Gaussian SLAM with drift, surface thickness and noisy normals. **Method:** Point-line joint tracking estimates poses, sparse geometry and gravity; Atlanta World's shared gravity component infers structural planes that become differentiable regularizers on Gaussian centers and normals, combined with anchor-based implicit neural Gaussians and adaptive structural sampling. **Results:** Robust tracking, high-fidelity rendering and strong geometry on several datasets with a balance of quality, efficiency and size; no numbers in the abstract.

### 2. [PGGT-Loc: Primitive-Grounded Geometry Transformer for Feed-Forward Camera Localization](https://arxiv.org/abs/2610.41833) — Hanqiao Ye, Yuzhou Liu 等
开源状态 / Code: ✅ 已开源 / Released — Comments 给出 [3dv-casia/PGGT-Loc](https://github.com/3dv-casia/PGGT-Loc)(代码与模型);链接匿名不可访问,待核实。Comments:NeurIPS 2026 接收。
- 🇨🇳 **问题:** 相机定位多为依赖昂贵地图的多阶段流水线,而由平面基元组成的结构化地图常见但尚未被直接用于定位。**方法:** 提出 PGGT:输入单张查询图像和一组平面地图基元,网络预测多个定位目标,实现可泛化到未见环境的前馈 6-DoF 定位。**结果:** 摘要称在稠密表面地图和极简布局模型上均推进最先进定位性能;预印本摘要未给出定量数字。
- 🇬🇧 **Problem:** Camera localization relies on costly multi-stage map pipelines, while compact planar-primitive maps are common but unexplored for direct localization. **Method:** PGGT takes one query image and a set of planar map primitives and predicts multiple localization targets for feed-forward 6-DoF localization that generalizes to unseen environments. **Results:** The abstract claims state-of-the-art localization on both dense surface maps and minimal layout models; no numbers in the abstract.

### 3. [OpenVIO: A Versatile Open-Source Visual-Inertial Odometry System](https://arxiv.org/abs/2610.41671) — Seungwon Choi
开源状态 / Code: ✅ 已开源 / Released — [93won/openvio](https://github.com/93won/openvio)(MIT 许可;ls-remote 验证可访问)。
- 🇨🇳 **内容:** 面向研究与实用的开源 VIO 系统,支持针孔、鱼眼及拼接 360° 图像,文中描述各组成与设计考虑。**结论:** 在公开数据集上与其他开源 VIO 系统做了基准对比;摘要未给出具体数值。
- 🇬🇧 **Content:** An MIT-licensed open-source VIO system supporting pinhole, fisheye and stitched 360° images, with each component and design consideration described. **Conclusion:** Benchmarked against other open-source VIO systems on public datasets; the abstract gives no numbers.

### 4. [Visual-Inertial RGB-D SLAM with Encoders for a Differential Wheeled Robot](https://arxiv.org/abs/2610.41768) — Zhanghao Zhu, Yutaka Kaizu 等(原文发表于 IEEE Sensors Journal 2022,vol. 22, no. 6;本次为作者接收稿上传 / author-accepted manuscript)
开源状态 / Code: ✅ 已开源 / Released(据摘要)— 摘要称源码与含编码器的数据集已公开,但未给链接,未核实。
- 🇨🇳 **问题:** VIO 方法多不开源,且在特征点暂时缺失或快速运动时易失败。**方法:** 提出编码器的生成式测量模型,推导 MAP 估计与所需雅可比,构建紧耦合的视觉-惯性-编码器 RGB-D SLAM。**结果:** 自有数据集上实时状态估计精确稳健,RMSE 约 2–7 cm。
- 🇬🇧 **Problem:** VIO approaches are rarely open source and fail when features are temporarily lacking or motion is fast. **Method:** A generative encoder measurement model with its MAP estimate and Jacobians underpins a tightly coupled visual-inertial-encoder RGB-D SLAM system. **Results:** On an in-house dataset it gives accurate, robust real-time state estimation with RMSE of about 2–7 cm.

---

## 其他值得关注 / Other Notable

- [Mechanistic Interpretability for End-to-End Self-Driving](https://arxiv.org/abs/2610.41185)(CoRL 2026;自动驾驶 SAE 可解释性,路线意图无监督恢复准确率 98.3%,适配器使轨迹选择误差降低 3.44%)。 / SAE-based interpretability of an E2E driving planner (CoRL 2026): route intent recovered at 98.3% accuracy, adapter lowers trajectory selection error 3.44%.
- cs.RO 列表中其余约 44 条(无人机固件、多机器人规划、外骨骼、手术机器人、水下导航、航天器规划等)与关注主题弱相关,未展开。 / The remaining ~44 listing items (UAV firmware, multi-robot planning, exoskeletons, surgical, underwater, spacecraft planning, etc.) are weakly related and not expanded.

## 运动控制错归自查 / Misclassification Self-check

逐条检查优先级 3–7 类别:REA(含 G1 人形与全身控制器,但贡献为运行时编排,已加理由)、I3L(模仿学习 + 采集硬件,已加理由)、Hourglass(导航命令规划,已加理由)、VEGA、OpenFlyV2(空中)、PDRVLA、SV-WAM 等均不以人形/足式 locomotion、全身控制、动作跟踪或 RL 控制策略为主要贡献;π-StepNFT、ResMerge(RL 微调操作策略)已移入「运动控制·RL」。 / Items in categories 3–7 were checked; RL-fine-tuned manipulation policies (π-StepNFT, ResMerge) were moved to Motion Control · RL; borderline items carry a rationale line.

## GitHub 动态 / GitHub Highlights

**Release:** 本窗口无重点项目(LeRobot、openpi、Isaac Lab、MuJoCo、GR00T 等)release(watchlist_releases 为 0)。 / No watchlist releases in window.

**star 增长最明显的相关仓库(相对前一日快照) / Top star growth:**

| 仓库 / Repo | ★ | 增长 / Δ | 说明 / Note |
|---|---|---|---|
| [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) | 438 | +26 | SuperMimic 相关实现/扩展/资源合集(第三方整理,非官方代码)。 / Third-party curated list, not official code. |
| [Motphys/Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) | 231 | +13 | SuperMimic 在 UniLab 上的独立复现(第三方)。 / Independent reproduction (third party). |
| [Ropedia/ropedia-w0](https://github.com/Ropedia/ropedia-w0) | 209 | +12 | Ropedia W0:跨具身的 loco-manipulation 世界模型(未核实对应论文)。 / Cross-embodiment loco-manipulation world models. |
| [tuotuoLyu/FPO](https://github.com/tuotuoLyu/FPO) | 123 | +17 | 面向 π0 等 VLA 的 Flow Policy Optimization 官方代码(ICRA 2026)。 / Official FPO code for RL fine-tuning of flow-matching VLAs. |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28648 | +18 | LeRobot。 / LeRobot. |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 16038 | +17 | MuJoCo。 / MuJoCo. |
| [rsasaki0109/lidar_slam_ros2](https://github.com/rsasaki0109/lidar_slam_ros2) | 924 | +20 | ROS 2 LiDAR SLAM,地图制作与基准。 / ROS 2 LiDAR SLAM mapping and benchmarking. |
| [Junchao-cs/SolarWM](https://github.com/Junchao-cs/SolarWM) | 839 | +15 | 长时程视频世界模型的开放数据与训练。 / Open data and training for long-horizon video world models. |

**新仓库(筛选后,均为小型项目) / Notable new repos (filtered):**
- [BIGAI-General-Vision-Lab/Zero-HLM](https://github.com/BIGAI-General-Vision-Lab/Zero-HLM) — 8★,见「运动控制·RL」第 14 条。 / See Motion Control · RL #14.
- [ProActRobot/ProAct-Official](https://github.com/ProActRobot/ProAct-Official) — 5★,流式动作生成与 agentic 推理(对应论文未核实)。
- [J1dan/MiniWAM-release](https://github.com/J1dan/MiniWAM-release) — 3★,MiniWAM 紧凑未来目标 WAM(是否官方未核实)。
- [ApurvK032/pi-wbc](https://github.com/ApurvK032/pi-wbc) — 0★,Unitree G1 的 PPO 全身控制器(师生训练 + 域随机化,个人项目)。
- [gaetanotorella/H1_2_Squat_Locomotion_RL](https://github.com/gaetanotorella/H1_2_Squat_Locomotion_RL) — 1★,H1_2 下蹲 locomotion RL(个人项目)。
- [REA 官方仓库 InfRec-Cardinal/REA](https://github.com/InfRec-Cardinal/REA) — 2★,见具身智能小节。

## 今日趋势 / Today's Trends

1. **人形全身控制转向"梯度/生成式"路线 / Humanoid whole-body control goes gradient-based and generative.** ∇Mimic 用精确仿真梯度,DiffWBC 用一步扩散控制器,FOCUS 用可微模仿,HIPC 做生成规划 + 跟踪闭环;共同点是降低 PPO 的样本代价或获得可 steer 性。 / [∇Mimic](https://arxiv.org/abs/2610.41654), [DiffWBC](https://arxiv.org/abs/2610.41354), [FOCUS](https://arxiv.org/abs/2610.41540) and [HIPC](https://arxiv.org/abs/2610.41334) all move beyond plain PPO tracking toward cheaper or steerable controllers.
2. **人形鲁棒性与极端环境 / Humanoid robustness in hard settings.** ROOF(头顶障碍跌倒恢复)、月面迁移研究、关节退化 RL 都在检验控制策略在非常规条件下的表现。 / [ROOF](https://arxiv.org/abs/2610.42097), the [lunar transfer study](https://arxiv.org/abs/2610.30080) and [joint-health RL](https://arxiv.org/abs/2610.41348) stress-test policies under unusual conditions.
3. **Agentic harness 与小模型蒸馏 / Agentic harnesses and distillation.** CaPtain、TinyAstral、LEXP、REA、META-Robot 都围绕"harness + 记忆/经验 + 小模型"构建机器人智能体。 / [CaPtain](https://arxiv.org/abs/2610.40799), [TinyAstral](https://arxiv.org/abs/2610.41216), [LEXP](https://arxiv.org/abs/2610.41320) and [REA](https://arxiv.org/abs/2610.42053) build robot agents around harnesses, memory and small models.
4. **评测可信度审计 / Evaluation-integrity audits.** SimuGuard 追到物理引擎常量,WAM 测试时搜索审计发现渲染损坏,MolmoSpaces-CommonSense 表明现有基准高估零样本能力。 / [SimuGuard](https://arxiv.org/abs/2610.41857), the [WAM test-time search audit](https://arxiv.org/abs/2610.41970) and [MolmoSpaces-CommonSense](https://arxiv.org/abs/2610.41377) all question benchmark reliability.
5. **WAM 研究从"能用"走向"拆解原因" / WAMs: from "it works" to "why".** WorldBridge 拆解视频与动作泛化,CausalWAM 做可辨识性理论,Adaptive-WAM/SV-WAM 去掉推理时视频生成。 / [WorldBridge](https://arxiv.org/abs/2610.40748), [CausalWAM](https://arxiv.org/abs/2610.42096) and [SV-WAM](https://arxiv.org/abs/2609.03602) analyze or remove video generation at inference.

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
- `differentiable simulation`(arXiv + GitHub topic)— 中:今日 ∇Mimic、FOCUS 以及已监测的 SuperMimic 都依赖可微仿真/可微模型做人形控制。 / EN: Differentiable simulators are becoming a core tool for humanoid control. 证据 / Evidence: 3 篇/个,代表 [∇Mimic](https://arxiv.org/abs/2610.41654)、[FOCUS](https://arxiv.org/abs/2610.41540)。
- `agent harness` / `code-as-policy`(arXiv + GitHub)— 中:机器人 VLM 智能体的 harness、经验记忆与蒸馏成为反复出现的新设定。 / EN: Harness-centered VLM robot agents recur across papers. 证据 / Evidence: ≥5 篇,代表 [CaPtain](https://arxiv.org/abs/2610.40799)、[TinyAstral](https://arxiv.org/abs/2610.41216)。

**建议观察 / Watch**
- `benchmark audit` / `simulator artifact`(arXiv)— 中:评测可信度类论文开始出现。 / EN: Evaluation-integrity papers are emerging. 证据 / Evidence: 3 篇,代表 [SimuGuard](https://arxiv.org/abs/2610.41857)、[WAM audit](https://arxiv.org/abs/2610.41970)。

**建议移除/收窄 / Remove or Narrow:** 今日无建议 / No suggestions today(注:API 严格窗口过滤下 16 个关键词命中为 0,属数据量少所致,不建议据此移除)。

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 / Added | 当前状态 / Status | 今日检查 / Today | 备注 / Notes |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 / Unknown | signal = false;candidate_repos 为空;project_page_release_claims 与 arxiv_github_links 为空;arXiv 最新版本 v1;errors 为空 | 无变化。search_hits 中为第三方复现/个人项目(如 [Motphys/Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) 231★、[miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) 438★ 合集),不算官方开源。 |

**建议加入监测 / Suggested additions**(均为运动控制·RL,状态为计划开源):

1. ∇Mimic — 中:摘要明确承诺开源 NablaEngine 与 ∇Mimic 但尚无链接,值得盯。 / EN: The abstract promises releasing NablaEngine and ∇Mimic but no link yet.
```json
{"name": "NablaMimic", "title": "∇Mimic: Ultra-Efficient Humanoid Control with Differentiable Simulation", "arxiv_id": "2610.41654", "search_terms": ["NablaMimic", "NablaEngine", "nabla-mimic"], "owners": [], "project_pages": [], "known_repos": []}
```
2. DiffWBC — 中:通用人形动作跟踪 + 测试时 steering,项目页出现 "coming soon"。 / EN: Steerable humanoid tracker whose project page shows "coming soon".
```json
{"name": "DiffWBC", "title": "DiffWBC: Unlocking Steerable General Humanoid Motion Tracking via One-Step Diffusion Whole-Body Control", "arxiv_id": "2610.41354", "search_terms": ["DiffWBC"], "owners": [], "project_pages": ["https://diffwbc.github.io"], "known_repos": []}
```
3. ROOF — 中:人形跌倒恢复,G1 真机验证,有项目页但无代码。 / EN: Humanoid fall recovery with G1 real-robot validation; project page but no code.
```json
{"name": "ROOF", "title": "ROOF: Learning Humanoid Fall Recovery under Overhead Constraints", "arxiv_id": "2610.42097", "search_terms": ["ROOF humanoid fall recovery"], "owners": [], "project_pages": ["https://lu-yidan.github.io/ROOF/"], "known_repos": []}
```

**建议移出 / Suggested removals:** 无 / None.
