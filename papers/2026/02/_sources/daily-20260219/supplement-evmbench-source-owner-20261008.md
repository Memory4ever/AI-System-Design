# EVMbench 必要 Source / actual owner 比较（作者，待独立）

补充事件日期：官方正文标 2026-02-18；原 RSS Feb18 00Z 是同 BJT 自然日。原候选与旧窗口不改。本次采用材料仅 [OpenAI 日期原文](https://openai.com/index/introducing-evmbench/) 的核心三评价对象及直接限制（HTML34–49）；不是对链接 PDF 初版或实验数字的采用。原版身份许可不能被后续 PDF 的 117/120 数差或修改时间单独否定，未发现这些核心机制已被纠正/撤回的公告。

## 采用与停止

detect 用审计已知漏洞的 recall；patch 用功能保持与 exploit checks；exploit 用隔离本地链的交易重放及链状态判据。它们不是同一 correctness authority，已知标签命中不认证新增发现，程序执行也不自动等价真实链安全。官方核心同时指出未知额外发现难分真误报、顺序重放不覆盖精确时序、干净 Anvil 非 mainnet fork且限单链。这些是研究作者公开协议与边界，不是我们复现的判据完备性证明。

不采用排行榜、漏洞人口、模型比较、准确率、生产攻击成功或防护保证。当前 CDN PDF 120 与 blog 117 不合、Last-Modified 位于补充日之后，只使未采实验人口/精确 PDF 初版保持未决，不扩大为不相关版本恢复请求。本次不依赖 PDF 才能作出的结论不因此隔离。不查代码/额外附件，协议和关键反侧已经足以支持本次限定命题。

评分：Design Delta2 + System Reach2 + Durability2 = 6。评分对象是三评价对象/authority与范围分账，不借安全重要性或实验数字加分；标准审阅完成。局部区块链实例不单独决定准入，也不假称建立一种全新通用验证算法。

## actual owner / No Change 提案

已完整读取 ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE；本轮 LS 路由与 owner 交接，Ch65结尾→Ch66开篇→Ch67开篇。StableID 为 `PLATFORM-EVALUATION-SYSTEM`，不是安全漏洞内容或链运行时的另建 owner。

实际 Ch66:1965–1981 的完整论证已经把 evaluation object 从文本推进为 artifact+environment+execution trace，要求 exploit compile/run/目标条件、冻结目标版本/网络/时间/成功判据，明确 executable非groundtruth、verifier可能不完备与 sandbox非真实环境。Ch66:1983–1991的完整 preservation 段要求请求变化与未请求行为分别验证；Ch66:2010–2026冻结维护/执行契约，并区分代理与最终 correctness；本次完整顺读了1940–2065的该论证及相邻段。detect已知标签、patch preservation、exploit sandbox replay 在这个实际既有论证中的权限与边界已有承载，EVMbench未披露一项必须增改该推理链的独立新验证机制。拟决定为**已有覆盖 / No Change**，不是仅凭相同主题名。案例中具体单链、Anvil和时序限制留在报告，不把版本相关条件扩成普遍链系统规则；无 Books 写入提案、无共享锁或 POST。

root非作者独立Source/PRE及最终DAY已通过，实际范围见[非作者记录](./supplement-independent-20261008.md)末节。未更改Books，也未声称代码复现。
