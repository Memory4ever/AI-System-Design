# 2026-10-03 首批事件与有限准入校准材料

检查时间：2026-10-03T09:06:30+08:00。窗口：2026-10-02T09:00:00+08:00～2026-10-03T09:00:00+08:00。
本文件只保存本日有限发现和真实原文定位；不是 Evidence/Books/日级通过收据。拟候选尚为0；以下是负侧或窗外线索，不评分。

## A1 Google 新Blog与旧论文身份

实际打开原源：[Google Blog](https://research.google/blog/toward-provably-private-learning-from-federated-data/)，页面显示 October 2, 2026，无时区/时刻。
已读核心说明：Building a verifiably private FL system（数据上传、KMS-policy、root/worker TEE及加密恢复）；How TEE-based FL strengthens privacy（透明日志、reproducible builds、动态sideload）；How Gboard is using TEE-based FL；What's next（当前TEE边界/side channel，未取得完整software correctness proof）。

小段原文：逻辑限制为“all privacy-relevant logic remains hardcoded in the Python program”（§Verifiable execution with dynamic sideloading）。不把此博客说成任意动态程序或硬件无条件安全保证。

[arXiv完整题摘](https://arxiv.org/abs/2609.31494)显示v1 Submitted on 25 Sep 2026、v4 last revised 30 Sep 2026。version history原值：
- v1 Fri, 25 Sep 2026 16:34:25 UTC
- v2 Mon, 28 Sep 2026 16:53:03 UTC
- v3 Tue, 29 Sep 2026 17:01:41 UTC
- v4 Wed, 30 Sep 2026 02:32:53 UTC

摘要完整语义：以TEE建立下一代FL，提供外部可验证central DP，改善privacy–utility tradeoff；设备上传由TEE-KMS管理密钥的加密数据；数据被密码学绑定到限定server TEE Python programs的policy；外部可查公开透明日志；优化已收集数据的参与排程摆脱设备在线时段约束；作者称Gboard已productionized、训练更快、更低隐私预算下更好accuracy。这里的提交字段不等于首次公开；准确旧归属仍需官方公告或更早作者原页。

拟处置：10/02 Blog传播事件核心主张与已公开旧论文题摘一致，没有找到独立新增设计/修订事件，贡献前关闭本次传播。不写“已审重复”：root定点Books与九/十月Report未命中该family，旧论文未建立有效采用链路。仅把原论文列本日报§5窗外恢复线索，不扩本窗全文/Books。若非作者发现Blog实际披露旧论文未有的长期机制，则只重开这一个事件并先核公开时间。

非作者决定性补核：[精确v4 HTML](https://arxiv.org/html/2609.31494v4) §3.1 ExternalHandle已写runtime sideload、client-encrypted/runtime-unencrypted数据、受控匿名结果与recovery；§3.3.1 Trust Chain已写公开program、root/worker hash及sideload proprietary logic仍由审计其使用方式保证DP。这支持Blog动态sideload不是独立首次披露，只用于本次事件关闭；未完成或声称完整论文Evidence/Books审阅。

## A2 Anthropic 培训公告

实际原源：[Claude Frontier Academy](https://www.anthropic.com/news/claude-frontier-academy)，显示 Oct 2, 2026，未核时区/时刻。
已读公告核心：资金与工程师培养目标、模拟企业部署→12周residency→实操考核和认证、首批合作机构、提名参加条件及合作网络。没有披露模型架构、训练算法或新执行/安全保证机制。
拟处置：贡献前关闭培训与合作事件。课程中有security review/handover词汇不构成项目增量；无纠错/撤回信号。无须再核不影响处置的精确日期。

## A3 arXiv窗口而非提交日

[官方availability](https://info.arxiv.org/help/availability.html)正文说明Sunday–Thursday20:00 Eastern公告，Friday/Saturday无公告；新稿、替换、withdrawal、cross-list均在公告流程。Thu10/01 20:00EDT = Fri10/02 08:00北京时间，早于本窗起点；下一正常公告Sun10/04 20:00EDT = Mon10/05 08:00北京时间，在窗外。
cs.CL /new实际显示Friday, 2 October 2026；各recent当前可见Friday2 October header。本窗无常规arXiv批次这一窄判断，不意味着作者其他原站没有新公开，不把旧标题线索变成本日题摘/全文工作队列。
本日主题API查询为submittedDate 202610010000～202610022359，仅查漏/日期代理核验，不可替代公告；第1、2、4组查询HTTP200，分别totalResults87（仅start0/max50）、6（0/50）、46（0/50）；第3组Agent/RAG/Memory查询15秒timeout、HTTP000。返回可见最新submitted字段10/01，未据此分配本日候选。未翻旧窗87项的下一页，因为官方公告窗口已排除本日正常事件；不声称87条均题摘关闭。

## A4 修订/安全负侧与旧日期

- [kimi-code Releases](https://github.com/MoonshotAI/kimi-code/releases)：latest2.1.1，release原值24 Sep07:24，资产显式2026-09-24T07:44:51Z；2.1.0为23 Sep12:31。2.1.0包括symlink/workspace trust/background git约束，2.1.1回滚部分defensive变化。它们窗外，组织Updated Oct2不是Release时间，不把“fix/revert”标签冒充10/02重要修订。这里只核当前页面的轻量安全说明，不审所有PR。
- [MiMo工具调用重复复盘](https://mimo.xiaomi.com/zh/blog/mimo-v2-6-tool-call-repetition)：浏览器实际打开，原页显示2026年9月27日；正文发布更新为9/25 06:00UTC+8，不属于本窗。此项有具体纠错/奖励盲区信号，不能以“仅harness组合”理由排除机制，只按明确窗外停止。本轮未作其必要Evidence/Books审阅。
- [DeepSeek V4.1 Flash](https://www.deepseek.com/news/deepseek-v4-1-flash/)原页2026年9月10日，窗外；不重复研究参数/缓存宣传。

## A5 Meta有限题摘负侧

实际从[Meta Publications首屏](https://ai.meta.com/results/?content_types%5B0%5D=publication)发现六条October02日期的数学题目，在September24 MaD-RL前停止；不是Meta全年队列，不宣称所有Meta原站没有新发布。以下四项标题范围关闭；root另从下列两实际原页的Related Publications列表核对完整身份，不读无关附件：

- On Solvable Evolution Algebras and a Conjecture by García-Martínez and Pérez-Rodríguez：演化代数的可解性与具名猜想，标题未建立模型学习/表示或系统机制关系。
- String Two-Point Function = Height Function on a Curve：String两点函数与曲线高度函数的关系，标题未提供多模态表示/生成模型机制。
- Semiabelian Groups Need Not Be Monomial：半阿贝尔群单项式性质的数学反例，未指向本项目模型/训练/执行约束。
- Finite-Time Blow-Up of Radial Negative-Energy Solutions for the Mass-Critical Biharmonic Nonlinear Schrödinger Equation：特定偏微分方程解的有限时爆破，未建立学习/优化理论或模型系统命题。

另两条相近题目实际打开完整摘要：

- [The Strict Threshold for Gaussian Ellipsoid Fitting](https://ai.meta.com/research/publications/the-strict-threshold-for-gaussian-ellipsoid-fitting/)：iid高斯向量，找PSD矩阵S满足所有二次型等式，阈值n/d²=1/4上下两侧可行/不可行、临界点不作结论。原摘要没有模型学习/表示机制，不能把纯随机几何可行阈值外推为LLM容量/泛化判断；拟贡献前关闭。
- [Tightness of the Cycle-Based Relaxation for Completed Length-Three Alpha-Cycles](https://ai.meta.com/research/publications/tightness-of-the-cycle-based-relaxation-for-completed-length-three-alpha-cycles/)：binary polynomial optimization特定三超边cycle的relaxation恰等于multilinear polytope iff三个差交集各为单点；slice-wise gluing与四变量parity obstruction。原摘要未建立模型训练/编译/通信约束，不能只因含optimization/AI use而准入；拟贡献前关闭。
两条没有撤回/纠错/安全事件说明，不把研究中的AI Use声明理解为模型训练新贡献。Oct02原日期未核时区/精确时刻，但明确贡献关闭无需继续日期材料请求。非作者定点核范围由root记录。

## A6 Seed无日期首页卡片恢复

[SeedRealtime原页](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction?view_from=content_recommend)实际显示2026-08-05；首页无日期卡片不意味着本窗新材料。本轮只恢复身份日期，未声称机制/实验审阅。Publications首屏第1/13页共20可见项，最新8/18，停止，不展开242项旧库。
