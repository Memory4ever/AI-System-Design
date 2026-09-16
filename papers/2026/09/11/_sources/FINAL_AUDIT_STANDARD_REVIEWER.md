# 2026-09-11 Final Semantic Audit — Independent Standard Reviewer

**审阅者：** 非日报作者的独立语义复核者（standard-review / Ch24 作者仅排除其本人写入的 Ch24 段，不以该段作为本审计的独立证明）  
**审阅快照：** 2026-09-11 17:24+08:00  
**结论：** **未通过**。Deep Batch A/B 的证据记录和绝大多数 Books 写回可以通过，但日报仍有一个可执行的 primary-source 审阅未完成，以及三类报告一致性错误；修复并由另一复核者定点复验前，不能把 Daily 状态改为 `完成`。

## 1. 必须修复的发现

### F1 — NCP 的 exact-v1 PDF 可访问，不能作为终态受阻项

- **日报锚点：** `## 3. 候选与判断` 的 `NCP-ArchPreview` 行；`### NCP-ArchPreview`；`## 5. 缺口与下一步` 中“当前可访问的官方入口和替代 artifact 已穷尽”的断言。
- **当前记录：** score `3 + 3 + 3 = 9`，但因 exact-v1 HTML 返回错误而标记 `受阻 / 暂缓`，并将 HTML/PDF 恢复列为未来重开条件。
- **反证：** 本审计定点请求 `https://arxiv.org/pdf/2609.10715v1` 得到 HTTP `200`、`Content-Type: application/pdf`、`Content-Length: 2370690`、文件名 `2609.10715v1.pdf`；`https://arxiv.org/html/2609.10715v1` 同时返回 HTTP `404`。因此只有 HTML 转换失败，exact-v1 primary PDF 并未受阻。
- **影响：** 该项不是安全终态，而是仍可执行的 9 分候选。按 `RESEARCH_CONTRACT.md`，需要从 exact-v1 PDF 完成深入 Evidence Review、Books 对读与最终处置；若触发写回，还要完成 post-write audit。完成前 Coverage/Evidence/Books 链不能宣称闭合。
- **定点修复：** 只重开 `2609.10715v1`，不重扫本窗或其他 39 项；完成后同步候选行、证据段、缺口、Repository Changes、Open Questions 与最终复核结论。

### F2 — `WORLDVIEW-REPRESENTATION` 的章节号和正文链接错误

- **日报锚点：** `Quantifying the Memorization-to-Generalization Transition` 与 `Distribution-aware Language Neuron Identification` 两个候选行，以及后者的 `### Distribution-aware Language Neuron Identification` 证据段。
- **当前记录：** 两个候选均写 `WORLDVIEW-REPRESENTATION [Ch4](.../04-why-models-learn.md)`；证据段另写“Ch4/66 已有覆盖”。
- **权威映射：** `ROADMAP.md` 将 `WORLDVIEW-REPRESENTATION` 唯一映射到 Ch5、`books/part-01-worldview/05-what-neural-networks-learn.md`。`STANDARD_BOOKS_DECISIONS.md` 的精确锚点也是 Ch5 的 `## 记忆与泛化不是简单对立`、`## 分布式表示与 Superposition` 和 `### 从可读出到机制：证据应逐级变强`。
- **影响：** 当前链接虽然指向一个存在的文件，却是错误 owner，比断链更难被机械校验发现；读者会被引到“模型为何学习”而不是“表示、记忆与泛化”的 canonical body。
- **定点修复：** 两行改为 Ch5 / `05-what-neural-networks-learn.md`，并把证据段的 Ch4 改为 Ch5；Stable Node ID 保持不变。

### F3 — `2609.10863v1` 的审阅强度与证据记录冲突

- **日报锚点：** 候选表的 `Flow Duality and Source Geometry` 行与同名 `###` 证据段。
- **当前记录：** 写作“深入完成”“深入审阅”。
- **原始审阅状态：** `STANDARD_REVIEW_BATCH.md` 明确记录 score `2 + 1 + 3 = 6`、`标准审阅完成`；`STANDARD_BOOKS_DECISIONS.md` 也将其放在 Standard Review Books Decisions 中。Books Integration 是额外的长期知识判断，不会把已完成的标准审阅自动改名为深入审阅。
- **影响：** Report 与 evidence artifact 对 Review Status 的陈述不一致，容易让读者误认为已执行 7～9 分的默认深审投入。
- **定点修复：** 候选表改为 `标准完成`，证据段改为 `标准审阅`；保留已完成的 Ch24 Integration，不改评分。

### F4 — `2609.11146v1` 的候选摘要把 head identity 与 susceptibility 混为一个正面解释变量

- **日报锚点：** 候选表 `The Oligarch Barely Steers Model Collapse` 的贡献摘要。
- **当前记录：** “supplier identity/susceptibility 比集中度更能解释 collapse”。
- **exact-v1 证据边界：** `DEEP_REVIEW_BATCH_B.md` 记录：share 与 head-identity arms 的 endpoint separation 均只占自身五代漂移的 2.6–3.2%，且低于 cross-seed noise；较强信号来自 human-text fraction，以及由各模型 propensity 组成的 post-hoc travel-propensity fit。Head identity 本身并未被证明是比集中度更强的解释变量。
- **Books 正文：** Ch27 正确地把 supplier share、susceptibility、pool composition 与 human anchor 分成四个控制轴，并明确不能用任一轴解释全部机制。
- **影响：** 表格摘要可能把论文的负结果倒写成“supplier identity 更能解释 collapse”，与深审和 Books 的谨慎结论冲突。
- **定点修复：** 改成类似“clean-base reset 下，有限的 concentration/head-identity 变化均弱于共同递归漂移；human-text fraction 与 susceptibility-derived pool composition 更能解释所测速度，但仍是小模型、五代与 post-hoc 条件结论”。

