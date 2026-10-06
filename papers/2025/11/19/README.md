# Daily Research — 2025-11-19

**规范：** V3
**窗口：** 2025-11-18T09:00:00+08:00 ～ 2025-11-19T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-04T19:39:03+08:00

## 1. 结论

原日级验收保持有效于未变范围；用户指定官方RSS日期恢复后，仅重开Codex同家族，root已实际通过新增日期/必要Evidence/OnlyReport及局部报告范围。确定落窗候选2家族：Gemini API/UI及Codex-Max官方publication/release所披露的外生用户编辑RL训练；均必要深入完成、仅报告、Books实际写入0。普通待办0，无新Books/POST。新模型名称与排行榜不作准入理由。

原11方向及窄主题6方向的首公开隔离不变，既有准入/必要反侧不重审。Gemini API深入、UI core标准与OnlyReport继续复用root通过；Codex新增官方publication/release日期及必要core/owner独立通过，不认证Safety Hub最早公开。实际改书0、无POST，不用名称缺位造长期缺口。原[首批校准](../_sources/daily-20251119/ADMISSION_CALIBRATION.md)、[必要证据](../_sources/daily-20251119/EVIDENCE_NOTES.md)、[窄主题包](../_sources/daily-20251119/NARROW_TAIL_CALIBRATION.md)和[作者停点](../_sources/daily-20251119/AUTHOR_STOP.md)未变范围保留。

root原负侧5项通过及TDD+CI改潜在的处置不变；18篇论文（11+6+1）仍具名日期隔离，98%比值与预算限制不变。原Anthropic/Z.ai/MiniMax来源处置不重扫，见[负侧notes](../_sources/daily-20251119/NEGATIVE_INDEPENDENT_REVIEW.md)与[来源补检](../_sources/daily-20251119/SOURCE_ENTRY_SUPPLEMENT.md)。root17:25:31[原日级复核](../_sources/daily-20251119/DAY_REVIEW.md)及本次Codex增量独立通过共同覆盖当前报告；终态保留项不授正面Coverage、Evidence、Books或无遗漏。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 原Research有限补检保留；本次仅指定Codex两个官方RSS guid、200原XML及publication入口身份恢复，均Nov19 00:00GMT/BJT08:00，见CODEX_DATE_REOPEN | 受阻 | Codex官方发布事件已恢复，未认证Safety Hub最早公开；目标历史Research列表仍不足，不授无遗漏，其余原范围不重扫 |
| SRC-ANTHROPIC | 原Research首页GET200，Flight publicationList.posts实际171条；只核目标月标题/日期/slug，Nov21→Nov12跨本窗，publishedOn过滤本窗无条目；Nov18三公告核心另核，详见SOURCE_ENTRY_SUPPLEMENT | 已检查 | 只支持当前列出目录目标区间，不授删除/未列材料或历史版本无遗漏；不把171条变题摘队列，三公告不代Research |
| SRC-GOOGLE-AI | DeepMind/Research原入口、相关blog及Gemini/API/UI官方推出core；UI app原HTML精确Nov18T16Z，原Research blog/PDF日期权限分离 | 受阻 | 确定发布已处理；publication目标历史切片不能由当前入口还原，已隔离。PDF发布日身份未绑定且数值不采用 |
| SRC-META-AI | Research动态入口、publication page4实际Nov19→Nov18 SoCE→Nov11后混旧年；SoCE原页自然日期，直抓reset；WEB_NATIVE_SEARCH_05/COVERAGE_06 | 受阻 | 停page4，不由非严格排序授全历史覆盖；需目标原列表及SoCE精确首公开，现隔离，不扩旧年题摘 |
| SRC-QWEN | 旧入口重定向qwen.ai/blog，目标日有限补检及HTML/home/layout/shared三份bundle；浏览器blog及实际research索引无条目、日志appendChild错误，详见QWEN_BROWSER_STOP | 受阻 | 动态目标历史列表未得，未调用未确认API；停止空路径与盲抓bundle，需官方目标段列表/原API响应，不授零命中或正面Coverage |
| SRC-DEEPSEEK | 官方Research & News直页L7–13已实际读；research Nov27→Nov1、news Dec1→Sep29，WEB_TARGETED_20 | 已检查 | 仅当前可见目录目标区间；View All未展开，不授整个历史目录或删除材料无遗漏 |
| SRC-MOONSHOT | Kimi overview/changelog，最新边界Nov7/Nov6；WEB_NATIVE_02/04 | 已检查 | 仅支持当前公开目录所显示的目标日期区间，不保证删除/未列出的历史材料 |
| SRC-TENCENT-HUNYUAN | 官方Research动态提取失败、浏览器有限失败；POST publicList pageNum1,pageSize20,renderType0，实际total9且均2026blog | 受阻 | 2025 Research历史段未恢复，2026英文blog不是替代；精确重开见§5 |
| SRC-ZAI | 首页15条nextPage2/hasMoretrue；本次IAB超时后按Research组件原分页实现GET ?page=2，累计18条/hasMorefalse，最早createAt Dec7；停止第2页，raw/receipt/结构化字段见SOURCE_ENTRY_SUPPLEMENT | 受阻 | 当前列表已耗尽但2025-11目标历史段缺失；不以CMS createdAt或release notes补造首公开，不再把已执行查看更多列普通待办；需目标历史原列表 |
| SRC-BYTEDANCE-SEED | GET get_article_list_v2，type1/2、2025、count20、page_token0及20、order_desc=true、x-tt-localeUS；置顶单核，page20全部早于6月20日，停止20 | 已检查 | 当前返回目录覆盖目标日期边界，不授全年全读；has_more=true,next40保留，不扩大旧标题队列 |
| SRC-BAIDU-ERNIE | 官方Blog两页均实际查看；日期边界Nov21→Nov11，停止第2页 | 已检查 | 仅当前目录目标日期范围，不声称整个机构历史无遗漏 |
| SRC-XIAOMI-MIMO | Paper8条2026-01-08→2025-10-21跨目标；Blog15标题无日期且More；实际home/index bundle仅layout/chunk映射，WEB_MIMO_TAIL及receipts | 受阻 | Paper边界已查，Blog目标历史日期列表未得；停止盲抓chunks，不以Paper代替Blog或把15标题变全文队列 |
| SRC-MINIMAX | EN/CN博客CN13条Dec23→Oct27；追加Agent Tech合同入口、等价Markdown与llms索引各200，当前只列2026 Agent Team条目；停止该实际入口，见SOURCE_ENTRY_SUPPLEMENT | 受阻 | 模型博客可见目标边界已查；独立Agent技术目录2025目标历史缺段不能由当前文档或CN博客替代，需目标历史目录/快照；不授全机构零命中 |
| SRC-ARXIV | 原language主题query及CL有界标题12500≤id<13800；system/multimodal既有请求补正后发现OR过宽，收窄AND实际18/6标题第一页读完；11+8份exact-v1题摘及TDD原完整题摘/v1关键条件，NAND去重；URL/start0/size50/停止详见NARROW_TAIL_CALIBRATION | 受阻 | 窄主题有限发现已停，不授全分类召回；submitted非public、announcement日级过滤不支持、API过滤响应失配。18篇潜在论文首公开具名隔离；未把349/440宽结果变题摘/全文队列 |

