# 12/30 实际发现题摘判断

检查2026-10-02T18:42:46+08:00。仅三主题与月身份邻接实际发现的59个新增相关身份，通过原始HTTP读官方 `https://arxiv.org/abs/2512.<ID>` 全题摘；长输出被截断的14项及LiveTalk/ProGuard/RouterBench/PI四项定点重取，已读完整，不冒称冻结v1正文。未见当前撤回提示。potential首次公开仍缺，不评分、不计确定本窗候选、不采用Books。以下是具体准入潜力而非收益成立结论。

| ID | 具体判断 |
| --- | --- |
| 23905 SPM | Potential：稀疏pairwise stage替代dense operator，闭式forward/backward与容量约束，需核任务结构条件。 |
| 23881 audio encoder attack | Potential/安全：不访问下游LLM的通用latent扰动，揭示encoder级攻击权限边界。 |
| 23858 Yggdrasil | Potential：equal-growth树适配static graph、latency目标选draft及stage调度，针对动态speculation/runtime失配。 |
| 23847 lookahead bias | Potential/评价反证：[exact v1](https://arxiv.org/abs/2512.23847v1)的LAP描述为pretraining data detection likelihood；date-only recall属于当前修订题摘，不能倒填v1。按root独立v1核准保留forecast lookahead/data-leakage诊断潜力，首公开仍hold；未采用当前修订作为v1证据，不提供金融建议。 |
| 23836 admit ignorance | Potential/评价边界：retrieval chunk大小在相关/噪声间取舍，insufficient evidence却答错的具体失败来源值得核。 |
| 23760 ASG-SI | Potential/安全：skill promotion需verifier replay/contract检查与可重构reward，需核实际artifact及不能由自审授可信的边界。 |
| 23693 span feedback | Potential：局部改写链相邻pair而非全答案A/B监督，改变preference数据归因粒度。 |
| 23684 hidden PI | Potential/安全反证：等语义四语言隐藏指令控制发现评审劫持差异，需核PDF呈现/模型访问条件。 |
| 23572 VLM instruction | Potential/反证：视觉tuning削弱旧格式遵循、显式format数据介入检验，修正只看视觉指标假设。 |
| 23547 KG hallucination | Potential：生成答复转原子实体/关系用于自检，与SelfCheckGPT比较；需核自检误差独立性。 |
| 23518 MoLaCE | Potential：prompt-specific latent concept activation mixture对抗确认偏差，区别单一固定干预/多agent相关错误。 |
| 23512 UniHetero | Potential/反证：200M+样本下semantic generation有益而pixel loss干扰理解，修正统一生成必有协同的假设。 |
| 23511 MATP | Potential/评价：FOL转换与多步theorem proof检验答案正确却逻辑错，需核转换忠实性。 |
| 23471 semantic density | Potential：density层级与中间分辨率semantic alignment峰值，需核是否改变embedding索引粒度而非只是聚类可视化。 |
| 23453 CoFi-Dec | Potential：coarse/fine视觉hypothesis生成与Wasserstein融合分布，需核额外T2I成本及自反馈hallucination。 |
| 23430 C2PO | Potential：counterfactual隔离spurious features与logit敏感preference抑制，针对两类bias互相恶化。 |
| 23356 SGR | **重开potential**：[exact v1 §3/§4.3](https://arxiv.org/html/2512.23356v1)定点恢复schema-based subgraph与Neo4j retrieval分拆消融；存在可核结构检索归因，不因摘要成熟组合关闭。KG质量/覆盖及构图开销限制未采纳为普遍结论。 |
| 23340 collaboration law | Potential/理论边界：minimum-loss oracle下heterogeneous pool参数预算scaling，不把oracle上界当可部署ensemble收益。 |
| 23329 backprop tutorial | **贡献前关闭**：index-free解析梯度与最小GPT实现为教学推导，未给新梯度/计算机制、反证或适用约束。 |
| 23310 Splitwise | Potential：head/FFN子块切分与Lyapunov队列稳定、checkpoint/backoff恢复，需核不混淆同名历史系统。 |
| 23258 CEM | Potential：timestep/cache interval累计误差近似与DP选策略，纠正固定cache计划的错误变化。 |
| 23219 UAVBench | Potential/评价：空间bias与多视角理解瓶颈诊断而非仅新增UAV条目；需核任务难度/混杂。 |
| 23214 Anka | Potential：显式受限DSL与Python跨模型多步任务对照，检验syntax/state自由度的生成错误边界。 |
| 23213 PeerReview | Potential：多judge分数的graph truth inference及统一ensemble协议，需隔离correlated judge偏差。 |
| 23184 model belief | Potential：token概率估计与choice采样均值的渐近等价/variance界，可能改变LLM统计采样预算。 |
| 23173 EquaCode | Potential/安全：equation/code双模块消融检验跨任务安全失焦，单query预算需核。 |
| 23167 SPIRAL | **重开potential/设计反证**：[exact v1 Ablation/Appendix B/G/H](https://arxiv.org/html/2512.23167v1)定点读取equal-budget MCTS/组件消融，模拟器与critic共同接受hallucinated literal参数、固定budget导致提前finish、串行搜索误DAG依赖，以及latency/API效率取舍。原摘要关闭撤销；simulated grounding不等于真实tool rollout，正确率不采用。 |
| 23126 InSPO | Potential：alternative-response conditioning与scalarization/reference不变性，须核全局最优证明假设。 |
| 23097 hybrid IL/RL | Potential：trajectory KL+reward梯度的dense closed-form与sparse MC分解，需核off-policy估计。 |
| 23087 DVP | Potential/反证：低概率tail放大train/infer logprob偏差，vocab裁剪以有界bias换稳定性。 |
| 23075 TRM | Potential：长序列trust region界与whole-sequence masking，反证token clipping控制最大divergence的充分性。 |
| 23070 FLEX-MoE | Potential：非IID/容量限制下client-expert fitness与全局load平衡assignment，属于expert机制而非仅无线应用。 |
| 23029 private LLM server | **重开potential/局部部署边界**：[exact v1 §3–5/Conclusion](https://arxiv.org/html/2512.23029v1)实际定点读Q6/RTX5090/llama.cpp下input/output长度及concurrency、同步burst对排队影响；明确单model/GPU/localhost/synthetic与runtime限制。原摘要关闭过早；可核局部quality/resource取舍，不把其云比较或8–12 sweet spot当通用SLO。 |
| 22925 Argus | Potential：length-aware预测与prefill/decode成本联合Lyapunov offload，damping/congestion求解动态资源。 |
| 22905 JavisGPT | Potential：SyncFusion与synchrony-aware query桥接JAV-DiT、三阶段训练，针对音视频时序联合理解/生成。 |
| 22827 FasterPy | **重开potential/评价与执行边界**：[exact v1 §4.5/5.7/8](https://arxiv.org/html/2512.22827v1)定点读小模型prompt保留suggestion而排slow-code污染；benchmark从每snippet subprocess改persistent subprocess+thread exec/new namespace及插桩计时。改计时/执行边界有准入潜力，不能把namespace/thread等同安全隔离或sys.exit以外终止防护。原摘要组合关闭撤销，待确日后受影响可靠性必须深审，不采用快/安全保证。 |
| 22790 ChatGraPhT | **范围关闭**：node-link对话分支/merge与用户反思交互设计，不是模型形成或Agent执行系统机制；不借memory标签引入UI设计。 |
| 23965 SFS temperatures | **范围关闭**：multimodal指多峰概率分布、Euler数值采样收敛，与多模态基础模型非同义；摘要未给学习模型机制关系，不通过关键词纳入。 |
| 23953 T2VAttack | Potential/安全反证：语义/时间目标下synonym/插词微扰造成视频失配，需核生成随机性与攻击预算。 |
| 23897 WMFM | **重开potential/跨模态噪声边界**：[exact v1 §V-C/VII-C.3](https://arxiv.org/html/2512.23897v1)定点读同scene-class/Lipschitz等假设与CSI噪声强度干预；clean预训练遇noise退化、适量噪声训练改善而过量破坏跨模态feature。对照给具体表示鲁棒性边界，不只是6G任务名；InfoNCE成熟理论本身不是新贡献，不接受低loss必保证下游线性预测的概括。 |
| 23709 Stream-DiffVSR | Potential：past-only frame级因果distillation/运动对齐与decoder，检验chunk等待/未来帧依赖的流式时延。 |
| 23705 transparency | Potential：video diffusion光学先验转depth/normal的LoRA与时间一致性、grasp跨材质验证，需核合成数据/先验归因。 |
| 23676 Web World Models | Potential：代码状态/physics与model imagination分离及typed deterministic exploration，需核是否新增可验证执行机制而非成熟web包装。 |
| 23592 TWIN | Potential/训练边界：same-object细粒度pair训练与unseen领域/通用VQA保持对照，可能修正粗识别数据偏置。 |
| 23576 LiveTalk | Potential：multimodal conditioning导致Self Forcing闪烁/黑帧的新失效及输入质量/初始化/schedule干预。 |
| 23573 ProGuard | Potential/安全：modality-balanced分类与synonym reward下OOD类别描述，需核真正OOD/类别泄露。 |
| 23562 RouterBench | Potential/评价：sample-model原始成本/质量矩阵与throughput下routing-oracle差距，需核归一化排名/成本协议。 |
| 23557 provenance defense | Potential/安全待核：跨agent text/image sanitizer、output validator、source/trust provenance针对PI传播；成熟结构本身不足准入，具体防护成立/失效主张需必要审，日期未知不当已关闭安全负侧。 |
| 23541 Act2Goal | Potential：imagined trajectory近密/远稀MSTH与闭环control、hindsight LoRA，区分goal规划与扰动reactivity。 |
| 23426 DDSPO | Potential：backward denoising contrastive policy pair直接step监督，纠正terminal forward-process近似失配。 |
| 23412 MindWatcher | Potential：interleaved multimodal tool reasoning/图像操作及agentic RL继承现象，需要精确证据辨别工具组合与真实训练边界。 |
| 23239 RS-Prune | Potential：entropy与scene-aware分层采样平衡高prune多样性，提供diffusion数据分布约束，非只遥感指标。 |
| 23243 RAH-VLA | Potential：动态resolution与object/region/global层级alignment，需核机制与跨粒度语义预算归因；VLA此处不是action模型。 |
| 23232 SGPS | Potential：SURE gradient/PCA噪声纠正早中期posterior trajectory，检验low-NFE误差积累。 |
| 23210 learned timesteps | Potential：task-aware timestep选择/feature consolidation针对few-shot任务偏置，改变只凭经验选择diffusion表示。 |
| 23260 SAILS | Potential/安全：SAE decoder方向初始化LoRA分离安全polysemanticity，monosemantic recovery误差与理论假设必须核。 |
| 23343 memory survey | **贡献前关闭**：taxonomy/存储/lifecycle/benchmarks/安全与未来方向综合，未给新机制、反证或修正既有约束的具体证据；不按综述标签普遍关闭。 |
| 23422 EntroDrop | Potential：低熵token主导重复训练，entropy dropout curriculum针对高熵generalization退化。 |
| 23447 ERC | Potential：router embedding proxy与expert双向activation约束、固定n²辅助成本而非token数，针对router/expert能力失配。 |

59新增题摘：55 potential、4明确关闭。2026-10-02按root共同理由纠错，对9关闭项先辨含糊准入事实，5项上述必要v1差额局部读取后重开；四项tutorial/ChatGraPhT UI/多峰数值采样/综述具体原范围理由保留，不默认全文。旧50/9计数与这5项摘要关闭理由撤销。准入补读普通待办0，但不是精确正文/Evidence验收；全部potential仍需first-public安全保留。其他29已读身份只定点复用其具体题摘判断/日期请求，不复用日级完成。明确范围标题负侧：医学诊断23932、InSAR预测23906、金融QA23848、新闻bias应用23835、Burgers量子求解23817、婚姻话语23609、教育任务23601/23587、化学RxnBench23565/临床23440/肽23175/PDE23192/烟草23137暂缓或领域应用；无安全提示才按明确标题范围停止。Jan/Feb datehold身份不以December提交挪回。
