# 10470：必要Source、实际owner差额及收紧PRE独核

复核者：mar13_admission_review（非准备者、非Books writer）。仅2026-03-13既有Daily补充Mar12北京时间自然日。启动重读AGENTS；当前Research/Report/Prompt、Sources每日及arXiv边界、本日停点已实际恢复。完整v1题摘与日级日期有效独核复用，不由Submitted/CVPR接受信号代签首次公开或扩大会议库。

## 真实核验范围与身份

实际读[准备包](./SUP_EVIDENCE_10470_HANDOFF.md)后，回[精确v1 HTML原件](./SUP_HANDOFF7_SOURCE_10470.raw)及完整必要提取文本§3.1–3.2 Eq1–11、§4.1–4.9、完整主Tables1–5及§5固定offline projection/future adaptation限制（txt330–2045）。实际公式保留原TeX，不用摘要代替方法。身份为 *Fighting Hallucinations with Counterfactuals: Diffusion-Guided Perturbations for LVLM Hallucination Suppression*，Hamidreza Dastmalchi、Aijun An、Ali Cheraghian、Hamed Barzamini，arXiv2603.10470v1。

[GET结果](./SUP_HANDOFF7_FETCH_RESULT.json)对应https://arxiv.org/html/2603.10470v1、200/370007 bytes、2026-10-10T04:33:36.339517Z。实际完整核[精确abs题摘/Comments/history](./SUP_ABS3_10470.txt)，保留CVPR2026身份信号；本次不作所有版本diff、全作者/会议检索或证明全网无更早稿。没有使用图像幅度推断：Fig7–9只核直接正文所述反侧，不认证未目视曲线值；不扩九图、全部附录、代码或生产实现。

实际顺读[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)当前108–144完整局部，包括MOH/SCR/attention proposal、VLI两段、One Token两段、音频差分两段与多层readout交接。ROADMAP唯一owner为`MULTIMODAL-REPRESENTATION`；离线diffusion制图属于producer背景，不把LVLM消费者责任重复写Ch24。

## 原证支持的新增命题

§3以COCO训练集5000图/正确caption为校准人口，GPT生成错误caption用于SD1.5视觉编辑，每图5个noise-seed变体。隐藏表示提取时仍消费不变的原caption；Eq6先按caption tokens均值，Eq7再按五个变体均值，然后编辑图表示减原图表示。Eq8跨样本堆叠差分矩阵，Eq9 SVD主要右奇异向量形成逐层固定bank；Eq10–11每个生成步骤在指定层执行`h−V_r V_rᵀh`，不在未来每个请求重做diffusion。原文称hallucination subspace不认证自然错误唯一因果或结构/语义严格保持。

真实差额是跨校准人口的视觉反事实差分制备与未来在线投影消费者分离，不是SVD、正交投影或“表示不是真值”的成熟原则。Eq8没有中心化，因此主要奇异方向反映该差分矩阵能量，不必等同统计高方差方向。

## 必要收益、代价与直接反侧

500 COCO验证图/三个runs；LLaVA1.5、MiniGPT4、mPLUG-Owl2的rank为8/64/32，经grid选择，投影在16–32上层。实际完整Table1 LLaVA CHAIR-S13.05±.57 vs Nullu15.20±.60、greedy20.40±2.80，三个模型局部物体指标有收益；全部BLEU主行亦实际读，不由受限生成代理认证自由问答无损或严格事实保持。Table2 OPOPE完整各模型主行亦核，只支持该caption/负对象协议。Table3的准确/详细分数由GPT4V评价24-image LLaVA-Bench，MMHal由GPT4裁判，不授独立真值。

Table5 image-only13.05/4.53/15.82，text-only15.20/5.30/15.69，joint15.71/5.32/15.66（CHAIR-S/CHAIR-I/BLEU）；联合两类bank确实退步，更多扰动不自动更好。§4.9正文所测rank8与diffusion .5T为局部最佳，增rank/强扰动及image noise存在反侧；只采用正文趋势，不补未读图值。400训练/1000测试clean-vs-edited probe可分性不排除纹理/编辑artifact混杂，也不证明这些方向是自然幻觉唯一原因。

Table4 A6000 LLaVA7B CIPHER与greedy同0.70 items/s，是受印在线条件，不可抹掉GPT、25000图、features、SVD、grid、bank驻留与回归成本。§4.1通用beam3与该表greedy/beam配置不同，未披露的整次运行协议不能拼为质量13.05与吞吐0.70已经完整匹配的端到端SLO。权重不更新也不是无校准；推理无diffusion只限定消费者开销。

## 评分与真实owner缺口

**2+1+2=5成立**：视觉输入反事实汇总固定bank的producer/consumer接口改变（2），有限LVLM/物体与代理评价负载（1），bank适用人口与制备/消费费用、必要回归边界可复用（2）。重要局部gap及明确反侧已做必要深入，不借SVD成熟原理加分，不因已有相邻主题自动NC。

实际VLI在当前请求生产两份派生视图；One Token在首次请求产生局部方向并缓存后续；音频分支对当前输入做原音频/静音forward。三者没有具体承载跨校准人口SVD bank对未来每步hidden投影这一接口。因此两段受限长期补充有真实差额，不是模块组合包装或重复写已有缓存。插在One Token两完整段后/音频差分前，保留旧方法合理性、局部方向有效期及音频职责。

## 最小修正后的逐字PRE

第一段保持准备者原文。第二段仅把“高方差编辑方向”换成“差分矩阵的主要奇异方向”，原因是Eq8–9未中心化；不改其收益/费用/回退命题。以下两段可写，source链接/marker由Books writer按既有格式补齐，不增实验保证：

差分方向也可以先在校准人口上汇总，而不为每个请求生产新负视图：保持原 caption，不改变它的文字条件，只用错误 caption 引导离线 diffusion 编辑图像；对多个编辑样本的 caption-token hidden 取均值，减去原图表示，再以逐层 SVD 的主要右奇异向量保存一个方向库。推理只对指定层每步 hidden 执行 `h−V_r V_rᵀh`，把昂贵的反事实制备与在线投影消费者分开。这不同于首次请求的局部差分缓存：bank 的有效性现在依赖校准人口、编辑器、caption、LVLM、层与rank共同保持兼容。

差分矩阵的主要奇异方向不自动是自然幻觉的唯一原因，投影正交也不认证保留全部事实语义。局部物体错误减少伴随 rank、扰动强度和图像noise敏感；文本与视觉两类bank联合还会退步，代理judge的高分不能代替独立grounding。权重不更新仍支付错误caption制备、多次图像编辑、features、SVD、搜索与bank驻留，在线吞吐不抹掉这些费用。新人口或编辑artifact失配、旁侧任务回归或总预算不值得时，保留原forward、输入特定的受限方向与外部取证，不让固定投影库授予事实发布权。

**裁决：受限Source与5分通过；真实Ch23差额及上述最小修后PRE通过。** 本记录不授Books实际写入/POST、实现复现或DAY。仅本人独核文件，无共享Books/Report/State/mainledger写，无stage、commit、push。
