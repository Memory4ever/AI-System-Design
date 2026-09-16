# Daily Research — 2026-06-06

**规范：** V3
**窗口：** 2026-06-05T09:00:00+08:00 ～ 2026-06-06T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T22:00:00+08:00

## 1. 结论

本窗重新核实 canonical owner 恢复结果，arXiv 去重 raw identity 与 owner bucket 均为 0。旧 submission-date 条目已迁往真实 owner 日，不在本日重复计数；本轮厂商源再认证恢复 Kimi Code 0.11.0，并已完成 release Evidence 与 Books 比较。旧完成标签未直接继承，本次以现存 0-row arXiv inventory、owner receipt、厂商候选和撤回清理重新闭合。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [厂商源再认证](../_sources/daily-20260601/CURRENT_CONTRACT_DAILY_SOURCE_RECERT_20260914.md#来源结论)：本窗无保留事件 | 已检查 | 无 |
| SRC-ANTHROPIC | 同上；Making Claude a chemist 属暂缓的 AI for Science，已关闭 | 已检查 | 无 |
| SRC-GOOGLE-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-META-AI | 同上；SIRA 指向 05-07 首次公开家族，非重要修订去重 | 已检查 | 无 |
| SRC-QWEN | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-DEEPSEEK | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MOONSHOT | 同上；Kimi Code 0.11.0 的精确 release 时刻落在本窗，见候选与判断 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 同上；“全部”列表本窗无条目 | 已检查 | 无 |
| SRC-ZAI | 同上；Research 列表本窗无条目 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 同上；技术博客本窗无条目 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MINIMAX | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-ARXIV | [`canonical-raw-identity-inventory-v2.1.json.gz`](../_sources/daily-20260606/canonical-raw-identity-inventory-v2.1.json.gz) 与 [`official-arxiv-first-public-owner-receipt-v1.json`](../_sources/daily-20260606/official-arxiv-first-public-owner-receipt-v1.json) 复核，本日 owner identity 为 0 | 已检查 | 无 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.11.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.11.0) | 2026-06-05T18:26:45+08:00 | 层级 sub-skill discovery 与固定 subagent timeout 把 capability lookup 与 delegation budget 显式化；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` — [章节](../../../../books/part-07-agent/84-agent-platform.md) |

本窗 arXiv owner identity 为 0；厂商源再认证恢复 1 个候选家族。

## 4. 证据与知识整合

### [Kimi Code 0.11.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.11.0)

官方 release 支持实验性 sub-skill inventory/consolidation、built-in skill 命令与固定 30 分钟 subagent timeout；它只证明公开版本行为，不证明层级划分正确、超时恢复完整或跨 workload 的收益。`AGENT-PLATFORM` 已要求 capability/skill identity、activation、evaluation 与 lifecycle，`AGENT-MULTI-AGENT` 已要求 delegation timeout/handoff，因此 No Change。其余采样参数和 UI patch 作为版本事实关闭。

arXiv 空分母仍由月份级 DOI/announcement owner 对账与本日 0-row packet 支持；撤回家族没有残留正向采用链。

## 5. 缺口与下一步

无

本窗没有外部材料请求或可执行待办。

## 6. 复核

复核者：`fresh-context:canonical-owner-empty-denominator`（复用未变化的非作者独立复核）

结论：通过

复核检查 0 条 arXiv raw identity、厂商候选、跨日迁出、撤回清理与 Books 判断；不依赖旧完成标签。两个 V3 校验与限定 diff check 在本轮执行。
