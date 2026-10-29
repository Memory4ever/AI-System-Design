# 02449 HLL：标准必要、拟五分与具体已有覆盖

仅2026-06-03补Jun02；当前AGENTS/研究与Report合同、Sources使用/Daily/arxiv恢复、统一入口、ROADMAP和当日停点已恢复。R62完整题摘、准入和联合Jun02日证复用，不第三日期。当前[官方abs](https://arxiv.org/abs/2606.02449)实际只有v1，所见无撤回/纠错；v1提交Jun01 16:20:45Z不是直接公开日。只读作者受控benchmark，不操作真实CAPTCHA、运行solver、访问protected服务或核代码。

## 实际证据与边界

实际读[exact-v1 HTML](https://arxiv.org/html/2606.02449v1)§3.1–3.4/4.1–4.4、T1–4、A.4完整、B.1/B.5；先前web长输出截断后以原HTML正文定点补全A.4/B.1/B.5，不冒读全部27页/图像素。必要支持与直接反侧足后停止。

十类任务的难度、页面干扰和动态检查是不同轴，不是三十三种新任务。动态仅八类，静态答案匹配后还需家族专用的可观察trace/committed-state检查。A.4区分拖动连续性、相对目标点击偏移、重复错循环和单步状态合法性，另把答案—最终状态一致性视为辅助benchmark检查，不冒生产防bot机制。检查是作者定义的接受集合；规则认定不合格不能直接推出不具人类能力，规则通过也不认证真人、授权或真实网站安全。过于规整的偏移被拒尤其体现规范与一般任务成功并不等价；本文没有给这些heuristic相对真实人类的完整false-positive/false-negative校准。

八模型同闭环GUI harness，但B.1是分批采样，不披露每批完整step/attempt/sample数；只明确1200秒timeout。硬件、模型完整revision、precision、输入输出/token预算、完整费用/重复区间均未闭，不补。T4以同八个动态支持家族的静态均值比较，不能借T1十类平均作同分母下降；Qwen-Max动态2.5反高于静态0.7，不能照录所有模型均降。T2 GPT-5.4/两弱模型部分平均亦持平或略升，不采所有干扰必然降分。该设计支持结果分数与指定过程规则分数分账，不证明改变scorer本身导致模型能力变化；不同运行/任务实例还不能当同一trace重评分的唯一因果。采样/模拟、渲染/截图、每轮模型调用、遥测、各规则校准与独立真实任务回归全计费。

## 评分与实际章节比较

拟Design Delta2 + System Reach1 + Durability2 = 5。计具体终态正确与过程接受集合的测量差额及边界，不给CAPTCHA题名、榜单、成熟GUI链或“human-like”口号加分；没有新执行算法或跨生命周期机制，不把旧准入提分当已定。标准必要足以支持这一窄命题。

实际完整读Ch78 Tool Contract/动作粒度与Evaluation分项及其Ch66交接：它拥有工具执行责任而非本研究的scorer接受集合。实际Ch66“过程指令”完整binding组（2605.01771）已明确真实工具trace/环境effect、process compliance与outcome分账、受控环境与替代合法路径/false reject的取舍；其后AuditKIT整段具体要求先固定turn/依赖/允许替代路径，再分开匹配、终态和证据可见性，不可观察非no-call。随后Procedure-Aware完整段（2603.03116）又明确冻结合法状态转换、各scorer接受集合及stop/confirmation后的执行机会，保oracle冲突trace与人工逐步核对，不以proxy失败等同任务失败。前后组完整读，不只搜主题/marker。

这些具体正文已经承载本项可支持的长期判断：终态命中不足以证明声明的过程，过程规则也需独立审计且不能取得真实授权/身份真值。HLL的几种family-specific启发式/局部模型表没有支持必须新增的通用执行或发布选择，不能为了新benchmark再追加同义段。拟唯一owner改为`PLATFORM-EVALUATION-SYSTEM`/[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，不是原初筛的泛Tool路由；Ch78仍负责工具动作接口，Ch65集群调度/Ch67监控各不接管评价定义。

拟**已有覆盖**，无Book/PRE/本人注/POST请求。若后有新可比人类校准、规则false-reject或真实服务迁移反证改变上述acceptance-set判断，只恢复该命题；不将当前未披露配置扩成无限附件请求。当前首次必要/正式分及实际具体覆盖待非writer独核，不预通过/I/DAY，Report/State/index未改，不stage/commit/push。

## root采用

R168独立标准必要/正式五分及actual Ch66具体已有覆盖通过，已融Report§3/4/5/6，未改Books/注，不授日级验收。
