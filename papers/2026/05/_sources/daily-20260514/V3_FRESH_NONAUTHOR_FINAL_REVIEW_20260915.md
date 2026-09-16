# 2026-05-14 V3 独立最终语义复核

- **复核者：** fresh nonauthor reviewer（非作者上下文）
- **复核日期：** 2026-09-15
- **结论：** `FAIL — 保持 Ongoing`
- **审查对象：** `papers/2026/05/14/README.md` 及其 V3 作者证据包

## 已通过的边界

1. Daily 窗口为 `[2026-05-13T09:00:00+08:00, 2026-05-14T09:00:00+08:00)`，没有把次日截止点后的 Seed 条目回拨进本日。
2. active arXiv inventory 守恒：`714 = 77 retained + 637 pre-denominator closure + 0 withdrawn`；旧 745 账本因按 submission timestamp 组窗而失效，没有与 active denominator 混算。
3. 13 个非 arXiv Daily 来源均有终态；OpenAI 命中 2 项，其余为有入口和相邻记录边界的 no-hit，未把 Weekly-only 来源扩入 Daily。
4. 77 个 arXiv retained family 的 exact-v1 HTML 均可访问；当前没有 exact-version material blocker，也没有发现 withdrawn 候选。
5. `SF-2026-OPENAI-WINDOWS-SANDBOX` 已真实写入 `PLATFORM-SECURITY` 正文：机制段落位于最终 `Review notes` 之前，marker 唯一，正文说明了 OS principal、setup/runtime 权限分离、enforcement boundary、trade-off、fallback 与证据边界。该写入本轮接受，不需回滚。

## 未通过 Gate 1：Candidate Denominator

对 637 个关闭项进行了风险分层的有界 false-negative challenge：先按 training/inference/platform/agent/multimodal/security/evaluation 等高风险主题抽取近边界项，同时复核一组明显低贡献对照项。12 个低风险对照保持关闭；以下 41 个 family 的题名与完整摘要已经给出可能改变长期机制、状态/控制权或评价合同的具体信号，不能继续使用当前泛化的 `local_method_or_empirical_result...` 理由关闭，必须重新进入 contribution screening：

```text
2605.12517  2605.12529  2605.12565  2605.12574  2605.12694
2605.12765  2605.12813  2605.12869  2605.12975  2605.13043
2605.13050  2605.13105  2605.13115  2605.13130  2605.13155
2605.13162  2605.13179  2605.13213  2605.13255  2605.13277
2605.13290  2605.13329  2605.13334  2605.13352  2605.13369
2605.13429  2605.13438  2605.13448  2605.13467  2605.13486
2605.13511  2605.13534  2605.13537  2605.13625  2605.13632
2605.13652  2605.13687  2605.13695  2605.13724  2605.13757
2605.13829
```

其中的高置信代表包括：missing-modality calibration（2605.12517）、模型后门移除与 watermark 保留的安全边界（2605.12529）、policy/worklist 状态化 agent program analysis（2605.12694）、runtime activation rotation unlearning（2605.12765）、time-to-jailbreak survival evaluation（2605.12869）、可执行 multi-hop RAG 及 repair trace（2605.12975）、DLM step-wise safe remasking（2605.13043）、主动 context search/pruning（2605.13050）、长期 agent runtime trace taxonomy（2605.13625）。这不是判定它们最终必须进入 Books，而是判定现有 closure 证据不足。

由于高风险分层已经出现系统性 false negative，Candidate Denominator 尚未冻结。返修时只扩展这些受影响的主题类和相邻同类，不要求推倒 714 条重新全量枚举。

## 未通过 Gate 2：Evidence Review

77 个 arXiv retained family 虽然都有可访问 HTML 和三个 locator 字段，但 README 的“最小命题”大多直接复制摘要句，“证据边界”则重复同一句通用模板，没有实际写出机制、evaluation contract、结果边界、未证明项、trade-off 或 failure mode。这只能证明页面可访问，不能证明完成了合同要求的 Source Review。

locator artifact 还包含明确无效或不充分的定位，例如：

- `2605.12673` 的机制定位为 `Appendix A Disclosure of Language Model Usage`；
- `2605.12874` 的评价定位为 `2 Related Work`；
- `2605.13076` 的机制定位为 `Instructions for reporting errors`；
- `2605.13768` 的评价与限制定位为 `Instructions for reporting errors`；
- `2605.13825` 的机制/评价只写成 `Alignment of language models.` / `Single-turn evaluation.`。

