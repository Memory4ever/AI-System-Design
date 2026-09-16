# 2026-06-09 V3 recovery checkpoint（已解除）

> **2026-09-11 final update：** 本文件保存恢复过程中的中间队列，不再是当前状态依据。两轮非作者审计最终冻结 112 Candidate / 1,123 Close；112 项 Evidence 与 Books Decision 已逐项完成，结果均为 `已有覆盖`，new Integrate = 0。2606.09774 撤回采用链已清理。权威结论见当日 README、`V3_SCREENING_LEDGER.md` 与 `JUNE_09_SECOND_FULL_TABLE_AUDIT.md`；下方旧队列仅用于解释审计演进，不表示仍有待执行工作。

## Historical denominator checkpoint（非权威）

可读基线为 1,235 raw / 99 prior / 1,136 closure proposals。896 项共用 incremental closure 理由被反例击穿后已逐题重审，其余 240 项也完成 title-first、边界项完整摘要复核。权威分母冻结为 Candidate 125 / Close 1,110：old prior 保留 77、关闭 22；old closure 恢复 48、维持关闭 1,088。Training-Inference Kernel Contracts（2606.07581）、Agent Skill System（2606.07586）、routing plateau（2606.07587）与 action-boundary failures（2606.07595）均恢复。逐项依据与 12+12 FP/FN 抽查见 V3_SCREENING_LEDGER.md。当前 blocker 转为 48 个新恢复 Candidate 的评分/Evidence/Books Decision，以及 surviving Integrate 的 Books trace-to-body。

## Historical Books body queue（已被终审覆盖）

已有正文 anchor，且 survives 当前分母：

- SF-2026-ARXIV-2606-07881 → books/part-04-training-system/38-pipeline-parallel.md（约 328 行）。
- SF-2026-ARXIV-2606-09692 → books/part-06-ai-infrastructure/69-trace.md（约 230 行）。

旧 Integrate SF-2026-ARXIV-2606-09774 撤回：论文只讨论用轻量 coding-agent adapter 配置科学模拟器，属于当前延后的 AI-for-Science 分支；应删除 books/part-07-agent/81-workflow.md 中相应 semantic-body-binding 与 daily-books-trace，而不是继续修订日期。

其余三十六项只找到 daily-books-trace，且均 survives 当前分母，需补写正文：

- books/part-07-agent/77-memory.md: SF-2026-ARXIV-2606-07684
- books/part-07-agent/82-multi-agent.md: SF-2026-ARXIV-2606-07790, SF-2026-ARXIV-2606-07805
- books/part-06-ai-infrastructure/66-evaluation-system.md: SF-2026-ARXIV-2606-07783, SF-2026-ARXIV-2606-07822, SF-2026-ARXIV-2606-07834, SF-2026-ARXIV-2606-07874, SF-2026-ARXIV-2606-08200, SF-2026-ARXIV-2606-08960, SF-2026-ARXIV-2606-09809
- books/part-06-ai-infrastructure/72-security.md: SF-2026-ARXIV-2606-07808, SF-2026-ARXIV-2606-07833, SF-2026-ARXIV-2606-07867, SF-2026-ARXIV-2606-07943, SF-2026-ARXIV-2606-08403, SF-2026-ARXIV-2606-08539, SF-2026-ARXIV-2606-09005, SF-2026-ARXIV-2606-09084
- books/part-06-ai-infrastructure/67-monitoring.md: SF-2026-ARXIV-2606-07889
- books/part-05-inference-system/45-why-kv-cache-speeds-up.md: SF-2026-ARXIV-2606-07878
- books/part-05-inference-system/56-inference-scheduling.md: SF-2026-ARXIV-2606-07923, SF-2026-ARXIV-2606-09613
- books/part-07-agent/81-workflow.md: SF-2026-ARXIV-2606-08049, SF-2026-ARXIV-2606-08919
- books/part-07-agent/84-agent-platform.md: SF-2026-ARXIV-2606-08106
- books/part-05-inference-system/44-decode.md: SF-2026-ARXIV-2606-08411
- books/part-04-training-system/36-distributed-training.md: SF-2026-ARXIV-2606-08476
- books/part-05-inference-system/55-pd-disaggregation.md: SF-2026-ARXIV-2606-08635
- books/part-07-agent/80-reflection.md: SF-2026-ARXIV-2606-08671
- books/part-05-inference-system/54-gpu-memory.md: SF-2026-ARXIV-2606-08761
- books/part-07-agent/76-rag.md: SF-2026-ARXIV-2606-08950
- books/part-05-inference-system/43-prefill.md: SF-2026-ARXIV-2606-09441
- books/part-05-inference-system/53-kserve-llm.md: SF-2026-ARXIV-2606-09643
- books/part-05-inference-system/49-tensorrt-llm.md: SF-2026-ARXIV-2606-09682, SF-2026-ARXIV-2606-09686
- books/part-04-training-system/31-rlhf.md: SF-2026-ARXIV-2606-09711

## Historical trace date queue（已被终审覆盖）

前二十五项 trace 日期错误，应改为 2026-06-09：

- 当前 2026-06-06（十三项）：07684, 07783, 07790, 07805, 07808, 07822, 07833, 07834, 07867, 07874, 07878, 07881, 07889。
- 当前 2026-06-07（五项）：07923, 07943, 08049, 08106, 08200。
- 当前 2026-06-08（七项）：08403, 08411, 08476, 08539, 08635, 08671, 08761。

上述简写均指 SF-2026-ARXIV-2606-*；从 08919 到 09809 的十四项日期已正确。
