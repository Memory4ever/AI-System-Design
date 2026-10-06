# 本日 root 三项必要审阅与 owner 判断

仅处理本日既存12746/12760/12772，日期准入复用本日有效题摘/公开夹证；不扩发现，不迁旧候选。root此前实际读取以下精确v1核心方法、关键评价和反侧，压缩恢复按当前研究合同复用未变化原证；未核代码或复现。

## 2603.12746v1 — DynBench

[原证](https://arxiv.org/html/2603.12746v1)：§2.2、§3.1–3.5、§7，尤其数据构建/annotation来源、Tables3/5/6与STTCM输入。1,000 videos/7,000 VQA/3,000 grounding来自八个不同2D/4D集合；缺失标注可由其他pipeline估计，随后motion filter及VLM/人工检查。推理与mask J&F是不同任务；通用/空间模型未测grounding，不能补造联合失败。STTCM将RGB-D/mask/geometry转为文字辅助，再交模型回答，其生成和输入披露改变受测系统，并非证明模型自己从视频获得同样状态。Qwen235B辅助构建成本、源标注/估计状态与消费接口必须进入评价身份。

Table5 prose所述模型/最佳M-only与表内模型/all-TMS不一致，§3.2最佳模型叙述与Table3另有排序冲突，隔离这两项精确headline，不由此删除独立方法贡献。Table6 Qwen8B mask-only平均仍53.8且两切片下降，融合57.1同时改变可见appearance/motion，不能把辅助收益唯一归因理解能力。有限任务与未披露运行配置不授物理能力或服务SLO。

2+2+2=6，标准审阅完成。唯一`PLATFORM-EVALUATION-SYSTEM`具体已有覆盖：root实际Ch66 220–269完整subject包含protocol/scaffold/environment，900–928 No-Aux/Generated-Aux/Validated-Aux配对及参考状态只作上界，已经解释本材料拟保留的构念、外部辅助来源/消费与成本责任；不声称现文包含该benchmark库存或精确STTCM公式。建议No Change，不为增加paper例子再写同机制。两个表文冲突不作为Books正面采用依据。

## 2603.12760v1 — HiFICL

[原证](https://arxiv.org/html/2603.12760v1)：§3.1–3.4/Eq1–4，§4/5/Tables1–3与消融。给定Q/K/V时，单head attention分成原query self-attention乘`α=Zq/(ZD+Zq)`和demo读取`βVD`；这项代数分解不证明整层/全模型任务等价。受限分支冻结基座，以每head低秩virtual K/V参数和任务CE训练，无teacher、无真实demo在线输入。VA/VB初始化中的V零仅令新增value项零，virtual keys仍改变softmax分母、α通常小于1，因此不是完整attention no-op。固定资产由请求query读取不同响应，不是线上修改权重；普通LoRA激活也依赖输入。

有限7B/8B、每任务1,000训练样本、随机8-shot比较与val-best checkpoint；低秩/shot容量不构成全部搜索预算匹配。Table3 CHAIRi/recall改善而CHAIRs2.8→3.2反退，不能写所有幻觉减少；α=1消融退步保留。参数更少不授端到端低成本，部署设备/precision/batch/concurrency/SLO未完整绑定。

2+1+2=5；已确认适配资产/零初始化边界差额，按知识缺口深入必要命题。root实际Ch30 444–480权重delta→prompt→recurrent launch接口与Ch29/31相关入口，现文尚缺virtual KV分母与零value不等no-op这一责任。唯一`TRAIN-LORA`；以下一段拟插在低秩prompt段后、Recurrent Launch State前，未写入，待独核PRE与root锁。

> 不改权重的适配还可以把每层 attention 的虚拟 K/V 作为可训练资产：固定虚拟 keys/value 参数，由当前 query 读取它们，替代每次请求都带入真实示例的部分上下文作用。给定这一层的 Q/K/V，原 query self-attention 与示例读取可按各自 softmax 归一化质量拆开，但不能据此认定所有层或任务都等价；学习的低秩虚拟 K/V 仍增加 attention 读取和归一化开销，不能像权重 LoRA 一样直接 merge 消失。尤其把新增 value 初始化为零，只消除了新增 value 项；虚拟 keys 已改变分母，原 attention 项仍可能被缩放，因此零 value 不是整个层的 no-op。基座、head/layout、虚拟 K/V、初始化与归一化规则须共同绑定适配版本，并分别验收初始输出及训练后的任务质量。有限对照中幻觉子指标也会反退，较少可训练参数不等于总训练或在线成本更低；质量、布局或请求预算不适配时，真实示例、显式 prompt 与可 merge 的权重 delta 仍是不同的合理分支。

## 2603.12772v1 — PVI

[原证](https://arxiv.org/html/2603.12772v1)：§3.1–3.5、§4/5/Tables1–2与消融。冻结VLM/main DiT及辅助视觉encoder，另训练从main expert完整复制的分支；两路只共享初始proprioception/noisy-action token序列h0，随后各自演进，旁路以辅助视觉条件替换VLM条件，逐层经zero投影残差注入主链。Eq5旁路消费自己的前层hidden，不是每层读取主链hidden。不是只有小投影可训练；embodiment state/action adapters也可训练。零注入只在冻结主链及相同输入adapter的初态保证不改变该路径，不能证明训练中全局行为不变。恢复时定点重开§3.4/Eq5–6已纠正原笔记的“主分支层状态”误述，不影响此前关键评价限定。

VJEPA2八帧4fps与DINOv2单帧及组合改变输入与资产；sim20任务每任务50demo/100rollout，freeze/trainable容量差额未被完全控制，不能把收益归因为注入位置单因素。平均35.7→59.7不等每项最佳；bottle95低于Reference96等反侧保留。十任务temporal69.4优于DINO56.8、组合68.9非相加；4frame71.8优于16frame66.6；非零初始71.8优于零69.4，零初始是保守接口而非最终质量最优证据。50-task增益收窄，Airbot cloth仅定性demo，无实机成功率/SLO证明；aux encoder/copy branch训练及线上成本必须计入，不授轻量免费或物理安全。

2+1+2=5；辅助输入与冻结主链的梯度/部署分责差额深入必要命题。root实际Ch26 268–291 action mediator→通道bottleneck与105–155训练特权表示、328–387 policy/World交接；训练期特权teacher不能替代本材料部署仍读取aux encoder/copy expert的成本，唯一`MULTIMODAL-EMBODIED-VLA`。以下一段拟放mediator三段后、接触通道bottleneck前，未写入；等Anchor同Ch26锁释放及独核PRE。

> 不希望动作监督直接改写已训练的主专家时，还可以冻结主视觉语言与动作分支，把另一种视觉表示交给从主动作专家复制的可训练旁路，再以逐层投影把旁路 residual 注入主链。两路从同一 proprioception 与 noisy action token 初态出发，随后分别演进：主链保留原视觉语言条件，旁路使用辅助视觉条件，不是在每层读取主链的 hidden state。新增的是条件与梯度通道，而不是授予旁路物理执行权；辅助 encoder 与旁路在部署时仍需运行，不同于训练后丢弃的特权 teacher。零初始化注入投影可令冻结主链在相同输入接口下从原函数启动，但 input/action adapter 的更新须另查，不能把局部初态相同当作后续行为保真。完整复制分支、视觉读取与训练增加参数、时延和耦合资产；有限任务中增加帧数、组合两种视觉表示或采用零初始也并非总能提高最终成功率。辅助状态失配、费用超出预算或任务反退时，直接融合、原冻结策略及更小的 action mediator 仍合理，由闭环任务和真实 controller 验收决定是否采用。

## 2603.12989v1 — CleanSight，root 非作者 Source/PRE 复核

root 实际打开 exact-v1 HTML，核 §3.1 权限、§4/Eq6–12、§5.1–5.4/Tables1–4、B 选层与 C.1–C.3/Tables5–7 的必要反侧；读取作者 [必要审阅与逐字 PRE](./SUP_RESUME_CLEANSIGHT_PRE_20261011.md)。参考是逐维 mean/std，不是 full-covariance whitening；ratio 分母仅 prompt keys，mask 来自最后检测层的 max-head union，只改变后续 key logits，未物理删 token/KV 或重算早层。Table4 Qwen/LoRA 的效用反退、Table1/3 ISSBA 配置不一致、oracle PU 和 adaptive 残余/FPR 均未被正文 headline 掩盖；不授任意模型/攻击、免费或生产安全结论。2+2+2=6 的具体安全命题深入审阅通过，未核代码或复现。

actual Ch72 62–105 及 958–985，另读 Ch71 主体身份交接和 Ch73 生产入口：现文分别解释跨步概率 sensor、外部前端与白盒 probe，但没有 headwise visual/prompt ratio 参考校准及跨 decode key-mask 分支，不能虚记 NC。唯一 owner `PLATFORM-SECURITY`，两段插在 BackdoorAgent 概率 sensor 后、trigger strength 绑定前可形成“便宜读出 → 可控白盒干预 → 仍须独立行为验收”的衔接。逐字 PRE 两段及静态本人注通过，授权报告作者窄写该位置；实际写后正文、完整局部邻接及本人注仍待 root 非 writer POST，不由本节预支 Books 或日级验收。

实际 POST：作者写入后，root 非 writer 完整顺读当前 Ch72 69–103，新增 78/80 与原概率 sensor、后续 trigger strength 论证衔接，逐字对回已通过 PRE；尾部 4449–4457 本人静态注与邻注实际回读。未添加未获准机制或动态验收注，ratio、key-mask、未重算早层、adaptive/utility/oracle/全费用及旧分支保持。正文和本人注均通过，Ch72 此 family 窄锁释放；报告与最终日级验收仍由各自责任人完成，不授日级通过。
