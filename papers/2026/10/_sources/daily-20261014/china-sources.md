# Daily 2026-10-14：中国机构六源有限记录

窗口：北京时间 **2026-10-13 ～ 2026-10-13**。作者：`live_oct14_china`。实际检查日期：2026-10-14；终端时间读回 **18:52:22 +0800**。仅 own 本文件；未写 Report、Books、State、公共索引或 Git index。历史 cursor 按最新用户暂停段不启动，非周日不建 Weekly。

本轮独立重读 AGENTS、CODEX_RESEARCH_PROMPT、RESEARCH_CONTRACT、REPORT_CONTRACTS、来源使用说明/每日组、ROADMAP 与最新暂停 checkpoint。旧日 china-sources 只用于恢复真实 API 主机和具名 URL，不继承旧日 coverage。以下是收集/贡献初筛，**不是日级验收或 Books 结论**。

## 1. 六源实际访问与停止边界

| ID | 实际入口与检查范围 | 实际停止/结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-TENCENT-HUNYUAN | 首查 [Research](https://hunyuan.tencent.com/research)，web 提取超时；随后实际 POST [官方 API](https://api.hunyuan.tencent.com/api/blog/publicList)，`{"renderType":0,"pageNum":1,"pageSize":20}`，Content-Type JSON、Origin 官网、Referer Research、Accept-Language 分别 zh/en。zh 返回 code0、total11、实际11；en 返回 code0、total9、实际9。仅检查 id/title/publicAt/publishedAt/displayPublishTime。官方 GitHub 首10及具名 UniRL 窄窗、T1 release。 | zh 最前100119 publicAt/publishedAt/displayPublishTime分别 `1790053389/1789959110/1790006400`，100116分别 `1790049600/1789749798/1790006400`；en最前100116分别 `1790150728/1789707529/1790006400`。全部日期字段均窗前，已到total终点；日期字段不互充首次公开。T1 release空。UniRL本窗3 commit槽见§3。 | 可见目录已恢复，不再把动态网页超时保留为必需缺口；不证明删除条目或全组织历史完整。GitHub首10是有限发现，不授全org coverage。 |
| SRC-ZAI | 首查 [Research](https://www.zhipuai.cn/zh/research)，web超时、IAB创建超时；实际curl官方HTML恢复“全部”题名及内嵌 createAt。另查 [New Released](https://docs.z.ai/release-notes/new-released)、官方org首10，触发zcode-plugins、GLM-OCR窄窗与ZCode release。 | 可见最近GLM-5.3-Flash createAt `2026-08-26T14:00:00.000Z`，GLM-5.3 `2026-08-14T06:00:00.000Z`，GLM-5.2 `2026-06-16T16:00:00.000Z`，其余首段均更早，停止不按“查看更多”扩旧年池。release最近08-26/08-18/06-16；ZCode v3.14.3 published09-24；zcode-plugins无release、本窗4commit，GLM-OCR本窗0。 | HTML恢复首段足以检查本窗有限日期段，不声称完整机构论文史。createAt只保原字段口径，不自动当论文首次公开。 |
| SRC-BYTEDANCE-SEED | [Research/Blog](https://seed.bytedance.com/en/research)、[Public Papers](https://seed.bytedance.com/en/public_papers)，Newest→oldest、Page1/13、1–20 of246；featured无目录日，实际打开 [SeedRealtime](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction?view_from=content_recommend)。org首10触发VeOmni。 | Publication最新09-28 Periodic Weak Spots，09-01 HarnessDev，08-31 S3Gym/Aspire，均窗前；倒序页1夹住窗口即停，不扫13页或把246条变队列。Blog dated前缀07-31/07-20/07-08，featured原文Date08-05，均窗外。VeOmni release首5最近v0.1.13 published09-30；本窗4commit见§4。 | 仅此倒序目录段和具名相关repo；无全org无遗漏保证。AI for Science条目不进入本轮队列。 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)页1/2可见10条；[ERNIE releases](https://github.com/PaddlePaddle/ERNIE/releases)、具名repo窄窗commit。 | Blog最新05-09/04-30/04-15，页尾2025-11-21，首段已窗前，停止不进入旧第2页。唯一registered release ernie-4.5 published2025-06-30；窄窗commit空。 | 只授Blog当前日期段与具名repo，不称全机构论文/所有版本已审。 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/) Paper8条/Blog15条；实际打开 [首Blog](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)核其原文日期；org首10触发MiMo-Code窄窗及release。 | Paper日期前缀06-29/03-13/02-03/01-08均窗前；首Blog原文09-27，不因发现日移入10-13。MiMo-Code registered releases实际2条，v0.1.15 published09-22、v0.1.14 published09-23，非可靠倒序但已检查两条。本窗8commit槽，merge与branch同事件去重，见§3/4。 | **其余14条Blog目录无日期**；无法证明10-13日级完整覆盖，不记零命中。终态隔离，恢复须官方dated窗口片段或明确本窗具名单篇原始发布，仅重开受影响项。 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)、[中文入口](https://www.minimaxi.com/blog)实际redirect [minimax.cn/blog](https://www.minimax.cn/blog)、[Agent Tech Blog](https://agent.minimax.io/docs/techblog)。org首10触发OpenAgentCore、minimax-code、MiniMax-Code-MiniApps窄窗，并查cli release。 | EN/CN日期前缀08-13/07-31/06-09/06-01均窗前；Agent Tech Blog10-08/09-22/09-19共3条均窗前，停止。OAC release首5最新v0.0.11/v0.0.10均10-12；minimax-code v0.6.5为10-09；cli v1.0.28为10-12；MiniApps无release。窄窗OAC3、minimax-code1、MiniApps0commit。 | org首10有限发现，不授其外repo coverage；代码commit不当模型首公开。 |

本轮没有确认六机构网页的新10-13论文。MiMo目录日期缺口与有限GitHub发现边界仍不支持六机构完整零命中或互联网无遗漏。没有扫描每周来源、历史年份或完整组织目录。

## 2. 实际GitHub查询与事件计数

发现 API：`https://api.github.com/orgs/<org>/repos?sort=updated&direction=desc&per_page=10`，实际org为Tencent-Hunyuan、zai-org、ByteDance-Seed、XiaomiMiMo、MiniMax-AI。各首10，不分页；updated_at只作活动线索，不作公开日期。pushed_at在窗口或更晚者定点查询，另恢复具名近期UniRL入口，**不是扩全机构目录**。

窄窗：`https://api.github.com/repos/<repo>/commits?since=2026-10-12T16:00:00Z&until=2026-10-13T15:59:59Z&per_page=20`，这是北京时间完整10-13自然日的UTC映射，材料归属仍只按公开日期。实际：UniRL3、zcode-plugins4、GLM-OCR0、VeOmni4、MiMo-Code8、OpenAgentCore3、minimax-code1、MiniApps0、ERNIE0、ExplorationBench0；均首个短页/空页终点，没有第二页待扫。23是**commit槽**，非23候选/论文/全文审阅；MiMo2657 branch＋merge属同事件。带PR只核具名实际 `pulls/<number>` 的merged_at，不把每条branch commit当首次公开事件。

release API均 `releases?per_page=5`：T1、ZCode、zcode-plugins、VeOmni、ERNIE、MiMo-Code、OpenAgentCore、minimax-code、MiniApps、cli。只取tag/published_at，均无窗内registered release；不深入窗前release或遍历全版本。

## 3. 待root局部准入校准的两条具体增量

以下是**拟候选**，独核未完成，不以topic/owner关联保留。两者都是实现事件，非新模型论文。先保新增且可验证的契约/失效命题，成熟hash/async原则不计新增。

### A1 — UniRL frozen teacher：成功加载不等于跨rank身份一致

原完整题名：[fix(lora): reject frozen teachers whose weights differ across ranks #575](https://github.com/Tencent-Hunyuan/UniRL/pull/575)。实际merged_at `2026-10-13T05:37:27Z`，merge commit [6c828f5](https://github.com/Tencent-Hunyuan/UniRL/commit/6c828f5ed81649153315d996f0f597e8808ff144)，公开日期本事件10-13。

完整核心：每rank从自身teacher路径加载自身shard（broadcast_from_rank0=False）。旧控制器只能抓read/injection抛错，无法发现均成功但node-local副本陈旧/Hub revision下载间漂移的teacher混合；本次inject后按teacher content sha256跨rank gather，任一不同则各rank抛同一RuntimeError并列各rank sha。先前草稿read错误/spec/perteacher多次gather及path resolver改动已撤回，不能把被删方案当当前修复。rank-local失败仍归已有#258 fail-fast actor collector；stuck mount/download不抛错的hang不覆盖。

准入链：rank-local teacher load均成功仍可能形成无error的混合权重目标 → 实際hash一致性gate及2process负例把该错误与controller fail-fast区分 → 需要在sharded frozen teacher构造时单独验证跨rank语义身份，而不能由actor成功状态代替。拟评分 **1 + 2 + 2 = 5**：局部构造检查，跨rank/控制器边界，稳定身份条件；不把通用哈希价值/整个RL训练借入评分。拟owner `TRAIN-LORA`，与分布式失败传播交接，最终owner/Books差额由root查实际正文。

作者证据：CPU/Gloo2process，synthetic LoRA checkpoint；rank1一个lora_B元素变化使两rank同错误，identical copies sha相同，无teacher跳过gather；作者本地torch2.13/PEFT0.21，不作项目版本推荐。Ray2actor实collector实验：一rank构造FileNotFoundError、另一rank blocked gather，controller约2.3s抛错、shutdown约1.6s；这验证旧fail-fast适用而不是本PR新增。最终缩减后GPU未跑，早期2×H100 smoke对应旧commits；full recipe训练未跑，不能写当前FSDP/GPU acceptance或普遍无hang。无config/checkpoint格式变化、已有resume hash不变；含teacher新增一small object gather。

必要当前代码已实际核：[merge精确版lora.py](https://github.com/Tencent-Hunyuan/UniRL/blob/6c828f5ed81649153315d996f0f597e8808ff144/unirl/train/lora.py)，§`_inject_frozen_adapter`、`_load_frozen_adapter`、`_weights_sha256`、`FrozenAdapters.inject`，及本PR两file patch。raw.githubusercontent.com连接reset后实际GitHub contents API精确ref取得正文，不再留外部缺口。代码读取CPU weights、检查key/shape、登记defer_after_materialize，返回sorted `(key,dtype,shape,bytes)` 内容sha；之后所有非empty shas作默认process-group all_gather_object并比较name→sha字典。materialize后load_model_state_dict仍broadcast_from_rank0=False。

**采用限定：** 该gate检查已读tensor内容，不是GPU materialize后的checksum；hash不含adapter_config，不能仅凭相同tensor sha证明完整teacher函数/缩放配置一致。peft_cfg仍从本地配置注入且使用use_rslora/alpha_pattern/rank_pattern；“不同配置可能在同tensor hash下改变函数”是代码边界推断，未做crossrank实验，不宣称已复现新的bug。无teacher分支不gather，没有single-process无dist fallback；rank-localhang不覆盖。完整PR及受影响当前代码已读，本分支必要Source完成；**独立Source复核与Books未完成**。

### A2 — MiMo-Code MCP：首turn工具集合可部分就绪

原完整题名：[feat(mcp): connect servers in the background with a bounded first-turn wait #2657](https://github.com/XiaomiMiMo/MiMo-Code/pull/2657)。实际merged_at `2026-10-13T08:03:43Z`，merge [b258d28](https://github.com/XiaomiMiMo/MiMo-Code/commit/b258d28f436446bb1c9768fe0134693219be7cdc)；branch [2f37328](https://github.com/XiaomiMiMo/MiMo-Code/commit/2f37328981efe33383006e3d10fa51be29a35e62)为07:56:44Z，同事件不重复计。

完整核心：旧启动把state初始化/首prompt阻塞在最慢MCP server；新启动background fork，tools()给startup settle最多3s等待后继续当前ready集合，后续turn再拿到其余（后续refreshHost不在此deadline内）。管理accessor仍full settle，connect/disconnect/add不得与background工作race；clients(context)捕获视图例外见下。作者只声明first-turn-wait.test验证慢server不拖住startup tools及稍后可见、typecheck通过，无real remote MCP端到端/SLO评价。

准入链：首prompt过去消费“所有startup已settle”能力视图 → 现在deadline后可消费ready subset而管理mutation仍等full settle → 首turn缺tool不能再直接解释为server不存在或永久无能力，工具发现和连接管理必须采用不同完成条件。拟评分 **1 + 2 + 2 = 5**：局部启动变更，Agent首turn与MCP连接边界，稳定partial readiness契约；不把一般async设计抬分。拟owner `AGENT-MCP`，不借全部Agent lifecycle升分。

必要当前代码已实际核：[精确merge MCP index.ts](https://github.com/XiaomiMiMo/MiMo-Code/blob/b258d28f436446bb1c9768fe0134693219be7cdc/packages/cli/src/mcp/index.ts)及[first-turn-wait.test.ts](https://github.com/XiaomiMiMo/MiMo-Code/blob/b258d28f436446bb1c9768fe0134693219be7cdc/packages/cli/test/mcp/first-turn-wait.test.ts)，PR全2file patch与contents API限定refreshHost必要段。State.settled为Deferred；startup Effect.forEach unbounded connection attempts forkIn(scope,startImmediately)，ensuring settled完成（成功或失败），pending占位失败清除。finalizer在fork前登记，先中断inflight再关闭stored/retired clients；storeClient uninterruptible避免创建后未登记orphan，但不作完整生命周期无泄漏证明。

**采用限定：** `tools()`只给Deferred startup settle await设FIRST_TURN_WAIT=3000；其后仍`refreshHost`，host变更/retry可同步`create`，故**不是tools()整体3s端到端SLO**。其他通常accessor经getState等全settle，但`clients(context)`从captured turnClients直接返回，是明确例外，不能写“所有其他accessor都等”。prompt loop每step重新resolve工具并announce delta属原code注释声明，未本轮端到端执行。fixture真实localhost HTTP中slow initialize等待手动promise release，first tools仅fast_ping，release后status两connected，后tools两ping；没有assert elapsed上限，虽hard blocked slow使subset路径有效，仍非remote生产SLO。完整PR/受影响code/fixture已读，本分支必要Source完成；与lazy loading不捆绑评分，独立准入/Source/Books待root。

## 4. 具体EX与实际受影响边界

仅摘要/核心贡献筛选，不把普通fix全部变成code/Books深审。含正确性、兼容或安全信号的必要事实保留，独核若发现改变既有论点的新证据，仅重开对应项。

| 原件/身份 | 本窗日期与已读核心 | 具体EX理由/限制 |
| --- | --- | --- |
| [UniRL share stack lifecycle #585](https://github.com/Tencent-Hunyuan/UniRL/pull/585) | merged10-12 16:23:31Z→北京时间10-13；共用base constructor/lifecycle和metric aggregation，unified新增optimizer_updates；NaN max_grad_norm旧<=0检查漏过会NaN填grad而返回finite norm，改构造期拒绝。training loss/grad/optimizer/anchor不变。 | 既有数值输入/指标契约修复，不新增训练机制；作者CPU旧新对照，不支持GPU/FSDP acceptance。NaN信号保留，非整份release深审。 |
| [UniRL stack layout/input placement #592](https://github.com/Tencent-Hunyuan/UniRL/pull/592) | merged10-13；路径rename/共享input placement，backend._device替代first-param device以适配FSDP2 CPUOffload参数在host；只segment/conditions/advantages搬GPU，不搬media；严格检查int/positive标量而非截断coerce。 | 修复/重构既有设备与类型契约；不提出新offload机制或可比端到端收益。 |
| [VeOmni GLM-5 EP #1283](https://github.com/ByteDance-Seed/VeOmni/pull/1283) | merged10-13 07:55:46Z；扩已有#1274 perexpert converter/EP stream到GLM-MoE-DSA，复用DeepSeek patches，fp32 router避autocast、monitor记录索引、dim0 expert shard、skip未build MTP。 | 增加模型支持/复用既有EP机制，没有新的资源边界或可比性能证据。作者290CPU tests；GPU/NPU models-patch/e2e仅collected未run；GLM无SP attention、LoRA target/router replay未接、count_flops未登记→MFU0，不能写全能力支持。 |
| [VeOmni shuffle #1292](https://github.com/ByteDance-Seed/VeOmni/pull/1292) | merged10-13 06:36:33Z；data.shuffle→data.dataloader.shuffle，map sampler与HF iterable buffer明确转发，offline_embedding强制off，Energon用独立buffer。 | 配置迁移/既有shuffle wiring；旧key解析失败是真兼容性变化，不能借通用数据顺序原则升分。 |
| [VeOmni drop_last #1301](https://github.com/ByteDance-Seed/VeOmni/pull/1301) | merged10-13 11:41:16Z；旧赋data.drop_last是未读stray attribute，改dataloader.drop_last并日志同字段；当前offline embedding已pad至完整global batch。 | 旧假日志/未生效override修复，**当前路径runtime behavior不变**；自动release摘要“now retains final batch”不能推断旧路径曾丢样本。 |
| [VeOmni NPU images #1294](https://github.com/ByteDance-Seed/VeOmni/pull/1294) | merged10-13 12:25:14Z；CANN9.1 test image与job120min。 | CI版本/预算切换，无新增模型系统机制/benchmark。 |
| [MiMo history classification #2642](https://github.com/XiaomiMiMo/MiMo-Code/pull/2642) | merged10-13 06:40:18Z；kind恢复、CJK body_idx隔离search form与original body显示，v8 clean/repair/finalize中drop triggers后rebuild/restore，migration慢retry120s。History.search无kind新参数，shared index保synthetic/summary kinds供consumer过滤。 | 修复既有全文索引/展示/迁移流程，不新增memory表示或可靠性证据；97tests/5bench skipped不是Agent任务质量对照。 |
| [MiMo FDS launcher #2652](https://github.com/XiaomiMiMo/MiMo-Code/pull/2652) | merged10-12 16:02:28Z→北京时间10-13；npm optionalDeps多130MB sibling，改thin launcher取单version-pinned archive，package-local vendor，Windows temp运行copy；原平台npm packages退役，native安装推荐。 | 分发/安装范围，不是训练/Agent执行机制。安全核心保留：仅存在well-formed published hash才强制checksum，未发布sha256可跳过；不能写供应链完整性保证，后续发布sha256/收紧policy未实现。 |
| [MiMo lazy MCP #2653](https://github.com/XiaomiMiMo/MiMo-Code/pull/2653) | merged10-12 16:09:16Z→北京时间10-13；tool definition稳定、user persisted delta catalog、conversation最多32加载、search full schema。 | 本窗merge事件实际核实；相同branch核心在前日报已具体EX，未见本窗新增命题，不机械把不同日期merge当新贡献。prompt-effect test本作者未完成(hang>3m)，不称全runtime验证。 |
| [MiMo Go session #2655](https://github.com/XiaomiMiMo/MiMo-Code/commit/597e71039d60ff843f2ca0d9fc10fb9f71feb973) | committer10-13 05:51:11Z；既有sessionID送x-opencode-session，仅Go provider/effective base URL，修复09-05起MissingSessionID；其他provider不变。 | Provider request兼容字段，不是新会话语义或训练机制。 |
| [MiMo Desktop GA readme #2654](https://github.com/XiaomiMiMo/MiMo-Code/commit/c7dbd85d815438c128b8e578ec57da313b696784) | committer10-13 05:04:59Z；移beta/invite与X-Preview名称，voice例用Flash、ASR不变。 | 文档availability/model naming，不能当V2.6模型首公开。 |
| [MiMo scripted MCP test](https://github.com/XiaomiMiMo/MiMo-Code/commit/73393597a61f90e8ef05fbc14e890b7f6f3aa1f0) | committer10-12 16:00:23Z→北京时间10-13；scripted model直调工具，测试显式tool_search=false。 | 测试fixture兼容，不是Agent新执行保证。 |
| [OAC request log #690](https://github.com/MiniMax-AI/OpenAgentCore/pull/690) | merged10-13 07:20:13Z；metadata bounded windows public/admin各1000 started requests，restart清空，active/completed/aborted只HTTP不表示Turn完成；不buffer bodies，不收raw path/query/header/payload/credentials/errors；保stream/HEAD/implicit Content-Type行为。 | 实现通用轻量HTTP日志，没有新增Agent完成证据机制；作者discard sink microbenchmark14–15µs不含real sink，不是distributed tracing/production成本证据。 |
| [OAC settings storage #689](https://github.com/MiniMax-AI/OpenAgentCore/pull/689)、[hierarchy #691](https://github.com/MiniMax-AI/OpenAgentCore/pull/691) | merged10-13 06:52:00Z、08:13:35Z；settings canonical home、immutable-selection现有API、observed selection变更invalidate form；布局响应式，existing API/lifecycle不变。 | UI组织/既有配置ownership，不新增storage并发协议；unseen concurrent PUT仍last-writer-wins，不冒充atomic conflict detection。 |
| [minimax-code OSC7501 #471](https://github.com/MiniMax-AI/minimax-code/commit/e798b460f4d8603ce732e5d319d63c8018ef6cad) | committer10-13 08:02:51Z；approval/question wait readback不再受build-mode gate，missing login统一status/error、OSC blocked auth；tui.programStatus可关。 | 既有交互状态metadata到terminal projection，非新增可靠执行/权限机制。 |

ZAI四commit核心读取限README/目录文档及非dist相关patch；不全generated bundles：

- [Blender panel/sidebar](https://github.com/zai-org/zcode-plugins/commit/1164f7a9e12adc88a81ab2d1f199b6e8d52ba6d1)（10-13 11:07:53Z）：UI panel controls/default sidebar，具体EX布局变更。
- [Tripo 3D plugin](https://github.com/zai-org/zcode-plugins/commit/f09f7d181bbd42b3ea6181248f4cb5cdaee0e007)（09:31:42Z）：现有OAuth2.1 MCP26tools与两skill/SessionStart规则接入，China-only构建、短期CDN链接、批量credit确认；不披露生成模型新机制/评价，不因多模态或MCP关联入选；付费与权限事实不作运行安全保证。
- [external directory docs](https://github.com/zai-org/zcode-plugins/commit/de46a889afd976b7a1b57276637c014f4ec20b54)（09:23:38Z）、[marketplace classification](https://github.com/zai-org/zcode-plugins/commit/2b757a16bc1593a495791ecd49bc216086f4ce1d)（07:53:40Z）：directory导出publisherType=community，与usage category/capability分开，旧plugins不迁；具体EX发布者分类/贡献目录，不新增authority/security模型。

## 5. 交接与尚未完成层

- 有限源收集和核心贡献筛选已落盘；拟候选A1/A2待root/reader准入校准；各5分仅对应上述最小命题，不借成熟原则或整repo修复集合升分。
- A1/A2必要当前code与明确未覆盖边界已核，普通本分支有限Source待办0；独立准入/Source、具体Books差额与日级验收交root/reader，不扩23commit全部PR深审。
- 外部终态保留：MiMo14无日期Blog不得用于候选、Books或“本窗零命中/无遗漏”断言；恢复须带日原件/目录片段，只重开受影响项。官方org首10有限发现边界明示。
- 没有Books差额/整合、独立Evidence/日级验收或实验复现完成声明；普通待办以root最终报告为准。未stage/commit/push。

本文件用`git diff --no-index --check /dev/null <本文件>`实际检查untracked文本空白；最终语义/链接读回由root/reader另核，不声称全仓diff干净。本分支ownership可交接给root；其他文件已有/并发修改未动。
