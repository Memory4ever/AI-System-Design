# Daily Research — 2025-09-29

**规范：** V3
**窗口：** 2025-09-28T09:00:00+08:00 ～ 2025-09-29T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T19:57:07+08:00

## 1. 结论

本日确定落窗入选1家族：Instant Checkout/ACP官方Blog发布。原RSS明确`Mon, 29 Sep 2025 00:00:00 GMT`，即本窗尾部29日08:00北京时间；没有具体占位证据，不能仅因午夜否定。GTO、SafeSearch与DeepSeek-V3.2-Exp首公开仍未确证，留§5而不评分/采用。实际已读两份精确v1完整题摘/必要反侧，ACP官方Blog与dated初版规范必要安全语义；正式一项作者侧受影响深入阅读完成，root校准/证据复核已通过。实际Books写入0。

root准入、Books已有覆盖及最终日级复核通过；当前本窗完成，外部保留项继续隔离。[交接](../_sources/daily-20250929/CALIBRATION_HANDOFF.md)给出原字段、实际证据位置、关键冲突和重开条件。没有把本日未确认的论文简单排除为小改进/领域应用。

## 2. 来源覆盖

原请求/执行时间/失败在本日`fetch-log.json`、`focused-fetch.json`、`recovery-log.json`、`date-recovery.json`、`spec-fetch.json`及`checkout-fetch.json`。只授下列真实切片，不承诺全集。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 原news RSS实际解析1247条，本窗pubDate确证ACP Blog一条；官方Blog core由web读取，urllib403保留；关联仓库身份/发布列表/初版spec读取 | 已检查 | Blog发布和后续artifact是分开事件，不把repo时序覆盖RSS；初版spec历史身份边界见§4 |
| SRC-ANTHROPIC | Research Flight实际恢复174出现/172唯一slug，逐原publishedOn筛本窗无记录；搜索触发Consumer Terms原core | 已检查 | 当前Terms页Aug28发布、截止已为Oct8，不能拿旧转载Sep28当新原始发布；不授历史未收录全集 |
| SRC-GOOGLE-AI | `/blog/2025/09/`首12条Sep30～Sep11越窗停；pubs category2025/search language model实际首1～15/37，只是全年发现目录，无目标first-public字段，未转全37正文队列。DeepMind Research gzip实际解压；RSS100条至Nov5 | 受阻 | DeepMind9月历史目录/Google论文首公开未恢复；不是空gzip/零事件 |
| SRC-META-AI | Research标题壳；Blog页1～3原卡实际读，页2非单调旧Feb20未提前停，页3Oct24后普通Aug27、Aug14至Jul31越窗，停止 | 受阻 | Blog有限卡片切片已处理，动态Research历史未恢复，不授Research历史覆盖 |
| SRC-QWEN | 旧Blog5条窗前；新官方Research API本日实际200，完整数组60项，非时间排序全部原date/lastmod检查后停，无本窗项；[原响应](../_sources/daily-20250929/qwen-research-api.json)、[元数据](../_sources/daily-20250929/qwen-research-metadata.json) | 已检查 | 限官方可恢复数组，不授未收录历史修订全集 |
| SRC-DEEPSEEK | 官方news18条目录，Sep29 V3.2-Exp与Sep22夹窗；Sep29原发布core已读，DSA替代机制有潜力 | 受阻 | 日精度未定时区/时刻，不能确定是否在本窗最后1小时；不以降价代替机制贡献 |
| SRC-MOONSHOT | 官方Blog26条实际可见目录，Sep16/Sep5至2024均已读标题日期，无本窗条目 | 已检查 | 限Blog目录，不授所有仓库临时事件 |
| SRC-TENCENT-HUNYUAN | 首Research页壳；正确publicList POST 1/100/renderType0实际total9/list9，displayPublishTime全部2026 | 受阻 | 当前9条不能覆盖2025；无可见浏览器可用，不授历史0 |
| SRC-ZAI | Research blogsItems页1 15/页2 18，页2hasMore=false，最早Dec7；release notes Sep30/Aug11夹窗 | 受阻 | 当前Research截断不能授9月全集；notes所列切片已读 |
| SRC-BYTEDANCE-SEED | type2/year2025/page0/count20真实15/total49/moretrue/next20，分离置顶后普通条目越7月停止；type1前页US/CN94均无list；真实page20只Jun12 SwiftSpec | 受阻 | 缺前页内容，不以一个后页补授9月论文覆盖；Blog有限段已读 |
| SRC-BAIDU-ERNIE | 首猜rss.xml404后实际index.xml恢复18项并解析（16普通+2导航），Oct16/Sep12夹窗，无本窗字段 | 已检查 | 已恢复路径，不把最初404当终态历史空 |
| SRC-XIAOMI-MIMO | 官方首页、两实际JS、原route metadata读8论文/15Blog；论文Sep19/Oct21夹窗，Blog日期可见Dec18/19和2026；More本地展开 | 已检查 | 不授当前目录之外历史全集，无窗内身份 |
| SRC-MINIMAX | EN12/CN13技术卡实际读，无分页；本日另实际Agent Tech Blog及llms.txt全部索引，仅恢复2026-05-13 Agent Team，无历史分页，停；[文本](../_sources/daily-20250929/minimax-agent-text.json)、[索引](../_sources/daily-20250929/minimax-agent-index.txt) | 受阻 | 当前精选公司列表/Agent2026目录不授完整9月 |
| SRC-ARXIV | 12分类/10主题题名，submitted发现Sep25 18UTC～Sep26 18UTC/start0/max100返回429；旧2509月路404保留。正确 `/list/cs.CL/2025-09?skip=0&show=2000` 实际200，1–2000/2214无逐篇公告日期，只定点查GTO身份，不转全月题摘队列；[恢复](../_sources/daily-20250929/narrow-route-recovery.json)、[原月表](../_sources/daily-20250929/arxiv-month-corrected.html)。公告机制/两必要v1已读 | 受阻 | 未取得目标逐篇历史首公开，月表末214未读、不授全量；不从提交时间直接推公开日 |
| 表外：[ACP官方规范](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol) | 只读本次触发的README身份、releases（空）、2025-09-29初版changelog与checkout/delegate payment规范，不扩当前RFC全集 | 受阻 | 初版日期标签不等于原公开时刻；现存dated规范未冒充当时执行日志 |
| 补检：[Web主题搜索](https://www.google.com/) | Sep28机构/有界Sep26模型推理与RL/arXiv公告恢复；原search与focused-web保留，回原v1核身份 | 检索受限 | 二手security数据库Sep28只作SafeSearch发现；转载周报不授新研究日期或贡献 |

## 3. 候选与判断

确定落窗1家族，root准入、证据与Books裁决通过；三项论文/模型日期潜力隔离于§5。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/) | 2025-09-29T08:00:00+08:00 | 语言提案不能直接支配支付凭据→用户确认、限定金额/merchant的payment token与merchant-of-record分责→重新考虑执行授权和凭据转交范围；2+2+2=6 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)实际金额/资源/时间窗口校验与payment approval/narrow scope；root裁定通过 |

