# 2026-06-02 V3 candidate evidence — batch 01

本批覆盖从旧 closure 恢复的前 10 个 Candidate。准入结论来自当前 `V3_SCREENING_LEDGER.md`；本文件不使用 legacy disposition、Books trace 或 post-Review note 授权候选或正文。评分按 Design Delta / System Reach / Durability（0–3）记录；5–6 分执行标准审阅，7–9 分读取 exact-v1 中足以验证 mechanism、evaluation 与反证边界的正文。

## Candidate ledger

| ID | 公开时间（UTC+8） | 评分 | Review | Stable owner | Books Decision |
| --- | --- | --- | --- | --- | --- |
| 2606.00021 | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 2+2+2=6 | 标准完成 | `INFER-SPECULATIVE-DECODING` | 已有覆盖 |
| 2606.00024 | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 3+2+2=7 | 深入完成 | `INFER-KV-CACHE` | 整合已写入 |
| 2606.00093 | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 3+2+3=8 | 深入完成 | `PLATFORM-EVALUATION-SYSTEM` | 整合已写入 |
| 2606.00144 | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 2+2+2=6 | 标准完成 | `INFER-SPECULATIVE-DECODING` | 已有覆盖 |
| 2606.00152 | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 3+3+3=9 | 深入完成 | `PLATFORM-SECURITY` | 整合已写入 |
| 2606.00279 | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 3+3+3=9 | 深入完成 | `PLATFORM-EVALUATION-SYSTEM` | 已有覆盖（当前正文） |
| 2606.00395 | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 3+3+3=9 | 深入完成 | `TRAIN-GRPO` | 整合已写入；正文锚点“MoE Route Replay 也属于 Behavior-policy Identity” |
| 2606.00448 | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 3+3+3=9 | 深入完成 | `PLATFORM-SECURITY` | 已有覆盖 |
| 2606.00485 | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 3+3+3=9 | 深入完成 | `PLATFORM-SECURITY` | 整合已写入 |
| 2606.00487 | 2026-06-02T08:00:00+08:00 ～ 2026-06-02T09:00:00+08:00 | 2+2+2=6 | 标准完成 | `INFER-SPECULATIVE-DECODING` | 已有覆盖 |

## Evidence and Books comparison

### 2606.00021 — SENSE

- Primary / exact-v1: <https://arxiv.org/html/2606.00021v1>。
- Method: §3.2 用 target hidden states 做 semantic retrieval，§3.3 用 soft-gated evaluation 接受语义近似候选，§3.4 把 retrieval、draft 与 target evaluation 组织为统一路径。
- Evaluation: §4 在 LLaMA/Qwen 与多领域 workload 上比较 acceptance length、latency/speedup 和输出质量；这些结果只支持所测模型、数据与实现。
- Non-proof: D.1/D.6 与后续讨论没有把 semantic acceptance 证明成 bit-exact 或 distribution-preserving。它改变的是 sampling/quality contract，不能沿用“lossless speculative decoding”标签。
- Books comparison: `books/part-05-inference-system/48-speculative-decoding.md` 在 Review notes 前已区分 exact target acceptance 与 lossy/semantic verification，并要求 matched sampling/truncation baseline、质量预算和保守 exact fallback。因此本 family 为 `已有覆盖`，不新增正文。

### 2606.00024 — ART

- Primary / exact-v1: <https://arxiv.org/html/2606.00024v1>。
- Method: §3 在 attention kernel 内跟踪 accumulated output 的 magnitude 与 direction stability；当剩余 KV blocks 的贡献进入受控上界后终止 traversal。它叠加在 dense/sparse KV policy 上，不接管 KV selection owner。
- Evaluation: §4 报告 LongBench、RULER Needle-in-a-Haystack、不同 cache policy 的吞吐与质量；结果是有限模型、context length 与 kernel 路径的实验信号。
- Non-proof: 没有证明任意 attention head、position、mixed precision 或 production batching 都满足相同 termination threshold；稳定判据失配时必须回退完整 KV traversal。
- Books comparison / final: 当前 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 已覆盖 KV selection、sparse residency、prefetch 与验证；本项差额已写入正文锚点“Value-aware Termination 只能提前结束读取，不能接管正确性”，并保留 full traversal fallback。

### 2606.00093 — Agreement Metrics for LLM-as-Judge Evaluation

