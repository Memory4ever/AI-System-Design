# CRE-T1 2603.17387：必要 Source / actual owner / 最小 PRE 准备

resume_review17_18，2026-10-11，只03-20补03-19自然日；本次恢复已实际重读AGENTS、研究/Report合同、Sources使用/每日/arXiv、统一Prompt、完整ROADMAP、Books PROJECT/学习/写作约束及本日README/STOP，相关LS只作本日路由。原完整AB/date准入复用本日独核§13、SUP_ADMISSION_BATCH5，原2+2+2=6不变。准备者不自授Source/PRE PASS、safe或DAY；未写Books/Report/LS。

## 1. 精确身份与实际必要读取

[exact-v1 HTML](https://arxiv.org/html/2603.17387v1)实际§3.1–3.2/Eqs1–7 L72–113、§4.1–4.5/Tables1–3 L114–178及结论必要179–181；A1–3 L204–216有说明但HTML缺prompt代码块，因此定点恢复[同v1 PDF](https://arxiv.org/pdf/2603.17387v1)用户页11–13/A1–3（解析L378–464），实际读query/doc instruction与GLM教师prompt，不冒截图/像素检查。当前官方abs已实际完整title/AB/comments/history L9–29，只v1、未见具体撤回/纠错信号；不扩完整版本史、repo或外部teacher dataset，不从Submitted反推公开日。

## 2. 有限支持、必要反侧与采用边界

§3.1由同一训练模型共享query/doc表示空间：query先有限步AR生成中间文本，自动输出特殊embedding token，用其hidden state作向量；doc以独立instruction、原文及末尾token单次forward取向量，不生成同样的文本。因此是query-side线上生成与doc-side离线索引的非对称分支，不是原Ch76 frozen-teacher mapper，也不等query端没有生成费或doc索引永久兼容。具体最大步数、未输出token的fallback与在线终止预算Not Disclosed，不能补成完整服务recipe。

§3.2前两阶段仍有InfoNCE/Triplet，不能照录“contrastive完全不能动态关联”的普遍否定；固定采样/解码策略下生成后向量也可视为输入映射，这只是本材料选择的query-compute路径，不是静态/动态能力定理。第三阶段在同题多路径上用正负文档soft排名和格式reward，排序reward为正样本log软rank的归一化；非空正负集及温度正条件必要，未披露精确负样本/温度/format penalty，不补其可执行配方。排名和结束格式不直接验证中间推导、文档事实或答案支持，也不授权“最优策略/逻辑质量已保证”。

必要PDF A1例的stage1 assistant只有embedding固定后缀，非现成推导trace；stage2指令要求概念关系/上下文及理想目标文档内容，A3教师实际被要求生成假想文档段落，学术/历史类明确允许预测乃至编造具体日期、法律/引文等。保留原“reasoning trajectory”作者命名与这一决定性相反证据，不把训练生成当已经grounded的逻辑链；这不是断言所有训练样本错误。仅采用“生成查询侧假说/描述后取向量”的接口，并独立核召回及原文支持；强grounding/忠实推理宣称不采。

评价为Qwen3-Instruct-4B、MSMARCO 400K与ReasonEmbed 82K、GLM4.5再生成，四A800三阶段20/8/20小时；BRIGHT12子任务nDCG@10，不是reader答案或推理忠实度。Table1单模型平均37.1优于所列直接retriever，但RaDeR+QwenRerank39.2高于37.1，不能写所有组合pipeline均被替代；Leet14.9低于Seed43.2/RaDeR37.3、AoPS11.9低于ReasonIR14.7。Table2stage2→3 Pony36.6→31.9、AoPS最终仍低于stage1；原“剩余11”计数不采。Table3同base整体33.2→37.1，但Econ31.2→30.6，训练数据/教师/目标/线上query预算未完整matching，不据此授GRPO唯一因果或所有对比学习失效。

没有可采用的在线latency/throughput/precision/batch/concurrency/SLO、重复seed/CI、teacher合成/索引构建/搜索与reader总费用；四A800训练工时不能代替全链成本。无独立可验证trace支持时，保留query-only/lexical/hybrid、显式改写/rerank与原文support gate；不因少外部模块授免费或安全。

一次精确重开条件：若要采用grounded reasoning或线上低开销强命题，请提供教师假想段落与可验证原文的对应审计、独立推导/事实评价，以及绑定query decode长度/特殊token终止、文档索引revision和完整执行预算的matched latency/质量比较。有限表示接口不等待该强命题，不为省时改贡献EX/中心全篇或降分。

## 3. actual sole owner 与具体差额

sole `AGENT-RAG`，当前[Ch76](../../../../../books/part-07-agent/76-rag.md)。actual完整75–104与347–383及有关260–310已定点读：89–91已有离线自产响应→冻结LLM/后缀投影、上线不逐token生成；361–363已有当前Agent trace联合编码；365已有在线生成query hidden→mapper→冻结teacher空间/索引。均不能具体承载“retriever自身AR生成→自己的特殊token hidden、共享训练的doc单forward索引、排名proxy与假想teacher不赋事实权威”组合，故不假NC或复制泛生成/检索原则。

Ch75/77开篇实际1–22/1–23分责：本次可见trace由Context接手，派生文本不可升级为持久事实；检索表示/索引版本由RAG sole owner，GRPO通用公式与memory写入策略不在此重复推导。拟在actual365 native-projection完整段后/原367 query-distribution验收前插两最小段，作为另一表示训练与query-compute分支，不覆盖冻结teacher路线、不加结构候选。

## 4. 两段 literal PRE 与静态注（未写，待非准备者裁决）

另一条分支不把在线hidden投影到冻结teacher空间，而让检索模型自己先为query逐token生成一段受预算约束的中间文本，再取结束embedding token的hidden state作查询向量；同一模型对带instruction的原始document只做一次forward，得到可离线建索引的文档向量。这把生成预算放到每次query、把doc端生成留在索引外，不是消除线上生成，也不保证训练模型更新后旧索引兼容。Query原文、中间假说、特殊token终止、模型/指令与document-space revision应共同绑定，未结束或超预算须回到原query路径，不能让更长文本自行获得更高证据权限。<!-- source-family:SF-2026-ARXIV-2603-17387 -->

训练可先用对比式表示损失对齐这两侧，再用同题多条生成路径的文档排序与格式反馈适配query侧；这些信号奖励找到标注文档及可读取的结束位置，不直接证明中间推导真实。[有限检索对照](https://arxiv.org/html/2603.17387v1)的教师提示还生成假想理想文档，某些域允许编造细节，因此应把自产文本当检索提案而非原文事实。受限平均排名提升仍有代码/数学与阶段切片反退，不能授所有contrastive方案失效、无需rerank或全链低成本。教师合成、训练、query decode、doc重编码/索引、搜索与reader均计费；长尾召回、原文支持或预算失配时，保留普通query-only、lexical/hybrid、显式改写/rerank与独立support gate，不由embedding质量替回答签字。<!-- source-family:SF-2026-ARXIV-2603-17387 -->

拟末注：

- `SF-2026-ARXIV-2603-17387` — [CRE-T1 exact-v1](https://arxiv.org/html/2603.17387v1)必要§3–4/Eqs1–7/Tables1–3及同v1 PDF A1–3用户页11–13；只采用query生成后特殊token向量/doc单forward索引的非对称分支与ranking-proxy边界。保假想教师细节/grounding未验、任务反退、索引与完整费用责任；不采最优推理、contrastive普遍失效、全pipeline替代或低开销保证，未核代码/复现。

准备完成后交resume_mar17非准备者一次必要Source/actualowner/原逐字PRE裁决；未获root窄锁前不写Books，准备者不授PASS/safe/DAY。

## 5. 非准备者必要裁决

resume_mar17恢复本20适用合同与Books上下文后，独立实际读exact-v1 §3.1–3.2/Eqs1–7、§4.1–4.3/Tables1–3及必要结论；同v1 PDF A1–3用户页11–13的指令/末token/教师prompt实际解析核对。没有审代码、复现或扩读外部教师数据。actual Ch76完整335–415表示/当前trace/冻结teacher mapper与查询分布前后链，75–104离线自产响应分支、相关260–310索引与表示局部，Ch75/77入口责任实际读取。

有限Source/actual sole差额/两原literal PRE及静态注PASS。相同模型query生成后取自身特殊token与doc单forward取向量，区别于冻结teacher空间的小mapper；排名/格式反馈不验证中间文本事实，教师假想段落与允许编造细节的直接反侧保留。实际T1–3的pipeline及任务/阶段反退、非完整匹配预算和全费用边界与PRE一致；没有把固定参数映射误称所有contrastive算法不能query条件关联。结束失败fallback和revision绑定是本书据接口推导的验收责任，不冒充作者已实现。原6分保留，不假NC/整篇center或贡献EX。拟原365 mapper完整段后/查询分布前两段长期差额成立；root协调唯一窄锁后才能写，当前未POST或计safe/DAY。

## 6. root授权后的 writer 实际落实

root收到§5非准备者裁决后明确授resume_review17_18唯一Ch76本family窄锁。已实际按原两literal PRE逐字写新367/369与静态本人1742；写前现347–388及尾部邻注实际读，写后完整353–391（视觉历史→当前trace→冻结teacher mapper→新两段→query分布/方言→OCR表示）及1736–1742本人/BCAS/LLM2Vec-Gen/NEO邻注顺读，scoped本family两正文+本人注与diff-check0。新旧表示/索引与support gate职责一致，未覆盖旧mapper或改过程身份注。交resume_mar17一次非writer实际POST，writer不自授POST/safe/DAY，不改Report/LS。

## 7. 非 writer 实际 POST

resume_mar17实际顺读Ch76完整353–391及1736–1742本人/BCAS/LLM2Vec-Gen/NEO邻注，逐字回两原PRE/静态source边界及已核v1必要证据，限定check0。冻结teacher mapper与同模型AR生成/自己的doc单forward是共存不同表示空间，未静默替换；生成假想细节、排名/格式不证事实、任务/阶段反退与全费用均近文，后续query dialect/最终support责任衔接准确。正式有限actualPOST PASS，报root接纳释放；不循环修改身份注或授DAY。
