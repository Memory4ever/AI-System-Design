# MEDiC `2603.29009v1` — 语义 teacher 下 mask/loss 的局部反側

root完整AB与必要§3–4/Table4–6实际核通过，`2+1+2=5`。实际读v1完整必要§3/4，[原件](SUP_MEDIC_CORE_20261013.json)；未读全26configuration附录或代码，未复现。正常复合日门与owned上界见 `SUP_STANDARD_DATE_SIGNALS_20261013.json`。

## 只保具体新增，不借成熟组件评分

CLIP ViT-B/16 frozen teacher看完整图，ViT-B/16 student看masked；patch-SmoothL1、CLS-softmaxcrossentropy、pixel重构三项都是已知监督组合。实际可改选择的是在这类teacher/student人口里，更“语义连贯”的evolved mask未必更好，以及全局loss权重很敏感；不用三loss名字或整体榜分自动准入。

§3 HC新增在attention distance中混relativepositionbias、average-linkage，按训练epoch的alpha从grid转cluster；这是已有evolved mask的局部变体。Sparse student仅visible token，decoder重建masked；dense加masktoken，全局loss权重彼此耦合。Equation/bias归一化细节不充分，本次不声称完整clustering实现已核。

## 必要负对照与人口边界

ImageNet1K，CLIP teacher/ViTstudent，300epoch/40%blockmask/B2048/AdamW；硬件/precision/seed/repeatedrun及uncertainty Not Disclosed，300epoch不含teacher既有训练，不能据无teacher800epoch行推净训练效率。

§4.5Table5明确blockmask kNN68.59，evolved-EM47.52、HC64.56；正文26config sweep仍不追平，Fig6另best64.93。此mask对照的block分母是68.59的patchdistill基线，不是默认三loss73.92整系统，不能说所有MEDiC或其他语义teacher都无需semanticmask。原文“teacher已编码语义故redundant”是解释，没有隔离teacher语义内容的因果干预，采用的是受限负对照而非证明该原因。

§4.4pixelweight0.01附近与CLS0.30附近很敏感：pixel0.005为54.19，CLS0.20为56.05，对各自不同loss人口不能直接拼成一种同trial跌幅。DLW0.5为61.57，不称全局统一17pp；局部调参结果不授普遍最优权重。§4.3三loss73.9优于本表patch+CLS72.3，但§4.6 sparse Token+CLS75.7反而高于triple73.9，说明objective/mode条件不能漏；不采用“所有组合中三项最强”。

Fine-tune85.07 vsMaskDistill84.89只有0.18pp、无uncertainty，不说显著；ADE20K Table3 MED52.5低于Mask53.8，§4.1FCN/frozen与Table3UperNet/endtoend协议描述不一致，不能给精确跨protocol因果收益。Sparse更少token有数学算量变化，不等linear实际训练或Serving加速。

## 拟结论

条件性mask负证与loss/mode敏感可留，semanticcoherence不是独立质量验收；不采teacher redundancy普遍因果、三loss全胜、净训练省epoch或production收益。Books具体NC：owner MULTIMODAL-REPRESENTATION Ch23 316–318承载重建/teacher目标及consumer分别验收、非天然互补，117–119承载classification/CLS读出不等dense grounding；本轮受限loss/mode反侧支持这些实际判断，不给局部排序另写通用recipe。root已实际读308–322/111–121完整正文，NC5通过；不称覆盖paper全部或实现复现。
