# 03-19 首批准入后的必要证据与具体 Books 判断

作者 resume_mar18；只补 BJT03-18自然日。首9日期/准入经非作者 root 校准通过，见 SUP_ROOT_CALIBRATION_20261011.md；下面不是独立 Source/Books 通过或 DAY。未运行实现或复现实验，机器结果不代语义。

## 2603.15854 FlashSampling — 2+2+3=7

[精确 v1](https://arxiv.org/html/2603.15854v1)，实际必要原证：§2.3–§3.2/Alg2、§4.1–4.7/Thm4.7/Lemma4.9、§5.1–5.7/Tables2–5。经典 Gumbel-Max 不是新增；增量是 tile-local 扰动 argmax 的路径等价与 group log-mass 的分布等价分开，从而融合 LM-head epilogue、并以 shard 数量而非词表大小通信。至少一个 finite transformed logit，独立 Gumbel、正确 support/temperature/RNG 与全局 index 是必要条件。全局 top-p 不能直接局部化；top-k后top-p是不同限制，原文明确实现留未来，不能授已实装。

必要反侧：避免 logits 往返的最低字节量相对 weight read 仅2B/D，最大收益不能只归因 HBM；launch/独立采样kernel与 GEMM效率共同影响。D4096/V151936、B1–256，H100/H200/B200/B300，BF16输入/FP32累加扰动，torch2.10/CUDA13/Triton3.6/FlashInfer0.6.3，25warmup/100median。FI2已是Gumbel-Max，故较小差额才隔离fusion；H200 B128/B256、H100 B256相对FI2反退保留。端到端单B200/vLLM四模型/AIME22–24，Poisson请求率与maxconcurrency同B、5run medianTPOT；Qwen3-32B B2 -1.8%反退，不能授普遍加速。完整输入/输出长度、vLLM精确version、SLO=Not Disclosed；5000sample χ²及GSM8K1319/judge p=.776只与数学exactness一致，不是数值实现零误差或生产保证。

拟 Books：**已有覆盖**，owner MODEL-SAMPLING，实际 Ch20 556–594/工程评估→“保持分布不变，也可以改变Logits的物化边界”已完整承载 materialized路径、tile Gumbel归并、TP group mass、same-distribution与 processor/RNG/shard/layout耦合、完整logprobs/复杂processor/高batch回退；本family末注662–663引用一致。Ch19开头cache不决定选择，Ch21开头容量分支非Sampling后执行步骤，Ch44 148–179把samplingoverhead与cadence分开。此次具体必要证据支持现论点而非新增性能保证，不强造正文或末注diff。非writer resume_review17_18 必要Source/actualowner具体NC正式PASS并持久化于本日独核；不授DAY。

## 2603.15953 HAT — 2+2+3=7

[精确 v1](https://arxiv.org/html/2603.15953v1)，实际必要§3.1–3.4、§4.2、§6、§7.1–7.3.1/Tables1–8与直接SFT/DPO反侧T11/T15/T22。规则采用UAX29并附camelcase/math/空白标点修改，仍有切分接口，tokenizer-free不等无预处理。byte encoder causal局部→每组learned query crossattention聚合→标准causal backbone→shifted nextword latent给byte decoder crossattention；不是旧BPEembedding直接热换。Llama3.1移除旧embedding/head、random encoder/decoder/connectors，2000step冻结backbone后小LR联合适配，134Bwords+20Blongcontext；training预算不同，不能把所有质量差额归因boundary。8B外壳实际7.192B，70B实际69.303B，parameter减少非吞吐减少。

关键反侧：§3.4 byte层更小parameter但activation可更大；byte→word→byte CP重分片/concat成本与SWA支持限制导致作者不用CP，不能泛称CP不可用。§6 middle-word轻环/过boundary完整环，byte/word双KV不均匀映射及双空间admission，batched throughput低于FLOP-matched tokenizerTransformer；§7.2 fertility/bytes-per-backboneposition不是已测latency/throughput，作者明示生产指标未评。§7.1 promptwhitespace/cue变化使publishedscores不可直接跨suite；T5HATified Trivia .623<.695，T6Hella .793<.818，T15GSM8K .667<.699，T22DPO .647<.710/.782，不采普遍质量优势。Model/corpus/trainrecipe/word-boundary明确；部署hardware、精确servingprecision、batch/concurrency、input/outputlength、SLO及latency数字=Not Disclosed；未核代码或复现。

拟 Books：整合 MODEL-TOKENIZER/Ch11，当前实际309–392及389–442全局部/交接已读，Ch10/12开头已读；actual现文Vocabulary Adaptation 345–360拥有finite新item参数对齐/初始化，DynamicBytePatch 362–380拥有可学习patch及block/selfspeculation，但缺**固定rule split→可计算word latent、旧backbone迁移、双clock/双KV与压缩非吞吐**联合边界。不重复HAT论文模块清单、不写Ch12/serving其他owner。拟在360 FVT反侧后、362 DynamicBytePatch标题前插下面两段；只增加本family章末注，尚未授PRE/锁。

### 两段逐字 PRE

固定词表迁移仍为每个新 item 分配离散参数；另一条分支则保留确定的文本切分规则，让开放字节串经过因果局部 encoder，再由组内 cross-attention 计算一个 word-level latent，交给全局 backbone，最后用已移位的 next-word latent 条件化逐 byte decoder。这并非“没有分词”：Unicode、camel case、空白与标点规则仍决定组边界；变化在于不再为所有可能的 word 保存固定查表行。复用旧 backbone 也不是热换 tokenizer，旧 embedding 与 LM head 被新 encoder、connector 和 decoder 替换，必须通过冻结起步与继续训练恢复接口。固定 subword/checkpoint 在无需迁移或兼容验证更重要时仍是合理基线。<!-- source-family:SF-2026-ARXIV-2603-15953 -->

较短的全局序列也不自动成为较快的服务：word 内的 byte 生成可以只走轻量局部环，跨 word 边界才再次调用 backbone，因此一次请求同时持有 byte/word 两种进度与不均匀映射的两份 KV；只有两边都能继续分配，它才可前进。批内等待边界以提高 backbone 利用率，会与输出延迟相冲突，字节层的小参数量也可能伴随更大的 activation。[受限迁移与 serving 说明](https://arxiv.org/html/2603.15953v1)明确报告当前批处理吞吐低于 FLOP-matched tokenizer 模型；bytes-per-backbone-position 是压缩单位，不是端到端收益，任务质量也有反退。迁移训练、规则边界、双状态协调或目标流量回归不合算时，应保留稳定词表与普通生成路径；下面的 dynamic patch 分支则进一步把边界选择本身交给模型。

### 拟章末注（不复制人员/验收）

- `SF-2026-ARXIV-2603-15953` — Daily `2026-03-19`补`03-18`自然日；[HAT exact-v1](https://arxiv.org/html/2603.15953v1) §3.1–3.4/4.2/6/7.1–7.3.1及直接质量反侧，2+2+3=7。只采用rule-split/learned-word接口、旧backbone适配与byte/word双clock/KV成本；tokenizer-free非无规则，压缩非吞吐，FLOP-matched批处理反退/任务质量反侧近正文。不授热换兼容、普遍质量/加速或生产SLO；未核代码或复现实验。

## 2603.15965 MoLoRA — 2+2+2=6，中心争议拟暂缓

[精确v1](https://arxiv.org/html/2603.15965v1)，实际§2–§8/Alg1/Eq2–11/Thm3.4–3.7/T1–8及必要A/B.1/B.2/D.1/E.1/E.3–E.7/T13–17。潜在增量：请求meta×token modality的composite target与 histogram/dispatch/groupGEMM复用，vocab-range无法辨domain时learnedTop-k adapter gate，加固定resident slot避免criticalpath paging并支持graph。必要条件contiguous可辨词表range、finitehotset与已校准gate；不是多模态encoder输出一律有integer-vocab身份，不授任意adapter无router校准可加入。

中心反证必须同留，不能删或降分：Thm3.7 Eq7把逐token `x_i A_m B_m` 写成同group所有j变换之和；取两同组token、AB=I时右端x1+x2而左端x1，不相等，普通tokenwiseadapter不等block-sparse Attention。Thm3.6 KN下界只对作者强制K完整passes的baseline模型成立，不能称任意correct per-sequence机制必需；Thm3.5“词表即optimal”把需要证明的optimal路由作为假设。§4.4 1.7B四rank32 GRPO adapter对8B没有等训练/混合adapter/单adapter/静态混合预算控制；E.7只监督classify4Bembedding，分类正确不是独立语义能力组合因果。

评价反侧：T13 single Val3.435低于oracle3.819、MoLoRA3.555及L3.599，trainingloss改善不支持validation优势；T16 fixed10.9×/k1 12.1×/k2 27.6×/k4 48.8×单adapter开销不能只称router免费。§7.5的67×一处归graph、一处归主paging与graph增量1–2×，来源口径冲突；D1graphCV在batch64 .33>paging .32、batch256 .07>eager .01，不能授所有workload方差下降。fullTransformer T7明确是强制Kpass simulation、T8只是Chameleon-style d2048/L4/K2，不是Chameleon完整端到端。H100/CUDA13/torch2.9、d4096/r64/4modalities，100warmup/1000median；图B2 H100NVL/8adapters是另配置，precision、完整I/O长度、请求arrival/concurrency、SLO、quality-training预算及seeds=Not Disclosed。

拟本窗**争议/暂缓**，保全family6分和已读mechanism/negative；不用其中心optimal/equivalence/quality/productionclaims进入Books，不将未解决claim挂名“已有覆盖”。actual Ch30既有条件gate与composition论点仅供以后重开对照，尚未授新采用。定点重开需Eq7有效修正/严格适用假设、非K-pass强制baseline的可比执行评价及quality训练/路由控制；不需要全部artifact/所有版本史。待独立复核中心反证与隔离裁决，普通已读不是访问受阻。
