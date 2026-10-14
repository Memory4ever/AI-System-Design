# 2026-10-13：机构六项独立证据审阅与 Books 比较

窗口：**2026-10-12 ～ 2026-10-12，北京时间完整自然日**。复核者：`today_institutions`（非机构来源记录作者、非 Daily 作者）。必要 Source/Books 比较执行于 2026-10-13 11:16～11:43 BJT；后续落实与日级验收另记。

启动完整重读当前 AGENTS、Research/Report 合同、来源使用说明与每日组、Prompt、ROADMAP、Books 三份方法文件及本日停点。复用 [global-sources](global-sources.md) / [china-sources](china-sources.md) 的有效有限发现层，不重扫机构目录，不恢复历史/Weekly。主张以本轮直接 primary 为准，来源作者笔记只作路由。既有 staged/unstaged 变更保留；本记录不代表已写 Books 或整日报已通过。

## 1. 六个家族的实际结论

| 家族/事件 | 日期与精确版本 | 实际新增评分 | Source 与 Books 比较 |
| --- | --- | --- | --- |
| Anthropic self-replicating-ai | 官方页 `2026-10-12` | 2 + 2 + 2 = 6 | 受影响安全边界深入完成；`PLATFORM-SECURITY` 实际整合，root非writer POST通过 |
| Anthropic distillation-defenses | 官方页 `2026-10-12`；公开措施含更早实施时间，不能重记措施首次事件 | 2 + 2 + 2 = 6 | reasoning 消费接口深入完成；`PLATFORM-SECURITY` 具体已有覆盖，No Change |
| Qwen Code PR13674 | merged `2026-10-11T16:06:51Z`＝10-12 BJT；`a8990042e648a7807e251d99b3d37c0ee8c16100` | 1 + 2 + 2 = 5 | admission/approval/恢复及 internal policy 受影响实现深入完成；唯一 `AGENT-PLATFORM` 实际整合，root非writer POST通过 |
| UniRL PR583 | merged `2026-10-12T06:03:31Z`；`279298dc8aa9d3a727c015fcf10fc0da90613871` | 2 + 1 + 2 = 5 | 为实际allocator长期缺口进一步深入完成；`TRAIN-DISTRIBUTED-TRAINING` 实际整合，root非writer POST通过，不另写 Ch54 |
| MiMo-Code PR2650 | merged `2026-10-12T13:52:22Z`；`8e1df4abee56da60c11db14606dd855823b1a29f` | 1 + 2 + 2 = 5 | containment authority 的受影响实现深入完成；`PLATFORM-SECURITY` 实际整合，root非writer POST通过 |
| OpenAgentCore PR667 / release 家族 | merged `2026-10-12T04:16:48Z`；`48292f409a042e2b8bb8588c87e1e1a7004dc867`；v0.0.10/11 本窗发布载体不重复评分 | 2 + 2 + 2 = 6 | exact-incarnation cleanup 与 continuation 资格深入完成；`AGENT-PLATFORM` 实际整合，root非writer POST通过 |

评分仅针对实际新增命题：局部实现可具有跨 boundary 的稳定反例，但不借成熟的 least privilege、幂等、版本一致性或模型名升分。安全深入只覆盖真实受影响机制，不遍历全 release/PR 历史。六项均未复现实验或接受生产运行。

## 2. Anthropic：部署可行性不等于闭环自主复制

