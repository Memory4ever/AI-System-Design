# LEAFE 16843：回退经验的监督资格与窄 PRE

作者resume_mar18，仅03-19补03/18自然日。2+2+2=6给reset/replay分支→移除经验的action示教＋成功rehearsal，不给普遍agency/capability-ceiling因果。实际[exact-v1 HTML](https://arxiv.org/html/2603.16843v1)完整題摘、§3.1–3.2/Eq1–3、§4.1–4.5/Tables1–6、A Algorithm1与B.1–B.4/Table7必要实现/对照已读；未核全部图像点、B.5图内prompt、代码或复现。current abs仅v1/Submitted to ICML2026，未见具体撤回/更正，不把标签当先公开；日级夹证复用本批有效字段。

## 必要机制与直接反側

§3周期/失败后当前policy提议rollback位置tau和自然语言诊断e；环境reset后重放原actions到tau，再仅新分支首action读e，随后普通history下继续。BFS queue在attempt预算下扩树，真实状态恢复不是删历史文字。A line11在执行新action之前即收D_refl，未以独立正确性/终态成功作统一过滤；正文“improved action/counterfactual”只是作者命名，proposal资格不是已证修复，periodic反思也可来自未失败状态。全同policy生成e/新action，非外部教师或独立根因oracle。

Stage2在原history/q不读e下，对branch首action做CE；另一rehearsal只从成功episode抽state/action。B.3随机20%成功rollout、每题3branch，batch128/LR1e−6/2–3epochs；原Lcf+betaLreh和实际union采样的精确beta/reduction、失败branch接纳完整阈值与最大depth/attemptB未充分披露，不授统一可执行recipe。成功终态不能验证所有动作最优/反思真实，原history与读取未来feedback提出e的训练信息权限必须保存；test无需e不等已经学会同一因果恢复程序。

五bench环境合同分开：ALFWorld暴露合法action候选，ScienceWorld给可用objects/模板且最多最近10turn，Sokoban文本grid、WebShop页面、CodeContests每轮整程序/最多4turn，公共测试具体反馈/private只有aggregate。此ScienceWorld只是通用文本Agent训练验证，不扩AI-for-Science领域研究。K10/5/4不同，Code最多4turn故只attempt用完触发反思；真实不确定/不可逆环境无法同样reset/replay，§4.5明确承认诊断/恢复假设。

Main LEAFE从GRPO-trained起再SFT；EarlyExp为重现IWM+GRPO非完整原artifact，ACE亦GRPO-trained+有100item限playbook。额外branch/reflection/恢复/训练费未等同GRPO，Table3固定program executions不计变长token、reflection和replay成本。训练split3553/2000/5000/5000/5000、test140/150/500/500/165，Table7 SFT10k/12k仅approxorder不是exactaccepted样本；没有统一trainseed/CI/HW/precision/exactruntime/arrival/SLO披露，未认证完整time/cost收益。

T1 pass1 WebShop Qwen66.50<GRPO67.45/ACE68.65，ALFWorld67.50<GRPO69.46/Early72.23、Llama71.79<72.50/74.15；ScienceWorldLlama22.70<24.25/25.28，不能称所有单试更好。T2 Qwen72B pass117.12<GRPO20.45但pass12847.88>36.97；摘要+14是对base33.94差13.94百分点，非对GRPO14pp。有限独立无rollback采样pass128是该population/decoder/test预算的coverage proxy，不证“无支持变有支持”或无限能力ceil；主/消融同时变训练来源和预算不能从高k唯一归因agency。T4 Qwen14B Lcf+reh pass136.50<reh37.17、pass12872>67.33；T6 EE/RL有pass128反退也有真实提升，不把outcomeRL一般写成只sharpen且不能创新。T5 MBPP有限pass128保留非所有旧能力无遗忘。

## actual sole owner

完整Ch29 507–542的textcontinuation→privilegedbranch→same-prefix contextdistillation，Ch28/30首18行交接已实际读。本19Books背景/学习法/写法当前已重载。soleTRAIN-SFT：520–522现有teacher–student divergence选token/teacherforcedbranch、student后缀与teacher分布再次蒸馏，但不承载环境reset/replay的action边界、同模型feedback经验只训练移除e后的首action及成功rehearsal分池、branchproposal未证修复的新监督资格。662–675泛部署策略contextdistill不是此树分支硬target接口，故不假NC，也不复制Agent运行控制作第二owner。拟522末branch证据后/Context Distillation标题前一段，待非preparer Source/actualowner/PRE和root新锁，未写未safe。

## 逐字一段 PRE

若环境可以可靠 reset 并重放到某个 action 边界，也可用反馈生成训练分支，而不要求 teacher 提供词表分布。一条[受限经验分支](https://arxiv.org/html/2603.16843v1)让当前模型提出回退位置与诊断经验，恢复当时环境后，仅让新分支的首个 action 额外读取该经验，再用原历史、不提供经验的条件模仿这个 action；成功 episode 的动作另作 rehearsal。这里改变的是示教来源和训练条件，不是证明反思找到了真实根因：branch 样本可以在执行和终态验证之前取得训练资格，不能仅因称为“改进”或“反事实”就认证修复成功。须联合保存环境与 replay 身份、反馈的可见时点、分支 policy、接纳规则及两池采样权重，并以无经验的新任务轨迹检查修复与遗忘。更高有限 Pass@k 只属于受测采样预算，部分 Pass@1 仍更差；反思、重放、额外分支和后续 SFT 都付费。状态无法恢复、反馈不可靠或质量与总费用回归时，保留完整 verified demonstrations、原 outcome RL、可靠教师或显式运行时恢复，不把训练期回退能力迁成部署的任意撤销权。<!-- source-family:SF-2026-ARXIV-2603-16843 -->

静态来源注：`SF-2026-ARXIV-2603-16843` — [LEAFE exact-v1](https://arxiv.org/html/2603.16843v1)必要§3–4/Tables1–6/A Algorithm1/B.1–B.4/Table7。仅reset/replay的经验条件action→移除经验示教及成功rehearsal分工；训练资格不等终态修复、Pass1反退/有限k/GRPO起点和全费用保留。不授根因、无限capability支持、统一配方、生产撤销或普遍无遗忘；未核图内全部prompt、代码/复现。
