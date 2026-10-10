# GER08672：必要Source与owner/PRE请求

exact-v1题名 Learning to Judge: LLMs Designing and Applying Evaluation Rubrics；2+1+2=5，负侧改变rubric可移植解释/可靠性资格而非一般judge不是真值成熟原则；root完整AB/日期已通过。ger-core.json实际完整§3/4/5/Limitations；ger-direct.txt官方必要A.3 L378–418。支持/直接反侧已足，不遍历其余例子附件，不复现。

生成者提出(name/description/scale/instruction)rubric，scorer应用，分别变generation Task-only/Context/Contrastive和scoring zero/few-shot；人类rubric与generated rubric、同model与GPT4o/Llama rubric×多reader交叉，是实际新资格接口。四dataset各50samples、3contexts；5models GPT4o/mini、Mixtral8×22、Llama3.3-70B/Qwen2.5-72B，API不同provider，精确snapshot/hardware/precision/SLO费用/重复运行数量未披露。ScoringT0不认证deterministic；generationT.7/p.9/max512，scoring256，malformed最多3retry后discard，retry/drop人口不能忽略。Unique靠embedding cosine>.82去重，Align由GPT4o tagging human rubric，名称覆盖不是独立人类认可或事实验证。

§4T3内部zero/few agreement与Spearman不同，后者不等absolute agreement；T5独立human-score相关并不全高（GPT4o human rubric SumPubMed.14/.30而USR.81/.82；mini−.09/.06）。Rubric transfer USR Llama rubric Fluency ICC.8138/kappa.4005、GPT4o Creativity ICC.3979；不能说对话全rubric稳定。知识密集SumPubMed Llama Accuracy ICC.0723/alpha.0007/kappa−.0781，GPT4o Terminology ICC0/alpha−.1054/kappa−.1173，支持同model稳定≠跨reader/外部效标。五静态Englishmodel、50sample限制，内部表示“evaluation dialect”只是解释，不是internals/架构因果证明；没有独立fact核验，仅referencehuman标签。生物摘要只作通用judge知识负载测试，不纳入AiScience应用机制。

actual Ch66 1149–1172可靠性段、1156单judge/itemfacet与externalgold边界已读；现有principle承载一致≠真值，但缺rubric生成者×应用者×domain和三类结果分账的资格迁移接口。Ch31 criteriaRewardDAG不是readability transfer；Ch65/67交接已核。唯一owner Ch66，拟接facet段后、average success前一段。尚未root Source/PRE、无Ch66锁，不写；Feb14持锁则等协调，不扩材料。

当 rubric 也由模型生成，评分身份还要拆为判据的提出者与应用者。冻结(name、description、scale、instruction)后，可以比较同一reader跨prompt的一致性，再把相同判据交给其他reader，并另对独立人类或任务效标校准；这三种结果不能互相替代。受限对话/摘要评价中，同模型应用自定义判据较稳定，跨reader和知识密集切片却可明显退化，判据名称与人工rubric重合也只是覆盖线索，不是事实验证或通用可移植性。应保存generator×reader×domain、示例人口、解析retry/drop和各维刻度，分别报告agreement、排序相关与外部正确性。生成、交叉评分和人审增加成本；reader或domain改变而transfer未核时，回退冻结人工rubric、独立事实/任务验证与明确unknown，不用自我一致给judge授放行权。

拟链接exact-v1#S4；末注保50sample/模型协议/Align tagger非truth与不全一致反侧。请求root实际Source/owner/PRE与共享锁协调。
