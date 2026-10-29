# 2603.10780：必要 Source / owner 差额提案

状态：准备者已实际读精确 v1 必要源与 Ch24 连续 guidance 局部；拟5分标准审阅/具体 gap。待 root 非准备者 Source/owner/PRE 裁决；不写共享书稿，不授采用或 DAY。

## 身份 / 日期 / 阅读范围

Guiding Diffusion Models with Semantically Degraded Conditions；Shilong Han、Yuming Zhang、Hongxia Wang。复用 `SUP_ABS3_10780.txt` 完整题摘准入及 `SUP_DATE3_10780.raw` / 主独核 DATE3 的 Mar12 arXiv 日级事件。Accepted CVPR 2026 没有具名 dated 早稿全文信号，不扩大 venue 恢复或全网证明。

官方 exact-v1 `SUP_HANDOFF7_SOURCE_10780.raw` / `.txt`，GET/UTC 原件在 `SUP_HANDOFF7_FETCH_RESULT.json`。实际必要阅读 §3–5 Eq2–11（txt490–1560）、§6 Tables1–4 / §6.3.1–6.3.4 / 结论（1561–2299）、Appendix B 必要 Algorithm2 与 ProcessToken 局部（3535–4105）、C.3真实超参/FLUX配置（4150–4375）。未读全部图片、代码或其他附件；Fig2/5/6仅采用相邻文字支持的条件，不称目视验图或采用未核幅度。

## 原约束→本稿实际新增

固定 CFG 以正条件与空条件作差，capacity/history/prototype reference 也各有语义。这里改变的是负分支的**条件保留范围**：将已经承载上下文的 encoded token 分成 content 与 context-aggregating（padding或special）两组，先把 content token 用匹配位置的空条件状态替代，再按预算替代 context-aggregating 组；二者不是把整个prompt清空，也不是把token从sequence删掉。

Eq9把 R_deg∈[0,2] 映射为 r_content=min(R,1)、r_context=max(R−1,0)；Eq11在表示上按mask混合原条件与empty branch状态。Eq5仍使用同样两支差分代数 `D(c)+(w−1)[D(c)−D(c_deg)]`，新对象是保留部分共享上下文的负条件。重要delta不在加权外推或PageRank这项旧算法，而在**content先退化、上下文聚合状态后退化**的分组条件构造与被控对照。

默认R=1恰好替换全部content、保留context组，可绕过WPR。非边界预算才按denoiser指定block的attention/importance挑组内token；first-step排名缓存复用避免每步再算，不能写成每步语义实时重判或只改静态文本encoder。不认证主文与伪码共同构成唯一逐行执行协议；mask保留/退化位的互补约定须按各公式/实现分别读。

## 必要评价 / 反侧

- 主表5,000 COCO captions / GenAI-Bench，SD3、SD3.5、FLUX1、QwenImage均有限改善；Qwen Aesthetic2.54低于CFG2.57，FLUX FID优势较小，不授全质量支配或所有模型普效。
- Table3 固定 R=1.1，stratified/random与stratified/WPR相近，前者CLIP32.02与VQA92.27甚至略高于WPR31.98/92.21。因此WPR不是必要模块，“有WPR即新理论/因果”的评分不成立。全局不分组/reverse/random的退步支持分组接口，在此人口内而非一般证明。
- Eq6 principal angles / Eq7 projected-energy 的几何对象是**跨COCO prompt预测的SVD近似子空间**。与它近正交不证明真实数据manifold法空间已知、任意迭代无干扰、语义保真或概率law保持；common-mode cancellation是解释性假说而非必要/充分定理。
- CFG*中把退化条件当正条件再生成与CLIP变化支持剩余语义不同，不是独立语义ground truth。VQA Score是yes概率、CLIP/Aesthetic也为proxy，不能授composition真值。
- Table4 **R=1.1** SD3：5.655s对CFG5.456（+3.6%）；每步WPR8.031（+47.2%）。默认R=1绕开WPR不等全流程免费，仍是两denoiser分支、状态/空条件生产、hooks与调参。不能把这个+3.6%贴到所有模型/默认R。
- C.3 SD3.5 block2而SD3/FLUX block1，scale也各自配置；FLUX512²/28steps不是原1024²/50steps。PAG/SEG比较关闭CFG、使用自己scale，受控比较不等完全同算法调用人口。强度、block、tokenizer/empty-state与step网格须保留具体identity。

## 三维评分 / 实际 owner 差额

2（新增分组条件退化 reference 的可执行接口与实际分组反例）+1（有限模型/代理评价，几何hypothesis不授普效）+2（公式、分组消融与计费/质量反侧）=5。拟标准必要审阅，是否采用待 root 独核。

实际顺读 Ch24 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 270–310完整连续局部；Ch23/25入口也实际核。现有Sparse Guidance的capacity gap、velocity EMA、MMD reference、harmful keyword/prototype、pooled modulation 各有owner，但**未直接承载同一prompt的content/context-aggregating保留范围与分组退化边界**。拟唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`，不重复写Ch23 generic encoded语义、不按论文新开结构。

## 逐字两段提案（尚无写锁 / PRE授权）

负分支还可以保留正条件的部分共享上下文，而不完全清空条件或削弱主干capacity。一个受限分支将encoded text positions分为content与context-aggregating两组，先把content状态替换为匹配的empty-branch状态，再随退化预算替换聚合组；正支减去这份部分退化负支，仍采用原两支外推形式。默认替换全部content、保留聚合组时无须组内排名；其他预算才在指定denoiser层提取attention排序，并可复用首步排名。它改变的是条件差分的参照对象，不是删除sequence位置，也不是对所有模型重新训练unconditional分支。

这种分组只在受测tokenizer、聚合状态与模型接口下成立：对COCO预测做SVD得到的近正交子空间是诊断代理，不是已知真实manifold或全轨迹无干扰证明。分组消融支持局部配置，组内PageRank却非必要；图像质量仍有反退，CLIP/VQA不授语义真值。两支求值、empty-state/hook、排名或缓存与block/scale校准继续计费，非默认预算的局部计时不签所有模型SLO。条件布局或排名漂移、质量和完整费用不合算时，保留原CFG、dense/capacity reference与独立生成验收，不让部分上下文保留自签语义无损。

建议在 Ch24 Sparse Guidance 两支接口之后/velocity EMA历史reference之前加入；保留原正文及marker。以上只是具体delta与待独核提案，不是 Books 已整合。
