# Daily Research — 2025-09-06

**规范：** V3
**窗口：** 2025-09-05T09:00:00+08:00 ～ 2025-09-06T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T13:03:13+08:00

## 1. 结论

2个确认发布家族、2个深入审阅完成，均获实际Books整合。root已在Ch8“能力不等于知道自己知道”新增条件IIV边界及评分激励交接两段，在Ch66“选一个分数”与“Evaluation Identity”分别落实回答/拒答期望式和Git对象/测试可见性。非写入者Mendel实际POST通过，root最终DAY通过。OpenAI官方RSS09/05 18:00发布幻觉研究，不采用“所有AI必然幻觉”；Kimi官方管理员发布帖09/05 11:30及冻结README支持具体环境控制，不授全泄漏消除。arXiv提交线索不等于本窗公开，不作零发布结论。

14每日来源已处理至真实有限停止或明确外部保留，普通待办0；动态历史目录及日期缺口不支持“无遗漏”或正面Coverage/Evidence保证。作者未改Books、共享索引或LEARNING_STATE；完成只授本日，不推及其他日期。

## 2. 来源覆盖

查询参数、原记录与停止点见[作者交接](../_sources/daily-20250906/HANDOFF.md)。所有搜索仅发现，结果集合读完后停止，不授全网召回。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research当前首页；Sep5限定查询；官方news/rss.xml与幻觉事件页题名/链接核对；v1题摘 | 已检查 | RSS为官方发布事件，不把提交或稿件日期改写为公开；不授全网无遗漏 |
| SRC-ANTHROPIC | 本次原HTML的Next.js JSON解析出171 publication；按原publishedOn筛本窗；最近biorisk为2025-09-05T00:00:00.000Z，前于窗起 | 已检查 | 只授当前官方研究目录的有限窗口检查，不授全网无遗漏 |
| SRC-GOOGLE-AI | DeepMind/Research入口及窗口查询；月份第1页12条09/30→09/11；实际GET /blog/2025/09/?page=2 成功200，末页1条09/09；原HTML已保存 | 已检查 | 该官方Blog月份有限列表已跨窗，无本窗条目；不授全部论文或全网覆盖 |
| SRC-META-AI | Research当前入口、Sep5原域查询及September2025模型补检 | 受阻 | 有限索引/入口无法授日级无遗漏 |
| SRC-QWEN | 官方旧Blog/精选及本日查询；本日本地GET qwen.ai/api/page_config?code=research.research-list成功，60条配置按原date筛本窗0；最近09/08 ASR与08/18 Image Edit在窗外；QWEN_CONFIG.json及请求原记录已存 | 已检查 | 仅授实际配置列表的窗口检查，不授全论文历史覆盖；不将60条变全文队列 |
| SRC-DEEPSEEK | 官网/09/05查询；本日实际GET官方API Docs /updates/，200；Date 09/29→09/22→08/21跨窗 | 已检查 | 仅现存官方更新页有限检查，不授所有研究无遗漏 |
| SRC-MOONSHOT | Platform Blog/研究目录；官方管理员发布帖JSON原时刻；HF commits冻结0905 README、必要旧版差额 | 已检查 | 使用官方发布事件，不把09/03仓库创建或commit直接当first-public；in-house harness未公开 |
| SRC-TENCENT-HUNYUAN | 首查Research为空；浏览器失败；官方JS→publicList第一页9/9，窗口查询 | 受阻 | 现存目录均2026，不能证明2025旧记录齐备 |
| SRC-ZAI | 首查Research15条；本日实际GET /zh/research?page=2，200，Next JSON累计18/nextPage3/hasMore=false，最旧2025/12/07；release notes09/30→08/11及查询 | 受阻 | 当前Research已至末页但未覆盖2025年9月历史层；不是未执行More或0研究 |
| SRC-BYTEDANCE-SEED | 官方type2 API 2025/token0/count20：15条、total49；置顶逐日期核，非置顶序列已越窗至07/15停止；type1实际token0/20/40/60/80到has_more=false | 受阻 | Blog有限窗已检查；papers标total94但只返回token20的1条06/12 SwiftSpec，其余缺sub_article_list，不能授94项覆盖或0条 |
| SRC-BAIDU-ERNIE | 官方Blog2/2末页09/12→08/14夹窗；09/05查询 | 已检查 | 只授这个Blog有限列表，不推论所有论文无发布 |
| SRC-XIAOMI-MIMO | 官方8项Paper目录09/19→06/04夹窗；窗口原域查询 | 已检查 | Blog More历史部分未恢复；不授全发布覆盖 |
| SRC-MINIMAX | 英/中文Blog及09/05查询；本日Agent Tech Blog与llms.txt实际200，仅2026-05-13一篇至当前目录末尾 | 受阻 | 注册入口已执行；只授当前有限目录，2025历史完整性未证 |
| SRC-ARXIV | 原公告政策；本窗模型/多模态/系统/RAG/Agent主题查询；宽CL月列表仅查漏下载 | 已检查 | 本窗无常规公告时点不证明异常/作者提前公开不存在；提交线索需日期核验 |

