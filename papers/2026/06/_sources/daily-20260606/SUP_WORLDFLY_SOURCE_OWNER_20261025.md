# WorldFly 2606.06147v1 — 必要证据与owner拟稿

作者 `supp_20260606_author`，2026-10-25。精确[原HTML](https://arxiv.org/html/2606.06147v1)、[本地去标签原件](SUP_WORLDFLY_HTML_20261025.md)、[精确官方DOI原件](SUP_FIRST_DATACITE_20261025.md)。日期/首次完整题摘见[作者A3](SUP_AUTHOR_20261025.md)；只Jun05 BJT公告资格，不宣称全球首公开。当前abs无撤回/纠错标记。

## 必要Source（未独核）

实际读§3–7、A/B必要域。贡献理由不变：reactive历史条件在急转/遮挡下受限，双分支video/action条件联合去噪提供替代设计；拟分 `2+2+2=6`，标准审阅；具体长期界限需Books判断。§4.1/4.3区分干净历史、未来video latent与8维action chunk；共享flow timestep只对齐加噪求解进度，不能等同真实控制时间。双向cross-attention连接两分支；连续action先floor匹配十个primitive，无效则stop，不是完整安全shield。

§3/5/A：AirSim >4000条轨迹、Easy/Hard各100，Hard为14个未见intersection；三模型同split、三历史帧、40Ksteps/globalbatch128/4A100，但LR不同、OpenFly chunk1 vs WorldFly/Pi0 chunk4。后两50denoise，实际只执行首action再观测；T1仅支持这个有限模拟protocol。T2无DB同训练支持coupling的局部增量，不证明独立future因果贡献/真实飞行安全。原文字55pp/56pp却称后者更moderate，不采用这一衰减强解释。

§6.1单A100/CUDA-event/action-only/50step报7.81s与约0.5Hz口径不相容，不采控制Hz或实时宣称；不是端到端延迟。精度、并发、尾延迟与SLO Not Disclosed，TP不适用该单GPU测量。§6.2长路线仍明显退步；T3影像fidelity不是policy安全。没有运行代码/复现/实机验证。付费边界含视频/动作训练、两分支50步、感知/codec与实际controller，不能只计小action维度。

## Owner实际比较（未独核）

已读ROADMAP、PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE；Ch25开篇/transition分责，Ch26当前World-action model完整相关段、Future-to-Action首组及Latency/末交接，Ch27开头确认训练数据owner不接动作授权。唯一owner为 `MULTIMODAL-EMBODIED-VLA` Ch26。

Ch26既有World-action model开篇承载joint video/action与相关错误；Future-to-Action明确同policy干预和重训消融不同；Latency段禁止局部延迟代完整deadline。不能把这些成熟约束借来抬高分数或说成WorldFly独有。窄delta：现有异步视频/动作时间表前，还没有把“同一个flow噪声时钟只同步求解、并不交付物理控制同步”连到连续proposal→离散primitive→无效stop的授权边界。拟在现有异步时间表首段之前补一段，不另加论文小节。

## 逐字PRE（尚未批准/未写Books）

共享求解时钟也不等于共享物理控制时钟：两条独立video/action分支可对未来目标使用同一flow timestep，再以双向cross-attention交换条件；历史观测仍保持clean，不应随生成未来一起改写。[受限UAV模拟分支](https://arxiv.org/html/2606.06147v1#S4)把连续动作离散到primitive白名单，无效编码回stop，但这只定义proposal的解码退路，不证明碰撞、接触或deadline已验收。同预算重训去耦合的改善也不等同固定policy下future的独立因果使用；两路去噪、感知与控制都付费，局部耗时和频率口径未齐时不签实时能力。求解、动作支持或反馈失配时，保留reactive policy、短chunk真实重观测与独立controller，而不让联合生成或stop标签批准物理安全。<!-- source-family:SF-2026-ARXIV-2606-06147 -->

本人注拟稿：`SF-2026-ARXIV-2606-06147` — Daily2026-06-06补Jun05，作者supp_20260606_author；exact-v1 §3–7/A–B必要，拟2+2+2=6/唯一Ch26。仅共享flow求解时间与primitive解码/物理授权分责；保局部模拟、重训消融非固定policy因果、7.81s/0.5Hz口径冲突与长程退步/完整费用，不采实时安全或净收益。未运行代码/真机或复现。必要/PRE/实际保存/唯一POST仅按后到事实记，不预I/DAY。

当前：待唯一reader准入/必要/分数/owner/逐字PRE；其后root重新fresh窄位授权才可保存。未锁章、未改Books。
