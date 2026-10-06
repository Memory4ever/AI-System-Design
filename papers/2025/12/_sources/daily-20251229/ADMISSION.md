# 12/29 题摘与贡献判断

检查时间2026-10-02T18:34:04+08:00。仅实际主题查询及月列表邻接发现的29项相关身份，原始HTTP已读官方 `https://arxiv.org/abs/2512.<ID>` 完整标题/abstract，当前页面未见撤回提示。当前abs不等于精确冻结v1正文。以下potential缺逐ID首次公开，未记确定当窗候选、不评分、不采用Books；不因为日期缺口跳过可执行题摘。

| ID | 具体判断 |
| --- | --- |
| 23180 GaussianDWM | Potential：每Gaussian注入语言特征早期对齐、task-aware采样压缩3D token及双条件生成，改变仅生成无3D语义理解的DWM。 |
| 23162 SurgWorld | Potential：[SurgWorld exact v1](https://arxiv.org/abs/2512.23162v1)；Cosmos-H-Surgical仅为稿内相关模型称谓，不替代论文题名/版本。无action视频经world model生成与inverse dynamics补pseudo-kinematics，再训练VLA；动作数据稀缺链值得核，不能声称医疗安全。 |
| 23161 decentralized representation | **范围关闭**：完整摘要只研究共享低秩线性回归的decentralized projected gradient与样本/迭代界；未说明基础模型或其计算机制的直接关系，不借通信类比引入。 |
| 23109 uniform convergence | Potential：prompt embedding Lipschitz与低维谱结构下VLM诱导分类器的uniform accuracy/calibration界，医学动机不排除通用表示理论；须保留假设。 |
| 23077 MoVLR | **重开potential**：[exact v1 §4.2–4.3/§5.2](https://arxiv.org/html/2512.23077v1)定点读VLM比较当前best dynamics并反馈reward局部搜索，reward无再优化转移到rough/sloped/injured morphology的成立/退化边界，及单统一VLM反馈+code生成消融。原摘要无归因关闭撤销，不能把控制反馈组合一律排除；不采用收益。 |
| 23073 mask tuning VLM | Potential：冻结权重、语言/projector子网gating的跨backbone PEFT比较，可能新增结构重参数化适用证据。 |
| 22991 fusion complexity | Potential/反证：19方法/9数据的统一调参、初始化、CV与统计测试，检验复杂融合对简单基线的必要性。 |
| 22969 CLIP-Joint-Detect | Potential：region/grid对齐可学习text embedding与joint detector loss、跨架构消融，需核共享表示收益归因。 |
| 22933 RW-Post | Potential/评价：可审计evidence链接与closed/evidence-bounded/open-web受控协议，区分视觉grounding与证据使用。 |
| 22881 GPS | Potential：CFG外推导致refinement离流形误差增长，以流形约束插值与guidance schedule稳定；须核理论域。 |
| 22877 M-ErasureBench | Potential/安全反证：text/embedding/inverted latent五场景揭示erase跨输入模态失效，latent扰动防护需权限和质量对照。 |
| 22867 MUSON | **重开potential/评价反证**：[exact v1 §III–V](https://arxiv.org/html/2512.22867v1)定点读long-tail accuracy掩盖稀有动作、Macro-F1及reasoning/action一致性；§V-B SNEI CoT退化而结构一致MUSON CoT改善。新增dataset本身不是贡献，但这些监督噪声/代理评价边界可准入；不采用safe navigation保证。 |
| 22802 ReDiF | Potential：terminal reward替代轨迹回归，允许非可微/多目标并给同单GPU预算比较，改变distillation数据/训练成本。 |
| 22799 VPTracker | Potential：region位置prior与必要时global搜索，具体应对遮挡/干扰切换；需核局部/全局预算与模式消融。 |
| 22796 EPD | Potential：并行gradient ODE积分与低维Dirichlet solver policy，而非backbone RL，需核硬件并行/曲率误差界。 |
| 22748 TrimTokenator-LC | Potential：图内/图间冗余拆解及动态预算、diversity/alignment Pareto筛选，针对多图长context。 |
| 22737 WeDLM | Potential：observed token物理prefix、逻辑位置保留的topological reordering及流式commit，实现因果attention/prefix缓存兼容的diffusion。 |
| 22647 FinPercep-RM | Potential/反证：全局IQA reward被局部伪影hack，spatial degradation map与reward/policy共同curriculum稳定训练。 |
| 22626 Envision | Potential：region-aware goal image与first/last-frame条件插值，检验纯forward预测的goal漂移。 |
| 22615 Dream-VLA | Potential：diffusion双向骨干适合action chunk的跨objective/AR比较，需核训练预算与action控制闭环。 |
| 22545 SR-MCR | Potential：五项内生process reward与confidence cooling及消融，需核self-reward闭环偏差，非自己验证即可信。 |
| 22539 VLA-Arena | Potential/安全评价：三正交难度轴、L0训练/L1L2泛化及排名反转，区分memorization与grounding/safety。 |
| 22519 OBEYED-VLA | Potential：object-centric与几何grounding解耦perception/control，单对象无clutter训练检验absent target/新clutter失效。 |
| 22857 AutoForge | Potential：自动可验证高难环境合成与environment-level advantage，针对用户模拟不稳定/异构环境。 |
| 22955 diversity/precision | Potential/反证：pretraining reward shaping与rank-aware负token，反证高entropy必有更好RL探索。 |
| 23014 FANG | Potential：按语义功能分组/加权、跨context神经元保留与block sparsity，针对少样本pruning校准偏差。 |
| 23032 CoT faithfulness | Potential/度量反证：hint未verbalize不等于不忠实，faithful@k与causal mediation区分budget/不完整解释；不声称所有CoT忠实。 |
| 23049 Prompt Choreography | Potential：跨call重排global KV及fine-tune修正cache/re-encode语义差异，改变multi-agent重复计算与一致性权衡。 |
| 23145 reservoir MatMul-free | Potential：共享/冻结部分权重与reservoir dynamics结合访存融合，需核训练成本与质量归因。 |

29题摘：28 potential、1范围关闭。MoVLR/MUSON按root共同理由纠错，作者2026-10-02定点读决定准入的上述v1部分，原负侧计数撤销，普通准入补读已完成；不是深审/Evidence通过。22630已在28同身份完整题摘判断，定点复用其设计分析potential，不复用日归属。明确标题范围负侧：23130病理MRI合成、23056 PDE物理AI暂缓、23025心理健康叙事应用、22946捕食者趋化、22921粘弹流、22878医学分割、22689影像配准、22683宇宙背景、22585两相流、22558相位物理、22535无线地图、22503月表领域应用、22493 PDE，不按这些宽库存增加读文任务。2601 datehold身份不移回December。