## 4. 证据与知识整合

### [Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/)

日期依据为本日原官方RSS，保留原`Mon, 29 Sep 2025 00:00:00 GMT`，没有推造时刻或时区。关联repo创建于04:09:29UTC，仅约束artifact事件，不能反证Blog00UTC发布；本次只采用Blog发布事件，不把仓库创建当首公开。官方Blog How Instant Checkout works/The Agentic Commerce Protocol/Built for trust明确用户确认、merchant负责订单/支付/履约及金额/merchant限定token。2+2+2只给这一授权/委托边界命题，不给用户数、厂商名、销量或新标准名加分。

为核必要安全语义读current main下dated`spec/2025-09-29`初版checkout/delegate payment规范及changelog：前者complete成功须创建order/进入completed，已完成不可cancel；后者Allowance将one_time、max_amount/currency、checkout_session_id、merchant_id、expires_at组合。Idempotency-Key与参数冲突说明不等于跨PSP exactly-once，也未取得历史commit对应/实际执行日志。因此这些schema只作机制解释与未证明边界，不把后来新增版本倒填当时，生产安全/吞吐均未披露/未验证。

Books已有覆盖而非因“小改进”拒绝：本次实际读取Ch78 Tool Contract行37～55拥有side-effect class/authorization/idempotency，行88明确金额、目标资源、环境、时间窗口和真实principal校验，Side Effects表行337～339已有payment→approval/strong idempotency/narrow scope，行642～648拥有opaque token的byte integrity/scope/expiry与runtime原样传递。相邻Ch77管理persisted state不授权，Ch79 plan是可验证假设；Ch83行187～211区分delegation provenance与真实effect receipt。Blog是这些责任分离的产品协议实例，未给可修正其条件的新实证；No Change已由root实际独核裁定，作者未改Books。

