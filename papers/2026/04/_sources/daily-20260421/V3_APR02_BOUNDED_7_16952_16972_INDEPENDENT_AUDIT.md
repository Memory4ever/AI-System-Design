# Apr21：16952–16972 七项有限非作者核验

复核者：apr02（不是 Apr21 作者）；检查日期：2026-09-27。依据当前 AGENTS、研究合同与 Report V3，仅复核作者指定的七身份、必要原文与实际章节差异；未重扫原始库存、机构目录或版本史，未修改作者报告或 Books。本文件不是日级 Gate，也不把已有日期组合推断改称逐篇首次公开日志。

结论：三个 6 分缺口提案通过 source→owner 核验；两个仅报告判断通过；一个具体前分母关闭通过；一个日期隔离通过。提案仍待共享写锁、实际正文整合及写后独立复核，**本批实际 Books 写入为 0**，不能把普通写入待办称作外部受阻。

## 2604.16952v1：5 分标准仅报告，通过

实际读[官方 v1 HTML](https://arxiv.org/html/2604.16952v1) III-C/D、Eq3–6及作者已定位的局部评价合同。Eq3 在原表示上增加跨模态 attention 残差，Eq4 对条件化表示施加 contrastive loss；这改变对齐的位置，不阻断基础表示的梯度。把灰度化重建目标用于减少难预测谱信息是受限训练配方，不能据残差路径证明基础表示不受约束，也不能从互信息最大化推出条件熵必为零。

保留 2+1+2=5、仅报告。采用范围是局部对齐/目标裁剪，不采用普遍梯度屏蔽、物理不变量或表征拓扑保证；不因遥感场景否定机制，也不将该域配方扩写成大模型通律。模型、样本、训练硬件和阶段沿作者具体配置保留；未复现实验，未作生产 SLO 判断。

## 2604.16955v1：具体前分母关闭，通过

实际读[官方 v1 完整题摘与版本说明](https://arxiv.org/abs/2604.16955v1)。题摘明确比较五种共享架构/数据的条件化配置，给出慢进展眼底预测中输入分布匹配的重要性及后验集中解释；不是没有受控证据，更不能只凭医疗标签拒绝。

但本篇新增证据限定在这一纵向成像预测操作点，没有新增基础生成过程、可迁移的低熵判定算法或改变主线生成/训练机制的适用条件；时间差条件和多尺度历史聚合也仍是该任务配方。作者具体关闭理由成立，不评分、不追所有附件或 Apr25 v2，不声称论文没有学术价值。若后来出现改变基础生成边界的新证据，再定点重开，不以同名章节映射倒推准入。

## 2604.16957v1：6 分纠错深入仅报告，通过

实际读[官方 v1 HTML](https://arxiv.org/html/2604.16957v1) §3.1–3.4/Alg1、§4 Eq6/Table1与层相关叙述。寄存器内解量化、online softmax和 split-K 两阶段显式数据依赖是真实执行方案；Ch49“量化为什么不自动带来加速”实际正文已分开解量化、launch、未融合访存与端到端收益，Ch45 混合 layout/残差 kernel 段也已分开压缩代理与真实执行成本。Metal 的具体实现可仅报告，不伪称整篇实现已有覆盖。

Eq6 的普遍角度误差表达不成立：令 q=(0,1)、k=(1,0)、量化后 k=(cosθ,sinθ)，score 变化为 α sinθ，而非 α(1−cosθ)。原文未给 q 与 k 同向等足够条件；单层相关系数直接乘方也不是一般层叠误差保证。保留 2+2+2=6，深入隔离这些保证，不否定全部实现和实测。M1 Max/macOS 的有限 kernel、模型/容量与长 context 证据不能外推完整生成质量、同负载端到端加速或生产 SLO；未写 Books。

## 2604.16965v1：6 分缺口深入，Ch66 提案通过

实际读[官方 v1 HTML](https://arxiv.org/html/2604.16965v1) §3.2/Listing1、§3.3–3.5和相关测量视图，并对读 Ch66“Living-world Evaluation：外生变化必须进入 Run Identity”（当前约 L749–772）及下一段 floor-first 交接。现有正文要求 timing/event semantics、校准与真实 replay，但未承载下面两项不能互相替代的责任。

第一，整数时钟比例上取整使 CPU/DRAM 接口视图扭曲，按物理时间推进可修换算；第二，ZSim 第一阶段的 immediate-response 已将依赖请求交给后端，第二阶段改时间不能收回错误重叠。组件内部统计因此不能替代 interface/application 的 load-to-use 验收。该因果提交失败链是新长期有效性分支，2+2+2=6、owner `PLATFORM-EVALUATION-SYSTEM` 成立。可在现 digital-twin 论证末、floor-first 前窄补组件/接口/应用三视图，以及时间域换算与依赖提交分离，不追加论文摘要。

95/5 延迟反馈只减少两阶段模型差距，不证明恢复所有因果状态；地址映射、NoC、prefetch 仍有限制。证据为作者 CPU/DRAM 模拟器与校准基准，不能外推 GPU/LLM 生产准确率；解析模型与单组件 microbenchmark 仍保留原适用条件。实际 Books 尚未写入。

## 2604.16966v1：日期隔离，通过

实际读[官方 v1 abs 的题摘与历史](https://arxiv.org/abs/2604.16966v1)，并定点核原始 `arxiv-owner-replay-20260903/20260421/arxiv-owner-receipt.json` 中该身份：v1 Submitted 为 Apr18，`v1_updated_timestamp_revision_metadata_only` 为 2026-07-13T00:22:24Z，当前 OAI 列表为空；DOI created 是 Apr21T03:53:27Z。这些字段单独或当前组合均未给本窗首次公开上界。

支持作者日期隔离、不评分、不进入正式当窗候选或 Books；April 编号和 Submitted 不能替代公告，July Updated 也不能证明真实 July owner。恢复条件是该家族首次公告/合法早期公开材料或足够精确、完全落窗的版本公开范围。相关安全题摘并不消失，但不因它有贡献信号继续全套深审、补造日期或沿用旧库存的 deep_complete/已有覆盖标签。

## 2604.16968v1：6 分保护/缺口深入，Ch72 提案通过

实际读[官方 v1 HTML](https://arxiv.org/html/2604.16968v1) §4.1–4.3/Table3、Eq1–2及§5经验类型对照；对读 Ch72 的中性文本/runtime influence、benign-DPO 更新边界、“外部化 Attack/Defense Memory 需要 Provenance Gate”（当前约 L2565–2571），并核 Ch77 provenance/retain/replay 的职责。已有正文不是完全不知良性内容可改变行为；真正缺口是**固定 backbone、无恶意经验写入时，外部经验读取仍须按行为安全回归验收**，而非只核内容来源或把训练参数更新的结论套到记忆。

Table3 的 memory-enabled 与长度匹配 system expansion 给出受限区别；检索数量和执行/拒绝经验类型进一步改变安全—utility关系。2+2+2=6、`PLATFORM-SECURITY` 窄提案通过：在持久 memory 发布边界加入 enabled/disabled/length-matched 与读取量/经验类型切片，Ch77仅交接状态治理。不采用“安全文本即安全行为”或简单拒绝记忆保证。

Eq1 是 attention×gradient，不是路径积分或因果干预；长度对照同时改变指令语义，不能排除所有语义 confound。自动 ASR grader、受测模型/bench和配置只支持局部行为风险，不是开放事故率或所有 self-evolution 必然退化。实际 Books 尚未写入。

## 2604.16972v1：6 分缺口深入，Ch33 提案通过

实际读[官方 v1 HTML](https://arxiv.org/html/2604.16972v1) §5.1–5.2/Eq7–15、§6.1–6.3/Tables1–2；对读 Ch33 DAPO Dynamic Sampling、bounds anchors及 DYPO 三路分流（当前约 L386–418）。现有方案分别提高有效梯度、给 collapsed group 信号或跳过全对组；都不能推出其他 prompt 更新时已掌握行为自动不变。

MCPO 对全对组另加相邻更新的所采 token log-ratio hinge，是与补采/过滤不同的 consolidation 责任，2+2+2=6、`TRAIN-GRPO` 缺口通过。可在 Dynamic Sampling 成立条件旁窄补“省算/学习信号 vs 已有行为保持”分支。它不是对未来正确率的硬保证；有限 mastery、共同 checker 错误与任务漂移仍可固定错误行为。

Table1 的 14B/AMC23 pass@8 退步、Table2 去 reweight 的 AIME25 pass@1 更好均须保留。关闭动态过滤也改变输入分布和补采成本，不能称全部 compute 匹配或唯一 hinge 因果；Eq12 在 p=1 的零分母须通过明确全对分支处理，不称公式自动定义。该训练配置及未披露 GPU/precision/SLO 不补造。实际 Books 尚未写入。

## 本批交接与校验

本批 ordinary 后续仅三个已通过的最小正文提案及其实际写后核验；16966 是单项外部日期保留，不掩盖普通待办。两个 Only、一个具体关闭不需强制制造 Books diff。六项日期推断沿作者已有联合证据，**本审计未替代日级来源与日期复核**；未复现实验，未声称全网无遗漏。

本文件以必要原文、当前实际命题及相关交接为核验范围。七身份唯一；Markdown/行尾空白检查通过。没有修改作者 README、Books、月度 checkpoint 或 Learning State，没有 stage、commit、push。
