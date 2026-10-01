# 04/28 四项已核 Existing 的 arXiv 日期有界提案（作者侧）

固定窗口 `[2026-04-27 09:00, 2026-04-28 09:00)` 北京时间。本记录只核 arXiv v1 的日期组合，不替代 Source Family 更早机构全文查找、非作者日期复核或整日 Gate。[官方公告规则](https://info.arxiv.org/help/availability.html)给出周五 14:00 EDT 后至周一 14:00 EDT 的正常周一 20:00 EDT 公告槽，即北京时间 04/28 08:00；arXiv ID 在公告时才分配。`2604.23073v1` 的连续 ID 邻界、OAI/早 Updated 组合已另获[非作者有限日期通过](./V3_ROOT_23073_DATE_BOUNDARY_INDEPENDENT.md)，可作本簇交叉锚点，但不能替代下列各身份的例外检查。

| 官方 v1 | 投稿原字段及本地原 receipt | 作者侧有界判断 |
| --- | --- | --- |
| [2604.22981v1 TCRM](https://arxiv.org/abs/2604.22981v1) | `[v1] Fri, 24 Apr 2026 19:49:56 UTC`；既存 receipt v1 Updated `04/28T00:08:18Z`。 | 投稿已晚于周五 18:00Z 截点，正常进入周一公告；ID 在 `.23073` 之前且处理字段在本窗截止前。与公告规则、相邻簇共同支持本窗 08～09 的**有据推断**，不是 Updated 秒点即公开。 |
| [2604.23036v1 Long-tailed Expert SFT](https://arxiv.org/abs/2604.23036v1) | `[v1] Fri, 24 Apr 2026 21:48:20 UTC`；receipt Updated `04/28T00:11:19Z`；后续 v2 为 09/08，不回填当前版本。 | 同批有据推断；后续 v2 与本次首发分开，不能从当前 HTML 默认版本倒填正文。 |
| [2604.23080v1 Agent Discovery](https://arxiv.org/abs/2604.23080v1) | `[v1] Sat, 25 Apr 2026 00:21:35 UTC`；receipt Updated `04/28T00:13:56Z`。 | 周末投稿与相邻 `.23073` 同簇，正常周一公告；只能推断 arXiv 路径，不断言 Agent 项目页无更早全文。 |
| [2604.23205v1 Tessera](https://arxiv.org/abs/2604.23205v1) | `[v1] Sat, 25 Apr 2026 08:29:50 UTC`；receipt Updated `04/28T00:25:07Z`。 | 同批有据推断；官方 v1 摘要/正文的硬件测量与 proxy 证据边界由[单篇 source→body 复核](./V3_ROOT_FIVE_EXISTING_BODY_INDEPENDENT.md)另判，日期不证明评估成立。 |

四项 exact-v1→实际 Ch32/21/84/72 机制正文已由 root [独立对读](./V3_ROOT_FIVE_EXISTING_BODY_INDEPENDENT.md)通过；本页不再据此预记正式候选。若逐篇出现延迟审核/撤回、公告簇跳变或同族更早公开正文，应重开其 first-public owner。下一步请非作者仅核这四条日期组合与明确反例，而非重读全部机制附件；通过后方可从 Date Pending 移为本日正式已判定子集。