两份v1未决材料必要阅读详细位置见交接，未声称实现已运行或实验已复现。

GTO `2509.22134v1` §3.1/Appendix A有具体理论冲突：正文Theorem 1把reward增加写成温度0时接受长度必增；附录却要求超过smooth-max slack，并在Remarks承认提高非最大分支可不改最大值。§3中连续期望接受长度与附录离散长度对象亦不能无声等同。保留其树策略目标、batch1 A100下EAGLE-3局部增益潜力，不采用无条件保证。

SafeSearch `2509.23694v1`实际§3.1～3.4、§4.1～4.2、Appendix B/E.2读到：首轮混入至多一个固定、query相关且agent无关网站；300筛选病例/五风险各60，三次采样，最终响应LLM judge；提示reminder未消除污染，过滤有44.2% recall和stealth限制。商业deep-research内部实现未测、仅Google搜索、端到端成本未纳入。因此该反证不是“所有联网产品ASR90.5%”或“多搜索必安全”。

ACP初版采用显式用户确认、merchant-of-record边界、一次性allowance（金额/币种/checkout/merchant/expiry）与complete/cancel状态、Idempotency-Key，有Agent执行授权范围潜力；原Blog不是可靠性复现，schema不证明真实PSP执行一次性约束。Terms补检则是Aug28已公布的厂商保留策略，当前页截止Oct8；不把转载Sep28当本窗新约束发布。

## 5. 缺口与下一步

可执行普通待办0；独立复核通过。以下为本窗终态保留，不用于正面证据、Books或Coverage/无遗漏断言，日期未确证不评分；只在具名材料到达时定点重开。

- [GTO精确v1](https://arxiv.org/abs/2509.22134v1)：原submitted `Fri, 26 Sep 2025 09:55:35 UTC`，尚缺首公开官方公告/完全落窗的原公开区间。重开本家族日期及上述理论争议，不把7.7%小增益机械排除；若归属成立再独立校准评分/采用边界，关键反侧已读。
- [SafeSearch精确v1](https://arxiv.org/abs/2509.23694v1)：原submitted `Sun, 28 Sep 2025 07:05:17 UTC`，二手数据库称Sep28，不能代官方公开。需要可追溯首发布/公告区间；不拿之后v6标题/实验补v1。必要安全反侧已读，之后只重开日期/受影响命题。
- ACP artifact边界：官方repo `created_at=2025-09-29T04:09:29Z`、releases空；dated初版spec尚未绑定历史commit。本窗Blog日期已按原RSS确证，不能仅午夜留hold。只有需采用当时精确schema/实现事实时，再以历史commit/原发布record定点恢复artifact事件，不阻塞Blog可支持的有限结论。
- [DeepSeek-V3.2-Exp](https://api-docs.deepseek.com/news/news250929)：原目录Sep29日精度与core有DSA潜力，缺时区/具体事件区间。需要官方原公开记录确定本窗尾小时还是之后；价格不是速度/架构收益证据，若确证再读所需技术报告及校准。

机构历史切片和arXiv请求限制按§2具名原文件作本窗终态保留；可接受恢复是官方历史目录/真实缺失API前页/首次公告，不是当前主页空壳、DataCite注册或submitted。正确月表1–2000/2214已取得但只是身份线索，不造逐篇公开或全文已读；只窄补受影响源与窗口，不扩9月29日09:00之后、Weekly或别月。

## 6. 复核

复核者：root（非报告作者）。

结论：通过

实际重开官方ACP Blog核心与本日原RSS，确认00GMT落窗，不拿后续repo创建时间否定Blog。核Ch78 typed contract、真实principal/金额资源时间校验、payment approval与opaque token范围，已有覆盖成立；6分只评具体委托边界，安全发布约束按受影响深入审阅，现存dated spec不冒充历史commit/真实PSP日志。Books不新增产品摘要。

定点核GTO精确v1 Appendix A smooth-max slack与Remarks，不把reward上升等同最大分支升；SafeSearch精确v1 E.2不测商用内部、只Google/300病例/成本遗漏，结合已读threat与300筛选分母保留局部反证。三日期潜力不评分不采用；Terms原Aug28不是转载Sep28的新事件。14源参数、月份身份补检停止与六部分已核，原始索引之外未宣称全量召回。普通待办0；外部缺口不作正面Evidence/Coverage或无遗漏。

本日V3一致性校验与本地引用/围栏/限定diff-check通过，不代替语义验收。共享Books/索引/LEARNING_STATE未改，未stage、commit、push。
