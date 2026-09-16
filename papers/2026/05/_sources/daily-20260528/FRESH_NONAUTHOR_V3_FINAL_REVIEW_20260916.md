# 2026-05-28 V3 fresh non-author final review

**Reviewer:** `/root/may25_repair`（未参与 05-28 V3 author rebuild）  
**Reviewed at:** `2026-09-16T12:09:01+08:00`  
**Decision:** `FAIL — bounded repair required`  
**Report status:** 保持 `Ongoing`  
**Shared Books modified by reviewer:** `false`

## 1. 通过的独立挑战

- 窗口严格为 `[2026-05-27T09:00:00+08:00, 2026-05-28T09:00:00+08:00)`。
- arXiv 官方 availability 只能证明 `2026-05-27 20:00 ET = 2026-05-28 08:00 BJT` 的公告时点，不能证明 835 条 identity 的 batch membership；DataCite created/updated、OAI datestamp、submitted time 与连续 ID 均不能替代 membership。
- Google DeepMind 两页只披露 `2026-05-28` 日级日期，无法证明是否落在 09:00 截点前，因此隔离 2 项是正确的。
- MiniMax Agent Team 官方日期投影为 `2026-05-27T08:00:00+08:00`，比本窗起点早一小时，只能重开 05-27。
- confirmed raw 算术 `0 = 0 retained + 0 closure + 0 withdrawn` 与 surfaced conservation `838 = 835 arXiv ambiguous + 2 Google ambiguous + 1 MiniMax previous-Daily clue` 均成立。
- 835 条 owner-ambiguous inventory 的 arXiv ID 与 Source Family ID 各自唯一；每项都有非空 terminal reason 与精确 reopen condition。Evidence、Books V3 comparison 与 V3 root queue 都是空集合。

## 2. 实质缺陷：Books 隔离没有真实成立

Report 合同允许外部材料作为本窗终态保留项，前提是它们不用于正面证据、不进入 Books，也不支撑无遗漏断言。V3 文件虽然把 835 项移出分母并清空 queue，但当前共享 Books 仍命中其中 17 个明确 `source-family` marker：

### 来自 05-27 旧 writeback queue 的 8 项

| Source Family | 当前 Books 文件 |
| --- | --- |
| `SF-2026-ARXIV-2605-27480` | `books/part-06-ai-infrastructure/70-cost.md` |
| `SF-2026-ARXIV-2605-27494` | `books/part-07-agent/76-rag.md` |
| `SF-2026-ARXIV-2605-27599` | `books/part-06-ai-infrastructure/67-monitoring.md` |
| `SF-2026-ARXIV-2605-27678` | `books/part-04-training-system/36-distributed-training.md` |
| `SF-2026-ARXIV-2605-27712` | `books/part-06-ai-infrastructure/66-evaluation-system.md` |
| `SF-2026-ARXIV-2605-27784` | `books/part-07-agent/74-prompt.md` |
| `SF-2026-ARXIV-2605-27785` | `books/part-06-ai-infrastructure/68-logging.md` |
| `SF-2026-ARXIV-2605-27789` | `books/part-06-ai-infrastructure/66-evaluation-system.md` |

05-27 当前 V3 owner evidence 把其 official batch 限定为 `2605.24798..2605.26116`；以上 8 项均在该区间之外，却仍由 `daily-20260527/books-writeback-queue-independent-final.json` 声称已写入。该 queue 和其旧 post-write audit 不能继续作为有效 owner 证明。

### 来自 05-28 旧 V2.1 writeback queue 的 9 项

| Source Family | 当前 Books 文件 |
| --- | --- |
| `SF-2026-ARXIV-2605-27825` | `books/part-06-ai-infrastructure/72-security.md` |
| `SF-2026-ARXIV-2605-28053` | `books/part-05-inference-system/46-continuous-batching.md` |
| `SF-2026-ARXIV-2605-28095` | `books/part-05-inference-system/54-gpu-memory.md` |
| `SF-2026-ARXIV-2605-28201` | `books/part-06-ai-infrastructure/72-security.md` |
| `SF-2026-ARXIV-2605-28433` | `books/part-07-agent/82-multi-agent.md` |
| `SF-2026-ARXIV-2605-28617` | `books/part-07-agent/78-tool-calling.md` |
| `SF-2026-ARXIV-2605-28632` | `books/part-06-ai-infrastructure/72-security.md` |
| `SF-2026-ARXIV-2605-28704` | `books/part-05-inference-system/49-tensorrt-llm.md` |
| `SF-2026-ARXIV-2605-28760` | `books/part-04-training-system/28-pretraining.md` |

这些 family 同时存在于当前 835 owner-ambiguous inventory 与旧 `daily-20260528/books-writeback-queue-final.json`。V3 已明确旧 Books disposition 不继承，因此这些 marker 是未被 V3 queue 清零动作撤销的正向采用痕迹。

### 同集合的 3 个裸 arXiv Review-notes 引用

| arXiv ID | 当前 Books 文件 |
| --- | --- |
| `2605.27760` | `books/part-07-agent/84-agent-platform.md` |
| `2605.28732` | `books/part-07-agent/77-memory.md` |
| `2605.28816` | `books/part-03-multimodal-world-models/25-multimodal-world-models.md` |

它们没有当前 V3 正向 owner 证明，不能继续被当作 05-28 已闭环 evidence。裸引用不一定要求删除相邻的独立论证，但必须移除、隔离或由合法 owner report 重新建立证据链。

## 3. 有界修复条件

1. 对上列 17 个 source-family 段逐项处理：若没有另一份具备有效 official owner、exact-version review 与 Books Decision 的报告，则从 Books 正向证据链中隔离；若存在，则明确改由该报告承担 provenance，并重新做相邻章节语义复核。
2. 对 3 个裸 arXiv 引用执行同样的 owner/provenance 检查；不能仅因链接可访问就保留为长期证据。
3. 纠正 05-27 的旧 queue/post-write audit 对 8 个区间外 family 的采用记录；只修受影响项，不推倒 05-27 其余有效 batch。
4. 重新扫描当前 835 inventory 与 `books/**/*.md` 的交集。未取得 owner 证明的 family 必须为 0 个正向 marker/引用；若由其他有效 owner 接管，保存可追溯的 owner report 和 Books Decision。
5. root 完成共享 Books 修复后，由未参与修复的新 fresh reviewer 顺读受影响段落及相邻交接，再决定 05-28 是否可标 `Complete`。

## 4. 机器与范围检查

- V3 JSON parse：通过。
- 835 arXiv ID / Source Family uniqueness：通过。
- terminal reason / reopen condition 非空：`835/835`。
- Google ambiguous：`2`；MiniMax previous-Daily clue：`1`。
- Evidence / Books V3 comparison / V3 queue：`0 / 0 / 0`。
- 共享 Books：本 reviewer 未修改。

机器结果不覆盖“隔离项仍在 Books 中被正向采用”的语义冲突，因此本轮不能签署 Complete。
