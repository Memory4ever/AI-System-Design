# Apr24 精确采用提案

## 21160 → TRAIN-GRPO Ch33

必要原文：2604.21160v1 §3.3–3.5/Eq6–16、§4.2/Table3、§4.5；字段 char-span→token 对齐、四组局部归一与 background credit 为当前 Sequence Reward 段真实缺口。6分 gap Deep；尚未独立采用/写锁/实际写后，不计 I。

插入位置：Ch33「Sequence Reward 怎样作用到 Tokens」通用 process-reward 说明之后、正确子集 auxiliary reward 之前。拟正文两段：

完整回答含多个结构字段时，终局 reward 广播会让不同字段的错误共享同一 credit。一种条件分支先按可解析输出识别字符区间，再用累计解码 offset 映射回 token；分别对几何字段构造组内相对信号，只更新对应 span，语义与格式 background 则使用明确的混合规则。这里拥有训练信号的不是字符串位置本身，而是 parser 版本、字段定义、char-to-token 映射与各组 support；多个字段与 background 的归一不能默认为一次完整回答归一。预测3D与预测2D一致只是内部一致性，GT box containment也不等于关键点坐标正确，最终几何验收仍要独立。

该分支增加解析、对齐和字段 verifier 成本。malformed 输出、一个 token 跨字段、重叠 span及零方差组需要明确工程处置，而不是把不可解析部分静默丢掉；这些是我们的 admission 要求，不是作者已验证的防御。受限 Point-VLM 实验中，field-credit-only 的3D IoU略低于 broadcast，加入一致性分支才局部改善，所以不能把粒度更细直接写成质量更好。字段 oracle 或对齐不可靠时，完整回答 reward 仍是更稳妥基线；Qwen2.5-VL3B/PointBERT、ShapeNet、4×A800、SFT/RL预算不外推任意JSON任务或机器人安全。

## 21741 → MULTIMODAL-EMBODIED-VLA Ch26

位置：human-online-RL两段后、训练侧teacher action-delta前；必要§3–4，6分gap深入，待非作者采用/共享锁。

人工纠正也可以先改变数据采集位置，而非直接更新真实在线策略。action-conditioned world model中的闭环policy进入失败风险状态时，由人提供短纠正动作，再把控制还给policy；缓存模拟中间状态可从同一失败前位置回滚并产生多条纠正分支。这让稀缺机器人reset和人工在场时间转成模型状态复用，但缓存的是预测分支，不是可回滚的真实环境；训练样本需保留分支起点、动作、生成器及纠正者身份，不能把模拟成功复制成已发生的物理事实。

纠正片段与真实示教合并posttrain之后，仍需在真实机器人上验收。失败/边缘状态覆盖能改善局部校准，却不由有限相关系数保证所有失控状态可信；分支多样性还可能只是生成器共同偏差。它增加world-model训练、人工筛选与数据发布成本，收益也与纠正片段的支持分布耦合，不能唯一归因rollback。超出已校准工作区、接触状态失真或模型预算不足时，保留真实机器人短纠正与保守控制；低层safety和环境真值职责不移交给human-in-model接口。

## 21632 → MODEL-EMBEDDING Ch12

位置：输入/输出weight tying段之后、Padding梯度边界之前。必要§3–6/AppA/B/E；6分gap深入，以下为待非作者采用的条件性正文，不写未限定学习率的普遍定理。

共享输入与输出矩阵除了节省参数，还耦合了训练支持。没有作为正确label出现的token，虽然输入lookup很少更新，输出softmax归一化仍会对其行产生梯度；在bounded features、小GD/SGD步长及weight decay相对未见类概率足够强的条件下，不同未见输出行可能趋近。新符号因此不仅难以被生成，也可能在共享输入空间中失去区分度；增加copy路径解决从context到输出的读出，不自动解决多个近同向符号的表示。

冻结或周期reset行、增加符号diversity、额外copy head是不同干预，应分别检验符号区分与原语言质量。受限逻辑模型及Gemma unused-row实验支持这种风险，但冻结行会损害C4 loss，cosine相似也不是推理失效的充分因果证明；原Lemma的未限定η版本缺小步长前提，AdamW现象不能靠GD定理直接担保。普通可训练embedding仍合理，真正需要新token时先核初始化/监督支持，再选择有限局部干预，而非全表永久冻结。

## 21724 → MODEL-EMBEDDING Ch12

