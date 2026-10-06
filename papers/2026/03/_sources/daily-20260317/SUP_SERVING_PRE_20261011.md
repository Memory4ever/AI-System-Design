# HeteroServe / OmniServe 必要Source复用与两owner窄PRE

仅本17补03/16。两家族完整v1题摘准入已独核，首arXiv日夹证原字段在SUP_DATACITE_BATCH。root非准备者本轮实际必要核心与actual Ch55/56差额核，以下有效复用，不以旧done标签代替证据。两项2+2+2=6，具体长期知识差额加深；尚未写Books/申请锁，需reader逐字PRE与唯一owner核。

## 12707 HeteroServe / INFER-PD-DISAGGREGATION

[exact-v1](https://arxiv.org/html/2603.12707v1) root实际§4、Alg1/§5.3.4–5、§6/Table8/§6.5关键对照：§4只standard KV阶段对embedding切点，ratio=2L(nkv/nh)(1+stext/Nv)，batch不改变此ratio，不授所有cut最优或EPD必须NVLink。Alg1整sequence worksteal、reuseweights、KV和assist仍计费；§5宣称100ms/实测212ms、timeout500ms/1.7s口径矛盾不采用无vision延迟。Table8同label5986/$64k与3156/$38k并非直接37%同预算提升，两个hetero worksteal行重复，§6.5另2793→3156，不借headline分配因果或经济保证。只采用encoder→embedding与P/D→KV切点的payload身份/大小区别及全assist成本，不采headline最优/普遍更快。

作者actual Ch55 55–92 Encode共驻→KV迁移及205–260 A/F切分完整邻接读：原72/74具体microbatch/Encode-Prefill共驻/EAServe已存在，因此不是新增Encode概念；差额是embedding切点只搬encoder output而PD搬全层KV，以及跨tier capacity/复用权重/完整sequence辅助路径分账。实际Ch54/56开篇交接有效重读；唯一Ch55，不复制模型表示/原通信算法。拟现Encode两段之后、新问题KV怎么移动标题之前，两段：

多模态切分还须先声明搬运的对象。把encoder留在独立tier、只把其输出embedding交给语言模型，与Prefill完成后搬全层KV是两条不同边；embedding只覆盖编码后的模态序列，而KV还随语言模型层数、KV-head形态及文本与模态总token数增长。因此embedding交接可能改变可用链路和encoder placement，却不能把一条standard-KV比较推广成所有内部cut的最优证明；bytes、dtype、model/encoder revision与消费者身份仍要实测匹配。<!-- source-family:SF-2026-ARXIV-2603-12707 -->

[HeteroServe的受限机制](https://arxiv.org/html/2603.12707v1)支持比较这两类payload，不支持“更小embedding自动消除vision排队”或同预算的普遍吞吐优势。跨tier还要支付encoder queue、权重驻留/复用、transfer与辅助执行；若work stealing接管整条sequence，相应KV、后续语言计算和assist状态不能只按embedding bytes计费。原文延迟/timeout与经济表口径不一致时，不采用性能保证；输入、链路或完整成本不匹配时，保留原Encode–Prefill共驻、独立E/P/D或单池，并按完整TTFT/TPOT与goodput决定拓扑。<!-- source-family:SF-2026-ARXIV-2603-12707 -->

## 12831 OmniServe / INFER-SCHEDULING

[exact-v1](https://arxiv.org/html/2603.12831v1) root实际§3.2–3.3/4/5.1–5.4：BE的QKV/同layer attention结果跨CPU，LS不等待BE attention；BE后续Dense在后续iteration同layer的GEMM中piggyback，req_id/layer residual store维持跨层/跨轮关联，非随意混入当前token。modulewise latency而非静态headroom预算；CPU/KV/PCIe模型不保证任意SLO。4A10080G+5hosts Xeon6342/400GB、100GbRoCE另10G，BF16 Yi34BTP2/Llama70BTP4；LS ShareGPT Poisson，BE LongBench8952/136和DailyMail1964/397平均输入/输出；LS TTFT2/3s、TPOT.2/.25s、30min。CPU baseline同预算但NEO适配；全load无拒与admission实验分开，不混goodput分母。未核artifact/复现，未披露配置不回填。

作者actual Ch56 373–447 iteration→operator边界/compute-KV移交→mixed与prefix grouping完整读，现iteration以当前token/batch为单位，不含“LS前进而BE attention在CPU等待→later iteration同layer ready GEMM”这一layer frontier/residual分支。actual Ch55/57开篇交接已读；唯一Ch56拥有ready选择/成本预算，runtime维护reqid/layer与dependency，不重复Ch54容量或Ch49kernel。拟Iteration Scheduling的SuperInfer source-family之后、Prefill抢占标题之前两段：

在线与best-effort请求共用Dense算子时，ready也可以细到layer而非整条request。一个异步分支让BE的attention在CPU执行，在线batch继续前进；只有BE对应layer的attention结果已返回、依赖状态有效，才把其后续Dense工作搭入后续iteration同layer的GEMM。runtime须保存request/layer对应的residual与结果，scheduler只选择已ready工作；不能因一份batch能进入GPU，就把仍等待CPU的BE层视为已完成，也不能将不同layer或token frontier静默拼接。<!-- source-family:SF-2026-ARXIV-2603-12831 -->

[OmniServe的受限证据](https://arxiv.org/html/2603.12831v1)用模块级latency模型预算BE搭载，而非把平均GPU空隙当固定headroom；CPU attention、KV与QKV/结果传输、残差驻留和重组同样计费。作者BF16 Yi34B/Llama70B与A100/多host、指定Poisson在线流量支持该分支，不证明突发负载的硬SLO；无拒绝压力实验与admission实验也不能合并成相同goodput。异步状态不可靠、链路/CPU瓶颈或在线slack不足时，停止接纳BE搭载，保留普通mixed batching、等待ready或专用容量，不由GEMM利用率批准最终token或服务保证。<!-- source-family:SF-2026-ARXIV-2603-12831 -->
