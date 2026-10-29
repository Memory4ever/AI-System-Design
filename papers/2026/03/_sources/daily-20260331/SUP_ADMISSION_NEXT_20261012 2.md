# 第二批具体准入提案（待root独校）

44＋额外12具名exact-v1完整题摘/history实际读；原证SUP_AB_DATE与SUP_AB_EXTRA，DOI client全部56 arxiv.content/findable原关系另存SUP_DATACITE_CLIENT。公告最早日与registered上界仅合并为日期范围，不当registered公告。以下命题只为准入，非实验证实，分母未冻结。

| identity | 原有约束→实际增量→需核设计选择 |
| --- | --- |
| 26097 ReinPatch | 固定patch或soft relaxation→离散边界策略GRPG+严格压缩率/可detach→输入codec与backbone联合目标/迁移边界；不是time-series指标本身 |
| 26127 Object-DINO | 末层CLS总结整图→跨层q/k/v对象信息聚类→对象归因/grounding不只末层attention |
| 25931 DiReCT | 负prompt混语义与物理→明确梯度冲突/对齐条件及两尺度负采样→contrastive何时伤FM目标 |
| 25981 PiJEPA | 高维uninformed MPPI初值→policy action prior warmstart latent WM→策略和规划预算/失败互补边界 |
| 25994 NLCE | 删除target伤neighbor→谱方向稳定neighbor+空间残余gate→删除范围/语义邻域代价，不保证遗忘 |
| 26154 IP-Bench | image保护旧任务分数→I2V/preprocessing及crossmodel/crossmodality反侧→保护验收应冻结consumer/攻击协议 |
| 26167 GaussianShannon | fuzzy detection非exact payload→将latent watermark作noisy channel/localflip vs global扰动分账→元数据恢复/检测的不同可靠性条件 |
| 26193 MemCam | 有限frame context大视角变化失一致→压缩memory+co-visibility选择→历史retrieval的可见性与state identity |
| 26211 DiffusionGUI | 坐标mask混结构→几何hybrid mask及steps/length/block精度latency饱和→GUI grounding建模与成本边界 |
| 26320 DFM-VLA | 早actiontoken固定不可改→概率velocity全序列迭代+deterministicvalidation→proposed动作/commit边界 |
| 26330 IADA | SFT感知增益/推理tax→fixed跨depth也恢复、低秩adaptive聚合→不能只以新能力训练忽略旧representation访问 |
| 26357 MPDiT | 每block固定token数→早大patch/晚小patch→训练compute与细节/embedding改动混杂 |
| 26360 RealtimeVLA2 | GPU快不等机器人快→calibration/planning/control+learned execution speed→端到端physical闭环/速度验收 |
| 26666 VLA-OPD | offline状态shift/online稀疏reward→学生selfrollout上dense教师token ReverseKL→mode寻优与teacher不确定性的边界 |
| 26599 VGGRPO | geometryreward RGB VAE反复decode/静态场景→latent→4D geometry+两reward→world-consistency与代价不等安全控制 |
| 26589 VLM affordance | 通用描述近人不等affordance→human-calibrateddistribution+六解释干预→image/text分布训练的局部缺口而非先验必需embodiment |
| 26034 AgentCollab | 外部route/固定tier→self-progress escalation+累计difficulty预算→少/强模型交接/成本验收 |
| 26137 TimeConsistent | currentrepo知识可能混未来→T0知识/未来PR matchedAB+prompt粒度→repo context收益的评价变量 |
| 26664 LearningToCommit | latestsnapshot不含changepattern→历史blindattempt/oraclediff反思技能→futurePR有机性评价/时间隔离 |
| 26653 PerceptionComp | singlemoment捷径→多段conjunctive/sequential/人为禁止rewatch负侧→视觉长推理评价必须控制重复感知 |
| 26639 GeoSR | 添加geometrytoken仍依2D shortcut→mask2D+adaptive geometryroute→fusion可用性与实际采用区分 |
| 26635 AmongUs | deception语言表象不等策略收益→1100游戏角色/pressure/胜率反侧→在该游戏里equivocation未带可靠收益 |
| 26499 AIRA2 | extendedsearch退化可误归记忆过拟合→hidden consistent eval+asyncworker/interactiveoperator消融→选择信号noise和搜索资源分账 |
| 26410 ThinkingAnswer | answer监测不含全部hint依赖→paired misleadinghint条件中thinking/answer通道差额→关键词可观测不是全faithfulness |
| 26348 VRE | 长CoT漂离image→informationgain选择visualreexamination/selftraining→反思需grounded证据，不采普遍hallucination消除 |
| 26323 SpatialPrimitive | task accuracy掩不同机制→三primitive controlledtasks/probe/SAE/intervention+跨语言→局部可用表征不等general spatial能力 |
| 26266 GUIDE | 未见软件planning/groundingdomainbias→subtitle三段retrieve+相邻keyframe inverseactionannotation→教程derived知識与实际工具状态分账 |
| 25960 CoTBackfire | generalprompt经验未必迁移→MedGemma CoT/fewshot/optionperm/context方向与clozescoring反侧→该模型/MC任务的prompt比较不当医学结论 |
| 26494 QuantumMemory | 端点分数不分classical策略→gateablation/interchange显示单/双qubit表征与实硬件noise失败→noise/expressivity边界，非量子优势承诺 |
| 26511 AMALIA | translatedscore隐藏locale能力→pt-PT原生与translated对照→nativevariant评价变量，非语言数准入 |
| 26512 CADSmith | renderjudge不能定尺寸正确→executor内loop+exactgeometry/visual外loop消融→判断分工而非多个Agent数量 |

必要core才能裁决的弱信号：26164 DataFlex共有抽象是否实际改执行/比较条件；26363 uncertainty tree是否新增可用目标；26134 InstaVSR剪枝/训练增量的归因；26322 DiffusionAnything是否有主线model/action机制而非领域控制组合；26362 HandVQA是否仅task增加或controlled blindspot；25823 ViGoR dual-processjudge是否真实不同metric；25973 MemoryCD真实user/crossdomain是否改变memory评价选择；26648 Vision2Web verifier是否有独立新约束；26221 Clawed安全taxonomy是否仅重述；26557 MemBoost复用cache/RAG/tier组合是否有独立新机制；26539 openness是否只重述透明性原则；26389动态margin在contrastive表示学习的因果边界；26270 Knowdit是否仅DeFi图谱+既有PoC loop应用。

代表性拟EX：26008仅临床MI正则/LoRA公平应用，暂未见改变主线机制；25813既有autoresearch/BitNet/DiLoCo/on-chain组合案例；26207词义holism哲学争论；26823既有系统材料综述；26100/26085推荐pipeline提升agent blueprint缺新执行/失效机制。安全/反侧不得靠标签关闭，root否定理由将只恢复受影响项。

Qwen必要日期门与28651延迟公开（registered31跨补30上界）另隔离，不纳确定分母。Apr/Jun IDs查询只有SubmittedMarch，未当公开日，相关具名线索将核原public metadata后定点记录。
