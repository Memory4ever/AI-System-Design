# 2025-07-03 原始恢复与停止点

固定窗口 `[2025-07-02T09:00:00+08:00, 2025-07-03T09:00:00+08:00)`。本日独立读取原始payload；复制同URL缓存不是沿用其他Daily结论。带 `.request.json` 的原件保留原始获取时刻/URL（2026-10-06）；没有该文件的以下新请求保存响应原件，本记录保存实际入口与判断。网页直接读取的记录不是伪造的raw下载。

## arXiv 有界发现

API基址 `https://export.arxiv.org/api/query`，发现时间范围 `submittedDate:[202507010000 TO 202507022359]`（UTC）；仅提交池，不是公开事件窗口。

- `topic-model.raw`、`topic-model-p100.raw`、`topic-model-p200.raw`：AND `(ti:"language model" OR abs:"language model" OR ti:transformer OR ti:inference OR ti:reasoning OR ti:agent)`；start0/100/200，max_results100，submittedDate ascending，276条完整响应，末页76，标题用于主题线索。
- `topic-system.raw`：AND `(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF)` AND `(all:LLM OR all:GPU OR all:transformer OR all:"large language")`；start0/max100，22条，列表读至末项。
- `topic-multimodal.raw`：AND `(cat:cs.CV OR cat:cs.RO)` AND `(all:"world model" OR all:"vision language" OR all:"foundation model" OR all:diffusion OR all:VLA)`；start0/max100，74条，列表读至末项。
- `https://arxiv.org/list/cs.CL/2025-07?skip=0&show=2000` → `arxiv-cl-month.raw` 只恢复约1.68MB/2.94MB、35秒超时。实际只浏览前61个标题（2507.00152～2507.01479），相关标题用于查漏，没有把整月1677项或余项变成题摘队列；部分响应不证明当日分类列表完成。
- `v1-abstracts.raw` 为30个id_list精确v1完整题摘；`glmv-v1-abstract.raw` 为2507.01006v1；`check-abstracts.raw` 为22份精确v1（REG重复一次）。合计52独立题摘家族，不是本窗候选计数。具体筛选见FIRST。
- `arxiv-model.raw` 是早期错误查询，响应窗口正规化异常、total133239，不用于发现范围/覆盖。`topic-revisions.raw` 原请求lastUpdatedDate但响应title变为submittedDate，总191/返回100；未证明查到修订历史，故停止，不继续分页假冒重要修订覆盖。

实际公告有限恢复：定点打开REG/CompactDS v1 abs页面只有submission history；请求 `https://arxiv.org/list/cs.CL/2025-07-03?show=100` cache miss；REG OAI GetRecord不可达；SciRate 2025-07-03入口不可达且即便恢复也只作辅助；定点作者/公告搜索未取得精确公开时刻。没有把arXiv排班当实际公告，没有无限遍历OAI/DataCite。日期共同缺项保留精确身份后隔离，不按submittedDate移入本窗。

## 官网直接读取记录

2026-10-06T16:54:44Z 起定点复核（网页文本工具，可查URL；未保存成虚构raw）：

- [Google Research July 2025 archive](https://research.google/blog/2025/07/)：9项，July29→July2；唯一July2为[SpeechCompass/sound localization](https://research.google/blog/making-group-conversations-more-accessible-with-sound-localization/)，此前已读正文核心：multi-mic GCC-PHAT/TDOA+ASR app组合，无本项目LLM/基础生成机制增量，范围关闭。archive没有继续分页。此不代表Google publications目录全部覆盖。
- [DeepMind page5](https://deepmind.google/blog/page/5/) 和[page6](https://deepmind.google/blog/page/6/)：page5 November→July2025，page6 July→April2025，依时序停止在July/June相邻段；page6 MedGemma链接与GoogleResearch July9同一材料，下一项[Gemma3n developer guide](https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/)是June26。目标附近未见July2卡片。`?page=6` 在 `/discover/blog/` 被重定向首页、在 `/blog/` 不可达，不能用其为分页依据。此不代表DeepMind publications全量覆盖。
- [Meta Research](https://ai.meta.com/research/)：正文下载连接超时、网页工具无可提取研究payload；定点域内日期补检没有恢复历史清单。无命中不作零事件。
- [GLM-V](https://github.com/zai-org/GLM-V) Project Updates：官方当前原文2025/07/01发布GLM-4.1V-9B-Thinking及报告，未见官方07/02artifact release。当前family版本已到GLM-4.5V/4.6V，使用精确2507.01006v1身份，不继承新版本能力。日历日期无zone/time，不证明本窗事件。

## 动态目录及机构历史限制

- Hunyuan首查 `/research` HTML为SPA；`hunyuan.raw` 与 `hunyuan-js.raw`保留入口/productionbundle。按来源要求尝试隐藏浏览器加载，但30秒超时/内核重置，未获可核查的“全部”研究列表。`hunyuan-public-list.raw` pageNum1/pageSize100/renderType0返回9条全在2026，不能恢复2025窗口。
- Z.ai `/zh/research?page=2` payload仍当前20卡、截至2025年12月；page参数未获目标历史分页。不是研究不存在。GLM-V是已触发的定点原始补检。
- Seed `/api/get_article_list_v2` article_type1/publish_year2025/page_token0、20、40、60、80/count20：除token20只有SwiftSpec June12一条外，其余只含total94/has_more等metadata，无sub_article_list。再试count100的 `seed-papers-2025-all.raw` 仍无完整论文payload，停止。blog article_type2 tokens0、20、40实际15+18+8项，July14→June28之间没有July2卡，页40结束Jan6；blogs可判断此段，papers仍缺。
- MiniMax英文/中文当前blog页各12/13卡，英文最旧Oct27，中文含Jan15但没有恢复June M1，列表并非完整2025chronology；`minimax.raw`/`minimax-cn.raw`不支持窗口零事件。
- MiMo paper8项给May12、June4、September19等历史日期，June→September纸面列表无本窗项；blog当前仅2026，2025blog历史不支持零事件。

公开日期和历史payload隔离均不用于正面证据、Books、无遗漏或性能/安全保证。到达可接受原始材料时只重开对应身份/目录，不重扫其他日。

## DAY新增身份边界与最终停止

root非作者定点核EdgeLoRA原件首页：MobiSys June23–27 2025、DOI10.1145/3711875.3729141。root读取[Crossref works原始响应](https://api.crossref.org/works/10.1145/3711875.3729141)：published-print `[2025,6,23]`、published-online `[2025,9,25]`、created `2025-10-02`；ACM正文403。三字段不是实际首次公开的等价证明。可能会议正文早于arXiv上传公开，缺口须先恢复family真实首次公开身份，不能用July2提交/上传重复记事件，不需继续日期考古。已同步README/FIRST。

最终停止2026-10-07T01:04:00+08:00：52唯一精确v1题摘、43日期保留项、9贡献关闭、0正式本窗候选、0标准/深入证据审阅完成、0Books写入。14来源可取范围/停止点已记录，历史目录/真实公告/修订批次未恢复部分仍隔离。root DAY范围为三份叙述文件、52题摘和CARE/EdgeLoRA上述有限核心，未重读宽列表全部条目/未补齐受阻机构目录；安全终态通过，不是Coverage/Evidence均通过。无继续可执行待办，不stage/commit/push，不扩大其他日。
