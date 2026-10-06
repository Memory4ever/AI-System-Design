# 2025-11-11 尾批有限题摘裁决

作者Noether。实际检查时间2026-10-04T19:05:30+08:00。窗口`[2025-11-10T09:00:00+08:00,2025-11-11T09:00:00+08:00)`。原月表skip200/show50仅标题查漏，选20项完整exact-v1题摘；定点日期query另外发现4个相关身份，均已读完整v1题摘。不是24个已确认本窗事件，不把月表或submitted变公开池，不扩全附件/owner队列。

原完整题摘保存在[AB1](nov11-tail-ab1.txt)、[AB2](nov11-tail-ab2.txt)、[AB3](nov11-tail-ab3.txt)、[AB4](nov11-tail-ab4.txt)、[AB5](nov11-tail-ab5.txt)；04715的web失败响应不算已读，随后取得[原v1 HTML](04715-v1.html)并实际读取完整摘要。新增四项原题摘见[NEW4](nov11-new4-ab.txt)，发现query见[日期/身份线索](nov11-tail-finalproof.txt)与[原header](nov11-tail-new-hits.txt)，header本身不算摘要审阅。

下表日期均为原submission history UTC，**不是public**。贡献明确的保留潜力，真实日期缺口终态隔离；最小重开为对应精确版本官方首次公开记录/公告或完全落窗的首公开上下界。若已早公开，须另有本窗实质变更和真实公开日期，版本号变化不足。不以索引Published、周日schedule或后来的会议日期授归属。暂不对日期保留项列正式候选或最终评分，首包原拟评分不变。

