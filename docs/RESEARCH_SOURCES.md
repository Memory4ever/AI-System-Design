# 研究来源

注册表版本：2026-09-07

## 怎么使用

这是一份围绕大模型及其 Training、Inference、平台与 Agent 的工作清单，不是 AI 机构大全。
只加载本次报告需要的分组，组内按表中顺序检查，始终限定在本次报告窗口和关注主题内，不遍历机构历年全部论文。

- **每日**：Daily 检查；Weekly 直接复用对应 Daily 的来源记录和研究结果，不重新扫描。
- **每周**：Weekly 检查；Daily 不加载或扫描这组来源。
- **按需**：相关会议论文发布、重要版本/协议变化，或已有候选需要此材料时定点检查；不做常规全站扫描。

频率约束的是发现扫描，不阻止为已入选候选打开必要的原始证据，也不因此扩扫该来源。
Weekly 对 Daily 的复用与缺口补查按 [Report 合同 §2](./REPORT_CONTRACTS.md#2-时间与归档) 执行。

日常与历史报告共用此清单。历史窗口中尚未存在的来源记为不适用，无法恢复的必要材料记为缺口。
表外出现明确相关的原始研究也可以采用，不必先扩充清单，更不因此扫描该机构整个网站。
来源只决定去哪里找；机构名和学科分类不能代替项目范围。各入口只检索[研究合同 §3](./RESEARCH_CONTRACT.md#3-先判断贡献再投入审阅)
定义的 ROADMAP 主线主题，再通过题摘语义判断范围与贡献。官方机构也不全量审阅其医学、材料等其他研究；
AI for Science 按 ROADMAP 暂缓。下表“关注内容”是本项目从该源选取的切片，不是该机构或平台全部研究范围。

## 来源清单

ID 只用于稳定引用和来源去重。检查结果按[Report 合同](./REPORT_CONTRACTS.md)记录“查哪里、查到哪里、结果、缺口”，
不为下表另建逐字段收据。日期、证据权限、评分与 Books 判断不在本文件重复定义。

### 每日检查

<!-- validator:source-list -->
| ID | 来源 | 入口 | 频率 | 关注内容 |
| --- | --- | --- | --- | --- |
| SRC-OPENAI | OpenAI | [Research](https://openai.com/research/) | 每日 | 模型机制、训练方法与系统报告 |
| SRC-ANTHROPIC | Anthropic | [Research](https://www.anthropic.com/research) | 每日 | 模型、Agent、可靠性与系统报告 |
| SRC-GOOGLE-AI | Google AI（DeepMind / Research） | [Google DeepMind](https://deepmind.google/research/)<br>[Google Research](https://research.google/pubs/) | 每日 | 模型、训练、推理与多模态系统 |
| SRC-META-AI | Meta / FAIR | [Research](https://ai.meta.com/research/) | 每日 | 开放模型、架构与训练机制 |
| SRC-QWEN | Qwen | [Qwen](https://qwenlm.github.io/) | 每日 | 模型架构、训练与多模态机制 |
| SRC-DEEPSEEK | DeepSeek | [Research](https://www.deepseek.com/) | 每日 | 模型架构、训练与推理效率 |
| SRC-MOONSHOT | Moonshot / Kimi | [Kimi Platform Blog](https://platform.kimi.com/blog)<br>[MoonshotAI GitHub](https://github.com/MoonshotAI) | 每日 | 长上下文、模型与 Agent 机制 |
| SRC-TENCENT-HUNYUAN | 腾讯混元 / Hunyuan | [官方 Research（首查）](https://hunyuan.tencent.com/research)<br>[Tencent-Hunyuan](https://github.com/Tencent-Hunyuan)<br>[T1 技术说明](https://github.com/Tencent/llm.hunyuan.T1) | 每日 | 从研究页“全部”列表进入原文；语言/多模态、生成、后训练与训练部署效率。动态目录无法提取时用浏览器核查 |
| SRC-ZAI | Z.ai / 智谱 GLM | [官方 Research（首查）](https://www.zhipuai.cn/zh/research)<br>[zai-org](https://github.com/zai-org)<br>[官方发布说明](https://docs.z.ai/release-notes/new-released) | 每日 | 首查 Research 论文目录；GLM 架构、训练、多模态、推理系统与 Agent |
| SRC-BYTEDANCE-SEED | 字节跳动豆包 / Seed | [Research / Blog](https://seed.bytedance.com/en/research)<br>[论文目录](https://seed.bytedance.com/en/public_papers)<br>[ByteDance-Seed](https://github.com/ByteDance-Seed) | 每日 | 语言与多模态基础模型、推理、后训练、Agent、模型系统效率；研究论文与技术博客，不纳入暂缓的 AI for Science |
| SRC-BAIDU-ERNIE | 百度文心 / ERNIE | [ERNIE 技术博客](https://ernie.baidu.com/blog/zh/)<br>[PaddlePaddle/ERNIE](https://github.com/PaddlePaddle/ERNIE) | 每日 | 文心语言/多模态架构、MoE、预训练/后训练与训练推理工程；官方论文、技术报告与技术博客 |
| SRC-XIAOMI-MIMO | 小米 MiMo | [MiMo Paper / Blog](https://mimo.xiaomi.com/)<br>[XiaomiMiMo](https://github.com/XiaomiMiMo) | 每日 | 推理与多模态模型、Attention、后训练/蒸馏、Agent 与训练推理效率；论文、技术报告与技术博客 |
| SRC-MINIMAX | MiniMax | [Research / Blog](https://www.minimax.io/blog)<br>[中文技术博客](https://www.minimaxi.com/blog)<br>[MiniMax-AI](https://github.com/MiniMax-AI)<br>[Agent Tech Blog](https://agent.minimax.io/docs/techblog) | 每日 | 长上下文、模型架构、多模态生成、后训练、Agent 与系统效率；研究论文、技术报告与技术博客 |
| SRC-ARXIV | arXiv | [论文列表](https://arxiv.org/)<br>[查询接口](https://export.arxiv.org/api/query) | 每日 | 按下节范围检查窗口内论文；跨分类先去重 |

### 每周补齐

<!-- validator:source-list -->
| ID | 来源 | 入口 | 频率 | 关注内容 |
| --- | --- | --- | --- | --- |
| SRC-MISTRAL | Mistral | [News](https://mistral.ai/news/) | 每周 | 开放模型、架构与部署约束 |
| SRC-AI2 | Ai2 | [Papers](https://allenai.org/papers) | 每周 | 可复现训练、数据与开放模型 |
| SRC-BLACK-FOREST-LABS | Black Forest Labs | [Research](https://bfl.ai/research) | 每周 | 图像表示与生成机制 |
| SRC-PHYSICAL-INTELLIGENCE | Physical Intelligence | [Physical Intelligence](https://www.pi.website/) | 每周 | VLA、机器人策略与闭环控制 |
| SRC-WORLD-LABS | World Labs | [Research & Insights](https://www.worldlabs.ai/blog) | 每周 | 空间表示、世界模型、生成/重建/模拟与训练推理机制 |
| SRC-SSI | Safe Superintelligence / SSI | [Updates](https://ssi.inc/updates)<br>[官方主页](https://ssi.inc/) | 每周 | 能力与安全协同、泛化、学习效率与持续学习的公开研究 |
| SRC-REFLECTION-AI | Reflection AI | [Blog](https://reflection.ai/blog)<br>[News](https://reflection.ai/news) | 每周 | 开放基础模型、预训练/RL、MoE 与 Agent；Blog 首查，News 定位原始发布 |
| SRC-AMI-LABS | AMI Labs | [Updates](https://amilabs.xyz/updates)<br>[官方主页](https://amilabs.xyz/) | 每周 | 世界模型、表示学习、持久记忆、推理规划与可控性 |
| SRC-THINKING-MACHINES | Thinking Machines Lab | [Connectionism](https://thinkingmachines.ai/blog/) | 每周 | 模型学习、LoRA、蒸馏、后训练、交互模型与推理数值行为 |
| SRC-PRIME-INTELLECT | Prime Intellect | [Blog / Research](https://www.primeintellect.ai/blog) | 每周 | 分布式训练、异步 RL、rollout/权重同步、训练环境、MoE 与推理 kernel |
| SRC-SAKANA-AI | Sakana AI | [Blog](https://sakana.ai/blog/)<br>[SakanaAI](https://github.com/SakanaAI) | 每周 | 模型合并、架构/优化搜索、推理效率、模型编排与 Agent 自改进 |
| SRC-RECURSIVE | Recursive | [Recent Stories](https://www.recursive.com/) | 每周 | 语言模型训练算法自动改进、训练效率与 GPU kernel |
| SRC-MIND-LAB | Mind Lab | [Publications / Updates](https://macaron.im/mindlab) | 每周 | 持续学习、PEFT/LoRA、长上下文 RL 与训练运行时；目录经 Hugging Face 跳转作者论文 |
| SRC-SAND-AI | Sand.ai | [SandAI-org](https://github.com/SandAI-org)<br>[MAGI-1](https://github.com/SandAI-org/MAGI-1)<br>[MagiAttention](https://github.com/SandAI-org/MagiAttention) | 每周 | AR/扩散基础模型、Attention、长上下文、分布式训练与流式推理 |
| SRC-EVERMIND | EverMind | [EverCore 论文入口](https://evermind.ai/) | 每周 | 大模型 Agent 长期记忆的表示、组织、检索与长程推理评价 |
| SRC-METR | METR | [Research](https://metr.org/) | 每周 | 能力测量、任务评估与可靠性边界 |
| SRC-PYTORCH | PyTorch | [Releases](https://github.com/pytorch/pytorch/releases) | 每周 | 训练、编译、分布式与执行语义变化 |
| SRC-MEGATRON-LM | Megatron-LM | [Repository](https://github.com/NVIDIA/Megatron-LM) | 每周 | 大模型训练并行与运行时 |
| SRC-DEEPSPEED | DeepSpeed | [Releases](https://github.com/deepspeedai/DeepSpeed/releases) | 每周 | 训练状态分片、通信与内存机制 |
| SRC-VERL | verl | [verl](https://github.com/verl-project/verl) | 每周 | 后训练数据流、rollout 与训练调度 |
| SRC-VLLM | vLLM | [Releases](https://github.com/vllm-project/vllm/releases) | 每周 | 推理调度、KV 状态与执行路径 |
| SRC-SGLANG | SGLang | [Releases](https://github.com/sgl-project/sglang/releases) | 每周 | 结构化生成、推理调度与缓存 |
| SRC-TRITON-LANGUAGE | Triton kernel language | [Releases](https://github.com/triton-lang/triton/releases) | 每周 | GPU kernel 编译与执行机制，不是推理服务器 |
| SRC-FLASHINFER | FlashInfer | [FlashInfer](https://github.com/flashinfer-ai/flashinfer) | 每周 | Attention、KV 与推理 kernel |
| SRC-NCCL | NCCL | [Releases](https://github.com/NVIDIA/nccl/releases) | 每周 | GPU collective、拓扑与通信语义 |
| SRC-HF-TRANSFORMERS | Transformers | [Releases](https://github.com/huggingface/transformers/releases) | 每周 | 模型实现、生成与缓存接口 |
| SRC-KSERVE | KServe | [Releases](https://github.com/kserve/kserve/releases) | 每周 | 模型部署、服务控制与推理接口 |
| SRC-RAY | Ray | [Releases](https://github.com/ray-project/ray/releases) | 每周 | 分布式执行、训练与服务调度 |
| SRC-MCP | MCP | [MCP Releases](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | 每周 | 工具协议、权限与调用契约 |

### 按需触发

<!-- validator:source-list -->
| ID | 来源 | 入口 | 频率 | 关注内容 |
| --- | --- | --- | --- | --- |
| SRC-MLCOMMONS | MLCommons / MLPerf | [Benchmarks](https://mlcommons.org/benchmarks/) | 按需 | 新评测轮次、规则或 suite 变化 |
| SRC-STANFORD-CRFM | Stanford CRFM / HELM | [CRFM](https://crfm.stanford.edu/)<br>[HELM](https://crfm.stanford.edu/helm/index.html) | 按需 | 评估方法、透明度与 foundation-model systems |
| SRC-LM-EVAL-HARNESS | LM Evaluation Harness | [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) | 按需 | 影响评估可比性或复现的实现变化 |
| SRC-MLSYS | MLSys | [MLSys Proceedings](https://proceedings.mlsys.org/) | 按需 | 新一届正式论文中的机器学习系统机制 |
| SRC-OPENREVIEW | OpenReview | [OpenReview](https://openreview.net/) | 按需 | ICLR、ICML、NeurIPS、COLM、CoRL 的公开论文与必要审稿记录 |
| SRC-USENIX | USENIX | [USENIX](https://www.usenix.org/) | 按需 | OSDI、NSDI、ATC、FAST 中的 AI 系统论文 |
| SRC-JAX | JAX | [Releases](https://github.com/jax-ml/jax/releases) | 按需 | 影响编译、并行或训练语义的发布 |
| SRC-TENSORRT-LLM | TensorRT-LLM | [Releases](https://github.com/NVIDIA/TensorRT-LLM/releases) | 按需 | 执行计划、量化与推理调度的重要变化 |
| SRC-LLAMA-CPP | llama.cpp | [Releases](https://github.com/ggml-org/llama.cpp/releases) | 按需 | 端侧执行、量化与资源约束的重要变化 |
| SRC-TORCHTITAN | TorchTitan | [TorchTitan](https://github.com/pytorch/torchtitan) | 按需 | 可复现分布式训练参考实现的机制变化 |
| SRC-KUBEFLOW | Kubeflow | [Releases](https://github.com/kubeflow/kubeflow/releases) | 按需 | 训练工作负载与模型生命周期控制变化 |
| SRC-LLM-D | llm-d | [llm-d](https://github.com/llm-d/llm-d) | 按需 | 分布式推理、路由与状态管理变化 |
| SRC-GATEWAY-INFERENCE | Gateway API Inference Extension | [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension) | 按需 | 推理路由与调度接口变化 |
| SRC-KUEUE | Kueue | [Kueue](https://github.com/kubernetes-sigs/kueue) | 按需 | AI 工作负载准入、配额与资源调度变化 |
| SRC-DEEPEP | DeepEP | [DeepEP](https://github.com/deepseek-ai/DeepEP) | 按需 | MoE dispatch/combine 与通信机制变化 |
| SRC-DEEPGEMM | DeepGEMM | [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) | 按需 | 低精度矩阵计算与 kernel 机制变化 |
| SRC-A2A | A2A | [A2A](https://github.com/a2aproject/A2A) | 按需 | Agent 间任务、消息与状态契约变化 |

## arXiv 查哪些分类

分类是主题检索的入口，不是必须全量逐篇审阅的队列。先确定与 ROADMAP 主线对应的主题及同义表达，再在以下分类检索本窗公开事件；
不以 `cs.CL` 代表整个项目，也不把分类全部条目默认送入逐项题摘筛选或审阅。

| 分类 | 中文含义 | 本项目关注 |
| --- | --- | --- |
| `cs.CL` | 计算语言学 | 大语言模型的架构、训练、上下文、生成、后训练与评价；不全扫传统语言学/NLP应用 |
| `cs.LG` | 机器学习 | 按 foundation/language model、Transformer、MoE、模型训练/优化等相关主题检索，不全扫通用学习及领域预测 |
| `cs.DC` | 分布式与并行计算 | 按大模型训练/推理、GPU并行、模型状态、通信与调度主题检索，不全扫一般分布式算法 |
| `cs.AI` | 人工智能 | 按大模型推理、工具调用、Agent、模型驱动规划主题检索，不全扫传统规划与领域AI |

以下入口覆盖同等重要的多模态与系统主线，也只按主题做窗口内检索，不全量扩池：

| 分类 | 中文含义 | 补检主题 |
| --- | --- | --- |
| `cs.CV`、`cs.RO` | 视觉、机器人 | 多模态基础模型、生成基础模型、World Model、VLA；不泛化到所有视觉与控制研究 |
| `cs.AR`、`cs.PL` | 计算机体系结构、编程语言 | 服务大模型计算的 accelerator、kernel、编译与执行计划 |
| `cs.OS`、`cs.PF` | 操作系统、性能 | 大模型运行时、资源管理与性能测量 |
| `cs.IR`、`cs.MA` | 信息检索、多智能体 | 大模型 RAG、记忆检索与 Agent 协作；不全扫通用推荐、检索与博弈 |

主题查询用常见术语及同义表达获取线索，不按一个固定关键词或正则决定入选；同一论文跨分类出现先去重，再读一次。
对检索得到的条目按研究合同先范围、后贡献判断。已抓取的宽列表只作查漏与重用的原始线索，不能因列表已存在就把整类条目变成待逐项关闭的工作量。
用本窗官方分类列表的相关标题浏览及已知相关原始发布作有界补检，弥补只靠术语查询可能漏掉新命名机制的局限；
记录实际主题、查询、分页/停止点与补检范围。若执行中变成整类逐项筛选，先收窄入口并说明受影响范围；覆盖指完成这些约定主题检查，不宣称全学科召回。
其他分类有具体相关线索时定点查看，不列为每日必扫来源。

## 补检与材料恢复

Hugging Face Papers、学术搜索和元数据服务只用于补线索、去重或恢复具体材料，不再逐站固定扫描。
有线索就回到作者稿、官方报告、正式论文或对应版本的实现；无法取得必要证据时列出缺口，不无限追查。
搜索摘要、转载与排行榜名次不能替代原始证据；机构声誉也不能代替实验条件和证据边界。

会议来源只检查目标年份、实际发布批次与项目相关论文，不全站扫描投稿、评审或历史记录。
代码项目关注改变系统机制、接口或可靠性判断的发布、RFC 与实现；不逐个审查普通修复 PR。
