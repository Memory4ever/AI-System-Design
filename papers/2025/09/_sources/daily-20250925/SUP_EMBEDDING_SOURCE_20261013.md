# EmbeddingGemma必要Source与Ch76具体差额/PRE提案：Carson

## 1. 已通过准入与实际必要原文

Feynman§10真实准入/2+2+2=6与Sep24机构研究披露门通过。Sep04仅模型release/MRL/QAT产品事实，后附report不能倒证当时已公开整稿；本次精确2509.20354v1，不用currentv3或版本号赋重要修订。原件/完整v1 HTML341216 bytes200/exit0、AB/作者/机构身份均在SUP_GOOGLE及SUP_curl-embedding-*文件。

实际读§1、§2.1–2.3/Eqs1–5、§3.1–3.3/Tables2–4，量化Table1及§4评价协议/§5future限制。机制：Gemma3先作UL2 encoder-decoder适配，再取encoder，bidirectional+mean-pool、768→3072→768两随机投影。输入query/positive/optional hardnegative，任务前缀不同；NCE+重复negative mask+stopgradient难负权重，GOR只second-moment项；GE embedding matching的teacher为Gemini Embedding，对Q/P+/P-分别matching，不只query-document relevance scalar。采用只到这个披露层，不补造未展示的teacher/student维度兼容实现或完整matching函数；成熟GOR/MRL/QAT非本次新公式。

配方2.1T含encoder-decoder训练，预fine314B/fine20B；大batch noisy无hardnegative与小batch高质量hardnegative阶段分开，单dataset batch组织in-batch negatives。Mixture以既有seed+10 Dirichlet随机初始化的Bayesian优化，后作无权重平均soup，训练/搜索/selection不是免费。Table2/3消融只单mixture，除注明外无soup：encoder-decoder总体60.4/53.6对decoder59.7/52.6，但Multi.Class50.3低于50.5；mean pool总体较好，attention Retrieval61.7仍高于mean60.2。Table4三个mixture vs平均soup不能独立证明teacher matching/GOR/初始化各收益，也不是任何checkpoint均可合并。未给对应matching包含hardnegative的单独受控消融，不把整套SOTA归因该扩展。

Table1 raw bf16与QATint4/int8/mixed precision分开，原bf16 mean-task61.15/code68.76与int4 block60.62/67.99不是无损。4bit/短embedding结果不授生产latency/完整RAM/质量一致保证。§1官方MTEB特定Sep23 leaderboard、排除训练>25%MTEB对象与CodeSearchNet缺项说明不能消除所有污染/selection；query检索语义、task平均/类型平均/子任务均分开。§5多模态只是future；完整训练硬件、运行配置/E2E服务SLO与独立重复不确定性必要域Not Disclosed，未核权重/代码/复現。

## 2. 已实际加载owner与具体缺口

ROADMAP owner `AGENT-RAG` Ch76。当前Ch76正文50–164、检索表示303–369和1354–1380交接实际读：index身份/source权威、LLM2Vec-Gen93–95 response embedding目标、97–99doc效用listwise蒸馏、任务负例152、难负例ARK322、阶段适配dense/late-interaction324、SemPA326、SAE索引328等；Ch75的615–631 Context→外部evidence/Memory交接与Ch77开篇状态/证据身份已实际读，不扩全书或改目录。现有LLM2Vec-Gen目标是response embedding，LURE是task utility/排名，ARK是难负例评价，阶段适配是匹配目标/多向量，**均未明确把query、positive passage和hardnegative passage自身的teacher embedding同时作为student监督对象**。这是有限训练信号选择差额，不是将普通teacher/negative概念重复为新机制；原encoder/index/来源身份与任务检索退路仍保留。

拟采用不包含数值或完整训练recipe，只限定三对象matching与空间/任务/事实分责。该具体缺口触发受影响内容深入，已按§1足够方法、反侧/单因素限制读，不遍历所有MTEB表/权重。现在供reader必要Source/owner/PRE，非writer自授；若非作者判现有正文已足具体覆盖则No Change，不坚持制造新段。

## 3. 两段逐字PRE提案（待reader与root锁，尚未写）

实际进一步定位后，拟插在Ch76完整`从 dense encoder 转向 late-interaction，还要决定在哪个训练阶段让表示适配新的匹配目标`段（末尾2602.16609 marker）后、`表示适配也不必直接在向量 similarity 上训练`SemPA段前。这比原93/95 query-side位置更贴近训练目标/表示主线；原ARK难负例、阶段适配与后SemPA/SAE完整邻接已读，仅两段与自身Review note。当前Ch76限定unstaged diff为空；无锁，不改Books。若获准写前再次读取完整锚点/邻接/dirty diff，保护新并发修改。

