# 04557 Cartridges at Scale：首次必要 / 正式6分 / actual Ch45两段PRE

最新行政事实：reader R103–104唯一actualPOST已实际采用，真实整合生效/指定窄位释放，新增I21＋旧Kimi1合22；下述A103待POST为历史过程，不第三技术。

A103过程：reader R101–102首次必要/正式6分/actual Ch45小gap与原两段PRE逐字通过已实际采用；root fresh完整双锚新窄授后已真实SAVE/完整自读＋本人true-H2注，仅待唯一非writer actualPOST，未预I22/DAY。既成21I保持；本项AB/Jun04联合日期按reader R89–91有效原件复用，不第三GET/校准。下列准备态是本SAVE前过程，不再是当前待办。

## 身份与真正读取域

精确 `2606.04557v1`，题名 *Cartridges at Scale: Training Modular KV Caches over Large Document Collections*。官方abs/notice/唯一v1与exact DOI已R89–91独核，当前无撤回提示；原字段见SUP_TITLE_STOP_BATCH4_20261025.md。Submitted-v1 `2026-06-03T07:42:55Z`；精确DOI `10.48550/arxiv.2606.04557` 为findable/arxiv.content，registered `2026-06-04T02:01:20.000Z`。最早公告界Jun04 08:00BJT、最晚Jun04 10:01:20BJT完整同日，不冒实际公开时刻/全球首稿，不混Updated-v1。

官方必要HTML `https://arxiv.org/html/2606.04557v1` GET200/419584bytes，原件SUP_2606.04557v1_20261025.html，SHA256 `a8092cba1fd6ea0ac803f8ea8bd694cfc7c33620f37b150b6d9fd0693c8f0c0b`。实际文本读§1–7、§2.1–2.5/Eq1–2、§3–4/T1–4/F1/3/4说明、§5成本/Grouping、完整Limitations/Potential Risks；A/T5及inference、B per-cartridge LR、C self-study关键对照/T6、F retrieval/indexing/T9–10、G recall定义及相关T11–14切片、J/T16–17质量分析。不是全附录/完整refs/全部prompt或图像素，未执行公开代码/复现/生产请求；支持和直接反侧足够停止，无需扩全附件。

定点检索exact family/题名/Cartridges未发现同事件已成必要/owner有效链；不以无marker直接认定gap。旧Cartridge作为本文背景不重新计首次发明/另建候选；shared wrapper与query-side LoRA是不同受训对象，具体比较如下。

## 必要机制、关键对照与直接反侧

§2背景：冻结base，文档可学习Z是各层KV向量，不更新model weights。teacher在文档chunk上下文产生回答分布，student仅见cartridge prefix，按token KL蒸馏；这是受训近似状态而非真实文档Prefill KV恒等。GPT-OSS120B生成问题而回答/目标log-probs由目标Qwen3-8B产生；不把问答合成teacher更换与batching收益拆成已隔离因果。

§2.1 Eq1–2：以P_iso只见相关Z*，否则加从pool取样distractors；packed各样本以不同attention mask读子集，所有active cartridge可获梯度。GPU只驻B≤N，数据也由resident carts抽；每R步以phi轮换CPU/disk状态、优先训练步少的cart，offloaded期间不获梯度。query position按当步active KV总token数重算offset。§2.2按每cart实际s步做warmup、4档bucket维持fused Adam，而非只看global step。它联动组合训练分布/驻留状态/局部优化时钟，不把成熟KL、Adam、offload分别计创新；“uniform coverage”是作者意图，不等未测故障恢复/公平保证。

T3 LongHealth20 docs/每cart约585tokens/80epochs、3runs均值±std：独训P_iso1 oracle73.6±.4而Full20混合26.0±3.1；联合P_iso.75且kmax10，oracle78.9±1.0/Full56.4±.6；增到20为79.0±1.4/77.8±.6。这里是特定训练混合规模与组合评价人口，不签任意N/任意新doc或组合外推；frozen model“collapse”是任务表现崩塌不是weights被训练坏。shuffle与原序同77.8仅有限经验对照，不证普遍permutation equivariance。随机子集有/无相关doc准确率差不证知识严格隔离、access control或可靠删除。

A/T5：五个英文任务、同一Qwen3-8B；BF16 weights/FP32 Adam，H200/B200集群（完整GPU数/端到端墙钟/IO/故障恢复未披露），T3另注明H100且20 carts无需offload。默认B20/R10/phi.5/P_iso.75/kmax10、每cart warmup20/global200、80epochs/globalbatch128/packing8192，0.1 LongHealth/.05其他LR，末值.02。B的slow decay再加warmup/优先轮换是组合改变，不将54.8→59→60.8唯一归单项；训练/搜索/状态交换全计费。

