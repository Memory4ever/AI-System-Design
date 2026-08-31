# AI System Study Tasks

`tasks/` 是个人学习执行层。它不替代其他目录：

- `books/` 保存长期、可维护的知识解释；
- `labs/` 保存可复现的实验合同与产物；
- `interview/` 保存求职训练与 Mock；
- `tasks/` 只回答：本周学什么、每章掌握到哪一级、升级依据是什么。

## 使用入口

1. 阅读 [24 周学习计划](./STUDY_PLAN.md)，确认当前阶段与本周主题。
2. 在 [逐章学习矩阵](./CHAPTER_MATRIX.md) 中查看章节目标、实验和目标 Level。
3. 使用 [执行 Checklist](./CHECKLIST.md) 推进本周任务。
4. 章节通过验收后，更新唯一进度真值 [progress.yaml](./progress.yaml)，并附上证据路径。
5. 每周使用 [周复盘模板](./templates/WEEKLY_REVIEW.md) 记录预测偏差、知识债务和下一步。

已有 Books、聊天回答、实验或工作经验不自动折算为 Level。只有重新对照以下 Gate 并留下可定位证据后，
才能更新 `current_level`。

## 六级掌握度

Level 是累积门禁。达到 `L4` 意味着 `L1～L4` 均有证据，而不是只完成一项源码阅读。

| Level | 能力 | 通过证据 |
| --- | --- | --- |
| L0 / Unassessed | 尚未验收 | 允许已有经验，但不推定掌握 |
| L1 What | 知道对象、输入输出和知识树位置 | 闭卷 3 分钟解释，不依赖术语堆砌 |
| L2 Why | 能从问题、朴素方案和失败推导现代设计 | 回答 Why、trade-off、旧方案共存边界和相邻章节连接 |
| L3 Derive | 能推导核心公式、shape、状态机或资源预算 | 独立完成一个数值例子，并在验证前写下 prediction |
| L4 Source | 能把机制映射到 primary source 或源码 hot path | 保存版本、入口、关键状态/控制流和不能外推的边界 |
| L5 Experiment | 能用受控实验验证机制和失败边界 | 复用对应 Lab，至少达到 `E2`：correctness、control group、measurement、反例 |
| L6 Design / Debug | 能在未知场景中设计、诊断和优化 | 完成定量预算、故障假设、观测方案、替代设计，并通过 fresh-context challenge |

## 章节升级规则

每次升级至少完成以下动作：

```text
Question
→ Hypothesis
→ Prediction
→ Source / Derivation
→ Experiment or Scenario
→ Observation
→ Gap
→ Updated Mental Model
→ Evidence Link
```

- L1～L2：可使用闭卷讲解、反例问答和概念图作为证据。
- L3：必须保存公式、shape、状态流或容量预算，不能只引用 Books 正文。
- L4：版本敏感实现必须绑定 commit、tag 或文档版本。
- L5：实验报告使用 [`labs/_templates/EXPERIMENT_REPORT.md`](../labs/_templates/EXPERIMENT_REPORT.md)，不得以“跑通 Demo”替代受控比较。
- L6：必须由未参与原学习过程的 Reviewer、Mock interviewer 或 fresh-context Agent 提出反例并复核修正。
- 同一证据可以支持多个章节，但必须逐章说明它证明什么；不能因为完成一个大 Lab 自动升级所有关联章节。

## 状态与知识债务

`progress.yaml` 只使用以下状态：

```text
unassessed
in_progress
blocked
passed
refresh_due
```

- `passed`：当前 Level 的累积证据完整。
- `blocked`：缺硬件、源码访问、数据或前置知识，必须写明 blocker。
- `refresh_due`：长期原理仍成立，但版本敏感的 L4～L6 证据需要更新。
- `knowledge_debt`：明确记录尚未推导、未验证或仍靠类比理解的部分，不因章节文字完整而隐藏。

## 固定节奏

每周投入 10～12 小时，默认分配为：

```text
Primary source / Books     3h
Derivation / source trace  2h
Experiment / profiling     3～4h
Compression / writing      1～2h
Closed-book explanation    1h
```

一周只在证据完成后结束；没有完成的任务进入下一周 `knowledge_debt`，不回填虚假的完成勾选。
