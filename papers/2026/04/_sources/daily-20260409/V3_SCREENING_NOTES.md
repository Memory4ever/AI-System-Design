# 2026-04-09 V3 题摘校准记录

窗口：`2026-04-08T09:00:00+08:00` ～ `2026-04-09T09:00:00+08:00`。检查于2026-09-26；作者apr01。本文为进行中材料，不是已冻结分母、审阅完成或Books采用。

## 作者侧收口索引（2026-09-26）

最终非作者复核恢复06812，81=24Integrate/10Existing/39ReportOnly/8Disputed。root额外12题摘抽核及apr03公式反证复核的实际范围见日报§6；06812旧训练ownership排除无效，现按自适应粒度贡献必要深入后将主题加权公式/消融冲突争议隔离，不写Books。下方80和“待日验收”仅阶段记录，最终状态以当前README为准。

原87工作信号已逐家族处理：77进入作者侧候选，06182具体前分母关闭，六日期例外07345/06291/06436/06652/07026/07277、三个必要版本例外06425/06820/06779精确隔离。另从已有189完整题摘的反向复核恢复06491/07108/06281，候选80=24Integrate/10Existing/39ReportOnly/7Disputed。必要方法、评价和直接反证已按最低投入实际核，不将562宽列表转全文队列，也不将79/87差当剩余待读数量。日级最终独立验收仍由root；下方初批/第二批标题和待核词是历史筛选过程，具体终态以README及当前checkpoint为准。

## 实际阅读范围

库存入口：[原始身份与题摘](../arxiv-owner-replay-20260903/20260409/arxiv-owner-receipt.json) `identities[]`，562个去重身份，首06171、末07350。562标题用于轻量范围定位，不等于562摘要或全文；完整题摘已读189项，其中首两条06171/06172与以下187条。旧screening_status/reason不作为本轮准入或排除依据。题摘来自保存的原始库存，版本身份/撤回状态及拟采用命题仍须在官方exact-version页面核对；不能将后版摘要默认绑定v1。

```text
06176 06177 06182 06185 06188 06192 06195 06196 06201 06211 06222 06228 06233 06240 06241 06247
06250 06253 06256 06258 06260 06268 06277 06281 06284 06285 06291 06296 06297 06298 06330 06333
06356 06366 06367 06370 06374 06376 06377 06389 06393 06401 06409 06413 06422 06425 06427 06436
06452 06465 06483 06485 06491 06495 06501 06502 06515 06542 06543 06550 06613 06627 06628 06636
06637 06647 06652 06662 06664 06668 06693 06694 06695 06699 06710 06714 06723 06725 06729 06736
06742 06748 06750 06753 06755 06756 06757 06765 06767 06771 06774 06777 06779 06787 06794 06798
06811 06812 06819 06829 06831 06832 06834 06836 06840 06845 06870 06871 06912 06916 06939 06950
06954 06955 06956 06966 06970 06995 06996 07007 07012 07023 07026 07030 07035 07036 07039 07079
07084 07098 07102 07108 07121 07123 07144 07147 07165 07169 07172 07173 07190 07192 07201 07209
07220 07223 07236 07238 07242 07254 07266 07269 07274 07277 07279 07296 07306 07316 07321 07328
07331 07335 07340 07341 07343 07345 07350
06339 06391 06438 06529 06566 06607 06616 06633 06644 06734 06793 06820 06833 06861 06902 07069
07105 07146 07213 07230
```

## 首批准入校准（尚待日期与独立题摘复核）

这些条目说明为什么值得核验，不是仅因对应章节而保留；分数与确定候选只能在窗口归属及身份通过后写入报告。

