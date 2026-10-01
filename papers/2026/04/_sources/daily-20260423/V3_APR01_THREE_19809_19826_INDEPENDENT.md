# 2026-04-23 三项具名准入复核（非作者，非日级 Gate）

本轮只复核 `2604.19809v1`、`2604.19821v1`、`2604.19826v1` 的必要官方原文及实际章节命题；未重扫该日来源或其余候选，不判定 first-public 窗口，也未写 Books。

## 19809 MIRROR — 保留候选，6 分深入，Books 待相邻命题裁决

[官方 PDF v1](https://arxiv.org/pdf/2604.19809v1) 首页和实验协议、[官方 HTML v1](https://arxiv.org/html/2604.19809v1) §3.3 Exp9／§5.3 已核：597 个复合任务中 297 个跨模型固定任务用于共同分析，C1 自主、C2 加自身校准分数、C3 再加规范提示、C4 外部路由强制控制。这确实把“是否有相对领域自知”与“是否据此升级”拆为两种行为事件；故不应因 Ch66 已有一般 confidence 校准或 Ch80 已有 selective escalation 就前分母关闭。C4 是外部控制，不是模型自省能力变强；主 CFR 下降依赖升级后由外部 oracle 正确解决，原文另给 540 个升级 component 的 fallible resolver 50.2% 与 38.7% 不必要升级，须一起报告。API-only、parse missingness、人工标签及构造任务生态限制不能被 16 模型数量掩盖。6 分保护／Evaluation 合同的深入准入成立；真正 Books 缺口应只比较 Ch66 已有 sensor→decision 分权、Ch80 已有 selective verifier 后，再决定是否需加入“自知测量×升级行为×resolver 质量×误升级成本”的配对分母，不预支 Integrate。

## 19821 JTPRO — 5 分标准，仅报告为妥

[官方 HTML v1](https://arxiv.org/html/2604.19821v1) §4／§5.2／§6 已核：全局规则与局部 tool/slot 描述可共同编辑，ToolACE、ETID 与 SEAL-Tools 仅测 tool、slot、value 的 call-level 指标，未执行真实 backend。ETID 的工具数为 124，ToolACE 表列 336–1036，SEAL-Tools 为 1138；不能将 OSR 译为真实工具执行或任务成功。§6 表 2–4 主对照主要是 Base／GEPA／JTPRO，虽然摘要称有单组件消融，可见主结果不足以把“联合编辑的独立协同”与更多可编辑参数、反思预算完全拆开。Ch78 已将 schema/version、候选路由与授权／effect commit 分权，故本项可作大目录下 prompt+tool schema 联合版本化的受限例证，不由论文名另造执行协议。保留标准 Source Review／Report Only；若日后提 Books，须先给受控单组件、相同搜索预算及真实章节尚缺的命题。

## 19826 Co-Located Tests — 具体前分母关闭

[官方 HTML v1](https://arxiv.org/html/2604.19826v1) Appendix B.5–B.7 的 Python 同语言 5 模型×3 条件×50 run：四个 frontier 模型在 inline、同文件、sidecar 均完整保留测试；布局效应主要在 RNJ-1 的受限能力区间。Qwen-3B steering 在 n=50 从 7/50 到 10/50，`p=0.30`，不能采用小样本效果为稳健机制。Rust 与 Python 的测试语法／模型条件不同，主文跨语言差异不能单独归因物理共置。实际 Ch66 §代码编辑的 change-vs-preservation 双 oracle 已明确未请求区域与测试 coverage 不同，Ch81 §迭代修复又要求 full-invariant suite；本篇只给测试呈现方式在特定能力／语言下的受限案例，未改变新的长期 state/control owner 或评价合同。前分母关闭应指向上述两个具体正文，而不是泛写“已有 coding benchmark”或仅凭领域小。

三项准入判断均不确认本窗首次公开，也不替代 04/23 其余分母、来源、Evidence 或日级独立验收。