- Primary / exact-v1: <https://arxiv.org/html/2606.00093v1>。
- Method: §2–§6 把 judgment scale、retained population、abstention/invalid output、item/rubric pooling 与 metric identity 组合成 measurement protocol；§3–§4 说明若干相关统计量的等价与 Cohen’s kappa 对边际分布的敏感性。
- Evaluation: §7 将相同 verdicts 置于三个已发表 judge evaluation 的不同协议中重算，显示 protocol choice 可显著改变 accuracy/kappa；该结果证明可重构性问题，不证明某个 metric 普遍最优。
- Non-proof: §8 限定 observed-count、有限样本、stochastic generalization、weighted-kappa 与 human ground truth 可靠性；开放生成、高风险 truth authority 仍需独立 verifier/人工证据。
- Books comparison / final: 差额已写入 `PLATFORM-EVALUATION-SYSTEM` 正文锚点“Judge Agreement 不是单一数字”；`agreement_run` 保留 population、scale、missing/abstain policy、pooling 与 metric，且 measurement inference 不拥有 truth。

### 2606.00144 — BudgetDraft

- Primary / exact-v1: <https://arxiv.org/html/2606.00144v1>。
- Method: §3 让同一 sparse-KV drafter 在多种 KV budgets 下学习，并以 full-cache teacher/branch 保持 acceptance-aware alignment；verifier 始终保留 full KV。
- Evaluation: §4–§5 在 PG-19、LongBench、LWM 与 A100 上比较 4K–16K context 的 acceptance、memory 与端到端速度。
- Non-proof: §6 limitations 及实验范围不支持其他 drafter/target family、longer context、batching/serving tail 或任意稀疏策略；budget mismatch 时应回退 full-cache drafter 或普通 autoregressive decode。
- Books comparison: `books/part-05-inference-system/48-speculative-decoding.md` 已把 drafter capacity/residency、acceptance、target verification cost、KV budget 与 fallback 放入同一控制环；`45-why-kv-cache-speeds-up.md` 已区分 sparse state 与 full correctness owner。multi-view training 是该 contract 的一个实现，不再新增长期正文，判 `已有覆盖`。

### 2606.00152 — PrivacyPeek

- Primary / exact-v1: <https://arxiv.org/html/2606.00152v1>；artifact: <https://github.com/Xuan269/PrivacyPeek-Resource>。
- Method: §3 将 privacy audit 前移到 acquisition：从 tool-call trajectory 检查 agent 调用了什么工具、收到什么数据，并用 follow-up probe 测量已进入 context 但尚未披露的信息是否可被诱出。
- Evaluation: §4 使用 1,182 cases、7 类 acquisition behaviours、16 domains、10 agents/4 model families；它支持“过度获取”是可观测 failure mode，不支持所有生产 agent 的发生率。
- Non-proof: §5–§6 明示 synthetic English cases、有限 agent/tool setup、prompt defense 与 deployment enforcement 边界；benchmark 没有证明 production policy 已能阻止 acquisition。
- Books comparison / final: 差额已写入 `PLATFORM-SECURITY` 正文锚点“Tool Response 在进入 Context 时就要执行 Data-minimization Gate”，覆盖 acquisition-time field admission、receipt 与更窄 scope fallback。

### 2606.00279 — Bit-Exact AI Inference Verification

- Primary / exact-v1: <https://arxiv.org/html/2606.00279v1>。
- Method: §3 固定 model/runtime/input/quantization/parallel identity，并在没有 backend atomics 的路径上观察 deterministic-but-hardware-dependent bits；§4 软件复现 tensor-core arithmetic、reduction order 与 rounding。
- Evaluation: §3.2/§4.4 跨多种 NVIDIA GPU、vLLM/HF paths 验证重算；证明范围绑定披露 operator 与硬件变体。
- Non-proof: §5 限定 dense FFN、部分 NVIDIA 路径、经验性的 MoE 与未建模 operator；bit match 不是 security attestation 或性能等价。
- Books comparison: 当前 `books/part-06-ai-infrastructure/66-evaluation-system.md` Review notes 前已有“Bit-exact Replay 可以脱离同型硬件，但不能脱离数值路径身份”，覆盖旧硬件 replay、software emulator、完整 identity、unsupported-op failure 与 tolerance fallback。判 `已有覆盖（当前正文）`。

### 2606.00395 — PR2

