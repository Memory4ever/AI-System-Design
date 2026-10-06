# 新四项必要原源（作者已读，待 root）

更新：PointWorld官方run20761798422及exactSHA e55cb6915faafb983ec628da44148add97b9a651原HTML由root fresh GET实际核，shared3D state/action/FK机制≤Jan06T21:00:05Z公开，上界窗前关闭，不代表全arXiv结果均旧公开。Hummingbird必要原源/具体owner已root通过，实际写165/167两段及355源注，jan01_v3实际正文/邻接/源注POST通过，窄锁释放。IntroLM/LayerOrder仍ordinary待独立核；本文件不宣称日级通过。

原分6/6/7/6已 root 完整题摘准入校准；当前不是 Evidence/Books 通过。必要原文见 NECESSARY_CORE_3_RAW.txt。v1 exact、原公开区间见 DATE_BASIS，PointWorld 的项目此前公开另定点核，不能先写Books。无代码复现/部署。

## Hummingbird2601.04071v1，2+2+2=6

实际 §4.2/4.3/4.4、§5、§6.1–6.3：低优先级 kernel 按block grid拆分，PTX注入offset保原blockIdx；offline/runtime profile选择可饱和SM/带宽的最小子kernel；host API patterns/event指认bubble，kernel-tick按预计执行减launch延迟投递、保持队列至多一项；大bubble合并回原kernel提高效率却重新增加突然arrival的等待。**这是在合法边界主动停止后续launch，不是中断任意running thread/闭源库 kernel 的硬件抢占**。§5明确cuBLAS/cuDNN PTX不可得，替换CUTLASS；cross-block sync/persistent kernel不拆，需source refactor/原路径。因此µs预emption必须绑定可split与queue/profile条件，非任何kernel/任何GPU硬保证。NVLink页offload另有HBM contention、LP-only eviction和DRAM回退，不能由计算分享授地址/故障隔离。

§6 A10080GB/SXM4、CUDA12.6/Ubuntu22.04、禁DVFS，llama.cpp INT8 BurstGPT replay为HP Llama8B/Yi34B，LP Mistral7B/DeepSeekMoE16B batch32、GPT2 batch16与RN101 batch64；SLO是exclusive P99 TTFT/TPOT阈值及attainment，非任意生产请求合同。LithOS因闭源由作者重建三组件，并非原artifact实际运行。切分单独使LP慢37%，consolidate/tick再回收；多GPU16A100 Llama405B/GPT2与L40S/H100另protocol，不混成唯一headline。核心未披露请求输入输出长度/并发完整分布，不授全ServingSLO/无限并发。代码未跑。

具体gap提案 PLATFORM-GPU-SCHEDULER / Ch63:153–170 GPU Sharing：现表time-slice/MPS及fault分责没有“可合法split的最小执行量→等待边界→tick队列→bubble合并取消细粒度边界”链。拟表后/故障域段前≤2段，先承接旧temporal sharing为何被longkernel阻塞，再解释PTX/grid与profile/queue条件、合并代价、unsupported原kernel/独占回退。Ch49:112–137已有persistent execution/task粒度，但不重复其模型executor，把底层合法性作为runtime履行sharing契约的前提；Ch62/64入口交接已读。等待 root 具体证据/owner/窄锁。

## IntroLM2601.03511v1，2+2+2=6

实际 §3.1、§4.1–4.2、§5、§6、AppB/C/D1。只append [CPX]于prefill尾，M mask令LoRA仅对特殊token生效，base prompt路径冻结；生成从原prompt最后token初始化，**[CPX]不进入decode KV**，不是append后正常decode仍见它。q/o/FFN适配但K/V不改，head/embedding可训练，保持的是该接口条件下原生成路径，不声称实现已独立核或任意batch数值完全一致。小模型prefill永远先付：留本地则复用prompt KV，升级则大模型再prefill，不能当决策前免费router。

AppB prompt-level80/10/10，QA Llama3.1-8B judge对gold semantic-match，Hotpot同judge，chat Qwen2.5-32B分≥8且丢history/100k英文；success target是任务/judge/解码版本条件人口，不是复杂度或真正确率的普适尺度。AppC Qwen3-8B、2048ctx、batch64、rank32/α64及分类器/adapter训练，DeBERTa184/435M不同容量/训练batch16，不能把更大模型胜baseline全归CPX。Table4 FFonly与full近似，Table3/4局部消融非全因素。§5.3 reliability把所有升级视为正确，只统计small错路人口；latency用vLLM/两H100/Qwen8B-32B TTFT/TPOT代入平均长度公式，BERT公式未含独立classifier额外时间，故不采完整部署reliability或端到端matched-speed数字。Limits明确训练比轻量encoder贵，不授无成本。

