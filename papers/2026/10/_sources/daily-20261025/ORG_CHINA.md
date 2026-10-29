# Live Daily 2026-10-25 — 中国机构来源

窗口：2026-10-24 ～ 2026-10-24，北京时间完整自然日。执行：2026-10-25 11:57～12:18 +08:00（本轮工具时间为依据）。作者：live1025_org_china。仅负责本文件；不改 Report、Books、State、索引或 Git index。

按本日重新读取 AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、RESEARCH_SOURCES 使用说明与每日组、CODEX_RESEARCH_PROMPT、ROADMAP；旧日期仅对精确身份去重。机构目录、GitHub updated、提交日均不直接等同本窗首次公开。以下是有界来源检查，不宣称机构全网召回。

## 1. 覆盖、真实入口与停止点

| 来源 | 实际入口、停止点 | 本窗结果与限制 |
| --- | --- | --- |
| SRC-TENCENT-HUNYUAN | 首查 [Research](https://hunyuan.tencent.com/research)，文本空；浏览器创建与绑定两次超时。随后读取该页实际加载的公开 bundle，恢复“全部”列表接口（下节）。实际 `totalNum=11`、返回11条，读完本页全部标题/日期；另读 [官方 GitHub](https://github.com/Tencent-Hunyuan) 最近10/90仓库及 [T1](https://github.com/Tencent/llm.hunyuan.T1) README；只追踪已见 Hy-Memory/Hy-Nomas 具体线索。 | Research列表无10-24展示/发布字段；目录不是空响应归零。GitHub有本窗活动，但Hy-Nomas为README推理示例、Hy-Memory为既有SDK迁移/界面实现修复；论文精确去重如下。没有将旧论文或普通活动重新计候选。 |
| SRC-ZAI | [官方 Research](https://www.zhipuai.cn/zh/research)“全部/时间排序”可见首屏15项（08-26～2025-12-09）；最新项GLM-5.3-Flash 08-26已早于本窗，停止在首屏，不点“查看更多”扫旧档；[官方 release notes](https://docs.z.ai/release-notes/new-released)首条08-26；[zai-org](https://github.com/zai-org)最近10/53仓库最新GLM-V、zcode-plugins为10-23。 | 已检查上述有界入口，无确定当窗研究事件。没有从空页或搜索零命中推断没有发布；查看更多后旧目录未扫，不宣称全仓库/release历史覆盖。 |
| SRC-BYTEDANCE-SEED | [Research/Blog](https://seed.bytedance.com/en/research)可见Blog专题及论文；[Publications](https://seed.bytedance.com/en/public_papers)明确 newest→oldest，Page1/13、1–20/246，最新09-28《Periodic Weak Spots》，至05-26，停止Page1。置顶无日期SeedRealtime原文核为08-05。[官方GitHub](https://github.com/ByteDance-Seed)最近10/63，定点VeOmni/VINCIE。 | 无确定本窗新研究候选；VINCIE本窗`update env`不是新机制事件，VeOmni当前latest release 09-30；不把repo updated解释为论文日期，不扫其余12页旧论文。 |
| SRC-BAIDU-ERNIE | [技术博客](https://ernie.baidu.com/blog/zh/)首屏8项，从05-09文心5.1至2025-12-23；[Publication](https://ernie.baidu.com/blog/zh/publication/)仅4项，至ERNIE5.0技术报告；[ERNIE官方仓库](https://github.com/PaddlePaddle/ERNIE)Recent updates至2025-11 v1.5。 | 已检查可见目录，无本窗具名事件；不从旧repo README外推整个百度无研究，不扫无关Paddle生态。 |
| SRC-XIAOMI-MIMO | [MiMo Paper/Blog首页](https://mimo.xiaomi.com/) Paper 01–08、Blog 01–15可见标题；论文最新06-29 MOPD。博客缺日期/普通可点击href，定点恢复最前沿6项中的5项主线原文（下节），另材料研发项按暂缓范围排除。读 [XiaomiMiMo](https://github.com/XiaomiMiMo)最近10/18，最新MiMo-Code updated10-23。 | 没有确定10-24候选。博客不能据首页序号证明严格时间排序；采用原文日期而非“首页首条即今日”。可见旧产品条目不形成待全文队列，也不声称隐藏“More”历史已全扫。 |
| SRC-MINIMAX | [英文Blog](https://www.minimax.io/blog)及[中文Blog](https://www.minimaxi.com/blog)（后者跳转minimax.cn），首条MiniApp10-22、其次M3.1Flash10-19，再到08-13旧项；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)首组10-20两文，下组10-08，停止越过本窗；[MiniMax-AI](https://github.com/MiniMax-AI)最近10/37，定点OpenAgentCore/minimax-code。 | Blog无10-24具名事件；OpenAgentCore发现具体当窗兼容/恢复机制变更，候选C1；minimax-code最新release为10-09，不把updated10-24计新发布。 |

辅助搜索只作定位，实际查询包括 `site:hunyuan.tencent.com/research "2026" "10"`、各官方域名与 `2026-10-24` / `Oct 24, 2026`、MiMo工具重复/长程Agent/UltraSpeed/推理优化的精确标题。没有用搜索首页或零返回替代上述官方入口。第三方命中只恢复MiMo官方路径，未采用其技术或日期主张。

## 2. 动态目录恢复与日期原件

### 浑元“全部”不是GitHub替代

Research HTML实际脚本：

- [index-3gZjLsMD.js](https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-3gZjLsMD.js) 路由 `/blog` → `index-CrZ8mUpC.js`；Research同用该组件。
- [列表组件](https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-CrZ8mUpC.js) “allTab” `renderType:0`，实际调用参数 `{pageNum:1,pageSize:1000,renderType:0}`。
- [公开请求定义](https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-BB5SXEwE.js) 指向 `POST /api/blog/publicList`；API基址来自官网脚本公开host映射。
- 实际只读列表请求：[publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，Content-Type application/json，accept-language zh，以上参数；响应 `code=0, data.totalNum=11, data.list.length=11`。非管理API，不需要认证，未尝试绕过访问控制。

返回顺序/身份：100119 Hy Image3.5 preview；100116 RL Batch Size Scaling；100100 Hy4 preview；100091 ELR；100087 Hyra；100064 Hy3；100041 Hy-MT2；100039 Real life/context；100061 Hy3 preview；100015 GradLoc/Layerwise Clipping；100025 Learning from context。

最新两项 `displayPublishTime=1790006400`，JS转Asia/Shanghai为09-22；对应 `publishedAt=1789959110` / `1789749798` 分别09-21/09-19。官网搜索缓存显示09-21，与展示字段存在日期口径差异，但各界均远早于10-24，本次无需为旧项追首次公开精确日。其余返回展示字段08-28及以前（到02-03），不是本窗候选。不得把UI以何时区格式化与first-public混同，也不把build-time `2026/10/23 13:31:10`当论文发布。

### MiMo无日期首页的定点恢复

| 原文 | 原文日期/结果 | 本次处理 |
| --- | --- | --- |
| [工具调用重复复盘](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition) | September 27, 2026；末段API新checkpoint为09-25 | 窗外。正文确有奖励阈值盲区/专用teacher融合增量，但不搬入10-24；没有在本窗重新评分或作Books采用。 |
| [V2.6发布正文](https://mimo.xiaomi.com/mimo-v2-6/article) | September 22nd, 2026 | 窗外；封面只有链接，实际打开article确认，未拿封面空文本作无事件。 |
| [新材料研发案例](https://mimo.xiaomi.com/blog/mimo-v2-6-material-research) | 标题与首页说明明确PFAS材料设计/干实验 | AI for Science暂缓；不借通用Agent/工具术语回流。日期不影响范围排除，不继续恢复iframe。 |
| [MiMo Code长程任务](https://mimo.xiaomi.com/blog/mimo-code-long-horizon) | June 10, 2026 | 窗外，不依据第三方转载10月日期归本窗。 |
| [UltraSpeed](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | June 8, 2026 | 窗外，未采用1000 TPS宣传为本窗性能结论。 |
| [推理全链路优化](https://mimo.xiaomi.com/blog/mimo-v2-5-inference) | May 30, 2026 | 窗外；不因HBM/KV/PD owner相关就重列。 |

### 精确重复与实际更新的区分

- [Hy-Memory-30B-A3B arXiv:2610.22196v1](https://arxiv.org/abs/2610.22196) 当次页面仅v1，提交10-15，并不是公开日证据；精确既有 [10-17 Daily](../../17/README.md) 候选表与§4已经以10-16公开归属深入审阅/整合。当前身份、版本不变，本窗不重收。DataCite辅助web入口报不可达不推翻已有精确事件；本次无必要追另一组日期证明。
- [Hy-Memory](https://github.com/Tencent-Hunyuan/Hy-Memory) 本窗9条default-branch commits，当前latest release `hy-memory-v2.0.5`发布10-22；SDK权威迁移此前 [10-23原记录](../daily-20261023/ORG.md)已有具体机制。10-24定点可见队列/SDK memory map、停止旧bridge、升级修复与迁移校验，不以“修改多”或通用authority术语另造论文贡献。没有把本轮活动当既有论文重要修订。若主作者后续发现这些实现改变已采用具体论点，仅重开对应迁移命题，不重跑论文。
- [Hy-Nomas PR1](https://github.com/Tencent-Hunyuan/Hy-Nomas/pull/1) 10-24 08:09:41Z merged；PR正文只有“add Diffusers inference examples into en and zh README.md.”。这是既有模型的使用示例，不是新的world-generation学习机制或可比取舍，排除，不评分。repo创建10-21不独自证明论文first-public；本次也没有借此给旧论文定日。
- [VINCIE](https://github.com/ByteDance-Seed/VINCIE) README明确技术报告2025-06-12，最新News为2026-03-19评估代码。本窗唯一`97cd2c57`为`update env`；不把环境更新等同新block-causal diffusion机制。
- [VeOmni](https://github.com/ByteDance-Seed/VeOmni) 当前latest release `v0.1.13` 09-30；[minimax-code](https://github.com/MiniMax-AI/minimax-code) `v0.6.5` 10-09；本窗default-branch精确查询均空。这只描述已查分支/发布入口，不证明所有分支与issue无变化，也不是每日扩扫PR的起点。

具体GitHub日期线索恢复查询为 `/repos/<已见repo>/commits?since=2026-10-23T16:00:00Z&until=2026-10-24T16:00:00Z&per_page=100`（default branch）及 `/releases?per_page=5`。只用于上述已见身份，未逐个扩所有机构仓库。OpenAgentCore当窗29条返回，未有下一页；普通清理/文案/导出/API装配条目不逐篇行政审计。下一节仅读与拟采用机制直接有关的#846。

## 3. C1：OpenAgentCore direct-provider checkpoint/lease边界

原件：[PR846合并commit 07bbac7e](https://github.com/MiniMax-AI/OpenAgentCore/commit/07bbac7ea4530fd08fe5d86e4ea80961fb0758aa)，committer `2026-10-24T02:07:13Z`，合并事件北京时间10-24。事件是实现/协议修改，不是新论文或正式release（当前latest rc2仍10-22）。来源家族MiniMax OpenAgentCore，本窗只记一次。

### 准入与评分（交独立校准）

原checkpoint只适配node registration、续租定位initial incarnation → 本次给direct E2B引入native pause/resume，并让同一native sandbox跨多个logical generation、为当前代增加RenewCompute和endpoint/template兼容约束 → 需要修正“restore一定新建native compute、按初始身份续租即可”的设计选择。不是把原有quiesce、operation ID或fence统一换词当增量。

拟评分 **2 + 2 + 2 = 6**：重要provider执行/身份边界；跨Core/Runtime/Provider；lease与恢复兼容性是可复用约束。标准审阅已完成源代码/协议范围；独立准入校准和Books比较交主作者。不预标已有覆盖或整合。

### 实际读过的精确位置

- [docs/sandbox-provider.md@07bbac7e](https://github.com/MiniMax-AI/OpenAgentCore/blob/07bbac7ea4530fd08fe5d86e4ea80961fb0758aa/docs/sandbox-provider.md)：Explicit operation contracts、checkpoint错误/代际约束、registration。精确patch把“checkpoint仅nodes”改为nodes/direct均可，增加`RenewCompute`，补充`Bootstrap.SuspendControl`的能力声明传递。
- [e2b/checkpoint.go@07bbac7e](https://github.com/MiniMax-AI/OpenAgentCore/blob/07bbac7ea4530fd08fe5d86e4ea80961fb0758aa/services/core/internal/sandbox/e2b/checkpoint.go)：该文件整份新增。开头明确同一个E2B sandbox跨allocation各代；`compatibility()`以installation+endpoint/domain与template构造两个digest域；`state()`核验name/native ID/generation/RestoredFrom/operation，不符不准认领；`Resume()`在native调用前拒绝不兼容snapshot或外部Workspace。
- [runtime_compute.go@07bbac7e](https://github.com/MiniMax-AI/OpenAgentCore/blob/07bbac7ea4530fd08fe5d86e4ea80961fb0758aa/services/core/internal/execution/runtime_compute.go)：`idleCompute`精确patch新增“有Runtime连接才RenewCompute，否则GetCompute”。旧Renew只针对initial incarnation；当前代续租是本次实际变化。`captureCompute/restoreCompute`已存在的原始流程只用于理解上下文，不冒称本次发明。

原始raw.githubusercontent访问先发生TLS/ECONNRESET；随后用GitHub官方contents API指定同commit，base64解码读取原文及commit API的精确patch。不是访问受阻后靠标题猜实现。

### 证据结论、代价与反侧

源码支持一个窄结论：同一控制面可以容纳“重建compute”和“原地暂停后重连”两种provider，但logical generation不能与native sandbox ID一一等同；续租、归属、snapshot可用性均要以当前代和provider特定兼容信息判断。E2B并非可任意搬迁的磁盘snapshot：同endpoint/installation/template域以外拒绝使用，外部workspace不被此adapter接受。每次检查须有deadline，未知结果仍错误，不自动把超时当成功或冷启动许可。

反侧/限制：没有运行单元测试、native E2B验收、注入故障或压测；代码中的校验不证明helper真实保持receipt、跨崩溃恢复已正确，也不证明暂停节省金额或恢复延迟。源文件变化和作者测试文件清单只支持“公开实现设计存在”，不等于production-ready。性能条件hardware/workload/batch/concurrency/SLO/evaluator均不适用：本次未作性能命题；真实native行为与成本未验证。

Books候选归属：`AGENT-PLATFORM` Ch84（Agent环境生命周期/原地暂停与迁移恢复边界），跨接`PLATFORM-FOUNDATIONS`只由主作者按现有具体论点判owner，不能同一论点多章重复入书。本作者未读Books上下文、未写书，不声称已整合。

## 4. 收束与重开

六源已完成本轮约定主入口及有界定点补检。没有必要正文仍待本作者恢复的外部阻塞；C1所需源代码已恢复，交主作者独立准入/证据/Books处理。目录的隐藏旧页、GitHub其他分支或全网未查入口不被宣称完成，也不形成无限待查队列。

浑元已用真实publicList补齐动态“全部”，不再把UI故障列成未解决覆盖；智谱/Seed最新排序列表已越过窗口即停止；MiMo首页无时间排序保证的限制如实保留。以后若出现具名10-24公告、真正重要修订或上述实现的反证，只重开对应身份。不能从当前未发现推导“六机构10-24绝无发布”。
