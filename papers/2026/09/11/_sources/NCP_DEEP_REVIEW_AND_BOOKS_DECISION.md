# NCP-ArchPreview exact-v1 深入审阅与 Books 决定

本文件只重开 `SF-2026-ARXIV-2609-10715`。它修正“HTML 不可达等于 exact-v1 正文受阻”的判断，
不重扫本窗，也不替代 Daily 的候选、评分或最终状态汇总。

## 1. 身份、日期与访问状态

- **Source Family：** `SF-2026-ARXIV-2609-10715`
- **标题：** *NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models through Next Concept Prediction*
- **作者：** The Intern-NCP Team；正文列出 Shanghai AI Laboratory 与 Shanghai Jiao Tong University LUMIA Lab。
- **Primary：** [arXiv:2609.10715v1 exact-v1 PDF](https://arxiv.org/pdf/2609.10715v1)
- **版本与日期：** arXiv Atom `published=updated=2026-09-09T18:12:43Z`；这是提交字段，不冒充公开时间。
  Daily 已用 arXiv 官方 Friday 公布批次将其归入 `2026-09-11T08:00:00+08:00`。
- **访问：** exact-v1 HTML 返回 404，但 exact-v1 PDF 返回 200、`application/pdf`，全文 43 页可读。
  因而 Access Status 从 `Blocked` 改为 `Available via exact-v1 PDF`。
- **撤回状态：** 本次读取的 Atom 条目、PDF 首页和正文未见 withdrawal / replacement notice；这只陈述本次可见状态，
  不扩写为永久保证。
- **Evidence Level：** 作者 technical report；机制、实现说明与作者实验可作为 primary evidence，未独立复现。
- **原评分：** `Design Delta 3 + System Reach 3 + Durability 3 = 9`；保持候选分母与原评分不变。

## 2. 问题与旧方案为何合理

标准 decoder-only 以 causal next-token prediction（NTP）提供逐位置、与最终输出同构的密集监督。它只维护一个 token
时钟，训练、生成、KV Cache、vocabulary projection 和 serving runtime 都能复用同一接口；当实现成熟度、流式输出、
可解释的 token 边界与 kernel 效率优先时，这仍是最稳健的默认方案。

它留下的压力不是“模型没有高层表示”，而是高层表示只作为 NTP 的间接副产物形成：目标本身没有显式要求模型预测
跨多个 token 的内部状态。论文要验证的是，能否在不删除 token-level causal output 的前提下，再建立一个较慢的 concept
时钟，把 learned latent representation 变成一等预测目标，并将预测结果反馈给 token decoder。

## 3. 机制、状态所有权与因果边界

### 3.1 双粒度状态流

8.94B 配置把 OLMo-3-7B 的 token pathway 分成 16 层 Token Encoder 与 16 层 Token Decoder，二者之间增加 8 层
Concept Module。Token Encoder 的连续状态每 `k=4` 个 token 做 mean pooling，得到长度约为 `T/4` 的 concept sequence。
每个 4096 维 concept 又切成 32 个 128 维 segment；每段从含 128 个 codeword 的独立 codebook 取最近邻，product
quantization 因而用小 codebook 组合出较大的离散 concept vocabulary。

Concept Module 自回归读取此前的**连续** concept history，并为每个 codebook 预测下一 concept 的 codeword 分布。模型
不做 argmax 或 sampling，而以该分布对 codeword 求期望，形成可微的 predicted concept。预测结果重复 `k` 次并向后移动
`Δ=k` 个 token position，再残差注入 Token Decoder；该 shift 保证 concept 只在构造其 target 的 token 已被处理后进入
后续 token prediction，不把未来 token 泄漏给当前 NTP loss。

```text
tokens
→ causal Token Encoder states
→ fixed-span pooling + product-quantized vocabulary
→ autoregressive Concept Module predicts next latent concept
→ causal shift by k + repeat to token resolution
→ Token Decoder + vocabulary projection
→ next token
```

checkpoint 因而必须共同拥有 `k`、codebook 内容与 segment layout、三段 module depth、concept prediction heads、
IRC/CRC residual routing、loss weights及其版本。runtime 必须区分 observed token prefix、由其形成的 continuous concept、
predicted concept 与可注入 token position；错一位的 shift 会直接破坏 prefix causality。论文还使用三条 CRC
（Encoder→Concept、Encoder→Decoder、Concept→Decoder），跨粒度传递前分别 chunk 或 repeat，并对 Concept→Decoder
采用相同 causal shift。

### 3.2 三个目标拥有不同梯度边界

训练目标为 `L_total = L_NTP + alpha L_NCP + beta L_VQ`：

- `L_NTP` 是标准 shifted next-token cross-entropy，更新 token pathway 和 concept pathway，并保留最终 token 接口；
- `L_NCP` 对 predicted continuous concept 与 detached target concept 做 MSE。target 端 stop-gradient；Token Encoder 只经
  提供给 Concept Module 的历史 concept 收到 NCP gradient；
- `L_VQ` 把选中 codeword 拉向 detached continuous concept，不更新 Token Encoder。

这组 stop-gradient 与 shift 不是实现细节：前者定义谁能改变 latent vocabulary 和表示，后者定义哪些状态可作为当前
token 的条件。把 codebook、concept target 或 shift 混为同一状态，会分别造成 codebook/representation ownership 不清、
错误梯度路径或未来信息泄漏。

## 4. 实现与评价合同

- **主模型与数据：** OLMo-3-7B backbone；Stage 1 使用 Dolma 3 Mix、共 5.73T tokens；Stage 2 使用 Dolma 3 Dolmino、
  100B tokens；最大 context 8192；参数 precision 为 BF16。
- **优化：** matrix-valued parameters 使用 Moonlight Muon，默认 LR `6e-5` 与 OLMo-3-7B 同一 cosine schedule；embedding、
  bias 和其他非 Muon 参数使用 AdamW。主实验为保持基线可比，仍使用 OLMo-3 的 layer-wise Q/K normalization。
- **评价：** OLMo-Core 协议覆盖 30 个 benchmark families；Appendix E 给出 task、shot、split、metric 与固定生成 seed 42。
  论文把 higher-is-better task macro 与 lower-is-better BPB 分开，不把二者混合为一个分数。
- **硬件与复现：** 主 5.73T 训练的硬件、wall-clock、energy、batch/concurrency 和重复独立训练 run 未披露；作者发布
  weights、recipes、checkpoints 与部分 evaluation/deployment links，但本审阅未执行代码或复现实验。
- **性能数字：** 下述 FLOPs 均为 analytical training FLOPs；论文明确指出它们未计 source-state materialization、memory
  traffic、reduction 与 small-kernel launch overhead，不能外推为 wall-clock 或生产吞吐。

## 5. 关键对照、收益与反证

### 5.1 主训练与组件消融

- 与 7B Vanilla 相比，作者报告 Stage 1 最终 token loss 低 0.091，并在 51.3% 训练 tokens 处达到 Vanilla 的最终 loss；
  Stage 2 最终 loss 低 0.027，在 66.2% tokens 处达到 Vanilla 最终 loss。因为 NCP 模型约 8.94B，单独这组结果不能把
  收益归因于 concept objective。
- 参数/计算对齐实验补充了必要对照：NCP 为约 `40 P_blk / 34 F_blk`，与 34-layer computation-aligned 和 40-layer
  size-aligned Vanilla 比较；200B-token progressive ablation 显示加入 Concept Module、hierarchical residual 和 NCP loss
  时训练 loss 依次下降。完整模型优于 computation-aligned baseline，并以 size-aligned baseline 约 85% analytical compute
  接近其 loss。这支持“该分支可行且不只是 Vanilla 额外 FLOPs”，但仍不是所有数据/规模上的质量排序。
- 1B、150B-token residual ablation 中，IRC-only、IRC+CRC 和其他 cross-module variants 均有对照；完整 IRC+CRC 的 loss
  改善最大，但论文自己说明 analytical FLOPs 漏记 runtime/memory cost。
- scaling ladder 在多个 FLOPs budget 下为两类架构分别搜索 model/data allocation、learning rate 与 batch，作者拟合出
  `1.74x` compute-efficiency difference。它是 validation-loss scaling fit，不是固定硬件的端到端速度，也没有独立复现。

### 5.2 下游能力不随 loss 等比例转换

作者报告 Stage 1 higher-is-better macro 比 OLMo-3-7B 高 2.45 points；Stage 2 只高 0.59 points，而且 code 与部分
MC-STEM 指标回退。论文的 Limitations 也承认，loss 到能力的转换依赖训练 mixture、stage 与 evaluation domain。
因此可保留“显式 concept target 在所测设置中可训练且有受控增量”，不能写成“更低 NTP loss 必然带来普遍能力提升”。

### 5.3 轻量 adaptation 与 speculative drafting 只是附加 operating points

- 冻结 token backbone、只更新现有 VQ codebooks 与 concept-prediction heads，共 17M trainable parameters；与 17M LoRA
  和 full tuning 比较时，VQ 在所测 code/math/knowledge adaptation 上呈现更低 memory、更高 tokens/s/GPU，但 target gain
  不总是最高，general retention 也不是全部无损。该路径只适用于已经训练出 NCP concept space 的 checkpoint。
- 将最后一个 fully completed Target chunk 的 concept state 经零初始化 gate 注入 1.1B DFlash2/DFlare drafter，增加
  0.04M parameters、不增加 Target forward；相同 distillation data order、seed 与 budget，在 GSM8K、MATH、HumanEval、
  MBPP、proposal horizon 16 的 exact verification 下，mean accepted length 从 5.933 增到 6.180（相对 4.17%）。这证明
  该 concept signal 在该 drafter/evaluator 上有用，不证明端到端 latency、throughput 或其他 target model 一定改善。

## 6. Trade-off、failure mode 与 fallback

- 双粒度路径用显式 span-level target 换来额外 Concept Module、codebook、prediction heads、cross-module state materialization
  和三目标权重。只有当更短 concept sequence 的收益覆盖这些参数、memory traffic 与 kernel fragmentation 时才成立。
- 固定 `k=4` mean pooling 把边界先验写进 checkpoint；自然概念不一定四 token 对齐。product-quantized codeword 是 learned
  prediction support，不保证具有人可解释语义；codebook utilization、漂移与 collapse 需要独立监控。
- 训练时 Concept Module 读取真实 continuous concept history，推理时递归读取先前 predicted concepts，新增 concept-level
  exposure mismatch 与误差累积。causal shift 防止 label leakage，但不消除 prediction drift。
- 主报告没有 long-context training；8192 上的压缩路径不能证明其在更长依赖、不同 chunk size 或 streaming cache 下保持收益。
- Muon 与 layer-wise Q/K normalization 的组合出现 head-wise norm outlier、attention-logit growth 和 gradient spike；per-head
  Q/K normalization 在对照中稳定了它，但没有用于主性能结果。该观察提示 optimizer/normalization 仍是独立训练约束，
  不能把稳定性收益归因于 NCP 架构。
- 需要成熟单时钟 runtime、严格可审计 token state、短上下文，或缺少 concept-aware kernels/evaluation 时，普通 decoder-only
  NTP 仍是 correctness fallback。若只希望增加多个未来 token 的监督而不引入 learned codebook 与 concept feedback，MTP
  是较小的替代分支；论文 3B 对照显示 NCP 与 MTP 可叠加，并不构成互斥替代。

## 7. 证明、未证明与证据位置

**证明到的窄结论：** 在作者披露的 OLMo-3/Dolma、8.94B/5.73T 与较小受控实验中，token NTP 可以与 learned
product-quantized concept target 联合训练；只要 concept feedback 经正确的 causal shift，最终仍可保持标准 token-level
autoregressive output。参数/计算对齐与 progressive ablation 支持该架构分支具有独立于简单扩宽/加深的训练-loss 增量。

**没有证明：** 不证明 learned codeword 等同于人类概念；不证明 NCP 普遍优于 NTP、MTP 或其他 hierarchical model；
不证明 1.74x 是 wall-clock 加速；不证明 lower loss 在所有 stage/domain 转化为更高能力；不证明 long-context、线上 serving、
多租户 cache、端到端 speculative speedup 或生产稳定性。主规模实验缺少独立重复 run 与不确定性，代码/artifact 未在本次复现。

**Evidence locators：** §2.1–2.5 / Eqs. 1–20 / Figure 2；§3.1–3.6 / Eqs. 21–25；
§4.1–4.6 / Tables 1–3 / Figures 1, 3–6；§5.1–5.3 / Tables 4–9 / Figures 7–8 / Eqs. 26–27；
§7 Limitations；Appendix B / Algorithm 1；Appendix C；Appendix D / Figure 10 / Table 12；Appendix E / Tables 13–14。

## 8. Books 比较与决定

- **比较结果：** Ch18 已解释 vanilla decoder-only 的单 token causal factorization，也讨论将可见 reasoning token 压缩成
  recurrent latent state；但没有承载“保持 token output、同时把 learned multi-token representation 作为显式 autoregressive
  target 并反馈 decoder”的通用双粒度架构。Ch28 已拥有多目标训练和 latent-path optimization，但该材料首先改变的是
  decoder architecture 的状态粒度与 causal interface，训练目标是实现该架构的 handoff，不应在两个章节重复推导。
- **Decision：** `Integrate`
- **Canonical owner：** `MODEL-DECODER-ONLY` / Ch18 / `books/part-02-model/18-decoder-only.md`
- **正文锚点：** `Next-token 接口不要求内部状态只有一个粒度`
- **Marker：** `source-family:SF-2026-ARXIV-2609-10715`
- **写回范围：** 只写长期架构命题、state/control ownership、trade-off、fallback 与证据边界；不把作者 benchmark 写成
  通用性能结论，不在 Ch28 重复建立第二 owner。
