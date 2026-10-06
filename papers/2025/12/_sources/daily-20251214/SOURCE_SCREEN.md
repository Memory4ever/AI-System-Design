# 12/14 原始来源与作者停点

作者Gibbs；窗口 `[2025-12-13T09:00:00+08:00,2025-12-14T09:00:00+08:00)`，实际2026-10-02执行，首访20:15:42+08。当前合同独立重读；修04/07/08普通差额后恢复时再次加载，不继承邻日报结论。首批题摘与校准请求见[ADMISSION_CALIBRATION](ADMISSION_CALIBRATION.md)。本文件只记必要观察，不抄整页或内部工具引用。

## 官方来源实际范围

- OpenAI：Research当前首屏仅2026，不能证明历史。原生[RSS](https://openai.com/news/rss.xml)实际HTTP200，XML解析12月邻接：Dec12 `00:00:00 GMT` 的BBVA、Codex/Sora Android、BNY；后邻Dec16 `00:00 GMT` Images1.5，另science08/09GMT。该Feed段未见Dec13–14项，不授整个机构零事件；午夜字段保留原精度。
- Anthropic：[Research](https://www.anthropic.com/research)实际原生317670字符，内嵌publicationList所见 `publishedOn=2025-12-04T17:00:00.000Z` interviewer → `2025-12-18T10:33:00.000Z` project-vend-2 → Dec19 bloom。图像_createdAt/_updatedAt非文章公开。该明确邻接排除本窗所列目录事件，不授全部机构召回。
- Google Research：原先只有[2025 Blog](https://research.google/blog/2025/)的Dec18年终/Dec15 Paper Assistant/Dec12 Health/Dec10 DP邻接，**不能代替pubs覆盖**，原该层声明撤销。2026-10-02本次实际补原[pubs](https://research.google/pubs/)HTTP200，默认772页；核原官方JS filter生成规则后实际正确请求[category=2025](https://research.google/pubs/?category=2025)，checkbox已checked、45页、首页15条，只做过滤/字段检查，不读45页库存。原`year=2025`不选2025的错误尝试仅复用Mill观察，不授覆盖。实际有限查询[language model December13](https://research.google/pubs/?category=2025&search=language+model+December+13+2025)与[training/inference/multimodal/agent December14](https://research.google/pubs/?category=2025&search=training+inference+multimodal+agent+December+14+2025)，均HTTP200、2025 checked、0行、无下一页；它们是文本搜索而非日日期过滤，不能授空日。pubs本窗历史公开段仍外部终态保留，需要原始相邻历史记录/具名first-public；不再从Blog授pubs已检查通过。DeepMind第4页及四个固定个体层未变化：Gemini audio原datePublished=2025-12-12T17:00:00+00:00早于窗，FACTS Dec9、Scope2 Dec19、[Flash](https://blog.google/products-and-platforms/products/gemini/gemini-3-flash/) Dec17；月标/model-card Updated不授日。
- Meta：首访错误`/blog/?page=4`所得July2025不是正确历史论文段，未算覆盖。修正至[Publications page4](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=4)，原生287708字符，实际Dec16 audiovisual correspondence → Dec12 Text-Guided Semantic Image Encoder → Dec1 RIFL → Nov19 SAM3。仅用本窗邻接，不把收录日期授论文首公开。
- Qwen：旧站Sep23停点与新[Blog](https://qwen.ai/blog)92469字符仅Qwen skeleton，不能恢复2025目录。窗口限定官方域辅助查询未返回项；上述有限替代未恢复历史目录，现为外部终态保留，需原始2025列表/具名事件才能定点重开，不据空页记零。
- DeepSeek：`/news/news251201`再次是Your First API Call错页，V3.2仓库路径转Exp不是历史说明。正确[Change Log](https://api-docs.deepseek.com/updates)实际完整日期目录，Dec1 V3.2/Speciale → 2026Apr24 V4，不见本窗更新；所声明范围只此官方release目录。
- Kimi：[Blog](https://platform.kimi.com/blog) Overview与[Changelog](https://platform.kimi.com/blog/posts/changelog)实际12192字符；发布日期Nov7，最新章节Nov6 K2 Think，下接Oct27/Sept5，至2024Apr。没有扩仓库普通提交。
- Hunyuan：首查[Research](https://hunyuan.tencent.com/research)实际6885字符仅skeleton；本任务浏览器iab/chrome均明确不可用，不伪称看过动态全部。原生POST `https://api.hunyuan.tencent.com/api/blog/publicList`，body `{pageNum:1,pageSize:20,renderType:0}`，本轮code0/totalNum9/list9，publishedAt全2026，最早1770090898；不是沿用此前11项数量。不能证明旧2025全部，官方域有界替代无恢复时隔离。
- Z.ai：首查[Research](https://www.zhipuai.cn/zh/research)原生1097209字符，实际解码12个RSC flight块、15个去重含createAt文章对象，不抄正文库存。2025最近：AutoGLM145=Dec8T16Z、ASR149=Dec9T16Z、TTS147=Dec10T16Z，其余对象2026。官方release所见后邻Dec22 GLM4.7。未见本窗目录条目；createAt明显午夜日编码不授首发精度，不拿release替代论文目录。现有可提取对象已检查，不声称归档保留了全部历史文章。
- Seed：原网页Research精选及papers当前1–20/242不是旧列表。原生 `get_article_list_v2?article_type=1/2&count=20&order_desc=true&publish_year=2025`，US头，两类均18行/next20/has_more true，total94/45；停止在本窗邻接，不读94/45库存。Paper ID1323 Seedance `PublishDate=1765728000000` (Dec15BJT00) → ID875 GR-RL `1764604800000` (Dec2BJT00)。Blog ID1817 Seedance `1765882058000` (Dec16BJT18:47:38) → ID1504 GR-RL Dec2；pinned Dec24/18同读但不假定排序。午夜明显日编码不补上线精度；本窗在这些相邻段之间，不授全机构零事件。
- ERNIE：官方Blog实际原生26083字符、Page2/2，Dec23 ERNIE5.0-1203排名 → Dec9 ERNIE5.0-1103排名 → Nov21，已读本窗邻接。排名标题不因机构名进入贡献集合，不读周级源。
- MiMo：官方Paper/Blog原生58111字符，Paper8项实际标题/日期已读：2025May12/Jun4/Sep19/Oct21及2026Jan8/Feb3/Mar13/Jun29；没有本窗Paper目录项。原Blog15标题无日期层保留审计；本次复用Mill实际官方4752.2908c99e.js frontmatter：HSS Dec19、Safety Dec18均窗外，收窄两具名缺口；Flash route无date、实际具名页HTTP200仅导航shell，必要正文/日期仍隔离。不能由空shell关闭或对MiMo整体授零事件。
- MiniMax：[English Blog](https://www.minimax.io/blog)原生134584字符，Dec23 M2.1→Oct27 M2邻接；中文入口跳新站未补历史。实际Agent Tech Blog仅2026May13长程团队条目，不冒充2025历史；无具名候选触发不扩其他工程附件。

四组官方域辅助搜索以 `2025-12-13 OR 2025-12-14 OR December 13/14, 2025` 限上述每日机构，均空；它们只补线索，非覆盖/零事件证明。一次宽`site:... OR`误命中外部gist已弃，不新增来源或待办。

本次pubs有限替代另实际两query：`site:research.google/pubs/ "December 13" "2025" ("language model" OR training OR inference OR multimodal OR agent)`及December14同式。搜索实际返回Blog和2015/2017/2021/2022页，未恢复可用2025 pubs证据；不谎称严格域过滤成功或零结果，未打开这些无关网页。

## arXiv实际查询与修正

先用Dec12–14提交日期及含Transformer的宽主题入口，model query显示1–200/222，输出并未逐项读完；它是过宽线索，不被设成222项关闭队列。原记录缺精确参数，此次从本线程实际请求/返回恢复下列已执行四页，**未重新请求或扩扫**。共同base为`https://arxiv.org/search/advanced`，精确共同参数如下，`terms-0-term`值见表（单个值内literal OR，不改写为多terms组合；按URL encoding加入请求）：

```text
advanced=&terms-0-operator=AND&terms-0-field=abstract&date-filter_by=date_range&date-from_date=2025-12-13&date-to_date=2025-12-14&date-date_type=submitted_date_first&abstracts=hide&size=200&order=submitted_date&start=0
```

| 主题 | terms-0-term原值 | HTTP200实际页末依据 | 首/末具名ID |
| --- | --- | --- | --- |
| model | `"large language model" OR "foundation model" OR "mixture of experts"` | Showing1–33 of33，33题名，单页 | 12201 / 12281 |
| system | `"LLM inference" OR "distributed training" OR "GPU kernel" OR "KV cache" OR "speculative decoding"` | Showing1–3 of3，3题名，单页 | 15773 / 12284 |
| multimodal | `"multimodal" OR "world model" OR "vision language action" OR "video generation"` | Showing1–22 of22，22题名，单页 | 12193 / 12320 |
| agent | `"LLM agent" OR "retrieval augmented" OR "agent memory" OR "tool use"` | Showing1–4 of4，4题名，单页 | 12389 / 12400 |

四页实际读取进程最终正常结束；Submitted/current-version日期均不是公开，逐个v1下界校正，不把查询日期参数当本窗公告。

网页检索 `after:2025-12-12 before:2025-12-15 site:arxiv.org` 同四主题仅恢复MixtureKit12121、ACR12219、RAST13727，均回官方精确v1。完整题摘分批实际读取；版本表明确在Dec14T01Z后提交的12536/12548/12544/12552/12508为未来下界，不投入本窗证据审阅，也不授真实归属日。

官方月长列表只作有界题名查漏，不用月ID归日。原首轮CL为skip400，其余同下表，HTTP200但单引号解析错误产生0题名，不授零条/已读。最终修正后CL实际skip425，其余保留原段；**“正在读”是过期停点**，此次回查实际返回六段各25题名且进程结束，最终共150题名。skip为略过条目数，不是页号；show25为单页上限，未请求后继页。实际六URL及完成位置：

| 原始有限URL | 实际题名数 | 首/末ID，停止于末项 |
| --- | --- | --- |
| https://arxiv.org/list/cs.CL/2025-12?skip=425&show=25 | 25 | 12537 / 13109 |
| https://arxiv.org/list/cs.LG/2025-12?skip=950&show=25 | 25 | 11859 / 12210 |
| https://arxiv.org/list/cs.DC/2025-12?skip=75&show=25 | 25 | 10236 / 12476 |
| https://arxiv.org/list/cs.AI/2025-12?skip=375&show=25 | 25 | 12225 / 13070 |
| https://arxiv.org/list/cs.CV/2025-12?skip=1300&show=25 | 25 | 11558 / 11800 |
| https://arxiv.org/list/cs.AR/2025-12?skip=50&show=25 | 25 | 07312 / 14661 |

上表修复的是原已执行范围/末端证据，不是新增150审阅或当窗论文。历史first-public权限只复用[固定原始日期恢复](../ARXIV_DATE_RECOVERY.md)的2025 day list/catchup/API有限失败、announced月精度、OAI Submitted非公开；不循环接口或按常规EST补个体时刻。

## 作者停点

本次已完整读Mill INDEPENDENT_REVIEW §4十项及§7–8恢复层，并按原有限集合修复：84 potential/11题摘或局部关闭/3题名范围外，总98不变。六项机制恢复与12500安全信号重开、旧误判保留；Neural Chameleons补helpful-only/abliterated主协议条件。12500旧HTML失败/官方PDF400超容量保留为历史，当前已复用Mill实际官方export精确v1 PDF HTTP200（25,900,642字节、98页）的必要原文pp1–4/7–9/12–13/16/29–31/51，不冒称作者另读全98页。错误上游标签后只生成解释的协议与局部准确率退化反证已校准；最终第二轮order准确率无显著差异、跨群体不同任务等直接边界见CORE_AND_BOOKS。核心正文请求撤销，仅first-public hold；v1 Submitted原值`2025-12-14T00:06:06Z`不是公开。三首批个体日期查询和固定历史失败层未变，84项均未授first-public，不进本窗候选/评分/Books。

Google pubs本窗历史段、Qwen/Hunyuan/MiMo Flash与MiniMax Agent Tech历史段、arxiv日级公开召回均外部终态保留，非Coverage/Evidence通过或零事件。pubs本次正确过滤和两有限主题日期文本请求结束后停止，不遍历45/772页。普通作者修复收束后交Mill局部核；不改其metadata/§6/复核记录、不授完成。
