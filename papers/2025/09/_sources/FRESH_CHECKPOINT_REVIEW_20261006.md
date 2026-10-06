# 2025-09-01 / 02 / 03 恢复点独立事实复核

执行日：2026-10-06。复核者：`/root/fresh_review`（非三份作者）。已重新读取 AGENTS、CODEX_RESEARCH_PROMPT、三个 canonical 研究合同/来源及 ROADMAP。此次只核 2025 新材料，不继承 2026 或旧日报 receipt；未改 Books、LEARNING_STATE、共享索引，也未 stage/commit/push。

**结论：三份恢复 checkpoint 的事实与未完成状态通过独立复核；三份 Daily 的 Report Gate 均未通过，研究仍未完成。** 必要公开时间/历史目录材料缺口真实，普通待办同时存在。按 root 协调暂停扩池保存停止点，不等于已穷尽所有可执行工作或已完成用户范围。

## 复核对象与实际范围

- [09-01 checkpoint](../01/_sources/RESUME_CHECKPOINT_20261006.md)、`admission-calibration.md`；实际解压 DataCite Sep1 registry 全页、267 身份解析与部分精确 DOI；核历史 official availability、原始错误状态、版本字段。
- [09-02 checkpoint](../02/_sources/RESUME_CHECKPOINT_20261006.md)、`source-screening.md`；实际解压 OpenAI RSS XML、解析全部 pubDate，读 Anthropic 174 目录记录、Google 46 请求/676 title；读八份 exact-v1 完整题摘与 00072v1/v2 原页增量。
- [09-03 checkpoint](../03/_sources/RESUME_CHECKPOINT_20261006.md)、`ADMISSION_AND_DATE_NOTES_20261006.md`；实际解压三页 DataCite、九项独立 DOI/完整 v1 题摘；AppCopilot §4.2.2 定点方法、两篇 OpenAI 原文、安全行为与计划状态；核内部链接和日窗边界。
- [首批独立准入记录](FRESH_ADMISSION_REVIEW_20261006.md) 保存具体校准判定和日期挑战。日期未核的机制线索不计为冻结候选，局部准入 PASS 不等于 Evidence 或 Books 完成。

机构目录事实核对是上述具体材料的复核，不声称所有未读目录/全部当前题摘已全量审阅。

## 1. 日期缺口与原字段

历史官方 availability exact commit `95c71658adbaa987dc2ba1105ef9c5201ecde4ce` 说明 final ID/DOI 在 announcement 自动处理过程分配、不能提前获得，并给出 EDT 14:00 cutoff/20:00 announcement schedule、2025-09-01 holiday 与延期说明。final DOI registry 已存在可作为身份已分配的可靠最迟界；registry created/registered 不是正文 first-public 字段。名义 schedule 不能在 metadata 上界跨截止时自动变成精确公开时刻。

| 恢复点 | 实际核实的日期/计数 | 尚不能推出的结论 |
| --- | --- | --- |
| 09-01，UTC `[Aug31 01Z, Sep1 01Z)` | registry raw 753，meta total753/totalPages1/page1；ID `2508.21073–2508.21825`，created Sep1 `01:18:19–01:37:42Z`，全在截止后；12 类匹配 JSON 267 unique identity | 名义 Aug31 Sunday20EDT=Sep1 00Z 不证明正文在01Z前公开；753不是本窗论文数，267不是候选/全量筛选。2509 month namespace 不可默认 UTC 月界。 |
| 09-02，UTC `[Sep1 01Z, Sep2 01Z)` | 正常名义槽 Sep1 Monday20EDT=Sep2 00Z；Sep1 holiday 原文只给 deferred mailing，实际批次尚未恢复 | 不得宣布本窗 arXiv actual announcement=0；不把 374 个 prefix00 恢复身份归到本日。 |
| 09-03，UTC `[Sep2 01Z, Sep3 01Z)` | registry 三页1000+1000+566=2566 unique/meta3pages；created Sep3 `03:22:09–04:23:42Z`。九项 v1 Submitted Sep2，个体 created/registered Sep3 `04:12–04:23Z`；九项逐一匹配身份和版本 | 唯一名义 Sep2 Tuesday20EDT=Sep3 00Z 不证明 first-public 在01Z前；2566全学科 registry 与133条submitted API discovery 不是日窗分母。九项日期继续 hold。 |

00031 的 `Updated v1=Sep3 00:00:46Z` 与 00105 的 `Updated v1=Oct1 01:13:26Z` 已读原始 DOI；09-03 的 02175 `Updated v1=Sep4 14:42:53Z` 晚于 Sep3 registration。这些是当前 metadata 原字段，不能只凭名称补成首次公开。arXiv catchup 的90天限制、日级 URL400、advanced form只支持公告年/月、OAI/部分政策域的 Tunnel403，都未被当作零命中。

