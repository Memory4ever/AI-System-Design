# Oct11 最后四个最低决定域

作者Kierkegaard，root§22已actual本17完整v1AB/7P4N6C；本包仅四N决定事实，作者2窄P2具体C提案待root，不授日门/score/完整Evidence/Books。四原件HTTP200；09355保存317588、09682保存538797、11728保存245077bytes，15949退出28/partial897209 of1547209，所需正文在截点前可读，不称完整15949/附件。联合输出中段截断后，09682方法/评价及11728算法/评价分别完整补读；HTML坏嵌套带入的其它段落不当“全稿已读”。

## 09355 NL2GenSym：C提案

精确[v1](https://arxiv.org/html/2510.09355v1)/[raw](SUP_DECIDE_09355_V1_20261013.raw)，实际III-B/C/D、IV-D完整TableIII与必要TableII、V限制。Basic/Case KB由官方教程/22functional modules/完整成功案例形成，按执行decision cycles选最优few-shot，Generator用RAG/案例/critic反馈；Critic用execution trace和metrics多维prompt，成功例回灌。这里确实消费SOAR执行结果而不是纯LLM自评，但实际规则仍是成熟RAG+执行反馈generator-critic+最优案例记忆，未建立新的更新/验证规则或受控适用边界；不是因为symbolic/WJP主题或小实验而关闭。

TableIII去critic/KB的Avg.DC均大变，但去不同模块改变信息/预算、又始终保cold-start初始例，不单独证明一般operator贡献。TableII总体Qwen91%但variant90%，不是全成功；V明确非单调、反复迭代额外费用与真实噪声尚未验证。保必要反侧，不授formal证明/全部可执行规则正确或显著泛化；不因成本而抹掉已建立贡献，本最低未建立准入所需新增事实，提案C。

## 09682 GRASP：窄P及安全反侧

精确[v1](https://arxiv.org/html/2510.09682v1)/[raw](SUP_DECIDE_09682_V1_20261013.raw)，实际IV-B/C含Algo1、V-A/D/G完整TablesII/V/VI与VI直接限制。28 OWASP code-level practices经人工MITRE25筛选、LLM pair dependency/去cycle+expert校验形成SCP DAG；specificity与sequential dependency分开。不是仅给security prompt：遍历只有parents已访问、至少一个相关才由LLM给1–5 relevance并更新code，随后最后LLM修功能。提案只依赖消费/选择规则及安全-功能评价分责；expert graph不等真实逻辑证明，最后LLM review不等execution/formal verifier。

Algo1先EvaluateAndUpdate再判R≥τ，文字先相关再apply，保该同版规则差额、不补成安全recipe。w/oGraph将所有practice平铺同时改变结构/overload，w/oReasoning在TableV GPT4o SR.80相同，不能授所有选择单调收益。TableVI τ1/3/5平均SCP30/22.91/6.87、SR.81/.80/.51，和正文28node/最少7口径不同不修。V-D secure-pass@1 GPT4o.47→.58，但Gemini/Claude/Llama下降2/7/9%，提高k另费；CodeQL对应CWE无标记与limited tests共同评估，不代表全部安全。TableII denominator valid可下降，不能用SR提高声称更多全部secure。VI明确小模型可能broken/irrelevant、CodeQL helper+subsetmanual，不授zero-day普遍保证/无需所有标注知识。窄P保当前具体条件，强声明不采。

## 11728 HyperLLM：C提案

精确[v1](https://arxiv.org/html/2510.11728v1)/[raw](SUP_DECIDE_11728_V1_20261013.raw)，实际§4.2/Eq4–8、§5.1–5.2完整Algo1–2、§6.1–6.2及完整Table2。实际实体属性/局部邻接作为prompt，generator提hyperedge、reviewer APP/REJ、remover删边、optimizer以density/diversity发策略；未给新的LLM执行/学习算子或验证资格，主要是成熟多agent生成/审核/删除组合用于hypergraph结构拟合。

理论rank/quality分布在Eq4–8预先指定，概率不以degree动态更新，Zipf-Mandelbrot由这个概率归一导出，不是实证证明LLM有真实preferential attachment因果。算法伪码没有该概率/quality threshold的对应可执行绑定，§6所调attachment与agent persona也不等理论等价。Table2只8dataset结构rank/不同输入NN/DD/SD/attributes，HyperLLM平均2.13不是每指标最优，.85定性拟合不隔离agent新机制；Eq9只有slope差，不是通用质量/隐私/faithfulness。最低原件未建立主线新增条件，提案C，不因graph/theory或篇幅关闭。

## 15949 ATLAS：窄P提案

精确[v1](https://arxiv.org/html/2510.15949v1)/[partial raw](SUP_DECIDE_15949_V1_20261013.raw)，实际§3.2–3.3、§4.1完整Tables1–2、§5.1及Limits。静态instruction与动态analyst/portfolio placeholders分开；每K5decision累积ROI clip映射score，meta更新只静态块，接受门是placeholder集合不变，而非即时reward必须改善。延迟反馈用于序列prompt更新、运行时字段资格不由优化器改写，构成具体局部条件，不凭金融收益/多agent模块准入。

保持placeholder集合不证明语义/权限正确，clip/window不自动低方差或全credit attribution；三资产Apr28–Jun28同2月每天一步、三runs/同backbone、StockSim抽象microstructure，未执行任何订单/交易或提供投资建议。Table2 XOM LlamaROI -.42→-1.10反退，NVDA Qwen235B43.91→41.25退；Table1 o4 DD9.68→11.48可变差，不采§5“consistently”/风险普遍降低。反思与OPRO额外call/优化费用、window参数选择未单独控制，ROI与simulation小人口不能因果签prompt普遍更优；提案只静态-动态接口/延迟反馈的更新资格，不授生产金融安全。
