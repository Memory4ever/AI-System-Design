# 2026-05-18 增量来源补查：独立复核

复核者：`/root/may18_supp_reader`（非本日报告作者；不写 README、Books、LEARNING_STATE 或公共合同）。

## R1 — 独立初态与边界（2026-10-19）

已重读 `AGENTS.md`、当前研究合同、Report 合同、来源使用说明及 Daily/arXiv 恢复组、统一 Research 入口和 `ROADMAP.md`；月度 checkpoint 只确认本日 ownership。采用日报闭合 skill 的分层检查，不把机器通过或旧完成标签当本次语义验收。

- 本次仅补北京时间 `2026-05-17 ～ 2026-05-17`。原小时窗、64 个既有候选整行及其日期/评分、连续有效原 §4 块保留；不搬移旧候选，不继承别日候选池。
- 本日既有 `V3_FRESH_NONAUTHOR_POSTWRITE_FINAL_REVIEW_20260915.md`、官方批次和非 arXiv 来源记录用于定位已完成层；未出现具体失效信号时不第三遍重读旧论文/Books。
- 原 Meta GIM 05-17/05-18 冲突仍为具名资格保留项，不计确定新增候选、不作证据/Books/无遗漏依据；只有取得足以消解冲突的官方材料才定点重开。
- 初态本日本次目录工作树未列差额；仓库有大量既有及其他日期并发修改，全部保护，不 stage/commit/push。

## R2 — 先行独立入口核对（尚非整日验收）

