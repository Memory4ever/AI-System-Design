# Daily Research — 2025-10-08

**规范：** V3
**窗口：** 2025-10-07T09:00:00+08:00 ～ 2025-10-08T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T05:13:03+08:00

## 1. 结论

本日确认候选1个家族（Gemini Computer Use），必要安全核心深入完成1、仅报告1；Books提案0、实际写入0。Peirce FIRST及FINAL窄修写后DAY均实际通过，普通研究/复核待办0。采用范围是当前官方发布说明中的模型动作提议、模型外逐动作检查、用户确认与客户端执行分工，不是安全效果或2025精确API保证。OpenAI 10/07主发布core新增贡献已关闭，区别于10/01七个案例页事件，不称整PDF已审或同事件重复。日期不明及历史目录缺段作为终态保留项，不等零事件或完整覆盖。

## 2. 来源覆盖

原件及真实下载时间见[日级目录](../_sources/daily-20251008/fetch_manifest.json)和[定点恢复记录](../_sources/daily-20251008/recovery_manifest.json)。保存原件不等于读过全部内容；恢复判断与分页边界见[必要笔记](../_sources/daily-20251008/AUTHOR_CLOSEOUT.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 网页工具可读、直连403；官方 RSS 按本窗筛日期，10-07 03:00 GMT主发布页；发布core已读，必要安全/纠错命题及Peirce核查有界复用 | 已检查 | 仅关闭主发布core新增贡献；整PDF历史首次公开/当时字节未确定，不声称全PDF已审或全站召回 |
| SRC-ANTHROPIC | Research 原始SSR含 publishedOn；从本窗两侧 Petri 10-06 11:10Z 到 small-samples-poison 10-09 13:50Z 的日期区段，无本窗记录 | 已检查 | 仅当前官方目录，不证明全部历史事件 |
| SRC-GOOGLE-AI | DeepMind Research首查；pubs原`?year=2025`实际忽略该过滤，定点恢复`?category=2025&search=language%20model`，真实2025主题结果1–15/37，停止首15标题线索，不将全年条目变队列；原Blog `/2025/10/`及`?page=2`到2/2，10-07 S2R→10-09 XR Blocks；独立Computer Use、S2R core | 受阻 | Blog不是pubs替代；年级主题目录无本窗公开时间，不能证明日级完整；S2R仅10-07日名，无时区/完整落窗bounds |
| SRC-META-AI | 官方Research返回品牌外壳；一次官方域名10-07研究补检 | 受阻 | 未取得本窗历史条目，搜索无命中不证明无事件 |
| SRC-QWEN | GitHub官方博客第1页最新09-23，迁站后实际访问qwen.ai/research，官方域名10-07补检 | 受阻 | 新站返回应用外壳而非本窗历史目录；旧页停止于第1页，未向旧年代扩扫 |
| SRC-DEEPSEEK | 主页首查后实际恢复`/news/`独立Research；读可见10研究条目的日期/标题，10-21 OCR→05-14 V3研究，以及动态09-29→12-01，停止可见列表 | 已检查 | 当前列表未显示本窗记录；“查看全部”未取得独立历史分页，不外推全部repo或互联网无事件 |
| SRC-MOONSHOT | Platform Blog第1页及MoonshotAI组织页；只检查可见日期与入口 | 受阻 | 当前页不能重建本窗研究/版本历史 |
| SRC-TENCENT-HUNYUAN | Research首查为动态外壳；browser首次超时，有限重试返回子线程不支持IAB visibility；从官方bundle恢复`https://api.hunyuan.tencent.com/api/blog/publicList`，POST pageNum1/pageSize100/renderType0，11条全返回 | 受阻 | 当前全部目录11条均为2026新站内容，不能替代2025历史；origin错误404已用真实API修正 |
| SRC-ZAI | Research首查后读本日bundle的LoadMore `page`参数，实际`?page=2`累计18条，末项2025-12-07并明确“没有更多”；release notes独立日期跨09-30至12月 | 受阻 | 已消除普通分页待办，但Research当前终页仍无2025-10历史段；release notes不替代论文目录 |
| SRC-BYTEDANCE-SEED | Research/Papers首查；本日官方bundle和`get_article_list_v2`，2025/asc/type1/count20，加`x-tt-locale: US`实际token0/20/40/60/80，末页has_more=false,total94；只浏览日期/标题以定位本窗。type2实际0/20/40终页 | 已检查 | 目录相邻09-22 MEF/ByteWrist与10-09 Function Tokens，无10-07/08日名；日期值不冒称精确first-public，不将全年题摘变队列 |
| SRC-BAIDU-ERNIE | 官方中文博客两页均读日期，终页最早06-30；本窗两侧PLAS09-12、PaddleOCR-VL10-16 | 已检查 | 只限博客目录，不外推所有repo事件 |
| SRC-XIAOMI-MIMO | Paper全8项日期浏览；本窗两侧Audio09-19、MoE RL10-21；Blog可见15项 | 受阻 | More不是历史分页证明，Blog更早段未恢复 |
| SRC-MINIMAX | 英/中文Blog当前首屏及独立Agent Tech Blog；中文最早01-15、M2为10-27；Agent当前仅2026-05-13 | 受阻 | 当前目录不能证明历史无事件，Agent历史缺段独立保留 |
| SRC-ARXIV | 旧查询原响应与[四主线有界补检](../_sources/daily-20251008/arxiv_topic_bounded.json)保留；旧手拼编码使上界只剩10位，是请求错误，不是服务无端重写。R-ARXIV使用urlencode重新请求cs.CL/cs.LG、transformer、submittedDate:[202510060000 TO 202510072359]，start0/max20、ascending，HTTP200；[真实请求与范围](../_sources/daily-20251008/arxiv_corrected_request.json)及[原Atom](../_sources/daily-20251008/arxiv_corrected_max20.xml)：total72、返回20，字段范围10-06 01:08:34Z～16:19:57Z，停止此页 | 受阻 | 正确请求已恢复，首20/72为截断提交线索，不是本窗公开事件分母；官方first-public时刻/完全落窗bounds仍未取得，不授日级覆盖，不扩库存全文队列 |

按需来源：未发现需要本日扫描的独立发布批次；不扫描每周来源。Gemini原始card和评价说明仅为定点证据恢复，不扩来源扫描。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Gemini 2.5 Computer Use](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/) | 2025-10-08T03:00:00+08:00 | 既有执行器权限/approval仍需保留 → 当前官方明确模型外逐动作检查、确认与客户端执行分工 → 重核产品控制契约及风险边界；2+2+2=6，经FIRST校准 | 深入完成 | 仅报告：具体产品发布控制分工，无可验证长期安全保证或超出现有owner论点的差额；Peirce实际FINAL通过 |

