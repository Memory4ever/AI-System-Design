# 2026-04-27 Daily V3 重开 checkpoint

作者 apr01；固定窗口 `[2026-04-26T09:00:00+08:00, 2026-04-27T09:00:00+08:00)`。已重新实际阅读 `AGENTS.md`、`CODEX_RESEARCH_PROMPT.md`、三份当前合同、`ROADMAP.md` 与月度 V3 checkpoint。只负责本日报及本日 `_sources`；历史 Daily 独立于 Weekly，14 个到期每日来源逐一有界核查。共享 Books 修改须另行协调写锁，完成前由非作者独立复核。

## 当前最窄恢复点

旧正式 README 是 V2.1 档案，不可继承其 `Complete`、48 分母、339=全当窗或 Books 已完成。旧 `screening-ledger-final.json` 也不可当 V3 分母：其中 2604.23488/23505 在相邻 04/28 owner receipt 的 DataCite 初建为 04/28，2607.05397 的 4 月提交不能改变其后来公告 ID 归属。旧 20 候选既跨日期又存在泛化准入理由。本次需以官方公告/相邻批次/精确 v1 组合重建当窗事件；DataCite created、submitted、OAI datestamp 各自只能按原字段做佐证，不独立冒充 first-public。

可复用的原始线索：`arxiv-owner-replay-20260903/20260427/arxiv-owner-receipt.json` 有 339 个以 DataCite 初建日为入口的 arXiv identity，ID 范围至少 2604.21932～22753；同目录 04/28 receipt 可用于相邻批次去重。这些只是原始身份，不是 339 篇候选或必须全文审读的配额。范围清楚的题名先关闭；含糊及主线相关者读完整题摘并以具体长期贡献筛选；撤回/重要纠错先看当前官方标记。独立复核前不冻结候选数。

当前可执行工作：核 14 Daily 官方入口真实窗口停点；核 arXiv Sunday 20:00 ET→北京时间 Monday 08:00 批次及例外；按题摘重审真正当窗主线线索，必要精确版本证据与 Books owner 对照。普通未读不得称外部受阻，不沿旧 V2.1 的来源和 Books 断言。

## 2026-09-28 最新有界续跑位置

正式 V3 仍为**进行中**：408 个去重原始身份线索不是候选分母；38 项重新筛出的工作家族经非作者校准具名关闭 `22436/22050/22708`、随后从旧泛化关闭恢复 `22438/22550/22291/22662/22504`，暂为 40 项，尚未冻结。29 项 Books 真正文已由非作者写后 PASS（先前 26 项及 BERAG/UAE 的 Ch76、Abstract-CoT 的 Ch33 三处新增）；7 项拟 Existing 待整日终核，2 项仅报告，`22136` 中心定理和 `22152` exact-v1 版本材料具名隔离。普通 Books 待办 0；来源和否定侧整日 Gate 尚未通过，不能以单篇写后替代。

正反准入复查新增三个具名前分母关闭：`22446` OneManCompany 的动态任务/失败/暂停并未证明无死锁，与 Ch81 状态/effect owner 无新合同；`22577` QuantClaw 的任务类型→离线量化配置在固定 INT4 质量/成本/耗时反向下未超 Ch49 已有三轴联验；`22597` math judge 的独立题解/多 judge/格式抽取是 Ch66 现有 reference/semantic/format 分权的数学域受限实例。`22520` RouteLMT exact-v1 的大/小模型边际 gain 与 guard tail-risk 对照核 Ch56 后维持 5 分标准 Existing，不新增 Books；这些判断保留具体原文/章节理由于筛选与证据记录，不按题名/小模型硬拒。

14 源补查发现两组**真实当窗但贡献前关闭**的官方 GitHub release：QwenLM/qwen-code `v0.15.3` 04/26T06:49:56Z 与 04/27 nightly 00:25:13Z，已用单项分页 p335–339 找到相邻停止边界并定点核 rewind/flush/hot-path/preconnect PR；MiniMax-AI/cli `v1.0.12` 04/26T01:40:29Z，已核 image HTTPS/base64 PR。两者发布家族不改变顶部当前 40 项 arXiv/OpenAI 工作集合；其它仓库不能因新仓库零命中或一仓库 release 阴性而说组织级零更新。来源具体入口、限制和重开条件见 `V3_SOURCE_DISCOVERY.md`，正式 §2 已同步。`python3 scripts/validate_research.py --report papers/2026/04/27/README.md` 与本轮 scoped `git diff --check` 均通过，二者不等于语义或整日 Gate。

