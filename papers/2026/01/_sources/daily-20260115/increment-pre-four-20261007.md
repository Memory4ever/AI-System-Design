# 首批余四必要证据与 actual owner

作者supp_jan15；原52与原证据不动。首批完整题摘及必要原源/actual owner已获root独立PRE。08379 actual Ch24:248/240–259及末注、08325 actual Ch26:71/65–84及末注、08773 actual Ch76:63/57–78及末注POST分别通过，三窄锁已释放；08273具体Ch48 Existing通过，无写入。新增日期使用root已核的正常公告下界＋正式ID/DOI已存在上界限定于BJT Jan14，不以Submitted、Updated或registered单独判公开。早artifact不是更早完整论文，未授整日完成。

必要原件：[方法1](./increment-core-four-method1-20261007.txt)、[方法2](./increment-core-four-method2-20261007.txt)、[核心评价1](./increment-core-four-eval1-20261007.txt)、[核心评价2](./increment-core-four-eval2-20261007.txt)、[核心评价3](./increment-core-four-eval3-20261007.txt)、[必要限制](./increment-core-four-limits-20261007.txt)。不授代码实现或复现。

## 2601.08379v1 MMD Guidance — 2+2+2=6；具体 gap 深入，拟 Ch24 窄整合

已读 exact-v1 §3/4.1/4.2 Eq5–8/Alg1、Theorem1/2 的条件与所证对象、§5 product kernel Eq10–11、§6.1/6.2 Tables1–4、§7 必要反侧。采样更新叠加 empirical MMD 梯度：batch 内 repulsion 与 reference attraction；prompt-aware kernel 用文本相似度乘 latent kernel，固定 prompt 仅更新 latent。直接优化有限参考人口的 divergence，不是单样本分类器或恢复原 score。Theorem1 的 iid reference、normalized differentiable Lipschitz kernel及固定点/§4 uniform bounded ball+gradient Lipschitz只约束 cross-term estimation，未证明有限 solver 最终命中任意分布，更未证明 decoder 后像素人口匹配。Sparse reference/kernel choice 是明确反侧。

实验：LDM/SD1.4 无条件，SDXL/PixArt 条件；DINOv2 metrics五 seed，非人类质量/语义真值。真实FFHQ500 reference与合成参考/style-population有局部 FD/KD/coverage 改善；No-guidance/CG/Domain Guidance 不同训练/适配预算，不采总体优于finetune。Table3 4090、50-step 累积样本时间增加，非免费；precision/batch/concurrency/SLO Not Disclosed。成对项引入 O(B²+BNr) kernel work及reference编码驻留，随批大小改变 proposal coupling；不从局部图像质量外推视频一致性。

actual MULTIMODAL-GENERATIVE-PARADIGMS Ch24 已读 DDPM sampling/原 guidance 邻接131–188、guidance替代分支242–264、对应术语/正文检索：现有CFG/capacity差分、history EMA、latent diversity proxy与temporal方向约束，但没有以 finite reference population 的 attraction/repulsion 取代 surrogate 单样本条件梯度并采用 prompt×latent kernel 的接口。拟在 guidance 替代分支中、history-reference段后窄增一段，说明 reference population/编码/核和 batch 是 sampler state，集中界不是最终分布证书，reference稀疏或净质量失配回退原CFG/专用适配与更大已验收reference。不是新写“万能MMD”节或照录theorem。

## 2601.08773v1 AST GraphRAG — 3+1+2=6；纠错深入，拟 Ch76 窄差额

§5–6构造/Alg1与code、§7–9/45问题三repo、§10/11、§12/14必要反侧已实际读。相同 Java repo 的 No-Graph top10/1000chunk/100overlap、LLM JSON graph、Tree-sitter typed injects/extends/implements 与 InterfaceConsumerExpand 比较；LLM pipeline batch字符串截断/class_name map gate embedding，377 skip 不能单独归因LLM随机机制，也非所有静态语义已证明。Shopizer coverage0.641vsDKB0.902、43/45 human coarse correctness是局部条件，ThingsBoard向量与DKB都14/15。图边语义/数量不同，节点数非完整率；独立filesystem denominator/uniquepath/schema failure计数尚未完善，人验无inter-rater，重复次数未披露。Reflection/runtime generation/dynamicdispatch是AST反侧，局部价格与buildtime绑定Gemini provider/此repo workload；hardware/precision/concurrency/SLO Not Disclosed。不运行实现。

