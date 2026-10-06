# Daily Research — 2026-01-30

**规范：** V3
**窗口：** 2026-01-29T09:00:00+08:00 ～ 2026-01-30T09:00:00+08:00
**窗口说明：** 用户授权仅补遗漏，保留已有候选日期、评分、原窗口与有效证据；新增材料按前一北京时间自然日检查，不搬移旧归属。
**补充窗口：** 2026-01-29 ～ 2026-01-29
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-08T11:37:17+08:00

## 1. 结论

原稿63家族及其评分、日期和有效审阅原样复用，原有限发现的302个DataCite标题identity、5个分类新增identity与118完整题摘不重建队列。本次补充窗口新增3个唯一家族：OpenAI内部数据Agent、Qwen3-ASR、PaddleOCR-VL1.5；后两项以官方Jan29公开日解除旧小时门限，前者为机构来源漏项。合计冻结66家族，中心理论争议2项仍终态隔离；有限发现停止不宣称历史全目录恢复。补查必要证据、Books POST及六部分独立DAY均已实际通过，普通待办0；不以原稿完成替代本次验收，不授保留项正面Coverage/Evidence。[原稿基线](../_sources/daily-20260130/supplement-original-20261008.md)完整保留。

Books处置：5整合（Ch45/56/23/5/66实际POST均通过）、1具体已有覆盖（Ch76）、55仅报告、2争议暂缓。实际增量是mutable KV的phase生命周期、双SLO轮转与真实迁移预算、多模态ICL课程/label读取路径、跨context固定方向干预的极性边界、冻结题库自适应prediction-residual估计。99×固定工作量、普遍公平性、有限预算CI/生产安全、意识或参数知识删除均不采用。未运行artifact、复现实验或验证生产能力。

补充处置：1整合AGENT-CONTEXT Ch75（实际POST通过）、2仅报告；合计6整合、1已有覆盖、57仅报告、2争议。新的书稿差额仅为producer-derived表语义、离线派生Context、在线观察与用户确认Memory的分责；ASR中间/完成接口、polygon/Real5保留为局部版本事实，不强改已有owner。未采用2000倍throughput、94.5因果归因、所有Agent的prompt定律或独立权限安全保证。

## 2. 来源覆盖

执行时间2026-10-04；依据与原始查询见[有限停止记录](../_sources/daily-20260130/V3_SOURCE_FINITE_STOP.md)。以下只声明实际范围，不宣称历史目录全恢复或互联网无遗漏。每日14源均处理；每周源不扫描。

