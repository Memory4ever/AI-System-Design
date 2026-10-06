# Live 2026-10-09：检索必要证据

作者 supplement_20260312；窗口仅BJT2026-10-08。root完整AB已准入独校准；author11与root实际官方CL/IR Oct8日期组核，不以Submitted Oct7当公开日。两current仅v1、无withdraw信号；10170自述Initial draft。正式README独立维护，Source/PRE通过不预授Books写后或DAY。

## 2610.10508v1 — Your Prompt Should Do More: Effects of Retrieval Instructions in Embedding Models

[精确HTML](https://arxiv.org/html/2610.10508v1)。完整AB及当前history/comment实际读；actual必要§3全部、§4.1–3/Tables2–5，§5全部/T6、§6完整，F.1–4/H/J完整（web输出结尾截断后从官方HTML定点补全）；图只caption/正文，未核像素、可选代码或复现。2+1+2=5，标准必要Source已完成，具体检索表示gap深入受影响方法/反侧，不因gap改分。

任务孤立候选池能让相似度取巧→为任务关系加入query-side paraphrase distractors、同时把同一文本在STS指令下作positive→应检验共享候选池中的任务服从而非只比较prompt对单任务排名。§5：Qwen3Embedding0.6B全参InfoNCE、QA/bitext分别训练；8 target-side随机负例，50%一项换wrong-task target；QA+STS或bitext+STS联合。不是只在线改query或免索引迁移。F固定开发集select checkpoint（paraphrase setting），SQuAD原eval只最终用；OPUS去重且按所有test语言过滤相同/高char4gram相似，不能授完美无污染。

反侧：T6 SQuAD正常R@1 .724→.706、Tatoeba .844→.837，paraphrase分别 .014→.470/.102→.569，仍远非可靠完全服从；random池增大控制并非仅语义干扰。T5报告all-instruction/all-language最大值，不作默认onlineprompt性能；e5/harrier在部分Tatoeba保留，不能说所有embedding都无服从。H同setup去query-negative不改善paraphrase只支持这个消融，不证明所有原训练缺少这种负例或唯一内部成因。几何相关非机制因果，QA与bitext的similarity变化还异向。§6八模型/两任务、单GPT5.4mini paraphrase生成器，未测clustering/全域/安全；未采用Fig5全MTEB均值作无退化证明。

费用/身份：F全参一epoch/max1024/batch8/lr1e-6，J每个训练约12h单GPU、全实验上界504GPUh；MI250x/GH200列作总体资源，不补各run完整硬件/软件SHA或生产时延。合成/编码/训练/开发checkpoint选择/共享池评价及backbone改变后的passage重编码/双索引与回归均付费；论文未证明旧索引兼容。

Actual唯一owner `AGENT-RAG` Ch76；实际65–108、120–157、990–1025完整局部与章开篇，Ch75/77开篇，Ch12输入embedding/检索owner边界124实际核。已有query-only优化、domainprefix冻passage、迁移和heading不同分支，不承载错任务同语义负例/同文本角色按指令切换的训练与共享池验收。

### 最小逐字PRE（已写，actual POST通过）

拟Ch76 Dense/hybrid完整段后、UNREAL共享decoder分支前一段：

单任务候选池中，相似度高常足以得到好排名，却不能证明编码器遵守了“找答案”而不是“找同义问题”的指令。共享索引面对多种关系时，应在候选池加入语义相近但不满足当前任务的 query-side distractor，并保留等量随机扩池控制；若要训练这条分支，可让同一改写文本在 STS 指令下作正例、在答案或翻译检索下作负例，联合保存 instruction、关系标签与候选身份。[受限对照](https://arxiv.org/html/2610.10508v1)支持这种负例资格和验收人口，不证明所有原训练的唯一缺陷或完全服从；正常检索仍会小幅退步，强干扰下也未恢复可靠首位命中。合成、全参数训练、checkpoint选择与共享池评价均付费，backbone变化后的passage重编码/双索引兼容还须另验；负例资格含糊、旧任务退步或迁移预算不足时，保留专用任务检索、lexical/hybrid与已核索引，不把prompt措辞或几何位移当作任务完成证明。<!-- source-family:SF-2026-ARXIV-2610-10508 -->

非作者 review_mar11_continue 已实际必要Source、Ch76局部owner及逐字PRE通过；root授窄锁后实际写新140/本人1354注。作者已实际顺读127–154完整邻接及末注；root非writer实际127–147完整Dense/new/UNREAL与本人注POST通过，窄锁释放，不授整日。

## 2610.10170v1 — Does Document Structure Help Dense Retrieval? A Placebo-Controlled Ablation of Four Mechanisms Across Two Corpora

[精确HTML](https://arxiv.org/html/2610.10170v1)。actual完整§3–8必要方法/人口/评价/反侧与T1–2、A.2/A.4/E.3定点控制（原HTMLsection抽取全文，不读全图pixels或代码）；当前Initial draft保留。2+1+2=5，标准必要Source已完成，拟具体结构检索归因gap深入受影响范围；不将作者‘organization可靠’升级为所有RAG经验。

§3在同corpus/embedder/budget内对比boundary、prefix与routing；P保持A3 chunks而用跨文档按depth置换heading作控制，C2不变chunk/flat算法。A3是与chunk正确对应的induced路径，不能将‘真实heading’改读成全部native/gold路径，G3才gold分支。C1 A3-A1同时改变边界和prefix类型，只是bundled comparison；严格‘只隔离boundary’不由这个contrast单独推出。作者size匹配正文≤4而列均值255.4/259.6及244.9/249.8差4.2/4.9，故不写精确≤4/完全size matched。P构造E.3只再说count residual，没有实际数；不授严格零同文/语义独立，仅采用应做置换控制这一接口。

§4 Wikipedia200文档（实际951synthetic query/184doc）、QASPER1585paper（实际4303native question/1508paper），native/induced字节span一致78.9/75.8非同segmentation；英长结构文本与单Gemma4 inducer，未测全语言/平坦短文。QASPER合train/val/test作无监督IR对照，不称独立heldout训练。cov-nDCG的marginal gain去重复gold character coverage，再用各condition自己的ideal normalizer；不能冒称共同absolute coverage或下游answer分数。prefix排除于gold offsets，tokenbudget计prefix。cluster bootstrap/Holm只四primarycontrast，depth与querytype切片探索，不把n.s.当gold/induced等效。

T1小局部C2 .0099/.0161；C4 centroid-top5 firststage过滤原vectors在两人口退步。§3.2实际有fewer-than-k时global-ranking backfill，不能写完全无补回路径；但后续ranking不能自行恢复没有进入其候选池的chunk，原§6.4关于reranker宽flat‘恢复被剪候选’未与§3.2/5.3闭合到同一协议，不采用该机制解释。C3 QASPER n.s.非所有induced等价；T2/A1在512token预算可低于plainwindow，不能用固定top-k收益代替contextbudget。§8明确仅retrieval，未测answergeneration；不授通用hierarchy无效、所有结构gain因果或所有prefix必好。

费用：Gemma4 26BA4B单H200完成induction/context/query/改写，一次cache不免offline成本；bge-small/large与reranker身份、prefix长度、分块/repair、重编码、两级route/全库backfill和上下文成本分别保存。代码/config/results仅will release，本命题不依赖artifact可用，无复现。缺少全链时延/运维/answer效用，不补生产SLO。

Actual owner唯一AGENT-RAG Ch76：实际65–108完整document/query/answer层、headingindex与局限，446–477完整chunk/evidenceunit/pathset交接，120–157及990–1025检索/迁移局部；75/77开篇。已有结构与分层原则不新写；窄差额仅是同chunks/encoder跨文heading置换控制＋prefix计费/第一阶段recall分验，不重复说明‘结构有益’。

### 最小逐字PRE（已写，actual POST通过）

拟Ch76原headingindex两段和其source marker完整之后、Structured Retrieval标题前一段：

标题前缀改善排名，还可能只是额外文本改变了 embedding，不能仅拿无前缀 baseline 归因于正确结构。可在同 chunks、encoder 和检索算法下，将与 chunk 对应的 heading path 与跨文档置换的路径分别编码，匹配格式和深度分布、核对残留同文赋值，再按原文 content-only offsets 计相关性；前缀自身也须计入 token budget。[两语料受限对照](https://arxiv.org/html/2610.10170v1)支持这条归因控制，却只有小幅检索效果，没有答案级效用验证。若再用 section router 剪候选，应另测第一阶段保留 gold-bearing section 的概率，不能由后续排序较好掩盖证据已被剪掉；有限 centroid/top-5 退步不否定所有层级检索。结构诱导、修复、置换回归、重编码与额外 prefix 均付费，归因、召回或预算失配时保留 flat/hybrid 和原文 chunk，不由组织形式批准替换完整证据。<!-- source-family:SF-2026-ARXIV-2610-10170 -->

非作者 review_mar11_continue 已实际必要Source、Ch76局部owner与逐字PRE通过；上述conditional backfill/A3 induced身份笔记消歧已同步，root指定PRE写‘与 chunk 对应的 heading path’。root授窄锁后实际写新103/本人1356注；作者及root非writer均已实际顺读91–117完整heading/new/Structured邻接及本人注，actualPOST通过，窄锁释放，不授DAY。
