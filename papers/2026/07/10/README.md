# Daily Research — 2026-07-10

**规范：** V3
**窗口：** 2026-07-09T09:00:00+08:00 ～ 2026-07-10T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T16:00:00+08:00

## 1. 结论

本窗以 arXiv 官方 2026-07-10 新公告为 owner 边界。旧报告恢复的 1006 个跨类别去重身份仅作为题摘筛选种子；重新逐项语义筛选后保留 10 个材料家族，而不是继承旧 16 项路由。综述、VLA 局部架构、AI for Science 和不改变长期系统责任的局部 benchmark 在分母前关闭；入选 exact v1 未见 withdrawn。

最有长期价值的变化集中在四条链：可验证环境把搜索 Agent 的训练闭环从 live web 解耦；线性 Attention、量化与分布式 reasoning 把模型结构选择变成 runtime contract；reasoning uncertainty 必须区分输出一致性、内部 probe 与外部 verifier；Agent memory 与 evaluation harness 需要明确 intervention 和 hidden supervisor 的权责。候选均已完成相称证据审阅；独立复核确认现有 Books 已在正文承载全部长期增量，本次没有新增书稿 manifest。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-ANTHROPIC | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-GOOGLE-AI | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-META-AI | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-QWEN | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-DEEPSEEK | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-MOONSHOT | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-ZAI | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-MINIMAX | 本项目历史 Daily 来源生效边界晚于本窗，不倒推扫描义务 | 不适用 | 无 |
| SRC-ARXIV | 官方新公告与 availability schedule；1006 个跨类别去重身份完成标题巡检，含糊/高信号项阅读完整摘要，10 项进入分母 | 已检查 | 无 |