补充执行2026-10-08：复用本日旧14源有限入口、分页与已明确缺段；新增仅Jan29具名线索/精确查询，原始范围见 supplement-native-0～3-20261008.json，必要源/owner比较见[增量证据记录](../_sources/daily-20260130/supplement-source-owner-pre-20261008.md)。未扩全月池、Weekly或90daycatchup。旧有效入口不重复授验收；以下三源新增恢复不代表完整历史目录恢复。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 复用旧Research/News有限目录及精确Jan29补线索；恢复[内部数据Agent官方正文](https://openai.com/index/inside-our-in-house-data-agent/) | 受阻 | 新增数据Agent准入；退休旧models为产品可用性关闭，历史Research段仍不可完整恢复，不报无遗漏 |
| SRC-ANTHROPIC | 当前Research10篇+SeeMore线索、Jan29精确日期查询 | 受阻 | Vertex AI高级agents workshop是教学/成熟toolmemory组合，非原始机制；历史分页缺段保留 |
| SRC-GOOGLE-AI | DeepMind/Google Research当前目录、Jan29相关主题/日期查询，未扩Google全部应用 | 受阻 | 当前目录不能恢复精确历史全部；无具名窗内未处理lead，缺段隔离 |
| SRC-META-AI | 官方Research响应空、精确Jan29相关主题查询 | 受阻 | 历史动态列表不可恢复；T-Mimi原始稿由arXiv覆盖但不能代替目录全覆盖 |
| SRC-QWEN | 复用旧blog/具名仓库；官方News Jan29及Jan29初始README/stream example定点恢复；commits第一页5条已到底 | 受阻 | 官方日粒度使release补入自然日，commit仅artifact身份；后发README更新不回填Jan29接口，arXiv Submitted不借作release公开。完整历史blog仍缺段 |
| SRC-DEEPSEEK | 官方主页当前V4.1及Research原始入口、updates有限访问、Jan29精确主题查询 | 受阻 | 当前页面不恢复历史Jan29段，无具名窗内新增，缺段隔离 |
| SRC-MOONSHOT | 官方Platform blog完整可见26条（2025Nov07–2024May）；Kimi-K2.5 GitHub releases20返回空[] | 受阻 | Blog不含2026且空releases不是全project历史；K2.5原发布Jan27非本窗，未给新的Jan29具名event，缺段隔离 |
| SRC-TENCENT-HUNYUAN | 首查官方research动态空；子线程IAB两种已允许入口有限超时/hidden不支持 | 受阻 | 精确历史全部目录不可恢复，没有具名Jan29漏项；保持终态外部保留，后续只对具名原文重开，不今天空段报历史0 |
| SRC-ZAI | 官方Research可见Aug2026→Dec2025；ReleaseNotes完整可见Aug26→July2025，目标附近Jan19→Feb02/03 | 已检查 | 有限可见日期bracket无Jan29条目；只支持这些目录范围，不保证历史删除无遗漏 |
| SRC-BYTEDANCE-SEED | Research选中条目及public_papers第1页20/242（1/13），最新May–Aug；Jan29精确主题查询 | 受阻 | 第1页并非历史全覆盖，未把全部242设逐项队列；历史分页目标段不可恢复保留 |
| SRC-BAIDU-ERNIE | 复用官方Blog目标bracket及PaddleOCR-VL1.5核心，定点复核Jan29官方公开日及polygon/Real5/速度协议 | 受阻 | release按官方日粒度补入自然日，不依午夜占位推小时；论文Submitted不替公开。polygon能力/五类slice采用为局部事实，历史目录缺段仍隔离 |
| SRC-XIAOMI-MIMO | 当前Paper8条/Blog15条可见停止；目标PaperJan08→Feb03；Jan29精确主题查询 | 受阻 | 当前选中列表不完整历史，未具名窗内event，缺段隔离 |
| SRC-MINIMAX | 英文Blog13条、中文14条可见停止，Jan27/28 M2her→Feb12；补[Agent Tech Blog](https://agent.minimax.io/docs/techblog)完整可见15行导航壳，原响应见[V3_MINIMAX_AGENT_FINITE.txt](../_sources/daily-20260130/V3_MINIMAX_AGENT_FINITE.txt) | 受阻 | 两Blog可见bracket无Jan29只支持其范围，M2her不同语种不新家族；Tech Blog无条目/日期/分页，精确Jan29历史段终态隔离，不报0。后续具名原文或可恢复历史bracket才定点重开 |
| SRC-ARXIV | 原API submittedDate被代理改写返回2026Oct，已作无效停止；DataCite prefix10.48550精确created区间5组title主题查询各单页90/42/55/124/81；过宽一般领域先收窄。官方cs.CL 2026-01 skip1850/show500只浏览19900–20868已观测邻域23相关标题，补7完整AB | 受阻 | created只公开可访问上界，不精确firstpublic；语义选择118个完整题摘而非全部宽行队列。日期按官方Eastern公告schedule+近Submitted下界包络，早Submitted需具名announcement-day；月列表不证明当日全类召回 |

表外：[PMLR](https://proceedings.mlr.press/v267/dong25d.html)仅因DIT具体旧发表lead触发首公开核；确认2025 ICML已公开，不扩会议整卷扫描。补检DataCite仅恢复arXiv身份及可访问上界，不支持实验或精确公开时刻。当前118具名official notes已查撤回/纠错，SwitchCodec已撤回不评分/不入Books；没有遍历版本全史。

## 3. 候选与判断

以下冻结66个唯一家族：原63行保持原评分/日期，末尾3行按补充自然日。2中心争议只记录争议及重开条件。原arXiv公开时间为推定范围，不是Created精确firstpublic：原v1 Submitted落Tue14ET～Wed14ET批，官方[availability schedule](https://info.arxiv.org/help/availability.html)最早Wed20ET=Jan29 01Z；Created给已可访问上界，秒精度字段取下一秒为exclusive end，范围完全原窗。原字段保留在[V3_DATE_RAW_FIELDS.json](../_sources/daily-20260130/V3_DATE_RAW_FIELDS.json)。早Submitted不使用这条下界。新增官方Jan29日粒度不强求小时；重要release只计本次增量，不重复整家族历史。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Window-Diffusion: Accelerating Diffusion Language Model Inference with Windowed Token Pruning and Caching](https://arxiv.org/abs/2601.20332v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:50:31+08:00 | 新揭示不等KV稳定→phase-refresh与active/buffer/farfield→缓存生命周期需质量验收；2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)857–861；root POST通过 |
| [SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips](https://arxiv.org/abs/2601.20309v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:49:58+08:00 | 过载OOM后swap会拖SLO→双SLO虚拟滞后主动轮转+充分写入块提前同步→联合预算；2+3+2=7 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)361–365；root POST通过 |
| [SATA: Sparsity-Aware Scheduling for Selective Token Attention](https://arxiv.org/abs/2601.20267v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:48:58+08:00 | 逻辑稀疏未落硬件dataflow→operand排序与Q-stationary→纳入排序/调度成本；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [T-Mimi: A Transformer-based Mimi Decoder for Real-Time On-Phone TTS](https://arxiv.org/abs/2601.20094v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:44:48+08:00 | 低bit codec还原误差→近waveform层敏感→保留局部高精度；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/abs/2601.20055v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:43:54+08:00 | 一致但不真的形式翻译→MCS deleted-clause局部repair→限制solver正确性authority；2+1+2=5 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Policy of Thoughts: Scaling Test-Time Training for LLM Reasoning via Online Policy Evolution](https://arxiv.org/abs/2601.20379v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:51:36+08:00 | 搜索后仍可有instance adaptation→临时LoRA+tests reward→训练预算与请求状态分账；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Demonstration-Free Robotic Control via LLM Agents](https://arxiv.org/abs/2601.20334v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:50:34+08:00 | VLA比较未必观测匹配→privileged-state agent反侧→按控制/观测条件选接口；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Efficient Evaluation of LLM Performance with Statistical Guarantees](https://arxiv.org/abs/2601.20251v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:48:35+08:00 | 自适应有限bank估计→PAI与history-dependent propensity→去重不能沿旧权重做CI；2+2+3=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)4017–4019；root实际POST通过 |
| [NPU Design for Diffusion Language Model Inference](https://arxiv.org/abs/2601.20706v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:59:12+08:00 | dLLM GEMM外sampling尾部→NPU采样dataflow→sampling与模型端到端分开；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [LinguaMap: Which Layers of LLMs Speak Your Language and How to Tune Them?](https://arxiv.org/abs/2601.20009v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:42:49+08:00 | 语言遵循不等任务准确→层结构与late-layer SFT局部修复→评价两轴分开；2+1+2=5 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Membership Inference Attacks Against Fine-tuned Diffusion Language Models](https://arxiv.org/abs/2601.20125v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:45:35+08:00 | 自定义mask攻击接口→多step sign aggregation→reference及mask权限限制风险；2+2+2=6 | 深入完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Improving Diffusion Language Model Decoding through Joint Search in Generation Order and Token Space](https://arxiv.org/abs/2601.20339v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:50:40+08:00 | 固定揭示顺序限制mask解码→joint order/token beam→scorer与搜索预算一起比较；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Linear representations in language models can change dramatically over a conversation](https://arxiv.org/abs/2601.20834v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:02:18+08:00 | 泛化probe跨conversation可反向→context-dependent features/steering→方向移植需核验；2+2+3=7 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)215–217；root实际POST通过 |
| [TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation](https://arxiv.org/abs/2601.20321v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:50:15+08:00 | 瞬时touch遗漏contact演化→时序触觉token+force alignment→历史sensor条件入模型；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler](https://arxiv.org/abs/2601.20755v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:00:20+08:00 | 重profiling干扰edge Decode→QoS选择低层uprobes→按丢事件/开销选观察粒度；2+1+2=5 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [SokoBench: Evaluating Long-Horizon Planning and Reasoning in Large Language Models](https://arxiv.org/abs/2601.20856v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:02:48+08:00 | solver有效不等输入忠实→等形走廊PDDL误转译→formalized-state独立验证；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Investigating the Development of Task-Oriented Communication in Vision-Language Models](https://arxiv.org/abs/2601.20641v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:57:42+08:00 | 显式共享视觉协议可隐蔽→unaware overseer局部差异→威胁条件含通信提示与协议；2+2+2=6 | 深入完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Beyond Divergent Creativity: A Human-Based Evaluation of Creativity in Large Language Models](https://arxiv.org/abs/2601.20546v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:55:25+08:00 | 随机无关词赢novelty→cue appropriateness gate→指标需分离新颖与关联；2+1+2=5 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Rewarding Intellectual Humility Learning When Not To Answer In Large Language Models](https://arxiv.org/abs/2601.20126v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:45:36+08:00 | 正确率掩盖拒答行为→可调IDK reward/R-tuning反侧→奖励与拒答分账；2+1+2=5 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Beyond Bug Fixes: An Empirical Investigation of Post-Merge Code Quality Issues in Agent-Generated Pull Requests](https://arxiv.org/abs/2601.20109v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:45:09+08:00 | PR raw issue混churn→按KLOC归一→静态质量比较需分母控制；2+1+2=5 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Semi-Supervised Masked Autoencoders: Unlocking Vision Transformer Potential with Limited Data](https://arxiv.org/abs/2601.20072v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:44:17+08:00 | 早期伪标签错误→validation门控介入→启用时机可控；2+1+2=5 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Syncopate: Efficient Multi-GPU AI Kernels via Automatic Chunk-Centric Compute-Communication Overlap](https://arxiv.org/abs/2601.20595v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:56:33+08:00 | 粗kernel分割损利用率→logicalchunk/tile依赖lowering→保全高层通信plan；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [SwiftFusion: Scalable Sequence Parallelism for Distributed Inference of Diffusion Transformers on GPUs](https://arxiv.org/abs/2601.20273v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:49:06+08:00 | 跨机Ring volume不可缩→Torus stagedall-to-all→布局/backend/长度共同选；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [VersaQ-3D: Architecture Support for Visual Geometry Grounded Transformers via Versatile Quantization](https://arxiv.org/abs/2601.20317v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:50:10+08:00 | VGGT持续saturation不同LLMspikes→WHT+DCT/PTQ→量化形态及模拟成本边界；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Quantization-Aware Distillation for NVFP4 Inference Accuracy Recovery](https://arxiv.org/abs/2601.20088v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:44:40+08:00 | NVFP4恢复训练不稳→多阶段quant-aware distill→prefix/数据条件分离；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [HESTIA: A Hessian-Guided Differentiable Quantization-Aware Training Framework for Extremely Low-Bit LLMs](https://arxiv.org/abs/2601.20745v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:00:06+08:00 | 超低bit误差敏感度不同→Hessiantrace分配与annealedsoftmax→精度成本联合；2+1+2=5 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [OnePiece: A Large-Scale Distributed Inference System with RDMA for Complex AI-Generated Content (AIGC) Workflows](https://arxiv.org/abs/2601.20655v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:58:02+08:00 | 两侧协同阻塞流水→one-sidedRDMA double-ring→GPUbuffer依赖/liveness明确；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Dissecting Multimodal In-Context Learning: Modality Asymmetries and Circuit Dynamics in modern Transformers](https://arxiv.org/abs/2601.20796v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:01:25+08:00 | 模态固有主次判断→固定序列不同curriculum的读取/容量反侧→训练历史与label路径分账；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)347–349；root POST通过 |
| [Self Voice Conversion as an Attack against Neural Audio Watermarking](https://arxiv.org/abs/2601.20432v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:52:50+08:00 | 语音自转换可抹watermark→感知保持攻击→水印评价含转换威胁；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Detecting and Mitigating Memorization in Diffusion Models through Anisotropy of the Log-Probability](https://arxiv.org/abs/2601.20642v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:57:43+08:00 | dDiffusion norm memscore不稳→isotropy与angular/lownoise条件→分布假设入检测；2+2+3=7 | 深入完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [DiffVC-RT: Towards Practical Real-Time Diffusion-based Perceptual Neural Video Compression](https://arxiv.org/abs/2601.20564v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:55:50+08:00 | 异步video decode时序耦合→temporalshift与cache→pipeline质量/调度联合；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Can Continuous-Time Diffusion Models Generate and Solve Globally Constrained Discrete Problems? A Study on Sudoku](https://arxiv.org/abs/2601.20363v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:51:14+08:00 | 连续状态Sudoku采样→SDEvsODE有效性反侧→噪声与constraintquality分开；2+1+2=5 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [SemBind: Binding Diffusion Watermarks to Semantics Against Black-Box Forgery Attacks](https://arxiv.org/abs/2601.20310v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:50:00+08:00 | 防伪不等文本水印检测→semanticlatent binding→语义迁移攻击边界；2+2+2=6 | 深入完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Decomposing multimodal embedding spaces with group-sparse autoencoders](https://arxiv.org/abs/2601.20028v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:43:16+08:00 | 融合SAE难辨模态功能→group-sparse mask→分模态特征解释条件；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [$\mathbb{R}^{2k}$ is Theoretically Large Enough for Embedding-based Top-$k$ Retrieval](https://arxiv.org/abs/2601.20844v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:02:32+08:00 | 较优top-k几何不等可学习→MEDR/2ktheory→表示条件与训练可达分离；2+2+3=7 | 深入完成 | 已有覆盖：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)225–231/302–307，表达容量≠训练/有限精度可执行，root实际NoDiff通过 |
| [Training Reasoning Models on Saturated Problems via Failure-Prefix Conditioning](https://arxiv.org/abs/2601.20829v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:02:12+08:00 | 饱和RLVR难探索新成功→failure-prefix训练→采样状态决定信号；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Reward Models Inherit Value Biases from Pretraining](https://arxiv.org/abs/2601.20838v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:02:23+08:00 | RM基底价值有偏→matchedpreference/training反侧→reward并非中性truth；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [DenseGRPO: From Sparse to Dense Reward for Flow Matching Model Alignment](https://arxiv.org/abs/2601.20218v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:47:48+08:00 | imageflow终局reward稀→ODE路径/timestepSDE→densecredit与采样成本分开；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Reinforcement Learning via Self-Distillation](https://arxiv.org/abs/2601.20802v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:01:33+08:00 | verifiable反馈富含诊断→selfteacher denseKL→奖励信息与teacher质量条件；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation via Context Poisoning](https://arxiv.org/abs/2601.20615v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:57:01+08:00 | RAG输入攻击不只错答→energy/lengthpoison→resourceexhaustion威胁；2+2+2=6 | 深入完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [AgentLongBench: A Controllable Long Benchmark For Long-Contexts Agents via Environment Rollouts](https://arxiv.org/abs/2601.20730v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:59:45+08:00 | 静态检索不等长轨迹记忆→rolloutdensity控制→Agent上下文评价需动态；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [When Flores Bloomz Wrong: Cross-Direction Contamination in Machine Translation Evaluation](https://arxiv.org/abs/2601.20858v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:02:51+08:00 | translation目标污染跨方向→FLORES反侧→语言方向污染不能泛化；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [P2S: Probabilistic Process Supervision for General-Domain Reasoning Question Answering](https://arxiv.org/abs/2601.20649v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:57:53+08:00 | 无processlabels→goldsuffixconditionalprob→proxy质量/生成预算核验；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation](https://arxiv.org/abs/2601.20614v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:57:00+08:00 | hardquestions梯度失衡→answer-preserve augmentation→训练信号分配；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale](https://arxiv.org/abs/2601.20276v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:49:12+08:00 | API retrieval成功不等QA成功→semanticnearmiss→embedding access/回答评价分离；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis](https://arxiv.org/abs/2601.20103v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:45:01+08:00 | isolatedjudge错rewardhacking→contrastivecompare→识别能力受条件影响；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [HE-SNR: Uncovering Latent Logic via Entropy for Guiding Mid-Training on SWE-bench](https://arxiv.org/abs/2601.20255v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:48:41+08:00 | midtrain PPL混context tax→HE-SNR metric→上下文学习与词预测分开；2+1+2=5 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction](https://arxiv.org/abs/2601.20299v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:49:44+08:00 | 弱judge能被deception骗→peerpredictioninversegap→评分接口影响风险；2+2+3=7 | 深入完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Minimax Rates for Hyperbolic Hierarchical Learning](https://arxiv.org/abs/2601.20047v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:43:43+08:00 | Euclidean hierarchy样本复杂度→hyperbolicLipschitz条件→几何选择边界；2+1+3=6 | 争议 | 暂缓：中心理论证明缺口；本窗终态争议，不作正面证据/Books，重开条件见§4/5 |
| [When More Data Doesn't Help: Limits of Adaptation in Multitask Learning](https://arxiv.org/abs/2601.20774v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:00:47+08:00 | 无分布假设多任务不能成→impossibility→task相关性必须声明；2+1+3=6 | 深入完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [SA-PEF: Step-Ahead Partial Error Feedback for Efficient Federated Learning](https://arxiv.org/abs/2601.20738v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:59:56+08:00 | partialEF残差在nonIID变化→warmup及残差state→压缩训练条件；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Look in the Middle: Structural Anchor Pruning for Scalable Visual RAG Indexing](https://arxiv.org/abs/2601.20107v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:45:06+08:00 | 最后层attention剪枝失效→middle-layeranchors→querydependency非所有pruning否定；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [What's the plan? Metrics for implicit planning in LLMs and their application to rhyme generation and question answering](https://arxiv.org/abs/2601.20164v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:46:34+08:00 | next-token可含future计划→causalsteeringfutureanswer/rhyme→层状态目标辨识；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [One Word is Enough: Minimal Adversarial Perturbations for Neural Text Ranking](https://arxiv.org/abs/2601.20283v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:49:22+08:00 | 一词扰动可抬retrievalrank→midrankGoldilocks→retriever安全取决初始rank；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs](https://arxiv.org/abs/2601.20357v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:51:06+08:00 | 单drafter跨scenario不稳→verified-history ensemble/batchshare→SD动态资源策略；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [Evolutionary Strategies lead to Catastrophic Forgetting in LLMs](https://arxiv.org/abs/2601.20861v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T11:02:56+08:00 | 低memory ES不等低forgetting→matchedsteps非同compute denseupdatenorm→continualtraining约束；2+2+2=6 | 标准完成 | 仅报告：局部机制/评价条件未支持普遍设计结论；具体采用边界见§4 |
| [MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization](https://arxiv.org/abs/2601.20577v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:56:09+08:00 | 同形计划不能直接重放→overlap/区域变换reuse条件→先验收轨迹可复用；2+1+2=5 | 标准完成 | 仅报告：局部任务/评价接口不足支持普遍机制，边界见§4 |
| [SAPO: Self-Adaptive Process Optimization Makes Small Reasoners Stronger](https://arxiv.org/abs/2601.20312v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:50:03+08:00 | PRM/reasoner失配→score-gap定位与相邻rollout校正→预算/验证同步分账；2+1+2=5 | 标准完成 | 仅报告：局部任务/评价接口不足支持普遍机制，边界见§4 |
| [Reinforcement Unlearning via Group Relative Policy Optimization](https://arxiv.org/abs/2601.20568v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:55:56+08:00 | 禁词GRPO称必然收缩→all-zero group/KL反例→formal unlearning保证待修；2+2+2=6 | 争议 | 暂缓：中心contraction争议；NoBooks，重开条件见§4/5 |
| [CE-RM: A Pointwise Generative Reward Model Optimized via Two-Stage Rollout and Unified Criteria](https://arxiv.org/abs/2601.20327v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:50:24+08:00 | response自拟rubric不一致→query-only共享criteria/三条件adv→评分输入合同需保留；2+1+2=5 | 标准完成 | 仅报告：局部任务/评价接口不足支持普遍机制，边界见§4 |
| [Memory Retrieval in Transformers: Insights from the Encoding Specificity Principle](https://arxiv.org/abs/2601.20282v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:49:19+08:00 | cue相关不等使用→数量匹配random K干预→targeted影响与普通破坏分离；2+1+2=5 | 标准完成 | 仅报告：局部任务/评价接口不足支持普遍机制，边界见§4 |
| [Spark: Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning](https://arxiv.org/abs/2601.20209v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:47:36+08:00 | uniform探索分配不足→policy explore-tag触发N封顶forest→信号与预算执行分离；2+1+2=5 | 标准完成 | 仅报告：局部任务/评价接口不足支持普遍机制，边界见§4 |
| [Trajectory2Task: Training Robust Tool-Calling Agents with Synthesized Yet Verifiable Data for Complex User Intents](https://arxiv.org/abs/2601.20144v1) | 2026-01-29T09:00:00+08:00 ～ 2026-01-29T10:46:03+08:00 | 最终outcome可遮蔽intent/禁用动作→动态intent与forbidden-action评价→不只测最终DB成功；2+1+2=5 | 标准完成 | 仅报告：局部任务/评价接口不足支持普遍机制，边界见§4 |
| [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR/blob/9567667698f195fa807b1581de5c03184e63d2b0/README.md) | 2026-01-29 | 流式中间文本与完成刷新分开→unfixed chunks/tokens状态+独立finish、另设文本—语音aligner→版本接口不等不变commit/时间真值；2+1+2=5 | 标准完成 | 仅报告：Ch23现状态/时间分责已有具体覆盖，局部runtime事实保留，见§4 |
| [PaddleOCR-VL1.5](https://ernie.baidu.com/blog/zh/posts/paddleocr-vl-1.5/) | 2026-01-29 | 规整bbox/clean页评价不足→polygon定位/spotting+Real5物理畸变slice→按几何表示与处理链分开验收；2+2+2=6 | 深入完成 | 仅报告：Ch23区域身份/Ch66 corruption slice未得新稳定机制差额；94.5不作因果，见§4 |
| [Inside our in-house data agent](https://openai.com/index/inside-our-in-house-data-agent/) | 2026-01-29 | schema/查询历史遗漏producer过滤与粒度→代码派生语义离线归一化，缺/陈旧时live query→派生Context/当前观察/确认Memory三种权威分责；2+2+2=6 | 深入完成 | 整合：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)127–129；root实际POST通过 |

## 4. 证据与知识整合

每项采用精确v1，以下只概括判断；链接笔记保留方法/关键对照/配置/直接反侧与必要物理行，不要求第二次泛读附件。全部候选的必要命题与处置已由root分批实际复核；未核artifact或复现。

### [Window-Diffusion: Accelerating Diffusion Language Model Inference with Windowed Token Pruning and Caching](https://arxiv.org/abs/2601.20332v1)

评分修正为 2+2+2=6，不借成熟DLM cache原则加Durability。§3.1–3.2/图2–4在LLaDA/Dream、MBPP见活跃首16未解码位置与邻近buffer，远端低漂移；新解码位置短期仍不稳定，旧解码更稳定。§4外窗128、内窗16，仅phase边界滑窗：前phase decoded KV可缓存，本phase新decoded持续更新KV但不算logits；buffer复用KV，farfield剪枝，每32步refresh。§5/表1–2在FP32 NVIDIA A6000、GSM8K/MATH/HumanEval/MBPP同长度与cachebudget、无parallelFastdLLM/earlystop对照支持局部资源取舍。剪枝alone L16 Instruct HumanEval 27.4 vs55.5，L32回52.4，不支持普遍无损。§5.3过早refresh会冻结unstable刚decoded状态；过迟refresh又增加recompute/stalecontext。表3 headline99×比较静态最大1024 MBPP 217.8s vsadaptiveEOS2.2s，准确58.8→55.6，工作量不同，不能当同长度99×。
已落实差额：Ch45原正文“DLM撤销prefix不可变”解释layer/block version及query-derived近似state，但未解释active/buffer/pruned三种角色与刚decoded稳定性phase。该状态生命周期已窄补，不外推其他模型。

整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)857–861；root POST通过。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips](https://arxiv.org/abs/2601.20309v1)

2+3+2=7深入必要部分。§3–5 RotaSched按waiting(now-arr-βF*TTFT_SLO)、rotary α*(now-lasttoken-βB*TBT_SLO)、running负runage排序，以HBM和transferbudget执行主动轮转；不是只在OOM才换出。DuplexKV在preempt前把fully-written块提前D2H同步，dirty部分才换出；双向copy不得同块race。block-first跨层连续+批量CUDA memcpy减少64KB碎片开销；C2C物理双向450GB/s但Grace DRAM半双工384限制方向并用。GH200 144GB HBM/480GB DRAM、400GBoffload、vLLM0.6.6.post1、LLaMA3-8B/Qwen2.5-32B/Mixtral8x7B、ShareGPT/LMSYSChat1M Poisson到达，SLO TTFT5s/TBT100ms，α3 βF.5 βB0 transferbudget2400。16GB双方8GB table1 naive1556ms→Duplex46.8ms，是transfermicrobenchmark，不是端到端SLO保证。消融低效swapengine加大transferbudget反而恶化TBT，调度与实际copy执行需协同；不推广所有PCIe机器、α3普遍最优或生产公平性。
已落实差额：Ch56原正文完成operator后preempt、recovery/SLO与memory预算，但未承载“达到OOM前按双SLO虚拟滞后主动轮转，并受真实swapbudget约束”。唯一完整owner INFER-SCHEDULING；KV同步是该可执行机制必要依赖，不另章重复推导。

整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)361–365；root POST通过。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [SATA: Sparsity-Aware Scheduling for Selective Token Attention](https://arxiv.org/abs/2601.20267v1)

2+2+2=6标准。§III算法1二值mask位运算贪心排序O(n²)，把HEAD/TAIL/GLOB转入连续operandflow；K每head可变而Q固定count，故Q-stationary+interhead FIFO流水，GLOB退回常规。16×16 tilezero-skip。§IV controller SV+TSMC65nm综合/NeuroSim校准模拟、1GHz、32×32array；不是实芯片。TTST、kVT-DeiTTiny/Base、DRSformer，不是LLM端到端。包括TopK与scheduler代价；QK峰throughput1.76×/energy2.94×条件限定，Dk>=64或Sf<=24 scheduling<5%；Dk<32、Sf>28或tile太小会使ordering/zero-skip开销主导。仅报告局部数字与mask→物理dataflow条件，不授生产LLM收益。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [T-Mimi: A Transformer-based Mimi Decoder for Real-Time On-Phone TTS](https://arxiv.org/abs/2601.20094v1)

2+2+2=6标准。§3固定window transformer取代CNN deconv，新增4层至12+两linear waveformupsample，frozenencoder GAN/mel训练。§4同5M小时in-house语料基线，100客观/200pair×10raters，CMOS+2.32% CI[-.70,5.34]不能证明更优。TorchAO8bitperchannelweight/dynamicactivation QAT；表2 all4bit PESQ2.32、all8bit2.74，保留最终两transformer及两linear FP32到2.99（不是只两总operator）；最终QAT3.16 vsFP3.21。S22 80mschunk4.4ms/68.7MB vsCNN window5 42.1ms/window2 18ms/81MB，只codecdecoder不是整条TTS TTFT。Books若采纳应是接近waveform输出的重构误差放大导致混精度边界，不能泛化所有decoder最终两层不可量化。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/abs/2601.20055v1)

root第三校准授窄2+1+2=5候选（最终Books待证据核），不采“formal truth”。§3.3互相equivalent候选K3/roundtrip只证formula一致，translator可能一致错误。§3.4 SAT/MCS deletedclause反馈局部repair，MCS失败转soft/selfconfidence；strict strengthening只验证formula entailment。§4.2表2strict ARLSAT去MCS91.7→83.0；ZebraSoftOnly91→70.2；UnsatCoreOnly平均-10.9，是删除子句的纠错信息局部收益而非所有组件创新。router54stress94%不授通用安全。§4.4测试20B~30%validsyntax、120B/Sonnet>90；总结70Bthreshold未实测70B，不授阈值。§6 n>20 periteration15–30s vsCoT<2，greedy O(n SAT)不是SAT多项式保证。§7作者明确consistency≠事实/伦理truth与verifiedhallucination。倾向仅报告当前局部repair，已有solver/replan原则不自动Books新gap。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [Policy of Thoughts: Scaling Test-Time Training for LLM Reasoning via Online Policy Evolution](https://arxiv.org/abs/2601.20379v1)

2+2+2=6标准，因预算/估算信号多读Appendix A/B/D受影响部分。§4每实例MCTS探索+可执行tests reward→transientLoRA GRPO，episode末丢弃adapter避免跨请求状态传播。code withoutLoRA37.14 vsfull49.71局部消融支持更新有用，未授所有任务性能。Appendix D backward281ms/forward192.66ms=1.46额外，节点/token近似预算不是equal端到端训练算力；静态各baseline实际call上限不同。Appendix A/B Table6明说measured OR conservatively estimated improvement并引用officialreportbaseline，故跨域、商业胜出、普遍节省算力不作为实测采用。Table7单迭代473.66ms需模型/序列配置绑定。当前仅报告机制和局部code边界。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [Demonstration-Free Robotic Control via LLM Agents](https://arxiv.org/abs/2601.20334v1)

2+2+2=6标准，实际安全/对照影响读§II–IV。ClaudeOpus4.5/AgentSDK unmodified、absoluteend-effectorcontrol/get_obs privilegedstate，不是rawRGB；“demonstrationfree”不等zero-shot singletry，LIBERO试验10trial70.6%，取消presetlimit84.9%；ManiSkill14tasks×5seed60/70，MetaWorld48/50（两cheat/bruteforce记failed）。对照VLARGB来自原论文，作者明确非相同observation；LIBERO task0自动成功脚本还作后续例子。coaching迁移ManiSkill85.7→81.4、API成本150→220。§IV singleframework/model、仅simulation，highfrequency/contactdifficulty未来，不能说已替代VLA或真机安全。仅报告planningdominant可执行tool场景与资源边界。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [Efficient Evaluation of LLM Performance with Statistical Guarantees](https://arxiv.org/abs/2601.20251v1)

2+2+3=7深入§3/Thm3.1、AppendixA.1–A.3/B与§4–6。finitebank固定binarycorrectness不是未来真实用户总体；historicalBayes factors用于采样效率而非可信度。PAI estimate预测均值+inversepropensity residual，prob/pred仅依赖past，withreplacement。hybridvariance/activelearning配合τ/Nuniformfloor避免extremeweights。unbiased逐实例，但95%CI是nb→∞且variancepositive-stabilization、Lindeberg、conditionalvariancecontrol下渐近，不是任意有限预算保证。AppendixB去重抽样但沿原q权重破坏martingale，Figure6大预算miscoverage。两suite MMLUPro/BBH+GPQA+IFEval+MATH+MuSR，按releasedate2.2Khistorical/2.2Ktest，100seed，预算2.5–25%，historymissingMCAR。4–5×ESS是同CI宽估计查询数（1500 vsuniform7515），不表示5×walltime/全新OODbank保证。Ch66已补冻结bank prediction-residual接口，并将naive去重+旧propensity破坏CI条件的反侧放近正文。

整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)4017–4019；root实际POST通过。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [NPU Design for Diffusion Language Model Inference](https://arxiv.org/abs/2601.20706v1)

2+2+2=6标准。§III–IV separatedVector/FP/IntSRAM、reduction/exp/reciprocal/ArgMaxTopK/maskwrite、in-place覆盖logits，分片约4k趋饱和。§IV GPU LLaDA8BInstruct/MoE dInfer/vLLM采样占比最高71%依配置；TableII T1 B16 L32 V126k、VLEN512–2048 R1，2.53×只sampling，model()excluded。HBM2e/Ramulator、CocotbRTL+7nmOpenROADDC1GHzsimulation/synthesis不是芯片实测。Algorithm2温度Gumbelnoise略去未来补，不能声称所有sampling功能equivalent。仅报告减少GEMM之外samplingtail的具体映射，不授endtoend2.53或通用NPU架构已验证。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [LinguaMap: Which Layers of LLMs Speak Your Language and How to Tune Them?](https://arxiv.org/abs/2601.20009v1)

2+1+2=5标准。§3四种prompt保语义控codeswitch/Englishdistractor/bilingualans，langdetectlanguageconsistency与taskaccuracy分开；Qwen3-32B code-switchMMLU准确60.5% vsmono51.77%，LC8.35% vs45.17%，不是中文等全部language普遍规律。§4logitlens/meanpoolcos只观察层结构，不证因果英文思考；BLOOM7.1B/Qwen3-8/32B。§5仅最后k层SFT+maskQRAtokens，business五科2500examples80/20，Claude3.5Sonnetverify/生成CoT，非business52科MGSM/XQuAD验，随机selective/fullSFT对照。最佳层数§5.1与AppendixE文字有2vs3层差，故不采用唯一通用k；只采用languageadherence可以不同于准确度、有限late-layer修复。无硬件性能/SLO主张，Not Applicable。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [Membership Inference Attacks Against Fine-tuned Diffusion Language Models](https://arxiv.org/abs/2601.20125v1)

2+2+2=6，安全信号深入受影响§2.1/§3–4/D.1/D.4–7。greybox可提交custommasked文本并读tokenlogits，还需referencebase；fine-tuningmembership不是不加条件的公开API泄露。mask5→50% T16，每步target/reference一对forward、离线N128子集m10 signvote+inverse-stepweights。LLaDA8BBase/Dreamv0Base7B，MIMIR6×1000member/1000nonmember+3NLP×10000，AdamW bf16 3×A100 batch48 lr5e-5，4epochearlystop，fine-tuning而非未知pretrainingmembership。Table1 avgAUC.81 vsRatio.62/TPR1%FPR.16 vs.04仅controlled设定，baseline查询T16；D.1同时写4MC平均，预算精确实现未artifact核。§3.3称centeredzero noise推出sign>.0概率.5并不由均值零成立（需median/symmetry）；因此不采用分布无关universalproof。D.6 tokenizer/architecture差异使reference校准变差；D.5 SOFT/DP等为该攻击下降不是已证全部privacy安全。D.7 Ratio1h32m00/Sama1h32m16只是指定benchmark，不授productionefficiency。必要机制/实测风险已读，仅采用该greybox接口局部风险，不支持所有公开API或pretraining泄露保证，不因安全词自动写书。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [Improving Diffusion Language Model Decoding through Joint Search in Generation Order and Token Space](https://arxiv.org/abs/2601.20339v1)

2+2+2=6标准，§4/§5/AppendixA.3–A.7。beam在block边界分叉order和token，prune score仅本次newlyrevealed块且以fullprediction futurecontext条件，不累计allrevealedprefix或maskfuture。LLaDA8BInstruct/1.5在GSM8K/MATH500/Countdown/HumanEval，对照lowconfidence、random/AR+MV、ARbeam、orderonly/tokenonly；scorer单独消融保持search相同。AppendixA.4 NFE S*K*L+B*K²*L，K4/S=L2/B=L32≈MV5 FLOPs，不是调度walltime普遍相同；主要beam3/5/8且temperature.2–1search预算应保留。A.5同temp.4Countdown K1 22.7 vsK5 34.4亦扩大预算，不单独证免费收益。A.7 Sudoku模型likelihood与全局合法性不相关时全部方法低于/近randomcellaccuracy25%，结构search不能补模型缺失约束knowledge。仅报告固定maskmodel的局部选择与搜索成本，不能采tokenlikelihood等于correctness。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [Linear representations in language models can change dramatically over a conversation](https://arxiv.org/abs/2601.20834v1)

2+2+3=7，新增context-dependentfeature/steering portability而非借linear原则。§2Gemma3-27B-IT为主，岭/线性logisticregression factualyes/no方向，§3 Figure2反向prompt避免词形/behaviourconstruct混杂后，再用oppositeday+empty训练robust方向；heldoutconsciousness/chakras conversations，topicrelevantmargin反转generic大致稳定；offpolicyreplay/onpolicy都有，显式fictionstory弱。AppendixB.8另在answer前一token拟合direction并steer，chakras会相反效果consciousness相对一致，所以不可用某个长context成功授全context有效。注意该beforeanswer方向不同于主实验afteranswer方向，不能当同一probe证明因果；§4少量conversation/concepts、机制未知、非普遍belief改变或完整安全监测。Ch5已补before-answer固定方向跨context极性边界，与after-answer读出分離。

整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)215–217；root实际POST通过。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation](https://arxiv.org/abs/2601.20321v1)

2+2+2=6标准§IV–VI/表I–III。同步tactile+6axiswrench+12×12pressuremap，N5滑窗force双codebookVQVAE reconstruction防collapse，tactileViT+causalTFsummary，InfoNCE对齐forcecode；部署不需FTsensor。7realworldforcecriticaltasks ACT/DP/π0.5及tactilebaselines，nohistory/小codebook/连续latent/forceexplicit对照；history消融支持瞬时纹理不能分辨staticgrip与incipientslip。SeenCustomA75 vs66.7、GelSight65 vs58.3；UnseenCustomB60.3 vs30、GelSight53.3vs23.3。仅相似visuotactilesensortypes不能推capacitive等普遍transfer；VI微米airgap/contact前控制错误未解，actionchunk慢于forcespike会失败，感测通道不等于fastsafecontroller。Chocolategentle任务vision可比，不授全部VLA必须touch。仅报告特定contact/historylatent取舍，这些传感器/任务族的局部历史latent反侧不足改变所有foundation/VLA长期机制。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler](https://arxiv.org/abs/2601.20755v1)

2+1+2=5标准§3–5。libbpf/BCC uprobes解析llama.cpp/GGML operator/tensor/graph并关联CPU PMC/thread/expertID，QoS<5tok/s动态关闭部分probes，在token/graph与operator粒度间交易可见性；ringbuffer更轻但丢事件不报告，perfbuffer可知missingevents。OrangepiRK3588/OpenHarmony5.1 Ubuntu22.04/RubikPiQCS6490Ubuntu24.04，CortexA76 2/4cores，完整BCCdecode速度-2.8–4%、libbpf最低-1.7%（部分feature不支持），tok/graphonly-.1%。先验ONNX8%只是preliminary不同系统不能公平profiler优势。MoEQwen1.5A2.7B4bit8.9GB>RAM+mmap时expertdistance/pagefault定位diskIO，不能泛化所有MoE bottleneck。论文支持runtime动态probe取舍，未声称first-eBPF/全GPU完整可观测。仅报告局部工具与配置，特定probe/硬件动态阈值不等可复用的所有runtime可观测性保证。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FIRST_THROUGH_SECOND.md)。

### [SokoBench: Evaluating Long-Horizon Planning and Reasoning in Large Language Models](https://arxiv.org/abs/2601.20856v1)

2+2+2=6。§3–4：一箱直走廊长度5–100、四旋转共80地图；GPT-5/GPT-oss-120B/DeepSeek-R1，8次重复，最多32768输出token。LLM-Modulo以GPT-5-mini生成PDDL problem，人核domain、FastDownward/PyperPlan、60秒/3次上限，4次重复。必要反侧是§4.2：320个problem只有7个语法错误，但语法通过仍会把地图尺寸/位置写错，solver只能证明它收到的形式状态；换旋转/换行也会改变难度。不能把该局部计数/转译失败变成所有规划的25–30步阈值、指数复杂度定律或端到端可靠性；75分钟是收集总时间，不是请求延时。仅报告：局部PDDL输入忠实性证据，不由特定走廊阈值改写通用规划机制。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_THIRD.md)。

### [Investigating the Development of Task-Oriented Communication in Vision-Language Models](https://arxiv.org/abs/2601.20641v1)

2+2+2=6，受影响的隐蔽通信主张深入。§3、§5–7：sender见10图及目标，receiver相同图片不同顺序；共享协议与独立创造协议不同，overseer同架构但不知道协议。自然/高效/隐蔽是明确提示条件，不是无提示自发串谋。GPT-4o、Qwen2-VL72B、Pixtral12B、Llama4-MaverickFP8，COCO/CLEVR/真实及合成旗帜，300局；局部std最高.029。15名人类、自然/隐蔽最多5词、高效1词，条件长度不完全匹配。§5人类表中GPT隐蔽成功.53、人类.31，不能外推任意带宽或所有模型协作；独立协议接收者损失约.1–.4也说明共同可解码结构的条件。仅报告：受提示、10目标、英语视觉游戏的局部反侧，不授现实隐蔽串谋或安全保证。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_THIRD.md)。

### [Beyond Divergent Creativity: A Human-Based Evaluation of Creativity in Large Language Models](https://arxiv.org/abs/2601.20546v1)

2+1+2=5。§3 DAT用首7个合法WordNet名词的SBERT平均距离，500回答，温度.5/1/1.5另单次0，500随机名词/显式作弊对照；随机无关词可取得更高novelty，不能把这个指标称全面创造力。§4 CDAT 539 cue先要求语境关联：对random进行two-sided Welch检验、每温度FDR α=.001，且模型均值高于random；通过后仍以novelty为标量，2D Pareto仅诊断。所有模型通过门槛；99人类样本、70cue、11评者不支持普遍人机排名或温度因果。仅报告：英文词嵌入评价的具体混杂/条件门，不把此阈值作为通用创造力判据。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_THIRD.md)。

### [Rewarding Intellectual Humility Learning When Not To Answer In Large Language Models](https://arxiv.org/abs/2601.20126v1)

2+1+2=5。方法/实验/讨论：MedMCQA添加IDK选项与Hendrycks数学开放答案，正确1/错误-1/拒答可调；Granite3.3-2B和Qwen3-4B，GRPO LoRA，TRL，lr2e-5、8样本batch/64积累、group8、最大500步、prompt256/completion1024、bf16 A40/A100。8k训练、约100评测，RL-only/SFT随机30%IDK/R-tuning按base错误IDK；答案准确率与拒答召回分别度量。Qwen拒答reward .3局部拒答41%/错误10.3%，不等真实性或医疗安全。文末直接反侧：SFT或R-tuning的IDK比例可压倒学习，拒答与能力不能同看单一正确率；所谓最优比例尚未系统测量。仅报告：两模型有限奖励/数据条件，不从成熟三元reward推普遍探索定律。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_THIRD.md)。

### [Beyond Bug Fixes: An Empirical Investigation of Post-Merge Code Quality Issues in Agent-Generated Pull Requests](https://arxiv.org/abs/2601.20109v1)

2+1+2=5。方法及§6：AIDev33,596 PR→8,106 fix→1,802 Python→1,210 merged、206 repo，Codex949/Copilot106/Devin100/Cursor40/Claude15。SonarQube同配置比较base/merged，新增issue密度分母为added+deleted LOC。raw count差异大多在按churn归一后不显著，Cursor局部例外；不显著不是质量等价。静态code smell/security hotspot不等确认的运行漏洞，无人类反事实、选择偏差、小agent样本、Community edition限制。仅报告：本语料静态比较中的分母混杂；不授Agent排序、merged即安全或泛化修复能力。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_THIRD.md)。

### [Semi-Supervised Masked Autoencoders: Unlocking Vision Transformer Potential with Limited Data](https://arxiv.org/abs/2601.20072v1)

2+1+2=5。方法/评价：ViT-B16、75%patch mask；弱强增强均>.95信心且标签一致。warmup10epoch，可信验证样本准确率≥70%才启pseudo，连续n个epoch低于阈值禁用（n具体未披露）。CIFAR10/100上采样224、10–40%labels、200 pretrain/100 fine-tune、AdamW lr1e-4 wd.05、labelbatch16/unlabel32。Table3 CIFAR10/20%labels全机制66.40 vs首epoch启pseudo62.37/不设val gate63.49。未提供强FixMatch基线、硬件、重复CI，不授通用SOTA或LLM伪标签条件。仅报告：验证准确率控制伪标签介入时机的局部配方，具体70%并非跨任务稳定常数。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_THIRD.md)。

### [Syncopate: Efficient Multi-GPU AI Kernels via Automatic Chunk-Centric Compute-Communication Overlap](https://arxiv.org/abs/2601.20595v1)

2+2+2=6。§3/5：logical chunk介于global tensor与compute tile，显式(rank,index)依赖，用户注释tile size/index/scheduler；从partition/loop IR取通信计划，构图插wait，swizzle tile schedule而非搬数据；同一logical plan可lower copy engine、专用/共置SM TMA或load/store，调chunk/SM/tile/通信backend。§6固定高层计划对比Domino/Alpa/Mercury，8×H100 NVLink900GB/s、CUDA12.9/NVSHMEM3.3.9/PyTorch2.7，同栈，多种GEMM/attention算子shape来自Llama3/Qwen；不是完整训练step/服务SLO。人工最优GEMM平均4GPU99.8%、8GPU104%，小7B/8B GEMM-AR仍落后TritonDistributed；图11最佳chunk非单调、过细同步开销、过多SM抢compute。仅报告：特定算子自动lowering接口和实测实现，不把tile/通信共同依赖这个成熟原则作新长期缺口或宣称通用无注释自动编译。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_THIRD.md)。

### [SwiftFusion: Scalable Sequence Parallelism for Distributed Inference of Diffusion Transformers on GPUs](https://arxiv.org/abs/2601.20273v1)

2+2+2=6。§3–4：Ulysses跨机减少volume、Ring机内；Pu=gcd(NM,H)受head divisibility约束，Pu=2是volume例外。Torus利用all-to-all原地head chunk先compute，再Pull Q/Pull KV/Push O流水，partial softmax输出须合并；NVSHMEM put/get与stream内顺序/barrier保持数据一致，仍有层始末跨机同步，不是任意无同步读写。§5四AWS p4de.24xlarge各8×A10040GiB、NVSwitch/EFA400Gbps，CUDA12.8/PyTorch2.8/NCCL2.27.3/NVSHMEM3.4.5，Flux12B 3072/4096图、CogVideoX5B 20/40秒768×1360，评价一次sampling step，不是全视频请求SLO。TAS两机反差于USP；>2机平均1.27×，完整SF比TAS1.35×。AppendixB：Flux短序列NCCL Torus不提速而one-sided有益；video Torus已隐藏通信，one-sided边际小。序列>160k且D32可不胜；不得只说拓扑反转普遍更优。仅报告：该布局/两类DiT负载下backend与序列共同影响机制收益，尚不把此布局统一替代现有混合SP设计。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_THIRD.md)。

### [VersaQ-3D: Architecture Support for Visual Geometry Grounded Transformers via Versatile Quantization](https://arxiv.org/abs/2601.20317v1)

2+2+2=6。II-D/III：VGGT通道是较广分位持续saturation非仅孤立spike，WHT单独仍残variance；离线WHT+LayerNormγ融合+DCT weight，在线IDCT/BF16 RoPE再WHT/INT，持rotated activation减少额外WHT，未校准数据。IV两遍score重算只存softmax统计、INT4/8/BF16重配置；不能把数学未量化的orthogonal等价授低比特数值等价。V官方VGGT1B、Co3Dv2单序列8.9GB/15scene及7-Scenes7scene；W4A8 AUC@30 .9553 vsFP.9719，但AUC@3 .5931 vs.7536；W4A4 AUC@30 .5617仍显著落于FP，不照录‘98–99%所有精度’。III硬件是RTL/synthesis TSMC28nm1GHz、cycle simulator、Ramulator2 LPDDR5-6400 102.4GB/s，Jetson XNX20W/ONX25W实测功耗，不是流片实测。3.88mm²/2.18W和10.8×等为作者模型条件，未运行。仅报告：VGGT量化形态与模拟加速器的局部反侧，不能证明所有多视角transformer校准无效或所有低bit正确性；旋转/精度合同的成熟原则不重复建owner。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_THIRD.md)。

### [Quantization-Aware Distillation for NVFP4 Inference Accuracy Recovery](https://arxiv.org/abs/2601.20088v1)

2+2+2=6。§3 110–141/192–296，§4 330–454：固定原BF16 teacher，量化student以KL回配参考分布，避免在已多阶段SFT/RL/merge的权重上继续labelCE破坏原能力。Nemotron49B/.3B tokens/5k heldout8M tokens，BF16与QAT CE同.408但QAT KL.311，QAD CE.416/KL.004；验证labelCE不足确定行为恢复。单SFT Nano12B局部QAT可与QAD相当，不称QAD总优。RL-heavy Nano30BA3B/Ace7B冷启动SFT+RL，QAT局部甚至落后PTQ；并非随机teacher会恢复所有能力。保留部分attention/Mamba BF16/KV FP8，不是所有算子NVFP4。训练.3–6B tokens、lr/教师选择皆依产物，取validation最低10checkpoint再按benchmark平均选择，存在基准选择偏差；AIME/LCB/GPQA/IFEval的多采样和temperature不同，不跨协议直接比较。硬件成本Not Disclosed，SLO不适用。仅报告：这些特定产物多阶段目标保真与budget边界，未授所有低bit无损或全部hidden knowledge恢复；所测产物的teacher目标/训练预算边界不作为所有低bit产物通用恢复机制。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_FIRST.md)。

### [HESTIA: A Hessian-Guided Differentiable Quantization-Aware Training Framework for Extremely Low-Bit LLMs](https://arxiv.org/abs/2601.20745v1)

2+1+2=5。§3 128–239，§5 582–608/722–784：ternary soft assignment渐进退火；Hutch++ Hessian log trace产生层敏感度并离线冻结，调温度，不是online Hessian feedback。Llama3.2 1B/3B、10B UltraFineWeb、seq1024、group128 weight-only、全精度activation/其他参数、AdamW、5runs均值。软连续主机制贡献大，增加Hessian调度的精度增量仅1B .540→.547、3B .599→.601；不能把全部增益归Hessian。基线有原论文数值而非全同栈重跑；其他模型/2bit局部结果不证明任意LLM普遍收敛。离线校准成本无数字、硬件Not Disclosed、SLO不适用。仅报告：低bit局部退火配方/小增量，不在成熟mixed-precision原则外强建长期缺口。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_FIRST.md)。

### [OnePiece: A Large-Scale Distributed Inference System with RDMA for Complex AI-Generated Content (AIGC) Workflows](https://arxiv.org/abs/2601.20655v1)

2+2+2=6。§6 516–696、§9 764–777及conclusion811：one-sided RDMA可变消息，经CAS producer spinlock注册buffer/size环，busybit由consumer释放。短timeout解锁后旧producer可覆盖新数据，header checksum丢坏消息；证明只到环遍历，不到valid payload，且假设consumer不故障。§9丢消息不重传，称interactive user不等待；可靠delivery是可扩展但未实现，不能写exactly-once或lossless。v1正文未提供可比实验setup/table；intro称16×而结论称16% GPU降低，分母/workload/hardware/端到端成本Not Disclosed，不采用正面性能数字。仅报告：registered-buffer生命周期与有限liveness设计，不将注册地址擅称GPU驻留，性能/可靠性未授。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_FIRST.md)。

### [Dissecting Multimodal In-Context Learning: Modality Asymmetries and Circuit Dynamics in modern Transformers](https://arxiv.org/abs/2601.20796v1)

2+2+3=7。§2–4 91–260；A1 523–549、A3.7 689–711；135–145：2-layer RMSNorm/SiLU/RoPE decoder，GMM N8/L1=32/L2=16/D1=64/D2=32/eps.1，primary8192 vssecondary256类，B4；ICL query必须有同类exemplar，新类与label-swap分离IWL/ICL。SGD128 lr1e-3/wd1e-6到收敛（非fixedcompute），5seeds std<.03。先M1再joint M2 MLP增加alignment capacity可能避IWL捷径；更大单模态反而捷径。RoPE低复杂度反例不能外推一般多模态：highcomplexity N8各positional近满分。prev/induction头ablation .97→.199/.062，因果限该2层。去M2 .336、去M1 .063，非M1单用。earlyfusion从头共同训练[M1,M2,label]使邻label的M2主导，primary不是固定text身份。真实Qwen/IDEFICS观察有架构/数据混杂，§4.4.4不提供生产机制解释。必要命题已独立复核，Ch23 curriculum/label读取/容量反侧的窄差额实际写入并POST。

整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)347–349；root POST通过。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_FIRST.md)。

### [Self Voice Conversion as an Attack against Neural Audio Watermarking](https://arxiv.org/abs/2601.20432v1)

2+2+2=6，安全反侧深入。III–V90–329：同speaker输入经WavLM kNN特征重建或经加ECAPA speaker embedding的RVC重建；保内容/身份的能力假设，不需要获取水印key，却需要操作VC模型/计算环境。LibriTTS test-clean，ECAPA cosine/Whisper-L WER/UTMOS代理：GT1/.114/4.152，kNN.857/.115/3.941，RVC.748/.120/4.190；不是逐语义等价或人类身份不可分辨。五watermark DCT/AudioSeal/Timbre/WMCodec/VoiceMark，vocoder-only对Timbre/VoiceMark可不破坏，selfVC使1-bit extraction accuracy约.49–.54；近随机bit恢复不证明所有presence detector失效或未来水印普遍无效。额外10–30dB noise/64–192kbps codec固定同seed，重复不确定性及硬件/攻击成本Not Disclosed。仅报告：此原有防御训练畸变之外的具体表征重建风险，不能采用作者universal攻击/完美保身份，未形成已验证的新防御机制。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_NEXT.md)。

### [Detecting and Mitigating Memorization in Diffusion Models through Anisotropy of the Log-Probability](https://arxiv.org/abs/2601.20642v1)

2+2+3=7，安全风险深入。§4/5 106–170/249–262；A1 550–581、A3 714–719：Gaussian局部例子显示norm方向/距离混杂，不能推出norm只在isotropy有效。Theorem1除SPD需条件项近α无条件score且mode displacement小、r=eps+tau<1、非零score；A1三角/Cauchy证明对应cos下界，不证明所有memorized状态自动满足。Eq14检测实际上对同初始Gaussian xT人工t0/tT查询，不跑真实low-noise轨迹；高低noise加权合成，gamma logistic在20memorized prompts拟合，防止把局部理论当该输入分布保证。SD1.4/2，500/219memorized+500non，3seed均值/std、n1/4；AUC在SD2低于Hessian方法而TPR@1%FPR局部提高，TPR对seed更敏感。RTX A6000 48GB、Python3.11.5/DDIM，metric计时10prompts不含完整图片生成。MemBench prompt embedding GD改变当次条件，不是权重unlearning；SSCD下降与CLIP/aesthetic有质量取舍、5超参配置非5独立重复。仅报告：新角度低noise条件与测量输入的错配要保留，不授隐私证明或普遍消除记忆。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_NEXT.md)。

### [DiffVC-RT: Towards Practical Real-Time Diffusion-based Perceptual Neural Video Compression](https://arxiv.org/abs/2601.20564v1)

2+2+2=6。§3–6 107–159/351–370/455–475、C1010–1054、E1278–1305：latent compressor使用前已解码latent，frame reconstruction不在prediction loop，允许异步和跨frame并行；OTSM留前帧部分channels、warping losses仅train且有flow误差/occlusion假设。PixelUnshuffle本身无损不等整个压缩链无损；移VAE encoder损失generative prior、perception/distortion不同取舍。Vimeo90k train七阶段/Adam，HEVC/UVG/MCL-JCV评价cropped64multiple且排4animation；速度原resolution闲置机多次平均，不同评价样本处理。3090/A800/H800，U-Net/VAE因FP16 overflow改BF16、latent compressor留FP16；720p H800>30fps为吞吐。并行batch须batch-dimension OTSM传末样本channels到下一batch，原文明确N−1 frame latency；N8(H800/A800)/N4(3090)，饱和后compute转瓶颈。部分未开源基线原论文数字非同栈，不直接采用100×所有负载。仅报告：特定codec的in-loop latent依赖重构解耦与吞吐/质量边界，不授首帧SLO/跨codec语义等价或普遍零成本。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_NEXT.md)。

### [Can Continuous-Time Diffusion Models Generate and Solve Globally Constrained Discrete Problems? A Study on Sudoku](https://arxiv.org/abs/2601.20363v1)

2+1+2=5。§3/4/5 149–267/463–492/598–665、B770–805：同约3.3M四层8headTransformer、H128、dropout.01，flow/score分别300k迭代batch2000 RTX3090；score近终点需scaled目标。经验beta-noise drift未随噪声更改，原文明确不是exact probability-path sampler。生成与given-cells soft→hard约束求解的最佳path不同；constraint injection未系统ablate，单数据/架构，不外推dLLM。重要反侧B：DDIM no-dropout25000/25000 valid却仅1 unique，DDPM no-dropout21350valid/21350unique，不能用validity衡量distribution diversity。guided cost约1.8M模型评估/puzzle，不比经典solver高效，不授symbolic reasoning。仅报告：此toy模型的采样忠实度/约束搜索目标分离与validity-collapse评价盲区，不能把数学path关系等同实际准确分布。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_NEXT.md)。

### [SemBind: Binding Diffusion Watermarks to Semantics Against Black-Box Forgery Attacks](https://arxiv.org/abs/2601.20310v1)

2+2+2=6，安全增量深入。§3/4/5 155–280/760–790、D1282–1328、F1780–1834：private frozen DINOv2-Giant+MLP semantic hash（训练SemCon3M），辅助同prompt clean image产mask，sign-modulate latent；verify重算hash、invert50step解mask。σ加强binding同时减benign robustness。SD2.1 512²/4×64²latent/CFG7.5/DPMSolver50，TreeRing/GS/PRC/GS++；COCO/SDP各100prompts vsI2P100，SD1.5/2.1 forged latent，理论FPR1e-6不是经验足量确认该尾概率。自适应D五同数据/架构/recipe不同seed masker码约半距，仅非识别对称，不证明通过oracle校准不能克隆；pixelspoof固定cat覆盖一类，≤.8仍距大/.9骤降，不授所有adaptive attack安全。额外clean generation及hash训练有真实代价，不能零开销。F证明独立mask/π挑战latent+Gaussian sign/permutation不变性和对postprocessing闭合的distinguisher class；仅继承base undetectability，不能继承防伪保证。t-test未显著/FID好不证明分布不可区分。仅报告：该key/privacy与辅助generation接口的局部防伪结果，不授一般语义认证或所有base都provable。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_MIDDLE.md)。

### [Decomposing multimodal embedding spaces with group-sparse autoencoders](https://arxiv.org/abs/2601.20028v1)

2+2+2=6。§3–5 82–156/214–225、A1 510–541/A2 541–557：已aligned dense embedding的TopK SAE可有modality-split support；L2,1 paired code penalty+shared随机mask引联合support。Theorem1需paired unit positiveinnerproduct>c、nonnegative exact K-sparse split decomposition，扩大dictionary p+n、稀疏K+1，不证明固定p/K训练必达或causal neuron真语义。A1 GramSchmidt添加pair共享atom（同向退化可直接共享），存在性不是optimizer保证。CLIPViTB16/CC3M和musicfinetunedCLAP/Jamendo30s，d512、p8192/K32、25k/10ksteps、batch128/Adam；λ选择不令平均K下降，p选择匹配FEV。10kvalidation paired，MMS用另RN50/MSCLAP cosine代理，不是human conceptgroundtruth。ZS与dense保留不同，CLAP GSAE Genre .705/MGSAE .672 vsdense .710，非所有指标best。概念命名依text/image alignment，probe“blonde”相关性≠causal验证，重复CI/硬件Not Disclosed。仅报告：局部SAE对齐及解释命名可靠性条件，尚不改通用representation干预结论。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_MIDDLE.md)。

### [$\mathbb{R}^{2k}$ is Theoretically Large Enough for Embedding-based Top-$k$ Retrieval](https://arxiv.org/abs/2601.20844v1)

2+2+3=7，几何瓶颈设计反侧深入。§2/3 97–199、§4 199–232、A1 351–386、A2 386–426：任意所有≤k subset严格分数间隔，允许每subset独立query向量和无限精度/无margin保证。cyclic polytope k-neighborly给2k linear空间存在，VC下界k−1；cos lifted n+1保持可分；不能授可训练encoder/自然query分布/finiteprecision部署保证。centroidquery额外约束，上界O(k²logm)独立Gaussian pairwise concentration+union bound；A2 Eq10/11正文norm平方/正负界有笔误，不照录完整证明正确性，Θ(k)基本存在与centroid高概率上界分别保留。Adam lr1/max1000step hinge-free embeddings只找到upper bound，不到真实语义检索端到端；优化失败不能下界。必要理论边界已独立复核；Ch76实际已有表达容量≠learnability/precision论点，不以‘所有失败都是learnability’改普遍结论。

已有覆盖：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)225–231/302–307，表达容量≠训练/有限精度可执行，root实际NoDiff通过。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_MIDDLE.md)。

### [Training Reasoning Models on Saturated Problems via Failure-Prefix Conditioning](https://arxiv.org/abs/2601.20829v1)

2+2+2=6。§4.2 141–171、§5/6/7 224–259、A509–562：先找稀少错误rollout，枚举prefix重新采N后选成功率近τ=.5，训练从失败中间state起，恢复group reward variance而非仅增rollouts；预生成/搜索预算不在训练step相同保证内。DeepSeekR1distillQwen1.5B，MATH7.5k/DSR40.3k以32sample里31correct筛1000；sameGRPO16rollout/response6000、4GPU type未披露、batch160、lr1e-6/cliphigh.4/low.2/KL0。5mathbench temp.6/32samples/max32k pass1/32平均43.4 vsbase40.6/saturated40.7/medium43.2；单训练run/未CI不授所有模型收益。176共同有正负解子集30%failedprefix降11.5point vsbase23.8，而correctprefix增5 vs8.4，有回退tradeoff与选择偏差。下一轮128attempt滤440remaining新前缀44.0，前缀随策略可能offpolicy；MDP解释依‘not excessively offpolicy’，不是通用无mismatch理论。仅报告：该饱和数据/失败前缀搜索与训练成本边界，不把成熟variance原则或passk改善当能力普遍证明。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_MIDDLE.md)。

### [Reward Models Inherit Value Biases from Pretraining](https://arxiv.org/abs/2601.20838v1)

2+2+2=6，设计反侧深入。96–119、241–273：10领先RewardBench Llama/Gemma RM，54正负prompt、BigTwo263/MFD2040词，mixed-effects/多重检验，用共同token子集避免部分tokenizer差；价值词rank不是完整人类价值或实际RLHF政策。对pretrained/instruct logprob与新RM沿训练观察，Llama3.2 3B vsGemma2 2B不同大小/架构/pretrain均有混杂，不能隔离某pretrain机制因果。控制same LoRA r32/a64、AdamW1e-5、batch16、seq1024、2epochs/固定seed，Skywork80k、UF13/26/53/106k；checkpoint1000steps。两轴差缩小但原80k不闭合，~100k可减Llama/Gemma差，Qwen与GRM保generative regularizer反侧不随数据充分闭合；GRM632k为他人产物非samecontrolled，机制待核。硬件/重复trainCI Not Disclosed。仅报告：词级评价说明init family与RM objective不能由RewardBench rank或配对数量自动消除，不授模型价值本体/普遍100k阈值；具体机制尚未披露，不改书主干。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_RL_SECURITY.md)。