训练小型检索表示时，teacher 还可以提供向量空间中的监督对象，而不只提供某个 query–document pair 的相关性分数。一条受限分支在已有对比目标旁，对 query、positive passage 与 hard-negative passage 分别加入 teacher embedding matching；难负例不仅决定对比排斥方向，它自身的表示也进入教师监督。这里改变的是训练信号的对象，不意味着 teacher 的空间已是任务真值，更不能让相近向量取得原文事实权威。工程上要共同保存任务前缀、正负例资格、teacher/student encoder、投影与索引 revision，教师变更后重新验收表示及检索消费。<!-- source-family:SF-2025-ARXIV-2509-20354 -->

这条分支还支付 teacher 编码、额外初始化训练、mixture 搜索与 checkpoint 选择费用；spread-out、维度截断和量化不能被合成一份无损保证。[有限配方与消融](https://arxiv.org/html/2509.20354v1)同时显示总体均值和子任务可能分离：较好的初始化仍有类别切片退步，简单 mean pooling 的均值较高，attention pooling 却能在 retrieval 切片更好；单独配方消融没有隔离三对象 matching 的全部收益。因此只采用这个监督接口，不把整套结果唯一归因它，也不外推跨teacher或生产SLO。教师几何、负例资格或任务消费不兼容时，保留普通对比训练、已验encoder/index与lexical/hybrid检索，用独立任务评价和原文支持核验决定是否替换。

拟自身note：`SF-2025-ARXIV-2509-20354`；Sep24机构研究披露、exactv1§2/Eqs1–5/§3T2–4/Table1。6分、仅Q/P+/P-监督接口差额；成熟GOR/MRL/QAT、未隔离matching收益、子任务反侧/teacher与全费用保留。Source/PRE待非作者、root锁待，未写/无POST、无DAY。

## 4. root窄锁后的实际写入，供Feynman非writer POST

本节覆盖上节尚未写入状态，不改变原提案/Source记录。Feynman实际§12必要Source、具体owner及两段PRE通过，root已实际回读并授Carson Ch76唯一窄锁。压缩恢复后actual重读AGENTS/当前Research与Report/Sources说明及Daily和arXiv/Prompt/完整ROADMAP、本日停点与§12–14；Books背景/理念/写作、State相关路由、Ch76完整306–340及93–101、Ch75的615–631/Ch77的1–45实际重读。写前Ch76 cached/unstaged diff均空。

仅apply_patch在完整`SF-2026-ARXIV-2602-16609`阶段适配段后、SemPA整段前加入两段（当前326、328），并在Review notes末尾加入本人一条`SF-2025-ARXIV-2509-20354`（当前1768）。正文沿已核两段，并显式落实§12/root边界：hardnegative optional、三对象仅含难负例的高质量fine-tuning，不反投noisy预微调所有样本。无matching函数补造、无损/唯一因果/生产SLO保证。teacher/投影/index revision是显式工程要求，非作者已验证热升级。

写后实际顺读难负例ARK整段→阶段适配完整段→两新段→SemPA完整段→SAE两段，实际读本人末注；监督对象与适配阶段邻接成立，未更改原前后论证。限定unstaged diff为6新增/0删除（两正文及其空行、本人note及空行），没有运行前Ch76其他改动；其余共享工作树并发dirty不归本任务。限定diff-check通过，cached本日/Ch76为空，未stage/commit/push；未改State/index/shared scripts或任何他人notes。

**作者写入/顺读已完成，非作者POST尚未发生；不声称Books完成/DAY/FINAL/计数。** root锁保持，须Feynman实际两正文/完整邻接/本note回对有效Source与采用边界，root接纳后才释放。本文件是立即可转交持久包，不使用UI跨任务消息。

## 5. 实际POST接纳后的own note行政同步

本节覆盖§4未POST停点。作者实际读回Feynman§15，root现已actual完整回读§15、Ch76真实314–340及本人末注/完整diff，接纳POST。按root同窄锁行政授权，仅apply_patch本人note的待POST/root字句为真实Feynman§15/接纳结果；两正文及其他notes不动。root尚待最后回读行政差额释放锁，作者不代释放，不改State/计数、不授DAY。Source/采用域不重研，继续Video/LiteRT/具名日期及来源。

root已实际最后读回own末注同步/正文未变并释放窄锁；按明确行政授权仅将自身末注待释放句改为已释放。正文及其他notes不动，Source/PRE/实际POST有效复用；报告已同步实际整合1和真实§15，不待Embedding域，不预支DAY。
