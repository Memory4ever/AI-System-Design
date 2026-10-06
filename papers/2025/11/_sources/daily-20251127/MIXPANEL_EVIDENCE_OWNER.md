# Nov27 Mixpanel 单项证据与owner比较

作者Aristotle。准入/必要安全证据/Books等待root非作者校准；本文件不是整日通过。Source family拟`SF-2025-OPENAI-MIXPANEL-INCIDENT`。

## 事件与采用范围

[OpenAI原公告](https://openai.com/index/mixpanel-incident/)本日原生RSS的`Wed, 26 Nov 2025 19:00:00 GMT`支持BJT2025-11-27T03:00:00+08:00，完全落[Nov26 09,Nov27 09)。见[本日RSS窗筛](./openai-window.json)及[安全原核心](./raw-security-boundary2.json)。Nov9 aware/Nov25收到dataset分别为事故调查节点，不作为本窗公开时刻。

拟2+2+2=6，因安全与当前更正信号深入受影响范围：已实际原核心L19–60、FAQ64–105，必要厂商对照L269–287，未读无关安全附件。原文新增的是一个具体局部反证：OpenAI声明API系统/内容未被攻破，同时承认外部frontend analytics导出了可与账号关联的姓名/email、粗粒度地理位置、OS/browser、referrer及organization/user IDs。因此“主要服务未攻破”不能推出完整账号数据链路无暴露。这不是借用MFA成熟原则评分，也不证明LLM模型漏洞或prompt内容泄漏。

`No chat/API requests/API usage/passwords/API keys/payment/government IDs`等均按OpenAI厂商调查权限保留，不宣称独立取证、攻击复现或全无风险。已有数据可能被用于phishing/social engineering是风险描述，不是已测成功攻击量；未公布受影响人数、风险概率与防护效果，不补数字。

## 必要对照与晚更正

[Mixpanel原通告](https://mixpanel.com/blog/sms-security-incident/)原生HTML及[实际定点核心](./raw-primary-counterpart7.json)已读：日字段Nov27，时区/时刻未知，不给独立本窗family。其Nov8 detect smishing与OpenAI Nov9 aware是不同主体/节点，不自动冲突。撤销sessions/sign-ins、轮换credentials、employee password resets、authentication/session/export logs forensics及新增controls是厂商披露的处置；没有独立效果数据，不借其“未收到通知即未影响”断言授全平台安全保证，也不把后续通告内容冒充本窗已公开事实。

当前OpenAI正文明确标记Dec19 clarification：最初API用户范围补充到少量help-center/platform登录ChatGPT用户。实际受影响正文/FAQ已核；报告保留更正信号，但不把晚文字当Nov26历史冻结版、不给更正重新落本窗。当前tokens/session/authentication未受影响等FAQ亦保留厂商权限与当前版边界。停止在事件边界、身份analytics暴露和直接受影响更正；不扩全部vendor审查。

## Books实际比较

实际按ROADMAP读取`PLATFORM-SECURITY` [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) L1–120、328–416；相邻[Ch71](../../../../../books/part-06-ai-infrastructure/71-multi-tenant.md)L1–50、[Ch73](../../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)L1–65，并已读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE。本次恢复定点重读Ch72 L14–30/107–118/342–365与相邻段确认未变；首次路径误写multi-tenancy/production-readiness已纠正，以ROADMAP真实路径为准。

**拟已有覆盖，0写入，非新长期缺口。** Ch72“资产与信任边界”实际要求枚举主体、数据流与信任转换；其端到端observable data flow段明确单组件验证不能外推端到端安全、遗漏channel产生错误all-clear，实际承载上述命题。检测/隔离/最终归因与限定通知段亦明确known/unknown和通知不代修复。现有覆盖不因为没有Mixpanel名字而失效。Ch71 evidence plane负责metric/log/trace access与redaction，Ch73 Governance proof obligation负责敏感telemetry/owner/evidence/recovery，交接不需新增并行安全owner。

这些是当前Books结构对本次知识采用的比较，不声称2025当时书稿已包含2026实例，也不把现有理论的成熟原则算成事故本身新增机制。具体事故事实留报告，不补造供应商取证实现或泛化定律。

## 独立核验请求与停点

请root定点核本日RSS身份/时刻、原公告受影响core及Dec19更正权限、Mixpanel后续核心日期隔离，以及Ch72上述具体覆盖/Ch71与73交接。单项准备好即可判，不等27其余日期保留/来源；作者不写共享Books，若Existing通过无写后POST对象。普通其余继续本日有限边界与查漏，整日仍进行中。