### [DenseGRPO: From Sparse to Dense Reward for Flow Matching Model Alignment](https://arxiv.org/abs/2601.20218v1)

2+2+2=6。§4/5 158–244/371–407、Appendix631–659：每中间latent用n步ODE完整还原后reward，相邻reward差group归一作步advantage；noise强度按正负reward balance离线校准后固定，不是训练中online调噪。n1可差于FlowGRPO，不证明任意clean-domain评价准确：ODE路径特定潜在回报不是counterfactual真实因果credit。SD3.5M，三task GenEval/PickScore/OCR、train10step/eval40step、G24/512²/KL.04或.01、16A100、LoRA32/a64、AdamW3e-4/batch144。20trainsteps n1/2/t成本11/13/19GPUh；同时间图显示局部收益，不能只报same steps或免费dense reward。CoCA改造成Flow版本非原实现直接比较；DrawBench alternate评估及B4有rewardhack：count/OCR改善可能图质差。没有human safety/生产SLO，precision/重复CI未披露。仅报告：此flow训练的reward-domain误差、调噪与compute代价边界，尚非所有denoising目标适用的可靠credit理论。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_RL_SECURITY.md)。

### [Reinforcement Learning via Self-Distillation](https://arxiv.org/abs/2601.20802v1)

2+2+2=6。§2 154–177/214–239/271–307，code§4 450–491、Table6 601–641、TTT679–708、limits748–765、hardware1836–1840：当次策略feedback-conditioned teacher stopgrad，用logitKL自蒸馏，无额外teacher generation但需teacher logprob；top100+tail节省logits内存，EMA/初teacher插值+JS稳定。LCBv6 131问题train publictests为private随机50%子集，Qwen3默认8B，4rollout验证48.8vsGRPO41.2局部，不与榜单他模型不同协议直接比；Qwen2.5 1.5B可劣于GRPO。Table6环境+同batch成功解互补，只有solutionsteacher42.4但student36.8/entropy.07，加原attempt也偏teacher、降低探索。TTT hard19/veryhard9按任何方法512steps/5seeds至少成1次预选，bootstrap90%仅5seeds；discovery budget不含梯度全算力，不能认为未选不可解所有问题皆改善。4GH200378GB CUDA12.8/Pytorch2.7/FSDP2/vLLM，wallclock排initialization/validation；小模型短rollout开销更大，misleading/uninformative反馈可失败。仅报告：具体feedback-owner与selfteacher容量/探索条件，未在通用‘反思必纠错’成熟原则上强制造diff；科学domain只说明方法评价范围，不纳入AIforScience应用链。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_RL_SECURITY.md)。

