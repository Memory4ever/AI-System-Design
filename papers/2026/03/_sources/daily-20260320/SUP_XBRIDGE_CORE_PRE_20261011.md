# XBridge17512：必要原证 / actual owner / 最小 PRE 准备

准备者 resume_review17_18，2026-10-11，仅03-20补03/19。root允许、作者明确未开始此core并分配；原2+2+2=6与完整AB/自然日准入复用本日独核§12。仅准备，交resume_mar17非准备者必要核，不自行授Source/PRE/safe/DAY；未授Books写，不改Report/LS/索引。

## 1. 必要实际原证与停止

[exact-v1 HTML](https://arxiv.org/html/2603.17512v1)实际§3.1–3.3/Eq1–4 L107–147，§4/Table1 L148–214，§5.1–5.6与Limitations直接段L215–281；A.1–4/Eq5–9 L333–368；D.1/Table2 L393–402；必要详细评价仅C/Table6的MetaMath/Llama与Qwen决定性行535–552/558–569、Table7 L570–596、消融Tables8–10 L597–618。没有遍历references、全部untuned/所有语对表、D案例/commonsense或repo/代码/复现，图像曲线只用正文与实际表值不冒像素读取。当前abs/header/完整AB/history轻量实际读：ACL2026 Main/v2说明未见具体纠错/安全信号，不机械全版本diff。

输入先由NMT encoder产生contextual states，经Mapping_enc投影，加英语instruction交给冻结LLM；LLM实际自回归生成英语tokens z，抽倒数第二层hidden，经Mapping_dec作为外部NMT decoder的cross-attention K/V，目标语言token指定输出。不是绕开英语中间序列/直接latent推理，更非移除全部生成或串行费。encoder/LLM保持冻结；stage1训两mapping和decoder crossattention，stage2只训encoder mapping，stage3只训decoder mapping/crossattention。冻结参数不认证新输入分布下知识/功能无回归，不授任意checkpoint或即插即用。

§3.2同一英语文本再经NMT encoder，得到长度不同的两个表示序列，以cosine代价作对齐proxy；“同源故expectation语义等同”是作者假设而非已证明hidden语义保真。A.2 balanced两marginal到A.3实际去掉列约束：每个encoder row可将全质量给cosine最近decoder-side state（ties未规定），下界不保证bijection/decoder覆盖/顺序或跨token真值。只采用两侧表示需额外兼容监督，不授完整OT/Sinkhorn实现、非退化transport或语义等价证明。L198重复lambda2=1与lambda2=6，不能自行纠为lambda3并授精确recipe。

## 2. 关键评价 / 直接反侧 / 费用

四7B/8B LLM为MetaMath、Llama3、Aya23、Qwen2.5Instruct，外部NLLB200-1.3B；10语言，3低资源。stage1 OPUS100英语centric数据，另外3.3B NLLB生成三语target；后两stage数学和XL-Sum也含机器翻译response，不当独立groundtruth/零预付训练。8H800、AdamW2e-5、每stage3epochs/batch128可核；训练精度、输出长度、推理batch/concurrency、完整三stage/mapping/翻译数据/搜索和存储费、latency SLO及seed/CI在必要段Not Disclosed，不用8H800训练设置冒填推理条件。

Table1平均受限改进不授每方向无损：Llama En-Ja25.40→20.12、En-De36.24→35.45，Qwen En-Ja25.76→18.66。Table6英语LLM与decoder的平均MGSM并非完全等价：Meta53.80→52.12、Llama56.72→54.48、Qwen71.80→69.08；Meta某些语言低于LayAlign/MindMerger，不能照录所有baseline均赢。Table7 XL-Sum平均可提高但Qwen English33.52→31.52、French29.14→27.72等反退。metric得分相近不是忠实保留每条推理内容；BLEU/COMET/ROUGE/算术正确不能单独授知识core语言无关的唯一因果。

消融MetaMath/Table8去OT的X-En33.76高于XBridge32.63、w/oDecoder35.41也更高；出向En-X24.27→28.10支持部分generation监督取舍，不支持“去OT全部任务/方向都退”。Table9有stage1必要和joint23低于分stage的有限证据，但与Table6不同列/平均口径（54.84/52.92 vs53.80/52.12）不强行合并；Table10 w/oOT25.48→25.78有限增量，不证明普遍唯一机制。untuned42语言是NMT已覆盖但mapping未调，不等模型从未接触该语言；正文NMT大小/另一backbone只有限可组合，非architectureagnostic定理。

D.1/Table2 training相对SFT speed.91、inference.66（TranslateTest.55、MindMerger.85）；本文确实比LLM-only推理更慢，不称整体提速或全部费用更省。以相对速度表无时长/人口/推理执行配置，不授“moderate/生产tail”数字。保持独立translate-test与原native decoder路径共存，语言/接口漂移或质量回归需回退。

## 3. actual sole owner 与最小差额

适用AGENTS/三合同/Sources/统一prompt/完整ROADMAP/本日README/STOP已独立重载，Books PROJECT/学习/写作上下文与相关LS路由实际读。actual [Ch18 MODEL-DECODER-ONLY](../../../../books/part-02-model/18-decoder-only.md)29–64完整三架构链、190–218接口代价/职责分拆，以及275–310中实际读到的seed外部decoder与hidden/input状态接口；Ch17/19入口与Ch12 110–123初始/上下文表示区分定点读。没有按owner标题假NC。

Ch18现50–52已有原encoderdecoder与merged attention/T5Gemma替代，283已有seed→外部decoder→文本回入main的CoLT，但缺多语encoder→冻结LM英语自回归→LM hidden作为外部decoder K/V的输入/知识/输出三责与不同tokenizer双侧兼容。sole MODEL-DECODER-ONLY原52完整T5Gemma段/marker后、54 Decoder-only标题前两小段；Ch11仍own tokenizer身份，Ch30仍own PEFT训练算法，Ch23无跨模态raw signal，不复制多语语言接口。

## 4. 最小逐字 PRE（等待非准备者核 / 未写）

输入与输出职责还可以分配给已预训练的外部模块，而不重新训练中央语言模型：多语encoder先把源文本变成状态，经学习到的映射交给冻结的语言模型；中央模型仍逐token生成英语序列，再把相应hidden经另一映射作为多语decoder的cross-attention K/V，由目标语言标记控制最终输出。这改变的是语言输入、中央计算与目标语言表达的组合接口，不是省去英语中间生成，也不证明冻结参数使知识能力必然不变。不同tokenizer产生的序列未必逐位置对应；同一中央输出再经encoder得到的表示可提供兼容监督，但相似度与放松匹配不认证语义等价、顺序或全部内容保真。<!-- source-family:SF-2026-ARXIV-2603-17512 -->

这一组合要同时验输入理解、中央结果和最终目标语言表达，不能用平均翻译分数把三者合成一个“语言无关知识core”证书。[有限XBridge对照](https://arxiv.org/html/2603.17512v1#S4)中，一些语言方向及decoder输出仍退步，额外decoder也比只运行原语言模型更慢。两侧映射与cross-attention训练、机器翻译数据、额外encoder/英语生成/目标decoder及接口回归都付费；部署应共同绑定三个checkpoint、两侧tokenizer、映射和取层位置，再分别检查内容保持、语言遵守与端到端预算。语言覆盖、接口或质量不适配时，保留原native生成、显式translate-test或重新适配，而不把外部表达流畅当成中央结论正确。

静态源注：`SF-2026-ARXIV-2603-17512` — [XBridge exact-v1](https://arxiv.org/html/2603.17512v1)§3–5/Limitations、A1–4及必要Tables1/2/6–10；仅冻结LM与多语encoderdecoder的两侧映射/英语中间序列/输出K/V接口及分验边界。relaxedOT非语义等价、lambda/表口径、局部反退/推理变慢与全费用限制保留；未核代码/复现，不授全语言保真或生产性能。

准备者不自己PASS；支持与直接反侧已够此接口采用提案即停止。非准备者若判已覆盖须指出实际具体正文；若有限接口不成立保留明确必要请求/中心隔离，不降分或假EX。

## 5. 非准备者有限 Source / actual owner / literal PRE 裁

resume_mar17，2026-10-11，恢复仅本20合同/路由与Books约束后实际独读exact-v1 §3/Eq1–4及§4/T1 L107–198、§4.2–5.6 L199–272、A1–4/Eq5–9 L333–369、D1/T2 L393–402、必要T6–10 L535–618；actualCh18 29–64、190–218、275–310及Ch17/19入口、Ch12 110–123。不冒全部图像/附件/代码或独立复现。

正式有限 Source/差额/两literal PRE及静态注 PASS。中央英语序列与倒数第二层state、外部decoder crossattention消费可核；固定参数不认证功能无回归。单row约束逐row最小cosine代价即可达下界，无decoder列覆盖/双射/顺序保证，受限兼容监督可分采，未采语义等价/全OT recipe。实际T1方向反退、T6 decoder平均下降、T7语言反退、T8反向消融、T2额外推理变慢均与近文边界一致；lambda2重复与统计口径不得自行修配方。现有CoLT只seed展开后回填，不能覆盖本多语输入→冻结英语生成→外部目标decoder三责接口，sole MODEL-DECODER-ONLY两段位置成立。未授权/未写/未POST，不计safe/DAY；root协调窄锁，writer与nonwriter角色分离。

## 6. 具名窄写与 writer 自读（不是独立 POST）

root在§5正式非准备者通过后授resume_review17_18唯一Ch18窄锁。恢复重读适用AGENTS/三合同/Sources/Prompt/ROADMAP/本日README/STOP及Books学习/写作上下文，actual三架构39–73与末注邻接后按原两literal PRE实际写正文54/56、静态章末源注。writer已完整顺读39–73和末8，原T5Gemma→两新段→Decoder-only及尾部现有来源都保留，正文逐字回§4；scoped实际diff已检查且diff-check0。只有两段及静态注，不作动态验收身份注。尚待resume_mar17一次非writer实际完整局部/本人注POST；不自授POST/safe/DAY，不改Report/LS。

## 7. 非 writer 实际 POST

resume_mar17实际完整读回Ch18 39–73、新54/56及429–437本人437/CoLT与hidden-input邻注，回对§4两literal PRE及§5已实际核必要Source，正式有限POST PASS。原encoder-decoder/T5Gemma共存→外部输入/中央英语自回归/目标decoder职责→原Decoder-only因果生成链顺读一致；相似度/放松匹配非语义等价、方向/decoder质量反退及额外推理费近文，静态注不授实现/复现/全部语言保真。仅新增本family两段及本人静态注，限定diffcheck0；原Book流程身份不重写，root可释放。本项POST不是Report DAY。
