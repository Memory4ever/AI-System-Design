# 2603.10913v1：03-13 独立必要 Source / 评分 / Ch76 PRE

复核者 `mar13_admission_review`；准备者 `mar13_supplement`。本项仅 Mar12 北京时间自然日补充窗；沿用本轮刚重读的当前 AGENTS/Research/Report/Prompt/SourcesDaily/arXiv/ROADMAP 与本日停点，不加载其他日期或重开已有效题摘/日级日期。本文件不授实际 POST 或 DAY。

## 实际原证范围

实际读 [准备包及逐字两段 PRE](./SUP_EVIDENCE_10913.md)，回 [官方精确 v1 raw](./SUP_CORE_10913.raw)及[manifest](./SUP_CORE_10913_MANIFEST_RESULT.json)：https://arxiv.org/html/2603.10913v1，GET200449744 bytes，2026-10-10T03:49:24.098567Z。从 raw 顺读完整 §3、§4.1–4.5/完整 T1–2、§5/完整 T3–4、§6、§8 当前/未来边界；AppA 仅实际训练参数及 MTEB-Lite 定义/Table6。数学直读 alttext。图只读文字/caption，不采用坐标；没有全读其他附录、代码、未来 latent-chain 实现或全部版本差分，未复现。

[实际完整 v1 题摘/history](./SUP_ABS3_10913.txt)显示六作者、v2 Apr2/v3 Jul29，未显示 Comments 勘误/撤回信号。精确采用仍为 v1；版本编号本身不证明重要修订。不把成熟 LLM2Vec/HyDE 引文当同稿去重，也不以 Submitted 代替公开日；本 ID 既有 §23 日级夹证复用。

## 必要机制、评价与直接反侧

- §3/§4.1 确用160K Tulu单轮 query，但不使用其答案监督；由冻结的同LLM自产响应，再用独立 unsupervised LLM2Vec encoder 提供该响应 embedding。新增10 thought/10 compression tokens，compression最后层状态先经 `MLP_recon`，第二次冻结LLM teacher-forcing 重建响应；这些中间向量再经 `MLP_align`/meanpool，MSE拟合teacher响应表示。只更新token与两MLP；在线附suffix一次LLM前向+两投影，无须先AR生成响应。不是直接投影原 query 语义，也不是“thought”标签证明真实思考。
- §4.2 query改用generative指令、document用summarize指令；产出response-oriented检索向量不能认证源文信息无损。**可解码的是用于reconstruction的compression/soft-prompt中间表示，不据此宣称最终meanpooled retrieval vector 可唯一逆解码。** 拟两段没有作此强断言，正文写后应维持区分。
- 完整 T1：Qwen1.7/4/8B全41task平均58.6/59.9/62.1，teacher54.8/56.8/56.8；9.3%是relative而非pp。4B retrieval41.1→38.0/summary31.1→28.5，8B retrieval42.7→42.2，1.7B pair76.4→75.6/summary30.4→29.0。新表征目标可改善macro均值却仍有负切片；未把不同训练数据/LoRA与零训练baseline当匹配完整预算因果对照。
- 完整 T2 AdvBench-IR 520 harmful query、1796passages，指标是top5是否含harmful passage：1.7B46.7→26.5、8B54.2→44.4仍非0。相对−43.2%不是下游生成ASR或全安全风险，拒绝归因只是作者解释，未独立隔离其全部因果。BRIGHT四Qwen的nDCG@10提高，8B14.9→19.3相对29.3%，仅支持该retrieval relevance条件，不认证真实推理完整转移或部署授权。
- 完整 T3：alignment-only62.1接近dual62.4、reconstruction-only41.8；重建主要另服务可解码性，不能说双目标对retrieval严格必要。0thought20compression62.0、19thought1compression61.9仅局部点差，无CI不授两类token都普遍必需。LoRA r8=63.0优于冻结62.4，r32=62.3；冻结是共享base/产物隔离取舍，非唯一质量最优。
- T3更强/异来源response 61.8/62.0/61.3，同family更大embedding teacher62.0、跨family59.7；支持当前设置兼容性负侧，不证明更强teacher一般更差或唯一空间错配。§6 T4 selected可读响应/LogitLens answer-associated词，仅局部解码与相关性；alignment-only检索较好但解码差两者分验。未读附录全部decode/LatentLens样本，故不认证全语义可解释、安全压缩或来源审计。
- §8 FullJEPA/latent chaining/agent communication明确为future proposals，不把当前单前向embedding认成已执行多步推理、通用world model或透明Agent协议。
- AppA实际 AdamW、one epoch160K、batch32、query/response max512并截断，Qwen4B约13M训练参数；Qwen8B约3.5h/2×H10080GB/bfloat16。预算不含已证明的全部响应合成、teacher编码/teacher自身训练、索引刷新/调参；单前向仍支付完整backbone，不授免费或生产latency/SLO。必要段未披露重复seed/CI、完整在线batch/concurrency/尾延迟/全费用。

**必要 Source 受限通过。** 保留冻结response生产者→suffix训练→线上response-oriented编码的可复用接口；因果、安全、无损、全部可解码与未来协议不采用，支持和直接反侧已足，停止扩大附件。

## 独立评分与 actual owner 差额

认可 **2+1+2=5**：D2计表征目标与生产/消费接口变化，不计成熟meanpool/蒸馏/JEPA发明；R1限retrieval representation负载，不借可联想到的优化/安全章扩Reach；Durability2计producer/teacher与线上encoder/index身份、源文证据分责。具体长期owner差额需要受影响深入，已经完成；不因负切片降低投入或排除候选。

ROADMAP唯一 `AGENT-RAG`，[Ch76](../../../../../books/part-07-agent/76-rag.md)实际顺读 **53–108完整局部**，以及155–173生成标识、522–545效用标签/共享encoder责任、748–763 LatentRAG完整邻接：

- 53–73已有index/source-of-truth与切分身份；83/85 query-only优化冻结encoder/index，只优化本query向量；87/89 reader-utility是离线答案效用造reranker标签，不改变base表示目标。
- 生成ID/teacher-ranking分支输出标识并解析回文档，不是本response-embedding suffix接口。
- LatentRAG已有单前向latent query/retriever联合对齐和natural-language decoder边界，但没有本稿冻结LLM自产响应+外部unsupervised response target+两投影重建/对齐的训练生产者与query/document编码生命周期。因此不能仅凭latent关键词签已有覆盖；现骨架可以承载这项窄新增，无需新owner或结构。

## 两段 PRE 裁决

**准备包的逐字两段 PRE 通过，无必要机制修改。** 放置于现query-only完整两段后、Document-side reader-utility两段前，保留前后分支。第一段准确保留离线自产响应、外部encoder、冻结base/新suffix与小projection、第二前向重建和线上单前向；第二段将离线/在线全费用、局部负切片、producer兼容、alignment检索与decode分责、安全代理与真实来源门、旧路径fallback放在同一链。`原始文档和权限`的工程身份与fallback要求属于系统推断，不冒称作者完成生产治理。

不把最终pooled向量可逆解码、所有安全下降因果或完整latent通信加进实际稿。root写入时加精确v1引用/Source Family，并保留完整前后局部；之后必须由非writer实际顺读新增、邻接及本人末注回源，才能授 POST。当前未写 Books，本次仅 Source/评分/owner-gap/PRE 通过，未授formal完成或DAY。
