# Ch33 — POPE / PrefixRL Source / PRE（待独立确认）

Owner TRAIN-GRPO。Root现授各两段+自身note窄锁，未写。作者与peer各自已实际必要精确v1来源；scores各2+2+3=7。实际owner的group size/zero mixed-outcome/curriculum/稀有正确路径已有采样信号，但未讲“外部短prefix仅改条件，不模仿prefix而训练当前policy续写”；scaffold/correction与state-matched trajectory接纳已有provenance，但未讲correct-realizable trace条件下prefix/no-prefix objective global consistency与实践去prefix迁移反侧。恢复重读Ch33这两节/邻接及Ch32/34交接，保留现有全部内容。

## 18779v1 POPE

实际§2–6/7–8/Appendix C；Qwen3-4B-Instruct2507，128×32K筛nearzero难题，8×16K GRPO/温度.8，guided:unguided 1:1。同oracle-prefix SFT/rejection对照窄支持；LUFFY未有效跑通不算胜出。禁止backtrack干预guided↑而unguided↓仅stitching hypothesis，不证明内态原因。日期Jan26 cutoff前+finalID/schedule+Jan27deposit联合，待peer核该ID。

拟插入mixed-outcome/稀有正确轨迹两段之后、`只按reward variance选题`之前：

当整组采样长期全失败，继续扩大组或改entropy仍可能只增加没有正向信号的轨迹。一条受限分支把人工短解题prefix作为条件，随后仍由当前policy生成并验证续写；prefix不进入模仿损失，guided与原prompt的unguided rollout共同训练。这与直接把成功全文当demonstration不同：它先让当前策略从较易到达的中途状态取得成功，再检查这种学习能否返回无prefix任务。应保存prefix来源、长度、选取策略和conditional policy身份，不能仅因suffix由当前模型生成就称整个原prompt分布纯on-policy。

[POPE的必要对照](https://arxiv.org/html/2601.18779v1)在Qwen3-4B的near-zero数学题上使用1:1 guided/unguided，前置128条长rollout筛难题，再以8条续写训练；人工oracleprefix和筛选/验证均有成本。禁止回溯到prefix所述步骤的干预使guided表现提高、unguided迁移变差，只支持上下文重叠或“stitching”的行为假说，不认证内部因果；同prefix监督对照也不证明所有难题都适合这条路径，未成功运行的LUFFY不构成有效胜出比较。依赖prefix的高成功率不代签无prefix能力；缺少所需知识、prefix失真或迁移不稳时，保留明确SFT、普通outcome RL和逐难度评测，不用人工开头隐藏部署时仍需脚手架的事实。<!-- source-family:SF-2026-ARXIV-2601-18779 -->

## 18795v1 PrefixRL

实际§2–5/B1 proof/B2算法假设/D1–3，peerSOURCE通过。正确offpolicy trace、可实现deterministic μ才给prefix/no-prefix global optimum consistency，非samegradient/每步保证；B2 NPGstatewise mirror+realizable finite-Q critic/ρ=.5μ+.5π及mixture输出不覆盖实际REINFORCE/fixedcuts。Llama先OpenThoughtsV3distill，1Khard基于Llama512zero，3cuts40–80%，3:1，n8/400iter。related/unrelated和crossfamily方向反侧；D2 2ND+6ND/upfrontreject只估算compute。Fig10额外suffixinjection实现不明不采。

拟插入同节上述POPE两段后、原reward-variance交接前，连续两段以理论条件接行为迁移：

外部prefix的另一条边界是梯度属于谁：从正确的off-policy trace选定开头，屏蔽开头的loss，只对当前policy在该条件下采样的completion作reward update，并保留一定比例原prompt rollout。[PrefixRL的目标分析](https://arxiv.org/html/2601.18795v1#S3)在全部外部trace正确且policy class可实现相应deterministic成功策略时，证明存在同时最大化prefix条件与无prefix目标的global optimum；这不说明两种目标梯度相同、每步改进一致或有限训练一定找到它。另一个sample bound依赖NPG、可实现finite-Q critic、off-policy/current-policy混合行为与prefix-state覆盖及输出mixture，与实验的REINFORCE和有限固定切点并非同一算法，不能借理论替实践担保。

部署是否能去掉开头仍须单独测。受限数学实验以3:1 prefix/no-prefix、三个40–80%切点、每prompt八rollout训练，并比较相关和无关prefix；较长或跨模型prefix可能更迟迁移，Llama→Qwen也弱于相反方向。两道题的keyword策略只是行为proxy，不读出“回想被注入内态”的因果机制；Llama基线都先作同一distillation，难题人口与前置rejection采样须保存。2ND sampling加6ND update并计入rejection的FLOPs估算，不等生产wallclock或完整系统费用。无prefix质量、跨family匹配或成本不合适时，保留可早停的显式SFT、原prompt RL及固定辅助条件，不用correct trace的身份替代实际迁移验收。<!-- source-family:SF-2026-ARXIV-2601-18795 -->
