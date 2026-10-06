# 2025-10-27 初筛与必要反侧

BJT [10/26 09:00,10/27 09:00)。实际 API 参数见 arxiv-model/system/agent/agent-narrow.request.json；响应不是已读证明。

## 入口与停止

前三查询统一12个合同分类、提交线索范围 `[202510231800 TO 202510241800]`、start0/max100、submittedDate升序。model标题 language model/transformer/attention/MoE共43；system是LLM加training/inference/kernel/cache共11；agent原词组agent/RL/world model/vision language/multimodal/diffusion共70。三个查询去重112，是提交时间线索，不是本窗候选数。

原agent入口过宽：仅保存为相关标题补检定位，不逐项关闭。实际重查受影响入口：cs.CL/LG/CV/RO/IR/MA，原主题同时要求摘要 language model/foundation model/vision language/VLA 或标题world model；共19，start0/max100即止，无分页。月cs.CL首页50标题只作查漏，不把2666条月库存转换队列。新命名机制通过这次标题定位补检；不声称全学科召回。

API summary当前版本可能是v2/v3，提交后延迟到2511的ID也在返回中。availability只给名义日程及处理延迟，无法提供本窗完全落入的first-public bounds。日期缺口不是0事件；下面机制潜力都不进入确定候选、评分、正面Evidence、Books或无遗漏声明。没有撤回标记不能反推所有历史版本有效。

## 完整题摘后的具体潜力

这些已读题摘用于准入潜力而非证据完成，版本取响应ID；未核日级首公开。按新增命题归并记录，不继承其他日期池：

- 2510.20909 CodeAdapt：代码执行反馈自举是否改变指令模型/推理模型适配收益，不能只据8任务平均数定论。
- 2510.21090 Self-Reward：SFT/base log-ratio作为demo-only PPO反馈；2510.23629 TracePile：可执行链条监督区分rationale与结果监督；2510.21175 NuSACL：近似null-space约束连续LoRA；2510.21184 RePULSE：低reward重采样与辅助损失是否控制尾部风险；2510.23631 RCPO：多路排序观测的choice likelihood。保留各自优化差额，不以已有RL/LoRA主题关闭。
- 2510.21270 PBS-Attn：token permutation变换block-sparse prefill执行；2510.20984 GLVQ：learned lattice/Babai rounding低比特解码；2510.21450 ParaRNN：Newton并行解非线性递归；2510.21908 fast-weight plasticity：短依赖与长依赖条件不同。需要精确历史版和端到端配置，不把摘要倍数当已证收益。
- 2510.21310语义不确定性估计的diversity sampler/importance weighting；2510.21258 correlation dimension区别long-range语言复杂性与PPL；2510.21326 Typoglycemia的碰撞/上下文对照；2510.21518 Head Pursuit head probe/edit；2510.21606 ModestAlign noisy/resource-limited contrastive alignment。都可能提供具体评价/表示边界，不以局部或小模型排除。
- 2510.21111 PhysVLM主动信息获取；2510.21122 NoisyGRPO视觉噪声探索与Bayesian advantage；2510.21182 KBE-DME动态重选图像/知识；2510.21232 constrained world-model confusion；2510.21447 PhysWorld以物理示范合成训练deformable dynamics；2510.21473 MRO diffusion language多reward与group-step weighting；2510.21571 egocentric视频VLA数据分段。保留基础模型/world/action机制潜力，非所有视觉/RL应用。
- 2510.20903 diffusion信息论KL/Fisher对象；2510.21264 TSSR topology-shape两阶段生成；2510.21323 VLSAE跨模态concept-neuron语义；2510.21361 compositional MCTDiffusion；2510.21366 bandwidth-aware diffusion early stop；2510.21686可控MI的数据生成基准；2510.21697图像扩散几何推理。需方法/反侧才能判断，不由标题词汇授采用。
- 2510.21180模拟社会的desirability偏差；2510.21031 AgentArcEval架构评价条件；2510.21007 confidence-guided CoT是否真正有用；2510.21398 budget-forcing小模型；2510.21443 requirements分类中dataset主导且规模差不显著；2510.21902代码访问/互动探索切换的SWE-controller基准；2510.21603 DocResearcher多粒度证据链；2510.21903 ToM-SWE持续user-state；2510.21614 meta-productivity指标；2510.21618 memory folding与ToolPO；2510.21704 model-attribute实验式反思；2510.21557 CoSight冲突热点验证。保留可能改变对应设计的受限命题，局部结果不是排除理由。