T2 oracle知道正确doc不代现实retriever：FinQA66.8 full context→62.7@2x/23.0@100x，LongHealth87.4→77.3@100x，极压缩可显著退化；不把跨数据/不同压缩容量的monolithic比较合成普遍同预算10–31点保证。F/G TitanEmbedv2/1024维cosine、chunk128/256/512/1024、10%overlap、k1/3/5/10；top10一次取得后切片，chunk→doc去重，kchunks不等kcartridges。16grid最优选择未充分闭held-out调参隔离；QASPER未进retrieval对照。FinQA多k可反退、TechQA text73.2优于cart71.0，未召回/失真均不可由KV压缩自行恢复。

C/T6同时更换question model/batching/length sampling，非20倍端到端保证。J九份FinQA抽688非年份数字：41%直接有据/37%推导/13%round/9%fabricated；非原文59%不能全当幻觉。正确n15/错n13及25%number coverage阈值只是描述性关联，不是必要充分质量证书；数值覆盖也不解决entity binding。缓存训练照搬错误或私密内容仍有治理风险。

Limitations当前仅prefix/single-turn。中途插新cartridge改变history token位置需完整recompute，不签在线无损插入/任意更新；仅单model/English不授跨family/低资源语言。§5抽象prefill FLOPs不等完整请求成本：retrieval、加载、query/decode读取、合成/训练、离线state/moments及交换均付费。未核生产SLO或崩溃后恢复/事务一致性；不写零推理成本/无损组合/安全隔离。

## 正式评分与actual owner差额

Design Delta2＋System Reach2＋Durability2＝6：具体增量为可训练KV状态的组合可见性与resident-pool/每对象更新时钟联动，跨训练状态和推理复用边界；改变“独训后直接拼接即可”及只按全局步调度状态的设计判断。不是压缩率宣传/模型名/成熟优化原则/可映owner加分。已确认长期小gap，深入受影响域，未机械要求全附件。

唯一owner `INFER-KV-CACHE` Ch45。实际读既有prefix身份/COW/causal-repair及当前位置非prefix复用段、shared Header/Trailer wrapper完整两段、下侧关系闭包完整段，以及ATTUNER固定producer-KV/query-projection LoRA consumer适配两段；邻Ch44/46交接开篇与ROADMAP定位有效。现文已覆盖位置/上下文差额、共享wrapper离线蒸馏与消费者适配、离线成本，不重复它们。尚无每文档Z通过distractor可见性联合训练、与驻留轮换/局部更新clock绑定这一具体状态生产接口，故非“同主题已有”NC，亦非无marker即I。

拟两段插shared-wrapper完整成本段之后/关系闭包完整段之前，仅解释训练state与组合人口。支持与直接反侧已足，不挖旧family全史。尚未PRE/授写/实际整合。

### 完整直接上锚

