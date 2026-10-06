# 2025-11-25 续跑查询与停点

执行日期：2026-10-04，BJT15:01之后。本文件只补充本日真实调用，不授覆盖或独立校准。

## 原始调用

web调用一次包含以下open（各第一页，无click分页）和search（各结果第一页，response_length=long）；输出原样在raw-source-boundaries.json：

- open https://docs.z.ai/release-notes/new-released
- open https://agent.minimax.io/docs/techblog
- open https://arxiv.org/list/cs.CL/2025-11?show=25 —— Internal Error，停止；此前show2000超时等已在首批包保留，不循环失败入口。
- search query=`site:ai.meta.com "November 24, 2025"`
- search query=`site:research.google/blog "November 24, 2025"`
- search query=`site:deepmind.google "24 November 2025"`

之后仅为上述已知原页补读核心，open（同次调用response_length=long，原始输出raw-boundary-core.json）：

- https://docs.z.ai/release-notes/new-released lineno=75；读到165行末，可见December08→September30；没有November24目录条目。不读窗外机制正文。
- https://agent.minimax.io/docs/techblog lineno=0；只15行导航，无历史技术条目，不作零命中。
- https://ai.meta.com/blog/segment-anything-conservation-x-wildlife-monitoring/ lineno=20；实际核心L48～88。范围外科学应用/无新机制，贡献关闭见FIRST_CALIBRATION.md，日期恢复停止。

Rynn完整v1补读：open https://arxiv.org/abs/2511.17502v1 response_length=long，raw-rynn-v1.json。未点全文、未读v3正文。

## 有效主题查询与无效探针

四个有效的窄主题API完整query/url/start/max_results/排序/returned_query/执行时间/返回条目/stop均在 arxiv-{model,systems,agents,multimodal}-query.json；原Atom在对应page0.xml。当前复算30+7+38+34=109返回，去版本身份去重88。全为提交时间发现线索，不是公告证明或88全文队列。

早期无效CLI探针未保存原始返回文件，只有会话输出与校准包所记失败性质；不用于任何覆盖或候选判断，也不补造旧query。宽月表仅保存标题线索，未转题摘队列。本窗相关官方公告标题切片尚未成功恢复，仍普通有限恢复待办；必要目录长期不可得后须独立确认隔离，而不是随意算已检查。

## 可执行停点

首批准入待root独立校准，已通知文件路径。本报告尚未冻结候选/完成证据/完成Books。校准前只继续无关来源初筛和这些精确材料日期恢复；不把准入理由借成熟原则加分，也不把名称缺位当长期Books缺口。原页、原始日期和访问失败均保留，日期请求只指向首批包具名材料。

## 恢复更新与有限停止（2026-10-04T16:21:09+08:00）

上段为15:01停点，不覆盖新进展。root首批校准已回，Opus必要证据/Ch66窄整合及作者非写入者POST实际通过，记录见OPUS_EVIDENCE_OWNER_REVIEW.md末段。工具release单项在TOOL_RELEASE_EVIDENCE_OWNER.md，AMD日期+必要限定在SYSTEMS_CALIBRATION_TAIL.md，安全追加事件在SECURITY_EVENT_CALIBRATION.md；已发送文件路径，后两项仍待独立校准。不等待整日池才送单项。

补充调用raw-resume-official-slice12.json至raw-tail-controls24.json各自保留实际request与response。四项系统尾部是窄主题相关查漏，不把88个标题变逐项题摘/全文队列。fetch_tail_dates.py只取4个具名DOI，原日期与receipt分别保存；submitted/Updated/created保持不同权限。

