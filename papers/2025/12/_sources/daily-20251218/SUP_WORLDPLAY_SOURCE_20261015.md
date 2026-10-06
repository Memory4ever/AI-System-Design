# WorldPlay：Dec17原发布与必要Source包

## 1. 事件与版本角色

作者Boyle实际打开官方仓库当前README、精确arXiv v1完整题摘及必要正文，另保存[Dec17版本README](./RAW_WORLDPLAY_RELEASE_README_20261015.md)（commit `fc2e0e830e077dce40341c0478958e8c574b3e3a`）。News明确两项December17,2025：HY-World1.5开源发布、技术报告/研究论文公布；按当前date-only规则可记录Dec17官方发布日，不造小时/时区，不把commit时间或arXiv submitted授首次公开。官方[固定revision](https://github.com/Tencent-Hunyuan/HY-WorldPlay/blob/fc2e0e830e077dce40341c0478958e8c574b3e3a/README.md)支持该日发布身份；原小时窗的日期hold不等于当前自然日永远不能采用。需Newton/root独立核事件去重及日门；作者不先签通过。

采用域是[WorldPlay exact-v1](https://arxiv.org/html/2512.14614v1)，[本日原HTML](./RAW_WORLDPLAY_V1_20261015.html)。abstract原三项与§3.1–3.5、§4/4.2、A算法1–2、C.3–4/F已实际读；current abs提示v2=2026-06-09，只作后续版本信号，不双版全文比较。当前仓库新增的2026训练代码/quantization/WAN5B发布不倒填；注意Dec17固定README本身已提WorldCompass，不能把“当时无RL披露”作为排除理由。

Dec17 README所链[官方系统报告](https://3d-models.hunyuan.tencent.com/world/world1_5/HYWorld_1.5_Tech_Report.pdf)当前20页另存[PDF](./RAW_WORLDPLAY_TECH_REPORT_20261015.pdf)，实际读p1–3、p9–16必要角色/方法/评价。网页工具因38,606,835字节超限未读，普通下载实际成功，非外部材料缺失。当前PDF非不可变上线快照：§5写WorldCompass clip-level rollout、action/visual双reward与DiffusionNFT，正文回指另一论文提供完整细节；这只是系统披露角色，不授Dec17完整RL recipe或无reward-hacking保证。当前报告与v1同有Context Forcing算法19行real/fake记号重复，采用概念分工，不照录为执行实现。

## 2. 必要机制、比较与反侧

全历史条件成本增长；最近窗口会丢复访信息。v1 §3.3保3 recent temporal chunks与1 spatial chunk，空间按FOV/距离取回，重赋有限相对时间位置，而非保存真实3D物理state。§3.4/算法1不是只给teacher增加更多history：学生自rollout四chunk，各自重构context；teacher取这些context的并集，去除当前生成组，令其score读取与学生相关的历史条件。历史前缀从真实视频抽取，当前组由学生产生；它仍是memory-augmented bidirectional teacher与causal student的条件近似对齐，不是架构/分布完全相等证明。

§4.2/Fig8给决定性反侧：teacher按latent而学生按chunk取memory的错配可导致崩塌；把更早历史也全改成self-rollout会因teacher原来以clean history训练而出伪影。因而“self-rollout越多越好”不是结论。C.3/Table6四步student改进相对未蒸馏AR，但并非在全部视觉/pose指标超过100步teacher；C.4/Table7更大spatial memory的PSNR略好而其他指标反退，且相邻chunk的spatial context差异扩大teacher并集/训练压力，不能将memory大小视为单调收益。

§4 protocol使用600 case；短期61帧对真实视频GT，长期≥250帧沿cycle复访比较第一次自产画面，不是长期对真实世界GT。D为30评审/600对照视频，非真实控制安全。§3.5的720p24FPS绑定8×H800/并行/量化/分段VAE，不是消费者GPU、TTFF、端到端网络或并发SLO；首发仓库14GB offload门槛不与其同口径。F把更长视频、多agent/复杂动力学及更广action留待后续。作者未核artifact、运行代码或复现实验。

## 3. 准入与唯一owner提案

建议本日新增仅一个WorldPlay发布家族，不把系统报告、arXiv论文和同日开源拆计。具体评分提案2+2+2=6：改变“仅缩短采样步数即可保memory”的设计判断，跨history-conditioned teacher/student有适用面，长期价值来自可核条件接口而非24FPS或“首个”声誉；不是把所有成熟DMD/attention/并行原则重新计分。待Newton/root校准，不先写正式已审通过。

唯一owner提案`MULTIMODAL-WORLD-MODELS`当前Ch25。fresh已读项目背景/学习理念/写作指南、Ch25开篇及840–885完整history-bank→self-rollout→learned query邻接，另读Ch24/26开篇分工。当前Ch25覆盖有界bank/self-rollout一般原则；缺的是“teacher/student按不同粒度选择history可使distillation条件错位，历史来源亦不可无差别自产”的具体反侧。Ch24拥有一般DMD/采样范式，Ch26拥有真实动作提交，均不重复新增。建议只在Ch25有界History Bank节末、规则检索→学习式Context Query标题前承载一自然段，保Draft、反侧/费用/回退近文。尚无逐字PRE/写批准/锁/写入；root可先核本单篇，不等其他来源。

## 4. 唯一Ch25逐字PRE及完整锚点

2026-10-15按root新message即时准备。实际读Newton本日§1–5及当前Ch25 815–868完整前后：前有causal少步rollout与teacher/student mismatch；目标bank节解释有界history/self-rollout，但未承载§4.2的两种history错配。以下仅提案，不称6分/正式资格已核，不写Books；等Newton实际PRE与root窄锁。root已把最小出处/固定revision差额转reader，不要求重方法。本节取代§3“尚无逐字PRE”之当时状态，其余Source有效层不重开。

目标文件：`books/part-03-multimodal-world-models/25-multimodal-world-models.md`，唯一owner `MULTIMODAL-WORLD-MODELS`，保Draft。不加标题，不改现有marker、他段/他注/index。

插入位置是以下完整原段之后：

> 这条路线同时改变 state 与 execution：选择性历史减少 residency，self-rollout distillation 缩小训练时真值历史与
> 部署时生成历史的差距，kernel、并行和按需加载决定收益能否落到实时路径。但检索可能遗漏真正的 causal state，
> self-rollout 只覆盖训练时见过的误差，面向特定 NPU 的 kernel 也会用可移植性换 latency。短 horizon 或安全关键
> 状态仍应保留较完整历史；视觉质量和 FPS 只能证明生成与系统合同，不能证明 controller utility 或安全。

后锚点是完整下一标题及起段，不在其间另加标题：

> ### 从规则检索到学习式 Context Query
>
> 固定最近窗口、关键帧或相似度检索假设“哪些历史重要”主要由人工规则决定。这个旧方案成本可控、容易解释，
> 在短片、静态主体和遮挡较少时仍合理；但 long-video generation 中，不同预测帧甚至不同 denoising timestep
> 需要的历史细节并不相同。于是 read policy 可以从固定 retrieval 演进为由当前 generation state 条件化的 query：

逐字自然段PRE：

> 有界 memory 接入蒸馏后，还须分别声明当前 rollout 与历史条件的来源。一个受限分支让 causal student 自生成当前四个 chunks，并逐步重构各自的 memory；bidirectional teacher 则读取这些 memory 的并集，排除当前生成组后提供条件 score。它对齐的是相关历史接口，不是让两者每个条件完全相同，更不是消除所有分布差异。[WorldPlay 的具体反侧](https://arxiv.org/html/2512.14614v1)显示，teacher 按 latent、student 按 chunk 选择 memory 会使蒸馏崩塌；把更早历史也全部自生成，又会偏离以 clean history 训练的 teacher，产生 score 失准与伪影。因此 self-rollout 不能自动扩成所有历史的自产许可，训练记录须同时保存调用者、选择粒度、history 来源与目标组排除范围。更大的 spatial memory 还会扩大 teacher 的历史并集与训练成本，部分指标反退；少步学生并未全面超过 teacher，复访自产画面的一致也不是真实动力学或物理安全证据。检索、teacher 训练/判分、student rollout 与解码均付费；条件身份或质量失配时，应保留 clean-video 历史、原 memory-aware teacher、较短 rollout 与真实 observation 校正，不以流畅视频替代它们。

逐字本人末Review note PRE（只本人一条，拟在当前Review notes末追加，不改他注；写前root须恢复当前末尾）：

> - `SF-2025-WORLDPLAY-20251217`：Daily `2025-12-18`补Dec17自然日；[官方固定发布revision](https://github.com/Tencent-Hunyuan/HY-WorldPlay/blob/fc2e0e830e077dce40341c0478958e8c574b3e3a/README.md) News及[WorldPlay exact-v1](https://arxiv.org/html/2512.14614v1) §3.3–3.5/4.2、A算法1、C.3–4/F。作者Boyle，仅采用teacher/student history身份与clean-history反侧，不授完整RL recipe、分布全等、性能全面支配、真实动力学或安全，未核artifact/复现。Newton必要Source/逐字PRE及root窄锁/实际非writer POST尚待，不授日级。

该note仅草案，等正式资格/评分/写前核验事实到达后才同步实际状态，不提前填“通过”。正文不依赖note才知道反侧；无root写锁不得写书。当前6分与日门仍需Newton实际校准，非writer POST只在实际保存后进行。

## 5. 窄锁下实际保存与作者读回，待实际POST

root已实际保存`ROOT_REVIEW_20261015.md`§1，授唯一Ch25的§4逐字自然段+本人末note两窄位置；Newton§6实际通过Source/Dec17发布资格/6分/唯一owner，§7实际通过逐字PRE与完整邻接。本人实际读取这些已发生记录，不重方法；本节更新此前提案态，非预签。

写前再次实看Ch25 cached和unstaged numstat均空，实际恢复当前末注`SF-2026-ARXIV-2604-09201`及目标完整bank/ContextQuery锚点。已用apply_patch只保存§4逐字一自然段（现860行）及本人末一note；note只同步Newton6/7与root实际许可，不写POST已通过。没有新marker/标题，未动原段/他注/index，Status仍Draft。限定unstaged numstat=4add/0del，diffcheck退出0，非语义验收。

保存后本人实际顺读840–891完整bank/新增/ContextQuery至Control flow及书末前注/本人注，核与批准逐字稿一致。现在可请Newton对实际完整新增/两侧/本人note做POST，root实际回读后才接纳释放；当前是已写待POST，不称实际整合通过、锁已释放或DAY。其余本日Source/date/six仍普通推进，未stage、commit、push。

## 6. 已发生实际POST/root接纳及本人note行政同步

本人实际读Newton§8与ROOT_REVIEW§2：非writer已实际完整顺读新增/两侧/本人note，root实际读回/完整diff/两层检查后接纳该一段整合并释放唯一Ch25窄锁。只把本人note的POST尚待换为Newton8/root2已发生接纳释放，未重Source/PRE或改正文/他注。当前总94/132不含Dec18；本日实际新增整合1不等DAY，root尚须读本次行政差额。现在无本日Books余锁，继续其他Source/date/six普通事项。