## 4. 证据与知识整合

### [Gemini 2.5 Computer Use](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/)

原件`gemini_release.html` JSON-LD datePublished为2025-10-07T19:00:00+00:00，dateModified为2026-01-07T18:57:02.363124+00:00。采用精确边界是“当前官方对该产品发布的说明明确区分模型动作提议、模型外逐动作安全检查、用户确认与客户端执行”。作者在FIRST通过后读回How it works及How we approached safety，以及当前card物理p4–5 Known Limitations / Ethics and Safety / Additional Risks & Mitigations；[Peirce独立结果](../_sources/daily-20251008/FIRST_INDEPENDENT_REVIEW.md)已核同一必要安全内容，可复用，非最终DAY。

输入为用户请求、截图和动作历史；模型提议function call，客户端执行后回传截图/URL。发布说明中的模型外inference-time服务在执行前检查每个提议动作，但这不是证明所有动作fail-closed或reference monitor完备。Card保留不可信网页prompt injection、误解意图、不可逆错误动作/数据外泄与敏感或有害输出风险；要求确认时开发者不得绕过确认。训练内拒绝/确认、推理期monitor/filter与客户端权限仍是不同责任。卡片未披露这些控制的完备性、误判率或生产风险消除量化证据；未进入Frontier Safety Framework评估范围不是“通过安全测试”。不采用跨harness性能排序，故不为此扩读性能附件。

当前card标题含updated2且保留October7发布标签，不称取得不可变2025原始字节。当前开发文档已是Gemini3.x：不借其`safety_decision`、字段或默认行为补证2025精确接口。本日正面结论仅是当前官方对发布产品的控制分工说明，历史字段/接口行为和安全效果不获采用。

