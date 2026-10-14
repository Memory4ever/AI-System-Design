# 04-05 来源补查：04-04 北京时间自然日

作者：supp_apr05_author。执行：2026-10-13T20:45～20:51+08:00。只补遗漏，原日报窗口、旧0候选及连续原§4保留；本次不引用04-04日报或其候选。原§4正文连续169字符（含末空行），SHA256 `cc2400e049ef7c2d9a6caf77eb7fb7b826c6f6cf77d2d7a5f03c0fe2249d6507`，逐字保留，独立DAY由root完成后才改完成字段。

官方HTTP请求、响应与参数集中在本目录 `SUP_<入口>_20261013.raw` / `.request.json`，`SUP_FETCH_20261013.mjs`只取得有界入口，不创建论文队列。读取本窗相邻日期与显式公开目录字段；正文中的媒体uploaded/createdAt不作公开日期。Google、OpenAI和Meta另用web直接打开同一官方页面恢复可见文本，下面保存必要位置，避免把一次shell失败写成永久正文不可达。

## 本轮14源与停止位置

| 来源 | 实际检查与停止 | 结论与限制 |
| --- | --- | --- |
| SRC-OPENAI | Research HTTP403；web恢复研究首页与Research Index。Index当前首屏Oct7→Sep10/Load more，未得到Apr4历史分页。RSS解析完整可见items，Apr2 10:30Z《OpenAI acquires TBPN》→Apr6 10:00Z Safety Fellowship。 | News当前目录无Apr4项；Research历史分页仍隔离，RSS不替代Research。 |
| SRC-ANTHROPIC | Research HTTP200，嵌入publishedOn相邻2026-04-02T10:56Z emotion-concepts-function→04-07T09:35Z mythos-preview。 | 当前研究目录无补窗条目；不证明未列作者研究为零。 |
| SRC-GOOGLE-AI | shell三入口网络失败；web实际打开[四月Blog](https://research.google/blog/2026/04/)9卡，末三条Apr9 ConvApparel、Apr8 Academic Workflow、Apr3 behavioral dispositions。DeepMind Publications第一页所见Apr25/23/22→Mar22（页面说明selection）；[Google Publications](https://research.google/pubs/)年份2026=409并有主题filter，无日级恢复。 | Blog相邻真正边界Apr8→Apr3，不继承旧Apr9边界；DeepMind精选不代表全部。Google日级研究切片隔离。 |
| SRC-META-AI | Research shell失败/web0行；[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication)web恢复当前页，Oct2、Sep24/7/6、Aug4、Jul29/17后混入2019/2020，末Next；试Next无法解析。 | 不把非时间顺序页面或可见首页当Apr4历史停点，目录仍隔离。 |
| SRC-QWEN | 公开retrieval接口success=true、完整articles40，逐条extra.date取Apr2T04+08 Qwen3.6-Plus→Apr15T10+08 Qwen3.6-35B-A3B。 | 当前公开模型列表无Apr4卡片；无触发则不扫高频CLI或全部普通commit。 |
| SRC-DEEPSEEK | 官方News与官网主页均HTTP200。News日期序列Apr24 V4-preview之前为2025-12；主页当前研究footer只有项目入口、没有Apr4日期切片。 | News当前有界目录无Apr4项；footer不证明全部作者研究。 |
| SRC-MOONSHOT | Kimi Platform Blog HTTP200，完整可见列表最新2025-11-07，包含Muon/MoBA等已更早项目。 | 该官网目录无补窗项；未再次遍历组织全部commit/release，也不沿用旧43仓当本轮证据。 |
| SRC-TENCENT-HUNYUAN | 官方POST publicList，pageNum1/pageSize100/renderType0；code0,totalNum9/list9。displayPublishTime Apr22T16Z Hy3-preview→Feb13T08:36Z RLVR。 | 当前全部9条已读，Apr4无目录项；publishedAt/publicAt分别是内部/实际字段，不混为显示日，当前目录不是删改历史。 |
| SRC-ZAI | Research HTTP200，实际可见显示日Apr1 GLM-5V-Turbo→Apr7 GLM-5.1；release-notes HTTP200显示Feb12→Apr7。嵌入媒体createdAt Apr3不当公开新稿。 | 两可见目录无补窗独立卡片；不依CMS建档/媒体上传制造候选。 |
| SRC-BYTEDANCE-SEED | papers API type1/page_token40/count20/x-tt-localeUS，实际18条,total243,next60,has_moretrue；整页最高PublishDate Apr8T16Z Topological，属AI for Science暂缓；项目相关Not all tokens Apr7T16Z后下一列表日期Mar31T12Z TDDFT（也属暂缓Science，只作日期邻界），这段相关slice跨左界停止，不冒全18条最高日为Apr7。Blog type2/page0实际15,total95,next20，Apr8T16Z full-duplex→Mar31T16Z招聘，已跨左界停止。 | 两官网可见序列没有Apr4卡片。旧total242/14条不继承；字段只支持现存目录，不独证历史全文首公开。宽243库非队列，AI for Science不回流。 |
| SRC-BAIDU-ERNIE | 博客HTTP200，entry-footer title日期Apr15→Feb6，正文列表横跨窗口而止。 | 博客目录无Apr4项；无触发则不把一般仓库commit当研究。 |
| SRC-XIAOMI-MIMO | 官网页HTTP200，8条Paper有原日期，June29 cross-model-distillation→Mar13 Agent Hologram跨窗；15条Blog（含blog-more隐藏区）都无原日期。 | Paper有限检查有效；Blog没有可核历史日期停点，日级切片单独隔离，需dated官方原稿/历史目录才能定点重开，不追15全文。没有“18仓全组织已核”新声明，历史删改/未列作者稿不由现目录证明。 |
| SRC-MINIMAX | 英文/中文Blog HTTP200，相邻Mar18→Apr27。Agent llms索引与techblog.md均200；techblog当前列Sep19/22、Oct8三项。 | 主Blog无补窗项。旧Agent index“只见Apr27”无法由当前三条支持，Agent历史切片单独隔离，不据现时索引宣称Apr4零事件。 |
| SRC-ARXIV | 本轮重开availability HTTP200；完整Apr4 BJT对应Apr3 Fri12→Apr4 Sat12 EDT，正常Sun–Thu20批次不在窗。CL四月列表只作原始查漏入口，不扩2000条全文队列。另四组窄查询见下。 | 正常公告规则仅支持没有常规batch，不证明特殊公告/机构首次公开不存在。主题搜索不满足严格历史日期，检索受限；不授全学科召回/无遗漏。 |

## 本日限定主题补检与负样本校准

查询都执行到搜索返回结果页即停，没有继续翻宽库存。四个arXiv主题表达均为 `site:arxiv.org/abs/ "2026-04-04"`，分别附 `(language model OR Transformer OR MoE)`、`(inference OR GPU OR distributed training OR kernel)`、`(multimodal OR world model OR vision language OR diffusion)`、`(agent OR tool OR RAG OR memory)`。分类边界按来源清单：CL/LG，DC/AR/PL/OS/PF，CV/RO，AI/IR/MA。实际引擎返回2610.09051、2610.13455、2610.12989、2610.10085等十月页，说明日期文本筛选没有得到有效Apr4历史切片；不是Apr4零论文证据，未按这些十月题摘建立候选或另日工作。

另官方域名有限日期补检使用Apr4/2026-04-04并限定model/training/Agent、模型/研究。本轮未返回可核Apr4官方研究事件；返回OpenAI Community Codex rate limits与plan-mode用户讨论。它们不是作者/机构研究原件：订阅额度、建议保存Plan等产品反馈没有新增模型/系统机制或可审因果证据，前分母排除，不评分、不写Books，不为这些具体已排除项追日期。明确边界的代表性负样本供root独立抽核；没有首批拟入选项可校准。

## 剩余安全终态

确定新增候选0、原候选0；没有证据审阅/Books普通项，Books No Change。五类机构来源保留：OpenAI Research历史分页、Google Research日级publications、Meta Research/publications时间切片、MiMo无日期Blog日级切片、MiniMax Agent旧技术博客历史切片；连arXiv必要历史事件切片共六类限制。特殊arXiv/独立官网首公开未知覆盖不被“无常规batch”抹除。上述限制不用于正面证据、Books、全Coverage或无遗漏；取得具体落Apr4 BJT的官方dated原稿/公告或可核历史切片后，仅定点重开该源和family。MiMo仅缺日期层，不把15条无日期Blog变全文队列。正常公告规则、v1提交、DOIcreated和旧完成标签均不代替本轮补查。

普通待办仅root非报告作者完整六部分DAY；尚未通过前README状态保持进行中。无需Books窄锁，无Books新写，未stage/commit/push。

## root实际六部分DAY：通过

root非本补充报告作者，于2026-10-13实际完整读README六部分、本记录、当日请求参数/HTTP停点及关键原响应。实际重开官方arXiv announcement/ID规则、Google四月Blog/Publications、Meta Research与OpenAI Research Index；另读Qwen40条extra.date、混元9/9显示日期、Seed18/243与15/95及next60/20、Anthropic嵌入publishedOn、OpenAI RSS相邻items、MiMo8篇dated Paper/15条无日期Blog和MiniMax三条技术博客原件。检索反侧独立限定Apr4日期/主题核到窗外九十月arXiv页与Codex额度/PlanMode产品讨论，不把这些命中计为当日论文或技术证据。

1. 结论与规模：旧0＋确定新增0，未拿旧提交/created库存或无常规batch倒推全源零论文；Books新写0，有限覆盖与不能恢复的切片分开。
2. 来源：14组均有实际入口/停止或具名隔离；Seed18条中Apr8科学项与Apr7相关邻界已区分，未把243全年量变全文队列。root发现MiMo无日期Blog不能证明日停点、Seed最高日期不能拿相关slice代全部，作者已按原响应最小修正且root实际读回。
3. 准入/负侧：没有确定当窗拟入选项；代表性产品反馈仅额度/计划保存建议，不提供本项目可审机制/因果反证，具体关闭有效；日期不可靠的窗外搜索结果不评分、不移入其它日报。
4. 证据与Books：无新增候选需要Source/owner或写书，不制造diff或伪造POST；原连续§4和旧候选保持，No Change只限确定候选，不对受阻来源作负面证明。
5. 终态边界：五个机构切片（OpenAI/Google/Meta/MiMo Blog/MiniMax Agent）及arXiv特殊事件历史切片精确隔离；不授正面Coverage/Evidence、无遗漏或研究零发布。可接受替代原稿/目录、恢复身份/日期与定点位置明确，无已知可执行候选被转成外部受阻。
6. 复核/检查：root独立身份与实际范围可追溯；初筛、必要证据、写书和验收不混同。实际V3与限定cached/unstaged diff-check通过；HEAD原窗口与连续原§4（含标题185字符、正文169字符）逐字保持，四个本地路径存在。机器只检查格式/冻结，不代以上语义判断。

DAY实际通过；作者现在可仅同步完成字段与§1/5/6验收叙述，root一次实际FINAL读回后才增加全年验收数。本日没有Books锁；未stage、commit、push。单日checkpoint不是停止指令，完成后由root以fresh上下文继续分配下一未验收日期。

## root一次实际完成态FINAL：通过

root实际读回正式报告状态完成、检查时间2026-10-13T21:32:46+08、原窗口/04-04自然日补窗和全§1/5/6：旧0＋新增0、Books新写0、普通待办0；本轮独核为root、结论通过且按本记录真实DAY范围，无以旧完成态代本轮。五机构切片与arXiv限制仍隔离、不授正面覆盖或无遗漏，MiMo无日期Blog和Seed整页/相关slice修正保持。完成态V3及限定cached/unstaged diff-check通过，原窗口与169字符连续正文§4保持、5本地路径有效；没有新的Books状态需要POST。

FINAL通过，可计入全年日级验收；这是已处理到安全终态，不是所有来源均证明无发布。root继续fresh下一日期，本日作者ownership释放，不stage、commit、push。
