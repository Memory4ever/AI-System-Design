# 准入决定处定点补读

完整精确v1题摘由root独核后要求CLARIFY；这里只补决定处，不把这些条目自动变成深审队列。位置为 `V3_BLOCKS_2602.<ID>.md` 内block号，不是文件行号。作者建议待root独立裁决；不以贡献失败替代已成立候选的中心争议。

| ID | 实际必要core | 作者判断及理由 |
| --- | --- | --- |
|21377|31–57，逐词character序列/diacritic+uppercase modifier与identity/context/dictionary三loss|建议EX：成熟character encoder替换，尚无可改变主线的独立新条件。|
|21441|43–86，frozen detector binary image belief、object-conditioned MLLM、beta-mixture contrastive|建议EX：detector+contrastive组合无新独立成立边界；原z已image-only与后do(x)解释不一致，不采用泛causal术语。|
|21497|17–53、58–76，prefix evidence probability/候选knee/mass match、topprob alpha、GRIT decider|待裁：存在可核的有限解码控制器差额，不只是pool名字；Eq10候选外仍alpha*p使总质量alpha+(1-alpha)P(C)<1，不得当完整归一分布。GRIT只接图/尾prefix/候选，不接原question，框坐标不用于评分或crop重编码；需要决定能否仅采用有限proposal/decider接口。|
|21646|16–22、90–101 Table5，文本生成TTS音频/positive self-filter|待裁：text+authentic与text+synthetic同为40BLEU/89COMET，synthetic取自同text仍有增益，支持模态增益不等新增外界信息的反侧；不采独立额外语义信息或泛synthetic替代。|
|21681|32–56，已有Rust repair角色FSM、weighted error waveform/lowvariance TestGen/highvariance rollback|建议EX：成熟反馈/测试生成/回退组合；没有独立新controller条件。|
|21720|23–35，tiny5D/10hiddenLSTM已编码连续numberline+REINFORCE|建议EX：传统数词语言学习模拟，不建立foundation模型能力形成新条件；不因小模型本身排除。|
|21728|33–41，BFS路径/Gemini过滤、subject/relation/object substring奖励|建议EX：成熟process shaping；匹配三词不是顺序连接路径验证，未给新长期credit条件。|
|21786|19–53、55–86，temperature-role tags+ORPO、trained-vs-base及inference tag对照|建议EX：已有control-tag distillation，没有同data tag-free训练/ORPO反侧；局部训后收益不建立新标签条件。|
|21806|15–30、32–70，998 bug-tag issues/两作者taxonomy/API生命周期分布|建议EX：一般API/调度/持久化分类，没有具体新协议失效反例或改变设计边界。serialization实际core39存在但并非v1摘要，原准入理由不得预设它。|
|21833|65–95、193–216、253–281、301；230Java/5轮3prompt、154可用tests/名字逆映射人工修正|待裁，作者倾向EX：naming/comment提示改变microedit稳定速率，readability没实际测量；没有新stop controller，成熟早期收益与反复重写风险不足独立主线增量。|
|21951|15–56、73–75 Table4，candidate discrimination/hard negatives、SFT→F1-GRPO、probe/rerank|建议EX：成熟ranking/discrimination与局部三轴消融；MI探针不建立因果语义或独立新条件。|
|22125|20–46、59–106、121–123，translation关键词metadata一致/IndicNLP替换、parallel321/Ground不平行|建议EX：合理本地化，不揭实际validator错误或新等值盲区；换语言低分/词形约束已有，Ground间差异不等能力比较。|
|21317|22–37、82–95，随机noun检索+图prompt mapping/blending/inversion、禁止context-context边|建议EX：creative RAG既有组合/seed敏感；samechunks flat-vs-graph一般Novelty收益4.38→4.42，主要科学结果暂缓，不推为新长期机制。|
|21814|23–53，carwash单prompt20×6STAR/profile/RAG、scorer词匹配→regex|建议EX：成熟任务分解/提示组合局部消融；不因有限样本本身排除，不采用perfect reliability。|
|21835|26–45、60–73，200video多任务/shot/checklist/judge与V2T→T2V|建议EX：新多任务目录和已知串联信息丢失，未隔离新评价盲区；细粒度反馈本身成熟。|
|22103|26–55、124–130，CPU trace满buffer stall→GPU resident collect-and-analyze helper|待裁，作者拟IN：实际analysis placement避免fine-trace传输/flush停顿，区别于仅统一profilingAPI；若准入只核V-B3成本/扰动，不授passive instrumentation零干扰。|
|22150|17–47、69–80，KV-LoRA/top1 noisyrouter冻结旧expert+usage-ratio辅loss|建议EX：现成LoRA-MoE渐进组合和局部concept/localization表格，不建立独立新condition。|
|21800|84–111，EM/editSim codecompletion比较，92/95/96将Paged/Flash误作丢上下文、111未探索extensivecontexts|待裁，作者倾向EX：对照语义身份失配且已知metric≠功能正确，不见成立的独立主线增量；不把错误制造为纠错Books主题。|
|22136|55–87、129–137，weightstd聚类+KL local混bit/QAT、ResNet shift-add post-synthesis|建议EX：成熟mixed-bit search新proxy拼接及更多Pareto点，无独立新quality/resource边界；17.5%latency反側、非LLM/全硬件保证。|

新增具名CLARIFY21697/21811及风险EX→CLARIFY21950仍属普通待决定core；不得记外部受阻。最终裁决同步初筛表与报告，不覆盖原精确AB证据。

root实际独核后的准入终态：21377/21441/21681/21720/21728/21786/21806/21833/21951/22125/21317/21814/21835/21800/22136为具名EX，原建议及core依据保留。21497与21646为5–6分窄potentialIN（解码proposal/decider接口；synthetic模态增益≠新增环境信息）；22103为6分potentialIN（GPU resident分析位置改变）；22150根据root实际26–45/60–73及Table5改判potentialIN：同空间concept/localization联合反而损部分指标的分责条件，仍须matched预算、staging/router混杂最小核验，非新LoRA/MoE原理。下表原作者建议不是最终处置，以上四项只是准入，普通必要证据/Books判断未结束。

剩余三项决定core已作者及root实际核验准入：21697 blocks76/83–97/120/158–176/210，partial-order next-edit与只看最近hunk错拒h−2关联合法edit、25人注图反侧及额外费用；21811 blocks51–71/147–153/196–227，同policy的局部contact与global表征附加干扰，但输入encoders未参数匹配；21950 blocks32/52–60/Table4，RemoveText/length-matchedRandomText反而提高最终选择，专家文本不等raw image同信息，候选覆盖与最终多选不等同协议。三项5–6分窄potentialIN校准通过；普通命题匹配必要评价和真实owner差额仍待办，非外部受阻或Books终态。
