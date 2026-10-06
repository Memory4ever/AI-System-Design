# 2026-01-28 原入口及恢复停点

检查时间：2026-10-04T12:42:00+08:00（各请求真实检查时刻在 JSON；本行是整理时刻）。本窗固定为2026-01-27T09:00+08 ～ 01-28T09:00+08。以下历史目录缺口不支持“没有遗漏”。所有当前可执行的有限恢复已停止，不扩大历史/周级来源。

| ID | 实际入口与停点 | 结果/必要限制 |
| --- | --- | --- |
| SRC-OPENAI | official news RSS403；定点Introducing Prism direct403，web primary正文恢复 | Prism 产品组合/科学写作应用没有新增机制，关闭；Research历史完整性仍不可恢复，终态隔离 |
| SRC-ANTHROPIC | Research403；定点官方Jan27研究查询仅发现GOV.UK合作发布 | 商业部署公告不证明技术增量，未采用；Research历史目录终态缺口 |
| SRC-GOOGLE-AI | Research Jan2026月页完整标题读到Jan28～Jan8；Jan27ATLAS、Jan28agent-scaling核心说明可读；DeepMind current blog入口 | 两篇blog复述旧研究，无本次新机制；DeepMind当前列表不能证明历史完整，隔离 |
| SRC-META-AI | research响应仅57字 | interstitial/empty不能当无命中；恢复条件为当窗相关历史目录/原发布 |
| SRC-QWEN | qwenlm.github.io当前页最新仍2025-09-23并指向qwen.ai | 旧入口不证明Jan2026无发布；定点query没有恢复完整历史，隔离 |
| SRC-DEEPSEEK | 首页静态533字；news429；web primary当前research精选10篇读到2025-05 | OCR2 nativeJan28和具体ID已恢复，日精度不够；精选列表不覆盖全历史 |
| SRC-MOONSHOT | platform blog旧主题列表1178字；官方tech blog308到新URL403；web primary新URL正文可读，officialmodel/help只说Jan27 | K2.5 PARL机制已作潜在贡献识别，必要发布时间隔离；不使用Feb技术报告或后续300-agent说明替代1月公开 |
| SRC-TENCENT-HUNYUAN | 首查research只有“腾讯混元”；按来源要求浏览器create tab70s超时、getTab到aboutblank成功、goto research35s超时kernel reset | 无完整“全部”研究目录；浏览器恢复已实际尝试，不静态空页记无命中；能运行并读取当窗dated all list时定点重开 |
| SRC-ZAI | 首查Research日期顺序列表15条，读到2025-12-09；本窗被Jan19和Feb2条目夹住，查看更多从更旧区间开始 | 可见区间未见Jan27条目；不能扩大成全站无遗漏，无必要正文缺口 |
| SRC-BYTEDANCE-SEED | 首查Research精选10篇含Jan27Keel，public_papers当前18条主要May～Aug；定点Keel publication正文+v1AB | nativeJan27时区/时刻未披露，论文提交18:58Z不决定native公开；两个目录非历史完整，隔离 |
| SRC-BAIDU-ERNIE | blog第1页10条，Jan29→Jan15→Jan8；next page开始更旧条目（2025年），本窗可见排序段读完 | 可见区间没有Jan27发布；不声称网络所有百度研究无遗漏 |
| SRC-XIAOMI-MIMO | 主入口10129字当前产品/首页，未给完整研究日期；定点nativeJan2026研究查询未恢复 | 首页无日期不等于无发布；历史paper/blog目录终态缺口 |
| SRC-MINIMAX | blog12条日期顺序列表，Jan27M2-her被Feb12和Dec23夹住，定点M2-her原核心说明 | 日精度+JSON-LD午夜合成值不足确定窗口，终态保留；不使用该值造精确公开 |
| SRC-ARXIV | 四主题API429；DataCite四主题2/1/2/1页去重377发现线索；monthly相关标题有限补检；106个定点v1原AB完整读完 | schedule+created为93事件支持落窗包络，非93候选；老Submitted10+Keel/OCR2必要日期保留。实际贡献/证据停点见SCREENING/REVIEWS，不将monthly无dayheading推成所有项受阻，不称全分类召回或无遗漏 |

辅助搜索只恢复身份/原入口：日期窄 query 包含 site.github.com/MoonshotAI/Kimi-K2.5 “January 27”、site.mimo.xiaomi.com “2026-01” research、site.anthropic.com/research “Jan 27, 2026”、site.ai.meta.com “January 27, 2026” research，四条各一页结果；native原页恢复优先。后两项搜索返回商业公告/非目标文献不支持历史目录完整。搜索检索受限不代替primary证据。

## Web primary 恢复的可复查说明

- DeepSeek current news primary `https://deepseek.com/en/news/`：Research Index中OCR2（Jan28）/Engram（Jan12）/mHC（Dec31）相邻，链接OCR2为2601.20552。没有发布时间；精选列表不可据此排除全部未收录研究。
- Kimi旧tech URL `https://www.kimi.com/blog/kimi-k2-5.html` 经web重定向 `https://www.kimi.ai/blog/kimi-k2-5`。§2公开PARL：trainable orchestrator+frozen subagent、并行实例化和完成率辅助奖励逐渐退火、CriticalSteps含主agent开销与最慢subagent。可支持潜在新执行/训练命题，但本次不采用4.5×/安全保证。官方model `https://www.kimi.ai/ai-models/kimi-k2-5` 与Moonshot官方help repo仅日精度Jan27发布日期；后续更新内容不能证明初版准确时刻。
- OpenAI `https://openai.com/index/introducing-prism/`：介绍LaTeX scientific writing workspace与现成GPT功能，无本文提出的原创模型/系统机制；停于贡献排除，不再为日期发请求。
- Google agent-scaling旧Dec17v2精确AB已持久保存，不使用当前Apr8v3替旧版。本次blog核心数值差别不构成已披露的新实验/方法或安全条件。

## 终态保留的采用边界

目录不可恢复项只保留明确来源/入口/失败/停止范围：没有ID时不造材料，也不推定零命中；有ID的必要日期保留项按SCREENING逐项身份重开。可接受替代是该历史窗官方dated目录或明确首次公开正文日志，非搜索发布时间、不是Submitted/Updated的改名。所有保留项不支持正面候选/Books/性能/安全/无遗漏；缺口不因机器校验消失。
