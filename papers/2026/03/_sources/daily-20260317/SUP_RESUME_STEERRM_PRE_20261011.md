# SteerRM12795：必要Source/actual owner与逐字PRE

仅本17补03/16。resume_mar17实际[exact-v1](https://arxiv.org/html/2603.12795v1) §3.1–3.4/Eq2–8、§4.1–4.4/Tables1–4、A2/B1–2/C、D1–6/E必要原证；当前官方abs仅v1、未见给出的具体纠错或撤回，有限轻查不外推全网。2+1+2=5，RM稀疏干预的重建/功能校准差额深入，不借一般SAE原则增分；独核/PRE待做，未授锁未写、未核artifact/复现。

## 原证与反侧

500GPT4.1mini format pairs，四域各125、regex与50manualaudit只有限content保持证据；prompt也在同一non-special token平均人口，不是只response或对齐token一一差。每feature配对差均值/方差global minmax后strength/stability排名，positive mean且top10，从LlamaScope base32x postMLP-residual SAE（131072）探测0–9layers。runtime在选feature所属层对全部non-special tokens SAEencode/零相应坐标/decode，直接h′=reconstruction，不保留h−SAE(h)重建残差；special tokens不动。不能叫prompt-gated修改或当无损semantic projection。原Eq6文字variance和σ符号不采完整numeric recipe。SAE从base迁移RM先核MSE/绝对rewarddelta/L0，深层明显不匹配，不把早层feature集中=偏置只在浅层或架构唯一因果。

六Llama RM＋Gemma2B，RM-Bench四域Easy/Normal/Hard；Table1每个Normal均退，QRM/BaseRM平均也退，六Safety均退，Hard更好不认证generalcontent保持/下游RL安全。直接dense减均值baseline差，不证明所有macro不可能或SAE必需；重建单独baseline与容量/层/剂量完整控制不足，功能收益不唯一归因disentanglement。Table4同dictionary跨RM复用Skyworkfeatures，Tulu Hard33.9→62.3但Normal73.8→63.4/Average66.5→60；可共用feature身份不等可复用干预权限。Gemma使用其自有Scope/重新500pairs不是跨架构同feature直接转移。Politeness200客观math/code人为插标记只限域。

D4 N50总体退、500Hard优于1000；D5直接RM-Bench选feature与其评价不能证独立heldout迁移，未给split映射；D6K30局部峰/K50退非普遍最优；D7GPT4o-mini/Neuronpedia解释只proxy不因果语义。E披露4A80080G、几分钟probe和10–15%额外compute作者估计；500pairs×10层称5000SAEpasses未分双响应/batch口径，不当完整2victim/全文token成本。precision、长度/batch/concurrency/tailSLO与独立重复不确定性ND。SAE预训练、合成/人工审、encoder/decode/mask/heldout回归全计费，trainingfree只RM权重不更新。

## actual owner/PRE

实际Ch31 142–188 preference身份/偏置counterfactual/ObjDisco；531–566权重→conditional sparse activation map→macro/micro geometry→输出通道选层，以及Ch30/32开篇交接已读。现conditionalmap针对policy输出且保有promptgate，不含contrastive RM feature排名→baseSAE到RM重建功能校准→全replacement/crossRM资格的差额；唯一TRAIN-RLHF，不把RM感知另塞Ch17或Ch66。拟在现conditionalmap成本/回退后、macro/micro geometry前插两段，未授锁未写：

同一种稀疏干预用于Reward Model时，目标不是让policy说出某类内容，而是减小评分器对受控表面变化的响应。一条分支对词义尽量相同、仅格式不同的成对回答，比较非special-token平均SAE特征的变化，以跨样本变化强度和稳定性提出少量候选坐标；部署再将这些坐标归零后重建hidden state。配对改写和feature标签都不是真值，完整重建还会引入SAE自身的误差，而不只是减去所选方向。因此要先在具体Reward Model上分别检查重建误差、原reward变化和稀疏度，再验证格式敏感性及内容评价；从base model取得的dictionary不能自动获得新评分器的功能兼容资格。<!-- source-family:SF-2026-ARXIV-2603-12795 -->

共享dictionary和坐标也不等于共享干预权限：[SteerRM的有限跨模型对照](https://arxiv.org/html/2603.12795v1)中，同一feature集合可以改善格式混杂的Hard排名，却同时损伤Normal及平均分，部分本地设置亦退步。不能用Hard收益证明一般语义、安全或下游RL偏好已保持，更不能把一次dense方向失败写成稀疏分解必然更好。Probe合成与审核、SAE预训练/编码/重建、选层选坐标和每个目标评分器的独立内容回归都计费；漂移、误删结构信号或总费用不合算时，保留原评分器、可核偏好对、后验校准与重训分支，不让“权重不更新”替代行为验收。<!-- source-family:SF-2026-ARXIV-2603-12795 -->
