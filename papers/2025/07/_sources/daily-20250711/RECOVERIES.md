# DAY定点来源修复

仅复用原始官方响应、独立筛自己的窗口，不读取另一日报或其判断。

## Anthropic

原始入口：https://www.anthropic.com/research 。root指出SSR包含历史publications，不应仅按可见十项断言受阻。作者独立读取root提供的`daily-20250721/anthropic.raw`原件后，按相同结构回到本日已有`anthropic.raw`解析（因此最终依据保留于本日原件，不依赖其他日报判断）。

从`self.__next_f.push`中的一个JSON字符串payload递归提取`_type=post`且含`publishedOn`的记录；共174条序列化记录、172个不同slug（含两条重复），不是174/172篇新论文。只读取邻接目标窗的目录切片：

- `2025-07-15T00:00:00.000Z` / `claude-4-cyber` / Detailed cyber evaluations of Claude 4。
- `2025-06-27T06:51:00.000Z` / `how-people-use-claude-for-support-advice-and-companionship`。
- `2025-06-27T06:05:00.000Z` / `project-vend-1`。

该目录所有July `publishedOn`仅7/15，与6/27邻接越过本窗；目录无本窗条目。illustration的`_createdAt/_updatedAt`不是论文公开日期，未用作事件clock。完整邻接post objects保留`anthropic-pubs-slice.json`；原始payload保留本日`anthropic.raw`。此处检查仅原目录此日期切片，不声称所有未列修订/全站活动完整。

## DeepSeek

原始入口：https://api-docs.deepseek.com/updates 。root提供`daily-20250701/deepseek-updates.raw`为官方响应，附request URL与检查时间`2026-10-06T15:55:09.121239+00:00`、HTTP200。作者只读取同一原始HTML、独立定位目标窗口邻接h2。

`date-2025-08-21`（DeepSeek-V3.1）后直接接`date-2025-05-28`（deepseek-reasoner/R1-0528），无2025年7月更新。原始相邻HTML片段保留`deepseek-updates-slice.raw`，包含Aug21段与下一May28 h2以保留邻接关系。只据此判官方updates目录此段无命中，不采用窗外benchmark/架构事实，不称全站/全部paper revision无遗漏。