实际打开 [arXiv availability](https://info.arxiv.org/help/availability.html)：页面说明新稿、replacement、withdrawal notice、cross-list 和 journal reference 都通过公告流程公开；周五/周六美东无常规公告，常规 Sunday 20:00 ET 对应次日北京时间 08:00。补充窗 05-17 BJT 对应 05-16 12:00～05-17 12:00 EDT，不能把旧报告的 05-18 BJT 公告批次搬进来。当前 2026 holidays 没有 May17 例外；仍待作者实际相关月列表/状态或有界恢复记录，不能由一般日程单独冒充所有异常事件已核。

同次打开官方 [Z.ai Research](https://www.zhipuai.cn/zh/research)，当前时间序目录给出 `2026/04/29 Scaling Pain` 与 `2026/05/20 ZCube` 相邻记录，其间无 05-17 项。该判断仅限实际目录覆盖。

[Anthropic Research](https://www.anthropic.com/research) 的本次 web 提取仅给十月前十条和 See more，不能证明五月覆盖。官方历史 availability commit/raw GitHub 与 arXiv 月表 web 请求 cache miss；另一次 curl 月表管道无正文命中，均不作为零命中证据。这些工具结果不否定作者随后恢复的有效原件。

当前 Source/PRE、候选证据、Books、DAY、保存完成态 FINAL 均待本次实际材料，不提前授予通过。

## R3 — 代表入口/排除校准与漏检风险

独立打开的 [Qwen 旧 Blog](https://qwenlm.github.io/blog/) 明示迁往 `qwen.ai`，静态目录仅列 2025；不能以旧目录无 2026 条目证明本窗无公开事件。已通知作者定点恢复新站或保留历史覆盖缺口。

[MiMo 官网](https://mimo.xiaomi.com/) 的 Paper 列表可实际读到 `2026-03-13 ARL-Tangram → 2026-06-29 MOPD`；但 Blog 卡片无日期且有 More，Paper 邻接不能扩大为所有 Blog 已覆盖。已通知作者单独处理 Blog 时间依据。

[MiniMax 英文 Research](https://www.minimax.io/blog) 当前可实际读到 `2026-03-18 M2.7 → 2026-05-26 sparse token forgetting → 2026-05-27 Agent Team`，该目录的有界邻接有效；[ERNIE Blog](https://ernie.baidu.com/blog/zh/) 最新实际条目是 `2026-05-09 ERNIE 5.1`，不是空响应，但仍只支持实际可见目录范围。

独立做四组日期/域名限定辅助检索（OpenAI/Anthropic；Google/DeepMind；Qwen；Hunyuan/Seed，`May 17, 2026` 或 `2026-05-17`）。搜索返回的社区讨论不扩张为研究候选/待关闭队列；辅助索引不证明各官网完整覆盖。

对检索出现的官方 [GPT5.5 Performance Degradation](https://status.openai.com/incidents/01KRP6FM6HSKWB3MS1EJTY6AT4) 信号，已打开并读完全部 Investigating、Monitoring、Resolved 三条更新。其内容仅有性能异常调查、应用 mitigation、恢复，没有根因、机制、可比评价或改变保证的事实；因此未达到研究合同 §3 的具体增量门槛。页面显示 May17 00:15 而本次 web 未带时区；这是贡献明确排除项，日期未核实不改变处置，不为它追查时区或建立新请求。该具名条目作为有运行反证信号排除样本，已向作者校准；不是通过标题/修复标签直接关闭。

## R4 — 恢复后 Source 子集与日期/准入校准

已逐一实际读取作者本日原件，而非沿用早期入口标签：

- `SUP_EXTRACT_0_20261019.json` 的全部五月原始字段上下文与 `SUP_fetch_20261019.py`：日期匹配扫描的是原始 HTTP 全文，并非被截断的正文。Anthropic 明确 `publishedOn` 为 05-14T17:06:12.172Z 与 05-22T17:00/18:00Z 邻接，未混用 created/updated 字段；本目录补窗覆盖接受。
- `SUP_ROUTE_0_20261019.json`：RSS 实际解析 `totalItems=1299`，保存 May10–22 的 title/link/pubDate；05-16 00:00 GMT Malta 与 05-18 10:00 GMT Dell 之间无条目，转为北京时间仍不落 May17。修复了初版 text 截断且正则不匹配 RSS 日期的问题，不再拿初版空匹配作依据。
- `SUP_FINALNAV_0_20261019.json`：混元从当前前端绑定的 `api.hunyuan.tencent.com/api/blog/publicList` 以 `pageNum=1,pageSize=50,renderType=0,accept-language=zh` 返回 `code=0,totalNum=11` 的全部 11 条，具体 04-30 与 05-21 两侧字段可复查；所列 publishedAt/displayPublishTime 均未出现本窗事件。作者已实际尝试动态浏览器但超时；有效 API 恢复解决了该入口，而不是把 timeout 计零。英文目录用于补查，不把版本/显示日期自动改名全球首次公开。
- `SUP_PUBLIC_0_20261019.json` 与第一页 `SUP_EXTRACT_2`/`SUP_WEB_C`：Seed publication API 实际 offset20/count20 是第二页，返回 Charon 起至更早的 20 条，第一页面尾 05-26、第二页首 05-16，覆盖 May17 夹段后停止，不把其余246条变队列。`SUP_DATA_2_20261019.json` 的 Blog API 为 article_type=2,page_token=0,count=20，实际可见15条、June19→Apr23 已跨本窗；has_more 不要求为不涉及本窗的更早段继续。
- `SUP_RECOVERY_2_20261019.json`：DeepSeek 官方 News 显示动态 04-24→09-10 与研究索引 02-25→06-24，可复查本窗两侧；首页“更多”不再是唯一证据。
- `SUP_SEARCH_B_20261019.json` 再现 Meta GIM 官方目录 05-17 与精确详情 05-18 的冲突，维持原具名保留，不新计确定候选。不会用 arXiv 后来提交覆盖已知更早可能正文，也不凭目录单字段强定 May17。

独立核查 Meta 搜索列表的另一个日期错配线索 TransText。官方[精确详情](https://ai.meta.com/research/publications/transtext-transparency-aware-image-to-video-typography-animation/)与[按computer-vision筛选的目录](https://ai.meta.com/results/?content_types%5B0%5D=publication&research_areas%5B0%5D=computer-vision)均标 April14，arXiv 身份为 `2603.17944`，其三月 v1 提交仅作身份线索，不充当公开日。已读完整题摘：其 Alpha-as-RGB/latent spatial concatenation 确有潜在机制增量，不能按“typography应用”直接排贡献；但官方正文 April14 已存在，足以排除本窗首次公开。未见具名重要修订或纠错信号，按窗外早稿线索关闭本日，不展开 Source/Books，也不制造另一项 May17 日期争议。作者独立恢复同样结果后共同校准一致。

以上是已完成的有限 Source/准入层；其余机构的实际历史段与补查结束条件仍待下一批，不提前通过 DAY。

## R5 — 全部到期入口处理与准入层闭合

已实际读回作者 `SUP_SOURCES_20261019.md` A1–A4 及其中对应原件，覆盖14个到期 ID。补读 `SUP_WEB_D/E/F/H` 的实际日期行与分页、`SUP_BOUNDED_1/2`、`SUP_FINALNAV_1`：DeepMind page1 30条已跨 05-28→05-06→04-25，MiniMax中/英/Agent三个入口均跨本窗，Kimi42仓库单页到底与K2.5无release仅证明对应切片，不拿created_at或repo列表代整个历史技术博客。

Source处理通过安全终态：8个来源结果为已检查，6个来源带精确保留；Google Research子入口、Qwen新站、Kimi历史技术博客、MiMo Blog、arXiv历史实际日公告/新命名标题补检的5处来源缺段，以及Meta GIM具名日期冲突，共6项保留须在报告中显式隔离。其中 Google/Meta/MiMo 各自已有有效片段并不失效。这里的“通过”是处理/隔离符合当前合同，不授受阻子入口完整Coverage，不证明这些来源实际没有发布。

arXiv没有具名拟入选论文被统一推迟或拒绝日期组合：补窗常规日程本就无公告，旧/现代月表及有限主题/官方status恢复失败；没有以Submitted或DataCite created构造本日候选，也没有因为单字段不足否决一个已有效的日期组合。分类宽列表未成为题摘/Source待关闭队列；不能把“十二类同受日程约束”表述成十二类实际标题均已浏览。

准入校准覆盖本轮全部拟入选（0），全部具名日期/修订/运行反证信号（GIM、TransText、GPT5.5 status 3项），以及按来源/主题分层的邻接样本（OpenAI Malta、Seed Charon、混元Hy-MT2、ZCube、MiMo两侧、MiniMax两侧）。邻接样本仅判窗外，没有冒称全体贡献排除；未对更早无关目录/附件作全文复读。没有发现共同错误理由需要扩池；前述 RSS截断、Qwen迁移、MiMo双目录、TransText日期错配问题均已在受影响范围修正。

确定新增候选0；新增必要Evidence0、Books决定/写入0，故新增PRE/实际POST无对象，不对旧64重新背书。旧64及31/33既有结果沿有效原层复用。不存在待协调的共享Books写位或普通Source/Books工作；作者下一步仅需融入六节、限定QA，再交DAY。未作整日验收，也未验保存完成态。

## R6 — 实际六部分 DAY（通过）

已读当前 README 完整差额、六节开头/结论/缺口/复核以及原连续 §4 边界，并读 SUP A1–A4。当前仍保存“进行中”，没有提前冒充保存完成态。六节一致表述原64＋新增0、必要Evidence0、Books新写0；六项外部保留均具身份/入口、所缺证据、采用禁止与精确重开位置。原小时窗三段结论和旧 §5/§6 Complete 已加历史范围，不能被解释为本次补充窗无缺口；没有其他可执行扫描、Source或Books对象。

本次 reader 实跑：

- `validate_research.py --report papers/2026/05/18/README.md`：1份V3通过；仅证明可判定一致性。
- 从真实本日 baseline 独立比较：64条原候选完整行在当前均且仅一次；当前候选仍64；原小时窗完全相同；补充窗为05-17。原 §4 从标题至 §5 前的连续块保持且仅一次（含标题约162931字符；独立比较排除标题后的正文162917字符），不是由散落片段或摘要替代。
- Markdown本地引用：README 78处、SUP_SOURCES 33处，全存在，无缺失目标；reader记录没有本地链接缺失。
- 本日 README与_sources 限定的working/cached两层 `git diff --check`：通过；只读检查cached，未stage/commit/push。

DAY通过，作者可更新本日状态、结论、§5及§6为完成态并保存，再交最小FINAL读回。此通过不授六个受阻来源完整Coverage/Evidence，不重验旧64研究，不新增Books变化；保存态FINAL尚未执行。

## R7 — 保存完成态最小 FINAL（通过）

已实际从磁盘读回 README 当前 header、§1、§5、§6 及 SUP A4–A6。检查时间为 `2026-10-19T11:11:00+08:00`，状态“完成”，当前独立复核者和“结论：通过”字段正确；历史作者/Complete段明确标为历史，不被当前补窗复用为证明。§1/§5/§6一致保留原64＋新增0、Evidence/Books新写0、普通研究/Books待办0及六项精确外部保留；SUP A5明确是先前进行态，A6记录真实保存态，不构成尚未研究的普通任务。

完成态再次实际运行V3及本日限定working/cached两层diff-check，均通过。没有新实质性差额，不第三遍研究来源/旧64/Books；R5/R6的有效语义和冻结/引用层直接复用。actual FINAL通过，本日处理达到当前合同的安全完成态；受阻子入口、GIM日期冲突仍不是正面Coverage/Evidence或无遗漏保证。共享Books新增0、无写位；reader仅写本文件，不stage/commit/push，不自行接下一日。交root接纳并释放本日reader ownership。