位置：Hashed N-gram Capacity碰撞/热点与allocation frontier之后、输入/输出共享之前。必要§4–5.5；6分gap深入，待非作者采用。

把参数放进词法表之后，容量仍取决于哪些row得到训练。频繁token占专用槽、尾部token按平衡频率分桶并混合alias与多hash，可以将有限更新分配到更少的共享槽；读出后再用局部causal卷积与非线性提取器形成动态n-gram，而不是将一次hash结果直接当成熟语义。按层注入value或residual又改变同一表对各计算层的职责，需要联合验收更新覆盖、冲突、提取器与层位，不从更平的频率proxy推出无冗余概念。

共享表和预取有参数、host/device搬运及缓存成本；注入当层value虽不必重算当层Q/K，后续表示与计算仍会变化。受限backbone和memory配置存在2×优于4×等非单调结果，层位消融也有参数量混杂，不能承诺所有扩容都改善或零FLOPs。简单静态lookup在预算紧、词法短路风险高时仍更清楚；采用该分支需把table/hash/提取器/gate作为联合训练资产，不把带宽估计当线上延迟保证。

## 21700 → PLATFORM-SECURITY Ch72

位置：Backdoor Evaluation trigger邻域及训练强度矩阵之后、Coalition前。必要§III/IV-A/C–F；6分保护深入，待非作者采用。

长答案的目标片段还引入另一项训练选择性：全回答loss可把一个被植入的短片段稀释，具有模型适配或隐藏系统配置写权限的提供方可以另用目标片段loss，在poison输入强化、benign输入抑制同一输出。自然风格触发不必是固定怪字符，因此输入PPL、流畅性或一组exact trigger的低ASR都不能独立排除这一资产风险；需把注入权限、风格邻域、目标内容与benign误激活分别放进冻结评估。

逆向生成trigger或输出探测也只有受限sensor权力：正常无害prefix可能将模型输出引向另一方向，一次反演未找到目标不等后门不存在。所测LoRA/隐藏prompt权限、poison率和有限下游输入已有较高benign FPR反例，不推任意无权限用户攻击或所有防御失效。高风险模型资产仍需独立来源/adaptation授权及效果canary；这些工程边界不是本研究验证过的普遍防御证明，普通低风险输入probe则保留其有限证据范围。

## 21590 → TRAIN-DATA Ch27

位置：Synthetic data的generator/judge同源错误说明之后，原生成要求×模型规模分支之前。必要§3.1–3.3/Algorithm1、§4；拟正文未写、待非作者采用与锁。

从一条可执行轨迹合成任务，能保持工具顺序，却可能只教会模型一条固定路径。一个模拟数据分支先把轨迹展开为条件行为树，再选择一条支路反推使它必需的环境状态、用户目标和Agent操作说明：环境决定可选动作，用户请求给出目标，SOP描述允许的条件策略。比如用户要求补偿并不产生补偿权限，任务应把真实资格放在工具状态而非用户话语中。这里改变的是训练样本的触发条件和输入职责，不是让模型自主改写线上授权。

这种逆生成增加mock状态、分支检查与合成成本；强模型走通预定路径或同模型多次回答一致仍可能共享错误，不能替代真实工具和独立outcome。应保存支路与三类输入的lineage，先以受控模拟验收，再用真实轨迹/权限canary检验迁移，这是工程要求而非已有普遍防御证明。目标失配、模拟器状态不足或生成预算有限时保留固定真实轨迹与人工检查；两个数据flywheel和多轮训练的综合收益不唯一归因这一步，也不保证持续变难总会提升能力。

## 21511 → AGENT-RAG Ch76

位置：检索表示的单/多向量成本段之后、数据面多向量搬运之前。必要§3–7；本条拟正文，未写/未通过采用。

倒排检索并不必把每个维度永久绑定到 tokenizer 的词。词法维度保留精确标识符和可解释匹配，在语料变更频繁时很直接；另一条分支先从冻结编码器的上下文状态学习稀疏字典，再用检索目标联合适配编码器与字典，将查询和文档的非零 latent 权重交给倒排执行。它改变的是检索输出空间与训练职责，而不是宣布每个 latent 已成为跨语言稳定的语义真值。逐 token 保留 TopK 后，跨 token pooling 仍可能使文档表示变密，因此重建、相关性训练和聚合后的 posting 预算要分别验收。

