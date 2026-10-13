# DaPT19097：双语子问题检索与融合图保证分开

resume_mar18 sole准备，只本03-21补BJT03-20，复用完整题摘/root有限准入及必要先公开门裁，不扩query/venue/附件。尚待非准备者Source/date/actualowner/onePRE裁，无锁未写未safe/DAY。

## 身份、日期和贡献

实际[official exact-v1 abs](https://arxiv.org/abs/2603.19097v1)八作者/header/history与完整AB，current仅v1，未见明确withdraw/correction。Accepted ICASSP2026只是书目/会期信号；root已独核后发Crossref createdApr21/issuedMay3，不能把accepted当窗前正文公开。真实DataCite findable currentversion1，v1Submitted03-19T16:23:04Z、v1Updated03-20T01:13:18Z、created03-20T02:28:33Z/registered34Z，Available仅月份；沿本批BJT20日级夹证有限归属，不补精确公告或宣称别处从未公开。

仅按查询语言检索/统一翻译会丢失另一种表示的子问题与支持→原语言和英语各自拆问题，再对被选中的双语子问题分别检索/生成并判断→新增双表示与检索人口接口，而非英语天然更可信或多hop图必可靠。拟2+2+2=6；不是成熟“多源验证”借用原则计新分。中心全图recipe与受限接口必须独立裁定，不自行绕过。

## 必要原证和直接反侧

实际[exact-v1 HTML](https://arxiv.org/html/2603.19097v1)§2.1–2.3/Eqs1–4 L60–125、§3.1–3.3/T1–2 L128–153及结论；支持与直接反侧已足，不读引用全史、代码或遍附件。

- 两种语言各自LLM分解为依赖DAG；以跨语embedding最大cosine≥τ配对子问题，重定向全部入/出边、删除英语节点，最后拓扑排序。单语node读同语corpus，双语node分别检索生成候选；Judge比较一致/充分，两个valid时优先原语，否则以已有路径ReGen，最终子问/答案链与原query检索材料共同读入generator。
- 原§2.2没有披露合并后的cycle guard。自己的结构反例：原图a→b与c→d均无环，若相似度错误配成a~d、b~c，合并后出现双向边；各图无环不证明相似度合并后无环。Eq3只组合紧邻前一答案与下一node，不等于任意multi-parent dependencies全部传递；图保证与完整recipe不采用。LLMJudge一致也可能来自共享翻译/检索错误，重生成“until succeeds”未明确有限次数或可靠成功判据，不能据此授终止/事实支持。
- 评价是三英文validation集合各抽1000、GPT-4o-mini翻译Sw/Th/De/Es/Zh，同默认LLM和BGE-m3、同corpus；作者称实体规则与人工检查，但未披露检查人口/差错率，不能认证自然低资源任务。HippoRAG2 topk5、其他baseline3，τ.8；8×3090不等端到端模型/API/设备、precision/concurrency/SLO及全部预算已闭合。
- T1 Hotpot平均EM46.8>43.6但F1 57.1<58.1；2Wiki平均EM50.1>48.7但F1 57.5<58.1，多个语言/指标反退。MuSiQue F1平均改善仍Sw/Zh/En反退。T2无fusion与TranslateQ&A较低支持受限双表示分支，却没单独控制全部query/生成/Judge重试预算或证明graph fusion唯一因果。没有多seed/CI、明确失败循环与全费用；EM/F1取舍不能外推全面更准/更简洁或稳定可靠。未核实现/复现。

## Actual sole owner差额

`AGENT-RAG`/[Ch76](../../../../../books/part-07-agent/76-rag.md)。实际完整640–695、多语言665–671及1235–1284 querypolicy/evidenceDAG/logicalplan交接顺读，Ch75/77开篇实际读。665–671已有按证据语言拆candidate/reranking/support、离线oracle非selector及reasoninglanguage分责；1256–1273已有traceDAG/provenance与logicalplan，但均未解释原语言/英语先独立拆子问后各自query/answer的双表示接口。不能只因“多语言/图”主题相同判NC，也不能为不可信融合图强造通用planning模块。拟671完整后/QueryRobustness标题前one段，仅裁受限双表示检索是否可独立采用；全graph recipe/无环与终止保证中心隔离。

## One literal PRE（待非准备者裁）

另一条受限分支把问题的原语言与英语翻译先独立拆成子问题，再让配对后的两种查询分别检索并产生答案候选，而不只在同一候选池里改语言排序。子问题配对只能提出合并建议，须保留各自的问题、依赖、检索文档与语言身份；两路答案一致只是一项核对信号，不能替代原文支持或把英语路径升级为事实来源。[双语子问题对照](https://arxiv.org/html/2603.19097v1)支持这一替代接口，但相似度重定向两图的边不保证融合图仍无环，紧邻前一步的答案也不等于保存全部父依赖；因此不能由成功拓扑排序或judge通过认证完整多跳推理。原题翻译/抽样人口、top-k与额外检索、拆问、生成和重试预算须分账，平均EM改善仍有F1及语言切片反退；配对不稳、依赖冲突、支持不足或预算触顶时，保留两份未合并路径、固定单语/跨语检索与独立support gate，或明确拒答，不以反复生成直到通过自签可靠性。<!-- source-family:SF-2026-ARXIV-2603-19097 -->

拟本人静态章末注：

- `SF-2026-ARXIV-2603-19097` — [DaPT exact-v1](https://arxiv.org/html/2603.19097v1)，必要§2.1–2.3/Eqs1–4、§3.1–3.3/T1–2。仅原语言/英语独立子问题与双检索候选接口；相似融合无环、完整父依赖/重试终止、judge真值与全费用不获认证，译题人口/top-k混杂及EM/F1、语言反退近文。未核代码/复现。

交root非preparer一次必要Source/date/actualowner/onePRE裁，中心完整recipe是否与这段有限接口独立分采需明确裁决；不自授锁/写/safe/DAY。

## root 非准备者有限裁

作者获root soleCh76窄锁后逐字原onePRE落实673/静态1756，实际完整655–684及末六行回读与scoped diff-check0；旧多语言/推理语言→双表示子问→queryrobustness衔接保持。源注仅原证/范围/边界，不加动态验收身份；待root一次nonwriter完整正文/邻接/本人注POST，未先计safe。

实际打开 exact-v1 §2.1–2.3/Eqs1–4、Table1 全语言/指标与§3.1–3.3/Table2直接反侧；必要日期与身份的本批已核结果复用，不扩会期/检索历史。实际 Ch76 655–677、1253–1275 完整局部确认现有语言切片、reasoning language 与 trace DAG 未拥有双语分别拆问后的双检索接口。单图无环不推出相似节点融合后无环，紧邻答案不等全部父依赖，Judge 与无界重生成不提供事实/终止保证；其融合后的实验只能为有限接口提供受限案例，不能孤立证明双语拆问的唯一因果收益。One PRE 明确保留这些反侧与译题、top-k、额外预算和 EM/F1 分项代价，没有把未验证的图保证转移给通用规划。

必要 Source/actual owner/one PRE 有限 PASS；准入6分不因全graph强claim受限而降分/删除。授作者 sole Ch76 本 family one PRE及本人静态末注窄写，之后 root 实际完整局部与本人注 POST；尚未写不计safe/DAY。

## root 实际非写者 POST

实际完整读回 Ch76 655–684 及末六行，原 one PRE 新673及本人静态注1756均落实。前接 query/evidence/output/reasoning 各语言分责，后交 Query Robustness；双语拆问/分别检索不替代已有语言候选切片或图的 provenance 责任。融合无环、完整父依赖/终止与Judge真值仍未获认证，原Source/PRE有限接口、语言/指标反退与预算代价未扩大。actual POST PASS，接纳第39项实际整合/45安全处置，释放本 family Ch76锁，仍不授 DAY。
