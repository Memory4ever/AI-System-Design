# 首批五项实际 owner 差额 PRE

本页保存各文件具体差额与实际落实位置，不授日级完成。必要源已在 [核心证据](V3_CORE_FIRST_BATCH.md)逐项记录，独立证据复核未变化可复用；安全15323的Ch72整合另已PRE/POST通过，不重复请求。

五项必要源与实际owner PRE均已由root独立通过，实际正文均已写入。Panini正文Ch76 L118/120（完整邻接L110–133）与末注、ToolObserver正文Ch78 L59/61（完整邻接L51–76）与末注，root实际POST通过；两处窄锁释放。COMPOT正文Ch49 L1349/1351、RM bias正文Ch31 L164/166、Sparrow正文Ch48 L946/948及末注均已由root实际顺读完整邻接，非作者POST通过，三窄锁释放。这里行号只定位本次读到的实际文件，后续并行改动可使行号移动。

## Panini — AGENT-RAG / Ch76

实际读Ch76 L95–121持久corpus map、online pipeline与relation-bearing bridge；Ch77 L247–273受预算关联回忆、L355–379写读成本与query-local实体工作区，以及Ch75开头/Ch77交接。现有论点已有预组织、bridge与写读摊销，但未承载本篇RICR把问答对与答案实体当下一跳接口，消除每跳LLM生成这条具体替代分支。新贡献是检索/索引选择，按ROADMAP索引表示owner放Ch76而非把Ch77变为另一份检索实现。建议Ch76 L116之后1–2段：chunk/每跳LLM在叙事自由、写入预算低时合理；事实密集、重复查询可一次写成带source指针的entity-event QA workspace，查询分解后稀疏实体/密集QA召回+重排，答案实体实例化下一跳并beam选链，仅pack链QA。QA和关联是派生证据，不获得事实权威。原始chunks保留回退；writer抽取/链接错误、开放模型漏verb、长叙事/多模态未验、索引更新/删除传播及写入成本近正文。只采用Table19明确写入与读取成本交换，不授普遍更快。

## ToolObserver — AGENT-TOOL-CALLING / Ch78

实际读Ch78 L29–82含ToolContract、源码entryslice和动态声明校验；邻Ch77与Ch79开头。现有description证据分支依赖源码可取得；实际未承载black-box状态依赖从多步task trajectory修订文档，以及训练gold的offline和无gold的online边界。建议L57后1–2段：源码不可得、工具行为依赖先前调用时，完整任务轨迹是更合适学习单位，offline按训练gold/执行反馈batch生成与merge，online只用可观察执行结果早停。修订只改变metadata而非权限与程序证明；held-out真实任务和版本必须核。已有参数时收益很小、BrowseComp调用成本可升、weak模型反例与不充分重复保留；无可靠反馈时回退人工窄合同/澄清/outcome检查。

## COMPOT — INFER-TENSORRT-LLM / Ch49

实际读Ch49 L1300–1358含module replacement、结构fusion、原通道保留/whitening-SVD与分层预算；相邻Ch48 target feature/验证和Ch50 engine开头。现有静态低秩拥有whitening/SVD与预算，不拥有正交dictionary与稀疏系数的两个条件闭式子问题；其差异不是再列一种压缩配方。建议L1347后1–2段：单SVD子空间简单；activation-whitened字典正交可让固定字典的系数hard threshold与固定系数的Procrustes薄SVD分别解析，但联合非凸、交替仍迭代，主实验20轮，不能全局non-iterative。字典/非零系数/mask应同预算计，原范数全局谱分配与whiten重构指标分开。校准Gram/代表性、字典驻留、稀疏执行开销近正文；无匹配kernel不能推runtime加速，回退SVD或dense；不采用协议不一的普胜。

## Reward Model bias discovery — TRAIN-RLHF / Ch31

实际读Ch31 L146–174偏置列表、candidate distribution漂移与分支反事实身份；相邻Ch30/32开头。现有列举长度/格式偏置与分布漂移，未承载未知属性发现与独立反事实检验分责。建议L164后1–2段：固定属性清单便宜透明；未知shortcut可用自然语言属性在RM偏好与独立judge反偏好间搜索Pareto集合，再由独立validation/test、counterfactual最小改写和多重检验确认。搜索score不是bias事实，更不是policy已经学习；judge/rewriter可能同源关联变化，需要保留prompt子分布与改写身份。生成/搜索/重写成本、单fullrun search对照和n10/三合成regex注入recall不能授未知偏置完整召回；预算小/评估不独立回退人工属性与随机审计。

## Sparrow — INFER-SPECULATIVE-DECODING / Ch48

实际读Ch48 L941–946动态视觉取证、L959–968 target feature/commit，邻Ch47和Ch49相关execution段。已有视觉读取适配和借target feature，不等于本篇训练visual bridge、推理不读visual KV的分离机制。建议L944后1–2段：draft全视觉条件在容量足时合理；长视觉/小draft可训练中层visual bridge并递归MTP，推理只读target融合后的text hidden/window，视觉计算留target，target仍verify与commit。不授任意任务可丢视觉或lossless实现已核。Bridge/interface和分布漂移须重新校验，失败回退完整条件/原AR；prefill仍付费、DSR不是ESR，训练/接口成本与仅受测7B/四video任务近正文，无并发/SLO普遍收益。