### [DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation via Context Poisoning](https://arxiv.org/abs/2601.20615v1)

2+2+2=6，安全深入。III/IV 129–198、V199–225/530–581、VI922–931：攻击需可污染检索库、源模型梯度，hypothetical-query对待检索code近似实际query；1–3样本使被retrieve为必要触发，不是无检索/用户权限系统普遍漏洞。EOS/diversity/KL proxy+multi-position/buffer mutation，KL放loss指导，不是已证明输出非trigger位置完全不可区分/功能等价。RepoEval373/1.7Mfiles、Odex945/34kdocs，BM25/context2048/output1024、两A10080GB，10mutationiter/64candidate；source2code+2general。NVML GPU energy/latency不含CPU/memory、平均请求非SLO/concurrency，无安全非劣保证。黑盒transfer也有最多9%Pass1降低，与summary95–99%accuracy/‘preserve’不一致，不能抄‘准确率不变’。poisonprep216/53.2s对760/185.9为攻击自身成本不是受害服务加速；10repeat固定seed残差未全面CI。仅报告：具体检索注入可保一些tests却浪费资源的可行性风险，不授所有retrieval/future防御失效、攻击完美语义保留。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_RL_SECURITY.md)。

### [AgentLongBench: A Controllable Long Benchmark For Long-Contexts Agents via Environment Rollouts](https://arxiv.org/abs/2601.20730v1)

