# 机器人/具身智能每日速递 — 2026-11-13 / Robotics & Embodied AI Daily — 2026-11-13

## 🔔 监测项已开源 / Watchlist Item Released

**[SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](https://arxiv.org/abs/2610.28480)(CoRL 2026 Oral,UC Berkeley Hybrid Robotics)官方代码已公开,今天是第 3 天跟进 / Official code is public; this is the third day of follow-up.**

- **仓库 / Repo**:[HybridRobotics/supermimic](https://github.com/HybridRobotics/supermimic) 现有 **1,302★**(昨日 1,019,一天约 +283);匿名 `git ls-remote` 可访问,HEAD 仍为 `abc124c1`,与昨日相同,没有新提交。配套依赖 [HybridRobotics/mjlab_research](https://github.com/HybridRobotics/mjlab_research) 有 37★(昨日 16)。 / 1,302 stars (+~283 in a day); HEAD unchanged at `abc124c1`; the mjlab_research dependency grew from 16 to 37 stars.
- **发现来源 / Found via**:radar `oss_watch` signal=true;candidate_repos 是 `HybridRobotics/supermimic`(known_repo + owner:HybridRobotics)和 `HybridRobotics/mjlab_research`(owner:HybridRobotics)。errors 为空。
- **开源内容 / What is released**:README 未变:包含两个 G1 任务(`SuperMimic-GenCoord-G1`、`SuperMimic-MaxCoord-G1`)的世界模型与策略训练脚本、回放脚本,以及配套的 mjlab 分支。**仍没有预训练权重**,play 脚本从 W&B run 路径加载自己训练的模型。 / Training and playback code for both G1 tasks plus the mjlab fork; still no pretrained weights.
- **社区动态 / Community**:作者账号以外按名称搜到的 search_hits 增至 15 个,其中 11-11 以后新建 6 个,都是第三方复现或笔记,例如 [luckylhf/Dex-SuperMimic](https://github.com/luckylhf/Dex-SuperMimic)(29 自由度全身跟踪基线)和 [uwvwko-zzz/go2w-supermimic](https://github.com/uwvwko-zzz/go2w-supermimic)(29★,轮足 Go2-W 盲走上下 20 cm 台阶)。另外 [NTUMARS/ODE-POLICY](https://github.com/NTUMARS/ODE-POLICY) 新增了把 ODE 策略用作 SuperMimic actor 的分支(见下文)。 / Search hits rose to 15, all third-party; ODE Policy ships a branch that uses its actor inside SuperMimic.
- **建议 / Suggestion**:继续建议将 SuperMimic 移出监测列表(列表文件中仍为 `unknown`)。 / Still recommend removing it from the watchlist.

---

## 检查窗口与来源状态 / Window & Source Status

- **窗口 / Window**:台北时间 2026-11-12 07:40 – 2026-11-13 07:40(UTC 2026-11-11 23:40 – 11-12 23:40)。周五,不需要覆盖周末。 / Friday run; no weekend catch-up needed.
- **arXiv cs.RO 列表 / list**:**今日没有新列表 / No new listing today.** [cs.RO new](https://arxiv.org/list/cs.RO/new) 仍显示 "new listings for Wednesday, 11 November 2026"(New 57 + Cross 12 + Replacements 42 = 111 条),这和昨日报告用的是同一份列表。cs.AI、cs.CV、cs.LG 的 new 页面以及 cs.RO pastweek 也停在 Wed 11 Nov。用脚本核对,列表中 68 个 ID 已出现在昨日报告里,其余条目昨日已逐条判定为无关。因此**今日 arXiv 没有新论文可展开**。 / The listing is still Wednesday 11 Nov, already fully covered yesterday; Thursday's announcement had not appeared at run time.
- **arXiv API 关键词检索 / keyword search**(cs.RO/cs.AI/cs.LG/cs.CV,按 submittedDate 降序,每词取 30 条,只保留 published ≥ 2026-11-11T23:40Z):embodied 0、VLA 0、vision-language-action 0、VLN 0、vision-language navigation 0、humanoid 0、legged locomotion 0、whole-body control 0、model predictive control 0、reinforcement learning robot 0、sim-to-real 0、dexterous manipulation 0、robot foundation model 0、world model 0、world action model 0、WAM 0、video world model 0、spatial intelligence 0、spatial reasoning 0、SLAM 0、visual SLAM 0、LiDAR SLAM 0、gaussian splatting SLAM 0、3D reconstruction 0、motion tracking 0、motion imitation 0。**所有关键词在窗口内的命中都是 0**:API 中最新的提交时间是 2026-11-10T18:47Z([2611.14488](https://arxiv.org/abs/2611.14488)),已在昨日报告中。按 lastUpdatedDate 排序的 cs.RO 前 40 条也都早于窗口。 / All keywords returned 0 in-window hits; the newest API submission (11-10 18:47Z) was already covered.
- **入选与摘要 / Selected & abstracts**:没有新论文入选。为了核实今日的开源状态变化,我用 arXiv API(`id_list`,https)取回 4 篇论文的完整摘要与 Comments(2611.14135、2611.13766、2611.01729、2610.28480),**摘要全部非空**;其中 3 篇 Comments 非空。 / No new papers; 4 abstracts fetched to verify code-status changes, all non-empty.
- **GitHub radar**:`data/latest.json` 的 date_taipei = 2026-11-13(**已更新**,生成于 2026-11-12 23:12 UTC)。new_repos 有 150 条(总计 278),其中 143 条未在昨日报告出现,逐条筛选后保留下文几条。star_growth_top 有 60 条(基准快照 2026-11-11 23:13 UTC)。watchlist_releases 有 2 条:MuJoCo 4.0.1 和 Newton v1.8.0,两者都在台北时间 11-11 23:47–23:53 发布,**早于本窗口,而且昨日已报告**。oss_watch 有 1 条(signal=true)。 / Radar is fresh; the two releases predate the window and were reported yesterday.
- **Hugging Face Daily Papers**:API 可访问,返回 100 条。相关且带 githubRepo、此前未报告代码的有 2 条:[FAME-QP](https://github.com/santoshrajkumar/fame-qp) 和 [ODE Policy](https://github.com/NTUMARS/ODE-POLICY),这两项的开源状态需要更新。其余相关条目(LingBot-Touch、SWAM、RoboScript、Embodied First Exam、LEASH、ExRL、memory-clock 等)此前已报告。 / Two new code links found (FAME-QP, ODE Policy).
- **仓库核验 / Repo checks**:用匿名 `git ls-remote` 验证了 8 个仓库,**全部可访问**(supermimic、mjlab_research、fame-qp、ODE-POLICY、Sim3-TurboReg、blinkmimic、a2-mjlab、grail)。我还读取了这些仓库及 Compass、DexSeed、robot-weight-debugging、SO-ARM102、BWM-Forge 的 README。 / All 8 claimed repos reachable anonymously.
- **推送权限 / Push**:`git push --dry-run origin HEAD:main` 通过。

---

## 今日必读 / Top Picks

> 今日 arXiv 没有新列表,下面挑的是今天**开源状态出现变化**或**新放出代码**的工作。 / With no new arXiv listing, picks are works whose code status changed today.

1. **[ODE Policy: Robot Learning via Action Dynamics, Not Actions](https://arxiv.org/abs/2611.01729)**(运动控制·RL / Motion Control · RL,✅)— 🇨🇳 11-04 报告时标为"未知",现在确认官方代码已完整公开,包括仿真、π0.5 动作头、G1 真机,以及 **SuperMimic 世界模型 RL actor** 分支,是今天最值得上手的运动控制代码。 / 🇬🇧 Previously "Unknown"; the full official code is now confirmed public, including sim, π0.5 head, real G1 and a SuperMimic world-model-RL actor branch.
2. **[FAME-QP: A GPU-Accelerated Quadratic-Programming Solver for Real-Time Model Predictive Control](https://arxiv.org/abs/2611.13766)**(运动控制·传统 / Motion Control · Classical,✅)— 🇨🇳 昨日标为"未知",今天确认已发布 PyPI 包和完整仓库。README 给出 G1 推扰恢复 MPC 比 ReLU-QP 快 2.3–3.1 倍。 / 🇬🇧 Previously "Unknown"; now a PyPI package and repo, 2.3–3.1x faster than ReLU-QP on G1 push-recovery MPC.
3. **[Sim(3)-TurboReg: Robust and Efficient Scale-Aware Registration via Tri-Scale Consistency](https://arxiv.org/abs/2611.14135)**(空间智能与 SLAM / Spatial Intelligence & SLAM,✅)— 🇨🇳 给 VGGT/DA3 等前馈 3D 基础模型的流式重建提供即插即用的 Sim(3) 对齐后端,KITTI 上 ATE 降低 22.2%,代码已开源。 / 🇬🇧 A drop-in Sim(3) alignment backend for streaming feed-forward 3D reconstruction (−22.2% ATE on KITTI), with code.
4. **[SuperMimic 官方代码 / official code](https://github.com/HybridRobotics/supermimic)**(运动控制·RL / Motion Control · RL,✅)— 🇨🇳 一天又涨约 283★,第三方复现已扩展到 29 自由度人形和轮足机器人,但官方仍未发布权重。 / 🇬🇧 +~283 stars in a day; third-party ports now reach 29-DoF humanoids and wheeled-legged robots; still no official weights.

---

## 运动控制·RL / Motion Control · RL(今日无新论文;开源状态更新 1 条 / no new papers; 1 code-status update)

### [ODE Policy: Robot Learning via Action Dynamics, Not Actions](https://arxiv.org/abs/2611.01729) — 作者:Jindou Jia, Jingliang Li, Kuangji Zuo, Tuo An 等(NTU MARS Lab)
🏷️ 交叉方向 / Also: VLA / VLA, 世界模型与 WAM / World Models & WAM
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/NTUMARS/ODE-POLICY);匿名可访问,Apache-2.0,[项目页](https://ntumars.github.io/ODE/)。**状态变化:11-04 报告为 ❓ 未知**(当时 arXiv Comments 只有 "35 pages, 23 figures")。今天通过 HF Daily Papers 的 githubRepo 字段发现了仓库。README News 写明 2026-10-28 已发布代码,11-09 又把默认求解器改为 Euler(8 步动作块在 LIBERO 上生成耗时 5.7 ms)。
- 🇨🇳 问题:多数模仿学习/强化学习策略逐步预测动作值,动作连续性只能隐式学到,轨迹容易跳变。方法:ODE Policy 用神经 ODE 学习"动作的动力学",也就是动作向量场。模仿学习时匹配短动作块,强化学习时匹配单步;另加一个轻量多样性头来捕获多模态;部署时从上一个动作开始积分,所以轨迹天然连续。它可以单独作为视觉运动策略,也可以作为 VLA/WAM 的动作头或基于模型 RL 的 actor。结果(摘要):在模仿学习中,与 flow matching 相比,训练 1 个 epoch 后成功率提高到 5.9 倍、泛化 5.4 倍、模式平衡 3.9 倍,动作生成快 10.8 倍;在 14 个真机任务(单臂、双臂、灵巧手、人形)上成功率最高;在强化学习中,它加速了 SuperMimic 人形动作跟踪的训练,动作也更平滑。代码按分支组织:`main` 是仿真和 10 个模仿学习基线,另有 `wam-imagewam`、`real-g1`(GR00T + SONIC 全身控制 + 灵巧手)、`real-r1lite`、`vla-pi05`(替换 openpi 的 flow-matching 动作专家),以及 `rl-supermimic`(在 LAFAN1 上做 G1 全身跟踪,附 PPO 基线)。
- 🇬🇧 Problem: most IL/RL policies predict per-step action values, so motion continuity is learned only implicitly and trajectories can jump. Method: ODE Policy learns the dynamics of the action with a neural ODE vector field, matched over short chunks in IL and single steps in RL. A lightweight diversity head captures multimodality, and each action is integrated from the previous one, so trajectories are continuous by construction. It can serve as a visuomotor policy, a VLA/WAM action head, or a model-based-RL actor. Results (abstract): versus flow matching in IL, after one epoch it reaches 5.9x success, 5.4x generalization and 3.9x mode balance, with 10.8x faster action generation; it has the best success on 14 real-world tasks spanning single-arm, dual-arm, dexterous and humanoid robots; and in RL it speeds up SuperMimic humanoid motion tracking with smoother actions. The release has separate branches for sim and baselines, ImageWAM, real G1 (GR00T + SONIC whole-body control), R1 Lite, a π0.5 ODE head, and a SuperMimic RL actor on LAFAN1 with a PPO baseline.

> 🇨🇳 今日 arXiv 没有新的运动控制·RL 论文。GitHub 侧的相关新仓库(第三方 a2-mjlab、blinkmimic 等)见「GitHub 动态」。 / 🇬🇧 No new RL-control papers today; related new repos are listed under GitHub Highlights.

---

## 运动控制·传统 / Motion Control · Classical(今日无新论文;开源状态更新 1 条 / no new papers; 1 code-status update)

### [FAME-QP: A GPU-Accelerated Quadratic-Programming Solver for Real-Time Model Predictive Control](https://arxiv.org/abs/2611.13766) — 作者:Santosh Mohan Rajkumar, Debdipta Goswami, Stephanie Stockar(Ohio State University 团队)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/santoshrajkumar/fame-qp);匿名可访问,MIT 协议,已发布 PyPI 包 `fame-qp`,附 [项目页](https://santoshrajkumar.github.io/proj/fame_qp/)。**状态变化:昨日报告为 ❓ 未知**(arXiv Comments 为空)。今天通过 HF Daily Papers 的 githubRepo 字段确认;仓库 11-10 创建,在 radar new_repos 中有 8★。
- 🇨🇳 问题:线性 MPC 每个控制周期都要求解稠密二次规划(QP),现有 GPU 求解器的延迟仍然偏高,难以满足人形机器人这类 2 ms 级的控制周期。方法:FAME-QP 基于 ADMM 并预先求逆线性系统。只作用于单个变量的约束(如输入上下界)按元素处理,不当作稠密行。一次完整的 ADMM 迭代在一到两个融合核内完成,并通过 CUDA graph 成批重放。它根据一次性的设备标定和每个问题形状的计时,自动选择执行模式、tile 尺寸和精度;通过缓存的算子库探测初始惩罚参数,问题矩阵变化时只重新求逆当前用到的算子。结果:摘要只说明在数值基准、仿真人形和四旋翼控制上延迟低于其他 GPU 求解器、精度不变。仓库 README 给出了具体数字(RTX 3080 Laptop,float64):随机稠密 QP 在各规模下都是最快的 GPU 求解器,比 ReLU-QP 快 1.5–4.3 倍;Unitree G1 推扰恢复(2 ms 周期,290 变量)比 ReLU-QP 快 2.3–3.1 倍,时域长度可到 N=20,而 ReLU-QP 只能到 N=10;Skydio X2 的 Koopman MPC 每步 12.5 ms,CuPIQP 为 59.2 ms。
- 🇬🇧 Problem: linear MPC must solve a dense QP every control period, and existing GPU solvers are still too slow for 2 ms-class periods such as humanoid control. Method: FAME-QP runs ADMM with pre-inverted linear systems. Constraint rows on single variables (e.g. input bounds) are handled element-wise rather than as dense rows. A full ADMM iteration runs in one or two fused kernels, and blocks of iterations are replayed through CUDA graphs. A one-time device calibration plus per-shape timing selects the execution mode, tile sizes and precision; a cached operator bank probes the starting penalty, and only the active operator is re-inverted when the problem matrices change. Results: the abstract reports lower latency than competing GPU solvers at the same accuracy on benchmarks and simulated humanoid and quadrotor control. The repository README gives the numbers (RTX 3080 Laptop, float64): it is the fastest GPU solver at every size on random dense QPs (1.5–4.3x faster than ReLU-QP); on Unitree G1 push recovery (2 ms period, 290 variables) it is 2.3–3.1x faster than ReLU-QP and fits a horizon of N=20 versus N=10; and Skydio X2 Koopman MPC takes 12.5 ms per step versus 59.2 ms for CuPIQP.

---

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

🇨🇳 今日无新论文。新仓库 [NiLabs-Org/grail](https://github.com/NiLabs-Org/grail)(机载 VLA 实时推理工具)见「GitHub 动态」。 / 🇬🇧 No new papers today; see GitHub Highlights for the new on-device inference repo Grail.

## VLA

🇨🇳 今日无新论文。[Can LLMs Debug Robots by Editing Their Weights?](https://arxiv.org/abs/2611.09376) 的[官方仓库](https://github.com/jushengzhang/robot-weight-debugging)今天涨了 31★(11-10 已报告);README 新增说明:"Version 2 与真机实验正在进行"。 / 🇬🇧 No new papers; the weight-editing repo (reported 11-10) gained 31 stars and now says v2 and real-robot experiments are in progress.

另见 / See also: [ODE Policy](https://arxiv.org/abs/2611.01729)(已归入 运动控制·RL / filed under Motion Control · RL;含 π0.5 ODE 动作头分支)。

## VLN

🇨🇳 今日无新论文。[Compass 1](https://arxiv.org/abs/2611.12087) 的[仓库](https://github.com/OpenDriveLab/Compass)今天 +15★(共 38★),但仍只有 README 和图片,TODO 写明数据集、部署代码和真机权重预计 2026-12 发布,状态维持 🕒 计划开源。 / 🇬🇧 No new papers; the Compass 1 repo gained 15 stars but still holds only a README, with data, code and weights expected 2026-12 (still 🕒 Planned).

## 世界模型与 WAM / World Models & WAM

🇨🇳 今日无新论文。新仓库中只有 [BWM-Forge/bwm-forge.github.io](https://github.com/BWM-Forge/bwm-forge.github.io)(1★)与主题有关:这是 "Agentic World Programming for Embodied Intelligence" 的项目展示站,用多智能体流程编排几何、运动和视角来生成机器人视频。目前只有静态页面,没有论文链接和代码,❓ 未知。 / 🇬🇧 No new papers; BWM-Forge is only a static showcase site for agentic robot-video generation, with no paper or code (❓ Unknown).

另见 / See also: [ODE Policy](https://arxiv.org/abs/2611.01729)(已归入 运动控制·RL / filed under Motion Control · RL;含 ImageWAM 分支)、[SuperMimic](https://arxiv.org/abs/2610.28480)(已归入 运动控制·RL / filed under Motion Control · RL)。

## 空间智能与 SLAM / Spatial Intelligence & SLAM(新开源 1 条 / 1 new code release)

### [Sim(3)-TurboReg: Robust and Efficient Scale-Aware Registration via Tri-Scale Consistency](https://arxiv.org/abs/2611.14135) — 作者:Zijun Zhou, Shaocheng Yan, Zhenjun Zhao, Yutong Hu 等(Wuhan University、University of Zaragoza)
开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/ivan-zzj/Sim3-TurboReg);arXiv Comments 写明 "Code available",匿名可访问,MIT 协议。这篇论文 11-10 提交,属于 cs.CV,前两天的报告没有收录;今天出现在 radar new_repos 中(4★)。
- 🇨🇳 问题:VGGT、DA3 这类前馈 3D 基础模型受推理显存限制,无法直接处理长序列。流式系统通常用滑窗分块来绕开这个限制,但分块会带来严重的单目尺度歧义,需要一种在大量外点下仍然准确高效的 Sim(3) 配准。方法:Sim(3)-TurboReg 改写了 TurboReg 的兼容图构建方式,用严格的"三尺度一致性"(Tri-Scale Consistency, TSC)准则替代绝对距离约束,再结合局部尺度投票和 TurboClique 候选搜索。分析表明 TSC 能同时抑制误匹配外点和坐标畸变外点。整个求解器用 C++/LibTorch 实现,CPU 和 GPU 共用同一套稠密图算法。结果:在 90% 外点的未知尺度配准上,精度与 RANSAC 相当,中位延迟降低 92.5%;README 显示同一设置下 TEASER++ 发散,而本方法的平均旋转误差为 0.48°。作为 DA3-Streaming 的分块对齐后端时,KITTI 平均 ATE RMSE 降低 22.2%,端到端耗时降低 16.6%,可以实现公里级重建。
- 🇬🇧 Problem: feed-forward 3D foundation models such as VGGT and DA3 cannot process long sequences natively because of inference memory. Streaming systems work around this with sliding-window chunks, which introduces severe monocular scale ambiguity, so they need Sim(3) registration that stays accurate and fast under heavy outliers. Method: Sim(3)-TurboReg reformulates TurboReg's compatibility-graph construction, replacing absolute-distance constraints with a strict Tri-Scale Consistency (TSC) criterion, combined with local scale voting and TurboClique candidate search. The authors show that TSC suppresses both mismatch and coordinate-distortion outliers. The solver runs in C++/LibTorch with one dense-graph algorithm shared by CPU and GPU. Results: at 90% outliers in unknown-scale registration it matches RANSAC accuracy with 92.5% lower median latency; the README shows TEASER++ diverging in the same setting while this method keeps a 0.48° mean rotation error. As the chunk-alignment backend of DA3-Streaming it cuts mean ATE RMSE on KITTI by 22.2% and end-to-end time by 16.6%, enabling kilometer-scale reconstruction.

## 其他值得关注 / Other Notable

🇨🇳 今日无。 / 🇬🇧 None today.

> **错归自查 / Misfiling check**:优先级 3–7 的类别里,只有 Sim(3)-TurboReg 一条展开条目(点云配准/流式重建,不涉及运动控制)。BWM-Forge 是机器人视频生成展示站,也不涉及控制。ODE Policy 同时涉及 VLA/WAM 动作头和 SuperMimic RL,但它的贡献是策略/控制,所以归入运动控制·RL。 / Only Sim(3)-TurboReg is expanded in categories 3–7, and it involves no motion control; ODE Policy stays in Motion Control · RL.

---

## GitHub 动态 / GitHub Highlights

### Star 增长 / Star growth(相对 2026-11-11 23:13 UTC 快照 / vs. snapshot)

| 仓库 / Repo | Stars | 增长 / Δ | 说明 / Note |
|---|---|---|---|
| [HybridRobotics/supermimic](https://github.com/HybridRobotics/supermimic) | 1,302 | +283(按 oss_watch 前后两日数值) | SuperMimic 官方代码,见顶部区块。 / Official SuperMimic code. |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 17,759 | +122 | 4.0.1 发布后的第二天,仍在增长。 / Still climbing after 4.0.1. |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | 26,166 | +97 | 用 AI 从文本设计实体产品(CAD),与机器人关系较弱。 / Text-to-CAD; weakly robotics-related. |
| [dexmal/opendm](https://github.com/dexmal/opendm) | 2,618 | +55 | 开放世界具身基础模型(此前已报告)。 / Open-world embodied foundation model. |
| [eust-w/opengeniemaster](https://github.com/eust-w/opengeniemaster) | 292 | +42 | 开源具身智能体框架(执行、反馈、持续改进)。 / Embodied agent framework. |
| [jushengzhang/robot-weight-debugging](https://github.com/jushengzhang/robot-weight-debugging) | 33 | +31 | 用 LLM 编辑 π0.5 的 65 行 token embedding 来修复指令失败,765 条留出改写指令上成功率 86.3%→92.0%。 / LLM weight edits lift π0.5 from 86.3% to 92.0%. |
| [harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio) | 2,355 | +30 | 跨厂商 3DGS 训练器(视频→splat→网格)。 / Cross-vendor 3DGS trainer. |
| [openrobokit/robokit](https://github.com/openrobokit/robokit) | 206 | +29 | 通用机器人任务工具包。 / General robotics toolkit. |
| [roboninecom/SO-ARM102](https://github.com/roboninecom/SO-ARM102) | 217 | +21 | SO-ARM100/101 的后继:开源 5 自由度主从臂套件,PET-CF 机架加平行夹爪,兼容 LeRobot。 / SO-ARM 101 successor, LeRobot-compatible. |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28,844 | +22 | — |
| [embodied-agent-arena/embodied-agent-arena](https://github.com/embodied-agent-arena/embodied-agent-arena) | 111 | +18 | 10 个前沿 VLM 智能体 × 5 类机器人能力 × 1,000 个案例的评测。 / VLM-agent robotics benchmark. |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 14,630 | +17 | — |
| [mujocolab/mjlab](https://github.com/mujocolab/mjlab) | 3,393 | +16 | SuperMimic、a2-mjlab 等的上游。 / Upstream of SuperMimic and others. |
| [OpenDriveLab/Compass](https://github.com/OpenDriveLab/Compass) | 38 | +15 | Compass 1 VLN,仍只有 README(🕒)。 / README only. |
| [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic) | 592 | +11 | SuperMimic 实现与扩展合集(第三方)。 / Curated SuperMimic list. |
| [fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic) | 224 | +9 | 第三方 G1 全身动作跟踪,单 GPU 约 3 分钟。 / Third-party G1 tracker. |

### 新仓库精选 / Notable new repos

- [santoshrajkumar/fame-qp](https://github.com/santoshrajkumar/fame-qp)(8★)— FAME-QP 官方代码(见运动控制·传统)。 / Official FAME-QP code.
- [ivan-zzj/Sim3-TurboReg](https://github.com/ivan-zzj/Sim3-TurboReg)(4★)— Sim(3)-TurboReg 官方代码(见空间智能与 SLAM)。 / Official Sim(3)-TurboReg code.
- [HanshangZhu/a2-mjlab](https://github.com/HanshangZhu/a2-mjlab)(2★,11-11 新建)— 在 mjlab 中训练 Unitree A2:盲走速度步态(粗糙地面、台阶、背负载荷),以及冻结步态之上的高度图导航策略。后者复现了 ETH 的 [Learning Robust Autonomous Navigation and Locomotion for Wheeled-Legged Robots](https://arxiv.org/abs/2405.01792)(Sci. Robot. 2024)。属于第三方复现,部分模型和数据未包含。 / A2 gait + ETH-style navigation in mjlab; third-party reproduction.
- [NiLabs-Org/grail](https://github.com/NiLabs-Org/grail)(1★,11-12 新建)— 面向机载芯片的 VLA 实时推理工具,目前是 pre-alpha。提供延迟 p50/p99、功耗、动作漂移基准,以及按截止时间执行动作块的 `ChunkRunner`(超时时保持、减速或停止);首个基准尚未发布。 / On-device VLA inference harness; pre-alpha.
- [Morantkk/SO101-PI05](https://github.com/Morantkk/SO101-PI05)(2★)— 双臂 SO101 用 π0.5 叠裤子:冻结主干微调,用 RTC 做真机部署。 / π0.5 on bimanual SO101 with RTC.
- 其余 new_repos 多为课程项目、SLAM/ROS 练习、无描述空仓库、硬件小项目,以及第三方 SuperMimic 复现(见顶部),已略过。 / Remaining new repos are coursework, empty or hobby projects.

### 新 Release / New releases(窗口内 / in window)

🇨🇳 无。radar 记录的 [MuJoCo 4.0.1](https://github.com/google-deepmind/mujoco/releases/tag/4.0.1)(11-11 15:47 UTC,主要修复 4.0.0 引入的稀疏 Cholesky 超节点合并错误,该错误会让 Newton 求解器得到错误的 Hessian 因子;另外 Studio Web Viewer 支持 Windows,新增 `mjs_getInStringVec`)和 [Newton v1.8.0](https://github.com/newton-physics/newton/releases/tag/v1.8.0)(11-11 15:53 UTC,新增与 Skild AI 合作的实验性 SolverSteel 接触密集 RL 求解器、无质量走线腱、可变形体静息形状与全表面接触)都在窗口之前发布,昨日已详细报告。 / 🇬🇧 None in window; MuJoCo 4.0.1 and Newton 1.8.0 predate it and were covered yesterday.

---

## 今日趋势 / Today's Trends

1. **SuperMimic 正在成为人形全身跟踪的公共底座。** 🇨🇳 官方仓库一天涨约 283★,[ODE Policy](https://github.com/NTUMARS/ODE-POLICY) 直接提供 `rl-supermimic` 分支,把自己的策略当作 SuperMimic 的 actor;第三方复现也扩展到 29 自由度人形([Dex-SuperMimic](https://github.com/luckylhf/Dex-SuperMimic))和轮足机器人([go2w-supermimic](https://github.com/uwvwko-zzz/go2w-supermimic))。可微世界模型加 BPTT 这条路线的门槛正在快速降低。 / 🇬🇧 SuperMimic is becoming shared infrastructure: +~283 stars in a day, ODE Policy ships a SuperMimic actor branch, and community ports reach 29-DoF humanoids and wheeled-legged robots.
2. **mjlab 生态继续扩张。** 🇨🇳 [mjlab_research](https://github.com/HybridRobotics/mjlab_research)、[a2-mjlab](https://github.com/HanshangZhu/a2-mjlab)、[blinkmimic](https://github.com/fuyichen0725/blinkmimic) 都基于 [mjlab](https://github.com/mujocolab/mjlab),MuJoCo-Warp 正在成为 Isaac Lab 之外常用的 RL 训练栈。 / 🇬🇧 mjlab (MuJoCo-Warp) keeps spreading as an alternative RL training stack to Isaac Lab.
3. **实时控制要求推动求解器和推理工具的工程化。** 🇨🇳 [FAME-QP](https://github.com/santoshrajkumar/fame-qp) 把人形 MPC 的 QP 压进 2 ms 周期,[Grail](https://github.com/NiLabs-Org/grail) 按 `t_max = k/f` 的截止时间来衡量 VLA 推理,两者都把"满足截止时间"而非平均延迟作为核心指标。 / 🇬🇧 Real-time deadlines drive tooling: FAME-QP fits humanoid MPC into 2 ms, and Grail measures VLA inference against per-chunk deadlines.
4. **前馈 3D 基础模型配上几何后端。** 🇨🇳 [Sim(3)-TurboReg](https://github.com/ivan-zzj/Sim3-TurboReg) 用鲁棒 Sim(3) 配准修补 VGGT/DA3 流式重建的尺度漂移,说明在前馈 3D 模型之上做长程 SLAM,仍然需要经典的鲁棒估计。 / 🇬🇧 Robust Sim(3) registration patches scale drift in streaming VGGT/DA3 reconstruction; long-range SLAM on feed-forward 3D models still needs classical robust estimation.

---

## 关键词建议 / Keyword Suggestions

**建议新增 / Add**
1. `mjlab`(**GitHub topic/关键词 / GitHub topic & keyword**)— 🇨🇳 今天的新仓库和增长仓库中至少有 5 个基于 mjlab 的运动控制项目([a2-mjlab](https://github.com/HanshangZhu/a2-mjlab)、[mjlab_research](https://github.com/HybridRobotics/mjlab_research)、[blinkmimic](https://github.com/fuyichen0725/blinkmimic)、[Xiaoxibin/in-hand-rotation-mjlab-supermimic](https://github.com/Xiaoxibin/in-hand-rotation-mjlab-supermimic)、[supermimic](https://github.com/HybridRobotics/supermimic)),但它们大多没有打 humanoid/locomotion topic,容易漏掉。 / 🇬🇧 At least five mjlab-based control repos appeared today, mostly without humanoid/locomotion topics, so they are easy to miss.

**建议观察 / Watch**
2. `action chunk deadline` / `real-time chunking (RTC)` / `on-device VLA inference` — 🇨🇳 今天有 2 个仓库([Grail](https://github.com/NiLabs-Org/grail)、[SO101-PI05](https://github.com/Morantkk/SO101-PI05))关注动作块的实时执行,信号还弱,再观察几天。 / 🇬🇧 Two repos focus on real-time chunk execution; the signal is still weak.

**建议移除/收窄 / Remove or Narrow**
3. `reinforcement learning robot`(**arXiv**)— 🇨🇳 这个短语检索在 4 个类别中只返回 12 条结果,最新一条是 2026-05-28,长期没有产出;建议改为 `reinforcement learning AND (robot OR locomotion OR humanoid)` 这类布尔组合。 / 🇬🇧 The phrase query returns only 12 results with the newest from May 2026; replace it with a boolean combination.

---

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 / Added | 当前状态 / Status | 今日检查结果 / Today's check | 备注 / Notes |
|---|---|---|---|---|
| **[SuperMimic](https://arxiv.org/abs/2610.28480)** | 2026-10-22 | ✅ 已开源 / Released(11-11 首次确认;列表文件中仍为 unknown) | signal=true;candidate_repos 为 [HybridRobotics/supermimic](https://github.com/HybridRobotics/supermimic)(known_repo + owner,**1,302★**,最后推送 11-11 08:06 UTC,HEAD `abc124c1` 与昨日相同)和 [HybridRobotics/mjlab_research](https://github.com/HybridRobotics/mjlab_research)(owner,37★);project_page_github_links、project_page_release_claims、arxiv_github_links 均为空;arXiv 最新版本 v2;errors 为空。 | 代码无变化,仍无预训练权重。search_hits 共 15 个,都是第三方(新增如 [Dex-SuperMimic](https://github.com/luckylhf/Dex-SuperMimic)、[codyn-supermimic](https://github.com/Co1con/codyn-supermimic))。[ODE Policy](https://github.com/NTUMARS/ODE-POLICY) 提供了把 ODE 策略用作 SuperMimic actor 的分支。 |

**建议移出 / Suggested removals**
- **SuperMimic** — 🇨🇳 官方训练代码和依赖已全部公开 3 天,继续留在列表里只会每天重复触发 signal,建议移出。 / 🇬🇧 Code and dependency have been public for three days; keeping it only re-triggers the signal daily.

**建议加入监测 / Suggested additions**
- 🇨🇳 今日没有新的详细论文,所以没有新增建议。此前建议的 AHEADance、DexSeed、RedirectMimic、LHNav、SimDuoReal、DreamVLA 尚待你决定。今天在 radar new_repos/star_growth_top 中没有找到这些工作的对应仓库,[robbyant-research/DexSeed](https://github.com/robbyant-research/DexSeed) 的 README 仍写 "Coming soon"。 / 🇬🇧 No new suggestions today; earlier suggestions remain pending, and none of them shows a code release yet (DexSeed still says "Coming soon").
- 🇨🇳 已开源的 ODE Policy、FAME-QP、Sim(3)-TurboReg 不需要加入。 / 🇬🇧 ODE Policy, FAME-QP and Sim(3)-TurboReg are already released and need no monitoring.

---

<sub>交付前自检 / Pre-delivery checklist:① 类别 1–2 条目已全部展开(各 1 条开源状态更新,今日无新论文);② 无"未读/仅标题"占位;③ 每个展开条目都有开源状态行;④ 已完成类别 3–7 的运动控制错归自查;⑤ arXiv API 26 个关键词均已运行并记录命中数(全部为 0);⑥ 窗口内没有 release,窗口外的 2 条已写明主要更新;⑦ 已用脚本扫描链接格式。</sub>
