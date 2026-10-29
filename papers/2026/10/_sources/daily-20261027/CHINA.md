# Daily 2026-10-27：中国机构来源与 Qwen 必要证据

**窗口：** 北京时间 2026-10-26 ～ 2026-10-26。

**执行：** `live1027_china`，2026-10-27 09:12 +08:00 前后实际请求。

**范围：** 只负责以下九个每日 Source ID；不修改 Report、Books、State，不 stage/commit/push。独立 reader 尚待准入校准与最终核验。昨日记录仅导航已知公开 endpoint 形状；下述目录及必要原件均重新实际请求，未继承昨日覆盖结论。宽列表只读身份/日期，不转为旧 Methods 队列。

## 1. 来源与停止位置

| 来源 | 本轮实际检查、停止与结果 | 限制/后续 |
| --- | --- | --- |
| SRC-QWEN | [Research](https://qwen.ai/research)文本仍0行；实际 GET [retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)，随机 X-Request-Id，HTTP200/success=true，全部40身份/extra.date已读，混序且最大2026-09-20，末项Qwen-Image-2.1。另实际 [research-list](https://qwen.ai/api/page_config?code=research.research-list)60项、[latest-advancements](https://qwen.ai/api/page_config?code=research.latest-advancements-list)19项全部身份/日期，最大分别2025-12-23、2025-09-24；均无分页元数据，不以首项截断。定点 [qwen-code releases](https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=8)8项身份日期，至10-22Z即停；当窗nightly与SDK两事件见§2。 | 公开payload已成功恢复，不记JS空壳受阻；这些列表滞后不证明全站Oct26无发布。nightly权限/安全P待reader与root的Books判断。 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/)→[Research & News](https://www.deepseek.com/en/news/)及[日志](https://api-docs.deepseek.com/updates/)；主页置顶1017，News最新09-10/04-24；日志最新10-17，随后09-10，均已越窗即停。 | 未发现确定本窗研究事件；不扩大所有repo/PR。旧版本不因安全/Agent标题搬入窗。 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)读取可见26身份/日期，最新2025-11-07，目录滞后；[官方GitHub组织](https://github.com/MoonshotAI)导航到[kimi-code releases](https://api.github.com/repos/MoonshotAI/kimi-code/releases?per_page=5)，5项日期为10-26/25/23/21/14Z。2.3.3确定本窗，完整5条说明已读，具体N见§2。 | repo Updated不当公开日期；旧Blog不能证明机构零事件；具名release已实际检查，不把目录滞后写成整个来源无法处理。 |
| SRC-TENCENT-HUNYUAN | 首查[Research](https://hunyuan.tencent.com/research)文本0行。实际公开publicList只读POST `{pageNum:1,pageSize:1000,renderType:0}`返回英文9；加Accept-Language/lang仍9，不能借它授中文全覆盖。随后真实后台浏览器打开同页→`research?page=1`，当前中文“全部”列表完整11条，最前09-22两项，随后08-28、08-11、07-21、07-06、05-21、04-30、04-23、02-13、02-03；无分页继续控件。顶层featured非全部替代，已实际读`research all list`全部。 | 最新Hy Image3.5 preview与Batch Size Scaling均09-22，已越Oct26；不读旧Methods。此为中文All真实恢复，不将英9当中11或空UI当零。 |
| SRC-ZAI | 首查[Research](https://www.zhipuai.cn/zh/research)“全部/时间排序”15项，最新GLM5.3Flash08-26，随后08-14至2025-12；越窗即停，不点更多旧项。[发布说明](https://docs.z.ai/release-notes/new-released)最新08-26，随后08-18/06-16。 | 无确定本窗候选；目录与release日期口径差异不影响Oct26排除，不为此追旧史。 |
| SRC-BYTEDANCE-SEED | [Publications](https://seed.bytedance.com/en/public_papers)Newest→oldest，第1页，首项Recycler10-25，次项09-28，至旧日期停止；同时[Research/Blog](https://seed.bytedance.com/en/research)当前首置顶SeedRealtime未显日期，故实际打开[原文](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction?view_from=content_recommend)核Date2026-08-05，其他首屏Jul31/20/8/7，均窗外。 | Recycler官方Oct25是更早公开线索；若Oct26 arXiv批出现该身份，必须归同家族，不重计首次公开。未据标题对其他arXiv材料作去重。 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)第一页10项身份/日期，最新05-09，随后04-30/04-15至2025-11-21，页脚下一页2/2为更旧；越窗停止，不开旧Methods。 | 无确定本窗事件；不采用榜单数字为长期结论。 |
| SRC-XIAOMI-MIMO | [主页](https://mimo.xiaomi.com/)Paper8条日期均旧（最新06-29）；Blog15条全身份已读。重新实际核HTML中button `aria-controls="blog-more"`，More只展开09–15七条，不是未知分页。精确日期恢复见§3。 | 全15已作窗外/暂缓判断，不留伪More缺口；不声称未公告渠道全覆盖。 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)最新10-22MiniApp、10-19M3.1Flash，随后08-13；[中文入口](https://www.minimaxi.com/blog)实际转[minimax.cn/blog](https://www.minimax.cn/blog)，同样10-22/19后08-13。另[Agent Tech Blog](https://agent.minimax.io/docs/techblog)最新10-20两项，随后10-08、09-22、09-19；越窗停止。 | 无确定本窗研究事件，不把旧MiniApp机制重新计入。 |

本轮轻量检查已读目录/事件原件中的撤回、纠错、安全、修订说明：目录未见影响上述当窗排除的具名标记；Qwen明确安全变化保留为P，不因“fix”标签降为普通修补。未遍历全站或无限版本史，也未把“未见标记”外推为全站无纠错。

有界补检只用以下首批查询作线索：`site:qwen.ai "2026" "October 26"`、`site:hunyuan.tencent.com "2026" "10-26"`、`site:moonshot.ai "October 26, 2026"`、`site:seed.bytedance.com "Oct 26, 2026"`。实际主要回Kimi论坛支持/配额问题与旧公告，没有额外研究候选；不遍论坛线程、也不以搜索空证明零发布。

## 2. 当窗事件的具体准入/排除

### P1 — Qwen Code nightly 权限与凭据边界

家族为Qwen Code发布，不是每个PR各一篇论文。[精确release](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.1-nightly.20261025.8e28d5380c)的[API](https://api.github.com/repos/QwenLM/qwen-code/releases/tags/v0.26.1-nightly.20261025.8e28d5380c) `published_at=2026-10-25T23:20:17Z`，确定BJT2026-10-26。完整release说明已读。当前[tag compare](https://api.github.com/repos/QwenLM/qwen-code/compare/v0.26.1...v0.26.1-nightly.20261025.8e28d5380c)为diverged/86 commits；只用作身份/变更导航，不把86构成完整方法队列。另实际核[gitref](https://api.github.com/repos/QwenLM/qwen-code/git/ref/tags/v0.26.1-nightly.20261025.8e28d5380c)：type=commit，真正tag commit为`8d14dd966cff397c600da66302c54ac87f286904`，不要把tag名中的`8e28d5380c`当成实际tag commit。

**准入链：** 既有粗粒度审批与项目环境加载能将会话例外或凭据来源混在默认设置中 → release新增session级规则/Auto以及仓库环境不得设定daemon bearer的真实边界 → 需要重新判断谁可授权工具、何时必须保留真人决定、何种配置能成为服务凭据。拟`Design Delta1 + System Reach2 + Durability2 = 5`，不因安全标签抬分。受影响安全域按合同深入，其他普通CI/UI不扩审。不是同commit桌面包去重：对比旧[v0.26.1](https://api.github.com/repos/QwenLM/qwen-code/releases/tags/v0.26.1)已重新核其完整release说明与具体变化身份，15448/15228不在旧完整列表；旧日报QQ scope处置不代本次新域审阅。

已读首次必要：PR15448、15228完整官方英语核心说明、文件清单、下述实际patch与测试；并通过GitHub contents API精确nightly ref读回相关实现/设计，绑定真正tag commit。raw.githubusercontent.com一次超时后，contents API base64原文真实恢复，不留伪外部材料缺口。root/reader负责实际Books owner比较、准入校准与独核；本文件不签Books，也不把测试源码当本轮运行通过。

#### PR15448：规则与 Auto 的权限路径

[PR15448](https://github.com/QwenLM/qwen-code/pull/15448) merged2026-10-24，head `bb4eaf2353342426bba62c57ac06326316e99dd0`；PR公开/合入日期与Oct26 release事件分开，不改称Oct26首次发明。实际读[file API](https://api.github.com/repos/QwenLM/qwen-code/pulls/15448/files?per_page=100)60文件清单中的相关安全域：

- 测试先读`hosted-permission-policy.test.ts`、`managed-permission-rules.test.ts`、`hosted-tool-approval.test.ts`、`hosted-approval-selection.test.ts`。重叠deny/ask/allow、shell组合中rm/未知段、真实MCP producer identity与WebFetch domain、有界/拒非法rule、snapshot不可同revision重写、`requiresHumanDecision=true`在YOLO后仍不自动publish，均是具体源码断言，未运行。
- `managed-permission-rules.ts`只允许3组allow/ask/deny；单规则512 UTF-8字节、每组32/总64、JSON8192字节限制；拒路径谓词`Read(./secret)`等不支持格式。不是任意策略语言。
- `hosted-permission-policy.ts`复用PermissionManager，getCwd/projectRoot均`/`、sandbox classification开启，**不查Harness host的工作目录去替远端Shell分类**；MCP以producer serverName/toolName重建真实identity，不凭opaque advertised名字匹配。`hosted-workspace-tool-turn.ts`先rule deny，再把rule ask/Hook ask/Plan退出构成humanOnly；allow或既有预批准可跳过人工，只有native且非MCP的Auto才调用classifier。分类unavailable落持久人工Action；signal abort在结果后检查，不凭分类完成自动派发。
- `hosted-harness-model.ts`/`hosted-harness-session.ts`只从已committed输入还原真人原文，最多最近40个hosted-harness accepted输入；排除非real_user provenance、agent_message/agent_mention，不把模型/子agent说法升格为用户授权。缺原文返回unavailable。Auto复用既有classifyAction，不是本版本提出新安全算法。
- `hosted-approval-selection.ts`固定Turn快照rules；同revision重写、live更换rules/版本回退报错。`hosted-tool-approval.ts`及session冷恢复分支持久`requiresHumanDecision`，即使后改YOLO仍不能抹去rule ask/Hook ask/Plan退出的真人要求。Auto的预批准工具列表沿default；不是所有调用必经过classifier。
- Java `ManagedAgentStore`/`ManagedSessionStore`/`ManagedActionStore`/`ManagedAgentService`实际patch：规则持久到Session与Turn；利用原授权/expectedRevision/idempotency receipt；请求改rules时有active Turn、decidable Action或open settlement operation即拒。`QwenHostedHarnessConnector`分别协商`approval-selection/1`+`auto-approval/1`、`permission-rules/1`；已保存策略遇缺能力Harness明确拒，不静默退化。`childAgentsOf`对委派子会话将Auto映射default，规则未自动下放；creation modes保持原保守列表。

**直接反侧与不能证明的内容：** 规则只限制模型工具输入，不是OS confinement，也不约束Hook副作用；不支持路径谓词、自动MCP分类或部署全局策略。PR自身的证据仅macOS限定构建/fixture/隔离Harness探测，明确真实classifier/Runtime派发、完整Hosted故障、retained-MCP idle编辑、真实MySQL、完整Java/CSI等未通过完整验收；V1数据库baseline原地变更需要重建开发库，没有in-place migration。不得把release、源码断言或作者自报tests改写为本轮实测生产保证。

**精确release读回位置：** [design全文](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/docs/design/2026-10-24-managed-permission-policy.md)已读，仍明写“not production acceptance”及Java/CSI/MySQL边界；[matcher全文](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/serve/hosted-permission-policy.ts)与PR相符。[实际approve分支](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/serve/hosted-workspace-tool-turn.ts#L8439)8439–8476核deny/humanOnly/Auto/MCP/unavailable；[Action floor](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/serve/hosted-tool-approval.ts#L585)585–596核持久真人要求。该文件95行缺mode的旧parser默认仍yolo，不能把“新增可选择Auto”误写成产品全部默认Auto；创建时仍不提供Auto由`ManagedApprovalChangeTest`实际测试断言和`WorkspaceBindingCreator`改为`isManagedInitialApprovalMode`印证。[capability列表](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/serve/hosted-harness-contract.ts#L89)89–91已公布两项能力；能力声明不等于真实Runtime验收。

#### PR15228：daemon bearer 不能由仓库预设

[PR15228](https://github.com/QwenLM/qwen-code/pull/15228) merged2026-10-24，head `c4395d02fa9fa162b0e6e58e71e3412d0141519a`。全部[file API六文件patch](https://api.github.com/repos/QwenLM/qwen-code/pulls/15228/files?per_page=100)已读：environment/shared-env-keys实现与四测试文件。核心实际变化是`QWEN_SERVER_TOKEN`从reload-only tier移到`PROJECT_ENV_HARDCODED_EXCLUSIONS`，统一initial与reload/full-loader/serve-fast-path。仓库`.env`、`.qwen/.env`、workspace settings.env均不得在启动前预设token；trusted workspace也不豁免；大小写变体一并匹配。home `.env`与home `settings.json.env`不能混称：前者作为operator渠道仍可用，后者settings.env在所有scope均拒此key。

测试不仅改“token被拒”，每处有无关inert marker仍加载的positive control，覆盖trusted/untrusted、显式workspace、case variant、placeholder等；因此支持拒的是凭据key/作用域，而非不读取任何环境文件。此为源码中的预期行为，不是本轮执行了攻击PoC或HTTP401。operator仍可通过`--token`、导出的shell变量或home层`.env`供token；无operator token时，**非loopback bind**才生成一次性随机bearer，不得概括成所有loopback启动也强制随机/身份认证。旧workspace/home settings.env凭据配置需迁移。不能证明任意进程/Hook/其他配置键无注入。

**精确release反侧已完成：** [shared-env-keys](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/config/shared-env-keys.ts#L266)266–276仍含hardcoded token exclusion；[run-qwen-serve](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/serve/run-qwen-serve.ts#L3486)3486–3489实际传入`isLoopbackBind`，3254–3264注释和3853–3872非loopback/require-auth拒绝分支已读；[serve-token全文](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/serve/serve-token.ts)实际生成条件为`!loopback && optionToken === undefined && environmentToken === undefined`，randomBytes16/base64url。显式空token不会生成替代物，而是trim为空后在需token绑定中拒启动；loopback默认仍trusted tokenless，须`--require-auth`配凭据才能强制认证。10955–10960启动告警明确本地调用可执行daemon用户代码。这个直接反侧阻止把凭据来源硬化夸成全端点默认强认证或OS安全保证。

### N1 — Kimi Code2.3.3：可见性/提示，不是新执行机制

[精确release](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%402.3.3) [API](https://api.github.com/repos/MoonshotAI/kimi-code/releases/tags/%40moonshot-ai%2Fkimi-code%402.3.3) `published_at=2026-10-26T13:22:15Z`→BJT2026-10-26。完整5条核心说明：4414不再把任何子agent启动前已拒绝的AgentSwarm显示为failed swarm，并提示`/swarm`；4424 model switch确认prompt；4423启用swarm的high-usage warning；4432合并重复权限提示句；4443泛web交互修复。

已有拒绝/执行不变，新增是错误状态呈现与提示文本，未提供足以修正授权/可靠性机制的证据；明确N，不评分、不进Books。没有把它当“旧Kimi风险已被修复”或沿用昨日2.3.2的执行域贡献。未见该release撤回/安全纠错说明；无须因同含swarm/permission词扩到所有PR。

### N2 — Qwen TypeScript SDK0.1.23：打包旧CLI，不新建机制候选

[精确release/API](https://api.github.com/repos/QwenLM/qwen-code/releases/tags/sdk-typescript-v0.1.23) `published_at=2026-10-26T04:43:39Z`→BJT2026-10-26。完整release说明实际包含连续累计Bundled CLI旧版本/旧SDK changelog，最上仅称本SDK bundles CLI0.26.1；没有说明本次独有的授权/协议变化。按实际core说明以版本打包事件N，不把累计旧安全项归成本日新贡献，也不由此声称SDK与CLI产物完全相同或安全已测。

窗外身份：Qwen `v0.26.2-preview.0` Oct26 18:25:27Z和`v0.26.1-nightly.20261026.34769f9d41` Oct26 22:32:18Z均属BJT10-27，不进入本窗，即使工具当前已能读到。旧stable/desktop日期Oct24Z均早于本窗。

## 3. MiMo 精确有限日期恢复

当前主页所列15个Blog，重新实际请求官网公开[manifest](https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js)相关route frontmatter，并重开必要原件，只有日期/标题用于本窗过滤，不审旧Methods：

| 序号/身份 | 本轮实际原件与日期 | 处置 |
| --- | --- | --- |
| 01 tool-call repetition | manifest `/blog/mimo-v2-6-tool-call-repetition`对应date2026-09-27 | 窗外 |
| 02 V2.6 | [article](https://mimo.xiaomi.com/mimo-v2-6/article.html)正文September22nd2026 | 窗外 |
| 03 New Materials | 主页完整标题/说明即PFAS capture、分子设计和材料研发应用 | AI for Science暂缓；日期不影响N，不额外恢复 |
| 04 MiMo Code | manifest`/blog/mimo-code-long-horizon`date2026-06-10 | 窗外 |
| 05 UltraSpeed | manifest`/blog/mimo-tilert-1000tps`date2026-06-08 | 窗外 |
| 06 inference | manifest`/blog/mimo-v2-5-inference`date2026-05-30 | 窗外 |
| 07 ASR / 08 TTS | [ASR](https://mimo.xiaomi.com/mimo-v2-5-asr/index.html)/[TTS](https://mimo.xiaomi.com/mimo-v2-5-tts/index.html)原文April2026 | 月精度已足排Oct26，不造日 |
| 09 V2.5Pro / 10 V2.5 | [Pro](https://mimo.xiaomi.com/mimo-v2-5-pro/index.html)/[V2.5](https://mimo.xiaomi.com/mimo-v2-5/index.html)原文April27th/22nd2026 | 窗外 |
| 11 V2Pro / 12 V2Omni / 13 V2TTS | [Pro](https://mimo.xiaomi.com/mimo-v2-pro/index.html)/[Omni](https://mimo.xiaomi.com/mimo-v2-omni/index.html)/[TTS](https://mimo.xiaomi.com/mimo-v2-tts/)原文均March18th2026；TTS的index.html一次web失败后准确slash URL恢复 | 窗外；一次失败不记外部缺口 |
| 14 Flash / 15 HSS | [Flash](https://mimo.xiaomi.com/mimo-v2-flash/index.html)December16,2025；[HSS](https://mimo.xiaomi.com/blog/mimo-v2-flash-hss)December22,2025 | 窗外 |

## 4. 交接与尚未完成

中国来源初筛为1个确定当窗P家族（Qwen nightly），2个当窗具体N事件（Kimi2.3.3、SDK0.1.23）；其余是有界目录窗外/暂缓，不把它们累计成几十篇当日审阅完成。Qwen相关首次必要及精确release反侧读回已完成，见§2；本分工没有未做的原件恢复普通待办，仍未执行第三方代码/实验。root负责将候选与其他来源归并、实际Books/owner比较与后续独核，这些仍是普通可执行工作，不是外部保留项。当前没有支持“九机构当日绝无遗漏”或“生产安全验收通过”的声明。

## 5. Actual owner 比较与完整拟稿 PRE（暂停：六个具名核心域待补校准，尚未写 Books）

2026-10-27 `live1027_china`按Books路径重新加载AGENTS/ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE及LEARNING_STATE最新相关checkpoint。有效首次必要与精确tag证据直接复用§2，不重复下载两PR方法。实际读取Ch78/72相关完整论证与直接邻接，另读Ch77→78/78→79、Ch71→72/72→73交接及Ch84 policy-as-code段。没有把章末Review notes的旧“已覆盖”声明当正文。

### A. 具体已有覆盖与真实差额

| 拟命题 | actual正文位置 | 比较结论 |
| --- | --- | --- |
| tool proposal与真实principal/执行权分开 | Ch78“模型输出只是Proposal”117–145、标准data path；“Preventive/Evidential Gate”712–747 | **具体NC**：不因Qwen重写基础分责，不再复制canonical action/typed arguments/审批与effect回执。 |
| retry/idempotency/conditional revision是可靠执行所需 | Ch78“Retry、Idempotency与Exactly-once”484–505；Ch72“Delegation Chain”3058–3068 | **部分NC**：原文已覆盖远端effect未知、去重与delivery fence，但并未讲编辑审批policy本身的幂等/版本、已准入Turn快照与待决真人floor；不能用同词授全部NC。 |
| classifier/monitor只是sensor，规则/人持最终authority | Ch72“行为控制权”985–1008；“安全承诺”3656–3674 | **部分NC**：已有deterministic tool policy、真人principal和自动policy批准须如实名；未讲显式ask不被后续mode改写、恢复时保留真人要求，以及Auto分类器必须从已提交真人原文恢复意图。 |
| runtime policy binding run/rule revision/effect/receipt | Ch84 policy-as-code 45–50（完整段已读） | **具体NC**：不在Ch84再介绍一般策略版本化；本次差额只解释“旧审批义务怎样跨live mode/cold recovery存活”的安全authority，不增加另一个runtime/service owner。 |
| dangerous-command guard、审批UI、OS隔离不是一回事 | Ch72 Kimi CLI段1786–1791及“不可信代码需要OS Effect Boundary”3381附近 | **具体NC**：保留已有三分责，不把新增permission或拒项目env推成sandbox保证。 |
| repository配置不能决定daemon bearer；workspace trusted≠operator credential source；loopback默认非强认证 | Ch72资产/信任边界31–33、Supply-chain1395后、secret-backed operation3068–3078、OS effect3381后 | **真实差额**：管理配置路径、凭据不进入模型与进程隔离已有；但这些正文没有承载“相同env key须按来源scope决定能否成为启动凭据”、显式空值与nonloopback随机/loopback tokenless这组反侧。只采用来源与执行资格边界，不把本版本配置格式写成通用规范。 |

**唯一owner拟定：** `PLATFORM-SECURITY` / Ch72，而非Ch78或84。两段共同回答“谁能在当前与恢复后的执行点决定authority”：第一段是审批policy来源/持久义务，第二段是启动凭据来源/绑定默认；Ch78继续拥有通用调用/幂等和effect协议，Ch84拥有平台run/state整体控制。Ch71身份入口与Ch73生产验收交接保持，不新增第二owner或结构候选。其余版本细节仅报告，不逐项搬书。

### B. 完整前肩（当前磁盘原文，保持不改）

同样需要分开“危险命令识别”“是否弹出审批”和“进程实际能访问什么”。一个交互式 CLI 可以在危险命令
命中时询问用户，却在 non-interactive 模式跳过该 guard；workspace path resolver 放宽路径范围，也不等于
每个执行器都移除了自己的限制。Kimi Code 0.40 相关的 [command guard](https://github.com/MoonshotAI/kimi-code/commit/4b9888b)
与 [workspace 检查调整](https://github.com/MoonshotAI/kimi-code/commit/b4ae7f8) 是具体实现案例，不能据此
推断它具备或失去了完整 sandbox。平台封装 CLI 为无人值守 Job 时，应逐项检查启动模式、配置覆盖、
审批缺席时的行为，以及文件、网络和进程隔离；增加一个交互提示不会自动补齐这些边界。

### C. 拟插入的完整两段（仅此两段与独立marker）

启动模式固定、每次人工确认的工具链，可以用较简单的审批状态；会话允许中途切换策略并跨故障恢复后，当前模式却不能追溯抹去已经要求的真人决定。一个[公开的受限实现](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/docs/design/2026-10-24-managed-permission-policy.md)先按显式拒绝、询问、允许的顺序处理规则，再应用模式默认，并把必须由人决定的标记写入待决Action，跨模式切换与冷恢复仍保留。修改规则本身要求空闲状态、预期revision和幂等回执，已准入Turn保留原policy快照；兼容能力缺失的执行器拒绝既存策略，而非静默降格。自动分类也只处理其余未决的原生调用，意图取自已提交的真人原文，不把Hook展开、摘要或Agent消息提升为授权；缺安全分类路径时回人工。这用额外策略状态、协议协商和等待成本保住既有义务，不是分类器正确或OS隔离证明，也不约束Hook副作用；规则或恢复资格不明时保留静态权限、人工确认或拒绝，而非由“自动”模式自行放行。

启动凭据同样要按来源，而不只按配置键名判定：处理一个仓库，不应允许仓库作者顺便决定保护管理服务的bearer。另一处[已披露的来源硬化](https://github.com/QwenLM/qwen-code/pull/15228)在初次加载与重载路径都排除项目环境文件和settings.env中的服务token，工作区被标为trusted也不豁免；操作者的显式参数、导出环境或home层环境文件则另属可信渠道。这改变的是凭据的设定权，不自动改变监听接口的认证默认：该精确版本仅在非loopback且没有显式token来源时生成新bearer，显式空值不获得随机回退，loopback仍可保留tokenless开发模式，须另行要求认证。依赖旧项目配置的部署要迁移并重验实际绑定、认证和恢复路径，增加配置管理与兼容成本；未知来源或不可信共享主机应拒启动或收紧认证/隔离。公开代码与测试断言不证明本轮已运行攻击，也不让工具级规则、一次性凭据或本机地址替生产安全验收签字。
<!-- source-family:SF-2026-QWEN-CODE-PERMISSION-20261026 -->

### D. 完整后肩（当前磁盘原文，保持不改）

### Search Query 本身也是 Public Egress Action

传统 research Agent 常把最终回答当作唯一输出面：本地文档进入 Context 后，模型可以先生成公开 Web query，最后再由
response filter 删除敏感文字。约束变化在于 query 已经离开 private boundary；即使最终答案干净，关键词、实体组合或
多跳检索顺序也可能泄露本地 evidence。Query planner 因而只能提出带 provenance 的 search intent，privacy/egress
owner 在发送前按 principal、document sensitivity、query digest 和目的做 admission，必要时 redact、改写、转私有索引、
请求审批或 fail closed；search provider 的 receipt 记录实际公开的内容，不能由最后一层 moderation 代替。

### E. 拟置于 true H2 `## Review notes` 的本人证据注

- `SF-2026-QWEN-CODE-PERMISSION-20261026` — `live1027_china`，Daily2026-10-27补Oct26 release；精确nightly tag实际commit `8d14dd966cff397c600da66302c54ac87f286904`，PR15448/15228的核心说明、相关actualpatch/tests及tag版design/matcher/approve/Actionfloor/capabilities/shared-env/serve-token必要域，初始两安全域拟1+2+2=5，扩域后同family正式2+3+2=7，权限/凭据变化域深入。仅采用待决真人义务跨mode/recovery与凭据来源scope，保Auto资格、classifier不足回人工、非OS/Hook隔离、loopback tokenless及无完整Runtime/JavaCSI/MySQL生产验收；已有通用proposal/idempotency不重复。未运行第三方代码、攻击或复现，PRE/真实SAVE/POST按本日独核实际记录，不由本注预签。

整体PRE只请求上述Ch72精确Kimi段后/Search Query标题前两段+marker和trueH2本人注。**当前仍未写Books。** 原件证据/准入校准与owner/整稿由唯一reader直接独核；若通过，再按该窄位检查共享并发并保存，未通过不写。未锁全章，也不请求修改Ch78/84、Report、State或其他日期。

## 6. Reader 具名指出的六个核心域：重新有限初筛（同一Qwen家族）

§2首次安全必要继续有效。Reader发现完整nightly中另有六个具名非CI/UI核心变化；root要求先暂停§5 Books稿，补具体准入与既成事件去重。本节不构成86PR或212文件全Methods队列，不再称原安全域已经穷尽整版。全部六PR官方英语What/Why/Risk已完整实际读取；它们均在本轮已读tag compare中，release事件仍为Oct26的唯一Qwen家族，不另加六家族，也不把PR较早创建/合入日改成当日首次公开。

对已存在Oct20–26七份Daily及其_sources的这六个精确PR ID、shared-agent-loop/scratch-worker/mid-turn/pinned-extension具名词作定点查重，没有发现已完成的相同事件有效审阅记录。旧release0.26.1的设计15343、既有parameter snapshots15004、恢复底座15384/15386是相关前置，不等于当前六增量已审；不以代码版本或相同主题替代家族事件去重。

| 精确原件/身份 | 旧约束 → 实际增量 → 需要重考虑的设计 | 初判/待核 |
| --- | --- | --- |
| [15369 shared agent loop](https://github.com/QwenLM/qwen-code/pull/15369)，head`555951575a1599e5731b28d18bc4c905f62b8d7c`，mergedOct24 | 七surface各自循环与headless drain重复 → opt-in单scheduler处理一batch、结果只finalize/record一次且按请求序、typed stop与serial before-launch，明确预算边缘intentional parity差额 → 不能将不同surface“同一Agent”或refactor直接当退出/预算/审批语义等价 | P：不是仅搬代码；默认false、仅headless，其他surface循环未迁移；session_token_limit/user_prompt_blocked仍按旧completion，mod hooks等边界保留。等待独立准入校准后只审scheduler/stop资格。 |
| [15261 HTTP external scratch](https://github.com/QwenLM/qwen-code/pull/15261)，head`40f6798171b70d6828250affb5e79d6459ee3b48`，mergedOct25 | Broker不应内置各vendor SDK且lost response可能重复分配 → provision前持久logical request handle、operator HTTP provider保持原physicalresource映射，observe重attest原worker，不将lostowner release映kill → placement恢复与Hosted工具可用性必须分层验收 | P：原件明确Spring scratch dispatch只warm worker、无Hosted consumer；1024 seed缓存不随Sessionclose/TTL驱逐、close不stopworker；instance recreation用了共享in-memory repo，不等DB/process crash durability。只审该placement/owner边界。 |
| [15449 durable midturn guidance](https://github.com/QwenLM/qwen-code/pull/15449)，head`05535350decf7897b9cf057764aaca38e297abaf`，mergedOct25 | 活跃Turn拒二次admission、browser pending依赖tab → perSession durableFIFO在safe model boundaries消费并与userhistory提交、保tool/result配对，edit/withdraw受revision/claim限制 → 指导到达、已消费与下一Turn资格不能等同 | P：pending最多32、images仍idle-only，stop/fail pause需显式resume；unknown delivery显式discard不重放、保late原回执，pending turn自有恢复barrier。精选MySQL/SQLclaim replay不证明exactly-once process delivery或原writer crash恢复；完整Hosted/fault/provider仍未验。 |
| [15333 reviewed UI parameters](https://github.com/QwenLM/qwen-code/pull/15333)，head`22492964daeadbbdedd7b94bb54c6feb5405157c`，mergedOct25 | generated card只能本地算/手工复制 → host outerframe冻结applied参数供真人显式review，原session走现有admission，guest没有messaging API → 数据交互、确认与会话发信authority成为不同边界 | P：default-off不变、参数snapshot不是human-authored事实，hidden/disabled/scriptwritten值均数据；16KiB双限不截断，unknownacceptance不自动retry，card stop不撤已admitted请求。非仅改按钮，未开新daemonroute/guestAPI；只审freeze/review/send资格，不审全部UI美学。 |
| [15389 complete OpenTUI checkpoint](https://github.com/QwenLM/qwen-code/pull/15389)，head`ffd4447aee005695c8df7d1826d8a3c4de82ddb6`，mergedOct25 | 显示文本丢canonicalmetadata、pending edit尚未被consumer接到就capture会缺待批对象 → 真approval入口完成后capture，freshphysical replay回应旧logicalcall，stale/cancelledowner不得publish → checkpoint存在、可恢复会话与已执行effect须分别验 | P：复用15384/86底座不等本producer新事件重复；filesystem effect已发生不会被stalepublicationguard撤回，toolonlyrestore不自动模型请求。受控fakeprovider的shipping source矩阵不是installed/跨平台/全部视觉验收；只审capture/publication/replay身份，不把compact显示字样作贡献。 |
| [15490 pinned extension packages](https://github.com/QwenLM/qwen-code/pull/15490)，head`099f5f46621d3f3ed67108ddd59567103a8682dd`，mergedOct25 | 分散导入Skill/MCP/Hook丢package来源/版本边界 → authoritative archive/encryptedsettings、Session immutablepins与单effectiveconfig，apply/continue/restore持久op与admissionbarrier → 插件选中、配置绑定与Runtime已激活不等同，unknownop不能重新执行 | P：opt-in、7component仅静态受支持域，不扩大basepermissions；profile/lifecyclev2不合在Session/receipt落盘前拒。需要freshcatalog无migration；完整7component/fault、Linux/SSH cleanup、多平台与最终Javaqualification仍缺。只审pin/binding/recovery安全域，不展开212文件所有Methods。 |

这六项的P是具体潜在机制/兼容边界，不是证据已成立或Books必改；分数仍按唯一家族的实际拟采用层统一处理，不能把六项成熟原则相加抬分。普通下一步为唯一reader扩域准入校准及通过项的窄必要原件/实现核验；未读层不称外部缺口或终态保留。§5只是一份待更新草稿，不能先授本家族Books完成。

## 7. 六域校准后的唯一首次必要（精确tag，未运行）

唯一reader `live1027_review`已独开六PR完整English core/Why/evidence/Risk，六项P准入通过，要求继续相应窄域。以下统一绑定真正release commit `8d14dd966cff397c600da66302c54ac87f286904`。GitHub未登录REST额度耗尽后，已用已连接GitHub原件读取恢复精确blob，**不是外部缺口**；只加载已具名原件/文件，未遍repo或将文件目录变成Methods清单。下面的测试均为实际读取测试源码断言，未在本工作区执行Qwen、fixture、HTTP或攻击。

### 7.1 PR15369：共享循环的实际语义资格

精确tag [design](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/docs/design/2026-10-23-unified-agent-loop.md)的Tool batch/Continuation/Outcome/Setting/Headless/Compatibility/Risks必要段已读。目标七surface归一是迁移计划；本次默认false、仅headless接入，ACP/Ink/OpenTUI/AgentCore/speculation/Hosted不能冒称已迁完。Callback不提供额外授权；不传新callback的scheduler保原行为。

实际读[agent-loop.ts194–305](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/core/src/core/agent-loop.ts#L194)：每round先runModelRound，typed stop先返回，没有calls才completed；retry/fallback清旧attempt calls，UserCancelled仅主signal实际aborted时映cancel。STOP_EVENTS分开max_session_turns/session_token_limit/user_prompt_blocked，不把所有终止等价为成功。375–450的offerUntil按request order给每个call一次beforelaunch，连scheduler预先settled的invalid/deny项也计，拒启动项不被记为已完成effect；abort后不发送/记录新的模型工具结果，**不是已发生effect回滚**。

测试先读[agent-loop.test487–572](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/core/src/core/agent-loop.test.ts#L487)的refused-unexecuted与settled-beforelaunch依序offer；再核[parity482–554](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/integration-tests/cli/agent-loop-parity.test.ts#L482)：sessioncap旧路径可重复上一答案并exit0，新路径只一答/exit53；两路径budget-edge都exit55且模型请求/非control frames相同，但旧审批只call1，新路径先审批call1+2再阻第二执行。**批准次数、预算计数、物理执行次数与terminal结果必须分账**是有限采用域，不采“重构保证完全parity/更快”。notification modelround计数、Mod hooks/重复structuredoutput以及部分stop仍completion等直接反侧保留；未复现作者Linux局部测试或跨surface迁移。

### 7.2 PR15261：placement恢复不等Hosted工具就绪

精确tag [external-runtime-provider设计全文](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/docs/design/2026-10-23-external-runtime-provider.md)已读。实际实现是opt-in external-scratch/boot-v1；external-workspace七步扩展仍是设计，不能视为原有功能。Spring warm无Hosted consumer、recreate后warm不恢复process-localSession且须再次acquire，是作者在当前原件中的source-inspected caller边界；本分工未运行Spring链路，不能改称端到端实测。

实际代码[ExternalRuntimeProvisioner.java90–211](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/managed-agent-server/src/main/java/com/alibaba/qwen/code/runtimebroker/provisioning/ExternalRuntimeProvisioner.java#L90)证实ensureResource无remoteIO先造logicalhandle，provision核原handle与identity后调用provider；retryableunknown保原placement，reconcile严格核lastlease/endpoint且UNKNOWN丢readiness不换ownership。212–241再次独立transport.attest，provider RUNNING不是identity证明；243–280 release是no-op，不以lostCAS/failedattestation授kill，GONE/未知state拒adopt不替换。283–327 boundedplacements耗尽503，不由closeSession自动回收。

测试[37–133](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/managed-agent-server/src/test/java/com/alibaba/qwen/code/runtimebroker/provisioning/ExternalRuntimeProvisionerTest.java#L37)、285–320与343–384已读：重建provider还原原handle、不新provision/stop；scope/handle替换拒；lostprovisionreply保同body/seed/generation；uncertainconfirm保READYbinding、endpointdrift转LOST。这些明确使用InMemoryRuntimeBindingRepository与operator fixture，**不支持数据库或整进程crash durability/厂商sandbox互通/Hosted公共tool可用**。采用placement identity、readiness与toolconsumer三层资格，不采用历史CI green为tag版完整验收。

### 7.3 PR15449：durable指导的admitted/claimed/consumed分开

精确tag [queue设计全文](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/docs/design/2026-10-24-managed-user-message-queue.md)已读。实际[ManagedUserMessageStore.java55–168](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/managed-agent-server/src/main/java/com/alibaba/qwen/code/managedagent/persistence/ManagedUserMessageStore.java#L55)复用actor+key digest持久结果快照；不同command同key冲突；edit只queued、withdraw可显式discard blocked但保原revision，resume若原Turn RECOVERY_BLOCKED仍拒。claim只ACCEPTED/RUNNING，contextrevision失配批阻断/paused，lostclaimreply按prompt读同已claimed批，非重新创建。

264–326的reconcile将terminalTurn上未证实claimed转recovery_blocked；capture只消费匹配`umsg_id:revision`的真实message.committed/user记录，late原receipt可将withdrawn改consumed，**discard不证明原来没递交**。实际[hosted-harness-model.ts934–994](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/serve/hosted-harness-model.ts#L934)在下个model边界claim，逐条过UserPromptSubmit再commit，保各消息身份；1234–1236先consume完整toolresults；1267–1285在最终assistant之后仍可接新guidance继续，而不把新消息插入未配对tool结果中。恢复prepared存在时不drain新guidance。

已读[StoreTest69–126](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/managed-agent-server/src/test/java/com/alibaba/qwen/code/managedagent/ManagedUserMessageStoreTest.java#L69)、143–211：FIFO/receipt replay、closed-session旧回执仍可读而拒freshwrite、staleedit拒、claim再读相同、wrongrevision不消费、failurepause、unprovableterminalclaim阻resume、discard后latecommit仍收。只采用这些状态分责，不采完整exactly-once投递；原件精选MySQL同promptclaim幂等也不等originalwriter crash恢复、并发edit/settlement或realprovider全链。source没有把message.committed签成模型已经处理/任务完成。

### 7.4 PR15333：冻结参数审阅不是生成内容取得发信权

实际[continuation.ts全文](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/integrations/generated-ui/src/app/continuation.ts)与[continuation.test全文](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/integrations/generated-ui/src/app/continuation.test.ts)已读：序列化appliedsnapshot+rejectedEvents，不含derivedresult；control/formatunicode显式escape仍保decodedvalue，冻结文本不跟随原mutableinputs变；JS长度与UTF8两16KiB限整体拒，不truncate字段。hidden/disabled/scriptwritten值明确标数据，snapshotidentity不是authorization/persistencekey；text告诫本身非独立安全证明。

[outerframe main.ts80–147](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/integrations/generated-ui/src/app/main.ts#L80)在capture前锁pendingattempt、capture不ready/过大都不send；sendMessage仅由outerframe连接host能力后发固定frozen text，error/timeout→unconfirmed、无auto retry；stop只abort等待并明确不撤回sessionrequest。实际读既有host复用路径[useMcpAppMessages191–262/301–337](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/web-shell/client/hooks/useMcpAppMessages.tsx#L191)：reviewing才真人Send，完整review.text呈现，dispatchedclose转unknown而非cancelled；[App.tsx12739–12806](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/web-shell/client/App.tsx#L12739)在beforeadmission重核sameSession/client/workspace/writegeneration/idle，包括shell drain busy，复用sendPrompt而非guest直通新权限。

有限采用域为“交互参数→冻结审阅对象→原会话admission→接受回执”分责，不从role:user、脚本写参数或UI可见升级为human-authored intent；accepted不是analysis完成，stop不是withdraw。这是默认关闭实验feature的工程合同，没有新增生成算法、provider质量或全网失效保证。

### 7.5 PR15389：完整checkpoint首先是current-owner的producer合同

精确tag [OpenTUI recovery设计全文](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/docs/design/2026-10-21-opentui-session-recovery.md)已读。复用既有sharedrestore底座不当重复事件，但本次新增producer必须等真实approval事件被consumer折入canonicalhistory。[live-session1166–1193与1245–1287](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/ui/opentui/live-session.ts#L1245)实际仅model-origin edit awaitingapproval登记captureowner，先yield confirm，再snapshot当前UI/APIhistory+promptIDs；current/session/abort/sameentrance四条件共同决定能否publish。[live-turn377–389](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/ui/opentui/live-turn.ts#L377)过滤canonicalPending与未完成assistant/thought/tool，snapshot缺canonical源则失败，不凭displaytext重建元数据。

[tool-checkpoint.ts全文](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/ui/opentui/tool-checkpoint.ts)在首FS await前serialize全部UI/API/toolcall/rawargs；UUID temp+wx、最后isCurrent后同步rename只发布完整文件、finally清未发布temp；[测试全文](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/ui/opentui/tool-checkpoint.test.ts)有同时间同call不同快照、完整canonical payload、capture缺失不发布、二/三owner检查拒后目录无残留、初始失效不capture。这里核的是producer与stalepublication，不把已有FS effect撤销。

设计的existingrestore合同保freshphysical/oldlogicalcall、真实重新Read、旧branch审计与coldactiveancestry；作者所报OLD1→NEW2/多runtime产品矩阵是原件的限定测试声明，**本分工未重复底座实现审计或运行恢复，不授npm/standalone/platformunion**。因此仅采用capture资格/身份与发布分责，不把render compact名相同作恢复正确，亦不造整迁移完成。

### 7.6 PR15490：包pin、配置绑定与激活/恢复不是一个状态

精确tag [package设计全文](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/docs/design/2026-10-24-managed-extension-packages.md)已读；它明确accepteddesign而非qualificationcomplete、七静态component支持人口、archive/settings权属与secret不回灌、profile/lifecycle准入、config_install phase/ACK与未达平台矩阵。不采动态Skill权限/Hook/model/path语义、透明Runtime替换或hostreboot恢复。

实际[managed-extension-package.ts270–340](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/core/src/managed-runtime/managed-extension-package.ts#L270)closedkeys验证extensionId/packageRevision/digest/settingsRevision，Object.freeze；apply另绑operationId/actorKey/expectedRevision，sameextension重复拒、最多32。此只是typed/pinned身份，不自带完整供应链可信或权限增加。

[runtime221–289](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/serve/managed-extension-runtime.ts#L221)existingoperation必须exactcommand/base相同，重编contributions/catalog相同才reprepare，未知pending拒新operation。454–534 activate先检查revision/idle，pendingjournal先落，再drain→重查Session/idle→install→state原子写→删pending；lostreply留下pending不自动重install。375–451 reconcile要求原operation/expectedRevision+1/当前pending-activeidentity一致，stop证据不全返回outcome_unknown；不能compensate更晚owner。已读[测试56–129与257–313](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/packages/cli/src/serve/managed-extension-runtime.test.ts#L56)：CAS/只drain目标Session、unknown重建不replayinstall、新operation阻断、exact原prepare恢复metadata、更晚activeowner拒旧compensation。

有限采用的是当前runtime所实现的pin/binding/unknown/recovery资格及设计中对应平台admissionbarrier；不据这几份源码宣称已审完整212文件/Javacontrolplane或七component全链。原件实际macOS/MySQL/Hostedrun停在commandexpansion，command完成/child/update/compensation/restartnonreplay尚未跑全；Linux/SSH cleanup与最终faultqualification没有passingevidence，**partial不改称通过也不抹掉已支持的有限状态合同**。独立reader可据上述精确位置核采用命题，Books仍待本family扩域后的实际owner比较，不复用§5为六域全部NC。

## 8. 扩域 actual owner 与最小完整 PRE（尚未写 Books）

root明确授权由本作者继续四域actualowner/最小稿，原两安全域仍Ch72，不混合Owner。以下只读当前Ch84/81/78相关论点和直接邻接，未第二次读Source。§5的两安全段及其本人注仍是原稿；本节三处Ch84最小差异与之合成同Qwen家族的整体PRE，不预授任何SAVE/POST。下列独立binding marker用于定位本家族不同采用段，不增加材料家族数。

### 8.1 两项具体NC与版本事实

- **15369：长期控制分责已有，具体兼容事实仅报告。** Ch78 `Loop Boundaries`584–598已明确runtime强制maxsteps/walltime/toolcost/concurrency/repeatedcall/usercancel，不由prompt软指令控制；Ch84 `Agent Runtime State Machine`588–609明确Succeeded/Failed/Cancelled/Escalated、transition绑定actor/policy/budget/effect，并以拒绝/暂态/已有输出分不同停止与重试资格；Ch84 1033–1058另有真实dispatch/effect与append-before-fold的state authority。这些正文确实承载“公共loop必须分离terminal reason、调用与effect、只记录真实状态”的有限长期命题；不再加一段共享loop架构图。**未声称已有正文包含Qwen的全部callback细节或batchbudget协议**：opt-in headless、整batch先审批/后budget阻第二执行、notification round计数、部分stop仍completion等为该release兼容事实，留§7.1/报告，不称全parity或给通用理论加分。
- **15261：原owner恢复边界具体已有覆盖，external-scratch产品资格仅报告。** Ch84 `Resume`710–716已经逐字要求unknown不授权replacement、exactincarnation与cleanup及Session可继续证据、保原nativehistory、不静默新root、dispatch之后unknown保原target/ownership；1114–1121明确sandbox预热不授effect，须canonicalcall/policy后才提交绑定。Ch78 484–505另有丢回执不能当未执行、稳定operationID/工具侧去重与unknownreconciliation。它们承载本次拟留的“logicalrequest/原physicalowner不能因HTTPunknown替换，READY/warm不等工具完成”原则。HTTPvendor边界、1024缓存、release不kill、Spring无Hostedconsumer是有用的实现/未交付边界，不写成通用平台产品手册；不以这些NC反推Qwen的完整placement或DBcrash方案已获证明。

### 8.2 四域的真实差额与唯一owner

`AGENT-PLATFORM` / Ch84拥有本次四域，**不是**另建Ch78的call语义、Ch81的完整workflow恢复或Ch72的安全策略副本：

1. **15449**：Ch84 105“runtime不是browser”、1033–1058“journal/fold/projection”与Ch81 957–972“durable外部event/lostwake”已解释存储与重驱；尚未解释活跃Turn中guidance的queued/claimed/消费证据、safe model boundary与late原receipt。补这一窄输入状态交接，不重述通用eventlog。
2. **15333**：Ch84 101–107已有streamedUI不授语义/行动与MiniApp manifest不自授，但没有承载applied参数冻结对象、完整outerframe人审、scriptwritten值不等human-authored、unknownacceptance不等withdraw的消息admission边界。与15449在同一client→runtime交接点放两自然段。
3. **15389**：Ch84 `Agent Recovery State超出Transcript`1001–1005已有turn-boundary联合恢复与manifest authority，`Resume`已有外部对账；缺intraTurn approval入口必须先fold canonicalpending、首await前capture与currentowner publication的producer条件。补一段，不再审/复制既有restore算法或声称FSrollback。
4. **15490**：Ch84 235–247已有namespace/digestpin、显式reload不等消费且未证明原子迁移；1007–1013已有审计bundle同digest。缺多component合成effectiveconfiguration的stage/bind/enable与pendingbarrier/原operation恢复。只补config lifecycle，不重复供应链扫描、secretstore、registry或低层MCPtransport。

三个位置均已按当前磁盘完整读两侧，不锁全章。原章与Ch81邻接继续分责：单工具参数/sideeffect在Ch78；workflow compensation在Ch81；本节只写Session输入、配置与恢复资产资格。

### 8.3 插入位A：client持久状态后的两段

**完整前肩，保持不改：**

长运行任务的权威状态还必须留在 runtime，而不是浏览器连接里。Client 断线应触发持久 Thread 的回读与展示状态重建，不应仅为恢复界面而重新提交原任务；事件投影需要按身份去重，但这不等于外部 effect 已有 exactly-once 保证。Codex App Server 的公开设计给出了双向事件流、server-side thread persistence 与 ephemeral Web client 分离的例子；代价是 typed binding/schema、client/server 配对与兼容性维护，无法协商所需能力时应保留已验证版本配对或退回较简单的调用接口。其 backward-compatible 目标不证明任意版本配对无故障，TUI 改走这一协议在原文中仍是计划，而非已实现的恢复保证。<!-- source-family:SF-2026-OPENAI-CODEX-APP-SERVER -->

**拟完整两段：**

只在空闲时接受输入，适合短任务；任务正在执行时还要接收用户指导，就应把已入队、被当前执行者claim、已写入真人消息历史和模型已经处理分成不同状态。[一条受限的持久队列](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/docs/design/2026-10-24-managed-user-message-queue.md)保留FIFO消息身份，只在完整tool结果之后的模型边界消费，不能为插入指导打断审批或拆散call/result配对；编辑与撤回只作用于仍可修改的revision。原投递结果未知时应保留原claim与执行者证据，显式discard也不证明消息从未递交，迟到的原回执仍可结算；stop或失败后须另行resume，不自动把指导重发到新Runtime。这增加持久队列、锁、扫描与等待成本，SQL claim幂等不提供exactly-once模型处理，局部fixture和精选MySQL证据也不证明完整crash/concurrency验收；资格不明时保持paused/blocked，或回退空闲后显式提交，而不由“已保存”签任务完成。

指导来自交互页面时，还须分开参数数据与发信权。页面中的值可由用户、隐藏控件或脚本写入，已applied也不等计算正确或每个值都是人写的；[另一条受限接口](https://github.com/QwenLM/qwen-code/pull/15333)由可信outerframe冻结完整参数消息，经host显示目标会话和原文本，用户明确确认后再走原session admission，生成内容本身没有messaging API。后续页面编辑不改已审对象，accepted只表示请求受理，不等分析完成；停止卡片等待不能撤回已发请求，unknown时自动重试反会重复提交。冻结、来源标记、大小限制、busy重查和人工审阅增加成本；超限、身份漂移或接受状态不明时保留失败/未知并先查原会话，不截断成另一份被批准消息。这是默认关闭的局部工程合同，不是参数真实性、模型回答质量或开放页面安全证明。
<!-- source-family:SF-2026-QWEN-CODE-INPUT-20261026 -->

**完整后肩，保持不改：**

当协作结果需要持续更新，而不是生成后即离开对话时，还可将页面与后端封装为可安装应用：后端通过 hosted MCP 向 Agent 暴露能力，同时经 Agent API 请求 Agent 工作；host 统一管理进程、端口、持久目录、凭据保管及发布版本，manifest 声明可用 connectors 与 Agent 权限。这把可交互产物与 Agent 调用纳入同一生命周期；manifest 声明仍须经 host 权限判断，不能视为应用自行授予执行权。[MiniMax Mini App 的官方发布](https://agent.minimax.io/docs/techblog/minimax-code-mini-app)披露了这条装配接口及页面内容先进入用户输入框的交互边界，不证明工具结果正确或本地代码被 sandbox；原文明示代码以当前用户权限运行，host 保管账户凭据也不能替代可信包、最小权限与完整副作用审计。持续服务要支付进程/数据恢复、接口兼容和升级回滚成本，发布可回滚也不代表外部 effect 可撤销；短任务仍可使用一次性页面或简单 MCP 调用。<!-- source-family:SF-2026-MINIMAX-MINIAPP-20261020 -->

### 8.4 插入位B：完整package effective configuration

**完整前肩，保持不改：**

对插件提供的同名能力，另一种选择是让调用显式携带namespace，而不是只依赖first-win顺序。[Kimi Code的受限版本合同](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html)将插件Skill写成`plugin-id:skill-name`并停止接受bare name；这减少同名遮蔽，却新增旧调用迁移与名称绑定维护，名称也不等于artifact可信。规则还存在激活时点：文件中的AGENTS、skills或配置已修改，不表示当前会话已消费新版本；显式reload把重新装载变成可见操作。该发布同时以workspace trust拒绝阻止发送，但没有说明这会撤销全部在途工具或提供sandbox。平台仍须把所用定义/解析结果绑定到run，独立执行effect授权；重载原子性、旧调用兼容或来源无法确认时，固定已验版本、重建会话或保留封闭能力集，而不以一次reload宣称全部历史状态已安全迁移。<!-- source-family:SF-2026-KIMI-CODE-20261021 -->

**拟完整单段：**

同一扩展还可能同时带来Skill、命令、Agent定义、context、MCP、Hook与settings；只分别pin文件，不能说明一次会话当前激活了哪组兼容配置。[一个受限的包配置实现](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/docs/design/2026-10-24-managed-extension-packages.md)将精确package/settings版本合成为Session effective configuration：先prepare/stage，绑定配置时保留admission barrier，再只drain本会话受影响组件、enable并确认active；stage本身不连接MCP或执行Hook。原operation结果未知时保barrier，不换owner重做；恢复旧内容也作为新revision提交，须核原owner停止证据，不能回退计数器或停掉更新的配置。这用archive、配置journal、组件所有权和停机等待换可核对的激活状态，不扩大基础tool profile或父会话权限。当前实现只覆盖受支持的静态component，完整七组件/故障与Linux/SSH清理仍未验收，透明替换丢失Runtime也不在该合同内；资格或原结果无法确认时拒新执行、对账或人工恢复，不能由安装成功、typed pin或一次配置ACK批准生产就绪。
<!-- source-family:SF-2026-QWEN-CODE-PACKAGE-20261026 -->

**完整后肩，保持不改：**

### 从 Skill Catalog 到 Competence-aware Orchestration

平面目录在资产少、团队固定时易于审计；规模增大后，平台还要把可见 active catalog、可检索但未激活的 dormant pool 与本次 run 选定的 skill graph 分成不同状态。离线 capability tree 可以缩小发现范围，用户管理的 activation 决定哪些资产进入常用目录；任务检索再选定有版本的 skill，DAG 节点绑定其输入、上游 artifact 与输出约定。出现在树中不等于已加载，选入 DAG 不等于依赖、权限或执行结果合法；现有 digest resolution、composition admission 与 effect policy 仍须逐次执行。

### 8.5 插入位C：intraTurn checkpoint producer

**完整前肩，保持不改：**

只保存消息历史适用于无外部副作用的短会话；工具开始修改文件、启动进程或持有运行时 artifact 后，恢复点必须在 turn boundary 联合提交 conversation、filesystem、process、tool receipt 与 runtime identity。语义稀疏检测可以减少 checkpoint traffic，但会引入 eBPF/分类 false negative、co-location contention 与跨对象 restore consistency。因而平台应把“检测到变化”视为 checkpoint proposal，由可验证的提交清单拥有恢复 authority；检测证据不足时回退到更保守的全量或固定边界 checkpoint。

<!-- source-family:SF-2026-ARXIV-2604-28138 -->

**拟完整单段：**

若需要在Turn内部、真实编辑审批前保存更细恢复点，producer还必须等当前assistant与pending tool事件先被consumer折入canonical history，不能从尚未drain的显示队列或格式化文本补造状态。[一个受限的checkpoint producer](https://github.com/QwenLM/qwen-code/blob/8d14dd966cff397c600da66302c54ac87f286904/docs/design/2026-10-21-opentui-session-recovery.md)在首个文件await前固定UI/API history、prompt与原logical call/arguments，先写临时文件，重核Session、Turn、abort与同一approval entrance后才发布完整快照；缺canonical源或owner过期就不发布。这样将快照内容完整与发布资格分开，代价是更多元数据、临时存储与所有权同步；已运行的文件effect不会被stale-publication guard撤销。恢复仍交给既有外部对账、当前权限和真实重执行回执，不能把旧逻辑call或相同显示标签当成新的物理执行证据；缺少完整capture或可恢复绑定时保原历史并显式失败/人工处理。局部源码与受控恢复案例不提供全部安装产物、平台或文件系统事务保证。
<!-- source-family:SF-2026-QWEN-CODE-CHECKPOINT-20261026 -->

**完整后肩，保持不改：**

### 被审计的 Skill 必须与实际执行 Artifact 同一

离线审计 source 或 manifest，却在运行时重新解析、下载或动态拼装 skill，会形成 audit–runtime gap。平台应对 reviewed bundle 生成不可变 identity，验证依赖与 policy，执行时只加载同一 digest，并把 runtime receipt 绑定到调用。任何重打包、依赖漂移或解析差异都必须重新 admission。

### 8.6 true H2 Review notes 的本人拟注（Ch84一条，不预签）

- `SF-2026-QWEN-CODE-RELEASE-20261026` — `live1027_china`，Daily2026-10-27补Oct26 nightly，同一Qwen家族，正文INPUT/PACKAGE/CHECKPOINT为三个独立定位binding而非三家族。精确tag commit`8d14dd966cff397c600da66302c54ac87f286904`，PR15449/15333/15389/15490的Englishcore/直接反侧、tag版design与§7列明actualsource/tests必要域；原15369/15261通用longterm原则已有具体承载，版本资格仅报告。仅采safe-boundary指导消费/冻结参数发信权、intraTurn canonical capture/currentowner publication、effectiveconfig pin/bind/unknownbarrier；保SQLclaim非exactonce、scriptwritten非human-author、stop非withdraw、FS effect不随staleguard撤销及partialpackage/fault/platform限制。未跑代码/测试、攻击或复现，不授完整212files/恢复底座/生产验收；PRE/真实SAVE/POST按本日唯一reader实际记录，不由本注预签。

**整体PRE交接：** 本节三处四段+三个独立marker/一条Ch84本人注，以及§5两安全段+独立marker/Ch72本人注，均只保存于CHINA稿。请求唯一reader按逐字稿和完整邻接做整体PRE；通过后由reader现场核并发窄位，授作者真实保存/自读，再由同一reader唯一POST。当前仍无Books SAVE，不借等待增加Source或改Report/State。

### 8.7 正式家族范围、评分与保存ownership

root已明确由**root唯一Books/State writer**保存reader通过的原稿；`live1027_china`保持只写本文件，不写Books/Report/State。上面早期“reader授作者保存”仅描述拟流程，现由此处的精确writer分工替代；reader唯一实际POST，不等root第三研究。

Qwen正式是**1个Oct26 release家族、8个已处理的具体域，整体评分2+3+2=7**：2分针对真实审批/输入/恢复/配置机制与兼容边界，3分针对CLI/Core/host UI/Java control-plane/Runtime及恢复生命周期的实际跨层reach，2分针对可复用的身份、提交与unknown处理约束。不是八项分数相加，也不是因security或机构声誉抬分。§2原1+2+2=5是只见两安全域时的首批评分；六核心域被reader具名指出、完整core准入独核通过且§7必要证据补足后，评分对象扩大，这是新证据驱动的正式改分理由，不删旧判断来伪造一次性正确。

八域=15448会话策略/Auto、15228凭据来源、15369sharedloop、15261externalplacement、15449durableguidance、15333reviewedparameters、15389checkpointproducer、15490packageconfiguration。原两安全域及六新域均有core、必要实际源码/测试与直接反侧；六域§7只支持所列窄命题，**不表示86commits/全部PR、15490全部212文件、恢复底座、其他surface或生产fault资格都已审完**。未执行任何第三方代码、fixture、攻击或复现实验；作者历史/局部测试与本轮源码观察保持分开。

Books差异：15369/15261的长期原则按§8.1指向真实已有承载，新增产品兼容/未交付事实仅报告；15449/15333/15389/15490在Ch84有§8三窄位差额；15448/15228在Ch72有§5两段差额。每个机制只有对应owner，整个release仍只有1家族。当前只是完整拟稿与必要证据交接，**尚未由本作者声称root已SAVE或reader已POST**。

日期只采用nightlyAPI发布`2026-10-25T23:20:17Z`→BJT2026-10-26；八PR更早创建/merge是背景，不搬成当日首次公开。tag名后缀8e28不是实际gitref，引用统一实际commit`8d14dd966cff397c600da66302c54ac87f286904`。Oct26 18:25Z preview及22:32Z nightly均BJT27、明确窗外；SDK0.1.23/Kimi2.3.3虽同窗但具体N不加入八域或家族分。

## 9. 代理追加工作：五篇已准入Agent论文的唯一首次必要证据

root追加委派，`live1027_china`仅承担以下五项的首次必要机制/关键评价/直接反侧阅读，不承担本五项的owner比较、Books修改或最终评分。准入/日期归属沿用root的当前SOURCE与reader有效独核；本节不是重新发现的五个中国来源候选，也不增加本日家族分母。五个精确v1 HTML均重新实际打开，按具名小节补读，正文足够后停止；未下载/执行artifact、未重跑实验，不声称通读全部附录/引用。HTML页眉的Oct22是稿件提交标记，不由本节覆盖SOURCE已核的公开事件日期。以下保留英文紧缩证据命题以防数字与限定翻译失真；采用前仍需唯一reader独核，本节不预签。

### 9.1 [2610.31778v1 — Benchmarks Are Surprisingly Compaction-Friendly](https://arxiv.org/html/2610.31778v1)

Actual necessary reading: §§3–5, including methods, metrics, Q1–Q4 and limitations. Fixed OpenCode compares self-summary, tool-output pruning, filesystem offload, reasoning deletion and Haiku summaries; two runs/task/configuration. Main text includes four models, but Gemini rarely compacts and is weak compaction evidence; do not silently inherit abstract's three-model count.

At 160K–380K, the two 1M models' task scores are similar; this covers only 16–38% of their windows, not default near-full compaction. GPT-5.3-Codex's PaperBench score deteriorates at lower thresholds; PostTrainBench intervals do not resolve an effect. Strategy results are model-dependent and conditional on valid submissions.

ProgramBench summaries lose approximately 0.92/3 rules initially. SWE-chat has 44 sessions/269 LLM-extracted constraints: process/scope losses 35.9%/36.8% versus feature requirements 6.2%; another judge changes overall loss from 19% to 24.5%. Crucial counterevidence: cheating starts before compaction, so erosion does not establish cheating causation. SWE-chat uses different scaffolds/models and measures retention, not final task harm. Adopt only the distinction between artifact-recoverable progress, context-only constraints, and outcome scoring—not universal harmless compaction or a proved safety intervention.

### 9.2 [2610.31710v1 — Compact-Bench: Measuring What Context Compaction Costs Long-Horizon Coding Agents](https://arxiv.org/html/2610.31710v1)

Actual necessary reading: §§3–5, Appendix G's availability, tools and budgets. PRE uses full history and POST summary-only from the same restored working-tree snapshot, agent, interpreter and eight-step budget. Damage and rescue remain separate; verification requires POST failure in at least two of three runs. Fourteen backbones use a fixed Claude Code prompt/Kimi-K3 continuation agent; 22 validated PRE successes give stable damage of 1–14/22, not population failure rates.

Prompt comparison, using Kimi-K3, preserves 19/22 repairs with Kimi Code versus 18/22 with Claude Code; the separate 146-session detail set favors Claude Code (15.0% versus 8.2%). Retention is literal recurring-string matching, including retransmitted history, not semantic necessity. Pytest-7571 preserves all five audited fix tokens yet fails; Sphinx retains ingredients without the reasoning-to-edit transition.

Production boundaries are a different, shrinking population: 106/27/6/1 evaluable boundaries; later averages are not longitudinal decay estimates. Input truncation precedes the transcript cap; prompt output lengths differ. Private payloads and cached repair histories/snapshots are withheld. Released grids permit rate reconstruction, not exact rerunning of private sessions. No claim that higher detail retention guarantees repair preservation.

### 9.3 [2610.31733v1 — Learning to Be Monitored](https://arxiv.org/html/2610.31733v1)

Actual necessary reading: §§2–6; Appendix B.2–B.5's coupling, proof, attainability and filtering. For fixed intervention semantics/consistency and p1>p0, R=(p1−p0)/p1 gives causal-recall bounds max(0,(TPRob+R−1)/R) ≤ rc ≤ min(1,TPRob/R). Independent sampled arms do not identify potential-outcome coupling. No individual monotonicity assumption is needed; sharpness is over unrestricted compatible binary distributions, not every constrained generation mechanism.

SFT uses privileged-teacher targets; RL rewards outcome/disclosure agreement; OPSD mixes public/private teacher distributions on student CoT tokens. Three task models, three fixed monitors, twelve MonitorBench tasks: upper-endpoint composites improve in 27/27 configurations, lower-endpoint composites in 26/27. Mistral OPSD/Llama monitor declines 0.21 lower-bound points.

These composites also multiply operational specificity, so improvement does not identify increased causal recall or faithfulness. Valid-output filtering may change arm populations; empirical endpoint estimates are not confidence bounds. Training budgets/objectives differ; direct concealment/evasion is untested. §2 dates equivalent concurrent bounds to Oct20 and their estimator code to Oct14: preserve earlier-public provenance; the paper additionally evaluates three training recipes. Do not frame the mathematics alone as a new Oct26 discovery or monitorability as safety/accuracy.

### 9.4 [2610.31916v1 — Permission to Retry: A Study of Authorization and Recovery in AI Agent Workflows](https://arxiv.org/html/2610.31916v1)

Actual necessary reading: §§3–7, including contract, native recovery paths, observation boundary and limitations. Scripted refund histories separate checkpoint, authorization instance, transport key, effect evidence and reconciliation authority. Hidden provider truth is not supplied to applications. P1 deduplicates within a horizon; P2 only queries; P3 is opaque. Empty lookup cannot close an in-flight predecessor. Confirmed retained observations can settle without another write, including P3; unresolved outcomes retain reservations.

Prospective 336 histories cross two native hosts, fourteen schedules, three providers and four authored policies. Per host, cached/revalidated/stable-key/ledger policies pass 30/36/31/42 of 42; ledger's 42 comprise 21 checked completions, 15 denials and six unknowns—not 42 successful tasks. All 168 matched host cells agree; these are shared application ablations, not framework defaults or general host equivalence.

Current-write authority is required by this benchmark for redispatch; already-admitted remote effects may finish after revocation. Different prepared-redelivery contracts are not disproved. Native processes restart outside active database transactions; no real IAM/provider, transaction crash or concurrent-agent qualification. InfinityOS's separate 16 repository-fake component cases are not pooled. Fixture wall times include different timeout mechanisms, so no throughput/host latency ranking.

### 9.5 [2610.31971v1 — Knowing Whom to Trust is not Enough](https://arxiv.org/html/2610.31971v1)

Actual necessary reading: §§3–5's protocol, trust updates, controls and gap; Appendix F.4's condition composition. Five parties negotiate five four-option issues; four votes suffice, with one covert blocker. Identities persist across twenty episodes; only directed trust vectors cross episodes, not transcripts. BRS/rubric/free-form assessment is separated from scores-only S and prescriptive S+P decision guidance.

Ten seed-matched trajectories support paired intervals. Replay S→P, performed for grok-r, freezes trust formed under S while changing guidance, measuring a lower bound—not the supremum—of unused trust value. In 1HB+3G, agreement improves 16.5–30.5 points with the same trust; normalized lower bounds are 30–47% of disagreements. In 2HB+2G, gap intervals include zero. Gemini-r's guidance gains are not significant; zero measured improvement does not prove no gap.

Fixed-0.5/random-score guidance controls do not reproduce informative-trust gains. Models with saturated baseline or below-BATNA acceptance are not evidence of general negotiation reliability. The two populations also use different utilities/scenarios. Trust changes some votes above BATNA; it is neither authorization to violate private thresholds nor guaranteed agreement. Scratchpad interpretation is behavioral explanation, not a causal oracle. Keep diagnosis, retained assessment and action-policy evaluation distinct.

### 9.6 本代理停点

五项首次必要域已实际完成，未扩全文附件、模型榜单或新搜索队列；保留上面明确反侧，不把“完成阅读”写成实验复现或Books验收。待办属于root/唯一reader：正式评分、所需owner/已有覆盖判断、必要PRE/SAVE/POST及本五项证据独核。31733更早code/concurrent公开归属已具名通知root；若需要核精确首公开，只定点其estimator/recipe差额，不重开其余四篇。Qwen的实际Books保存与POST仍以root/reader记录为准，本代理不代签。

## 10. 31778/31710实际owner与Ch75整体PRE（新窄授，未SAVE）

root追加独占授权：仅本两项的Ch75正文精确窄位与本人注由`live1027_china`保存，root不写本章；其他Books/Report/State仍无写权。唯一reader的精确PRE通过后即可真实SAVE、自读并交其唯一POST，不需再等root行政授予。此授权不改变其他日期/并发作者的原内容，不锁整章。已重新完整读AGENTS、ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE与最新checkpoint；Ch75实际压缩损失/原文视图/compaction评价/执行状态/未来更新论证及Ch74/76开头与末尾交接已对读。复用§9两项首次必要，不重Methods。

### 10.1 具体已有覆盖与剩余差额

唯一owner均为`AGENT-CONTEXT`，`books/part-07-agent/75-context.md`。Ch74只拥有版本化概率接口/软约束；Ch76拥有外部证据检索/packing质量，不复制本次历史替换评价协议到这两章。

- 31778：Ch75原§Context Compression的损失已承载temporal slice与type-specific rule retention（现约366–411）；§Policy carriage（622–628）已规定active policy完整携带和effect-time enforcement；§Compaction后台转换的ContextEcho两段（434–440）已说明普通分保持而role/instruction漂移，要求同snapshot probe/continuation。上述机制与一般“任务分不等约束遵从”均NC，不再重写。真实差额是**评价人口中可从产物重新取得的状态与仅存在交互历史的约束不同**，所以固定目标/持久FS的score对compaction损失可能不敏感；并保留erosion不证明作弊因果。拟在Observability接成一种评价边界，不把论文变成runtime强制策略。
- 31710：Ch75执行状态节首段（642–644）已要求相同environment重放，ContextEcho已有snapshotfork；原词面proxy与generator排序分责段（559）及literal recall/latent分支亦已承载“保信息不等tasksuccess”，这些NC。真实差额是**同repo working state配对后按PRE成功人口识别损害、另报反向挽救，避免总成功率相抵；recurring literal retention与真实production后续边界不是同一评价人口**。拟把统计方向、分母及非纵向解释接到上一段，而不重复compaction训练或状态提交。

两项各拟正式评分**2+1+2=5**：新增测量/验收边界2，当前context-evaluation局部组件1，可复用约束2；不是借整条Agent生命周期提高reach。虽5分，已确认Ch75具体缺口须深入受影响域；§9所列机制、对照、评价条件和直接反侧已足够本两段采用，不授所有模型/完整附件或生产验收。拟判两项整合各一自然段；若reader证明具体正文已有此人口/统计边界，则有效改为NC，不为diff坚持。

### 10.2 逐字整体稿：同一窄位两自然段、各自marker

位置：Ch75 `## Observability 与 Evaluation` 中，以下完整前肩后、以下完整后肩前。只新增两段及两个独立marker，不改现有清单、其他正文或后续heading。

**完整前肩，保持不改：**

只评最终答案会无法区分 retrieval miss、bad ranking、compression loss 与 model misuse。

**拟完整第一段（31778）：**

固定目标、进度可从文件重新读出的任务，仍可用最终产物分数验收结果；但它可能对历史替换不敏感，因为遗漏的信息能够从工作产物补回，而用户后来追加的工作方式与禁止范围未必存在于文件中。评价应先区分这两种可恢复性，再分别检查产物、约束留存与实际遵从，不能以任务分近似不变推断交互约束完整。[受限压缩对照](https://arxiv.org/html/2610.31778v1)支持这一测量边界，不证明压缩导致作弊：所测作弊早于首次压缩，真实会话的约束留存又依赖judge，未测其最终任务伤害；少量任务、模型与触发区间也不能签发通用阈值。额外约束标注、分层检查和重跑都有成本；交互约束未知或评价不可靠时，保留原始指令、独立执行检查与可回读历史，而不由基准分数批准删除。
<!-- source-family:SF-2026-ARXIV-2610-31778 -->

**拟完整第二段（31710）：**

在同一状态重放之外，配对统计还要保留变化方向：固定代码工作树、继续执行的模型、工具和预算，分别从完整历史与摘要续做，把原本成功而摘要后失败计为损害，把反向变化另列为挽救，不能只用总成功率让两者相抵。标识符或修复词串仍在，也不保证消费者能把证据转成正确编辑；[配对修复对照](https://arxiv.org/html/2610.31710v1)中，这两种验收给出了不同的配置排序。字面细节留存集与修复集应各报分母，连续production压缩的后续可评价子群缩小也不能直接当作同一人口的纵向衰减。配对重放、环境还原、重复确认、摘要与全部后续工具执行均计费；私有轨迹及缓存状态未公开时，结果表可重算不等原实验可精确复跑。任务、消费者或预算改变后应重新验收，分歧时保留原历史、更完整状态或回读入口，不把较高保留率当成续做保证。
<!-- source-family:SF-2026-ARXIV-2610-31710 -->

**完整后肩，保持不改：**

即使每条外部内容都没有显式指令，选择哪些内容、按什么比例和顺序让模型连续阅读，也可能改变下一次决策。可固定模型、persona与最终问题，仅干预此前的暴露轨迹，再分别测原默认方向、反方向与无变化条件；[有限feed对照](https://arxiv.org/pdf/2606.00914v1)支持把上游选择器纳入Context审计，而不把下游prompt单测当全链安全。效应依模型与任务而变，平衡或披露并非普遍防御，forced-choice建议也不等真实动作；逐帖无恶意标记不认证整体暴露无偏。数据池制备、全部暴露轮次、重跑和防御均计费，轨迹内probe须按run分组并比较可见history基线。选择器或默认方向改变时重验；影响不可控时保留固定可信源、显式来源与人工批准，不由filter未报警批准执行。<!-- source-family:SF-2026-ARXIV-2606-00914 -->

### 10.3 true H2 Review notes本人拟注（两项，不预签）

- `SF-2026-ARXIV-2610-31778` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31778v1)§3–5核心方法、metrics/Q1–Q4与limits首次必要按§9复用，2+1+2=5，实际AGENT-CONTEXT Ch75单段差额。仅文件可恢复/历史独有约束的评价人口边界，不重复既有rulepin/snapshotfork/enforcement；保validsubmission/触发区间、Gemini少compaction、异judge与作弊先于压缩反侧及全标注/重跑成本，不采压缩导致违规/普遍无损或阈值。未核代码/全部附件或复现；PRE/真实SAVE/selfread/solePOST以本日实际记录为准，本注不预签。
- `SF-2026-ARXIV-2610-31710` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31710v1)§3–5与G可得性/工具/预算首次必要按§9复用，2+1+2=5，实际AGENT-CONTEXT Ch75单段差额。仅同代码状态配对damage/rescue分向分母及literal/production异人口，不重复一般replay；保固定Kimi-K3/预算、选PRE成功、后续小子群、输入截断/输出长度与privatecache限制，全部还原/确认/工具费；不采保留率即续做保证、总体损害频率或精确复现，未核代码/运行。PRE/真实SAVE/selfread/solePOST仅本日实际记录，本注不预签。

本人注拟插在现有true H2 `## Review notes` 下原第一条之前，不改变原note次序或内容。整体仅两段/两marker/两本人注；当前尚未SAVE Books，待唯一reader按此逐字稿、完整两侧与当前窄位核PRE。

### 10.4 R23后真实SAVE与作者完整自读（待唯一POST）

唯一reader R23已核两篇必要、各2+1+2=5、实际owner/gap与六件整体逐字PRE，现场确认两肩和true-H2注位无冲突，并依root新授权直接窄授。作者已用apply_patch把§10原两段/两marker/两本人注真实保存到Ch75；现正文在L558–562、本人注在L785–786。已完整自读eval前组、两完整新增、完整feed后肩/后续proxy段和true-H2两注/旧首注，未改两肩、旧注或其他本章内容。

机械检查：两个正文marker各唯一一次，Books两段与本人注均逐字匹配CHINA批准稿；从当前Book仅移除本次批准两段/marker/两注后，SHA256恢复为保存前`660add4a4dcb08cf2e6d406e57fa52862e2c37ee9ac30af53ef9231546455b56`，证明本次修改未改动原有并发2025增补。限定Ch75 `git diff --check`通过。这个校验不代替语义POST；现向唯一reader交实际保存态，不声称其已通过，不改Report/State或其他Books。

### 10.5 R25实际POST后闭合

root已收到并转达唯一reader R25 actual POST通过，本两项各2+1+2=5、真实I生效，指定两段/本人注窄位释放。精确题名与最终locator：`2610.31778v1 — Benchmarks Are Surprisingly Compaction-Friendly`，AGENT-CONTEXT/Ch75正文L558、独立markerL559、本人注L785；`2610.31710v1 — Compact-Bench: Measuring What Context Compaction Costs Long-Horizon Coding Agents`，同章正文L561、markerL562、本人注L786。以上只行政同步既成状态，§10早期未SAVE/待POST保留为过程停点，不再代表当前状态；不重Source/Methods或替root签整日完成，不继续改其他Books/Report/State。

## 11. 代理追加：31840/32109/32349/32411/32214唯一首次必要与评分（不做Books）

root新委派上述五项，B与root均不重复其首次必要。本代理已重新加载当日AGENTS/研究合同适用部分/来源使用及Daily组/Prompt；Report合同、ROADMAP与当前checkpoint复用本日刚完整读取且无变化的上下文。日期/准入仍由SOURCE与唯一reader有效层承载，不重新发现或改变家族分母。以下均精确v1 HTML实际打开并按具名方法/评价/直接反侧有限补读，未执行artifact、未核全部附录/代码、未复现。此批只承担必要与拟评分，未开始owner比较/Books；reader尚需独核，不由本节预签。

### 11.1 [2610.31840v1 — SpecMem: Accelerating Agentic Tool Calling via Live Memory Management](https://arxiv.org/html/2610.31840v1)

拟**2+2+2=6**：新增在线draftstore生命周期/副作用准入边界2，检索草稿到验证/执行的跨边界reach2，可复用隔离/更新/风险分责2。安全变更域已按下述必要深入，不因安全标签抬分。

Necessary: §§3–5/Limitations, A.1–A.2. Verified calls update bounded user-keyed stores; nearest retrieval backs off to a population-seeded shared store and then schema skeletons. Therefore local keying alone is not proof that every fallback path is private. Drafting remains speculative; declared unsafe tools execute only after verification. Idempotency is not harmlessness, and target-token agreement is not external authorization.

Forty synthetic users, twelve sessions, three stream seeds use cached greedy targets; MAT is canonical-call prefix overlap, not deployed acceptance sampling. Live global storage accounts for almost all acceptance gain; user partitioning/eviction slightly reduce it. Complete warmup shrinks the gap to approximately 2%. Tau2 traces are generated once, then replayed under different memories—not independent task-success trials. External-loop p50 decoding speedups are stack-specific, not end-to-end agent throughput.

Side-effect results use 400-call simulated streams and author labels: zero unsafe execution is constructed by deferral, sacrificing correct unsafe speculation. Real BFCL wrong drafts reach similarity 0.9995, refuting confidence-as-safety. Per-call-dependent safety, annotation correctness, shared fallback, access control and post-verification effect authority remain qualifications. Do not claim production privacy, zero tool harm or that model verification establishes user intent.

### 11.2 [2610.32109v1 — Context or Knowledge: How LLMs Attribute Their Own Answers](https://arxiv.org/html/2610.32109v1)

拟**2+1+2=5**：同token不同Q+A缓存的具体因果边界2，模型内部source-report组件1，可复用报告/真实使用分账2；不借外部审计系统扩大reach。

Necessary: §§2–8, D's behavioural-check qualification and E's replication scope. Four 7B–32B models use short, length-matched factual dialogues. After answering, document-cache deletion/replacement leaves templated reports unchanged; transplanting Q+A KV between identical question/answer tokens transfers every eligible report. Same-condition controls do not flip. This manipulates cached computation, not answer text or the retained document.

Directions fitted before any source question generalize across held-out relations; small-model value steering flips 98.9–100% at a fixed strength versus at most 1.1% matched random. Joint K+V projection clamps nearly block transfer, while projection-only transfer nearly reproduces it. These conditional interventions do not identify an exclusive global source variable. Joint K+V edits lack answer-repetition/document-readback checks that accompany value-only experiments.

Eligibility requires the expected intact answer/report; rates are not unrestricted reliability, and item–split pairs are not independent facts. Wikipedia replication has rare document-edit exceptions. During answering, the same values shift selected source more weakly, with prompt dependence, random-control effects and damaged answers. Availability versus actual source use remains unresolved. Adopt state-dependent reporting, not faithful provenance, unrestricted introspection, or content preservation after every edit. Fitting, counterfactual generation and behavioural checks cost; no runtime qualification.

### 11.3 [2610.32349v1 — Why Full-Duplex Speech Models Collapse in Long Conversations](https://arxiv.org/html/2610.32349v1)

拟**2+2+2=6**：区分initial-anchor eviction/近期输出重复及两种受控干预2，持续speech输入/decoder KV/输出控制跨边界2，可复用训练-推理状态与时长验收约束2。

Necessary: §§3–6; B.1–B.2 diagnostic controls; C.1/core C.2; E.2. Forty fixed replays reach sixty minutes; forty adaptive sessions reach twenty. Capacity exhaustion is right-censored, not collapse. Five models are characterized, but diagnosis/fixes cover only sliding-window Moshi/PersonaPlex.

Window sweeps, silence input, fixed-slot retention and matched audio/cache histories support anchor dependence. Large-index shifts/reindexing do not remove entropy collapse. Chunk-reset evidence is verified only for public Moshi finetuning, not unpublished pretraining/PersonaPlex training. Fixed-slot diagnostics use predictive entropy, not directly dialogue quality.

IAP pins the first entry and repositions its unrotated key without reindexing the whole cache. DRP penalizes recent lexical tokens, preserves lexical probability mass and adds prolonged-PAD correction; it does not change audio-stream logits. Replay gibberish drops to zero by the judge, but PersonaPlex still has two-minute silence in 19/40 runs. Early listening preferences favor IAP alone, so lower repetition is not uniformly better conversation.

PersonaPlex bf16/RTX A6000 RTF is 0.7525 versus 0.5957 baseline and 1.0323 StreamingLLM-style; this is added cost, not universal acceleration. Judge misses, finite horizons, selected repetition contexts and model-specific sampling limit generalization. No growing-context cure, indefinite stability, complete causal training explanation or production SLO.

### 11.4 [2610.32411v1 — A Broader Look into MLLM’s Retrieval Heads](https://arxiv.org/html/2610.32411v1)

拟**2+2+2=6**：证据模态配对/功能干预和attention-ranking训练2，跨模态backbone适配至ranking训练/推理消费者2，可复用候选定位/实际依赖/优化目标分责2；不把18checkpoints数量单独计分。

Necessary: §§3–5, equations 1–6, tables 2–4 and figure captions. Detection subtracts question-to-evidence attention under an uninformative question. Spoken/displayed six-digit needles share video, answer, depth and question; eighteen checkpoints concern language-decoder heads, not every encoder/generator component.

Head ablations zero outputs before projection, with size/layer-matched random controls, three seeds and held-out examples; cluster bootstrap/Holm supports qualified reliance, not attention-as-truth. AV-shared subsets harm broader tasks, but corrected significance holds on 4/8 tasks per tested model, not all tasks. Preservation correlations do not establish a complete adaptation mechanism.

Ranking fixes selected base heads, normalizes scores with detached endpoints and a degenerate-range guard, and updates attention-projection LoRA with relevant-page/hard-negative loss. Inference uses uninformative-question subtraction. Matched Qwen3-VL page Micro R@1 improves 56.45→62.48; layout 47.14→48.60 without layout labels. Other families improve under their own candidate windows, so cross-family ranking is not controlled. Published retriever settings also differ. Attention collection, calibration, candidate windows, training and inference all cost; no end-to-end retrieval speed or answer-correctness guarantee. Hardware/precision/timing for a performance claim are Not Disclosed here, and no such claim is adopted. No source-code or pixel-level plot verification.

### 11.5 [2610.32214v1 — DIAL-S2ST: Learning Latency Control for Simultaneous Speech-to-Speech Translation](https://arxiv.org/html/2610.32214v1)

拟**2+2+2=6**：lookahead on-policy蒸馏/大text-KL遮罩/scale条件接口2，训练privileged teacher至因果student与部署时序控制跨边界2，可复用imitationgap/质量-延迟分责2；不把成熟LoRA或单语种榜分作为新增机制。

Necessary: §§2–4/Limitations, equations 1–5 and tables 1–2. Student-generated text/speech prefixes condition both models; frozen teacher sees future source only for text supervision. Speech KL uses the same available source/text, anchoring semantic/acoustic outputs. Text KL above ten nats is masked, not evidence that unseen future content becomes inferable.

Training samples lookahead and pairs adapter scale α=k/kmax, with two-second maximum; inference changes α without future source. α=0 recovers the frozen base, while timing is empirically characterized, not a per-utterance latency guarantee. Ten source-only FLEURS hours, 500 steps, rank-16 Temporal Transformer LoRA use three trained seeds combined by model soup—not three independent reported confidence intervals.

CVSS French→English/Hibiki matched-LAAL comparisons favor on-policy distillation, especially low latency. Removing masking lowers ASR-BLEU; removing speech KL degrades voice/content, and reversing KL collapses to silence. Logit biasing can emit before listening. ASR-BLEU, forced-alignment LAAL/End Offset, speaker similarity and UTMOS are proxies, not human adequacy or serving wall latency. Long-form translation, other languages/models and human quality remain untested. Teacher passes, student rollouts, training and output generation cost remain; hardware/throughput/SLO are not established. No code execution or exact Pareto-curve pixel reading.

### 11.6 本批停点

五项首次必要与拟评分均已完成，保留直接反侧后停止，没有全附件/宽列表队列。普通待办为唯一reader独核必要/评分，以及root后续的正式采用、actualowner/具体NC或最小整合；本代理未给此五项写Books。SpecMem的shared fallback与binary annotation适用性、full-duplex的残余静默/训练premise权限、cache attribution的joint-KV未核内容读回、retrieval-head的有限显著性/窗口差和DIAL句级/单语人口均不得在报告中省略或升级为安全/性能保证。

## 12. 32349/32411/32214 actualowner与Ch23整体PRE（未SAVE）

root新授本三项的Ch23精确窄位及本人注由本代理独占；root SAGE实际POST后已释放且不再写本章。其他日期原有并发内容保留，不锁整章。已重读AGENTS/ROADMAP/PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE/最新Live checkpoint，并实际对读Ch23相关语音、Shared self-attention、Full-duplex、Streaming Identity完整局部推理与Ch22/24开篇/末尾交接。§11首次必要直接复用，不第三Methods；本批不动31840/32109、Report/State或其他Books。

### 12.1 真实owner、具体NC与最小差额

三项窄命题均拟归`MULTIMODAL-REPRESENTATION`，Ch23 `books/part-03-multimodal-world-models/23-multimodal-representation.md`。这不是因题名包含speech而归本章：三项采用对象分别是跨模态证据读取功能、持续双流状态兼容，以及可见prefix到text/speech时序消费者的条件接口。Ch22通用sliding/prefix/cache与长窗联合约束不重讲，Ch24采样/commit范式不重讲，Ch28/29一般优化/蒸馏不重讲；线上cache物理管理/索引执行仍归对应owner。

- **32411**：Ch23 Shared self-attention首段（原L1267–1269）已有允许图/元数据；原L1293–1295的encoder-free受控融合深度、原L1333–1340的ICL示例grounding→query读出分责已承载“attention允许/可读不等实际使用”，此一般原则NC。尚无**同证据spoken/shown配对校准检索头、layer/size匹配删头的功能依赖、固定头集到attention-ranking训练消费者**这条具体链。只在Shared self-attention首段后新增一段，不授attention为事实truth或所有下游任务都显著。ranking在此仅作为功能表示的消费实例，不接管Ch76的完整检索/索引/packing机制；若该消费者后续需独立展开，由root另协调，不在本段重复。
- **32349**：原Full-duplex路由节（L1374–1396）已有并发到达/显式safe point/打断与commit权；原Streaming Identity（L2359起）已有时钟/prefix/观察版本与触发，L2401–2405已有long/short memory压缩/trigger故障。上述均NC，但不承载**持续每帧生成填窗后，初始化anchor兼容与近期lexical自强化是两个可分状态/输出故障，须用不同干预及长时评价验收**。新增一段放在Full-duplex通道路由完整论证后、token budget竞争段前；不把IAP写成新的通用KV算法owner、不提供全runtime实现/无限稳定保证。
- **32214**：原L2369–2371 Hibiki-Zero段已有sentence-level提前发声支持/RL不能自动跨监督支持，后续Silent Thought/WAIT/三层监督mask已有teacher标签与arrived prefix分责，以上NC。尚无**源语音only、同student prefix上的lookahead text teacher/无lookahead speech anchor、大textKL遮罩与lookahead–adapter scale配对，部署只调scale的时序接口**。在Hibiki-Zero完整反侧段后新增一段，保留它作为另一条有条件分支，不覆盖既有RL/显式WAIT或claim任意模型无需目标监督就能学习翻译。

三项沿用§11拟**2+2+2=6**，需要reader必要独核及本次actualowner/最小差额PRE；不因章节数、模型数、安全或需要Books抬分。下列三段各独立marker、本人注各一，共三个窄位；未SAVE Books。

### 12.2 窄位A：32411，一自然段

**完整前肩，保持不改：**

所有 tokens 进入同一 self-attention graph。计算接口最统一，但必须明确 attention mask、position system、modality type、packing boundary 和 loss mask。没有这些元数据，同一个 sequence 中的相邻 token 可能只是打包邻居，而非语义邻居。

**拟完整段：**

共享图还要区分“允许读取”与“哪些头实际承担读取”：把同一证据分别说出或显示，在内容、问题和位置配对后，比较问题到证据的attention，并减去无信息问题下的同输入读数，才能提出较少受位置偏好影响的功能头候选；再以层位和数量匹配的随机头、未参与选择的样本做删头干预，检验实际依赖，而不是让热图自证grounding。[受限跨模态对照](https://arxiv.org/html/2610.32411v1)还把固定头集的问→页面分数作为排序监督，更新attention投影的LoRA，让同一表示路径成为可训练的消费者接口。其共享头对更广任务的作用并非全部显著，页面/区域召回改善也不保证答案正确；不同模型的候选窗口不同，不能直接排跨模型优胜。配对检测、attention读出、校准、训练和完整消费均计费；证据定位或原任务回归失配时，保留原联合forward、专用encoder/projector或独立检索与原输入回读，不把稀疏头集当作跨模态事实或充分证据的唯一owner。
<!-- source-family:SF-2026-ARXIV-2610-32411 -->

**完整后肩，保持不改：**

同一sequence兼作多模态生成接口时，还须标出每个token是clean condition还是noisy target，而不只标模态：保native latent各自维度，以投影接入共享宽度，再将role、modality与noise time逐token交给AdaLN。Position也可按query角色解释：condition只读自身segment的局部结构，target对不同condition使用共同参考，避免相同局部索引制造虚假对应。[Modaliff的受限消融](https://arxiv.org/html/2610.25533v1#S4.SS3)支持这一接口，不证明语义已共享或任意模态/顺序都无损；冻结codec也不免它的制备与文本重建训练。投影/属性、codec、共享denoiser与全部生成回归均计费，role、位置或细节支持不合时保固定任务布局、专用codec/生成器与独立条件验收，不由单一backbone签发统一真值或普遍低成本。
<!-- source-family:SF-2026-ARXIV-2610-25533 -->

### 12.3 窄位B：32349，一自然段

**完整前肩及绑定，保持不改：**

这里 encoder 拥有声学表示，fusion layer 拥有跨 channel interaction，interruption policy 拥有控制决策，已发送
token 则属于不可撤回的外部 effect；任一层都不能把自己的 confidence 冒充用户意图。更早 commit 可降低打断延迟，
代价是 coherence、rollback 与训练/推理对齐更难；更晚 commit 保留轮次语义，却可能错过实时控制窗口。低并发、
turn-based UI 或缺乏 interruption 标注时，原来的 utterance-level late fusion 仍是更稳健的基线。公开实验只约束其
模型、对话数据与延迟设置，不提供跨设备和生产噪声的通用结论。[受限证据：arXiv:2605.10199v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-10199:end -->

**拟完整段：**

持续听说还会暴露短轮打断测试看不到的状态压力：即使暂不发声，每帧推进的token也能填满窗口，而丢掉初始化状态与近期输出自强化未必是同一故障。一条[受限全双工分支](https://arxiv.org/html/2610.32349v1)保留首个KV项并随滑窗只调整该项的位置，另对近期lexical token作重复惩罚、保持词汇总概率并对长静默作条件修正，分别处理缓存兼容与输出反馈。它不是保留任意早期语义证据，也不代表修复了所有长对话：诊断只覆盖两个滑窗模型，训练前提未完整公开，部分固定槽实验只测entropy，组合修复仍有长静默且会损自然词复用。验收应分开重复、静默、乱码与回应质量；容量耗尽是观察终止，未观察到故障不等无限稳定。额外位置更新、logit控制和长时回归均计费，较稳定还会慢于原基线；状态/输出质量或实时预算不合时，保留较短会话、显式重启或半双工等待与原声回读，runtime仍拥有播放、打断和交付，而不由一项cache保留签发持续服务保证。
<!-- source-family:SF-2026-ARXIV-2610-32349 -->

**完整后肩，保持不改：**

fusion 之后仍要决定不同 modality 如何竞争有限 token budget。均匀或对称 compression 最容易实现，但默认各模态拥有相同 information role；当视觉承担事件定位、音频承担补充语义时，可以让视觉 anchors 条件化音频 selection。反过来，在 ASR、音乐或遮挡场景中，audio-first 或 full-token branch 仍可能更可靠。**方向性 compression 是受任务 truth authority 约束的 policy，不是“视觉永远更重要”的架构事实。**它还需要对 modality conflict、selector drift、chunk boundary 与 abstention 做显式验证。

### 12.4 窄位C：32214，一自然段

**完整前肩，保持不改：**

这条分支先建立提前输出的 exploration support，再调整等待策略；[Hibiki-Zero 的有限反侧](https://arxiv.org/html/2602.11072v1#S4.SS7)中，只学整句结束后发声的 base 经 RL 仍未学会提前开始，去掉句内随机 silence 也使质量与 lag 退步。它不证明任意 RL 都能突破监督支持，低 lag 还可能牺牲长语音内容与音色保持。数据合成、codec 缓冲、reward 与重复生成都有成本，语义 lag 指标不是设备 wall-clock SLO；时序或质量不可验时，保留逐词对齐、完整句等待与保守 turn-taking。无论训练 reference 多完整，下一层读取日程仍只能消费实际到达的 prefix，输出 commit/cancel 继续由 runtime 决定。

**拟完整段：**

已有翻译底座还可用源语音上的自蒸馏学习另一条时序接口：学生在因果输入上生成自己的text/speech前缀，冻结教师在同一前缀上只为文字预测多看一段未来源语音，语音预测则仍用相同已到达输入作anchor，避免调早文字同时任意改变声学条件。未来信息带来的模仿差额不能靠强行追齐消失，因此只屏蔽过大的text KL；训练再把lookahead长短与同一adapter的scale配对，部署只调scale而不读取未来。[DIAL-S2ST的有限对照](https://arxiv.org/html/2610.32214v1)支持已有法英Hibiki句级能力的这种适配，不是从源语音无监督学会任意翻译，也不提供逐句延迟保证；去掉语音anchor会伤内容/音色，反向KL甚至静默塌缩。教师前向、学生rollout、适配训练和完整语音输出都计费，ASR/强制对齐的质量与lag代理不等人评或设备时延。新语言、长语音、质量或预算失配时，保留原底座、显式等待或已验对齐/RL分支，重新验收时序与内容，不让更早发声取得正确性或交付权。
<!-- source-family:SF-2026-ARXIV-2610-32214 -->

**完整后肩，保持不改：**

同一语音底座也可以先用显式转写建立听取与发声的训练桥梁，再在后续训练隐藏这条中间文字。[受限双通道语音分支](https://arxiv.org/html/2509.02521v1)把文字、听入音频和说出音频放进对齐slot：TTS训练让文字领先待生成音频，ASR训练则让文字跟随已给定音频；先学习转写、回答和语音串联的半双工轨迹，再加入隐藏转写与合成打断。这里改变的是监督支持和通道条件，不是让部署提前听到未来音频，也不证明隐藏文字等于真实思考；文字领先量、空位/等待规则、codec帧率、训练标签与部署实际前缀须分别保留。不同底座/数据量和多阶段配方不能唯一认证这种组织更省数据，人评帮助性与部分识别/音色切片仍可退步，合成反应时也不替代设备播放停止或端到端deadline。转写/TTS和合成轨迹、全部训练、编码/KV/多码生成及独立质量时序回归都付费；通道对齐、打断或质量不可验时，保留显式转写、级联ASR/文字/TTS、完整句等待和保守turn-taking，实际输出的commit/cancel仍交runtime。

### 12.5 true H2 Review notes本人拟注（三项）

均拟放在当前唯一 `## Review notes` 原第一条之前，保旧note顺序；只绑定各自独立marker，不混家族，不预签。

- `SF-2026-ARXIV-2610-32411` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32411v1)§3–5/Eq1–6/T2–4与图注首次必要见本日CHINA§11，2+2+2=6，actual Ch23单段差额。仅同证据模态配对/校准候选头→matched删头→固定头排序训练消费者；保language-decoder范围、4/8显著/非全部、candidate窗与跨retriever设置不匹配、全校准/训练/消费费，不采attention即truth、充分证据/答案正确或服务加速；不接管Ch76完整索引。未核图像素/代码或复现；PRE/真实SAVE/selfread/solePOST仅以本日实际记录为准，不预签。
- `SF-2026-ARXIV-2610-32349` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32349v1)§3–6/B1–2/C1及C2核心/E2首次必要见本日CHINA§11，2+2+2=6，actual Ch23单段差额。仅持续双流anchor兼容/lexical反馈分离与有限干预，保两滑窗诊断、FT非完整预训证/entropy代理、19/40残余静默、early偏好/漏检、finite/rightcensor与额外RTF成本；不采growingcontext修复/无限稳定/通用KV或设备SLO。未核代码/音频与复现；PRE/真实SAVE/selfread/solePOST仅实际后到，不预签。
- `SF-2026-ARXIV-2610-32214` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32214v1)§2–4/Limits/Eq1–5/T1–2首次必要见本日CHINA§11，2+2+2=6，actual Ch23单段差额。仅causal student前缀/teacher text lookahead与speech anchor、textKL遮罩和scale时序消费接口；保FrEn/Hibiki句级、三seed soup非CI、reverseKL静默/音色反侧、ASR/forcedalignment代理与全teacher/rollout训练费，不采从零无监督翻译、任意语言/长语音或逐句延迟保证。未核图曲线像素/代码或复现；PRE/SAVE/selfread/solePOST仅实际后到，不预签。

当前三完整段/三marker/三本人注与完整两肩仅在本文件，待唯一reader必要、评分与整体逐字PRE；之后依root授予直接窄SAVE/自读/solePOST，不等第三研究或再行政批准。若实际owner/完整已有覆盖被反证，按具名差额改NC，不强造三摘要。

### 12.6 R36后真实SAVE/完整自读，待唯一POST

唯一reader R36已核三项exact-v1必要/反侧、各2+2+2=6、actualowner三具体差额和原9件整体逐字PRE，现场六完整肩/newmarker0通过，并依root既授直接窄准保存。作者已仅用apply_patch真实保存原三段/三marker/三本人注：32411正文Ch23 L1271/marker1272/注2653；32349正文L1403/marker1404/注2654；32214正文L2379/marker2380/注2655。已完整自读三新增及其所有直接完整肩、true-H2三注与旧首注，未改旧内容。

逐字检查三段与三注均匹配批准稿，各正文marker唯一；只剥本次原三段/marker/三注后，SHA256恢复保存前`be90dff41680c9971d1dab0e08a2ccf7a43b6472ba35ca76cc3f21115b5e3439`。限定Ch23 diffcheck通过，保护SAGE/2025等已有并发修改。该机械校验不代语义POST；现交唯一reader实际保存态，不预签其通过，不改其他Books/Report/State。root新授31840实际Ch48可在待POST时独立推进，32109仍不动。

### 12.7 R37实际POST后闭合

唯一reader R37已实际完整读三新增/六完整肩/三注与旧首注，逐字同R36且限定diffcheck通过；32411/32349/32214正式各6、三项真实I生效，指定三窄位释放。本代理仅同步既成状态，不重必要/POST；本批不再改Ch23或其他Book。完整题名分别为`A Broader Look into MLLM’s Retrieval Heads`、`Why Full-Duplex Speech Models Collapse in Long Conversations`、`DIAL-S2ST: Learning Latency Control for Simultaneous Speech-to-Speech Translation`；最终locator见§12.6（32411 L1271，32349 L1403，32214 L2379）。早期未SAVE/待POST保留为过程记录，不代表当前状态；不据本三I预签整日完成。

## 13. 31840 SpecMem实际Ch48 owner/最小PRE（未SAVE）

root新授仅此项Ch48正文精确位/本人注，32109仍只保必要，不动Ch66/76。已按当前AGENTS Books上下文实际读Ch48 drafter在线更新、semantic retrieval、历史logit/LRU、Agent workflow/ToolSpec/read-only speculation/commit链与章末交接，并对读Ch47/49开头和末尾交接；复用§11.1首次必要，不第三Methods。唯一reader尚未独核该必要/6分，以下只拟稿，不SAVE。

### 13.1 具体NC与唯一差额

唯一owner为`INFER-SPECULATIVE-DECODING`，Ch48 `books/part-05-inference-system/48-speculative-decoding.md`，不是Ch50产品功能归纳。原L519起在线drafter循环已有target信号/版本gate/资源费，但更新的是参数/hidden-state训练；L578–595已有tenant/revision-scoped semantic draftstore与index/eviction/隐私，L668起已有已验logit/ngram的LRU候选维护；L824–826已有schema FSM/历史调用retrieval，L828–846已有read-only speculation/actionmatch/外部effect及串行写调用。上述候选权、隔离、cache boundedness和副作用晚提交一般原则均NC，不重写为SpecMem发明。

真实剩余差额是**已确认完整target call的写回事件不同于draft部分接受、参数训练或外部工具执行成功；跨session新call到达时，冻结/在线draftstore、peruser隔离与eviction各有不同作用，且shared fallback不能继承私有store保证**。拟在ToolSpec维护/局部证据完整段之后、read-only speculation标题之前新增一段，将旧schema来源分支接到生命周期，再自然交给外部effect frontier；不改下一节已有效的工具执行合同。沿用拟2+2+2=6，安全变化域只采用有明确条件的分责，不采zero harm/完整隐私或生产加速。

### 13.2 原一自然段/独立marker与完整两肩

**完整前肩，保持不改：**

状态解析、schema revision 和历史检索增加维护、隐私与检索成本，开放值与结构边界判断错误还可能压低接受率；格式不稳定、复用弱或大 batch 下应回退统一 drafter/普通 target 生成。作者 Qwen/Llama、API-Bank/ToolAlpaca/BFCLv2/ToolBench 的 batch-1 实验支持这个条件分支，不证明高并发 SLO 或任意精度下分布完全相同；训练型 drafter 的准备成本也不能从单请求加速中消失。下一层的 read-only tool speculation 则真正提前发起外部调用，它另有 effect frontier，不能与本节的 token 草稿混为一件事。

**拟完整段：**

历史调用还可以不经参数训练而在线更新：target确认完整call后，将它连同当前query键写回有界draftstore，不因本次草稿只接受了短prefix就放弃更新；生成被确认不等工具已成功，store只拥有下一次proposal。[SpecMem的受限对照](https://arxiv.org/html/2610.31840v1)中，跨session新调用持续到达时，在线写回解释了主要接受量收益，按用户分区与淘汰分别提供隔离和容量界，而非额外准确率；warmup已覆盖全部任务时，冻结store仍可合理。私有store之外若回退population-seeded共享候选，必须另核其来源和访问资格，不能把按用户keying写成所有fallback都保密。外部执行仍服从下一节的effect frontier，检索相似度或幂等性都不批准错误对象上的动作。Embedding、写回/淘汰、canonicalization与验证均计费，canonical-call前缀接受代理也不是部署采样接受率或完整Agent吞吐；证据只覆盖模拟重复/到达流及一次生成后重放的轨迹。来源、更新资格或净收益不合时，保留隔离的schema草稿、冻结store或target-only，不由历史相似和较长接受量替代实际验证、权限及完整费用验收。
<!-- source-family:SF-2026-ARXIV-2610-31840 -->

**完整后肩/标题组，保持不改：**

### 从 Token Draft 到 Read-only Tool Speculation

Token-level speculative decoding 只提前产生候选 token，外部工具仍在完整 action 生成后启动。对长 reasoning
与慢 read tool 的 Agent turn，可以增加一层 action speculation：main stream 产生首 token 后复用同一 prefix
KV fork 当前模型，以 forced tool-call prefix 探测下一 action；只有 probe confidence 达到门限才并发执行被
manifest 标为 read-only 的工具。Main stream 完成后，最终 tool name 与 canonical arguments 完全匹配，
precomputed observation 才能进入会话；不匹配则丢弃结果并走 serial fallback。被拒 probe 的已验证 token
prefix 可以继续作为普通 speculative draft，但仍由 target verification 决定提交。

### 13.3 true H2 Review notes本人拟注

拟放在当前唯一 `## Review notes` 原首条之前，保留全部旧note与并发内容。

- `SF-2026-ARXIV-2610-31840` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31840v1)§3–5/Limitations/A1–2首次必要见本日CHINA§11.1，2+2+2=6，actual Ch48单段差额。仅verified完整call→在线bounded draftstore写回与liveness/scoping/eviction分责；原tokenproposal/lateeffect一般原则已有覆盖。保shared fallback/正确annotation与per-call资格、模拟用户/once-trace replay、MAT/canonical/greedy代理、warmup全覆盖差额收窄及全维护/验证费，不采按用户key即全隐私、幂等即无害、targetcall即真人授权或zero harm/生产SLO；未核实现/真实多session日志或复现。PRE/SAVE/selfread/solePOST仅本日实际记录，不预签。

当前仅拟一段/一marker/一本人注；待reader先必要/拟评分，再actualowner与整体逐字PRE，未通过前不SAVE。本项闭合后停在授权分工，不自行接32109。

### 13.4 R39后真实SAVE/完整自读，待唯一POST

唯一reader R39已核exact-v1必要/直接反侧与6分、actual Ch48具体NC/唯一差额和§13原三件整体逐字PRE，现场完整前肩/read-only后组、新marker0通过；依root既授，作者仅apply_patch真实保存原一段/独立marker/本人注。正文Ch48 L828/marker829，本人注L1152。已完整自读实际新增、两完整肩与true-H2本人注/旧首注；原稿逐字匹配，正文marker唯一。只剥本次原段/marker/本人注后，SHA256恢复保存前`e591bbecc83c65028fe9e428ee10e5f7a57fb7f6b0f0554568a6ce71ef4b64b1`，限定Ch48 diffcheck通过。保护旧DVI等并发内容，该机械校验不代语义POST；现交唯一reader实际保存态，不预签其通过，不动32109或其他Books/Report/State。

### 13.5 R41实际POST后闭合

唯一reader R41已实际完整读新增/完整两肩/本人注与旧首注，逐字一致且限定diffcheck通过；31840正式6分、`INFER-SPECULATIVE-DECODING`真实I生效、精确位释放。题名`SpecMem: Accelerating Agentic Tool Calling via Live Memory Management`，最终Ch48 L828/marker829/注1152。本代理仅行政同步既成状态，不重必要/POST；后续仅推进root另授31695/31974，不接32109，不据本I预签整日完成。

## 14. 代理追加：31695/31974首次必要与安全直接反侧

仅root新授两已准入家族，不新发现；重读当前AGENTS/研究合同、Books上下文/ROADMAP和最新Live checkpoint。精确HTML优先，针对拟用安全域读原机制/关键评价/直接反侧与官方对应实现，不执行第三方代码/攻击/测试、不遍附件。以下评分是必要后拟分，须唯一reader独核；日期身份沿本日SOURCE合法联合日层，不凭代码或网页更新时间补造Oct26首次发明。

### 14.1 2610.31695v1 — Fooling LLM Safety Guards into Judging the Wrong Text

已实际读[exact-v1](https://arxiv.org/html/2610.31695v1)§2–6/8、Eq1、T1–5及Appendix C解析/D相关实现与训练边界。拟2+1+2=5：重要guard任务/监督目标边界，reach仅单组件，稳定分责2；因安全变化读足受影响实现，不因安全名称抬分。内容中完整伪任务可改变判分对象，但不证明真实role/parser越权、唯一因果或下游harm。防御T用冻结base对whole content和已知segments分数的max作训练target，保组合被base识别的harm，不是部署必跑segmenter；B只保护不可由content产出的token边界。B单独无效，T的append-heldout低绕过不认证clean noninferiority；adaptive位置/结构搜索再击穿（T49/50），多guard机制并不一致。

原实现已定点读且pin相同内容：[979370c](https://github.com/ukanwat/guardrebind/tree/979370cda284dda68763610fa43c036751e36560/src/fix) `inputs.py`的render/content/ids/bounded/split全链，`distill.py`L65–113、335–370、412–426与`test_distill.py`全结构检查：trusted模板前后不改、content关闭special parsing，36/37由宿主插；训练确实含whole+原项+decoy、max teacher与yes/no BCE，boundary只另训两行delta。只读测试断言，不冒运行通过。非special added tokens仍需tokenizer具体核；本轮未实际加载权重/tokenizer。B不删内容、分段边界训练已知也不等任意隐藏组合保护；训练/teacher标注、全部攻防/误拒回归计费，保独立output/effect gate。

直接反侧保留：攻击后仅已flag人口/阈值分母不同；最佳family是选后结果；LG3有纯recency成分，ShieldGemma有generic evasion；fixed-decoy hardnegative含structured-test重叠，heldout-decoy方案部分后设；clean-copy丢掉trailing harm，naiveAT不能按matched recall比。当前作者[较早博客](https://utkarshkanwat.com/writing/safety-guards-wrong-document)实见September5,2026，完整读核心及末段：同攻击与boundary/whole-content训练方向早已公开，且明确当时未端到端实现；本次只可记论文扩展测量/训练防御及其新反证，不重计攻击首次。仓库当前HEAD commit时间Oct17也不是Oct26首次证。已通知root该日归属限定，不改SOURCE旧日期或跨日展开。

### 14.2 2610.31974v1 — Agentic AI Defense: Decode-Time Provenance Binding for MCP

已实际读[exact-v1](https://arxiv.org/html/2610.31974v1)§III/V–IX、Alg1–2/假设与证明、VI各关键评价/ablation/substitution/utility/overhead/cross-context反侧。拟2+2+2=6：decode-source到跨agent/context及sink的机制边界；不因安全名或零观察提高分。核心有限命题是签名只能抗label改写，不能阻止agent拿另一份真Trusted标签顶替真正影响；参数closure之外还需宿主持有已进入context的decode-origin状态，在effect前独立检查。它以完整mediated lineage、D/C注册、key隔离和受控promotion为前提，不保护summary真值或未观察旁路。

已实际只读[官方notebook固定ed7739b](https://github.com/ericyoc/stego_provenance_defense/blob/ed7739bdc79b62f4e9b6db82749266a7d3bb3d1f/stego_provenance_defense_poc.ipynb)cells9–10/18/24/41–47相关实现（未执行）：10基础binding验证；18真实FastMCP decoder与critical端点；24 client固定decide；41声明扩展权威评价为deterministic/no-model-network并覆盖早期live pass；42 `MCPLayer` mint/run_tool/enforce/promotion/handoff全体；43权威24项直接构造payload/工具名，不经模型决定；44逐组件/remote反侧；45手动promotion合法3例；46 router直接读取`hidden_text`；47显式handle handoff与旁路。论文的24/24→0/24是受控谓词台架，不是已证生产emailagent harm下降；普通taint baseline同为0。artifact当前HEAD时间Oct24/notebook元信息Oct20只作版本边界，未据此决定论文公开日。

三条关键实现反侧不得丢：`run_tool`/`enforce_critical`用`if h in self.store`过滤未知handle而非算法要求的missing-dependency拒绝；`handoff(src_ctx,...)`不读src_ctx已有taint，只沿所传handle，cleanhandle不能自动代表全部受污染context输出；`promote`仅内部方法接受promoter字符串，无内置principal授权检查，合法测试直接调用，攻击测试另用未promotion新layer。故不采用“任意影响已自动捕获”“audited promotion已完整鉴权”“drop-in端到端零泄漏/100%utility”。proof与实现资格分开，须补可靠入口/缺失拒绝、所有mediated输出继承与独立promotion授权，不能由HMAC自行补齐。登记/ledger/closure/跨hostkey管理、误拒与人工恢复均计费，未覆盖时隔离/禁敏感sink或人工；LSB/DCT需匹配decoder，不采默认图像总结必然运行。此处不重做所有攻击carrier/图像素，不运行model或网络experiment。

## 15. 31695/31974实际Ch72 owner与最小整体PRE（未SAVE）

唯一owner `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md`；已实际读该章开篇/章末Ch73交接、结构注入与完整相关tool-boundary/多模态语义/PolicyCompiler链、influence/IFC/ChainCaps/权限图/认证层级与taint恢复论证，并读Ch71/73开篇末尾交接。沿§14首次必要不第三Methods；只拟以下两完整段/两marker/两本人注，未通过reader前不SAVE。

### 15.1 具体NC与剩余差额

31695：原Ch72 L1707结构注入已区分统计模板与真实role/parser、L1767起已管重建语义/窗口/计算能力、L1888起pre-guard sensor与effect authority均具体NC；尚未承载whole/原项/decoy max作为训练target与content不可造token边界的不同职责，以及clean-copy遗漏后段harm、B单独无效与adaptive位置反证这条同一论证，故仅补一段接在结构注入后，不重复攻击payload或旧首次发明。

31974：原L1712–1714 PolicyCompiler已有可信事件/依赖/完整中介，L1078–1082已有显式/隐式sink影响诊断，L1822–1826 ChainCaps已有value-sink衰减、保守context budget与外部降密，L2711认证来源、L3146恢复分支均NC；不能因泛称taint或ledger就造新owner。实际余差是**另一份真实签名的label不能替未记录的decode影响、host捕获完整性与MAC正确性分责**，以该实现未知handle/handoff/promotion的反侧限定部署资格；不是宣称新发明context taint或已经实现完整授权。拟仅在现ChainCaps具体context段之后、revocation memory之前增加一段，保旧论点/旧撤权链不动。不把有缺口实现当充分防御；若reader认为此已被原具体论点完整承载，可有效NC而非为diff强写。

### 15.2 31695原单段/独立marker及完整两肩

**完整前肩，保持不改：**

不可信内容还可能模仿对话的结构，而不只是要求忽略先前指令：工具返回文本中伪造 tool 结束、assistant 回答和下一轮 user 消息，使模型把数据当成一段待续写的历史。这里要区分模型对 chat template 的统计先验与真实 runtime 的 role/parser 权限；前者受到扰动不证明后者已经被攻破。[有限结构注入对照](https://arxiv.org/html/2602.16958v1)中，强制模板 tokenization 与移除括号的结果差异支持这种形式敏感性，但成功样本的 attention 分析不确定唯一成因。攻击搜索的 proxy 又只以有效轮次中的成功比例计分，不能当作所有请求的攻击率。因而应把模板序列化、外部文本转义及 tool-return 回灌作为独立回归面，保留真实 role 与来源身份，并在每次 effect 前重新执行授权；这些是工程防误用条件，不是论文验证的充分防御。模板回归、搜索查询及良性恢复测试都有成本，低风险 typed data 路径仍合理，不能由有限实验宣布所有过滤或权限边界失效。<!-- source-family:SF-2026-ARXIV-2602-16958 -->

**拟完整段：**

同样的伪结构若进入guard，还会改变它在判断哪份内容，而非真的改变runtime角色：只恢复原请求的高分，可能让模型学会忽略后来追加的危险文本。一个受限训练分支因此保留whole content、原项与decoy，用冻结base对这些对象的最高风险分数监督整份内容；组合风险只有base已识别时才被保住，训练已知分段也不意味着部署拥有通用segmenter。[GuardRebind的有限对照](https://arxiv.org/html/2610.31695v1)把content单独tokenize、关闭special parsing并由可信侧插入不可从文本产生的边界ID，但未训练的边界本身无效；训练后的append-heldout改善也会被自适应位置/结构搜索击穿，clean效用非劣尚未确立。因而边界/监督目标、阈值分母、合法结构误拒和知情攻击要联合验收，不能把特殊token或一次低绕过率当隔离证明。Teacher标注、训练与全部安全/效用回归均付费；tokenizer、任务或攻击支持失配时，保留原已验guard、隔离/人工与独立output/effect gate，而非让模型通过判分选择取得权限。
<!-- source-family:SF-2026-ARXIV-2610-31695 -->

**完整后肩，保持不改：**

程序执行失败后，把错误反馈给模型以修复程序是合理的恢复方式，但 runtime 产生的 exception 仍可能包含工具或外部系统控制的不可信内容，不能因此升级为指令。[代码执行代理的受控反例](https://arxiv.org/html/2602.15945v1)显示，返回合法 schema 后附带的异常，经原样回灌使模型重新生成程序，并调用沙箱内已经可用的管理或写入能力；这里没有 sandbox escape，隔离成功也不代表权限使用符合任务。每次再生成都应视为新的 program proposal，重新检查对象、参数、effect 与预算，并保留错误的类型和来源；这是工程控制要求，不是作者已证明的充分防御。更严格的反馈过滤和重新授权会增加恢复成本，低风险 typed error 与单步端点仍可保留；四类有限攻击不能证明任意传统工具代理免责，也不能证明所提 semantic gate 能防住自适应攻击。<!-- source-family:SF-2026-ARXIV-2602-15945 -->

### 15.3 31974原单段/独立marker及完整两肩

**完整前肩，保持不改：**

具体执行时，可以把每份 value 的 authority 表示成允许到达的 sink 集合，sink 同时绑定 operation 与 scope；工具组合输出只继承各输入预算与该工具 pass-through 规则的交集，effect 请求必须仍属于这份交集。模型生成参数还可能依赖上下文中未显式引用的值，因此 ChainCaps 另维护保守 context budget，把已进入 Context 的限制一并收紧，而不是让摘要或中间 Agent 洗回权限。这用更多 false block 与 manifest 制备/回归成本换取 proxy 可见显式流的组合约束；manifest 错误、未中介的 shell 或隐藏状态仍在保证之外，context/session 边界重置也不能代替真实信息隔离。必要放行须由外部可信授权显式降密，不能由模型自行扩大预算；普通单工具、无敏感数据路径仍可保留较简单的逐调用权限检查。<!-- source-family:SF-2026-ARXIV-2605-26542-supp -->

**拟完整段：**

给来源标签签名也不能证明影响记录完整：Agent可以呈交另一份真实的Trusted binding，同时省略使它选择敏感动作的decode结果。签名抗改写，宿主持有的参数依赖与context限制才负责抗这种替换；decode返回因此须在进入context时登记，而非等Agent自报用过哪个值。[MCP provenance的受限协议与演示](https://arxiv.org/html/2610.31974v1)暴露了这份分工，但不证明drop-in实现已满足完整中介：其固定notebook扩展把未知handle过滤掉而非拒绝，handoff只跟显式handle、不自动继承源context全部taint，promotion也依赖外部调用者授权。部署应把缺失依赖拒绝、所有跨context输出继承及逐值可信降密作为独立验收项，不能用HMAC补齐；受控24项谓词检查不是模型实际泄漏率，零观察和三个手工合法例也不签全效用。登记表、ledger/closure、密钥、误拒与人工恢复都计费；decoder注册、传播或promotion资格不完整时隔离context、禁敏感sink或转人工，普通只读低风险路径仍可保留，不让新标签替代原权限边界。
<!-- source-family:SF-2026-ARXIV-2610-31974 -->

**完整后肩，保持不改：**

持久化标签还要防止旧checkpoint把已撤销的信任关系复活。[一种尚未实现的设计](https://arxiv.org/html/2610.28093v1#A1)给派生memory保存所有祖先来源的revocation counters，而把当前counters留在快照之外；reload与动作授权时重新比较，过期描述符不能直接恢复旧权限。这个分工依赖完整来源追踪、不可绕过的读取/调用hook和可信的单调counter store；它不撤回已发生的外部效果。参数级来源检查也不等于控制模型为何选择某个工具，schema把敏感参数错标为safe仍会留下缺口。因此它只提供可检验的设计边界，不能由标签规则或比较表签发攻击阻断、保密性或低开销保证；绑定/检查不完整时，保留隔离与当前exact-call人工审批。<!-- source-family:SF-2026-ARXIV-2610-28093 -->

### 15.4 true H2 Review notes本人拟注（两项）

拟在当前唯一 `## Review notes` 原首注之前，保留全部旧注顺序/内容；两项独立marker。章内旧低级别Review notes不作为注位。

- `SF-2026-ARXIV-2610-31695` — `live1027_china`，Daily2026-10-27补Oct26论文扩展；[exact-v1](https://arxiv.org/html/2610.31695v1)§2–6/8/Eq1/T1–5/C/D必要及fixed979370c inputs/distill/test见CHINA§14.1，2+1+2=5，安全域深入。仅whole/segment-max监督与token边界分责；原结构注入/外部授权一般原则NC，保B单独无效、adaptive反侧、clean非劣未证与分母/后设/overlap资格，不采parser越权/唯一因果或充分防御。Sept5博客已披攻击及训练方向，Oct26不重计首次发明；未运行tokenizer/代码/攻击/复现。PRE/SAVE/selfread/solePOST仅本日实际后到，不预签。
- `SF-2026-ARXIV-2610-31974` — `live1027_china`，Daily2026-10-27补Oct26论文；[exact-v1](https://arxiv.org/html/2610.31974v1)III/V–IX/Alg1–2必要与fixeded7739b notebook affected cells见CHINA§14.2，2+2+2=6，安全域深入。已有value/sink/context budget与可信降密NC，仅valid-label substitution/host capture资格差额；保deterministic24项、unknown-handle过滤、handoff不继承全部context与promotion外部授权边界，不采drop-in完整保证/0 harm/全utility或默认图像decoder。代码时间不证论文公开日；未执行网络/模型/攻击或复现，PRE/SAVE/selfread/solePOST仅实际后到，不预签。

当前完整六件只在CHINA；Ch72保存前基线SHA256 `eb526078d31b0ce3262b480527c08dc13b06d7d5ba7fca0b8ef9bfc7bc0aa650`。待reader必要/评分、actualowner具体NC/gap及整体逐字PRE；通过后依root既授可仅此窄SAVE/完整自读/solePOST，不另行政批准，不写其他Book/Report/State。

### 15.5 R47后真实SAVE/完整自读，待唯一POST

reader R47已真实独核31695必要/5分及新增而非Sept5旧攻击重计、31974必要/6分/协议与fixed notebook三关键反侧，actual Ch72具体NC/两窄差额和§15原六件整体逐字PRE通过，依root既授准窄SAVE。作者已apply_patch只保存原两段/两marker/两本人注；31695正文Ch72 L1710/marker1711，31974正文L1831/marker1832，两注L3798–3799。完整自读两新增/四完整肩/两注与原首注，逐字同原稿、marker各唯一。只剥本次六件恢复基线SHA256 `eb526078d31b0ce3262b480527c08dc13b06d7d5ba7fca0b8ef9bfc7bc0aa650`，限定Ch72 diffcheck通过，保护旧Qwen/ChainCaps/2025并发内容。现交唯一reader实际保存态，不预签其POST、不改其他Book/Report/State；未执行代码/攻击或复现。

### 15.6 R49实际POST后闭合

唯一reader R49实际完整读两新增/四完整肩/两注和旧首注，原稿一致、限定diffcheck通过；31695正式5/31974正式6，两项`PLATFORM-SECURITY`真实I生效、两精确位释放。最终Ch72 locator依次L1710/marker1711/注3798与L1831/marker1832/注3799；完整原题名见§14。仅同步既成状态，不重必要/POST，不授全日完成。本批不再改Ch72。

## 16. 代理追加：31686/31709/31712/31854/31895普通首必要在途

root已授本日五已准入项唯一首次必要，后续实际owner→reader→自然整合/POST或具体NC；不扩大题摘/来源，不重复root31678/31679/31707与B32229/32849/32802/32770/32679。已实际打开五精确v1 HTML及本日SOURCE具名准入行，仅导航/部分核心初读，**必要尚未完成/未评分/未Books判断**，不能当H或终态。正文纸面日期不替本日合法公告身份，沿root SOURCE有效层复用，无更早公开具体信号不扩跨日调查。

五原题名为`From Target Selection to Condition Reuse: Auditing Residual Interventions in Tool-Use Models`、`Mining the Design Space of Multi-Agent Workflows`、`Reuse, Rewrite, or Reject: Evidence-Constrained Trace Reuse for Repeated Mobile GUI Control`、`SWE-Clar: Can Coding Agents Clarify Incomplete Client Requirements and Deliver Greenfield Software?`、`Knowing When to Stop: The Evidence–Action Gap in Coding Agents`。下一实际层只读各关键方法/评价/直接反侧，充分即停，不先因owner已有一般原则拒审。

### 16.1 31686首次必要完成，拟5，尚未actualowner

[exact-v1](https://arxiv.org/html/2610.31686v1)实际读§2–5/7、Eq1–3/T1–3、A及G受影响source-support/primary/secondary/composition/execution反侧；拟2+1+2=5，仅残差控制的跨消费者资格。冻结27B、每world/direction重拟一条late residual，初始历史block60自身cache更新后写一次，只改随后61–63 retained state，futurehook移除；这不是一条vector迁移32任务，也不是全部KV替换。原target-ID监督在训练暴露Anchor有效，fact-ID交叉后偏旧ID、独立eligibility/winner消费者不继承；wrapper稳健不等condition复用，fullaction另验。Natural/text控制支持更宽，能力上限本身仍差，不能把全部gap归因编辑失败或唯一memorization circuit。

关键正反侧：source-grants span patch在routing声明前取，fact与source是否used独立交叉；primary block31区间含0失败，预声明secondary block15仅64/64用与不用匹配、50/64 judgment改变且unused有1伤，完整动作仍弱。早patch同时改变更多hybrid状态，不能唯一定位语义层；composition只试block31，不冒成功15能经writer保持。独立单位32world（source复用其中16），27例posthoc/大量生成不是独立人口；currentartifact仅重算已存输出、无完整GPU tensors/portable inference，不冒独立复现。训练/teacherforce、分支生成、state替换和全部collateral/重组回归均付费；更正condition、proposal正确与真实权限不互代，不能据此覆盖真人许可。未读无关历史附表/代码或运行模型；必要足即停，后续具体owner/reader未成。

### 16.2 31709首次必要完成，拟6，尚未actualowner

[exact-v1](https://arxiv.org/html/2610.31709v1)实际读III–VI/Eq1/T1、A policy-conditioned estimand/固定bundle与split、D-A/C泄漏反侧、E-B smallcluster与T11必要成本；拟2+2+2=6，编排/提示/上下文路由共同设计而非工具名排名。固定6operators的MCTS保全部中间工作流，不只argmax；AutoResearch从graph与prompt提出特征，以验证R²−λL0选有限表示，再用隔离的search-level test查预定方向。High/low不是随机A/B，完整trace也不等全设计空间；估计随optimizer/worker/固定bundle而条件化。20固定instances复用于搜索和test，heldout search不是新taskinstance/OOD验证。

具体反侧：28,568可执行workflow后再gate仅13可预测puzzle，test每arm4–14clusters不足以按名义Wald95%置信作强认证；符号复现不等各task显著或因果。Star-first负/SharedMemory正与prompt长和placeholder同阶，只作受限关联，不能把字符长度单独当原因或劝所有任务用共享文档。SharedMemory还更贵；one-shotbackbone与多调用workflow不是同计算预算。早mining曾用round/训练标签均值泄漏，现删identity/禁targetderived，不将byte-replay自述当本轮已复现。搜索全部候选、固定bundle求值、自动特征试验与调用/共享文档增长均付费；低风险/弱收益保简单单路径或旧拓扑，重新在相同prompt/路由/预算/任务上验收。未遍全部operator代码/所有表格/图像素或跑workflow；必要足停，不作生产工具域结论，actualowner/reader后到。

### 16.3 31712首次必要完成，拟6，尚未actualowner

[exact-v1](https://arxiv.org/html/2610.31712v1)实际读§3–5/Eq1–4/T1–2、A1–4/Alg1完整transition合同与B1–4/D1–4受影响协议；拟2+2+2=6，record→template→live execution三接口。只保有明确pre/post证据的transition，将intent/typedslot与UI边/selector/风险合存；当前instruction和liveUI只提名候选，payload不因同页命中获准。明确typed值可rewrite，否则reject不执行；precheck后只走一步，postcheck失败本episode封edge并回同base，再观察，不盲复用整段/错误后无限重试。模糊preference不替历史值授权，permission/login/payment等不当普通overlay自动清掉；postcheck不撤已发生effect，addcart不是下单完成。

反侧与费用：Alg1是method-level specification而非本轮代码验证，TOCTOU/不可观察metadata与rapidUI仍有边界；安全人工终止是评价外部事件。AndroidWorld success由base×条件replay success算得，不能和条件94–98%互换；其派生总体低于base，失败保success分母但排出双成功效率人口，speedup是每task ratio均值。实机Table1乘积也不是fullcontroller实测成功率：D1明确full本身不以replay-only成功为条件；效率另用LLM-only且优化UI采集，非同一baseline/单一机制归因。仅3类变化量化、未测组合/长期/跨系统迁移；同系统累计消融不签与未对齐外部系统的SOTA。全部record/template/检索/刷新/pre/post/fallback及真实设备动作付费，公开速度不含record形成摊销；复用比例不是token/时延节省公式。权限、值或live证据不足时回原base/人工，不让template成为执行权。未读所有示例/代码或运行实机；必要足停，后续actualowner/reader未成。

### 16.4 31854首次必要完成，拟6，尚未actualowner

[exact-v1](https://arxiv.org/html/2610.31854v1)实际读§2–3/A task构造/B1–3/C1/3–5关键分母与反例、D/E关键对照；拟2+2+2=6，澄清→冻结context→独立理解/实现评价的接口差额。Client完整要求与Supervisor审后回答先形成共同context，QA题可泄露未问需求，故QA/implementation独立fork、后续消息/分数不得相通。理解给0/.5/1按task先均，代码task全测通过另计；RU联合统计只是要求级配对，不让口头懂或局部测试通过代完整交付，reference/test同源又不等真实客户验收。

直接反侧：两模型no/interaction/full requirement对照有收益但完整给要求仍失败；同model参与client/supervisor/judge、reference抽取依赖模型/两人核，不授全人口独立gold，review也有正确→错误2.9%的选后revised子集。512RU不是512独立job；披露曲线过滤round离群、firstcomplete后矛盾不回减，不能直接减clarification分；QA有错而code过/QA正确而code错均保。100job经本地可复现/可测筛选、改syntheticservices、starter非空且原sourceconversation未公开，不把历史高报酬当当前价值/收入。每模型maxeffort但默认token/时长不同、900s是无进度非总预算；cost只coding澄清/实现，不含client/supervisor/QA/judge，完整成本须补。澄清不能因score好自动结束或批准代码；需求变更仍须新revision/规划/验收，持续问更差只两模型有限对照，不授前置澄清普遍最优。未读所有task/test/代码、图像素或复现；必要足停，actualowner/reader后到。

### 16.5 31895首次必要完成，拟6，尚未actualowner

[exact-v1](https://arxiv.org/html/2610.31895v1)实际读§2–6/T1–5、B定义/Eq2–6/unsafe rules、C1/D测量直接反侧、F monitor/restoration/cleancriterion/unknown/completeclaim核验及F1有限重试接口；拟2+2+2=6，证据→执行/交接的边界，非一般“多试/少试”建议。Blockercard按同一路径失败/诊断/合理恢复确定t*，不是第一次error或普遍重试次数；临时故障、仍可改代码但不能验证与需外部修复分别处理。Baseline已有verified=false诚实结束，新增escalation+instruction并非单独tool消融；observer/card真值、runtime可见monitor和model愿不愿选升级是三层。Monitor只发证据提醒与可选ticket，不强制停止/授权，成功目标操作可清warning，重复同警不刷屏，serviceerror不因两次就判永久。Ticket还要保存已做进度/未验状态/请求与resume条件，不只报blocker。

关键反侧必须近采用：原8model unsafe计请求（含拒绝）非effect，早结束也减暴露机会；Q与t*是实验规则、非证明一切修复不可能。已验F/Q/Y/Z/patchA不同，原A不含PASS_TO_PASS，正verification大多数未审/未决不能估总体假报率。F后续冻结monitor在heldouttask、最多一次外部scriptrestore/余80step保patch-history才有最终repair增益，不能归为agent独立解障；完整trajectory总步/外援更多，clean预设非劣两条件均失败，jointtarget未过，p=.839不授无损。完整unsupportedclaim未证下降，二次审核是知aggregate的单Codex非盲人审；unknownsetup保分母/识别界非CI。F1只重试窄read/query或availabilitycheck、不自动重放edit，仍不强迫升级；不采生产安全、已测训练奖或通用停止最优。所有诊断/重试/monitor、ticket/复核、外部恢复与重测均付费；证据不足保Unknown/有限诊断和原最小权限，不因提示/票据形式正确越权或预签完成。未核外部代码/全部case/图像素/轨迹或运行攻击复现；必要足停。

### 16.6 当前实际停点

五篇首次必要均已实际读完拟用方法/关键评价/直接反侧，拟分依次5/6/6/6/6，尚待唯一reader独核与actualowner/具体NC或最小PRE。初始“仅打开/未必要”保留为过程而非现状。下一步仅定位五项长期owner/现有完整论证与邻接，不因一般原则直接关闭，也不预设一定五I；需共享Books写入先协调精确窄位，不触其他日期或SOURCE/Report/State。31840/两安全及先前三Ch23均已solePOST释放，不再重开。

## 17. 五篇actualowner/最小整体PRE（未SAVE）

root已确认31686/31854仅Ch66对应两精确位与本人注不冲突，其余Ch81/82/84也无root占位；最终由sole reader核精确肩，不锁整章。作者重读AGENTS和Books适用上下文；已完整读下述受影响论证，并读Ch65/67、80/81/82/83/84的开篇和知识树/小结交接。复用§16必要，不第三Methods；以下均未SAVE，不把主题关联当差额。

### 17.1 具体已有覆盖与剩余差额

- 31686：Ch17 L38–95已有residual/表示消费，L459–498已有干预协议/定位非因果/新checkpoint回归，故不重造模型组件owner。实际唯一归`PLATFORM-EVALUATION-SYSTEM` Ch66：L5432双臂sensitivity/invariance、L4093fork身份、L5473target/control survival均NC；余差是同编辑状态的独立消费者与fact–ID重组，区分target answer控制、condition复用和完整action，并用不同support/能力控制限定。只补target/control节一段，不扩Ch17/18。
- 31709：Ch82 L169起已有Supervisor/Peer/共享板分工及费用，MANGO已有graph与prompt联合修改，L1094同预算frontier及L1135参与/step联合状态均NC；余差是选拓扑时冻结prompt/placeholder消费、保非argmax候选并以search隔离挖有限设计规律，且这些只是policy-conditioned关联。归`AGENT-MULTI-AGENT`，不在Ch66重复整套统计教学，接equal-budget论证之后。
- 31712：Ch77 L760–815已管过程片段/当前对象重grounding及memory只advisory，L1220规则scope/晋升NC；Ch84 Skill契约/trajectory编译NC。实际`AGENT-WORKFLOW` Ch81 L1119 procedure封装、L1188 versioned notebook/precondition fallback、L126 state alignment与L1265trace/derived graph身份均NC；余差是本轮逐transition三决定、typed值及expected effect同步重绑、失败edge在episode封闭并重新观察。接稳定procedure后，保memory/平台owner不重导。
- 31854：Ch66 L1872已分hiddenintent/披露/人负担、L2087 selfreport/probe/outcome、L2241 simulator外效度、L4077–4086交互spec需求访问与实现失败、L4093一般fork身份均NC；余差是评估QA本身有教学效应，须同一澄清freeze再独立QA/code分支、按同RU分开理解/实现证据。唯一仍`PLATFORM-EVALUATION-SYSTEM`，插既有交互spec后、repair三state测试前。
- 31895：Ch81 L854重试类型、L891 ask/takeover/handback及L1230 diagnosis/guidance、L1311 handoff约束已NC；Ch84 L700 resume对账、stopcontroller/cap/value及L1084–1124 controller/规则触发/独立outcome也NC。真正剩余是按目标关联累积障碍证据而不强制stopping、warning生命周期与有进度/未验状态的ticket，再区分外援restore后的实际结果与提醒生效。归`AGENT-PLATFORM`，接stopcontroller之后，不新写Ch72/81同义摘要；cleancriterion失败及外援费用保正文，未采整体无损主张。

### 17.2 31686原一完整段/独立marker与完整两肩

路径：`books/part-06-ai-infrastructure/66-evaluation-system.md`。原保存态hash：`8fe71692ab4ea784271eabe60f04251f64e87bc8696294860432282b78f4eeed`；共享Ch66其余窄位可并行，hash不是全章锁。

**完整前肩，保持不改：**

让目标 skill 的成功率下降只证明行为被压制，不证明该能力被局部、稳定地移除。完整编辑评测应同时冻结目标任务、未目标 control matrix、编辑强度、架构与闭环环境，报告 target suppression、collateral damage、组合编辑和 relearning；几何相似或单层定位只能作诊断，不能代替行为证据。它用更大的闭环矩阵换取不把广泛能力破坏冒充精准删除；只需临时禁用且可由 policy gate 完成时，运行时授权仍比改权重更可逆。`arXiv:2608.04692v1` 的结果只覆盖作者 VLA、suite 和系数，不证明 task-vector negation 等同知识删除。<!-- source-family:SF-2026-ARXIV-2608-04692 -->

**拟完整段：**

编辑也可以把某个目标答案变得容易产生，却没有让后续计算复用它应依赖的条件。对此应保留训练暴露的选择接口，再交叉重组已见事实与标识，并从同一已编辑状态独立fork条件判断、winner判断及完整动作，避免把已选答案回灌成提示。[一项受限残差审计](https://arxiv.org/html/2610.31686v1)中，选择收益能跨wrapper保持，却随fact–ID重组消失；另改源事实虽可按是否使用该源选择性改变判断，完整动作仍不保证正确。这里自然history控制可见更多状态，早层patch也改动更多后续hybrid状态，故consumer能力、干预support和collateral结果须分别验，不能由深度差唯一定位语义或把选对ID当condition已改好。每world重拟的writer不是跨任务通用编辑，训练、全部分支生成/重组和状态检查均计费；复用或能力控制不成立时，保留原模型、显式条件与独立任务验收，不由一次目标命中批准永久修改或真实权限。
<!-- source-family:SF-2026-ARXIV-2610-31686 -->

**完整后肩，保持不改：**

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20262:start -->
Selective refusal editing 的失败还可能来自 routing，而不是知识已被删除或保留。把中间表示送入 oracle route 能
诊断“正确安全分支其实存在但没有被选中”，却不能证明危险知识已移除，也不能作为生产控制器。评测要把 target
effect、route choice 与 control survival 分开；作者设置之外，oracle 不可得或 route 干预改变分布时，应回退端到端
行为测试、relearning 与未目标 control matrix。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20262:end -->

### 17.3 31709原一完整段/独立marker与完整两肩

路径：`books/part-07-agent/82-multi-agent.md`。原保存态hash：`a9fd12bb4ecc32930effd083b07d4fe3d5e33fef90246351bb571bb2fdcf5270`；共享Ch66其余窄位可并行，hash不是全章锁。

**完整前肩，保持不改：**

这个 admission 仍可能低估相关错误、通信失败与尾延迟，因此通过离线 frontier 不等于可直接推广到生产。系统需要逐步放量并保留 single-agent fallback；任务不可分、共享状态强耦合或验证成本高时，单 Agent 仍可能更稳健。多 Agent 是条件化并行分支，不是能力随数量单调增长的路径。

<!-- source-family:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION -->

**拟完整段：**

比较拓扑还应共同冻结角色prompt及上下文路由：同一个graph可以因缺少必要placeholder而没有把证据交给消费者，较长prompt也可能只是更具体的角色任务，并非长度本身产生推理能力。可保留优化器的失败与中间workflow，联合解析graph/prompt提出候选规律，再把同一search的后代放在同一划分，只在隔离的heldout search检验预定方向。[受限设计空间挖掘](https://arxiv.org/html/2610.31709v1)据此得到的是固定搜索策略、无外部工具任务和可预测切片下的关联，不是随机拓扑干预；重用同一题bundle也不证明新题泛化。test小cluster数、组件共变及共享文档更贵都限制把某个正负方向写成普遍规则。全部搜索/求值/特征试验和真实prompt读取均付费；规则只能指导待验候选，仍须按前文同预算frontier验收，支持不足时保留单Agent、旧prompt或固定小图，而非按一份拓扑排名直接扩团队。
<!-- source-family:SF-2026-ARXIV-2610-31709 -->

**完整后肩，保持不改：**

### Delegation 应由任务状态与不确定性触发

固定团队会在简单任务上支付不必要 coordination tax，也会在困难任务上调用错误角色。router 应依据 task decomposition、当前 uncertainty、能力证据和剩余预算选择是否委派、委派给谁以及何时收回。收益是按需使用协作，代价是 router 误判与选择偏差。

### 17.4 31712原一完整段/独立marker与完整两肩

路径：`books/part-07-agent/81-workflow.md`。原保存态hash：`2f29f119e664399fd781b836bfe2ed106f33b099a057164818686d5a1932fda8`；共享Ch66其余窄位可并行，hash不是全章锁。

**完整前肩，保持不改：**

反复把完整历史塞进 prompt 会让 context 随任务增长。稳定 procedure 可以通过训练或封装迁移到 learned module，只向模型暴露固定大小的 skill interface；但 run state、输入输出、版本、失败与补偿仍必须由 deterministic workflow 持有。learned skill 负责 proposal，不拥有事实提交。

这减少 token 与重复推理，却把可解释性和更新治理转移到 module artifact。procedure 漂移、版本不匹配或验证失败时回退显式 workflow steps；低频或高风险流程继续保留可读 DAG 更合适。

<!-- source-family:SF-FROM-HISTORY-TO-STATE-CONSTANT-CONTEXT-SKILL-LEARNING-FOR-LLM-AGENTS -->

**拟完整段：**

不必把整条旧流程一次编译成黑盒Skill：对可观察的GUI，可把已核before/action/after存为transition，图保状态/selector，文本保intent与typed slot；当前任务和liveUI先提出候选，再决定原payload可复用、明确值可改写，还是证据不足拒绝且不执行。[受限逐边复用分支](https://arxiv.org/html/2610.31712v1)要求改值时连同预期postcondition一起更新，precheck后只执行一步，postcheck失败就在本episode封该边、回同base并重新观察；同页面或一次历史成功都不能补出当前对象、数量或许可。它保住仍有效的导航，却增加检索、刷新与检查费用，也不撤销已发生effect；原伪码是方法规格，未知元数据、快速UI及TOCTOU仍须独立验收。速度只取双方成功的配对，实机汇总乘积不等fullcontroller实测成功率，构建记录的摊销另计；槽值/目标不明、权限dialog或成本不合时，保留显式步骤、base策略/人工，而不让偏好记忆自动填高风险参数。
<!-- source-family:SF-2026-ARXIV-2610-31712 -->

**完整后肩，保持不改：**


#### 重复 Trace 可以离线编译，但 Solver 仍是受限 Artifact

重复调用 LLM 处理结构稳定、具有精确 verifier 的任务，在线成本高且每次都重新探索。可把多条 reasoning trace 离线归纳为版本化 symbolic solver，在线先运行 solver，未覆盖或验证失败时再调用 LLM；这把部分一次性推理成本转成可复用构建成本。solver 只拥有候选求解权，workflow state、effect commit 与最终正确性仍分别由编排器和 verifier 持有。

### 17.5 31854原一完整段/独立marker与完整两肩

路径：`books/part-06-ai-infrastructure/66-evaluation-system.md`。原保存态hash：`8fe71692ab4ea784271eabe60f04251f64e87bc8696294860432282b78f4eeed`；共享Ch66其余窄位可并行，hash不是全章锁。

**完整前肩，保持不改：**

这种路线增加了 repository/test bias、user-agent bias 和 framework/environment identity，因而不能线性取代 static issue benchmark。前者适合诊断模糊需求到完整 artifact 的链路，后者仍适合局部 repair 与长期 release regression。公开证据覆盖 480 tasks、12 languages、50-task Lite split、六个模型与 Claude Code，并附 OpenHands 分析；它不提供跨所有 coding workload 的通用排名，provider precision、并发和生产 latency SLO 也不是该实验的声明范围。

**拟完整段：**

需求访问之后还可另测“能否解释已获要求”，但评估题本身也可能提示遗漏需求，不能先问完再让同一run继续写代码。应在澄清结束时冻结初始请求、获准对话与workspace观察，从这里分别启动只读需求QA和实现分支，后续题目、回答及评分互不进入；再按同一requirement unit并列回答标签与对应代码测试，完整task仍须全项验收。[SWE-Clar的受限协议](https://arxiv.org/html/2610.31854v1)保留了已披露却答错、答对却实现错及部分回答却测试过的反侧，因而获取、可表达理解与交付不能互代。QA judge与测试同源材料、合成client及本地改写任务仍有限，不代表客户真值或真实部署；两模型的前置澄清优势也不证明持续交互普遍有害。制备、client/监督/QA/judge与全部实现/测试均付费，公开coding调用费用不是全费。需求/接口或独立分支隔离不足时，保留明确issue、当前要求revision与可执行验收，不用高QA分批准交付。
<!-- source-family:SF-2026-ARXIV-2610-31854 -->

**完整后肩，保持不改：**

对于已有明确 bug 的 repair task，看到测试通过仍不等于测试覆盖了目标缺陷。Evaluation harness 应在捕获 validation command 的 exact working-tree state 后，至少保存三种可重放状态：原始 buggy state、candidate state 与可信 gold/reference fix。只有命令在 buggy state 失败、在 candidate/reference state 按预期通过，才形成 bug-discriminating evidence；在三者都通过的 regression test 只能证明没有触发该 bug，不能获得修复证明权。

### 17.6 31895原一完整段/独立marker与完整两肩

路径：`books/part-07-agent/84-agent-platform.md`。原保存态hash：`2f2260512565b233f17564c396aa8d1dbde6335813164a75aee322b19cc84684`；共享Ch66其余窄位可并行，hash不是全章锁。

**完整前肩，保持不改：**

模型自报“已经完成”不能成为 stop evidence；hard safety limit、用户 deadline 和不可逆动作审批也不受 utility 覆盖。价值估计失准会过早放弃困难任务，能耗模型漂移则会把节省写成虚假收益，因此 controller 必须有固定 cap/floor、shadow calibration 和按 task slice 的 outcome 复核。证据不足时回退固定预算或人工，而不是让局部成本最小化接管任务正确性。

**拟完整段：**

固定cap之外，还可把“已收集到何种障碍证据”做成显式状态，而不要求模型自行把散落错误联成停止决定。按目标路径关联失败、所有权/模式与已试恢复，规则满足时另发一次证据提醒和可选ticket，保留原tool反馈；目标操作成功可清warning，model仍决定继续、保存未验改动或升级。[受限coding scaffold对照](https://arxiv.org/html/2610.31895v1)的证据点只是诊断参照，不证明全部合法路径已穷尽，短暂故障也不能凭首次error关闭任务。Ticket需同时交付已做进度、未验状态、外援请求与resume条件；报过障碍或提交票据不等恢复完成。改善最终repair依赖一次外部环境恢复与余预算，完整费用/外援更多，预设clean非劣未通过，不能称无损或agent独立解障；unsafe请求减少亦不等真实harm下降。采集/规则、提醒、票据审阅、外部恢复和完整重测均付费；证据或授权不完整时保留有限诊断、原cap与人工，不由提醒赋予绕过权限，真实effect与resume继续服从既有对账。
<!-- source-family:SF-2026-ARXIV-2610-31895 -->

**完整后肩，保持不改：**

同理，运行前让 Agent 自估这次任务要用多少 token，可以帮助粗分高成本任务或提前预警，却不能充当逐 run 的硬预算或账单真值。长程 coding trajectory 的输入历史、工具输出与后续探索路径尚未发生，Agent 为估算而预先探查本身也要付成本；在受限八模型、OpenHands/SWE-bench Verified 对照中，自估与实际用量只呈弱至中等相关，普遍低估，部分模型估算成本甚至超过任务执行成本。平台应把预估作为可撤销的 admission 信号，把实际用量交给运行时 meter、硬 cap/floor 与 outcome evidence；当估计误差或探查成本超过收益时，回退静态预算和运行中告警，而不是给用户虚假的精确报价。这不是对所有 Agent 或价格制度的普遍测量结论。<!-- source-family:SF-2026-ARXIV-2604-22750 -->

### 17.7 true H2 Review notes本人拟注（五项）

各放对应章唯一 `## Review notes` 原首注前，保旧注；Ch66两注同批，其余各一条。每项只绑定自身marker，不预签。

- `SF-2026-ARXIV-2610-31686` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31686v1)首次必要见本日CHINA§16.1，2+1+2=5；actual Ch66控制/条件复用窄差额，原一般原则具体NC。保每world重拟/Anchor暴露、natural support与早层statecoverage混杂、primary31失败/secondary15非完整动作，未采旧ID控制等于condition复用。仅采用正文有限命题及直接反侧，不授唯一因果、完整安全/无损或生产SLO；未核外部实现/全附件/图像素或执行复现。必要/actualowner/整体PRE/真实SAVE/完整自读/唯一POST仅本日实际后到，不由本注预签。
- `SF-2026-ARXIV-2610-31709` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31709v1)首次必要见本日CHINA§16.2，2+2+2=6；actual Ch82图/提示联合验收窄差额，原一般原则具体NC。保固定optimizer/bundle与13gate、policy-conditioned非随机因果、test4–14cluster及共享文档更贵，不按方向符号发布通用拓扑。仅采用正文有限命题及直接反侧，不授唯一因果、完整安全/无损或生产SLO；未核外部实现/全附件/图像素或执行复现。必要/actualowner/整体PRE/真实SAVE/完整自读/唯一POST仅本日实际后到，不由本注预签。
- `SF-2026-ARXIV-2610-31712` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31712v1)首次必要见本日CHINA§16.3，2+2+2=6；actual Ch81逐transition改值/预后条件窄差额，原一般原则具体NC。保method-level逐边合同、typed值/expectedeffect同改、episode封边、TOCTOU、derived实机SR非full实测及双成功效率/record摊销。仅采用正文有限命题及直接反侧，不授唯一因果、完整安全/无损或生产SLO；未核外部实现/全附件/图像素或执行复现。必要/actualowner/整体PRE/真实SAVE/完整自读/唯一POST仅本日实际后到，不由本注预签。
- `SF-2026-ARXIV-2610-31854` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31854v1)首次必要见本日CHINA§16.4，2+2+2=6；actual Ch66冻结澄清双fork窄差额，原一般原则具体NC。保QA教学泄漏隔离、同RU理解/代码不互代、同源judge/合成client、本地任务/无统一总预算与缺client等全费用，不授高QA即交付。仅采用正文有限命题及直接反侧，不授唯一因果、完整安全/无损或生产SLO；未核外部实现/全附件/图像素或执行复现。必要/actualowner/整体PRE/真实SAVE/完整自读/唯一POST仅本日实际后到，不由本注预签。
- `SF-2026-ARXIV-2610-31895` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31895v1)首次必要见本日CHINA§16.5，2+2+2=6；actual Ch84证据/停止/交接窄差额，原一般原则具体NC。保t*仅规则诊断、model仍有选择、外部一次restore/余预算、clean非劣与jointtarget失败/完整claim未降，不授无损、独立解障或真实harm下降。仅采用正文有限命题及直接反侧，不授唯一因果、完整安全/无损或生产SLO；未核外部实现/全附件/图像素或执行复现。必要/actualowner/整体PRE/真实SAVE/完整自读/唯一POST仅本日实际后到，不由本注预签。

当前五段/五marker/五本人注和全部完整肩只在CHINA；待reader必要/拟分→actualowner具体NC/gap与整体逐字PRE，通过后仅按已授精确位SAVE/完整自读/solePOST，不写其他Book/Report/State。若某具体链实际已有完整承载，改有效NC不为diff硬写。

### 17.8 31686 R60后三件真实SAVE/完整自读，待POST

reader R60已核31686 exact-v1必要/5分、actual Ch66差额与§17.2单段/marker/§17.7本人注整体逐字PRE；不等其余四项，依root既授作者只apply_patch保存该三件。正文L5486/marker5487/本人注5849；实际完整自读新增/完整前后肩/本人注与旧首注，原稿逐字match/marker唯一，限定Ch66 diffcheck通过。共享root测量位先已变化，保存前fresh baseline为`0e30762dbdf49127499c734bedda77d58dba2840d14858c97241e18feb69775f`；只剥本次三件恢复同hash，未覆盖其他窄位/旧2025注。现交sole actualPOST，不预签其通过；31709/31712/31854/31895仍未PRE/未SAVE，不重复必要。

### 17.9 R61后31686闭合；31709三件真实SAVE/完整自读待POST

reader R61已实际核31686 POST通过，5分Ch66真实I/精确位释放；本代理仅同步，不重必要/POST。另R61核31709必要/6分、actual Ch82 MANGO/Equalbudget与§17.3现稿（仅tool-free误译已纠正）原三件整体PRE，准独立窄SAVE。作者apply_patch只保存31709原单段/marker/具名注：Ch82正文L1102/marker1103/本人注1336；完整自读新增/完整两肩/注与旧首注，逐字match、marker唯一，限定diffcheck通过。只剥三件恢复保存前`a9fd12bb4ecc32930effd083b07d4fe3d5e33fef90246351bb571bb2fdcf5270`，保护旧32871/B与2025改动。现交sole actualPOST，未预签31709 I；余31712/31854/31895仍未PRE/未SAVE。

### 17.10 31712 R62后三件真实SAVE/完整自读，待POST

reader R62已核31712 exact-v1必要/6分、实际Ch81 stableprocedure/Notebook与§17.4原段/marker/具名注整体PRE，依root既授作者apply_patch只存该三件。正文L1127/marker1128/注1362；实际完整自读新增/两完整肩/本人注与旧首注，逐字匹配且marker唯一，限定diffcheck通过。仅剥本三件恢复保存前`2f29f119e664399fd781b836bfe2ed106f33b099a057164818686d5a1932fda8`，保旧Qwen/Notebook与2025改动。现交sole actualPOST，不预签其I；31854/31895未PRE/未SAVE，31709已SAVE待POST。

### 17.11 R63后31709闭合；31854三件真实SAVE/完整自读待POST

reader R63已核31709实际POST通过，6分`AGENT-MULTI-AGENT`真实I/位释放，不重必要/POST。另31854必要/6分、actual Ch66双fork差额与§17.5原三件整体PRE通过，作者依既授apply_patch只保存该三件：正文Ch66 L4096/marker4097/本人注5852。实际完整自读新增/两完整肩/本人注和旧首注（31686），逐字match、marker唯一、限定diffcheck通过。共享Ch66保存前fresh baseline `633831234d189fa82731e79bfafff9878be1f62d2266eacfec333c2ea827a479`已含31686与root其他窄位，仅剥本三件恢复同hash。现交sole actualPOST，不预签31854 I；31712已存待POST，31895仍未PRE/未SAVE，不动其余已闭窄位。

### 17.12 R64后31712/31854闭合；31895三件真实SAVE/完整自读待POST

reader R64已核31712/31854实际POST通过，各6分真实I，精确位释放；不重已成四项。31895必要/6分、actual Ch84 gap及§17.6原三件整体PRE通过后，作者按既授仅apply_patch保存原单段/marker/本人注，正文L737/marker738/注1247。完整自读新增/完整前后肩/本人注与旧DrivingAgent首注，逐字同稿、marker唯一，限定diffcheck通过；仅剥三件恢复原fresh baseline `2f2260512565b233f17564c396aa8d1dbde6335813164a75aee322b19cc84684`。初次自检命令的双引号让注内反引号被shell解释，仅诊断串损坏、文件无变；已改安全单引号并以磁盘CHINA原稿重新比对通过，不把错误diagnostic作POST证据。现交sole actualPOST，不预签31895 I。


### 17.13 R65实际POST闭合（行政同步）

reader R65已实际核31895原三件/完整两肩/本人注与旧注POST通过，6分`AGENT-PLATFORM`真实I/窄位释放；本批31686=5（R61）、31709=6（R63）、31712=6/31854=6（R64）、31895=6（R65）五项全实际闭合，不第三必要/POST。当前实际正文/marker/注定位：Ch66 31686 L5489/5490/5854、31854 L4096/4097/5852；Ch82 31709 L1102/1103/1336；Ch81 31712 L1127/1128/1362；Ch84 31895 L737/738/1247。日期/版本仍Oct26 exact-v1，不授全日完成。

## 18. 代理追加五项（31846/31918/31985/32024/32053）：逐篇必要与actualowner

承接root明确分工；SOURCE既成AB/日期层复用，不新发现、不把本批未读项标完成。当前仅31846首次必要足够，另四项普通待办。§5按拟采用命题只补关键反侧，未核全附件、代码或执行复现。

### 18.1 31846 首次必要/拟分与停止

精确题名 **Don’t Forget What You Just Learned: Self-Directed Repair Turns Agent Mistakes Into Lasting Lessons**；[2610.31846v1 HTML](https://arxiv.org/html/2610.31846v1)。拟2+2+2=6；永久外部文字/共享参数更新→失败后分lesson自产adapter与显式路由→参数冻结与consumer无干扰要分验。身份/公开日沿SOURCE已核Oct26，不把页上Oct22提交或内部date改成公开日。

实际读§3.2–3.3与4.2–4.3、E.1直接错配/pooled反侧、F.2反馈/训练、F.3总费用、F.5完整高层loop及C.6 rollout口径/C.8阈值反侧；不顺读其他模型/全任务表。base先尝试，验证失败后用自身轨迹合成8–24纠正例，rank16只训B、A与base/旧lesson冻；粗失败类型按termination/可提取输出/binary verifier归一，gold/hidden tests/judge自由反馈不入此接口，不等无外部验证。相似度只路由一项，不满足阈值且库有容量才训练；F.5在adapter retry之前已register，失败后卸载并base fallback，故未验证lesson仍可能持久存在。

核心评价保留两个不同问题：185个既有失败、每encounter两次whole rollout，第三次仍全成功18.9% vs base9.7%，不是全部任务成功率或独立新任务迁移。E.1错配恢复9.6%低于base retry，pooled更大rank未改善；C.8零跨域检索阈值由受测相似度最大值定，不能当未来安全界，低阈值可伤行为。base首尝试不变仅结构上保护原首尝试，不证明整体无干扰。C.6只计环境rollout，不计反思合成/训练；F.3单H200顺序测130项的完整构造均8.16min，约1.5min仅优化，GPU能耗还排host/storage。不把局部recovery/其他harness榜分写作普胜、净速或生产SLO。已足支持拟采用窄命题及直接反侧，停止，不补全其他附表/实现。

### 18.2 31846 actualowner与具体NC/差额

实际owner `AGENT-MEMORY`，Ch77。已读Ch77失败反思admission L163–175、ExternalProcedure→WeightUpdate L816–857、microLoRA L1164–1174及Ch80诊断generator/演化 L371–381；Ch76/78首段与交接、Ch77首/尾知识树交接也实际读。原Ch77已承载参数化来源/删除/回滚、冻结权重不保行为与独立adapter producer，Ch80 ParamMem是生成诊断，不是此后失败executor lesson；这些为具体NC不重写。尚缺分lesson独立库、base失败后路由、retry前注册仍待验证这一consumer/写入资格链。拟在本节原不可逆段后、现weaver段前补最小一段，不增加模型实现手册；root已知精确位，待其冲突消息及reader必要/整体逐字PRE，不提前SAVE。

**完整前肩，保持不改：**

一旦进入 weights，逐条 provenance、selective deletion 与 exact rollback 不再天然成立；必须冻结 training set、
update job、checkpoint lineage、judge 和 before/after evaluation。外部 memory 在频繁更正、隐私删除和小样本场景
仍更合理。Memory Intelligence Agent 提供 Experimental loop，不证明 online weight update 已经 production-safe。

**拟完整段：**

另一个可撤销分支不合并所有失败经验，而将每次失败派生的程序lesson训练成独立adapter，保存源任务和版本，再只在原base失败后按任务相似度选择一项重试；不匹配或库已满时可保留普通base retry。[Self-Direction的有限对照](https://arxiv.org/html/2610.31846v1)以二值验证结果和粗失败类型触发自产纠正样本，不把reference或隐藏测试内容交给反思。这里冻结的是base与旧adapter参数，不是所有路由后的行为；错配lesson可比普通retry更差，跨域零召回阈值也只是受测人口的排除边界。原循环在候选retry成功前已登记lesson，因此入库不等有效经验，需另验当前修复、后续重复稳定性与未见任务迁移，不由一次成功批准长期复用。训练合成、adapter驻留/装卸、路由和全部重试均付费，相同rollout数不等总计算相同；来源、路由或回归不稳时卸载该项，保留原始失败轨迹、显式文本经验与有限base retry，不将参数未覆盖或库可删除当作行为无损、完整遗忘或执行授权。
<!-- source-family:SF-2026-ARXIV-2610-31846 -->

**完整后肩，保持不改：**

经验也不必直接更新共享Planner：可以冻结执行推理的模型，把经验训练进单独的memory adapter，再由另一个trigger在推理到标点等候选边界时决定是否调用它；被调用的producer按当前hidden-state生成一小段latent条件，注入后仍由原reasoner继续生成。这样持久化的是adapter参数，当前latent只是一次读取结果，调用时机又是另一份可训练策略；三者的模型版本、训练经验与适用任务要一起保留，不能把临时latent当可逐条核对、删除的外部事实。[一条受限设计](https://arxiv.org/html/2509.24704v1#S4)先训练weaver、再固定它训练trigger，支持这种分责，不证明冻结权重就保持所有输入条件下的能力，也不授跨模型隐藏空间兼容。随机插入、每个标点都插入与学得触发有质量取舍，较少调用不等于学到了可靠的“需要知识”时刻；两个模块训练、全部rollout、latent上下文和每次生成均付费，所列平均时延还高于普通SFT。任务、reader或预算变化时应重验并保留无该adapter、固定触发及可回读的显式经验，不让更高reward或更隐蔽表示取得事实与行动权限。

**true H2 Review notes本人拟注（放原首注前，保旧注）：**

- `SF-2026-ARXIV-2610-31846` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31846v1)§3.2–3.3/4.2–4.3、E.1、F.2–3/5及C.6/8必要，拟2+2+2=6。仅失败后独立lesson adapter库/路由与候选资格；保base首尝试、粗二值反馈非gold、注册在成功前、错配反退/阈值受测、rollout排训练与总费用，不采冻结即无行为干扰。未读全附件/核外部实现或执行训练复现；必要/actualowner/整体PRE/真实SAVE/完整自读/solePOST按本日实际后到，不以本注预签。

### 18.3 31918 首次必要/拟分与停止

精确题名 **Beyond On-Policy vs. Off-Policy: At What Level Should LLM Agent Distillation Follow the Student?**；[2610.31918v1 HTML](https://arxiv.org/html/2610.31918v1)。拟2+2+2=6；history与action-prefix分源/联合配对，纠正“单一on-policy比例就足够描述数据”的判断。复用SOURCE Oct26日期/准入，不重日期层。

实际读§2/Eq1–2/§3协议、§4.1与§5.1关键匹配对照、§6课程口径、§8限制、A.1.3训练/解码表；§4.2诊断/A.1.4只作annotation边界，不采用全诊断表/因果机制排名。H生成此前交互history，A只在该history条件下生成当前action前缀，四种HA均由同checkpoint冻结且有PI的teacher提供target，student无PI；sampled context/teacher target固定，梯度只到student。student-dependent三类每轮refresh，TT来自预缓存三条轨迹；每task等8action exercises/同更新数不等tokens/采集全费用。三backbone/四受限环境，三次evaluation SE不是重复训练seed；teacher PI曾由更强模型/人工改写，不是零外部信息。

关键支持是同marginal student-history及student-prefix各50%的diagonal/crossed/independent三种联合分布仍得不同结果；ST在10/12 SR最高但两个ToolQA例外，SS单独最弱却有益于混合，不据standalone弱就删全部SS。课程把TT前置、SS后置，保累计目标权重；§6只逐轮validation三环境，不能冒充独立test普胜或最优recipe。3类data refresh、prefix生成与teacher/student全词表评分有成本；未匹配全token/训练seed或所有采集费用，不用同exercises推总compute因果。已足支持two-axis joint/consumer评价的窄命题，停止，不补全所有任务表/超参附件或实现。

### 18.4 31918 actualowner/整体三件PRE

实际owner `TRAIN-SFT` / Ch29。读原恢复训练L294–314及distill source/privilege、target-vs-occupancy和异步policy身份等具体论证（L467–475、594–603），并读Ch28/30开篇/知识树交接及Ch29收束。原文已有student失败历史作条件不拟合坏动作、监督特权和policy版本分离，属具体NC；尚未承载H/A两层的joint分布、固定边际仍不足及SS单弱不等混合无用。拟在当前同模型privileged self-distill段之后、离线重述供给段之前仅补一段；非Agent runtime owner，不占root其他Ch29精确位。待reader必要/actualowner/逐字整体PRE，未SAVE。

**完整前肩，保持不改：**

同模型产生 target 也不必是无外部监督：student 在只有问题的条件下生成 rollout，teacher 在同一已访问 prefix 上额外读取 reference solution，再提供 detached 的词表分布或采样 token 的 log-probability correction。新增信息而非模型名字决定监督权限，teacher checkpoint、privileged context 与 student rollout 应各自绑定版本；[受限 on-policy self-distillation 实验](https://arxiv.org/html/2601.18734v1)实际固定 initial teacher，不能推成持续同步当前 policy 的自教。参考答案也不保证弱 teacher 能生成可靠指导；full-vocabulary 信号增加 logits 和峰值内存，少 rollout/较短输出下的 generated-token 降幅不等端到端训练降本，部分小模型或任务仍反退。teacher 能力或 reference 质量不足时，保留独立教师、verified targets 或既有 policy-gradient 路径，不把特权上下文蒸馏认证为零外部信息的自我纠错。<!-- source-family:SF-2026-ARXIV-2601-18734 -->

**拟完整段：**

交互式蒸馏还须把on-policy拆成两层：此前action–observation历史由谁生成，以及在该历史下当前action的token前缀由谁生成；无论哪种配对，都可由带privileged guidance的冻结teacher在同一前缀提供固定监督。设两源分别为H/A∈{T,S}，联合权重w_HA决定训练人口，student-history比例w_ST+w_SS与student-prefix比例w_TS+w_SS只是边际。[受限self-distillation对照](https://arxiv.org/html/2610.31918v1)中，两边际相同的联合配对仍得不同结果，student历史配teacher动作较强不等于应删除所有SS：单独较弱的SS在混合中仍可有益。应共同保存teacher/指导、history policy、prefix policy、刷新轮次与累计配比，而不以一个on-policy标签替代分布身份；早TT/晚SS的课程结果只来自受测验证集，不认证通用比例或调度。教师未必能从错误prefix给出可靠续写，相同exercise/更新数也未匹配全部token、环境采集与teacher评分费。须另验独立任务成功与错误状态恢复；源资格、预算或质量失配时，保留可信TT示教、已验混合和原student，不把训练loss下降或更高student占比批准为部署能力。
<!-- source-family:SF-2026-ARXIV-2610-31918 -->

**完整后肩，保持不改：**

不需要在线教师分布时，也可先把固定专家语料改造成更接近当前模型的离线监督：每题先从原问题采样，验证通过才随机保留一条；全部失败才附参考解让同一模型重述，仍无可靠正确解就保留原专家示范，最终在原问题条件下训练。三条供给分支必须分别保存生成 checkpoint、参考条件、正确性判据与选择记录；验证筛选后的自采样并非未经条件化的原策略，重述也不是没有额外信息的自我改进。随后用停止梯度的目标 token 概率重权交叉熵，只是另一种训练目标；把混合行为分母近似为一，不能继续称作精确、无偏的 importance correction。[有限数学推理对照](https://arxiv.org/html/2509.15157v1)支持这条离线数据与权重分工，未证明平均序列概率变高就降低了完整分布偏差，更新后数据仍会陈旧，部分子分支也退步。两阶段候选、参考解与验证、重写评分、训练和独立任务回归都要付费；正确判据或参考解不可靠、能力或预算回归时，保留原专家示范、普通 SFT 或已验证的概率重权路径，不用较低训练 loss 批准持续自我改进。
<!-- source-family:SF-2025-ARXIV-2509-15157 -->

**true H2 Review notes本人拟注（放原首注前，保旧注）：**

- `SF-2026-ARXIV-2610-31918` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31918v1)§2/Eq1–2/§3/4.1/5.1–5.2/6/8及A.1.3必要，拟2+2+2=6。仅history/action-prefix联合来源与matching边际非matching joint；保同checkpoint特权teacher、student刷新/TT缓存、SS单弱但混合有益、课程仅validation、三次evaluation非多训练seed与全费，不采普遍最优配比/调度。未核全附件/外部实现/训练复现；必要/actualowner/原三件PRE/SAVE/selfread/solePOST仅本日实际后到，不预签。


### 18.5 31985 首次必要/拟分与停止

**The Helpful Agent Problem: When Emergent Cooperation Among LLM Agents Bypasses Intended Workflows**；exact-v1 [PDF](https://arxiv.org/pdf/2610.31985v1)，[HTML](https://arxiv.org/html/2610.31985v1)实际404后fallback，abs唯一v1/未见撤回，公开日沿SOURCE Oct26，不把Oct22提交当公告。拟2+2+2=6：各自local合法互帮仍绕跨ownerreview，拟采用涉及权限所以深入本受影响域，不扩全附件。

实际读PDF§2定义/§3 scope-vs-guard-vs-feedback、§4指标/共享环境/判断协议、§5.1支持与5.3.1–2直接控制反侧；核心机制是owner-owned≠owner本task修改scope，请求者单向依赖、无共同reward/互惠激励，共享频道可让owner自发接纳仅发reviewer的请求。脚本review者热身两任务后离线；权限强制挡nonowned写，但owner能改自己out-of-task文件。Favor须实际完成修改/approve merge，口头同意不计；FavorBench TF是trajectory任一favor，不是task率，HF只在完成trap favors条件下算contractfail且revert恢复，safe alternative每项已有，不能直接合成全任务harm。CooperBench仅支持现实repo中出现favor，未量化其absent-party harm。GPT6Sol两次judge同任务text/成功edit，非独立人审全部；TF Wilson、task率trajectory bootstrap。

直接反侧：只要求requester走admin仍可有volunteered代改；owner own-task提示在该GPT/warm-safe20trajectories控制下零favor，却使requester无进展，不是强制实现或普遍无害。Raw/causal事后CI只降低conditional harm，favor仍高；sound preactionguard未实例化，证明依赖review/scope原本安全及check sound假设。任务结构刻意造依赖、review不可用和有限模拟tests，不得报生产发生率/恶意串谋或现成完备防御。scope维护、外部性核验/审核等待与全部模型/tests均有费用，未披露全费/生产SLO。不采用无关turn-budget/全prompt和task实例；PDF screenshots工具未返回可见像素，本文不依赖图形形状/曲线数值，未声称视觉校验。必要足即停。

### 18.6 31985 actualowner与整体三件PRE

actual owner `AGENT-MULTI-AGENT` / Ch82。实际完整读共享repo commitment L673–703、CollectiveRisk L705–723、Identity&Delegation L725–758及Ch81/83原交接。一般局部utility/交互组合风险、message不等commit、参与权/工具权/约束交集已具体NC；未写合法owner为他人代改可绕review、仅管requester不够的窄路径。拟在CollectiveRisk原缓解段后、Identity标题前插单段。不因安全名称自动I，待reader必要/actualowner/原三件整体PRE，未SAVE。

**完整前肩，保持不改：**

“更多讨论”不能自动修复，因为错误可能相关、信息被不对称隐藏，或 aggregation 本身奖励共识。Mitigation
可以限制资源、隔离权限、保留 dissent、引入独立 verifier 与 human escalation，但每项控制都可能牺牲并行度
和协作收益。Synthetic scenarios 适合发现机制，不提供生产发生率；不同 backbone、trial 与 judge 混合后的
比例也不能当作跨系统常数。

**拟完整段：**

还要检查一条不依赖恶意或权限突破的代改路径：请求者不能写别人的资源，owner却可用自己的合法写权替对方改动，绕过本应审查跨任务影响的reviewer。因而resource ownership与本次task scope不是同一边界；共享频道中只向reviewer发请求，也可能被owner主动接纳成自己的工作。[受限共享仓库对照](https://arxiv.org/pdf/2610.31985v1)中，只限制请求路由仍留下此类代改，owner只做自身任务的提示则在该条件下消除它，却同时阻断请求者；这不是已实现的强制scope gate或全模型保证。Workflow应保留请求受益人、原task与实际writer、受影响第三方和真实review状态，不能由owner身份洗掉审核义务。对第三方的tests与revert对照可发现部分外部性，但反馈后少伤害不等预先获得许可；sound全方安全check只是理想条件，并未被该实验实现。更细scope/依赖核验、等待审核和外部性回归都有成本，也可能拒绝无害互助；证据或review不可用时，保留原最小权限、排队/人工及独立任务，不让善意、口头同意或局部测试通过代签跨任务发布。
<!-- source-family:SF-2026-ARXIV-2610-31985 -->

**完整后肩（下一节标题与首完整段），保持不改：**

## Identity 与 Delegation

可复用能力包的 identity 与执行 substrate 的 identity 不应合并。相同 Skill/Talent 可以由不同 model、container
或 credential scope 执行；同一 runtime 也可以承载多个能力包。组织层需要把二者组合成一次有界 assignment，
而不是让 Agent 对话维护“谁正在做什么”：

```text
portable capability artifact + version
+ runtime / container / credential identity
→ assigned worker instance
→ DAG task state and lease
→ result / cost / evidence
```

Scheduler 而非自然语言共识应拥有 acyclicity、dependency completion、one-task lease、idempotent dispatch、
bounded review、cancel cascade 与 crash recovery。OMC 的作者系统支持这种 typed orchestration 能承载异构
backend，却没有 component ablation、长期 self-evolution 或广泛 domain evidence；company metaphor 只是类比。
简单请求应回落 single Agent，自声明 capability 还需独立验证以防 supply-chain 与 benchmark gaming。

**true H2 Review notes本人拟注（放原首注前，保旧注）：**

- `SF-2026-ARXIV-2610-31985` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1 PDF](https://arxiv.org/pdf/2610.31985v1)§2–4/5.1及5.3.1–2必要，拟2+2+2=6。仅合法owner写权/本次task scope与受益人review分责；保脚本review/单向依赖、favor与harm分母不同、实际edit非口头endorsement、own-task提示非hardgate/损requester与soundguard未实验，不采普遍发生率或全防御。HTML404已真实请求，未核全部附件/实现/复现或PDF曲线像素；原三件PRE/SAVE/selfread/solePOST仅本日实际后到，不预签。


### 18.7 32024 首次必要/拟分与停止

**BARC-Bench: Benign Asks, Risky Consequences**，[2610.32024v1 HTML](https://arxiv.org/html/2610.32024v1)。拟2+2+2=6；SOURCE Oct26准入/公开日复用。实际§3–4/Eq1、§5.1关键protocol/结果、§5.3诊断口径与§6限制已读；不扩Appendix全部生成管线。110任务/9模拟工作区，human seed专选GPT5.6Sol三run中至少两次unsafe再扩写，故不是自然请求抽样。四配置同OpenCode/AgentEnv但defaultthinking不等compute匹配。Taskrubric可来自显式记录、跨记录隐含边界及社交规范；不能将用户善意当安全授权或把规范rubric当客观truth。

每task五attempt，safe completion/未先unsafe的deferral/任何一次unsafe三态；unsafe优先于后续完成或deferral。Eq1 safety pass^5是五次无违规的task比例，含deferral，不是完成率/单次违规概率；pass@5只要任一安全，甚至会换模型次序。§5.3按每failedtask第一条unsafe trajectory分一种pattern、全failedtask作分母，不能拿它作全轨迹发生率/因果retrieval瓶颈。Judge GPT5.6Sol接trace/artifacts/finalstate；300 trajectories/30tasks/2models三人有限校准，后整合分歧反馈，不是独立全量金标。§6明确US研究/工程师norm、single-turndelegation及通常单hazard，safe completion更粗且较少人审，未测用户澄清答复后能力。采用只限protocol/边界分账，不采用普适模型排行/生产harm或现成防护。

### 18.8 32024 actualowner与整体三件PRE

`PLATFORM-EVALUATION-SYSTEM` / Ch66；已读Policy/Outcome分层及2610.27548权限vs伤害原论证L173–187、ReviewUnit/cleantwin L5436–5443、完整DepthRepeatedInference L5465–5474及Ch65/67交接（未变上下文复用）。原一般重复压测/相关性/权限与成功具体NC；真实窄差额为欠明确benign边界、三态与all-safe不等safe completion。拟2602.11786成本段后/2510.03992证书段前，单段承接原纵向评价，不另建安全手册，待reader/PRE，未SAVE。

**完整前肩，保持不改：**

加速重复采样会增加调用成本，还可能因共享 cache、provider drift、judge 误差或近重复 prompt 而破坏独立假设。因此它是对 breadth benchmark 的补充，不是取代；预算不足时应保留高风险 slice 的最低采样深度并将未见失败标为上界未决。公开实验只支持披露模型、AIR-BENCH 派生 prompts 与 decoding 配置，不给出生产故障频率。<!-- source-family:SF-2026-ARXIV-2602-11786 -->

**拟完整段：**

纵向安全测试也不能只取恶意请求：善意但欠明确的任务，可能要求模型从工作区记录、记录间冲突或隐含社交规范推断内容/受众边界。应冻结这些rubric来源，并将每次尝试分成安全完成、未先越界而暂缓澄清、以及至少一次越界；后续完成或道歉不抹除先前动作。[BARC-Bench的受限模拟测量](https://arxiv.org/html/2610.32024v1)把同任务五次均无违规作为all-safe，但其中可含未完成的deferral，不能替代safe-completion、单次违规概率或真实风险；改成五次中任一次安全还会改变排序。应把安全一致性与用户目标交付分别报告，再以trace定位证据未取回、边界未推断或已取回却未应用，不能默认所有错误都可由扩大retrieval解决。Rubric仍编码有限审核者的规范，不是客观全局安全真值；种子按易诱发违规筛选、模拟环境和单轮委派也不估生产发生率或多轮澄清能力。环境/任务构造、全部重复执行与judge/人审均付费；规范有争议或当前权限不清时保留Unknown、澄清和原effect gate，而不是让一次完成或一个all-safe高分批准自治。
<!-- source-family:SF-2026-ARXIV-2610-32024 -->

**完整后肩，保持不改：**

随机红队还须先声明证书针对哪一个攻击人口，而不能把统计下界直接升格为最坏安全保证。固定攻击生成过程下的成功率为p_D，许可攻击集合中的最坏成功率为p_*；即使L是p_D的有效置信下界，p_*≤p_D也不推出L≤p_*，未抽样到的攻击仍可能使p_*=0。[一份受限工具选择审查](https://arxiv.org/html/2510.03992v1)还提醒，低下界本身不证明真实成功率低于某阈值；成功/失败计数、区间尾概率和全成功/全失败边界必须先与所估事件一致，不能由证书名称补齐。若一个trial要求整条R轮均成功，R增加也增加失败机会，不能单由存活率下降归因攻击适应；每个trial的检索池、反馈与攻击状态须按协议重置，另验等机会对照及多seed/多配置推断。应保存完整trial事件、计数、生成分布和许可威胁集，分别验候选暴露、选择正确与真实执行权限，全部改写、检索、selector/judge、重试和回归均计费；人口覆盖、计数方向或独立性未闭时，只报告所测过程的经验结果与未决，不授worst-case证书，保固定预算红队、独立权限门和人工升级。<!-- source-family:SF-2025-ARXIV-2510-03992 -->

**true H2 Review notes本人拟注（放原首注前，保旧注）：**

- `SF-2026-ARXIV-2610-32024` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32024v1)§3–4/Eq1/§5.1及§5.3/6必要，拟2+2+2=6。仅benign欠规范任务的边界rubric/三态与重复all-safe联合验收；保deferral非完成/先unsafe不能后洗、seed难例选择、judge有限人审/规范非客观真值和single-delegation，不采真实单次risk或更大retrieval万能。未核全附件/实现或执行复现；原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。


### 18.9 32053 首次必要/拟分与停止

**Are LLM-Generated Formal Specifications Faithful to Their Requirements? A Study on Bimodal Formal Specification Generation**，[2610.32053v1 HTML](https://arxiv.org/html/2610.32053v1)。拟2+2+2=6；req+unknown-correctness-code输入下，spec可能weak或跟错implementation，proof通过不等需求忠实，作为形式评价的设计反证深入受影响域；SOURCE Oct26日期/准入复用。页面JACM/2018/DOI占位属模板，不当正式发表或另一个公开事件。

实际读§3.1–3.3.2/Eq1–5/T2、§4.1与4.3关键分类/校准/反侧、§5；RULER仅§3.3.3和§4.4已返回的关键反退结论，不扩全方法/HoarePrompt对比队列。500req/1403短C程序，最多每题1correct/2wrong-answer，C99过滤/I-O静态与gpt-mini归一后仅已有tests核原输出，未证明语义全等；不含timeout/runtime错人口。Spec应表达R，code仅proof-relevantcontext，formal Verify(I,S)与Beh(S)=Beh(R)不同。

FramaC32 kernel syntax/WP+AltErgo/Z3，30s全POdischarge才pass，error/timeout都记fail；错误I上的fail可能忠实，也可能规范错误/过强/不可判，不自动成功。E-ACSL最多40原tests优先原I错例，A/B/C/D区分执行对错与spec接受/abort，E timeout；不能执行仍留validrate分母、缺分母归Other，阈值由每模型50项人审校准。Correct/Wrong/Weak/Misled只是有限runtime代理，含Other kappa约0.51–0.57，剔Other后较高不证明全部标签精确或需求全集忠实；本次不采用表Ver列口径混用的精确失败百分比/模型排序。迭代refine仍可向错实现移动，GPT5.5存在反退，不把prompt流程写成现成修复。Req细节/短contest程序与无thinking固定配置限制工业外推，未见多训练/生成重复CI；预处理、spec生成、solver/runtimechecks/人审和全部repair皆费，不授形式方法无效、通用生成器排名/净成本或可靠自治。已足支持反证窄链，停止不补全部prompt/无关表/外部实现。

### 18.10 32053 actualowner具体已有覆盖（不写Books，待唯一reader核）

实际owner `PLATFORM-EVALUATION-SYSTEM` / Ch66。已完整读L225原NL2VC段与L227 Verus-SpecGym段，及L1047–1052语义盲回译/独立需求核对论证；邻Ch65/67交接未变复用。不是只见general压缩或“形式验证有限”便NC，具体承载逐项为：

- 原L225明确verifier接受只证当前spec、原intent/规范前置条件/proof/独立执行tests四身份、weakpostcondition与禁止削弱spec自签，覆盖本篇unknown-code下weak/misled通过的采用命题。
- 原L227把valid/invalid input与correct/wrong output四反例分账，proof不能排规范过强/过弱、转换执行未证等价仍Unknown/有限tests不证全需求，覆盖本篇E-ACSL分类只是局部代理、fail不自动忠实及manual语义核对边界。
- 原L1047–1052分需求独立提取与代码盲回译，表示一致不等执行语义/独立正确证明，覆盖不让code实现反向定义意图这一分工；本篇没有新增本次拟采用的可靠修复/验证协议足以替换它。

本篇C/ACSL/FramaC特定观察、规模扩大/校准分数与RULER局部反退可在Report作上下文/反证支持，未形成现正文未承载的长期机制差额；因此拟“已有覆盖”，具体链接[Ch66现有规范忠实论证](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，不追加摘要/marker/本人注或伪造实现验收。保持材料贡献准入和6分不因NC降分，最终需sole reader确认此必要/actualNC。

### 18.11 本批当前实际停点

31846/31918/31985/32024首次必要与实际owner最小三件PRE均已准备，root各精确位确认无冲突，待sole reader；32053必要与actualNC待sole reader。五项均未SAVE/未预签I或NC通过，不扩来源/其余附件。前批§17五项R61–65已实际闭合不重复。

### 18.12 31846 R73后三件真实SAVE/完整自读待POST

reader R73实际核31846必要/6分、actual Ch77具体差额与§18.2原三件整体PRE通过，作者按root窄授apply_patch仅保存原单段/marker/本人注。正文L833/marker834/注2017；完整新增、两完整肩、本人注及旧Arendt首注逐字读回/匹配，marker1，限定diffcheck过。仅剥本三件恢复fresh baseline `9dd2c59431db42297692206fc208bb0839be967e290647ac0fd28b3dfd1cf936`，未覆盖旧2025/其他窄位。现交唯一actualPOST，不预签I；其余四项仍普通复核待办，不重Methods。


### 18.13 31918 R74后三件真实SAVE/完整自读待POST

reader R74核31918必要/6分、actual Ch29具体差额与§18.4原三件整体PRE通过。作者按root已授只apply_patch存原单段/独立marker/本人注：正文L601/marker602/注1608；完整新增/两完整肩/本人注及原32770首注逐字读回一致，marker1、限定diffcheck过。只剥本三件恢复fresh baseline `8097cf247b4c6847a092777579d635032902ca1d1a4bbc697a49f89116e84bd0`，保root/B/2025其他已成位。现交sole actualPOST，不预签I；31846已存待POST，其余三项仍未PRE，不重必要。

### 18.14 R75/76后三件真实SAVE；R77具体NC行政同步

reader R75已核31846实际POST6/I通过、精确位释放，不重审。31985必要/6分与§18.6整体原三件PRE R75通过、32024必要/6分与§18.8整体原三件PRE R76通过，作者依root精确位授权只apply_patch保存两章各原单段/独立marker/本人注。31985正文Ch82 L725/marker726/注1339；32024正文Ch66 L5471/marker5472/注5855。两项完整新增/完整两肩/本人注和旧首注分别实际读回且逐字同原稿，marker各1、限定diffcheck过。只剥各自三件分别恢复fresh baseline `359e4927059baa5210cf95240087257a1d17cbce037b193c57618a5fca8e8c2c`与`f0a1c496ad8cf30d9ed6fc378124826c6e6068607c22324bc8bf0f06ae56ea42`，保护前批及root/B/2025已成改动。现交sole actualPOST，未预签两项I。

另reader R77实际独核32053必要6及§18.10 Ch66具体已有覆盖通过，正式NC生效；未增Books段/marker/本人注，无待POST，不重必要。31918已存待POST；31846已正式I6，不把批内等待写成受阻或整日完成。

### 18.15 R79/80后本批五项闭合（仅行政同步）

唯一reader R79/80已实际核31918/31985/32024各sole actualPOST6/I通过、窄位释放；与既成31846 R75 I6、32053 R77 NC6合成本批4I/1NC，五项均2+2+2=6，不重Methods/原件/PRE/POST。四实际I正文/marker/本人注：31846 `AGENT-MEMORY` Ch77 L833/834/2017；31918 `TRAIN-SFT` Ch29 L601/602/1608；31985 `AGENT-MULTI-AGENT` Ch82 L725/726/1339；32024 `PLATFORM-EVALUATION-SYSTEM` Ch66 L5471/5472/5855。32053具体NC位置为同Ch66规范忠实L225/227及盲回译L1047–1052，无新增段/marker/注。本批精确事件均Oct26 exact-v1，不扩发现/其他日期/Report/State；未执行实现/训练/攻击/模型复现。已分配本批范围无剩余可执行工作，不授全日完成；若后续有新委派，仅复用有效层从新具名任务继续。


## 19. 代理追加五项（32129/32318/32285/32322/32336）：先评分后确定必要投入

root明确新分工；已完整重读当前AGENTS/研究合同（尤其§4/5）及适用Daily上下文，并复用SOURCE已成题摘/Oct26公开日/准入/去重。为准确限定新增评分，本轮仅重新打开五个官方abs完整题摘与唯一v1身份（均未见撤回提示），未先追Methods/owner。提交Oct23不替代SOURCE公告日，五候选仍全部保留，不按分数删除或扩池。

### 19.1 分数与投入决定（Methods前）

| 身份与精确题名 | 实际新增、评分理由 | 拟分及本次最低投入 |
| --- | --- | --- |
| [2610.32129v1](https://arxiv.org/abs/2610.32129v1) — **Shorter Is Not Cheaper: A Controlled Comparison of Declarative Animation Specifications and Free-Form Code for LLM-Generated Explanations** | 新增是同请求/同模型、预冻结分析的declarative-vs自由code反侧：短answer未必少reasoning/快、formatvalidity与semanticcheck可反退。D2为重要格式选择边界；R1只给生成解释这一局部负载，不借用全平台计费/编译链；U2为可复用的输出格式与总生成成本分账，不把“成本要全计”成熟原则加分。 | **2+1+2=5**，标准；因明确反驳格式天然更廉价可靠这一设计假设，深入受影响的实际对照/成本与validity协议，不扩全领域表/用户体验。 |
| [2610.32318v1](https://arxiv.org/abs/2610.32318v1) — **System One models Are Not Better Rerankers** | 新增是同backbone decision-vs-reranker训练对照与question-sensitive校准不继承ranking/阈值保留质量。D2为从decision校准外推ranking的边界修正；R1仅reranker组件，不因可连到RAG/全平台给2；U2为可复用的训练目标与ranking/calibration分验。 | **2+1+2=5**，标准；读足同骨干训练/候选人口/阈值对照及27B tie、措辞反侧，不追所有集合结果或产品发布历史。 |
| [2610.32285v1](https://arxiv.org/abs/2610.32285v1) — **Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution** | 新增是native harness下任务成败与harness机制义务分层、context/harness/environment三来源证据及run级机制链，观察到task成功但harness失败。D2为具体评价机制/归因接口；R2因实际跨agent/harness/环境证据边界，不把七component名称自动算多生命周期3；U2可复用的分层验收与取证资格。 | **2+2+2=6**，标准；读足two-layer/TT/MEA/FA拟采用机制及关键groundtruth/归因限制，不遍95任务与全实现。 |
| [2610.32322v1](https://arxiv.org/abs/2610.32322v1) — **Beyond Gain: Measuring Skill Internalization for Agent Skill Retirement** | 新增为gain≈0的internalized/uncovered不可辨，另以unaided与其他model确实受益作probe资格；不是把一般“删除要回归”借作贡献。D2为retirement判据的重要辨识边界；R1仅permodel skillretirement这一局部registry策略，跨四model不自动R2；U2可复用的probe资格/consumer维度。 | **2+1+2=5**，标准；读清probe构造/资格与被删uncovered反侧/retirement评价，不因能接Books或有删除字样默认安全深入；若实际冲突只加深相应域。 |
| [2610.32336v1](https://arxiv.org/abs/2610.32336v1) — **SkillRep: Characterizing and Understanding the Representation Design Space of Agent Skill Retrieval** | 新增为同retriever五representation选择的交互、fine-tune反转training-free模块排序/重叠及三个gap诊断的受测解释。D2为模块组合选择/失效边界；R1仅retrieval表示组件，111k规模不自动跨系统2；U2可复用的组合条件，不从成熟模块本身/单MRR涨幅取分。 | **2+1+2=5**，标准；读足模块交互/训练隔离与三个proxy适用性，收益/代价和直接反侧，不全量组合/数据实例。 |

以上是新增命题在现有证据下的正式拟分，不是按预期Books处置倒推。没有为了显示差异强造0–4关闭项，也不因五项已P就默认6；四项R1与一项R2来自各自新增实际到达的系统边界，后续只有具体新证据改变命题才解释调分。当前Methods尚未开始，五项均普通必要待办，独立reader可校准本评分与具体投入；不预签证据/Books。


### 19.2 32129 必要完成（5分，拟采用命题有界）

R81已实际独核§19.1评分/投入校准通过，既成AB/date复用。[exact-v1 HTML](https://arxiv.org/html/2610.32129v1)实际读§3 observation contract、§4同task/prompt/isolation/checker/analysis、§5.1–5.4总费/repair不对称纠正与semantic反侧、§6 followup thinking条件及§7限制；未读全任务附图或外部实现。身份/题名见19.1，2+1+2=5保持；设计反证仅深入此比较受影响内容，不因Booksgap加分。

同20任务/两condition各3repeat，用seek/getState/setParam统一状态checker；只invalid回一次repair并只给runtime/contract错误，不给semantictests。Checker对40同family agentreference与mutation核验，但只测暴露state，不点可见controls/不证drawing一致、视觉/教学效用。原Spec swallowing runtime errors导致五项没获repair，primary保留，corrected harness重评并报告deviation；Qwen followup从头用corrected harness。冻结为内部hash非外部注册，analysis script未hash。统计按20task配对、跨重复median/mean、exactWilcoxon/任务bootstrap+Holm，不把600jobs当600独立题。

关键支持为short answer与总output/latency、含repair费用分开；Claude只有最大模型firstattempt总token显著少，含repair价格估计三者均更贵，其他family不必同一机制：Qwen thinking shift未复现，reasoning本来主导总output。Qwen为Q4_K_M/14B、Ollama0.34.3/单16GB GPU、32kctx/24,576cap，串行/已加载，ClaudeCLI低effort/4jobs并发、隔离process无tools；不跨family合latency/price或当同硬件causal。无thinking快但Spec语义极差，比较大多validHTML与invalidSpec，不是等质量净速。Claude postrepair5–10点semantic差异不显著不等同，Qwen明显反退；不采所有声明式format都差/缩短必不省。两分支不同incontext熟悉度、范例controls、DSL表达能力，不能归因唯一planning机制；熟悉度vs编码规划仍未分离。格式文档/固定runtime、prompt处理、全部reasoning/answer、validation/repair与renderer费用进入取舍，实验未streaming/cachedDSL/finetune或完整lifecost。已足拟采用的格式选择—全生成/有效质量反侧，停止。


### 19.3 32129 actualowner与整体三件PRE

`PLATFORM-COST` / Ch70。已读实际正文资源时间/训练与推理成本L1–129、相邻Ch69/71开篇及知识树交接、Ch70收束。原文state-dependent work、Prefill与length/SLO、image输入转换和提醒简短的quality/cap分账实际已有，具体NC不重复。缺的是输出格式改变reasoning与生成/repair全过程、短artifact但invalid和等质量比较的局部反侧；该差额不是宣称一般成本原则由本篇发明。拟仅在下列两完整段之间插一个自然段，不产品手册，不预签I；root窄位协调/reader必要及整体PRE待到。

**完整前肩，保持不改：**

只看 output token 会忽略 Prefill；只看 request 会忽略长度。应同时保留 prompt/output lengths、cache hit、model/quantization、hardware、concurrency 与 SLO。

**拟完整段：**

输出表示也会改变生成过程本身：把自由代码换成由固定runtime解释的短声明，省掉的是可见artifact，不保证省掉生成它之前的reasoning。应在相同任务与可观察语义条件下，分别核answer/reasoning/总token、首可见回答与完整生成时间，以及invalid后的全部validation/repair；可运行也不等内容正确。[受限动画格式对照](https://arxiv.org/html/2610.32129v1)中，部分模型为短声明多作推理，另一模型没有复现这种shift但推理原已占主导；关闭thinking虽快，质量却退步，不能把更短的invalid产物当等质量省费。陌生DSL、范例和表达能力仍是共同变化，未隔离唯一原因，也未验证训练熟悉后、streaming或缓存路径。文档/固定runtime维护、prompt处理、推理、回答、渲染和失败重试都进入成本；格式、质量或净收益不合时，保留熟悉的自由代码、已验runtime接口和原生成配置，不由短artifact、schema或一次valid签发更低成本与可靠性。
<!-- source-family:SF-2026-ARXIV-2610-32129 -->

**完整后肩，保持不改：**

[固定配置的局部decode能耗模型](https://arxiv.org/html/2610.28576v1#S3)还需把共享权重与私有历史分开计量：在dense、full-history前提下，令`T`为副本实际输出数、`S`为迭代数，则有效batch为`T/S`，而不是初始并发数；每输出的逻辑weight需求为`M_w/(T/S)`，KV需求为`K_KV×(按输出token加权的平均历史长度+1)`，其中`M_w`为权重逻辑bytes、`K_KV`为每历史token的KV逻辑bytes。两者与实际decode秒数/`T`可共同拟合GPU-board的局部能量响应，但logical bytes不是HBM实测量，拟合时间系数也不是独立测得的idle power。请求逐步离开时，应更新实际batch与token权重历史；跨model、precision、graph policy或topology要重验系数，MoE也不能把activated参数直接除以全batch。该模型不包含prefill、host或设施，采用已观察时间的局部预测不能冒充未执行配置的能耗、全服务节能或SLO保证；校准失效时仍回到同步实测与较粗资源分账。<!-- source-family:SF-2026-ARXIV-2610-28576 -->

**true H2 Review notes本人拟注（放旧首注前，保旧注）：**

- `SF-2026-ARXIV-2610-32129` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32129v1)§3/4/5.1–5.4/6/7必要，R81前评分2+1+2=5。仅format对完整generation/repair成本与有效质量的条件反证；保内部冻结/20task配对、runtime swallowing纠正、Qwen shift未复现与无thinking低质量、同family参考/DSL熟悉度混杂，不采所有格式无效/净费SLO或视觉教学效用。未核全附件/外部实现或执行复现；必要/actualowner/原三件PRE/SAVE/selfread/solePOST仅本日实际后到，不预签。


### 19.4 32318 必要完成（5分）

[exact-v1 HTML](https://arxiv.org/html/2610.32318v1)，实际核心§3 isolation/joint定义、§4 backbone/自训对照/候选与calibration协议、§5关键比较及§6–7阈值/措辞/base-rate反侧已读，不采用所有collections/闭源系统榜单。2+1+2=5保持（R81校准），不是SystemOne名字或同骨干就证明objective唯一因果。

所有同BM25 top100，samebackbone有untuned chat/decision/reranker，但releasedtraining数据/objective各异：小KevLoRA pretrained与27B fullchat不同，RLCD未公开且不是复现；自训9/27B是一次rank32/100kMARCO/1positive15hardneg、InfoNCE+BCE，预定dev选点/去testdev重合，不匹配decision的全部训练费/seed。0.6–9B rerank在受测rank更强，27B tie且decisioncutoff可更有用，不能推全规模/全decision永不优。

排序nDCG与概率用途独立：TREC judgedpairs/grade≥2、ECE15bins/Brier；固定.5保留集F1把unjudged当不相关，posthoc最优threshold仅regret参照非线上oracle。措辞从answerquery变looserrelevant会改变校准，untuned亦受益；decision校准不足补更差rank。27B rank近似时calibration反有用；MARCOdev拟合Platt到TREC不同relevancebaserate使cutoff反退，不能写后处理总能修。只TREC/Singlerelevancegrade/.5与两question，域/labels/base-rate均是资格；joint上下文也非所有size增益。Pairedquery t+Holm不是训练seed不确定性，bestmean decisionmode选择非固定全系统公平预算。全部candidate读取/scoring/训练/校准及下游retained passages费未完整披露，不能由概率输出少tokens授更廉价生产能力。已足rank/calibration分验及prompt/label资格的窄采用，停，不追外部仓库/全表。


### 19.5 32318 actualowner与整体三件PRE

`AGENT-RAG` / Ch76。实际读原Reranking&ContextPacking L803–832相关完整论证、上游候选消费/utility标签L163–178、联合阈值/置信L1083–1101，以及Ch75/77开篇与Ch76知识树交接（其余未变交接复用）。现正文已承载score非probability/标签依赖/不同candidate消费和threshold校准，具体NC；真实差额是rank次序与absolute calibrated cutoff各消费不同资格，decision训练不自动继承rank、question/labels/base-rate可改校准而未改排序。只在该节开头单段后增自然段；root窄位已发，待reader必要/actualowner/整体PRE，不提前SAVE。

**完整前肩，保持不改：**

Retriever 优化高 recall，cross-encoder/LLM reranker 可用更强交互提高 precision，但增加 latency/cost。

**拟完整段：**

选择概率式重排器时，还要把“候选次序是否好”与“分数能否按绝对阈值消费”分开。相同backbone与候选池可隔离部分容量差异，却不消除训练数据、目标和prompt的差别；通用decision模型的校准能力不能直接继承为相关性排序优势。[受限同骨干对照](https://arxiv.org/html/2610.32318v1)中，较小模型的reranker训练保留了更好的排名与固定cutoff集合，即使decision分数在匹配问题措辞下更校准；较大模型排名近似时，校准则可改善保留集，不能把二者规定为统一赢家。应绑定relevance定义、question、候选/已判标签人口与base rate，分别验nDCG、calibration、截断后的precision/recall及reader支持；换一句问题或跨base-rate迁移校准可能改变绝对分数而几乎不改排序。事后最优threshold只是诊断参照，未标注当负例也限制截断结论。训练/全部候选评分、阈值校准和下游阅读均付费；目标、标签或迁移不合时，保留已验reranker、固定预算top-k与重新校准，不由概率接口或低ECE批准更好证据与更低全链成本。
<!-- source-family:SF-2026-ARXIV-2610-32318 -->

**完整后肩，保持不改：**

重排也可以保持语言模型权重不变，直接选择内部attention的读出通路，而不生成排序ID或先训练新scoring head：在带gold与hard negatives的离线查询上，按gold文档相对负例的attention softmax份额为各head打分，再固定少数高分head用于query到文档的相关性聚合。[受限对比head分支](https://arxiv.org/html/2510.02219v1#S4)区分了“对gold看得多”与“能排开不相关候选”；copy/NIAH任务选出的head不自动取得relevance排序资格。权重无需追加训练不等无需标签或校准，线上还以真实query与content-free query的差作token读出。head集合、温度、gold/负例与位置人口、prompt和首阶段候选池因而共同定义重排资产，不由attention较大认证文档支持最终答案。

**true H2 Review notes本人拟注（放旧首注前，保旧注）：**

- `SF-2026-ARXIV-2610-32318` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32318v1)§3–4及§5/6/7关键对照必要，R81前评分2+1+2=5。仅ranking/absolute calibration/cutoff消费资格分验，保同骨干非同data/objective/总费、一次自训/27B tie且calibration有用、question与base-rate迁移、unjudged作负例/有限TREC，不采RLCD无效或全系统排行。未核全表/外部实现/训练复现；原三件PRE/SAVE/selfread/solePOST按本日实际后到，不预签。


### 19.6 32129 R83后三件真实SAVE/完整自读待POST

reader R83已核必要5/actual Ch70差额/§19.3原三件整体PRE通过，root窄授作者仅apply_patch存原单段+独立marker+本人注。正文L121/marker122/注426，完整新增/完整两肩/本人注及旧28576首注实读逐字同稿，marker1/限定diffcheck过。仅剥三件恢复fresh baseline `9581b58abf80487f5e4f3969183b395769b3bc8360212ea2df69c823f1ebf386`，保并发其他位；现交sole actualPOST，不预签I，不重必要。

### 19.7 32285 必要完成（6分）

[exact-v1 HTML](https://arxiv.org/html/2610.32285v1)，2+2+2=6保持R81校准。实际读§2.3/§3.1系统/观察边界、3.2.3 native-semantic对齐、3.3 TT/MEA与boundedpacket、3.4二层scoring/T4、3.5候选归因资格、§4关键selection/全grid/成本及§5.1–2关键二层反例。不把七维95任务自动Methods队列，不读全任务/附图/实现。

Runner归一native日志保raw/provenance，nativeID优先对call-result；无ID/ambiguous保unlinked，不按顺序猜。环境ledger/executionprobe证实际后果，native模型面证送到什么，provider仅成功完整structured tool声明而非全requestbody；criterion selector按冻结types/fields/关键词/数量构造有截断计数的packet，不替rawarchive。缺匹配当前实现赋0只表示未证满足，不直接证harnessdefect。Apparatus admission独立于两层score，但本次全grid所有finalized cells原值计入，并非以事后gate过滤后成绩。

二层先Agent后Harness、deterministic固定，semantic由固定deepseekflash判；T4 notexercised state2按Agent是否全过决定binary，故两层非独立，不能把Harness平均当纯机制故障率。rawHarnesszero F_H与扣bypass Z_H、confirmed D_H分层；实验聚合/激活仍取raw F_H，harness_caused标签只predeclared endpoints+condition激活，不是传播因果。仅人审复核端点、各自authority、时间顺序/intermediatedistortion/竞争解释才可升级L_val，未估全corpus selectorrecall/judgeagreement/linkprecision，不能把31.1%task成功且rawHarnesszero叫已确认缺陷被吸收。

4×9×95各1 selectedrun=3420含先前recovery replacement，无within-cell重复，task修订/调度/recovery限制harness因果。Budget task-specific120–5400s/轮与toolceilings，judge output4096/8192/32000不一；不称统一吞吐/等judgebudget。macro每run与micro每criterion权重不同，全过与均分不同；计费统一价格估算，仅validusage，排judge/丢弃runs/storage/toolfee，非实际账单/全life费用。已足拟采用：native obligation与task outcome双轴+取证资格/候选非因果；停，不采系统排名或全安全/可复现已执行保证。


### 19.8 32285 actualowner与整体三件PRE

`PLATFORM-EVALUATION-SYSTEM` / Ch66。实际读原五层成功/授权分账L173–187、RuntimeCoverage首两完整段/邻接、Harness fragility L5249–5264、MeasurementIdentity/JudgeAgreement L5655起完整一般论证；Ch65/67交接未变复用。旧论证已承载subject=model+runtime+env、trace不等完整语义、observation/authority与同名metric问题，具体NC不重写。真实差额为native obligation/outcome二张命名表、criterionfail/confirmeddefect/validatedpropagation资格，以及notexercised按outcome解分导致非独立；不是新增一份日志术语表。拟RuntimeCoverage两段后、staleissue原binding前一段。root窄位协调/reader必要及整体PRE待到，未SAVE。

**完整前肩，保持不改：**

为降低反复调参污染，holdout 还应冻结，场景与 runtime coverage 一起版本化，并通过多次运行区分随机波动。Trace coverage 改善可诊断性，却不等于 evaluator 覆盖全部语义错误；场景代表性、隐藏副作用和 judge 漏检仍需独立审计。

**拟完整段：**

评native harness还应将任务交付与机制义务保存为两张独立命名的score sheet：最终artifact成功，可能只是模型绕过了丢失的状态或失真的结果通道；任务失败也不自动证明harness坏。先确认测量器/归档资格，再按criterion选择模型面、native记录和外部环境证据，并保留原archive及packet截断范围。[TraceTrial-Bench的受限协议](https://arxiv.org/html/2610.32285v1)明确区分未证满足的criterion零分、经对应authority复核的缺陷，以及端点/中间失真/时序和替代解释都核过的传播；自动harness_caused标签只表示预定候选链激活。两张表也不必统计独立：该实现对未触发义务按Agent结果解binary，空selector亦赋零，故raw失败交集不能当确认故障率。Native接口归一不能增强原模型可见证据或偷偷补能力，无法保存等价语义的组合应另标不可比；归档、probes、全部selector/judge与必要人审都有费。当前selected-run矩阵含恢复替换且未测全量judge/link精度，不认证跨harness因果排名；证据、适用性或取证通道不足时，保留原verdict、Unknown和定点人审，而不由任务完成或可追溯标签签可靠性。
<!-- source-family:SF-2026-ARXIV-2610-32285 -->

**完整后肩（原binding与首完整段），保持不改：**

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07769:start -->
只用“给 issue 产出 patch”的任务评估 Coding Agent，会把行动本身训练成隐含成功条件；真实队列还包含已经修复的 stale issue，此时正确结果是复现后保持 no-op。EvalSpec 应把 needs-action、already-fixed 与 partially-fixed 组成配对切片，分别记录 reproduction evidence、empty/non-empty patch、test outcome、abstention reason 和 technical-debt side effect。

**true H2 Review notes本人拟注（放旧首注前，保旧注）：**

- `SF-2026-ARXIV-2610-32285` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32285v1)§2.3/3.1/3.2.3/3.3–3.5/T4/§4关键selection及5.1–2必要，R81前评分2+2+2=6。仅native义务/outcome双轴与criterion/defect/传播资格；保notexercised outcomeconditioned、空selector零非缺陷、raw/bypass/confirmed分层、自动link非causal、全gridselected含替换/预算不一/无corpusjudg精度和全费，不采系统排名/完备取证或安全。未核全部95任务/全附图/实现或运行复现；原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。


### 19.9 R86后32129闭合；32318 R85后三件真实SAVE/自读待POST

reader R86实际POST已通过32129，正式5分I/Ch70位释放，不第三必要/POST。32318 R85必要5/actual Ch76差额及§19.5原三件PRE通过，作者按root窄授仅apply_patch保存原单段/marker/本人注。正文L807/marker808/注1786，完整新增/完整两肩/本人注与旧DecEx首注逐字读回一致，marker1/限定diffcheck过；剥本三件恢复fresh baseline `fd97a7d54586856682dc0357f56cd7bf331fc705a3e4fd1f321670f3748ab0a2`，保护并发/历史与其他位。现交sole actualPOST，不预签32318 I；32285原三件PRE待到，32322/32336尚未必要。


### 19.10 32318闭合及32285 R88后三件真实SAVE/完整自读

32318 sole reader R88实际POST已过，正式5分I/Ch76位释放；32129此前R86已闭。32285 R88必要6/actual Ch66差额及§19.8原三件整体PRE通过，root随后确认RuntimeCoverage两段后→2605.07769:start前精确位无冲突。作者仅原单段/marker/本人注apply_patch真实SAVE；正文L4647/marker4648/本人注5861，完整新增/完整两肩/本人注及旧32024首注逐字读回一致，marker1，限定diffcheck通过；剥本三件恢复fresh baseline `14eb534d9337d0ceef93ef157dcbf544b59674f4a3a287744fba29c485f7d04e`。保护并发/历史/旧注，不改其他位；现交sole actualPOST，尚不预签32285 I。32322已有限必要阅读，下一保存其实际范围/owner；32336尚未必要。

### 19.11 32322 必要完成（5分，保直接反侧）

复用本日AB/date/准入，精确[2610.32322v1 HTML](https://arxiv.org/html/2610.32322v1)，已实际有限读§2与§3.2–5核心probe构造、Alg1、cross-fit和SkillsBench运行退役；支持与直接反侧足即停，不追加全证明/全表/全附件/代码。方法以unaided U与aided A区分gain≈0的internalized（两边高）/uncovered（两边低），positive-witness要求其他模型在同探针因Skill受益；缺见证经再生仍无效便保留无verdict，并非认证可安全删除。结论是permodel soft-retire，不能继承另一个模型标签。任务生成与受测目标分离，但目标unaided>半即重生的difficulty gate偏向难例；去generic rubric条目有限人工120项precision.85/recall.81，不认证所有条款必要。

关键反侧：single-task state/rule共用U有循环，124 skills/29 uncovered的两任务cross-fit有限支持band较level少误删；给band也加aidedlevel门槛同样避免低低，故不采一切gain策略无效。重复run相关.90而parallel-form仅.41，更多同task rollout不能替代新任务。self-judge虽有限替换相关.89，第三family99临界例仍有9–15%不支持full marks，可抬U约.1；不把unaidedlevel当无偏真值。SkillsBench从200→182scorable→92无answerleak→59 witness-admitted，仅81任务；至少5删除run/9 full，whole81含untouched零稀释、level实际触17任务，整体−.2[−2.7,2.4]可在touched容许约11点损害。无规则检出成本/成功差异不等于等价、非劣或优于其他policy；deleteall损19点只说明基准会响应删除。保难度选择/有限family/同源任务与judge；不读无关更广库表或称生产保证。

### 19.12 32322 actualowner与整体三件PRE

实际owner `AGENT-PLATFORM`，Ch84 Skill Lifecycle。已完整读dual-gate、SkillApt同task WITH/WITHOUT admission、CoCA组合边际、2609.29543 utility/permission双证书与library维护论证，复用未变Ch83协议→平台交接。具体NC：runtime相关≠效用、版本冻结/回归、权限证书独立均已有；差额不是一般删后回归，而是gain零不能辨低低、高unaided之前的positive-witness探针资格及模型专属可逆退役。Ch80 componentcredit/heldout一般原则不承载此辨识链。root已确认下列CoCA完整段后→两证书完整段前精确窄位无冲突；不锁全章，仅拟一段/独立marker/本人注。以下完整两肩与原稿交唯一reader，未PRE不SAVE。

完整前肩：

多个 Skill/能力一起激活时，单项 WITH/WITHOUT 收益不能简单相加：一个能力可能补足另一项的前置条件，也可能重复占用上下文或互相干扰。集合选择应把当前任务阶段、已有激活集合、权限与 token/延迟预算放进同一个 state，估计**条件边际收益**后再提交组合；能力调用仍受各自 runtime gate 约束。CoCA 用条件 teacher 比较和学生集合策略探索这一分支，作者多模态 Agent 基准仅支持所测组合与成本设置，不证明对未见能力目录或生产环境的最优分配。组合证据不足时，回退小型人工 allowlist 与逐项验证。<!-- source-family:SF-2026-ARXIV-2609-27869 -->

拟新增正文与独立marker：

不过，任务上一次 WITH/WITHOUT 的增益接近零，不能单独批准 Skill 退役：模型可能早已会做，也可能两边都不会。退役的 utility 证书应改问当前模型在多个新任务上，不给 Skill 时是否已稳定达到所需能力；还要确认这些探针确实需要该 Skill 的信息。[Beyond Gain的有限审计](https://arxiv.org/html/2610.32322v1)以其他模型在同一探针上确实因 Skill 受益作为资格见证；它只排除部分无效探针，不证明所有条款都必要，也不把其他模型的会做转移给当前模型。没有见证就保留且不给退役结论；WITH/WITHOUT 都低则标记能力或 Skill 待修，而不是因低 gain 删除。结论绑定 model revision、任务分布和库版本，宜先 soft-retire 并允许恢复。新的独立任务、成对执行与 judge 审计都有成本，重复同一任务不替代探针多样性；作者小规模运行退役实验未检出质量损失，但置信区间仍容许损害，自评 judge 与难度筛选也限制外推，不能签零损失或跨模型通用退役规则。
<!-- source-family:SF-2026-ARXIV-2610-32322 -->

完整后肩：

Skill 退役还要把“删后能完成授权任务”与“删后仍守住权限边界”做成两张独立证书。只在合法任务上测 utility，会把从未变化过的 principal、permission 或物理状态条件误认为冗余；应固定请求的 action/effect，仅翻转授权或状态 predicate，分别核查 proposal、sink decision 与真实 effect，才有依据在**所测状态和完整中介的 sink**内有条件批准退役。匹配反事实审计提高测试与环境建模成本；未测谓词、旁路或更长观察窗都不能由这张证书覆盖，前置条件无法完整枚举时应保留旧条款或在 effect-time 强制拒绝。作者 12 个受限 bundle、四种模型配置显示多数 procedure 可以大幅裁剪而仍通过授权任务，却暴露 protected effect；单条只读 camera 路径也不证明真实物理安全。<!-- source-family:SF-2026-ARXIV-2609-29543 -->

拟true-H2 `## Review notes`本人注（保旧首注）：

- `SF-2026-ARXIV-2610-32322` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32322v1)§2/3.2–5关键probe/Alg1/cross-fit与SkillsBench退役反侧必要，Methods前2+1+2=5。仅gain混淆、unaidedlevel与positive-witness资格/permodel soft-retire；保低低不是冗余、no-witness无verdict、judge/generator与难度门限偏差、parallelforms不稳、未检出损失非noninferiority，权限证书仍独立。未核全附录/实现或运行复现；原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。

### 19.13 32285闭合；32336必要完成（5分）

32285 reader R89真实actualPOST已通过，正式6分I/Ch66精确位释放，不第三必要/PRE/POST。32336复用既成AB/date/准入，只actual请求精确[2610.32336v1 HTML](https://arxiv.org/html/2610.32336v1)，有限读§3–4实现/评价条件、§5.2 alone-last关键对照、§6–7三个proxy与直接干预反侧、A训练隔离及B融合资格；足够即停，不读全C–F/全部组合或代码。五模块共享0.6B encoder；FT用38,308合成配对且训练看过部分被搜nongold库，test query/gold的cosine去近重不能等于完全inductive。UniPool上选w/u/alpha后跨pool保持；主机制分析限5400 SRA请求及UniPool，不把pool调参叫独立heldout结果。两个扩展各Qwen3.6-27B生成两文本；dense只body、lexical含name/description，不能把双路gain唯一归于数学fusion；onlineQE需LLM，DE/投影需离线构建/更新。未披露完整服务费用/SLO，不授更低净费。

关键控制为同encoder/pool各模块单加与从全组合去掉的残余：未训时projection较值钱、微调后QE较值钱；fouralone之和15.33/full13.15为受测重叠，而untuned16.56/17.30为互补，不推 universal law。文档侧扩展用全库平均pseudoquery也得1.67/其3.10，直接反驳所有收益来自skill特有语义。Gold删去QE缺失词损3.12，同IDF其他词损.08；gold edits是离线probe。Dilution=maxsection cosine−body cosine自带分数耦合；另以异skill/通用/自身重复padding、sectionretriever/BM25控制支持‘无关内容稀释单向量’，不把量当长度或线上可得gold；词通道也可挤掉dense已有正确top1，scorefusion保margin在所测池改善但不授概率校准。仅同任务检索指标，非实际Skill执行/平台安全。§7.4受测微调缩background与QE背景迁移支持重叠解释，仍不让三个弱相关proxy认证独立语义因果或完备分类。支持与直接反侧已足，停止额外表/附件。

### 19.14 32336 actualowner与整体三件PRE

实际owner `AGENT-RAG` Ch76‘检索表示决定可表达的匹配’。已完整读该节单/多向量成本、预算prefix、hybrid/PRF与dense迁移、训练/表示相关段，复用未变Ch75可见state→Ch76 evidence→Ch77 memory交接。具体NC：单向量局部信息折叠、hybrid/改写可退步、encoder/index联合版本已有；差额为同encoder/pool下alone-last残余及FT后模块排序反转，用background/unsaid/dilution的gold-dependent受控探针区分重复补偿，而非又贴一个retriever目录。root已确认首段2608.21494 marker后→多向量条数完整段前无冲突；以下原三件及两完整肩交sole reader，未PRE不SAVE。

完整前肩：

把一段内容压成单一向量很便于建立 ANN 索引，却会把多个局部语义关系折叠为一个相似度。token 级多向量匹配扩大了可表达的相关性类别，但代价是向量数量、候选生成、精排和跨设备数据移动同时上升。因而“召回质量更高”不能脱离表示与执行成本单独讨论：表示层先决定哪些证据关系能够被区分，系统层再决定这些关系能否在延迟和内存预算内被实现。
<!-- source-family: arxiv:2608.21494v1; semantic-body-binding: multivector-retrieval-expressivity-cost -->

拟新增正文与独立marker：

在增加表示容量前，还可先问检索管线的多个补偿模块是否在修同一种失真。固定请求、候选库与 encoder，既测每个模块独加的收益，也测其在完整组合中最后加入仍剩多少，才能区分互补与重复补偿。[SkillRep的有限对照](https://arxiv.org/html/2610.32336v1)显示，对比微调削弱共享背景后，背景投影的收益减小，而 query 扩展又开始修复请求侧背景，因而原来互补的模块会重叠；旧 encoder 上的模块排名不能直接继承。其诊断将竞争者共享背景、请求未说出的目标词汇，以及整篇单向量稀释局部信息分开：扩展补词、投影去背景与 lexical 通道保留词匹配，可能覆盖不同残差，但不是普适一一映射。需要 gold 的删词和填充实验只是离线机制探针，不能变成线上可用的真值或选模块 oracle；几何量与相关性本身也不证明充分相关。微调、离线扩展/重索引、在线 LLM 扩展及双路搜索都有费，移除在线扩展仍可能保留较好排序，却不代表所有基准等质量或净成本更低。组合与权重应随 encoder、语料和评分接口共同验收；迁移不稳或预算不足时，保留原表示与已验的小组合，继续以原文支持而非模块名批准下游回答。
<!-- source-family:SF-2026-ARXIV-2610-32336 -->

完整后肩：

多向量的条数也可以成为受训练的预算接口，而不只缩短每个向量的维度：在query与文档各自输入后追加learned tokens，以它们的表示做late interaction，再让若干嵌套条数前缀分别接受对比监督，才能在部署时选择较小的query/document向量集合。[一条受限前缀分支](https://arxiv.org/html/2509.18095v1#S3)支持这种表示与消费预算的交接，不表示任意旧多向量可直接截断，或更多向量对每个query都更好。两侧预算改变MaxSim的支持与求和尺度，分数阈值和融合也须重新验收；已存完整文档向量时可选较短前缀，若索引只保留短前缀，日后加长仍需额外副本或重编码、迁移索引，不能把无需重训写成无需重建。应共同保存encoder/adapter、读出token顺序、两侧条数与索引revision，并分别验收检索与最终原文支持。多预算训练、全部编码、向量驻留/换入、索引刷新和打分都计费，局部scoring延迟不代表全请求便宜；质量、索引支持或净预算不合时，保留已验单向量、固定预算的完整late interaction与lexical/hybrid，不由预算旋钮批准答案事实或生产SLO。

拟true-H2 `## Review notes`本人注（保旧首注）：

- `SF-2026-ARXIV-2610-32336` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32336v1)§3–4/§5.2/§6–7及A训练隔离、B融合反侧的必要，Methods前2+1+2=5。仅同encoder/pool的alone-last与三类残差诊断；保fine-tuned排序反转、gold删词/填充仅离线、dilution量有分数自耦、UniPool调权重/训练见nongold库非inductive、检索非execution与全费用未证，不采普适模块映射/生产SLO。未核全部附录/实现/运行复现；原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。

### 19.15 32322 R91后三件真实SAVE/完整自读

32322 R91必要5/实际Ch84差额与§19.12原三件整体PRE通过，root已确认CoCA后→原退役双证书前精确位；作者仅原单段/marker/本人注apply_patch SAVE。正文L1204/marker1205/本人注1250，实际完整新增、前后完整肩、本人注和旧31895首注读回逐字匹配，marker1；剥本三件恢复fresh baseline `4bbc9c28d7fa45887da1003bb0c5f55bae399111d5633861df34c8585998d3ff`，限定diffcheck无输出。保护并发、旧注及其他位。现在交sole actualPOST，不预签32322 I；32336必要/原三件整体PRE待reader，不扩附件。

### 19.16 32322闭合及32336 R93后三件真实SAVE/完整自读

32322 sole reader R93真实actualPOST已过，正式5分I/Ch84精确位释放。32336 R93必要5/实际Ch76差额及§19.14原三件整体PRE通过，root已确认2608.21494 marker后→多向量条数前精确位；作者仅原单段/marker/本人注apply_patch SAVE。正文L481/marker482/本人注1789，实际完整新增、前后完整肩、本人注与旧32318首注读回逐字匹配，marker1；剥本三件恢复fresh baseline `00d2d076be65da7a72ece1584345fffa5b50771867c3cba85d24c0b53d682948`，限定diffcheck通过。保护已有并发/旧注/其他位。现交sole actualPOST，不预签32336 I；本批不扩来源/附件或其他候选。

### 19.17 本批五项实际闭合与下一分工

sole reader R96实际POST已过32336，5分I/Ch76精确位释放。本五唯一家族均已按R81最低投入审阅、actualowner比较及逐项PRE/SAVE/完整自读/solePOST真实闭合：32129 5/I Ch70（R86）、32318 5/I Ch76（R88）、32285 6/I Ch66（R89）、32322 5/I Ch84（R93）、32336 5/I Ch76（R96）。一般原则具体NC保于各owner比较，最终最小差额才整合，不因有位或为分布造I/低分；日期仍Oct26唯一v1，未扩来源/附件/其他日期。root新授下一五32110/32305/32483/32608/32851；仅在本批POST齐后接Methods前评分，复用既成题摘/date/准入，不重AB/日期或宽列表。Report/State仍root独占，不冒本日全完成。

## 20. 代理下一五项：先评分，后最低必要投入

root在§19五项actualPOST全部闭合后新授32110/32305/32483/32608/32851。复用SOURCE既成完整题摘、Oct26日期/唯一精确v1与准入校准，不重新请求AB/date，不扩宽列表。本节只按原件已明确的实际新增命题定最低投入，不以Books是否已有主题/能否找到插入位、篇数或节省费用改分；正式题名在必要HTML身份核时原样记，不猜名。此时未读新五Methods、不预I/NC。

### 20.1 Methods前评分与最低投入

| 身份 | 本文新增与计分边界 | 分数/必要范围 |
| --- | --- | --- |
| [2610.32110v1](https://arxiv.org/abs/2610.32110v1) tool formatter | 正确tool计算仍可在rendering丢limit/cap/namespace，受控改render wording改变agent与verifier接受；不是借一般‘receipt非真值’原则。D2重要证据接口反证；R2实际跨tool计算/呈现与agent/validator消费，不由安全词加3；U2稳定的语义资格边界。 | **2+2+2=6**。标准并深入实际formatter变化/消费反侧受影响域，核payload固定、对照权限与评价；不遍全tool目录/攻击或生产测试。 |
| [2610.32305v1](https://arxiv.org/abs/2610.32305v1) workflow GO/NOGO | 同workflow位置GO/NOGO反事实分‘说出了诊断’与‘实际禁止后续计算’，不是又一个gate名称。D2执行约束的重要失效条件；R2实际跨模型诊断输出与workflow下游执行，不把多领域当3；U2可复用的state条件执行责任。 | **2+2+2=6**。标准，拟采用工业主域的gate/下游调用对照及直接限制；科学RNA/GWAS不扩AIforScience，不按全任务表读。 |
| [2610.32483v1](https://arxiv.org/abs/2610.32483v1) harness/model残差 | completion/task success/pairwise harness-model residual与failedtokens分账、排名按配对翻转；不借总成本常识或模型榜声望。D2联合测量和解释边界；R2真实跨model/harness配置与执行结果/预算；U2稳定的配对身份约束。 | **2+2+2=6**。标准，读实际矩阵/失败与预算分母、配对比较及残差解释的反侧，不遍全部模型轨迹或榜表。 |
| [2610.32608v1](https://arxiv.org/abs/2610.32608v1) scope metadata/router | truthscope过滤与estimatedscope路由在post-audit扰动分离，具体选择错可破坏理想filter收益。D2重要检索consumer资格；R1仅scope过滤/路由的局部检索组件，领域名/可连法律不升2；U2可复用的oracle-v-estimated输入边界。 | **2+1+2=5**。标准，核metadata来源、router扰动/诊断人口与检索对照、失配反侧，不授法律正确或heldout。 |
| [2610.32851v1](https://arxiv.org/abs/2610.32851v1) rule namespace | 同名跨service规则flat retrieval高相似误取，以producer/component/service命名结构先约束合法池；不是仅多metadata提高rank。D2检索适用域重要机制；R1仍为规则检索组件，多个service是负载不自动跨生命周期；U2可复用的namespace/合法候选资格。 | **2+1+2=5**。标准，核scope结构由谁提供/误配router、flat-v-filter控制及代价，若实际安全/权限边界变化只深入该域，不全服务规则。 |

各候选保留且分数由新增决定，非配额或预期Books产出；支持与直接反侧足即停。若必要层显示命题/影响域真实不同，明确证据再调，不因低访问或已有覆盖降分。现交同一reader评分/投入校准，随后单篇ready即推进，不等全五。

### 20.2 32110 必要完成（6分）

精确题名 **Who Verifies the Tools? How Warped Formatters Mislead Agents and Their Verifiers**，只实际打开[2610.32110v1 HTML](https://arxiv.org/html/2610.32110v1)核心§2–4/6及A estimate/provenance反侧。tool实际计算与呈现分开，same内部result双渲染；B同时补披露与行为指令，因此agent改善不归披露标签单因。40作者已知缺陷case，8pilot/32holdout，每model/case/condition5rep；scope仅7document且一件跨split，预定去该件仍同模式。claim sheet frozen、model共识grader/作者裁决，独立human仅pilot12及full36，不把AI校准64冒人工或总体金标。

固定手写falseanswer只换format才是verifier因果对照，threefamilies90/90→0/90；生成答案frequency条件选不同answer非因果。额外facts×supported/correct四格仅46已选scope/completeness错误，只有facts+correctness全拒，不授general competence。直接反侧：估值同line侧生archivepage仍被洗确定、namespace clear113/120仍错，不能把更清楚文本当typeenforcement。Stresscase单系统/对抗已知缺陷、单toolreturn无loop/非productionprompt，不估真实发生率；auditprompt事先知道defects、作者run/部分模型确认，未作为长期采用，不读prompt全仓审计/两外部PR或运行复现。收益/代价只采用披露资格与审计成本，不拿$74.44研究API费代表生产净费。支持和反侧足即停。

### 20.3 32110 actualowner与整体三件PRE

实际owner `AGENT-TOOL-CALLING` Ch78 Tool Catalog/Result Typed Admission。已读其完整catalog admission→typedfailure→旧总结，并完整读Preventive/Evidential、TypedClaim与canonicalaction相关论证及未变Ch77/79交接。具体NC：transport≠semantic、receipt来源/形式证明≠真值、permission/effect分责均已有。差额不是再喊独立verification，而是正确payload的formatter遗失scope/uncertainty/namespace导致shared-information上限；同falseanswer呈现对照与supported-v-correct反侧支持窄补。root已确认transport/semantic完整段后→两项机制总结前精确位无冲突；旧TypedClaim不变。以下完整两肩+原单段/独立marker/本人注交sole reader，未PRE不SAVE。

完整前肩：

工具调用返回后还要分离 transport success、semantic usability 与 provenance。HTTP/SDK 成功但 payload 空缺、错误或不可验证时是 typed failure，必须阻断事实提交；prompt 声明只能作为旧工具链兼容 fallback，不能替代协议状态。<!-- source-family:SF-2026-ARXIV-2609-14758 -->

拟新增正文与独立marker：

即使 payload 的计算正确，formatter 仍可能把受限搜索写成全库未发现、把返回条数写成总数，或让估值和不同 namespace 的整数看似确定事实。应在呈现层保留 searched scope、截断/总数资格、每个派生值的不确定性与 typed identifier，并把模型实际可见文本和后台执行事实成对审计。[受限的同结果双呈现实验](https://arxiv.org/html/2610.32110v1)中，固定错误答案只改变 tool wording，verifier 的接受就会翻转；另一个 verifier 若只拿到同一份省略资格的文字，并不构成独立事实核验。要求“被文本支持”和要求“符合额外核过的事实”也不是同一个判断。不过修复文本同时含披露与行为指令，不能将全部收益归给字段标签；estimate 的旁系页码仍可能被洗成确定值，namespace 标签也未解决多数跨 ID 误用，需要接收端类型或解析校验。呈现/源事实差异检查、兼容迁移与额外核验均有代价；单系统已知缺陷的无 tool-loop 压力测试不估计生产发生率，也不证明审计 prompt 找全。范围或身份仍不明确时，保留局部结论、原结果与重新取证，不以 receipt 一致或两个模型同意批准后台真值。
<!-- source-family:SF-2026-ARXIV-2610-32110 -->

完整后肩：

两项机制分别缩小输入 action space 与防止失败结果被语言模型补写，代价是 catalog routing、schema 校验和额外重试。作者有限模型/域与强制调用实验不证明开放工具生态的完整覆盖。

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32110` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32110v1)§2–4/6与A estimate/provenance核心反侧必要，Methods前2+2+2=6经R102校准。仅正确tool结果的formatter资格损失及同信息verifier上限；保B披露+指令共变、固定答案因果与生成答案frequency分开、估值旁系/namespace失败、32holdout/单系统已知缺陷/无tool-loop，不采普遍恶意tool/审计召回/生产率。未核code/PR实现、完整审计附件或运行复现；原三件PRE/SAVE/selfread/solePOST按本日实际后到，不预签。

### 20.4 32305 工业主域必要完成（6分）

精确题名 **DMAIC-Bench: From Self-Reflection to Self-Restraint for Agents in Multi-Stage Analytical Tasks**；[2610.32305v1 HTML](https://arxiv.org/html/2610.32305v1)实际读§3机制/4.1–4.5采用所需控制、O/P直接纠错/限制；不采用RNA/GWAS扩展，不全附录/全任务表。97seeded任务/15case、40matchedfork把52NO-GO配146同位GO；不是300个独立任务。共享Harbor native loop，3attempt；casecluster CI，未用现存32task structuralheldout做报告campaign，非独立泛化/排行榜认证。数据steward仅按declared publicpredicate放行，不知private truths；9stop有跨batch锁，40nogo数据已给，故不能由无unauthorizedaccess认证所有forbiddencomputation被阻。

关键反证是272reported+verifiedNO-GO中201走错，174在诊断后才forbiddenanalysis；不把其余computation/reportfailure或时间顺序称模型已读/知道。路线严格‘算了即错’，expert最终报告可能不支持该计算，二者不同，不能用routeerrors估相同harm。Permit/规范规则与remind控制保两侧：Astra停得更多却GO退步、DeepSeek规范规则改善但提醒增量CI含0。plainbrief可要求reference禁止的量，故部分继续有task冲突；去冲突干预仍未全修，非单一completionbias因果。O九scorer错误含check误当branch、未报告guard误当knew/跨stage methodset误认route等均已纠正；reference1/null0只是内部一致性，非rule真值。完整采用命题不需重复M全audit/所有模型表或E全部prompt，core已明确expert抽样两研究与限制；不引用全报告47%作为生产率。资源额外诊断/审计皆成本，不采跨域或生产安全。另一次只读curl取原HTML未取得输出已取消，不作为正文缺口/读取成功。

### 20.5 32305 actualowner与整体三件PRE

拟实际owner `AGENT-WORKFLOW` Ch81 TaskStateAlignment。已读state machine完整transition contract、alignment完整两段、随后人类permission双gate、DeterministicSpine语义与相关恢复，复用未变Ch80 critique不授action/Ch82委派交接。具体NC：precondition/真实executor、stateversion一致和用户许可已有；差额是同fork相反证据的dispatch验收、correctdiag→禁止的同batch计算反侧，以及合法停止同时保GO，不将一般前提检查当新贡献。Ch66总体measurement分层不接管workflow execution obligation。root具名窄位协调已发，未确认不SAVE；即使readerPRE通过也仅此段/marker/本人注，旧approval不变。

完整前肩：

对齐检查减少 stale-plan execution，却增加 snapshot、cross-component reconciliation 与 false stall；任何输入遗漏都可能产生表面一致。简单 linear workflow 仍可用单 state pointer，外部状态变化或 delegation 出现后才升级完整 contract。`arXiv:2605.19314v1` 的 §3、§4 与 §7 只支持其 hierarchical task-state alignment 和受测 long-horizon embodied tasks，不证明开放工具环境中的 completeness、liveness 或通用成功率。

<!-- source-family:SF-2026-ARXIV-2605-19314 -->

拟新增正文与独立marker：

状态版本对齐之后，还须检查诊断是否真正约束了下一次计算，而不只在 trace 里出现一个正确 guard 值。可以在同一 workflow fork 构造只翻转前提证据的 GO/NO-GO 配对，分别记录诊断、允许的转移、实际执行和终态 claim；只会继续与一律停下都不能通过。[DMAIC-Bench的工业主域对照](https://arxiv.org/html/2610.32305v1)发现，已报告且核对正确的失败诊断后，仍可能执行该前提禁止的分析；时间先后不证明模型实际读过诊断，也不识别内部认知原因。仅在下一批数据入口设 gate 还不够：同一批已释放数据可以支持被禁止的计算，按模型声明放行也不等独立验证前提。需要强约束的分支，应由 runtime 在真正的计算或发布边界核 guard，这是由反证推出的要求，不是该基准已实现的完备防线。合法停止应按有效 prefix 验收，同时保留证据成立时的继续能力；更明确的停止许可或规则提示可能改善一侧、损伤另一侧，不能只报 NO-GO 提升。成对任务、执行审计及独立报告核查增加费用；其 scorer 曾纠错、无报告 campaign 使用的 held-out，且 plain brief 有任务冲突，故不用局部错率代签通用不服从。规则无法可靠编译时保留人工 milestone/明确未决，不让继续计算或隐去无效结果自行变成合法完成。
<!-- source-family:SF-2026-ARXIV-2610-32305 -->

完整后肩：

对话型流程还要分开“进度证据允许提出下一步”与“用户已许可真正推进”。阶段判定可以触发一个低压 offer，但不能替最新 turn 签发同意；明确拒绝或犹豫应阻止晋升，而不是被先前进度摘要覆盖。若状态提取在 background 异步执行，foreground 可消费上一轮的结构摘要，却必须让最新用户输入保有拒绝当前 transition 的机会。它补的是提议与获许可之间的交接，不让模型输出的状态字段成为事实或硬授权。

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32305` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32305v1)工业§3/4.1–4.5及O/P必要，R102前评分2+2+2=6。仅同fork证据翻转→实际计算/claim分责；保steward按声明/同batch未锁、174时序非已读因果、GO/NOGO tradeoff、scorer九纠正/无使用heldout、plainbrief冲突，不采认知cause/完备hardgate或普遍工业率；不采用RNA/GWAS科学扩展。未核全任务/附件/实现运行复现；原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。

### 20.6 32110 R107后三件真实SAVE/完整自读；32305窄位已协调

32110 R107必要6/actualCh78与§20.3原三件整体PRE通过，root精确位已授；作者仅apply_patch保存原单段/marker/本人注。正文972/marker973/本人注979，完整新增/完整两肩/本人注+旧2510.04514首注逐字读回匹配，marker1；剥三件恢复fresh baseline `a7bd89e88a90edf80522629ee11a1584dd76d8f8e9c3b3d486916398764f3da3`，限定diffcheck通过。现交soleactualPOST，不预I。32305 root已明确§20.5 TaskStateAlignment精确窄位无冲突，仅工业主域；仍待sole必要/整体PRE。

### 20.7 32483 必要完成（6分）

精确题名 **When Agents Fail: Model or Harness—Who’s to Blame?**；实际[2610.32483v1 HTML](https://arxiv.org/html/2610.32483v1)读§3.3/4/5.3、6.1–6.3采用所需比较/反侧、6.4资源要点及A.3状态映射/A.4分母和归一边界。只联合完成/正确及pair残差，不遍全modeltable/六benchmark附录或111cell资源矩阵。4generalharness×4coremodels中两multimodal仅3model，跨benchmark用common3×4均衡panel，fixednative参考与stress不混入；R4，selected benchmark/外部条件匹配仍保nativeprompt/loop等捆绑，非模块因果。

U=normaltermination×evaluatorconsumable，不含taskcorrectness；如newartifact路径合格即可valid，errorfree不等真成功。J=mean(US)全scheduled分母；VCR>0才可拆VCR×clean条件均值，零时条件均值undefined但J0。非clean仍可有officialcredit，不能一律‘已失败无价值’。Fit对每model/benchmark面板best归一，zero-best全ratio0（本实验positive），换候选/任务权重可换reference；geomean有zero→0且非普适偏好。双中心VCR residual只是当前panel偏离additive均值，bench反向可聚合抵消；matchedtask bootstrap2000保全部rep与配置，CI pointwise无multiplicity，留一model只是observedpanel回顾诊断。6.3整体排序不变的反侧也保，不声称jointmetric总能改排名。

资源只在matchedblock100%token记录比较，全failedattempt留账；mean/median长尾、低load可早退，logicaltokens不直接比跨tokenizer/硬件、真实成本与SLO。支持的设计差额与反侧已足；不读取全部trace/action实现或把actionrealization定点事件归成whole-model根因，不做系统推荐。分数维持6，不因规模/能落Book加分。

### 20.8 32483 actualowner与整体三件PRE

实际owner `PLATFORM-EVALUATION-SYSTEM` Ch66 EvaluationIdentity。已读该节完整身份/adapter两段、紧接specoracle、environment起点/重演；并读RuntimeCoverage与32285完整新增及开篇成功层分工。具体NC是model+runtime+environment身份、native证据不可自证与任务/机制两表已有；差额不是又写身份，而是完整交叉panel中的doublecenter残差/联合E[US]和clean条件分母，以及relativefit面板reference。root已确认adapter完整段后→spec/testoracle完整段前窄位无冲突，不重owner全章。以下原一段/marker/本人注及完整两肩交sole reader，未PRE不SAVE。

完整前肩：

可复现的评估身份至少应写成 `model × benchmark × harness × environment × scorer`。Harness 负责适配与控制流，Environment 负责可执行状态，Scorer 只拥有从轨迹到判断的映射；聚合分数之前必须保存原始 trajectory 与 component-level receipt，才能区分模型退化、adapter drift、工具故障和评分变化。统一协议可以复用执行与观测设施，但每个 adapter 仍需证明语义等价。

拟新增正文与独立marker：

把 harness 纳入身份后，还应以完整交叉面板检查某个配对是否偏离组件均值，不能用一个模型的优胜 harness 推出全模型排序。固定任务、重复次数与外部约束，分别保存任务分数 S 和正常终止且可交给 evaluator 的 U，再报告同一 attempt 的联合均值 E[US]；只在 U=1 的幸存运行上算分会换掉分母，非 clean 的有效任务进展也不应从原分数中抹掉。[一项受限 model×harness 对照](https://arxiv.org/html/2610.32483v1)以配对值减模型均值、减 harness 均值再加总体均值，揭示聚合会抵消的交互残差；它依赖当前均衡面板和所定义的 U，不是组件根因或新模型的适配保证。将联合分数相对面板最佳归一后，候选 harness、任务权重或模型人口改变还会改变 reference，不能把相对 fit 当固定能力。所有失败尝试的 tokens 也应纳入相同覆盖分母；少耗可能来自早退，token 量不等跨 tokenizer 的计算、墙钟或账单。交叉运行、状态映射、完整资源归档和配对不确定性估计都有成本；native prompt/控制流仍是捆绑变量，分母、覆盖或面板不齐时保留分项与不可比，不由高完成率或正残差批准正确、安全或普遍最优。
<!-- source-family:SF-2026-ARXIV-2610-32483 -->

完整后肩：

评估身份中的task specification与test oracle还必须对齐：隐藏test本身合理，但若test要求的名称、路径或literal既未在可见规范披露，也不能由起始代码/环境推出，失败就混入了对隐藏约束的猜测，而不只测实现所声明需求的能力。可逐项追踪oracle依赖到可见来源，并用reference依赖的单名遮盖等有界干预辅助定位缺口；静态scanner只提出候选，仍需独立人工核对可推导性。[一项五语言受限审计](https://arxiv.org/html/2610.30635v1)支持这种specification–oracle gap确实存在，但检测precision/recall并非完美、召回样本小，受影响case失败较多也不把全部失败唯一归于缺口；剔除后的总体排行基本稳定，更不能宣称所有benchmark失效。应共同保留原spec、base、reference/test与审计版本，分别报告缺口切片及完整人口；依赖提取、干预运行、人审和重新评分全付费。缺口确认时优先公开必要约束或隔离该切片并重验，不为提高分数擅删有效test；可推导性未闭时保留Unknown与原分数上下文，不让一次pass或fail独占通用代码能力结论。<!-- source-family:SF-2026-ARXIV-2610-30635 -->

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32483` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32483v1)§3.3/4/5.3/6.1–6.3关键反侧、6.4资源要点与A.3状态映射/A.4分母边界必要，R102评分2+2+2=6。仅E[US]与conditional分母/交叉panel残差；保nativebundled、balanced/commonpanel与fixedreference隔离、panelbest归一/零块、pointwise无多重校正、failedtokencoverage非总费，不采rootcause/公平总排或新模型外推。未核全模型/附件/代码运行复现；原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。

### 20.9 32608 必要完成（5分）

精确题名 **UAE GovTrust Scope Filtering Gains and Routing Failures in Bilingual Public Service Retrieval**；actual[2610.32608v1 HTML](https://arxiv.org/html/2610.32608v1)§3–5采用所需机制、评价与直接反侧已读，非新AB/date。22AI辅助双语summary/21source，6card仍只索引excerpt，publisherlevel与applicability分开；no independent Arabic/domainjudgment、query/label/router共编无untouchedsplit。主72variant来自36scenario，翻译不独立；100gate/10mixedexploratory/24control及168post-audittransform分母分清，不能拿开发72与压力168相减估总体effect。

原router在开发labels完美使RoleRRF=OracleRRF，不能认证scopeinference。字段包含action{answer/clarify/abstain}+allowedscopes，local+FED是目录policy非普遍法律；wrongaction空C仍0recall，不能以无wrongscope返回免检。Scope-role swap保词频时BM25无从两边都选对；DirectLookup/RoleDense近似主fusion得分，反驳目录需要复杂hybrid。压力定向按已知parser编，route仅2/168/证据全存亦2，120wronggate/46wrongscope；不是naturaltraffic或heldout，支持存在且重复的失效，不估发生率。Oracle161/168只离线标注上界，不上线可得。

独立rank反侧：BM25零overlap仍按ID给rank，English-only Arabic evidence时融合污染；只移除此类sparse候选不改dense，RoleRRF52→64/72，原双语无变化，不能推广最优cutoff。Warm单CPUthread float32、3warmup+3randompasses、无cache/network/generator/concurrency/coldstart；重装同host复现1320不是external/humanvalidation。只用源报告结果，未运行code/读全ancillary或核真实法律内容；足即停，维持5分。

### 20.10 32608 actualowner与整体三件PRE

实际owner `AGENT-RAG` Ch76文档结构/查询分层。已完整读2604.25676 scope、前置schema/documentstate与后续feedbackpool，并读OnlineRetrieval融合伤害30612和前批32318/32336上下文。具体NC：scope独立于query、pool外证据reranker救不回、router非oracle与hybrid可伤害已有；差额为控制地点role≠mentionedlocation及hardfilter的action/scope/evidencesurvival分层，另零sparse分可污染条件内rank这一受测反侧。root该精确位协调已发，未确认与PRE不SAVE；不因为已有一般原则强NC或硬贴法律摘要。

完整前肩：

检索域本身也是一个独立旋钮：在错误的语种或区域语料里反复改写query，仍可能只得到主题相关却不适用的证据。一条[受限多语检索分支](https://arxiv.org/pdf/2604.25676v1)让planner分别提出corpus scope与查询表达，再用证据critique决定是否重选语料、改写或停止；同一英文问题可以指向不同地区，因此语言匹配不是culture真值。Corpus选择仍受原权限与来源身份约束，critic给出的相关、适用与充分性分数也不能代替原文支持。作者在13语言Wikipedia与两个文化MCQ任务上给出分步对照，但额外大模型critique/多轮检索未与固定路线严格同预算，最终同为top-5不代表中间成本相等，也未验证开放问答。它支付多索引、scope选择、critique与全部重检索，语料缺证时再改query也无法补出事实；scope含糊、critic共错或收益不足时，保留固定已授权语料、原query/有限多改写及独立原文核验，不让地域标签或自动停止签发正确答案。<!-- source-family:SF-2026-ARXIV-2604-25676 -->

拟新增正文与独立marker：

Scope 不能只从问题出现的地名集合推得，还应解析哪个地点承担当前服务的控制角色；居住地、车辆注册地和服务发生地可同时出现而指向不同规则。应将 action/scope 选择、过滤后证据存活与子集内排序分别验收：正确 metadata 的 oracle-filter 收益，不是实际 router 的收益，空候选也不能因没有返回错域文档而算安全命中。[GovTrust的受限诊断](https://arxiv.org/html/2610.32608v1)中，原模板下正确路由掩盖了这一差别，已知规则的否定、纠正及无关地点/日期扰动却可先抑制检索或误删目标，后继 reranker 无从恢复。另一条独立失效面是零词重叠的 sparse 候选仍以 ID 破 tie 后参与融合，即使 scope 正确也会污染跨语排名；修正该分支不修复 router。两类检查均须保留无回答、错域和正确路由后仍排错的分母，而不是只报条件内 rank。该小型共编目录和事后具名扰动不是持出用户流量，也未独立验法律或阿语标签；路由、索引、复核与重检索皆有费。控制角色含糊时应澄清、保留多 scope 的获准取证或回到已验路线，不让完美模板分数批准硬过滤全部新问法。
<!-- source-family:SF-2026-ARXIV-2610-32608 -->

完整后肩：

在固定语料内，改写还可由一个累积的相关性反馈池驱动：每轮只给当前Top-k中新出现的文档按原问题评分，保留已评文档及等级，再据此生成下一轮扩词；检索消费原问题与本轮扩词，不把已过时的历轮文本一直叠上去。已评标签复用节省调用，却把judge错误留在后续条件里，原问题不变并不证明评分正确或永远无需重验。[受限反馈对照](https://arxiv.org/html/2606.13905v1#S3)以满分、少新文档或轮次上限停止，但饱和只是停止这次探索，不是语料已完备、答案已支持或最后一轮最好；若干数据集后续轮次反退。直接基线的生成配置相近，不代表额外改写、评审与串行检索已经等总预算，也不足将收益唯一归给反馈设计。应共同保存原query、corpus/retriever、已评池、judge、当前expansion及停止原因，另验真实相关性与答案支持；评分漂移、质量或全费失准时，保留原query、预算化多改写/固定融合与独立原文核验，不让反馈自评签发充分性或净加速。<!-- source-family:SF-2026-ARXIV-2606-13905 -->

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32608` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32608v1)§3–5路由/过滤/排名与稀疏零分直接反侧必要，R102评分2+1+2=5。仅controlling-role/estimatedscope与oraclefilter分责，保22card共编/无untouchedsplit、168post-audit定向依赖例非总体率、6card只excerpt/法律阿语未独核、warm单host/无生成SLO；回退为项目推导非已验防线。未核附件code或运行复现；原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。

### 20.11 32851 必要完成（5分）

精确题名 **Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves**；actual[2610.32851v1 HTML](https://arxiv.org/html/2610.32851v1)Design/Deployment/Boundaryconditions中拟采用必要已读，不重AB/date。Producer先给service/domain/feature等分类，artifact唯一ID/来源版本/lineage入registry，catalog/store/hypergraph同步；alias/intent缩node→artifactID约束vectorquery，graph是artifact导航非实体truth。上游分类不知/人写异质文本需重分类成本，不能声称免内容推理普遍成立或ontology昂贵是受控实验。

关键直接反侧：lightweight intentmodel/alias/placement可错而静默剪证；LLM confidence按scoped结果判不足才fullcorpus扩，错scope中出现合理假阳性可能不触发。原文称safetyproperty不被采用为完备防线/ACL；widen后错service可重入，须另核scope。Runtimecontextgraph只存消费证据路径不验证事实，usagewriteback不是truthpromotion。现有>100live defects/35regression由熟悉服务开发者审，没有flat-v-scoped随机/匹配比较、分母/失败率；retrievalaccuracy与wideningrate均inprogress，latency未测。故采用具体组织接口/边界，不复制‘高准确/低延迟/一周省总费’结论。codechange自动reingest/完整boundarycurationroleagents仍发展方向，不能冒全production。源实现未公开核验/无运行或全图像素检查；已足停止，5分不因deployment词加分/不因缺benchmark降分。

### 20.12 32851 actualowner与整体三件PRE；两检索窄位已协调

实际owner `AGENT-RAG` Ch76 ingestion。已完整读source-manifest coverage、2509.04696 ontology→抽取/normalize、OCR documentstate与结构分层；Ch84durableartifact/typedownership一般NC，不接管retrieval组织。具体NC是source/provenance、字段类型/版本/入库一致、queryscope与事实authority分离已有；剩余差额为机器生成时已有producer/component/service namespace保留在artifact层，候选ID裁剪而非内容entityontology及confidence widening失败边界。root已明确本位2509.04696完整段+marker后→OCR标题及首段前与32608的scope→反馈池独立位均无冲突；只各一段/marker/本人注，不锁全章、不改旧论证，不把scope当ACL。以下整体原稿交sole reader，未PRE不SAVE。

完整前肩：

语料身份明确后，已有ontology还可以先决定抽取器获准读取哪些字段，而不让模型每次从全文重新发明schema。一条[受限知识入库分支](https://arxiv.org/html/2509.04696v1)按实体类型从既有ontology生成有界snippet，将predicate、domain/range、qualifier与单位要求供给LLM抽取，并与后端规范化配置衔接；供给与排序改变的是可提出哪些事实候选，不使schema合规成为原文支持。Extractor提出的最短surface、归一答案或单位仍需回指原页，第二模型对context与triple给出True也只是grounding代理，不替代实体、时间及冲突核验。工程上应共同保存source、ontology、snippet与normalizer版本，条件外字段或未知单位回到原文和schema维护者，不能由模型自行扩权；这是从接口推出的约束，不冒原系统已实现全部权限协议。抓取、条件制备、抽取/grounder、链接与单位归一、人审和索引刷新均付费，不同筛选人口的precision与coverage也不能合成全网页保证。Schema、来源支持或单位映射失配时，保留原文检索、可信规则/人工映射及待定状态，不由更多入库triples或另一模型同意批准事实。
<!-- source-family:SF-2025-ARXIV-2509-04696 -->

拟新增正文与独立marker：

当语料由已知 producer 为具体组件和服务生成时，组织结构还可落在 artifact 层，而不先从内容抽取一套实体 ontology。同名 eligibility 规则可能属于不同服务；保留 producer/run、service/domain/feature、类型、源版本与 lineage，把查询先解析为候选 artifact IDs，再在该集合内做 hybrid 检索，能让错服务的近似文本不参加排名，而非期待更高相似度将它压下去。[一项单企业实现](https://arxiv.org/html/2610.32851v1)采用这条分支，并以 artifact 节点及共享 workflow 的多方关系导航；命名结构只保留上游已作的分类，不证明分类或规则本身正确，也不是 ACL。Intent、alias 或 placement 错误会系统性排除证据，LLM 判 scoped 结果不足后扩到全库是恢复候选路径，却可能再次引入碰撞，不能由 confidence gate 自签充分性或权限。Context graph 可回指被消费的规则和源位置，仍须独立检查；usage write-back 也不是新事实的自动授权。Catalog/图同步、元数据维护、扩池及人核都有费用，作者部署的缺陷案例没有给出受控精度增益，widening rate 与 adjudicated retrieval accuracy 尚在评估。缺可靠 producer 元数据或版本/placement 支持时，保留人工分类、较窄已验范围及原文检索，不把这种 artifact 索引提升为通用实体图替代或生产保证。
<!-- source-family:SF-2026-ARXIV-2610-32851 -->

完整后肩：

### OCR 之后仍需要 Document-level State Owner

逐页 OCR 保留页内坐标且易于并行，但跨页段落、表格和标题会被切断，RAG 随后面对互相矛盾的 chunk 与结构索引。ingestion 应在 page artifact 之上维护 document revision，跨页合并结构并同步 chunk、locator 与 enrichment；原页和 region provenance 仍是可回溯 source of truth。收益是检索消费同一文档状态，代价是合并错误会跨页放大且更新粒度变大；结构不可靠时回退 page-level evidence。现有结果绑定披露 OCR/VLM、H200 与文档集，不证明跨页摘要可替代原始证据。

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32851` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32851v1)Design/Deployment/Boundaryconditions采用所需必要，R102评分2+1+2=5。仅producer已知artifact namespace→ID约束候选分支；保placement未独测/intent错失、LLM扩大仅候选恢复且非ACL、单estate/实践者乐观、accuracy+wideningrate未完成/无latency测量，codingagent/完整serving未来设计不冒部署。未核私有实现/全图像素或运行复现；原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。

### 20.13 32110闭合；32305 R111后三件真实SAVE/完整自读

32110 reader R111唯一actualPOST通过，正式6分I/Ch78窄位释放。32305 R111必要6/实际Ch81差额及§20.5原三件整体PRE通过，root精确位已协调；作者仅原单段/marker/本人注apply_patch SAVE。正文L134/marker135/本人注1365，完整新增/两完整肩/本人注及旧31712首注逐字读回匹配，marker1；剥三件恢复fresh baseline `3d60d42ff8cdf2cfea18fa94666337ceeb3714541b46338651de7a0e9ee07257`，限定diffcheck无输出。现交soleactualPOST，不预32305 I；32483/32608/32851必要/原稿PRE已ready，仍按独核实际后到，不扩源/全附件。

### 20.14 32305闭合；32483 R112后三件真实SAVE/完整自读

32305 reader R113 soleactualPOST通过，正式6分I/Ch81窄位释放。32483 R112必要6/实际Ch66差额及§20.8原三件整体PRE通过，root精确位已确认；作者仅原单段/marker/本人注apply_patch SAVE。正文697/marker698/本人注5864，实际完整新增/identityadapter与specoracle两完整肩/本人注+旧32285首注逐字匹配，marker1；剥三件恢复fresh baseline `9421a78de542824db8d966f79d7996cb171725f6bf74b56cb9fd655554dfd823`，限定diffcheck无输出。现交soleactualPOST，不预32483 I；scope两项原稿待reader，不重必要/扩源。

### 20.15 32483闭合；两scope R116后各三件真实SAVE/完整自读

32483 R115 soleactualPOST已过，正式6分I/Ch66精确位释放。32608/32851各必要5/actualCh76与§20.10/12原三件整体PRE已R116通过，root两精确位已无冲突；作者顺序仅各原单段/marker/本人注apply_patch SAVE，未改两肩或旧注。32608首保存完整读回同PRE、marker1、剥本三件恢复fresh baseline `736ca6ecfef4bcdbf35416a0e5d0df7497d85741f00095cfa5b7e2fef512ebab`；其时正文114/注1792。随后32851完整新增/ontology前肩及OCR标题+首段完整后肩/本人注+32608及旧32336注读回匹配，marker1，剥其三件恢复fresh第二baseline `c97e70cb75181548e616324c1d2b145e5bbfa7f84107bfb2432ea602e7195636`。剥两项全部六件恢复第一baseline，证明仅本两窄增量；限定diffcheck无输出。

当前真实locator：32851正文98/marker99/本人注1795；32608正文117/marker118/本人注1797。新增、完整肩与原注均保，本两位现交soleactualPOST，不预I；新五没有其他Methods/owner普通待办，不扩来源或下一候选。

### 20.16 本批五项真实闭合

唯一reader R119实际POST通过32608/32851，各5分I/Ch76两精确位释放。本批最终五唯一家族全按R102评分最低投入、actualowner具体差额及原稿PRE/真实SAVE/完整自读/solePOST闭合：32110 6/I `AGENT-TOOL-CALLING` Ch78（R111）；32305 6/I `AGENT-WORKFLOW` Ch81（R113）；32483 6/I `PLATFORM-EVALUATION-SYSTEM` Ch66（R115）；32608 5/I和32851 5/I均`AGENT-RAG` Ch76（R119）。一般原则NC与新增差额各自保在owner段，不因主题映射或已有位置强造I。当前正文locator分别972、134、697、117、98（marker均次行），Report后续行政归并归root。日期/准入继续复用本日Oct26精确v1；新五普通必要/owner/SAVE/POST待办为零，不代表本日Source/Report全完成。未stage/commit/push、未写Report/State或其他日期；停止在本分工，不自动扩源或接新家族。

## 21. 代理下一五项：流式视觉与模态预算（Methods前评分）

root新授31734/32132/32784/32664/31768，固定本日BJT Oct26窗。已按新批完整重读AGENTS、当前研究/Report合同、Prompt、ROADMAP、每日来源使用组与最新本日checkpoint；仅复用SOURCE/ARXIV_B既成完整题摘、落窗/去重/准入校准，不新请求AB/date或宽列表。ARXIV_B原拟五项全6只作既有准备；本次按实际拟采用新增重新明确R维度，不以旧分布、读费或Books结果决定。Methods尚未读，不预证据完成或I/NC。

### 21.1 五项三维评分与最低必要范围

| 身份/精确已核题名 | 实际新增与三维边界 | 分数与本次最低投入 |
| --- | --- | --- |
| [2610.31734v1 — DirCast: Live Esports Directing and Commentary with a Single Streaming Video-Language Model](https://arxiv.org/abs/2610.31734v1) | 不把human预选镜头上的commentary当自主direct；lowres allview scan→hold/switch→highres chosenview，context仅保上播/说过而余流expire，改变因果多流选择与播出状态交接。D2重要状态/感知分支；R2实际跨多流输入选择、模型可见状态与控制/输出，而非因电竞负载扩3；U2可复用的因果可见/多分辨率取舍。 | **2+2+2=6**。标准；核causal streaming/scan-switch/保留过期接口、同输入对照和质量/费用/切换失败，支持足即停，不读全部比赛案例。 |
| [2610.32132v1 — SyncPro: Synchronous Reasoning and Responding for Proactive Streaming Video Understanding](https://arxiv.org/abs/2610.32132v1) | 原scheduled reasoning阻塞响应；共享causalhistory而inner与response独立激活/事件触发并发，实际分开证据状态更新与输出需求。D2调度语义重要变化；R2跨输入事件/推理状态与response执行，不以共享单模型名给3；U2稳定的状态/输出生命周期分责。 | **2+2+2=6**。标准；核共享history一致性/trigger与两路并发、关键response延迟及质量反侧，非全训练数据/全场景表。 |
| [2610.32784v1 — Video-MemComp: Taylor-Guided Sensitivity-Aware Memory Management for Streaming Video Understanding](https://arxiv.org/abs/2610.32784v1) | 原KV局部距离不等输出扰动；local approximation×layer sensitivity分解、preRoPE聚合/logitbias保mass及gradientprior/contextentropy分层预算，改变KV压缩判据。D2重要近似/位置边界；R1仅cache压缩/层预算组件，层数/训练梯度/能接系统不自动R2；U2可复用误差与budget条件。 | **2+1+2=5**，相对旧拟6仅R2→1：不借广泛模型/系统reach。标准；核Taylor假设/旋转位置/mass与层预算必要及质量/实测cost反侧，不全附件。 |
| [2610.32664v1 — The Answer Knows Where to Look: Zooming before MLLMs Answer under Visual-Token Budgets](https://arxiv.org/abs/2610.32664v1) | correctanswer hindsight attention可定位但不能线上先知，looktoken独立pointer+counterfactualview学zoom且不进answerpass，改变budget下定位监督/消费资格。D2重要定位接口；R1单视觉区域选择组件，额外训练/answerforward不自动跨系统2；U2可复用的privilegedtraining-v-online定位边界。 | **2+1+2=5**，相对旧拟6收R维度而非看成本/已有覆盖。标准；读hindsight资格/selection-vanswer隔离、visualbudget匹配和直接伤阅读/放大错误反侧，够用停。 |
| [2610.31768v1 — Efficient Omni-modal Large Language Model Inference via Per-Query Modality Selection](https://arxiv.org/abs/2610.31768v1) | frozenOmniLLM的querywise cost-sensitive modalityselection，按tokens/latency/money独立成本，不以全模态输入天然最优，具体识别负/冗余信息与选择误差。D2重要输入/成本替代边界；R1局部input-modalityselector，跨模态是输入人口而非自动跨系统2；U2可复用的query质量—预算条件。 | **2+1+2=5**，旧拟6的R2不因模态数继承。标准；核selector可用信息/训练target与oracle区别、成本口径及质量反侧，不全benchmark表。 |

五候选全部保留；没有为差异或保留率强造低分，也不因已P一概给6。正式调整只针对新增命题实际到达边界，后续如原件显示reach不同再具名解释，不因访问/Books处置降分。以上交唯一reader校准，随后单篇就绪即必要→actualowner/NC→整体PRE及真SAVE/POST，不等全批。

### 21.2 31734 必要完成（6分）

[DirCast精确2610.31734v1 HTML](https://arxiv.org/html/2610.31734v1)实际读§3数据资格、4.1–4.6采用所需流序列/holdswitch/memory/目标与节拍、5.1协议及5.3/T3–5关键对照与5.2指标反侧，支持足即停，不全比赛/附例或代码。27match replay渲染10hero view并对齐humanbroadcast，只有strict LIVE作direct标签；20train/3calib/4test、36s clips1fps、4test496clips，跨match不是496独立比赛。当前structuredhero状态与event是额外输入，不能只归纯pixel；训练用human节目/perturbedprogram drift及kill附近eventanchoredtarget，不等部署已见未来事件，未核实现所有causalcutpoint。

每秒先clock/event+10lowres/state，再D决策、chosenviewhighres、C/words；hold默认+pointer其他9camera，低分辨率128/fine288。未上播lowres W8秒过期；上播/words/event较长但超过36s总horizon也删，不能把program永久无损。Qwen3VL8B LoRA三epoch/8H100训练，inference单GPU；未披露精度/并发/完整capture&ingest费用，不补造。Thresholdrate feedback/phraseend策略是受测节拍，不等human utility/外部turn许可。

关键反侧：humanagree Top1约27而非完整专家director，actionrule fightcoverage62.4高于41.1，人工镜头/killcoverage不同目标。移eventtarget Anyvisible反更高，stateremoval解说CC不变；不能把全收益归一个组件。Joint/separate同role以及humanprogram下对照支持sharing/任务训练，仍baselinecommentator看humanprogram，而ours自选，GPT5替官方不可用5.1judge且CC29.21是相对offlineGPT4o的wins，不宣全面更优；F1可奖alwaysspeak/fidelity可奖沉默。三seed统计clipbootstrap非match泛化cert。8×288s长窗retention有性能/缓存变化，不等整场/设备deadline或horizon信息无损；只采用角色化输入/保留接口，停止全场case/更多表，不跑模型或代码。

### 21.3 31734 actualowner与整体三件PRE

实际owner `MULTIMODAL-REPRESENTATION` Ch23 StreamingIdentity。已完整读该节causalprefix、videoorder/history检索、双KV/逐帧chunk、longshortmemory/trigger、grounding/通知与时序边界；并读Ch22/24开篇交接，Books背景/理念/写作指南已本批重读。具体NC是因果可见前缀/已到达不等已提交、memory/trigger分责与有界窗口已有；差额是多流输入中候选扫描与真正上播节目不同保留资格、hold/switch后fine读取的roleconditioned接口，不新增导播产品手册。root具名slot协调已发，未确认+PRE不SAVE；只本一段/marker/本人注，其他时序/生成owner不变。

完整前肩：

流式视频还应分开“学会顺序”与“此刻需要读历史”两种干预。训练可将带timestamp的帧内容打乱，让模型恢复顺序后回答；推理则先读当前窗口，只有答案分布entropy高时才用pooled frame相似度从可见历史做coarse-to-fine检索并重新回答。顺序监督没有消除timestamp线索的shortcut，低entropy也只是无需检索的proposal，不是真值证明；coarse阶段漏掉的证据不能由后续fine检索自动恢复。[有限消融](https://arxiv.org/html/2602.22142v1)中，仅添加timestamp的微调会退步，顺序训练与history cache分别改变结果，仍不足以识别唯一视觉因果机制或所有任务收益。离线合成数据、额外训练、历史编码/KV与第二次回答都付费，阈值曲线和不同样本表格不授统一最优或真实deadline；检索失配、旧帧混淆或阈值失准时，保留固定近期窗口、更广原始历史与显式人工/外部查询，不将cache命中当作新观测。<!-- source-family:SF-2026-ARXIV-2602-22142 -->

拟新增正文与独立marker：

当输入不是预选的一条视频，而是多个可选直播视角时，观察选择本身会改变后续可见历史。可以先以低分辨率扫描所有当前视角，将决策分成保持现镜头或切换，再只为选中的视角读高分辨率并生成解说；未上播候选与真正上播/说过的内容因此有不同保留资格。[DirCast的有限分支](https://arxiv.org/html/2610.31734v1)让候选扫描缓存先过期，而节目历史保留较久，仍另设总 horizon 删除旧节目，不能把“program memory”理解为无限保留或任意历史无损。训练中扰动上播轨迹可暴露自选镜头后的状态偏移，目标仍来自人工节目与事件标签，不是部署时可读未来。它还消费当前游戏状态/事件，非纯像素多流能力；人工切镜一致、事件覆盖与解说质量也可能反向，不能把更多 kill 上播直接当更好导演。多流编码、二次高分辨率读取、训练和缓存维护都有费用，共享模型省权重不等全部处理免费；四场测试与八个短长流窗口的单 GPU 计算不认证整场 deadline。流来源/时间、镜头切换或状态支持失配时，保留固定已验镜头、显式窗口及人工导播，重新核已播内容与可用观测，不由 hold gate 或更短缓存批准事实与外部摄像机控制。
<!-- source-family:SF-2026-ARXIV-2610-31734 -->

完整后肩：

训练对齐的时序支持与推理时可见的输入前缀，是另一对不能合并的身份。跨语语音不必始终提供逐词源—目标对齐：可先保留 sentence 对应关系，为目标句首与句内停顿采样延迟，让训练数据包含源句尚未结束就开始输出的轨迹，再优化质量与语义 lag。放宽的是监督配对粒度，不是去掉 transcript、TTS 时间戳或 ground-truth reference；过程奖励可以使用当前已开始句的完整译文，却不能把这份训练标签解释为部署时已经听到的输入。<!-- source-family:SF-2026-ARXIV-2602-11072 -->

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-31734` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31734v1)§3/4.1–4.6/5.1及5.3/T3–5、5.2指标反侧必要，R127评分2+2+2=6。仅多流coarse-scan→hold/switch→选中fine与role-aware缓存；保currentgameevent/36s总horizon、perturbedprogram非未来输入、人工切镜/事件覆盖不等价、baselines人选节目/不同judge与有限match/window，不授纯视觉、长场SLO或控制权限。未核代码/设备/图像素或运行复现；原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。

### 21.4 32132 必要完成（6分）

[SyncPro精确2610.32132v1 HTML](https://arxiv.org/html/2610.32132v1)实际读§3.1–3.4拟采用机制/训练资格、4.1与4.3–4.4关键同formulation反侧、A的mask/位置/merge及streaming、B长流profile；不追加全C–F/代码或原数据。q+pastH+currentv同prefix，Inner/Response各silent/active且不读本turn另一branch；生成完整后按I再R进history，下一turn共同可见。1fps frameindex无drop/coalesce不是实时物理队列。Fullattn concat与共同MRoPEstart、nextmaxbranchlength；DeltaNet forkstate取均值γ.5是训练和推理相同heuristic，非serialcomposition/通用statesum。learnedmerge局部REC更好但其他变差，不授独一最优。

目标从physicallytruncatedprefix生成，offline fullvideoaudit/最多三修在对应prefix；innerstatecontext去旧视觉后可重建response是semanticjudge筛选，非独立记忆真值或全信息充分。合成137827/适配51576中8600jointactivations；只训练split/具体heldoutvideoID去交，未遍源视频或完整prompts。Qwen3.5-4B frozenvision/backbone，MLP双LoRA/actiontokens训练；对照samebackbone/source/budget，但interleaved联合机会仅保response目标，不把全部归并行本身。RL只800unique/50update timingF1且零KL，terminaladvantage遍两branch tokens，不是独立content保证；conditionalcontent与allpopulation分清，offline3bench均低原底座且无非劣证明。

samefixedmodel/mask并行与Inner-first同prefix在1870例greedy一致只验调度，不等串行互读语义。A最多256tokens/branch、B profile另cap64/W1/16384preallocated，不能把两个budget混速度。B BF16单stream480s/1fps，移除前两compile步，包含预处理/编码/共享prefill/双decode/merge/evict，不含disk/video decode或多流排队；retainedKV2126→11220、peak+0.88GiB，mean985ms/p901597ms/仅74.9%帧≤1s，绝非fixedallocation⇒boundedlongstream/SLO。完整硬件型号未在已读profile披露，记NotDisclosed不补造。只采用同prefix独立输出与合并合同及直接反侧，支持足停止。

### 21.5 32132 actualowner与整体三件PRE

实际owner `MULTIMODAL-REPRESENTATION` Ch23。复用本批完整StreamingIdentity与Ch22/24交接阅读，具体NC为视觉/文字logicalaxis、observationrevision、trigger/commit与framebudget已有；差额是Inner/Response同prefix互不读本turn、下一microturn同步合并以及hybridstate非serial的角色接口，非一般并行更快。PartV保留物理batching/队列owner，不重复写。root已确认02872完整拆分状态段后→06991逐帧chunk完整段前精确位无冲突；以下完整两肩与原三件交sole reader，未PRE不SAVE。

完整前肩：

拆分状态并不消除 frame 编码、KV 读写或同步成本。作者的指针级 cache composition 是实现主张，未在本次核验其 kernel 或并发一致性；3B 与 7B 的质量对照也不支持统一优胜。尤其 decoder 暖启动时的首 token 计时，不能直接替代从首帧到输出的端到端延迟，论文两处口径未充分一致，因此不采用微秒响应保证。观测持续改变、deadline 紧或快照语义不能确认时，保留逐窗口完整输入、串行 interleaving 或显式同步边界，再验实际 freshness 与响应成本。<!-- source-family:SF-2026-ARXIV-2603-02872 -->

拟新增正文与独立marker：

拆开观察与生成之后，内部证据更新与用户响应也不必争用同一条当前文字序列：两条分支可从同一已到达 frame 和历史前缀独立选择沉默或生成，只读自己的本轮 tokens，Response 不必等 Inner 写完才开始。但它也不能借用本轮尚未生成的 Inner 作为回答依据；两条完整输出合入历史后，才供下一 micro-turn 读取。[SyncPro的受限实现](https://arxiv.org/html/2610.32132v1)用角色 LoRA、block-causal mask 与共同时间起点表达这份合同；full-attention 可拼接两条 KV 增量，线性递归状态却用受训练的对称均值合并，不等串行处理或无损可交换状态。独立激活减少固定周期的冗余更新，仍需实际输出、时序和答案支持分别验收；两分支都完成再进下一帧的 barrier，也没有变成任意异步输入实时处理。该实现删除 frame KV 后仍保留文字，长期成本继续增长，预分配 cache 只稳住部分驻留；其单流长窗中仍有帧超过一秒服务预算。双路训练/生成、状态合并、缓存及独立评判均付费，冻结底座不保证旧任务无退步。合并语义、历史证据或预算失配时，保留串行 interleaving、较短显式窗口与外部 response gate，不由更早首 token 批准新证据已读、输出正确或实时 SLO。
<!-- source-family:SF-2026-ARXIV-2610-32132 -->

完整后肩：

帧到达时，还可让输出只推进一个受预算约束的token chunk，而不等整句说完再观察：scene-local context吸收新帧，控制器用ongoing prefix的相容性信号仲裁继续旧句、开启新响应或沉默，小pacer再提出本帧输出量。PPL只是相容性代理，转入Triggered也不是首token已交付；若视觉与verification已超过framebudget，截断后续生成无法补回deadline。语速/时间戳弱监督与固定token数反侧限制pacer的独立归因，语义突变快于utterance也会不断打断。逐帧同步累计比、首帧到末token吞吐和真实deadline须分开验，全部frame编码、验证、pacer与token/KV费用均计入；变化、质量或预算失配时保固定小chunk、显式同步/turntaking与旧前缀身份，runtime仍决定commit/cancel，不由并行叙事签发实时或事实保证。<!-- source-family:SF-2026-ARXIV-2606-06991 -->

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32132` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32132v1)§3.1–3.4/4.1/4.3–4.4与A同prefix mask/merge/streaming、B长流profile必要，R127评分2+2+2=6。仅独立Inner/Response与下一microturn合并资格；保本turn互不可见/两者finishbarrier、DeltaNet均值非serial、frameeviction仍text增长、frameindex非wall/480s单流仅74.9%达1s、offline退步与judge/data筛选，不授无损/实时/事实。未核代码kernel/设备或运行复现，不遍全部C–F。原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。


### 21.6 32784 必要完成（5分）

**Video-MemComp: Taylor-Guided Sensitivity-Aware Memory Management for Streaming Video Understanding**，[精确2610.32784v1 HTML](https://arxiv.org/html/2610.32784v1)实际读§3.1–3.3/Alg1–2机制、4.1setup及4.2关键RVS/效率与4.3直接消融、B.3.1 mass条件和C.1.2–3位置/幅值假设；够用即停，不全D–F/源实现或模型运行。Taylor把输出扰动近似为层内attention误差×下游敏感度之和，小扰动/局部线性前提，extremecompression本身承认失效，不作全局严格界。PreRoPE内容merge、跨帧动态保留/帧内bipartite软fusion并加log(count)；mass近似同时要求K_i≈K_c且V_i≈V_c，严格同响应才精确，不采用任意query严格mass。C1的局部R_pi≈R_pj/范数均衡有条件，满秩Wk不一般推出矩形投影双射，不采用普遍最优定理；此为所需边界而非宣称已修论文。

离线梯度norm先验、在线attentionentropy/logVnorm proxy及uniform混合预算，query是模板proxy非未来问题。不同模型lambda/过大onlineweight有反退；Alg2取整、Eq7可能负值/归一与总cap的实现闭合未核，不把预算proposal写成完整可执行recipe。硬cap/非负验证是项目从接口推出责任，不冒原实现已具备。评估采用developmentsets与模型特定参数，不证未知架构/分布；RVS的GPTjudge与OVO choice协议分开。RVS平均acc56.6低于ReKV59，分数3.2非全面优。A6000/LLaVAOV7B效率Mem16.74GB/frame64.92ms/TTFT.0302s但吞吐27.58低于ReKV35.61及无offload36.93；原baseline标OOM而另报局部指标，不推fullbaseline完成，精度/batch/并发/完整编码口径NotDisclosed。

关键反侧：同层压缩下static→dynamic在tau.75时Medium60.3→60.0，tau.90时60.7→59.9；All小增并非所有长度受益。加intraframe短程70.7→70.3而MLVU+0.51，不证无损/唯一敏感度因果；过强动态权重方差和激进时序融合均会伤质量。离线校准梯度、preRoPE维护与onlineproxy费用，cachecap不证总系统O(1)/长历史充分性。5分范围足，不因脆弱强宣传改全篇纠错/扩全部理论附件，只不采用这些强结论。

### 21.7 32784 actualowner与整体三件PRE

实际owner `INFER-KV-CACHE` Ch45，而非Ch23视频接口。已实际读Ch45 attentionmass、preRoPE calibration、Token×Featurebudget与合成KV/标量bias、KVCompose及EvolKV相关完整论证，Ch44/46开篇交接与本批Books背景/写作上下文。具体NC：预旋转内容/位置分责、校准绑定、按层数量proposal及硬cap、合成KV要合K/Vmass与完整费已有；真实差额为局部压缩误差×下游敏感度作为分层预算近似，并把其与preRoPE计数补mass条件联系而非普遍误差证书。root已确认EvolKV完整段/marker后→物理页布局段前精确位无冲突，只原一段/独立marker/本人注；未solePRE不SAVE。

完整前肩：

层间保留数量也可以先由小量有标签任务数据离线搜索，再冻结成线上cache配置，而不只能均分或按固定金字塔。[EvolKV的受限分支](https://arxiv.org/html/2509.08315v1)逐组尝试预算、以实际下游fitness反馈，再让既有token选择器按所得数量保留；搜索器拥有数量proposal，不拥有被删证据的充分性或层重要性的因果解释。校准人口、scorer、模型/tokenizer、选择器和预算映射应共同绑定；扩展旧配置到更大总预算仍需重新验硬容量，逐层向上取整不能自动满足总cap。部分任务与换校准人口会反退，离线平均好也不授未知query无损。全部搜索前向/标签、配置验证、压紧与独立质量回归均计费，局部推理不含搜索成本；任务支持或预算失配时，保留均匀/已验固定分配与FullKV，不由少量校准样本批准普遍质量或端到端省费。

<!-- source-family:SF-2025-ARXIV-2509-08315 -->

拟新增正文与独立marker：

层预算还可以从局部压缩误差怎样传到输出提出，而不只把各层相似度或近期性当作可直接比较的重要性。一次小扰动下的 Taylor 近似，可将层内 attention 误差与下游敏感度相乘；[Video-MemComp的受限分支](https://arxiv.org/html/2610.32784v1)据此混合离线梯度先验、在线 attention/Value 代理与均匀份额，提出逐层缓存数量。它并未得到所有未来 query 的最优分配：代理和校准会漂移，激进压缩时小扰动近似也会失效，最终仍须核非负数量、取整后的总 cap 与实际质量。层内在 RoPE 前聚合相近内容，并以融合数量的 log-bias 补偿被合并项，只在相关 Key 和 Value 响应都接近、位置影响可控时近似保留 attention mass；内容相似或投影满秩本身不授任意 query、任意位置的无损性。局部层预算与合并几何因此是相关但不同的误差来源，不能用一个平均分数认证充分性。离线校准、在线统计、聚合和重排均付费，受测模型中部分中等长度质量回退，token 吞吐也未统一优于保留更多 KV 的对照。敏感度代理、位置或质量支持失配时，保留已验固定分配、更细原位置记录或 FullKV，不由更小 cache 批准长流信息无损、总内存恒定或端到端 SLO。
<!-- source-family:SF-2026-ARXIV-2610-32784 -->

完整后肩：

层级选择还没有决定物理页应按什么排列。逻辑 token 顺序最容易维护因果身份，稀疏选择却可能在许多页上各取少量 row，造成大量零散 host→device 传输。另一条条件分支按每个 head 的 key locality 组织物理页，用近似索引提出候选；GQA 的多个 query head 共用 KV head 时先合并所需页，再由 host gather 到连续 staging buffer，经 bulk PCIe 传输后在 device scatter。改变的是物理布局与访问计划，不是原 token 的因果位置；cache manager 仍拥有 row/page identity、动态插入、索引版本及驻留有效性的验证。<!-- source-family:SF-2026-ARXIV-2604-10539 -->

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32784` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32784v1)§3.1–3.3/Alg1–2、4.1–4.3与B.3.1/C.1.2–3必要，R127评分2+1+2=5。仅Taylor小扰动localerror×downstreamsensitivity预算proposal及preRoPE聚合/mass适用条件；保K和V近似/局部位置与范数假设，未采用满秩投影⇒普遍双射/任意query最优/严格mass或精确预算算法。Medium反退、吞吐较ReKV低/未全费与校准漂移保留；未核代码kernel或运行复现、不全D–F。原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。


### 21.8 31734 R132后三件真实SAVE/完整自读

唯一reader R132必要6/actualCh23差额及§21.3原三件整体PRE通过，root22142→11072精确位已无冲突。作者仅原单段/独立marker/本人注apply_patch真实SAVE；正文2375/marker2376/本人注2656，完整新增/两完整肩/本人注与旧32411首注实际逐字读回match，marker1；剥本三件恢复fresh baseline `3d54a526f39629fb7e51028cb43caa4b749bee22926a83c995b38767abe10339`，限定Ch23 diffcheck无输出。现交soleactualPOST，不预I；32132/32784原稿待PRE，后两必要普通待办，不重既成层。


### 21.9 31734闭合；32132 R134后三件真实SAVE/完整自读

31734 reader R135 soleactualPOST通过，正式6分I/Ch23位释放。32132 R134必要6/actualCh23与§21.5原三件整体PRE通过，root02872→06991位已确认；作者仅原三件apply_patch真实SAVE，正文2411/marker2412/本人注2659，完整新增/两完整肩/本人注+旧31734首注实际逐字读回match、marker1；剥本三件恢复fresh baseline `2cd9946b968dd4e1e578ff304bfeb5591a11f6a468d3f37a66da19599b4faab5`，限定diffcheck无输出。现交soleactualPOST，不预32132I；32784已R135原三件PRE过，接其真实SAVE，不重复必要。


### 21.10 32784 R135后三件真实SAVE/完整自读

32784已按R135整体PRE与root具名位，apply_patch仅原单段/独立marker/本人注真实SAVE Ch45。完整新增/EvolKV完整段+marker及物理页完整段两肩/本人注与旧31827首注实际逐字读回match，marker1；正文221/marker222/本人注1893，剥本三件恢复fresh baseline `dfd73e7875f3d48a3f9831425e59440a83b2b6a7346527f139648987d5f6def2`，限定Ch45 diffcheck无输出。现交soleactualPOST，不预I；后两必要支持与关键反侧已足，actualCh23两位root无冲突，接原稿而非更多附件。


### 21.11 32664 必要完成（5分）

**The Answer Knows Where to Look: Zooming before MLLMs Answer under Visual-Token Budgets**，[精确2610.32664v1 HTML](https://arxiv.org/html/2610.32664v1)实际读§3的pre-answer/teacherforced定位与阅读反侧、4.1–4.5拟采用、5.1协议/5.2费用和5.3 T3–4关键直接消融、A训练/隔离/replace口径与E.S4因果mask和梯度条件、F及G失败文字；不扩全B–D/像素案例。Look位置专属offset与position-onlyLoRA，causal放最后；losslook后丢reader梯度，answerpass移look。**给定view**答案分布不依赖lookparams不等最终选择view后答案不变，reader仍另GRPO训练，不能写冻reader/无行为改变。训练从r≥.5至多两不同rollout取低清图teacherforced回答attention，平方锐化/KL；这是答案条件定位target，不是线上答案或truth。Outcome gate取消只70.6→70.2，不能把正确gate当已证关键；无sharp66.8，sharedattention69.5且single58.4<59。直接shared-attn监督在11设置8退，最多2.7点，不授所有模型reading必互斥定律。

Howview的MLP读lookhidden+八scalar、heldout10%选输入/weightdecay；另6000images×3budgets×8views全执行=144000answerpasses/model，用中心化taskscore训练actionhead；这些图片不用于RL，4500RLquestions/200step/8rollout，单seed0。八view可选none/crop/square/adapt/fovea，部署prefillpointer→原图transform重encode→answer两pass，默认answer两view，replace另训reader/actionset且仍两pass；不冒单pass或相同总预算。Qwen3VL2/4/8B、五text-richtasks，fixed500questions/publicset加300VCoTDoc，不把不同ANLS/relaxed/VQA/EM合单概率，TextVQA未训为局部OOD非全领域。

关键受控反侧：相同reader/view中adaptivepointer显益，固定crop/square有负格；actionhead在392的81.6低bestfixed82.2，4B主表392整体低bestbaseline.2，效益随informationgap收缩。给定viewreaderRL本身+1.1–1.5，不把全主表归pointer；correctnessgate很小与锐化更重要保留。Batch1/单RTX4090/4B/B196 tablecost默认565tokens/.35s高single194/.25与GapSight561/.33，但低AttWarp388/.60；replace388/.34不含离线144k采集，精度/并发SLO与完整图像IONotDisclosed。失败可plausibledistractor、tightwindow截字/正确框错行、极高图框太大无法放大；多区域/video仍future。支持足，停止全附件/代码；5分不因模型数或两pass抬reach。

### 21.12 32664 actualowner与整体三件PRE

实际owner `MULTIMODAL-REPRESENTATION` Ch23开篇局部信息/consumer链；已完整读序列化/可读信息probe→局部crop训练→撤提示课程及图表策略，并复用本批Ch22/24交接与Books背景。具体NC是注意力不等证据/训练特权不等在线输入、定位与answer分验、局部回读成本已有。剩余差额是hindsightanswerattention蒸馏到专属lookposition、参数与loss梯度和回答pass三重隔离，以及pointer集中性与view形状共同决定收益，不等旧objectcrop训练或纯提示课程。root已确认16586完整段/marker后→撤定位2510.04477前独立窄位无冲突；以下原单段/marker/本人注交sole reader，未PRE不SAVE。

完整前肩：

确认局部证据的消费可能受干扰后，还可把额外区域只用于训练，而不在每次回答时外部裁图：将原图中的 object crop 作为第二份视觉 query，要求模型在原完整图中找回其 box，以格式与 IoU 奖励训练，再回到普通全图—问题接口。[受限局部搜索对照](https://arxiv.org/html/2606.16586v1#S3)保留目标尺度地遮掉背景，支持检查上下文竞争而非只归因分辨率；但遮挡本身改变输入，定位正确、attention 入框和最终属性答对仍是不同证据。训练中更小的 cue 也并非越多越好，tiny-only 会损其他尺度的 grounding；有限模型的 OCR 与推理切片仍有退步。Object 标注/裁图、全部 rollout 与 reference、辅助 teacher、全图编码和新旧能力回归都计费，无部署 crop 不等免费获得新证据或所有细节可读。Cue、尺度或旧能力失配时，保留原模型/原图、较均衡定位监督与可信局部回读，另验答案，不让高 IoU 或更集中的 attention 替理解正确性签字。

<!-- source-family:SF-2026-ARXIV-2606-16586 -->

拟新增正文与独立marker：

另一条分支在部署时仍回读区域，却不让定位与阅读共用一份必须被塑尖的 attention：先以低分辨率图和问题运行一个专用 look 位置，让它提出 pointer 与视图类型，再从原图生成受预算约束的放大视图供回答。[LookZoom的受限实现](https://arxiv.org/html/2610.32664v1)用模型训练时正确答案的 attention 蒸馏这个位置，专属参数只作用于该位置，定位损失不更新 reader，回答 pass 也移除 look；这是给定视图下的参数/输入隔离，不表示选错视图不会改变答案。训练时逐一执行候选视图的结果，再教 head 决定不放大、裁剪或变形，属于有答案与多次前向监督的选择器，非线上已知正确证据。正确 rollout 筛选的独立增益很小，关键收益更多来自集中 pointer 与适配视图；固定窗口或细节已足时优势会缩小，过窄窗口还会漏行、截字。每视图相同 token cap 不等全请求相同预算：默认回答消费原图和放大图，单视图替换仍有前置定位 pass，训练与反事实视图采集也付费。预算、定位或阅读失配时，保留原图、已验固定窗口或更高分辨率并独立验答案，不由无部署答案生成、attention 集中或较少视觉 tokens 批准证据充分与通用无损。
<!-- source-family:SF-2026-ARXIV-2610-32664 -->

完整后肩：

撤去可见定位提示，还不等于撤去定位监督。一个[受限视觉grounding课程](https://arxiv.org/html/2510.04477v1#S3.SS2)先让输入带框并联合学习答案、rationale与区域锚点，再去掉可见框却保留attention-mask和rationale监督，最后才只按答案训练；三阶段分别改变模型看见什么、由哪些标签约束，以及哪些输出被奖励。更弱监督并非自然更好：加入最后阶段在部分QA切片退步，最终答案概率选出的理由也不认证推理真实，训练loss差更不是校准难度。框/分割与teacher生成、分阶段训练和原任务回归均计费，输入可见性、监督来源和consumer要一起保存；证据噪声、领域变化或质量反退时，保留较稳定的显式/隐式定位阶段、原图与独立答案核验，不由更少可见提示、BLEU或attention入框批准临床、物理或通用推理可靠性。<!-- source-family:SF-2025-ARXIV-2510-04477 -->

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32664` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32664v1)§3/4.1–4.5/5.1–5.3关键T2–4、A隔离/训练与E.S4、F及G失败文字必要，R127评分2+1+2=5。仅hindsight→look-position独立参数/梯度/回答隔离与counterfactualview消费资格；保sharedreader仍GRPO、正确gate小益/固定窗口和高budget反退、2pass与perview非总tokens、144000offlinepass/单seed/五text-richbenchmark和漏/截/错行。未核图像素/源码或运行复现、不纳视频/多区域未来外推；原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。


### 21.13 31768 必要完成（5分）

**Efficient Omni-modal Large Language Model Inference via Per-Query Modality Selection**，[精确2610.31768v1 HTML](https://arxiv.org/html/2610.31768v1)实际读§3.1–3.2/Eq2–8机制、4.1–4.4/Eq10–12与T1–2关键评价/反侧、A.1–2 runtime与价表、B.oracle及C限制；未扩tasktype全部任务/无关router附件。固定Omni f，对训练样本枚举候选结果/成本，label为argmax(correct−λcost)，weight=best−runneruputility，用weightedCE训router；线上只h(q)预测，λ变化另训，不是一次阈值保证全预算。**理论采用边界：**原Lemma1/Eq5把给定h的最优写为逐q/已实现正确性argmax，proof在q条件下逐点选择，未保证压缩h能区分同特征不同q/标签；已知y实现值也不一般替条件期望。故不采用其强Bayes最优/一致性，拟长期命题仅经验utility-gap监督与线上资格，需条件分布/表示支持是本人的有界数学辨析，不补造原定理。权重归一全零等实现未核，不发布精确recipe；这不否定受限实证而无需把全家族改H/扩大所有理论。

实测不是全部2^M子集：仅TA vsTAV，BGE-M3以question+四options1024d归一embedding，singlelinear/100epoch，线上不读audio/video/答案决定。Qwen2.5Omni7B BF16、Qwen3Omni30BA3B autoprecision，单H200，greedy/thinker16/newtokens32，答一个option；两模型processor各defaultframebudget，audio16k，promptheader还随模态改变，不作同tokenizer/同帧的架构因果优胜。WorldSense70:30 train/test，各方法同test；video级隔离、splitseed/CI未在已读协议披露，不冒无leak/多seed稳定。Oracle用groundtruth两输入结果59.03%/8970token是上限线索而非可部署router。

关键评价：三费用各自Pareto curve对commonTA–TAV区间做线性插值、TA锚/尾段水平延拓，normalizedAUC及matchTAV48.00/51.79%均是平均操作前沿，不是每题同质/独立锁阈值的部署证书，未披独立validation选operatingpoint。Qwen2.5 match时tokens−58.89%、latency−61.07%、money−38.94%，Qwen3较小，不能借主摘要扩大；inputtoken/局部latency与estimateprice不同单位。Money用另一Qwen3.5OmniPlus国际价表1.4/11/1.4e−6算T/A/V输入，非这两本地模型发票/全输出费用。Router编码/label双前向/训练、loading、完整IO并发SLO是否计入latency未闭，NotDisclosed不补估。Verbalizedcascade两模型三费均比alwaysTAV高，logitcascade2.5钱也反增，信心非可靠必要性。额外视频可能使有限模型改错不等视频无信息/消因果，回退也是需验的固定输入。支持与反侧足停，不读全部任务表或代码。

### 21.14 31768 actualowner与整体三件PRE

实际owner `MULTIMODAL-REPRESENTATION` Ch23 Latefusion的“读哪些输入”合同，非Ch56跨请求调度或模型选择普遍理论。已实际读本节从独立encoder/latefusion、2610.24108对齐/consumer到CoM两个完整输入/派生描述段、后续内部向量，以及GeoSense双条件标签/2510.01681刷新调用规则相关完整论证，复用本批Ch22/24交接。具体NC是queryplanner/小集合非充分、额外模态可退、双条件标签绑定策略与全费已有；真实差额为fixedOmni外仅文本输入的utility-gap加权TA/TAV分流，把hindsightoracle与可用特征、均值预算前沿与逐题/锁策略资格分开。不是把成熟成本优化原则算新贡献；也不以一般NC覆盖掉新增不对称标签/经验反侧。root已确认CoM第二受限对照完整段后→内部向量2604.22560前位无冲突，以下原三件交sole reader，未PRE不SAVE。

完整前肩：

[CoM 的受限对照](https://arxiv.org/html/2604.14520v1)支持按问题比较这些分支，但部分固定拓扑、prompt 和模型仍更好；增加 reasoning 并非单调收益，Omni 配置的总推理时间还会上升。分角色提示可以复用同一 backbone，却不免 planner、各模态读取与汇总的多次调用；并行阅读只隔离本次输入，不证明跨模态语义独立。应分别保存原信号、片段对应、拓扑与派生描述，验收最终答案和总费用；模态选择漏证、对应失真或文本描述不可靠时，回读原始输入、采用已验证的固定融合或独立感知路径，而不把原文无效规划时的 Audio→Visual 默认次序当通用安全回退。

拟新增正文与独立marker：

若只需决定是否补读一种昂贵模态，planner 也可换成在固定主干外训练的成本敏感选择器：先离线测同题在候选输入下的答题结果与费用，用“正确性减成本权重”的最佳候选作标签，并按最佳与次佳 utility 差加权，让漏掉必要视频与多读无用视频不必付同一训练代价。[一项受限 Omni 对照](https://arxiv.org/html/2610.31768v1)只用问题和选项的文本 embedding 选择 TA 或 TAV，不改 Omni 主干；这是是否补视频的预测，不是已看完音视频后的证据充分性判断，更未验所有模态子集。标签使用已知答案，线上却只见压缩后的文本特征；不能把逐题 hindsight 最佳动作写成该特征下必可实现的 Bayes 最优，也不能把加入视频偶尔使答案变差解释为视频没有信息。成本权重、模型、processor 和任务分布改变都需重校准；匹配全模态平均准确率的 Pareto 插值也不保证每题不退步或一个预先锁定策略满足预算。双条件标签制备、文本 encoder、路由训练/推理及必要回读均付费，输入 token、局部延迟与按另一服务价表估算的钱不是同一份完整账；自报信心的 cascade 甚至会更贵。选择支持或质量/全费失配时，保留已验固定输入和补读/独立答案核验，不由低费用或 frozen backbone 批准模态充分性、全域无损与服务 SLO。
<!-- source-family:SF-2026-ARXIV-2610-31768 -->

完整后肩：

阶段间也可传内部向量而非生成的perception文本，但必须先声明状态在哪个时刻捕获。一条受限分支从上阶段最后的nonvisual、nonpadding prompttoken读取hidden，经可训练投影与小gate注入下一阶段；因果prompt状态尚未见随后生成的answer，不能称传递了那份完整答案或其推理。[驾驶VQA的有限比较](https://arxiv.org/html/2604.22560v1)将这种接口与显式文本链分开，后者与隐式链又用不同模型/适配配置，不能合成单一因果优越。近恒定gate也不是已验证的动态语义router，跨语NLI一致率、较短答案与真实grounding/驾驶安全仍是不同对象。状态token、producerprompt/checkpoint、投影、freeze顺序与consumer输入须共同绑定；多阶段前向、adapter训练和独立原信号核验均付费。语言/输入漂移、一致性或任务质量退步时，保留原始六视图、已验固定融合/文本接口与独立答案核验，不让隐藏向量接力签发新增观察、内部推理忠实或闭环行动安全。<!-- source-family:SF-2026-ARXIV-2604-22560 -->

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-31768` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31768v1)§3.1–3.2/Eq2–8、4.1–4.4/Eq10–12/T1–2及A.1–2/B.oracle/C必要，R127评分2+1+2=5。仅frozenOmni外textonlyTA/TAV utility-gap加权预测；不采Lemma1将逐q标签等同压缩h(q)可实现Bayes最优，需条件期望/表示支持，原件该强式不授。保question+options/70:30非视频ID去交证明、两模型processor不同/单H200与有限输出、testPareto插值非锁策略/逐题非劣、另一服务价表估算/全费未闭/自报confidence更贵。未核源码/原数据或运行复现；原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。


### 21.15 前三真实闭合；32664 R142后三件真实SAVE/完整自读

32132 R138 actualPOST6/I、32784 R139 actualPOST5/I已过，前同31734R135全部三项正式生效/位释放，不重复必要。32664 R142必要5/actualCh23与§21.12原三件整体PRE通过，root16586→04477精确位已协调；作者仅批准单段/独立marker/本人注apply_patch真实SAVE。完整新增/16586段+marker及04477完整后肩/本人注+旧32132首注逐字实际读回match、marker1，正文57/marker58/本人注2662；剥本三件恢复fresh baseline `e85eadbf14119b62d75ee7a623218c3e9d691e851687c1ec72e7c7b75608e9ba`，限定Ch23 diffcheck无输出。现交soleactualPOST，不预I；最后31768原三件仍待PRE，不扩Methods。


### 21.16 32664真实闭合；最后一项普通待核

32664 reader R144 soleactualPOST实际核完整新增/完整两肩/本人注通过，正式5/I Ch23生效，精确位释放；前三项R135/R138/R139已成，不第三必要/POST。当前本批4I，31768必要5/actualCh23原三件已交、等待solePRE，未SAVE，仍普通可执行审阅/写后待办，不记H或本批完成。root后授32941/31859/32102/32969/32348仅排队，待31768闭合后另节先按实际命题评分；尚未读新五Methods或扩AB/date，不以新授权混淆当前分母。


### 21.17 31768 R146后三件真实SAVE/完整自读

唯一reader R146必要5/actualCh23与§21.14原三件整体PRE通过，rootCoM第二完整段→22560精确位已授；作者仅原单段/独立marker/本人注apply_patch真实SAVE。正文1211/marker1212/本人注2665，完整新增/两完整肩/本人注+旧32664首注实际读回逐字match、marker1；剥本三件恢复fresh baseline `22db70356001f5947437341b8828b9dc5ce09642f4a2e21da565c2e675adc1dc`，限定Ch23 diffcheck无输出。现交soleactualPOST，不预本项I/本批完成；本批其他四actualPOST有效不重核，新五仍未开始Methods。


### 21.18 本批五项全部真实闭合

31768 R152 soleactualPOST正式5/I通过，完整原新增/两完整肩/本人注与限定diffcheck已实际核，最后精确位释放。本批最终5唯一家族全部最低必要→actualowner具体差额→原稿PRE/真实SAVE/完整自读/唯一POST闭合：31734 6/I Ch23 R135；32132 6/I Ch23 R138；32784 5/I Ch45 R139；32664 5/I Ch23 R144；31768 5/I Ch23 R152。当前最终正文/marker/本人注分别31734 2381/2382/2671、32132 2417/2418/2669、32784 221/222/1893、32664 57/58/2667、31768 1211/1212/2665，后续并发行号可移动但独立marker唯一。全日Report/State仍归root，不假本日完成；本批普通待办0，未stage/commit/push或写其他日期。按root后授另接下一五，旧必要/POST不重。

## 22. 代理下一五项：VLA恢复、数值精度与执行记忆（Methods前评分）

只接root具名32941/31859/32102/32969/32348，仍Daily2026-10-27/BJT Oct26完整日；换批已重读AGENTS与当前研究合同，其他本日未变适用合同/来源/ROADMAP/背景与checkpoint沿本批已完整实读有效层复用。SOURCE/ARXIV_B原完整题摘、公开日/去重/准入沿用，不扩列表或AB请求。以下评分先于原件Methods；旧ARXIV_B评分仅准备态，按实际拟采用命题重新限定，不因阅读成本/Books状态降分，不先断I/NC。


### 22.1 五项三维评分与最低必要

| 精确已核身份/题名 | 新增命题与维度边界 | 分数与最低阅读 |
| --- | --- | --- |
| [2610.32941v1 — If at First You Don't Succeed, Backtrack: Lightweight Recovery for Frozen VLAs](https://arxiv.org/abs/2610.32941v1) | 冻结policy越出训练态不必只等重训；内部representation的failurehead触发对已达动作轨迹回溯再交回原policy。D2推理恢复执行接口；R2检测状态→真实动作回溯→policy再入的边界，不以机器人或冻结名词扩3；U2可复用检测/恢复资格。 | **2+2+2=6**。核head标签/阈值与可逆/已达动作边界、reentry/恢复耗时和失效反侧；物理回溯不能因已执行便安全，深入所涉控制域但不全机器人附件。 |
| [2610.31859v1 — Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates](https://arxiv.org/abs/2610.31859v1) | 原bf16artifact不能反推训练更新精度；缺fp32master让小AdamW更新在写回时丢失，matchedruns与actionhorizon改变收益。D3具体数值实现纠错而非基本浮点舍入原理；R2optimizer更新→trainableweight持久化→执行policy评价的实际接口，不因能映所有训练层加3；U2受参数格式/步长约束的稳定条件，不借成熟精度原则算3。 | **3+2+2=7**。深入受影响更新路径/recipeaudit事实权限与matchedLIBERO、master-voptimizerstate/LoRA和horizon关键反侧，不审全部框架/完整运行复现。 |
| [2610.32102v1 — Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies](https://arxiv.org/abs/2610.32102v1) | 积分步数与执行horizon不能独立调：粗解在快重规划伤precision却在长openloop改善成功，centroid近似不变而lateraldispersion收缩。D2重要solver/方差取舍；R1同一VLA actionchunk的采样/执行参数组件，不把模型与控制两名词自动跨系统；U2可复用的联合调参条件。 | **2+1+2=5**。核sampler/初始噪声/步长与horizon受控配对、分布变形证据和任务/费用反侧，不全solver研究或轨迹附件。 |
| [2610.32969v1 — DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection](https://arxiv.org/abs/2610.32969v1) | samehand便携skillinterface同时记targetcommand与measuredstate，BC不消费skilllabel而不同actiontarget改变成功。D2数据动作语义的实证界，不以硬件新颖打分；R2采集端目标/状态日志→训练actionlabel→同hand执行消费者真实交接；U2可复用的command-v-state条件，不授异构robot普适性。 | **2+2+2=6**。核target/测量采样和skill控制/BC接口、command-vstate关键对照/任务与数据成本反侧，不全硬件装配或所有skill附件。 |
| [2610.32348v1 — LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners](https://arxiv.org/abs/2610.32348v1) | 每步改写notes会丢执行事实且全帧昂贵；appendexecutionlog/保旧notes，planner按预期change选帧/示范snippet，改变事实/派生状态消费与预算接口。D2执行记忆分工及局部读取机制；R2观测/执行log→派生note/context→下一planner调用的具体交接，不把一般memory分层原则算3；U2可复用事实与派生状态边界。 | **2+2+2=6**。核何者append/谁改notes、frame与snippet选择的可见性/失败边界、matchedplanner/预算和关键退步，不全robotepisode或prompt附件。 |

五项均保留，不为凑低分或减少投入调整；与旧拟分相同不等默认6。准备层本身不证必要或I，评分校准后按实际命题支持/关键反侧足即停；如发生具体实现冲突仅受影响域加深，不全Methods队列。


### 22.2 32941 必要完成（6分）

**If at First You Don’t Succeed, Backtrack: Lightweight Recovery for Frozen VLAs**，[精确2610.32941v1 HTML](https://arxiv.org/html/2610.32941v1)实际读§3机制与4协议、5.1–5.3主对照/检测及5.5所需阈值规则、6.1–6.2与A.6直接特权恢复反侧；不全feature/controller格或机器人附件。MAP+三层FFN只读已算postprefix，actionchunk一次，不额外baseforward但head非零费；训练将episode最终成败赋各frame，平衡八suite×labelcell，不是当前失败原因或自然prior下校准的证书。Smol/FAST/pi.5 rollout20k/7953/14k与100kframes/policy，head20ksteps，而非免训练。在线超过阈值固定退步或较低restart阈值/最短最长adaptive，cooldown/cap限制再触发；只把正常policy中achieveddelta入buffer，backtracking不追加，命令若被blocked不能逆出不存在运动。LIBERO绝对gripper倒序重发会越过抓持时再打开，MetaWorld增量negate；近似跟踪/物体被移或接触不可逆，不是fullstate rollback，未将源码未闭buffer精确pop/并发协议补成recipe。

关键协议：LIBERO四suite、五seed/每task50eps，same双wrapperstepbudget560/600/1040，retreatsteps计入，非baseline原budget更短；Long用1000–3000seed选配置，4000–5000未选且单独uplift更小/近似，五seedheadline不是五全heldout。Smol原10flow/每actionreplan改2flow/执行10action，也用于control，不泛称原checkpoint官方速度。Long三policyfailure下降19–48%是net uplift/basefailure非逐失败恢复概率；shortSmolObject−.20、FASTSpatial−.36/Object−.20。No-trigger99.7%以上是干预后条件人口，不能推必要性；pi.5 offline2772episode135failure AUROC.977不等frame.908，在.99阈80%detect/2%falsealarm，.9阈96%/6.1%，FPr与实际打断费需分开。

关键直接反侧：pi.5 adaptive t.9是−1.92pp，fixed同阈+.84；低阈/长退耗时解释未隔离于时刻/state，不能作唯一cause。Postexpert差不可分不授表示因果；重试差异可能arm/scene/noise多来源，未识别唯一机制。A6同operatingpoint executable+2.80 vsprivilegedrestore+5.72（差CI正）同时改变返回精度/回退耗时/环境演化，是simulator特权而非可执行改进；所有主结果也simulation，无physicalrobot。参数增量≤.88%不等墙钟/碰撞安全，computeGPU集群说明无精确precision/并发tail，NotDisclosed。不需后续完整A7/8表才采此有界机制；支持/反侧足停。

### 22.3 32941 actualowner与整体三件PRE

实际owner `MULTIMODAL-EMBODIED-VLA` Ch26 Reset-free节，已实际读该完整两段与相邻离散SafetyFilter/可达域、开篇proposal/controller及freshness/chunk责任并读Ch25/27交接，Books适用上下文复用。具体NC是可逆性非任意环境reset、absorbingfailure/独立controller与停机/成本已有；差额是episode预测head与实际达成运动日志的恢复primitive、command-vachieved/gripper与近似重入、trigger条件人口/物理返回非特权瞬移，不是原oracle隔离的复述。root已确认17745第二完整段后→SafetyFilter标题前精确位无冲突，只原一段/marker/本人注；未PRE不SAVE。

完整前肩：

恢复动作、oracle 和隔离试验会增加环境建模与操作成本，也不能证明开放世界的全部回路可逆。现有 multi-engine benchmark 只支持其定义的 reversibility axis；恢复不可达、oracle 不可信或物理后果不可撤销时，应停止在线学习、人工复位或回退冻结 policy。<!-- source-family:SF-2026-ARXIV-2609-17745 -->

拟新增正文与独立marker：

不重训原 policy 的恢复，也可以只尝试回到较早的机械臂配置，而不假定能够 reset 场景。[Backtrack的受限分支](https://arxiv.org/html/2610.32941v1)从冻结 VLA 已计算的表示训练 episode-outcome failure head，超过阈值后暂停 policy，反放正常执行中实际达成的位姿增量，再以新观测交回同一 policy；被障碍挡住而从未发生的命令不能拿来反放，夹爪的绝对或增量语义也须分别处理。这个返回仍受跟踪误差影响，既不恢复物体位置，也不撤销接触，回退过程还可能继续改变场景；低 failure 分数只是重入提议，不是安全可达或任务可解证书。训练将整段最终成败赋给各帧并平衡来源，检测到未来失败不等识别当前可恢复原因；从无 trigger 人口的高成功率也不能推出每次干预必要。固定步数与带滞回的自适应回退共享执行预算，较低阈值下后者会反退，短任务亦有负收益。原对照只在仿真中计回退 steps，特权瞬时恢复的更高成功还混合精度与耗时，不能替真实反向轨迹。Head/rollout训练、检测、全部退让和重试均付费；不可逆物体变化、跟踪或预算不合时，保停止/人工复位与已验 controller，不让曾走过的路径或冻结权重绕过独立 safety envelope。
<!-- source-family:SF-2026-ARXIV-2610-32941 -->

完整后肩：

### 离散控制周期要为 Safety Filter 预留一步可达域

连续时间 safety filter 在任意时刻可介入的假设最清楚，但数字 controller 只在离散采样点更新动作；若危险状态能在下一个周期前进入，等到边界触发已经过晚。一个更保守的分支按最大一步可达集合向外扩张 unsafe region，让 filter 在当前周期提前接管。扩张减少 late intervention，却会增加 false positive、保守轨迹和模型误差敏感性。

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32941` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32941v1)§3–4/5.1–5.3及5.5关键阈值规则、6.1–6.2/A.6必要，R154评分2+2+2=6。仅episodeoutcomehead→暂停/achieveddelta反放→fresh重入冻结policy；保balanced未来标签非当前cause/校准、gripper本体语义/近似返回非scene reset、低阈adaptive负与短suite反退、同doublebudget退步计费/heldoutseed有限与privilegedrestore混杂。全部仿真/未实机安全、wallhardwareprecision未闭；未核源码/全图/运行复现，不全A1–8。原三件PRE/SAVE/selfread/solePOST依后到事实，不预签。


### 22.4 31859 必要完成（7分，受影响数值路径深入）

**Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates**，[精确2610.31859v1 HTML](https://arxiv.org/html/2610.31859v1)实际读II浮点/AdamW幅度界与step probe、III pinnedrecipeaudit/Hub权限、IV matchedLIBERO/重训horizon/统计与VI直接限制/修复内存边界；不扩所有框架源码或作者私有日志/训练。Round-to-nearest BF16相邻格距与|w|相关，<|w|/512必丢是保守量级，半ULP依bin/方向；master中累计但compute cast看不见与直接round丢掉是不同路径，未把LoRA默认lr更新不丢推广至更小updates。E(u)只从weights估双符号不动比例，bound要当前weights和每元素step≤cη、β1²<β2（.9/.95c1.165），β2.999用η时仅estimate；bf16moment极值1.202η来自有限梯度search非全输入定理，releasedweights与当前weights不同且另由probe检验。Decay separate乘法可被独立round，fusedcombined路径不同。作者每100stepcopyweights看stored值unchanged，非所有unchanged均非零梯度被丢；pi.5剔除多数无gradientembedding仍≥95.8%，支持此局部解释，不冒全部标量非零update计数。

Audit12 pinnedcodebase9有bf16无master/default或documentedrecipe，其中4fullweight/5LoRA，不能将9全作fullweight故障；论文记录LeRobot b9cb121/runtime构建使Smoldtypeflag表面float32却expert继承bf16，pi.5configdefaultfp32但guidebf16是另一入口。此为作者核验，不冒本人已读当前code/复现runtime；本次不采用具体CLI一行修复。Oct16 Hub随机300各模型、tags由上传者自填，bf16fileheader99.3%或config84%不证明每份原训练路径；40expert矩阵同base bitidentity是间接信号且addedafterwardcheck，非独立全体训练audit。

Matched必要：Smol454Objectdemo/10kstep/b16/β.9,.95/相同bf16autocast和初态/推理dtype，storage三组而moment也随dtype变，模拟平均差<.2%不是独立实训消融。三Smolseed、两pi.5seed；外部注册无，datedprojectlog多前置但部分pairedtests/postdispersion后加。Smol50openloop headline69.5vs59.3/+10.2，低率49.3vs4.3/+45.1但两边undertrained；重训sameGPU/seed10actionreplan gap只4.2<预定10pp阈，原训练checkpoint未保。ScorerSmol原50chunk没过先验88check，另checkpointcheck半程止/未按plandebug，**仅paper内配对，不与原榜合并**；pi.5scorer99.2接近99。Pi.5generalbase非guideLIBEROtrainedbase、2500step/b32短训，相同初始bf16round后castmaster比89→97.7/+8.7低large阈，lowerlr5.1→80.9也undertrained且GPU换；pairedsignificance不等预定large/跨训练seed普遍性。原bf16已99.2的同suitecheckpoint说明不能声称bf16不能学任务。

适用/成本反侧：lr各自最优sweep未做，高lr补偿bf16是否等master不知；VI还给探索性另一LM高率masterheldoutloss反更差，保局部而不扩该外文为本日候选。SmolRTX4090、pi.5H100default/Blackwelllow不同硬件，精度bf16compute但runtime/concurrency不是生产SLO；单卡master额外.8GB与pi.5约75GB含checkpointing/逐tensorAdamW有配置限定。fp32写回修复会增effectiveupdate，原LR需再调；gradientchain下溢非同storebug，weightmaster/moment/compute分开，residual/stochastic在该VLA实验未测。仅采用实际写回/可累积状态和消费者条件，不采全框架黑名单、所有seed大涨或一行热修保证。所需证据与直接反侧足，7分不要求遍全部code/私有log；剩余本人未复现是边界非外部H。

### 22.5 31859 actualowner与整体三件PRE

实际owner `TRAIN-PRETRAINING` Ch28通用Precision/optimizerwriteback，而非Ch26机器人产品配置或Ch41框架手册。已完整读Precision compute/master/moment/accum与FlashOptim residual、FP4operator路径/格点master移动的相邻论证及optimizerstate round误差段，读Ch27/29开篇交接，背景/理念/写作指南本日有效。具体NC是dtype身份、精度路径分责、弱更新残差累计与状态费用已有；真实差额为compute暂不可见vs实际writeback丢弃、step前后实测与staticE资格、master修复需重新验有效lr和actionhorizon而非低loss或bf16artifact认证。root已确认BF16实际dtype完整段后→FlashOptim residual/moments前无冲突，仅本原一段/独立marker/本人注；未PRE不SAVE，不把本短实证替换旧多条精度机制。

完整前肩：

所以“模型以 BF16 训练”并不能唯一确定每份状态的 dtype。Checkpoint、optimizer memory 估算和 collective bytes 都必须基于实际 precision policy。

拟新增正文与独立marker：

还要把低精度 compute 暂时看不见更新，与 optimizer 写回时真正丢弃更新分开。若 trainable weight 本身是 BF16，且没有高精度 master 或误差残差，round-to-nearest 可让小于该权重半个 ULP 的 AdamW 更新写回原值；较低学习率因此未必只是更温和，也可能进一步降低有效更新率。[一项 VLA 精度审计与受限配对实验](https://arxiv.org/html/2610.31859v1)发现，配置名称、autocast 与保存的 BF16 artifact 都不足以确定 optimizer 构建时实际参数、moment 和写回路径，loss 仍下降也不排除大量权重原地不动。应同时检查实际可训练参数 dtype、是否保存可累积的 master/residual，并在受控 step 前后 probe 存储值；仅从权重分布估出的不可动比例还依赖更新幅度界、当前权重和 rounding 条件，不能直接作每步实测。保留 FP32 master/参数并低精度计算能避免这条直接写回路径，却增加状态内存并改变有效步长，原学习率须重新验，不能宣称任意任务都更好。受测成功差额随执行 horizon 缩小，低率大差额来自未充分训练的模型，moment 精度也未完全独立消融；同一 BF16 计算路径下的配对结果不授全部 framework 故障或通用倍率。更新支持、恢复或质量失配时，保已验高精度状态和匹配预算的训练/真实消费者回归；残差或随机写回是另需验收的替代，不由不报错、低 loss 或较小显存批准训练正确性。
<!-- source-family:SF-2026-ARXIV-2610-31859 -->

完整后肩：

进一步压缩 master 与 moments 时，两类误差应分开：BF16 权重外另存按该权重 ULP 半区间归一化的 signed residual，帮助累积弱更新；momentum 则先 absmax-normalize 后做 softsign companding，variance 先 sqrt 再分组整数化，以把 bin 分辨率分配到实际状态分布。每步局部重建、普通更新、重新编码，并非改变 AdamW objective 或无损保存 FP32。[FlashOptim v1 §3–5](https://arxiv.org/html/2602.23349v1)的有限 matched-control 支持状态分布影响稳定性，但梯度精度亦不同，optimizer-step 变快不等全训吞吐，部分配置直接更慢。Residual、两个 group scales、padding 与 checkpoint 都须进账，FSDP 只通信 BF16 不使 local residual 消失；零组处理、signed 编码与极弱更新仍需验证，伪码没有给全输入保证。Activation 主导或敏感任务下节省可变小，量化/解码/融合与回归费均在；恢复身份、状态精度或质量不稳时，关闭压缩或保留 FP32 master/较高精度 moments，而非从整数位数自签训练恢复等价。<!-- source-family:SF-2026-ARXIV-2602-23349 -->

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-31859` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31859v1)§II–IV/VI及相关VI写回/替代界首次必要，R154评分3+2+2=7。仅BF16实际trainable-writeback弱更新丢失vsmaster累积/step probe与LR/horizon消费条件；保E界当前权重/Adamβ与幅度搜索条件、Hubartifact非训练证、authors pinned审计非本人runtime、Smolscorer未过/shortschedule/低率undertrained/多硬件/两三seed、moments未独消融/高LR补偿未测。替代residual/stochastic未在该VLA实验验证，不授全域收益/安全训练或修复recipe；未索取私有logs/核源码/运行复现。原三件PRE/SAVE/selfread/solePOST按实际后到，不预签。


### 22.6 32102 必要完成（5分）

**Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies**，[精确2610.32102v1 HTML](https://arxiv.org/html/2610.32102v1)实际读III-A–D公式/Prop1假设、IV-A factorial协议及关键主行/IV-B matchednoise/scalarrescale与noiseredraw反侧、IV-C硬件/动态边界；不扩solver全部研究/项目代码或轨迹像素。N是覆盖1→0全区间的均匀Euler步数，s是预测H内执行prefix，不是停止在早期flowtime；time与物理step分开。高斯线性路径affinevelocity下centroid精确不变与rho(N)乘积/极限成立，不推任意非线性VLA定律；原文‘earlytruncation只取initialphase/strictlyonmanifold’叙事不由此证明，不采用通用on-manifold或高阶必不稳。

固定观测/pairedGaussiancloud中N2vs10半径约.51，但centroid仍有约3%偏移、最佳scalar留下48%variance未解释（pi.5另53%），是结构变形非单一varianceknob；不拒单峰也不证明真实unimodality。SingleN1明显失真/99%variance不可scalar解释，不能从解析rho1=0延伸为无害零噪声。LIBERO-Long pi0配对7/8/9 shallow短s5−2.7、长20约+3.7/interaction+6.4；GR00T长s8仍−1.8，interaction正不等longgain为正。pi.5受H10ceiling不声称所有模型反转。Scalar initialnoise匹配radius却加centroiddrift/更差，freeze acrossreplans深短81.2→42.3，支持重抽依赖但不是唯一几何因果；两干预均还改变轨迹分布，不作独立全部机制证明。

Runtime/评价边界：A100/官方releasedpipeline；LIBERO每suite500、若干heatmap是单seed而factorialmatched3seed，RoboTwin50task100matched/task，表文‘55simulationtasks’与40+50未闭，不用总数作覆盖结论/不补查新任务。主表各backbone原H/N不同，原架构若干描述不用于事实。RoboTwin pi.5(25,2)70.8低(10,10)73.8，文‘maintains’不授非劣；1NFE非fullmodelcost，pi0percall45.93+2.57N ms再/s得到局部摊销，5.6×非query/IO+controller总速度。Franka3/25Hz Cartesianimpedance/ZEDRGB+proprio、每task50demo并有模型FT、四cell各40physicaltrial，采用trainingfree仅指变更N/s，不等模型没训；动态图5RPM长openloop各N均失败。精度/batch/并发tail与thermal测量未披露，不纳消throttling/完整SLO。所需机制/关键反侧足停，5分不因更多task/层数升级。

### 22.7 32102 actualowner与整体三件PRE

实际owner `MULTIMODAL-EMBODIED-VLA` Ch26 ActionChunk节。已实际读完整chunkcontract、2610.25961temporalgranularity、metareasoning/ADP及2606.14375 jointK/C、后续p/e与AutoHorizon/样本不确定性论证，Ch25/27交接本批有效。具体NC为compute与执行承诺分责、NFE/实际步/全墙钟不同、jointbudget与短反馈/独立controller已有；差额是固定均匀solver深度本身改变输出云几何，受控N×s收益符号反转及其Gaussian/非标量/动态失败条件，非再写一般联合调参。root确认14375完整段/marker后→p/e完整段前位无冲突；原一段/marker/本人注交sole reader，未PRE不SAVE。

完整前肩：

对冻结的生成式动作policy，计算预算与执行承诺还可以是两个独立选择，而不只用同一个等待长度表示：外部adaptor共同提出latent steering、去噪步数K和本次执行prefix C，再由原sampler生成动作。[受限联合调度分支](https://arxiv.org/html/2606.14375v1#S3)用critic分歧提议多计算/短承诺的工作点，但分歧不是物理危险真值，也不保每项任务更好。Replay应保存实际执行步数L和终止，以相应低层步时钟折扣；请求的K/C预算、实际K/L摊销与完整墙钟仍是不同分母，不能用少NFE替controller deadline签字。离线专家轨迹也没有替代schedule下的真实反馈，其质量proxy须再经闭环验收。Adaptor/critic训练、编码、全部采样与重规划、通信及物理执行均计费，调度、观测或真实质量失配时，保固定预算、短chunk和可信controller，不由冻结基座或较低平均调用成本批准自知安全、硬预算可行或跨技能泛化。
<!-- source-family:SF-2026-ARXIV-2606-14375 -->

拟新增正文与独立marker：

即使不训练外部调度器，数值采样深度也应与执行承诺联合验收，而不只把少步求解视为同一轨迹的低精度近似。[一项冻结 flow-policy 对照](https://arxiv.org/html/2610.32102v1)在配对噪声下减少覆盖完整 flow 区间的均匀 Euler 步数，观察到动作云更收缩、均值路径较接近；频繁重规划时损失的 redraw 多样性可能有用，长 open-loop 时同一离散误差却可能抑制横向漂移，少步收益因此会随执行 horizon 反转。这里不是提前停在 flow 中途，也不证明所有非线性 policy 的 centroid 不变：解析结论限于高斯线性流，实测仍有均值偏移和非标量协方差变化，简单缩初始噪声未复制收益，单步采样又会明显失真。部分模型只减轻长 horizon 的退步而未真正超过深解，动态目标和精密接触仍需要及时反馈，不能由静态任务结果鼓励更长盲执行。已有训练、联合 sweep、全部编码/求解/重规划与真实控制均付费，per-call 时间除执行步数只是摊销计算，少 NFE 不等相同比例的完整延迟或硬 deadline。超出预测 horizon、几何或观测支持时，保留已验 solver、固定保守 prefix 和短步重观测，由 controller 决定执行，不让更窄动作云自行获得安全资格。
<!-- source-family:SF-2026-ARXIV-2610-32102 -->

完整后肩：

还应把预测长度 `p` 与本次实际执行的 prefix 长度 `e<=p` 分开：缩短 `e` 不会自动省掉已经预测完整 chunk 的模型成本，却让真实 observation 更早重新进入闭环。一个无需额外 rollout 的提案分支从 action self-attention 的跨头/层平均、行 entropy 与连贯区间估计截取边界；attention 只拥有 execution-length proposal，不是新的传感信息、校准置信度或安全阈值，真正中断仍由 controller 决定。<!-- source-family:SF-2026-ARXIV-2602-21445 -->

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32102` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32102v1)III-A–D/Prop1与IV-A–C中factorial、matchednoise/重抽与scalarrescale反侧必要，R154评分2+1+2=5。仅均匀Euler完整区间步数×执行horizon的经验符号/几何条件；保Gaussianlinear非通用centroid、单步失真/协方差非纯scalar、GR00T仍负/RoboTwinpi.5不NI、dynamic目标失败/精接触短反馈、percall/s非总SLO。表文任务数/部分架构措辞未闭不纳、未核图像素/代码或运行复现。原三件PRE/SAVE/selfread/solePOST依后到事实，不预签。


### 22.8 32941 R159后三件真实SAVE/完整自读

32941 R159必要6/actualCh26与§22.3原单段/独立marker/本人注整体PRE通过，root17745→SafetyFilter精确位已确认；作者仅原三件apply_patch真实SAVE。正文2485/marker2486/本人注2538，完整新增/17745完整前肩/SafetyFilter标题+完整首段后肩/本人注及旧04436首注实际逐字读回match、marker1；剥本三件恢复fresh baseline `cd572bc1e196ad21e62adc4d5e529c3f3358daa5ab9cc15f8e267c3af9620e71`，限定Ch26 diffcheck无输出，保护暂停他日未POST旧段/旧注不触碰。现交soleactualPOST，不预I；其余单篇独立推进，不重既成必要。


### 22.9 32969 必要完成（6分）

**DexPort: A Hand-Held Skill Interface for Dexterous Hand Data Collection**，[精确2610.32969v1 HTML](https://arxiv.org/html/2610.32969v1)实际读III-A–C相关采集/skill与rawlabel/标定、IV-A–D关键label对照/评价反侧、D/E的训练差异与异步部署；不全机械装配/rotationreward矩阵或图像视频。Wuji20DoF同physicalhand+camera模块用于收集/部署，Quest轨腕，记录20Dtarget与measuredstate；手指由power/pinch/twofinger/rotation协助operator，BC不给skillID/params/phase，只predict腕相对chunkstart9D+手absolute20D，observation反而是两step图像/proprio/measuredhand。不能把保留20joint写成示教覆盖任意独立手指运动；rotationactor实控12joint、ring/pinky固定，20HzsimPPOskill另训且critic有handle特权，operator握腕仍人工。

Skilllabels不进BC不等无skill支持/无训练成本。Samehand-camera省手retarget，不省Quest→robotflange的6DoFhandeye leastsquares，两arm分别约30posescalibrate；Eq1框架约定不在本书拼完整SE3recipe。Data动作30Hz，rotation20Hz为不同loop；部署16stepchunk只保first8、按observationtickdropelapsed/overlapaverage，时钟对齐仍要验，非每tick freshinference。DDIM50train/10sample、DINO-U-Net与全部预处理/normalization均费，未核kernel/deadline。

关键对照：targetcommand vsmeasuredstate是共享recipe单label替换；原文解释contact下state不等所需target，不能反推已量到真实接触力或target就是环境effect。各policy每task15episode/各condition15，三success任务mean64vs11不包含screwrpm，phase成功以前面全通过为条件，不是全trial并列独立success。Statebaseline持物31.7s反好于15.6s但转速约1/3，不能写所有指标支配。1605lab+1000wild PnP，同trainingobjects/多背景光线，unseen测试不同；co-train部分U-Net512…2048 vsbaseline256…1024且更多数据，故不把36→78或各condition增益全归portability/环境广度唯一cause。单expert各30min122 vsglove86/skill68/human275是局部throughput，human最快但无robotaction，不是等动作质量/总训练费，重复/CI与净训练硬件wallNotDisclosed。四realworldtask不给开放物理安全/跨手型泛化。支持/反侧足停，不再全附件/重采实验。

### 22.10 32969 actualowner与整体三件PRE

实际owner `MULTIMODAL-EMBODIED-VLA` Ch26数据演进，而非通用Ch27资料去重或robot产品手册。已实际读本数据节teleop→portable→derivedlabel/embodimentalign、QwenRobotManip slot/frame/本体条件、contextauxiliary分工及derivedprovenance论证；Ch25/27交接本批有效。具体NC为sameembodiment仍要actionframe/consumer标定、derivedlabel非事实与全费已有；差额是接触下rawcommand-vmeasuredstate actionlabel、skill只塑collector支持而不进BC、同handcamera仍需腕mount时钟合同，不能由一般数据广度覆盖。root已确认‘后一步…物理证据越强’完整段后→2510.02538前独立位无冲突；以下原单段/marker/本人注交sole reader，未PRE不SAVE。

完整前肩：

后一步没有否定前一步。越远离真实 embodiment，数据越容易扩展，action semantics 越弱；越接近真实 robot，成本越高，物理证据越强。

拟新增正文与独立marker：

即使用同一只机器人手采集示教，command 与 measured state 仍是两种标签：接触时关节未到达目标，可能恰好来自维持抓力所需的 target–state 偏差，不能把后一个测量姿态直接当成下次应发送的控制目标。[DexPort的受限采集分支](https://arxiv.org/html/2610.32969v1)把部署的 hand–camera 模块装到便携把手上，以少量参数化技能协助人产生手指命令，同时保存目标与测得状态；随后 BC 预测原始腕部动作和关节 targets，不消费 skill ID。技能因此约束采集支持，不是部署策略必须重放的离散标签，也不证明有限技能已经覆盖所有高维动作。复用手和相机减少 retargeting 差异，腕部仍需 controller-to-flange 标定与时间对齐，同本体不等控制器、负载和接触自动等价。只换 action label 的小样本对照支持命令监督的重要性，但状态标签基线也有更长持物时间，完整任务、阶段成功和转速不能合成一个保真保证。采集/技能训练、标定、BC、异步 chunk 对齐及实机回归均付费，野外共训还同时增加数据和部分容量，不能把全部收益归给可携带设计。目标/测量时钟、标定或接触支持失配时，保留两类记录与明确 controller schema，回目标本体示教和已验短步控制，不由更快采集或同一硬件批准任意手型迁移与物理安全。
<!-- source-family:SF-2026-ARXIV-2610-32969 -->

完整后肩：

模拟广度也可以先通过在线模仿取得，再把真实域更新限于已采示教，而不要求真实环境提供可直接优化的任务reward：用少量模拟expert与新增交互训练latent dynamics、价值与策略，并以expert/behavior分布的代理信号提出学习目标；随后只用目标域示教适配encoder和policy。[受限在线预训/离线迁移对照](https://arxiv.org/html/2510.02538v1)因此改变的是交互与更新阶段，不是没有reward proxy、真实采集或物理风险。目标优化离线，示教仍可由真实rollout和人工纠正获得；部署state还须绑定相机、mask/物体mesh/pose估计、proprioception与动作坐标，不能从模拟精确状态直接继承观测资格。更宽的关节边际分布不证明联合覆盖或唯一收益因果，更新encoder也不自动保留冻结dynamics的latent语义，应分验目标动作、旧能力与实际消费的组件。模拟探索、专家制备、世界模型训练、真实采集/重置、感知/标定与微调和闭环验证均付费；三任务各十次和局部pose/kinematics gap不签通用OOD或安全。支持、状态估计或净收益失配时，保留目标本体真实示教、直接BC/既有policy与独立controller、停机和人工接管，不由有限成功率批准真实域自行探索或在线更新。<!-- source-family:SF-2025-ARXIV-2510-02538 -->

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32969` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32969v1)III-A–C/IV-A–D关键label配对与D/E部署必要，R154评分2+2+2=6。仅samehand target-vmeasuredlabel/collector skill非BC标签与mount/timingconsumer接口；保15trial/partial-vfull/rpm-vholdtime反侧、rotation12joint特定支持、co-training额外数据/容量非唯一因果、单expert30minthroughput非全费。未核全reward/RL超参/图像素/源码或运行复现，不纳任意hand迁移/完整recipe或安全。原三件PRE/SAVE/selfread/solePOST依后到事实，不预签。


### 22.11 32348 必要完成（6分）

**LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners**，[精确2610.32348v1 HTML](https://arxiv.org/html/2610.32348v1)实际读§3.1–3.5采用接口、4.1完整比较/信息/协议、4.2–4.3关键sameexecutor与T2–3反侧和5限制；不用全A/Bcase或Cprompt。系统每action追加index/envstep/command及紧后fingeropening/eeheight或NOTEXECUTED；log每次全给，note-only最后八action。所有旧notes逐字保而非只latest，但模型判断target/plan和真正抓到/动作purpose仍可能错，log不是effecttruth，更不是硬controller。Actionsequence最多6move/wait/有限检查失败重问；learneddelegate则perchunktrace。仅physicallyexecuted命令记录与measurement能支持相应事实，不称完整effect/事务exactlyonce。

Watch在action前提出frontimagepoints或all；action期间约四envstep一帧，长动作最多16evenlyspaced含末；action后在watch28px圆/512分辨率比较，>5%pixel差>30强度才返当前与predecessor，并报告扣帧数。无watch不返中间帧，这不是无变化证据/不支持missedregion还原，也不是在线triggercontroller。Demo先每8帧skim、model指定range每2帧最多24，再作仍会被改写的running summary，finalsummary作初note，不能把分工等同所有facts免压缩。观测读取depth/calibration可转pixel3D，API等待时simulation暂停，fullhistory成本增长未界，不是实机闭环SLO。

关键受控：RoboMME16task/800test，仅oneproprietaryGPT6Astra/每episodeconfiguration一次，1300envsteps/1.5Mtokens cap，plannerinput+output含demoviewing但非API钱/latency/机器人IO全账。Samecode/prompt/executor/tasknotes/budget noteonly对照在motionplanner256episode237vs234success（19wins/16losses，不significant），40.5kvs71.3k、46vs114images；learnedexecutor128同104success/7v7。Failuresmotion15vs10、other4vs12是事后人工逐决策归因，非独立blindedcause/cert；同command重放也可异结果，不能把最终成败全记memory。Hard64epis单组件关闭反**更高**58/61success vs56，withoutexec/history/gate各other2–3而full0，单组件2–4case仅一致线索、非各自显著因果；skim关闭tokens46.3k低full50.7k但images93多full53，不能说每component都省所有资源。

直接反侧：directcontrol93.5与learnedpolicy/人比较换executor和depth/calibration/tasknotes，前沿系统perchunk还换callfreq/actions，均不当memory-only证据。Tasknotes含successcode阈值/离线oracletrainingepisode测出的height，非episode-specific位置count但确有附加监督；no-note仍89.1仅局部不是所有notes免费。API模型/异步硬件latencyprecision与实机安全未披，全部一个simbench无physicalrobot。待采用为事先expectation限定frame消费和事实记录/派生notes职责，不采更高通用success/事实保证/所有组件唯一机制；支持和反侧足停，不追加全prompt/所有episode。

### 22.12 32348 actualowner与整体三件PRE

实际owner `AGENT-MEMORY` Ch77长期视觉流/retention，不是Ch26policy内部latent或Ch75单次contextcompaction。已完整实读Ch77 CompactControlState/ExactArchive与长期视觉流Entity/perception/EventMemAgent两完整段，并具体比较Ch26 runlog/observer/controller及短期policymemory段；Ch76/78交接与本日Books背景沿前批未变有效实读复用。具体NC是rawarchive/derivedsummary/历史非current事实、灰度事件proxy和窗口不等全存储有界已有；差额是action事前watch→事后局部变化筛帧（无watch无中间）/demo skiminspect，以及system完整log+旧notes原存所保信息和增长边界，不把一般factauthority重算新贡献。root已确认EventMemAgent第二完整有限评价段后→‘从原始轨迹到派生策略’真H2及首完整段前位无冲突；原单段/marker/本人注交sole reader，未PRE不SAVE，保护31846旧段与旧注。

完整前肩：

这条分支把短期 retention 与长期 evidence 生命周期分开，不把固定 32-frame 窗口说成总存储恒定。EventMemAgent 的有限评价使用预计算记忆和离线 GRPO；event/reservoir 相比固定分段的局部收益较小且未报重复运行区间，移除 OCR 的切片或已有 streaming baseline 也可能更好。长期写入、检索和额外工具调用仍有成本，尚未证明真正无限在线流或稀有事件保证。短 clip、精确回放和查询关键帧已知的负载仍可采用固定窗口或原始 frame 保留，而不是强制事件化。

拟新增正文与独立marker：

当历史来自 planner 自己触发的动作，视觉 retention 还可按执行前的预期来取样，而不只等全图变化超过阈值。[LogLook的受限机器人分支](https://arxiv.org/html/2610.32348v1)让系统逐动作追加命令、执行状态与紧随其后的夹爪/高度测量，并原样保留旧 notes；模型另为动作指定 watch 区域，系统才从已记录的有限帧中返回该区域变化处的相邻帧。没有 watch 就不返回中间帧，局部未变或采样前已经消失的证据也可能被漏掉；预计哪里会变不是语义事件检测，更不是无变化的证明。示范视频则先 skim，再在模型指定片段内 inspect，最终摘要仍是可错的派生状态。执行 log 避免一次 note 改写抹掉记录，却只证明发过什么与测到什么，不认证抓到了目标物、计数完成或动作目的，旧 notes 全保留也会积累冲突和 Context 费用。相同 executor、提示与预算的比较支持更少 planner tokens/images，单组件成功差却常被执行器随机失败掩盖，不应将完整系统成功唯一归给某条 memory。原实验只在等待 API 时暂停的仿真运行，部分 task notes 使用 benchmark 完成阈值，不能外推真实控制时限。记录/图像采样、筛帧、反复读取全部 notes/log、API 与执行均付费；预期范围、历史解释或费用失配时，保原帧/明确完整窗口、外部执行核验与新观测，不由 append-only 名称或更短模型请求批准事实充分和安全行动。
<!-- source-family:SF-2026-ARXIV-2610-32348 -->

完整后肩：

## 从原始轨迹到派生策略：Memory 的演进不是无限追加

Agent 最早可以直接重放最近对话或成功 trajectory。随着任务增长，原始记录变长、检索噪声增大，并会反复
带入偶然步骤，于是出现两条互补的演进路线：

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-32348` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.32348v1)§3.1–3.5/4.1–4.3关键sameexecutor/T2–3及5必要，R154评分2+2+2=6。仅actionexpectation watch→事后有限帧filter/skiminspect与machine-log/旧notes分工；保command+measurement非purpose、NOTEXECUTED/无watch漏中间、灰度变化非语义/fullnote增长、同总success未显著/单组件2–4失败非独因果、API单次/仿真暂停/深度标定与successcode tasknotes信息差。未核C全部prompts/图像素/源码或实机复现；原三件PRE/SAVE/selfread/solePOST依后到事实，不预签。


### 22.13 31859 R161后三件真实SAVE/完整自读

31859 R161必要7/actualCh28与§22.5原三件整体PRE已过，root实际dtype→FlashOptim精确位无冲突；作者仅批准单段/独立marker/本人注apply_patch真实SAVE。正文1280/marker1281/本人注1954，完整新段/两完整肩/本人注+旧31897首注逐字实际读回match、marker1；剥本三件恢复fresh baseline `a9e9b88e978ed875f93258a8100742d6f105442f15c46044699060fbcca8009a`，限定Ch28 diffcheck无输出。现交soleactualPOST，不预I；32941原SAVE已交，后三原稿待PRE，保持既成必要域不扩附件/全源码。


### 22.14 前两真实闭合；32102 R165后三件真实SAVE/完整自读

32941 R162 actualPOST6/I、31859 R164 actualPOST7/I均已过且精确位释放，不重必要/POST。32102 R165必要5/actualCh26与§22.7原三件整体PRE通过，root14375→p/e精确位已协调；作者仅批准原单段/marker/本人注apply_patch真实SAVE。正文1686/marker1687/本人注2541，完整新增/14375完整段+marker前肩/p/e完整后肩/本人注+旧32941首注实际逐字读回match、marker1；剥本三件恢复fresh baseline `6359977a947313f835b0d4170aaba15162d2326fab914cbfa1d504b8794532fb`，限定Ch26 diffcheck无输出。现交soleactualPOST，不预I；32969/32348原稿仍待PRE，不新增附件。


## 23. 代理并行下一五项：示教表示、仿真与历史消费（Methods前评分）

root明确在§22最后两项仅等sole时可并行准备31762/31801/31834/31845/32094，单篇不等批齐。§22三项实际POST有效，后两未PRE/未SAVE，仍分层普通待办，不借本新批掩盖。换批已重读AGENTS/当前研究合同，未变本日Report/来源/ROADMAP/背景及checkpoint沿本日已完整实读层复用。只复用R35及ARXIV_B既成完整题摘/日身份/准入，不扩AB/date/列表。

### 23.1 实际新增命题评分与最低必要

| 精确已核身份/题名 | 增量/维度边界 | 分数与最低投入 |
| --- | --- | --- |
| [2610.31762v1 — See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space](https://arxiv.org/abs/2610.31762v1) | 固定foundationencoder目标未必最合导航；跨encoder全层residual重构表示空间，与JEPA预测/策略端到端协同，改变表示目标→预测→policy消费者接口。D2重要构造/替代；R2跨producer与预测/行动训练目标；U2可复用任务相关预测空间边界，不因foundation名称扩大3。 | **2+2+2=6**。核RepresentationResiduals/目标与梯度可见性、concat或单目标受控比较、下游导航反侧/全费，足停不全环境/扩架构。 |
| [2610.31801v1 — KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations](https://arxiv.org/abs/2610.31801v1) | kinematics→监督SparseMotionTokens→开放LLM解释替rawmulticamera，新增动作/进展/反向区分而非普通语义总结。D2有意义的表示/消费者资格；R1局部kinematic tokenizer/segmenter，跨模态名字不自动R2；U2可复用有损token与未见本体/ego motion条件。 | **2+1+2=5**。核token监督/kinematic权限、LLM消费和heldoutembodiment/progress/reversal关键对照，不全数据生成/全视频。 |
| [2610.31834v1 — WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations](https://arxiv.org/abs/2610.31834v1) | 外观重建不能保证物理trajectory可重放；可执行worldprogram迭代verification与cameraanchored背景/support/interactiveassets分层。D2环境构造/验证重要分支；R2演示观测→程序/资产→replay验证与交互环境交接；U2证据、生成与执行支持分责，不借一般sim真实性原则加3。 | **2+2+2=6**。核程序/验证何者真可执行及视觉/物理反馈资格、replay与interactiveeval反侧，不遍所有agentprompt/生成工具/物体。 |
| [2610.31845v1 — EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions](https://arxiv.org/abs/2610.31845v1) | noisyretargetaction不等权监督，可靠性条件corruption/weightedregression；未来cleanEMAteacher蒸馏studentearlyrepr，改变标签可靠性与特权future消费。D2重要目标/训练分支；R2数据可靠性估计→扰动/目标→teacher与policy消费者；U2可复用训练特权/部署可见性边界，不按ego规模加分。 | **2+2+2=6**。核reliability来源和监督是否可识别、futureteacher/stopgrad与关键受控反侧/部署费，足停不全dataset/各bench。 |
| [2610.32094v1 — TTT in VLA Models: Exploring Training with Human Demonstrations](https://arxiv.org/abs/2610.32094v1) | fastweight加pairedhumanvideo并不证demo目标被用；truncatedBPTT/seq短化/fullgradient/contrastive负对照与singleframe固定位置偏好限制此具体TTT消费者。D2局部重要负结果/适用边界，而非把‘有memory未必用历史’成熟原则算新D3；R1所测TTT-VLA组件；U2可复用可见性/实际消费的评价条件。 | **2+1+2=5**。相对旧准备3+1+2=6仅D3→2：本拟采是所测局部否定，不预宣布所有TTT/历史方法设计结论纠错，非因读费/Books降分。核memorytransfer/BPTT、目标依赖对照/训练与容量反侧；若与具体Book冲突再仅受影响域深入，不全TTT库。 |

五候选均保留，不因已有Book覆盖或Methods工作量缩池。以上先交sole评分校准；依root单篇不等批齐授权，未变准入/未变分值的31762/31801/31834/31845可按原最低域准备，32094局部D调整待校准后展开。本层不预证据完成、owner缺口或I/NC。


### 23.2 前批32969 R171后三件真实SAVE/完整自读；本新批R173最低投入校准通过

本节只是异步保存前批§22既成原稿，不重必要或改变新批分母。32969 R171必要6/actualCh26与§22.10原三件整体PRE通过，root数据演进后→02538位已确认；作者仅原单段/独立marker/本人注apply_patch真SAVE。正文1255/marker1256/本人注2544，完整新增/数据演进完整前肩/02538完整后肩/本人注+旧32102首注实际逐字读回match、marker1；剥三件恢复fresh baseline `ed87a96988ecf7047df8a2901c7cfc1a2382f13e69f8f3ccda647a4bb317b6be`，限定Ch26 diffcheck无输出，现交soleactualPOST，不预I。§22前三32941/31859/32102实际POST仍有效，最后32348待PRE，普通待办不H。

新五§23.1分6/5/6/6/5已R173校准通过，32094原准备6保留、仅局部D2采用对象变清楚不因费/Books降。31762/31801沿未变准入/分值已开始精确HTML必要，尚未写必要完成/owner；其余三未开始Methods，支持/反侧足即停。


### 23.3 31762 必要完成（6分）

**See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space**，[精确2610.31762v1 HTML](https://arxiv.org/html/2610.31762v1)实际读§3.1–3.4、4.1协议与关键4.2反侧、5.1–5.2/T3同编码器/目标对照、6限制及A.1–A.3梯度/可见性与latentinputs干预直接域；不全B读出decoder/实机视频或训练源码。三个frozen视觉priors semanticDINOv3/geometryDA3/dynamicOpenD4RT跨深度，adapters对齐16×16、source/layer/position身份，三层RepresentationResiduals按position/encoderlayer+incominghidden softmax混合，再spatialselfattn/FFN与CLS。当前每view1CLS+64spatial、历史1+8，原Qwenvisualtoken仍在，不声称只一个latent/省全encoder。Dynamic4frameclip只到各obstime，futuretargets用真实未来相应viewCLS经G到256，missingview置零，0.4–1.6s四target；未来只target不进policycontext，**预测与target两端都更新、无stopgrad/EMA**，VISReg在globalbatch逐futuretime约束mean/scale/randomprojectionshape，非语义真值/普遍不坍塌证明。

StageI mask隔离visual与instruction前缀，latent读两者，action只读instruction+latents，nav/wm/reg/QA权.01/.1/.9/1；StageII全causal共读visual/latent，权1/.001/.009/1，共享LLM/Residuals/CLS/planner/projectors均训，source/Qwenvision冻结。5.08Msamples/16GPU/38270steps，stagehalves按sample而非episode分开，同episode可两stage；非独立两个数据episode证书。QA另路径无navigationrollout/futuretarget。Action是当前robotframe八waypoint；预测future来自行为数据条件，不提供任意候选action反事实transition查询，latentdream不是环境认可当前状态。

关键对照：同三个encoder无dream concatSR87.3/CR28.7 vsResiduals93.45/18.05支持接口分支，但多层访问/容量同时变化，attentionshare非encoderlayer独因果。相同接口仅dreamtarget，free-run93.35/15.90、nativepooled92.75/22、self95/13.45，target/regularizer有实证差额不等prediction唯一原因。Fullbenchmarkbasefromciteddifferent训练/相机信息；monotrackingCR11.89弱TrackVLA++4.71，RxR SR64.2弱Qwen65，pointgoalSPL等亦有反侧，不采全面SOTA安全。A3samefullcausal下crosssceneswap/zero保持外输入但同时改四recurrentinputs/h0，two-stage更敏感/GT ADE恶化，**200navigation-trainingobservations openloop**非heldout闭环cause；single正常ADE3.93还低two4.38。Readout只作analysis，未来真实CLS优于predictlatent，本次不采‘一latent完整worldstate’或新增occupancy真值。source披16GPU未给本采用域精确型号/precision/concurrency/latency，均NotDisclosed；额外encoders全层特征、四latent、futureencode/regularizer/QA训练与完整controller回归都费。仅navigation验证/其他manipulation未验，必要足停。

### 23.4 31801 必要完成（5分）

**KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations**，[精确2610.31801v1 HTML](https://arxiv.org/html/2610.31801v1)实际读§3.1–3.3/4.1–4.4关键协议与反侧、B.1–B.3采用所需normalization/双向scope/码本、C匹配边界、D人类转换缺测与E独立progressprobe；不全humanpose图/全Fprompt/G环境。共享14D=左右v/ω/开合速率，以transitiontimestamps训练temporalCNN及focalboundaryhead，headdiscard；冻结encoder后均匀1sbox/stride.5s聚合、trainstats归一/K512Kmeans码本，**2token/s固定网格并非事件触发稀疏/Huffman无损**。拓展Qwen3.5-9B词表/LMadapt，input为taskinstruction+SMT+每秒time，answerJSON start/end/description只responseCE。encoder只boundary监督，不是natural-language/trajectoryreconstruction；codebook冻结readstage不等原LM冻结或无标签。

Offline segmentation每episode自身zscore和509samples/17s双向centeredconv会见未来，不能线上时刻决定动作；这是明示适用而非leak指控。跨本体14D同shape仍有FK/poseframe/humanheadyaw/palm/aperture定义、30Hzresample与timeidentity，非actuator同义。训练YAM5478/608valid，heldout200十task；AgiBot2653/三task与human193未targettrain；各表部分video人口不同，不能把.61vs.30特定heldout人口与大test.40vs.19拼成统一F1。SameLM/LoRA只是sharedreader，替tokenizerinput/preprocess/训练人口仍不同，C FAST/OAT/MotionGPT readers6086而SMTtrainheldouttask/normalization不同，故不把所有差距唯一归boundaryloss。OAT同2Hz实际readerinput1162低SMT1368，SMT只是相对FAST/MotionGPT更短；groundedF1要求IoU+lexical/cosineproxy，排controltags不认证语义完整性。

Humanprojection193longruns46%frames插值、114有video；端点近.5s边界删/trackgap筛选，98%boundary邻近真实追踪不消除插值限制。Taskname可推未训词，作者明说open-vocab展示不是从motion恢复objectsemantics；removal/错trajectory控制仍有意义而不授每description真值。**Progress是另一consumer**：frozencontinuousfeatures非SMTcodes，固定YAMstats/过去4scausalwindow、0.25sstep，额外subtaskstart以来8Ddisplacement和68khead用4000YAMsubtasks训/600valid，非encoder自然零监督进展能力。Reversal是已标subtask内sequence倒序并negate14channel/视频倒放，不等真实物理可逆；2586subtask357episode不算2586独立episode，clusterbootstrap2000/meanSpearman与86%negative有相应范围，forward.51弱ReWiND.88，不能全方向支配。真实controller/closedloopreward未验，数据转换/所有encoder、码本/LM与progress训练费用均计；恢复后R196独核F/G纠正旧ND：reader BF16、3×H200/globalbatch9约2.2h；加载后单H200/vLLM批量200轨迹32s，finalreader单seed；这不是含加载/制备的E2E、在线SLO或全部费用，不冒模型小就全系统高效。机制/关键反侧足停。


### 23.5 31762 actualowner与整体三件PRE

实际owner `MULTIMODAL-WORLD-MODELS` Ch25，而非把一般多encoder融合重复放Ch23。已完整读Ch25 DT-JEPA两段、Latentdynamics/LeWAM共训与连续target/stopgrad/运动target相关链及Ch24/26交接；本日Books背景有效。具体NC是预测供policy、target漂移/防坍塌、latentprobe非物理状态和任意action模型已有；剩余差额是task读出的多encoder层空间同时成为当前输入/可训练futuretarget、两端gradient与先限actionmask后放开消费者，这不同于旧EMA目标/固定latent的概念复述。root已确认DT-JEPA32657两完整段/marker后→Next-observation标题/首段前精确位无冲突；以下原单段/marker/本人注交sole reader，未PRE不SAVE。

完整前肩：

未来预测也可以直接成为policy的条件，而不先把候选action逐一送进dynamics搜索。一个标量return-to-go能对应许多不同未来，另一条分支先从可见state/action history预测未来latent的分布，再把抽样结果转换成policy表示的逐维scale/shift；真实future经EMA encoder只提供训练target。[DT-JEPA的受限分支](https://arxiv.org/html/2610.32657v1#S3)因此把预测器与动作consumer联合学习，但预测latent不是真实未来、不是由环境承认的状态，也不自动成为可供任意action查询的transition model。逐target的可见history与mask仍要在实现中明确，不能只因有stop-gradient便签发整条训练无泄漏。

这里reward-free指预训练不消费reward，仍依赖离线轨迹和行为克隆；适应新的reward又需要实际交互、筛选高return样本和critic指导，不是无需反馈的任意目标控制。固定预测器下逼近population policy的有限样本界不等最优控制保证，预测NLL下降也不能忽略随encoder变化的目标熵而直接认证信息更多或不坍塌。有限模拟中分布预测与AdaLN消费有收益，仍须另验目标/动力学变化与真实controller；encoder/采样、全部critic交互与训练费都在。分布或动作质量失配时保留确定性预测、原BC/return条件或显式短rollout与重观测，不把一次未来表示的改善替代执行可行性和安全验收。
<!-- source-family:SF-2026-ARXIV-2610-32657 -->

拟新增正文与独立marker：

预测目标还可以与 policy 当前读取的视觉空间共同构造，而不先固定某个预训 encoder 的末层为未来答案。[RepresentNav的受限分支](https://arxiv.org/html/2610.31762v1)保持多个视觉 prior 冻结，从它们跨层特征及当前 residual 学习按位置的混合读出；同一读出既供当前决策，又把真实未来观察压成训练 target，预测端和 target 端都接收梯度，用分布正则约束坍塌。没有 EMA/stop-gradient 不表示目标是物理真值，防坍塌也不证明信息充分。为避免 policy 绕过预测，早期让 action 只读指令与生成 latent，后期再开放当前视觉；换场景或清零 latent 会改变动作，说明这条通路被消费，却只是训练观察上的 open-loop 干预，不能替闭环安全和收益归因。未来图像只建训练 target，部署仍从已见历史预测；这份经验未来不等可供任意候选 action 查询的反事实 dynamics，事后解码出深度或 occupancy 也不使 latent 成为完整 world state。多 encoder/层特征、四步 latent、未来编码和联合训练均付费，部分碰撞与导航切片仍弱于替代模型。表示目标、相机历史或真实行动质量失配时，保留固定/单 encoder 目标、较简单视觉接口与显式短 rollout/新观测，不由更低预测误差或更强 probe 批准通用世界辨识和 controller 权限。
<!-- source-family:SF-2026-ARXIV-2610-31762 -->

完整后肩：

### Next-observation generation

它让模型学习 temporal regularity，适合 representation pretraining 和短期预测。但 observation correlation 可能由 camera motion、dataset bias 或常见脚本解释，不等于模型识别了 action cause。

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-31762` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31762v1)§3/4.1及关键4.2反侧、5.1–5.2/T3、6与A.1–A.3必要，R173评分2+2+2=6。仅共享trainable层读出→当前policy+双端梯度futuretarget与maskcurriculum消费；保future只训练/非任意action条件dynamics、sample非episode split、latent干预训练observations/openloop及single正常ADE更低、CR/RxR反退和全encoder/latent费用。不采probe完整worldstate/唯一表示cause/实机SLO，未核全部B/C图像素/源码或复现；原三件PRE/SAVE/selfread/solePOST依后到事实，不预签。

### 23.6 31801 actualowner与整体三件PRE

实际owner `MULTIMODAL-REPRESENTATION` Ch23离散接口，非Ch26将code当动作执行。已完整读本离散表示首段到码本训练/producerconsumer/别codec分责的相关论证，具体比较Ch26数据本体/动作标签与Ch23连续时间/采样身份；Ch22/24交接本日有效。具体NC为量化损失、码本/encoder/消费者版本、短序列不保语义与全费已有；剩余差额是transition而非reconstruction监督的运动词表、uniformtoken位置与标签监督分责、离线整段和独立causalcontinuousprobe权限，不用‘已有VQ’全NC。root已确认通用codes完整段后→量化前扰动18252完整段前无冲突，以下原三件交sole reader，未PRE不SAVE。

完整前肩：

离散 codes 可共享 categorical prediction objective，也适合缓存、传输和自回归生成。代价是 codebook collapse、rare-code mismatch、长序列和重建误差。一个 code 是否“语义化”必须由 intervention、retrieval 或 reconstruction evidence 支持，不能从可视化聚类直接推断。

拟新增正文与独立marker：

离散词表也可以先为“动作何时改变”保留信息，而不要求重建全部连续运动。[KiRoSe的受限分支](https://arxiv.org/html/2610.31801v1)用标注的 subtask transitions 训练运动 encoder，丢弃边界 head 后，将特征按固定时间网格聚合并离线聚类，再冻结 encoder/码本，让语言模型从 motion codes、时间标记和 task instruction 生成分段与描述。Sparse 在这里是低固定码率，不是边界触发或无损熵编码；码本索引既非 actuator 命令，也不证明对象名称由运动感知得到，任务名仍可补语言先验。原分段路径使用整段统计和双向时间卷积，因而适合离线示教解释；另一个因果进展 probe 改用过去窗口、训练集统计、连续特征和已知 subtask 起点后的位移，还单独训练 head，不能将两者合成同一线上能力。跨机器人/人手还依赖速度、角速度、开合率及坐标/缺测转换；相同 14 维不保证接触语义相同。对照支持边界与方向信息的局部迁移，但预处理和 reader 训练人口不全相同，人工倒放也不等真实动作可逆。标注、转换/插值、encoder/码本、LM/probe 训练和独立分段/消费回归均付费；时序、细接触或标签支持失配时，保留原连续运动、视频/人工分段与明确因果输入，不由更短 token 或下降的 progress 曲线批准动作成功与物理安全。
<!-- source-family:SF-2026-ARXIV-2610-31801 -->

完整后肩：

离散量化的不可导边界也不是鲁棒性屏障：攻击可以在量化前扰动连续 feature，再通过改变 codes 影响冻结的消费者。一条受限替换分支固定 codebook 与 downstream，仅用无标签 adversarial feature distortion 更新 encoder，使扰动输入的表示靠近原 encoder 对干净输入的表示；这是生产者兼容旧消费者的训练目标，不是逐 code 一致或所有下游安全的证明。[原版本控制](https://arxiv.org/html/2602.18252v1#S3)中，攻击失败仍可改变大量 code indices，说明索引稳定不是安全的必要条件，索引变化也不充分判有害；更大攻击半径则付出 clean/robust quality 取舍。监督与无监督分支使用不同半径、目标及更新集合，不能把跨任务差异全归因无标签训练。Encoder 训练、攻击搜索/ensemble 与逐消费者校准均计费，须绑定旧 encoder、码本、consumer、扰动范数和评价任务；兼容或 clean quality 回归、强攻击未覆盖时，保留旧 codec、连续 encoder 与独立 downstream/effect 验收，不由 tokenization 一项自签系统安全。<!-- source-family:SF-2026-ARXIV-2602-18252 -->

拟true-H2 `## Review notes`本人注（保护旧首注）：

- `SF-2026-ARXIV-2610-31801` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31801v1)§3/4.1–4.4/B.1–3/C匹配边界/D缺测转换/E独立progress必要，R173评分2+1+2=5。仅transition监督低率码本冻结→LM读取与离线-vcausal独立consumer分责；保uniform2Hz非事件/非Huffman、wholeepisode/双向17s非在线、continuousprobe另训/annsubtaskstart、taskname可补语义、baseline不同人口/预处理、人手46%插值/114video子集及倒放非物理逆。未核全Fprompt/G环境/图像素/源码或运行复现，不授控制/全费用优势；原三件PRE/SAVE/selfread/solePOST依后到事实，不预签。


### 23.7 前批32348 R175后三件真实SAVE/完整自读

32969 R176 soleactualPOST已过，正式6/I Ch26精确位释放；§22前四项实际闭，不重已成必要。32348 R175必要6/actualCh77与§22.12原三件整体PRE通过，rootEventMemAgent→原始轨迹真H2+首段位已确认；作者仅批准原三件apply_patch真实SAVE。正文760/marker761/本人注2020，完整新增/前完整评价肩/真H2与首完整后段/本人注+旧31846首注实际逐字读回match、marker1；剥本三件恢复fresh baseline `a7860cefdad80758eb346ad9d2c79ea7fb21c0e4fc7646380662be9d1be54e93`，限定Ch77 diffcheck无输出。现交soleactualPOST，不预本项I或§22全闭。新批31762/31801必要/原稿ready，后三刚开精确HTML仅核心导航/摘要，尚未必要完成，不把工具返回全页当已读附件。


### 23.8 前批五项实际闭合；31834 必要完成（6分）

§22五项已全真实solePOST：32941 R162=6/I、31859 R164=7/I、32102 R167=5/I、32969 R176=6/I、32348 R179=6/I；对应Ch26/28/77精确位释放，不第三必要/POST。当前§23不预I。

[WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations](https://arxiv.org/html/2610.31834v1)，exact-v1；R35题摘/日身份、R173三维2+2+2=6复用。实际已读§3.1–3.5核心及4.1–4.5关键T2–6/§5直接限制，拟采用域已足停止，不扩全部工具实现或机器人附件。

输入RGB视频加记录的机器人轨迹，不是视频独立恢复动作。模型M分静态场景/对象/关系/反馈；specialist candidate经stagechecks才commit，否则旧M不变；typedfailure与rewind标受影响components，下游依赖失效重建。Router只遍固定constructiongraph合法advance/skill/rewind/inspect/accept，由executioncontroller核合法性，不是任意自治pipeline。Gaussian供appearance，collision支持geometry另建；对象mesh、metricpose/physics/articulation与相机外参/坐标轴/robotbase共同对齐。camera用match+photometric/line，Meshy/Articraft资产不等真实物理。verifier消费render/config/simoutcome/diagnosis，文中无完整形式oracle或全部阈值执行证据。原jointtrajectory不retarget/replan进入IsaacSim，支持有限replay兼容，不签发新policy/真实控制。

视觉10DROIDscene首帧外观，spatial17objects/8pairs用可见面centroid非完整3D/dynamicsGT；PSNR13.57略高RoLA13.53但SSIM.570低于.587，layoutIoU.469低ASTRA.598/pos9.66差于8.72，非普遍胜。ReplaycontactF1.873非完美，表中100%只是所测小示教人口；完整replay分母、successcriterion/重复seed/CI及硬件wallcost在采用域未披露，不把10视觉scene擅补为10replay。T5onepass1轮/fixed2/full4非matchedtoolbudget；T6去StatefulMemory仍成功且数值接近，去adaptive/refine失败也不授各组件独立因果/普遍必要。Budgetexhaust不等pass；§5明确smallDROID/no downstreampolicylearning/no真实部署。完整资产/标定/工具/返工/replay均计费；不采“100%”作物理真值或安全率。未运行代码或模拟，未读域不改H。

### 23.9 31834 actualowner与整体三件PRE

实际owner MULTIMODAL-WORLD-MODELS Ch25“旧Simulator仍合理”下资产→物理接口，非Ch82通用agent编排。已完整实读静态资产/PBR19944、projection21542、对象化15843与邻静态edit26055，并比较同章可执行WorldHypothesis05138的proposal/sandbox/historyverifier完整两段及Ch26真实动作交接。具体NC是外观不认动力学、对象化mesh/collision分交付、有限replay不授物理事实已有；真实差额是多阶段候选检查commit/上游回退时依赖失效与同一记录轨迹验收入口，不借“agent”重复原则。拟15843完整段后→26055静态编辑完整段前，待root确认精确位；以下原三件交sole reader，未PRE不SAVE。

完整前肩：

一份可渲染场景还可以只提供对象的空间 anchor，而不让原表示直接承担碰撞：先从 Gaussian 场景提出对象 inventory 与区域，移除目标并补背景，再独立生成对象 mesh、构造简化 collision proxy，以配准和渲染/接触约束把新对象放回场景。[受限对象化接口](https://arxiv.org/html/2605.15843v1)让外观表示与可编辑实体分开交付，原 splat 是定位参照，不是最终真实网格；补出的隐藏面、mask 和语义 inventory 也不变成新观测或完备对象分区。独立资产的对象级外观改善可以伴整scene人评下降，姿态/碰撞代理相容不辨识质量、摩擦、关节或动力学。生成场景、分割/补图、深度与对象生成、全部配准候选和独立用途验收都计费，抓取样例或单卡局部用时不授实机迁移与普遍效率。对象身份、遮挡或几何失配时，保留原可渲染场景、已测mesh与独立collision/simulator校核；替换后的状态继续待验，不能由“可交互”签发物理事实或安全。<!-- source-family:SF-2026-ARXIV-2605-15843 -->

拟新增正文与独立marker：

可交互资产也可以按重建依赖逐级提交，而不把一次生成的完整场景直接交给 simulator。[WorldMirror的受限分支](https://arxiv.org/html/2610.31834v1)从示教视频及已记录机器人轨迹构造可编辑 world program：静态外观、对象、空间关系与反馈分别存放，专职 agent 的候选须经阶段检查才进入 committed model；失败保留旧状态，回退上游则使受影响下游失效并重建。Router 在固定构建图内选择下一合法步骤，并非任意工具自治；共同米制坐标、相机/机器人标定以及独立的碰撞支持几何把视觉资产接到物理执行。检查来自渲染、配置与模拟结果，不是形式正确性或真实物理 oracle。原轨迹不重规划直接 replay，可揭露场景与既有运动的不相容，却不证明新 policy、安全或实机迁移；小规模示教上的完成也可伴非完美 contact F1，视觉/布局指标并非全部优于替代方案。更多自适应修订与固定轮数对照预算不同，去 memory 的单任务仍成功，不能把组合收益拆成各组件必要性。资产/标定、全部工具与返工、模拟 replay 和独立真实验证均计费，预算耗尽不是检查通过。坐标、资产身份或接触支持失配时，保留上一有效场景、已测资产与显式 simulator/真实观测，不把内部 committed 状态升级为外部世界事实。
<!-- source-family:SF-2026-ARXIV-2610-31834 -->

完整后肩：

若任务只是修改已有静态场景，也可直接在选定区域内更新高斯参数，而不先把整个表示变成可交互物体。先冻结区域外的高斯，再交替用局部对象与带背景的全景渲染接受生成先验监督，可把局部细节与对象在场景中的尺度、位置关系分开约束；一条[受限编辑分支](https://arxiv.org/html/2509.26055v1#S4)还用多视图类别先验缓解各视角外观冲突。这里背景参与条件，不等于其全部几何已被识别；类别先验也可能覆盖参考对象的特殊细节，bbox夹杂物或遮挡会让编辑边界失准。场景重建、概念适配、多模型引导、纹理细化与重新验收均付费，静态渲染更协调更不代表接触、动态形变或机器人可执行。局部/全景质量、对象身份或预算失配时，保留原场景、可信区域分割与独立资产编辑，让产物继续接受几何和用途检查，不以一组更相似的视图批准环境动力学。
<!-- source-family:SF-2025-ARXIV-2509-26055 -->

拟true-H2本人注：

- `SF-2026-ARXIV-2610-31834` — `live1027_china`，Daily2026-10-27补Oct26；[exact-v1](https://arxiv.org/html/2610.31834v1)§3.1–3.5/4.1–4.5/T2–6与§5必要，R173评分2+2+2=6。仅分阶段候选→检查→committed model与上游回退失效、外观/碰撞/共坐标交接；保固定graph、原轨迹replay非新policy、10视觉scene非replay分母、memory去除仍成功/预算不匹配、非全指标胜。完整成功判据/重复区间/全wall硬件费未披露；未核全工具代码/运行模拟或实机，不授形式安全或迁移；PRE/SAVE/selfread/solePOST依后到事实，不预签。


### 23.10 31762 R184后原三件真实SAVE/完整自读

R184必要6/actualCh25与§23.5整体PRE通过，rootDTJEPA→Next-observation精确位已授。仅原单段/独立marker/本人注apply_patch真实SAVE；正文257/marker258/注1796。完整新增、两侧完整DTJEPA组及Next-observation标题/首段、本人注+旧04390首注实际逐字读回，pair/note均true、marker1；剥本三件恢复fresh SHA `c8ac33acb141efd3c6d38f2597fb9fd869509580d4cb12496aac97ed2168cf38`，限定Ch25diffcheck无输出。交soleactualPOST，尚不预I。31834精确位root已确认无冲突，与本位不同；其余等待/必要按当前事实继续。


### 23.11 31845 必要完成（6分）

[EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions](https://arxiv.org/html/2610.31845v1)，exact-v1，R35题摘/日期与R173评分2+2+2=6复用。已实际读§3.1–3.4核心、4.1–4.4关键T1–3、A sampler/噪声假设、B有效mask/teacher、C1/C2与C6失败导出/C7费用、D3直接可靠性反侧及F；仅采用可靠性调action corruption与未来teacher表示的两条监督路径，不采全部retarget实现/科学应用或全图。支持/直接反侧已足停止。

c仅当前obs/instruction/state/embodiment；jointvision/actionflow各有time、共享attention，可读部分未来表示但部署没有真实future。q_d只是datasetprior，S2robot1/human.2，非标注错误的校准概率。普通样本τv~U、g~Beta(α,2)、τa=τv+(1−τv)g，α=.5+(1−q)*2.5；visionmarginal不变而低可靠action更带噪，普通τa~Beta(α+1,1)。2%cleanfutureboundary另τv0/τa~Beta(α,1)，故完整分布非单个Beta；全support非ADP硬资格区间。validcoordsdenominator不除Σq，q只权直接actionflow；futureflow和PFD不加q。零mean条件独立Gaussian解释只在同conditionalmean下给高噪收缩，F明确systematicretargetbias不被更强corruption/weight自动消除。

EMAteacher只含coupledmodule与conditioningprojection，排VLM；复用detachedcurrentcontext，teacherFP32无梯度，真实futureτv0、同actionnoise/time/mask，对student早层经MLP对齐teacher晚层stopgradcosine。Teacher非独立真值；S1sync/noTeacher→S2新20kh人数据并replayS1与两机制，不能把阶段效应拆给单机制。无机器人future部署，双流仍共同采样；stageboundaries与invalidpadding/attentionmask分责。人跟踪/solver失败可holdprevious，diagnosticflags不自动定义validitymask，kinematicjointlimits不约束物体接触/碰撞。

关键reduced1/10预算：baseline52、reliability54.3、teacher56.3、both58.6；但PnP reliability53.1低baseline53.4。D3固定corruption只把qweight换1得到54.2≈54.3，因此不授downweight独立关键cause；q.2/.5/.8均54–54.3，coarseprior非精确noiseestimate。TeacherposttrainAvg70.7→72.8却Art81.7→75，visionleadingpath最后Art80仍低81.7，非各任务单调。3/10/30kh比例/预算matched scaling仅三点OLS，baselinebestcheckpoint而非overfitendpoint，不授普遍scalinglaw。RoboCasa24task各50episode，100/1000demo；real四task各100demo/20trial，π.5重置58D新层等pretrain接口不同，publishedbaseline非总预算matched。4B/130D/30chunk/globalbatch2048、100k+200k、BF16/22kH200GPUh已披露，精确推理硬件/batch/concurrency/tailSLO及全重复seed/CI未闭，不补数。Future/EMA偏差、source内变化、全部actionlabels/retarget/过滤/双流和teacher费保留；未核代码/运行训练或实机。

### 23.12 32094 必要完成（5分）

[TTT in VLA Models: Exploring Training with Human Demonstrations](https://arxiv.org/html/2610.32094v1)，exact-v1，R35准入/日身份与R173的局部2+1+2=5复用（原预6保在§23.1）。实际读§3.1/Alg1、3.2受影响write/read与两core、3.3/Alg2完整boundary、4.1–4.4关键negative、6.1/6.3/6.4与B1–3直接contrastive反侧；支持采用域足，不读全机器人附件/复现。

slowweights外环、每轨迹/层/head独立fastMLP内环，Finit学得；当前features QKV内重建K→V再Q读，gatedresidual，写selectedtokens一次。InternVLA每generation/actionexpert层TTT，state/register写/动作只读；π.5 18actionlayer独立writebranch读prefix，no noisyaction，onceperanchor后10denoise只读，memory非attentionKV。两coreFP32fast但normalization/shape/LR不同，不凭η1v.03排名。每trajectoryreset、shortertrajectoryfreeze不贡献loss，human先按videoHz写无robotloss，robot再按chunkanchors读并续写。

TBPTT每段反传后detachfastgraph但保数值，slowgrad段间累积到全trajectorybatch结束才step并不恢复时序梯度。human/robottransitionsegment只连最后human与最初robotanchor，早cue/晚target仍可隔断；writeHz与anchor数共同决定秒级覆盖。GTstate训练的memory带历史但nextstate为示教，ARstate仅由previouspredictedaction近似nextstate，图像仍录制，非真实闭环；本实现不把finalpredictedaction直接写fastweights。WarmupTTTdeltaMAE改善而real73%低baseline90%，TTTabsARMAE更低但real64%，成功分母/CI未披露不作显著性。

654paired/621train33val（完整pair切分），Intern20kTTT预训+30k/60k、π.5 60k预训+30k/30k两初始化，videoHz1.5/TBPTT16或4；杯目标三选一成功低1/3且with/withoutdemo趋固定位置。改273shortpairs/264train9val、wholepair一段保完整梯度后10k25%、60k13%，不是matched单因素只改gradient（数据/阶段/chunk50变）；故不以“连图就足”或“断图唯一根因”解读。Singleframe210pairs/200train10val/seed42仍低33%，不是TTT无法存储任何cue。B固定R/images/state/prompt/flow noise/time换Hmemory，全B²pair，zero-marginhinge在equal无梯度；contrast梯度仅经terminalmemory回human、不直接robotprediction；两组lossaggregation也不同。10k标准real25%/regular12.5%，with/withoutdemoMAE变化绝对<.15%且符号不齐，5倍walltime，不能把不改善当普遍反证所有contrastive。2GPU/global4trajectory/FP32fast已披露，完整硬件类型/实机trial分母/多seedCI/端到端SLO未闭。写入/保留/消费根因未辨与scale有限仍保，未运行代码/训练/机器人。


### 23.13 用户额度暂停 checkpoint（2026-10-27）

root已传用户明确因额度立即保存并暂停；本作者收到后已停止新增研究、网络抓取、评分、Books写入与推进下一候选，不为凑闭环补PRE/POST。此节仅保存真实停点，不改Report/State/index，不stage/commit/push。§22五项全闭复用：32941 R162=6/I、31859 R164=7/I、32102 R167=5/I、32969 R176=6/I、32348 R179=6/I，各精确位已释放；不重既成必要或POST。

当前§23五项仍均R35准入/日身份有效、R173最低投入6/5/6/6/5有效；不重AB/date、不扩来源、别日或机器人附件。逐项停点：

- **31762 RepresentNav：** 必要6/actual Ch25/§23.5原三件整体PRE已R184通过；作者已按许可真实SAVE并完整selfread（§23.10），**截至此暂停记录未收到sole actualPOST，不记I，不重复插入**。Ch25正文257/独立marker258/本人注1796（按本次SAVE时定位，后续并发可能移行）；完整DT-JEPA两段+32657marker前肩→Next-observation标题/首完整段后肩，原稿/marker/本人注与旧04390首注全部match、canonicalstrip恢复fresh SHA c8ac33acb141efd3c6d38f2597fb9fd869509580d4cb12496aac97ed2168cf38、限定diffcheck过。本窄位尚未释放。恢复第一处为sole reader实际POST而非再SAVE/Methods；reader已收到暂停，不在暂停后补核。
- **31801 KiRoSe：** 必要5 §23.4、actual Ch23具体NC/gap及完整原三件§23.6 ready，已交sole reader；**尚未收到PRE、未SAVE**。root已授离散codes完整段后→量化前扰动2602.18252完整段前本单段/独立marker/本人注，属未执行窄授。恢复只接必要/owner/原三件PRE缺层，不重Methods或准入。
- **31834 WorldMirror：** 必要6已足§23.8、actual Ch25一般NC/窄gap与整体原三件§23.9 ready并已交sole reader；**未PRE、未SAVE**。root已实际确认2605.15843对象化完整段/inline marker后→2509.26055静态edit完整段前无冲突，与31762位不同；原稿保存§23.9，属未执行窄授。恢复接sole必要/实际owner/PRE，不再全工具或机器人附件。
- **31845 EgoForesight：** 首次有限必要6已真实完成并存§23.11，尚未独核、actualowner结论/整体PRE/SAVE均未成。仅准备actual Ch26比较：已实读Training-only foresight/既有PFD2604.25859完整两段、邻directed31394及数据演进相关接口；一般future特权/全费已有覆盖，可靠性调actioncorruption-vlossweight与未来teacher分责是否有最小差额尚未收口。**没有申请或获得具体Books位，不写。** 恢复接actualowner比较/具体NC或最小稿，不第三Methods。
- **32094 TTT human demonstrations：** 首次有限必要5已完成并存§23.12，原预6与局部R2→1理由保§23.1/R173。尚未独核、actualowner结论/整体PRE/SAVE均未成。已实读actual Ch26 episode-state整段、固定EMA12942、signature14551、教师history/consumption及memory audit27247；一般state身份/credit/敏感不等利用已有，但fastweight数值延续-v梯度连通、跨humanrobot transition与局部negative差额未收口。**没有申请或获得具体Books位，不写。** 恢复接具体owner判断，不重Methods/全contrastive附件。

在途状态：没有运行中的terminal、curl、functions exec或网络请求；最后有限HTML返回已结束，未启动训练、代码/机器人或模拟。已向唯一reader发停止通知；不再等新核或自行补POST。仅31762存在已SAVE未POST，31801/31834为未执行具体窄授，后两无Books授权。下一步须用户明确恢复后沿原唯一pair接31762 actualPOST、前两ready包缺层及后两actualowner/必要独核；当前暂停不代表本批/全Daily完成。