因此 77/77 arXiv retained family 都必须重新形成非模板化证据审阅。返修可以优先使用 HTML，并围绕候选的最小贡献命题定点阅读，不要求无差别逐页 PDF 对比，也不要求比较 revision 前后。

两个 OpenAI 官方来源的审阅不属于这一系统性失败；Windows sandbox 已通过，safety summaries 只需在 Books Gate 中复核 `No Change`。

## 未通过 Gate 3：Books Decision

78 个 `No Change — Existing Coverage` 中，多项只是“主题相近”，并非 Books 现有具体命题完整承载候选 delta。已确认的高置信错配包括：

- `2605.12519` 的 verifiable process supervision 不能由 Ch33 的纯 RL/GRPO 概览直接关闭；
- `2605.12549` 的 VLM GUI grounding prefill bottleneck 不能由 Ch43 的基础 Prefill 并行计算直接关闭；
- `2605.12571` 的 evidence misalignment 与 answer authority 解耦不能由 Ch81 的一般 failure attribution 直接关闭；
- `2605.12673` 的 benchmark exploit audit 不能由 Ch66 的 hidden-shape kernel evaluation 直接关闭；
- `2605.12705` 的 early data exposure 对后续 fine-tuning retention 的影响不能由 Ch29 的 hard-tail weighting 直接关闭；
- `2605.12825` 的 dual-view diffusion/AR generation 不能由 Ch48 的通用 speculative speedup 关系直接关闭；
- `2605.13768` 的 waterfilling bit allocation 不能由 Ch49 的 reasoning quantization commitment 直接关闭；
- `2605.13772` 的 step-level hallucination localization 不能由 Ch67 的 session search trajectory 直接关闭；
- `2605.13825` 的 unsafe history anchoring 不能由 Ch72 的 safe-commit certificate 直接关闭；
- `2605.13839` 的 receiver-specific transient weight perturbation 不能由 Ch82 的 single-agent baseline 直接关闭。

这说明比较方法存在共享缺陷。77 个 arXiv family 完成真实证据审阅后，必须重做全部 78 个 `No Change` 对读：引用 Books 的真实命题，说明它为何完整覆盖候选 delta；否则改为 `Integrate`、`Structural Candidate` 或其他准确 disposition。已经通过的 Windows sandbox integrate 不在返修范围内。

## 有限返修清单

1. 重开上述 41 个 closure family，并对同一高风险主题的相邻关闭项做一次有界扩展；给出逐项 retain/closure 理由与更新后的守恒式。
2. 对最终 retained 的每个 arXiv family 写真实 Source Review：最小机制命题、状态/数据/控制变化、evaluation contract 与结果边界、未证明项、trade-off/failure mode；替换无效 locator。
3. 基于重写后的证据，对全部 78 个作者 `No Change` 重新对读真实 Books 命题；只保留能够完整承载 delta 的 `No Change`。
4. 需要新增 Books 语义时交由 root 按 owner 串行写入；本 reviewer 不编辑 Books。
5. 更新候选表、Source Review、Books Decision 与 Gate 状态，再由新的非作者上下文执行最终语义复核。

当前没有需要用户补交的材料；问题是仓库内已有 primary material 尚未被正确筛选与审阅。

## Gate 结论

| Gate | 结论 | 原因 |
| --- | --- | --- |
| Window / inventory conservation | Pass | 窗口和 714 条 active inventory 守恒成立 |
| Daily source coverage | Pass | 13/13 非 arXiv 来源终态成立 |
| Withdrawal / material access | Pass | 0 withdrawn；77/77 exact-v1 HTML 可访问 |
| Candidate Denominator | Fail | 风险分层抽样发现 41 个需重开的 false-negative family |
| Evidence Review | Fail | 77 个 arXiv 审阅为摘要/模板化边界，且存在无效 locator |
| Books Decision | Fail | 78 个 No Change 存在系统性主题近似替代命题承载的问题 |
| Independent semantic final | Fail | 上述三个语义 Gate 未闭合 |

因此 `2026-05-14` 必须保持 `Ongoing`；不能标记 V3 Complete。