本日原八项普通 Books 中的 `22127`、`22509` 已由 apr20_resume [有限独立 source→实际 owner 审阅](V3_APR20_TWO_22127_22509_INDEPENDENT.md)通过，随后 root 实写 Ch30/Ch63，待另一人实际写后复核，不提前计 I。旧实写 `22228` 由 apr02 [定点核](V3_APR02_22228_WRITE_AFTER.md)确认正文机制与 exact-v1 一致，却发现 Ch36 的 source-family end marker 越界包入后续 NIMBLE；root 已将 end 移至本篇两段后，待修后独立确认。其它普通项状态以顶部当前清单为准，不沿本段早期“原八项”阶段计数。

旧实写 `22312` 的 [apr02 定点核](V3_APR02_22312_WRITE_AFTER.md)已确认 Ch49 主机制、成本、邻接和 SF marker，但原句把 official v1 正常 `K≤f(T)≤C` 后候选多于 K 时的精确 refine 误说成验证失败；root 已窄修，仍待修后独立确认，不提前计写后 PASS。`SRC-ZAI`、`SRC-BYTEDANCE-SEED`、`SRC-XIAOMI-MIMO` 的具名仓库 release 历史层已补入来源/正式 §2；仍缺组织其它仓库/无 tag 提交的可回溯总目录，精确隔离而非普通未查或组织零更新。

旧实写 `22753` 的 [apr20 独立核](V3_APR20_22753_WRITE_AFTER_INDEPENDENT.md)与 [apr02 复核](V3_APR02_22753_WRITE_AFTER.md)确认 Ch28 主链和来源标记，但原句漏 official exact-v1 §4.2/Alg.1 的可负担候选与 `(ΔV_intra+ΔV_inter)/c(x)^α` 成本惩罚。root 已补入成本惩罚，仍须按实际修后正文独立确认，不能继承旧 Integrate；apr02 原先的 PASS 已据此降为“主链通过、句子待修”。它仍占顶部普通六项中的一项。

否定侧新增单项 [`2604.22438v1` SSG](V3_SCREENING_NOTES.md) 的旧 receipt 泛化关闭理由不成立；[apr20 的有限非作者复核](V3_APR20_SSG_INDEPENDENT.md)确认低熵水印 keyed 分组的 source→Ch72 窄 gap，且给出全词表理论不能直接外推 top-k 实现的反例。作者随后核官方 ID 公告规则、Sunday 20 ET、原始本批 `22436/22438/22439/22442` 连续 ID 的 v1 Updated/OAI/DOI 原字段及下一批 `22754` 边界，按本日既有组合口径有界推断该家族在 04/27 08～09 北京时间公告；不把单一字段叫首发或逐篇日志。故暂恢复为第 36 个 2+2+2=6 标准候选，尚未冻结；新增第 9 项普通 Books 待 root 写前采用、共享 Ch72 实写和另一人的写后核，不能把 source→owner PASS 当实际整合或日 Gate。其余原 8 项普通与两项来源隔离仍按上方状态；当前 36/9 尚未冻结，不能用于最终完成结论。

