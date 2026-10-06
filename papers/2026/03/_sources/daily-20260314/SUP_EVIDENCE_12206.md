# 12206 CLASP：必要安全Source与Ch72具体差额/PRE提案

当前结果：root已实际必要Source/owner与逐字PRE通过并窄写Ch72两段/衔接/本人note；mar14_supplement实际非writer完整邻接和note回源POST PASS（SUP_POST_12206.md），root实际回读后同步note/释放。formal53已融入。以下“待审/尚未写”是原提案历史，不是当前停点；不授DAY。

mar14_supplement，待非准备者实际独核；第六窄P及Mar13 arXiv事件日root实核复用。官方exact-v1 HTML GET200/303823B/2026-10-10T01:11:31.190639Z，SUP_NECESSARY_12206.raw/txt与结果。本人实际完整身份/AB、§3.1–3.3全机制、§4 fullTable2/误差、§5–6/Ethics、A全限制、B.1–B.2必要feature身份/B.4 fullcost、D.1/Table7、D.4/Table10关键反側；未遍历C攻击catalog、逐triggerTables8–9、代码/复现或全部统计。精确v1当前无具名撤回/早稿，v2Mar27不自证重要修订，未做版本diff。

## 实际增量与最低评分

普通输入文本或目标Transformer风险probe不覆盖SSM状态污染→在独立Mamba上先读取block-output embedding(BOE)并训练token detector，聚合成document flag后才交给目标消费者→改变入口检查的模型身份/状态观测对象与单位，不能让另一模型无告警即认证目标状态安全。BOE特征接口是新增局部检测机制，XGBoost/独立分类/权限分离成熟原则不另加分。**拟2+1+2=5**（单个检测组件/受测文档负载）；因为现Ch72缺独立SSM-surrogate前端与token/document仲裁的具体长期差额、安全边界，深入必要受影响内容，非全攻击论文。

## 方法身份与评价反侧

§3/B.2：state-spaces/mamba-2.8b-hf单独forward，65输出tensor含embedding层+64block；从独立RoBench25比较Clean/HiSPA/Benign选13维/45(dim,block)值和26blocks×14statistics，共409特征，XGBoost再取200best。预训练BOE包含之前token历史，所谓time-invariant只是分类器没有另外给周边位置特征，不能据此证明不记触发串或无lexicalshortcut。未报告按每个LOO/CCVfold重新选择fingerprint维度；RoBench特征选择使用同类catalog，故没有认证整条feature-discovery对未见结构完全盲。chi²/相关性不认证BOE spike为target唯一损坏因果或全domain数学signature。

2,483résumés三份Clean/HiSPA/同位置Benign共≈9.5Mtokens，Mamba tokenizer；正标签来自注入字符串tokenspan，newline约定负，file有任一positive即malicious。真实目标model是否受损/是否被可靠保护不是每条label的事实判定。file-stratified20%validation/80%training/basefile不两边，15手工trigger LOO与三clusterCCV检查局部泛化；fullset不是unknowntrigger。doc flag=max token风险超过阈值，tokensegment 与document alert不是同一效用。

Table2 bestfullset docF1 .993、LOO .969、CCV3 .8217，不能照录所有noveltrigger几乎无降；D.1 Table7 token .959/LOO .9062/CCV约.78–.81 与doc不能互换。Table2为每setting最优doc threshold，Table7另tokenthreshold，shift下重选不能认证一个冻结部署阈值。D.4 Table10 99%tokenrecall在CCVprecision仅约.8%–10.4%，漏报与误拦不能同时由highrecall标签消失；.99recall不是每trigger每token全抓。原§5/A明确只有resume域、15trigger、static nonadaptive adversary，未有跨domain/跨downstream target实际cleanutility/attackeffect验证；反侧都保留，不据hybrid标题授Jamba/Nemotron已防住。

B.4同100145token测整条BOE+feature+XGBoost，32CPU cores/未具名单NVIDIA GPU得1032tok/s/<4GB，1CPU只有129tok/s，GPU型号/precision/batch等NotDisclosed；这些不含目标model执行/网络tail，不授generic‘negligible overhead’/realserviceSLO。feature训练/统计选择/threshold校准、额外Mamba forward与CPU提取都计费；本论文无false-positive公平性隔离/最终unsafeeffectguard证明，Ethics要求humanreview而非静默丢简历。

## 实际owner差额/PRE

已实际顺读Ch72 936–1012完整CoT→LearnedSecuritySensor→HiddenStateObservationPoint→multitrace交接、697–735输入影响/权限分层，及Ch22 491–518 SSM动态/容量边界；Ch71/73入口明确隔离/production职责。本Ch72已有目标模型白盒probe、多层组合/几何trigger、跨模型direction与reference monitor分责，却未直接承载**另一个SSM扫待消费document的BOE前端**及**token定位vsdoc任一告警阈值/未知结构的校准边界**。Ch22拥有SSM机制，不另讲完整安全pipeline。仅拟在Ch72『Learned Security Sensor 与 Reference Monitor 必须分层』标题后/当前白盒选层段前两段；下文目标内probe保留，不授前端取代它或effect gate。

### 拟逐字两段（尚未写Books）

入口检测还可以读取一个独立模型的状态，而不要求受保护模型开放自己的 activation。面对可能扰乱递推记忆的文档，一条受限分支先让单独的 Mamba 扫描全文，从其 block-output embeddings 提取若干维度与层统计，再由训练过的分类器给出 token 风险；它观察的是前端模型如何响应这份输入，不是下游 SSM 或 hybrid 的真实状态。前端只提交待核的 span 或文档告警，不能把“与下游无耦合”升级为跨模型保护证明，目标模型的效用、状态损坏和最终 effect 仍须独立验收。<!-- source-family:SF-2026-ARXIV-2603-12206 -->

这里还必须分开定位与拦截的单位：token-level 分类尝试找出污染片段，document-level 则只需一个 token 过门即可标记整份文档，两者需要不同阈值与误拒预算。[有限 BOE 前端证据](https://arxiv.org/html/2603.12206v1)显示，未见结构下的文档 F1 仍会下降，强求高 token recall 又可能使良性告警大量增加；按测试切片分别找出的最佳阈值不能直接成为一个冻结部署规则。特征选择、触发族与词法捷径、额外模型前向和 CPU 提取/分类、校准与人审都付成本，简历上的局部检测速度不等完整目标服务的吞吐。域、触发结构或消费者改变且无法重新验收时，保留告警隔离与人工复核、独立目标行为测试和原有 output/action gate，不由无告警批准输入或动作安全。

待root非Source作者实际必要机制/关键table负侧/具体owner/PRE裁决；若判已有论点足够，也须具体指出本文两新增接口实际已有覆盖，不为论文名写段。无SharedBooks写入、不授DAY。
