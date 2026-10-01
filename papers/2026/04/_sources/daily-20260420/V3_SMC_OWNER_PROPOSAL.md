# SMC 有限 source → actual owner/literal 提案

作者apr20_resume；以下保留写前提案原貌，实际采用状态见文末，不以提案预支整合。原始[2604.15672v1](https://arxiv.org/html/2604.15672v1)实际§3 Algorithm1/3.1–3.3/4与必要反证已读，详见本日notes同ID。2+2+2=6；实际Ch48:844–868已有asymmetric verifier、Cactus单step目标与最终混合law，但未承载population-resampling不逐轮commit exact prefix的独立分支。Owner `INFER-SPECULATIVE-DECODING`，拟放Cactus两段后/经典路径总结前，只两段与Review note。

> 另一条有损分支不再遇到首个拒绝就停止当前 draft，而是维护多条尚未提交的粒子轨迹。每个粒子先生成一段，target 批量计算该段的 likelihood ratio，以 importance weight 修正 proposal；有效样本数不足时重采高权重祖先，再继续推进，最后从归一权重中选出一条完整输出。这里的权重、祖先和 KV 引用是候选状态，不是已经验证可提交的 exact prefix；重采复制的 metadata/refcount 必须与真正共享的 KV 区分，内部一步推进更多 token 也不等用户同时收到多条序列。要求严格 target law 的请求仍用经典 acceptance；允许近似的请求则必须验收最终混合分布和任务质量，不能沿用 verifier 的逐 token 无损合同。
>
> 单轮重要性采样的一致性也不是整轮重采历史的有限误差保证。受限 [SMC v1](https://arxiv.org/html/2604.15672v1) 的定理要求 iid proposal、目标绝对连续和有限四阶权重矩，完整多轮误差仍未证明；有限粒子不能称 exact。并行粒子只在权重搬运主导、总验证 token 未超过 roofline 的条件下便宜，输出仍只有一条，不能把粒子数直接乘进交付吞吐。Paged/Radix 的祖先元数据复用减少 KV tensor 复制，却仍有随序列长增长的元数据和重采成本；其单 H100、Llama/Qwen 结果还须保不同 draft 容量、质量容差以及额外 GPU 基线的分母，不能外推同质量、同预算或生产 SLO。权重退化、长轨迹相关或质量回归无法校准时，保留普通自回归与经典 speculation 回退。

拟Review note：SF-2026-ARXIV-2604-15672，只采用多粒子私有祖先状态/终点commit及近似law-资源成本边界，保单round假设、draft不matched、3pp/10pp/15%质量容差分账，未实验复现。待非作者source→actualowner/literal，再锁与真实写后核。

## root 非作者有限裁决（2026-09-28）

已重新打开官方 exact-v1 §3 Algorithm 1、§3.1–3.3、§4 与 Ch48 的 Cactus 前后段，并查看 Ch49 的执行计划边界。**通过 source → actual owner**：改变的是 speculative proposal 的粒子状态、target 批量评分、resampling 与最终提交语义，唯一 owner 为 `INFER-SPECULATIVE-DECODING`；Ch49 只负责底层 engine，不应重复算法。Ch48 当前 Cactus 后、经典/有损分支汇合前确有“单路径局部 law → 多粒子终点 law”的过渡缺口，适合局部写入。

写入时须保留三个限定：Theorem 3.1 的 iid proposal、`p≪q` 和四阶矩是**单轮**重要性重采误差条件，论文明确未证明多轮祖先相关的整轨迹界；roofline 的“粒子几乎免费”仅限 `BN(K+1)≤R`，跨 ridge 后不成立；3pp 相对 SD、10pp 相对 SD、15% 相对 target 的质量口径不同，且 Qwen 两方案 draft 不同、SSD 比较多一张 GPU。不要把实验吞吐或准确率写作一般 SLO、同预算同模型严格优势。允许 apr20_resume 对 Ch48 此处窄写两段及章末 Review note；写后仍须由 root 复核真实正文和相邻交接，单项通过不使 04/20 日报完成。

## 实际写后状态

依上述最窄锁，Ch48 在 Cactus 后的第 866、868 行写入两段，Review 第 970 行追加受限证据。作者顺读相邻正文并做 scoped diffcheck；root 随后实际顺读两段、Cactus→经典/有损汇合交接和 Review，非作者写后 PASS，并同步 Review 的通过状态。本日 README 已列为真实整合；其余候选与整日 Gate 仍未完成。
