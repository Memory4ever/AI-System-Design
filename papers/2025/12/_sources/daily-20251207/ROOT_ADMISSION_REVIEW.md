# 2025-12-07 实际非作者日级复核

2026-10-02，本轮截至19:59:49+08:00；Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`，非作者Gibbs。换日已重读AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES使用说明/每日组、CODEX_RESEARCH_PROMPT、ROADMAP及相关checkpoint。只加载本日WINDOW_REVIEW和原始固定邻接，不读旧Weekly/其他月份池。

## 原始范围与实际访问

窗口Dec6 09BJT至Dec7 09BJT（Dec6 01Z至Dec7 01Z）。逐源审计14源WINDOW_REVIEW及固定恢复记录的分页/停点：OpenAI RSS Dec4 19GMT至Dec8 00/04/06GMT；Anthropic Dec4 17Z至Dec18；Google Blog Dec4至Dec10/DeepMind第3页Dec3；Meta第4页Dec1/Dec12/Nov19；Qwen旧Sep23及空新站有限替代；DeepSeek正确Dec1 API Docs；Kimi26条至Nov7/changelog Nov6；Hunyuan11/11全2026；Z.ai第2页GLM；Seed官方2025首段Dec2/Oct22；ERNIE2/2至Nov7/Dec9；MiMo Paper8和不全More；MiniMax13项/Oct27–Dec23；arXiv四查询及两类首25。只审这些有界入口，未知历史目录不授覆盖/零事件。

不是本复核重新访问全部14目录。OpenAI实际原生RSS在06独立取得的同身份1243项仅重新按本窗判断；其他固定同身份有效原始范围定点复用，不从前日报完成标签复制结论。本日新增原始访问：cs.IR首25原生48018 bytes（总225），cs.PF首25原生52184 bytes（总52），实际逐标题浏览后停止，不翻页扩月。

全部17原arXiv潜在项实际独立完整精确v1题摘：00007、00367、00596、00679、00772、00968、01372、03025、03413、03514、04343、04588、04852、05119、05831、00288、04355。05831网页abs/HTML失败，第一次原生解析依赖缺失不计访问；改用标准HTML parser取得abs38988 bytes并读完整摘要/提交字段。04588题名的toolkit v2不是arXiv版本v2，本次采用04588v1，未误用2026版本。

GLM第18项：Research网页工具失败，原生1397454 bytes以JSON decoder解析RSC对象144，实际得到createAt=2025-12-07T16:00:00.000Z、createdAt=2026-01-07T02:44:32.087Z、updatedAt=2026-04-21T04:48:35.168Z。午夜日编码与迁移不是公开钟点。官方[当前模型卡](https://huggingface.co/zai-org/GLM-4.6V/raw/main/README.md)原生8354 bytes，完整Introduction和Fixed/Remaining Issues实际读，视觉input/output不用文字中转是潜在表示线索；纯文本、overthinking、counting/person-recognition限制保留。不是2025冻结artifact或已验证执行授权。Blog有限失败不冒称访问成功。

17精确v1、GLM时刻及旧目录均真实终态保留；提交/月号/收录/当前卡日期不能补first-public。确定落窗家族0，不是无事件；日期保留不计Evidence/Coverage。PF后窗提交下界只作身份排除，未深审十一项后窗正文，也不否定此前其他渠道发布可能。

## 必要核心与负侧校准

- [SHRAG 00772v1](https://arxiv.org/html/2512.00772v1) §3/5.1.1/5.2：递减关键词OR集合、去重/重排；50查询每条件10次，QSR只至少一个相关文档。保留窄检索取舍，不授答案正确或通用Boolean选择。
- [LORE 03025v1](https://arxiv.org/html/2512.03025v1) §5/6.1–6.2/Table11–12：频率分层cache/distill/实时；实时0.9%是离线估计，pass1 .929→.887而pass8 .937→.964，预算/teacher shift解释不授因果证明。
- [M3DR 03514v1](https://arxiv.org/html/2512.03514v1) §3.1–4.3：翻译/字体/合成query共同条件，单dense与MaxSim不同表示；Figure3的in-batch优于所测hard negatives是局部训练边界，不授universal。作者窄potential正确。
- [UserSimCRS 04588v1](https://arxiv.org/html/2512.04588v1) §4.2–4.6/5：agenda information need和单双prompt停止；每组合100合成dialogue的排名/尺度不同，不等真实用户满意度。
- [AskSafely 04852v1](https://arxiv.org/html/2512.04852v1) §3–5：已知值词典/匹配和人工synonym masking，503问题pattern及single-word例外限制隐私推断；82.5与人工改标91不同label口径。schema限制不证明任意Cypher授权，RBAC自动适配为future。窄payload potential保留，不能授DP/无泄漏。
- [gpuFLOPBench 04355v1](https://arxiv.org/html/2512.04355v1) §3/3.1：clang18.1.3/CUDA12.6/O3、RTX3080 sm86、无fast_math、首kernel invocation及特定CLI，intrinsics/division/CSE/library/runtime值改变executed FLOPs。人工属性分类与编译/运行失败样本有限，预测FLOPs不是代码正确性；未本地运行。

十项原关闭完整题摘实际独立读：00004、00313、02474、02502、03439、04009、04790、07841、03807、04368。普通分层代表00004角色MoE/CTR-CVR应用组合、00313搜索学习问题/意图、03807 Boolean OR/AND/IP数学关系；窄主线贡献不足理由保留，不否定学术价值。07841 A*布局/线程开销不直接建立神经模型runtime约束，局部负面结果存在仍不自动准入。

02502另实际读§3.3/4.4：Geo/Graph/Vector外部数据组合及本域指标未建立新模型机制，窄关闭可保留，不声称从摘要证明无全部边界。04368安全负侧实际读精确v1 PDF III/Algorithms1–2/IV：通用DevSecOps RL/playbook且LLM-assist为future，无当前模型供应链增量；Alg2低impact分支未明确赋execute是伪码静态缺口，不是runtime漏洞，更不授安全机制已实现/安全保证。保留此边界后窄关闭，不把领域security数字当模型安全。

## 精确普通差额5项

仅共同“成熟组合/无边界”理由决定事实含糊的具体集合定点读，不要求所有摘要全文审阅。

| 项 | 实际精确v1核心与准确最小补正 |
| --- | --- |
| 1 | [02474 Q-BERT4Rec](https://arxiv.org/html/2512.02474v1) §3.3、AppendixB Table5、§4.4：per-item融合深度gate区别固定层，有对应质量对照与深度/速度代价。原RVQ/mask组合理由漏此计算选择；保留窄表示/条件potential，不授codec新发明、因果归因或普遍延迟改善。 |
| 2 | [04009 LTCS](https://arxiv.org/html/2512.04009v1) §3.3 Eq1–6、§4.1–4.2/§5.1：分解依query及purchase条件独立；联合ranker共享embedding及leaf→master复用，O(K²)限制只top40。是训练/执行耦合选择，不仅购物域数字；保留窄potential，不授独立假设普适或negative transfer消失。 |
| 3 | [03439 Explainable Reranker](https://arxiv.org/html/2512.03439v1) §4.2/4.4：人评p=.22不证明相等/对齐；较强KG baseline大多收益不显著，对弱base与强base的边际收益不同。撤回成熟SFT/DPO组合关闭，保留评价/成本收益条件，不推所有rerank失败或人类真值已证。 |
| 4 | [04790 WalkRAG](https://arxiv.org/html/2512.04790v1) §3.1/Table1：4/10空间完全正确、6部分；更结构化prompt精度升/fluency降，遗漏步骤；3个错答检索失败。保留窄质量/执行反证，不把“无hallucination”当路线完整正确，不以40问题小样本自动删边界。 |
| 5 | 作者WINDOW_REVIEW和§1/5实际归并四项后更新potential/关闭集合与普通计数；保留原日期终态/不正面证据/Books/无遗漏/具名真实日重开。不新增确定候选、评分或Books采用。 |

## Books 与日级 Gate

实际对读ROADMAP唯一AGENT-TOOL-CALLING Ch78 Tool Contract/typed input-output→proposal/authorization及相邻Ch77 provenance、Ch79 belief/action/observation。GLM native visual serialization并非现有权限段主题相似即覆盖；必要日期与协议恢复后定点评估，仅此时形成采用命题。AskSafely路由Ch72/78、评价冲突路由Ch66，不授现已有覆盖或整合。

暂无新增Books proposal，所有本日潜在项日期受阻，不写正面机制。普通差额5，status进行中、结论未通过；格式校验另记，不代替语义。未改Books/shared state/其他日期，未stage/commit/push。

写后校验：2026-10-02 本轮实际执行07进行中状态V3，退出0，接口一致性通过；语义仍未通过，普通5项不被机器结果覆盖。作者闭合后只定点核四项贡献与正式报告，不重复未变来源。

## 作者差额闭合与日级终态

2026-10-02T20:36:01+08:00；Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`，非作者Gibbs。换日恢复重读适用合同、每日来源、Prompt、ROADMAP及相关checkpoint；实际读取当前WINDOW_REVIEW四项新增行、关闭集合与停点，以及README §1/4/5。仅定点复用本身份上文已实际取得的精确v1核心，不重新访问未变原文，不冒称本轮新全文阅读或运行。

