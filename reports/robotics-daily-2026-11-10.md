# 机器人/具身智能每日速递 — 2026-11-10 / Robotics & Embodied AI Daily — 2026-11-10

## 检查窗口与来源状态 / Window & Source Status

- **窗口 / Window**:台北时间 2026-11-09 07:40 – 2026-11-10 07:40(UTC 2026-11-08 23:40 – 11-09 23:40)。arXiv 周末不发布,今日可用的最新 cs.RO 列表是 **Mon 9 Nov 2026**(覆盖 11-05 晚至 11-06 的提交,即周五的论文),昨日报告尚未包含。 / The newest cs.RO list is Monday 9 Nov (covers Thursday-evening to Friday submissions), not yet in yesterday's report.
- **arXiv cs.RO 列表 / list**:[cs.RO new](https://arxiv.org/list/cs.RO/new)(Mon 9 Nov)解析 103 条 = New 54 + Cross-lists 6 + Replacements 43,逐条分类完毕。
- **arXiv API 关键词检索 / keyword search**(cs.RO/cs.AI/cs.LG/cs.CV,submittedDate 降序,发布时间 ≥ 2026-11-05T19:00Z,因为 API 中最新的提交是 2026-11-06T18:59Z):embodied 6、vision-language-action 11、VLA 10、vision-language navigation 0、humanoid 4、legged locomotion 0、whole-body control 2、model predictive control 2、reinforcement learning robot 0(短语检索返回结果很少)、sim-to-real 5、dexterous manipulation 1、robot foundation model 1、world model 3、world action model 2、video world model 0、spatial intelligence 0、spatial reasoning 2、SLAM / visual SLAM / LiDAR SLAM / gaussian splatting SLAM 均 0、3D reconstruction 2、motion tracking 1、motion imitation 0;合并去重共 32 篇。API 检索在列表之外新增的相关论文:Dejavu、TT-MBRL、BEV3SR、HiMEM、HomeLoop、ToolDex(其余均已在 cs.RO 列表中)。
- **入选与摘要 / Selected & abstracts**:入选并展开/列名的论文约 75 篇;已用 arXiv API(id_list,https)取回 118 篇的完整摘要(含 cs.RO 列表 103 条 + HF/API 补充 15 条),全部非空;其中 73 篇 Comments 非空(已用于开源判断)。
- **GitHub radar**:`data/latest.json` date_taipei = 2026-11-10(已更新);new_repos 150、star_growth_top 60、watchlist_releases 2、oss_watch 1(signal=false)。
- **Hugging Face Daily Papers**:API 可访问,100 条;其中与机器人相关并带信息的有 SLA、NEO-VLA、DreamFree、Open-HumanWAM、PyRUA-DataFarm/REAL、HeLM、VFlash、DRAP,已并入下文。
- **推送权限 / Push**:`git push --dry-run` 通过;Google Drive 连接器见文末。

---

## 今日必读 / Top Picks

1. **[DKWBC](https://arxiv.org/abs/2611.09605)**(运动控制·RL,✅ 已开源)— 逆动力学前馈 + 残差 RL 平衡策略,把"动作跟踪"与"平衡"解耦,真机验证,代码已发布。 / Inverse-dynamics feedforward plus a residual RL balancing policy decouples tracking from balance; real-robot validated, code released.
2. **[ForPC](https://arxiv.org/abs/2611.08664)**(运动控制·RL,🕒 计划开源)— 两阶段 RL 的人形推车全身控制,无力传感器、纯仿真训练零样本上真机 Unitree G1,可推 30 kg 货物。 / Two-stage RL whole-body cart pushing without force sensors; zero-shot sim-to-real on a G1 pushing up to 30 kg.
3. **[STRIDE](https://arxiv.org/abs/2611.08857)**(运动控制·RL,❓ 未知)— 只用 IMU 的加速度奖励 + off-policy RL,在 G1/T1 上约 14 分钟样本学会走路,训练跌倒减少 81%。 / IMU-only acceleration reward with off-policy RL learns to walk on G1/T1 in ~14 minutes of samples.
4. **[SUGARv2](https://arxiv.org/abs/2611.09266)**(运动控制·RL,🕒 计划开源)— 合成交互参考 + 参考式模仿奖励,统一训练视觉人形 loco-manipulation,仿真平均成功率 91.0% 并上真机。 / Synthesized interaction references plus mimic rewards for visual humanoid loco-manipulation; 91.0% mean sim success and real deployment.
5. **[DreamFree](https://arxiv.org/abs/2611.04527)**(世界模型与 WAM,❓ 未知)— 不生成未来视频,把 14B 视频扩散模型蒸馏成"预测型视觉编码器",11 Hz 实时闭环控制。 / Distills a 14B video diffusion model into a predictive visual encoder, enabling 11 Hz closed-loop control without imagination.

---

## 运动控制·RL / Motion Control · RL(14 条,全部展开 / all expanded)

### [STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards](https://arxiv.org/abs/2611.08857) — 作者:Nico Bohlinger, Jan Peters(机构摘要未给出)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空,摘要无代码链接或承诺。
- 🇨🇳 在真机上直接学习人形行走可以绕开 sim-to-real 差距,但常规 locomotion 奖励要跟踪基座速度,而这在机载条件下需要动捕或高精度状态估计器。STRIDE 改为奖励机器人跟随指令加速度曲线,只需板载 IMU;为提高样本效率,采用 off-policy RL 算法 XQC,并结合高增益关节位置控制器与左右对称数据增强。仿真中在 Unitree G1 与 Booster T1 上约 14 分钟样本即学会行走;相比不使用这两个组件,训练期间跌倒减少 81%,而不使用时需要超过一小时才能学会。预印本摘要未给出真机结果。
- 🇬🇧 Learning humanoid locomotion directly on hardware avoids the sim-to-real gap, but typical velocity-tracking rewards need base velocity that is unavailable onboard without mocap or a calibrated estimator. STRIDE instead rewards following a commanded acceleration profile using only the onboard IMU, and pairs the off-policy RL algorithm XQC with high-gain joint position controllers and left-right symmetry augmentation. In simulation it learns to walk on the Unitree G1 and Booster T1 within 14 minutes of samples, and cuts training falls by 81% compared with learning without those two components, which needs over an hour. The abstract reports no real-robot numbers.

### [ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing](https://arxiv.org/abs/2611.08664) — 作者:ZhenYu Zou, Xing Liu, ShiChuang Wang, YunLong Dong 等
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://roboforpc.github.io/)显示 "Code Coming soon",无仓库链接。
- 🇨🇳 人形推购物车时双手抓握形成力耦合闭环,接触力既推动车辆又扰动平衡,载荷变化还会改变耦合动力学。ForPC 采用两阶段 RL:先在不同手部负载与上身姿态下训练 locomotion 先验提供平衡支撑,再由机载观测推断力隐变量和状态隐变量(无需外部力传感器),输入残差策略来协调手臂、腰部、腿部的有界调整与基座速度指令;多目标奖励惩罚双手内力对抗、抓握打滑与执行器饱和,无需人类示范。Sim-to-sim 实验中,相对仅 locomotion 基线,车速 RMSE 最多降低 68.2%,多弯路线横向误差最多降低 74.2%;仅在仿真中训练的策略零微调迁移到真机 Unitree G1,无需针对载荷调整即可以 0.5 m/s 推动最重 30 kg 的货物。
- 🇬🇧 In humanoid cart pushing the bimanual grasp closes a force-coupled loop where contact wrenches both drive the cart and disturb balance, and payload changes alter the dynamics. ForPC uses two-stage RL: a locomotion prior trained under varied hand loads and upper-body postures, then force and state latents inferred from onboard observations (no force sensors) feed a residual policy that coordinates bounded arm, waist and leg adjustments with base-velocity commands; rewards penalize bimanual internal opposition, grasp slip and actuator saturation, with no demonstrations. In sim-to-sim tests it cuts cart-velocity RMSE by up to 68.2% and cross-track RMSE by up to 74.2% versus a locomotion-only baseline. The policy, trained only in simulation, transfers to a real Unitree G1 without fine-tuning and pushes carts carrying up to 30 kg at 0.5 m/s.

### [DKWBC: Decoupling Motion Tracking and Balancing for Humanoid Whole-Body Control](https://arxiv.org/abs/2611.09605) — 作者:Dingkun Wei, Zehong Shen, Huaijin Pi, Xueyang Wang 等
🏷️ 交叉方向 / Also: 运动控制·传统(逆动力学 + PD)/ Classical (归入 RL 类,因含 RL 残差策略)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/robbyant-research/DKWBC);项目页头部链接,匿名 `git ls-remote` 验证存在,发布内容(权重/训练代码)未逐项核对。
- 🇨🇳 现有基于 RL 的人形动作跟踪器让同一策略同时学习跟踪控制和平衡修正,相近的参考姿态可能对应完全不同的动力学需求,导致学习困难且控制输出高频抖动。DKWBC 用显式的模型驱动跟踪(逆动力学前馈 + 关节 PD 反馈)提供跟踪力矩,再由残差策略只学习用于平衡执行的额外关节力矩修正,依据是浮动基动力学中模型项与环境接触力项对关节力矩的分解。仿真与真机实验表明,单个平衡策略可泛化到不同动作数据集,并在地面支撑、附加负载、物理交互条件下保持跟踪精度与平衡;预印本摘要未给出具体数值。
- 🇬🇧 RL-based humanoid trackers usually learn tracking and balance jointly, yet similar reference poses can need very different dynamics, which complicates learning and produces high-frequency control fluctuations. DKWBC supplies tracking torques explicitly via inverse-dynamics feedforward plus joint PD feedback, and a residual policy learns only the extra joint-torque corrections needed for balanced execution, motivated by the model-based and environmental-wrench terms of floating-base dynamics. In simulation and on hardware, one learned balancing policy generalizes across motion datasets while keeping accurate tracking and balance under ground support, attached payloads and physical interaction. The abstract gives no quantitative numbers.

### [SUGARv2: Learning Diverse Visual Humanoid Loco-Manipulation Skills from Synthesized Interaction References](https://arxiv.org/abs/2611.09266) — 作者:Tianshu Wu, Tianxiang Gui, Yue Chen, Tingxu Liu 等
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://tianshuwu.github.io/sugarv2-humanoid/)显示 "Code (Coming Soon)",无仓库链接。
- 🇨🇳 视觉人形 loco-manipulation 技能随任务和空间配置增多,示范采集与任务专属训练设计的人力成本迅速上升。SUGARv2 通过适配可复用任务模板到不同空间配置,合成协调的机器人-物体运动作为低成本参考,并以基于参考的模仿作为跨任务统一学习目标:先训练特权教师执行参考,再用教师蒸馏加使用相同模仿奖励的 RL 训练视觉策略,配合多样物体实例与视觉域随机化实现 sim-to-real。五个人形 loco-manipulation 任务在仿真中平均成功率 91.0%,并在真机人形上验证了全身操作的 sim-to-real 迁移。
- 🇬🇧 Scaling visual humanoid loco-manipulation is limited by demonstration collection and per-task training design. SUGARv2 synthesizes coordinated robot-object motions by adapting reusable task templates to different spatial configurations, uses reference-based imitation as a common objective, trains privileged teachers on the references, then trains visual policies via teacher distillation and RL with the same mimic rewards, using diverse objects and visual domain randomization. Across five humanoid loco-manipulation tasks it reaches a 91.0% mean success rate in simulation, and a real humanoid shows successful sim-to-real transfer for whole-body manipulation.

### [Q-OIL: Optimistic Exploration in Learning from Human Interventions](https://arxiv.org/abs/2611.08576) — 作者:Pranav Teegavarapu, Sriyash Poddar, Rico Qi, Cleah Winston 等
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI(人在回路机器人学习,含对预训练 VLA 的改进)
开源状态 / Code: 🕒 计划开源 / Planned — [项目页](https://weirdlabuw.github.io/qoil)显示 "Code (coming soon)",无仓库链接。
- 🇨🇳 现有人在回路机器人学习研究大多用仿真的人类模型,其假设与真实人类干预行为不符。作者分析真人干预数据,发现人类倾向在智能体进展停滞时介入,且纠正动作常常次优,据此提出基于进展的干预模型,与真人用户的算法排序有更高的秩相关,可用于仿真中的真实基准测试。在此基础上提出 Q-OIL:在 RL 中对干预转移加乐观奖励,软引导探索靠近人类纠正,并发现分离的 critic 对稳定性至关重要(避免奖励回传到干预前状态)。结果是 Q-OIL 比竞争基线学习更高效,在仿真和真机上成功率高 10–50%,并在两个双臂操作任务上改进了预训练 VLA。
- 🇬🇧 Human-in-the-loop robot learning is mostly studied with simulated humans whose assumptions do not match real intervention behavior. Analyzing real intervention data, the authors find humans intervene when progress stalls and their corrections are often suboptimal, and build a progress-based intervention model that better correlates with real-user algorithm rankings. Q-OIL adds optimistic bonuses to intervention transitions in RL to softly guide exploration toward human corrections, with decoupled critics needed to stop bonuses backing up to pre-intervention states. It learns more efficiently than competitive baselines with 10–50% higher success in simulation and on real robots, and improves pretrained VLAs on two bimanual manipulation tasks.

### [FASTFUNNELS: Agile Multi Robot Navigation in Narrow Spaces via Adaptive Dynamic Funnels](https://arxiv.org/abs/2611.09005) — 作者:Vignesh Rajagopal, Rohan Chandra
🏷️ 交叉方向 / Also: 运动控制·传统(分布式 MPC)— RL + MPC 混合,按规则归入 RL
开源状态 / Code: ❓ 未知 / Unknown — Comments 无代码信息。
- 🇨🇳 多机器人(Ackermann 车型)在狭窄空间高速导航需要在安全与敏捷之间权衡,现有编队控制依赖刚性预定义形状,高速下难以维持。FastFunnels 采用分层结构:高层 RL 策略生成可实时变形的椭圆形"水滴"区域,在障碍与窄缝间挤压、拉伸、转向;低层用分布式 MPC(DMPC)让各机器人留在该区域内并相互避碰。在仿真 F1TENTH 赛车、14 个场景、1–6 台机器人、每场景 20 次试验中,完成率 89%、速度 7.73 m/s,而所有基线要么无法完成赛道,要么只在很低速度(0.07–1.79 m/s,完成率约 40%)下成功。
- 🇬🇧 High-speed multi-robot navigation in tight spaces must balance safety and agility, but formation control relies on rigid predefined shapes that are impractical at speed. FastFunnels is hierarchical: an RL policy outputs a dynamic blob-like elliptical patch that morphs in real time around obstacles and gaps, and a distributed MPC (DMPC) keeps each robot inside the patch while avoiding collisions. On simulated F1TENTH cars over 14 scenarios with 1–6 robots (20 trials each) it achieves an 89% completion rate at 7.73 m/s, while all baselines either fail to finish or succeed only at 0.07–1.79 m/s with about 40% completion.

### [Think Fast, Plan Selectively: Adaptive Deliberation for Efficient Data-Driven MPC (Fast-TD-MPC)](https://arxiv.org/abs/2609.32591) — 作者:Yi Xian Goh, Sze Jue Yang, Hao Luan 等(replacement,2026-11-06 更新)
🏷️ 交叉方向 / Also: 运动控制·传统(MPC)/ 世界模型(学习的世界模型规划)
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 数据驱动 MPC 用学习的世界模型加在线轨迹优化,但每步要采样评估数百条候选轨迹,限制了实际控制频率。受 System 1/2 双过程理论启发,Fast-TD-MPC 自适应地在"快速策略执行"与"测试时规划"之间路由,把昂贵的规划留给最需要的状态。在 103 个连续控制任务上取得有竞争力的性能,推理最多约快 4 倍;在外部扰动下会选择性回退到规划,鲁棒性与原规划器相当。该版本为 v 更新,具体更新内容未逐版比对。
- 🇬🇧 Data-driven MPC pairs a learned world model with online trajectory optimization, but sampling hundreds of candidates per step limits control frequency. Inspired by dual-process theory, Fast-TD-MPC adaptively routes between fast policy execution and test-time planning, reserving deliberation for states that need it. It stays competitive across 103 continuous control tasks with up to ~4x faster inference, and under external disturbances it falls back to planning, keeping robustness comparable to the original planner. This is an updated version; the diff against earlier versions was not checked.

### [It Takes Two to Tangram: Multi-Agent Object Centric Reinforcement Learning for Assembly](https://arxiv.org/abs/2611.08814) — 作者:Paul Knaußt, Kay Pompetzki, Nico Bohlinger, Niklas Funk 等
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://tangrambench.org/)的 Code 链接是占位 "#",无仓库,也无发布承诺。
- 🇨🇳 几何装配要求精细的时空协调,以免在紧间隙下发生碰撞或死锁。该工作提出以物体为中心的 RL 框架:把每个零件视作智能体并学习共享策略;图神经网络表示零件、目标位姿及空间关系并预测每个零件的平移与角速度,采用逐智能体 PPO 加中心化图 critic。以平面七巧板(Tangram)为研究载体,通过程序化生成目标配置与随机初始布局进行训练评估,并与基于采样的规划比较。仿真中展示了并发装配,并因对象中心形式把装配协调与底层物理控制解耦,策略可迁移到真机做顺序执行;摘要未给出具体成功率。
- 🇬🇧 Geometric assembly needs fine spatiotemporal coordination to avoid collisions and deadlocks under tight clearances. The paper treats each part as an agent with a shared policy: a graph neural network encodes pieces, target poses and relations and predicts per-part translational and angular velocities, trained with per-agent PPO and a centralized graph critic. Studied on planar Tangram with procedurally generated targets and random initial arrangements, it isolates the roles of relational structure and multi-agent optimization and compares against sampling-based planning. It shows concurrent assembly in simulation and transfers to sequential execution on a real robot because the object-centric formulation decouples coordination from low-level control; the abstract gives no success rates.

### [Grasp-TAGS: Task-Aware Grasp Selection via Critic Distillation for Prehensile Loco-Manipulation](https://arxiv.org/abs/2611.09864) — 作者:Xun Tu, Minghao Zou, Karthik Desingh
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://rpm-lab-umn.github.io/Grasp-TAGS-web-page/),摘要与 Comments 无代码链接。
- 🇨🇳 移动操作机器人进行大物体重排时,不同的几何稳定抓取会导致后续操作表现差异巨大,而现有方法要么依赖精确动力学模型,要么假设固定初始抓取。Grasp-TAGS 训练一个跨多种初始抓取配置的统一 PPO 策略,并把学到的 critic 蒸馏成一个轻量抓取效用网络,仅用候选抓取配置与目标信息给候选排序,在接触前就选出下游效用最高的抓取。平均成功率达 89.84%,最佳单一抓取策略为 79.87%,提升 9.97 个百分点,并降低了所有评估物体的最终朝向误差。
- 🇬🇧 In large-object rearrangement by mobile manipulators, different geometrically stable grasps lead to very different downstream performance, yet prior work either needs accurate dynamics models or assumes a fixed initial grasp. Grasp-TAGS trains one PPO policy across multiple initial grasp configurations and distills its critic into a lightweight grasp-utility network that ranks candidates using only the grasp configuration and goal, choosing before contact. It reaches an average success rate of 89.84% versus 79.87% for the best single-grasp policies (+9.97 points) and reduces final orientation errors on all evaluated objects.

### [Revisiting Temporal Regularization for Smooth Control in Deep Reinforcement Learning (CATS)](https://arxiv.org/abs/2610.07910) — 作者:SungJae Ahn, Jeong Woon Lee, Kyoleen Kwak, Hyoseok Hwang(replacement,2026-11-06 更新)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/dmach1ne/CATS);[项目页](https://dmach1ne.github.io/CATS/)链接,匿名 `git ls-remote` 验证存在。
- 🇨🇳 深度 RL 策略常产生非平滑的动作振荡,阻碍真机部署;已有的空间平滑方法(惩罚对状态变化的敏感度)广泛约束会降低任务性能,而时间正则一直被认为在观测噪声下无法提供空间平滑。作者证明时间惩罚能约束共享同一后继状态的当前状态之间的动作差异,从而带来空间平滑的效果,并据此提出 CATS:时间平滑惩罚 + 线性渐增权重(先学奖励行为再逐步平滑)。仿真与真机实验表明 CATS 显著降低动作振荡且不损害任务性能,计算开销很小;摘要未给出具体数值。已投稿 ICRA 2027。
- 🇬🇧 Deep RL policies often produce non-smooth action oscillations that hinder deployment on robots; spatial smoothing penalties degrade task performance and temporal regularization was thought unable to give spatial smoothness under observation noise. The authors prove the temporal penalty bounds action differences between current states sharing a next state, yielding a spatial effect, and propose CATS: a temporal-smoothness penalty with linear ramp-up so the policy learns rewarding behavior before smoothing. Simulation and real-world experiments show substantially reduced action oscillation without hurting task performance, with little overhead; no numbers are given in the abstract. Submitted to ICRA 2027.

### [VLD: Visual Learned Distance as an Interface for Reinforcement Learning Navigation](https://arxiv.org/abs/2512.07976) — 作者:Lazar Milikic, Manthan Patel, Jonas Frey(replacement,2026-11-06 更新)
🏷️ 交叉方向 / Also: VLN / 导航(图像目标导航)、空间智能
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空(仅有 CoRL 2026 SISREN 研讨会出处)。
- 🇨🇳 端到端从图像预测导航动作难以训练,既受 sim-to-real 差距影响,也缺少带动作标注的数据。VLD 将感知学习与策略学习解耦:先在约 3000 小时互联网规模与仿真视频上训练自监督的"到目标距离"预测器;RL 策略则在仿真中用带 GeoNoise(复现距离预测器视角/重叠相关误差的学习噪声模型)扰动的特权几何距离训练,部署时零样本直接使用 VLD 预测。使用 VLD 输入时,GeoNoise 训练的策略在 HM3D 成功率 58.7%、Gibson 76.2%,而通用时间相关噪声训练的策略仅 4.9% 与 11.5%;真机上成功率 88%,强端到端图像目标基线为 60%。
- 🇬🇧 End-to-end image-to-action navigation policies suffer from the sim-to-real gap and scarce action-labeled data. VLD decouples perception from policy: a self-supervised distance-to-goal predictor is trained on ~3,000 hours of internet and simulated video, while the RL policy is trained in simulation on privileged distances perturbed by GeoNoise, a learned noise model reproducing the predictor's viewpoint- and overlap-dependent errors, then consumes VLD zero-shot at deployment. With VLD inputs, GeoNoise-trained policies reach 58.7% on HM3D and 76.2% on Gibson versus 4.9% and 11.5% for policies trained with generic correlated noise. On a physical robot it succeeds in 88% of trials versus 60% for a strong end-to-end image-goal baseline.

### [Probably Safe Sim-to-Real Transfer with Lifetime Validity (Dejavu)](https://arxiv.org/abs/2611.09344) — 作者:Rohan Tangri, Jan-Peter Calliess
开源状态 / Code: ❓ 未知 / Unknown — 摘要无链接,未取得 Comments。
- 🇨🇳 在约束马尔可夫决策过程中,把仿真训练的 RL 策略迁移到真实环境时,如何在不断更新策略的整个生命周期内保证安全是难题。Dejavu 使用逐决策重要性采样与投注置信序列构成的"随时有效"检验,仅利用生产环境中安全基线策略采集的轨迹,在部署前认证每个仿真训练出的候选策略;可求和的单次检验失败概率给出整个生命周期有效的安全保证。仿真质量不影响安全保证,只影响生产环境中的样本效率;摘要称三个 sim-to-real 基准上的实验支持理论,未给出具体数字。
- 🇬🇧 Safely transferring simulation-trained RL policies in constrained MDPs over an unbounded sequence of policy updates is hard. Dejavu uses an anytime-valid test built on per-decision importance sampling and a betting confidence sequence to certify each simulation-trained candidate before deployment, using only trajectories from a safe baseline policy in production; a summable per-test failure probability gives lifetime validity. Simulation quality affects only production sample efficiency, not the safety guarantee. The abstract says experiments on three sim-to-real benchmarks support the theory but gives no figures.

### [Autonomous Particle Image Velocimetry Using Zero-Shot Sim-to-Real Reinforcement Learning](https://arxiv.org/abs/2611.09679) — 作者:Chang Rajani, Luke Sebastien Marsden, Stephan Kunz, Claudio Mucignat
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅 "9 pages"。
- 🇨🇳 粒子图像测速(PIV)的重建质量受限于采集位姿,通常由操作者事先固定。作者把相机摆位建模为序贯决策问题,训练 RL 智能体控制带相机的 6 自由度机械臂,仅通过时间间隔图像对估计的速度场及其不确定性来观察场景,在水洞中定位、取景并解析水翼尾流。策略完全在水洞的逼真仿真(尾流来自不同翼型/位置/攻角的 CFD)中训练,零样本迁移到真实水洞后能可靠定位随机放置水翼的尾流;相比固定相机视角分辨率更高、流动统计误差更低,用时约为全扫描的一半,图像对数也少得多。
- 🇬🇧 PIV quality is bounded by acquisition position, normally fixed by the operator. The authors cast camera placement as sequential decision making and train an RL agent to command the pose of a camera on a 6-DoF manipulator, observing only velocity fields and uncertainty from time-separated image pairs to locate, frame and resolve a hydrofoil wake in a water tunnel. Trained entirely in a photorealistic simulation with CFD-generated wakes, the policy transfers zero-shot to the real tunnel, reliably framing wakes of randomly placed hydrofoils, resolving them at higher resolution with lower flow-statistics error than a fixed view, in roughly half the time of a full scan and with far fewer image pairs.

### [Ordered Policy Optimization](https://arxiv.org/abs/2611.08936) — 作者:Dongkyu Derek Cho, Pan Xu(Cross-list)
🏷️ 交叉方向 / Also: 通用 RL 算法 / General RL(归入此类因评估于 MuJoCo 连续控制)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅注明 NeurIPS 2026 论文,无代码信息。
- 🇨🇳 PPO 对所有样本使用固定裁剪范围,无法区分统计上有害的极端重要性比与可容忍的大变化。OPO 在每个 minibatch 内对重要性比排序,挑出对更新影响最大的极端比,按预设的"尾部剖面"给它们分配自适应的逐样本裁剪半径,目标仍是一阶的,仅需 minibatch 排序和修改后的策略损失。在 MuJoCo 与 Atari 基准上相对已有基线表现强劲;摘要未给出具体提升幅度,也没有真机实验。
- 🇬🇧 PPO uses one fixed clipping range for all samples and cannot tell statistically harmful extreme importance ratios from tolerable large changes. OPO sorts importance ratios within each minibatch, selects the extreme ones with the largest effect, and assigns them adaptive per-sample radii derived from a prescribed tail profile; the objective stays first-order and needs only minibatch sorting and a modified policy loss. It achieves strong performance versus established baselines on MuJoCo and Atari; the abstract gives no figures and no robot experiments.

**另见 / See also:** [CS-Pi](https://arxiv.org/abs/2611.08654)、[Horizon-Coupled Obstacle Guidance](https://arxiv.org/abs/2611.09340)(扩散/流匹配操作策略的推理期约束,为模仿学习而非 RL,已归入「具身智能」)。

---

## 运动控制·传统 / Motion Control · Classical(8 条,全部展开 / all expanded)

### [Autonomous Whole-body Loco-manipulation Using a Snake Robot](https://arxiv.org/abs/2611.09777) — 作者:Adarsh Salagame, Henry Noyes, Haroon Hublikar, Alireza Ramezani(IROS 2026)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅注明 IROS 2026。
- 🇨🇳 蛇形机器人的整个身体既是推进机构又是操作工具,全身 loco-manipulation 很难,以往工作多通过专用附肢、分段或夹爪把两种功能分开。作者在 COBRA 蛇形机器人上实现无此区分、身体任意部位都可接触的闭环 loco-manipulation:建立基于 Moreau-Jean 时间步进的接触隐式动力学模型(统一机器人-地面、机器人-物体、物体-地面相互作用),并在全阶动力学上做轨迹优化,以几何规划器与名义比例控制器引导,在侧向蜿蜒(sidewinding)过程中自主把物体推到目标位置。规划器与控制器在不同配置的硬件上验证,并给出简化轨迹优化的仿真结果;摘要无量化指标。
- 🇬🇧 For a snake robot the whole body is both propulsor and manipulator, and prior work separates the functions through appendages, segmentation or grippers. On the COBRA snake robot the authors do closed-loop loco-manipulation where any body part may make contact, using a contact-implicit dynamic model within a Moreau-Jean time-stepping framework (robot-ground, robot-object, object-ground) and a trajectory optimization over the full-order dynamics guided by a geometric planner and nominal proportional controller to push an object to a goal during sidewinding. The planner and controller are validated on hardware across configurations, with simulation results for a simplified trajectory optimization; no quantitative metrics are given.

### [Goodhart in the Planner: Sampling-Based Control Exploits Rewards Learned from Human Preferences](https://arxiv.org/abs/2611.09670) — 作者:Soovadeep Bakshi, Apurba Bose
开源状态 / Code: 🕒 计划开源 / Planned — Comments:"Code and results will be released"。
- 🇨🇳 机器人常用从人类偏好学习的奖励模型做 MPC 或 best-of-N 搜索,作者量化其对真实目标的影响。在 HalfCheetah、Hopper(众包标签)和 Meta-World drawer-open、plate-slide(合成标签与作者盲标)上,更强的 MPPI 搜索使真实回报最多下降 76%:使用人类标签时抽屉在 20 次中 0 次打开,而作为起点的克隆策略为 10/10,尽管保留集标签准确率为 0.75–0.97。理论上证明 χ²-正则化 MPPI 在由评分器误差范围设定的温度下是最坏情形最优的;用 100 对由真实回报排序的提案校准后,该规则在每次运行中都成功,在 plate-slide 和 drawer-open 上保留克隆策略平均 86–94% 的回报,但在搜索本该有益的任务上偏保守。
- 🇬🇧 Robots often search (MPC or best-of-N) against reward models learned from human preferences; the paper measures the effect on the true objective. On HalfCheetah and Hopper with crowd labels and Meta-World drawer-open and plate-slide with synthetic and blind author labels, harder MPPI search cuts true return by up to 76%: with human labels the drawer opens in 0 of 20 runs versus 10 of 10 for the cloned starting policy, while held-out label accuracy stays 0.75–0.97. The authors prove χ²-regularized MPPI at a temperature set by the scorer's error spread is worst-case optimal; calibrated from 100 oracle-ranked proposal pairs it succeeds in every run and keeps on average 86–94% of the cloned policy's return on plate-slide and drawer-open, though it is cautious where search helps.

### [LACART: Lookahead-Augmented Collision Avoidance and Reference Tracking Strategies for Safety-Critical Robots](https://arxiv.org/abs/2611.09640) — 作者:Pedro Lopes, Amit Shivam, Luis Tiago Paiva
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 自主赛车对碰撞避免的几何与算力约束要求很高。LACART 把前瞻型控制障碍函数(CBF)、松弛控制李雅普诺夫函数(CLF)与二次规划(QP)结合,修改名义车辆指令以避障并跟踪参考,圆形障碍与赛道边界在同一个优化层处理。仿真中与 Huang 等的方法相比路径相似,计算更快:中位每步 0.31 ms 对 0.33 ms,每次 QP 求解 0.023 ms 对 0.025 ms;学位论文还演示了 1:43 比例车,基于相机估计和无线驱动,控制频率约 25 Hz。作者说明了前瞻点间隙与车体间隙的关系条件及硬件限制。
- 🇬🇧 Autonomous racing is demanding for collision avoidance under tight geometric and computational limits. LACART combines lookahead control barrier functions, a relaxed control Lyapunov function and QP to modify nominal commands for obstacle avoidance and reference tracking, handling circular obstacles and track boundaries in one optimization layer. In simulation versus Huang et al. it yields similar full-track paths with lower median compute: 0.31 vs 0.33 ms per step and 0.023 vs 0.025 ms per QP solve. The accompanying dissertation demonstrates a 1:43-scale vehicle with camera-based estimation and wireless actuation at a reported 25 Hz, and the paper identifies conditions linking lookahead clearance to body clearance and notes hardware limitations.

### [Diffusion-Steering-Based MPC with a JEPA World Action Model (LeWAM)](https://arxiv.org/abs/2610.12407) — 作者:Shashank Hegde, Alexander Popov, Elie Aljalbout, Nikolai Smolyanskiy(replacement,2026-11-05 更新)
🏷️ 交叉方向 / Also: 世界模型与 WAM / World Models & WAM(核心贡献含 MPC 规划方式,故归入控制类)
开源状态 / Code: ❓ 未知 / Unknown — Comments 无代码信息。
- 🇨🇳 世界-动作模型(WAM)通常基于重建式表征,带有噪声和冗余信息,影响下游预测。LeWAM 是一个双向 Transformer,在无解码器的 JEPA 隐空间中端到端训练前向、后向、逆动力学和策略预测四种模式。线性探针能从其隐空间读出机器人与物体状态,优于前向 JEPA 世界模型 LeWM,同时和 LeWM 一样忽略视觉干扰物,远好于重建式 WAM;闭环评估中与同等规模的 flow-matching 策略相当,并额外提供世界模型。规划时如果直接采样原始动作,MPC 会利用动力学模型误差;改为在策略头的噪声空间做规划,可提高 WAM 的闭环性能。摘要未给出具体数字。
- 🇬🇧 World action models typically use reconstruction-based representations carrying noisy, redundant information. LeWAM is a bidirectional transformer for forward, backward, inverse dynamics and policy prediction on a decoder-free JEPA latent trained end-to-end across all four modes. Linear probes read robot and object state better than from the forward-only JEPA world model LeWM, the latent ignores visual distractors as LeWM does and far better than a reconstruction-based WAM, and closed-loop performance matches a flow-matching policy of matched size while also providing a world model. Sampling raw actions during planning lets MPC exploit model inaccuracies, whereas planning in the policy head's noise space improves closed-loop performance; no numbers are given in the abstract.

### [Closed-Loop Object-Informed Control for Non-Prehensile Robot Manipulation (CLOI)](https://arxiv.org/abs/2605.30778) — 作者:Nikola Raicevic, Hyomuk Kim, Shahid Mulla, Hyungjun Doh 等(replacement,2026-11-05 更新)
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 非抓取操作的接触不连续、长时域,采样式 MPC 在长时域下难找到好轨迹。CLOI 把问题拆为物体级规划(寻找把物体送到目标的长时域物体位姿)和机器人级规划(选择跟随这些位姿的机器人动作),二者都用 MPPI 求解,并通过 ADMM 在物体位姿上达成共识:物体计划朝机器人可实现的轨迹修正,机器人计划对齐任务所需的物体位姿。在 xArm6 带障碍的平面推动任务上,相同算力预算下相对标准 MPPI,仿真成功率提高 35%,真机提高 43%。
- 🇬🇧 Non-prehensile manipulation involves discontinuous, long-horizon contacts, and sampling-based MPC struggles to find good long-horizon trajectories. CLOI splits the problem into object-level planning (long-horizon object poses leading to the goal) and robot-level planning (actions following those poses), solves both with MPPI and couples them by ADMM consensus on object poses, so the object plan is revised toward robot-realizable trajectories and the robot plan aligned with required object poses. On planar pushing with obstacles using an xArm6 it raises success by 35% in simulation and 43% on hardware over standard MPPI at the same compute budget.

### [CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation](https://arxiv.org/abs/2609.23614) — 作者:Jongmin Kim, Junsu Ha, Che-Sang Park, Minchang Song 等(replacement,2026-11-06 更新;CoRL 2026)
🏷️ 交叉方向 / Also: VLA(输出刚度 + 阻抗控制,控制贡献为主,归入控制类)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅注明 CoRL 2026。
- 🇨🇳 接触密集操作要求机器人不仅调节运动,还要调节如何顺应外力,而现有 VLA 只输出纯运动学指令,真实接触任务表现下降。CompVLA 在常规 VLA 上加入专门的 Compliance Expert,由 RGB 与语言联合预测运动和刚度矩阵,输出随时间变化的刚度与虚拟位移曲线并通过几何阻抗控制执行。在多种接触密集任务上取得最高平均成功率,优于普通 VLA 与具备顺应性的 VLA 基线,消融证明每个组件都必要;摘要未给出具体数字。
- 🇬🇧 Contact-rich manipulation requires regulating not just motion but how the robot yields to external forces, yet existing VLAs output purely kinematic commands and degrade on real contact-rich tasks. CompVLA adds a Compliance Expert that, from RGB and language, jointly predicts motion and a stiffness matrix, outputting time-varying stiffness and virtual-displacement profiles executed through geometric impedance control. It achieves the highest average success rate across diverse contact-rich tasks, beating vanilla and compliance-aware VLA baselines, with ablations confirming each component; the abstract gives no figures.

### [FATHOM: World-Model-Guided Diffusion Action-Trajectory Selection for Sparse-Marker AUV Tracking](https://arxiv.org/abs/2611.08898) — 作者:Xiaorui Wang, Zeyu Sha, Mingyang Yang, David Chen Wang
🏷️ 交叉方向 / Also: 世界模型 / World Model、扩散模型(AUV 跟踪控制为任务,故归入控制类)
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 水下协同 AUV 相对跟踪受非线性动力学与水下视觉退化影响,主动光标记提供的观测稀疏,在遮挡、反光、检测噪声下易不完整。FATHOM 先用多模态、任务监督的循环状态空间模型(RSSM)把结构化标记观测、惯性测量、动作历史融合成预测性跟踪信念,再由扩散动作先验生成多条类专家的多推进器轨迹,通过学习到的隐动力学预测其未来跟踪后果,并按显式滚动时域目标选出最优候选,持续用机载观测更新决策。实机 AUV 实验(含基于位姿的强基线对比与组件消融)显示在部分标记可见的常规与挑战性运动下都能鲁棒自主跟踪,且无需动捕反馈即可实时机载运行;摘要未给出具体数值。
- 🇬🇧 Relative tracking of cooperative AUVs is hard under nonlinear dynamics and degraded underwater vision, and active light markers give sparse observations that occlusion, reflection and detection noise can corrupt. FATHOM fuses structured marker observations, inertial data and action history into a predictive tracking belief via a multimodal task-supervised recurrent state-space model, generates multiple expert-like multi-thruster trajectories with a diffusion action prior, predicts their consequences through the learned latent dynamics, and selects the best under an explicit receding-horizon objective, updating continually from onboard observations. Real-AUV experiments with pose-based baselines and ablations show robust tracking in nominal and challenging motions with partial marker visibility, running in real time onboard without motion capture; no numbers are given in the abstract.

### [Task-Driven Closed-Loop Design Optimization of Passively Morphing Quadrotors for Contact-Mediated Narrow Gap Traversal](https://arxiv.org/abs/2611.09272) — 作者:Etor Arza, Luca Girardi, Gabriel Maquignaz, Javier Paez 等
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/ntnu-arl/soft-quadrotor-optimization);Comments 给出,匿名 `git ls-remote` 验证存在。
- 🇨🇳 现有被动变形无人机多为人工设计,难以平衡折叠比、飞行效率和控制跟踪性能。该工作提出闭环设计方法,以接触式窄缝穿越仿真中的任务成功率为反馈,联合优化四旋翼几何与两条被动折叠臂的扭矩-偏转响应。得到的样机可把宽度从 31.3 cm 被动缩到 14.1 cm,以 2 m/s 参考速度穿过 15 cm 宽缝隙,可容忍最高 30° 进入角误差并穿过 40 cm 长受限通道;相对刚性孪生机,无接触飞行时位置 RMSE 仅增加 2 mm、电功率增加不到 1%。
- 🇬🇧 Passively morphing drones are usually human-designed and struggle to balance folding ratio, flight efficiency and tracking performance. This closed-loop design method jointly optimizes quadrotor geometry and the torque-deflection response of two passive folding arms, using task success rate in a contact-based gap-traversal simulation as feedback. The prototype passively shrinks from 31.3 to 14.1 cm, traverses a 15 cm opening at 2 m/s, tolerates approach-angle errors up to 30° and folds through a 40 cm passage; versus a rigid twin it adds only 2 mm position RMSE and under 1% electrical power in contact-free flight.

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models(展开 12 条 / 12 expanded)

### [Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation](https://arxiv.org/abs/2611.08577) — Meituan Robotics Team
🏷️ 交叉方向 / Also: VLA
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/Meituan-Robotics/Meituan-Robotics-0);Comments 给出,匿名 `git ls-remote` 验证存在;[项目页](https://meituan-robotics.github.io/Meituan-Robotics-0/)。
- 🇨🇳 面向固定底座桌面操作的 VLA 基础模型与具身智能体系统。MR0 使用 1.47 亿视觉-语言样本和覆盖 12 种本体的 15,060 小时机器人轨迹,三阶段训练:离散动作 token 预训练 → flow-matching 中期训练迁移到连续跨本体控制 → 真机后训练;提出 Rollback(把被替换的策略片段与人类纠正配对提供正负监督,用于 CFG-DAgger),统一末端接口与异步动作块合并,以及事件驱动的智能体。MR0 在 RoboTwin 2.0 上成功率 93.6%,RoboDojo VLA 赛道第 5;在同等 HG-DAgger 后训练下,三个真机任务平均成功率与进度分均高于 π0.5,以太网插接任务上 Rollback 数据训练的 CFG-DAgger 达到 70% 成功率、进度分 0.90。
- 🇬🇧 A VLA foundation model and embodied-agent system for stationary-base desktop manipulation. MR0 combines 147M vision-language samples with 15,060 hours of robot trajectories over 12 embodiments in three stages (discrete action-token pretraining, flow-matching mid-training for continuous cross-embodiment control, real-world post-training), plus Rollback (pairing replaced policy segments with human corrections for CFG-DAgger), a unified end-effector interface, asynchronous action-chunk merging and an event-driven agent. It reaches 93.6% on RoboTwin 2.0, ranks fifth in the RoboDojo VLA track, beats π0.5 in average success and progress under matched HG-DAgger on three real tasks, and Rollback-trained CFG-DAgger reaches 70% success and 0.90 progress on Ethernet insertion.

### [On Agentic Manipulation Policies](https://arxiv.org/abs/2611.09892) — 作者:Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, Jesse T. Gonzalez 等
开源状态 / Code: ✅ 已开源 / Released — Comments 称视频与代码见[项目页](https://apple-aiml-research.github.io/ml-amp/);具体仓库链接未单独核实。
- 🇨🇳 论文主张通用 AI 模型直接指挥机械臂比 VLA、WAM 等专用策略更可靠。作者系统分析"智能体操作策略"(AMP),给出参考框架 AMP1,可原样运行于单臂、双臂和移动操作,无需示范或任务训练。RoboLab-120 上零样本成功率 85.6%,领先 VLA 与 WAM 的 49.2% 和 42.9%;在三个机器人实例、12 个任务的 108 次真机试验中成功 104 次,相对强 VLA/WAM 基线失败率分别降低 20 倍和 15 倍;加入跨回合持久记忆后,RoboDojo 双臂任务失败率比零样本降低 4.6 倍。
- 🇬🇧 The paper argues generalist AI models commanding manipulators directly are more reliable than specialist VLA and WAM policies. It systematically studies agentic manipulation policies (AMPs) with a reference harness, AMP1, running unchanged across single-arm, bimanual and mobile manipulation without demonstrations or task training. It reaches 85.6% zero-shot on RoboLab-120 versus 49.2% and 42.9% for leading VLA and WAM, succeeds in 104 of 108 real trials over twelve tasks and three robots (20x and 15x lower failure than strong VLA/WAM baselines), and a persistent memory store lowers RoboDojo bimanual failure 4.6x versus zero-shot.

### [Toward the Era of Agentic Embodied Intelligence (A2-MEAS)](https://arxiv.org/abs/2611.09124) — 作者:Chao Liang, Ke Chen, Fengxiaoxiao Li, Shibo Huang 等
🏷️ 交叉方向 / Also: VLA、世界模型
开源状态 / Code: 🕒 计划开源 / Planned — 摘要称 "We will release the system, models, training scripts, and infrastructure"。
- 🇨🇳 基础模型已能指导机器人动作,但持续自主需要高效控制与失败恢复。A2-MEAS 是以"代码作为扩展接口"的具身多智能体框架:学习到的纠正代码结合纠正语言、空间证据、执行历史与动作提案,训练时由 MetaBrain 提供监督与运行指引,部署时用新代码在冻结权重下调整行为;动作模型 A2-WLA 在 VLA 上加入运动感知历史和隐式世界模型。BEHAVIOR 2026 公开 50 任务子集在线纠正前 Q-score 0.5755(2025 冠军报告值 0.2605 的 2.21 倍,但基准版本和配置不同),100 任务 Q-score 0.6411、成功率 45.40%;RoboTwin 2.0 上 A2-WLA 93.98%(完整系统 95.05%);12 个真机家庭任务平均 57.92%,π0.5 为 26.67%;训练吞吐 427.1 样本/秒,为 π0.5 参考实现的 4.03 倍。
- 🇬🇧 Foundation models increasingly guide robot actions, but sustained autonomy needs efficient control and failure recovery. A2-MEAS is an embodied multi-agent framework with code as the scaling interface: learned correction codes combine corrective language, spatial evidence, execution history and action proposals, MetaBrain gives training supervision and runtime guidance, and fresh codes adapt behavior with frozen weights at deployment; the action model A2-WLA adds motion-aware history and a latent world model to a VLA. It scores 0.5755 Q on the 50-task BEHAVIOR 2026 public subset before online correction (2.21x the 2025 winner's 0.2605 across different editions/configs), 0.6411 Q and 45.40% success on all 100 tasks, 93.98% on RoboTwin 2.0 (95.05% full system), 57.92% vs 26.67% for π0.5 over 12 real household tasks, and 4.03x training throughput.

### [Computer-Use Agents Are Embodied Generalists](https://arxiv.org/abs/2611.09847) — 作者:Pranjal Aggarwal, Sean Welleck(Cross-list)
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://pranjal2041.github.io/cua-embodied),未见代码链接。
- 🇨🇳 作者主张具身任务可表述为与数字软件的交互:构建把物理环境视角渲染到屏幕并提供控制的软件,让计算机使用智能体(CUA)用同样的截图和键鼠动作执行具身任务。使用单一 CUA 设计、仅更换软件,在四个 ECCV 研讨会竞赛中获得第 1、2、3、6 名,且无需针对竞赛调参。结论是 CUA 在软件上学到的视觉定位、精确点击、探索等技能可迁移到具身任务,并倡导沿同样训练策略走向单一通用具身模型。
- 🇬🇧 The authors argue embodied tasks can be cast as interaction with software: they build software that renders an agent's view of a physical environment on screen with controls, so a computer-use agent (CUA) acts via the same screenshots and keyboard/mouse actions. With a single CUA design and only the software changed, entries win first-, second-, third- and sixth-place prizes across four ECCV workshop competitions without competition-specific tuning. They conclude CUA skills such as visual grounding, precise clicking and exploration transfer to embodied tasks and advocate following the same training strategy toward one general embodied model.

### [A Controlled Study of Models, Skills, Feedback, and Curriculum in Agentic Robotics](https://arxiv.org/abs/2611.09030) — 作者:Kaiyuan Chen, Xinyue Zhu, Shuangyu Xie, Uksang Yoo 等
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 研究让编码智能体根据仿真与真实交互实现并迭代改进机器人策略的"自学习回路"。在 9 个操作任务、631 种实验配置、2.8 万次编码智能体 rollout 的受控仿真研究中,系统变化模型能力、技能先验、反馈结构和课程。结论是瓶颈往往不在信息获取,而在把信息解释成正确的策略更新;成功的回路取决于智能体能否有效归因失败、推理任务相关的空间与几何结构、有选择地重构代码。
- 🇬🇧 The paper studies the self-learning loop in which coding agents implement and iteratively improve robot policies from simulated and real interaction. In a controlled simulation study spanning nine manipulation tasks, 631 configurations and 28K coding-agent rollouts, it varies model capability, skill priors, feedback structure and curriculum. It finds the bottleneck is often not access to information but interpreting it into the right policy update; success depends on attributing failures, reasoning about task-relevant spatial and geometric structure, and selectively restructuring code.

### [PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](https://arxiv.org/abs/2611.05320) — 作者:Kewei Zhang, Juncheng Ma, Guodong Lv, Duomin Wang 等(11-03 提交,HF Daily Papers)
🏷️ 交叉方向 / Also: 世界模型(视频模型渲染)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/DAGroup-PKU/PyRUA-Lean/tree/DataFarm);Comments 给出,[项目页](https://dagroup-pku.github.io/PyRUA-Lean/DataFarm)。
- 🇨🇳 遥操作采集示范成本高且每个新任务从零开始。DataFarm 让编码智能体接收数据请求和一段目标场景的标定 episode,在仿真中重建任务(编写场景、专家控制器与成功判定器),由仿真给出精确动作,再用基于真实图像条件的视频模型把每次 rollout 渲染为多视角一致的照片级视频,独立评审在入库前认证。五个真机任务上仅用农场数据训练的策略与同数量遥操作数据相当(100 次试验中成功 93 对 84 次),在陌生桌布和彩色灯光下前者保持 87 次成功、遥操作训练策略降到 46;每任务适配平均 API 成本 21 美元,每多一个 episode 约 0.80 美元,一小时三视角数据平均 107 美元,低于 117 美元的中国遥操作报价。
- 🇬🇧 Teleoperated demonstrations are costly and every new task starts from scratch. In DataFarm a coding agent takes a data request plus one calibration episode, rebuilds the task in simulation (scene, expert controller, success judge), gets exact actions from the simulator, and renders each rollout with a video model conditioned on real images into consistent multi-view photographic video, with independent judges certifying everything. On five real tasks, policies trained only on farm data match teleoperation-trained ones (93 vs 84 successes in 100 trials) and keep 87 successes under an unseen tablecloth and coloured light where teleoperation-trained policies fall to 46. Adaptation costs $21 on average per task, each extra episode $0.80, and one hour of three-view data $107, below a $117 teleoperation quote in China.

### [PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real World](https://arxiv.org/abs/2611.06768) — 作者:Qiang Wang, Jianxin Bi, Shulong Jiang, Ruiyang Si 等(11-04 提交,HF Daily Papers)
开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 无链接(同系列 [PyRUA-Lean 仓库](https://github.com/DAGroup-PKU/PyRUA-Lean)已出现于 radar,但与本文的对应关系未核实)。
- 🇨🇳 研究编码智能体如何从物理交互中让机器人能力持续提升(具身递归自我改进,RSI)。PyRUA-REAL 让编码智能体把交互经验保存为持久记忆与可复用的可执行技能,指导后续探索与改进,并研究智能体如何协作、何种执行反馈有利于代码精修、任务描述与已有技能如何影响鲁棒性与迁移,以及部署时不依赖在线智能体的效率。在八个真实任务上平均成功率 91.1%,在 RoboDojo 的 42 个任务上平均 84.4%。
- 🇬🇧 The paper studies how coding agents can produce lasting robot-capability gains from physical interaction (embodied recursive self-improvement). PyRUA-REAL lets agents keep interaction experience as persistent memory and reusable executable skills, and examines agent collaboration, which execution feedback helps code refinement, how task specs and prior skills affect robustness and transfer, and efficiency when deployed without an online agent. It averages 91.1% success on eight real-world tasks and 84.4% on 42 RoboDojo tasks.

### [VOMMI: Collecting and Leveraging Portable Demonstrations for Mobile Manipulation](https://arxiv.org/abs/2610.08220) — 作者:Yutian Zhang, Xingrui Xiong, Siyuan Ma, Donghao Wang 等(replacement,2026-11-06 更新)
🏷️ 交叉方向 / Also: VLA、SLAM/视觉里程计
开源状态 / Code: ❓ 未知 / Unknown — Comments 无代码信息。
- 🇨🇳 便携式移动操作示范可缓解具身数据稀缺,但从 RGB 获得可靠、低成本、无需机器人的运动监督很难,直接用视觉里程计(VO)轨迹会因漂移与不一致带来问题。VOMMI 通过离线轨迹重建与在线视觉-运动条件,把便携 RGB 示范连接到 VLA 后训练:同步身体与手部视角,R2-VO 用稀疏几何锚点精修离线轨迹并产生多预测时域的因果局部运动 token,动作组残差适配器仅把这些 token 注入基础分支。仅用便携示范后训练的策略比用机器人采集示范训练的策略基座速度误差低 18.2%、末端平移精度相当;离线重建使身体与手部轨迹的绝对轨迹误差平均降低 24.6%(相对各自最佳基线);完整系统在三个真机任务上平均成功率比 OpenPI 0.5 高 8.3 个百分点。
- 🇬🇧 Portable mobile-manipulation demonstrations ease data scarcity, but robot-free motion supervision from RGB is hard and raw visual-odometry trajectories drift. VOMMI links portable RGB demonstrations to VLA post-training via offline trajectory reconstruction and online visual-motion conditioning: it synchronizes body and hand views, R2-VO refines trajectories with sparse geometric anchors and emits causal local-motion tokens over several horizons, and an action-group residual adapter injects them into the base branch only. A policy post-trained only on portable demonstrations has 18.2% lower base-velocity error than one trained on robot demonstrations with comparable end-effector accuracy, offline reconstruction cuts absolute trajectory error 24.6% on average versus the best baseline per stream, and the full system improves mean success by 8.3 points over OpenPI 0.5 on three real tasks.

### [CS-Pi: Constraint-Satisfying Flow Policy Sampling](https://arxiv.org/abs/2611.08654) — 作者:Soumojit Bhattacharya, Oliver Kroemer, Shubham Tulsiani(CoRL 2026)
🏷️ 交叉方向 / Also: 运动控制(推理期约束控制,模仿学习策略,非 RL)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/Sumo048/CS-Pi);[项目页](https://sumo048.github.io/CS-pi_site/)链接,匿名 `git ls-remote` 验证存在。
- 🇨🇳 部署中的 flow-matching 策略常需满足示范中不存在的约束(如避开从未见过的障碍),重训不现实,必须在推理时施加,同时不能丢弃策略学到的内容。常用梯度引导会在策略不确定时(如绕左或绕右)用平均动作估计代价而穿过障碍。CS-Pi 的"采样-投影-加噪"采样器把投影的高效与拒绝采样的合理性结合:把每次采样投影到最近的安全动作,按投影移动距离加回噪声,重新运行未经修改的策略直到采样安全;只替换投影步骤即可扩展到连续代价。在 2D 诊断、7 自由度货架抓放、朝向偏好和 Franka 零样本部署中,货架任务安全成功率 81%(投影 55%),硬件上 55%(投影 40%),且保持合理性。
- 🇬🇧 Deployed flow-matching policies often must satisfy constraints absent from demonstrations (e.g. unseen obstacles); retraining is impractical so constraints must be enforced at inference without discarding what the policy learned. Gradient guidance fails when the policy is uncertain (passing left or right) because the averaged action estimate can pass through the obstacle. CS-Pi's draw-project-renoise sampler projects each draw to the nearest safe action, re-adds noise scaled to the projection distance and reruns the unmodified policy until a draw is safe, extending to continuous costs by replacing only the projection step. It reaches 81% safe success on a shelf pick-and-place versus 55% for projection, and 55% versus 40% on a zero-shot Franka deployment, while staying plausible.

### [Horizon-Coupled Obstacle Guidance for Relative-Action Diffusion Policies](https://arxiv.org/abs/2611.09340) — 作者:Guangyuan Wang, Haishan Xia, Zitao Zhang, Kejia Chen 等
🏷️ 交叉方向 / Also: 运动控制(推理期避障,模仿学习策略,非 RL)
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 现有策略级引导往往在各个时域步上独立施加避障修正,难以把动作序列协调成完整的绕行。该方法为预训练的相对动作扩散策略提供推理期避障:把累积相对动作展开成工作空间轨迹,用基于 SDF 的障碍模型评估沿轨迹的障碍交互,并在去噪中把每个障碍响应传播给所有相关的动作增量。四类操作任务共七个有障碍场景的真机实验中,无碰撞任务成功 105/140(75.0%),绝对动作逐点引导为 8/140(5.7%);消融表明相对动作的时域耦合形式贡献最大。
- 🇬🇧 Existing policy-level guidance often applies obstacle corrections independently at single horizon steps, failing to coordinate the action sequence into a complete detour. This inference-time framework rolls cumulative relative actions into a workspace trajectory, evaluates obstacle interactions with an SDF obstacle model, and propagates each response to all contributing action increments during denoising of a pretrained relative-action diffusion policy. In real-robot experiments over seven obstacle scenarios and four manipulation tasks it achieves 105/140 (75.0%) collision-free successes versus 8/140 (5.7%) for absolute-action pointwise guidance, with ablations showing the relative-action horizon-coupled formulation gives the larger gain.

### [DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation](https://arxiv.org/abs/2611.05119) — 作者:Zhewei Gui, Anthony Bolton, Jiyao Zhang, Zeyuan Chen 等(replacement,2026-11-06 更新)
🏷️ 交叉方向 / Also: 运动控制(灵巧手策略;摘要未说明是否用 RL,故留在本类)
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://dex-hot.github.io/),摘要无代码信息。
- 🇨🇳 灵巧操作常以物体位姿或轨迹为目标,手-物体配置只是隐式涌现。DexHOT 将其表述为"手-物体配置转移":在联合描述手关节与物体相对腕部位姿的可行配置间移动;从合成的可行配置对中学习可复用的关系条件转移基元,无需人类参考动作,并通过对配置子目标的闭环跟踪组合长时域行为。DexHOTBench(120 个物体)上单一策略对已见物体转移成功率 80.5%、未见物体 69.4%;真机灵巧手 200 次转移成功率 61.5%,六个示范引导任务的任务成功率 90%。
- 🇬🇧 Dexterous manipulation is usually specified by object poses or trajectories, leaving hand-object configurations implicit. DexHOT formulates it as hand-object configuration transfer between feasible configurations jointly specifying hand articulation and object pose relative to the wrist, learns a reusable relation-conditioned transfer primitive from synthetic feasible pairs without human reference motions, and composes long-horizon behavior by closed-loop tracking of configuration subgoals. On DexHOTBench with 120 objects one policy reaches 80.5% on seen and 69.4% on unseen objects; on a real dexterous hand it gets 61.5% over 200 transfers and 90% task success over six demonstration-guided tasks.

### [ToolDex: An Ego-Exo Human Demonstration Dataset for Creative Physical Tool Use](https://arxiv.org/abs/2611.09036) — 作者:Mohamed Elmoghany, Kehan Li, Ruoqu Chen 等
开源状态 / Code: ❓ 未知 / Unknown — 有[数据集页面](https://tooluse-dataset.github.io/),代码/数据发布状态未说明。
- 🇨🇳 创造性工具使用是通用具身智能的重要一步,但缺少规模、保真度和多样性足够的真实数据集。ToolDex 是大规模自我视角-外部视角(ego-exo)人类示范数据集,用同步自我视角相机和八个外部视角相机记录人类选择、改造、挪用物体作为工具的场景,提供手、工具、目标物体及其可变形交互的丰富标注,并建立三类能力基准:物理工具使用推理、稀疏视角 3D/4D 重建、机器人策略学习。预印本摘要未给出定量结果(数据集/基准类论文)。
- 🇬🇧 Creative tool use is a step toward general embodied intelligence, but real datasets of sufficient scale, fidelity and diversity are lacking. ToolDex is a large-scale ego-exo human demonstration dataset with synchronized egocentric cameras and eight exocentric cameras capturing humans selecting, adapting and repurposing objects as tools, with rich annotations for hands, tools, targets and deformable interactions, and a benchmark suite for physical tool-use reasoning, sparse-view 3D/4D reconstruction and robot policy learning. The preprint abstract gives no quantitative results.

**其余条目 / Others(14):** [Augmentron](https://arxiv.org/abs/2611.09145)、[HOC2R](https://arxiv.org/abs/2611.08920)、[Can LLMs Debug Robots by Editing Their Weights?](https://arxiv.org/abs/2611.09376)、[DRAP](https://arxiv.org/abs/2611.05029)、[MATE](https://arxiv.org/abs/2607.17257)、[Real-Time Execution with Autoregressive Policies](https://arxiv.org/abs/2606.13355)、[NoContactNoWorries](https://arxiv.org/abs/2606.24450)、[HomeLoop](https://arxiv.org/abs/2611.08914)、[PyRUA-Lean 仓库](https://github.com/DAGroup-PKU/PyRUA-Lean)、[Flex-RSI](https://arxiv.org/abs/2611.08946)、[ManiTaskGen](https://arxiv.org/abs/2505.20726)、[Learning-augmented robotic automation for real-world manufacturing](https://arxiv.org/abs/2604.22235)、[Adaptive Collision Sensitivity for Human-Robot Collaboration](https://arxiv.org/abs/2409.20184)、[Sketch-MoMa](https://arxiv.org/abs/2412.19153)。共 12 条展开 + 14 条列名。 / 12 expanded + 14 listed.

**另见 / See also:** [Open-HumanWAM](https://arxiv.org/abs/2611.06817)(已归入 世界模型与 WAM)、[SLA](https://arxiv.org/abs/2611.08373)(已归入 VLA)、[PRISM](https://arxiv.org/abs/2611.08917)(已归入 VLA)。

---

## VLA / VLA(展开 11 条 / 11 expanded)

### [SLA: Scaling Spatial-Language-Action Model via Continual Pre-training](https://arxiv.org/abs/2611.08373) — 作者:Fuhao Li, Wenxuan Song, Qizhou Huang, Ziyang Zhou 等(HF Daily Papers 97 赞)
🏷️ 交叉方向 / Also: 空间智能 / Spatial Intelligence
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/OpenHelix-Team/Spatial-Forcing/tree/master/SLA);Comments 给出,仓库匿名 `git ls-remote` 验证存在(radar 中该仓库 +23 星,子目录未单独核实)。
- 🇨🇳 VLA 基础模型多继承 2D 视觉-语言预训练的视觉表征,空间监督通常只在任务适配时引入。SLA 从预训练的 π0.5 初始化,在持续预训练中联合优化动作预测与中间视觉嵌入和冻结 3D 感知模型空间表征的对齐,并在下游后训练中保持;整合异构机器人数据集,引入特征依赖门控自适应聚合多个 VLA 层的视觉嵌入,教师可利用部分可得的深度和相机标定,概率状态丢弃促使模型依赖视觉线索。所有辅助组件仅训练时使用,推理架构不变;摘要未给出定量结果。
- 🇬🇧 VLA foundations inherit 2D vision-language visual representations while spatial supervision is added only at task adaptation. SLA, initialized from π0.5, jointly optimizes action prediction and alignment between intermediate visual embeddings and a frozen 3D perception model during continual pre-training and keeps it in post-training; it unifies heterogeneous robot datasets, uses feature-dependent gates to aggregate embeddings across VLA layers, lets the teacher use partial depth and calibration, and applies probabilistic state dropout to force reliance on visual cues. All auxiliary parts are training-only so pretrained weights and inference architecture are reused; the abstract reports no quantitative results.

### [From Pixels to Actions — Towards Native Vision-Language-Action Policies (NEO-VLA)](https://arxiv.org/abs/2611.06918) — 作者:Weichen Fan, Haiwen Diao, Penghao Wu, Siyuan Hu 等(HF Daily Papers 62 赞)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/EvolvingLMMs-Lab/NEO/tree/main/VLAKit);Comments 给出,仓库匿名验证存在。
- 🇨🇳 VLA 通常先由视觉编码器压缩感知再做动作推理,但操作依赖局部几何、边界、深度等最易被抽象丢失的视觉信号。NEO-VLA 是无编码器的原生架构:图像经轻量 patch 卷积 token 化后与语言一起贯穿骨干演化,flow-matching 动作专家可读取不同深度的指令条件视觉表征。受控比较中原生架构优于基于编码器的对应模型,全量微调缩小但不消除差距,单靠加规模也无法弥补;逐层探测显示动作关键信号常在最终视觉表征之前就达到峰值;在多种操作设置和分布偏移下控制更强更鲁棒(摘要未给出具体数字)。
- 🇬🇧 VLAs usually compress perception with a visual encoder before action reasoning, though manipulation hinges on local geometry, boundaries and depth that abstraction loses. NEO-VLA is encoder-free: images are tokenized by lightweight patch convolutions and evolve jointly with language through the backbone, so a flow-matching action expert can draw on instruction-conditioned representations at different depths. Native architectures beat encoder-based ones in controlled comparisons, full fine-tuning narrows but does not erase the gap, scale alone cannot recover it, and layer-wise probing shows action-critical signals peak before the final visual layer; across settings and shifts it controls more strongly and robustly, with no figures in the abstract.

### [VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models](https://arxiv.org/abs/2611.08698) — 作者:Luca Macesanu, Tianluo Zhang, Aditya Patil, Archit Sharma 等
开源状态 / Code: ❓ 未知 / Unknown — [项目页](https://ai4ce.github.io/VICTR/)称含代码、数据与视频,但未取得仓库链接,待核实。
- 🇨🇳 基于检索的后训练让 VLA 具备示范上下文学习(ICL),但检索效果取决于选到与当前执行阶段相关的上下文,单靠视觉相似度难以捕捉。VICTR 围绕上下文价值函数估计器 IC-VFE:以参考示范视频、语言指令与当前观测估计任务相对进度,即使对训练中未见任务也能把当前状态与示范执行对齐;再据此挑选对应阶段的示范片段输入为上下文动作生成后训练的 π0.5 策略。在未见的域外真机操作任务上,成功率从微调 π0.5 基线的 6.2% 提高到 23.8%,任务进度率从 28.9% 提高到 55.5%。
- 🇬🇧 Retrieval-based post-training gives VLAs in-context learning from demonstrations, but retrieval depends on selecting context relevant to the current execution stage, which visual similarity alone may miss. VICTR is built around an In-Context Value Function Estimator (IC-VFE) that conditions on a reference demonstration video, instruction and current observation to estimate task-relative progress, aligning the current state with a demonstration even for unseen tasks, then selects demonstration chunks at the matching stage for a π0.5 policy post-trained for in-context action generation. On unseen out-of-domain real-world tasks it raises success from 6.2% (fine-tuned π0.5) to 23.8% and progress from 28.9% to 55.5%.

### [ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2611.08827) — 作者:Sungwon Moon, Minji Kim, Hyemin Boo, Daeun Song 等
开源状态 / Code: ❓ 未知 / Unknown — Comments 为空。
- 🇨🇳 VLA 推理成本限制闭环响应速度,已有视觉 token 剪枝都在视觉编码器处理完整个观测之后才估计冗余。ActPrune 免训练,把剪枝决策提前到视觉编码器之前,依据上一控制步已预测的动作块所给出的末端与相机运动几何先验:第三人称固定视角保留沿投影末端轨迹的 patch 与语义锚点,手腕视角在补偿动作引起的相机运动后剪掉不变的 patch。在 LIBERO、VLABench 两个仿真环境与四个真机任务上,最高 1.61 倍加速、FLOPs 减少 59.5%,成功率下降可忽略。
- 🇬🇧 VLA inference cost limits closed-loop responsiveness, and prior token pruning estimates redundancy only after the encoder has processed the whole observation. ActPrune is training-free and moves pruning before the vision encoder using a geometric prior from the previous action chunk (end-effector and camera motion): in the fixed third-person view it keeps patches along the projected end-effector trajectory plus semantic anchors, and in the wrist view it prunes patches unchanged after compensating action-induced camera motion. On LIBERO, VLABench and four real tasks it achieves up to 1.61x speedup and 59.5% FLOPs reduction with negligible success loss.

### [PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation](https://arxiv.org/abs/2611.08917) — 作者:Jiachen Tao, Gengyu Zhang, Haoxuan Wang, Bing Liu 等(NeurIPS 2026)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅注明 NeurIPS 2026 接收。
- 🇨🇳 VLA 部署需要技能保留与长时域组合,标准做法把每个新任务吸收进一个共享更新,既无可复用技能的参数级位置,也无调用机制。作者发现各技能的低秩更新处于可区分的低维子空间,复合任务 LoRA 约一半 Frobenius 能量集中其中。PRISM 因此把技能表示为参数级基元:每类技能一个专用低秩动作专家适配器放入基元库,配合技能残差,由按块的 VLM 条件路由器(以动作派生的确定性 oracle 逐块标签监督)在推理时组合,基元冻结。RoboCasa365 上原子技能成功率 56.43%、长时域复合任务 20.00%,标准 π0.5-LoRA 两阶段微调为 17.86% 与 17.50%(原子 / 复合);并在 AgileX PIPER 真机上验证。
- 🇬🇧 VLA deployment needs skill retention and long-horizon composition, but the standard recipe folds every task into one shared update with no parameter-level locus for skills. The authors find per-skill low-rank updates occupy a distinguishable low-dimensional subspace holding roughly half of a composite LoRA's Frobenius energy. PRISM stores each skill family as a low-rank action-expert adapter in a primitive bank, adds skill residuals, and composes them with a per-chunk VLM-conditioned router supervised by action-derived oracle labels, keeping primitives frozen. On RoboCasa365 it gets 56.43% atomic and 20.00% composite success versus 17.86% and 17.50% for a two-stage π0.5-LoRA fine-tune (atomic / composite), plus validation on a real AgileX PIPER.

### [ODEAction: From Predicting Chunks to Evolving Actions](https://arxiv.org/abs/2611.09672) — 作者:Qishen Wang, Pengxiang Ding, Shifeng Bao, Mingyang Sun 等
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅注明技术报告。
- 🇨🇳 VLA 按块生成动作,块边界处会出现不连续。ODEAction 用"连续动作演化"取代动作块预测:模型学习定义在动作空间上的动作转移场(转移向量表示当前动作随演化时间的变化率),执行时以当前动作为初值用 ODE 积分,递归生成带显式依赖的后续动作;它作为动作头实现,不依赖特定视觉-语言骨干。在 LIBERO、EBench、RoboTwin 和真机上,相对匹配的动作块基线同时提升任务性能与轨迹质量,精细操作任务增益尤为明显(摘要未给出具体数字)。
- 🇬🇧 VLAs generate actions in chunks, causing discontinuities at chunk boundaries. ODEAction replaces chunk prediction with continuous action evolution: it learns an action transition field over action space whose vector gives the evolution rate of the current action, and at execution integrates it as an ODE from the current action to recursively produce subsequent actions with explicit dependencies; it is an action head independent of the vision-language backbone. On LIBERO, EBench, RoboTwin and real robots it improves task performance and trajectory quality over matched chunking baselines, notably on fine manipulation, though the abstract gives no figures.

### [SURE: Spatiotemporal Uncertainty Representation for Efficient Vision-Language-Action Learning](https://arxiv.org/abs/2611.09684) — 作者:Jingye Zhang, Choo Sin Wai, Dake Zhong, Zhifang Liu 等
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 VLA 依赖大量示范数据,而逐点监督把每个示范动作当作精确目标,忽略了空间上多个相近动作都可成功、时间上等价示范速度不同的不确定性。SURE 给 VLA 骨干加一个轻量转置卷积概率动作解码器,通过相邻动作 bin 的局部相关性捕捉空间不确定性,并引入 Soft-DTW 对齐监督容忍预测与示范动作块间的局部时间偏差。在 LIBERO、RoboTwin 2.0 与真机任务上,仅用 10% 示范数据或 20% 训练步数即可达到或超过基线 VLA 的操作成功率。
- 🇬🇧 VLAs depend on large demonstration sets, and pointwise supervision treats each demonstrated action as exact despite spatial uncertainty (many nearby actions succeed) and temporal variation (equivalent demonstrations at different speeds). SURE adds a lightweight transposed-convolutional probabilistic action decoder capturing spatial uncertainty through neighboring action-bin correlations, plus Soft-DTW alignment supervision for local timing variation between predicted and demonstrated chunks. On LIBERO, RoboTwin 2.0 and real tasks it matches or surpasses baseline VLAs with only 10% of demonstrations or 20% of training steps.

### [VLA Handover: Failure-Prediction-Based Switching from On-Robot to Server VLA Models](https://arxiv.org/abs/2611.08987) — 作者:Takayuki Nishio(投稿 IEEE ICC 2027)
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 大 VLA 泛化好但难在机器人上实时运行,小 VLA 易失败;通过 B5G/6G 远程调用服务器大模型每个动作块都请求则限制单服务器支持的机器人数量。VLA handover 让机器人运行小 VLA,仅在预测其可能失败时切换到服务器上的大 VLA;将切换形式化为在要求成功概率下最小化请求代价,并提出无需重训任何 VLA 的启发式框架。在 LIBERO 四个套件中的三个上用 SmolVLA 与 π0.5 仿真,相对仅小 VLA 成功率提高 11–22 个百分点,相对全程服务器控制请求减少 49–77%,成功率仅低 2–4 个百分点,且完成时间随网络时延增长更慢。
- 🇬🇧 Large VLAs generalize well but are hard to run on robots, small ones fail more, and querying a server for every action chunk limits robots per server. VLA handover runs a small VLA on the robot and switches to a large server VLA only when failure is likely, formulating switching as minimizing request cost under a required success probability and solving it heuristically without retraining either VLA. In simulation on three LIBERO suites with SmolVLA and π0.5 it raises success 11–22 points over the small VLA alone and sends 49–77% fewer requests than server-only control at 2–4 points lower success, with completion time growing less with network latency.

### [Localizing and Editing the Goal Representation of a Vision-Language-Action Model](https://arxiv.org/abs/2611.08895) — 作者:Sudhanshu Srivastava, Faisal Aqlan
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 研究 OpenVLA 是否遵守"不要把碗放在炉子上"这类禁令,以及它在何处表示执行的目标。在 LIBERO-Goal 上结合闭环 rollout、激活修补、线性探针、激活引导与运行时监视器。结果:否定词对执行哪个任务没有可检测影响,模型在 79% 的否定 rollout 中执行了被禁任务(普通任务完成 78%);第 8 层指令 token 处的固定引导向量使 18 个 rollout 中 12 个被重定向,第 12–20 层固定向量与预填充修补对 158 个全部无效,第 16 层起只有对每个解码动作 token 的修补有效(第 24 层 15/18);第 32 层目标读出检测不遵守比失败检测器更好。结论是禁令应在指令之外强制执行并监控目标读出。
- 🇬🇧 The paper asks whether OpenVLA follows prohibitions such as "do not put the bowl on the stove" and where it represents the goal. On LIBERO-Goal it combines closed-loop rollouts, activation patching, linear probes, steering and runtime monitors. Negation had no detectable effect on which task executes: the forbidden task ran in 79% of negated rollouts (78% of plain tasks completed). A fixed layer-8 steering vector at instruction tokens redirected 12 of 18 rollouts, fixed vectors and prefill patches at layers 12–20 redirected 0 of 158, and from layer 16 only patches at every decoded action token worked (15/18 at layer 24); the layer-32 goal read-out detects non-compliance better than failure detectors. Prohibitions should be enforced outside the instruction with read-out monitoring.

### [DobotTrack: Target-Grounded Vision-Language-Action Learning for Embodied Person Tracking](https://arxiv.org/abs/2611.09041) — 作者:Shengjun Deng, Yinghan Zhang, Chengrui Wei, Liu Liang 等
🏷️ 交叉方向 / Also: VLN / 导航(语言引导的具身人物跟踪)、四足机器人
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/Dobot-Team/dobot_track);摘要给出,匿名 `git ls-remote` 验证存在。
- 🇨🇳 语言引导的具身人物跟踪要求移动智能体根据指代描述识别目标并在第一人称观测下持续跟随。DobotTrack 研究五种辅助任务(人物分割、边框定位、视觉-空间分类、未来 DINO 特征预测、未来帧预测),采用互补的掩码与边框监督,并提出 Q-identity——利用目标定位预测有选择地保留身份判别外观特征与空间线索的目标条件历史视觉压缩模块。0.8B 参数模型在 EVT-Bench 三个任务上平均成功率 77.9%,比 OmTrackVLA 高 16.9 个百分点;另构建四足机器人采集的真实数据集(126 个 episode、596,323 帧带掩码标注)。
- 🇬🇧 Language-guided embodied person tracking needs a mobile agent to identify a target from a referring description and keep following it under egocentric observations. DobotTrack studies five auxiliary tasks (segmentation, box grounding, visual-spatial classification, future DINO feature and future frame prediction), adopts complementary mask and box supervision, and introduces Q-identity, a target-conditioned history compression module that uses grounding predictions to keep identity-discriminative appearance and spatial cues. Its 0.8B model averages 77.9% success on EVT-Bench, 16.9 points above OmTrackVLA, and the authors build a real quadruped-collected dataset of 126 episodes and 596,323 mask-annotated frames.

### [STAR: Steering Action Representations with Proprioception for VLA Inference](https://arxiv.org/abs/2610.41009) — 作者:Guangyu Zhao, Yongchang Zhang, Haoxuan Ru, Kaichen He 等(replacement,2026-11-06 更新)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/PKU-VaLuE-Lab/STAR);摘要给出,匿名 `git ls-remote` 验证存在。
- 🇨🇳 探测实验显示 VLA 输出附近的动作表征没有完全保留任务相关的视觉落地("晚层落地差距")。STAR 是免训练的推理方法:对晚层残差更新做指数移动平均,使后续动作表征继承前层的物体感知更新方向,无需更新模型或改架构;还用近期本体感觉状态自适应混合强度,在执行动力学变化快时保守混合。在机器人操作基准上提高了晚层的物体感知,平均任务成功率提高 4.0 个百分点。
- 🇬🇧 Probing shows action representations near the VLA output do not fully preserve task-relevant visual grounding (a late-layer grounding gap). STAR is a training-free inference method that applies an exponential moving average over late-layer residual updates so later representations inherit object-aware directions from earlier layers without model or architecture changes, and adapts the mixing strength using recent proprioceptive states, mixing conservatively when execution dynamics change fast. On manipulation benchmarks it improves late-layer object awareness and raises average task success by 4.0 percentage points.

### [HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation](https://arxiv.org/abs/2611.02660) — 作者:Gyeonghun Kim, Donghoon Kim, Minsoo Choi, Suyun Lee 等(11-02 提交,HF Daily Papers)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/kimspacehuni/HeLM)(HF githubRepo 字段);[项目页](https://kimspacehuni.github.io/HeLM/);仓库匿名 `git ls-remote` 验证存在。
- 🇨🇳 多数 VLA 在马尔可夫假设下只把当前观测映射到动作,在需要工作记忆的非马尔可夫任务中失败。HeLM 受"内心独白"启发,是一个分层 VLA 框架,通过分解的事件检测与事件触发的记忆更新,用显式语言维护任务相关历史。在 10 个真实非马尔可夫任务(56 个变体,含 5 个需要跨任务边界持久上下文的新任务)上,回合内成功率比最强基线高 12.8 个百分点,组合泛化任务子任务成功率 78%,在长时域下内存最多减少 4.5 倍、比关键帧基线快 2.5 倍。
- 🇬🇧 Most VLAs map only the current observation to action under a Markovian assumption and fail on tasks that need working memory. Inspired by "inner monologue", HeLM is a hierarchical VLA framework that keeps task-relevant history in explicit language via factorized event detection and event-triggered memory updates. Across 10 real non-Markovian tasks (56 variants, including five new inter-episode tasks) it improves intra-episode success by 12.8 points over the strongest baseline, reaches 78% subtask success on compositional generalization, and uses up to 4.5x less memory and runs 2.5x faster than the keyframe baseline at long horizons.

**其余条目 / Others(3):** [HiMEM](https://arxiv.org/abs/2611.09355)(π0 在 LIBERO 上 91.88% → 98.20%)、[Real-Time Execution with Autoregressive Policies](https://arxiv.org/abs/2606.13355)、[DRAP](https://arxiv.org/abs/2611.05029)。共 11 条展开 + 3 条列名。

**另见 / See also:** [CompVLA](https://arxiv.org/abs/2609.23614)(已归入 运动控制·传统)、[Meituan-Robotics-0](https://arxiv.org/abs/2611.08577)(已归入 具身智能与机器人基础模型)、[A2-MEAS](https://arxiv.org/abs/2611.09124)(已归入 具身智能)、[VOMMI](https://arxiv.org/abs/2610.08220)(已归入 具身智能)。

---

## VLN / VLN

今日无专门的 VLN 论文(arXiv 关键词检索 vision-language navigation 命中 0)。相关工作:[VLD](https://arxiv.org/abs/2512.07976)(已归入 运动控制·RL)、[DobotTrack](https://arxiv.org/abs/2611.09041)(已归入 VLA)。 / No dedicated VLN papers today; related items were filed under higher-priority categories (see links above).

**另见 / See also:** [VLD](https://arxiv.org/abs/2512.07976)(已归入 运动控制·RL)、[DobotTrack](https://arxiv.org/abs/2611.09041)(已归入 VLA)。

---

## 世界模型与 WAM / World Models & WAM(展开 8 条 / 8 expanded)

### [Future Representation Distillation for Imagination-free World Action Models (DreamFree)](https://arxiv.org/abs/2611.04527) — 作者:Jaehyeong Jo, Sangwon Jang, Sihyun Yu, Seonghyeon Ye 等(11-03 提交,HF Daily Papers)
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://harryjo97.github.io/dreamfree/),摘要与 Comments 无代码链接。
- 🇨🇳 WAM 利用预训练视频扩散模型的预测知识做机器人控制,但迭代视频去噪昂贵,视觉预测不准还会损害动作预测。DreamFree 通过表征蒸馏把预训练视频扩散模型改造为预测型视觉编码器:编码器仅凭当前观测预测冻结视频扩散模型的表征,再训练动作模块从中提取动作相关信息,无需生成未来视频。在真实与仿真任务上成功率高于最先进的 VLA 与 WAM,并以 14B 视频扩散骨干实现 11 Hz 实时闭环控制,还能利用更强的视频先验和额外视频数据,并从含不同本体的视频示范中学习无动作标注的新任务。
- 🇬🇧 WAMs use video-diffusion predictive knowledge for control, but iterative denoising is costly and inaccurate predictions can hurt actions. DreamFree repurposes a pretrained video diffusion model as a predictive visual encoder through representation distillation: the encoder predicts a frozen model's representation from only the current observation, and an action module extracts action-relevant information from it, so no future video is generated. It beats state-of-the-art VLAs and WAMs on real and simulated tasks while running real-time closed-loop control at 11 Hz with a 14B video backbone, benefits from stronger video priors and extra video data, and learns new tasks from action-free demonstrations, including from other embodiments.

### [Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models](https://arxiv.org/abs/2611.06817) — 作者:Juncheng Ma, Jiaxin Li, Jiankai Tu, Bo Liang 等(Cross-list;HF Daily Papers 38 赞,HF 标题为 Open-HumanScale)
🏷️ 交叉方向 / Also: 具身智能与机器人基础模型(数据 / 训练配方)
开源状态 / Code: ✅ 已开源 / Released — [代码仓库](https://github.com/DAGroup-PKU/HumanNet/tree/Open-HumanWAM);[项目页](https://dagroup-pku.github.io/open-humanwam/);摘要称开源语料、数据整理与预训练流水线、预训练/后训练权重、推理代码与仿真评测套件(仓库匿名可访问,分支未单独核实)。
- 🇨🇳 自我视角人类视频是可扩展的操作先验来源,但把数据规模转化为可泛化策略需要严格的数据整理与训练配方。Open-HumanWAM 提供首个完全开放的、扩展到 5 万小时自我视角预训练的配方,以带手部动作和语言标注的 Open-HumanWAM-50K 语料为核心,发现预训练小时数与下游机器人成功率之间的对数线性缩放律。仅用人类视频预训练的 HumanWAM-Vanilla 后训练后在 RoboTwin 2.0 Clean2Clean 达 92.08%、Clean2Random 68.88%,RoboDojo 平均成功率 14.17%;人机联合预训练的视觉目标条件模型 HumanWAM-Goal 将 RoboTwin 2.0 提高到 92.70% 与 84.60%,并在真机上显示出对未见视觉目标的涌现式上下文学习。
- 🇬🇧 Egocentric human video is a scalable source of manipulation priors, but turning data scale into generalizable policies needs rigorous curation and training recipes. Open-HumanWAM is the first fully open recipe scaling egocentric pretraining to 50,000 hours, anchored by Open-HumanWAM-50K with hand-motion and language annotations, revealing a log-linear scaling law between pretraining hours and downstream robot success. HumanWAM-Vanilla, pretrained only on human video, reaches 92.08% on RoboTwin 2.0 Clean2Clean and 68.88% on Clean2Random after post-training, plus 14.17% mean success on RoboDojo; the visual-goal-conditioned HumanWAM-Goal with joint human-robot pretraining raises these to 92.70% and 84.60% and shows emergent in-context learning on real robots for unseen visual goals.

### [MDF++: Visuo-Tactile World Action Model with End-to-end Representation Learning](https://arxiv.org/abs/2611.09293) — 作者:Zixuan Huang, Jinhao Yu, Zachary Charlick, Dmitry Berenson 等(CoRL 2026)
🏷️ 交叉方向 / Also: 接触密集操作 / 触觉
开源状态 / Code: ❓ 未知 / Unknown — 有[网站](https://jointmdf.github.io),摘要与 Comments 无代码说明。
- 🇨🇳 现有 WAM 常依赖用重建目标训练的冻结预训练编码器,表征未必适合机器人控制。MDF++ 是视觉-触觉 WAM,以扩散骨干端到端学习多感官观测的隐表征;朴素联合训练会导致特征坍缩,因此引入利用跨模态相关性的多任务学习策略以学到任务相关表征。在包括真实螺栓拧紧与螺母配合在内的接触密集操作任务上,比基于冻结预训练表征的 WAM 最多高出 50%。
- 🇬🇧 Existing WAMs typically rely on frozen pretrained encoders trained for reconstruction, whose representations may not suit control. MDF++ is a visuo-tactile WAM that learns latent representations of multisensory observations end-to-end with a diffusion backbone; naive joint training collapses features, so it uses a multi-task strategy exploiting cross-modal correlations to learn task-relevant representations. On contact-rich tasks including real bolt screwing and nut mating, it outperforms WAMs built on frozen pretrained representations by up to 50%.

### [Self-Distilling Future Video Representations for World Action Models (FRED)](https://arxiv.org/abs/2610.30320) — 作者:Huiwon Jang, Suhyeok Jang, Hyeonmo Kang, Seungku Kim 等(replacement,2026-11-06 更新)
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://huiwon-jang.github.io/FRED/),无代码说明。
- 🇨🇳 一类 WAM 通过只做一次去噪、提取中间未来视频表征并给独立动作解码器提供条件来提升推理效率,因此动作质量直接依赖这些未来表征。FRED 用自蒸馏训练 WAM,让它从噪声单步预测未来表征,目标取自真实未来观测提取的表征,并让视频模型以历史观测为条件提供时间上下文。在多种真实操作场景中持续优于其他 WAM,在长时域和域外零样本环境泛化上增益尤大,并显著改善人到机器人的技能迁移:在仅出现于人类视频的任务上成功率达 50.0%,最强竞争 WAM 为 19.4%。
- 🇬🇧 One line of WAMs improves efficiency by conditioning a separate action decoder on intermediate future-video representations from a single denoising step, so action quality depends directly on them. FRED trains WAMs by self-distillation to predict future representations from noise, with targets extracted from ground-truth future observations, and conditions the video model on historical observations for temporal context. It consistently beats competing WAMs across real-world manipulation, with large gains on long-horizon and out-of-domain zero-shot tasks, and reaches 50.0% success on tasks demonstrated only in human videos versus 19.4% for the best competing WAM.

### [WorldBridge: Bridging Video and Action for Task Generalization in World Action Models](https://arxiv.org/abs/2610.40748) — 作者:Jun Cen, Yubo Guo, Hao Li, Liangkai Li 等(replacement,2026-11-06 更新)
开源状态 / Code: ❓ 未知 / Unknown — 有[项目页](https://worldbridge-jd.github.io/),无代码说明。
- 🇨🇳 研究 WAM 的任务泛化中视频泛化与动作泛化的各自贡献。RoboTwin 2.0 上仅用分布内视频-动作监督时,分布外任务成功率 25.07%;加入这些任务的无动作标签视频后升至 55.90%,每任务再加一条带动作示范升至 70.70%。据此提出 WorldBridge:视频与动作专家通过结构化注意力连接并以联合 flow matching 训练,加入双时间尺度视觉记忆和动作强制,以及统一的数据处理流水线。在 RoboTwin 2.0 全数据设置 96.23%、clean-to-random 80.9%,RoboCasa GR1 TableTop 82.8%,DOMINO Level-1 57.6%,在对比方法中最优。
- 🇬🇧 The paper dissects video generalization versus action generalization in WAM task transfer. On RoboTwin 2.0, in-distribution video-action supervision yields 25.07% on out-of-distribution tasks; adding action-free videos of those tasks raises it to 55.90% and one action-labeled demonstration per task to 70.70%. WorldBridge uses separate video and action experts linked by structured attention with joint flow-matching training, two-scale visual memory, action forcing and a unified data pipeline. It reaches 96.23% on RoboTwin 2.0 full data, 80.9% clean-to-random, 82.8% on RoboCasa GR1 TableTop and 57.6% on DOMINO Level-1, best among compared methods.

### [CLAW: Continuous Latent Action World Models via Adversarial Regularization](https://arxiv.org/abs/2606.04130) — 作者:Tewodros Ayalew, Samuel Wheeler, Matthew Jeung, Xiao Zhang(replacement,2026-11-05 更新)
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 CLAW 是完全端到端的自监督框架,直接从无动作视频联合学习世界模型与连续隐动作表示:对抗隐变量正则阻止隐变量编码未来观测,使其捕获动作结构;扩散式世界模型把环境动力学建模为未来观测分布而非单一确定性 rollout。同时训练隐动作模型与世界模型,使其仅从视觉学会推断动作如何引起环境转移。可用于从观测模仿学习(从原始视频提取的隐动作做行为克隆)和目标导向规划(生成隐动作序列并映射为可执行动作),多种任务与本体上优于现有方法(摘要未给出具体数字)。
- 🇬🇧 CLAW is a fully end-to-end self-supervised framework that learns a world model jointly with continuous latent actions directly from action-free video: adversarial latent regularization stops the latent from encoding future observations so it captures action structure, and a diffusion-based world model models dynamics as a distribution over futures rather than a deterministic rollout. Training the latent action model and world model together lets it infer how actions induce transitions from vision alone, supporting imitation from observation (behavior cloning on latent actions from raw video) and goal-directed planning (latent action sequences mapped to executable actions), outperforming existing methods across tasks and embodiments; no figures are in the abstract.

### [Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning (TT-MBRL)](https://arxiv.org/abs/2611.09625) — 作者:Maxime Burchi, Fayaz Ali Dharejo, Radu Timofte
🏷️ 交叉方向 / Also: 强化学习(模型型 RL,非机器人控制主线)
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 模型型 RL 的世界模型在需要长期记忆与规划的任务上仍难超越人类。TT-MBRL 不改架构,而是在测试时用梯度下降把本回合观测记忆编码进世界模型参数,让智能体为每个回合学习独立世界模型。先在简化的二维 Memory Maze 2D 上验证对不同世界模型架构的一致提升,再在 3D Memory Maze 基准上取得新的最优结果,并在 DeepMind Control 与 Atari 100k 等非记忆基准上保持强性能;摘要未给出具体数值。
- 🇬🇧 World models in model-based RL still struggle to beat humans on tasks needing long-term memory and planning. TT-MBRL moves beyond architecture design by using gradient descent at test time to encode an episode's observation memory into world-model parameters, learning a distinct world model per episode. It shows consistent gains across architectures on a simplified Memory Maze 2D, new state-of-the-art results on the 3D Memory Maze benchmark, and maintained performance on DeepMind Control and Atari 100k; no numbers are given in the abstract.

### [VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding](https://arxiv.org/abs/2611.08449) — 作者:Yu-Cheng Chou, Shihao Wang, Jin Huang, Chi-Pin Huang 等(HF Daily Papers 109 赞)
🏷️ 交叉方向 / Also: 空间智能(视觉规划:点、框、轨迹)、具身智能
开源状态 / Code: ❓ 未知 / Unknown — HF 无 githubRepo,摘要与 Comments 无链接。
- 🇨🇳 物理 AI 模型可用点、边框、轨迹等视觉规划表示空间目标,但自回归 VLM 逐坐标 token 生成使更丰富的预测代价越来越高。VFlash(Flash Primitive Decoding)利用视觉基元的已知结构,用轻量 drafter 一次前向联合预测整个基元,布局随基元类型、维度和长度自适应,并在标注基元上直接训练、无需目标 token 一致即可接受结构合法的预测。在 2D/3D 机器人轨迹任务上持续降低预测误差,3D 点运动预测的初步单次 rollout 测量显示约快 25 倍;以 VFlash 规划为条件的 WAM 在四个 MolmoSpaces 任务套件上平均成功率 70.2%,基线为 62.6%。
- 🇬🇧 Physical-AI models can use visual plans (points, boxes, trajectories), but autoregressive VLMs emit one coordinate token at a time, making richer predictions costly. VFlash (Flash Primitive Decoding) exploits the known structure of visual primitives: a lightweight drafter predicts an entire primitive in one forward pass with a layout adapting to type, dimensionality and length, trained on annotated primitives and accepting structurally valid predictions without target-token agreement. It reduces prediction error on 2D and 3D robot-trajectory tasks, with preliminary single-rollout measurements indicating about 25x faster generation for 3D point motion forecasting, and a WAM conditioned on VFlash plans averages 70.2% success across four MolmoSpaces suites versus 62.6% for the baseline.

**其余条目 / Others(2):** [Pelican-Sim 1.0 仓库](https://github.com/ZouShilong1024/Pelican-Sim1.0)(通用具身世界模型模拟器,13 星,11-07 新建)、[RigidFormer](https://arxiv.org/abs/2605.09196)(mesh-free 刚体动力学学习)。共 8 条展开 + 2 条列名。

**另见 / See also:** [LeWAM / Diffusion-Steering MPC](https://arxiv.org/abs/2610.12407)(已归入 运动控制·传统)、[FATHOM](https://arxiv.org/abs/2611.08898)(已归入 运动控制·传统)、[Fast-TD-MPC](https://arxiv.org/abs/2609.32591)(已归入 运动控制·RL)、[PyRUA-DataFarm](https://arxiv.org/abs/2611.05320)(已归入 具身智能)。

---

## 空间智能与 SLAM / Spatial Intelligence & SLAM(展开 6 条 / 6 expanded)

### [BEV3SR: Evidence-Aware 3D Spatial Reasoning from Video](https://arxiv.org/abs/2611.09816) — 作者:Fan Zhu, Rui Yu(WACV camera ready)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅注明 WACV camera ready。
- 🇨🇳 视频只提供顺序、局部视角的观测,VLM 难以进行 3D 空间推理,许多问题还需在查询指定视角而非观测相机视角下回答。BEV3SR 免训练、与骨干无关,面向带相机参数的 RGB-D 视频:把观测转为可查询的度量鸟瞰(BEV)场景记忆,空间任务形式化器指定查询的参考系、空间约束、目标和证据要求;需要几何证据的查询由几何推理器在度量 BEV 记录中确定性计算,需要视觉证据的则由视觉证据对齐器检索与对象一致的 RGB 帧供 VLM 落地。在 16 帧预算内,多种 VLM 骨干在多个 3D 场景问答基准上持续提升,空间密集型问题增益大(摘要未给出具体数字)。
- 🇬🇧 Videos give sequential, view-local observations, so VLMs struggle with 3D spatial reasoning, and many questions must be answered in a query-specified viewpoint. BEV3SR is training-free and backbone-agnostic for RGB-D video with camera parameters: it builds queryable metric bird's-eye-view scene memory, a Spatial Task Formalizer specifies the query's reference frame, constraints, objective and evidence requirement, geometric queries are answered deterministically by a Geometric Reasoner on metric BEV records, and visual-evidence queries use a Visual Evidence Aligner to retrieve object-consistent RGB frames for VLM grounding. Within a 16-frame budget it improves several VLM backbones across 3D scene QA benchmarks, with large gains on spatially intensive questions and no figures in the abstract.

### [Seeing What Matters: Benchmarking Task-Conditioned Actionable Spatial Belief for Manipulation](https://arxiv.org/abs/2611.09794) — 作者:Yina Jian, Mingkun Xu
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 现有空间推理基准评估能否描述场景,而操作需要获取使当前指令可执行的特定证据。该基准在咖啡工作站、抽屉/柜子、微波炉/电器三个域的仿真桌面操作中提供 860 个冻结评估用例,两种协议(闭环可行动性与同物体功能域外泛化)下的评估者 episode 超过 11.5 万个;每个用例配有候选 RGB 视图、操作指令、脚本技能与隐藏后置条件。诊断参考流水线维护空间-功能信念并按缺失证据给视图排序,闭环 98.8%、功能域外 98.9%,消融功能或指令绑定组件后降至接近零;七个 VLM 仅 26–43%;打乱视觉分数则降到 15%/11%,证明结果依赖图像内容。真机验证仍在进行中。
- 🇬🇧 Spatial-reasoning benchmarks test whether a model can describe a scene, but manipulation needs the specific evidence that makes the current command executable. The benchmark provides 860 frozen cases across coffee-workstation, drawer/cabinet and microwave/appliance domains, over 115,000 evaluator episodes under closed-loop actionability and same-object functional-OOD protocols, each pairing candidate RGB views, a command, scripted skills and hidden postconditions. A diagnostic reference pipeline maintaining a spatial-functional belief state and ranking views by missing evidence reaches 98.8% closed-loop and 98.9% functional-OOD, collapsing to near zero when functional or command-binding parts are ablated, while seven VLMs reach only 26–43%; shuffling visual scores drops it to 15%/11%, confirming dependence on image content. Physical-robot validation is still in progress.

### [SGM-SLAM: Scene Graph Matching for Data-Efficient Distributed SLAM](https://arxiv.org/abs/2606.16881) — 作者:Yewei Huang, Tixiao Shan, Abhinav Rajvanshi, Niluthpol Chowdhury Mithun(replacement,2026-11-06 更新)
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 面向 GPS 拒止、通信受限环境下的多机器人分布式 SLAM:各机器人可能从独立初始化的局部坐标系出发,且空间重叠有限。方法用融合的 RGB-LiDAR 点云构建场景图——语义分割点云层加离散有界物体层,附带估计轨迹;机器人通过交换并匹配物体数据与邻居协同匹配场景图,并用多步数据交换与优化最大化通信效率。在轨迹重叠有限、视角变化大、重复结构和视觉退化条件下的真实数据集上验证了有效性与通信效率;摘要未给出具体数值。
- 🇬🇧 A data-efficient distributed SLAM framework for multi-robot teams in GPS-denied, communication-constrained settings where robots start from independent local frames and share limited overlap. It builds a scene graph from fused RGB-LiDAR point clouds with a semantically segmented point-cloud layer and a layer of discrete bounded objects alongside estimated trajectories, matches scene graphs collaboratively by exchanging object data with neighbors, and uses a multi-step exchange and optimization process to maximize communication efficiency. Real-world datasets with limited trajectory overlap, viewpoint variation, repeated structure and degraded visual conditions demonstrate effectiveness and communication efficiency; no numbers in the abstract.

### [When to Trust the BIM: Identifiability-Aware LiDAR-Inertial–BIM Fusion under As-Built Deviations](https://arxiv.org/abs/2611.09045) — 作者:Yujie Zhang, Yuxuan Guo, Xinbao Sun, Chunlei Zhao 等
开源状态 / Code: ❓ 未知 / Unknown。
- 🇨🇳 建筑信息模型(BIM)可为 LIO 定位提供全局几何参考,但竣工偏差使扫描与 BIM 的不一致可能来自位姿误差、墙面偏移/遮挡物或房间整体偏移,某些几何下这些解释产生相同观测。作者将其形式化为三类故障的归因问题并推导可归因的几何判据,提出可识别性感知方法:仅在可归因时报告归因,否则保留候选、推迟 BIM 更新和模糊方向上的位姿修正,待新参考出现后恢复。预注册二维研究中,在可检测但不可归因的情形下条件错误率 0.83%,同等回答率的不确定性弃权基线为 31.67%;5,600 个可归因案例中 5,574 次给出唯一归因且无错误归因;实验室和 SLABIM 三层楼的成对故障注入中零次偏离目标归因(0/168 和 0/1,302)。
- 🇬🇧 BIM can give LiDAR-inertial odometry a global reference, but as-built deviations mean a scan-BIM disagreement may stem from pose error, an offset wall or unmodeled object, or a shifted room, sometimes with identical observations. The paper formalizes this as fault identification over three classes with a geometric attributability criterion, and proposes a method that reports an attribution only when attributable, otherwise keeping candidates and deferring BIM updates and corrections in ambiguous directions until new references arrive. In a pre-registered 2D study the conditional error rate on detectable-but-unattributable cases is 0.83% versus 31.67% for an uncertainty-abstention baseline at the same answer rate; 5,574 of 5,600 attributable cases got unique attributions with no wrong ones, and paired fault injections raised no off-target attribution (0/168 in the lab, 0/1,302 on SLABIM).

### [MosaicIMU: Composing Carrier Experts for Generalizable Neural Inertial Odometry](https://arxiv.org/abs/2606.09355) — 作者:Junye Zou, Huiyi Yan, Xinning Xu, Xiaolei Li 等(replacement,2026-11-06 更新;CoRL 2026 Spotlight)
开源状态 / Code: ❓ 未知 / Unknown — Comments 仅注明 CoRL 2026 Spotlight。
- 🇨🇳 学习式惯性里程计常与特定载体绑定,难以泛化到异构平台。MosaicIMU 是载体条件的混合专家(MoE)预训练-适配框架:基于原型的路由器组合载体专属专家特征,解码局部速度与不确定性约束,并与历史感知 EKF 融合;对未见域冻结预训练基座并学习新的轻量专家残差分支,边缘部署时复用路由器选择信息量大的在线样本做增量更新。实验中持续优于学习式基线,平均 ATE 与 RTE-10s 分别降低 40% 与 34%。
- 🇬🇧 Learned inertial odometry is often tied to one carrier and generalizes poorly across platforms. MosaicIMU is a carrier-conditioned Mixture-of-Experts pretraining-and-adaptation framework: a prototype-based router composes carrier-specific expert features, decodes local velocity and uncertainty constraints, and fuses them with a history-aware EKF; for unseen domains it freezes the base and learns a lightweight expert residual branch, and for edge deployment it reuses the router to select informative online samples for incremental updates. It consistently beats learning-based baselines, reducing average ATE by 40% and RTE-10s by 34%.

### [Extended Model-Based Learned Inertial Odometry](https://arxiv.org/abs/2611.09584) — 作者:Sasanka Kuruppu Arachchige, Joni-Kristian Kämäräinen(ICUAS 2026)
开源状态 / Code: ❓ 未知 / Unknown — 摘要称 "Code, data pipeline and trained models are publicly available",但无链接,待核实。
- 🇨🇳 敏捷四旋翼飞行中仅靠积分惯性测量会因传感器误差和时变偏置产生位姿漂移,已有学习式惯性里程计对训练中未见的轨迹泛化有限。本工作采用机体系表示,并把机体系力矩动力学引入学习流水线;学习模型预测短时域相对位移,并与 IMU 测量在扩展卡尔曼滤波器中融合。在未见轨迹上的四旋翼位姿估计优于此前最先进的学习式惯性里程计;在四个公开四旋翼数据集(整条轨迹形状均不参与训练)上每个保留集的速度误差都更低,且力矩输入由旋翼信号导出时信息量最大。
- 🇬🇧 For agile quadrotor flight, integrated inertial measurements alone drift from sensor errors and time-varying biases, and prior learned inertial odometry generalizes poorly to unseen trajectories. This work uses a body-frame representation and adds body-frame torque dynamics to the learning pipeline; the learned model predicts short-horizon relative displacements that are fused with IMU data in an Extended Kalman Filter. It outperforms the previous state-of-the-art learned inertial odometry on unseen trajectories, achieves lower velocity error on every held-out set across four public quadrotor datasets with whole trajectory shapes held out, and the torque input is most informative when derived from rotor signals.

**其余条目 / Others(5):** [ABot-Recon 仓库](https://github.com/amap-cvlab/ABot-Recon)(流式 3D 重建,+18 星)、[Spatial-Forcing 仓库](https://github.com/OpenHelix-Team/Spatial-Forcing)(+23 星)、[Lightweight Path-Aware Frontier Re-ranking for LiDAR-Based UAV Exploration](https://arxiv.org/abs/2611.09561)、[EGT: Execution-Grounded Traversability](https://arxiv.org/abs/2611.09270)、[HaNDF](https://arxiv.org/abs/2611.08578)。共 6 条展开 + 5 条列名。

**另见 / See also:** [SLA](https://arxiv.org/abs/2611.08373)(已归入 VLA)、[VFlash](https://arxiv.org/abs/2611.08449)(已归入 世界模型与 WAM)、[VLD](https://arxiv.org/abs/2512.07976)(已归入 运动控制·RL)。

---

## 其他值得关注 / Other Notable

仿真器与基础设施(非控制贡献,故未归入运动控制;均以训练 RL/轨迹优化为目标):
- [Lodos](https://arxiv.org/abs/2611.08872) / [Lodos-v2](https://arxiv.org/abs/2611.08868)(Onur Beker, Andreas René Geist, Georg Martius):GPU 大规模并行刚体仿真器,专攻大量精细网格的接触;摘要称物理保真度与成熟仿真器相当,在精细网格碰撞场景吞吐约高一个数量级;v2 提出求解精确摩擦接触的原始形式算法。开源状态:✅ [代码仓库](https://github.com/martius-lab/lodos)(摘要给出,匿名验证存在)。🏷️ 交叉方向:运动控制·RL(仿真基础设施)。
- [RevoSim](https://arxiv.org/abs/2611.08939):BrainCo Revo3 灵巧手的多模态触觉仿真(285 个压阻触点 + 5 个视触觉指尖),单张 RTX 5090 最高支持 4,096 并行环境,在仿真中训练了手内操作与抓取策略。开源状态:❓ 未知(有[项目页](https://braincotech.github.io/RevoSim-web/))。🏷️ 交叉方向:运动控制·RL(仅仿真,未做 sim-to-real,故未归入)。
- 其余列名(10):[RigidFormer](https://arxiv.org/abs/2605.09196)、[The effect of limb kinematics on the speed of a legged robot on granular media](https://arxiv.org/abs/1303.7276)(2013 年论文的 replacement,无实质新内容)、[Multi-bounce Drum Roll](https://arxiv.org/abs/2609.08490)、[Evolving Drone Morphologies for Agile Flight](https://arxiv.org/abs/2502.01197)、[Spectral Alignment in Forward-Backward Representations](https://arxiv.org/abs/2603.20103)(NeurIPS 2026,[代码](https://erfi.github.io/spectral_alignment/))、[DexTeleop-0](https://arxiv.org/abs/2606.23431)、[Safe Circumnavigation (HOCBF-QP)](https://arxiv.org/abs/2611.09112)、[TPS-A*](https://arxiv.org/abs/2611.09210)、[Auditing Grasp Feasibility Predictors](https://arxiv.org/abs/2611.09130)、[Behavior Graphs](https://arxiv.org/abs/2611.00405)。
- 本窗口 cs.RO 列表中另有约 40 条与关注主题无关(医疗/软体机器人、农业感知、交通与自动驾驶治理、传感器标定等),已逐条分类为不相关,不列出。 / About 40 further cs.RO entries (medical/soft robots, agricultural perception, AV governance, sensor calibration, etc.) were classified as not relevant.

---

## GitHub 动态 / GitHub Highlights

### star 增长明显的仓库 / Star growth(相对前一日快照)

| 仓库 | 星数 | Δ | 说明 |
|---|---|---|---|
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 16,886 | +509 | 通用物理仿真器,单日增幅最大(原因未明,同日其 playground 发布 v1.0.1)。 / Largest one-day jump; reason unclear. |
| [dexmal/opendm](https://github.com/dexmal/opendm) | 2,442 | +51 | 通用具身智能开放世界基础模型。 / Open-world foundation model for embodied AI. |
| [OpenHelix-Team/Spatial-Forcing](https://github.com/OpenHelix-Team/Spatial-Forcing) | 391 | +23 | SLA 与 Spatial Forcing(ICLR 2026)官方实现;SLA 今日 arXiv 上线。 / Official code for SLA and Spatial Forcing. |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 14,599 | +22 | π0 / π0.5 开源实现。 |
| [groundingpi/GroundingPI](https://github.com/groundingpi/GroundingPI) | 415 | +21 | 4B 物理智能 grounding 基础模型。 |
| [amap-cvlab/ABot-Recon](https://github.com/amap-cvlab/ABot-Recon) | 1,441 | +18 | 仅视频输入的流式 3D 重建。 |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28,774 | +16 | LeRobot 端到端机器人学习。 |
| [newton-physics/newton](https://github.com/newton-physics/newton) | 5,921 | +15 | 基于 NVIDIA Warp 的 GPU 物理引擎。 |
| [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) | 556 | +14 | SuperMimic 第三方实现/资源合集(非官方)。 / Third-party collection, not official. |
| [nv-tlabs/lyra](https://github.com/nv-tlabs/lyra) | 2,851 | +13 | 开放生成式 3D 世界模型。 |
| [fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic) | 200 | +12 | Unitree G1 全身动作跟踪,单 GPU 约 3 分钟;topics 含 supermimic、world-model、mjlab(第三方,2026-11-02 新建)。 |
| [mujocolab/mjlab](https://github.com/mujocolab/mjlab) | 3,361 | +10 | 基于 MuJoCo-Warp 的 Isaac Lab API,面向 RL 与机器人研究。 |
| [NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) | 8,338 | +8 | GR00T N1.7。 |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 8,603 | +6 | 统一机器人学习框架。 |

(radar 中 ruvnet/RuView、bilawalsidhu/gods-eye-view 等高增长仓库与机器人/具身无直接关系,已忽略。)

### 值得关注的新仓库 / Notable new repos
- [YeWR/EPO](https://github.com/YeWR/EPO)(2026-11-08 新建,3 星)— Energy-Based Policy Orchestration(CoRL 2026):Unitree G1 目标条件全身控制策略、能量模型与能量训练代码,属运动控制·RL;昨日报告已提及。
- [Robbyant/lingbot-touch](https://github.com/Robbyant/lingbot-touch)(8 星)— 面向通用灵巧操作的异构触觉表征学习。 / Heterogeneous tactile representation learning for dexterous manipulation.
- [ZouShilong1024/Pelican-Sim1.0](https://github.com/ZouShilong1024/Pelican-Sim1.0)(13 星)— 具身智能通用世界模型模拟器。
- [jushengzhang/robot-weight-debugging](https://github.com/jushengzhang/robot-weight-debugging)(2 星)— [Can LLMs Debug Robots by Editing Their Weights?](https://arxiv.org/abs/2611.09376) 的首发代码(65 行编辑、16 个实验日志),作者账号下新建,对应关系明确,可视为该论文已开源。
- 另有若干个人项目(locomotion 学习实验、G1 devkit 等)均 ≤ 5 星且无明确对应论文,已略过。

### 新 release / New releases(窗口内)
- **[google-deepmind/mujoco_playground v1.0.1](https://github.com/google-deepmind/mujoco_playground/releases/tag/v1.0.1)**(2026-11-09T05:16Z)— release body 仅指向 [changelog](https://reaf-sim.readthedocs.io/en/v1.0.1/playground/changelog.html)。v1.0.1(11-08)主要更新:`SO101Follower` / `YamFollower` / `BodyTrackingDevice` 改用 `get_measurements`;`RslRlVecEnvWrappercfg.is_finite_horizon` 默认改为 `False`(启用超时 bootstrap);`MotionReferenceProducer` 与 `SmoothCartesianIKProcessor` 的状态推进移到 `on_step` / `on_begin_stepping` 以处理部分重置;恢复 `uv.lock` 中 Linux CUDA 13 PyTorch 运行时依赖(issue #382)。上一版 v1.0.0(11-06)基于 `reaf-sim` 与 MuJoCo Warp 重建,采用声明式 `flat_scene` 环境,新增 SO-101 / YAM / Trossen WXAI / Unitree G1 的 `sim/` 与 `real/` 配对机器人包,并加入 RSL-RL 训练、遥操作、`mujoco.sysid` 与 sim-to-real 部署。
- [Genesis v1.4.6](https://github.com/Genesis-Embodied-AI/genesis-world/releases/tag/v1.4.6) 发布于 2026-11-08T21:56Z,早于本窗口,昨日报告已覆盖(非刚体求解器 FEM/MPM/PBD 打磨、可微仿真原生兼容 torch 且约快 3 倍)。

---

## 今日趋势 / Today's Trends

1. **人形全身控制:模型 + 残差 RL 与力感知。** DKWBC 用逆动力学前馈加残差 RL 平衡策略、ForPC 用无力传感器的力隐变量残差策略做推车、SUGARv2 用合成参考与统一模仿奖励训练视觉 loco-manipulation、STRIDE 只用 IMU 加速度奖励在分钟级学会行走,共同指向"减少任务专属奖励/传感器依赖"。GitHub 侧 EPO、blinkmimic 与 SuperMimic 第三方复现也在跟进。 / Humanoid whole-body control is converging on model-plus-residual-RL, force-aware latents and unified imitation rewards that reduce task-specific rewards and sensors (DKWBC, ForPC, SUGARv2, STRIDE; EPO and blinkmimic on GitHub).
2. **WAM 走向"免想象"与表征蒸馏。** DreamFree、FRED、WorldBridge、MDF++ 都在改善 WAM 的未来表征质量并避开昂贵的视频生成,DreamFree 以 14B 骨干实现 11 Hz;Open-HumanWAM 则以 5 万小时人类视频给出缩放律与全开源配方。 / WAMs are moving toward imagination-free control and representation distillation (DreamFree, FRED, WorldBridge, MDF++), while Open-HumanWAM provides a scaling law and a fully open recipe.
3. **编码智能体/通用智能体直接控制机器人。** AMP1(RoboLab-120 零样本 85.6%)、Computer-Use Agents Are Embodied Generalists、PyRUA-REAL / DataFarm 与 Controlled Study 都在把通用模型当作"操作策略"或"数据生产者",并报告对 VLA/WAM 的优势或成本优势。 / General and coding agents are being used directly as manipulation policies or data producers (AMP1, CUA, PyRUA-REAL/DataFarm, the Controlled Study).
4. **VLA 的效率、记忆与连续性。** ActPrune(剪枝)、VLA Handover(端云切换)、ODEAction(无分块)、SURE(不确定性监督)、HeLM / HiMEM(记忆)说明 VLA 研究重心从"更大"转向部署可行性与时序一致性。 / VLA research is shifting from scale to deployability and temporal consistency (ActPrune, VLA Handover, ODEAction, SURE, HeLM/HiMEM).
5. **仿真基础设施继续升级。** mujoco_playground v1.0.1 / v1.0.0(reaf-sim + MuJoCo Warp)、Genesis v1.4.6、Lodos 系列与 RevoSim 都面向更高吞吐的并行仿真与 sim-to-real 部署。 / Simulation infrastructure keeps scaling (mujoco_playground, Genesis, Lodos, RevoSim).

---

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
- `agentic manipulation` / `coding agent robot` / `code-as-policy`(适用:arXiv 检索 + GitHub 关键词)— 今日至少 5 篇相关工作以通用/编码智能体直接指挥或改进机器人,现有关键词覆盖不到。 / At least five papers today treat general or coding agents as robot policies, which current keywords miss. 证据:[AMP1](https://arxiv.org/abs/2611.09892)、[PyRUA-REAL](https://arxiv.org/abs/2611.06768)、[PyRUA-DataFarm](https://arxiv.org/abs/2611.05320)、[Controlled Study](https://arxiv.org/abs/2611.09030)、[CUA Embodied](https://arxiv.org/abs/2611.09847);GitHub 侧 [PyRUA-Lean](https://github.com/DAGroup-PKU/PyRUA-Lean) 星数增长中。
- `inertial odometry`(适用:arXiv 检索)— 同一天出现 3 篇学习式惯性里程计/状态估计相关论文,属 SLAM 邻域但未被现有 SLAM 关键词命中。 / Three learned inertial-odometry papers today sit next to SLAM but escape current SLAM keywords. 证据:[MosaicIMU](https://arxiv.org/abs/2606.09355)、[Extended Model-Based Learned Inertial Odometry](https://arxiv.org/abs/2611.09584)、[BIM-LIO fusion](https://arxiv.org/abs/2611.09045)。

**建议观察 / Watch**
- `imagination-free WAM` / `future representation distillation`(适用:arXiv 检索)— 信号尚弱但 3 篇同期工作共享这一思路,值得再观察几天。 / Three concurrent papers share this idea but the signal is still young. 证据:[DreamFree](https://arxiv.org/abs/2611.04527)、[FRED](https://arxiv.org/abs/2610.30320)、[VFlash](https://arxiv.org/abs/2611.08449)。

**建议移除/收窄 / Remove or Narrow:** 今日无建议 / No suggestions today.(备注:`reinforcement learning robot` 作为短语检索在窗口内命中为 0,建议改为 `reinforcement learning` AND `humanoid|legged|manipulation` 的布尔组合,以免漏检;证据为本次检索输出。 / The phrase query returned 0 hits; consider a boolean combination.)

---

## 开源监测 / OSS Watchlist

| 工作名称 | 加入日期 | 当前状态 | 今日检查结果 | 备注 |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 | signal=false;candidate_repos、project_page_github_links、project_page_release_claims、arxiv_github_links 均为空;errors 为空;arXiv 最新版 v1。匿名 `git ls-remote` 检查 qiayuanl/SuperMimic、HybridRobotics/SuperMimic、HybridRobotics/supermimic 均不存在。 | 状态不变。search_hits 中全是第三方复现/笔记(如 A100Supermimic、awesome-supermimic 等),按规则不能据此判定已开源。 |

**🔔 监测项已开源:** 今日无。 / None today.

**建议加入监测 / Suggested additions**(均为运动控制类,状态为"计划开源/未知"):
1. **ForPC** — 🕒 项目页明确 "Code coming soon",人形推车全身控制 RL 且已 sim-to-real,值得追踪代码发布。 / Project page says code is coming soon; a humanoid RL whole-body controller with real G1 transfer.
2. **SUGARv2** — 🕒 项目页 "Code (Coming Soon)",视觉人形 loco-manipulation,仿真 91.0% 并上真机。 / Code coming soon; visual humanoid loco-manipulation with real deployment.
3. **STRIDE** — ❓ 无任何代码信息,但"分钟级学会人形行走"的实用价值高。 / No code information, but minutes-scale humanoid learning is high-value.

可直接粘贴进 oss_watchlist.json 的条目:
```json
{
  "name": "ForPC",
  "title": "ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing",
  "arxiv_id": "2611.08664",
  "added": "2026-11-10",
  "status": "planned",
  "search_terms": ["ForPC", "humanoid cart pushing"],
  "owners": [],
  "project_pages": ["https://roboforpc.github.io/"],
  "known_repos": []
},
{
  "name": "SUGARv2",
  "title": "SUGARv2: Learning Diverse Visual Humanoid Loco-Manipulation Skills from Synthesized Interaction References",
  "arxiv_id": "2611.09266",
  "added": "2026-11-10",
  "status": "planned",
  "search_terms": ["SUGARv2", "SUGAR humanoid"],
  "owners": [],
  "project_pages": ["https://tianshuwu.github.io/sugarv2-humanoid/"],
  "known_repos": []
},
{
  "name": "STRIDE",
  "title": "STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards",
  "arxiv_id": "2611.08857",
  "added": "2026-11-10",
  "status": "unknown",
  "search_terms": ["STRIDE humanoid locomotion", "acceleration-based rewards"],
  "owners": [],
  "project_pages": [],
  "known_repos": []
}
```

**建议移出 / Suggested removals:** 无(SuperMimic 仍未开源)。 / None.

---

*自检 / Self-check:* ① 运动控制 RL(14)与传统(8)均已完整展开;② 未使用"未读/仅标题"类占位;③ 每条均有开源状态行;④ 已逐条复查类别 3–7:CS-Pi、Horizon-Coupled 为模仿学习策略的推理期约束,已在 RL 类末尾「另见」说明并保留于具身智能;DexHOT 摘要未提及 RL,保留于具身智能并注明交叉;DreamFree、FRED 等 WAM 以操作策略为主,未涉人形/足式控制;VLD、Fast-TD-MPC、FASTFUNNELS、LeWAM、FATHOM、CompVLA 已移入运动控制类;⑤ arXiv API 关键词检索已运行并记录命中数;⑥ release 已写主要更新;⑦ 链接格式脚本扫描见提交前检查。
