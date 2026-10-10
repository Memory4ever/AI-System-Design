# 第三批准入提案：42个新完整题摘，不作候选分母

原件[language20](./increment-abstracts-language20-20261007.jsonl)18成功、2TLS失败；[agent24](./increment-abstracts-agent24-20261007.jsonl)仅重试前2成功＋22新题摘。下面42逐项完整题摘已读；日期在必要恢复，不因Submitted直接落窗、不评分。No quotas，宽题名库存不是全文队列。

|ID|原约束→实际增量→待核选择|
|---|---|
|08545|潜在：修复retrieval冻结→code评估结果改edit-driven检索方向→反馈改变下一步证据而非只改generation；预算归因待核|
|08892|拟关闭：role-consistency adversarial dataset+Vicuna/openLLM对比，未识别新的角色失败条件或设计取舍，仅覆盖与coherence统计|
|08477|拟关闭：治疗场景Transformer特征→SHA/统计模型检查/strategy的愿景与初步fidelity，未给改变模型系统判断的具体保证条件；formal术语/领域结果不自动准入|
|08267|拟关闭：English scaffold+local concepts/retrieval+distill医疗语言总体改善，未给可隔离的新跨语言组合成立条件；非因small/local排除|
|19935|潜在：passive fact retrieval成绩→同topic长中断历史的主动tool/parameter grounding仍失败→memory应用需与召回分开|
|08181|潜在：TabPFN只看output→hidden probing发现线性系数/表达式intermediates及早层答案→可读出计算对象的层位置，probe≠因果需核|
|08146|潜在：continued全模型SFT损source能力→proxy relevance选head并gradientmask→hard transfer edit相关head、easy preservation低相关head不同分支|
|08141|拟关闭：Urdu corpus+English replay+continuedpretrain/SFT和总体成绩，未新增配比成立条件/forgetting反证，成熟recipe不能计贡献|
|16224|潜在：廉价style ngram logit注入→单TinyLlama仅窄λ/单作者可用，多作者甚至小λ失败→轻量control有效域与style/fluency分开|
|07986|拟关闭：文化L1–5分层数据覆盖与高层更难，未给修正主线测量/设计判断的具体盲区对照；内容丰富不替代增量|
|07985|拟关闭：ClaimReview/抓取/归一/LLMextract/justify组合＋G-Eval/人评总体，无新的标签冲突控制/机制成立条件|
|07984|潜在：多个judge直接avg→crossjudge scale mismatch与主judge isotonic人锚校准→量表身份与culturaldepth/metricproxy分开|
|07974|潜在：detector通用能力分→crossprompt/model/domain泛化与tense/pronoun等shift相关→测量人口/linguistic变化解释范围；相关非因果|
|07965|潜在：raw confidence不可跨model比较→validation校准后advantage router+ensemble cleaning→competence可比性是cascade前提，经验holdout不授普遍校准|
|08816|潜在：reasoner自己维护庞大graph→独立廉价LM_Mem异步图传播后只供高信号context→memory更新与消费拆预算/新鲜度条件；总体Pareto非验证|
|08785|拟关闭：真实议会投票数据/CHES映射与政治方向描述，未建立新的偏见因果控制、可靠性条件或主线选择反证|
|08747|拟关闭：orchestrator majority切retriever/reasoner+concise context/QA总指标，题摘未给新的trigger定义/成立条件；将常见selective retrieval重命名不足|
|08743|潜在：table order变化造成prefix副本→PK/FK引导离线table KV+Trie+rerank/load pipeline→结构条件与cache兼容/TTFT一起核|
|08734|拟关闭：IaC SFT+verifier RL及syntax/deploy/security筛选、总体多bench增益，未给新的verification/credit机制或失效边界；框架移领域不自动准入|
|08731|潜在：直接模仿long专家trajectory累积误差→沿trajectory实时competence选超当前能力的中间goal→demonstration用于curriculum而非只初始化|
|08682|含糊定点：实际summarization案例提示prompt供应商转移差及upstream瓶颈/需求演化；需核心是否具体实验/失败条件，不能仅四项经验主题准入|
|08679|潜在：persona强化损objective→SFT双reason模式＋DualGRPO学select→helpful/misaligned context分支；adaptive不是事实真值保证|
|08673|拟关闭：alignment结构性论述/社会关系类比，未给可核的模型机制/理论假设与结论，泛AGI治理不新增技术链|
|08670|潜在：独立doc KV丢跨docattention→retrieval-aware contrastive logit同步各expert→把evidence融合移到decoder，非声称恢复原完整attention|
|08653|潜在：并/串clarification忽略问题依赖→intent dependency引导澄清顺序＋轨迹训练→dependency影响有效交互；userload指标需真实人/模拟分开|
|08605|潜在：任务前passive memory→每step entropy触发、定制experience→检索时机与内容joint条件；entropy非correctness保证|
|08557|潜在：视频SE/calibration弱→clean/时空perturb多采样再semanticcluster的VASE→扰动揭示视觉条件blindspot，LLM hallucination标签非gold|
|08510|拟关闭：screenplay四任务/150film统一narrative benchmark，无实际失败条件/一致性测量反证，仅任务库存与数据覆盖|
|08462|潜在：mixed-game结果合理→reasoning/communication仍矛盾→过程与outcome分开，BigFive画像不作内部人格或intent真值|
|08450|潜在：speech固定l2r假定→masked diffusion可调order并比TopK动态→order是factorization选择，量化与decodeorder归因分开|
|08444|拟关闭：已知table graph保row/column/cell+questionPPR重排总体提高，未给新的结构机制/可靠性条件或反证；graph映射章节不足|
|08441|潜在：dense steering entangle→referencefree偏好优化SAE sparse codes→控制接口/稀疏代价，SAE稀疏不保证disentanglement|
|08430|潜在：coarse单rubric ceiling→principle/multimodel aggregation/difficulty evolution细化rubric再RuFT/RuRL→criterion生成与verifiable reward分权；医疗score仅实验范围|
|08406|潜在：webagent文本/fragmented安全分→1226 executable tasks实际page行动判别→framework effect与base模型不同；scalable不授实际风险率|
|08403|潜在：sequence advantage稀疏→semantic segment coalition的Owen-Shapley potential shaping→credit粒度改变；policy-preserving需核assumptions/成本|
|08333|潜在：tool transport被当warrant→formal semanticlaundering/selflicensing条件定理→来源接口与epistemic许可分开；不先采不可消除普遍断言|
|08323|潜在：手工memory流程→atomic CRUD学policy/SFT+RL→maintenance是可学决策；CRUD atomic不授storage transaction原子性|
|08310|潜在：single训练costaccuracy权衡→分budgetRL frontier与onpolicydistill融合→部署可切effort模式；Paretooptimal宣传待核|
|08280|潜在：全action探索→block sparse/contextlinear下OMP recovery+coverage lowerbounds→工具剪枝成立依赖信号/覆盖而非工具规模本身|
|08276|潜在：currenttool语义路由→dependency-rich graph合成多turn、historyaware router→当前历史/依赖是路由输入；开放AgentWeb保证不采|
|08271|潜在：prompt dense policy稳定假定→convex sparse surrogate/PolicyRSC/incoherence lowerbound→klogM依赖是强统计条件而非LLM通用保证|
|08258|潜在：causal题总accuracy→sensitivity/specificity/underdetermined refusal分离发现过拒→abstain与真正安全分账；不采跨模型scalingparadox|

