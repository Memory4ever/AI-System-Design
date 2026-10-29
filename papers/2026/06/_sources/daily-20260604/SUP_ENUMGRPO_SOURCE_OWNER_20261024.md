# 03152 EnumGRPO — necessary Source / owner / PRE

作者supp_20260604_author；R2准入/Jun03日期已过。2+2+2=6，具体queryplan quality-equivalence边界深入。exact-v1完整TEXT86064chars已实存，作者已读§2/3.1–3.3/4/5.1/5.5必要；支持与反侧足够，未核实现或复现。

## 必要证据

§2 semantic map/filter/rank/reduce/join是approximate，不同ordering/粒度改变quality而非仅cost；SQL固定snapshot deterministic，LLMphysicaltool另绑定model/prompt/batching。§3.1五axis（code-vs-data、scalar-vsaggregate、placement、scope、projection）；§3.2 seedN distinctassignment是soft recommendations可被真实中间关系override，不硬冻结plan。权重冻结，EX/TupleF1/CellF1及组内token/step归一cost产生relativeadvantages，经summary/contrast/ADDUPDATEDELETE/consolidate改自然语言pool，非gradient GRPO训练。只在offlinelearning可见gold，testprompt带pool后不enumeration、不见gold。组内优势不自动唯一识别axis因果，不采用公式为已验证全局优化recipe。

§4 SWAN120缺列/缺joinpath构造问题，40learning/80eval，gold来自原数据库；并非真实DB已经知道被删事实。DuckDB1.5/MCPstdio/OpenHandsSDK1.11.5，Ubuntu22.04双Xeon8352Y/504GB/no localGPU；Sonnet4.6planner、Haiku4.5operator，LiteLLM1.81.16/AWS，30steps/30min。N5/B2即200learningrollouts/约8.4h；结果3独立runs。费用/价格仅报告作者当时条件，不作为当前价推荐。

§5.1 表3 main35.4%EX vsbase32.1%，不是高可靠全正确；heldout32.9%更短便宜但低于35.4，不授无损。317×是LLM-operator账3.42→.011/每query，base已88×，不把全部收益归新optimizer；此账不含全部Sonnet规划、制备/蒸馏等总服务费。§5.5另报learning约$41.2（200×.206）与约1460query摊销估计，仍依作者固定流量/价格、学习账边界；不认证生产回本。Gold只offline，promptpool换schema/backbone要重验，额外context也有费。

## actual owner与PRE

三context/ROADMAP已读，唯一AGENT-PLANNING Ch79；actual Decomposition完整两组benefit/cost列表与“拆分粒度应由可验证边界...”原段，以及下方完整SQLprobe段/依赖并行交接已读。当前只讲过度拆分开销与probe-first，没有approx semanticoperator重排**非answer-equivalent**以及按axis枚举后的文本heuristic更新这条边界。不在Ch76重写retrieval；经验存储生命周期仍由Ch77拥有，这里只讲planner消费/评价。

拟在“拆分粒度应由可验证边界决定，而非步骤越多越‘智能’。”完整段后、SQLprobe完整段前插2段。

完整上锚：

拆分粒度应由可验证边界决定，而非步骤越多越“智能”。

拟增两段：

含近似语义算子的计划，不能直接继承“重排只改变成本、答案仍等价”的关系代数假设。将推断放在过滤前后、逐行还是成组处理、给窄列还是较宽上下文，会同时改变模型所见信息、误差和费用；先看真实中间结果再决定下一步，比一开始固定所有近似操作更有适用性。可以在离线学习中沿这些结构轴为同一 query 构造不同软提示，执行后比较质量与成本，再把差额压成供后续 planner 消费的文字启发式；这更新的是提示经验，而非模型权重，候选也不是已被证明语义等价或最优的计划。<!-- source-family:SF-2026-ARXIV-2606-03152 -->

[受限混合查询实验](https://arxiv.org/html/2606.03152v1)中的 gold 只用于离线评分，线上选择仍须根据当前 workspace 和工具结果修正；组内相对收益不能唯一证明哪一轴造成改善。较短、较少语义调用的策略仍可能降低完整答案正确率，LLM-operator 费用的大幅下降也不包含全部规划、经验制备和摊销成本。执行比较、样本与蒸馏调用、额外 prompt、数据库运算及独立质量回归都需计费；schema、数据或模型变化时重验经验，支持不足或净收益不明时保留显式 SQL、原有受控算子与人工核对，不让一个便宜计划或可执行查询自签答案正确性。<!-- source-family:SF-2026-ARXIV-2606-03152 -->

完整下锚：

对可查询环境，拆分还可以先生成取证 probe，而不是立即把每个子目标当作最终答案的一部分。一条受限 SQL 分支让 planner 提出覆盖原问题及周边信息的独立短查询，执行并保留成功、失败与探索结果；只有 planner 判断证据足够，才由另一个 proposer 结合这些结果合成最终 SQL。[必要分支与评价反侧](https://arxiv.org/pdf/2604.22934v1)支持这条 probe-first 接口，却不把模型判断的 coverage 变成逻辑完备证明：执行有结果不等语义符合，合法空结果也不必是错，back-translation verifier 仍会共享模型盲点。并行同时扩大搜索，不能将收益全归调度；调用、数据库负载、有限返回和重试都付费，平均时延模型不授生产 SLO。取证、覆盖或最终语义失配时，保留原 schema、单链/有限分支、独立结果检查或人工查询，不由许多局部成功批准最终答案或数据库副作用。<!-- source-family:SF-2026-ARXIV-2604-22934 -->

Review note拟：`SF-2026-ARXIV-2606-03152`：2+2+2=6；exact-v1 §2–5.1/5.5，approx算子重排非answer-equivalent，结构soft hints→gold限offline→文字pool非weightupdate；保40/80/三runs、heldout更省可更错、317x仅operator/base88x与learning/总费边界，未授最优/生产SLO。未核实现或复现。待实际写后复核。
