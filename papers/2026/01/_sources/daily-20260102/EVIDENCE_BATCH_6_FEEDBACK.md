# Jan02 preference/feedback/measurement 四项必要证据

四项完整v1题摘准入校准；评分6/7/5/6。作者与root实际必要机制与评价/反证已读：RR与Triangulation针对具体测量缺口深入，分别Ch31 97/99、Ch66 2803/2805两段及末注已实际POST通过；Pareto标准仅报告，Iterative中心争议安全暂缓均root通过。日期DATACITE_POTENTIAL原值created分别03:25:42/03:23:42/03:21:25/03:19:53Z，共同holiday+ID规则界完全本窗，不用Submitted或register当分钟。未运行可选代码/复现实验，性能不外推。下面原拟处置保留过程依据，以此实际决定为准，不授日级完成。

## [ResponseRank — 2512.25023v1](https://arxiv.org/html/2512.25023v1)

2+1+3=6。实际§2/3/5/8、AppendixD.1–D.3与资源披露：按annotator/length等strata建立comparison强度rank，先normalize winner/loser、强度utility差与0 anchor联合PL，singleton退BT。只需局部单调关系是必要假设，不是由stratification保证；tie splitting、小strata与batch packing改变信息支持，rank中比较对象是utility differences不是response本身。PDC比较绝对utility差相关，不能替ordinal方向；真utility现实未知，不能把agreement-based近似称为真实cardinal恢复。

真实MultiPref 10461→length≤1024后9846，2000test，30seed重新split；每train pair随机1/4annotation，eval majority标签，ties约26.32%去除，fraction按annotator组采。RR-RT在annotator×8length bucket仍较差，额外分类/justification耗时破坏proxy；RR-Stated相比BT0.6pp不显著，RR-Random只in-distribution益不迁RewardBench，故不是rank强度必然提升。RR-Agree来自全部4标签，虽然train方向抽1票，资源不是单标注无额外监督；RM而非LLM-policy RLHF downstream尚未完成。Llama3.1-8B fullFT，BF16/AdamW1.5e-5/3ep/batch16×4accum/1024，A100/H100，fullrun~1.5h单H100；BT2ep/3ep显示不同task overfit取舍。small control5run数在CI内，不借其数学给语言policy保证。

拟TRAIN-RLHF Ch31 73–95在BT score difference后补strata-valid强度差rank/anchor与局部单调性、共享metadata资源和RM/后训分账，现论证尚未该桥接；待必要原源及owner独立核。不把ordinal准确/采样一致性当cardinal识别。

## [Iterative Deployment — 2512.24940v1](https://arxiv.org/html/2512.24940v1)

2+2+3=7。实际§2/2.1/3、AppendixA.1–A.3：生成→VAL过滤valid→跨代池每task取最短plan/最短trace→SFT，implicit selection目标非公开人类utility。主文§2说finetune M_n，A.2却每代从固定Qwen3-4BThinking2507base重新LoRA训练累计pool，不能补造真实parameter inheritance。三PDDL domain各1000task既collect又test，尚未解决全独立新任务/现实部署泛化；3run/unanimous@3不是跨dataset generalization。curation/no-curation Blocksworld对照支持局部选择效果，不保证开放世界validator、safealignment或防collapse。

A.1 Prop1对固定on-policy binary-valid sample显示SFT trace-summed gradient与REINFORCE仅差N+/N正尺度，要求N+>0、相同支持/完整trace加权，不能外推多epoch optimizer等价。Prop2分别定义p_pi^+∝μπ1_valid与p_beta^+∝μβ1_valid，却L374直接把条件分布ratio写成β/π：一般还应有Z_pi/Z_beta，除非两valid normalizers相等/被系数重新吸收。L380沿用原λ，因此不能无说明授精确off-policy等价；R_eff ratio还依赖currentpolicy，只能冻结数据的局部gradient重写，非固定reward完整优化证明。保留作者原式和这一数学未决，不改低分/不删候选。

Xeon6248R/A10080GiB，Qwen3-4BThinking2507，inference temp.6/context32768；rank16/alpha32/dropout.05、AdamW1e-5/2ep/batch1/每代10%trace validation。precision与全rollout成本未披露。Ch27 342–358已将corpus recursion/parameter recursion拆开、387–405强调verifier闭环与共同measurement channel；具体缺口/争议边界待root核。建议暂缓‘完整RL等价/现实迭代部署泛化’，可限定Prop1局部事实，但不让未纠正Prop2进入Books。

## [Triangulation — 2512.24842v1](https://arxiv.org/html/2512.24842v1)

2+1+2=5。实际§2/3.1–3.5/4/6：reference family保持完整predicate，predicate-swap另作sufficiency source，不把gender改变当同family；跨语言translated patching需对齐映射/activation distortion界，KO necessity、swap sufficiency、同predicate stability和cue-only falsifiers分别预注册。mechanism class允许language-specific低层circuit，min_e T(e)≥η不是要求同head位置；P/Sim/τ/δ/η/α都属验收对象，i.i.d Bernoulli/Beta区间只在真实采样假设成立，重复关联干预不自动独立。

§4明确propose实验protocol（Gemma1/4B、Llama1/3B、Mistral3B/MADLAD MT、FairTranslate/GLITTER/mGeNTE），未给已完成baseline胜率/production实现。reference判定器/LLMjudge共享偏差、multiple valid circuit不唯一、异质family错误拒收/假通过、额外alignment与patch预算保留；不说该标准已经过滤真实跨语言spurious circuits。hardware/precision/batch/已运行样本与结果NotDisclosed；理论/协议无性能保证。

拟已有覆盖PLATFORM-EVALUATION-SYSTEM Ch66 2795–2797已要求estimand/identification/assumptions/falsifiable stress test及Unknown降级，2814–2816保存rawpatch/control/版本；若跨predicate-family验收仍为真实具体缺口应最小融入而非仅主题NoChange，待root核。

## [Compute-Accuracy Pareto — 2512.24776v1](https://arxiv.org/html/2512.24776v1)

2+2+2=6。实际§3/4.1–4.5/limitations：19model/config单completion、reasoning temp.6 vsinstruct greedy、officialtopk/p/contextmax及freqpenalty.05，各模型自然停止不是同length干预；regex后GPT5.1mini看最后20tokens，会漏output位置/格式失败，未给独立judge误差。Eq7算active projections/FFN/MoE-router、prefill+KV-aware decodeattention、vocab；analyticalFLOPs不含HBM/EP/通信、batching/kernel/utilization及judge成本，非实测latency/cost。

§4 frontier跨model点/五bench任务难度混杂，不能由其flattening证明固定checkpoint增加budget后因intrinsic deductive horizon因果饱和；不同prompt/temperature/defaultconfigs也不 isolate MoE架构优势。incorrect-trace更长为条件关联，不推出提前停止已能识别错误；原97%说法不采为全部署比例。modelrelease chronology非同architecture/data的controlled算法效率因果。hardware/precision/backend/重复seed/运行concurrency未披露；只保配置限定cost-quality诊断，不推荐模型或补完整公平预算。

拟已有覆盖PLATFORM-COST Ch70 86–101已要求state-dependent work与analyticproxy≠latency账单，MODEL-LONG-CONTEXT/采样具体饱和需core因果不成立，不能以主题相似声称全frontier已覆盖。建议仅报告有限frontier/失败trace现象：缺同model可控budget/质量与实际运行成本，未确立可部署停机或通用模型选择规则；待root核具体长期门槛。
