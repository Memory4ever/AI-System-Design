# Daily 2026-10-13：模型与训练候选的必要证据及 Books 比较

窗口：北京时间2026-10-12完整自然日；精确版本均为2610.*v1。准备者：today_models，持本文件及root逐批授予的Books局部窄锁；不写Report/LS/index，不自授独立Source/PRE/POST或整日报验收。条目中的写前proposal保留研究因果，实际结果以末尾执行同步及对应Books正文为准。

日期身份复用本日原始36题摘及root实际核过的官方Mon12公告批次；HTML页眉/abs的Submitted Oct9不是公开日。未核代码或复现实验。当前官方事件入口未见影响下述命题的撤回/纠错说明；不遍历全版本史。评分只对应每篇新增命题。

## 2610.13910v1 — When VLMs Destroy What They Know

- 准入链：输出组合准确率不能判断内部关系信息在哪里丢失 → 同一概念编辑下，谓词token、EOS和mean pooling出现可读出差异 → downstream representation的选择需要独立关系保留测试。评分2+1+2=5；标准证据及owner差额定点深入完成。
- [exact-v1](https://arxiv.org/html/2610.13910v1)：§3.1–3.2/Eq1、§4 Setup/§4.2–4.4/Table2–3、Limitations已读。CASP-VL改scene graph中的一概念，再渲染caption；**图像不变**。linear probe只在原caption训练、在编辑caption的留出image-group split测试，五split/bootstrapped区间。CLIP/SigLIP与LLaVA的末prompt token口径不同，不能合为同一池化算子。
- 采用：局部predicate上的可辨识信号，不保证全句EOS/mean读出保留；行为分数不能给表示保真签字。反侧：只测text path；谓词近满分首先能识别编辑词，不是已证明谁在谁上方的完整几何；非线性编码未被完全排除；多句压缩解释部分差额，单句、自然描述仍有剩余。不采用“所有VLM摧毁全部空间知识”、视觉encoder缺陷、真实场景干预或通用修复。
- owner `MULTIMODAL-REPRESENTATION`：[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)“Object Hallucination需要分开视觉写入与语言读取”已有write/read和不同token存关系（当前1435–1445），但没有**同一表征从predicate token到global pooling的consumer瓶颈**。邻接“感知到了，不等于行动会使用该模态”保留，机制只留Ch23，不另在Ch66复写。
- 最小PRE（待独核/落实）：接原“表示经过contextual encoder…”两段后，增两段：关系可在局部token读出却在全局聚合丢失，所以声明consumer的token/layer/pooling；用只改caption、image固定的受控probe与lexical baseline，分开检测局部词汇、global encoding和行为；保留有限模型/text-only/非线性边界与原token/专用readout/独立关系测量退路。当前Books决定：拟整合，未落实。

## 2610.13895v1 — Task Context Shapes Component Roles

- 准入链：共享head身份常被当作共享功能 → 同一graph facts与固定head在task/context编辑后改变事实响应和下游influence → 必须把组件归因条件化。评分2+1+2=5；标准+owner差额定点深入完成。
- [exact-v1](https://arxiv.org/html/2610.13895v1)：§2.1–2.5、§3.1–3.4/Fig2–5与§4。固定final input位置，head沿任务方向±2个标准单位扰动；influence是下游projection响应，importance是mean replacement的答案logit-margin损失，二者不是同一尺度。graph facts固定的指令变更、固定书面指令的内部task-vector编辑、乱序/符号控制与下游restoration支持**被测条件下网络响应变化**。
- 采用：同一个head的事实响应和到后续组件的局部影响可随任务状态变化，报告head名称不足；conditional response map在Gemma/Qwen的分别局部预测好于平均map。反侧：只测合成graph与固定sites/方向；influence包含所有中间路径不是直接边；importance角度常被Res主导，head-only比较不总同向；局部head恢复只占整体task edit效应小部分，不授全任务开关唯一回路或选择性安全编辑。
- owner `MODEL-MULTI-HEAD-ATTENTION`：[Ch15](../../../../../books/part-02-model/15-multi-head-attention.md)“注意力图与平均传播只是诊断线索”已有mean/deviation与干预要求（277–283），但没有**同一事实下task-conditioned influence与answer importance分责**。最小PRE为该节两段，说明固定identity不固定role、matched事实/任务与局部扰动/恢复分别测量，保synthetic/local、间接路径和side-effect验证，不把局部map当通用线性机制。当前拟整合、未落实。

## 2610.13821v1 — Learn When to Abstain

- 准入链：置信度标量经校准不保证正确release → 同一candidate上学习新selector优于标量重新拟合，但跨dataset仍负utility → 将learning score、calibration与release三层分别验收。评分2+1+2=5；标准+反侧/owner深入完成。
- [exact-v1](https://arxiv.org/html/2610.13821v1)：§3.1–3.6/Eq1–4/Table1、§4.1–4.3/Table2–4及§5。Qwen3-14B关闭thinking；TriviaQA train2000/cal500/test2000，NQ500，三seed，阈值.65/.85未用于policy训练；同一greedy测试candidate比较原P(True)、校准、TRAIN logistic和LoRA selector。Rτ=correct−τ·answered；筛选保固定candidate，RL arms同generated responses但**selector与RL预算不相同**。
- 采用：分开score信息性/校准/阈值utility；更高AUC、更低Brier不保证域移下正utility，always abstain零utility应作为明示基线。TriviaQA的selector主对照置信区间支持局部收益；RL三对照adjusted区间跨零不等无效或等价。反侧：NQ未重校且selector负utility；exact match不能识别全部语义正确，150unit局部单人AI辅助审查非全测试语义验收；三seed有限；job elapsed time不是GPU利用率/部署时延。
- owner `PLATFORM-EVALUATION-SYSTEM`：[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)55–64已有reward threshold、coverage与条件正确率，183–197已有model/calibration共同发布；缺**同candidate学新score vs scalar calibration的对照和better-ranking仍低于abstain的反侧**。最小PRE可融入threshold后两段，不更改既有reward示例或校准发布段。当前拟整合、未落实。

## 2610.13672v1 — UPTURN

- 准入链：反思文字或最终失败标签不回答在哪修 → 学paragraph-boundary cut，保prefix、以新user turn注入同instruction再生成 → 截断位置与conversation-role边界是两个独立干预变量。评分2+2+2=6；标准+具体Books差额深入完成。
- [exact-v1](https://arxiv.org/html/2610.13672v1)：§4.1–4.2/Eq3–4、§5.1–5.3/Eq5–9、§6.1–6.3/Table1–2、§6.5及AppendixB/C所需chat-template。冻结Qwen0.6B encoder的130K position MLP仅用final answer成功训练；另66K正确性gate并非oracle。训练用失败rollout内切点组，相比cut不是比较不同完整response。
- 采用：同text保持inline与new-turn对照，学切点和turn-boundary组成bounded suffix repair。保留用户/assistant聊天模板与未闭think处理，不能把synthetic user role当真实用户授权。Base@32与UPTURN@16+至多16修正只同最大generation次数，生成token上限不同，修后pool16也不同；不称全面同compute。六数学task四reasoner局部收益和matched correction比较支持该机制；长reasoning截断解释较大收益，非通用自纠能力。
- 限制：gate误判会改好答案/漏坏答案，位置选择、encoder、前缀重prefill与训练都需计费；automatic outcome任务与共享Qwen vocab边界，不授任意tokenizer兼容或不可验证开放任务保证。
- owner `AGENT-REFLECTION`：[Ch80](../../../../../books/part-07-agent/80-reflection.md)148–201已有earliest repairable偏离、drift sensor与outcome authority；没有**external turn boundary相对inline conditioning**。最小PRE接repair action之后两段，保gate仅proposal、原无修改/完整retry与外部verifier回退。当前拟整合、未落实。

## 2610.13630v1 — Multi-Stream Attention Residuals

- 准入链：depth retrieval的多头若切hidden channels会破坏完整value、复制标量不能保证source多样性 → 用多尺度因果depthwise conv扩展完整source，逐stream depth attention再轻量混合 → 多读出不必多persistent residual state。评分2+2+2=6；必要机制/消融及Books差额深入完成。
- [exact-v1](https://arxiv.org/html/2610.13630v1)：§3.1–3.4/Eq9–17、§4.1–4.4/Table1–2与§5。先单流累积block summary，再按需多stream扩展；per-stream pseudoquery对历史source各自softmax，H_pre以sigmoid标量融合，不是序列attention的channel concat或carry H_res。因果conv只用当前位置及更早位置。
- 采用：persistent source储存/跨stage payload仍O(Nd)，不等**全部activation或读写仍单流**；two-phase仍保存每target的m retrieved results，final多流读出与融合有额外traffic。10B消融的无conv（shared source/multiquery）及uniform mixer分别支持source diversity主增量与fusion小增量。
- 主对照18B/28B MoE，12task相同reported配置；28B activated params+0.3%、FLOPs+0.5%，不是wall-clock净加速。1.58×是四scale、同token预算、排LM head并计residual FLOPs、固定loss floor拟合的iso-loss compute值，不是实测训练吞吐或生产SLO；stream8比4边际很小，full保存较多source有成本。未核fused kernel实现或硬件trace。
- owner `MODEL-TRANSFORMER-LAYER`：[Ch17](../../../../../books/part-02-model/17-transformer-layer.md)445–482已解释显式depth history、block/slots和persistent多流；484起拥有carry mixer几何。缺**单流source保存与多流读取分离**，不重写mHC或旧AttnRes。最小PRE：插在445节现depth路由归责段之后/现rank-one更新之前，用两段解释conv视图→独立depth读取→adaptive单流输入；第二段保persistent O(Nd) vs retrieved m-state、不可任意改已有checkpoint、预算/小增益/未核fusion与单流退路。当前拟整合、未落实。

## 首批逐字最小 PRE（待独立核验与窄锁；不是实际正文）

### 13630 / Ch17

位置：现depth-routing归责及普通residual退路段之后、现rank-one carry/write替代分支之前。保留原段落，新增：

多路 depth retrieval 也不一定要求维护多份可更新 residual state。可以先保存完整维度的单流 source 或 block summary，再由多尺度因果 depthwise convolution 构造含不同局部上下文的视图；各视图以自己的 pseudo-query 对历史 sources 做 softmax retrieval，最后用输入相关标量混合成下一子层的单流输入。这里扩展的是历史的读取视角，不是切开 hidden channels，也不是把同一向量乘几个标量便获得多样信息；因果窗口只允许当前位置及更早 token，checkpoint 必须与这套扩展、查询和融合接口共同训练。<!-- source-family:SF-2026-ARXIV-2610-13630 -->

按需扩展让持久 source 保存与跨 stage payload 仍按 `O(Nd)` 计量，却不让全部中间状态、访存或计算都保持单流：批量预计算仍会产生每个目标层的多路 retrieved states，最终融合也需读写它们。[MSAR 的受限 MoE 对照](https://arxiv.org/html/2610.13630v1#S3)支持这种读取分支，去掉上下文扩展后收益缩小；较多 streams 的边际收益很小，论文的 iso-loss FLOPs 拟合也不是实测 wall-clock 加速。卷积、重算、深度读取、融合与并行缓存都计价，fused execution 尚须实际实现验证；净质量或预算不成立时，保留单头 depth retrieval、较粗 block summaries 或普通 residual，不对已有 checkpoint 任意改接线。

### 13672 / Ch80

位置：“最早可修复偏离”的三对象/repair讨论之后、下一现有小节之前。新增：

局部 repair 还要分开“保留哪段前缀”和“用什么对话边界重启”。在可自动检查 outcome 的推理任务里，可先由轻量 gate 提议失败，再学习段落边界的 cut，保留前缀、丢弃后缀，以新的 user turn 注入固定重定向指令后继续生成；同一句指令若仍放在未结束的 assistant reasoning 中，可能只是被吸收为原轨迹的一部分。[UPTURN 的有限对照](https://arxiv.org/html/2610.13672v1#S5)分别控制 cut 与 inline/new-turn，支持把角色模板视为 conditioning 变量，但合成 user role 不代表真实用户授权，gate 也不取得正确性 authority。同最大生成次数不等同总 token、最终候选数或 compute；encoder、位置/gate训练、保留前缀的重新处理和修正都需计费。证据局限于所测可验证任务、模型与共享词表，gate误判或模板不兼容时，保留原答案、无修改 continuation、完整 retry 与外部 verifier，不以一次重定向签发通用自纠保证。<!-- source-family:SF-2026-ARXIV-2610-13672 -->

### 13821 / Ch66

位置：现阈值reward段之后、下一个评价对象段之前。新增：

回答筛选应将 score 学习、概率校准和 release threshold 分别比较：固定同一 generator 的同一候选，标量 logit 的再校准只改变其映射，不会凭空学习新的 question–answer 特征；另训 selector 则改变判别信息，还须在独立 calibration set 上校准分数，再按事先声明的业务阈值评价。评价同时保留 coverage、released-answer risk 与成本敏感 utility，并列 always-abstain 的零 utility 基线，不只报 AUC 或 Brier。[受限短英语 QA 对照](https://arxiv.org/html/2610.13821v1#S4)中，学习 selector 改善本域筛选，却在未重校的另一数据集上仍低于拒答；更好 ranking 因而不保证可发布收益。三个 seed 的 RL 对照区间跨零不等证明无效，局部人工修正也不是完整语义验收。候选生成、scoring、训练和校准全部计价；域移或净 utility 未通过时，应重新校准、回退原 filter 或拒答，不把一次训练收益转成跨域可靠性保证。<!-- source-family:SF-2026-ARXIV-2610-13821 -->

### 13910 / Ch23

位置：“Object Hallucination”中现contextual encoder关系token两段之后。新增：

关系在局部 token 上可被读出，也不意味着 downstream 的全句表示仍保留它。应固定模型与输入条件，分别测 predicate token、末位置与 mean pooling，再问只改变一个概念时，原caption上训练的 probe 能否在留出的编辑caption上跟随新标签；词袋 baseline 提供输入词汇信号的参照，行为准确率则是另一条验收线。[有限 CLIP/SigLIP/LLaVA 证据](https://arxiv.org/html/2610.13910v1#S4)显示局部谓词与 global readout 可以明显分离，但干预只改caption、图像不变，识别编辑词不等完整关系绑定，线性 probe 失败也不排除所有非线性编码。token、layer、pooling 与消费者应共同版本化，probe、控制描述和行为回归另有费用；关系保留不成立时，保留局部 tokens、专用关系 readout 与原图/行为复核，不以 pooled similarity 或局部可辨识性认证完整空间能力。<!-- source-family:SF-2026-ARXIV-2610-13910 -->

### 13895 / Ch15

位置：“注意力图与平均传播只是诊断线索”末段之后、现“几何分离不等于训练独立”之前。新增：

固定 head 身份也不固定它在每个任务中的角色。保持输入事实不变，分别改变任务指令或内部 task state，再比较同一 head 对哪些事实响应、扰动如何传到后续组件，以及替换该 head 怎样影响答案；influence 与 answer importance 是不同干预量，不能靠两张 attention 图或一个总分互代。[有限 graph-task 对照](https://arxiv.org/html/2610.13895v1#S2)中，匹配当前状态的局部 response map 比平均 map 更能预测同prompt干预效果，但影响包含中间组件路径，依赖选定方向、幅度和位置，少数head恢复也只占整体task切换的小部分。配对构题、activation measurement、随机控制与恢复均增加成本；新prompt或任务尚未验证时，保留真实干预和非目标行为回归，不把该局部映射当通用线性回路或选择性安全编辑证书。<!-- source-family:SF-2026-ARXIV-2610-13895 -->

## 2610.13617v1 — Training User Simulators with Latent Intrinsic Feedback

- 准入链：只生成用户utterance的环境还需另付judge → simulator联合生成latent评价字段和下轮utterance，直接提供turn reward → 环境与reward可合一次推理，但资格与独立评价须分开。评分2+2+2=6；必要Source与具体owner比较完成。
- [exact-v1](https://arxiv.org/html/2610.13617v1)：§3.1–3.2、§4.1–4.4/Table1–4、§5.1–5.2/Table5及D已读。Gemma3 base 4/12/27B全参训练；WildChat真实utterance，但LES由Gemini3.1-Pro合成，非真实用户心智观测。internal thought/rating/instruction followed/reaction/feedback先生成，再生成utterance；目标只是用户可观察条件。intent conditioning用高层目标固定任务。
- 采用：同一模拟器joint latent评估→utterance可省独立judge调用；realism、critique、human-rating correlation、assistant下游质量分别验收。反侧：LES F1在主Table1均低于纯SFT，27B realism亦非全面胜出；reward标签与行为judge同Gemini会共偏；909conversation人评相关不是真实逐turn ground truth；RL assistant仅Qwen2.5-1.5B、最多3turn、Gemma4Bsimulator、Gemini checklist评价；Table5三次sampling run不是三次独立RL训练。2.45e19 vs5.48e19是估算RL FLOPs、judge不同大小，不能外推全部制备/模拟器训练或部署时延省半。
- owner `TRAIN-RLHF`：[Ch31](../../../../../books/part-04-training-system/31-rlhf.md)119–123解释真实用户后续反馈/缺失/噪声，但不拥有**simulator latent reward与environment utterance联合生成**。Ch33仍负责group/update，不在此复写其算法。拟整合一段，尚未写。
- 逐字PRE，接现真实对话后续等级反馈段之后：

用于训练的用户环境还可以同时生成评价，而不另调用一个 judge：先在 conversation history 上生成模拟的 thoughts、rating、reaction 等 latent fields，再据这些字段生成下一轮用户话语，并把 rating 作为 turn reward。这改变的是环境与评分的执行耦合，真实 interaction logs 只提供话语，合成 latent labels 不是真实用户的内心观测。[LES 的受限对照](https://arxiv.org/html/2610.13617v1#S5)支持用一次模拟器推理替代环境加外部 judge 的训练分支，但 realism、critique recall、人工评分相关和 assistant 质量并不总同步提高，同一标签生成器与评价者还会共有偏差。论文的估算 RL FLOPs 节省不包含全部制备和 simulator 训练，三次 sampling 评价也不等三次独立训练。应保留 reward 字段、utterance条件与独立任务效标的身份和全部成本；偏好人口、模拟器或奖励失配时，回退纯话语环境、独立 judge 与可核人类反馈，不让模拟评分取得真实用户授权或任务正确性 authority。<!-- source-family:SF-2026-ARXIV-2610-13617 -->

## 2610.13370v1 — COAX

- 准入链：全局expert均衡不确保minority可用capacity → category-conditioned selection bias指定与token share不同的preferred expert share → capacity allocation与sampling mixture可分别控制。评分2+2+2=6；必要Source/actual owner比较完成。
- [exact-v1](https://arxiv.org/html/2610.13370v1)：§3.1–3.2/Eq6–11、§4、§5.1/Table1–2与§6/Table5–6。bias仅加TopK selection score，gate仍用原score归一；soft prior不hard partition，K不增加；shared experts不变。345M/3B/10.6B，32层、64GH200、10Btokens、4096length、aux load balancing仍存在，多seedmatched validation loss是主要对照。
- 采用：preferred share q_c/p_c可大于1、但不等实际固定reserved capacity/请求权利；bias可训练时用并撤除，无类别label推理需**训练—无bias验证**。Table6强bias拔除显著失配，退火只部分恢复且English退步；保bias推理又损吞吐；coarse dominant-vs-rest已在多语言中可足，不授language本体或expert独立性。只在所测mixture/scale支持局部收益与token-equivalent估算，不将额外baseline tokens当实测净节省。
- owner `MODEL-MOE`：[Ch21](../../../../../books/part-02-model/21-moe.md)132解释specialization/load冲突，465已解释global load-feedback selection bias与原gate分责；缺**category preferred share独立于data share、可撤除prior与失配**。拟整合一段接specialization/load段，保既有global controller。
- 逐字PRE：

Expert 数量均衡也不保证低频类别有足够的可学容量。可给每个已知类别指定 preferred expert subset，在训练时仅向该subset的 Top-K selection scores 加偏置，选中后仍用未加偏置的 router scores 计算贡献；类别的 preferred expert share 因而可以高于其 data token share，而每token激活的 K 不变。这是允许跨类别共享的软先验，不是硬分区、固定资源配额或新增专家。[COAX 的有限对照](https://arxiv.org/html/2610.13370v1#S3)支持这条容量分配分支，却显示强偏置训练后直接拔除会产生严重 train–inference mismatch，退火仍可损伤主类别，保留偏置推理又有负载与吞吐代价；细分每个少数类别也未必比 dominant-vs-rest 更好。类别标签、subset、bias/退火、数据配比和原load balancing共同版本化，制备、训练与全部质量/执行费用计价；无偏置推理或主/尾类回归未通过时，保留原router、global均衡、数据重采样或经核的类别条件路径，不由preferred share认证专家语义独立或生产收益。<!-- source-family:SF-2026-ARXIV-2610-13370 -->

## 2610.12995v1 — CIG-SFT

- 准入链：高full-context probability可能只是prefix可续写，低support又可能正是要学的新决策 → frozen reference比较相同gold-prefix有/无task input，另以current policy做KL projection → learning-value proposal与update movement分责。评分2+1+2=5；必要方法/对照/反侧及owner完成。
- [exact-v1](https://arxiv.org/html/2610.12995v1)：§3.1–3.4/Eq4–20、§4.1–4.3/Table1–4与§5。task-free empty input只是intractable marginal的近似，不是客观conditional MI。归一clip c_t可离线缓存；q*对current policy指数tilt，CE soft-target与hard weighted CE仅在targets/weights detach时**梯度等价而非loss值等价**。分母原有效监督token数N，不是sum weights。
- 采用： frozen attribution与current proximal adaptation两种reference职责；标准SFT模型Qwen2.5-Math1.5/7B与Coder3B、共同同epoch超参、Avg/Pass@16，Table4去c/去prox及online attribution反退支持局部设计。7B部分Pass与AMC不胜最强baseline，code HumanEval Pass低于base；不采全面普胜。小update norms不能排除总梯度尺度解释，非matched总训练/制备FLOPs，无seed uncertainty披露则保Not Disclosed；不授优于RL完整预算或全原能力保持。
- owner `TRAIN-SFT`：[Ch29](../../../../../books/part-04-training-system/29-sft.md)159–171已有probability门/trajectory变化/visualblur gain代理和loss-vs-visible-history，缺**task-input-free条件差与current projection的双reference分工/梯度detach等价**。拟接Visual Information Gain段后，不重复泛化proxy原则。
- 逐字PRE：

监督价值还可以比较相同 gold prefix 在“给任务输入”和“不给任务输入”时的 reference-token likelihood，而非只按完整context的绝对概率选词。冻结 reference、缓存归一后的 log-likelihood gain，再以当前 policy 为近邻构造只抬升示范token的 KL-regularized target，分别回答“任务增加了多少支持”和“这一步向示范移动多少”。[CIG-SFT 的必要机制与消融](https://arxiv.org/html/2610.12995v1#S3)中，empty task input只是 marginal 的近似；gain是该模型/输入格式的监督proposal，不是客观互信息或语义因果。将投影soft target改写为scalar-weighted CE时，只有target与weight都detach才有梯度等价，loss值不必相同，归一分母仍须声明。双reference前向、缓存和训练全部计价，较小参数变化也可能受总体权重尺度影响；所测数学/代码有质量切片反退，不能由aggregate分数认证全能力保持或等总预算胜过RL。条件差失真、长尾覆盖或净质量失败时，保留verified CE、原概率门与完整可信trace。<!-- source-family:SF-2026-ARXIV-2610-12995 -->

## 2610.13257v1 — CAST

- 准入链：decoded text对齐只确定teacher/student比较对象 → chunk advantage仍需分到student tokens，未对齐位置仍会共享参数drift → credit与correspondence独立设计、absence单独anchoring。评分2+2+2=6；必要Source/owner完成。
- [exact-v1](https://arxiv.org/html/2610.13257v1)：§3.1–3.3/Eq1–11、§4.1–4.3/Tables1–6。alignment chunks与默认K6 credit chunks不同；uncertainty×inverse-local-teacher-variation归一权重保持每chunk的总signed advantage。局部smoothness不是teacher correctness；KL allocation最优只对该objective，bounded distortion只界smoothness，entropy仍可集中credit。异tokenizer只anchor未对齐采样token（clipped KL estimator非full distribution硬界）；同tokenizer all-positionreference KL，不照搬空U。
- 对照Qwen3-8B→Mistral/Llama，以400K SFT初始化；uniform control保clipping/anchor/two rollouts，支持credit差额。主benchbestAvgcheckpoint、三seed只是所报setting；MATH或GPQA等切片反退；4rollouts/stronganchor非单调，梯度sketch诊断非全部优化无偏。20K/15Kprompt/teacher scoring/initial SFT与entropy/retokenize/anchor成本均保，不称更少监督免费或普适tokenizer transfer。
- owner `TRAIN-GRPO`：[Ch33](../../../../../books/part-04-training-system/33-grpo.md)1270已有disagreement/task relevance选监督，2101已有cross-tokenizer ratio不严格token IW；缺**alignment后chunk credit与无对应token的anchoring**。拟一段接Selective Distillation开头、原概率尺度讨论之前；不让Ch11重推训练credit。
- 逐字PRE：

跨 tokenizer 的 decoded-text alignment 只建立可比较的 span，不会自动规定其中每个 student token 的 credit。可将同一chunk的 signed teacher–student log-probability gap按student uncertainty与局部teacher-score平滑度分配，归一后保留chunk总advantage；没有对应teacher信号的位置再对初始student加独立anchoring，避免共享参数更新无意带走这些位置。[CAST 的有限对照](https://arxiv.org/html/2610.13257v1#S3)支持把correspondence、credit和absence处理拆开，但smoothness不是正确性，局部allocation最优不是无偏policy更新，采样token上的clipped KL也不是硬保留保证；同tokenizer的实现采用全位置reference KL，不能照搬未对齐集合为空便无需正则的结论。retokenization、chunk映射、entropy/teacher scoring、初始SFT和anchoring都计费，更多rollouts或更强anchor并不总更好。映射或teacher资格不成立、质量退步时，保留均匀chunk credit、同tokenizer蒸馏与原reference，不能由文字对齐批准概率事件或旧能力完全保持。<!-- source-family:SF-2026-ARXIV-2610-13257 -->

## 2610.13202v1 — S3R

- 准入链：sparse response直接训练改变behavior，response自己的IS只修它的概率 → group-relative advantage还依赖其他稀疏成员 → 在proposal层稀疏、exact sampling还原dense group而非只修训练weight。评分2+2+2=6；必要反证/Source/owner完成。
- [exact-v1](https://arxiv.org/html/2610.13202v1)：§3.1–3.3/Propositions1–2/Eq1–3、§4、§5/Eq5、§6.1–6.3/Tables1及稀疏预算直接对照。固定snapshot、每response独立fresh randomness、baseline同sampling/stopping、正确accept/residual sampling，才能得到dense product group；不意味着所有group-IW不可能，只否定response-wise自身weight对unchanged group advantage的一般恢复。full attention verifier还需**dense历史KV**并重算proposal block各层，approx历史KV不够。
- Qwen3-1.7/8B、8H100、DAPO17K、B256prompt×8response、temperature1、16K/24Kmax、s=.05/k6；1.39/1.35×是所报完整training run-afterwarmup throughput含reward/update/overhead，quality bestcheckpoint非精确等价训练路径。attention72–76%只decode kernel；small B/4K即使fullaccept也亏，denseKV仍存、offload/thrash费用在，direct sparse correctioncollapse仅此aggressive设置。不授全部sparse训练失效或生产加速。
- 必要性能口径补核C.1–C.3/F.2：main为TP2×DP4、每replica最大256、S3R AIMD160–256，共同KV预算/CUDAgraph/prefix cache/chunked prefill；训练temperature1无top-p/k，评价temperature1/top-p.7/每题16次，main throughput分子是nonpadding prompt+response，按step throughput算术平均，整系统stack差而非每个lifecycle机制的独立因果加速。main actor/rollout精度未在C配置披露，记`Not Disclosed`；不能把F.2单replica2H100/BF16/固定concurrency/ignoreEOS的component profile精度静默移给main RL。输入prompt长度分布未完整披露，SLO对训练实验不适用。
- owner `TRAIN-GRPO`：[Ch33](../../../../../books/part-04-training-system/33-grpo.md)515组依赖、1205低fidelity目标重建已有，但缺**自己的response IS不能修其他成员reward comparison**。只在本章新增该组不变量与proposal/target分离，基础exact speculation仍由Ch48负责。
- 逐字PRE，接现Group-relative Gradient起始两段后：

这层组依赖也限制 rollout 纠偏：即使给每条稀疏policy生成的response乘精确的dense/sparse整response likelihood ratio，它仍使用其他稀疏成员的reward形成advantage，通常不能恢复dense独立group下的期望更新。它不否定重新设计group-level correction，而是提醒自身概率权重不修整组比较人口。一条[受限替代分支](https://arxiv.org/html/2610.13202v1#S3)只让sparse attention提出draft，再用同一冻结snapshot的dense历史KV/full-layer verification和精确accept/residual sampling生成最终responses；保持独立随机、sampling/stopping规则及完整group identity，才把稀疏预算留在cost而非objective里。full attention复用近似历史KV不满足条件，shared weights也不自动签发exactness。denseKV保存、proposal分布、验证重算、offload/restoration和权重同步仍需计费；小batch/短context可连满accept都不划算，局部collapse反证也不宣告所有稀疏训练无效。条件或净成本不成立时，保留dense AR、已有完整group与经验证的纠偏目标。<!-- source-family:SF-2026-ARXIV-2610-13202 -->

## 2610.12707v1 — Unsupervised Multimodal Reward Modeling

- 准入链：rewardbench排名不标识policy自己的candidate选择能力 → 冻结中间层linear head的negative comparison sampler决定拟合重点，policy-error bootstrap改善captionselection反而降bench → comparison law/readout/实际pool分别验证。评分2+2+2=6；必要方法/对照/反侧及owner完成。
- [exact-v1](https://arxiv.org/html/2610.12707v1)：§2.1–2.3/Eq1–5、§3.1–3.4/Tables1–8与§5。no human preference labels≠no labels：MRB用于选layer仅dev、policy bootstrap用verifier labels。response-token mean读冻结Qwen3-VL中间层，inbatch BT含coupled same-entry12.5%；density-ratio理想解不适用于全实际objective，sampler不满足互绝对连续且长度law并非全匹配；AdamW也非固定quadraticpenalty强凸最优。
- 采用：保持同image的caption perturbation能减少部分作者/风格shortcut但不认证负例真劣；head从policy自身verifier-labeled candidates训练，独立测在该pool selection utility。反侧：高rewardbench可不胜majority或training-freejudge；CHAIR同时收label与评价仅absentCOCOobjects，不是全面faithfulness；DPO randompairs亦改善、label增加actor收益未成立；图像160hardprompt仅OWLv2-verifier非真实人类偏好、安全列length artifact。全部frozenbackbone scoring/制备渲染/采样/校准费用，不能把fewparameters或headline千分之一当完整部署优势。
- owner `TRAIN-RLHF`：[Ch31](../../../../../books/part-04-training-system/31-rlhf.md)99–107已有比较人口/非unique scalar/pooling，174近候选与178label污染的BoN限制；这些generic边界**已有覆盖**，不重写。新增差额只为**same-image perturbation的轻量reward训练与policy-error comparison替换**，拟在174附近一段，非把全部论文塞Ch66。
- 逐字PRE：

没有人工偏好对时，也可固定backbone的某一中间层，用同图caption与其局部扰动训练response-token pooled linear reward head；这把监督放在negative sampler，而不是消除监督。哪层读出、扰动算子与comparison population共同定义head，benchmark选层的那份数据只能作development。[有限多模态对照](https://arxiv.org/html/2610.12707v1#S3)中，改用policy自身candidate里的verifier-labeled成功/失败对能改善该pool的caption选择，却降低rewardbench分数；原扰动head也可能不胜majority或training-freejudge。小head不是小全链成本，同图扰动仍有错误负例、长度shortcut和有限覆盖，CHAIR兼作label与metric更只核缺失的COCO对象提及；理想density ratio与强凸最优也不直接传给实际coupled BT/AdamW。原图编码、扰动/渲染、全部candidate、verifier与训练均计费；真实pool质量不成立时，保留原judge、majority、可信偏好对与独立任务检查，不由无需人工标签或benchmark排名批准deployment reward。<!-- source-family:SF-2026-ARXIV-2610-12707 -->

## 2610.13881v1 — Prediction Is Not a Sufficient Memory State

- 准入链：保存全部当前prediction也可能丢下次更新证据 → exact cumulative ridge的equal-prediction histories可对同nextsample不同，kernel attention的ratio亦不定normalization mass → state test必须包含continuation。评分2+1+3=6；理论必要假设/直接构造与owner完成，不遍历无关proof/CompleteAttention附录。
- [exact-v1](https://arxiv.org/html/2610.13881v1)：§1、§2/Eq1–4/Theorem1、§7/Propositions7/Theorem8与§8–9。continuous history-dependent state、unrestricted real features/labels、exact cumulative ridge、λ>0；W=MC^-1当前predictor不定C。d2零label collision可追加同(e1,1)得到不同nextprediction。positivekernel attention保(B,Z)而非只ratio；softmax exactcontinuous N(d+p)需openqueries/distinctrealkeys，不应用finite-vocab/approx/forgetting。本文不声称trained-model质量、独立神经优化或新的RLS算法；polynomial完整分类/finite-bit exponent未作为本次采用命题。
- owner `MODEL-LONG-CONTEXT`：[Ch22](../../../../../books/part-02-model/22-long-context.md)493–501已明确linear attention保S,z numerator/denominator；579–583已说明online ridge Gram/inverse让历史key几何影响下次写入，并将仅prediction-error分支与该统计分开。**拟已有覆盖**：这两处实际承载“当前readout不替nextupdate evidence”，本次保留exact-state/collision作为报告的新增验证，不为理论paper造新architecture或重复讲同状态责任。非排除候选；不改评分。不请求Books新段，待独立核验NC。

## 2610.13835v1 — Specialists Learn Faster

- 准入链：pretraining仅看同corpus总loss会忽略order塑造未来适配成本 → 同facts chron/shuffle改变最近知识specialization与后续update steps → 历史retention、当前query与future更新cost一起选择data order。评分2+2+2=6；必要机制/评价及owner完成。
- [exact-v1](https://arxiv.org/html/2610.13835v1)：§3–4.2/Eq1–2、§5.1–5.2/Table2/Eq3、§6.1–6.4/Fig5–6/§7。synthetic biographies，同records/三timestamp口径/110M350M682M GPT2-RoPE；chron是每person时间排序、并非全局所有records年月排序。dated/undatedquery不同目标；LoRA只新value CE，成功是Pnew>strongestPold，不是所有自由生成正确。specialists忘旧history，mixed旧shuffled/近windowchron提供局部折衷。
- 采用：order属于未来update条件，不只无关数据排列；conditional timestamp MI针对local empirical window的最佳predictor，不证明真实网络采唯一yearmechanism。step law N≈D/(ηA||g0||1)含校准A，初gradient近似平均speed，不授普适收敛/因果中介。same-editor/mixed数据、Gemma9B continued与versionedtools提供有限扩展，但不认证所有知识保持；新增CPT/数据组织/gradient测量与后续update费用须全计，不能以steps百分比代完整生命周期compute。
- owner `TRAIN-PRETRAINING`：[Ch28](../../../../../books/part-04-training-system/28-pretraining.md)145–153已有formation不同曲线/context用vsparametric写入、153提order但只内化压力，缺**同事实order影响futureoverwrite/injectcost、历史shuffle+近windowchron折衷**。拟在当前目标扩展前一段；dataset版本治理仍Ch27，不另做结构candidate。
- 逐字PRE：

相同事实集合的顺序也可能改变模型以后更新知识的代价，而不只改变本轮loss。对带版本或时间的同一entity记录，随机混合使模型需要区分多期值；按entity内顺序连续呈现则可形成偏向最近值的specialist，学新值较快却会损伤旧期知识。一条[有限数据组织分支](https://arxiv.org/html/2610.13835v1#S3)把旧历史shuffle、近窗口按entity排序，再分别检查dated/undatedquery、overwrite/inject更新和其他事实retention；它不要求全语料按全局年月排序，也不把更快适配当无遗忘。作者的step-law把初始log-probability gap、gradient和拟合常数联系起来，只是所测optimizer/adapter轨迹的近似，成功阈值更不等全部自由生成正确。重排、额外continued pretraining、梯度测量与后续更新共同计价，少update steps不能直接称生命周期省算力。时序不可靠、历史与当前质量或总预算回归时，保留全shuffle、可信replay和原更新器，不因较新数据而静默抹去旧知识。<!-- source-family:SF-2026-ARXIV-2610-13835 -->

## 执行同步

首五13630/13672/13821/13910/13895已按上文逐字PRE实际最小写入Ch17/80/66/23/15；13821经root修正为独立calibration set校准score+事先业务阈值。root实际nonwriter POST通过，本人末注已同步，五窄锁释放。上方首批条目保留写前proposal以说明审阅因果，但当前结果以本节为准。

原后八必要Source/逐字PRE与NC已由root独立定点通过：13617/13370/12995/13257/13202/12707/13835已实际最小写入Ch31/21/29/33/28，root实际顺读新增正文、完整邻接、diff及七末注，nonwriter POST通过。本人末注一度误带COAX的共享反侧模板，已仅七注改为各family自己的确切限制并完整读回，同步actual POST；五窄锁释放。13881的Ch22 numerator/denominator与Gram/inverse具体已有覆盖由root实际独核成立，不另造diff。原13为12实际整合+1已有覆盖，未核代码/复现，不授日级完成；以下新增8仍单独处理，不沿用原13证据完成标签。

## 本日新增8：日期与独立准入边界

13929/13816/13740/13732/13516/12818的官方Mon12身份与完整题摘由root实际读过；本人另在各exact HTML读完整题摘，13816读取官方abs完整题摘。12544/12530完整题摘原件为`runtime-generation-discovery-abstracts.json`，官方Mon12身份由root/runtime核实，本人独立题摘准入。下列均不以Submitted Oct8/9裁掉。未见官方入口撤回/纠错信号；只处理这8，不扩大窗口或目录。

## 2610.13929v1 — Chronos Policy

- 准入链：固定序号隐含固定采样/执行间隔 → observation capture time与action execution time分别进入attention，temporal randomization保原物理时间 → sensing变化与compute delay不再混成内容差异。评分2+2+2=6；必要Source和具体owner差额深入完成，未核实现。
- [exact-v1](https://arxiv.org/html/2610.13929v1)：§3/Eq2–4、§4.1–4.5/§5。action查询时间为request+estimated latency+jΔt；time-aware RoPE保持content不变，用各模态原capture time/未来execution time调制pairwise elapsed time。训练随机观测与延迟不重写timestamp；异步部署估计前次request latency，已过执行时间动作丢弃。
- 受限对照：Conveyor/vision-force Pivoting的temporal randomization单独分支、AddTime/RoPE比较，六quasi-static及三实机task。randomization无time在Pivoting反退；AddTime在Conveyor nominal更强，所以不宣称RoPE全面胜。异步/RTC与时间表示互补，当前仍fixed action rate，variable control frequency为future work。timestamp/clock/lag估计、训练增广与完整传感—执行延迟计价，模型输出时间不认证实际deadline或安全。
- owner `MULTIMODAL-EMBODIED-VLA`：[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)action chunk542–555已解释open-loop exposure，state ownership629–638已有timestamped observations，但未把capture与查询execution time分开进入policy attention。拟一段接action chunk基本staleness段，保controller权限。
- 逐字PRE：

固定序号的 action chunk 隐含观测和执行都落在同一时间网格；当多模态 capture 间隔、measurement delay 或推理时间变化时，相同 token 位置便不再代表相同物理间隔。可让观测保留各自 capture time，让 action token 查询预计 execution time，再以 time-aware rotary position 将 pairwise elapsed time送入attention，内容表示不必直接加时间向量；训练的 temporal randomization同时保留原timestamp，使时序变化可被解释。[Chronos 的有限对照](https://arxiv.org/html/2610.13929v1#S3)中，无显式时间的增广在多传感任务反而退步，RoPE也非所有nominal条件最优。异步执行仍需估计延迟、丢弃已过执行时刻的动作并由controller验收，当前fixed action rate不证明任意控制频率迁移。时钟/传感标定、增广训练、估计和完整控制链均付费；时间失真或deadline无法验收时，保留固定网格同步、短chunk、重新观测与可信controller，不让查询时间代签真实执行或安全。<!-- source-family:SF-2026-ARXIV-2610-13929 -->

## 2610.13740v1 — SmolWAM

- 准入链：零padding/空槽看似无内容便可删 → bias-free K/V的zero text slots仍承载softmax mass，布局/深度压缩又改变已学接口 → 压缩必须分别保归一质量与迁移layout，不能凭少token外推无损。评分2+1+2=5；决定准入的core与owner缺口深入完成，不只组合或11×数字。
- [exact-v1](https://arxiv.org/html/2610.13740v1)：§3.2–3.3、§4/Q1–4、§5及A.5直接single-flag。teacher约500zero text slots虽value零仍是attention sinks，截短后0/5、解析restore softmax mass后5/5，padding attention误差6e−8只是局部数值检验。individual近identity blocks可删不等联合可删；action queries保原slots，blank/layout移位会失败。distillation先teacher布局后compact，分开pruning与layout shift。actions不读denoised future、world head不在线decode，已有Ch26对此职责覆盖，不重写该通用边界。
- 400LIBERO episodes、单seed195、16-action open-loop；batch1 BF16 A100SXM4含preprocess/VAE但text cached。95.5% vs引用teacher98.2%不同既有pipeline；11×不是等成功率/全硬件匹配保证。Goal/Long明显损失；96contexts motion改善却LPIPS不胜copyframe；截短chunk8反失败，模型快不等反应更快；无真机/广任务。teacher cache与学生训练、interface/device输入变化和全控制费保留。
- owner同[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)440–474已有joint/video action的单向接口与删除future支路；新增只为**空text sink仍有归一作用、layout与depth分别迁移**。拟一段接Future-to-Action因果使用讨论的总开头后，不另向Ch17重复WAM接口。
- 逐字PRE：

压缩 WAM 的输入接口不能只数有内容的tokens：bias-free K/V路径中的零text padding虽不提供value，仍可吸收softmax mass，删去便改变其余tokens的归一权重。一个受限分支在截短text时显式恢复这份mass，再把保留原action slots的depth pruning与后续compact layout迁移分开蒸馏；单个近identity block可删，也不证明多个同时删除无损。[SmolWAM 的接口诊断](https://arxiv.org/html/2610.13740v1#S3)支持这种分责，但少量screen不能认证全任务等价，完整LIBERO中长horizon仍退步，world-head motion改善也未保持texture。动作不读future的接口本身不能承担压缩收益的全部归因。Teacher缓存、蒸馏、layout适配及完整编码/控制费用须计入；更快预测16-action open-loop chunk不自动提高reactive frequency。归一、布局或质量失配时恢复原padding/layout、较完整trunk与已验chunk/controller，不由零value或更低FLOPs批准删除与执行。<!-- source-family:SF-2026-ARXIV-2610-13740 -->

## 2610.13732v1 — LAPT-Scale

- 准入链：VQtransition目标可能丢细微变化，video latent不直接是robot action → diagonal-Gaussian continuous latent与perceptual/semantic/motion目标共同限定transition，同flow expert按阶段换监督并做embodiment alignment → capacity/目标与readout交接须分验。评分2+2+2=6；最小core确认具体差额后准入，必要证据与owner深入完成。
- [exact-v1](https://arxiv.org/html/2610.13732v1)：§3.2–3.3/Eq1–8、§4.3–4.7/Tables4–7、§5。两帧learned queries给32dim diagonalGaussian；decoder读current frame+latent change，KL/LPIPS/frozenDINO patch+CLS/stop-gradientRAFTflow targets，冻结LAM后取posterior mean作Stage1目标。Stage1 human latent chunks、Stage2 robot动作、Stage3task共享同Perceiver flow expert，不另adapter/reinit；pad到maxdim并mask无效loss。
- VQ与MSE-only比较只是LAM reconstruction/人类action classification，不是独立robot VQ-policy因果；flow去除损RT-H但PSNR可升，证目标不应只按重建像素；去Stage1/延长Stage2计算匹配仍弱。23.3Kh LAM固定，human policy数据1/3/5Kh，hand-only5K反退。实机7tasks单平台各20trial，latent replacement三examples只是camera-relative局部motion；不可授independent robotDoFs、广本体或物理安全。大量video筛选/派生labels/全阶段及robot250h成本保留。
- owner同[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)320–344已有forward/inverse、FutureVLA目标分工和hand geometry/shared embodiment head；缺continuous transition监督到**同一flow readout换target**与mask的交接。拟一段接forward/inverse预训练对照后，保邻接FutureVLA特权边界。
- 逐字PRE：

Human video 的 transition target还可以用连续posterior而非有限VQ codebook表达：由前后帧推断latent change，decoder同时读当前帧，以感知、语义和光流辅助目标约束变化，再冻结encoder取posterior mean给policy预训练。随后保持同一flow action expert，先监督human latent chunks，再换成robot原生action chunks并做embodiment alignment；异维padding的无效部分不参与loss。[LAPT-Scale 的有限消融](https://arxiv.org/html/2610.13732v1#S3)支持这条监督/读出交接，但VQ比较只诊断LAM，并未独立证明continuous latent使robot policy更优；更高PSNR也可能伴更差动作。连续坐标仍含camera-relative motion，不自动对应可独立控制的robot自由度，alignment与controller继续必要。视频筛选、latent标注、辅助模型、全部预训练/对齐与真实动作监督均付费；遮挡、ego-motion、本体差额或闭环质量失配时，保留VQ/普通重建、显式原生动作标签与专用policy，不以可迁移latent或同head授权跨本体执行。<!-- source-family:SF-2026-ARXIV-2610-13732 -->

## 2610.13516v1 — RESCUE

- 准入链：高failure AUROC不说明此时还能救或值得打断 → 同完整simulator/policy checkpoint分支continue/recover并按remaining time评价，falsealarm与freshattempt成本统一 → monitor需操作价值而非仅检测排序。评分2+2+2=6；直接设计反证受影响内容深入完成。
- [exact-v1](https://arxiv.org/html/2610.13516v1)：§III恢复/branch/Eq1–5与§IV/§V。保存完整robot+policy state、相同observed corruption，nativeπ0.5随机/弱policy额外armnoise，checkpoint replay fidelity是前提；K4→16仅near decision，Jeffreys .25quantile成功率估计；remaining horizon220−t，恢复耗20/30steps不刷新deadline；reset是renewal成本模型不是实际同状态branch。1341trunks/262fail、23430snapshots/128340branches属于所定义workload，不是独立物理试验。
- 66recoverablefailure中continue14、recover33、union34；恢复也可伤π0.5/弱policy。理想falsealarm预算仅成本模型下2–3.3%，nominal5%实际heldout7%；primary monitors无人低于never-intervene总cost，部分提高失败prevalence可有益，不采所有monitor无用。不可恢复physical世界不继承snapshots。脚本/分支采样/监视器、失败/恢复/新attempt和deadline全部计价。
- owner同[Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)655–665区分视觉偏离/失败、无恢复验证，1132区分识别/停止deadline；缺**同state的action选择value与falsealarm renewalcost**。拟一段接FIDeL前后两段后的binding end，不覆盖原监测权限。
- 逐字PRE：

即使failure判断准确，还须问同一时刻继续、恢复或reset哪项更有价值。若simulator能保真恢复完整环境与policy state，可从同一checkpoint配对分支，在同一remaining horizon内估计continue与指定recovery的成功和耗时，再把false alarms、恢复失败与fresh-attempt成本纳入预先声明的renewal模型。[RESCUE 的受限反证](https://arxiv.org/html/2610.13516v1#S3)中，恢复有时反伤成功，较准monitor仍因误报费用不胜never-intervene；检测排序不是干预净收益，模型下的误报上限也不是通用安全阈值。分支采样、恢复器、全部检测/失败/重试费用均须计价，恢复不刷新原deadline，物理机器人更不拥有任意checkpoint rollback。状态不可复现、操作值或尾延迟未获验收时，保留确定性告警、人工复核、短horizon与可信stop/controller，不让AUROC或反事实仿真自授continue/recovery权限。<!-- source-family:SF-2026-ARXIV-2610-13516 -->

## 2610.12818v1 — LeWAM: End-to-End World and Action Modeling with JEPAs

- 准入链：只学latent dynamics仍需另训/搜索action proposal → JEPA未来预测与action flow在masked MoT共训，isotropic约束用于表示，directpolicy或goal-conditioned refinement分开消费 → action proposal/latent cost/真实control分别验收。评分2+2+2=6；必要方法、control评价/反侧与owner深入完成。
- [exact-v1](https://arxiv.org/html/2610.12818v1)：§3.1–3.3、§4.1–4.4/Tables1–2与§5。modality独立QKV/FFN、共享attention；clean actions只向state query开放，noisyaction读history，history不反读actions，阻止间接clean-action leak。MSEfuture+actionflow+SIGReg随机投影characteristic-function标准Gaussian匹配，isotropy不是环境真值。planner先policy proposals→latent rollout→goal cost梯度refine，direct BC另训无goalcondition并只执行半chunk。
- noSIGReg rank collapse/PushTplanning−25.3；LeWM某objectprobe更好。goaled规划与no-goalBC不同目标不合并。实机3tasks各30tries，LeWAM均33.3% vsDP38.9%/π0.5 28.9%，端到端并非全面更强；13.3×是fullchunk GFLOPs ratio非wallclockSLO/同质量，scratchencoder与frozenVJEPA均有限任务；所测scale、接触/探索覆盖与未知object/view一般化未成立。训练、regularization、全部候选/rollout/refine和物理反馈计价。
- owner `MULTIMODAL-WORLD-MODELS`：[Ch25](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)279–301已有embedding metric/collapse/目标梯度；307–331有inverse anti-collapse与latentaction分支；缺**joint future/action flow的leakage mask与policy proposal/goal refinement两个消费者**。拟一段接原embedding充分性段，不向Ch26重复世界训练。
- 逐字PRE：

Latent dynamics也可与action flow共同训练，让同一表示既支持未来预测，又产生可被planner改进的动作proposal。接口须明确训练信息如何流动：state query读取history与clean action，noisyaction读取history与自身causal noisy prefix而不读clean action，history也不能反读clean action，避免间接泄漏；goal另作为action条件，随机投影的isotropic分布约束只是anti-collapse目标，不是完整world-state真值。部署可直接采样policy chunk，或在有goal时从这些proposals出发，经latent rollout/goal cost再refine，两者是不同消费目标。[LeWAM 的有限对照](https://arxiv.org/html/2610.12818v1#S3)支持共训兼容性，却不证明所有表示probe或physical task优于独立policy；operation-count比也不是等质量墙钟。共训、regularization、全部candidate/rollout/gradient与反馈付费，encoder metric仍须由行动结果裁定。goal、接触或proposal支持失配时，保留独立dynamics+policy、显式simulator、短horizon重观测与可信controller，不以latent距离、isotropy或自洽想象批准执行。<!-- source-family:SF-2026-ARXIV-2610-12818 -->

## 2610.12544v1 — Transformer-Based Masked Diffusion Models Provably Learn Distributions with Latent Structure

- 准入链：perfect mask predictor的并行误差分析不说明finite-sample learner如何形成 → MHMT低复杂度近似下ERM估计项与parallelization项联合界 → schedule/样本/architecture budgets共同决定输出分布误差。评分2+1+3=6；仅必要definitions/MainTheorem1–2/关键反侧深入，不读全部proof或采用附录examples。
- [exact-v1](https://arxiv.org/html/2610.12544v1)：§2/3/§4.1–4.2/Eq18–24。离散有限V、L，R个J-state HMT任意tree/transition/emission，模型类boundednorm/稀疏/clip logits，i.i.d.n样本与exact empirical-risk minimizer，同fixed-cardinality schedule训练/测试、揭示集合随机且value-independent。输出**保留partition**的expected KL(p*||pY|S)≤C[εparallel+smax ProjMHMT+L Kpar/n polylog]，Kpar=R[LJ(J+V)+J³]。网络budget仍依赖n,L,V,J,R，不知tree/latent不是任意architecture无hyperparam知识。
- 支持低结构statistical复杂度代指数support，但不证SGD找到ERM、learningcompute polynomial、真实language分布是MHMT或wallclock采样；小J/R不自动小DTC，一般tree不都像star；misspecification乘smax，增加并行会放大近似项。T≈DTC/ε只在所给schedule/条件，notuniversalerrorfloor。不采用全continuoustheoryexamples或proof细节。
- owner `MULTIMODAL-GENERATIVE-PARADIGMS`：[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)546–548已有learning/factorization error与finite样本代理污染；**generic拆误差已有覆盖**，新增仅MHMT approximation/finiteERM项与parallelwidth共同放大。拟一段紧接现tau-leaping受限理论两段后。
- 逐字PRE：

把这两种误差同时降下来，还依赖learner能从有限样本拟合哪些条件分布。对接近少量hidden Markov trees混合的离散分布，一条[受限Transformer理论](https://arxiv.org/html/2610.12544v1#S4)用指定bounded模型类的exact ERM，将输出的expected KL界拆成parallelization、按最大并行宽度放大的结构近似误差，以及按序列长度放大的有限样本估计项；未知tree/latent不必作为训练输入，但architecture预算仍依赖长度、词表及结构规模。低复杂度潜结构可避免按指数support计样本，不代表每种tree都有小并行依赖，也不证明SGD有效找到ERM或真实语言服从该结构。样本制备、训练/优化和完整采样预算仍须独立验收；近似失配、样本不足或计算不可行时，保留较窄并行、原confidence/fixed schedule与逐位置采样，不以statistical可学习界代签优化效率、wallclock或任务正确性。<!-- source-family:SF-2026-ARXIV-2610-12544 -->

## 2610.12530v1 — CacheScope

- 准入链：raw shallow-probe change混入input displacement → Δy/(Δx+ε)提沿当前方向的gain并累计到exactanchor，固定reconstructor比较exactplacement → sensitivity与trajectory移动分开而非更复杂重建。评分2+2+2=6；必要core/匹配scheduler/直接反侧与owner深入完成。
- [exact-v1](https://arxiv.org/html/2610.12530v1)：§Method/Eq2–12、Tables1–2、Ablation/Conclusion、B.3/C.1–4/D.5–6。固定baseexact和boundedfirstorder DiCacheΓ，补充exact仅在原reuse步触发，累计score后freshanchor归零；CFGbranches分开history/accumulator。score是localdirectional relativegain非globalJacobiannorm/errorbound；exact在已近似latent只刷新当前轨迹，不复原originalfull轨迹。dev16仅count校准averageextraexactbudget，test32冻结阈值，不是每prompthardcap/免校准。
- FLUX50steps1024²/Wan50steps81frames832×480/OpenSora30steps51frames480p，RTX PRO6000D单GPU，同seed/配置，全latency含fixedtext/VAE但loading除；precision、batch/concurrency未在已读设置披露记Not Disclosed，serving SLO不适用该离线generation比较。同probe/Γ/warmup/cachematchedskip D/M/S ablation，LPIPS paired promptbootstrap/sign/BH、seed43有限replication。Wan SSIM切片不占优，primaryLPIPS不是semantictruth；多historyreconstructor更弱只限examineddesign。一次shallowprobe方向/coeff/probeconsistency是限制，新增input/outputstate/calibration全部费，不授生产SLO。
- owner同[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)1574–1595已解释trajectoryconsistentprior与perchunkdisplacement，但无**input-normalized probe与当前轨迹anchor**。拟一段接cache误差开头/现sourcefamily binding后、block-specific复用段前；保全原近似/刷新分支。
- 逐字PRE：

缓存刷新sensor还须分开“输入沿轨迹移动多少”与“网络对这次移动响应多大”。固定浅probe和重建器后，可用probe output的相对变化除以input相对displacement加ε，形成沿当前方向的gain，再从最近exactanchor累计，超过校准阈值便在该步继续完整forward并重置anchor；CFG两条轨迹各保自己的统计与cache。[CacheScope 的matched-skip对照](https://arxiv.org/html/2610.12530v1)支持改变exact-compute位置，但这不是globalJacobiannorm、最终error或语义风险界，exact刷新已近似latent也不回到原完整trajectory。开发集只按平均extraexact预算校准，不能称每prompt硬上限或免校准；有限图像/视频LPIPS改善伴某些SSIM反退。Probe、双份统计、校准和全部编码/解码/刷新付费；方向代理、阈值或质量失配时，保留raw displacement、更多exactanchors与full recompute，不把低scheduler开销或保真指标自签无损/SLO。<!-- source-family:SF-2026-ARXIV-2610-12530 -->

## 2610.13816v1 — Dream to Remember（本窗必要正文隔离）

- 完整官方[abs-v1](https://arxiv.org/abs/2610.13816v1)题摘读回；准入链：frozen generalist仍会因learned steering适配遗忘 → worldmodel旧行为rehearsal与新task优化依赖不同fidelity → freeze/replay与新任务environment budget须分责。评分2+2+2=6，不因访问失败缩池。
- exactHTML为404；网页exactPDF返回16906920bytes tooLarge；一次有限替代直取exactPDF45s timeout只得1250550bytes，partial PDF未用于证据。root另授权today_institutions一次后台有界≤120s恢复，对方实际约99s仅得2.64MB/16.1MB即终止、未解析/采用，不开多路重抓。完整必要正文仍不可得，已穷尽该bounded primary尝试，不无限找附件。题摘的CALVIN/LIBERO/Franka数字与方法声明只保作者摘要身份，不作为正面Evidence、Books采用或性能/安全保证。
- 暂缓/受阻精确需求：取得完整exactv1 PDF或作者与该版本对应fulltext，定点读steering/noise路径、worldmodel旧技能rehearsal及新任务environment-vs-imagination选择、matched forgetting/新task对照与直接失败条件。先比较Ch25 continualdynamics输入漂移/Ch26 onlineRL冻结policy的具体段落，不因同topic直接NC。当前无BooksPRE、无写入；待原件可得只重开此family，不阻塞其余已可执行项。

## 新8当前执行同步

7可读项必要Source、准入/评分与actual-owner最小逐字PRE经root逐条独立定点通过，13816保持必要正文隔离/无Books。root授Ch26/25/24局部及本人末注独占窄锁后，today_models已实际最小写入并读回正文/前后邻接及七末注：13732 Ch26:328、13929:560、13516:666；12818 Ch25:295；12544 Ch24:554、12530:1586。root实际完整邻接/正文/七注POST核事实边界通过，发现Smol在引言与首个mask实例之间打断论证；按其要求保全部段内内容，仅移到2603-17240 action-only共同backbone段后、未来条件段前，并加“在这种单向接口下，”衔接，当前13740 Ch26:472。末注为Ch26:1751/1753/1755/1757、Ch25:1458、Ch24:2105/2107（并发其他合法写入可移动行号，family marker为稳定定位）。其余六actual POST已同步本人各注并完整读回，Ch24/25锁释放；root进一步实际读核Smol完整迁移后的新邻接，最后迁移POST通过，本人末注已同步/读回，Ch26锁释放。未删旧正文，局部diff-check通过，不自授本日DAY完成。

本分支最终21唯一family：19实际最小Books整合（12原项+7新项）、13881具体已有覆盖、13816必要正文受阻安全隔离；ordinary可执行待办0、Books窄锁0，不恢复新日期。19均由root非写入者完成必要Source/PRE及实际POST；13881 NC同样root实际独核。13816不计Evidence通过、不为正面Books/性能/安全/无遗漏断言支撑，精确重开条件保上文。本文件仅本分支证据与采用链，正式日报与全分母/来源覆盖/非作者DAY由root及指定整体验收者负责。
