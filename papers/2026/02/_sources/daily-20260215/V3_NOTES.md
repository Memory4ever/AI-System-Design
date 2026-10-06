# 2026-02-15 来源执行与筛选停点

检查：2026-10-04T20:58:36+08:00。仅窗口 2026-02-14T09:00:00+08:00 ～ 2026-02-15T09:00:00+08:00。
当前 AGENTS、研究合同、Report V3、统一 Prompt、ROADMAP 与 LEARNING_STATE 最新 JanFeb 路由已在启动读取；未读取其他日报/Weekly。
旧 V2.1 空收据只保留历史，不采用 Complete 和注册生效日排除机构来源的规则。

## 查询与实际停止

本日 V3_DISCOVERY_0..2 是逐组官方入口；V3_SEARCH_0..3 是带 site、日期范围或精确 2026-02-14 的主题/日期查询。
V3_WESTERN_0 是官方研究索引及 Blog 入口，V3_WESTERN_1 为二月局部历史恢复；原始查询保留在工具结果 Source 字段与本记录。
Search0: site:openai.com/index/ after:2026-02-13 before:2026-02-16 research model；
site:anthropic.com/research after:2026-02-13 before:2026-02-16；
site:deepmind.google/blog after:2026-02-13 before:2026-02-16；
site:research.google/blog after:2026-02-13 before:2026-02-16 model training。
Search1: Meta February2026/14、Qwen/DeepSeek/Moonshot 2026-02-14。
Search2: Hunyuan/Zhipu/Seed/ERNIE 2026-02-14。
Search3: XiaomiMiMo/MiniMax英中文/MoonshotAI GitHub 2026-02-14。
Western1: Anthropic研究、OpenAI/index、DeepMind/blog、GoogleResearch/blog 的 February2026；只检查相关日期/题摘，不将整月结果作逐项队列。
Tail0: DeepMind February2026/12；Anthropic after02/12 before02/16；XiaomiMiMo、Tencent-Hunyuan GitHub 02/14。
Google Research二月归档实际夹在02/11与02/17，原始全文192行，无02/14或15日期项；Publications只到2026年粒度，不能证明该日零事件。
Meta publications page=3 日期顺序实际02/26、02/13、02/11，未查其他页。
Z.ai Research“全部”实际02/21、02/11、02/02；release-notes实际02/12、02/03，不把后来技术报告首发改为开源日。
ERNIE blog首面日期顺序05/09、04/30、04/15、02/06、01/29，停止01/29。
MiMo Paper 实际03/13、02/03、01/08；Blog当前目录不提供所有旧日内容，无02/14补检命中，仍有限制。
Moonshot blog当前完整可见Overview最新2025-11-07；GitHub组织主页当前研究链接无历史当天时间，不把组织更新时间作发布。
DeepSeek 主页“研究→更多”实际 /news/：研究索引02/25、01/28、01/12，停止01/12；不是仅产品首页零命中。
MiniMax英文blog首面已穿过03/18、02/14 Forge、02/12 M2.5、01/27；中文本日相应正文也恢复，AgentTechBlog仅导航无历史日期索引。
OpenAI初始ResearchIndex首面停止Sep3，Anthropic首面停止Sep4，DeepMind首面最新研究，无完整二月批次；官方定点查询为有限补检，不能把首页/搜索的无命中当历史零遗漏。

## Hunyuan 实际浏览器观察

Web 提取为0行后按来源要求打开浏览器 https://hunyuan.tencent.com/research 。初始空AX后getAXState成功，URL变为 ?page=1。
研究全部列表11个当前条目，日期依次：
2026-09-22；2026-09-22；2026-08-28；2026-08-11；2026-07-21；2026-07-06；
2026-05-21；2026-04-30；2026-04-23；2026-02-13；2026-02-03。
本窗附近条目：2026-02-13 Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping（黄冠华、许庭强、王锦波）；
2026-02-03 Learning from context is harder than we thought。
日期13不带时区/时刻。作者原始简介和官方GradLoc仓库确认distributed binary search将gradient spikes定位token及layerwise clipping稳定策略，不能仅按标题/主题关闭。
初始观察未得时区后留日期待核；root提供唯一日期恢复位置，本线程只读该证据并定点访问官方detail。
https://hunyuan.tencent.com/research/100015 本日直接只读POST detail英文标题，公开字段publicAt/publishedAt/displayPublishTime/updatedAt=1770971763，即2026-02-13T16:36:03+08:00；选定字段保存在V3_HUNYUAN_DATE_ACTUAL.txt，明确窗外。
root给出的窄日期证据来自papers/2026/02/_sources/daily-20260213/V3_HUNYUAN_PRECISE_DATE.md L7–15，为1770971794（16:36:34），只读此日期证据不读其他日报。两次字段相差31秒，原因未核实（不把语言版本推测当事实），归属均窗外。
不读该博客全文或重扫其全部实现，不声称artifact/论文首公开同博客。初始GradLoc日期隔离由这个实际依据解除为窗外。