按需来源未触发；不检查Weekly分组。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Why Language Models Hallucinate](https://arxiv.org/html/2509.04664v1) | 2025-09-05T18:00:00+08:00 | 分布拟合的条件性IIV错误下界与零分弃答评分的猜测激励需分开治理；2 + 2 + 3 = 7 | 深入完成 | 整合：`WORLDVIEW-LLM-INTELLIGENCE` [Ch8能力边界](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md#能力不等于知道自己知道)两段；`PLATFORM-EVALUATION-SYSTEM` [Ch66评分](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#为什么选一个分数不是评估系统)期望式与拒答边界；实际POST/DAY通过 |
| [Kimi-K2-Instruct-0905 发布card](https://huggingface.co/moonshotai/Kimi-K2-Instruct-0905/blob/7152993552508c9f22042b3bb93b5e6acd06ce73/README.md) | 2025-09-05T11:30:13.003+08:00 | 冻结代码Agent可读Git对象/目标测试，而非只冻结checkout；外引榜单分开比较；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66环境身份](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#evaluation-identity-必须包含-harness-与-environment)具体Git/test单元；实际POST/DAY通过 |

未确认落窗的arXiv线索与负侧不提前计候选。

## 4. 证据与知识整合

### [Why Language Models Hallucinate](https://arxiv.org/html/2509.04664v1)

OpenAI官方RSS原记录见[完整RSS](../_sources/daily-20250906/OPENAI_RSS.xml)与[提取事件](../_sources/daily-20250906/OPENAI_RSS_EVENT.xml)：题名及link/guid与事件页一致，pubDate为09/05 10:00GMT。Blog日历、PDF稿件日期、arXiv提交及后续公告是不同事件字段，不否定官方提前发布；不声称证明全网绝无更早稿。

[精确证据与Books提案](../_sources/daily-20250906/EVIDENCE_HALLUCINATION.md)保留实际阅读、定理证明、反侧与owner正文位置。Theorem1只在有限回答集合、同提示分布、无噪声p和指定IIV构造下，给出含集合比例及阈值质量偏差delta的下界；delta不是truth-confidence ECE。§4.1证明binary评分下弃答0分严格不如某个正成功概率回答，不证明模型实际最优化或所有幻觉的单因果。§4.2公式独立核对给出q>t才回答；官方PDF与HTML中的t=.75惩罚2、IDK概率方向两句不一致不采用。无复现或生产保证。

root实际在Ch8“能力不等于知道自己知道”原mode解释之后新增两段：有限IIV条件及非平凡下界限制、能力辨别与评分激励分开并交接Ch66。Ch66“选一个分数”原条件测量之后新增scorer期望式`(q-t)/(1-t)`，明确t=.75罚3、q=.6期望-.6与覆盖/错误代价边界。两个机制分别有唯一owner；非写入者Mendel顺读实际正文与完整前后邻接，对照v1§3.2/A/4.1/4.2/E后POST通过，root必要原文独核及最终DAY通过。

### [Kimi-K2-Instruct-0905 发布card](https://huggingface.co/moonshotai/Kimi-K2-Instruct-0905/blob/7152993552508c9f22042b3bb93b5e6acd06ce73/README.md)

[证据与owner差额](../_sources/daily-20250906/EVIDENCE_KIMI.md)保留官方管理员首帖身份、03:30:13.003Z发布事件、03:07:24Z精确README与前日差额。card§3披露逐run剪除目标commit不可达Git对象及SWE-Dev目标测试删除；5-run mean±std不是置信区间。外引基线与in-house重测不合并排名。未公开prune/harness实现，无防泄漏因果消融，不采用全部历史泄漏消除、质量归因或API吞吐/100%语义正确性宣传。root实际在Ch66“Evaluation Identity 必须包含 Harness 与 Environment”原身份解释后新增可读Git对象、refs、测试与工具权限单元，并保留成本、稳定专用沙箱和无完备保证；Mendel对照715299§3顺读完整邻接POST通过，root证据与DAY独核通过。

## 5. 缺口与下一步

普通待办0；root实际Ch8/Ch66窄增量已获Mendel非写入者POST与root最终DAY通过，裁决和完整邻接阅读位置见[交接顶部](../_sources/daily-20250906/HANDOFF.md)及[独立DAY记录](../_sources/daily-20250906/INDEPENDENT_DAY_REVIEW.md)。Anthropic、Seed Blog、Google月份分页、DeepSeek更新页、ZAI第二页、MiniMax Agent有限目录与Qwen配置API均已本日实际执行。

外部终态保留项：以下未恢复材料不用于正面证据、Books或无遗漏断言；定点重开条件分别见各项及来源行，不阻塞已限定结论。

- 两正式家族日期/version hold已解除并经root核连接，不列外部日期缺口。Kimi in-house实现仍未公开，采用范围已收窄；只有需授清理完备或性能因果时才定点请求prune/harness实现、可读状态与受控消融，目前不授这些保证。
- 历史研究目录：Anthropic、Seed Blog、Google09月份2/2页及DeepSeek正确更新页已窄恢复。Seed papers：US/CN token0均无列表，header CN与count100同样无列表；实际token20仅1条、40/60无列表、80无列表且has_more=false。需要恢复该2025列表的可见条目/原快照；不把metadata total94当已筛数量。Meta、Hunyuan、MiniMax及ZAI/MiMo历史部分见交接。ZAI本次已到hasMore=false，MiniMax Agent当前目录已到末尾，不再列未执行More或注册入口。缺口不支持零事件/无遗漏；有目标旧目录或具名本窗原材料才窄重开。

窗外/未归属线索：`2509.04716/04827/04876/04996/05258/05263/05276`题摘展示的是Sep5提交，可能对应下一常规公告批；09/08只可定点核原公开事件，不能把本日发现或提交日期作为归属证据。本日不展开窗外正文审阅；负侧position `2509.04731` 的具体关闭理由见交接。

## 6. 复核

复核者：root（非报告作者，首批准入、必要证据与最终日级复核）；Mendel（非Books写入者，实际POST）。

结论：通过

root于2026-10-06T13:00:29+08:00实际核最终六部分、查询与14源有限停止、RSS及forum admin时间/冻结715299与D30差额、全部两正式候选必要原文、7项潜力与1项position负侧题摘及日期隔离；详见[独立DAY记录](../_sources/daily-20250906/INDEPENDENT_DAY_REVIEW.md)。IIV条件/概率质量偏差、scorer公式与原文冲突、Git控制权限边界均保留；OSC/KERAG/FLOWER不按组合或局部实验机械关闭。实际Ch8与Ch66正文及完整邻接由Mendel非写入者POST通过，root同步源注。未核未公开harness、运行artifact或复现实验；有限source停止不授全网无遗漏。作者据独立裁决同步完成，不自授验收。

机器检查：本日 V3 格式/一致性校验通过；限定范围 `git diff --check` 通过。两者不验证历史来源真实性或语义完成。
