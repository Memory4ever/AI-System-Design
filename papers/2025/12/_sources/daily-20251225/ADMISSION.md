# 12/25 首批准入校准与停点

检查时间：2026-10-02T17:28:32+08:00。作者：Feynman；未独立复核。
窗口：2025-12-24T09:00:00+08:00 ～ 2025-12-25T09:00:00+08:00，含起不含止。

本文件不是完成声明。尚无已确认落窗的拟入选；以下是实际入口发现与代表性负侧，供主线程先校准理由。继续检查其他每日来源与 arXiv，不等待校准。

## 实际发现

| 原始材料 | 日期原值与证据 | 准入判断 | 后续 |
| --- | --- | --- | --- |
| [Qwen-Image-Edit-2511: Improve Consistency](https://qwen.ai/blog?id=qwen-image-edit-2511) | 官方 Blog `2025/12/23`，未给时区/时刻。原入口 qwenlm.github.io 已提示迁移到 qwen.ai。 | 有潜在贡献，不按发布标签排除：独立 LoRA 组合/身份漂移约束 → 官方声称将选定社区 LoRA 整合进基础模型并改善多主体一致性 → 应核实基础模型内置能力与外接适配器的边界。仅展示图不能支持质量收益归因。尚不评分。 | 首公开日期未证明落入 12/25；不计确定候选。若官方精确记录证实较早公开，交对应日期作者；不得用 12/24 转载日期改归属。 |
| [ERNIE Blog：ERNIE-5.0-Preview-1203 位居 LMArena 中国文本模型榜首](https://ernie.baidu.com/blog/zh/) | 目录 `2025年12月23日`，相邻上项为 `2026年1月8日`。 | 代表性负侧：核心说明只有排名与分数，没有新增机制、混杂分析、适用条件或对既有评价结论的具体反证；主题相关和排行领先不足准入。不评分。 | 贡献已明确排除，不为不影响处置的时刻继续材料请求。未核实精确首公开时刻，不作为窗内零命中证明。 |
| [MiniMax M2.1 官方发布](https://www.minimax.io/blog) | 完整可见目录从 `2026-01-27` 到 `2025-12-23` 再到 `2025-10-27`；M2.1 标注 `2025-12-23`。 | 多语言代码与 Agent 框架泛化是值得核验的主张，但目录简介不够完成贡献筛选；不是因已有 Books 或读文成本而排除。 | 日期邻近线索，不转成 12/25 候选；精确正文只在确认本窗事件/重要修订后必要读取。 |
| [GLM-4.7 发布说明](https://docs.z.ai/release-notes/new-released) | 官方日期 `2025-12-22`；下一模型条目 `2026-01-14`。 | 本窗发现的较早版本事件，不因重新被检索就重列候选；暂未宣称前日报已有效审阅。 | Research 目录首查超时，仍需有限替代/浏览器恢复；release 目录不能证明 research 无窗内论文。 |

## arXiv 原始入口状态

- 官方 advanced query：abstract=`language model`，首次公告字段 `announced_date_first`，日期范围 `2025-12-23` 至 `2025-12-25`，size=200、start=0；直接 HTTP 200，正文明确 `Sorry, your query returned no results`，查询回显同上述条件。该结果只证明这个实际查询返回空，不证明所有主题零命中。
- 同范围 all=`LLM` 的官方 advanced query：直接 HTTP 200，同样明确无结果；没有下一页。
- 官方 `https://arxiv.org/list/cs.CL/2512` 以及 `?show=2000` 返回 404；带 skip/show 的 web 抓取还出现 timeout/400。历史官方列表补检仍为缺口，不能拿提交记录或当前假日安排填补。
- 已启动 submitted_date 的局部同义词查询，仅恢复身份线索，不用 submitted_date 作归属。

## 主线程校准后修正

2026-10-02T17:38:54+08:00，依据主线程独立意见与直接官方响应：

- arXiv 的 `announced_date_first` 日粒度空返回不支持本窗零命中或覆盖；本字段实际只提供年月过滤。前述两次查询保留为失败的历史切片尝试，而非有效日查询。长格式官方月列表 `https://arxiv.org/list/cs.CL/2025-12?show=2000&skip=0` 已恢复，1302 条仅作身份/有界相关标题线索，未逐项排队；它仍不证明日公告。
- Qwen-Image-Edit-2511 贡献前关闭：官方 `Built-in Support for Community-Created LoRAs` 段仅称选定社区 LoRA 直接内置在基础模型，未公开新增合入算法、可复用的新适用边界或受控收益归因。一致性部分为展示性例图；不能用既有 LoRA merge 原理给本次产品更新补造长期机制。不评分，不因 Books 已覆盖或审阅耗时排除。外窗与准入判断分开，12/25 不列确定候选。
- ERNIE 普通负侧的关闭理由获主线程校准，详见本目录 `ROOT_ADMISSION_REVIEW.md`；该校准不代表本日来源、候选证据或 Books 验收。
- Z.ai Research 直接 HTTP 恢复正文：首屏按时间排序可见 2026/01/13 后接 2025/12/10 GLM-TTS，再接 2025/12/09 GLM-ASR-Nano；此次可见时间切片无 12/24 发布。release 目录与 research 目录分别记录，不能互相替代。

下一可执行项：补齐 arXiv 多模态/系统/Agent 主题查询与官方列表有限替代，恢复 Hunyuan 动态目录，补齐其余每日源的目标窗口检查；对实际新线索逐篇贡献筛选、必要日期核验，再评分与正文审阅。不得将这些尚未做的工作标为外部受阻。

## 第二批：确认落窗的 Kimi CLI 0.68

检查时间：2026-10-02T17:46:24+08:00。

原始事件：[0.68 release](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.68)，GitHub 官方 releases/tags/0.68 API 实际字段 `published_at=2025-12-24T12:40:22Z`，换算 `2025-12-24T20:40:22+08:00`，完全落窗。`created_at=2025-12-24T12:37:28Z` 是另一个字段，不混用。已读完整 release body 与官方 changelog 0.68 的十项。

拟准入命题：原先 CLI 自己持有 MCP 连接与本地 Shell 执行位置 → 0.68 实际新增 ACP 客户端托管 MCP、在客户端终端执行命令（有能力条件）、OAuth 认证/清除/测试命令 → 需要重新检查工具执行位置、客户端能力协商与凭据生命周期，不能继续把 Agent 所在进程等同于执行/授权 owner。这是此次实际兼容性与权限边界变化，不把通用 RPC 或 OAuth 原理当创新。拟评分 `2 + 2 + 2 = 6`；因实际执行/授权约束变化，深入审阅受影响实现，不审整份 release 无关优化。

原始必要位置：release 引用 [PR521](https://github.com/MoonshotAI/kimi-cli/pull/521)、[PR522](https://github.com/MoonshotAI/kimi-cli/pull/522)、[PR479](https://github.com/MoonshotAI/kimi-cli/pull/479)。官方 API 已恢复三者正文：521 只有模板无机制解释；522 body=null；479 Summary/Changes 明确 OAuth 命令及 HTTP transport 用法。下一步读取 release 0.68 精确实现与必要测试，不由空 PR 正文推定机制不存在。拟 owner `AGENT-TOOL-CALLING` / `AGENT-MCP`，最终唯一 owner 与 Books 决定待具体相邻正文比较和证据校准。

## 动态目录恢复的实际边界

混元 Research 页面公开 JS 依次引用 index-CUQAWQeM.js → index-cEoitnb7.js，后者公开 `POST /api/blog/publicList`；主组件公开生产 base `https://api.hunyuan.tencent.com`，请求参数 `pageNum=1,pageSize=1000,renderType=0`（全部页签，原 UI 默认）。实际 HTTP 成功 `code=0,totalNum=11,list.length=11`。可见最早项 `Learning from context is harder than we thought`，displayPublishTime=1770092288，换算 2026-02-03T12:18:08+08:00；全部十一项均为 2026。此当前目录不保存目标历史，不据此称 2025 尚无来源或本窗零。

字段 publicAt / publishedAt / displayPublishTime 均为不同秒值；只恢复当前目录，不把任一当前修改时间赋给 2025。已作官方域限定 12/24 搜索替代，搜索实际忽略域限定返回其他仓库，不能支持混元覆盖；不继续无限重试同目录。
