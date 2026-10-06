# 第76章 RAG

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-RAG`
**Legacy Chapter:** Ch72
**Status:** Draft

**Roadmap Intent:** 用检索把外部知识动态注入上下文。

## 本章要回答的问题

为什么参数中的知识不足以支撑可更新、可引用的系统？RAG 是向量数据库加 Prompt，还是 retrieval 与 generation 的联合信息系统？为什么检索到正确文档仍可能回答错误？

本章的核心判断是：**RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。**

## 参数化知识的边界

模型参数中的知识：

- 更新需要训练或后训练；
- provenance 难以直接定位；
- 对私有、时效性和长尾数据覆盖有限；
- 不能天然执行 per-user authorization。

RAG 引入外部 corpus：

```text
query x
→ retrieve documents z
→ generate y conditioned on x, z
```

原始 RAG 工作把 parametric generator 与 non-parametric dense index 结合。工程系统进一步拆成 ingestion、index、query、rerank 和 context assembly。

### 外部知识放在哪里是 Workload-dependent Branch

同一文档可以每次放入 context、预计算成 KV representation，或通过 parameter adaptation 吸收。三条路径分别交换 retrieval latency、memory/compression、更新成本和 forgetting：context 最易更新但消耗窗口，KV 加速重复前缀却绑定模型/layout，参数化最紧凑却最难撤销和证明来源。<!-- source-family:SF-2026-ARXIV-2609-17346 -->

选择应绑定访问频率、更新率、provenance/删除义务、质量和 serving budget，而不是追求单一 winner。文档频繁变化或需要逐条引用时回退显式 retrieval；稳定高频内容才值得 KV/参数分支，且必须保留原始 evidence 与重建路径。

## Offline Ingestion 不是预处理细节

```text
source
→ authorize/collect
→ parse
→ segment/chunk
→ enrich metadata
→ embed/index
→ publish index version
```

每一步都影响可检索事实。错误 parser 会丢表格结构；固定 chunk 可能切断定义与条件；缺少 ACL metadata 会让 retrieval 无法执行权限过滤；增量更新若非原子发布，会让同一 query 看到不一致版本。

Index 应记录 source URI、content digest、version/time、tenant/ACL、parser/chunker 和 embedding model。Embedding vector 不是 source of truth。

代码语料还需要改变检索单位：独立 cell 在前置变量与状态已知时轻便，但 notebook 中一次绘图往往依赖更早的数据派生和 mutation，语义相似并不意味着可直接重用。一条受限分支沿 AST 追踪 data-variable 的创建、修改与使用，把目标 cell 所需语句按原执行顺序组成 dependency closure，再在当前数据上重跑、修复并保留原 notebook 链接。[同840对 cell/component 的标注对照](https://arxiv.org/html/2602.17215v1#S4.SS2.SSS1)支持依赖上下文改善 used-column 识别，不证明完整静态语义、执行成功即分析正确或 sandbox 本身安全；非线性执行需要完整 execution log，未知库 mutation 也可能漏依赖。重跑、代码调试与后续 VLM 解读增加费用，作者离线设置约300个 components 的检索处理约3分钟，完整12子任务 notebook 约10分钟，不是生产延迟保证；固定提示和未为该任务定制的 RAG baseline 也限制总体比较。依赖闭包或新数据运行无法核验时，回读完整 notebook、补执行日志或人工确认，简单自足的代码片段仍可直接检索，派生输出不能取代原数据事实。<!-- source-family:SF-2026-ARXIV-2602-17215 -->

切分与编码的顺序也属于索引身份：先 chunk 再独立 encode 保持局部差异且构建简单，先让文档在较长窗口中 contextual encode、再按 span pool 成 chunk 则把邻域信息带入每个向量，却可能让同一文档的 chunks 更难区分。[前后切分的有限对照](https://arxiv.org/html/2602.16974v1)显示，在跨文档以 MaxP 选文档时较有利的方案，平均上可能在同文档 chunk 竞争中反向；这不是所有 encoder/configuration 的定律，E5 与 Jina 的若干同文档设置仍有正例。文档级相关性与答案重叠 chunk 的评价单位、512 与8192的编码窗口也不同，不能把平均反转解释为已控制长度的唯一因果。选择因此应交叉验收编码前后边界与检索竞争人口，保存原始 span、context window 和 pool/chunker版本；这些是工程要求，不是向量自动取得证据权威。长窗编码、重新索引和评估均增加成本，跨 chunk 上下文不足时可走该分支，局部精确引用、长窗不可得或同文档辨别退步时，独立 chunk encoding 与原始 paragraph 检索仍合理。<!-- source-family:SF-2026-ARXIV-2602-16974 -->

在 retrieval 前，ingestion 本身已经是一段编译过程：解析文档、切分、提取结构、生成 embedding/metadata，再提交 index revision。若把它当成一次离线导入，就无法解释写放大、迟到更新、删除传播和 freshness。Index owner 应保存 source revision、compiler pipeline、segment lineage 与 commit point；查询只读取已提交快照。更丰富的结构索引提高可检索性，却增加构建成本和 stale window，文档小且更新少时直接扫描仍合理。<!-- semantic-body-binding:SF-2026-ARXIV-2608-20845 -->

### OCR 之后仍需要 Document-level State Owner

逐页 OCR 保留页内坐标且易于并行，但跨页段落、表格和标题会被切断，RAG 随后面对互相矛盾的 chunk 与结构索引。ingestion 应在 page artifact 之上维护 document revision，跨页合并结构并同步 chunk、locator 与 enrichment；原页和 region provenance 仍是可回溯 source of truth。收益是检索消费同一文档状态，代价是合并错误会跨页放大且更新粒度变大；结构不可靠时回退 page-level evidence。现有结果绑定披露 OCR/VLM、H200 与文档集，不证明跨页摘要可替代原始证据。

<!-- source-family:SF-2026-ARXIV-2605-24973 -->

### 文档结构、查询改写与答案核验必须分层消融

单一 chunk index 在问题局部、文档结构弱时简单、低延迟，也容易维护统一 freshness；但标题、表格解释和结论跨页分布时，继续增加 query rewrite 或 answer checker 未必能补回 ingestion 已经切断的 document structure。RAG 的三类改进应先作为不同责任层分别验证：document-side 负责可导航结构，query-side 负责表达信息需求，answer-side 负责提交前核验证据是否足够。

Query-side 也有一个容易错位的选择：同一 information need 可以写成多个 query variant，但服务端往往只能按预算先选一个执行。离线检索分数更高的改写不必给出更有用的答案；因此选择器要冻结原问题、候选改写集合、目标 retriever/index 与后续 reader，在真实执行前用受限 query 特征提出 variant，再分别验收排名／召回和答案支持／效用。它只拥有查询表达的 proposal，不因预测分数高就替检索结果赋予事实权威，也不能把 oracle 最优改写当成线上可得输入。<!-- source-family:SF-2026-ARXIV-2604-22661 -->

这条分支可能省去并行执行全部改写，却增加 predictor、训练标签和错误选一的机会成本；若选择器本身比多路检索更贵，或答案需要互补证据，就应回退固定 query、受预算约束的多改写融合或直接取证。受控 TREC-RAG 2024 的 BM25／dense、top-5 reader 与 nugget 评价显示，nDCG-optimal 的 variant 与答案效用可错位，甚至不保证优于某些简单 pre-retrieval predictor；但它没有给出匹配完整生成成本的生产比较，也不证明某一种 QPP 策略普遍最优。Document-side 结构修复与 answer-side 证据核验仍由各自 owner 承担。

视觉 query 的修复还应保持信息需求本身：crop、deblur、caption 等工具可能让图更容易检索，也可能删除关键对象、补造细节或改掉问题语义。保留原图与扰动/修复 identity，用配对样本分别核对真实工具执行、oracle 修复、retriever recall 与 reader 答案；[VQPP 的受限对照](https://arxiv.org/html/2602.13179v1)揭示这些层不能由最终 answer gain 合并归因。单一合成 corruption 不覆盖组合噪声，watermark 也可能直接污染回答而非检索；Nomic 的文本/独立视觉配对与预处理未完整锁定时，对应数值不授确定复现，不据此否定其他 encoder 分支。工具调用、重编码、多轮搜索和语义核验都有费用，oracle crop 不当线上可得输入；repair 丢语义或索引失配时，保留原图直检、受预算的多路检索与独立答案核验，而不是用去噪分数给证据签字。 <!-- source-family:SF-2026-ARXIV-2602-13179 -->

对书籍、报告和规范等有可靠标题层级的 corpus，可以在 chunk index 旁维护一个 heading index。查询命中标题后，retrieval controller 再按 token/权限预算展开对应 page 或 section，并与普通 chunk candidates 去重、重排；heading 只拥有 navigation proposal，完整页也不因被展开而自动获得 support authority。索引身份必须同时绑定 document revision、heading extractor 与 section locator，避免文档更新后结构入口仍指向旧页。

该分层能恢复跨段关系，却增加双索引 freshness、布局解析误差、整页噪声和 Context 成本；标题抽取错误还会让一次命中扩散成更大的错误上下文。扫描件、无格式网页或 OCR 质量不足时，应回退经过核验的 LLM heading extraction 或普通 chunk/hybrid retrieval；简单精确查询继续直接走 chunk baseline。Exact-v1 的 factorial 实验只覆盖一个企业 RAG、8 份结构化文档、40 个查询和两个生成模型，证明三个层在该 workload 中具有互补性，不证明 heading index 普遍优于 Agentic Search，也不支持把作者的参数设置外推到其他 corpus。

<!-- source-family:SF-2026-ARXIV-2607-24781 -->

### Structured Retrieval 是可撤销的中间表示，不是新的事实源

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24366:start -->
原文 chunk 在噪声有限、版式简单时保留信息最完整，仍是合理 baseline；当 corpus 中 metadata 不一致、表格关系散落
且 query 依赖结构约束时，只做 embedding search 会把格式噪声和事实关系一起交给 reader。一条受限演进路径先对
metadata 做 quality-aware normalization，再通过 semantic/structural consistency Gate 生成表格化 intermediate
retrieval object。检索可以利用 row、column 与实体关系，但每个 cell 必须保留回到原文 span 的 provenance。

结构化接口提高了可过滤性，也会引入表格化信息损失、metadata drift、离线构建成本和错误 schema 的系统性放大。
exact-v1 的收益只绑定作者披露的数据、生成流程与 ablation，不能证明任意 noisy corpus 都适合表格化。若 table
quality、原文可追溯性或 query-side sufficiency 失败，应回退原文 chunk 或 hybrid retrieval，并把结构化结果降级为
候选索引，而不是让它取得 evidence authority。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24366:end -->
<!-- source-family:SF-2026-ARXIV-2605-24366 -->

### Persistent Corpus Structure 把在线搜索变成有限预算导航

每次查询临时重建工作区，会把大量预算花在重复组织同一语料；持久的多视图 corpus map 则让 Agent 在共享结构上逐步导航。真正的评价单位应是证据从可达、被发现、被打开到决定性片段被实现的阶段性概率，而不是“系统可访问完整语料”。持久结构会增加预处理、更新一致性和权限维护成本，但能把在线预算留给证据验证。
<!-- source-family: arxiv:2608.24764v1; semantic-body-binding: persistent-corpus-navigation-evidence-realization -->

## Online Retrieval Pipeline

```text
user/task state
→ query construction or decomposition
→ authorized candidate retrieval
→ hybrid fusion / filters
→ rerank
→ dedup/diversify
→ context packing
→ generation with citations
```

Dense retrieval 擅长语义相似，lexical retrieval 对 rare identifiers、code symbols 和精确词更稳。Hybrid retrieval 常更鲁棒，但增加融合和调参复杂度。

多跳检索还要决定**第二跳到底由哪个对象承担关系信息**。问题已包含决定答案关系的描述时，继续以原 query 为锚能避免第一跳噪声扩散；若原问题缺少关键实体或关系、必须由第一跳文档提供，question-only embedding 又可能忽略真正的桥接信息。一条条件分支先从第一跳文档挑选 relation-bearing sentence，再由 query 与 bridge 的表面特征二元选择 question-only 或 question/bridge union；选中 union 后使用冻结的混合系数，而不是让路由概率直接控制连续权重。路由器决定第二跳的评分方式，不赋予桥接文档事实权威；第一跳正确性、候选池和后续 sufficiency 仍需独立验收。

该分支用更细的信息角色换取 sentence selector、路由标注与迁移误差。[两跳实验](https://arxiv.org/html/2604.09019v1)只评价第一跳正确的子集，分析中的 Gaussian-score AUC 也依赖分布假设。主配置在三个数据集都冻结混合系数 α=0.25，受测迁移结果为正，但一项不显著；另用路由概率连续调权的消融虽提高域内结果，却降低迁移收益并出现负增益。它支持保守固定权重与自适应权重须分别验收，不证明开放检索的 no-regret 保证。关系角色不清、第一跳不可靠或校准样本不足时，保留 question-only、query/bridge union fusion 与固定 hybrid 基线；不要用更复杂路由掩盖错误的 bridge evidence。<!-- source-family:SF-2026-ARXIV-2604-09019 -->

对于事实密集、反复查询的语料，桥接关系还可以在写入时预组织：保留指向原文的 entity/event 与 QA 对，查询只分解一次，以实体 lexical 与 QA dense 双索引召回并重排，再用当前 QA 的答案实体实例化下一跳，按有界 beam 选择链，最后只把链上的 QA 送入 reader。这样把每跳 LLM 生成的部分工作移到前置抽取与索引，不必让读取控制器每次重新组织相同事实；派生 QA、关联和链分数仍不是独立事实来源，最终回答应可回指原始证据。原 chunk 与逐跳查询在写入预算低、叙事自由或未来问题难以预知时仍然合理。

这条分支用昂贵写入、实体消歧、双索引与更新维护换取更窄的查询上下文，而不是保证全生命周期更便宜。[受限 QA-chain 实验](https://arxiv.org/html/2602.15156v1)中，MuSiQue 11656 passages 的写入为100.1分钟、读取3.3秒/query，对照 dense index 为1.9分钟、1.3秒/query；减少 answer-context tokens 不代表抽取、分解、重排与回答总成本下降。开放模型抽取缺失 verb/QA 边、错误实体或旧关联都可能截断真正证据，叙事与多模态范围亦未验。应保存 source span、索引/抽取版本和删除传播；缺桥接信息或 provenance 失效时回读原 chunks、扩大检索或回退普通 hybrid，不让较短的证据链自认证充分性。<!-- source-family:SF-2026-ARXIV-2602-15156 -->

还有一条替代分支：不把 query 与 document 都压成一个向量，而让模型生成 document identifier，再由标识解析对应文档。它绕开单向量匹配的部分表达限制，却把区分压力移到 identifier、解码和评分链：相关与不相关文档若共享同一 ngram，生成出它不等于选中了相关文档；beam search 即使恢复部分 recall，也可能持续剪掉真正能区分两者的标识。因此要分别测标识覆盖、难负例区分及最终排序，并版本化标识到文档的映射、corpus 与解码规则。

标识长度也可以成为单独的预算变量。固定长度离散码便于统一解码和映射；若热门对象更容易压缩，一条受限分支可让 AR content code 共享词表，同时另学不使用 EOS 的 stopping hazard，以截断几何长度先验、期望长度惩罚和 prefix 加权重建权衡表达与长度。长度选择不等于内容正确，同一符号共享语义只是结构假设，短码仍可能碰撞；下游追加 unique ID 的处理又带回标识和解析成本，因此 code、stop、decoder 与映射应共同版本化，这属于工程要求。[推荐式生成标识实验](https://arxiv.org/html/2602.16375v1)按交互频率加权重建，不能替代均匀 catalog 覆盖；固定512-token历史下较短码能容纳更多事件，也不能读成相同事件预算的纯质量改进。冷尾对象可能更长，部分数据集重建仍逊于固定码基线；更强长度惩罚可伤重建，扩大最大长度或词表也会增加训练和输出头成本。该有限评价没有测开放 RAG 部署延迟、beam或生产 SLO，较短码不自动等于加速；碰撞、冷尾或更新成本越界时，保留固定标识、lexical/hybrid 与显式映射回退。<!-- source-family:SF-2026-ARXIV-2602-16375 -->

这种分支增加标识维护、beam 和更新成本；精确符号查询、快速变更语料仍可优先 lexical 或 hybrid 检索。[生成式检索的受控反例](https://arxiv.org/html/2604.05764v1)来自 SEAL/MINDER 与 LIMIT-H/HS，oracle pseudo-query 只是诊断上界，不是部署输入，也不证明所有生成式检索必然失败。<!-- source-family:SF-2026-ARXIV-2604-05764 -->

当知识库同时包含 text、table、graph、image 或 executable corpus 时，“统一检索”不应意味着把所有对象强行
压成同一种 vector。更稳定的抽象是统一 query plan 与 evidence identity，同时保留 modality-native operators：

```text
typed query and authorization
→ route to lexical / dense / table / graph / media operator
→ operator-native candidate construction
→ normalize provenance and confidence
→ cross-source rerank / pack / verify
```

这保留了各类索引的 inductive bias，也让 operator failure 可归因；代价是 routing error、score calibration、
materialization cost 与跨源去重。Corpus 小且同质时单一 index 更简单。OmniRetrieval 只在其受限 heterogeneous KB
合同下证明统一 orchestration 的可行性；GrepSeek 则提醒 code/frozen corpus 可把 `rg/grep` pipeline 本身作为 typed
retrieval program，并只并行 shard-independent transformations。它们都不证明 semantic retrieval 或 lexical search
可以普遍取代另一方。

Authorization 必须在返回内容前执行。先全局检索再让模型“忽略无权内容”，已经发生数据泄露。

检索入口若已解析一个对象，交接时还需区分“这个对象是否被正确选中”和“它是否被送到 reader”。只有任务合同明确要求保留该对象且授权有效时，才应按稳定 identity 直接解析并预留 Context 位置，让语义 ranking 补充其他证据，而不是把已选对象重新交给相似度竞争。验证也要分开检查 selection、handoff 和最终回答：对象成功送达不证明选对了，更不等于召回了数据集标注的全部证据。预留位置会挤占预算，也可能保留错误选择；没有 selected-return 要求的开放检索仍可完全由 ranking 决定返回集合。

### Retrieval Format 也是输入身份

只按语义相关性选择文档，在来源都是自然语言、序列化近似一致时足够；当知识图谱 triple、表格或重复 slot 与正文共同进入 context，delimiter 和结构重复会独立争夺 attention，即使内容语义等价也可能改变答案。RAG pipeline 因此应把 serialization format 与 content provenance 一起版本化，并在 Evaluation 中将 source relevance 与 format-induced attention capture 分开消融。

Flattening 或改变分隔符可以作为低成本 mitigation，却可能丢失结构关系，局部 attention 变化也不等于答案正确。结构化检索确实需要 schema 时继续保留原格式；干预收益不稳定或下游任务依赖结构时，回退原 serialization 并由答案级 verifier 判断。现有证据只支持作者任务中的格式效应和部分缓解，不证明统一扁平化对所有 RAG 都更优。
<!-- source-family:SF-2026-ARXIV-2606-11198 -->

在 reader 之前，format 也会改变同一表格的检索 embedding。一条训练侧分支让同表的多个 serialization 形成 centroid 目标，只训练 table adapter、冻结 query encoder；线上仍编码一个选定 view，而非每次展开全部格式。它试图使表格表示减少对 format 的敏感度，和后续 reader 的 attention capture 是两个不同 owner 接口；所谓消除 format shift 依赖表示偏移假设，不是已证明任意格式不变。<!-- source-family:SF-2026-ARXIV-2604-24040 -->

多格式训练增加 adapter、样本构造与 corpus re-encoding 成本，必须把 format set、adapter revision 和索引版本绑定。作者对照中 SPLADE 及部分强格式会退步，说明 centroid 并非统一优胜目标；线上 format 已稳定、强 baseline 更好或重编码预算不足时，继续原单 view 索引，并分别检查召回和最终答案，不用 embedding 接近代替答案质量。

来源差异还会在 reader 之前进入 retriever 的训练分布。即使 human 文档与改写文档按假设表达相同事实，训练 stage、配对 query 和正负样本来源也可能改变二者的排名倾向；不能只凭 source 名称、文本流畅度或语言模型 perplexity 推断召回公平。升级 encoder 或微调语料时，应在固定 query 人口、语义配对文档和索引协议下比较两类来源的 ranking/recall，再把 reader 的格式效应另行测量。这里审计的是检索选择，而非判断哪种来源为真。<!-- source-family:SF-2026-ARXIV-2602-10833 -->

配对构造、重新编码与分来源回归有成本，改写也可能悄悄改变实体和事实。[受限训练阶段对照](https://arxiv.org/html/2602.10833v1)呈现随模型和数据变化的方向，合成微调后仍存在偏 human 的配置；重新接回 LM head 的概率代理也未解释全部偏置，不能推普遍 pro-LLM 或无任何流畅度影响。来源质量或配对假设不可靠时，保留原 encoder/索引、独立相关性标注和人工事实审计；不能用更低 perplexity 或更高某来源排名批准替换。

持续加入合成文档时，来源评价还应把四个人口分开：全 corpus 的合成份额、实际 top-k 的曝光份额、答案显式引用的来源份额，以及答案对独立 reference 的质量。它们是不同测量接口：来源 origin 不是真值，显式 citation 也不揭示模型所有隐藏使用；曝光上升而答案分数暂时稳定，不能证明语料生态无损。[受限注入模拟](https://arxiv.org/html/2602.16136v1)分别运行 SEO 式重写与实体替换 abuse，未证明二者构成真实网络的时序循环；生成、排序、回答同模型家族的相关盲点和有限 judge/reference 又限制外推。逐轮检索/回答、来源标记与独立事实审计增加成本；provenance graph 或 ingest filter 是待验证防御，不是原实验已测得的修复。来源身份不清或质量退化时，保留原可信 corpus、检索/回答对照与人工事实核验，不以单一 aggregate 分数批准继续注入。<!-- source-family:SF-2026-ARXIV-2602-16136 -->

### Speculative Retrieval Draft 必须经过 Accept / Fallback


每次查询都执行完整检索，在 corpus 大、检索链深时可靠但把全部延迟暴露给 TTFT。若历史缓存中存在与当前 query 同源或高度同构的查询，可以先从窄 cache/fuzzy channel 产生 candidate documents，形成 retrieval draft；关键是 draft 不能因为“看起来相似”就直接进入 Context。

Speculative retriever 只拥有 draft proposal 和 reference-query identity。Validator 必须检查 cached query、其已知相关文档与当前 query 的关系，在代理条件满足时 accept；否则回退完整 retrieval。Context packer 只接收已经通过授权、freshness 和 accept gate 的 documents。这样把省略全库检索的决定变成显式状态，而不是 cache hit 的隐式副作用。

代理验证比调用强 evaluator 便宜，却会引入 homology false positive、过期 cache、错误 golden-document identity 和分布漂移；接受错误会直接牺牲 recall。高风险 claim、query 关系不足、corpus revision 不一致或 validator 未校准时必须执行完整检索。作者的 latency/accuracy 结果只证明所披露数据集与 pipeline，不证明开放域或生产尾延迟。

<!-- source-family:SF-2026-ARXIV-2604-20452 -->

### Tenant Filter 必须在检索内核中前置执行

在多租户向量检索中，先取全局 top-k 再按 ACL 丢弃结果，只在授权集合不稀疏时尚可接受；当 tenant 只拥有很小的 candidate partition，未授权向量会同时占用 score budget 与 top-k slot，over-fetch 也无法稳定恢复 recall。Tenant / ACL policy 应由可信控制面决定，并在 ANN kernel 的 candidate admission 之前执行；index 只消费不可伪造的 allowlist，不能自行解释用户身份。

Kernel pre-filter 用执行耦合与可能的数据倾斜换回安全和 recall；per-tenant index 隔离更强，却增加内存、build 与 freshness 成本。Codebook-oblivious quantization 只能消除一种 corpus-trained codebook channel，不是 embedding privacy 证明；query、access pattern、compressed vector 与 calibration statistics 仍需第 71、72 章的隔离和 threat model。

不同 agent 反复访问重叠语料时，独立索引最易隔离，却会为宽 scope 查询重复 coarse 导航。一个性能分支让每个 scope 保留自己的 coarse graph，再以 inter-graph portals 连到 static graph；fine vectors 仍只存一份，每个 static cluster 另存 agent-specific 的近期 local vector IDs，优先访问该 profile，而不是复制 embeddings。这里的 scope/profile 只决定搜索路径，可信 allowlist 与最终 admission 仍决定权限，跨图可达不等于有权读取。[受限共享索引对照](https://arxiv.org/html/2602.21477v1)支持这层导航/访问次序分工，不采用其有歧义的连接概率公式；近期平均距离的 early-return 也不是 recall 证书，后台完整搜索仍计费。GPU 热 cluster 与 CPU 插入 buffer 可共同提供候选，新副本完成后再切换会增加双驻留、metadata、split 尖峰及读者/失效管理成本，不能由 async copy 授完整 publication 或 crash 一致性。有限 H100、MSMARCO/agent trace 的 ANN recall/latency不等端到端生产倍数或固定显存上界；共驻 weight/KV、scope churn、quality或freshness失配时保留独立索引、普通完整检索与已发布 snapshot，而不让 profile 命中率自认证证据充分。<!-- source-family:SF-2026-ARXIV-2602-21477 -->

<!-- semantic-body-binding:SF-2025-ARXIV-250501538-HONEYBEE:start -->
当租户权限由重叠 role graph 表达时，“一个 tenant 一个索引”会复制大量公共向量，而单一全局索引又让每次 query 承担复杂过滤。中间分支可以把稳定的 RBAC role/permission cut 编译成 ANN physical partitions，并对跨 partition 的热点向量做受控 replication。Policy owner 仍拥有 role graph 与 revision；index builder 只消费已签署的 partition plan，runtime 只在授权 partition 中搜索。它用更低查询过滤成本换 memory、update fan-out、role churn rebuild 和 policy/index 双版本一致性。角色稳定、重叠结构显著时值得考虑；权限频繁变化、小 corpus 或强隔离优先时，kernel pre-filter/per-tenant index 更透明。HONEYBEE 的 13.5×/90.4% 只属于作者 RBAC benchmark、HNSW 参数和 workload，不能成为通用向量数据库承诺。
<!-- semantic-body-binding:SF-2025-ARXIV-250501538-HONEYBEE:end -->

当过滤谓词是临时组合而非稳定 role cut 时，为每种谓词建物理分区会迅速耗尽索引与更新预算；但仅在稀疏近邻图上强制过滤，又可能把允许访问的诱导子图切成互不相通的片段。另一条条件分支不把谓词编进拓扑：先用向量几何构造较密的邻接，并以 clique cover 压缩重复边；查询时由可信 policy/filter owner 提供谓词结果，检索器只在合格节点中导航，并以多个起点缓解过滤后的断连。这里改变的是**候选可达性与索引表示**，不是把授权判断交给向量图，也不是省去最终 allowlist 验证。

这种 predicate-agnostic 路径把逐谓词索引成本换成更复杂的构建、邻接展开与多起点搜索；为取得有效起点，还要支付谓词位图预计算，或在低选择率时支付拒绝采样成本。目标 recall 接近 1 时，遍历成本仍可能急升。稳定 RBAC 可继续用受控分区，极小的授权集合可直接前筛/扫描，较低 recall 工作点也可能更适合普通 HNSW/ACORN。现有 [受限证据](https://arxiv.org/html/2604.22171v1)只比较作者的 CPU filtered-ANN 数据集、合成 Zipf 标签、Recall@k/QPS 与索引大小；没有证明真实 ACL churn、索引在线更新、RAG 答案质量或租户隔离正确性。若谓词身份、权限版本或索引 revision 无法绑定，先回退可信前筛与最终验证，不能用检索吞吐替代安全验收。

<!-- source-family:SF-2026-ARXIV-2604-22171 -->

### Retrieval 可以预测未来需求，但必须允许取消与过期

同步检索只在问题明确后发起，语义可靠且控制简单，却把 retrieval latency 完整暴露给生成路径。predictive prefetch 根据当前 trajectory 预测后续 information demand，并让检索与生成重叠；prefetch controller 因而必须拥有 query revision、freshness deadline、cancellation 和最终 evidence admission，而不是把预取结果自动塞进 context。

收益是隐藏部分 IO 延迟；代价是误预测流量、过期证据和更大的 cache/context 压力。预测置信不足、数据快速变化或高风险 claim 出现时，回退同步检索与重新验证。exact-v1 只覆盖其披露任务、预测器、retriever 和延迟/有用性指标，不证明开放对话、不同知识库或生产尾延迟中的普遍收益。

<!-- source-family:SF-2026-ARXIV-2605-17989 -->

### SSD Filtered ANN 要把 Superset Traversal 与最终验证分开

为每种 metadata filter 建独立索引，查询简单但组合爆炸、更新昂贵；直接在图遍历中强过滤又可能过早剪掉通往有效邻居的路径。SSD 路径可以遍历一个受控 superset，以 pipeline 隐藏随机 IO，再在候选进入 top-k 前由 filter verifier 做最终 admission。

这种分层改善索引复用与 IO overlap，却增加无效读取、候选缓冲和 filter selectivity 估计；高选择性、频繁更新或工作集可驻内存时，专用/内存索引仍可能更合适。exact-v1 只支持其披露数据集、SSD、索引参数、filter 分布和 recall/latency 合同，不证明任意检索库或在线更新条件的优势。

<!-- source-family:SF-2026-ARXIV-2605-17992 -->

### SSD 检索可以先分开图导航与向量读取

把邻接表和完整向量放在同一磁盘记录中，导航一步即可取得两者，访问合同简单；当许多探索节点最终不会进入重排，而4KiB对齐又产生碎片时，这种共址会把不必要的向量读取放进图遍历的critical path。一个条件分支将图邻接和向量数据分开压缩、存储与缓存：导航优先读取邻接，以内存PQ分数维护候选，待候选趋于稳定后再批量预取完整向量重排。邻接的排序/编码不改变待比较的邻居集合，向量的无损编码也不改变原值，但候选稳定性和early-stop仍是近似搜索策略，不能因此宣称exact nearest-neighbor。<!-- source-family:SF-2026-ARXIV-2604-09173 -->

分离还改变维护路径：图可以批量merge/repair，向量append后由ID-location映射定位，后台GC再压实并切换映射；它没有免除query snapshot、删除和freshness责任。收益是减少碎片和导航I/O，代价是独立metadata、解压、prefetch缓冲、GC与映射一致性；原向量已经8bit量化、候选很少或内存工作集足够时，编码和额外向量I/O可能不划算。[受限实证](https://arxiv.org/html/2604.09173v1)在双Xeon/单NVMe、64搜索线程、100M至1.4B向量中观察到这些取舍：低搜索预算以及部分billion-scale低recall工作点可比PipeANN更慢。于是验收要把storage、相同recall下的QPS/P99、update成本一起比较，而不是仅用压缩率批准替换；未经验证的高freshness或强尾延迟负载仍可保留共址布局与独立维护窗口。

完整向量重排还有一条中间分支：coarse PQ 已常驻快内存，而原向量仍在 SSD 时，可以重用 coarse distance，把精化残差和缩放标量另放到 far memory。距离分解让残差 inner product 修正已有分数；将残差方向编码为 {-1,0,1}、五维压入一个 byte 后，精化主要消费紧凑 codes，而不是重建和搬运每条完整向量。再用邻近样本上的局部线性校准改善 top-k 边界排序，先裁短候选队列，最后只为保留项读取原向量。这改变的是精化 I/O 的层级，不改变原始 evidence 或授权；残差近似各向同性且与 query 不相关才支持所用零期望近似，校准后的裁剪也不是带未读贡献上界的 exact early-stop。<!-- source-family:SF-2026-ARXIV-2601-09985 -->

中间层增加 residual codes、calibration 与 index revision 的绑定、far-memory 容量和重排成本。应在相同 recall 下比较完整查询、SSD/far-memory 流量与构建开销，而不是用距离 MSE 或压缩比批准替换。[受限 ANNS 证据](https://arxiv.org/html/2601.09985v1)基于 Wiki/LAION、A10 coarse search 与 CPU/SSD 精化，CXL 路径用 Ramulator 模拟、逻辑面积功耗用 ASAP7 综合，不证明真实设备或生产 P99/SLO。更高 recall 时前级遍历会重新主导；残差/query 分布偏移、校准失配、候选很少或向量可驻内存时，完整向量精化与既有 CPU/GPU 路径仍合理。检索答案质量、在线更新和多租户 policy 继续独立验收。

物理 page locality 与搜索怎样消费一页也需联合验收。把图近邻排到同一 SSD page，只有被读取的其他记录真正参与候选距离/扩展时才可能充分利用这次 I/O；后者又增加距离工作，因此 page shuffling 或 page-level search 各自并不必然更快。[同库有限组合对照](https://arxiv.org/html/2602.21514v1)显示二者在部分 matched-recall 工作点互补；48 workers 下 speculative pipeline 却因 SSD 已饱和而多读未确认候选，低于部分无 pipeline 配置，高维 dynamic width 也有 recall 反退。Layout 重排、离线峰值内存、候选计算和查询全路径必须一起计价，uniform expected-page 近似不签最坏界，禁用 io_uring 的控制也不代表所有引擎。低并发、布局收益不稳或额外扫描不合算时，保留原节点消费与既有异步 I/O，不凭 overlap 名称批准替换。<!-- source-family:SF-2026-ARXIV-2602-21514 -->

同一页怎样进入 cache，还取决于访问偏斜发生在哪个粒度。Page cache 管理简单，但热门 vertex 与冷门 vertex 混排时，整页统计会抹平 record 的热度；只缓存被请求的 record 又可能沿 `P1→P2→P1` 重读同页。因此可把 metric-affine records 共址并共同装入，丢弃同页的其他记录；metric 近邻不等于导航图邻接，group 也可能因页容量被拆开。[受限缓存对照](https://arxiv.org/html/2602.22805v1)在 Sift 中观察到 47.3% vertices 未访问、却只有 0.1% pages 未访问，并在固定布局、10% buffer 的渐进实验中发现：异步 coroutine 提高 QPS，却先恶化平均单查询时延；record cache 再改变这个取舍。Affinity 阈值、batch 与 beam 过大仍会污染缓存或浪费预取，不能把更多 overlap 当作单查询必然更快。<!-- source-family:SF-2026-ARXIV-2602-22805 -->

这条分支支付构建期 affinity、slot/映射状态和预取费用；各系统以自身 disk size 的比例分配 buffer、4KiB/8KiB page 又不同，整体排名不等于同绝对 RAM 下的单因素归因。原文 visited-set 伪码与文字不一致，cache-hit 随 beam 成倍的说法也没有一般概率条件，均不作为终止或正确性保证；这里只采用布局、缓存粒度与披露 Recall@10/mean-latency 的局部取舍。分布不稳、较小工作集能驻内存或质量/时延退化时，保留 page cache、直接搜索或原 beam；在线更新、并发安全与生产 tail 仍须另证。

把热 record 放对位置，仍不保证每页计算便宜。高维 PQ 的逐邻居 LUT 访问可以成为瓶颈；另一条布局分支把 PCA principal 的邻居 codes 按 subcode 跨邻居交错存入 node，让 SIMD 同时算多条距离，并保留 principal 与 residual 供最终精排。这用 disk 复制邻居码换掉全体 PQ 常驻内存；它不是上段 record cache 的替代，也不改变 evidence identity。[同 GIST、Recall@10=.90、R64/BW8 的布局对照](https://arxiv.org/html/2602.23342v1)将计算由约1847降到221μs，却把平均 I/O 次数由77升到131、I/O 时间由1254升到1775μs：计算提速会重新暴露 I/O，而不是消除它。<!-- source-family:SF-2026-ARXIV-2602-23342 -->

同步 beam 等待最慢请求时，还可在部分节点完成后提前发下一 hop，让迟到节点随后更新候选；这是有 recall 代价待验的近似执行分支，不是任意完成顺序等价的证明。PCA、cache、graph/layout revision、磁盘放大与重建共同付费；OOD query 会退化，DPR 构建并不比所有基线快，部分 BigCode 低 recall 工作点也更慢。披露 Xeon/NVMe 的 QPS 与单线程均值不能签生产 P99；分布变化、页放大不合算或 late-arrival 语义无法核验时，保留普通 PQ、同步 beam 与完整向量精排。

### Index Update 可以借用 Search I/O Stall，但不能借走 Freshness Authority

把 index update 与 search 完全串行，状态简单、容易证明 snapshot 一致；disk ANN 在等待随机 I/O 时存在空窗，后台 updater 可以把可分解的更新工作放入这些 stall windows，并由 feedback controller 限制单次 overrun。Search owner 仍固定 query snapshot，update owner 只构建下一 revision，publisher 在完成性和 freshness gate 通过后原子切换，不能让半成品进入候选集。

这提高设备利用率，却会增加 stall prediction、update starvation、tail-latency interference 与双 revision 容量；I/O pattern 变化或 freshness deadline 临近时，应回退独立 update window。`arXiv:2605.19335v1` 的 §4 与 §6 只支持其 LIOS decomposition、bounded budgeting 和 FreshDiskANN/OdinANN experiments，§8 不证明其他 ANN、设备或 production concurrency 同样受益。

<!-- source-family:SF-2026-ARXIV-2605-19335 -->

### Adaptive Fusion 的停止必须有未读贡献上界

固定读取 dense 与 lexical 各自 Top-L 最容易复现，却会在两路高度重合时浪费预算，在排序互补时又过早截断。Exact adaptive fusion 可以先冻结完整列表融合后的 ordered Top-K 作为 correctness contract，再用每路未读条目的最大可能贡献决定是否继续读取；只有剩余项不可能改变 Top-K 时才停止，否则安全耗尽列表。节省来自可证停止，而不是把未读项当作零；反相关排序可能读完整表并更慢，低成本近似或固定 Top-L 在允许有损、严格尾延迟时仍是合理分支。

<!-- source-family: arxiv:2608.07152v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: exact-adaptive-fusion-unread-contribution-bound -->

## 检索表示决定可表达的匹配，而不只是索引速度

把一段内容压成单一向量很便于建立 ANN 索引，却会把多个局部语义关系折叠为一个相似度。token 级多向量匹配扩大了可表达的相关性类别，但代价是向量数量、候选生成、精排和跨设备数据移动同时上升。因而“召回质量更高”不能脱离表示与执行成本单独讨论：表示层先决定哪些证据关系能够被区分，系统层再决定这些关系能否在延迟和内存预算内被实现。
<!-- source-family: arxiv:2608.21494v1; semantic-body-binding: multivector-retrieval-expressivity-cost -->

单向量退化也不能只归咎于维度不够。即使表示维度足以编码某些 top-k 关系，训练域变化、余弦相似度与任务所需
relevance 不一致，以及语料扩大后噪声近邻累积，都可能让真正证据被“相似但无用”的文档淹没。
因此在决定增加维度、换多向量或追加 reranker 之前，应按领域迁移和 corpus size 分层测 recall，分别检查
正例、难负例与最终 answer support。微调可以修复目标域排序，却可能损害原域；多向量扩大表达能力又增加
索引与数据搬运成本。稳定单域、吞吐优先或高召回不是硬要求时，单向量仍是合理基线。
[单向量检索的受控研究](https://arxiv.org/html/2603.29519v1)只支持其 LIMIT/MSMARCO 与模型对照，
玩具推导和作者观察都不证明所有 RAG 语料必然出现同等退化。<!-- source-family:SF-2026-ARXIV-2603-29519 -->

从 dense encoder 转向 late-interaction，还要决定在哪个训练阶段让表示适配新的匹配目标，而非只换输出头再做一次 KD。[受限阶段与接口对照](https://arxiv.org/html/2602.16609v1)比较 dense 预训练后做多向量监督/KD，以及从更早阶段就训练多向量目标；完整多向量预训练有额外成本，局部残余收益又与训练规模混杂，不能据此宣称唯一必要路线。继承的 query/document prompt 与训练长度也属于接口：弱微调时保持原 prompt 有助局部结果，但更强、更长微调可适配新的 prompt，所谓隐式 query expansion 仍是猜想。选择应同时保存起点、各阶段目标/数据/预算、prompt 与长度；复用已训 dense 的成本不等于总生命周期免费，encoder 变化后的索引重建与回归也须付费。资源有限或旧检索已稳定时，保留 dense 起点加多向量监督/KD、原单向量/hybrid，而不是只为更高 BEIR 均值重做全部预训练。<!-- source-family:SF-2026-ARXIV-2602-16609 -->

倒排检索也不必让每一维永久对应 tokenizer 的词。词法维度便于精确标识符匹配和直接解释，语料变化快时尤其容易维护；另一条条件分支先从冻结编码器的上下文状态训练稀疏自编码字典，再用检索目标联合适配编码器与字典，使查询和文档的非零 learned latent 权重进入倒排索引。它改变的是检索输出空间与训练责任，而不是宣称每个 latent 都是跨语言稳定的语义真值。逐 token 取 Top-K 仍可能在跨 token 聚合后形成稠密文档表示，所以重建质量、相关性与最终 posting 预算必须分开验收。<!-- source-family:SF-2026-ARXIV-2604-21511 -->

字典预训练、检索适配与索引重建会增加生命周期成本；编码器、字典和 postings 按同一 revision 迁移，是依据索引可比性提出的工程要求，不是作者已验证的全量热升级协议。[受限 SAE–SPLADE 对照](https://arxiv.org/html/2604.21511v1)只覆盖披露的 DistilBERT/MS MARCO 与多语切片，存在域内或语言退步；启发式共现名称不证明 concept 正确，预期 posting 访问量也不等于真实延迟。精确词查询、预算紧或语料频繁更新时，保留词法/SPLADE 与已验证 hybrid，不能用新的“概念”标签遮蔽匹配错误。下节再处理多向量表示真正产生的物理搬运成本。

缩短检索向量还会改变哪些约束被保留下来。普通 Matryoshka 训练让多个前缀都能做语义匹配，但带时间的问题可能同时需要“内容相关”与“在指定时期成立”；若时间信号被截在后部，短向量可能先丢掉时间条件。一个受限分支把每个可用前缀的前 $t$ 维留给 temporal representation，其余维度承载 semantic representation，并用语义投影目标与时间监督共同训练；这不是把时间简单加进文本，也不是声称所有前缀都具备同等信息。检索表示 owner 需要同时验收时间条件召回与一般语义召回，而不能把低维索引的体积优势直接当成质量优势。<!-- source-family:SF-2026-ARXIV-2601-05549 -->

时间监督的权重增加了新的取舍：过强会损害一般语义表现，过弱则不足以区分时间上错误的近邻。[时间优先前缀与受限评价](https://arxiv.org/html/2601.05549v1#S3)只支持其 LoRA 编码器、六类 temporal embedding models、所测时间问答与 NQ 对照，部分低维配置并不优于基线；它不认证文档时间戳、事件真实性或所有语料的时间推理能力。时间字段不可靠、工作负载不需要时间约束或语义质量退步时，保留普通语义/词法检索并显式过滤时间仍合理。表示训练、监督数据和索引重建也要计入生命周期成本，下节再处理表示实际引起的数据搬运。

表示失配也可以在建索引之前作有限探测，而不只在最终检索失败后更换 encoder。一个条件分支为每个 retriever 构造固定知识图谱竞争池，以实体相关查询是否进入 top-k 的经验比例训练风险读出；再在文档中定位低分实体，补入外部知识的多个检索视图或单个合成视图。它把 **retriever-specific probe → entity selection → index augmentation** 接成可审计的写路径：竞争池、读出、实体映射、外部来源与新增视图都需共同保存身份，而原文仍保留为回读依据。这个比例只是给定探针人口下的可检索性，不能当真实 corpus/query 的失败概率，更不能认证外部知识真值。<!-- source-family:SF-2026-ARXIV-2602-09616 -->

[Argus 的必要对照](https://arxiv.org/html/2602.09616v1)限于固定 Wikipedia/Wikidata 探针及受测八个 retriever；合成视图在 Jina 的 ImpliRet 切片反而退步，多视图和合成单视图不等价。原实验没有控制相同索引膨胀下的随机或全实体增强，不能将全部收益归因于风险选择。探针训练、外部检索、生成、索引扩容与更新失效都增加成本；域迁移、实体误连或增强收益不稳时，保留原索引、lexical/hybrid 与显式 rerank，不让风险读出拥有证据 admission 权。

另一条分支不改 index，而选择值得加入 retriever 训练的合成 query。固定 encoder `φ` 后，用 inverse model 将 `φ(x)` 还原成 query `x̂`，再按相对往返误差 `1−||φ(x̂)−φ(x)||²/||φ(x)||²` 排序，筛选与 encoder 当前表示较一致的增强样本；这是训练数据 selector，不是文档真值、query 可回答性或“容易学会”的充分条件，零范数的实现 guard 也未披露。[RPDR v1 Eq8/9、§4.2–4.3 与 Appendix B](https://arxiv.org/html/2602.17366v1)用相同增强数量和训练设置的 Random 对照，在 PopQA 长尾上为74.5对66.8，但 frequent slice 为81.3对82.7，选择收益并不均匀；可重建问答与错误增强的反侧也不能组成完备的因果 factorial。证据限于 Contriever、T5-base inverse 与短形式单事实检索；复杂 multi-hop/long-form 未验证。生成增强、训练 inverse、重新编码与 retriever fine-tuning 都有成本，部署硬件、并发与 tail SLO 未由这些质量数字说明。域迁移或 frequent slice 退步时保留原训练人口、matched random/不增强基线及现有 lexical/hybrid 路线，不让 roundtrip score 获得 evidence admission 权。<!-- source-family:SF-2026-ARXIV-2602-17366 -->

跨语言表示训练还要区分“以英语为 pivot”与“每种语言都可作为 anchor”。同一 translation group 的多语言正例可以共同约束表示，并用原 encoder 特征作漂移参照；但 translation equivalence 只是训练 proxy，不授文本事实或证据权限。[有限 multi-way 对照](https://arxiv.org/html/2602.21543v1)中，同 pair count 的多语行和双语行拥有不同 semantic instances/训练步数，部分语言与未训练语言退步，不能由几项收益宣布全部语言更好。原loss的denominator排除positive，也不能照称标准normalized contrastive likelihood。翻译、温度/正则搜索、encoder适配与全索引重编码都付费；需冻结translation group、anchor population与revision，在语言切片/迁移失配时保留旧双语训练、原encoder或lexical/hybrid路线。<!-- source-family:SF-2026-ARXIV-2602-21543 -->

组合图像检索还需要表达“修改什么、保留什么、排除什么”。把 reference caption 与 edit 合成一句话便宜，却可能丢掉否定与不变属性；一个受限分支把 query 拆成带正、负、开放 anchor 的属性字典，并把 gallery 字典离线编码到同一 text space。按正项与 anchor 加分、负项减分后再做可控 diversity rerank，改变的是检索约束接口，不把 VLM 抽出的属性认证为像素事实，也不把相似度负项当作硬过滤。[固定字典接口的局部消融](https://arxiv.org/html/2602.22510v1)中，显式负项与仅正项的控制支持 negation 的增量；另一些行同时改变 anchors 和 MMR，不能拆成 anchor 独有因果。MMR 能降低近重复，却并非在所有 caption 基线维持 recall；默认归一化、属性抽取和候选池也属于执行身份。可选自监督训练另付费，不因无需 CIR triplets 而免费；主文未给完整硬件、预算、独立 seed 与附录指标定义，不能签通用增益。抽取漏属性、edit 冲突或净收益不足时，回读原图、保留 caption/原视觉检索与独立 intent 核验。<!-- source-family:SF-2026-ARXIV-2602-22510 -->

属性接口之外，也可同时用编辑后文本与编辑后图像提出候选，再让同一个 candidate verifier 检查 reference、edit 与候选图。固定 similarity 加权在 [CIRCO 的受限同组件对照](https://arxiv.org/html/2602.23029v1)甚至差于单文本路径，因此双路覆盖与排序应分开验收；verifier 的 yes/no 分数可用于排序和触发低分 refinement，却不是校准后的真值概率。尤其同一个候选的 verifier 输入没有 branch 特有证据，把两路分数相加不能冒充两个独立 likelihood。Threshold 过高会多做无益修订，追加轮次收益递减，32B verifier 也不必优于7B；双路都漏目标或共用 caption 误读时，反馈仍会放大共同错误。BAGEL、Qwen2.5-VL、GPT-4o 与 CLIP 的单H20设置只支持该人口的经验选择，额外生成、50候选验证和外部调用必须计价，不以 GPU-hour/指标点代生产 SLO。未校准或预算不足时，保留单路、固定已验证 fusion 与原图核验；refinement 只修 proposal，不创造缺失的证据。<!-- source-family:SF-2026-ARXIV-2602-23029 -->

### 多向量检索的数据面要避免搬运高精度向量

多向量匹配需要细粒度表示，却容易让 CPU 驻留的高精度向量在每次查询时跨总线搬到 GPU，计算加速最终被数据移动抵消。异构执行可以让 GPU 常驻低精度 codes 做 candidate generation 与过滤，再由 CPU 上的高精度数据完成 refinement，并重叠两侧计算。它以额外副本、量化误差和一致性管理换取低延迟；验收必须在相同 recall 下报告 host/device memory、传输量、QPS 与尾延迟，不能只比较 kernel 时间。
<!-- source-family: arxiv:2608.23553v1; semantic-body-binding: heterogeneous-multivector-retrieval-data-plane -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25522:start -->
把 graph-based ANN 进一步迁移到 Processing-in-Memory 时，旧路线仍不能简化为“把距离计算下沉”。十亿级索引还受 index footprint、跨 processing unit 的 graph traversal、host dispatch、候选回传与 rerank 共同约束。一个可行分支是先压缩索引以减少分区和远程跳转，再用异步 mini-batch pipeline 重叠 host 调度、PIM 搜索和 rerank；但控制权仍应留在端到端 retrieval planner，而不是交给单个 PIM kernel。

这条路线以 PIM residency 和内部带宽换取索引副本、分区、overfetch 与专用 kernel 的复杂度，并可能把新瓶颈推到 host rerank 或传输。是否采用它必须在相同 recall 下同时比较 overfetch、QPS、energy 与尾延迟；跨 PU 通信、负载不均或 host 阶段吞掉收益时，应回退已验证的 CPU/GPU ANN 或普通 hybrid refinement。现有 exact-v1 证据只覆盖作者披露的三套 billion-scale 数据、dual-Xeon/A100/UPMEM 环境和 recall@10；multi-node 与新一代 PIM 的部分结果仍含模拟或投影，不能外推为任意硬件与生产并发下的优势。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25522:end -->

混合 text/graph RAG 不应只拼接两路结果。Graph-to-text 通道可用已访问节点为文本证据投票降噪；text-to-graph 通道则把 search history 中被 beam pruning 的 orphan nodes 保存为带 provenance 的 deferred search state，并在文本线索支持时重开。该机制用历史状态与双向校验换 recall/precision，代价是 stale graph、错误 resurrection 与额外融合控制；identity/provenance 不完整时回退独立 text/graph 检索与显式 rerank。

作者仅报告多个 multi-hop benchmark 的相对结果，摘要未披露完整模型、硬件、并发或生产 freshness 条件；不证明通用最优融合。 PLATFORM-SECURITY 只接收 poisoning/authorization handoff；RAG 章节拥有检索状态与证据 admission。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05643 -->

## Retrieval 的基本度量

只让 retriever 读取当前 query，在短问答和稳定输入分布下最简单；但 Agent 可能已在当前推理中形成未写进 query 的实体关系、排除条件或搜索意图。一个条件分支把当前 reasoning trace 与 query 联合编码，再用成功研究轨迹中的支持文档及难负例适配检索训练；它改变的是检索输入与训练分布，而不是让推理文本取得事实权威。Context owner 决定哪些 trace 可见，RAG owner 才负责表示、候选与证据召回。

更多历史不必更好：完整 trajectory 会带入过时假设和无关工具结果，受控消融中甚至弱于当前 reasoning。联合编码新增 trace 可得性、训练数据构造、输入 token 与检索成本，也可能继承 planner 的错误；trace 不可用、噪声大或分布迁移时保留 query-only、lexical 与显式 rerank。[AgentIR v1 §3.2–5](https://arxiv.org/html/2603.04384v1) 的同 backbone 消融支持当前 trace 与检索适配的互补收益，只覆盖其 BrowseComp-Plus 与三种 Agent 配置，不保证任意私有 CoT 可访问或所有任务更快。<!-- source-family:SF-2026-ARXIV-2603-04384 -->

Retrieval metric 必须与 Agent 实际 query distribution 对齐。面向自然问题训练的 dense retriever，未必适合 deep-research Agent 生成的短 entity、keyword 或逐步 subquery；更强 encoder 在接口分布错位时也可能输给 lexical baseline。评估应联合版本化 query generator、corpus/index、retriever/reranker、packing policy 与 context use，并分开报告 source recall、duplicate evidence、search/tool cost 和 final outcome。

Agentic research 还会改变 ranking 的**输入方言**。训练在自然问题或 document query 上的 ranker，面对由 Agent
生成的 entity fragment、keyword conjunction 和逐步 subquery 时可能发生接口漂移。比较 ranker 必须固定：

```text
query generator / dialect
+ retrieval unit and candidate construction
+ ranker training distribution
+ reader/context budget
+ final task and citation verifier
```

让 ranker 直接适配 Agent query 可以提高局部排序，却也可能过拟合当前 planner 的措辞；扩大 reader budget
能掩盖 ranking miss，却增加 token/latency 并改变最终指标。传统 lexical/dense baseline 在 rare identifiers、
稳定 corpus 或低预算下继续成立。Deep Research ranking 的作者实验支持这种 interface-contract 解释，不构成
任意 Agent 或 ranker 的通用排序。

多语言文档比较还有一个容易被隐藏的输入层：视觉 page、普通 OCR 文本与包含图示语义描述的转录，并不是同一份检索材料。保持 retriever 与评价协议不变、只改变 OCR 和预处理后，text-only 路径的表现仍可明显变化；因此“视觉检索优于文本检索”不能只归因于 encoder 模态。评价要共同保存 page 到检索表示的转换器、语言设置、图示描述 prompt、chunk 与索引版本，先做固定 retriever 的输入表示对照，再讨论换 encoder 的增量。

更强转录会增加处理成本，也不能可靠还原空间关系和非文字图形；按同一评价集逐语言选择最佳 OCR 配置还可能乐观地偏向该集合。[2603.04238v1 §3、Appendix C Tables 3–4](https://arxiv.org/html/2603.04238v1)支持检查这种归因混杂，而其中引用的多模态基线并非全部在同一环境重跑，不能推成 lexical 方法普遍胜出。普通文字与稳定语言的简单 OCR/lexical 路径继续合理；图形或布局是关键证据时，保留视觉表示与独立切片验收。<!-- source-family:SF-2026-ARXIV-2603-04238 -->

对于 query `q`，候选集合 `D`，relevance score：

```text
top_k(q) = arg top-k_d score(q, d)
```

Embedding 系统常用 cosine similarity：

```text
cos(q, d) = (q · d) / (||q|| ||d||)
```

高维空间还会让 cosine/距离的对比度收缩：nearest 与 typical neighbor 的 margin 变小后，微小数值误差、hubness 或索引近似都可能重排 top-k。Vector dimension 因而不是“越大表示越强”的孤立参数；evaluation 要同时保存 score distribution、neighbor margin、stability under perturbation 与下游 evidence use，index owner 再据此选择降维、hybrid lexical signal 或拒绝低对比 query。

这些诊断用额外 calibration 与可能的表示损失换可预测检索；它们不能从 synthetic concentration 直接推出某个生产 embedding 已失效。低维、margin 充足或 lexical exact-match 主导时，普通 top-k 仍成立。`arXiv:2606.28330v1` 的 PDF §II–§V 只支持其 concentration analysis、synthetic 与 simplified RAG experiments，§VI–§VII 明确没有生产 embedding validation。

<!-- source-family:SF-2026-ARXIV-2606-28330 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-24322:start -->
这个 margin 合同也要延伸到**检索 encoder 的权重量化验收**。分类准确率接近原模型、权重重建误差很小，仍不能保证检索排序稳定：分类训练往往把正确类与其他类拉开，检索的第一名和第二名却可能很接近；量化使 score 小幅移动，就足以让不同文档占据 top-1。若每个候选 score 的误差不超过 `ε`，原第一名与第二名的差距至少 `2ε` 时 top-1 对该误差预算稳定；差距更小只说明**可能**翻转，不等于必然检索错误。

因此上线同一 retriever 的低精度版本时，应固定 query 与 corpus，并分别版本化全精度/量化 encoder、document embedding 和 index artifact，再配对比较两条路径的 top-1 身份、相关文档留存、gap 分布及聚合 nDCG。身份翻转不是质量损失的同义词，但均值 nDCG 接近也可能掩盖部分 query 丢失原本相关的首位证据。若风险集中在大量小 gap query，按逐层 gap 敏感度分配 bit 可以作为统一低比特之外的分支；代价是全精度参照、校准样本、逐层试量化和更复杂的执行计划。把小 gap 请求一律送回全精度也会损失量化收益，且校准阈值依赖查询与语料分布。这里讨论的是 **encoder weight-only PTQ**，不是索引中已存 embedding 的压缩；现有作者实验未证明 ANN、动态 corpus、不同硬件或生产 SLO 下的普遍收益，简单且 margin 充足的检索仍可保持统一精度和常规 top-k。<!-- source-family:SF-2026-ARXIV-2609-24322 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2609-24322:end -->

除了数值精度，Hubness 还可能成为写路径的信任问题。通常由可信 encoder 从内容构建向量，几何相似才有可追溯的语义来源；若允许外部直接写入任意 embedding，攻击者可以估计语料簇的中心，在其附近放置向量并绑定无关内容，不必修改 query 或 encoder。此时 ANN 返回的只是几何近邻，不是内容经过该 encoder 编码的证明。工程上应让 imported embedding 绑定 source/content digest 与 encoder revision，并按风险执行可信重嵌入或一致性核查；这是由威胁推导的入库设计，不是作者已验证的完整防御。

额外核查增加计算与版本维护；中心性检测也会误伤自然 hub，改变距离度量则可能损伤正常召回，不能据异常直接判恶意。[Black-Hole 的原始实验](https://arxiv.org/html/2604.05480v1)依赖向量注入权限、受限 Gaussian 分析和三个 encoder/三个数据集；其防御 recall 比较的是原空间 clean top-k 的留存，不是答案 truth，更不是所有生产索引的安全保证。后面的安全生命周期仍负责身份授权与隔离处置。<!-- source-family:SF-2026-ARXIV-2604-05480 -->

即使检测分数能把攻击向量与大多数正常向量分开，有限告警预算仍可能漏掉攻击：自然 universal hubs 占据全局排序前端时，固定 top-H 告警先用在这些正常高中心性向量上。[HubScan 的受限实验](https://arxiv.org/html/2602.22427v1)中，全局 ROC-AUC 达 .995，而包含 15 个自然 hub 与 10 个域攻击 hub 的 top-K=H 检查仍可零召回；这反驳的是“排序指标好就足以覆盖告警预算”，不是统计不可见。按相关域的代表性 query 人口重新扫描可恢复部分识别，但 query 代表性、漂移、扫描及人工告警费用成为新条件，污染率增大也可退化。实验依赖索引写入及 query/encoder 知情权限，百万文档离线扫描不证明线上自适应攻击安全；异常 score 仍不是真实恶意标签，处置继续服从 provenance、可信重嵌入与隔离核查，不能自动删除自然 hub。<!-- source-family:SF-2026-ARXIV-2602-22427 -->

相似不等于有用或真实。Evaluation 至少区分：

- recall@k：需要的 evidence 是否被召回；
- precision/context relevance：注入内容有多少相关；
- ranking quality；
- citation correctness；
- answer faithfulness 与 task success；
- latency、token 和 storage cost。

最终答案错可能来自 retrieval miss，也可能是正确 evidence 被生成器忽略。必须逐层归因。

这些是 RAG 的局部 failure taxonomy；第 66 章负责把 model、prompt、index、retriever、dataset、scorer 与 execution trace 绑定成可比较的 Evaluation Run。

### Embedding PTQ 必须绑定 Model Family 与 Retrieval Task

相同 bit width 或 reconstruction error 不会跨 embedding family 保持相同 retrieval quality。量化 policy 必须绑定 checkpoint、module、group size、precision、corpus/task 与目标 Kernel；重构误差只能在同一设置内筛选，不能直接充当跨模型 allocator。<!-- source-family:SF-2026-ARXIV-2609-16391 -->

作者的五个 checkpoint、四个 family 和三个 corpus 未覆盖完整 MTEB、整数 Kernel latency，也没有实现 mixed-precision allocator。因此分层混合精度是待验证的设计选项，不能据此声称已获得部署加速；错误策略可能造成 retrieval collapse。失败时回到已验证的 INT4/FP 或更高精度基线，in-domain distilled student 也须另验 OOD 质量。量化表示与执行成本的通用机制见 [Ch49](../part-05-inference-system/49-tensorrt-llm.md#量化为什么不自动带来加速)。

<!-- june29-owner:AGENT-RAG:start -->
### 度量选择先诊断几何，再验收任务收益

Cosine 归一化长度，适合按该目标训练且几何较均匀的表示；当少数坐标承载过多方差时，角度可能主要反映共同方向，而非任务需要区分的语义。可以先测方差集中程度，再在同一 encoder、数据与评价协议下比较 cosine、rank 或 L1 类度量。这里改变的是检索比较规则，不是获得新的事实来源；候选度量仍需经过真实 query/corpus 的质量与索引成本验证，并写入 index identity。

这一诊断有计算与校准成本，而且坐标级集中度依赖基底，离线相似度收益不自动迁移为 ANN 或在线 RAG 收益。19 个 encoder、19 个 parameter-free metric 与七个静态数据集的对照支持条件化选择，不证明 0.01 的分组阈值是通用上线门槛；去主方向也同时删去其他信息，不能当作干净的因果干预。未覆盖 learned metric 或在线 corpus 漂移。收益不稳时保留已校准的 cosine/hybrid；后文 logical/physical plan 则负责把这种选择纳入可提交的检索配置，而非宣称跨 operator 联合最优。
<!-- source-family:SF-2026-ARXIV-2606-29571 -->
<!-- june29-owner:AGENT-RAG:end -->

度量还要分清 query 与 document 的幅度，以及训练与推理两种角色。对固定非零 query，乘一个正 norm 只缩放其全部 dot-product scores，不改变当次候选排名；document norm 则逐候选变化，可以改写排名。可是在 InfoNCE 训练中，query norm 仍会改变 softmax 的有效温度与梯度，因此“推理排序不变”不能推出“训练时可以任意归一”。分别保留或移除两侧 norm 的匹配对照，才可判断当前 encoder 的幅度是否适合目标任务；这不是由任务名字自动选择 dot 或 cosine。<!-- source-family:SF-2026-ARXIV-2602-09229 -->

[幅度分责的受限研究](https://arxiv.org/html/2602.09229v1)在同训练人口下观察到 scratch 与 fine-tuning 的不同趋势，部分检索项保留幅度仍退步；dot 对称也不意味着幅度必然无用。它不提供通用 symmetry 规律或安全默认 norm gate，学习门控还新增训练与校准成本。encoder、两侧 normalization、训练温度、索引向量和评分规则应一起版本化；表示迁移、排名或 held-out 质量不稳时，保留已验证的 cosine/dot 与 hybrid，不能只凭 score scale 或一组聚合指标批准全索引重建。

固定分数接口后，多个 positive passages 的训练目标仍会重新分配更新责任：等权联合目标推动正例概率靠近均分，sum-marginal 更偏向当前高分正例，pairwise log-sum-exp 则给低分正例更强补偿。它们改变的是已标正例间的梯度权重，不证明标签同质、score 就是真实相关性，或增加正例总能提高排序。[多正例训练的有限对照](https://arxiv.org/html/2602.12727v1)中 recall 与 MRR 的最佳目标不同，更多正例也会退步；随机抽一个正例的预期 Single-LH 梯度并不等于一般 LSE-pair 目标，不能用 stochastic approximation 一词签无偏。标签来源/质量、负例池、温度、batch 和搜索/epoch 预算须一并保存，额外标注与训练另计；弱正例噪声、预算或排名回归时，保留质量筛过的 single-positive、原目标与 hybrid retrieval，答案支持另验。 <!-- source-family:SF-2026-ARXIV-2602-12727 -->

当 relevance 有完全相关、部分相关与无关三个等级时，同一部分相关文档不必永远被标为 positive 或 negative：它相对无关项可提供正向关系，相对完全相关项又可承担负向关系。因此应把 grade、当前比较对与训练 stage 一起保存，而不让随机 in-batch 文档自动获得“无关”真值。[分级检索的受限训练](https://arxiv.org/html/2602.17654v1)先学习原始多正例关系，再用当前 encoder 的 ANN 候选经标注器重判，挖掘排名过低的相关项与过高的无关项；第二阶段保留原负样本，避免只追新 hard pairs 丢失旧边界。该角色变化不要求把等级间距当 cardinal utility，也不证明 cosine score 已校准。标注和离线评价共用 finetuned LLM、只有约30%评价 query 未在训练出现，部分增广虽改善平均指标却损伤分离度，故有限相同 backbone/dimension 对照和整套线上检索收益不能单授 grade/mining 因果。重标、ANN、两阶段训练与重建索引均计费；训练硬件、precision、batch 和完整服务 SLO 未披露。弱标签失配、旧支持遗忘或收益不足时，保留可独立核验的 binary/single-positive 标签、原负样本与 hybrid 检索，答案证据另验。<!-- source-family:SF-2026-ARXIV-2602-17654 -->

若 dense 向量的存储和比较成本成为瓶颈，还有不同于 encoder 权重量化的表示分支：从语料向量建立多组随机空间划分，把文档表示为各树的 leaf index，query 仍经原 encoder 后映射到同一组叶子，以碰撞次数排序。压缩的对象变成由语料导出的 partition code，同时改变检索 score；它不是保持 cosine 的无损短码。采用这种表示时，encoder、corpus snapshot、划分树、query mapping 与 ANN index 必须绑定同一身份，语料或 encoder 变化后重新验证或重建；即便不做梯度训练，base encoder 和在线映射也没有消失。<!-- source-family:SF-2026-ARXIV-2601-09159 -->

更多树或更细划分增加码长、构建、全语料映射与查询成本，不能只报告压缩后向量大小。有限 CPU、两个高维文本 encoder 和静态语料实验支持这一可行分支，却在部分检索任务出现 nDCG 退步；索引搜索时间也不等于包含 query encoding 的端到端服务成本。应配对保存 dense 与碰撞度量的召回、排序质量和完整资源账，另验动态语料与 ANN 路径；不从随机划分直接推导叶子均匀、bit 独立或相关性层级保证。质量或身份不稳时保留已验收的 dense/cosine、hybrid 或其他压缩方案，不以较短 code 取代相关性门槛。

## Chunking 是信息边界设计

Chunk 太小：

- 缺上下文；
- 同一事实跨 chunk；
- 候选数量和 index overhead 增加。

Chunk 太大：

- embedding 表示混合多个主题；
- 无关 token 占 context；
- 精确 citation 困难；
- Prefill 成本增加。

更合理的策略结合 document structure、semantic boundaries、overlap 与 parent-child retrieval。没有对所有语料通用的 chunk size。

对于图表、表格和解释文字互相依赖的文档，按 parser 原始元素逐个建索引虽然简单，却可能只召回标题而漏掉数据本体。另一条条件性路径是先把不同 parser 的元素类型归一为稳定的语义角色，再将图表、caption、单位和解释段组成同一个可检索 evidence unit；unit 保留 source revision、page/region locator 与构建它的 parser 版本。这样换 parser 时可以检验同一证据单元的内容和区域是否稳定，而不把元素级 bbox 或 label 当成不变身份。小 chunk 仍适合精确文本查询，unit 不能因“语义完整”就自动取得答案权威，reader 仍要回到原页核验。

组合单元会拉长 embedding 输入、增加构建和权限过滤成本，并可能让短 query 的相似度被无关内容稀释；跨页引用和 parser 误识别也不会因单页分组自动消失。原始实验只覆盖两种 parser、1,340 页和自动构造的 1,551 个问答；其中图决策层的部分恢复/验证规则尚未在 runtime 执行。因此这里吸收的是**先规范证据角色、再比较 parser 变化后的可检索单元**这一设计分支，不是对任意语料的 parser independence 或生产 RAG 质量保证。<!-- source-family:SF-2026-ARXIV-2604-00500 -->

证据单元还可以把**选择身份**与**当前展示视图**分开。固定 chunk 在结构弱、精确文本查询中简单可靠；HTML 的一个句子若依赖远处标题、列表层级或表格行列头，单纯扩大 chunk 又会让无关内容参与匹配。另一条分支将原文树上的 path-set 保存为选择对象：embedding 时补入使它可解释的 global context，命中后才按预算展开附近的 local view，再由 reader 选择、合并并映回原路径。同文结果共享的结构 scaffolding 可以合并，而不是每次重复附带一份；检索匹配粒度、展示粒度和 citation identity 因而不必相同。<!-- source-family:SF-2026-ARXIV-2604-20849 -->

该分离增加 tree/parser 维护、展开和生成式过滤成本。Path 只在绑定的 document revision 与解析规则内可重建，不是跨修订稳定身份，更不是 support 真值。标题缺失、布局错误或结构规则不适用时仍应回退原始 evidence unit 或固定 chunk，并由 Context budget 与最终答案验收限制展开。[受限 HTML 实验](https://arxiv.org/pdf/2604.20849v1)用两数据集各400题与1000-token citation budget测 helpful citation 比例，不测答案准确或支持完备；Hotpot 上纯 embedding 的比例略低 block，关闭 global context 又容纳更多 helpful 总数。加入 filter、换 encoder 和改变 citation 粒度也会影响比较，不能把更高比例外推为所有语料、等成本或生产SLO优势。<!-- source-family:SF-2026-ARXIV-2604-20849 -->

Late-interaction retrieval 又引入独立的 index budget。文档可以保存多个 token/patch vectors，以更细粒度匹配
query；直接保存全部向量提高表达容量，却扩大 storage、memory traffic 和 rerank cost。把一组 vectors 压成固定
预算的代表向量，改变的是 persisted index state，不会让 encoder 无需读取原始 document，也不会让 query-time
reader cost 自动同比下降：

```text
raw multimodal document
→ encoder produces token / patch vectors
→ budgeted compression builds index artifact
→ query late-interaction against compressed state
→ optional source dereference and reader verification
```

压缩率、encoder revision、vector budget、distance rule 与 reconstruction/selection policy 必须进入 index identity。
更小 index 用 recall、rare evidence 和 rebuild cost换容量；single-vector embedding 在吞吐与治理优先时仍合理，
full multi-vector index 在高召回和容量允许时继续成立。Multi-Vector Index Compression 的实验只支持特定模型、
数据集和 budget 下的 frontier，不证明 indexing path 或端到端 latency 等比下降。

固定向量预算还可以按**查询实际需要哪一个 patch**分配，而不只按文档向量的几何密度重建。先用离线 query tokens 估计原始 MaxSim 的胜出频率，将它作为 source marginal；再以 target-balanced 的熵正则 transport 把重要源向量软分配给有限代表槽位，随后用 Lloyd readout 生成压缩向量。在线仍执行固定 compressed MaxSim，不逐次查询重建索引。这把需求校准与在线评分分开：使用 1,000 个 query tokens 可能只对应几十个查询，其分布、backbone 与 encoder revision 必须进入校准及 index identity。<!-- source-family:SF-2026-ARXIV-2609-21018 -->

需求加权增加 query-token 校准、源×槽位 transport 与 readout 成本；软计划的平衡也不保证最后硬 cluster 等大。[MAGIC 的 Proposition 1](https://arxiv.org/html/2609.21018v1)只在 unit document vectors、query norm 不超过 1 且使用真实 population 胜出概率时，约束期望的正向 score decrease，不约束绝对评分误差、分数虚增、排名或召回。估计需求可能漏掉 rare intents，换 backbone 要重建；受限 ColQwen2.5、2,000 页、单 H20 的穷举实验在较宽保留向量预算下仍有切片反退，per-page 构建成本也不能冒充全局字典或端到端 RAG/QPS 成本。验收失败时仍应恢复更大预算、完整多向量索引或 source dereference，而不从这一上界推导任意 query 的证据保全。

Index budget 之外，late interaction 的聚合器也决定训练信号流向哪里。Hard MaxSim 对每个 query token 只把直接梯度送给得分最高的 document patch；短且目标明确的文档中，这种稀疏选择有利于区分，但更多 patch 或定向 hard-negative spike 会增加偶然极值占据最大值的机会。Top-k 平均可分散梯度，却仍可能让整个 top-k 被 spike 占满；更平滑的 softmax 也可能稀释有效关系。因此 pooling 必须连同训练目标、长度切片与定向/随机干扰对照验收，不能单独按梯度均匀程度选优。

[Spike Hijacking](https://arxiv.org/html/2604.05253v1)在受控合成训练中观察到最平滑版本质量反而最低；真实 ColQwen2.5 的 160-query 对照仅在推理时替换聚合器，没有分别重训，也没有测生产攻击频率。它支持这一稀疏性与鲁棒性的条件取舍，不要求所有多向量索引弃用 MaxSim。<!-- source-family:SF-2026-ARXIV-2604-05253 -->

## Reranking 与 Context Packing

Retriever 优化高 recall，cross-encoder/LLM reranker 可用更强交互提高 precision，但增加 latency/cost。

交互的成本还可以沿信息流拆开，而不必在双塔与全量 cross-encoder 之间二选一：早层分别编码 query/document，后层固定 document 表示，由 query 读取它的 K/V，同时保留 query self-attention，再由 CLS 读取 query 得分。冻结的是 document 的更新，不是删除 query→document 的读取；这种受限结构需要按相应 mask 重训，不能对现成模型任意删交互后继承原质量。[MICE 的有限对照](https://arxiv.org/html/2602.16299v1)发现去掉 query self-attention 会使排序崩溃，部分跨域配置也低于原 cross-encoder；速度比较还共同减少层/参数，不能全部归于单向交互。预计算文档需存储、刷新与版本绑定，原研究没有实现完整索引/第一阶段召回；候选召回和最终答案支持仍另验。文档常变、分布迁移或质量回退时，保留普通 cross-encoder、late interaction 与独立 retriever，不把预计算可行性当成完整在线服务收益。<!-- source-family:SF-2026-ARXIV-2602-16299 -->

若检索器只学语义相似，读者真正需要的答案信息可能排在后面；把强 LLM 放在每次检索的重排路径上虽能评估下游效用，却使在线成本随候选数增长。一个条件分支把指定 reader 对参考答案的偏好留在**离线训练**：先对候选文档估计生成效用，以成对排序训练较稳定的 utility proxy，再把候选间的软效用分布蒸馏进双塔 embedding；线上仍用 ANN 取回，不逐候选运行 teacher。这改变的是第一阶段检索目标，而不是让 embedding 相似度成为答案正确或文档支持的概率。Teacher、参考答案集合、候选池与索引版本共同决定该目标；换 reader 或答案空间时必须重验，不能只复用旧向量。<!-- source-family:SF-2026-ARXIV-2604-22722 -->

离线 LLM 标注、proxy 学习、hard-negative 选择和重建索引是新增成本，teacher 的措辞/长度偏好还可能把有用文档误标为负例。UAE 的 QASPER、NewsQA 受限实验并非各项都优于效用重排对照，报告的检索阶段速度也不含离线训练与最终生成；因此只有固定 reader、稳定语料和足够可校验答案对时才值得采用。reader 常变、需要跨文档组合或人工 provenance 高于代理效用时，普通语义/词法候选加独立 reranker 与 evidence gate 仍是清晰的基线。<!-- source-family:SF-2026-ARXIV-2604-22722 -->

离线 teacher 固定时，效用标签容易版本化；若 reader 也在更新，还可以将被选文档的历史回答成功率平滑成排序标签，交替训练 reranker 与 generator。这里历史值拥有的是指定 query、consumer 和曝光人口下的成功代理，不是文档独立因果效用：答案可能来自模型原有知识，旧 reader 的失败也可能因消费能力而非证据不足。更新 consumer、候选池或曝光策略后，统计须分版本重验，不能把累积标签当作永久文档质量。<!-- source-family:SF-2026-ARXIV-2602-18734 -->

[历史反馈排序的受限实验](https://arxiv.org/html/2602.18734v1)在训练时只选 K=1 文档，部署却选 K=3 或 7；单文档反馈不能自动认证组合证据、文档顺序鲁棒性或单个模块可迁移。初期 Llama 文档标签、generator rollout、历史存储和两个模块的 LoRA 更新均付费，pairwise 排序代理也不是严格 GRPO 等价。仅 PopQA 训练及其他任务的局部反侧不授通用共同优化优势；consumer 漂移、标签失准或净收益不合算时，保留固定 reader 的离线效用、普通 reranker 与独立 evidence gate，而不由最终答案一次成功替代文档支持核验。

两阶段不一定要训练两套完全独立的表示。若同一个 passage encoder 既负责第一阶段召回，又把每篇文档压成一个向量供 listwise reranker 读取，训练目标就承担了两种不同责任：候选集之外的相关文档必须能被 encoder 取回，候选集之内的文档还要经交互后排对次序。只用重排损失更新共享 encoder，固定候选池上的排序可以维持，独立检索能力却可能退化；因此 retrieval 对比目标不能被看似正常的 rerank nDCG 静默删除。一个条件性分支让 encoder 与 reranker 联训，分别保存两项目标及文档向量、索引版本，再用固定候选池测重排、用重新构建的真实候选池测召回与最终答案。把每篇候选压成单向量、以 contextualized passage state 和 query 汇总 state 一次打分，可以避开输出排序文本的 decode，但不会恢复压缩时丢掉的证据。<!-- source-family:SF-2026-ARXIV-2604-22180 -->

这条分支用双模型全参数训练、离线编码、索引重建与表示耦合，换取更短的重排输入；“每篇一个 token、零生成 token”只描述重排器的部分执行，不能代替端到端时延或训练/更新成本。受限实验中，去掉 encoder 检索损失后重排均值未下降，作者报告第一阶段能力退化；dense-only 的跨域候选池也不总胜 BM25，融合反而可能更稳。因此上线要同时验收 lexical 与 dense 候选覆盖、编码/索引刷新、listwise 排序和最终 evidence use。检索域转移、embedding 维度不匹配、重编码预算过高或简单 BM25 已足够时，保留独立 retriever 加普通 reranker，比强行合并更容易维护。该论文只在 Qwen3 4B、TREC DL 与八个 BEIR 数据集的披露设置下支持这项取舍，不能证明任意语料的生产并发收益。<!-- source-family:SF-2026-ARXIV-2604-22180 -->

扩大 reranker 还应先声明拟合的目标。候选集上的 Contrastive Entropy 用正例相对负例的 softmax 概率衡量 score/margin，是连续诊断；NDCG 则衡量相关性等级的相对顺序。连续 proxy 不一定拥有更平滑、可外推的 scaling：受限对照中，NDCG 随模型规模与训练曝光较稳定，而 pairwise 模型的 CE 仍有波动，即使已经归一 scores。因而应直接在最终 ordering metric 上做 held-out checkpoint 预测，并把 CE 留作校准/间隔诊断，而不是互相代签。<!-- source-family:arxiv:2603.04816v1 -->

这里的 data exposure 是同一固定数据集在训练中已消费的样本，不等于新增独立数据或领域多样性；first-stage 候选、negative sampling、score normalization、模型家族和 held-out 范围都属于拟合身份。[Ettin 的受限研究](https://arxiv.org/html/2603.04816v1)只覆盖 17M～1B、MS MARCO/BM25 top-100 与 TREC 切片，不能把局部幂律扩成跨语料或任意规模预算保证。多配置训练与诊断增加成本；分布改变、外推误差大或预算不足时，继续用实际下游评价、checkpoint sweep 和固定已验证模型，而非仅凭平滑 surrogate 批准更大训练。

当排序输出只是文档相对次序时，逐 token 生成排序文本并非唯一接口。可以把 query 放在候选文档之后，选取特定 attention heads 的 query→document 权重作为连续读出，用相关性等级构造偏好对训练该读出；最终前向可在最深被选层截断，因为该层已经提供需要的排序信号。这条分支把排序责任从文本生成迁移到受监督的 head/weight/readout 联合 artifact，避免的是排序文本 decode，而不是全部 attention 计算。截断仅保留所选排序读出，不意味着与完整模型答案等价，更不把 attention 当因果解释。<!-- source-family:SF-2026-ARXIV-2604-17237 -->

head 选择、训练权重、候选位置与长度、连续得分汇总和截断层必须共同验收；训练后重新选 head 也会改变部署 artifact。原文 211 个训练 query 派生多个偏好对，不是只有 211 次免费计算，显式 attention materialization 与训练仍有成本；有限 Qwen3、top-40 与特定执行配置中部分质量切片退步，生成基线的候选窗口也不完全相同。格式总能解析只消除了输出格式失败，不证明 relevance、evidence support 或最终答案正确。标注与执行条件不成立时，cross-encoder、完整前向或生成式 reranker 仍是有效基线，应比较总成本与独立质量，而不是只比较有无 decode。<!-- source-family:SF-2026-ARXIV-2604-17237 -->

Head readout 还可以从训练后静态集合变成 query-conditioned 集合：离线为每个 query 标记合适的 head subset，再训练 query router 在线选择读出组合。Router 拥有读出 proposal，不能把选择 head 写成底层不计算那些 heads，也不能把 attention weight 当作 relevance truth；静态 subset 仍是更简单的 baseline。<!-- source-family:SF-2026-ARXIV-2604-24608 -->

逐 query 标注、router 训练与在线选择增加成本，domain shift 会让旧 subset 标签失效；数学、代码和跨域切片的反向结果说明动态路由并非稳定优胜。应比较包含 label/router 成本的完整前向和最终排序质量；标签预算不足、路由漂移或收益不稳时，回退静态 head、普通 reranker 或完整 reader。

排序标注不足时，还可在开发 query 上逐层测读出，固定 peak 附近的 layer interval，在新数据上只聚合该区间；null query 校准和候选反序用于减轻位置/内容偏差，前向在最深选层后终止。这与受监督 head 或在线 query router 是不同分支：它省去任务排序训练，却仍付开发集层搜索、额外校准前向和 attention materialization；截断只服务排序，不保完整模型答案。[有限跨域对照](https://arxiv.org/html/2602.22591v1)中 Qwen3-0.6B 固定区间在 BEIR 略低于全层；Llama 单次 listwise 变快却稍降排序，反复 heapsort 调用又能吞掉 layer-only 的省算。BRIGHT 按测试子集选择最好层是 oracle 上界，不是部署 zero-shot 策略；两组 A100/300words 与 L40/128tokens 协议不可合并计价。因此不存在由这些实验认证的“所有模型中层最优”，更不把 attention 当 relevance truth；域偏移、校准开销或多次调用不合算时，保留全层、普通 reranker 与完整前向。<!-- source-family:SF-2026-ARXIV-2602-22591 -->

无论排序分支如何，Packing 还要处理：

- evidence authority 与 freshness；
- redundancy/diversity；
- source conflicts；
- position bias；
- per-source/token budget；
- citation mapping。

把 top-k 简单按 score 拼接，会让重复内容占满窗口并掩盖少数反例。

在交错的 search–reasoning history 中，Packing 还决定外部材料在因果序列里能看见什么。若新文档只追加在已有推理后面，它的编码便能读取旧推理；一个替代分支保留原交错 history，同时把检索文档另按新到旧复制到 question 与旧 reasoning 之前，让这一副本文档在 causal mask 下不读取那些推理。双视图分别保留操作历史和较少受旧推理影响的证据编码，并不是删除旧 history，也不等于在原 slot 重复一遍 token。[受限文档位置实验](https://arxiv.org/html/2602.09517v1)固定 gold 文档并改变 pre-search reasoning 长度，及 repeat/stack-only 对照，支持这个消费接口的局部边界；语义匹配仍只是检索证据，不获得 truth 或 authority。<!-- source-family:SF-2026-ARXIV-2602-09517 -->

双视图支付文档副本的 context/token 成本；每轮重插 prefix 还可能影响已有 KV 的复用，这是缓存布局上的系统推断，不是该实验已经测出的 runtime 收益。作者任务中也有退步，位置控制不能证明唯一 attention 因果，更不能保证旧推理偏差、错误文档或 prompt injection 全部消失。Reader revision、两个视图的 document identity/citation mapping、预算与 history layout 应一起验收；收益或 cache 成本不合适时仍可保留普通交错 history、独立 evidence gate 与原 packing，而不把复制当作全负载必要步骤。

Packing 决定哪些材料进入 reader；质量 proxy 还可以跨过这个边界，成为 reader 内部可训练消费的条件。[一项受限实验](https://arxiv.org/html/2601.09028v1)把 retriever 相似度、reranker 与 query-performance predictor 的文档分数转换为 token-level indicators，再调节 attention 并以答案监督训练 decoder。这不是只把文档按分数排好，也不把 relevance 认证为 truth 或 authority；indicator 来源、文档/token 映射、归一化、训练数据与 reader revision 必须一同保存。原文矩阵与附录维度、负值缩放语义有未清之处，不能照抄为精确 recipe，更不能声称低分文档的 attention 必然单调减少。<!-- source-family:SF-2026-ARXIV-2601-09028 -->

该分支增加在线 ranker/QPP、indicator 维护和 decoder 训练成本；只比较 attention 附加计算，不能代表完整检索与生成开销。显式 guidance 与 noisy-context training 共同影响结果，局部聚合多个指标反而会退步，噪声训练单独也可能更强；应分别验收质量特征、归一化和训练干预，而不是把综合收益全归给内部 attention。域转移、proxy 漂移、分数接口不稳定或额外成本不值得时，普通 packing、独立 reranker 与原有 SFT reader 仍是清晰退路，最终答案继续经独立 evidence gate 验收。

Pointwise relevance 仍把文档看成彼此独立；真正进入 Context 的却是一个 evidence set。多个高分文档可能重复
同一主张，也可能互相冲突，却没有覆盖 rubric 的关键维度。Setwise selection 应把目标从分数求和改为受预算
约束的联合效用：

```text
authorized candidate documents
→ declared rubric / claim obligations
→ evaluate coverage, redundancy, conflict and complementarity
→ select a bounded evidence set
→ preserve per-document provenance and rejected alternatives
→ answer / abstain / escalate
```

Rubric 本身可能遗漏真实问题，LLM judge 也可能同时影响 selection 与 generation，因此 set utility 不是 ground
truth。Pointwise/listwise rank 在问题单一、文档同质或低延迟优先时继续合理；setwise policy 只在 coverage/conflict
确实主导 failure 时值得额外成本。Rubric-Oriented Document Set Selection 的作者实验支持这一受限分支，不证明
其九维 rubric 或 judge 可跨领域直接迁移。

证据集覆盖更多立场，不保证生成器在同一 query 的多次回答中表达不同而有效的观点。开放多答案目标需分别保存输入证据的互补性与输出 claim 的差异，并共同验收相关性、事实支持和相同预算下的质量；新观点 reflection 和多轮 MMR 只提出搜索/生成方向，不能把 embedding 距离升级为 truth。Claim 抽取、相似度阈值与 judge 共同定义多样性分数，模板变化或无关长答案也会抬高它。多轮搜索/记忆增加成本，输出 diversity 无增量或 quality 退步时保留单轮检索或普通多样解码，不为观点数量追逐偏题。<!-- source-family:SF-2026-ARXIV-2602-00238 -->

### 文档也可以成为独立生成分支，而不只是拼接片段

把 top-k 文档拼成一个 Context，适合证据需要跨文档交叉组合、单次生成和共享 query prefill 的场景；但文档顺序、长上下文稀释与逐文档归因会纠缠在同一次前向中。另一条条件分支让每篇文档分别条件化同一生成 prefix，训练一个文档先验，并用各分支对已生成 token 的似然逐步更新文档后验，再按后验混合下一 token 分布。这样可保持文档分支身份，并在后验集中时剪去低权重分支；它改变的是**生成状态的组织方式**，不是把检索相关性直接升级为事实支持。后验衡量哪个条件分支更能解释当前输出，不能替代上文的 evidence-set coverage、跨文档关系或独立 sufficiency gate。<!-- source-family:SF-2026-ARXIV-2604-22678 -->

分支化要重复 query 编码并保存多份 KV；不剪枝时，分支数增加会使解码比拼接更慢。剪枝又可能过早丢掉少数关键文档，而单文档边际化并不能显式表示必须联合阅读两篇材料的证据组合；训练阶段还需让模型学会分支混合。BERAG 的受限视觉问答实验显示其特定后验剪枝可改善所测 decode 时间，但无剪枝版本在 K=50 时更慢，且论文未证明端到端 prefill、吞吐、并发或生产 SLO 优势。证据需要互补文档、训练与多份 KV 预算不足，或简单拼接已满足质量和成本时，保留拼接及其独立证据核验更合理。<!-- source-family:SF-2026-ARXIV-2604-22678 -->

### Recall 还要服从固定 Context 的可用工作集

提高 gold-file recall 在 Context 充足、证据独立时通常有利；固定 slot/token budget 下，加入更多文件会降低单文件深度、证据多样性或关键依赖的完整度，最终 resolve rate 反而可能下降。Retrieval policy 因而要同时报告 recall、每项读取深度、跨源 diversity 与下游任务成功，并允许在边际证据不再提高 sufficiency 时停止。这个结论不是“recall 有害”，而是 capacity 约束改变了目标。`arXiv:2608.14838v1` 的结果绑定 12-slot coding context 与作者任务，不能外推任意 RAG 或 corpus。

<!-- source-family:SF-2026-ARXIV-2608-14838 -->

## Relevance 不等于 Sufficient Context

一个 chunk 可以与问题高度相关，却没有包含回答所需的 decisive fact。因而 RAG failure 不能
只分成“检索到/没检索到”，至少要拆成：

```text
retrieval relevance
  candidate 是否谈论同一主题

