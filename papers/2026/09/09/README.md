# Daily Research — 2026-09-09

**规范：** V3
**窗口：** 2026-09-08T09:00:00+08:00 ～ 2026-09-09T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-09T09:20:48+08:00

## 1. 结论

本窗按十四个每日来源检查，在日期、同族去重与题摘/变更说明的贡献判断后保留 11 个材料家族：1 项多模态模型与安全发布，2 项 UniRL 分布式控制/接口变更，3 项 VeOmni 训练正确性修复，4 项 Kimi Code Agent runtime 变更，以及 1 项 MiniMax provider evaluation contract。机构页面上的合作、社会项目和本阶段暂缓的 AI for Science 在候选前关闭；仓库内文档、命名、UI、单领域 reward/scorer 与无行为变化的普通重构也没有因“属于 AI 项目”而进入候选。

arXiv 的 cs.AI、cs.CL、cs.LG、cs.DC 官方 new-list 页面仍停留在北京时间 09-07 08:00 已由 09-07 日报拥有的 Monday batch，本窗没有新的 owner identity，也没有复读 revision history。OpenAI 8 月 25 日发布的 Jalapeño 首批结果虽在 9 月 8 日公司文章中被再次引用，但其 primary event 与 benchmark 均属旧 family，本日不重复评分。

11 项均完成与处置强度相称的 primary-source 审阅和 Books 对读。七项长期机制增量已写入 Ch35、Ch36、Ch81、Ch83、Ch84：训练退出必须等待异步 checkpoint，rank-local failure 要先暴露并毒化失效执行域，collective 需要 buffer/mask/ownership correctness，Agent cancellation 必须由 scope owner 发出，长 observation 要有可验证 continuation，MCP 的 human-readable 与 structured result 不能互相替代，opaque reasoning continuation state 必须按 provider contract 原样回放。其余四项由现有章节完整承载。非作者独立复核已核对时间、来源、候选、证据边界、评分和实际 Books 写入，并校准了局部 correctness PR 的 System Reach；本窗没有普通 Evidence、Books 或复核待办。

## 2. 来源覆盖

