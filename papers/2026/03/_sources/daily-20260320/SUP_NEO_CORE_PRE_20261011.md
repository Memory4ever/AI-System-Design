# NEO17533：有限原证与 Ch76 差额 PRE

resume_mar17，2026-10-11，仅03-20补03/19；6分（2+2+2）准入/date复用本日批4独核§12。本文件是准备，不自授Source/PRE/Books/POST/safe/DAY。

## 1. 必要精确原证与停止

[v1 HTML](https://arxiv.org/html/2603.17533v1)实际读§3.1–3.4 L145–212、§4.1–4.2/T2–4 L217–327、§4.2.3/T5–6 L328–374；B1–3 L471–506、C/D的ID稳定性及F直接失败L507–546。先前本日必要方法已读有效复用，本次补实现/语言评价/失败边界，未遍历refs、G/H、代码或旧版本。

接口：内容嵌入→分类型离散SID；扩词表后先冻结backbone只对齐新SID输入/输出参数，再监督混合text/SID序列。trie只约束SID span；collision用canonical item选择，合法ID不是唯一对象或语义正确。评价是作者受限目录与时窗，非开放RAG。

直接反侧：冷启动相对生产baseline退步，SID token嵌入直接kNN失败；mixed输出无对照，解释由GPT-4o-mini代理评价而非独立事实认证。语言保持指标在grounding后，不授最后全参数SFT保持。核心小backbone、8H100训练已披露；推理hardware/precision/batch/SLO及全生命周期总费未披露，不采headline或通用成本。CF标识漂移需重训/稳定化；内容SID亦不能自动授权。

## 2. actual owner / 非 NC 差额

实际Ch76 L150–185包含生成ID排序、trie边际监督、变长码/collision附加uniqueID及lexical/hybrid回退，但未承载同一输出序列text与typed SID span、span内catalog约束与collision canonical解析的组合边界。拟唯一owner `AGENT-RAG`，Ch76原170变长码完整段后/172总成本段前两段；Ch75/77交接实际读，不把历史交互当新Memory。Ch23 codec只保表示分工，不另写重复正文。

## 3. 逐字 PRE（未授权写）

目录标识还可以与自然语言在同一输出序列中混排。先从内容表示构建按对象类型区分的离散码，扩展输入 embedding 和输出头；冻结原 backbone，仅对齐新标识参数，再进入共同的指令训练。生成时只在标识 span 内用目录 prefix trie 限制后续 token，普通文本继续按语言模型生成。它把外部候选检索的一部分工作移入模型，却仍依赖目录、码本与解析映射；多个对象共用同一码时还要选择 canonical 对象，生成合法标识既不保证对象唯一，也不保证推荐相关或解释真实。

[受限混合标识实验](https://arxiv.org/html/2603.17533v1)支持这一接口，不证明开放 RAG 可以省掉证据检索或权限检查。冷启动评价有反退，直接拿学得的标识 token embedding 做 kNN 也失败；自然语言解释主要由 LLM judge 评分，混合输出没有对应 baseline。冻结对齐阶段的语言保持不能外推到后续全参数训练；内容编码、量化、蒸馏、训练、trie/碰撞映射维护与 beam 都付费，代码较短不等于服务更快。目录漂移、碰撞或质量预算越界时，保留显式检索、lexical/hybrid 与独立支持性检查，不让 catalog-valid 输出自认证正确。<!-- source-family:SF-2026-ARXIV-2603-17533 -->

## 4. 本人静态源注拟文

NEO：必要v1§3–4、B1–3及C/D稳定性/F失败边界；采用typed SID与text混排的有限目录约束接口，不授唯一对象、语义/解释正确、最终语言保持或开放RAG替代；未核代码、未复现。

## 5. 窄写与作者实际回读

2026-10-11 reader独核§18必要Source/actualowner/原两literalPRE及static正式有限PASS；root授Ch76单family窄锁后，resume_mar17仅按原两PRE及静态源注实际写。完整158–192前后链（变长ID→混合text/SID→总成本→typed retrieval）与末尾本人/LLM2Vec-Gen邻注实际顺读，正文逐字保持PRE，静态注只来源与边界、无过程身份收据。git diff --check限定Ch76通过，其他Books/Report/LS不动。待非writer实际POST；未自授safe或DAY。
