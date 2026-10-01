# 两项普通 Books 待采用：最窄正文提案

仅供非作者写前 source→actual-owner 裁决。作者已读的必要 exact-v1 段、数字与反证在 [本日证据表](V3_EVIDENCE_REVIEW.md) `22678/22709` 两行；本文不授权实际写入，也不把两项计作 Integrate。目标章节与邻接现文已读，以下文字须经 root 采纳/授共享锁及另一人的实际写后复核。

## 2604.22678v1 BERAG → `AGENT-RAG` Ch76

**建议位置：**[Ch76「Relevance 不等于 Sufficient Context」](../../../../../books/part-07-agent/76-rag.md)中旧 `retrieval relevance→context sufficiency→generation faithfulness` 链及旧 top-k 有效边界之后、Query Robustness Gate 之前。既有链条把文档集整体交给 reader，再判 evidence 是否足够；本文受限条件分支改动的是 reader 执行单位，不是事实权威。

**拟正文：**

> 把 Top-K 文档一次拼进同一 Context，最容易让 reader 跨文档组合线索；当长拼接主要引入无关证据和竞争时，也可以为每份文档保留独立的条件生成分支，按已生成 token 的条件 likelihood 更新分支权重，并提前剪去权重低的续写。这样检索候选不再只是静态文本列表，而成为带文档身份、生成前缀、权重和剩余预算的可撤销 reader state。分支权重只刻画该 reader 在给定文档下延续当前答案的相对支持，不能授予文档事实真值；跨文档证据必须组合的问题不能靠单文档分支剪枝保证覆盖。
>
> 这以重复 query/prefill、多个活跃分支、后验误剪与 deflection 开销，换取部分无关长 Context 的节省。作者的视觉问答、所测模型和 Top-P 实验只支持该条件下的质量/局部 token 时延取舍，Naive K=50 分支还显著更慢；索引、吞吐和端到端生产 SLO 未随单 token 数一起证明。若证据需要跨文档合取、分支预算紧或后验校准失准，仍回退普通集合检索→sufficiency/faithfulness gate，来源身份与独立 verifier 继续拥有答案提交权。<!-- source-family:SF-2026-ARXIV-2604-22678 -->

**写前问题：**先确认这不是 Ch76 已有 query 侧多路检索或 LatentRAG 压缩 subquery 的同义复述；本分支的 `document-conditioned reader continuation` 才是唯一 proposed delta。不能把“Bayesian”字样当外部事实概率。官方[exact-v1](https://arxiv.org/html/2604.22678v1) §3 Eqs.2–6、§4.6–4.8 Tables 5–6。

## 2604.22709v1 Abstract-CoT → `TRAIN-GRPO` Ch33

**建议位置：**[Ch33「Reasoning Cost 也是版本化的 Reward Prior」](../../../../../books/part-04-training-system/33-grpo.md)的显式 token 税/prior 论证之后、Pure RL 与多阶段训练交接之前。旧段仅给语言 trace 的成本与 reward prior，未把 reasoning 的可见词元换为额外的离散隐码并纳入训练资产身份。

**拟正文：**

> 减少自然语言 CoT token 不一定要给每个词征税；另一个条件分支扩展一组专用离散 token，让模型在这些不可直接人读的码上形成中间状态，再输出可核答案。此时训练协议也要改变：先用 verbal-CoT bottleneck SFT 使码承接推理，再用 prompt-only 自蒸馏 warm-up 建立生成轨迹，最后以受约束 GRPO 联合更新码与答案；直接 cold RL 在作者设置中不能被当成等效替代。Codebook/保留词表、warm-up teacher、reward/verifier 与解码约束须进入同一 experiment identity；较短输出不是较少训练 compute，也不是更忠实的解释。
>
> 隐码可缩短已测输出，却失去人读过程证据、增加训练阶段和迁移成本。作者只测 Qwen3 4/8B、Granite 3B 与其数学/代码协议；Qwen3-8B 在 MATH/AIME 上有相对 verbal SFT+RL 的反向质量切片，约 600k SFT 与 1M RL episodes、8–32 H100 的准备工作不能由推理 token 节省自动抵销。需要逐步审计、没有可靠 verifier、或新增训练预算不划算时，保留显式短 CoT、普通 SFT→RL 与外部验证分支；隐码只拥有生成提案权，不拥有 reasoning faithfulness 或发布权。<!-- source-family:SF-2026-ARXIV-2604-22709 -->

**写前问题：**Ch33 已有多阶段 SFT→RL 与 reward cost，但本来源的 proposed delta 是离散 latent action space 的训练前置责任；若 root 认为现 Ch33/Ch28 已足以承载该判断，应改为具名 No Change 而不为论文名添加正文。官方[exact-v1](https://arxiv.org/html/2604.22709v1) §3–4/Tables 1–2。