这条分支增加重建预训练、检索适配和索引重建成本；作为系统资产，编码器、字典及 postings 应按同一检索 revision 联合发布，这是基于索引可比性的工程判断。受限 DistilBERT/MSMARCO 与多语实验有域内、语言切片退步，posting 访问预期不等于真实延迟，启发式共现也不是概念正确性证明。精确词查询、预算紧或语料变化快时保留词法/原SPLADE与固定hybrid；不能用新的“概念”名称掩盖匹配错误或承诺无成本多语迁移。

## 21549 → PLATFORM-EVALUATION-SYSTEM Ch66

位置：自动metric与人工残差校正/总体prevalence MLE两段后、Risk–Coverage前。必要官方PDF物理3–9页；拟正文未写/未通过采用。

总体估计还有一种会被全局 calibration 隐藏的风险：旧群体不同切片的正负残差恰好相抵，总体平均正确，但目标流量重新分配切片权重后，原来的抵消就不再成立。若目标只改变这些可观测特征的分布，标签条件规律保持稳定且支持重叠，可以在有代表性的人工标签上约束可重加权组的条件平均残差，再汇总预测估计新群体 prevalence。它补充的是 estimator 的条件，不是把每条模型标签升为事实，也不由高 AUC 推出总体无偏；多重校准比平均组误差要求更强，有限拟合不自动满足所有组与分数区间。

条件校准用标注与更细分组换取可迁移的测量设备，也会增加小组方差、特征选择与支持覆盖责任。受限 LLM 文本分类中，新的文档类型仍有偏差，离散标签加 metadata 有时优于概率自报；因此输入分数、分组、标签和校准 revision 都是测量身份，不能只记录一个校准数字。目标出现新特征值或条件标签规律漂移时，要补标注、扩大不确定区间或回退原有人工作为 anchor，而不能沿“任何 reweighting”理论条件声称任意未来分布无需重估。

作者 apr01。必要证据位置/配置/日期原字段见 `V3_EVIDENCE_NOTES.md` 对应七家族；以下只是拟正文，未获独立采用和共享写锁前不写 Books，不计 Integrate。恢复本轮已实际读取当前 AGENTS/合同、ROADMAP、项目背景/学习理念/写作指南、相关checkpoint与七项目标相邻正文。日期沿官方赋号/Thu20EDT slot、邻批与exact-v1处理簇的有据08–09推断，非Updated孤证；不外推21例外。无需重复所有附件，非作者围绕下列命题核必要源与实际owner即可。

新增两项在同一提案文件维护，不另造平行账本；不是所有拟准入均进入Books。

## 21275 → TRAIN-DATA Ch27

位置：lineage连接checkpoint/data cursor段之后、从Shard可见到Batch原子发布之前。必要§III–V；manifest只固定输入身份，下面补正常并发读取顺序，不声称故障恢复或全训练bitwise确定。

数据版本和shuffle种子固定之后，训练看到的顺序还可能由执行调度改变。多个worker竞争共享任务与结果队列时，领取的rowgroup与返回速度都受线程、网络及CPU转换影响，同一manifest并不自动组成同一batch序列。一个受限实现给worker独立队列，按固定round-robin分派，再按相同顺序合并ready结果；它把输入序列的决定权从完成时刻转移到reader调度。并行转换与缓存仍可进行，但慢worker会阻住后续有序提交，故吞吐与确定顺序要分别验收。

缓存还要区分原始bytes与已转换的训练数组：把转换下推worker并缓存后者能同时避开重复网络和CPU工作，却增加内存/磁盘、quota回源和线程退出管理。上述正常路径只在相同rowgroup、worker配置与RNG条件下支持有序读取，不证明worker重启、扩缩或全训练数值确定；推荐训练中的loss/MAP对照还同时用了其它稳定性技巧。离线串行或顺序不影响目标时简单共享池仍合理，需要恢复时仍由cursor/checkpoint声明已消费序列，不能由一条固定seed补造exact replay；下节再处理已生成batch的原子可见与回收。

## 21254 → MODEL-TRANSFORMER-LAYER Ch17

位置：Residual Stream多流mixer/Sinkhorn与go-mHC分支之后、Parallel Tracks之前。§2–4.3；与Ch18共享循环/停止、Ch49量化artifact交接。

混合状态的频率也要与计算和权重预算分开。普通逐层mixer随每个子层更新状态；当中间block被反复使用以节省参数驻留时，可以保留多条residual stream，只在整轮block结束后混合，再进入下一轮。输入/输出混合加diagonal sigmoid carry不是双随机守恒，也不保证方向完整或梯度稳定；loop-specific位置与少量参数还意味着并非所有权重都严格共享。这是用较少混合调用换不同状态更新节奏，不能从较少参数推出更少activation、KV或总执行工作。