代表性分母前关闭包括 KV-cache survey（secondary）、LEEVLA/WCog-VLA/Harness VLA 的局部变体、博弈论 hallucination 单点分析与 Ideas Have Genomes（AI for Science）。这些项目不进入候选表，也不被计为零分。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [DeepSearch-World](https://arxiv.org/html/2607.07820v1) | 2026-07-10T08:00:00+08:00 ～ 2026-07-10T09:00:00+08:00 | 用可验证 offline search world 和 evolving SFT 构造 Agent 自蒸馏闭环；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Linear Attention Architectures](https://arxiv.org/html/2607.07953v1) | 2026-07-10T08:00:00+08:00 ～ 2026-07-10T09:00:00+08:00 | 把线性 Attention 的跨层 routing 与表示对齐作为独立机制，而非只比较单层 kernel；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [KronQ](https://arxiv.org/html/2607.07964v1) | 2026-07-10T08:00:00+08:00 ～ 2026-07-10T09:00:00+08:00 | 用 Kronecker-factored curvature 和双侧变换决定 mixed-bit 权重配置；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [GraphEval](https://arxiv.org/html/2607.08017v1) | 2026-07-10T08:00:00+08:00 ～ 2026-07-10T09:00:00+08:00 | 将 reasoning uncertainty 从文本一致性提升为分解后因果图的一致性和鲁棒性；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [What LLM Forecasters Know but Don't Say](https://arxiv.org/html/2607.08046v1) | 2026-07-10T08:00:00+08:00 ～ 2026-07-10T09:00:00+08:00 | 分离内部可读 confidence、语言自报与 correctness calibration；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MORES](https://arxiv.org/html/2607.08116v1) | 2026-07-10T08:00:00+08:00 ～ 2026-07-10T09:00:00+08:00 | 将 reasoning unit 与无线/计算资源联合路由，改变 edge/server 分工；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：INFER-DYNAMO，[Ch52](../../../../books/part-05-inference-system/52-dynamo.md) |
| [FabriVLA](https://arxiv.org/html/2607.08575v1) | 2026-07-10T08:00:00+08:00 ～ 2026-07-10T09:00:00+08:00 | 用 conformal action-chunk uncertainty 把 VLA failure sensor 接到 abstain/fallback 控制边界；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Remember When It Matters](https://arxiv.org/html/2607.08716v1) | 2026-07-10T08:00:00+08:00 ～ 2026-07-10T09:00:00+08:00 | 将 memory maintenance 与是否向当前上下文注入提醒的 intervention policy 分开；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [The Illusion of Equivalency](https://arxiv.org/html/2607.08734v1) | 2026-07-10T08:00:00+08:00 ～ 2026-07-10T09:00:00+08:00 | 证明量化需要同时检查 aggregate 指标、内部分布漂移和逐样本行为一致性；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [UniClawBench](https://arxiv.org/html/2607.08768v1) | 2026-07-10T08:00:00+08:00 ～ 2026-07-10T09:00:00+08:00 | 用 hidden supervisor、隔离 executor 和 leakage-bounded user simulator 定义 proactive Agent harness；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [DeepSearch-World](https://arxiv.org/html/2607.07820v1)

§3～§4 定义可验证 offline search world、scaffold teacher、rejection 与 evolving SFT，§5 只支持论文 search benchmarks 和有限轮次设置，不能证明迁移到 live web。Ch81 已把 deterministic simulator、verifier、生成数据版本和真实环境回归写成 workflow self-improvement 的提交边界。

### [Linear Attention Architectures](https://arxiv.org/html/2607.07953v1)

§2～§4 统一 recurrent notation，并提出跨层 routing 与 representation alignment；§5～§7 的收益随规模衰减且没有 serving benchmark。Ch22 已将线性/递归状态的表达能力、跨层传递和 full attention 共存边界连成主线。

### [KronQ](https://arxiv.org/html/2607.07964v1)

§3～§4 以输出梯度协方差与 activation covariance 的 Kronecker 近似估计 curvature，再做双侧 incoherence transform 和 mixed-bit allocation；附录保留 calibration 与临时内存开销。Ch49 已在 execution-plan 的量化分支承载“离线敏感度决定 artifact，runtime 仍需验证 kernel 与质量”的边界。

### [GraphEval](https://arxiv.org/html/2607.08017v1)

§3～§4 将多条 CoT 分解成 claimed causal DAG，用 semantic/structural distance、medoid 与 adversarial-medoid 测试一致性；短 reasoning、decomposer/judge 依赖和额外计算限制其外推。Ch66 已将其归为 reasoning-structure sensor，而非真值证明。

### [What LLM Forecasters Know but Don't Say](https://arxiv.org/html/2607.08046v1)

§3～§4 从 activation 训练轻量 probe，并比较温度、OOD、forced answer 与 pre-reasoning triage；“可被 probe 读出”不等于模型能自行可靠使用，也不证明跨模型校准。Ch66 已明确 verbal confidence、internal sensor 和 evidence-backed correctness 是三种不同状态。

### [MORES](https://arxiv.org/html/2607.08116v1)

§3～§5 把 reasoning 拆为 device prelude/coda 与 server recurrent units，并联合优化语义路由、无线和算力；§6 仍是指定模型、A100 server 与移动侧建模，不是生产 tail/energy 证明。Ch52 已承载 semantic work 与资源 placement 共同决定 distributed state edge 的机制。

### [FabriVLA](https://arxiv.org/html/2607.08575v1)

exact v1 把 action chunk 的 uncertainty set 接到 conformal calibration，但有效性依赖 exchangeability、calibration data 和执行环境，不能把 coverage 声明外推为物理安全保证。Ch26 已要求 failure sensor 只提出 abstain/fallback，由独立 safety controller 持有 action commit。

### [Remember When It Matters](https://arxiv.org/html/2607.08716v1)

§3 的两阶段结构先维护 structured memory bank，再决定 silence 或 grounded reminder；§4 的 Terminal-Bench/tau2 对照不能证明通用 intervention policy。Ch77 已分离 memory truth、retrieval proposal 与 context-injection ownership。

### [The Illusion of Equivalency](https://arxiv.org/html/2607.08734v1)

§3～§4 在四个模型和 llama.cpp quantizers 上比较 attention-distribution divergence、per-example agreement 与 aggregate 指标；没有通用 safe-bit threshold。Ch49 已把量化视为新部署 artifact，要求用 held-out 行为、分布和 runtime contract 共同验收。

### [UniClawBench](https://arxiv.org/html/2607.08768v1)

§3 将 executor、hidden supervisor 与 leakage-bounded user simulator 分离，§4 覆盖 400 个双语任务和多框架对照；它证明的是所测 harness contract，不是 universal judge reliability。Ch66 已把环境、工具、judge、泄漏和 task isolation 纳入 evaluation identity。

## 5. 缺口与下一步

无

无材料请求。Books manifest 为“新增写入 0，已有覆盖 10”。

## 6. 复核

复核者：`/root/aug21_31`（非作者独立复核）

结论：通过

复核重新阅读了原分母中被关闭的 6 项摘要：KV survey 属 secondary source，三项 VLA/Embodied 工作是局部模型变体，科学谱系 benchmark 属暂不纳入的 AI for Science，化学多智能体只证明领域 pipeline，均不应恢复为长期系统候选。10 个保留项的 first-public owner、withdrawn 状态、评分与 exact-v1 claim boundary 一致；相应 Books 章节均存在正文机制承载，且保留实验适用边界与 fallback。结构、链接和候选算术通过检查。
