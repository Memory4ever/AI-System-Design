# 11563 SVLL：实际增量最低评分 / 安全措辞反侧

mar14_supplement；[精确v1](https://arxiv.org/html/2603.11563v1) `SUP_NECESSARY_11563.raw`，实际200/UTC/bytes在`SUP_SVLL_MANIFEST_RESULT.json`。完整题摘校准后实际§3/Eq1–4/Alg1与§4/Tables1–2、§5直接限制全部必要段；未读参考文献所引所有方法、代码或隐藏部署实现。身份14作者/仅v1/无具名先稿或纠错说明，日级公开夹证`SUP_DATE_THIRD.md`/`SUP_DATE_11563.raw`：v1Thu05:35:29UTC、owning/findable精确DOI/URL与Mar13 01:58:26UTC上界同BJT日，下界依已核官方日程，不以Submitted/Registered单独作first-public。

## 实际新增 / 最低评分

Stage1先筛仅当前图就能定最优下一动作的样本、去history做SFT，Stage2启用history仍冻结visionencoder/fulltune剩余模型。Stage3 LoRA组合：w>1乘chosen logratio的DPO、expert sequence NLL、max(0,logπ(rejected)-τ)；label smoothing与多个权重/阈值继续存在，普通相对DPO的绝对likelihood盲区是已有成熟问题，不给它或SFT/unlikelihood原则新分。

拟**1+1+2=4、已关闭/仅报告**：实际delta是stage/samplechannel选择与已有loss的局部配置，而不是新的DPO推导、环境reference monitor、hard-constrained action support或跨系统执行接口。Reach1只限特定高层planner训练，不因VLM/robot标签或9物理任务当跨生命周期机制；Durability2为局部训练条件配置。尚未识别新长期有效界/预算可行性、具体纠错或重要机制可支持命题，不以收益数字、方法名、Book映射或深审费用抬分/撤销原窄准入。

## 必要安全反側：不将softobjective当严格约束

Eq1b声明每步a∈V(I)，但Alg1训练loss不做decoder support mask/环境authorization gate，不保证部署动作都可执行；loglikelihood τ甚至不等动作有效性阈值。Table1 Stage3 VAR89.64%、CVR26.34%，真实9任务5成功、CVR4.35%均直接反驳“strict adherence/prevent catastrophic failures”的普遍保证。原定义CVR包含重复search/未terminate等逻辑类别，不能等真实碰撞或物理unsafe概率；四类1000negative是同Stage2near-policy人口，unknown违例不因loss消失。

DirectStage2与Stage1+2训练时间/数据人口不同（每阶段约25h、第三4h/8 A10080GB），不独立证明history本身因果坏或先spatial可普适。Table1没有独立vanillaDPO、仅加SFT/UL/weight等拆分对照，所谓B-DPO修正likelihood displacement的单因素作用未隔离；absolute chosen likelihood/KL曲线、匹配data/steps/compute、SE/重复seed、精度和评估episode总数未充分披露。Realworld6DoF/九组合primitive任务不认证scope/controller/latency合同或事故率；未核artifact/复现。Expert示教噪声/次优会被强anchoring固化，作者lim承认。

已读反证完整保留，不因为4分略去安全说明；最低关闭在身份/日期/重复关系和实际delta理由上结束，不授标准正面实证或写Books。Ch34已明确relative margin≠absolute likelihood，Ch26原controller/environment verifier不受该训练prose覆盖；本项不请求新owner锁或补书。root实际必要core/原表反侧与评分理由独核后再formal，不授DAY。
