# Daily Research — 2026-01-05

**规范：** V3
**窗口：** 2026-01-04T09:00:00+08:00 ～ 2026-01-05T09:00:00+08:00
**窗口说明：** 用户授权对已有 Daily 补充遗漏，保留原窗口、候选日期、评分及有效审阅，不搬移旧材料。
**补充窗口：** 2026-01-04 ～ 2026-01-04
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-07T13:34:10+08:00

## 1. 结论

原窗口14个每日来源已作有限检查。确认窗内KimiCLI两个release事件、同一材料家族，完整核心说明初筛经独立校准贡献前关闭；0正式候选、0候选证据审阅完成、0 Books整合/已有覆盖，No Change。目录、日期字段和变更说明初筛不计候选证据审阅。原root非作者日级验收通过，不替代本轮增量复核。

2026-10-07 增量补查已实际处理14个Daily有限入口，补充窗口没有确认新增候选：新增候选0、新增候选证据审阅0、新增Books改动0。原KimiCLI0.71/0.72有效结果复用不重算；相邻0.70的官方公开日期为Dec31，未在旧09:00起点之前新增Jan04事件。Qwen/Hunyuan、智谱、MiniMax中文及Agent、MiMo Blog本轮已恢复有限目录，不把历史隐藏/删除/所有镜像不能穷尽另造缺口。Google Research日级日期目录及Meta可读目录仍隔离。本轮root非作者独立复核通过，原验收仍只适用于原工作；完成不声称两项外部来源无缺口。

arXiv元旦延迟批次的官方计划公告时刻恰好在本窗不含的右端点，不按Submitted日期吸收下一批。机构历史及公开revision/mirror限制已单列；以上0候选不代表互联网无相关论文，也不表示Coverage/Evidence没有缺口。

## 2. 来源覆盖

