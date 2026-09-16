# 2026-05-05 V3 Fresh Non-author 最小范围最终复核 — 2026-09-15

**复核者：** `fresh-context:may07_final_independent`

**角色隔离：** 本复核者未参与 2026-05-05 bounded repair，也未参与 Ch31 `SF-2026-ARXIV-2605-02375` 写回。本轮只复核上一轮 FAIL 指定的最小范围；既有 52 项 Applied 不做无差别重审，且未编辑任何 Books 正文。

**结论：** **PASS**。Daily、Candidate Denominator、Evidence 与 Books Gate 可以闭合。

## 1. 定点 Evidence 与 owner

- `2605.01710v1`：exact-v1 HTML 的 §5、§6、§8 与 Appendix A 确实承载 route-receipt 的 provenance、schema 与字段设计；§7 是 fictional case，§10、§11、§14 承载 usability、redaction/threat model 与限制。当前 Evidence locator 和“position/schema proposal、非生产效果实验”的 claim boundary 成立。
- `2605.01771v1`：active ledger、Evidence 与 root queue 的 current owner 均为 `PLATFORM-EVALUATION-SYSTEM` / Ch66。Ch66 拥有 process-compliance evaluation contract；Ch69 只作为 trace 输入 owner，Books 中不存在第二份 `SF-2026-ARXIV-2605-01771` 正文。
- `2605.02196v1`：17 页 exact-v1 PDF 的 §3–§9 与 Appendix C/D 支持 NF4+LoRA 下的 INT4 recovery、FA–RA–Q-INT4 trade-off、STE mitigation 与低 retain accuracy 等限制。8/9 deep、`PLATFORM-SECURITY` / Ch72、`No Change` 成立；结论没有外推到未知 quantizer、生产合规或通用 unlearning failure。
- `2605.02206v1`：16 页 exact-v1 PDF 的 §3–§7 与 Appendix C 支持 metric disagreement、oracle-distance、KR blind spot 和 data-dependent UQS。6/9 standard、`PLATFORM-EVALUATION-SYSTEM` / Ch66、`No Change` 成立；UQS 没有被提升为通用 deletion certificate。
- `2605.02375v1`：25 页 exact-v1 HTML/PDF 的 §2.3–§5.1 与 Appendix A/B 支持 binary-reward degeneracy、filtered target、forward/reverse KL support asymmetry、misspecification 与 toy autoregressive illustration。6/9 且因写入 Books 强制 deep、`TRAIN-RLHF` / Ch31、`Integrate Applied` 成立。

五个 arXiv abstract/version 页面均未显示 withdrawal notice；本结论只针对 exact-v1 与本次检查时可见状态。

## 2. Ch31 写回

`SF-2026-ARXIV-2605-02375` 在 Ch31 中只有一个 semantic-body binding，位于 `## Review notes` 之前。正文按既有 reverse-KL 演进链补入：

```text
binary verifier 的 fully-valid optimum degeneracy
→ base/reference 决定 filtered target 内部质量
→ forward/reverse KL 的 support asymmetry
→ misspecified policy family 下的 near-Dirac pressure
→ validity 与 coverage 分轴评价
→ forward/alpha 分支的额外成本与 reverse-KL fallback
```

正文明确把 mode-collapse 证据收窄为 toy autoregressive experiment，没有声称规模化 LLM RLVR 必然坍缩，也没有声称 forward/alpha divergence 普遍优于 reverse KL；机制 owner、trade-off、fallback 与 evidence boundary 完整。

## 3. 守恒与终态

- `1058 = 181 retained + 877 pre-denominator closure`。
- `181 = 96 deep + 85 standard`。
- `181 = 53 Integrate Applied + 128 No Change`。
- `Blocked / Unverified = 0`；Materials Request 为空。
- Source Family 与 arXiv identity 无重复；三维评分均在 0–3，Total 均等于三项之和。

## 4. 校验

- `scripts/validate_research.py --report papers/2026/05/05/README.md`：通过。该结果只证明可判定结构，不替代以上语义复核。
- JSON 解析、Score V2 算术、Stable Node 存在性、README 相对链接、Ch31 marker 唯一性/位置、Ch66/Ch69 owner 唯一性：通过。
- `git diff --check`（本日 Daily、source artifact 与相关 Books 范围）：通过。
- 未 stage、commit、push；未修改 Books 正文。

## 5. Gate

- Window / identity conservation：**PASS**。
- Candidate Denominator：**PASS**。
- Evidence / score / owner / Books disposition：**PASS**。
- Books semantic writeback：**PASS**。
- Materials / blocked closure：**PASS**。
- Daily：**Complete**。
