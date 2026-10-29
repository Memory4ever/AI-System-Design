# Daily Research — 2025-09-22

**规范：** V3
**窗口：** 2025-09-21T09:00:00+08:00 ～ 2025-09-22T09:00:00+08:00
**补充窗口：** 2025-09-21 ～ 2025-09-21
**冻结候选日期：** [原档案](../_sources/daily-20250922/baseline-before-supplement-20261012.md)
**窗口说明：** 用户已有Daily增量补查授权；旧窗口/候选/日期/评分及连续§4冻结，新材料仅前一完整BJT自然日，不catchup、不追公开时分秒。
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-24T04:04:47+08:00

## 1. 结论

2026-10-24修复由Goodall唯一作者、McClintock唯一reader负责，记录见[作者日志A1–A3](../_sources/daily-20250922/REPAIR_20261024.md)及[独核R2](../_sources/daily-20250922/REPAIR_REVIEW_20261024.md)。14每日源的未变有界入口/停止与实际限制分层复用，未因周末预判全部来源零事件。旧提交主题112条去重91身份的59P/10C/22R及69精确v1题摘/23必要局部core保持原读层，不是59篇完整证据审阅。

本轮修正的是日期门：Sep21 BJT无常规arXiv公告点；69个已知v1的原始提交均处于Friday14–Monday14 EDT档，最早公告界为Sep23 08:00 BJT，仅排除这些v1公告落补窗，不认证实际公告日或全球首公开。16857/17072/17105三实例已获McClintock有限独核；具名FDP/Roundtable/SaSaSa2VA早稿/代码及RLinf旧release、17057后续修订已有限核对，见A3。Advanced仅年月精度的共同修复复用，不第三GET，不以按日空响应证明零公告或恢复穷尽。新增确定当窗候选0，不给日期资格未定项评分、Evidence或Books采用；McClintock本轮完整DAY见R6，完成保存检查及唯一FINAL链见§6。

原窗口、FSF3.0/Omni两正式家族、日期/各2+2+2=6和连续§4冻结，证据2/2及两处既有Books整合/非writer POST有效复用，新增Books写入0，无共享gap请求。原七风险core、TTS关闭、RS中心争议及旧arXiv/ARE/Terminus保留项不借新窗口重算或迁日；具体原证保留在§4与[原档](../_sources/daily-20250922/SUP_BASELINE_README_20261012.md)。不授全历史Coverage、全部P的Evidence或安全保证。

## 2. 来源覆盖

以下为2026-10-12实际入口/停止的未变有效层，本次复用而非重新请求；本轮只补A2–A3的具体日期门/具名分支。旧请求数量不计为本轮新请求；必要失败响应不删，动态解析错误不伪装外部受阻。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | own Research403；官方RSS1287 item按pubDate转BJT，09-22→09-17邻界未见09-21，停止于有限feed | 已检查 | RSS不证明Research历史全集/未列事件 |
| SRC-ANTHROPIC | own App Router177带publishedOn对象/174唯一slug，09-15两项→09-05在窗前，有限Research目录无09-21 | 已检查 | 不是174正文或全网召回 |
| SRC-GOOGLE-AI | own Sept Blog首12题名09-30→09-11，09-23/19夹窗即停；DeepMind publications/page/2实际30项09-24→09-18夹窗；年级Pubs/Blog page5请求有限恢复 | 受阻 | Pubs2025年级不证明日公开；DeepMind历史Blog页恢复失败，不以当前2026页授历史 |
| SRC-META-AI | own global_search page5 publication实际Nov18→Sep15，ARE09-22→CyberSOC09-15夹窗；不同type分别排序 | 已检查 | 有限publication切片非全Research/Blog史；旧ARE近边日期hold不搬日 |
| SRC-QWEN | own code-only page_config60 ISO对象转BJT，Next09-11→Omni/TTS09-22→ImageEdit09-23，有限目录无09-21 | 已检查 | UTC09-21不等BJT09-21；旧Omni准入/证据复用，不读未来窗外全部Blog |
| SRC-DEEPSEEK | own homepage/updates，09-22 Terminus→08-21相邻，本目录无09-21标签 | 已检查 | date-only语言页不授历史完全落窗；旧修正信号/日期hold保持，不因标签关闭 |
| SRC-MOONSHOT | own Kimi单页Nov07→Sep16→Sep05→更旧，已读可见题名日期，无09-21 | 已检查 | 非全GitHub事件史 |
| SRC-TENCENT-HUNYUAN | own shell/runtime定位实际publicList POST page1 size1000 renderType0，total9/list9且lang=en；日期字段全2026 | 受阻 | 当前EN目录不恢复2025/中文历史；浏览器尝试失败未冒充读页 |
| SRC-ZAI | own首15/page2累计18唯一ID，hasMore true→false；createAt最早12-07T16Z→BJT12-08，显示12-07口径分开；release notes最早09-30 | 受阻 | 两页当前目录非9月历史，未队列化正文 |
| SRC-BYTEDANCE-SEED | own2025 type2 page_token0/count20 actual15/total49，12-24至07-15，非置顶递减段10-23→09-09跨窗即停；type1 total94/next20/hasMoretrue但无数组 | 受阻 | 只处理真实15项，不称49已尽；type1缺sub_article_list不记0论文 |
| SRC-BAIDU-ERNIE | own Blog1/2与2/2共16卡，footer带UTC日期实际读取，PaddleOCR10-16→PLAS09-12→FastDeploy08-14→ERNIE06-30 | 已检查 | 原parser删footer假阴性已修，不是外部缺日期；不授全网 |
| SRC-XIAOMI-MIMO | own Paper8项10-21→09-19→06-04夹窗；Blog15当前题名无日期，more非有效历史链接 | 受阻 | Blog历史日期未恢复；不重读窗外MiMo-Audio或借Sep20覆盖 |
| SRC-MINIMAX | own英文12最早10-27未跨窗；中文13项10-27→01-15有限夹窗；Agent3标题2026-10-08/09-22/09-19 | 已检查 | 中文/Agent历史完整性未知；未把英文首页当09月全集，未借旧page2计新请求 |
| SRC-ARXIV | 复用12分类四主题start0/max100，各33/44/31/4，112条去重91完整题摘及69相关exactv1/23必要局部core；本轮核69原v1提交、三实例日门/具名早稿/后续修订，详见作者A2–A3 | 已检查 | 无常规Sep21BJT公告点仅是有界发现依据，不授14源零事件；既知v1最早公告界晚于补窗，具名站外正文/代码资格另保留。旧日路径400/Advanced空不证明日零或穷尽，未扩月库存/catchup/全文 |

