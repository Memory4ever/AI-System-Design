# 2026-05-06 Fresh-context Coverage Challenge

**Auditor:** root（非 05-06 author）

**Status:** Open — author repair required

## Finding

对 513/513 screening ledger 做 fresh-context adversarial false-negative review 后，当前 31-family denominator 不能通过 Coverage Gate。下列分母前闭合项明确涉及长期 AI System 的 state/data/control ownership、training/inference runtime、evaluation contract、security boundary 或 Agent workflow，不能以“局部方法”泛化拒绝；它们必须先进入 denominator 完成 exact-v1 Source Review，再逐项决定 `Integrate`、`No Change` 或有证据的拒绝。

## Required Reopen

| arXiv | 必须重开的系统理由 |
| --- | --- |
| 2605.03275 | production RAG 的 freshness、tenant scope 与同步 state ownership |
| 2605.03327 | token-level RL credit 与 bounded divergence 的训练控制分支 |
| 2605.03379 | repeated inference 的 test-time compute / reliability contract |
| 2605.03408 | observation 与 reward interface 的联合生成和 executable authority |
| 2605.03425 | DP noise filtering 与 optimizer second-moment state calibration |
| 2605.03505 | observability-driven RCA search、evidence 与 production gap |
| 2605.03561 | exascale telemetry ingestion、GPU analysis 与 topology localization |
| 2605.03566 | tensor lifting 的 compiler/runtime execution contract |
| 2605.03596 | workspace Agent 的 file-dependency evaluation contract |
| 2605.03644 | many-shot ICL 的 KV reuse 与 cache identity |
| 2605.03667 | low-rank pretraining 与 activation sparsity 的 execution trade-off |
| 2605.03677 | on-policy distillation 的 post-training handoff |
| 2605.03971 | hallucination detector 与 self-judgment consistency contract |
| 2605.03986 | Agent workflow composition、recommendation 与 execution ownership |
| 2605.04036 | search-Agent trajectory data 与 capability training loop |
| 2605.04039 | capability 与 safety 的不同 scaling/evaluation contract |
| 2605.04135 | benchmark freshness 与 frontier capability misrepresentation |
| 2605.04172 | programmable memory hierarchy 的 compiler/runtime contract |
| 2605.04209 | parameter-space backdoor 与 artifact security boundary |
| 2605.04213 | GPU silent-data-corruption fault model 与 training/inference reliability |
| 2605.04236 | adaptive ensemble budget 与 calibrated commit signal |
| 2605.04256 | heterogeneous physical neural network control plane |
| 2605.04269 | non-stationary training 下 Adam/SGD state trade-off |
| 2605.04295 | semantic entropy 与 conformal uncertainty calibration |
| 2605.04312 | multi-agent benchmark contamination/saturation contract |
| 2605.04333 | large-scale AI network multipath、failure bypass 与 training tail latency |
| 2605.04341 | compute-budgeted LoRA/distillation 与 inference structure |
| 2605.04356 | online natural-language feedback 与 proxy over-optimization loop |
| 2605.04361 | conditional context injection 对 multi-agent exploration 的反例 |
| 2605.04375 | Experiment-as-Code 的 compile、policy、resource 与 physical effect boundary |
| 2605.05253 | enterprise RAG 的 noisy/conflicting/missing evidence benchmark contract |
| 2605.08192 | frontier-safety claim 的 tiered reproducibility contract |
| 2605.10959 | quantization 的 accuracy/latency/compression viability gate |

## Gate Consequence

- Coverage Gate: `Open`
- Evidence Gate: `Open`
- Books Gate: `Open`
- Completion Status: `In Progress`

找到候选不等于已完成全文审计。Author repair 必须为每项补齐 exact-v1 Method、Evaluation、limitations/counterevidence、Score V2、owner/adjacent comparison 与 disposition；root 随后重新执行 fresh-context audit。
