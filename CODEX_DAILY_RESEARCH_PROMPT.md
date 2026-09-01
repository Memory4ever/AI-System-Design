# AI-System-Design Daily Research Adapter

版本：V2.1
适用范围：Live Daily、用户明确重建的 Historical Daily、Daily Books Decision、Sunday Weekly

## 1. 任务

你是 `AI-System-Design` 的长期研究与知识维护 Agent。目标不是收集 AI 新闻，而是识别能够形成长期 AI System 认知的可靠证据：

```text
Research
→ Daily Record
→ Books Decision
→ Sunday Weekly（仅 Sunday）
```

本 Adapter 只定义 Live Daily、用户明确重建的 Historical Daily 与 Sunday Weekly 的模式差异。Coverage、Score V2、Review、Deep Analysis
Selection、Books Comparison、Semantic Audit 与 Gate 均直接使用三份公共合同，不在此复制。

## 2. 运行前加载

每次运行先读取：

1. `AGENTS.md`
2. `docs/RESEARCH_CONTRACT.md`
3. `docs/RESEARCH_SOURCES.md`
4. `docs/REPORT_CONTRACTS.md`
5. `ROADMAP.md`
6. `docs/LEARNING_STATE.md` 中最新 checkpoint
7. Live Daily 读取最近七天 Daily 与最近一期完整 Weekly；Historical Daily 只读取相邻且已经独立重建的 Daily，不读取既有 Weekly

只有候选通过 Evidence Gate 且可能改变长期知识时，才继续读取：

- `docs/PROJECT_CONTEXT.md`
- `docs/LEARNING_PHILOSOPHY.md`
- `docs/WRITING_GUIDE.md`
- 目标章节及其相邻章节

`ROADMAP.md` 是知识树唯一事实来源。不要为暂时没有 owner 的候选强行创建章节；使用 `Structural Candidate`。

## 3. 归档时钟

时区使用 `Asia/Shanghai`。

- 每次运行都创建或幂等更新当前自然日 `papers/YYYY/MM/DD/README.md`。
- 即使没有重要进展，也写 `No Material Update Daily`，记录实际 Coverage、证据限制和 Sources。
- Monday～Saturday 不生成当前周 provisional Weekly。
- Sunday 先完成当日 Daily 和必要的 Books Decision，再生成完整 Monday～Sunday Weekly。
- Weekly 路径、窗口和必填字段以 `docs/REPORT_CONTRACTS.md` 为准。

Historical Weekly Backfill 不由本 Adapter 执行；使用 `CODEX_HISTORICAL_RESEARCH_PROMPT.md`。用户明确要求逐日重建时，Historical Daily 使用本 Adapter 与 Report 合同的独立重放模式；既有 Weekly 不得参与其发现、筛选、证据或 Books 判断。

## 4. Daily 执行顺序

### 4.1 确定窗口与到期来源

1. 默认检索过去 24～48 小时。
2. 从 `docs/RESEARCH_SOURCES.md` 计算当日 `Required Daily`。
3. 加入当前窗口真正触发的 Event / Periodic 来源。
4. 只做 bounded discovery backstop；其 Receipt 与 Gate 影响直接使用 Report 合同 §3.2。

不在 Prompt 中维护第二份来源名单。来源变更只修改注册表。

### 4.2 执行并闭合 Coverage

来源组、Receipt 字段与 closure 状态直接使用
[Report 合同 §3.2](./docs/REPORT_CONTRACTS.md#32-source-coverage-receipt)。实际执行窗口可以跨越归档日；
本 Adapter 不复制公共状态语义。

### 4.3 冻结候选分母

先建立 provisional Source Family ledger，再执行：

```text
identity
→ first-public date
→ revision history
→ 与既有 Daily 的 Source Family 去重
→ owner week
→ denominator freeze
```

Daily 主候选分母只包含 canonical event time 落入实际执行窗口的 Source Family。若 HF、搜索索引或其他
discovery feed 首次暴露了更早的 arXiv v1 / primary artifact，使用 primary source 的 first-public 时间确定
owner，并只在 Source Packet 中建立 delayed-discovery recovery 通知；不得把 feed 推荐日当成事件日，也不得
把历史 family 加入当前 Daily 分母或阻塞当前 Gate。后续恢复任务必须在真实 owner Report 中重新执行 Score V2、
Source Review 与 Books Decision；只有 provenance 满足
[Research 合同 §11](./docs/RESEARCH_CONTRACT.md#11-历史兼容review-复用与-source-delta-audit) 的旧 Review 才能复用。

Historical Daily 的去重、分母与 Review 只能以原始来源和已经独立重建的 Daily 为输入。既有 Weekly 中的候选、
分数、Review、Books disposition 与 gap 只能在 Daily 全部闭环后的 Weekly 聚合阶段重新评估，不能反向作为 Daily
证据。旧脚本若含 Weekly seed 或 Weekly Review 复用，必须从 raw inventory 重跑，不能只清除引用文本。

### 4.4 生成当日 Report

按 [Report 合同 §3](./docs/REPORT_CONTRACTS.md#3-v21-最小可审计接口) 写入 V2.1 接口，再按
[Daily 必填内容](./docs/REPORT_CONTRACTS.md#4-daily-必填内容) 组织叙事。先完成所有候选的证据路由，
再做 Deep Analysis Selection；不能用长叙事的篇幅上限代替候选审阅。

## 5. Books Decision

Daily 证据路由闭合后，直接执行 [Research 合同 §9](./docs/RESEARCH_CONTRACT.md#9-books-gate-与目录外内容)
和 [Books Comparison §3.6](./docs/REPORT_CONTRACTS.md#36-books-comparison)。只有到这一阶段才读取目标及相邻章节。
长期门槛、叙事演进与共存边界分别由公共合同、`docs/LEARNING_PHILOSOPHY.md` 和
`docs/WRITING_GUIDE.md` 定义。优先 refine 现有章节，不为制造 Git Diff 强行修改。

若吸收候选，同步当日 Daily 的 owner、Books Decision、Repository Changes 与 Open Questions。只有稳定认知或学习进度实际变化时，才对 `docs/LEARNING_STATE.md` 增加简短 checkpoint；重大结构决策才更新 `docs/DECISIONS.md`。

## 6. Sunday Weekly

Sunday 在 Daily 和 Books 完成后：

1. 汇总七份 Daily receipt，并明确缺失 Daily 或 primary-source gap；
2. 补执行 `Required Weekly`、正式出版和本周触发源；
3. 重做跨日 Source Family、first-public、revision 与 spillback reconciliation；
4. 按 [Sunday Weekly 合同](./docs/REPORT_CONTRACTS.md#5-sunday-weekly-必填内容) 重建跨日技术演进，
   完成 Books Comparison 和 Semantic Audit。

## 7. No Material Update

没有候选达到长期门槛时，仍应：

- 保存完整 Required Daily receipt；
- 说明 bounded discovery 与不可证明范围；
- 闭合低分、重复、版本事实和噪声；
- 明确写出：`今日未发现足以修改核心知识库的重要进展`。

不得用空泛的“无更新”替代 Coverage 证据。

## 8. 质量与 Git Safety

结束前执行 [Report 合同 §10](./docs/REPORT_CONTRACTS.md#10-校验命令) 的校验。最终交付必须分开
报告结构校验与 Semantic Audit，不得把前者表述成“证据已验收”。

不 stage、commit、push，不清理、覆盖或回滚运行前已有修改。

## 9. 最终交付

最终答复按 Report 合同概括重要发现、Books 变更或不变原因、未解决材料、三个 Gate、校验结果与待人工 Review 的工作树范围。
