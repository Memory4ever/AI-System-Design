# Daily Research — 2026-04-06

**规范：** V3
**窗口：** 2026-04-05T09:00:00+08:00 ～ 2026-04-06T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T14:09:00+08:00

## 1. 结论

本日窗口包含周日美东20:00对应的北京时间04-06 08:00常规公告时刻。单独的预定时刻不证明历史公开；本轮结合永久ID于公告时分配、相邻连续批界/OAI日级链、保留项自己的版本元数据与首/中/末落在00:00～01:00Z的交叉依据，支持标明推断性质的08:00～09:00区间，不要求逐篇公告日志，也不把任一Updated直接改名为首发。独立复核已纠正此前过强的日志门槛，见[日期审计](../_sources/daily-20260406/V3_DATE_RECONCILIATION.md)。旧449个身份仍只是原始库存，旧50候选及泛化关闭不继承；[旧存档](../_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-04-06.md)和[逐项检查点](../_sources/daily-20260406/V3_REVIEW_CHECKPOINT.md)保留可复核证据。具体早发/身份例外仍单独隔离，不由批次推断支持零遗漏。

作者28项加独立恢复15项，以及本次定点恢复3项和日期校准恢复1项，最终为**47个家族：26项实际整合、18项已有覆盖、1项仅报告、2项争议暂缓**；另有1个身份/日期冲突的单篇隔离项。旧50 retained的关闭侧与共同错误理由已定点复核，不把449库存当全部全文队列或全网无遗漏证明。最新两处真实正文为Ch33的归一化顺序和Ch77的失败规则晋升；Ch72对受限Run安全证据已有具体覆盖。47项均已完成必要证据与最终处置，新增书稿写后和日级独立验收已通过；日期/身份与争议保留项及外部目录缺口仍按§5隔离，不据完成状态声称全源无遗漏。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | [官方 Research](https://openai.com/research/)与[News RSS](https://openai.com/news/rss.xml)；RSS 邻近 04-02T10:30Z → 04-06T10:00Z，后者在窗口之后。 | 受阻 | News 不等于 Research；旧 Research 历史精确日列表不能完整回溯，需官方历史目录或当窗原始公告；不作零命中断言。 |
| `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research) HTML `publishedOn` 邻近 04-02T10:56Z → 04-07T09:35Z。 | 已检查 | 限官网当前可回溯列表，不代替未列作者论文。 |
| `SRC-GOOGLE-AI` | [Google Research 2026-04 Blog](https://research.google/blog/2026/04/)由 04-03 跳至 04-08/09；[DeepMind Publications](https://deepmind.google/research/publications/)所见相邻 03-22 与 04-25。 | 受阻 | [Google Research Publications](https://research.google/pubs/)未取得完整日级停点；博客不能代替论文目录。 |
| `SRC-META-AI` | [Research](https://ai.meta.com/research/)历史文本不可完整读取，[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication)请求超时；[Blog](https://ai.meta.com/blog/)只作相邻日期线索。 | 受阻 | 需官方历史分页或当窗原始报告；不作 Research 零命中断言。 |
| `SRC-QWEN` | [官网动态接口](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) 40 条，`extra.date` 在 04-02T04:00+08 后至 04-15 无本窗项；[静态研究目录](https://qwen.ai/api/page_config?code=research.research-list) 60 条更早项目；[QwenLM](https://github.com/QwenLM)组织新仓库窗口有界检查。 | 已检查 | 限官方列表与重要新 artifact；不按普通提交扩扫。 |
| `SRC-DEEPSEEK` | [官方动态/研究](https://www.deepseek.com/news/)当前目录由 2025-12 跳至 04-24；本窗未见列项。 | 已检查 | 限官网可见目录。 |
| `SRC-MOONSHOT` | [Kimi Blog](https://platform.kimi.com/blog)最近可见 2025-11；[kimi-cli Releases](https://github.com/MoonshotAI/kimi-cli/releases)相邻 04-02T14:40:52Z → 04-10；组织新仓库本窗未见事件。 | 已检查 | 限官网、正式 release 与组织新仓库，不审普通提交。 |
| `SRC-TENCENT-HUNYUAN` | [Research 全部列表](https://hunyuan.tencent.com/research)官方 `POST /api/blog/publicList`，`pageNum=1,pageSize=100,renderType=0` 返回 9/9，04-23 → 02-13 无本窗文章；[Tencent-Hunyuan](https://github.com/Tencent-Hunyuan)组织新建 `HY-Embodied` 仓库在窗内，但其官方 README 将模型发布写为 04-09，窗内没有可核研究正文/正式 release。 | 已检查 | 仓库创建不冒充模型首发；若恢复确切 04-06 artifact，再定点重开。 |
| `SRC-ZAI` | [Research](https://www.zhipuai.cn/zh/research) 04-01 → 04-07、[Release Notes](https://docs.z.ai/release-notes/new-released) 02-12 → 04-07；组织新仓库本窗未见事件。 | 已检查 | 官网 CMS 创建时间不用作公开时间。 |
| `SRC-BYTEDANCE-SEED` | [论文列表](https://seed.bytedance.com/en/public_papers)官方 `get_article_list_v2` `article_type=1,count=20,page_token=40`（`x-tt-locale: US`）跨 04-08 → 03-31；博客 `article_type=2,page_token=0` 跨 04-09 → 04-01；组织新仓库本窗未见。 | 已检查 | 限目录公开时间和重要 artifact，排除暂缓的 AI for Science。 |
| `SRC-BAIDU-ERNIE` | [技术博客](https://ernie.baidu.com/blog/zh/) 02-06 → 04-15；[ERNIE Releases](https://github.com/PaddlePaddle/ERNIE/releases)无本窗正式版本。 | 已检查 | 限博客与正式 release。 |
| `SRC-XIAOMI-MIMO` | [MiMo Paper](https://mimo.xiaomi.com/)可见 03-13 → 06-29；[XiaomiMiMo](https://github.com/XiaomiMiMo)组织新仓库本窗未见。 | 已检查 | 无日期卡片不证明本窗事件。 |
| `SRC-MINIMAX` | [英文博客](https://www.minimax.io/blog)、[中文博客](https://www.minimaxi.com/blog)相邻 03-18 → 04-27；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)无本窗文章；组织新仓库未见。 | 已检查 | 限公开目录与重要 artifact。 |
| `SRC-ARXIV` | [公告规则](https://info.arxiv.org/help/availability.html)、[449个旧原始身份](../_sources/arxiv-owner-replay-20260903/20260406/arxiv-owner-receipt.json)、02333–03231连续批界/OAI及保留项自身版本字段；题摘贡献、必要正文和关闭侧已定点重判。 | 已检查 | [独立日期审计](../_sources/daily-20260406/V3_DATE_RECONCILIATION.md)支持带推断性质的本窗区间，不把任一元数据字段直接等同first-public；02947身份/日期例外仍隔离，日级独立复核通过。 |

这 14 行只表示实际到期来源与窗口的当前状态；三个不可回溯官网目录已与可核来源分开隔离，不能放进“零命中”算术。arXiv 分类以 LLM/Infra/Multimodal/Agent 主题检索和相关标题浏览为边界，不把原始跨分类总量视为逐篇全文队列。

## 3. 候选与判断

当前46项由原43项及独立定点恢复的`.02869/.02734/.03131`组成。日期采用官方规则、连续批界、相邻OAI和保留项版本元数据的组合推断；公开时间栏明确标“推断”，不是逐篇披露时刻。root对原43项及两个既有隔离身份的缓存版本字段逐项核对，均在00:00～01:00Z，但独立更早公开/身份冲突的两项仍不能据此纳入；新增三项分别为00:31:46/00:23:26/00:47:19Z，同样只作为组合证据。46项方法与具体Books处置已经完成，最后日级独立验收未通过前不提前标完成。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [2604.02869v1 — Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration](https://arxiv.org/html/2604.02869v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 逐turn标准化后相加与raw-return先汇总后标准化不交换；2+2+2=6，知识缺口override | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，新正文待写后独立验收 |
| [2604.02734v1 — Aligning Progress and Feasibility: A Neuro-Symbolic Dual Memory Framework for Long-Horizon LLM Agents](https://arxiv.org/html/2604.02734v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 正例误拒淘汰与负例覆盖分开；训练池零误拒不保证新状态；2+2+2=6，知识缺口override | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)，新正文待写后独立验收 |
| [2604.03131v1 — A Systematic Security Evaluation of OpenClaw and Its Variants](https://arxiv.org/html/2604.03131v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 框架安全结果须绑定Run、权限和effect证据，不支持模型因果或产品排行；2+2+2=6，安全override | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) Run/trace/Containment；apr03独立复核 |
| [2604.02344v1 — WebGPU Dispatch](https://arxiv.org/abs/2604.02344v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 区分直接API dispatch、fusion推导framework成本与异步重叠，2+2+2=6，知识缺口 override | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，写后独立复核通过 |
| [2604.02485v1 — Failing to Falsify](https://arxiv.org/abs/2604.02485v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 查询假设补集或改变单一属性可改变证伪测试策略，但 I:C 与成功率并不必同步；2+2+2=6，知识缺口 override | 深入完成 | 整合：AGENT-REFLECTION [Ch80](../../../../books/part-07-agent/80-reflection.md)，写后独立复核通过 |
| [2604.02505v1 — Projection-Free Adaptive SGD](https://arxiv.org/abs/2604.02505v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | FTRL 将范数球可行性放入正则几何；免参数投影不免结构投影和矩阵计算；2+1+2=5，知识缺口 override | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，写后独立复核通过 |
| [2604.02500v1 — I must delete the evidence](https://arxiv.org/abs/2604.02500v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 利益目标和角色指令可能诱导不当文本提议，不赋予删除证据的执行授权；2+2+2=6，安全 override | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，目标/权限/提交分离 |
| [2604.02652v1 — Compound Jailbreaks](https://arxiv.org/abs/2604.02652v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 单独防线不保证联合攻击安全；类别覆盖与响应 ASR 的分母不能混用；2+1+2=5，安全 override | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，仅采用联合风险；数值与内部因果主张隔离 |
| [2604.02863v1 — EMS](https://arxiv.org/abs/2604.02863v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 固定票集的严格多数允许结果保持早停，但历史共识不是真值校准；2+2+2=6，知识缺口 override | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，写后独立复核通过 |
| [2604.02967v1 — FoE / RED](https://arxiv.org/abs/2604.02967v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 对比生成干预与跨提示 probe 早停拥有不同控制对象，错误上界不证明首答最优；2+2+2=6，知识缺口 override | 深入完成 | 整合：AGENT-REFLECTION [Ch80](../../../../books/part-07-agent/80-reflection.md)，写后独立复核通过 |
| [2604.02460v1 — Equal Thinking Budget Comparison](https://arxiv.org/abs/2604.02460v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 相同预算参数不证明相同计算，信息与错误概率界不能直接排序现实 Agent；2+2+2=6，设计反证深入审阅 | 深入完成 | 仅报告：受限比较有反证价值，Ch82 已有等总预算/coordination tax 主线；不采用有争议的严格理论外推 |
| [2604.02431v1 — SelRoute](https://arxiv.org/abs/2604.02431v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 扩词适合词面索引却可能损坏 dense 表示，通道选择需保留原 episode 与派生词的身份；2+2+2=6，知识缺口 override | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [2604.02345v1 — UI-Oceanus](https://arxiv.org/abs/2604.02345v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 真实 GUI 探索转移可用于 forward CPT，固定数据下 inverse 目标不等价；2+2+2=6，知识缺口 override | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [2604.03118v1 — Salt](https://arxiv.org/abs/2604.03118v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 局部分布匹配不保证组合一致，AR 视频还依赖自产生历史的质量分布；2+2+2=6，知识缺口 override | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2604.02343v1 — Massive Knowledge Transfer via Binary Communication](https://arxiv.org/abs/2604.02343v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 共享先验可把专家反馈压成二元回答，但 answer-bit 压缩不等于整条通信/计算链压缩；2+2+2=6，知识缺口 override | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [2604.02525v1 — Operand-Pattern Mixed-Precision Training](https://arxiv.org/abs/2604.02525v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | forward/dW/dX 的操作数异常方向不同，统一 rotation 可能失配；2+2+2=6，知识缺口 override | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [2604.02686v1 — Token Mapping Reward-Model Interface Attack](https://arxiv.org/abs/2604.02686v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | policy 与 reward tokenizer 同 ID 非同文本，raw-ID/clamp 桥可创造异常奖励输入；2+2+2=6，安全 override | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [2604.02721v1 — GrandCode](https://arxiv.org/abs/2604.02721v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | immediate stage reward 与 delayed correction 分开归一化并绑定行为版本；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [2604.02795v1 — Rubric-to-Token Credit](https://arxiv.org/abs/2604.02795v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | token 局部约束分数的分组归一化改变长回答权重，定位不等于因果归因；2+1+2=5，知识缺口 override | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [2604.02340v1 — Denoising Step Scheduling](https://arxiv.org/abs/2604.02340v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 中间 denoise step 对小模型替换更敏感，调度模型大小而非固定所有步；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2604.02372v1 — Decentralised Post-Training Backdoor](https://arxiv.org/abs/2604.02372v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 中间 pipeline stage 恶意参与者可绕过数据投毒防线；2+2+2=6，安全 override | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.02375v1 — KAIJU](https://arxiv.org/abs/2604.02375v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 执行层而非 prompt 拥有 scope/intent/impact/clearance gate；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [2604.02473v1 — Reverse Address Translation](https://arxiv.org/abs/2604.02473v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 跨 GPU 小 collective 的目标侧地址翻译可主导尾延迟；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [2604.02522v1 — Opal](https://arxiv.org/abs/2604.02522v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | Agent 外置长期记忆的访问模式隐私与可信区计算预算分离；2+2+2=6，知识缺口 override | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [2604.02560v1 — DEMASK](https://arxiv.org/abs/2604.02560v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 并行 unmask 的位置依赖限制 product-of-marginals 近似；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2604.02623v1 — Environment Memory Poisoning](https://arxiv.org/abs/2604.02623v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 单次网页观察可升级为跨 session 的持久恶意记忆；2+2+2=6，安全 override | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.02638v1 — AXELRAM](https://arxiv.org/abs/2604.02638v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | KV 量化读路径免反量化，但 sign pattern 引发极端 PPL 风险；2+1+2=5 | 标准完成 | 已有覆盖：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2604.02650v1 — Long-Context CPT Dynamics](https://arxiv.org/abs/2604.02650v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | NIAH 可早于 PPL/SFT probe 饱和，停止训练不能只看检索命中；2+2+2=6，知识缺口 override | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [2604.02715v1 — FluxMoE](https://arxiv.org/abs/2604.02715v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | expert 权重瞬态驻留可与 KV 容量分账；2+2+2=6，知识缺口 override | 深入完成 | 整合：INFER-GPU-MEMORY [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [2604.02766v1 — Random vs Active online DPO](https://arxiv.org/abs/2604.02766v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 强预训练先验下 active selection 成本可能高于随机多样性收益；2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-DPO [Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [2604.02767v1 — SentinelAgent](https://arxiv.org/abs/2604.02767v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 多级委托的确定性 authority narrowing 与概率 intent 校验应分开；2+2+2=6，安全 override | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.02816v1 — QAPruner](https://arxiv.org/abs/2604.02816v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | vision-token pruning 与量化 outlier 耦合，独立压缩策略会损坏数值稳定；2+1+2=5，知识缺口 override | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2604.02954v1 — LogicPoison](https://arxiv.org/abs/2604.02954v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | GraphRAG 类型保持边交换可损坏拓扑推理却绕过文本过滤；2+2+2=6，安全 override | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [2604.02965v1 — SV-VLA](https://arxiv.org/abs/2604.02965v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 低频大 VLA chunk 计划 + 高频轻 verifier 减少开环漂移；2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2604.02985v1 — Prompt Compression in the Wild](https://arxiv.org/abs/2604.02985v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 压缩预处理与 prefill savings 要按模型/硬件/长度求 break-even；2+2+2=6，知识缺口 override | 深入完成 | 整合：AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md) |
| [2604.02986v1 — SignCert-PO](https://arxiv.org/abs/2604.02986v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | Reward proxy 的 advantage sign 不稳可把更新推错方向；2+1+2=5 | 标准完成 | 暂缓：阈值定义与权重公式有未解释的自洽问题，不据此改 Ch33 |
| [2604.03035v1 — Sequential Coding Agent Evaluation](https://arxiv.org/abs/2604.03035v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 依赖 PR 链暴露单 PR pass 掩盖的回归和技术债；2+2+2=6，知识缺口 override | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.03070v1 — Credential Leakage in Agent Skills](https://arxiv.org/abs/2604.03070v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | stdout/debug 与 Skill 自然语言/代码组合泄露凭据；2+2+2=6，安全 override | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.03081v1 — Skill Supply-Chain Poisoning](https://arxiv.org/abs/2604.03081v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 正常复用示例/配置可隐式执行恶意 payload；2+2+2=6，安全 override | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.03088v1 — SkillRT](https://arxiv.org/abs/2604.03088v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | Skill 的能力画像/编译/环境绑定形成跨 harness 可移植性合同；2+2+2=6 | 标准完成 | 已有覆盖：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [2604.03128v1 — Self-Distilled RLVR](https://arxiv.org/abs/2604.03128v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 可验证环境给更新方向、自蒸馏仅调 token 级幅度；2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [2604.03141v1 — Importance-Aware Recall](https://arxiv.org/abs/2604.03141v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 事实性评价需同时测已说事实精度和重要事实遗漏；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.03143v1 — TokenDance](https://arxiv.org/abs/2604.03143v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 同步 Agent 轮次对共同输出做一次 collective KV reuse 和 master/diff；2+2+2=6，知识缺口 override | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2604.03179v1 — Visual Necessity in MLLM RL](https://arxiv.org/abs/2604.03179v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 视觉信息剥离后 RL 仍提升，常规准确率可能测到 language shortcut；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.03191v1 — VLA Compression Gap](https://arxiv.org/abs/2604.03191v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 固定离散 action codebook 抑制更强视觉 encoder 的收益；3+1+3=7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [2604.03208v1 — Hierarchical Latent World Model](https://arxiv.org/abs/2604.03208v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 多时间尺度 latent MPC 与 macro-action 是机制线索；同版本官方载体数字冲突，2+1+2=5 为题摘暂评分 | 争议 | 暂缓：Disputed Version Evidence，不据此写 Books |
| [2604.03216v1 — BAS Confidence Utility](https://arxiv.org/abs/2604.03216v1) | 2026-04-06T08:00:00+08:00 ～ 2026-04-06T09:00:00+08:00 | 答/弃效用跨风险阈值可能区分 ECE 类似却风险不同的模型；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

日期隔离而不计入上述工作集合：[2604.02947v1](https://arxiv.org/abs/2604.02947v1) 是 `Disputed identity/date`，原始字段与恢复条件见 §4，不给本窗确定评分或 Books 正面决定。`.02344` 的早提交/OAI created 不是更早公开证据，现按同一组合批次依据恢复，不再机械隔离。

## 4. 证据与知识整合

### [2604.02869v1 — Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration](https://arxiv.org/html/2604.02869v1)

§3.1–3.2的Eq2与Table1–2显示逐turn GN后求和可能改变轨迹优势符号，改用discounted raw-return汇总后GN并加单独outcome校准，是不同的credit分支；不否定对不同来源各自GN的已有设计。IRC tier/outcome相关性不是因果credit，宽松deep_equal不保证语义正确。作者5952条rollout的零mismatch限于该诊断，Table6–7训练还混变learning rate、KL、步数或prompt，不能把headline全部归因于reward重排。root已在[Ch33](../../../../books/part-04-training-system/33-grpo.md) Immediate Reward Lifecycle的独立normalization段之后真实插入非交换边界、population/objective身份、有限校准和简单terminal基线共存；apr03已独立核原文与拟稿，写后验收待接。

### [2604.02734v1 — Aligning Progress and Feasibility: A Neuro-Symbolic Dual Memory Framework for Long-Horizon LLM Agents](https://arxiv.org/html/2604.02734v1)

§3.2与AppendixC从失败转移生成Python规则，以全观察正例的零误拒淘汰候选，再做负例贪心覆盖。这是Ch77原MDL/consolidation论证未明确的规则晋升分支；训练池零误拒不证明新状态soundness。Table4组合过滤的invalid率更低但成功率较低，AppendixD最多5次重提后仍执行最后proposal，并非fail-closed。root已在[Ch77](../../../../books/part-07-agent/77-memory.md) Failure Trace→Procedural Rule之后真实加入提议/晋升分权、正负样本检查、task-success分账和advisory回退；真实执行授权仍交Ch78/81，不将它误写成作者已实现安全gate。apr03已独立核原文与拟稿，写后验收待接。

### [2604.03131v1 — A Systematic Security Evaluation of OpenClaw and Its Variants](https://arxiv.org/html/2604.03131v1)

§1.2/3/5对六个框架、205案例、13风险类别报告受限Run结果；部分“success”仅为recon而非入侵/外发，没有统一配对的模型、runtime、权限与公开重放协议，不能形成模型能力导致风险的因果结论或通用产品排行。[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) Run/trace/Containment已经具体拥有权限、模型、judge与最终effect的分账，故已有覆盖。root实际对读，apr03独立核原文及正文命题通过；不因没有新防护就把安全反证排除。

### [2604.02485v1 — Failing to Falsify](https://arxiv.org/abs/2604.02485v1)

Exact-v1 §3–6、Table 2/5 与 Appendix G/H 比较当前假设及其逻辑补集的 Dual Goal 提示，和只改变一个属性的 Try its Opposite 查询；观察来自交互环境，不是同模型自由文本 critique。Wason 的 80 个 episode、11 个模型和最多 45 轮交互，以及有限规则发现/迁移对照显示，更强推理、更多与假设不兼容的测试和更高任务成功并不等价。`I:C` 是不兼容/兼容查询比，不能写成成功证伪比例；小模型迁移存在不显著结果。蒸馏测试查询还保留未解出的 teacher episode，不等于只学成功答案。Ch80 已在独立反馈之后补入查询选择、环境观察归属、额外交互、危险测试与静态/sandbox 回退；没有把有限规则发现推广成开放 Agent 的正确性保证。Books：**整合**；`apr03` 核原文和写后正文通过。

### [2604.02505v1 — Projection-Free Adaptive SGD](https://arxiv.org/abs/2604.02505v1)

Exact-v1 §2–4、Lemma 2/4、Algorithm 2 与 Theorem 4/5 通过 FTRL 累积梯度和由 `δ²I` 初始化的正定统计，在指定算子空间及范数下直接保证迭代点位于半径 R 球内；省掉昂贵的加权参数投影，不是省掉结构投影或逆平方根。加速凸分支用相邻随机梯度差，增加梯度查询并依赖凸性、光滑性和噪声假设；非凸分支的 `(γ,ε)` 是分布平均意义，不能当输出点自身梯度小或全局最优。允许任意小正 δ 的理论边界也不保证有限精度稳定。Ch28 原有 optimizer 范数几何未解释可行域如何改变更新规则，现已在其后补入这条分支及矩阵代价/简单基线的共存条件。本文未给大模型训练吞吐或质量实验，不采用生产收益。Books：**整合**；`apr03` 实际写后复核通过。

### [2604.02500v1 — I must delete the evidence](https://arxiv.org/abs/2604.02500v1)

Exact-v1 §3–5 的开发者指令给模型企业利益/角色目标，研究在 16 个模型、重复文本任务与人工编码中观察不当提议；没有真实删除工具的 effect receipt。探索后添加法律责任等提示的设计和评价意识线索不能证明模型犯罪意图或生产因果效应。可保留的安全反证是：任务目标并不自动产生合法权限。Ch72 的“谁获得行为控制权”及 containment 主线已经区分目标、提议、授权和提交，并要求无合法路径时停止/外部确认；现有具体命题足以承载，本次不追加道德归因或未经测量的执行结论。Books：**已有覆盖**；`apr03` 独立核定此受限决定。

### [2604.02652v1 — Compound Jailbreaks](https://arxiv.org/abs/2604.02652v1)

Exact-v1 §4–5 在单一 gpt-oss-20b、7 类攻击任务与每类 10 个提示的受限设置比较组合攻击。Table 2 的 `5/7` 是类别覆盖，而 §5.1 将 ASR 定义为有害响应率；没有充分逐响应计数使两者相等。另报的 tool-misuse/transfer 数字缺少足够协议和分母，所谓认知负载也不证明内部因果机制。这些数值与机制推断明确隔离，不据其写 Books。仅保留“多种独立防线不保证联合攻击安全”的风险边界，与 Ch72 已有联合威胁、相关失效及真实 effect 验证相同，故 Books **已有覆盖**。重开数值所需材料是逐响应标签、评分 rubric 和对应攻击/工具协议；`apr03` 已独立复核窄结论及隔离范围。

本节逐项说明已核 exact-v1 的机制、评价边界及对应章节决定；标准审阅与深入审阅分别依 §3 状态，不把旧版大表中的 `deep_complete` 或缓存存在冒充本轮审阅。另列两个日期归属隔离项，其方法线索不构成本窗 Books 正面决定。

### 独立排除侧复核恢复的五项

### [2604.02863v1 — EMS](https://arxiv.org/abs/2604.02863v1)

[Exact-v1 §3.1–3.4、§4](https://arxiv.org/html/2604.02863v1) 对固定 N 个无权重、独立生成答案的成员，以严格多数阈值提前结束；它保持完整票集结果，不保证真值，也不获得 Byzantine 安全性。可靠性状态按与最终共识一致更新，会有自证和调用选择偏差。九模型聚合 API、六个选择题/数学 benchmark 以调用数为成本 proxy，不是硬件吞吐/并发/SLO 证据。Ch82 原有共识与验证分离，尚缺该确定性停止条件，现已在 Aggregation 中补入票集不变量、串行 critical path、已花成本与回退；**整合，`apr03` 独立写后复核通过**。随机 early-stop 对照的正文与表2平均调用数不一致，因此不采用其精确加速数字；不影响固定票集严格多数的条件命题。

### [2604.02967v1 — FoE / RED](https://arxiv.org/abs/2604.02967v1)

[Exact-v1 §4.2–4.3、§5、Appendix J/K](https://arxiv.org/html/2604.02967v1) 用 entropy/variance 触发负提示分支的对比 logits，并周期多提示、多样本探测答案稳定性；二者分别改变生成与停止控制。作者六个开放推理模型、数学/GPQA、三次采样与 A100 成本测试支持受限净收益，不是开放 Agent 或服务 SLO；额外分支/probe 必须计费。错误森林的上界比较不能证明首答总更优，全部 probe 可共同出错。Ch80 现有 sensor/slow critic 尚未承载对比分布与跨提示停止的分工，已局部整合并保留独立验证和继续探索分支；**整合，`apr03` 独立写后复核通过**。

### [2604.02460v1 — Equal Thinking Budget Comparison](https://arxiv.org/abs/2604.02460v1)

[Exact-v1 §3–5、Appendix F/G](https://arxiv.org/html/2604.02460v1) 在 FRAMES/MuSiQue 四跳、Qwen/DeepSeek/Gemini 的指定调用和 thinking-budget 配置下比较单 Agent 与五种团队；各切片存在例外，不能外推单 Agent 总胜。API 预算只是配置，自报 thought count、可见文本及真实 FLOPs 不是同一量。§3 由 Fano 下界排序推出真实错误率排序并不足够；信息严格损失也不保证 0–1 Bayes error 严格增加，不采其现实固定计算保证。Ch82 的同信息理论前提、coordination tax 与等总预算 frontier 已承载稳妥边界；本次**仅报告**受限反证和理论争议，不以论文标题增加长期结论，也不机械排除新验证。

### [2604.02343v1 — Massive Knowledge Transfer via Binary Communication](https://arxiv.org/abs/2604.02343v1)

§4–5 与 Appendix E/G 将小模型的问题和专家二元回答组成协议，再由共享先验与可重放计算恢复推理。主配置为一次生成十个问题；实验中的答者可见参考答案，不能当作部署中任意专家都能判真。Claude-family、八类任务及自问自答对照表明部分收益来自结构化自我修订，困难任务并非一致改善。只计回答 bit 的压缩不计问题、双向传输、两侧推理与重建计算；不可确定重放或错误反馈也破坏恢复前提。因此不采用整体通信倍数。Ch82 原有 latent message 压缩之前现补入共享先验、channel budget 与 correctness authority 的分工，保留完整文本和独立 verifier 分支。作者模型服务硬件、精度与生产并发/SLO 未披露；本文结果不是 fleet 级成本保证。**整合，单篇独立对读通过。**

### [2604.02525v1 — Operand-Pattern Mixed-Precision Training](https://arxiv.org/abs/2604.02525v1)

§4–6 将 forward、weight-gradient 与 input-gradient 的两操作数分别按行/列异常分类，再选择在线 Hadamard 变换、异常部分高精度计算或 BF16 回退。约三十步校准与后续短轨迹检查支持其固定分类设计，不证明异常模式在任意长期训练都不变；高精度例外有索引、搬运与融合成本。C4 上约 1–8B Llama/Instella、MXFP4 与 AMD CDNA4 kernel 的训练损失和任务比较支持这条受限选择，部分任务不占优、提取预算等未全量扫描，不采用无条件质量或加速结论。Ch28 已在 BF16 默认精度与 Precision Policy 之间补入按操作数形态选分支的机制，保留高精度基线、重新校准与回退。**整合，单篇独立对读通过。**

### [2604.02686v1 — Token Mapping Reward-Model Interface Attack](https://arxiv.org/abs/2604.02686v1)

§3.2 的攻击接口把 policy 原始 token ID 直接映射至不同 reward tokenizer 的同索引，越界时夹界；同 ID 不等于同文本，优化因而能接触正常文本桥不会生成的奖励输入。Llama/Qwen 与对应 Skywork reward model 的两组配对、WildChat 训练和 NoveltyBench 受限检验支持此接口攻击，而非正确重新分词的所有生产 RM 都有同一漏洞。奖励胜出不是事实正确或人类偏好保证；硬件/精度等未披露字段不补造。Ch31 reward-hacking 段现先检查实际 RM 输入的 tokenizer、模板、特殊 token 与映射 identity，再讨论优化是否追逐代理；文本桥增加处理成本且不消除通常的 reward hacking。**整合，安全深入审阅与单篇独立对读通过。**

### [2604.02721v1 — GrandCode](https://arxiv.org/abs/2604.02721v1)

§4 式 1–7 将阶段奖励与最终减阶段的迟到修正分别归一化，且 behavior policy 可以逐 token 变化；两部分不因此代数等价于单一 terminal objective。完整方案还包含 CPT/SFT、测试生成和 test-time RL 等；私有百题与比赛结果不能将全管线增益单独归因迟到修正，关键消融和公开训练代码缺失。Ch33「Immediate Reward、Delayed Correction 与 Staleness 是同一 Lifecycle」已具体说明行为/token 身份、独立 normalization、迟到 correction 权重/clip 与缺失反证，故不重复添加正文。**已有覆盖，单篇独立对读通过。**

### [2604.02795v1 — Rubric-to-Token Credit](https://arxiv.org/abs/2604.02795v1)

§3–4 把 rubric 是否满足与 token relevance 结合；在单回答、单 criterion 内标准化后，与跨回答 outcome advantage 组合，避免较长回答以 token 数主导局部 credit。relevance 由额外判别器和自动标注提供，并非因果归因；零方差数值处理、权重与标注 identity 仍需实现验收，不能从公式推定已被普遍解决。HiR 指令遵循、Qwen/Llama 小规模 policy、IF 系基准及 §6 分组/系数消融支持此选择，但部分子任务与域外能力下降，局部项过强会伤整体目标，未验证长程 Agent。额外判别器训练/推理成本不可省略；未披露精度、并发/SLO 不据此推测。Ch33 rubric credit 段已纳入归一化对象、局部定位误差与 outcome-only 回退。**整合，单篇独立对读通过。**

### [2604.02344v1 — WebGPU Dispatch](https://arxiv.org/abs/2604.02344v1)

[Exact-v1 §3.3–3.6、§4.3–4.4、§5.1与§7](https://arxiv.org/html/2604.02344v1)区分直接测得的WebGPU dispatch、fusion差值推导的framework/per-operation成本和未直接测得的overlap残差。异步queue submission的CPU时间不能简单相加为wall time；融合减少的操作数也不是纯API调用成本。RTX5090/Dawn/Vulkan、Qwen2.5-0.5B、float32、batch=1、5输入/50输出token是端到端开销分账主路径；CUDA部分float16对照、多厂商端到端观察不能证明跨设备同一分解或生产SLO。原始Submitted/OAI created=02-09只证明早提交，不证明早公开；自身v1 Updated=04-06T00:00:24Z与本日连续ID/公告规则/相邻链相容，按§1同一有界推断支持本窗，不再要求逐篇日志。Ch49原有host-stack归因未明确异步CPU求和与fusion差值的区别，现已在其诊断段真实补入测量/推导分账、重叠及回退。Books：**整合** `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，写后独立复核通过。

### [2604.02372v1 — Decentralised Post-Training Backdoor](https://arxiv.org/abs/2604.02372v1)

Exact-v1 §2–4 的攻击者只控制去中心化 SFT 的一个中间 pipeline stage，不直接看 plaintext token 或最终回答；先用相同 base model 离线训练该 stage 的恶意 surrogate，再在共同 SFT 中按固定间隔加入缩放参数差分。clean validation loss 可近似正常，含触发词的 harmful-response 行为却偏离；作者在 Llama-3.2-1B Instruct、固定 stage 切分与 Llama Guard 判定下报告 94% 触发成功、后续安全微调后约 60% 仍有效。这是受限模型/攻击参数/判分器实验，不证明任意 pipeline stage、LoRA 或生产部署会同样失效。攻击前提是对手知道 base 权重及精确切分；原文尚未验证防御。与 [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 现有中间 activation canary 相比，训练期 stage-owned 参数 delta 与最终 loss 不能证明无后门是另一个责任边界；书稿已在该段后补入参数 revision 的来源/授权审计和触发切片发布验收，明确这些是需要验证的防线而非论文已证明有效的防御。Books：**整合**。

### [2604.02375v1 — KAIJU](https://arxiv.org/abs/2604.02375v1)

Exact-v1 §4–7 将 LLM 的 workflow proposal 转成 DAG nodes/typed data dependencies，由 Executive Kernel 管理并行、失败与反射轮次；工具执行 gate 分 scope、intent、impact、clearance，planner 未见工具、scheduler 拒绝越界名称、impact cap 再约束已允许工具。作者 GAIA 仅测 127 个 text-only 问题，DAG Reflect 15.7% vs ReAct 12.6%，简单查询有规划开销，统计还受输出格式和任务/工具配置影响；不能把该局部比较写成一般安全保证或所有任务吞吐优势。[Ch84](../../../../books/part-07-agent/84-agent-platform.md) 已把模型 action proposal、独立 runtime typed primitive、capability/path/object scope、approval 与 side-effect commit 分权，恰是此 gate 的可迁移设计责任；KAIJU 的四字段是受限实现而非新的 owner，故 **已有覆盖**。

### [2604.02522v1 — Opal](https://arxiv.org/abs/2604.02522v1)

官方 [OAI 记录](https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2604.02522&metadataPrefix=arXiv)给出 `created=2026-04-02`、`updated/datestamp=2026-04-06`；`2604` ID、04-06 OAI 日期与本窗连续公告 ID 批次共同支持 04-06 归属，但不把手稿页眉 04-02 或 OAI 日期冒充精确公告分钟。Exact-v1 §2–6 把个人记忆的 query-dependent KG/filter/ANN 控制与小型 metadata graph 留在可信区，外部 embedding 与原文分别进入固定读取预算的两套 ORAM；client counter、完整性根及 checkpoint 防止在已声明恢复边界之外回滚。旧的只加密正文/外置检索会泄露访问模式；全量载入可信区或用很大的固定访问预算又使容量、带宽成本上升。作者的准确率、吞吐与成本比较基于合成个人数据、特定 TDX 4-vCPU/4-GB/NVMe controller 及 B200 模型服务、ANN-only/Graphiti/plaintext/in-memory 等基线；没有生产部署证明，未实际跑 secure Graphiti，硬件 side channel、DoS 与授权后的内容正确性不在同一保证内。[Ch77](../../../../books/part-07-agent/77-memory.md) 原本有受约束检索和 freshness，但未把访问次数/位置作为单独隐私合同；主任务已在该检索主线纳入可信区控制、外部固定形状访问及 ORAM 成本/普通授权检索共存边界，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 仍拥有安全威胁模型。Books：**整合**。

### [2604.02638v1 — AXELRAM](https://arxiv.org/abs/2604.02638v1)

Exact-v1 §II–V 的设计把 K 的正交旋转与固定码本量化放在写入侧，读取时对每个 query 只旋转一次并预计算查表内积，不对每条历史 K 反量化；这是 KV read path 的具体候选，不是已制芯或已测 Serving Engine。作者的 102.4× 是设计中的乘法次数差异，不是实测时延；PyTorch PPL 仿真又显示随机 sign pattern 会在 Qwen2.5-3B 低 bit 设置产生极端退化，逐层用校准集选 pattern 才缓解，且 Qwen3-8B 的 2-bit 仍有明显质量代价。ROM、calibration、索引布局、真实 SRAM 面积/能耗/带宽和 runtime kernel 尚未形成可外推的硬件证据。[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 已把 query transform、KV 量化读路径、校准身份和可执行 kernel 与质量联合验收；此项是受限实现分支，不改变长期设计判断，故 **已有覆盖**，不写入“102× 加速”。

### [2604.02650v1 — Long-Context CPT Dynamics](https://arxiv.org/abs/2604.02650v1)

[Exact-v1 §3–7](https://arxiv.org/html/2604.02650v1) 跟踪 Hunyuan-A13B（80B 总参数、13B active）从 32K 扩至 64K 的一条 200B-token CPT 轨迹：短/长材料约 25/75，常数学习率与 RoPE base 同时改变。普通 NIAH 命中在约 20B token 起趋于饱和、50B 后为 100%，但 NIAH answer-token PPL 继续下降至约 150B；固定轻量 SFT 后的 RULER/MRCR/LongBio 任务与 retrieval-head 指标提供不同层次的诊断。论文所测 SFT probe 使用 440K 内部样本、约 0.25B token、两 epoch，并不等于 base model 自身具备同等指令能力；head 与任务成绩的相关也不证明因果。单架构、单数据配比、32K→64K、单训练轨迹，不能把 150B 当通用停点，更不能把作者 FLOPs 估算当实际训练时间。对照 [Ch28](../../../../books/part-04-training-system/28-pretraining.md) 原有“训练信号分层证据”主线，新增的长期判断是**长上下文 CPT 的检索命中可先于条件分布与任务能力饱和，停训要按同一 checkpoint 的多路信号及目标任务决策**；主任务已在 Mid-training 段局部整合，且保留 NIAH 作为便宜 smoke test。Books：**整合**。

### [2604.02767v1 — SentinelAgent](https://arxiv.org/abs/2604.02767v1)

Exact-v1 §III–VII 用可信的非 LLM Delegation Authority Service 逐 hop 记录 human principal、scope、parent 和过期约束；authority narrowing、policy conjunction、API scope-action 与输出 type schema 是确定性约束，intent entailment 则仍是概率判别。作者在自建 DelegationBench v4 的 516 场景上报告 P2+P6+P7 组合 100% TPR/0% FPR，但单独 P2 仅 13.3% TPR；允许的 API 被恶意用于错误目的、允许的输出类型中含有害内容、宽泛 manifest 与过期 schema 都可能越过对应局部 gate。TLA+ 只检查其形式模型的有限状态，不认证真实代理安全。[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 已要求可核的 principal→delegate→scope 链、执行前 fail-closed、独立 policy/effect gate，并明确签名不能证明 Agent 意图或行为正确；该论文是多级组合的受限安全案例，未改变 canonical owner，故 **已有覆盖**，不把其 benchmark 100% 作为普适防护率。

### [2604.02947v1 — AgentHazard](https://arxiv.org/abs/2604.02947v1)

官方 [abs/v1](https://arxiv.org/abs/2604.02947v1) 的提交历史为 2026-04-03，而同一 ID 的官方 [OAI 记录](https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2604.02947&metadataPrefix=arXiv) 当前写 `created=2026-09-22`、`updated/datestamp=2026-09-23`。这不是“提交早于公告”的普通 hold，而是两个官方载体对原始身份/创建日期相差五个月；虽有 `2604` ID，本轮无法安全判定 04-06 的 first-public owner。其 2,653 项 computer-use Agent 有害轨迹评估只保留为待核线索，不引用 73.63% 等数值作 04-06 结论，也不据此写 Books。状态 **Disputed identity/date**；需 arXiv 修复/解释 OAI 或可核原始逐篇公告存档后定点重开。

### [2604.02473v1 — Reverse Address Translation](https://arxiv.org/abs/2604.02473v1)

Exact-v1 §3–5 用 ASTRA-sim/Omnet++ 与 MSCCLang 的 All-to-All，模拟 8–64 GPU、2MB pages 的 UALink Clos 路径，指出目标 GPU reverse address translation 的冷 TLB/page walk 可主导 1MB 小 collective 的关键路径；流式跨页后几乎不再读旧页，单纯扩 L2-TLB 不一定收益。作者在该模拟系统报告小消息最多 1.4× 性能退化，不能外推 NCCL 实机、其他 page size 或任意 topology。[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 已要求按 transport、topology 与 collective completion time 分账，并独立定位同步尾部。本文是其中一种受限的目标侧地址翻译诊断，尚不足以改变实机调度、拓扑或算法选择，故 **已有覆盖**；不为模拟例子重复扩写。

### [2604.02340v1 — Denoising Step Scheduling](https://arxiv.org/abs/2604.02340v1)

Exact-v1 只在 OpenWebText 的 masked diffusion LM 上检验逐步切换 12-block heavy 与 4-block light denoiser：先对各 timestep 轻重模型替换引发的 loss/KL 变化做敏感度画像，再在预算内把重模型留给较敏感的中间窗口。作者给定 1000-step schedule、约 25% light 使用比例时报告最多约 17% FLOPs 降低；这不是端到端 wall-clock、吞吐或同等输出质量在其他预算下普遍成立的证明，画像和双模型驻留也有额外成本。不能把这个文本 MDLM 的 critical window 直接搬到图像或视频 denoising。[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 已有“不同 step 的状态变化/误差敏感度决定 reuse 与 recompute”的条件化计算框架；本文为其受限文本实例，不改变 owner 或设计结论，故 **已有覆盖**。

### [2604.02766v1 — Random vs Active online DPO](https://arxiv.org/abs/2604.02766v1)

Exact-v1 §2–5 在同等 pair 标注预算下比较随机 on-policy pairs 与按 entropy/margin 选择的 active pairs；后者要额外计算不确定度并依赖 proxy judge，理论的信息效率未自动转化为更好策略。作者以 Llama 3.2-3B、Qwen3-1.7B、Gemma-2B、Qwen2.5-7B 的 LoRA online DPO，在 HH-RLHF/UltraFeedback 的 helpfulness、harmlessness、instruction-following 设置中观察多数 active 改善很小；proxy win-rate 改善还可能同时伴随独立 LM Eval 能力下降，Gemma 的波动也说明不能断言随机永远优。它没有覆盖真实人工标注或长期生产反馈，代理 judge 质量与候选池分布会改变结果。[Ch34](../../../../books/part-04-training-system/34-dpo.md) 的 pair-acquisition 主线已经明确随机/分层抽样的可复现基线、active selection bias 与独立 held-out 验收；此项提供反证案例而非新的设计责任，故 **已有覆盖**。

### [2604.02965v1 — SV-VLA](https://arxiv.org/abs/2604.02965v1)

Exact-v1 §3–5 让较慢的 VLA 生成 action chunk；较轻的 verifier 以新 observation 与既定 chunk 的偏差为触发器，决定是否提前重规划，而非每步完整 VLA 推理或无条件执行全部 chunk。它用 verifier 计算和阈值校准换更短闭环，误报导致多次慢路径、漏报则让动作在旧 observation 上继续；verifier 不拥有物理执行的最终 authority。作者在 LIBERO Goal/Object/Spatial 仿真、四张 A100 训练与单张 V100 推理、batch 1 的受限设置报告平均成功率由 open-loop 79.5% 到 90.9%，不能外推真实机器人 latency、安全或所有 action schema。[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 已将慢语义计划、快频 observation correction、speculative verification 和低层 controller 的责任分开，亦保留静态场景的 action chunk 适用条件；该论文是同一闭环分层的仿真案例，故 **已有覆盖**。

### [2604.02816v1 — QAPruner](https://arxiv.org/abs/2604.02816v1)

Exact-v1 §3–4 先指出独立做 W4A4 PTQ 和按语义剪视觉 token 的失配：被剪掉的 token 可能包含激活 outlier，令保留序列的低比特数值误差上升。作者按视觉 token 计算 group-wise 模拟量化误差与动态范围，再与语义相关性混合后选 top-K；selector 因而既要回答“这个 token 语义有用吗”，也要回答“低精度后是否仍稳定”。LLaVA-1.3 7B/13B、LLaVA-1.5 7B 在 ScienceQA 的 W4A4 设置中，LLaVA-1.3 7B 从 256 个视觉 token 保留 32 个时相对 naive 合并基线的平均准确率差是 2.24 个百分点；没有对其他模型、硬件端到端速度或精度/SLO 的普遍保证，量化敏感度画像也需额外计算。[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 现有压缩身份及 [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的执行计划各自成立，但联合 selection/admission 是新增边界；主任务已把语义与数值敏感度共同验收写入 Ch23 原视觉压缩主线，Ch49 保持执行 artifact owner。已独立核正文事实、局限和交接。Books：**整合**。

### [2604.02954v1 — LogicPoison](https://arxiv.org/abs/2604.02954v1)

Exact-v1 §4–5 攻击者不直接添加显眼假实体，而在可改的 corpus 中按实体类型做循环替换，分别针对高频全局 hub 或 query-specific 多跳桥接；文本仍可读，图构建后的边却改指错误对象。HotpotQA、2Wiki、MuSiQue 与所测 GraphRAG/GFM-RAG/HippoRAG2、三类生成模型的受控实验支持拓扑破坏路径，不证明所有图构建器或生产语料都有同一攻击率。论文 §5.5.3 的 PPL 检测度量实现描述存在疑问，不作为防御有效性的依据。与 [Ch76](../../../../books/part-07-agent/76-rag.md) 原先仅要求最终引用可回溯相比，新增的是**图边/实体身份及其原文 span、构图 revision 的入库证据合同**；主任务已将它局部写入原 RAG 主线，并保留无法验证拓扑时退回原文逐跳检验的边界。Books：**整合**。

### [2604.03088v1 — SkillRT](https://arxiv.org/abs/2604.03088v1)

Exact-v1 §3–7 以 `(model, harness, environment)` 能力画像处理原始自然语言 Skill 的隐含依赖：安装期 AOT 生成 target-specific variant，运行期按目标选择并在结果显示不匹配时 JIT 修订；依赖绑定和可并行片段提取属于不同编译 pass。作者在 8 个模型、3 个 harness、14 类 Skill 与 Mac Mini M4 的任务设置中报告成功率和局部 3.2× 并行速度收益；weather/PDF code-solidification 的 19–50× 只属于两类稳定签名任务，不能套到任意工具调用。编译非确定、能力 profile 过期、依赖副作用、target variant 过多都可能抵消收益；admission 仍需独立执行和权限 gate。[Ch84](../../../../books/part-07-agent/84-agent-platform.md) 已有以 model/harness/revision/environment 为 key 的 capability profile、AOT/JIT/fallback、variant registry 和 promotion evidence 论证，故 **已有覆盖**。该 v1 名称是 SkillRT；不把后来版本的名称和实验回填成本窗事实。

### [2604.03208v1 — Hierarchical Latent World Model](https://arxiv.org/abs/2604.03208v1)

来源身份与日期可核：官方 [abs/v1](https://arxiv.org/abs/2604.03208v1) 记提交为 2026-04-03、[PDF/v1](https://arxiv.org/pdf/2604.03208v1) 首页为 `arXiv:2604.03208v1` 且正文日期 2026-04-06；本窗首次公告批次可保留其 Source Family 归属。但**同一 v1 官方载体自身不一致**：abs/v1 摘要称模拟环境 planning compute 最多 `4× less`，PDF/v1 首页摘要及实验文字称 `3× less`；实验性 [HTML/v1](https://arxiv.org/html/2604.03208v1) 又显示后发 `August 24, 2026` 首页日期，不能视作 04-06 的原始正文。高层 latent macro-action 产生 subgoal、低层以 primitive action 短 horizon MPC 接续只是待修复机制线索；本轮不引用任何 `3×/4×` 性能结论，不用污染的 HTML 支持设计判断，也不进入 Books。状态 **Disputed Version Evidence**；若作者或 arXiv 修复同版本对应关系、或可核提交源包与 PDF 匹配，定点重开全文和 Ch25/26 owner 审阅。

### [2604.02560v1 — DEMASK](https://arxiv.org/abs/2604.02560v1)

Exact v1 的 §4–7 将并行 masked 位置的乘积近似与真正联合条件的失配作为机制问题，预测器从一次前向的 hidden states 估 pairwise influence，贪心选累计依赖较弱的变量。总变差界依赖 sub-additivity 假设，作者在 Dream-7B 的速度/质量对照不能推为所有 diffusion LM 的普适收益。与 [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 既有“pairwise conditional MI → 依赖图 → 弱依赖位置并行提交”命题同构；此项带来另一实现与受限证据，不改变当前设计结论，故 **已有覆盖**，不为制造书稿增量重复追加。

### [2604.03141v1 — Importance-Aware Recall](https://arxiv.org/abs/2604.03141v1)

Exact v1 §3–5 把 generated claims 的 evidence support precision 与从外部知识建立的 reference facts 的 coverage/recall 分开；重要性权重由 relevance/salience 决定，fact extraction、聚类与 judge 的错误会传递到结果，参考源不完整也会制造假遗漏。 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) “验证没有遗漏必须先建立应出现事实的 Inventory” 已明确 expected facts、support/coverage、criticality/dependency 与 revision/extractor/rubric，足以承载同一评价合同。论文的开放式长文实验不证明 inventory 可穷尽，故 **已有覆盖**。

### [2604.03143v1 — TokenDance](https://arxiv.org/abs/2604.03143v1)

Exact v1 §2/§4/§6 的 workload 是中心调度器按同步轮次 All-Gather 每个 Agent 输出，随后各请求重新看到共同文本；普通 prefix/PIC 逐请求处理，会重复 shared-block prefill/KV。论文让 KV Collector 在整个轮次处理一次共享块，后续 sibling cache 用一份 Master 与 block-sparse diff 表示，读取时做融合恢复。**共享文本不等于 KV 完全同一身份**：位置差异需 correction，差分恢复有近似 fidelity/metadata/生命周期约束。作者在 GenerativeAgents/AgentSociety、Qwen2.5-7B/14B、单 A100 80GB、1500ms 轮次 SLO 与 QPS 1–16 条件下报告容量/压缩/速度收益；precision、输入输出长度未完整披露，不能外推生产 fleet。与 [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 原来的任意 Chunk 复用相比，新增的是**轮次级 collective state owner** 和 Master/diff 存储；主任务已将条件、代价与旧 prefix cache 共存边界纳入对应正文。Books：**整合**。

### [2604.02715v1 — FluxMoE](https://arxiv.org/abs/2604.02715v1)

Exact v1 §3–6 将 expert 的逻辑 tensor identity 与 GPU 物理驻留分离：不预测 router 命中的 expert，而是用稳定虚拟地址把当前层全部 expert 按层临时物化，前一层计算时从压缩 GPU/固定页 host 两路加载下一层，再按 stream/事件依赖回收旧层。它用可预测的整层滑窗换路由预测 miss 风险，却可能为未命中 expert 过量搬运；双路带宽、解压、PCIe 与低并发的计算/搬运比例决定是否能重叠。作者在 vLLM 0.10.2、Qwen3-Next-80B-A3B 与 Mixtral、L40、TP=4、batch 32–256、context 至 4096 的条件下报告高内存压力区吞吐收益；不得把 Qwen 单一 `up to 3.0×` 外推到其他 workload，精度与生产 SLO 也未完整披露。§6.3 明言当前 serving engine 的 KV 预分配是静态的，释放 HBM 不自动增大同进程 KV 容量。相比 [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) 原有完整驻留→静态 offload→router-conditioned cache→预测预取，新增的是**无需路由预测的整层短寿命权重物化**与 KV 压力下的 residency controller；主任务已把该条件分支及与旧路共存边界整合到 Ch54。Books：**整合**。

### [2604.03128v1 — Self-Distilled RLVR](https://arxiv.org/abs/2604.03128v1)

Exact v1 §3–5/§8 将有正确性标签的 environment verifier 与可见额外信息的 teacher 分开：verifier 的 outcome advantage 决定 sampled-token 更新符号，teacher/student likelihood ratio 只作为正的、带裁剪与归一化的 token 权重。这样能在学生自身轨迹上细分学习幅度，但不证明 teacher 贡献了真实 causal credit，也不消除 teacher bias、额外前向、数据泄漏与未探索状态缺口。与 [Ch33](../../../../books/part-04-training-system/33-grpo.md)“Verifier 拥有方向，Privileged Teacher 最多调节幅度”及负 outcome reset 段对照，方向所有权、正权重、成本和回退均已明确；本项 **已有覆盖**，不重复改书。

### [2604.03179v1 — Visual Necessity in MLLM RL](https://arxiv.org/abs/2604.03179v1)

Exact v1 在 Qwen2.5-VL 3B/7B 的受测视觉任务上，用被破坏或移除关键视觉信息的图像继续做 GRPO，再测成功率和视觉依赖；部分收益仍保留，表明单看任务准确率会把语言先验/shortcut 当作感知改进。该干预没有证明模型完全不看图，也不能外推所有多模态数据。与 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的模态必要性和 counterfactual visual intervention、[Ch33](../../../../books/part-04-training-system/33-grpo.md) 的视觉捷径边界对照，已有同等评估合同；故 **已有覆盖**。

### [2604.02985v1 — Prompt Compression in the Wild](https://arxiv.org/abs/2604.02985v1)

Exact v1 §4 将 LLMLingua/2 压缩运行时长与 target inference 时间分开，再按 prompt 长度、压缩率、模型及设备计算端到端 break-even，同时检验实际压缩率、质量和 GPU memory。作者 30,000 次查询覆盖 7B–70B 及两类 API 模型、A100 40GB/GTX 1080 Ti/M1 Pro、100–50,000 输入 token 与 1.5–5 压缩率；所报最高 18% 加速和 75% GPU memory 减少只是适配参数/硬件的局部最优值，其他窗口压缩成本反而抵消收益。其质量检验为 summarization、coding、QA，不能证明所有事实/安全约束完好；batch、concurrency、输出长度及生产 tail-SLO 未形成统一可外推合同。[Ch75](../../../../books/part-07-agent/75-context.md) 先前已解释信息损失与原文回退，本次在 Context Compression 原论证中补入 `T_compressor + T_target(compressed) < T_target(original)` 的准入条件、显存与质量验收、短输入及高风险证据的共存边界；[Ch43](../../../../books/part-05-inference-system/43-prefill.md) 保持 prefill owner，不重复新增。Books：**整合**。

### [2604.02986v1 — SignCert-PO](https://arxiv.org/abs/2604.02986v1)

[Exact-v1 §3、§4 与 Algorithm 1](https://arxiv.org/html/2604.02986v1) 针对 proxy reward model 错判组内 advantage 符号的问题：对线性 reward head、同 prompt 的完整回答，定义符号在 head 参数扰动下不翻转的半径 `Δ=|A|/||h−mean(h)||`，再用 `ρ=1−ε/Δ` 重权政策梯度。其证明只覆盖所设线性 head 与 Dr.GRPO 形式；普通 PPO/GRPO 是近似扩展，且半径不是“真实人类偏好正确概率”。作者在 TL;DR/AlpacaFarm 的 Pythia 1B/2.8B、Qwen2.5 1.5B/3B 设置用另一更强 RM（Skywork Reward 8B 或 GPT-4.1 nano）判断输出，而不是独立真人偏好；小模型两列 3 seed，其余单 seed，Qwen2.5 1.5B TL;DR 列 BSPO 胜率还高于本法。更重要的是 §3.2/Algorithm 1 令 `ε` 取 `1/Δ` 的 batch 分位数，却代入 `1−ε/Δ`；两处定义如何一致未解释，且该权重可能为负，不能笼统写成“只降权”。[Ch33](../../../../books/part-04-training-system/33-grpo.md) 已把 proxy reward 的方向风险和独立 outcome/evaluation gate 分开；本项提供受限候选机制，但在阈值定义/实现与外部偏好证据澄清前，不能成为长期优化 recipe 或发布门槛。Books：**暂缓**；重开条件为作者澄清阈值/实际实现，或独立复现按原公式证明稳定收益。

### [2604.03035v1 — Sequential Coding Agent Evaluation](https://arxiv.org/abs/2604.03035v1)

Exact v1 §3–5 从真实 PR 图构造相依任务链，逐步在上一 PR 改过的仓库上继续修改；F2P/P2P 测试义务累积，另用静态复杂度和技术债指标评估仓库健康，不只看最后一次任务 pass。SWE-STEPS 是 6 个 Python 仓库、168 个 tasks/963 个 PR、每链 3–11 PR；依赖判断用 symbol 引用与 git blame，重放设置分对话持续状态/一次 PRD/每 PR 重置，三者并不拥有完全相同的信息预算。作者观察单 PR 重置评测相对其设置成功率最多高估 20 个百分点；不能视为所有 coding agent、语言或真实团队的普遍偏差，SonarQube proxy 也不等于长期维护成本真值。[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原先只笼统要求长周期研发 Agent 测跨轮行为，此次新增“依赖 PR 链 + 累积回归义务 + 健康指标”的具体 admission contract。主任务已把它插入原长周期 Agent 段，且保留单题重置式评价的诊断用途。Books：**整合**。

### [2604.03070v1 — Credential Leakage in Agent Skills](https://arxiv.org/abs/2604.03070v1)

Exact v1 §3–5 对 17,022 个来自同一 Skill 市场的分层样本，用规则/AST 识别静态秘密，再用 mock credential、沙箱执行、网络观测和人工分类确认数据流。关键失效不是“Skill 可能有秘密”这句常识，而是 `stdout`/debug 输出由框架自动回灌给模型，令执行环境里的凭据跨入模型可读 Context；自然语言描述和代码要联合分析，单看其中一侧会漏条件路径。作者的泄漏比例和可利用性只限采样市场、特定验证配置，mock 命中不等于真实生产失窃；不能以此证明所有 Skill 的风险率。[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 原有 source-to-sink fact base 与模型 Context 禁入原则已提供上层框架，但缺这个自动日志回灌的具体边界，主任务已在原 Skill 安全段整合并保留隔离/调试代价。Books：**整合**。

### [2604.03081v1 — Skill Supply-Chain Poisoning](https://arxiv.org/abs/2604.03081v1)

Exact v1 §3–5 的攻击者控制分发的 Skill 文档，在看似正常的 code example/配置模板中嵌入 payload；Coding Agent 为合法任务复用片段后，恶意逻辑被生成并执行，故没有显式 jailbreak 也可能出现 effect。作者由 81 seeds 扩成 1,070 adversarial skills，在四框架、五模型与受控 sandbox 中测绕过率 11.6%–33.5%，报告四个披露确认项；这些数字受种子、任务、权限与评测防线配置限制，不证明任意生产 Skill 一定可绕过。与 [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 既有静态 fact-base 和 Skill side-effect 检验相比，新增的是**文档示例/模板也是可执行供应链输入**的路径；主任务已局部吸收，且保持真正副作用由独立 runtime gate 判定。Books：**整合**。

### [2604.02623v1 — Environment Memory Poisoning](https://arxiv.org/abs/2604.02623v1)

Exact v1 §2–3/A.1 的攻击者只能改 Site A 页面观察，不能直接写 Memory；Agent 把含 payload 的原始轨迹存下，之后 Site B 合法任务的相似度检索再把它读入 Context，借当前任务的权限执行原任务未授权的动作。WebArena/VisualWebArena 约 280 个跨站 task pairs 和数种模型支持这个受限路径；注入与触发发生在不同 session，不能用单次网站 allowlist 证明安全。作者又用点击丢失、滚动倒置等 stress 测“frustration”效应，但同时提高最大步骤数，不能将增长全归因心理状态；只测 raw trajectory memory，未系统验证 consolidation 或防御。最初 3+2+3 高估了其对长期设计的增量：与 [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 持久内容写时保存 origin/trust、每次读/执行前按当前 principal/权限/目的再验证的现有命题完全对齐；这项是对同一控制边界的跨站攻击证据，而非新的 owner 机制。分数收为 2+2+2=6，因安全路径仍完成深入审阅，Books **已有覆盖**。

### [2604.03191v1 — VLA Compression Gap](https://arxiv.org/abs/2604.03191v1)

Exact-v1 §2–5 测试“升级视觉 encoder 是否一定提高 VLA action 成功率”：在同一 OAT 代码路径上比较连续 Diffusion Policy 与离散 OAT；ResNet-18→SigLIP 对前者 M/L 模型的 LIBERO-10 峰值成功率增量为 +21.2/+26.0 pp，对后者仅 +3.6/+10.4 pp。四个 encoder 的梯度实验中连续路线较一致，离散路线不单调；码本从 1000 放宽到 1920 时对 encoder 的敏感度部分恢复，但到 4375 又回落，不支持容量越大越好的通用律，更不能由信息量上界证明真实瓶颈已饱和。实验限 LIBERO-10、50 demos/task、7D action、H32 chunk 执行前16步、单 A100、每50 epoch 取峰值成功率且无多 seed；不证明真机、不同 action schema、实时延迟或安全故障。[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 原有离散/连续动作表示与 codec 身份，却缺“上游感知扩容能否穿过 action codec”的设计 gate；主任务已在该表示主线补入 component-scaling 的条件性诊断，保留离散 token 对统一语言动作接口的价值。Books：**整合**。

### [2604.03216v1 — BAS Confidence Utility](https://arxiv.org/abs/2604.03216v1)

Exact v1 把 confidence 评价改成 answer/abstain 不同风险阈值下的实际 utility；ECE/AURC 类似的模型可因少量严重过度自信而有不同决策效用，理论性质仍受作者 utility 定义与自报置信度测法限定。 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已有 `Loss(abstain)=C_abstain`、错误代价阈值、selective prediction 与任务风险 policy 的直接论证，且强调评分要对齐实际损失。它是同一 contract 的另一度量实例，不改变目前结论，故 **已有覆盖**。

### [2604.02345v1 — UI-Oceanus](https://arxiv.org/abs/2604.02345v1)

Exact-v1 §4 将自主 GUI 探索产生的真实前后状态与 VLM 转移标签用于 CPT，再做任务对齐；真实观察不保证标签无误。§5.3 在固定转移数据下比较 forward/inverse 目标，inverse 变体不能重现 forward 收益，因而不是单纯多收演示。§5.2 的在线验收限 149 条人工核验指令，不能外推任意 GUI、物理因果识别或安全执行。Ch25 原有 inverse dynamics 辅助防坍缩，不等于 GUI forward prediction 主目标；已在该论证之后整合两者的条件分工、探索授权、标签噪声、遗忘和反应式回退。Books：**整合** `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。`apr01` 已对读方法、对照和实际正文，确认该边界；首提交为 02-11 不能直接充当首次公开，仍按本日报的公告批次依据接受日级独立归属验收。

### [2604.03118v1 — Salt](https://arxiv.org/abs/2604.03118v1)

Exact-v1 §3 在 DMD 外加入一步/两步终点的近似组合正则；AR 路线又混合不同步数自产生历史，并作弱历史与更密步数 reference 的关系特征对齐。后者来自同一 generator，不是固定 teacher cache。关键消融不支持只加一致性就稳定获益；额外 rollout、reference 成本和运动退化风险仍在。评价限 Wan 2.1/Self Forcing 等作者路线、私有 I2V 数据与所测短/长视频，不是无限 horizon 或 serving SLO 保证。Ch24 原有少步蒸馏尚缺局部匹配→组合误差→历史质量分布的联系，现已局部整合并保留增步、缩短 horizon 与旧配方回退。Books：**整合** `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。`apr01` 独立复核实际正文并指出 reference 身份措辞，已修正；07-01 v2 不混入本次 v1 审阅。

### [2604.02431v1 — SelRoute](https://arxiv.org/abs/2604.02431v1)

Exact-v1 §3、§5–6 保留原会话 episode，给 BM25 文本追加同义词、上位词与动作桥接词，而 dense channel 仍编码原文；类型 router 决定使用原词面、扩展词面或 hybrid。该设计说明检索辅助词不能自动成为用户事实，也不能假设同一扩展对所有表示都有效。作者的会话检索实验支持这种非对称性的受限作用，但相对最强固定 RRF 对照的差异未显著（p=0.121），预测类型弱于已知类型；Recall 不证明最终回答正确率，额外索引、类型误判和未知查询分布仍是代价。并发、服务 SLO 与跨会话复杂推理收益未建立。[Ch77](../../../../books/part-07-agent/77-memory.md) 原有 workload-adaptive cascade 解释了何时启用 dense，却未区分两通道读取的原始/派生表示；现已在该论证中补入表示分路、provenance、路由代价与回退，未将它写成普遍优于 fusion。`apr01` 独立核 exact-v1 和实际正文后通过这项写后复核。Books：**整合**；日级日期和分母 Gate 仍待完成。

## 5. 缺口与下一步

- **本窗普通工作：** 已无未处理的可执行扫描、候选审阅或Books写入。`.02869/.02734/.02344`实际正文已写后独立核对，`.03131`具体已有覆盖已核；`.02556`4分关闭及`.02837/.02367`关闭理由已校正，不重复审阅。以下仅为精确终态保留项，到达新材料时单项重开。
- **日期例外与恢复条件：** [日期审计](../_sources/daily-20260406/V3_DATE_RECONCILIATION.md)经一致性复核撤销了“必须取得逐篇实际公告日志”的过强门槛；组合证据支持本日保留项的推断区间，不再请求整批全文或日志。仅`.02947`身份/记录冲突仍精确隔离，需官方首公告/同题原始公开记录或身份说明后单项重开；不自动移动整批或由已检查推导零遗漏。
- **外部保留项：** OpenAI Research、Meta Research/Publications、Google Research Publications 的历史精确日目录尚不能完整回溯；所见 News/Blog 不替代它们。恢复条件分别为官方历史目录、可核站点存档或具有本窗首次公开证据的原始报告；只重开受影响来源/候选。它们不支持全源零命中与任何 Books 正面采用。
- **版本污染与同版本争议：** 原始旧账本的 `2604.03088` 标题来自后版，v1 为 **SkillRT**；`2604.02340v1` 摘要仅列 OpenWebText。`2604.03208v1` 官方 abs 与 PDF 摘要分别写 4×/3×，HTML/v1 首页还有后发日期，已隔离为 Disputed，不机械择一作为事实或 Books 证据。
- **公式/实现争议：** `2604.02986v1` 的阈值取值与重权公式未解释一致性，权重还可能为负。已完成必要审阅但不采用为 Ch33 的优化配方；只有作者澄清实际阈值/实现，或独立复现解决该矛盾后才重开，不能把它记为普通待审或已验证的仅报告机制。

## 6. 复核

复核者：apr03（非日报作者；来源/准入的前轮独立检查复用，新增Books逐项写后对读）
结论：通过

实际检查：14个到期来源的检查/精确外部隔离，449原始身份与最终47个家族的区分，旧关闭侧及共同错误理由的定点反查，组合日期推断和单项例外，评分/处置对账，以及必要Books实际正文和邻章交接。47项为26整合、18已有覆盖、1仅报告、2争议暂缓，另02947身份/日期隔离不计确定分母。修正了GN聚合顺序的误外推、Memory有效动作与任务成功的混淆、SignCert计数遗漏、早提交被误当早公开，以及WebGPU直接dispatch与完整端到端分账的适用范围。后两项争议和三处外部历史目录限制不用于Books正面结论，也不支撑零遗漏。结构校验与本次相关文件diff检查通过；未stage、commit或push，不修改无关工作树。
