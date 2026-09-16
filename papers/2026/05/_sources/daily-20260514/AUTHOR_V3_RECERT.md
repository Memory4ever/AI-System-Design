# 2026-05-14 V3 作者重认证 checkpoint

- 唯一 active raw identity：714（official OAI direct=539，revision recovery=175）。
- V3 窄准入：arXiv retained=77，pre-denominator closure=637，withdrawn=0；13 个非 arXiv Daily source 全部终态，OpenAI retained=2；总 Candidate Denominator=79。
- exact-v1：77/77 HTML 可达；章节定位来自实际页面标题，blocked=0。
- 非 arXiv primary：2/2 官方全文可达；其余 12 个来源为可核验 no-hit，未跨日期扩展。
- Books：79 项均完成 owner 文件与现有具体论点对读；78 项作者建议 No Change — Existing Coverage，Windows sandbox 已由 root 写回 `PLATFORM-SECURITY` 并保留 `SF-2026-OPENAI-WINDOWS-SANDBOX` 标记。作者未编辑共享 Books。
- 最终 Gate：未自签；等待 root 与 fresh nonauthor reviewer。

## 714 / 745 冲突

745 账本按 submitted_v1_utc 组窗，而该字段只是提交来源，不能替代首次公开/官方公告时间。两个集合交集=518、714-only=196、745-only=227，并非“旧账本多 31 条”；因此 745 整体失效，714 owner-day receipt 是本次唯一 active inventory。

## 非 arXiv Daily sources

`non-arxiv-source-coverage-v3.json` 是本 checkpoint 的逐源终态：13/13 已检查、0 unresolved。OpenAI 官方 RSS 在严格窗口命中 2 条并完成全文审阅；Anthropic、Google AI、Meta、Qwen、DeepSeek、Moonshot、Hunyuan、Z.ai、Seed、Baidu ERNIE、MiMo 与 MiniMax 均为有具体入口与相邻记录依据的 no-hit。Seed 的两条 05-14 date-only 目录项经 linked arXiv first-public timestamp 核对后均落在截止点之后，没有回拨到本日。
