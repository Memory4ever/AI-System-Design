# 2026-01-08 Daily：2026-10-07 增量来源补查（作者记录）

- 本轮只补北京时间自然日 `2026-01-07T00:00:00+08:00 ～ 2026-01-08T00:00:00+08:00`，即 UTC Jan6T16～Jan7T16；原09～09窗口、17候选及其日期/评分/§4有效审阅不改，不搬已归属其他日报的同事件。
- 检查时间：来源2026-10-07T14:25:00+08:00，受影响写回14:49:19、验收状态写回14:53:28。执行者：audit_supp_jan06（本日作者）；root已完成新增准入/必要源及日期合取，jan02_new_evidence已完成新增Books非写入者POST和最终实际Report日级复核，通过见[独立记录](shs-audit-20261007.md)。原有效非作者验收仅适用于原轮。
- 完整重读当前 AGENTS、研究/报告合同、统一 Prompt、sources使用说明/每日14组/arXiv主题和 ROADMAP；本日材料独立加载。跨日只定点核 Health 同事件去重，未扫其他日期候选或 Weekly。
- 原候选与§4保留范围 SHA256：`dd431ac0e0b2e1ac48d56587152be4ff42f79509ef822976ed65e233c6c56dce`（§3标题之后至原§5标题之前；校验时只排除本轮追加SHS行及同标题§4）。本作者不写Books/LEARNING_STATE/索引；root独立负责实际Ch24新增两段。

## 每日14来源：实际入口与有限停点

