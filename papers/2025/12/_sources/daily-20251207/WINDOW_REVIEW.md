# 12/07 独立窗口原始观察与作者判断

执行于2026-10-02，恢复写入检查时间19:14:29+08:00；07首次启动及此次恢复均重读AGENTS、三个合同/来源每日组、Prompt、ROADMAP。本日无既有checkpoint，窗口为 `[2025-12-06T09:00:00+08:00,2025-12-07T09:00:00+08:00)`，即Dec6 01Z至Dec7 01Z。不从其他Daily结论生成本日。

## 14源实际切片

固定历史目录[原始观察](../daily-20251201/RECOVERY_NOTES.md)逐源重读，仅复用原始相邻段、分页和接口限制，本日重新套窗口；不是复用另一日覆盖结论。

- OpenAI本日重新解析[RSS](https://openai.com/news/rss.xml)，1243 items；Dec4 Australia19GMT至Dec8 Virgin00GMT、enterprise04GMT、Instacart06GMT相邻。本窗无feed item，只支持该feed切片。
- Anthropic publicationList Dec4 Interviewer17Z至Dec18下一条，本窗未见具名目录事件；不把现在正文称2025冻结快照。
- Google Blog2025第1页Dec4 Titans/MIRAS至Dec10 DP、DeepMind第3页Dec3 Reward Features/Nov21邻接，按本窗有界判断，无具名本窗新事件证明。
- Meta第4页Dec12/Dec1/Nov19至Nov10跨过本窗；AdvancedIF仅目录身份，不把收录授首次公开。
- Qwen旧Sep23/新站空正文/部署无旧列表/错误_posts404/README有限替代，无2025完整历史目录；隔离而非零事件。
- DeepSeek用正确API Docs Dec1 release/后续2026邻接；旧news路径实际重定向不能恢复首发。只声明此入口范围。
- Kimi全Overview26项最近Nov7，changelog Nov6；本窗没有具名新条目线索。
- Hunyuan Research skeleton和浏览器超时、All POST API total11且全2026，不足恢复2025Research；停止同接口。
- Z.ai本日实际重新读Research `?page=2`到Dec7 GLM-4.6V、“没有更多”，release notes显示Dec8。下面具名恢复正文和日期，不借目录完整性背书。
- Seed2025paper首20/total94/has_more至Dec2 GR-RL/Oct22，Blog首20/total45至Dec2/Nov27/Oct23，本日按原始精确邻接重判，不扩库存；常见16Z日编码不能当上线钟点。
- ERNIE2/2页至Nov7，Nov21/Dec9夹窗；只声明Blog入口范围。
- MiMo Paper8项Oct21/Jan8，Blog15项/More历史不全；部署路由HSS Dec19、Safety Dec18，无date的Flash不借下一route日期；历史缺口隔离。
- MiniMax英文13项/中文Oct27 M2至Dec23 M2.1夹窗；没有具名事件触发Agent Tech Blog。
- arXiv主题查询和官方有界查漏如下，不以month ID归日。

## arXiv发现与停止范围

本日实际四查询均以 `site:arxiv.org "6 Dec 2025"` 开始，分别追加 `(transformer pretraining optimization mixture-of-experts)`、`(inference KV cache GPU compiler)`、`(multimodal VLA world model)`、`(agent retrieval evaluation reinforcement learning)`。四组返回空，只说明搜索限制，不证明没有公告。

官方[cs.IR十二月首1–25](https://arxiv.org/list/cs.IR/2025-12?skip=0&show=25)，total225；[cs.PF首1–25](https://arxiv.org/list/cs.PF/2025-12?skip=0&show=25)，total52，原生HTML实际成功。只浏览这两段、不翻全月，按模型检索/表示、执行/测量主题定点读精确v1。IR初读21个完整题摘，中段输出缺失的00772/00968/01372/02474/02502另实际读取补齐；含糊BMF03807另读完整题摘。PF先核15个可能相关条目的版本下界，4个非明确晚于本窗者读完整题摘；AutoGuard04368另读完整题摘。下面不是当日新论文数量。

### 潜在准入：21个arXiv家族，均首公开隔离

| 精确v1 | 原约束→实际增量→需重考虑的选择；采用限制 |
| --- | --- |
| [SAFE 00007](https://arxiv.org/abs/2512.00007v1) | retrieval多加自反query rewrite未必更稳定；本文Self-RAG一致性下降相对基本RAG是窄反证，需重核检索升级验收。50文章/246claims局部数据不授临床效果、普遍可靠性。 |
| [Breaking it Down 00367](https://arxiv.org/abs/2512.00367v1) | 定长chunk可能割裂语义；PSC/MFC把语义chunk投影及多指标融合用于retrieval/generation，潜在索引表示增量；不采用24倍宣传或把医学域当准入/排除理由。 |
| [DLRREC 00596](https://arxiv.org/abs/2512.00596v1) | 固定降维分离于排序目标；LLM多向量联合降维/CF contrastive优化可能改变语义噪声与排名目标的对齐；不从应用排行授因果增量。 |
| [ProEx 00679](https://arxiv.org/abs/2512.00679v1) | 单一LLM profile可能绑定偏见；多profile组合环境与invariance学习是潜在derived-profile稳健表示条件，不证明CoT真实偏好或环境覆盖。 |
| [SHRAG 00772](https://arxiv.org/html/2512.00772v1) | 作者另读§3/§5.1.1：多语言关键词按重要度递减形成OR query集合、去重后dense rerank；50 queries每条件10次比较AND/OR，具体检索召回/开销取舍有窄反证增量。不是“human-inspired”名称准入；QSR至少一个相关文档不等于正确答案，AND语义/搜索引擎相关性不可泛化。 |
| [GRM 00968](https://arxiv.org/abs/2512.00968v1) | 序列级reward难分配相关性推理credit；Stepwise Advantage Masking与轻量distill提出过程credit替代，潜在RL训练机制；不采用商用排名收益为普遍提升。 |
| [SSR 01372](https://arxiv.org/abs/2512.01372v1) | 模态噪声在不同频率作用不同；graph spectral bands、masked consistency与跨band低秩融合保留频率可靠性条件，不授任意模态去噪。 |
| [LORE 03025](https://arxiv.org/html/2512.03025v1) | 作者另读§5/§6.1–6.2：hot pair离线cache、medium由LLM教小排序模型、hard实时推理的频率分层是具体quality/cost路径；Table11实时0.9%明确offline估计、未上线。CoT蒸馏pass1降/pass8升亦是评价反证，不把27%总收益或teacher shift解释当受控因果。 |
| [BookRAG 03413](https://arxiv.org/abs/2512.03413v1) | TOC层级与entity映射合成BookIndex及动态query route，潜在检索表示/适用条件；不把所有long-book RAG提高归因于该索引。 |
| [M3DR 03514](https://arxiv.org/html/2512.03514v1) | 作者另读§3.1–3.2/§4.1开头：layout-aware parallel translation/rendering、query合成、分开mono/crosslingual协议支撑比较单/多向量跨script取舍的窄线索。不是仅新增22语种榜单；合成翻译、字体及query由模型生成是共同混杂，不采用“universal”。 |
| [Personalization Paradox 04343](https://arxiv.org/abs/2512.04343v1) | generic reference similarity与personalized grounded answer可能反向；12问题/10配置mixed-effects报告评分冲突，潜在metric-target反证，不用RAGAS本身定义真值或生产质量。 |
| [UserSimCRS v2 04588](https://arxiv.org/html/2512.04588v1) | 作者补读§4.2–4.4/§5：固定information need驱动agenda，LLM单/双prompt停止策略不同；同系统不同simulator产生排序/尺度冲突，潜在模拟评价条件，不仅toolkit升级。100合成对话/组合不能证明真实用户满意度。 |
| [AskSafely 04852](https://arxiv.org/abs/2512.04852v1) | 敏感KG直接给外部LLM有暴露；先结构性移除敏感值再生成Cypher，潜在payload边界，不授DP、推断泄漏消失或任意查询安全。 |
| [RAG-IGBench 05119](https://arxiv.org/abs/2512.05119v1) | 纯text/image单模态评分可能漏混排一致性；分开text/image/consistency的人类相关协议为窄评价线索，不以新榜单准入。 |
| [EmbeddingBag DLRM 05831](https://arxiv.org/abs/2512.05831v1) | HBM分片增加communication/sync；H100 NCCL/NVSHMEM随table、pooling、batch等条件比较，潜在跨GPU性能边界，不迁移成任意LLM embedding普遍加速。 |
| [PORTAL 00288](https://arxiv.org/abs/2512.00288v1) | 不可控优化landscape混合多个难度轴；独立curvature/conditioning/interaction/ruggedness并neutralize尺度，可修正优化器比较混杂，潜在评价条件；不授真实训练全景代表性。 |
| [Counting Without Running 04355](https://arxiv.org/abs/2512.04355v1) | CUDA源级算术计数忽略编译/runtime行为；577kernels、8属性ground-truth profile揭示intrinsics/CSE等计数误差，潜在代码性能评价反证；代码能运行与executed FLOPs正确预测分开。 |
| [Q-BERT4Rec 02474](https://arxiv.org/html/2512.02474v1) | 撤回原成熟组合关闭：§3.3、Appendix B Table5、§4.4的per-item融合深度gate与固定层有质量对照及深度/速度代价，需重考虑表示融合计算选择；不授新codec、受控全部归因或通用低延迟。 |
| [LTCS 04009](https://arxiv.org/html/2512.04009v1) | 撤回原购物排序关闭：§3.3 Eq1–6、§4.1–4.2/5.1的联合ranker共享embedding、leaf→master复用改变训练/执行耦合；依query及purchase条件独立且O(K²)只取top40，不授普适独立性或无negative transfer。 |
| [Explainable Reranker 03439](https://arxiv.org/html/2512.03439v1) | 撤回原SFT/DPO成熟组合关闭：§4.2/4.4强KG baseline相对弱base的边际收益不同，且人评p=.22不授相等/对齐，需重考虑质量与成本验收；不推广所有reranker失败或人类真值已证。 |
| [WalkRAG 04790](https://arxiv.org/html/2512.04790v1) | 撤回原路线RAG组合关闭：§3.1/Table1中4/10空间完全正确、6部分，结构化prompt精度升/fluency降并遗漏步骤，3个错答与检索失败有关；需分开无幻觉、完整路径及执行正确，不因40问题局部负载删除反证。 |

四项本轮准入修正复用Mill已实际访问的精确v1必要原文与反证位置，见[本日非作者原始复核](./ROOT_ADMISSION_REVIEW.md#精确普通差额5项)；不是本作者重新全文阅读或实验复现。新证据推翻的是关闭理由，不授first-public、Evidence或Books采用；其他有效来源不重跑。

这些精确v1已查提交/评论身份：例如00007 Oct10、00004 Oct5、05119 Oct11、00288 Nov29、05831 Dec5、04355 Dec4，足以证明月号/列表不能直接套日，仍不把提交当公开。03025 v2 Dec4、00968 v2 Dec29仅身份线索，未声称本窗重要修订，采用只指上表v1。

### 明确关闭与窗外下界

完整题摘后仍贡献前关闭6项：00004 TalentSearch是job/CTR/CVR特征抽取+角色MoE多任务组合、本域指标，未改变MoE成立约束；00313 Search学习研究只写研究问题/意图，无具体新受控机制/反证；02502 AskNearby地理/graph/vector外部数据组合及§3.3/4.4本域指标未建立新模型机制。07841 DOD/OOD A* cache/layout测量未建立当前模型runtime的直接约束，不采用一般DOD优越结论。03807 BMF实际题摘有AO/IP、多run rank-one选择及Boolean数据结构，但只论binary OR/AND因子分解在topic/imaging，未建立当前神经模型形成/执行机制或可迁移限制，当前主线关系不足；不是否定其数学贡献。04368 AutoGuard精确v1 PDF III/Algorithms1–2/IV为通用DevSecOps RL/playbook，LLM-assist为future，没有当前模型供应链机制；Alg2低impact分支未明确赋execute仅是静态伪码缺口，不授runtime漏洞或安全已实现。原02474/04009/03439/04790关闭因具名必要原文反例撤回，已归并上表。

IR明确标题范围外只简记00439 PEOAT经典问卷组卷、01171/01179传统CTR/CVR综述/广告benchmark；没有全225项语义验收。PF明确血流/甲状腺/量子等题名不扩当前主线。

PF潜在模型系统标题但v1 submitted在本窗之后：06699 Dec7 07:25Z、07011 Dec7 21:20Z、07449 Dec8、08715/09199 Dec9、09786/09800 Dec10、13176 Dec15、16512/16854 Dec18、19606 Dec22。这是提交下界排除当前arXiv首次公开可能，不证明作者从未更早发布，也未深审这些窗外正文；不扩本窗。

## GLM-4.6V具名原始恢复

[Research?page=2](https://www.zhipuai.cn/zh/research?page=2)的原生RSC payload以JSON parser实际恢复对象144：title为GLM-4.6V native tool use，`createAt=2025-12-07T16:00:00.000Z`，`createdAt=2026-01-07T02:44:32.087Z`，`updatedAt=2026-04-21T04:48:35.168Z`。createAt换算BJT Dec8午夜像日编码，目录文字显示Dec7；不能把这些CMS字段当2025真实上线钟点。[release notes](https://docs.z.ai/release-notes/new-released)只有Dec8。[z.ai Blog](https://z.ai/blog/glm-4.6v)网页和原生均空可读正文，有限替代[官方模型卡](https://huggingface.co/zai-org/GLM-4.6V/raw/main/README.md)核心/limitations实际读，Research payload也有完整同名核心，不反复探空Blog。

潜在增量是图像/截图/页作为工具输入及visual tool output直接返回模型，不先转纯文本；synthetic agentic training与MCP多模态扩展是作者公开机制线索，不证明执行授权/真值闭环。当前model card依赖版本和benchmark图片可能已更新，不能反填2025 artifact。128K、150页/一小时视频不作成功保证，作者明确counting/person recognition、overthinking和纯文本能力限制。日期、精确release与执行协议终态保留；四项重开归并后为21个arXiv家族加GLM共22个潜在家族，不作确定本日候选。

## 日期停止、Books和作者停点

AskSafely announced与Counting December published、z.ai Dec8具名搜索实际未取得个体真实first-public；Counting搜索仅镜像月身份，无日期权限。官方历史list/catchup400、API429、帮助announced月精度/OAI提交字段及表单超时有限恢复已有原始观察，权限仅定点复用，不反复请求同一接口。恢复需上表具体v1的历史new公告/RSS/email或原始首次正文，GLM需原始release时刻/完全落窗区间，不是CMS migration/文件创建/当前README时间。

Books未正面采用日期保留项。GLM若归日，owner `AGENT-TOOL-CALLING` Ch78；实际对读Tool Contract typed input/output及“模型输出只是Proposal”约35–90行，邻接Ch77 memory provenance约35–95和Ch79 belief/action/observation约30–85。已承载权限/事实边界，不据此冒称覆盖native visual serialization新机制；需日期与协议审阅后由root判断是否补Ch78输入/返回表示。AskSafely恢复后由Ch72/Ch78定点比较payload治理，gpuFLOPBench/模拟器评分冲突由Ch66具体scorer/evaluator identity承担；此处不虚称整合。

作者已按Mill具名新原文修正四项并同步集合，普通可执行项0，0个确定落窗家族，22个潜在家族安全隔离及6个完整题摘贡献/关系关闭。隔离均为本窗终态保留项：不用于正面证据、不进入 Books、不支撑无遗漏或性能/安全保证，不计Coverage/Evidence通过，也不是零事件。待Mill定点核重开归并/正式同步，不重复有效全源；作者不授日级通过，metadata/§6由Mill维护。
