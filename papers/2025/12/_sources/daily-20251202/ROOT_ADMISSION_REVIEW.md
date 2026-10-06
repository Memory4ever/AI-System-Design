# 12/02 独立日级复核

身份补充：本文件实际复核者为Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`，已从本进程 `CODEX_THREAD_ID` 实核。下文此前记录的chat ID是fork共享的会话ID，不是区分复核者的身份；实际范围与未通过结论不变。

复核会话：`019f44db-4f09-7ee1-8754-b88e0749f3a2`，非作者 Gibbs，非主线程。2026-10-02。原本无本日ROOT文件；此文件为本复核实际新建，不冒称既有root结果。

## 范围与结论

本日独立重读AGENTS、研究/Report合同、每日来源组、Prompt、ROADMAP和WINDOW_REVIEW；相关state检索没有本日checkpoint。窗口 `[2025-12-01T09:00:00+08:00,2025-12-02T09:00:00+08:00)`。14源范围与停点逐项审计，不扩旧Weekly、其他月份或整月论文池。结论未通过；普通补齐12项，确定落窗候选0，外部保留不等于零事件。

来源审计：OpenAI原RSS Dec1 05GMT合作邻接仅支持商业题名关闭，当前403不是零事件；Anthropic SCONE午夜编码不证明精确公开，Dec2 18:58后一条晚于右端；Google Blog/DeepMind原Nov21/Dec3邻接、Meta第4页Dec12/Dec1/Nov19、Moonshot26项最近Nov7及changelog Nov6、ERNIE2/2至Nov7与Nov21/Dec9、MiniMax13项Oct27/Dec23均限制在各入口，不外推全机构。Qwen旧站Sep23/新站及部署有限恢复、Hunyuan All11项全2026、Z.ai两页至Dec7无更多、MiMo8项Paper与无date/More缺失分别保留历史目录缺口。Seed paper/blog首段跨Dec2/Oct22及Dec2/Nov27停止，GR-RL日编码与本窗相交，不能擅自移出。arXiv四主题及三拼写空结果、cs.CV/catchup失败不证明零条；独立成功读取[cs.LG首25](https://arxiv.org/list/cs.LG/2025-12?skip=0&show=25)，仅在这个既有范围内补核。

以上14源全部是范围记录审计；不是本复核全部14目录重新请求成功。DeepMind/Meta、SCONE、DeepSeek、AdvancedIF和受限入口的同身份有效访问只定点复用本会话01实际结果，重新比对02边界，没有复用前日报候选分数/日期结论。SCONE core支持ASR与收益不同；DeepSeek正确API Docs支持工具思考/任务合成，HF createdAt不是公开可见时刻。两者仍隔离。

## 全部8项拟准入校准

独立打开下列官方精确v1完整摘要与版本/评论字段，校准潜在贡献，不声称摘要完成Evidence Gate。提交Nov28/29不是首次公告。

| 精确材料 | 独立判断 |
| --- | --- |
| [2512.00207v1](https://arxiv.org/abs/2512.00207v1) | 容量度量、构造/GD关系与Transformer可用性取舍是真实潜在线索；不等于无限事实存储 |
| [2512.00164v1](https://arxiv.org/abs/2512.00164v1) | 验证查询重用、verifier-optimal解释显式容纳不完备；不是完备安全证明 |
| [2512.00196v1](https://arxiv.org/abs/2512.00196v1) | pullback度量、逻辑运算与rich/lazy边界不能因神经科学分类删除；不外推任意LLM |
| [2512.00181v1](https://arxiv.org/abs/2512.00181v1) | 双轴/层次/关系注意力与label routing、合成因果先验具有具体设计线索，不只表格排名 |
| [2512.00272v1](https://arxiv.org/abs/2512.00272v1) | 预测保持参数对称变换减少unlearning前后差分泄露，潜在安全约束；不采用后续v2标题/结果，不保证隐私 |
| [2512.00342v1](https://arxiv.org/abs/2512.00342v1) | 相关/shift条件下NLS界与meta-LMS漂移，保留受限理论线索，不转成LLM保证 |
| [2512.00351v1](https://arxiv.org/abs/2512.00351v1) | 表格零和Markov game资源界可有潜在意义；admin重叠与ICLR2024说明已核，保持来源关系隔离，不指称撤稿/抄袭。另定点打开[2110.04645](https://arxiv.org/abs/2110.04645)，其MDP sample-burn-in/variance reduction与本项并非题名同一；未做全文原创性证明 |
| [2512.00352v1](https://arxiv.org/abs/2512.00352v1) | 部分覆盖、robust offline value迭代与Bernstein界条件真实潜在线索，不自动外推深度RL/LLM |

另实际访问[Seed原题摘](https://seed.bytedance.com/en/public_papers/gr-rl-going-dexterous-and-precise-for-long-horizon-robotic-manipulation)及[GR-RL 2512.01801v1](https://arxiv.org/abs/2512.01801v1)：noisy/suboptimal demonstrations、offline Q-progress筛选、morphological symmetry和online latent-noise适配是具体潜在训练约束，不采用鞋带成功率作通用可靠性。Dec2日精度/Dec1提交都不能授首公开。作者称另读但未留下ID/实际增量，须补齐可复核记录。

## 同一有界范围的漏记与负侧

下列11项全部独立读取官方精确v1完整摘要。不是新增候选池，均来自作者已声称扫描的cs.LG首25。安全/反证信号全部列明，普通负侧按应用/模型机制/来源重复分层，未以小模型、非LLM、领域题名自动排除。

| 材料 | 实际发现与作者普通补齐 |
| --- | --- |
| [2512.00163v1](https://arxiv.org/abs/2512.00163v1) | LLM自解释与SHAP不一致是必要反证；另读HTML方法与实验段，不能把SHAP本身当因果真值，需记清被解释预测量/遮蔽与不平衡条件 |
| [2512.00170v1](https://arxiv.org/abs/2512.00170v1) | 高维BO中经几何变换的线性kernel反证复杂结构先验默认优势；不是因molecule任务删除，若保留需定点核比较与边界 |
| [2512.00229v1](https://arxiv.org/abs/2512.00229v1) | classifier inversion/exclusion闭环、不用外部OOD集；不能因MNIST删除，也不能将约0 FPR扩成普遍校准，需判断是否有可迁移新约束 |
| [2512.00242v1](https://arxiv.org/abs/2512.00242v1) | polynomial recurrence/diagonal restriction与stalk维数、梯度及内存取舍；需明确与项目长期知识链的新增关系 |
| [2512.00249v1](https://arxiv.org/abs/2512.00249v1) | admin与2408.13333大量文本重叠，实际定点打开[旧文](https://arxiv.org/abs/2408.13333)，同作者2024已述high-level RL/low-level scripts。当前摘要未展示区别，应记录去重关闭或具名修订证据，不能只按wargaming删除 |
| [2512.00251v1](https://arxiv.org/abs/2512.00251v1) | 安全应用负侧：CTGAN+Sinkhorn loss用于DDoS不平衡，摘要只支持组合/本域指标，未呈现新增系统安全约束；可据此贡献前关闭，不把zero-day宣传当安全证明 |
| [2512.00283v1](https://arxiv.org/abs/2512.00283v1) | BioArc架构/tokenization/training交互及架构预测，不可仅因biology排除；需必要设计原则段确认迁移增量 |
| [2512.00293v1](https://arxiv.org/abs/2512.00293v1) | LLM-as-Enhancer而非Predictor、三级alignment/interaction/fusion具有角色边界线索；需记明迁移约束，不只time-series排名 |
| [2512.00303v1](https://arxiv.org/abs/2512.00303v1) | FRL梯度反演必要安全侧；另读HTML引言与method原文，TD梯度同值不确定、state/reward/dynamics priors限制伪解；保留威胁前提，不保证任意梯度泄露均可恢复 |
| [2512.00307v1](https://arxiv.org/abs/2512.00307v1) | signed graph的符号翻转/级联错误/节点依赖改变DP敏感度；需明确保护单位及迁移边界，不以social graph排除或把DP营销当证明 |
| [2512.00311v1](https://arxiv.org/abs/2512.00311v1) | teacher-student-teacher抽取学生解题过程表征；当前题摘主要是KT域中间信号，没有新的LLM系统约束，可具体贡献前关闭，不能仅按education标签关闭 |

普通明确应用层另抽[Seismic 2512.00191v1](https://arxiv.org/abs/2512.00191v1)完整摘要：Sobel几何attention gate+DBSCAN服务地震稀疏标注/连续曲面，未见本项目新增长期机制，窄关闭理由成立，不是领域禁入。IoT energy `2512.00321v1`本复核访问Cache miss，没有独立摘要通过，不计成功样本。首25其他题名不冒称全部深入审阅。

普通待办12项准确含义：11项作者贡献处置记录（可关闭项不需无限正文恢复），加GR-RL精确身份/已读题摘记录。其中含糊可迁移机制仅核必要决定段；潜在准入日期真正穷尽后可安全隔离，不能以未知日期省掉尚未完成的贡献判断。作者应同步§1/§5和WINDOW_REVIEW，不改本复核§6。

## Books、安全与校验

实际对读 `MODEL-FFN` Ch16开头非线性变换与FFN矩阵、Ch15信息选择和Ch17残差/归一化交接。现文未承载本项新容量定理，不能写已有覆盖；不创建重复owner。全部日期受阻潜在线索暂不正面采用，未写Books，未把安全/性能摘要当保证。SCONE/DeepSeek/GR-RL及8项必要日期、旧目录外部保留允许真实终止隔离，不要求无穷恢复历史。

本日semantic未通过；机器格式、链接和diff检查另执行，不替代上述发现判断。

## 十二项补正后的日级结果

复核者：Mill，agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`，非作者Gibbs。2026-10-02T18:52:00+08:00。前述初审未通过及12项发现不删除；本次只复核作者[TARGETED_REPAIR](./TARGETED_REPAIR.md)的受影响项，不扩论文池、不重复有效同身份原始访问。

