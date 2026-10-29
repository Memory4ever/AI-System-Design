# 10195 AAC：必要Source与实际owner受限终态提案

补充Mar12 BJT自然日；第二包完整exact-v1 AB准入和arxiv日级日期夹证有效复用。当前精确版 `https://arxiv.org/html/2603.10195v1`，`SUP_CORE_10195.raw`及txt，GET200 UTC2026-10-09T13:47:41。作者实际必要读§3.1–3.5（Eq2–8/Alg1–2/Tables3–4）、§4完整、§5.1–5.11 Tables7–21及§7/§8完整与Summary必要口径；没有实际图像点值、代码、复现或硬件日志审阅。文本图注不替像素检查，不采用未读图像细节。

## 原约束→实际增量→评分对象

内部probe能区分样本，但不自动成为可干预truth节点→作者按signed probe权重取top50，grounded样本80th percentile baseline＋probe-confidence gate/scale在每个生成step抑制excess→需重新核局部选择性与真实输出/非目标能力的关系。本包准入不由成熟linear probe/ITI/DoLA原则或ANC名称支撑，也不因小增益/缺代码排除。拟2+1+2=5：具体局部抑制接口及其可用性/评价边界为设计2，单模型推理组件1，受限可复用条件2；不借成熟“相关≠因果”抬Durability3。

中心设计/采用保证受到反证，因此实际必要深入，不把5分当停止上限或争议降分。拟争议/暂缓Books0，待非作者实际源/owner校准，不预授正式candidate处置。

## 核心机制及识别权限

§3.1最后nonpadding token或meanpool残差状态；§3.2 logistic probe采用50/25/25 train/cancel/eval。Alg1第5–6行直接在D_eval上选最大AUC层，然后后续同heldout eval报告效能；没有独立layer-selection validation，不能授完全未参与选择的test估计。输入样本/label如何从MC正误构成prompts与完整token-prompt模板未披露于必要主文，不虚构question/answer拼接实现。

§3.3 Eq3 topK(w) signed排序、K50；Eq4只用cancel grounded y0第80百分位。§3.4五posthoc策略修改一次forward后的hidden，一个live hook在生成每步更改所选层。Eq7/Alg2在c=f(h)>.45时用 c*.9*max(h[H]-b,0)衰减，其余维度不动；不会因为未选维度逐字保留就使后续非线性输出或所有task不变。对同一个probe优化后再报告其confidence下降，只能认证该readout下改变，不能唯一识别真实“hallucination locus”。原文Table19后与§5.10把selectivity当因果特异/全能力无损，证据不够。

FFT variant把非自然排序neuron坐标视为空间signal、只留top5谱分量；没有神经元任意置换不变的证明，局部selectivity不证明频率是hallucination因果。暂不采用FFT机制为稳定知识。

## 关键评价与直接反侧

§4三frozen模型OPT(表称163.8M)/Phi3mini3.821B/Llama3-8B8.03B，分别float32/fp16/bf16。TruthfulQA600用于提取、probe、cancel baseline和evaluation，HaluEval600称crossbenchmark；generation100 samples/max_new_tokens30。主文必要位置没给GPU、软件version、latency、hook host/device sync或端到端成本，不以“no additional forward pass”授零计算/延迟。Probe fit、各layer state采集/每token logistic scoring仍有费用；可选code未核不阻断主文受限裁决。

Tables7–11定位/层扫是作者相关结果：各模型峰46–53%深度，不能从三不同架构/训练/precision模型推出模型规模的单因果阈值。Meanpool“best”Table7与Tables8–10有不同layer，不能当同一位置pool差的通用数；不采用all-modelscale law。

Tables12–14五posthoc有较高probe Sel，但Table16全部accuracy原样；§8.1作者说明这些posthoc发生在决策之后，所以这不是“在线方法公平胜五种活跃控制器”的对照。live Hook在OPT Table12 Reduc=-.0073/Drift=.0281/Sel=-.26；Phi Sel=.98、Llama1.35。Table18adaptive/static的probe readout改善也不能消除此负侧，更不是独立truth概率。Table16 live accuracy .6933→.7133/.7933→.8000/.8133→.8200，但列名HallRate OPT .7125→.7875、Llama .8125→.8625（Phi .7375不变），与“统一降低hallucination”不一致，原必要正文未给足其人口/阈值/评分算法解释；不任意改列含义为真实错误率，也不抹去实际反侧。

