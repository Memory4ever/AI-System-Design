# Daily 2026-10-15 — 国内六来源有限检查

**窗口：** 北京时间 2026-10-14 ～ 2026-10-14；不处理历史 cursor、Weekly 或窗外旧材料。
**检查时间：** 2026-10-15 09:04～09:07 +08:00，后续必要原证另记。
**状态：** 有限来源已处理；root首批准入校准接纳548/596/492、2618按5分窄边界、254按4分安全深入关闭；549归548家族、704排除。必要Source与具体Books差额提案已保存，待root独核与落实；不是报告完成或Books验收。
**文件 ownership：** 本子任务仅写本文件；Books、README、State、索引不写，不 stage/commit/push。

## 1. 本轮实际来源与停止位置

所有记录来自本轮重新打开的官方入口；昨日记录仅恢复具名路径，不继承旧覆盖。官方 org API 仅最新 updated 首 10 项、无分页，updated_at 仅线索；pushed_at 落窗或更晚的主题相关 repo 才查本窗 commit。普通 commit 不自动成为论文或深入审阅队列。

| ID | 实际入口与已读段 | 当前结果 / 停止位置 | 限制 |
| --- | --- | --- | --- |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research) web 两次 timeout；curl 得动态 HTML 与真实资产 JS。browser 首次 timeout，第二次返回 subagent 不支持 IAB visibility。最新首10 org 中 UniRL 活跃，窄窗6 commit。 | 真实动态JS解析出的公共API恢复结果见§3：仍未取得Research日段，终态隔离；UniRL6条完整commit核心已筛，4拟准入、2具体EX。 | 不授Research日段coverage或零论文。HTML build 2026/10/14不等于研究公开日。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 全部/时间排序可见首段，最新08-26/08-14/06-16；[release notes](https://docs.z.ai/release-notes/new-released)最新08-26/08-18；org首10→GLM-OCR。 | 首段已早于窗口即停，不点旧查看更多；GLM-OCR本窗1 commit，#254安全边界拟准入。 | 只授这些目录段和具名repo，非全org无遗漏。 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)、[Public Papers](https://seed.bytedance.com/en/public_papers) Newest→oldest、1–20/246、Page1/13；featured [SeedRealtime](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction?view_from=content_recommend)原文Date08-05。org首10→VeOmni。 | Publication最新09-28/09-01/08-31，Blog dated首段07-31/07-20/07-08，均窗前即停；VeOmni本窗选择性重计算#1166完整PR body已筛EX，见§5。 | 不扫13页、不把246条变队列；AI for Science不入范围。 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)页1/2十条，最新05-09/04-30/04-15；具名ERNIE repo本窗commit。 | Blog首段窗前，停止不进旧页2；commit实际返回空数组。 | 不称全百度论文或无遗漏。 |
| SRC-XIAOMI-MIMO | [主页Paper/Blog](https://mimo.xiaomi.com/) Paper8条、Blog15条；[首Blog原文](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)实读原文日期09-27；org首10→MiMo-Code。 | Paper日期06-29/03-13/02-03/01-08均窗前；首Blog窗前，余14目录无日期，未用发现日重归属。MiMo-Code本窗3 commit，#2618执行结算/恢复边界拟准入，其余EX。 | 余14Blog目录不支持本窗零命中；保留外部日期片段缺口，见§3。 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)、[中文Blog](https://www.minimaxi.com/blog)redirect至[minimax.cn](https://www.minimax.cn/blog)、[Agent Tech Blog](https://agent.minimax.io/docs/techblog)；org首10→OpenAgentCore。 | EN/CN首日期08-13/07-31/06-09/06-01均窗前；Tech Blog10-08/09-22/09-19三条窗前即停。OAC本窗15 commit，按完整核心说明主题筛选，UI/文案早退。 | 仅目录段与相关repo，不全组织；commit非模型首公开。 |

实际 API：`https://api.github.com/orgs/<org>/repos?sort=updated&direction=desc&per_page=10`，org Tencent-Hunyuan/zai-org/ByteDance-Seed/XiaomiMiMo/MiniMax-AI。具名 commit 查询：`https://api.github.com/repos/<repo>/commits?since=2026-10-13T16:00:00Z&until=2026-10-14T15:59:59Z&per_page=20`；这是完整BJT自然日映射，日期归属仍按公开日期。UniRL6、GLM-OCR1、VeOmni1、MiMo-Code3、OAC15、ERNIE0；皆短首页/空数组即终点，没有第二页待查。26是commit槽，不是26候选或论文。

## 2. 首批准入校准请求（必要原证尚普通）

以下五项均已实际读完整 PR body/核心说明及 merge 日期。拟分只计实际新增命题，不借成熟原则或机构声望；root 校准前不记证据/Books完成。

| 事件 | 已核当窗公开日期/精确merge | 具体准入链 / 拟分 / owner |
| --- | --- | --- |
| [UniRL BAGEL token-layout & first ratio #548](https://github.com/Tencent-Hunyuan/UniRL/pull/548) | 2026-10-14；`0fbf3ad002c27dd57a5e6c542b200c210a2e4ca0`，merged12:23:04Z | rollout/replay初次ratio≈1仍可能漏conditioning错配 → 记录并比对KV length/RoPE/canvas，作者真实负例中ratio偏差很小但layout不等 → 重考虑“单靠logprob/ratio parity证明条件一致”。拟2+2+2=6，`TRAIN-GRPO`（owner最终由root确认）。 |
| [UniRL non-persistent buffer dtype #596](https://github.com/Tencent-Hunyuan/UniRL/pull/596) | 2026-10-14；`d8a82c60eac5a878ddc179b7395bfc408213637f`，merged12:11:49Z | 加载相同BF16参数仍非同policy → meta-init/wrap/to_empty/restore可把显式FP32非持久RoPE buffer降BF16造成position-dependent logprob drift；恢复captured dtype并区别persistent/non-persistent → checkpoint参数一致不覆盖初始化派生状态语义。拟1+2+2=5，`TRAIN-CHECKPOINT`。 |
| [UniRL guarded CUDA MPS #492](https://github.com/Tencent-Hunyuan/UniRL/pull/492) | 2026-10-14；`0ac8bc3e0e9f59fc7c7019aab61645f545e1650b`，merged12:38:13Z | fractional GPU仅调度记账、低util不等于可靠共享收益 → 同H20/535.247.01测得MPS收益取决scorer实际forward/瓶颈且active-thread<100的FP16/BF16可finite-but-wrong → 共享资格需区分调度、并发、数值正确性。拟2+2+2=6，`PLATFORM-GPU-SCHEDULER`。PR正文可能包含已删草稿，当前merge代码必须先核。 |
| [MiMo-Code Stop/recovery #2618](https://github.com/XiaomiMiMo/MiMo-Code/pull/2618) | 2026-10-14（merged2026-10-13 20:07:21Z）；`002cb4c97bd1346829dbb08d98242913df4575d0` | abort不证明异步工具退出/无副作用 → Stop关准入后消费真实结果再释放、持久化started边界及确切resume target → 重新考虑取消/恢复何时可安全重放。root校准1+2+2=5，`AGENT-WORKFLOW`。status retry文案/状态投影不单独升分。 |
| [GLM-OCR task file security #254](https://github.com/zai-org/GLM-OCR/pull/254) | 2026-10-14；`0288f96bb9e78cb439883eaa725eeae90bd177c5`，merged01:46:03Z | 路径存在/位于输出目录不证明任务产物登记 → /tasks/file改为completed task记录的verified PNG crop并拒绝traversal/symlink → 文件读资格不能由客户端path给出。root校准1+1+2=4，`PLATFORM-SECURITY`；单下载组件、不借通用授权原则跨系统升分，安全受影响Source已深入，拟仅报告关闭。 |

均非新模型论文。作者测试声明不是本轮运行；本子任务未执行作者测试或GPU实验。必要当前原证及反侧见§4；492的PR正文与实际merge能力不一致必须收窄。

后来补充两项亦已实际读取完整PR body及当前必要代码，待root一并校准：

- [UniRL mixed canvas #549](https://github.com/Tencent-Hunyuan/UniRL/pull/549)，merged2026-10-14 13:10:26Z，`2c19e14e5bbbf573d30f3b8bfb3ef126a748b88f`。同一rollout不同分辨率从单canvas变per-group → contiguous canvas run发请求、dense pad至default tokens并replay trim → 降生成分辨率不等于降trajectory存储，per-token anchors仍需一canvas。root校准归并548的BAGEL conditioning家族事件，**不另增候选、不重复评分**；owner同`TRAIN-GRPO`。旧单canvas仍成立，dense pad开销不另升分。
- [OAC bounded native retries #704](https://github.com/MiniMax-AI/OpenAgentCore/pull/704)，本窗merge `283f14e258c8503b7809f837ac1adc9c86f37612`（commit2026-10-14 10:30:16Z；精确merged秒不作为日期必要条件）。实际Core修复由unbounded改native bounded retries与结构化连接错误分类；root校准**贡献前EX，不评分**：有限retry不等walltime是成熟timeout设计的局部边界，未提供新LM执行机制或足以修正已有解释的对照反证。已读原证/限制保留，不因审阅费时排除；不列正式候选。

## 3. 真实恢复、release与外部边界

- Hunyuan实际HTML资产 `index-DY_9LI5-.js`→`index-CsiqYD6x.js`→`index-Coqz4btG.js`，真实定义`/api/blog/publicList`，前端`{pageNum,pageSize,renderType}`，全部renderType0；显示日期优先`displayPublishTime || publishedAt || createdAt`。axios真实base为`https://aistudio.tencent.com`。本轮POST到hunyuan域404；正确Studio域POST405 Not Allowed；GET只返回Studio HTML非JSON。此前web两次timeout与子任务IAB限制不冒官方零条。root另实际浏览器尝试36s timeout/kernel reset，未拿目录，无登录/权限问题；不重复失败。有限原始入口已尝试，Research日段终态隔离；恢复条件是未来可用浏览器“全部”当前日期前缀或官方带日期目录响应。只重开这个源段，不扩扫旧年。
- MiMo余14Blog目录没有日期，首Blog原文已确认09-27，不自动假设目录可靠倒序。其余14不变逐项深审队列；终态缺的是本窗官方dated目录片段或具名本窗原始发布，未取得时不支撑六源零命中/无遗漏。
- Release API实际均`releases?per_page=5`：UniRL2条最近v0.2.0 published10-08；GLM-OCR首5最新04-08；VeOmni首5最新09-30；MiMo-Code实际2条09-22/09-23（非可靠倒序但两条都核）；OAC首5最新v0.0.11/v0.0.10为10-12；ERNIE唯一ernie-4.5为2025-06-30。均未见本窗registered release，不深审窗前release或完整版本史。
- 本轮GitHub匿名API实际rate-limit（服务器明示配额用尽）；`gh`不存在；GitHub网页files timeout/cache miss、commit.patch空结果不能算code已读。随后GitHub连接器list filenames/per-file patch/精确ref成功恢复必要Source，**不能继续把可恢复的候选代码标外部受阻**。仅具名必要路径、未扩组织。

## 4. 必要Source：精确当前实现、支持与反侧

### A1 / UniRL #548：条件layout与ratio是不同证据

精确merge code/全受影响patch已读：[diffusion.py](https://github.com/Tencent-Hunyuan/UniRL/blob/0fbf3ad002c27dd57a5e6c542b200c210a2e4ca0/unirl/models/bagel/diffusion.py) `_resolve_single`；worker pipeline `_install_noise_tap`/forward；adapter `build_conditions`；[single.py](https://github.com/Tencent-Hunyuan/UniRL/blob/0fbf3ad002c27dd57a5e6c542b200c210a2e4ca0/unirl/train/stack/single.py)255–342及guard。

worker捕获`kv_len,rope,height,width`，per-row layouts沿conditions交付；trainer实际rebuild context后字典不等直接require失败。已携context路径且不force_rebuild/differentiable input-image则直接返回，不检查；没有layouts的trainside不检查。四个字段相等不是token内容、embedding或整个条件函数的checksum，这是范围限制而非新bug复现。

作者实验：8×H20，BAGEL-7B-MoT、vLLM-Omni0.28.0、LoRA、16prompts×8samples、512²，t2i PickScore/it2i异节点EditScore。正常t2i首ratio deviation8.6e-6/1.4e-5；rollout anchor it2i5.4e-5。改prompt多3token由KV63→66、改source-width由2268→1161均layout硬失败；旧it2i5938 vs2263错配时ratio_min0.99995，健康0.999966，表明ratio粗检不是conditioning同一性证明。

guard opt-in、finite正tol、只警告非阻断；算法必须给ratio_min/max，缺失KeyError；rank0指标不是跨rank聚合。**实现读取的是step前forward算出的ratio，但警告函数在`_run_updates`全部update返回后或`_run_window`最后optimizer已step后调用；不能写“警告保证optimizer前停止”。** synchronous/每rollout权重同步及rollout-oldlogp假设必要；replay anchor0/0不是独立rollout parity。作者harness未commit，具体多模型/跨后端普遍性未证；本轮未运行。

### A2 / UniRL #596：参数产物之外的构造态

精确merge [meta_init.py](https://github.com/Tencent-Hunyuan/UniRL/blob/d8a82c60eac5a878ddc179b7395bfc408213637f/unirl/models/types/meta_init.py)1–212已完整读；Qwen bundle、VeOmni wrap/backend必要patch已读。`capture_init_state`取state_dict外named_buffers及plain tensor attrs的CPU clone；meta态capture失败。factory在temporary default dtype下构造，finally恢复进程default；finalize只cast参数和persistent buffers，nonpersistent保持显式构造dtype；restore先按captured dtype重register，再拷到DTensor local/常规tensor；shape不等fail。wrap仅参数cast，旧针对RoPE重算helper删除，不把它当当前修复。

作者repro：Qwen3/Qwen3-MoE，seq4096/BF16，两backend对from_pretrained的maxΔlogp0/bit_identical；lifecycle还覆盖QwenVL/Qwen3.5/SD3/DTensor，SD3persistent buffer仍BF16符合对照。硬件/样本prompt/重复数/完整GPU训练与性能Not Disclosed，本轮未运行。可采用构造态dtype边界，不泛化为任意模型完全一致或所有meta init安全。

### A3 / UniRL #492：MPS局部资格证据与当前实现分责

连接器实际list仅6file，全部patch已读：README、example、config.py、mps.py、server.py、workers/group.py。精确merge为[0ac8bc3](https://github.com/Tencent-Hunyuan/UniRL/commit/0ac8bc3e0e9f59fc7c7019aab61645f545e1650b)。当前any reward.mps启动**managed local daemon**，single-node、0<num_gpus<=1；actor runtime_env在first CUDA context前传pipe、active percentage、可选`0=<MiB>M`内存cap。config只校验active整数1..100与memory unit，不查scorer/dtype；README和example对H20 driver535给halfprecision100%的**建议**。

重要反侧：PR body还声称external模式、qualification allowlist、低于100的FP16/BF16硬拒绝、30s CUDA drain、bench/test模块；实际merge没有这些路径，pool.py/actor.py/bench均不变。server仍pool.shutdown再退出daemon context；不得采用正文的“当前guard/排空保证”。mps.py会去掉daemon ambient client限制、拒绝覆盖已有pipe/log；parent watchdog每秒检测owner退出后quit，quit timeout10s然后清临时目录；这不是已证明全GPU故障/进程kill安全。

作者H20/driver535.247.01、Python3.12.11/Ray2.46.0局部实验：idle确认后client concurrency4、两重复35pairs/triples及三重复homogeneous sweeps；native forward batch与service batch分开。轻量三scorer median+24.9%，OCR瓶颈约0或负；CLIP+PickScore native batch1为-3%、batch4+25.2%，不是普遍MPS提升。active<100时FP16/BF16 CLIP160/160 nonfinite，FP16 PickScore50%有finite wrong；FP32例正确，但非FP32 throughput证据。以上是作者声明，不是本轮profile或已与最终缩减代码完整复验；作者早期受其它GPU workload污染的timing已明确废弃。**可保局部H20数值/负面结果，当前guard实现主张不成立；是否仅报告/争议由root独核。**

### A4 / MiMo-Code #2618：取消不是副作用回滚

**当前body核对：** 本轮匿名REST先成功读取完整body，后连接器`fetch_pr`再次返回同title/merge/body：Summary覆盖保留已completed tools、exact resume target admission、planResumeTrim＋真实SDK转换、Stop后abort/consume真实结果；Scope明确optional execution not-started/started。与root较旧网页body不同，按精确merge实际新增code/fixture立论，不采用相邻PR或旧索引未披露内容。

精确merge [settlement.ts](https://github.com/XiaomiMiMo/MiMo-Code/blob/002cb4c97bd1346829dbb08d98242913df4575d0/packages/cli/src/tool/settlement.ts)全33行、[processor.ts](https://github.com/XiaomiMiMo/MiMo-Code/blob/002cb4c97bd1346829dbb08d98242913df4575d0/packages/cli/src/session/processor.ts)executeTool390–490及cleanup patch、message-v2 planResumeTrim/assertResumeModelBoundary、prompt resume admission/ToolSettlement接线、run-state ownership退出必要段已读；没有逐44文件无关路径深审。

`ToolSettlement.promise`interrupt→abort controller→不可中断wait真实promise→consume结果→再传播原interrupt。processor注册local tool未started，trusted完整input且仍running才标started；scope关闭关准入/await fiber exit，settled.result用于完成/error持久化，不再旧250ms后无条件aborted。resume parent scoped、精确目标admission再核、preserve已完成工具/输出、删除仅未started且无protected output项；SDK转换后保证call/result成对且不留下assistant prefill。

实际新增fixture `tool-gate-cancel.test.ts`中的Filesystem.write：延迟真正write，cancel已abort但未release时仍busy/started/running；release后文件真实出现，completed part携cancelled metadata；resume后writes仍1且原result保留。另plugin/MCP after-hook、exec guests、partial与complete-empty input、cold registry fixture明确覆盖。作者109pass及retries状态测试声明不是本轮运行；scripted model/local file不等于任意远端工具exactly-once。

关键限制：settlement没有timeout；忽略abort且不settle的工具可使Stop等待无限。本机制等待可观察结果并不回滚已生效write；process crash/kill后远端副作用与持久result原子性未建立。`execution=started`不能证明远端committed，无结果时也不能保证安全重试。只采用这些边界，不宣称生产无重放/全工具exactly-once。

### A5 / GLM-OCR #254：产物allowlist不等于用户鉴权

精确merge [task_images.py](https://github.com/zai-org/GLM-OCR/blob/0288f96bb9e78cb439883eaa725eeae90bd177c5/apps/backend/app/utils/task_images.py)全146行及tasks route、全部必要test patch已读。task UUID canonical、固定PNG basename、客户端path无`..`且仅root/task/image两级；任务必须completed且有result path，OCR manifest success/ref_image_paths精确匹配task+image。POSIX dirfd/O_NOFOLLOW pin目录、fstat普通文件、PNG真实解码verify；非POSIX仅路径resolve/symlink检查。隐藏404、500不回显private path，nosniff。

fixture包括跨task同basename不授登记、伪PNG/FIFO、manifest/image/directory symlink与resolve后swap、未完成/未知task、image/PDF真实pipeline而外model响应stub；作者commit声明58 backend tests。本轮未run。**route无caller owner/auth检查；测试明确请求无authorization/cookie仍可读已登记crop，UUID不是租户授权。** 只支持阻止任意本地文件读取与任务产物身份检查，不支持跨租户机密隔离或所有平台race-free。

### A6 / UniRL #549：生成canvas和储存shape分离

精确merge必要patch已读：BAGEL adapter `_canvas_params/build/build_segment/build_conditions`、tracks.build_image_segment、diffusion.replay/predict_velocity、anchor.prepare_segment_anchors。canvas每frontier row从group元数据派生；同canvas连续run发一个GenerateCall；max latent tokens受default canvas约束；dense trajectory右padding、replay按实际packed token裁回。无field不改旧calls；其它engine明确reject row_canvas。

作者8×H20/BAGEL-7B-MoT/vLLM-Omni0.28/LoRA，16prompts×4samples、default1024、512/768/1024混合，正常replay layout相等，t2i first ratio4.6e-6/1e-5；rank max/mean长尾1.16–1.84。局部per-call timing非跨rank调度优化对照；512 under1024存4×trajectory bytes是token dense shape比，不是总训练内存benchmark。per-token sde_means anchor跨shape显式拒绝；直接消费segment.latents的算法也未泛化。未实现ragged储存、video、other engines或rank scheduler；本轮未run。

### A7 / OAC #704：有限retry不构成walltime期限

完整PR body和必要当前patch已读：Codex.options关闭unbounded_connection_retries，provider_config移未被生产赋值retry knobs；Claude.native_failure api_retry(status null)记录connectionRetry、任何model stream/assistant/result清signal；root error候选＋matching终态才commit classification；两fixture区分null/no-output与503或midstream；native Codex fixture要求0.153.4，在model-host.invalid/3min测试deadline下验connection_failed。

作者固定Codex0.153.4观察25.8/46.5s，Claude Code2.1.269/SDK0.3.269约176–201s，MiniMaxCode0.4.12 116s仍unclassified。版本事实为PR使用的pinned artifact，不是本项目建议；本轮未run。没有新Core timeout，slow response/300s stream idle不改；Codex没有connect timeout，silent SYN每attempt可等OS期限，不能把有限retry写保证1min/3min。Claude retry无parent_tool_use_id时child retry紧邻root error可能误归connection_failed；不支持无歧义多Agent因果分类。

## 5. 代表性排除与全部有限槽处置

只为普通项目完整核心筛选，不逐个修复深入；root复核含correctness/security信号样本时可定点重开。

- UniRL [#601](https://github.com/Tencent-Hunyuan/UniRL/pull/601)（merge ba3a113）、[#600](https://github.com/Tencent-Hunyuan/UniRL/pull/600)（65ea9f9）完整commit核心：typed字段直接访问、去silent exception/getattr fallback、system prompt resolver适配FSDP wrapper、移dead RMSNorm patch；显式坏contract不再吞错属局部既有契约修复，没有新增训练解释或对照边界。与548/596不同，不仅因fix标签EX。
- VeOmni [#1166](https://github.com/ByteDance-Seed/VeOmni/pull/1166)：完整PR body支持已有SAC/layer-granular checkpoint选项；20layer、ulysses2、full6.278→mix6.058（单位未披露）、150step total_loss表相同。硬件/显存/质量SLO/repeated timing未披露；不能仅此3.5%和引入已有SAC当新资源设计结论；无具体新失效或反证，EX。不是以少样本/小提升本身排除。
- MiMo-Code [#2661](https://github.com/XiaomiMiMo/MiMo-Code/pull/2661)（6ba6a625）：完整commit核心最后方案保Drizzle事务/migration ownership，只session.run接受精确duplicate/no-column/index-exists replay-safe no-op；早期startup ensure sidechannel撤回。不新增memory表示或Agent恢复协议，既有DB迁移幂等修复，EX；不可把撤回草稿当新实现。[#2659](https://github.com/XiaomiMiMo/MiMo-Code/pull/2659)（e27e87de）native Windows memory路径parse兼容，EX。
- OAC [#694](https://github.com/MiniMax-AI/OpenAgentCore/pull/694)完整body：由structured provider JSON error.code/type映射既有accepted code，不从prose推断；已有协议/code不变，duplicate terminal文案去重。[#708](https://github.com/MiniMax-AI/OpenAgentCore/pull/708)完整commit核心：后来的无码settlement error不覆盖旧classified code、有accepted新code仍覆盖。两者是既有诊断分类修复，没有新增可靠执行保证，EX；不可和704打包升分。
- OAC [#696](https://github.com/MiniMax-AI/OpenAgentCore/pull/696)完整body：runtime history改Core时钟named range、避免browser clock skew400、bucket交集和局部retry避免重复read；通用metrics读API修复，非Agent新state/evaluation机制，EX。
- OAC其余11槽：#703 upgrade后offer既有Runtime、#709手机隐藏reason、#707本地化错误、#702 UI leftover/既有Core lifecycle投影、#701词汇统一/移unused helpers、#706重试文案、#705名字wrap、#698手机table/tabs、#695健康capacity页面归属、#699错误next-step展示、#697管理员导览/配置变量名；逐完整commit核心均读，UI/文档或既有metadata组织不新增长期系统机制。加694/696/704/708＝15 EX。

root校准后最终有限26commit槽＝6准入事件＋20具体EX；准入6事件归**5唯一家族**（548/549合1、596、492、2618、254），其中254总4安全深入关闭。OAC15全EX，UniRL6＝4事件/3家族＋EX2，MiMo3＝1＋EX2，GLMOCR1＝1，VeOmni1＝EX1。无branch/merge重复槽；Source与Books仍须root独核，不把准入当采纳完成。

## 6. 本分支交接

- 本轮来源段、核心贡献筛选与上述必要原证已保存；root首批准入校准如上，必要Source/Books仍待独核/落实。若校准改变门槛，只重开受影响集合。
- 有限Source普通待办0；root浏览器若可恢复混元当前全部前缀则定点补该coverage段，不能因子任务限制声称零命中。MiMo无日期14Blog仍不支持完整覆盖。
- 未写Books/README/State/index；未运行作者测试/GPU实验，未stage/commit/push。root负责Books与fresh独核，其他已有/并发修改保留。

## 7. 具体Books比较与最小提案（仅source，不是已写）

已完整加载`PROJECT_CONTEXT`、`LEARNING_PHILOSOPHY`、`WRITING_GUIDE`，并读当日State与ROADMAP；以下实际owner段及两侧局部邻接、相邻chapter开篇职责已读。其他章节只交接，不复刻owner。

### 548＋549 / TRAIN-GRPO：建议已有覆盖 / No Change

实际[Ch33当前1620](../../../../../books/part-04-training-system/33-grpo.md)已用547解释同policy＋ratio≈1不认证conditioning，source-image变换、KV layout、canvas、replay自比与失配隔离全部明确；1606–1632邻接将该命题放在trajectory identity后/Objective-level actuator前。548提供新的检测实现与负例，强化而不反转原解释。549混canvas/存储padding是这个受限实现事件，尚无跨rank scheduler或新objective；建议报告列代码约束与开销，不为案例名另加正文。ratio warning触发在optimizer返回后尤其不能让正文变“强前置guard”。

### 596 / TRAIN-CHECKPOINT：具体缺口，最多一段

实际[Ch35当前177–193](../../../../../books/part-04-training-system/35-checkpoint.md)已要求global tensor dtype/layout及派生低精度model parameter从FP32main恢复；440–466发布身份与固定input logits验收也已有，但未明确**state_dict之外初始化计算的nonpersistent buffer**及meta-init/to_empty生命周期。建议放在177“保存global tensor identity...”之后、低精度恢复小节之前，不在章末追加：

> 参数与持久 buffer 的 dtype/shape 对齐仍可能漏掉初始化计算的非持久状态：例如 RoPE frequency 不在 checkpoint 的 state_dict 中，meta-init、整module cast、to_empty 与恢复若沿用当前低精度buffer，而非其已捕获的构造dtype，就可能在相同BF16权重下产生随位置增长的logprob偏移。恢复owner应区分持久参数状态与构造派生状态，保留后者的值、dtype和shape，在materialize后重建并用固定输入对照验证；UniRL的限定修正对Qwen3路径支持这一边界，不证明任意架构全部恢复等价。它增加构造态快照、copy与跨wrapper校验成本；无法重建或输出失配时，应回退已核的完整from_pretrained路径，不能仅由权重成功load批准policy一致。[原证](https://github.com/Tencent-Hunyuan/UniRL/pull/596)

### 492 / PLATFORM-GPU-SCHEDULER：具体数值资格缺口，最多一段

实际[Ch63当前154–189](../../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)已区分MIG/time-slicing/MPS/application batching，功率/HBM/时序与fatal fault domain合同完善；尚无fractional placement记账与MPS client active-thread配置的**输出数值资格**。建议在164共享机制表后、167 MIG容量折中之前插一段：

> Fractional GPU额度只为placement记账，不等于执行资源隔离；MPS并发资格还必须绑定scorer实际forward batch、dtype、GPU/driver与client active-thread设置，分别验输出和共置收益。UniRL作者的H20/535.247.01限定实验中，轻量scorer有局部并发收益，OCR瓶颈和较小native batch也可零收益或变慢，而低于100% active-thread的半精度结果既可非有限也可有限但错误；因此无NaN与低util都不能自签共享合格。当前merge只给100%的配置建议、没有相应dtype/scorer硬guard，不能据PR正文宣称限制已执行。逐配置parity、warm-up、共置对照和故障恢复都有成本；版本、负载或输出资格未知时应保留原分配、100%已核profile或独占，不把作者局部结果外推为通用MPS收益/安全。[原证](https://github.com/Tencent-Hunyuan/UniRL/pull/492)

### 254 / PLATFORM-SECURITY：建议仅报告关闭，不强制新增正文

4分实际是下载组件安全修正，不升级通用授权设计。实际[Ch72当前29–33](../../../../../books/part-06-ai-infrastructure/72-security.md)已明确普通数据API可达敏感资产、目录名不是访问控制；1768–1785已区分typed/canonical path、真实runtime/symlink检查及最终文件授权。254只是task manifest身份allowlist的新具体实例，不证明caller/tenant授权（fixture无auth）。建议仅报告该当窗安全行为、兼容PNG preview和上述未覆盖边界；不以“已有覆盖”假称书中已经有completed-task manifest算法，也不为案例名新加长段。

### 2618 / AGENT-WORKFLOW：具体Stop结算缺口，最多一段

实际[Ch81当前1211–1219](../../../../../books/part-07-agent/81-workflow.md)已区分effect ledger/state、at-least-once、explicitresume权限；1249–1258解释scope owner取消但未明确**收到abort与真实async result settle/释放运行权**的排序。建议在1211后、旁路问答1213之前插一段，并由原cancellation段交接不复制：

> 同进程Stop也必须区分取消请求与工具真实退出：先关闭新调用准入，向已started异步工具发abort，再等待并持久化其可观察结果，最后释放turn运行权；已经完成的文件写入不会因Stop被回滚。MiMo-Code的限定实现用started/未started标记与完整input boundary区分可删除的未执行尾部，在恢复准入时重验确切目标、保留已完成tool结果，并检查真实模型输入中的call/result配对。它增加结果登记、等待和恢复验证成本；不响应abort且不settle的工具仍可让Stop无限等，process crash后的外部副作用也未与本地记录原子提交。因此本地受限fixture中的写入只一次，不认证开放远端工具exactly-once；结果未知时仍应核postcondition/idempotency或转人工，而非用取消状态直接批准重放。[原证](https://github.com/XiaomiMiMo/MiMo-Code/pull/2618)

这些提案是作者Source/owner比较，不是PRE批准或Books已整合；由root独立比较和窄写决定，实际写后另复核。

## 8. 最终校准交接（2026-10-15）

此前七拟事件轨迹保留，但最终不沿用七候选计数：root首批校准与2618当前连接器body独核后，**5唯一家族**为548＋549、596、492、2618、254，分分别**6 / 5 / 6 / 5 / 4**；704贡献前EX、不评分。548/549为同BAGEL rollout/replay条件家族的两个当窗实现事件，不另计家族、不叠加分数。254是当窗安全受影响深入、单组件4分关闭/仅报告边界，不宣称UUID或completed status授caller授权。

本子任务有限Source普通余项0，必要原证/核心反侧/具体owner比较已保存；建议548/549已有覆盖，596/492/2618各仅必要一段差额提案，254仅报告。Hunyuan官方Research日段与MiMo14无日期Blog目录是明确隔离的来源保留项，不支撑覆盖通过、零论文或无遗漏；不是把未尝试普通项当外部。root承接Source独核、Books决定/必要实际窄写及写后复核、报告DAY/FINAL。本子任务到此退出，不创建后日、Weekly或历史任务。

Root报告评分明确：2618最终为2+1+2=5，重要恢复接口变化但仅单Workflow运行组件，不借通用取消原则扩大System Reach；前文初拟1+2+2轨迹不作最终维度。总分及深入审阅不变。