结论：通过

十二项普通补齐现已处理；11漏记中7项保留潜在准入、4项关闭，另GR-RL身份/增量补齐。对00170/00229/00242/00249/00251/00293/00303/00311及GR-RL复用本复核此前成功的精确v1完整题摘与必要核心，逐项比对补正的贡献/重复及采用边界；不是直接接受作者“普通0”。本次新增独立成功访问如下原始正文：

- [SHAP自解释2512.00163v1](https://arxiv.org/html/2512.00163v1) §3、§4对照定义：被解释函数输出JSON正类概率；250样本、五中心masker、四次排列是受限估计。三任务正类比例不同；特征方向的Pearson阈值对照不等于内部机制或因果真值。反证保留，未授部署充分性或采用效率数字。
- [BioArc2512.00283v1](https://arxiv.org/html/2512.00283v1) §3.4/3.5、§4.2–4.5：独立任务微调/从零训练而非直接用supernet排序；架构次序、预训练与tokenization交互、架构预测的知识库/transfer测试均依DNA/蛋白任务。不是仅凭biology标题排除；目前实际增量是暂缓的AI for Science路线内经验设计规则，通用NAS组合与Agent流程未建立独立迁移机制，贡献前范围关闭合理。未采用25倍宣传或把Agent性能差异当减幻觉因果证据。
- [Signed-graph DP2512.00307v1](https://arxiv.org/html/2512.00307v1) §2.2、§3.1、§4.1及§4.2/4.3敏感度段：node邻接同时改变关联signed edges，不是edge邻接；共享依赖使批次敏感度条件改变。正负子图分离、判别器扰动、受限BFS路径是潜在条件化方案；保留威胁/保护单位，不独立宣称privacy proof成立，不外推LLM token/document隐私。

确定本窗候选0；原8项及新增7项arXiv、GR-RL、SCONE/DeepSeek必要公开归属保持真实外部隔离，不能把submit、CMS日编码或HF创建当first-public。此前有限恢复停点不重新无限探测。关闭项不再借日期留普通判断待办，保留项不获得Coverage/Evidence/零事件、无遗漏或安全保证。Books沿此前实际Ch16与Ch15/17对读，未授容量命题已有覆盖，未正面采用受阻材料；无Books写入。

本次语义通过与完成态机器校验分开：当前§5仅写“外部保留项”，已通知root/Gibbs明确真正“终态保留项/不支持正面证据/定点重开条件”；本复核只拥有metadata/§6，不改§5，暂不授完成status。机器措辞补齐后须实际运行完成态V3再收口，不能把进行中校验代替完成态。

写后实际校验：02当前进行中状态的V3接口一致性通过；01–03共六个README/ROOT文件的本地链接目标与尾随空白检查通过，`git diff --check`通过。六文件当前均未跟踪，故另做了文本检查，不把Git空diff当内容验证。以上不替代语义复核或完成态验收，未stage/commit/push。

## 完成态闭合

2026-10-02T19:06:17+08:00，Mill `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e` 定点读作者新§5，确认已明确本窗终态保留、不用于正面证据/Books/无遗漏与具体恢复归属。普通差额已闭合，不重复未变原始来源或语义复核。实际运行本日完成状态的 `validate_research.py --report papers/2025/12/02/README.md`，退出0、V3接口一致性通过；metadata置完成。外部保留仍不授Coverage/Evidence或普遍性能/安全。前述暂进行中记录是当时真实停点，现由本段闭合。
