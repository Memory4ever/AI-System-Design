# 03/04 有界非作者复核

复核者 mar02_v3；复核时报告作者 root。2026-10-01T22:04:28+08:00。窗口03/03 09:00→03/04 09:00 BJT。此记录先于接手剩余项作者角色；只覆盖下列范围，不授整日报完成，不代作者修改结论。按当前AGENTS、研究/来源/Report合同、Prompt、ROADMAP及本日README/停点重新加载；不读Weekly或将旧33/1270库存变成队列。

## 六项首批

独立打开00356、00357、01639、01776、01914 exact-v1完整题摘与历史；01865 abs访问失败后恢复[exact-v1 HTML](https://arxiv.org/html/2603.01865v1)完整题摘。准入分别是容量预留/结算、冗余stack重排、draft/verify cycle成本协同、秩亏条件下activation多变换与weight共享、固定panel均衡预算、halt/KVreuse一致性；不是题材映射。5～7分合理，没有发现需改成全9分的依据。

独立DataCite实际核得client=arxiv.content、state=findable，registered UTC 03/03依次04:44:56、04:44:57、05:14:34、05:17:41、05:19:47、05:20:55，与作者原值一致。按[官方公告表](https://info.arxiv.org/help/availability.html)Friday14→Monday14的提交在Monday20EST公告，前两篇Friday22:44UTC已越Friday19UTC截止；另四篇Monday截止前。结合[ID/DOI不预分配原则](https://info.arxiv.org/help/doi.html)和原机构findable登记，可支持本日报中的完全落窗区间，不把Submitted或登记单独当公开时刻，也不证明没有更早作者发布。

00356另实际读[§3–5](https://arxiv.org/html/2603.00356v1)及Ch56 945–953。现正文真实承载input+max_tokens预留、吞吐/KV/并发、completion成本与debt、preemption未验证和单Qwen3-8B-NVFP4负载范围。本日报窄采用命题的已有覆盖成立。原题摘更宽的admission/autoscaling统一容量授权，不由此自动宣布整篇机制全覆盖；单固定replica实验也不证明新autoscaling收益。其余五项实际Books POST按root明确提供的mar01结果复用，不无差别重复附件。

## 有限尾批建议

### 00811 Curation Leaks

实际完整题摘及[§3.1/Table1、§3.5、§4.1–4.4、§5–6](https://arxiv.org/html/2603.00811v1)：private target未进入训练，仍能通过其指导的public pool选择泄漏参与身份。score/mask是被动观察；最终model攻击还要求向pool主动注入fingerprint，不能写成任意被动黑盒恢复。TRAK随target规模变化，DP/删高风险样本不授零泄漏。建议准入3+1+3=7，PLATFORM-SECURITY。Ch72 262–264已区分训练成员/筛选参与者，但缺private-guided public pool且private完全不训练的直接反例；可窄补机制及三种观察合同，不复制攻击清单。

实际[v1](https://arxiv.org/abs/2603.00811v1)Submitted02/28T21:14:01Z；[DataCite](https://api.datacite.org/dois/10.48550/arXiv.2603.00811)arxiv.content/findable registered03/03T04:55:26Z。同官方复合依据可支持03/03T09:00～12:55:27+08完全落窗。

### 01499 Collaborative Obfuscation

实际完整题摘及[§3.1–3.2、§4.1、§5.1–5.2、§6.2–6.4](https://arxiv.org/html/2603.01499v1)：honest-but-curious server，联合token/model变换以保持受限推理，另加noise保护映射。建议2+2+3=7、PLATFORM-SECURITY，不能仅因重命名/混淆标签关闭。只采用数据与权重共同改变、等价计算不等于保密保证的边界；不授worst-case密码学安全。Table2 Qwen3 VMA恢复约19–25%、BF16大lambda退化、noise不足攻击增强，反驳摘要性能/隐私数字的普遍外推。未核全部定理，不能声称形式保证验收。

实际[v1](https://arxiv.org/abs/2603.01499v1)Submitted03/02T06:16:36Z；[DataCite](https://api.datacite.org/dois/10.48550/arXiv.2603.01499)arxiv.content/findable registered03/03T05:11:21Z，复合范围03/03T09:00～13:11:22+08完全落窗。live-v1标题Collaborative，正文Covariant机制；旧inventory标题不是权限更高的身份来源。

### QwenCode v0.11.1 / PR2021

实际[release API](https://api.github.com/repos/QwenLM/qwen-code/releases/tags/v0.11.1)published03/03T13:08:44Z、release明确包含[PR2021](https://github.com/QwenLM/qwen-code/pull/2021)。PR created02/28T11:25:53Z、merged03/02T12:59:36Z，head f59328aada7155c863f6c304fee304fd22a250d9，merge f770be495ffebc8dd80b661af263ba42fba4e62c；本窗采用release事件，不伪称首次PR公開在本窗。

实际[files API](https://api.github.com/repos/QwenLM/qwen-code/pulls/2021/files?per_page=100)读parser/converter/turn/scheduler及相应tests：provider误报stop/tool_calls时，结构未闭合检测覆盖为length，pending calls携带截断flag，Kind.Edit拒绝，nonEdit仍可执行。repair可产生合法但内容不完整参数，所以finish/schema合法不授完整effect。建议3+1+3=7、AGENT-TOOL-CALLING，安全correctness窄深入；不授全部provider/工具/跨调用事务保证，tests未本地运行。Ch78 88附近已有finish批次门槛，但缺provider伪finish与repair完整性这层反例，可窄补。

### GPT-5.3 Instant release/card

实际[发布核心](https://openai.com/index/gpt-5-3-instant/)及[Hub §3.1](https://deploymentsafety.openai.com/gpt-5-3-instant)：release机制未披露不按产品名准入；card动态user response轨迹及any-assistant-turn/message分母有具体evaluation增量，安全回归、offline/online差异、系统护栏须保留。可准入2+1+3=6并窄深入；Ch66 2363–2367已覆盖adaptive轨迹，不自动补书，未见该card final-only与message-share/episode风险的具体分母对照。安全本地结果不外推线上保证。

**日期冲突未解决**：已保存并复查官方RSS release/card pubDate03/03T10:00GMT=BJT18:00；Hub却显示PublishedMarch2，模型版本shipped2/26不等于card公開。March3发布事件确定，card首次公开仍需官方带时区公开/历史正文记录，或明确March3为重要修订的版本差额，不能把RSS单独覆盖更早首发。PDF链接一次解析失败，未宣称已读PDF。作者应分开release与card事件，对不能落窗的card增量隔离，不绕过日期推进Books。

### Gemini 3.1 Flash-Lite

实际[Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/)core及原JSON-LD datePublished03/03T16:34+00=BJT03/04T00:34；[card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite/)架构/训练沿用Pro、thinking tiers及价格速度不足新增机制。card负侧安全表、query/grader改进不可跨旧卡直比、manual复核与借最强Pro评估推断已窄读；没有发现改变现有evaluation设计条件的新机制。可贡献前关闭、不评分；须留下具名安全反证检查，不能用‘更快更便宜所以准入’或‘厂商卡所以零风险’。此建议不授整个家族所有未披露机制。

## 来源/剩余边界

重新打开[Kimi实际目录](https://www.kimi.com/en/blog/)，19条至Mooncake2024/06/26、2/09AgentSwarm→4/20K2.6跨本窗，没有可见3月行；原报告旧platform缺口不能代表实际Research不可恢复。可有限已检查，不授全机构历史完整。DeepSeek隐藏News及其他已有具体隔离不由本次解除。

本复核六项准入/日期/00356具体已有覆盖通过；五项Books采用root提供的非作者POST结果。尾批原文和建议只涵盖上述5家族；Gemini为具名安全负侧样本，不是全量排除验收。没有复核未具名‘其余有限信号’、全部负侧、旧33或1270宽库存；作者需在实际本日入口范围内具名有限信号或说明其停止依据，不创建全库存队列。正式分母与日级验收尚未授予。本文件未改Books、LS/索引或正式03/04报告，无stage/commit/push。
