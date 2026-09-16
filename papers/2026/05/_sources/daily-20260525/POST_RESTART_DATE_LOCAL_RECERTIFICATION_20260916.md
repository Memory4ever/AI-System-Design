# 2026-05-25 post-restart date-local recertification

- 检查日期：`2026-09-16`
- 角色：日期本地修复作者；不具备 fresh non-author 最终签署资格。
- 范围：仅复核现有冻结 corpus、Evidence / Books 投影、root 写回队列和当前 Books binding；没有扩窗、扩源、增删候选或修改共享 Books。
- 状态：`Ongoing`。

## 冻结投影

- 身份守恒：`499 = 280 retained + 219 pre-denominator closure + 0 withdrawn`。
- retained、Evidence 与 Books comparison 的 Source Family 集合逐项相等，均为 `280` 项。
- Evidence：`280 = 132 deep complete + 145 standard complete + 3 deep blocked`；结构化状态实际为 `221 complete + 56 complete_revalidated + 3 blocked_exact_v1_body`。
- Books：`280 = 47 Applied + 3 Deferred + 5 Integrate + 209 No Change — Existing Coverage + 9 Report Only + 7 Structural Candidate`。
- README 中 `review` 与 `claim` 各有 `280` 组唯一成对 marker，集合与 retained candidates 一致。

## 现有 Books binding

- `27` 个新增正文 binding 与 `2` 个 binding-only repair 当前均为全局唯一的成对 `semantic-body-binding` marker，并位于各目标章节的 `Review notes` 之前。
- `2605.22834` 与 `2605.23857` 两个 evidence quarantine 在稳定正文中仍无正向 marker；本轮没有将它们恢复为 Books 证据。
- 以上只证明结构与位置仍然一致，不替代 post-write 语义复核。

## 待 root 串行写入的 5 项

| arXiv | Owner / Target | 当前检查结果 |
| --- | --- | --- |
| `2605.23128` | `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` | score 7、exact-v1 deep complete；前后锚点存在；拟写 proposition、证据边界、trade-off/failure/fallback 与 3 个 locator 齐全；当前无提前 marker。 |
| `2605.23482` | `TRAIN-DATA` / `books/part-04-training-system/27-data.md` | score 7、exact-v1 deep complete；前后锚点存在；拟写 proposition、证据边界、trade-off/failure/fallback 与 3 个 locator 齐全；当前无提前 marker。 |
| `2605.23562` | `AGENT-MULTI-AGENT` / `books/part-07-agent/82-multi-agent.md` | score 7、exact-v1 deep complete；前后锚点存在；拟写 proposition、证据边界、trade-off/failure/fallback 与 3 个 locator 齐全；当前无提前 marker。 |
| `2605.23565` | `TRAIN-PPO` / `books/part-04-training-system/32-ppo.md` | score 7、exact-v1 deep complete；前后锚点存在；拟写 proposition、证据边界、trade-off/failure/fallback 与 3 个 locator 齐全；当前无提前 marker。 |
| `2605.23883` | `TRAIN-DATA` / `books/part-04-training-system/27-data.md` | score 7、exact-v1 deep complete；前后锚点存在；拟写 proposition、证据边界、trade-off/failure/fallback 与 3 个 locator 齐全；当前无提前 marker。 |

这 5 项与 `books-comparison-v3.json` 的全部 `Integrate` 项完全相等，没有遗漏或额外写回项。完整可执行内容继续以 `root-books-writeback-queue-v3.json` 为唯一队列，不在本 checkpoint 复制正文。

## 机器检查

- `python3 scripts/validate_research.py --report papers/2026/05/25/README.md`：通过。
- date-local JSON 解析、身份集合、算术、Evidence 深度、Books disposition、5 项队列字段和目标锚点：通过。
- 29 个正向 binding 的 marker 唯一性/成对性/位置，以及 2 个 quarantine 的 marker 缺失：通过。
- `git diff --check -- papers/2026/05/25/README.md papers/2026/05/_sources/daily-20260525`：通过。

机器检查不能证明语义正确。本轮是 delegated author-side 检查，未调用外部 cross-model reviewer；最终 Gate 仍必须由未参与修复和写回的 fresh reviewer 完成。

## 剩余 Gate

1. root 只按 `root-books-writeback-queue-v3.json` 串行写入上述 5 项，不重新生成或扩大 corpus。
2. 未参与写回的 reviewer 逐项检查正文位置、相邻语义、证据边界、trade-off、failure/fallback 与唯一 marker，并同步 date-local 投影。
3. 另一位 fresh non-author reviewer 对冻结 `499/280/219` corpus、Evidence、Books 和 README 执行最终 Gate。
4. 上述 Gate 通过前，`papers/2026/05/25/README.md` 保持 `Ongoing`，不得标记 `Complete`。
