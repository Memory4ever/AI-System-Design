# 00993 决定准入的定点核心

原源：[WildIng v1](https://arxiv.org/html/2601.00993v1)，fresh完整AB在exact-v1-first-screening.jsonl；actual §3.2–3.7（HTML L126–178）以及原述新增相对preliminary study的L88–89，非全附件。

真实机制是LLM类描述平均为centroid，image crop→frozen LongCLIP向量；VLM图像描述→text encoder→trainable MLP，分别与类centroid算cosine，再用αW+(1−α)Q训练temperature contrastive loss。并非由名称直接证明geographical invariant；原文相对2025preliminary主要CLIP+BERT换LongCLIP、LLM-only类表示和更多baseline/seed/消融。新对象是此局部species-recognition表示配方，不是基础VLM新表征接口、隔离地理/类别/采集差异的通用失效界，或有新条件支持的adapter设计反证。跨域测试本身不是新测量契约，84.77→16.17不独立授所有adapter地域失效或text因果。

贡献前关闭，理由是本次原增量未超过既有description融合/MLP/对比分类的领域局部适配，而非wildlife标签、实验小、无artifact或Books主题已有；root实际原§3.2–3.7定点准入确认通过。§3.6称cosine凸组合在[0,1]并不一般成立，但此局部数值描述没有触及当前Books的保证，不借一般cosine范围知识制造候选高分或判整篇无效。不采headline性能。