## 必要安全与设计反侧 core，均日期隔离

七项定点打开 `/abs/IDv1` 与 `/html/IDv1`，读以下必要正文后停止，不遍历全部附件，不写安全保证：

- 2510.20956 Self-Jailbreaking v1：§3.2–3.3固定500 thinking tokens、StrongReject313项与GPT-5检测/250人工标注；§4.1–4.2主要s1.1-7B/base directions及steering；§5与§6 safety reasoning混入、English及部分失败解释限制。看到“仍识别有害”与“最后拒绝”不是同一状态；50条修复限这套多任务设置，未采用普遍保证。
- 2510.21236 AgentBound v1：§3.1–3.3 generic→runtime permission、Docker mounts/env/hostname-resolved iptables；§5人工manifest审核、语义/配置问题另需控制。网络初始化/安装发生限制施加前，IP粒度不等精确URL授权；§4.3 startup150–400ms与steady-state <1ms分别计费。不能用摘要“negligible”概括冷启动或全攻击防护。
- 2510.21885 Behavior-Aware Sampling v1：§3、§4.1–4.4、§8读到类别分层/T1 refusal、Llama2-7B LoRA、20k Alpaca、L40S、HarmReward/SALAD/XSTest。HTML摘要写0.05%，abs写0.5%，未选择有利值；同一原件存在数量口径差异，保留核对需求。只作日期隔离的安全信号，不采纳41%安全提升。
- 2510.21144 NeuroGenPoisoning v1：§3.1、3.2–3.3及§6。明确white-box推理activations/attribution，不是任意black-box攻击；poison-responsive neuron遗传文本优化不能直接证明生产RAG必被攻破。
- 2510.21524 EU-Agent-Bench v1：§2–2.1，60人写prompt增强600，首turn工具参数rubric，七checkpoint温度0.7、每query十次；不调用必要tool的trial被排除，所以legal-rate分母不是端到端task-completion。此处只读评价协议，不给法律建议/合规保证。
- 2510.20963 ColMAD v1：§2.2–2.3与§4.1，竞争说服/伪证与合作引证检查，Bayes judge+bounded LLR模型假设；三种error-detection任务、temp0、judge选择效应，不把理论toy setting外推通用debaters。当前v2改题/论点，不拿v210pp主张当v1收益。
- 2510.21339 Multi-turn Training v1：§3–5，Qwen2.5-3B、GSM8K、55epochs，UACR/ULCR/UADR与basic incorrect反馈；Pass@8与8-turn不可混同，temp0，单turn能力下降受这套全信息任务限制。不是所有闭环agent不用multi-turn训练的结论。

## 分层排除样本

- 明确领域应用标题：2510.20976 metal-organic frameworks、2510.21228 emergency medical services、2510.21445 remote health monitoring、2510.23639 genomics/EHR。仅领域应用/暂缓AI for Science，不借Agent/Data/Eval重新引入。
- 完整题摘归纳材料：2510.21890 diffusion教材、2510.21425 neurosymbolic四维分类，新增主要归纳/路线图，无明确改变设计选择的证据，停止此次初筛；未声称全文无学术价值。
- 2510.21566 ColorEcosystem完整题摘为carrier/store/audit组织蓝图与部分实现，尚不足以把广义“可信服务”当具体新执行条件，未作正面采用；不是因为主线已有覆盖。

未经独立校准的排除样本和全部安全/反侧信号交root检查。普通其余明确应用项只抽样复核，不虚报全量读完112项。
# FIRST反馈后的M2贡献关闭

2026-10-05T07:16:17+08:00，仅同步Peirce R-M2，不重读有效原件。官方发布文章JSON-LD `2025-10-27T00:00:00.000Z`核实落窗，不能证明首次权重公开。原完整core说明算法/认知进展留待后续披露；产品用途、服务价格、模式和现成部署支持没有支持改变设计解释的新机制或可比质量/资源边界。8%价格是服务政策，TPS/倍数未绑定hardware、precision、batch、concurrency、输入输出、SLO或可比evaluator，不以其或230B/10B规模数字授5分。当前HF main不是已锁初始card，top_k40与原Blog20不一致，不补证当窗新机制或历史性能。故M2贡献关闭、正式候选0、候选Evidence0；不是因名气、Books已有覆盖、附件成本或访问失败改判。保留原准入草稿为历史，最新处置以本段及Peirce FIRST为准。只有具名官方精确版本披露具体新机制/可比取舍时定点重开，不要求全版本史或全附件。
