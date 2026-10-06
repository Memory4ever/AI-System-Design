# 首批必要证据与 Books 差额（等待非作者复核）

本日窗口不变。实际读取当前合同：AGENTS.md；docs/RESEARCH_CONTRACT.md；docs/REPORT_CONTRACTS.md；CODEX_RESEARCH_PROMPT.md；docs/RESEARCH_SOURCES.md 使用说明/每日14/arXiv主题；ROADMAP.md；docs/LEARNING_STATE.md 顶部本轮 checkpoint。旧 V2.1 只留历史材料，不继承验收。

## [KVP 2602.10238v1](https://arxiv.org/abs/2602.10238v1)

准入 2+1+2=5；确认长期缺口后仅受影响命题深入。官方 PDF 元数据 /arXivID 精确绑定 v1，第一页 Date February 12, 2026；arXiv Submitted 10 Feb 2026 19:34:15 UTC 不是首公开，v1 Updated 12 Feb 01:04:27 UTC，DataCite Created 02:49:44 UTC 是已公开上界。官方公告规则与该批 v1 可给窗内公开范围推定，不把 Updated 冒充实际首公开时刻。HTML 的 August 24, 2026 未被采用为论文日期。

实际方法 §3 + PDF pp15–16/A.1–A.3：每 head 的两层 MLP 只消费 K/V/位置，离线完整 QKV traces 用未来 attention mass 构造跨 budget ranking reward，RLOO 学离散排序；112 agents（Qwen2.5 7B GQA 4 KV heads×28层）。Nested optimal subset 是“同一排序满足全 budget 最优”的必要假设，不是一般未来效用定理；future attention mass 仍是代理，不等于答案质量真值。Agent 之间不建模跨 head 交互。

§4：均匀 head/layer budget；所有 baselines 的 binary selection 改全排列比较。Prefill 通常包含 final question，BoolQ/GovReport 特意排除；不能把这种协议推广到所有在线场景。RULER/OASST约4k独立 train/test，再 downstream 零样本；更长 context 外推只是受测范围。§4.2 对比同 architecture/data 的 differentiable-sort训练，部分方法不收敛；不证明一切排序必须用 RL。

A.2：始终保留 first4/last16；FlexAttention mask **模拟 eviction**，没有证明实际 KV tensor/block compaction 或 memory reclamation。A.3：一次性 trace 采集需要完整模型 forward；8×H100 offline agent training <30min 是作者成本，不含普遍生产优化。112×0.65M =72.8M 参数，作者 FLOPs估算 prefill +约1%；only-once-after-prefill 使后续 decode 不再调用 scorer。Figure6 是 **单 KV head eviction score时间**，B200 bf16/TF32、取 eager/compiled 较快者、30runs，10k context0.71ms 对 full-model prefill404ms；忽略 TOVA/SnapKV attention recomputation。不能用这个不同比较层级的570倍比值授端到端加速、SLO或多租户保证。

Books 实际读 Ch45 420–495：已有 past attention/future utility 不等同、结构/Agent region correction、policy proposal与物理删除owner边界；没有离线 future-label 学习 K/V-only 全 budget ranking这条替代分支。拟在 semantic-region 后/model-driven GC 前增加一段“历史proxy→离线未来标签→学习ranking，但代理、模型/数据版本、mask vs physical compaction与OOD回退仍需验收”。owner INFER-KV-CACHE，目标 books/part-05-inference-system/45-why-kv-cache-speeds-up.md。请求先独立 Source/差额复核，再该文件窄写锁；未写。

## [SnapMLA 2602.10718v1](https://arxiv.org/html/2602.10718v1)

准入 2+2+2=6；确认具体跨算子长期缺口后受影响命题深入。§3.1–3.3/§4/AppC 已实际读取。MLA shared latent 内容小量级，RoPE 大量级；content 用 per-token FP8E4M3，RoPE 留 BF16，inverse content scale 注入位置项让 QK 同域并于softmax前恢复原score单位。V 与 K 共享 latent、scale 沿序列 reduction 轴，所以不能把每 token V scale 移到 PV 完整 GEMM 之后；需要先乘 P_j，再量化 P，并同步调整 online softmax accumulator 的 denominator/output、max rescale和交替 warp-group pipeline。AppC 的P/γ双缓冲readiness防止重用仍在被消费的状态，是具体数据供给约束。

§4.1：DeepSeekV3.1/LongCatFlash560B，8×Hopper NVLink，SKU Not Disclosed。Quality不是无损：DeepSeek AIME25 87.92→85.42、GPQA84.15→82.57、ArenaHard57.1→55.5；LongCat GPQA81.5→80.24。Table2独立量化RoPE/scale粒度控制支持位置项留高精度，不能外推所有模型可同格式。
§4.4 generation最大吞吐允许 FP8 **更大 batch**，DP8TP1最高1.91×不是相同 concurrency/SLO比较；输入16k–128k，output length/concurrency/SLO Not Disclosed。固定batch kernel结果（32，H16–128，MTP1/2）不是完整 Serving。没有跑实现或复现实验。

Books actual Ch49 850–910/1120–1170：已解释quantization粒度、metadata轴和outlier高精度/统一scale一般原则，尚未承载“shared K/V 的 per-token scale 在 PV reduction轴，必须进入乘法之前并维持 online-softmax状态一致”具体机制。owner INFER-TENSORRT-LLM；目标 books/part-05-inference-system/49-tensorrt-llm.md，拟在量化kernel合同处窄补MLA混合精度和scale不能跨reduction移动的两段。先请求 Source/差额复核，未抢锁/未写。

