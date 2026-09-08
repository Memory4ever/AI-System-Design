# Daily Research — 2026-09-03

**规范：** V3
**窗口：** 2026-09-02T09:00:00+08:00 ～ 2026-09-03T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T14:20:00+08:00

## 1. 结论

本轮按用户已认可的初筛预览生成正式报告。独立逐项题摘审阅从排除侧恢复01615、02264、02866；01746、01768保留为具体争议而非“无贡献”。02293已从精确HTML恢复完整摘要，01821已核实prefill收益与decode拥塞的反向关系。02652经独立核实于Aug27由Zenodo公开，移出本窗。当前50个arXiv家族及4个机构家族共54项，均已完成采用范围的审阅与独立核对；47项有限命题已落实Books判断，7项中心结论因证据争议而暂缓。普通审阅与书稿工作已结束；争议及来源日期限制已隔离，不用于正面结论或Books，材料到达时只定点重开。54项不等于54项新增长期知识。

原始缓存 875 个去重身份包含窗外、修订与交叉分类；本日首次公告身份核对集合为 531。旧 336 等候选口径已停止沿用；本轮改写前报告及原始审阅保留，用于核实精确版本、采用命题与旧争议，不能借旧完成标签通过本轮验收。不重跑宽池、不按篇数配额、不为普通修订比较旧新全文。

本轮新增Books落点为Ch77的memory baseline/净害分层、Ch49的加密执行离线近似预算，以及Ch17的传输谱上下界与差异保持。三处均已完成独立来源及写后复核；其余已有覆盖或既有整合按实际正文核实，不为新论文强行追加段落。

当前三维评分针对表中具体命题，不沿用旧评分。标准项仍须核实关键机制和评价；安全、纠错或已确认 Books 缺口即使不足 7 分，也深入审阅相关内容。准备好的单篇先推进，不等待其他材料。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 复用本窗官方事件，机构初筛见机构记录 | 已检查 | 本窗Astra已并入；版本声明不等于机制验证 |
| SRC-ANTHROPIC | 既存官方 Research 本窗核查，见旧来源原始依据 | 已检查 | 无新增本窗线索 |
| SRC-GOOGLE-AI | Gemini/Fairwind 本窗事件及定点记录 | 受阻 | 两项相关目录材料缺首次公开日期，不借全年目录计作当日论文 |
| SRC-META-AI | 复用本窗定点核查，依据 | 已检查 | 无确认本窗新事件 |
| SRC-QWEN | 英中官方目录及 Drive 博客，机构记录 | 已检查 | Drive 已由Sep02 arXiv:2609.00111首次公告，不在本日重复计分 |
| SRC-DEEPSEEK | 官方 News 及补充列表本窗核查，依据 | 已检查 | 无确认本窗新事件 |
| SRC-MOONSHOT | 官方本窗 release，机构记录 | 已检查 | Kimi Code固定commit采用命题已完成，非交互模式不注册guard |
| SRC-TENCENT-HUNYUAN | Research 下方“全部”截图仅已显示 9 行，最上方 Aug28；共同记录 | 受阻 | 完整目录入口与具体论文链接仍待可访问材料，不把空提取当无更新 |
| SRC-ZAI | 官方 Research 目录，共同记录 | 已检查 | 所取目录未命中本窗，不宣称全站无遗漏 |
| SRC-BYTEDANCE-SEED | 官方研究及论文目录，共同记录 | 已检查 | 所取目录未命中本窗 |
| SRC-BAIDU-ERNIE | 官方博客及论文入口，共同记录 | 已检查 | 所取目录未命中本窗 |
| SRC-XIAOMI-MIMO | 官方Paper/Blog及publisher route/frontmatter已定点恢复，共同记录 | 已检查 | 所取blog为窗外；本窗MiMo Code v0.1.14另作机构候选 |
| SRC-MINIMAX | 官方llms.txt与techblog索引、changelog，共同记录 | 已检查 | 所取Agent Team为May13、最新changelog为Aug27，无确认本窗新事件 |
| SRC-ARXIV | 复用四主类及已有邻类相关标题缓存，531 首次公告身份；逐项初筛理由、公告归属 | 已检查 | 50项本窗家族已独立准入；更早公开02652单列去重，不代表全学科召回 |

