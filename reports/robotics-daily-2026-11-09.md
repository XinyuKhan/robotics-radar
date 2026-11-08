# 机器人/具身智能每日速递 — 2026-11-09 / Robotics & Embodied AI Daily — 2026-11-09

## 检查窗口与来源状态 / Window & Source Status

- **窗口 / Window**:台北时间 2026-11-08 07:40 – 2026-11-09 07:40(UTC 2026-11-07 23:40 – 2026-11-08 23:40;周一,覆盖周末)。 / Monday in Taipei; the window covers the weekend.
- **arXiv cs.RO 列表**:最新仍为 [Fri 6 Nov 2026](https://arxiv.org/list/cs.RO/new)(New 68 + Cross 13 + Replacements 34,共 115 条解析),已在 11-07 报告处理,周一新列表尚未发布。 / The latest listing is still Fri 6 Nov (already covered on 11-07); the Monday listing has not been published yet.
- **arXiv API**:cs.RO 按 submittedDate 降序,最新一条提交为 2026-11-05T18:53Z,窗口内命中 0 篇。关键词检索(embodied、vision-language-action、humanoid、legged locomotion、whole-body control、world model、SLAM、motion tracking、sim-to-real、spatial reasoning,限定 cs.RO/AI/LG/CV)窗口内命中数均为 0。入选 0 篇,完整摘要 0/0。 / API returned 0 submissions inside the window for cs.RO and for all 10 keyword queries; 0 papers selected.
- **GitHub radar**:`data/latest.json` date_taipei = 2026-11-09(已更新);new_repos 150(counts 239)、star_growth_top 60、watchlist_releases 2、oss_watch 1(signal=false)。
- **Hugging Face Daily Papers**:API 可访问,返回 100 条,最新 publishedAt 为 2026-11-03,均早于窗口,无新增论文需补充开源状态。
- **推送权限**:`git push --dry-run` 通过。 / Push dry-run OK.

---

## 今日必读 / Top Picks

今日无新论文;以下为 GitHub 侧值得关注的信息。 / No new papers; GitHub-side highlights only.

1. **[Genesis v1.4.6](https://github.com/Genesis-Embodied-AI/genesis-world/releases/tag/v1.4.6)**(运动控制·RL 工具链)— 2026-11-08T21:56Z 发布,可微仿真大幅改进(原生兼容 torch、约快 3 倍),新增对 PD 控制目标的梯度支持。 / Differentiable simulation greatly improved, now natively torch-compatible and about 3x faster; adds gradients w.r.t. PD control targets.
2. **[YeWR/EPO](https://github.com/YeWR/EPO)**(运动控制·RL)— CoRL 2026 的 Energy-Based Policy Orchestration,Unitree G1 目标条件全身控制策略与能量模型训练代码,新建仓库。 / New repo with goal-conditioned whole-body control policies and energy-model training code for Unitree G1.

## 运动控制·RL / Motion Control · RL

今日无新论文。GitHub 侧:

- [YeWR/EPO](https://github.com/YeWR/EPO)(3 星,2026-11-08 新建)— Energy-Based Policy Orchestration(CoRL 2026)。
  开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/YeWR/EPO);已用匿名 `git ls-remote` 验证可访问,包含目标条件全身控制策略、能量模型与能量训练代码(依据仓库描述,未读 README 细节)。
  🇨🇳 仓库描述称其面向 Unitree G1,提供目标条件的全身控制策略、能量模型和能量训练代码;对应论文未在今日 arXiv 窗口内出现,预印本定量结果未知。
  🇬🇧 Per its description, the repo provides goal-conditioned whole-body control policies, energy models and energy training code for the Unitree G1; the paper did not appear in today's arXiv window, so no quantitative results are known.
- [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic)(542 星,+9)— SuperMimic 实现/扩展/演示合集(第三方整理,非官方)。 / Third-party curated list for SuperMimic, not official code.
- [fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic)(188 星,+8)— Unitree G1 全身动作跟踪,描述称单卡约 3 分钟训练。 / Whole-body motion tracking for Unitree G1, trained in about 3 minutes on one GPU per the description. 开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/fuyichen0725/blinkmimic)

## 运动控制·传统 / Motion Control · Classical

今日无新论文。 / No new papers today.

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

今日无新论文。GitHub 列名(star 增长):[dexmal/opendm](https://github.com/dexmal/opendm)(2391 星,+37,通用具身智能开放世界基础模型)、[groundingpi/GroundingPI](https://github.com/groundingpi/GroundingPI)(394 星,+11,4B 物理智能 grounding 基础模型)、[uclanlp/OpenVLHarness](https://github.com/uclanlp/OpenVLHarness)(427 星,+14)。共 3 项。 / 3 repos listed; no papers.

## VLA / VLN

今日无新论文。 / No new papers.

## 世界模型与 WAM / World Models & WAM

今日无新论文。GitHub 列名:[ZouShilong1024/Pelican-Sim1.0](https://github.com/ZouShilong1024/Pelican-Sim1.0)(7 星,新建,通用具身世界模型模拟器代码)、[Ropedia/ropedia-w0](https://github.com/Ropedia/ropedia-w0)(294 星,+9,跨本体 loco-manipulation 世界模型)。共 2 项。
另见 / See also: SuperMimic(已归入 运动控制·RL / filed under Motion Control · RL)。

## 空间智能与 SLAM / Spatial Intelligence & SLAM

今日无新论文。GitHub 列名:[OpenHelix-Team/Spatial-Forcing](https://github.com/OpenHelix-Team/Spatial-Forcing)(368 星,+30,空间智能机器人基础模型 SLA)、[amap-cvlab/ABot-Recon](https://github.com/amap-cvlab/ABot-Recon)(1423 星,+26,视频流式 3D 重建)、[harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio)(2245 星,+31,跨厂商 3DGS 训练器)。共 3 项。

## 其他值得关注 / Other Notable

- [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)(16377 星,+271)延续 4.0.0 发布后的关注。 / Continued star growth after the 4.0.0 release.
- 自查 / Self-check:优先级 3–7 类别中仅有 GitHub 列名,未发现涉及运动控制的错归。

## GitHub 动态 / GitHub Highlights

| 仓库 / Repo | 星数 / Stars (Δ) | 说明 / Note |
|---|---|---|
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 16377 (+271) | 物理仿真器,4.0.0 后持续增长 / Physics simulator, still growing after 4.0.0 |
| [dexmal/opendm](https://github.com/dexmal/opendm) | 2391 (+37) | 通用具身开放世界基础模型 / Open-world embodied foundation model |
| [OpenHelix-Team/Spatial-Forcing](https://github.com/OpenHelix-Team/Spatial-Forcing) | 368 (+30) | 空间智能机器人基础模型 / Spatial robot foundation model |
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 28758 (+24) | 机器人学习库 / Robot learning library |
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 8597 (+8) | 机器人学习框架 / Robot learning framework |

(radar 的 star_growth_top 前列还有 gods-eye-view、RuView 等与机器人无关或弱相关的仓库,已忽略。)

**新 release / New releases**

- [Genesis v1.4.6](https://github.com/Genesis-Embodied-AI/genesis-world/releases/tag/v1.4.6)(2026-11-08T21:56Z):打磨非刚体求解器(FEM、MPM、PBD)与耦合器;可微仿真原生兼容 torch、约快 3 倍并支持更多 setter 与物理;刚体与隐式 FEM 求解器在 GPU 小 batch 下快数倍。破坏性变更:用刚体地面替换 SAP 与 FEM 的硬编码地板;隐式 FEM 求解器最高提速 1.5 倍且内存减半。新功能:PD 控制目标及 dof force getter 的梯度;各平台的 level-set 重建、泡沫、基于物理的采样与混合实体;隐式求解器下 FEM 实体的可微仿真;可微仿真的中点积分。另含多项接触与休眠相关的 bug 修复。(release 正文较长,以上为已读到的部分。) / Polishes non-rigid solvers and couplers, with faster, torch-native differentiable simulation, new PD-target gradients and implicit-FEM diff sim, plus contact and hibernation fixes. The body was read up to a truncation point.
- [MuJoCo Playground v1.0.0](https://github.com/google-deepmind/mujoco_playground/releases/tag/v1.0.0)(2026-11-06T23:34Z,窗口前,昨日已报):正文仅指向 changelog。 / Outside the window; body only links a changelog.

## 今日趋势 / Today's Trends

1. **周末空窗,信号来自 GitHub / Quiet weekend, signal from GitHub。** arXiv 窗口内无新提交,有效信息来自 radar。 / No arXiv submissions in the window; the useful signal came from the GitHub radar.
2. **可微仿真走向实用 / Differentiable simulation maturing。** Genesis v1.4.6 加入 PD 目标梯度与隐式 FEM 可微仿真,与 SuperMimic 一类可微世界模型思路相呼应。 / Genesis v1.4.6 adds PD-target gradients and implicit-FEM diff sim, echoing the differentiable-model direction of SuperMimic.
3. **G1 全身控制代码持续开源 / G1 whole-body control code keeps landing。** [YeWR/EPO](https://github.com/YeWR/EPO)、[blinkmimic](https://github.com/fuyichen0725/blinkmimic)。 / EPO and blinkmimic.

## 关键词建议 / Keyword Suggestions

今日无建议 / No suggestions today(信号不足)。

## 开源监测 / OSS Watchlist

| 工作 / Work | 加入日期 / Added | 当前状态 / Status | 今日检查 / Today | 备注 / Notes |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 / Unknown | signal=false,无官方候选仓库,项目页无仓库链接与开源承诺,arXiv 最新为 v1 | search_hits 中均为第三方复现/笔记,如 [Huangw-NKU/supermimic-go2](https://github.com/Huangw-NKU/supermimic-go2)(非官方),不能据此判定已开源 |

**建议加入监测 / Suggested additions**:今日无 / None.
**建议移出 / Suggested removals**:无 / None.
