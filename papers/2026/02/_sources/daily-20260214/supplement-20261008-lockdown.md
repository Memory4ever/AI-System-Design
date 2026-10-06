# OpenAI Lockdown：本日官方事件最小准入与必要Source包

只处理2026-02-14补充北京2026-02-13。本项与已终态57论文分开；原30冻结。官方[事件页](https://openai.com/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/)标Feb13，[本日实际RSS](./supplement-20261008-native-first.json)同标题/链接pubDate Feb13 10:00UTC，因此公开日期为2026-02-13。此次实际读官方原始公告保留正文（web31969view0行38–65）；行31–34明确June4追加，个人账户/后来功能清单不倒填Feb13。本日有限检查未见对Feb13核心机制的撤回说明，不遍历产品站/帮助中心。

拟准入：模型层拒绝无法单独限制外部工具出网→公告披露确定性禁用部分能力、浏览仅消费缓存、管理员限制app/actions→把功能取舍与网络effect authority分开。**2+2+2=6**；涉及安全控制变更，必要受影响内容深入，不按产品名/风险标签准入。公告只支持厂商公开控制事实：缓存浏览不向其受控网络外发实时请求；risk label是告知，不是授权、防泄漏证明或完整边界；管理员可保留指定app/action，不能读成所有外部交互全部关闭。无公开攻击率/utility对照、实现证据或形式安全证明；硬件/precision/batch/并发/模型版本/性能人口不适用产品控制事实，真实时延/总费与独立安全评价未披露，不补造。

必要核心与直接反侧足STOP，不追当前HelpCenter功能组合或June新版。条件是管理员配置与具体外部能力路径；公告的deterministic声明不授全部连接、隐式通道/缓存内容可信、无prompt injection或已泄漏可撤回。代码/实验未核。拟**仅报告＋已有原则覆盖**，唯一PLATFORM-SECURITY：作者actual Ch72 1383–1411已将query当发送前egress action、受隐私与目的gate约束并保留私有索引/fail-closed；1279–1296已有最小service account/network egress与sandbox，实际工具/权限路径仍须独立执行。现书没有声称已有该产品模式配方，声明的缓存-only/管理员控制是本日版本事实，不能据名称制造新通用边界。root已实际打开原始官方38–65、区分June更新并核RSS/日期；独立准入/必要Source和actual Ch72 Only/Existing通过，在57新论文日期权限撤回后，现为本轮唯一确定新增；候选表原30＋本项=31，不计新Books写入、不自授DAY。实际裁决见[独立core-first](./supplement-20261008-independent-core-first.md)。
