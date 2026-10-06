# 本日贡献判断的有限补读

## 2602.15539 DynamicFusion — 一次决定core，root限定准入通过

actual[exact-v1](https://arxiv.org/html/2602.15539v1) §4–5/Tables3–5：并非摘要的连续“自适应融合权重”，Eq13逐layer硬选KL扰动较大的subject或style分支；相较K-LoRA权重幅度静态选择，新增输入/层/denoisingstep相关的执行选择，而非仅两个成熟模块并联。Table3拆FLS/LLR：FLS单独DINO40.1→43.7但style60.3→59.5，LLR单独style66.1比联合64.0高，显示内容/风格目标冲突与动态selection作用，不由best总体图背书。拟2+1+2=5只该选择条件，CLIP/DINO梯度是成熟guidance并非独立增量。KL用于feature前未说明probability normalization且原feature可非概率，不能采用严格信息论解释；training-free仍需双LoRA参考图/每步encoder梯度，成本与采样模型scope需必要审阅。保留反侧，不因核心含糊无限附件。

## 2602.15543 SelectivePerception — 一次决定core，root成熟组合EX通过

actual[exact-v1](https://arxiv.org/html/2602.15543v1) §III–IV：router在ViT之后，以wristtokenmean+promptattentionpool预测softmax权，Eq4只乘全部已编码feature再channelconcat/project，没有跳过view encoder、裁token或实测latency/FLOPs；不能采用摘要按task相关省compute。实作是成熟contextgating+FocalLoss稀有标签+history-aware VLM标注的VLA组合；wrist+prompt比external+prompt更高SR（83.33vs73.33）和rawstate噪声反侧，仅三个人为需要thermal/tactile阶段任务各10trial/50demo，未识别新的view可省条件、执行接口或contextgate成立边界。因此拟EX的理由是实际增量止于该组合/任务验证，不是因没有实测cost或证据弱；noRouter多模态10与gated73.33是bundle验证而非无学术价值。headline省计算纠偏保留，VLM83.33vs人工86.67非独立等价证明，failedgrasp/transport仍在，不授安全。

## 2602.15485 SecCodeBench-V2 — 一次决定core，root贡献EX通过

完整v1题摘及[exact-v1](https://arxiv.org/html/2602.15485v1) §2–6实际定点读。新内容是98 industrial scenario/22CWE/5language题库，function scaffold固定接口、先function再PoC/security及不能dynamic判定时多judge多数票、默认功能失败retry3、10round Pass@1与severity/scenario加权；这些是成熟安全测试分账和工具实现，没有提出新的oracle成立条件、受控反证或改变既有securecode评价判断的盲点。§6仅可用用途，没有具体跨模型结果或揭示新漏判路径。故不因V2/工业安全标签或题库扩量准入；不是因证据弱EX，而是决定core确认增量止于题库/成熟pipeline。Threats声明passingPoC≠无其他漏洞、多judge≠formalabsence保留为安全headline审阅边界；不继续全例子/日期恢复，不把Docker隔离宣称host无风险保证。

## 2602.15400 GTA — 一次决定core，root接口贡献准入通过

实际[exact-v1](https://arxiv.org/html/2602.15400v1) §IV与V-C决定核心：持续TSDF metricstate独立于MLLM，pose/time/extrinsic标定的四正交views+BEV覆盖normalized0..1000 grid，MLLM只输出viewID/coordinates，raycast回TSDF真实waypoint交localplanner；相比预设textmap，新增的是无需continuous regression head的表示→coordinate decode→metricgrounding接口条件。不是metricmap+planner名字本身；拟2+1+2=5。物理有效仍依赖图与localcontroller，不由semanticreasoning拥有碰撞真值；loop countalert不是安全保证。

V-C有with/withoutEWR across agents的局部机制比较但bundle未拆四view/grid/graph，PB45.0→47.2SR只是curated180trajectories；模型swap三点不证明规模因果/未来必然更好，OSR不能替stop成功。以下待必要setup/表协议审阅，不因实作受限EX；若root认为这个新增interface条件只是成熟组合则具体关闭，不默漏潜在metricgrounding贡献。

## 2602.15473 POP — 一次scope核心，rootEX通过

完整v1题摘、[exact-v1](https://arxiv.org/html/2602.15473v1) §2–3/8–9实际读。原增量synthetic quadratics/RBF-RFF prior+PPO训练coordinate step policy用于47一般函数优化；§8明确application to ML tasks留future，MLloss landscape prior需另设计。未建立模型训练/学习机制的新成立边界；能映射optimizer或使用policy network不足。GP/RKHS prior支持任意compactfunction的引用标准universality也不证明learnedoptimizer泛化或模型loss新理论。拟本项目范围EX，不因benchmark弱/尚未读附件排除，不追补日期。

## 2602.15488 KHI — 一次scope核心，拟EX待root

完整v1题摘与[exact-v1](https://arxiv.org/html/2602.15488v1) §1实际core：attribute-space KDsplit+HNSW nodegraphs/in-range neighbor routing为一般vector数据库numeric range ANN，例子scholarlysearch year/citationrange；虽引用RAG论文，没有foundation/RAG接口、modelrepresentation条件或训练推理增量。与15423同范围门槛，不用索引可映射Ch76/cost类比准入，也不否认一般索引研究价值。具体skew-height/logn与QPS条件保留发现，不为EX追日期/完整index实验。

只补决定准入的原文，不因宽库存或已取得HTML而自动全文排队。日期下界/同身份上界仍独立核，当前摘要只用于发现。

## 2602.15809v1 — 排除贡献，不追补日期

完整题摘及[exact-v1](https://arxiv.org/html/2602.15809v1) §2实际读：SME gold dataset、Kappa与correctness分开、RQ-VAE第一层256码coverage、JSD与XGBoost inverse-propensity补采样、policy/dataset immutable版本。新增是Pinterest将这些既有方法用于内部审核数据维护，原文明确图2未量化成本/规模/质量取舍；决定核心未给新的判定机制、成立边界或足以修正本项目判断的受控反证。并非因现有Books有topic而排除，也非机构应用一律排除：这里原文实际增量尚不足改变设计选择。旧V2.1的8分/Existing结论不继承。

## 2602.15423v1 GaiaFlow — root范围校准排除，不追补日期

root实际读题摘、§3performance-positive和§4PISA/MSMARCO后纠偏：实作是一般lexical/index retrieval配置搜索，intro虽然提RAG/LLM碳足迹，没有foundation-model或RAG实际接口，也没有改变LLM设计的具体命题。不能由可映射cost/解释性系统类比准入。以下已读机制与评价保留，但不评分、不当本窗候选或Books依据；不是因弱benchmark而排除，不再追补日期。

题摘的笼统carbon优化不足，实际有限补读[exact-v1](https://arxiv.org/html/2602.15423v1) §3–4后发现具体增量：纯lexical query邻近不保证适合相同执行配置→按同configuration的recall差<1%定义performance-positive，并把query–configuration attraction加入latent配置搜索→需要比较语义邻近与实际performance条件的配置选择。并非只因Langevin/early-exit/quantization组合而准入。

§4.1–4.8实际已读：MS-MARCO v1 dev 6980、PISA BMM k1000、单logical core、Intel Xeon Gold5118/AMD EPYC7402P，5runs。Table3 γ2=0对完整9.9vs9.0ms/7.0vs6.1steps、recall .857vs.859是有限局部对照；预建index/预处理query、cache fastpath比例、latent模型训练和完整搜索成本未分账。Table2部分ratio与latency除法不一致，采用原ms不采用错误ratio。Carbon由Mop/Flop线性模型和PUE估计，不当直接测排放；§3.3 Pearson>.98不是点对点monotonic certificate，不能采用“保证”标题。核心机制可以受限评估，理论Appendix仅在欲采用其保证时定点补核，不能把未核理论宣传授权为Books。Books待actual owner；不授全硬件/生产收益。

## 2602.15384v1 WAC — 潜在准入 2+1+2=5

root已实际核Ch80 L60–88、Ch79 L217–230，Existing通过：AGENT-REFLECTION，有限再提案/历史best与unresolved条件由已有正文具体承载；无Books改动。

root已实际核原core，5分具体接口差额准入通过。实际Books比较：Ch80 L60已承载低分定点重生/回退、保留已核前缀，以及预算耗尽best强制前进不能继承verified；L72是执行前重写理由—行动对且judge不拥有权限，L74–88把逐constraint反馈作为下一轮控制信号；Ch79 L217–230则现有simulated observations/候选预算与真实commit分责。WAC低分rationale回灌proposal及Kmaxbest的有限实现未改变这些已有论点，拟Existing以AGENT-REFLECTION/Ch80 L60/72/74–88为owner，Ch79只交接。不写新WorldModel路线或安全gate。以上actual owner/pre建议待root核，不是自行授Existing。

完整v1题摘、[exact-v1](https://arxiv.org/html/2602.15384v1) §3–5实际读。仅simulation再择优的旧机制在全部候选不好时仍被迫选一项→原文把低分candidate/rationale回灌proposal并保留历史TopN、最多Kmax轮→具体选择是重新提案而非只扩初始sampling。这条接口差额可核，不因WorldModel+Judge成熟就预排。

Horizon1、同Qwen3-VL-Plus/temperature1、VWA233/OnlineMind2Web300；主要SR22.7→24.5/14.7→16.0，Classifieds56累加模块32.1→33.9→35.7。Table5单初始proposal仍35.7，未匹配整体calls/tokens/latency或给重复run区间；不是因果效率证书。Judge scores {0,.5,1}不是概率，Kmax后仍执行历史最高分，绝非fail-closed safety gate；simulate是文本且作者§5承认真实环境失配。局部接口与反侧足够标准必要审阅，若Books有实际长期差额再受影响深入；不授生产安全/执行许可。

## 2602.15391v1 Adaptive abstention — 决定核心与安全信号保留

root实际核已有必要正文/A/B后校准：准入主张只剩固定detectors、domain/trust线性threshold及cascade的成熟组合，原文没有新增可采用的机制/成立条件或受控反证来改变本项目设计选择。现已明确EX；不是因为实现证据弱而排除，也不借安全标题升级无限阅读。以下score/timing/benchmark反側已实际处理保留，不授宣传guarantee，不为EX追补日期。

完整v1题摘及[exact-v1](https://arxiv.org/html/2602.15391v1) §3–5实际读。原文具体机制为5固定detectors+domain/trust线性threshold和4级cascade；未把成熟组合自动判新增，也未因缺实验细节预排。安全headline须处理：Eq5 .7×1+.2×5+.08×20+.02×50=4.3ms描述exit加权，但前级累积cost没明示；实Table2 42.78ms并非同一模型。score方向不统一，Eq6 confidence低分abstain而Eq2混perplexity/entropy/variance作正项，未披露归一化与反向transform；部分detector先需生成完整candidate，cascade不是省掉LLM生成。

§5 strict precision .5/recall1与adaptive .95/.98分属不同人口/设定，不能合成安全保证；Guardrails是simulated、450ms baseline身份/hardware/baseLM/config未唯一给出；RealToxicity600与mixed1000、domain synthetic未给足复查split/labels。正文仍声称safe guarantee与全部loop100%，而限制承认benign-language jailbreak逃逸。需要定点读必要implementation/validation是否补足，之后决定实际贡献或中心主张暂缓；尚可读的附录不作外部缺口，不授性能/安全或Books。

后续已实际读AppendixA/B全必要块：A1只给五base阈值与domain加减，A2生产10000 exit-rate文字停在“70”，B1只有10-trial聚合JSON，mean42.78/std18.37/no-cascade118.26/speedup3.24与主表10.5属不同baseline；B2仅说figures目录未指明repository身份。没有补足baseLM/实际score归一化方向/匹配timing，这些不是尚未读完。root已按完整决定core校准成熟组合增量不足准入，EX通过，不把弱证据直接改判EX，也不采用其安全/性能headline。