Z.ai恢复：本日实际GET native-zai-research.html 1276425bytes；JSON解码Next flight得nextPage=2/hasMore=true。仅读取页面引用的研究chunk `/_next/static/chunks/app/(frontend)/%5Blocale%5D/(routes)/research/page-dbb507db4bffb18e.js`，HTTP200/18362bytes；真实handler用URLSearchParams设置page再router.push，不再猜分页身份。实际GET `https://www.zhipuai.cn/zh/research?page=2` HTTP200/1397496bytes，保存native-zai-page2.html。第二页RSC含长度标记T文本，按UTF8字节长度跳过该文本再JSON.parse元数据，不能把按换行初次仅5个nav记录当全部。实际13个JSON记录、1个text frame跳过、跨nav/blog去重18个id；第二页blogs含此前16项加GLM-4.6V/GLM-4.7，nextPage=3/hasMore=false。当前目录最早Dec7/8，尚无11月旧切片；当前18项不是18篇题摘或全文审阅。历史11月覆盖仍隔离，恢复条件为旧官方目标段/具名事件。

Anthropic本日独立GET native-research-resume.html 279365bytes，实际解码publishedOn邻接Nov25 11:05Z/Nov24 15:10Z/Nov21/Dec1；没有复用30的Coverage。Nov24 prompt-injection目标事件追加校准；Nov25 11:05Z在本窗终点后只作下一日线索，本日不审其贡献。DeepSeek实际GET native-deepseek-updates.html 48079bytes，标题日期Dec1→Sep29且无Next；ERNIE实际page2六条Nov11→June30、无Next；DeepMind两页共48标题仅相关四条定点核原日期均窗外，raw-final-source-boundaries14.json、raw-neighbor-dates-and-catalog19.json、raw-google-neighbor-dates20.json保留查询停止。不因当前无项给删除库存保证。

已触发按需SRC-OPENREVIEW：MURMUR具名forum wwXP9eqWeW及API2 notes请求，HTTP403见murmur-openreview-receipt.json；只核本项日期/版本，没有扫描会议。现有日期保留项均已有限尝试：作者公告/项目、具名API/元数据及官方列表有界路径；未得完全落窗范围不正面采用，不以常规schedule造精确时刻。不再重复空路径。

作者收束交付：正式README当前2个确定落窗拟家族（Opus/AMD），作者普通扫描与必要审阅0，独立追加AMD/browser与日级仍待。root工具机制/OnlyReport通过，独立19Z工具事件不通过；已撤回该推定，工具仅Opus关联背景，不计family/评分。十项潜在论文、政治纠错及历史目录限制在§5逐项隔离，重开精确。最新V3通过不授日级完成。随后按fresh合同接11/26，不等待25独立复核。共享Books/state/index未写。

## 日级来源表定点返修

按root反馈，实际重读本日raw-native-1.json中Moonshot原列表L0～108：带日期文章标题链接0～25，共26篇；L108的26/27是用户中心及文档导航。撤回28文章的误计，正式行同步26，不借其他日报计数，不重读窗外正文。Google行的博客有限检查有效，但必要pubs历史日切片仍受阻，所以整组结果改为受阻，未将博客检查授予pubs覆盖。此处只是两行返修；政治纠错受影响原源和整日Gate仍由root独立核，不自授25完成。

随后实际读取root的TAIL_INDEPENDENT_REVIEW.md。原query首条Quantum Fourier Transform Based Kernel for Solar Irrandiance Forecasting不能因词面不含Transformer就判API故障；关键词/可能词干匹配只负责发现，不认证ROADMAP主题语义。109返回/88身份只报发现规模，未全范围筛选/未全题摘，返回published在请求提交区间的权限仍保留，但不等于公告公开。正式§1/2同步此限定，不新增失败探针、不换日期池、不扩88全题摘。尾部受影响安全/更正及代表性关闭的root实际范围同步§6；仍无作者日级完成授权。

## 完成态交付检查

实际读取root DAY_REVIEW.md后按授权同步README状态完成、普通0及§6独立通过；保留root实际Ch66一段/末注、Aristotle非写入者POST和所有外部终态隔离。完成态V3首次因“结论：通过”后同行解释不被当前接口识别而失败，只改为独立字段行，未改校验器或语义结论，随后重跑通过。实际逐文件检查本日13份Markdown、39个本地引用与行尾空白，问题0；本日限定git diff --check无输出，新目录untracked已另按文件字节检查。未stage、commit、push；root可核最终文件并计数。作者继续独立26，不扩公共合同/其他月/Books。
