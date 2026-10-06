# Daily Research — 2026-01-12

**规范：** V3
**窗口：** 2026-01-11T09:00:00+08:00 ～ 2026-01-12T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-03T00:39:00+08:00

## 1. 结论

本轮从当前原始来源独立重建，不采用旧 Daily/Weekly 的判断。冻结1个完整落窗的原始安全披露；深入审阅、非作者必要原源与owner复核、Ch72实际两段整合、独立写后及六部分日级验收均通过。普通待办0；历史目录与日期保留项明确隔离，不等原始来源绝无遗漏或所有安全主张均已验证。

检索返回的Jan11 arXiv提交时间不等首次公开：本窗终点恰为冬令时周日20:00 EST的公告时刻，因此不能把终点批次放进本窗；三篇Sunday提交按正常流程更晚，不能把其提交当该终点公告。Solar Open、CLIMP、PenForge保留更早作者公开的恢复线索，不评分，也不记为此前已经审过的重复材料。1正式家族之外，4份具名完整题摘含3日期保留和1贡献前关闭，不把宽目录命中或窗外索引数量计入候选。

Books在主体授权之后补足敏感管理资产的备用数据路径与宿主保护/兼容迁移边界，原有主体与最小权限判断保留；没有改成通用攻击或安全保证。未运行攻击或复现补丁，其他日期的材料不进入本日分母。

## 2. 来源覆盖

