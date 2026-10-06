# 2025-10-10 FIRST 小包

本窗2025-10-09T09:00+08～10-10T09:00+08。作者Mill；非作者校准未到，不授正面Evidence。原core响应official_core_web.json；额外官方题摘/代表排除additional_core_web.json。拟入选2个官方说明家族，候选分母未冻结。

## 拟入选

1. [Anthropic small-samples-poison](https://www.anthropic.com/research/small-samples-poison)：Research原SSR publishedOn=2025-10-09T13:50:00.000Z（BJT21:50）。处理的是官方技术说明事件，不冒称[2510.07192v1](https://arxiv.org/abs/2510.07192v1)首次公开同刻；论文只有submitted 10-08 16:25Z，需定点裁决先公开/同事件归属。旧威胁评估以污染比例为尺度→600M～13B、三seed/24配置的DoS backdoor实验保持污染文档绝对数→需要把文档数和干净token预算分开，而不能推定扩大干净语料自动稀释风险。拟3+2+3=8，但只评分这个实验修正，不借通用安全原则。官方core同时明示仅gibberish trigger，不能外推更大模型/代码后门/绕过guard。
2. [OpenAI political bias evaluation](https://openai.com/index/defining-and-evaluating-political-bias-in-llms/)：本日新读RSS10-09 13:00GMT（BJT21:00）与官方日期一致。多选立场问卷遗漏开放式交互行为→100主题×5倾向、五行为轴与LLM grader→需要区分挑战集条件风险和生产人口估计，而不是把平均立场分数当全部偏差。拟2+1+2=5；不借泛化“评价要切片”给高分，不采<0.01%为独立实测或跨地区保证。

## 代表性排除/日期保留

- [XR Blocks](https://research.google/blog/xr-blocks-accelerating-ai-xr-innovation/)完整官方core已读：Script/Reality Model/Core将WebXR、Three.js、LiteRT与Gemini接成XR原型，Reality Model是可替换接口模块，不是learned transition world model。现说明没有新的基础模型机制、可比系统收益/失效边界；不因有World/Agent词而入选。日名10-09未经时区确认；贡献已明确不足，不为其新增日期任务。
- arXiv四主题只做start0/max30有界线索与官方标题补检，不把截断库存变全文队列；当前public time缺口不当学术贡献排除。原API混最新版本，不能当v1。

## Books预比较（未最终采用）

`TRAIN-DATA` Ch27正文[内容无害不等于更新无害](../../../../../books/part-04-training-system/27-data.md#内容无害不等于更新无害过滤器还要预测-training-effect)与[代码可运行](../../../../../books/part-04-training-system/27-data.md#代码可运行不等于它适合训练代码模型)已承载canary/训练recipe/来源lineage，但没有本小包的“绝对污染文档数与干净token量非同尺度”命题。是否新增长期差额须独核必要v1/order/posttraining反侧后再提出，作者不写书。

`PLATFORM-EVALUATION-SYSTEM` Ch66[为什么选一个分数不是评估系统](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#为什么选一个分数不是评估系统)实际正文已有切片、scorer对象、非随机反馈与高风险平均掩盖；Ch67[先定义目标](../../../../../books/part-06-ai-infrastructure/67-monitoring.md#先定义目标再选择可测信号)邻接负责运行信号而非语义裁定。OpenAI五轴若只有具体rubric实例，则仅报告，不强造diff。

请求非作者：先裁日期/技术说明事件与先公开论文关系，再校准两条准入链与XR代表排除。通过后作者继续受影响必要证据与最终Books判断；未到校准可继续其它独立日初筛。
