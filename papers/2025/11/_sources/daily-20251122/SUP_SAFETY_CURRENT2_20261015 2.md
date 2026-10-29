# Nov22 三项安全潜力必要域与LightFusion版本角色

作者Noether；[HEAD](SUP_WEB_REMAIN_HEAD_20261015.raw)、[定位](SUP_WEB_REMAIN_LOCATOR_20261015.raw)、[CORE](SUP_WEB_REMAIN_CORE_20261015.raw)、[CORE2](SUP_WEB_REMAIN_CORE2_20261015.raw)、[尾](SUP_WEB_SAFETY2_TAIL_20261015.raw)保存本轮原调用/返回。仅必要机制与权限/受影响限制，不采用新安全效果，不实施攻击、执行代码或扫描全基准。

## Secure-Instruct 2510.07189v2

实际§3.1–3.3、4.1及AppendixD原L99–143/304–309。MITRE CWE seed生成vulnerable→双static checker确认→repair再检，另secure-only路可扩大人口；CodeQL/Sonar同结果是检查器范围非无漏洞证明。训练保持functional数据混合，生成策略训练样本量/CWE覆盖不同；CWEBench secure ratio由CodeQL判断，CWEval另functional/security test与joint指标，不直接互换。MinHash/LSH Jaccard>.7去重及排MITRE seed样例是已声明缓解，不保证语义/预训练无污染，原限制明确false positives/missed duplicates、CWE/语言/模型范围。P保持在成对生成验证与功能/安全不同消费约束，不采用28.5/157.3%或任意secure ratio即安全/功能俱成；v2具体日门/重要增量仍未知，不需全四模型/44CWE方法。

## Q-MLLM 2511.16229v1

实际II-B threat、III-A/B必要nearest-codebook/安全mapping与完整Algorithm1/2、Limitations及必要utility/textonly反侧（原L104–117/137–162/188–315/484–495；返回另含VIII/IX必要表域）。white-box image perturbation与toxicimage两种权限分开，dualVQ之外还有标注D_map的codeword-category阈值；非neutral先warning，neutral才接patch tokens+text。不是“纯量化不需任何安全校准”，codebook训练本身采用gradient approximation，非可据离散就认证不存在adaptive/gradientfree路径。

原对一处失败用LED定向edit后再评不能与untouched模型合并作完美安全；作者明确不能保证random-search攻击，text-only更高不消除视觉残余。额外curation/fine-tuning的enhanced utility与原设置不同，不能归VQ单因果。P保留视觉token/检测消费者的机制，不采用100%/所有攻击或无额外推理成本，不扩大全部attack/实现审计。

## Reason2Attack 2503.17987v3

实际§3.2与§4必要定义/过程reward（原L116–125/157–170）。权限为blackbox prompt→image或拒绝反馈，posttraining/RL使用attack反馈和相似性/长度等proxy，而非无查询/无训练成本。reward语义相似性不等人工harm真值、拒绝/成功/transfer不等通用绕过。只保训练过程改变攻击prompt生成的具体潜力；无采用ASR/商业迁移/普适攻击效果，不复现或制作攻击样例。currentv3及具体修订资格未知，不能由旧first与v3自动当Nov21事件。

## LightFusion 2510.22946v4

当前原abs明确v2 withdrawn后v3/v4正常正文。Ohm§18随后实际打开旧[v2原身份](https://arxiv.org/abs/2510.22946v2)原L8–37：withdrawn by Zeyu Wang，Comments为premature/not agreed by all parties，v2无PDF；v3/v4后有正常正文。该必要说明现已实际读核，不再挂普通显示域，不将全family记W或推断数据造假。不得采用撤回v2，当前v4潜力/具体公开与重要修订资格另分责，不双版全文或重double-fusion机制。本包其余三项安全必要域亦已Ohm§18实际通过，不预日级完成。