恢复条件已精确到对应公告批次/个体正文公开、时区与截止前可核原始证据，或能解释原日期字段语义的官方说明；无需更高精度 submitted。只能定位某个 nominal slot 或与窗口相交的日期继续 hold。TopH/PACS/AppCopilot 的历史 README/committer/repo birth 是更早同族线索，不是 public-release 时刻，不能由它们直接归日。

## 2. 来源分页、正文与普通待办

- OpenAI raw RSS 解压后为 XML，1247 items、无 next link；1247 pubDate 均成功解析。09-02 窗内0，邻接 Aug28 10Z 和 Sep2 04Z helpful；后者及 Sep2 11Z Statsig 都落 09-03 窗。这里的0只限所取完整 RSS 的记录，没有用下载失败判0。
- Anthropic 174 research records 的时间范围 2021-12-01 至2026-10-01，Aug27/Sep5 近窗边界吻合，不扩大为所有 News/全站 coverage。
- Google 年目录日志46页 GET200，title JSON676；filter677差额未核，正文日期/语义仍待办。676不是本窗事件或候选数，机械下载结束不等于贡献处理结束。
- Meta/Hunyuan 成功品牌壳、Seed被忽略的page参数与最新18条/total242、MiniMax重复第一页、Z.ai当前旧段未恢复、MiMo无日期Blog等，都保留准确停止点。普通浏览器、同源API、近窗原文、轻量仓库与精确版本处理没有被改称“已完成”或“外部全部穷尽”。
- root 新保存的 `browser-directory-checks/{meta,hunyuan}-offline-render.json` 已实际读取：verified HTTPS 200下载280268/6893 bytes，offline Chromium body空、links0、scripts77/7。只支持离线加载所得结果，不证明 live assets 执行或历史目录无数据。default Chromium CA trust 修改被自动审查拒绝而未执行的环境动作由 root 记录；本复核未据此宣布浏览器覆盖完成或另行绕过代理/TLS。

## 3. 准入与排除校准未被升级为完成

09-01 七条机制线索/三代表排除、09-02 八 exact-v1 小批、09-03 TopH/DCPO/PACS/AppCopilot 四项已按具体原文增量校准。AppCopilot 的 bbox外nearest-widget correction + framehash失败校正后回原点分支纠正了原泛组合排除；不承诺意图正确、fallback安全或普遍终止。BrainReplay 的小模型负面边界允许定点核，不以模型规模/负面结果退出主线。

00072 的 exact-v1 原题为 **Beyond Memorization**，纵向合成QA无cutoff衰减不等于 current v4 **Test of Time** 的同源问题改写受控证据。原 v1 只说 newer version withdrawn；v2 原页实际 withdrawn/noPDF/no-license，history Oct6 2025 14:10:14 UTC，未给原因，后续v3/v4恢复。修后作者没有把整个 family 或 v1 自身说成撤回，没有采用当前主张支持 v1；后续正面采用前仍需处理真实撤回/纠错信号。

两项 09-03 OpenAI 排除独立抽检通过，条件是保留原文实际状态：helpful 的 sensitive routing 是 soon、parental controls next month；deliberative alignment已有，原文也确实说最近已引入 real-time router、已rolledout break reminders。这些既有事实不能说成全文无实际保护行为；原文未提供其本窗新事件日期或新增检测/受控评价，不能用未来计划证明保护已生效。Statsig 为收购/任命与实验平台整合目标，没有足以改变本项目 AI 机制选择的增量。

其余09-03五条潜在线索的准入、正文审阅和全来源覆盖未在本次校准中冒充通过。无候选评分、无已完成Evidence清单、无Books决定/写入，无三日报README。到期Weekly及余下日期未因此完成。

## 4. 文件与状态检查

本次实际解析顶层 JSON：09-01 227、09-02 13、09-03 22，全无解析错误；解压gzip分别106、98、41，均无解压错误。09-01有10个、09-03有4个失败请求空body；这是真实失败原始记录，不是有效正文，未将“gzip可解”写成“全部正文非空可读”。09-02保存gzip无空body。

三份 checkpoint 与 canonical screening/admission 内部 Markdown 链接在复核时均存在，三日正式 README 均不存在。本复核两个新增 MD 已检查空白/diff 范围。机器格式/JSON/gzip检查只辅助恢复材料可信，不替代研究语义。

**最终受阻验收记录：checkpoint facts PASS；Daily/Weekly completion NOT PASSED。** 外部日期与必要历史枚举尚未闭合，普通待办如实保留；没有错误完成 Gate、零候选日报、伪造分母或 Books 完成。恢复后只重开相关批次/材料，并复用未变化的有效证据。