实际入口与停止可复查[own源入口](../_sources/daily-20250922/SUP_SOURCES_FETCH.py)、[arXiv主题/日路径](../_sources/daily-20250922/SUP_ARXIV_FETCH.py)、[Web有限恢复](../_sources/daily-20250922/SUP_WEB_RECOVERY_3.json)、[当前说明轻核](../_sources/daily-20250922/SUP_CURRENT_LIGHT.json)及[独核](../_sources/daily-20250922/SUP_INDEPENDENT_20261011.md)§3–10。173份SUP请求/raw含失败原件，4份Web原返回单列；存在原件不等全文Evidence。Weekly来源未扫描；按需仅已知身份的原HTML/当前说明，未触发发布全仓扫描。

## 3. 候选与判断

FSF 3.0和Omni经root局部独立日期/准入校准后列为本窗2家族。其余潜在贡献/日期缺口不伪装为确定本窗候选。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Frontier Safety Framework 3.0](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf) | 2025-09-22T08:00:00+08:00 | 外部模型放行边界不足覆盖大规模内部ML R&D使用与探索性阈值状态→3.0的内部deployment safety-case审查及无显式misalignment acceptance rule→重考虑使用范围与审批条件；2 + 2 + 2 = 6 | 深入完成 | 整合：root已写并窄修两项限定，James非写入者第二次actual POST通过；PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，Residual Risk Loop两段/末注；不授DAY |
| [Qwen3-Omni](https://qwen.ai/blog?id=qwen3-omni) | 2025-09-22T05:00:00+08:00 | 旧chunk renderer等block-context→主码按时间AR、MTP补同帧残余码、左上下文波形增量解码→区分帧间与帧内等待及首包提交；2 + 2 + 2 = 6 | 深入完成 | 整合：root已写，James非写入者actual POST通过；MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，speech/ARIA前两段及首条末注；不授DAY |

## 4. 证据与知识整合

[DeepSeek Terminus](https://api-docs.deepseek.com/news/news250922/)实际核心说明包括语言混合/random-character正确性与Code/Search Agent改进；[ARE](https://ai.meta.com/research/publications/are-scaling-up-agent-environments-and-evaluations/)完整题摘指出异步环境评价盲区及预算效率取舍。两者都有继续核验理由，但本次事件的完全落窗区间尚未取得，不授候选审阅完成或Books采用，未因“未改通用原则”排除。

### [Frontier Safety Framework 3.0](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf)

原artifact封面为Version3.0/PublishedSeptember22,2025，原Blog meta及JSON-LD发布字段 `2025-09-22T00:00:00+00:00` 对应北京08:00；root已独立核字段及原PDF准入核心，不凭无证据CMS猜测取消。当前3.1不能反推3.0。

作者必要深入范围：§1.6 p7、§3.1 pp12–13、§3.2 pp13–14、§4 p15、§5 p16及harmful manipulation §2.2.3 pp10–11。采用的约束是达到ML R&D CCL后的外部/大规模内部部署须治理职能审查safety case，material update再审；进一步研发与此部署门槛分开。Misalignment仍illustrative，**没有显式risk acceptance criteria**，不能把CoT监测或风险类别变成许可。政策支持规范性公开事实，不证明缓解有效、残余风险为零或已阻断失控；没有实现核验或实验复现。具体机制、反侧、适用性与评分依据见scan末段。

写前实际owner差额：Ch72 Residual Risk Loop已承载部署语境、缓解验证、决策owner及refresh，Run安全论证和CoT sensor分权也已有覆盖；未具体承载内部大规模使用与准入标准的探索性状态。root独核必要原§3–5及owner后，在Meta v2说明后实际补两段及Review notes末注。James第一次非写入者POST发现第一段缺达到ML R&D CCL触发与safety-case material update对象；root只窄修该句后，James第二次重新实际读完整邻接/末注并核精确3.0 §3.1.2，通过。原误范围及修正链保留于FSF_BOOKS_POST.md；两段均区分政策与工程推导，无控制有效性或零风险证明；James未写Books。

RPG、MANZANO、Latent learning、Visual sycophancy、ByteRobust、RLinf、SABER、UniGist等19项精确v1潜在贡献链和查漏新增BiRQ/R2U/Chunk SSL/Visual grounding等见scan。题摘不等于证据审阅；未复现、未核生产实现。RLinf当前官方README记录2025/08已开源，代码release和论文首次公开不能合并；意外读过v1 intro/§2.2，不声称全文审阅。

### [Qwen3-Omni](https://qwen.ai/blog?id=qwen3-omni)

原配置date=2025-09-21T21:00:00.000Z→22日05:00；root已实际读两core与日期对象，见[局部独立准入](../_sources/daily-20250922/INDEPENDENT_QWEN_CALIBRATION.md)。本窗Blog Architecture支持每步一帧、同帧MTP残余码和增量Code2Wav。具名ae5dbf9 PDF及2509.17765v1的§2.1–2.5/pp3–7/Table1–2、必要§5.2质量反侧已实际读，作为后续精确补证，不反推其全部内容截点前公开。旧2503.20215v1 §2.4/Fig4文字只为比较必要定点读：原Flow-Matching DiT/BigVGAN已有chunk streaming与lookahead，不是整句离线。

采用帧间时间AR、帧内固定步AR残余码、左上下文renderer的分工；**MTP不等于未来多帧独立并行**。报告Table2是cold-start theoretical first-packet，音频/视频234/547ms（1并发）增至1172/2284ms（6并发），与正文largely unaffected叙述不一致；RTF<1不免除首包依赖费用。Blog211/507ms协议未给，不混合或取优。硬件、precision、输入输出长度、batch组织、完整SLO与evaluator版本 `Not Disclosed`；没有同配方codec/renderer单因素消融，质量/延迟不能全部归MTP/ConvNet。必要TTS测试若干语言指标不胜对照，不授SOTA/无退化/普遍稳定或生产保证；未核代码、未复现、未试听全部音频。

写前实际Ch24语音差额是同帧fixed-step AR与renderer block-context等待尚未展开，原交错/prefix-rate及RVQ/时间层级区别已存在。root独读精确必要原源、旧v1与owner后，已在reasoning/speech交错后ARIA前自然写两段及Review notes首条。James非写入者actual POST通过：三依赖、旧lookahead合理性、RTF/首包与并发、有限质量/无matchedrenderer对照都被限定，完整邻接/实际末注与Ch23/25承接已核，没有侵占表示或world真值owner。详见OMNI_BOOKS_POST.md，不授DAY，没有修改Books。

本日两正式家族与新增七项必要风险/反侧core的作者工作已做完。[补读记录](../_sources/daily-20250922/RISK_CORE_SUBSET.md)包含Trojan受限classifier、视觉迎合纠正退步、SABER权限/能力代价、RS oracle推导强化假设、latent oracle检索/ICL边界、MatchFix非真总体accuracy及alignment同风险/分布假设。未自授独立Evidence。[Omni实际POST](../_sources/daily-20250922/OMNI_BOOKS_POST.md)及[FSF第二次实际POST](../_sources/daily-20250922/FSF_BOOKS_POST.md)均通过；不把Books写后验收等同全日DAY，不作全日No Change。其余材料的日期/历史目录保留不进入Books，作者未改Books。

## 5. 缺口与下一步

本轮普通研究/新Books写入待办0，McClintock完整DAY R6已通过；作者同步真实完成保存态，再由reader唯一FINAL核其差额。以下为隔离限制，不支持正面Coverage/Evidence/Books或无遗漏断言，旧完成标签不替代本轮验收。

旧59P的贡献潜力与逐ID理由保留于[SUP_SCREEN](../_sources/daily-20250922/SUP_SCREEN_20261012.md)；本轮只排除已知v1常规公告落Sep21，不关闭所有全球首次公开问题、不要求全59Source。已实际核具名16830 FDP项目页（无日级公开字段）、16839 Roundtable后续项目页（404且链接非v1原comments）、16972 SaSaSa2VA官方迁移仓/具名README（有后续内容但无Sep21事件日）。这些具体早稿/代码日期资格不支持当窗候选；若取得相应原历史页面、paper发布或release原公告，定点核身份/完整落窗区间再恢复必要Evidence/owner。新增原件和失败请求已按root窄授持久保存，唯一文件名前缀`REPAIR_EARLY_20261024_in6Fkt_`，实存路径/字节与原请求指纹核验见作者A5，临时原件不删。既有69项可见history无本补窗v2+提交，17057后续limitations是2026事件；不扩所有版本史或假想渠道。其它清楚P没有具体更早正文线索时，不为排除全网首公开无限请求。

原16788/16895/17066/17050/22697等局部误排更正与实际必要读域继续有效，16750具体C保持，不因日期门改回排除；未采用题摘性能数字、未核代码或复现。旧Advanced仅年月参数修复已复用，空响应不证零公告或恢复穷尽。

旧scan中19v1及查漏潜力、ARE/Terminus的原日期口径和有效读层保留，原窗口冻结不搬Sep21；不新增时分秒请求。RLinf八月开源/九月论文/十二月v0.1不能合成一个Sep21事件，旧论文日期资格需原公告或有效联合日才重开。RS原Eq5依赖更强相同条件翻转率，中心保证保持争议；恢复须明确条件或修正证明，不能仅日期恢复采用。FSF/Omni原证/实际Books和非writer POST已解决，未变层无需重审。

来源终态保留：Google Pubs年级日期/DeepMind历史Blog未恢复、Hunyuan当前EN9全2026、ZAI18最早ISO对应BJT12-08、Seed type1 total94但无论文数组、MiMo15 Blog无日期，及OpenAI RSS/Meta类型切片/MiniMax历史完整性限制。现存有限入口与恢复失败均保留；需要Sep21相应历史目录或具名原事件，取得后只重开对应来源。它们不证明零事件、历史全集或无遗漏，未读普通方法不混入这些保留项。

## 6. 复核

复核者：McClintock，非作者Goodall。

结论：通过

[本轮独核R6完整DAY](../_sources/daily-20250922/REPAIR_REVIEW_20261024.md)实际通过，限本次补Sep21的安全终态。R1–R5已实际核三实例S/2025排程L、贡献P与代表EX有效层、69可见history有限复算、具名早稿/代码/修订分支及Seed非漏解析，并核当前两旧Books完整局部/自身注仍保持原采用边界。没有新Source、PRE/写位或Books新写，不继承旧日级完成声明。R6撤回额外复制前置的同时，root另已明确窄授原件copy；作者A5实际完成9文件持久保存，原请求字节/时刻不改，reader最终差额另核该保存事实，不重GET/研究。

旧Cicero[独核§1–13](../_sources/daily-20250922/SUP_INDEPENDENT_20261011.md)的实际题摘/必要core与局部误排更正分层复用；旧root/James日期、两候选Evidence/Books及七风险core独核按未变身份/命题复用，见[原档§6](../_sources/daily-20250922/SUP_BASELINE_README_20261012.md)、[七风险读域](../_sources/daily-20250922/RISK_CORE_SUBSET.md)、[FSF POST](../_sources/daily-20250922/FSF_BOOKS_POST.md)、[Omni POST](../_sources/daily-20250922/OMNI_BOOKS_POST.md)。两候选/旧证据2/2/Books2有效整合，新写0；不授59P完整Evidence或新日级验收。

机器检查：本轮进行中V3、22个本地链接及限定working空白检查已实际通过，原窗口/完整§3/连续§4与运行前快照逐字相同；完成态检查与真实保存读回见作者A6，随后交McClintock唯一有限FINAL，不由作者自授。结构通过不代独立语义验收；不stage/unstage/commit/push，不改共享State/Books/index或其他日期。