仅Daily组，不扫描Weekly源；原有效候选/评分/审阅保留，跨日只核材料家族去重。以下为本轮补充窗口的实际有限入口与停点；[本轮完整补查记录](../_sources/daily-20260105/supplement-20261007.md)保留查询参数、动态目录恢复、贡献关闭及原始响应链接。[原查询与停止](../_sources/daily-20260105/queries-and-screening.md)、[原日期字段](../_sources/daily-20260105/official-date-slices.jsonl)、[arXiv与Kimi原记录](../_sources/daily-20260105/arxiv-and-kimi.jsonl)、[原日期搜索](../_sources/daily-20260105/date-search.txt)、[原补充官方入口](../_sources/daily-20260105/supplemental-official.txt)及official-entry-0～4.txt继续保留；原09:00窗口检查不代替补充自然日检查。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS1251条metadata按pubDate核Jan04 BJT，0行；邻接Grove Jan02/Health Jan07，止日期切片 | 已检查 | 无；有限RSS范围，不授全网召回 |
| SRC-ANTHROPIC | 官方Research HTML174 publishedOn字段核Jan04，0行；Dec19 Bloom→Jan08 critical-infrastructure-defense桥接，止metadata | 已检查 | 无；有限Research目录 |
| SRC-GOOGLE-AI | 本轮重开DeepMind Publications page1，30行/265总/9页，Jan09→Dec03桥接止page1；GoogleResearch pubs首屏只有year，官方域Jan04主题日期检索首组无恢复 | 受阻 | GoogleResearch Jan04日级公开日期目录未取得；空搜索不判零 |
| SRC-META-AI | 本轮官方Research0行，官方域Jan04模型主题日期检索首组无结果，止此 | 受阻 | 必要可读日期目录未取得；空正文不判零 |
| SRC-QWEN | 官方page_config research.research-list当前60条逐date核切片，最大Dec23 2025，Jan04无行；止完整有限API，不按数组序 | 已检查 | 无；只支持当前60条目录范围 |
| SRC-DEEPSEEK | 本轮重开/news研究索引10条，Jan12→Dec31桥接，动态5条，无Jan04行，止有限目录 | 已检查 | 无；不按模型名猜日期 |
| SRC-MOONSHOT | Platform26 dated条目最新Nov07 2025；fresh exact-tag ReleaseAPI0.70/0.71/0.72，0.70=Dec31，两个Jan04已审重复事件复用；止三明确版本 | 已检查 | 无；平台及已触发项目有限范围，不扩普通PR |
| SRC-TENCENT-HUNYUAN | 首查Research对应官方POST publicList page1/pageSize1000/renderType0，code0/total9/list9，publicAt/publishedAt/display分列，最早Feb03，Jan04无行，止完整有限响应 | 已检查 | 无；不要求证明所有隐藏/删除历史不存在 |
| SRC-ZAI | 首查官方Research全部/时间排序当前15行，Jan13→Dec10/Dec09桥接，无Jan04，止查看更多前 | 已检查 | 无；不把后台created/updated当公开日期 |
| SRC-BYTEDANCE-SEED | 本轮fresh API type1/2，各2026ASC/2025DESC/count20/page_token0，19/14/18/18行，最早Jan20/Feb12与最近Dec15/Dec24，Jan04=0，按PublishDate而非pinned止 | 已检查 | 无；token/has_more与四切片在本轮记录，有限日期桥接 |
| SRC-BAIDU-ERNIE | 官方Blogpage1十条dated，Jan08→Dec23桥接，无Jan04，next2/2更旧，止page1 | 已检查 | 无；有限Blog范围 |
| SRC-XIAOMI-MIMO | Paper8dated行Jan08→Oct21桥接；Blog15行/More→官网所引JS16个/blog/路径及显式iframe，Flash Dec16、HSS/Safety Dec22，其他datedMar18及以后；两个无日期项具体贡献/范围关闭 | 已检查 | 无；完整题名/核心负侧和可核正文日期见本轮记录，不授所有历史镜像覆盖 |
| SRC-MINIMAX | English12dated Jan27→Dec23、中文13dated Jan28→Dec23，本轮均可读且无Jan04；AgentTechBlog唯一dated May13 2026，止三目录 | 已检查 | 无；不沿用旧CN/Agent提取故障 |
| SRC-ARXIV | 本轮Availability说明new/replacement/withdrawal/cross-list都按scheduled公告，Jan04 BJT无常规批次；holiday原完整官方正文复用。四窄主题lastUpdatedDate自然日发现查询仅首组，止此不扩Submitted池 | 已检查 | 无常规批次待处理；索引published/updated不证明首公开，不宣称所有作者先行镜像覆盖 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无正式候选，不评分。两Kimi版本只保留完整核心说明初筛及具体排除理由，不把同家族两个release算两篇候选；贡献前关闭已通过独立校准。

## 4. 证据与知识整合

无候选证据审阅或Books写入。以下为已确认发布的初筛与日期边界，不冒称深入完成：

本轮增量没有新候选，不改变以下有效初筛和Books决定。[本轮记录](../_sources/daily-20260105/supplement-20261007.md)说明Qwen/Hunyuan日期核查、Seed分页、MiniMax/MiMo动态目录恢复及两个无日期MiMo项的具体负侧理由。arXiv四个窄主题查询命中是submitted/version-update线索，不是当天公开论文数；没有据此扩池、评分或写书。

