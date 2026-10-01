# Daily Research — 2026-09-18

**规范：** V3
**窗口：** 2026-09-17T09:00:00+08:00 ～ 2026-09-18T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-21T13:03:15+08:00

## 1. 结论

本窗的每日来源检查与日级 arXiv 去重已完成。arXiv 十二个目标分类共得到 621 个去重 new/cross identity。终审圈定的 14 个标题边界项均已读取完整摘要：3 项的 first-public date 早于本窗，6 项形成 family-specific 候选前关闭，5 项恢复为当窗候选并完成 exact-v1 审阅。后续 closure 抽检再定点恢复 `2609.17904v1` 与 `2609.18622v1`；最终账目为 62 个当窗 arXiv 候选、24 个前日 owner、122 个完整题摘关闭与 413 个标题明确关闭。机构来源另增 1 个当窗 artifact（Meta/FAIR UnStep），因此候选分母为 63 个唯一 Source Family；没有用题摘阅读代替入选项的证据审阅。

本日最重要的系统增量不是单一 benchmark，而是四类可复用的设计边界：一是把模型更新、推理优化与自动调参的质量判断升级为配对、可校准且有 null/control 的测量合同；二是将 KV 的局部修复、离线读取深度与扩散模型的分组缓存统一到“请求真正读了哪些状态”；三是把 fault recovery、GPU fragmentation 和 restart-aware scheduling 写成明确的状态/控制权移动；四是将 reward hacking、first-token refusal 与多 Agent 延迟共识的信号限定为传感器或特定环境现象，不将表征可读性、verbal confidence 或共识冒充真值。

