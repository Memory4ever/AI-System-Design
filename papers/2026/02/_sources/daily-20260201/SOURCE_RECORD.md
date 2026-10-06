# 2026-02-01 独立原始来源记录

窗口：[2026-01-31T09:00:00+08:00, 2026-02-01T09:00:00+08:00)。执行日 2026-10-02。报告作者 feb01_v3；独立复核由 root 负责。

本轮先从当前合同、ROADMAP 和原始入口发现；没有加载旧 Daily / Weekly / screening 的候选或评分。此目录既有旧材料保持原状，只有本文件、`feb01_web*.json`、`closing*.json`、`finite_lists_final.json`、`hunyuan_metadata.json`、`date_dynamic_final.json`、`release_hunyuan.json` 是本轮依据。`LEGACY_README.md` 只作逐字备份，不作为准入依据。

## 入口与实际停止

- OpenAI：官方 [RSS](https://openai.com/news/rss.xml) 1243 个 item 只用于恢复日期；提取 2026-01-28～02-03 邻接段，不把全 feed 转成题摘队列。本窗 RSS 日期命中 8 个安全案例页面，全部读取 Actor / Behavior / Impact 核心；归到同一个 February 2026 abuse-report 家族，贡献筛选关闭。原始 pubDate 全部为 `Sun, 01 Feb 2026 00:00:00 GMT`（08:00+08），页面显示 February 1，且说明原刊于 February 2026 report；保留此日期精度/来源字段，不断言真正首公开在该时刻。前侧 Inside our in-house data agent 为 Jan29 10:00 GMT，后侧 Codex app 为 Feb2 00:00 GMT。日期表见 finite_lists_final；核心原文见 feb01_web7/8。
- Anthropic：[Research](https://www.anthropic.com/research) 官方 HTML 的 174 个 publishedOn 元数据匹配只作日期定位；窗口邻接记录 Jan28 21:07:19.613Z Disempowerment、Jan29 19:13:26.601Z Coding skills（均窗前），下一项 Feb5 00:00Z zero-days。没有把全部174项送入题摘队列。见 finite_lists_final。
- Google：[DeepMind page4](https://deepmind.google/blog/page/4/) 的 Jan22 D4RT / Jan29 Project Genie / Feb11 Gemini Deep Think 相邻片段；Project Genie 原文 [Google官方](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/) 标 Jan29，窗外。[Google Research](https://research.google/pubs/) 只恢复当前按年动态入口，无法恢复本窗有限时间切片，保留覆盖限制。没有“搜索无命中=无遗漏”断言。
- Meta：[Research](https://ai.meta.com/research/) 动态空响应；[官方results page3](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3&sort_by=relevance) 显示 Feb27/26/13/11/10、Jan2、Dec26 及更早结果。sort_by=relevance 不构成完整时间有序段，因此此有限页不证明 Jan31 无发布。保留排序/历史切片缺口。
- Qwen：[旧入口](https://qwenlm.github.io/) 跳向新站；[qwen.ai/blog](https://qwen.ai/blog) 原文与抓取只返回动态壳。补检具体 qwen3-max-thinking 页面未恢复日期正文；搜索摘要不作为 primary 日期证据。保留本窗发布目录缺口，不给零发布结论。
- DeepSeek：[官方news](https://www.deepseek.com/news/) 显示研究有限10项，Jan28 DeepSeek OCR2 到 Feb25 DualPath 跨过窗口，动态news也检查了显示段；止于覆盖本窗的相邻日期，不扫所有历史repo变更。见 feb01_web12/13。
- Moonshot：[Platform Blog](https://platform.kimi.com/blog) 当前可见26项日期均2025；[官方GitHub组织](https://github.com/MoonshotAI) 有限首页引到 [Kimi-K2.5](https://github.com/MoonshotAI/Kimi-K2.5) 与 [Tech Blog](https://www.kimi.ai/blog/kimi-k2-5)。技术博客有PARL机制但无可用首公开/修订日期；[官方模型卡](https://huggingface.co/moonshotai/Kimi-K2.5) Changelog 明示2026.1.29模板修订，不能据当前无日期PARL正文证明本窗事件。只定点恢复这一材料，不扫描整个HF/组织历史。当前日期不明的技术博客事件隔离，见 date_dynamic_final、release_hunyuan。
- Hunyuan：[Research](https://hunyuan.tencent.com/research) 原文仅骨架；隐身IAB浏览器核查超时，未据此断言无发布。再从官方前端脚本 index-I3I3bCf9.js、index-cEoitnb7.js 确认 publicList 与主机映射，POST [官方公开目录](https://api.hunyuan.tencent.com/api/blog/publicList) `{pageNum:1,pageSize:1000,renderType:0}`，code0、totalNum9、返回9；只提取日期标题，不逐篇读全部内容。最早 publicAt=1770112927（Feb3 18:02:07+08）、显示发表字段 Feb3 11:54:58+08，全部窗外。publicAt / publishedAt / displayPublishTime 分开保留，后两者不偷换首公开。当前目录不保证保留2026年1月全部历史项。[Tencent-Hunyuan](https://github.com/Tencent-Hunyuan) 与 [T1](https://github.com/Tencent/llm.hunyuan.T1) 有限主页补查。见 hunyuan_metadata。
- Z.ai：[Research](https://www.zhipuai.cn/zh/research) 可见时间段 Jan19 Flash → Feb2 GLM-OCR → Feb11/21；release-notes 当前页没有可用1月切片。以官方research相邻日期止步，非全repo扫描。见 feb01_web9/10。
- Seed：[官方论文目录](https://seed.bytedance.com/en/public_papers) 前端对应 [升序API](https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&count=100&order_desc=false) 请求实际返回20个记录，total82、next_page_token20、has_moretrue。只查看窗口相邻 Jan29 ConceptMoE / Retrieval-Infused Reasoning Sandbox、Jan31 A²D、Feb2 SPARKLING；过窗即停，不转成82篇队列。Blog 类型2相同年升序请求返回9项，total23、next20、has_moretrue，最早显示Feb12 Seedance2.0；明确当前接口返回数与total不一致，只支持已见片段，不给完整历史覆盖保证。A²D整天字段无法落窗，单独保留。见 closing0、finite_lists_final。
- ERNIE：[中文技术博客](https://ernie.baidu.com/blog/zh/) 第1页，Jan29 PaddleOCR-VL1.5 到 Feb6 ERNIE5，页面有第2页但前后日期已跨过窗口，停止第1页；无全站扩扫。见 feb01_web11。
- MiMo：[Paper/Blog](https://mimo.xiaomi.com/) Paper 日期 Jan8 MiMo-V2-Flash 到 Feb3 HySparse；Blog 当前15卡无可用历史发布日期，不用Paper时间替Blog背书。保留Blog本窗切片缺口。见 feb01_web11。
- MiniMax：[英文博客](https://www.minimax.io/blog) Jan27 M2-her → Feb12 M2.5 → Feb14 Forge；[中文博客](https://www.minimax.cn/blog) Jan28 M2-her → Feb12；中英差异保留，两日期均在窗前。[Agent TechBlog markdown](https://agent.minimax.io/docs/techblog.md) 当前完整列表只有2026-05-13 Agent Team，窗外；不是“历史上不存在Agent技术资料”的证明。见 date_dynamic_final。

## arXiv：公告时间与有界主题

[官方availability](https://info.arxiv.org/help/availability.html) 规定 Sunday–Thursday 20:00 US Eastern 公告，Friday / Saturday 无公告；包括首次发布、替换、撤回、cross-list与journal-ref事件，ID在公告时分配且不能backdate。冬季本窗起点为 Friday Jan30 20:00EST，终点为 Saturday Jan31 20:00EST，因此没有常规公告批次。下一个 Sunday Feb1 20:00EST 是 Feb2 09:00+08，窗外。本结论仅限arXiv常规公告，不能否认独立官网先行公开。

没有以Submitted代替公开；也没有把当前“recent”列表当历史当天列表。用长年月 `/list/{cs.CL,cs.LG,cs.DC,cs.AI,cs.CV,cs.RO}/2026-02?skip=0&show=25` 有界核对；cs.AI恢复首25标题，其他多为cache-miss。二月ID按公告规则均不可能属于本窗；目录失败保留，不称历史档案不存在。没有逐篇扩池。

辅助搜索四组，日期均限定“31 Jan 2026”或“1 Feb 2026”，site:arxiv.org：

1. language model / transformer / mixture of experts（架构、预训练、后训练与上下文）；
2. multimodal / world model / VLA / diffusion；
3. GPU / inference / compiler / parallel / cache（包括AR/PL/OS/PF相关系统主题）；
4. agent / retrieval / memory / evaluation（包括IR/MA相关主题）。

只作主题定位，返回主要是窗外项目；不把检索无命中当分类全量召回。来源记录见 feb01_web0/1/2/3。A²D是Seed定点引到的明确材料，而非整类回扫所得。

## 8个安全案例：全部核心筛选，1个家族，0个正式候选

这些页面是既有滥用流程的观测例证与归因限制，本轮没有发现改变具体模型 / 平台 / 评价合同的新机制或反证。不是“缺少controlled benchmark所以安全案例一律无贡献”。

| 页面 | 实际核心与关闭理由 |
| --- | --- |
| [Fish Food](https://openai.com/index/disrupting-malicious-uses-of-ai-fish-food/) | 多语内容农场；同批六条帖观看数差异与账户受众有关，不能当模型能力或新传播机制因果证据。 |
| [Silver Lining](https://openai.com/index/disrupting-malicious-uses-of-ai-silver-lining-playbook/) | 冒充咨询/招聘、公开信息检索与FaceFusion指南；无法确认邀请发送或响应，未呈现新的模型执行或控制边界。 |
| [False Witness](https://openai.com/index/disrupting-malicious-uses-of-ai-false-witness/) | 假律师/资金追讨、翻译与可信材料生成；资金与成功多为操作者输入，属于既有欺诈工作流而非新系统合同。 |
| [Trolling Stone](https://openai.com/index/disrupting-malicious-uses-of-ai-trolling-stone/) | 评论/多账户宣传、文风清理是人类分发网络的观测，未显示新增自主代理执行或模型控制机制。 |
| [Cyber Special Operations](https://openai.com/index/disrupting-malicious-uses-of-ai-cyber-special-operations/) | 拒绝计划后，操作者仍提交行动报告求润色。refusal不等于行动停止是局部描述；不能据此证明跨provider因果、拒绝绕过或新平台权限机制。 |
| [No Bell](https://openai.com/index/disrupting-malicious-uses-of-ai-no-bell/) | 外部调查引入，假署名与社媒内容生成，包含多模型；人类协作网络，不推出新的模型内部机制。 |
| [Romance scams](https://openai.com/index/disrupting-malicious-uses-of-ai-romance-scam/) | 既有ping/zing/sting流程；原文明确碎片证据不足可靠比较，未提供新的AI因果失效边界。 |
| [Date Bait](https://openai.com/index/disrupting-malicious-uses-of-ai-date-bait/) | 人工与API配合的假接待员/任务骗局；API自动化不证明新agent控制机制，钱款归因未独立确认。 |

root已实际读取全部8例Actor/Behavior/Impact并校准上述关闭理由；不要求进一步追查不影响贡献关闭的实际首公开日期。

## 日期保留项，不是正式候选

### A²D（唯一新增日期交叠线索）

[原始题摘及v1身份](https://arxiv.org/abs/2602.00759)：RLVR训练decomposer，再用生成子问题指导reasoner训练，有潜在训练探索机制，不能按“无贡献”关闭。Seed PublishDate=1769788800000编码为Jan31 00:00+08，是整天显示字段而非首公开时刻；对应整天与窗口只相交。arxiv v1 Submitted Jan31 14:48:23UTC，不是公开。Seed ArticleID=1776927992143、UpdateTime=1781527022000说明当前目录还经历后续建档/更新；不能倒推Jan31先行公开。本轮未取得官方首公开网页/可靠历史归档。隔离：不评分、不全文采用、不进入Books、不支撑当窗候选0以外的召回断言。恢复条件：取得首次可公开访问的官方原文事件时间/范围，完全落窗再开始正文证据审阅；若证为Feb2之后则归真实日期。

### Kimi-K2.5 技术博客事件

[当前原文](https://www.kimi.ai/blog/kimi-k2-5) 包含PARL与critical-steps机制，但无发布日期；官方模型卡Jan29的模板更新属于窗前已知事件，不能给当前正文内容任意指定新发布日期或更新归属。需要带日期的原始PARL公开/重要修订记录才能建立本窗事件；当前仅保留事件身份不明，不评分不Books。媒体发布日期、图片路径Jan31、Git作者提交时间均不替代该事件首公开证据。

## Books与终态边界

正式本窗候选0，候选证据审阅0，Books写入0。没有把题摘审阅包装为标准/深入证据完成；没有“已有覆盖”冒充在书稿找到同义机制。No Change仅表示本轮没有已核实当窗且通过贡献筛选、证据审阅的可写入增量。外部日期/历史切片保留项不作为正面通过与无遗漏保证。恢复仅重开上述材料/具体来源窗口，不扩扫整月。

每周来源未扫描；无按需发布批次触发。独立复核仍待root验日报整体14源、停止点、隔离项与实际无Books写入。

