# 2026-05-27 Fresh Non-Author Post-write Review — Bounded Path Repair

- Reviewer role: fresh non-author；未参与 05-27 author rebuild 或三项 root Books writeback。
- Scope: 只复核冻结的 `692 = 94 retained + 598 pre-denominator closure`、94 项 Evidence、Books 投影和三项最新写回；未扩来源、日期或候选。
- Verdict: 三项 Books 语义绑定通过原文反向核验；发现并修复一处 comparison 元数据断链。由于本 reviewer 已成为 repair author，本轮不能签署最终 PASS，Daily 继续保持 `Ongoing`，等待另一名 fresh non-author 做最小终审。

## 语义核验结果

1. `2605.26089` / Ch23：paired marker 完整承载 quantization axis 改变 representation unit、sequence length 与 AR factorization；明确 channel 没有天然顺序，nested dropout 只在所测设置中诱导 coarse-to-fine ordering。正文同时保留 patch/grid VQ、连续 feature 和独立 decoder 的共存/回退边界，并限制在作者的图像重建、文生图和 matched token-budget 证据内。
2. `2605.26097` / Ch29：paired marker 将 retention signal、spare capacity 与 optimization speed 放在同一设计判断中；明确低 learning rate 只交换 steps/compute，自生成 replay/KL 不能越过容量下界。正文保留真实 replay、低 LR/早停、adapter/扩容或停止更新的 fallback，并限定于 controlled mixtures、单任务和一个 1B Verilog slice。
3. `2605.26099` / Ch22：paired marker 未漂移。论文事实是 KV clear 前执行多轮 offline recurrence 并把计算移到 consolidation phase；atomic commit、state version 与恢复 Gate 明确标成项目系统推论。证据边界、失败模式和 full/sliding KV、普通 recurrent update、外部检索 fallback 均完整。

## 有界修复

`books-comparison-v3.json` 中 `2605.26089` 的相邻章节错误指向不存在的 `books/part-02-model/17-transformer.md`，已机械修正为当前真实路径 `books/part-02-model/17-transformer-layer.md`。没有修改 adopted proposition、评分、Evidence、Books decision、正文或 marker。

## 已验证不变量

- Screening：`692 = 94 retained + 598 closure`；retained 唯一且与 Evidence 集合一致。
- Evidence：94/94 deep、complete，三维评分逐项求和正确。
- Books：61 Applied + 33 No Change；root queue `pending_count=0`。
- 三个目标 paired marker 的 start/end 均各 1 个，且位于各章首个 `## Review notes` 之前。
- `scripts/validate_research.py`、JSON 解析、路径存在性复查、marker 检查与 scoped `git diff --check` 均通过。

下一名 reviewer 只需确认该路径修复没有引入漂移，并将 comparison/queue 的 pending-review 状态与 README `Complete` 原子同步；不应重开来源或全文审查。
