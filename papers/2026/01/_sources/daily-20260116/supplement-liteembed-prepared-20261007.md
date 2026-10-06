# 01-16 / LiteEmbed 必要原证与owner差额

后续实际状态：root必要原证/actual owner PRE通过并授窄锁；作者已写Ch23两段635/637及自身末注、完整邻接顺读；root非作者实际独读627–652完整局部邻接/新正文及自身末注POST PASS，Lite锁释放。下文“待PRE/拟写”保留原提案过程，不是当前待办。不授日级Gate/实现/复现。

待root独立准入/必要原证/owner PRE，未写Books、未授锁或DAY。exact-v1 abs09661/HTML/date已保存；normalcohort Jan15下界＋registeredJan15T02:51:19Z公共存在上界条件限定Jan15，不等注册为首公开。原abs/HTML无直接作者project早正文声明，未全网追史。

## 决定性机制与反侧

§3.1–3.4/4/Table1–2、A3–A5与决定PCA解释的A7已实际读。image-alignment-only新token优化可让anarsa单类100%，加入相似malapua后前者30%、semantic邻域漂移；不是罕见类别名本身贡献。LLM提出coarse标签与visually similar fine候选，CLIP-image过滤候选；在合并的text neighborhood做局部PCA，以较高方差方向的coarse anchor与较低方差方向的fine-negative separation配合imagealignment，优化新text token而冻结原CLIP。PCA只是受限类别几何分工，未证明跨encoder/任意语义普适因果或LLM候选是本体真值。

Table2 alignment-only cosine.65/accuracy45.3，加coarse后.48/52.6，加fine后.39/69.1；增大alignment不等提高discrimination。累积消融不单独识别全部loss交互，A7仅75classes/5broadgroups，PC1跨类比5.02而PC2–5均1.62，是有限split依据；主文与附录k记号口径不强行统一成通用配方。NOVA5集由LLM选post2023classes+iCrawler/Bing每类50图，emergence不证明未进CLIP预训练。8集常规4shot与continual单类4shot、五randomorders分开；少量结果不授不遗忘/文化全覆盖。

CLIPViTB16（detectionViTB32），Adam1e-4/warm1000/5000steps；hardware、precision、batch及整体训练/LLM/PCA/下游时延成本Not Disclosed。所谓training-free只是不重训CLIP，新token确实优化，不采用零训练headline。IFD无maskGT，nonzero coverage不是mask正确；UECFood100才有maskIoU.43→.71，检测报告mIoU非AP。Generation§4.2明确把imagealignment换为TI reconstruction loss，不是未变classification token直接保证生成兼容。A4 TI8–10类benefit到13类后反转、80类34.9低base44.2；A5直接meanimage4refs有3/7类回退，纯image参考不能自动获textcomposition。

评分2+2+2=6；已确认具体“适配时alignment与跨类别discrimination分工”owner缺口，拟采用则受影响内容深入，不读无关全附录/后版本/代码。未复现。

## 实际owner差额与拟窄整合

实际读Ch23 stage2 L59–89的encoder/map、imagecosine不授text迁移；L626–660完整reliability交接、alignment开头/caption+sceneIR，已有projection兼容、全局对齐/像素或reconstruction不授语义，但没有新增概念texttoken的coarse/fine分工和竞争类别扩展反侧。Ch12专注language token lookup/tying，不移跨模态几何owner。拟在Ch23“对齐不是把向量拉近这么简单”后、Caption小节前两段，仅本节＋自身note，待root实际PRE/窄锁。

冻结原视觉/文本 encoder 后，为新概念优化一个可读的 text token，比重训整套模型更容易局部更新；但只把 token 拉向几张参考图，会让相似类别一起吸向相同视觉 cue，既损伤区分度，也改变原语义邻域。一条受限分支先以语言候选和视觉过滤形成局部 coarse/fine 邻域，再在其 PCA 方向上分别约束粗语义锚与细粒度负例，同时保留 image alignment；这改变适配目标的分工，不是把相似度最大当成新概念已学会。[LiteEmbed的局部对照](https://arxiv.org/html/2601.09661v1)中，更高image-text cosine并不对应更高分类准确率；较高/较低方差方向的语义解释仍只由有限类别支持，候选与encoder版本改变后须重新验收。<!-- source-family:SF-2026-ARXIV-2601-09661 -->

这个接口保留原CLIP路径，却仍支付候选生成、PCA与每个新token优化费用，并需分开回归原类别、竞争类别扩展与下游consumer；冻结backbone不等零训练。没有mask真值的非零coverage不能证明定位正确，生成用重建目标替换alignment也不是同一个token产物无损通用。邻域误导、语义/区分度退步或费用不合适时，保留base text token、直接参考图检索与已验证的prompt/adapter；需要生成时另签训练目标和decoder接口，不以分类或检索收益自动授完整多模态兼容。
