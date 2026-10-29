# 2603.10470：必要 Source / 具体 owner 差额提案

状态：准备者实际原证与 Ch23 局部已读，拟5分必要深入；等待 root 非准备者 Source/owner/PRE 判断。不写 Books，不自授 PRE、采用或 DAY。

## 身份 / 日期 / 实际范围

Fighting Hallucinations with Counterfactuals: Diffusion-Guided Perturbations for LVLM Hallucination Suppression；Hamidreza Dastmalchi、Aijun An、Ali Cheraghian、Hamed Barzamini。复用 `SUP_ABS3_10470.txt` 完整题摘准入与 `SUP_DATE3_10470.raw` / 主独核 DATE3 的 Mar12 arXiv 日级事件。Comments CVPR 2026 不是具名早公开稿，不以接受信号制造早稿阻塞。

精确官方 v1：`SUP_HANDOFF7_SOURCE_10470.raw` / `.txt`，GET 原件 `SUP_HANDOFF7_FETCH_RESULT.json`。实际必要顺读 §3 Eq1–11（txt348–1000）、§4.1–4.2、Table1 完整主行、§4.4–4.9/Table3–5 与直接 noise/rank/strength 反侧（至2045）。未称全附件、代码或完整图像目视。表中定量依据来自文字/HTML table，Fig7–9只采用相邻正文所述趋势，不采用未目视幅度。

## 新增接口，不借成熟 SVD 原理加分

已知 Nullu 用错误文本配原图求方向，本稿改变差分生产者：在5,000 COCO训练配对上用 GPT 造错误 caption，再用 SD1.5 round-trip 生成每图5个 counterfactual；**hidden extraction 仍使用不变的原 caption**，因此变化对象是视觉输入。逐层 caption-token mean 先在5个编辑图间平均，再减原图 hidden；把所有样本差分堆成矩阵，SVD top-r 右奇异向量构成固定 layer bank。

在线每个 token 的指定上层 hidden 用 `h−V_r V_rᵀh` 正交投影，移除整个校准人口的高方差编辑方向。这不是每个请求生成新的图像/方向，也不是推理时再运行 diffusion；它把离线生产者、校准人口与在线固定消费者分开。真正的设计差额是**视觉 counterfactual aggregation 的跨输入投影库**，而不是 SVD、线性 projection 或“表示不是真值”的成熟原则。

## 评价 / 必要限制与反侧

- 500 COCO val、3 runs；LLaVA1.5/MiniGPT4/mPLUG-Owl2 的 r分别8/64/32 grid-selected，指定layers16–32。权重不更新，但离线 GPT/25k SD images、LVLM features、SVD、rank/层/strength grid 与 bank驻留仍需制备与费用；不能称无训练意味着无校准。
- Table1 LLaVA CHAIR-S13.05 对 Nullu15.20 / Greedy20.40，局部物体错误减少有证。BLEU与受限 CHAIR 不证明自由问答/语义无损，MMHal GPT4与24-image LLaVA-Bench GPT4V仍是代理裁判，不能签事实真值。
- Table5 image-only CHAIR-S13.05 / text-only15.20 / joint15.71：把两类扰动一起用反而差，不能认证更多负样本/更强bank一定好。Diffusion strength0.5T与rank8是所测局部 optimum，过强扰动或删去更多维度可损效果；视觉 noise 后仍退。
- 编辑可引入多种语义、纹理与 artifact。400/1000 probe 的 clean-vs-edited 高可分离性不证明这些方向是自然 hallucination 的唯一原因、真实图像条件有效或可删全部事实。
- Table4 A6000时0.70 items/s对greedy0.70是所印在线条件；§4.1的beam3与table的greedy/beam口径不同，不把 CHAIR13.05+0.70 拼成已核同一完整运行协议，更不覆盖离线制备、并发/尾延迟。

## 评分 / 具体 owner 差额

2（新增视觉反事实跨样本校准 bank 的消费者接口）+1（有限LVLM/物体与代理评价，不授普遍消除幻觉）+2（明确公式、比较与反侧）=5。建议必要深入；是否 Books 采用待非准备者裁决，不按章节映射自动整合。

实际 Ch23 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 115–130 连续局部已有 VLI：逐请求派生两图；One Token, Two Fates：首次请求差分缓存；音频：两forward局部方向。这些已覆盖派生输入误差、线性假设、方向有限期和独立 grounding；**未直接承载跨校准人口的编辑差分 SVD bank 在未来请求每步投影删除**。Ch24负责 diffusion 制图/采样，而此稿消费者是 LVLM hidden，拟唯一 owner `MULTIMODAL-REPRESENTATION`，不新增结构或把离线扩散细节重复写入Ch24。

## 逐字两段提案（未授权写入）

差分方向也可以先在校准人口上汇总，而不为每个请求生产新负视图：保持原 caption，不改变它的文字条件，只用错误 caption 引导离线 diffusion 编辑图像；对多个编辑样本的 caption-token hidden 取均值，减去原图表示，再以逐层 SVD 的主要右奇异向量保存一个方向库。推理只对指定层每步 hidden 执行 `h−V_r V_rᵀh`，把昂贵的反事实制备与在线投影消费者分开。这不同于首次请求的局部差分缓存：bank 的有效性现在依赖校准人口、编辑器、caption、LVLM、层与rank共同保持兼容。

高方差编辑方向不自动是自然幻觉的唯一原因，投影正交也不认证保留全部事实语义。局部物体错误减少伴随 rank、扰动强度和图像noise敏感；文本与视觉两类bank联合还会退步，代理judge的高分不能代替独立grounding。权重不更新仍支付错误caption制备、多次图像编辑、features、SVD、搜索与bank驻留，在线吞吐不抹掉这些费用。新人口或编辑artifact失配、旁侧任务回归或总预算不值得时，保留原forward、输入特定的受限方向与外部取证，不让固定投影库授予事实发布权。

插入位置建议为 Ch23 的 One Token, Two Fates 两段之后/音频差分段之前；以上仅 Source/实际差额与 PRE 待审提案，不改 existing source marker。
