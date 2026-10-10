# 已校准缓存/视觉融合三项：必要证据与窄owner差额

作者supp_jan15；精确v1必要source保存retrieval-core0–3/required4/direct5–6。date47原字段＋普通公告下界/正式ID Jan14存在上界限定本次日期，不用Submitted/Updated/registered单独证明first-public。三个当前abs无撤回/勘误，更早完整稿direct signal未见；08151后续v2不自动比较全版本。各2+1+2=5先标准审阅；若确认下述长期owner gap则深入受影响命题。无Books锁。

## 08743 TableCache: Primary Foreign Key Guided KV Cache Precomputation for Low Latency Text-to-SQL

实际§4.1–4.2/Alg1/§5 Tables1–5/§6–8/AppB/D/E：按声明PK/FK关系联合编码离线table cache、去position后在线补global position；Trie精确table串lookup，batch table-set Hamming近邻重排，再CPU→GPU KV预取/compute微批overlap。FK图**非所有schema天然DAG**，仅在实际acyclic/topological order成立；FK稀疏也不等完整query语义依赖，位置修复不恢复各层原fullcausalhidden。adaptive training是单table attention mask，省略PFK intertable，作者以形式blockidentity称充分但不认证跨block大小训练匹配。BIRD train3epochs/lr1e-6/warmup.03/Adam，其他baseline也tune但mask不同，不等无训练完全同modelartifact因果对照。Omni7B/QwenCoder7B、Spider/BIRD随机request/tableorder、single A800、bc100/bm10；metric是**全test累计TTFT**而非单请求90秒/P99，precision/concurrency/SLO/seed/cachecapacity Not Disclosed。

Table1 BIRD Omni61.5→59.9违反正文“所有gap≤1%”；Table5 trainingfree Qwen BIRD51→42.9（−8.1pp）必须保反侧，不授near-lossless全部backbones。Table2 cachemanager/rerank/pipeline分别增费/延迟，三成熟cachepolicy近.2秒不证明任何workloadpolicy等价；微batch compute/load参数不同及离线precompute不含全部lifecycle费。AppE拓扑O(m)省略edges/token attention，不能采完整线性离线编码复杂度。static-schema假设不保证model/schema/权限永不变，本文未验multi-tenant安全。当前abs无早completeproject/link、仅v1。

actual INFER-KV-CACHE Ch45:204–218完整邻接已明确独立KV不含跨chunk、局部repair/wrapper近似且fullfallback；188–190 graph prior转accessplan又是读取层，不是**先用显式relation选择offline联合编码closure、后组合table packets**。若确认差额，拟在独立chunk seam邻接一段区分显式关系的可验证编码边界与原fullcontext因果闭包；保DAG/依赖缺边/循环或改版须扩大joint closure或fullprefill，以及offline/tuning/重排/搬运费用。不为Trie/LRU成熟机制新增长期分。

## 08670 Parallel Context-of-Experts Decoding for Retrieval Augmented Generation

actual§3 Eq1–3/§4–5 Table1–3/Limitations/AppA/B/C1–5：N contextual独立KV＋emptyprior共N+1streams，retrieval与rerank归一harmonic r，(1+β)s_k−βs0＋γlog r_k，再对expert和vocab jointlyMax选择token并append给**全部**stream。因此是共享生成history的decode融合，不恢复文档间完整attention/原KV，也不是平均各doc答案。归一r不是可信事实概率，rawlogit offset/跨expert可比性没理论校准，γlogr影响全expert selection而非单expert内部token排序；重权retrieval可压正确低rank evidence、缺候选不能恢复。

三selfhosted7–13B family greedy、LOFT同top90/LongBench加2randomdistractor，完整共享prompt/retrievedpool但不同处理路径；MapReduce多calls预算不同。Table1 Llama Hotpot64<full66/QAMParI77<86、Tracking7仍很弱、NQ mixture87>Max85，不能采所有任务完整替代。β仅首token估后固定，dynamic并非所有最佳，γ默认2.5有部分固定值更高；seed42 single deterministicrun不是随机重复。AppA4 synthetic64×2048tokens one-secret-code/512output是速度人口，TTFT .14 vs25.5s与~1.7×E2E不等上述QA matched quality/SLO；仅声称continuousbatch/PagedAttention，hardware/batch/concurrency/fullSLO Not Disclosed；FP16 Llama corpus1222×74token KV11.04GB作者披露，仅cache存储非总HBM。每步N+1forward和全部streamappend仍增compute/KV、离线建库/更新费不免费。未核实现/复现。当前abs仅v1，无更早dated完整稿链接。

actual Ch45:204–218只有online修KV与offlinewrapper训练/拼KV两分支，314–316另有attention矫正需teacher，均未明确**保持KV分离而在decoder读出面汇合**这第三接口。拟独立chunk seam邻接一段，保logitAPI/internalaccess、sharedhistory的读出局部取舍和全部stream成本/缺候选/跨doc合成退路；fullcontext重算与cache repair并存，不称完整因果恢复。一般contrastive sampling归Ch20，不在Ch45展开gamma配方。

## 08151 Where Does Vision Meet Language? Understanding and Refining Visual Fusion in MLLMs via Contrastive Attention

actual§3layerzeroing/§4 Eq1–4/§5.1–5.6 Tables1–3：LLaVA1.5/1.6 7B、六VQA，zero visual-positionhidden 保shape，不等完全移除所有已传播视觉信息。mask19后nearstable/29敏感是该干预路径条件，不证明human式review、唯一fusion层或task真值。先按diagnostic定位候选earlylayers，28map和candidate Hellinger最大差选early，再abs差attention低percentile softscale visualfeatures，于29hook。数值attention差不是因果贡献/已定位grounding，矩阵/分布维度/heads说明不足不照抄exactrecipe。层28必须在29前才可用，额外map采集/attention计算、内部hooks费用，不是黑箱API。

sameLLaVAbase局部quality改善，但大表不同模型不等capacity/训练budgetSOTA，Qwen2更高不能忽略。all/deeplayer候选范围成绩反退、best20%mask之后更大比例退；λ软抑制不等物理token pruning或无需所有计算。作者“RTX A800”身份仅原口径、不自行改准确SKU；PyTorch2 Ubuntu20.04，precision/batch/concurrency/SLO/seed/fullcost Not Disclosed，1/t图不授production端到端速度。代码willrelease，未复现。当前absv2无纠错标记，本次只v1。

actual MULTIMODAL-REPRESENTATION Ch23:105–111完整邻接为two-pass spatialhidden搬运与derivedviews差分，115–117为producer/consumer层注入；尚非**用同一路径early-vs-late attention差作为晚层visualposition软maskproposal**。如确认长期差额，仅在局部干预邻接单段说明sensor/map identity与consumer hook分责、不要把late敏感证明层已完成fusion；低质量、过mask或map/hookbudget不可用回原forward与外部grounding。无锁不写。