- Primary / exact-v1: <https://arxiv.org/html/2606.00395v1>。
- Method: §3 定义 rollout/training 之间的 router drift 与 frozen routing replay staleness；§4 用旧 snapshot 上的轻量 evolution predictor 生成短时 predicted route，rollout 采用该 top-k route，training 重放同一 route 以稳定 importance estimation。
- Evaluation: §5 在 Qwen3-30B-A3B、Moonlight、OLMoE 与多 reasoning benchmark、不同 off-policy gap 上比较稳定性和任务表现。
- Non-proof: predictor 只估短 horizon，cached/predicted route 可能阻止未入 route 的 expert 获得梯度；模型更新、router temperature、top-k、rollout batch 与 predictor revision 失配时必须拒绝 replay，回退 current-policy routing 或更严格同步。
- Books comparison / final: 已写入 `TRAIN-GRPO` 正文“MoE Route Replay 也属于 Behavior-policy Identity”。该 owner 持有 predicted route、router/policy revision 与路由约束组成的 rollout/training replay contract；分布式训练仍只持有 placement/collective data plane，并保留丢弃、重新 rollout 或 current-policy routing fallback。

### 2606.00448 — When Safe Skills Collide / SkillReact

- Primary / exact-v1: <https://arxiv.org/html/2606.00448v1>。
- Method: §3–§4 建立 deterministic pair composition、双 rater+human adjudication 与 action exploitability harness；安全对象从单 skill revision 扩展为 installed skill set/capability union。
- Evaluation: §5–§6 在 1,520 ClawHub skills、211,575 pairs 与不同 host-model dispositions 上区分 recall-oriented static candidates、human-valid risk 和实际 tool issue。
- Non-proof: §8 说明静态规则会 over-approximate、真实 exploit 依赖 host/runtime、regex 有 false positive 且人工校准只覆盖样本；组合命中不能自动授权封禁。
- Books comparison: `books/part-06-ai-infrastructure/72-security.md` Review notes 前已写明 skill 审计要覆盖安装后动态行为、trigger 与跨-skill composition，静态 manifest/代码扫描不能代表 runtime authority，并保留 effect boundary/fail-closed release。该 paper 提供受限案例，不再新增正文，判 `已有覆盖`。

### 2606.00485 — Confused ChatGPT

- Primary / exact-v1: <https://arxiv.org/html/2606.00485v1>。
- Method: §3 把理想边界定义为 per-app subcontext + mediator，区分 user/platform-owned global context；§4–§5 描述 persistent first-party API writes、跨轮/跨 app confused-deputy chain 与两类 payload。
- Evaluation: §6 在六个当时模型上复验三个 context-pollution channels，证明 2026-05 所测 client/runtime 的 architecture gap。
- Non-proof: §8 限定 proprietary/evolving platform、client-side observation、作者自建 app/store review 与未部署 remediation；不能外推当前产品仍保留同一 undocumented behavior。
- Books comparison / final: 差额已写入 `PLATFORM-SECURITY` 正文锚点“App-local Context Namespace 阻止普通 Writer 获得跨 App Authority”，覆盖 provenance-tagged subcontext、mediator projection 与 fail-closed fallback。

### 2606.00487 — TAPS

- Primary / exact-v1: <https://arxiv.org/html/2606.00487v1>。
- Method: §4 将 diffusion marginal 转为 prefix-conditioned acceptance estimate，用 reach product 与 target-aware utility/cost 在固定 verification budget 下选择 prefix-closed subtree。
- Evaluation: §5 在公开 model/dataset 组合、batch size 1、A40/A800 上比较 acceptance、target latency 与 end-to-end speed。
- Non-proof: §6 仅覆盖 greedy temperature 0、single-request research prototype，未集成 vLLM/SGLang 或 production batching；candidate pool 决定性能上限。
- Books comparison: `INFER-SPECULATIVE-DECODING` Review notes 前已要求树形候选服从 causal-prefix reachability，并把 accepted progress、target verification cost、tree width/depth、batch 与 conservative sequential fallback 联合结算。TAPS 是这个长期 contract 的局部算法实例，判 `已有覆盖`。

## Batch result

- Evidence closed: 10 / 10。
- Books: 5 `已有覆盖`，5 `整合已写入`，0 `整合 proposal`，0 `仅报告`，0 `暂缓`。
- Proposal queue: 空。2606.00024、2606.00093、2606.00152、2606.00395、2606.00485 均已完成正文绑定。
- 写入后按当前 owner 正文复核；未发现重复合并或 trace 代替正文。
