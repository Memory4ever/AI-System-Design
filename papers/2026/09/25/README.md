# Daily Research — 2026-09-25

**规范：** V3  
**窗口：** 2026-09-24T09:00:00+08:00 ～ 2026-09-25T09:00:00+08:00  
**状态：** 完成  
**Books：** 纳入本次  
**检查时间：** 2026-09-25T20:30:00+08:00

## 1. 结论

本窗最值得长期保留的不是论文数量，而是四条边界：工具副作用的 unknown outcome 不能仅靠读回变成 exactly-once；Prefix KV 的淘汰策略须同时考虑会话节奏、重算成本与碎片；跨模型共享 GPU 需要可比较的服务缺口而非裸 queue；评估必须读对输出事件，并防止 Agent 同时控制结果和证据。这些机制已分别进入 Tool、GPU Memory、Inference Scheduling 与 Evaluation 的原有论证。多模态表示、具身异步控制、Agent Memory 和训练评估的局部增量也已定点写入，均保留作者实验边界。

14 个每日来源均已检查到可说明的停止点或精确限制。arXiv 官方 09-25 `New` 的 12 个合同分类共见 **567 个跨分类去重原始身份**；这是宽列表的查漏规模，不是 567 篇长期贡献论文，也不是逐篇全文审阅量。按本项目主题做窗口内筛选，对可能涉及主线或含糊的条目读完整摘要并判断具体增量；补检后入选 **30 个唯一候选家族**：28 项形成书稿语义增量、1 项已有实质覆盖、1 项仅保留报告，不因能映射 ROADMAP 就强行入选。`2609.30123` 已有 Workflow 覆盖，`2609.29661` 是较早同家族，`2609.29499` 已找到 08-26 作者上传的完整正文，均不计 09-25 首次公开候选。Meta 09-24 的 MaD-RL 尚无可信的 09:00 前后归属和可读正文，被隔离，不参与评分和 Books。