2+2+2=6。HTML未提供正文，必要官方PDF；本地`V3_CORE_2601.20730_PDF.txt`保留main原源web行号，§2–4/P3–9实际已读；定点Appendix E/P23原源L666–681已读。环境为有限Pokémon属性与确定性oracle，rule-based轨迹离线拼接成问答，不是模型真实online执行整个4M-token交互。Knowledge-Free用实体/属性符号替换，减少参数知识线索，不证明消除所有结构偏差。Concise工具已经求交，Verbose分别列属性候选、由模型求交；同token长度又意味着不同回合数，因此二者不是只改变密度而固定计算要求/时间跨度的因果控制。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_TAIL.md)。

### [When Flores Bloomz Wrong: Cross-Direction Contamination in Machine Translation Evaluation](https://arxiv.org/abs/2601.20858v1)

2+2+2=6，设计反侧深入。§2/3物理82–112、§4/限制163–190，Appendix C/D381–401：FLORES200 dev997、15语言、Bloomz7.1B与Llama3.1-8B。Bloomz已披露含FLORES训练，Llama只是无报告使用，不是经证明clean control。BLEU被明确当词形重合诊断、COMET语义指标，80BLEU/.9COMET等阈值不是严格membership证明。目标侧高分、异语源/回译/改写仍可召回目标；另语料Tamil/Malayalam/Odia near-zero支持泛化不足，也含语料分布差。Aya实体替换降低5–20BLEU，但作者承认词形屈折与实体数量改变会混杂。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_TAIL.md)。