- [KimiCLI0.71官方release](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.71) published_at=2026-01-04T05:08:41Z（BJT13:08:41）；[0.72](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.72)=2026-01-04T06:01:07Z（14:01:07），均本窗。created_at分别04:59:46Z/05:55:57Z另存，不作为公开日期。[精确tag变更说明](https://raw.githubusercontent.com/MoonshotAI/kimi-cli/0.72/CHANGELOG.md)完整核心：0.71将file/shell通过ACP client同步并增加model/skill/info/terminal功能，未提出新的失效/控制契约或验证边界，拟不改变长期机制判断；0.72只修Python3.14安装兼容。不是因为框架名或fix标签排除；未发现这些核心说明中的安全、撤回或本书设计反证信号，不扩普通PR。
- [arXiv Availability](https://info.arxiv.org/help/availability.html) L172常规Fri/Sat不公告，L175/176首次公告才分ID且不backdate；[官方假期全文](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/) L17/21/32计划Jan4ET20公告=Jan5BJT09，恰好本窗不含右端。只支持计划边界，不伪装具体材料的实际first-public证明，不排除作者镜像或非标准变化。
- ROADMAP主线仍是模型/训练/推理/多模态/Agent机制，AI for Science暂缓；无纯主题映射占位。No Change只针对本次已确认与可判断材料，不证明所有历史研究无贡献。

## 5. 缺口与下一步

尚可执行：无。本轮root非作者独立复核已完成，原日级验收不代替本轮补充窗口验收。

本轮仍隔离两项外部终态保留项：GoogleResearch的Jan04官方dated论文/报告目录或已定位材料的原始日期，及Meta官方Research可读取同窗dated目录。当前年字段、0行正文与首组空搜索不支持零事件；定点重开条件是取得上述替代原始入口，仅恢复对应源日期切片，不扩全年。本轮已恢复Qwen/Hunyuan、智谱、MiniMaxCN/Agent及MiMo有限目录；不再请求证明全部历史无删除/隐藏或所有先行镜像，不把此前访问限制原样沿用。

隔离项不用于正面证据、Books、无遗漏或性能/安全保证，不算Coverage/Evidence无缺口。官方延迟批次仅为右端以后恢复的排期线索，未把该批Submitted标题池搬进本日，也未称已审重复。

## 6. 复核

### 本轮增量

复核者：root（非补查作者supp_jan05）

结论：通过

实际读本轮14源记录、查询边界、两个Kimi release原body/日期、MiMo动态route/date恢复及两个无日期项的负侧理由。独立重开0.71官方Release API完整body与0.72官方release核心；原版本功能集成/安装兼容没有新的长期机制命题，复用原排除而非重评分。独立读MiMo Model Description完整短核心，为产品能力展示而非训练/执行机制；材料研发标题明确落暂缓AI for Science。抽核Qwen/Hunyuan原响应日期字段、AnthropicJan08原publishedOn/slug，纠正误写的Constitutional Classifiers名称为critical-infrastructure-defense；负侧不扩到所有模型研究。arXiv规则限定常规公告，查询命中未当公开事件或深审队列。全部新增拟入选为零，Books无新命题/写入，无普通待办；两个具体来源限制不授无遗漏。原日级复核保留如下，不自动代替本轮验收。

本轮机器检查：V3字段/一致性校验通过；README及补查记录14个源ID齐全、本地引用存在、无行尾空白，限定路径git diff --check通过。只证明接口/文件一致性，不替代上述独立语义复核。未stage、commit或push。

### 原有效日级复核

复核者：root（非报告作者jan01_v3）

结论：通过

root实际完整读取README、queries-and-screening、本日两fresh ReleaseAPI body及exact-tag完整0.71/0.72核心、四窄主题查询0、全部source-date字段（Hunyuan九项多日期、Seed四slice/pagination）与入口关键日期桥接，另重开availability L170–186与holiday全文L17/21/29/32。两个release完整核心负侧准入通过，不是机械fix排除；未见这些核心中的设计反证/安全深审触发。确认0正式候选/0 Books/No Change、无普通待办，8组机构及arXiv public revision/mirror/title-backstop外部限制安全隔离。不把这一有限实际范围称全机构、全部公开修订或互联网无遗漏验证。

机器校验：最终V3 validator通过，本日本地引用、限定git diff --check及README/_sources全部新增文件noindex空白检查通过；机器结果不能替代实际独立复核。未stage、commit或push。
