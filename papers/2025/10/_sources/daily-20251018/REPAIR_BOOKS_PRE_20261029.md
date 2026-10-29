# 完整写前包（未保存Books，待sole reader整体PRE）

已加载Books三份方法文件、ROADMAP及最新本日路由；实际读Ch22 context-switch/fixed-state与外部工作集1200–1239，Ch28 Future-token83–126及Mid-training1769–1818，Ch24 Equilibrium1507–1524与Parallel Progress2339–2367。以下每项只有一正文段、独立marker、本人source note；reader须核完整内容与当前实际直接两侧，不能marker-only通过。源证据见REPAIR_EVIDENCE；所有收益均作者局部结果，未复现。

## B1 Tool-use改变固定状态的系统边界

owner `MODEL-LONG-CONTEXT`，Ch22 `## 外部工作集`第一段后、现有“RAG、检索、摘要和 memory compression”段前。前段已有“历史保存与模型计算不再共享同一容量边界”，后段讲working set；尚未具体承载一次observe与持续交互的区别/任务轨迹覆盖条件。

正文：

固定状态的限制还取决于什么时候能再次读取外部材料。若一次工具调用后便只能依赖有限内部状态生成完整答案，增加思考长度并不自动恢复已丢的信息；持续的读、写和指针移动则让增长的工作状态留在模型之外。[受限SSM构造](https://arxiv.org/html/2510.14826v1#S2)以有限状态、有效输出支持随任务复杂度增长为前提，区分了这两种交互合同；正面构造还要求合适的memory oracle与覆盖任务转换规则的训练轨迹，不是任意工具接上后SGD就保证无限泛化。合成算术与代码依赖修复支持这种系统边界的选择，却不证明开放代码任务普遍优于Transformer。外存容量、读写调用、训练轨迹与失败恢复仍计入总预算；外部证据不可靠或无法持续交互时，保留显式上下文、可验证检索或更大状态，而不把固定模型内存称为固定系统成本。

<!-- source-family:SF-2025-ARXIV-2510-14826 -->

本人注：`SF-2025-ARXIV-2510-14826` — Schrodinger，Daily2025-10-18补Oct17；exact-v1 §2定义/2.4、B.1–B.2必要构造及§3–4，3+2+2=7。仅有限内部状态与持续外存交互的系统边界；保oracle/任务轨迹/有限状态及合成coding、Hanoi seed边界/全部费用，不授SGD普遍无限泛化或免费系统内存。未核全proof/附件/实现或复现；PRE/真实SAVE/自读/solePOST按本日canonical实际后到记录。

## B2 Future summary是辅助目标而非未来输入

owner `TRAIN-PRETRAINING`，Ch28 Future-token小节第一段后、“关键不是”段前；现有正文只有多个未来token头与梯度路径，没有单个摘要头的目标表示/教师成本分责。

正文：

未来监督也可以先压成一个目标，而不为每个未来位置增加头：从当前prefix预测未来窗口的multi-hot词袋，或拟合独立反向语言模型对真实后缀的表示，再与原NTP共同训练。部署仍只读取prefix，不获得真实未来；词袋丢掉次序，反向teacher则引入额外训练与前向成本，单辅助头不能代表总预算更低。[FSP的受限对照](https://arxiv.org/html/2510.14751v1#S4)按相同语料比较，却不把teacher成本计入等算力条件，而且模型规模、任务与pass@k改变排序。因而应分别验收摘要目标、主头质量和完整训练成本；需要精确局部依赖、teacher不可靠或辅助目标竞争时，普通NTP与短程future-token头仍合理，不能由摘要预测收益批准长程规划或推理加速。

<!-- source-family:SF-2025-ARXIV-2510-14751 -->

本人注：`SF-2025-ARXIV-2510-14751` — Schrodinger，Daily2025-10-18补Oct17；exact-v1 §2/Eq1–13、§4/Table1–3，2+2+2=6，具体摘要目标接口gap必要深入。仅prefix→未来词袋/反向teacher target与部署分责，保非iso-compute/3B与8B排序及GSM8K反侧，不授免费/规划/推理提速。未核实现或复现；实际PRE/SAVE/自读/solePOST见本日canonical。

## B3 Midtraining的时机与曝光量必须同时记录

owner `TRAIN-PRETRAINING`，Ch28 Mid-training中“目标分布小、demonstration可信时直接SFT仍更便宜”段后、“阶段变化还要分开”段前。已有mixture/预算与restoration，但尚未具体分开引入时机、混合权重与累计专用token这一实验混杂。

正文：

混合比例还必须与引入时机一起记录：总训练长度固定时，更早混入专用数据也增加了它的累计曝光量，不能把收益全部归于某个“可塑性窗口”。[一组小模型midtraining对照](https://arxiv.org/html/2510.14865v1#S6)在代码任务中显示时机与比例交互、错配领域收益有限；其纯专用继续预训练还为避免重复数据采用不同起点，因此不提供比例本身的独立因果结论。设计阶段应共同冻结入口checkpoint、混合起点/权重、各来源累计tokens与后续SFT预算，再分别测目标质量及原分布保持；更低C4 loss只是所测遗忘代理，不认证全部能力。混合搜索、继续训练与多路回归均付费，目标或保留能力退步时可缩短/减弱专用阶段，保留直接SFT与原通用续训，而不是靠晚期加量承诺恢复。

<!-- source-family:SF-2025-ARXIV-2510-14865 -->

本人注：`SF-2025-ARXIV-2510-14865` — Schrodinger，Daily2025-10-18补Oct17；exact-v1 §2–6/§7必要，2+2+2=6，具体时机×比例×累计曝光的归因gap深入。70–410M Pythia/C4/128B及五seed SFT局部；保纯domain不同起点、CKA关联/C4 proxy与全费，不反投v2强plasticity结论、不授任意规模配方。未核实现或复现；实际PRE/SAVE/自读/solePOST见本日canonical。

## B4 Causal recurrent-depth也可跨token精炼

owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Ch24 Equilibrium小节末段之后、Editable tokens标题前。现有loop/prefix训练与固定点求解，未具体说明兼容input injection的既有causal recurrent-depth模型如何以wavefront组织跨token精炼。

正文：

递归深度还可以沿多个token交错执行，而不等前一个token完成全部loop再启动下一个：对具有input injection、可解码中间态的causal recurrent-depth模型，wavefront同时保留几个待精炼latent，每轮推进新位置，只冻结连续满足停止条件的前缀。[受限diffusion-forcing sampler](https://arxiv.org/html/2510.14961v1#S3)展示这条免重训分支，KV跨深度共享可减小状态驻留，却不是所有looped模型都兼容；前位晚改变会使后位重新适配，过早freeze会级联放大错误。真实模型未证明收缩，latent变化阈值不认证答案正确或与AR同分布；单请求A100实验中的速度与质量取舍也不外推高并发SLO。prelude/coda重复计算、活跃wavefront、cache与回归全部计费，停止不稳或状态过多时缩窄wavefront、增加loop或恢复逐token采样，保留原causal依赖而非命名成双向生成。

<!-- source-family:SF-2025-ARXIV-2510-14961 -->

本人注：`SF-2025-ARXIV-2510-14961` — Schrodinger，Daily2025-10-18补Oct17；exact-v1 §3/Alg1/Remarks3.1–2、§4假设及§5/T1–2，3+2+2=7。只input-injected recurrent-depth的wavefront/连续prefix freeze接口；保KV sharing条件、收缩未证/级联与HumanEval2.44pp反侧、batch1与全部费，不授AR同分布/双向语义/高并发净速。未核全proof/实现或复现；实际PRE/SAVE/自读/solePOST见本日canonical。

## B5 首层信号复用与当前层依赖不是同一路径

owner `MODEL-TRANSFORMER-LAYER`，Ch17“为什么顺序是Attention再MLP”中“这是一种稳定主流设计，不是唯一可能顺序...”完整段后、Composer搜索菜单段前。已有并行名称与结构搜索，未承载首attention旁路如何改当前依赖/TP reduction的具体合同。writer实际读该完整小节与现有首skip/parallel相关导航；Ch37执行collective不拥有这份结构变更。

正文：

并行化也可以靠改变MLP读取的信号，而不是仅让执行器重排原依赖：保留各层Attention的residual更新，却将MLP输入改为当前层归一化状态加上首层Attention的归一化输出，使它不再等待本层Attention完成。[FAL的受限结构](https://arxiv.org/html/2510.14614v1#S4)因此允许两路并行，并在所测TP布局中先作本地加和再归约；这是需要重新训练和验收的模型图，不是原checkpoint的代数等价替换。另保留当前层依赖、只增加首层信号的质量分支，不能继承同样的通信收益。早层表示复用、训练与多流执行均有成本，较低PPL也不保每项下游质量；信号、任务或执行预算失配时，保留标准串行block或已验并行分支，不由一次归约减少批准全网无损。

<!-- source-family:SF-2025-ARXIV-2510-14614 -->

本人注：`SF-2025-ARXIV-2510-14614` — Schrodinger，Daily2025-10-18补Oct17；exact-v1 §4–6.4/Eq2/T1–2，3+2+2=7。仅MLP读首attention/保当前MHA residual而改变依赖的结构；FAL+另账，保任务反退/需重训及真实执行全费，不授checkpoint等价或通用通信收益。未核实现/全附录或复现；PRE/SAVE/自读/solePOST以本日canonical为准。

## B6 新增空间通道而非挪用文本位置容量

owner `MULTIMODAL-REPRESENTATION`，Ch23 native小节“它不必然优于staged alignment...”段后、“共享表示也不要求每种输出使用同一套末层”段前。已读868–909完整native论证；既有2605-28820的unit mask和分轴位置不承载扩QK/zero-init如何保文本初始化。此不是Ch13通用RoPE频率重复。

正文：

从已有语言权重扩展空间位置时，还要选择新关系使用哪份容量：一条分支保留原序列位置的Q/K通道，额外增加横纵通道并将新增K投影零初始化，再为两空间轴设置独立频率；文本的空间索引置零，图像内部另按视觉unit读取。[NEO的受限设计](https://arxiv.org/html/2510.14979v1#S3)以此让初始文本路径兼容原位置计算，再分阶段学习空间关系，而不是从原通道中直接挪走维度。初始兼容不保证联合更新后语言能力不变，新增Q/K与pre-buffer也增加参数、Attention及训练费用；图像/文本mask与分轴坐标必须一起保存。数据、原语言回归或总预算不合时，保留原语言路径、专用encoder加projector或较小扩展，不把native命名或zero-init当作无遗忘保证。

<!-- source-family:SF-2025-ARXIV-2510-14979 -->

本人注：`SF-2025-ARXIV-2510-14979` — Schrodinger，Daily2025-10-18补Oct17；exact-v1 §3/Eq1–2、§4.1/4.3与A3，2+2+2=6，新增位置容量/初始化具体gap深入。保Qwen初始化、分阶段解冻/约10%额外参数与image-text限制，不授zero-init永久等价/所有模态或免费。未核代码/像素/运行复现；实际PRE/SAVE/自读/solePOST见本日canonical。

## B7 同一可渲染场景不等真实Dynamics

owner `MULTIMODAL-WORLD-MODELS`，Ch25 Persistent world state末、Object Address标题前。已读715–747完整当前空间状态论证；已有viewbank/pointcloud几何缓存，没有共同生成position+feature点latent再一次解码成统一scene的生成状态接口。Ch23拥有一般表示，而本段只拥有已知/新区域的state增长与renderer权限。

正文：

场景扩展还可直接发生在共同3D latent中，而不逐视图生成后再重建：将带位置和特征的点作为生成状态，固定已知区域的条件点，只生成待补区域，再解码为同一组可渲染Gaussians。[Terra的受限分支](https://arxiv.org/html/2510.14977v1#S3)共同生成几何与外观，让不同相机消费同一份场景；这给静态渲染提供一致参照，却不证明隐藏几何真实、环境受动作后的转移正确或无限扩展不漂移。位置扰动有助生成而可能损重建，几何指标改善也可伴图像质量退步；历史点累加、位置匹配、codec训练和渲染都计费。新旧区域身份、几何或预算失配时，保留可信capture、短区域补全与显式renderer，需要控制时另用可靠simulator和真实新观测，不能让多视图自洽替world truth签字。

<!-- source-family:SF-2025-ARXIV-2510-14977 -->

本人注：`SF-2025-ARXIV-2510-14977` — Schrodinger，Daily2025-10-18补Oct17；exact-v1 §3/Eq1–9、4.1–4.4/T2–3，3+2+2=7。只共享pointlatent scene/固定已知条件与renderer消费，保静态ScanNet/RGBD信息/图像指标反侧/历史增长全费，不授actiondynamics、真实隐藏面或无限稳定。未看gallery/核代码或复现；实际PRE/SAVE/自读/solePOST见本日canonical。

## B8 BM的元素角色也是格式身份

owner `INFER-TENSORRT-LLM`，Ch49 Block Scale小节2605-12464 marker之后、Block Scale格式选择标题前。当前讲改sharedscale/多grid，没有保scale而改变最大元素私有编码的分支；实际读2275–2310，notes仅来源。

正文：

处理block outlier还可以保持shared scale，只改变最大幅值元素的编码角色：记录它在block中的索引，将其原本可由shared scale推知的私有exponent位用于更多mantissa，其余元素仍按原格式解释。[MX+的受限设计](https://arxiv.org/html/2510.14557v1#S4)因此需要额外索引与小值边界约定，不能把所有元素同宽称为总metadata不变；原生MX指令也不会自动理解这个扩展。软件可以先转换到较高精度，或用额外修正乘加补最大元素，硬件专用支持则是另一实现分支。转换、寄存器交换与额外计算在prefill和decode的代价不同，aggregate GEMM计时不等完整服务时延；格式/索引、质量或执行预算不合时，保留标准MX、较高精度或原kernel，不由更低量化误差批准无损或免费部署。

<!-- source-family:SF-2025-ARXIV-2510-14557 -->

本人注：`SF-2025-ARXIV-2510-14557` — Schrodinger，Daily2025-10-18补Oct17；exact-v1 §4–5/Alg1、7.1–7.4，2+2+2=6，最大元素角色/metadata具体gap深入；arXiv与ACM online同Oct17一family。保32元素多1byte/4.5bit、prefill/decode额外费及RTL/AccelSim非实芯片，不授原生MX零修改/完整服务净速。未核代码/运行复现；实际PRE/SAVE/自读/solePOST见本日canonical。

## B9 离线Policy晋级门不等物理单调改进

owner `MULTIMODAL-EMBODIED-VLA`，Ch26 DROL段/marker之后、World-action model标题前。实际827–841已有perstate BC/RL Q与likelihood、winner示范约束，没有以学得transition+critic对完整policy版本作OPE晋级的生命周期门；与控制器执行权不同。

正文：

保守比较还可用于决定哪个policy版本进入下一轮，而不只逐状态选择动作：从示范训练的diffusion policy出发，先在离线数据上更新候选，再由学得transition与critic估计其相对旧版本的收益，超过门槛才晋级，否则保留旧policy。[RL-100的受限流程](https://arxiv.org/html/2510.14830v1#S3)将这份离线门与后续真实采集、重训、在线调整及单步蒸馏分开；OPE较高只证明相对所用模型的估计，不认证真实回报单调、分布外安全或蒸馏student等价。各阶段policy/critic/数据与执行horizon须分别保存，全部评估、采集、重置、训练和控制回归都计费；预测支持、真实成功或deadline失配时，保留旧示范policy、多步采样与独立controller，不能由有限trial的100%成功批准任意环境部署。

<!-- source-family:SF-2025-ARXIV-2510-14830 -->

本人注：`SF-2025-ARXIV-2510-14830` — Schrodinger，Daily2025-10-18补Oct17；exact-v1 §3/Eq12–22及§6/8必要，3+2+2=7。仅完整policy的OPE晋级与真实控制权限分责；保learnedcritic/transition估计、v1的400DDIM/500CM分母/重置与全费，不反投current1000trial或授安全单调。未核全附录/代码/视频或复现；实际PRE/SAVE/自读/solePOST见本日canonical。
