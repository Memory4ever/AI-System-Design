# 2026-03-10补充来源覆盖：03-09完整自然日

执行：2026-10-09 BJT。原窗口与旧结果冻结；本轮只审增量，不继承他日池。Daily14行如下，前13家除Seed locale定点校正外复用本日可核未变的有限切片/core（原值见baseline与V3原件）；此前标签不是全源coverage。所有有限目录已覆盖目标邻接，未把宽列表变逐项队列。

| 来源 | 实际范围/停点 | 结果 | 限制 |
| --- | --- | --- | --- |
| SRC-OPENAI | 复用本日官方RSS1240项的3/8–3/11七条切片及Promptfoo原core；覆盖03-09完整日，不以09:00筛新材料 | 已检查 | Promptfoo仅收购/计划，贡献EX；精选/RSS不证明全部历史 |
| SRC-ANTHROPIC | 复用本日Research10项/See more同页、Alignment March五项；AuditBench/Abstractive旧事件定点身份 | 受阻 | 主Research历史分页未恢复；March可见切片不等机构全历史 |
| SRC-GOOGLE-AI | 复用本日DeepMind真实page3 24卡/Google March archive12卡3/11→3/6、下一页更早；Pubs仅year | 受阻 | 官方论文日级切片缺口保留；回顾EX，非全研究无命中 |
| SRC-META-AI | 复用本日Blog page1十卡/page2十二卡；Research/publication入口400 timeout | 受阻 | 需要03-09模型/训练/推理原始历史论文清单；Blog不是全FAIR |
| SRC-QWEN | 复用本日新public API40项标题/date/path，2/16→3/19跨窗；旧页停2025 | 已检查 | 可见40项无03-09条目；无total，不证完整机构历史 |
| SRC-DEEPSEEK | 复用本日官方/en/news Research10/News5元数据，2/25→6/24及12/1→4/24 | 已检查 | 可见切片无03-09；不外推View all/删除历史 |
| SRC-MOONSHOT | 复用本日现官方Kimi Blog19条，2/9→4/20跨窗 | 已检查 | 19可见范围无03-09；不扩repo/release队列 |
| SRC-TENCENT-HUNYUAN | 复用本日本publicList page1/pageSize20/renderType0，11/11 current total；2/13→4/23 | 已检查 | 当前可见无03-09；入口恢复有效，不证删除历史 |
| SRC-ZAI | 复用本日官方Research15可见卡，2/21→3/15邻接；停View more | 已检查 | 本页无03-09；不把可见15卡称全部历史 |
| SRC-BYTEDANCE-SEED | 同页API article_type1/year2026/token20/count100/order_descfalse；US18项与默认14项实际比较，next40/moretrue/total82；Feb25/27→Mar2→Mar12，已过目标未来段即停 | 已检查 | 无03-09目录项；US四额外身份1992/1644/1664/1661不遗漏，显示date≠paper first-public；不遍历剩全年 |
| SRC-BAIDU-ERNIE | 复用本日Blog/zh page1十项；2/6→4/15跨窗，下一页更早 | 已检查 | 可见无03-09；不证其他历史/修订 |
| SRC-XIAOMI-MIMO | 复用本日首页Paper八项2/3→3/13；Blog15标题无日期，/blog为旧单篇 | 受阻 | Paper无03-09；请求带原始日的03-09 Blog切片，不以无日期标题作零 |
| SRC-MINIMAX | 复用本日英文Blog12卡2/14→3/18；中文redirect shell/Agent Tech heading与llms48行恢复链接不可读 | 受阻 | 英文可见无03-09；Agent历史正文/日期缺口不因llms目录消失 |
| SRC-ARXIV | 本轮四主题submitted缓冲UTC03-05 19:00→03-06 19:00；start0/max200/ascending各87/87、63/63、17/17、83/83页内取完；72完整题摘冻结，宽标题仅发现。48日级区间归属/10 EX/10边界日期/4早稿身份；当前72官方header已轻核 | 已检查 | 约定主题已查；10+4必要日期保留，不授全分类召回；官方03-09列表cache miss不是日级零 |

四query原式/分页参数：[supplement-fetch](supplement-fetch-20261009.py)，原值与筛选72见同日supplement标题/abstracts文件；各total均小于max200，未留下同query可执行分页。72→48并无数量/保留率配额。arxiv Submitted只是发现缓冲；官方availability no-advance finalID/DOI和Thu14–Fri14最早Sun20公告规则给03-09 BJT下界，findable/registered给03-09日内可发现上界，二者夹证该日而非registered=first-public。10越界日期与4更早稿信号不能借此通过；见[必要日期恢复](supplement-date-recovery-20261009.md)。

Seed原始当前projection：[US18](supplement-seed-us-projection-20261009.json)、[默认14](supplement-seed-default-projection-20261009.json)。US额外veScaleFSDP/ModalityGap/ResidualScaling/FlexTrain为Feb25/Mar2/Mar2/Mar20目录身份；后两日期/论文链接不一致不授首公开，均非本轮03-09新增。不继续page40未来段或全年扫描。

当前事件轻核：[72官方header/comments/history](supplement-current-events-20261009.json)，实际全部成功。没有当前撤回/方法伦理或安全纠错标记；PolyBlocks仅补漏Acknowledgments，Omni后窗v2称优化checkpoint。版本与camera-ready标签不等重要修订，本轮不比较全部版史/未来正文，不将最新条件混入v1。中心争议仍由本轮必要原证保留。

实际触发的按需/补检仅4先稿OpenReview身份、GraphRAG出版方、ATLAS Microsoft原页和Real-3DQA作者原页/项目日期，见date-recovery；没有Weekly源扫描、会议全站、repo/release队列或他日重跑。旧Meta/Anthropic/Google/MiMo/MiniMax历史来源缺口按03-09本轮日级请求保留，不拿搜索无结果授全源零命中。
