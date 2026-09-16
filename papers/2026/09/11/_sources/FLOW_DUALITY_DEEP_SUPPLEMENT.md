# 2026-09-11 Deep Review Supplement — Flow Duality

**材料：** [Flow Duality and Source Geometry for Categorical Generation](https://arxiv.org/html/2609.10863v1)  
**Source Family：** `SF-2026-ARXIV-2609-10863`  
**复核版本：** `arXiv:2609.10863v1`  
**评分：** `Design Delta 2 / System Reach 1 / Durability 3 = 6`  
**深入审阅触发：** 分数默认只要求标准审阅，但本材料被判断为 Ch24 的长期知识缺口；按研究合同，Books 知识缺口不论分数均须深入审阅。  
**结论：** 深入审阅通过。证据足以支持 Ch24 中关于“条件 duality、source geometry 与 transition timing”的窄化机制，不足以支持生成质量、训练稳定性或 Serving 性能排序。

## 1. Identity、日期与访问

- exact-v1 HTML 标识为 `arXiv:2609.10863v1 [cs.LG]`，题名与作者身份可定位；正文、定理、证明和附录均可访问。
- 本材料属于 arXiv 2026-09-11 Friday new-submission batch；采用的 first-public time 是 `2026-09-11T08:00:00+08:00`，位于日报窗口 `2026-09-10T09:00:00+08:00 ～ 2026-09-11T09:00:00+08:00` 内。HTML 页的 `09 Sep 2026` 是版本标识中的提交日期，不冒充首次公开时刻。
- 审阅时 exact-v1 页面未显示 withdrawal、replacement 或 retraction notice。该判断只限本次访问状态，不构成未来不会撤回的保证。

## 2. 中心主张与旧问题

continuous flow matching 与 categorical discrete flow matching 通常由不同状态空间、插值路径和采样器实现；把 continuous source 只当成中性的初始化噪声，在这种分工下曾是合理简化。论文追问的不是两类生成器是否普遍等价，而是一个更窄的问题：当 continuous conditional path 在 one-hot target 与 continuous source 之间作 convex interpolation，再逐位置执行 argmax 时，究竟诱导什么 categorical conditional path。

论文的长期增量是给出可检查的条件接口。它证明：在特定 source、coupling 与 boundary assumptions 下，argmax pushforward 形成 uniform-source 的 discrete convex-interpolant conditional path；其中 source 的 pairwise-gap geometry 决定 effective discrete coefficient。由此，source law 会改变 token 从 source category 切换到 target category 的有效时间，不再只是可互换的采样细节。

## 3. 机制、状态与控制权

每个位置的 continuous state 是一个 `V` 维 block。先采样 product continuous source `Z0`，令 `X0 = argmax(Z0)`；再通过只依赖 `X0` 的 discrete kernel 采样 `X1`，并设 `Z1 = onehot(X1)`。conditional continuous path 为：

```text
Z_t = (1 - k_tilde(t)) Z0 + k_tilde(t) Z1
X_t = position-wise argmax(Z_t)
```

关键条件包括：

1. source 在位置间乘积分解；每个位置内对 coordinate permutation 不变；
2. source 在 argmax tie hyperplane 上无概率质量，pairwise gap 在相关 threshold 上无 atom；
3. lifted coupling 满足 `Z0 ⟂ X1 | X0`，即 target 只能通过 `argmax(Z0)` 依赖 continuous source；
4. target 是 one-hot categorical state，continuous path 是 nondecreasing convex interpolant。

在这些条件下，Theorem 3.4 给出每个位置的 categorical conditional：

```text
p_t(x_t | x0, x1)
= (1 - k_i(t)) delta_x0(x_t) + k_i(t) delta_x1(x_t)
```

其中 `k_i(t)` 是 source-coordinate gap 越过 `c_t = k_tilde(t)/(1-k_tilde(t))` 的条件概率。相同 per-position source 产生共享 coefficient；不同 source 则可以有 position-dependent coefficient。

因此 Books 中的 owner 划分成立：source、coupling 与 schedule 决定条件路径和 transition timing；learned vector field 决定实际 transport；sampler/runtime 决定数值积分、token revision 与 commit。定理没有把这些控制权合并，也没有证明更换 source 后既有 learned field 可以直接复用。

## 4. Source Geometry 的三条可核结论

- **Gaussian source：** coefficient 包含词表规模 `V`；target coordinate 要超过更多 competing coordinates，因而词表增大时 transition 延后。
- **Bounded uniform source：** coefficient 由 support width 与 `V` 决定，location shift 不改变离散 coefficient；clipping 可让 coefficient 在 continuous endpoint 之前达到 1，使含 `(1-k)^{-1}` 的 velocity 只能在未饱和区间解释。
- **Centered negative-exponential source：** 推导得到 `k(t)=1-exp(-beta*c_t)`，表达式不显式依赖 `V`。这只是给定 source family 下的 coefficient 结论，不证明训练后的生成质量对词表规模不敏感。

这些结论由 §3.1–3.2、Theorem 3.4、Eq. (23)–(35) 以及 Appendix A/B 的证明和系数推导支持。reverse lift 并不自动等于任意既定 discrete flow，仍须 coefficient matching；mask-source 需要扩展状态空间和单独论证。

## 5. 实现与评价合同

论文的主体是理论接口，不是完整生成系统。经验部分只有：

- 一个 OpenWebText、10K training steps、one-step generation 的 single-run pilot，对比 Gaussian、centered negative-exponential 与一个 shifted uniform operating point；
- 指标为 generative perplexity、sample unigram entropy，以及用 unigram entropy 近似 joint sequence entropy 的 plug-in KL；
- 一个 vocabulary size 2、sequence length 1 的 learned marginal toy flow，用相同小型 vector-field model、loss 与 integration grid 比较 source trajectory。

Table 1 报告 Gaussian / centered negative-exponential / `U(-4,-3)` 的 GenPPL 分别为 `428.88 / 258.51 / 244.68`，plug-in KL 为 `1.913 / 1.533 / 1.447`。这些数字没有充分披露硬件、precision、完整 architecture、batch、sequence length、seed uncertainty 或 SLO，也没有多 seed 或收敛训练；只能作为 source choice 会影响早期 learned behavior 的单点诊断，不能用于通用质量排序。

exact-v1 没有公开代码仓库或可审计实现链接。本审阅没有复现实验，不能声称实现、数值或 artifact 已验证。理论命题由正文证明直接支持，不以代码缺失为阻塞；任何经验或工程结论则继续受该缺口限制。

## 6. Trade-off、Failure Mode 与 Fallback

把 source geometry 变成显式设计变量，可以校准 categorical transition timing，并揭示相同 continuous schedule 在不同 source/词表下并不等价。代价是 source law、scale、coupling、schedule、vocabulary 与训练 revision 必须共同版本化；source 替换还要求重新训练或定点校准 learned field 与 sampler compatibility。

主要失效条件是：position independence、coordinate symmetry、无 tie/threshold atom、argmax-compatible lifted coupling 或 coefficient matching 任一不成立；bounded source coefficient 提前饱和；source placement/scale 改变 continuous trajectory；以及 mask-source 被错误地当作原定理的直接特例。此时数学 duality 不能作为运行时保证。

fallback 是保留已训练、已验收的 Gaussian source 或原 schedule；对 mask-source 使用其专门状态空间与证明；无法证明 learned field、source 与 commit compatibility 时不做 source 热替换。需要生产结论时，重新建立至少包含多 seed、收敛训练、真实生成质量、稳定性、端到端成本和 Serving SLO 的评价合同。

## 7. 证明与未证明

**证明：** 在列明的 product/symmetry/regularity/lifted-coupling 假设下，continuous convex-interpolant conditional path 经 position-wise argmax 会诱导 discrete convex-interpolant conditional path；三类 source 的 pairwise-gap geometry 产生论文给出的 coefficient 形式。

**未证明：** 任意 continuous flow 与任意 discrete flow 普遍等价；任意 learned marginal transport 满足该 conditional theorem；source 更换可无重训复用；negative-exponential 或 bounded-uniform source 普遍优于 Gaussian；生成质量、稳定性、吞吐、延迟或 Serving SLO 获益；mask-source 与 optimal-transport/consistency 构造自动满足同一结论。

## 8. Books Gate

Ch24 的写回只采用上述条件 theorem、source-geometry timing、状态/控制权分离以及 failure/fallback，不采用 pilot 的性能排序。该正文位于首个 `## Review notes` 前，且 `SF-2026-ARXIV-2609-10863` marker 唯一。基于本补充深审，`Integrate → MULTIMODAL-GENERATIVE-PARADIGMS` 的窄化决定有效；若正文越过这些边界，则须重开本材料而不能引用本结论兜底。
