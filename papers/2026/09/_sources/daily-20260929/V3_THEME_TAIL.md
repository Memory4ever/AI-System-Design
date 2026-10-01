# 2026-09-29：四个限定主题尾项 Source → actual owner 提案

状态：2026-10-01T18:37:24+08:00；仅这四个已由 root 指定的实际贡献，不扩库存、窗口或附件。窗口仍为 2026-09-28 09:00—09-29 09:00 Asia/Shanghai。本人没有写 Books、Report 或 LEARNING_STATE；下列 literal 需 root 非作者 PRE 后实际写入，再由非作者 POST。不得把本文件的 I 提案称作已整合。

本轮直接重核四份完整题摘、exact-v1 必要方法/评价/反侧和当下 owner 正文。HTML 均可读；SpeakGR 的 web abs 曾 cache miss，但直接官方 abs 读取成功，HTML 方法正常，不构成 External Blocked。没有为 I 遍历全部附件。现行合同/Prompt/ROADMAP/Books 方法沿本 lane 本日重新完整加载的上下文执行；闭环 skill 要求 source、owner、提案与实际整合分账。

## 窗口与版本

[cs.PL 官方 recent](https://arxiv.org/list/cs.PL/recent) 的 Tue, 29 Sep New 为 35425；[cs.IR 官方 recent 全显示](https://arxiv.org/list/cs.IR/recent?skip=0&show=2000) 的 Tue, 29 Sep New 开头为 35739/35430；[cs.MA 官方 recent 全显示](https://arxiv.org/list/cs.MA/recent?skip=0&show=2000) 同日 New 含 33517。未把 Submitted 日期直接当公开日期；33517 的 Submitted 27 Sep 与同一批首公开并不冲突。列表批次加官方可用性规则支持本窗口归属，正常周一 20:00 Eastern 的公布时刻折合本日 08:00 BJT，不伪称页面提供独立 first-public 秒级时间。四项均绑定 v1，当前可见资料未见撤稿或后续纠正。

## T1 Semantic Prefix Oracles — 2609.35425v1

准入：**7 = 2 实质增量 + 2 系统关联 + 3 长期性（Durability）；建议 I**。不是“输出符合 grammar”的改名：增量是 prefix 的安全剪枝合同与可完成性合同分离。必要证据：[§2.2–3.2、§4 differential validation、§6](https://arxiv.org/html/2609.35425v1)。只拒绝稳定语义矛盾支持 safe pruning；Live 不蕴含有完成 witness。Dead-end freedom 另需 surface productivity、type coverage、左到右约束流，token lift 另需精确拼写与词表覆盖。有限差分验证不等于 mechanized implementation proof；实验 unrestricted STLC 和 tool DSL 不获 dead-end 保证，C 的匹配对照也未显示 typing 的额外收益。

实际 owner：[Ch51 `INFER-SGLANG`](../../../../../books/part-05-inference-system/51-sglang.md) 的“Structured Generation 也是 Runtime State”已有 syntax/FSM mask 与 CPU state 成本，但没有 safe-prune/Live/completability 的两合同。位置：该节最后“constrained decoding 则在每一步改变合法 token set”后、Adapter Readiness 标题前；新增 `### 语义前缀的安全剪枝不等于可完成性`。不转成编译器正式证明 owner。

可供 PRE 的 literal：

> Syntax mask 在格式约束明确时最简单；加入类型与名称绑定后，prefix oracle 只应拒绝无法被后续输入修复的稳定语义矛盾。未完成前缀仍可能是 Live，却没有任何合法 completion，因此“没误剪一个可完成前缀”与“每个保留前缀都可完成”是两个合同。后者另需 grammar 的可生成性、类型需求覆盖与左到右约束流；字符级结论移到 token 序列，还须精确拼写和词表覆盖。Decoder 的 mask 不拥有程序行为正确性的认证权。
>
> 维护增量约束与候选检查增加 CPU 状态、采样和验证成本；错误实现、未覆盖类型或有限 proposal search 仍可停在死路。[Semantic Prefix Oracles v1 §2–4/6](https://arxiv.org/html/2609.35425v1)的有限 differential tests 不等于实现的机械证明，STLC/tool 的实验分支也没有统一可完成性保证。条件不成立时保留 syntax-only、生成后 compiler/verifier 或明确失败，不能因一组零 false-prune 就承诺任意 tokenizer 或程序都有效。<!-- source-family:SF-2026-ARXIV-2609-35425 -->

## T2 Rubric-Calibrated Preferences — 2609.35739v1

准入：**6 = 2 + 1 + 3；建议 I**。必要证据：[§3.1–3.4、§4.1–4.5、§6及 Appendix A 的测量范围](https://arxiv.org/html/2609.35739v1)。BT 的 query 内相对评分不自带跨 query unit/origin；正尺度 affine 映射保持 query 内顺序，共享 rubric 的 2PL 参数为每 query 拟合尺度/偏移。连续 gain 是 criterion 通过概率的区分度加权，不是事实真值。有限英文检索池与人类/NIST检查支持此测量分支；单文档 gain 不计冗余与互补，近差额仍须并列，训练和同源 judge bias 不因 IRT 消失。

实际 owner：[Ch66 `PLATFORM-EVALUATION-SYSTEM`](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已有 soft-win→BT/Elo 和 conformal interval，但没有跨 query 的相对坐标校准。Ch31 `2609-35646` 已负责 rubric 的 scalar reward/criterion 信息选择，**不是**本项 query 内固定 BT ordering→跨 query measurement；不复制 RL reward 机制。位置：Ch66“这套校准降低硬判决噪声”及其前提/fallback 段后、Route/defer 分数分解前；新增 `#### Query 内排序与跨 Query 评分不是同一坐标`，避免混入 conformal coverage。

literal：

> Query 内的比较能确定相对排序，却不能直接把不同 query 的 BT 分数当同一单位。一个测量分支先保留 listwise soft preferences 和 query 内顺序，再以共享 rubric 的 yes/no criterion verdict 拟合共同 2PL 难度与区分度，并为各 query 校准正尺度和偏移；正尺度映射不重排该 query 的 documents。校准后 criterion 通过概率可形成连续 relevance gain，用于跨 query 标签与汇总，而不是宣称发现客观正确性。
>
> 这增加 judge 调用、拟合与 rubric 维护成本，依赖测量模型适合 verdict；rubric、judge 或 pool 漂移须重核。[RCP v1 §3–4/6](https://arxiv.org/html/2609.35739v1)的有限检索评估仍忽略文档间冗余/互补，人工问题与 rubric 接近、LLM 同源偏好也未被消除。校准不稳、分差过小或事实/安全不在构念中时，保留独立人工标签、原 qrel 指标及并列/无结论；不可用该 gain 同时认证答案真值、发布政策与 RL reward。<!-- source-family:SF-2026-ARXIV-2609-35739 -->

## T3 SpeakGR — 2609.35430v1

准入：**6 = 2 + 1 + 3；建议 I，唯一机制 owner TRAIN-SFT**。必要证据：[§3–4、§5.1–5.2、Appendix B 的范围与 matched-weight 反侧](https://arxiv.org/html/2609.35430v1)。词表扩展为 text+SID 后，语言 drift 对原 text subset 重归一测量，不可把 SID leakage 和原文本内重排合并。Student 在 text-only 分支 rollout，冻结原 base 在同 prefix 给分布，计算 teacher→student forward KL；teacher 不生成训练 suffix。Adaptive 只按观测 KL 改下一步 preservation 权重。WikiText 恢复不授 coding/reasoning 全能力，也未验证完整 retrieve–resolve–generate，普通 SpeakGR 的若干 recall 下降。

实际 owner：[Ch29 `TRAIN-SFT`](../../../../../books/part-04-training-system/29-sft.md) 已有 student occupancy 与 token KD，但没有同模型 SID specialization 下“新增 action vocab/原文本条件分布/双验收”的接口分账。位置：混合 Occupancy 的 `2605-12913:end` 后、“共享 Trace 的监督权重”前；新增 `### 扩展输出词表时单独保护原语言分布`。[Ch76 `AGENT-RAG`](../../../../../books/part-07-agent/76-rag.md) 只消费 query→SID→document resolution 接口；不再写一份训练机制，也不声称统一 RAG 已实证。

literal：

> Query→semantic ID 的监督训练在专门检索器上简单直接；若还希望同模型保留语言行为，新增 SID vocabulary 会使检索正确与原文本分布漂移成为两个验收对象。一个训练分支在原 text vocabulary 上重归一学生分布，由学生生成 text-only continuation，让冻结的原 base model 在相同学生 prefix 提供分布，再以 forward KL 保护原语言输出。Teacher 提供 token 分布而非生成 suffix；SID 监督仍训练检索，不能由较小 KL 直接批准文档事实或回答。
>
> Preservation 增加 rollout、base forward 与双评价成本；在线 controller 可以根据观测 KL 调下一步 loss 权重，却不是独立能力门。[SpeakGR v1 §3–5/Appendix B](https://arxiv.org/html/2609.35430v1)只在三 backbone、两 corpus 上验证检索与 held-out 文本分布，部分 recall 仍下降，adaptive 缺 matched-average-weight 的完备归因对照；没有完整 retrieve–resolve–generate 或全能力保证。任务/语言回归不通过时，保留专用 retriever 加独立 generator、静态 preservation/replay 或原 checkpoint，不把概率保护升级为统一 RAG 能力。<!-- source-family:SF-2026-ARXIV-2609-35430 -->

## T4 TRACE — 2609.33517v1

准入：**7 = 2 + 2 + 3；建议 I**。必要证据：[§3、§4.2–4.6、§6；仅补 C.4/C.5/C.8 的完整视图、身份假设与反例](https://arxiv.org/html/2609.33517v1)。重返同任务时，departure checkpoint 与 absence delta 固定 return epoch；单项 authorization/validity/applicability/source 合格不等于所选集合覆盖 critical obligations。预算内覆盖不够须 reset/block，private experience 依其 source 是否在 admitted view 才再准入。Authenticated view 绑定 lifecycle，不认证内容真值。Explicit replacement 未一致获益；implicit verifier 漏判和不必要 abstention 均出现，长 absence 退步，总 tokens 不证明 latency。

实际 owner：[Ch77 `AGENT-MEMORY`](../../../../../books/part-07-agent/77-memory.md) 已有 read authorization、source/time/supersession，以及 write-time dependency-aware retention，后文也已有 current-validity/unknown；本项只补 **重返 lifecycle + 预算下整组 obligation coverage + 私有经验再准入**，不重复“记忆可能陈旧”。位置：Memory Read 的“Recency 高不代表正确…supersession state”后、跨多次查询累计披露段前；新增 `### 重返任务要先验收整组可用记忆`。

literal：

> 存储完整历史便于续做，却不证明 Agent 缺席期间的旧前提仍适用。重返任务时，可以把 departure checkpoint 与相关更新绑定一个 return epoch，分别检查单项授权、时间有效性、task applicability 和 source binding；没有明确点名替换的更新也可能使依赖前提失效。随后在预算内检查整组选中 evidence 是否覆盖关键 obligations：各项都合格仍可能整体缺依据。覆盖不足就 reset 或阻止准入，不能让高相似度补签；私有经历只有绑定 source 已进入准入视图才可恢复为 context。
>
> 视图身份与完整性检查不认证事实真值，排除项可保留审计但不再作为当前前提。更新追踪、dependency verifier、覆盖选择和暴露前重核均有成本；[TRACE v1 §3–4/6/C.4–5](https://arxiv.org/html/2609.33517v1)没有在显式替换下持续领先，长缺席和漏失效仍会退步，总 token 对照也不证明 latency。来源或 epoch 不可信、关键覆盖不足或更新无法判定时，保留 reset、重新取证或人工确认，不能声称对任意 poisoning 或开放协作环境的安全恢复。<!-- source-family:SF-2026-ARXIV-2609-33517 -->

## 交付边界

四项都不是因主题同义而留池，也不因有限时间降为 E：每项已核到可承载的具体 owner gap。四段提案均保留旧路径、权限、代价、failure 与下一压力，没有更改 ROADMAP 或新设 owner。请 root 逐项非作者 PRE，按通过的 literal 窄写并标记真实整合；未实际写入前，Report 不得记作 Books 已完成。日级 Gate 仍等待 root 汇总候选分母、来源停止、其他项闭环与最终 Report。
