# 2026-05-05 V3 非作者最终语义终审 — 2026-09-15

**复核者：** `fresh-context:may05_fresh_final_review`

**角色隔离：** 本复核者未参与 2026-05-05 的作者修复或 root Books 写回；本轮没有修改 Books、扩大日期窗口、重新抓取来源或替作者完成候选审阅。

**结论：** **FAIL**。Daily 必须保持 `进行中`。现有 34 项 Books 写回本身通过正文终审，但 Candidate Denominator 存在新的明确 false negative，且 canonical ledger、Daily 与作者 checkpoint 的状态不一致，因此不能签发完整 Gate。

## 1. 已通过的账目与 Evidence 边界

- 窗口仍为 `2026-05-04T09:00:00+08:00 ～ 2026-05-05T09:00:00+08:00`。
- 分母守恒可复算：`1058 raw = 145 retained + 913 pre-denominator closure`；arXiv ID 与 Source Family ID 均为 1058 个唯一值。
- 145 个 retained 均有三维评分，三个分项范围与 Total 算术一致；所有 7～9 分项目均进入 deep review。
- Evidence 账目可复算为 `74 deep + 69 standard + 2 blocked = 145`。除 `2605.02206v1` 与 `2605.02375v1` 外，143 项均有 exact-v1 URL、Method、Evaluation、Limitations locator、证据摘录和 claim boundary。
- 两个 exact-v1 blocked 没有 Method/Evaluation/Limitations 伪定位，也没有被用于正面结论或 Books；隔离有效。
- 本地 exact-v1 缓存未检出 arXiv 官方 withdrawal notice。缺少本地缓存的已审阅项目仍保留 exact-v1 URL 和定位信息；这不等于重新证明其全文已读，本终审只核验当前证据包与 Books 语义是否一致。

## 2. 34 项 Books 写回终审结果

34 项 `Integrate Applied` 的目标 node 均能在 `ROADMAP.md` 解析到唯一章节；每项在对应章节正文中恰有一个 canonical source-family 或 semantic-body marker，且 marker 位于章末二级 `## Review notes` 之前。按 owner 分布为：

```text
WORLDVIEW-REPRESENTATION 2
MULTIMODAL-REPRESENTATION 2
MULTIMODAL-GENERATIVE-PARADIGMS 5
MULTIMODAL-EMBODIED-VLA 1
TRAIN-PRETRAINING 1
TRAIN-LORA 1
TRAIN-RLHF 1
TRAIN-GRPO 3
TRAIN-DPO 1
TRAIN-DISTRIBUTED-TRAINING 1
INFER-TENSORRT-LLM 1
INFER-SCHEDULING 1
PLATFORM-GPU-SCHEDULER 1
PLATFORM-EVALUATION-SYSTEM 1
PLATFORM-MONITORING 1
PLATFORM-SECURITY 5
AGENT-RAG 1
AGENT-MEMORY 1
AGENT-TOOL-CALLING 1
AGENT-WORKFLOW 1
AGENT-PLATFORM 2
```

逐项回读 marker 相邻正文后，34 项均不是 trace-only 或“已吸收”的空标签。正文能够定位旧方案/成立条件、约束变化、机制及状态或控制权、收益与代价、failure/fallback 和证据边界；新段落也处于相应机制主线的合理位置。四项 2026-09-15 root 写回（`2605.01208`、`2605.01913`、`2605.01959`、`2605.02323`）同样通过此检查。

109 项 `No Change` 均有存在的目标章节、现有命题和逐命题比较字段；本轮没有发现仅凭标题或 marker 宣称 Existing Coverage 的缺字段记录。这个结论只适用于当前 145 个 retained，不能弥补分母前漏收。

因此，**Books 写回子 Gate 通过，但 Daily 的整体 Books Decision Gate 仍因候选分母不完整而失败**。

## 3. Candidate Denominator 终审失败

913 个 closure 中有 467 项使用完全相同的终判句：

> 属于局部模型、算法或应用改进；未改变长期机制 owner、state/data/control ownership 或验收契约。

虽然每项前面附有题名和摘要片段，但相同终判没有真正解释本 family 为什么不能改变项目设计。对该高风险层按训练、生成、推理、证据与安全状态分层反查完整摘要后，至少发现以下 8 个明确 false negative：

