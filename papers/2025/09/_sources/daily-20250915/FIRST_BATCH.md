# 2025-09-15 首批提案：root校准请求

作者Bacon，本窗2025-09-14T09:00:00+08:00～2025-09-15T09:00:00+08:00；尚无root准入或DAY，不自授通过。来源/题摘工作继续，不等待全部附件。

## GPT-5-Codex card：具体贡献有潜力，精确版本日期有反侧

官方RSS原pubDate为 `Mon, 15 Sep 2025 00:00:00 GMT`，对应本窗08:00BJT。官方落地页可见September15、model/product两层防护说明；HTTP403已保留错误body，web实际恢复正文。只凭这条RSS还不能证明当前七页PDF在08:00BJT已公开：下载原PDF metadata CreationDate/ModDate均 `D:20250915165852Z`，CDN响应 Last-Modified=`Mon, 15 Sep 2025 17:00:07 GMT`。两者都在本窗结束之后。metadata/Last-Modified本身也不是首公开，不能反向强授另日，只能作为版本归属的重要反侧。当前采用链隔离，不列正式候选；请root判断RSS支持落地发布的范围与PDF历史版本差额。可接受替代为当窗原始卡片、官方更正/发布版本时刻或完整落窗区间，不机械要秒级。

原源：[官方说明](https://openai.com/index/gpt-5-system-card-addendum-gpt-5-codex/)、[官方七页PDF](https://cdn.openai.com/pdf/97cc5669-7a25-4e63-b15f-5fd5bdc4d149/gpt-5-codex-system-card.pdf)。本地原PDF293503B与请求metadata、逐页提取均保存；作者实际读7页，没有核代码或复现。

若日期/版本准入成立，拟命题为：代码Agent接触网络/代码等不可信内容→卡片分别披露instruction-hierarchy训练与接口相关的sandbox/网络权限→评估模型拒绝不能替代实际effect约束。建议2+2+2=6，但未给隔离项正式评分。重点必要证据：§2.1–2.2 pp3–4及Tables3/4；§4.1–4.2 pp6–7；§1 Tables1/2与§3限作者评价权限。表4是内部任务中忽略注入的比例，两模型均0.98，未披露样本/重复、CI、完整攻击者权限和现实effect分母，不能证明exfiltration/backdoor/destruction都被防住。表1几个类别低于GPT5-thinking，厂商称自然噪声但未给不确定性，不采用“已统计证实噪声”的因果。默认网络关闭/工作区文件限制与用户批准unsandboxed/放宽网络是不同配置；没有在此读出完整审批控制流保证。

实际owner对读：[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) `PLATFORM-SECURITY` 1245–1273已承载模型提案→schema→policy→可选approval→最小权限executor及effect前重授权；764–812已区分prompt测试、完整run/attempt、scorer与release，不以单ASR授保证。[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) `PLATFORM-EVALUATION-SYSTEM` 104–118固定eligible population、failure taxonomy、scorer与uncertainty。相邻[Ch71](../../../../../books/part-06-ai-infrastructure/71-multi-tenant.md)实际1–75在control/data/resource/evidence平面承载tenant/credential/network隔离；[Ch73](../../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)实际25–55把运行身份/质量/governance证据与发布门禁分开。

Books建议为日期解决后NoChange/版本事实仅报告，不增段落：上述具体论点已承载机制，Seatbelt/seccomp/landlock和该版本默认网络只是卡片公开的接口事实，不是新长期链，也未审当前实现。若root认为有差额，应在Ch72现有工具边界段自然补接口配置反侧而非另建产品小节；作者不写Books。日期未解决时全部保持暂缓，这不是已通过Books NoChange。

## CyberSOCEval：必要评价反侧已补读，日期隔离

[Meta官方完整题摘](https://ai.meta.com/research/publications/cybersoceval-benchmarking-llms-capabilities-for-malware-analysis-and-threat-intelligence-reasoning/)与原PDF必要pp6–10/12–14实际读取，详[NECESSARY_CORE](NECESSARY_CORE.md)。默认provider thinking设置、不同模型对照，不是同模型同预算test-time scaling；只保留该任务配置的局部反侧，不采用训练scaling因果或真实SOC保证。目录/原文仅September15无timezone，尚不能确定落窗，当前不评分、不遍历剩余附件。

## arXiv题摘首批

本日96唯一当前版本，82完整题摘已实际读（补11191随机adversarial training、11369音乐生成来源）；提交范围是有限发现而非公开归属。建议root先校准11076 SmartSwap、11155 AQUA、11254 PowerSGD+、11167 OTA/FFG、11145 Text2Mem、10963 composite-null，以及10931/11128/11250风险潜力；代表关闭10935 Spotlight、10937 clickbait、11071驾驶组合、11198 quantum QAS、12282科学工作流组合。完整具体逐项理由见[SCREEN](SCREEN.md)；安全/设计反证不普通抽样跳过。未变成82篇全文队列。

正式家族0；必要core实际11家族（Codex1+精确v1九项+Meta1），逐source/version/位置/边界与条件owner见[NECESSARY_CORE](NECESSARY_CORE.md)。FIRST需root核该packet及SCREEN全部potential/代表关闭；特别保留11128v1 ENJ与新版ERIS身份差异、PowerSGD零向量QR证明争议，不以datehold免必要反侧。