> [有限模型与任务对照](https://arxiv.org/html/2604.13226v1)保留了 Qwen 在 MusiQue 相对 Full Recompute 的质量差距；单域 Hotpot 与跨域训练结果不可混为同一条件。线上指标包含 CPU→GPU cache 传输，却排除了离线训练/预缓存，额外 wrapper row 也占存储与读取预算。它更适合文档反复复用、近似质量可验收的负载；模型或 wrapper 升级须失效重建，跨域质量不足或因果依赖较强时，选择性 repair 或完整 Prefill 继续成立，不能采用“免重算”作为全部成本为零的承诺。

### 完整直接下锚

> 还可在离线编码前声明有限的关系闭包，而不是先完全独立编码、线上再猜哪些 row 需要修复。对于有显式 primary/foreign-key 关系的表集合，可在已核为 acyclic 的依赖图上按拓扑顺序联合编码相关表，再把 table packet 对齐位置交给线上组合；FK 不天然形成 DAG，也不涵盖任意 query 的语义依赖，去除再补 position 更不恢复各层缺失的 full-context hidden state。[有限 Text-to-SQL 对照](https://arxiv.org/html/2601.08743v1)仍有 BIRD 质量损失，training-free 配置损失更大，全 test 累计 TTFT 不能当单请求 P99。缓存身份须绑定关系/schema、model、mask-training 与位置协议，离线 precompute、调优、重排、传输和重建一并计费；依赖缺边、出现循环、改版或质量不达标时扩大联合编码边界，必要时完整 Prefill，不能让 schema relation 自证完整因果闭包。<!-- source-family:SF-2026-ARXIV-2601-08743 -->

## 拟两段最小PRE（R101逐字通过；A103已按原稿真实SAVE，待唯一POST）

若允许每份文档的KV本身成为可学习前缀，组合能力还应在状态生产时训练，而不只在读出端适配。冻结base、仅优化各文档KV时，可让训练样本有时只见相关前缀，有时经attention mask同时看见相关与干扰前缀，按带原文上下文的teacher分布蒸馏；这不是重建原文逐token的exact KV。[一项多前缀训练分支](https://arxiv.org/html/2606.04557v1)把这种可见性分布与GPU驻留池联动：只从驻留文档采样，轮换CPU/磁盘状态，按每份前缀实际收到的更新数warmup，而不是用全局step假定全部状态同龄；query位置offset也随当步active前缀的KV总长度重算。缓存artifact因此须绑定base、文档与合成目标、组合mask/规模、训练及每对象优化状态、位置协议，不能把独立训练完毕等同组合已验收。

组合训练的覆盖范围仍是边界：受限20文档对照中，独训前缀在全量混合时准确率明显下降，扩大训练可见组合后改善，却不证明任意集合可拼、顺序不变或知识隔离。检索漏召回、蒸馏遗漏/错误以及数值与实体绑定继续限制回答；较少prompt tokens不免检索、合成/训练、optimizer状态、轮换传输和query/decode读取费用。现有证据仅单一8B模型与英文任务、prefix式单轮读取，中途插入新前缀会使历史位置失效并需重算。应同时验oracle与真实检索、训练内外组合和完整质量/成本；文档或模型改版、组合外推或质量不合时，重训/重建并保留原文RAG或完整Prefill，不以“可插拔”签发无损更新、可靠删除或访问隔离。<!-- source-family:SF-2026-ARXIV-2606-04557 -->

## 当前精确停止

单篇必要/正式6分/actual Ch45小gap与双锚原两段已ready供唯一reader首次核，不等剩余五篇Batch4和EvalStop/Multi-SPIN，不堆未POST稿。本项无Books新授权/SAVE/注/POST/I；总21I保持。04032跨日Hold与DistIL中心争议保原证；剩余必要/有限title stop/六节/DAY仍ordinary，不冒外阻/普通0，不扩月2000/73/706。State/index/他日未改，无stage/commit/push。

保存后实际读回本原两段与完整直接双锚/Report/恢复，限定diff check和本新文件no-index空白核无诊断；V3真实仅本CAS普通Books枚举失败，不改“暂缓”过格式。阶段就绪交root/唯一reader首次必要/score/actualowner/PRE后释放，不等后七/扩附件。

## A103 — 新窄授后真实SAVE/完整selfread，待唯一actualPOST

已实际完整采用R101–102原域/逐字PRE，不第三AB/date/必要。root本轮fresh双锚后仅授本原两段+一条章末本人注；作者只在shared-wrapper完整成本段后/关系闭包完整段前逐字保存上述两段，单独family marker唯一，本人单注在唯一true-H2 Review notes下。真实完整读回新增两段/直接完整上成本段/直接完整下关系闭包段及本人整注；非exact、当步active总KV长度、20doc受限组合与oracle/真实retrieval分责、蒸馏与entity错误、全费、单8B英文单轮中途重算及原文RAG/fullPrefill退路均保留，不授无损/安全隔离。

写前快照 `/private/tmp/cas-0605-save.EmZ5Aw/ch45-before.md`，before SHA256 `e6979f1d9009d5299f3055bdab7b3d0364a7fa0f4e59906943abf1170bc1a1e4`；after `6038bbd461f8193ac765a389733cb773596dae80eb7a821d1432ca121340f846`。仅逆除本原两段及本人单注后整个Ch45字节等写前，literal连文/正文marker/本人注各唯一，trueH2正确；保护原两侧/他注/RedKnot等并发内容。首次patch因生成器多空行拒绝、未修改文件，已定位格式并用原精确双锚重新通过；正文无修句。

README六节已按本项真实SAVE普通态同步，当前仅待唯一非writer actualPOST不预I22，I21保持；V3普通Books枚举继续如实失败，不冒暂缓/改脚本。阶段ready立即交root/唯一reader实际POST释放作者槽，不做另一篇、不第三必要/PRE；State/index/他日未改，无stage/commit/push。
