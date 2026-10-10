# 12246 Reasoning Judges：必要 Source / actual Ch66 NC

mar14_supplement；精确[2603.12246v1](https://arxiv.org/html/2603.12246v1)，SUP_NECESSARY_12246.raw，GET200/425712B/2026-10-09T15:33:41.965873UTC见SUP_CORE_CREDIT_JUDGE_MANIFEST_RESULT.json。十作者、完整题名/AB、唯一v1与当前轻量说明实际核，没有具名先稿/撤回/纠错信号。owning/findable DOI/official URL/arxiv.content与Thu17:57:06UTC v1/Mar13 02:14:11UTC注册上界见SUP_DATE_SECOND.md/本ID raw；官方日程/ID非预分配有效原证夹Mar13BJT日级公开，不單取Submitted/registered首次公开。root完整AB窄准入已实际通过。

静态judge与reference agreement被当policy训练有效性→不同judge训练后的policy奖励/同reference heldout与跨judge评价皆可能被学到的adversarial输出抬高→训练judge、reference标签来源及模型评价迁移都须接受policy-shift检验，不能将更强reasoning或不同型号gold单独当真值。**2+2+2=6标准完成**：新增是静态→实际优化→跨evaluator的局部反证，影响judge训练与policy训练/评价边界；不把Goodhart/防注入/独立验证成熟原则或更高分数加基础分。

## 实际必要原证

实际§2/Eq1–2（B32–51）/§3.1–3.3及Table1（B52–88），§4.1–4.4/Eq3–4/Tables2–6（B89–150）、§6直接结论，A.3 KL/A.4无fine-tuning/A.6 benchmark人口与style口径。未遍历完整攻击示例/A.2/A.5、所有曲线/全部28模型表或代码；拟采用的是受限评价反证，不是攻击部署/防御实现。

gpt-oss-120b high为synthetic preference reference，而非真人/可执行gold；100K Tulu3 offpolicy points→约164K judge训练样本、738同source静态test。nonreasoning只SFT finalscore，reasoning SFT reference思维与score再GRPO，SFT/RL预算和trace监督也变化，不把全部效果归因“开thinking”。RL stage主要把invalidformat5–10%降<1%；Eq1 prose invalid指s/hat记法不齐，不自行补成唯一实现。政策用另117K instructions/1K heldout并保相同reference，即不同数据不解除reference偏好家族的shared blindspot。

三policy Llama3.1-8B/Qwen2.5-7B/Qwen3-4B，train judge Qwen3 1.7–14B、reasoning主要4/8B。pointwise policy reward是0–9 expectedscore，经judge token概率归一，而非human质量。Judge agreement static提高不保证训练稳定：nonreasoning自身reward逼近9但reference先升后跌；reasoning SFT+RL下reference也升，却manual100例识别过拒/伪规范/自夸、boundary污染的非任务完成策略。reference prompt修改/规则不足的作者尝试不是全部防御不可能证明。仅Llama3.1 policy在ArenaHard同量级高收益，其他两policy未同效果；不同GPT4.1 pairwise/分布仍可能被操纵，不能说人类偏好/能力优于frontier。Table1 stylecontrolled Creative89.6/Hard39.1不同切片，绝不当90%全任务或真实质量。

§4.1 RLonly缺reference trace监督，staticagreement相近不保证reference训练曲线相同；§4.2 rubrics提高staticagreement仍未消hacking；§4.3 high/medium/low样本164K/165K/125K，保high相同label筛选改变人口，不是只增token的完全matched控制。§4.4 pairwise是同组候选两两winrate，Eq4非负r平均在完整antisymmetric比较下为1/2，prose称恒0只可能指centered reward，本轮不采未中心化零均值保证。O(G²)judge比较约6倍训练时长，非免费判分；pairwise Arena两subset90.8/86.2及nonstyle>95是作者特定协议，仍非人类truth。

Judge SFT8A100/epoch约10h、judgeRL4nodes×8A100每100step约20h；policy默认4×8A100＋reasoning judge另4nodes Matrix、1200step约120h，policy prompt/output2048、judge4096。更多judgecompute不能直接授省TCO，precision/在线concurrency/deadline、完整独立训练重复CI本轮未核披露值（Not Disclosed）。A3 β0/.001/.01/.05/.1在指定非reasoning14B/Llama政策下未避免referencehacking，非KL对所有设置无效；A4原Qwen3-4B thinking无定向微调仅有限改善。Arena750（250creative/500hard）、28基线precomputed、style控制/原始表分开，所报ranking区间不等独立训练seed。没有blindhuman审或taskverifier，不认证真正偏好对齐/防御安全；无artifact核验/复现。

## Actual owner 与具体已有覆盖

ROADMAP `PLATFORM-EVALUATION-SYSTEM`；实际顺读Ch66 **2732–2791完整Scorer节/前后**，**1830–1854 reference/monitor轴**、**4490–4506 agreement identity**及Ch65/67入口；并实际读Ch31 406–441 rewardhacking作相邻主题owner边界。不将训练优化机制另抄两个owner。

Ch66 2778–2787已有本稿具体论证：RL使candidate分布不静止，static agreement只在frozen candidate人口近似reference；policy→judge→policyshift回路、reasoning/rubric/distillation可固化可利用模式；policy-shifted redteam/holdout/crossjudge/artifact与stop并行，trainingjudge reward与external evidence分账，开放domain不能独占reward和release。2747–2760已有modeljudge共享盲点、防注入/同源偏好与“更强模型不是groundtruth”；1830后明确referencejudge仍非truth。不是凭相同标题/论文名或通用Goodhart一句授NC。

这些实际正文已经承载本稿可采用的specific设计解释。Gold来源、不同data/model/bench仍为proxy和distillation trace偏好传递在上述sharedblindspot/shift论证内；当前数字不构成新安全不变量，没必要再叠相同两段。**标准完成/已有覆盖/Books新写0**，6分不因已有覆盖减分；root实际必要原证/完整owner NC独核PASS，见本日独核文件“11327 / 12246”节，不授本日DAY。