以上原始材料均在[本日_sources](../_sources/daily-20251119/)；入口与停止细节见[校准包](../_sources/daily-20251119/ADMISSION_CALIBRATION.md)。未扫描每周来源。本日尚无注册表内按需来源的发布/协议触发；为既有材料打开官方API说明是必要证据恢复，不扩机构全站。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Gemini 3](https://blog.google/products-and-platforms/products/gemini/gemini-3/) | 2025-11-18T16:00:00+00:00 | signature/tool-output组合改变多轮兼容性；同家族UI推出改变交付对象但偏好/等待分账；2 + 2 + 1 = 5 | 深入完成 | 仅报告：API深入及UI官方core标准/OnlyReport均获root非作者通过；版本/交付实例不强造长期缺口，改书0 |
| [Codex-Max publication/release](https://openai.com/index/gpt-5-1-codex-max-system-card/) | 2025-11-19T00:00:00+00:00 | RL rollout内用户冲突编辑/保留改动强化；2 + 2 + 1 = 5 | 深入完成 | 仅报告：root增量独立通过，版本训练实例未给可核对照/有效性边界；改书0 |

## 4. 证据与知识整合

### [Gemini 3](https://blog.google/products-and-platforms/products/gemini/gemini-3/)

公开日期来自原始HTML JSON-LD `datePublished=2025-11-18T16:00:00+00:00`，即BJT19日00:00，落窗；当前页面`dateModified=2026-03-19T17:52:32.737752+00:00`必须保留。因此不把当前链接到的2026年5月model card作为2025年11月证据。

[开发者发布说明](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-3-developers/)核心L262–263、L292实际宣布signature验证、thinking level/media resolution参数及工具/输出组合变化，原始记录见[WEB_GEMINI_DEVELOPER](../_sources/daily-20251119/WEB_GEMINI_DEVELOPER.txt)。恢复官方cookbook精确提交de43f20的thinking参数及同版本manual function-history例；当时Pro仅列low/high、默认high，旧thinking_budget仍兼容。客户端签名逐part规则/具体400条件没有发布日版本依据，不采用；当前指南已改为2026年3.1/Interactions，明确隔离。client-side bash是模型提议命令；hosted server-side bash当时为early-access partners、GA coming soon，不写成普遍可用或安全保证。

状态携带命题owner为`AGENT-CONTEXT`，实际对读Ch75执行状态/typed-state保留和Ch74/76交接；这覆盖一般原则，不冒称已覆盖opaque-signature具体协议。Ch78实际Proposal→validation→authorization链承载bash提议与授权分离，但成熟原则不计本次增量。root实际亲核日期、developer目标段、精确两notebook cells及owner，必要Evidence/OnlyReport通过，不请求共享Books写锁；模型/能力榜单数字未采用为性能结论。日期raw L49–56、精确notebook、反侧/停止及owner差额见[单项包](../_sources/daily-20251119/GEMINI_SINGLE_REVIEW.md)，非作者结论见[独立审阅](../_sources/daily-20251119/GEMINI_INDEPENDENT_REVIEW.md)。只此项，无Books改动、无POST。

同家族[Generative UI app推出](https://blog.google/products-and-platforms/products/gemini/gemini-3-gemini-app/)由原HTML L55同一Nov18T16Z时刻、L56仅晚4秒修改及正文当天rollout支持，不是论文首公开。官方Research core公开prompt条件的可执行界面、server tools/指令/postprocessors，且明示偏好评价不计生成速度、分钟级生成及偶发错误；只采用交付对象改变和该限制，不采用组件收益因果、未绑定22页稿数值或后来50%。Ch66开篇五类成功事件及Resource Budget实际支持偏好/outcome/运行资源分账，Ch65/67交接已读；新增实例不改变长期解释，OnlyReport不强改书。root实际日期/最小core/owner及OnlyReport通过，见[两项独立裁决](../_sources/daily-20251119/UI_AND_TRAINING_INDEPENDENT_CALIBRATION.md)与[UI原请求](../_sources/daily-20251119/UI_EVENT_CALIBRATION.md)。API深入、UI标准满足本家族受影响内容的必要投入，不机械增加第二家族。

### [Codex-Max publication/release](https://openai.com/index/gpt-5-1-codex-max-system-card/)

官方RSS两个guid均Nov19 00:00GMT/BJT08:00，publication入口指向同一Safety Hub card，采用官方发布事件，不认证正文最早可见时刻；原Published Nov18无时区字段保留。§4.3.2.1披露user model在RL rollout中制造冲突编辑并强化保留改动；§3.1 sandbox/unsandboxed批准及§4.2不可信输入限定它，不证明训练替代授权或干预收益已归因。实际对读`TRAIN-RLHF` Ch31多轮模拟器/trajectory归因、环境transition及reward代理反侧，Ch30/32邻接与Ch78 proposal授权链。差额为同一共享workspace中的外生编辑，不是静态指令；当前披露缺可核扰动/reward/独立对照与该项结果，仅报告版本训练实例，不造长期配方缺口。root实际核RSS、入口L13–27、同card L161–207及Ch31正文，增量日期/必要Evidence/OnlyReport独立通过，见[恢复包](../_sources/daily-20251119/CODEX_DATE_REOPEN.md)。未写Books或请求锁，无POST。

## 5. 缺口与下一步

作者普通待办0；Codex日期恢复后的增量独立复核已通过，旧日级未变范围复用。以下外部限制为本窗终态保留项：不支持正面证据、Books、性能/安全保证或无遗漏断言；仅对应精确材料/可靠公开时间或目标目录到达时定点重开，不重审全附件：

- root已实际通过有限source/query/分页/停止及最终六部分；[窄主题独立notes](../_sources/daily-20251119/NARROW_TAIL_INDEPENDENT_REVIEW.md)已关闭6方向准入/2代表性排除校准待办；[新增负侧notes](../_sources/daily-20251119/NEGATIVE_INDEPENDENT_REVIEW.md)已实际通过Intuit/Foundry/Rwanda/Hope/NeuroLex五项，TDD撤销关闭。Microsoft/NVIDIA合作未在新增抽检复读，不冒称8个关闭全部重新亲核，不自动扩为全附件待办。原已校准题摘范围不重核，必要反侧已保留，不把非采用项未读附件或owner比较列普通待办。
- Generative UI官方推出事件已通过、归Gemini同家族，剩余仅是未采用PDF的版本身份保留；最小替代为该22页稿发布时快照/可靠版本绑定，只有将来实际需要采用实验数值才重开，不继续追PDF日期、不扩所有附件。
- arXiv：官方表单明确announcement只支持年月；日级空结果不授零命中。original submitted查询只用于窄主题发现，language-model查询503结果首页含后来公告项，未转入题摘队列。现停新增全日发现，只处理既有材料的必要纠错；不扩整月全类全文。Donors v3中心方法差异已定点核并作版本隔离，后版不当本窗事件；KAN AppG具体不等式疑点隔离理论率，不抹掉局部实验。
- OpenAI/Google publications/Meta/MiMo目标历史切片的有限恢复已经停止，当前原入口/定日查询/bundle未能提供必要目标列表，作为本窗目录保留项隔离；不是检完所有历史或零命中。最小替代分别是OpenAI研究目录目标段、Google相关publication目标原列表、Meta按事件/日期可靠排序的目标列表、MiMo Blog有日期的目标More段。Anthropic已从原Flight恢复目标区间，撤销此前不可恢复陈述；只支持当前目录，不认证历史版本。MiniMax Agent实际入口/Markdown/index检查已止于2026条目，需2025目标techblog目录/快照，不能被CN模型博客替代。只重开相应目标切片，不重扫整月。DeepSeek等已检查行只支持其实际可见边界，隐藏/删除材料不授无遗漏。

当前具体目录保留：Hunyuan2025 Research目标历史段、Zhipu2025目标历史段与Qwen动态目标段，root已核整体安全终态。Hunyuan提取/浏览器有限失败后API仅给2026blog；Zhipu真实分页已成功，累计18条hasMorefalse但仅Dec7以后，停止第2页，release notes不是Research替代；Qwen原页/研究索引浏览器均无条目并有加载错误，三份必要bundle仅给prefix，未确认endpoint，详见[浏览器实际停点](../_sources/daily-20251119/QWEN_BROWSER_STOP.md)与[本次补检](../_sources/daily-20251119/SOURCE_ENTRY_SUPPLEMENT.md)。恢复条件为各目标历史段官方列表/正文或可核原始接口响应；相同失败路径不反复重试，均不支持候选、Books、无遗漏或正面Coverage。

有限恢复后已精确隔离的潜在项：11篇论文保留[原准入理由](../_sources/daily-20251119/ADMISSION_CALIBRATION.md)、[已读必要证据](../_sources/daily-20251119/EVIDENCE_NOTES.md)与[逐ID日期原字段/最小请求](../_sources/daily-20251119/AUTHOR_STOP.md)，不因日期不定改判贡献排除，但当前不作为确定当窗候选、正面证据、Books或无遗漏依据。API published与Submitted相同、DataCite Available仅月份，Updated/registered不能单独认证首次公开；STEP OAI仅日粒度，SoCE原HTML抓取reset，NAND publisher DOI实际打开后受JS验证阻断。最小替代为各精确v1的实际官方公告/可查首公开上下界（完全落窗）；只有该材料到达才重开对应项，不逐一扩全部实验附件，也不以schedule补造09:00。

Codex此前日期保留现已恢复为官方publication/release事件，见§3–4及[增量包](../_sources/daily-20251119/CODEX_DATE_REOPEN.md)；撤销该发布事件的datehold，保留Safety Hub原字段与最早公开未知边界。root原潜在准入复用，新增日期/必要Evidence/OnlyReport独立通过；不扩其他19材料，不授未披露的训练安全有效性。

窄主题补正的6潜在方向T-SAR13676、MACKO13061、KForge13274、VOLTA12638、PIGEON13207、Beyond13630：完整题摘、理由、当前修订信号与逐ID日期原字段在[增量包](../_sources/daily-20251119/NARROW_TAIL_CALIBRATION.md)。root已实际读8份exact-v1题摘并通过这6方向潜在准入及FLOWER/Fuse两项关闭；API/abs/DataCite有限恢复仍不能认证首次公开，同样以对应exact-v1实际公告/可靠上下界为最小请求，隔离不正面采用/Books/无遗漏，不因日期改判排除。VOLTA v2上界跨截止不反证窗外；Fuse晚v2未见明示纠错/撤回，版本差异不自动证明旧稿错误，未来叙事/数字不反填。此次不扩大这些日期保留项的全实验/owner。

[TDD+CI12823v1](https://arxiv.org/html/2511.12823v1)完整题摘及§3–6已由root实际核，原成熟组合关闭未通过，现作为第18篇潜在论文日期隔离。测试/编译反馈及跨语种收益依模型改变可能修正小模型推理预算选择；98%是best20B/best120B结果比值，不是绝对准确率。公开单测、隐藏评测、至多五次修复、单函数任务限制和无matched端到端预算保留，不授普遍替代或资源节省。没有有效首公开下界，Submitted不认证public；最小请求为exact-v1实际官方公告/完全落窗可靠上下界，只有日期材料到达才重开适用Evidence/owner，不扩全附件，不授当前Evidence/Books。

## 6. 复核

复核者：root（非作者，日级检查时间2026-10-04T17:25:31+08:00）。Codex/Ohm本次仅指定来源补检与获授权同步，不是日级复核者；作者Dalton不自审。

结论：通过

仅Codex官方RSS新增日期证据定点重开，root独立协调反馈确认实际核两个guid/pubDate、publication L13–27链接身份、Safety Hub Nov18无TZ冲突、同card L161–207及Ch31 pipeline/trajectory与environment credit正文。5分局部厂商机制披露、必要安全受影响core及OnlyReport0写入独立通过；不认证最早公开、安全有效性或训练替代授权。以下17:25:31通过复用于未变范围，与本次增量共同覆盖当前报告；不重审Gemini/18篇论文保留/其余来源。该反馈接收后按真实时钟2026-10-04T19:39:03+08:00局部同步完成态，机器另核，不代语义。

[DAY_REVIEW](../_sources/daily-20251119/DAY_REVIEW.md)已实际读取：root通读六部分及有限source/query/分页/停止、18篇潜在论文和Codex方向的日期隔离、必要纠错反侧及Books处置，确认没有尚未处理的具名可执行入口。Gemini家族的必要Evidence/OnlyReport复用此前独立通过；Books实际写入0，无POST。7个具名关闭经分层独立核验，Microsoft/NVIDIA合作未在此次复读，不声称全量排除核验。普通待办0；安全终态保留项不授正面Coverage、Evidence、Books、性能/安全保证或无遗漏。下列分批复核中的“日级待验/未通过”仅描述当时时点，现由本次日级通过覆盖。

root实际读11份exact-v1完整题摘及Gemini developer原核心tool/parameter/signature段，准入方向通过。另于2026-10-04T15:53:55+08:00实际核Gemini日期/身份、developer协议、精确两notebook关键cells与Ch75/78及相邻交接，**仅Gemini家族的必要Evidence/OnlyReport通过**，见[非作者审阅](../_sources/daily-20251119/GEMINI_INDEPENDENT_REVIEW.md)。实际Books写入0，无POST。其余日期/证据/Books与日级未通过；代表性排除新增实际范围见下段，不授日级完成。

随后root实际核UI app/Research core/JSON-LD与Ch66，UI准入/日期/官方最小core+OnlyReport通过，同Gemini家族；Codex扰动训练潜在准入通过但日期隔离，见[独立裁决](../_sources/daily-20251119/UI_AND_TRAINING_INDEPENDENT_CALIBRATION.md)。2026-10-04T16:58:50+08:00 root实际核窄主题8份exact-v1完整题摘、FLOWER v1及Fuse current v2，6潜在准入/2代表性关闭通过，未授日期/Evidence/Books或日级，见[窄主题非作者notes](../_sources/daily-20251119/NARROW_TAIL_INDEPENDENT_REVIEW.md)。有限source终态与其余具名负侧仍待日级独立核。本包作者ready只表示有限普通处理已保存，不授独立日级通过；不能把准入方向通过当全量排除核验。

2026-10-04T17:09:58+08:00 root实际新增负侧5项通过：Intuit直接官方core补证（旧WEB_OPENAI_TAIL仅元信息）、Foundry/Rwanda core及Hope/NeuroLex完整题摘。TDD+CI原关闭未通过，root实际v1§3–6后改潜在日期隔离；已同步18篇论文计数及比值/预算限制。此前FLOWER/Fuse关闭可复用，Microsoft/NVIDIA合作此次未复读，不声称全部负侧附件通过。[负侧独立范围](../_sources/daily-20251119/NEGATIVE_INDEPENDENT_REVIEW.md)。Codex/Ohm本次实际补核三来源入口与字段，只此范围，未审其余11来源；最终14来源整体终态与六部分仍交root日级Gate。

2026-10-04T17:40:58+08:00完成态同步后实际V3校验通过；8份作者Markdown的142处本地引用全部存在，恰为六部分、代码围栏及行尾空白检查通过，限定git diff --check无诊断；未跟踪的8份作者Markdown另用no-index检查，无空白诊断（新增文件差异状态1不等于失败）。本轮只同步README开头及§1/5/6、作者停点，不重审附件，不改root独立notes或共享文件，未stage/commit/push。语义通过依据是root DAY_REVIEW及其明确的实际范围，不是机器检查。
