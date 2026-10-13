# 第三批：既有相关标题完整AB/日级字段

resume_mar17，本20补03/19，仅已发现相关4题。exact-v1完整官方题摘/currenthistory已读，不采用摘要数字/Evidence。四exactDOI官方DataCite真实HTTP200：17809 created03/19T02:41:04Z registered05Z；17771 created=registered02:40:11Z；17683 created02:38:05 registered06Z；17280 created=registered02:28:25Z。Submitted03/18只用于发现，沿已核官方ID不预发/公告最早03/19BJT08至登记上界，同日级夹证不造确时。现未独校/评分冻结。

- [QIG17809](https://arxiv.org/abs/2603.17809v1)：modality级粗校准无法捕获跨token敏感性→Quantization-aware integrated gradients逐token量化校准→需要重新比较跨/内模态token权重与校准成本；不是因名称quantization自动准入。拟2+1+2=5，仅局部表示校准，必要Source再核归因与granularity控制。CVPR2026accepted信号定点官方[CVF正文入口](https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_Fine-Grained_Post-Training_Quantization_for_Large_Vision_Language_Models_with_Quantization-Aware_CVPR_2026_paper.html)同九作者/完整AB身份、bibtex monthJune2026；录用不是窗前正文信号，不拿相似FPTQ旧题作同稿。原v1唯一，无当前撤回纠错说明。
- [Attention Sinks Induce Gradient Sinks17771](https://arxiv.org/abs/2603.17771v1)：旧forward sink/大激活相关关系未区分中介→causal mask backward梯度集中与V-scale的value路径干预，保持attention sinks却抑制massive activations→需要区别forward相关与training-time媒介。拟2+2+2=6，形成/推理异常衔接而非吞吐分数。必要§5.1纠正准入笔记原“只改反传”：实际φ(r)v同时改变forward value与backward Jacobian，Q/K的同次权重不变不等整网forward不变，不能授纯反传因果隔离。当前v2 May6题名增加Massive Activations as Gradient Regulators，不能仅改名推出重要修订；必要只按当前具体说明核受影响，不展开全部版本。
- [Sensi17683](https://arxiv.org/abs/2603.17683v1)：单凭外部curriculum state machine、perception/action拆分与数据库context steering不足新贡献；具体负面证据是v2完成curriculum/裁判进度却0level，相对v1两level，作者仍把32学习action比1600–3000task交互称sample efficiency。拟核是否真正隔离出self-consistent perception hallucination cascade、及学习进度/任务成功不同分母，可能修正stage-judge进度的使用条件，而不以新控制术语重述成熟workflow。此决定准入事实仍含糊，需一次定点机制/评价才能裁，不先假EX/中心或用0level自动排；拟5仅在具体失效路径成立后评分。v1唯一，代码future不是缺全稿。
- [1/W Law17280](https://arxiv.org/abs/2603.17280v1)：固定功率近似、KV容量限制并发的解析roofline→按context长度路由两pool vs换代硬件能耗比较。论文明确无新hardware实验、B200/H200是投影、MoE dispatch omitted上界；不能把这些数字当新硬件证据。旧KV容量/route成熟原则本身不评分；决定准入的是该输入模型是否新增有用的validity/break-even边界而非把容量公式包装成普遍law。拟定点解析假设及评价够证再裁，不先认作全新的energy机制或以模拟自动排。currentv2Apr27 workinprogress，具体重要说明轻量核，不全history。

此四潜力/含糊均只是有限初筛，不预支Books/Source/全体候选；Sensi及1/W先定点消歧，而不是把宽题库送全文队列。作者正在准备已正式准入的MUD必要核心/反侧，准备好即单篇送reader/root。

## 一次必要消歧后的拟准入（待非作者校准）

2026-10-11压缩恢复后实际重读本日合同与STOP；仅两已具名含糊项，不扩发现。下面是决定准入的有限原证，不授Source完成/NC/中心终态或Books。

**Sensi17683拟2+1+2=5。** [v1](https://arxiv.org/html/2603.17683v1)实际必要§4.1–4.5、§5/6.1–6.4、§9已读。Listing4/Eq11的judge输入仅learningitem/rubric/facts/figured-out，没有frame或独立groundtruth；score≥8使completed，Eq10将当前K整批提升facts。§6.4/Eq17报告错误diff→错误K→高分→completed→后续错误facts，§9明确grounding漏洞。这不是DB/state术语本身的贡献：裁判进度可驱动真实持久状态变更，而输入与被晋升对象同源，需要区分“通过学习步骤”与“学得正确”。这条具体失效接口值得核验，故拟准入；不以0level排除，也不采作者“仅感知失败、架构已验证”归因。Figure3是illustrative；两版本不同backbone；32curriculum action与reported1600–3000 baseline不是同任务成功分母，50–94×不采用。真实逐turn审计/paired intervention未披露，后续必要owner比较限定这个状态晋升接口，不遍代码/附录。

**1/W17280拟2+1+2=5。** [v1](https://arxiv.org/html/2603.17280v1)实际必要§2–5及§10.1/10.2读到，拟准入对象不是context路由成熟原则，而是将KV容量、roofline步时与logistic功率组成context-window能效关系的具体成立区间；如果成立，会改变“缩短配置窗口与换代硬件可独立相乘”的设计判断。本文为analytic study，无新B200/H200测量本身不决定排除。但原nmax∝1/window、H∝平均实际长度，要另假定实际长度随配置窗口变化；容量饱和时H·n未必随window增大，功率也未必饱和。Table1 H100从2K到128K功率598→369W，tok/W35.0→.88不是严格反比；同70B/TP8/8K的Table1/Fleet用128并发而Table2/5用22，需解释profile条件，不能拼通用law。§10保TP-shardedGQA/steadydecode与smoothload，output-only未计prefill，MoEdispatch未计、投影硬件无实测。准入后先具体owner核条件分支能否分采或已有覆盖；中心冲突保反证，不以EX或降分代替审阅。无需扩大所有表/代码/旧版。

两原DOI夹证日期仍为03/19自然日（见本节顶部字段）；未独校不预支确定候选或safe。请求reader一次准入及必要日期校准；若理由需要改，按具体误判修正，非为减少普通待办。
