# 第十一批必要精确v1命题

四项root准入校准通过后只读核心、主要对照和直接反侧。原Submitted分别15556 Feb17 13:08:06Z、15563 13:23:26Z、15564 13:24:56Z、15567 13:27:05Z；同身份DOI Created分别Feb18 02:44:18/27/28/33Z（Registered同刻或+1秒），与官方公告下界Feb18 01Z共同限定完整落本窗。未用Updated/相邻ID推日期；现有当前metadata轻查无撤回信号。源码未核、实验未复现。

## 15556 PADE — 2+1+2=5，必要核心/具体指令保证受影响深入完成

actual[exact-v1](https://arxiv.org/html/2602.15556v1) §3–5/Eqs1–8/Tables1–6/§7及必要B benchmark定义。逐层positiveattention差平均PAD，按每head visual logit MAD缩放后最后层加λ=.1，systemlogit减平均视觉增量STC。PAD不是语义oracle；MAD为零也不能自动造增强。Eq7只减logit平均值，不严格守恒softmax归一化质量：一个system/visual/user/history logits全0，visual加a>0、system减a后分母e^a+e^-a+2>4，user/history概率低于1/4。因此只采补偿启发式与受限结果，不采用保持指令attention的数学/安全保证，也不说sys tokens普遍无语义。

5个LVLM/单RTXA600048GB、samplingdefault、CHAIR最多128输出token；POPE均衡yes/no，CHAIR仅object/caption计数，HallusionBench/AMBER不能等全安全。Table6去MAD/去STC局部退步，但13B/Qwen数据与Table2部分不一致（47.9/12.8或47.3/12.6不能静默当统一population），λ过大质量下降，late-layer最优只tested。新增地图/逐headMAD有额外读attention/计算，主文“negligible/similar speed”无runtime数字，precision/batch/seed/CI/真实instructionlongtext独立评价NotDisclosed，不授全模型无退步/零成本。视觉比重/指令比重/任务质量分责，静态或完整grounded检查仍共存。

## 15563 1-Bit Wonder — 2+1+2=5，必要核心与质量/资源反侧完成

actual[exact-v1](https://arxiv.org/html/2602.15563v1) §2–3/Tables1–3及A1–5/E1–3必要配置。1000step bf16 warmup后tensor 1D kmeans centroids固定、block64/16bitscale，STE高精度backward，实际1/4bit含scale1.25/4.25而非整模型1bit；embedding/output仍bf16。4B16bit、12B4bit、31B1bit约7.8/7.7GB权重匹配，不是KV/activation/总HBM匹配；模型depth/width/LR与compute不同。64H10080GB、FSDP2、global4.19Mtoken/4096ctx、同151Btoken采样/36ksteps，12/31Bcheckpointing；Tulu3 SFT5epochs/8192ctx。相同token不等相同总训练FLOPs。

Table1 generative任务局部优于4B，1bit也非全部胜4bit：GSM8K45.26<48.52、Hella54.70<55.41、IFEVAL62.70<63.45；GPTjudge Aidan不是人工truth。scalinglaw只是所测N/D/format经验拟合，不授所有硬件/预算的数学最优。E2 L40S/CUDA12.8/PyTorch2.9.1/Triton3.5.1，micro8192平方/B1 lookup+bf16，Marlin4bit用fp16；100callCUDAgraph×100 runs SE，model空KV100decode/B1均值error<1%。同model1bit可快但权重匹配31B1bit60.7tok/s低4B16bit88.8/12B4bit79.3；B256无速度优势，prefill/computebound可更慢。图捕获刻意排hostlaunch，不是online E2E/SLO/energy；codes/checkpoints承诺未核，质量seedCI未披露。

## 15564 SquRL — 2+1+2=5，必要核心与oracle/训练边界完成

actual[exact-v1](https://arxiv.org/html/2602.15564v1) §3–5/Theorem3.1/Tables1–5及必要B2–4。固定有限workflow binarysuccess的oracle union≥best单集是条件上界，pairwise disagreement不够：A1={a},A2={b},A3={a,b}仍Δ=0；必须最佳静态之外有success质量，不能从heterogeneity或oracle81.5直接推出可学policy/低成本nearoptimal。SFT逐simple→complex取首correctworkflow（无valid者推迟），GRPO用format/timeout5min/executable/goldresult/conditionaltime分层reward；各actorBernoullimask强迫替代，complexquery留存率更高；p比例由LLMpairwise reference/confidence替代完整execution，非groundtruth。

Qwen2.5-1.5/3/7Bpolicy/QwenPlus actor、Squrve sandbox/VERL；test每query5workflow再按结果majority，其他baseline全成本未match。Spider2Lite改DeepSeekR1actor，正文44.97与Table49.18不一致不可统一；1.5B BIRD64.47低RSL65.82、3B65.59亦低，非各scale全胜。p=.1局部提升但.3低于trueonly，mask低available下反侧支持actor组合依赖；强actor改变奖励质量不是单独policycapacity因果。trainingHW/precision/batch/iterations/G/seedCI/API总调用NotDisclosed，83.27/4.41s消融单协议不是allmain统一时延，OOD/longtail只是所测dataset，不能保证SQL安全/权限或全数据库语义。静态workflow在单一覆盖集/审计预算条件下仍合理。

## 15567 CASF — 2+2+2=6，安全受影响必要核心完成，精确保证隔离

actual[exact-v1](https://arxiv.org/html/2602.15567v1) §III–V/Eqs5–14/TablesI–II/§VI。streamingflow推理实时流v，distance/normal造SPD metric，workspace约束经JᵀMxJ pullback、bodypoints合并I+ΣwMq后M^-1v。神经distance用abs(s)回归/Eikonal、有限bodypoint/kinematics，不能视为完美signeddistance或全表面collisions。Eq7所写argmin 1/2||dot a-v||M²唯一解v，而非M^-1v；后者对应含线性项的不同目标。有限SPD metric只缩放/旋转，不提供barrier条件：一维safe q≥0，v=-1、M=1+c有限时qdot<0，在boundary仍可穿越。原§VI也将方向非对称metric/更强保证留未来。隔离严格constraint/safety与“distribution不改变”命题，不因理论冲突改EX，受限metric变形机制/实测仍可保留。

PushT200demo、state/image各50episodes，SR门槛为demo最小coverage；TableI CASF局部优但LASA TableII KhameshMaskedFD .157高于CBF .142，Sine .211高CBF .205、Rshape .054低.075；不能写全任务最低。rawSFP FD为NA相对自身不适用。有限表CASF violation显示0是该rollouts精度，不等严格不变集。Robomimic每link至多15bodypoints、UR真实四任务每项50demo/learnSDF只qualitative执行，缺真实trial成功率/接触统计；训练超参引用SFP上游，不为了枚举读整上游，HW/precision/seedCI/controlrate/E2Esolvercost当前NotDisclosed。固定SDF场景、不证明perception-driven未结构化障碍，距离/法向/采样或deadline失准仍需独立controller/CBF校验或停止。
