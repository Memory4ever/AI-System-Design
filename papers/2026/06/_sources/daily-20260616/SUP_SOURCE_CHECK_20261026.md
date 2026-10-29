# Jun16补Jun15：实际来源入口与停止边界

本轮执行日2026-10-26，窗口仅2026-06-15 BJT自然日。按当前RESEARCH_SOURCES每日组次序核查；不扫描每周组。下表是实际入口和可支持的范围，不把访问成功当历史完整，不把当前官方页日期等同全球首次公开。原始下载由[有界脚本](SUP_FETCH_20261026.py)保留，`SUP_RAW_<key>_20261026.raw`命名见下表；curl失败/不完整页不授零。

## 1. 十三个机构来源

| 来源 | 实际入口/原件与停止位置 | 结果及边界 |
| --- | --- | --- |
| SRC-OPENAI | [官方RSS](https://openai.com/news/rss.xml)，`OPENAI_RSS`；XML完整解析，目标日前后条目均在feed内。Jun14 17:00GMT的[Partner Network](https://openai.com/index/introducing-openai-partner-network)折BJT Jun15，核心说明实际读到；下一Jun16 00:00GMT发布已窗外 | 已检查该feed的本窗发布。Partner Network为采用/伙伴分层、商业支持与客户案例，无新模型/训练/推理机制或受控设计反证，贡献前N，不评分。不是零发布 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)及[历史listing第2页](https://www.anthropic.com/listing/research/default/2)，`ANTHROPIC`/`ANTHROPIC_HISTORY`；历史JSON posts覆盖Jul28→Apr23，Jun12 Public Record后至Jun16 interactive coding，跨过目标日 | 已检查该research目录目标段，无本窗条目；不把当前首页独自当覆盖 |
| SRC-GOOGLE-AI | [DeepMind研究](https://deepmind.google/research/) `DEEPMIND_RESEARCH`、当前官方[具名Jun15论文](https://deepmind.google/research/publications/248131/)完整题摘；[Google Research June archive](https://research.google/blog/2026/06/)列12条、单页Jun03–30，Jun12→Jun16，无Jun15；[Publications](https://research.google/pubs/)仅year2026/430与1–15of11637，无日级filter | 博客段已检查；具名AI Consciousness论文为社会政治协商/共识论证，非模型或系统机制，贡献前N。**Publications日级完整目录受阻/隔离**，不以year或搜索0授Jun15无论文。恢复需当日发布目录/明确public日期原件，只补这段 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)当前web提取0行；[Blog第1页](https://ai.meta.com/blog/)及[第2页](https://ai.meta.com/blog/?page=2)实际读到，1页April08置顶/Jun29等不严格排序，2页Mar27→更早；定点site查询Jun15未恢复相关原始研究 | 当前blog线索已核，不能拿乱序跨界证明完整Research历史。**完整Jun15 Research发布目录受阻/隔离**；恢复需历史官方目录/当日具名原件，不能声称Meta零发布 |
| SRC-QWEN | [英文官方API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)及[中文](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=zh-CN)，`QWEN_EN/ZH`；success=true，各40篇、data只有articles无next；内容日期Jun01 Qwen3.7→Jun16 Robot suite/World/Nav/Manip | 已检查实际返回研究文章目录，目标段无Jun15；type/language非空正控正确。不因Jun16相关就移动归属或做窗外全文 |
| SRC-DEEPSEEK | [官方Updates](https://api-docs.deepseek.com/updates)，`DEEPSEEK`；完整HTML历史标题日期Apr24→Jul24/31跨界 | 已检查该发布说明目标段，无Jun15；不扩大普通repo提交 |
| SRC-MOONSHOT | [官方Blog](https://platform.kimi.com/blog)，`MOONSHOT_BLOG`，可见最新2025-11-07；[官方org API](https://api.github.com/orgs/MoonshotAI/repos?per_page=100&sort=updated)，`MOONSHOT_REPOS`，42<100终页 | 两个入口已执行，但repo created/updated不证明发布日期，旧blog无法覆盖2026。**2026 Jun15官方发布历史受阻/隔离**，需历史Blog/明确release/具名原件；不授零发布。无具名早稿则不无限追渠道 |
| SRC-TENCENT-HUNYUAN | 首查[官方Research](https://hunyuan.tencent.com/research)，`HUNYUAN`；实际`POST https://api.hunyuan.tencent.com/api/blog/publicList`，body `{"pageNum":1,"pageSize":100,"renderType":0}`，headers Content-Type application/json、accept-language zh；`HUNYUAN_ALL`及恢复后同参复验`HUNYUAN_ALL_CONFIRM`均code0/totalNum11/list11。官方bundle `HUNYUAN_BUNDLE`核api域名与语言拦截器，无需下一页。按displayPublishTime而非updatedAt，May21 Hy-MT2→Jul06 Hy3跨界 | 已检查本接口完整中文All目录，目标日无display发布；updatedAt在Jun15的旧May21项不当新发布。没有抽空动态页当零 |
| SRC-ZAI | 首查[官方Research](https://www.zhipuai.cn/zh/research)，`ZAI`；完整HTML目录May20→Jun16条目跨界，无Jun15 | 已检查该目录目标段，无本窗条目；不因后版或repo更新时间扩事件 |
| SRC-BYTEDANCE-SEED | 首查[Research/Blog](https://seed.bytedance.com/en/research)，`SEED_RESEARCH`：featured Blog不足历史，故实际进入五个`/en/blog_list/{foundation,visual,audio,ai-infra,frontier-research}`，原件`SEED_BLOG_*`。Foundation Jun19→Feb16、Visual Jul08→Apr23、Audio Jul20→Apr09、AIInfra最新2025-08-14、Frontier Jul07→Dec02'25，均当前第一页跨界/已早于目标，不读窗外正文；另[官方Papers](https://seed.bytedance.com/en/public_papers) `SEED`，1–20of247、共13页，第一页Jun11→Jun19跨界 | 论文与技术Blog目标段已检查，无Jun15；不把featured五条当全部Blog、不将13页变全站历史队列。science标题范围外不进全文 |
| SRC-BAIDU-ERNIE | [官方技术Blog](https://ernie.baidu.com/blog/zh/)，`ERNIE`；完整返回目录最新May09，含Apr/Feb/Jan历史，未见分页/next | 已检查该实际Blog目录，无本窗条目；不保证所有未列出的机构渠道 |
| SRC-XIAOMI-MIMO | [官方首页](https://mimo.xiaomi.com/)与官方静态route/frontmatter bundle `MIMO/MIMO_BUNDLE`；paper dates Mar13→Jun29，blog Jun08/Jun10→Sep等；[官方Model Release](https://mimo.mi.com/docs/en-US/updates/model) `MIMO_MODEL` Apr23→Jun02 ASR→Sep22 | 已检查官方暴露Paper/Blog/Model Release目标段，无Jun15；不把bundle加载日/模型旧更新当本日发布 |
| SRC-MINIMAX | [官方Blog](https://www.minimax.io/blog)，`MINIMAX`；完整返回目录Jun01→Jun09→Jul31，目标日无条目；可见技术研究标题按主题浏览 | 已检查该Blog目标段，无本窗条目。无本窗明确Agent Tech新事件，不扩全站历史 |

前三个隔离的历史目录不用于正面覆盖、候选日期或Books保证。它们不抹掉已取得的独立arXiv原件；普通尚未完成的审阅也不借这些外部缺口改成终态。本记录尚待唯一reader核真实停止边界，不预DAY。

## 2. arXiv主题发现与有界标题查漏

四个实际DataCite查询逐字在`SUP_FETCH_20261026.py`：`client-id=arxiv.content`，`registered:[2026-06-14T16:00:00Z TO 2026-06-15T15:59:59Z]`，仅`titles.title`主题同义词，page[size]1000。LM（language model(s)/LLM(s)/transformer(s)/MoE/GRPO等）81、system（GPU(s)/kernel(s)/collective/inference/serving/quantization/parallel/KV等）31、agent（agent(s)/agentic/reasoning/RAG/retrieval/memory/tool use）85、多模态（multimodal/vision-language/world model(s)/generation/diffusion/VLA/foundation model(s)）53，跨组214唯一身份。四raw均meta.total=data数、totalPages1、无next；这不是214项当窗新候选或全部完整题摘配额。

初始无主题`DATACITE_JUN15`超时JSON不完整，**完全不作数量/零命中/日期结论**。日公告列表没有用registered代理自动授全部公告召回；精确候选的日期层另核v1+适用官方发号/日程+findable同DOI登记，created不当上界。40个跨日区间不截Jun15，213个同日机械结果还须身份/原件/贡献核验；后者也不等213候选。

标题补检只为弥补新命名机制，实际官方窄页：

- [CL skip900/show100](https://arxiv.org/list/cs.CL/2026-06?skip=900&show=100)，`ARXIV_CL_BOUNDED_FINAL`完整100标题，前2606.13643/13647、末15735/15741。对应已发现ID段13682–14702的42个CL标题，前邻13680/13681、后邻14832/14867；不将前后其余条目改成AB或Methods队列。
- [LG skip1400/show250](https://arxiv.org/list/cs.LG/2026-06?skip=1400&show=250)，`ARXIV_LG_BOUNDED_FINAL`HTTP200/399032B、完整250标题，前12780/12808、末15701/15716；相同发现段91标题，前邻13657/13671、后邻14801/14865。**此前show300的`LG_BOUNDED`是Invalid show value错误页，不是完整列表；本合法页替代其停止依据。**

13682–14702来自本次发现身份跨度，只作为标题查漏定位，不是官方公告批次完界。两窄页包含两侧，按目标日/主题浏览而非整类逐项关闭；近邻v1已核CL13680/13681为Jun11 17:59:52/59Z、LG13671为17:58:56Z，仅说明早提交，不凭它否定延迟或将ID递增直接当公开日。初次CL show2000/LG skip1000 show1000的大页均超时，虽已越目标段只能作导航；合法窄页恢复了同段实际标题，不声称全月完整。

对标题相关/含糊增量定点恢复39身份完整题摘：`DATACITE_TITLE_EXTRA`8、`DATACITE_LG_EXTRA`31，两raw meta.total等于data、无next；总计253发现身份，36与已独立发现的Jun15旧exact-v1相同按[作者§4](SUP_AUTHOR_20261026.md#4-精确事件跨daily去重覆盖前文拟p不迁旧日期)去重。标题明确领域外只按范围关闭，相关/含糊完整AB后决定。准入校准及短core结论见作者/reader，不用发现数推入选数，不重新审旧36。

**合法页外侧有界修正：** 作者实际读了上述两页14702之后的相关标题，没有沿registered端点停止。对此已取得的134个唯一标题身份仅恢复日期字段（不是134个AB/全文队列），同client按具名DOI分45/45/44三次查询，原件`DATACITE_TITLE_BOUNDARY_1/2/3`均meta.total=data45/45/44、无next；总请求134的首raw超时不完整不使用。132项唯一v1最早公告已≥Jun16 BJT，明确窗外；其余14832 PhoneHarness（Jun12 15:01:32Z v1，registered Jun16 03:10:32Z）与14801 QPILOTS（Jun11 18:22:03Z，registered Jun16 03:09:50Z）区间跨Jun15–16，不能截成Jun15。14832为旧100同exact-v1，定点复用不迁日期；14801非旧候选，已读完整AB后作具名日期恢复线索，不先评分/列当窗。页末15716/15741 v1均Jun14、最早Jun16，构成实际外侧停止而非ID递增假说；不声称所有后续ID永无delayed submission，不为假想漏项扩全月。

## 3. 日期、当前信号与剩余普通事项

### 13个具名跨日潜贡献：原字段与有限接口边界

下表UTC原精度。v1在对应`SUP_RAW_ABS_<id>_20261026.raw`唯一历史中可核；同DOI的DataCite raw中读取`dates[Submitted,v1]`、`registered`、`state=findable`及`client arxiv.content`。表内简写raw均完整名`SUP_RAW_DATACITE_<key>_20261026.raw`，按精确DOI定位，`created/Updated`未作上界或实际公告日。earliest按适用官方14ET截止（EDT为18UTC）/20ET公告计算，只是最早可能；整个区间跨日故不截取Jun15。

| 精确v1（2606.）/身份 | Submitted UTC | 最早可能公告UTC | registered UTC上界 | raw key |
| --- | --- | --- | --- | --- |
|13705 When Can One Neuron Fix Repetition Loops|2026-06-09T21:20:57Z|2026-06-11T00:00:00Z|2026-06-15T01:39:08Z|LM|
|13706 HierSVA|2026-06-09T22:41:44Z|2026-06-11T00:00:00Z|2026-06-15T01:39:09Z|LM|
|13707 Orchestra-o1|2026-06-10T04:50:35Z|2026-06-11T00:00:00Z|2026-06-15T01:39:11Z|AGENT|
|13709 LoMC|2026-06-10T08:02:25Z|2026-06-11T00:00:00Z|2026-06-15T01:39:13Z|MULTI|
|13715 WorkBench Revisited|2026-06-10T21:21:35Z|2026-06-12T00:00:00Z|2026-06-15T01:39:20Z|AGENT|
|13731 TwinBI|2026-06-11T11:49:31Z|2026-06-12T00:00:00Z|2026-06-15T01:39:40Z|AGENT|
|13737 FreoStream|2026-06-11T12:25:13Z|2026-06-12T00:00:00Z|2026-06-15T01:39:47Z|AGENT|
|13753 Weight Norm/Grokking|2026-06-11T15:36:10Z|2026-06-12T00:00:00Z|2026-06-15T01:40:07Z|LG_EXTRA|
|13757 SEVRA-BENCH|2026-06-11T16:35:56Z|2026-06-12T00:00:00Z|2026-06-15T01:40:13Z|AGENT|
|13763 Programming Languages/Coding Agents|2026-06-11T17:34:00Z|2026-06-12T00:00:00Z|2026-06-15T01:40:22Z|AGENT|
|13767 Beyond LoRA|2026-06-11T17:59:01Z|2026-06-12T00:00:00Z|2026-06-15T01:40:27Z|LG_EXTRA|
|13768 CineOrchestra|2026-06-11T17:59:10Z|2026-06-12T00:00:00Z|2026-06-15T01:40:28Z|MULTI|
|14801 QPILOTS|2026-06-11T18:22:03Z|2026-06-15T00:00:00Z|2026-06-16T03:09:50Z|TITLE_BOUNDARY_1|

这是潜贡献已校准但必要日证缺失的具名层，不是13篇已被授当窗候选或全文配额。只对13705**实际执行**合法announced-month表单作为接口能力正控，显示月不显示日的能力边界可复用到其他12；不谎称每项重复请求了month。当前官方abs、唯一v1和同DOI findable registered已逐项取得，仍不足把区间压到同BJT日。没有另一个具名早文信号时，不排除所有假想渠道；拟将这13项保为具体外部日期缺口，不评分/不作本日正面证据。重开需该identity直接官方日公告/当日目录或有明确公开日原文，只恢复受影响日证。是否可安全停由唯一reader核；其他已合法当窗候选必要/Books仍ordinary，不借此终态。

当前官方abs轻核已发现13856/14066撤回，均仅保原始排除、不评分/采用；13856旧Jun15/Ch29唯一依赖撤回例外修复已由reader§11/12真实POST/最终读回，非本日新增I。其他材料按具名当前页轻核，后版号本身不重开v1。

**有限停止接纳（唯一reader§44）：** 十三机构实际入口/窗口段及arXiv四主题、有界标题差额/外侧日期已完成有限来源检查。Google Publications/Meta完整Research/Moonshot2026历史三项保隔离的具体外部目录缺口；上表13具名跨日材料保日期外部缺口，不评分/不正面Coverage，不将任何一个跨日区间截成Jun15。重开仅对应官方日级目录/公告或具名原文；13705合法month正控的接口能力复用，不重复无意义表单。14108/14673的当前2025workshop信号已由作者§8/reader§39恢复早正文，明确窗外，不改N或扩2025。下方先前“日期仍恢复”保为过程记录，由本句收束；当日95已过贡献/日期候选的ordinary必要/Books仍执行，不因外部目录或日期保留而终止，不预DAY。

适用官方日程/发号规则原件及2025-01-06官方snapshot按研究合同可复用，不能将周末无公告想象替代实际周日20ET公告。早提交潜P的跨日日期仍在本日作者记录内定点恢复；无贡献项不继续无用日期追溯。作者对具名13705进行了真实恢复检验：先day范围参数表单返回同from/to错误；改官方合法month参数`date-filter_by=date_range,date-from_date=2026-06,date-to_date=2026-07,date-date_type=announced_date_first,terms-0-term=2606.13705,terms-0-field=all`，原件`ADV13705_MONTH`成功返回1/1精确身份，但仍只显示“originally announced June2026”，不是Jun15。官方表单说明Announcement date只支持year/month；这次不是把一次报错改名全部恢复已尽，而是合法解析后仍缺日级。当前v1/同DOI/registered联合区间确实跨日，没有created替代上界；后续具名可用公告/原始发布线索仍按实际原件定点恢复，不扩无限假想渠道。逐篇必要/owner及候选终表仍普通可执行工作，**不是外部终态，也不是来源/日级已全部完成**。