这42初判为29明确潜在＋1决定准入事实含糊待定点＋12具体贡献前关闭。root已实际完整读language20成功18＋agent24成功24并独立校准，27项具体潜在可继续；随后实际必要core定点解除08731/08816/08682的准入疑问，见下述真实事实，不表示Evidence/Books已通过。其余明确负侧未见共通误拒；局部/负面/理论不按规模排除。19935/16224必要日期上界在窗后仍精准隔离，不先assign本窗。只对实际准入者定点日期/最低审阅，不因额外工作降低分母。

决定准入的必要原件：[exact-v1 core](./increment-j15narrowfacts-20261007.txt)。08731 §3.1–3.3是Dreamer/RSSM的demonstration-aligned goal rollout，不仅普通robot curriculum类比；BC占用TVκ、world-modelμ与imagined/expert trajectoryν分条件的理论界直接改变imagined distribution/model error选择，访问阈值不授TV guarantee。root确认WorldModel直接关系，可继续最低必要审阅。08816 §2.1 Eq5–6/§3.3–3.5将curated user/item memory邻居一起批量异步更新，有具体状态更新/消费接口；O(1)仅调用数，不授tokens/write/freshness或隐私，成熟decoupling/batching本身不升长期机制，root已实际core准入。08682固定输入与仅special-token适配的模型迁移对照，反侧是prompt/model条件不可直接转移，而非四条通用经验主题，root准入通过。08477 §2.2及§3.2/4现已读SHA输入确定性建模与MITL局部概率；未建立实际LM观察抽取误差→policy/回复保证运输，回复生成模块仍future work，作者维持具体贡献前关闭待root窄核，不因therapy名称排除。
