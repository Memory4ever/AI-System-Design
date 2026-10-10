# 2603.08942 — 上三角双线性评分，不继承硬等距（ready）

[BiCLIP exact-v1](https://arxiv.org/html/2603.08942v1)。作者实际完整§4–6/式4–8/Tables1–4，包括非正交澄清、identity初始化、评价、直接消融；未核Fig3像素、repo/复现或全部引用。读取方式为同日supplement_html.py URL S4 S5 S6，stdout，不声称存在全文CORE缓存。batch4 exact-v1完整題摘/current comment/history与原日期字段实际核；v2接受状态/同摘要不自动重要修订，本窗仅v1，未见当前withdraw/correction。

原Submitted Mar09UTC21:26:15是Monday18UTC截止后机会线索，不能单独充公开；官方availability实际L170–186 noadvance finalID/DOI与Tuesday20EDT公告规则给最早Mar11BJT08下界，owning arxiv.content/findable registeredMar11UTC02:01:42为已可发现上界，同BJT日夹证，不伪造精确公告时刻。定点首稿轻核：[作者主页](https://pmantini.github.io/profile/)实际news L20–21为Mar27接受/Mar26项目页，selectedpublication同标题/两作者/arxivID；[正式workshop接受名单](https://dg-ebf.github.io/2026/accepted-papers.html)实际BiCLIP同题/两作者。没有更早具体公开冲突线索，不把接受、搜索crawl或主页列表缺项当绝对首公开证明，不追完整repo史。

2+1+2=5，唯一MULTIMODAL-REPRESENTATION。小样本监督适配的bilinear score/上三角结构及正交代理边界是具体差额；不是把同域分类提高等同全域canonical恢复。必要gap加深但不采用理论普遍claim。

## 必要机制与直接反侧

§4实为iWtᵀ，冻结两encoder，用W=I初始化，改变双向softmax/sigmoid交互评分；D(D+1)/2可训练数仍二次，不是rank小或D线性。§4.2明确不是纯orthogonal rotation。行向量乘上三角W时，第k输出依赖前k输入，与原文“only subsequent dimensions”方向不一致，不照录维度依赖或实现已核；零对角也可奇异，上三角/identity初值不硬约束训练后可逆/长度/角度。§5.3只保证初始score相等，不能保证训练后原任务保留。

§6.3/T3使用||WᵀW−I||F / D。作者独算反例：D=512，W=diag(2,1,…,1)，该量3/512=.005859375仍小于报告Food101 .006，但第一轴长度翻倍；W=diag(0,1,…,1)则1/512=.001953125而方向被完全删除。因此小平均值不认证worst-direction等距或恢复原语义；不否定有限经验关联或§4的非刚性承认。原文Table3 .022均值不转成硬保证，KDE positive/all及每图随机5negative、Simpson overlap不是校准/内部因果/完整错分数。

§5 actual CLIP/SigLIP ViT-B16（512/768）、AdamW1e-4/WD.1、20–50epochs/2080Ti、1/2/4/8/16shot/fulltest；batch/precision/seed重复CI/完整runtime与SLO未披露。Table1两backbone各与零样本比较都加了标签和训练，不能唯一归上三角或匹配全部prompt参数/预算。Table4 random Dense→Tri在DTD69.63→69.57/Aircraft44.88→44.55退步；identity Dense→Tri在三个切片更好，机制效果须依赖初始化/任务而非无条件每域结构最优。Table1 DTD71.86与Table4 identityTri71.01冲突保留，不自修。少参数不等训练/编码/测试便宜：标签锚、encoder feature/cache、D²矩阵打分、优化、调参及原任务/跨modal消费者回归全部计费。

## actual owner 与逐字PRE

作者实际Ch23 64–94完整latent map/Procrustes/跨模态等距/少锚softOT/pivot邻接和Ch22/24开篇。原正文有“软几何变形不继承正交保证”，但缺少单一空间内identity初始化上三角bilinear评分与维度归一化正交proxy的具体分支。拟仅在2602.17584完整两段后/少配对softOT前插两段，不改原kernel条件、Procrustes/真实配对退路。

拟段1：

若目标不是把两个 encoder 接到共同坐标，而是在冻结的 image/text 空间中适配少量有标签的目标域，还可直接改交互评分：把点积换成 image·W·textᵀ，以恒等矩阵初始化 W，随后只训练上三角部分。这保留初始分数，并用结构减少可训练自由度；它是依赖坐标基的监督适配，不是从少量锚点证明全域存在唯一正交映射。上三角矩阵仍可缩放、剪切或变奇异，恒等初值也不保证训练后的角度、长度、语义与原任务不变。

拟段2：

[受限双线性对照](https://arxiv.org/html/2603.08942v1)支持这一小样本评分分支，不支持无损 canonical 恢复。上三角结构在不同初始化与任务下并非总能改善；用维度除过的平均正交误差较小，也可能掩盖单一方向的强放大或丢失，须分别核原任务、目标任务与真实消费者，而不把分类准确率或正负角度分布当硬几何证书。锚点标签、encoder forward/缓存、二次规模矩阵打分、训练与调参、跨任务回归均付费；任务失配、几何漂移或费用不合算时，保留原点积、纯正交 map 与真实配对适配，不由初始化批准默认迁移。<!-- source-family:SF-2026-ARXIV-2603-08942 -->

root必要Source/date/PRE通过，作者仅窄写Ch23 85/87及自身1265，root非writer实际完整共同坐标→isometry→bilinear→softOT/pivot邻接及本人末注回对必要原证/PRE，actualPOST通过、旧段保留、锁释放。计新增第33，非DAY；不授全图/代码/复现。
