# 2025-11-30：原始入口与有限停止记录

作者root，实际检查2026-10-04，最后补检北京时间15:41～15:44。窗口为2025-11-29T09:00:00+08:00～2025-11-30T09:00:00+08:00，即UTC11/29 01:00～11/30 01:00。只执行每日14源与目标主题补检，未扫描Weekly来源、普通PR或整类论文全文。以下数量属于当前返回的目录，不是当天论文数。

## 官方入口

1. **OpenAI**：[Research](https://openai.com/research/) 当前featured不提供目标历史段；[RSS](https://openai.com/news/rss.xml) 首次请求403后有限原生回退成功，单响应759641bytes，XML解析1245items，缺pubDate=0，本窗pubDate命中0。目标两侧为11/26 19:00Z Mixpanel事件与12/01 05:00Z条目。没有把1245条送入题摘队列，也没有声称RSS涵盖被删除页面。11/28～29官方域日期补检未恢复新机制原文；非官方社区账单/功能请求不作为研究证据。
2. **Anthropic**：[Research](https://www.anthropic.com/research) 当前10个入口均为2026年，See more未恢复历史分页；原生279195字符中没有可用nextCursor/hasNextPage等历史分页字段，目标Nov29/30无日期匹配。限定11/28～29官方域查询恢复的是窗外webinar、模型deprecation与Opus current card；card的11/24、11/25、12/05修订信息不构成本窗事件。未遍历完整system-card附件，也未用当前目录证明旧窗零研究。历史段隔离。
3. **Google**：[Research 2025/11归档](https://research.google/blog/2025/11/) 列10条，最新11/21、随后11/19、18、13等至11/04，底部无Next。DeepMind实际[page4](https://deepmind.google/blog/page/4/)与[page5](https://deepmind.google/blog/page/5/)共48个标题日期入口覆盖2026-02至2025-07；11月相关项的原页Gemini3为11/18、图像verification为11/20。蛋白/蜂类等AI for Science标题按暂缓范围关闭，不批量读摘要。Google pubs目标year/query原生请求25秒超时，web只恢复当前年份筛选，未获得日级切片。博客有限检查不替代pubs覆盖。
4. **Meta**：[Research](https://ai.meta.com/research/) 没有可提取历史文本；官方global_search本次原生连接reset，不作零结果。11/28～29官方域研究日期补检只回到SAM3等窗外研究，未恢复目标原目录。历史切片隔离。
5. **Qwen**：[旧入口](https://qwenlm.github.io/) 最新09/23并迁移到新Blog，新入口没有目标历史目录文本；限定11/29日期搜索定点读[Qwen3-TTS update核心说明](https://qwen.ai/blog?id=qwen3-tts-1128)。页面显示2025/12/04，citation urldate为12/01，代码model ID含11/27，URL尾1128不是首公开时刻。完整核心改进说明为声音/语言覆盖、韵律及指标与API用法；没有可辨认的新增训练/架构机制或控制条件下的新成立边界，按当前贡献门槛关闭，不采宣传性能。没有因日期不明另造该已关闭材料的请求；目录历史缺口仍独立保留。不得从2026年另篇Qwen3-TTS技术内容反填本篇机制。
6. **DeepSeek**：[updates](https://api-docs.deepseek.com/updates) web超时后原生恢复47922字符，日期标题读到2024-05-17，目标两侧为12/01 V3.2与09/29 V3.2-Exp，无Next；所列release没有本窗事件，不代表组织全部论文/仓库完整。
7. **Moonshot**：[Blog](https://platform.kimi.com/blog) 当前26条日期标题读至2024-05-29，11/06～07与09/16邻接，无Next。目标段没有列出新事件；不将后来的推荐视作新公开，不逐项扫描全组织PR。
8. **Hunyuan**：[Research](https://hunyuan.tencent.com/research) 无文本，hidden浏览器创建实际30秒超时并kernel reset，没有成功截图。POST `https://api.hunyuan.tencent.com/api/blog/publicList`，body为pageNum=1,pageSize=20,renderType=0，HTTP200/code0/total9。首个大响应输出截断，没有声称正文已全读；随后只抽取并实际读取9项标题/PublishedAt：100116=1789707529、100100=1787896672、100091=1785989409、100087=1784111171、100064=1783319811、100039=1777227059、100061=1782369407、100015=1770971763、100025=1770090898，全部2026年。PublicAt和PublishedAt不混用。当前Blog接口不替代2025年Research“全部”论文列表；有限官方日期补检未恢复历史，隔离。
9. **Z.ai**：[Research](https://www.zhipuai.cn/zh/research)与page2，原生读取已显示18个入口，最早12/07且“没有更多”；[release notes](https://docs.z.ai/release-notes/new-released)读到07/15，目标相邻为09/30与12/08。官方11/29日期查询回到2024/12/30 CogAgent新闻中对2024年11/29的回顾，明确不是2025事件，不跨年搬移。11月Research旧段缺失，不授历史零命中。
10. **Seed**：原始GET `https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&page_token=0&order_desc=true` 与type2，header `x-tt-locale: US`。首次错误参数400不作结果，修正后均200/StatusCode0，各实际18项，next_page_token20、has_moreTrue，total94/45。实际读取全部18项标题日期而非正文：type1置顶12/15、12/02后非置顶10/22及更早；type2置顶12月与11/27后非置顶10/23及更早。停在page0，不全扫全年余页；置顶/删除/修订不因排序下界得到排除保证。11/28～29补检回到Depth Anything3官方11/27，原字段1764172800000为11/26 16:00Z，即11/27 00:00BJT，窗外，不把二次传播视作新公开。
11. **ERNIE**：[blog首页](https://ernie.baidu.com/blog/zh/)与[page2](https://ernie.baidu.com/blog/zh/page/2/)共16项（10+6），末页到06/30、无Next；目标两侧为11/21与12/09。已列Blog没有本窗项，不声称所有历史仓库事件完整。
12. **MiMo**：[首页](https://mimo.xiaomi.com/) 实际338行，Paper8个日期入口目标两侧2025-10/21与2026-01/08；Blog15项无日期，More未恢复目标历史分页；限定官方11/29补检未恢复具体原文。Paper范围已核，但不替代Blog；缺旧Blog日期/切片。
13. **MiniMax**：[EN Blog](https://www.minimax.io/blog)12项、[中文Blog](https://www.minimaxi.com/blog)重定向minimax.cn13项，目标两侧10/27与12/23，中文多出01/15，均无Next。Agent Tech Blog只有空导航；进一步实际读取[官方llms.txt](https://agent.minimax.io/docs/llms.txt)50行，只有当前Agent Team技术入口，没有可核2025年目标列表。该恢复只核目录，不把当前说明反填旧窗；Agent历史段隔离。
14. **arXiv**：2025年有效的[availability精确commit](https://raw.githubusercontent.com/arXiv/arxiv-docs/95c71658adbaa987dc2ba1105ef9c5201ecde4ce/source/help/availability.md) 原生两次reset后通过GitHub contents API恢复同一ref并base64解码实际阅读，当前[帮助页](https://info.arxiv.org/help/availability.html)亦读作对照。2025/11/27是公告假日；本窗UTC换算为纽约11/28周五20:00EST至11/29周六20:00EST（zoneinfo实际转换），周五/周六无常规公告，因此没有一个标准公告批次落窗。下次周日20EST为12/01BJT09，不在本窗。规则中typically不是单篇首公开时刻证明，也不排除提前作者稿或异常事件。

## 有界主题与负侧

arXiv非标准事件只作有限补检：官方域 `"Nov 29, 2025"` 分别配language model/Transformer/MoE、GPU/inference/distributed training、world model/multimodal/vision-language、agent/memory/reinforcement learning四组查询，实际工具返回空；这不是全网无论文。之前inference日期查询出现[2512.00338](https://arxiv.org/abs/2512.00338)，实际完整摘要为binary time-series statistical inference的估计/检验，不是大模型训练/推理机制；按范围关闭，submitted Nov29不改造成公开日期。Qwen核心说明的贡献关闭见第5项，不因日期混杂改写为当窗候选。

辅助搜索负责入口与日期恢复，不提供机制或性能证据。以上未形成确认落窗的候选家族，候选0、候选证据采用0、Books No Change。历史目录不可恢复与非标准公开范围均隔离；独立语义复核尚待执行，不由本文自授完成。

## Anthropic有限恢复纠正

首轮只查首屏/分页字段不足。再次本日curl原生Research成功，保存`anthropic.html`（279365bytes），实际对`self.__next_f.push`内容用JSON解码得到一个flight字符串，定点检查publishedOn/slug目标邻接：11/25 11:05Z estimating-productivity-gains之后为12/01 00Z smart-contracts，目标窗没有已列条目；11/24 15:10Z prompt-injection-defenses也窗外。没有以首屏空结果授零研究。首次“历史段隔离”被此具体恢复解除，正式来源行同步；当前CMS删除/遗漏仍不获保证，不把44个2025字段转为题摘队列。
