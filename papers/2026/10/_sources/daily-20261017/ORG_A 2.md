# Live Daily 2026-10-17：机构组 A 原始检查

- 执行者：`live1017_org_a`；检查时间：2026-10-17 09:04～09:16 Asia/Shanghai。
- 仅本窗：2026-10-16 北京时间完整自然日。历史 cursor 未恢复；不扫描周级组，不扩到其他日期。
- 启动已读当前 AGENTS、研究合同、Report 合同、Prompt、来源使用说明/每日组与 ROADMAP；学习状态只核对暂停及 Live 路由，不复用历史完成声明。
- 本记录只负责来源发现、准入理由与必要原证。拟候选归并、独立复核与 Books 决定由 root 完成；这里的源码/测试读取不是运行测试或生产验收。

## 来源与实际停止位置

| 来源 | 实际入口、范围与停止位置 | 结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) → [Research Index](https://openai.com/research/index/) 首屏日期段 Oct 7 至 Sep 10，共9张卡，到 Load more 前止；首项已早于本窗，不展开旧页。[定点补检 Release notes](https://openai.com/products/release-notes/) 本窗至 Oct 15 段，止于 Load more。 | Research 首屏没有窗内发布。Release notes 10/16 有 Prompt-to-voice/nine voices，读完整说明及其 Custom voices 核心后贡献关闭；不是没有发布。Research index覆盖仅为实际有序首段，不声称全站无遗漏。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) Publications 首屏10项：10/16五项，10/12两项，10/9一项，10/8两项；止于 See more，不扩旧页。 | 窗内五项按下节排除，相关原文未见撤回/纠错指示。日期是官方页所标公开日期，不补造时刻。 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/) → [Publications](https://deepmind.google/research/publications/) 首段16 September至May2026；[News](https://deepmind.google/blog/) 首段 October6项至September边界，定点核相关October项原文日期。[Google Research Blog](https://research.google/blog/) 第一页12项10/16至9/17，止于page1/136。另打开注册入口 [Pubs](https://research.google/pubs/) 首屏1–15/11619，只作有限相关标题浏览，不逐项审阅或翻全年目录。 | DeepMind相关October发布原文为10/14、10/13、10/6，均窗外；Google Blog 10/16湿实验室按AI for Science暂缓。Pubs按年份排序且只给年份，不能提供本窗完整日期覆盖，保留目录日期限制。具名潜在相关 From Growing to Looping 已定点身份恢复为 arXiv:2602.16490v1（二月旧事件），不入本窗。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) web两次访问失败（Internal Error / timeout），改 [Blog](https://ai.meta.com/blog/) 首屏（日期非单调，最大Jul27）及官方导航 [Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication) 首屏，读至Oct14、Oct13、Oct2段后出现2019等旧项；止于Next前，不把乱序页向后遍历。 | 官方入口部分恢复但非有序、可按日本窗关闭的目录；首屏未恢复10/16相关材料，不能据此断言0或覆盖通过。恢复条件：Research/日期过滤入口可读取目标窗明确列表。 |
| SRC-QWEN | [旧入口](https://qwenlm.github.io/) 明示迁至 [qwen.ai/research](https://qwen.ai/research)。新页web提取0行；浏览器tab虽建立但读取超时，Mac锁屏，未得可读动态状态。按官方main.js→p_blog-useblog.hook.js/p_research-index.js可见请求恢复 page_config两个配置及article/retrieval中英请求，见下节。 | 有界原始API恢复成功但没有确认最新动态目录/精确空壳身份；保留限制，不用0行/空壳/旧配置证明窗内0。 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/) → [研究与动态](https://www.deepseek.com/news/)：动态首5项（最新2026-09-10）、研究索引首10项（最新2026-06-24），均已早于本窗，止于两处查看全部前。定点打开最新V4.1 Flash正文核9/10日期。 | 在该官方有序最新段无本窗发布；未见10/16撤回/纠错信号。不扩展旧索引或声称所有代码仓库无改动。 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog)现页26篇，最新2025-11-07；[MoonshotAI组织页](https://github.com/MoonshotAI)前10/42仓库按Last updated，最新kimi-code Oct16，第二MoonEP Oct12，故只展开kimi-code。官方release API首2项最新10/14；commit API目标窗一页100上限，实际3条，无下一页。 | 同一kimi-code项目家族的两项本窗机制/权限事件拟候选；第三TUI改动排除。组织页更新时间只作线索，具体事件以PR merged_at/commit对象交叉核对，不以仓库updated_at代公开日。 |

## 官方站点补检查询（只作线索）

实际web查询为：`site:openai.com "Oct 16, 2026" research`；`site:deepmind.google "October 16, 2026"`；`site:research.google "2026-10-16" "language model"`；`site:research.google/pubs/ "October 16" "2026" "model"`；`site:ai.meta.com "October 16, 2026" model research`及`"Oct 16" "2026" "AI"`；`site:qwen.ai October 16 2026 research`、`site:qwen.ai "2026/10/16"`与精确空壳ID。只处理返回的官方相关线索，不把搜索无命中作确定性覆盖。

OpenAI补检还返回论坛/Academy科学研究演示、伦理/教育使用视频，标题/完整summary指向科学应用与使用培训，未建立本项目机制增量，未扩展视频附件或全站；不是本窗候选池。

## 明确排除及窗外定点恢复

### Anthropic 10/16五项

1. [Designing more efficient quantum circuits with Claude](https://www.anthropic.com/research/designing-efficient-quantum-circuits)：官方日期10/16。核心是给8个量子电路规格和自动评分器后搜索更省量子资源的电路，属于暂缓的AI for Science；不以通用Agent/evaluator节点重新纳入。未见撤回/纠错标记。
2. [Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins)：官方日期10/16。已读正文从问题、PRNG/截断LCG/LLL恢复，到base points及Open questions。新增是NIST/ANSI曲线参数来源的密码学发现；原文明确不是cryptographic break，部分seed/base points仍未解。模型使用scanner和求解器不构成新Agent执行机制、评价混杂识别或可比可靠性边界；不因Frontier Red Team分类/安全词汇误收。
3. [The AI expectations gap](https://www.anthropic.com/research)；4. How employment is changing at Anthropic；5. Working at the frontier shapes expectations for the future。三者在官方列表明确Economics，内容主题是期待、就业/组织，不是模型形成、训练/推理系统机制；无相关纠错/安全信号，标题层范围排除，无需正文附件队列。

### OpenAI产品事实而非可留存机制

[Prompt-to-voice and nine new GPT-Live voices](https://openai.com/products/release-notes/) 官方10/16；对应 [Custom voices](https://developers.openai.com/api/docs/guides/custom-voices) 核心§Create a voice from a description：文本描述生成并保存voice、取得id重用、仅GPT-Live可用、合成来源透明提示、声音创建与session生成的retention边界。实际是产品开放/调用约束；未披露新的语音表示、训练/采样机制或可比系统实验，不能仅因跨模态/安全条款映射就入选，不评分。

### Google窗外与范围排除

- [Gemini 4 Argon available](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)、[safety](https://blog.google/innovation-and-ai/technology/safety-security/gemini-4-model-safety-security/)、[Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/) 原文均10/13；[EmbeddingGemma2](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)10/6；[on-device scam detection](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/)10/14。止于日期排除，不把旧安全材料扩为当窗深审。
- News October段 antimicrobial peptide 标题明确AI for Science，未为不影响处置的日期建立恢复请求。
- [Grounding AI agents in biological reality](https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/)官方10/16，完整官方核心已读。VERID追踪实验台3D/孔内体积/试剂/枪头、模拟后硬件检查及wet-lab闭环，评价目标为aptamer/protein binder发现。按ROADMAP明确暂缓科学应用，不用Agent、状态、Robotics通用映射绕开。原文的simulation/human oversight是该科学管线范围，不外推新通用VLA或安全保证。
- [From Growing to Looping](https://research.google/pubs/from-growing-to-looping-a-unified-view-of-iterative-computation-in-llms/)完整题摘有潜在迭代计算增量，但Google只有2026年份。定点原文 [arXiv:2602.16490](https://arxiv.org/abs/2602.16490)当前只有v1，history为2026-02-18；PDF精确版本也为2602.16490v1（2月18），当前页无修订/撤回信号。不是10/16新事件，未推进历史归属日审阅。Google其他年份目录条目不是本日逐项队列，目录日期覆盖仍受限。

## Qwen有限恢复与隔离

官方静态脚本显示真实请求：`/api/page_config?code=research.research-list`、`...research.latest-advancements-list`、`/api/v2/article/retrieval?type=qwen_ai&language=en-US`（中译zh-CN）。

- 两个page_config各返回60/19个旧配置对象，max date分别2025-12-23/2025-09-24，不能证明2026本窗覆盖；仅计算字段范围，不把旧目录变成审阅队列。
- article/retrieval中英各40篇，响应data只有articles，日期在`extra.date`，实际max均2026-09-20T20:00:00+08:00（Qwen-Image-2.1）；本窗条件无记录。加`page=2&page_size=40`返回相同first/last id，不能把未知参数视为有效第二页或读完全部动态列表；官方p_research调用本身没有传分页。
- 搜索得到精确 [空壳URL](https://qwen.ai/blog?%3B=&fom=research.latest-advancements-list&id=7a9090115ee193ce6a7f7195271d96dd93)，展示`2026/10/16 · undefined minute · 0 words`却没有标题、身份、正文；web再次打开0行，简化精确URL不可访问；直取`/api/v2/article/7a9090115ee193ce6a7f7195271d96dd93`为Not Found，三组已恢复对象均没有此ID。
- 结论：不能确认这是实际10/16材料、旧站slug、新接口UUID不兼容还是缺失页面的日期回退；不从搜索日期、empty words或404推断撤回，不计候选也不计已审重复。已穷尽本次有限原始恢复后隔离。恢复条件：动态Research可读的目标窗身份/官方精确文章URL、正文及日期。

## Moonshot：一个项目家族、两个本窗事件

来源：[public repo](https://github.com/MoonshotAI/kimi-code)。正式候选规模须按家族只记1，不把下列两项事件重复计家族。

### 日期/停止依据

- [releases API](https://api.github.com/repos/MoonshotAI/kimi-code/releases?per_page=2&page=1)：最新`@moonshot-ai/kimi-code@2.2.0` published_at=2026-10-14T15:31:16Z，次项2.1.1=9/24，均窗外；没有为10/16虚构版本。
- [commit窗口](https://api.github.com/repos/MoonshotAI/kimi-code/commits?since=2026-10-15T16%3A00%3A00Z&until=2026-10-16T16%3A00%3A00Z&per_page=100&page=1)：实际3条，小于100而止。精确PR当前closed+merged、merged_at与对应commit commit date一致，公开仓库可读；日期归属本窗，无需恢复提交前私有实现。
- 18c6d64272952503baccf706bff455bb6a2c488e = 2026-10-16T07:15:57Z；6e7cc909da9084a424f822dd5a9aae5b98070b73 = 05:23:18Z；8fcd3326e7488e5e0d4c595115ef74a10c340d5b = 05:28:52Z，后者仅折叠preview节省TUI行数，范围/贡献关闭。
- 必要原证为GitHub PR正文及commit API精确files.patch；没有遍历普通PR、旧release附件或执行测试。当前对应PR/commit未见撤回/纠错标记；与本次改动直接相关的已关闭细粒度开关方案是作者说明的设计边界，不当独立候选。

### 事件A：reload后的上下文变更比较基线

- [PR4019](https://github.com/MoonshotAI/kimi-code/pull/4019)，[精确commit](https://github.com/MoonshotAI/kimi-code/commit/18c6d64272952503baccf706bff455bb6a2c488e)，[commit原件API](https://api.github.com/repos/MoonshotAI/kimi-code/commits/18c6d64272952503baccf706bff455bb6a2c488e)。建议准入：系统prompt冻结但磁盘/能力目录变化 → 以渲染时注入内容seed、持久化比较基线与watch/reload共享去重，undo/clear/compaction协同恢复 → 需要将“当前外部状态”“进入上下文的描述”“运行时实际允许能力”分开，不能把reload完成等同模型上下文已更新。
- 初步分数2+2+2=6，标准审阅；实际纠正删除漏检/恢复失效的必要层已深入代码。可能owner为AGENT-CONTEXT，是否已有覆盖由root读当前正文决定。
- 完整读取本commit新增`packages/agent-core-v2/src/agent/changeNotifier/changeNotifierService.ts`509行及`changeNotifierOps.ts`62行。seed由rendered AGENTS文件分块hash、skill listing、profiles/model pool构成；AGENTS逐文件exact hash避免尾部删除仍被substring命中；catalog回到最初内容仍需相对更新后的基线比较。subagent提醒含profile添加/删除、模型描述/default变化，并受当前persisted binding的工具/allowlist gate控制。
- Ops：`changeNotifier.snapshot` durable、replayable、undoable；ContextClear/ContextApplyCompaction清空。reload路径先mute旧notifier，reload配置/插件/目标workspace目录、close/resume再notify；失败unmute并补notify；active turn/compaction拒绝。不是重写冻结system prompt，长运行非main subagent不接收这些提醒。
- 直接相关tests已读断言/用例：尾删/清空、announced-then-deleted、watch与reload双向去重、rendered snapshot而非二次读盘、model pool已无→有、undo回退、clear/compaction清空、mute在途抑制、disabled tool时无reminder。只核官方测试源码，作者宣称套件通过不升级为本次执行事实。
- **重要收窄**：PR把信念称“投递即信念”，但源码先`await recordSnapshot(...)`再`reminder.notify(...)`；Skill/Agent工具不可用时明确仍推进基线而不通知，tests亦覆盖。因此不能声称严格“模型已读/消费确认”、exactly-once delivery或物理动作事务保证。可支持持久化比较基线与上下文生命周期的设计案例，不支持模型真的遵守新规则、安全/性能普遍改善。

### 事件B：guard配置语义扩宽，确认策略与硬阻断分层

- [PR4250](https://github.com/MoonshotAI/kimi-code/pull/4250)，[精确commit](https://github.com/MoonshotAI/kimi-code/commit/6e7cc909da9084a424f822dd5a9aae5b98070b73)，[commit原件API](https://api.github.com/repos/MoonshotAI/kimi-code/commits/6e7cc909da9084a424f822dd5a9aae5b98070b73)。贡献链：用户可能以为dangerous_command_guard=false只去掉危险shell询问 → 同一键现扩为全部built-in ask策略 → 配置兼容不代表审批安全语义兼容，必须分别看用户规则、内置询问、工具硬阻断。
- 初步分数1+2+2=5；属于实际安全/兼容约束变化，深入受影响层。仅该版本事实未必改变Books，PLATFORM-SECURITY或AGENT-TOOL-CALLING现正文若已有此分层可具体NC/仅报告，不能自动写入。
- 完整读取全部6文件patch：changeset、两语言配置文档、`git-control-path-access-ask.ts`、`sensitive-file-access-ask.ts`、permissionPolicyService.test.ts。两策略新增注入config并在`!isDangerousCommandGuardEnabled`时return undefined；链顺序未改。
- 明确边界：默认true不变；Never Ask本来不启用这些ask；false时Ask When Needed仅自配ask仍可问，Always Ask未autoapprove的tool照旧问。`Read/Write/Edit`的秘密文件PATH_SENSITIVE硬阻断在工具层，按PR行为表与文档未改变；不能把policy测试中Read `.env`被approve当整个tool执行已获放行。
- tests源增四个策略落点断言（危险命令、敏感文件、git配置写/读到yolo-mode-approve）；不能证明工具层secret block实际运行，也不证明关闭guard仍安全。作者强调开关仅适用于Agent之外已有命令限权的环境；无本次运行或部署保证。

## 本执行者结论与交接

有限来源已处理到上述停止位；拟1个kimi-code家族、2个事件；Qwen动态目录/空壳、Meta Research与Google Pubs日期目录按具体限制隔离，不支持零命中、完整召回或覆盖通过。未修改Report、Books、LEARNING_STATE、索引与其他日期；未stage、commit、push。

## 同窗追加：八项 exact-v1 Source 与实际 owner 对照

本层不是重新发现：仅处理 root 已核官方 CL recent Fri Oct16 首50中的八项。首公开归日沿用当日发现层，不把 HTML 的 submission 日期当公开日期；以下均锁定 v1。建议评分均为初步判断，不替代独立 DAY、Source/PRE 与实际写后复核。未写入 Books。

### 2610.22209 MemoryEval：具体 NC

- 原件：https://arxiv.org/html/2610.22209v1 。已读 §3–7 的生成、指标、主要结果与局限。
- 机制：30条轨迹、6类、3等级、147份生成文档；以状态 claim 检查记忆内容，再与下游 QA、更新/遗忘和动作分类分开。状态 claim coverage 使用 embedding 阈值加 LLM entailment，并非无噪声确定评分；11个运行的330个实例不是330条独立轨迹。人工检查修订11%内容、28%脚手架。
- 反侧：intrinsic 跨全部状态平均，extrinsic 是最终状态 QA，二者差值不能独立归因检索。三 judge 不能消除噪声；仅事实演化，不覆盖 episodic/procedural；30轨迹不足细排名。表4与正文个别数字不一致，不将相关精确值写成通律。
- 实际 owner：Ch77 AGENT-MEMORY 的“先分开 Construction 与 Retrieval Failure，再选择 Memory 结构”(约951–986行)已有固定 consumer/检查检索证据；“先分解 Memory 组件，再判断 Graph 是否值得”(1123–1167)已拆 extraction/storage/retrieval/maintenance/use；“用干预矩阵定位写入、检索与阅读失败”(约1348起)已有 oracle/full-context/fixed-reader 干预。typed transition 段(95–141)也已说明写入动作不是真实性。
- 结论：2+2+2=6，标准 Source；新 benchmark 支撑现有因果诊断链，但未给出当前 owner 缺失的新决策边界，故具体 NC，不以题材相同代替比较。

### 2610.21900 TEM：最小 PRE 候选

- 原件：https://arxiv.org/html/2610.21900v1 。已读 §3.1–3.5、算法1/式1–5、§4.1–4.7表与讨论局限。
- 机制：fact=(subject,relation,object,session,index)；按规范化 subject+relation 分组，保留全部 object。先在完整组确定 max index，较旧项标 HISTORICAL，再做相关性 Top15；并非仅在检索结果中选最新。返回按来源顺序排序、携状态标签的证据，不默认滤掉历史。
- 评价：60 persona/600 session/420问，4 backbone、6配置；matched-unmarked 保留相同内容与顺序。状态测试有明显标签收益，但 LoCoMo 两 backbone 上 marked/unmarked 几乎相同，不能把混合证据组织收益全归标签。LoCoMo 未决 judge 项以总分母区间呈现，不是置信区间；长上下文基线有大量截断。构建与 embedding 成本未计入节省证据 token。
- 反侧：同一最大 index 的冲突未解；假定单值关系和摄入顺序，不能替代 event valid-time、延迟报告或并行偏好处理。选择性重排也不证明完整时间推理。
- 实际 owner：Ch77 约1210–1235的双时态/修订段已有 valid/transaction time、supersession、旧版本可能更高相关，以及 consumer 的按时选择；缺的是“完整组状态先于 TopK”的具体失败边界。
- 建议2+2+2=6；最小拟文：版本状态应先由完整、已提交的版本组确定，再交给相关性检索。若只在 TopK 内选“最新”，新版本漏召回会把旧记录误作当前。历史项可保留以支持 as-of 查询，但应携带来源顺序与 superseded 标记，由 query 决定使用；摄入序号不能替代有效时间，同序冲突仍需显式消解。该路径增加版本组维护成本，标签对状态问答的收益也不能外推到所有长期对话。

### 2610.21571 ToolGraphNegative：最小 PRE 候选

- 原件：https://arxiv.org/html/2610.21571v1 。已读 §2–4、主表1–2、附录A1–A2核心设置及直接相关A3。9个开放模型2B–120B，3次运行；ToolSandbox train825/test207，BFCLv4 640/160底层任务分离。
- 机制：ToolNet 是工具后继加权；H-EPM 为完整工具集叠加 contextual top2后继和轨迹摘要，仅推理配置，不是 RL。图由训练轨迹的 best-of3 形成，摘要另有 LLM 成本。
- 关键反侧：随机建议、无建议仍保留不少收益；仅加“先尝试可用工具再放弃”的无图对照可相近且较便宜。表2括号是 BASE失败→变体成功子集的 TOOL-call 比率，非全体 LLM-call 或严格等算力比较。oracle 正确 next-tool 也未指定调用必要性、依赖和参数；人工 earliest-failure 分类不是互斥因果真值。
- insight 从相同训练经验蒸馏软规则，多数但并非全部模型/任务优于 BASE；H-EPM+Insight 在7/9设置更差且多2.68 LLM calls，不支持普适协同。不能把负结果写成图无用。
- 实际 owner：Ch77 1123–1167已有记忆组件消融，667–720/1091–1123已有 advisory procedural memory 与规则准入；尚未明确继续尝试预算、random/no-advice、无图 persistence 对照对图增益归因的约束。
- 建议2+2+2=6；最小拟文：比较工具图记忆时，除了相同经验和工具集合，还应控制继续尝试的策略及调用预算，并加入随机建议、无建议与无图但鼓励尝试的对照。否则收益可能来自多一次探索，而非图边本身。正确的下一工具仍不等于正确调用时机、依赖或参数；稳定依赖下图仍可能有价值，但应把构图、摘要、额外调用和失败代价一起记账。

### 2610.21731 RetrievedNotRead：最小 PRE 候选

- 原件：https://arxiv.org/html/2610.21731v1 。已读 §3–6与局限。225个较训练截止更新的事实、6域；冻结223事实的同一10结果菜单，必要时插入 gold page，比较6个开放配置与 Luna。GLM cutoff 不明，行为检查不是预训练未见证明。
- 机制/观察：菜单可达、工具 open、open且引用是不同层级。准确率排除 abstention；跨 prompt 汇总与 bare-open 的分母不同。snippet-only 陈旧回答比例较高是相关性，不能证明 open 的因果收益。
- 直接干预：50 sports 同页直接入 prompt 对3模型降低陈旧回答，但非全任务普适；在已失败的157 fact-check 上重复问题恢复41次，不能写成全部任务提升26%。Jacobian/logit lens 发现更新候选早期提升后被旧答案覆盖，未做 activation 因果干预，且仅3模型sports首token候选。
- 实际 owner：Ch76 RAG 682–688已有每项阅读深度与可用工作集，688–740已有 relevance/sufficiency/faithfulness，1018–1045已有来源因果与 probe 非真值。缺的是工具菜单可达→open→有效使用→claim支持的分层观测和同页干预。
- 建议2+2+2=6；最小拟文：搜索结果中可达不等于页面已打开，工具 open 也不等于 reader 用到了证据。应将菜单、实际返回片段、open/find轨迹和 claim 支持跨度分别保留；必要时用同页直接入上下文、读后重申问题等局部干预定位使用失败。摘要已充分时不必强制打开全文；额外读取有预算与噪声成本，小样本特定域的恢复率不能当通用策略保证。

### 2610.22300 LinearKnowledge：最小 PRE 候选

- 原件：https://arxiv.org/html/2610.22300v1 。已读 §3方法、§4设置、§5主要结果、§6讨论及直接相关控制。
- 机制：旧关系答案随机双射为新动物标签；训练/留出 subject 分开、4训练模板与第5测试模板分开。全参数20epoch拟合标签第一token。预训练 subject末token隐状态用PCA16白化+岭logistic，nested CV在训练subjects选layer，held-out subjects未进入fit/selection。
- 评价：70关系、11模型2B–27B，prelinearity与重标记泛化相关，控制 recall/类别数/样本数/频率后仍存在相关；Dolma频率只是共同代理，不是各模型训练集。首token区分不了同首token答案；70关系内相关不证明线性结构因果必要/充分。更多label类别、重随机、另一数据集控制仅覆盖子模型/子关系，不升级全覆盖。
- 实际 owner：Ch5 77–112有表示的分离/不变/组合用途，185–211有记忆与泛化，295–365有证据层级及“存在/可解码/实际使用”三分，513–534有知识获取/保留/泛化；未显式区分事实复述与使用事实学习新关系的 readiness。
- 建议2+2+2=6；最小拟文：能复述事实与能把一组事实用于学习新关系不是同一能力。将旧关系答案固定随机重标记、对 subjects 和表达模板分别留出，可以检查表示是否为后续关系学习提供可迁移结构；线性 probe 的留出预测力可作 readiness 诊断，但相关性不证明训练确实沿该方向使用它。有限类别首token、全参数拟合下的结果不能直接外推到自由文本推理，应由真实下游留出评价兜底。

### 2610.22169 LexFrame：最小 PRE 候选

- 原件：https://arxiv.org/html/2610.22169v1 。已读 §3式1–3/各order、§4.1–4.4、附录C1–C3公式成本、D讨论。
- 机制：把 remaining-layer transport 及上下文放入词汇读出，梯度方向 Jᵀ(w−mean w)、基方向 J⁺s；实际非线性 transport 的系数不能用一个点积替代。order0仍运行剩余所有层，只将attention替成校准估计；order1读取prefix的order0状态，order2加入relay；infinite order等于完整模型输出是定义边界。
- 评价：SmolLM3-3B/OLMo3-7B、WikiText103校准/测试、16 checkpoints；agreement/KL是对模型输出的忠实度，不是真实性。状态替换/runner-up steering 是有限局部因果证据，不证明某语义方向普遍安全。coherence界约束定义好的固定单位方向平均余弦，不覆盖全部非线性probe。
- 成本与反侧：order n需 n+1条剩余计算流，读全层约(n+1)(L+1)/2次forward；“可跳过45%/42%层”是agreement阈值读数，reader本身仍执行后续层，不是已实现净加速。早退/幻觉检测/编辑是未来应用。
- 实际 owner：Ch5约331–338的Jacobian-adjusted lens已写局部Jacobian和跨上下文平均局限、干预要求；尚未明确context-specific finite-order residual transport的读出边界/成本。
- 建议2+2+2=6；最小拟文：固定读出会平均不同 prefix 的后续变换。另一诊断先声明保留多少后续计算，再用剩余层及有限阶 prefix 交换构造上下文特定读出；它能更忠实地复现最终输出，但忠实度不等于该层状态单独拥有事实，也不等于输出为真。阶数提高需要重跑更多后续计算，不能把潜在早退位置直接记成净推理加速。

### 2610.22100 NoveltyPatching：最小 PRE 候选

- 原件：https://arxiv.org/html/2610.22100v1 。已读 §3–8、五张主表与局限。
- 机制：novelty训练目标用未来字符串在前128byte是否见过、最长16的匹配长度；运行时仅用前2byte表及1byte/global回退，是因果proxy，不是偷看未来。训练4MB表、目标patch率10%；实际率10.9–12.1，不能说严格等compute。BLT式全局patch+局部128byte，1M/12M/50M。
- 评价：数学真前缀teacher-forced greedy answer-span准确率，不是端到端解题；50M上computed/final span增益明显但BPB更差，小模型弱。code/trace在相同实际patch率下entropy更好或接近噪声；boundary coverage/novelty预测好不保证任务好。BLT1B直接换规则出现computed改善但final塌陷，12M换entropy也塌，须联合训练/对齐。混合Apple/T4/A40等环境无生产时延结论。
- 实际 owner：Ch11 378–396有动态patch、全局压缩、offset与causal verifier、scratchpad熵lag及额外attention成本；未写entropy预测困难与全局compute边际收益可能不同。
- 建议2+2+2=6；最小拟文：下一byte的高熵是patcher的预测困难，不必等于全局计算最值得花的位置。可用离线重复/新颖性目标训练因果边界proxy，但未来信息只能用于监督，运行时边界仍须由已见前缀决定。比较需同时核实际patch预算、BPB与目标跨度/端到端任务；边界策略通常需联合训练，不能把一次规则替换当无损部署，code/trace等域仍可能更适合entropy路径。

### 2610.22071 UTF16Boundary：最小 PRE 候选

- 原件：https://arxiv.org/html/2610.22071v1 。已读 §2–3/P1–P5、§4主要设置与结果、§5.1–5.2/5.6、§7局限及直接相关审计。
- 机制：UBE以不相交route alphabet混合UTF8/UTF16LE；3byte BMP变2byte低位优先，supplementary仍4。边界目标先对齐同一scalar/grapheme集合，删除cluster内部切分；合法target不保证预测器合法。相同左上下文和可见首symbol而目标相反时，确定性一symbol-lookahead无法辨识；编码顺序可改变可见信息，但跨page低byte碰撞仍存在。
- 评价：同raw exposure的LSTM512、4000steps、2seeds、17语言；非同FLOPs，因为位置数不同。UTF8多lookahead后逼近UBE，证明受限接口的信息可见性差异，不是UTF16普遍优越。UBE-BE全历史也改变，不能隔离为首byte唯一因果。sentence bootstrap不覆盖run variance；公开转码模型训练不同，不能做编码因果比较。
- 反侧：未训练完整新目标UBE LLM，无端到端收益/吞吐结论。删除目标边界会改变patch数；需控制预算、teacher/localdecoder/suffix/BOS条件。batch composition和条件似然审计不能升级为文本边际likelihood。
- 实际 owner：Ch11 122–144有UTF8合法性，322附近是pretokenizer硬边界，378起动态patch；均未写合法可逆编码与有限lookahead可辨识性的区别。
- 建议2+2+2=6；最小拟文：编码可逆不等于受限lookahead下的边界策略可辨识。若同一左上下文和可见编码前缀对应相反切分目标，再好的确定性预测器也无法同时正确；应分别审计target合法性、运行时信息是否可见与实际预测行为。改变字节顺序只是一个有碰撞边界的选择，增加lookahead和保留稳定UTF8也是基线；更换编码须重新对齐tokenizer、teacher、局部decoder及预算，不能热替换后宣称模型能力提升。

八项 Source 已有限完成；未遍历全部附件、未运行实现、未修改 owner。NC/PRE 为本执行者建议，等待 root 独立取舍。

## 同窗追加：六项指定 Source（不扩发现）

只接 root 已完成题摘的六个身份，日期沿用其同窗发现证据；全部锁 exact-v1 HTML。以下“PRE”均只是最小贡献草案，不授写入、独立 PRE 或 DAY 通过。实际对照了当前 owner 的局部正文与邻接，不声称全章/全附录已读。

### 2610.22355 OmniVerifier-C1：最小 PRE 候选，TRAIN-RLHF

- 原件：https://arxiv.org/html/2610.22355v1 。已读 §3.1–3.2、§4.1–4.2、§5主表/设置/分析、B.2/B.5、C局限；B.3/B.4为有限补充，不遍历附件。
- 机制：复杂要求拆 K 个binary子问，总分为通过比例；SFT先学分解，再把每对prompt/image转为1个global评分与K个local判断的混合RL样本。global reward=1−绝对误差，local reward=答案匹配。Qwen3-VL-8B，80步/16A800；generator另训200步。理论排序界假设无损分解、已知真实满足数z，以z/K作reward，因此不能证明实际学到的分解/判断必然保序。
- 具体差额：这里 pairwise 不是winner/loser偏好，而是提供 ground-truth目标图，与generated图逐条比较；pointwise必须从初态+规则先推目标。参考图把目标推断移出judge，但没有消除视觉判断错误，更没有对非唯一正确状态提供免费oracle。文中epsilon相加是建模说明，不采用为任意judge的严格误差不等式。
- 评价/反侧：GenEval/CLIPScore和六种规则游戏的normal/hard，hard不进训练，Gemini3.1-Pro独立于数据处理但仍是模型judge。200子问人工标注由5人各40题、并非每题五人一致；更细21–30子问反而比11–20误差高，会重复加权或引入原prompt无关要求。游戏场景有明确目标，不能推出开放世界推演、真实物理或DiT唯一拥有reasoning。
- 实际 owner：Ch31 292–301已拥有binary criteria聚合、rubric来源/覆盖、非真值与must-have gate；105–107已有生成解释/逐判据训练。新缺口仅为“judge自行推目标”和“显式参考状态比较”的信息权限差异，不重复讲graded reward。
- 建议2+2+2=6。最小拟文（接既有rubric分支）：规则任务若能独立产生可信目标状态，verifier可直接消费该reference比较候选，避免同时承担目标推演与视觉判断；这与两候选偏好不是同一pairwise合同。应绑定reference的产生方式和允许解集合，逐项分解也须避免重复或增造要求。参考制备、额外视觉输入与局部评分均付费；目标不唯一、reference不可靠或视觉judge失配时，保留原pointwise/rubric与独立规则执行器，不以更细分数代替正确性验收。

### 2610.21633 ContextLift：最小 PRE 候选，TRAIN-SFT

- 原件：https://arxiv.org/html/2610.21633v1 。已读 §2–3完整方法/设置/表1–3、结论、Limitations及privacy/scope。正则取首user turn中请求标记之前的6–60词前置语境；20%安全混入预算中，一半原始generic rows、一半相同rows加随机搬运的训练语境，答案不改；70%前置/30%后置，无生成模型或harmful标签。
- 评价：Qwen2.5-7B-Instruct/QLoRA rank32、一epoch，3seeds；security/legal/medical纯有害与10%稀释。比generic同例数/步数；重复但不加context的对照不改善，everyday context已去掉大部分差额、训练域context进一步改善。单LLM judge，rate分母仅coherent answers；未缓解组约40% cued答案不连贯，不能忽略。无句首语境时退化为duplicate，medical uncued也未改善。
- 关键反侧：保留ID任务意味着仍会按请求给坏建议，并非去除有害能力或得到安全模型。只覆盖原数据包含的语境，未知system/output-format触发及跨模型/配比未证；复制用户第一人称语境还增加个人信息重复曝光。四个benign任务未见明显费用不证明任意任务无损。
- 实际 owner：Ch29 55–57已有剥离有害意图/保留良性语境的配对监督；977–981已有默认prompt压低不等trait删除、匹配训练条件再评价。缺的是同预算把适配语境放进不变aligned targets来打断“有该语境→坏答案”捷径，而不改变窄任务目标。
- 建议2+2+2=6。最小拟文：通用安全混入未必打断适配语境与坏答案的共现。可在固定混入预算内，将部分良性示范复制后加上从适配数据抽出的情境句、保持原aligned answer，用反事实配对降低“看见该语境就换persona”的捷径；搬运前仍须确认语境不改变原请求含义并执行隐私处理。默认、语境匹配、真正域内请求与benign效用应分开测；这条数据分支不删除原有害窄任务，也不覆盖未被搬运的触发器，原安全监督及独立发布gate仍保留。

### 2610.21679 TokenizerMetrics：具体 NC，MODEL-TOKENIZER

- 原件：https://arxiv.org/html/2610.21679v1 。已读 §3 U-statistic、§4材料、§5–9方法/主要评价与反侧、Limitations。29项报告指标，48 benchmarks；TokSuite14个1B、TIMTC可用45个350M、VISTA130M/350M多语词表控制。U-stat以token内最弱PMI加两端较小branching entropy，汇总词表可把原本局部有用差异洗掉。
- 评价不是“所有相关为零”：13指标汇总显著但弱，最强约r=.27；同指标跨任务/语言/模型suite可变号，两个指标组合的增量R²至多.01。orthographic任务仅TokSuite英文弱显著，其他多为近chance。compression仍对成本有用，不能由不稳相关推出tokenizer无关或intrinsic指标全废。
- 反侧：最大1B、部分任务近chance；TokSuite的tokenizer语料/normalization/pretokenizer/词表大小共同变化；TIMTC英语、VISTA小模型/部分语言数据不足及head大小变化。不同token预算、raw exposure与参数量不自动等compute，不能宣称完全隔离通用因果；语言benchmark/形态标注覆盖不等。
- 实际 owner：Ch11 约288–310“多语言中的隐藏不公平 / Fertility是Language×Domain的成本与可达性合同”已经明确tokenizer不能单独决定能力、fertility不是quality；85–100的quality/source-support merge分支要求分别验压缩率、原文曝光、模型行为与生命周期费用；101附近proxy emission/邻熵不是真值。当前取舍已能承载：intrinsic用于接口/成本诊断，独立真实任务验质量；本文未给可靠替代预测器。
- 建议2+2+2=6，作为受限多suite负证据准入，但 Books 具体 NC；不新增指标清单或把有限“不可靠预测”写成所有规模数学不可能。

### 2610.22046 HiddenStateProbe：最小 PRE 候选，PLATFORM-EVALUATION-SYSTEM

- 原件：https://arxiv.org/html/2610.22046v1 。已读 §2定义/rollout协议、§3全部probe/控制、§4定位/直接反侧、§5局限；不遍历全附录。
- 目标：detection最终标签、continuation value估计、pit定位是三任务。每步至少400tokens；有限4–16 rollout、隔步scan，在一条实现trace上取当前及其后prefix value最大包络，阈值.1首次跌破为pit。该max不是最优policy值，capability gap不是绝对不能解题；局部第一无效步骤也不是pit。
- Qwen3 thinking 4B/8B、hardmath。final-label probe对每步广播终局标签，训练的是step-weighted conditional outcome，不能识别未来已实现轨迹的包络；exact recovery不可能界还需条件方差非零，该方差未测，不用此界解释实际失败。替代probe还改变mask/weight/schedule，次序反转不归label唯一原因。
- 评价：相同problem split、与无hidden的text/长度规则比较；单probe定位未胜长度，ensemble仅一种权重胜。8B只测value probe，无gold collection且用seed均值非paired interval。最重要限制：约一半trace的final read位置落在更早步骤，未用正确位置重评分；有限rollout标签也有不一致。因此负结果仅约束所存状态/所试probe，不能断言内部无定位信息。offline rollout search读取定义reference的同批rate，不与probe accuracy作独立能力排名。
- 实际 owner：Ch66 282–291已有probe人口/null/shuffle/容量/held-out和输出控制分责，363–365有token信号聚合非权限；Ch5 343起“存在/解码/实际使用”也已有一般边界。新具体缺口是“终局正确性标签不识别可恢复性/错误位置”，以及长度基线、读位置与rollout标签合同。
- 建议2+2+2=6。最小拟文：错误报警、从某prefix继续成功的概率和失去可恢复性的步骤，应建立不同标签与评价合同。把终局对错广播到每步，不能据此把最低probe分数叫作根因或首次错误；定位至少要胜过长度/位置基线，保存实际read token、步骤划分及有限rollout的阈值和预算。追加续跑能提供受策略与采样限制的reference，却增加成本，也不证明绝对不可恢复；读位置或标签噪声未闭时保留Unknown，回到外部重放/人工诊断，不把负probe写成信息不存在。

### 2610.22065 ABNAT：最小 PRE 候选，INFER-TENSORRT-LLM

- 原件：https://arxiv.org/html/2610.22065v1 。已读 §2、§3全部机制/式1–8、§4设置/式9–11/主消融与mismatch/成本反侧、结论。clean冻结teacher与同checkpoint噪声student；对每head的postsoftmax attention跨query平均、去CLS后以KL对齐，并与task CE/logit KD联合。它并非匹配完整query×key矩阵，更不认证teacher路线为真实语义因果。
- 选择：noise drift×clean concentration排名，校准一次固定top-k；另有Last-block整块选择。主结果full alignment，不能把选择版费用和主结果无条件拼接。teacher无须另训，但必须额外forward/存attention。
- 评价：W8A8 bit-plane乘性Gaussian conductance扰动，NeuroSim及TIA/ADC误差模拟，不是新实芯片；ViT/CIFAR主体，有限Pythia WikiText与CLIP retrieval。30 seeds是inference噪声重复，不是30次独立训练。mismatch只扫给定σ，不覆盖任意硬件漂移。LM高噪声相对PPL降低仍有很差绝对PPL，不能授部署可用；attention漂移相关也不证明唯一路径。
- 反侧/费用：AttnAlign独用高噪声弱，必须核task/logit协同；full比NAT训练时间/峰存约多82.9%/54.4%，Last4有小质量损失但降到40.8%/23.3%。所谓无推理开销只指训练目标移除后同NAT推理图，不是已实测相同能耗/服务SLO。
- 实际 owner：Ch49 1275–1283已有Analog CIM expert/router联合校准和noise artifact身份，但未有dense attention分布作为噪声适配的teacher目标；Ch29 hidden distillation段只拥有一般teacher监督，不重复硬件特有验收。故唯一落点建议Ch49该analog局部。
- 建议2+2+2=6。最小拟文：模拟存内噪声还可能改变dense attention的内部路由，最终预测或logit贴近并不约束该变化。一个训练期分支用同checkpoint的冻结clean路径监督噪声路径，在task/logit目标之外对齐选定head的attention统计；高漂移与clean集中度可作预算选择代理，但不是语义真值。额外teacher前向、attention存储和校准均计费，选择版也需独立质量验收；有限噪声模拟不签实芯片或未知漂移保证，目标硬件/任务不匹配时保留原NAT、较高精度或数字fallback。

### 2610.22293 SST：最小 PRE 候选，TRAIN-SFT

- 原件：https://arxiv.org/html/2610.22293v1 。已读 §2.1–2.3方法/式1–3、§3关键实验、§4.1直接比较、结论/limitations、B.12–B.14的必要超参/成本/训练身份。
- 机制：从anchor W取top-k左/右奇异基U/V，把优化器完整delta投到 `(I−UUᵀ)delta(I−VVᵀ)`，删除protected→protected及两个cross-block，仅free→free可动。r=.99是奇异方向rank比例，不是99%能量。固定anchor可保持其受保护作用，非全模型behavior保证；refresh重新在当前W定basis，会让旧保护方向进入新free空间，故保护相对原模型变松。
- 关键控制：Adam坐标预条件不与投影交换，raw gradient投影不能保证最终delta confinement；toy仅0.5B/8例/60steps，不能外推所有optimizer任意实现。OPLoRA本来就以固定两侧投影约束BA，不能说它漏投；差异有rank、factor坐标、moments和refresh，不是只差“是否正交”。
- 评价：主要Qwen3-8B四域thinking，SFT/SDFT/Muon，scale/data/两三阶段补充；prior capability是给定benchmarks平均，WikiText KL/保留长度不等完整行为保持。R10可损失3–5pp retain，低LR个别ID仍由SFT最高，matched常用LR不等各方法充分调优；hundredsB和更长序列未验。
- 费用：无新可训参数/推理图改变，不是零训练代价。每步projection、basis存储和Gram/SVD刷新均付费；B.13的step实测和8GPU独立分解的摊销估计口径分开，不拼成无条件低于1%的总训练开销。
- 实际 owner：Ch29 1037–1064已经拥有rotation保护、梯度proposal≠Adam最终delta、动态mask刷新与anchor-gradient来源。因此不重复泛泛“保护最终更新”；最小新差额是保护对象为weight的双侧singular action，必须同时去cross-block，以及refresh换锚对原基座保护的含义。
- 建议2+2+2=6。最小拟文：若保护对象取自anchor权重的左右主奇异方向，限制必须同时落在delta两侧；只删protected→protected块仍允许一个方向读入或写出而改变原作用。固定basis下将优化器完整delta限制为free→free，与按历史样本估计方向或mask不同；重新在当前权重分解会开放新自由度，也把保护合同从原anchor改成一串新anchor。分解/存储/刷新付费，rank和refresh须按新旧任务共同验收，谱保持或低KL均不能替行为保持签证。

本执行者14个指定arXiv Source与7机构有限发现到此结束。未运行代码/实验、未遍历完整附件、未继续历史cursor或下一日；Report、Books、LEARNING_STATE、index未由本执行者修改，未stage/commit/push。

## 同日定点补闭合：五项既有未决身份

承上14项的有限任务之后，root另授同一10-17 Daily中的五项定点恢复；不是新日或扩大来源。已重读当前AGENTS、研究合同、Report合同、Prompt、来源使用说明/每日组、ROADMAP及本日相关停点；原有有效笔记不改。

### 身份、日期与当前信号

- 实际复核官方入口：https://arxiv.org/list/cs.CL/recent?skip=0&show=50 和 https://arxiv.org/list/cs.LG/recent?skip=0&show=50 ，均停首50，只定点核五个已知身份，不追加发现队列。CL的Fri,16 Oct2026分组中：22127在[18]、22067在[23]、21553在[43]；LG同日分组中22099在[25]、21979在[37]。与五个abs的唯一v1联合，归属本窗2026-10-16，不把Thu15 submission改名公开日。
- 已读 https://arxiv.org/abs/2610.22067v1 、https://arxiv.org/abs/2610.22127v1 、https://arxiv.org/abs/2610.21553v1 、https://arxiv.org/abs/2610.22099v1 。21979的exact-abs初次读取错误，以 https://arxiv.org/abs/2610.21979 恢复：唯一v1、题摘与 https://arxiv.org/html/2610.21979v1 一致。五页当前均未见撤回、删除、纠错或额外版本信号；仅为本次事件页轻量检查，不是全站无更早稿证明。

### 2610.22067 Beyond Context Length / LURCH

- 原件：https://arxiv.org/html/2610.22067v1 。完整题摘准入链：同长度不能说明长上下文推理难度→对证据scope/dispersion与DAG依赖depth作实例级定量→评价不能只按窗口长度或单needle分层。建议2+1+2=5；已读§3–5.5、结论/直接反侧。
- Scope为扩展证据token数/L；dispersion为首末证据之间非证据数/(L−证据数)，非单纯距离；depth为原子查找/推断DAG最长链节点数，额外并行lookup不增加depth，也不表示每步难度。证据来自原标注或检索后扩到段落/表格，3次仅证据作答通过，不等最小必要证据；answer-conditioned图只是候选推导，不是模型内部CoT。
- 6550英语32k–256k实例/17源，4模型每题3答；fractional-logit控制任务/模型等，question-cluster CI和Holm检验。scope对Gemini局部反向；length×depth交互不确定；三轴叠加极难格探索性、SciTrek占62%，移除后depth差额大降。两图annotator depth仅65.6%相同、ρ=.48，40例人工审计不构成全部ground truth。没有操纵context的因果实验，不写难度普适定律。
- 实际owner：Ch22 99–103 Effective utilization已有长度≠使用、单检索≠组合；130–136已有位置/干扰/长度任务切片，但没有必要证据量与分布、并行工作量和顺序依赖depth的独立测量。建议最小PRE接该评价列表：固定长度后，另报支持证据占比、证据间非证据分布及依赖图最长链；多次并行查找不等更深推理，自动证据/图须保来源与误差。它们是受标注/任务人口约束的关联诊断，不能单凭proxy决定压缩、检索或模型替换；标注不可靠时保留现有人工支持跨度与配对长度/位置对照。

### 2610.22127 Explaining the Roles of Experts in MoE LLMs for Personalization

- 原件：https://arxiv.org/html/2610.22127v1 。题摘准入链：routing频率不能认证专家语义→配对adapted/base crosscoder提出personalization latents，再映射expert并干预→需要把适配差额、相关路由与输出作用分开。建议2+1+2=5。已读§3–6.5全部核心、Limitations。
- 先只训router，再冻结router只训每层最常选k个experts；crosscoder配对重构base/adapted activations，以两decoder norm差阈值提latent，取高激活序列中触发/未触发token的routing frequency差提expert。N与top-k按distinctiveness/stability grid选择；后以base激活+adapted latent作hybrid patch，并对base的候选expert gate作按logit std缩放的soft bias，比较next-token KL与随机/共享latent控制。
- 3个开放MoE；Multifaceted是GPT4-Turbo产生的group-level system preferences，不是实际用户长期persona。LaMP/LongLaMP transfer较弱；dense按active/total参数匹配但预训练不同。最佳layer×expert以test分数挑选（原文所谓mitigation仍使用test），不能当独立heldout选择；crosscoder FVE .65–.80、阈值/单层/残差盲区；大多数Qwen/OLMoE latent在system message触发。KL变近说明有限计算干预，不证明唯一语义expert、真实偏好满足或必要性；Mixtral相对active-matched dense的disentanglement有反侧。构建、grid、双模型前向、解释/scorer与干预回归均付费，active参数少不等端到端便宜。
- 实际owner：Ch21 77–79已有reference频率差提soft-bias且非语义/因果，142–144已有频率≠输出重要性及logit扰动；缺配对适配差额到expert提案的诊断支路。最小PRE：配对base/adapted激活可先由共同字典提出适配特有方向，再用方向触发时的路由频率差提出expert集合；其语义名仍是解释假说。匹配latent patch/随机控制与gate小幅干预只检验指定模型/输入/层的局部作用，须保选择人口、重构误差和独立任务/负载回归；不能用更可解码或KL更近宣布单一persona owner。

### 2610.21553 Writability and the Pathway

- 原件：https://arxiv.org/html/2610.21553v1 。题摘准入链：可枚举的地址让局部写入看似数据库→row-only/row+shared projection×residual anchoring的共享起点2×2与未写实体控制→写位置、训练表达、新问法和行为保留须分别验收。建议2+2+2=6。已读§3–6主方法/评价和§8限制；生产模型旁证只采用其已明确的有限权限，不作方法排名或实现事实。
- frozen GPT2新挂两层2/3gram polynomial表；row mask只限制embedding gradient，原实现仍为全表dense参数/gradient/Adam moments，不是稀疏optimizer内存。shared K/V的readout及context gate让未写地址也可改变；OAW约束mounted pre-write的module residual，不是native GPT2或output-KL。50 synthetic facts，2500steps，3seed只变采样，同一初始化/数据；全句LM loss而非仅answer，OAW额外anchor forward，非等compute。
- 所有臂训练completion100%；新问法strict EM/prefix均0但词面命中随shared projection增加，不能把0EM当所有语义转移全失败，也不能把substring当正确实体检索。相同relation的未写实体会intrude；heldout synthetic controls不代表遗忘已知真实事实。OAW降固定WikiText slices的KL/PPL漂移，同时部分question NLL/词面命中变差；不升级为普适semantic tradeoff。生产Qwen/DeepSeek主体首token promotions与少量保存continuations不证明整答案、事实真值或SPSA必要性，§8明确未隔离pathway width/scale/预训练强度。
- 实际owner：Ch16 198–200已有静态地址candidate、动态gate/shared projection及表/optimizer费用，277已有direct recall≠组合和locality/fluency。最小新差额是后挂addressed memory的写权限与shared readout分责；建议在静态candidate段后最小PRE：行局部不保证行为局部，地址复用和shared projection仍传播更新；扩大到projection是另一写权限，residual anchoring只保护指定mounted reference切片。训练prefix、新问法、未写实体/其他relation与最终分布应分别验，保存完整continuation；词面/首token命中不授知识写入成功。额外anchor与dense optimizer state计费，语义转移/保留不通过时保留原checkpoint或可追溯外部记忆。

### 2610.22099 TIPS

- 原件：https://arxiv.org/html/2610.22099v1 。题摘准入链：冻结dLLM的单调unmask不能撤回错误上下文→小policy同时决定下步visible集合且固定schedule只控制期望占比→内容预测、位置偏好、进度和对外commit需分责。建议2+2+2=6。已读§2–4.4、§6限制、B.2.1–2.3/B.2.7与B.4.2直接反侧，有限必要证据即停。
- 2层约600k DiT仅看active-token logodds/相对最佳alternative比值、mask与time；已visible时active是当前token而非新argmax。Bernoulli next-visibility可remask，scalar logit shift求期望visible fraction，不保证实际count单调。固定T即便allvisible仍继续，末轮确定填剩余mask；不是纠错内容oracle或adaptive stopping。warmup用reference utilities，RL只训policy对visibility联合likelihood，不需decoder梯度/序列likelihood。
- LLaDA8B、256response，GSM/MATH训练，1819题micro test；3训练seed×3inference draw。不同baseline的block几何、固定NFE/mean target/cap口径不同，不能把横轴直接说等FLOP/墙钟。去remask及重训monotone控制均有差额，但消融1seed，warmup+RL共同重要；免费进度会出现finalization deferral。coding transfer不稳定，T64原Fast-dLLM更好；接续heuristic可不胜重启。主结果不是长生成/吞吐/SLO保证；额外controller、校准、数据/rollout训练和放弃early-stop均付费。
- 实际owner：Ch24 650–662已有frozen predictor的where-to-unmask/离线gold rank，697–725已有revision、soft-state联合训练和冻结correction head。缺当前token信心而非新proposal信心、可撤回visibility与独立occupancy控制的组合。最小PRE接learned planner后：冻结内容模型时也可训练可撤回visibility policy；已可见位置必须测当前token支持，不能把argmax信心错配给旧token。位置偏好与期望进度分开，避免把所有决定拖到末步；保留重训monotone与实际消费预算对照。额外policy/校准和等待修订有代价，fixed horizon不授提前流式commit，迁移不稳时回原confidence/保守unmask。

### 2610.21979 P2TPO

- 原件：https://arxiv.org/html/2610.21979v1 。题摘准入链：页面总分会抵消不同元素的相反质量、同质低分组无相对信号→按reference instance对齐、补missing/ceiling-gap、保块信用总量向span分配→element身份、反馈构造和credit消费不能混成一个“细粒度reward”。建议2+2+2=6。已读§2完整式1–4、§4主设置/消融与直接反侧、§5理论适用条件、§6限制、B.2机制、C.1.1/C.1.3与C.7费用，不遍历全附件。
- 对齐保reading order与instance身份；missing计0，同质不完美分数用负ceiling-gap，省略块信用走现有boundary token代理，不经过SCR。matched高质量且type匹配块中，负credit指error、正credit指correct；cap-and-rebate使非负权重均值1，保的是该块signed/absolute coefficient mass，不是全部policy gradient或因果信用无偏。固定additive utility下聚合不可逆，不证明实际异质reward全面最优。
- Qwen3.5-2B/700k SFT共同起点，100 RL updates/128pages/G8，5训练seeds；六bench13splits中若干复用OmniDoc源页，不当13独立人口。Full优于response baselines均值不等全部component最好：Scanning/DocPT等有组件更高；SCR独用仅2/13改善，加UAP后11/13。保coefficient与选中count的random/shift对照支持位置有用，但reference/serialization/重复文本会误对齐，region内token权重仍相同，不是真实逐token因果。
- 费用/权限：BF16 veRL/Megatron+vLLM，硬件只披露8张high-performance cards，具体型号Not Disclosed；C.7信用构造1.215s vs .707s及约.19%总step占比是不同分母，非总训练只增.51s；60GPUh不含全部SFT/制备。annotation quality筛选、对齐、评分、生成及actor全部计费。图/代码非独立类型；省略位置代理不精确时会误惩边界。
- 实际owner：Ch33 277–285已有sequence advantage广播，345段已有按advantage正负选择supported/unsupported span但不保总质量；尚缺reference实例组、missing无span的消费路径与保块mass重分配。最小PRE：有可信结构reference时，先按元素身份跨rollout比较，避免同类不同块相互抵消；missing和同质低分需显式反馈，不能因为无span就丢掉。已匹配块可按credit正负集中到正确/错误span，但需保预算并把省略代理单列；对齐不是真因果，reference/序列化失配时回原sequence advantage或可靠process监督，不能由局部对齐分自动签正确性。

五项均完成有限Source与具体owner比较；未因数量或同主题关闭。此层不修改任何Books，交root独立取舍。原14项和机构笔记仍保持有效。

### 后续单独授权的六家族 Books 窄写（非上述五项写入）

root明确说明已独核原14项Source/PRE，并仅授权22300/22169→Ch5，22071/22100→Ch11，22355→Ch31，22065→Ch49。本执行者随后按该授权各保存一自然段及本人Review note，旧文未清理；已实际顺读新增正文、完整直接两侧与本人源注，并逐文件检查diff-check无诊断。六个`SF-2026-ARXIV-2610-<id>`marker为本轮定位。未自行授非作者POST或DAY，等待root独立检查；Report/README/LS/index未改，无stage/commit/push。此前“未修改Books”只描述当时尚未获窄写授权的阶段，不撤销已有来源判断。

## 同日定点 CV 七项 Source（接 REVIEW R8，不扩发现）

只处理root指定22328/22321/22311/22282/22276/22267/22264。复用REVIEW R8的完整题摘、官方CV Fri16首50身份/唯一v1与无可见撤回信号层，精确审阅以下v1；HTML头的Thu15 submission不改名公开日。本层只给Source与具体owner PRE/NC建议，不写这七项Books；不预签root独核、POST或DAY。

### 2610.22328 ACEdit：6分，最小 PRE，MULTIMODAL-GENERATIVE-PARADIGMS

- 原件：https://arxiv.org/html/2610.22328v1 。已读§3–6，核心式1–2、主表与条件/rollout消融。约束链：多轮自产图暴露drift却使固定配对target失配→student读自身前态+当前指令，teacher与aux都读原图+累积指令→训练暴露人口与监督条件锚不必相同。二者仍对同一加噪student输出求score差，不是teacher不接触student state；不需要逐轮成对目标图。
- 4步FLUX.2-klein9B、rank16 LoRA、10轮rollout；前轮不保梯度，当前轮随机exit step之前步骤也no-grad，只反传该exit预测，不是整链BPTT。aux另作flow-matching适配student分布。96合成图/960局部指令，100student更新、4.4B200 GPUh；冻结teacher前向、aux更新与自产rollout均计费。
- EdiVal-10为252真实图链；完整图VLM/anchor-DINO/背景LPIPS和编辑执行分开。相同100更新的关键消融：teacher/aux加前态后consistency3.85→2.81、以其替换原图+累积指令→2.28；student加原图提升保留却使编辑分3.38→2.80，可能撤销旧编辑。成对链2SE不等训练seed区间，其他方法step/分辨率不同；不是全指标最佳。困难指令仍删除前轮眼镜、局部保留任务和长于训练的极长链不授普遍稳定，替换整个场景本来就可少drift。
- 实际owner：Ch24 1000–1015已说明student访问状态、同noisy state不同目标及对象teacher条件资格；113–125还有自产视频历史训练。它们没有“student污染前态、teacher/aux原图+累积指令”的分责及保真/保留旧编辑的冲突，故不是仅主题已有覆盖。
- 最小拟文：递归编辑的训练可让student消费自身前态，却使监督路径保持原图与累积编辑条件；同一noisy后态上的score目标不要求两侧拥有同一历史。清洁锚能降低累积伪影，却不能无条件交给student，否则可能恢复旧图、撤销已完成编辑；需把背景保留、当前指令和前轮编辑分别验收。teacher/aux、自轨迹与累积条件构造付费，困难或更长链失效时保留短链、重新锚定或独立局部验证，不授所有递归任务稳定性。

### 2610.22321 AVC-Reward：5分，最小 PRE，PLATFORM-EVALUATION-SYSTEM

- 原件：https://arxiv.org/html/2610.22321v1 。已读§2–5.5、AppB.1–2核心制备、D.1–4与E直接案例。准入不依赖新榜单：§3先区分speech/music/环境事件，再A→V/V→A核每份存在、时间与属性关系；off-screen声源未显示不自动算错、合理静默不强制配音。whole-clip语义相似不能单独认证每个局部声画关系，这是提出event/relation测量单位的具体增量。
- 706样本含50源片段构造的119 negatives：局部事件删除、±2s shift、在音频峰freeze视频、音色编辑等；E中双人仅一人有语音、演奏结束后音乐仍持续、打击声延迟及有效合唱转场，给出不只是整体题材不匹配的具体失效人口。D.4三输出对相应issue-label分类有分项置换差额；但没有“同模型同训练只移除event decomposition”的匹配消融，不能把所有相关/训练提升归因于分解或宣布所有whole-clip metric失效。
- Qwen3-Omni-Thinking全SFT8k结构数据，再10k human-calibrated GRPO；五阶段是记录/验证链，不是已核信号分离网络或真实因果图。706样本三独立annotator与训练annotator不重叠；human reference跨整bench归一、PLCC另作5参数映射，pairwise样本对不独立，不把大pair数当独立clip数。SRCC仅.244、与SFT-only相同且低于macro-only.251；自动分数不是普遍人类真值。generation RL调整权重/学习率，text alignment有反退，不是仅替换reward的单因果控制。
- 实际owner：Ch66 308–310已拥有事件/主体/时间/视图身份及错误distractor；4810已有配对物理factor响应不等同步。尚未承载声画关系的“是否应该对应”资格，不能用一般分项测量直接NC。独立解析、timestamp/属性、双向验证、模型链、annotation及校准均计费，背景音乐/离屏关系本身不能机械惩罚。
- 最小拟文：音视频一致性可先以事件和关系为单位：分别找声/画事件，先判断它们是否本来需要对应，再检查时间和属性；全片题材相符不能覆盖局部缺声、误时与动作停止后仍发声。离屏声源与合理静默须按关系资格处理，保留macro/temporal/attribute分项及原片段证据。自动event解析和judge不是真值，需独立标注与配对负例；资格不明时保Unknown/人工，不让一个平均分批准所有声画一致性。

### 2610.22311 Velox：6分，最小 PRE，MULTIMODAL-WORLD-MODELS

- 原件：https://arxiv.org/html/2610.22311v1 。已读§3完整式4–17、§4.1–4.4主评价、A.1和B.1–3中坐标/缓存资格。按固定KV block保存camera rectangle+robust depth slab；当前query通过recent-first可靠multiwarp取depth，以coverage gate决定几何是否有资格。有效覆盖处的OBB overlap只乘性boost逐层pooled-QK importance，未覆盖保model-only cumulative-mass route，不是直接dense或硬删除全部无重叠块。
- previous chunk在80/150 route预算内保留，Gilbert邻居/参考块在预算外补入；global block坐标同时给几何与Triton indexed sparse kernel消费。geometry与denoise同一H200异步，通常落后两chunk；pose bridge/历史相机刷新和ring depth cache也必须兼容。KV历史仍保留，pooled importance与route构建仍读历史，不能从bounded attention tile term推常数总内存/总执行。
- 48chunk单H200 trace的attention约34.2→7.8ms、denoise7.19→2.96s，不是完整交互SLO。158 WBench navigation matched三行同cases/同Gemini，API-free73.66 dense/73.11 model-only/73.51Velox；几何相对matched sparse有局部差额，但dense的多项仍更好，.15总体接近不证明逐项无损。外部published行用Doubao不可混judge排名；单配置/定性案例不授任意动态世界。重建、静态mask、坐标误差、陈旧geometry或disocclusion都限制coverage；无formal安全保证或独立复现。
- 实际owner：Ch25 800–808已有per-target FOV与motion-aware QK取历史、强制近邻及几何非新观测；缺“geometry trust先于score、逐层soft fusion、unknown回model route、同block落kernel”的具体接口。建议仅补该局部，不重写Ch49attention硬件常识。
- 最小拟文：相机几何可作有资格的历史路由先验，而不是硬可见性证书；将可靠深度/覆盖与overlap分开，覆盖足够才soft重权每层自己的关联，缺失处保模型route与近邻保障。几何状态、pose bridge、新鲜度和KV block坐标共同绑定，路由粒度须实际减少kernel tiles。重建/校准、保留历史和路由构建都付费；异步陈旧、动态物体或质量回归时放宽预算、回原model/dense历史或真实观测校正，不由局部denoise加速授无限memory与控制安全。

### 2610.22282 Routing Policy Optimization：6分，最小 PRE，TRAIN-GRPO

- 原件：https://arxiv.org/html/2610.22282v1 。已读§3–6/式1–8、D对照差异与E估计器/失败。保原确定sampler，在少数early levels以原attention mass提出block routes；Gumbel多选+own-block safety、随机dense anchor layers，非全链随机化。配对同prompt/初噪声/非route随机量，只换route seed；离散route不由新policy head学习，但proposal仍随generator改变。
- replay在每份实际访问latent重算dense velocity，以围dense的Gaussian deviation log-likelihood surrogate向较高reward routed transition靠近；不是反传离散route概率。作者明示非Gaussian、遗漏route likelihood和后链pathwise、每batch重估width，不能授无偏REINFORCE、准确transition density或原sampler分布保持。test去mask/用原sampler是接口保持，不是权重或生成分布不变。
- SD3.5-Medium LoRA32/512²/10步/无CFG，50updates比较只有一个训练seed；后端base训练reward不同，必须看shared64prompt/28step dense validation，不能用routed-vs-SDE training reward直接排名。Wan2.2-TI2V5B/13frames/704×1280/10step/CFG5，6220视频VBench；24.1H100 GPUh对75.4/102.3不compute-matched，overall差小且color/style反退。E明确dense-gain fade：routed reward持续涨时dense收益可先峰后降；reward hacking仍开放。dense scoring、paired rollouts、replay、decoder/reward均付费。
- 实际owner：Ch33 412–438已有内部denoising credit、非真实latent likelihood、pivot噪声候选+部署保sampler。没有“临时attention route作探索、Gaussian dense-velocity重放且须单验dense transfer”的支路；Ch24仅保留生成状态/solver责任，不重复RL推导。
- 最小拟文：确定性生成器的训练探索可暂放在内部attention可见性，而不永久改变测试sampler；同内容种子的route配对减少随机混杂，重放再把结果偏好投到dense预测。但离散route造成的偏移若以Gaussian拟似然消费，必须明确它是surrogate，不能借score-function符号自授无偏信用。训练routed reward和实际dense质量分验，保原sampler不保原分布；route/anchor、width、replay与全部rollout费用共同绑定，dense收益衰减或独立质量回归时早停、回原checkpoint/已验SDE训练。

### 2610.22276 MJev-Spatial：6分，最小 PRE，MODEL-DECODER-ONLY

- 原件：https://arxiv.org/html/2610.22276v1 。完整题摘及§3.1–3.3、§4主评价/关键消融、E.1–2读出反侧已读。约束链：有限选项/数值/点输出为AR文字与parser付费→候选内容经原主干contextualize，用最后attention预训练Q/K给Decide/option-end评分→输出消费者可用声明的候选空间而非必生成answer tokens。这里复用投影，不是零训练：所有保留语言参数全量微调，视觉encoder/merger冻结，移除最后层未用V/O/gate/FFN路径。
- 一个classification decision一forward，不是所有任务一步：数值1–2、点3stage且重编码两次原图crop，多点tree最多91节点再prune。单位、codebook/overflow、option permutation及原图坐标共同定义身份。正确格子时的量化误差界不保预测；上层选错可排除真区域。训练teacher-force全stage一pass，causal序列使早决策不可见后续GT/crop，推理仍串行按自己的选择展开，非免费消除依赖。
- 12.3M-QA主模型平均排名不独归readout。72K/2.2Kupdates同optimizer/token预算的nativeQK、linear/KEV控制无全胜：RefSpatial/length较好，Where2Place/pointing别头更好；E.1说明表示取点/保留计算/模板也不同。E.2是历史pilot非最终release，MMSI27.7<AR34.2、counting38.78<66.84。crop去掉与重新训练无crop是不同控制，更多细bins反而加预测误差。12benchmark均值160.6ms/B200/batch1不授真实interaction SLO；global batching短程提速无quality/convergence验收。所有适配、候选context、crop/编码与tree扩展付费。
- 实际owner：Ch18 153–169已有词表投影与替代scalar readout，196–218已有统一NTP的收益/串行代价；缺复用原attention matching作为候选内容读出、并将有限数值/点解释交给外部controller。Ch23开篇表示/坐标合同是依赖，不重复建通用预测owner。
- 最小拟文：消费空间已有限时，可让decoder的contextual候选表示直接进入分类读出，而不是先生成文字再parse；读出可复用预训练matching投影，不必另添随机head，但仍需任务训练与匹配控制。数值/区域以声明codebook逐级细化时，候选、单位、溢出和坐标归controller，早层错误与crop成本不能隐藏；训练全stage teacher forcing并行不使部署选择并行。开放回答、范围不完整或任务回归时，保原AR、显式head或可靠parser，不从少token签通用空间/行动安全。

### 2610.22267 DetNO：5分，最小 PRE，MULTIMODAL-GENERATIVE-PARADIGMS

- 原件：https://arxiv.org/html/2610.22267v1 。已读§3–5.2/式1–11、Alg1、T1–4，AppA.6–8直接bandwidth/费用/stop-gradient控制。继承CNO的initial-noise搜索，在t=T的one-step Tweedie预测上avg-pool+normalize，以固定reference median bandwidth的RBF Gram作`−logdet(S+epsilon I)`，full-resolution预测到原reference的距离作软fidelity罚，之后原sampler生成。UNet输出stop-gradient，梯度不穿UNet Jacobian，非完整生成reward反传。
- 新差额是set-level聚合对kernel谱冗余的权重，不是pairwise距离缺少全部几何信息：完整成对距离本来决定RBF Gram；logdet经chain rule仍是全局系数加权的pairwise方向，不能采用“逃出pairwise方向span”的泛化说法。Proposition1只在Gram空间比较梯度范数，不保证latent/语义有效维度或真实mode恢复。RBF RKHS体积也不是raw图像空间的维度，fidelity软罚非hard可行性或高密度证书。
- SD1.5/XL/3、2000COCO prompts、同seed/CFG/hardware，B=5或3；主表diversity较好但SDXL/SD1.5的precision/density/部分quality反退。T3固定kernel/fidelity/optimizer只改aggregator，pairwise-RBF→logdet的Vendi4.8006→4.8024，1shot两数据各+.5pp；大部分相对InfoNCE增量来自共用kernel/fidelity，不能全归determinant。大B比较CNO仍混这些因素；10splits是分类切分非独立生成训练。A.6将“小sigma使off-diagonal→1”的文字与式4相反，此解释不采用；不因此丢弃可复查目标定义和局部对照。
- SD3/1024²/B5/28NFE作者cost表17.8s vs base16.3s/28.3GB，4额外forward；硬件型号/precision未在该表披露，不授一般端到端速率。matrix分解O(B³)、denoiser/anchor、全部候选和λ/window校准计费。实际owner：Ch24 450–456已有DPP/一致性方向与内部condition干预，1854起有prior guidance分责，但没有initial-noise上的核谱聚合与full-res锚分责，故最小PRE而非按“都有DPP”NC。
- 最小拟文：联合输出的多样性目标可从pairwise相似度之和改为kernel Gram的谱/体积聚合，在初始噪声的clean预测代理上惩罚集合冗余，并另用原预测锚限制漂移。它重新分配同一批成对关系的梯度，不创造几何真值或保证稀有mode；kernel、pooling、bandwidth和软罚均改变实际目标。额外候选/前向、矩阵分解和校准付费，较高集合多样性仍须独立验质量与用途；proxy/质量失配时回IID、温和排斥或更多真实数据，不将软锚授为分布保持。

### 2610.22264 SCOPE：5分，最小 PRE，TRAIN-GRPO

- 原件：https://arxiv.org/html/2610.22264v1 。已读§3完整式1–12、§4.1–4.3主评价/消融、App1.2–1.4/1.6–1.9必要配置。冻结renderer，Qwen3-8B同时产rewrite及语义span；tokenizer offsets映射实际loss tokens。每completion仍仅一signed advantage，不增加span reward或独立correctness标签。
- 对同sample的current−old token logprob在span内均值，exp(beta·mean)先clip[.8,1.2]，再按span token数加权均值归一到1并detach，统一乘span内token的原advantage；wrapper/separator仍原权重。归一后单个weight不再保证落[.8,1.2]，保的是answer-content平均coefficient而非policy gradient、无偏因果信用或严格trust region。β0回GRPO，首步current=old为全1，后续才分化；格式/截断/offset失配回uniform，额外一个EOS占位零权重。
- 同renderer配置/奖励/训练设置GRPO为主控制，QwenImage/SD3/FLUX固定512²、20/28steps、各自CFG；GenEval4、CompBench10image seeds，训练组共享renderer seed但test新seeds。semantic vs随机/固定3token partition、token独立shift与format-only控制支持受限结构归纳偏置，不证明作者“subword高方差”唯一因果。训练seed重复/CI未披露，QwenImage color比GRPO低.01；部分RePrompt用published不同来源，不能当完全matched重现。
- 原prompt另作第8member只供baseline、不接受更新；低baseline减原prompt分，高baseline用组标准化，这是另一个目标差异，不能与span单独混归。原文§3.3称增加old-forward、App1.7称复用已有current/old logprobs：这里只采用需取得兼容两份概率，不授零forward。H200但node数不确定；全rollout、render/reward、rewrite、概率与训练均计费，无新render只指modulation增量。
- 实际owner：Ch33 277–291已有sequence advantage广播/保总量的局部程序span、345已有evidence-supported正负重权；400–404又有查询coalition归因。这些均没有“无span truth、policy shift按semantic unit池化”的权重来源。最小PRE：没有逐span真值时，语义分区可只作为更新的结构先验，以同span内policy变化池化后重权共享advantage；它不生成新的正确性标签，平均系数保持也不保证梯度或因果信用守恒。分区/offset、old policy、归一与fallback应保存，概率/格式/生成费用仍计；边界不可信或独立结果回退时保uniform GRPO、可靠过程监督，不从更完整phrase签发内容正确。

七项有限Source及实际owner比较均已准备，本层不写任何CV七项Books、不自授Source独核通过。此前六family已获root实际正文/完整两侧/本人注POST PASS，依明确行政授权仅把六条Review notes状态同步为实际通过；机制正文未因本行政同步改写。未stage/commit/push，不扩发现或开启新日。

## root后续具名授权的 Books 写入层

Source/PRE后root另授三family：21553→Ch16、22127→Ch21、22067→Ch22；随后明确已独核CV7、REVIEW R9和ORG_B S23/S32，另授22276→Ch18，22264/21979/22282→Ch33，22060/22267/22099/22238/22328/22370/22347/22369→Ch24。本人仅按这些具名窄位各保存一自然段+来源note，无孤立新增标题，保旧段/源注及并发改动；未写Velox/AVC或其他Books。

已实际顺读新正文、完整直接两侧及本人notes，并作限定Markdown/diff-check（无诊断）。Ch24 ACEdit同时将费用用语明确为“冻结teacher前向、aux更新”，不是teacher被更新；随机exit之前no-grad也已精准回写本层Source，未改变准入或score结论。以上新增15family仅为作者写后自读，非作者POST仍待root，不能据本层授DAY；先前六family的root实际POST PASS不受影响。本日具名Source与授权写入到此停止，不扩发现/日期，不stage/commit/push。

## 非writer实际 POST：ORG_B八家族与root四家族

复核者：live1017_org_a（这12项非writer）；结论：12项实际POST通过。仅本日10-17/窗口10-16，已重读当前AGENTS、研究/Report合同与Prompt、来源使用/每日组及owner路由；复用未变化的Source/PRE独核，不再发现、不无差别复读原件。实际读取以下保存正文、完整直接两侧及本轮来源note，再与ORG_B S16–18/S22/S24/S29–30/S33、REVIEW R9.1/R9.5/R9.7和ORG_A Velox有效层核对。本人刚写的15项不属于本层验收。

| 家族 | 实际保存位置 | POST所核采用与边界 |
| --- | --- | --- |
| 21456 TITAN | Ch30正文127；注898 | 关联probe后增加subspace干预提名组件；SAE解释非实际更新单位、非targeted模型knockout减循环、各语对重发现与TER/全发现训练费均保留，接后续LR公平比较自然。 |
| 22236 Training-Free OPD | Ch30正文707；注900 | ACT-Mat真实二阶矩后新增teacher-rollout统计人口；loop tokenmass、correct-filter反侧、fixed-input非整网保真、精度与全费用身份明确，没有借题名宣称任意模型免训练蒸馏。 |
| 21763 Audio Bias | Ch23正文65；注1772 | 位于群体probe诊断与speaker-change之间；chance可由常标签/拒答组成，多consumer/知觉/关联分验，二元英文与distillation/utility反侧近文，无删除/公平性保证。 |
| 21937 Flow-CLIP | Ch23正文169；注1770 | SAGA后/另head读出前，signed同patchset支持增量与samecaption跨图margin分责；切面只在W前、旧gold保留非新图truth、global/迁移consumer反退及token×patch全费未丢。 |
| 22356 DK-VLM | Ch23正文1423；注1768 | 原query-view编码后/混合rig前；native位置/causal保留、valid视觉full-attention另支路、gate非零/联合目标与训练费用、一般能力反退完整，未授全序列因果取消。 |
| 22371 Gen4P | Ch23正文1750；注1766 | 可复用perceiver后新增生成prior的感知consumer；clean latent非预测未来、相对clip时间、非微小LoRA/深度prior历史费用与局部反退充分，未流入World Model控制权限。 |
| 22075 Recurrent Retrofit | Ch17正文598；注829 | parameter/execution depth后接预训练VLM恢复路径；56/22执行与2.55×KV、per-pass身份、训练外depth崩溃、sampled非单调scaling、阶段数据/监督混杂及全费保留，接continuous-thought不同状态轴清楚。 |
| 22200 OpenGCUA | Ch78正文71–73；注834 | 连续gesture后、Proposal权限前；program跨GUI/shell消费中间值不等首次batch，capture/delivery不混，todo非外证、handle/reset/权限与全轨迹费用近文，无真实设备/SLO泛化。 |
| 21995 UWE | Ch5正文38–39；注619 | 神经元置换例之后、distributed representation之前；supported-op坐标接口/等变和不变摘要、sound非完整函数对称、unsupported拒与metamodel资源反侧明确，不把weight摘要授为语义地址。 |
| 22343 GeoState | Ch25正文305–306；合注1533 | VGGT-World后新增view-decoupled scene query；camera-matched CopyLast、重建非可预测、rollout target污染、观测LiDAR尺度与有效overlap、全训练/前端费用保留，未授action因果。 |
| 22311 Velox | Ch25正文813–814；合注1533 | FOV/QK历史局部后新增geometry资格先于score的soft route；unknown保model route，indexed tiles和旧KV/pooled score仍在、异步/动态/遮挡反侧及总费明确，未签常数总内存/SLO/控制安全。 |
| 22312 Grid-Bench | Ch25正文959–960；合注1533 | planning admission入口拆完整state EM、valid coverage、错误extent及初终保留/更新，same-valid配Copy/Zero；非never-changed、独立prefix非持续修复、full denominator/费用与symbolic边界保留。 |

本次未发现必须修正文义的问题；无需为制造diff改写旧文。上述六个目标文件限定diff-check无诊断，Markdown链接均指原精确v1或本日有效记录；没有用机械检查替代语义POST。各writer可仅行政把本人note的待POST同步为本层既成通过，再读回；本reviewer未改任何Books正文或notes。以上仅12项写后通过，不授整日DAY/FINAL、实现复现或全来源无遗漏。

### 后续唯一 LangDiT 写入（writer，非上述 POST 对象）

完成上述12项非writer POST后，root明确单授22330 LangDiT在Ch24 LangFlow两段之后补一段+本人note，采用REVIEW R11.5已由root独核的最小PRE。已保存于正文524/注3077并实际顺读LangFlow两段、新段、完整DoubleCat相邻段及本人note，限定diff-check无诊断。仅前向shortcut/显式codebook梯度路由/训练SC辅助与部署未加权mean分责，保noisy-input学习、单seed累加消融与bootstrap/conditioning全费；未采用Plaid异进度排名，未复核全部原件或复现。作者自读不是POST，仍待root实际写后独核；未扩其他材料或日期，不授DAY。

### 本人16项 notes 仅行政同步 root 实际POST既成通过

root随后明确告知：已实际读取后15项正文/完整两侧及15本人注，并完整读取LangDiT正文、LangFlow/DoubleCat两侧和本人注，16项非作者POST通过，无新增问题。本执行者仅据此将Ch16 21553、Ch21 22127、Ch22 22067、Ch18 22276、Ch33 22264/21979/22282、Ch24 22060/22267/22099/22328/22238/22370/22347/22369/22330共16条本人的Review note，从待root改为root实际正文/完整直接两侧/本人注POST通过。未改任何机制、分数、边界或旧注，未把作者自读冒充独立复核；前文待POST是当时保存阶段，当前以本既成同步层为准。

已逐条读回16条实际保存状态、检查限定diff-check无诊断。不授DAY/FINAL，待README现45项归并及root追加DC8后的完整六部分独立复核；不扩来源/日期，不stage/commit/push。

## 最终 DAY：89 家族六部分独立复核通过

复核者：`live1017_org_a`。检查时间：2026-10-17 10:37～10:39 +08:00。本执行者从未撰写或修改本日README；root与reader是报告共同作者，reader后来取得的归并作者身份不倒退其此前实际非writer Source/POST。本人是部分Source及Books作者，不自签这些层；复用root已发生的独立核验。本层实际完整读[当前README](../../17/README.md)六部分、89个候选整行及89个证据段，重读当前AGENTS、研究/Report合同、Prompt、来源使用/每日组/arXiv主题和ROADMAP适用路由，完整消费本日REVIEW R1–13、ORG_B S0–47、ROOT收尾/发现/必要Source层及本人既成记录。结论：**DAY通过**，仅本日10-17/北京时间10-16自然日；不包含保存完成态的FINAL，不扩大来源、日期或历史任务。

### 来源、日期与候选集合

14个每日来源均有行，实际入口/主题/停止点可回到A/B/ROOT；Hunyuan的动态空壳由同源publicList实际11/11恢复，Qwen中英各40条与重复page2没有误记为有效分页。Google年份乱序Pubs、Meta失败/乱序目录、Qwen空壳身份及MiMo部分无日期条目继续为受阻终态，不证明零发布。arXiv只采用CL首50/177、LG相关前40/306、CV首50中的26个主题题摘、AI首12中的10项及DC已见8项模型/运行时/编译线索；未翻的分类尾页、其他分类与旧pastweek/new/AR缓存不是逐项关闭队列或本窗日期原证。12分类主题API两次超时、四限定官方域搜索空结果及OS/PF/PL/RO/IR/MA未恢复日期列表构成明确覆盖限制；README正确把SRC-ARXIV标受阻，不能将已处理切片扩称全学科召回。已穷尽本次有限路径的外部隔离不遮盖普通待办，也不要求为证明全球无遗漏继续搜索。

88个arXiv家族的公开日采用本日官方Fri16分组与精确ID/唯一v1联合依据，不由Oct14/15 submitted改名。此前CL/LG/CV/AI的实际逐项日期/current层按身份未变化复用；本轮又定点打开[DC recent首屏](https://arxiv.org/list/cs.DC/recent?show=50&skip=0)，实际Fri16的16条段中八个DC身份均可见，停止该日段，不消费Thu15及以后返回的旧标题。四个B作者新增项abs现仍各仅v1、未见撤回/纠错：22035/21815/21640提交Oct15，20981提交Oct14，均不与该公告日混用；其余四项沿B已独立核root的有效版本/日期层。没有具名更早公开或实质修订信号需重开。Kimi公开仓库两commit/merged_at在窗内；两个事件只计同一项目家族，guard事件不因仅报告而漏审安全/兼容边界，两个事件分数也未重复计家族。

实际逐行比较具体贡献、三维分数、审阅深度与最终处置：原36＋后45＋DC8＝89，77整合＋10具体已有覆盖＋FDE仅报告1＋RBCD争议1，整合落29个唯一owner。没有用owner映射、机构名、榜单或附件数量代替贡献，也没有因NC/Only/争议缩候选池。5/6分项的深入采用限实际必要命题；Remote KV 7分只到成本门与collective连续前缀，未虚授未读bug/kernel/全部吞吐；RBCD保持5分争议，不降分隐藏中心反例。FDE最终仅报告覆盖benchmark业务anchors/专家成本模型，未执行历史PRE或硬称已有同一算分公式。10个NC均指实际owner所承载命题，报告仍保新增受限验证/反侧；Meta NC已再次对照Ch49实际662–704的descriptor/catalog、物理后果、重校准及fallback，不是泛称同为cost model。

### DC 四项本轮必要原件独核（并入DAY，不另建重复层）

本人对ORG_B作者S38–41独立打开精确v1，完整题摘后实际核下列必要方法、评价及直接反侧；不是只接受S47 marker或下载成功。四项Source及最小采用通过，均未核实现、复现、全附件或旧版。

| 身份 / 本轮实际范围 | 独立核验与实际owner采用 |
| --- | --- |
| [22035 ETH v1](https://arxiv.org/html/2610.22035v1)：§3–4、§6–8必要配置/评价/反侧，§5仅正文四优化身份及评价反侧 | 三阶段局部优化/greedy local-batch/再refine是heuristic；partition/exchange-combine/fuse以参数坐标和DP组对齐，不是异形buffer直接AllReduce。Eq3确为ΣLbs≥GBS，未闭样本权重/overshoot，不采用exact原SGD。TypeSplit有2/5匹配、重算单项1.8–5.7%、α.5更快搜索却更慢运行及短2000步trainloss反侧均在。实际完整读Ch38新276及246–298邻接：新旋钮/统计合同与旧StageBalance/HAPMoE共存，采用未越界。 |
| [21815 Exact Makespan v1](https://arxiv.org/html/2610.21815v1)：§2–5的recurrence/定理/必要proof、§7.1–2及§9–10必要直接边界 | Στ fill与maxτ steady在固定服务、无限buffer、纯forward模型成立；其async递推没有独立link吞吐排队资源，NCCL另stream不充分。160k是recurrence求值点；8571 gateway单请求日志拼stage、queue≥0不能验证物理PP sandwich。不采ρ随M恒定/线性插值、通用compute-first或历史优先性。实际完整读Ch38新89及67–108：现理想bubble式未被说成错误，后接训练反向边界清楚。 |
| [20981 Cyclotron v1](https://arxiv.org/html/2610.20981v1)：§3.1必要grammar/映射、§4依赖与通信lowering、§5及§6.1–3 | stale边从live排序图移除但旧register读取保留，mapping改变read-before-clobber及send/receive/guards；简单cycle不证明任意输入live-DAG/通用soundness。模拟默认无payload不是数值正确执行。2warmup＋4次取best、CPU部分慢、host-stage同transport至1.24×与GPU-direct换transport分清，融合90%只在不均衡配置。实际完整读Ch49新2313及2303–2336：只补通信IR接口，保验证/成本/成熟库，不授LLM整请求收益。 |
| [21640 ReFlow v1](https://arxiv.org/html/2610.21640v1)：§4–6方法/Eq2–6/Alg1、§7评价及Availability | σ控制replay占batch，τ另衰减loss并按tokenmass归一；unused可能stale，partial需真实behavior身份。局部variance界确依赖unused无偏、中心误差不相关、equal importance-token mass等条件。完整replica保shard/预热CPU驻留并非任意免费reshard。processed tokens含replay、5＋5/10＋10短测、trainreward非heldout、角色切换5.72/9.20秒及代码待approval均保留。实际完整读Ch33新1713及1697–1742：与既有replay三账/后接Agent-RL身份分责一致。 |

ROOT作者的EdgeFlow/BCL/RemoteKV/Meta四项复用B S42–45的实际非作者原件核验；Eq5/9启动排空矛盾、有限带宽准确阈值、健康可progress rank前提与Meta93%平均效率等都已进入README限定采用。B S47真实非writer POST又分别核七家族八机制段/完整直接两侧/本人注，不能把其Source作者身份误当Books writer。没有未决必要Source被S47替代。

### Books、争议及非writer写后链

77项实际POST分批闭合：REVIEW R5/R7/R10核root原22；root核A原6/B原5共11；本文件上一POST核B后8/root Ch5/25四共12；root核本人后15/LangDiT共16；root核reader六；reader R12核root Ch66三；B S47核root DC七，合77。本人完整消费这些既成结果，与89表行/具体证据段的采用边界逐一相对；本人作者层由root非writer核，reader成为报告共同作者后仍可核其未写的Books，但不授本日报DAY。没有把自读、仅PRE、来源note或marker存在算实际整合。

采用保留旧机制、相邻交接、全成本及回退：例如ACEdit冻结teacher前向/aux更新、LangDiT codebook仍经noisy input学习、P2TPO/SCOPE系数质量非完整梯度、MJev并非全部一步、Velox旧KV不消失、AVC关系资格先于同步、Remote健康collective非crash容错。RBCD由B及root分别实际核原假设/Eq14/Eq20和允许的常步长二次反例；只隔离受影响rate/early-stop，不宣布全文全错，不写Ch4或其他Books。重开须正式修正或可核证明排除反例；它不是待继续盲读全部附件的普通工作。

### 负侧分层样本与未全检范围

本日普通明确排除的arXiv具名抽检共8项：复用R1的22336治疗MDP（项目范围）/22110单变体NMT（已有方法任务组合），R6的22053 NameBias（固定句式人口）、21862 TagInsert（已有insertion/easy-first的有限tagging适配）、21440 SITAR（领域metric/便宜回归器）。本轮另实际完整读[22363 P3-WAM](https://arxiv.org/abs/2610.22363)、[22240 MMSearch-OPD](https://arxiv.org/abs/2610.22240)、[22182 LAMP](https://arxiv.org/abs/2610.22182)当前唯一v1题摘/标记，分别覆盖World-Action多任务组合、teacher反馈/curriculum recipe、few-shot多层预测集成；承认共享base/随机模态可见性、reward-gap权重与class-score混合的实际设计，仍未从所述局部验证建立需重选主线机制的独立条件/反证，不以机器人、小模型或不普适硬排。TagInsert已有理由修复有效，未见需要扩查受影响整组的共同错误。

另对两条含安全词的官方关闭项定点核核心，合计本层有10个具名负侧实例：[Anthropic ECDSA](https://www.anthropic.com/research/ecdsa-curve-origins)实际读起源恢复方法、What this means及Open questions，原文明确非cryptographic break/新攻击，scanner/LLL的密码学发现不构成新通用Agent可靠性机制；未把未解base points说成已解。[MiniMax承诺书](https://www.minimax.cn/news/integrity-self-discipline-pledge)web失败后同一官方URL普通HTTP恢复，实际读10/16日期与全部8项核心，只有企业治理/标识/报告/监督承诺，没有技术执行新机制或可检验安全保证，关闭不漏一个应采用的安全修正。Kimi真实guard语义变化属于已审候选事件，未按此类声明关闭。

未逐项重检其余明确关闭/范围外标题、CV另外3项关闭、全部未翻宽列表、全部机构窗外文章、全附件/代码或实验；已有首批准入与负侧校准只覆盖各自明确样本，不称全量负侧验证。没有将未抽检集合写成已审论文数，也没有新发现/下一日扫描。

### 辅助QA与移交

本人本轮实际再跑当前README的V3校验，结果通过；限定README/本日五记录的tracked diff-check无诊断，但五文件当前均untracked，故不拿该空输出冒充untracked内容验收。root此前265本地链接/围栏/行尾及77 marker位置检查作为辅助层复用，不代替以上语义检查。DAY内容未发现必须修复的准入、采用或实际落地问题；剩余仅root将§1/§5/§6、状态与检查时间行政同步后，保存完成稿再做最小FINAL读回。本层只追加本文件，不改README、Books、LS、index或其他日期，不stage/commit/push。

保存后实际读回本DAY完整新增，以及root刚明确化的README §5原始入口链接/RBCD单列重开条件，采用与隔离均未变，DAY仍通过。另保QA边界：root本次42窗口回归实际为41通过/1既有失败`test_renamed_event_cannot_inherit_old_date`，不是全套绿。本人定点读该test第229行，确为仅改同URL的标题后预期错误；`scripts/README.md`现明确允许同精确URL改标题而冻结日期，和root定位相符。本日无冻结日期豁免、此fixture不读取本日报；不据该不一致伪装本日日期/Source失败，也不修改范围外测试/validator。此处记录已有失败与隔离，不将V3单报通过改写成全回归通过。

## 保存完成态 FINAL：实际读回通过

复核者：`live1017_org_a`（非报告作者）；实际检查时间2026-10-17 10:41:08+08:00。仅核root在DAY后保存的完成态差额，未变化的原件/证据/Books POST不重审。已实际读README开头/§1–2、§5及§6：状态为完成，检查时间为`2026-10-17T10:39:38+08:00`，前一自然日窗口与Books纳入本次保持；§6独立身份、单独结论通过及77非writer链正确。当前表重新计数为89行＝77整合/10具体已有覆盖/1仅报告/1争议，89证据头仍对应，29owner与DAY一致。§5本窗可执行待办无；五源外部覆盖限制与RBCD中心争议保留，不用于正面证据/Books/无遗漏保证，原始入口和定点重开条件仍在。V3单报通过与窗口回归41/1既有不一致分开陈述，未宣称全套绿；10个负侧实例及未全检范围准确。结论：**保存完成态FINAL通过**，没有发现行政同步导致的采用、日期、计数或隔离不一致。本执行者只追加本文件，不改README/Books/LS/index，不stage/commit/push；本日任务到此结束，不接新日期、不恢复历史cursor或启动Weekly。