| exact-v1身份 | 原约束 → 题摘给出的增量 → 待核设计判断 |
| --- | --- |
| [2604.06176](https://arxiv.org/abs/2604.06176v1) | 对话检索常把噪声视作不相关文本；题摘提出结构化噪声在Qwen embedding中形成hub，query instruction会改变排序；需核输入模板和噪声切片是否进入encoder/index发布合同，而非仅按总体检索分数验收。 |
| [2604.06188](https://arxiv.org/abs/2604.06188v1) | 同名API与消费端UI往往被当作同一能力接口；题摘比较端点及跨两月行为变化，聚合指标隐藏时间模式；需核endpoint/version/time条件是否改变可复现的评估对象。 |
| [2604.06228](https://arxiv.org/abs/2604.06228v1) | 频率缓存默认持续跟随经验访问；题摘给出stationary prior条件下阈值相关的cache损失界；需核哪些先验与误差前提允许另一缓存分支，不能把定理外推所有KV或语义cache。 |
| [2604.06240](https://arxiv.org/abs/2604.06240v1) | GUI Agent的结果验证容易把未达到目标与过程失效混合；题摘分离process/outcome并指出不可控失败和截图上下文；需核验证对象如何影响错误归因及后续动作，而不是多加一个judge。 |
| [2604.06241](https://arxiv.org/abs/2604.06241v1) | 安全检查若只看对话文本，初次打开不可信repo/artifact后已可能执行；题摘给出执行前capability/egress admission的具体路径；需核可执行对象和效果边界是否由模型外策略拥有。 |
| [2604.06247](https://arxiv.org/abs/2604.06247v1) | 生成式安全判定会支付输出时延；exact-v1题摘提出residual stream的layer-wise kNN与layer ensemble，而库存标题/last-token描述来自后版，已纠正；需核无需生成的检测分支能支持哪些攻击/分布，不能把检测分数叫安全证明。 |
| [2604.06268](https://arxiv.org/abs/2604.06268v1) | RL探索常以同一输入的输出entropy衡量；RAGEN-2题摘把输入依赖的互信息与该entropy区分；需核探索目标何时改善策略对不同环境状态的依赖，而不是只让回答更随机。 |
| [2604.06297](https://arxiv.org/abs/2604.06297v1) | PEFT降低可训练秩常被视为隐私上的天然缓冲；题摘利用梯度子空间/null-space及token-order alignment恢复文本；需核训练梯度接口及低秩结构是否引入独立泄漏边界。 |
| [2604.06409](https://arxiv.org/abs/2604.06409v1) | 删除或泛化敏感内容会损害任务效用；题摘研究自由文本pseudonymization及多轮隐私压力；需核替换状态、跨轮一致性与效用的条件关系，不等于一般匿名化成功。 |
| [2604.06422](https://arxiv.org/abs/2604.06422v1) | 模型能识别输入特征不代表会按自己的阈值规则决策；题摘通过阈值/颜色反事实拆开感知与行为；需核该干预是否使评价不再以描述正确代替约束遵守。 |
| [2604.06543](https://arxiv.org/abs/2604.06543v1) | 声明目标概率不等于实际采样遵守该分布；题摘比较直接生成、seed转换及实际分布；需核随机操作应何时交给可检验工具而非token选择。 |
| [2604.06613](https://arxiv.org/abs/2604.06613v1) | 强迫模型立即回答会混淆答案不可恢复与输出接口失配；题摘比较自由延续和强制提取，并给出串行/API开销；需核恢复能力指标和部署收益是否被同一测试测准。 |
| [2604.06647](https://arxiv.org/abs/2604.06647v1) | 静态RAG正确率不测用户纠错后的适应；题摘引入feedback后的修正滞后和语义结果；需核纠错状态真正生效的evaluation contract，而非仅提倡反馈。 |
| [2604.06668](https://arxiv.org/abs/2604.06668v1) | 存储性能模型可能把metadata与设备延迟混为一体；SwarmIO题摘显式模拟GPU高IOPS路径并用于vector search；需核模拟器拆分是否改变索引执行/设备选择，不采用headline IOPS作生产保证。 |
| [2604.06723](https://arxiv.org/abs/2604.06723v1) | 回答级全局校准可能不适合局部token编辑；题摘以局部decision的校准/拒绝控制比较全局方法；需核被校准对象与损失在何种编辑任务下必须变更。 |
| [2604.06834](https://arxiv.org/abs/2604.06834v1) | 平均log-prob常用于CoT样本排序；题摘指出首token概率和长度稀释的混杂；需核数据筛选是否错误地奖赏长输出，属于评价/训练反证而非新应用排名。 |
| [2604.06836](https://arxiv.org/abs/2604.06836v1) | optimizer统一精度简化状态管理；题摘联合layer/state/time动态bit选择与转换代价；需核精度预算是否可在训练阶段调度，而非只做一次低比特压缩。 |
| [2604.06840](https://arxiv.org/abs/2604.06840v1) | 只检查可见CoT可能遗漏回答阶段触发；题摘给出clean reasoning与后续恶意输出的分离；需核安全验证的执行范围，不能以解释无异常等同整个路径可信。 |
| [2604.06916](https://arxiv.org/abs/2604.06916v1) | Diffusion RL的低精度rollout直接训练会引入分布/数值耦合；题摘先用FP4池筛选、再BF16重新生成训练样本；需核哪些选择偏差仍在、哪些训练数值身份恢复，而不称等价原分布或默认AR LLM。 |
| [2604.06996](https://arxiv.org/abs/2604.06996v1) | 可验证的binary rubric和judge ensemble常被当作消除偏好的办法；题摘仍观察self-preference；需核评价器来源与可验证标准是否足以支撑独立结论。 |
| [2604.07023](https://arxiv.org/abs/2604.07023v1) | AR逐token解码与masked diffusion常各自训练；MARS题摘以masked slots继续训练既有AR并提供block/KV执行分支；需核改变状态和质量/吞吐控制的具体条件。 |
| [2604.07172](https://arxiv.org/abs/2604.07172v1) | 题摘主张单scalar temperature在所测条件优于复杂token-level方法并可同时改善calibration/discrimination；需核实际评价对象和适用范围，不能反写成token局部优于global或只改calibration。 |
| [2604.07173](https://arxiv.org/abs/2604.07173v1) | LoRA通常与base执行共驻服务端；题摘分离adapter执行并显式考虑通信、rank和SLO；需核adapter状态与共享base路径的分布式边界，不等于一般加节点扩容。 |
| [2604.07345](https://arxiv.org/abs/2604.07345v1) | GPU能耗或整机估算不代表facility能耗；题摘用H100工作负载观测连接bottom-up设施模型；需核测量粒度与估算不确定性，而不把推断当厂商披露。 |

## 可直接关闭的具体反例（题摘贡献筛选，不冒充日期已核）

| 身份 | 本轮关闭理由 |
| --- | --- |
| 2604.06171 | support ticket RCA知识库比较SFT/RAG/hybrid，用lexical/semantic相似度表明可用起点；未拆出改变训练、检索或RCA正确性合同的新机制，只有业务组合和指标。v1Updated后版污染亦不能据其归本窗；贡献排除不等于日期验证。 |
| 2604.06211 | 教学问答把隐含解释问题展开后检索；题摘未给查询分解相对既有链的新有效性条件或反证，不因教育QA效果入选。 |
| 2604.06222 | 几何拟合人类记忆的有效维度/遗忘；题摘没有研究大模型参数、Context或Memory机制，不能以类比替代项目关系。 |
| 2604.06401 | DSL加可信证明义务、checker组成代码验证链；题摘只应用已有形式化验证分工，没有新增可复用保证或适用前提。 |
| 2604.06729 | 物理反射侧信道研究不以基础模型或其运行时为攻击对象；安全主题本身不能恢复到本项目候选。 |
| 2604.06755 | 旧前分母关闭重开：虽然verifier-stop是成熟机制，题摘报告token降幅与实际能量降幅不同、GPU每token overhead增加，提供净能量不能从token收益推断的反证；须核必要measurement及Ch70再判，不因没有新机制关闭。 |
| 2604.06765 | 分工角色和三阶段multi-agent benchmark组合；题摘没有分离角色收益的条件或新的控制/失效机制，不能因workflow术语保留。 |
| 2604.06954 | 普通图像分类器压缩与对抗扰动；摘要未建立基础模型压缩的直接机制，不能凭可类比量化安全进入。 |
| 2604.06956 | 推荐系统embedding lookup通过冻结窗口、稀疏key聚类和staleness控制减少远端读取；其等价条件依赖该推荐训练的数据路径，题摘没有证明可迁到Transformer token表示/梯度状态，不以名称embedding直接映射LLM。 |
| 2604.07035 | 固定协议比较模型238项质量/latency/VRAM；提供更多工作点，没有改变已有资源—质量Pareto选择或测量边界的证据。 |
| 2604.07039 | PyBullet中模块化Agent/policy语言、技能封装与同类策略组合；题摘未分离出新权限、控制提交或可行性边界，不能把政策平面重述当增量。 |
| 2604.07169 | Bayesian filtering与flow状态递归是独立控制估计方法；未研究语言基础模型、训练/推理或learned world model，不因state词汇类比纳入。 |
| 2604.07190 | 下载/派生模型采用分析属于生态事实；不改变模型机制或Infra设计，因此不进入贡献分母。 |
| 2604.07274 | 临床QA在consumer GPU比较40种RAG配置；题摘只是领域工作点与已知检索组件比较，没有新有效性/正确性合同。 |
| 2604.07296 | OpenSpatial增加3D bbox与多任务数据覆盖；题摘未给改变表示/物理状态正确性的新机制或受控反证，数据规模与任务数本身不充分。 |
| 2604.07321 | LTL任务以语法/语义检查和prompt对照建benchmark；题摘重复既有functional correctness分账，未暴露新的基础模型评价盲区。 |
| 2604.07341 | 多Agent跨语言repo翻译与验证；摘要显示角色组合和任务改善，未给独立执行或validation contract增量，不直接采用框架名称。 |
| 2604.06339 | GAN/Diffusion/AR综述归纳，不解决当前某项机制分歧或提供新的综合证据。 |
| 2604.06391 | 生物医学图基础模型的结构prompt和message passing应用；AI for Science当前暂缓，未建立大模型/Infra基本机制贡献。 |
| 2604.06529 | 间歇网络的通用同步/上下文一致性oracle；不是模型或Agent持久状态实验，不从一般分布式类比入选。 |
| 2604.06607 | SystemVerilog coverage-driven迭代assertion生成；题摘应用现有coverage-feedback控制，没有新可迁移机制或验证边界。 |
| 2604.06633 | 多Agent SAST+RAG/ReAct漏洞检测；标题有安全，但摘要仅组合已有检查，未指明新攻击/信任接口或纠错信号。 |
| 2604.06861 | 结构化要求和迭代修复提升issue解决；摘要未改变已有requirement→plan→patch流程的条件或权责边界。 |
| 2604.07069 | 独立控制系统的SSM observer/LMI contraction，不是语言序列state-space架构；同名缩写不能建立项目范围。 |
| 2604.07105 | panorama/depth/Gaussian pipeline用于仿真背景，任务吞吐提升；不研究world-state转移/学习或VLA闭环机制。 |

## 官方撤回与轻量版本检查

### 第二批具体语义裁决（进行中，不是冻结候选）

在上述189完整题摘中，另61项具有需进一步核验的具体信号；它们不全部是深审或已证实贡献。准入仍须逐家族官方身份/日期、独立校准与最小必要证据；下列仅说明题摘哪条判断值得核验，不据新名字、参数量或owner存在直接保留：

| 身份 | 具体待核增量 |
| --- | --- |
| 06182 / 06185 | 真实GUI环境变化、跨轮implicit intent/转场分别给出固定任务成功率不能解释的反证；需区分受控干预与仅换一套较难任务。 |
| 06192 | prefix answer-information假设连接内部entropy与外部正确率，需核训练能否推出假设、条件entropy对象与可观测proxy。 |
| 06233 | 能识别rule缺陷与是否拒绝被拆成两个行为对象，不以拒绝率直接推道德reasoning能力；需核合成题目和judge的限定。 |
| 06256 / 06366 | 参数update主方向不等于representation局部feature；aligned/balanced线性网络SGD噪声的逐mode动力学另有条件；不从toy推所有模型。 |
| 06260 / 06330 | DLM逐denoising分支重采样与space/time稳定commit是两种不同执行分支；前者新law、后者阈值/缓存身份需核，不只采用倍数。 |
| 06284 | 生成Agent策略必须由真实syscall capability/egress边界执行，需核用户态kernel/BPF覆盖与policy证明范围。 |
| 06291 / 06515 / 06542 / 07030 | LoRA专家先通信再routing、router变化/rare-feature量化敏感性、跨层pruning预算以及balance scope专门影响expert specialization；各核具体控制与反例，不合成一条线性替代史。 |
| 06298 / 06628 | hard sample训练收益平台与reasoning SFT dip/recovery提供条件性反证，不能把GRPO重分配或SFT记忆标签当普遍因果解释。 |
| 06333 / 06413 | drifting归一化可使field非保守；直接flow-map监督在不一致coupling下mean collapse。两项改目标解释，需核定理假设/最小反证。 |
| 06356 / 06871 / 06694 | speech ICL内容与声学copy不同；浅层声学/深层语义冗余及audio KV连续性分别决定压缩边界，需核oracle不当deployment。 |
| 06370 | multi-LoRA KV分叉不能按相同base prompt exact共享；shared/residual cache及SRAM重建的条件改变状态身份。 |
| 06374 / 06427 | latent-CoT训练策略的superposition/collapse与发现更深算法vs执行已知算法的深度上限需分开，不从模型层数或长trace直接推能力。 |
| 06425 | 从像素/I-O trace学出的screen runtime与真实程序执行不同；原文明确reuse/update/symbolic stability失败，需核此负面边界。 |
| 06436 | prompt-wrapper安全不可能性依赖连续性/utility/Lipschitz等条件，必须核假设和离散模型适用范围，而非引用theorem标题。 |
| 06452 / 06485 | listener中途interrupt取得控制与代码候选等价类共识改变验证对象；分别核通信代价/错停与等价不等真值。 |
| 06483 | activation capture/steering跨rank的执行与trace内存路径影响可观测性，需核拆分缓冲与pipeline保证。 |
| 06495 / 06695 / 06767 | SAE feature absorption干预、early/deep token saliency与BF16 margin伪影分别挑战representation解释；需核控制后改变的对象。 |
| 06566 | evaluator与solution共同演化会改变证据独立性，需核heldout隔离及测试oracle而非只称AI-for-AI框架。 |
| 06616 | dynamic空间filter与ANN cell/graph连接改变过滤访问路径，需核增删、跨cell查询与有效性，不泛化模拟/局部数据。 |
| 06627 | 并行mask预测替代逐token prompt剪枝，需核层次shot/token监督、压缩预处理和答案质量联合成本。 |
| 06636 / 06777 / 07165 | solvability potential→层次advantage、视觉描述/observation alignment reward、功能相似步骤树合并/credit各是具体训练分支，需核reward身份/估计偏差/预算。 |
| 06652 | ODE velocity与Adam momentum软过渡对硬切换collapse的控制可提供优化机制，而非仅新的optimizer名字。 |
| 06664 | CUDA graph持久topology不等于可执行context；确定性地址、kernel binary与rank communication materialization可能补cold-start机制。 |
| 06714 / 06820 | 人可辨识hallucination与模型truth分开；judge直接问target response不一定最好预测人的target，需核真实人类评价与泛化。 |
| 06748 / 06756 / 07102 / 07123 / 07223 | visual ICL是否使用pair、fluent错误CoT、persona steering judge偏移、语言冲突选择、JSON competence与guard安全五种具体评价混杂/反证，分别核控制，不因都叫benchmark合并。 |
| 06755 | verifier early-stop token收益不等于net energy收益，重开原成熟机制关闭理由，核GPU每tokenoverhead与总measurement。 |
| 06779 | 多trajectory diffusion SMC offspring allocation改变估计方差/偏差，需核与Max选择区别及理论条件。 |
| 06811 | 多skill正常片段可经加密/组合变成恶意payload，需核组合信任接口和effect证据而非仅字符串检测。 |
| 06819 / 06832 | layer-sequential训练通过lookahead/cotune维持跨层耦合、ARVLM直接转diffusion与先LLM转换的matched路径是不同设计分支。 |
| 06912 / 06939 | query触发局部高分辨率与视频global anchor/local dynamics双KV、dual-reference RoPE/recache各改变状态预算与条件，不称长期无损。 |
| 06950 / 06966 | human-readable但model-unreadable视觉smuggling区分感知/推理；AR-diffusion GRPO的多trajectory不确定token策略区分logprob噪声/oversmooth。 |
| 06970 / 07144 | API黑盒调度需要哪层magnitude先验与在线生成policy代码谁获admission是具体控制边界，不能从本地模拟推厂商全局调度。 |
| 07026 | distribution/token importance与cross-attention spatial reweighting的实际训练增量待核；CMS可能倒填、需检查更早同家族正文，不凭Submitted/CMS任一单字段定owner。 |
| 07192 | compact header成本下降但compliance无显著增益、违反model default的constraint失效提供受控负面结果，不当格式万能。 |
| 07209 / 07277 | camera/global state与implicit world cache、single-state多action critic分别补world-state和环境sample-cost的具体分支，需核几何/真实转移与critic偏差。 |
| 06250 / 07213 | DISSECT的model-oracle输入干预是VLM感知→推理有效性问题，不因科学题目直接恢复AI-for-Science应用；implicit-manifold Brownian构造则需核它对生成sample路径的实际条件，不能MNIST图示代训练分布保证。 |

上述成对/组行只是压缩题摘理由，每个ID仍是独立家族，不合并计数。当前是首24+另63的工作信号范围（07345已日期隔离，尚未复核的贡献/日期亦可能改判），不是87篇确定贡献或全文已读。

### 明确的应用/成熟组合关闭（不因没有新owner关闭）

| 身份 | 完整题摘中的具体前分母关闭理由 |
| --- | --- |
| 06177 | domain facet/experience retrieval与preference规划组合改善EM/hops；没有分离改变检索正确性/控制权的新增条件，领域prior补齐本身不足。 |
| 06195 / 06196 | 支持缺口gate与refusal组合、逻辑否定映射projection分别复用已知复核/形式checker边界；所测complementarity与FOLIO工作点不形成新增保证。 |
| 06201 | 以comment比例/高频topic扩充阅读任务，但题摘未发现新的聚合机制或改变现有总体统计验证判断的反证，不能因benchmark对象不同直接保留。 |
| 06253 | LoRA/optimizer/Fourier regularization在MBPP跨编程语言获得工作点；题摘未明确可迁移的频域机制/隔离控制，几个有利pass@1数字不足以准入。 |
| 06258 | residue debugger对科学程序的数值监测改进有价值，但材料未建立与模型训练/推理kernel数值路径的直接研究关系；不以一般浮点类比恢复本项目。 |
| 06277 / 06285 / 06502 | external弱label→hidden probe、hyperbolic语义异常检测及CLIP长文本聚合安全分类器，题摘给新detector实现，但未揭示新的信任路径/保证或重要失效边界；不把安全名称本身当deep触发。 |
| 06281 | 重开旧关闭：不能因两层模型而排除。题摘明确给非全局有界loss下的SGM norm控制，独立test与依赖样本有不同rate；实际必要假设/公式已读，转标准理论候选工作项，不将其外推Transformer。 |
| 06296 / 06465 | UCB/arm elimination客户端模型组合与进化Pareto checkpoint merging应用已知搜索；成本/长度工作点本身未改变搜索有效性或merge兼容条件。 |
| 06367 | cookie/privacy UI task增加任务覆盖并观察stateful toggle失败；题摘没有新权限/执行接口或受控原因分解，不能安全场景直接入选。 |
| 06376 | 多hop视觉data生成/验证及cached工具replay是成熟data流程；题摘不支持新的replay有效性/工具状态身份条件，不以数据条数或tool步数增长入选。 |
| 06377 / 06393 | 能力向量跨model低秩对齐和浅层attention改local是局部实现；题摘未给改变现有steering/attention可行性判断的新解释/边界或明确受控反证，不能模型结果提高就保留。 |
| 06438 | 精确conjugate Bayesian shadow posterior retrain没有在题摘建立foundation模型训练/推理的新增条件；关闭不代表任何posterior方法均范围外。 |
| 06491 | 重开旧关闭：原文研究任意DFM velocity到一步transition policy的通用后训练机制，DNA只是评价任务，不能把后者偷换为贡献范围。实际§4必要公式已核，转候选工作项，不恢复AI-for-Science领域应用。 |
| 06501 | letter-string copy任务/异质data与attention steering重复已知中间任务辅助和组合泛化限制；题摘的新任务成功不构成对模型能力形成的独立新机制。 |
| 06550 / 06693 | skills安全triage/jury与JWT/Merkle授权日志组合成熟工具/信任原语；题摘未发现新的攻击接口或可验证保证，真实cost/F1工作点不自动改变本项目判断。 |
| 06637 / 06644 | SuiteSparse SpMM roofline重述structure/layout与memorytraffic依赖；CNN指定classifier的variational feature压缩未给基础模型用途控制的直接机制或自适应保证，均不凭通用术语类比保留。 |
| 06699 / 06710 / 06742 | single-factorprompt优化、persona longitudinal任务和CLI blackbox effect tests分别使用已知消融、时序覆盖与functional oracle原则，没有新的保证或重要独立反证。 |
| 06725 / 06736 / 06750 | 单图3D重建+view工具、SQL AST consistency与驾驶场景输入敏感性分别是具体任务组合/指标；题摘未给当前world state真实性、semantic program correctness或通用模态必要性的新增条件。 |
| 06753 / 06757 / 06771 | 三种reasoning模式router、全modal转visualprompt与CQR多facetDPO提供局部architecture组合；题摘的任务指标/数据量未分离出重要控制或alignment有效性新边界。 |
| 06774 / 06787 / 06794 | 无限维operator逼近不是当前基础模型输入/训练机制；reflection-cue sufficiency stop与Fibonacci/consensus search复用成熟控制，未发现本项目长期判断增量。 |
| 06793 / 06812 / 06829 / 06831 / 06833 | 文档functional benchmark、NLI/topic confidence、crossdoc合成、client encoder加噪及federated refusal模板分别是成熟评测/组合；摘要未提出改变当前文档、truth/uncertainty、合成label、privacy guarantee或安全数据身份的条件。 |
| 06845 / 06870 / 06955 | event/entity memory+query路由、crop-resize-paste局部图像修复、SRAMtracebanking分别复用既有机制；题摘没有新的state一致性/编辑保证/功耗模型边界，局部工作点不足。 |
| 06995 / 07007 / 07012 / 07036 | GUI元素中间层、blockchain principal治理、query-conditioned summary tree与小大model uncertainty deferral重述已知控制组合；题摘未分离新的权限/语义truth/coverage条件。 |
| 07079 / 07084 / 07098 / 07121 / 07147 | expand-retrieve-rerank、flow动作best-ofN、neuronamplify、HCI context object及跨batch dedup/promptevolution都是局部已有原则组合；题摘未改变当前检索、控制验证、表示因果、context治理或diversity真实性判断。 |
| 07108 | 重开旧关闭：实际必要方法是frozen encoder/evaluator上局部RBF修正的读写/decay/contradiction lifecycle，不因toy或frozenViT就否定其主线设计分支。已读CIFAR中kernel-only足够和复杂机制冗余等反证，拟标准候选继续真实Books比较，不称通用无遗忘。 |
| 07201 / 07220 / 07236 | queryalignment/迭代query验证和Battleship harness分层各复用已有设计分工，题摘尚未给重要新增机制/反证；不以新任务名保留。 |
| 07238 / 07242 / 07254 / 07266 / 07269 / 07316 / 07331 | 分别为形式language privacy rates、categorical broadcasting表示、普通图像authenticity解释、通用temporal shift metrics、临床双memory Agent、edge smashed-data频域压缩和wearable采集；题摘没有足以改变本项目foundation模型/Infra解释与选择的直接机制，不凭language/state/compiler/privacy词汇纳入。 |
| 07230 | 3D geometry prior与2D/3D联合监督改善单张图像编辑的scale/position工作点；题摘没有新的几何身份/物理状态转移保证或改变已有render与environment transition分账的反证，不把物体编辑准确率当world dynamics有效性。 |

这些均为作者题摘裁决，非作者尚需按共享理由检查安全/纠错/反证强信号和分层排除；若发现反例只重开受影响项，不能把此表当全体负面已独立验证。既有25具体关闭与新增关闭可能重叠身份，最后计数按唯一家族而非表行数。晚于截点的07279/07306/07328/07335/07340/07343/07345/07350先保留日期隔离，不以它们的初步潜在贡献代当窗候选。

[2604.06798v1官方页](https://arxiv.org/abs/2604.06798v1)明确显示该提交由管理员应提交者机构请求撤回；v1 history也标`withdrawn`。不列入候选、不评分、不进入Books，原始记录只保留必要排除依据。

本轮已实际打开06268v1/06664v1官方题摘与history；06268 Submitted=`2026-04-07T04:29:41Z`，06664 Submitted=`2026-04-08T04:31:34Z`，这些原字段不是first-public。其余首批仍须定点核身份及日期/事件页说明；页面不显示某标记不等于它缺失，也不要求搜完整版本史。

## 日期和剩余普通工作

### 首批逐家族官方 DOI 元数据复取

本轮只读取得 `https://api.datacite.org/dois/10.48550/arxiv.<ID>` 的原始 `dates[dateType=Updated,dateInformation=v1]` 和 `created`，24条当前Abstract与库存全文摘要均一致。它证明身份/描述未变化及时间组合中的版本可用上界线索，不单独证明公告时刻。前23条Updated在01:00Z前、07345在01:04:10Z，后者不得凭整批slot冒充09:00前已公开；仍须隔离或恢复更早公开上界。Created全部晚于本窗09:00，反而说明旧DOI-created owner不能继承。

| 身份 | v1 Updated原字段 | DOI created原字段 | 当前摘要与库存 |
| --- | --- | --- | --- |
| 2604.06176 | 2026-04-09T00:00:12Z | 2026-04-09T01:43:11.000Z | 一致 |
| 2604.06188 | 2026-04-09T00:00:29Z | 2026-04-09T01:43:28.000Z | 一致 |
| 2604.06228 | 2026-04-09T00:01:27Z | 2026-04-09T01:44:24.000Z | 一致 |
| 2604.06240 | 2026-04-09T00:01:46Z | 2026-04-09T01:44:41.000Z | 一致 |
| 2604.06241 | 2026-04-09T00:01:48Z | 2026-04-09T01:44:42.000Z | 一致 |
| 2604.06247 | 2026-04-09T00:01:54Z | 2026-04-09T01:44:51.000Z | 一致 |
| 2604.06268 | 2026-04-09T00:02:27Z | 2026-04-09T01:45:20.000Z | 一致 |
| 2604.06297 | 2026-04-09T00:03:01Z | 2026-04-09T01:46:02.000Z | 一致 |
| 2604.06409 | 2026-04-09T00:07:47Z | 2026-04-09T01:48:46.000Z | 一致 |
| 2604.06422 | 2026-04-09T00:08:10Z | 2026-04-09T01:49:04.000Z | 一致 |
| 2604.06543 | 2026-04-09T00:15:40Z | 2026-04-09T01:51:55.000Z | 一致 |
| 2604.06613 | 2026-04-09T00:20:20Z | 2026-04-09T01:53:35.000Z | 一致 |
| 2604.06647 | 2026-04-09T00:23:03Z | 2026-04-09T01:54:23.000Z | 一致 |
| 2604.06668 | 2026-04-09T00:24:51Z | 2026-04-09T01:54:54.000Z | 一致 |
| 2604.06723 | 2026-04-09T00:28:46Z | 2026-04-09T01:56:11.000Z | 一致 |
| 2604.06834 | 2026-04-09T00:36:13Z | 2026-04-09T01:58:49.000Z | 一致 |
| 2604.06836 | 2026-04-09T00:36:28Z | 2026-04-09T01:58:52.000Z | 一致 |
| 2604.06840 | 2026-04-09T00:36:54Z | 2026-04-09T01:58:59.000Z | 一致 |
| 2604.06916 | 2026-04-09T00:41:10Z | 2026-04-09T02:00:47.000Z | 一致 |
| 2604.06996 | 2026-04-09T00:46:32Z | 2026-04-09T02:02:41.000Z | 一致 |
| 2604.07023 | 2026-04-09T00:47:52Z | 2026-04-09T02:03:18.000Z | 一致 |
| 2604.07172 | 2026-04-09T00:55:35Z | 2026-04-09T02:06:51.000Z | 一致 |
| 2604.07173 | 2026-04-09T00:55:36Z | 2026-04-09T02:06:52.000Z | 一致 |
| 2604.07345 | 2026-04-09T01:04:10Z | 2026-04-09T02:10:57.000Z | 一致 |


原缓存有511项v1Updated早于04/09 01:00Z、51项晚于；该字段可能在后版中被改写，不能直接当公告。先沿root已校准的永久ID分配、相邻批次/OAI、官方slot与逐家族可用时间组合恢复有据推断；不能证明上界的贡献项精确隔离。14来源仍有Seed/Meta/部分仓库或目录停点待收口，未完成的候选准入与证据审阅属于普通可执行工作，不因共同日期问题标作全部受阻。
