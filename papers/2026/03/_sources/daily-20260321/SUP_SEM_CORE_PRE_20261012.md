# SEM19028：查询相关性与偏差敏感性的稀疏表示调制

root 准备，仅03-21补03-20自然日；复用本日65完整题摘独立准入校准，不扩发现。尚未非准备者 Source/owner/PRE 裁定，不自行写书或计完成。

## 身份与具体贡献

[exact-v1](https://arxiv.org/abs/2603.19028v1)原题摘、当前header和版本已核，未见明确撤回/纠错信号；DataCite created/registered03-20T02:26:55Z、v1 Updated03-20T01:08:55Z 与本批公开日夹证一致。后发 CVPR Findings 正式版本为2026年6月，不将它当3月之前的首稿；不以 Submitted03-19 单独判公开日。必要早稿身份门已单独关闭，具体依据保留于本日 FIRST_ADMISSION。

硬投影可能连内容一起删去 → 在固定 SAE basis 上分别以查询/中性描述和各偏差类/其他类的激活对比提出两种评分，再软调制和重建 → 重新考虑“一个全局删除方向足以保内容且去偏”的表示接口。拟2+1+2=5，新增为局部 dual-encoder 表示消费者的对比/调制边界，不给通用 SAE、公平性理想或所有 VLM 额外分。为补此具体长期机制缺口，必要审阅加深，但不遍历全附录。

## 必要原证、支持与反侧

root 实际读[exact-v1 HTML](https://arxiv.org/html/2603.19028v1)§3.2–3.5/Eqs2–11、§4.1–4.4及 Tables1–4。冻结 CLIP 两 encoder，在最终 text embedding 上训练 MSAE；query neuron score 是相对多样中性 prompt 激活的 percentile，bias score 是每一类相对中性/其他偏差类评分的 min，再跨类 max。可选 paraphrase median 与原 query 输入不同；SEM_i 用 concept²，SEM_b/bi 用(1+concept−bias)²，后者可大于1。Eq11因此可外推，不是始终凸混合、全程非负或严格删除；中性描述由数据/语言定义，不是客观语义原点。§3.2各组其他概念分布相同是假设，不可推广所有部署人口。

两 CLIP 主干、每主干8.5M CC12M-cleaned caption的16384维 SAE，10-fold；每fold测试人口拆50% reference/50% evaluation，不把有标注 reference 的方法当相同 zero-shot输入。检索 KL/MaxSkew@500、Precision与分类 mean/worst-group/Gap分别验。Table2 UTKFace race 的ViT-B SEM_b/bi 均有KL/Skew反退，ViT-L gender也非全部更好；Table3 SEM_i 在CelebA平均及worst-group退步，Waterbirds worst-group改善可伴平均accuracy降低。Table3/正文Waterbirds .684/.676不一致，不抄headline；Table4某单评分消融在Waterbirds比full更高、CelebA稍退，不授full普遍支配。无需恢复所有像素或baseline代码即可支持有限调制接口与直接反侧。

主文未披露全硬件/precision/端到端时延、并发或SLO，当前不采用性能数字。SAE训练/重建、中性及偏差prompt、paraphrase、评分与校准有费用；query-relative activation不识别真实因果/纯语义，也不证明内容无损、通用公平、生成安全或跨模型迁移。未核实现/复现/全附录。

## 实际唯一 owner 与差额

sole `MULTIMODAL-REPRESENTATION`/[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。实际1148–1205完整：硬SVD子空间净化、视觉补空间门控，以及matching image-caption共训dictionary/能量mask已有覆盖；后者并未拥有query相对中性与bias相对其他类的双评分/软重建。拟在该SAE能量净化完整两段后、理解与生成tokenizer分工前补两段，保持表示净化论证。不改Ch12/模型通用Embedding，不把公平benchmark分工复制到Ch66；Ch22/24交接未变可复用。

## 两段 literal PRE（待非准备者）

稀疏 dictionary 还可以只提供固定坐标，而让每次查询决定怎样调制它。一条受限 dual-encoder 分支冻结原文本和图像 encoder，在最终文本 embedding 上训练 SAE；把当前查询的每个稀疏激活与多样的中性描述比较，提出内容相关性，再把指定偏差类分别与中性描述和其他偏差类比较，提出偏差敏感性。两个评分随后共同控制激活放大或向中性基线回落，再由 decoder 重建查询表示。这不同于删除一个全局子空间或按跨模态能量固定 mask：修改依赖当前查询、描述人口与选定属性，而不是由一个方向批准纯语义分离。调制系数也可能大于一，因此该回落公式不总是凸插值；中性描述和较高激活都不是内容真值或因果证据。<!-- source-family:SF-2026-ARXIV-2603-19028 -->

[受限 CLIP 对照](https://arxiv.org/html/2603.19028v1)支持这种软调制接口，仍需分别验检索内容、各群体结果和原模型回归：worst-group 改善可伴平均准确率降低，部分检索公平指标也退步，不能以一个 gap 或总体均值签发内容无损。SAE 训练与重建、描述构造、可选改写、评分和校准均付费；原 embedding、完整重建与调制后重建应分别作为比较对象，使用标注参考集合的方法也不是同一输入合同。描述失真、群体分布或 query 支持改变、内容与属性仍纠缠时，保留原表示、显式条件读取或经验证的投影/adapter，不把稀疏可读性当通用公平或生成安全保证。<!-- source-family:SF-2026-ARXIV-2603-19028 -->

静态注：

- `SF-2026-ARXIV-2603-19028` — [SEM exact-v1](https://arxiv.org/html/2603.19028v1)必要§3.2–3.5/Eqs2–11、§4.1–4.4/Tables1–4；仅固定SAE坐标上的query/neutral与bias-class双评分软调制。保M>1非凸插值、中性代理/组间假设、平均/worst-group与检索反退、不同reference合同及全费；不采内容无损、纯语义/因果、公平/生成安全或普遍最优，未核代码/复现。

请 resume_mar18 非准备者一次核必要Source/actual owner/两 literal 与本人注；支持与关键反側够即停，不重新深审整个历史。未授写入或DAY。

## 非准备者必要 Source / owner / PRE 裁定

resume_mar18 已独立重载本日适用合同；实际打开 exact-v1 官方 abs 完整题摘/current header/history，并取得 DataCite 原字段：created/registered `2026-03-20T02:26:55Z`、findable、v1 Updated `2026-03-20T01:08:55Z`、Available 仅月份。复用本日已裁的后发 CVF 日期门，与本批日级夹证一致；不把 Submitted 等同公开、不声称别处从未公开。

实际读 v1 §3.2–3.5/Eqs2–11、§4.1–4.4/Tables1–4，回对两 literal PRE 和静态注。Eq11 的 SEM_i 重建输入可用 paraphrase median，SEM_b/bi 则使用原 h_q，二者不是相同输入协议；PRE保留可选改写成本且不发布统一精确 recipe。M 的平方可使其超过1，因此软调制不认证凸插值或非负激活。Table2 的 UTKFace ViT-B race反退、Table3的CelebA SEM_i反退及Waterbirds mean/WG取舍、Table4单评分并非全面弱于full均成立；正文/表Waterbirds .676/.684不一致只保反侧、不采用争议headline。组间其他语义分布相同是条件，描述中性与高激活不是内容真值。无需无关附录、代码或全历史即可支持此受限接口；未复现、不采硬件/端到端性能或通用公平保证。

actual sole Ch23 完整1148–1208及Ch22/24开篇已顺读：1177硬SVD删除、1179补空间门控、1181–1183共训dictionary/能量mask仍未承载query/neutral与bias/其他类双评分的软重建差额。拟1183完整段后、1185理解/生成tokenizer分工前，两PRE自然顺承且保旧路径。2+1+2=5与新增局部消费者接口相符，不给成熟SAE/公平理想额外分。必要Source、actualowner、原两literal及本人静态注正式有限 **PASS**；无须改PRE。未写、未授POST/safe/DAY，由root协调唯一Ch23窄写后再一次nonwriter实际POST。

## 一次非 writer actual POST

resume_mar18 实际顺读 root 窄写后的 Ch23 完整1174–1207，新1185/1187两正文及末9行、本人静态注1740与邻注；逐字回原两literal/static及上节必要原证，局部 diff-check 无输出。固定SVD/补空间/能量mask→query相关双评分软重建→理解生成tokenizer分工顺承；M>1/中性代理、检索与mean-WG反退、不同reference和全部费用、原表示/条件读取/adapter退路均完整。有限 actual POST 正式 **PASS**，送root接纳释放soleCh23；不改静态注流程身份、不授整日DAY。

## writer 实际落实

root 仅按本 family 的 Ch23 窄 ownership 将上述两段 literal 写在原 dictionary/能量 mask 完整论证后、理解/生成 tokenizer 分工前，并把本人静态注放在章末。实际顺读1174–1204及末6行，批准稿、旧硬投影/视觉门控/能量净化与 tokenizer 交接均保留，局部 diff check 通过。交 resume_mar18 一次非writer实际 POST；本步骤不自授写后验收或日级完成。