context sufficiency
  当前 evidence 是否包含形成确定答案所需的信息

generation faithfulness
  输出是否只使用并正确组合这些 evidence
```

Sufficient Context 工作把 context 定义为：包含给出 definitive answer 所需的全部信息；若
关键事实缺失、证据不完整/不确定或互相冲突，则属于 insufficient。这个概念把 retrieval metric
推进为 control signal：

```text
retrieve and pack
→ evaluate sufficiency
→ sufficient: generate + claim/evidence check
→ insufficient: re-query / decompose / broaden source
→ still insufficient: abstain or escalate
```

它解决的是“相关文档诱导模型凭参数记忆补全”的问题，但也新增一个 evaluator。LLM-based
sufficiency rater 可能受领域、prompt、position 和自身知识影响，不能被当成 ground truth；
应使用人工标注切片校准，并记录 rater/version、false-sufficient rate、额外 latency 和
abstention cost。论文在若干 QA datasets 上报告 selective generation 改善，只能支持这个
机制方向，不能外推成固定阈值或所有 corpus 的通用收益。

旧的 relevance/reranking 仍然成立：它们负责高效找到候选，sufficiency gate 负责判断候选
集合是否已足够。前者不能被后者替代，后者也无法从未召回的 corpus 中创造 evidence。

补查也可以改变 retriever 的训练接口，而不只扩大同一 query 的 top-k：让后续 retriever 同时读取原 query 与已被 relevance verifier 选中的有限文档 context，训练时以已有 gold context 之外的 gold 文档作正例，专门提议尚未覆盖的证据。[原版本的双检索机制](https://arxiv.org/html/2602.18425v1#S3)使 query-only 召回与条件补缺承担不同责任；这里的 verified 只是相关性选择，不是事实真值、完整性或答案支持证书，最终输出还会补入未全部验证的检索文档。Verifier 错误与冗余 context 会反馈到下一次检索，LLM 多轮增益可提前停滞，gold-string oracle 也不能被当作线上语义真值。双模型训练、双索引、context 编码与 verification 均付费，少验证预算或跨域可退步；须分别验收补缺 recall、最终 evidence sufficiency 和 claim support。回读不稳、预算不足或证据仍缺时，保留 query-only/lexical retrieval、原 reranker 与独立 sufficiency gate，不以多轮或新文档数宣布证据集完整。<!-- source-family:SF-2026-ARXIV-2602-18425 -->

还应区分“证据尚未找到”与“当前问题没有可确定的答案”。对确实可答的题，继续检索可能补足支持；对知识未知、用户意图未定或互相矛盾而无法裁定的问题，更多搜索也可能增加貌似相关的材料，让模型从应拒答转为无依据回答。尤其 intent 含糊时，需要先澄清任务，而不是把 query expansion 当作消除意图不确定性的办法。[受限双人口对照](https://arxiv.org/html/2601.05503v1)显示搜索轮数在可答与应 abstain 人口上有不同取舍，few-shot 更早拒答也会牺牲可答题；固定 token-price 系数与模型 judge 不等于真实账单或独立 gold。额外检索、澄清与审核都要计入成本；没有可信可答性标签时保留原始结果、请求澄清或保守 abstain，不把轮数或一个统一阈值当 sufficiency 证明。
<!-- source-family:SF-2026-ARXIV-2601-05503 -->

把同一 query 的候选按顺序分成窗口、遇到答案即停，是节省 reader 输入的合理分支，却改变了 gate 的暴露人口：单个无支持窗口上的拒答表现，不等于连续经过多个阴性窗口后仍能等到真正支持答案的窗口。排序既改变 first-positive 之前的窗口数，也改变窗口内容；只统计这些负窗口的误答，不能当成全部无答案问题或所有模型的幻觉率，也不能假设各次错误独立。应同时记录 candidate 顺序、已访问窗口及其支持标注、首次错误早停、调用与 token 预算，并在独立阴性人口上检查拒答边界；少样本提示不能自行保证消除重复暴露风险。每次拟提交答案仍须通过独立的 claim/support gate，支持不足时继续拓宽 Context、回到完整证据路径或保守拒答，而不是把 reader 的早停当作检索已经成功。<!-- source-family:SF-2026-ARXIV-2512-23836 -->

### 多语言证据要分开候选覆盖与语言偏向

单语语料中，用相关性重排再验答案支持，是成本清楚的基线；当同一问题的证据散落在不同语言中，检索器即使已把异语关键文档放入候选池，重排器仍可能偏好查询语言或高资源语言，将其挤出有限的 Context。此时只看总体 top-k 相关性或最终答案均值，分不清是候选缺失、重排偏向，还是 reader 无法利用已选证据。多语言 RAG 应在同一 query、corpus 与候选池下，按**证据语言**分别验收候选覆盖、重排后留存、证据充分性和最终答案支持；query language 与 document language 是不同字段，不能用前者代替后者。重排器只拥有排序 proposal，原始文档继续拥有事实来源，answer gate 独立判断是否足以提交。<!-- source-family:SF-2026-ARXIV-2604-20199 -->

这种切片增加语言识别、跨语标注与候选池构造成本，也可能把语料原本不均衡误判成模型偏向。离线按各语言分别生成答案、再用**已知答案得分**挑最佳语言，可以诊断候选池中的可用证据上界，却不能变成上线时可调用的选择器。受限的 13 语言 MKQA 实验只测试 BGE-M3 候选池后的 reranking；其 character 3-gram recall 改善小且部分语言退步，不证明每种语言均受益，更不证明事实支持或生产公平。语料和用户任务确为单语、普通重排已满足支持检查时，旧路径仍更简单；跨语言切片出现缺口时，先定位 retrieval、reranking 或 reader 的责任，再决定是否值得引入效用监督和额外成本。[受限机制与实验](https://arxiv.org/html/2604.20199v1)

即使 query、evidence 与 output 都固定为同一种语言，reasoning language 仍是另一条控制轴：它可能影响证据整合，但不应默认强制与其他三项一致。保持检索内容、预算和模型不变，再分别比较无约束与指定推理语言，才能定位语言对齐的净值；人工反侧与多语执行增加费用，未校准时保留模型原生推理路径。[German 单语 RAG 的受限对照](https://arxiv.org/html/2610.03136v1)中，强制 German 优于 French，却未超过无约束 English；单一虚构领域的 585 单段与 30 人工 multi-hop 问题、同 family judge 不支持所有语言统一采用同语推理。<!-- source-family:SF-2026-ARXIV-2610-03136 -->

### Query 本身也要经过 Robustness Gate


传统 top-k 默认 query 的实体、时间、范围与前提可信；在这个前提下，按 relevance 召回再判断 sufficiency 是最短路径。可当用户问题带有错误前提或确认偏误时，高相关文档可能只是更擅长迎合错误方向。一个受限分支可以对 query 做保持任务意图的 counterfactual perturbation，比较候选证据能否在前提变化后继续支持同一决策，再把稳定性作为 relevance 与 sufficiency 之间的独立风险信号。Critic 只拥有 evidence-risk proposal；原始来源和 answer gate 仍拥有事实与提交权。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01302 -->

这一步用额外扰动、critic 校准和更多 abstention 换取对迎合性检索的抵抗，也可能因偏误模板覆盖不足、critic 漂移或真实问题本就不稳定而误杀证据。普通 query、低风险检索或无可靠扰动集时，仍应沿用 relevance → sufficiency 主线；高风险结论则回退多源原文核验或人工判断。作者证据只覆盖其 decision benchmarks、扰动合同与 critic，不能把 robustness score 当作事实概率或生产固定阈值。

### Evidence Access Right、Cost 与 Sufficiency 是联合检索状态

<!-- semantic-body-binding:SF-2026-ARXIV-2606-02245:start -->
传统 top-k 把候选文档视为已授权且免费，在公共 corpus、单次查询和成本可忽略时合理；受许可、付费 API 或组织预算约束后，相关性最高的 evidence 可能无法访问，也可能消耗后续查询需要的共享预算。检索控制器应先由 authorization owner 判定 access right，再把 source authority、cost tier、per-query budget、shared budget、已购 evidence、当前 sufficiency 与停止条件写成同一 versioned state。Selector 只能提出购买/读取 proposal，budget owner 原子扣减并生成 purchase receipt，answer gate 根据实际获得的证据决定提交、继续检索或 abstain。

联合控制可在预算内优先取得高价值证据，却会引入价格模型、共享预算竞争、错误 sufficiency 判断与廉价低质来源偏置；cost tier 绝不能替代来源权威。价格、授权或预算 ledger 不可靠时，应回退仅使用已授权免费 corpus，或升级人工；预算不足且关键 claim 无证据时拒答，而不是用参数记忆补齐。论文使用模拟价格和简化检索环境，支持 cost-aware selection 的机制方向，不证明真实许可、paywall、组织结算或生产尾延迟。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-02245:end -->

### 真实 Evidence 也必须匹配当前 Query 约束

来源可信、陈述为真且主题相关，仍不等于它对当前问题拥有 support authority。同一实体的上一年度、相邻子集、
兄弟对象或不同 answer slot 都可能形成高度可检索的真实 evidence；若 reader 把其中答案直接迁移到当前问题，
factuality 与 relevance gate 都会通过，但结论依然错误。因而 query controller 应冻结原问题 identity 与关键约束，
包括 entity、time、scope、unit、negation 和 requested answer slot；evidence admission 再记录每个 span 实际支持的
约束范围、当前 query/rewrite revision 与 accept/reject 理由。只支持相邻问题的材料可以作为 re-query、decompose
或定位原始来源的 clue，不能直接进入最终 claim commit。

这种约束对齐增加结构抽取、比较与审计成本，抽取器本身也可能漏掉隐含条件；低风险简单查询可继续依赖普通
rerank，关键约束无法可靠抽取时则回退精确过滤、再次检索或人工核验。构造的 nearby-evidence 实验在 12 个
model–benchmark pair 中证明这类失败可发生，并显示 later、answer-shaped evidence 更易被采用；但实验隔离了
真实 indexing、ranking、freshness 与 source reputation，constraint-checking prompt 也只部分缓解。因此它支持
增加 query–evidence alignment gate，不支持真实网络攻击发生率或“一个 prompt 已完成防御”的结论。

<!-- source-family:SF-2026-ARXIV-2608-30303 -->

### Web Evidence 可以一路追踪到 Pixel Grounding

普通图像检索返回相似页面，却没有证明页面中的哪个实体对应目标像素。search-to-pixel workflow 先取得 web evidence，
解析实体身份，再把证据绑定到 box/mask grounding；搜索器拥有候选来源，identity resolver 提交实体映射，grounder 只提交
空间位置，最终答案保留整条 provenance。它增加网络 freshness、工具失败与身份同名风险；任一阶段证据不足时应返回未知、
请求人工或只给页面级结果。现有证据限 120 images、645 QA pairs 与作者工具链，不证明开放网络上普遍可靠。

<!-- source-family:SF-2026-ARXIV-2605-12497 -->

### 多模态 Evidence 还要检查模态间的覆盖与支配关系

文本与图像都来自可信来源时，把两者一起交给 reader 看似只会增加信息；但文本如果直接给出一个可复制的答案，
可能压过图像中的相反证据，使“增加 context”反而重新引入错误。因而多模态 admission 不能只逐模态检查真实性，
还应记录每条 claim 由哪种模态支持、不同模态是否冲突，以及答案变化究竟来自新证据还是某一模态的注意力支配。
可先用受限的 reference pass 比较 image-only、text-only 与 joint-input 输出，再把 attention mass 或 sharpness 作为
诊断信号；这些信号只帮助定位支配关系，不能单独充当真实性分数。

这条检查增加额外推理、模态对齐和阈值校准，且受测模型的 attention 不一定可访问或可比较。低风险、单模态材料
可继续走普通 sufficiency gate；当模态冲突无法消解时，应回退单模态反事实、重新检索或人工判断，而不是让更流畅的
文本自动取得 authority。现有证据只覆盖六个模型、三个数据集和单张 RTX A5000，支持“跨模态支配会破坏 grounded
answer”这一 failure mode，不证明 attention 指标是通用 verifier。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05594 -->

把不同模态并入 GraphRAG，可保存跨页关系，但一个 fact 若同时由图、表和正文支持，按 edge 是否存在筛选还可能把被屏蔽模态的 chunks 带回 reader。更可诊断的 admission 为 edge 保存 supporting chunks 及各自 modality，按当前允许 subset 保留仍有支持的 fact，只传递该 subset 内的 evidence；来源身份不因高 contribution 改写。再在同一题目、图和 ranking 配置下比较单模态与 joint subset，把“新增信息贡献”同“组合后的冗余/干扰”分开，而不是默认模态越多越好。

这增加 provenance、重复检索/生成和切片样本成本，edge 提取错误与输入预算仍会混杂结果。[有限两模态 DocVQA 分析](https://arxiv.org/html/2609.35304v1)的交互量还使用各组最频繁 gold answer 作零模态基线，不是实际空context运行；负交互不单独证明 interference，分组 CI 和模型/intent 变化也不支持固定模态淘汰规则。部署 router 仍须独立验证实际质量/成本与 source sufficiency；支持身份不全、切片太小或结构不可信时，回退原页/flat retrieval、单模态反事实和独立 answer gate，不让诊断分数取得事实 authority。

<!-- source-family:SF-2026-ARXIV-2609-35304 -->

### Escalation 与 Abstention Threshold 必须联合校准

级联 RAG 常分别设置“是否再检索/升级”和“是否拒答”的阈值，单独调参在 distribution 稳定时简单；两者共享同一 evidence uncertainty 时，独立阈值会形成空洞或重叠区域。更完整的 calibration object 把 threshold pair、target risk、calibration distribution 与 fallback cost 一起冻结：retrieval controller 决定升级，answer gate 决定提交或 abstain，二者都不能修改 source truth。

联合校准可以明确风险预算，却新增样本需求、distribution-shift sensitivity 与更多 abstention；认证只对声明分布和 risk level 成立。低风险、单阶段或缺少 calibration set 时，保守规则与人工升级仍更稳。`arXiv:2605.20084v1` 的 §3–§5 只支持其 BalanceRAG threshold certification 与受测 cascades，文中 Limitations 不允许把阈值外推到新 corpus、retriever 或模型。

<!-- source-family:SF-2026-ARXIV-2605-20084 -->

联合 threshold 之外，还可先问当前 retrieval 是否提供完整证据，而不是直接预测答案正确。一个受限 multi-hop 分支将 top-5 是否包含完整 gold support 作为训练 target，用九项 ANN score-distribution features 和 query length 建立较便宜的 confidence gate；再按 retrieval regime 检查 feature 的有效性。它只决定继续检索、交给 answerer 或 abstain 的 proposal，不让 support label 取得 answer correctness 或 source truth 的权限，换 corpus、retriever 与 hop 结构须重验。

Logistic 输出并不天然 calibrated，有限 MuSiQue 上的 MLP、tie 与 ECE 对照也不是所有 query 的风险证书。不能采用‘经验 CWAR 必随 threshold 单调’、空选择集合默认风险零，或将 Bayes 最佳规则的结论直接授予训练得到的 scorer；这些断言不由局部 feature 效果补齐。标注完整 support、校准 gate 与维护 regime 增加成本，需并报 coverage、support completeness、answer quality 与实际 retrieval/生成预算。目标或校准不可信、域移或 evidence 不全时，回退扩大检索、独立 verifier、已有联合校准/abstention，而不由廉价分数签发安全回答。 [必要机制与反证](https://arxiv.org/html/2609.22056v1)。<!-- source-family:SF-2026-ARXIV-2609-22056 -->

## Agentic Retrieval：Relevance 也可以是执行先验

传统 retrieval 常把 relevance 用作一次性 gate：选出 top-k，再把内容交给模型。但复杂问题
需要反复定位、组合和验证 evidence，Agent 可能在 corpus 中执行 grep、局部 read 与追踪
中间实体。此时 relevance 还有第二种用途：

```text
relevance as content filter
→ decide what enters the candidate set