### [P2S: Probabilistic Process Supervision for General-Domain Reasoning Question Answering](https://arxiv.org/abs/2601.20649v1)

2+2+2=6。§3物理127–179，§4/appendix336–351、631–647：ground-truth answer条件生成GoldCoT，过滤think/answer格式后按答案似然选；不是独立验证每步逻辑。prefix等步切分后看gold suffix最大条件概率减maskprefix基线，末步直接答案概率，sigmoid/late weighting与ROUGE混合。内部probability差只是一种process代理，错误但高似然路径、替代正确推理可能被错误排序，不授causal faithfulness。每题K+m² forward，不是免费verifier-less，也需要answer标注。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_TAIL.md)。

### [Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation](https://arxiv.org/abs/2601.20614v1)

2+2+2=6。§3物理128–238、实验540–560/640–668、Appendix B.2 1128–1139、F1211–1265：非uniform reward组以mean absolute deviation归一，sum|adv|=G在非零分母下是代数恒等；GRPO binary对应2G√p(1−p)。但实际gradient含logprob gradient、clipping/importance/length等，B.2明确它仅在响应梯度范数相近、方向少抵消假设下是proxy而非相等。不能把等优势总量说成每题实际梯度必相等。difficulty weight以valid query平均reward加softmax T2，权重比例有exp(.5)≈1.65范围，不是无限硬题优先。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_TAIL.md)。