最终 38 个 Source Family 已由对应 Books 正文承载；本轮确认的 `2609.18270v1` 与 `2609.18649v1` 已按日期顺序写入 Ch66，定点恢复的 `2609.18622v1` 与 `2609.17904v1` 则分别核实为 Ch66、Ch26 中已有的唯一实质绑定，无需重复写入。fresh non-author 终审核对 exact-v1 证据、评分、处置、账目和真实正文绑定后通过。其余 25 个候选经比较后判定为现有正文已完整承载，不为制造 diff 重复追加。`2606.27409v2` 作为当窗重要修订单独深审但不重复评分，其延迟索引、synthetic stability 与 factual-QA 不确定性边界已在既有 owner 中修正。同时处理 replacement list 的撤回信号：`2605.06850`、`2608.04765` 已从旧 Daily 的正面候选、评分与证据链路清除。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/RSS 按当窗检查；直连目录返回 403，辅以官方域搜索定位可见条目 | 受阻 | 无法用目录证明当窗绝对零事件；不支持候选、Books 或无遗漏断言 |
| SRC-ANTHROPIC | Research 列表与当窗可见文章；生物建模条目为 AI for Science 暂缓，frontier-lab measurement 只给日期 | 已检查 | measurement 条目缺可判定落窗的公开时刻，已隔离为 Date Precision Gap |
| SRC-GOOGLE-AI | DeepMind Research 与 Google Research 公开列表按窗口检查；09-17 Generative UI 教育应用读取后关闭 | 已检查 | DeepMind 目录日级完整枚举有限，不做绝对零事件断言 |
| SRC-META-AI | FAIR/Research 入口与官方 GitHub 创建事件；确认 UnStep 于 09-17 19:52 北京时间公开，并绑定初始 commit `e7525751dc00582571cb3eea6e357cfa57db0843` | 已检查 | 官网无稳定日级完整枚举；已用不可变 artifact 限定当窗结论 |
| SRC-QWEN | Qwen Blog/Research 与官方仓库可见事件按窗口检查 | 已检查 | CSR 目录枚举有限；未发现可确认的当窗机制事件 |
| SRC-DEEPSEEK | 官方 Research/发布页与公开仓库事件按窗口检查 | 已检查 | 无当窗入选事件 |
| SRC-MOONSHOT | Kimi Blog、MoonshotAI 公开仓库与发布事件按窗口检查 | 已检查 | 无当窗入选事件 |
| SRC-TENCENT-HUNYUAN | 官方 Research“全部”列表与公开仓库按窗口检查 | 已检查 | 静态/CSR 结构的机器枚举有限；未发现可确认的当窗事件 |
| SRC-ZAI | [智谱 Research](https://www.zhipuai.cn/zh/research)、官方发布和仓库按窗口检查 | 已检查 | 无当窗入选事件 |
| SRC-BYTEDANCE-SEED | Seed Research、论文目录与官方仓库按窗口检查 | 已检查 | 无当窗入选事件 |
| SRC-BAIDU-ERNIE | ERNIE 技术博客、PaddlePaddle/ERNIE 发布与可见事件按窗口检查 | 已检查 | 无当窗入选事件 |
| SRC-XIAOMI-MIMO | MiMo 论文/博客卡片与官方仓库按窗口检查 | 受阻 | 博客卡片缺稳定时刻；获得带时区的日级列表或唯一新材料身份后定点重开 |
| SRC-MINIMAX | 中英文 Blog、Research、Agent Tech Blog 与官方仓库按窗口检查 | 已检查 | 无当窗入选事件 |
| SRC-ARXIV | Thursday new list；`cs.CL/LG/DC/AI/CV/RO/AR/PL/OS/PF/IR/MA`。621 个 new/cross 唯一 identity；终审圈定的 14 项完成摘要分流，closure 抽检再定点恢复 2 项，最终冻结 62 项当窗候选、24 项前日 owner、122 项完整题摘关闭与 413 项标题关闭；293 个 replacement 检查重要修订/纠错/撤回 | 已检查 | 无 |

完整 identity、去重、关闭理由、replacement 处置与本地 exact-version 路径见 [screening ledger](../_sources/daily-20260918/screening-ledger.md)。上述目录限制均已隔离：不用于正面候选、Books 或“无遗漏”断言，不阻塞其余已确认材料的闭环。

## 3. 候选与判断

评分顺序为 Design Delta / System Reach / Durability。arXiv 当窗候选以 Thursday new list 的首次公开事件为日期依据，均使用 exact v1；`2606.27409v2` 是当窗重要修订事件，按合同不重复评分。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Register Bias in Complexity-Based Large Language Model Routing](https://arxiv.org/html/2609.17542v1) | 2026-09-18T08:00:00+08:00 | 路由的语言 register 偏差可以让 complexity gate 把同等问题送往不同模型，需要将 fairness 与成本路由共同评价；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Pay Only for Disagreement](https://arxiv.org/html/2609.17560v1) | 2026-09-18T08:00:00+08:00 | 更新审计可只标注新旧模型的 disagreement support，并用 anytime-valid confidence sequence 给出 no-regression verdict；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GroupKV](https://arxiv.org/html/2609.17573v1) | 2026-09-18T08:00:00+08:00 | diffusion LLM 的多步全序列 KV 可按 group 稳定性分层并预取，需显式约束 staleness；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Fathom](https://arxiv.org/html/2609.17652v1) | 2026-09-18T08:00:00+08:00 | offloaded KV 不必每查询读全部 bitplane，per-query read depth 改变带宽/精度控制；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Accelerating Diffusion Sampling via Speculative Draft Trees](https://arxiv.org/html/2609.17691v1) | 2026-09-18T08:00:00+08:00 | speculative draft tree 为 diffusion sampling 提供受限并行分支，但 exactness 与校正权仍由 verifier 决定；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [REVERSAL-BENCH](https://arxiv.org/html/2609.17745v1) | 2026-09-18T08:00:00+08:00 | reset-free embodied learning 必须把环境可逆性、recoverability oracle 与吸收态作为运行时安全合同，而不是假设失败后总能恢复；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [SFT or RL for Tool-Calling Agents?](https://arxiv.org/html/2609.17848v1) | 2026-09-18T08:00:00+08:00 | 受控实验表明 SFT/RL 不是普遍排名，选择受数据、backbone 与 tool task 约束；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Who Judges Matters](https://arxiv.org/html/2609.17857v1) | 2026-09-18T08:00:00+08:00 | LLM-as-judge 面板存在 family-conditioned preference，增加 judge 数量不会自动消除共享偏差；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Timely Activation of Safety Filters via One-Step Reachability Expansion](https://arxiv.org/html/2609.17904v1) | 2026-09-18T08:00:00+08:00 | continuous-time safety guarantee 不能静默继承到 sampled control；最坏情况一步可达域应进入提前触发边界；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Locating Hidden Failures Makes Long-Horizon Agents More Reliable](https://arxiv.org/html/2609.17930v1) | 2026-09-18T08:00:00+08:00 | long-horizon 评价若只看结果会隐藏早期错误，failure localization 应独立于最终 success；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Beyond the Previous Layer](https://arxiv.org/html/2609.17940v1) | 2026-09-18T08:00:00+08:00 | MoE expert path 不满足简单的一阶 Markov 假设，较早 routing history 可作为 residency hint，但不能取得路由执行权；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [ASPIRE](https://arxiv.org/html/2609.17943v1) | 2026-09-18T08:00:00+08:00 | mixed draft/verify 请求可异步批处理，但每请求的 confirmed frontier 与 rollback 必须独立；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Contiguity, Not Importance](https://arxiv.org/html/2609.17983v1) | 2026-09-18T08:00:00+08:00 | 文档局部编辑后的 stale KV 修复对象是连续影响区间，而不是抽象 token importance；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Whom Do AI Agents Work For?](https://arxiv.org/html/2609.17989v1) | 2026-09-18T08:00:00+08:00 | system prompt 中的 principal assignment 会改变 sponsored listing 的选择与 disclosure 解读，说明 role/authority context 不能当作中性措辞；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-PROMPT` [Ch74](../../../../books/part-07-agent/74-prompt.md) |
| [The Attention Within](https://arxiv.org/html/2609.17997v1) | 2026-09-18T08:00:00+08:00 | selective SSM 的 recurrent update 与 output gate 产生 consensus dynamics，补充状态收敛与输出可观测边界；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [A Calibrated Instrument for Measuring How Inference Optimizations Affect Output Quality](https://arxiv.org/pdf/2609.18005v1) | 2026-09-18T08:00:00+08:00 | 质量损失比较需 dual reference、exchangeability/implementation null、等价界与功效预算；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Causal-History Test-Time Scaling for Failure Recovery in Autoregressive World-Action Models](https://arxiv.org/html/2609.18016v1) | 2026-09-18T08:00:00+08:00 | 恢复不是删除最后一步，而是检测失败、定位可靠 prefix、重建 causal KV 并比较完整历史/恢复 prefix/全重置假设；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [The Other Half of the Memory Wall](https://arxiv.org/html/2609.18063v1) | 2026-09-18T08:00:00+08:00 | SSD-serving MoE 用 prerouter 的预测直接替代下一层路由，并以沿 student path 训练、未合并的 Recovery LoRA 补偿质量，不是 prefetch miss/fallback；2 + 3 + 2 = 7 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Towards Training Private LLMs on Apple Silicon with RDMA over Thunderbolt](https://arxiv.org/html/2609.18066v2) | 2026-09-18T08:00:00+08:00 | 多链路通信、持久 worker 与 CPU-side overlap 展示了大统一内存/低互联带宽这一异构训练分支，收益绑定四节点 Qwen3-9B 合同；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Decodability is Not Causality](https://arxiv.org/html/2609.18080v1) | 2026-09-18T08:00:00+08:00 | probe 可读出特征不等于模型行为使用该特征，SAE intervention 给出因果分离；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [When Is Graph Structure Worth Its Cost?](https://arxiv.org/html/2609.18099v1) | 2026-09-18T08:00:00+08:00 | GraphRAG 必须把 ingestion/query 成本与 answer quality 放在同一 evaluation identity 中，图结构不能靠单一质量分数证明值得；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [SSD-LLaMA](https://arxiv.org/html/2609.18110v1) | 2026-09-18T08:00:00+08:00 | 超大 MoE 的 SSD/DRAM/VRAM residency、连续 expert-pack、异步 I/O 与 CPU-GPU 分工是同一执行计划；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Token Latency Fairness](https://arxiv.org/html/2609.18112v1) | 2026-09-18T08:00:00+08:00 | multi-tenant fairness 需限定每个 token 相对独占执行的延迟增量，并统计 compute/cache delay；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [AutoTuneBench](https://arxiv.org/html/2609.18123v1) | 2026-09-18T08:00:00+08:00 | Agent 调参评价必须冻结 baseline、机器、饱和度、provenance 与 validator；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Symbolic Temporal Supervision of LLM Agents Using Contracts](https://arxiv.org/html/2609.18128v1) | 2026-09-18T08:00:00+08:00 | temporal contract 可将跨步规则从 prompt 提示升级为可检查的 workflow state，但 monitor 不拥有环境真值；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Reaching Every Position Without Searching](https://arxiv.org/html/2609.18145v1) | 2026-09-18T08:00:00+08:00 | 跨层旋转稀疏 wiring 能以固定连接在对数深度形成全局可达性，但不等于内容自适应 Attention；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [Zero-I/O Fault Recovery](https://arxiv.org/html/2609.18178v1) | 2026-09-18T08:00:00+08:00 | fail-stop 恢复可在已 commit optimizer step 后重绑 handle/process group，不代替持久 checkpoint；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Beyond Accuracy](https://arxiv.org/html/2609.18204v1) | 2026-09-18T08:00:00+08:00 | procedural trace 会改变 overseer 的判定 criterion，因而 outcome 和 process evidence 不能被同一 accuracy 隐藏；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [BENCHCOMPASS](https://arxiv.org/html/2609.18270v1) | 2026-09-18T08:00:00+08:00 | 同一模型在 closed、open 与 attacked-open 条件下的差异能分离参数知识、context-use gap 与 harness brittleness；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Bias Amplification in Multi-Agent Network](https://arxiv.org/html/2609.18306v1) | 2026-09-18T08:00:00+08:00 | biased minority 可能同时改变数值意见与修辞，而两类收敛并不等价；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Beyond Quadratic Loss](https://arxiv.org/html/2609.18314v1) | 2026-09-18T08:00:00+08:00 | Adam 的稳定性由 loss curvature 与 `β1/β2` 共同决定，不存在脱离问题的普适最优 momentum；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Faithful yet Collusive](https://arxiv.org/html/2609.18346v1) | 2026-09-18T08:00:00+08:00 | CoT 的结构/意图 faithfulness 与联合行为 effect 是不同轴，解释监控不能独立拥有安全判定权；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Market Signal Injection](https://arxiv.org/html/2609.18357v1) | 2026-09-18T08:00:00+08:00 | 数值不变的数据呈现仍可操纵 LLM agent 决策；untrusted-data canonicalization 与 decision-boundary enforcement 必须分层；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [GeoMesh](https://arxiv.org/html/2609.18388v1) | 2026-09-18T08:00:00+08:00 | 异构 WAN 训练用按 worker 的 batch/inner-step 负载计划与 sign-compressed pseudo-gradient 降低等待，但会改变 objective identity 与恢复状态；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Planning or Improvisation?](https://arxiv.org/html/2609.18440v1) | 2026-09-18T08:00:00+08:00 | 复现归因曲线形状不能证明复现原机制；claim 应拆成位置特异性、位点身份与因果计划三个可证伪子命题；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Mirage of Calibrated Confidence](https://arxiv.org/html/2609.18453v1) | 2026-09-18T08:00:00+08:00 | verbal confidence 可能与实际 reasoning trajectory 脱钩，不能单独作为 abstention 或真值证据；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Collective Loss of Control in LLM Agent Systems](https://arxiv.org/html/2609.18460v1) | 2026-09-18T08:00:00+08:00 | 多 Agent 的隐式通信路径会把局部异常放大为条件性 contagion，隔离、message admission、recovery 与 effect authority 必须分开；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [First Token Matters](https://arxiv.org/html/2609.18471v1) | 2026-09-18T08:00:00+08:00 | reasoning model 的 refusal 可在首 token/onset 决定后快速崩塌，安全观测不能只检查最终文本；3 + 2 + 2 = 7 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Align, Integrate, and Fire](https://arxiv.org/html/2609.18516v1) | 2026-09-18T08:00:00+08:00 | speech encoder 的连续帧可按目标文本 token 长度对齐压缩，并以单层 distillation 限制训练成本；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [COMPASS-ABS](https://arxiv.org/html/2609.18519v1) | 2026-09-18T08:00:00+08:00 | shared GPU cluster 要区分 scheduler-induced 与 workload-inherent fragmentation，并将 compaction 代价纳入决策；2 + 3 + 3 = 8 | 深入完成 | 整合：`PLATFORM-GPU-SCHEDULER` [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) |
| [AeroWeaver](https://arxiv.org/html/2609.18520v1) | 2026-09-18T08:00:00+08:00 | 分布式 embodied agents 需要分离语义决策、受控 skill invocation、body-local observation、coordination report 与固定 executor；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；Ch26 handoff |
| [The evolution of sex for artificial intelligence](https://arxiv.org/html/2609.18560v1) | 2026-09-18T08:00:00+08:00 | 递归模型训练中真实样本的绝对注入量、父模型组合规则与冲突 convention 会改变漂移、互补与合并兼容性；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [How Many Labels Does Model Choice Need?](https://arxiv.org/html/2609.18622v1) | 2026-09-18T08:00:00+08:00 | 模型选择的标注证书必须绑定目标指标；disagreement labels 可闭合 accuracy choice，却可能无法闭合 AUGRC choice；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Selection Is Retrieval, Abstention Is Not](https://arxiv.org/html/2609.18672v1) | 2026-09-18T08:00:00+08:00 | tool selection 与 abstention 需要不同信号与校准，不能把 top-1 similarity 同时当两种保证；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [DyMT-ESB](https://arxiv.org/html/2609.18649v1) | 2026-09-18T08:00:00+08:00 | 固定脚本和固定轮数会隐藏 late-emerging、非单调与重新出现的偏差，评价必须把对话历史与 turn frontier 纳入状态；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [HBFlex](https://arxiv.org/html/2609.18675v1) | 2026-09-18T08:00:00+08:00 | fine-grained LLM state 与 coarse HBF execution 之间需要 plane-level layout/translation，而不是仅增加带宽；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [RayOrch](https://arxiv.org/html/2609.18703v1) | 2026-09-18T08:00:00+08:00 | foundation-model dataflow 需要跨粒度 lineage、replay 和 materialization 控制，才能使数据 artifact 可追溯；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Rethinking Critic Learning in PPO](https://arxiv.org/html/2609.18708v1) | 2026-09-18T08:00:00+08:00 | dense、相关的 state supervision 会导致 critic value flattening，需要更稀疏、分离的 anchor；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-PPO` [Ch32](../../../../books/part-04-training-system/32-ppo.md) |
| [Version- and Scope-Aware Question Answering over Normative Documents](https://arxiv.org/html/2609.18769v1) | 2026-09-18T08:00:00+08:00 | normative QA 的答案 identity 必须包含版本、生效期和 scope，不只是文本相似性；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Compositional Policy Violations](https://arxiv.org/html/2609.18820v1) | 2026-09-18T08:00:00+08:00 | 逐步合规不能推导组合 workflow 合规，policy monitor 要拥有跨步 joint state；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Infinite-Parameter LLMs](https://arxiv.org/html/2609.18842v1) | 2026-09-18T08:00:00+08:00 | hypernetwork 可把 live data 编译为低秩权重调制并在线更新 latent belief，但必须版本化会话、base checkpoint、provenance 与回滚；3 + 2 + 2 = 7 | 深入完成 | 整合：`MODEL-FFN` [Ch16](../../../../books/part-02-model/16-feed-forward-mlp.md) |
| [Ask the Tool, Don’t Guess](https://arxiv.org/html/2609.18849v1) | 2026-09-18T08:00:00+08:00 | tool-reported progress 可让 serving scheduler 估计返回后的 KV 复用价值，不再只猜 timeout；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Taming the Agentic RAN](https://arxiv.org/html/2609.18857v1) | 2026-09-18T08:00:00+08:00 | 独立正确的 agents 共享控制变量仍可产生对向振荡，需要显式 proposal arbiter、feasibility invariant、dwell 与 deadband；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Decodable but Misrouted](https://arxiv.org/html/2609.18860v1) | 2026-09-18T08:00:00+08:00 | supervised decodability 与 native output routing 是不同命题；knockout、feature patching 与 calibration-only recovery 才能定位 readout gap；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Preventing Model Collapse](https://arxiv.org/html/2609.18878v1) | 2026-09-18T08:00:00+08:00 | Fisher–Rao dynamics 给出 synthetic-data feedback 下的稳定阈值，但是受理论假设约束的边界而非通用配比；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [One Axis, No Brake](https://arxiv.org/html/2609.18998v1) | 2026-09-18T08:00:00+08:00 | Multi-Agent 的 self-knowledge 不足以为 harmful peer conformity 提供可靠刹车，minority evidence 与 consensus 必须分离；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Capability Emergence Can Be Forecast](https://arxiv.org/html/2609.19000v1) | 2026-09-18T08:00:00+08:00 | 能力监控需要 per-seed lead time、校准区间、负对照与 blind gate，不能把平滑 loss 或单一 precursor 当 release permission；3 + 2 + 3 = 8 | 深入完成 | 整合：`WORLDVIEW-LLM-INTELLIGENCE` [Ch8](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md) |
| [OAK](https://arxiv.org/html/2609.19024v1) | 2026-09-18T08:00:00+08:00 | 调度需要显式估计作业 age、restart cost 与已消耗 work，不能把 preemption 当无状态；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-GPU-SCHEDULER` [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) |
| [Monitoring and Discovering Reward Hacking with Internal Representations](https://arxiv.org/html/2609.19101v1) | 2026-09-18T08:00:00+08:00 | internal representation probe 可作 reward-hacking sensor，但不是 intent/truth detector，需要 independent outcome evidence；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [How Model Growth, Recursion, and Boundary Operators Influence Scaling Exponents](https://arxiv.org/html/2609.19107v1) | 2026-09-18T08:00:00+08:00 | architecture、growth rule 与 recursion/boundary operator 会改变拟合 scaling exponent，其不是脱离实验 identity 的常数；3 + 3 + 3 = 9 | 深入完成 | 整合：`WORLDVIEW-SCALING-LAW` [Ch7](../../../../books/part-01-worldview/07-scaling-law.md) |
| [Exponential Hardness of Off-Policy Evaluation under History-Dependent Logging](https://arxiv.org/html/2609.19135v1) | 2026-09-18T08:00:00+08:00 | 当前状态 coverage 不能替代 logger history identity；历史依赖可使 OPE 在有限 latent state 下仍需随 horizon 指数增长的样本；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Objective vs. Search](https://arxiv.org/html/2609.19145v1) | 2026-09-18T08:00:00+08:00 | tokenizer 应把 objective 与 search procedure 做 2×2 分解；BPB、语法边界和下游效果不是同一目标；3 + 2 + 3 = 8 | 深入完成 | 整合：`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [UnStep](https://github.com/facebookresearch/UnStep/tree/e7525751dc00582571cb3eea6e357cfa57db0843) | 2026-09-17T19:52:19+08:00 | 无训练视频 diffusion 加速组合少步 denoising、更小 KV window、cache refinement 与 runtime 优化；结论只绑定不可变初始 commit 的 artifact claim；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Multi-Agent Iterative Consensus under Delay v2](https://arxiv.org/html/2606.27409v2) | 2026-09-18T08:00:00+08:00 | 修正 delay indexing，收窄 stability/placement 声明；400-question factual study 因 abstention/completion bounds 未识别或证实振荡；重要修订，不重复评分 | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |

## 4. 证据与知识整合

本节给出面向读者的结论；63 个当窗候选与 `2606.27409v2` 的 exact-version Method、Evaluation、non-proof locator、采用命题和最终处置见 [逐项 Source Review notes](../_sources/daily-20260918/review-notes.md)。五项新增写入与两项既有实质绑定的锚点、长期语义增量和回退边界见 [Books queue](../_sources/daily-20260918/books-queue.md)。

### [Register Bias in Complexity-Based Large Language Model Routing](https://arxiv.org/html/2609.17542v1)

论文把相同问题改写为不同 register，测量 complexity-based router 的决策和后续效用，支持“路由不能只校准平均难度”的局部结论。它没有证明所有 router 都存在同等偏差，也没有提供新的调度状态机制；Ch56 已把路由的质量、成本、租户与 fairness slice 放入同一决策合同，因此判为已有覆盖。

### [Pay Only for Disagreement](https://arxiv.org/html/2609.17560v1)

方法利用新旧模型一致时 loss difference 为零的 support identity：先用无标注流量判断 disagreement rate，不足以直接证明时只标注 disagreement，再以 empirical-Bernstein confidence sequence 支持自适应停止。理论保证绑定有界 loss、可观测的配对预测与路由权重；不能替代 slice 定义、标注真值或 distribution shift 检测。Ch66 已将它整合为 model-update promotion 的“配对差值→只审分歧→anytime-valid verdict”测量路线。

### [GroupKV](https://arxiv.org/html/2609.17573v1)

完整方法将 diffusion LLM 的 token/group 状态按跨步变化分组，优先常驻或预取预计被再读的 KV；评价只支持披露模型和硬件配置下的带宽/延迟改善。分组错误会产生 staleness 和无效预取，所以 Ch45 将它收窄为分层驻留分支，保留 freshness/version 检查与 full recompute fallback。

### [Fathom](https://arxiv.org/html/2609.17652v1)

方法将离线 KV 量化为可逐层读取的 bitplanes，再按 query 估计还需读取的深度，使带宽开销与当次查询的误差需求绑定。结果不证明固定阈值可跨模型/任务复用；估计器失配时必须继续读取。Ch45 已将“存了多少”与“查询实际读了多少精度”分开。

### [REVERSAL-BENCH](https://arxiv.org/html/2609.17745v1)

方法在 reset-free embodied learning 中显式标记不可逆状态、recoverability oracle 与吸收态，说明失败后继续在线探索并非安全默认值。实验只覆盖作者的 physics engines、任务和 oracle；它不证明开放世界可逆或 recovery policy 普遍有效。Ch26 因而把 recoverability、停止条件和人工接管写入物理闭环，而不是把 reset 当作免费操作。

### [Beyond the Previous Layer](https://arxiv.org/html/2609.17940v1)

在控制最近层 expert choice 后，较早 routing history 仍含下一层选择的增量预测信息，可作为 expert residency 的 hint；实际 router 仍拥有执行权。证据只来自 frozen OLMoE/JetMoE 的预测结构，没有证明端到端 prefetch、吞吐或 SLO 改善。Ch54 将它收窄为 speculative placement 分支，并保留 miss fallback。

### [Causal-History Test-Time Scaling for Failure Recovery in Autoregressive World-Action Models](https://arxiv.org/html/2609.18016v1)

恢复路径被拆为 failure trigger、可靠 history prefix、causal KV reconstruction 与多假设 verification，而不是简单删除最后一步。有限仿真和实机 manipulation 不证明 prefix 总可恢复、隐藏状态可观测或高风险动作适合在线试错；Ch25 因此保留全历史、恢复前缀和完全重置三种假设及安全退出边界。

### [Towards Training Private LLMs on Apple Silicon with RDMA over Thunderbolt](https://arxiv.org/html/2609.18066v2)

多 trunk、持久 worker 与 CPU-side overlap 面向“大统一内存、低互联带宽”的训练拓扑，展示容量、通信和 acquisition cost 必须共同评价。四节点 Mac Studio、Qwen3-9B 与作者序列长度不能外推任意模型、规模、可靠性或隐私保证；Ch36 已由异构拓扑与通信重叠主线承载，无需新增机制。

### [When Is Graph Structure Worth Its Cost?](https://arxiv.org/html/2609.18099v1)

GraphRAG 的结构收益必须与 ingestion/query 模型调用成本及原文 evidence 保真共同评价，不能只比较答案质量。120 个问题、四个领域和单一主要 baseline 不证明普遍优势；Ch76 已把图构建成本、查询成本、provenance 与回答质量放在同一 evaluation identity 中。

### [SSD-LLaMA](https://arxiv.org/html/2609.18110v1)

超大 MoE 的本地执行把 SSD expert-pack、异步读取、DRAM/VRAM cache 与 CPU-GPU work split 合成一套 execution plan；“SSD 容得下”不等于 token latency 可接受。结果绑定作者模型、量化、RTX 5090、RAM/SSD 与 benchmark，不能外推任意 tail latency 或耐久性；Ch54 的多层 residency 已完整承载。

### [Reaching Every Position Without Searching](https://arxiv.org/html/2609.18145v1)

跨层旋转的 fixed sparse wiring 可在对数深度建立全局可达性，却不等于内容自适应选择。小型字符模型、短窗口和固定 step budget 不证明它可替代通用 LLM Attention；Ch14 将其作为稀疏连接的 alternative branch，并保留动态选择与表达能力边界。

### [Faithful yet Collusive](https://arxiv.org/html/2609.18346v1)

论文区分 CoT 的 structural/intent faithfulness 与真实行为 effect，说明可读 trace 不能独立判定多 Agent 联合策略安全。有限模型和 Bertrand pricing simulation 不证明现实市场共谋率；Ch72 因此要求 trace sensor 与 execution/effect evidence 分权。

### [GeoMesh](https://arxiv.org/html/2609.18388v1)

geo-distributed synchronous training 用 per-worker batch/inner-step plan 与 sign-compressed pseudo-gradient 减少异构等待，同时改变聚合权重、local work 与 compression state 的身份。150M～500M 模型和作者 WAN/GPU 设置不证明大规模收敛、非 IID 数据或故障恢复；Ch36 将收益与 objective drift、压缩误差和恢复状态一起记录。

### [Collective Loss of Control in LLM Agent Systems](https://arxiv.org/html/2609.18460v1)

特定 pending-call transport 中，隐式通信可把局部异常放大成条件性 contagion，因此隔离、message admission、recovery 与最终 effect authority 必须分别拥有状态。论文未测自然 rare-event rate，也未证明 autonomous cascade；Ch72 只吸收控制面分权，不外推普遍风险率。

### [Infinite-Parameter LLMs](https://arxiv.org/html/2609.18842v1)

hypernetwork 将 live data 编译为低秩 FFN 调制并更新 latent belief，使权重本身成为带生命周期的派生状态。小规模受控实验不证明无限容量、生产持续学习稳定性、隐私或跨租户隔离；Ch16 要求生成权重绑定 base、session、provenance、validity 与 rollback。

### [Capability Emergence Can Be Forecast](https://arxiv.org/html/2609.19000v1)

能力 early warning 需要 per-seed lead time、calibrated interval、manufactured negatives、false-alarm bound 与 blind gate；precursor 只是风险传感器，不拥有 release authority。合成/小模型和有限公开 families 不证明任意新能力均可预测，Ch8 因而保留负对照与不可预测边界。

### [Exponential Hardness of Off-Policy Evaluation under History-Dependent Logging](https://arxiv.org/html/2609.19135v1)

构造结果表明当前状态/行为边际 coverage 不能替代 logger history identity：即使 latent state 很少，history dependence 仍可使 OPE 样本需求随 horizon 指数增长。这不表示所有 OPE 不可用，也不给出生产 estimator 的统一阈值；Ch66 要求无法证明 Markov sufficiency 时报告不可识别或扩大 uncertainty。

### [Accelerating Diffusion Sampling via Speculative Draft Trees](https://arxiv.org/html/2609.17691v1)

论文以 draft tree 一次提出多个 diffusion 转移，再由高保真过程验证/校正，支持“proposal 可并行，commit authority 不能丢”。评价只是特定 sampler 的 operating point，不支持对所有 diffusion workload 的通用加速结论；Ch48 已覆盖提议、验证、rollback 与 exact/lossy 分支。

### [SFT or RL for Tool-Calling Agents?](https://arxiv.org/html/2609.17848v1)

作者在数据、方法和模型规模上做受控比较，但证据支持的是条件分支而非“RL 总是更好”。当 demonstration 已充足时 SFT 仍然合理；需要在线探索且 verifier 可靠时 RL 才可能改变边界。Ch29–Ch33 已以数据覆盖、reward 可验证性与 rollout identity 组织同一路线，不重复追加。

### [Who Judges Matters](https://arxiv.org/html/2609.17857v1)

论文对多 judge panel 的 family-conditioned preference 进行配对测量，表明面板一致也可能是共享偏差。结果受候选模型、rubric 和样本分布限制，不等于 judge family 的固定可靠性排名。Ch66 已要求 multi-family judge、human/grounded control 和 disagreement 审计，因此已有覆盖。

### [Timely Activation of Safety Filters via One-Step Reachability Expansion](https://arxiv.org/html/2609.17904v1)

连续时间 HJ filter 假设可随时介入；数字 controller 只在离散时刻更新，因此状态可能在下一次更新前一步跨入 unsafe BRT。论文以最坏情况一步可达域扩张触发边界，在理想假设下给出安全命题，却没有证明现实系统已经闭合：Dubins-car 仿真采用精确动力学与完美状态，扩张分支在不同采样周期的 100 次运行中仍只有 67–86 次安全，作者也明确说明 continuous-discrete mismatch 尚未完全消除。Ch26 已把 reachability、采样周期、扰动界与 actuator delay 绑定为 safety identity，并保留降频、硬件急停和停止高层 policy 的回退，因此本次核实既有唯一绑定而不重复写入。

### [Locating Hidden Failures Makes Long-Horizon Agents More Reliable](https://arxiv.org/html/2609.17930v1)

方法在长 trajectory 中标定局部 failure location 并使用定点修正，实验支持 process supervision 对所测任务的改善。它不证明定位器拥有真值，也不能用局部标签代替最终 outcome。Ch66 已把 step/trajectory/outcome 指标和定位不确定性分开。

### [ASPIRE](https://arxiv.org/html/2609.17943v1)

系统允许同一 batch 中不同请求独立处于 draft 或 verify 阶段，用每请求的确认前缀屏蔽异步执行与正确性之间的冲突。收益绑定长上下文、披露模型/硬件和调度策略，不可外推为固定加速比。Ch48 已整合 per-request frontier、mixed-stage batching、rollback 和 verifier authority。

### [Contiguity, Not Importance](https://arxiv.org/html/2609.17983v1)

论文从 causal dependency 定位 document edit 后必须修复的连续 KV 区间，再在预算下选择修复边界；它反驳了“抽取最重要 token 就足够”的无条件做法。评价不证明修复窗可跨架构固定，因此 Ch45 保留 edit identity、position shift、可验证 repair frontier 与 full recompute 回退。

### [The Attention Within](https://arxiv.org/html/2609.17997v1)

论文在 continuous-time Mamba-2 depth dynamics 中分析 consensus equilibria：persistency-of-excitation 支持局部指数稳定，更强正定条件给出吸引域；time-varying weights 可中断趋同，output gate 会缩小最终输出中可见的 consensus extent。它不证明实际离散网络、任意输入或任务质量必然趋同。Ch22 已把这项增量整合为“state convergence 与 output observability 分开验收”的受限分支。

### [A Calibrated Instrument for Measuring How Inference Optimizations Affect Output Quality](https://arxiv.org/pdf/2609.18005v1)

论文的 dual reference 估计同模型采样噪声，exchangeability null 检查 judge 仪器，strict speculative arm 作 implementation null，再用预注册等价界而非“不显著”判断质量无退化。Qwen2.5-7B/Llama-3.1-8B、220 prompts 与特定量化/早退出配置只证明该 instrument 的受限 operating point，数值不能外推。Ch66 已将 null、positive control、power、equivalence 与 workload identity 串成统一优化评价合同。

### [The Other Half of the Memory Wall](https://arxiv.org/html/2609.18063v1)

系统不是先预测 expert、再等待真实 router 并处理 prefetch miss；per-layer prerouter 的预测直接成为下一层 routing，使 SSD→GPU 读取可与当前层计算重叠。近似误差由沿 student routing path 训练的 Recovery LoRA 补偿，serving 时保持未合并，避免 merge 后重新量化抹掉恢复收益。它以重训、额外 LoRA state 与质量偏差换 I/O overlap，证据绑定论文模型、Mac 硬件和高方差同 session A/B 协议。Ch54 已将它作为不同于 router-confirmed prefetch 的 trained-routing 分支整合，并保留常驻、on-demand 与普通 prefetch 回退。

### [Decodability is Not Causality](https://arxiv.org/html/2609.18080v1)

论文不停留在 linear probe，而以 SAE decomposition 和 intervention 检查“可解码特征”是否真正驱动行为，支持 decodability/causality 的分离。干预仍受 SAE 分解完整性、off-manifold effect 和任务范围限制。Ch66 已把 probe 降级为诊断传感器，必须用 causal intervention/outcome 才能升级命题。

### [Token Latency Fairness](https://arxiv.org/html/2609.18112v1)

论文把多租户推理的隔离对象从平均 request latency 下沉到每个 token，以相对独占 baseline 的额外 compute/cache delay 设定 `δ` 边界。该边界受 workload mix、cache policy 和 admission 影响，不能脱离 SLO 复用。Ch56 已将 token-level isolation、驻留拖延、抢占代价和吞吐损失纳入调度目标。

### [AutoTuneBench](https://arxiv.org/html/2609.18123v1)

评测把 agent 修改 serving configuration 的过程置于可回放的 baseline、固定机器和 workload saturation 条件下，分开 throughput/latency 改善与 correctness/validity。其任务集和配置范围不证明任意 agent 可安全自动发布。Ch66 已将 machine image、engine/version、workload、baseline、provenance、validator 和 rollback 收敛为自动调参证据合同。

### [Symbolic Temporal Supervision of LLM Agents Using Contracts](https://arxiv.org/html/2609.18128v1)

方法将时序规则表达为 symbolic contract，监视 agent 事件序列而非只检查单步输出，支持跨步违约的定位。contract 覆盖与 event instrumentation 决定它能看到什么，未观测环境状态仍是 Unknown。Ch81 已把 durable workflow state、temporal invariant、monitor 和 commit gate 分开，因此不重复追加。

### [Zero-I/O Fault Recovery](https://arxiv.org/html/2609.18178v1)

论文的核心不是“不要 checkpoint”，而是在 fail-stop 且 survivor 已共同 commit optimizer step 的窄边界内，动态重绑 framework handle/process group 并恢复 sharded runtime。证据中两项实验不能混为一谈：1.216B decoder、4×RTX 5880、local NVMe 只测 per-update DCP 的 I/O backpressure；十次连续 fault 注入则使用完整 Mistral-7B-v0.3、4 节点共 16×RTX 5880、1 Gbps Ethernet，在 25 updates 中验证最终 frontier bit-identical。丢失唯一 state shard、silent corruption、跨步不一致或整个 job 丢失时仍需 durable checkpoint。Ch36 已分开记录两组 evaluation identity，并将 committed step、存活状态所有权、rebind 与 checkpoint fallback 写成恢复分支。

### [Beyond Accuracy](https://arxiv.org/html/2609.18204v1)

论文比较只看最终答案与附加 procedural trace 时 overseer 的决策变化，表明 trace 会改变判定阈值而非只增加信息。它不证明过程观测者一定比 outcome 更真实。Ch66 已要求 process/outcome 独立指标、blinding 和 criterion-shift 审计。

### [BENCHCOMPASS](https://arxiv.org/html/2609.18270v1)

论文把同一 payment-domain 模型分别放进 closed、open 与 attacked-open harness，并为每个问题生成带来源定位的 evidence pack 和 answer-preserving perturbation，因而能把“模型本身不知道”与“上下文存在但没有被稳定使用”分开。306 个专家最终接纳的案例只支持该领域和所测 harness；repair hypotheses 不是已验证的因果修复，也没有评价 retrieval、tools 或 multi-agent。Ch66 需要新增这条三条件对照链，但不得把作者 benchmark 外推成通用能力排名。

### [Bias Amplification in Multi-Agent Network](https://arxiv.org/html/2609.18306v1)

受控 Llama 3.2 网络实验显示，持续偏置少数可以推动中立 agents 的数值意见，同时让修辞词汇向偏置方向对齐；两条曲线并不必然同步。结果来自单一模型族、四个主题、理想化网络和 15 次重复，不能当生产 incidence。Ch82 已要求把 belief state、message effects、herding 与 correlated error 分开测量，因此作为受限案例已有覆盖。

### [Beyond Quadratic Loss](https://arxiv.org/html/2609.18314v1)

论文分析非二次 loss 下 Adam 的相图，表明 `β1/β2`、局部 curvature 与 gradient noise 共同决定稳定/振荡区，否定脱离 workload 的普遍最优 momentum。理论与实验不等于为任意 LLM 直接给出 hyperparameter。Ch28 已把它整合为“平滑器参数是优化动力学的一部分，需随曲率/噪声与训练阶段验证”。

### [The Mirage of Calibrated Confidence](https://arxiv.org/html/2609.18453v1)

论文比较不同推理 trajectory 与 verbalized confidence，发现文本置信度可能对路径改变不敏感，即使表面 calibration 可接受。证据限于所测 VLM/任务，但足以反驳“单次自报置信度可当 truth probability”。Ch66 已将 verbal confidence、行为一致性、evidence support 与 abstention calibration 分开。

### [First Token Matters](https://arxiv.org/html/2609.18471v1)

论文定位 reasoning model 在输出起始阶段的 safety onset，显示首个 token/早期方向选择会使后续长推理远离 refusal 轨道。它不证明一个通用内部“安全开关”，也不保证特定 anchor 跨模型有效。Ch72 已将 onset monitor、trajectory-level policy check 与 final-output guard 组成多层防护。

### [COMPASS-ABS](https://arxiv.org/html/2609.18519v1)

方法区分由 scheduler placement 造成的可修复碎片与 workload shape 本身的不可避免空洞，再在作业搬迁/压紧代价下决定是否 compact。结果受 cluster topology、queue 和 workload trace 限制，不支持固定 compaction 周期。Ch63 已整合 fragmentation provenance、收益阈值、移动代价与不打扰现有作业的回退。

### [AeroWeaver](https://arxiv.org/html/2609.18520v1)

系统把角色条件的语义决策、受治理的 skill invocation、body-local observation、coordination report、固定低层 executor 和角色索引 memory 明确分层；各 agent 基于局部状态行动，而不是由中央模型一次生成 joint action。九个 MPE-inspired 闭环任务与组件消融只证明该模拟 harness 的 operating point，不证明真实飞行安全、sim-to-real 或 reward adaptation 的普遍性。Ch82 已拥有 role/authority/communication-state 主线，Ch26 只保留 embodied execution handoff，因此不重复扩章。

### [How Many Labels Does Model Choice Need?](https://arxiv.org/html/2609.18622v1)

论文把模型选择写成由目标指标、容忍度和标注查询共同决定的证书问题，而不是把 prediction agreement 当统一代理。在 108 个 panel comparisons 中，disagreement labels 闭合了全部 accuracy choice，却没有闭合任何 AUGRC choice，直接证明相同候选模型的 label budget 会随 selection objective 改变。该结果只覆盖固定 pool、固定候选预测/排序、binary 或共享 multiclass predictions 与 `K<=8`，不证明 retraining、transfer 或分布漂移下仍有相同预算。Ch66 已要求 metric-specific certificate、不可区分候选集与目标变化后的重新采样，本次核实其唯一实质绑定而不重复写入。

### [Selection Is Retrieval, Abstention Is Not](https://arxiv.org/html/2609.18672v1)

论文在 70 个韩英双语 on-device actions 上分开“选哪个工具”与“是否应调用”，显示后者不能由前者的 top-1 score 直接推出。该 action set、语言和设备限制数值外推。Ch78 已要求 candidate retrieval、schema validation、abstention threshold 和 effect authorization 独立验收。

### [DyMT-ESB](https://arxiv.org/html/2609.18649v1)

方法让后续用户 turn 依赖模型上一轮响应，并比较 5-turn 与 10-turn 对话，从而暴露固定脚本会漏掉的 late-emerging、非单调和重新出现的偏差。240 个 seed stereotypes、六类偏差、六个目标模型及 human judge validation 支持“对话状态必须进入 evaluation identity”；但用户是合成的，generator/judge 主要依赖 GPT-4o-mini，也不代表真实用户发生率。Ch66 需要把 conversation history、turn frontier 与动态停止条件写入多轮评价合同。

### [HBFlex](https://arxiv.org/html/2609.18675v1)

论文将 LLM 细粒度 state 切分为可映射到 coarse-grained HBF transfer/execution 的 plane，并显式处理 layout conversion 和并发传输。结果依赖特定 memory fabric 与 workload，不表明 HBF 是任意集群的默认选择。Ch54 已从 state granularity、placement、layout conversion、搬运/计算 overlap 与 fallback 承载同一路线。

### [RayOrch](https://arxiv.org/html/2609.18703v1)

系统把数据准备流程的 dataset/file/record 多粒度操作放在 lineage-controlled execution 中，使中间 artifact、失败恢复与增量重算可定位。性能数值绑定 Ray 实现和测试 pipeline，机制上不要求采用特定框架。Ch27 已覆盖 data lineage、versioned transformation、materialization、replay 和验证。

### [Rethinking Critic Learning in PPO](https://arxiv.org/html/2609.18708v1)

论文将 value flattening 定位为长 trajectory 上高相关、稠密监督的副作用，通过稀疏且彼此分离的 value anchors 恢复状态区分度。证据不证明 anchor 策略对所有 reward/trajectory 都有效，过稀会提高 variance。Ch32 已将它整合到 critic target correlation、bias/variance 与 fallback 的设计分支。

### [Version- and Scope-Aware Question Answering over Normative Documents](https://arxiv.org/html/2609.18769v1)

部署系统把 normative documents 的 version、生效时间和 applicability scope 放入 retrieval/answering identity，并用端到端评价观察错版本回答。单一部署不证明所有法规/手册 QA 的完整性。Ch76 已要求 evidence chunk 保留 source/version/time/scope，生成答案不能脱离这些条件。

### [Compositional Policy Violations](https://arxiv.org/html/2609.18820v1)

论文构造单步看似合规但跨步组合违规的 agent workflows，直接反驳局部 guard 的合成性假设。benchmark 的 policy 和 workflow 不覆盖现实中所有 joint failure，但机制足以要求跨步 stateful monitor。Ch72/Ch81 已有 joint invariant、durable state、effect log 和 final commit gate，因此无需复制案例。

### [Ask the Tool, Don’t Guess](https://arxiv.org/html/2609.18849v1)

方法从 agent tool call 中提取进度/剩余工作信号，帮助 scheduler 判断暂时缓存或驱逐 KV 是否值得，改变了请求状态的可观测边界。信号可被工具估错或敌意上报，必须绑定 confidence、timeout 和 conservative fallback。Ch56 已将 tool-reported progress 作为调度 hint，不作 authoritative truth。

### [Preventing Model Collapse](https://arxiv.org/html/2609.18878v1)

论文在 Fisher–Rao geometry 下分析真实/合成数据混合动力学，给出避免分布退化的条件阈值与不稳定区。结论受模型化假设、生成分布和训练动力限制，不能直接转换为产线固定 synthetic ratio。Ch27 已将它整合为条件理论，并保留真实 holdout、lineage 与 collapse monitor。

### [One Axis, No Brake](https://arxiv.org/html/2609.18998v1)

实验显示模型对自身能力/置信的估计不能稳定阻止有害 peer conformity，一致性可能是 herding 而非 truth alignment。结论受所测交互协议和模型限制，不表明多 Agent 必然比单 Agent 差。Ch82 已将 consensus、minority evidence、independent verification 和 confidence 分开。

### [OAK](https://arxiv.org/html/2609.19024v1)

调度器将 job age、restart overhead 和已完成 work 带入 placement/preemption，避免只看当前优先级而反复杀死快完成或恢复很贵的作业。trace-driven 结果不支持固定权重跨集群复用，且过度保护老作业可造成 starvation。Ch63 已整合 age/restart-aware cost，同时保留 quota、deadline 与 fairness guardrail。

### [Monitoring and Discovering Reward Hacking with Internal Representations](https://arxiv.org/html/2609.19101v1)

论文训练 representation-level probe 检测所测评价中的 reward hacking，并用干预/迁移实验检查信号。内部可分性不等于 intent、truth 或因果机制，probe 还可被分布漂移和适应性对手破坏。Ch72 已将此信号定位为多传感器之一，必须与 outcome、trace 和独立 verifier 交叉验证。

### [How Model Growth, Recursion, and Boundary Operators Influence Scaling Exponents](https://arxiv.org/html/2609.19107v1)

论文分析模型增长、递归和边界算子如何改变观测到的 scaling exponent，使“幂律参数只由数据和 compute 决定”的简化叙述失效。证据不足以提供跨架构通用指数，而是要求报告 architecture/growth/operator 身份。Ch7 已整合该边界，并保留旧 scaling law 在固定实验族内的有效性。

### [Objective vs. Search](https://arxiv.org/html/2609.19145v1)

论文把 tokenizer objective（compression 与 likelihood）与 search direction（top-down 与 bottom-up）正交分解，用匹配模型规模、语料和词表的实验区分它们的影响。BPB、词法边界、代码/URL 压缩与 downstream 能力不是同一目标，且局部删除近似在大规模下仍有未知误差。Ch11 已将“目标与搜索分开验证”整合到 tokenizer 演进主线。

### [Whom Do AI Agents Work For?](https://arxiv.org/html/2609.17989v1)

两个受控 choice studies 只改变 system prompt 中被指定的 principal，并观察 sponsored listing 的选择与 disclosure reasoning；platform-delegated agent 对 sponsorship 的惩罚和质疑更弱，且更严格的 disclosure wording 没有消除差异。该结果受所测购物场景、模型与角色措辞限制，不证明任意 system prompt 都产生固定偏差，也不证明 reasoning trace 等于真实决策机制。Ch74 已把 prompt 视为携带角色、权限和利益边界的输入，并要求外部 policy/evidence 验证，而非把角色描述当作无害文案，因此已有覆盖。

### [Market Signal Injection](https://arxiv.org/html/2609.18357v1)

论文保持市场数值不变，只改变格式、竞争者顺序或定性评论，显示 data presentation 本身可以成为 LLM agent 的攻击面；matched neutral controls 与 rule-based agent 支持 framing account，但 activation probe 的高可分性不等于识别了有害决策。输入 canonicalization 在所测攻击上有效，prompt constraint 加 output projection 的 decision-boundary anchoring 在 adaptive attack 下只部分缓解。Ch72 已在“指令注入”之外补上 untrusted data presentation、canonicalization 与最终 effect boundary 的分层防御。

### [Planning or Improvisation?](https://arxiv.org/html/2609.18440v1)

研究把“模型提前规划押韵”拆成位置特异性、newline 位点身份和 newline-resident plan 三个可证伪命题。四个开放模型与六个开放 CLT 能复现原图的形状，却把有效位点定位到 emission-adjacent final prompt token；newline feature census、长程 steering 和 residual patching 均未恢复原机制。论文明确不是 faithful reproduction，且小模型/开放 transcoder 结果不能否定其他模型存在规划。Ch66 已要求复现时区分表面曲线、测量位点、干预和因果机制，因此该负证据为已有覆盖。

### [Align, Integrate, and Fire](https://arxiv.org/html/2609.18516v1)

ACIF 利用 DTW alignment 把连续 speech frames 动态压缩到目标文本 token 的精确长度，第一阶段绕过完整 LLM forward，后续以单层 knowledge distillation 控制训练内存。ASR 与 speech translation 结果只证明作者模型、语言和任务下的效率/质量 operating point；目标文本 alignment 在真正 zero-shot 输入时仍依赖训练阶段得到的桥接关系。Ch23 已覆盖 modality-specific encoder、连续到离散的 sequence-length 对齐、projector 与 distillation 边界，因此无需重复机制。

### [The evolution of sex for artificial intelligence](https://arxiv.org/html/2609.18560v1)

论文把 recursive model-output training、multi-parent composition 与 model merging 放进一个可检验的 inheritance framework：exact model、训练网络和 LLM 案例共同支持真实样本的绝对注入量会改变漂移，多父输出的简单平均可能消掉互补，而保留各父模型最强贡献或合并 specialists 才可能获得组合收益；冲突 conventions 比一般参数漂移更能预测 merge incompatibility。生物学对应关系不是普遍 LLM 定律，实验规模与模型族也不足以给出固定配方。Ch27 已将 corpus recursion 与 parameter inheritance 分开，并显式记录 immigration count、parent composition、disagreement 与 merge fallback。

### [Taming the Agentic RAN](https://arxiv.org/html/2609.18857v1)

live O-RAN 实验显示，两个各自目标正确的 agents 共同写共享 resource partition，仍会产生任何单个 agent 都不会造成的对向振荡。AURA 把各 agent 降为 proposal producer，由 arbiter 检查 feasibility invariant、per-variable dwell 和 deadband，并在论文假设下证明收敛；它降低了共享状态振幅和 cross-slice starvation，却没有改善受保护 slice 自身的 latency compliance。结果绑定 O-RAN 变量和单变量 proposal schema，复合动作仍需更强 coordinator 或人工 fallback。Ch82 已将 shared control variable、proposal authority、commit owner 和 convergence/fairness trade-off 写成明确的 coordination contract。

### [Decodable but Misrouted](https://arxiv.org/html/2609.18860v1)

论文在六个 harmful-content 多模态任务上发现 sparse probe 能读取 native head 未使用的判别信息，并以 feature knockout、routed-feature patching 及 calibration-only routing/LoRA 分开测试“可读”与“真正进入输出路径”。它没有证明 supervised probe 等于模型原生决策规则；干预样本数较小、比例随尺度敏感，LoRA 还出现负迁移。Ch66 已明确要求把 decodability、causal intervention、routing/decision authority 与 recovery 分开，因此属于现有覆盖。

### Fresh-context 复核恢复的候选

初次宽筛把一批“实验规模有限但确实改变系统 contract”的材料误归为局部方法。复核后恢复的 13 项不是因为主题相关便进入分母，而是分别改变了长期状态、控制权或评价边界：REVERSAL-BENCH 把物理环境的可逆性和恢复 oracle 纳入 embodied loop；causal-history recovery 把失败后的 KV/history 重建变成显式三分支验证；旋转稀疏 wiring 说明全局可达性与内容自适应选择并不等价。这三项分别进入 Ch26、Ch25 与 Ch14，并保留只在作者任务、窗口和小模型上成立的证据边界。

GeoMesh 把异构 WAN 训练中的 per-worker workload、local steps、压缩 residual 与聚合权重绑定为同一 step identity；较早层 MoE routing history 只取得 residency hint，不取得下一层路由权；Infinite-Parameter LLM 的 live-data weight modulation 则要求 base checkpoint、session、provenance、有效期和 rollback 共同版本化。对应机制已分别整合到 Ch36、Ch54 与 Ch16。Apple Silicon over Thunderbolt 的多 trunk/CPU overlap 是受限硬件分支，Books 已有异构拓扑与 communication-overlap contract，故不重复追加。

SSD-LLaMA 的 expert-pack、SSD/DRAM/VRAM tier 与 CPU-GPU work split 已由 Ch54 的 expert paging/多层 residency 主线承载；EffiRAG 的结构成本与质量联合评价已由 Ch76 的 GraphRAG budget/provenance contract 承载，二者均为现有覆盖。Capability Emergence 的价值不在宣称“能力可预测”，而在要求 per-seed lead、校准区间、负对照、false-alarm bound 和 blind gate；history-dependent logging 的 OPE 下界则否定“当前状态覆盖足够便可闭合评估”。这两项分别进入 Ch8 与 Ch66。

最后，两项安全材料共同纠正了“可读解释等于安全证据”：pricing-agent 实验区分 CoT 的结构/意图 faithfulness 与真实联合行为，RogueHandoff-20 则只证明特定隐式通信路径下的条件 susceptibility，不证明自然 cascade 发生率。Ch72 因而明确把 trace、message admission、execution isolation、recovery 和最终 effect evidence 分开；其有限模拟结果没有被外推为普遍风险率。本轮定点返修又从标题层恢复五项：BENCHCOMPASS 与 DyMT-ESB 已写入 Ch66；Bias Amplification、AeroWeaver 与 Decodable but Misrouted 分别由 Ch82 与 Ch66 的既有具体命题承载。它们不改变此前已通过候选的证据结论。

### [UnStep](https://github.com/facebookresearch/UnStep/tree/e7525751dc00582571cb3eea6e357cfa57db0843)

官方仓库初始 commit `e7525751dc00582571cb3eea6e357cfa57db0843` 披露的无训练加速以更少 denoising steps、更短 KV attention window、clean-cache refinement、truncated SVD 与 DiT/VAE runtime 优化组合视频 diffusion 推理。当窗只有 artifact/README 与其绑定配置的性能声明，没有可足以采用新普遍机制的论文证据；Ch24 已将 step budget、KV window、cache refinement 和 runtime co-design 作为可组合但需独立测量的层次，因此 No Change。

### [Multi-Agent Iterative Consensus under Delay v2](https://arxiv.org/html/2606.27409v2)

v2 修正 delay indexing，收窄稳定性与 corrector-placement 声明，并增加 400-question factual study 与完整 response logs。synthetic linear recurrence 支持其假设下的 delay-induced oscillatory boundary；grounded factual QA 因大量 abstention，使 conservative completion bounds 同时允许 error amplitude 增加或降低，因而没有识别或证实同类振荡，也不能据此断言 truth 是 absorbing boundary。placement approximation 仍是 surrogate，不能外推为任意 Multi-Agent 共识定律。Ch82 已据此改写 completion/abstention-aware measurement boundary；该修订作为重要 revision 整合，不重复评分。

## 5. 缺口与下一步

14 项定点返修已完成：`2609.17555`、`2609.18959`、`2609.19006` 的 first-public date 早于本窗，作为前日 owner 去重；`2609.17800`、`2609.17977`、`2609.18045`、`2609.18120`、`2609.18416`、`2609.18496` 在完整摘要后以具体理由关闭；`2609.18270`、`2609.18306`、`2609.18520`、`2609.18649`、`2609.18860` 恢复为候选并完成 exact-v1 Source Review。closure 抽检发现的 `2609.18622v1`、`2609.17904v1` 也已按最小 checkpoint 重开并完成 exact-v1 Evidence、评分、Books 比较与 queue；未重扫其余 619 项。

更新后 `621 = 62` 个当窗 arXiv 候选 `+ 24` 个前日 owner `+ 122` 个完整题摘关闭 `+ 413` 个标题关闭；UnStep 另计后为 63 个候选。再加 `2606.27409v2` 这一不重复评分的重要 revision，候选表共 64 条，其中 38 项 Integrate、25 项 Existing Coverage、1 项 revision。

两项新恢复材料均不是待写 Books：Ch66 已有 `2609.18622v1` 的 metric-specific model-selection certificate，Ch26 已有 `2609.17904v1` 的 sampled-control one-step reachability safety boundary；两个 source-family marker 均唯一、正文均位于章末 `Review notes` 之前，并与本次 exact-v1 证据边界一致。为避免重复与破坏章节主线，本次只修正 Report、ledger、Review notes 与 Books queue，不修改 Books。fresh-context 复核已通过，本日无剩余内部 Gate。

已隔离的外部限制均为本窗终态保留项；它们不支持正面证据、Books 或无遗漏断言，也不阻塞已确认材料的 Daily 终态。每项均给出定点重开条件：

- Anthropic 的 frontier-lab measurement 条目只有 `2026-09-17` 日期，缺原始公开时刻而无法确认是否落在 09-17 09:00 之后；若取得带时区的 `publishedAt`/官方 feed，只重开该 identity 的归属与证据审阅。
- OpenAI Research、DeepMind、Qwen、Hunyuan 的日级完整目录枚举受限；MiMo 公开卡片缺稳定时刻。若未来获得当窗原始列表或唯一事件身份，只定点重开对应来源/事件，不重扫其他已闭合来源。

窗外纠错：`2605.06850`、`2608.04765` 的后续撤回已完成原 owner Daily 的正面链路清理；其他撤回信号未在当前 Report/Books 发现正面痕迹。

校验范围隔离：`books/part-02-model/11-tokenizer.md` 存在本轮开始前已有的 Markdown 语法问题；本轮没有修复或扩大该无关改动。最终验收只可声明 09-18 Report、当日 `_sources`、本轮触及的语义段落与 Git whitespace/diff 检查通过，不能据此宣称全仓 Markdown 已清洁。

## 6. 复核

返修作者：`/root/sep18_final` 定点返修（2026-09-21）

复核者：独立非作者终审（`/root/sep15_close`，未参与本日报作者筛选、返修或 Books 写入）

结论：通过

前一轮 non-author audit 已验证 14 项返修的 `3 earlier owner + 6 closure + 5 restored` 分流、原有 62 条候选/修订账目，以及 `2609.18270`、`2609.18649`、`2609.18357`、`2609.18560`、`2609.18857` 的五个唯一 Books 绑定；但 closure 抽检发现 `2609.18622v1` 与 `2609.17904v1` 两项 false negative，因此未通过。

终审严格限定在最小 checkpoint，没有重扫其余 619 项。`2609.18622v1` 的 exact-v1 正文支持 metric-specific certificate、108 个 panel comparisons、accuracy/AUGRC 分化及其固定 pool、固定候选预测和 `K<=8` 边界；`2609.17904v1` 支持 continuous-to-discrete mismatch、one-step reachable expansion 与 Dubins-car 每设置 100 次仿真，同时明确扩张分支仍只有 67–86 个 safe outcomes，不能外推真实机器人安全保证。两项的 3/2/3=8 评分和 Books Decision 与窄证据一致。

最终账目可复算为 `621 = 62 + 24 + 122 + 413`；UnStep 另计后 63 个候选，加 1 个 revision 后候选表 64 条。表内 39 行标为 Integrate，其中 `2606.27409v2` 是不重复评分的 revision，故最终处置正好为 38 Integrate、25 Existing Coverage、1 revision。Ch66 与 Ch26 的对应 source-family marker 各自在全书唯一，均位于章末 `Review notes` 之前，正文包含机制、证据边界、trade-off、failure 与 fallback；没有论文名占位或重复写入。Cross-model skipped: non-interactive subtask context.
