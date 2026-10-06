# 2025-10-01 首批准入与必要证据

作者：root / Codex。窗口BJT `[2025-09-30T09:00:00+08:00,2025-10-01T09:00:00+08:00)`。恢复按当前V3合同，不从其他月份报告反推本日候选。

## 同一家族，而非七篇新研究

本日[官方RSS原件](openai.xml)1245项中七个案例页均原pubDate `Wed, 01 Oct 2025 00:00:00 GMT`，换算BJT08:00。每个原页明确指向同一份October 2025 threat intelligence report，七页只是其案例呈现，不拆成七个家族。正文原日期Oct1与RSS一致；保留原字段权限，不从RSS宣称互联网上首次出现的全面证明。原PDF入口因13,394,397bytes超web工具限制失败，不把该请求算PDF正文读取。

原始PDF：[October 2025报告](https://cdn.openai.com/threat-intelligence-reports/7d662b68-952f-4dfd-a2f2-fe55b041cc4a/disrupting-malicious-uses-of-ai-october-2025.pdf)。本轮采用案例原HTML，不依赖未读的PDF附件、截图像素或第三方调查全文。

## 为什么继续核验

需要检验的代理指标假设是将生成量/跨平台展示或一次拒答近似为实际影响/安全结果 → 本次Stop News纠正OpenAI自身既有传播影响分级，Russian-speaking案例指出直接恶意请求被拒后仍跨会话获取双用途片段 → 应分别验证真实受众触达与行为组合风险，而非用局部指标替代结果。不据此声称本项目曾采用错误分级。评分针对这两项新增的局部纠错/观测边界：Design Delta2 + System Reach1 + Durability2 =5。安全与实际纠错使受影响核心深入审阅，不借安全治理的通用原则加3分，不称新通用检测算法或因果试验。

## 已实际读的原HTML核心与采用边界

| 同报告案例 | 实际原入口/位置 | 必要结论及边界 |
| --- | --- | --- |
| Nine-emdash Line | [原页](https://openai.com/index/disrupting-malicious-uses-of-ai-nine-emdash-line/)，Actor/Behavior/Completions/Impact | 多平台内容量不等真实受众；Category2、少量互动。未识别技术关联，不能按相似外观确定组织身份；便利性不证明新增能力。 |
| Scam operations | [原页](https://openai.com/index/disrupting-malicious-uses-of-ai-scam-operations/)，完整核心L26～54 | 主要嵌入既有诈骗流程、翻译与扩量，封禁后持久换行为。估计识别诈骗使用多于诈骗使用不等受害损失净因果下降，没有全流量/效果分母。 |
| Stop News | [原页](https://openai.com/index/disrupting-malicious-uses-of-ai-stop-news-2025/)，核心L25～50 | 原Category3依据的媒体合作后来被判虚构，修正Category2。模型生成/跨平台投放不等真实社区突破；其他视频工具未独立确认，不归因全部视频给OpenAI。 |
| PRC-linked abuse | [原页](https://openai.com/index/disrupting-malicious-uses-of-ai-prc-linked-abuse/)，核心L26～44 | 已封禁账户选择性样本，规划/宣传不等实施监控；机构采用、具体工具部署不可独立确认，不把请求意图当已发生环境结果。 |
| Korean-language | [原页](https://openai.com/index/disrupting-malicious-uses-of-ai-korean-language-malware-support/)，核心L25～49 | 跨账户窄任务、双用途上下文及外部指标重叠，不能独立国家归因；未见恶意二进制由模型生成或超公开技巧的新能力。 |
| Phishing/scripting | [原页](https://openai.com/index/disrupting-malicious-uses-of-ai-phishing-and-scripting-support/)，核心L25～53 | 语言本地化、迭代脚本提效，技术仍有粗糙错误；未确认DeepSeek自动化最终实施或实际用哪个模型，不归因新攻击能力。 |
| Russian-speaking | [原页](https://openai.com/index/disrupting-malicious-uses-of-ai-russian-speaking-malware-tooling/)，本轮补读核心L25～48，含Completions与Impact | 直接恶意请求被拒后获取双用途片段，持续跨会话迭代；可能在平台外组装。本案模型未执行攻击者工具或工作流，平台外活动无法独立验证。作者未发现超公开资源的新能力，拒绝直接exploit/keylogger请求；不等完整攻击成功、净伤害为零或普遍无能力提升。 |

局部厂商观测不提供检测召回率、漏报率或总体发生率；模型/hardware/precision/输入输出/batch/concurrency/SLO未披露，不用这些案例作生产安全保证。真实原反侧不是通篇实验无效；无需遍历无关政治事件或历史全部归因。

## 代表性排除及未完成

RSS的Sep30 Sora2、responsible launch与card原字段BJT08:00在起点前一小时，只作窗外恢复线索，不纳当前候选，也未读取/授该card安全结论。Samsung/SK Stargate原Oct1T03Z在终点后；商业合作不因有GPU词自动贡献准入。Anthropic本日原Research嵌入对象174、去重172；独立结构化复查窗前最近项原字段2025-09-15T20:33:00.000Z（BJT09/16 04:33），窗后最近项2025-10-03T18:31:00.000Z（BJT10/04 02:31）。本次返回数组无落窗项，不当全站无研究。

独立首批准入复核见[FIRST_INDEPENDENT_REVIEW.md](FIRST_INDEPENDENT_REVIEW.md)。本轮已落实R1/R2并实际补读Russian末尾；剩余本日来源/arXiv与具体Books owner比较仍普通工作。首批准入未变化结果复用，不由本包授整日完成；不stage、commit或push。
