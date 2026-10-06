# 10700 Structured Linked Data：最低关闭判断（待独核）

仅Mar12 BJT补充自然日。完整exact-v1题名/四作者/abstract/Comments实际本次重对，第三独立准入有效；SUP_DATE3_10700.raw原DataCite registeredMar12T02:07:47Z与submittedMar11T12:12:51Z日级夹证已独核，可Mar12，不以Updated代公开。原official https://arxiv.org/html/2603.10700v1，SUP_CORE_10700.raw/txt与manifest/result GET200415865bytes、UTC2026-10-09T16:36:13.855922。未读其他日期/候选或v2，不扩家族history。

## 具体新增命题与评分

原flattext无navigation→本文三document representations×standard/agentic retrieval加Enhanced+，在同349query/4domains比较→局部entity-page可见资料/导航配方的收益与更rich links增量未显著。准入保的是新实验/局部实现，不是RAG/linkeddata成熟组件。拟Design1+Reach1+Durability1=3：页面物化/导航与已有tool组合的局部配方1，单检索负载1，Gemini/WordLift/Vertex当前数据与实现的工程观察1；不把借用的事实保留、factorial控制/同源judge独立性等成熟原则算成长期约束2或设计纠错3。也不因已存在Books、unread或工作量定低分。

本次直接读足决定关闭的§3.1–3.6/Table1、§4/Table2与§4.2–4.4/4.7、§5.1–5.7直接限制；Appendixaccuracy judge prompt实际片段3100–3178。图仅文字，不读全部33pages附录/代码/部署，也不自授实验统计或运行实现。以下原证显示它不能独立支持重要新机制或稳定替换方案，故拟3分已关闭/不进一步采用，非贡献EX、非外部受阻；不新写Books，也不认证该新实验已被现文吸收。

## 决定性原证与不能采用的外推

§3.3 Enhanced同时新增KG派生natural-language summary、JSON-LD、可见relatedentity links、llms-style instructions、neural-search skill和breadcrumbs。§5.4/5.5明确**也materialize baseline只以URI指向的邻居事实**，未做same-facts ablation。配方改变呈现、信息量和工具affordance，不能单独称JSONLD/导航新算法作用或+29.6%纯格式效果。文中llms-style指令只是页面数据，无可信执行/授权规则，不因可读给它权限。

§3.4 standardtopK10一答，agentReAct三tools最多2hops；§3.1称text-embedding005，§3.4/5.5实际又称gemini-embedding001，具体embedding身份需对回。§5.5 flattext~20k chars截断：82%plain/88%JSONLD超限，JSONLD起点median18510，常部分或全部不进index。因此本pipeline下small JSONLD结果不证明parsedstructured ingest或其他RAG格式本身无用。§3.5 KG生成groundtruth与Enhanced物化同资料，作者承认可因信息/文本近答案获得高分；Gemini家族query/generation/judge共源，未做人审或独立锚点。

实际2443 evaluations，C4一/C5三error排成2439，不把全部349每condition自动当相同有效paired人口。Table2 C3 accuracy4.69≈C6 4.70，C6+4.85，richlinks102.2/可见而只follow.4，未充分报告完整query/prefill/API费用与独立gate；平均fewerlinks不能授净latency/效率SLO。C6→C6+报告p_adj1/d.08未显著，不能因headline最高score当新navigation层必需。

文本/Table4 pairedΔ与Table2 mean不一致：C2(3.89)−C1(3.62)=.27而原Δ.17、completeness3.33−3.01=.32而原Δ.18；C6+(4.85)−C6(4.70)=.15而原Δ.06。C1/C2均无报告excluded errors，不能用四舍五入补出这些差，若另paired人口必须原样注明；不自行更改作者统计或推造假。§4.2准确率称statistically significant p_adj.024，§5.1/5.3又称no measurable benefit，只保“效应小且本特定ingest缺段”，不授严格null。Grounding只C1–3，agentic动态证据集未评，答案正确不认证retrievedfaithfulness。§5.6 same-visibledata不证明更抗操纵/真实事实/同URI各时刻同版本，也不是新安全控制。生产AI Mode/真实搜索可见性只是类比，未执行生产验证。

## 不进一步采用与owner边界

ROADMAP AGENT-RAG Ch76（实际路径books/part-07-agent/76-rag.md）是检索表示唯一owner，Ch77不因题名memory收。实际Ch76 75–108完整document/query/answer分层与结构/信息budget、entity/heading导航只proposal；Ch66 3910–3929完整first-loss→behavior归因接口具体已在。它们不是本稿具体数据已覆盖/新实现吸收，但本文未额外确立超出局部配方的新可验证机制或可靠适用边界；缺same-facts/相同可见span的解析对照、不完整agentgrounding/metadata身份和不一致统计，不采用强替换/格式因果/普遍安全效率。这是实际新增命题范围的3分关闭，不按topic相似免审，也不按未读附件外部隔离。

若后续确有同可见事实/截断校准、parsed-vs-flat接口对照、真实agent证据集及完整成本匹配，并提供具体新选择/恢复条件，可重开相应新增命题；本次不为了确认这些未来可能机制扩大附件。正式还需非作者核身份/date复用、实际贡献/评分及具体不采用理由，当前不改Report候选/分数，也不授DAY。