Qwen当前Research静态0行；浏览器首次隐藏选项报subagent不支持，去掉选项后导航超时/kernel reset。
按debugging技能保留失败条件，没有把故障当空列表。官网旧站已跳qwen.ai；定点官方博客与官方仓库对照：
博客2026/02/15，时区未知；官方QwenLM/Qwen3.5重定向Qwen3.8的News记2026-02-16首发。不以二者补造09:00。
raw V3_IDENTITY_BOUNDARIES.txt 为实际官方README News及FirstProof X 403依据。

## 准入与代表排除

- 唯一确认落窗工作候选：OpenAI First Proof首次attempt分享，官方回顾明确2026-02-14 00:00PT；
  换算PST(-08)为2026-02-14T16:00:00+08:00。只处理公开attempt与自主评价不能混淆的边界。
  当前02/20描述limited human supervision、human best-of-few与P2纠错是后来观察，不是本窗新发布或已核准的数学结论。
  root非作者实际核V3_WESTERN_1后准许DD1+SR1+D2=4低分关闭；原始X为403，
  当前官方PDF首页明确First Proof? / OpenAI / February20,2026（90页）；仅核第一页身份，不遍历10个proof。
  不把这个后来PDF冒充02/14精确版本，不报告自主pass-rate、成功证明数量、模型训练算法或普遍可靠性。
- Seed2.0 Official Launch：读核心说明后排除贡献。原始date2026-02-14，未核时区/时刻，因贡献排除不再追日期。
  只有模型家族/能力分数/价格与VideoCut工具名，没有新增可复用方法、控制混杂的机制归因或会改变项目设计的有效条件。
  当前落地页已标April升级，官方发布页含Feb16榜单，均不倒灌本窗。root实际核后准入排除通过。
- Forge：目录/新英文/blog原始日期2026-02-14；旧英文/news显示2026.2.13，JSON-LD datePublished=2026-02-13T00:00:00.000Z；
  中文正文2026-02-12，HF作者原文Published February13,2026。这些不是新revision依据。
  核心WindowedFIFO限制从滑动窗口取完成轨迹有具体吞吐/分布选择，但首先公开时间冲突无法本窗确定，精准隔离。
  先前消息把调度增量误写为bounded-staleness+soft-suspension：原文实际是WindowedFIFO，已纠正此初始描述，不采用错误机制。
- OpenAI GPT5.2 gluon result/蛋白质成本：范围为领域科学应用，当前AIforScience暂缓；
  不读专业解法，不借Evaluation owner重新准入。首发日期字段未作本窗落窗声称。
- 搜索中的OpenAI社区投诉、用户图像、第三方llm4free provider修复/airun日志选项：具体新增仅产品反馈或provider适配/日志；
  不证明公开研究、训练/推理的新机制。已关闭；日期不必为贡献排除另追。
- Qwen3.5：潜在项目增量明确但必要日期不确认，留缺口，不评分、不作正面证据；GradLoc博客经窄日期核验明确窗外。
  这不是因深审耗时或Books已有覆盖而缩池；未进入确定落窗候选的原因仅日期/事件身份必要条件不满足。

## 外部保留与普通工作

普通可执行工作：无。root实际顺读六部分与本记录，并核唯一候选FirstProof日期/后来观察/PDF身份，代表排除Seed2.0、Forge/Qwen日期隔离、GradLoc本日公开字段；直接重开arXiv政策核公告日。本日日级独立语义复核通过，完成态V3校验、限定diff-check、6个本地引用存在性通过。未全量重读无关附件/数学解法/全站历史。原始txt仅机械去除行尾空白，未改原字段、日期或正文含义。
外部：Forge、Qwen3.5日期；OpenAI/Anthropic/DeepMind/GooglePublications历史日期段；
Moonshot/Xiaomi动态旧发布与MiniMaxAgentTechBlog历史目录。均不支持正面候选/Books或零遗漏保证。
恢复只需相应目标窗口官方日期索引或精确首次公开时刻，重开对应项，不全月或全站重扫。