共享权重在各轮看到不同activation，量化校准也需覆盖这些轮次，而不是只收第一轮画像。受限语言模型对照支持该架构与INT4的某些质量/权重取舍，但depth-matched不是compute-matched，部分过训练PPL与训练吞吐反向；没有证明动态早停或线上延迟下降。需要成熟并行、固定延迟或状态复杂度低时普通residual stack仍合理，混合/校准失配时回退普通loop或非共享层，第18章再处理停止语义。

## 21326 → MULTIMODAL-REPRESENTATION Ch23

位置：Fusion早/晚原则后的text-conditioned earlyfusion取舍两段之后、multimodal ICL路径之前。§3–5/A.3；检索排序后续Ch76不重复owner。

融合点的选择还受**实际可见模态集合**约束。独立视觉/文本encoder保留专用特征，decoder用同一个query跨读两组KV可以在末端形成统一检索表示；但训练长期依赖caption时，视觉支路仍可能在无caption输入上塌缩。一个受限训练分支把单模态读出的embedding随机混入联合表示，并按比例删除caption，让同一个contrastive objective同时承担完整与缺模态输入，而不是部署时才临时删一条支路。

该分支增加多次表示计算、caption-ratio与mixin校准及负例重建成本；比例过强或无caption也可能损害语义桥，检索近邻重叠不是真实语义或答案正确性。T5/CLIP、两个改造数据集的消融只支持所测缺模态分布，部分纯文本slice低于baseline，不证明所有早/晚融合都应改成FiD。模态集合稳定、隔离或低耦合优先时保留独立/晚融合，部署缺失模式超出训练支持时另验收或回退单模态检索。

## 20985 → PLATFORM-SECURITY Ch72

位置：`Differential Privacy 先定义被保护对象` 的 post-processing说明之后、production contract之前。来源v1 §2–5/6.1–6.3/8.1–8.2。与Ch30合并utility交接，隐私会计唯一owner在Ch72。

多个私有训练资产也要先区分**实际发布什么**。以公开或非敏感规则随机只选一个模型发布，可以按各资产的privacy profile对混合分布作会计，不能等同把全部模型公开；线性合并只发布最终参数时，若只知道各资产profile，保守边界仍可退回联合发布的composition。更紧的训练轨迹会计则需要clipping、sampling、学习率/合并权重和各run噪声的独立性，不能直接“平均epsilon”。同run checkpoints共享早期随机更新，不属于独立噪声的这一分支。

因此selection规则、资产随机性lineage、privacy unit和历史发布集合都进入release identity。私有validation驱动的选择或重复发布需另行会计，post-processing也不能退还已消费的历史预算。此分支增加资产比较和accountant成本，并不证明模型合并的utility；现有裁剪均值、MNIST与CIFAR受限证据不足以推出LLM质量。独立性难以恢复或新的会计收益不足时，保留composition边界或只发布原资产；第30章再处理非隐私的参数融合取舍。

## 21330 → MODEL-MOE Ch21

位置：负载均衡auxiliary与计算价值teacher分权两段之后。必要证据§3/4/5.1–5.4/J.4，与offline contribution prior和upcycling初始化蒸馏不同；6分gap深入，但仅提案，未授权/未写。

训练期的assignment信号也可以来自外部dense模型的feature空间，而不是只从当前被选expert获得任务梯度。一条受限分支冻结dense backbone，在其中间features上另训练仅受负载与熵约束的辅助router，再将其分布停止梯度作为student router的KL目标。固定的是feature提供者，不是辅助router本身；这能在稀疏task反馈之外提供平滑选择目标，却没有把均衡proxy变成每个token应由哪个expert处理的语义oracle，也不同于从现有激活路径虚拟移除expert得到的任务贡献先验。

指导时间与teacher层位都要计入训练identity：所测视觉模型中，早期指导、末层features和只模仿路由有不同甚至反向结果，外部router在线推理的upper bound不能用作部署收益。它需要dense teacher资产、额外features与辅助loss；列出的epoch时间小幅增加且参数总量排除teacher，不应称零成本或证明任意LLM路由稳定。任务反馈充分或指导失配时保留原Top-k联合训练、较短指导时程与已验收负载约束，并由训练与runtime分别测质量和真实负载。