同类理由有界反查的 [`2604.22550v1` ArmSSL](V3_SCREENING_NOTES.md#同类泛化排除理由的第二个具名漏收260422550-armssl) 也经[apr20 非作者必要审阅](V3_APR20_ARMSSL_INDEPENDENT.md)恢复：encoder 经下游分类头后的黑盒 confidence 归属接口及水印 OOD 密簇可被定位/移除，是 Ch72 现文尚无的窄安全边界；主表 frozen encoder、64 个负例零误报和自适应攻击成功反证必须保留。官方 Sunday 公告/ID 赋号规则、`22549/22550/22551` 同批 v1 Updated 00:40Z/DOI created 01:40Z、OAI 04/27 及 04/28 `22754` 边界仅支持本日 08～09 北京时间有据推断，不能单证改称首发。**此处当时阶段值**为 37=17 实写通过+8 Existing 拟处置+2 隔离+10 普通；后续八项 Existing 独立审计已将 `22167` 降回普通待办，**当前值以本节首段 17+7+2+11 为准**。新增 ArmSSL 只具名准入/标准必要审阅，Books 仍需 root 独立深入采用与共享章写后，不能以两次发现称全部 408 关闭项无漏。

最新来源/否定侧独立审计见 [V3_SOURCE_NEGATIVE_INDEPENDENT_AUDIT.md](V3_SOURCE_NEGATIVE_INDEPENDENT_AUDIT.md)：日期是有据公告批次推断而非逐篇首发日志；14 源和共享泛化排除理由的整日 Gate 仍待重核。此后正式 §2 已将 Qwen 动态/静态研究入口闭合，Moonshot、Tencent-Hunyuan、ZAI、MiMo 的当前公开组织/仓库层做有界停点，旧 Tencent 六仓 GitHub 限流已在额度恢复后重取有效空数组。Seed/MiniMax 也已恢复限流、逐个核当前窗前建且后续活跃的 12/7 仓 Releases/Tags，MiniMax CLI 本窗发布阳性已贡献前关闭；两家 GitHub Search Commits 精确窗均 `0,incomplete_results=false`。Google Publications、两家已删/改写旧 tag/非默认分支与无日期博客等历史子入口均具名终态隔离为 `受阻`，不称组织零更新或全网零遗漏；Seed/MiniMax 旧页面失败已有效重试或确认窗后新建。当前普通 Books 待办为 0，唯一正式 `未完成` 来源行是 arXiv 的分层否定侧/整日独立准入 Gate；这并不代替 root 的完整日级语义复核。

**下一最窄日 Gate 差额（2026-09-28）：**作者侧 14 个到期来源的可执行目录/版本重试均已到有界停点：4 行 `已检查`、9 行具名 `受阻` 终态隔离、1 行 arXiv `未完成` 仅因排除侧/日级独立语义 Gate。九处隔离各在正式 §2/来源记录给出实际入口、为何现有证据不能说零命中和定点重开材料，不再当普通“待扫全组织”。旧泛化前闭 `2604.22615v1` GazeVLA 经 root 独立准入、作者 Ch26 实写及 root 非作者按实际正文/相邻/exact-v1 写后 PASS。同一旧关闭理由的[158 身份子集有界反查](V3_GENERIC_LOCAL_METHOD_SUBSET_AUDIT.md)已补齐 158/158 完整库存题摘，定点恢复 `2604.22236v1/22442v1` 为 5 分标准、仅报告候选，`2604.22169v1` 为 6 分受限训练机制候选并获 Ch33 实际写后 PASS；`22464` 由 root 写前裁决并实写 Ch30，apr01 按 exact-v1 与正文、邻接做[非书稿作者写后 PASS](V3_APR01_22464_CH30_WRITE_AFTER.md)，计入。当前暂为 45 工作候选、32 Integrate/7 Existing/4 ReportOnly/2 Disputed，普通 Books 待办 0，仍非冻结分母。抽查起点 158 中已选 12、旧前闭 146；本轮不是 158 篇全文，而是按共享错误理由补全题摘、再对具名高信号读必要 Method/owner。下一步 root 对来源终态、公告组合/例外、拟入选与共享理由负侧样本做最终独立日 Gate；若定点发现系统性漏收，仅扩相同受影响理由。机器校验只证明结构。

**本轮定点更新（覆盖上一段阶段计数，不改其历史记录）：** root 在 158 题摘否定侧独立抽样指出 `2604.22171v1` MCI 旧泛化关闭错误。作者实际核[exact-v1 §3–5/Appendix A 与 Ch76](V3_APR01_22171_MCI_REVERSE_ADMISSION.md)，root 另核 §2–3/现章并认可窄 source→owner 采用。root 已窄写 Ch76，apr01 作为非书稿作者[实际正文、相邻与证据写后 PASS](V3_APR01_22171_CH76_WRITE_AFTER.md)。当前 **46 工作候选=33 实际 Integrate/7 Existing/4 ReportOnly/2 Disputed**，尚未冻结；158 同理由组改为 **141 题摘级前闭+17 已选/恢复**，不把 158 全部说成 Method 全文审阅。普通可执行 Books 待办 0；来源可执行重试仍为 0，14 源的 4 已检查/9 精确隔离/1 arXiv `未完成` 仅待作者外分层否定侧与日级语义 Gate。不能由单篇恢复或机器校验预称 Complete。
