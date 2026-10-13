# InfoDensity17310：轨迹熵代理与正确性资格分责

resume_mar17，仅03-20补03/19。当前适用合同/本日停点与Books约束实际重载；批5完整AB/日级夹证准入有效复用，原2+1+2=5不变。准备必要Source/actualowner/逐字PRE，未自授Source PASS、写锁或safe/DAY。

## 1. 必要原证与停止

[exact-v1](https://arxiv.org/html/2603.17310v1)实际§3 L95–152（§3.1回答token条件测量、ProcessBench人口及first-error截断）、§4 Eq1–6 L153–193、§5.1–5.4/T2 L195–263与Limitations267–269，A L309–314必要prompt。当前[官方abs](https://arxiv.org/abs/2603.17310)有June4 v2，完整AB明确改为自身token entropy与suffix-max envelope，影响拟采用命题；因此仅定点[v2](https://arxiv.org/html/2603.17310v2)§3–4 L95–193、§5/T2–3/长度消融及Limitations L198–289、A338–348/B350/C355–358/D359–364与E3直接失败379–382。不遍全部案例/图像、references、代码或更早版本。v2仅纠正当前采用边界，不把June事件计成本窗第二家族或倒写成03/19首次机制。

## 2. 采用接口与反证

v1将固定Qwen3-4B-Instruct judge在各推理前缀条件下对回答token的vocabulary entropy均值，形成H轨迹；§3.1写gold answer Z/answer-prefix，A另说自然续写prompt，精确gold/采样续写实现未在采用中补齐。它不是随机回答整序列熵的普遍恒等，也不是互信息真值。v1质量取1−mean(H)/H0与严格下降比例各半，再乘本题group长度z-score的指数；只给最终正确回答，否则0。H0=0、sigmaL=0的数值守护未完整披露，不采用可执行全recipe。fixed judge稳定参数不等测量真值；first-error后剔除与不同长度插值聚合的mean曲线，不支持每条trace每步必须降低，更不授低熵代表语义正确。

v1 ProcessBench step AUC .52–.67/d .06–.58已直接否定可靠单步错误oracle；T2 Qwen0.6B平均49.2低于原49.5/GRPO-Acc51.9/PEAR50.2，MATH50072.2低于原73.2；DSR1.5B Olym44.7低于原45.0与GRPO-Acc45.2，PEAR输出6136还少于Info6443。最高GSM8K验证准确率/1%近值偏短选checkpoint有选择预算，不等独立总费匹配。§5.4 AUC-only重复演算/hacking、monotonic-only高不确定、lambda.5塌缩为原文直接反侧，不能宣称分量均是高质量充分条件。max32768/temp.6/top-p.95已披露；v1硬件/precision/组大小/完整训练steps与judge/选点全费用ND，不用token下降证明总成本。

v2改为当前模型自身生成token的top20归一截断分布熵，训练每50token chunk均值（分析时双newline），不是v1固定judge的回答条件熵。A明确renormalize，因此0≤H≤log20属于该截断测量；接近full-softmax只是作者关于高置信分布的条件性主张，不授任意尾分布。质量用从右向左suffix-max的均值除log20，故早期统计依赖后面整条trace，是事后sequence reward，不是线上prefix告警；它偏好较早进入持续低不确定区间，不认证中间步骤或正确性。final verifier仍先给资格，长度指数仍共享group统计，sigma0须另护。与v1共享的是轨迹代理×相对长度×最终正确资格的分责，不是同一具体目标。

v2 stepAUC .489–.531/d −.02..+.12、外部ProcessBench traces非本模型own generations及Qwen family异常，作者均承认。不将group内ranking自动豁免代理失配：同题低熵错误仍低熵，final gate只能验最终结果，不能证过程。T2 DSR1.5B GPQA9.6低于PEAR/ETR11.1；Qwen8B平均78.1低于ETR79.1且AMC90<92.5/MATH93<93.6/GPQA56.1<57.1。T3基线正确问题仍7.8%回归且长度4684→10323；E3实际算术错且未再次检查。极强lambda.5仍塌缩；不授各题无损/防hacking/总费普遍下降。v2 group5、max16384、LR1e−5/B32/KL.005/lambda.05、LoRA32/64、DeepMath7000/207steps、greedy/H200+A100已披露，但precision/seed/并发/SLO及全feeND；7B/8B baselines直接复用另一论文，1.5B才自训，不把相同data/protocol等于全预算matched。

如需强语义保证，只一次请求固定版本的回答/自身测量实现、H0/sigma0守护、独立过程真值/错误盲验和matched全部judge/rollout/选择费。有限分采接口不依赖普遍语义真值或防hacking保证。

## 3. actual sole owner差额

sole `TRAIN-GRPO` / [Ch33](../../../../../books/part-04-training-system/33-grpo.md)，实际完整293–333及1–160与Ch32/34入口已读。现有DRT对齐参考步骤、DR2第二pass、CRT冻结reference容忍边界、hybrid正确短bonus与长度loss系数，未承载“固定回答条件熵/自身生成熵的版本区别、轨迹聚合的质量代理、后验suffix统计与最终正确资格分责”。不是泛entropy主题NC，不重复Ch31外部PRM或Ch70成本。拟327 CRT完整段后/329 hybridbonus前两段，保持已有过程verifier、参考容忍与outcome-only分支。

## 4. 两段literal PRE与静态注

正确性资格之外，还可用整条回答的不确定性轨迹提出压缩偏好，而不让每步低熵自行认证推理。一个受限分支用冻结judge在逐步推理前缀下估计回答条件的token熵，再以低累计不确定和下降比例组成质量代理，乘同题组内相对长度项；最终答案验证未通过仍赋零。它改变的是正确回答之间的sequence reward，不是逐步错误定位或真实信息增益。测量对象、judge与分段规则应绑定版本：当前修订改用policy自身生成token的截断分布熵，并以右向左的后缀最大值聚合；该分数消费未来整条trace，是事后奖励，不能作为当下prefix已有充分证据的在线判据。<!-- source-family:SF-2026-ARXIV-2603-17310 -->

[轨迹熵代理的有限对照](https://arxiv.org/html/2603.17310v1)仍有任务/模型反退、单分量钻空子与过强长度压力下的塌缩；[受影响修订](https://arxiv.org/html/2603.17310v2)也保留原正确题回归、单步熵近随机判错及外部trace人口的限制。低熵可以是重复演算或共同错误，截断分布的归一界不证明完整回答语义质量，组内长度尺度退化也须另护。额外judge/概率读取、完整rollout、分段统计、checkpoint选择与训练都计费，减少输出tokens不等总费用或所有任务质量保持。代理失配、验证不足或压缩退步时，保留完整trace、可靠过程检查和普通outcome-only/保守长度项，不由不确定性分数替最终答案或过程签发正确性。<!-- source-family:SF-2026-ARXIV-2603-17310 -->

静态注：

- `SF-2026-ARXIV-2603-17310` — [InfoDensity v1](https://arxiv.org/html/2603.17310v1)§3–5/Eq1–6/T2/A必要测量，与[v2受影响目标](https://arxiv.org/html/2603.17310v2)§3–5/A/B/C/D及E3。仅轨迹熵代理×相对长度与最终正确资格分责，固定judge回答条件与自身token/suffix-max版本分开；保单步判错弱、人口/基线/任务反退、hacking与全费，不采语义真值、在线prefix保障、完整recipe或通用无损压缩；未核代码/复现。

## 5. 获准实际窄写与 writer 读回

reader§26原两PRE有限通过且root明确授soleCh33窄锁后，resume_mar17逐字写新329/331及本人静态3218。writer实际完整317–345与3210–3218邻注读回，CRT相对容忍→轨迹代理/最终资格→hybrid bonus衔接准确，literal与静态原文一致；本family scoped diff仅两正文+注，diffcheck0。未自授actualPOST/safe/DAY；交reader一次非writer完整局部和本人注POST，不把验收身份写入Books。