实际读回owner `PLATFORM-SECURITY`：[Ch72 Learned Security Sensor 与 Reference Monitor 必须分层](../../../../books/part-06-ai-infrastructure/72-security.md#learned-security-sensor-与-reference-monitor-必须分层)正文，已有“模型侧sensor提出风险、versioned policy解释证据、独立output/action gate enforce”，monitor安全判断不能授工具权限。邻接`AGENT-TOOL-CALLING`：[Ch78 Side-effect Class](../../../../books/part-07-agent/78-tool-calling.md#side-effect-class-决定控制)明确irreversible/high-impact使用approval、strong idempotency、narrow scope，且只读也可能泄露。本次发布具体实例值得保留，但未证明新的授权机制或可泛化安全保证，不能改变上述长期论证；处置仅报告，Books No Change，0提案/0写入，不以“主题已有覆盖”取消候选或降低6分。

### 必要安全/纠错线索：OpenAI October threat report

官方RSS区分10/01七个案例页发布（00:00 GMT，BJT08:00）与本窗10/07主报告发布页（03:00 GMT，BJT11:00），同一家族不同页面事件；不能将前者当整PDF最早公开，亦不自动称后者同事件重复。主发布core仅概括季度案例、已有攻击流程提效、未观察到新攻击能力、账户处置与合作，没有相对已读case最小命题的新机制/评价纠错，关闭范围仅为该core新增贡献判断，不新增候选/不重复评分。

必要反侧有界复用01已读Russian/Stop News命题及Peirce实际核查：Russian构件可能组合、模型未执行工具、无法验证平台外活动，与未观察到超公开资源的新能力同存；Stop News疑似虚构合作证据使Category3修正为2。不能以普通案例增长忽略纠错，也不称完整攻击成功。没有无差别重读37页PDF，主发布关闭不代表整PDF已审。当前[PDF](https://cdn.openai.com/threat-intelligence-reports/7d662b68-952f-4dfd-a2f2-fe55b041cc4a/disrupting-malicious-uses-of-ai-october-2025.pdf)的Last-Modified为2025-10-08T03:03:09 GMT（BJT11:03:09，窗后），只证明当前对象修改标签；不是first-public、首次上传或重要修订。整报告历史首公开与当时PDF字节未确定，不用作本日历史事实或Books证据。该未采用命题不阻塞core关闭；若将来依赖它才定点恢复历史原件/官方说明。

## 5. 缺口与下一步

普通研究待办0、独立复核待办0、Books待写0。Peirce FINAL §6已实际解析正确请求/原Atom并核终态措辞，R-ARXIV写后窄复查DAY通过；复用有效FIRST/FINAL，不重复全附件。作者只据实际非作者结论同步完成态，没有自审；共享Books/index/state未修改。

本窗终态保留项：来源表受阻项不支持正面证据、Books、无事件、无遗漏或覆盖通过。Qwen新站/Meta/Moonshot历史目录、Z.ai实际终页仍缺10月段、MiMo Blog更早段、MiniMax Agent仅2026条目、混元新目录无2025段，各需原站含本窗历史列表/精确事件重开；Google pubs需本窗公开日期；arXiv正确12位范围请求已恢复，仍需具名材料的官方first-public公告/完全落窗bounds，不将submitted或截断返回当公开覆盖。Seed type1与DeepSeek实际Research的普通恢复已处理，不再写缺列表/主页hold。精确入口、失败、停止均保留在来源表与原件，未将宽库存变全文队列。

外部保留线索：[VecInfer 2510.06175](https://arxiv.org/abs/2510.06175)只取得submitted线索及题摘，量化机制可能有增量，待官方first-public公告完全落窗；[S2R](https://research.google/blog/speech-to-retrieval-s2r-a-new-approach-to-voice-search/)官方core为双encoder绕过ASR中间文本、WER与下游MRR不等价的局部证据，仅日名10-07不足落窗，待官方时区/时刻或完全落窗公开bounds。均不作为正面证据、Books或零遗漏依据。

## 6. 复核

复核者：Peirce（非作者）

结论：通过

Peirce [FINAL](../_sources/daily-20251008/FINAL_INDEPENDENT_REVIEW.md) §2–4实际通过Gemini必要Evidence/6分/仅报告Books理由，核OpenAI页面事件与core关闭、十四有限来源及必要/分层反侧；§6实际独立解析正确编码max20请求与原Atom、核total72/20及范围，R-ARXIV写后DAY通过，替代初轮未通过。作者据此同步，未扩大其有限覆盖或保留项权限。V3结构检查通过；保存raw和机器检查不替代语义验收。
