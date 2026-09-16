# 2026 年 6 月 Daily 月级闭环复核

**复核日期：** 2026-09-14
**结论：** 06-01～06-30 共 30 份 Daily 已按当前合同重新认证并闭环。本文件取代
`LATEST_CONTRACT_CHECKPOINT_20260903.json` 对当前状态的解释；后者只保留为当时的过程快照。

## 1. 月级账目

- 30/30 份报告状态为“完成”。
- 每日均实际处理 13 个机构来源与 `SRC-ARXIV`，共 420/420 个来源槽位；没有按“来源后来才注册”豁免历史回放。
- 候选总数为 1,192：06-01～10 为 551，06-11～20 为 419，06-21～30 为 222。
- 既有 arXiv identity、版本、全文审阅与 Books 证据仅在身份和 claim 未变化时复用，没有为改写报告机械重读同一正文。
- 跨日 arXiv/primary identity 重复为 0；Kimi Code 各版本家族已改用对应 release tag 作为 primary identifier，不再共享模糊的 releases 列表地址。

## 2. 当前来源再认证恢复的候选

| 日期 | Source Family | 评分 | Books Decision |
| --- | --- | ---: | --- |
| 06-01 | MiniMax M3 | 8 | `MODEL-LONG-CONTEXT` 已有覆盖 |
| 06-03 | Kimi Code 0.7/0.8 | 6 | `AGENT-WORKFLOW` 已有覆盖 |
| 06-04 | Kimi Code 0.9 | 6 | `AGENT-MCP` 已有覆盖 |
| 06-05 | Kimi Code 0.10 | 5 | `AGENT-WORKFLOW` 已有覆盖 |
| 06-06 | Kimi Code 0.11 | 5 | `AGENT-PLATFORM` 已有覆盖 |
| 06-10 | Kimi Code 0.12 | 7 | `AGENT-MULTI-AGENT` 已有覆盖 |
| 06-10 | MaxProof | 8 | `TRAIN-GRPO` 已有覆盖 |
| 06-17 | GLM-5.2 / IndexShare | 8 | `MODEL-LONG-CONTEXT` 已有覆盖 |
| 06-25 | Gemini 3.5 Flash computer use safeguards | 8 | `PLATFORM-SECURITY` 已有覆盖 |
| 06-30 | MOPD | 9 | `TRAIN-GRPO` 已有覆盖 |

以上十项均已完成来源日期、贡献准入、Evidence、评分、目标章节及相邻机制比较。本轮没有为了形成 diff 强行修改
Books；十项都由当前命题级正文完整承载。

独立复核还纠正了两类相反错误：DeepSeek V4 官方首次发布为 2026-04-24，不属于 06-25 窗口；Gemini
computer-use safeguards 与 MOPD 不能作为普通版本事实或局部方法在候选前关闭，已分别重开并完成深审。

## 3. Books Gate

- 原有 `Integrate` 项继续以唯一 Stable Knowledge Node 为 owner，并能从 Daily 链接到实际章节正文。
- 06-11～20 中十二条旧“待写”标签已对照现有正文锚点重新核验，确认写入早已存在后改为闭合状态；没有把 trace
  或 Review notes 标签冒充正文。
- 当前再认证新增十项全部为 `No Change — Existing Coverage`，新增 Books 写回队列为 0。
- 普通 Evidence pending、Books pending 与共享写入队列均为 0。

## 4. 终态来源限制

以下缺口已隔离，不参与评分，不支持正向技术结论、Books 或“来源无遗漏”断言；取得指定材料时只重开对应
Source Family，不重跑整月：

1. OpenAI `Dreaming` 只有 `2026-06-04` 日级日期，缺带时区的原始发布时间，暂不能唯一归入 06-04 或 06-05。
2. 06-11/06-12 缺能改变 first-public owner 判断的 official historical arXiv listing/announcement receipt。
3. Anthropic `Project Fetch: Phase two` 只有 `2026-06-18` 日级日期，缺带时区的官方发布时间，暂不能唯一归入
   06-18 或 06-19。

这些是外部材料边界，不是仍可由当前执行者继续完成的普通待办，因此不妨碍其余确定性链路闭合。

## 5. 最终验收

- 30/30 `scripts/validate_research.py`：通过。
- 每份来源行：14/14；候选总数：1,192；跨日 primary identity 重复：0。
- Daily 内部本地链接缺失：0；候选 primary URL 已按 family/version 区分。
- 失效的“来源注册较晚所以不追溯”口径：0。
- 可执行的 Evidence/Books/独立复核 pending：0。
- Markdown 与当前工作树 `git diff --check`：通过。`git diff --cached --check` 仍能看到运行前 index 快照中的
  行尾空格（06-11/06-12 及不属于本任务的 09 月文件）；本轮没有通过重新 stage 改写用户的暂存边界。
- 未 stage、commit 或 push；工作树中本轮以前的 Books、Daily 与其他日期修改均保留。

机器校验只证明结构和可判定一致性。月级结论还经过分组之外的独立语义复核；该复核实际发现并纠正了
DeepSeek 日期、Gemini/MOPD false negative 与 Kimi primary identifier 冲突，因而不是把子任务自检直接当作完成证明。