Primary：[AI models may be capable of self-replicating without access to a datacenter](https://www.anthropic.com/research/self-replicating-ai)。直接读 Introduction/Threat modelling、A/B、C/D 的必要评价与反侧、G、Appendix A～C/F；官方页日期 Oct12、William Zhou / Daniel Freeman。网页正文与必要附录可读，嵌入图只是作者证据，没有实际运行图表实验。

关键位置 A 的异构 inference standup、B 的八节点 redroid 试验和 floor/ceiling、Appendix C 的 context/memory/流水气泡、F 的去除 inference 步骤 ablation。实物 15×4GB Android boxes 部署 Gemma4-26B-A4B，与 GLM5.2 外部推理、部署 Llama3.1-8B 的 emulator 链条是两种实验，不得拼为同一模型真实自复制。后者 5 次仅证明简化访问条件下的组合能力；作者明确尚无 full rogue replicator，当前 capability floor 与 size ceiling 不相交。32K budget、4-bit weights/FP8 KV、低并发和长轨迹时间限制部署，不采用 ECI 年末预测或 H100-equivalent 外推。

Memento 为 workspace/短 notes 的跨 instance 继承；六代20 lineages 的局部改进不授一般 memory/反思新原则，不增加第二 Books owner。strong advisor 无显著帮助只在该任务与设置下成立。完整 controller/scaffold、运行重复的全部配置和正式 field risk 分母 `Not Disclosed`；未经验证的现实网络 exploitation 不作正面证据。

准入：现有风险评价分阶段，但可能把部署/组合两种分别成立的试验拼成自主复制已成立 → 本文提供明确没有相交的能力/资源边界及外部推理反侧 → 安全评价应单独验证同模型、同资源条件下的闭环。`2+2+2=6` 针对这项界限，非新 PP 原理。

Books 实际比较：Ch72「生命周期威胁」现有 data/training/artifact/serving/action 风险及 n-day activation 窗口；「Safety Evaluation 的单位是 Run」和「Containment 不能只看最终是否发生攻击」已拥有分阶段效果与 trace，但没有 joint capability/resource eligibility。拟在生命周期威胁的层间 identity 段后加入 §8-A1 最小正文；Ch71 tenant identity → Ch72 security → Ch73 release 的交接保持，不改第10章预测或 Ch77 memory。

## 3. Anthropic：reasoning 消费授权已有具体 owner

Primary：[Strengthening our defenses against distillation attacks](https://www.anthropic.com/research/distillation-defenses)，官方 Oct12。web 提取失败后一次真实 HTTP200 的 article 内容读完：Simple defenses、Our new methods、How well、trade-offs、platform boundary；不是搜索摘要。无当前撤回/纠错标记。

关键增量是 reasoning artifact 的可消费域：新账户 prior-context 编辑限制、强模型到弱模型的读取限制、Sonnet5.5 的原 organization 约束；两阶段 classifier 与限速/封号/重复请求成本共同承担 abuse 防线。既有措施日期 August31/September24 不能当10-12首次上线；本窗为新官方合并说明与作者观察。FPR<0.1%、平台提取量降10～100倍和 full/summarized SWE-bench80.4/71.8只保留厂商口径，不用作独立因果/永久安全保证。数据分母、完整训练预算、FPR估计协议和前后混杂控制 `Not Disclosed`，尚未见高度持久复杂绕过；正常迁移、误拒与拒绝计费都是真实代价。

评分 `2+2+2=6` 针对明确的跨模型/组织消费与 repeated attempt boundary，不因 Books 已有覆盖降分。无必要中心外部证据缺失；未公开 classifier 权重不阻塞受限定公开接口命题，也不补造机制。

**No Change：** 唯一 `PLATFORM-SECURITY`，具体 [Ch72 Hidden Reasoning Trace](../../../../../books/part-06-ai-infrastructure/72-security.md#hidden-reasoning-trace-不是-secrecy-boundary) 中原文已明确：「另一个用户、workspace、组织、会话或 model family」消费需另授权；artifact admission 与 output release/hold 分责，传输保密和隐藏界面不能替代授权，并保留 compaction/迁移、延迟/缓冲/误拒与跨提供方路径未验收。这是同一设计命题，不只是同主题。新增 account classifier 与计费实施事实仅报告，不需要产品专名/每个组织复制成新段。Ch75只消费provider接口，不接管安全owner。

## 4. Qwen Code：新准入与旧回执/收尾不能共用开关

Primary：[PR13674](https://github.com/QwenLM/qwen-code/pull/13674)、[API身份](https://api.github.com/repos/QwenLM/qwen-code/pulls/13674)、[精确合并 patch](https://api.github.com/repos/QwenLM/qwen-code/commits/a8990042e648a7807e251d99b3d37c0ee8c16100)。本轮直接读完整 What/Why/Test/Risk，affected Store/Service/Properties/Compiler/Harness/profile patch、internal admission设计和两个实际新增 admission test 文件。PR creation10-08不搬入10-12；采用合并/接口事件，nightly是载体。

精确位置：`ManagedAgentStore.insertWorkspaceSessionCommand` 在原key replay之后拒绝新的 Shell initial input；`insertTurnCommand` 先返回原命令回执再门禁 fresh work。public foreground 必须 default/auto-edit、public Shell 仅 owner回答 Action，child suppression 是另一条持久 Harness事实。`insertInternalTeamLeadSessionCommand` 固定 reserved profile 且要求原Workspace执行前提；`replayWorkspaceCommand` 公有/内部 policy-kind 不匹配拒绝，`AgentDefinitionCompiler` 即使allowlist含保留值仍拒绝。未知profile和旧reader不能退化为files。

直接反侧：关Shell不等关闭已受理的approval/cancel/settlement；更不等物理worker已静默。空definition绑定和已接受key重放不是新执行许可。新tests覆盖 fresh初始input/turn零新行、公有/内部key碰撞、profile/revision/digest保留；作者H2/macOS controlled-model进程与特定Linux/MySQL CI证据，仍有CLI661/663未消除的异步夹具限制。不是本轮运行；物理quiescence、signed-auth/CSI、Windows、完整G3/L4、background/Monitor未资格通过，默认off不变。旧1062项不可继承给最后head。

贡献 `1+2+2=5`：新增的是 public runtime interface 上 admission 与既有事务收尾的分离及 reserved policy provenance 实现，非一般幂等原则。安全深入受影响content已足够，不把整个新版本开发史送审。

Books 比较：Ch84「Agent Definition 与 Run Identity」已有固定definition；「Resume」已有外部effect对账、Policy持续授权；「Workspace」已有生命周期隔离。未明确禁新执行与允许原key回执/合资格收尾的两条不同路径，也未写公开allowlist无法mint内部policy；拟 §8-Q1 两段插在Workspace隔离节结尾、三个平面之前。唯一 `AGENT-PLATFORM`，不复制至Ch72。

## 5. UniRL：all-gather 等待可能来自 allocator retry，而非通信字节

Primary：[PR583](https://github.com/Tencent-Hunyuan/UniRL/pull/583)、[精确 merge](https://api.github.com/repos/Tencent-Hunyuan/UniRL/commits/279298dc8aa9d3a727c015fcf10fc0da90613871)。直接读全文 Summary/Test/Risk/Reviewer Notes、全部六 affected patches。`FSDPBackend.__init__` 在 wrapping前追加 env 原配置再调用 `_set_allocator_settings`；config default false，H3 trainside true、2×8HSDP validation false、VeOmni明确拒绝。

证据限定 1×8H20、torch2.13.0+cu130、MiniMax-H3 t2va trainside、128samples/step=8prompts×16、256×384×124、BF16运行/fp32 LoRA masters、无allocator env。作者 main两run18steps 与新两run×3rollouts，train1177→1078～1096s、step1624→1513～1550s、retry降0；local phase timer没有提交，误差/置信区间 `Not Disclosed`。8GPU FSDP2 microbench的 gather bytes不随masters dtype变化，不能把11%都当通信量改善；no-grad anchor与optimizer不变。

**实际反侧必须同文保留：** 同code另一main报告缺env/retry，launch环境可能决定有无病理；`max_split_size_mb:512`与expandable并用作者step3263s，约2×变慢。开关process-wide；SGLang可重设；共享worker的CUDA IPC weight sync未validate；早期全trainer guard已撤，不采用。原key保留只证明未丢原配置，不证明组合更快。非matching veRL配置下不采用框架优劣排名，未复现本轮GPU。

评分 `2+1+2=5` 只针对受限诊断反例与runtime-policy边界。Books owner `TRAIN-DISTRIBUTED-TRAINING`：Ch36已有临时/communication buffers、overlap资源竞争和数据就绪/存储回收不同completion，但未区分同bytes的allocator recycle/sync病理或process-wide策略。Ch54 §Fragmentation/Reserve仍有效背景，不重复写。拟 §8-U1 接在Ch36「单卡为什么会失败」最后判断后、IPC开始前，一段保留实测反侧和低压/兼容分支；Ch35恢复identity与Ch37 TP交接不改。

实际审阅不止标准评分：识别Ch36长期机制缺口后，进一步完整核六affected patch的调用位置、env原key保留、process-wide修改、default-false及VeOmni拒绝/另一HSDP负侧；把同bytes microbench、另一main报告缺allocator状态、`max_split_size_mb:512`组合退化与共享rollout/IPC未验逐项对齐。root独立核同六patch与owner/完整邻接，再实际非writer POST。这些必要实现与直接反证足以支撑已写的条件性allocator归因和共存边界；不支撑普适降时、框架排名、IPC兼容或GPU复现。审阅层据实际工作记为「为实际allocator长期缺口进一步深入完成」，分数仍5，不因深入升分。

## 6. MiMo-Code：跨卷 absolute relative 不能取得 containment authority

Primary：[PR2650](https://github.com/XiaomiMiMo/MiMo-Code/pull/2650)、[merge原件](https://api.github.com/repos/XiaomiMiMo/MiMo-Code/commits/8e1df4abee56da60c11db14606dd855823b1a29f)。直接读完整原说明、两实现和三个新增test patch。CLI `Filesystem.contains` / shared `AppFileSystem.contains`（约L164/L233）将 `!relative().startsWith(..)` 改为同时拒host与win32 absolute；overlaps调用两向contains，不加test-only win32 routing。

跨drive/UNC的 `path.relative` 返回目标absolute而非`..`，旧否定条件会fail-open给workspace/tool-script/server cwd/plugin resolution的共有jail。新逻辑关闭此具体通路。**POSIX新增test旧实现也通过**，作者win32-relative local实验只证明两predicate对这些输入不同，不是本轮真实Windows acceptance；没有所有symlink/TOCTOU与所有consumer都安全的证明。不把Bun宿主/cron普通fix拼成一项分数。

评分 `1+2+2=5` 针对明确的多consumer authority反例。Books Ch72「Canonical Action 与 Effect-time Authorization」已有symlink/path resolution仍需runtime check，但没有relative不是containment证书的跨平台反侧。拟 §8-M1 单段接在该runtime-check段后、后续authorizer论证之前。唯一 `PLATFORM-SECURITY`，没有新MCP协议/AgentPlatform owner。

## 7. OpenAgentCore：只有 qualified compute loss 才能 release writer

Primary：[PR667](https://github.com/MiniMax-AI/OpenAgentCore/pull/667)、[merge](https://api.github.com/repos/MiniMax-AI/OpenAgentCore/commits/48292f409a042e2b8bb8588c87e1e1a7004dc867)。直接读原core、docs `Confirmed compute loss`/cold replacement边界、`runtime_compute.go` 的 `idleCompute`/`releaseLostCompute`、deployment `ReleaseLostCompute`/cleanup、SandboxProvider语义、positive/negative/concurrent test受影响部分。release v0.0.10/11日期复用原API身份，无需重扫所有release。

online owning-node的exact-incarnation ErrNotFound/verified stopped/crashed不是一般heartbeat断联。实现需settled running create、有nativeID、无capture/restore/rollback、无authenticated Runtime connection、retained native continuation资格；lease ownership后Kill exact compute，只有confirmed cleanup才Session-lock内检查same compute revision/retainability并revoke device/release allocation。Session、native ID、filesystem和pending input保留，不replay已完成或中断input。

直接negative：paused、running-without-peer、node unavailable、timeout、foreign ID、unknown Create、owned workspace、初始化未完、native_history未声明、live peer、cleanup失败都不能释放。SQL/WS tests是deterministic provider fixture而非native evidence；kill后revision/归档/删除竞争须失败，取消到release前仍保持ownership。作者native microsandbox/NFS Codex/Claude idle/mid-turn/post-ack VM-loss与physical delete验收只限其场景。host-crash durability、任意crash-tail完整性不qualified；可解析但截断history尾不能被ID检查发现，缺history不创建新native root。必要非通用吞吐指标不适用，全面故障率/原生运行样本量 `Not Disclosed`。v0.0.10当前建议v0.0.11，fresh installation而非跨release原地migration，不推荐缺陷旧版。

评分 `2+2+2=6` 对新合资格loss→release→retained continuation路径，非借普遍fencing成熟原则。Ch84「Resume」已有外部effect/identity验证和不可重放，Workspace有release/destroy，但没有明确 offline≠lost，exactcleanup与锁内revision/retainability共同授释放资格。拟 §8-O1 两段接Resume general transition段后、stop controller之前。唯一 `AGENT-PLATFORM`，Ch72只交接权限，不再复制。

## 8. 最小 PRE 文本与实际窄写（root非writer POST通过）

以下五份PRE由root实际核必要primary、三个owner及邻接后通过，并授仅对应正文与本人末注的窄ownership。today_institutions已逐字落实（U1耗时表达按root修为「约为原耗时两倍」），写后顺读并检查限定diff。root随后实际完整读diff正文/上下文及五本人末注，确认两IoT实验未拼闭环、MiMo跨卷非symlink保证、UniRL反侧/processscope、Qwenfresh/replay与OAC锁/revision/资格，非writer POST通过；本人末注已同步并读回，Ch72/84/36窄锁释放。

### A1 — Ch72：生命周期威胁，层间 identity 段后

自主复制的风险还要把三份资格放到同一条链上：Agent 能完成目标发现、部署与继续传播；模型能在目标硬件的内存、上下文和通信预算内运行；新副本确实由该目标计算资源继续驱动。分别展示这些步骤，不能拼成完整闭环。受控 inference standup 适合定位长程部署失败，却不能由另一台服务器承担 controller 推理，再把服务较小模型的成功记成 controller 已在目标上复制。<!-- source-family:SF-2026-ANTHROPIC-SELF-REPLICATING-AI -->

[受限IoT评价](https://www.anthropic.com/research/self-replicating-ai)同时给出小模型的部署可行性与更强模型的组合能力，但当前能力floor和目标设备size ceiling尚未相交，简化访问条件也不是现实入侵验收。安全owner应保留这两条独立证据及尚未相交的区域，再由目标环境验证同模型闭环；PP分片能扩容量，却增加节点故障、KV重建、流水气泡和低并发成本。上下文/资源或真实访问前提不足时，保持风险为未决并收窄运行权限，不能用趋势预测给自主复制签发已成立结论。

### Q1 — Ch84：Workspace 结尾、三个平面前

部署开关还须区分新执行准入与已受理工作的回执、取消和收尾。关闭高风险Shell可以拒绝fresh初始输入和后续Turn，但原幂等key应先找回既有决定，合资格的approval/cancel/settlement仍沿原授权处理，不能为阻止新工作而遗失旧状态。固定definition的profile、approval、revision与digest不由新默认覆盖；公有和可信内部执行policy若共享入口，重放也必须核对policy-kind，公开allowlist不能自行mint内部身份。<!-- source-family:SF-2026-QWEN-CODE-13674 -->

这增加reader升级、持久policy和跨层negative controls的成本；禁止fresh work不证明旧worker物理静默，更不授权新的background、child或lifecycle能力。[Qwen Code的受限公开Shell切片](https://github.com/QwenLM/qwen-code/pull/13674)保持默认off、强制询问审批与内部profile隔离，其H2/特定CI证据不覆盖Windows、物理恢复或完整生命周期。前提不齐时保持未开放并允许合资格收尾，不把一次界面能力标志当作全链执行验收。

### U1 — Ch36：单卡失败判断后

接近容量上限时，collective等待还可能来自分配器，而不是更多通信字节：大all-gather临时buffer找不到合适cached segment，可能触发cache回收、重试和device sync。因而应把allocation retry、实际buffer字节与各训练阶段时间一起观测，不由master dtype或collective timer独自归因。进程级expandable-segment策略可以改善某个trainside负载，却必须保留启动配置并检验共享rollout/IPC的兼容性；保留key不等于组合性能更好。[UniRL的H3/1×8H20受限对照](https://github.com/Tencent-Hunyuan/UniRL/pull/583)中，retry消失伴随局部降时，但与`max_split_size_mb:512`组合的耗时反而约为原耗时两倍，另一同代码报告还缺allocator状态。无retry、兼容前提未验或共享引擎会重设策略时，原分配模式仍成立；不要用版本开关替代匹配环境的端到端测量。<!-- source-family:SF-2026-UNIRL-583 -->

### M1 — Ch72：Canonical Action 的 runtime-check 段后

路径的规范表示也不自动给出containment证书：在Windows跨drive或UNC share时，`relative(parent,child)`可能返回absolute目标而不是`..`，因此“结果不以`..`开头”会fail-open。共用workspace、tool-script和plugin jail的predicate应拒绝absolute结果，再按实际consumer执行path/symlink检查，不能把字符串相对关系当最终文件授权。[MiMo-Code的具体修正](https://github.com/XiaomiMiMo/MiMo-Code/pull/2650)只关闭该跨卷路径；POSIX绿测在旧实现也成立，不能继承为真实Windows修复验收或所有symlink/TOCTOU安全。新增平台negative tests与调用链核验有成本；无法验证解析/执行一致性时应拒绝越界路径，而非由一个通用helper签发完整sandbox保证。<!-- source-family:SF-2026-MIMO-CODE-2650 -->

### O1 — Ch84：Resume general transition段后、stop controller前

恢复compute前还要区分“看不到writer”与“已确认旧incarnation终止”。Node离线、daemon断开、paused VM或unknown observation不能授权replacement；拥有该compute的节点重新在线后，只有证明exact incarnation不存在或已终止、exact cleanup成功且保留的Session可继续，才进入release。Device撤权、allocation/placement释放与retainability应在Session lock中复核compute revision；并发archive、delete或新的compute transition优先，不能让旧观察覆盖新状态。<!-- source-family:SF-2026-OPENAGENTCORE-667 -->

这种qualified recovery减少永久owned的废弃compute，却增加provider语义、lease、锁顺序和native-history验证成本。[OpenAgentCore的受限实现](https://github.com/MiniMax-AI/OpenAgentCore/pull/667)保留filesystem、native ID和pending input，并不重放旧输入；缺history须显式失败，不能悄悄创建新native root。其VM-loss验收不证明host-crash持久性或任意crash-tail完整，ID相同也检不出可解析的截断尾。不能取得上述资格时继续保留ownership、隔离或人工恢复，不能用超时或新容器可启动替代旧writer已被安全释放。

## 9. 当前剩余

- 六项必要 Source 和具体 Books 比较完成；distillation为具体NC。root的必要Source/PRE独核已通过，五处实际整合由root真实非writer POST通过；本人末注已同步，三owner窄锁释放。机构六项为5整合+1已有覆盖，不是整日报终态。
- 机构特殊排除项与ordinary分层抽检已完成，具体范围以§10为准；新增九项证据/owner及实际九窄写均已完成，root实际非writer POST通过，六窄锁释放，见§11–12。DAY准备又将13348由旧EX实际core改判准入、root具体NC独核通过，见§13；本人16家族终态为14实际整合+2具体已有覆盖。没有assigned未读源或未写Books，唯全日报source范围/全部候选与特殊negative/普通EX分层及六部分验收待root报告齐备后归并，不能提前日级通过。
- 机构目录的精确外部保留项继续由两个source文件承担，不授无遗漏或完整Coverage；普通可执行Books/DAY待办不改为外部受阻。

## 10. 机构排除项独立校准：具体 signal 与 ordinary 样本

非来源记录作者在上述六候选外直接打开以下原件；不依赖source笔记代读。审阅深度按具体新增命题决定：存在真实bug不等于有新的长期贡献，已恢复的成熟不变量不重新捆repo家族。下面14组/16事件为具名安全、正确性、测量纠错或兼容信号的实际核查范围，**不是34个窄commit全部代码审计**。

| 特殊排除信号/原件 | 实际primary阅读与限定结论 |
| --- | --- |
| [MoonEP33](https://github.com/MoonshotAI/MoonEP/pull/33) | 完整PR/core和exact `d86fda4`唯一`buffer.py`四error-path patch。SCM_RIGHTS fd与socket不同owner，export fd pin allocation、multicast handle失败回收属成熟shareable ownership恢复；作者仅py_compile/代码审读、无NVLink错误路径执行。不支持新通信/资源保证，EX不评分。 |
| [Kimi4184](https://github.com/MoonshotAI/kimi-code/pull/4184) | 完整Why/behavior/core、exact `cbd7540`两schema patch。保executor字段只收窄enum，避免unknown-key stripping静默local执行；整文件CONFIG_INVALID与SDK移除迁移成本都保留。未可用backend退出、不是新能力或新的authorizer，EX。 |
| [Kimi4183](https://github.com/MoonshotAI/kimi-code/pull/4183) | 直接完整PR/core/behavior/test范围：ctx已有AbortSignal却未传实际上传，补signal及取消后rethrow、禁止inline fallback；ordinary upload错误仍fallback。既有Esc合同落地，非新取消协议；作者真实挂起HTTP/engine不称本轮执行，EX。 |
| [Kimi4182](https://github.com/MoonshotAI/kimi-code/pull/4182) | 直接完整PR/core/behavior：已有user-requested stopped/closed/lock-release，foreground漏观察closed；新增terminal状态与normal shutdown wiring，embedded kap-server仍可重开。恢复既有终态合同，非新生命周期机制或全服务quiescence证明，EX。 |
| [UniRL582](https://github.com/Tencent-Hunyuan/UniRL/pull/582) | 完整core/作者各版本测试与撤回说明、batch.py全部changed helper/CFG split受影响patch。SHARED proxy仅shape/dtype、非batched CONCAT tensor仍item0、旧pytree_chunk不新增guard；最终merge未重跑全部GPU。恢复实际row/CFG容器不变量，不借fail-closed原则升为新机制，EX。 |
| [UniRL554](https://github.com/Tencent-Hunyuan/UniRL/pull/554) | 完整core与exactdocspatch：旧BAGEL overlap未重测；4902→1227 prefill改变不能推算新overlap。实际Ch33:1572/3190已采用#547 conditioning/KV身份反侧，明确不把修复前后时延当一般收益，未含旧127.5/111.6等数字；无受影响旧收益claim须改，EX不新造benchmark。 |
| [OpenAgentCore681](https://github.com/MiniMax-AI/OpenAgentCore/pull/681) | 完整core、exactpublisher/render-compose/template/test patch：all three defaults用publisher immutable digest，preserve override；测试是rendering/mockpublisher而非本轮docker部署。恢复named-release composition一致性，不新增模型/Agent机制，EX。 |
| [ZCode CSP](https://github.com/zai-org/zcode-plugins/commit/d8bd5dd997c40b5e5d1c73102657fc712d09a6cb) | exact resources/bootstrap/docs及strictCSP fixture core；wasmUnsafeEval/unsafeEval仅panel资源，非Agent eval工具。startup completion撤listeners、防后续error误报；fixture不替代desktop partition/origin。权限声明与UI启动修复不是新增hardening成果，EX。 |
| [MiMo2645](https://github.com/XiaomiMiMo/MiMo-Code/pull/2645) + [Bun capability follow-up](https://github.com/XiaomiMiMo/MiMo-Code/commit/4fb57c5648d2ca4f5a0599f3492368537460cd13) | 完整PR/core及follow-up exactcode/spec/real-Node fixture。探`Bun.plugin`而非global名称，Node/partialBun退config-only；旧node_modules不删除，显式npm安装路径仍在。host统一既有SDK/适配能力门禁，不借supplied-runtime原则再评分；真正跨drive新命题已单独MiMo2650，EX。 |
| MiMo测试隔离 [2649](https://github.com/XiaomiMiMo/MiMo-Code/commit/c68463f28dd6d27ee42d2739322029bc75274e00) / [2651](https://github.com/XiaomiMiMo/MiMo-Code/commit/ca056a8ee4b05b64930e2bfe921738872eb64647) | 两exact完整patch/core：先nonexistent root guard，后允许script并preload disposable env+阻packages tests；不是本轮运行，更不是Agent runtime新隔离机制。真实防写生产db/testing约束保留，EX。 |
| [VeOmni1274](https://github.com/ByteDance-Seed/VeOmni/pull/1274) | 完整core/test及shared converter完整patch。#1273既有per-expert机制扩三model，拒未经scale的FP8避免静默cast；DeepSeekV3仅BF16、V4 FP4未支持。CPU210/stubEP不是全GPUIO/训练收益；恢复已存在format/scale契约，无新泛化design命题，EX。 |
| [VeOmni1248](https://github.com/ByteDance-Seed/VeOmni/pull/1248) | 完整core/2GPUmodule与2×L4full-model输出/gradient条件。text/image各自reverse scatter恢复本stream shard，非#1246padding新机制；真实bug/test不授其他jointattention统一保证，EX。 |
| [VeOmni1261](https://github.com/ByteDance-Seed/VeOmni/pull/1261) | 完整core/repro及dataset.py affectedpatch。HF自己按worker分source，再按同worker过滤漏行；deepcopy把sharedepoch race改为worker-private。48row/realDataLoader/parquetRepeat作者CPU条件、无training/分布式launch。修成熟独占partition/epoch状态，EX不把模型训练增益虚构。 |
| [VeOmni1282](https://github.com/ByteDance-Seed/VeOmni/pull/1282) | 完整官方core：name替换非可逆，用checkpointindex的load-map求逆；不与1274拼FP4支持，恢复export命名正确性，EX。 |

ordinary 分层抽检7项/7来源，完整读官方core及直接限制：Qwen [13909](https://github.com/QwenLM/qwen-code/pull/13909) adapter列表空、无broker/producer；Moonshot [MoonEP10](https://github.com/MoonshotAI/MoonEP/pull/10) physicalSM conservative bound不是occupancy证明；Hunyuan [UniRL586](https://github.com/Tencent-Hunyuan/UniRL/pull/586) 删除已过时hydration，无GPU真实NCCL/step-time、HI3ragged仍部分driverhydration；Seed [VeOmni1278](https://github.com/ByteDance-Seed/VeOmni/pull/1278) 传统filesystem返回值/exit-code恢复；Z.ai [UI插件README与构建合同](https://github.com/zai-org/zcode-plugins/blob/d1639cff514dcba29cfbfbc634d4609492640660/docs/MCP_APP_BUILD.md) 官方SDK应用组合与构建/安装分层，不代表新协议保证；MiMo [cron2648](https://github.com/XiaomiMiMo/MiMo-Code/pull/2648) 修既有creator-session routing、legacy fallback；MiniMax [CLI282](https://github.com/MiniMax-AI/cli/pull/282) nativeYAML集成与preview默认，explicit/savedmodel和availability边界不改模型机制。该样本没有发现共同准入误判，不扩无关PR历史。

追加ordinary两样本：Kimi [4092](https://github.com/MoonshotAI/kimi-code/pull/4092)直接完整core/behavior，headers-only变量仍受SDK10min总timeout，SOCKS与google-genai未支持；既有HTTP client参数接线，非新推理机制。arXiv [12970 Minions exact-v1](https://arxiv.org/html/2610.12970v1)直接§2–3及§4：REST pull/DB unique acquirement/heartbeat-watchdog重排/host preference是成熟工作队列的闲置Mac组合，无改变状态交付或重复执行边界的机制/可比反证，不因mapping准入，也不授zero-cost/exactly-once。总ordinary实际9样本/8来源分层（上方7项/7机构+Kimi同源1+arXiv1），未独读其余普通EX题摘/全部代码。

没有独立重读每个普通EX（其余sample尺寸、UI显示、releasewiring等），也未将上述code静态审阅称为作者测试的独立执行。source文件中的完整身份/日期/具体理由保持，DAY复核按此真实范围披露。

## 11. 当日补检九项：独立准入与必要证据

仅这九项，不接12970。完整精确v1题摘已逐项读，保存在`runtime-discovery-abstracts.json`；以下准入基于具体新增贡献，而非关键词路由。直接核官方`recent`的Mon12 day/name：cs.DC [3]13474/[11]13003/[15]13408/[18]12815；cs.PL [1]13679；cs.LG [24]13735/[59]13328；cs.CL [70]12570/[72]12545。官方入口：[DC](https://arxiv.org/list/cs.DC/recent?show=2000&skip=0)、[PL](https://arxiv.org/list/cs.PL/recent?show=2000&skip=0)、[LG](https://arxiv.org/list/cs.LG/recent?show=2000&skip=0)、[CL](https://arxiv.org/list/cs.CL/recent?show=2000&skip=0)。不是将10月8/9 submission改为公开日，未见withdrawn/correction。未宣称其余全部GPU论文纳入。

| Source family/exact version | 具体准入增量 | 真实评分/审阅 | 唯一owner与实际局部缺口 |
| --- | --- | --- | --- |
| SF-2026-ARXIV-2610-13474 / v1 CompileMask | 静态mask结构分析与动态metadata端点生成分开；定长interval执行descriptor而非predicate逐element检查 | 2+2+2=6；受影响机制深入 | INFER-TENSORRT-LLM Ch49，FlashAttention末Tessera→Heterogeneous Batch之间；已有retile不覆盖结构bounded interval编译 |
| SF-2026-ARXIV-2610-13679 / v1 Layout Algebra | logical/thread/physical typed空间与compose后restriction，合法general map不强迫affine | 2+2+2=6；kernel correctness受影响深入 | INFER-TENSORRT-LLM Ch49，Lowering commit起始段→RVV之间；已有typed commit没有broadcast读写及restriction准入 |
| SF-2026-ARXIV-2610-13735 / v1 Orthros | local历史生产流与full-read输出查询流成对训练，prefill/decode相位改变执行而保全历史KV | 2+2+2=6；具体架构缺口深入 | MODEL-LONG-CONTEXT Ch22，SwitchAttention后→Immutable Prefix前；不是现有query router或固定状态压缩 |
| SF-2026-ARXIV-2610-13328 / v1 DuoRate | 同artifact的resident与routing-weighted batch1读率两约束；同正频率乘畸变和rate时决策取消频率 | 2+1+2=5；为双账具体长期缺口进一步深入 | INFER-GPU-MEMORY Ch54，少读Weight/KV交点后→低比特Compute Balance前；已有desired/committed精度页非two-rate决策 |
| SF-2026-ARXIV-2610-13003 / v1 SlackSwap | forward host-link time是显式预算，昂贵重算tensor优先swap、剩余廉价recompute，再deadline/峰值repair | 2+1+2=5；为host-budget具体长期缺口进一步深入 | TRAIN-DISTRIBUTED-TRAINING Ch36，Training Memory Contract末→ExactReplay前；Ch35持久checkpoint非本activation owner |
| SF-2026-ARXIV-2610-12815 / v1 ByteExpress | 参数服务跨层组合：receive credit与outstanding-byte window资源不同，SRQ改变credit合同，transport可靠不授Push retry-safe | 1+2+2=5；为真实组合边界进一步深入 | TRAIN-DISTRIBUTED-TRAINING Ch36，五层通信末→Collective前；推荐PS直接训练系统证据，不称LLM collective实测 |
| SF-2026-ARXIV-2610-13408 / v1 Ember | mapped-default hybrid按仅host可见counter升温/衰减推断resident冷度，保headroom主动batch回收 | 2+2+2=6；受影响placement/correctness范围深入 | INFER-GPU-MEMORY Ch54，CapacityPlacement末MSched→层级管理权前；现有profile-driven demand paging不覆盖此反转 |
| SF-2026-ARXIV-2610-12570 / v1 DCOCO | topK adjacent候选交互并行评分、prefix-first串行轻选路，与真实point-mass verifier语义分离 | 2+2+2=6；sampling correctness必要深入 | INFER-SPECULATIVE-DECODING Ch48，InformationFloor最后DSpark→输入自适应前；Domino causal correction无并行adjacent grid分支 |
| SF-2026-ARXIV-2610-12545 / v1 AutoIndexer | generation时钟因果、display次序可编辑；cursor/marker/可见性+unrotated KV配Chain-of-Edits训练 | 2+2+2=6；cache/cause受影响必要深入 | MODEL-DECODER-ONLY Ch18，MultiStream→LatentReasoning前；已有stream/latent接口无可变display次序 |

### 11.1 CompileMask

[exact-v1](https://arxiv.org/html/2610.13474v1)直接读§2–3结构/descriptor、§4.1–4.4完整必要setup与反侧。MaskSpec互斥/覆盖Regions，固定K、sequence无关可表端点的规则才编译；端点随batch metadata在线一次计算，重复head/layer/recompute复用。forward row/backward column spec需分别正确，bool DNF不满足时保callable predicate fallback。Tile full/empty/partial状态不消除数值回归。

Blackwell exactSKU未披露，BF16/torch2.11cu130/Python3.12.9、TileLang0.1.9/CUTLASSDSL4.5.2；operator多mask/shape vs fullQwen3-8/14 TorchTitan batch1/compile/checkpoint为不同人口。完整训练收益1.05–1.31×不能继承3.8×operator峰值；causal仍落后nativeFA4（85–89%），FlashMask旧FA2硬件/stack不同且CLEAR不支持，不是零性能。未核artifact/复现，无生产SLO。

### 11.2 Layout Algebra

[exact-v1](https://arxiv.org/html/2610.13679v1)直接读§1–5定义/Thm1必要证明、§6–7实例与测试、§9边界。logical/thread-value必须完整bijective；physical允许明确⊥复制用于读取，write仍须injective，不由zero-stride取得write许可。physical不能作domain（terminal swizzle例外）；完整view先compose再restrict，受限slice不再可组合。合法composition可能不是layout，退普通index算术，不强制affine。滑窗partial overlap不在该formal model。

Rocq9证明§2–4操作及recognition decision；CuTe对应§6、restriction arithmetic§5仅测试。CUTLASS4.8指定complement输入M24覆盖16/24的反例不授当前所有CuTe故障。有限OCaml oracle/随机/8192coord SM90GMMA一致性不是compiled GPU timing；编译后性能是future work。只采用typed准入/读写、限制/证明范围，不授race freedom或runtime提速。

### 11.3 Orthros

[exact-v1](https://arxiv.org/html/2610.13735v1)直接读§3算法/相位/复杂度、§4.1–4.6、§5及必要AppA设置。base流local W128生产所有historical KV；对应output流global query共享WQ却独立scale/offset，拼接流共用norm/FFN，logits仅output。PT每位有output token增训练长度、SFT仅response复制；decode一base更新KV+一global输出查询，不是旧checkpoint runtime mask flip。fullKV不省容量；input重/output轻条件才减attention工作。

1.3B/100B FineWeb、160M–6.8B/10B及8B conversion/80B CPT不能混人口；128Kneedle另加20BProLong CPT。部分1.3B NQ/TQ/SQ recall反退；singleH100/SGLang/Triton batch2重prefill端到端、decode仅comparable而hybridGDN可更快，不授21.9×全链或长输出通用收益。双流训练/MoE IO与完整KV费用、agentRL未证近文。

### 11.4 DuoRate

[exact-v1](https://arxiv.org/html/2610.13328v1)直接读§3/Props1–2/两阶段、§4.1–4.5及§5，具体storage/layout与allocation controls。offline p4单artifact含prefix-readable p2/3/4、baked distortion；online自身prefill labels-free二阶moment估计decode，以dot+bisection选read tier。相同正f乘distortion和readcost才取消于每expert argmin，f仍决定预算；pooled domain组成或resident预算不取消。大batch expert union趋未加权，短输出prefill主导。

只有Qwen3-30B-A3B；MB/token/GiB为布局推算，fused prefix-read kernel与真实throughput未测。质量实验prefill也跑readdepth，**不是拟两阶段deployment实测**。own-format allocation值约0.07–0.11bpw，不借全部外部format优势；0.07 crossing外推，昂贵mixture可tie。校准testdocs与disjoint validation控制分别保留，requestmix drift须再校准，GPU/hardware与end-to-end SLO Not Disclosed。

### 11.5 SlackSwap

[exact-v1](https://arxiv.org/html/2610.13003v1)直接读§2–4/Alg1、validation/repair、§4.1全部simulator/基线、ablation/search与反侧。单profile需operator序/size/产生/下一读/recomputecost，D2H结束+last forward读后释放，H2D deadlines在容量允许时admit；D2H2%guard、六轮以内repair、无swap保底。不能把planned schedule当真实hookruntime。

A100 roofline-derived times/PCIe4 25GBps，每DMA concurrent85%+10µs/copy，fragmentation-free allocator忽略1.2%HBM copy争用；states常驻、单GPU BERT/GPT2XL/Llama7B-style/VGG BF16。全部throughput为DES，SwapAdvisor省去order/pool搜索，genetic6600–14000plans≤0.45%非globaloptimal；无GPU训练、动态shape、多GPUcollector/真实hostallocation测量。不授96–100%实机或通用半显存承诺。

### 11.6 ByteExpress

[exact-v1](https://arxiv.org/html/2610.12815v1)直接读§2.1/§3–7（allocator、sameQP completion、receive/TD/SRQ/window/recovery）、§8–9。registered block pool跨app/transport ownership、写入分片后sameRCQP最终WRITE_WITH_IMM completion才授payload visible；registration增长不free、zero-copy不含全serialization。per-peer dedicated RQ credit不直接授SRQ，SRQ队列/retry仅缓解不保证credit bound；per-engine window非aggregate全局bound/适应公平controller。Push exactly-once未证。

推荐PS实际300PS/124ranker inference及124PS/346trainer训练，25GbpsConnectX5；matched-load部署kernelTCP而非全部调优TCP比较。latency是Fetch/Push非训练step/推荐端到端；硬件only训练P99反而更差，PFC仍enable，window运行观察无pause不授可禁PFC。恢复<1min作者operational statement无systematicavailability/QPfailuretail。LLM/collective通用适用未测；组合控制的新边界可长期采用，不把成熟verbs逐项当发明。

### 11.7 Ember

[exact-v1](https://arxiv.org/html/2610.13408v1)直接读§3–6/§7.1/7.4/7.6–7.8/§8。adaptive595.71.05UVMpatch/CUDA12.4/Linux6.17需module权限，stock-CUDA static需app三placement calls固定hotprefix，非同合同“无修改”。只hosttraffic counter不见resident冷度；promotion前需求衰减+回迁grace/headroom推断，误判造成双搬。oneVAblock锁+driver migrate/page-table原序保存原coherence，不授任意driverport保证。GPU-only/library buffers不受控，apphint override，multiGPU future。

LLM llama-bench Qwen2.5-14B/Qwen3-32B、三discreteGPU均cap16GB、512prompt/128gen，计token generation非完整请求；1.41×过订阅none>3tok/s，headline3–13×vs thrashing非驻留或线上SLO。GH200只static（无baremetal），reuse低单扫mapped可更优；HELMonkernel有两反退，adaptive数据fits慢1.2–1.8×、stablehot高reuse static更快且重迁流量可增。precision/独立重复协议未完整披露，不拼data-intensive/LLM headline16×。

### 11.8 DCOCO

[exact-v1](https://arxiv.org/html/2610.12570v1)直接读§3–5/§4全部eq、AppA/B/C及G完整lossless推导，必要per-suite负侧。topK=16、adjacent K²MLP residual一次并行评分，firstslot保持argmax、后slot按已选predecessor逐row选择O(BK)，不globalpathargmax；不能超candidate缺token的coverage ceiling。训练joint CE软归一不是真实proposal，decode选路确定，target temperature处理q，接受概率q(yhat)、拒绝排除yhat归一residual才保target law，p不是draft原logit/score softmax。

singleB200/BF16/vLLM0.27/torch2.13cu130/TP1、graphs/prefixcacheoff；concurrency1率为request outputtokens/含prefilllatency后suite median，10suite等权，不TPOT。mainT0单run/T1三generationseed无trainingrepeat，6+6epochs vs mainbaseline6有12epochextensioncontrol仅Q8no-thinking；nativeB=15+anchor vsnominal16不同drafted人口。平均最优不all suite最优（AppD Table10 Llama-3.1-8B/thinking-off/greedy MBPP DCOCO989.7<Domino1128.5/DFlash1036.3；T1 LiveCodeBench也反退）。4–32平均并发收益非生产tailSLO，未核代码/复现。

### 11.9 AutoIndexer

[exact-v1](https://arxiv.org/html/2610.12545v1)直接读§2全部/§3编辑negative/§5、AppA.1–A.3/必要数据及protocol。因果在generation order，display index由marker+start/endcursor解析；alternating EDIT/RETURN、删除span只mask未来attention不物理释放KV；K/V存unrotated按本次display/anchor位置旋转，exact cache仅新CoE语义非普通文本重排后fresh-forward等价。Inverse随机edit生成训练序列，pointer/marker/LoRA联合学，不runtime零训练插件。两varlenpath disjointkeys+logsumexp合并同jointsoftmax，仍有packing及segment状态。

Qwen3-8B BF16LoRA r16/100K约200M token **perturb前**与marker/cursor额外预算；硬件/训练独立repeat/端到端latency未披露。单corruption每类别100、64generatedtoken limit的freegen exact insert10/delete53/substitute18/noop89，insert57不edit、clean11错edit；teacherforcing约90% emission不是autonomous修复90%。SFTmath/code低于originalQwen而无RLVR，capability保持是有限matched-LoRA比较，非所有model/任务等价。不要将hidden deletedspans当物理容量释放、普通KV证书或外部Agent effect权限。

## 12. 补检九项最小PRE与实际窄写（root非writer POST通过）

root已实际必要Source/owner与逐字PRE独核通过并授窄锁；Ch49先等runtime释放后授锁，其余五owner按约定窄锁。today_institutions已落实以下九段与九本人末注，并实际顺读各新正文/完整局部邻接与本注，限定diff-check通过；root随后实际完整读九正文、局部邻接与九本人注，非writer POST通过。本人九注已同步实际POST并读回，Ch49/22/54/36/48/18六窄锁释放，不授DAY。所有source采用均Status Experimental，未核代码/复现或生产部署。DCOCO的root independent推导核查不夸大为复读全部G，原有效必要Source由本人承担。

### C1 / Ch49 FlashAttention末、Tessera后

可见规则也可以先编译结构、再在线填metadata，而不每次对全部token pairs重跑predicate。互斥且覆盖有效query的区域若各自能化为数量不随序列增长的interval，编译器可生成只计算端点的preprocess；attention kernel消费端点和full/empty/partial tile状态，复用到heads、layers与重计算。这个descriptor只执行已声明mask，不决定哪些历史该可见；forward与backward的行/列规则仍需分别核对。结构不满足编译条件、interval数增长或metadata不兼容时，原callable predicate或已验证native mask仍是回退。静态分析、descriptor构造和workspace都付费；[CompileMask的受限Blackwell对照](https://arxiv.org/html/2610.13474v1)中causal仍慢于nativeFA4，完整训练收益也小于单operator峰值，不能由表达更广推出通用更快或生产SLO。<!-- source-family:SF-2026-ARXIV-2610-13474 -->

### L1 / Ch49 Lowering起始commit段后

Layout合法性还应区分索引空间：logical或thread-value映射需要覆盖其完整扁平域，physical映射则需要无alias，除非明确标出供多线程读取的复制；读取broadcast不能取得多线程写同地址的许可。先组合完整tile view、再取thread/warp restriction，可避免把稀疏slice当作仍可组合的完整空间。合法组合不一定仍能写为shape/stride layout，识别失败时可退普通索引算术，而不是强制生成affine式。这个typed分支增加表示和生成成本，不消除数值/并发回归；[Layout Algebra v1](https://arxiv.org/html/2610.13679v1)的证明只覆盖其定义与decision procedure，CuTe对应/部分restriction仅经有限测试，没有编译后GPU速度或任意overlap/race保证。广播写、partial-overlap或模型外转换仍保原库/显式索引及独立kernel验证。<!-- source-family:SF-2026-ARXIV-2610-13679 -->

### O2 / Ch22 SwitchAttention后

重输入、轻输出还提供相位分治的访问图：用local base流生成并保存全部历史KV，为需要输出的token另建global查询流，读取这些KV后形成logits；prefill主要批量生产local历史，decode每步同时推进base状态和输出查询。这不是推理时把旧checkpoint的mask切换一下，而是需要共同训练的双流接口，也不因local窗口而释放完整KV。[Orthros v1](https://arxiv.org/html/2610.13735v1)支持受限模型转换及长prefill成本下降，但双流增加训练token/FFN与状态，部分检索切片仍退步，128Kneedle另需长数据继续训练；decode并不普遍胜过hybrid，输出变长会缩小优势。无法再训练、远程关系回归失败、KV容量主导或输出很长时，原dense、固定hybrid与既有query路由仍合理。<!-- source-family:SF-2026-ARXIV-2610-13735 -->

### D1 / Ch54 少读Weight/KV交点节后

MoE精度还要分开resident账与decode读率账：容量向所有expert收费，batch-one每步只向选中的expert收费。prefix-readable权重可保持一个较深的驻留artifact，prefill读完整深度、decode按workload校准的tier表读前缀；tier改变不必重新编码。当同一正routing frequency同时乘该expert的畸变与读成本时，它从每expert的Lagrangian选择中取消，但仍决定总预算，跨domain混合或resident预算不继承此取消。大batch的expert并集、短输出的prefill会收窄收益，并增加profile、校准漂移和prefix kernel成本。[DuoRate v1](https://arxiv.org/html/2610.13328v1)只在一模型验证质量，流量为布局推算且prefix-read kernel未作端到端测量，质量实验也没有实际分离两相位；不能由低read bpw签发更低驻留容量或吞吐。条件不成立时保持静态精度/原预算，并按质量与实测完整路径重验。<!-- source-family:SF-2026-ARXIV-2610-13328 -->

### S1 / Ch36 TrainingMemoryContract末

Activation offload不是容量缺多少就向host搬多少：forward结束前可隐藏的D2H bytes受host bandwidth乘forward时间限制，晚完成的swap也来不及降低峰值。可用一次匹配profile先把可行link时间留给最昂贵/不可单算重建的tensor，再用廉价recompute覆盖剩余缺口；FIFO offload与deadline prefetch仍须同时满足buffer生命周期和峰值，出现等待或shape漂移后repair并保留no-swap计划。它用host流量、重算、pinned buffer与计划验证换容量，不取消最后reader和transfer completion再释放的条件。[SlackSwap v1](https://arxiv.org/html/2610.13003v1)仅以单GPU、无碎片allocator和模型化DMA的事件仿真支持此预算，不是实机半显存/近理想吞吐证书。profile不可靠、真实host竞争或重算依赖失配时，原block checkpoint/显式offload及更保守容量仍合理。<!-- source-family:SF-2026-ARXIV-2610-13003 -->

### B1 / Ch36 五层通信末

参数服务的RDMA迁移还需分别限制endpoint接收容量与fabric注入：dedicated RQ credit约束SEND/WRITE_WITH_IMM消耗的receive槽，per-engine outstanding-byte window限制incast在途数据，DCQCN/PFC则继续承担rate与链路backpressure；共用SRQ后不能沿用逐peer credit保证。注册buffer在application与transport间移交生命期、同RCQP最终completion确认payload可见，QP分片复用只缓解调度HoL，不证明端到端无阻塞。硬件可靠连接也不授state-changing Push重试exactly-once。[ByteExpress v1](https://arxiv.org/html/2610.12815v1)中硬件only反而加重训练尾部，软件窗口后的无PFC观察仅属推荐PS工作负载，不证明可禁PFC、任意aggregate公平或LLM step提速。注册池、fragment/窗口调参和RPC恢复都付费；负载/接收合同不匹配时保原TCP或已验证transport，并独立验收update语义。<!-- source-family:SF-2026-ARXIV-2610-12815 -->

### E1 / Ch54 MSched后

未知hot set还可以反转UVM默认路径：数据先mapped在host，允许GPU直接读，只有remote-access counter显示复用足够才迁到GPU；保留headroom并分批回收，避免每个新fault都触发临界eviction。counter仅看host而不看resident冷热，因此需以升温前需求衰减和误驱逐后的回迁保护推断，错误会增加往返，不能把hint当驻留真值。driver-adaptive管理原managed allocation却需module权限与版本重接；stock-CUDA的static分支需应用placement calls且固定split，两者不共用“零修改”承诺。[Ember v1](https://arxiv.org/html/2610.13408v1)的受限LLM token-generation对照仍低于3tok/s，非完整请求SLO；稳定高复用hot set可由static更快，单次读取可让host-mapped更合算。library/GPU-only buffer不受控、hint可override，容量足够或迁移不摊销时保常驻、原UVM或显式placement，不由相对thrashing倍率批准默认替换。<!-- source-family:SF-2026-ARXIV-2610-13408 -->

### P1 / Ch48 InformationFloor节末

缺realized prefix的parallel draft也不必用完整串行corrector修复：单pass保留每slot top-K，用相邻候选与slot hidden一次并行打分全部K²交互，再从首slot argmax沿已选predecessor逐row选后继。轻量串行walk保留prefix-first偏好，却不等全路径最优，也无法召回top-K外的正确token。评分只提proposal：若选路确定，stochastic verifier面对的是point mass，应按target对该token的概率接受、拒绝后从排除它的target残余采样，不能拿draft原logit或训练softmax冒充真实proposal。额外候选/scorer和联合训练要计费；[DCOCO v1](https://arxiv.org/html/2610.12570v1)的B200平均吞吐最优仍有单suite反侧、训练预算与native drafted长度差别，不授生产tail或所有任务收益。依赖弱、候选coverage低或scoring抵消收益时，原parallel/AR drafter与target-only回退继续有效。<!-- source-family:SF-2026-ARXIV-2610-12570 -->

### I1 / Ch18 MultiStream末

因果生成顺序也不必等于最终display顺序：模型可逐步产生marker与cursor来打开/结束编辑，把新token插入、替换或删除已生成文本；inverse-edit扰动训练让它学习位置与修复，而非只学习下一个可见字。此时generation clock仍因果，parser维护display位置与可见性；删除仅从后续attention和最终输出隐藏旧span，不物理释放历史KV。K/V可存unrotated并按本次编辑位置旋转，缓存精确限定在这套Chain-of-Edits语义，不等重排文本后普通decoder重新前向。这个分支增加pointer/marker训练、segment/packing和仍保留的历史状态；[AutoIndexer v1](https://arxiv.org/html/2610.12545v1)的单corruption诊断中插入常不触发，exact repair远低于teacher-forced定位率，能力保持也只限matched-LoRA对照。质量、cursor或预算不稳定时，原追加式AR及外部显式编辑仍合理；显示修订不撤销已发送内容或外部effect。<!-- source-family:SF-2026-ARXIV-2610-12545 -->

## 13. 原36池四项独立准入校准与13348改判

四项精确v1完整题摘均已读回`arxiv-abstracts.json`，而非沿用旧EX标签。以下三项具体理由由root与本人当前独立题摘校准；不因已有Books或访问失败排除，不评分。必要core仅13348须补，已直接读，不无差别全文打开其余三。

| exact-v1 | 贡献前具体关闭理由 |
| --- | --- |
| [13627 AMLworld-Compact](https://arxiv.org/abs/2610.13627v1) | 固定prediction上的HT confusion counts无偏、precision/F1 ratio非无偏是成熟统计区分，应用到金融图评价；lexical audit不证明答案正确亦为具体评价结果，题摘未给直接LLM/Infra设计的新机制/边界，不因其cost reduction或可映射Ch66准入。保500draw局部统计与金融领域，不借新标签升分。 |
| [13476 A Better Metric Will Not Save You](https://arxiv.org/abs/2610.13476v1) | 15语言vowel category condition选择的representational study；分类选择影响rank在该acoustic领域的结果，没有直接LLM/训练推理平台的机制或适用边界差额，不能仅以普遍“比较人口重要”主题纳入主线。不否定其领域结果。 |
| [12495 Kairos](https://arxiv.org/abs/2610.12495v1) | 现有linear/window/AttnRes/MoE/byte codec组合只single440-byte text过拟合，作者明确不是generalization/multimodal训练或baseline性能证明；analytic target throughput非测量。题摘的核心新增为该组合能优化的sanity而非新的foundation-model机制/有效性边界，不能借目标所有模态/计划200M产出准入。 |

### 13348v1 T²Mem：旧EX停止使用，当前准入/具体NC（root独核通过）

旧停点把本项列具名EX但未持久确切增量依据；DAY准备读回完整题摘后发现“初始retrieve pool以外还可再取证”不能由成熟组合一句关闭。root明确授权仅决定准入core与评价，实际[exact-v1](https://arxiv.org/html/2610.13348v1)§3.1–3.2/Eq3–13、§4–5/Tables1–3、A.3–A.5已读，支持具体准入；旧EX作为审阅因果保留但不作当前处置。日期复用本日36精确v1官方Mon12有效身份层，不搬Submitted Oct9。

真实新增：offline episode metadata/backlink作cue；query-local cache逐步append，SearchMeta补未seen池、ReadRaw跟已seen metadata回原session，构造出的缺口再驱动下一次读取，不被首次候选池封死。Tmax5、initialk5/后k1、Answer停止是有限controller预算不是证据充分证明。评分`2+1+2=5`，标准必要方法/对照与实际owner比较完成；不升为跨生命周期研究或把已有覆盖反推低分。

Qwen3.5-27B/Gemma4-31B、BGE-M3/vLLM，LoCoMo1540（排adversarial）和LongMemEval-clean500，Qwen3.5-Plus同judge非独立事实真值；temperature0/native thinking off/answer max1024。LazyMem未公开4B被替换为各backbone，不能称原实现完全matched。总tokens/消融预算不等，LoCoMoQwen本项8765k比Light6178k更大；summary/graph/noMetadata/noRaw/noRollout平均支持局部作用却有multiHop/temporal等反侧，不授every category/noRaw总弱。推理budget只prompt长度+maxN64全response上限，非reasoning硬上限；按实际停止T分层也非随机匹配人口。hardware/precision/独立重复及端到端latency/所有维护成本Not Disclosed，不以token账代完整生命周期省算力。只采用cue/raw与query-local逐步增量取证，不采用attention saliency为因果证据。

唯一owner `AGENT-MEMORY` [Ch77](../../../../../books/part-07-agent/77-memory.md)实际完整局部对读：269–294的anchor→bounded expansion→evidence assembly及controller/source分责；395–407的summary sufficiency触发source-linked/global raw回读、query-conditioned constructor及开销；429的query-local实体工作记忆global路径补未覆盖实体、保存source/update版本；1598–1622的lossless source/late materialization与budget/permission/citation authority。它们具体承载“工作记忆不固定在首retrieve pool、derived cue不替source、读与构造预算共同验收”。T²Mem的nongraph episode metadata与two-tool实现为新增局部证据，不改变这些已在正文解释的长期论点；root随后实际完整读上述四处owner并独核准入/真实5分标准审阅与具体NC通过，当前已有覆盖，不写重复algorithm/论文引用。本项不成为EX、不能预支DAY。

## 14. 最终非报告作者六部分 DAY（通过；待作者同步完成字段）

复核者：`today_institutions`；报告作者为root，本复核者未写本日报README。实际完整读取最终六部分，并逐项对照本文、`model-evidence.md`、`runtime-evidence.md`的必要证据、反侧、评分、owner及当前执行层；范围是2026-10-13 Daily的10-12北京时间完整自然日，不继承其他日期或Weekly。结论：**DAY通过**。普通扫描/准入/必要审阅/Books写入和独立验收已无余项；此刻只待报告作者将§1/§5/§6与header同步完成状态，再由本复核者只读完成字段差额一次，不预先声称该字段已落盘。

1. **来源及停止范围。** 已对照每日14源、全球/中国来源有限记录和runtime当前停止节。四主题首段100/100/53/10及两query末页76/276、63/263是实际线索范围；12分类Mon12 union648只负责身份/日门，不是648完整题摘或Source队列。相关新命名标题子切片与58具名完整题摘另算，不以下载/索引存在授全部初筛。保留原start0合并输出截断中段及其余宽池未逐项题摘范围。Google Pubs日级、Meta动态/混排隐藏段、Qwen动态Research和MiMo14无目录日期Blog被精确隔离，不拿替代入口或旧前缀推无遗漏，也没有未读ordinary被改名外部材料。使用本日有效源，不重复抓取13机构目录、不扩大GPU/科学应用或Weekly范围。
2. **全部准入/日期/分母。** 三作者16+21+23归并60唯一家族，54 arXiv+6官方；58完整arXiv题摘当前为54入选+4贡献前关闭。已逐条核报告贡献链与新增命题评分，不以mapping/已有Books/访问状态倒推。arXiv采用官方Mon12事件门而非Oct8/9 Submitted，四工程merge采用本窗BJT事件，OAC两release不重复家族。T²Mem在最小core后从旧EX改判5分标准审阅、Ch77具体NC；HnS最小受控反证改判5分深入、Ch66具体NC，保早期理由但不再沿用旧标签。其余三个原池EX完整题摘及Minions最小core已独立校准，没有把“成熟组合”泛化为排除所有局部/负面机制。
3. **必要证据及权限。** 59家族必要证据/Books判断完成，1家族13816完整必要正文受阻。本人16直接必要primary阅读保持§1–13精确范围；其余43可读项由两位非Report作者的实际必要Source阅读支持，本次完整读回其证据/直接反侧与报告采用主张；13816只复用实际完整题摘与失败恢复层，不宣称已读必要正文。未变化层按合同复用，不声称第二遍无差别全文/附件阅读。实际进一步深入的受影响安全/correctness、长期缺口及设计反证与表中审阅层相符；UniRL为allocator真实长期缺口深入而非仅改标签。作者结果、局部timer/模拟/形式假设、Not Disclosed和未复现保持权限边界：没有把两IoT实验拼闭环、posix/win32模拟升为Windows acceptance、SlackSwap DES升实机、RDMA推荐PS升LLM collective、DuoRate布局估算升实测、DCOCO训练score升proposal概率。SOAR配方、InstantFusion阈值/次序和HnS Table11人口/estimand冲突的强主张隔离，保可独立支持命题。
4. **最终owner与实际Books。** 53整合=48 arXiv+5官方，落27唯一owner章节；6具体NC为distillation/13881/13060/13303/13348/13935，13816为暂缓且无PRE/写入。逐项对照最终packet的独立Source/PRE与非writer实际正文/完整局部邻接/本人末注POST；53写入都已root实际非writer POST通过，作者注同步读回、全部窄锁释放。本人的14写入不由本人自授POST，本DAY复用root有效实际POST；两其他分支的39写入亦据其当前实际POST层，不沿用早期“待写”因果快照。全部53报告身份在指定owner的Review notes之前有正文binding，未出现只加末注。六NC对应实际论点而非主题相似：已读的Ch72消费授权、Ch22下一更新充分统计、Ch66criterion/gold、Ch77增量取证链保持；本轮又直接顺读Ch45 position/context/correction/exact退路与Ch66 attribution estimand/falsifier/匹配mask/output/replacement/OOD局部，验证最后NC无遗漏差额。Smol移到action-only后且再POST，保持上下文；不制造NC引用或结构收纳章。
5. **排除项/特殊信号分层。** §10的14组/16事件具名安全、正确性、兼容或测量信号，已直接读必要primary/core及实际受影响patch；不是34个commit全源码审计，EX恢复成熟不变量不重新捆repo评分。ordinary实际9样本/8来源（七机构原样本、同Moonshot Kimi4092、arXiv Minions12970）加原池三篇完整题摘13627/13476/12495独立校准，理由/样本保§10/§13。没有独立读其他ordinary EX全部题摘/代码、宽池截断中段、全部附件/版本史/证明，更没有执行作者GPU/Windows/VM测试。T²Mem漏收理由被发现后仅重开受影响原四项并持久化具体新判断，没有把这一局部纠正等同全召回验收。
6. **六部分一致性与机器检查。** 完整报告60行/60原始材料证据小标题/60唯一URL、全部公开日期10-12、三维和与处置均一致；53正文binding存在、owner文件存在、27整合章节，未缺项或重复。本人实际运行`python3 scripts/validate_research.py --report papers/2026/10/13/README.md`，1份V3 interface/consistency通过，semantic不由机器授权；各作者限定diff检查与root最终全局/cached检查有效，root另提供42窗口测试通过，不冒称本人复跑42测试。工作树既有/并发历史和staged Ch69/LS保护，未stage/commit/push。§5保留精确外部重开条件：13816完整exact-v1或对应作者全文只重开该family/Ch25–26，其余四目录段和三争议主张只定点恢复；保留项不授Evidence/Coverage通过或性能/安全/互联网无遗漏。

**完成态 FINAL 读回通过。** root随后实际同步本日报header状态「完成」、§1的60/59/53整合27章/6NC/1隔离与普通0、§5的终态保留项和§6的非作者通过及真实抽检范围，并提供完成态V3通过。本复核者只读上述行政字段差额，确认安全终态含义、原窗口、精确隔离/重开条件和不授无遗漏/实验保证未变，无需重审已有效研究。前文「待作者同步」为DAY时点，已由此当前层关闭。本人本日任务终止，不接其他日期/历史/Weekly，不stage、commit或push。

