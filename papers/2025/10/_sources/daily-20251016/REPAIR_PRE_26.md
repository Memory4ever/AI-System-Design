# 第二十六包：跨checkpoint干预、统计选数与集合监督

Books/ROADMAP有效。actual Ch17完整局部Jacobian两段、PID全文、layer-redundancy两段/后替换全文；Ch21总/active预算链、固定分区risk两完整段与HuBERT下段；Ch29 demonstration likelihood/entropy两完整段与forget下段均读。Ch16/18、20/22、28/30交接有效。只消费R14/R9首次必要，不第二Methods/代码/复现；以下三处完整稿待sole整体PRE。

## 12229 Knobe / 2+1+2=5 / MODEL-TRANSFORMER-LAYER Ch17

actual owner是层间状态的干预身份，不是初始lookup；当前固定baseline/交换/拟合替换未承担同输入跨checkpoint prefix→suffix的拼接参照。插在“任何 layer-redundancy 结论都应绑定”完整段后、“若目标是替换而非直接删除”前。

正文：

干预参照也可以来自同输入的另一个checkpoint，而不是零值或固定均值：让pretrained前缀产生指定层activation，再交给finetuned后缀继续，逐层比较原模型、微调模型与拼接路径。[受限跨checkpoint对照](https://arxiv.org/html/2510.12229v1#S3)测的是这份替换对指定行为差的影响，不由差额消失定位唯一bias存储，也不能由一个intentionality标签恢复推出全部旧能力或公平性。前后模型、输入/层位、token对齐与读出协议须共同保存，跨模型状态分布失配本身也可能改变输出；80个scenario的随机温度重复不是同数量独立人类。双模型求值、activation驻留/拼接、层扫和独立旧任务回归均付费；语境、状态兼容或效用不稳时保各原checkpoint与普通干预对照，只将拼接用于有限诊断，不据其批准无损去偏、剪层或部署安全。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12229 -->`

本人末注：

- `SF-2025-ARXIV-2510-12229` — Herschel，Daily2025-10-16补Oct15；消费Cicero R14 exact-v1 §3.1–3.3/Alg1/4.1–4.3首次必要，2+1+2=5，仅跨checkpoint activation拼接的干预身份差额。actual Ch17非lookup；保局部intentionality/80scenario与283重复输出、状态失配和全费，不授唯一bias定位/全部公平或能力恢复。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

## 12744 SGMoE / 2+1+2=5 / MODEL-MOE Ch21

固定分区risk论证未承担可识别混合模型中merge path+likelihood选数、MLE与实际EM分责。插完整SF2510-03151 inline段后、HuBERT同预算分配段前。

正文：

专家数还可以按统计可识别性选择，而不只按算力或固定分区风险扫描：在给定混合模型里先拟合较多组件，再沿合并路径结合高度与likelihood提出数量，避免对每个候选数从头拟合。[受限Gaussian线性expert分析](https://arxiv.org/html/2510.12744v1#S3)依赖IID、紧参数域、有界连续输入及相应分离/Condition K和渐近权重窗口，K₀至少为二；它不是Transformer深层token路由的通用专家数定律。统计MLE与有限EM返回的局部解也须分开，不能把一致性保证自动交给一次训练。模型族、初始过拟合数、合并/阈值、样本支持与独立预测质量共同验收，初始拟合、整条path及选数均计费；族、识别条件或优化失配时，保较少专家/dense与有界独立配置比较，不由一条dendrogram批准真实组件数、全局最优或免费容量搜索。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12744 -->`

本人末注：

- `SF-2025-ARXIV-2510-12744` — Herschel，Daily2025-10-16补Oct15；消费Cicero R14 exact-v1 §2/3.5–3.6/4首次必要，2+1+2=5，仅受限混合模型合并path/likelihood与MLE资格差额。保IID/compact/有界连续x/Gaussian线性expert、K0>=2/ConditionK/渐近窗、有限EM非全局MLE及全费，不授Transformer通用最优expert数。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

## 12273 MACSIM / 2+1+2=5 / TRAIN-SFT Ch29

当前likelihood/完整采样/greedy分验未承担无序matching对称set CE surrogate与实际AR无放回采样分责。插完整SF2609-30572 inline段后、forget训练段前。NCO只作有限监督机制证据，不冒LLM多agent运行时。

正文：

当demonstration目标是一组匹配而非唯一序列，监督还要声明排列资格：一次神经前向可以给出joint logits，但真正选多个互斥匹配仍须逐步更新可选集合；对称set CE可减少任意标签排序的负担，却不是完整有序匹配的精确likelihood。[受限集合监督分支](https://arxiv.org/html/2510.12273v1#S4)因此把训练surrogate、无放回采样与最终可行动作分开，单次forward不使选择步骤同时完成。Skip容纳不必全分配的目标，仍须至少一个真实动作；best-of-β伪expert还包含生成与筛选预算。目标集合/排列、mask/skip、采样规则和真实约束须共同保存，局部质量与时间并非每配置都支配。全部伪标签搜索、训练、采样和执行核验均付费；目标、合法性或净质量失配时保已验有序监督、显式匹配/约束求解与独立回归，不由set名称批准全局最优、安全调度或LLM多agent并行。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12273 -->`

本人末注：

- `SF-2025-ARXIV-2510-12273` — Herschel，Daily2025-10-16补Oct15；消费Cicero R9 exact-v1 §4.1–4.4/5/T1首次必要，2+1+2=5，仅joint logits/set CE surrogate与AR无放回consumer差额。保skip至少一真动作、best-of-beta制备筛选/全部费用和局部质量时间反侧，不授全局最优/安全执行或LLM多agent并行。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

请sole reader核三完整原稿/独立marker/本人注及actual owner/完整邻接；未SAVE/不预POST。
