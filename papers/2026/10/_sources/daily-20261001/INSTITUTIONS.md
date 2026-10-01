# 2026-10-01 机构来源：本日有限检查

窗口：2026-09-30T09:00:00+08:00 ～ 2026-10-01T09:00:00+08:00。实际检查：2026-10-01 13:21～14:00 北京时间。只处理每日组；目录旧条目只核日期停止，不制造全文队列。以下是检查依据，不是全机构零遗漏保证。

## 入口、停止范围与限制

| ID | 实际入口与停止位置 | 结果与边界 |
| --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/news/research/) 与 [RSS](https://openai.com/news/rss.xml)；RSS 首 8 项至 09/28，最新两个为 09/30。web RSS 错误后原始 XML 可读 | 窗内两个事件；distillation campaign 拟入选，小企业培训/顾问公告核心说明排除。RSS 日期而非 Research 子栏证明事件时间 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 最新 09/30→09/29→09/25；打开 09/30 唯一新文核心问题与方法 | 职业机器人可行性估算排除，理由见下；不逐读旧目录 |
| SRC-GOOGLE-AI | [DeepMind publications](https://deepmind.google/research/publications/) 首页 30 项，最新 09/16；[Research Blog](https://research.google/blog/) 最新 09/29→09/24；[DeepMind Blog](https://deepmind.google/blog/) 顶部 Argon 发布卡回原文 | Argon 精确时刻落窗；Google pubs 年份目录没有可靠日排序，只作辅助线索，不把全年条目列为本日待办或证明全覆盖 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) 空响应，恢复到 [Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1) 首页面最新前缀 09/24→09/07→09/06→08/04；[Blog](https://ai.meta.com/blog/) 首页面最新可见日期 07/27、含较旧置顶 | 已检查有限公开入口；Blog 混排与空 Research 不支持全机构无遗漏。未见确定窗内事件，未把空响应记零 |
| SRC-QWEN | [Research](https://qwen.ai/research)、[Blog](https://qwen.ai/blog) 与旧主页跳转均无可提取目录；fresh原HTML两页同为应用壳，公开首页脚本亦未提供带日期研究列表 | 本窗动态目录终态隔离；页面脚本08/10是开屏下架时间，不是research公开日期。浏览器替代因锁屏/建tab超时未能恢复，不要求无限重试或把它记零；取得官方带日期列表/具体链接时定点重开 |
| SRC-DEEPSEEK | [News/Research](https://www.deepseek.com/news/) 可见 News 5 项最新 09/10，Research 10 项最新 06/24；Show All 无可提取后续 | 有限可见最新前缀均窗外；未遍历历史，未声称动态后续全量覆盖 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog) 可见 26 项最新 2025/11；[kimi-cli releases](https://github.com/MoonshotAI/kimi-cli/releases) 最新 1.52.0 为 09/22、上一项 09/21，09/23 archive 标记 | 沿具体模型/Agent 发布入口有界检查，未见本窗新事件；不是枚举 org 的所有普通 commit |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research) 空壳后按公开页面实际 route JS 恢复 API：`https://api.hunyuan.tencent.com/api/blog/publicList`，POST `pageNum=1,pageSize=30,renderType=0` | code 0；totalNum=11、返回11，全部列表已取完。核 publicAt/publishedAt/displayPublishTime/updatedAt，全部早于窗口；不用 createdAt 当首次公开。最新两个 publicAt 为1790053389/1790049600。仅公开列表请求，无登录/内部接口 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) web 旧缓存后 fresh urllib 原页；最新日期 08/26→08/14→06/16；[Release notes](https://docs.z.ai/release-notes/new-released) 最新 08/26→08/18 | 已检查当前可读目录最新边界，未见窗内事件；无旧论文重审 |
| SRC-BYTEDANCE-SEED | [Public papers](https://seed.bytedance.com/en/public_papers) newest 首页20/242，13页中第1页，最新08/18→08/12→08/06→07月；[Research](https://seed.bytedance.com/en/research) 最新07/06；[Blog](https://seed.bytedance.com/en/blog) 无可提取列表 | 按逆序已越过当前窗停止，不遍历242；Blog 动态入口单独保留，不由论文列表替它背书 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/) 首页最新05/09→04/30→04/15→02月 | 最新可见发布窗外即停止，不扫旧模型 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/) Paper 8项最新06/29→03/13→02/03；Blog 15卡片无时刻；公开route JS恢复首卡[tool-call repetition](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)原文日期09/27，模型页仍无日期 | 首卡已证窗外，不重审该旧文；其余Blog目录日期未恢复，终态隔离。不能仅凭首卡窗外断言15项全部零；官方本窗带时刻目录/文章到达时局部重开 |
| SRC-MINIMAX | [EN Blog](https://www.minimax.io/blog)、[CN Blog](https://www.minimax.cn/blog) 可读目录最新08/13→07/31→06/09；[Agent Tech Blog](https://agent.minimax.io/docs/techblog) 无正文；[llms index](https://agent.minimax.io/docs/llms.txt) 指向 techblog.md，实际打开失败 | 主目录有限检查完成；Agent 子目录缺实际文章/日期，不用旧目录推断零，恢复入口明确 |

## 首批题摘/核心说明判断

以下“拟/待”措辞保存初批准入时点，不是当前待办；两正项目前均为 Ch72 实际整合、独立来源与写后 PASS，详见末节及正式日报。两负项实际核心说明独立复核已关闭。

- **OPENAI-DISTILLATION-CAMPAIGN**：[原文](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/)，RSS `Wed, 30 Sep 2026 10:30:00 GMT` = 09/30 18:30 北京时间。密文不是完整隔离契约 → 跨会话重放及 scope 收紧 → 需区分 artifact 保密与消费权限。拟 3+2+3=8；读攻击路径、保护动作与局限，不采用归因/成功率或推断密码破解。相连的旧 [2608.09867v1](https://arxiv.org/abs/2608.09867) 只作上下文，不纳入本窗或重读旧版本。拟 owner `PLATFORM-SECURITY` Ch72；待独立 PRE。
- **GOOGLE-GEMINI4-ARGON-RELEASE**：[原文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)，JSON-LD `2026-09-30T20:00:00+00:00` = 10/01 04:00 北京时间。模型能力不等于统一发布权限 → 受限 cyber profile、监测/隔离与训练反馈边界 → 重新核对 release/security 契约。拟3+2+2=7。公开说明支持厂商版本事实，不证明内部模型机制或普适安全；不采用裸榜单数字。比较 Ch72 具体 sensor/authority 论点后决定整合、已有覆盖或仅报告，不因入选强制改书。
- **ANTHROPIC-ROBOT-WORK-EXPOSURE**：[原文](https://www.anthropic.com/research/what-work-can-robots-do)，JSON-LD `2026-09-30T16:01:00.000Z` = 10/01 00:01。已读核心问题、任务拆解与估算方法：职业暴露/成本情景，不提出新的 VLA 闭环控制或模型系统机制；估计不改现有控制/评价 contract。pre-denominator closure，不评分、不读无关附件；供非作者漏收抽核。
- **OPENAI-SMALL-BUSINESS**：[原文](https://openai.com/index/helping-small-businesses-put-ai-to-work)，RSS09/30 10:00GMT =18:00北京时间。核心为培训/顾问支持与采用，不新增模型/Infra设计或验证约束；pre-denominator closure。并非因机构或经济类标签自动排除。

## 审阅与恢复状态

机构两项准入/必要来源与actual Books POST均获 `sep22_resume_v3` 独立PASS：Ch72两个原论证seam，各两窄段，未覆盖旧机制；来源与工程推断分开。Qwen、Seed Blog、MiMo其余无钟Blog、MiniMax Agent目录均已穷尽本次可用有限原页/公开索引替代，终态隔离，不支持正面证据、Books或全覆盖断言。恢复仅需官方当窗带日期目录或具体原文，不请求用户整个机构历年文档。

独立机构初筛覆盖2正2反全部；arXiv与整体日级Gate仍进行中，不以该机构batch冒称整日报告完成。arXiv 作者只写本日 ARXIV.md；root 唯一写正式 Daily/共享 Books/LEARNING_STATE。