relevance as execution prior
→ decide where interaction starts
→ decide which documents are traversed first
→ decide which local matches survive observation truncation
```

这一区分避免两个极端：纯 top-k retrieval 可能过早截断 decisive span；完全
relevance-agnostic 的直接搜索又会把有限 tool calls 和 observation budget 浪费在低价值区域。
更稳健的组合是让 retrieval 提供 coarse-to-fine priority，同时保留 Agent 对原始 evidence
的局部交互能力。Relevance 是“更可能有用”的 prior，不是充分性、真实性或授权证明。

RARG 预印本在固定 corpus 的 BrowseComp-Plus 与 BRIGHT 设置中报告了更好的
accuracy/interaction-cost frontier，并通过 document order、entry-point paragraphs 与
match-level reranking 实现这种 prior。该结果仍是单篇作者实验，依赖具体 embedding、
corpus、模型、tool budget 与 truncation policy；因此本章只吸收机制，不把其 benchmark
外推为所有 RAG 或 Agentic Search 的默认实现。

显式 Agentic RAG 逐 token 生成 thought/subquery，透明但延迟高；LatentRAG 把 reasoning 与 subquery 变成一次前向产生的 latent tokens，并与 dense retriever 联合对齐。系统因此必须把 latent query、retriever revision、parallel natural-language decoder 与 evidence admission 作为同一 run identity；并行解码只能提供可观察视图，不能证明真实 latent control。对齐或审计失败时回退显式 subquery、单步 RAG 或人工可读 trace。

作者在七个 benchmark 报告约 90% latency reduction 与 comparable performance，但摘要未绑定硬件、backend、batch/concurrency/SLO；不证明生产尾延迟、可解释性或开放 web retrieval。 INFER-SCHEDULING 可消费 latent path 的成本模型；AGENT-RAG 拥有 query/evidence state。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06285 -->

### Retrieval Router 选择的是检索系统，而不只是文档

固定 BM25、dense 或 multimodal pipeline 在语料稳定、延迟预算明确时最容易校准；异质 document workload 中，query 可能需要不同 modality 与 reranking depth。Router 可以只看 query，在预认证 action 集合中选择检索架构：

```text
query + tenant / corpus identity
→ eligible retrieval actions
→ effectiveness-latency policy
→ selected index / reranker
→ evidence sufficiency and answer gate
```

Soft reward target 比 noisy hard argmax 更能保留 action 间差异，但 query-only router 看不到目标文档 layout，
也可能记住 domain lexical cue。多套 index 会增加显存、更新、删除与 authorization 一致性成本；oracle gap、
P95 latency、index footprint 与 downstream answer quality 必须一起记录。语料单一、成本敏感或路由样本不足时，
固定 hybrid retrieval 仍更可维护。

Router 使用 retrieval-state feature 时，必须与 query-only control 做 matched attribution。一个 feature 能预测后续 step 是否有益，不等于它改变了最终 RUN/SKIP 决策；开发集上的小增益若在 held-out 消失，就不能升级为长期机制。只有 final action、latency 与 failure slice 同时产生可复现增量时，retrieval state 才获得 routing authority，否则保留更简单的 query-only 或固定 pipeline。

<!-- source-family:SF-2026-ARXIV-2609-12437 -->
### Query、Compression 与 Stopping 是联合 Policy

当 retrieval 变成多步过程，Agent 的决策变量不再只有“下一条 query 是什么”：

```text
query / search breadth
+ evidence retain / discard
+ Context compression / dereference
+ verify / cross-check
+ stop / answer / abstain
```

这些动作共同决定最终 outcome、Context pressure 和 tool cost。只训练 query policy、再用固定 compressor 与
固定最大步数，状态最清楚且便于审计，在短任务和高风险 evidence retention 中仍很合理。Joint policy 可以
根据当前 progress 移动预算：证据重复时压缩，关键 nugget 尚缺时继续 search，sufficiency 已成立时停止；但
它也把 terminal reward 粗粒度地传播到每次 query、summary 和 stop decision，产生新的 credit ambiguity。

“更短 trajectory”尤其不是单向收益。它可能表示移除了得到答案后的冗余搜索，也可能表示 numerical
reasoning 困难、retriever miss 或 compressor 丢证后 premature give-up。因此 evaluation 至少应把：

```text
retrieval coverage / decisive evidence found
compression fidelity / provenance retained
verification performed / contradiction handled
stop correctness / premature-stop rate
task outcome + token/tool/latency cost
```

分开报告，而不是以 step count 或单一 terminal score定义 efficiency。对 compression segment 复用 episode
reward 能降低标注成本，却不能证明某次 summary 对成功有因果贡献；counterfactual replay、不同 compressor/
retriever cross-swap、oracle sufficiency 或人工 evidence audit 只能分别提供受限诊断。

若用 synthetic task generation、off-policy rollout reuse 和线上同一 harness 训练该 policy，train/eval/serve
还必须绑定 corpus/index、chunking/embedding、tool schema、compression transition、step/token budget、reward/
judge 与 policy revisions。共享 harness 可以减少 distribution shift，也可能让 policy 过拟合某个 tool、summary
格式和 evaluator。Static top-k、外部 deterministic compressor、single-task expert 与 snapshot RAG 因而继续
成立；联合 policy 只在多任务、长 horizon 且其额外 state/bias 可观测时值得采用。

在资源受限设备上，compression 还必须把自身开销计入决策，而不是只比较压缩后的 generation tokens。固定压缩率
最容易复现，但同一比例在短证据、长噪声文档和不同模型上会产生不同的 fidelity 与 energy 结果。一个可部署的
controller 至少需要显式状态：

```text
query + retrieved evidence + source provenance
+ model / precision / device / power mode
→ estimate compression cost and saved generation work
→ choose retain / compress / bypass under a quality floor
→ record realized latency, energy, fidelity and answer outcome
```

压缩器只能拥有 evidence transformation，不能拥有事实 authority；被删 span 的 provenance、可回取指针与
compression revision 仍要保留。单设备、FP16、小模型与 single-query 实验能够说明“压缩本身可能吃掉收益”，却不
足以训练通用 online controller，也不能外推量化模型、并发负载或不同 RAG corpus。输入很短、evidence 不可丢、
压缩 overhead 大于预期 decode 节省时 bypass 仍是正确动作；因此 adaptive compression 的目标是 constrained
net benefit，而不是把压缩率单向推高。

固定总 memory-token 预算还需要决定“给哪篇 passage”，而不只是是否压缩。[AdaMem](https://arxiv.org/html/2609.22100v1)在同一次 query-conditioned passage forward 中生成固定候选 memory bank 和 relevance score，pool 标准化后以 B·softmax(score/τ) 分配连续份额，再用 largest remainder 保持整数总量 B；份额为零的 passage 省略，其余取前 mᵢ 个 memory state 投影给 decoder。它把 uniform 分配改为 query-dependent 分配，却不是直接优化真实 answer utility：score detach 切断离散 allocator 的 answer-loss 梯度，训练另有 teacher ranking MSE 与 generation loss；连续最优仅对假定 log utility 成立，整数 rounding 也不继承真实答案最优性。

候选 bank 在分配前已编码，因此较少送入 decoder 不意味着 compressor 成本随 mᵢ 成比例下降。工程验收还必须检查 mᵢ 不超过实际 bank 容量且总预算 B 可行；per-passage cap 不在该连续证明中，不能说作者已证明受 cap 约束的最优分配。Llama3.2-1B compressor/Mistral-7B decoder LoRA rank 64、25 passages、query/passage 各截到 128 tokens 的 matched OSCAR 对照隔离了 allocation，但单 A100 80GB、BF16/FA2、同 16× 压缩下 AdaMem 为 192.4 ms/56.4 GB，对照为 156.1 ms/39.6 GB，明确付出 latency/peak-memory 代价。Substring-match、模型 judge 和 bootstrap SD 不等于事实真值或多次训练不确定性；不同 compression ratio 的结果也不能拼成通用“同质量四倍”保证。Uniform budget、raw retrieval/bypass 仍是有效回退，原始 source pointer 应可回取，这是工程要求而非 compressed state 自带证据权限。<!-- source-family:SF-2026-ARXIV-2609-22100 -->

### Iterative Retrieval 的 Stop Policy 要看 Marginal Utility

多跳检索不能只看当前 partial answer 的表面质量；每轮应同时估计新增证据的 marginal utility，并由校准后的 stop policy 决定继续、停止或转入 verifier。utility 比 quality 更难预测，错误停止会漏证据，过度检索则增加噪声和成本。<!-- source-family:SF-2026-ARXIV-2609-16453 -->

进一步要区分“没有检索到 passage”和“passage 已在上下文但事实不可抽取”：只有前者适合 targeted re-retrieval，后者应转 extraction/verifier、扩大可见上下文或人工处理。<!-- source-family:SF-2026-ARXIV-2609-17043 -->

多跳 QA 与 LLM fact judge 不提供通用阈值；校准失效时回退最大轮数、无进展阈值和显式 evidence coverage，而不是让生成器自行宣告充分。

### 共享文档表示会把 Retriever 与 Reader 版本绑在一起

独立 retriever 与 compressor 可以分别升级、索引和回退；重复编码与双份文档向量成为主要成本时，也可以联合训练一条共享路径：decoder 的文档 hidden states 先投影为 multi-vector retrieval representation，再由第二 projection 直接变换为 reader 消费的 compressed context，文档只持久化第一份向量。retrieval 与 generation 的损失共同更新表示，loss scaling 要处理两任务的梯度竞争。这样减少重复存储和路径，却使 index embedding、projection 与 reader revision 共同决定兼容性；这是系统应补充的版本责任，不是论文已交付的生产协议。

`arXiv:2604.14403v1` 的 ECG 只在 SmolLM2-135M/Gemma3-1B、Wikipedia NQ/TriviaQA 等受限设置验证；去掉 scaling 后 NQ top1 EM .343→.173，更多文档也可能退步，不支持普遍多任务增益。context budget 只计文档向量，disk 只计 embeddings，不含 query、完整 index 或原文；“on-device”目标不等实际手机能耗、latency/SLO 已测。联合训练、重新编码/索引、reader 耦合和域外 fidelity 是代价。原文仍须可回取以支持出处、删除和重建；latent 相似度不拥有事实 authority。decoder 升级、分布漂移或质量门失败时，回退独立索引/压缩器或直接原文，而不是只因少存一份就批准替换。

<!-- source-family:SF-2026-ARXIV-2604-14403 -->

### 跨轮压缩应保存可续写的结论状态，而不是反复搬运历史

最直接的多轮 RAG 会把此前检索结果与推理文本重新送入下一轮；它在轮数少、证据量小时透明且容易核验，
但历史会随轮次重复进入 Context，使输入成本和注意力干扰持续增长。更紧凑的分支把每轮已经核验的结论追加到
一条 conclusion chain：原始证据仍由 provenance pointer 保留，下一轮只消费可续写的结论状态，并在同一次
生成中区分临时 reasoning 与允许提交的 conclusion。

这改变的是跨轮 Context state 的所有权，而不是事实 authority。Compressor 只能提出保留、合并或删除；
RAG controller 必须记录 source revision、压缩版本、被删证据的回取指针和本轮 commit，冲突或新问题需要旧细节时
回到原文重新核验。它以更小的跨轮输入换取信息损失、错误结论持久化和额外生成开销；短对话、证据不可压缩或
压缩成本高于节省时，继续重放原始 history 更可靠。现有实验只支持作者的模型、任务和轮次，不证明输入从近二次
增长降为线性后，事实完整性也必然保持。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-28361 -->

集合型 research task 还暴露了普通 sufficiency gate 的盲区：找到一个正确答案，不等于找全目标集合。若问题要求列举所有满足条件的 entity，控制状态至少要区分：

```text
candidate discovered
→ identity resolved and deduplicated
→ claim verified against source
→ exclusion boundary checked
→ marginal search yield estimated
→ stop / abstain / report incompleteness
```

这种 completeness 是相对于 source universe、time window 与 inclusion criteria 的合同，不是可证明的开放世界“全部”。继续搜索能提高 recall，却增加 API cost、重复证据和错误合并；过早停止则把已知正确项误当成完整答案。固定 top-k 在问题只需少量支持证据时仍合理，hierarchical/decomposed search 只在集合覆盖与 identity resolution 是任务核心时值得承担额外状态。

Graph-grounded search 还可以把训练与运行时检索连成一条 evidence lifecycle。离线阶段从 source graph
构造需要多跳 traversal 的问题并记录 oracle evidence；运行时只给 Agent 原始、含噪 observation，让它
自行搜索、访问和停机。Teacher 可使用摘要化 history 降低生成噪声，但 student 不应继承这份 privileged
state，否则 demonstration 与部署 observation 不同构。

在线 graph traversal 也不只等于“向量检索后扩邻居”。多 anchor 从不同 entity/frontier 出发，在交汇处
形成 query-specific evidence subgraph，可以捕捉分散关系；代价是 graph construction/provenance、anchor
calibration、动态更新/删除、授权过滤与 tail latency。Source graph 稳定且关系是主要信号时值得使用；
关系弱、索引频繁变化或授权过滤会破坏连通性时，chunk retrieval 与原文 dereference 更简单。

Graph 的来源审计还不能只验证最终引用句子。若 ingestion 允许把 corpus 中同类型实体互换，局部文本仍可能流畅，构成的边和多跳桥接却已指向错误主体；后续 traversal 即使忠实于图，也会把错误拓扑当作证据。因而 graph owner 应把实体身份、类型、边的原文 span 与构图 revision 一起纳入 admission，并在图上复核关键路径能否回指原始关系；静态文本过滤和 citation 格式正确都不足以证明拓扑未被污染。这增加图更新与核对成本；无法可靠维护 provenance 时，应回退到原文检索和逐跳验证。受控 GraphRAG 攻击只证明所测 corpus、构图器和多跳问答的这一失效路径，不给开放部署的统一攻击率。<!-- source-family:SF-2026-ARXIV-2604-02954 -->

Corpus 也可以被编译成可导航的 procedural index，而不是只生成 embedding/chunk index。Compiler 从文档提取
主题、依赖、入口与可执行 navigation hints，运行时 Agent 先选择一条 coarse skill，再沿其引用回到原文：

```text
authoritative corpus
→ versioned corpus compiler
→ navigable skill / topic graph
→ agent traversal under a budget
→ source dereference and claim evidence
```

这能把复杂 corpus 的 query decomposition 从每次在线推理摊销到离线阶段，却新增 compiler hallucination、
incremental rebuild、ACL/delete propagation 和 graph drift。Skill node 是 retrieval plan，不是事实 authority；
最终 claim 必须回到原文与 event-time revision。Corpus2Skill 的作者实验支持其静态 corpus 与 agent harness
下的 navigation mechanism，但其高 input-token/cost、缺少增量更新和 adversarial document 评估，不能证明它
取代普通 top-k RAG。小 corpus、更新频繁或权限图复杂时，chunk retrieval + deterministic filters 更简单。

对结构约束明确的代码或关系库，另一个分支把 source 解析成带位置的 facts，让模型只提出逻辑查询，再由确定性引擎执行。parser 通过只证明语法可执行，结果仍可能因猜错 identifier、join 或 predicate 顺序而为空；也可能因为原条件确实没有匹配。可以对中间空关系做有界字符串放宽或单条件移除，观察哪条限制影响结果，把变体 identity、row count 和有限 tuple 样例作为修订反馈。变体返回的记录不是原查询答案，不能为“找到东西”静默削弱用户条件；最终查询仍须保留明确意图并回指 source。

这把深层结构遍历从模型 token 交给 facts 和 query engine，却增加解析覆盖、facts 更新、查询合成与诊断执行成本。所有探针仍为空或执行失败，只说明在这组有限探针下未恢复结果，不证明开放代码库不存在答案；放宽后非空也不证明原限制错误。受限 Python 定位实验支持这条 diagnostic 分支，未证明完整程序语义、跨语言覆盖或普遍低延迟，额外反馈在部分配置反而增加时间。关系不稳定、事实抽取不完整或无法确认查询意图时，应保留原条件、报告未决并回到原文检索/人工核对；有明确标识符的简单任务继续使用词法或 chunk 检索。[受限空结果诊断证据](https://arxiv.org/html/2604.16021v1)<!-- source-family:SF-2026-ARXIV-2604-16021 -->

## RAG 不消除 Hallucination

<!-- source-family:SF-2026-ARXIV-2605-26778 -->

回答与检索文档内容一致，不等于回答由该文档支撑：模型可能只是在 parametric memory 中本就知道答案，检索内容甚至没有进入有效推理路径。若 evaluation 只看最终正确率或 citation overlap，就无法区分“证据导致了答案”与“答案碰巧和证据一致”。更严格的 groundedness contract 需要成对干预：保留问题、替换或遮蔽关键证据，观察结论与引用是否按预期改变，并把这种 counterfactual sensitivity 与普通 correctness 分开报告。

干预评估提高了因果诊断力，却增加样本构造、对照污染和 evaluator 成本；答案对证据不敏感也可能因为模型拥有正确先验，而非一定错误。低风险搜索可继续用 relevance/citation 指标快速迭代，高风险发布则需要 provenance、support span 与干预证据共同证明检索链真正拥有结论的 support authority。

参数与 context 的归因也可用 model-specific hidden-state probe 做诊断，但监督标签的生成本身要纳入证据链。一个受限方案先用三种无 context 提问测试实体：任一次答对记 known，再移除上下文中的实体；三次未答记 unknown，并在上下文保留实体，随后用生成首 token 或实体末 token 的状态训练线性 probe。这定义的是操作性知识测试人口，未答不证参数从未存过、出现实体也不证模型实际只用 context；实体末 token 更不能当作生成前 verdict。[标题隔离 split 与 answer-string decoy 控制](https://arxiv.org/html/2602.22787v1)显示较复杂 MLP 更容易利用表面线索，且正确来源预测仍可能伴随错答；同 probe 判断 dual source 的输出不能再循环当作外部真值。模型/语言/能力版本改变会改 known/unknown 人口，状态存储、构题与重训都付费。Probe 可提出“可能忽略检索”的检查请求，不能获得 causal provenance 或 grounded truth authority；自然长答、版本漂移或标签不足时，仍以配对 evidence 干预、support spans 与独立 claim 核验为准。<!-- source-family:SF-2026-ARXIV-2602-22787 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06919:start -->
检索排序和来源权威都正确时，最简单的回答器仍可能把文本中的“可能、据称、90%”一律吸收为事实；反过来，低 certainty context 也可能压掉模型原本稳定的先验。RAG answer gate 因而应把三类状态分开：来源表达的 certainty 只是带 provenance 的 claim metadata，模型 prior 只是候选解释，最终 answer confidence 必须由 authority、freshness、corroboration、contradiction 与任务风险共同校准。

一个受限的交互分支可以先要求模型显式给出 prior，再简化复杂 context、重标 certainty 并合成答案；它不能把模型自报概率升级为真值。这条路径以额外 forward、prompt coupling 和概率访问换更细的证据服从，也会新增来源自报失真、长上下文稀释、部分正确证据与校准漂移。出现这些压力时，应回退逐 claim 引用、冲突展示、外部 verifier 或 abstain。现有 exact-v1 只支持作者披露任务中的证据服从现象，不证明 verbalized confidence 等于真实正确率。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-06919:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2604-16686:start -->
这种 prior/context 取舍还可以落在逐 token 解码，而不只是回答级的置信提示。连续 contrastive logit tilt 即使很小，也可能改变 argmax；一个替代分支是在同一当前生成 prefix 下同时计算有 context 与无 context 的分布，用低 JS divergence 和较大的无 context top-1 margin 联合触发显式回退，直接复制无 context logits。未触发时，再按 context margin 选择普通条件解码或 contrastive fallback。回退保证的只是该共同 prefix 上、greedy 规则下的下一 token 一致；只有每一步都回退，整串才与独立无 context 基线一致。margin 和两流的一致并不证明答案正确，也不证明 context 没有新证据。

显式回退以更保守的证据采用换取减少无益扰动，也会拒绝真正有帮助的 context。其预算包括两条 forward、分布比较和阈值校准，而不是免费纠错。受限研究在 Llama-3.1-8B 的受控短 QA 切片上调三个阈值，再迁移至 70B 与 Ministral；该调参切片不能同时充当独立泛化证明，top-K JS 近似和短 greedy 输出也不覆盖任意长回答。既有单流生成、连续 tilt 与回答级 verifier 仍分别适合低成本、强冲突或需要外部 support 判断的场景；发布时应分别测 baseline-correct 保持和有益 context 利用，不能由总准确率掩盖二者取舍。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-16686:end -->

### Web Retrieval 的 Corpus 也可能主动塑造 Agent Trajectory

<!-- semantic-body-binding:SF-ECOGEO-TRAJECTORY-AWARE-EVIDENCE-ECOSYSTEMS-FOR-WEB-ENABLED-LLM-SEARCH-A:start -->
传统 RAG 把 corpus 当作被动事实集合；web-enabled Agent 会连续搜索、引用、回访并让多个页面共同塑造后续 query，
于是发布者优化的不再是单页排名，而是整条 evidence trajectory。检索系统必须记录页面 provenance、跨站关联、
query evolution 与最终 claim uptake，不能把“多处出现”自动解释为独立证据。协调内容生态可以提高可发现性，也会
制造相关来源、反馈回路与操纵面；高风险结论应回到独立 primary source 和 claim-level entailment。固定私有 corpus
仍适合低变化、强治理场景。受控虚构产品实验只证明 trajectory-level influence 可以被测量，不证明现实 web 排名
或所有搜索 Agent 会同样受影响。
<!-- semantic-body-binding:SF-ECOGEO-TRAJECTORY-AWARE-EVIDENCE-ECOSYSTEMS-FOR-WEB-ENABLED-LLM-SEARCH-A:end -->

### 长文生成需要把检索、叙事状态与核验分开提交

一次取回大量文档再自由生成全文，在短答案和低风险任务中路径最短；长文同时要求全局结构、跨段一致性和逐 claim grounding 时，单次 Context 很难既容纳所有证据又保持可审计。一个更稳健的分支是先冻结 outline，再让每个 section 只读取有界证据和 coherence memory，最后由独立 checker 产生返工而不是直接宣告可信：

```text
evidence inventory → versioned outline
→ section-scoped retrieval + bounded coherence state
→ atomic claims and citations
→ independent check → accept | revise | abstain
```

这个分层用更多检索、NLI/attestation 误拒和 revision latency 换可定位的错误边界。Checker 只能证明其契约内的一致性，公开测试文本还可能已进入预训练语料；对新颖私有文档、法规判断或跨段隐含冲突，人工复核与 source-side authorization 仍不能省略。

这里的原子化对象是待核验的 claim，不意味着支撑它的 citation 必须只有一句。定义、否定、条件和因果关系可能跨句存在；强制拆开引用单位，会失去必要上下文。可以保留小而可独立判断的 claim，同时允许它指向连续的多句 support span，并检查这些句子共同是否充分支持命题。反过来，扩大引用片段也增加无关文本和人工定位成本，不能以“段落里出现了相关句子”替代整个 claim 的蕴含检验。

因此比较引用粒度时，应分开报告 claim 正确性、支持关系、引用总量与定位成本，先固定输入证据，再测试生成与引用策略；检索 chunk 的最优大小不由这个比较直接决定。[受限的粒度实验](https://arxiv.org/pdf/2604.01432v1)观察到单句约束并不总是改善 attribution，但其“含任意相关信息即算有效 chunk”的指标会偏向粗粒度，联合生成与引用也不能单独归因于推理或定位。它不提供统一最佳句数，更不证明引用导致了答案。短而自足的证据仍可精确引用；需要跨句条件时保留上下文，高风险输出则回到逐 claim、逐 support span 核验。
<!-- source-family:SF-2026-ARXIV-2604-01432 -->

模型仍可能：

- 未使用 evidence；
- 混合多个来源；
- 生成来源未支持的细节；
- 把旧文档当最新政策；
- 遵循文档中的恶意指令。

高风险场景需要 evidence-aware response policy：缺 evidence 时 abstain，关键 claims 可验证，冲突升级给人或确定性规则。Citation 只是引用字符串，必须检查 claim-to-source entailment。

引用还可以与 claim 同时生成带类型的关系：绑定 document revision、sentence/support span，并区分直接 quotation、compression 与跨片段 inference。这让定位与检查路径更明确，却不会让 generator 自报的关系取得证明权；与 reference 的字符串/语义匹配只是在该标注协议里的评分，不能代替独立 entailment，更不能证明模型内部确实使用了这份来源。[联合生成 typed provenance 的受限实验](https://arxiv.org/html/2601.04932v1)中，匹配 F1 和内容质量会沿不同方向变化，因而二者须分账。由此推导的输出合同应保留 relation type、冻结的 source/span identity 与独立支持结论，特别对 inference 检查跨句前提；它增加标注、检索、tag tokens 和复核成本，且错误 reference 会制造漏报。来源不可恢复或关系未验证时保留 Unknown、重新检索或交人工，而不是把正确格式的 provenance tag 当成更强的事实 authority。<!-- source-family:SF-2026-ARXIV-2601-04932 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-35794:start -->
拒答的原因也需要区分：retrieved set 没有充分证据，与它含有正确答案却同时混入冲突或干扰，并不是同一个状态。让 generator 统一判断在低噪声时最简单；干扰频繁且生成较贵时，可以先以轻量 classifier 检查整组证据是否 distracted，拦下后不调用生成器；通过后，再让 generator 判断缺证据或生成 grounded answer。缺证据可触发 re-retrieval，干扰可触发过滤和重新核对，避免反复在同一坏集合上推理。Classifier 只提供可校准 gate，不拥有事实真值；过滤后仍须验证剩余 evidence 对 claim 的支持。

这条分层以训练标签、domain adaptation、误拒和较低 coverage 换掉部分错误回答与无效生成。[Sieve/Sage v1 §3–6、Limitations及AppC](https://arxiv.org/html/2609.35794v1)主要使用 reference answer/NLI 构造的检索状态与模拟噪声，expert域仍需监督，raw推理耗时也不是生产并发吞吐。更少错误可以同时伴随更低 selective accuracy，不能用总system accuracy掩盖效用取舍。自然噪声、来源变化或classifier漂移尚未验收时，保留单模型判断、claim-level verifier及人工升级；不能把 answer 出现在某篇文档里当作整组证据可靠。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-35794:end -->

### Grounded Output 也可能泄露 Corpus Membership

让回答严格蕴含 retrieved evidence，是减少无依据生成的合理旧路径；在 corpus 含私有文档、攻击者可反复查询时，同一 entailment signal 也可能暴露某份文档是否存在于索引中。攻击者不需要读取 chunk，只需构造与目标文档相关的 probes，并比较模型输出对该内容的支持模式。于是 corpus owner 不仅要控制 retrieval ACL，还要拥有 membership threat model、query budget、rate/identity correlation 与输出 release policy；generator 不能因为答案“有证据”就取得泄露判定权。

收紧输出、加入不确定性、限制重复 probes 或对敏感 corpus 做更强隔离可以降低攻击面，却会牺牲回答效用、可解释性和合法用户的 recall；简单噪声还可能被多次查询平均掉。公开 corpus、低敏感度或查询主体可信时，普通 evidence-aware RAG 仍成立；无法校准泄露风险时应回退私有检索服务、人工审批或不对外暴露该 corpus。`arXiv:2605.24312v1` 的 §3 与 §4 支持作者 entailment-based black-box membership attack 及五次查询合同，§5 不证明所有 retriever、模型、文档或攻击预算都同样可辨识，也不证明单一防御足够。

<!-- source-family:SF-2026-ARXIV-2605-24312 -->

### Self-authored Evidence 必须隔离 Provenance Feedback

RAG 把模型生成内容写回可检索 corpus，在内部知识库和迭代 drafting 中可以降低人工成本；若后续 retrieval 不区分作者来源，系统会把自己的旧输出当作独立证据，形成 citation self-bias、答案同质化与错误自强化。Retrieval identity 应保留 author/model revision、生成链和外部来源，并对 self-authored items 限额、单独聚合或要求独立 evidence corroboration。隔离会牺牲缓存命中和迭代速度；明确标注的个人草稿库仍可复用，但不能计作新的独立来源。`arXiv:2608.22118v1` 的三类 simulation、三个模型家族和 1,019 个请求支持 self-bias 仍存在于控制 reference quality 后，不证明真实 Web 有固定 collapse 概率。

<!-- source-family:SF-2026-ARXIV-2608-22118 -->

## Freshness、Deletion 与 Consistency

### Embedding Upgrade 是兼容性迁移，不只是新空间更准确

替换 embedding model 后，新 query 向量若无法与旧 corpus index 比较，就会把质量升级变成全量回填和双写迁移。Version contract 应同时评价旧索引兼容、新任务增益、adapter/reprojection 误差、回填比例与 rollback；“新 benchmark 更高”不能单独授权切换。<!-- source-family:SF-2026-ARXIV-2609-16875 -->

兼容 adapter 可降低迁移成本，却可能限制新空间表达并积累双版本复杂度。高风险 retrieval slice 或跨域误差无法接受时，应双索引、逐批回填或保留旧模型；作者模型/数据不承诺零回填。

若更新只针对检索域，还可以让 query 侧的 domain prefixes 变化、passage 侧只使用冻结的 general prefix，从而复用同一套 passage embeddings；这把 adaptation 的可变状态限制在 query/router，而不是承诺任何新 embedding 都兼容旧索引。General prefix 或 backbone 一旦变化，passage 重编码与回归责任仍回来。[八模块 dense retrieval 对照](https://arxiv.org/html/2602.22547v1)使用128长度 prefix、coCondenser、BERRI 五负例和单A100，在六个 BEIR 切片中比较 top-2、带领域先验的路由与 uniform/all-module 控制；domain prior 与 learned weighting 的局部增量不证明任意未知域都能正确选模块。2.3M 是单模块口径，表列 `2.3M×8`，不能把约2%当作全方法总参数或总费用；引用的其他 baseline 也非全部同预算重跑。模块、prior mapping 与 general/passage index revision 须联合保存，训练和在线 routing 仍付费；先验不可靠、general space 需改变或质量退化时，保留固定 retriever、重编码/双索引及原迁移回退。<!-- source-family:SF-2026-ARXIV-2602-22547 -->

### Temporal Retrieval 要在 Admission 前验证事实有效期

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23497:start -->
只按语义相关度检索，在 corpus 近似静态时足够；事实随时间变化后，query fact date、source validity interval 与 corpus revision 必须共同决定 evidence admission。Retriever 可以返回候选，但过期或未来泄漏的证据不能因相似度高就进入回答。

时间过滤减少错期事实，却依赖完整 metadata，并可能把日期未知但真实的材料误删。exact-v1 只支持作者数据与 protocol；时间戳缺失、有效期冲突或高风险 claim 无法定位时，应回退权威历史档案、扩大检索后人工核对，或明确返回 Unknown。arXiv:2605.23497v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23497:end -->

有效期metadata进入Context后，还要验收reader是否实际按它改变证据权重。发布时间、事实生效区间和当前evaluationdate不是同一个字段；在同一份历史证据、同一问题和选项上，只翻转evaluationdate，再比较仅给日期与显式给失效边界，可以区分“知道日期”与“遵守有效期”。这是一条受控验收接口，不是让模型自称文档过期便取得事实权威；边界仍由可核来源提供，时间未知的材料继续按原admission规则降级。

检索评价也须看两个方向：有效新证据能否纠正旧模型，与失效旧证据会不会覆盖模型本来正确的答案。后一分母限定不检索已正确的同model/query集合，不能替代全请求效用；更强follow指令可能增加错误deference，准确日期reranking有益也不证明适用性已解决。有限choice、自由生成与内部干预的范围分开，judge误差和eligible切片保留。元数据不可信、reader行为未校准或高风险claim冲突时，回到权威后继、确定性validity检查或人工核对，不能把更多检索自动当更可靠。[受限反证](https://arxiv.org/html/2609.31342v1) <!-- source-family:SF-2026-ARXIV-2609-31342 -->

#### 时间过滤之前，先找出可能遗漏的权威后继

验证候选的事实有效期，只能处理已经召回的材料；同一实体的后继文档可能用完全不同的词汇撤销旧结论，根本不在 semantic top-k 中。可将流程拆成 semantic anchor discovery、entity-scoped authority/supersession 补检、active-frontier admission：语义检索负责找到主题，权威关系负责扩大必须核的候选集，reader 只能消费已核身份/有效期的证据。后继不是因为“更新”就自动有权替代前文，scope 与真实 supersession 关系必须可追溯。

补检会引入 authority graph 维护、额外 lookup、错误实体合并与虚假 supersession。`arXiv:2604.14488v1` 的 CAR 理论限静态 corpus、已知确定性单一 partial order、理想可恢复 scope 与 deterministic answer function；不能将有限领域结果升级为开放语料完整性或线上 SLO。其“正确答案必然要求完整 frontier”的必要方向也不普遍成立：两个 active 文档独立给出同一答案时，只取一个仍可答对。因此采用主动补检机制，不采用通用 iff 正确性保证。关系或 scope 缺失时标 Unknown，回到权威原档或人工核对；语料近似静态、无正式替代关系时，普通语义检索与既有时间门仍是清楚的旧路径。

<!-- source-family:SF-2026-ARXIV-2604-14488 -->

### RAG 安全必须覆盖完整状态生命周期

在事后取证之前，检索器也可以先削弱局部poison对表示的影响：将文档分片独立embed，再组合平均，区别于先拼接含poison的原文再embed。若对各组合分别取top-p，再按出现频率保留多个候选，它已不是每次只作一个决策的多数投票；原分片多数条件不能直接迁移，平均表示也不保证单个poisoned fragment必然无效。该分支控制候选exposure，不拥有来源真值或最终answer effect。<!-- source-family:SF-2026-ARXIV-2512-24268 -->

组合增加表示存储、检索与聚合成本；只在initial候选上逐span做mask probe、观察similarity下降再重排，则又支付多次embedding，并依赖候选支持集和局部敏感性。probe响应不是poison意图或事实错误的证明，语义贴题的假事实尤其不能由这条接口固有区分。ASR应按取回恶意文档、SR按保留有用文档分别回归，retrieval侧通过不授answer安全或实时SLO；utility下降、poison跨片段扩散或支持不足时，保留可信源admission、文档隔离、原检索与独立claim–source/answer gate，再用下述取证恢复实际影响链。

#### 从错误输出反查到字符 Span，需要两阶段取证

文档级 quarantine 在来源少、人工可读时足够；黑盒检索链路中，一篇长文只可能有少量 poisoned text，整篇删除会扩大可用性损失。取证流程应先冻结 misgeneration、query、retrieval/rerank 与 context 事件，再对候选文档做 counterfactual deletion，逐步缩小到实际改变输出的字符 span。Trace owner 保存事实，localizer 只提出 causal suspect，corpus owner 决定删除、重建索引和回放验证。

删除测试成本高，受非确定生成和关联片段影响，也不能从输出变化证明攻击者意图。证据不稳定时应回退文档级隔离与人工审查；修复后还要验证缓存和副本已失效。现有 exact-v1 只支持作者的黑盒 RAG 攻击与定位设置。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01782 -->

定位一个 poisoned span 还不足以识别组合攻击：单独看来正常的多个片段，可以在同一 Context 中共同推导攻击者希望模型作出的 claim。检索后的 admission 因而需要检查 joint-context claim support，并区分来源数量与证据独立性；两个数据库复制同一批材料，不会凭两个入口生成独立支持。逐 passage 检查仍能处理局部明显恶意内容，但 retrieval depth、database selection 与共同出现的片段集合要进入 threat model，不能把单片通过复制成整组通过。

这项检查增加联合阅读、支持关系与 provenance 维护成本。受限攻击实验中的 DPAR 是启发式 proxy，OLS 关联不构成通用 detector 或 defense 证书；top-k 增大也不总是更安全，不能只用一个成功率决定检索预算。应沿 exposure、selection、use 到 answer effect 分别记录攻击路径，并用真正独立的支持与 utility 回归复测。组合证据不可信或风险无法隔离时，回退单一可信来源、缩小 Context 或人工核对，而不是从局部正常文本推定联合安全。 [必要机制与反证](https://arxiv.org/html/2609.21573v1)。<!-- source-family:SF-2026-ARXIV-2609-21573 -->

只在最终答案前检测恶意文本，或只看一项 attack success rate，在 corpus 小、组件固定时容易实施；真实 RAG
却会依次改变 source、chunk、index、ranking、Context 和 answer state。攻击既可能写入文档，也可能修改 retriever
参数或索引入口；同一恶意 chunk 被取回，也不等于它通过 rerank、进入 Context 并改变了生成。因此安全验收应冻结
整条组件身份，并把 exposure、selection、use 与 answer effect 分开：

```text
source admission + sanitization
→ chunk / index publication
→ retrieval + rerank exposure
→ context admission + claim–source relation
→ generated claim + effect audit
→ repair / delete propagation
```

Corpus owner 拥有 source admission、拒绝记录和 utility regression；index owner 拥有 encoder/index revision、异常
hub quarantine 与 retriever repair；Context/answer gate 只消费带 provenance 的候选，并分别验证 claim 支持关系与最终
输出。任何一层的通过都不能替代其余层。这样可定位攻击发生在哪个状态转换，却增加 factorial evaluation、阈值漂移、
误拒和跨组件版本管理；低风险、封闭且只读的 corpus 仍可用较薄的 ingestion filter 加 answer check。

删除也必须沿同一依赖链完成。Tombstone 只改变逻辑可见性，不证明 embedding、HNSW node、cache、replica、backup
或派生摘要已不可恢复。需要擦除承诺时，应保存 source-to-derived lineage，采用物理 purge 或受治理的 epoch-key
rotation，并产生可核验的 deletion receipt；无法证明依赖闭包时，应隔离旧 generation、重建索引或转人工处理。
现有论文证据分别覆盖有限攻击、RAG 配置与向量库，不能证明该链已经穷尽所有投毒面，也不能把某个冻结阈值、
修复 anchor 或密钥方案外推为通用安全保证。

<!-- source-family:SF-2026-ARXIV-2605-27494 -->

Answer cache 只按 query key 复用，在知识稳定、答案无时间敏感性时最省成本；文档更新、删除或权限变化后，同一问题却可能命中已经失去 support 的旧答案。缓存 identity 因而不能只绑定问题，还要绑定 supporting evidence 的版本、可见性与 freshness policy。命中时先验证这些依赖仍可解析且继续支撑 claim，再允许提交；验证失败回退到 retrieval 与 regeneration。

这种 evidence-aware cache 用 dependency index、invalidation fan-out 与命中前验证换一致性；文档频繁变化时验证成本可能接近重算，错误的 support extraction 也会制造假新鲜。稳定、只读 corpus 仍可使用 TTL 或版本化 namespace；需要删除语义、审计或强时效时，则应让 evidence identity 而不是 query string 拥有复用权。

### 异步验证只能修订未来 Cache State，不能改写当前请求

每次语义 cache miss 都同步调用强 judge，在高风险请求上容易解释，却把昂贵验证放入每条请求的 critical path；只按 embedding threshold 直接命中又会把语义相似误当答案等价。一条中间路线保留静态阈值和动态 cache 的快路径：落入灰区的当前请求照常检索/生成，同时把候选问答送到 off-path judge；只有 judge 确认等价后，cache owner 才以新 query key、answer/evidence generation 与 verdict revision 原子写入，供未来请求复用。触发验证的当前请求不能被事后改写，judge 也不能绕过 corpus freshness 与权限检查。

异步修订移出在线 judge latency，却增加 delayed benefit、错误 overwrite、stale answer、重复验证与 cache pollution；高风险 claim、动态 corpus 或 judge 未校准时仍应同步验证或直接 miss。`arXiv:2602.13165v1` 的 exact-v1 只支持 Krites 披露的 grey-zone scheduling 与 auxiliary overwrite 机制；其 trace-driven simulation 用 benchmark equivalence class 代替真实在线 judge，且没有闭合生产 judge 准确率、cache capacity、overlap distribution 或删除传播，因此不能证明开放域语义 cache 的端到端可靠性。

<!-- source-family:SF-2026-ARXIV-2602-13165 -->

### 语义 Cache 的发布标准必须绑定工作点，而不是只看排序分数

语义 Cache 的离线 PR-AUC 可以比较 representation 或 reranker 的排序能力，却不能回答生产系统在某个 threshold
下会错误复用多少答案、实际命中多少请求。Cache owner 应冻结 query distribution、正例先验、score/threshold、
命中预算和错误代价，再以 threshold-aware precision、coverage/hit-rate 与可校准残差选择工作点；evaluation owner
只能提出 release evidence，不能自行改写在线阈值。

这使上线决策对应真实 false-hit 风险与节省量，却会随流量 mix、corpus revision 和模型变化而失效。Post-hoc
calibration 可以修复 score 到概率/决策阈值的映射，不能消除表示本身无法分离的结构性错误；低重复率、证据频繁
变化或错误复用代价高时，直接 miss、同步检索或强 judge 仍是合理路径。公开实验只覆盖其固定英文 pair、模型与
正例比例，不证明生产流量中存在相同最优 threshold。

### GraphRAG 的 Citation 必须绑定实际 Traversal

在扁平文档检索中，citation 通常绑定被送入 Context 的 chunk；图检索还会经由实体、关系和多跳邻域选择证据。若最终只列出几条可见文档，系统就无法区分“被访问但未采用”“作为中间桥接”“真正支持 claim”的节点。可审计路径应同时冻结 graph revision、遍历邻域、访问集合、支持边和最终 citation：

```text
query + graph revision
→ bounded traversal
→ visited and supporting subgraph
→ claim-level citation
→ independent entailment check
```

这提高了可追踪性和删除传播能力，却增加图快照、路径基数与隐私成本。可见或被访问不等于对结论有因果贡献，路径存在也不证明关系正确；低跳数、单文档即可回答的任务仍应回退到普通 retrieval + claim citation，避免为了图结构制造虚假的解释感。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21994:start -->
图上的 attribution 还存在第二种混淆：一个节点对 answer representation 的语义贡献可能很低，却是连接两段证据的必要 bridge。把 post-hoc score 直接当作裁剪依据，会把“对表示贡献小”误写成“对路径不重要”。一种受限分支是约束 graph encoder，使输出能够精确分解为各节点的加性贡献；routing controller 因而可以分别保存 semantic support 与 structural bridge role，而不是用一个分数覆盖两种责任。Graph revision、真实 traversal、claim citation 与最终 entailment 仍由外部证据 Gate 持有，模型归因不能取得事实 authority。

加性分解换来了精确的节点账目和更简单的 routing diagnosis，也限制了节点交互表达能力，并可能降低任务性能；保留低贡献 bridge 还会增加 traversal 和 Context 成本。现有证据只覆盖 STaRK-Prime 与少量详细案例，没有证明 answer faithfulness、graph correctness 或跨图泛化。若加性模型的准确率、图质量或 bridge 判定不足，应回退更强的常规 GNN/retriever，保留显式 traversal 与 claim citation，并把 attribution 标为诊断信号，而不是据此删除证据。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21994:end -->

<!-- source-family:SF-2026-ARXIV-2605-15109 -->

更新 corpus 时要同步处理 vector、lexical index、cache 与 derived summaries。删除请求必须传播到全部 derived state，不能只删 source。

Query trace 应记录 index version 和 retrieved document digests，使线上答案可复现。Mutable “latest index” 不足以事后审计。

### Concurrent Update 让 SSD Index 同时拥有 Search 与 Maintenance State

<!-- semantic-body-binding:SF-NAVIS-CONCURRENT-SEARCH-AND-UPDATE-WITH-LOW-POSITION-SEEKING-OVERHEAD-IN:start -->
内存足够、语料批量刷新时，离线重建 index 再原子切换最容易保持一致；当向量图落在 SSD、写入持续发生且查询
不能停机时，packed page locality 会与 selective vector read 冲突，entrance graph 也会在更新中变旧。可维护的
路径是让 storage layout 支持只读必要向量，复用更新遍历形成轻量 entrance state，并让 cache 显式感知 entrance
identity。Index owner 负责 graph revision、并发可见性和 crash recovery；retriever 只消费已发布 snapshot，不能
把搜索过程中看到的半更新边升级为 evidence。

这条分支用更低 position-seeking overhead 和在线 freshness 换取写放大、cache invalidation、并发控制和更复杂的
恢复语义。写流量低、corpus 可停机重建或内存索引可容纳时，immutable generation 加原子切换仍更简单可靠。
作者结果只覆盖其 SSD、图布局与 workload；未披露或未复现的 durability、tenant isolation 和尾延迟不能外推为
通用 RAG 性能结论。
<!-- semantic-body-binding:SF-NAVIS-CONCURRENT-SEARCH-AND-UPDATE-WITH-LOW-POSITION-SEEKING-OVERHEAD-IN:end -->

### 连续媒体先变成可修订事件状态，再进入检索

短视频可以直接作为一次 VLM 输入，路径短、状态少，在片段能够完整装入 Context 时仍是合理基线。长视频或持续感知流改变了约束：原始 frame 数量随时间增长，同一事件跨片段延续，后续观察还可能修正早期描述。此时直接把 frame caption 当作独立 chunk，会同时丢失时间关系、实体连续性与 revision provenance。

<!-- semantic-body-binding:SF-2025-AVA:start -->
更可维护的分支先按固定 observation window 产生带来源的描述，再合并为 event/entity/time graph；检索器从不同视图提出候选，最后仍回到原始时间段核验。Graph owner 负责 event identity、timestamp、merge history 与 stale-edge invalidation，retrieval policy 只拥有 search plan，不能把推断边当作 source fact。它以额外的视频解析、图更新和多步搜索成本换取跨时间证据；描述误差会沿图传播，实时更新还会制造旧边与新观察冲突。语义连续性弱、视频很短或低延迟优先时，直接 VLM/segment retrieval 仍更合适。AVA 的受限实验覆盖 8 段长视频和 120 个问题，只证明这条状态化检索路径在该合同下可执行，不证明通用实时视频理解或图搜索质量。
<!-- semantic-body-binding:SF-2025-AVA:end -->

### Corpus Ownership 可以留在 Peer，但信任问题不会消失

中央索引把 corpus、权限和 freshness 收敛到一个控制面，最容易审计，也会形成集中收集、单点容量与跨域治理压力。当文档必须由各 peer 保管时，检索可以演进为 topic-aware discovery：query 在候选 peer 间路由，每个 peer 只对本地授权 corpus 执行 retrieval，再汇总带 provenance 的结果。

<!-- semantic-body-binding:SF-2025-DISTRIBUTED-RAG:start -->
这个分支改变的是 corpus 与 index 的 state ownership，不是自动获得隐私。Peer discovery、query forwarding、result merge 和 timeout policy 都要版本化；恶意 peer、内容撤销、重复证据、访问模式和跨 peer 一致性仍需独立治理。仿真中的 topic-aware random walk 只说明在作者网络与 workload 下可用较少消息接近其中央 baseline，不覆盖对抗 peer、真实故障、query privacy 或生产尾延迟。稳定、可集中授权的 corpus 继续使用中央或分区索引；只有数据主权约束高于协调成本时，peer-owned retrieval 才值得进入主路径。
<!-- semantic-body-binding:SF-2025-DISTRIBUTED-RAG:end -->

### 分布式证据汇聚应按 Sufficiency 收敛，而不是等待所有节点

等待所有 device 或 peer 返回、再统一生成，在文档少且网络稳定时最容易解释；节点变多后，慢设备会把同步 barrier
变成主要 critical path，一次性上传全文又会扩大通信和数据主权风险。协调器可以为每个候选文档维护 waiting debt、
证据缺口与可核验的 sufficiency certificate：先消费已经到达且授权有效的局部证据，只向最可能缩小缺口的节点请求
最小补充，并在新证据到达时重新判断继续等待、回答、降级或 abstain。

Certificate 只证明其定义下“当前证据足够”，不拥有事实真值；document owner 仍保留原文，协调器只拥有请求与停止
决策，最终 claim gate 必须回到实际到达的 source span。该路线用更少等待和传输换 certificate 误差、遗漏慢节点、
异步版本冲突与更复杂的恢复。关键文档不可替代、需要全局一致快照或 certificate 未校准时，应回退同步 barrier、
上传完整授权材料或人工确认。现有证据只支持受测 device-cloud 文档隔离 workload，不给出通用网络或生产 SLO。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16341:start -->
filtered ANN planner 应把 selectivity error 到 plan regret 的 phase boundary 作为切换条件，而不是用单一 pre/post/in-filter 规则。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16341:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19692:start -->
旧的周期 reverse-kNN 扫描在毒文档入库后才处置；该工作把 sentinel hub-score、冻结阈值和 quarantine 决策放进写路径，由索引入口拥有 admit/reject 控制，阈值缓冲按写增量维护。代价是 sentinel/encoder 漂移和自然 hub 误报；tight-domain、删除最坏路径或监测盲区仍由 provenance 审核与周期扫描兜底。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19692:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19719:start -->
语义缓存的发布标准从 PR-AUC 排序改为 threshold-aware P-CHR 曲线与 CRR：cache owner 保存 score/threshold/命中预算，evaluation 将 ranking quality 分解为可校准差距和由正例率决定的结构差距，再决定是否上线 retriever/reranker。post-hoc calibration 仅是共存修复，不能替代重新训练或生产域阈值重估。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19719:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-24204:start -->
把 interval predicate 的双端点约束映射为统一 2D dominance space；每个 predicate 拥有独立 UDG instance，patch edge 只在 validity 保持时补路由，避免两个 scalar index 的交集爆炸。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-24204:end -->

### Retrieval Object 需要 Validity 与 Lifecycle

Passage ranking 在语料静态、事实长期有效时足够简单；持续变化的知识库中，失效事实若到生成后才被发现，已经污染了 retrieval set。更稳定的对象是带 provenance、validity interval、conflict state 与 lifecycle 的 atomic nugget：admission 先排除 expired/retracted 项，再在授权范围内排序。代价是 nugget extraction、关系维护与失效传播成本；来源无法原子化或生命周期未知时，应保留原 passage 并显式降级 authority，而不是伪造精细状态。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25641:start -->
事实纠正还需要区分“内容正确”与“生产检索能找到”。一种迭代分支把 correction 写成带原始来源和版本的 nugget，用真实 RAG 对触发 query 及 paraphrases 反复 probe，根据失败 trace 重写到可发现。Rewrite loop 只能优化 discoverability，不能改变事实 authority；每次改写都必须保留与原 evidence 的语义等价检查。

这种 test-harness 式优化增加索引构建、模型调用和 lineage 成本，也可能过拟合少量 query，甚至为了易检索而改变纠错含义。无法证明等价性或覆盖时，应回退不可变 correction+原文 provenance、人工 curated entry、hybrid retrieval，并在失败时直接 dereference 原始来源。单一生产架构与英语实验不证明跨系统的普遍增益。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25641:end -->

<!-- source-family:SF-2026-ARXIV-2604-27306 -->

### 视觉证据也必须有可追踪的 Claim–Evidence 生命周期

文档包含截图、图表或扫描页时，文本 chunk ID 不足以复现证据。ingestion 应保存 source 与 page revision、截图或渲染身份、region/bounding-box locator，再把区域证据逐 hop 绑定到 atomic claim。region locator 解决的是“回到哪里”，不能替代来源权威、entailment、sufficiency 或独立 verifier；页面重排、OCR 版本变化和图像裁剪都会使旧 locator 失效，因此必须随 corpus revision 一起版本化。

绑定到 atomic claim 后，还须核验拆分粒度与证据粒度是否匹配。把 parent claim 分为 subclaims，却为每项重复同一段 parent evidence，并不等于分别获得支持；一条受限对照在 oracle decomposition 下分别提供 aligned subclaim evidence、重复 parent evidence 与缺少标签的输入，发现分解增益依赖 granularity 与 label signal。因而要冻结拆分、证据内容和标签身份，再比较支持关系，不能由更细的 claim graph 自动批准答案。<!-- source-family:SF-2026-ARXIV-2602-10380 -->

[必要对照](https://arxiv.org/html/2602.10380v1)中，去掉 label 时 finer evidence 甚至不如重复 parent evidence，更多拆分还支付额外 evidence tokens 与调用成本。oracle、有限 parent/subclaim 人口和未核 sibling 切分不认证部署无泄漏；abstention 与 refuter 的相关也不证明政策因果。缺少可信拆分或标签、预算不足时，保留完整 parent context 与逐 claim verifier，而不是为追求细粒度丢掉成立条件。

更根本的限制是，自回归生成后的 token-level attribution 不会自动组合成可靠的 claim-level provenance。若生成时没有保存 evidence admission 与 claim mapping，事后仅靠 black-box query 重建 credit assignment 可能需要组合搜索，成本随长文本迅速增长。于是 provenance 不能被视为生成结束后的装饰：检索接纳、context packing 与 generation commit 必须共同携带证据身份；做不到时应明确标记 unsupported claim，而不是用一个模糊引用覆盖整段答案。

<!-- source-family:SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN -->
<!-- source-family:SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER -->

### Retrieval Control 应成为 Reader 外部的 Typed State

让 reader 在 prompt 中隐式决定是否检索、查哪里，在 corpus 小且单轮任务中最简单；多源、权限与预算约束出现后，决策无法审计或恢复。RAG controller 应外置 retrieval state，记录 query tree、已访问 source、预算、权限、证据覆盖与下一 routing action，再把受控证据交给 reader。收益是可重放、可恢复和最小权限，代价是 state schema 与 router 错误；state stale、错误剪枝或跨租户泄漏时应回退静态检索/人工批准。exact-v1 只支持 StateRAG 披露的 MARS/SMP 等机制和实验，不证明任意 corpus 或 reader 上的收益。<!-- source-family:SF-2026-ARXIV-2605-25379 -->

### Query Policy 与 Evidence Graph 分开拥有控制与证明

<!-- semantic-body-binding:SF-2026-ARXIV-2609-11065:start -->
固定 top-k、固定深度的 GraphRAG 在查询形态稳定时便于复算；复杂 query 却可能需要不同 seed、traversal、depth、beam、anchor/connector、stop 条件与 evidence budget。演进后的 query policy 不是自由生成一段检索提示，而是在 allowlist、范围 clamp 和默认值约束下，为本次请求提交一份有界 control vector。它拥有“准备怎样搜”的 proposal，不能创建 corpus fact、改写 ACL 或自行宣告答案证据充分。

按 query 调参能减少无关路径，也会把 analyzer latency、参数耦合和域外迁移失败带入关键路径。已有受控结果只覆盖共享 graph/generator 下的有限 benchmark：某些设置减少路径却增加端到端时延，跨数据集迁移也可能显著退化。因此 analyzer 过度扩张、控制向量越界、profiling 失效或尾延迟不闭合时，应回退固定 retriever、固定预算和已校准的 traversal，而不是把自适应本身当作收益。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-11065:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-10901:start -->
执行结束后还需要另一种状态：把实际 search trace 转成 evidence-propagation DAG，节点保存 query、result、answer 与 prior sentinel，边记录问题约束怎样被使用、证据怎样流向 claim，以及哪里注入了无来源先验。最小 supporting-query set 和 unsupported-prior edge 回答的是“这次 run 实际依赖了什么”，不能反向证明检索策略因果最优，也不能把结构完整的错误答案提升为事实。

图解析器与 attribution model 本身会漏边、错连或受 trajectory 格式影响；graph score 与正确率的相关性不是 truth oracle。其 identity 至少要绑定 trace schema、parser/attributor 版本、并行或串行路由语义、corpus revision 与无法解析比例。图不完整或高风险 claim 无法回到原始 locator 时，应降级为 unsupported，转人工、直接 citation/entailment、矛盾与约束检查或可执行 verifier。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-10901:end -->

两者组成同一条可恢复链，而不是两个互相自证的模型：`typed query policy -> bounded retrieval run -> evidence-propagation DAG -> claim-level answer gate`。前置 policy 负责预算与动作，后置 graph 负责记录已发生的证据流，最终 authority 仍来自原始证据与独立 gate；小语料、低风险或 schema 不稳定时，静态检索加逐 claim 引用仍是更可靠的 fallback。

### 从固定 Retriever 演进到可提交的 Logical / Physical Plan

外置 retrieval state 后，复杂查询不必直接绑定一个固定 backend。Controller 可以先把自然语言需求编译为带类型的
semantic operators 和 logical DAG，再由 physical planner 为每个 operator 选择检索后端、模型、阈值与执行顺序；
最终提交的是一份绑定 corpus/index revision、backend profile 和成本预算的 physical plan。Logical rewrite 只拥有
等价变换 proposal，physical planner 只拥有计划 proposal，RAG owner 才能在质量、延迟和成本约束下提交执行。

这条路径能让异构搜索、过滤与聚合共享一个可审计计划，却会引入语义编译错误、代价模型漂移和组合搜索开销。
Teacher label、backend profile 或 operator contract 变化时，应使旧计划失效并回退已校准的固定检索路径；单一 corpus、
查询形态稳定或延迟预算很紧时，固定 retriever 仍是更小且更可靠的系统。受限实验可以证明这类规划在其 benchmark
上改善 quality/latency/cost 选择，不能证明跨 operator 全局最优或跨 provider 可移植。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29151 -->

### Video Retrieval 需要显式的 Physical Plan

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23826:start -->
单一 scorer 在视频规模小、问题类型固定时最简单；复杂查询可以先生成 typed tool calls，由不同视觉/文本 scorer 产出 ranking，再用显式 boolean merge 形成 physical plan。Planner 只拥有计划 proposal，工具 coverage 与最终证据 Gate 才决定结果是否可用。

多工具计划提高可组合性，却会引入调用延迟、schema 漂移、排序不可比和 merge 错误。作者 benchmark 只支持披露工具与数据，不证明开放视频检索可靠；planner 越界、工具缺失或 provenance 不完整时，应回退固定 schema、单一已校准 scorer 或人工检索。arXiv:2605.23826v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23826:end -->

### Multimodal Memory Graph 必须分离 Evidence Identity 与 Structural Credit

把所有页面切成独立 chunk，在查询局部且文档关系弱时最简单；超长视觉文档中的同一事实却可能分散在图、表、正文与跨页引用里，单次向量排序既丢失关系，也无法说明一条推理路径为何保留某个视觉区域。更强的检索对象可以把文本或视觉单元、关系边和来源 locator 组成版本化 memory graph：graph builder 拥有结构 proposal，retrieval controller 记录实际 traversal、分辨率分配与 pruning frontier，reader 只消费已经接纳的 evidence subgraph。训练得到的 structural credit 可以影响下一次搜索，却不能改写节点来源或把高 reward 升格为事实。

图结构换来跨页组合与稀疏检索，也引入 graph construction error、过期 edge、错误剪枝和更昂贵的 provenance 维护；压缩后的视觉 memory 还可能删除后来问题所需的细节。因此 corpus 小、页面独立或关系提取不可靠时，保留 flat retrieval 与原页 fallback 更稳妥；高风险回答必须能从 traversal 回到原始 page/region，而不能只引用派生图节点。

<!-- SF-2026-ARXIV-2602-12735 -->

### Checker Reward 不能同时充当训练信号和独立证据

用 NLI/grounding checker 给 RAG policy 奖励，checker 与真实质量高度一致时能减少人工标注；policy 适应 checker 后，可能通过迎合判别边界获得高分而不改善证据支持。Training owner 与 evaluation owner 必须分离：checker 可生成 proposal reward，但 release gate 需独立 judge、held-out evidence 与多 seed regression。收益是保留可扩展反馈，代价是双评估链和更高成本；独立性不足或 reward collapse 时应冻结 policy、回退基线并审查错误 cascade。exact-v1 只支持论文的医疗 RAG、checker、模型和实验设置，不证明临床正确性或跨域稳定性。<!-- source-family:SF-2026-ARXIV-2605-25988 -->

### Ingestion 与 Query-time Workspace 是两条条件分支

预先解析、切分并构建向量或图索引，在语料稳定、查询复用率高时是合理旧路径：一次 ingestion 成本可以被许多查询摊薄，索引版本也容易统一审计。但在一次性 corpus、模式未知或更新快于索引发布时，预构建结构可能先支付大量无用成本，甚至在 query 到来前就冻结了错误的关系假设。

另一条路径是在查询时创建隔离的 document/value workspace。Retriever 直接读取原文，把中间选择、集合运算与派生值写入只属于本次 run 的工作区，再由 reader 消费已通过授权和 evidence gate 的结果。Workspace 只拥有查询期计算状态，不能改写 corpus truth、绕过 ACL，或把临时派生值升格为长期事实。若重复查询增加，可把经过验证的热点表示或少量模式发现结果提升为 limited-ingestion artifact，但必须绑定 corpus revision、builder 与失效条件。

这种分支省去前置图构建，却把扫描、工具调用和中间状态管理移到 query critical path；大 corpus、高并发或严格尾延迟下可能比成熟索引更贵。权限、workspace 隔离、派生值污染或扫描预算无法闭合时，应回退已版本化的 lexical/vector index；稳定高复用语料继续优先 offline ingestion。exact-v1 的六个 corpus 结果只支持这种条件分支，不证明“零 ingestion”普遍优于索引，也不覆盖生产并发、频繁查询或多租户隔离。

<!-- source-family:SF-2026-ARXIV-2607-25135 -->

### 多跳 RAG 可以把推理计划变成可执行程序

自由文本 chain-of-thought 足以表达短推理，但多跳检索需要反复产生子问题、保存中间值并根据失败修改下一步；仅保留叙述文本时，系统很难区分检索失败、变量引用错误和答案合成错误。一条更可审计的分支把 query decomposition 与 planning 分开：planner 生成受限的可执行程序，runtime 逐步执行 retrieval/QA operator，把中间结果写入 typed workspace，编译或运行错误再作为修复证据返回。程序拥有控制流，原始文档仍拥有事实权威，answer gate 只接纳能回到 source locator 的结果。

可执行表示换来显式状态、确定性错误反馈和局部重试，却增加生成无效代码、sandbox、资源限制与程序正确但证据错误的 failure mode。简单单跳查询仍以固定 retrieval-and-read 为更小基线；高风险场景还需独立 entailment、citation 与权限检查。exact-v1 的五个 QA benchmark 只证明这一接口在披露设置中的任务收益，不证明生成的程序语义正确、生产隔离完备或开放域事实可靠。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12975 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05245:start -->
### 多跳检索的停止条件应由 Evidence Gap 驱动

固定 top-k 在问题短、语料同质且一次检索通常足够时简单可靠；多跳问题却常出现两种相反浪费：证据仍有缺口时过早生成，或证据已经充分后继续堆叠冗余文档。更可控的路径把 `evidence set + entity ledger + unresolved gaps + remaining token budget` 保存为检索状态：controller 根据尚未闭合的 gap 生成 micro-query，以 corroboration、coverage 与 redundancy utility 更新候选集，再由独立 sufficiency gate 决定继续、回答或 abstain。Query policy 只拥有下一检索动作，原始来源仍拥有事实，reader 不能用流畅答案覆盖未闭合 gap。

这种 gap-repair loop 用更精确的停止换来状态维护、权重校准与额外检索开销；gap detector 也可能制造伪缺口或漏掉隐含前提。现有证据仅覆盖 HotpotQA、固定小规模 evidence set 与作者 retriever/generator，不证明 web-scale completeness。gap 不可靠、预算不足或问题本就是单跳时，应回退 question-anchored fixed top-k，并把未满足约束显式交给 answer gate，而不是补猜证据。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05245:end -->

独立 sufficiency decider 自身昂贵时，可以先做单侧调用路由：便宜的 coverage margin 只在明显未覆盖时暂缓 decider、继续检索，其余状态仍调用原 decider。这个前置门槛不拥有回答或停止权，budget exhausted 也须另报 budget exit，不能把省掉验证调用解释成已充分。Coverage 预测、真实证据与最终采用是三个对象；固定 top-k 或每步完整 decider 仍是更易审计的旧路径。

[CoVeR 的受限检索实验](https://arxiv.org/html/2609.26086v1)支持这条 one-sided defer 分支，而非 embedding margin 对事实真值的校准。训练/阈值、分布漂移和误暂缓会增加重复搜索，single-seed 与 held-out proxy agreement 也不构成完整 Agent latency 或安全保证；LODO 与独立gold只覆盖所测协议。门槛不稳定、风险高或无匹配校准数据时，恢复每步 decider 与原 evidence gap/abstain gate，不让便宜 router 静默替代它。<!-- source-family:SF-2026-ARXIV-2609-26086 -->

### 无效检索方向是控制记忆，不是事实反证

Evidence-gap repair 知道缺什么，却还可能反复访问已经无助于当前问题的方向。一个有状态分支把 supportive/contextual 文档保留为带原文身份的 evidence units，将 irrelevant 方向另外提炼为 query negative constraints，供下一次补检避开重复探索。这里的 negative 表示“对当前 query 无信息”，不是“文档反驳了某项事实”；增强 query 只作为临时控制输入，不回写成新事实。来源继续拥有证据 authority，搜索记忆只拥有减少无效动作的 proposal 权，不能用同一个负面标签合并两种责任。

这增加相关性误判、历史维护、过时控制记忆与额外 LLM 调用；遗漏的背景材料若被永久禁止检索，反而会制造新的 evidence gap。`arXiv:2604.14170v1` 的 Stateful Evidence-Driven RAG 在固定 DPR 与生成器下给出 negative-evidence 消融及受控噪声结果，但 relevance、confidence、query refinement 与 stop 都由同一 LLM 产生，不是独立真值或可靠 abstention 保证，更多轮次也非单向收益。query/corpus 改变、分类不可靠或预算不足时，应重验或丢弃控制约束，回退固定 top-k 并显式交付未闭合 gap，而非将曾经 irrelevant 的方向永久封为错误知识；跨会话持久记忆的写入资格仍由下一章管理。

<!-- source-family:SF-2026-ARXIV-2604-14170 -->

## RAG Benchmark 的 Corpus 本身也是实验状态

直接从开放语料抽问答最接近真实分布，却难以确认答案、证据与污染边界；合成问答又容易只测生成器偏好。一个更可审计的分支是对冻结 corpus 做受控 transformation，生成可验证 answer/evidence pair，同时保存 source span、变换规则、generator/verifier revision 与污染检查。这样 retrieval failure、generation failure 与 evidence mismatch 可以分别归因。

代价是构造成本、变换偏差和任务自然度下降；高分只在 corpus、transformation、retriever、verifier 与 leakage policy 冻结时可解释。开放域线上评估仍需要真实流量与人工核验，受控 benchmark 不能替代它。[受限证据：arXiv:2605.08838v1]

<!-- source-family:SF-2026-ARXIV-2605-08838 -->

即使 corpus 已冻结，相关性标注也可能只是旧 retriever 的候选池，而不是所有相关证据的完整集合。新 retriever 找到未标注的有效 chunk 时，按旧 qrel 将它直接记为 irrelevant，会把标注覆盖不足误归为检索失败；生成器答对而旧 gold 未命中，也不能据此断言答案只来自参数知识。评价身份因此还要保存 judged pool 的构造来源、qrel revision 与 unjudged/unknown 状态；在作这些归因之前，定点审查未标注的 top-k，补齐有依据的标签，并在同一标注版本下重新比较系统。

[有限检索池的补标与重评价](https://arxiv.org/html/2602.06526v1)支持这条测量边界，不证明扩池后的 gold 对未来所有 retriever 无偏。归一化指标的理想分母也会随标签改变，应同时报告覆盖变化和重新计算的排名，不能把得分变化当作系统本身改善。模型预过滤、模型间同意与人工升级仍有残余偏差，增加候选、人审和复验成本；未核的负样本继续保留 Unknown。小语料能完整标注时，固定 qrel 和简单 top-k 仍更直接；开放池或预算不足时则限定评价覆盖，而不是让未标注自动拥有否定证据的资格。<!-- source-family:SF-2026-ARXIV-2602-06526 -->

## 本章在知识树中的位置

RAG 是 Context 的 external knowledge path，不是长期用户状态的全部实现。下一章讨论 Memory 如何跨交互写入、压缩、检索和遗忘状态，以及为什么 memory write 比 retrieval 多一层信任问题。

## 从机制演进到系统设计

RAG 从 top-k 相似度检索演进到 evidence admission 和闭环预算控制。Query、candidate generation、rerank、dedup、context allocation、answer attribution 与 abstention 是不同阶段；高相关不等于足够证据，shared index 的 population density 和跨租户 crowding 也会改变召回行为。

更多检索可以提高 recall，却增加噪声、token 成本、污染传播和错误置信。系统应冻结 corpus/index/embedding revision，记录候选为何被选、模型是否实际使用证据，并在 coverage 不足或来源冲突时拒答。小语料、稳定查询或 exact lookup 场景中，简单 top-k 仍可能是更透明的 baseline。

## 自检问题

1. RAG 相比参数化知识提供了什么能力？
2. 为什么 embedding vector 不是 source of truth？
3. Authorization 为什么必须发生在 retrieval data path？
4. Dense 与 lexical retrieval 的偏好有何不同？
5. 为什么正确 retrieval 仍可能产生错误回答？
6. Index version 为什么要进入 trace？
7. Relevance、context sufficiency 与 answer faithfulness 分别归属哪一层？
8. 为什么多步 Agentic Retrieval 中 query、compression、verification 与 stop 必须作为联合 policy 评估？
9. “平均搜索步数更少”为什么既可能是效率提升，也可能是 premature failure？

## 小结

RAG 将外部 evidence 动态送入 Context，换来更新性与 provenance，同时引入 ingestion、ranking、security 和 consistency 的新系统边界。预测性检索可以隐藏部分 IO，SSD filtered ANN 可以扩大索引复用，但二者都必须把错误预测、过期、最终过滤和 evidence admission 留给明确 owner。下一章进入可跨会话演化的 Memory。

## Review notes

- `SF-2026-ARXIV-2602-22591` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22591v1) §2–4/blocks21–57、60–79、83–97，2+1+3=6。固定层区间/null校准/多次调用费用与BEIR反侧，BRIGHT test-oracle不采用为部署证据。fresh非原packet作者必要原证与actual owner复核后窄写，作者正文/完整邻接/自身末注已顺读，root 非写入者已实际核正文、完整邻接与自身末注，POST通过；未核代码/复现。
- `SF-2026-ARXIV-2602-22787` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22787v1) §3–6/blocks30–58、67–76、89–100、118–124，2+1+3=6。knowledge-testing操作label、title-disjoint split、decoy慢侧；不授causal来源、truth或RAG修复闭环。fresh非原packet作者必要原证/actual owner复核与窄写，作者实际邻接已读，root 非写入者已实际核正文、完整邻接与自身末注，POST通过；未核实现/复现。
- `SF-2026-ARXIV-2602-22805` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22805v1) §3–5/blocks46–59、66–74、80/83、90–95、103/105、110–118，2+2+2=6。record/page skew与metric共址、QPS/meanlatency分账；不采B倍hit-rate、所写visited termination配方或生产安全保证。fresh非原packet作者必要原证/actual owner复核与窄写，作者实际邻接已读，root 非写入者已实际核正文、完整邻接与自身末注，POST通过；未核代码/复现。
- `SF-2026-ARXIV-2602-23342` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23342v1) §3.2/4.3/5、blocks48–57、65–75、78–90、104–118，2+2+2=6。Table2布局控制保compute降/I/O升、Table4 DPR慢侧，earlydispatch不授exact顺序等价。原准备在packet24非23。fresh非原packet作者必要原证/actual owner复核与窄写，root 非写入者已实际核正文、完整邻接与自身末注，POST通过；未核实现/复现。
- `SF-2026-ARXIV-2602-22510` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22510v1) §2.1–2.5/§3，blocks26–60、101–109、120–126，2+1+2=5，具体owner差额深入。只采用signed dictionary/可控MMR接口及有限neg对照，不授anchor单因素、可选AE增益或附录指标定义；缺完整budget不支持一般性能。作者必要证据/owner与实际正文邻接已核，root 非写入者已实际核正文、完整邻接与自身末注，POST通过；未核实现/复现。
- `SF-2026-ARXIV-2602-22547` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22547v1) §3–5、blocks19–66，2+1+2=5，具体owner差额深入。固定general/passage与query-only domainprefix，Table2/3保2.3M×8及prior人口；不授总2%/任意热升级。作者必要证据/owner与实际正文邻接已核，root 非写入者已实际核正文、完整邻接与自身末注，POST通过；未核实现/复现。
- `SF-2026-ARXIV-2602-23029` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23029v1) §3.2–4.3/§7.4、blocks32–53、58–61、67–76、96–101，2+1+2=5，具体owner差额深入。双路proposal/shared verifier/threshold与iteration局部慢侧，不授分支独立likelihood或calibrated confidence；额外50候选/编辑/外部调用近文。作者实际正文邻接已核，root 非写入者已实际核正文、完整邻接与自身末注，POST通过；未核代码/复现。

- `SF-2026-ARXIV-2602-21514`：exact-v1 I/O/layout/search机制与同库组合实验；PS×PSe互补、饱和SSD下speculative多读与高维recall反侧分别保留。仅披露Xeon/NVMe/libaio/48workers/5runs，不授全引擎或最坏I/O保证；未复现。 非原 packet 作者必要原证/actual owner PRE 与窄写完成；root 已实际顺读正文、完整邻接与自身末注，POST 通过。
- `SF-2026-ARXIV-2602-21543`：exact-v1 §3–4与训练说明；all-language anchors与translation groups分责，same pair count非same实例/步数，保各语言反退、loss归一差异与重编码费用。未核生成任务、代码或复现。 非原 packet 作者必要原证/actual owner PRE 与窄写完成；root 已实际顺读正文、完整邻接与自身末注，POST 通过。

- `SF-2026-ARXIV-2602-10833` — Daily `2026-02-13`；[Training-Induced Source Bias exact-v1](https://arxiv.org/html/2602.10833v1) §3–5、Tables3–6及训练配置。2+1+2=5，paired-source训练阶段排名评价反证深入；不授普遍pro-LLM、PPL因果或语义改写等价保证。配对/重新编码成本与模型/数据反侧近正文。root必要原源/current owner/邻接PRE通过；root实际核正文143–170、邻接与末注，非作者POST通过、窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2601-09985`（Experimental）— Daily `2026-01-17`；[FaTRQ exact-v1](https://arxiv.org/html/2601.09985v1) III-A–E/IV/V-A–E，2+2+3=7。只采用 coarse-distance reuse、ternary residual far-memory、local-boundary OLS 与裁短后完整向量精化，不采无条件 unbiased 或可证无损 early-stop。88M Wiki/100M LAION、10k L2 top10 queries，A10/40-thread Xeon 基线；CXL Ramulator 与 ASAP7 综合非真实设备吞吐。未验证生产并发、P99、更新或答案质量，未复现；root必要原源与当前owner写前通过，root实际正文/邻接及末注非作者写后复核通过，非日级验收。

- `SF-2026-ARXIV-2601-05549` — Daily `2026-01-13`；[TMRL exact-v1](https://arxiv.org/html/2601.05549v1) §3–4及时间权重/维度反侧。只采用 temporal prefix 与 semantic tail 的条件表示取舍，不认证时间真值或普遍低维优势。未复现；root 必要源/当前owner写前通过，root实际新增正文/前后衔接及末注写后复核通过。

- `SF-2026-ARXIV-2601-04932` — Daily `2026-01-10`；[GenProve exact-v1](https://arxiv.org/html/2601.04932v1) §3 typed relations、§4 Eq3–10 reference matching/F1、§5 setup/消融及限制。原2+2+2=6，具体claim/provenance接口缺口深入；关系taxonomy借TROVE不计原创。只采用联合生成关系与reference-match/entailment/实际用证分账，不授内部因果、item-level人类一致、全质量提升或生产开销保证；硬件Not Disclosed，未复现。root必要原源及具体owner写前通过，jan02_v3实际正文798–831及本注非作者写后复核通过，未重复原源审阅，日级Gate待验。

- Daily 2026-03-07：[Reranking scaling exact-v1](https://arxiv.org/html/2603.04816v1) §4.2/5/6.2/7–8。CE是Contrastive Entropy而非training cross-entropy，BM25 top100/64negatives/normalized scores；NDCG本来primary，未指控作者以loss代质量。Ettin17M～1B、100k MS MARCO queries、一epoch、不同训练paradigm batch与heldout exposure边界保留，摘要/正文MRR不一致不采用。root必要定义/趋势及窄锁通过，作者已写两段，root实际原文/正文及邻接POST通过；未复现。

- `SF-2026-ARXIV-2603-04238`：[exact-v1](https://arxiv.org/html/2603.04238v1) §3、Appendix C Tables 3–4；Daily 2026-03-06。只采用 OCR/转录变化的检索归因校验；配置选择与非重跑基线、空间语义损失均保留。作者源/owner/邻接与实际写后检查完成；root 必要源、实际正文及邻接独立写后复核通过，未复现实验。

- `SF-2026-ARXIV-2609-16875`：[exact-v1](https://arxiv.org/html/2609.16875v1) 的 backward-compatible adapter；正文 owner 为检索索引升级，不是 token embedding。迁移策略为系统设计推断，不把作者受限多模态评价写成零回填保证。
- `SF-2026-ARXIV-2609-16391`：[exact-v1](https://arxiv.org/html/2609.16391v1) 的受控 PTQ 与 Limitations；只支持 family/task 绑定和代理误差边界，不证明混合精度 allocator 或整数 Kernel 的加速。
- `SF-2026-ARXIV-2606-29151`：SemBench 上的 intent-specific DAG 与异构 backend 支持受限计划选择；teacher-label noise、operator 组合和 Azure/API 与本地模型之间的可移植性仍有限，正文不作全局最优承诺。

- `SF-2026-ARXIV-2604-22171`（Experimental）：[MCI exact-v1](https://arxiv.org/html/2604.22171v1) §3.1–3.2、§4.1–4.2、§5 与 Appendix A；Daily 2026-04-27。只采用谓词无关的 clique-cover 邻接表示、查询期过滤与多起点遍历作为过滤组合多变时的条件分支；可信 policy owner 仍决定授权，索引与检索器不持有 ACL 真值。作者在 CPU/L2 filtered-ANN 数据集、合成 Zipf 标签下报告 Recall@10、QPS、索引大小和构建成本；高 recall 的 beam/吞吐代价明显，部分较低 recall 点 ACORN 更快。昂贵谓词可能要求全量布尔位图或付出拒绝采样成本，Appendix A 只把动态增删列作未来工作。未验证真实 ACL churn、在线索引更新、生产 RAG 答案质量或租户隔离正确性；未复现实验。本轮按具名漏收重开，正文与相邻 RBAC/SSD 路径的[写后独立复核已通过](../../papers/2026/04/_sources/daily-20260427/V3_APR01_22171_CH76_WRITE_AFTER.md)，不代表日级 Gate。

- `SF-2026-ARXIV-2604-20199`（Experimental）：[All Languages Matter exact-v1](https://arxiv.org/html/2604.20199v1) §2.1–2.3、§3.1–3.4/Table 5、Limitations 与 Appendix C；Daily 2026-04-23。只采用多语言候选池内按**证据语言**拆分召回、重排留存与答案支持的评价边界；作者按各语言生成后用已知答案分数择优的是离线 estimated oracle，非上线 selector。13 语言 MKQA/BGE-M3 top-50→top-5 rerank，实验只改 reranker，character 3-gram recall 并非事实支持；总体小幅改善掩盖个别语言退步，未证明跨语料/reader/生产成本。root 已读必要 exact-v1 并据非作者 source→owner 反查实际落笔；apr20_resume 对正文两侧及本条注记的[非作者写后复核](../../papers/2026/04/_sources/daily-20260423/V3_APR20_20199_CH76_WRITE_AFTER_INDEPENDENT.md)通过，未复现实验，不代表日级 Gate。

- `SF-2026-ARXIV-2604-22722`（Experimental）：[UAE exact-v1](https://arxiv.org/html/2604.22722v1) §2.1–2.2、§3/Table 1、§4；Daily 2026-04-27。仅采用指定 reader/答案集合的离线 perplexity 效用→pairwise proxy→soft-target 双塔训练、线上 ANN 这一条件分支；teacher 偏好不是 support 真值。QASPER、NewsQA 并非所有指标优于强对照，检索阶段延迟不包含 teacher 标注、建索引与读者生成。root 必要源→实际 owner 并实写，apr02 对 exact-v1、真实正文和邻接独立写后 PASS；未复现实验，不代表日级 Gate。

- `SF-2026-ARXIV-2604-22678`（Experimental）：[BERAG exact-v1](https://arxiv.org/html/2604.22678v1) §3 Eqs.2–6、§4.6–4.8/Tables 5–6、Limitations；Daily 2026-04-27。只采用每文档生成分支、逐 token 后验混合及可剪枝状态；后验不是真值或充分性，单文档 mixture 不显式覆盖多文档组合。K=50 naive 470.2 vs 拼接 203.0、Top-P 44.4 ms/token 仅作者 E-VQA decode 协议，重复 query prefill、KV、BEFT 训练与部署吞吐未证明；Qwen2-VL-Instruct/PreFLMR-L 为主要条件。root 必要源→实际 owner 并实写，apr02 对真实正文及相邻独立写后 PASS；未复现实验，不代表日级 Gate。

- `SF-2026-ARXIV-2604-22180`（Experimental）：[exact-v1](https://arxiv.org/html/2604.22180v1) §III-B–E、§IV-C–E；Daily 2026-04-27。仅采用同一 encoder 兼任 first-stage retrieval 与 compressed-passage listwise rerank 输入时的双目标/双候选池验收；Table V 删除 retrieval loss 后重排 BEIR 均值 .5440→.5462 未降，standalone 检索退化是作者另述而非该表直接量化，Table III dense-only BEIR .5317 低于 BM25 .5440。成本含双模型训练、离线编码和 index revision，Table IV 的 one-token/zero-decode 不是端到端 latency。root 已核必要来源→实际 owner；实际正文和相邻衔接待非作者写后复核，未复现实验。

- `SF-2026-ARXIV-2604-22661`（Experimental）：[exact-v1](https://arxiv.org/html/2604.22661v1) §3.4–3.5、§4.1–4.4；Daily 2026-04-27。采用同一 information need 的多个 query variant 在执行前选一，与 ranking／recall 和答案 nugget 效用分账；TREC-RAG 2024、固定检索器与 top-5 reader、未匹配的端到端成本限制外推。root 已核必要来源→实际 owner，并顺读实际正文与 document-side、answer-side 相邻交接，写后复核通过；未复现实验。

- `SF-2026-ARXIV-2604-21511`：[exact-v1](https://arxiv.org/html/2604.21511v1) §3–7；Daily 2026-04-24。仅吸收重建预训→检索联训的 learned sparse latent 词表与倒排 posting 身份；Top-K token 不保证文档聚合稀疏，解释名称非 concept 真值。编码器/字典/index 同 revision 发布属于工程判断，受限域内/多语反例与未测真实延迟保留。root 已完成必要源→当前 owner 写前复核，且实际正文与相邻衔接写后非作者复核通过；未复现实验。

- `SF-2026-ARXIV-2604-16021` — [LogicLoc exact-v1](https://arxiv.org/html/2604.16021v1)，Daily `2026-04-20`。采用 §3.1–3.4.3 的 source facts/query proposal/确定执行和空关系有限探针分权，probe 不是最终答案，stable-empty 包括失败，不证明无解，fragile-empty 不证明原条件错误。§4/Tables2–4/§5 的225非空synthetic/9Pythonrepos与单repo负例、SWE274范围、Qwen VAL→Full 104→136秒且ExecSucc相同、Claude比例分母歧义均保留，不采完备否定、跨语言能力、泄漏排除或生产SLO。root source→actual owner有限采用及真实两段与相邻内容的非作者写后均通过，未复现实验，不代表日级验收。

- `SF-2026-ARXIV-2604-17237`：[exact-v1](https://arxiv.org/html/2604.17237v1)，Daily 2026-04-21；§2.1–2.5/Eq5、§3.1/Table1–3、§3.5/Limitations 与 E/F。采用监督 attention readout/head/weights/layout/截断执行的共同身份，不采用 attention 因果解释、完整生成等价或格式成功即 relevance 正确。211-query 衍生训练、8-head 重选、显式 attention 与有限配置/质量反例保留。source→实际 owner 的必要非作者审阅通过（apr02）；本轮实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-16686` — [NWCAD exact-v1](https://arxiv.org/html/2604.16686v1)，Daily `2026-04-21`。必要证据 §3.1–3.3、§4.1–4.5、§6/Table3、AppB/C；采用共同 prefix 下条件 token 回退，不采用全 context 无退化或开放正确性保证。受控阈值选择、双 forward 与近似分布比较成本保留。有限非作者 source→owner 采用核验及 root 对实际正文、两侧 prior/context 交接的写后独立复核通过，实验未复现。

- `SF-2026-ARXIV-2604-14170` — [Stateful Evidence-Driven RAG v1](https://arxiv.org/pdf/2604.14170v1)，Daily `2026-04-17`。采用 §3.3–3.4 / §5.2–5.4 的 evidence unit 与 transient negative query constraints 分权；同LLM relevance/stop非独立真值，固定DPR/受控噪声及轮次限制保留。复用既有 apr01 与日期/准入审计中的窄采用 PASS，root已实际顺读正文及两侧、复用有效必要证据后写后独立PASS；真实整合，Ch76锁释放。
- `SF-2026-ARXIV-2604-14403` — [ECG v1](https://arxiv.org/pdf/2604.14403v1)，Daily `2026-04-17`。采用 §3–5/Tables1–4 的 Eret→Ecomp 一份持久化表示，保留 scaling 消融、top1/向量预算与非手机SLO边界；复用 `V3_ORIGINAL_GAP_INDEPENDENT_AUDIT.md` 必要原文/真实owner PASS，root已实际顺读正文及两侧、复用有效必要证据后写后独立PASS；真实整合，Ch76锁释放。
- `SF-2026-ARXIV-2604-14488` — [CAR v1](https://arxiv.org/html/2604.14488v1)，Daily `2026-04-17`。采用 §2.1/Definitions6–7/§3.2 的 anchor→entity-scoped authority补检→admission；隔离Theorem4必要方向过述，静态确定性scope假设不升级通用保证。复用 `V3_ORDINARY_TEN_FOUR_INDEPENDENT_AUDIT.md` §1前置 PASS，root已实际顺读正文及两侧、复用有效必要证据后写后独立PASS；真实整合，Ch76锁释放。

- `SF-2026-ARXIV-2604-09173`，Experimental：[exact-v1](https://arxiv.org/html/2604.09173v1) §3.1–3.5、§4.1–4.2、§5.1–5.2.2。DecoupleVS向量/index分离；dual32-core Xeon8336C、512GB DDR4、SamsungPM9A3 NVMe、64threads，109M proprietary/100M–1.4B公开数据、recall@10配QPS/P99。8bit向量delta不改善，Ls50与部分billion低recall吞吐反收益（较PipeANN最高低11.9%）；不采用生产freshness/SLO保证，未复现实验；本次必要来源、实际正文及相邻论证的非作者独立复核通过（root）。

- `SF-2026-ARXIV-2604-09019`，Experimental：[exact-v1](https://arxiv.org/html/2604.09019v1) §3–6/Alg1：Logistic Regression 二元选择 Q/Union，主配置冻结 α=0.25；881 development questions/五折、100 sentence annotations，MuSiQue303/Hotpot570，NV-Embed-v2/BGE/e5-mistral 与固定候选池，只评价 hop-1-correct。Table2 主配置迁移 MuSiQue+5.3pp（p=.002）、Hotpot+1.1pp（p=.143）；§6.5 P-weighted α 消融为+2.6pp不显著/−0.2pp，不可混作主配置。不能承诺开放检索、第一跳正确性、最终 LLM 答案或生产 SLO；§5.3作者成本/延迟不等于完整 serving 合同。Gaussian-score 假设不证明所有语料的 q/bridge 分界。root 已独立重开必要原文并核修正后实际正文，采用通过；本地实验未复现。

- `SF-2026-ARXIV-2604-00500`，Status: Experimental：[exact-v1 §3–6](https://arxiv.org/html/2604.00500v1) 只支持两种 parser、单页 Evidence Unit 与作者的 1,340 页/1,551 自动 QA 协议；D2/D3 graph schema 尚未 runtime 执行，parser 质量和 chunk 长度是未消除的变量。[当前 artifact](https://github.com/hanyeonjee/evidence-units) 只开放 evaluation code/QA，不含完整 EU 构建管线，且 README 的页数/指标不同于论文 v1；不能把现时 README 当作当窗复现或改写 v1 结果。

- [The Cost of Context](https://arxiv.org/html/2605.05594v1)（Status: Experimental）：仅支持受测六个模型、三个数据集与 RTX A5000 上的 multimodal textual-bias failure 和 BAIR 诊断/重平衡，不支持通用 attention verifier。

- [Selected-object identity handoff v1](https://arxiv.org/html/2609.04579v1)：采用§2–4、§6及limitations的接口区分，不采用直接lookup普遍提高正确率的推论。实际选中身份与标注身份不等价；64条高反差删除样本及59条sham仅支持该子集，日志hash不证明预声明时间或来源真实性。书稿只增加有明确selected-return合同的条件分支。

- `SF-2026-ARXIV-2602-13165`（Status: Experimental）：exact-v1 支持 Krites 的 static/dynamic threshold fast path、grey-zone off-path verification 与 future-only auxiliary overwrite；evaluation 以 benchmark ground-truth equivalence classes 模拟 judge，未证明真实在线 judge、动态 corpus、capacity/invalidation 或生产 tail latency。https://arxiv.org/html/2602.13165v1

- `SF-2026-ARXIV-2602-12735`（Status: Experimental）：exact-v1 的 §3.1～3.3 描述 multimodal memory graph、graph-modulated visual memory 与 graph-guided policy optimization，§4.1～4.3 给出作者 benchmark、结果与分析，§6/Impact Statement 不构成开放域可靠性证明；证据不覆盖 graph provenance 的生产维护、动态 corpus 或高风险事实核验。https://arxiv.org/html/2602.12735v1

- **HaS（arXiv:2604.20452v1；Status: Experimental）**：支持基于历史 homologous query 的 speculative retrieval draft、surrogate validation 与 full-retrieval fallback。证据限于作者数据集、cache/fuzzy channels 和实验设置，不证明代理条件在开放域、高风险或动态 corpus 中可靠。https://arxiv.org/abs/2604.20452v1

- RetrievalRouter（per-query modality/architecture selection；Status: Experimental）：
  https://arxiv.org/abs/2608.25625v1

- RH-RAG（隐私约束长文的 outline/section/check 分层；Status: Experimental）: https://arxiv.org/abs/2608.01311

- AVA（长视频的事件图与多视图检索；Status: Experimental）：https://arxiv.org/html/2505.00254v1
  - 证据边界：3 秒片段描述、语义合并、事件/实体/时间图与多视图搜索只在 AVA-100 的 8 段视频、120 个问题上评估；不证明实时流、开放域或图陈旧条件下仍成立。
- Distributed RAG（peer-owned corpus 的 topic-aware discovery；Status: Experimental）：https://arxiv.org/html/2505.00443v1
  - 证据边界：结果来自仿真网络；不覆盖对抗 peer、真实网络故障、隐私证明或生产 tail latency。
- HONEYBEE（RBAC role graph 驱动 ANN physical partition；Status: Experimental）：https://arxiv.org/html/2505.01538v1
  - 证据边界：headline 只绑定作者 RBAC benchmark、HNSW 参数与 workload；不证明动态 policy、任意数据分布或生产 tail latency。

- OmniRetrieval（heterogeneous source-native operators；Status: Experimental）: https://arxiv.org/abs/2605.29250
- GrepSeek（programmable lexical retrieval；Status: Experimental）: https://arxiv.org/abs/2605.29307

本章止于 external knowledge retrieval，不把 vector database 当作模型 Embedding，也不把 RAG 等同于 Agent Memory。所有性能结论保持 workload/corpus 条件。

Primary-source 入口：

- Retrieval-Augmented Generation: https://arxiv.org/abs/2005.11401
- Dense Passage Retrieval: https://arxiv.org/abs/2004.04906
- BIPIA / indirect prompt injection: https://arxiv.org/abs/2312.14197
- Sufficient Context: https://arxiv.org/abs/2411.06037
- RARG / relevance-aware corpus interaction（Status: Experimental）:
  https://arxiv.org/abs/2607.24223
- KARL（Status: Experimental；joint retrieval/compression/stopping policy；公开训练 artifact 不完整）:
  https://arxiv.org/abs/2603.05218
- DeepSearchQA（set completeness、entity resolution 与 stopping；Status: Experimental）:
  https://arxiv.org/abs/2601.20975
- Sage（agent-conditioned retriever interface；Status: Experimental）: https://arxiv.org/abs/2602.05975
- Revisiting Text Ranking in Deep Research（query-dialect/ranker contract；Status: Experimental）:
  https://arxiv.org/abs/2602.21456
- Multi-Vector Index Compression in Any Modality（index-budget contract；Status: Experimental）:
  https://arxiv.org/abs/2602.21202
- Rubric-Oriented Document Set Selection（set-level evidence utility；Status: Experimental）:
  https://arxiv.org/abs/2607.19747
- OpenSeeker（graph-grounded search training；Status: Experimental）: https://arxiv.org/abs/2603.15594
- BubbleRAG（multi-anchor evidence subgraph；Status: Experimental）: https://arxiv.org/abs/2603.20309
- Adaptive Compression for Edge-based RAG（net energy / fidelity contract；Status: Experimental）:
  https://arxiv.org/abs/2608.19535
- TurboVec（ANN kernel tenant pre-filter 与 codebook-oblivious quantization；Status: Experimental；不构成完整 embedding privacy 证明）:
  https://arxiv.org/abs/2607.16973v1

### Daily integration evidence trace

<!-- daily-books-trace:SF-2026-ARXIV-2607-24781:start -->
- `SF-2026-ARXIV-2607-24781` — Daily [2026-07-29](../../papers/2026/07/29/README.md)；primary `arXiv:2607.24781v1`；正文锚点“文档结构、查询改写与答案核验必须分层消融”。本章吸收 document/query/answer 三层责任、并行 heading index 与预算化 page/section 展开；作者的小规模企业文档实验不证明该分支普遍优于普通 chunk 或 Agentic Search。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24781:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25135:start -->
- `SF-2026-ARXIV-2607-25135` — Daily `2026-07-29`；primary `arXiv:2607.25135v1`；正文锚点“Ingestion 与 Query-time Workspace 是两条条件分支”。
  本章吸收 query-time document/value workspace 与 limited-ingestion 的选择边界；六个 corpus 的作者结果不证明零 ingestion 在高复用、多租户或严格尾延迟条件下更优。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25135:end -->

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22778` — primary `arXiv:2606.22778v1`; Method=`arXiv:2606.22778v1 — §Lightweight evaluation and Nano-set construction; §Design of HAKARI-Bench; §Appendix A Nano-set construction and dataset list`; Evaluation=`arXiv:2606.22778v1 — §HAKARI-Bench: A Lightweight Benchmark for Comparing Retrieval Architectures and Efficiency Settings under Unified Conditions; §Retrieval evaluation benchmarks and retrieval architectures; §Lightweight evaluation and Nano-set construction`; non-proof=`arXiv:2606.22778v1 — §Discussion; §Scope of evaluated models; §Conclusion`; fallback=该 family 的 failure pressure 是：With the rapid spread of retrieval-augmented generation and semantic search, choosing the right embedding and retrieval configuration is increasingly hard. 披露的 evaluation signal 是：HAKARI-Bench does not replace full evaluation; it enables rapid model selection, regression detection, and reading the quality-efficiency Pareto frontier. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23642` — primary `arXiv:2606.23642v1`; Method=`arXiv:2606.23642v1 — §3 Method; §3.1 Scoring, Training, and Retrieval; §3.2 Random Prefix-Length Augmentation`; Evaluation=`arXiv:2606.23642v1 — §4 Experiments; §4.1 Setup; §4.2 Main Results`; non-proof=`arXiv:2606.23642v1 — §Storage overhead.; §Source attribution.; §5 Conclusion`; fallback=该 family 的 failure pressure 是：Long-context retrieval exposes a tension: single-vector embeddings lose fine-grained detail, while token-level multi-vector methods incur prohibitive storage. 披露的 evaluation signal 是：Experiments on MLDR-en, BrowseComp-Plus, and LongEmbed show that MPE is competitive with or outperforms single-vector, independent-chunk, and multi-vector baselines, while providing a natural source attribution mechanism for locating evidence chunks. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24204: `arXiv:2606.24204v1`; exact-v1 URL=`https://arxiv.org/html/2606.24204v1`; Method=`https://arxiv.org/html/2606.24204v1 — §III Unified Dominance Abstraction; IV/V Unified Dominance Graph`; Evaluation=`https://arxiv.org/html/2606.24204v1 — §VI Experiment; Search Performance and Index Construction`; Non-proof=`闭合 two-bound conjunctive predicate 与论文数据集不覆盖任意布尔 filter、动态高 churn 或 distributed index consistency；过滤结构不匹配时回退普通 filtered ANN。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25191: `arXiv:2606.25191v1`; exact-v1 URL=`https://arxiv.org/html/2606.25191v1`; Method=`https://arxiv.org/html/2606.25191v1 — §3 Reasoning-Score Coupling; 4 Candidate Treatments; MADARA`; Evaluation=`https://arxiv.org/html/2606.25191v1 — §5 Experimental Setup; 6 Results; K Cost-Accuracy`; Non-proof=`7B–9B、给定 QA benchmark 与 pilot-derived threshold 不证明高 stakes、长多跳或 retrieval drift；diagnostic 不稳时回退 isolation 或普通 single-pass RAG。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-28387: `arXiv:2606.28387v1`; exact-v1 URL=`https://arxiv.org/html/2606.28387v1`; Method=`https://arxiv.org/html/2606.28387v1 — §3 Schema-First Retrieval; Catalog Objects; Retrieval and Access Control`; Evaluation=`https://arxiv.org/html/2606.28387v1 — §4 Experimental Setup; 5 Results; D Analyses`; Non-proof=`CRUSH4SQL/SEDE/BIRD 与 warehouse catalog quality 不证明跨 dialect、动态权限或低元数据环境；metadata noise/ACL 不确定时回退受限 catalog browse 或人工 schema selection。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25656**：Primary `arXiv:2606.25656v1`；Method `https://arxiv.org/html/2606.25656v1 — §3 Methods; 3.2 Regular RAG; 3.3 GraphRAG; 3.4 Modular and Agentic RAG; 3.5 Context Optimization`；Evaluation `https://arxiv.org/html/2606.25656v1 — §4 Experimental setup; 5 Experimental results`；未证明边界 `https://arxiv.org/html/2606.25656v1 — §6 Conclusions and future work; C Retrieval-Generation Gap`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25674**：Primary `arXiv:2606.25674v1`；Method `https://arxiv.org/html/2606.25674v1 — §3 Method; 3.2 Low-bit Embedding Backbone; 3.5 Multi-precision Embedding Quantization`；Evaluation `https://arxiv.org/html/2606.25674v1 — §4 Experiments; 4.1 Experimental Setup; B Evaluation Details`；未证明边界 `https://arxiv.org/html/2606.25674v1 — §4.4 Analysis; task-type sensitivity to quantization`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26439**：Primary `arXiv:2606.26439v1`；Method `https://arxiv.org/html/2606.26439v1 — §TileMaxSim IO-aware GPU MaxSim scoring; dimension tiling and fused product quantization`；Evaluation `https://arxiv.org/html/2606.26439v1 — §GPU retrieval throughput, latency and quality evaluation`；未证明边界 `https://arxiv.org/html/2606.26439v1 — §Evaluated MaxSim layouts and GPUs only; index update and distributed consistency are not proved`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26441**：Primary `arXiv:2606.26441v1`；Method `https://arxiv.org/html/2606.26441v1 — §GPUSparse learned sparse retrieval with parallel inverted indices`；Evaluation `https://arxiv.org/html/2606.26441v1 — §Retrieval quality, latency and GPU scaling experiments`；未证明边界 `https://arxiv.org/html/2606.26441v1 — §Static benchmark indexes do not prove high-churn update cost, multi-tenant isolation or cross-node scaling`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29151`；Method `https://arxiv.org/html/2606.29151v1 — §2.2 System Architecture; 4 Logical Planner; 5 Physical Planner`；Evaluation `https://arxiv.org/html/2606.29151v1 — §7 Experiments; 7.1 Experimental Setup`；未证明边界 `https://arxiv.org/html/2606.29151v1 — §6.3 Robustness; G Validation Set Noise`。

Review note：`SF-2026-ARXIV-2606-29571`；Method `https://arxiv.org/html/2606.29571v1 — §3.4 Geometry measures; 4.3 The cause: a few crowded directions; 4.4 Mechanism and consequences`；Evaluation `https://arxiv.org/html/2606.29571v1 — §3.1 Encoders; 3.3 Datasets; 3.5 Scoring`；未证明边界 `https://arxiv.org/html/2606.29571v1 — §6 Limitations`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-CROWDED-EMBEDDING-EXTERNALITY:start -->
- `SF-CROWDED-EMBEDDING-EXTERNALITY` — Daily `2026-06-02`；primary `arXiv:2606.28343v1`；Books review `books-review:SF-CROWDED-EMBEDDING-EXTERNALITY`。

  **已吸收的语义增量：** 把 corpus population density 与 cross-tenant crowding 作为共享 index failure mode 和 release monitor。
<!-- daily-books-trace:SF-CROWDED-EMBEDDING-EXTERNALITY:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08950:start -->
- `SF-2026-ARXIV-2606-08950` — Daily `2026-06-09`；primary `arXiv:2606.08950v1`；Books review `books-review:SF-2026-ARXIV-2606-08950`。

  **已吸收的语义增量：** 向量数据库的 insertion、indexing、query 与 mixed read/write 生命周期必须同 storage hierarchy、broadcast-gather 与 partitioning 一起评估；增加 core/node 可因协调瓶颈反向降低吞吐。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08950:end -->


<!-- daily-books-trace:SF-2026-ARXIV-2606-15179:start -->
- `SF-2026-ARXIV-2606-15179` — Daily `2026-06-14`；primary `arXiv:2606.15179v1`；Books review `books-review:SF-2026-ARXIV-2606-15179`。

  **已吸收的语义增量：** document-isolated device-cloud RAG 应用 waiting debt 与 certificate-guided minimal supplement 异步聚合证据，而不是等待所有设备或一次性上传全文。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15179:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-28361:start -->
- `SF-2026-ARXIV-2606-28361` — Daily `2026-06-14`；primary `arXiv:2606.28361v1`；Books review `books-review:SF-2026-ARXIV-2606-28361`。

  **已吸收的语义增量：** 多轮 RAG 服务可把历史文档/推理改成 append-only conclusion chain，并在一次调用中联合生成 reasoning 与 conclusion，使跨轮输入从近 O(N²) 降为 O(N)。
<!-- daily-books-trace:SF-2026-ARXIV-2606-28361:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-28365:start -->
- `SF-2026-ARXIV-2606-28365` — Daily `2026-06-15`；primary `arXiv:2606.28365v1`；Books review `books-review:SF-2026-ARXIV-2606-28365`。

  **已吸收的语义增量：** RAG ingestion enrichment应作为budgeted multi-index portfolio，分开agentic template proposal、atomic view-model evaluation与confidence-aware promotion
<!-- daily-books-trace:SF-2026-ARXIV-2606-28365:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-28367:start -->
- `SF-2026-ARXIV-2606-28367` — Daily `2026-06-15`；primary `arXiv:2606.28367v1`；Books review `books-review:SF-2026-ARXIV-2606-28367`。

  **已吸收的语义增量：** retrieval enhancement必须在固定strong reranker后做incremental ablation，并按heterogeneous source分别校准acceptance threshold
<!-- daily-books-trace:SF-2026-ARXIV-2606-28367:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16341:start -->
- `SF-2026-ARXIV-2606-16341` — Daily `2026-06-16`；primary `arXiv:2606.16341v1`；Books review `books-review:SF-2026-ARXIV-2606-16341`。

  **已吸收的语义增量：** filtered ANN planner 应把 selectivity error 到 plan regret 的 phase boundary 作为切换条件，而不是用单一 pre/post/in-filter 规则
<!-- daily-books-trace:SF-2026-ARXIV-2606-16341:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16494:start -->
- `SF-2026-ARXIV-2606-16494` — Daily `2026-06-16`；primary `arXiv:2606.16494v1`；Books review `books-review:SF-2026-ARXIV-2606-16494`。

  **已吸收的语义增量：** 多模态 RAG 的 primacy bias 会让后到 evidence 被系统性忽略；evaluation 与 assembly 必须扰动 evidence order 并保留位置归因
<!-- daily-books-trace:SF-2026-ARXIV-2606-16494:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17467:start -->
- `SF-2026-ARXIV-2606-17467` — Daily `2026-06-17`；primary `arXiv:2606.17467v1`；Books review `books-review:SF-2026-ARXIV-2606-17467`。

  **已吸收的语义增量：** 专业文档 RAG 的 ingestion 需保留 provenance-aware sanitization、可追溯 rejection 与 utility check，不能把 paraphrase 或通用文本过滤当作 indirect-instruction 清除证明。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17467:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18037:start -->
- `SF-2026-ARXIV-2606-18037` — Daily `2026-06-17`；primary `arXiv:2606.18037v1`；Books review `books-review:SF-2026-ARXIV-2606-18037`。

  **已吸收的语义增量：** MCP factuality verifier 必须把 source block identity、claim-to-source relation 与 final answer 分开评分；高 block F1 不能证明 provenance relation正确。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18037:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18310:start -->
- `SF-2026-ARXIV-2606-18310` — Daily `2026-06-17`；primary `arXiv:2606.18310v1`；Books review `books-review:SF-2026-ARXIV-2606-18310`。

  **已吸收的语义增量：** RAG threat model 需覆盖 retriever parameter editing：攻击者可改变 ranking 而不改 corpus；index/model revision、anchor repair 与 retrieval regression 必须同 lifecycle 验证。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18310:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18497:start -->
- `SF-2026-ARXIV-2606-18497` — Daily `2026-06-17`；primary `arXiv:2606.18497v1`；Books review `books-review:SF-2026-ARXIV-2606-18497`。

  **已吸收的语义增量：** Vector DB deletion 必须追踪 source→embedding→HNSW node→backup/replica 的物理生命周期；soft-delete tombstone 不是擦除，需 epoch key rotation与 signed deletion proof。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18497:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19692:start -->
- `SF-2026-ARXIV-2606-19692` — Daily `2026-06-19`；primary `arXiv:2606.19692v1`；Books review `books-review:SF-2026-ARXIV-2606-19692`。

  **已吸收的语义增量：** `When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems` 路由到 `AGENT-RAG`：旧的周期 reverse-kNN 扫描在毒文档入库后才处置；该工作把 sentinel hub-score、冻结阈值和 quarantine 决策放进写路径，由索引入口拥有 admit/reject 控制，阈值缓冲按写增量维护。代价是 sentinel/encoder 漂移和自然 hub 误报；tight-domain、删除最坏路径或监测盲区仍由 provenance 审核与周期扫描兜底。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19692:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19719:start -->
- `SF-2026-ARXIV-2606-19719` — Daily `2026-06-19`；primary `arXiv:2606.19719v1`；Books review `books-review:SF-2026-ARXIV-2606-19719`。

  **已吸收的语义增量：** `Closing the Calibration Gap in Semantic Caching` 路由到 `AGENT-RAG`：语义缓存的发布标准从 PR-AUC 排序改为 threshold-aware P-CHR 曲线与 CRR：cache owner 保存 score/threshold/命中预算，evaluation 将 ranking quality 分解为可校准差距和由正例率决定的结构差距，再决定是否上线 retriever/reranker。post-hoc calibration 仅是共存修复，不能替代重新训练或生产域阈值重估。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19719:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21777:start -->
- `SF-2026-ARXIV-2606-21777` — Daily `2026-06-20`；primary `arXiv:2606.21777v1`；Books review `books-review:SF-2026-ARXIV-2606-21777`。

  **已吸收的语义增量：** retrieval verifier telemetry 应保存 evidence coverage、置信校准与 abstention，verifier 分数不能直接改写知识库
<!-- daily-books-trace:SF-2026-ARXIV-2606-21777:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16973:start -->
- `SF-2026-ARXIV-2607-16973` — Daily `2026-07-19`；primary `arXiv:2607.16973v1`；Books review `books-review:SF-2026-ARXIV-2607-16973`。

  **已吸收的语义增量：** 新增证据边界：Tenant allowlists are applied inside the retrieval kernel before scoring/admission, avoiding post-filter over-fetch; a separate codebook-oblivious scalar-quantization branch removes corpus-trained codebooks but does not eliminate vector leakage. 该 delta 已进入 `books/part-07-agent/76-rag.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16973:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-01311:start -->
- `SF-2026-ARXIV-2608-01311` — Daily `2026-08-03`；primary `arXiv:2608.01311v1`；Books review `books-review:SF-2026-ARXIV-2608-01311`。

  **已吸收的语义增量：** RH-RAG 把隐私约束下的长文生成拆为全局 outline、带 bounded coherence memory 的分段写作，以及由 NLI/attestation 驱动的事实检查与返工。文学、金融与法律实验说明该 pipeline 在作者的 7B–8B 本地模型设置中可改善 grounding/coherence；公开文本可能已进入预训练语料，通用 NLI checker 会增加误拒与 revision 成本，因此不等于对新颖私密文档的独立保证。
<!-- daily-books-trace:SF-2026-ARXIV-2608-01311:end -->

- `SF-2026-ARXIV-2604-20849` — [SPIRE v1 PDF](https://arxiv.org/pdf/2604.20849v1)，§2.1–2.3/§3.1–3.2、§4.1–4.3/Table1：path-set身份与global/local view分开，延迟展开和同文结构合并；helpful比例非答案准确，encoder/filter及粒度成本分开。source→owner及实际正文与相邻衔接写后非作者root复核通过；未复现实验，不采用HTML后发日期口径或跨修订稳定保证。[同作者 Zenodo 先行公开](https://zenodo.org/records/19441410)已反驳原04/24 Daily first-public 归属，故不沿用该日6分与本窗整合计数；真实日报 owner 待精确时间/版本核定，见 `papers/2026/04/_sources/daily-20260424/V3_ROOT_SPIRE_FIRST_PUBLIC_CORRECTION.md`。

<!-- daily-books-trace:SF-2026-RETRIEVALROUTER:start -->
- `SF-2026-RETRIEVALROUTER` — Daily `2026-08-27`；primary `arXiv:2608.25625v1`；Books review `books-review:SF-2026-RETRIEVALROUTER`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：冻结 Qwen3-0.6B 主体并以 LoRA query encoder 和 soft reward target，在五类 pipeline 间按 nDCG/latency 权衡逐 query 路由；并保留边界：需同时维护约 40GB 多索引；query-only 看不到 document layout，未验证跨域 routing，oracle gap 仍大。 相邻章节对读：books/part-07-agent/75-context.md#L72;books/part-07-agent/77-memory.md#L113。Context 拥有 assembly，Memory 拥有长期 read/write；逐 query retrieval pipeline selection 属于 RAG。
<!-- daily-books-trace:SF-2026-RETRIEVALROUTER:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2605-01302:start -->
- `SF-2026-ARXIV-2605-01302` — Daily `2026-05-05`；primary `arXiv:2605.01302v1`；Books review `books-review:SF-2026-ARXIV-2605-01302`。

  **写回边界：** 在 relevance 与 sufficiency 之间加入 query-robustness sensor；critic 只能暴露迎合错误前提的风险，不能替代原始 evidence、事实判断或 answer gate。作者结果不提供跨 corpus 的事实概率或固定阈值。
<!-- daily-books-trace:SF-2026-ARXIV-2605-01302:end -->

- `SF-2026-ARXIV-2603-04384`：[AgentIR exact-v1](https://arxiv.org/html/2603.04384v1) §3.2–3.3、§4、§5 Tables 2–3；采用当前 reasoning+query 与检索适配的互补输入机制，保留完整历史反例、trace 可得性和局部评价边界；未复现实验。Daily 2026-03-06，实际写后非作者 root 复核通过。

- `SF-2026-ARXIV-2602-00238` — Daily `2026-02-04`；[DIVERGE exact-v1](https://arxiv.org/html/2602.00238v1) §3–7及B/C。6分设计反证深入，只采用输入检索与同query输出多样性分权；claim抽取/embedding阈值、质量judge与额外搜索预算均有限。主文100query与C.1的200subset不合并，GPT5-mini质量4.342低于baseline4.578，不照录全部配置仅微降约.04；未有matched额外call对照，不授单组件因果、真实观点数或效率保证。未复现实验；root必要原源/当前owner写前通过，root实际正文及前后交接写后通过，日级Gate通过。

- `SF-2026-ARXIV-2512-24268` — Daily `2026-01-02`；[RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation exact-v1](https://arxiv.org/html/2512.24268v1) §3.1–3.2、§4 ASR/SR、§6 single-poison mix假设与§7。6分保证边界/gap深入，仅采用embed-before-mix、top-p多候选非决策多数保证、mask probe支持集与成本；retrieval非answer安全，贴题假事实非truth detector，不授所有攻击免疫或实时SLO。未运行代码；root必要原源/owner通过，实际正文/前后邻接及末注写后经root非作者复核通过。

- `SF-2026-ARXIV-2512-23836` — Daily `2026-01-02`；[Large Language Models Are Poor at Signaling Their Ignorance When Given Irrelevant Context exact-v1](https://arxiv.org/html/2512.23836v1) §2、§3、Figures 5–7。6分具体gap深入，仅采用顺序负窗口暴露与 first-positive 条件人口的分账：BM25/Wikipedia、KILT 三个 QA 数据集及单 Gemini 1.5 Pro 的有限证据，不授全模型幻觉率、独立错误假设或提示必然修复。原文 token 口径不合并为普遍成本优势；未复现实验。root 必要原源/owner 写前通过，实际正文/前后邻接及末注写后经root非作者复核通过。

- `SF-2026-ARXIV-2601-05503` — Daily `2026-01-13`；[Over-Searching exact-v1](https://arxiv.org/html/2601.05503v1) §3–5.4。原评分保持，具体owner差额深入；采用可答/应abstain双人口及intent未定先clarify；fixed TPC/judge与few-shot过拒绝反侧。未运行代码或复现实验；root实际必要源/现owner写前核通过并授窄锁；root已实际核正文/前后邻接及末注，非作者POST通过。

- `SF-2026-ARXIV-2601-09028` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09028v1) §3.2–3.4/4.2/4.4、Table2、5.3–5.5与AppD。6分quality-proxy进入decoder的具体gap深入，只采用显式指标的内部消费接口/lineage；Eq2/3与AppD维度/负值monotonic问题不采精确recipe，proxy非truth，在线ranker/QPP与训练成本、聚合/noisytraining未孤立和普通packing退路邻近。root必要原源/owner写前通过，root实际两段、邻接与末注POST通过，锁释放；未运行artifact或复现。

- `SF-2026-ARXIV-2601-09159` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09159v1) §3.1–3.3/4、Table1–2、ANN/CSR 与必要配置。6分partition leafcode/collision metric具体gap深入；不采附录entropy/bit independence/correlation证明，保留base encoder、建树/映射成本和质量反侧。root必要原源/owner写前通过，root实际两段/邻接及末注非作者POST通过，锁释放；未运行artifact或复现。

- `SF-2026-ARXIV-2602-06526` — Daily `2026-02-10`；[DREAM/BRIDGE exact-v1](https://arxiv.org/html/2602.06526v1) §3.2/4.1–4.3/5.2、AppI及必要B/E/F/H/J/K。6分评价反证差额深入，仅采用 judged pool/qrel/Unknown 的评价身份与未标 top-k 补核后复验排名/归一分母，不授自动标签准确、未来检索池无偏或参数知识因果归因。25检索池、三LLM预过滤、人审残余偏差及成本邻近；标签变化不是系统性能改善。未运行代码或复现实验；root必要原源/具体owner写前通过，root实际两段、前后邻接与末注非作者POST通过，锁释放；不授日级Gate。

- `SF-2026-ARXIV-2602-09517` — Daily `2026-02-12`；[SAKE exact-v1](https://arxiv.org/html/2602.09517v1) §3–6、Tables1–3与局部位置/repeat/stack-only反侧。2+2+2=6，具体reader双视图差额深入；保留交错history，副本在旧reasoning前编码，非retriever metric、删历史或truth认证。GAIA/Hotpot退步、token成本与KV复用仅系统推断近正文；hardware/precision/总E2E cost未披露，未核实现或复现。独立reviewer必要source、root具体owner写前通过，实际正文/邻接与末注经root实际非作者POST通过、窄锁释放；不授日级Gate。

- `SF-2026-ARXIV-2602-09616` — Daily `2026-02-12`；[Argus exact-v1](https://arxiv.org/html/2602.09616v1) §3.2/4/5/7、Tables1–2与D.2–3。2+2+2=6，具体索引前风险探针接口差额深入，只采用固定retriever/KG竞争人口→entity选择→额外view，RPS非校准失败概率/外证真值。Jina合成退步、等膨胀选择未控与新增成本近正文；未核实现/复现。root必要source/owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；非日级Gate。

- `SF-2026-ARXIV-2602-09229` — Daily `2026-02-12`；[Embedding Magnitude exact-v1](https://arxiv.org/html/2602.09229v1) §3/4.1/5/6与B。2+1+3=6，具体训练/推理norm分责差额深入，fixed query正scale不改rank但训练温度/梯度不同、docnorm可改rank；scratch/FT及Dot仍对称反侧近正文。不授普适task-symmetry律/免费quality，未复现。root必要source/owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；非日级Gate。

- `SF-2026-ARXIV-2602-10380` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10380v1) §3–5 aligned/repeated/no-label对照及预算反侧；只采oracle granularity×label条件，不采冲突delta、无泄漏或abstention因果。root必要源与实际owner PRE通过，具体差额受影响深入；实际正文/完整邻接与末注已经root非作者实际POST通过，窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2602-15156` — Daily `2026-02-19`；[Panini exact-v1](https://arxiv.org/html/2602.15156v1) §2–4/6、AppendixG/Table19。2+2+2=6，RICR QA/答案实体驱动的读写接口差额受影响深入；GSW表示不当本篇首创，减少answer-context不授总成本下降，100.1min/3.3s对dense1.9min/1.3s反侧近正文。派生QA/链score不授truth或证据充分；开放模型边缺失、叙事/多模态、更新删除成本保留。root必要原源/实际76及75/77邻接PRE通过并授窄锁；root已实际顺读正文L110–133及末注，非作者POST通过，窄锁释放；未核代码或复现，未授日级Gate。

- `SF-2026-ARXIV-2602-12727` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12727v1) 必要方法/关键控制/直接限制；2+1+2=5，具体owner差额定点深入。仅采用正文条件机制；相关理论/效果强保证隔离，成本与回退近正文。root必要原源/actualowner PRE通过并授窄锁；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接/末注POST通过，窄锁释放，未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-13179` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.13179v1) 必要方法、关键对照与直接限制；2+1+2=5，实际 owner 差额深入。视觉query repair identity/语义与真实tool-v-oracle、retriever-v-reader分账；Nomic pair数值隔离。root 必要原源/owner PRE通过并授窄锁，作者完整邻接已顺读，root非作者实际正文/完整邻接/末注POST通过，窄锁释放；未运行artifact或复现，非日级Gate。

- `SF-2026-ARXIV-2602-16299` — Daily `2026-02-20`；[MICE exact-v1](https://arxiv.org/html/2602.16299v1) §3/4.1/4.3/4.4/5。2+1+2=5，单向 query 读 frozen document 与 query self-attention 差额深入；mask需重训、跨域负侧、减少层/参数共因、未full indexing、缓存刷新成本保留。不授完整服务SLO。root必要原源/actual owner PRE通过；作者及root实际正文/完整邻接/自身末注顺读，非作者POST通过，窄锁释放；未核代码或复现，非日级验收。

- `SF-2026-ARXIV-2602-16974` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.16974v1) §3–4.5、Table4必要人口及正例；2+2+2=6，pre/post编码chunk边界与竞争人口差额深入，仅平均/指定配置反转，不授全部chunk退步或窗口/评价单位同一；反侧、额外成本与原方案回退近正文。root必要原源/actual owner PRE通过；作者正文/完整邻接及末注已顺读，root非作者实际正文/完整邻接及末注POST通过，窄锁释放；未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16609` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16609v1) §2/3.1/3.2 Table3/4。2+1+2=5，dense→late-interaction训练阶段与prompt×微调强度接口差额深入；额外scale/训练预算混杂，不采多向量预训练唯一必要、99.4%生命周期或隐式query expansion因果；阶段/长度/索引与旧路线成本近正文。root必要原源/actual owner PRE通过；作者及root非作者实际正文/完整邻接/自身末注已顺读，POST通过，锁释放，未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-18425` — Daily `2026-02-24`；[RVR exact-v1](https://arxiv.org/html/2602.18425v1) §3/Algorithm1、§5.2/6.1–6.6。2+2+2=6，query+relevance-selected context→missing-evidence retriever训练接口具体差额深入；最终集补未全部verify文档、goldsubstring非语义oracle、错误冗余plateau、budget/domain与双训练/index/verification成本近正文，不授完整证据或free迭代。root必要source/actual owner PRE通过并授窄锁；作者实际正文/完整邻接及末注顺读、root非作者实际正文/完整邻接/自身末注POST通过，锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16136` — Daily `2026-02-20`；[Retrieval Collapse exact-v1](https://arxiv.org/html/2602.16136v1) §3.2–3.3、§4–5 与直接限制。2+2+2=6，corpus/exposure/citation/answer 四人口评价接口差额深入，非理论突破；origin 非 truth、CCR 非隐藏 use，two scenarios 非真实时序证明，同 family/独立 judge 权限与额外审计费用近正文。不授已实现防御或真实生态定律。root 必要源/实际 owner PRE 通过；root非作者实际正文/完整邻接/自身末注 POST通过，窄锁释放；未运行 artifact 或复现。

- `SF-2026-ARXIV-2602-16375` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16375v1) §3、§4/Tables2/5、REINFORCE/scale必要反侧。2+1+2=5，content/独立停止长度与生成标识预算接口差额深入；频率weighted非catalog平均，固定token更多event非同event因果，collision唯一ID/冷尾/训练成本及旧标识回退近正文。root必要原源/actual owner PRE通过并授窄锁；作者正文/完整邻接实际顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-17215` — Daily `2026-02-21`；[NotebookRAG exact-v1](https://arxiv.org/html/2602.17215v1) §4.2.1–4.2.4/Table1、§4.3–4.4、§6.5/7。2+1+2=5，executable dependency-closure 检索单位的具体owner缺口深入；非线性log/未知mutation、同840对used-column标注与重跑/调试费用近文，不授完整静态语义、安全沙箱、运行正确即数据真值或公平总体收益。root必要原源/actual owner PRE通过并授自身窄锁；实际正文及邻接已由作者顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未运行代码或复现，非日级验收。

- `SF-2026-ARXIV-2602-17366` — Daily `2026-02-21`；[RPDR exact-v1](https://arxiv.org/html/2602.17366v1) Eq8/9、§4.2–4.3、Appendix B/§8。2+1+2=5，具体owner差额深入；训练query往返selector区分index增强；matched random/频繁切片反退、singlefact与inverse/finetune费用近正文。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-18734` — Daily `2026-02-25`；[exact-v1](https://arxiv.org/html/2602.18734v1) §3.3/4.1/4.3–4.4、Algorithm1。2+1+2=5；自更新 reader 的历史成功标签与 K1→K3/7 消费差额深入，consumer/exposure 人口、初始标签和双模块成本近文，不授因果效用或严格 GRPO。root实际必要原源/owner PRE通过授两段窄锁；作者实际正文/完整邻接/自身末注顺读及限定diff-check通过，root 非作者实际正文、完整邻接与自身末注 POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-17654` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17654v1) §3/4.3–4.4、同backbone对照及分级标注/反侧。2+1+2=5，partial grade在不同pair正/负角色与保原negative缺口深入，不授cardinal utility/score校准；同judge/未见query人口、增广反退和训练/索引成本近文。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-21477` — Daily `2026-02-27`；[Pancake exact-v1](https://arxiv.org/html/2602.21477v1) §4.3–4.4/§5，blocks83–101/104–141。2+2+3=7，各scope coarse图的portal联结与staticcluster agent-specific fine IDs/单payload差额深入；scope非ACL、heuristic earlyexit非recall、双驻留/split成本及独立索引回退近文，不用Eq88概率或26×生产倍数。root必要源/actual owner PRE通过授一段窄锁；作者正文/完整邻接/自身末注已实际顺读，root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放，未核代码或复现，非日级Gate。

- `SF-2026-ARXIV-2602-22427` — Daily `2026-02-28`；[HubScan exact-v1](https://arxiv.org/html/2602.22427v1) §3–5/blocks49–90、112–123、141–186。2+1+2=5，alert-budget crowding实际差额深入；AUC与有限top-H、自然hub与恶意truth分开，域代表性/污染与扫描费用近文。root必要原源/actual owner PRE通过并授单段及自身末注窄锁；作者实际正文及完整邻接顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级Gate。
