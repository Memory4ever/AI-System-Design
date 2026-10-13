# CRAFT17305：必要原证与受限采用提案

root 按本日作者明确分工准备；仅03-20补03-19自然日，原batch5题摘准入与日期夹证复用，不扩query。尚未非准备者裁定，不写Books或计safe/DAY。

## 身份、评分与必要审阅

[exact-v1](https://arxiv.org/abs/2603.17305v1)、[HTML](https://arxiv.org/html/2603.17305v1)；本批具名DataCite created03-19T02:29:00Z/registered01Z仅与既有availability共同支持日级归属，不把Submitted、HTML生成日期或ICML2026字段当first-public。当前官方身份无已见具体撤回/纠错信号，AB未变，不扩完整版本差分。原2+2+2=6，准入命题是只评最终回答不足以解释训练中的表示代理与文本判分不一致，需核latent/text联合监督的控制责任。必要中心理论与实验反侧定点深入，不用审阅费时改分。

实际必要HTML §3–5：三prototype/projector、contrastive/calibration损失、几何/文本/一致性reward及Theorem5.1假设；§6完整T1–3和§7/Impact；Appendix B全部直接证明、C全部系统/解码配置。未核全部额外图、代码、复现或后续版本，停止于采用命题与直接反侧已足。

- 取最后一个reasoning token的hidden state，经projection/归一化得到z；safe/unsafe/rethink三prototype用EMA。样本增强、triplet、instance contrastive及rethink anchor训练可分表示，BCE标签0/0.5/1并用KL对齐文本判分。z不是整条隐推理的忠实记录，prototype距离不是安全真值；PCA簇分离也不认证因果。
- 几何reward为正safe cosine、负unsafe cosine和正rethink cosine组合；文本reward为2P(safe|final)-1，固定StrongReject判分；一致性为1-|p_z-p_y|。两者同错同不安全也能得到最大一致性。三项正权总reward不是硬安全约束，额外学习head能改变测量本身。
- Theorem5.1要求Lipschitz projection/head、输出分布不变的局部latent可控扰动和局部最优收敛。正文“改变至多ε”本身不保证沿缩小gap方向可动；Appendix B另直接断言存在改善gap的扰动，不能只由连续性推得。证明只保存R_txt、提高R_cons便宣称R_total提高，却没有控制R_geo下降。即便一致性增加0.01，几何分减少0.02且同权，总reward仍下降；这是对所写推导的缺条件反例，不是对作者实验的复现。因而不采用排尽superficialalignment/局部最优必然无gap、熵/方差普遍控制或真实内部安全保证。需要方向可控及完整加权目标变化条件才重开理论保证。
- T1所测DeepSeek-R1-Distill-Llama-8B/Qwen3-4B-Thinking-2507在JBB100/StrongReject下评reasoning文本和final内容，二者与latent safety head不是同一测量。CRAFT不全胜：DeepSeek reasoning列有IPO更低，QwenStrongRejectfinal亦有IPO更低；SafeKey的部分JBBfinal更低。三seed作者报告平均，方差被作者省略，不授独立审计/泛化安全。
- T2多个任务平均改善不抹掉单项反退，QwenMATH500等低于base或其他baseline。T3完整配方人口/值与T1同模型列不直接相同，原文没有完整对应解释；消融同时改变representation/奖励，不授相互独立因果、精确宣传降幅或零能力代价。
- Appendix C披露4×H10080GB、Xeon6338、PyTorch/Transformers、默认systemprompt及temperature0.6/top-p0.95/max31000；不能因此填造各训练baseline预算全匹配、精度、并发或服务SLO。2500 harmful样本及benign训练、增强/head/prototype、verifier/训练、长轨迹和独立回归均付费，完整端到端成本未披露。固定judge错误与OOD安全/benign效用仍需独立验收。

## actual唯一owner与差额

actual `TRAIN-GRPO` Ch33完整60–88已有无外部标签的末token latent簇reward及一致性不是真值；Ch31 150–177拥有safety/helpfulness偏好数据与软判分不等硬gate。新的受限差额是**显式安全标签下的三prototype表示监督，与终局judge联合进GRPO reward**，不是重写Ch31偏好权衡或声明hidden知道真理。以下两段拟接Ch33既有latent-GRPO代价/回退段后、另一探索分支前；已完整actual读局部，不以rg命中代替阅读。

## 两段literal PRE（提案，非准备者可裁中心隔离）

无标签的组内表示一致性之外，有安全标签时还能显式训练另一份读出：取最后一个reasoning token的hidden state，经projection得到归一化表示，以safe、unsafe和rethink三个prototype作contrastive监督，再用安全标签及终局文本judge校准一个表示分数。随后把prototype几何reward、最终回答的文本reward与两路分数的一致性共同加入GRPO。这里改变的是学习信号与测量接口，不是读出了全部内部推理；prototype接近、head自报安全与最终回答通过judge仍是三种不同证据。<!-- source-family:SF-2026-ARXIV-2603-17305 -->

一致性项1−|p_z−p_y|在两路同错时也可最大，复合reward各项又可能竞争；只改善一致性、保持文本不变，不能在未控制几何项时推出总目标改善或消除表面安全。[受限联合训练对照](https://arxiv.org/html/2603.17305v1)支持这一可试的监督分支，不授权局部最优必然安全、latent忠实或所有任务无损，部分baseline与能力切片仍更好。额外标签、增强、head/prototype、文本判分、长轨迹与训练都有成本；测量失准、OOD gap或benign效用回归时，保留可靠outcome-GRPO、独立安全评价和确定性执行gate，不把学习head和一致性奖励交给部署安全签字。<!-- source-family:SF-2026-ARXIV-2603-17305 -->

静态注提案：`SF-2026-ARXIV-2603-17305`：[CRAFT exact-v1](https://arxiv.org/html/2603.17305v1)，§3–6、直接限制、Appendix B/C必要审阅；仅安全标签驱动的三prototype/head、文本/几何/一致性复合reward分责。不采用局部可控到全加权改善的缺条件推论、hidden忠实/安全保证、全能力无损或生产成本；未核代码/复现。

若非准备者认为上述construction与中心安全保证不可分，应保6分中心争议终态隔离，不降分/EX或虚NC；保原必要证据及定点重开条件。即便采用两段，也必须在Report显式隔离理论强claim，不能以实际整合洗成理论通过。

## 非准备者有限 Source/actualowner/两 PRE 裁定

resume_mar17仅本20独立上下文，实际exact-v1 §3–5（90–186）、§6/T1–3与直接限制（187–256）、B完整273–291及C292–294，实际Ch33完整60–93、Ch31 150–177与Ch32/34入口顺读；原两literalPRE及静态注逐字回对，有限Source/actualsole差额/PRE PASS，保6分。可分采的是显式标签下的prototype/head监督→几何/文本/一致性共同reward构造；其存在不依赖Theorem5.1成立。既有Latent-GRPO只无标签组中心，不授此监督构造NC。未授Books写锁、actualPOST、safe/DAY。

独算p_z=p_y=0时Rcons=1仍是共同不安全；正权不成硬安全约束。B278把‘至多ε可控’增强为朝gap改善的方向，又由Rtxt不变与Rcons升直接断言总reward升，未控制Rls：同权Δcons=.01/Δgeo=−.02使总变−.01，root反证成立。持续隔离强理论、真实内部安全、faithfulness与所有能力保持，不能将有限construction整合记成理论通过。T1 IPO DeepSeek两reasoning切片与QwenStrongReject final更低，SafeKey部分final更低；T2 QwenMATH.924<base.952；T3完整行与T1人口不齐，variance虽称≤.2%但数值省略、三seed均不代替独立审计。C硬件/解码与全budget未匹配边界正确。一次理论重开条件为方向可控及全部加权项变化/ε界推导，评价强claim需独立latent/输出安全真值与matched全费，不另重复材料请求。

literal两PRE不采用缺条件推论，反证和安全fallback近文，拟Ch33无标签latent段完整代价/回退后位置成立。必要支持及直接反侧已够此有限采用即停止；不扩图像prompt、代码、全部附件或旧版本。root若窄写，非writer实际完整局部/静态注POST后才归并I。

## 实际窄写与本人回读

root 在独立 Source/两PRE 通过后 sole Ch33 写入原两段，当前74/76，静态注3224；完整65–84与末注回读，局部diffcheck无输出。原PowerFlow段因patch一字误写已恢复为原“与”，不存在其他既有段改义。未宣独立POST或safe；请resume_mar17实际检查正文、相邻论证和本人末注，不把构造采纳解释为理论证明通过。

## 非 writer 实际 POST

resume_mar17 恢复仅本20合同/停点后，实际完整 Ch33 60–96（新74/76及无标签latent、PowerFlow、同prompt分组两侧）与3213–3224本人/InfoDensity/TRiMS等邻注顺读，逐字回有效两literal PRE和已核必要原证，有限 actual POST PASS。显式标签三prototype/head与终局文本/几何/一致性reward分采，缺条件方向可控与完整加权改善的理论桥、同错一致性、latent忠实/安全和全能力保持仍明确不采用；反退、费用与原outcome/独立安全gate回退近文，未以有限整合洗成理论通过。原PowerFlow“与”保留，既有无标签分支及分组交接自然，本family仅两正文及静态注；scoped diff-check无输出。不改Books验收身份、不授本日DAY；可由root接纳并释放本family窄锁。