actual AGENT-RAG Ch76 53–71已有parser/chunker identity、AST dependency closure非完整静态语义、ingestion compiler/freshness；1049–1067已有图遍历/claim citation不授关系真值。但未把**在结构化抽取成功前提下才embedding的pipeline**的corpus shrinkage与较低DB构建费用分账，也未规定原始发现manifest独立于derived graph。实际在ingestion compiler段后窄增63一段，root完整57–78与末注POST通过：独立source manifest与解析/embedding/graph身份对账，缺图不静默删除原语料，费用/语义权限分开。不照抄377数字进书，不授AST完整性或单LLM因果。原repo当前web空shell不能说明目录空；API实际createdDec30，窗前最后exactSHA dc06934ec2cade8a9067e6f6404a53bed299bc46为Jan13T17:34:38Z，递归42paths未截断，code/JSON/log/PNG/requirements无MD/PDF/tex完整本稿信号；Dec29 logs是artifact线索非论文public证据，root允许本次arXiv事件按已核Jan14限定继续，不遍历所有commits。

## 2601.08325v1 ActiveVLA — 2+1+2=5；具体输入接口 gap 深入，拟 Ch26 窄差额

§3.1–3.3/§4.1–4.2 Tables1–4/§5、real robot Table5与Appendix3训练已实际读；原项目全文可见明确 virtual cameras，未见更早dated论文/项目body信号。已观察 calibrated RGBD pointcloud→3 orthographic render→PaliGemma heatmap定位critical3D ROI→sphere candidates按LOS/distance/diversity选择→缩FoV虚拟zoom→heatmap backprojection→action head。主动**虚拟重渲染**不是新传感器观察或物理camera action，未知背面几何不能由重排观察取得。每候选全空间diversity求和不证明最优set diversity；collision flag是prediction非shield。Table4同组件添加支持local取舍：RLBench87.6/.26s→89.4/.45s→91.8/.53s；views>3与过zoom收益饱和/损context。不能把全体系vs不同baseline归因virtual选view唯一因果；GemBenchL4仅1.2且落后3D-LOTUS++17.4，真实四任务报告不是开放物理安全。主实现8H100/eye-to-handD455与Appendix顺序RLBench16H100/90K、COLOSSEUM16H100/90K、GemBench32H100/50epochs、真实8H100/400epochs分别记录；非整体frozen VLM，SigLIP与tokenembeddings冻结，其他文字未完全统一，故不采冻结整个backbone保证。precision/controlfrequency/fullSLO/realtrialcount Not Disclosed。

actual MULTIMODAL-EMBODIED-VLA Ch26 65–73：calibration/frame/uncertainty与physical future-flow activeview已有，TSDF渲染BEV供viewID/2D坐标的接口也已有，但未表达**同一观察 revision 的虚拟视角与局部render resolution预算**不同于real new observation。拟在physical activeview段后窄增一段：coarse3D目标提议→虚拟render/zoom是表示采样预算，保observedpointcloud/calibration/ROI/view/FoV身份；变换不增加未观测信息，zoom过强丢context、render/model双遍计费，无法定位/深度失配需真正重新观测或传统controller。不写模型名称库存，不复述主动视觉一般原则，不授论文线上controller/安全实现。

## 2601.08273v1 HIPPO — 2+1+2=5；标准完成，拟 NoChange—Existing

§3.2/4/5.1–5.2/§6–8、AppendixB/C/D必要配置已读。global target attention＋temporal adjacent cosine＋crop pairwise variance各frame z-normalize，保10%视觉tokens，static重要性/positionbias反侧不由attention alone修复；σ=0处理未披露，不授semantic保真。parallel prefill利用target较长vision阶段bufferdraft；lastbatch全部accept则optimistic下一batch overlap，否则先验首token并可取消restdraft。成熟PEARL并行原则不计Design/Reach新分，discard‘no additional cost’仅criticalpath隐藏、仍消耗算力/内存/争用。

4H200140GB、batch1、greedy固定256outputs，draft7B/target32或72B，同环境modelparallel4GPU；LLaVA64/128frames（196×frame），其他调整FPS至comparablelength；audio不prune；torch2.8/transformers4.57/CUDA12.8，precision/concurrency/SLO Not Disclosed。AppendixC 10VideoMME、videoSALMONN2+7/72平均164.84→58.82s含targetprefill33.71两组不变、decode131.13→25.11，draft2.79/23.77及prune.11overlap，不能外推高batch吞吐或省掉prefill；作者没测质量因自称lossless，本报告仅记录greedy target验证理论权限，未核代码/同序列分布，MAT跨连续全accept累加非普通单轮draftdepth。本文没有正文直接更早项目稿链接信号。

actual INFER-SPECULATIVE-DECODING Ch48 L204已明确同路径target guidance/correction后失效、743–745异步prefix/version可取消proposal与低acceptance费用、955–963视觉预算影响grounding/acceptance、target保完整视觉/verification authority、prefill与decode分账及failurefallback。HIPPO的具体heuristic与上轮accept切换在这些长期机制已有承载，受限独立局部验证不改变长期选择；拟 NoChange—Existing，报告保局部greedy性能与没测质量/高batch限制，不为新方法名添加段落。
