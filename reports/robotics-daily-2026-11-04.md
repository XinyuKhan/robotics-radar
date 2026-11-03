# 机器人/具身智能每日速递 — 2026-11-04 / Robotics & Embodied AI Daily — 2026-11-04
> **检查窗口 / Window**:台北时间 2026-11-03 07:40 → 2026-11-04 07:40(UTC+8,周二)。arXiv 取最新一期 cs.RO new 列表;radar 数据 `date_taipei = 2026-11-04`(已更新)。
> **监测项状态 / Watchlist**:SuperMimic 今日 `signal=false`,未发现官方代码。

## 来源状态 / Source Status

| 来源 / Source | 状态 / Status |
|---|---|
| arXiv cs.RO new 列表 | ✅ 成功:New 129 + Cross-lists 20 = 149 条已逐条分类;Replacements 69 条仅扫描标题,按规则只看与主题相关且有实质更新者(无法从标题判断实质更新,未展开) |
| arXiv API 取摘要/Comments | ✅ 89 篇相关候选全部取得非空完整摘要(89/89);其中 61 篇有 Comments |
| arXiv API 关键词检索(cs.RO/AI/LG/CV,submittedDate 2026-11-01 18:00 UTC 之后) | ✅ 已运行,命中数:embodied 8, VLA 6, vision-language-action 7, VLN 0, vision-language navigation 0, humanoid 9, legged locomotion 0, whole-body control 2, MPC 2, reinforcement learning robot 0, sim-to-real 6, dexterous manipulation 1, robot foundation model 1, world model 12, world action model 3, WAM 3, video world model 2, spatial intelligence 0, spatial reasoning 1, SLAM 1, visual SLAM 0, LiDAR SLAM 0, gaussian splatting SLAM 0, 3D reconstruction 3, motion tracking 1, motion imitation 0;合计去重 50 条,其中不在 cs.RO 列表中、与主题相关并入选的有 AgiWorld、Gnomon4D、History Forcing、OctreeSplat、LieVLM 等。注:API 索引最新的论文提交时间约为 2026-11-02 19:00 UTC,窗口内更晚提交要到下一期列表才可见 |
| GitHub radar(`data/latest.json`) | ✅ new_repos 150 条(counts 显示共 263 条新仓库,JSON 内保留 150)、star_growth_top 60 条;watchlist_releases 为 0(窗口内无 release);star 基准 2026-11-02T23:13Z 已建立 |
| Hugging Face Daily Papers API | ❌ 失败:返回 IP 限流(rate limit,需 HF_TOKEN),本期未使用 HF githubRepo 字段,开源状态仅依据 Comments、摘要全文、radar 与 git ls-remote |
| 仓库推送权限 | ✅ `git push --dry-run` 通过 |
| 入选篇数 | 89 篇相关候选;详细展开 71 篇(运动控制·RL 26 + 运动控制·传统 9 + 其余各类 36),其余列名 |

## 今日必读 / Top Picks

