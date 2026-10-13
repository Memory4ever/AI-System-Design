# PEFT-DINOv3 17782：少标签容量与评价人口的必要证据 / 最小PRE准备

准备者resume_review17_18，2026-10-12，仅03-20补03-19自然日。由author明确分配sole必要准备，原2+1+2=5/day准入复用本日独核§30与SUP_FINITE_TAIL_SCREENING，actual读取exact DOI身份/03-19 registered原字段；不改分数或日期。未自授Source/PRE PASS，未写Books/Report/LS；交resume_mar17非准备者裁。支持与关键反侧已够，未读代码、数据仓库、相关旧论文或全部附件。

## 1. 实际必要原证 / 停止

- [exact-v1 HTML](https://arxiv.org/html/2603.17782v1)：完整AB、§2.1–2.5 L134–221，§3.1–3.5/T2–8 L222–322，§4.1–4.6 L323–365及S1/TablesS1–S3仅rank/dropout/quantization与预算必要字段L383–447。只正文/表/caption，不冒图像视觉或训练曲线重建；未读S2以后不影响有限命题的资料。
- [current abs](https://arxiv.org/abs/2603.17782) L8–28实际同题/四作者/完整AB/v1 history，无具体撤回或重要修订说明，不展开版本diff。Submitted日期不作为公开日；已有本日day夹证按身份复用。
- 本材料使用DINOv3视觉分类，不为所有语言模型/小数据任务或未知farm给出规则；农业应用数字本身不加分，拟采用的是容量与独立评价人口的受限反证边界。

## 2. 可以提出的命题与必须保留的反侧

QLoRA在冻结NF4/double-quant基座上训练adapter，FP16 compute/AMP，80epoch上限、batch4×accum8、同学习率、validation早停、seed42。q_proj与all-linear是不同target-module集合；all-linear包括Q/K/V/O和MLP，不能把跨集合收益全归rank。同all-linear内r16→64的测试准确率80.40→83.16，是继续保留较宽容量候选的局部证据；并不证明rank64最优、所有任务underfit或同budget因果。

直接反侧：DoRA同q_proj r8→16从81.53降到81.03，all-linear r16为81.23，故AB/§4.3的“容量增大一致改善”不能推广到所有PEFT。QLoRA q8和q16不仅rank不同，S1 Q2 dropout=.10但§2.3统一称.05/Q1为.05；不能当完全matched单rank效应。Q2→Q3还同时改变module与rank，主文3.23pp不是模块唯一贡献。同架构/同程序同预算重复运行或CI未给（固定seed42），保留单配置报告性质。

训练/validation是2700人工审核图中的2160/540，transition frames被剔除，validation随机抽取；test是原未筛两source 211800图。98:1只是数量比，不能认证独立动物/farm/video/time split、无重叠或域外泛化。方法§2.1有意variance selection、§4.6又称未targeted sampling，数据选择责任不靠文字统一。两source均作为训练候选来源，分source测试不等leave-one-source-out；实际未验独立新farm。验证集较干净与test含歧义/错标签的差距不等训练过拟合，更不反向证明underfit唯一根因。

§4.2针对频繁混淆类人工审200测试图，32%标签不符、60%单图含糊、8%真错只是该定点样本，不外推全部测试真实accuracy；不把模型预测优先于标签或审后解释当独立groundtruth。T7 lying+standing占约72.4%，Walking F1 .26/precision .17，Gallop recall .50低于frozen .55；aggregate不是各类能力保证。真实跨source/动物/时间闭合仍需要精确split身份。

计费：baseline模型/epoch/learning-rate、训练batch与FP16/NF4/quantized基座改变，不以训练总小时证明算法统一加速。§2.5说inference batch32、T8 caption说64，latency列为全测试时间除图数的摊销ms/image，不是请求wall latency/strict deadline；并发、真实SLO、全搜索/人工标注与预训练费用Not Disclosed。DoRA大配置实测推理吞吐较低，少trainable state不等更快运行。分类head4.7M与PEFT参数表的scope须分账，不照录“仅2.72%全trainable”或部署VRAM保证。PlayBehavior未公开不阻塞论文有限命题，但未声称实现/复现。

精确请求只供强主张重开：同配置seed/预算控制，动物/farm/video/time及train/val/test排除字段、测试标注的独立审核；同时说明adapter/head参数口径与batch计时单位。该请求不将可支持的有限容量选择冻结为中心hold，也不预计取得内容。

## 3. actual sole owner / 最小差额

唯一`TRAIN-LORA`，[Ch30](../../../../../books/part-04-training-system/30-lora.md)。实际Ch30 223–325：rank/target选择、任务维度、监督歧义、条件rank、Rank Threshold绑定loss/base/feature/evaluation；320–425中的placement与high-rank runtime已读。相邻Ch29/31入口已读，SFT监督资格归29/Evaluation，不把视觉classifier教程复制过去。已有主题覆盖并不自动NC；拟差额只少标签下容量缩减的受限反例，以及curated validation→uncurated test gap不能诊断underfit/overfit的具体混杂。

拟在原rank不等任务本质维度完整段（当前237）后、value-only ICL段之前两短段。现owner允许局部经验边界，不创建新章、不复制QLoRA/DoRA算法或农业任务流程。若非准备者认为当前具体正文已完整承载此差额，可裁具体NC，不为制造diff保两段；未授锁不得写。

## 4. 待非准备者裁的逐字PRE / 静态源注

少量标签也不能单独决定 adapter 必须更窄：冻结基座与下游任务之间仍可能需要较宽的更新空间。可先分开固定 target modules 的 rank 对照，以及固定 rank 的 module 对照，而不是把两者一起增加后的收益全部归给 rank。[有限 DINOv3 分类对照](https://arxiv.org/html/2603.17782v1)中，QLoRA 在相同 all-linear 集合内提高 rank 后测试质量改善，但 DoRA 的 q_proj 小档并不随 rank 单调改善；较宽容量只能保留为待验候选，不能由标签数或这一局部排序签发通用欠拟合诊断。<!-- source-family:SF-2026-ARXIV-2603-17782 -->

容量验收还要绑定评价人口：人工筛清的 validation 与未筛的原始 test，即使后者数量远大于训练集，也不能由两者差距诊断训练过拟合或证明独立泛化。此处测试含不由单图决定的标签和类别不均衡，rank 小档另有 dropout 差异；target modules、标注与数据来源、独立动物/视频/时间切分、训练/搜索预算须分开核对。更宽 adapter、量化基座与更多可训练方向也不保证实际推理更快，整批时间除样本数不替请求延迟。质量切片、独立划分或完整成本未通过时，保留原固定配置、frozen features 与匹配预算的容量搜索，不用 aggregate accuracy 或参数比例批准新 adapter。<!-- source-family:SF-2026-ARXIV-2603-17782 -->

静态源注：

- `SF-2026-ARXIV-2603-17782` — [exact-v1](https://arxiv.org/html/2603.17782v1)必要§2–4/T2–8及S1配置反侧。仅少标签容量选择与curated-validation/uncurated-test人口的受限分账；保DoRA非单调、dropout/module混杂、标签歧义/类别切片及计时/全费用边界，不采underfit唯一因果、rank64通用最优、无重叠/跨farm保证或部署加速。未核代码、数据实例或复现。

## 5. 非准备者待核

交resume_mar17真正necessary Source/actual owner/两literal与static裁，保原5；未授Source/PRE PASS、Books锁、actualPOST或DAY。准备者不自核自身。

2026-10-12 resume_mar17 非准备者实际有限复核通过：重新加载本日合同/来源/ROADMAP及停点；exact-v1必要§2.1–2.5/T2、§3/T3–8、§4.2–4.6直接反侧与S1配置实际独读，current abs仅身份/说明复用已读。QLoRA all-linear r16→64时alpha32→128但alpha/r均2，不能冒纯rank因果或匹配总运行预算；DoRA q8→16反退、Q2 dropout.10与主文.05冲突、同两source训练并不成LOSO、curated/uncurated人口与计时batch32/64口径已实际核。第4节两literal与static逐字可有限分采，不采作者underfit唯一根因或泛化/加速保证。actual sole Ch30完整223–265及相邻Ch29/31入口实读：237 rank非本质维度后、value-only ICL前补少标签容量缩减反侧与人口混杂，现有监督歧义段不替代这个差额；唯一owner为TRAIN-LORA/Ch30，非Ch23。必要支持及关键反侧够即停止，不读S2以后、代码或数据实例。原5分/day不变，Source/actualowner/PRE有限PASS；未授写、未POST或DAY。root协调该family窄锁后才可落实。

## 6. root授权后实际writer落实（非actualPOST）

2026-10-12 root明确授resume_review17_18 sole Ch30 family窄锁。writer重读Books适用背景/学习/写作、actual正文与章末邻注后，仅逐字原两PRE写Ch30新239/241、原rank维度237后/value-only ICL243前，静态来源注写章末；保全部既有内容。实际完整225–265和末7本人/15990/HiFICL邻注顺读回原literal及有效证据一致；scoped实际两段＋静态注六新增行，原文件已有其他14新增行保留，现20新增/0删除，diffcheck0。不将writer读回称nonwriter POST；交resume_mar17一次实际正文/完整两侧/本人静态注POST后root接纳释放，不循环改身份，不改Report/LS或授DAY。


## 7. 作者非writer一次actualPOST

2026-10-12 resume_mar17实际完整Ch30 225–265（新239/241）与968–977本人/HiFICL/W2T邻注，回对第4节两literal/static及本次必要原证。目标模块/rank非本质维度→少标签容量对照与curated/test人口→value-only ICL/监督歧义/conditionalrank完整链保持；DoRA非单调/dropout、标签切片、独立切分与计时全费边界近文，不授欠拟合唯一因果/通用rank64/加速。原两PRE及静态注逐字一致、唯一family不重复；scoped diffcheck0。非writer实际POST有限PASS，告root接纳/释放Ch30；不再改静态注验收身份，不授本日DAY。
