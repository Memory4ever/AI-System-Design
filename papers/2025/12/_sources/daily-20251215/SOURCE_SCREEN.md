# 12/15 原始来源、窗口与停点

Gibbs；实际启动2026-10-02T21:11:11+08，窗口 `[2025-12-14T09:00:00+08:00,2025-12-15T09:00:00+08:00)`。本日AGENTS/研究合同/Report合同/Prompt/ROADMAP及每日源使用说明独立重读，15目录与_sources原停点不存在。以下本日原站重新访问，不继承邻日报完成或其候选分母；少量已知固定历史语义只用于日期恢复边界。

## 十三官方每日源

- OpenAI原[RSS](https://openai.com/news/rss.xml)本日HTTP200、756710字符，XML本窗邻接Dec12三条（BBVA/Codex-SoraAndroid/BNY）→Dec16 Images1.5/StayAhead的00GMT、science08/09GMT。该所见Feed段没有Dec14/15，不授整机构零；日期原精度保留，不以当前Research首页作历史。
- Anthropic原[Research](https://www.anthropic.com/research)HTTP200、317670字符，publication字段本日仍Dec4T17Z interviewer→Dec18T10:33Z vend2→Dec19T19:45Z bloom；其他资源created/updated不授发布日期。只限定所见目录邻接。
- Google Research原[2025Blog](https://research.google/blog/2025/)HTTP200、182543字符，Dec12健康活动→Dec15 PaperAssistant→Dec18年终，下邻Dec10 DPchatbot、Dec4 Titans/MIRAS。PaperAssistant日标签与本窗相交，实际核心已读，贡献前关闭见ADMISSION；页面May18,2026改名更新不冒充2025版本。DeepMind原page4 HTTP200、185443字符，实际Dec月八个标题；audio/FACTS/Scope2/Flash具名原始日期定点复用固定公开字段（Dec12T17Z/9/19/17），不拿月标签授日。
- Meta原[publication page4](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=4)HTTP200、287704字符，Dec12 TIE→Dec16 audiovisual、下邻Dec1 RIFL；收录非论文首公开，未识别本窗新版本，不认证全机构召回。
- Qwen原[Blog](https://qwen.ai/blog)HTTP200、92469字符，Qwen skeleton/route home，没有2025可读目录；本窗官方域有限辅助空，旧站停点只作入口失败语义，不授零事件。历史本窗列表缺段终态保留。
- DeepSeek原[Change Log](https://api-docs.deepseek.com/updates)HTTP200、47922字符，完整日期目录Dec1 V3.2→2026Apr24 V4。本日仅该release切片，无普通仓库提交扩扫。
- Kimi原[Changelog](https://platform.kimi.com/blog/posts/changelog)HTTP200、12192字符，Nov7文章/Nov6 K2Think→Oct27→Sept5至2024Apr；Blog Overview固定邻接入口已知，未把机构GitHub当前目录授历史全部。
- Hunyuan首查原[Research](https://hunyuan.tencent.com/research)HTTP200、6885字符skeleton；本任务可用浏览器iab/chrome均已明确不可用。原生publicList POST `{pageNum:1,pageSize:20,renderType:0}`本日code0/total9/list9；无2025项，历史All仍外部保留。内容中安全签名资源不是研究日期依据，不保留凭据参数。
- Z.ai首查原[Research](https://www.zhipuai.cn/zh/research)HTTP200、1097209字符，本日解码RSC得到15个含createAt独立对象；2025三项AutoGLM145 Dec8T16Z、ASR149 Dec9T16Z、TTS147 Dec10T16Z，其余2026。所见列表处理完，不拿午夜编码授first-public，也不声称完整归档未删除。release固定后邻Dec22不代替Research。
- Seed本日原生2025目录接口 `get_article_list_v2?article_type=1/2&count=20&order_desc=true&publish_year=2025`，US头；两类各18条，next20/has_moretrue、total94/45。Paper1323 Seedance→875 GRRL，Blog1817 Seedance→1504 GRRL；pinned2141/1815 Dec24/18独立检查，不假定排序。1323 PublishDate1765728000000是Dec15BJT00日编码，目录完整摘要及链接2512.13507v1完整题摘已读；v1提交15Dec16:36:52Z晚于本窗，但不能替代较早Seed正文first-public。1817 PublishDate1765882058000=Dec16BJT18:47:38不同事件。停止在本窗相邻段，不扫描94/45库存。
- ERNIE原[Blog](https://ernie.baidu.com/blog/zh/)HTTP200、26083字符，实际Page2/2：Dec9 ERNIE5.0-1103排名→Dec23 ERNIE5.0-1203排名，下邻Nov21。只所见日期段，排名题名不自动构成架构贡献。
- MiMo原[Paper/Blog](https://mimo.xiaomi.com/)HTTP200、58111字符，具体Paper8项重新读取：May12/Jun4/Sep19/Oct21→2026Jan8/Feb3/Mar13/Jun29。Blog15标题尾V2Flash/HSS与More无日或文章href，2025历史Blog有限官方域替代仍不可得；保留外部缺段，非零事件。
- MiniMax原[English Blog](https://www.minimax.io/blog)HTTP200、134584字符，Oct27M2→Dec23M2.1邻接；中文入口redirect边界已知。原[AgentTech](https://agent.minimax.io/docs/techblog)HTTP200、212494字符当前页不提供2025目标相邻列表；历史切片隔离，不认证全年仓库或工程站。

本日四组限定官方域查询：Qwen；Hunyuan/MiMo；Anthropic/Alignment/Google；OpenAI/Kimi/MiniMax/ZAI，日期为Dec14/15（ISO或英文），均空。只作为有限辅助，非原源覆盖/零事件证据，未扫描周级来源。

## arXiv检索与纠正

首次四查询错误order=date得到HTTP错误；一次缺advanced标记返回搜索表单。它们不是零结果。实际修正为 `advanced=&order=-announced_date_first&date-filter_by=date_range&date-from_date=2025-12-14&date-to_date=2025-12-15&date-date_type=submitted_date_first&abstracts=hide&size=200&start=0`。第i项 `terms-i-field=abstract`、首AND其余OR；四组实际词：

- model：language model / foundation model / mixture of experts，1–91/91。
- system：LLM inference / distributed training / GPU communication / KV cache，1–27/27。
- multimodal：vision language / video generation / world model / vision language action，1–44/44。
- agent：LLM agent / retrieval augmented / tool calling / agent memory，1–20/20。

四组各单页实际标题读完，交叉先去重；Submitted只能发现，Announcement只年月。当前月目录只作有界补检，不能授首公开日：`/list/<category>/2025-12?skip=N&show=25`，CL425、LG975、DC100、AI400、CV1400、AR50，各25题名共150。首轮regex忽略HTML单引号/属性空格导致0解析，实际修正后取得标题，不记为空窗。不扩全月；明确领域医疗/物理材料/生物、传统分布式/芯片版图题名范围止步，相关/含糊仅定点题摘。

精确v1版本表提供本窗右端Dec15T01Z之后的个体提交下界，不能由编号批量排除。2601/2602后月编号若v1真实Dec14仍处理潜在贡献；没有用后月编号改归日。已读完整题摘不自动等Evidence，必要含糊准入局部仍在执行。

## 本日收束与外部边界

首批三潜在/AnimatedLLM负侧已交校准。实际补齐Memoria/SoT/SignRAG、sandbox/协商/LLRC必要局部与owner/相邻段；12595/13714 HTML失败后各PDF有限替代成功，未借失败删项。含糊Quantum INR/TwinFormer/knowledge-guided MAE保留潜在，10180按完整题摘具体关闭，不按领域或硬件标签机械排除。

本日Hunyuan publicList第二次只提取必要字段核回9项（不保存正文/签名参数）：publishedAt最早1770090898、其余1770971763/1777227059/1782369407/1783319811/1784111171/1785989409/1787896672/1789707529，全部2026；仍不证明2025目录无事件。

本日个体官方域有限日期替代：`site:arxiv.org "2601.08835" announced`、`site:arxiv.org "2512.13733" announced`、`site:arxiv.org "2512.12806" "Dec"`均空，不当零事件。实际重读[ARXIV_DATE_RECOVERY](../ARXIV_DATE_RECOVERY.md)的2025固定文档/公告与OAI/list/catchup失败及字段语义；它只授历史规则，不授本日任何个体日期。无需让每个潜在家族重复同一不能给first-public的接口；没有日粒度公告或完全落窗正文区间前，ADMISSION全部potential保留外部终态，禁止採用。EST20:00是次日BJT09:00，若确为该时刻进入下一Daily，不填本日右端内。

初次作者交还时普通扫描/具名准入/必要局部/Books对读标0；此后Popper发现六项普通差额，不能沿用该旧ready授日完成。root已接手六项作者修正，非作者复核仍未完成。潜在日期恢复、Qwen/Hunyuan/MiMo旧目录和MiniMax Agent Tech2025段安全隔离，不是覆盖通过、Evidence完成、Books已落实或零事件。

## 六项具名独立发现的作者同步

root复用本日Popper实际独立原源层及16日同身份/命题的有效必要core，不声称本人重新访问。DreamRAM/EEG voice已在ADMISSION撤销关闭；Guardrail分类器指标及RAMBO异名已校正。随后同一标题误排理由的12887/12932恢复最小主线机制、12795/09709完整题摘后具体关闭也已同步；当前111potential/20关闭，剩9title-only，不机械全量全文。

- Anthropic增补[Alignment Science Blog](https://alignment.anthropic.com/)实际December六项至November段：Dec19、16、12、8相邻记录，有限停止；Research主目录不代替该可得子目录。未用日标签或所见段0授全机构零事件，mitigations/个体first-public依然隔离。
- Kimi增补[原始CLI CHANGELOG](https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/CHANGELOG.md)0.64 Dec15完整core：会话选择恢复/全局MCP管理未给新恢复一致性、state migration或授权隔离语义，贡献前关闭。只同版本处置，不以日标签授release时刻、不追不影响关闭的日期，也未执行CLI。

来源表/正式§1–5已同步八项及四个原题名局部结果，待Popper核实际来源边界及最终日级；未写其metadata/§6或共享Books。

## Google publications本窗有限恢复

root在15作者同步阶段重新加载当前AGENTS/研究/Report合同、每日源主题、Prompt、ROADMAP与本日停点后，实际访问原[2025过滤](https://research.google/pubs/?category=2025)及两个本窗主题/日期文本搜索。网页工具三URL均InternalError；原生只读HTTP替代成功，HTMLParser检查2025 checkbox确实checked。首次长输出截断后，仅重新取同三URL的字段核验，不把截断当完整原文阅读，也未扩发现库存。

最终原生响应：year过滤HTTP200，`1 - 15 of 675 publications`、`of 45 pages`；只核接口/年份/分页字段，不读675条/45页。[language model December14](https://research.google/pubs/?category=2025&search=language+model+December+14+2025)与[training/inference/multimodal/agent December15](https://research.google/pubs/?category=2025&search=training+inference+multimodal+agent+December+15+2025)均HTTP200、2025checked、`0 - 0 of 0 publications`/No Results Found，无下一结果页。它们是文本检索，不是日粒度首公开过滤；0不能证明空日，year也不能赋公开时刻。

所需pubs本窗原始公开/相邻历史切片仍未恢复，外部终态保留，不由2025 Blog替代或授Coverage。接受原始目标段/具名论文的公告与完全落窗公开区间后，只重开本来源/家族；不继续45页、全年或同类失败日字段循环。source正式Google行与§5已同步，不新增候选或Books。
