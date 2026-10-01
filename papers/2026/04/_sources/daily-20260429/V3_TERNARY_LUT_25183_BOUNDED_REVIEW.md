# 2604.25183v1：ternary LUT 架构的 activation dtype 条件

## 身份、准入与原文机制

[官方 exact-v1](https://arxiv.org/html/2604.25183v1) 的题名为 *Hardware Generation and Exploration of Lookup Table-Based Accelerators for 1.58-bit LLM Inference*；arXiv v1 身份页列 04/28 提交，**提交不独证首公开**。旧 60 的完整题摘已见[本日停点](./V3_REOPEN_NOTES.md)，其可核长期问题是：ternary 权重的表查找是否总比条件加减核更节省计算面积，以及应怎样选择 LUT group size/并行 fan-out。论文 §II–IV 以 `μ` 个 activation 构造 `3^μ` 组合表，`L` 个并行 LUT、每表 `K` 个 fetch，再以 adder/MUX/inverter/register 的工艺单元成本做面积模型；这是已有 ternary LUT 原语的**选择条件**，不是发明新量化格式。

§V-C/VI-C 给出真正可保留的反向条件：当 activation 为 INT8、`adder cost ≈ MUX+inverter cost` 时，增大 `μ` 的面积收益很小；FP16 的 adder 昂贵，`μ>1` 可减少累加器面积，并使更宽读出/更少 LUT 的矩形 tile 更合算。论文 Figure 8 的方向是 FP16 `K>Lμ`、INT8 `Lμ>K`；这会改变同样 1.58bit 权重下的 ASIC execution-plan 选择，不能只凭“低位权重”选择 LUT，也不能把 CPU SIMD 的无 LUT 条件加减路线视为劣等。作者侧拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5/9`，标准审阅；因可能存在真实 Ch49 长期选择缺口，Books 判断所需段落另按深入要求定点核。非作者尚未核准入和写入。

## 评价与反证

§V 的支持是 Chisel 生成设计在 TSMC 16nm、500MHz timing constraint 下的 synthesis 与 VCD 模拟功耗；Table III 的方 tile 为 8、32、64、96，`μ=1..5`，INT8/FP16 两种 activation。面积模型的 `γ` 按这些综合结果拟合，Figure 6 拟合良好并不构成独立工艺外预测。Table IV 的同 `32×32` FP16 tile 中，作者 LUT `0.120mm²`、sign-flip `0.197mm²`、full-width multiplication `0.268mm²`，可保留为**同一综合口径的 core 面积**，不是模型级 latency、能耗或线上吞吐。§VII/Table V 对 TENET 的 `7.9×` 用 28nm→16nm 的面积/时延缩放，还注明其报告面积可能含未知 buffer；对 FPGA TeLLMe 的 LUT 数又不是 ASIC 面积。不能把这些数字说成已制造的同芯片对照。

§VI-B Eq(10) 的大 core 面积密度随 tile 放大改善，建模上来自 build/output register overhead 被摊薄；其结论限 8–96 的综合空间和给定单元成本，未计芯片全局布线、片上 SRAM/HBM 接口、clock tree、thermal/封装、多 core 并发或完整 LLM。§II-C 说 GEMV core 可自然扩至 GEMM，但 §V–VII 未给 end-to-end prefill/decode 实板质量、token/s、SLO 或模型准确率对照，不能据这篇替代 GPU/CPU serving 路线。仓库 artifact 有[作者生成器](https://github.com/KULeuven-MICAS/ternary-lut-dse)，本轮只把它当披露身份，没有运行综合或代码复现。

## 真实 owner 与最小采用请求

[Ch49 当前低位路径](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)已在约 753–763 行分别讲非均匀码本/product-LUT 和 ternary bitmask 条件加减，明确 ISA、shape、packing 与端到端验证；但**未写 activation dtype 改变 adder:read-out 面积比、从而反转 LUT group size/矩形 tile fan-out 选择**这一受限硬件决策条件。Ch54 管 HBM/设备容量而非 ASIC datapath，故如非作者确认，该最窄 owner 是 Ch49：可在「码本 lookup 之外」前补一段“同一 ternary 权重下，activation dtype 与目标工艺的 adder/MUX 成本比决定 LUT 是否胜过条件加减、`μ`/fan-out 怎样选；INT8 可能只有微小面积收益，FP16 条件更有利”，下一段保 16nm synthesis 范围、未实板/模型端到端、跨工艺比较不等价及旧路线共存。不要采用“最大 core 普遍最优”或 `7.9×` 跨工艺宣传。

当前仅是 source→actual-owner 提案；请独立核 §V-C/VI/Table IV–V 与 Ch49 相邻段，确认是否非同义长期增量后由 root 授最窄共享锁，作者实写、另一非作者写后再计 Integrate。若 Ch49 现有语句已实质蕴含此 dtype 条件，改判具体 Existing 而不是为论文名字制造 diff。首公开批链及 ISPASS 2026 是否有更早独立公开仍待本日日期 Gate，不能用论文投稿或会议年份单字段定归属。

## ISPASS／作者仓库首公开的有界反查（本日日期尚未通过）

[ISPASS 2026 官方议程](https://ispass.org/ispass2026/program.php)把同题论文列在 04/28 星期二的 Session 5（11:30–13:00 KST，即 04/28 10:30–12:00 北京时间，确在本日窗口）；[官方 CFP](https://ispass.org/ispass2026/cfp.php)写会议日期为 04/26–28。这证明题名与会议安排，**不证明会议开幕日已经公开论文全文，也不证明报告者实际上于 11:30 开放完整技术内容**。Crossref 的[会议版 DOI 元数据](https://api.crossref.org/works/10.1109/ISPASS69572.2026.00048)给 `published-print=2026-04-26`，`published-online` 空、记录 `created=2026-05-26T19:39:19Z`；前者可能只是整册出版日期，后者仅是元数据建档。两者均不能独立给出 04/26 可获取的 article-level full text。IEEE Xplore 对应正文入口本轮未能给可验证的历史开放时刻。

更实质的反向线索是[作者 GitHub 仓库](https://github.com/KULeuven-MICAS/ternary-lut-dse)：GitHub API 记 repo `created_at=2026-03-08T22:52:48Z`、目前 `visibility=public`；[03/18 初始提交的 README](https://github.com/KULeuven-MICAS/ternary-lut-dse/blob/845bf65bf70f/README.md)已写同一正式题名、μ/L/K/activation dtype 参数及 INT/FP datapath、方法生成器与验证边界，[04/10 后继提交](https://github.com/KULeuven-MICAS/ternary-lut-dse/commit/d88efb3eb2e8)补图片。这是**可能早于 04/29 的同一方法公开**，不能再把 arXiv 批次链直接当本项首次公开。然而 Git 提交日期／仓库创建日期不是公共可见性日志，当前 public 属性不证明 03/18 当时仓库并非 private；README 也不含论文 §V–VI 16nm 综合、dtype 选择反转的完整证据。现有证据既不能断言 04/26 会议版全文先公开，也不能排除 03/18 作者仓库先公开核心机制。

**终态边界：** 本项贡献与 source→owner 提案保留为可核材料，但 `new_in_window`/Books 写入 **暂不签**。日期 Gate 只需一个能判别的窄凭据：会议版 article-level public fulltext 的可获取时间，或仓库 03/18–04/28 public 可见性的存档/平台日志，或作者机构带日期的完整方法发布页。不能要求无限追索整届会议、全部 Git 历史或 DOI 版本史；若这三个窄入口仍不可得，按本日合同具名隔离本项日期，报告须准确表达该不确定性，不用外部受阻挂起其它候选。
