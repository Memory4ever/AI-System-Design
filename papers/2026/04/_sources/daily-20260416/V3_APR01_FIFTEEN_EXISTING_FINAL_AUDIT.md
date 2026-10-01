# Apr16：15项 Existing 有界独立终核

复核者 apr01，报告作者 apr03/apr02；2026-09-27。实际读取当前 Apr16 README §4采用范围、相关有效独立记录、当前 Books 具体命题及邻接；未变化的13068/13108来源核验直接复用 `V3_INDEPENDENT_FOUR_CALIBRATION.md`，13151复用root有效必要源/owner裁决，不重复附件。其余核心采用点定点重开官方exact-v1必要方法/评价或官方公告，未复现实验、未核整日first-public/来源/全部否定侧，不签日级Gate。

本次判断的对象是**日报明确采用的长期命题**，不是宣称原论文全部算法/benchmark都已在书中。15项在该范围内 Existing 通过，原始受限方法、负例与未证明项仍应留在Report。

| 家族 | 实际来源核对范围 | 当前正文承载及结论 |
| --- | --- | --- |
| OpenAI Agents SDK | [官方公告](https://openai.com/index/the-next-evolution-of-the-agents-sdk/) Native sandbox execution / Separating harness from compute；manifest、外置state、snapshot/rehydration确是官方接口声明，不是跨provider等价证明 | Ch84“AgentRun / Workflow state”表及后续正文分开run/context/memory、runtime状态和Tool/Environment effect；Ch81“Toolspace变大后”分开registry、sandbox interpreter与durable workflow。公告是这一分权的实现案例，snapshot不撤销外部effect。Existing通过。 |
| 13068 | 复用apr02已实际核[PDF-v1](https://arxiv.org/pdf/2604.13068v1) §3.1–3.6/Tables2–4/§7.1–7.6的有效记录，本轮不虚报重读PDF | 实际顺读Ch66“可解码 Failure Direction 不拥有自动纠错权”两段和internal→steering→deployment；probe预测信息不拥有纠错权，固定干预失败不证明所有可控点不存在。Existing通过；不采用统一模型尺度阈值或post-training因果。 |
| 13073 OmniTrace | [HTML-v1](https://arxiv.org/html/2604.13073v1) §3.1–3.2/Algorithm1及B.3：生成token→source unit→span加权；option consistency明确不依赖答案是否正确 | Ch66“Model Self-report不能拥有输入来源真值”实际正文将authoritative lineage、cue intervention和模型sensor分权。93.84% option一致性不证明source truth或因果faithfulness；本文的具体ASR/投票算法不冒称全已写。Existing核心通过。 |
| 13108 FAD | 复用apr02有效§2/3.1–3.5来源记录；本轮实际核Ch75 Context Map/Context Identity与Ch78入口/声明分权 | 导航图保存位置/freshness/provenance pointer，命中后回原文；解析成功与真实代码事实、artifact writer损坏分开。描述器不取代代码authority，观察性session对比不当阅读因果。Existing通过。 |
| 13123 Spectral Entropy | [HTML-v1](https://arxiv.org/html/2604.13123v1) §3定义/§11–12必要反证：经验谱阈值、MLP collapse而无grokking、任务/架构外推未测，相关系数与CI不一致不正面采用 | Ch28“Optimizer也在选择参数空间中的方向尺度”后实有activation covariance/gradient spectrum诊断，SVD/尺度/漂移成本、heldout/noisy fallback、sensor无学习率或停止权。不是以grokking主题自动已有；只该诊断责任通过，不采通用必要性/因果/早停节省。 |
| 13151 Exploration/Exploitation | 复用root已实际核official-v1 §3–7/PDF §4 Eq1/Table1/§7的必要源裁决；不重读同一附件 | 本轮顺读Ch66“表面成功必须与可利用机会和过程轨迹分账”：task outcome、opportunity exposure、action trace与verdict分开；现有完整EvalSpec/input-run身份共同承载暴露分母随策略变化的条件率。不是声称开放环境已实现本文grid规则。Existing通过。 |
| 13304 CLTs for ViTs | [HTML-v1](https://arxiv.org/html/2604.13304v1) §5.2/Table4：ablation在重构的final-layer MLP贡献上，再替换原输出；all-token/CIFAR退步确在表中 | Ch5“解释模型也有自己的Faithfulness Budget”实际要求replacement reconstruction、pruning、未替换路径和原模型intervention分别记录。小CLT图不等原模型唯一知识owner；局部重构/Top4不是所有token不退化保证。Existing通过。 |
| 13321 Orientation | [HTML-v1](https://arxiv.org/html/2604.13321v1) §3–5：同scene旋转的ridge readout，feature替换仍测试预测器；背景旋转影响读出 | Ch5“信息存在、可读与被使用”实际三层命题和独立probe/causal intervention；Ch23模态表示写/读职责作为handoff。方向可读不证明原VLM可以利用或唯一失败因果。Existing通过，不把scene内外泛化混同。 |
| 13348 CONCORD | [HTML-v1](https://arxiv.org/html/2604.13348v1) §2.1–2.3、§4/4.1：owner speaker筛选、metadata/context补全及relationship/sensitivity gate；合成协作与VoxConverse分开 | 实际Ch72 Privacy Gate将recipient、purpose、所有subjects/co-ownership和reference-monitor授权分开；模型推断关系不拥有consent或authenticated authorization。§4.1确同时报告FPR0.8%、TPR99.2%、FNR约12%，但未给能合并这些数值的同分母解释，不能组成单一安全率。Existing核心通过。 |
| 13413 Non-Determinism | [HTML-v1](https://arxiv.org/html/2604.13413v1) §3.2、Tables2/3 caption与§4.4：前者定义每input跨config变化，后者sample Std/SE写固定config跨sample，二者不同estimand | Ch66“平均值、切片与不确定性”实有per-example results、聚类/重复run与采样结构匹配。各config均对前半错后半，则每input跨config variance0而固定config跨sample Std.5；因此不采表中Std为input instability幅度，仍保留具体flip案例。Existing通过，不否定全部观察。 |
| 13759 Cognitive Companion | [HTML-v1](https://arxiv.org/html/2604.13759v1) §4.2–4.4、§6必要结果；probe35样本及另组32/NaN，output_hidden_states提取非总成本为零 | Ch66FailureDirection/internal可读、verbalization、steering与deployment联合分账，Ch72CoT monitor是sensor非authority。检测AUROC不证明guidance改变任务效用，局部小模型/structured task负例仍留。Existing通过，不采用统一并行monitor或零开销保证。 |
| 13927 Compiler Remarks | [HTML-v1](https://arxiv.org/html/2604.13927v1) §3–4/Tables1–2：optimization record与differential testing分别检查变换/语义，手写dependence反馈仅受限改善，歧义可破坏语义 | 实际Ch78“编译器反馈可以前移，但仍是受限Authority”明确诊断、bounded rewrite与functional/security/outcome分权、compile成功不能替代功能验证。当前正文不声称已实现本文precise remark算法；Report可留其反馈质量局部证据，但不采用“瓶颈不是agent”普遍因果。核心Existing通过。 |
| 13954 HINTBench | [HTML-v1](https://arxiv.org/html/2604.13954v1) §3.3/4与C.4：30seed合成629轨迹、first-risk prefix和全轨迹评分不同，prefix安全/不安全recall不对称 | Ch72Containment实际按read→传播→proposal→authorization→commit与security/utility/efficiency分账；全轨迹成功不当执行前检测。合成风险比例不是生产事故率，1000prefix非独立原轨迹。Existing通过，不采普遍guard排行榜。 |
| 13997 Learned or Memorized | [HTML-v1](https://arxiv.org/html/2604.13997v1) §2.4–2.5/§5.4：扰动敏感度与未知训练数据边界；代码仅identifier alpha-renaming | Ch66“污染校正需要主动干预”要求已知注入与未污染counterfactual；没有训练访问只报疑似污染/provenance风险。敏感度既不证明membership，低敏感也不证明没记忆。Existing通过，未把研究全盘判错。 |
| 14004 Memory Transfer | [HTML-v1](https://arxiv.org/html/2604.14004v1) §3.1.1–3.2/4/AppendixB：目标benchmark排除、不同memory类型与query策略，pass@3、负迁移及rerank成本保留 | Ch77ReasoningBank和“子问题—过程检索”实有episode→procedural策略、适用范围、derived索引及原轨迹回退，memory不可升级workflow policy。具体跨域有限收益不证明所有原轨迹无用，本文完整embedding实现不称已有。Existing通过。 |

## 本轮13348访问判断的纠正

工具首批片段未完整展示§4.1时，复核者曾错误告知root该locator/三数不存在；随后定点find/open已实际恢复§4.1原句，上表才是最终结论。已同步root与apr02取消删除要求。该失误不能成为日期/版本隔离依据，不修改正式日报或Books。

15项采用核心Existing在当前实际Books有承载；仅现有命题充分，不要求为论文名产生diff。范围之外的原文细节不转为已验证事实；这里没有验收Apr16日期/14来源、全部89候选、否定侧或日级Gate。