## 21343 → MULTIMODAL-REPRESENTATION Ch23

位置：完整patch teacher监督两段后、latent检索预算前。必要§3.1–3.3/Eq9–12、§4.1–4.6直接反证；6分gap深入，未授权/未写。

腐化位置与恢复责任也可以跨越视觉encoder和语言模型的边界。视觉patch经过projector进入语言空间后，对选定tokens加噪声或遮蔽，再在语言模型中间层接训练期decoder去恢复冻结视觉encoder的clean patch targets，并联合关系与同图patch判别目标。它与前述encoder预训练的完整patch监督不是同一责任：这里希望视觉信息穿过语言模型内部仍可恢复，原答案loss也继续存在；teacher features是表示目标，不是视觉事实真值。

腐化与辅助decoder在部署时撤掉，不代表额外训练免费。受限LLaVA/Qwen视觉问答中，clean指标仍有退步，CKA或kNN改善也不能独立证明收益全来自语义对齐；latent corruption训练与pixel噪声测试的迁移更不能变成任意污染鲁棒保证。腐化比例、saliency和监督层位需要随模型与任务校准，并分别验收clean质量、视觉证据保持和外部污染切片；成本不合算或clean损伤明显时保留普通答案监督与已有patch对齐分支，必要时恢复完整视觉读取而非依赖重建置信度。

## 21079 → MULTIMODAL-REPRESENTATION Ch23

位置：`固定表示之后，可以按未决Claim主动补充Observation` 两段后、任务贡献与可靠性Gate前。来源§2.1–3.3/4/Table3/AppC。当前已解释proposal/assembler，但缺单AR轨迹动作头及correct-only面积训练职责。

主动观察还可以从外部多轮工具调用变成**同一自回归轨迹中的取证动作**：离散标记决定是否foveate，当前hidden state回归连续区域，crop编码后作为新视觉状态接回正在进行的推理。训练需要分别承担普通答案token与观察动作的职责：先以文本和区域监督建立路径，再用动作收益及只在正确回答条件下启用的面积正则约束“看哪里、看多少”。小crop本身不是好证据，不正确时不能单靠少读区域得到奖励。

这个分支省去独立规划往返，却仍支付crop编码、新视觉KV与路径依赖；保留全部新增视觉时，缓存会随观察数增长，并非exact复用旧完整输入。区域错误可能形成自确认，过强面积惩罚也会损失必要细节。Qwen2.5-VL单图实验只支持所测训练与任务，尚不覆盖视频或生产tail；静态证据已经充分、额外动作收益不足时固定读取仍合理，取证不确定时扩大区域或回退完整观察。

## 21100 → MODEL-LONG-CONTEXT Ch22

位置：GatedDeltaNet状态更新/固定state取舍之后、混合训练预算之前。来源§2.3/3.1–3.5/4.1/4.3/E.3。原delta/gate/momentum没有曲率预条件的精确→近似执行链。

写入误差之外，key的历史几何也能决定如何改写状态。在线ridge least-squares维护key Gram矩阵及其逆；在声明的初始化与可逆条件下，可以把query端预条件读取等价改写为key端预条件写入，利用Sherman–Morrison更新保持同一状态关系。它不是再保存全部token，而是让长期重复或相关key改变下一次写入方向，避免把当前误差和已有方向的曲率完全混为一体。

精确inverse引入顺序依赖与额外统计；以diagonal second moment及前缀统计换chunk执行，就不再拥有精确两端等价。实际decay/gain、log-centering与squash也属于训练稳定措施，不是全局稳定定理。340M/1B受限实验有额外preconditioner成本和若干任务退步，不能把NIAH或recipe差异解释成普适长文收益。统计成本不划算时保留原delta/gated分支，需要精确历史回读时继续使用显式Attention或retrieval。

## 21106 → TRAIN-PRETRAINING Ch28

位置：`Scaling不是只增加参数` compute-optimal总论之后、模型压缩baseline之前。官方PDF-v1 §2–6/AppA；当前预算分账缺unique parameter与execution depth轴。

循环共享权重进一步拆开了**独立参数容量**和**实际执行深度**：相同有效blocks下重复一组参数可以减少weight memory，却仍运行重复blocks及反向传播；固定训练FLOPs时，宽度与可消费tokens必须一起调整。因此dense的参数–数据最优分配不能只把共享后的参数量代回原公式，应在声明的recurrence、输入注入和执行预算下重新拟合质量frontier。

