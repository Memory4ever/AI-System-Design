# 2026-10-13 每日来源：中国机构六源

窗口：北京时间 **2026-10-12 ～ 2026-10-12**。检查者：`live1013_china`；实际检查时间：2026-10-13 11:00～11:09（UTC+8）。本记录只收集与初筛，**不代表候选证据、Books 或日级验收已完成**。

启动时重读当前 `AGENTS.md`、`CODEX_RESEARCH_PROMPT.md`、研究合同、Report 合同、来源使用说明/每日分组、ROADMAP 与最新暂停 checkpoint。历史补查暂停；本日不是 Sunday，不建立 Weekly。仅写本文件，不改变 Books、Learning State、Report、索引或 Git index。运行前已有 `books/part-06-ai-infrastructure/69-trace.md` 与 `docs/LEARNING_STATE.md` staged 修改保留。

## 1. 实际目录、日期字段和停止

| 来源 | 本次真实入口和检查范围 | 停止依据与结果 | 缺口/限制 |
| --- | --- | --- | --- |
| SRC-TENCENT-HUNYUAN | 首查 [Research 全部](https://hunyuan.tencent.com/research)。网页提取超时；误以页面域名请求 `/api/blog/publicList` 返回 HTTP404，随后仅复用旧日 raw 的 API URL 形状，真实重发到 [官方 API](https://api.hunyuan.tencent.com/api/blog/publicList)：POST `{"renderType":0,"pageNum":1,"pageSize":20}`，Content-Type JSON、Origin `https://hunyuan.tencent.com`、Referer Research、Accept-Language 分别 zh/en。两次 `code=0`；中文 `data.totalNum=11`、实际11，英文9/9。只投影 id/title/publicAt/publishedAt/displayPublishTime，未把目录夹带全文当审阅。另查 [Tencent-Hunyuan 官方组织](https://github.com/Tencent-Hunyuan)、[T1 releases](https://github.com/Tencent/llm.hunyuan.T1/releases) 与当前 push 触发的 UniRL。 | zh最前100119三字段北京时间分别09-22/09-21/09-22；100116为09-22/09-19/09-22；en100116为09-23/09-18/09-22。余下条目三字段均窗前；列表到total终点，不再保留动态目录故障。T1 releases API空；UniRL release v0.2.0为10-08，v0.1.0为10-07；本窗窄commit查询5条见§3。 | 三日期字段不同语义，不互当首次公开证明。本次检查当前可见全部列表，不证明被删除条目或整个组织历史保留完整。组织仅首10发现入口，不授全组织覆盖。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 时间排序“全部”可见首段；[New Released](https://docs.z.ai/release-notes/new-released)；[zai-org](https://github.com/zai-org) 首10与实际push触发的 [zcode-plugins](https://github.com/zai-org/zcode-plugins)。 | Research最新08-26/08-14/06-16，已早于10-12，不按“查看更多”扩旧年度池。release08-26/08-18/06-16前缀均窗前；ZCode registered release v3.14.3为09-24；zcode-plugins无registered release，本窗2条commit见§4。 | 没有从Research/模型release发现本窗新研究；组织首10只发现，不保证首10之外无事件。 |
| SRC-BYTEDANCE-SEED | [Research/Blog](https://seed.bytedance.com/en/research) 和 [Public Papers](https://seed.bytedance.com/en/public_papers)，后者 `Newest → oldest`、Page1/13、1–20 of242。Research featured无目录日，实际进入 [SeedRealtime原文](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction?view_from=content_recommend)；官方组织首10，VeOmni push触发窄commit/release。 | 论文前缀08-18/08-12/08-06/07-23，页1已早于窗，不扫13页。Blog dated前缀07-31/07-20/07-08；featured原文 `Date=2026-08-05`，排窗停止，不读旧机制作为新候选。VeOmni release首5最新09-30，均窗前；本窗5commit见§3。 | Page1足以夹住当前倒序目录窗口，不声明242条全量审阅；AI for Science条目不引入本轮队列。 |
| SRC-BAIDU-ERNIE | [中文技术Blog](https://ernie.baidu.com/blog/zh/) 页1/2（10条）、[Publication](https://ernie.baidu.com/blog/zh/publication/) 4项、[ERNIE releases](https://github.com/PaddlePaddle/ERNIE/releases)。 | Blog日期前缀05-09/04-30/04-15/02-06/01-29，页尾至2025-11-21；最新即窗前，停止不进入旧第2页。Publication仅2025/2026年份，不当10-12证明，也不为4个旧题名建新版本队列。release API唯一 `ernie-4.5` 为2025-06-30。 | 年份目录不能提供独立日级首次公开保证；本轮未发现指向10-12的新材料，不称全文或全版本审阅。 |
| SRC-XIAOMI-MIMO | [Paper/Blog首页](https://mimo.xiaomi.com/) Paper8/Blog15；无日期Blog第一项进入 [Tool-Call Repetition原文](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)；[XiaomiMiMo](https://github.com/XiaomiMiMo)首10，MiMo-Code push触发窄commit/release。 | Paper最新06-29/03-13/02-03/01-08；Blog第一项原文09-27，API updated checkpoints明确09-25，不移入10-12。其余14项无目录日期，未逐篇追旧材料。MiMo-Code releases实回2条（v0.1.15发布09-22，v0.1.14发布09-23；不是可靠倒序，两条全部检查），本窗commit页1=10、页2=1，到短页停止。 | **Blog无日期剩余项为本窗隔离覆盖缺口**，不支持零命中/全覆盖；恢复须官方带日的10-12目录片段或明确本窗单篇原始发布，仅重开对应项。 |
| SRC-MINIMAX | [英文Research](https://www.minimax.io/blog)12条；[原中文入口](https://www.minimaxi.com/blog)实际redirect [minimax.cn/blog](https://www.minimax.cn/blog)，web提取仅壳，直取官方HTML恢复 dated cards；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)3条。官方组织首10触发cli与OpenAgentCore当前事件。 | EN/CN dated前缀08-13/07-31/06-09/06-01均窗前，不把HTML `dateModified`执行时刻当论文日。Agent Tech Blog 10-08/09-22/09-19，停止窗前。cli v1.0.28及OpenAgentCore v0.0.10/v0.0.11均10-12；minimax-code最新release10-09，本窗无该repo push，停止。 | 组织首10只是有限发现入口，不授整个org全部事件；registered release与本窗实际commit分开计事件，家族不重复计数。 |

所有机构页面只检查本次主线：模型、训练、推理、多模态、平台、Agent。不搜索全组织全历史，不扫描每日清单之外的每周组。当前官方页未见针对本窗候选的撤回标记；只处理实际出现的纠错/安全/正确性信号，未遍历全版本证明“没有标记”。

## 2. GitHub 有界查询与实际停止

发现入口：`https://api.github.com/orgs/<org>/repos?sort=updated&direction=desc&per_page=10`，org为 Tencent-Hunyuan、zai-org、ByteDance-Seed、XiaomiMiMo、MiniMax-AI。每个实际首10；`updated_at`可能仅活动/收藏变化，**不作论文、commit、release公开日**。仅 `pushed_at`在本窗或更晚的相关repo定点查。

本窗commit API：`https://api.github.com/repos/<repo>/commits?since=2026-10-11T16:00:00Z&until=2026-10-12T15:59:59Z&per_page=10`。这些端点范围是北京时间10-12自然日的UTC映射，不按材料时分秒决定归属。实际返回：UniRL5、zcode-plugins2、VeOmni5、MiMo-Code10+第二页1、MiniMax cli1、OpenAgentCore10+第二页0；最后页均短页/空尾。commit committer时间只作事件线索，带PR项再真实请求 `https://api.github.com/repos/<repo>/pulls/<number>` 核 `merged_at`。

本次release API全为 `https://api.github.com/repos/<repo>/releases?per_page=5`，实查Repo：Tencent-Hunyuan/UniRL、Tencent/llm.hunyuan.T1、zai-org/ZCode、zai-org/zcode-plugins、ByteDance-Seed/VeOmni、PaddlePaddle/ERNIE、XiaomiMiMo/MiMo-Code、MiniMax-AI/cli、MiniMax-AI/OpenAgentCore、MiniMax-AI/minimax-code。只取tag、published_at、html_url；窗内release另取完整body/core；不把窗前大release全文展开为本窗待办。

旧日 `_sources`只帮助恢复 API主机/字段名和MiMo实际URL形状；本日所有覆盖、日期和事件来自以上重发，不继承旧日Coverage。

## 3. 局部准入校准后：真正拟采用命题与相关原始核心

这里没有本窗新论文题摘；以下都是官方commit/PR/release核心说明。核心说明用中文完整转述问题、变更理由和关键边界，原件/精确版本链接可直接回读。root已局部校准：**同repo本日fix不能整体捆成候选；correctness标签不自动触发Deep；既有实现不变量修复通常具体EX。** 校准后仅三个拟候选命题，其余明确标EX/必要纠错信号。评分尚须独核，不借成熟原则、机构声望或访问状态评分，不宣称实验复现。

### C1 — UniRL：只保留allocator病理的受限实验命题

家族：`Tencent-Hunyuan/UniRL`。**只有#583拟入选**，暂拟 **2 + 1 + 2 = 5**，标准审阅；其余#582/#586普通实现不变量修复具体EX，不按correctness标签自动深入。#554仅保留真实测量纠错，只有实际旧采用链依赖该timing时才深入受影响判断。

拟采用命题：同样的fp32 LoRA/FSDP通信量不应直接解释H3 recipe近显存上限的train slowdown → 原文以phase/allocator retry观测和相同字节microbenchmark区分缓存segment失败与通信量，并报告保留launch key后的expandable_segments正面结果及max_split_size_mb512负面交互 → 在此recipe做性能归因与launch配置选择时，需要加入allocator状态，而不是只比较dtype、网络带宽或预留显存数字。仅新增knob不是贡献；**采用范围仅作者的H20/H3 recipe与所报告实验，不做普遍训练定律**。

| 官方完整题名/原件 | 精确事件 | 实际已读核心与限制 |
| --- | --- | --- |
| [fix(tensor): fail closed when batch concat or DP dispatch sees inconsistent shards](https://github.com/Tencent-Hunyuan/UniRL/pull/582) | merged_at `2026-10-12T14:57:13Z`；merge `790b5ec5d19107e12c47a0d92fab50f8b6cfc7db` | `Batch.concat`以前留第一个SHARED值、局部缺字段可导致列表短于batch，2B CFG fused行未经按样本拆分可把一项cond配另一项uncond。新增共享结构比较/路径错误、非空分片每样本字段完整性、TensorRef CONCAT行数检查、Sample ID唯一性；Qwen3-Omni/Qwen3.5固定media key并用None占位，HunyuanImage3按B行split_cfg_fused后forward重拼。不是全面张量相等证明：SHARED TensorRef只比shape/dtype，non-batched CONCAT tensor最终仍保item0；`pytree_chunk`保持旧行为，不能抄PR早期撤回的guard。原件test声明含CPU与部分GPU smoke，但最终rebased精确merge未重新跑全部GPU；未作为本轮实际运行。 |
| [docs(reward): note the BAGEL it2i timings predate the #547 fix](https://github.com/Tencent-Hunyuan/UniRL/pull/554) | merged_at `2026-10-12T11:06:22Z`；merge `89ac5b03f57bb51fc378c7a881a0549b14a82f98` | reward README原overlap数字使用旧vLLM-Omni img2img prefill：512×512有4902 ViT token，而实际trainside contexts是1227；#547修后generation变短，旧overlap收益不能推算新端到端收益。新增近数字说明其未重新测，旧数保留而不认作当前；**docs only、无新run**。只采用measurement qualification，不用此纠错构造新加速benchmark。 |
| [perf(minimax-h3): enable expandable allocator segments for trainside training](https://github.com/Tencent-Hunyuan/UniRL/pull/583) | merged_at `2026-10-12T06:03:31Z`；merge `279298dc8aa9d3a727c015fcf10fc0da90613871` | 作者将H3 trainside近96GB H20显存上限的1.30GB FSDP all-gather allocation retry定位为CUDA caching allocator segment问题而非fp32 LoRA通信字节变化。新增default-false的FSDPConfig.expandable_segments，开启时拼接已有allocator环境key；VeOmniBackend拒绝此knob，只有H3 trainside recipe启用，2×8 HSDP验证recipe保false。作者测试为1×8H20、torch2.13+cu130、128samples/step、256×384×124；报告retry降0与局部step变化。不能外推：`max_split_size_mb:512`组合约2×变慢；进程级设置、SGLang可reset、CUDA IPC兼容未验证；相同代码另一报告缺allocator状态，病理可能依赖launch环境。 |
| [perf(trainer): stop driver-hydrating anchored rollout outputs before DP scatter](https://github.com/Tencent-Hunyuan/UniRL/pull/586) | merged_at `2026-10-12T05:52:33Z`；merge `a1ef2a83974f27098c055eed468e99006f34d0dc` | anchored AR与HI3 two-engine旧路径把整trajectory GPU→driver CPU/object store→GPU；旧single-handle slicing约束已被span-view TensorRef和localize移除，删除三处deep_hydrate以保持worker-resident，driver仍取rewards。move key含span与目标device使同handle不同DP subwindow可移动。作者CPU local Ray equivalence与emulated-NCCL覆盖不能证明实际NCCL性能；**无GPU端到端/driver-memory benchmark**。HI3跨replica ragged fused-condition padding仍局部driver hydration，不能写完全零driver物化。 |

拟owner为训练runtime的`TRAIN-DISTRIBUTED-TRAINING`，allocator背景归`INFER-GPU-MEMORY`；最终只定位实际差额，不重复owner。本轮未读Books差额/未写入。#582修复SHARED/row/CFG既有数据容器契约，#586移除#59已实现span-view slicing之后遗留workaround且无真实GPU性能结果，均具体EX，不把修复借成熟机制升分。#554原timing未在本分支证明曾进入Books，不能据此开启整本measurement重审。

同窗 [chore: drop runtime guards that can no longer fire](https://github.com/Tencent-Hunyuan/UniRL/commit/6624b28aab3299d116ae1e3d90aaa14926676911)（06:10:58Z）具体EX：同checkout硬编码protocol版本guard、transformers固定版本已覆盖的shim/check删除；request_id/command验证仍保留。没有新正确性成立条件或安全修正，不单独候选，不评分。

### EX-SEED — VeOmni：保留真实修复核心，不构造候选

家族身份：`ByteDance-Seed/VeOmni`，**不列候选、不评分**。以下本窗事实用于具体EX复核，不把多个修复捆成一项6分贡献。

具体EX：#1274扩展已有#1273 local-expert loader并拒绝未正确scale的格式、#1248恢复每stream shard原顺序、#1261避免HF已有worker sharding再过滤并隔离共享epoch、#1282用既有checkpoint index恢复非可逆rename。它们是实际工程错误/成立边界，但此分支尚未找到被这些证据改变的具体既有知识命题；不能借“ownership重要”这样的成熟原则反向升分。保留可复查的CPU/GPU作者证据与未测试边界，不因fix标签全量深入。

| 官方完整题名/原件 | 精确事件 | 完整核心变化与边界 |
| --- | --- | --- |
| [[model] feat: stream per-expert Qwen3-Omni-MoE and DeepSeek-V3 checkpoints under EP](https://github.com/ByteDance-Seed/VeOmni/pull/1274) | merged_at `2026-10-12T11:45:52Z`；`57e5f6d392a230c31488f57542cd534e1c73ed33` | 前版stream loader需converter显式提供fused_expert_target/for_expert_range；共享PerExpertFusedCheckpointTensorConverter把此能力扩到Omni/DeepSeekV3，每EP rank只读本地expert并stack local fused slice，未build的talker/MTP模块跳过不读。新增三converter拒绝FP8 per-expert：以前未经weight_scale_inv就cast BF16会静默错；DeepSeekV3这里**只支持BF16**，V4 FP4+scales仍拒绝，不能说全MoE低比特加载已支持。作者210CPU tests与stub EP精确tensor比对，不是多GPU生产训练/IO加速结果。 |
| [[model, ci] fix: scatter Flux joint attention output per stream under Ulysses SP](https://github.com/ByteDance-Seed/VeOmni/pull/1248) | merged_at `2026-10-12T04:50:10Z`；`62beaef91723f9b76615a4280c44673569881fe9` | `[text_full,image_full]`拼后一次reverse all-to-all让rank切片跨模态边界；分别scatter text/image使rank拿各自stream shard。与#1246 non-divisible padding独立，不合并为同修复。作者新2GPU module regression、2×L4 fp32全模型SP2-vs-off的output/grad误差比较，覆盖mask与odd长度；不表示本轮复現，不外推其他joint-attention实现。 |
| [[data] fix: don't split HF iterable streams by worker again](https://github.com/ByteDance-Seed/VeOmni/pull/1261) | merged_at `2026-10-12T04:19:34Z`；`ccb6ba02494161fa26821b33388f39b62b218c26` | HF IterableDataset已按DataLoader worker分source shard，wrapper再worker filter使默认num_workers2约半数据消失；检测_data/_dataset wrapper链，HF流只保row-level DP过滤，plain iterable不变。HF共享_epoch在各worker每pass set_epoch有race，给HF流worker-private deepcopy再设置。作者torch2.8cpu/datasets2.21、48行、workers0/2/4、DP1/2/4以及真实streaming parquet repeat tests；**没有端到端training或真实多进程distributed launch**。 |
| [[model] fix: deepseek v4 reverse mapping](https://github.com/ByteDance-Seed/VeOmni/pull/1282) | merged_at `2026-10-12T03:42:31Z`；`6712d3757e7626283647fa487df3f3d5738b31fe` | HF rename并非可逆字符串替换（反转.norm.会再重写原生attn.kv_norm）；从checkpoint index的load-time rename映射构造逆映射。仅该export naming错误，不等于V4 FP4 EP stream loader支持；不能和#1274未支持边界拼成全格式转换保证。 |

相关主线只用于检查范围：`TRAIN-CHECKPOINT`、`TRAIN-DISTRIBUTED-TRAINING`、`TRAIN-DATA`。能映射章节不是准入依据；本轮不展开这些普通修复的代码/Books队列。独核如有新证据发现具体设计反例，仅重开对应项。

同窗 [[data] fix: make the hdfs fallback isdir and listdir return real results](https://github.com/ByteDance-Seed/VeOmni/pull/1278)（merged03:04:51Z、`25c50a53097e174c80616a77158f722c6b0bd067`）具体EX：fallback原isdir忽略command exit code、listdir丢output返回True而使sorted(bool)报错；改为exit0判断、entry names、失败FileNotFoundError。已读完整变更原因和stub测试核心；修复传统filesystem API返回值，不新增主线机制/设计边界，不评分，不作整个HDFS安全保证。

### C2 — MiMo-Code：实际跨drive/UNC containment fail-open

家族：`XiaomiMiMo/MiMo-Code`，本窗commit11条。**只有#2650实际containment authority变更拟候选**，暂拟 **1 + 2 + 2 = 5**，安全信号仅受影响实现深入。其余MCP discovery、cron session owner、host-SDK是具体原始机制线索/EX，不与#2650合并升分，不默认它们各有长期新增贡献。

| 官方完整题名/原件 | 本窗精确事件 | 已读核心与限制 |
| --- | --- | --- |
| [feat(mcp): defer MCP tools with conversation-scoped lazy loading](https://github.com/XiaomiMiMo/MiMo-Code/commit/463cbb28729b9037bdf7fa74b73c37eb2aaca01f) | committer `2026-10-12T15:32:09Z`；精确commit及其中docs spec updated10-12；没有PR merge字段，不能推为新论文首次公开 | 原先catalog放tool description影响provider prefix cache、加载限当前user request；新spec采用静态search描述、最后user message synthetic reminder首全量后delta、compaction后重新announce；search返回完整schema，tool-result metadata作为activation事实，conversation内newest-first最多32加载项跨turn持续，但每step再按request权限过滤。`true/auto/auto:N/false`，auto取定义估算占context10%，无window假设200k；catalog预算10%/20k cap降names/truncate，search仍全catalog。外部MCP tags escape避免伪造harness；普通deferred调用必须下个outer-loop才激活。**Codex-mode例外**：exec经ALL_TOOLS可直接用全部request-authorized MCP，无search roundtrip；不能把普通direct-tools guard写成exec也强制search。尚未实际核全实现/运行。 |
| [fix(fs): treat absolute path.relative results as outside in contains](https://github.com/XiaomiMiMo/MiMo-Code/pull/2650) | merged_at `2026-10-12T13:52:22Z`；`8e1df4abee56da60c11db14606dd855823b1a29f` | Windows跨drive/UNC的relative()可返回absolute to-path而非..；原startsWith(..)否定误判inside影响workspace、tool-script、server cwd、plugin jail。新条件同时拒绝host/Windows absolute，overlaps复用contains，两实现同改。**POSIX tests在旧实现也过**，仅真实Windows可red-before；作者win32-relative本地实验不能替代真实Windows acceptance或防所有symlink攻击。 |
| [fix(cron): fire scheduled prompts into the creating session](https://github.com/XiaomiMiMo/MiMo-Code/pull/2648) | merged_at `2026-10-12T13:23:46Z`；`e0c9bb3a543f2ce87e42756c26dbc2576e1d06c6` | process-wide CronBridge总投首session造成多session任务错投。按task.createdBySessionId路由，legacy无stamp回bridge；armLoop/keepalive保持owner，LoopState在one-shot删除后继续持owner，get/delete/rename/list一致过滤，empty stamp视未标。问题是engine端路由而非Desktop不接受非active session；作者78tests，不是本轮实际跨session验收。 |
| [feat(plugin): serve the plugin SDK from the host instead of installing it](https://github.com/XiaomiMiMo/MiMo-Code/pull/2645) | merged_at `2026-10-12T09:16:11Z`；`4fcfe1b7283efe490ac02b71eebf77858458af34` | startup每config目录npm-install SDK会联网写用户目录、依赖不可见版本/多SDK-zod实例；Bun host通过virtual module统一SDK，bundle外置引用host副本；无法提供SDK的Node/Desktop或显式only-config-dir策略仅装载config目录内source，并resolve symlink与跨drive containment。显式npm插件/provider/LSP仍可原install，**不删除旧node_modules**。follow-up [fix(plugin): detect the plugin SDK host by Bun.plugin, not the Bun global](https://github.com/XiaomiMiMo/MiMo-Code/commit/4fb57c5648d2ca4f5a0599f3492368537460cd13)（11:52:38Z）核partial Bun global在Node缺Bun.plugin会startup失败且漏策略；必须以真实capability而非global名称判断。 |

准入链：通用Filesystem.contains把not-startsWith(..)当containment证书 → 官方明确Windows跨drive/UNC relative()返回absolute路径使真实jail fail-open，并把共用predicate改为同时拒绝absolute → 修正Agent workspace/server/plugin authority的具体适用边界，owner为`PLATFORM-SECURITY`；不是“path check重要”的通用原则。POSIX绿测不能证明Windows旧bug已修，必须保该反证。其余#2648修复既有session routing owner、#2645统一既有SDK实例/能力检测，具体EX。MCP新旧activation/exec绕过search差异已保存，尚无额外可靠性/资源对照或具体旧论点差额，不据code-style imitation自动入选。

本窗其余6条具体EX（完整commit核心已读，不评分）：

- [chore(test): allow root script tests while blocking packages tests](https://github.com/XiaomiMiMo/MiMo-Code/commit/ca056a8ee4b05b64930e2bfe921738872eb64647)（13:42:06Z）与 [chore(test): restore root bunfig test root guard](https://github.com/XiaomiMiMo/MiMo-Code/commit/c68463f28dd6d27ee42d2739322029bc75274e00)（12:31:40Z）：repo测试从根运行漏fixture preload会写真实db，隔离root脚本tests并拒packages root；必要test安全事实保留，不把测试runner修复当Agent runtime新机制。
- [feat(compose): retire legacy compose agent, workflow, and skills](https://github.com/XiaomiMiMo/MiMo-Code/commit/3c6e6bb0f209bc53919617591b89c9710e5ff98c)（10:25:48Z）：移除deprecated agent/14skills、旧session unknown agent在read回default、提示字符串/测试match迁移；未说明新执行机制或失效边界，不因“compose”名称入选。
- [fix(provider): recognize model context window overflow prose](https://github.com/XiaomiMiMo/MiMo-Code/commit/f5a46bee683b402e1a8c6185e5d8ef36c7fe65b9)（09:59:10Z）：异常文案识别/normalization及ordinary400对照，局部兼容修复，非context策略新证据。
- [feat(release): publish tagged releases from CI](https://github.com/XiaomiMiMo/MiMo-Code/commit/4a5e2140bc2bb59744dbed34dc18d688d01ee5a7)（07:33:07Z）：tag-trigger验证/build/多channel发布与OIDC、idempotent stages；通用release wiring，没有本次模型/Agent执行机制增量。
- [docs(agents): keep only enforced conventions in the style guide](https://github.com/XiaomiMiMo/MiMo-Code/commit/c20b2f7e211ddac9c9e1172d30ef89fbd6792786)（07:28:01Z）：移除旧风格偏好、限定Effect try/catch、避免向用户项目强加repo风格，文档清理非新的训练/Agent可靠性证据。

### C3 — OpenAgentCore：只采用confirmed compute loss的retained recovery资格

家族：`MiniMax-AI/OpenAgentCore`。官方完整标题 [OpenAgentCore v0.0.10](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.10) / [OpenAgentCore v0.0.11](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.11)，API published_at分别 `2026-10-12T08:14:08Z` / `2026-10-12T08:47:22Z`（均本窗），tag分别`e0ae7f0be2cb446a8a5bbf67a6e0fafb140e0510` / `3c62df303fca89b970fe530528265712a68044a3`。一个家族，两发布事件不重复评分。**只有#667 qualified retained recovery拟贡献**，暂拟 **2 + 2 + 2 = 6**；其他普通部署修复不一并计贡献。释放writer authority涉及实际安全/正确性资格，仅该受影响机制深入。

完整release核心：此两版把部署修复和microsandbox lifecycle放进published installer；去除hosted startup等待周期polling，Files请求在原预算内等Environment初始化；workspace独立存储、idle suspension、retained memory snapshot并在compatible node恢复；checkpoint archive IO、workspace容量约束、confirmed compute loss恢复；初始化预算支持dependency install、login-shell package PATH、初始化不确定性settled后重连；source-build安装路径与Web显示lifecycle/capacity。v0.0.11在这些之外把Core/Web/init镜像都固定为publisher返回的immutable references，修复named-release仍混latest服务。**安装政策要求fresh installation directory，不支持不同distribution release原地migration**。v0.0.10当前官方说明明确建议用v0.0.11，不把较早缺陷版推荐安装。

受影响必要原件（已经读PR完整核心，未claim全面code review）：

- [Pin release Compose images to published digests #681](https://github.com/MiniMax-AI/OpenAgentCore/pull/681)，merged_at `2026-10-12T08:30:35Z`，实际commit `3c62df303fca89b970fe530528265712a68044a3`。原named release只有init固定，Core/Web用latest，可能混不同构成；publisher返回digest填Core/Web/init模板，同时保explicit overrides。已见render-compose校验每个镜像immutable GHCR格式与publish注入实际digest的受影响patch，tests有stable/prerelease/draft、不含latest断言；不把生成模板检查当已下载release artifact/运行Docker验收。
- [Recover confirmed lost compute #667](https://github.com/MiniMax-AI/OpenAgentCore/pull/667)，merged_at `2026-10-12T04:16:48Z`，commit `48292f409a042e2b8bb8588c87e1e1a7004dc867`。原crash/stopped VM可能留下永远owned running allocation；仅owning node证明exact-incarnation absence/termination、exact cleanup成功、initialized retained Session仍可continuation才释放。device revoke/allocation release/retention须在Session lock与compute revision下序列化；offline/uncertain writers继续owned。作者声称PostgreSQL guards/concurrency及native microsandbox/NFS场景通过；明确**host-crash durability、任意crash-tail完整性未qualify**，history缺失不能自动创建新native root。只采用这些限定恢复资格，不写普遍无丢失/无replay安全保证。
- 其余同窗commit标题限定于发布核心上下文：`Read release image index digests from JSON #679`（08:12:46Z）、`Remove hosted startup polling waits and await file readiness #678`（07:39:29Z）、`Show sandbox lifecycle and align deployment guidance #675`（05:27:35Z）、`Support installing a distribution built from source #674`（05:02:21Z）、`Reduce microsandbox checkpoint archive I/O #666`（04:11:39Z）、`Enforce workspace storage bounds #665`（04:11:31Z）。release后`Link Session snapshots only to existing saved Agents #683`（09:36:20Z）、`Configure idle suspension alongside node capacity #687`（11:43:27Z）不当v0.0.11已发布功能；只是具体后续commit线索，不为此扫所有历史revision。

准入链：compute不再running并不等于旧writer已被fence或retained native state可继续 → #667将exact-incarnation absence/termination、exact cleanup、initialized retained资格与Session lock/compute revision连成释放路径，并用native VM-loss/negative cases限定适用范围 → 可改变Agent平台在失联、compute丢失和native history缺失间的恢复设计选择；owner为`AGENT-PLATFORM`。尚未核实现/独立Evidence/Books差额。#681 immutable compose固定是成熟版本一致性原则的实现修复，具体EX；其真实安装兼容性仍保留，不因版本纠错扩充机制分数。

## 4. 明确排除及受影响安全/兼容核心

### EX-ZAI-UI — 官方UI插件集不是模型/Agent新机制证明

原完整题名：[feat(plugins): add official UI plugins and unified MCP App workflow](https://github.com/zai-org/zcode-plugins/commit/d1639cff514dcba29cfbfbc634d4609492640660)，committer `2026-10-12T03:52:50Z`、Source-Commit `f93887da7f6d22b68eb72a275489acf27f99de93`。本轮实际读原说明前段/构建契约和相关README，不把generated dist bundles当全量代码审阅。

核心：官方MCP Apps SDK组装interactive tool results、session panels、page/server tools、updateModelContext/sendMessage等；repo维护standalone artifacts/local marketplace，local desktop支持，web/mobile/remote只留普通MCP records。增加Excalidraw/OpenPencil/Blender等插件与统一构建发布规则。具体EX理由：展示既有协议能力与应用组合，没有说明新执行/状态机制或可靠性条件；不因可映射AGENT-MCP就评分/入选。

安全/兼容信号独立核受影响核心：[fix(openpencil): declare editor CSP and report startup failures](https://github.com/zai-org/zcode-plugins/commit/d8bd5dd997c40b5e5d1c73102657fc712d09a6cb)，committer `2026-10-12T11:57:16Z`，Source-Commit `b13778d5875c3825ed27e7046d53672f875f5dde`。实际patch为resource-level `zcode/csp`声明`wasmUnsafeEval=true,unsafeEval=true`以运行Yoga/CanvasKit WASM与.fig kiwi动态schema编译，**不启用Agent可选eval工具**；loader等待module-ready并在startup error/rejection/syntax failure转错误UI，完成后移除启动listeners避免误报编辑异常。浏览器fixture增加strict CSP draw/save/failure场景；原fixture明确不替代desktop partition/origin隔离验证。具体EX：应用资源权限声明与启动错误修复是既有SDK/CSP约束落地，没有证明新增安全机制或更安全边界，不把unsafe-eval声明当security hardening成果；保留真实权限事实供独核，不支持全desktop安全保证。

### EX-MINIMAX-CLI — v1.0.28配置接入/default模型

官方完整标题 [v1.0.28](https://github.com/MiniMax-AI/cli/releases/tag/v1.0.28)，published_at `2026-10-12T08:31:56Z`；对应 [feat: add Oh my Pi setup and default text to M3.1 Flash Preview #282](https://github.com/MiniMax-AI/cli/pull/282)，commit `a965e72ce424e465ae65ded102315bf73bef0aa3`（08:26:12Z）。完整release核心已读：agent setup加Oh my Pi/omp、interactive install与native YAML profile；text chat/repl/SDK默认MiniMax-M3.1-Flash-Preview，显式model与saved default优先；subscription agent setup默认Flash Preview，pay-as-you-go默认M3；Flash Preview只M Plan或MiniMax Code，pay-as-you-go需明确选M3。具体EX：新增集成/配置默认与availability约束，无训练/推理/Agent新机制或可比性能证据，不评分，不把CLI版本当M3.1模型首公开。

## 5. 本分支交接状态

- 已收集、日期夹窗与核心初筛：六源有限入口，root局部准入校准后3个**拟候选家族/命题**：UniRL#583（5分）、MiMo-Code#2650（5分，authority修正）、OpenAgentCore#667（6分，qualified recovery）。VeOmni及其他普通fix具体EX，不因同repo打包升分。本窗34个窄commit只是发现事件槽（5+2+5+11+1+10），不是34候选或34已全文审阅；另3个release事件，其中OpenAgentCore两版同家族。计数只表达本分支有限入口。
- 普通本分支来源收集待办：0。拟候选独立准入/Source审阅与Books判断移交root，**尚未完成**；本文件不代替其审阅记录。需要核实现的具体采用边界见C1～C3。
- 外部终态保留项：MiMo无日期Blog14项无法确认10-12日级完整覆盖；必要官方dated窗口片段或具名单篇原始发布到达时定点重开，不进入正面Evidence/Books、不支持零命中/互联网无遗漏。官方组织首10发现边界也不得扩称全组织覆盖。
- 本轮有限网页/API没有确认新的10-12论文；不能用此分支替代arXiv当日公告和root其他source分支，不重复其家族。
- 本文件只新增本日来源记录。未stage、commit、push；未修改Report、Books、Learning State或公共索引。
