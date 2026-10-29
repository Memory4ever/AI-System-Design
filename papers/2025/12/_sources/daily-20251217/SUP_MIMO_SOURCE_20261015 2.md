# MiMo-V2-Flash / Dec17补Dec16单篇包

作者Boyle；只本日原研究发布事件，不改旧Seedance6分完整行/日期/旧window/连续§4。用户已恢复，§内评分/owner提案待Newton实际独核；不是已批准Books写入或DAY。

## 1. 真实原发布正文已保存，非动态壳

从RESUME§4已实际定位的iframe `https://mimo.xiaomi.com/mimo-v2-flash/index.html` 本轮一次curl，正常HTTP200/79305B，保存[本日原件](RAW_MIMO_IFRAME_20261015.html)，命令已结束。标准HTMLParser排除script/style后实际完整读可见正文，包括末Technical Report/SGLang/LMSYS出口；[原作者页](https://mimo.xiaomi.com/mimo-v2-flash)明确Introducing MiMo-V2-Flash、December16,2025、当日发布并开源。Newton§9已独立实际核此原件身份/Dec16事件/完整核心说明；不重复该层，不把网页immutable或全部历史字段视为已证。

网页披露GA/SWA hybrid、dense FFN/SWA轻量MTP draft与main-model verify，以及领域SFT/RL teacher→student自身rollout→token级teacher信号的MOPD。现正文与旧release65f0e738必要证据相容；网页Technical Report当前出口不准把2026报告倒填Dec16。声明日期按date-only落补窗，不要求秒/TZ，也不冒全球first。官网首页Paper8/Blog15/More边界沿Newton§6，非全站历史完整性证明。

## 2. 准入、拟评分与必要Source复用

窗口缩小后，softmax仍须把全部注意力分给可见Value→历史release的learnable sink只加归一化分母、不携带Value，提供不强制吸收局部内容的质量分配分支→不能把保持sink等同保留一份历史内容，也不能把hybrid的全部KV说成常数。这是具体attention算子与状态边界，不是只报309B/吞吐排名。

拟 `2+1+2=5`：DD2为归一化/内容状态分责的机制增量，Reach1只按本次主要拟采用attention组件计，不借同一模型另有MOPD/MTP扩大；Durability2为可复用但仍受所测模型/训练条件限制的分支。MOPD/R3/MTP是同family补证/反侧，不另增family或重复评分。最低标准审阅；sink与已有论证实际差额及评测泄漏信号已按必要受影响域深入，不降分规避对照。

旧[MIMO_NECESSARY_EVIDENCE](MIMO_NECESSARY_EVIDENCE.md)明确31页release PDF身份及实际必要p1–9/11–14/18–22/31，Feynman§1–2/Newton§9允许按身份/版本/命题复用。未新下载全报告、全部附录、权重或2026稿，也不声称本轮重新读了这些页。采用边界：

- p6–8 sink进入softmax分母而无Value；32B dense消融不等最终309B MoE全栈受控实验，W128去sink退步/加sink恢复不证明所有window或所有模型普效，regularization仍是作者解释。
- p9/21–22 MTP轻量dense/SWA构造与3层/16K输入/1K输出、batch32–128；acceptance/entropy相关不签发全链吞吐，硬件/precision/SLO等未披露字段保留，不采用网页倍率作普遍保证。
- p13–14/18–19 MOPD为按领域teacher对student实际prefix提供token级reverse-KL，可叠ORM；式7–9的importance ratio/stop-gradient/越界丢弃不是任意teacher logit平均。Table7多域低于best teacher，保留反驳网页全域peak/统一1/50说法。
- p19–21 R3 request-level KV+route避免重复prefill与采样route不一致，不保证同policy、freshness或全链零开销；scheduler/partial rollout与工具quota/QPS另有成本。
- AppendixB未来ground-truth commit污染SWE-Bench镜像，更新镜像和keyword检查不授任意泄漏安全；AppendixC上下文管理收益不证明越少context越好。未复现、未核实现或部署。

旧文件末“无TZ时刻暂缓”和旧无效TRAIN-RL-SYSTEM/TRAIN-DISTILLATION路由仅保历史，不再作当前门槛；当前owner依据下节。

## 3. 实际当前owner与差额（待独核）

实际读Books三文、完整ROADMAP和本日State；本轮实际读Ch22完整262–292、Ch48完整526–550、Ch29完整386–420/570–612、Ch31完整928–952，以及Ch33完整1664–1714。不因全文关键词无命中宣称无所有别名覆盖。

主拟采用差额归唯一 `MODEL-LONG-CONTEXT` [Ch22](../../../../../books/part-02-model/22-long-context.md)：现“Context Anchor从Passive Sink演进为独立状态轨道”完整段讲BOS内容聚合/另设cross-attention anchor，以及后段的结构性sink诊断与normalization干预；这两者都不是“无Value、仅分母的learnable sink”。具体差额是归一化可不把全部质量分给窗口内Value，不能由此恢复被淘汰历史内容；含GA层的hybrid仍有随长度增长的全局KV。可在现结构性sink诊断段后、Conditional Attention标题前窄融一段，不动anchor旧机制。尚未准备逐字PRE/获root锁/写正文。

本次其他具体机制已有承载：`TRAIN-SFT` Ch29多teacher段及Context Distillation完整链已解释student rollout、同一student prefix上的teacher分布、reverse-KL目标/teacher身份/额外前向费；domain-label单teacher还是明确旧基线。`TRAIN-GRPO` Ch33“MoE Route Replay也属于Behavior-policy Identity”完整两段已解释route+router/policy revision、重放、metadata/staleness与失败回退。`INFER-SPECULATIVE-DECODING` Ch48原生MTP段已有head归checkpoint、候选/完整target验证分责。以上只判这些具体长期原则已有覆盖，不声称MOPD所有式/结果、R3的request cache实现或轻量head的全部工程细部已覆盖；其未独立归因实现/性能留报告，不为产品recipe新增段。

请Newton核本family拟5分、必要受影响Source与唯一Ch22 sink具体gap；无需重原31页全部方法。若gap成立，另准备最小逐字PRE交root协调；本包不预签整合/完整Evidence/日级Source或DAY。

## 4. 唯一Ch22一自然段与本人末注逐字PRE（未写Books）

Newton§12已实际通过5分/受影响Source及唯一Ch22 gap；root实际读本包/原版本角色和Ch22 250–306邻接，准许准备最小PRE但未授写锁。当前准确前锚点是以“attention sink还可能不是某个特殊token的语义需求”起的结构性诊断完整段，及其后独立`SF-2026-ARXIV-2605-06611` marker；准确后锚点是`### Conditional Attention 的路由粒度必须匹配执行粒度`及其完整首段。原前段、marker、后标题/段落均保，不改anchor机制。

拟逐字正文（一自然段）：

> 窗口内的归一化还有一条不同于保存内容anchor的分支：加入可学习的sink分数，只进入softmax分母而不提供Value，使本次读取不必把全部注意力质量分给当前可见内容。它不是新增一个保存历史的KV token，也无法找回已经滑出窗口的信息；与global attention交错时，局部层的窗口上界更不能当成整个模型的常数KV上界。[固定发布版的必要对照](https://raw.githubusercontent.com/XiaomiMiMo/MiMo-V2-Flash/65f0e73804b030611b74235ddad9dc4ad1a6a586/paper.pdf)在32B dense模型中显示小窗口去掉sink后退步、加入后恢复，但更大窗口并非全指标更好，不能转授最终MoE或任意长上下文；regularization仍是解释假说，不是统一因果定律。额外参数、训练适配与kernel归一化路径都须计费，并独立验收长程检索和生成质量；历史信息不足、数值实现不兼容或质量回归时，保留原attention、更大窗口、BOS/anchor或显式回读，不由分母的一份质量替缺失证据背书。<!-- source-family:SF-2025-XIAOMI-MIMO-V2-FLASH-SINK -->

拟本人末Review note（一条）：

> - `SF-2025-XIAOMI-MIMO-V2-FLASH-SINK` — Daily `2025-12-17`补Dec16；[原作者Dec16发布](https://mimo.xiaomi.com/mimo-v2-flash)与[固定release65f0e738报告](https://raw.githubusercontent.com/XiaomiMiMo/MiMo-V2-Flash/65f0e73804b030611b74235ddad9dc4ad1a6a586/paper.pdf)必要p6–8，2+1+2=5。只采无Value分母sink/窗口状态分责，保32B dense而非最终MoE、W128恢复/W512非全胜及regularization假说；不采总KV常数、通用质量/速度或全模型安全保证。MOPD Table7/AppendixB反侧保本日报必要证据，不把已有MOPD/MTP/R3原则再写入。Newton§12必要Source/唯一owner通过，逐字PRE、实际写入与POST尚未发生；未核实现或复现。

请Newton实际逐字拟段、完整前后及ownnote PRE，再交root决定唯一窄锁；不是实际正文或POST。当前Ch22无本人写锁，不提前触书。

## 5. root窄锁后实际写入 / nonwriter POST待核

Newton§15逐字PRE通过，root已actual三PRE/必要版本角色与当前完整邻接，ROOT_ADMISSION_REVIEW末三项写前批准授Ch22仅本§4一自然段＋自身一末note。写前本人actual三个文件cached/unstaged numstat均空，未沿旧dirty状态；本次Ch22严格按逐字正文保存，完整前结构性sink段/原独立marker与后Conditional Attention标题/段均未改。自身note仅把审批/实写行政状态更新为已发生，不改Source/5分/边界。

实际保存后完整顺读当前272–302及末本人注/前注，4新增0删，限定diff-check通过。新正文L286与ownnote可交Newton实际POST，须其完整新增/两侧/ownnote回对有效Source，root实际读回后才释放；作者selfread/机械相等不替代nonwriter语义。未预签整合数或DAY，当前此窄锁尚待root释放，不碰其余正文/notes/index。

## 6. 已发生Newton18/root实际POST接纳与释放 / 自身note同步

actual读Newton§18逐项真实POST及root末实际接纳节；root已实际读Ch22完整新增/两侧/ownnote并接纳/释放此唯一窄锁。按用户转交仅同步本人末note的Newton18真实POST/root读回接纳与释放行政状态，不改正文/他注；本人已实际读回末注，限定diff-check通过。此family实际整合1，含Alignment/Meta本日合计4整合，非本日DAY/FINAL；没有待重Source/PRE或本作者Ch22锁。