本轮只检查每日来源，没有扫描每周来源。“已检查”只覆盖表中列出的官方入口、事件窗口和停止点，不扩张为机构全部内部研究。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方 RSS](https://openai.com/news/rss.xml)、[Images 2.5 发布页](https://openai.com/index/introducing-chatgpt-images-2-5/)与[System Card](https://deploymentsafety.openai.com/chatgpt-images-2-5/safety-evaluations)；量子实验与 Navier–Stokes 属暂缓的 AI for Science，其他合作/社会项目按范围关闭 | 已检查 | 无；限公开 RSS、发布页与 system card |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)最新公开研究仍为 Sep04，越过窗口起点 | 已检查 | 无；限公开目录 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/)与[Google Research Publications](https://research.google/pubs/)；未确认本窗大模型或大模型 Infra 新事件，月份级科学条目不强行归日 | 已检查 | 部分卡片只有月份，不能据此作日级无遗漏断言 |
| SRC-META-AI | [Meta AI Research](https://ai.meta.com/research/)仍返回不可提取空壳；同域定点检索未确认窗内 publication | 受阻 | 公开列表不可稳定提取，不能证明本窗为零 |
| SRC-QWEN | 官方中英研究/文章入口按公开日期检查，最新可验证条目仍为 Sep03 | 已检查 | 无；限公开入口 |
| SRC-DEEPSEEK | [官方更新日志](https://api-docs.deepseek.com/zh-cn/updates/)最新记录仍为 Aug21，随后 Aug13、Jul31 | 已检查 | 无；限公开日志 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog)与 [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) 窗内 merged commits；逐项读取相关 PR，20 个窗内 commits 中 4 项达到长期贡献门槛 | 已检查 | 无；普通 commit 不等于候选 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)的官方 `publicList` 最新为 Aug28；[UniRL](https://github.com/Tencent-Hunyuan/UniRL) 窗内 merged PR 逐项检查，保留 #258、#377 | 已检查 | 无；以公开列表与仓库 artifact 为边界 |
| SRC-ZAI | [官方 Research](https://www.zhipuai.cn/zh/research)最新日期仍为 Aug26，随后 Aug14、Jun16 | 已检查 | 无；限公开目录 |
| SRC-BYTEDANCE-SEED | [Seed Research](https://seed.bytedance.com/en/research)与 [VeOmni](https://github.com/ByteDance-Seed/VeOmni) 窗内 merged PR；三项 correctness fix 保留，scorer/recipe/optional-extra 等局部变更关闭 | 已检查 | 无；限公开页面与仓库 artifact |
| SRC-BAIDU-ERNIE | [ERNIE Blog](https://ernie.baidu.com/blog/zh/)最新公开记录仍为 May09 | 已检查 | 无；限公开目录 |
| SRC-XIAOMI-MIMO | [Paper / Blog](https://mimo.xiaomi.com/)与 MiMo-Code 窗内 commits；desktop 公告与 provider-loader 局部修复未改变长期系统合同 | 受阻 | Blog 卡片缺日级时间，不能证明页面本窗为零 |
| SRC-MINIMAX | [官方 Blog](https://www.minimax.io/blog)最新研究为 Aug13；[Provider Verifier #60](https://github.com/MiniMax-AI/MiniMax-Provider-Verifier/pull/60) 在窗内合入并改变图像输入边界验收 | 已检查 | 无；M3 行为只按披露 endpoint/config 采用 |
| SRC-ARXIV | cs.AI/cs.CL/cs.LG/cs.DC 官方 new-list 及具体主题回查；最新仍是 09-07 08:00+08 已由 09-07 日报拥有的 Monday batch，本窗 0 个新 owner identity | 已检查 | 不把重列、cross-list 或 revision 变成新事件 |

## 3. 候选与判断

三项评分依次为 Design Delta、System Reach、Durability。correctness 修复、协议完整性与实际写入 Books 的机制按深入范围审阅，不以总分替代 Evidence Gate。GitHub 项的“公开时间”取本窗内 merge/commit 成为默认分支公共 artifact 的时刻，不是 PR 首次创建时间。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [ChatGPT Images 2.5 与 System Card](https://deploymentsafety.openai.com/chatgpt-images-2-5/safety-evaluations) | 2026-09-08T19:30:00+08:00 | 多模态生成发布把输入/输出 guard、结果指标与 provenance 绑定到同一 release；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)、`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [UniRL #377：EP expert-layout policy 离开 generic transport](https://github.com/Tencent-Hunyuan/UniRL/pull/377) | 2026-09-08T11:04:32+08:00 | model/backend layout policy 与通用权重传输分责；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)、`TRAIN-TENSOR-PARALLEL` [Ch37](../../../../books/part-04-training-system/37-tensor-parallel.md) |
| [UniRL #258：rank error fail-fast](https://github.com/Tencent-Hunyuan/UniRL/pull/258) | 2026-09-09T00:21:33+08:00 | completion-order error exposure 与 poisoned pool 阻断二次 RPC；3 + 3 + 2 = 8 | 深入完成 | 整合 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [VeOmni #1159：preserve shared gather gradients](https://github.com/ByteDance-Seed/VeOmni/pull/1159) | 2026-09-08T20:39:37+08:00 | distributed autograd borrowed/owned gradient buffer correctness；3 + 2 + 2 = 7 | 深入完成 | 整合 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [VeOmni #1158：Wan Ulysses SP attention correctness](https://github.com/ByteDance-Seed/VeOmni/pull/1158) | 2026-09-08T18:26:39+08:00 | sequence/head ownership 与 padding semantics 共同决定 SP 等价性；3 + 2 + 2 = 7 | 深入完成 | 整合 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [VeOmni #1162：await pending async save at train end](https://github.com/ByteDance-Seed/VeOmni/pull/1162) | 2026-09-08T10:50:15+08:00 | job terminal status 必须消费 checkpoint future 与异常；3 + 2 + 2 = 7 | 深入完成 | 整合 — `TRAIN-CHECKPOINT` [Ch35](../../../../books/part-04-training-system/35-checkpoint.md) |
| [Kimi Code #3626：停止 child teardown 误取消 sibling tools](https://github.com/MoonshotAI/kimi-code/pull/3626) | 2026-09-08T10:26:13+08:00 | cancellation ownership 从 actor teardown 回到 spawn scope；3 + 2 + 2 = 7 | 深入完成 | 整合 — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Kimi Code #3645：large file read 可恢复分页](https://github.com/MoonshotAI/kimi-code/pull/3645) | 2026-09-08T19:47:28+08:00 | observation cursor、Unicode 边界与 source-drift 检查；2 + 2 + 2 = 6 | 深入完成 | 整合 — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Kimi Code #3492：reasoning_details round trip](https://github.com/MoonshotAI/kimi-code/pull/3492) | 2026-09-08T19:54:02+08:00 | summary 与 opaque continuation state 的身份、顺序和中断提交边界；2 + 2 + 2 = 6 | 深入完成 | 整合 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Kimi Code #3654：保留 structured tool results](https://github.com/MoonshotAI/kimi-code/pull/3654) | 2026-09-08T21:40:30+08:00 | human-readable 与 typed payload 的非等价性和 spill 完整性；3 + 2 + 2 = 7 | 深入完成 | 整合 — `AGENT-MCP` [Ch83](../../../../books/part-07-agent/83-mcp.md) |
| [MiniMax Provider Verifier #60：M3 image scaling contract](https://github.com/MiniMax-AI/MiniMax-Provider-Verifier/pull/60) | 2026-09-08T22:32:25+08:00 | provider 输入边界需要缩小、放大、像素上限与 orientation 的可执行矩阵；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [ChatGPT Images 2.5 与 System Card](https://deploymentsafety.openai.com/chatgpt-images-2-5/safety-evaluations)

官方发布区分 Flare 与 Sunburst：前者是默认 API 分支，后者用更长生成时间换更精细控制。发布页声称 Flare 相对 GPT-Image-2 有更高质量及 50% 更低 latency，但没有披露硬件、分辨率、并发、batch、端到端 SLO 或完整 evaluator，因此不把数字外推成通用性能结论。System Card 披露上游 LLM policy checks、覆盖文本/图像输入和生成输出的下游 multimodal monitor、线上/离线监控，以及 C2PA 与 SynthID provenance。安全表中的 `unsafe shown` 为 outcome 指标；作者使用未做多重比较校正的双侧 exact McNemar，且该项差异没有达到其阈值。Ch24 已区分生成分支与多轮编辑 state，Ch66 已要求输入/trace/输出和评价条件分层，Ch72 已包含生成内容双层 provenance 与 pre/post guard，故本次只更新 release evidence，不重复正文。

### [UniRL #377：EP expert-layout policy 离开 generic transport](https://github.com/Tencent-Hunyuan/UniRL/pull/377)

旧 `FullWeightSync` 让通用 transport 直接理解 VeOmni、Qwen3-MoE layout 与 parallel state，新接口由 backend 提供 ready stream transform，并按 `config.model_type` 而非参数名后缀解析 expert layout；未知 model type fail closed。两 rank CPU/Gloo equivalence 覆盖 gather 顺序与 bit-identical tensor stream，dependency guard 也证明 `distributed → train` 反向依赖会失败；但真实 8-GPU 30B/35B EP weight sync 未运行，out-of-tree backend 还需实现新方法。Ch36 的 typed state transition 与 Ch37 的 model/layout ownership 已给出同一设计边界，因此为已有覆盖。

### [UniRL #258：rank error fail-fast](https://github.com/Tencent-Hunyuan/UniRL/pull/258)

`ray.get(refs)` 等待全部 ranks，可能把 rank 0 在 collective 前的 OOM 隐藏到 peer watchdog 超时。新路径按完成顺序取得结果、立即传播首个 rank error，并 poison DevicePool，阻止 teardown/checkpoint 再发阻塞 RPC；成功结果仍按 rank 重排。六 GPU BAGEL OOM 复现支持“没有再等 NCCL watchdog”与二次 RPC 被拒绝，但总 20 分钟仍含启动/生成/backward，且复现 checkout 带有正交的 #252，不能据此声称统一故障恢复完成。已将 fail-fast、terminal execution domain 与重建 process group 的边界写入 Ch36。

### [VeOmni #1159：preserve shared gather gradients](https://github.com/ByteDance-Seed/VeOmni/pull/1159)

问题不在 gather forward，而在 `_Gather.backward` 修改了被另一 autograd branch 共享的 gradient。修复为 NCCL 正 shard 优先 reduce-scatter、borrowed input 生成独立 output，只有证明 owned packing 时才复用 local slice；其他 backend/complex/empty case 保留 owned contiguous all-reduce buffer。两 L4 结果覆盖数值、ownership 与内存矩阵，CPU/Gloo 测试覆盖更多布局；HCCL/NPU、四 rank、完整训练、FSDP parity 与端到端吞吐仍未验证。Ch36 新增 borrowed/owned buffer 与 sibling branch correctness，不采用测试 harness 加速数字作为训练性能证据。

### [VeOmni #1158：Wan Ulysses SP attention correctness](https://github.com/ByteDance-Seed/VeOmni/pull/1158)

Wan 的 sync self-attention path 原先没有执行 Ulysses Q/K/V All-to-All，优化 kernel 又忽略 padding mask，使每 rank 只在 local sequence shard 上 attention。修复在 attention 两侧执行 sequence/head view 交换，并在不接受 mask 的 kernel 前裁剪 padded K/V、之后 re-pad output。4×A10G 的 reference comparison 支持所测三种 backend 的等价修复，但不证明其他 shape、硬件、异步 SP 路径或端到端训练性能。该证据与 #1159 一起写入 Ch36，强调 collective invocation 之外还必须验证 view、mask 与 storage semantics。

### [VeOmni #1162：await pending async save at train end](https://github.com/ByteDance-Seed/VeOmni/pull/1162)

`dcp.async_save` 的 future 过去只在 load、下一次 save 或特定 HF save 路径中被等待；单次最终异步保存可能依赖 interpreter shutdown 偶然完成，后台异常则不进入 job status。新增 `on_train_end` 无条件调用 `wait_for_pending_save()`，无 pending 时为空操作，并保持所有 ranks 的 barrier 对称。PR 给出 16×H100 周任务的触发背景，但没有把完整训练测试结果作为该修复的独立证明。Ch35 已补“exit 是最后一个 commit step”，并保留尾部延迟、deadline 和失败终态的 trade-off。

### [Kimi Code #3626：停止 child teardown 误取消 sibling tools](https://github.com/MoonshotAI/kimi-code/pull/3626)

并行 tools 曾把每个 actor teardown 的 abort 汇合到 batch signal，最快 child 正常结束就会取消 siblings。新设计在 spawn site 为每个 tool call/LLM attempt 持有 controller，actor 只执行与回报；父 scope 决策时同步 abort，tool execution 提供默认 2.5 秒 grace 并为缺失 outcome 合成 aborted。150 个 focused tests 支持所述回归，但不证明所有外部 MCP server 都能在 grace 内响应或取消。Ch81 已形成 scope owner、child completion 与 parent cancellation 的清晰分责。

### [Kimi Code #3645：large file read 可恢复分页](https://github.com/MoonshotAI/kimi-code/pull/3645)

旧 Read 同时受 100 KiB、通用 50,000 字符 spill、行数与单行限制影响，超长单行还没有 continuation。新路径统一字符预算，使用 `column_offset` 和精确 Next Read 参数，维护 Unicode boundary，并以 inode/size/mtime 识别部分文件变化；targeted 133 tests 与 tracked full suite 6,424 tests 支持披露实现。它没有提供 snapshot consistency，append 可能在 EOF 前被读入。Ch81 因此只吸收“可恢复 observation cursor + source revision validation”，不把分页称为文件冻结或 exactly-once。

### [Kimi Code #3492：reasoning_details round trip](https://github.com/MoonshotAI/kimi-code/pull/3492)

OpenGW 的 `reasoning_details` 同时包含可读 summary segments 与尾部 encrypted state，后者需要跨轮原样回放。新路径按 index 保持 streaming segment boundary，只有拿到 ciphertext 的 thinking 才在中断后进入 history，并在 outbound message 重建原数组。公开 PR 支持 client contract 与 focused tests，full suite 仍有环境相关旧失败；它不说明 ciphertext 内容、推理正确性或跨 provider 可移植性。Ch84 将其归入 provider-coupled conversation runtime state，不把 opaque state 当可解释性证据或 action authority。

### [Kimi Code #3654：保留 structured tool results](https://github.com/MoonshotAI/kimi-code/pull/3654)

MCP adapter 过去只要 `content` 有可用文本/媒体就丢弃 `structuredContent`，导致“找到一行”留下而实际 record 消失。修复默认并存两种表示，仅当完整文本解析为规范等价 JSON 时去重；非规范数字写法保守保留，额外结构化数据进入 executor/spill/Read 路径。419 个聚焦测试及 1,200 records 无重复调用回归支持该路径；全局 spill retention 与 persistence failure 明确在范围外。Ch83 已补双表示非等价与 exact canonicalization 边界。

### [MiniMax Provider Verifier #60：M3 image scaling contract](https://github.com/MiniMax-AI/MiniMax-Provider-Verifier/pull/60)

测试矩阵补齐长边缩小、短边低于 112 的放大、横/竖方向和总像素边界，并把超限 case 从允许任意 200 的软断言改为：200 必须真正识别内容，或明确 4xx 拒绝。官方 endpoint 上 10 个用例通过，但响应不披露实际缩放尺寸，因此 `min_short_side` 目前只是 acceptance smoke；视频上限也没有真实长 fixture。Ch66 已要求输入处理、boundary、postcondition 与 false-pass 分开，故为已有覆盖，不把 provider 当前响应固定成所有部署的永恒合同。

## 5. 缺口与下一步

两个外部限制作为本窗**终态保留项**隔离：Meta Research 公开列表不可稳定提取；MiMo Blog 卡片缺少日级发布时间。它们不支持正面证据、Books 写回或本窗无遗漏断言，也不影响其余来源与 11 项候选到达安全终态。**定点重开条件：** 任一来源恢复带日级时间的完整官方列表时，只核对 2026-09-08 09:00～09-09 09:00 的事件身份，不重扫其他日期或已完成家族。

OpenAI Images 2.5 的 50% latency 声明只保留为缺少 workload/hardware/SLO 的 vendor claim；MiniMax M3 无缩放后尺寸回执；UniRL #377 未完成真实 8-GPU EP sync；VeOmni #1159 未完成 HCCL/NPU 与端到端训练。这些均是已明确 non-proof 的证据边界，不是普通待办，也不阻止本日报闭环。下一日报从 09-09 09:00 之后的新事件继续，不重开本日旧 PR。本次不生成 Weekly，不启动暂停中的历史任务。

## 6. 复核

复核者：`/root/sep09_review`（非作者 fresh-context reviewer）  
结论：通过

独立复核核对固定窗口、十四个 Daily 来源、11 个候选计数、GitHub 合入时刻、OpenAI/arXiv 跨日去重、primary/non-proof 边界、评分和五个 Books owner 的实际写入。复核要求把 GitHub 时间明确为 merge/commit 公开时刻，并指出局部 correctness PR 的 System Reach 不应因重要性自动评为 3；作者据此将 UniRL #377、三项 VeOmni、Kimi #3626/#3492/#3654 校准为 2，深入审阅和 Books 结论不变。格式校验和 `git diff --check` 通过；Meta 与 MiMo 的外部限制仍被隔离，不支持正面证据、Books 或无遗漏断言。Cross-model skipped: 本轮为父任务分派的非交互独立复核。
