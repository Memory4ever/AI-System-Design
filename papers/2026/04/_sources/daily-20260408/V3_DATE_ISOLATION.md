# 04/08 日期隔离与证据保留

## In-Place Test-Time Training — 2604.06169v1

官方[abs/v1](https://arxiv.org/abs/2604.06169v1)的Submitted为2026-04-07T17:59:44Z，comment为ICLR2026 Oral；提交时间不等于首发。相同title/authors的[OpenReview](https://openreview.net/forum?id=dTWfCLSoyl)与[PDF](https://openreview.net/pdf?id=dTWfCLSoyl)提供可能更早的正文身份。本轮forum和PDF重试转browser challenge，api2/notes?id及api/notes?id返回403；此前已可读PDF的ICLR2026 heading仍没有足够原始首次公开时间。第三方Jan/Feb目录只作为发现线索，不支持正面日期判定。

从34项本窗工作集合移除此家族，不评分、不据它写Books。不是撤稿、没有因日期未核而删除已读证据；拿到原始OpenReview note的公开时间或可验证官方首次正文公告后，只重开该家族真实owner day。

保留的机制证据来自[arXiv exact-v1](https://arxiv.org/html/2604.06169v1)§3与评价附录：W_up/W_gate冻结，W_down自pretrained MLP初始化；每chunk先apply，再由embedding卷积形成含后续token的target，以similarity loss作outer-product更新服务后chunk。不是完整archive或teacher分布蒸馏。Qwen3等需数十B token continued pretraining，H800评价，batch1效率含指定SWA1024；clipping/chunk size是兼容条件，非任意model零训练插件。Ch22已有NTP/sparse fast-state，复用已有MLP投影的成本分支可待真实日期恢复后对读；不能证明多租户共享或tail SLO，重试/reset必须保护request state。这些未据以获得本窗Books决定。

## Meta两篇Apr8博客

实际打开[Introducing Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/)与[Scaling How We Build and Test Our Most Advanced AI](https://ai.meta.com/blog/scaling-how-we-build-test-advanced-ai/)，正文原字段均为April8,2026，无原时区/时刻。只读urllib原始HTML分别213925/171862字节，未查得datePublished/publish_time/published_time/publishDate/creation_time等可用精确字段；这不是证明字段绝不存在，也不从当前访问时间反推公开时间。

Muse Spark博客可用机制线索为pretrain/RL/test-time三轴、reasoning长度penalty与parallel agents；作者对evaluation-awareness是否改变行为保留不确定性。Framework说明风险范围、before/after safeguard评估、部署决定与报告透明度，但Blog不能替代未读的具体报告评价。尚不能确定落入Apr7 09→Apr8 09窗口，所以不纳入候选、不评分、不支持Books或全源零命中。需要原始带时区发布时间/官方早发可得记录；拿到后只重开两家族，无需重扫全年Meta。

## 5项跨09:00截点的日期隔离（2026-09-26更新）

实际复取的v1 Updated原字段分别为06111 01:10:59Z、06163 01:13:32Z、06129 01:12:04Z、06036 01:06:37Z、06132 01:12:13Z，均在2026-04-08。Updated不是公告时刻，不证明一定晚发；但本轮没有早于09:00的公开上界，不使用全批slot冒充单篇归属。这五项不列当前候选、不评分、不写Books。以下是已读的机制证据，旧评分/拟处置仅记录当时审阅，现已失效；恢复需本家族原始公告/正文可得上界组合，只重开真实owner日。

### [ACE-Bench: Agent Configurable Evaluation with Scalable Horizons and Controllable Difficulty under Lightweight Environments](https://arxiv.org/html/2604.06111v1)

Exact-v1 §§3–4用hidden slots控制序列长度、globally-incompatible decoys控制难度，static JSON工具保留唯一解生成规则。它揭示aggregate容易混入horizon/difficulty/domain比例，值得恢复准入；步数与hidden slots相关、分数随decoys下降只证明作者合成协议，不证明两变量对任意环境统计独立或覆盖真实浏览器副作用。

Ch66已有factor-grid、任务分布/聚合敏感性与reference可解性合同；5分标准已有覆盖，不把可配置benchmark新名称视作新owner，不把合成scaling映射为真实Agent能力排序。


### [Data, Not Model: Explaining Bias toward LLM Texts in Neural Retrievers](https://arxiv.org/html/2604.06163v1)

Exact-v1 §§3–5用同主题BM25配对负例缓解topic差别，观察正负supervision artifact方向与LLM/human方向相符；AppendixE理想化additive-feature假设下的推导不能称任何实际encoder必然。14个BEIR-derived数据及多类retriever中的source偏好是检索分数现象，不是答案truth。调整数据artifact或投影bias方向可能一起删掉relevance信息，必须重新评估检索。

Ch76已有domain/relevance-proxy错位，是否已覆盖“标签来源的shortcut变成来源偏好”需具体对读。6分深入保留反证，不因有LLM文本就改变corpus来源白名单，不认为去source bias可保证公平或正确。


### [PoM: A Linear-Time Replacement for Attention with the Polynomial Mixer](https://arxiv.org/html/2604.06129v1)

Exact-v1 §§3–4.1将learned polynomial features汇总为共享state，再由token gate回读；causal路径用前缀累积。固定degree/hidden width下才是linear成本，乘法量break-even不是实测latency。UAT依赖compact domain、固定sequence length及learned position；存在性不能证明固定k=2、无限Context或任意checkpoint兼容。

125M GPT-2、FineWeb15B tokens；纯替换validation loss明显较差，128-token local attention混合较接近原模型。Table1是固定总token量、变batch/序列的forward速度，不是batch1逐token生产decode；正文也提及custom Triton，不能照“纯高层PyTorch”描述外推。Ch14 pairwise selection与多项式特征理论不等同此shared-state替代，6分深入后待owner判断，不恢复其地学应用范围。


### [CoStream: Codec-Guided Resource-Efficient System for Video Streaming Analytics](https://arxiv.org/html/2604.06036v1)

官方abs/v1与HTML为CoStream，旧CodecSight命名不继承。已读§§3–6：codec motion映射patch，GOP内累积dynamic mask并扩成projector group；I-frame anchor重新prefill，重叠P-frame的K作RoPE修正、V复用。位置修正只校相位，不校新context造成的hidden drift；低motion亦可含关键语义。

InternVL3/Qwen3-VL、2/4×A10040GB、vLLM0.11、UCF-Crime40秒窗/2FPS/流式replay，不推广所有视频任务或production SLO。Ch23已有codec-aware evidence与映射误差，Ch45任意chunk需context correction、选择性refresh及fallback，足以承载作者受限分支。5分标准已有覆盖，不把同画面当exact KV identity。


### [Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents](https://arxiv.org/html/2604.06132v1)

Exact-v1 §§3–4将grader在execution后注入，trace、service audit、environment snapshot交叉判rubric；300任务/2,159rubric、14模型、三次trial，Pass@3与Pass^3分开。温度0模型与模拟用户/judge的温度及身份不同，不能称三次试验严格同分布或分数拥有能力真值。

Ch66已有不可见oracle、trace/环境证据、harness identity以及Pass@k机会和Pass^k重复可靠性的明确区分。5分标准已有覆盖。零error-injection的主结果不能支持故障鲁棒性，即使框架能配置注入；mock及LLM judge仍保留共同偏差。