| arXiv v1 | 完整摘要已明确给出的系统变化 | 最小 owner / 重开理由 |
| --- | --- | --- |
| `2605.01347v1` | 将 on-policy distillation 的 teacher 从单模型改为多 Agent debate collective，并为 agentic trajectory 增加 step-level sampling 与 divergence 分支 | `TRAIN-PRETRAINING` / `AGENT-MULTI-AGENT`；改变 teacher ownership、trajectory sampling 与训练目标 |
| `2605.01373v1` | 根据高信息密度 token 的早收敛状态执行 self-contrast remasking，并在稳定候选上并行提交 | `MULTIMODAL-GENERATIVE-PARADIGMS`；改变 diffusion LM 的 revision、remask 与并行解码控制 |
| `2605.01642v1` | 用低秩 reward basis、jury voting 与可更新 annotator weights 表达随时间变化的 pluralistic preference | `TRAIN-RLHF`；改变 reward state、聚合控制与版本更新合同 |
| `2605.01710v1` | 定义每次请求的 route receipt，记录 model alias、tier、endpoint、fallback 与 safety handling，并给出最小 schema/redaction model | `PLATFORM-MONITORING` / serving provenance；直接改变 runtime evidence artifact 和审计合同 |
| `2605.01733v1` | 以 clean-path confidence、entropy reduction 与 pathway disagreement 对自生成 caption 逐 query 授权 | `MULTIMODAL-REPRESENTATION` / `PLATFORM-EVALUATION-SYSTEM`；改变 evidence admission 与 hallucination failure path |
| `2605.01782v1` | 记录 prompt-anchored RAG execution trace，并以 counterfactual replay 把 poisoning 责任定位到字符级 span | `AGENT-RAG` / `PLATFORM-SECURITY`；改变 retrieval provenance、forensic state 与 remediation 粒度 |
| `2605.02144v1` | 用 Gaussian kernel attention 替换 Q/K/V 投影，保留 causal/sliding-window 接口并给出参数、FLOP 与质量取舍 | `MODEL-ATTENTION`；属于明确的 attention architecture alternative，不是单一应用结果 |
| `2605.02152v1` | 以低分辨率 draft 和 discrepancy verification 选择高分辨率 denoising token | `MULTIMODAL-GENERATIVE-PARADIGMS`；改变 diffusion editing 的 draft/verify、token state 与计算分配 |

这些项目是否最终进入 Books 仍须由 exact-v1 Evidence Review 与逐命题比较决定；但完整摘要已经跨过 Candidate Denominator 的贡献门槛，不能在全文审阅前直接关闭。它们全部位于上述 467 项通用 closure 层，说明这不是单个漏项，而是同一关闭模板造成的系统性风险。

**最小重开范围：** 不重扫 1058 个 raw identity，也不扩大日期。只重新语义筛选这 467 项通用 closure 层；优先检查 LLM distillation/alignment、diffusion/attention execution、runtime provenance、RAG/multimodal evidence 四个受影响簇。已具有 family-specific 关闭理由且不属于这些簇的 446 项 closure 可保持冻结。

## 4. 状态文件存在互相矛盾

1. `V3_CANONICAL_LEDGER.json` 仍把 `2605.01208`、`2605.01913`、`2605.01959`、`2605.02323` 记为 `Integrate Proposed — root writeback and independent review required`；`V3_EVIDENCE_REVIEWS.json`、Daily 顶部和实际 Books 已为 Applied。
2. Daily §5 仍写“本次最小修复新增 4 项 root 待写回队列”，但 `ROOT_BOOKS_WRITEBACK_20260915.md` 已证明四项 root 写回完成。
3. `V3_AUTHOR_CHECKPOINT.md` 仍停留在旧账 `1058 = 123 retained + 935 closure`、`24 Applied + 97 No Change + 2 blocked`，与当前 canonical / Daily 的 `145/913`、`34/109/2` 不一致。
4. canonical 顶层仍是 `root_books_writeback_complete_independent_review_pending`，但本次独立终审已经失败；后续作者修复必须生成新的明确 checkpoint，不能继续让旧 pending 状态冒充当前进度。

这些冲突不会改变 Books 中已存在的正文，但会破坏恢复、复算和下一位 reviewer 的输入边界，因此也是 Gate 阻断。

## 5. 精确修复与再次验收

1. 仅对 467 项通用 closure 层执行题名 + 完整摘要重新筛选，至少将上表 8 项移入 Candidate Denominator；对同簇兄弟项给出真正 family-specific 的 retain/closure 理由。
2. 对新增 retained 完成 exact-v1 withdrawal、Method、Evaluation、Limitations、三维评分、owner 和 Books 命题比较；blocked 只能隔离，不能用摘要补写机制。
3. 若出现新的 `Integrate`，由 root 按 owner 串行写回 Books；否则明确记录 `No Change` 或其他最终处置。
4. 从最终数组重新生成 retained/closure、Evidence 与 Books 汇总，并统一修复 canonical ledger、Evidence JSON、Daily §5 与 active checkpoint。
5. 由未参与上述修复/写回的 fresh-context reviewer 再次反查受影响 closure、所有新增 retained 和任何新增 Books 正文。

## 6. Gate 判定

- Window / identity conservation：**PASS**。
- Current retained scoring / Evidence structure：**PASS**；两个 external blocked 正确隔离。
- Existing 34 Books Applied semantic writeback：**PASS**。
- Candidate Denominator：**FAIL**；至少 8 个明确 false negative，467 项通用 closure 层必须定向重审。
- State consistency：**FAIL**；canonical、Daily 和 checkpoint 对 4 项写回及当前账目不一致。
- Daily：**Ongoing**。

## 7. 校验边界

- `scripts/validate_research.py --report papers/2026/05/05/README.md` 在本次记录写入后通过；它不能消除上述语义 false negative。
- canonical ledger 与 Evidence JSON 可解析；账目、评分 Total、owner path 与 34 个正文 marker 可机器复算。
- 本报告、本终审记录的本地 Markdown 链接检查与 scoped `git diff --check` 均通过。
- 本轮没有修改 Books，没有 stage、commit 或 push。