02474融合深度gate/固定层对照及计算取舍、04009共享表示与leaf→master复用/条件独立/top40限制、03439强弱baseline边际收益及p=.22不授相等、04790完全/部分路线正确及精度/fluency冲突均准确归并窄potential，原四项关闭已撤回。正式集合与终态同步一致，第五项报告同步也闭合；普通差额0，21个arXiv加GLM共22个潜在家族、6项关闭，确定落窗分母仍0，不表示零事件。

日级语义结论通过。所有必要日期/历史目录及GLM当时协议保持本窗终态保留，不用于正面证据、Books、无遗漏或性能/安全保证，不计Coverage/Evidence通过；恢复仅需具名精确v1历史new/RSS/email、可核首次正文、GLM当时release/协议或2025目录邻接，只重开真实归属日。没有新增Books proposal，不凭Ch78主题相近授覆盖。旧未通过记录保留为历史，metadata/§6由本次实际结果更新；完成态格式检查随后追加。不改Books/共享state/其他日期，未stage/commit/push。

本次实际执行07完成状态V3，退出0；本日README/ROOT共5个本地链接与尾随空白检查0问题，限定git diff --check退出0。metadata完成，§6独立一行“结论：通过”；机器检查仅确认格式/可判定一致性，不替代上文实际语义复核。07日Gate已完成。
