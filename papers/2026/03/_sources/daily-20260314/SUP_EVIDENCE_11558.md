# 11558 RoboClaw：必要 Source / 具体采集重置差额 / PRE

mar14_supplement；精确[2603.11558v1](https://arxiv.org/html/2603.11558v1)，实际缓存SUP_NECESSARY_11558.raw/txt及SUP_CORE_ROBO_MANIFEST_RESULT.json的200/154199B/2026-10-09T14:30:51UTC。完整题摘及当前v3可见history已读，采用仅v1；当前说明未识别具名提前正文、撤回/纠错或明确重要revision，不以晚版本号追全diff。18作者/本ID题名DOI，日级官方事件夹证见SUP_DATE_THIRD.md及11558 owning/findable/official URL/registered Mar13 01:58:19UTC原件、v1Thu05:22:59UTC和有效官方公告规则；不是Submitted或registered单独首公开。root此前实际完整题摘窄准入通过；本单项日期字段和必要Source仍待非作者实际核，不授DAY。

原人工采集须每次恢复场景、部署单技能组合易偏离初态→EAP把learned forward/reset配对并保存两条真实轨迹、部署改以forward技能恢复→采集分布部分由reset policy决定，不能把共享VLM/MCP loop或采集reset可用性当部署可恢复保证。**1+2+2=5最低标准**：EAP采集/技能更新/部署角色的局部闭环配置（非新inverse理论或独立安全gate）为Delta1；其实际改变数据人口和采集→训练→部署接口Reach2；物理reset条件/两角色边界稳定Durability2。不把通用闭环、权限、真实state验证、module数和53.7%加分。具体Ch26采集reset身份缺口触发必要深入，不自动给整稿高分。

## 实际必要原证与边界

实际§3.1–3.3（B20–72），Eq1–8、§4.1–4.4/Tables1–3/Fig4文字说明（B73–137）、§5直接限制；恢复时回读B42–137必要核心与反侧，不读引用全集、代码或完整晚版。

§3.2 forward完成由VLM/当前observation判断，然后触发learned reset，正反两条trajectory都进入D；reset是另训练policy，不是把action倒放、物理逆映射或snapshot rollback。§4.2固定每forward人类demo、inverse故意较简单，Table2 reset36/50至43/50而非100%；可能恢复失败并改变下一采样初态。Table3每轮加50trajectory，五轮forward改善同时增加数据，不能由固定human-demo预算推出固定完整data/compute机制因果。采集on-policy experience不等本稿policy-gradient/RL更新；底层π0.5 conditional flow matching/LoRA。

§3.3部署从forward集合选技能、retry/change/replan，失败再CallHuman；并非每步调用采集inverse或保证同语义/同状态。§4.4 non-degrading miss可retry，degrading瓶倒/移位落到grasp前提外须恢复；早期human干预，逐渐把恢复行为加进skill库。这个结果不提供独立可靠precondition detector、真实state恢复证明或hard safety veto实现；同VLM既调度又评完成不授独立gold。§5假设practical inverse可用、cloud model latency，navigation/mobile等future不外推。

AGIBOT G01双臂20DoF，π0.5 BF16/LoRA r16 alpha16/all-linear，10K steps/bs16/lr2.5e−5、infersteps3。四场景采集human-time baseline2.16×、intervention8.04×是ours归一化相对费用，不是完整robot/VLM/train wallclock/TCO或全部生命周期53.7%。forward Lipstick2/50→23/50、wipe11/50→26/50仍大量失败；long-horizon20trial比较same-final-dataset vanilla VLA与四独立skill SR乘积，后者非matched controller、四skill不独立亦不认证全任务乘法。重复训练CI/各role调用总费、实际硬件训练资源、并发与deadline未披露本轮可核值，Not Disclosed；无artifact核验/复现。

## Actual owner / 差额 / 两段逐字 PRE

ROADMAP `MULTIMODAL-EMBODIED-VLA`，实际顺读Ch26 637–655完整数据演进/derived provenance与人类观测采集交接、723–748完整fleet干预→离线更新→safety→canary/rollback及接管后缀；Ch25/Ch27入口实际核。现文已覆盖通用fleet loop和干预选择偏差，但没有采集用learned reset如何制造下一真实初态人口、它与部署forward-only恢复的职责差额。不是以已有主题判NC，也不新增通用Agent workflow owner。拟在derived label provenance段之后/双手机world-frame之前窄插以下两段；不动Fleet正文、其他family或末注归属。

> 真实环境的采集扩容还受“下一次从哪里开始”约束。人工重置成本较高、且任务具有可执行恢复动作时，一个分支把forward skill与另训练的reset skill配成采集循环：观测确认前者完成后调用后者，并把正、反两条真实trajectory一起保留。这里reset不是动作倒放或状态snapshot；它自己的失败会改变下一次采样初态。采集身份因此还应包含两条policy的revision、各次完成/恢复观测与human intervention，不把“成对保存”当成已回到同一物理状态。<!-- source-family:SF-2026-ARXIV-2603-11558 -->

> 这条采集分支也不自动成为部署时的撤销协议。部署可从forward技能库中retry、切换或另选恢复技能：环境未退化时原skill尚可重试，瓶子倒下或物体离开前提区域时则须先恢复可执行状态；共享VLM和工具接口不证明两个角色的初态或成功判据相同。[受限真机证据](https://arxiv.org/html/2603.11558v1)的reset只有36/50至43/50成功，forward改进伴随新增轨迹，不能认证完整匹配预算或普遍恢复。另一条policy的训练、失败重置、VLM调用与人工接管都付成本；缺实用reset、当前状态无法确认或安全边界失效时，保留人工恢复、离线示教与受限场景采集，动作提交仍服从低层controller和safety envelope。

拟整合两段，待非作者实际Source/owner/逐字PRE；必要边界够即停，不再展开后续论文版本/全部task图/代码。无本日Evidence/Books/DAY自授。

## root实际独立Source、owner与PRE：通过

root直接打开精确v1 §3.1–3.3/Eq1–8、§4.1–4.4/Tables1–3及§5，核forward/reset两真实轨迹、deployment仅forward集合的retry/change/replan/CallHuman、36/50至43/50 reset不完备、每轮增加50样本与固定human-demo并非全预算、相同最终dataset基线与四skill乘积非同controller、云端时延和实用inverse假设。只采用正文可支持的角色差额，不读无关引用或旧版、不以作者原宣传代真实安全。必要原件足够，评分1+2+2=5及限定owner缺口的深入保持。

直接读`SUP_DATE_11558.raw`精确DOI与official URL、arxiv.content/findable及Mar13 01:58:19UTC上界；沿已核官方公告规则与明确晚Wed截止的v1下界，日级夹Mar13北京时间，不将registered或Submitted独用。未识别具名提前稿与重要纠错信号，不授全外部先稿查尽。

实际顺读Ch26 635–672数据演进完整局部、708–758 continual/fleet交接，以及Ch25/27入口。原文有派生label与fleet回流，缺learned reset决定下一初态人口及采集/部署角色差额；PRE两段位于derived provenance之后、双视图采集之前，不重复fleet版本循环或引第二owner。root已实际窄写两段与本人末注，待非writer实际POST；不授本日完成。