| 来源 | 实际入口/返回与本轮停点 | 结果与必要限制 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)本次可读；[RSS](https://openai.com/news/rss.xml)HTTP200、1251 metadata，只定位Jan1–12邻接段。Health Jan7T00Z、Tolan Jan7T10Z在自然日窗；Netomi Jan8T00Z窗外。 | 已检查。Health官方安全/记忆核心实际读后，定点核原Jan07条目同URL、同单向memory/connector权限命题与实际POST，去重复用，原归属不动；Tolan原本日核心负侧与独立复核保留，不重跑同事件。Jul23可见更新不算Jan07新机制。有限feed不授机构无遗漏。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)HTTP200；HTML174 publishedOn，实际Jan07字段0，邻接Dec19→Jan8T00Z。 | 已检查。Jan8T00Z critical-infrastructure在新窗外；原读核保留，不重读全部174正文，不请求不存在的具名缺口。 |
| SRC-GOOGLE-AI | [Research一月目录](https://research.google/blog/2026/01/)经实际年页January链接恢复，9条Jan28→Jan12；[DeepMind publications](https://deepmind.google/research/publications/)page1邻接Jan9→Dec3；[Google pubs](https://research.google/pubs/)只有year字段。Jan7官方site检索无结果。 | 受阻仅限必要日级publication日期入口：year-only不能恢复Jan07主题发布时间，月份blog/page1有限范围已检查。未要求所有隐藏历史、删除证明或全机构镜像，不将0检索当0事件。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)0可读正文/历史字段；Jan7官方site检索无结果。 | 受阻仅限Jan07可读日级研究目录/具名原发布；不是要求证明互联网无遗漏，不规避访问控制。 |
| SRC-QWEN | [官方research-list API](https://qwen.ai/api/page_config?code=research.research-list)HTTP200，递归解开data字符串后完整60条unordered date，max `2025-12-23T05:08:30.000Z`，无Jan07条目。 | 已检查该有限60条目录。原本日Qwen3-VL-Embedding同家族exact-SHA核心贡献关闭保留；API目录与官网发布渠道不同，不用未具名删除/修订可能性请求全历史快照，也不授所有渠道零事件。 |
| SRC-DEEPSEEK | [官方news](https://www.deepseek.com/news/)研究索引10条，Jan12 Engram→Dec31 mHC；动态Apr24→Dec1跨自然日窗，未读窗外论文。 | 已检查当前可读有限索引；不是全机构/作者先行镜像覆盖。 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)26条、max Nov7；[CLI release API](https://api.github.com/repos/MoonshotAI/kimi-cli/releases?per_page=100&page=1)100条到Oct24，0.72 Jan4T06:01:07Z→0.73 Jan8T16:54:15Z。官方[CHANGELOG](https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/CHANGELOG.md)Jan4→Jan9。 | 已检查这三个有限入口，无本窗条目；只用published_at，不用created_at。此范围不代表其他模型发布/所有revision。 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)页面失败后，fresh POST [publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，`pageNum=1,pageSize=1000,renderType=0`，code0/totalNum9/list9，逐条publishedAt/displayPublishTime/publicAt最早Feb03。 | 已检查实际完整当前9条有限目录。无具名Jan07遗漏或字段矛盾线索，不再由当前最早Feb03泛化为机构受阻/索完整历史快照；不是当时完整档案证明。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)当前15条时间排序，Jan13→Dec10/9已跨窗，在查看更多处停；[release-notes](https://docs.z.ai/release-notes/new-released)Jan14→Dec22。 | 已检查有限目录/notes，未读全年正文或认证其他渠道修订。 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)对应API：type1/2、2026 ASC与2025 DESC各count20/page_token0。2026paper total82/list20/next20/has_more，first PublishDate1768838400000（北京Jan20）；blog total23/list9/next20/has_more，first1770825600000（北京Feb12）。2025paper total94/next20/has_more但缺sub_article_list；2025blog沿原有限返回。 | 已检查本窗相关2026 ASC日期桥接；pin/has_more/少于count均保留，不称全目录。窗外2025论文返回缺list是入口限制，不变成无具名Jan07线索的历史请求。 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)当前page1邻接Jan15→Jan8→Dec23，无Jan07条目。 | 已检查有限日期段；Jan8排名在自然日窗外，原已核负侧保留，不再索无关时区或读窗外正文。 |
| SRC-XIAOMI-MIMO | [官网](https://mimo.xiaomi.com/)Paper卡8条；[真实JS元数据](https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js)恢复16个EN Blog routes，定点查真实正文日期（含显式iframe入口），停点详下。 | 已检查16有限routes；15实际正文日期均窗外、generic blog1无新增机制。原02780更早MOPD同体审阅/日期保留，不把Jan8卡变Jan07新事件，不索所有镜像。 |
| SRC-MINIMAX | [EN](https://www.minimax.io/blog)/[CN](https://www.minimax.cn/blog)可读日期链Jan27/28→Dec23。[AgentTech](https://agent.minimax.io/docs/techblog)实际HTML当前只呈May13文章，2024-01-01为配置占位字段、May13 dateModified不独自当首公开。 | 已检查这三有限页面。无具名Jan07新材料，不请求被删历史或将May13泛化机构受阻。 |
| SRC-ARXIV | 原四主题原参数重新取metadata，model105（0/80+80/80返回80+25）、system8、multimodal22、agent19；system新ID02799，完整exact-v1题摘及必要core已读。四旧稿lastUpdated实际attempt响应各0，但接口改写过滤。 | 已检查有界新稿metadata。lastUpdatedDate不支持、被改写为submittedDate导致互斥区间，0不是旧修订阴性。保留历史revision入口限制；02799v1获root准入并新增唯一候选，不自授日级验收。 |

每日14来源作者范围为12已检查/2受阻（Google日级publication日期、Meta可读日级入口）；另下述arXiv辅助title-backstop检索受限，不计机构零事件，不请求全公开批次。原触发OpenReview与表外LTX差额不属于新增机构扫描，旧具体hold原样保留。

### MiMo真实日期停点（不是十个JS壳hold）

当前EN routes：code-long-horizon June10、tilert June8、v2-5-inference May30、v2-6-tool-call-repetition Sep27，均2026；v2-flash-hss/safety正文Dec22 2025，frontmatter分别Dec19/18，两字段冲突均窗外，保留不改。

其余route页面的显式iframe正文入口：`/mimo-v2-5-asr/index.html` April2026；`/mimo-v2-5-pro/index.html` Apr27；`/mimo-v2-5-tts/index.html` April；`/mimo-v2-5/index.html` Apr22；`/mimo-v2-6-material-research/index.html` Sep21；`/mimo-v2-flash/index.html` Dec16 2025；`/mimo-v2-omni/index.html`、`/mimo-v2-pro/index.html`、`/mimo-v2-tts/index.html`均Mar18 2026。只取必要正文date，不逐项方法审阅窗外文章。

`/blog/blog1`实际iframe [generic描述](https://mimo.xiaomi.com/htmls/mimo_v2_flash_model_description.html)完整可读：只是Transformer/效率/推理/通用场景能力介绍，无新算法、实现或安全纠正命题，贡献前关闭；不为不影响关闭的无日字段索秒级日期。

## arXiv发现、去重与实际新线索

1. 原主题字符串/提交缓冲/分页沿本日[initial metadata](arxiv-initial-metadata.jsonl)与[model tail](arxiv-model-tail.jsonl)精确URL重取：`submittedDate:[202601051900 TO 202601061859]`，ascending，80/page，model尾页80。未把105+8+22+19有重叠metadata转换全量候选队列；除02799外ID集合与各原查询相同。
2. 四原主题各加 `lastUpdatedDate:[202601061600 TO 202601071559] AND submittedDate:[199001010000 TO 202601051859]`，start0/max30/lastUpdatedDate ascending，实际各total0/returned0。非作者复现发现API不支持该过滤，响应feed title把lastUpdatedDate改写为submittedDate，生成两个互斥提交区间。本作者定点复现原model query亦见同改写；因此四次0响应均不支持“零修订”或有效revision覆盖。原[source-stop](source-stop-and-limits.md)已记录lastUpdatedDate不支持；当前只隔离本窗历史修订入口限制，具体旧version公开记录/具名revision公告到达才重开，不改原17、不扩扫所有旧ID。
3. 辅助官方[cs.CL月标题页](https://arxiv.org/list/cs.CL/2026-01?skip=0&show=25)本次不可达；标检索受限。原定点补漏4题摘和28AB有效审阅不动，不请求2168全批次/所有标题逐项AB。
4. 当前API02799v3题摘使它新匹配system query；本次完整读[02799v1题摘](https://arxiv.org/abs/2601.02799v1)，标题为Stratified Hazard Sampling。只把v3当发现线索，不把Oct重要修订搬回Jan07，也不借v3四模型实验或新代码为v1证据。

### 02799v1必要审阅与独立校准后的采用

实际读[exact-v1](https://arxiv.org/html/2601.02799v1) §2.1、§4算法/命题、§5、§6、C1/C3与必要安全分支。增量是累计jump mass跨步维护单phase时钟，去向kernel独立；固定mass随机舍入边界不继承到state-dependent终态law，非exact Markov模拟。风险排序phase破坏iid无偏条件；安全协议非已验证安全。UDLM仅64句×5seed、NFE4–64、GPT2-large PPL；模型checkpoint/硬件未明确，未复现。

评分2+2+2=6、深入完成已获root独立校准。唯一owner按ROADMAP为`MULTIMODAL-GENERATIVE-PARADIGMS`/[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：原rate/destination与absorbing hazard没有single-phase跨步memory分责，root实际在两者交接处追加1174/1176两段机制/边界，保原sampler回退。jan02_new_evidence作为非写入者实际POST窄核通过，未因此自授Report完成。作者只将唯一新SHS行及同标题§4写回本日报告，不动Books。

必要日期原字段：OAIraw v1 Submitted=`2026-01-06T08:19:02Z`；DataCite v1 Updated=`2026-01-07T01:28:52Z`、created=`2026-01-07T02:41:45Z`、registered=`2026-01-07T02:41:46Z`。来源：[OAIraw](https://arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:2601.02799&metadataPrefix=arXivRaw)、[DataCite](https://api.datacite.org/dois/10.48550/arxiv.2601.02799)、[官方公告/ID规则](https://info.arxiv.org/help/availability.html)。提交晚于前cutoff Jan5T19Z，ID不得提前分配，官方Jan6 20ET公告批次与具体findable注册上界合取支持北京Jan07公开日；root及jan02_new_evidence已独立核合取，本轮新行只写2026-01-07日级归属，不要求秒级考古。registered/Updated不是public瞬间，也非没有作者先行镜像证明。

## 保留项与作者停止

- 正式原17候选/原日期评分/§4及原4实际POST全部不改；本轮新增唯一正式家族02799v1，现18家族（5整合、3已有覆盖、8仅报告、2中心保证隔离），原28AB加新1完整exact-v1题摘为29。Health同事件沿原Jan07归属去重。
- 当前外部限制仅Google必要日级publication日期、Meta可读日级研究入口和辅助title-backstop；原03067具体OpenReview更早body、LTX三branch差额、MiMo旧体、03305/03331越窗与LoRA/DIP受影响保证保持旧证据隔离，不泛化索所有历史。
- 本轮作者扫描/具名审阅、新增Books窄POST与最终实际Report六部分独立日级验收已处理，普通待办0，报告完成。外部限制为安全终态保留项，不用于超范围Evidence/Books/性能/安全或互联网无遗漏断言；只在具名必要原记录到达时重开受影响项。
- 实际作者校验：本日V3格式/可判定一致性、限定README/supplement的`git diff --check`、两个文件全部本地链接与行末空白检查通过；18行，排除唯一新增SHS行/同标题§4后的原内容SHA与上述冻结值一致，原17行不变。非作者独立复现同指纹及机器检查，实际语义根据其独立记录而非校验器。状态写回后再跑完成态检查；未stage/commit/push。
