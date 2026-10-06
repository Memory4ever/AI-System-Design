# Jan29 supplement — necessary-source / owner PRE

以下四项准入已由 root 完整题摘校准，不预授 Source / PRE / POST。每项原件是本目录 `supplement-primary-<ID>-20261008.json` 的 exact-v1 HTML 原文（`.text` 行号可用 `jq -r '.text' | nl -ba` 恢复）。5分三维均为2+1+2；由于具体长期差额，受影响内容深入审阅。不采用未审附件，不声称运行代码或复现。

## 2601.19399 — RT-MAE

2026-10-08恢复：root非作者 actual POST通过。实际读精确v1 §2.1–2.3/3.1、Table2与τ消融，Ch23正文158–174完整邻接及自身末注1534；确认两段属性+残余接口、整组dropout/identity leakage、代理N-MOS/有限语音边界、费用与原encoder回退一致。不采用MᵀV维度式或strict disentanglement。此为本条实际写后结果，不替本日Source覆盖或DAY验收。

必要位置：§2.1–2.3（text230–346/419–446），§3.1（452–509）、Table1（349–418）、Table2/解释（541–606）、τ消融/音高控制（619–651）。噪声扩展652–703仅作边界，不采用通用分离保证。作者先以有限显式pitch/loudness/speaker/PPG控制语音，再让固定25×512连续query从Mel提取残余tokens；整组dropout（τ=.5）限制残余路径绕过属性。τ=0丢控制、>.8趋向属性独用。Table2属性/残余双用STOI .82/代理N-MOS4.32/COS.92，残余独用.50/3.04/.72，身份仍可泄入残余，不能称严格互不重叠因素。Table1正文对EmoV基线N-MOS/COS数字与表格不一致，采用表格而不照录段落；不采用§2.2的M^T V维度式作已核实现。训练LibriSpeech360clean、4A100、batch128、AdamW400epochs、6+6Transformer；指标包括预训练模型代理N-MOS而非人工MOS，无独立seed/CI或推理精度/延迟/SLO。

实际 owner 比较：Ch23 L159–173讲codes/stride/fidelity、COMiT有限状态重新分配、LatentUM理解codes与像素decoder分责；L149–151讲audioencoder/readout不同信息。均未承载“属性+未命名残余双接口、整组dropout防绕过及残余泄漏”的具体机制。拟插Ch23“quantization error...codebook governance”段后、COMiT固定message段前，两段如下：

离散 codes 的另一种取舍，是不要求有限的可命名属性解释全部信号。先保留 pitch、loudness、speaker 或 content 等显式控制，再用固定数量的连续 queries 从原始声学表示读取未覆盖的变化，让属性与残余共同条件重建。残余预算越大越容易保真，也越可能绕过显式控制；训练中整组关闭残余、迫使属性独立重建，可以把“能重构”与“按属性控制”放回同一个约束，但残余并不会因此成为语义纯净或互不重叠的因素。<!-- source-family:SF-2026-ARXIV-2601-19399 -->