## [TVCache 2602.10986v1](https://arxiv.org/html/2602.10986v1)

2+2+2=6 标准审阅支持有限结论。§3–4已实际读：规范化完整history树，最长prefix snapshot restore后真实执行suffix，refcount与unused-subtree eviction约束并发；pure-tool annotation另一路。等价保证限定 deterministic tool、同 initial environment；不能推广clock、external依赖或权限变化。
§4 Docker easy128CPU128GB/medium30CPU200GB；rollout train mean20.2/25.3%（4B/14B）和14.2/16.7%；6.9× toolcall median不是训练总加速。SQL纯工具 remote sqlite network55.8ms，cache hit33.11%，56.6→6.5ms是hit路径，不代表全程8.7×。Video工具server L40S48GB、128CPU128GB，hit64.3%但straggler降低batch增益；作者API token cost估计不等账单。Task reward控制支持受测正确性而非任意真实外部系统重放。

owner AGENT-TOOL-CALLING；实际读取 books/part-07-agent/78-tool-calling.md 344–378：正文完整history/initial environment匹配、prefix snapshot、principal/dependency/validity是作者之外工程要求、clock/external状态失配bypass、在途引用回收均已承载。决定 **已有覆盖/No Change**，不是主题近似；等待独立 Source+actual owner确认。

## [Partial TEE 2602.11088v1](https://arxiv.org/html/2602.11088v1)

3+2+2=7，具体协议秘密基复用安全变化强制深入。§3–6已实际读：TEE当理想黑箱，但host OS/GPU可读改、有协议/架构知识；fresh coefficient不修复static secret basis复用的低维子空间。Confidentiality：多观测project noise，chosen-activation接口恢复permutation/weights；不是只给end-user text API也可同样攻击。Integrity：两组independent input sets的intersection恢复challenge基，伪造check；限 Soter/TSQP等具体参数与oracle，不授所有TEE失败。

§6 A10080GB+双XeonSilver4309Y、SGXv2 EPC4GB/heap512MB、Rocky9.5 SDK2.25/PyTorch2.5.1。6min 是 Llama8B **单layer**；405B选择layer scaling不是整405B模型已加载攻击。Table5 8B GSM8K82.34与原模型一致、throughput240vsTEE18是作者受控配置，不是安全或生产performance保证。尚未核验任何攻击代码，未采用附录fresh-secrets方案的完整防御保证。

owner PLATFORM-SECURITY；实际 books/part-06-ai-infrastructure/72-security.md 2786–2792 完整承载static basis复用、nonce/request binding/keyepoch/allowed reuse/crash recovery，fresh secret/domain separation需可证明与not-all-TEE边界。决定 **已有覆盖/No Change**。现成正文工程nonce要求是设计推断，不说作者实现已证明。等待独立 Source+owner核。

## [Repetition 2602.11149v1](https://arxiv.org/html/2602.11149v1)

2+1+2=5，现有长期缺口受影响内容深入；§2–4.4实际读。Fixed update budget =epochs×samples，batch1；不是同FLOPs/token（trajectory lengths不同）。Qwen3 4B/8B、OLMo3 7B，8bitAdam/bf16，10%warmup+cosine，至多H10094GB24hr；DolciThink<10ktrace，nested200–51200，holdout1000。AIME24/25各30题16samples，GPQA4samples/outputmax30k。LR在51200一epoch benchmark选择后复用，非完全blind eval。

Table4固定51200updates：OLMo32epochs tokenacc100%，任务acc38.8%，64/128平38.9/38.4；Qwen8B16ep37.6%/97.7%tokenacc，32ep36.2%且全memo；4B8ep29.1%/96.1%，16ep25.7%开始全memo，128ep12.4%。**并非全memorization总是最优**，更不是重复创造新data。
§4.3受测范围出现 train tokenacc饱和、heldout tokenCE变差但generated reasoning任务能力提升；这是 evaluation objective不等价的实证，memorization本身既非可用性充分条件也非必然failure。作者未给因果mechanism，tokenacc停止proxy需要task/transfer外部检查。
Weak teacher trace与strongteacher任务/难度不同，不能推导一般错误trace更好；termination改善仅相关，不能归因causal。§4.4受测MMLU二路线皆有forget，不授全部能力无额外遗忘。

owner TRAIN-SFT；actual books/part-04-training-system/29-sft.md 605–633已经写 repetition是sampling、梯度频率、验证/heldoutvariants与transfer/memorization，**没有** CE/逐字记忆和generated task gain可以反向的评价边界。拟在repeat schedule后/onpolicy distillation前窄补两段：在固定更新实验中可出现token-level过拟合与任务收益共存；不把train tokenacc/loss作单一停训规则，应联合受测任务/迁移/forget与真实token成本；memorization代理不是因果保证。请求独立 Source+差额后 Ch29窄写锁。未写。

支持原文返回保留 V3_CORE_FIRST_0..3、V3_RESUME_CORE_1、V3_FIRSTPUBLIC_CORE_1 及精确KVP PDF；Books actual不是legacy JSON。以上是作者提出判断，**尚非 Evidence/POST通过**。