### F5 — 复核段缺少合同要求的明确身份与结论

- **日报锚点：** `## 6. 复核`。
- **当前记录：** 只叙述“第一次非作者复核”和后续不同审阅者，没有 `复核者：...` 与 `结论：通过/未通过`。
- **合同要求：** `REPORT_CONTRACTS.md` §3.6 要求记录复核者身份、明确结论和实际检查范围。
- **影响：** 当前段落无法判断哪位复核者对最终版本负责，也无法区分历史中间复核与当前 Gate 结论。
- **定点修复：** 在 F1～F4 完成后，由未编写相应修复内容的复核者写明身份、`结论：通过` 及定点复验范围；本审计当前结论必须保持 `未通过`。

## 2. 已通过的独立检查

### Identity、日期与评分

- 候选表共有 40 个唯一材料家族；Disposition 算术为 `22 整合 + 16 已有覆盖 + 1 仅报告 + 1 当前受阻 = 40`，与日报结论一致。F1 修复后最后一项须重新归类。
- 40 个 arXiv 候选均记录为 Friday batch `2026-09-11T08:00:00+08:00`，位于 Daily 窗口 `2026-09-10 09:00 ～ 2026-09-11 09:00` 内；三维评分逐行求和均正确。
- Deep Batch B 的九项 identity、日期和评分与日报一致；Batch A 的九项 exact-v1 identity 与 Friday batch 归属一致。审阅文件没有把 Atom submitted time 冒充公开时刻。
- Deep Batch A/B 均限定了 withdrawal 检查是审阅时状态，没有把“未见撤回标记”写成永久保证。

### Evidence 事实边界

- Deep Batch A 的九项均写明问题、机制与 owner、实现/评价合同、直接证据、未证明事项、trade-off、failure 与 fallback；没有把 ExaServe non-streaming、Fengshui simulation、ReactHuman simulator 或 world-model update fork 外推为普遍生产结论。
- Deep Batch B 对 KV intervention、edge fused latent、belief-shift fork、output geometry、GraphRAG policy/evidence、judge noise、solver verdict 与 recursive synthetic data 的主张均限定到 exact-v1 实验合同；未公开 artifact 没有被写成已复现。
- `2609.11146v1` 的 Ch27 正文通过 clean-base reset 分开 corpus recursion 与 parameter recursion，保留了小模型、五代、28% natural concentration、90% injected probe、under-converged 7–8B probe、post-hoc fit 和未公开代码边界；正文没有声称集中度无害。

### Books owner、marker 与正文质量

- Batch A 的八个 Books writeback marker 均位于目标章节首个 `## Review notes` 前，且 source family 在 canonical body 中唯一。
- Batch B 的九个写回均以一对 start/end marker 唯一界定正文，且全部位于首个 `## Review notes` 前；`2609.10992` 的 Existing Coverage 可在 Ch72 `## 隐私检测是 Policy-bound Sensor，不是安全判决` 与 `### 从独立 Span 到关系感知的本地 Sanitization` 精确定位。
- 抽取并顺读所有 Batch A/B body block 后，均可定位旧方案为何合理、约束变化、状态/数据/控制 owner、收益、trade-off/failure、fallback 和证据边界。Ch56 的 control-plane capacity → workflow readiness/release，Ch26 的可执行评测 → 低延迟 action head，Ch76 的 pre-run query policy → post-run evidence graph，均形成连续演进而不是论文列表。
- Ch13 对 `2609.11063` 只作 bounded handoff，没有把整个 information geometry 迁入 Position Encoding；Ch49 对 Fengshui 保留 simulation-only 边界；Ch45 对 KV intervention 保留 exact-prefix/dense-recompute fallback。

### 报告覆盖与结构

- `## 4. 证据与知识整合` 已为 40 个候选各提供一个可定位的小标题；长证据通过明确链接委托给 Standard/Deep Review artifacts，没有以“已读全文”替代判断。
- 所有相对 Markdown 链接在本审计快照中均能解析到现有文件；F2 是语义 owner 错误，不是文件不存在。
- Repository Changes 列出的 Ch13、Ch23～27、Ch33、Ch45、Ch49、Ch54～56、Ch66、Ch72、Ch76、Ch77 与当前可定位的本窗 writeback 相符。

## 3. Gate 判定

```text
Coverage：未通过 — NCP exact-v1 PDF 可访问，仍有可执行工作
Evidence：未通过 — NCP 9 分候选尚未完成深入审阅
Books：未通过 — NCP 尚未完成 Books Decision；其余已判定项通过
Independent Review：未通过 — F1～F5 尚待修复并定点复验
Daily Complete：否
```

本结论不要求重开已经通过的 39 项，也不否定 Batch A/B 已完成的正文写回。修复范围应严格限制为 NCP 单篇的 Evidence/Books 链，以及 F2～F5 的报告一致性字段；不要重扫本窗、重算候选分母或重写已通过 Books 段落。