1. **[Anchor 1](https://arxiv.org/abs/2611.00193)** — ❓ 未知 — 运动控制·RL:人形全身操作控制器,真机最严格评分下跟踪误差降低 30%–80%,并附基准。 / Humanoid whole-body manipulation controller with 30%–80% lower real-world tracking error plus a benchmark.
2. **[MAPO](https://arxiv.org/abs/2611.02613)** — ❓ 未知 — 运动控制·RL:指出 MoE 策略梯度中散度误估问题,可多跟踪 182 条 PPO+MoE 失败的动作。 / Identifies divergence misestimation in MoE policy gradients; tracks 182 motions PPO+MoE fails on.
3. **[ReGATE](https://arxiv.org/abs/2611.02871)** — ❓ 未知 — 运动控制·RL:循环门控视觉融合的人形 loco-manipulation,静态物体抓取 85.2% 对 VisualMimic 48.5%,Unitree G1 真机。 / Recurrent gated visual fusion for humanoid loco-manipulation: 85.2% vs 48.5% (VisualMimic), real G1.
4. **[Why Koopman Structure Does Not Help Differentiable World Models for Humanoid Whole-Body Tracking](https://arxiv.org/abs/2611.00951)** — ❓ 未知 — 运动控制·RL(SuperMimic 相关,监测项的直接后续负面结果)。 / A clear negative result on SuperMimic-style differentiable world models.
5. **[OpenNWM](https://arxiv.org/abs/2611.01844)** — ✅ 已开源 — 世界模型与 WAM:1750 万观测的无动作视频潜在动作预训练,代码与项目页均已公开。 / Latent-action pretraining on 17.5M action-free observations; code released.

## 运动控制·RL / Motion Control · RL (共 26 条,全部展开)

说明:本类包含人形/足式全身控制、动作跟踪、RL 控制策略与操作控制策略,同时涉及世界模型、VLA 等的控制类工作按规则归入此类。

#### [Anchor 1: Precise and Stable Humanoid Control for Whole-Body Manipulation](https://arxiv.org/abs/2611.00193)
作者 / Authors: Archon Robotics 等(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 摘要与 Comments 均无代码链接

🇨🇳 人形全身控制器已具备多样技能,但用于全身操作时,小的执行偏差或多余的步伐就会导致失败。Anchor 1 用校准过的稀疏动作参考(无需在线关节空间重定向)保留任务相关的人体动作结构,并通过离线筛选机器人动作与稀疏参考配对来塑造训练分布,同时引入与动作编码解耦的显式误差反馈。同时提出一个评测精度、持续稳定性与可达性的基准。在最严格的真机全局评分设置下,跟踪误差相比所有现有控制器降低 30%–80%,且所需前瞻输入更少、无需重定向;下游实验显示遥操作数据采集更高效、任务成功率更高。

🇬🇧 Humanoid controllers have many motor skills, but whole-body manipulation is brittle: small deviations or unintended steps cause failure. Anchor 1 uses calibrated sparse motion references (no online joint-space retargeting), offline curation of robot motions paired with those references to shape the training distribution, and explicit error feedback decoupled from motion encoding; a benchmark for precision, sustained stability and reachability is also introduced. Under the strictest real-world global scoring, it cuts tracking error by 30%–80% versus all existing controllers with fewer look-ahead inputs and no retargeting, and downstream tests show more efficient teleoperated data collection and higher task success.

#### [MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking](https://arxiv.org/abs/2611.02613)
作者 / Authors: Seonghyeon Lim, Hyeonwoo Lee, Mincheol Kim, Kimin Lee 等(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 摘要给出项目页 [项目页](https://mapo-corl2026.github.io/MAPO/),未见代码声明(CoRL 2026)

🇨🇳 通用人形动作跟踪常用混合专家(MoE)策略,但作者发现 MoE 的动态路由会使策略梯度更新中新旧策略的散度被错误估计,导致更新过于保守或过大、策略次优。MAPO 交替优化路由器与专家,以避免散度误估。MAPO 能跟踪 182 条 PPO+MoE 无法跟踪的动作,而 PPO+MoE 仅比 MAPO 多跟踪 1 条;在对比方法中跟踪成功率最高,且多数误差指标最低。

🇬🇧 Universal humanoid motion tracking often uses mixture-of-experts policies, but dynamic routing causes the divergence between old and updated policies to be misestimated in policy-gradient updates, giving overly conservative or excessively large updates. MAPO alternately optimizes the router and the experts to avoid this misestimation. It tracks 182 motions that PPO with MoE fails on (PPO+MoE tracks only one that MAPO fails), and achieves the highest tracking success rate and the lowest error on most metrics among compared methods.

#### [ReGATE: Recurrent Gated Visual Fusion for Reactive Humanoid-Object Interaction](https://arxiv.org/abs/2611.02871)
作者 / Authors: Hao Zhu, Jorge Peña-Queralta(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 无链接,无开源声明

🇨🇳 人形 loco-manipulation 需要在不完整视觉观测下完成抓取、搬运与释放并响应用户指令。ReGATE 是基于 teacher-student 的全身控制器,融合第一视角深度、本体感知与在线 locomotion/接触指令,用循环适配器在无外部物体位姿估计器的情况下预测物体几何与接触,并用分头/全局门控调节视觉更新,配合视觉落地与损坏课程及阶段感知初始化训练。仿真中 330 次静态物体抓取成功率 85.2%(VisualMimic 为 48.5%),440 次移动物体抓取为 85.9%;在 Unitree G1 上完成指令式抓取-搬运-释放,并在相机被遮挡的情况下仍成功取箱(定性)。

🇬🇧 Humanoid loco-manipulation must acquire, transport and release objects under incomplete visual observations while following commands. ReGATE is a teacher-student whole-body controller fusing egocentric depth, proprioception and online locomotion/contact commands, with a recurrent adapter that predicts object geometry and contact without an external pose estimator, head-wise/global gates, and a grounding-and-corruption curriculum. In simulation it reaches 85.2% over 330 static-object trials (VisualMimic: 48.5%) and 85.9% over 440 moving-object trials; on a Unitree G1 it performs commanded grasp-transport-release and a qualitative box acquisition with the camera occluded.

#### [CompliantBot: Learning Whole-Body Compliance across Task Interfaces for Humanoid Control](https://arxiv.org/abs/2611.01748)
作者 / Authors: Haoyang Li, Keqi Zhu, Zhanxiang Cao, Yang Zhang(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — Comments 仅为页数,无代码链接

🇨🇳 人形控制器需要在受外力时顺应、撤力后恢复任务,但跟踪目标会惩罚顺应所需的偏差,且已有方法依赖特定交互接口或预先构造的顺应数据。CompliantBot 用状态相关的交互力场耦合外加载荷与机器人运动,配合降低交互力的奖励,并在受力期间降权任务奖励、撤力后恢复,适用于动作跟踪与速度指令 locomotion,无需预构造数据且不需显式力测量。在两种任务接口下,其在恒力牵拉下顺应距离更远、弹簧交互载荷更低,撤力后能恢复跟踪,强拉下任务完成率最高、平均关节机械功率最低;真机展示了通过手臂、迈步和身体转向的顺应响应。

🇬🇧 Humanoids must yield to external forces yet resume their task, but tracking objectives penalize the deviations needed for yielding and prior work depends on task-specific interfaces or constructed compliant data. CompliantBot couples applied loads to motion via a state-dependent interaction force field plus a force-magnitude reward, downweighting task rewards during loading and restoring them after release, for both motion tracking and velocity-command locomotion, without compliant data or force sensing. It yields farther under constant pulls with lower spring loads, resumes tracking after release, achieves the highest completion under stronger pulls and the lowest mean joint power; real-robot demos show compliance via arm motion, stepping and reorientation.

#### [HuG: Learning Humanoid Whole-Body Affordance-Aware Grasping with Active Perception](https://arxiv.org/abs/2611.01659)
作者 / Authors: Xuanbin Peng, Lai Wei, Yuze Zhai, Qingyuan Yu(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 提供项目页 [项目页](https://xuanbinpeng.com/hug)(CoRL 2026),未见代码声明

🇨🇳 人形在第一视角下目标常被遮挡,且抓取需要在保持浮动基座稳定的同时协调全身。HuG 的 Perceive-Align-Grasp 流程:基于信念的主动感知把视角作为决策变量,点云条件的 affordance 策略提出全身抓取,再做 affordance 对齐调整身体姿态;关键是用控制器在环的动力学仿真筛选训练数据,剔除 73% 运动学可行但会使部署控制器失稳的抓取。完全仿真训练、零真机演示,多层货架任务真机成功率 87.5%,可泛化到新物体且各测试高度成功率不低于 73%,并能外推到训练中未见的更低桌高。

🇬🇧 Humanoids face occluded targets from egocentric views and must coordinate the whole body while keeping a floating base stable. HuG's Perceive-Align-Grasp pipeline uses belief-driven active perception (viewpoint as a decision variable), a point-cloud-conditioned affordance policy for whole-body grasps, and an alignment stage; training data are curated with controller-in-the-loop dynamics simulation, rejecting 73% of kinematically valid grasps that would destabilize the controller. Trained entirely in simulation with no real demonstrations, it reaches 87.5% real-world success on a multi-level shelf task, generalizes to novel objects, stays at least 73% at every tested height, and extrapolates to lower table heights.

#### [Learning Agile Humanoid Dodgeball with Onboard Monocular Vision](https://arxiv.org/abs/2611.01197)
作者 / Authors: Feng Tian, Yulin An, Chenhao Li, Matthias Heyrman(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — Comments 仅为投稿信息(ICRA 2027),无代码链接

🇨🇳 人形需要在保持平衡的同时对快速逼近的物体作出反应。系统集成机载单目感知(球检测器的边界框历史 → 时序估计球相对位置与威胁标志)与学习的全身控制,闪避/恢复与搜索/跟踪两套策略共享接口并组合;三阶段课程先用特权球状态训练控制,再引入估计器监督,最后把策略的特权输入替换为估计输出,并用解析投影与感知随机化免去图像渲染。仿真中每种速度-距离条件 1000 次投掷:5.0 m、6 m/s 的闪避成功率 97.8–100.0%,2.5 m、10 m/s 为 33.2–40.8%;Unitree G1 上单次受控投掷成功率超过 85%(15 次以上试验),并展示了闪避后全方位重新锁定目标。

🇬🇧 Humanoids must react to fast-approaching objects while staying balanced. The system couples onboard monocular perception (bounding-box histories → temporal estimator of relative ball position and a threat flag) with learned whole-body control; dodge/recovery and search/track policies share an interface, and a three-stage curriculum moves from privileged ball states to estimator outputs, with analytic projection and perception randomization replacing image rendering. In simulation (1000 throws per condition) dodge success is 97.8–100.0% for 5.0 m launches at 6 m/s and 33.2–40.8% for 2.5 m launches at 10 m/s; on a physical Unitree G1, controlled single-throw success exceeds 85% over more than 15 trials, with full-azimuth target reacquisition demonstrated.

#### [ReContact: Reconstruct and Retarget Human Contacts from Video for Contact-Rich Humanoid Manipulation](https://arxiv.org/abs/2611.02968)
作者 / Authors: Zhongkai Gu, Yang Liu, Wei Zhu, Mitsuhiro Hayashibe(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 无链接,无开源声明

🇨🇳 人类视频是学习全身接触转换的可扩展数据源,但遮挡会破坏物体位姿跟踪,且复现物体轨迹并不保证机器人在预期接触点施加稳定的力。ReContact 通过以物体为中心的接触计划(接触阶段、接触对、锚点、按压方向、粘滑模式)重建并重定向人-物交互,用接触先验稳定遮挡下的位姿重建,并在冻结的全身跟踪器之上训练残差策略,奖励在计划锚点以对齐方向施力。仿真中大腿支撑再抓取任务达成计划双掌托底的比例为 83.5(摘要原文单位如此),最佳改造基线为 0.16%;一个基于 247 条参考训练的策略重新求解新放置后,工作空间内管件传递成功率从 20.4% 升至 97.8%;真机 Unitree G1 上执行 7 个接触丰富的操作和 2 个 loco-manipulation 任务。

🇬🇧 Human videos are a scalable source of whole-body contact transitions, but occlusion corrupts object pose tracking and reproducing the object trajectory does not ensure stabilizing forces at the intended contacts. ReContact reconstructs and retargets human-object interactions via an object-centric contact plan (phases, pairs, anchors, pressing directions, stick/slide modes), uses contact priors to stabilize pose reconstruction, and trains a residual policy on a frozen whole-body tracker rewarded for contacts at planned anchors with aligned forces. In simulation the planned two-palm bottom hold is achieved in 83.5 of episodes (as written in the abstract) versus 0.16% for the best adapted baseline; one policy trained on 247 references raises in-workspace tube-transfer success from 20.4% to 97.8%; on a real Unitree G1 it executes seven contact-rich manipulation and two loco-manipulation tasks.

#### [Why Koopman Structure Does Not Help Differentiable World Models for Humanoid Whole-Body Tracking](https://arxiv.org/abs/2611.00951)
作者 / Authors: Haizhou Ge, Mengshuo Wang, Yufei Jia, Lei Han(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 世界模型 / World Model(SuperMimic 相关)

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 在 SuperMimic 式「反向传播穿过可微世界模型训练人形全身跟踪策略」的流程中,检验 Koopman(提升状态空间线性动力学)结构是否有益。结论为否:仿真 Unitree G1 上回报至多持平(0.823 对 0.830),同数据单步误差为 MLP 的 1.3–1.6 倍,训练约慢 15%;提升空间的滚动要么发散要么无法训练出策略,每个想象步重新提升效果最好。作者进一步解释:动作仿射模型只在策略动作处的切线上准确(G1 上该处与 MLP 一样准,在平均动作处差 31 倍),把策略动作输入偏移项能消除大部分差距,故 MLP 世界模型仍是更好选择。

🇬🇧 In a SuperMimic-style pipeline that trains a humanoid whole-body tracking policy by backpropagating through a differentiable world model, the paper tests whether Koopman structure helps. It does not: on simulated Unitree G1, return is at best equal (0.823 vs 0.830), one-step error is 1.3–1.6x the MLP's, training is ~15% slower, and lifted rollouts diverge or fail to train a policy (re-lifting at every imagined step works best). The authors explain that an action-affine model is accurate only as the tangent at the policy's operating point (on G1 equal to the MLP there, 31x worse at the mean action), and supplying the policy's action removes most of the gap, so the MLP world model remains the better choice.

#### [ODE Policy: Robot Learning via Action Dynamics, Not Actions](https://arxiv.org/abs/2611.01729)
作者 / Authors: Jindou Jia, Jingliang Li, Kuangji Zuo, Tuo An 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: VLA / 世界动作模型 WAM

开源状态 / Code: ❓ 未知 / Unknown — 无链接,无开源声明(35 页)

🇨🇳 多数 IL/RL 策略把观测映射为离散步的动作值,动作连续性只能隐式学习。ODE Policy 学习「动作的动力学」:神经 ODE 学习动作向量场,在 IL 中匹配短动作块、在 RL 中匹配单步,轻量多样性头捕获多模态,部署时从上一动作积分,轨迹天然连续;可作为视觉运动策略、VLA/WAM 的动作头或基于模型 RL 的 actor。IL 中相对 flow matching,一个 epoch 后成功率 5.9 倍、泛化 5.4 倍、模式平衡 3.9 倍,动作生成快 10.8 倍;14 个真机任务(单臂、双臂、灵巧手、人形)成功率最高;在 RL 中进一步加速 SuperMimic 人形动作跟踪并使动作更平滑。

🇬🇧 Most IL/RL policies map observations to action values per step and learn motion continuity only implicitly. ODE Policy learns the dynamics of the action: a neural ODE learns the action vector field (matched over short chunks in IL, single steps in RL) with a lightweight diversity head, and each action is integrated from the previous one so trajectories are continuous by construction; it serves as a visuomotor policy, a VLA/WAM action head, or a model-based RL actor. Versus flow matching in IL it reaches 5.9x success, 5.4x generalization, 3.9x mode balance after one epoch and generates actions 10.8x faster; it has the highest success on 14 real-world tasks across single-arm, dual-arm, dexterous and humanoid robots, and in RL it speeds up SuperMimic motion tracking and smooths actions.

#### [Energy-Based Policy Orchestration](https://arxiv.org/abs/2611.02546)
作者 / Authors: Weirui Ye, Yen-Jen Wang, Elvis Hsieh, Zhiyang Dou 等(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 摘要给出项目页 [项目页](https://yewr.github.io/epo)(CoRL 2026),未见代码声明

🇨🇳 分层控制中固定的规划器-策略接口难以应对接触、平衡与扰动的快速变化,执行时不仅要选哪个低层策略,还要选给它什么目标。EPO 为每个目标条件策略学习关于低层目标的复合能量(能量越低越可行、目标实现越准),运行时细化各策略目标并执行能量最低的「策略-目标」对;新策略只需学习自己的能量模型,无需重训已有策略。仿真中改善精度-鲁棒性权衡,并在真实人形 loco-manipulation 任务上以同一组冻结策略和能量模型完成 sim-to-real 部署(摘要未给出具体数值)。

🇬🇧 Hierarchical control with a fixed planner-to-policy interface fails when contacts, balance or disturbances evolve faster than high-level updates; execution must choose both which low-level policy to run and which goal to give it. EPO learns, per goal-conditioned policy, a composite energy over low-level goals (lower = more feasible and accurate), refines each policy's goal at runtime and executes the lowest-energy policy-goal pair; new policies add their own energy models without retraining others. It improves the precision-robustness trade-off in simulation and deploys the same frozen policies and energy models on real humanoid loco-manipulation (the abstract gives no numbers).

#### [Sequential Recovery Updates for Learned Controllers under Successful-Trajectory Preservation](https://arxiv.org/abs/2611.02555)
作者 / Authors: Zongtan Li, Tianming Liu, Ye Zhao(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 无链接(投稿 ICRA 2027)

🇨🇳 已学得的控制器改进时,新的进入规则可能重定向旧技能原本成功的状态。该工作约束「进入条件」而非参数:每次更新在测得的失败处搜索反馈技能,拟合读取观测的进入规则并拒绝累积成功轨迹上的所有状态,仅当组合控制器能独立复现新恢复且精确重放所有受保护轨迹时才接纳。在两个人形系统各两种动作共四条流上,每流两次更新共增加 62 次恢复(192 个保留扰动),且不丢失基础控制器任何成功;去掉约束可多恢复 33 个条件,但会使 8 个受保护条件无法完成。

🇬🇧 When improving a learned controller, a new entry rule can redirect states on which an old skill succeeded. This work constrains entry rather than parameters: each update finds a feedback skill at a measured failure and fits an entry rule that rejects every state on an accumulated successful trajectory, admitting the skill only if the composed controller reproduces the new recovery and replays all protected trajectories exactly. On four streams (two motions on each of two humanoid systems), two updates per stream add 62 recoveries over 192 withheld perturbations without losing any base success; removing the constraint recovers 33 more conditions but stops eight protected ones from completing.

#### [Faster Imitation by Re-timing Demonstrations Within the Controller Limit](https://arxiv.org/abs/2611.00539)
作者 / Authors: Zongtan Li, Tianming Liu, Ye Zhao(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 无链接(投稿 ICRA 2027)

🇨🇳 模仿策略继承操作者的节奏,把示教加速 2–3 倍后成功率会崩溃;作者指出机制原因:底层控制器每个控制周期只能实现有限位移,合并连续命令会产生执行器无法兑现的训练对(「超限占比」预测崩溃点)。规则只有一个参数:只要和仍可实现就贪心合并。在四个 robomimic 仿真任务(每格 200 个保留种子)上,合并上限为 2 时全部不低于冻结策略,Square 上高 14 个点且缩短成功回合;并迁移到人形全身跟踪器,429 条参考动作在其速度包络内重定时,2.3 倍速下 71% 片段成功,均匀 2 倍缩放为 51%。

🇬🇧 Imitation policies inherit the operator's pace and collapse when demonstrations are re-timed 2–3x faster; the paper identifies a mechanical cause: a low-level controller realises only a bounded displacement per period, so merging commands creates training pairs the plant cannot deliver (the 'exceed share' tracks collapse). The one-parameter rule merges greedily while the sum stays realisable. On four robomimic tasks (200 held-out seeds per cell), a merge cap of 2 matches or beats the frozen policy on all four (+14 points on Square) and shortens successful episodes; on a simulated humanoid whole-body tracker, re-timing 429 reference motions within its velocity envelope succeeds on 71% of clips at 2.3x versus 51% for uniform 2x scaling.

#### [Learning Purposeful Co-designs of Bio-inspired Quadrupedal Robots](https://arxiv.org/abs/2611.02462)
作者 / Authors: Fabio Boekel, Jiatao Ding, Cosimo Della Santina(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 无链接(10 页)

🇨🇳 形态与控制被分开设计,现有协同设计的设计空间受限。作者提出仿生四足 Dogger(模块化三段腿、四连杆、可调被动膝顺应),并用「强化学习 + 贝叶斯优化」两阶段框架:先跨设计训练形态条件控制策略,再固定策略做任务特定的设计选择。得到的设计与策略零样本部署后,巡检与载荷任务的运输成本分别降低 18.6% 与 35.7%;完整几何-顺应协同设计优于固定与受限设计范围,不同任务得到不同形态。

🇬🇧 Treating morphology and control separately limits quadrupeds, and prior co-design spaces are restricted. The authors introduce Dogger, a bio-inspired quadruped with modular three-segment legs, four-bar linkages and adjustable passive knee compliance, and a two-stage RL + Bayesian-optimization framework: a morphology-conditioned policy is trained across designs, then fixed during task-specific design selection. Designs and policies deployed zero-shot reduce cost of transport by 18.6% (inspection) and 35.7% (payload carrying); full geometry-compliance co-design beats fixed and restricted design scopes, with distinct task-specific morphologies.

#### [Pixel-UMI: Learning Environment-Aware Whole-Body Manipulation from Sensorized Human Demonstrations](https://arxiv.org/abs/2611.03647)
作者 / Authors: Jason Jingzhou Liu, Tony Tao, Deepak Pathak, Ruslan Salakhutdinov(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 模仿学习 / Imitation; 移动操作

开源状态 / Code: ❓ 未知 / Unknown — 仅有视频结果页 [pixel-robot.com/pixel-umi](https://pixel-robot.com/pixel-umi)

🇨🇳 带传感器的人类示教可扩展,但与机器人存在本体差异。Pixel-UMI 提出环境感知重定向(EAR):结合重建场景几何与示教头/夹爪轨迹确定机器人姿态并生成避碰的关节与底盘目标;再用重定向误差感知掩码(REAM)减少对错位视角的依赖,并用 DAgger 收集在线人类纠正。在 5 个任务(关节物体、可变形物体、狭小空间、全身避碰、双臂接触丰富协调)上平均任务进度 87.0%。

🇬🇧 Sensorized human demonstrations are scalable but embodiment differences complicate policy learning. Pixel-UMI introduces Environment-Aware Retargeting (combining reconstructed scene geometry with demonstrated head/gripper trajectories to produce collision-aware joint and base targets), Retargeting-Error-Aware Masking (REAM) to reduce reliance on mismatched views, and on-policy human corrections via DAgger. Across five tasks (articulated and deformable objects, constrained-space reaching, whole-body collision avoidance, contact-rich bimanual coordination) it achieves 87.0% average task progress.

#### [Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation](https://arxiv.org/abs/2611.03648)
作者 / Authors: Tony Tao, Jason Jingzhou Liu, Ruslan Salakhutdinov, Deepak Pathak(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 具身智能 / Embodied AI

开源状态 / Code: ❓ 未知 / Unknown — 仅有结果页 [pixel-robot.com/pixel](https://pixel-robot.com/pixel)

🇨🇳 移动操作所需的硬件、数据采集、全身控制与策略学习常被独立开发而不匹配。Pixel 是协同设计的全栈系统:低成本轮式人形(人类对齐运动学、顺应夹爪)、多种遥操作/免机器人人类数据采集接口、统一全身控制器、跨人类与机器人示教的共同策略学习流程,并以分层学习栈支持语言条件视觉运动控制与长程任务。系统在硬件、数据采集与策略学习上做了评测并展示需要灵巧性、主动感知、导航与全身协调的行为;摘要未给出定量数字。

🇬🇧 Mobile manipulation components (hardware, data collection, whole-body control, policy learning) are often developed independently and mismatch. Pixel is a co-designed full-stack system: a low-cost wheeled humanoid with human-aligned kinematics and compliant grippers, multiple teleoperation and robot-free data-collection interfaces, a unified whole-body controller, and a common policy-learning pipeline across human and robot demonstrations, with a hierarchical stack for language-conditioned visuomotor control and long-horizon tasks. It is evaluated across hardware, data and policy learning, showing behaviors needing dexterity, active perception, navigation and whole-body coordination; the abstract gives no quantitative numbers.

#### [Beyond Policy Patches: Distilling RL Specialists into Vision-Language-Action Policies](https://arxiv.org/abs/2611.02777)
作者 / Authors: Zhennan Jiang, Tingying Xie, Shilong Ji, Shu'ang Yu 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: VLA

开源状态 / Code: ❓ 未知 / Unknown — 无链接(19 页)

🇨🇳 VLA 能处理长程操作中的非关键阶段,却在短暂的精度关键阶段失败;轻量 RL 专家可补救但部署时需保留辅助控制器与切换机制。REPAIR 是价值引导的蒸馏框架:在关键阶段观测处向专家查询多个动作候选,用其 critic 加权构造监督分布,以加权 flow-matching 目标先在专家辅助 rollout 的观测上、再在 VLA 自身执行的观测上训练,专家只提供监督、部署时移除。六个真机任务(每任务 30 次评估)全部达到 100% 成功,且每个任务的平均末端抖动(jerk)均低于专家辅助执行。

🇬🇧 VLAs handle noncritical stages of long-horizon manipulation but fail in short precision-critical phases; lightweight RL specialists fix this but keep auxiliary controllers and switching at deployment. REPAIR is a value-guided distillation framework: at critical-phase observations it queries the specialist for multiple action candidates, weights them with its critic to form a supervision distribution, and trains a flow-matching VLA with a weighted objective first on specialist-assisted rollouts then on its own execution, removing specialists at deployment. Across six real-robot tasks (30 trials each) it reaches 100% success on all six, with lower mean end-effector jerk than specialist-assisted execution on every task.

#### [Behavioral Steering of Vision-Language-Action Models in the Low-Parameter Regime](https://arxiv.org/abs/2611.00522)
作者 / Authors: James Tcheng, Feiyu Gavin Zhu(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: VLA

开源状态 / Code: ❓ 未知 / Unknown — 无链接(NeurIPS 2026 RoboPAD Workshop)

🇨🇳 RL 越来越多地用于适配预训练 VLA;本文研究「行为引导」(如把物体举得更高)需要多少可训练容量。冻结 OpenVLA-OFT 7B,用 8–384 个可训练参数的 TinyLoRA 适配器,以 GRPO 或 CMA-ES 优化。仅 256 个参数即可在训练任务上把搬运高度提高 120 mm(成功率 92%),在留出任务上提高 74 mm(成功率 80%);缩放更新可在不重训的情况下权衡风格增益与能力保留,低参数量时 CMA-ES 有竞争力,容量增大后 GRPO 更优。

🇬🇧 RL is increasingly used to adapt pretrained VLAs; this paper asks how little trainable capacity behavioral steering (e.g. carrying objects higher) needs. A frozen OpenVLA-OFT 7B is adapted with TinyLoRA adapters of 8–384 parameters using GRPO or CMA-ES. With 256 parameters, carry height rises 120 mm on trained tasks at 92% success and 74 mm on a held-out task at 80%; rescaling the update trades style gains against capability retention without retraining, with CMA-ES competitive at low capacity and GRPO better as capacity grows.

#### [GoalDex: Learning Image-Goal-Conditioned Policies for Dexterous In-Hand Manipulation](https://arxiv.org/abs/2611.02171)
作者 / Authors: Arjun Bhardwaj, Mayank Mittal, Maximum Wilder-Smith, Vaishakh Patil 等(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: 🕒 计划开源 / Planned — 摘要称视频与代码发布见 [项目页](https://rffr.leggedrobotics.com/works/goaldex/);未核实页面内容,暂无可验证仓库

🇨🇳 灵巧手内操作通常依赖显式物体位姿估计,而遮挡下位姿跟踪不可靠且需物体特定监督。GoalDex 是端到端视觉运动框架,仅用 RGB 与本体感知,通过对特权状态教师的行为蒸馏与辅助重建目标联合学习视觉表示与控制,并引入图像目标条件的重定向,用图像而非规范位姿指定目标。仿真中跨多种物体几何/实例稳定优于基于位姿的方法和基于预训练视觉编码器的策略,并在 5 个真实物体上用单个策略直接 sim-to-real 迁移(摘要未给出具体成功率)。

🇬🇧 In-hand manipulation usually relies on explicit object pose estimation, which is unreliable under occlusion and needs object-specific supervision. GoalDex is an end-to-end visuomotor framework using only RGB and proprioception, jointly learning visual representations and control via behavior distillation from privileged-state teachers with auxiliary reconstruction, plus image-goal-conditioned reorientation so goals are given as images. In simulation it consistently outperforms pose-based methods and policies on pretrained visual encoders across object geometries and instances, and a single policy transfers directly sim-to-real across five real objects (the abstract gives no success rates).

#### [BeyondContact: A Reinforcement Learning Framework for Airflow-Based Non-Contact Manipulation](https://arxiv.org/abs/2611.03059)
作者 / Authors: Peiyu Yang, Mohamad S. Moudallal, Antonio Langella, Giulio Turrisi(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/iit-DLSLab/BeyondContact);匿名 ls-remote 验证存在,摘要称为项目材料(含 Isaac Lab 气流扩展)

🇨🇳 接触式操作受限于末端可达性与物体属性;气流可无接触施力,但缺少适合 RL 的仿真。作者为 Isaac Lab 开发与机器人和任务无关的气流扩展,基于实验辨识的气流模型支持大规模并行训练,训练了接触推动+吹气的混合策略(HPB)和仅靠气流控制长方体朝向的策略(RR),并设计与夹爪共存的轻量高速鼓风机。零样本真机部署中 HPB 在 20 次试验中成功率 80%,RR 在四个目标朝向上平均绝对朝向误差 2.6 度。

🇬🇧 Contact-based manipulation is limited by reachability and object properties; airflow can exert force without contact, but RL lacked a suitable simulator. The authors build a robot- and task-agnostic airflow extension for Isaac Lab from experimentally identified airflow models for massively parallel training, train a hybrid push-blow (HPB) policy and an airflow-only cuboid reorientation (RR) policy, and design a lightweight blower that coexists with a gripper. In zero-shot real-world deployment HPB reaches 80% success over 20 trials and RR achieves a mean absolute heading error of 2.6 degrees across four target headings.

#### [Positive Safety Margins from Artificial Potential Field Reward Augmentation for Size-Robust Obstacle Avoidance under Partial Observability](https://arxiv.org/abs/2611.02947)
作者 / Authors: Ziyi Hao(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/Hao-Ziyi/apf-reward-margin);Comments 给出代码与数据,匿名 ls-remote 验证存在

🇨🇳 障碍物大小与位置未被观测时,仅有碰撞惩罚的 RL 奖励无法鼓励留出间隙,策略贴着障碍表面走,障碍变大即失败。作者在仿真 Franka Panda 到达任务的奖励中加入水平人工势场项(围绕两根立柱的安全边界内惩罚接近),不向策略暴露障碍信息。隐藏观测下,带该项的策略在半径 0.03–0.055 m 扫描中安全成功率保持 88% 以上(30 个种子),不带的在最大半径下低于 10%;最小间隙 47.9 mm 对 9.6 mm,结果对三种 RL 求解器成立,路径约增长 19%。

🇬🇧 When obstacle size and position are unobserved, a collision-penalty-only RL reward does not depend on clearance, so the policy skims the obstacle and fails once the radius exceeds the training value. The authors add a horizontal artificial-potential-field term (penalizing proximity within a safety margin around two pillars) to a simulated Franka Panda reaching reward, without exposing the obstacle to the policy. Under hidden observation, policies with the term keep a safe success rate above 88% across radii 0.03–0.055 m (30 seeds) versus below 10% without it at the largest radius, with minimum clearance 47.9 mm vs 9.6 mm, across three RL solvers, at ~19% longer paths.

#### [When Robots Outweigh Objects: How Inertia Mismatch Shapes Robot Policy Learning](https://arxiv.org/abs/2611.03501)
作者 / Authors: Younghyo Park, Antonia Bronars, Pulkit Agrawal(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 行为克隆 BC

开源状态 / Code: ❓ 未知 / Unknown — 提供项目页 [项目页](https://younghyopark.me/inertia-mismatch/),未见代码声明

🇨🇳 传统机械臂相对物体很重,接触处存在惯量失配,是否对学习有隐性代价尚不清楚。作者在受控仿真中改变机器人与物体质量:RL 在宽广质量组合下均能成功,行为克隆在轻机器人操作重物体时更可靠,更多数据缩小但不能消除差距;电机经减速器反射的惯量增大同样使 BC 变差。无法换硬件时,选择低惯量工作区或引导示教者用低惯量解法,这两种仿真情形下的示教都更易被模仿。

🇬🇧 Conventional arms are heavy relative to everyday objects, but whether this inertia mismatch costs learning is unclear. In controlled simulation varying robot and object masses, RL succeeds across a broad range of mass combinations, while behavior cloning is more reliable when a lighter robot manipulates a heavier object (more data narrows but does not close the gap), and BC also degrades as motors reflect more inertia through gearing. Without new hardware, choosing a lower-inertia workspace or steering the demonstrator toward lower-inertia solutions makes demonstrations more reliably imitated in both simulated cases.

#### [SNAP: Semantic Navigation Among Pedestrians](https://arxiv.org/abs/2611.03498)
作者 / Authors: Jakob Wolfram, Pascal Roth, Fan Yang, Cesar Cadena(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 导航 / Navigation

开源状态 / Code: ❓ 未知 / Unknown — 无链接,无开源声明

🇨🇳 城市人群导航需要同时避让行人并遵守人行道等社会规范,现有方法通常只解决其一。SNAP 是 RL 导航策略,仅从单张语义标注的鸟瞰(BEV)图联合推理语义地形与动态障碍,无需显式人体状态估计。其性能优于成熟的人群导航与语义感知基线,并可零样本迁移到足式机器人,在高度动态的真实场景中展示了符合社会规范的导航(摘要未给出具体数值)。

🇬🇧 Crowded urban navigation requires avoiding pedestrians while obeying norms such as staying on sidewalks, yet existing methods address either crowd avoidance or semantic planning. SNAP is an RL navigation policy that jointly reasons about semantic terrain and dynamic obstacles from a single semantically annotated bird's-eye-view map, without explicit human-state estimation. It outperforms established crowd-navigation and semantic-aware baselines and transfers zero-shot to a legged robot with socially compliant navigation in dynamic real-world scenes (no numbers in the abstract).

#### [KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL](https://arxiv.org/abs/2611.03138)
作者 / Authors: Aswin Ramachandran, Jona Schulz, Maurus Derungs, Carlo Angelini 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 基准/平台 / Platform

开源状态 / Code: ✅ 已开源 / Released — [RL 与仿真](https://github.com/IDSCETHZurich/klask_rl);另有[推理软件](https://github.com/IDSCETHZurich/klask_software)与[硬件文档](https://idscethzurich.github.io/klask_hardware);klask_rl 匿名验证存在

🇨🇳 物理多智能体 RL 缺少可获得、标准化的基准。KlaskTron 是成本低于 2500 美元的桌面级对抗 MARL 机器人测试台(基于 KLASK 桌游,双 CoreXY 龙门架),提供硬件 CAD/BOM、Isaac Lab 中的 GPU 原生数字孪生,以及基于学习到的神经执行器模型的 sim-to-real 基线。该基线实现零样本策略迁移,训练智能体表现出涌现的对抗行为(摘要未给出具体数值)。

🇬🇧 Physical multi-agent RL lacks accessible, standardized benchmarks. KlaskTron is a sub-$2500 desktop adversarial MARL testbed based on the game KLASK (dual CoreXY gantries), providing hardware CAD/BOM, a GPU-native Isaac Lab digital twin, and a sim-to-real baseline with a learned neural actuator model. The baseline enables zero-shot policy transfer, with trained agents exhibiting emergent adversarial behaviors (no numbers in the abstract).

#### [KlaskTron-IL: A Contact-Rich Adversarial Imitation Learning Benchmark with a Validated Sim-to-Real Bridge](https://arxiv.org/abs/2611.03091)
作者 / Authors: Nicklas Sohm, Aswin Ramachandran, Raffaello D'Andrea(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 基准 / Benchmark

开源状态 / Code: ❓ 未知 / Unknown — 摘要未给出独立链接(同平台仓库见 KlaskTron 条目,数据集是否公开未知)

🇨🇳 在 KlaskTron 平台上构建多层模仿学习数据集:真机 8 万步人类示教、32 万步对称增广、以及由零样本验证的 PPO 策略生成的至多 500 万步合成专家轨迹,并给出诊断基线。基线暴露了接触丰富对抗动力学下标准 IL 的三类失效:BC 的数据扩展平台期、GAIL 判别器可解释但梯度弱(Spearman ρ=-1.0,但 logit 跨度小于 0.1)、以及 BC 先验与奖励密度的不对称交互。最强 BC 基线在命令落在执行器模型 ±0.2 m/s 辨识范围内时可零样本在真机运行。

🇬🇧 Built on the KlaskTron platform, this is a multi-tier IL dataset: 80k real human demonstration timesteps, 320k symmetry-augmented timesteps, and up to 5M synthetic expert steps from a zero-shot-validated PPO policy, plus diagnostic baselines. They expose three failure modes of standard IL under contact-rich adversarial dynamics: BC's data-scaling plateau, GAIL's interpretable but weak-gradient discriminator (Spearman ρ=-1.0, logit span under 0.1), and an asymmetric BC-prior x reward-density interaction. The strongest BC baseline runs zero-shot on the physical robot when commands stay within the actuator model's ±0.2 m/s range.

#### [Beyond Ensemble Disagreement: Predictive STL Monitoring of RL Locomotion under Distribution Shift](https://arxiv.org/abs/2611.02218)
作者 / Authors: Qurban Ali, Badaruddin Chachar, Maqsood Ali, Sajjad Ali Rajper(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 安全监测 / Safety

开源状态 / Code: ❓ 未知 / Unknown — 无链接(CoRL 2026 研讨会)

🇨🇳 RL 运动策略在名义仿真下训练,分布偏移会危及安全;预测性监测依赖世界模型预测,但其在偏移下不可靠且集成分歧未经校准。作者对冻结的 Ant-v5、HalfCheetah-v5 策略,用闭环世界模型 rollout 与三模型集成评估预测性信号时序逻辑(STL)监测。外力、观测噪声与质量偏移下,预测鲁棒度对 HalfCheetah 的未来违规排序较强,而分歧不能可靠追踪预测误差或违规;严重噪声下违规仍常见(K=20 时 64.2±24.4%,三个 PPO 种子),但无预测的当前状态鲁棒度与预测鲁棒度的 AUROC 相差不到 0.03,提示不应把集成分歧当作可靠的安全不确定性指标。

🇬🇧 RL locomotion policies trained in nominal simulation can violate safety under distribution shift; predictive monitors rely on world-model forecasts that may be unreliable, and ensemble disagreement is uncalibrated. The authors evaluate predictive Signal Temporal Logic (STL) monitoring for frozen Ant-v5 and HalfCheetah-v5 policies using closed-loop world-model rollouts and a three-model ensemble. Predicted robustness ranks HalfCheetah's future violations strongly while disagreement does not track prediction error or violations; under severe noise violations stay common (64.2±24.4% at K=20 over three PPO seeds), yet current-state robustness without prediction is within 0.03 AUROC of predictive robustness, cautioning against treating ensemble disagreement as a safety-uncertainty indicator.

#### [To Coordinate or Not to Coordinate? Learning to Swim with Eight Soft Arms](https://arxiv.org/abs/2611.02468)
作者 / Authors: Junkai Chen, Dehan Yuan, Yiyuan Zhang, Yu Duan(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 软体机器人 / Soft robotics

开源状态 / Code: ❓ 未知 / Unknown — 无链接(8 页)

🇨🇳 多条欠驱动软臂游泳是否需要臂间显式协调?作者比较三种 PPO 控制策略:共享节律驱动下各臂独立学习幅值(无相位耦合)、带预设相位耦合的幅值学习、以及无节律结构的端到端 PPO 直接学习驱动命令。随机三维速度指令的 200 个回合中,无相位耦合的控制器满足跟踪标准 169 次,相位耦合 117 次,端到端 PPO 仅 28 次;直线游动与变向试验也显示无相位耦合的速度跟踪更准确。结论是八臂游泳不必预设臂间相位耦合。

🇬🇧 Does effective swimming with multiple underactuated soft arms require explicit coordination? The authors compare three PPO strategies: learning arm-specific amplitudes under a shared rhythmic drive without inter-arm phase coupling, with prescribed phase coupling, and end-to-end PPO without rhythmic structure. Across 200 episodes with randomized 3D velocity commands, the uncoupled controller meets the tracking criterion in 169 episodes versus 117 (phase-coupled) and 28 (end-to-end PPO); straight-line and direction-change trials also show more accurate velocity tracking without coupling. Effective eight-arm swimming thus needs no prescribed phase coupling.

另见 GitHub 动态中的 SuperMimic 衍生仓库。

## 运动控制·传统 / Motion Control · Classical (共 9 条,全部展开)

MPC、CBF、自适应/学习控制、轨迹与路径跟踪等。

#### [Safe-Ballbot: Tilt-Consistent MPC with Control Barrier Functions for Ballbot Navigation](https://arxiv.org/abs/2611.03307)
作者 / Authors: Duc Cuong Vu, Tung Lam Nguyen(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: MPC / CBF

开源状态 / Code: ❓ 未知 / Unknown — 无链接(Under review)

🇨🇳 球平衡机器人需倾斜才能加速,倾角受轮扭矩与安全限制;全模型规划昂贵,忽略平衡动力学的规划又产生无法跟踪的参考。两层导航方案:上层是基于球位置 jerk 模型的 MPC 加离散时间 CBF(处理静态、移动、旋转与凹障碍),下层是带扩张状态观测器和鲁棒指数 CBF 的分层滑模控制器(HSMC-ESO-ECBF),两层用由允许稳态倾角闭式导出的加速度界相连;预测不确定障碍用共形预测半径膨胀。MuJoCo 中保持至少 10 cm 间隙、RMS 跟踪误差 2 cm 内、倾角不超限,规划 9–12 ms,比碰撞进入膨胀区的全模型非线性 MPC 快 10–15 倍。

🇬🇧 Ballbots must lean to accelerate, limited by wheel torque and safety; full-model planners are expensive while balance-agnostic ones give unfollowable references. A two-layer scheme uses an upper-layer MPC on a jerk model with discrete-time CBFs for static, moving, rotating and concave obstacles, and a lower-layer hierarchical sliding-mode controller with extended state observer and robust exponential CBF on tilt, linked by a closed-form acceleration bound from the largest admissible steady tilt; predicted obstacles are inflated by conformal-prediction radii. In MuJoCo it keeps at least 10 cm clearance, tracks within 2 cm RMS, respects the tilt limit and plans in 9–12 ms, 10–15x faster than full-model nonlinear MPC.

#### [Neural Integral Control Barrier Functions for Agile Collision Avoidance](https://arxiv.org/abs/2611.02626)
作者 / Authors: Dasari Raj Vamsi, Vrushabh Zinage, Efstathios Bakolas, Rohan Chandra(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: CBF / 安全滤波

开源状态 / Code: ❓ 未知 / Unknown — 无链接(23 页)

🇨🇳 CBF 假设控制仿射动力学、闭式障碍函数和已知名义控制器;积分 CBF 去掉了第一个假设但仍需后两者。本文从数据中学习三者:神经 ODE 学动力学、模仿学名义控制器、监督回归学障碍函数,并用「可行性」而非几何训练障碍(只有执行器限制下仍存在紧急避让机动才算安全),把执行器限制作为硬约束使在线规划每个状态均可解。在 6 维动态自行车敏捷赛车上,滤波器在 200 个保留布局中消除全部 12 个不安全回合且成功率不变,单 CPU 核频率超过 100 Hz。

🇬🇧 CBFs assume control-affine dynamics, a closed-form barrier and a known nominal controller; integral CBFs drop the first assumption only. This work learns all three from data (neural ODE dynamics, imitated nominal controller, regressed barrier), trains the barrier on viability rather than geometry (a state is safe only if an emergency maneuver can still avoid the constraint under actuator limits), and keeps actuator limits as hard bounds so the online program is solvable at every state. On agile racing with a 6-D dynamic bicycle, the filter removes all 12 unsafe episodes from 200 held-out layouts at unchanged success rate and above 100 Hz on one CPU core.

#### [Control Barrier Functions for Safety-Aware Latent-Space Motion Planning](https://arxiv.org/abs/2611.01814)
作者 / Authors: Chandrakiran Ravula, Siddhanth Ramesh(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: CBF / 运动规划

开源状态 / Code: ❓ 未知 / Unknown — 无链接(8 页)

🇨🇳 潜空间路径规划把机械臂构型空间压缩到 VAE 学到的可微流形,但用二值碰撞分类器避障会因梯度饱和而停滞且无前向不变性保证。作者用在潜空间中学习的神经 CBF 取代分类器,以安全/不安全符号约束加离散时间递减条件三项目标训练,并在规划时用闭式一阶修正把每个目标导向步投影回 CBF 约束。7 自由度 Franka Panda 上,固定障碍任务成功率 75.6%,比 35 个调参分类器配置中最好的高 12.0 个百分点,多位置任务 83.8%;完全随机障碍下降至 33.0%,作者归因于协变量偏移。

🇬🇧 Latent-space path planning compresses a manipulator's configuration space into a VAE-learned manifold, but binary collision classifiers saturate near obstacle boundaries, stalling the optimizer without forward-invariance guarantees. The authors replace the classifier with a neural CBF learned in the latent space (safe/unsafe sign constraints plus a discrete-time decrease condition), enforced at planning time by a closed-form first-order projection of each goal-directed step. On a 7-DoF Franka Panda it reaches 75.6% on fixed obstacles (12.0 points above the best of 35 tuned classifier configurations) and 83.8% on a multi-position task, dropping to 33.0% in the fully random-obstacle setting, attributed to covariate shift.

#### [Dual Path Following for an Aerial Manipulator Under State and Input Constraints via Transverse Feedback Linearization](https://arxiv.org/abs/2611.01442)
作者 / Authors: Hamza Tariq, Adeel Akhtar(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 横向反馈线性化 / TFL

开源状态 / Code: ✅ 已开源 / Released — 代码与动画见[项目页](https://gradslab.github.io/am_dual_pf-/)(摘要所述,仓库链接未核实)

🇨🇳 携带 3 自由度机械臂的四旋翼需让质心沿车体路径、末端沿第二条路径,同时满足关节限位并避奇异。以质心与末端路径坐标为输出并对推力做动态扩展,系统存在无内动态的正规形;将横向反馈线性化控制器写成仅松弛末端沿路径速度的二次规划(约化为有闭式解的标量问题)。若问题始终严格可行,反馈局部 Lipschitz、两条路径不变且吸引、所有约束成立。Drake 中控制器通过减慢末端解决两速度参考冲突且两路径保持不变,而级联安全滤波会偏离两条路径。

🇬🇧 A quadrotor carrying a 3-DoF arm must make its center of mass follow a vehicle path and its end effector a second path while respecting joint limits and avoiding singular postures. With center-of-mass and end-effector path coordinates as outputs and a dynamic thrust extension, the system admits a normal form without internal dynamics; the transverse feedback linearizing controller is posed as a QP relaxing only the end-effector speed along its path (reducing to a scalar closed-form problem). If it stays strictly feasible, feedback is locally Lipschitz, both paths are invariant and attractive, and all constraints hold. In Drake it resolves a speed-reference conflict by slowing the end effector with both paths invariant, whereas a cascade with a safety filter leaves both paths.

#### [Multi-quadrotor systems interconnected via structurally unknown forces and moments](https://arxiv.org/abs/2611.00887)
作者 / Authors: Kaiyue Xing, Shivansh Pratap Singh, Sarthak Mishra, Di Liu(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 自适应控制 / Adaptive control

开源状态 / Code: ❓ 未知 / Unknown — 摘要给出[实验视频](https://tinyurl.com/4mzpb9rf),无代码声明

🇨🇳 多四旋翼系统存在紧耦合、结构未知的状态相关互联力与力矩(不假设线性参数化),只依赖欧拉-拉格朗日系统通用的二次界。作者提出嵌入自适应律的协调策略,补偿结构知识缺失,并给出考虑位置-姿态耦合的联合稳定性分析而非解耦设计。绳连负载协同空中运输的真机实验验证了有效性,对比实验显示当负载掉落扰动沿绳传遍整个编队时,所提策略显著降低扰动后的瞬态。

🇬🇧 Multi-quadrotor systems have tight couplings whose interconnection forces and moments are state-dependent with unknown structure (no linear-in-parameters assumption), relying only on general quadratic bounds valid for Euler-Lagrange systems. The authors propose a coordination strategy with adaptive laws compensating the missing structural knowledge, with a coupled position-attitude stability analysis rather than decoupled designs. Real experiments on cooperative aerial transport of rope-interconnected payloads confirm effectiveness, and comparisons show significantly reduced post-disturbance transients when a payload drop propagates through the ropes.

#### [Central pivot point control of a body-attached spring-mass runner: periodic gaits, stabilization, template embedding and approximate analytic return maps](https://arxiv.org/abs/2611.02564)
作者 / Authors: İzel Sever, O. Kaan Karagöz, M. Mert Ankaralı(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 跑步模板 / Running templates

开源状态 / Code: ❓ 未知 / Unknown — 无链接(投稿 Chaos 期刊)

🇨🇳 SLIP 模型没有躯干,带躯干模型中髋扭矩耦合姿态与质心运动并破坏中心力结构,故多只能数值研究。中心枢轴点(CPP)是一种使地面反力过质心的髋扭矩律,精确解耦俯仰并把支撑相化为平面中心力问题;直立姿态下时间反演对称产生单参数周期步态族,支撑相俯仰律和步幅调节器可镇定全部已算步态。含新的重力修正的解析返回映射(据作者所知为躯干模型首例)预测离地速度与顶点位置的平均误差为 1.6% 与 0.9%,基于该映射的 deadbeat 步幅控制器可跟踪速度、高度与姿态变化。

🇬🇧 The SLIP model has no trunk; in trunk models the hip torque couples posture and COM motion and destroys the central-force structure, so they are studied almost only numerically. The central pivot point (CPP), a hip-torque law directing the ground reaction force through the COM, decouples pitch exactly and reduces stance to a planar central-force problem; time-reversal symmetry yields one-parameter families of periodic gaits that a stance pitch law and stride-level regulator stabilize. With a new gravity correction, the analytic return map (the first for a trunk model to the authors' knowledge) predicts liftoff velocity and apex position with mean errors of 1.6% and 0.9%, and a deadbeat stride controller based on it tracks changes of speed, height and posture.

#### [Delay-Certified Readiness Barriers for Overactuated Multirotor Allocation Without Lipschitz Constants](https://arxiv.org/abs/2611.03490)
作者 / Authors: Giuseppe Silano(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: CBF / 控制分配

开源状态 / Code: ❓ 未知 / Unknown — Comments 仅投稿信息

🇨🇳 过驱动多旋翼同一合力矩有多种转速组合,有些使飞行器难以快速改变力矩(如抗阵风);「就绪度」屏障只在连续时间成立,采样指令与变化的速度控制器延迟下现有鲁棒界不足 1 毫秒。作者利用每个旋翼对自身扭矩单调且闭式响应的结构:不确定切换时刻下可达转速落在易算的盒内,盒内最低就绪度在预知的角点,从而得到免 Lipschitz 的检验与保证计划的备用扭矩。六旋翼仿真中延迟 2–40 ms、抖动 ±2 ms,滤波器从未违反下限;10±2 ms 时在设计包络内与延迟补偿预测器相当,超出后多 2–30% 跟踪误差,而单独预测器在 16 个任务中 2 到 16 个违反下限。

🇬🇧 Overactuated multirotors can realize one wrench with many rotor-speed combinations, some leaving little ability to change wrench quickly (e.g. to reject gusts); readiness barriers work only in continuous time, and with sampled commands and varying delays the available robustness bound covers under a millisecond. Exploiting each rotor's monotonic closed-form response, reachable speeds under uncertain switching lie in a cheap box whose lowest readiness is at a known corner, giving a Lipschitz-free test and a fallback torque on a certified plan. In hexarotor simulations with 2–40 ms delays and ±2 ms jitter the filter never violated the floor; at 10±2 ms it matched a delay-compensating predictor inside the design envelope (2–30% more tracking error beyond it), while the predictor alone violated the floor in 2 to 16 of 16 missions.

#### [Trading Transparency for Stability: Friction-Cone-Constrained Bilateral Teleoperation for Opening Doors of Unsecured Furniture](https://arxiv.org/abs/2611.00898)
作者 / Authors: Cheng Zhou, Jing Li(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 遥操作 / Teleoperation

开源状态 / Code: ❓ 未知 / Unknown — 无链接(7 页)

🇨🇳 拉开未固定家具的门会加载支撑处摩擦接触,拉力过大会滑动或倾倒;摩擦锥约束消除失效但牺牲触觉透明度。作者量化该权衡:由接触摩擦锥与支撑多边形倾覆裕度构造容许力矩集并按质量与摩擦误差收缩,集合内任何指令可证明使家具保持静止(鲁棒摩擦锥投影 RFCP),RFCP 与触觉护栏带来有界的力传递误差,仅在约束边界附近带内透明度下降,宽度由一个稳定因子决定。在 3 个柜子、2 种支撑、5 名操作者共 100 次试验中测量稳定-透明权衡并对护栏、RFCP 与位置基线做消融。

🇬🇧 Opening the door of unsecured furniture loads frictional support contacts; too large a pull slides or tips it, and a friction-cone constraint on the commanded wrench removes this but costs haptic transparency. The authors build an admissible wrench set from contact friction cones and support-polygon tipping margins, shrunk for bounded mass and friction errors, so any command in it provably leaves the furniture static (robust friction cone projection, RFCP); RFCP with a haptic guard gives a bounded force-transmission error, with transparency degrading only in a band near the boundary whose width is set by one stability factor. Experiments on three cabinets, two supports and five operators (100 trials) measure the trade-off and ablate the guard, RFCP and a position baseline.

#### [Differentiable Iterative Learning Control for Black-Box Position-Commanded Manipulators](https://arxiv.org/abs/2611.01220)
作者 / Authors: Mohammed Al-Ghaili, Yakoop Qasim, Hassan Almubarak(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: ILC / 学习控制

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 底层控制器不可访问的位置指令机械臂做高精度重复轨迹跟踪困难,约束模型 ILC 又需大量人工调参。Diff-ILC 是在线双层框架,在两次物理执行之间自适应约束 ILC 更新的参数:一次性辨识并固定闭环微分模型,每次试验用约束二次规划计算可行的指令修正,以真实锚定的下一次试验预测定义任务级目标,并通过隐式微分局部激活的 KKT 系统获得超梯度,无需额外机器人执行即可多次更新参数。DOBOT CR3 六自由度臂实验中,仅两次试验间更新后,关节向量与笛卡尔 RMSE 的均值相对固定参数模型 ILC 分别降低 78.8% 与 76.4%。

🇬🇧 High-accuracy repetitive tracking is hard for position-commanded manipulators with inaccessible low-level controllers, and constrained model-based ILC needs heavy tuning. Diff-ILC is an online bilevel framework that adapts the parameters of a constrained ILC update between physical executions: a closed-loop differential model is identified once and fixed; each trial a constrained QP computes a feasible command correction, a real-anchored next-trial prediction defines the objective, and hypergradients come from implicitly differentiating the active KKT system, allowing multiple updates without more robot runs. On a 6-DoF DOBOT CR3, after two trial-to-trial updates it lowers mean joint-vector and Cartesian RMSE by 78.8% and 76.4% versus fixed-parameter model-based ILC.

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

展开 6 条(本类可展开条目不足 8 条,其余列名)。

#### [RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild](https://arxiv.org/abs/2611.02497)
作者 / Authors: Tan Sang Nguyen, Yi Ru Wang, Shailesh Shailesh, Gang Yang 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: VLA 评测

开源状态 / Code: ❓ 未知 / Unknown — 项目页 [robocolosseum.ai](https://robocolosseum.ai/);未见代码声明

🇨🇳 通用机器人策略需跨机器人、任务与环境工作,但物理试验难以复现。RoboColosseum 是分布式评测框架,结合统一策略服务与标准化协议,覆盖局部运营的机器人网络;首轮研究评估 5 个 VLA 策略和 3 个前沿 AI 智能体,覆盖 SO-101、Franka、双臂 YAM 与 G1 人形四种本体。在 124 个站点的 5,699 次开放赛道成对比较中,前沿智能体可与专用 VLA 策略匹敌,但所有系统在开放世界任务上都不可靠;微调后 GR00T N1.7 在 SO-101 领先,pi0.5 在 Franka 与双臂 YAM 领先;跨本体任务套件的排名一致性较弱(Kendall W=0.24)。

🇬🇧 General-purpose policies must work across robots, tasks and environments, but physical trials are hard to reproduce. RoboColosseum is a distributed evaluation framework with unified policy serving and standardized protocols across a network of locally operated robots; the first study evaluates five VLA policies and three frontier AI agents across SO-101, Franka, bimanual YAM and G1 humanoid. Over 5,699 pairwise Open Track comparisons at 124 sites, frontier agents rival specialized VLAs while all systems struggle with open-world tasks; after fine-tuning, GR00T N1.7 leads on SO-101 and pi0.5 on Franka and bimanual YAM, and rankings agree weakly across embodiment-specific suites (Kendall W = 0.24).

#### [Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation](https://arxiv.org/abs/2611.01112)
作者 / Authors: Chengcheng Wang, Yuheng Shi, Siyu Xu, Yutong Wang 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 机器人使用智能体 / Robot-use agent

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 VLM 能理解指令并规划,但直接当策略时在 RoboDojo 上存在大的规划-执行鸿沟:去掉机械臂执行,GPT-6 Astra 成功率从参考控制接口下的 22.5% 升至 76.2%。Auriga 是任务无关的智能体 harness,模型基于显式任务信念,通过工具调用或合成的多步 Python 程序行动,harness 提供标定 3D 测量、手指参照双臂控制和统一准入网关,运动前预览视觉轨迹,执行中检查阶段容差与抓取边界并回传偏差用于原地恢复。它在 RoboDojo 排行榜上以 57.7% 成功率(64.0 分)排名第一,零样本下弥合了 68.3% 的鸿沟。

🇬🇧 VLMs plan well but struggle as direct policies: on RoboDojo a large planning-execution gap exists (removing arm execution lifts GPT-6 Astra from 22.5% under the reference control interface to 76.2%). Auriga is a task-agnostic harness where the model decides over an explicit task belief via tool calls or synthesized multi-step Python, while the harness supplies calibrated 3D measurements, finger-referenced dual-arm control and a single admission gateway, previews trajectories before motion and checks stage tolerances and grasp bounds during execution with in-place recovery. It ranks first on the RoboDojo leaderboard at 57.7% success (64.0 score), closing 68.3% of the gap zero-shot.

#### [Democratizing Robot-Use Agents: A Unified Harness with Open Models](https://arxiv.org/abs/2611.01560)
作者 / Authors: Jiarui Yuan, Yuxin Zuo, Xiaoyu Huang, Wenbo Zhang 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 机器人使用智能体 / Robot-use agent

开源状态 / Code: ❓ 未知 / Unknown — 摘要提到 uni-robot-agent harness,未给链接

🇨🇳 机器人使用智能体(RUA)依赖专有前沿模型,限制了进一步训练研究。作者提出 uni-robot-agent,一个支持继续训练的统一 harness,面向有竞争力的开放权重模型。无特权输入时,开箱即用的 Qwen3.8-Flash-Next 在 RoboDojo 得分 31.39,超过已发表的 GPT-6 Astra-RoboProbe(28.97)及许多 VLA/WAM 基线,并在 19 个真实任务上表现有竞争力;分析把有效的机器人使用归结为四种通用能力。

🇬🇧 Robot-use agents rely on proprietary frontier models, limiting research on further training. The authors introduce uni-robot-agent, a unified harness for competitive open-weight models that supports further training. With no privileged inputs, an out-of-the-box Qwen3.8-Flash-Next scores 31.39 on RoboDojo, surpassing the published GPT-6 Astra-RoboProbe result (28.97) and many VLA/WAM baselines, and is competitive on 19 real-world tasks; analysis links effective robot use to four general capabilities.

#### [MOST: Memory of Object States and Task Progress for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2611.00734)
作者 / Authors: Diqi He, Jinbang Guo, Yijun Shen, Zhiwei Yu 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 移动操作 / Mobile manipulation

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 长程具身操作需依据不再可见的信息行动;现有方法仍让策略从冗长、冗余、依赖视角的视觉经验中推断任务状态。MOST 是策略内部的记忆框架,把多视角观测压缩成时序 token,并用物体状态和子任务进度显式监督历史与预测的未来 token,直接在单个端到端策略内条件化动作生成,无需外部规划器或检索。作者还提出多分钟多阶段的移动操作基准 RoboCasa-Long;摘要截取处未给出完整的定量结果。

🇬🇧 Long-horizon embodied manipulation needs information no longer visible; existing approaches leave the policy to infer task state from long, redundant, viewpoint-dependent experience. MOST is a policy-internal memory that compresses multi-view observations into temporal tokens, explicitly supervises historical and predicted future tokens with object states and subtask progress, and conditions action generation within a single end-to-end policy with no external planner or retrieval. The authors also introduce RoboCasa-Long, a benchmark of multi-minute, multi-stage mobile manipulation tasks; the abstract text retrieved does not include the full quantitative results.

#### [D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models](https://arxiv.org/abs/2611.03622)
作者 / Authors: Marius Memmel, Shawn Yin, Urvi Rutia, Angad Wadhwa 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 奖励模型 / Reward model

开源状态 / Code: ❓ 未知 / Unknown — 摘要给出网站 [weirdlabuw.github.io/dna](https://weirdlabuw.github.io/dna);未见代码声明

🇨🇳 VLM 用于零样本视频任务进度估计时常有确认偏差,在失败执行中虚构进度,朴素提示退化为二值成功检测器。D&A(Describe & Assess)把进度估计解耦为:先对场景动态做客观、基于任务的文字描述,再用显式评分细则评估,迫使 VLM 先合成绝对成功的文字定义,让评估锚定外部全局标准而非视频内部时间线。结果显示该方法校准了零样本估计、缓解确认偏差并给出细粒度部分进度度量(检索到的摘要末尾被截断,未含具体数字)。

🇬🇧 VLMs used for zero-shot video task-progress estimation show confirmation bias, hallucinating progress in failed executions, and naive prompting collapses into a binary success detector. D&A (Describe & Assess) decouples progress estimation into an objective task-grounded textual description of scene dynamics followed by assessment with explicit rubrics, forcing the VLM to write an absolute definition of success first so evaluation is anchored to an external global criterion rather than the video's internal timeline. It calibrates zero-shot estimates, mitigates confirmation bias and gives fine-grained partial-progress metrics (the retrieved abstract is cut off before specific numbers).

#### [Closing the Dynamics Gap through Self-Directed Robotic Interaction](https://arxiv.org/abs/2611.02691)
作者 / Authors: Xilun Zhang, Liam Achenbach, Luis Pabon, Matthew Foutter 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: Real2Sim2Real

开源状态 / Code: ❓ 未知 / Unknown — 项目页 [cue-dynamics.github.io](https://cue-dynamics.github.io/)(CoRL 2026 LBR);未见代码声明

🇨🇳 Real2Sim2Real 系统能从相机重建仿真场景,但摩擦与恢复系数等接触动力学无法不交互地观测(「动力学鸿沟」)。CUE 是智能体系统,仅给高层指令且无重置,自行构建感知、辨识物理参数,并把交互目标放在仿真最不准的地方。在台球任务中,25 个隐藏物理条件下,保留球位置误差相对最强基线降低 72%,并部署在真实球台上。

🇬🇧 Agentic Real2Sim2Real systems can reconstruct scenes in simulation, but contact dynamics such as friction and restitution cannot be observed without interaction (the 'dynamics gap'). CUE closes it by interacting itself: given only a high-level instruction and no resets, it builds its own perception, identifies physical parameters and targets interactions where its simulation is least accurate. On billiards it reduces held-out ball-position error by 72% versus the strongest baseline across 25 hidden-physics conditions in simulation, and is deployed on a real pool table.

其余列名 / Others (16 条 / items):[From Concepts to Actual Causes: Toward Closing the Concept-Malfunction Gap in Robot Foundation Models](https://arxiv.org/abs/2611.00155)、[Learning to Live: A Step Toward Lifelong Embodied Intelligence](https://arxiv.org/abs/2611.00180)、[SPARK: Self-Correcting Embodied Memory via Physical Re-Observation](https://arxiv.org/abs/2611.00344)、[Knowing Where to Look: Interactive Object Search via Spatial-Semantic Fusion](https://arxiv.org/abs/2611.00499)、[Generalizable robotic manipulation through compositional skill reuse](https://arxiv.org/abs/2611.00978)、[Serving Agentic Robot Fleets: Workload Characterization, KV-Cache Thrashing, and Admission Control](https://arxiv.org/abs/2611.01404)、[Learning from an Imitable Teacher: Competition Solution for the MetaFine Challenge](https://arxiv.org/abs/2611.00615)、[Rollout then Recycle: 3,718 Labelled Real-Robot Episodes from Benchmarking 7 Policies on 12 Tasks](https://arxiv.org/abs/2611.03168)、[Does Validation Loss Predict Real-Robot Success? Evidence from Four Imitation-Learning Policies on a Low-Cost Arm](https://arxiv.org/abs/2611.00283)、[Beyond Validation Loss: Coverage and Reliability Dynamics in Robot Policy Pretraining](https://arxiv.org/abs/2611.01565)、[Neuro Inspired Robotics: What Robot Learning Can Borrow from the Sensorimotor Brain](https://arxiv.org/abs/2611.02510)、[DexArena: A Unified Benchmark for Long-Horizon Dexterous Manipulation](https://arxiv.org/abs/2611.02629)、[PointPilot: Unified Robotic Manipulation via Object-Centric 3D Point Flow Prediction](https://arxiv.org/abs/2611.02930)、[Visuo-tactile Diffusion Policy for Robotic Manipulation with Auxiliary Tactile Dynamics Prediction](https://arxiv.org/abs/2611.02677)、[TF²-Steering: Action Refinement with Tactile Forecasts and Feedback via Velocity-Field Steering](https://arxiv.org/abs/2611.01483)、[Evaluating Tactile Foundation Models for End-to-End Imitation Learning in Contact-Rich Manipulation](https://arxiv.org/abs/2611.00957)。其中 DexArena 在 radar new_repos 中有同名仓库 [SIPAIR-Elastic/DexArena](https://github.com/SIPAIR-Elastic/DexArena)(2 star,匿名 ls-remote 存在,与论文对应关系未经核实)。

另见 / See also: [Pixel](https://arxiv.org/abs/2611.03648)、[Pixel-UMI](https://arxiv.org/abs/2611.03647)(已归入 运动控制·RL / Motion Control · RL);[PREM](https://arxiv.org/abs/2611.00634) 保留在 VLA 类。

## VLA / Vision-Language-Action

展开 10 条。

#### [Vision-Language Models Are Joint Denoisers in Robotic Action Generation](https://arxiv.org/abs/2611.01215)
作者 / Authors: Xicheng Gong, Wenxuan Song, Chengze Liu, Qiwei Li 等(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 无链接(19 页)

🇨🇳 扩散式 VLA 把 VLM 与扩散动作专家级联,VLM 只提供静态条件,限制了预训练感知与推理对动作生成的引导。JADE 让 VLM 与动作专家联合去噪:结构化动作潜变量使 VLM 能同时读取当前带噪动作、视觉与语言,每个去噪步通过门控交叉注意力引导动作专家,并监督 VLM 从带噪潜变量恢复干净潜变量;联合去噪可减少采样步数,自适应步长调度权衡性能与延迟。在 RoboDojo 上平均成功率 12.67%,为 π0.5 系方法中最高,并与大规模预训练的 VLA/WAM 基础模型相当;RoboTwin 2.0 与四个真实双臂任务平均成功率也有提升。

🇬🇧 Diffusion VLAs cascade a VLM with a diffusion action expert but restrict the VLM to static conditioning. JADE lets the VLM and action expert jointly denoise: structured action latents let the VLM read the current noisy action with observations and language, guiding the expert via gated cross-attention at every step, with the VLM supervised to recover clean latents; joint denoising permits fewer sampling steps and an adaptive step-size schedule balances accuracy and latency. On RoboDojo it achieves 12.67% average success, the highest among π0.5-based methods and competitive with large-scale pretrained VLA/WAM foundation models, and it improves RoboTwin 2.0 and four real-world bimanual tasks.

#### [Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency](https://arxiv.org/abs/2611.01390)
作者 / Authors: Fuyi Chen(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 无链接(22 页)

🇨🇳 部署的 VLA 在等待下一块动作推理时停顿,且按缓慢谨慎的示教速度运动,二者的已有补救叠加会失效。路径保持时间缩放(PTS)是针对冻结动作分块策略的免训练执行层:路径层确定性解码每次重规划并按推理期间已消耗的进度进入;时间层累加规划增量,夹爪运动时保持 1 倍,并按执行器线性范围与延迟下的分块可行性限速,还推导出加速是否划算的盈亏平衡成功率。LIBERO 上两个冻结 VLA 在注入延迟下,任务吞吐相对最强可部署基线对 pi0.5 提升 33%、对 SmolVLA 提升 104%,成功率持平或提升,并超过零延迟 1 倍执行。

🇬🇧 Deployed VLAs halt while the next chunk is inferred and move at the pace of slow, cautious demonstrations; stacking existing remedies fails. Path-preserving Time Scaling (PTS) is a training-free execution layer for frozen action-chunking policies: a path layer decodes every replan deterministically and enters it at the progress consumed during inference, and a time layer sums planned increments, keeps 1x while the gripper moves, caps the rate by actuator range and chunk feasibility under latency, and a break-even success rate says when speed-up pays. On LIBERO with two frozen VLAs under injected latency, PTS raises throughput over the strongest deployable baseline by 33% (pi0.5) and 104% (SmolVLA) while matching or improving success, and exceeds zero-latency 1x execution.

#### [VLALagBench: Understanding When and Why VLA Inference Latency Matters](https://arxiv.org/abs/2611.03103)
作者 / Authors: Qi Wen, Borui Xu, Hussein Amro, Hongshi Tan 等(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: 🕒 计划开源 / Planned — Comments 称 [代码将发布于](https://github.com/codestrongestx/VLALagBench);匿名 git ls-remote 不可访问,尚未发布

🇨🇳 推理延迟与任务成功率的关系尚不清楚。VLALagBench 是研究 VLA 推理延迟敏感度的基准,覆盖任务类型、物体速度、同步/异步执行与 VLA 策略。发现仅 100 ms 延迟就能让移动目标任务成功率近乎减半,敏感度随任务与策略差异显著;异步执行可挽回部分成功率但需更频繁推理。作者还建立由少量标定数据预测任务成功率的经验模型,各 VLA 的 RMS 预测误差为 5.7–7.8%,可指导系统级配置选择。

🇬🇧 How latency relates to task success is poorly understood. VLALagBench benchmarks VLA inference-latency sensitivity across task types, object speeds, synchronous/asynchronous execution and VLA policies. A modest 100 ms latency can nearly halve success on moving targets with large task- and policy-dependent differences; asynchronous execution recovers some of it at the cost of more inference requests. An empirical model predicts success from limited calibration data with RMS errors of 5.7–7.8% across VLA policies, guiding system-specific configuration choices.

#### [Reflex: Fast Robot Policy Serving by Reusing and Correcting Past Actions](https://arxiv.org/abs/2611.00524)
作者 / Authors: Ziyang Lin, Zixuan Sun, Rami Nasser, Jianli Jin 等(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 机器人策略推理是实时控制的延迟瓶颈和多机器人服务的吞吐瓶颈;作者发现复用中间去噪状态的缓存相比直接少步去噪优势很小,且策略主干可占 GPU 时间的 70%。Reflex 是服务层,缓存完整动作块以绕过主干与动作头,并用两级缓存修正:动作层从历史决策学习动作感知相似性、拼接兼容块并做轻量残差修正;执行层捕获任务进度并自适应刷新原策略以限制累积误差。摘要检索文本在报告成绩前被截断,未含具体加速数值。

🇬🇧 Policy inference is a latency bottleneck for real-time control and a throughput bottleneck for multi-robot serving; the authors find that reusing intermediate denoising states offers little advantage over simply running fewer denoising steps, and the backbone can take 70% of GPU time. Reflex is a serving layer that caches complete action chunks to bypass both backbone and action head, with two-level correction: at the action level it learns action-aware similarity, assembles compatible chunks and applies residual correction; at the execution level it tracks task progress and adaptively refreshes the original policy. The retrieved abstract is cut off before the speed-up numbers.

#### [HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation](https://arxiv.org/abs/2611.02660)
作者 / Authors: Gyeonghun Kim, Donghoon Kim, Minsoo Choi, Suyun Lee 等(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 项目页 [kimspacehuni.github.io/HeLM](https://kimspacehuni.github.io/HeLM/);未见代码声明

🇨🇳 多数 VLA 采用马尔可夫假设,只把当前观测映射到动作,在需要工作记忆的任务上失败。HeLM 是分层 VLA 框架,受「内心独白」启发,通过分解事件检测和事件触发的记忆更新,用显式语言维护任务相关历史。在 10 个非马尔可夫真实任务(56 个变体,含 5 个需要跨回合上下文的新任务)上,回合内成功率比最强基线高 12.8 个百分点,组合泛化任务子任务成功率 78%,内存最多减少 4.5 倍,长程时比关键帧基线快 2.5 倍。

🇬🇧 Most VLAs are Markovian, mapping only the current observation to an action, and fail where working memory is needed. HeLM is a hierarchical VLA that keeps task-relevant history in explicit language through factorized event detection and event-triggered memory updates, inspired by the inner monologue. On 10 non-Markovian real-world tasks (56 variants, including five new inter-episode tasks) it improves intra-episode success by 12.8 points over the strongest baseline, reaches 78% subtask success on compositional generalization, uses up to 4.5x less memory and runs 2.5x faster than the keyframe baseline at long horizons.

#### [PREM: Prediction-Regulated Memory for Robot Manipulation](https://arxiv.org/abs/2611.00634)
作者 / Authors: Xiao Huang, Ya Zhang, Weidi Xie(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 世界模型 / World Model

开源状态 / Code: ❓ 未知 / Unknown — 无链接(23 页)

🇨🇳 机器人下一动作可能依赖当前观测中缺失的近期运动或早先视觉证据;循环视觉记忆的价值取决于状态表示什么及如何更新。PREM 用动作条件的未来预测引导 VLA 策略的记忆学习与更新:训练时预测未来视觉特征提供时序监督,执行时用当前特征与上一决策预测的空间归一化差异调节每个位置的视觉状态更新。基于 π0.5,DOMINO 动态操作任务平均成功率从 9.63% 提升到 20.74%,RMBench M(1) 记忆依赖设定从 14.4% 提升到 83.8%,LIBERO 与 LIBERO-Pro 也有改进。

🇬🇧 A robot's next action may depend on recent motion or earlier visual evidence absent from the current observation; a recurrent visual memory's value depends on what the state represents and how it is updated. PREM uses action-conditioned future prediction to guide memory learning and updating in VLA policies: predicting future visual features gives temporal supervision in training, and the spatially normalized discrepancy between current features and the previous prediction regulates per-location state updates at execution. Built on π0.5, it raises DOMINO dynamic-manipulation success from 9.63% to 20.74% and RMBench M(1) memory-dependent success from 14.4% to 83.8%, with gains on LIBERO and LIBERO-Pro.

#### [Route-Guided CBF-QP Repair for Safe Vision-Language-Action Models](https://arxiv.org/abs/2611.01713)
作者 / Authors: Chan Park, Sunwoo Hong, Kirak Kim, Yoonjeong Park(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: CBF / 安全

开源状态 / Code: ❓ 未知 / Unknown — 摘要称项目页在 GitHub,未给具体链接

🇨🇳 VLA 不保证障碍丰富场景中的执行安全;CBF-QP 安全滤波器局部投影不安全动作,但可能把机器人推离学到的任务轨迹且不给 VLA 恢复方向。作者提出 Route-Guided CBF-QP Repair:利用 VLA 预测的短时域动作块检测被阻挡的名义轨迹,生成「进入-退出-重新汇合」绕障引导,把所选路径作为软引导项加入 CBF-QP 目标,CBF 安全约束仍为硬约束。在 SafeLIBERO 上,避碰、任务成功率与 SafeSuccess 均优于 AEGIS(摘要未给具体数字)。

🇬🇧 VLAs do not guarantee safe execution in obstacle-rich scenes; CBF-QP filters project unsafe actions locally but may push the robot off the learned trajectory and give the VLA no recovery direction. Route-Guided CBF-QP Repair uses the VLA's short-horizon action chunk to detect blocked nominal trajectories and generate entry-exit-rejoin guidance around obstacles, added to the CBF-QP objective as a soft term while the CBF safety constraint stays hard. On SafeLIBERO it improves collision avoidance, task success and SafeSuccess over AEGIS (no numbers in the abstract).

#### [CalVLA: Shaping Native Confidence in Vision-Language-Action Policies with Outcome Supervision](https://arxiv.org/abs/2611.00394)
作者 / Authors: Boniface Chukwuemeka Godwin(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 VLA 能否从自身动作概率发出失败信号?CalVLA 用成功与失败 rollout 和 Action-Confidence Alignment(ACal)平方间隔排序损失塑造原生动作 token 置信度,通过低秩适配器更新 OpenVLA-7B,无需额外失败检测器。在 500 个 LIBERO-10 配置的留出测试上,适配后置信度的联合失败判别 AUROC 为 0.7392±0.0480(三个种子);冻结策略探针 0.6146–0.6436,但相对线性探针的优势统计上不确定;同一置信度摘要的 AUROC 由适配前 0.4485 升至 0.7327,平均任务成功率由 58% 降至 55%,作者强调这是失败判别的改善而非控制或安全收益。

🇬🇧 Can a VLA signal likely failure from its own action probabilities? CalVLA shapes native action-token confidence with successful and failed rollouts and an Action-Confidence Alignment (ACal) squared margin-ranking loss, updating OpenVLA-7B via low-rank adapters without an auxiliary failure detector. On a held-out split of 500 LIBERO-10 configurations, adapted confidence reaches a joint failure-discrimination AUROC of 0.7392±0.0480 over three seeds (frozen probes 0.6146–0.6436, superiority over the linear probe statistically inconclusive); AUROC rises from 0.4485 to 0.7327 after adaptation while mean success falls from 58% to 55%, which the author notes is improved failure discrimination, not improved control or safety.

#### [FineCraft: Enhancing VLA Models for Fine-Grained Manipulation](https://arxiv.org/abs/2611.03163)
作者 / Authors: Shuaike Zhang, Ziheng Quan, Junhao Ran, Muhe Ding 等(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/eqcy/FineCraft);摘要给出,匿名 ls-remote 验证存在

🇨🇳 细粒度操作需要同时具备指令落地、局部视觉精度与持续执行。FineCraft 为 MetaFine 挑战适配预训练模型:任务路由的策略混合通过统一观测-动作接口选择独立适配的 DINOv2-DiT 或预训练 π0.5 策略,局部视觉特征用于识别被指示的物体部位,示教与专家续写传授所需动作,新观测引导执行中的重规划。综合得分 0.878 排名第四,在五个任务上均超过公布参考。

🇬🇧 Fine-grained manipulation couples instruction grounding, local visual precision and sustained execution. FineCraft adapts pretrained models for the MetaFine Challenge: a task-routed mixture of policies selects independently adapted DINOv2-DiT or pretrained π0.5 policies through a common observation-action interface, local visual features identify instructed object parts, demonstrations and expert continuations teach actions, and new observations guide replanning. It ranks fourth with an overall score of 0.878, exceeding the published reference on all five tasks.

#### [When Delay Meets Drift: Physical Safety of Robot Foundation Models Is a Cross-Layer Problem](https://arxiv.org/abs/2611.02101)
作者 / Authors: Liangkai Liu, Bimal Thapa Magar(机构未在摘要中给出 / affiliation not given in abstract)

开源状态 / Code: ❓ 未知 / Unknown — 无链接(11 页)

🇨🇳 机器人基础模型的安全评测通常一次只扰动一个变量,而物理安全是环境、模型、计算平台与执行相互作用的结果。作者把它形式化为跨层变化传播,并用交互对比衡量联合变化的风险是否大于各自之和。在 pi0.5 VLA 于 LIBERO 的 4,000 个成对闭环回合中,400 ms 推理延迟在训练视角下仅使违规率升高 3.5 个百分点,而在 60 度相机偏移下升高 37 个百分点,比两种效应之和多 33.5 个百分点(95% CI:25–43)。

🇬🇧 Robot foundation models' safety is evaluated one variation at a time, but physical safety emerges from interactions among environment, model, computing platform and execution. The authors formalize cross-layer variation propagation and use an interaction contrast to measure when joint variation creates more risk than the sum of its parts. In 4,000 paired closed-loop episodes of pi0.5 on LIBERO, a 400 ms inference delay raises the safety-violation rate by 3.5 points under the training viewpoint but 37 points under a 60-degree camera shift: 33.5 points (95% CI 25–43) more than the two effects combined.

其余列名 / Others (1 条 / item):[Verifying Test-State Identity in Paired Evaluation of Vision-Language-Action Models](https://arxiv.org/abs/2611.00896)。

另见 / See also: [Beyond Policy Patches (REPAIR)](https://arxiv.org/abs/2611.02777)、[Behavioral Steering of VLAs in the Low-Parameter Regime](https://arxiv.org/abs/2611.00522)(已归入 运动控制·RL / Motion Control · RL);[ODE Policy](https://arxiv.org/abs/2611.01729)(已归入 运动控制·RL / Motion Control · RL)。

## VLN / Vision-Language Navigation

今日 cs.RO 与关键词检索中无严格意义的 VLN 新论文(vision-language navigation / VLN 命中数 0),此处收录两篇导航型具身问答(EQA)诊断工作。

#### [Answering Without Arriving: An Evidence Audit for Embodied Question Answering](https://arxiv.org/abs/2611.01958)
作者 / Authors: Shubh Garg, Divyansh Pandey, Niyati Rawal, Vedant Khandelwal(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 具身问答 / EQA

开源状态 / Code: ❓ 未知 / Unknown — 无链接(19 页)

🇨🇳 具身问答要求智能体导航、观察再回答,但仅看答案准确率无法判断这些是否发生。作者提出多房间基准(200 个测试回合、800 个问题,按路线长度分层)与评估阶梯:固定问题、仅改变提供给回答者的证据(从纯文本探针到闭环智能体再到参考轨迹重放),答案可追溯到符号化记录的观测。闭环视觉-语言智能体在 200 个回合中一次都没到达目标,却答对 45.5%,与同一模型无图像时相差不到 0.1 个点;重放参考轨迹使其升至 57.4%,说明证据存在于路线上但没有被收集;家族级审计显示 8 个家族中有 4 个基本可由文本回答。

🇬🇧 Embodied question answering asks an agent to navigate, observe and answer, but answer accuracy alone cannot show whether this happened. The authors build a multi-room benchmark (200 test episodes, 800 questions stratified by route extent) with an evaluation ladder that holds questions fixed while varying only the evidence supplied (text-only probes, closed-loop agents, reference-trajectory replay), with answers traceable to symbolic observation records. A closed-loop vision-language agent reaches no target in 200 episodes yet answers 45.5%, within 0.1 points of the same model with no images; replaying the reference trajectory raises it to 57.4%, so evidence exists but is not gathered, and an audit shows four of eight question families are largely answerable from text.

#### [Do Embodied VLMs Actually Use Their Scene-Graph Memory?](https://arxiv.org/abs/2611.02056)
作者 / Authors: Shubh Garg, Divyansh Pandey, Vedant Khandelwal, Niyati Rawal(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 具身问答 / EQA

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 具身智能体需要路线记忆,场景图是自然形式,但准确率无法说明图是否真的被模型依赖。作者提出「图交换」测试:给每个回合换上另一回合的图,统计答案变化数,用它比较向微调 VLM 提供场景图记忆的方式。以文本形式提供时记忆被强烈使用(路线问题 +30 点);以图形式提供时没有被使用,原因是标准池化与后融合丢弃了信息,给每个节点独立输入 token 可恢复一部分,路线问题上提升 8.3 点;测试还揭示当同样事实也出现在文本中时模型会忽略图的捷径。

🇬🇧 Embodied agents need route memory and scene graphs are a natural form, but accuracy cannot show whether the graph is relied on. The authors introduce a graph-swap test (give each episode another episode's graph and count changed answers) to compare ways of delivering scene-graph memory to a fine-tuned VLM. As text the memory is used strongly (+30 points on route questions); as a graph it is not, because standard pooled and late fusion discard the information; giving each node its own input token recovers part of it (+8.3 points on route questions, confirmed by the swap test), and the test exposes a shortcut where the model ignores its graph when the same facts appear in the text.

另见 / See also: [SNAP](https://arxiv.org/abs/2611.03498)(RL 导航策略,零样本迁移到足式机器人,已归入 运动控制·RL / Motion Control · RL);[WorldSketch](https://arxiv.org/abs/2611.00513)(含 R2R-CE 导航,保留在世界模型类)。

## 世界模型与 WAM / World Models & WAM

展开 12 条。

#### [OpenNWM: A Generalist Navigation World Model with Latent Action Pretraining](https://arxiv.org/abs/2611.01844)
作者 / Authors: Dujun Nie, Ruiqi Song, Zixuan Wang, Hanqing Wang 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 导航 / Navigation

开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/OpenSpace-Lab/OpenNWM);另有[项目页](https://openspace-lab.github.io/OpenNWM/);Comments 给出,匿名 ls-remote 验证存在

🇨🇳 导航世界模型的泛化受限于带动作标注数据的覆盖。OpenNWM 通过大规模无动作标注视频的视觉预测预训练学习通用潜在动作,再用带动作条件的后训练把潜在动作与物理运动对齐;为此整理了 NavAnywhere 数据集(来自 15 个异构来源、1750 万视觉观测,覆盖地面机器人、人和无人机)。实验显示在域内与域外基准上视觉预测更好,导航性能也有提升(检索到的摘要末尾被截断,未含具体数值)。

🇬🇧 Navigation world models' generalization is limited by the coverage of action-labeled data. OpenNWM learns universal latent actions from large-scale action-free videos through visual-prediction pretraining and aligns them with physical motion via action-conditioned post-training, supported by NavAnywhere, a dataset of 17.5 million observations from 15 heterogeneous sources (ground robots, humans, drones). Experiments show better visual prediction on in-domain and out-of-domain benchmarks and improved navigation performance (the retrieved abstract is cut off before specific numbers).

#### [Seeing Through the Illusion: Test-Time Scaling for World Action Models](https://arxiv.org/abs/2611.03585)
作者 / Authors: Cheikh Ahmed, Mahdi Mostajabdaveh, Milad Yazdani, Zirui Zhou 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: WAM

开源状态 / Code: ❓ 未知 / Unknown — 无链接(CoRL 2026 G2A 研讨会)

🇨🇳 WAM 联合生成动作与想象的未来,但合理的预测不一定被其共同生成的动作实现。WISE 是执行前的选择器,按动作有效性与时间规整度、想象运动与动作的逆动力学一致性、以及指令条件的任务进度为每个采样 rollout 打分,执行得分最高者,WAM 保持冻结。每次决策 4 个候选时,RoboLab 上用 Cosmos 3 Edge 的闭环成功率从 6.0% 升至 24.0%,LIBERO 上用 DreamZero 的平均成功率从 75.1% 升至 78.3%,总体超过最佳已有选择器 4.0 与 0.9 个点。

🇬🇧 World action models jointly generate actions and imagined futures, but a plausible prediction need not be realized by its co-generated action. WISE is a pre-execution selector scoring each sampled rollout on action validity and temporal regularity, inverse-dynamics consistency with the imagined motion, and instruction-conditioned task progress, executing the best candidate with the WAM frozen. With four candidates per decision, closed-loop success rises from 6.0% to 24.0% on RoboLab with Cosmos 3 Edge and from 75.1% to 78.3% on LIBERO with DreamZero, exceeding the best existing selector by 4.0 and 0.9 points.

#### [Gnomon4D: Learning Where and When to Focus for Geometric Motion-Grounded World-Action Modeling](https://arxiv.org/abs/2611.02474)
作者 / Authors: Lingwei Dang, Yan Zhou, Juntong Li, Zhenhao Zhang 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 空间智能 / 4D 几何

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 WAM 的 RGB 未来把物理状态变化与外观纠缠,逐帧深度缺少时间对应,现有 4D 方法把运动隐含在视觉特征中或通过单独接口翻译为动作。Gnomon4D 联合生成未来视频、机器人动作与 GeoDelta(视频对齐的 4D 几何运动场,编码本体与物体点的跨帧图像面位移和深度变化);交互显著性注意力(InSAttn)聚焦任务相关交互区域,转换锚定聚合(TransAgg)围绕抓取/释放等相对运动变化聚合证据。GeoDelta 与本体控制无关,为人-机器人共享的准动作,支持在 EgoManip-5000H 上无动作预训练再在 Robot-30H 上做机器人中期训练;检索到的摘要末尾被截断,未含基准数值。

🇬🇧 RGB futures in WAMs entangle physical change with appearance, frame-wise depth lacks temporal correspondence, and 4D approaches keep motion implicit or translate traces through a separate interface. Gnomon4D jointly generates future video, actions and GeoDelta, a video-aligned 4D geometric motion field encoding image-plane displacement and depth change of embodiment and object points; Interaction-Salient Attention focuses readout on task-relevant interactions and Transition-Anchored Aggregation aggregates evidence around changes in relative motion such as grasp and release. GeoDelta is embodiment-independent, a shared human-robot quasi-action enabling action-free pretraining on EgoManip-5000H and robot mid-training on Robot-30H; the retrieved abstract is cut off before benchmark numbers.

#### [W2A: Distilling World Priors into Action Models for Real-Time Robotic Control](https://arxiv.org/abs/2611.02600)
作者 / Authors: Xiaopeng Zhang, Yongjin Mu, Yueyang Weng, Chengzhi Zhao 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: VLA / 操作

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 WAM 受益于视频模型的未来想象,但测试时显式想象未来带来大量计算和延迟。W2A 是两阶段蒸馏框架:训练时把视频扩散模型的中间去噪表示蒸馏进动作模型,测试时完全丢弃视频模型;假设压缩的低维子空间足以为动作生成提供监督。仿真与真机均取得有竞争力的成功率,LIBERO 平均成功率 95.9%,推理速度比代表性 WAM 基线快约 21 倍。

🇬🇧 WAMs benefit from large video models' future imagination, but explicitly imagining futures at test time adds heavy compute and latency. W2A is a two-stage distillation framework that distills intermediate denoising representations of a video diffusion model into an action model during training and discards the video model at test time, hypothesizing that a compressed low-dimensional subspace suffices to supervise action generation. It achieves competitive success in simulation and real-world settings, 95.9% average on LIBERO, with about 21x faster inference than a representative WAM baseline.

#### [WorldSketch: Sketching World Models for Zero-Shot Mobile Manipulation](https://arxiv.org/abs/2611.00513)
作者 / Authors: Jiaming Wang(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: VLN / 移动操作

开源状态 / Code: ❓ 未知 / Unknown — 无链接(40 页)

🇨🇳 多数智能体机器人系统让 VLM 编排预定义技能或直接生成动作,前者受技能库限制,后者需 VLM 推理精确几何与接触。WorldSketch 让 VLM 构建世界模型而非生成动作:作为智能体主动查询感知工具,构建并视觉验证仅含任务相关物体、交互几何与可能运动的最小运动学世界模型,再由几何规划器在其上联合优化接触与全身运动,并利用执行反馈自我修正。零样本成功率在 RoboCasa 91%、LIBERO-PRO 97%、R2R-CE 导航 76%;RoboCasa 上比次优零样本智能体基线高 58 个百分点(摘要此处被截断)。

🇬🇧 Agentic robot systems use VLMs to orchestrate predefined skills (limited by the skill library) or to generate actions directly (requiring precise geometry and contact reasoning). WorldSketch has the VLM build a world model rather than actions: it queries perception tools to construct and visually validate a minimal kinematic world model of task-relevant objects, interaction geometry and motions, a geometric planner then jointly optimizes contact and whole-body motion, and execution feedback revises the model. Zero-shot success is 91% on RoboCasa, 97% on LIBERO-PRO and 76% on R2R-CE navigation, 58 points above the next-best zero-shot agent baseline on RoboCasa (abstract cut off thereafter).

#### [SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts](https://arxiv.org/abs/2611.01600)
作者 / Authors: Amir Hossain Raj, Xuesu Xiao(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 规划 / Planning

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 杂乱场景中前景物体遮挡目标与可用空间,反应式策略漏掉隐藏约束,穷举搜索代价过高。SCOUT 用以物体为中心的场景表示重建隐藏几何并导出刻画阻挡层级与可达走廊的关系规划状态,由 LLM 提出结构化动作候选,再用学习到的动作条件世界模型通过 MCTS 评估。在 Reveal 与 Placement 任务上优于 VLA 策略、具身智能体和 3D 世界模型,长程任务收益显著,并在杂乱货架的真实机器人操作中验证(摘要未给具体数值)。

🇬🇧 In clutter, foreground objects occlude targets and free space; reactive policies miss hidden constraints and exhaustive search is too costly. SCOUT reconstructs hidden geometry with an object-centric representation to derive a relational planning state (blocker hierarchies, accessibility corridors), has an LLM propose structured action candidates, and evaluates them by MCTS with a learned action-conditioned world model. It outperforms VLA policies, embodied agents and 3D world models on Reveal and Placement tasks, especially long-horizon ones, with real-robot validation on a cluttered shelf (no numbers in the abstract).

#### [ForceLDM: A Force-aware Latent Dynamics Model for Contact-Rich Manipulation](https://arxiv.org/abs/2611.03294)
作者 / Authors: Peiyuan Tang, Yao Li, Xiaodong Zhang, Wuyang Zhang 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 触觉/力 / Force

开源状态 / Code: ❓ 未知 / Unknown — 无链接(NeurIPS 2026)

🇨🇳 纯视觉策略难以从图像推断接触状态与交互力,已有方法把力/触觉作为辅助观测,未利用其对未来交互动力学建模的作用。ForceLDM 不直接预测未来观测(会纠缠无关感知细节),而是通过知识蒸馏学习未来动态的紧凑表示:拥有特权未来力/力矩与光流的教师提取未来动态特征,蒸馏到仅用当前观测的学生,使其无需未来感知输入也能推理即将发生的接触与物理动力学,以指导动作生成(检索到的摘要末尾被截断,未含数值)。

🇬🇧 Vision-only policies struggle to infer contact states and forces, and prior work treats force/tactile signals as auxiliary observations. ForceLDM does not predict future observations (which entangles irrelevant sensory detail) but learns a compact representation of future dynamics through distillation: a teacher with privileged future force/torque and optical flow extracts future dynamic features, distilled into a student using only current observations, so it can reason about upcoming contacts and dynamics to guide action generation (the retrieved abstract is cut off before numbers).

#### [pico-WAM: Evaluating Counterfactual Prediction and Planning Error in a Compact World Action Model](https://arxiv.org/abs/2611.01039)
作者 / Authors: Keivalya Pandya(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: WAM

开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/keivalya/pico-wam);Comments 给出,匿名 ls-remote 验证存在

🇨🇳 WAM 控制失败时,瓶颈是提案生成还是轨迹打分?pico-WAM 是提供物理状态的紧凑模型,用 206 条 Push-T 示教和 15 个训练种子比较数据设定与搜索配置。反事实分支训练改善短时域代价排序,并使策略重启搜索相对热启动搜索的覆盖优势增加 4.8 个百分点;用仿真器代价替换学习的轨迹打分使覆盖提高 12.2 个点,而只替换提案生成中的仿真器状态无可检测增益,表明打分是该设定下有效的改进目标。

🇬🇧 When a WAM fails at control, is the bottleneck proposal generation or trajectory scoring? pico-WAM is a compact model with supplied physical state, studied with 206 Push-T demonstrations and 15 training seeds across data regimes and search configurations. Counterfactual branch training improves short-horizon cost ranking and enlarges the coverage advantage of policy-restarted over warm-started search by 4.8 points; replacing learned scores with simulator costs improves coverage by 12.2 points while substituting simulator states in proposal generation shows no detected gain, identifying scoring as the effective target.

#### [Roz: A Taste Test for World Model Latents](https://arxiv.org/abs/2611.00612)
作者 / Authors: Kenneth Ge, Dhruv Sheth, Kunvar Thaman(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 评测 / Evaluation

开源状态 / Code: ❓ 未知 / Unknown — 无链接(NeurIPS 2026 研讨会)

🇨🇳 最先进的潜动力学世界模型在机器人规划上表现好,但它们是否编码物理?作者表明常见世界模型在可归结为图像相似度的任务上很强,却遗忘物体的质量、形变、摩擦与弹性。Roz 评测含 10 个对比任务和 3 个连续任务,共 1734 个场景,只需模型能接收静帧或视频、提取潜变量并有潜变量间距离函数,单次通过即可运行;在作者自己的 AnonWM 上,性能大体随训练步数提高,但不一定与重建 MSE 相关。

🇬🇧 State-of-the-art latent-dynamics world models perform well at robot planning, but do they encode physics? The authors show popular world models do well on tasks reducing to image similarity but forget object mass, deformation, friction and bounciness. Roz comprises 10 contrastive and 3 continuous tasks (1734 scenarios), needing only a model that ingests frames or video, a latent extractor and a latent distance function, run in one pass; on their own AnonWM, performance roughly improves with training steps without necessarily correlating with reconstruction MSE.

#### [History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models](https://arxiv.org/abs/2611.02782)
作者 / Authors: Hangyi Kuang, Chengzhi Wang, Yefei He, Weijie Wang 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 视频生成 / Video generation

开源状态 / Code: ❓ 未知 / Unknown — 项目页 [ziplab.co 项目页](https://ziplab.co/History-Forcing-Project-Page/);未见代码声明

🇨🇳 少步自回归视频扩散生成高效,但长程 rollout 中主体或场景重新出现时一致性难以保持,现有蒸馏方法未充分利用更丰富的历史信息。History Forcing 是在策略(on-policy)蒸馏框架:用教师在有/无信息性历史上下文时预测的残差解耦历史监督(历史可来自漂移较小的早期生成块,或让场景保持可见的固定视角教师 rollout),加权后加到蒸馏所用的分数或速度预测上形成修正目标。摘要称达到最先进性能(检索到的摘要末尾被截断,未含具体数值)。

🇬🇧 Few-step autoregressive video diffusion is efficient but long rollouts struggle to stay consistent when subjects reappear, and existing distillation does not fully exploit historical information. History Forcing is an on-policy distillation framework that decouples historical supervision using the residual between teacher predictions with and without informative history (earlier less-drifted chunks, or a fixed-view teacher rollout keeping the scene visible), weighted and added to the score/velocity target to form a corrected target. It claims state-of-the-art performance (the retrieved abstract is cut off before numbers).

#### [AgiWorld: An Agentic Video World Model for Building Persistent Worlds](https://arxiv.org/abs/2611.02341)
作者 / Authors: Shaoheng Fang, Yiqun Mei, Hanwen Jiang, Xin Sun 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 空间智能 / Spatial

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 交互式视频世界模型需要低层相机与文本控制,且探索中世界难以保持持久。AgiWorld 由单图与自由指令探索并构建持久世界:AgiWorld-Agent 在世界状态中设计世界与旅程并指挥探索,AgiWorld-WM 逐块生成视频并连同几何存入空间记忆,智能体据此更新世界状态,两层围绕共享空间记忆及度量相机轨迹/结构化提示接口协同设计,并提出处理遮挡与累积几何误差的机制(检索到的摘要末尾被截断,未含数值)。

🇬🇧 Interactive video world models demand low-level camera and text control and struggle to keep the world persistent. AgiWorld builds a persistent world from one image and a free-form instruction: AgiWorld-Agent designs the world and journey in a world state and directs exploration, and AgiWorld-WM generates video chunk by chunk, storing it with geometry in a spatial memory from which the agent updates its state; both levels are co-designed around shared spatial memory and a metric camera-trajectory/structured-prompt interface, with mechanisms for occlusion and accumulated geometric errors (the retrieved abstract is cut off before numbers).

#### [Toward Uncertainty-Aware, Physics-Grounded Human World Models](https://arxiv.org/abs/2611.03428)
作者 / Authors: Yufei Zhang, Zijun Cui(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 人体建模 / Human modeling

开源状态 / Code: ❓ 未知 / Unknown — 无链接(CoRL 2026 UncertainWM 研讨会)

🇨🇳 与人共处的机器人需要关于人的世界模型:对身体状态的信念加动力学预测。本摘要论证两个已发表组件恰好构成这两半并规定如何耦合:KNOWN 实时重建 3D 人体并估计偶然与认知不确定性(11.6 ms/帧),认知项驱动的细化把此类输入误差从 81.3 降到 70.3 mm;PhysMoP 通过求解带学习项的欧拉-拉格朗日方程预测未来身体构型,80 ms 预测误差在 Human3.6M 上从 9.6 降到 2.1 mm,在 3DPW 上从 12.1 降到 0.7 mm。本文是立场摘要,未报告新的实验结果。

🇬🇧 A robot acting around people needs a human world model: a belief over body state and a dynamics model. This abstract argues two published components form these halves and specifies how to couple them: KNOWN reconstructs the 3D body with aleatoric and epistemic uncertainty in real time (11.6 ms/frame), epistemic-driven refinement cutting error on low-density inputs from 81.3 to 70.3 mm; PhysMoP predicts future body configuration by solving Euler-Lagrange equations with learned terms, reducing 80 ms error from 9.6 to 2.1 mm on Human3.6M and from 12.1 to 0.7 mm on 3DPW. It defines the interface, proposes three mechanisms and an evaluation protocol; no new experimental results are reported.

另见 / See also: [Why Koopman Structure Does Not Help Differentiable World Models for Humanoid Whole-Body Tracking](https://arxiv.org/abs/2611.00951)(已归入 运动控制·RL / Motion Control · RL);[Beyond Ensemble Disagreement: Predictive STL Monitoring of RL Locomotion](https://arxiv.org/abs/2611.02218)(已归入 运动控制·RL / Motion Control · RL);[ODE Policy](https://arxiv.org/abs/2611.01729)(已归入 运动控制·RL / Motion Control · RL)。

列名 / Others:[Right Ranking, Wrong Scale: Reproducing the Robotic World Model's Dynamics Model and Testing the Uncertainty of Its Latents](https://arxiv.org/abs/2611.02699)、[Back to the Future: Predicting Long-Horizon Dynamics with Retrospective Correction for Disturbance-Aware Retrieval](https://arxiv.org/abs/2611.02073)、[Gibbs Variational Last Layers for Long-Horizon Dynamics Learning](https://arxiv.org/abs/2611.02891)。本类列名共 3 条 / 3 further items listed.

## 空间智能与 SLAM / Spatial Intelligence & SLAM

展开 6 条。

#### [A Tightly Coupled Magnetic-Inertial SLAM System for Field Robots](https://arxiv.org/abs/2611.03106)
作者 / Authors: Chuan Huang, Tongxing Peng(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 磁惯性 SLAM

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 矿井、隧道与灾区等 GNSS 拒止且相机/LiDAR 受粉尘烟雾影响的场景需要不依赖可见度的定位。MISLAM 用 IMU 与九磁力计阵列做紧耦合磁-惯性 SLAM,不依赖外部里程计:惯性导航模型结合局部多项式磁场模型做短期运动估计,并用全局高斯过程模型通过误差状态卡尔曼滤波做漂移校正。三个室内手持数据集上,总终点闭合误差相对磁惯性里程计降低 45.7%–78.0%;弱光下视觉惯性里程计失效后仍保持跟踪,水平闭合误差 0.332 m,但垂直漂移仍是局限。

🇬🇧 Mines, tunnels and disaster areas need localization independent of visibility under GNSS denial and degraded camera/LiDAR. MISLAM is a tightly coupled magnetic-inertial SLAM system with an IMU and nine-magnetometer array, no external odometry, combining the inertial model with local polynomial magnetic-field models for short-term motion and a global Gaussian-process model for drift correction in an error-state Kalman filter. On three indoor handheld datasets it reduces total endpoint closure error by 45.7%–78.0% versus magnetic-inertial odometry and keeps tracking in poor illumination after visual-inertial odometry fails (0.332 m horizontal closure error), though vertical drift remains a limitation.

#### [SceneBound: How Much Should a Streaming 3D Reconstruction Model Remember?](https://arxiv.org/abs/2611.00756)
作者 / Authors: Ziming Wang, Chuyue Gong, Chutian Wang, Jingmin Zhu 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 3D 重建

开源状态 / Code: ❓ 未知 / Unknown — 无链接(34 页)

🇨🇳 流式 3D 重建模型把过去帧存入循环状态、快速权重或 KV 缓存,每写入一帧都会移动后续相机坐标系或占用显存;免训练规则基于当前帧信号决定写什么,但作者发现写入多少决定平均精度——在均匀间隔帧花费同样预算的无信号规则就能匹配九种已发表门控。SceneBound 仅在预测相机位姿距所有已存关键帧至少固定半径时才写帧,关键帧数量保持在已访问位姿覆盖数的常数倍内,回到原地时保持平稳;在大场景中,当首帧解码再次显示漂移时关闭子图。同一半径用于四个已发布模型和三种记忆类型,在 CUT3R 的循环状态和 StreamVGGT 的 KV 缓存上获得已发表免训练方法中最低的平均轨迹误差。

🇬🇧 Streaming 3D reconstruction models store past frames in a recurrent state, fast weights or a KV cache; each written frame shifts later cameras' frames or uses GPU memory. Training-free rules decide what to write from the current frame, but how much they write explains mean accuracy: spending a gate's update budget at uniformly spaced frames with no signal matches nine published gates. SceneBound writes a frame only when its predicted camera pose is at least a fixed radius from every stored keyframe, keeping the keyframe count within a constant factor of the covering number of visited poses (flat on return), and closes a submap when decoding its first frame reveals drift. With one radius across four released models and three memory types, it achieves the lowest mean trajectory error among published training-free rules in CUT3R's recurrent state and StreamVGGT's KV cache.

#### [A Straight Line Is Not a Camera Pose: Auditing Short-Clip Pose Benchmarks](https://arxiv.org/abs/2611.00482)
作者 / Authors: Xinyi Shi(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 基准审计 / Benchmark audit

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 ATE 是从 SLAM 到前馈 3D 重建的标准相机运动精度指标,但在常见的 Sintel 协议上,不使用图像的匀速直线的平均 ATE 低于 11 个近期模型中的 10 个(官方代码重跑)。原因有二:对齐会把任何匀速预测映射到真实路径的最佳拟合直线,故直线得分反映路径回归残差,残差信噪比判据可预测 95% 的 1056 个模型-片段对(留出 792 对为 98%,ScanNet 1034 对为 97%);位置对齐忽略相机朝向,把轨迹相对朝向旋转 30 度 ATE 不变但静态点重投影变差。结论:更低的 ATE 未必意味着更好的几何。

🇬🇧 ATE is the standard camera-motion metric from SLAM to feed-forward 3D reconstruction, yet on the common Sintel protocol a constant-velocity straight line using no images has lower mean ATE than 10 of 11 recent models re-run with official code. Alignment maps any constant-velocity prediction onto the best-fitting line through the true path, so the line scores the path's regression residual, and a residual-SNR criterion predicts the outcome for 95% of 1056 model-clip pairs (98% of 792 held-out, 97% of 1034 ScanNet pairs); position-only alignment also ignores where cameras look, so rotating a trajectory 30 degrees against its orientations leaves ATE unchanged but worsens static-point reprojection. A lower ATE need not mean better geometry.

#### [Lie Routing Vision Language Models for View-Robust 3D Understanding](https://arxiv.org/abs/2611.02306)
作者 / Authors: Jingjun Yi, Chen Hu, Qi Bi, Hao Zheng(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 空间推理 / Spatial reasoning

开源状态 / Code: ❓ 未知 / Unknown — 无链接(NeurIPS 2026)

🇨🇳 MLLM 做多视角 3D 场景理解时,同一物体与查询在不同视角下会得到不一致响应(视角诱导语义漂移)。LieVLM 是 Lie 路由框架:在学习的三维子空间内对投影特征施加局部 SO(3) 变换,由 VGGT 提取的几何 token 预测局部旋转参数与通道级路由系数,经闭式 Padé–Cayley 映射变换视觉特征,并把恒等相对修正门控回原视觉/几何特征。在 3D 描述、定位、检测与空间推理上,相对加性融合在不同训练规模和骨干上取得一致提升(检索到的摘要末尾被截断,未含数值)。

🇬🇧 MLLMs for multi-view 3D understanding give inconsistent responses to the same object and query across viewpoints (viewpoint-induced semantic drift). LieVLM applies local SO(3) transformations to projected features within learned three-dimensional subspaces, with VGGT geometry tokens predicting rotation parameters and channel-wise routing coefficients, a closed-form Padé–Cayley map, and identity-relative corrections gated back into the original visual and geometry features. It shows consistent improvements over additive fusion on 3D captioning, grounding, detection and spatial reasoning across training scales and backbones (the retrieved abstract is cut off before numbers).

#### [OctreeSplat: Hierarchical Octree-Guided Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2611.02658)
作者 / Authors: Yibin Zhao, Yihan Pan, Wenli Yang, Jun Nan(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: Gaussian Splatting

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 前馈 3DGS 免于逐场景优化,但固定图像或空间分辨率限制按局部复杂度分配基元。OctreeSplat 从冻结的视觉基础模型提取多视角特征与几何先验,构建层次八叉树并预测致密化分数,使高斯基元按局部复杂度以不同密度分配;随机实体体渲染改善深度渲染并支持表面重建,有相机参数时可选测试时优化。训练仅更新 7600 万附加参数、需 35 GPU 小时;在 Replica、TUM、Tanks and Temples 与 DTU 上 RGB 视图合成、深度合成与表面重建有竞争力,同时减少高斯基元数量。

🇬🇧 Feed-forward 3DGS avoids per-scene optimization but fixed image or spatial resolution limits allocating primitives by local complexity. OctreeSplat extracts multi-view features and geometric priors from a frozen visual foundation model, builds a hierarchical octree and predicts densification scores so Gaussians are allocated at spatially varying density; stochastic solids volume rendering improves depth and supports surface reconstruction, with optional test-time camera optimization. Training updates only 76M extra parameters in 35 GPU-hours; it is competitive on RGB view synthesis, depth synthesis and surface reconstruction on Replica, TUM, Tanks and Temples and DTU while reducing the number of Gaussians.

#### [A Reproducible Reconstruction and Evaluation Framework for Photorealistic Lunar Analog Scene Reconstruction Toward Digital Twins](https://arxiv.org/abs/2611.00870)
作者 / Authors: Antar Mazumder, Ryan Hartzell, Luke Boyd, Alexander Robinson 等(机构未在摘要中给出 / affiliation not given in abstract)
🏷️ 交叉方向 / Also: 数字孪生 / Digital twin

开源状态 / Code: ❓ 未知 / Unknown — 无链接

🇨🇳 作者构建重建流水线,量化月面类比场景在漫游车桅杆相机单目输入下的照片级重建精度,并考察运动模糊、扬尘雾霾、轨迹偏置和稀疏视角等月面行驶效应。先在三个月面类比场景的留出集上基准测试六种 3DGS 变体,再发现测试集 NVS 性能不会按比例转化为重建数字孪生中的同类指标;单靠 splat 训练指标不足以预测跨重建的照片级 NVS 保真度,轨迹偏置与几何场景覆盖起关键作用。还试点基于 COLMAP 位姿与点云结构的覆盖得分 S_c 作为可达最高保真度的启发式诊断(摘要末尾被截断)。

🇬🇧 The authors present a reconstruction pipeline quantifying photorealistic scene reconstruction accuracy from rover mast-camera monocular feeds against physical ground truth as a function of lunar traversal effects (motion blur, lofted-regolith haze, trajectory bias, sparse views). They benchmark six 3DGS variants across three lunar-analog scenes, then show test-set NVS performance does not scale proportionally to the same metrics in reconstructed digital twins: splat training metrics alone do not predict cross-reconstruction photorealistic fidelity, and trajectory bias and geometric coverage matter. A pilot Coverage Score S_c from COLMAP poses and point-cloud structure is proposed as a diagnostic of achievable fidelity (abstract cut off thereafter).

列名 / Others (2 条 / items):[4D Triangle Splatting Reconstruction of Dynamic Endoscopic Scenes from Monocular Videos](https://arxiv.org/abs/2611.02034)、[MoSoLoco: Monocular 3D Human Localization through Visual Latent Features and Social Context](https://arxiv.org/abs/2611.03189)。GitHub 侧另有 SLAM 新仓库 [VCS-SLAM](https://github.com/jhakrraman/VCS-SLAM)(RAL 2026 官方实现,1 star,见下)。

## 其他值得关注 / Other Notable

- 分类自查:已逐条检查被归入类别 3–7 的条目(RoboColosseum、Auriga、uni-robot-agent、MOST、D&A、CUE;JADE、PTS、VLALagBench、Reflex、HeLM、PREM、Route-Guided CBF-QP、CalVLA、FineCraft、When Delay Meets Drift;EQA 两篇;OpenNWM、WISE、Gnomon4D、W2A、WorldSketch、SCOUT、ForceLDM、pico-WAM、Roz、History Forcing、AgiWorld、Human World Models;MISLAM、SceneBound 等)。其中 W2A、Gnomon4D、WISE、ForceLDM 的贡献为操作类 WAM/动力学模型而非运动控制/locomotion/全身控制;WorldSketch 的主要贡献是 VLM 构建运动学世界模型,全身运动优化为其下游规划器;均无人形/足式 locomotion 或动作跟踪的控制策略 RL 训练,故保留。未发现需移动的错归。
- Replacements 中与运动控制相关、值得下期关注的旧稿更新(仅按标题,未评估更新内容):[OpenHLM](https://arxiv.org/abs/2606.22174)、[ROOF](https://arxiv.org/abs/2610.42097)、[HumiMimic](https://arxiv.org/abs/2610.36615)、[DiffContact](https://arxiv.org/abs/2610.35852)。
- 本期未展开的相关但低优先级条目共约 25 条(多为触觉传感器、软体/外骨骼硬件、群体/多机器人、手术与自动驾驶),按规则不列入。

## GitHub 动态 / GitHub Highlights

### 星标增长较明显的相关仓库 / Star Growth (相对 2026-11-02T23:13Z 快照)

| 仓库 / Repo | ⭐ | 24h Δ | 说明 / Note |
|---|---|---|---|
| [kornia/kornia](https://github.com/kornia/kornia) | 12,311 | +195 | 几何计算机视觉库(Spatial AI);Geometric CV library |
| [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) | 463 | +25 | SuperMimic 实现/扩展的精选列表(第三方,2026-10-26 创建);curated third-party SuperMimic list |
| [TianxingChen/Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide) | 16,832 | +24 | 具身智能技术指南;Embodied AI guide |
| [datawhalechina/every-embodied](https://github.com/datawhalechina/every-embodied) | 4,355 | +20 | 从零构建具身机器人/VLA 教程;from-scratch VLA tutorial |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 14,522 | +19 | π 系 VLA 开源实现;openpi VLA |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28,666 | +18 | 端到端机器人学习库;robot learning library |
| [Ropedia/ropedia-w0](https://github.com/Ropedia/ropedia-w0) | 225 | +16 | 跨本体 loco-manipulation 世界模型;cross-embodiment loco-manipulation world models |
| [Vottivott/microduck-playground](https://github.com/Vottivott/microduck-playground) | 89 | +13 | Microduck RL 实验与策略;reproducible Microduck RL experiments |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 16,052 | +14 | 物理仿真器;physics simulator |
| [TencentARC/Looking-Ahead](https://github.com/TencentARC/Looking-Ahead) | 205 | +12 | 自回归视频生成中的未来演化建模;future evolution in AR video generation |
| [Junchao-cs/SolarWM](https://github.com/Junchao-cs/SolarWM) | 849 | +10 | 长程视频世界模型的开源数据与训练;long-horizon video world models |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 8,564 | +10 | 机器人学习框架;robot learning framework |
| [groundingpi/GroundingPI](https://github.com/groundingpi/GroundingPI) | 306 | +9 | 4B 物理智能 grounding 基础模型;4B grounding model for physical intelligence |

另有 [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view)(+241)与 [ruvnet/RuView](https://github.com/ruvnet/RuView)(+135)因 "spatial-intelligence" 话题命中,实为地理空间/Wi-Fi 感知项目,与机器人无关(噪声)。

### 新仓库(48h)/ New Repos(已筛选)

- [fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic)(99 ⭐,2026-11-02 创建):Unitree G1 全身动作跟踪,声称单卡约 3 分钟训练;topics 含 supermimic、world-model、mjlab。**第三方实现,非 SuperMimic 官方代码**。匿名 ls-remote 存在。 / Third-party whole-body motion tracking for G1 in ~3 min on one GPU, SuperMimic-tagged; not the official release.
- [ApurvK032/pi-wbc](https://github.com/ApurvK032/pi-wbc)(0 ⭐):Isaac Lab 中 PPO teacher-student 的 G1 全身控制器,sim-to-sim(PhysX/MuJoCo)6.6 万回合无摔倒(无踢扰动);个人项目。
- [GGbao-114/pi-plus-beyondmimic-sim2sim](https://github.com/GGbao-114/pi-plus-beyondmimic-sim2sim)(0 ⭐):BeyondMimic 人形动作模仿与 Isaac Sim↔MuJoCo 跨引擎验证。
- [DavidLXu/Revo3-Ball-Locomotion](https://github.com/DavidLXu/Revo3-Ball-Locomotion)(0 ⭐):灵巧手球上运动(MjLab GPU PPO,含预训练策略)。
- [cochon123/robot-badminton](https://github.com/cochon123/robot-badminton)(0 ⭐):两条 G1 手臂在 MuJoCo 中学习打羽毛球。
- [SIPAIR-Elastic/DexArena](https://github.com/SIPAIR-Elastic/DexArena)(2 ⭐):对应论文 DexArena 基准。
- [jhakrraman/VCS-SLAM](https://github.com/jhakrraman/VCS-SLAM)(1 ⭐):RAL 2026,可见性一致语义融合的 3DGS SLAM 官方实现。
- [BrunooCS/space-aware-world-models](https://github.com/BrunooCS/space-aware-world-models):"Space-Aware World Models" 官方 PyTorch 实现(0 ⭐)。
- [sudsho/vla-goal-representation](https://github.com/sudsho/vla-goal-representation):VLA 目标表示定位与编辑代码(SPAIS 研讨会,0 ⭐)。
- 其余新仓库多为个人作业/课程/硬件项目或空壳,未列入。 / The remaining new repos are mostly personal coursework, hardware hobby projects or marketing; omitted.

### 新 Release / New Releases

窗口内 watchlist(LeRobot、openpi、Isaac Lab、MuJoCo、GR00T、Genesis、ManiSkill、ORB-SLAM3、VGGT 等)**无新 release**(radar `watchlist_releases` 为空,counts.releases = 0)。 / No new releases in the window.

## 今日趋势 / Today's Trends

**1. 围绕可微世界模型 SuperMimic 的快速跟进。** 监测项 SuperMimic 官方代码仍未出现,但社区已出现多个第三方实现与整理([blinkmimic](https://github.com/fuyichen0725/blinkmimic)、[awesome-supermimic](https://github.com/miao-org/awesome-supermimic)),论文侧 [Koopman 负面结果](https://arxiv.org/abs/2611.00951) 与 [ODE Policy](https://arxiv.org/abs/2611.01729) 都以 SuperMimic 为对照或加速对象。 / Although no official SuperMimic code has appeared, third-party implementations and curated lists are emerging, and both the Koopman negative result and ODE Policy use SuperMimic as a baseline or speed-up target.

**2. 人形全身控制从「跟踪」走向「精度、顺应、感知」。** [Anchor 1](https://arxiv.org/abs/2611.00193)(精度)、[CompliantBot](https://arxiv.org/abs/2611.01748)(顺应)、[ReGATE](https://arxiv.org/abs/2611.02871)(视觉融合)、[Dodgeball](https://arxiv.org/abs/2611.01197)(单目感知闪避)和 [MAPO](https://arxiv.org/abs/2611.02613)(MoE 策略优化)覆盖了控制器的不同短板。 / Humanoid whole-body control is moving beyond tracking toward precision, compliance and perception, as shown by Anchor 1, CompliantBot, ReGATE, the dodgeball system and MAPO.

**3. VLA 的部署延迟与安全成为独立问题。** [PTS](https://arxiv.org/abs/2611.01390)、[VLALagBench](https://arxiv.org/abs/2611.03103)、[Reflex](https://arxiv.org/abs/2611.00524)、[When Delay Meets Drift](https://arxiv.org/abs/2611.02101) 同期讨论推理延迟,[Route-Guided CBF-QP](https://arxiv.org/abs/2611.01713) 与 [CalVLA](https://arxiv.org/abs/2611.00394) 讨论安全与失败预测。 / VLA inference latency and safety are becoming their own topics (PTS, VLALagBench, Reflex, Delay-Meets-Drift; Route-Guided CBF-QP, CalVLA).

**4. WAM 向「推理期更便宜、选择更可靠」演进。** [W2A](https://arxiv.org/abs/2611.02600) 蒸馏掉视频模型(约 21 倍加速),[WISE](https://arxiv.org/abs/2611.03585) 做测试时候选选择,[pico-WAM](https://arxiv.org/abs/2611.01039) 诊断打分瓶颈,[Gnomon4D](https://arxiv.org/abs/2611.02474) 加入 4D 几何运动。 / WAMs are becoming cheaper and more reliable at inference time: W2A distillation, WISE selection, pico-WAM diagnostics, Gnomon4D geometry.

**5. 「智能体 harness + 开放模型」与评测审计。** [Auriga](https://arxiv.org/abs/2611.01112) 与 [uni-robot-agent](https://arxiv.org/abs/2611.01560) 在 RoboDojo 上用 VLM 智能体 harness 超过许多 VLA/WAM 基线;[RoboColosseum](https://arxiv.org/abs/2611.02497) 与 [ATE 审计](https://arxiv.org/abs/2611.00482) 则质疑现有评测。 / Agent harnesses over (open) VLMs now beat many VLA/WAM baselines on RoboDojo, while RoboColosseum and the ATE audit question current evaluations.

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
1. `control barrier function` / `CBF`(arXiv 检索 + GitHub topic):今日 4 篇(中文:安全滤波成为跨方向共性;English: safety filtering is a cross-cutting theme)——[Neural Integral CBF](https://arxiv.org/abs/2611.02626)、[Latent-Space CBF Planning](https://arxiv.org/abs/2611.01814)、[Route-Guided CBF-QP](https://arxiv.org/abs/2611.01713)、[Safe-Ballbot](https://arxiv.org/abs/2611.03307)。
2. `VLA inference latency` / `asynchronous execution`(arXiv 检索):4 篇同日出现(中文:VLA 部署效率成为新问题;English: VLA deployment efficiency is an emerging topic)——[PTS](https://arxiv.org/abs/2611.01390)、[VLALagBench](https://arxiv.org/abs/2611.03103)、[Reflex](https://arxiv.org/abs/2611.00524)、[Delay Meets Drift](https://arxiv.org/abs/2611.02101)。
3. `SuperMimic`(GitHub 关键词/topic;arXiv 已有监测):radar 中出现 [blinkmimic](https://github.com/fuyichen0725/blinkmimic)、[awesome-supermimic](https://github.com/miao-org/awesome-supermimic) 等衍生仓库,另有 search_hits 中 supermimic_rl、MPS-Supermimic-Playground(中文:追踪衍生生态;English: track the derivative ecosystem)。

**建议观察 / Watch**
4. `agent harness` / `robot-use agent` / `RoboDojo`:2 篇([Auriga](https://arxiv.org/abs/2611.01112)、[uni-robot-agent](https://arxiv.org/abs/2611.01560))同时出现,信号尚弱,再看几天(中文/English: two papers on the same leaderboard, weak signal so far)。

**建议移除/收窄 / Remove or Narrow**
5. GitHub 关键词 `SLAM`:命中 [BTS SIO SLAM](https://github.com/roytitli-pro/roytitli-pro.github.io) 等无关教学仓库(中文:建议收窄为 `visual SLAM`/`LiDAR SLAM`/`gaussian splatting SLAM`;English: narrow to visual/LiDAR/Gaussian-splatting SLAM to avoid school-course noise);同样 `spatial intelligence` 命中地理空间/Wi-Fi 项目 [gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view)、[RuView](https://github.com/ruvnet/RuView)。

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 / Added | 当前状态 / Status | 今日检查结果 / Today | 备注 / Notes |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 / Unknown | signal=false;candidate_repos 空;project_page_github_links、project_page_release_claims、arxiv_github_links 均为空;arXiv 最新版 v1;errors 空 | 无官方代码、无开源承诺。search_hits 仅为第三方:[Yukikaze2233/supermimic_rl](https://github.com/Yukikaze2233/supermimic_rl)(轮足机器人 PPO + 可微世界模型)、[chenmuller19/MPS-Supermimic-Playground](https://github.com/chenmuller19/MPS-Supermimic-Playground)(Apple Silicon 实现,4 ⭐),以及 [blinkmimic](https://github.com/fuyichen0725/blinkmimic)、[awesome-supermimic](https://github.com/miao-org/awesome-supermimic);均不能据此判定已开源 |

**建议加入监测 / Suggested additions**

1. **Anchor 1** — 运动控制·RL 的高价值人形全身操作控制器,真机跟踪误差降低 30%–80%,但无任何开源线索。 / A high-value humanoid whole-body manipulation controller with 30%–80% lower real-world tracking error and no release signal yet.
```json
{"name": "Anchor 1", "title": "Anchor 1: Precise and Stable Humanoid Control for Whole-Body Manipulation", "arxiv_id": "2611.00193", "added": "2026-11-04", "status": "unknown", "search_terms": ["Anchor 1 humanoid", "Archon Robotics"], "owners": [], "project_pages": [], "known_repos": [], "notes": "Archon Robotics; whole-body manipulation controller + benchmark"}
```
2. **MAPO** — CoRL 2026 的通用人形动作跟踪方法,已有项目页,值得追踪代码是否随后发布。 / A CoRL 2026 universal humanoid motion tracker with a project page; worth watching for code.
```json
{"name": "MAPO", "title": "MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking", "arxiv_id": "2611.02613", "added": "2026-11-04", "status": "unknown", "search_terms": ["MAPO humanoid motion tracking"], "owners": [], "project_pages": ["https://mapo-corl2026.github.io/MAPO/"], "known_repos": [], "notes": "CoRL 2026"}
```
3. **GoalDex** — 摘要提到代码发布信息见项目页,灵巧手内操作 sim-to-real,值得确认何时放出仓库。 / The abstract points to a project page for code release; a dexterous in-hand sim-to-real work worth confirming.
```json
{"name": "GoalDex", "title": "GoalDex: Learning Image-Goal-Conditioned Policies for Dexterous In-Hand Manipulation", "arxiv_id": "2611.02171", "added": "2026-11-04", "status": "planned", "search_terms": ["GoalDex"], "owners": ["leggedrobotics"], "project_pages": ["https://rffr.leggedrobotics.com/works/goaldex/"], "known_repos": [], "notes": "project page says videos and code release; owner account inferred from project-page domain, unverified"}
```

**建议移出 / Suggested removals**:无 / None.
