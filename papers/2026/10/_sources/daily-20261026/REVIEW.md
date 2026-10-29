# Daily 2026-10-26 独立复核

复核者：`live1026_review`，唯一非 writer reader；作者为 root。只写本文件，不写 Report、Books、State 或公共合同。窗口固定为北京时间 2026-10-25 自然日；没有恢复其他日期的研究工作。启动已完整重读 AGENTS、当前 Research/Report 合同、每日来源使用说明、Research Prompt、ROADMAP 与本轮相关 checkpoint；工作树已有大量并发修改，全部保护。检查日为 2026-10-26。

## R1 首批准入校准

- **Recycler：通过，2+2+3=7。** 独立请求[Seed 官方页](https://seed.bytedance.com/zh/public_papers/recycler-cost-free-latent-reasoning-via-hidden-state-recycling)，实际正文日期 `2026-10-25`，完整题摘已读；web 文本入口失败后由官方 HTML 恢复。原有约束不是“AR 没有连续历史”，逐层 KV 仍保存连续状态；实际增量是上一 token 顶层 hidden 经轻量 adapter 加到下一 token embedding 的额外路径，以及由此产生的训练/Prefill 近似与 decode 递归不匹配。它可改变对连续跨步信息、额外位置与同位置 loop 的表示选择，符合 MODEL-DECODER-ONLY 主线。标题中的 cost-free 与摘要的 2–3× 不作已验证结论；不是由 Books 是否已覆盖倒推准入。
- **Kimi Code 2.3.2：通过，1+2+1=4，深入相关兼容/权限域。** 独立读取[release](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%402.3.2)、[PR4384](https://github.com/MoonshotAI/kimi-code/pull/4384)、[PR4386](https://github.com/MoonshotAI/kimi-code/pull/4386)核心说明与理由；官方 API `published_at=2026-10-25T07:59:14Z`，落本窗。4386 仅改 prompt 默认委派，不把它写成执行层安全保证；4384 才改变 swarm 可执行资格、二次检查和旧记录回放语义，并使没有人工开启入口的 print/ACP 无法使用 swarm。具体兼容/权限改变足以准入；成熟授权原则本身不加分。仅报告可接受，仍须作者说明与实际长期 owner 的差异。

## R2 Recycler 必要原文与实际 owner

独立读取官方[18页 PDF](https://lf3-static.bytednsdoc.com/obj/eden-cn/hyvsmeh7uhobf/recycler_arxiv%20(2).pdf) p1–13 中所有采用相关方法、评价文字/表格和直接反侧；p14 仅参考身份，不遍历无关参考。首页 Date October25,2026 与官网一致，未补造 arXiv ID。读取为官方 bytes 的 pypdf 内存抽取，未核代码、图像素或复现实验。

- §2.1 Eq2–3：`A(h)=Linear(RMSNorm(h))`，`Emb(x)+A(h_previous)`，保留离散 token 通路。§2.2.1 decode 递归深度随输出增加，并不是每 token 额外完整 backbone pass。
- §2.2.2 Eq4：前一 pass 的前一位置 hidden 支持本 pass 所有位置并行；每 pass 有 NTP loss，浅 `k_train` 不等一般完整顺序状态。零初始化、tied embedding 是该配方，不授任意 untied backbone 兼容。
- §2.2.3：一 pass Prefill 与普通 prefill 计算相当，二 pass 明确增加一次完整 prompt 计算；§2.3.2 的 prompt 区域 recycle mask 与部署 prefill 相配。不能由相同 decode 层数宣称完整请求免费。
- §2.3.1/Fig3–4：小模型浅训练向更深 decode 有受限稳定结果，但更大模型/数据确有 extrapolation loss 回退；部分三 pass 增加训练费用。原文“fully resolving”不外推无界稳定。
- §3.1/Fig5–7：token efficiency 未扣除两 pass 训练计算；model β 同大小 baseline 轨迹较短，原文明示不把三个终点视为 equal-budget。
- §3.2/Fig8：累计 FLOPs 为估算，PT/CT 与 SFT suites 不同，只能比较 suite 内成对点。Table1/相邻正文存在 IFEval、ArenaHard 等局部反退，不能写所有任务改善或 prefill 配置可任意替换。
- §3.3/Table2：完整路线来自不同 SFT 起点，code revision 与 rollout schedule 有差异；作者明确不授独立 RL 阶段 equal-compute 因果，且人工中止未收敛。不得据此授更高真实能力上限。
- §4.1/4.2：区别在连续路径与可见 token 共存，不是取消 CoT token；跨 token feedback 与同 token loop 的职责不同。Introduction 的 MTP parallel-verification 宣称没有相应算法正文可支持，不补造 speculative acceptance/commit。
- 主实验 α/β 精确规模、硬件/precision、完整输入输出分布、batch/concurrency/SLO 与端到端时间未披露；151M active/1B total 仅为 Fig3 小模型，不移给全部实验。

实际 owner 已读 ROADMAP `MODEL-DECODER-ONLY`/Ch18 的“从显式 CoT 到 Latent Reasoning”完整相关段及前后过渡、loop 监督/停止分支、末尾 KV/Sampling 交接；并读 Ch17 开头、Ch19 开头和 Ch44 相关状态分支。现有正文已覆盖 latent transition、hidden/embedding 接口与 loop 稳定，但尚无“离散 token 与跨 token 顶层 hidden 同步共存，浅 parallel passes 训练/Prefill 与长 decode recurrence 分离”的具体机制。有限整合 Ch18 合理，不应在 Ch44 重复推导或新造结构 owner。本项必要证据层通过；尚未作拟稿 PRE 或实际 POST。

## R3 Qwen 动态来源的可执行恢复

独立打开[Qwen Research](https://qwen.ai/research)文本仍0行，但官方 HTML 92469 bytes 并非空正文失败证据。当前公开 JS 版本 `qwen-ai-fe/0.0.85`：

1. HTML 明示加载 `https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/969.js`，其 module44467 定义 `/api/v2/article/retrieval`、`research.research-list` 和 `research.latest-advancements-list`。
2. 同站公开 `framework.js` 明示 research-index 使用 `js/p_research-index.js`；该模块实际调用 `j({type:"qwen_ai",language:"zh-cn"===t?"zh-CN":"en-US"})`，并读取上述 page configs。不是猜测私有/管理端点。
3. 实际 GET [article retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)，附随机 X-Request-Id：`success=true`、`data.articles`40项；读取全部身份/日期，没有分页元数据。最大 `extra.date=2026-09-20T20:00:00+08:00`，末项 `qwen-image-2.1`；其余最新包括 Sep18 Omni/LiveTranslate、Sep3 E-Commerce/Drive，均无 Oct25。列表本身不按日期有序，不以首项 Nov2025 截止。
4. 实际 GET [research-list config](https://qwen.ai/api/page_config?code=research.research-list) 返回完整 list60，读取全部身份/日期，最新 Dec23,2025；[latest-advancements config](https://qwen.ai/api/page_config?code=research.latest-advancements-list) 返回完整 list19，最新 Sep24,2025。未逐读这些旧材料方法，不扩全年研究队列。

**纠正要求：** 不再保留“实际JS仅定位config、retrieval未恢复”的旧失败说明。可写本次已经核查 Research UI 实际消费的公开 payload40+config60/19，未发现确定 Oct25 事件；目录内容滞后/未提供日级首次公开保证仍需明确，不把恢复到正控列表等同全站无遗漏，也不从旧内容反推所有2026发布均不存在。补检查或隔离范围应由这一真实结果限定，而非一次浏览器超时。

独立重开 Google Publications 确认为年份/会议排序目录（无按日首次公开筛选），Meta Research 仍0行；两项不能授 Oct25 零更新，作者隔离其日级边界正确。独立打开 cs.CL recent 日期导航为 Mon26 / Fri23 / Thu22 等，无 Sun25；没有逐篇读取 Oct26 论文或移动其日期。

## R4 actual owner 补充比较与唯一 PRE

作者提供了此前未比较的 Ch17 精确现有段位。补读实际正文 628–680 行的完整分支，尤其 `2610.25086`双slot、`2602.17993`高→低投影、`2610.25076`单core feedback/Jacobi，以及 ACT 停止器直接后肩；同时核 Ch16→17 和 Ch17→18/19 的原交接。由此**修正 R2 的初步 owner 建议为 `MODEL-TRANSFORMER-LAYER` Ch17**：该章已经拥有内部跨位置计算与高低层反馈，不应把这条完整机制再复制到 Ch18。Ch18 拥有是否取消/压缩中间可见 token 的表示/生成接口，而本次采用保持每步离散 token、补足既有 feedback 分支中完整顶层→输入及浅pass训练支持配对。这个更具体的实际 owner 比较是改判依据，不是变更原文准入或重复审方法。

**PRE 通过。** 已逐字读取 SOURCE“Recycler 当前owner与最小稿”两段、marker 与本人 Review notes 拟注。授权范围仅为 Ch17 `SF-2026-ARXIV-2610-25076`完整单state段后、ACT停止器首段前的该两段与 `SF-2026-SEED-RECYCLER-20261025` marker，以及 true H2 Review notes 下本人一条证据注；不得改写旧两肩或新增第二owner。

两段正确保留 token/KV、区分 full-top/embedding 与 middle core/same-token/latent positions；各pass NTP、浅训练/长递归、一/二pass Prefill、额外状态/训练和局部退步都在机制附近。非等预算与未披露服务条件阻止从近似逐token计算推端到端免费，fallback与相邻core分支衔接可顺读。本人注只引用必要证据层，不把 PRE 当 actual POST 或 DAY。作者可按该完整稿真保存并自读，之后只进行一次实际 POST。

Kimi 兼容/权限域补核官方 PR4384 files API16文件中四个直接执行/回放patch：`agentSwarmTool.ts`两处 `isActive`、`swarmService.ts`拒绝`tool` enter、`swarmOps.ts`保原状态、`foldFacts.ts`保marker但不启用。所读patch与R1/报告采用命题一致。此为公开实现证据，不是本轮运行测试；4分仅报告关闭通过。

R3 请求停止点补明：retrieval40的日期范围为 Nov13,2025 至 Sep20,2026，两个config完整响应长度分别60/19；仅取身份/日期核本窗，没有把其中旧条目送方法队列。没有请求未知分页/私有目录或穷尽所有GitHub仓库；未由响应无 pagination 字段推断互联网完整性。网页真实组件消费的三个列表均已实际核，不再留普通可执行恢复待办。

## R5 来源范围与分层排除抽检

先对作者 SOURCE 全14个每日 ID 的实际入口、主题/窗口、查询参数及停止依据作范围复核：没有每周源混扫、全年论文逐项关闭、catchup90天或把 Oct26 的论文搬到 Oct25。独立重新请求了其中9个来源 ID 的决定性入口/原件：OpenAI、Anthropic、Google Publications、Meta、Qwen、Moonshot、Seed、MiMo、arXiv；其余5个 ID（DeepSeek/Hunyuan/ZAI/ERNIE/MiniMax）在本轮只审作者记录与停止声明，没有独立重抓全目录，不把抽检写成全量再验证。Qwen失败范围被R3实际公开接口纠正；其余已核来源未发现共同错误理由。

明确排除项按三类抽检五个具名例子，不构造全部旧材料分母：

1. **重复代码事件**：独立请求 Qwen `v0.26.1` 与 `desktop-v0.26.1` 两个官方 git refs，均直接指向 commit `b475278c4a300acebe6cfc990a9e1b1d18819bfc`。精确读取前日报现有 v0.26.1 行/证据段，证明该代码事件已有有效处置；这里只去重同代码，不验桌面包分发安全或全部生态能力。
2. **清晰窗外**：OpenAI Research News 首批最新“Securing our frontier model training environment”Oct23，随后 Oct21/19；Anthropic Most recent 最新“AISI cybertesting incident”Oct23，随后 Oct20/16；Seed newest-oldest 的 Recycler Oct25 后紧邻“Periodic Weak Spots”Sep28。直接日期/顺序与作者停止依据一致，这三项旧文不进入本日方法审阅，不因安全标题将已明确窗外材料搬入本窗。
3. **暂缓范围**：MiMo 首页“New Materials R&D”说明为文献/分子设计/PFAS capture 的材料应用，标题说明足以落 ROADMAP AI for Science 暂缓；没有把它经 Agent/Evaluation 重新纳入主线。首页本身确无这些Blog日期，不能凭可见最前项把隐藏More宣称全覆盖；作者隔离此局限合理。

全部拟入选两家族均已独核，不仅抽样；Kimi具体权限/兼容变化已核实际相关patch，未遗漏为“普通小修复”。arXiv独立日程确认当地Fri/Sat无常规公告，Oct25周日20EDT对应BJT Oct26；cs.CL recent真实Mon26/Fri23导航与此相合。这只关闭本窗常规公告批次判断，不证明全网无作者稿。GooglePubs/Meta保留项不支撑 Coverage通过或零发布；Qwen当前可用列表恢复后的准确表述仍待作者同步正文。

## R6 Recycler 真实 SAVE 后检查

已实际读取 Ch17 654–674：完整新增两段、family marker、前置 `25076`完整单state段及 ACT完整直接后肩，另读 true H2 Review notes 中本人新注与邻接；内容与PRE相同，旧两肩没有被本项覆盖，局部质量/预算/状态边界保留，未出现Ch18第二owner。限定 Ch17/Report/SOURCE/REVIEW 的 `git diff --check` 通过。不是把全仓并发修改当本项 diff。

发现一个符号表述可收紧点：首句“经 RMSNorm 与学习投影 A”可能令 A 被读作仅Linear，与后式 `A(h_t)` 省略Norm的读法不一致。要求改为“经由包含 RMSNorm 与线性投影的适配器 A”，精确对应 Eq2 的整个 A。这是局部表述修正，不重审必要源或重写其余稿；该行真实修正后读回即可关闭本项实际 POST，尚未签 DAY。

## R7 进行稿机械校验与行政修正

当前 Report 的 Qwen 行/SOURCE 已实际读回：R3恢复路径与40/60/19停止范围被正确同步，旧“只找到config/未恢复”的失败标签移除。仍保内容滞后不授全站零、桌面包安全未验等边界。

实际运行 `python3 scripts/validate_research.py --report papers/2026/10/26/README.md` 得四个明确错误，已发作者：GoogleAI/MiMo为必查来源，其具体目录缺口应标“受阻”而非仅可用于补检的“检索受限”；两个候选§3的材料link label与§4小标题未精确一致，需统一标题。进行稿仍有预写/待PRE/待POST叙述，最终需按真实已成状态更新；本轮没有把机器错误或普通未做工作隔离成外部保留项。最终DAY待修后保存与复核，不因目前候选只有两家族省略验收。

## R8 唯一 actual POST 闭合

作者按 R6 窄修后，已直接读回 Ch17 第660行：`h_t`“经由包含 RMSNorm 与线性投影的适配器 A”，与后式 `A(h_t)` 及原 Eq2 一致。其余完整两段/直接两侧/marker/本人true H2证据注的 R6 实际检查有效复用，不重新读取相同附件。**本项唯一 actual POST 通过**，Recycler 的有限 Ch17 整合实际生效，指定两段与本人注窄位释放；未实现、测试代码或复现实验，不授免费性能/生产能力。

R7四项行政修正后，实际再次运行本日报 V3 校验已通过；这仅为机械字段/引用检查，不代后续完整DAY与作者最终完成保存态读回。

## R9 MiMo More 伪缺口纠正与有限日期闭合

DAY检查发现 R5 对作者“隐藏More未知部分”的接受过宽，现纠正：主页原 HTML 中 `button aria-controls="blog-more"` 只控制 `div id="blog-more" data-expanded="false"`，该div包含09–15七项，正是已读Blog15的后七项，不是另一个未知分页目录。**不能保留“More目录受阻”这一伪缺口。**

只恢复这15个既见身份所需日期，不开启全站研究：主页公开加载[4752.2908c99e.js](https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js)，其精确 route/preload 与[index runtime](https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/index.3082e2d7.js)公开chunk映射，定位各对应async页面。实际核八个wrapper的iframe `src`，以及V2.6组件的`/mimo-v2-6/article.html`，取得原件日期如下：

| 首页序号/身份 | 实际原件/日期依据 | 本窗处置 |
| --- | --- | --- |
| 01 Tool-call repetition | 对应manifest frontmatter `2026-09-27`；作者已读该原文 | 窗外，复用原日期，不读旧Methods |
| 02 V2.6 | [article.html](https://mimo.xiaomi.com/mimo-v2-6/article.html)正文 `September22nd,2026` | 窗外 |
| 03 New Materials | 标题/说明直接为分子设计与PFAS材料应用 | AI for Science暂缓；日期不影响排除，不追其日期 |
| 04 Code / 05 UltraSpeed / 06 inference | manifest对应原文frontmatter依次 `2026-06-10` / `2026-06-08` / `2026-05-30`，与作者既有原件核对相同 | 窗外，不重复旧Methods |
| 07 ASR / 08 TTS | [/mimo-v2-5-asr/index.html](https://mimo.xiaomi.com/mimo-v2-5-asr/index.html) / [/mimo-v2-5-tts/index.html](https://mimo.xiaomi.com/mimo-v2-5-tts/index.html)均正文 `April2026` | 月精度已经足以排除Oct25，不补造日 |
| 09 V2.5-Pro | [/mimo-v2-5-pro/index.html](https://mimo.xiaomi.com/mimo-v2-5-pro/index.html)正文 `April27th,2026` | 窗外 |
| 10 V2.5 | [/mimo-v2-5/index.html](https://mimo.xiaomi.com/mimo-v2-5/index.html)正文 `April22nd,2026` | 窗外 |
| 11 V2-Pro / 12 V2-Omni / 13 V2-TTS | 对应[/mimo-v2-pro/index.html](https://mimo.xiaomi.com/mimo-v2-pro/index.html)、[/mimo-v2-omni/index.html](https://mimo.xiaomi.com/mimo-v2-omni/index.html)、[/mimo-v2-tts/index.html](https://mimo.xiaomi.com/mimo-v2-tts/index.html)，正文均 `March18th,2026` | 窗外 |
| 14 V2-Flash | [/mimo-v2-flash/index.html](https://mimo.xiaomi.com/mimo-v2-flash/index.html)正文 `December16,2025` | 窗外 |
| 15 Humanities/Social Sciences | [/blog/mimo-v2-flash-hss](https://mimo.xiaomi.com/blog/mimo-v2-flash-hss)正文 `December22,2025`，manifest日期Dec19,2025 | 两口径均明确窗外；不为不影响处置的日期差异追无限版本史 |

wrapper路由直接文本只有壳不是必要原件不可得，准确iframe目标才能恢复日期。本次八wrapper的公开src与实际读取目标一致，未访问私有接口；没有遍历manifest其他路由，也未将15项重建成旧全文队列。当前主页Paper8有显式旧日期，Blog15均已按窗外或清晰暂缓关闭，无MiMo具名普通待办/外部日级缺口；仍不宣称互联网或未公告渠道绝无漏项。作者需据此将MiMo来源改“已检查”、移除§5伪More保留项，R5旧表述被本节精确取代。

## R10 唯一完整日级语义验收 DAY

**结论：通过，达到本窗安全终态。** 最新六部分已完整读回；R1–R9已成证据/范围/日期/抽检及真实POST有效复用，不重复全源。窗口保持BJT2026-10-25；14来源记录、9独立重开/5仅审记录和五具名排除样本的未查边界保留，Qwen恢复/MiMo伪More纠正已真实同步。

最终2唯一家族＝Recycler7分实际整合Ch17一项（R8 POST）+Kimi4分仅报告一项；相关反侧、费用与非证明边界保留，无第二owner/实现复现承诺。外部仅GooglePubs/Meta两日级目录gap，精确隔离且不授Coverage通过/零发布；普通研究、Books或POST待办0。只余作者行政完成SAVE及reader终存读回，不重有效研究层。

实际V3、Report/SOURCE/REVIEW/Ch17限定working+cached空白检查通过，本地引用核对无缺失，不称全仓clean。已有并发index/working内容保护，本reader未stage/unstage/commit/push；最终SAVE后只核行政字段与机械状态。

## FINAL 最终保存态读回

作者最终README已实际读回：状态完成、两家族＝1整合/1仅报告、§5普通待办0且仅GooglePubs/Meta两外部终态、§6通过引用R10。最终V3及限定working/cached空白检查再次通过；未重读Source/Books或重新验DAY。R10有效，作者行政终存闭合，本reader结束本日；无stage/unstage/commit/push。
