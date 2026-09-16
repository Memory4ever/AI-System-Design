# 2026-06-09 exact-v1 独立恢复审计

## 范围

本次只复核先前被写成“official abstract 可读、正文不可得”的四个 Candidate，不替代 1,235 项分母审计。四个 exact-v1 HTML 均已恢复并核对 Method、Evaluation 与 Limitations；因此外部材料 blocker 从 4 降为 0。

## 逐项结果

| Source Family | exact-v1 证据 | Books 判断 |
| --- | --- | --- |
| `SF-2026-ARXIV-2606-07571` | §4–§6、§9；浅层 prefix KV 复用、深层周期刷新及 LLaDA/B200 受限实验 | `No Change — Existing Coverage`；Ch45 已有 bidirectional dependency、refresh frontier 与共存边界 |
| `SF-2026-ARXIV-2606-07665` | §2–§4、§7；LLM advisory proposal 与 compiler admission/fallback 分离 | `No Change — Existing Coverage`；Ch49 已有 proposal/validation/admission 责任边界 |
| `SF-2026-ARXIV-2606-09421` | §3–§4、Limitations；preservation anchor 与 quality–cost constrained selection | `No Change — Existing Coverage`；Ch84 已有 paired evaluation、correctness/trajectory/cost 分账和 lifecycle compaction |
| `SF-2026-ARXIV-2606-09071` | §3–§4、Appendix R；prefix-preserving replay、faithfulness gate、verified rollback | `Integrate`；现有 Ch69/Ch80 尚缺 diagnosis-specific faithfulness gate 以及 outcome flip 只证明充分性、不证明唯一性的明确边界 |

## 精确 Books 写回队列

- Canonical owner：`PLATFORM-TRACE`，`books/part-06-ai-infrastructure/69-trace.md`。
- 写入位置：现有 replay / attribution recovery 段落内，不能追加为论文清单。
- 必须补充：replay 保留候选错误点之前的 prefix；diagnosis-specific faithfulness gate 排除“靠无关改动恢复”；outcome flip 只支持该 intervention 的充分性，不支持唯一性或最小性。
- 证据边界：主实验依赖 oracle expected answer；不可逆副作用、缺失环境和多处共同错误不在保证范围。
- Handoff：`AGENT-REFLECTION` 只引用 Trace owner，不复制机制。
- 完成条件：正文写入后由非作者核对命题、证据边界、owner 与相邻交接；在此之前 2026-06-09 不得标记 Complete。

## 结论

Evidence Gate 对四项恢复通过；Books Gate 因 REFLECT 的一项真实语义缺口保持未通过。该缺口不需要用户补材料，只需要共享 Books 按日期顺序写回并复核。
