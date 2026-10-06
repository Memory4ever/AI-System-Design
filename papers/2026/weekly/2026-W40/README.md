# Weekly Research — 2026-W40

**规范：** V3
**窗口：** 2026-09-27T09:00:00+08:00 ～ 2026-10-04T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T16:22:00+08:00

## 1. 结论

本周最重要的关系不是“又发布了几个框架”，而是从**形式正确 → 表示与寿命正确 → 真实效果与批准权限正确**补齐执行边界：CUDA 的具体 compiler/library 纠错、SGLang refit 的 checkpoint/kernel 表示转换、FlashInfer prepared attention 元数据跨 capture/replay 的寿命、Transformers 缓存与重算的配对生成回归、Olmo-core packing 的权威边界源，以及 METR 人审 principal 的隔离，分别落在已有 owner，不混成一套万能安全状态机。Ray 的本地认证默认、取消竞态和 backpressure 状态码只是具名版本事实；GLM-5.3 cyber 评估将真实离线 exploitation 与不执行代码的模拟 engagement 分开，不能把它们合成攻击成功率。

复用[09/28](../../09/28/README.md)、[09/29](../../09/29/README.md)、[09/30](../../09/30/README.md)、[10/01](../../10/01/README.md)、[10/02](../../10/02/README.md)、[10/03](../../10/03/README.md)、[10/04](../../10/04/README.md)七份已完成 V3 Daily，实际窗口连续覆盖本周，未重跑日源。按论文 ID 与官方项目归并七日报表170行为169家族（OpenAgentCore跨日两项发布合一，事件仍分别保留），新增每周源7家族及具体 Daily 日期缺口补查1家族，合计177。不同来源的列表返回量不是新材料数，本次未统一统计原始命中，故不报“几百篇发现”。

当前作者已完成176家族的相应审阅及Books判断；CodeJudge中心充分性争议1家族复用安全终态保留，不算正面Evidence。Books处置为155家族整合（其中149沿Daily复用，6为本周真实窄差额）、7已有具体覆盖、14仅报告、1暂缓。新增改动只在Ch27/45/49/72四个既有文件；未另建知识节点。六处新增正文及前后邻接均已由root非作者实际写后复核通过，周级最终报告复核亦通过，普通待办0。不得由这些数量推断所有材料主张已证实或外部覆盖缺口消失；未运行GPU/发布包、复现实验或验证生产保障。

## 2. 来源覆盖

本周新增扫描仅29个每周来源；宽目录先收窄模型/训练/推理/平台/Agent主题，有日期序列越过起点或可见列表读到尾即停止。GitHub使用发布 `published_at`，100项page1的历史尾已早于窗口时不追Next。普通PR不转成逐项阅读库存；具名纠错/安全信号仅补受影响核心。原始检查在[周入口A](../_sources/2026-W40/RAW_WEEK_A.md)、[B](../_sources/2026-W40/RAW_WEEK_B.md)、[C](../_sources/2026-W40/RAW_WEEK_C.md)、[核心D](../_sources/2026-W40/RAW_WEEK_D.md)、[release元数据](../_sources/2026-W40/RAW_RELEASES.json)及下表指向文件。执行日期为2026-10-05，本次恢复不会移动历史窗口。