[RT-MAE 的有限语音对照](https://arxiv.org/html/2601.19399v1)中，不关闭残余时模型忽略属性，关闭概率过高又丢掉残余收益；残余独用仍保留部分 speaker identity，因此应分别验重构、属性编辑与旁路泄漏，而不由更高自然度代理分数认证 disentanglement。25个512维tokens、声学前处理、MAE与vocoder都付费，有限LibriSpeech/EmoV及音高移动只支持这一训练接口，未证明任意属性可控、免费codec压缩或实时SLO。属性足够、必须独立编辑或预算不足时，保留属性独用与原encoder/codec，并把残余数量、关闭策略、控制器及decoder一起版本化。

## 2601.19740 — training-free GMM diffusion

必要位置：§2 Assumption1/Eq20（text1897–2092），§3 Assumption3（3365以下），Theorem8（8721–8792）/Theorem9（9115–9170）及§3.3（9942–10139）；§4.1（10233–10731）与§4.2（10732以下）。共享协方差SPD GMM平滑经验分布给精确score；终态总误差分数据近似、ODE离散和随后MLP拟合。Theorem8 E||error||2≤Cdh仅在均值L2半径M、谱上下界固定的假设下；C不依赖d/h但依赖M/谱，不能忽略这些参数随维数变化。Theorem9 L∞≤C(ln d+1)h额外要对角Σ。§4.1用1000条轨迹、Heun h_ref1e-3作reference；L2均值球内，L∞改cube[-M,M]^d且维数试验用fullSPD，与所述L2半径/对角Σ条件并不全同，因此只作受限经验趋势，不认证Theorem9在该人口的保证。§4.2维8–8192、10 modes、10万样本80/10/10、5随机切分、两层MLP1024或2048；拟合误差可比ODE误差高1–2数量级，不由更多Euler步承诺终态收益；无真实媒体质量或部署成本。

实际 owner 比较：Ch24 L294–300已有reversekernel表达/terminal mismatch分责；L322分函数近似/导数近似/solver误差；L1216–1218为离散MASK流程，不是本GMM。尚无“可解析score先分离solver，再压缩成单map时重新付fit误差”的具体实例。拟插Ch24 L322 Jacobian误差段后、blinddenoiser段前两段：

若数据能由平滑的 Gaussian mixture 表示，还可先用其解析 score 构造 reference flow，把学习 score 的误差从求解器诊断中拿掉，再由生成的 noise–sample pairs 训练单次映射。这里 training-free 只描述解析 score 路径，不描述后续 neural map；需要分别记录数据近似、有限步积分和压缩拟合误差，不能用 reference solver 更准替最终映射放行。<!-- source-family:SF-2026-ARXIV-2601-19740 -->

[受限 GMM 理论与实验](https://arxiv.org/html/2601.19740v1)的 Euler L2界依赖固定均值半径和受控协方差谱，L∞对数维数界另要对角协方差；常数还会随小特征值恶化。部分L∞试验改变了均值人口且使用full covariance，不能继承该定理的完整保证；拟合单map的误差又可主导积分误差。GMM密度近似、每步mixture求值、reference采样和MLP训练都计成本，维数趋势不认证媒体质量或部署SLO。数据近似或谱条件失配时，保留learned score、更多步/既有solver与独立终态评价；需要压缩时单独验收fit误差，而不是把“无需score训练”写成无需训练或无误差生成。

## 2601.19535 — LURE-RAG

必要位置：§3.1–3.5（292–1003）、§4.1–4.3（1004–1461）、Tables2/3/结果（1463–1738）。§3.2（407–473）定义utility为gold与单context生成答案的task-specific score（例F1/Exact Match），§4.3（1325–1462）说明Accuracy/F1及模型/配置；Fig1 caption（285）另写LLM posteriors，未披露足够实现对齐，不能把gold-answer posterior标签写作已核实现。采用“单context输出按下游任务分数造效用标签”的最小接口，LambdaMART lexical/LDA features listwise排序训练；固定BM25/Contriever黑盒backend。改造RePlug仅保KL objective训练reranker，不是原始端到端RePlug比较。UR-RAG用SBERT同labels+ranking isolation更好；LURE只有相对dense KLbaseline接近，不能把所有差额唯一归LambdaMART。NQOpen/TQA、Wiki2018/100word，Phi3标签迁Llama1B/Qwen14B，后者结果不授全modeltransfer。§3.5明确单doc独立打分却testpack多doc，交互dependence未来工作；排序效用不是真实supporttruth。97–98%只有限QA结果比例；未提供端到端matched硬件/precision/batch/SLO的成本证据，不授通用更快。

实际 owner：Ch76 L79–81具体queryvariant的nDCG/answerutility错位，不承载document-side单contextutility蒸馏listwise轻reranker与multi-doc依赖的接口差额。拟在该两段后、黑盒多query verifier段前两段：

Document-side 也可把固定 retriever 的相关性排序改为下游 reader 条件下的效用排序：离线让每个候选单独作为 context，用生成答案的下游任务分数造标签，再把这些次序蒸馏进 listwise reranker。这样不必在线为每个文档调用 LLM，也不必刷新 retriever/index；但 label 绑定 generator、prompt、评分协议和目标任务，答案分数更高不等于文档具有事实支持。<!-- source-family:SF-2026-ARXIV-2601-19535 -->

[LURE-RAG 的有限QA对照](https://arxiv.org/html/2601.19535v1)把该label交给lexical/topic特征的LambdaMART，并以dense ranking变体对照KL训练的改造baseline；它支持局部质量—ranker容量分支，不证明原始RePlug或完整RAG成本被普遍改进。单文档训练效用没有建模多文档互补与冲突，标签生成、特征/topic建模、ranker训练与在线重排都付费，跨model结果仍限受测reader。证据组合重要、标签迁移失配或净收益不足时，保留relevance/hybrid、原reranker及独立support核验，不让utility次序取代证据充分性。

## 2601.19551 — scale-consistent FROST

必要位置：§3.1–3.3 stationary/contractive条件（609–1375）、§4.1–4.4（1376–1654）、§5（1655–1950）、§6.1–6.6（1951–2579）以及AppendixD仅受影响collapse说明3945–4087。不同于原报告attention冻结FROST2601.19001。本篇共享stationarySSM沿depth，scaleconsistent中间表示、batch×time taskloss rank监督halting head，KLL经验quantile跨batch历史阈值；taskloss仅最终迭代反向，head有独立/绝对正则，原文自称隔离backbone。理论stationary contraction不等于任意非线性backbone天然满足Lipschitz收缩；几何proxy不是completefractalcharacterization。ImageNet100、ResNet50/ViTbase16最大16/12步；对照尝试同halting失败collapse因而按full depth报告cost，不能当严格matched共同可运行stop策略。RTX3090 throughput在q=.5，ResNet参数额外且另一haltingbackbone存在mutualcollapse，不能称全结构稳定；需保留expressivity/largerscale未验。

实际 owner：Ch17 L594 fixedpoint refinement拥有solverconvergence/L602–608区分latentmotion与任务正确，未具体拥有跨中间depth的taskloss ranking→historyquantile stop接口。拟在fixedpoint marker2605-12466后、recursive-depth诊断小节前两段：

还有一条不求fixed point的停止分支：先令共享变换的不同depth状态保持可比较的表示几何，再用训练batch中各sample/iteration的taskloss相对次序监督独立halting head，推理时以历史score分布的经验quantile选择阈值。它把中间表示的可比较性、停止score与部署预算分开；quantile只校准相对顺序，不把低loss rank或高停止score认证为本请求答案正确。<!-- source-family:SF-2026-ARXIV-2601-19551 -->

[FROST 的有限图像分类实验](https://arxiv.org/html/2601.19551v1)用 stationary SSM 细化实现这条分支；正文脚注的“contractive”指插值权重 λ，不是 Banach 收缩定义，λ 小于 1 本身不能保证任意非线性变换 A 收缩，几何 proxy 也不认证所有 backbone 的 self-similarity。相同 halting 训练在对照结构上曾 collapse，作者才以全 depth 报告其成本，这不是相同可运行 stop 策略的净收益证明。额外 SSM/head、全 depth 训练和 quantile 状态都付费，还需验阈值漂移、表示 expressivity、accuracy 与真实执行时间。中间状态不可比较、分布漂移或费用不合算时，保留固定 depth、显式 loop/solver 与外部 task gate，不由局部吞吐或经验分位数授任意输入收敛或 foundation-LM 收益。