Table17 generation MC1/MC2/tokenF1：OPT .24→.23/.4179→.4126/.1781→.1728，Phi .29→.28/.4260→.4250/.2418→.2370；Llama .29→.33/.4306→.4335/.2156→.2183；EM全0。作者自己近chance限制适用，不能因Llama4/100增益宣称其下游普遍准确/首个容量阈值。MC1是答案logprob ranking、MC2概率质量、F1参考token overlap；§5.7又称freegeneration，接口与实际评估实现未充分披露，不混成自然用户free-answer truth。未给repeat seeds/CI/统计推断，保留描述点估计而非置信改良证明。

Table19 ITI sweepingalpha/作者centroid direction、DoLA早38%层和late logprob-.5early配置只作者实现口径，不授所有原ITI/DoLA公平复现。Phi ITI Sel1.88>AAC1.62，Llama DoLA MC1+.08>AAC+.04；稀疏优越不是全模型/全指标。更高probe selection score不独立认证更好输出或polysemantic causal story。

§5.10/Table20：WikiText103仅80 sentences，PPL四有效数字65.42/11.66/21.07前后相同，MMLU100 questions OPT .20→.21，Phi .40/.40，Llama .42/.42。原文“zero change at all scales/entire distributions intact/无需重新验收”超出小样本四位显示，OPT实际也非accuracy零变化。没有逐token hook触发率/剂量、置信界/同一输出logits或分布距离，不确认hook未激活、造假或能力已下降；只确认这些显示不足以授全能力无损。未报告DoLA在相同80/100上的副作用，不能借对比措辞判AAC唯一安全点。

§8.4原in-domain probe限制、TruthfulQA→HaluEval转移随规模变弱、三模型near-chance及ANC没有独立noise reference全部保留；主文没有具体crossbenchmark效能表，不补造数值。这些足以受限终态，不需扫无关引用/附件。

## 实际唯一owner与Books差额

拟唯一 `MODEL-TRANSFORMER-LAYER` / [Ch17](../../../../../books/part-02-model/17-transformer-layer.md)，runtime residual干预/功能因果而非另建AAC章。作者实际顺读当前391–416完整“Layer冗余取决于干预协议”：候选minimal pairs→同数量random intervention/双向patching→checkpoint/utility/副作用，绑定projection/layer/token/probe/evaluator；局部线性orthogonal不保后续非线性/全语义，原权重和运行时vector退路具体在414–416。现owner已承载辨识与控制的长期资格，不宣称已吸收本稿50node/percentile实验。

相关handoff `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)当前265–286完整局部作者实际读：runtime residual sensor身份/label来源与effect authority分开，reconstruction/output扰动/解释预测是三测量对象，变化幅度vs带符号干预/等范数与平均梯度对照、非目标保留点估计≠全能力。它接测量发布，不复制成第二机制owner。

当前不提出书稿新段：正中心保证争议，原限定机制既有原则已充分承载；“已有覆盖”不能冒称本稿新的诊断实验获采。拟正式**争议/暂缓Books0**，必要深入完成；局部confidence/percentile recipe仍保留候选而非主题相似删池。

## 精确重开与停止

仅需重新提供真正分离layer selection与test、HallRate及MC/generation评分的实际定义/人口、独立行为与均预算对照，以及针对保留能力的hook触发/剂量与足量非目标回归；若主张部署零成本，补完整hook/probe路径latency和platform配置。保持已读精确v1/反侧，无需等待全部代码或所有引用。不采用唯一causal locus、规模阈值、普遍降低幻觉、零能力损伤/免回归或零端到端费用。中心争议不是材料访问受阻。作者只own本包/Report，待非作者Source与actual owner裁，未授DAY。