具体gap提案 INFER-SCHEDULING / Ch56:1016–1018 answer前反事实效用后≤1–2段：外部query classifier合理低成本基线→prefill内特殊token局部适配、KV排除/复用与升级重处理→原路径保持和预测权限独立、校准与fallback。现正文有model-profile/反事实score分责，却没有这份prefill artifact/branch成本合同。只此新增接口，不复制指标数；待 root 必要原证据/ownergrant。

## LayerOrderInversion2601.03542v1，2+1+3=6

实际 §3.1–3.2/§4.1–4.3、Limitations。MQuAKE至四hop，GPTJ6B/Llama3-8B greedy；按allatomic+multihop正确筛Correct人口，Incorrect为atomic全对但组合错，Missing另一人口。Patchscopes将指定layer/token hidden送至解释prompt，三次probe聚合；GF/LF按解释与query相似度删bottom比例，包括90%过滤，保raw与filter而不混分母。Table2/§4.2中3/4hop末token final entity可比subject bridge更早decodable，2hop未见相同反转；只反驳“该探针的layer解码次序普遍按hop递增”。subject/last不同坐标、解释prompt、filter/selection都不能授真实recall先后、extract causal机制或原任务必要计算顺序。§5概率/attention机理没有targeted causal validation，作者Limits明确attention hypothesis缺comprehensive验证，不采用该功能解释。无neural训练/硬件性能headline；不机械要求此观测理论负侧统一GPU模板。

具体owner核到 WORLDVIEW-LLM-INTELLIGENCE / Ch8:262–268“记住两个事实不等组合”：已有受控两跳桥state电路故障条件，但文字‘组合成功要求...后层读取前层bridge’不应外推所有pretrained QA按可解码桥实体逐层串行。拟原受限桥state段后1窄段：可复用中间状态是可验证的一条组合分支，probe可解码顺序≠hop/因果计算顺序；固定position/probe/filter与已答对条件人口再比较，不由layer-order inversion否定所有composition；保持旧受控机制，不把概率/MLP/Attention功能标签写入。需要 root 必要原源和具体owner判断后才写；Ch7/9相关入口将按授权再核。

## PointWorld2601.03782v1，2+2+3=7

实际 §3–4、§5.2–5.4及A1/A5/A6受影响内容：state为RGB-D回投scenepoints，action是已知URDF/joints FK传播的gripperpoint轨迹（300–500/夹爪），共享metric空间不共享物理执行权；correspondence仅一forward imagination固定，跨新capture需重建。H10/每步0.1s，DINOv3 features与robot temporal embedding concatenation→displacements；GT movement weighting/visibility与uncertainty/Huber均有标签条件。Wholebody-flow未必胜lowdim；sim-realzero-shot仍困难，细grasp/薄物与calibration/occlusion限制。A1明示static initial/no velocities、robotrigid FK已实现路径假设、environment action correlation非causalstructure、无photometric变化。A6 planning256候选×20迭代、30step/3forward、数秒，**实测不执行replanning**；pregrasp deformable/tooltasks、GUI手定pointgoal、IK/controller/workspaceclip，8task每10初始化、安全不执行算failure。0.1s模型forward≠实际MPC control SLA/安全。

§4正文real evaluation expert只训test过滤，写保留top80% points；A5 threshold0.8quantile/低于阈值outlier，即字面保留top20%，人口口径冲突精确保留，不能授reported mover-error或noise robustness的无条件评价；固定mask跨model可比不补gold真实性，巨量points相关不能直接授独立SE。只采用提出的geometry/action接口及明示条件，不授模型是全物理state/通用控制安全。

Ch25:157–165 action-conditioned schema段已有joint/URDF/camera/timing video统一conditioning，不等shared3Dpoint encoding，若本窗身份成立可拟其后一窄两段：观测scene部分可见vsFKrobot已知geometry→保contact支持但actuation/tracking仍外部；motion/time/calibration/correspondence、staticinitial/appearance成本与专用dynamics fallback。**官方project历史部署出现Jan6 successful build原线索，正在定点核exactsha当时方法，未授Jan09首次，暂不申请写锁**。不是用repo创建时间或commit时间直接当first-public。