本轮只处理每日来源及已发生的相关触发，不扫描每周来源。arXiv 表中时间是官方公告时制与本日 primary-new 列表的组合推定：20:00 EDT 对应北京时间 08:00；RSS 午夜 pubDate 是批次标签，不是实际公开时刻。精确版本和当前撤回检查逐项核实，不能以 submitted 时间替代公开时间。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Safety overview: GPT-6 Astra](https://openai.com/index/safety-overview-gpt-6-astra/) | 2026-09-03T08:00:00+08:00 | 对齐/鲁棒性与CoT可监控性须分别评价；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Gemini 3.8 Flash / Flash Cyber + Fairwind](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) | 2026-09-02T23:00:00+08:00 | 同family公开/受限版本的部署访问合同不同，Fairwind于23:40配套公布；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Kimi Code 0.40.0](https://github.com/MoonshotAI/kimi-code/releases/tag/@moonshot-ai/kimi-code@0.40.0) | 2026-09-02T13:59:00+08:00 | 危险命令guard的host/tool/config覆盖边界决定实际保护范围；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [MiMo Code v0.1.14](https://github.com/XiaomiMiMo/MiMo-Code/releases/tag/v0.1.14) | 2026-09-02T16:53:47+08:00 | 工具副作用后的自动重试、continuation与revision边界分离；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models](https://arxiv.org/abs/2609.01611v1) | 2026-09-03T08:00:00+08:00 | 部署转录的生成器身份会改变检测评价，应将生成器与被测模型校准分开；2 + 2 + 3 = 7 | 争议 | 暂缓 — `PLATFORM-EVALUATION-SYSTEM`；生成器校正、标签及probe预算待作者澄清 |
| [NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference](https://arxiv.org/abs/2609.01657v1) | 2026-09-03T08:00:00+08:00 | 生成式 VLM 改造检索与原生双向多模态编码器形成不同计算路径；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [How Fast Do Agents Rot? An Empirical Study of Long-Horizon Degradation in LLM Agents for Production Decision-Making](https://arxiv.org/abs/2609.01660v1) | 2026-09-03T08:00:00+08:00 | 控制上下文长度后考察步骤数导致的长程失效，区分 context 压力与执行深度；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Not All Agreement Counts as Corroboration: Provenance-Conserving Multi-View Fusion for Typed Action Admission in Human-Robot Collaboration](https://arxiv.org/abs/2609.01662v1) | 2026-09-03T08:00:00+08:00 | 将共享祖先证据与独立观测分开聚合，防止团队重复证据被当作独立支持；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Context Inference Attacks Without Jailbreaks](https://arxiv.org/abs/2609.01663v1) | 2026-09-03T08:00:00+08:00 | 不依赖越狱或逐字提取也可由正常任务推断私有上下文；3 + 2 + 3 = 8 | 深入完成 | 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Learning Evidence Sufficiency Boundaries for Selective Answering in Grounded Multi-Hop QA](https://arxiv.org/abs/2609.01687v1) | 2026-09-03T08:00:00+08:00 | 测量证据增加时何时应从拒答转向回答，而非只测最终正确率；2 + 2 + 3 = 7 | 深入完成 | 整合 — `TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Hearing the Whispers: Black-Box Membership Inference Attacks on Finetuned TTS Models](https://arxiv.org/abs/2609.01723v1) | 2026-09-03T08:00:00+08:00 | 区分语音模型的说话者级与录音级成员泄漏，超出文本复述指标；2 + 1 + 2 = 5 | 争议 | 暂缓 — `PLATFORM-SECURITY`；DP保护单位与会计参数未披露 |
| [HEAT: Faster Fully Homomorphic Inference via Approximations-Weights Co-Adaptation](https://arxiv.org/abs/2609.01730v1) | 2026-09-03T08:00:00+08:00 | FHE 约束下按位置学习非线性迭代预算并与权重联合适配；2 + 2 + 2 = 6 | 深入完成 | 整合 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [hLLM: Single Pass Decoding for Generative Reranking](https://arxiv.org/abs/2609.01807v1) | 2026-09-03T08:00:00+08:00 | 已知候选排列任务可由并行打分与约束匹配替代串行生成；2 + 1 + 2 = 5 | 争议 | 暂缓 — `MODEL-DECODER-ONLY`；Table3比较方向与capacity归因冲突 |
| [Scaling Inference Prefill with High-Radix Photonic Interconnects](https://arxiv.org/abs/2609.01821v1) | 2026-09-03T08:00:00+08:00 | 光子 MoE prefill 的通信与 pod 边界，题摘要报为仿真路线；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Agent Memory Is a Surface for Endogenous Authorization Laundering](https://arxiv.org/abs/2609.01836v1) | 2026-09-03T08:00:00+08:00 | 记忆写入器自己生成的授权陈述被执行器当权限，非外部注入也可失守；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [The Memory Trust Gap: Capability-Dependent Failures in Persistent-Memory Agents](https://arxiv.org/abs/2609.01852v1) | 2026-09-03T08:00:00+08:00 | 新旧权限信息写入记忆不等于模型执行正确，需要外部预解析边界；2 + 2 + 3 = 7 | 深入完成 | 整合 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [CREDIT: Cost-guided Reduction-reuse with Efficient DSMEM Inter-CTA Tiling](https://arxiv.org/abs/2609.01864v1) | 2026-09-03T08:00:00+08:00 | DSMEM 收益取决于复用、同步和资源占用成本，而非可用就更快；2 + 1 + 2 = 5 | 深入完成 | 整合 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding Retrieval](https://arxiv.org/abs/2609.01865v1) | 2026-09-03T08:00:00+08:00 | 相似代码检索可能召回执行语义相反的近克隆，检索相似性不等于可用证据；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Epistemic Sybil Resistance: Multiplying AI Agents Without Multiplying Evidence](https://arxiv.org/abs/2609.01873v1) | 2026-09-03T08:00:00+08:00 | 仅看报告内容可能无法识别同源证据，限制多代理证据融合的可信度；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?](https://arxiv.org/abs/2609.01924v1) | 2026-09-03T08:00:00+08:00 | 循环 Transformer 的状态传播与重构通过干预区分；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated Routing](https://arxiv.org/abs/2609.01925v1) | 2026-09-03T08:00:00+08:00 | Prefill 根据输入注意力结构选择稀疏模式，避免累计覆盖阈值随上下文增长吸收背景噪声；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `INFER-PREFILL` [Ch43](../../../../books/part-05-inference-system/43-prefill.md) |
| [Sparse Readout Prism: Explaining Logit-Lens Scores in Features Instead of Tokens](https://arxiv.org/abs/2609.01936v1) | 2026-09-03T08:00:00+08:00 | 探针自身数据先验可能改写隐藏状态的解释，应区分读出与模型原机制；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [RT-HiSS: Ray Tracing Accelerated High Dimensional Vector Similarity Searches](https://arxiv.org/abs/2609.01975v1) | 2026-09-03T08:00:00+08:00 | 利用 RT core 做高维搜索并由 CUDA 精化，改变向量搜索的执行位置；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Train What You Deploy: Closing the MLP Reachability Gap in Low-Rank Clone Distillation](https://arxiv.org/abs/2609.02006v1) | 2026-09-03T08:00:00+08:00 | 训练时压缩子空间可能令部署矩阵的容量不可达；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Multi-Turn LLM Conversations under the Least-Recently-Used Policy: Mean-Field Asymptotics and Hit Ratio Approximation](https://arxiv.org/abs/2609.02027v1) | 2026-09-03T08:00:00+08:00 | 会话增长改变 LRU 命中过程，容量估计不能直接套静态对象模型；2 + 1 + 3 = 6 | 深入完成 | 整合 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [A Unified Rate-Distortion Perspective on Vector, Product, and Scalar Quantization](https://arxiv.org/abs/2609.02107v1) | 2026-09-03T08:00:00+08:00 | 量化码本利用率、率失真与梯度传递共同决定视觉 token 方案排序；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [MeanField Surrogate Modeling for Scalable Runtime Scheduling of Concurrent Heterogeneous AI Inference on Shared GPUs](https://arxiv.org/abs/2609.02109v1) | 2026-09-03T08:00:00+08:00 | 共享 GPU 的联合配置搜索以局部模型与聚合占用近似降低 profiling 成本；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [A Power Law in Logarithm's Clothing: On the Scalability of Graph-Based Vector Search](https://arxiv.org/abs/2609.02143v1) | 2026-09-03T08:00:00+08:00 | 高维图索引的规模增长可能触发非多对数成本，改变容量规划假设；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [PGPO: Potential-Guided Policy Optimization for Multi-Turn Agentic Tasks](https://arxiv.org/abs/2609.02236v1) | 2026-09-03T08:00:00+08:00 | 稀疏终局奖励由跨 rollout 的状态势差做细粒度信用分配；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Entangled Representations Amplify Collateral Damage in Unlearning](https://arxiv.org/abs/2609.02285v1) | 2026-09-03T08:00:00+08:00 | 控制表征纠缠程度后测试遗忘与保留损失，区分拒答与知识删除；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Evidence for Shared Routing Geometry and Dynamics in Sparse Mixture-of-Experts](https://arxiv.org/abs/2609.02404v1) | 2026-09-03T08:00:00+08:00 | 专家共享结构与路由专门化的关系由对齐子空间分析；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) |
| [Coverage, Not Targeting: A Structural Regime in Multi-Turn Agent Credit Assignment](https://arxiv.org/abs/2609.02417v1) | 2026-09-03T08:00:00+08:00 | 稀疏 verifier 下信用分配需和随机集中预算对照，不能把集中收益当定位能力；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [When Decodability Is Not Enough: Logical Validity Representations, Behavioral Dissociation, and Causal Tests in Language Models](https://arxiv.org/abs/2609.02438v1) | 2026-09-03T08:00:00+08:00 | 隐藏状态可解码有效性不等于生成决策使用了该信息；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [AceSpec: An Asymmetric Edge-Cloud Collaborative Framework for Communication-Efficient LLM Inference](https://arxiv.org/abs/2609.02514v1) | 2026-09-03T08:00:00+08:00 | WAN 下利用不对称传输和状态缓存处理推测回滚；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [oHC: Orthogonal Hyper-Connections on SO(4) via Quaternions](https://arxiv.org/abs/2609.02672v1) | 2026-09-03T08:00:00+08:00 | 多流残差需分开传输范数上下界与流间差异，正交不保证二者共同不变；2 + 1 + 2 = 5 | 深入完成 | 整合 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [Momentum in large-batch training: Polyak enlarges the critical batch size, Nesterov improves data efficiency](https://arxiv.org/abs/2609.02728v1) | 2026-09-03T08:00:00+08:00 | 核回归模型区分 Polyak 的临界 batch 扩展与 Nesterov 的降噪机制；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [LoRA-TSD: Tangent-Space Spectral Descent for LoRA via Muon-Style Updates](https://arxiv.org/abs/2609.02734v1) | 2026-09-03T08:00:00+08:00 | 在诱导权重的切空间而非独立低秩因子中更新，改变优化几何；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Language Models Can Control Their Own Attention](https://arxiv.org/abs/2609.02737v1) | 2026-09-03T08:00:00+08:00 | 模型声明逻辑注意力读集合，由runtime切换可见block；不等于物理驱逐；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding](https://arxiv.org/abs/2609.02780v1) | 2026-09-03T08:00:00+08:00 | 视频历史保留浅层索引，仅按查询重建深层特征；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-PREFILL` [Ch43](../../../../books/part-05-inference-system/43-prefill.md) |
| [UE5M3 FP4 Block Scaling for Stable Language Model Pretraining](https://arxiv.org/abs/2609.02846v1) | 2026-09-03T08:00:00+08:00 | FP4 scale 格式可能改变变换与高精度回退需求；2 + 2 + 3 = 7 | 深入完成 | 整合 — `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Graph Machine: Towards Better Pretraining via Edges](https://arxiv.org/abs/2609.02881v1) | 2026-09-03T08:00:00+08:00 | 动态稀疏指针状态在固定状态与密集注意力之间提供另一计算结构；2 + 2 + 3 = 7 | 深入完成 | 整合 — `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885v1) | 2026-09-03T08:00:00+08:00 | 世界模型训练目标从重建观测转向区分行动结果；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [World-Coherent Decoding: Self-Verifying Test-Time Planning for World Action Models](https://arxiv.org/abs/2609.02159v1) | 2026-09-03T08:00:00+08:00 | 想象轨迹的内在误差信号与真实观测失配共同控制推演预算；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Towards Zero-Shot Transfer Across Embodiments For Driving VLAs](https://arxiv.org/abs/2609.02341v1) | 2026-09-03T08:00:00+08:00 | 多样数据增加时 BEV 辅助结构收益变化，区分架构先验与数据覆盖；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [ZETA: A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop Manipulation](https://arxiv.org/abs/2609.02546v1) | 2026-09-03T08:00:00+08:00 | 严格未见 embodiment 与少量暴露产生不同迁移判断；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [ACLE-MCP: Attested Capability Leases for Execution-Time Trust in Remote LLM Tool Use](https://arxiv.org/abs/2609.02690v1) | 2026-09-03T08:00:00+08:00 | 端点 OAuth 授权与实际工作负载、参数、证明新鲜度之间建立调用绑定；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖 — `AGENT-MCP` [Ch83](../../../../books/part-07-agent/83-mcp.md) |
| [VibeVoice-ASR-Streaming Technical Report](https://arxiv.org/abs/2609.02812v1) | 2026-09-03T08:00:00+08:00 | 流式 ASR 与说话者分离在共享 token 流中协调 lookahead；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](https://arxiv.org/abs/2609.02886v1) | 2026-09-03T08:00:00+08:00 | 相机条件视频生成与训练/推理历史分布对齐，不等于通用物理行动模型；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Prompt-Space Meta-Learning Does Not Transfer Across Users: A Frozen-LLM Negative Result](https://arxiv.org/abs/2609.01615v1) | 2026-09-03T08:00:00+08:00 | wrong-support与seed对照分离跨用户适应和通用prompt优化；2 + 1 + 3 = 6 | 争议 | 暂缓 — `AGENT-PROMPT`；有限对照原则已有覆盖，family争议未澄清，不新写Books |
| [CAT-Flow: Curvature-Adaptive sTeps for Flow Matching](https://arxiv.org/abs/2609.01746v1) | 2026-09-03T08:00:00+08:00 | 复用已发生vector-field评估自适应步长，但更新符号及EMA方差身份冲突；2 + 1 + 2 = 5 | 争议 | 暂缓 — `MULTIMODAL-GENERATIVE-PARADIGMS`；须作者方法勘误 |
| [Emergence of Fibrations, Compression, and Symmetry Breaking in Artificial Neural Networks](https://arxiv.org/abs/2609.01768v1) | 2026-09-03T08:00:00+08:00 | 计算等价压缩与近似聚类边界重要，但归组/偏置公式/逆命题条件冲突；2 + 1 + 3 = 6 | 争议 | 暂缓 — `TRAIN-PRETRAINING`；须作者精确公式与条件 |
| [Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems](https://arxiv.org/abs/2609.02264v1) | 2026-09-03T08:00:00+08:00 | 同profile打分器可能无法识别adjacency，edge数不能替代真实token成本；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment](https://arxiv.org/abs/2609.02293v1) | 2026-09-03T08:00:00+08:00 | shared expert提供每token必经防御位置，与router hardening的组合证据需核；2 + 2 + 3 = 7 | 争议 | 暂缓 — `PLATFORM-SECURITY`；projection mask维度和组合声明冲突，见§5 |
| [When Does Authorization End? Effect Closure at Provider Boundaries](https://arxiv.org/abs/2609.02866v1) | 2026-09-03T08:00:00+08:00 | 停止新授权与在途旧授权无法产生副作用是不同完成条件；3 + 2 + 3 = 8 | 深入完成 | 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |

## 4. 证据与知识整合

### [Safety overview: GPT-6 Astra](https://openai.com/index/safety-overview-gpt-6-astra/)

只采用官方overview第1—7项的声明边界：对齐/鲁棒性、CoT monitorability与outcome安全不是同一指标，未披露完整实验合同不补算性能。Ch72“CoT Monitor是Policy-bound Sensor”及相邻runtime状态已承载，NoChange；不把未见隐写写成不存在。 详见机构证据与具体Books段落、本轮独立采用命题复核。

### [Gemini 3.8 Flash / Flash Cyber + Fairwind](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)

固定当前release/Fairwind公布范围，仅采用版本访问与缓解策略不同。companion card的后续读取不证明本窗发布时间，未匹配harness的指标不采用。Ch72“Deployment-context Residual Risk Loop”已有checkpoint/controls/残余风险责任链，NoChange。 详见机构证据与具体Books段落、本轮独立采用命题复核。

### [Kimi Code 0.40.0](https://github.com/MoonshotAI/kimi-code/releases/tag/@moonshot-ai/kimi-code@0.40.0)

实读commit 4b9888b中dangerous-command-ask.ts和permissionPolicyService.ts完整核心文件：guard在普通Auto/YOLO批准前，但nonInteractive不注册、config可关闭、仅Bash及有界AST；undefined不是安全证明。Ch84 Policy owner与Ch72 effect-time approval已有覆盖，NoChange；不是完整运行沙箱验证。 详见机构证据与具体Books段落、本轮独立采用命题复核。

### [MiMo Code v0.1.14](https://github.com/XiaomiMiMo/MiMo-Code/releases/tag/v0.1.14)

复用同exact head 2a0eb706的有效独立源码证据；工具调用后禁自动重试不保证exactly-once，202接受非恢复完成，advance expected revision不自动使rotate成为CAS。重读Ch84 Resume、Ch78幂等与Ch81联合恢复后NoChange，不声称全并发机制已验证。 详见机构证据与具体Books段落、本轮独立采用命题复核。


以下记录围绕初筛提出的具体命题完成作者核实，当前新增采用范围的独立验收另见末节。原始独立审阅可复用的部分见既有独立审阅，但原313/336项准入口径不继承；只有实际证据位置与当前命题一致的单篇结果才回填。初筛表的建议 owner 在读 Books 后细化，不能用主题相似代替已有覆盖。

### [How Fast Do Agents Rot? An Empirical Study of Long-Horizon Degradation in LLM Agents for Production Decision-Making](https://arxiv.org/abs/2609.01660v1)

复用实际 PDF 与实现审阅及独立正文复核。自然、压缩、填充上下文确实形成不同长程表现，但同时改变历史、反馈或调用结构，不能只归因于步骤数量；最终任务允许后来修复，边际步骤正确率不是吸收式 survival hazard。论文 28/36 geometric-fit 与公开分析27/36、paired estimator 的实现差异保留，相关数字不采用。采用的窄结论是评估必须区分执行深度、可用历史与恢复机会，不主张普适几何退化定律。

Books 实读 Ch66“从 Final Pass 扩展到 Trajectory、Cycle 与 Checkpoint Decision”及其前后 System/Runtime Evaluation，还有“single snapshot → evolving state sequence”段，已明确中间失败、恢复成本不能由最终pass覆盖。因此**已有覆盖**，不向 Ch81 重复追加一条未经因果识别的规律。

### [Not All Agreement Counts as Corroboration: Provenance-Conserving Multi-View Fusion for Typed Action Admission in Human-Robot Collaboration](https://arxiv.org/abs/2609.01662v1)

复用精确正文、公式与有限 artifact 审阅及同一独立复核。采用的是外部给定 provenance partition 下，同component取逐坐标meet、跨component累计budget；missing member可能令整组支持归零，false split则虚增支持。分区真实性、可加单位和阈值都不是模型从意见文本自动证明的，hold/confirm/fallback也不是物理安全证书。旧实现路径及触发阈值争议不被抹去，不采用其未核实端到端保证。

Books 实读 Ch82“Verification 与 Aggregation / 同根报告可以帮助读懂证据，却不能按独立观察累加”，并对读 Ch72“Memory Origin Confusion”。现有正文已区分原始证据误差与提取误差、允许重复提取带来的有限信息增益并要求lineage collapse；该外生分区的保守实例不改变此核心判断，故**已有覆盖**，不是“重复Agent永远没有价值”。

### [Context Inference Attacks Without Jailbreaks](https://arxiv.org/abs/2609.01663v1)

复用精确证据与独立审阅；本轮重新打开对应HTML确认可取，并顺读当前 Ch72 已整合段。实验固定候选记录并强制检索，普通回答分布可带出记录存在性；grey-box目标打分与surrogate黑盒不是同一访问合同。未证明开放自主检索、未知秘密恢复或所有提供商通用攻击率，数据过滤/概率重归一化争议也不能用headline ASR掩盖。

原写入仍位于 Ch72“Hidden Reasoning Trace 不是 Secrecy Boundary”之后、authority BOM之前，明确“不包含原文”不能作为保密保证，并保留forced-retrieval与surrogate限制。**既有整合已核实，无需重复写入**；采用机制而非攻击率。

### [UE5M3 FP4 Block Scaling for Stable Language Model Pretraining](https://arxiv.org/abs/2609.02846v1)

复用原正文/写后复核中本ID的§4、§5、§7及独立结果。本轮重开 exact HTML。非负scale可借未用signbit扩exponent范围；sample-and-hold、二维weight scale、仅dY的stochastic rounding是相互约束的recipe，不可推每个tensor都应同样舍入。实验为单seed 8B、188.7B-token的软件UE5M3轨迹；原生Blackwell仍E4M3。联合移除RHT并扩大FP4覆盖的model-body吞吐不是UE5M3端到端加速，故不采用headline数字。

Ch28 scale format/lifecycle/tensor role 段（紧接trajectory invariant，后接coherent mean）仍完整承载该差异和native/BF16 fallback。**既有整合已核实**，未新增性能断言或修改章节。

### [Graph Machine: Towards Better Pretraining via Edges](https://arxiv.org/abs/2609.02881v1)

复用精确v1方法、局部训练与独立写后结果，本轮重新打开正文并顺读 Ch22 对应段落。token除features外携带稀疏indices/weights，两跳referral、coalescing、hard top-s和edge-plus-QK共同决定下一层访问；这是attention连接状态分支，不是替换MLP。596M单seed短文档训练仅支持可训练性，参数额外成本和慢generic-PyTorch原型不支持高效长上下文宣称。

因此将初筛建议 Ch17 细化到实际长期owner `MODEL-LONG-CONTEXT`，沿 Ch22 selector ownership/reuse → address state → position coupling 顺读确认已存在。**既有整合已核实**，保留dense回退，不在Ch17复制同一机制。

### [Learning Evidence Sufficiency Boundaries for Selective Answering in Grounded Multi-Hop QA](https://arxiv.org/abs/2609.01687v1)

复用精确版本方法与结果审阅和独立审阅，本轮顺读Ch29事实知识边界段、证据链新增段及下一节系统位置。四视图把同题的无支持、缺桥接、首次充分、冗余分开；gold-answer-prefix分数只能离线训练，不能成为未知答案的线上真值。首次充分相对于有限构造，不是全局最小证据；score不下降也不保证答案identity不变。Qwen2.5-3B LoRA单训练seed、不同监督视图与解码预算的受限比较，不证明所有回答/拒答指标全面领先。

当前Ch29已把上述关系插在base knowledge boundary之后，并交给Ch76运行时sufficiency gate；因此实际owner细化为`TRAIN-SFT`，**既有整合已核实**。未再向Evaluation追加同一机制。

### [When Does Authorization End? Effect Closure at Provider Boundaries](https://arxiv.org/abs/2609.02866v1)

独立题摘复核纠正了初筛false negative：平台通用授权机制可直接支撑本项目，不要求论文必须写LLM专有实现。复用精确正文§II–V与有限artifact记录及独立来源/写后复核。finite provider contract区分停止新使用、实例/派生链effect closure与全局quiescence，缺效果路径或控制证据时必须no-verdict，不能从局部clean状态签发关闭证明。

本轮实读Ch72 canonical-action receipt→撤权在途路径→Kafka限定案例→异步支付交接，确认原整合真实存在且未外推。Kafka证据限固定broker、同步非事务append、完整mediation；不采纳生产吞吐、任意provider或全局安全保证。**既有整合已核实**。

### [EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models](https://arxiv.org/abs/2609.01611v1)

作者审阅与独立审阅确认校正权重不保证所宣称相对影响上界、任务标签数量冲突，以及exhaustive/greedy probe预算身份不一致。材料可读，但当前校准合同不能支持长期结论；Books暂缓。需要作者公式假设/勘误、真实split标签及scorer/probe配置，而非再下载同一PDF。
### [hLLM: Single Pass Decoding for Generative Reranking](https://arxiv.org/abs/2609.01807v1)

来源审阅及独立记录确认Table3打印比较方向与caption归因相反，且缺click+LoRA完整factorial。并行候选打分→Hungarian匹配的意图可解释，却不足以绕开中心capacity归因争议写入Books。需Table3配置身份/勘误与缺失对照。
### [CAT-Flow: Curvature-Adaptive sTeps for Flow Matching](https://arxiv.org/abs/2609.01746v1)

方法/公式审阅与独立复核确认Euler更新正负号冲突，零初始化EMA不是所称已访问点上的正规概率方差。需作者明确执行公式、初始化/正规化条件及固定实现；不自行修公式后称理论通过。
### [Emergence of Fibrations, Compression, and Symmetry Breaking in Artificial Neural Networks](https://arxiv.org/abs/2609.01768v1)

有限压缩审阅与独立复核保留cosine归组不等于equal-sum、CNN偏置求和不保forward、逆命题缺可达满秩条件。需要作者分组/压缩公式与条件澄清；不把未审SGD/continual-learning全证明称已完成，也不把争议改称无贡献。

### 已有证据与当前Books逐项对照

| 家族 | 实际证据与边界 | 本轮Books对照 |
| --- | --- | --- |
| 01852 Memory Trust Gap | exact-v1与本轮写后记录：旧证据依赖与净损害不同，oracle删去已知stale是输入干预不是可靠resolver；三选一有限场景不证明规模安全规律 | Ch77新增两段已由非作者实际顺读通过，当前整合完成；metadata可改善小模型，不称完全无效 |
| 01864 CREDIT | 论文/有限固定artifact和独立写后：owner-local bulk加compact statistics复制，P增大也增加同步/资源成本；小shape可变慢，traffic下降非E2E收益 | 本轮实读Ch49跨Block共享前后TMA/DeepGEMM，owner/local与P(P−1)远端复制、ROI成本及单CTA回退仍真实存在，既有整合核实 |
| 01865 ExecRetrieval | 精确论文/固定scorer与独立写后：query输入域与test域不同、唯一canonical下exec与hit指标恒等，近克隆构造非自然bug率 | 本轮实读Ch66 reference-first→需求域→指标恒等→proxy段，已有具体论点；owner细化为Evaluation而非在RAG再写一次 |
| 02027 多轮LRU | 精确理论/实验及写后：whole-content/Poisson/指定独立条件下，固有可复用工作量份额与驻留概率分开；partial-block/ref/timestamp不满足通用定理 | 本轮实读Ch54 KV容量后3段及fragmentation交接；无response回写条件、fixed workload解释、Ch45/55/56handoff均在，既有整合核实 |

### [Hearing the Whispers: Black-Box Membership Inference Attacks on Finetuned TTS Models](https://arxiv.org/abs/2609.01723v1)

Deep作者审阅与独立DP合同复核：speaker/utterance邻接单位、δ、noise/clipping/sampling/composition/accountant缺失，使文中正式隐私声明不能由攻击AUC接近chance补足。保留有限攻击解释，但Books暂缓；不声称其未见实现必定不满足DP。

新增定点审阅见机制证据与Books对照。01730 HEAT两段已经非作者写后通过；01873复用原独立理论/写后记录，只采用给定Gaussian/正方差条件下的信息天花板与provenance解释，Figure4/NLL经验争议仍未解决，不能写成经验恢复。

### [Scaling Inference Prefill with High-Radix Photonic Interconnects](https://arxiv.org/abs/2609.01821v1)

服务DES中的prefill变快可能把队列压力转到decode；这是固定72GPU配置的模拟，不是光硬件实测。Ch55已明确两池到达率与端到端账本，NoChange。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Agent Memory Is a Surface for Endogenous Authorization Laundering](https://arxiv.org/abs/2609.01836v1)

writer凭历史生成错误权限与executor传播应分开；oracle log替换是归因不是部署resolver，事件抽取也会漏合法授权。Ch77授权先于ranking、Ch81前驱authority激活已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?](https://arxiv.org/abs/2609.01924v1)

循环层需step-aware hook；输入持续注入使相似状态未必来自持久存储。Ch17 step counter/readout与Ch5受控干预已有覆盖，不从一次patch失败推信息不存在。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Sparse Readout Prism: Explaining Logit-Lens Scores in Features Instead of Tokens](https://arxiv.org/abs/2609.01936v1)

固定hidden state仅替换lens训练分布即可改变读出语言，字典残差仍影响解释。Ch5读出≠使用与probe身份已有覆盖，不追加内部语言结论。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [RT-HiSS: Ray Tracing Accelerated High Dimensional Vector Similarity Searches](https://arxiv.org/abs/2609.01975v1)

RT生成保守三维候选，CUDA验证高维固定半径；不是ANN语义top-k，结果缓冲也限制batch。Ch76 typed retrieval验证/materialization与Ch49buffer成本已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Train What You Deploy: Closing the MLP Reachability Gap in Low-Rank Clone Distillation](https://arxiv.org/abs/2609.02006v1)

固定teacher slice限制训练可达方向，合并部署仍可为完整矩阵。Ch30已分离rank/update空间和部署dense执行成本，NoChange。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [A Unified Rate-Distortion Perspective on Vector, Product, and Scalar Quantization](https://arxiv.org/abs/2609.02107v1)

满codebook利用率不是低distortion；SQ/PQ/VQ最优排序有固定分布/预算条件，不保证训练或kernel排序。Ch23 rate–distortion–prior容量联合选择已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [MeanField Surrogate Modeling for Scalable Runtime Scheduling of Concurrent Heterogeneous AI Inference on Shared GPUs](https://arxiv.org/abs/2609.02109v1)

固定aggregate context的surrogate搜索不预测切换后的GPU状态，经验P25约束也非线上尾SLO。Ch56 profile身份、colocation和运行时gate已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [A Power Law in Logarithm's Clothing: On the Scalability of Graph-Based Vector Search](https://arxiv.org/abs/2609.02143v1)

扩容须固定recall再比较搜索成本；论文距离计算量不是GPU延迟，幂律并非所有ANN普遍定律。Ch76已有metric/workload合同，NoChange。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [PGPO: Potential-Guided Policy Optimization for Multi-Turn Agentic Tasks](https://arxiv.org/abs/2609.02236v1)

同batch相同观测的return均值形成potential，再与step advantage混合；非固定PBRS，不保证policy invariance，aliasing/单例组会失效。Ch33组identity与transition参考已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Entangled Representations Amplify Collateral Damage in Unlearning](https://arxiv.org/abs/2609.02285v1)

matched forget损失下需检查未参与优化的adjacent知识，forget loss不等于不可恢复。Ch72参数擦除/retained切片与Ch5归因已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Evidence for Shared Routing Geometry and Dynamics in Sparse Mixture-of-Experts](https://arxiv.org/abs/2609.02404v1)

对齐低维router动态可预测不等于共享router或跳过执行可行；不采用wall-clock加速。Ch21 router责任与Ch5坐标/干预证据已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Coverage, Not Targeting: A Structural Regime in Multi-Turn Agent Credit Assignment](https://arxiv.org/abs/2609.02417v1)

信用浓度、位置和更新预算须分别控制，首update之后rollout分布会分叉。Ch33已有matched-control归因原则，NoChange，不把uniform升格为唯一正确方案。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [When Decodability Is Not Enough: Logical Validity Representations, Behavioral Dissociation, and Causal Tests in Language Models](https://arxiv.org/abs/2609.02438v1)

有效性probe可解码不保证生成行为使用；有限层/token/方向的null干预不证明其他位置均无信息。Ch5信息存在、可读、使用三层已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [AceSpec: An Asymmetric Edge-Cloud Collaborative Framework for Communication-Efficient LLM Inference](https://arxiv.org/abs/2609.02514v1)

异步分支命中可减重算，miss仍rollback/redraft；压缩draft分布exactness未充分披露，不能保证目标分布完全相同。Ch48 commit frontier与residual核验已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [oHC: Orthogonal Hyper-Connections on SO(4) via Quaternions](https://arxiv.org/abs/2609.02672v1)

σmax≤1只限制不放大，σmin仍可能接近零；正交保所作用子空间欧氏范数，却不保证流间差异不变。Ch17新增一段及notes，来源/写后已独立通过；无通用稳定或速度外推。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立验收已通过。

### [Momentum in large-batch training: Polyak enlarges the critical batch size, Nesterov improves data efficiency](https://arxiv.org/abs/2609.02728v1)

单遍Gaussian线性核回归区分临界batch与数据效率，不外推Adam/非线性LLM。Ch28 batch/token/step/噪声与optimizer recipe已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [LoRA-TSD: Tangent-Space Spectral Descent for LoRA via Muon-Style Updates](https://arxiv.org/abs/2609.02734v1)

切空间更新需对应诱导权重；理论无momentum且需非退化factor，实践momentum/零初始化不自动满足保证。Ch30更新空间与Ch28optimizer状态身份已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Language Models Can Control Their Own Attention](https://arxiv.org/abs/2609.02737v1)

模型标签决定逻辑read set，runtime改可见页表；保留物理KV且可恢复global，不是驱逐或信息隔离。Ch45逻辑prompt/驻留页/read set已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885v1)

状态表示区分两个已观测action结果，非穷尽反事实；额外WM rollout增加成本且judge影响排序。Ch25预测表征与真实执行authority已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [World-Coherent Decoding: Self-Verifying Test-Time Planning for World Action Models](https://arxiv.org/abs/2609.02159v1)

用真实被执行观察纠正WAM自洽分数，但未执行候选无真值。Ch25/26反馈已有覆盖；Table3 predictor与headline冲突不采用。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Towards Zero-Shot Transfer Across Embodiments For Driving VLAs](https://arxiv.org/abs/2609.02341v1)

BEV辅助先验收益依数据与camera覆盖，teacher伪标签亦有成本；更多数据后并非所有slice都受益。Ch26 schema/calibration/sim-to-real已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [ZETA: A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop Manipulation](https://arxiv.org/abs/2609.02546v1)

排除目标所有预训练与仅排除目标post-training是不同zero-shot合同；程序化robot变体不等于独立实物种类。Ch26和Ch66暴露身份/物理slice已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [ACLE-MCP: Attested Capability Leases for Execution-Time Trust in Remote LLM Tool Use](https://arxiv.org/abs/2609.02690v1)

capability lease绑定参数、workload和sender依赖不可绕过gate；模拟attestation、执行后consume及单并发不证明生产原子性。Ch83/72执行时授权已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [VibeVoice-ASR-Streaming Technical Report](https://arxiv.org/abs/2609.02812v1)

音频/文本chunk与lookahead共同决定等待和speaker历史；算法C/2等待不等于实测尾延迟，旧文本不回改。Ch23时间/来源身份与Ch42计时已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](https://arxiv.org/abs/2609.02886v1)

canonical corpus、mixing recipe与backbone view分离；自rollout训练缓解历史分布差不证明持续物理世界状态。Ch25视频/状态与rollout限制已有覆盖。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Prompt-Space Meta-Learning Does Not Transfer Across Users: A Frozen-LLM Negative Result](https://arxiv.org/abs/2609.01615v1)

wrong-user/seed负对照可检验适应性，但Eq3/5单item推理不能推出population目标不依赖配对；mutation temperature0与0.9描述冲突，宽区间null不是equivalence或普遍不可能定理。Ch74holdout prompt搜索/Ch66不确定性已覆盖有限对照原则，但family仍为Disputed，不用局部NoChange替代整体争议；不新写Books。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems](https://arxiv.org/abs/2609.02264v1)

同候选集用实测token scorer替代edge proxy具有有限证据；归一化mean/GAT同profile不变不能推广sum聚合，六训练图也不能证明开放空间只需六code。Ch82协调成本已有覆盖；泛化理论保留争议。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment](https://arxiv.org/abs/2609.02293v1)

shared expert必经不等于全局安全；intermediate mask同时右乘gate/up/down ΔW存在维度缺口，组合声明超出§7实验。Books暂缓，需作者公式/layout和组合证据澄清。 精确版本、实际阅读位置与Books对照记录本项采用边界；本轮独立核对结果见当前采用命题复核。

### [NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference](https://arxiv.org/abs/2609.01657v1)

原exact-v1 source及独立Books记录采用native encoder与late-interaction index的压缩/读成本分离。重读Ch76 retrieval度量→chunking→late interaction→reranking，现有计算路径和index materialization足够承载，NoChange，不在Ch23再列一种encoder产品。 具体主源/非作者审阅文件与当前Books段落见有效证据与实际Books记录及本节已有对照；不继承旧分母完成标签。

### [HEAT: Faster Fully Homomorphic Inference via Approximations-Weights Co-Adaptation](https://arxiv.org/abs/2609.01730v1)

exact-v1§1–5/Appendix A–F采用输入不可见时把runtime动态精度控制迁到离线site-wise预算/权重联合适配；KL proxy不等于实际时延，124M teacher-forced边界不能外推LLM FHE实用。Ch49已补两段，Root来源及写后独立PASS。 具体主源/非作者审阅文件与当前Books段落见有效证据与实际Books记录及本节已有对照；不继承旧分母完成标签。

### [The Memory Trust Gap: Capability-Dependent Failures in Persistent-Memory Agents](https://arxiv.org/abs/2609.01852v1)

exact-v1§3–8区分no-memory缺必要事实与可从当前工具完成的任务，净害和stale reliance分开；oracle删除真值仅为诊断上界，metadata仍能改善小模型。Ch77补两段及notes，Root实际来源与写后PASS。 具体主源/非作者审阅文件与当前Books段落见有效证据与实际Books记录及本节已有对照；不继承旧分母完成标签。

### [CREDIT: Cost-guided Reduction-reuse with Efficient DSMEM Inter-CTA Tiling](https://arxiv.org/abs/2609.01864v1)

CREDIT exact-v1与固定artifact采用owner-local bulk加compact statistics复制；P增大同步/复制与资源成本也升，traffic下降非E2E收益。当前Ch49跨Block共享段已保留P(P−1)成本及小shape单CTA回退，既有整合核实。 具体主源/非作者审阅文件与当前Books段落见有效证据与实际Books记录及本节已有对照；不继承旧分母完成标签。

### [ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding Retrieval](https://arxiv.org/abs/2609.01865v1)

ExecRetrieval exact-v1与固定scorer只在选定canonical条件下exec/hit恒等，query域与test域也不同。当前Ch66 reference-first→需求域→指标恒等→proxy已经承载，既有整合核实，不把构造近克隆推广自然bug率。 具体主源/非作者审阅文件与当前Books段落见有效证据与实际Books记录及本节已有对照；不继承旧分母完成标签。

### [Epistemic Sybil Resistance: Multiplying AI Agents Without Multiplying Evidence](https://arxiv.org/abs/2609.01873v1)

只复用§5条件Gaussian/正方差的理论天花板及§6有限provenance解释；同源提取仍能增信息而非永无价值。Ch82相邻聚合段已有覆盖，Root认可采用范围；Figure4/NLL经验冲突仍保留，不称经验恢复。 具体主源/非作者审阅文件与当前Books段落见有效证据与实际Books记录及本节已有对照；不继承旧分母完成标签。

### [CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated Routing](https://arxiv.org/abs/2609.01925v1)

exact-v1§2–5独立审阅只支持anchor和背景阈值这一input-conditioned sparse prefill实现。Ch43已有selector总成本、误差预算/省略mass、index identity和dense回退，NoChange，不改称KV压缩。 具体主源/非作者审阅文件与当前Books段落见有效证据与实际Books记录及本节已有对照；不继承旧分母完成标签。

### [Multi-Turn LLM Conversations under the Least-Recently-Used Policy: Mean-Field Asymptotics and Hit Ratio Approximation](https://arxiv.org/abs/2609.02027v1)

exact-v1理论限whole-content、Poisson与指定独立条件，可复用工作量份额不等于LRU驻留概率。当前Ch54三段及fragmentation交接仍有无response回写/partial-block限制，既有整合核实。 具体主源/非作者审阅文件与当前Books段落见有效证据与实际Books记录及本节已有对照；不继承旧分母完成标签。

### [ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding](https://arxiv.org/abs/2609.02780v1)

exact-v1浅层index→query gate→选片full-depth重建，只在query前台减少历史全深物化；GPUpeak非全部存储。Ch43 layer-state/selector成本、TTFT与fallback已覆盖，NoChange。 具体主源/非作者审阅文件与当前Books段落见有效证据与实际Books记录及本节已有对照；不继承旧分母完成标签。

## 5. 缺口与下一步

本日普通可执行的审阅、Books判断及独立核对已经结束。54项均有逐项处置；47项有限采用结论已与实际Books对照，7项中心证据争议暂缓。以下外部澄清与来源日期材料均为本窗终态保留项，不支持正面证据、Books或无遗漏断言；材料到达时只定点重开。

需要外部澄清的7项：01611校准公式、split标签及probe预算；01723 DP保护单位/邻接、δ及完整accountant配置；01746更新符号与EMA正规化；01768分组/压缩偏置公式及逆命题条件；01807 Table3身份/方向及缺失factorial；02293 projection-specific mask布局/固定训练实现及未验证组合；01615逐item目标与population论证、温度配置及从null推广到不可能的边界。原文均可访问，接受作者勘误、对应实现或实验配置，不请求重复下载同一PDF。逐项依据已写入上节审阅正文。

局部不采用的争议另行保留：01873 Figure4/NLL、02159 predictor headline、02264 generic-GNN/开放拓扑泛化；这些不污染已核实的有限采用命题。02514采样等价、02690并发single-use/真实attestation未证明，不作为已实现保证。

来源日期缺口：Google两项目录材料缺可核first-public；浑元“全部”仅有9行可见截图而非完整可点击列表。需要官方带日期详情/目录导出或可访问原链接，详见覆盖表共享记录；不会因此搜全年并扩池。

窗外去重：02652实际primary为2026-08-27 Zenodo公开，不是Sep03新事件；日期与版本记录已独立核实，不纳入54项、不计零分、不扩展修复8月。

## 6. 复核

复核者：主任务协调的独立审阅者 Root。
结论：通过

完整闭环验收通过。独立准入、排除风险与日期核对已结束；当前采用命题独立复核覆盖50个arXiv家族，4个机构家族见机构独立复核。复用仅针对同版本、同采用命题的真实阅读与写后记录，不继承旧准入标准或旧报告完成标签。已落实本轮Ch77/Ch49/Ch17三处新增内容并验证与相邻论证衔接；其余采用判断核对实际Books覆盖。复核修正了01924模型身份、01975数据集数量及SolarWM的相机条件边界。§5的争议及日期限制均被明确排除出正面证据和Books，保留精确重开条件；格式、路径、评分和diff检查不被用来消除这些证据边界。