以上是研究作者的受限实验与本项目的设计推论，不是复现实验或生产保证。更大规模 Agent、异构 fleet、真实机器人、开放域证据仲裁等仍需要各自的任务和 SLO 复测。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) 与 [Publication](https://openai.com/research/index/publication/)倒序，最近可见 09-23、09-08，早于本窗 | 已检查 | 限上述官方研究目录 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 09-24 [Project Swap](https://www.anthropic.com/research/project-swap) 正文已读：书籍交易 Agent 的社会/经济观察，无本项目机制增量，题摘级排除 | 已检查 | 日期不影响已明确的贡献排除 |
| SRC-GOOGLE-AI | [Google Research Blog](https://research.google/blog/) 09-24 [long-form video 综述](https://research.google/blog/coherent-long-form-video-generation/) 引用四份早期论文；[DeepMind Research](https://deepmind.google/research/) 与 [Research Publications](https://research.google/pubs/) 检至首个窗前条目 | 已检查 | 综述不是所引旧论文的首次公开，未重复计分 |
| SRC-META-AI | [官方论文目录](https://ai.meta.com/global_search/?content_types%5B0%5D=publication&page=1) 首项为 09-24 MaD-RL，下一项 09-07；[论文页](https://ai.meta.com/research/publications/mad-rl-matching-distributions-for-calibrating-llms-with-reinforcement-learning/)有摘要 | 受阻 | 仅日级日期与失效的官方 PDF 下载；见 §5 的定点恢复 |
| SRC-QWEN | [官方 Research 关联目录](https://qwen.ai/research/qwen3.8-livetranslate)可读索引的最近条目 09-20、09-18；另一个 09-24 [空内容页](https://qwen.ai/blog?id=4074cca80393150c248e508aa62983f9cb7d27cd)仅显示日期、0 words，无标题/机制 | 受阻 | 动态正文返回空，不能声称该 09-24 空壳代表一篇新论文；有身份时定点重开 |
| SRC-DEEPSEEK | [Research/News](https://www.deepseek.com/en/news/)倒序首项 09-10，Research 首项更早 | 已检查 | 普通仓库提交不等于技术发布 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog)倒序首项为 2025-11-07；[MoonshotAI](https://github.com/MoonshotAI)未见本窗有身份明确的重大研究发布 | 已检查 | 限官方博客及明确发布，不推断全部代码活动 |
| SRC-TENCENT-HUNYUAN | [Research 全部列表](https://hunyuan.tencent.com/research)动态页改由官方 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，`pageNum=1,pageSize=30,renderType=0` 返回 9/9，最新 `publicAt=1790150728` 属 09-23 | 已检查 | 已到列表末页，未把空 HTML 当无更新 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)倒序首项 08-26；[发布说明](https://docs.z.ai/release-notes/new-released)首项 08-26 | 已检查 | 以可读的最近条目作倒序停止点 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers)首项 08-18；[Research](https://seed.bytedance.com/en/research)最近技术博客早于本窗 | 已检查 | 不把一般代码 push 或 AI for Science 应用纳入 |
| SRC-BAIDU-ERNIE | [技术博客](https://ernie.baidu.com/blog/zh/)首项 05-09；[ERNIE release](https://github.com/PaddlePaddle/ERNIE/releases)最近 06-30 | 已检查 | 限这些原始发布入口 |
| SRC-XIAOMI-MIMO | [MiMo Paper / Blog](https://mimo.xiaomi.com/) Paper 最新 06-29；Blog 前几项无日期，其中材料研发属于暂缓的 AI for Science | 受阻 | 未给 Blog 条目事件时刻；不能由无日期页宣称本窗完全零发布 |
| SRC-MINIMAX | [英文 Research Blog](https://www.minimax.io/blog)与[中文博客](https://www.minimaxi.com/blog)倒序首项 08-13；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)返回目录壳 | 受阻 | Agent 子目录未得到可分页的条目清单；未据此做无遗漏断言 |
| SRC-ARXIV | 09-25 官方 `New` 的 12 个合同分类逐一检查，分类、计数与复查范围见下；只取 New，跨分类按 arXiv ID 去重为 567 个宽列表身份，按项目主题检索和相关标题浏览，范围内/含糊项读完整摘要 | 已检查 | `New` 公告批次是本窗公开事件；HTML 的 submitted 字段不是公开时间。Cross/Replacement 未被误作首次公开；宽列表并不构成逐项完整摘要审阅队列 |

arXiv 的 09-25 New 对应其周四 20:00 US Eastern 的公告，即北京时间 **2026-09-25 08:00**，落在本窗。下表 30 项在该批次中；已发现的先前公开线索逐项反查。HTML 页面的 submitted 或文稿日期本身不能证明公开时刻，`2609.29499` 因 08-26 作者已公开正文而排除。[arXiv 公告时间说明](https://info.arxiv.org/help/availability.html)。当日访问日期均为 2026-09-25。

arXiv 于 **2026-09-25T19:32:22+08:00** 定点复查以下官方 `New submissions` 段，均读到本段末尾；括号内为该段身份数：
[cs.CL](https://arxiv.org/list/cs.CL/new)（86）、[cs.LG](https://arxiv.org/list/cs.LG/new)（119）、[cs.DC](https://arxiv.org/list/cs.DC/new)（15）、[cs.AI](https://arxiv.org/list/cs.AI/new)（107）、[cs.CV](https://arxiv.org/list/cs.CV/new)（111）、[cs.RO](https://arxiv.org/list/cs.RO/new)（87）、[cs.AR](https://arxiv.org/list/cs.AR/new)（11）、[cs.PL](https://arxiv.org/list/cs.PL/new)（7）、[cs.OS](https://arxiv.org/list/cs.OS/new)（0）、[cs.PF](https://arxiv.org/list/cs.PF/new)（5）、[cs.IR](https://arxiv.org/list/cs.IR/new)（16）、[cs.MA](https://arxiv.org/list/cs.MA/new)（3）。New 主分类的 12 组 ID 相加与按 ID 去重后均为 567；[原始 ID 快照](_sources/arxiv-new.md)保留逐组身份。567 只表示宽列表召回；本项目按注册表主题与相关标题浏览做有界补检，对可能相关的完整题摘判断贡献，未把其余分类论文冒充逐篇 Full Source Review。入选 30 项见 §3，先前公开及已有覆盖的边界例子见 §5；这不能证明全学科绝无漏项。

## 3. 候选与判断

V3 评分依次为 `Design Delta + System Reach + Durability = Total`，仅给通过贡献筛选的材料家族。表中“深入完成”表示已就采用命题读精确 v1 的方法、相关实验/对照与限制，**不是代码复现**；“标准完成”也不是只看摘要。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Reward Hacking Challenges Oversight of Autonomous Research Agents](https://arxiv.org/html/2609.28614v1) | 2026-09-25T08:00:00+08:00 | 结果与证据同由 Agent 控制时 artifact-only 审查盲区；2+2+3=7 | 深入完成 | 整合 PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Thinking Leakage](https://arxiv.org/html/2609.28682v1) | 2026-09-25T08:00:00+08:00 | NoThink 增益的模式依赖与能力归因；2+2+3=7 | 深入完成 | 整合 TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [Temporal Taxation / Whisper Compression](https://arxiv.org/html/2609.28739v1) | 2026-09-25T08:00:00+08:00 | 权重压缩后的群体级错误负担需部署切片审计；2+1+2=5 | 深入完成 | 整合 PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Xtrace](https://arxiv.org/html/2609.28769v1) | 2026-09-25T08:00:00+08:00 | 预编译探针改变被测 GPU binary，观测保真必须与探针开销分开验收；3+2+3=8 | 深入完成 | 整合 PLATFORM-MONITORING [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [LastOPD](https://arxiv.org/html/2609.28845v1) | 2026-09-25T08:00:00+08:00 | 跨深宽 latent 蒸馏的对齐指标可持续改善而行为崩溃，监督层位与时长成为 Gate；3+1+3=7 | 深入完成 | 整合 TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md) |
| [Where Hallucinations Live](https://arxiv.org/html/2609.29048v1) | 2026-09-25T08:00:00+08:00 | VQ 视觉 token 的早层路由不能跨架构套用统一消融；2+1+2=5 | 深入完成 | 整合 MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [When Fancy Eviction Fails](https://arxiv.org/html/2609.28870v1) | 2026-09-25T08:00:00+08:00 | session cadence 使 LRU 与 compute-aware/one-hit 淘汰的排序有条件变化；2+2+3=7 | 深入完成 | 整合 INFER-GPU-MEMORY [章节](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Streaming-WAM](https://arxiv.org/html/2609.28927v1) | 2026-09-25T08:00:00+08:00 | 异步物理预测须条件化已提交 action prefix；2+1+2=5 | 深入完成 | 整合 MULTIMODAL-EMBODIED-VLA [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Where Does Exactly-Once Live?](https://arxiv.org/html/2609.29095v1) | 2026-09-25T08:00:00+08:00 | read-back 无法覆盖晚到提交/重发；3+2+3=8 | 深入完成 | 整合 AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [Cross-Model Autoscaling](https://arxiv.org/html/2609.29160v1) | 2026-09-25T08:00:00+08:00 | 异构模型之间的相对服务缺口与 GPU 容量仲裁；2+2+3=7 | 深入完成 | 整合 INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Selective Supervision for Direct-OPD](https://arxiv.org/html/2609.29142v1) | 2026-09-25T08:00:00+08:00 | teacher/base 绝对概率质量趋零时 log-ratio 奖励仍可不变；3+1+3=7 | 深入完成 | 整合 TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [Scope Before You Persist](https://arxiv.org/html/2609.29144v1) | 2026-09-25T08:00:00+08:00 | 局部认证的 skill 不应全局检索部署；3+2+3=8 | 深入完成 | 整合 AGENT-MEMORY [章节](../../../../books/part-07-agent/77-memory.md) |
| [Post-Training Leaves Behavioral Shadows](https://arxiv.org/html/2609.29233v1) | 2026-09-25T08:00:00+08:00 | 任务无关单词输出可在同祖先主动查询下转移后训练能力；3+2+3=8 | 深入完成 | 整合 PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [No More Free Lunch: Corpus Task Complexity Matters as Corpora Grow](https://arxiv.org/html/2609.29245v1) | 2026-09-25T08:00:00+08:00 | 语料关系复杂度可改变 dense 与 block-sparse 的质量排序；3+2+3=8 | 深入完成 | 整合 MODEL-LONG-CONTEXT [章节](../../../../books/part-02-model/22-long-context.md) |
| [Reasoning Instructions Can Break Answer Decoding in VLMs](https://arxiv.org/html/2609.29278v1) | 2026-09-25T08:00:00+08:00 | CoT cue 后立即读 logits 与最终答案事件不一致；3+1+3=7 | 深入完成 | 整合 PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Decoupled Early Exits for Task-Dependent Compute Allocation in Flow-Matching VLAs](https://arxiv.org/html/2609.29382v1) | 2026-09-25T08:00:00+08:00 | 视觉前缀深度、动作专家深度与去噪步数的成本轴不同；浅视觉出口接深专家须合成缺失前缀 K/V；3+2+3=8 | 深入完成 | 整合 MULTIMODAL-EMBODIED-VLA [章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Stale Does Not Mean Unsafe](https://arxiv.org/html/2609.29522v1) | 2026-09-25T08:00:00+08:00 | 全局版本 guard 与语义前提 guard 的安全/可用性取舍；2+2+2=6 | 深入完成 | 整合 AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [ERRAND: Budgeted Maintenance of Agent Memory](https://arxiv.org/html/2609.29545v1) | 2026-09-25T08:00:00+08:00 | 记忆重检与同一 action budget 竞争；2+1+3=6 | 深入完成 | 整合 AGENT-MEMORY [章节](../../../../books/part-07-agent/77-memory.md) |
| [Is Reasoning Always Useful?](https://arxiv.org/html/2609.29560v1) | 2026-09-25T08:00:00+08:00 | 多模态检索正例相似度改善仍可能降低 hard-negative margin；2+1+3=6 | 深入完成 | 整合 MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [PartHackBench](https://arxiv.org/html/2609.29578v1) | 2026-09-25T08:00:00+08:00 | 先认证当前进度与 Agent attribution 相等，再测部分分数膨胀；2+2+3=7 | 深入完成 | 整合 PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Safe Skill Retirement](https://arxiv.org/html/2609.29543v1) | 2026-09-25T08:00:00+08:00 | 删除 skill 条款需分别认证授权任务效用与 protected effect；3+2+3=8 | 深入完成 | 整合 AGENT-PLATFORM [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [ModularSQL](https://arxiv.org/html/2609.29573v1) | 2026-09-25T08:00:00+08:00 | SQL set evaluator 静默忽略 duplicate-row multiplicity；3+1+3=7 | 深入完成 | 整合 PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Sequential Knowledge Editing Breaks Evidence Arbitration](https://arxiv.org/html/2609.29587v1) | 2026-09-25T08:00:00+08:00 | 编辑未触及事实也可损坏证据仲裁而不损常规能力分；3+2+3=8 | 深入完成 | 整合 PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Where Does the Energy Go?](https://arxiv.org/html/2609.29707v1) | 2026-09-25T08:00:00+08:00 | Agent 能耗的 device-only 与整机/phase 口径不能混用；2+2+2=6 | 深入完成 | 整合 PLATFORM-COST [章节](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [Three Ways Classical Test Theory Misleads for LLM Judges](https://arxiv.org/html/2609.29709v1) | 2026-09-25T08:00:00+08:00 | reliability 统计须声明 scorer facet 与被估计量；3+2+3=8 | 深入完成 | 整合 PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Your Transformer Can Hold Two Thoughts at Once](https://arxiv.org/html/2609.29845v1) | 2026-09-25T08:00:00+08:00 | 混合 embedding 可保留双流部分信号，但直接解码与端到端吞吐并未兑现宣传；2+1+2=5 | 标准完成 | 仅报告：实验性机制线索，缺可替代批处理的质量/成本证据 |
| [When Can Agents Forget Their Reasoning?](https://arxiv.org/html/2609.29875v1) | 2026-09-25T08:00:00+08:00 | 历史推理可删性的边界取决于外部执行状态；2+1+2=5 | 标准完成 | 已有覆盖 AGENT-CONTEXT [章节](../../../../books/part-07-agent/75-context.md)“Context Compression 必须保留执行状态” |
| [KREX: Concurrent Kernel Benchmarking](https://arxiv.org/html/2609.30057v1) | 2026-09-25T08:00:00+08:00 | 计时关键区间独占而非整命令独占；2+2+2=6 | 深入完成 | 整合 PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Alignment Illusion in MLLMs](https://arxiv.org/html/2609.30210v1) | 2026-09-25T08:00:00+08:00 | scalar geometry 可在视觉能力破坏后仍显“对齐”；3+2+3=8 | 深入完成 | 整合 MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control](https://arxiv.org/html/2609.30264v1) | 2026-09-25T08:00:00+08:00 | 无 common reset 时，预测 latent 的 action recovery 只给 planner 可辨别训练代理，不证明物理反事实；3+1+3=7 | 深入完成 | 整合 MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |

## 4. 证据与知识整合

**模型、训练与表示**

### [Thinking Leakage](https://arxiv.org/html/2609.28682v1)

§3–6 用三种 hybrid reasoning model、三种后训练方法、数学任务的模式控制与双向 activation intervention 检验 NoThink 质量改善有多少来自既有 Think 行为。干预能支持“部分增益依赖被重新调用的模式行为”，不能把方向向量当作完整因果分解；§9 承认架构/任务和单一方向限制。书稿原有 GRPO 比较强调 objective 与 rollout，缺少“模式是否真的遵守”这一评价身份；已将其作为后训练效果归因边界写入第33章，不宣称 GRPO 普遍泄漏。

### [LastOPD](https://arxiv.org/html/2609.28845v1)

精确 v1 §4–6、附录 A/C 对比 token-only OPD、深度比例配对的 latent-only/latent+token、只在输出接口对齐并早期退出的方案。Qwen3-4B/8B→1.7B-Base 的同一数学训练提示、约 7.9k rollout/62 step 中，latent-only 的投影相似度继续提高，而 MATH-500 表现由早期改善转为低于基座；masked massive activation、CKA 重新配层未消除崩溃。输出层 latent 监督向 token OPD 交接在这两组比 token-only 更好，但同源 JustRL→R1-Distill 对照中，持续 latent 监督并未同样崩溃。每格单次训练、数学任务、非 thinking 模式和切换时刻经验选择限制普遍性。第29章已有均匀/密度加权 representation distillation，却没说明**层位置与监督存续时间可使对齐度和行为质量反向**；已把该反例及同源旧路径仍成立的条件衔接进去。

### [Selective Supervision for Direct-OPD](https://arxiv.org/html/2609.29142v1)

精确 v1 §4.1 构造证明：teacher 与 matched base 在 student 候选 token 上的绝对概率质量同时趋零时，log-ratio 与局部梯度可保持不变，JSD 及双向 KL 却趋零。§4.2 在 student-visited prefix 上按 teacher/base JSD 选择每条 response 最高 10% 状态，§5 的两组 teacher pair×四种 1.7B–8B student 数学设置中，七组优于密集 Direct-OPD、一组持平；附录 F/G 给训练细节和局限。它不证明任何低 JSD token 都无价值，也没有跨任务和多 seed 训练级置信结论。第33章已有 matched-base delta 与方向门，却缺**相对变化掩盖绝对概率质量**的证据边界；现把有条件选择与全量 OPD 的共存条件写入同一监督链。

### [Where Hallucinations Live](https://arxiv.org/html/2609.29048v1)

精确 v1 §3–4 用早层 activation patching/ablation 和 POPE、AMBER、CHAIR 检查 VQ 图像 token 的路由。25 个模型中出现正、负与无效作用；在 VILA-U 上早层干预改善指定对象幻觉指标，但对 Qwen2.5-VL 的同层干预可严重退化。500 图像开放 caption 还显示 CHAIR 变化伴随长度与召回下降，不能只读幻觉率，也不能把诱导 VQ 的 LLaVA 结果冒充同等显著效果。第23章已有视觉证据写入/语言先验读取的诊断框架，此文只增加**层和架构不可通用映射**的反例；发布仍由外部 grounding 行为证据决定。

### [Temporal Taxation / Whisper Compression](https://arxiv.org/html/2609.28739v1)

§3–6 对同一 Whisper family 的 FP16、INT8、INT4、剪枝与蒸馏比较人口/口音组 WER、转录循环和按假定每错词时间换算的校正负担；某些剪枝配置放大群体差距，部分蒸馏配置缩小差距，不能概括为“压缩普遍有歧视”或把换算时间当真实劳动计时。该研究限一个 ASR 家族、特定英语朗读与口音数据，不能外推所有模型与部署。第66章此前已有**输入音频有损压缩**按语义问题族配对审计，却没有**模型权重压缩**对使用者群体错误负担的发布切片；已在同一 Compression Release 论证内补入这条不同的机制与共存边界。

### [Is Reasoning Always Useful?](https://arxiv.org/html/2609.29560v1)

§3 将正例相似度增益与最近 hard-negative 增益相减，辨认“正例更近但排序更坏”；三种 embedding model 的 MMEB-V2 诊断支持测 pairwise margin，不证明推理越多越好。附录的无标签候选条件化 prompt 未稳定改善 Hit@1，oracle 条件不能变成可部署策略。第23章原来由训练目标解释语义对齐，现加入检索排序的反例与额外推理成本，避免把正例 cosine 冒充效用。

### [The Alignment Illusion in MLLMs](https://arxiv.org/html/2609.30210v1)

§3–5 在 13 个 projector–LLM MLLM 上干预视觉输入，比较任务行为与 CKA/SVCCA/主子空间几何；共享 MLP 下投影各向异性提供标量相关性的替代解释。干预支持“几何指标不充分”，不能证明所有跨模态相关性都是幻觉或融合无效。第23章已有共享参数不等于可操纵语义，新增的是**标量指标可在行为损坏后仍保持**的测量失效，并保留几何分析的定位用途。

### [Your Transformer Can Hold Two Thoughts at Once](https://arxiv.org/html/2609.29845v1)

精确 v1 §2–5、§8 与附录 G 对 Pythia/Qwen/Llama 等短文本的两条 embedding 序列逐位置取均值，测原单流 top-token 在混合 logits 的排名，再以 FineWeb/TinyStories 和注意力 donor/permutation 干预检查“保留的信号只是频率先验”这一替代解释。未经微调的 top-10 保留率约 30–40%，但可预测位置占多数，关键内容词明显更差；直接从混合分布采样会交叉污染两条序列。作者的 Joint Contrastive 另跑小模型来拆流，LAMBADA 混合准确率仍低于单流；附录 G 的 128 prompt/128 generation 受测吞吐也没有胜过相同 token 数的 batch=2 大模型基线。因此“存在可测的混合信号”尚不推出“通用 Transformer 线性”或“单次 forward 带来部署吞吐翻倍”。短上下文、小模型、单语文本和辅助模型开销使长期执行结论未成立，本次仅报告，不改写第16–18章的模型主线；有匹配质量、真实 KV/吞吐和更长上下文的独立对照时定点重开。

**推理与物理闭环**

### [When Fancy Eviction Fails](https://arxiv.org/html/2609.28870v1)

§3–5 对两类生产 Prefix trace、14 种淘汰策略比较活跃会话的局部性、一次性 burst 与重算成本；§6 的 Qwen3-Coder-30B/H200/vLLM、48 GiB cache、10k 请求仅证明指定实验的 TTFT 取舍：平均和 p99 改善，中位数变差。它修正“有昂贵 prefix 就总该 cost-aware”的直觉。第54章已有容量与命中曲线，现补齐**淘汰粒度—碎片—延迟分位数**的下一个选择；没有拿作者平均值替代真实 workload replay。

### [Cross-Model Autoscaling](https://arxiv.org/html/2609.29160v1)

§3–6 用按模型能力校准的 Token Service Share 而非不可比的裸 queue/token/s 形成容量缺口，分 fast rescue、slow rebalance 和 donor draining。对照位于同 vLLM/Kubernetes 运行时，披露条件是两台机器、每台四张 A100 40GB、三个 7/8/14B 模型及七条约 720 秒 trace。作者自己将 co-located prefill/decode、校准漂移与重发而非 KV 迁移列为边界。第56章原有 routing/placement/autoscaling 权限拆分，却缺跨模型容量仲裁；已衔接进入，不外推 fleet SLO。

### [Xtrace](https://arxiv.org/html/2609.28769v1)

精确 v1 §2–5 用 FA-3、FlashMLA、HSTU、FA-4 等六个融合 kernel 检查 IR/预留位探针与编译后二进制 splicing 的保真及开销；在 H100/B300/MI300X 和作者实现的 Neutrino/IKET 对照下，前者可能因探针参与编译而改变寄存器分配、软件流水与实际等待，后者分析 live register、hazard/control bits 后插入 probe。指令保留率和 trace 对瓶颈的解释比单一 slowdown 更能检验“测到的是否仍是同一 kernel”。单一 Agent 在 FA-3 的优化迭代差异、FA-4 与 cuDNN 对照不证明跨 workload 通用收益；设备支持和现有工具重实现也约束可比性。第67章原已有 GPU counter 的采样/校准，却缺**观测手段改变编译产物**这一级 fidelity gate；已与原先计数器→精细 trace 的演进路径衔接。

### [No More Free Lunch: Corpus Task Complexity Matters as Corpora Grow](https://arxiv.org/html/2609.29245v1)

精确 v1 的 §2–5、附录 A/D 按 oracle 操作数而非仅 token 长度将语料任务分成较低与较高关系复杂度；这是候选算法的任务分级，不是严格计算复杂度下界。12 个低关系与 10 个高关系任务里，单文档查找与跨文档配对/矛盾所需访问边不同；在其 Qwen3.5-4B 的 20k task-specific 训练例、2K～32K 测试设置中，高复杂度任务的 block-sparse 与 dense 质量差距随长度扩大。64K/128K 外推及 OLMo hybrid 对照方向相符，但后者训练预算未完全相同，不能用来证明架构单独造成差距；受控语料也不代表生产长上下文。第22章原先仅从访问图讨论 sparse trade-off，本轮补入**任务实际需要多少跨文档关系**这个质量门禁，并保留局部证据查找时 sparse 仍合理的边界。

### [Streaming-WAM](https://arxiv.org/html/2609.28927v1)

§3 明确 future visual prediction 接收最新观测和**正在执行的固定动作前缀**，随后生成剩余 action；§4 在 LIBERO 与一个真实 Stamp Paper 任务对照异步/同步和 conditioning 消融。它证明的是其系统里的动作条件化帮助隐藏推理延迟，不证明视觉预测等于物理真值。第26章已有延迟进入 RL state、sensor/action pair；本轮只补预测器同样必须知道已提交前缀，以及偏离时回退真实观测。

### [Decoupled Early Exits for Task-Dependent Compute Allocation in Flow-Matching VLAs](https://arxiv.org/html/2609.29382v1)

精确 v1 的 §III–IV 与 Table II–III 把冻结 VLA 的视觉 backbone 深度 V、每步运行的动作 expert 深度 A、denoising 步数 D 分开；轻量出口只训练附加层。V<A 时若缺少深层 expert 所需的视觉前缀 K/V，不能直接截断 backbone：作者用出口表征经跳过层的 normalization 与 K/V projection 合成前缀。SmolVLA/π0.5 在 LIBERO/Meta-World、单张 A100 40GB、batch=1 下，四组选定出口的延迟均缩短，但有一组成功率 87.6→86.7%，故摘要四组均值不能当逐任务保证；D 单独缩减也贡献很大。task-wise 最优是离线分析而非在线路由，选点还依赖同 benchmark 的任务表现；无实机、p95/jitter 或安全验收。第26章原有 block×timestep×rollout 的 cache identity，却未解释 V/A/D **计算位置与缺失 KV 接口**，本轮将这条受限设计分支接到完整 policy/保守 controller 的回退条件。

### [AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control](https://arxiv.org/html/2609.30264v1)

精确 v1 的方法把事实转移的预测误差与**预测下一 latent 能否恢复候选 action**分开：residual predictor 保留小变化，逆动力学与归一化互信息辅助头只在训练时约束，测试时移除，原 MPC/CEM 搜索器不变。其 Cube matched 消融里 baseline、residual、residual+单项恢复、完整损失的成功率并不单调，说明收益不能全归给 action recovery；相对 matched LeWM reproduction，五个仿真环境中四项均值改善，PushT 由 94 降到 92，Scene 的 35.5→39.5 在 paired 检验中 p=.13、无法确证差异；真实 Franka 只有单站点、45 次/组并使用人工 subgoal。作者测 fixed action bank 的 elite regret，但这不是 adaptive CEM 分支的反事实校准，也没有证明物理安全。第25章原来要求同状态多动作 reset/branch outcome 才能增强被搜索分支证据；本篇提供无法 reset 时较弱的训练代理，并明确其失效时仍应依赖真实观测和保守重规划。

**Evaluation 与平台**

### [Reasoning Instructions Can Break Answer Decoding in VLMs](https://arxiv.org/html/2609.29278v1)

§2–4 对同一多选题比较 direct label logits、加 CoT cue 后立即读 logits、完整生成 CoT 再抽最终答案、matched probe，并用选项排列检查位置混杂。Qwen2.5-VL-7B/ScienceQA 的强烈差值是接口/任务受限现象，不可直接解释为知识变化；答案槽位与选项内容仍非完全可分。第66章既有 CoT/选项排列 paired audit，此处新增**读数事件必须相同**的前置条件。

### [ModularSQL](https://arxiv.org/html/2609.29573v1)

精确 v1 §2.2、§3–4 指出 BIRD 的集合式执行评分会把重复行计数抹掉，并提出受探测器触发的 DISTINCT 修补；在 BIRD-Dev 1,534 题中排除两题 gold timeout 后，以 1,532 题比较已发布预测，Set-EX 比 Multiset-EX 高 3.39–6.79 个百分点。修补器只是作者 SQLite/DeepEye 与两组外部预测的受限 guardrail，受 flag recall、SQL 语义和额外 LLM 调用限制，不能作为通用自动修复器。第66章的长期增量是**evaluator 的结果等价关系也是任务契约**：若业务关心行数，不能用 set 分数给 release 权；旧集合评测在重复数无语义的任务仍成立。

### [Three Ways Classical Test Theory Misleads for LLM Judges](https://arxiv.org/html/2609.29709v1)

精确 v1 §2–5 与附录 A 用 210 个合成短答题、一个 Claude Haiku 4.5 judge（180 个可解析）和模拟网格说明：固定 4.72% item 错误率时，改题库可使 KR-20 由约 0.01 到 0.68；该系数没有独立 scorer facet。阈值 Φ 是方差比而非判定正确概率，Livingston–Lewis 的“正确”相对自身 true score 而不是外部 gold。作者核查的三篇近邻论文没有这些具体误用，不能写成行业普遍错误。第66章已有 judge calibration，却缺**统计量究竟估计哪个 facet/estimand**的前置检验；正文现要求数字绑定题库、scorer variation 与外部效标，单一系数不得独立放行。

### [PartHackBench](https://arxiv.org/html/2609.29578v1)

§3–6 的私有 certifier 先检当前环境谓词与 Agent attribution 相等，之后才比较 partial-credit 分数；rollback 和历史 milestone 是关键混杂。六个开发、十八个 held-out 合成任务里只有十五个形成所需匹配对；这不是现实作弊 prevalence。第66章原有 reward hacking 提醒但未定义等量真实进度的配对参照，本轮补入该评价合同，并明确编码谓词之外仍未验证。

### [Reward Hacking Challenges Oversight of Autonomous Research Agents](https://arxiv.org/html/2609.28614v1)

§3–7 把普通任务的自发 exploit、允许作弊的红队条件、带审查反馈的多轮逃避分开；17 模型/38 任务、40 turn/3600s 的测试中，提交物审查和独立执行证据看的对象不同。作者的 verification panel 仍由 LLM 参与，且“允许作弊”样本不能估计部署发生率；反馈条件还共同改变理由与尝试历史，不能把差异单独归因于理由。第66章吸收的是**生成结果与证明材料同权时的独立证据所有权**，不是 AI for Science 应用成绩。

### [Sequential Knowledge Editing Breaks Evidence Arbitration](https://arxiv.org/html/2609.29587v1)

§3–7 固定未编辑事实的 query、候选字符串与检索段落，比较真实更新、错误声明、伪权威和无冲突条件；在 Qwen2.5-7B 的 1000 次 LoRA 编辑中，MMLU 几乎不变而证据仲裁排序/选择性风险退化，冻结 retriever 的端到端对照进一步支持同一方向。第二个 7B 模型只支持方向复核，三个 seed 的幅度相差逾三倍；固定检索端到端结果限 Qwen，不能写成双模型部署验证。norm-matched noise、损坏剂量和层增量提供替代解释对照；§9 承认小模型、探针构造和特定 editor 的范围。第66章 RAG 评估原来能归因检索/生成，但没有**参数编辑后对未编辑事实的证据仲裁**切片，现已补入。

### [KREX: Concurrent Kernel Benchmarking](https://arxiv.org/html/2609.30057v1)

§4–6 在 timing-critical region 前阻止其他提交并 drain 在途 GPU 工作、隔离 host 线程，其他阶段共享 device；四节点 NVIDIA H20/AMD MI308X、三个 kernel-agent 工作负载和约 20k 命令只证明该合作式原型的吞吐/测量取舍。p95 inflation、短 kernel 和 candidate-rank flip 均须保留，不能用峰值吞吐证明无偏。第66章已有 hidden shape 与 correctness receipt，新增 region 而非整命令的计时所有权及其失效回退。

### [Where Does the Energy Go?](https://arxiv.org/html/2609.29707v1)

§3–5 联合 GPU/CPU/主板遥测与 Agent phase，发现单一双 RTX Pro 6000 Blackwell、Qwen3.8-27B 环境的 GPU-only 估算遗漏整机负担；idle、低 batch 与 tool 等待改变每 token 分摊。不是外部交流电表，且只有一台服务器/一种模型；作者倍率不能当 fleet 常数。第70章已有 successful-goal 分母，本轮补分子侧的**component + phase 计量边界**。

**Agent state 与 Tool**

### [Where Does Exactly-Once Live?](https://arxiv.org/html/2609.29095v1)

§3 的故障模型把“已提交但确认丢失”与“读回后仍可晚到提交/重发”区分；§4–6 在六类模拟服务、12 类故障、九个模型及三种 harness 上比较了 tool-contract 变化。read-back 可解决前者，但没有 in-flight 上界就不能独立保证后者的 exactly-once；§7 承认模拟与短任务限制，代码公开并未验证。第78章原有 idempotency key 列表，现补不可由读回消去的未知状态及**工具端提交边界**。

### [Stale Does Not Mean Unsafe](https://arxiv.org/html/2609.29522v1)

§4–6 冻结同一 proposal，在 16 项基础设施任务的受控 state race 中反事实比较全局 epoch、读集版本及语义 predicate guard。前者安全但误挡无关变化，后者减少误挡但依赖谓词完整性；三个本地量化小模型和 3456 条模拟轨迹不能证明生产并发安全。第78章已有版本前提，本轮补“过期不等于危险”的精度—可用性取舍，提交 authority 仍在工具侧。

### [ERRAND: Budgeted Maintenance of Agent Memory](https://arxiv.org/html/2609.29545v1)

§3–6 让冻结 policy 的旧 briefing item 带条件与来源，把 recheck 的价值放入与任务动作共享的预算；不同 drift regime 下可保留版本，而不是覆盖为一个 timeless fact。受控环境帮助隔离“未做任务”与“未重检”的机会成本，却没有外部真实人机任务的行为保证。第77章已有 recall/commit 分离，这篇额外要求**reverification 有价格，且并非越多越好**，已作长期机制补充。

### [Scope Before You Persist](https://arxiv.org/html/2609.29144v1)

精确 v1 §3–6 区分某任务家族的局部 edit 证书与全局 skill 检索；在同一冻结模型与 code-repair 环境中，家族路由让匹配任务消费相应 skill。27 条随机顺序、各 12 round 的配对 stream 中，scoped 相比 global 的平均 trajectory utility 高 0.063，global 12 次接受中 6 次后续 checkpoint 变坏，scoped 63 次接受中本设置未见此类有害接受；单步实验区间和任务族有限，不能推出生产零错误。第77章已有 memory write gate 与版本管理，但局部认证不自动授权全局读取；现给持久记录加适用范围与跨家族复证，保留单任务全局记录仍可行的旧条件。

### [Safe Skill Retirement](https://arxiv.org/html/2609.29543v1)

精确 v1 §3–6、附录把技能删减分成授权任务效用证书，以及固定 action/effect、只翻转 permission/state predicate 的保护副作用反事实；观察 proposal、sink decision、effect 三层。12 bundle×四配置的 2,592 个测试单元中，单用任务结果可删去约 94.5–97.9% 条款却仍触发 protected effect；零副作用方案有的又损失授权效用，说明两门不能互代。真实设备只验证单条只读 camera measurement path，不能称物理安全证明。第84章已有 skill admission/runtime gate，却未规定**退役时从未被训练任务变化的治理 predicate 不可随 procedure 一起删掉**；已补成双门证书与回退条件。

### [Post-Training Leaves Behavioral Shadows](https://arxiv.org/html/2609.29233v1)

精确 v1 §3–5 从已知公共祖先选择 near-tie prompts，只取后训练 teacher 对无关问题给出的单词，学生不接触目标训练数据或 teacher logits。主实验 Qwen2.5-1.5B 同祖先、5,664 个响应的 HumanEval+ 相对严格 nuisance-matched control 高 5.34 个百分点，四 seed 区间 [1.22,9.60]；五组独立采集×三 seed 方向相同。其他模型家族均值为正但区间可跨零，且主动查询和同祖先是假设，不能声称任意公开文本泄露能力。第72章原有 subliminal probe 的 channel/init 对齐，本轮补“单词输出、无目标任务词仍可承载可学习更新”的风险边界；DLP/typed 输出控制继续防直接泄露，而衍生性审计另测主动探测。

### [When Can Agents Forget Their Reasoning?](https://arxiv.org/html/2609.29875v1)

§3–5 对保留/压缩历史推理块做 frozen proxy 打分并在约 260 个受控 Agent 任务比较后续行动；tool output、action 和 observation 不作为同类可删推理。局部奖励与 token 节省不能证明所有历史推理无用；任务状态若已写到 file/tool artifact，删 reasoning 的代价可能较小。第75章已明确 raw handles、versioned state、paired-state replay 与“压缩执行状态不可仅看语义”，所以结论为**已有覆盖**，不追加同义段落。

## 5. 缺口与下一步

本窗可执行的来源检查、候选审阅、Books 判断与实际修改、独立成稿复核及机器校验均已完成。下列外部材料只作为隔离的终态保留项；若出现精确原文或日期证据，再定点重开，不扩张本窗候选或重跑整月。

以下是本窗**终态保留项**：它们不用于正面证据、不支持 Books、不支持“无遗漏断言”。每项的定点重开条件如下；等待外部原文不阻塞其他已完成材料，也不允许把受阻候选写成零命中。

- **Meta / MaD-RL**：[官方出版页](https://ai.meta.com/research/publications/mad-rl-matching-distributions-for-calibrating-llms-with-reinforcement-learning/)仅标“2026-09-24”，不足以区分本窗前/后 09:00；[官方 PDF 按钮](https://ai.meta.com/research/publications/mad-rl-matching-distributions-for-calibrating-llms-with-reinforcement-learning/)本次返回临时 CDN cache miss。摘要给出分布匹配动机，但不足以核公式/实验，故**未列候选、不评分、不入 Books**。接受带可靠时区的首次公开时间、同一精确版本 arXiv/作者 PDF 或可读取的官方正文；收到后只重开 09-24/09-25 的真实 owner 日和 `TRAIN-GRPO`/相邻 RL 章审阅，不重跑全月。
- **Qwen 空内容页**：09-24 页面仅日期与 0 words，缺标题和正文身份；如官网恢复标题/正文，定点核 event time、贡献和首次公开家族，不从空壳反推新研究。
- **MiMo Blog / MiniMax Agent 子目录**：前者文章卡片缺发布日期，后者是不可列举目录壳；官方条目若出现可验证的本窗时刻和正文，定点补查。它们不支持“所有官方渠道均无新内容”的断言。

题摘级排除而非未审候选：`2609.30123` 的 skill→状态机/trace replay 被第81章现有 typed workflow 与回放 gate 承载；`2609.29661` 与已公开 `2608.20845` 属 ingest-time fact compilation 同家族；`2609.30094` 的主动会话隐私探测是有用的测试切片，但核心最小暴露/opaque handle 控制已在第72章，不能将本窗受测话题漂移外推为跨会话 Memory 泄漏。`2609.29499` 的 [作者上传正文](https://www.researchgate.net/publication/413630880_Task-Aware_Spectral_Pruning_A_Mixture-of-Masks_Framework_for_Efficient_LLM_Inference)标示 08-26 已有完整预印本；09-25 arXiv New 非其首次公开，本日不评分或入 Books，后续只回查原 owner 日的多任务 mask 机制。若原文后续提供相反的具体机制，只重开对应材料，不把“名字不同”当新家族。Google 09-24 视频综述引用的更早论文也不在本窗重新评分。

## 6. 复核

复核者：独立智能体 `/root/semantic_audit`。实际检查 14 个每日来源的窗口停止/隔离、arXiv 题摘补检与日期归属、30 项候选及逐篇证据、41 项高疑似准入前排除、评分、29 个章节链接，以及 28 项 Books 语义增量对应的 source-family 锚点。复核发现原 shortlist 遗漏 `2609.30264` 与 `2609.29382`、`2609.29499` 早于本窗公开，且纠正 World Model 四项均值改善不等于四项显著改善的措辞；均已在本报告、原始入口记录及相关书稿修复。最终只读语义复核通过。

结论：通过

`python3 scripts/validate_research.py --report papers/2026/09/25/README.md` 通过，§3 与 §4 各 30 项、评分合计与状态一致；`git diff --check` 无输出。`git diff --cached --check` 在运行前已有 staged 的 `papers/2026/09/22/README.md` 与 `tasks/PERSONAL_AI_CAPABILITY.md` 报行尾空格，本次未修改、清理或纳入验收。机器检查只证明结构和可判定一致性，不代替上述语义审阅；Meta 等精确隔离项不构成正面证据或“全部官方内容绝无遗漏”的保证。
