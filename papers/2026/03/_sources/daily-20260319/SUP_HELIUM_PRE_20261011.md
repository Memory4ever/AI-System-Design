# Helium 2603.16104：必要原证 / 唯一 owner / 一段 PRE

作者 resume_mar18；仅03-19补03-18。完整AB具体准入2+2+2=6，因实际调度接口差额作必要深入；[exact-v1 HTML](https://arxiv.org/html/2603.16104v1)§2 Scope/§3–6/§7.1–7.6 Tables1–5/§9必要方法/对照/关键反侧已实际读，不遍App全部算法证明、DSL附件、代码或复现。精确v1标题有Extended，不凭单词自证更早公开或重要revision；本日日级身份依据复用同批夹证，未发现具体先稿事件。

## 必要 Source / 有限支持

§2 Scope：同base LLM、local data operation，无remote API，批量相同结构DAG；§9又写external best-effort为限制而非受测支持。Dynamic loop/fan-out仍future，不批准任意Agent program。§4常规backward deadcode/CSE，输入已materialize时签operator type与input value，LRU prompt cache hit替CacheFetch，只限定deterministic nonLLM/greedyLLM；这不是全token数值确定性、合法副作用剪除或跨模型复用保证。Model/tokenizer/template/revision/数据freshness和sideeffect identity是本书采用时必须补充的工程门，未声称原实现已完整满足。

§5 TRT把static token/动态placeholder prefix树与leaf依赖DAG同时保留；静态prefix首批precompute/后batchreuse，query内动态共享与跨query静态共享不是同级。仅相邻calls同worker共享的tokenusage模型、平均output离线profile与precedence delay建模batch影响；不是GPU真实墙钟/一般KV执行最优。Operator-level nested soft schedule用criticalpath/earlieststart/forceprogress，inner sequence query-wise复用questionprefix，跨inner sequence operator-wise复用staticprefix；runtime可重排readycalls饱和batch，不是一条不可变token时序。最优gap0.9%只7缩小case、2–4agent/2–4query、单worker8192token/MILP6h timeout的该模型，不外推physical/SLO/fairness或证明一般复杂度（AppB未另审不采用精确复杂度保证）。

§6 vLLM0.16.0/APC/chunkedprefill，worker每engine独进程IPC；priority pin static KV仍原blockLRU/longestprefix eviction，evicted下batch重算；pin不等永不驱逐或总HBM减小。离线profile不同queryset、首次prefill/warm都付费后摊销，不能把预热后的相对耗时当coldstart全费。Prompt output缓存省整call，KV缓存只省prefill；两者验证对象不同。

§7：2×H100NVL94GB/AMD9554 64cores，Qwen3-8B/14B主实验每modelinstance一GPU，Llama3.1-8B/Qwen3-32B仅sensitivity；模型与runtimeprecision、CUDA/torch/driver、完整arrival/concurrency/SLO/重复run与CI/质量一致验证 Not Disclosed。AgentScope0.1.6、KVFlow SGLang版本ND且预populate，其他统一vLLM0.16.0；framework exactversions除上述ND。Baselines HTTP same-machine+queue-length loadbalancer，HeliumIPC路径不同，3.1msHTTP/89μsLB作者profile仅Trading16/1408calls，不宣布所有crossprotocol无混杂。NaivevLLM串行整query导致最高100.92倍，不叫对现代vLLM engine普遍加速；KVFlow最高1.56倍primitive、1.34倍Trading是对应层级。

Microbench MMLU200/TATQA100×6或200×6，Amazon200/100×60reviews，batch固定只开KV/scheduler；Trading19agents/88operators、100stocks两天，第一天warm第二天eval，无工具API，不认证金融或任务成功。Table3 Trading16 Qwen8B removeKV latency+3.55%、CSE+23.35%、promptcache+13.56%、CAS+17.66%，互依优化不说独立加法归因；Table4『caching disabled』具体只是proactiveKV/promptcache关闭，vLLM passiveprefix保留，否则cachehit率不可解释。QueryWise仍串行/OpWise拓扑优先不能代表所有DAG最优。§7.4 highsharing/少量model/人为cachecap受限，metadata552KiB vs14.8MiB不是全部cachememory（TRT与engineRadixCache抽象不同）。P95改善37.2vs51.7是batch受限population，无arrivalSLO/productionguarantee。未见受测数值全面反退不要求强造负数；实际成本边界是prewarm/profile/保留容量、动态graph/外部delay、输出identity未验。

## Actual sole INFER-SCHEDULING 差额

已实际重载Books合同/ROADMAP/PROJECT_CONTEXT/学习理念/WRITING_GUIDE/LS路由。Ch56 1368–1418完整criticalpath→postdecisionqueue/KV→programstate→toolprogress、公平性已有；1466–1484 readiness/released有界准入亦已有。Ch55/57开篇与Ch81 60–87读取：workflow侧temporalcache/状态/副作用规则不复制成调度实现。现文已有DAG+cache联合一般论点，但没有**static/动态placeholder前缀树与依赖图联结、query-wise inner/cross-query operator-wise outer软顺序**的具体可执行粒度。唯一 INFER-SCHEDULING，不创建queryoptimizer owner或改Agent状态机。

拟Ch56原“Runtime仍拥有真实page…”局部之后/ProgramState子标题之前一段与静态注；未授独核/锁，未写。

### 一段逐字 PRE

批量工作流若已知 prompt 模板，还可把静态 token 与等待上游输出的 placeholder 放进前缀树，同时保留叶节点之间的依赖图。这样，调度不只问“哪两个 ready calls 当前前缀相同”，而能让内层按同一 query 连续执行以复用动态上下文，外层按共享静态前缀组织不同 query；离线输出长度统计只提出软顺序，runtime 仍在依赖满足后按真实 queue 与 KV 容量调整。一个[受限同模型 DAG 系统](https://arxiv.org/html/2603.16104v1)还预填静态 KV，并在确定性且身份兼容的输入上用缓存结果替代整次 operator：前者省 prefill，后者改变计算依赖为读取依赖，不能混称同一种缓存。模型、template、数据 freshness 或副作用无法保持时，结果缓存不得替执行；预热、profile、保留容量、查询规划与驱逐重算都计费，greedy 也不自行保证跨 runtime 数值身份。动态循环、外部工具时延或低共享率使计划失准时，保留普通 engine-local prefix cache、依赖就绪调度与必要重算，不把 token-cost 模型的局部最优差距当作真实墙钟或多租户 SLO 保证。<!-- source-family:SF-2026-ARXIV-2603-16104 -->

### 静态来源注

- `SF-2026-ARXIV-2603-16104` — [Helium exact-v1](https://arxiv.org/html/2603.16104v1)必要§2 Scope/3–7/Tables1–5/9；采用模板前缀树+依赖与nested soft schedule、KV/输出缓存分责，限定同model/local/static批量结构。Greedy不授跨runtime exact identity、token-cost MILP不授physical/SLO最优，预热/profile及跨baseline路径、metadata抽象差异保留；未核代码/复现实验或精确AppB复杂度证明。

## 非准备者必要 Source / PRE（root）

恢复后实际重读当前本日合同与停点；打开精确v1 §2–6/§7.1–7.3 Tables1–5、§7.5–7.6与§9中拟采用接口及直接限制。TRT保留token/placeholder层级和leaf依赖，内层query-wise/跨内层operator-wise软顺序、runtime可调整ready calls、静态KV预热和整operator结果替换确为不同机制。对照使用串行naive vLLM、IPC/HTTP路径差异与预热/离线profile成本保留；0.9%是七个缩小token模型case而非物理SLO，metadata不是全缓存，greedy不授跨runtime数值同一性。

实际回读 Ch56 1368–1425/1466–1490及Ch55开篇，ROADMAP解析Ch57路径；本一段接在真实runtime状态所有权之后、ProgramState之前，解释模板已知的批量分支而不重写一般DAG/公平性或Agent持久状态。PRE和静态注 PASS：仅授Ch56这一段与本人静态注窄锁，作者写后仍须非writer实际POST；本Source不声称所有敏感性图、附件证明、实现或复现已核验，不授DAY。

## 非写入者 actualPOST（root）

实际Ch56 1370–1409完整 critical-path/postdecision state → 新1391 → ProgramState/tool-progress/fairness 局部与最后本人Helium注、三条相邻来源注已顺读；一段逐字回对PRE准确，静态来源正确。已读实际Ch57开篇确认平台合同仍不接管engine微状态。新增段落限定模板已知的批量共享机制，KV预热与whole-output替换不混同，soft plan不越过runtime控制，费用、身份、失准及旧路径附近可定位。actualPOST PASS，Ch56窄锁释放，允许本family计实际整合，不授DAY或一般SLO/确定性保证。