### [Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale](https://arxiv.org/abs/2601.20276v1)

2+2+2=6。§3物理248–306、实验527–561：326M tokens/160,280 docs/9datasets是MemoryBank证据池；39,860→9,621→3,457→882→483筛选并非483独立随机题。query-answer-reference三元组人筛、单/多hop改写，用Qwen3Emb8B mining与collision test把conflict排、hard negative保、false negative加入reference。LLM-verified集合并非独立全库gold truth，retriever mining会产生偏差。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_TAIL.md)。

### [Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis](https://arxiv.org/abs/2601.20103v1)

2+2+2=6，安全深入。§3物理116–153、§4/5 153–207、Appendix H807–826：ClaudeOpus4.5按10类taxonomy合成trajectory，最终517（249benign）/54任务/37software contexts，平均26utterances。三位日常用coding agents的fullstack engineers独立标合理性/hack种类/难度，81%acceptance、binary κ=.82支持注释一致性与情景现实性，不是实际运行全部攻击/验证causal rewardhack。39%多标签；用户接受中断操纵可误导detector，本身为细粒度语义反侧。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FOURTH_TAIL.md)。

### [HE-SNR: Uncovering Latent Logic via Entropy for Guiding Mid-Training on SWE-bench](https://arxiv.org/abs/2601.20255v1)

2+1+2=5。§3–5物理130–235：私有MoE-S linearRoPE与约十倍MoE-L YaRN，32K→128K各checkpoint；取SWE-benchVerified500成功轨迹（与SFT同合成分布）、只保Action，用regex/AST剔除标签/注释/格式。HE-SNR为targetprob/top10-renormalized entropy平均，仅target在top10且entropy超过(log3+log4)/2。PPL在MoE-L context extension200step恶化而SFT后Pass1改善，局部反侧说明top1 confidence与post-SFT任务表现不能混同。三次evaluation不等三次training。每checkpoint >10k SWE轨迹SFT3epochs；未披露准确参数/全部硬件、train预算与CI，500同目标benchmark成功轨迹指标选择并无独立heldout proxy验证。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FINAL_TEN.md)。

### [Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction](https://arxiv.org/abs/2601.20299v1)

2+2+3=7，安全/设计反侧深入。§3 131–216、C.1 795–819/C.2 819–846、D892–912/958–986：source提供答案后expert预测另一target的logprob增益，participant通过source角色支付；DPO取高/低score配对。honest等如实private signal，不必客观正确。Theorem1用共同prior及诚实reported probabilities的BNE，不证明任意实际LLM达到唯一truthful equilibrium；信息保留的可逆重标亦可能同信息。Theorem2新增不同prior条件需participants/experts iid来自同population、boundedPMI/跨prior概率比、large m/n，且只对Alg2先平均prob后log成立。主Alg1的for all t文字含self，证明/Alg2 excludes self，必要边界保留；主实验算法/理论接口不能无条件等同。未泛审其全部证明或实现。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FINAL_TEN.md)。

### [Minimax Rates for Hyperbolic Hierarchical Learning](https://arxiv.org/abs/2601.20047v1)

2+1+3=6，必要理论反侧定点。§2/3/5物理137–245/288–331，B.3 604–632：regular-growth树、branching固定、depthR增大，Euclidean k固定/半径B受限、predictor Lip≤poly(R)。几何pigeonhole只迫使存在远树叶近Euclidean pair；相应cut要拟合需指数Lip。hyperbolic curvature随logΔ/(λε)容纳树，canonical按depthuniform、parentprefix已知条件leafsampling/BSCρ噪声有限pathclass，depthwise estimator upper O(mR log(mR/δ)/((1−2ρ)²ε²))、oracle lower Ω(mR logm/βρ)。不是所有LLMembedding/classification皆双曲优越；upper/lower还含confidence/accuracy因子不同。

暂缓：中心理论证明缺口；本窗终态争议，不作正面证据/Books，重开条件见§4/5。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FINAL_TEN.md)。

### [When More Data Doesn't Help: Limits of Adaptation in Multitask Learning](https://arxiv.org/abs/2601.20774v1)

2+1+3=6。§2/3 61–117与§5 157–207：有限VC二元分类、所有task共享最佳classifier、Bernsteinβ/transfer exponents；adaptive只见source数据、不知哪源fair/noisy、没有targetdata。新构造fair与noisy都非常噪，去掉旧n<2/β−1限制，却仍要求N≥n^(nβ/(1−β))超级指数及分布随n/N设定。Theorem5.2的‘arbitrary n’不是固定现实task集合随每源数据增加仍无改善；oracle knows source order才达fasterminimax。pooling可近最佳adaptive、与知道结构oracle不同；作者明确poly(n)tasks是否可恢复adaptivity未决。必要定义/主证明sketch已读，不声称完整附录证明审计。仅报告：明确‘共享最佳解’不等自动可识别transfer-source质量；局部构造对实际Foundation multitask比例无可采用阈值，不把题名当more-data普遍失效。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FINAL_TEN.md)。

### [SA-PEF: Step-Ahead Partial Error Feedback for Efficient Federated Learning](https://arxiv.org/abs/2601.20738v1)

2+2+2=6。§3/4 123–270、§5 270–322、B1112–1161：本地先w−αe，再localSGD，压缩(1−α)e+g并保新residual；server另η，g本身已经含innerη0，两stepsize不可混同。contractive compressorδ、Lsmooth/unbiased boundedvariance/heterogeneityβ²ν²、s=η0LT≤1/8、ρmax<1/Θ≤.5等方有stationarity bound；constantstepsize保variance/heterogeneity floor，非精确消除compression。正文‘milder compression largerδ’与Definitionδ=d/k方向相反，不采用这句。α近.84–1理论小s下强收缩不授任意α通用稳定。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FINAL_TEN.md)。

### [Look in the Middle: Structural Anchor Pruning for Scalable Visual RAG Indexing](https://arxiv.org/abs/2601.20107v1)

2+2+2=6，反侧深入。§3 100–140、§4/5 470–560、F3037–3088：只visual↔visual attention columnsum、headmean/max与固定40–60%depth平均选patch；OSR为pruned/full MaxSim比分，不等语义等价；比值denominator为0/负时解释须额外条件，不授所有query通用0–1fidelity。ColPali/ColQwen2/Jinav4、ViDoRev1/v2，AdaptiveEOS quantile对齐keepbudget、random/cluster baselines；10/20%keep局部约90/95%原NDCG。LightColPali25×compression仍更好、differentfullmodelupperbounds，不说无训练总胜。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FINAL_TEN.md)。

### [What's the plan? Metrics for implicit planning in LLMs and their application to rhyme generation and question answering](https://arxiv.org/abs/2601.20164v1)

2+2+2=6。§3/4 145–227、总结268–279：10rhymepfamilies/20pairs，Claude3.5 105lines每family train85/test20、test每prompt50samples；noun20pairs vowel/consonant train13/test5+7neutral。Gemma2/3/Qwen3/Llama1–32B base/instruct23models，单token residual mean-difference steering m1.5，layer/position取最大effect。原公式把两项都标C1相减为0，与prose C1/C2冲突，采用prose实验思想但不授公式/代码正确；max选择未说明独立heldoutselection，可能偏高。原train数据足够小、20nounpairs不能普遍taskplanning理论。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FINAL_TEN.md)。

### [One Word is Enough: Minimal Adversarial Perturbations for Neural Text Ranking](https://arxiv.org/abs/2601.20283v1)

2+2+2=6，安全深入。§3/4 99–178、270–281：query-aware doc可修改，300d lexicalcenter one-word插首/词替换，whitebox top20gradientpositions实际score择优；不是不知query/blackbox皆91%。MSMARCO8.8M、TREC2019 43queries/2020 54、BM25top100后BERT/MonoT5base rerank，top10排除，PRADA改为同whitebox而非原blackboxprotocol。SR仅排名有一点提高，RB/SB分开，USEcos~.98非句义不变或人类coherence证明；‘one word’可为tokenizer多tokens。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FINAL_TEN.md)。

### [TABED: Test-Time Adaptive Ensemble Drafting for Robust Speculative Decoding in LVLMs](https://arxiv.org/abs/2601.20357v1)

2+2+2=6。§4/5 327–415、B1113–1124、G1565–1624：共享同drafter参数，把multimodal/textonly输入作为batch并混prob；用target已验证hist hard/softlabels在pastwindow挑ensembleweight，缓存历史q/p；没有新增training但多输入forward/cache/historysearch成本仍真实。主窗口ALL，未授在线history新条件最优理论；model68/160M LLaVAtraineddraft、targetLLaVA1.5/NeXT7/13B，single/multiimage与followup、5imageOOD，gamma5/greedy/output128。单drafter跨turn不稳定，dynamic对static/random局部消融支持权重选择。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FINAL_TEN.md)。

### [Evolutionary Strategies lead to Catastrophic Forgetting in LLMs](https://arxiv.org/abs/2601.20861v1)

2+2+2=6，设计反侧深入。§3/限制72–138，A379–420：Qwen2.5-1.5B/Llama3.2-1B，4mathreasoningtask/200trainexamples、population30与GRPO30rollouts/batch200/minibatch32/500epoch plateau提前停。peakvalidationselected、sameupdatecount并不是matched total compute：ESno-backprop vsGRPOgrad/KL.001，fp16替bf16与chattemplate也调了ES。Table1除LlamaGSM8K多劣于GRPO，LlamaCountdown15.2vs37.6甚至不支持统一‘within3–4points’。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_FINAL_TEN.md)。

### [MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization](https://arxiv.org/abs/2601.20577v1)

2+1+2=5，标准。原同形任务不能直接重放轨迹→§4.2/4.3 定义相同任务/机器人/依赖结构下，低 overlap 区域内几何变换和高 overlap reusable segment ratio→必须先判断 motion reuse 条件，再复用高层计划或局部轨迹。物理原文186–224，评价263–294、377–398；直接反侧 Appendix D/E 953–985。概率乘法 Eq4 未明确独立/逐单位恒定失败率，不能采用为 success lower bound。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_QUERY_SEVEN.md)。

### [SAPO: Self-Adaptive Process Optimization Makes Small Reasoners Stronger](https://arxiv.org/abs/2601.20312v1)

2+1+2=5，标准。PRM评分与reasoner分布失配→score-gap预测位置后仅核相邻两rollout并迭代同步verifier→局部纠错/预算接口。实际108–131 Eq8–13、346–383 实验及反侧。Eq9是 c_j−c_(j−1) 却argmax作first error，case(b)/(c)预测与真t不等方向及重复端点有逻辑/符号疑点；不证明实现错误，亦不宣称首错定位必然正确。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_QUERY_SEVEN.md)。