| 原exact-v1身份 | submitted原字段（UTC） | 约束→实际增量→需重审的选择 / 作者有限处置 |
| --- | --- | --- |
| [04654 LEASH](https://arxiv.org/abs/2511.04654v1) | 2025-11-06 18:43:16 | 固定CoT预算浪费→entropy斜率和top-logit margin双平台停止→推理质量/成本控制。原摘要明确10个百分点accuracy下降，不写无损；潜在，日期隔离。 |
| [04688 Ordered Procedural Steps](https://arxiv.org/abs/2511.04688v1) | 2025-10-25 23:37:00 | 静态答案分数遮蔽步骤顺序→Kendall Tau/NLCS/NED及长度/移位条件下退化→保留局部顺序推理评价证据，不外推所有规划；潜在，日期隔离。 |
| [04689 ATLAS](https://arxiv.org/abs/2511.04689v1) | 2025-10-26 03:54:12 | 静态全题成本→IRT/Fisher信息自适应测试→评价预算/排名有效性取舍。负item discrimination不直接等于标注错误；潜在，日期隔离。 |
| [04694 Instruction Ladder](https://arxiv.org/abs/2511.04694v1) | 2025-10-30 22:13:31 | 隐式指令优先级难验证→ReasonIH/VerIH与可验证冲突训练→控制遵循和安全的条件。部分攻击成功率反向，必要反侧已读；潜在，日期隔离。 |
| [04700 WinnowRAG](https://arxiv.org/abs/2511.04700v1) | 2025-11-01 20:08:13 | 检索分歧污染上下文→query cluster、agent回答/critic迭代prune和merge→检索质量/调用成本；不只按RAG组合名称准入，潜在具体筛选机制，日期隔离。 |
| [04703 Construct Validity](https://arxiv.org/abs/2511.04703v1) | 2025-11-03 17:39:40 | benchmark分数与构念不等价→29人审445项所发现的具体task/metric盲区→评价论证。保留实证方向，不把八条成熟建议本身当新增机制；潜在，日期隔离。 |
| [04715 Influence Estimation](https://arxiv.org/abs/2511.04715v1) | 2025-11-06 00:47:07 | 全模型influence昂贵/会相消→中层attention与rank/vote聚合、免retrain的Noise Detection Rate（NDR）评价→估计器成本及可靠性；不授语义因果真值。原v1完整摘要已恢复，潜在，日期隔离。 |
| [04754 Surprisal Scorers](https://arxiv.org/abs/2511.04754v1) | 2025-11-06 19:07:09 | 单scorer泛化多样性排序→caption n-gram与通用LM scorer可能反转human/model差距→局部评价负证据，不按caption应用自动关闭；日期隔离。 |
| [04800 ERPO](https://arxiv.org/abs/2511.04800v1) | 2025-11-06 20:40:27 | 零reward variance使GRPO数据无信号→残差历史tracker与all-correct prompt温度探索→sampling/学习信号成本条件；潜在，日期隔离。 |
| [04869 Semantic Calibration](https://arxiv.org/abs/2511.04869v1) | 2025-11-06 23:14:45 | token likelihood与答案正确率不同→语义等价类Bcal局部最优条件及RL/CoT破坏校准→置信度解释。定点query的Apple官方页显示March2026，不用于Nov首公开；潜在，日期隔离。 |
| [04875 Behavioral Self-Awareness](https://arxiv.org/abs/2511.04875v1) | 2025-11-06 23:28:16 | 统一self-model假设→rank-one LoRA/steering的领域局部行为改变→局部能力诊断，不证明意识/全任务自知。v2 submitted Nov10 01:27:05原摘要与v1相同，未识别实质新机制，不凭版本号加事件；日期隔离。 |
| [04919 BudgetMem](https://arxiv.org/abs/2511.04919v1) | 2025-11-07 01:49:22 | 长上下文成本→**学习**选择性gating加实体/TF-IDF/话语特征与BM25→记忆预算/质量；v1不是training-free，实验700QA/5–10k上下文不证明100k–1M范围。潜在，日期隔离。 |
| [04952 LoPT](https://arxiv.org/abs/2511.04952v1) | 2025-11-07 03:30:34 | 并行分片破坏sequential token边界→字符位置匹配与动态chunk merge→tokenization correctness/成本。lossless依赖原证明条件，不由标题保证；潜在，日期隔离。 |
| [05018 PBSuite](https://arxiv.org/abs/2511.05018v1) | 2025-11-07 06:43:01 | 单轮遵循高分→300政策、动态多轮压力测试→组织政策持久性评价盲区；不是普通流量84%失败，judge/过拒绝/无tools边界已核。潜在，日期隔离。 |
| [05064 OLA/TOA](https://arxiv.org/abs/2511.05064v1) | 2025-11-07 08:18:58 | adapter跨模型需再训练→order-level attention共性与已训练adapter迁移→表示/迁移成本。transfer无参数更新不等于初始adapter免训练；潜在，日期隔离。 |
| [05085 Layer-wise Distillation](https://arxiv.org/abs/2511.05085v1) | 2025-11-07 09:00:26 | 任意删层→迭代影响评估及KL/MSE恢复→局部深度压缩边界。Qwen2.5-3B 36→28层质量-9.7%、24层-18%，不写无损；潜在，日期隔离。 |
| [05162 MGSM correction](https://arxiv.org/abs/2511.05162v1) | 2025-11-07 11:30:10 | 语言能力差距混入翻译/解析误差→纠正MGSM和answer parsing→强模型特定任务差距缩小。共享LLM纠正/评价与可能污染不能证明所有语言差距消失；潜在负证据，日期隔离。 |
| [05184 CoT Distillation](https://arxiv.org/abs/2511.05184v1) | 2025-11-07 12:05:39 | teacher CoT不自动改善student→white-box BBH对照中task-specific收益/退步→蒸馏迁移条件。已读原表，尚未授matched token/training budget；局部验证/负证据潜在，日期隔离。 |
| [05408 Weight Arithmetic](https://arxiv.org/abs/2511.05408v1) | 2025-11-07 16:34:16 | steering对OOD及fine-tuning drift脆弱→对比fine-tuning delta/weight监测→干预/检测边界。原监测只三域小型controlled setup，无实用precision保证；潜在，日期隔离。 |
| [05516 Ming-UniAudio](https://arxiv.org/abs/2511.05516v1) | 2025-10-26 17:55:34 | 分任务speech表示阻碍联合理解/生成/编辑→连续语义+声学token统一并免timestamp指令编辑→多模态表示/生成语义；不采榜单为保证。潜在，日期隔离。 |
| [04707 NINJA](https://arxiv.org/abs/2511.04707v1) | 2025-11-05 01:12:50 | 长上下文能力不授安全保持→良性相关上下文与goal位置使ASR/NRR分离→上下文安全评价条件。必要core已核，不授任意模型脆弱或总成本最优；潜在，日期隔离。 |
| [04981 Deep Progressive Training](https://arxiv.org/abs/2511.04981v1) | 2025-11-07 04:56:45 | 深度容量/训练compute冲突→零/一层起步渐进增深的初始化、超参及扩展时机→训练预算选择。不把GPT2近同loss外推通用5倍加速；潜在，日期隔离。 |
| [04898 AgileThinker](https://arxiv.org/abs/2511.04898v1) | 2025-11-07 00:51:02 | 推理时环境仍演变→reactive+planning同时运行→深度/响应时效取舍。局部gym方向不授真实系统SLO；潜在，日期隔离。 |
| [05313 Compress & Attend Transformer](https://arxiv.org/abs/2511.05313v1) | 2025-11-07 15:13:28 | 固定efficient-attention牺牲recall→压缩chunk+dense attention、多chunk训练后测试时调整→模型状态/质量内存可控。与Meta Carbon Aware Transformers不同家族，不能因CAT缩写归并；潜在，日期隔离。 |

## 决定性有限补读，不生成全实验队列

06441原方法/表已读：[routing核心](nov11-tail-core2.txt)、[Table3/4及成本争议](nov11-tail-narrow-stop.txt)。TF-IDF/BERT对Always-Premium相似度不是正确性oracle；96/4与72/28调用占比不能混合；正文约1/3成本与Table3 MMLU70%/VQA68%、fine-eval42%不一致。Table4 premium28%查询占70%成本，不由4%叙述抹掉。保留局部classification/routing取舍潜力，**不采用这些聚合成本/质量保证**；未因成熟router原则自动关闭。硬件、端点版本、precision、输入输出长度、batch/concurrency/SLO为Not Disclosed。日期仍只有submitted，恢复后只核该命题必要可比配置，不展开全附件。

05184 [原表续读](nov11-tail-new-hits.txt)：Llama2-7B average baseline39.44/KD39.22/CoT41.50、teacher49.95；tracking objects、word sorting、time sequences中存在CoT相对普通KD退步。表头/紧邻标签需精确绑定模型，不能拼Qwen/TinyLlama行或把overall均值当全部任务收益。未读预算不授因果/相同成本，只保留局部反证方向。

所有原已读证据留存，潜力不因日期失败缩池。未来v2/后续稿只定点核版本/修订信号，不回填本日；04875对比见[原v2摘要](nov11-tail-narrow-stop.txt)。其余完整methods/代码/复现未读、不算Evidence完成。普通20题摘及06441小段现已处理；后续只有来源持久化/正式报告和必要局部独立校准，不等待Books或全附件。