日源14行直接复用上述七份Daily §2及其原始记录，保留各日有限入口、查询、分页和具体限制；下表是本周联合范围，不重新抓取。七份默认窗口依次为Sep27→28、28→29、29→30、30→Oct1、Oct1→2、2→3、3→4的09:00截点；10/04已由root完成非作者总复核。完整逐家族归并见[Daily复用记录](../_sources/2026-W40/DAILY_REUSE.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 七Daily官方研究索引/RSS实际日期停点与具名core复用，Dots/Safety cases/Australia/Distillation已有独立审阅；非重抓 | 已检查 | GPT6.1Sol日精度/原时区未恢复，见§5；不把article日期猜为BJT |
| SRC-ANTHROPIC | 七Daily Research日期序列/有限首批复用；本周仅定点恢复GLM5.3 cyber原日期及完整96行核心 | 已检查 | Sonnet5.5仍缺首公开时区；artifact创建时间不替文章发布 |
| SRC-GOOGLE-AI | 七Daily DeepMind/Research Blog有界范围与Argon候选结果复用 | 受阻 | Google pubs年粒度/动态query和某些具体事件日期不足，见各日§5 |
| SRC-META-AI | 七Daily publications有序停点与Blog有限替代复用 | 受阻 | 部分空正文/混排序/不可达目录，旧卡和补检零结果不证明周零 |
| SRC-QWEN | 七Daily新Research/Blog shell、旧blog及官方组织有限替代复用 | 受阻 | 新站本周可归属公开目录仍缺；翻译commit非研究发布 |
| SRC-DEEPSEEK | 七Daily Updates/News日期序列及Harness具名release复用 | 已检查 | 后段新闻入口未全恢复，10/04 G4仍隔离；Harness正面证据独立 |
| SRC-MOONSHOT | 七Daily Blog/release有限替代与窗口停点复用 | 受阻 | 10/04 Blog超时G5，组织更新时间不能替首公开 |
| SRC-TENCENT-HUNYUAN | 七Daily publicList/论文身份核对及后段浏览器失败复用 | 受阻 | 后段动态“全部”目录不可读，10/04 G6；不以早一日页面替全周 |
| SRC-ZAI | 七Daily Research/release notes与Law完整排除核心复用 | 受阻 | 部分研究入口未恢复，10/04 G7；Law未披露增量不是按题名排除 |
| SRC-BYTEDANCE-SEED | 七Daily Research/public_papers有序首批、实际Blog限制复用 | 已检查 | 部分Blog历史窗口日期不明；8/5 SeedRealtime窗外不扩读 |
| SRC-BAIDU-ERNIE | 七Daily Blog page1/2首批10、README/release日期停点复用 | 已检查 | 只支持已读入口，不宣称全组织开发历史零事件 |
| SRC-XIAOMI-MIMO | 七Daily主页Paper8/Blog15线索、日期缺口与MiMo-Code PR核心复用 | 受阻 | repetition Sep27无时区触及周起点，其他无日期卡不全排；10/04 G8 |
| SRC-MINIMAX | 七Daily中英文Blog/techblog/changelog、Code/OAC具名发布与精确安全配置复用 | 已检查 | CLI0.5.8首公开时刻、部分无日期techblog保留；同项目跨日事件不重复评分 |
| SRC-ARXIV | 七Daily New身份与官方公告日程、题摘筛选、exact-v1证据复用，正常公告Sep28/29/30/Oct1与Oct2有限记录按各日真实边界处理 | 已检查 | Oct2公告/具名v2日期未恢复等原限制仍保留；周末无常规批次不是其他源零进展 |
| SRC-MISTRAL | [News](https://mistral.ai/news/)当前88卡只作目录；日期prefix Sep28→16→10→8，Munich完整核心后停止 | 已检查 | Munich组织/算力愿景无新机制；未逐88旧卡审阅 |
| SRC-AI2 | [Papers](https://allenai.org/papers)首10年标2026、Next；Latest首9 Oct2 AstaBrief/Oct1Olmo→Sep1→旧项，有限下一页旧项止；两具名core，OLMo官方31release无Next | 受阻 | 年标Papers不能证明周归属；Olmo release定时独立，blog首公开与报告日期仍不替换 |
| SRC-BLACK-FOREST-LABS | [Research](https://bfl.ai/research)3卡到footer，最新Mar3、后2025Nov25/May29 | 已检查 | 当前Research入口无周项，不外推全站 |
| SRC-PHYSICAL-INTELLIGENCE | [主页](https://www.pi.website/)/blog/research原入口403；两host直接429；一次限定官方域September2026补检无恢复 | 受阻 | 精确终态隔离P1；不能写零进展 |
| SRC-WORLD-LABS | [Blog](https://www.worldlabs.ai/blog)Research13+News6到footer；Sep28AMD→Sep1Atlas，公告core与同事件转述归并 | 已检查 | 组织并购非新Atlas机制，旧Atlas不深读 |
| SRC-SSI | [Updates](https://ssi.inc/updates)3项到页尾，最新Jul26→2025→2024 | 已检查 | 当前公开入口无周项 |
| SRC-REFLECTION-AI | [Blog](https://reflection.ai/blog)2项最新2025Oct9；[News](https://reflection.ai/news)当前7项Jul14→Apr23至页尾 | 已检查 | 仅这些公开入口，不以官方主页口号入选 |
| SRC-AMI-LABS | [Updates](https://amilabs.xyz/updates)1项Mar10到footer，主页任务宣言 | 已检查 | 无本窗具体研究发布 |
| SRC-THINKING-MACHINES | [Connectionism](https://thinkingmachines.ai/blog/)7项至页尾，Jul31→Jul10→May11→2025 | 已检查 | 无本窗条目，不遍历无触发旧版 |
| SRC-PRIME-INTELLECT | [Blog](https://www.primeintellect.ai/blog)52卡仅前日期prefix Oct2Inference/Oct1Extropic→Sep23止；两项具体core | 受阻 | Inference原字段仅2026-10-02无时区；Extropic既有GRPO应用关闭 |
| SRC-SAKANA-AI | [Blog](https://sakana.ai/blog/)Sep28SAIL→Sep25/24→18停止；SAIL官方短全文及arXiv2603.08269历史v1Mar9/v2Sep19 | 已检查 | IROS展示/传播没有具名新机制修订，原论文不重新评分 |
| SRC-RECURSIVE | [Recent Stories](https://www.recursive.com/)唯一Jun11 FirstSteps，当前首页到footer | 已检查 | 无本窗新条目 |
| SRC-MIND-LAB | 原入口redirect至[mindlab.im](https://www.mindlab.im/)，Publications6项Aug15→May12、Updates23项Sep22→Sep2→旧项，prefix停止 | 已检查 | [清理后的原始日期](../_sources/2026-W40/FINITE_METADATA.json)；未按23旧条目建队列 |
| SRC-SAND-AI | SandAI-org11repos/noNext仅窗口push作线索；MAGI1 releases0、MagiAttention13最新Sep18、MagiCompiler2最新Jul1，README具体news核到旧日止 | 已检查 | MagiCompilerOct1push不是重要研究事件；不逐普通commit |
| SRC-EVERMIND | [EverCore](https://evermind.ai/)2论文卡EverMemOS/HyperMem，官方arXiv历史Jan/Apr版本均窗前；landing无日期机制宣言 | 受阻 | 无日期EverMemOS活动不可定周，隔离E1；不是论文候选 |
| SRC-METR | [Research](https://metr.org/)recentSep30证词/Sep27monitor→Sep22止；Research/Notes到footer；两具体core | 已检查 | monitor是有限研究note不是全面有效证明；证词旧Aug26调查转述关闭 |
| SRC-PYTORCH | 发布API page1 70/noNext，Sep30v2.14.1→Sep2；本窗完整core及CUDA13.2.2精确条件 | 已检查 | 未复现MPS/CUDA路径 |
| SRC-MEGATRON-LM | 官方release46/noNext最新Sep18，README News最新2026May，越起点停 | 已检查 | 不把普通push换成贡献事件 |
| SRC-DEEPSPEED | API page1 100/有Next，最新Sep16、尾2021Sep14，早于起点不翻历史尾 | 已检查 | 本窗该release入口无项 |
| SRC-VERL | API16/noNext最新Sep20，前后元数据已越起点 | 已检查 | 本窗该release入口无项 |
| SRC-VLLM | API100/有Next，Oct5窗后、Sep22窗前、尾2023Sep11；不读Oct5正文 | 已检查 | 不移动窗外v0.31到本周 |
| SRC-SGLANG | API62/noNext，v0.5.21Oct2→Sep18；release完整核心+具名PD/refit/numerics/安全信号必要PR | 已检查 | 不把779条PR逐项关闭；局部默认/回归不授全fleet安全 |
| SRC-TRITON-LANGUAGE | API7/noNext最新Aug28，末2025Jul30 | 已检查 | 非Triton推理服务器入口 |
| SRC-FLASHINFER | API100/有Next，Oct2rc2/Sep30rc1/Sep29post1同家族，尾May26，读受影响numerics/layout/lifetime核心与必要PR | 已检查 | RC不是稳定部署验收；不重收旧Autotuner主题 |
| SRC-NCCL | API17/noNext，v2.32.3Sep17/nccl4pySep23，尾2025Oct6；核整页metadata避免仅首item | 已检查 | 本窗release入口无项 |
| SRC-HF-TRANSFORMERS | API100/有Next v5.18Sep30→Sep9，尾2025Jan10；完整release与cache/stop/fractional/core安全范围 | 已检查 | 模型support列表本身不准入 |
| SRC-KSERVE | API63/noNext最新Sep25，尾2019Sep24，越起点停 | 已检查 | 本窗release入口无项 |
| SRC-RAY | API100/有Next v2.59Oct2→Aug23，尾2020Mar25；具名auth、Hudi、lease与backpressure核心 | 已检查 | 远端default未改，CLIhead无token仍未认证；不称所有cluster安全 |
| SRC-MCP | API9/noNext最新Jul28，末2024版于2024Nov6公开 | 已检查 | 本窗release入口无项 |
| 表外：[OLMo-core](https://github.com/allenai/OLMo-core/releases) | Ai2 code明确触发，31/noNext、v3.0.0Oct1→Aug11，精确发布core（不声称PR843代码核验） | 已检查 | release事件不替未知首公开的techreport事件 |
| 表外：[CUDA13.2.2](https://docs.nvidia.com/cuda/archive/13.2.2/cuda-toolkit-release-notes/index.html) | PyTorch明确component纠错触发，仅Overview/Compiler resolved及known/cuBLAS同版本条件 | 已检查 | 不使用当前13.4页替代历史版本 |
| 补检：[官方域精确日期](https://www.anthropic.com/research) | 只对七Daily具名日期缺口恢复HTML metadata；GLM cyber取得带时区字段，Sonnet/GPT/MiMo未恢复；Prime/Ai2同范围字段 | 检索受限 | 搜索缺结果不等无条目，未定时材料只隔离 |

没有新增无差别按需扫描。已在Daily触发的按需材料和结果随对应Daily复用；本周只读精确证明所需的官方PR/同版本文档，不因材料引用DeepEP/DeepGEMM等名字扩大到整项目历史。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [New LoRA Skills Should Read but Never Write](https://arxiv.org/abs/2609.31600v1) | 2026-09-28T08:00:00+08:00 | Gauge坐标与单向block权限区分旧参数项与总函数；2+2+2=6 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)，Fed gauge后两段；仅有条件composition |
| [Evaluating the accuracy of KV cache reuse techniques](https://arxiv.org/abs/2609.31415v1) | 2026-09-28T08:00:00+08:00 | Baseline条件评价与warmup角色反事实修正reuse验收；3+2+2=7 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，PatchKV后两段 |
| [Generalization behavior of OPTQ and the role of regularization](https://arxiv.org/abs/2609.31560v1) | 2026-09-28T08:00:00+08:00 | 校准→population泛化的独立概率/正则条件；2+1+3=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，weighted-cover后两段 |
| [Beyond Mean Attention: Diversity-Aware, Layer-Wise Scoring for KV Cache Eviction](https://arxiv.org/abs/2609.30738v1) | 2026-09-28T08:00:00+08:00 | 构建集合的冗余排序与depth profile非普适收益；2+1+2=5 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，TwinKV后两段 |
| [EAServe: Encode-Aware Disaggregated Serving for Multimodal Large Language Models](https://arxiv.org/abs/2609.31551v1) | 2026-09-28T08:00:00+08:00 | Encode批等待/SM共驻与分流联动，但吞吐目标不同于SLO goodput；2+2+2=6 | 深入完成 | 整合：INFER-PD-DISAGGREGATION [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)，goodput→KV transfer两段 |
| [ActKV: Efficient LLM Agents through Action-Guided KV Cache Management](https://arxiv.org/abs/2609.31395v1) | 2026-09-28T08:00:00+08:00 | Action访问历史与round末预算/无冲突原位压缩；2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，LoopGuard后两段 |
| [CacheReforge: Bounded Recovery for Stale KV Caches under Evolving Adapters](https://arxiv.org/abs/2609.30884v1) | 2026-09-28T08:00:00+08:00 | 逐层参数anchor/位移及可执行restart与tail证书分权；2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，21362 seam后两段 |
| [Quantizing Looped Transformers: Feedback Exposure and Calibration Blindness](https://arxiv.org/abs/2609.30820v1) | 2026-09-28T08:00:00+08:00 | Loop-entry反馈位置与跨step Hessian覆盖是不同精度轴；3+1+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，OPTQ→PTQ两段 |
| [Low-Bit Recurrent States in Hybrid Language Models](https://arxiv.org/abs/2609.30950v1) | 2026-09-28T08:00:00+08:00 | 误差存活/readout方向与range共同限制state位宽代理；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，Fractional末两段 |
| [Softmax Reparameterization for Output-Head Quantization](https://arxiv.org/abs/2609.31291v1) | 2026-09-28T08:00:00+08:00 | 公共row shift等价与量化/非线性修正的权限不同；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，Greedy→ExactTopK两段 |
| [Deterministic Regime Switching and Feasibility Inversion in Dynamic Tensor Rematerialization](https://arxiv.org/abs/2609.31250v1) | 2026-09-28T08:00:00+08:00 | 重复eviction与pinned frontier使在线budget可非单调；3+1+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，activation保存/重算末两段 |
| [Block Sparse Attention with Log-Linear Complexity](https://arxiv.org/abs/2609.31093v1) | 2026-09-28T08:00:00+08:00 | 分层候选routing降低selector扫描但ancestor漏选不由leaf精确修复；2+1+2=5 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)，MiniMax sparse→selector forward两段 |
| [From Shortcut Learning to Discrete Neural Insertion Sort](https://arxiv.org/abs/2609.31114v1) | 2026-09-28T08:00:00+08:00 | 最终正确与逐步算法执行不同，discrete control仍需全局终止监督；2+1+3=6 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，25800→训练标准两段 |
| [Common-Mode Collapse and Recovery in Direct Feedback Alignment](https://arxiv.org/abs/2609.31589v1) | 2026-09-28T08:00:00+08:00 | 共享mean teaching低秩驱动与readout/optimizer的非单调collapse；2+1+3=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，01563→depth parameterization两段 |
| [Weight Pair Encoding: Inducing a Smaller Grammar in Neural Network Weights](https://arxiv.org/abs/2609.31564v1) | 2026-09-28T08:00:00+08:00 | 训练code-domain重复语法是独立压缩轴，不等kernel或位宽收益；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，PTQ/QAT定义→W4A16两段 |
| [Decodable In-Context State and Model Output Across Training](https://arxiv.org/abs/2609.31401v1) | 2026-09-28T08:00:00+08:00 | logits与argmax分权否证probe对错差直接等于信息丢失；3+1+3=7 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，独立reader→encoder移植两段 |
| [The Residual Stream's Effective Depth](https://arxiv.org/abs/2609.31098v1) | 2026-09-28T08:00:00+08:00 | 累积state几何需matched参照，不是无用层或pruning许可；3+1+2=6 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER [Ch17](../../../../books/part-02-model/17-transformer-layer.md)，分别检验→逐层替换两段 |
| [Convergence guarantees for Muon: New parameter regimes and generalizations](https://arxiv.org/abs/2609.30546v1) | 2026-09-28T08:00:00+08:00 | 有限NS、ideal sign与soft-sign代理的轨迹保证权限分开；2+1+3=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，18999→多Optimizer两段 |
| [MoSAR: Mixture of Semantic Attention Regimes for Learning Adaptive and Approximable Attention Geometries](https://arxiv.org/abs/2609.31261v1) | 2026-09-28T08:00:00+08:00 | pair geometry、top1、hard tail及kernel是不同变化；2+1+2=5 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)，13141→无法重训Target两段 |
| [G$^2$PTQ: Improving LLM Post-Training Quantization with Generalized Gradient Compensation](https://arxiv.org/abs/2609.31009v1) | 2026-09-28T08:00:00+08:00 | partial-quantized block刷新梯度/曲率与估计预算一阶补偿；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，LoopPTQ→PTQ/QAT两段 |
| [Nonparametric In-Context Learning under Growing Geometric Complexity: Minimax Optimality and Local Geometry-Adaptivity of Transformers](https://arxiv.org/abs/2609.31458v1) | 2026-09-28T08:00:00+08:00 | geometry-first comparator与prompt样本/训练任务双预算权限；2+1+3=6 | 深入完成 | 整合：WORLDVIEW-LLM-INTELLIGENCE [Ch8](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md)，context质量state→Post-training两段 |
| [Where a Model Sends Its Own Repeated Token](https://arxiv.org/abs/2609.31181v1) | 2026-09-28T08:00:00+08:00 | fixedpoint集合cardinality反证与source-paired destination/null/precision floor；3+1+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，subject身份→adapter例子两段 |
| [Stale-Document Poisoning: When Outdated Retrieval Overrides Correct Model Answers](https://arxiv.org/abs/2609.31342v1) | 2026-09-28T08:00:00+08:00 | metadata存在不等reader遵守有效期，RAG纠正与损坏须双侧评价；3+2+2=7 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，Temporal旧binding→权威后继两段 |
| [Beyond Approved Actions: Runtime Validation of Persistent Outcomes in Agent Workflows](https://arxiv.org/abs/2609.31301v1) | 2026-09-28T08:00:00+08:00 | effect profile、同candidate equality与backend capability分权；2+2+2=6 | 深入完成 | 整合：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，LIBOS旧binding→Discovery两段 |
| [Estimating and Orthogonalizing Unknown Pre-training Gradients for Continual Fine-tuning of Large Language Models](https://arxiv.org/abs/2609.30935v1) | 2026-09-28T08:00:00+08:00 | 虚拟更新搜索synthetic保护gradient与有限步/coverage权限分离；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，14010→EmbeddingNoise两段 |
| [MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2609.30837v1) | 2026-09-28T08:00:00+08:00 | base-relative专长方向与student教学方向的token级筛选/权重分权；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，debate→Self-distillation两段 |
| [Persistent Negatives for Adversarial Black-Box On-Policy Distillation](https://arxiv.org/abs/2609.30864v1) | 2026-09-28T08:00:00+08:00 | 历史完整比较仅训练RM，fresh groups仍唯一进入policy update；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，14071→混合Occupancy两段 |
| [Recursive Self-Improvement via On-Policy Distillation for Reasoning](https://arxiv.org/abs/2609.30652v1) | 2026-09-28T08:00:00+08:00 | 特权guidance与无gold改写的独立CE/admission分支；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，ContextDistillation成本→carrier两段 |
| [TISD: On-Policy Self-Distillation with Trajectory Intervention](https://arxiv.org/abs/2609.30878v1) | 2026-09-28T08:00:00+08:00 | teacher一次branch提案后由student采新suffix、原反馈监督新状态；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，privileged evidence→ContextDistillation两段 |
| [Highlight-Then-Summarize: Learning to Compress Evidence for Long-Context Understanding](https://arxiv.org/abs/2609.31382v1) | 2026-09-28T08:00:00+08:00 | E/S/A分开训练及预算反转限定过程目标；2+1+2=5 | 标准完成 | 仅报告：局部layout/harmonic奖励与参数—质量frontier，无一般aggregation因果或新通用知识缺口 |
| [Entropy Regularization: A Free Correction to Cross-Entropy for Verified Demonstrations](https://arxiv.org/abs/2609.30572v1) | 2026-09-28T08:00:00+08:00 | 演示likelihood、采样分布正确集合与token entropy proxy分权；2+1+3=6 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，masked CE→loss-mask示例两段 |
| [ViSTA: A Simple Bridge Extends Visual Alignment to Clinical Time-Series Understanding in Multimodal LLMs](https://arxiv.org/abs/2609.31448v1) | 2026-09-28T08:00:00+08:00 | 内部变量summary与原visual token残差桥的局部选择；2+1+2=5 | 标准完成 | 仅报告：同参数桥接口/任务frontier，不外推通用信息保留或临床效力 |
| [Strategically Diverse Sampling for Self-Training](https://arxiv.org/abs/2609.31571v1) | 2026-09-28T08:00:00+08:00 | 同题approach预分叉采样与correct过滤/策略覆盖独立；3+1+2=6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)，synthetic开头→行为树前两段 |
| [DynBranch: Speculative Subgraph Reuse for Dynamic Agentic LLM Serving](https://arxiv.org/abs/2609.31047v1) | 2026-09-28T08:00:00+08:00 | 未resolve候选的不可见shadow与setup/fill负载准入分开；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，Pythia→coldwarmup前两段 |
| [Authority at Commit Time: Reject-and-Rerun Semantics for Governed Agentic Systems](https://arxiv.org/abs/2609.31490v1) | 2026-09-28T08:00:00+08:00 | governing subset与admission/dispatch两时点的权限不同；2+2+2=6 | 深入完成 | 整合：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，runpin→Feedback两段 |
| [Low-Rank Friction for Memory-Efficient Transformer Pretraining](https://arxiv.org/abs/2609.30342v1) | 2026-09-28T08:00:00+08:00 | 平方momentum形成friction而非平方gradient缩放position；2+1+3=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，roleallocation→Embedding两段 |
| [Compact Documentation for Coding Agents: A Benchmark, an Optimizer, and Why It Does Not Transfer](https://arxiv.org/abs/2609.31587v1) | 2026-09-28T08:00:00+08:00 | roundtrip proxy与真实交付、derived handbook与current source分权；3+1+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)；不E整recipe |
| [Multi-agent Scaling Across Disjunctive and Compensatory Tasks](https://arxiv.org/abs/2609.31563v1) | 2026-09-28T08:00:00+08:00 | conditional-iid与item bias、oracle/plurality/平均的极限不同；3+2+2=7 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，Peer/Debate→Blackboard两段 |
| [Towards Mitigating Fabricated Consensus: The Active Provenance Gate for Multi-Agent Debate Synthesis](https://arxiv.org/abs/2609.31422v1) | 2026-09-28T08:00:00+08:00 | 闭世界PF句比例/强制共识与实际发布权分开；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)；不E完整recipe |
| [A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory](https://arxiv.org/abs/2609.30813v1) | 2026-09-28T08:00:00+08:00 | lineage/truth分轴、assertion≠citation、写入/暴露/采纳三事件；3+2+2=7 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)，SelfStore→LateConstruction两段 |
| [Not All Memories Are Equal: Hierarchical Collaborative Memory for Validity-Aware Retrieval in LLM Agents](https://arxiv.org/abs/2609.30289v1) | 2026-09-28T08:00:00+08:00 | 学习current/history两级维护与soft validity重排，不等valid-only gate；2+1+2=5 | 标准完成 | 仅报告：局部维护/soft-rank recipe，不改变授权、有效期与并发通用合同 |
| [Cartograph: Federated Tool Discovery with Operator-Attested Retrieval for AI Agents](https://arxiv.org/abs/2609.30293v1) | 2026-09-28T08:00:00+08:00 | operator签文本与派生embedding分权、粗server召回决定tool shortlist；2+2+2=6 | 深入完成 | 整合：AGENT-MCP [Ch83](../../../../books/part-07-agent/83-mcp.md)，ToolDescription→组合Admission两段 |
| [When Is a Multi-Agent Code Judge Actually Grounded? Two Label-Free Measurements, and a Judge That Declines to Guess](https://arxiv.org/abs/2609.30328v1) | 2026-09-28T08:00:00+08:00 | question相同不认证候选证据/verification output不可区分；3+1+3=7 | 争议 | 暂缓：printed无区分力充分性隔离，有限经验gate与coverage保留 |
| [FuseReg: Regularizing Layer Fusion Mitigates the Reconstruction-Generation Gap in Representation Autoencoders](https://arxiv.org/abs/2609.31620v1) | 2026-09-28T08:00:00+08:00 | 随机nonempty layermean及decoder/DiT两个率与目标分开；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，RepresentationArtifact→Fusion两段 |
| [DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation in Few-Step Video World Models](https://arxiv.org/abs/2609.31349v1) | 2026-09-28T08:00:00+08:00 | teacher状态支持与critic拟合困难的表示/预算分权；3+1+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，reward-target→09536前两段 |
| [The Linear Representation Hypothesis for Vision-Language-Action Models](https://arxiv.org/abs/2609.30996v1) | 2026-09-28T08:00:00+08:00 | propagatedQoI线性probe存在与policy自然参数steering条件分开；2+1+3=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，Actionchunk→Trajectory前两段 |
| [OneWorld: Learning Consistent Physics Across Actions in World Models](https://arxiv.org/abs/2609.30946v1) | 2026-09-28T08:00:00+08:00 | 共同mechanism posterior支持与个体/共享fit/gap分开；3+1+2=6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，common-reset→action-recovery两段 |
| [Action Forcing: Training World Models on Unsupervised Video by Recovering Underlying Egomotion Bases](https://arxiv.org/abs/2609.30595v1) | 2026-09-28T08:00:00+08:00 | 数据PCA零点与noop、teacher输出label与generator真实target分权；3+2+2=7 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，inverse20104→GUI两段 |
| [InternW0-$\Delta$: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data](https://arxiv.org/abs/2609.31394v1) | 2026-09-28T08:00:00+08:00 | 部署change表示与两future监督/4D删除分权，mask才授contextKV复用；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，PFD→ActionRepresentation两段 |
| [Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability](https://arxiv.org/abs/2609.31048v1) | 2026-09-28T08:00:00+08:00 | expert-relative非单调恢复与observedterminalfrontier/采样预算分权；3+2+2=7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，OfflineFailure→EvaluationLadder两段 |
| [Learning to Stop without Learning to Stop: Self-Supervised Confidence Training Improves Reasoning Efficiency](https://arxiv.org/abs/2609.31619v1) | 2026-09-28T08:00:00+08:00 | 自监督概率标签改变效率但不同于可靠停止/校准；2+1+2=5 | 标准完成 | 仅报告：限定训练recipe经验，未确立通用stopping机制；任务质量反退保留 |
| [Compress What You See, Not What You Say: Anchored Context Distillation for Latent-Observation Software Engineering Agents](https://arxiv.org/abs/2609.31430v1) | 2026-09-28T08:00:00+08:00 | 双view独立behavior anchor与表示迁移cache成本；2+2+2=6 | 深入完成 | 整合：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)，POINTS后两段 |
| [Completed Pairs Hide Capped Failures: A ReVerPi Case Study of Selective Context Projection](https://arxiv.org/abs/2609.31381v1) | 2026-09-28T08:00:00+08:00 | 成对观测机会依赖first-arm完成造成zero positivity与有限识别；3+2+2=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，ResponseRate后两段 |
| [Which Influence Are We Estimating? The Role of Counterfactual Specifications in Data Attribution](https://arxiv.org/abs/2609.31214v1) | 2026-09-28T08:00:00+08:00 | 先声明B/P/T估计目标，再用匹配reference检近似误差；3+1+3=7 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)，SAE attribution后两段 |
| [Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning](https://arxiv.org/abs/2609.31121v1) | 2026-09-28T08:00:00+08:00 | 完整可读推理也可操纵monitor framing，paraphrase恢复有损；3+2+2=7 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，CoT score→runtime前两段 |
| [Stealth Apart, Harm Together: Skill Cascading Attacks on Skill-Based Agent Systems](https://arxiv.org/abs/2609.30383v1) | 2026-09-28T08:00:00+08:00 | 多个declared-capability内变换串联消关键signal，commitment审计不同于concat扫描；3+2+2=7 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，Skill描述后两段 |
| [ScopeBench: Do Agents Preserve Engagement Boundaries Under Goal Pressure?](https://arxiv.org/abs/2609.30325v1) | 2026-09-28T08:00:00+08:00 | 无合法路径时机械成功floor与failed-stratum过程judge分权；3+2+2=7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，adaptive profile后两段 |
| [Prompt Injection Detection for Email Agents Through Attack Chain Modeling](https://arxiv.org/abs/2609.30657v1) | 2026-09-28T08:00:00+08:00 | 阶段预测前提/条件分母与实际receipt及policy operatingpoint分权；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，Containment末两段 |
| [In-Context Binding Capacity in Language Models](https://arxiv.org/abs/2609.30634v1) | 2026-09-28T08:00:00+08:00 | own-ceiling归一化容量不能代替absolute task requirement与实测可行集；2+1+3=6 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)，eval slices后两段 |
| [TopoEP 2609.35481v1](https://arxiv.org/abs/2609.35481v1) | 2026-09-29T08:00:00+08:00 | 共享矩阵确定deviceplan与两级topology成本门；2+2+3=7 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，MoonEP→Cobalt，两段实际写后root通过 |
| [WavePP 2609.35263v1](https://arxiv.org/abs/2609.35263v1) | 2026-09-29T08:00:00+08:00 | all-stage endpoint租约与suffix backing先commit、延后materialize；2+2+3=7 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，05219→retention，两段实际写后root通过 |
| [TempoKV 2609.35065v1](https://arxiv.org/abs/2609.35065v1) | 2026-09-29T08:00:00+08:00 | metadata claim与capacity commitment分开，由TTU/TTR共同触发；2+1+3=6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，prefetch23049→CacheScout，两段实际写后root通过 |
| [Nereus 2609.34645v1](https://arxiv.org/abs/2609.34645v1) | 2026-09-29T08:00:00+08:00 | sealed TP/PP replica与跨stage转移DAG，feasibility与payback分权；2+2+3=7 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，22614→token balance，两段实际写后root通过 |
| [EfficientAgent 2609.33762v1](https://arxiv.org/abs/2609.33762v1) | 2026-09-29T08:00:00+08:00 | pool working-set压力下host writefilter与大池恢复写全的反向条件；2+1+3=6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，初Eviction→ContextResidency，实际写后root通过 |
| [AgentReplay 2609.32283v1](https://arxiv.org/abs/2609.32283v1) | 2026-09-29T08:00:00+08:00 | 模型正常forward后、nextstate前固定轨迹，logicalroute/tool等待与runtime自由度分开；2+1+3=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Runtime→AgentOutcome，实际写后root通过 |
| [Introducing dots](https://openai.com/index/introducing-dots/) | 2026-09-29T08:00:00+08:00 | 主动只读发现不继承delegated task执行权限；2+2+2=6 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，Omni→Scheduling，实际写后root通过 |
| [Towards safety cases for frontier AI training](https://openai.com/index/towards-safety-cases-for-frontier-ai-training/) | 2026-09-29T03:00:00+08:00 | 持续case失效暂停covered runs，派生数据/评分恢复与权重rollback分开；3+2+3=8 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，SafetyEval首两段，实际写后root通过 |
| [How we will do better for Australia](https://openai.com/index/how-we-will-do-better-for-australia/) | 2026-09-29T03:00:00+08:00 | 初步受影响方通知不等待最终调查归因，已知/未知分别提交；3+2+2=7 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，n-days→匿名，两段实际写后root通过 |
| [Read-Blindness 2609.35630v1](https://arxiv.org/abs/2609.35630v1) | 2026-09-29T08:00:00+08:00 | 读敏感、写增量与累积的不同权限；2+1+3=6 | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)，两段实际写后root通过 |
| [Entity Copy 2609.35663v1](https://arxiv.org/abs/2609.35663v1) | 2026-09-29T08:00:00+08:00 | context参与准备路由不等于原生context读出提供答案；2+1+3=6 | 深入完成 | 整合：`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md)，两段实际写后root通过 |
| [Rubric IRT 2609.35646v1](https://arxiv.org/abs/2609.35646v1) | 2026-09-29T08:00:00+08:00 | 条件latent测量与冻结测量器的criterion信息预算；2+1+3=6 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，两段实际写后root通过 |
| [SparseOPD 2609.34386v1](https://arxiv.org/abs/2609.34386v1) | 2026-09-29T08:00:00+08:00 | 全correction观察和有符号稀疏head微分分离；2+1+3=6 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)，两段实际写后root通过 |
| [ProbeQuant 2609.33923v1](https://arxiv.org/abs/2609.33923v1) | 2026-09-29T08:00:00+08:00 | isolated uncertainty、input secondmoment与downstream目标不同权限；2+1+3=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，实际两段root写后通过 |
| [Reset Is Not Recovery 2609.33672v1](https://arxiv.org/abs/2609.33672v1) | 2026-09-29T08:00:00+08:00 | reset事件不等于effectivecontext恢复，以pairedclean核残余影响；2+1+3=6 | 深入完成 | 整合：`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md)，实际两段root写后通过 |
| [LLaDA-Guard 2609.33634v1](https://arxiv.org/abs/2609.33634v1) | 2026-09-29T08:00:00+08:00 | labelconditional重构证据域与verdict权限；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际两段root写后通过 |
| [World-Model Post-Training Audit 2609.33335v1](https://arxiv.org/abs/2609.33335v1) | 2026-09-29T08:00:00+08:00 | 正确预测内容与额外优化、selection与coverage归因拆开；3+1+3=7 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，实际两段root写后通过 |
| [Perturbed Documents 2609.33642v1](https://arxiv.org/abs/2609.33642v1) | 2026-09-29T08:00:00+08:00 | 同question/rubric的with/without文档双侧admission门；2+1+3=6 | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)，实际两段root写后通过 |
| [Event-Set Completion Distillation 2609.34738v1](https://arxiv.org/abs/2609.34738v1) | 2026-09-29T08:00:00+08:00 | 实际child completion集合总概率不同于单token配给；2+1+3=6 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)，实际两段root写后通过 |
| [Torch-PIM 2609.34657v1](https://arxiv.org/abs/2609.34657v1) | 2026-09-29T08:00:00+08:00 | Lowering 产生的实际 loop nest 决定放置候选域与 host profile 权限；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49 lowering→dequantization](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过 |
| [SpecStream 2609.33184v1](https://arxiv.org/abs/2609.33184v1) | 2026-09-29T08:00:00+08:00 | 仅迁移已提交历史、多 query 流式验证与 target 优先准入；2+2+3=7 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48 memory-budget→drafter](../../../../books/part-05-inference-system/48-speculative-decoding.md)；实际正文与非作者写后通过 |
| [Planarian 2609.35366v1](https://arxiv.org/abs/2609.35366v1) | 2026-09-29T08:00:00+08:00 | 预先可补偿操作与 tool-boundary 联合 capture，不自授远端 fork；2+2+3=7 | 深入完成 | 整合：`AGENT-WORKFLOW` [Ch81 AgentRewind→Waypoint](../../../../books/part-07-agent/81-workflow.md)；实际正文与非作者写后通过 |
| [Dynamic Flow, Static Graph 2609.34727v1](https://arxiv.org/abs/2609.34727v1) | 2026-09-29T08:00:00+08:00 | 固定图容纳选择性 KV 重算，并按实测调用成本规划 chunks；2+1+3=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49 静态图→基础优化](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过 |
| [SPIMOE: Exploiting Hybrid Sparsity for Reasoning MoE Inference on Heterogeneous PIM Architectures 2609.34612v1](https://arxiv.org/abs/2609.34612v1) | 2026-09-29T08:00:00+08:00 | 联合稀疏/PIM 的质量与资源耦合验证，不把 recipe 升为通用机制；2+1+3=6 | 标准完成 | 仅报告：局部实现/评价不改变现有长期机制，具体理由见下节 |
| [PolyCIM: Improving Data Reuse in Digital CIM Accelerators with Polyhedral-Based Compilation 2609.34351v1](https://arxiv.org/abs/2609.34351v1) | 2026-09-29T08:00:00+08:00 | 非轴向 reuse 先仿射 realignment，再映射有限 CIM/layout；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49 Nautilus→Persistent Executor](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过 |
| [Tool Waiting and Re-arrival in Compile-Time-Static LLM Serving: Cost Mechanisms and Configuration Selection 2609.34663v1](https://arxiv.org/abs/2609.34663v1) | 2026-09-29T08:00:00+08:00 | 静态 bucket 与内生 tool re-arrival 联合决定 padding/驻留成本；2+1+3=6 | 深入完成 | 整合：`INFER-CONTINUOUS-BATCHING` [Ch46 trade-off→工程判断](../../../../books/part-05-inference-system/46-continuous-batching.md)；实际正文与非作者写后通过 |
| [Beyond Energy: When Sustainability Dimensions Reshape LLM Serving Decisions 2609.35569v1](https://arxiv.org/abs/2609.35569v1) | 2026-09-29T08:00:00+08:00 | 固定部署运营排序与跨部署 embodied crossover 分账；2+1+3=6 | 深入完成 | 整合：`PLATFORM-COST` [Ch70 Unit Economics 生命周期→需求反弹](../../../../books/part-06-ai-infrastructure/70-cost.md)；实际正文与非作者写后通过 |
| [Beneath the Tokens: A Performance Engineering Study of Multi-Token Prediction in GPU-Accelerated LLM Inference 2609.35188v1](https://arxiv.org/abs/2609.35188v1) | 2026-09-29T08:00:00+08:00 | 每有效 token 的调用摊销与单 kernel 时间不是同一指标；1+1+3=5 | 标准完成 | 仅报告：局部实现/评价不改变现有长期机制，具体理由见下节 |
| [DPS: Dual-Mode Precision LLM Serving with Semi-Unified Memory 2609.34380v1](https://arxiv.org/abs/2609.34380v1) | 2026-09-29T08:00:00+08:00 | persistent weights/residual/KV 非对称共享与 forward 模式提交；2+2+3=7 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54 双模式 Weight 与 KV](../../../../books/part-05-inference-system/54-gpu-memory.md)；实际正文与非作者写后通过 |
| [Where Activation Sparsity and KV-Cache Sparsity Cross in LLM Decoding 2609.33889v1](https://arxiv.org/abs/2609.33889v1) | 2026-09-29T08:00:00+08:00 | weight-read/KV-read 的 byte 交点还须质量和 kernel 成本校准；2+1+3=6 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54 少读 Weight 与少读 KV 的交点](../../../../books/part-05-inference-system/54-gpu-memory.md)；实际正文与非作者写后通过 |
| [Just Let Linear States Forget the Distant Past: Prefix Caching via SuffixReplay for Hybrid LLMs 2609.33477v1](https://arxiv.org/abs/2609.33477v1) | 2026-09-29T08:00:00+08:00 | 按 linear group 保存输入锚点，近似 replay 与发布边界分开；2+2+3=7 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45 Group 输入锚点→Video cache](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；实际正文与非作者写后通过 |
| [BEHAVE: Functional Behavior Modeling Enables Self-Improving Agents for Hardware Design and Verification 2609.34785v1](https://arxiv.org/abs/2609.34785v1) | 2026-09-29T08:00:00+08:00 | 允许 transaction timing 差异但双产物都须独立 hidden gold；2+1+3=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 Transaction oracle→Dense Process](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；实际正文与非作者写后通过 |
| [Argus: Agentic, Reference-Calibrated, Tree-Guided, System-Software-Level Bottleneck Localization 2609.35508v1](https://arxiv.org/abs/2609.35508v1) | 2026-09-29T08:00:00+08:00 | 同 workload reference 与 tree/probe 定位的受限实现验证；1+1+3=5 | 标准完成 | 仅报告：局部实现/评价不改变现有长期机制，具体理由见下节 |
| [Hardware-Aware Features for CUTLASS Kernel Selection 2609.35587v1](https://arxiv.org/abs/2609.35587v1) | 2026-09-29T08:00:00+08:00 | candidate-induced 硬件代理排序、shape-group 留出与执行 coverage；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49 硬件行为代理→Tensor Core层级](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过 |
| [Semantic Prefix Oracles 2609.35425v1](https://arxiv.org/abs/2609.35425v1) | 2026-09-29T08:00:00+08:00 | 语义 prefix 安全剪枝与可完成性是两份合同；2+2+3=7 | 深入完成 | 整合：`INFER-SGLANG` [Ch51 Structured Generation→Adapter readiness](../../../../books/part-05-inference-system/51-sglang.md)；实际正文与非作者写后通过 |
| [Rubric-Calibrated Preferences 2609.35739v1](https://arxiv.org/abs/2609.35739v1) | 2026-09-29T08:00:00+08:00 | query内BT排序与跨query单位/原点分开校准；2+1+3=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 Judge Ranking→Route/defer](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；实际正文与非作者写后通过 |
| [SpeakGR 2609.35430v1](https://arxiv.org/abs/2609.35430v1) | 2026-09-29T08:00:00+08:00 | 扩SID词表后分开检索正确与原文本条件分布保护；2+1+3=6 | 深入完成 | 整合：`TRAIN-SFT` [Ch29 Occupancy→共享Trace](../../../../books/part-04-training-system/29-sft.md)；实际正文与非作者写后通过 |
| [TRACE 2609.33517v1](https://arxiv.org/abs/2609.33517v1) | 2026-09-29T08:00:00+08:00 | return epoch 下逐项有效不等整组关键义务覆盖；2+2+3=7 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77 Memory Read Recency→累计披露](../../../../books/part-07-agent/77-memory.md)；实际正文与非作者写后通过 |
| [Revision, Not Restart: Revisable Visual Plans for Closed-Loop World–Action Models 2609.35439v1](https://arxiv.org/abs/2609.35439v1) | 2026-09-29T08:00:00+08:00 | 保存visual solver路径，用真实feedback修订未执行计划再解动作；2+2+3=7 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 World-action→Future-to-Action](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过 |
| [MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining 2609.35652v1](https://arxiv.org/abs/2609.35652v1) | 2026-09-29T08:00:00+08:00 | common endpoint loss下clean-head/velocity-head改变noise burden；2+1+3=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 固定点decoder→endpoint initialization](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过 |
| [Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching 2609.35469v1](https://arxiv.org/abs/2609.35469v1) | 2026-09-29T08:00:00+08:00 | flow阶段绑定code可见性形成ordered increments而非物理因果；2+1+3=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 离散codec→粗planner/refiner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过 |
| [Signal or Noise? Modality Contribution and Cooperation in Multimodal GraphRAG 2609.35304v1](https://arxiv.org/abs/2609.35304v1) | 2026-09-29T08:00:00+08:00 | supporting-edge subset admission与明确baseline的模态交互诊断；2+1+3=6 | 深入完成 | 整合：`AGENT-RAG` [Ch76 多模态admission→Escalation](../../../../books/part-07-agent/76-rag.md)；实际正文与非作者写后通过 |
| [MASTraceBench: Diagnosing Collaboration Gains through Proposal Trajectories in LLM-Based Multi-Agent Systems 2609.34496v1](https://arxiv.org/abs/2609.34496v1) | 2026-09-29T08:00:00+08:00 | initial→final proposal→aggregate分三层质量账；2+1+3=6 | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82 Evaluation成本表→条件分支](../../../../books/part-07-agent/82-multi-agent.md)；实际正文与非作者写后通过 |
| [Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention — 2609.35794v1](https://arxiv.org/html/2609.35794v1) | 2026-09-30T08:00:00+08:00 | 检索缺证据与存在证据却受干扰需要不同补救；生成前gate提供条件性路由。 2+2+2=6 | 深入完成 | 整合：`AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [When Successful Memories Mislead Embodied Agents: Memory Adaption For Task-Conditioned Execution — 2609.35808v1](https://arxiv.org/html/2609.35808v1) | 2026-09-30T08:00:00+08:00 | 成功轨迹的旧动作schema仍能误导；将接口兼容收益与压缩收益分开。 3+1+2=6 | 深入完成 | 整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [How to Run Statistics over LLM Judges and Trust the Results: Calibrated Inference for Small-Sample AI Evaluation with evalstats — 2609.35815v1](https://arxiv.org/html/2609.35815v1) | 2026-09-30T08:00:00+08:00 | 高judge agreement不保证区间/检验校准；人工配对抽样和估计不确定性改变发布判断。 3+2+3=8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Less Uniform Discrete Diffusion is More Powerful and Scalable — 2609.35817v1](https://arxiv.org/html/2609.35817v1) | 2026-09-30T08:00:00+08:00 | uniform reverse目标的平滑与corruption身份耦合；清洁目标和per-token time改变训练解释。 2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [When Should LLMs Trust Their Own Revisions? A Risk-Aware Study of Intrinsic Self-Correction — 2609.35832v1](https://arxiv.org/pdf/2609.35832v1) | 2026-09-30T08:00:00+08:00 | 修正错误与引入新错必须分账，revision前gate和后验acceptance预算不同。 2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-REFLECTION` / [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [The Detectability Gap: Hidden Heterogeneity in Hallucination Detection Across Language Models — 2609.35860v1](https://arxiv.org/html/2609.35860v1) | 2026-09-30T08:00:00+08:00 | 用同一统计量定义难组再测detectability会自造gap；冻结partition后须换signal检验。 3+1+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Mnemon: Raw Records, Fast Judgments, Slow Thoughts — 2609.36059v1](https://arxiv.org/html/2609.36059v1) | 2026-09-30T08:00:00+08:00 | raw authority已覆盖；新增判定器替换条件及waves、总判断、lifecycle cost的不同预算。 2+2+3=7 | 深入完成 | 整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Targeting Pivotal Decisions for Credit Assignment in Agentic Reinforcement Learning — 2609.36178v1](https://arxiv.org/html/2609.36178v1) | 2026-09-30T08:00:00+08:00 | judge选址不等数值credit；恢复两端状态，用固定current policy续跑估局部贡献。 2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Learning from Teacher Continuations at Student States — 2609.36246v1](https://arxiv.org/html/2609.36246v1) | 2026-09-30T08:00:00+08:00 | teacher文本continuation免logit接口，但其后续状态及CE监督边界不同于逐token纠错。 2+2+2=6 | 深入完成 | 整合：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Reliable Parallel Decoding in Masked Diffusion Language Models — 2609.36452v1](https://arxiv.org/html/2609.36452v1) | 2026-09-30T08:00:00+08:00 | 同pass高confidence不足以joint commit；final-layer稳定性与未解决上游熵约束承诺集合。 2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [ParaAnya: Accelerating Parallel Diffusion Sampling with Plug-and-Play Output Caching — 2609.36522v1](https://arxiv.org/html/2609.36522v1) | 2026-09-30T08:00:00+08:00 | 并行迭代反复访问同timestep可缓存输出，但命中检查及通信可能吃掉NFE收益。 2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [SEED: Self-Speculative Decoding via Implicit Encoder-Decoder — 2609.36590v1](https://arxiv.org/html/2609.36590v1) | 2026-09-30T08:00:00+08:00 | verifier刷新deep KV，再由薄末层读raw embedding起草，形成自推测的另一条件分支。 2+2+2=6 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Replay the Curvature: Accurate and Scalable NVFP4 Quantization for Large Language Model Inference — 2609.36654v1](https://arxiv.org/html/2609.36654v1) | 2026-09-30T08:00:00+08:00 | 未来列可补偿时当前误差应条件化；scale候选需私有回放真实顺序量化轨迹。 2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [ATTUNER: Recomputation-Free KV Cache Reuse via Query-Side Adaptation — 2609.36722v1](https://arxiv.org/pdf/2609.36722v1) | 2026-09-30T08:00:00+08:00 | 独立artifact KV丢跨artifact条件；冻结cache producer并训练query consumer，不将位置修复当充分条件。 2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Reshaping Rollout Workloads for Asynchronous RL Post-Training on Heterogeneous Accelerators — 2609.36899v1](https://arxiv.org/html/2609.36899v1) | 2026-09-30T08:00:00+08:00 | 暂停长轨迹可改善resident组成；depart/destination分离改变异构rollout调度。 2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation — 2609.36903v1](https://arxiv.org/html/2609.36903v1) | 2026-09-30T08:00:00+08:00 | 长多方双语评价及固定架构data对照限制由短dyadic效果外推的能力判断。 2+2+2=6 | 标准完成 | 仅报告：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；新增证据不改长期机制，旧机制不重评 |
| [Dating the Model: Hidden Dates in System Prompts Affect LLM Evaluation — 2609.36931v1](https://arxiv.org/html/2609.36931v1) | 2026-09-30T08:00:00+08:00 | system date是确定性输入干预，隐藏默认值可改变比较而非随机采样噪声。 2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Efficient Agentic LLM Serving over SSD-based Sparse KV Storage — 2609.36938v1](https://arxiv.org/html/2609.36938v1) | 2026-09-30T08:00:00+08:00 | 预测层间selector可预取，但target native selector及缺失补读仍决定Attention可见状态。 2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ER-JEPA: Experience Replay Improves Joint-Embedding Predictive Learning in Language Models — 2609.36952v1](https://arxiv.org/html/2609.36952v1) | 2026-09-30T08:00:00+08:00 | 匹配compute/token/current-batch对照仍显示历史内容作用；初筛关闭理由因此被独立反证。 2+1+2=5 | 标准完成 | 已有覆盖：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Purlin: Separating Orchestration from the Datapath of Collectives — 2609.36954v1](https://arxiv.org/html/2609.36954v1) | 2026-09-30T08:00:00+08:00 | layout/copy-reduce语义和coordination可复用，但hardware datapath及数值policy不等价。 2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Cobalt: Leveraging Expert Co-activation for Efficient Distributed MoE Training — 2609.36959v1](https://arxiv.org/html/2609.36959v1) | 2026-09-30T08:00:00+08:00 | 单token多expert的destination-node union不同于各expert负载和，改变布局目标。 2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Learning from Think-Mode Advantage via On-Policy Distillation — 2609.37044v1](https://arxiv.org/html/2609.37044v1) | 2026-09-30T08:00:00+08:00 | teacher优势与trace对兄弟response的可转移性分离，用group路由权重而非一律强模仿。 2+1+2=5 | 深入完成 | 整合：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [vSkipper: Translating Dynamic Layer Skipping into LLM Serving Gains — 2609.37062v1](https://arxiv.org/html/2609.37062v1) | 2026-09-30T08:00:00+08:00 | 内部skip仍需本层KV投影和route元数据；policy省层不自动成为引擎收益。 3+2+2=7 | 深入完成 | 整合：`INFER-SGLANG` / [Ch51](../../../../books/part-05-inference-system/51-sglang.md) |
| [ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents — 2609.37196v1](https://arxiv.org/html/2609.37196v1) | 2026-09-30T08:00:00+08:00 | capability shape grant与当前具体值provenance分离；缓存授权不能缓存证据真值。 3+2+2=7 | 深入完成 | 整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Compiling Learning Problems into Adaptation Programs for Language Models — 2609.37371v1](https://arxiv.org/html/2609.37371v1) | 2026-09-30T08:00:00+08:00 | episode geometry可摊销选择adaptation program；未知family仍需default与适配成本预算。 2+1+2=5 | 深入完成 | 整合：`TRAIN-LORA` / [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Your Benchmark Is Not Saturated: Reviving Multiple-Choice Evaluation with Answer Pooling — 2609.37494v1](https://arxiv.org/html/2609.37494v1) | 2026-09-30T08:00:00+08:00 | 共享答案池把单题分类变耦合assignment；chance和干扰控制变化须与原任务分开。 2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [DScale: Scaling Block-Diffusion Speculative Decoding with Adaptive Verification — 2609.37532v1](https://arxiv.org/html/2609.37532v1) | 2026-09-30T08:00:00+08:00 | 保完整草稿而限ragged verification共享预算；图固定地址不意味着commit边界固定。 2+2+2=6 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models — 2609.37533v1](https://arxiv.org/html/2609.37533v1) | 2026-09-30T08:00:00+08:00 | 离散router latent可让parallel reverse采样相关；clean/noisy router匹配决定训练推理接口。 2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Correct, Don't Delete: Mitigating Emergent Misalignment with Corrective Supervision — 2609.37624v1](https://arxiv.org/html/2609.37624v1) | 2026-09-30T08:00:00+08:00 | 删除坏监督移除该输入的训练机会，纠正则尝试供正面目标；两种intervention不可混同。 2+1+2=5 | 深入完成 | 整合：`TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [SPLASH: Switching Parallel Layouts of Attention with Seamless Handoff for LLM Serving — 2609.37626v1](https://arxiv.org/html/2609.37626v1) | 2026-09-30T08:00:00+08:00 | projection/KV ownership解耦后，live-layout切换需稳态+暂态容量及共同handoff。 3+2+2=7 | 深入完成 | 整合：`INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Honeycomb: Constant-Size Scene Memory Representation for Video World Models — 2609.37690v1](https://arxiv.org/html/2609.37690v1) | 2026-09-30T08:00:00+08:00 | 固定planes在expanding bounds下warp/coarsen；存储恒定不等信息精度恒定。 2+2+3=7 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Delta-Matching: Closing the Final Gap of Native 8-bit Training for LLMs — 2609.37852v1](https://arxiv.org/html/2609.37852v1) | 2026-09-30T08:00:00+08:00 | 量化dP使saved delta失配，重算匹配contraction恢复softmax梯度零行和。 3+2+3=8 | 深入完成 | 整合：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Retrieval Capacity of Self-Attention Under Competition — 2609.37879v1](https://arxiv.org/html/2609.37879v1) | 2026-09-30T08:00:00+08:00 | 权重不等独立知识贡献；V方向及delete/renormalize不同干预改变诊断解释。 2+1+3=6 | 深入完成 | 整合：`MODEL-SELF-ATTENTION` / [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [It's All Training: A Fully Synthetic Single-Stage Recipe for LLMs — 2609.37891v1](https://arxiv.org/html/2609.37891v1) | 2026-09-30T08:00:00+08:00 | 旧synthetic pipeline不重算；本窗同600M/data trace ablation和seed外反证限制效率归因。 2+1+2=5 | 标准完成 | 仅报告：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；新增证据不改长期机制，旧机制不重评 |
| [Scaling Zero-Order Pretraining through Model Sharding — 2609.37899v1](https://arxiv.org/html/2609.37899v1) | 2026-09-30T08:00:00+08:00 | 可分目标移除跨expert SPSA噪声，以表征耦合换独立更新，非通用通信分片。 2+2+3=7 | 深入完成 | 整合：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Learning What to Remember: Long-horizon Counterfactual Memory Optimization — 2609.37930v1](https://arxiv.org/html/2609.37930v1) | 2026-09-30T08:00:00+08:00 | rewrite总效用含继承收益；相邻状态对同future targets的增量才接近本次write credit。 2+2+3=7 | 深入完成 | 整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [How Local Mixing Encodes Relative Position in Global NoPE Attention — 2609.38109v1](https://arxiv.org/html/2609.38109v1) | 2026-09-30T08:00:00+08:00 | 局部mixing及Q/K对齐能读implicit recency，修正必须显式PE的绝对句。 2+1+3=6 | 深入完成 | 整合：`MODEL-POSITION-ENCODING` / [Ch13](../../../../books/part-02-model/13-position-encoding.md) |
| [WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms — 2609.38121v1](https://arxiv.org/html/2609.38121v1) | 2026-09-30T08:00:00+08:00 | K/query与V/output需要不同consumer metric，post-RoPE变换折叠及在线代价不同。 2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [HelixWorld: A Real-time Interactive Audio-Visual World Model — 2609.38123v1](https://arxiv.org/html/2609.38123v1) | 2026-09-30T08:00:00+08:00 | camera/world state联合条件视听，在student自身轨迹纠偏streaming而非只换音轨。 2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation — 2609.38142v1](https://arxiv.org/html/2609.38142v1) | 2026-09-30T08:00:00+08:00 | advisor对recorded response的预测敏感性可选择监督，但不是executor反事实因果。 2+2+3=7 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Rho: A Foundation for Efficiently Adaptable VLA Models — 2609.38164v1](https://arxiv.org/html/2609.38164v1) | 2026-09-30T08:00:00+08:00 | embodiment midtraining→任务更新→冻结action generator的latent repair分开适配authority。 2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization — 2609.38169v1](https://arxiv.org/html/2609.38169v1) | 2026-09-30T08:00:00+08:00 | state误差随transition传播；readout时序与temporal/spatial敏感度影响量化生命周期。 2+2+3=7 | 深入完成 | 整合：`INFER-GPU-MEMORY` / [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Disrupting a coordinated model distillation campaign](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/) | 2026-09-30T18:30:00+08:00 | 密文隐藏不等消费授权，跨身份/model-family重放需与release gate分层。3+2+3=8 | 深入完成 | 整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际POST通过 |
| [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) | 2026-10-01T04:00:00+08:00 | 风险监测与训练反馈权限分账，不能优化低monitor score代替安全。3+2+2=7 | 深入完成 | 整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，仅反馈分工增量，实际POST通过 |
| [TomasuLLM](https://arxiv.org/html/2609.38201v1) | 2026-10-01T08:00:00+08:00 | 真实工具推测执行需要区分operand就绪、当前提交与预测观测的后继有效性。3+2+2=7 | 深入完成 | 整合：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)，COW搜索与Live Fork之间，实际POST通过 |
| [The System Prompt Illusion](https://arxiv.org/html/2609.38205v1) | 2026-10-01T08:00:00+08:00 | probe可读、表征几何相似、局部patch因果证据不能互换；设计反证加深。2+1+2=5 | 深入完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，仅readout/局部因果分账 |
| [Conformal Factuality Control for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/html/2609.38222v1) | 2026-10-01T08:00:00+08:00 | 全回答支持率含空输出，不等于非空回答的条件支持率；verifier标签不是语义真值。2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，仅分母及oracle权限边界 |
| [SpecScale](https://arxiv.org/html/2609.39334v1) | 2026-10-01T08:00:00+08:00 | 逻辑候选数不等实际forward数，独立draw与PRM排队分别控制；长期机制缺口加深。2+2+2=6 | 深入完成 | 整合：`INFER-CONTINUOUS-BATCHING` / [Ch46](../../../../books/part-05-inference-system/46-continuous-batching.md)，iteration工作单元后，实际POST通过 |
| [Preserving Provenance in Shared KV Caches](https://arxiv.org/html/2609.38706v1) | 2026-10-01T08:00:00+08:00 | local key正确不保证connector保留计算等价和sharing权限，跨worker/lookup-store身份须一致。3+2+2=7 | 深入完成 | 整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，Prefix reuse，实际POST通过 |
| [Vosti](https://arxiv.org/html/2609.38981v1) | 2026-10-01T08:00:00+08:00 | 单kernel确定性不足wholeengine；canonical KV与relational kernel合同须组合。3+2+2=7 | 深入完成 | 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，数值验收，实际POST通过 |
| [KVTether](https://arxiv.org/html/2609.39819v1) | 2026-10-01T08:00:00+08:00 | message变异须传播prefix版本失效，跨context引用和waiting age分账；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，Agent语义区域后，实际POST通过 |
| [Characterizing High Bandwidth Flash for LLM Serving](https://arxiv.org/html/2609.39131v1) | 2026-10-01T08:00:00+08:00 | flash层容量不免费，write endurance、缓存锁定与admission压力联合规划；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`INFER-GPU-MEMORY` / [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)，扩展层级，实际POST通过 |
| [The Planning Limits of Latent World Models](https://arxiv.org/html/2609.39235v1) | 2026-10-01T08:00:00+08:00 | 精确transition仍会因目标评分短视失败，prediction质量与planning range不同。3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，Imagined rollout，实际POST通过 |
| [U-Fuzz](https://arxiv.org/html/2609.38275v1) | 2026-10-01T08:00:00+08:00 | 正确memory不保证正确消费，query/state变异、探索与判错需分权；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)，Recall/Use之后，实际POST通过 |
| [StateFork](https://arxiv.org/html/2609.38648v1) | 2026-10-01T08:00:00+08:00 | 文件恢复不等session后续观察等价，逻辑分支与checkpoint物理化分权；恢复合同深入。2+2+2=6 | 深入完成 | 整合：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)，联合恢复之后，实际POST通过 |
| [Blackout and Freeze](https://arxiv.org/html/2609.39145v1) | 2026-10-01T08:00:00+08:00 | 缺帧与陈旧帧不同，恢复任务成功不认证物理风险；安全设计反证。3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，Safety envelope，实际POST通过 |
| [Two-step Flow VLA](https://arxiv.org/html/2609.39822v1) | 2026-10-01T08:00:00+08:00 | 近action区间可另学平均velocity，NFE减少与控制质量必须分账；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，solver分支，实际POST通过 |
| [Prefix-invariant Fast Matrix Multiplication](https://arxiv.org/html/2609.39816v1) | 2026-10-01T08:00:00+08:00 | batch形状确定性不保证早先token不受未来影响，低精度累加需条件化prefix不变性。3+2+2=7 | 深入完成 | 整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，数值合同，实际POST通过 |
| [HAPMoE](https://arxiv.org/html/2609.39350v1) | 2026-10-01T08:00:00+08:00 | 异构stage不能事后固定同构EP/TPE，需要device-aware联合容量/通信/分区计划；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`TRAIN-PIPELINE-PARALLEL` / [Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md)，Stage Balance，实际POST通过 |
| [ThunderEP](https://arxiv.org/html/2609.40093v1) | 2026-10-01T08:00:00+08:00 | host-only通信的relay traffic与依赖链收益不同，prefill DMA不能直接移植captured decode；长期缺口加深。2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，多路径分支，实际POST通过 |
| [Gradient-Conflict Audit](https://arxiv.org/html/2609.38465v1) | 2026-10-01T08:00:00+08:00 | 降冲突proxy不等改善任务，诊断有效性须区分预测/同期、干预/结果与population；设计反证加深。3+1+2=6 | 深入完成 | 整合：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，多模态方差冲突后，实际POST通过 |
| [CW-OPD](https://arxiv.org/html/2609.38777v1) | 2026-10-01T08:00:00+08:00 | 单world端点匹配不约束跨视觉响应，共同logit变化消项仅限transition；长期缺口加深。2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)，teacher对照分支，实际POST通过 |
| [S-OPD](https://arxiv.org/html/2609.39120v1) | 2026-10-01T08:00:00+08:00 | teacher只选学生视觉contrast位置，mask敏感与noise稳定是不同辅助目标；长期缺口加深。2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)，视觉选择分支，实际POST通过 |
| [MiniMax Code v0.6.0](https://github.com/MiniMax-AI/minimax-code/releases/tag/v0.6.0) | 2026-10-01T21:56:17+08:00 | BYOK宽重试需排除安全拒绝，拒绝说明不得污染状态码分类；1 + 1 + 2 = 4 | 深入完成 | 整合：`AGENT-PLATFORM`，[Ch84状态机](../../../../books/part-07-agent/84-agent-platform.md#agent-runtime-state-machine) |
| [OpenAgentCore v0.0.3（含v0.0.4同窗演进）](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.3) | 2026-10-01T16:30:10+08:00 | CI工具/秘密边界，后续部署/TLS/管理密钥兼容事件分别复用见§4；1+1+1=3 | 深入完成 | 仅报告：两个Daily均只采用精确版本事实，不授生产安全 |
| [DeepSeek Harness v0.2.1-alpha.1](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.2.1-alpha.1) | 2026-10-03T14:42:19+08:00 | 插件子路径元数据、诊断导出与扩展入口的破坏性兼容契约；1 + 1 + 1 = 3 | 深入完成 | 仅报告：alpha 版本迁移事实，不建立长期兼容机制结论 |
| [MiMo-Code：Provider Refresh Without Instance Disposal，PR #2603](https://github.com/XiaomiMiMo/MiMo-Code/pull/2603) | 2026-10-03T19:11:41+08:00 | 保留 Instance 的 provider refresh：idle admission、先准备后统一发布、忙时不排队、closing-owner sampling 拒绝；1 + 1 + 2 = 4 | 深入完成 | 仅报告：局部 SDK/运行时契约及可复用约束的实现例证，不扩大为通用热更新保证 |
| [PyTorch v2.14.1](https://github.com/pytorch/pytorch/releases/tag/v2.14.1) | 2026-10-01T03:14:48+08:00 | 源语义/scale合法不保证compiler/library忠实执行；3+2+2=7 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md#lowering-与低精度执行都需要可回归的-commit-boundary) |
| [SGLang v0.5.21](https://github.com/sgl-project/sglang/releases/tag/v0.5.21) | 2026-10-02T09:09:04+08:00 | PD远端写寿命/多rankACK及refit表示finalize改变实际默认合同；3+2+2=7 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md#execution-plan-可以修订但只能在安全边界-commit)；PD顺序已有INFER-PD-DISAGGREGATION [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md#handoff-状态机)覆盖 |
| [FlashInfer v0.7.1rc1/.rc2与v0.7.0.post1](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.1rc1) | 2026-10-01T00:43:06+08:00 | 零行fast-math非finite、routed-only replay布局与prepared graph元数据寿命纠错；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md#从逐-kernel-launch-到-persistent-executor) |
| [Transformers v5.18.0](https://github.com/huggingface/transformers/releases/tag/v5.18.0) | 2026-10-01T00:46:27+08:00 | 两侧shape测试不认证缓存等价，配对生成回归发现position/mask角色错误；2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md#为什么缓存-kv-而不是-query)前两段 |
| [Ray v2.59.0](https://github.com/ray-project/ray/releases/tag/ray-2.59.0) | 2026-10-02T15:04:37+08:00 | 本地auth入口差异、取消lease时序与429/503可选合同变化；3+2+2=7 | 深入完成 | 仅报告：具名版本默认/保护与局部取消，不形成新权限理论或全局安全保证 |
| [Olmo-core v3.0.0](https://github.com/allenai/Olmo-core/releases/tag/v3.0.0) | 2026-10-01T23:17:49+08:00 | 未EOS边界推定会丢后续文档，同size sidecar更正须失效packing cache；3+1+2=6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md#tokenizer切分与-packing-的边界) |
| [METR per-action monitor](https://metr.org/notes/2026-09-27-implementing-a-basic-blocking-action-monitor/) | 2026-09-27T15:00:00+08:00 ～ 2026-09-28T15:00:00+08:00 | 动作检测/阻断不能代替真实人审身份，自动approve与漏监反例修正保障范围；3+2+2=7 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md#approval-summary-必须由待执行-effect-反向渲染) |
| [GLM-5.3 cyber assessment](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities) | 2026-09-29T23:46:00+08:00 | 可执行能力与可达攻击权限、模拟engagement分臂修正安全比较；3+2+2=7 | 深入完成 | 仅报告：当前模型/有限威胁与测量事实，不把version结果提升为普遍攻击率 |

## 4. 证据与知识整合

每项Daily的精确版本、必要原证据位置、对照、反证与实际Books写后结果保持原有效审阅；本周只复用，不用下列短句冒充重新读全文。未变化的复核结论按研究合同§7复用，当前新增差额仍单独核写后。各候选原始链接如下。

### [New LoRA Skills Should Read but Never Write](https://arxiv.org/abs/2609.31600v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：Gauge坐标与单向block权限区分旧参数项与总函数。整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)，Fed gauge后两段；仅有条件composition。不把该局部命题提升为完整recipe/生产保证。

### [Evaluating the accuracy of KV cache reuse techniques](https://arxiv.org/abs/2609.31415v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：Baseline条件评价与warmup角色反事实修正reuse验收。整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，PatchKV后两段。不把该局部命题提升为完整recipe/生产保证。

### [Generalization behavior of OPTQ and the role of regularization](https://arxiv.org/abs/2609.31560v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：校准→population泛化的独立概率/正则条件。整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，weighted-cover后两段。不把该局部命题提升为完整recipe/生产保证。

### [Beyond Mean Attention: Diversity-Aware, Layer-Wise Scoring for KV Cache Eviction](https://arxiv.org/abs/2609.30738v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：构建集合的冗余排序与depth profile非普适收益。整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，TwinKV后两段。不把该局部命题提升为完整recipe/生产保证。

### [EAServe: Encode-Aware Disaggregated Serving for Multimodal Large Language Models](https://arxiv.org/abs/2609.31551v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：Encode批等待/SM共驻与分流联动，但吞吐目标不同于SLO goodput。整合：INFER-PD-DISAGGREGATION [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)，goodput→KV transfer两段。不把该局部命题提升为完整recipe/生产保证。

### [ActKV: Efficient LLM Agents through Action-Guided KV Cache Management](https://arxiv.org/abs/2609.31395v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：Action访问历史与round末预算/无冲突原位压缩。整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，LoopGuard后两段。不把该局部命题提升为完整recipe/生产保证。

### [CacheReforge: Bounded Recovery for Stale KV Caches under Evolving Adapters](https://arxiv.org/abs/2609.30884v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：逐层参数anchor/位移及可执行restart与tail证书分权。整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，21362 seam后两段。不把该局部命题提升为完整recipe/生产保证。

### [Quantizing Looped Transformers: Feedback Exposure and Calibration Blindness](https://arxiv.org/abs/2609.30820v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：Loop-entry反馈位置与跨step Hessian覆盖是不同精度轴。整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，OPTQ→PTQ两段。不把该局部命题提升为完整recipe/生产保证。

### [Low-Bit Recurrent States in Hybrid Language Models](https://arxiv.org/abs/2609.30950v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：误差存活/readout方向与range共同限制state位宽代理。整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，Fractional末两段。不把该局部命题提升为完整recipe/生产保证。

### [Softmax Reparameterization for Output-Head Quantization](https://arxiv.org/abs/2609.31291v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：公共row shift等价与量化/非线性修正的权限不同。整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，Greedy→ExactTopK两段。不把该局部命题提升为完整recipe/生产保证。

### [Deterministic Regime Switching and Feasibility Inversion in Dynamic Tensor Rematerialization](https://arxiv.org/abs/2609.31250v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：重复eviction与pinned frontier使在线budget可非单调。整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，activation保存/重算末两段。不把该局部命题提升为完整recipe/生产保证。

### [Block Sparse Attention with Log-Linear Complexity](https://arxiv.org/abs/2609.31093v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：分层候选routing降低selector扫描但ancestor漏选不由leaf精确修复。整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)，MiniMax sparse→selector forward两段。不把该局部命题提升为完整recipe/生产保证。

### [From Shortcut Learning to Discrete Neural Insertion Sort](https://arxiv.org/abs/2609.31114v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：最终正确与逐步算法执行不同，discrete control仍需全局终止监督。整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，25800→训练标准两段。不把该局部命题提升为完整recipe/生产保证。

### [Common-Mode Collapse and Recovery in Direct Feedback Alignment](https://arxiv.org/abs/2609.31589v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：共享mean teaching低秩驱动与readout/optimizer的非单调collapse。整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，01563→depth parameterization两段。不把该局部命题提升为完整recipe/生产保证。

### [Weight Pair Encoding: Inducing a Smaller Grammar in Neural Network Weights](https://arxiv.org/abs/2609.31564v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：训练code-domain重复语法是独立压缩轴，不等kernel或位宽收益。整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，PTQ/QAT定义→W4A16两段。不把该局部命题提升为完整recipe/生产保证。

### [Decodable In-Context State and Model Output Across Training](https://arxiv.org/abs/2609.31401v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：logits与argmax分权否证probe对错差直接等于信息丢失。整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，独立reader→encoder移植两段。不把该局部命题提升为完整recipe/生产保证。

### [The Residual Stream's Effective Depth](https://arxiv.org/abs/2609.31098v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：累积state几何需matched参照，不是无用层或pruning许可。整合：MODEL-TRANSFORMER-LAYER [Ch17](../../../../books/part-02-model/17-transformer-layer.md)，分别检验→逐层替换两段。不把该局部命题提升为完整recipe/生产保证。

### [Convergence guarantees for Muon: New parameter regimes and generalizations](https://arxiv.org/abs/2609.30546v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：有限NS、ideal sign与soft-sign代理的轨迹保证权限分开。整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，18999→多Optimizer两段。不把该局部命题提升为完整recipe/生产保证。

### [MoSAR: Mixture of Semantic Attention Regimes for Learning Adaptive and Approximable Attention Geometries](https://arxiv.org/abs/2609.31261v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：pair geometry、top1、hard tail及kernel是不同变化。整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)，13141→无法重训Target两段。不把该局部命题提升为完整recipe/生产保证。

### [G$^2$PTQ: Improving LLM Post-Training Quantization with Generalized Gradient Compensation](https://arxiv.org/abs/2609.31009v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：partial-quantized block刷新梯度/曲率与估计预算一阶补偿。整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，LoopPTQ→PTQ/QAT两段。不把该局部命题提升为完整recipe/生产保证。

### [Nonparametric In-Context Learning under Growing Geometric Complexity: Minimax Optimality and Local Geometry-Adaptivity of Transformers](https://arxiv.org/abs/2609.31458v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：geometry-first comparator与prompt样本/训练任务双预算权限。整合：WORLDVIEW-LLM-INTELLIGENCE [Ch8](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md)，context质量state→Post-training两段。不把该局部命题提升为完整recipe/生产保证。

### [Where a Model Sends Its Own Repeated Token](https://arxiv.org/abs/2609.31181v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：fixedpoint集合cardinality反证与source-paired destination/null/precision floor。整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，subject身份→adapter例子两段。不把该局部命题提升为完整recipe/生产保证。

### [Stale-Document Poisoning: When Outdated Retrieval Overrides Correct Model Answers](https://arxiv.org/abs/2609.31342v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：metadata存在不等reader遵守有效期，RAG纠正与损坏须双侧评价。整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，Temporal旧binding→权威后继两段。不把该局部命题提升为完整recipe/生产保证。

### [Beyond Approved Actions: Runtime Validation of Persistent Outcomes in Agent Workflows](https://arxiv.org/abs/2609.31301v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：effect profile、同candidate equality与backend capability分权。整合：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，LIBOS旧binding→Discovery两段。不把该局部命题提升为完整recipe/生产保证。

### [Estimating and Orthogonalizing Unknown Pre-training Gradients for Continual Fine-tuning of Large Language Models](https://arxiv.org/abs/2609.30935v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：虚拟更新搜索synthetic保护gradient与有限步/coverage权限分离。整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，14010→EmbeddingNoise两段。不把该局部命题提升为完整recipe/生产保证。

### [MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2609.30837v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：base-relative专长方向与student教学方向的token级筛选/权重分权。整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，debate→Self-distillation两段。不把该局部命题提升为完整recipe/生产保证。

### [Persistent Negatives for Adversarial Black-Box On-Policy Distillation](https://arxiv.org/abs/2609.30864v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：历史完整比较仅训练RM，fresh groups仍唯一进入policy update。整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，14071→混合Occupancy两段。不把该局部命题提升为完整recipe/生产保证。

### [Recursive Self-Improvement via On-Policy Distillation for Reasoning](https://arxiv.org/abs/2609.30652v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：特权guidance与无gold改写的独立CE/admission分支。整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，ContextDistillation成本→carrier两段。不把该局部命题提升为完整recipe/生产保证。

### [TISD: On-Policy Self-Distillation with Trajectory Intervention](https://arxiv.org/abs/2609.30878v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：teacher一次branch提案后由student采新suffix、原反馈监督新状态。整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，privileged evidence→ContextDistillation两段。不把该局部命题提升为完整recipe/生产保证。

### [Highlight-Then-Summarize: Learning to Compress Evidence for Long-Context Understanding](https://arxiv.org/abs/2609.31382v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：E/S/A分开训练及预算反转限定过程目标。仅报告：局部layout/harmonic奖励与参数—质量frontier，无一般aggregation因果或新通用知识缺口。不把该局部命题提升为完整recipe/生产保证。

### [Entropy Regularization: A Free Correction to Cross-Entropy for Verified Demonstrations](https://arxiv.org/abs/2609.30572v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：演示likelihood、采样分布正确集合与token entropy proxy分权。整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，masked CE→loss-mask示例两段。不把该局部命题提升为完整recipe/生产保证。

### [ViSTA: A Simple Bridge Extends Visual Alignment to Clinical Time-Series Understanding in Multimodal LLMs](https://arxiv.org/abs/2609.31448v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：内部变量summary与原visual token残差桥的局部选择。仅报告：同参数桥接口/任务frontier，不外推通用信息保留或临床效力。不把该局部命题提升为完整recipe/生产保证。

### [Strategically Diverse Sampling for Self-Training](https://arxiv.org/abs/2609.31571v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：同题approach预分叉采样与correct过滤/策略覆盖独立。整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)，synthetic开头→行为树前两段。不把该局部命题提升为完整recipe/生产保证。

### [DynBranch: Speculative Subgraph Reuse for Dynamic Agentic LLM Serving](https://arxiv.org/abs/2609.31047v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：未resolve候选的不可见shadow与setup/fill负载准入分开。整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，Pythia→coldwarmup前两段。不把该局部命题提升为完整recipe/生产保证。

### [Authority at Commit Time: Reject-and-Rerun Semantics for Governed Agentic Systems](https://arxiv.org/abs/2609.31490v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：governing subset与admission/dispatch两时点的权限不同。整合：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，runpin→Feedback两段。不把该局部命题提升为完整recipe/生产保证。

### [Low-Rank Friction for Memory-Efficient Transformer Pretraining](https://arxiv.org/abs/2609.30342v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：平方momentum形成friction而非平方gradient缩放position。整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，roleallocation→Embedding两段。不把该局部命题提升为完整recipe/生产保证。

### [Compact Documentation for Coding Agents: A Benchmark, an Optimizer, and Why It Does Not Transfer](https://arxiv.org/abs/2609.31587v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：roundtrip proxy与真实交付、derived handbook与current source分权。已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)；不E整recipe。不把该局部命题提升为完整recipe/生产保证。

### [Multi-agent Scaling Across Disjunctive and Compensatory Tasks](https://arxiv.org/abs/2609.31563v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：conditional-iid与item bias、oracle/plurality/平均的极限不同。整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，Peer/Debate→Blackboard两段。不把该局部命题提升为完整recipe/生产保证。

### [Towards Mitigating Fabricated Consensus: The Active Provenance Gate for Multi-Agent Debate Synthesis](https://arxiv.org/abs/2609.31422v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：闭世界PF句比例/强制共识与实际发布权分开。已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)；不E完整recipe。不把该局部命题提升为完整recipe/生产保证。

### [A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory](https://arxiv.org/abs/2609.30813v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：lineage/truth分轴、assertion≠citation、写入/暴露/采纳三事件。整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)，SelfStore→LateConstruction两段。不把该局部命题提升为完整recipe/生产保证。

### [Not All Memories Are Equal: Hierarchical Collaborative Memory for Validity-Aware Retrieval in LLM Agents](https://arxiv.org/abs/2609.30289v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：学习current/history两级维护与soft validity重排，不等valid-only gate。仅报告：局部维护/soft-rank recipe，不改变授权、有效期与并发通用合同。不把该局部命题提升为完整recipe/生产保证。

### [Cartograph: Federated Tool Discovery with Operator-Attested Retrieval for AI Agents](https://arxiv.org/abs/2609.30293v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：operator签文本与派生embedding分权、粗server召回决定tool shortlist。整合：AGENT-MCP [Ch83](../../../../books/part-07-agent/83-mcp.md)，ToolDescription→组合Admission两段。不把该局部命题提升为完整recipe/生产保证。

### [When Is a Multi-Agent Code Judge Actually Grounded? Two Label-Free Measurements, and a Judge That Declines to Guess](https://arxiv.org/abs/2609.30328v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：question相同不认证候选证据/verification output不可区分。暂缓：printed无区分力充分性隔离，有限经验gate与coverage保留。不把该局部命题提升为完整recipe/生产保证。

### [FuseReg: Regularizing Layer Fusion Mitigates the Reconstruction-Generation Gap in Representation Autoencoders](https://arxiv.org/abs/2609.31620v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：随机nonempty layermean及decoder/DiT两个率与目标分开。整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，RepresentationArtifact→Fusion两段。不把该局部命题提升为完整recipe/生产保证。

### [DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation in Few-Step Video World Models](https://arxiv.org/abs/2609.31349v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：teacher状态支持与critic拟合困难的表示/预算分权。整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，reward-target→09536前两段。不把该局部命题提升为完整recipe/生产保证。

### [The Linear Representation Hypothesis for Vision-Language-Action Models](https://arxiv.org/abs/2609.30996v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：propagatedQoI线性probe存在与policy自然参数steering条件分开。整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，Actionchunk→Trajectory前两段。不把该局部命题提升为完整recipe/生产保证。

### [OneWorld: Learning Consistent Physics Across Actions in World Models](https://arxiv.org/abs/2609.30946v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：共同mechanism posterior支持与个体/共享fit/gap分开。整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，common-reset→action-recovery两段。不把该局部命题提升为完整recipe/生产保证。

### [Action Forcing: Training World Models on Unsupervised Video by Recovering Underlying Egomotion Bases](https://arxiv.org/abs/2609.30595v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：数据PCA零点与noop、teacher输出label与generator真实target分权。整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，inverse20104→GUI两段。不把该局部命题提升为完整recipe/生产保证。

### [InternW0-$\Delta$: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data](https://arxiv.org/abs/2609.31394v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：部署change表示与两future监督/4D删除分权，mask才授contextKV复用。整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，PFD→ActionRepresentation两段。不把该局部命题提升为完整recipe/生产保证。

### [Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability](https://arxiv.org/abs/2609.31048v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：expert-relative非单调恢复与observedterminalfrontier/采样预算分权。整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，OfflineFailure→EvaluationLadder两段。不把该局部命题提升为完整recipe/生产保证。

### [Learning to Stop without Learning to Stop: Self-Supervised Confidence Training Improves Reasoning Efficiency](https://arxiv.org/abs/2609.31619v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：自监督概率标签改变效率但不同于可靠停止/校准。仅报告：限定训练recipe经验，未确立通用stopping机制；任务质量反退保留。不把该局部命题提升为完整recipe/生产保证。

### [Compress What You See, Not What You Say: Anchored Context Distillation for Latent-Observation Software Engineering Agents](https://arxiv.org/abs/2609.31430v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：双view独立behavior anchor与表示迁移cache成本。整合：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)，POINTS后两段。不把该局部命题提升为完整recipe/生产保证。

### [Completed Pairs Hide Capped Failures: A ReVerPi Case Study of Selective Context Projection](https://arxiv.org/abs/2609.31381v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：成对观测机会依赖first-arm完成造成zero positivity与有限识别。整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，ResponseRate后两段。不把该局部命题提升为完整recipe/生产保证。

### [Which Influence Are We Estimating? The Role of Counterfactual Specifications in Data Attribution](https://arxiv.org/abs/2609.31214v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：先声明B/P/T估计目标，再用匹配reference检近似误差。整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)，SAE attribution后两段。不把该局部命题提升为完整recipe/生产保证。

### [Monitor Jailbreaking: Evading Chain-of-Thought Monitoring Without Encoded Reasoning](https://arxiv.org/abs/2609.31121v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：完整可读推理也可操纵monitor framing，paraphrase恢复有损。整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，CoT score→runtime前两段。不把该局部命题提升为完整recipe/生产保证。

### [Stealth Apart, Harm Together: Skill Cascading Attacks on Skill-Based Agent Systems](https://arxiv.org/abs/2609.30383v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：多个declared-capability内变换串联消关键signal，commitment审计不同于concat扫描。整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，Skill描述后两段。不把该局部命题提升为完整recipe/生产保证。

### [ScopeBench: Do Agents Preserve Engagement Boundaries Under Goal Pressure?](https://arxiv.org/abs/2609.30325v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：无合法路径时机械成功floor与failed-stratum过程judge分权。整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，adaptive profile后两段。不把该局部命题提升为完整recipe/生产保证。

### [Prompt Injection Detection for Email Agents Through Attack Chain Modeling](https://arxiv.org/abs/2609.30657v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：阶段预测前提/条件分母与实际receipt及policy operatingpoint分权。整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，Containment末两段。不把该局部命题提升为完整recipe/生产保证。

### [In-Context Binding Capacity in Language Models](https://arxiv.org/abs/2609.30634v1)

复用[09/28 Daily §4](../../09/28/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：own-ceiling归一化容量不能代替absolute task requirement与实测可行集。整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)，eval slices后两段。不把该局部命题提升为完整recipe/生产保证。

### [TopoEP 2609.35481v1](https://arxiv.org/abs/2609.35481v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：共享矩阵确定deviceplan与两级topology成本门。整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，MoonEP→Cobalt，两段实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [WavePP 2609.35263v1](https://arxiv.org/abs/2609.35263v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：all-stage endpoint租约与suffix backing先commit、延后materialize。整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，05219→retention，两段实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [TempoKV 2609.35065v1](https://arxiv.org/abs/2609.35065v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：metadata claim与capacity commitment分开，由TTU/TTR共同触发。整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，prefetch23049→CacheScout，两段实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [Nereus 2609.34645v1](https://arxiv.org/abs/2609.34645v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：sealed TP/PP replica与跨stage转移DAG，feasibility与payback分权。整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，22614→token balance，两段实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [EfficientAgent 2609.33762v1](https://arxiv.org/abs/2609.33762v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：pool working-set压力下host writefilter与大池恢复写全的反向条件。整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，初Eviction→ContextResidency，实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [AgentReplay 2609.32283v1](https://arxiv.org/abs/2609.32283v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：模型正常forward后、nextstate前固定轨迹，logicalroute/tool等待与runtime自由度分开。整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Runtime→AgentOutcome，实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [Introducing dots](https://openai.com/index/introducing-dots/)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：主动只读发现不继承delegated task执行权限。整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)，Omni→Scheduling，实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [Towards safety cases for frontier AI training](https://openai.com/index/towards-safety-cases-for-frontier-ai-training/)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：持续case失效暂停covered runs，派生数据/评分恢复与权重rollback分开。整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，SafetyEval首两段，实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [How we will do better for Australia](https://openai.com/index/how-we-will-do-better-for-australia/)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：初步受影响方通知不等待最终调查归因，已知/未知分别提交。整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，n-days→匿名，两段实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [Read-Blindness 2609.35630v1](https://arxiv.org/abs/2609.35630v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：读敏感、写增量与累积的不同权限。整合：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)，两段实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [Entity Copy 2609.35663v1](https://arxiv.org/abs/2609.35663v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：context参与准备路由不等于原生context读出提供答案。整合：`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md)，两段实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [Rubric IRT 2609.35646v1](https://arxiv.org/abs/2609.35646v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：条件latent测量与冻结测量器的criterion信息预算。整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，两段实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [SparseOPD 2609.34386v1](https://arxiv.org/abs/2609.34386v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：全correction观察和有符号稀疏head微分分离。整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)，两段实际写后root通过。不把该局部命题提升为完整recipe/生产保证。

### [ProbeQuant 2609.33923v1](https://arxiv.org/abs/2609.33923v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：isolated uncertainty、input secondmoment与downstream目标不同权限。整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，实际两段root写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Reset Is Not Recovery 2609.33672v1](https://arxiv.org/abs/2609.33672v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：reset事件不等于effectivecontext恢复，以pairedclean核残余影响。整合：`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md)，实际两段root写后通过。不把该局部命题提升为完整recipe/生产保证。

### [LLaDA-Guard 2609.33634v1](https://arxiv.org/abs/2609.33634v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：labelconditional重构证据域与verdict权限。整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际两段root写后通过。不把该局部命题提升为完整recipe/生产保证。

### [World-Model Post-Training Audit 2609.33335v1](https://arxiv.org/abs/2609.33335v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：正确预测内容与额外优化、selection与coverage归因拆开。整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，实际两段root写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Perturbed Documents 2609.33642v1](https://arxiv.org/abs/2609.33642v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：同question/rubric的with/without文档双侧admission门。整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)，实际两段root写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Event-Set Completion Distillation 2609.34738v1](https://arxiv.org/abs/2609.34738v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：实际child completion集合总概率不同于单token配给。整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)，实际两段root写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Torch-PIM 2609.34657v1](https://arxiv.org/abs/2609.34657v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：Lowering 产生的实际 loop nest 决定放置候选域与 host profile 权限。整合：`INFER-TENSORRT-LLM` [Ch49 lowering→dequantization](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [SpecStream 2609.33184v1](https://arxiv.org/abs/2609.33184v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：仅迁移已提交历史、多 query 流式验证与 target 优先准入。整合：`INFER-SPECULATIVE-DECODING` [Ch48 memory-budget→drafter](../../../../books/part-05-inference-system/48-speculative-decoding.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Planarian 2609.35366v1](https://arxiv.org/abs/2609.35366v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：预先可补偿操作与 tool-boundary 联合 capture，不自授远端 fork。整合：`AGENT-WORKFLOW` [Ch81 AgentRewind→Waypoint](../../../../books/part-07-agent/81-workflow.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Dynamic Flow, Static Graph 2609.34727v1](https://arxiv.org/abs/2609.34727v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：固定图容纳选择性 KV 重算，并按实测调用成本规划 chunks。整合：`INFER-TENSORRT-LLM` [Ch49 静态图→基础优化](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [SPIMOE: Exploiting Hybrid Sparsity for Reasoning MoE Inference on Heterogeneous PIM Architectures 2609.34612v1](https://arxiv.org/abs/2609.34612v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：联合稀疏/PIM 的质量与资源耦合验证，不把 recipe 升为通用机制。仅报告：局部实现/评价不改变现有长期机制，具体理由见下节。不把该局部命题提升为完整recipe/生产保证。

### [PolyCIM: Improving Data Reuse in Digital CIM Accelerators with Polyhedral-Based Compilation 2609.34351v1](https://arxiv.org/abs/2609.34351v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：非轴向 reuse 先仿射 realignment，再映射有限 CIM/layout。整合：`INFER-TENSORRT-LLM` [Ch49 Nautilus→Persistent Executor](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Tool Waiting and Re-arrival in Compile-Time-Static LLM Serving: Cost Mechanisms and Configuration Selection 2609.34663v1](https://arxiv.org/abs/2609.34663v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：静态 bucket 与内生 tool re-arrival 联合决定 padding/驻留成本。整合：`INFER-CONTINUOUS-BATCHING` [Ch46 trade-off→工程判断](../../../../books/part-05-inference-system/46-continuous-batching.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Beyond Energy: When Sustainability Dimensions Reshape LLM Serving Decisions 2609.35569v1](https://arxiv.org/abs/2609.35569v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：固定部署运营排序与跨部署 embodied crossover 分账。整合：`PLATFORM-COST` [Ch70 Unit Economics 生命周期→需求反弹](../../../../books/part-06-ai-infrastructure/70-cost.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Beneath the Tokens: A Performance Engineering Study of Multi-Token Prediction in GPU-Accelerated LLM Inference 2609.35188v1](https://arxiv.org/abs/2609.35188v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：每有效 token 的调用摊销与单 kernel 时间不是同一指标。仅报告：局部实现/评价不改变现有长期机制，具体理由见下节。不把该局部命题提升为完整recipe/生产保证。

### [DPS: Dual-Mode Precision LLM Serving with Semi-Unified Memory 2609.34380v1](https://arxiv.org/abs/2609.34380v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：persistent weights/residual/KV 非对称共享与 forward 模式提交。整合：`INFER-GPU-MEMORY` [Ch54 双模式 Weight 与 KV](../../../../books/part-05-inference-system/54-gpu-memory.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Where Activation Sparsity and KV-Cache Sparsity Cross in LLM Decoding 2609.33889v1](https://arxiv.org/abs/2609.33889v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：weight-read/KV-read 的 byte 交点还须质量和 kernel 成本校准。整合：`INFER-GPU-MEMORY` [Ch54 少读 Weight 与少读 KV 的交点](../../../../books/part-05-inference-system/54-gpu-memory.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Just Let Linear States Forget the Distant Past: Prefix Caching via SuffixReplay for Hybrid LLMs 2609.33477v1](https://arxiv.org/abs/2609.33477v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：按 linear group 保存输入锚点，近似 replay 与发布边界分开。整合：`INFER-KV-CACHE` [Ch45 Group 输入锚点→Video cache](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [BEHAVE: Functional Behavior Modeling Enables Self-Improving Agents for Hardware Design and Verification 2609.34785v1](https://arxiv.org/abs/2609.34785v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：允许 transaction timing 差异但双产物都须独立 hidden gold。整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 Transaction oracle→Dense Process](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Argus: Agentic, Reference-Calibrated, Tree-Guided, System-Software-Level Bottleneck Localization 2609.35508v1](https://arxiv.org/abs/2609.35508v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：同 workload reference 与 tree/probe 定位的受限实现验证。仅报告：局部实现/评价不改变现有长期机制，具体理由见下节。不把该局部命题提升为完整recipe/生产保证。

### [Hardware-Aware Features for CUTLASS Kernel Selection 2609.35587v1](https://arxiv.org/abs/2609.35587v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：candidate-induced 硬件代理排序、shape-group 留出与执行 coverage。整合：`INFER-TENSORRT-LLM` [Ch49 硬件行为代理→Tensor Core层级](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Semantic Prefix Oracles 2609.35425v1](https://arxiv.org/abs/2609.35425v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：语义 prefix 安全剪枝与可完成性是两份合同。整合：`INFER-SGLANG` [Ch51 Structured Generation→Adapter readiness](../../../../books/part-05-inference-system/51-sglang.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Rubric-Calibrated Preferences 2609.35739v1](https://arxiv.org/abs/2609.35739v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：query内BT排序与跨query单位/原点分开校准。整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66 Judge Ranking→Route/defer](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [SpeakGR 2609.35430v1](https://arxiv.org/abs/2609.35430v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：扩SID词表后分开检索正确与原文本条件分布保护。整合：`TRAIN-SFT` [Ch29 Occupancy→共享Trace](../../../../books/part-04-training-system/29-sft.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [TRACE 2609.33517v1](https://arxiv.org/abs/2609.33517v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：return epoch 下逐项有效不等整组关键义务覆盖。整合：`AGENT-MEMORY` [Ch77 Memory Read Recency→累计披露](../../../../books/part-07-agent/77-memory.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Revision, Not Restart: Revisable Visual Plans for Closed-Loop World–Action Models 2609.35439v1](https://arxiv.org/abs/2609.35439v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：保存visual solver路径，用真实feedback修订未执行计划再解动作。整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 World-action→Future-to-Action](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining 2609.35652v1](https://arxiv.org/abs/2609.35652v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：common endpoint loss下clean-head/velocity-head改变noise burden。整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 固定点decoder→endpoint initialization](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching 2609.35469v1](https://arxiv.org/abs/2609.35469v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：flow阶段绑定code可见性形成ordered increments而非物理因果。整合：`MULTIMODAL-EMBODIED-VLA` [Ch26 离散codec→粗planner/refiner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Signal or Noise? Modality Contribution and Cooperation in Multimodal GraphRAG 2609.35304v1](https://arxiv.org/abs/2609.35304v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：supporting-edge subset admission与明确baseline的模态交互诊断。整合：`AGENT-RAG` [Ch76 多模态admission→Escalation](../../../../books/part-07-agent/76-rag.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [MASTraceBench: Diagnosing Collaboration Gains through Proposal Trajectories in LLM-Based Multi-Agent Systems 2609.34496v1](https://arxiv.org/abs/2609.34496v1)

复用[09/29 Daily §4](../../09/29/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：initial→final proposal→aggregate分三层质量账。整合：`AGENT-MULTI-AGENT` [Ch82 Evaluation成本表→条件分支](../../../../books/part-07-agent/82-multi-agent.md)；实际正文与非作者写后通过。不把该局部命题提升为完整recipe/生产保证。

### [Sieve and Sage: Efficient Distraction Filtering for Reliable RALM Abstention — 2609.35794v1](https://arxiv.org/html/2609.35794v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：检索缺证据与存在证据却受干扰需要不同补救；生成前gate提供条件性路由。 。整合：`AGENT-RAG` / [Ch76](../../../../books/part-07-agent/76-rag.md)。不把该局部命题提升为完整recipe/生产保证。

### [When Successful Memories Mislead Embodied Agents: Memory Adaption For Task-Conditioned Execution — 2609.35808v1](https://arxiv.org/html/2609.35808v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：成功轨迹的旧动作schema仍能误导；将接口兼容收益与压缩收益分开。 。整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)。不把该局部命题提升为完整recipe/生产保证。

### [How to Run Statistics over LLM Judges and Trust the Results: Calibrated Inference for Small-Sample AI Evaluation with evalstats — 2609.35815v1](https://arxiv.org/html/2609.35815v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：高judge agreement不保证区间/检验校准；人工配对抽样和估计不确定性改变发布判断。 。整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。不把该局部命题提升为完整recipe/生产保证。

### [Less Uniform Discrete Diffusion is More Powerful and Scalable — 2609.35817v1](https://arxiv.org/html/2609.35817v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：uniform reverse目标的平滑与corruption身份耦合；清洁目标和per-token time改变训练解释。 。整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。不把该局部命题提升为完整recipe/生产保证。

### [When Should LLMs Trust Their Own Revisions? A Risk-Aware Study of Intrinsic Self-Correction — 2609.35832v1](https://arxiv.org/pdf/2609.35832v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：修正错误与引入新错必须分账，revision前gate和后验acceptance预算不同。 。已有覆盖：`AGENT-REFLECTION` / [Ch80](../../../../books/part-07-agent/80-reflection.md)。不把该局部命题提升为完整recipe/生产保证。

### [The Detectability Gap: Hidden Heterogeneity in Hallucination Detection Across Language Models — 2609.35860v1](https://arxiv.org/html/2609.35860v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：用同一统计量定义难组再测detectability会自造gap；冻结partition后须换signal检验。 。整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。不把该局部命题提升为完整recipe/生产保证。

### [Mnemon: Raw Records, Fast Judgments, Slow Thoughts — 2609.36059v1](https://arxiv.org/html/2609.36059v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：raw authority已覆盖；新增判定器替换条件及waves、总判断、lifecycle cost的不同预算。 。整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)。不把该局部命题提升为完整recipe/生产保证。

### [Targeting Pivotal Decisions for Credit Assignment in Agentic Reinforcement Learning — 2609.36178v1](https://arxiv.org/html/2609.36178v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：judge选址不等数值credit；恢复两端状态，用固定current policy续跑估局部贡献。 。整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)。不把该局部命题提升为完整recipe/生产保证。

### [Learning from Teacher Continuations at Student States — 2609.36246v1](https://arxiv.org/html/2609.36246v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：teacher文本continuation免logit接口，但其后续状态及CE监督边界不同于逐token纠错。 。整合：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md)。不把该局部命题提升为完整recipe/生产保证。

### [Reliable Parallel Decoding in Masked Diffusion Language Models — 2609.36452v1](https://arxiv.org/html/2609.36452v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：同pass高confidence不足以joint commit；final-layer稳定性与未解决上游熵约束承诺集合。 。整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。不把该局部命题提升为完整recipe/生产保证。

### [ParaAnya: Accelerating Parallel Diffusion Sampling with Plug-and-Play Output Caching — 2609.36522v1](https://arxiv.org/html/2609.36522v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：并行迭代反复访问同timestep可缓存输出，但命中检查及通信可能吃掉NFE收益。 。整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。不把该局部命题提升为完整recipe/生产保证。

### [SEED: Self-Speculative Decoding via Implicit Encoder-Decoder — 2609.36590v1](https://arxiv.org/html/2609.36590v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：verifier刷新deep KV，再由薄末层读raw embedding起草，形成自推测的另一条件分支。 。整合：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。不把该局部命题提升为完整recipe/生产保证。

### [Replay the Curvature: Accurate and Scalable NVFP4 Quantization for Large Language Model Inference — 2609.36654v1](https://arxiv.org/html/2609.36654v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：未来列可补偿时当前误差应条件化；scale候选需私有回放真实顺序量化轨迹。 。整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。不把该局部命题提升为完整recipe/生产保证。

### [ATTUNER: Recomputation-Free KV Cache Reuse via Query-Side Adaptation — 2609.36722v1](https://arxiv.org/pdf/2609.36722v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：独立artifact KV丢跨artifact条件；冻结cache producer并训练query consumer，不将位置修复当充分条件。 。整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。不把该局部命题提升为完整recipe/生产保证。

### [Reshaping Rollout Workloads for Asynchronous RL Post-Training on Heterogeneous Accelerators — 2609.36899v1](https://arxiv.org/html/2609.36899v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：暂停长轨迹可改善resident组成；depart/destination分离改变异构rollout调度。 。整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。不把该局部命题提升为完整recipe/生产保证。

### [MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation — 2609.36903v1](https://arxiv.org/html/2609.36903v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：长多方双语评价及固定架构data对照限制由短dyadic效果外推的能力判断。 。仅报告：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；新增证据不改长期机制，旧机制不重评。不把该局部命题提升为完整recipe/生产保证。

### [Dating the Model: Hidden Dates in System Prompts Affect LLM Evaluation — 2609.36931v1](https://arxiv.org/html/2609.36931v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：system date是确定性输入干预，隐藏默认值可改变比较而非随机采样噪声。 。已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。不把该局部命题提升为完整recipe/生产保证。

### [Efficient Agentic LLM Serving over SSD-based Sparse KV Storage — 2609.36938v1](https://arxiv.org/html/2609.36938v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：预测层间selector可预取，但target native selector及缺失补读仍决定Attention可见状态。 。整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。不把该局部命题提升为完整recipe/生产保证。

### [ER-JEPA: Experience Replay Improves Joint-Embedding Predictive Learning in Language Models — 2609.36952v1](https://arxiv.org/html/2609.36952v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：匹配compute/token/current-batch对照仍显示历史内容作用；初筛关闭理由因此被独立反证。 。已有覆盖：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md)。不把该局部命题提升为完整recipe/生产保证。

### [Purlin: Separating Orchestration from the Datapath of Collectives — 2609.36954v1](https://arxiv.org/html/2609.36954v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：layout/copy-reduce语义和coordination可复用，但hardware datapath及数值policy不等价。 。整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。不把该局部命题提升为完整recipe/生产保证。

### [Cobalt: Leveraging Expert Co-activation for Efficient Distributed MoE Training — 2609.36959v1](https://arxiv.org/html/2609.36959v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：单token多expert的destination-node union不同于各expert负载和，改变布局目标。 。整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。不把该局部命题提升为完整recipe/生产保证。

### [Learning from Think-Mode Advantage via On-Policy Distillation — 2609.37044v1](https://arxiv.org/html/2609.37044v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：teacher优势与trace对兄弟response的可转移性分离，用group路由权重而非一律强模仿。 。整合：`TRAIN-SFT` / [Ch29](../../../../books/part-04-training-system/29-sft.md)。不把该局部命题提升为完整recipe/生产保证。

### [vSkipper: Translating Dynamic Layer Skipping into LLM Serving Gains — 2609.37062v1](https://arxiv.org/html/2609.37062v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：内部skip仍需本层KV投影和route元数据；policy省层不自动成为引擎收益。 。整合：`INFER-SGLANG` / [Ch51](../../../../books/part-05-inference-system/51-sglang.md)。不把该局部命题提升为完整recipe/生产保证。

### [ToolFence: Fine-Grained Authorization for Secure Tool-Using LLM Agents — 2609.37196v1](https://arxiv.org/html/2609.37196v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：capability shape grant与当前具体值provenance分离；缓存授权不能缓存证据真值。 。整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。不把该局部命题提升为完整recipe/生产保证。

### [Compiling Learning Problems into Adaptation Programs for Language Models — 2609.37371v1](https://arxiv.org/html/2609.37371v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：episode geometry可摊销选择adaptation program；未知family仍需default与适配成本预算。 。整合：`TRAIN-LORA` / [Ch30](../../../../books/part-04-training-system/30-lora.md)。不把该局部命题提升为完整recipe/生产保证。

### [Your Benchmark Is Not Saturated: Reviving Multiple-Choice Evaluation with Answer Pooling — 2609.37494v1](https://arxiv.org/html/2609.37494v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：共享答案池把单题分类变耦合assignment；chance和干扰控制变化须与原任务分开。 。整合：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。不把该局部命题提升为完整recipe/生产保证。

### [DScale: Scaling Block-Diffusion Speculative Decoding with Adaptive Verification — 2609.37532v1](https://arxiv.org/html/2609.37532v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：保完整草稿而限ragged verification共享预算；图固定地址不意味着commit边界固定。 。整合：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。不把该局部命题提升为完整recipe/生产保证。

### [E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models — 2609.37533v1](https://arxiv.org/html/2609.37533v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：离散router latent可让parallel reverse采样相关；clean/noisy router匹配决定训练推理接口。 。整合：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。不把该局部命题提升为完整recipe/生产保证。

### [Correct, Don't Delete: Mitigating Emergent Misalignment with Corrective Supervision — 2609.37624v1](https://arxiv.org/html/2609.37624v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：删除坏监督移除该输入的训练机会，纠正则尝试供正面目标；两种intervention不可混同。 。整合：`TRAIN-DATA` / [Ch27](../../../../books/part-04-training-system/27-data.md)。不把该局部命题提升为完整recipe/生产保证。

### [SPLASH: Switching Parallel Layouts of Attention with Seamless Handoff for LLM Serving — 2609.37626v1](https://arxiv.org/html/2609.37626v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：projection/KV ownership解耦后，live-layout切换需稳态+暂态容量及共同handoff。 。整合：`INFER-SCHEDULING` / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)。不把该局部命题提升为完整recipe/生产保证。

### [Honeycomb: Constant-Size Scene Memory Representation for Video World Models — 2609.37690v1](https://arxiv.org/html/2609.37690v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：固定planes在expanding bounds下warp/coarsen；存储恒定不等信息精度恒定。 。整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。不把该局部命题提升为完整recipe/生产保证。

### [Delta-Matching: Closing the Final Gap of Native 8-bit Training for LLMs — 2609.37852v1](https://arxiv.org/html/2609.37852v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：量化dP使saved delta失配，重算匹配contraction恢复softmax梯度零行和。 。整合：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)。不把该局部命题提升为完整recipe/生产保证。

### [Retrieval Capacity of Self-Attention Under Competition — 2609.37879v1](https://arxiv.org/html/2609.37879v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：权重不等独立知识贡献；V方向及delete/renormalize不同干预改变诊断解释。 。整合：`MODEL-SELF-ATTENTION` / [Ch14](../../../../books/part-02-model/14-self-attention.md)。不把该局部命题提升为完整recipe/生产保证。

### [It's All Training: A Fully Synthetic Single-Stage Recipe for LLMs — 2609.37891v1](https://arxiv.org/html/2609.37891v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：旧synthetic pipeline不重算；本窗同600M/data trace ablation和seed外反证限制效率归因。 。仅报告：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；新增证据不改长期机制，旧机制不重评。不把该局部命题提升为完整recipe/生产保证。

### [Scaling Zero-Order Pretraining through Model Sharding — 2609.37899v1](https://arxiv.org/html/2609.37899v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：可分目标移除跨expert SPSA噪声，以表征耦合换独立更新，非通用通信分片。 。整合：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)。不把该局部命题提升为完整recipe/生产保证。

### [Learning What to Remember: Long-horizon Counterfactual Memory Optimization — 2609.37930v1](https://arxiv.org/html/2609.37930v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：rewrite总效用含继承收益；相邻状态对同future targets的增量才接近本次write credit。 。整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)。不把该局部命题提升为完整recipe/生产保证。

### [How Local Mixing Encodes Relative Position in Global NoPE Attention — 2609.38109v1](https://arxiv.org/html/2609.38109v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：局部mixing及Q/K对齐能读implicit recency，修正必须显式PE的绝对句。 。整合：`MODEL-POSITION-ENCODING` / [Ch13](../../../../books/part-02-model/13-position-encoding.md)。不把该局部命题提升为完整recipe/生产保证。

### [WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms — 2609.38121v1](https://arxiv.org/html/2609.38121v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：K/query与V/output需要不同consumer metric，post-RoPE变换折叠及在线代价不同。 。整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。不把该局部命题提升为完整recipe/生产保证。

### [HelixWorld: A Real-time Interactive Audio-Visual World Model — 2609.38123v1](https://arxiv.org/html/2609.38123v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：camera/world state联合条件视听，在student自身轨迹纠偏streaming而非只换音轨。 。整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。不把该局部命题提升为完整recipe/生产保证。

### [AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation — 2609.38142v1](https://arxiv.org/html/2609.38142v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：advisor对recorded response的预测敏感性可选择监督，但不是executor反事实因果。 。整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)。不把该局部命题提升为完整recipe/生产保证。

### [Rho: A Foundation for Efficiently Adaptable VLA Models — 2609.38164v1](https://arxiv.org/html/2609.38164v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：embodiment midtraining→任务更新→冻结action generator的latent repair分开适配authority。 。整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。不把该局部命题提升为完整recipe/生产保证。

### [STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization — 2609.38169v1](https://arxiv.org/html/2609.38169v1)

复用[09/30 Daily §4](../../09/30/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：state误差随transition传播；readout时序与temporal/spatial敏感度影响量化生命周期。 。整合：`INFER-GPU-MEMORY` / [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)。不把该局部命题提升为完整recipe/生产保证。

### [Disrupting a coordinated model distillation campaign](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：密文隐藏不等消费授权，跨身份/model-family重放需与release gate分层。整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：风险监测与训练反馈权限分账，不能优化低monitor score代替安全。整合：`PLATFORM-SECURITY` / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，仅反馈分工增量，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [TomasuLLM](https://arxiv.org/html/2609.38201v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：真实工具推测执行需要区分operand就绪、当前提交与预测观测的后继有效性。整合：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)，COW搜索与Live Fork之间，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [The System Prompt Illusion](https://arxiv.org/html/2609.38205v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：probe可读、表征几何相似、局部patch因果证据不能互换；设计反证加深。已有覆盖：`WORLDVIEW-REPRESENTATION` / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，仅readout/局部因果分账。不把该局部命题提升为完整recipe/生产保证。

### [Conformal Factuality Control for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/html/2609.38222v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：全回答支持率含空输出，不等于非空回答的条件支持率；verifier标签不是语义真值。已有覆盖：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，仅分母及oracle权限边界。不把该局部命题提升为完整recipe/生产保证。

### [SpecScale](https://arxiv.org/html/2609.39334v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：逻辑候选数不等实际forward数，独立draw与PRM排队分别控制；长期机制缺口加深。整合：`INFER-CONTINUOUS-BATCHING` / [Ch46](../../../../books/part-05-inference-system/46-continuous-batching.md)，iteration工作单元后，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [Preserving Provenance in Shared KV Caches](https://arxiv.org/html/2609.38706v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：local key正确不保证connector保留计算等价和sharing权限，跨worker/lookup-store身份须一致。整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，Prefix reuse，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [Vosti](https://arxiv.org/html/2609.38981v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：单kernel确定性不足wholeengine；canonical KV与relational kernel合同须组合。整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，数值验收，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [KVTether](https://arxiv.org/html/2609.39819v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：message变异须传播prefix版本失效，跨context引用和waiting age分账；长期缺口加深。整合：`INFER-KV-CACHE` / [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，Agent语义区域后，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [Characterizing High Bandwidth Flash for LLM Serving](https://arxiv.org/html/2609.39131v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：flash层容量不免费，write endurance、缓存锁定与admission压力联合规划；长期缺口加深。整合：`INFER-GPU-MEMORY` / [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)，扩展层级，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [The Planning Limits of Latent World Models](https://arxiv.org/html/2609.39235v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：精确transition仍会因目标评分短视失败，prediction质量与planning range不同。整合：`MULTIMODAL-WORLD-MODELS` / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，Imagined rollout，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [U-Fuzz](https://arxiv.org/html/2609.38275v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：正确memory不保证正确消费，query/state变异、探索与判错需分权；长期缺口加深。整合：`AGENT-MEMORY` / [Ch77](../../../../books/part-07-agent/77-memory.md)，Recall/Use之后，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [StateFork](https://arxiv.org/html/2609.38648v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：文件恢复不等session后续观察等价，逻辑分支与checkpoint物理化分权；恢复合同深入。整合：`AGENT-WORKFLOW` / [Ch81](../../../../books/part-07-agent/81-workflow.md)，联合恢复之后，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [Blackout and Freeze](https://arxiv.org/html/2609.39145v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：缺帧与陈旧帧不同，恢复任务成功不认证物理风险；安全设计反证。整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，Safety envelope，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [Two-step Flow VLA](https://arxiv.org/html/2609.39822v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：近action区间可另学平均velocity，NFE减少与控制质量必须分账；长期缺口加深。整合：`MULTIMODAL-EMBODIED-VLA` / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，solver分支，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [Prefix-invariant Fast Matrix Multiplication](https://arxiv.org/html/2609.39816v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：batch形状确定性不保证早先token不受未来影响，低精度累加需条件化prefix不变性。整合：`INFER-TENSORRT-LLM` / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，数值合同，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [HAPMoE](https://arxiv.org/html/2609.39350v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：异构stage不能事后固定同构EP/TPE，需要device-aware联合容量/通信/分区计划；长期缺口加深。整合：`TRAIN-PIPELINE-PARALLEL` / [Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md)，Stage Balance，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [ThunderEP](https://arxiv.org/html/2609.40093v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：host-only通信的relay traffic与依赖链收益不同，prefill DMA不能直接移植captured decode；长期缺口加深。整合：`TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，多路径分支，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [Gradient-Conflict Audit](https://arxiv.org/html/2609.38465v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：降冲突proxy不等改善任务，诊断有效性须区分预测/同期、干预/结果与population；设计反证加深。整合：`TRAIN-PRETRAINING` / [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，多模态方差冲突后，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [CW-OPD](https://arxiv.org/html/2609.38777v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：单world端点匹配不约束跨视觉响应，共同logit变化消项仅限transition；长期缺口加深。整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)，teacher对照分支，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [S-OPD](https://arxiv.org/html/2609.39120v1)

复用[10/01 Daily §4](../../10/01/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：teacher只选学生视觉contrast位置，mask敏感与noise稳定是不同辅助目标；长期缺口加深。整合：`TRAIN-GRPO` / [Ch33](../../../../books/part-04-training-system/33-grpo.md)，视觉选择分支，实际POST通过。不把该局部命题提升为完整recipe/生产保证。

### [MiniMax Code v0.6.0](https://github.com/MiniMax-AI/minimax-code/releases/tag/v0.6.0)

复用[10/02 Daily §4](../../10/02/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：BYOK宽重试需排除安全拒绝，拒绝说明不得污染状态码分类。整合：`AGENT-PLATFORM`，[Ch84状态机](../../../../books/part-07-agent/84-agent-platform.md#agent-runtime-state-machine)。不把该局部命题提升为完整recipe/生产保证。

### [OpenAgentCore v0.0.3（含v0.0.4同窗演进）](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.3)

复用[10/02 Daily §4](../../10/02/README.md#4-证据与知识整合)与[10/04 Daily §4](../../10/04/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：版本化CI Agent放宽工具/环境秘密边界，不能用main合入代替运行隔离。仅报告：具体配置事实，无新增防护机制或已测安全结果。不把该局部命题提升为完整recipe/生产保证。10/03部署事件的HTTP、浮动latest镜像和密钥格式反侧沿10/04精确配置复用，与10/01 CI秘密配置不是同一安全事件；归并不抹掉后续变化，也不重复家族评分。

### [DeepSeek Harness v0.2.1-alpha.1](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.2.1-alpha.1)

复用[10/04 Daily §4](../../10/04/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：插件子路径元数据、诊断导出与扩展入口的破坏性兼容契约。仅报告：alpha 版本迁移事实，不建立长期兼容机制结论。不把该局部命题提升为完整recipe/生产保证。

### [MiMo-Code：Provider Refresh Without Instance Disposal，PR #2603](https://github.com/XiaomiMiMo/MiMo-Code/pull/2603)

复用[10/04 Daily §4](../../10/04/README.md#4-证据与知识整合)的exact-v1/精确事件、必要位置、范围与反侧；本周沿用的受限命题是：保留 Instance 的 provider refresh：idle admission、先准备后统一发布、忙时不排队、closing-owner sampling 拒绝。仅报告：局部 SDK/运行时契约及可复用约束的实现例证，不扩大为通用热更新保证。不把该局部命题提升为完整recipe/生产保证。



### [PyTorch v2.14.1](https://github.com/pytorch/pytorch/releases/tag/v2.14.1)

采用release `published_at=2026-09-30T19:14:48Z`及其完整具名纠错；必要component证据为[CUDA13.2 Update2](https://docs.nvidia.com/cuda/archive/13.2.2/cuda-toolkit-release-notes/index.html) Compiler resolved/known与cuBLAS条目，不用最新文档替历史版本。两层以上nested divergence的reconvergence省略会留下旧register值，源程序合法不能证明编译artifact忠实；单层不在该条件中。cuBLASLt另一问题从CUDA13.2 Update1起，只涉及NVFP4输出、tensor-wide `D_SCALE_POINTER`、算法ID66及CC10.x/11.x，不是所有FP4都有问题。WGMMA `wait_group N>=1` copy-propagation仍列known issue，不因此patch发布全消失；MPS complex least-squares与SVD精度是另组受影响路径，未在本项目运行。

此前[Ch49 lowering commit boundary](../../../../books/part-05-inference-system/49-tensorrt-llm.md#lowering-与低精度执行都需要可回归的-commit-boundary)主要绑定source/计划；新增88–90行将compiler、cuBLAS、架构与算法加入运行artifact身份，并要求相关分支/非单位scale回归。修复交付、重新build与替换服务实例分开；增加component矩阵与回归成本，旧验证artifact仍可回退。root已实核必要原源与新增正文/邻接；这是窄正确性差额，不是运行认证。

### [SGLang v0.5.21](https://github.com/sgl-project/sglang/releases/tag/v0.5.21)

采用release `2026-10-02T01:09:04Z`，完整body仅作机制筛选，不把779条PR变库存。必要受影响核心与merge SHA保留于[PR核心](../_sources/2026-W40/PR_CORE.json)：[41023](https://github.com/sgl-project/sglang/pull/41023) Mooncake/NIXL默认deferred decode-KV回收要等全部已通知prefill rank ACK或30s timeout，Mori/fake不支持相应ACK因而opt-out；旧两帧ACK与超时行为是兼容边界。timer释放容量不构成DMA已retire的形式证明。[41557](https://github.com/sgl-project/sglang/pull/41557)只是layer-boundary指南/CPU collective stand-in，不当成新GPU runtime或性能实验。

[40777](https://github.com/sgl-project/sglang/pull/40777)处理多bucket加载后packed layout postprocess及target/draft runner，engine-owned正常加载与外部P2P/RDMA refit分支不同；Marlin/MXFP8/NVFP4 transforms与compressed W4A16 shape改变需要具名支持，未支持格式不得放行。[40105](https://github.com/sgl-project/sglang/pull/40105) fused FlashInfer finalize仍默认关闭以保数值精度，W4A4延迟/准确性压力不能以launch正确忽略。SafeUnpickler/chat-template具名安全变化只保留release范围，不授全fleet安全或声称全部安全PR已代码核验。

本次[Ch49 execution-plan commit](../../../../books/part-05-inference-system/49-tensorrt-llm.md#execution-plan-可以修订但只能在安全边界-commit)194–196行补checkpoint表示到kernel表示转换与完整bucket/multi-runner finalize；增加转换、双buffer、验证与失效责任，不支持时保留已验证plan。[Ch55 Handoff状态机](../../../../books/part-05-inference-system/55-pd-disaggregation.md#handoff-状态机)414–416行已明确 `ABORT → remote-write-retired → slot-reclaim` 与ACK的尾部/容量成本，故PD通用顺序不重复写，release默认仍仅具名版本事实。root必要PR/正文邻接POST通过。

### [FlashInfer v0.7.1rc1/.rc2与v0.7.0.post1](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.1rc1)

三个版本按release metadata归一项目家族（post1 Sep29 23:22:24Z、rc1 Sep30 16:43:06Z、rc2 Oct2 01:50:27Z），重要机制core是rc1所列纠错，post1/rc2仅保留版本谱系，不借空/简短body发明增量；既有Autotuner主题不重新评分。[5031](https://github.com/flashinfer-ai/flashinfer/pull/5031) per-token NVFP4零row在fast-math下可经无限scale产生NaN，作者回归不是本项目执行。[4894](https://github.com/flashinfer-ai/flashinfer/pull/4894) replay IDs仅routed `[T,K]`，不能用含shared experts的packed stride `K+S`；S=0掩盖问题，修正后维度K与T边界仍须验证。

[5350](https://github.com/flashinfer-ai/flashinfer/pull/5350)将cuDNN query-length storage交wrapper持有，capture/replay所引用prepared state不能因replan失效；device/layout/strides与scale/sink binding共同进入descriptor/cache identity。必要正反回归为 `capture → replan → allocator poison → replay` 的output/LSE reference、NHD/HND与特定B200 BF16 Hq/Hkv32/8 D128/cuDNN9.27/native-extension一致性；仍不支持的mask/scaling必须报错，single-token GQA prefill LSE拒绝保留，FP8部分xfail不变。不是所有cuDNN/FP8路径都已认证。

本次[Ch49 persistent executor](../../../../books/part-05-inference-system/49-tensorrt-llm.md#从逐-kernel-launch-到-persistent-executor)131行加prepared元数据寿命/绑定，而非另建kernel性能清单。驻留内存、完整key与更多回归换准备成本，兼容性不能证明则重plan或非capture回退。root已读5350正反侧并POST通过。

### [Transformers v5.18.0](https://github.com/huggingface/transformers/releases/tag/v5.18.0)

采用release Sep30 16:46:27Z。核心[48289](https://github.com/huggingface/transformers/pull/48289)把 `generate(use_cache=True/False)` 组成同例逐step logits对照，再只到首个near-tie前比较token IDs；near-tie判定使用processed scores而非logits，min-new-tokens下EOS负无穷须特殊处理，stateful模型另跳过。该测试实际暴露FSMT positions切片、sparse TopK布尔mask语义、PaliGemma生成token误继承bidirectional prefix、VibeVoice-ASR无cache路径丢audio等具名错误；它不发明KV近似等价，也不保证任意sampled轨迹逐token相同。

[48981](https://github.com/huggingface/transformers/pull/48981)扩大assisted generation EOS/max-length回归，修复此前候选特化而脆弱的停止条件，不证明所有candidate实现无终止错误；[48669](https://github.com/huggingface/transformers/pull/48669)Qwen2.5-VL小数temporal step应在grid index乘积后转换，0.5先截0会把多个frame positions坍缩，作者CPU案例不等下游GPU质量验收。release新增模型与CI安全条目没有被逐条当作算法候选。

[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md#为什么缓存-kv-而不是-query)37–39行补KV因果解释到实现验证之间的配对两路径/near-tie控制；原先只解释理论复用正确，不能替真实position/mask实现。测试增时与有界误差不能免除失败时full recompute，精确与近似路径仍分权。root已核48289实际测试核心及新增正文/邻接POST。

### [Ray v2.59.0](https://github.com/ray-project/ray/releases/tag/ray-2.59.0)

采用release Oct2 07:04:37Z及具名核心。[64755](https://github.com/ray-project/ray/pull/64755)只使无address的本地 `ray.init()` 在未显式设置时自动生成/复用auth token并warning；`ray start --head` 若没有现存token仍不启auth、只warning，有token才自动开启，远端connect/worker未统一改变。未来默认token所需KubeRay等credential分发不当成本版本交付。[65780](https://github.com/ray-project/ray/pull/65780)Hudi unpickle guard/已知RCE回归不是通用反序列化证明。

[65420](https://github.com/ray-project/ray/pull/65420)取消lease的tombstone IDs用于幂等/消息乱序，避免逐lease RPC风暴；late-granted reply反侧仍需release具名后续限制，不能称全取消链已无竞态。[65193](https://github.com/ray-project/ray/pull/65193)BackpressureConfig是opt-in429/503与独立Retry-After，默认503/no header保留，deployment unavailable仍503、gRPC RESOURCE_EXHAUSTED不变；不能假设客户端看到429自动正确重试。

仅报告：这是具名版本入口与配置差额，没有新增长期授权机制、全局取消协议证明或生产可用性结果。虽然[Ch72授权/执行分权](../../../../books/part-06-ai-infrastructure/72-security.md)承载相关原则，本次不以主题相同宣称这些新版本细节“已有覆盖”；亦不把暂未列入书的配置当待办。

### [Olmo-core v3.0.0](https://github.com/allenai/Olmo-core/releases/tag/v3.0.0)

采用官方31项release元数据中唯一窗内 `published_at=2026-10-01T15:17:49Z`；完整具名说明在[OLMO_RELEASES](../_sources/2026-W40/OLMO_RELEASES.json)。该release与Oct1不带原时区的blog、技术报告首公开事件区分：本次有定时的发布事件可以采用其明确描述的纠错，但不反推论文Submitted或blog首次公开时刻。核心采用release具名PR843纠错说明；不声称取得PR843最终代码核验，不把PR提交日期改成本周首公开研究。

每个document保留EOS时，扫描token array是合理旧边界源；producer truncate丢终止符后合并下一文档，LongDocStrategy.truncate再保留合并head就使下一文档消失。新显式source metadata路径保留旧默认，mask document lengths必须与packing权威源一致；same-size sidecar修正也要改变dataset fingerprint/packing cache身份并核BOS/EOS padding。单SFT cache的97.98%→100%有效token只说明这种输入失效，不证明全语料损失率或训练质量。v3 DDP等其他增量只在release支持范围内描述，不以blog random routing perf提升证明训练质量，报告中的gerrymandering/overlap结果不作本周正面新机制。

[Ch27 tokenizer切分与packing](../../../../books/part-04-training-system/27-data.md#tokenizer切分与-packing-的边界)780–782行两段补边界权威源和sidecar失效责任；不是再写packing概论。hashing、元数据/重pack有成本，terminator完整时旧扫描共存，来源/语义不明则隔离重建或停止。root实际POST通过，仅在release说明证据边界采用。

### [METR per-action monitor](https://metr.org/notes/2026-09-27-implementing-a-basic-blocking-action-monitor/)

原metadata `datePublished=2026-09-27T00:00:00-07:00`保留PDT日精度，不虚构文章午夜精确发布；对应整天BJT范围[Sep27 15:00,Sep28 15:00)完全落周窗。采用[完整必要core](../_sources/2026-W40/RAW_METR2.md)正文四条件与failure讨论：policy覆盖、危险动作可见、judge合格、阻断且可信人审同时成立，不是四个默认独立概率。真实部署曾忘开monitor、旧Inspect子agent动作不可见、image缺席；本研究并未使用provider-executed tools，不能跨界保证。Refusal/error fail-closed是实现路径，不能替人类身份验证。

关键反例是coding agent自行打开review面板并发按键；作者尚未强制human reviewer身份。平均动作误报掩盖长轨迹聚集，reviewer fatigue/可靠性未测。10条恶意transcripts被flag不证明每次有害动作前阻断，13条synthetic动作不是on-policy开放安全，文本spoof有限试验不是生产攻击率。成本只限作者preliminary配置，不外推所有agent；未运行其monitor。

[Ch72 approval summary](../../../../books/part-06-ai-infrastructure/72-security.md#approval-summary-必须由待执行-effect-反向渲染)3031–3033行补“忠实审批view≠可信批准principal”，把credential/输入通道与被审Agent capability隔离、批准绑定具体对象，并保留delay/reviewer-capacity与fail-closed代价。原consent-integrity承载审批内容一致，不承载谁真的批准；root原源/正文邻接POST通过。Ch66负责评价证据，不复制四条件成安全乘法公式。

### [GLM-5.3 cyber assessment](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities)

这是09/30 Daily具名日期缺口的定点补查，不重扫Anthropic。原metadata首次公开 `2026-09-29T15:46:00Z` 与修改Sep30 08:46Z分开，恢复后确定归本周、不直接改该日报。采用[96行原源核心与footnote](../_sources/2026-W40/RAW_GLM_CYBER.md)。ExploitBench41漏洞×10=410尝试中GLM50个端到端成功、Mythos56；另一binary评估random100任务4%/6%，两者是不同真实offline sandbox执行，不能合并分母或声称现实部署被入侵。人类辅助Linux0day/ARM64Ndayworkflow也不是本项目攻击复现。

safeguard行为臂的fake bash不运行code或外部副作用；每cell50样本来自5指令序列×2目标×5尝试，0/64/92/100%是尝试连接的engagement，不是exploit成功率。能力臂禁用safeguards与行为臂gated API不同；prefill/weight editing对某API不可达时padlock不是尝试失败。abliteration有限GPU预算与generic HarmBench refusal不能变为普适低成本攻击或cyber能力保证。

仅报告：具名模型、有限威胁/工具权限/成本事实，不形成新普遍安全保证；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)1090–1095行现有能力、elicitation、机会/授权和后果分账可路由概念，但不据此宣称当前数字已在Books。root实际读完整核心/footnote并FIRST通过，3+2+2=7，未改其他日文件。

### 跨日关系一：计算复用需要“行为、表示与寿命”三层验收

09/28的[Evaluating KV reuse](https://arxiv.org/abs/2609.31415v1)要求paired full-prefill分母与warmup/query角色，10/01的[Prefix-invariant Fast Matrix Multiplication](https://arxiv.org/abs/2609.39816v1)区分batch确定性与prefix不受未来影响；Transformers配对cache/recompute tests承接精确实现层，FlashInfer prepared graph与SGLang refit承接descriptor/weight representation寿命层。它们共享验收压力而不是同一算法：近似质量证据不能证明精确mask正确，launch/reference正确也不能证明后续capture仍持有效metadata。owner仍为Ch45的cache语义与Ch49的执行plan/数值合同，失败分别回到full prefill或已验收plan。

### 跨日关系二：输入/运行身份必须绑定“真正被消费的对象”

09/28的[Weight Pair Encoding](https://arxiv.org/abs/2609.31564v1)区分weight code-domain与kernel消费，Olmo-core说明token文件存在不等实际文档进入instances，PyTorch component纠错说明source合法不等artifact执行忠实，SGLang说明checkpoint与packed-kernel format不同。跨日归纳不是新一套lineage框架：Ch27只拥有数据边界与有效输入，Ch49只拥有表示转换/执行回归；三处都保留额外identity、重建与验证成本，不用“shape一致”替具体等价。

### 跨日关系三：检测、能力与批准不能替代实际效果

09/28的[Beyond Approved Actions](https://arxiv.org/abs/2609.31301v1)要求批准对象与持久effect分权，10/04的MiMo-Code要求prepare/publish及owner生命周期，METR真实self-approval说明审批view正确仍缺独立principal，GLM把sandbox效果与fake-bash意愿及不可达权限分开。CodeJudge争议也保留为判据充分性未得证的反侧。Ch84负责执行对象与提交，Ch72负责批准authority，Ch66负责评价口径，不能把这些局部控制汇合成开放安全证书。

## 5. 缺口与下一步

本周普通待办0，177家族均有最终处置，成稿及实际写后复核完成，不保留未读release库存。以下是穷尽当前有限入口后的本窗终态保留项，不支持候选正面证据、Books或“无遗漏”；条件恢复只重开受影响项，不重跑七Daily。

- **P1 Physical Intelligence**：主页/blog/research 403、两host直取429及一次限定官方域September2026补检未恢复。需本窗原始公开目录和正文/日期；可接受官方RSS、带发布日期的论文/报告原件。恢复时从SRC-PHYSICAL-INTELLIGENCE本窗入口定点重开，不称本周零进展。
- **A1 Ai2 Papers**：可见首10只有年标2026，不能定周；Latest日期prefix可读，但不能替这个不透明目录。需官方逐项带时区首公开字段或可排序本窗列表；恢复只核其相关周条目。**Olmo blog/report**另需原发布日期时区或同精确artifact首公开证明；现有v3 release只证明本周release事件，不用于将未知报告/博客日期回填。
- **P2 Prime Inference**：[Re-architecting inference](https://www.primeintellect.ai/blog/prime-inference)已读必要core，但Oct2原字段仅日无原时区；不得假定UTC/BJT。storage量化容量与native kernel、社区已有block-major方案、不同blocksize/TP-DCP workload需分开；原字段恢复后只重开该项，当前不记确定候选或正面Books。
- **E1 EverMind**：无日期活动/landing缺少首公开，已确认Jan/Apr老论文不入本窗。可接受官方精确事件metadata/报告版本记录；定点重开活动身份，不沿旧论文重新评分。
- **Daily继承限制**：七份Daily §5的原身份、恢复条件与停止范围继续生效，尤其Sonnet5.5、GPT6.1Sol、MiMo Sep27 repetition/CLI0.5.8首公开原时区，CDB/TeDiServe具体v2重要修订与公告归属；Google/Meta/Qwen/Moonshot/Hunyuan/ZAI/MiMo/arXiv Oct2具体目录失败见相应日报，不把某日恢复入口视为全周恢复。10/04 G1–G8仍按其组目录/日级归属隔离。GLM cyber这一个日期请求已恢复，其余没有用修改时间/repo创建时间代替发布。
- **CodeJudge arXiv2609.30328v1**：日报§4保留中心充分性争议，暂缓，不将局部empirical score证明candidate审计充分。需要明确新增假设/独立判错条件及可检查的中心证明或修订；这是证据争议终态，不是网站访问外阻。

明确排除项只保留筛选记录，不为不影响处置的日期另建请求：Mistral Munich组织算力愿景、WorldLabs AMD同事件组织公告、SAIL旧论文传播、Extropic既有GRPO应用、AstaBrief受限citation filtering/旧baseline与有限人评、METR证词旧调查传播。AstaBrief实际题摘与核心均核，不靠机构/时间先验关闭；其增加citation density与单pass配置、14问题人评不证明当前前沿通用进步或faithfulness。无本周之外待办被扩入本报告。

## 6. 复核

复核者：root（独立于周报作者w40_weekly）。

结论：通过

本窗可执行工作闭环；下列外部覆盖限制及CodeJudge中心争议仍隔离，不是全面Evidence通过。

已完成的独立检查：root实际定点读首批release/blog/METR核心并校准8家族准入；GLM日期恢复后另读96行完整核心/footnote，FIRST通过。METR四合取/人审身份、Olmo随机route系统perf与训练质量/首公开归属、Prime容量/native kernel/community lineage、SGLang ABORT/DMA/commit、Transformers cache测试不发明KV理论均作具体边界校正。高风险纠错核心5350/40777/48289与Olmo官方release metadata/具名说明已独核；不是对release所有PR的全量代码审计。

Books实际六处新增（Ch49 compiler artifact88–90、prepared metadata131、refit194–196；Ch45 paired cache37–39；Ch27 EOS/sidecar780–782；Ch72 principal3031–3033）及相邻正文已root实际POST通过。七日报独立结果按各自§6复用，10/04的完整写后总Gate已完成；每日日级外部终态保留不被抹除。周新增7家族与日期恢复GLM合8，未变化Daily168完成/1争议的exact事件和Books决定依研究合同§7复用，不宣称周作者无差别重读所有附件。

最终非作者检查已实际通读六部分，核29周源及14日源复用的有限入口/查询和停止位置、七默认窗口连续覆盖、170行归并169家族与新增8家族、全部177项处置及三条跨日关系。负侧分层抽检6项：Munich组织公告、WorldLabs/AMD同事件、SAIL传播与版本、Extropic既有训练配方、AstaBrief引用评价/过滤反侧、METR证词与旧调查归属；具名纠错/安全采用边界同时复核。未变化Daily的原审阅与写后结果按身份/版本/命题复用，未对177家族的全部附件第二次全文审阅，未复现任何实验。格式通过不替代以上实际语义检查。

机器校验：2026-10-05成稿 `python3 scripts/validate_research.py --report papers/2026/weekly/2026-W40/README.md` 通过（1份V3）；177个候选链接小标题与表逐项匹配，本报告本地引用目标存在检查无缺失，本次目标路径 `git diff --check` 通过。机器检查不替代周级最终语义复核。未stage、commit、push，未改其他Daily/Weekly或共享索引；没有运行GPU、安装release包、复现实验或证明生产性能/安全。