### [Reinforcement Unlearning via Group Relative Policy Optimization](https://arxiv.org/abs/2601.20568v1)

2+2+2=6，因明确 formal/security contraction claim 加深受影响推导。原 forbidden-mention reward→作者Theorem1采样mixing下点态收缩→若成立会改变unlearning验收。实际Eq13/16/17、Assumption1、Appendix A.2 Eq33–37 已读且 root 定点实核。全零reward组归一advantage为0；policy=reference时KL梯度也0，PPO clip不强制每个forbidden sequence (1−ηε) 收缩。不能从clipping或effective mixing叙述推出该必然收缩；不是用证明错排除潜在贡献。

暂缓：词集合proxy不等删除，all-zero advantage/KL反例不支持点态contraction；不写Books。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_QUERY_SEVEN.md)。

### [CE-RM: A Pointwise Generative Reward Model Optimized via Two-Stage Rollout and Unified Criteria](https://arxiv.org/abs/2601.20327v1)

2+1+2=5，标准。各response自拟rubric可不一致→query-only共享criteria与criteria/chosen/rejected三条件adv分组→评分条件身份需保留。92–114 Eq1–3及controlled Qwen3-Max统一/各自/隐式criteria；379–410 Eq8–10和训练；562–577 RL实践/直接限制。不是把benchmark≠RL成熟结论算新增。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_QUERY_SEVEN.md)。

### [Memory Retrieval in Transformers: Insights from the Encoding Specificity Principle](https://arxiv.org/abs/2601.20282v1)

2+1+2=5，标准。词与recall相关不足定位使用→匹配数量随机token的K perturbation反侧→可区分targeted cue影响与普通破坏。100–138方法；138–171结果/限制已实际读。Counterfact等token长度prompt Q/K/V swapping仅input、首token后恢复，first-word exact match/Δlogit/PPL；Gutenberg input512/output40/step30只取原模型ROUGE-L Recall=1，集合随model变化，是选择后memorization slice。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_QUERY_SEVEN.md)。

### [Spark: Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning](https://arxiv.org/abs/2601.20209v1)

2+1+2=5，标准。uniform rollout浪费局部步预算→policy生成<explore>触发forest分叉、active-leaf N封顶→信号与预算执行接口分开。128–187 Eq3–7；228–247、499–530及1051–1057必要评价/配置；626–630直接能力限制。标签是policy proxy，不是已校准epistemic uncertainty。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_QUERY_SEVEN.md)。

### [Trajectory2Task: Training Robust Tool-Calling Agents with Synthesized Yet Verifiable Data for Complex User Intents](https://arxiv.org/abs/2601.20144v1)

2+1+2=5，标准。最终DB outcome可遮蔽中途forbidden动作/intent改动→动态intent与forbidden action evaluation接口→任务验证不只最终成功。140–206、457–481原core已获root准入；361–393与455–489必要评价/限制实际读。不是POMDP+SFT pipeline本身准入。

仅报告：采用该笔记列明的局部证据/受控反侧，不授普遍正确性、性能或部署保证；具体为何不改变长期知识见笔记。[完整必要证据与直接反侧](../_sources/daily-20260130/V3_EVIDENCE_QUERY_SEVEN.md)。

### [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR/blob/9567667698f195fa807b1581de5c03184e63d2b0/README.md)

2+1+2=5，标准。官方News Jan29支持自然日；初始commit只锁定artifact，不代替公开日。精确Jan29 README及stream example实际核读：offline/streaming共享ASR模型，流式仅vLLM、无batch、无timestamps；另设NAR forced aligner给文本—语音词/字时间。example保存unfixed_chunk_num=2、unfixed_token_num=5、chunk_size_sec=2，持续更新state.text并在结束独立finish；支持中间状态/最终刷新分支，不证明中间文本不可改或对外不可撤回commit。2000倍数字缺必要硬件/precision/长度/总预算，不采用。未运行示例/GPU或评价时间准确度。

仅报告：MULTIMODAL-REPRESENTATION Ch23 §Full-duplex的channel-local状态/safe point/不可撤回输出（470–491）及§时间空间的timestamp proposal/时钟provenance（717–760）已承载对应推理链。公开局部runtime接口有贡献，但此版本未带来新的稳定适用条件或质量/成本反侧，不强造Books差额；不是整家族MechanismNotDisclosed。[必要原件/实际owner比较](../_sources/daily-20260130/supplement-source-owner-pre-20261008.md)已获root Source/PRE实核。

### [PaddleOCR-VL1.5](https://ernie.baidu.com/blog/zh/posts/paddleocr-vl-1.5/)

2+2+2=6，重要release受影响内容深入。Jan29官方公告直接支持不规则polygon定位、spotting和基于OmniDocBenchv1.5的Real5五类scan/skew/warping/screen-photo/lighting。原必要核心与公告能力/评价/速度段复用实核；架构图/公告未分离polygon、数据与训练共同变化，94.5不可归因polygon或认证所有畸变。单A100/batch512速度协议含PDF渲染与Markdown、各系统默认DPI/模块；precision/concurrency未披露，不是同输入/同模块单因素收益或单请求latency。未运行/复现，后续论文不重复计首公开。

仅报告：Ch23四层identity/region与reference-frame（16–35、717–741）及PLATFORM-EVALUATION-SYSTEM Ch66 clean/corruption、低光处理链身份与实际相机失配（761–783）具体比较后，新版本能力/五slice保留为本地事实；公告尚不足改变该稳定机制/有效条件/受控反侧，不强写两owner。[必要原件/比较](../_sources/daily-20260130/supplement-source-owner-pre-20261008.md)root Source/PRE通过。

### [Inside our in-house data agent](https://openai.com/index/inside-our-in-house-data-agent/)

2+2+2=6，标准；producer-derived Context gap定点深入。官方How it works/六层Context/Runtime Context（必要正文95–137）支持从生产代码补表filter、grain与更新语义，每日离线归一化/检索相关定义，缺或陈旧时live warehouse/metadata查询，用户确认后持久Memory。Evaluation/Security（148–161）的golden SQL/result比较与pass-through permissions是该内部工作流的作者说明，不是controlled分层收益、独立安全认证；lessmore/guidegoal（165–173）是局部经验非普遍prompt定律。hardware/precision/batch/concurrency/SLO未披露且无性能数字采用，未运行内部实现/复現。

整合：唯一owner AGENT-CONTEXT Ch75 §Context Serving新增127–129两段，CodeNib后/SPADE前：schema/query-history为何合理但遗漏producer逻辑→代码派生视图→实时观察/确认Memory权威分界；保留离线维护/stale-view成本、原代码/live/人工回退与小语料直接查询。Ch76离线索引发布与Ch77持久写入分责不复制。root实际必要Source/owner PRE通过；114–140完整邻接、两段及末注771非作者实际POST通过，窄锁释放。[差额与拟文记录](../_sources/daily-20260130/supplement-source-owner-pre-20261008.md)。

## 5. 缺口与下一步

普通待办：无。原63证据与5处Books POST复用，补3必要证据、Ch75实际POST及六部分独立DAY均通过；下述15日期材料、历史缺段与2争议是精确隔离的终态保留，不冒充正面证据，不删原反证。

本窗外部保留：早Submitted的19910/19917/19921/19918/19956/19923/19960/19942/19908/19912/19904/19961/19952/19935/19944缺官方Jan29公告day或足以约束首次公开的精确lead；Created只能上界、普通schedule不能替早稿证明本窗下界。19912仅定点303–313/395–404已确认scale/task/SDC-vs-DUE局部反侧，19904仅479–495确认SN30跨机TP利用率/吞吐反侧；都不因日期障碍删潜在贡献，不继续全文。可接受原材料为具名官方Jan29公告/正式原刊firstpublic或原始timestamp；得到后只重开对应材料，本次不得正面采用或进入Books。具体贡献已关闭的early稿不为无关日期追查。19944原‘非LLM排除’已纠正为IID tabular proper-score校准退化窄贡献，仍日期隔离。

旧17日期hold中的Qwen/Paddle已依官方Jan29日粒度补入本次自然日，原小时门限不延续到新增；不借其arXiv Submitted，也不由commit推公开日。其余15 early稿当前abs身份/notes与四个代表精确官方identity+Jan29查询作有限恢复，仍无announcement-day下界；已有19912/19904有效窄反侧与19944纠错复用，不重建全文队列。机构历史缺段仍逐源见§2，后续具名原文/可恢复目标bracket才定点重开；空页不能算历史0或全Coverage。

中心争议终态：PURGE20568缺与实际GRPO更新匹配的contraction证明，全部zero-reward组/零KL梯度不能由clipping强制收缩；20047 Cor22所需大δ-separated packing不由close-pair结论建立，且下界函数类不等有限hierarchical H。两项不支持任何正面采用/Books，重开仅正式勘误、与实际条件一致的证明或独立可支持的新窄命题；不继续无关附录。

窗外恢复线索（不阻塞本窗）：[DIT](https://proceedings.mlr.press/v267/dong25d.html)已有ICML2025/PMLR267公开；贡献入口5有效但本日arXiv收录不是新首次公开，不处理2025整份日报。外部保留与争议不支持正面Evidence/Books/无遗漏或安全性能保证。

## 6. 复核

复核者：root（独立非作者）。

结论：通过

原稿63及5处Books的既有独立通过记录如下保留；补查3准入与分层关闭、必要官方源/实际owner PRE已由root实核；root实际顺读Ch75 114–140、末注771及完整6行新增差额，POST通过，窄锁释放。root随后独立核本次六部分：3准入/所有必要Source/两Only/Ch75 POST、来源有限停止、15日期+2中心争议隔离，原63行/原窗口/原§4连续块逐字保留。DAY通过，返修旧/新增候选衔接为同一完整表及旧机器统计归属后完成；不是重复泛读原63或全附件。

已实际独立读118完整题摘，来源/主题/理由校准覆盖全部拟入选和有纠错/安全/设计反证的排除：撤回SwitchCodec、旧公开Insight、SEER未建立shared-space保证、PURGE中心反证保留；其余明确EX在首六批完整题摘逐项校准，未称全量全文审计。成熟recipe借原则、主题关联、StructAlign/Gap-K/Drift/MobileBench/CtrlCoT等误收已纠正，19944非LLM一概排除已重开。

63项必要命题全部分批实际复核：第一/二15、第三9、第四22、最终10、QUERY7；实际检查证据笔记及决定性原源（不是第二次全文审计），包括PoT maximize/minimize符号、CI跨0不等非劣、dPLENA sampling-only、低AUC/模拟性质、K=0不等softmax0、PURGE全零组反例、20047证明缺口。所有Only/Existing理由经实际核；MED Ch76具体覆盖与Peer ideal-PMI/private-signal≠truth均NoDiff通过。

Ch45/56/23/5/66的实际正文/邻接/末注非作者POST均通过，窄锁释放。root已实际核来源有限入口/查询/停止范围、窗口和63 metadata（Submitted同公告deadline批，Created窗内）、六部分字段与终态隔离，MiniMax Agent必要入口空壳不报历史0。五处POST与One Existing/55 Only/两Disputed算术和边界一致；这是实际报告/必要命题复核，不第二次全文审所有附件。保留项不授正面Coverage/Evidence或Books。

原稿机器检查：当时进行态与完成态V3均实际通过（完成态首次结论字段尾句号不被解析，改规范字段后复跑；未改校验器）。原17份自写Markdown的78个本地引用、代码围栏配对及尾空白检查通过，原63唯一家族及5/1/55/2处置一致；原本日与5个owner限定cached/unstaged diff-check通过。该旧记录不代替本次检查。

补查机器检查：进行态与完成态V3均实际通过；当前66表行/66证据段与6整合/1已有覆盖/57仅报告/2争议一致，报告84个本地引用0断链。原63表行与§4原连续块逐字未改，原稿基线SHA256为f6e9d3190c61fe6764ceceee45935e04cfe437a23a5b81d186e1ea0fa1769927；基线内相对链接按原报告目录解释，不当新证据。本日/Ch75限定cached/unstaged diff-check实际通过。机器只确认格式与明显一致性，不替代语义审阅。未stage、commit、push，Ch75原cached12行及无关dirty均保留。
