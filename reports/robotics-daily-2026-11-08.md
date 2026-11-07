# 机器人/具身智能每日速递 — 2026-11-08 / Robotics & Embodied AI Daily — 2026-11-08

## 检查窗口与来源状态 / Window & Source Status

- **窗口 / Window**:台北时间 2026-11-07 07:40 – 2026-11-08 07:40(UTC 2026-11-06 23:40 – 2026-11-07 23:40;周日,arXiv 周末不发布新列表)。 / Sunday in Taipei; arXiv publishes no new listing over the weekend.
- **arXiv cs.RO 列表**:最新仍为 [Fri 6 Nov 2026](https://arxiv.org/list/cs.RO/new)(New 68 + Cross 13 + Replacements 34),已在 [昨日报告](robotics-daily-2026-11-07.md) 全部处理,今日无新增。 / The latest listing is still Fri 6 Nov, already fully covered yesterday; nothing new today.
- **arXiv API**:按 submittedDate 降序检索 cs.RO,最近一条提交时间为 2026-11-05T18:53Z,窗口内命中 0 篇;因此未重复运行各关键词(命中数均为 0)。入选 0 篇,完整摘要 0/0。 / API returned no submissions inside the window (latest 2026-11-05T18:53Z), so keyword hits are all 0; 0 papers selected.
- **GitHub radar**:`data/latest.json` date_taipei = 2026-11-08(已更新);new_repos 150(counts 247)、star_growth_top 60、watchlist_releases 2、oss_watch 1(signal=false)。
- **Hugging Face Daily Papers**:本次未查询(无新论文需要补充开源状态)。
- **推送权限**:`git push --dry-run` 通过。

---

## 今日必读 / Top Picks

今日无新论文。以下为 GitHub 侧值得关注的信息。 / No new papers today; GitHub-side highlights only.

1. **[MuJoCo Playground v1.0.0](https://github.com/google-deepmind/mujoco_playground/releases/tag/v1.0.0)**(运动控制·RL 工具链)— 2026-11-06T23:34Z 发布,GPU 并行 RL 训练环境首个 1.0 正式版;release 正文仅指向 [changelog](https://reaf-sim.readthedocs.io/en/v1.0.0/playground/changelog.html),未列出具体条目。 / First 1.0 release of the GPU-parallel RL environment suite; the release body only links a changelog.
2. **[MuJoCo 4.0.0](https://github.com/google-deepmind/mujoco/releases/tag/4.0.0)** — 昨日报告已详述,今日继续有 star 增长(+23)。 / Covered yesterday; still gaining stars.

## 运动控制·RL / Motion Control · RL

今日无新论文。GitHub 侧:
- [fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic)(180 星,+12):Unitree G1 全身动作跟踪,描述称约 3 分钟完成训练。 / Whole-body motion tracking for Unitree G1, trained in about 3 minutes per the description. 开源状态 / Code: ✅ 已开源 / Released — [仓库](https://github.com/fuyichen0725/blinkmimic);仅依据仓库描述,未查看 README 与论文。
- [EGalahad/boltrt](https://github.com/EGalahad/boltrt)(5 星,新建):MuJoCo 与真机共用的 C++ 策略循环。 / One C++ policy loop for MuJoCo and real hardware.
- [miao-org/awesome-supermimic](https://github.com/miao-org/awesome-supermimic)(533 星,+9):SuperMimic 第三方实现汇总,非官方。 / Third-party SuperMimic collection, not official.

## 运动控制·传统 / Motion Control · Classical

今日无新论文或值得报告的仓库。 / Nothing new today.

## 具身智能与机器人基础模型 / Embodied AI & Robot Foundation Models

今日无新论文。GitHub:[dexmal/opendm](https://github.com/dexmal/opendm)(2354 星,+28)通用具身智能开放世界基础模型;[uclanlp/OpenVLHarness](https://github.com/uclanlp/OpenVLHarness)(413 星,+12);[huggingface/lerobot](https://github.com/huggingface/lerobot)(28734 星,+12)。

## VLA / VLN

今日无新论文。新仓库:[momoiorg-repository/urdf2vla](https://github.com/momoiorg-repository/urdf2vla)(2 星,Isaac Sim 中从 URDF 到 VLA 的流程)、[ppyyds0330/pi05-libero10-finetuning](https://github.com/ppyyds0330/pi05-libero10-finetuning)(2 星,openpi pi05 LIBERO 微调教程)。

## 世界模型与 WAM / World Models & WAM

今日无新论文。GitHub:[nv-tlabs/lyra](https://github.com/nv-tlabs/lyra)(2832 星,+19)生成式 3D 世界模型;[Junchao-cs/SolarWM](https://github.com/Junchao-cs/SolarWM)(909 星,+18)长时程视频世界模型;[Ropedia/ropedia-w0](https://github.com/Ropedia/ropedia-w0)(285 星,+15)跨本体 loco-manipulation 世界模型;新建 [ZouShilong1024/Pelican-Sim1.0](https://github.com/ZouShilong1024/Pelican-Sim1.0)(4 星)与 [flyingbitac/FlowPilot](https://github.com/flyingbitac/FlowPilot)(6 星,无人机世界-动作建模)。

## 空间智能与 SLAM / Spatial Intelligence & SLAM

今日无新论文。GitHub:[amap-cvlab/ABot-Recon](https://github.com/amap-cvlab/ABot-Recon)(1397 星,+9)视频流式 3D 重建;[harry7557558/spirula-studio](https://github.com/harry7557558/spirula-studio)(2214 星,+22)3DGS 训练器;[Leonhart999/slam-autonav-console](https://github.com/Leonhart999/slam-autonav-console)(4 星,新建)LiDAR SLAM 建图控制台。

## GitHub 动态 / GitHub Highlights

| 仓库 | 星数 | 增长 | 说明 |
|---|---|---|---|
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | 102870 | +141 | WiFi 信号空间感知,与主题弱相关 / WiFi-based sensing, weakly related |
| [dexmal/opendm](https://github.com/dexmal/opendm) | 2354 | +28 | 具身开放世界基础模型 / embodied foundation model |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 16106 | +23 | MuJoCo 4.0.0 发布后持续增长 / growth after 4.0.0 |
| [nv-tlabs/lyra](https://github.com/nv-tlabs/lyra) | 2832 | +19 | 生成式 3D 世界模型 / generative 3D world model |
| [fuyichen0725/blinkmimic](https://github.com/fuyichen0725/blinkmimic) | 180 | +12 | G1 全身动作跟踪 / G1 motion tracking |

**Release(窗口前后 48 小时内)/ Releases:**
- [MuJoCo 4.0.0](https://github.com/google-deepmind/mujoco/releases/tag/4.0.0)(2026-11-06T15:39Z,早于本窗口,昨日已报):新增 speculative 接触标志,防止快速移动的凸几何体在单步内穿透薄障碍;其余条目见 [发布说明](https://github.com/google-deepmind/mujoco/releases/tag/4.0.0)(radar 抓取的正文被截断,此处不展开未读部分)。 / Adds a speculative-contact flag against tunneling; the radar body was truncated, so remaining items are not listed.
- [MuJoCo Playground v1.0.0](https://github.com/google-deepmind/mujoco_playground/releases/tag/v1.0.0)(2026-11-06T23:34Z):正文仅链接 changelog,无具体更新条目。 / Body only links a changelog.

## 今日趋势 / Today's Trends

周末无新论文,无法形成趋势判断。GitHub 侧可见 SuperMimic 的第三方复现仍在持续出现(见下方监测列表),说明该工作关注度高。 / No trend can be drawn from a weekend with no new papers; third-party SuperMimic reproductions keep appearing.

## 关键词建议 / Keyword Suggestions

今日无建议 / No suggestions today.

## 开源监测 / OSS Watchlist

| 工作 | 加入日期 | 当前状态 | 今日检查结果 | 备注 |
|---|---|---|---|---|
| [SuperMimic](https://arxiv.org/abs/2610.28480) | 2026-10-22 | ❓ 未知 / Unknown | signal=false,candidate_repos 为空,无项目页开源承诺,errors 为空,arXiv 最新版 v1 | search_hits 均为第三方复现(如 [Uni-SuperMimic](https://github.com/HUSTforever/Uni-SuperMimic)、[OpenSprite-SuperMimic](https://github.com/BeijingDynamics/OpenSprite-SuperMimic)),不算官方开源 |

建议加入监测 / Suggested additions:今日无(无新论文)。 / None today.
建议移出 / Suggested removals:无。 / None.
