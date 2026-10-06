# July11 necessary N core screening

范围：root 指定的 12 个 N 身份及追加 GUIDE 2507.08870v1，共 13 项；仅决定准入。重读 AGENTS、当前 RESEARCH_CONTRACT、REPORT_CONTRACTS、CODEX_RESEARCH_PROMPT、RESEARCH_SOURCES 使用说明/每日组、ROADMAP、July11 README、当日 root screen 与 exactRoot 题摘。新增窗口 2025-07-10 完整自然日；原窗口和旧候选不迁移。submitted、HTML 页眉日期均不证明首公开日；不追 hours，不使用 catchup。

P=实际增量足以继续核验，首公开日仍未知，不是本窗正式候选；C=必要 core 已支持贡献关闭。未读正文是普通工作，不是 external。仅日期未知的明确 P 在此停止，不展开 score/general Evidence/Books。原件命名 `SUP_A11_NCORE_<ID>v1.html`，相同 stem `.html.request.json` 保留请求状态，`.txt` 是派生定位文本；全部保留，不覆盖已有原件。精确 v1 HTML 优先，必要时 PDF fallback。

## Batch 1: 3/13 已决定

| 身份 / exact v1 原文 | 实际读到的 section | 原文实际新增 | P/C 与具体理由 | 未读与采用边界 |
| --- | --- | --- | --- | --- |
| [2507.06335](https://arxiv.org/html/2507.06335v1) | §3.2.1 方法/基线/Table1，§4 unified sketch，§5 | 固定 WAC 分类器系数与可学习文本 embedding 共存；ELECTRA-small 同训练数据比较 concat/add/mult：concat 不改善、add 退化、mult 改善。§4 保留分类器概率进入 attention 是尚待实现的 sketch。 | **P**：不是仅 WAC 综述或泛称 grounding 有益。实际局部反侧是视觉系数与文本表示的融合方式决定收益方向，足以重考“补视觉表示就改善”的选择；拟路由 MULTIMODAL-REPRESENTATION。 | 未遍历 §2 认知综述/§3.1形式语义；未核复现、统计/超参公平性。concat 修改模型超参，不能把 Table1 当普遍算子优劣或已完成神经符号架构；公开日未知，仅潜力。 |
| [2507.06396](https://arxiv.org/html/2507.06396v1) | §2 PDL 双通道 result/context、typed parser/constrained decoding；§3 Case Study/Fig2–4 | Think 分为自然语言与 ActionSpec 两调用，再加模型特定 parser；同 models/tools 的 ITBench 例将未调用工具失败与总任务成功分开。 | **P**：不是凭 declarative DSL/API 新名准入。小模型同次输出 Thought+JSON 造成语法/工具名失败，拆调用/解析适配提供具体执行有效性条件；拟路由 AGENT-TOOL-CALLING。 | 未核 Fig 图像数值/完整约200次样本与预算；两阶段及 parser 同变，不能单独归因语言或拆分，也不外推 4x；不验代码/安全部署。公开日未知。 |
| [2507.06427](https://arxiv.org/html/2507.06427v1) | §3.1–3.3/Fig2/Table1–2，§4.1–4.3，§5.1–5.3/Table4–5，§6 | SAE 特征映射数学类别或由辅助模型识别 literal/metaphorical 混淆，选择性触发解释/补充；数学 rewrite 另经 Gemini 等价检查，metaphor 不改整句而加目标词语义。 | **P**：内部特征不是仅事后可视化，而进入输入干预触发；符号/函数和 literal sense 的具体错配给出可核失效路径，拟路由 WORLDVIEW-REPRESENTATION。 | 未读附录训练/统计、未复现或核全部样本；原文 Original/Enhanced 不隔离 SAE 触发、GPT-4知识和新增提示的各自收益，不能宣称因果解释或所有歧义自动可修。标注争议仅保留线索。公开日未知。 |

## Batch 2: 累计 6/13 已决定，5P/1C

| 身份 / exact v1 原文 | 实际读到的 section | 原文实际新增 | P/C 与具体理由 | 未读与采用边界 |
| --- | --- | --- | --- | --- |
| [2507.06520](https://arxiv.org/html/2507.06520v1) | §3–4，§5.1–5.3/§6.1–6.2，Appendix B.3/B.4/F.5 | capacity 提示/dispatcher 拒绝、token/turn cap、失败写 scratchpad 后 retry/replan、流式 tool launch；另报告 20%随机 tool 故障注入及重规划收益。 | **C**：实际容量/恢复仍是已有 admission/iteration cap/error-feedback 组合；故障注入也未区分新增失败类型、恢复一致性或适用阈值，只验证启用已知 retry/replan 比禁用有益。不是按 MCP/GAIA 名字关闭。 | 未核代码、A隐私实现和完整 F 参数曲线；没有宣称无安全风险。§5 baseline 工具/模型不同，§6 33-task single-thread 是另协议，不能合并为新调度语义。日期未知但关闭贡献不另追日。 |
| [2507.06554](https://arxiv.org/html/2507.06554v1) | §2.1–2.3/Fig1–2，§3两case，§6，Appendix A Eq2–23 | 所有待比较 retriever 召回结果并集生成 pseudo-GT；共同遗漏 FN_res 在理想同一标签全集下保持 precision、使 recall 同倍率改变；minimal facts 去除跨chunk重叠造成的伪漏召回。travel组件有 rewriter/filter/reranker 非叠加反侧。 | **P**：具体低成本相对评价条件和 segmentation 计数盲点，不是仅自动标注+subset新名字；拟路由 PLATFORM-EVALUATION-SYSTEM。 | Appendix A只支持固定比较集、同一事实空间/正确标注及非零分母的相对recall，非absolute recall或未入池新retriever。未核所有图/附录配置和 PR-AUC 结论；不能把理想证明直接套LLM生成事实。§6明确未处理 unanswerable queries；公开日未知。 |
| [2507.06564](https://arxiv.org/html/2507.06564v1) | §III-A/B/C/Fig2–4/Eq2–6/Algo1；§V-A–D/TableI–II | 九sector坐标细化 landmark 描述；历史 landmark/instruction 图提供最短路径回溯与澄清，在无landmark连续指令中避免重复动作；控制端消费状态/障碍轨迹，NMPC非LLM直接控电机。 | **P**：有具体“粗视角词不足定位/无landmark会重复动作”的输入失效与历史参考干预，不只是 VLN+NMPC 主题映射；拟路由 MULTIMODAL-EMBODIED-VLA。 | NMPC/PANOC属借用机制，非新增贡献；未核平台/完整传感接口或真实飞行。仅模拟且AirSim提供障碍状态，不认安全保证。TableII有SPL高于SR的表面不一致，需核指标协议，不采用性能定律；公开日未知。 |

## Batch 3: 累计 10/13 已决定，8P/2C

| 身份 / exact v1 原文 | 实际读到的 section | 原文实际新增 | P/C 与具体理由 | 未读与采用边界 |
| --- | --- | --- | --- | --- |
| [2507.06622](https://arxiv.org/html/2507.06622v1) | §3.3–3.4/Algo1，§5.2–5.3/Fig4–5/Table4，§6/§8 | 原 concat-then-project/等权改成各模态先SVD、各自维数及可为0的权重联合BO；低维不是统一损失曲线，Hate Speech上高维concat更好；KG无映射率和投影预算不同。 | **P**：具体资源受限下“先融合再统一压缩”与“分别压缩再选权重”的取舍/失败边界，不是凭六dataset或BO名字。拟路由 MODEL-EMBEDDING。 | 未读全部 end-to-end表/§4预算/实现/抽取器附录；权重不是因果模态重要性，无显著均值差异不可说KG普遍更弱；50搜索/低维集合、AutoML及KG抽取成本不授端到端省钱或新域迁移。公开日未知。 |
| [2507.06715](https://arxiv.org/html/2507.06715v1) | §2.1–2.3，§3.1–3.3/Table1，§5 | section-first递归chunk、同patient/visit元数据过滤、global→note-type local检索、hybrid/rerank/dedup及前次visit summary。Unlabeled内容保留为More Information。 | **C**：实际仍是结构chunk/分层检索/来源与时间过滤成熟组合，实验未提出新的检索成立条件或独立可复用失效机制；未按医学名关闭。 | 已实际核 deterministic/safety信号：跨模型section齐全或embedding相似不证明同输入重复输出确定性/事实正确；Table1 Mistral Generated 0.8248低于Gold 0.9126，不能照录both outperform。这是本文采用限制，不把作者过度宣称凭空提升成新机制。未核图/代码/临床安全，不作医疗建议；日期未知不追日。 |
| [2507.06774](https://arxiv.org/html/2507.06774v1) | §2.2，§3.1–3.3，§4.1–4.4及Table1–3/§5关键结果 | instruction/response各抽concept，再用一侧全文+另一侧concept双向生成动态描述checklist；checklist英语，最终judgment仍吃原语言以限制translation bias；pairwise各候选独立checklist，不是固定打勾加权。 | **P**：准入限于双向半盲的信息组织及原语言最终判断这一具体评价替代机制，而不是multilingual prompt移植或接近GPT-4o榜单；拟路由 PLATFORM-EVALUATION-SYSTEM。 | 未核附录图中的prompt、blindness/translation消融、成本与显著性；不存在已证实新blindspot的断言。§4.3 pointwise/pairwise指标描述与任务/表题有交换，需未来澄清，不采用总榜可靠性结论；公开日未知。 |
| [2507.06795](https://arxiv.org/html/2507.06795v1) | §3，§5.2.1/Table5，§7，Appendix A/Table7–8/Fig6说明 | 固定约3B token/Exaone2.4B比较5/10/25/50/75% pseudo-replay：general趋于饱和，domain收益更早下降；原预训练数据未知使pseudo-replay匹配受限，full pipeline另含SFT/DPO。 | **P**：不是仅“DACP提高行业指标且保general”。实际ratio sweep给出总预算内general保留与domain摄入相互竞争的局部条件，并限定小配置到full训练迁移；拟路由 TRAIN-PRETRAINING。 | 未核所有full模型/finance/RAG应用和附录超参，非50%普遍最优。Table7 base general均值仍高于50%结果；Table8 chat分类在50%显著降低；不把avg接近写全部能力保留。batch/context预算变更及SFT/DPO混杂未独立归因；公开日未知。 |

## Batch 4: 累计 13/13 已决定，9P/4C

| 身份 / exact v1 原文 | 实际读到的 section | 原文实际新增 | P/C 与具体理由 | 未读与采用边界 |
| --- | --- | --- | --- | --- |
| [2507.06803](https://arxiv.org/html/2507.06803v1) | §4.1.3属性/块评价核心Eq10–13；§5.1 code skeleton/comments、§5.2.1函数模板；§6.1–6.3/Table4–7；§7限制 | SysML块/属性/关系生成类结构；人工 equation template库按cosine检索填参，缺参默认1并告警；分层属性匹配评价将零属性块另算。单pendulum与Copilot比较后者错填参数。 | **C**：实质是已有结构IR、模板匹配/参数填充及局部抽取评价组合；空属性块不混入属性分数防止空项抬分，是任务评分拆分而非新的模型验证或执行保证。没有新的接口一致性/因果完整性规则；不是因SysML或物理词关闭。 | 已核代码生成反侧：Copilot收到skeleton但参数上下文是否一致未立，不能从错填1m/1kg证明模板普遍更准确。§7明确复杂组件接口/因果语句未完整建模；未读全部NLP pipeline/图/附录/代码，不授“LLM validation”等于验证正确性。日期未知不追日。 |
| [2507.06909](https://arxiv.org/html/2507.06909v1) | §3.1–3.3/Fig2/Table2，§4.1–4.3，§5/Table3–4，§6.1–6.2 | 多人/多charge保留到样本，四场景预测charge/penalty；比较按任务fine-tune、多任务、zero/fewshot。 | **C**：实际未比较同一case“拆被告/charge独立推理”与“保联合依赖”的执行设计，四场景还同时变化事实长度/charge数/penalty分布，不能据复杂场景降分形成具体推理分解失效条件。多任务对照仍是该预测任务的指标组合，无新训练机制或controlled泛化条件。 | 已核负面/评价反侧：Table3 InternLM2 S4 LogD 56.5低于S1 59.3，与“更高2.8”文字相反；Table4多任务penalty改善而charge常下降，不支持全指标统一更差；§4.3 exemplar从test检索，排除当前query/label泄漏未明确。不作法律建议或安全保证；未读附录prompt/代码及独立抽样，不因dataset名字关闭；日期未知。 |
| [2507.08870](https://arxiv.org/html/2507.08870v1) | §3.2–3.4/Fig1–3/reward，§4.1–4.5/Table2–5/Fig4文字，Limitations | 按abstract/contribution/method/experiment分库压缩；R1 warm-up后RAFT对齐human rating/review；同RAG协议比较backbone，固定retrieval对比rubric；rating classifier熵筛低熵10/20/30%，子集内再取rating top30%。soundness-only各backbone均降分，实验setup补充不总改善。 | **P**：不由7B胜R1单leaderboard准入。实际补读得到selective evaluation的coverage/ranking双门、rubric与评价代理的反侧及上下文信息不必单调有益；这些是LLM evaluator有效性条件，拟路由 PLATFORM-EVALUATION-SYSTEM，不采用自动科学发现应用路线。 | 1000个ICLR2025 test/319 accepted是§4.1口径。93.3%是最低熵10%子集再top30%，约全体3%（本表据协议计算），不是全体准确率或校准保证。classifier entropy非独立advisor可信度；accepted非科学正确性；未核Fig4像素/阈值选择泄漏、classifier训练独立性、全部附录/复现。摘要/方法压缩与可容纳文献数量同变，不授单独压缩因果收益；公开日未知。 |

## 交付与核验边界

13/13必要准入判断已交付：P为06335、06396、06427、06554、06564、06622、06774、06795、08870；C为06520、06715、06803、06909（均2507前缀、v1）。此清单是本侧支判断，不重算root整池。

全部13项实际取得HTTP200且有ltx_document的精确v1 HTML，没有启用PDF fallback；原件、请求记录和定位文本保留。所有P在公开日未知门停止，不记当窗候选、score、general Evidence、Books或独立通过。C也保留必要core中的负面/安全/评价矛盾，不因日期不明另追日期。没有尚未处理的本侧支准入N；表列未读仅是未展开的后续证据边界，不伪装外部阻断。

已分批通知root协调Ptolemy独立校准；本作者未直接取得Ptolemy独立结果，不认领验收。08034未纳入本侧支；没有发现足以据此推翻其API/calculator成熟组合关闭的共性依据。06622/06795等提醒是“成熟组件也可能有实际budget/失败边界”，不是要求重开所有同主题条目。

写入范围仅本表与SUP_A11_NCORE_*材料。没有修改Report、Books、LEARNING_STATE、index或其他作者文件；未stage/commit/push，模型设置未改。