以下为实际有限检查，不是互联网召回保证。查询及具名筛选依据保留在[本日原始记录](../_sources/daily-20260112/DISCOVERY.md)；当前目录无法恢复历史切片的来源已明确隔离，不称零事件。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)→Index动态页后恢复[原RSS](https://openai.com/news/rss.xml)，实际1244个metadata，定点Jan8–15八项日期桥接：Jan09T11Z SB Energy→Jan13T16Z Zenken，无本窗条目 | 已检查 | RSS保留切片不保证删除历史或未索引Research；不称1244份正文审读或零遗漏 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)原HTML嵌入`publishedOn`与slug；实际Jan09T17:17Z constitutional-classifiers→Jan14T00Z property-based-testing夹住本窗，并检查January及December相邻字段 | 已检查 | 所读原目录字段无窗内条目；不保证被删除历史页或全部官方事件均保留 |
| SRC-GOOGLE-AI | [DeepMind](https://deepmind.google/research/)当前入口及Jan11定点查询；[Google Research 2026/01](https://research.google/blog/2026/01/)月目录读到Jan12 | 已检查 | 仅该公开月目录切片可核；DeepMind动态历史publication切片未恢复。NeuralGCM气候模拟属暂缓范围，贡献前关闭，不补造时刻 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)无可读正文；官方域名Jan11/2026定点补检 | 受阻 | 目标历史目录不可恢复，不据空提取记零 |
| SRC-QWEN | [旧入口](https://qwenlm.github.io/)迁往[官方Blog](https://qwen.ai/blog)；新页动态目录后恢复`api/page_config?code=research.research-list`，actual60条metadata、最新date2025-12-23T05:08:30Z；Jan11定点查询 | 受阻 | 可读旧配置不覆盖2026实时retrieval目录，不把空响应记0；目标动态历史切片仍未恢复 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/)及定点查询；恢复[官方Change Log](https://api-docs.deepseek.com/updates)，实际Date 2026/04/24紧接2025/12/01夹住本窗 | 已检查 | 该changelog切片无落窗条目；不证明全部仓库研究/修订无事件，不从当前产品反推当日行为 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog)可读完整当前26条至2024边界；官方域名Jan11查询 | 已检查 | 目录最新2025/11，所读切片未见落窗事件；不据它保证其他仓库revision也无事件 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)静态空/浏览器超时后恢复`api.hunyuan.tencent.com/api/blog/publicList`，POST page1/size1000/render0，code0、total9/list9；两个语言header均返回en。另核[HY-WorldPlay News](https://github.com/Tencent-Hunyuan/HY-WorldPlay)01/06、01/03、12/17 | 已检查 | API最早publicAt在02/03，所返切片无窗内条目；未授中文/被删除历史全量。publicAt、publishedAt与displayPublishTime不混用，仓库Updated不授新事件 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)读到2026/01/13与2025/12/10边界；Jan11定点补检 | 已检查 | 仅该边界目录切片，未保证其他API/revision全量历史覆盖 |
| SRC-BYTEDANCE-SEED | [Publications](https://seed.bytedance.com/en/public_papers)及官方`get_article_list_v2` API：US/type1/year2026，token0/20/40/60/80返回18/20/18/19/2，末页has_more=false；type2 Blog返回14、末页false。细节见原始记录 | 已检查 | 返回最早日期晚于本窗；77与total82、14与total19均有差额，历史完整性未证，不能写零事件或完整召回 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)第一页至2025/11，含01/15与01/08夹住本窗的边界，停止于旧页2/2链接 | 已检查 | 所读Blog切片未见当窗事件；日期无时区的排行不另造新论文或修订 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/)Paper完整8项，01/08技术报告至02/03 Attention；Blog最新列表无完整历史日期；Jan11定点查询 | 受阻 | Paper所读切片无确定落窗事件；Blog/代码历史事件未恢复 |
| SRC-MINIMAX | [英文](https://www.minimax.io/blog)及[中文](https://www.minimaxi.com/blog)官方入口（重定向minimax.cn），Jan11定点查询；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)及`llms.txt`当前50行索引 | 受阻 | 动态历史列表未提取；当前文档索引没有目标窗事件日期，不能记零或反推当时能力 |
| SRC-ARXIV | [公告日程](https://info.arxiv.org/help/availability.html#announcement-schedule)与具名abs/version history；短格式月列表406后恢复[长格式首25](https://arxiv.org/list/cs.CL/2026-01?skip=0&show=25)，实际total2168、1–25、nextskip25；主题有界补检 | 已检查 | 月列表首25仅有界标题线索，不是本日2168候选。规则说明本窗无常规公告批次，不证明其他入口无更早正文；特殊历史revision/mirror未恢复，日期不明项隔离 |
| 表外：[ComfyUI-Manager原始安全公告](https://github.com/Comfy-Org/ComfyUI-Manager/security/advisories/GHSA-95pq-hr8p-f5g7) | 官方repository advisory API精确时间和完整核心说明；未扫整个项目PR/release | 已检查 | 本文未运行攻击或复现补丁；不采用后来的global数据库收录日 |

未发生另外的按需扫描触发；本日不扫描每周来源组。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Unprotected Alternate Channel in ComfyUI-Manager / GHSA-95pq-hr8p-f5g7](https://github.com/Comfy-Org/ComfyUI-Manager/security/advisories/GHSA-95pq-hr8p-f5g7) | 2026-01-11T23:47:18+08:00 | 主管理界面受控但普通用户数据API能改管理配置→重新检验敏感资产全部可达路径及宿主保护版本；3+2+3=8 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)主体段后两段与末尾证据注；非作者实际POST通过 |

## 4. 证据与知识整合

### [Unprotected Alternate Channel in ComfyUI-Manager / GHSA-95pq-hr8p-f5g7](https://github.com/Comfy-Org/ComfyUI-Manager/security/advisories/GHSA-95pq-hr8p-f5g7)

家族`SF-COMFYUI-GHSA-95pq-hr8p-f5g7`。官方[repository advisory API](https://api.github.com/repos/Comfy-Org/ComfyUI-Manager/security-advisories/GHSA-95pq-hr8p-f5g7)公开和更新均为`2026-01-11T15:47:18Z`，当前未撤回；不能用global advisory的2026/06/22收录代替原事件。此次是安全说明事件，不把此前patch重新计为当日release。

作者已读Impact、Affected Configurations、Patches/Requirements、What the Patch Does、Fallback Protection和Workarounds。采用范围仅为公开威胁与迁移分支：普通用户数据接口可到达管理配置，受保护system目录依赖宿主保护API；旧宿主强制更严模式不等已消除全部路径。公告所述远程前提含网络暴露/缺访问控制，不能外推默认localhost亦受同一远程攻击。没有运行攻击、复现代码或验证完整防御。

长期命题是“管理资产的授权不能只守主操作界面，兼容迁移也必须绑定宿主保护能力”；不采用漏洞排名、通用攻击成功率或所有部署安全结论。独立对照Ch72现有资产/最小权限及Ch71租户、Ch73生产交接后，确认备用数据通道与宿主保护/迁移/回退的联动尚未具体承载。已在Ch72主体段后写两段：本机单用户为何旧存放方式合理、网络暴露后的替代控制路径、Manager3.38与宿主0.3.76+共同保护条件、旧备份与strong禁安装分支及可用性代价。全可达路径/旧副本验收是工程推断，与原公告事实分清。jan01_v3实际读取正文、前后衔接及末注，POST通过；未复现。

## 5. 缺口与下一步

**可执行普通待办：** 无。唯一候选、必要原源/owner、具名负侧、实际Books/写后及日级复核已完成。

以下为本窗终态保留项：不支持正面证据，不进入Books，不支撑无遗漏断言；仅在所列必要原始材料到达后定点重开。

**已隔离的外部保留项：** Meta/Qwen目标动态历史切片、Seed API返回/total差额及历史完整性、MiMo Blog及MiniMax历史列表。OpenAI原RSS、Anthropic原嵌入January字段和混元API已恢复，不再以初次提取失败列为未处理入口；RSS删除或Research未索引历史、Anthropic被删历史与混元中文切片未获原索引证实。DeepSeek仅恢复具名changelog切片，不授全部仓库历史事件覆盖。缺少的是目标窗原始目录/原事件身份或日期，不是已取得安全公告缺全文；可接受官方目标日期索引、可读HTML、API分页或归档快照。材料到达只重开对应来源切片和真正落窗事件，不授互联网无遗漏。

Solar Open、CLIMP、PenForge的Jan11 **Submitted**字段只作线索。若恢复作者在本窗内更早公开的正文与精确时间，再定点打开该家族；若仅有终点或其后的arXiv公告，交真实归属日，不扩本窗。不为明确领域气候模拟、一般组件说明或第三方推荐等已关闭项另索日期材料。

## 6. 复核

复核者：jan01_v3（非报告作者）

结论：通过

实际核六部分、原始查询与14到期源有限停止；读取本日五入口原字段（OpenAI RSS、Anthropic、Hunyuan、arXiv、Qwen）及Seed/DeepSeek边界，其中RSS由复核者独立抓取，其余按作者本日实际返回的最小字段核验，不冒称重复抓取全部入口。不扩2168/1244条库存为论文队列。唯一候选完整advisory、fresh repository API日期、Ch72/相邻owner及实际两正文/末注POST全部核验。另实际重开四exact-v1完整AB、三日期隔离、Cognitive贡献前关闭、HYNews及三具名issue/PR负侧；PR12510误命中的Feb18身份已修正。

不称全互联网、全部PR commit、补丁实现或所有附件已审；历史目录及revision/mirror、较早作者公开未决不授Coverage/Evidence正面结论，不进入Books，也不支撑无遗漏。完成态V3与报告/单章限定cached、unstaged diff-check通过；格式通过不替代上述语义核验。

当前依据及停点见[本日原始记录](../_sources/daily-20260112/DISCOVERY.md)。尚未stage、commit或push；其他日期及既有Books修改保持原状。
