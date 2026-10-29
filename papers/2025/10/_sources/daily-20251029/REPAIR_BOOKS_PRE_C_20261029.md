# Books C整体PRE：完整新增、独立marker、本人注及实际邻接

以下七处精确gap，未SAVE；沿当前owner主线，不授权整章。Writer已加载当前Books合同与owner/相邻交接，全文如下供整体PRE。自身最终全自读与请求见canonical后到记录，不以本文件生成代替。

## 22115 · books/part-04-training-system/38-pipeline-parallel.md

唯一段首：`### Split-Backward 与低精度状态`

### 实际前肩

序列长度差异还可在不切断样本身份的前提下进入1F1B：将超长因果序列切成有前后依赖的token块，把短序列按容量打包，再按stage选择保留哪些块内激活、哪些在反向重算。[InfiniPipe的受限v1](https://arxiv.org/html/2509.21275v1)用这一分工联合选择切片与重算，但长序列的后块仍依赖前块K/V，反向对前块的dKV也有自己的回收边界，checkpoint并未取消这些跨块状态；packing还必须保持各原样本的mask、位置与target归属。相似块数分组可减少局部等待，却增加多次填充/排空和规划开销，不能由受限cost model的最优解批准所有硬件或在线形状。样本/有效token的loss与梯度权重、RNG及最终optimizer提交应另作一致性验收，短程吞吐对照不证明同SGD或相同收敛。CPU规划、profile、打包、所有K/V与dKV驻留和传输、重算与独立质量回归均计费；依赖、容量或净收益不合时，保留完整样本的GPipe/1F1B、固定packing与较简单checkpoint，而不以更多切片默认获得免费并行。

<!-- source-family:SF-2025-ARXIV-2509-21275 -->

### 完整新增

当网络混合dense、MoE与MTP模块时，stage balance也不能只数Transformer层：MTP中的transformer计算与vocabulary loss可能有不同成本，可拆成独立调度单位，让不同VPP stage分配不同数量甚至零个普通层，并只重算较合算的MTP部分。这样改的是同步1F1B内部的partition和activation lifetime，不是去掉参数版本边界。[Ling 2.0的受限报告](https://arxiv.org/html/2510.22115v1#S5.SS2)支持这一异构分区，但单MoE stage对routing imbalance更敏感，增加VPP也未必有净收益。应从真实forward/backward、loss与通信profile共同选择分区，并校验同一步loss/梯度、低精度scale和重算状态；FP8减的是具体张量/缓存成本，不能把active参数少直接当吞吐快。Profile、调度粒度、驻留、通信与收敛回归均付费；不均衡、显存或净吞吐失配时，保留较粗且已验的1F1B分区与完整重算，不把局部40%提升外推成任意模型/硬件的保证。
<!-- source-family:SF-2025-ARXIV-2510-22115 -->

### 实际后肩

### Split-Backward 与低精度状态：Schedule 之外还有执行合同

普通 1F1B 将一个 micro-batch 的 backward 视为相对完整、按栈回收的动作；在 eager 执行下，这让 activation lifetime 与依赖次序较容易追踪。若为了填补空隙，把反向拆成尽早传播的输入梯度 `dI` 和可延后的权重梯度 `dW`，再以捕获图复用固定地址，逻辑 micro-batch 与物理 buffer 就不再天然一一对应。低精度训练还持有 `amax` 历史、scale、量化权重缓存等不在显式 tensor 边上的可变状态；单一顺序 token 无法证明所保留任务的身份与版本，可能错绑或过早释放 tape、错序或重复更新 scaling state，或在 optimizer 提交后消费旧缓存。

因此这类 runtime 需要把四个合同分开：低精度 scale 更新的顺序；保留任务的逻辑身份与可重用物理槽的世代；参数提交版本与量化缓存版本；调用 stream 进入和离开捕获图的双向完成边界。`dI` 留下 `dW` 任务时，tape 仍归该 micro-batch 的逻辑身份所有，直到两类 consumer 均完成才可释放；optimizer commit 后旧权重缓存不能借相同地址冒充新版本。Checkpoint 保存持久数值状态，并在安静的更新边界重建进程内 graph、event 与槽位，而不是序列化旧地址。这样把吞吐优化从隐含栈次序变成可验证的状态转移，代价是世代检查、预留 buffer、额外显存和捕获 setup；静态 scale、即时 `dW` 或开销并非 launch 主导的 workload，仍可用更简单的 eager/full-backward 路径。

一项 exact-v1 实验在单节点 H800 PCIe / RTX 5880 Ada、短序列 `seq=256`、`microbatch=1` 的细粒度场景演示这种组合合同，并报告额外峰值显存与 setup 成本。其完整 step 收益混合了 split/full-backward、捕获与 gradient placement 等变化；只有局部消融能隔离其中一项，不能外推成“CUDA Graph 单项普遍加速”或长序列、多节点的训练结论。论文描述了实现和附属报告，但本次未核实可访问的代码 artifact，亦未独立复现。

上述 split-backward 仍可保持同步 optimizer step；下一节讨论跨更新边界的异步参数版本问题。

### 本人注及自读理由

- `SF-2025-ARXIV-2510-22115`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。新差额为MTP Transformer/loss独立partition与选择性recompute，区别普通异构fill模型和split dI/dW状态；保routing不均衡反侧，不复制整体Ling配方。

新差额为MTP Transformer/loss独立partition与选择性recompute，区别普通异构fill模型和split dI/dW状态；保routing不均衡反侧，不复制整体Ling配方。

### 本人注实际末段邻接

- `SF-2025-ARXIV-2507-00217` — Boyle，Daily2025-07-03补Jul2；[exact-v1](https://arxiv.org/html/2507.00217v1)§2–8、AppB/D.1/F必要，2+2+2=6/具体owner差额深入。只采用链路资源/到达依赖与实际收发编排分层；保同质GH200注入、64次取min、profile/控制握手假设、batch/activation/recompute和完整成本，不授真实WAN/SLO、所有表最优或端到端收敛。USENIX同题四作者只出版角色，未核全部图像/实现/复现；root§38已实际必要Source/6分/具体gap/逐字PRE通过并授本窄位；Boyle已按批准稿实际保存并完整self-read，root§40已实际完整新增/完整直接两侧/本人注及限定diff-check非writer POST通过，本指定窄位生效释放；仅同步既成事实，不授DAY。

- `SF-2025-ARXIV-2509-10371` — Carson，Daily2025-09-16补Sep15BJT；root首次必要准备，本人REPAIR31实际一次非准备者采用exact-v1 §3–8与A.2/A.5/A.6及直接图注，2+1+2=5。只采用同SKU热态×PP切层粒度及温差/效率相反结果，保TP4/每node两stage/DP关闭、联合改变/统计未披与完整费用；8K/800G仅projection、寿命与inference SLO未证。只核Zenodo元数据角色，未核/执行归档code/trace或复现；Zeno45原三项PRE通过，root本轮fresh授本精确位，作者已真实保存；Zeno55唯一完整nonwriter actualPOST通过，I6生效/位释放，未DAY。


## 22255 · books/part-04-training-system/33-grpo.md

唯一段首：`没有参考答案或可用 verifier 时`

### 实际前肩

这里的 reward 还随当前参数 θ 变化：完整期望目标的梯度既含 CoT 采样的 score-function 项，也含 reward 对 θ 的直接导数；后者在 log-likelihood 分支连接到参考答案的监督梯度。把 reward detach 后只作 policy-gradient 更新，会省略直接导数、改变梯度估计，不能静默称作完整期望目标的等价实现；用于减方差的 baseline 也须与当前 sampled CoT 独立。二项梯度分解并非这项实验首创，新增证据限于几种 reward/advantage 在作者两个 3B 模型、四个数据集上的取舍：greedy 与 sampled 的排序可能不同，长答案设置的 CoT 可收缩到接近普通 SFT；长度约束、KL 或 warm-start 维持更多 CoT，也不保证回答更好。reward 代理失配、参考不足或反向路径难以核实时，应回到可验证 outcome 或明确的普通 SFT，并分别验收输出质量、推理长度与总计算。

有可信参考和outcome时，也可把CoT前后的参考答案似然差作为附加sequence reward，而非替代最终正误：分别在生成CoT和另一个直接回答模板下teacher-force同一gold答案，取平均token logprob差，经有界非线性变换后与任务奖励相加。[DRER的受限分支](https://arxiv.org/html/2509.06024v1)另在组相对advantage算完后，用上一轮validation中各难度桶成功且格式合格响应的长度分位带，衰减带外response的signedadvantage；奖励条件与旧validation人口是两份状态。正衰减不翻符号，也会减弱负advantage的惩罚，不能统称为更重长度penalty；两模板不只是删CoT，likelihood差不认证中间步骤正确、必要或faithful，sequence分数展开也不产生独立token信用。已答对的CoT仍可有负差额，联合训练/不同采样统计不证明该代理的单独因果或净降本；停止梯度、gold对齐、空桶和样本不足未闭时，不应补成统一recipe。两路forced forward、全部rollout、validation与分位统计、训练调参及独立质量回归均付费；代理、长度支持或任务质量失配时，保可靠outcome、普通GRPO/DAPO与完整trace，不由自评分更高或输出更短签发推理正确与部署效率。
<!-- source-family:SF-2025-ARXIV-2509-06024 -->

### 完整新增

参考答案似然还可沿每个reasoning step读出，而不只比较整条CoT前后：在训练可见的gold上，分别teacher-force加入本步前后的答案，取logprob增量，或统计增量为正的比例，再与终局可验证reward共同训练。[PACR的受限分支](https://arxiv.org/html/2510.22255v1#S5)把这份自评分当dense shaping；answer-conditioned理想policy下的KL非负只在一致概率模型中描述期望，不证明给定正确答案就能生成faithful步骤，更不能倒推一次正增量是真实过程credit。逐步forced forward、gold制备、归一化与完整rollout都付费，少训练steps不直接等少墙钟；min–max全相等、不同轨迹长度与当前参数依赖也要明确定义。应另验最终答案、可见过程错误与原能力，不让更自信替代独立oracle；proxy、数值接口或质量失配时，保可靠outcome、较弱shaping与普通GRPO，不从局部数学任务提升签发所有步骤正确或policy-invariant保证。
<!-- source-family:SF-2025-ARXIV-2510-22255 -->

### 实际后肩

没有参考答案或可用 verifier 时，还可把同题 rollout 的末 token hidden state 归一化，用迭代 Gaussian 重权估计组内中心，再以到中心的负距离和组内 min–max 缩放构造 reward。[Latent-GRPO 的受限分支](https://arxiv.org/html/2601.08427v1)改变的是 reward 来源，不是为答案提供新的真值：表示一致性可能反映共同格式、风格或系统性同错，中心也不能自动叫作正确推理方向。min–max 尺度不是校准后的正确概率，更不保证梯度安全；末 token 选择、组大小、中心估计与 policy revision 都应随训练信号保存。<!-- source-family:SF-2026-ARXIV-2601-08427 -->

这条路径省去外部 judge 调用，却仍支付 hidden-state 存取和中心迭代成本。作者小模型数学实验有低于初始模型的反侧；API judge 的 2 QPS 是主动限流条件，不能把其耗时差写成普遍的两倍训练提速。采用前应独立验证正确性、同错簇和格式变化，并分账 rollout、代理计算与最终质量；一致性失配、组内信号退化或可靠 outcome verifier 可用时，保留普通 outcome GRPO，而不是用更紧的 latent cluster 替代答案检查。

### 本人注及自读理由

- `SF-2025-ARXIV-2510-22255`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。承接已有sequence gold-likelihood/DRER，新增逐步增量及oracle期望≠过程真值；不照录零分母未闭recipe，不授免费reward或通用faithfulness。

承接已有sequence gold-likelihood/DRER，新增逐步增量及oracle期望≠过程真值；不照录零分母未闭recipe，不授免费reward或通用faithfulness。

### 本人注实际末段邻接

- `SF-2026-ARXIV-2606-18216` — Daily2026-06-18补Jun17；exactv1，本作者§80必要3/4.1/4.3–6/Limitations/C/D3/F6–7、sole§134key。仅teacher-in-prompt/plain-only毕业/group及额外人口，原6不变；F6 benchmarkbootstrap非training repeats，F7三dump非穷尽shortcut/压缩标签证明，C6 ε项不照录精确倍率。64H10080GB/8node及wall反侧/估算FLOPs非profiling/全费保留；未核code/全workedimages/复现，待sole一次PRE/actualPOST。

- `SF-2025-ARXIV-2510-21583`：Daily2025-10-28补Oct27；exact-v1 Chunk-GRPO而非current改名，2+2+2=6，R20通过。仅chunk ratio/clipping与terminal credit分责，保weighted sampling反侧/全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。


## 22371 · books/part-06-ai-infrastructure/66-evaluation-system.md

唯一段首：`算法题的难度还应把结构边界与熟悉措辞分开`

### 实际前肩

任务难度切片也不能只按输入长度或实体数划分。关系推理可以分别改变输入规模、任务生成器规定的 binding arity，以及识别或比较单个 operand 的难度；它们是三个不同轴。同一 arity 下更多输入可能提供额外线索，而非必然更难；实体少却需要同时满足更多关系，也可能比长输入更困难。EvalSpec 应保存生成规则和 oracle，在输出格式、scorer、推理预算可比的切片中交叉改变这些轴，不把换任务后不同的 accuracy、substructure 或 recall 拼成同一条下降曲线。<!-- source-family:SF-2026-ARXIV-2604-12176 -->

这种控制比单一长度排行榜增加生成、oracle 与样本预算，也仍只能约束已测混杂。生成器定义的 relational complexity 是任务属性标签，不是模型内部容量的计算下界；合成、多选与有限 token 预算下的失败，更不证明增加任意计算都无效。简单任务、长度已主导成本时仍可保留原长度切片，复杂关系任务再补上述交叉维度。受限关系评估支持将这些难度来源分账，而不支持通用 arity 阈值或唯一失败因果。

### 完整新增

图搜索还需把输出路径长度与选择下一分支所需的lookahead分开：一条没有岔路的长链可以每次只看一步，而短路径中的分支结构可能要求多次BFS展开才能区分。EvalSpec可交叉改变branching、lookahead和path length，并分别固定“返回完整路径”“只选下一步”和判断题的输出合同。[受限DeepRD对照](https://arxiv.org/html/2510.22371v1)显示只按路径长短会误述难度，却不把生成器定义的BFS迭代当模型实际执行算法或计算下界；较大图同时改变输入/记忆压力，有限失败也不证明任意推理预算均无用。生成、可信search oracle、全部输出与预算扫描均计费，输出截断、人口和模型snapshot须分账；难度因素未解耦或oracle不可靠时，保原简单图切片与可执行搜索验证，不由一条accuracy下降曲线批准普遍搜索无能或真正算法理解。
<!-- source-family:SF-2025-ARXIV-2510-22371 -->

### 实际后肩

算法题的难度还应把结构边界与熟悉措辞分开：先在同一问题设置构造仅差关键结构条件的 P 与 NP-complete twin，再在各自答案、输入合同和 class 不变的约束下改写表述。可执行例子与有限测试不能独自证明所有自然语言改写保义，须保原题、solver/validator、改写 lineage 与独立人审；同 lineage 的多轮结果也不是独立样本。受限 hardening 流程同时压低两侧成绩，但改写长度与实例攻击仍可能混杂，失败又常是错程序或崩溃，而非只差运行时间；延长程序 wall-clock 不等增加模型思考预算，更不证明计算复杂度下界。构造、攻击搜索、程序执行和语义复核全计费；保义、class 或 oracle 不稳时回原题与可信测试，不由一个 class gap 签发真正算法理解或任意算力都无效。 [受限机制与证据](https://arxiv.org/html/2610.30103v1)。<!-- source-family:SF-2026-ARXIV-2610-30103 -->

内部轨迹的几何读数也要先控制生成过程的长度：在同一层沿 token 时间取 hidden states，路径、转角或 directness 都可能随输出 token 数、采样间隔、切段和截断规则改变，而不只是随任务难度或推理训练改变。一条[受限长度校正审计](https://arxiv.org/html/2605.15454v1)按 model/layer/domain 拟合长度项后比较残差，并用不同校正规则复核；它改变测量协议，不把残差变成无混杂的推理指纹。Directness 在不同校正下可改变排序，curvature 也仍有残余长度关联，code、SAT 与 MATH 的关系并不统一；模型训练 recipe 和共享 baseline 的差异更不容直接归因 RL 的内部作用。应共同冻结题目、层/token采样、reasoning边界、过短/截断人口、校准模型与独立行为评分，报告原读数、替代校正和敏感性。全部生成、hidden 抽取/存储、难度校准与重复验证都计费；关联不稳或协议身份不齐时，保留原任务行为分数和简单长度分层，不用一张更直或更弯的轨迹图签发因果解释、正确性或通用能力。<!-- source-family:SF-2026-ARXIV-2605-15454 -->

### 本人注及自读理由

- `SF-2025-ARXIV-2510-22371`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。按R36真实gap，仅lookahead-v-path长度及输出合同，接三轴难度前后，不引入额外Methods/未读普遍复杂度证明。

按R36真实gap，仅lookahead-v-path长度及输出合同，接三轴难度前后，不引入额外Methods/未读普遍复杂度证明。

### 本人注实际末段邻接

- `SF-2025-ARXIV-2510-21538`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+1+2=5。仅proxy sensor/target-state权限、弱span标签和聚合分母，保copyinghead未复现/投影全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。

- `SF-2025-ARXIV-2510-21258`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6。仅全logprob recurrence读出与校准资格，保O(N²)/词表算量、FP32距离及SEP有限case；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。


## 22422 · books/part-07-agent/82-multi-agent.md

唯一段首：`讨论输出的变化还可以先用可证伪的动力学基线诊断`

### 实际前肩

当自报概率直接成为下一轮状态时，还须检查同一事实的互补表述是否产生兼容更新：把命题换为穷尽互斥的另一面，同时将自己的概率与按原次序保存的peer概率取补，事实证据本身不改。只有整个请求和执行规则一起对应，局部更新的互补等变才足以保持配对轨迹；同一seed整数不自动构成随机更新的兼容耦合，后续分歧也不全是一次局部误差。[受限概率反馈对照](https://arxiv.org/html/2610.32874v1#Sx3)据此把同义改写、互补一致、同伴吸引与事实误差分验；平均报告一致不等每次draw一致，先平均再取绝对误差也会改变测量量。这里观察的是输出与外部状态，不是读取内部信念或人类行为。

一条修复分支保存同一请求两种取向的报告q0、q1，取R=(q0+1−q1)/2，并从同一pair派生R与1−R。它在构造上保证互补，固定pair和互补标签下不增加两取向平均Brier，却可能损害原来较好的单一取向；修复结果成为新状态后，未来请求已改变，一次投影的代数保证不延伸为整条反馈更准确。有限闭环对照保留这一反侧，不把零轨迹分歧当独立验证。配对调用、状态同步、概率解析与独立事实检验均付费；命题不真互补、配对或净效用不稳时保留原输出与外部verifier，不靠平均或强制一致认证真值。
<!-- source-family:SF-2026-ARXIV-2610-32874 -->

### 完整新增

群体大小还会改变有限尺度动力学，不能只把更多成员理解成更多独立投票。对二选词、同质policy与有限memory，可先枚举记忆状态下的响应概率，再用随机成对交互模拟不同population，比较有限时间的basin、混合稳态与mean-field极限。[受限naming-game分析](https://arxiv.org/html/2510.22422v1)的万级成员主要来自policy表上的随机模拟，不是万模型完整多轮实跑；N趋无穷的近似也不把有限样本偶然共识变成严格确定性，未共识和混合稳态反侧仍须保留。记忆长度、交互规则、初始人口与policy revision应一起冻结，表制备、模拟和真实调用校验都付费。它只提供人数/初态敏感性的诊断轴，不把词选择等同实际伤害、串谋或安全保证；表或动力学不能转移时，保较小独立候选、真实反馈与外部verifier，不由人数大或拟合稳态批准协作增益。
<!-- source-family:SF-2025-ARXIV-2510-22422 -->

### 实际后肩

讨论输出的变化还可以先用可证伪的动力学基线诊断，而不直接给改答命名为潜在信念改变：权重非负且和为一的邻居/初值混合不能走出初始意见的凸包，越界便说明这类固定混合解释不足。再给模型加入可拟合的持续驱动项，也应比较同一增量目标上的受限基线，并以未参与拟合的run预测选模，不能由更多参数带来的训练内高拟合批准机制。[受限hidden-anchor对照](https://arxiv.org/html/2606.19494v1#S5)只有一个模型取得明确的held-out平均优势，另外两者无优势或反退；十题、三成员、五轮且经top5重归一的自报概率，不是读取内部表示，更不证明越界或更动态便更正确。小驱动系数会使anchor恢复病态，投影、阈值和样本人口也改变解释；原概率/理由、解析与通信版本、拟合/验证划分及全部调用成本应保留。预测不转移或不确定性过大时，保较简单混合基线、独立候选与外部事实验收，不把潜变量拟合授作信任、权限或协作增益。<!-- source-family:SF-2026-ARXIV-2606-19494 -->

同伴意见已经可能放大共同错误时，一条额外分支不是让模型更强硬，而是把发言者的可检验表现与本轮说服力分开。外部系统持有已知答案的校准题，先取得各 Agent 在看见 peer 前的独立回答，再把校准所得信任值作为 speaker 属性随消息交给 receiver，指导下一轮按信任而非简单人数权衡。校准后冻结减少更新状态，却允许先在校准期答对、后来改变行为者利用旧信誉；随机选择后续校准题更新提供了另一条适应路径，但继续消费正确答案、额外调用与状态维护。信任标记只参与意见形成，不让 sender 取得任务事实、工具权限或最终验收权。<!-- source-family:SF-2026-ARXIV-2603-15809 -->

### 本人注及自读理由

- `SF-2025-ARXIV-2510-22422`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。按R36新差额，从有限policy表到population/meanfield关系；与后邻持续驱动项拟合不同，保模拟/实跑权限与反侧，不授大群体必失配。

按R36新差额，从有限policy表到population/meanfield关系；与后邻持续驱动项拟合不同，保模拟/实跑权限与反侧，不授大群体必失配。

### 本人注实际末段邻接

- SF-2025-ARXIV-2510-16572 — Socrates，Daily2025-10-22补Oct21；Tesla R26 exact-v1 §3–8必要/R52差额复用；counterfactual sensitivity消息与aggregation/consensus/transport分责深入。保text非真gradient、同步合作非恶意、A2A应用baseline非协议缺陷、LLM/等待全费与有限配置反侧；未核实现/复现。完整PRE/SAVE/全自读/solePOST按同日实际层。

- `SF-2025-ARXIV-2510-21557`：Daily2025-10-28补Oct27；exact-v1必要层、2+2+2=6，R20通过。仅冲突定点审计/一致区盲点/前置全费，非truth锚点或独立性保证；未核实现/复现，PRE/SAVE/全自读/solePOST据本日实际层。


## 22775 · books/part-06-ai-infrastructure/66-evaluation-system.md

唯一段首：`局部代码 confidence 还可以有另一种 label event`

### 实际前肩

有些selective gate不需要训练新置信度模型，而先改变可观测的证据协议。对冻结VLM的word-level OCR，一条受限分支在同prompt与确定decoding下查询原crop及轻微几何变换视图，先按预定normalization与几何长度上界排除明显退化，再只在足够valid views、唯一众数、vote比例与归一edit-distance dispersion共同合格时输出；视图数、transform分布与阈值一起冻结。几何上界不是真实字数，跨视图同意也可能稳定地错，不能给consensus授真值或把vote当正确率。[必要对照](https://arxiv.org/html/2603.19790v1)同时报告原全集风险、已输出子集风险和coverage，并与近似匹配coverage的single-view token-confidence gate比较；筛选人口不同不代表底座被修复，严格阈值或更多views也未使所有tail指标持续改善。多次forward、视图构造、screen/距离计算、校准与拒答转人工均付费；word-level之外、变换损字、稳定误识或预算不足时，保留单次识别、独立文字标签/区域证据及人工核验，不由经验frontier签发统计或生产安全保证。<!-- source-family:SF-2026-ARXIV-2603-19790 -->

当 strong verifier 昂贵而 cheap score 足以筛出部分样本时，可以用上下两个阈值把候选分为拒绝、送强验证和接受三个区，而不让两端彻底失去反馈：接受区和拒绝区仍以已知非零概率随机调用 strong verifier，观测到其标签后用 inverse-propensity 加权更新阈值；否则保持阈值。这样省的是 strong 调用频率，不是让 cheap score 自证 truth。[弱／强验证研究](https://arxiv.org/html/2602.17633v1)的有限时域结果要求固定 horizon、步长、正的 audit 概率下界及两阈值投影，以 strong-negative 与 strong-positive 各自累计数量为错受、错拒分母；不是 accepted-population selective risk，更不是任意停止或所有时刻同时成立的证书。小 audit 概率会放大估计波动和界的余项，空类约定不证明部署中该类无风险；MATH 的 GPT-4o 对照标签与 Sudoku 的确定性规则也不是同一 truth oracle。受测 weak/strong 组合与任务上的调用节省不能替代 wall-clock/GPU 成本：生成、cheap 检查和随机 strong 审核都需预算，硬件、precision、并发与 tail SLO 未披露。强标签失配、支持不足或必须逐项验证时，回退 strong-only、独立执行判据或 abstain，保留前述 oracle 分工。<!-- source-family:SF-2026-ARXIV-2602-17633 -->

### 完整新增

弱verifier也可以读取同题多个patch的相互关系，而不只单独评分一个候选：把group成员一起交给reward model，学习辨识哪些patch曾在声明环境中通过执行测试，再把这一判别器用于后续不运行tests的rollout奖励。[受限group-conditioned验证](https://arxiv.org/html/2510.22775v1#S3)改变的是运行期评分接口，训练标签仍来自执行；group大小、成员顺序、空patch padding、来源与测试环境都属于scorer身份。候选互见可以提供对照，也会让分数依赖同伴质量和多样性，固定reward model还会随policy漂移失配；可解析、syntax-check通过与真实修复正确不能互代。离线验证、group采样、模型训练与独立release tests均付费，免一次在线执行不等全流程无oracle或无成本。group支持、语义或校准不足时，保原执行测试、独立审查和Unknown，不由组内可辨认或训练reward稳定签发代码正确性。
<!-- source-family:SF-2025-ARXIV-2510-22775 -->

### 实际后肩

局部代码 confidence 还可以有另一种 label event：不是“整段程序正确”，而是“在满足同一 intent tests 的修复中，这个任意 token/line 集合是否保留”。用最小修复近似该事件，再让辅助模型汇总集合内的表示，可以查询不同长度、位置或非连续 span；这把固定 token 分类扩展为 arbitrary-span 风险测量，却没有找到唯一 bug。测试不完备、多个同样有效的修复及最小 patch 的选择都会改变标签；只有能生成并通过修复的样本进入人口时，校准对象还受 patchability 筛选约束，不能把“被保留概率”当成程序语义正确概率。

这种测量需要分别交付修复合同、span 标签与目标域 calibration 数据。即使 probe 在其他 dataset 上训练，若 Platt scaling 仍使用目标 dataset 的标签，就不是 zero-shot 校准；低 ECE 与几乎没有相对基率预测收益也可能共存，必须同时检查校准与定位区分能力。已有研究没有干净 held-out calibration/hyperparameter 控制，且多副本信号另付生成成本，故只支持受限代码修复人口中的诊断，不授任意 span 的安全证书。修复不可得、支持集漂移或高风险代码不能接受局部事件时，回到完整执行、独立语义审查或 abstain，不让 repair oracle 同时认证自己定义的 correctness。<!-- source-family:SF-2026-ARXIV-2512-24560 -->

### 本人注及自读理由

- `SF-2025-ARXIV-2510-22775`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。按R37实际gap，新增group互见+离线execution标签移交online reward；不让免线上执行偷换无测试/最终正确。

按R37实际gap，新增group互见+离线execution标签移交online reward；不让免线上执行偷换无测试/最终正确。

### 本人注实际末段邻接

- `SF-2025-ARXIV-2510-21538`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+1+2=5。仅proxy sensor/target-state权限、弱span标签和聚合分母，保copyinghead未复现/投影全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。

- `SF-2025-ARXIV-2510-21258`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6。仅全logprob recurrence读出与校准资格，保O(N²)/词表算量、FP32距离及SEP有限case；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。


## 22922 · books/part-06-ai-infrastructure/66-evaluation-system.md

唯一段首：`Policy/Safety的一次binary verdict还不能认证诊断粒度`

### 实际前肩

```text
delivered_success
= runtime_success
  AND contract_success
  AND quality_success
  AND policy_success
  AND outcome_success
```

某些任务无法为每个请求即时获得 ground truth，因此不能简单把语义错误重新编码成另一个实时 `error_rate`。平台通常组合离线标注集、规则与 deterministic checks、抽样 human review、judge、用户反馈和延迟到达的业务 outcome，并为不同证据保留 provenance 与不确定性。高风险 policy failure 还应作为 hard gate，而不是被大量正常请求在平均值中抵消。

### 完整新增

抽样human review也不是固定不变的oracle，呈现界面本身会改变人能发现哪些错误。可把同一推理改为可交互的结构化表示，再与静态CoT比较error detection，同时冻结受审错误类型、正确/错误比例与每人题量；转换后的语义保持须另核，界面更容易检查不认证原模型内部推理忠实。[受限随机界面对照](https://arxiv.org/html/2510.22922v1#S3)支持部分交互界面优于静态展示，但三种交互之间与时间差未显著，不授唯一最佳形式或普遍节时；每人九错一对的人口也不能搬成正常部署检错率。解释生成/转换、人工阅读、点击与返工都计费，judge和human各自的错误仍要估计。转换、人口或预算不合时，保原轨迹、可信参考与独立人工复核，不以更可读的说明取代运行证据或安全gate。
<!-- source-family:SF-2025-ARXIV-2510-22922 -->

### 实际后肩

Policy/Safety的一次binary verdict还不能认证诊断粒度：指出trajectory不安全、定位风险来源、分类failure mode与说明可能伤害，是不同标签和决策对象。Binary分数较高时，细粒度诊断仍可能很弱；应保存taxonomy、trajectory/tool人口、每轴标签来源和人工/模型judge分工，不把多项描述压成统一可信解释。[受限 SAFER对照](https://arxiv.org/html/2601.18491v1)的合成平衡人口与工具隔离支持这项测量差额，最佳failure-mode分数仍低，额外诊断监督也非等预算因果。标签与多轴审核计费，likelihood扰动代理不认证内部因果，诊断错误或标签资格不足时回binary拒绝/升级、原轨迹与独立人工审查；只有外部policy owner能决定是否放行，细致解释不代安全gate。<!-- source-family:SF-2026-ARXIV-2601-18491 -->

第 67 章可以持续观察 transport/runtime errors 和已产出的质量信号趋势；本章负责定义 semantic success 的口径、样本与决策边界。两者共享 request、model、prompt、retriever、tool 与 environment identity，但不能用可观测性代替规范性判断。

### 本人注及自读理由

- `SF-2025-ARXIV-2510-22922`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。按R37新差额人审interface改变测量能力，保错误人口/语义转换/无显著时间差，接human evidence后而非新列产品界面。

按R37新差额人审interface改变测量能力，保错误人口/语义转换/无显著时间差，接human evidence后而非新列产品界面。

### 本人注实际末段邻接

- `SF-2025-ARXIV-2510-21538`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+1+2=5。仅proxy sensor/target-state权限、弱span标签和聚合分母，保copyinghead未复现/投影全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。

- `SF-2025-ARXIV-2510-21258`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6。仅全logprob recurrence读出与校准资格，保O(N²)/词表算量、FP32距离及SEP有限case；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。


## 22931 · books/part-06-ai-infrastructure/66-evaluation-system.md

唯一段首：`校准还可以把每个候选label的重新训练换成同一in-context打分器`

### 实际前肩

[Calibration state](https://arxiv.org/html/2610.28937v1)的失效触发还包括推理配置改变，而不只checkpoint更新。若quantization或token-logit temperature改变了同一任务的nonconformity score分布，固定数据分布和训练权重也不能让旧threshold继承matched coverage；变化可能导致欠覆盖，也可能过覆盖，不由某个bitwidth推单调风险。应把实际score计算、quantization/backend与temperature纳入producer身份，分别声明已知固定配置、稳定mixture或未知但有限配置集的目标。Pooled校准只保证其混合人口；对每个已列配置分别校准再取最大threshold可保守保护，代价是较大的prediction set，latent配置推断还另付错误预算与校准费用。有限label小模型实验不授开放生成真值或任意未见配置可靠性；配置、支持或exchangeability无法核实时，保固定已校pipeline、重新matched校准或停止coverage声明，不以accuracy未降批准旧calibration。<!-- source-family:SF-2026-ARXIV-2610-28937 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2604-23987:start -->
模型更新与 calibration 更新属于同一个 release transaction，但 accuracy evidence 与 coverage evidence 保持独立。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-23987:end -->

### 完整新增

若变化来自已定义domain的混合比例，而非任意域内分布漂移，可先估计目标mixture，再按域权重重采或重权校准分数；域分类器有混淆时，还需可辨识、稳定且可逆的confusion matrix来校正比例。[受限mixture校准分支](https://arxiv.org/html/2510.22931v1#S4)仍要求域内iid与目标支持，聚类通常可分不能替代这些条件，也不恢复任意OOD的exchangeability。有限生成候选中的answer-set coverage、拒答比例与单query正确率是不同对象，采样未见真答案也可能只是预算不足。域模型、mixture估计、每次模型更新后的重新采样/校准和完整生成均付费；矩阵病态、未知域或人口不稳时，保matched校准、保守集合与Unknown/拒答，不把较小集合或低语义熵签成无条件有限样本安全界。
<!-- source-family:SF-2025-ARXIV-2510-22931 -->

### 实际后肩

校准还可以把每个候选label的重新训练换成同一in-context打分器：把候选label加入context，让context彼此可见、每个query只读context和自身，再把同一打分规则的nonconformity交给精确quantile构造预测集合。这里省的是per-test参数适配，不是候选label枚举或完整前向；score producer的对称接口、固定meta参数与数据exchangeability仍须独立成立，普通causal prompt或带破坏置换身份的位置编码不能继承该覆盖论证。[受限FCP分支](https://arxiv.org/html/2509.01840v1)另提训练集合大小的平滑目标，但所写sigmoid与其indicator方向冲突，这里不照用该loss recipe或宣最小集合。QPSK/二类图像的平均coverage与校准期时延不认证逐样本真值、OOD可靠性或大词表免费推理；辅助任务训练、每label复制、全部token打分与quantile均付费。对称性、支持人口或总预算无法核实时，保留已验收split/full conformal校准和原scorer，并停止不合资格的coverage声明，不由一份较小预测集替release gate。

<!-- source-family:SF-2025-ARXIV-2509-01840 -->

### 本人注及自读理由

- `SF-2025-ARXIV-2510-22931`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。按R37实际gap，domain mixture/confusion correction与已有配置mixture不同；不照录符号不闭reject式，不授任意漂移coverage。

按R37实际gap，domain mixture/confusion correction与已有配置mixture不同；不照录符号不闭reject式，不授任意漂移coverage。

### 本人注实际末段邻接

- `SF-2025-ARXIV-2510-21538`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+1+2=5。仅proxy sensor/target-state权限、弱span标签和聚合分母，保copyinghead未复现/投影全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。

- `SF-2025-ARXIV-2510-21258`：Daily2025-10-28补Oct27；R12首次必要/R24实际gap，2+2+2=6。仅全logprob recurrence读出与校准资格，保O(N²)/词表算量、FP32距离及SEP有限case；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。