固定20个有效blocks、full BPTT及六预算的116-run证据支持这项分账，但其共享容量指数只是该范围拟合，所测dense frontier仍占优。v1没有证明truncated-BPTT或hyperconnection可弥补差距；优化稳定性、kernel与wall-clock也不由参数下降自动改善。共享weight的服务内存确实是约束时可继续比较这一分支，知识容量或训练效率优先时保留dense baseline，第18/22章负责循环状态语义而不是把经验拟合当通用容量定律。

## 21189 → MULTIMODAL-EMBODIED-VLA Ch26

位置：`离散控制周期要为SafetyFilter预留一步可达域` 后、ActionLatent前。来源II-A/B、III-A–D/Theorem1、IV/V；旧段负责时间采样，新分支负责空间表面覆盖。

时间裕量还不能证明机器人**整块表面**都安全。有限body点若构成连续表面的epsilon球覆盖，先把自由空间向内侵蚀epsilon，再约束每个点留在缓冲空间，才在该几何条件下推出表面避障。基于密集点云的实现还要计入原点云逼近误差delta，实验中的epsilon+delta缓冲与fully-free voxels不能简化为“Poisson-disk点间距够大就覆盖全部表面”。同一Poisson场供各body点查询，再由joint-velocity QP和低层跟踪执行。

覆盖更密或缓冲更大增加查询、保守性和不可行风险，并不消除QP失败：所测较大epsilon及缺少可动自由度时仍有不可行。已知动态障碍几何和状态、受限FR3/UR10e结果也未解决未知感知、自碰撞或全部执行扰动；PDE/OSQP平均时间不是WCET。应与上一节离散可达裕量共同验收几何、时序与actuator，条件不满足时保留低层约束、降低速度、急停或停止高层proposal，不能由优化器存在授权物理动作。

## 21215 → MODEL-LONG-CONTEXT Ch22

位置：YOCO-U局部循环/全局KV两段后、`从线性混合到原生稀疏` 前。来源§2.1–2.3/4–7/E.4。区别于跨层共享及fixed-state recurrence。

递归也可以发生在**同一层的时间轴**，而不是把一段网络重新执行：过去位置的persistent KV来自该层输出，当前位置先用层输入的temporary KV避免自身循环，取得输出后再提交为未来可读历史。这增加有效的时间递归路径，却仍保存逐token历史，并非把上下文压为固定state。状态身份必须区分temporary输入表示与persistent输出表示；第45章消费这个模型合同，不能把两者按位置相同就视作普通KV。

当前位置之前的输出存在顺序依赖，但未来query只依当前层输入，可预先计算；将已形成KV tile的在线softmax统计提前累计，可降低HBM访问而不消除二次Attention FLOPs，也不消除MLP顺序瓶颈。checkpoint重算、位置优先布局和专用反向都是交换代价。初始化uniform-attention简化稳定结果不覆盖所有learned attention，150/300M逐层测量亦排除embedding/readout/loss，优化decode仍是未来工作。普通Attention或YOCO分工在并行执行更重要时继续成立，不能把公式少存KV写成已测生产加速。

## 21221 → MULTIMODAL-GENERATIVE-PARADIGMS Ch24

位置：Salt历史conditioning训练两段后、组合一致性监督量之前。来源§3.1–3.5/4.1–4.5/Tables1–3。Ch49仅handoff执行，不重复生成训练owner。

历史conditioning质量之外，还要让训练覆盖**实际保留和读取策略**。一条原生稀疏AR视频分支把完全denoised历史保为persistent anchors，local窗口承载近处与当前denoise；退出local的候选由coarse pooling提出，再保留有限anchors与sink。读取时persistent密读和local Top-K进入同一个masked softmax，DMD训练就使用这套动态cache和mask，而不是训练完以后才裁剪历史。pool summary只有路由权，被丢弃的旧细节并未因此可无限恢复。

它以anchor维护、选择与训练反向换较小active读取；去掉persistent在所测配置更快却损质量，短片也有质量切片退步。Wan1.3B受限训练、有限20/60秒评价和kernel数据不证明无限一致性、物理world真值或完整生成SLO；实际PBSA artifact由第49章按硬件与执行路径验收。动态策略漂移、细节不足或训练/部署mask不一致时，应提高历史预算、回退full-history/dense或恢复原训练，而不是把更稀疏作为独立发布理由。
