# Nov19 Codex-Max authorized single-family reopening

作者Dalton；2026-10-04T19:12:00+08:00。仅恢复用户指定的同家族日期保留；未重扫19或月份。此前准入范围见[root原裁决](UI_AND_TRAINING_INDEPENDENT_CALIBRATION.md)，该裁决没有授日期/Evidence/Books。

## Actual Date and Identity

本次GET官方[RSS](https://openai.com/news/rss.xml)成功200、759641 bytes，[实际raw](codex_reopen_openai_rss.xml)及[receipt](codex_reopen_openai_rss.xml.receipt.json)保留。只解析两个精确guid，不把完整feed当新队列：

| title | guid/link | category | 原pubDate |
| --- | --- | --- | --- |
| GPT-5.1-Codex-Max System Card | https://openai.com/index/gpt-5-1-codex-max-system-card | Publication | Wed, 19 Nov 2025 00:00:00 GMT |
| Building more with GPT-5.1-Codex-Max | https://openai.com/index/gpt-5-1-codex-max | Product | Wed, 19 Nov 2025 00:00:00 GMT |

转换为2025-11-19T08:00:00+08:00，完全落在19窗[Nov18 09,Nov19 09)。本次采用官方publication/release事件，不以Nov19整日或submitted替代。官方[publication入口](https://openai.com/index/gpt-5-1-codex-max-system-card/)实际L13日期Nov19，L19链接指向此前同一Safety Hub card，L23–27介绍一致，见[入口原响应](WEB_CODEX_CARD_ENTRY.json)。Safety Hub L95仍为Published November18、未给时区；保留冲突字段，不宣称RSS证明该正文最早公开时刻，亦不改写它。正式候选采用官方发布事件及其所链接的披露，非另造论文首次公开。

## Necessary Core and Counter-side

复用已校准的[原core](WEB_OPENAI_TAIL.txt) L204–207，并本次实际打开同一官方card，见[本次响应](WEB_CODEX_REOPEN.json) L204–207；关键内容一致。原静态指令无法覆盖rollout途中用户修改造成的冲突；厂商披露在RL中由user model制造conflicting edits，对不revert用户改动给予正强化，并称建立destructive-actions评价。这是训练环境的具体扰动，不是仅把原则改写成状态术语。准入2+2+1=5；安全约束改变，受影响core深入。

仅采用这条厂商机制披露及评价对象。未披露user model身份/采样、edit timing/冲突强度、reward定义、独立干预对照、样本与该项结果，不能归因收益、证明冲突均被保护或生产安全。本次同页§3.1 L161–170说明sandbox/用户可批准unsandboxed；模型被训练不revert不代替执行权限/文件状态检查。§4.2 L185–203说明外部不可信输入仍有注入面；不扩大为全卡cyber/biology评价。所读关键段无明示撤回/纠错，不为此遍历完整版本史。compaction、Windows、benchmark与token宣传数字不作为本项采用命题。

## Owner Delta for Root

实际读取当前`TRAIN-RLHF` [Ch31](../../../../../books/part-04-training-system/31-rlhf.md) L39–74、166附近的多轮用户模拟器/分支归因、L364–392 reward代理与独立安全评价、L430–474环境transition/observation-credit及L1038–1042小结；相邻Ch30开篇与Ch32 L10–42实际读取。`AGENT-TOOL-CALLING` [Ch78](../../../../../books/part-07-agent/78-tool-calling.md) L59–77承载proposal→validation→authorization；这不是本次新贡献。

具体差额：Ch31的用户模拟器段讨论不同对话分支造成的trajectory preference混杂；这里是同一代码rollout中外生用户对共享workspace的冲突编辑，以及保留这些编辑的强化。已有正文不等于已经覆盖该配方，但当前披露没有可复查的分布/目标或效果边界，新增的是该版本采用的训练实例，不建立新长期有效性结论。作者建议**仅报告**，不是按owner名称缺位/成熟原则关闭准入；root若认为该训练实例值得嵌入，最小位置为Ch31 RLHF pipeline之后的environment/trajectory身份论证，只写“用户模拟器可改变rollout中共享状态；task reward与保留外生编辑需分账，独立执行gate仍必要”，不写安全收益。该处涉及共享Books，须root另行协调窄锁与非写入者POST，作者未写Books。

## Precise Stop

2026-10-04T19:39:03+08:00接收并同步root独立协调反馈：已实际核RSS两个guid+timezone、publication L13–27对Safety Hub身份、原日期冲突、同card L161–207（冲突编辑L206–207、sandbox/注入反侧）及Ch31 pipeline/trajectory/environment credit正文。局部5分厂商披露、必要Evidence与OnlyReport0写入独立通过；官方publication/release作为事件，不认证正文最早公开，不授扰动/reward/独立对照未披露的安全有效性，训练不代授权。19 README仅同步本项完成态与§1/3/4/5/6，旧日级未变范围复用，无新Books/POST。不重审Gemini、18篇论文保留项或其余来源；未stage/commit/push。
