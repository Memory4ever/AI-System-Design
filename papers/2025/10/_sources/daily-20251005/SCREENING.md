# 2025-10-05 有限筛选

作者Huygens。本窗BJT `[2025-10-04T09:00:00+08:00,2025-10-05T09:00:00+08:00)`。原作者实际读42个精确v1完整题摘及当前submission history；Curie独立额外读03751/03689两项，归并共44身份、39日期潜力（原37+独立2）。新增两项不回填作者原阅读，也不构成Evidence。四主题model7、systems2、agent11、multimodal6，26次命中去重24；本日日期范围官方分类标题补检CL首25/30、CV首25/55、DC8/8、PL1/1、IR2/2，只从已读61个标题定点恢复18个新命名相关项。其余标题不转入全文/题摘队列，也不声称全部分类召回。

请求原值与执行/分页见`acquire.py`、`finite_repairs.py`及各`.receipt.json`；日期查询是submittedDate发现范围，不是first-public证明。最初`/2510`列表404已用`/2025-10`恢复；月页首25多为早于本日的标题，仅作边界线索，不形成逐篇关闭队列。所有拟保留项仍缺官方历史公告/完全落窗公开bounds，日名相交与submitted不准入。当前页轻量检查未见其他撤回/删除；03669明确管理员删除v1，单独排除。

## 明确关闭及删除

| 精确v1 | 具体理由 |
| --- | --- |
| [03606 DINO survey](https://arxiv.org/abs/2510.03606v1) | 完整AB梳理既有mean-teacher/self-distillation/multi-crop及既有表现，没有识别新机制、盲区或修正原判断的证据；非按综述类型排除。 |
| [03815 HCAA](https://arxiv.org/abs/2510.03815v1) | Bayesian诊断、LLM仲裁和temperature scaling的领域组合；必要PDF§3.3.3/3.4/4.1/5进一步实际核：阈值选择性仲裁是具体实现，但未揭示新的校准/可靠性条件，accuracy/ECE不授安全保证；real/simulated数据表述不一致保留。 |
| [03829 A4FN](https://arxiv.org/abs/2510.03829v1) | position将感知→意图→网络配置模式移植飞行网络，完整AB未给新的委派/执行/失效条件；非按局部领域本身排除。 |
| [03859 IoT anomaly](https://arxiv.org/abs/2510.03859v1) | context/memory/attention+XAI组合与rule baseline领域提升；必要PDF§4–7已核，未披露可归因的新模型机制；attention/解释index不是政策合规证明，Jetson/云端部署表述不支持性能外推。 |
| [03669 Token Hidden Reward](https://arxiv.org/abs/2510.03669v1) | 精确页原话：`This version has been removed by arXiv administrators as the submitter did not have the rights to agree to the license at the time of submission`；v1/v2 withdrawn。该版本不入选、不评分、不进入Books；不得用后来有效v3/v4替换本次v1。 |

前四项日期未核实，贡献已明确关闭且必要安全反侧已处理，不另建first-public请求。删除项保留原身份/管理员说明，不记作访问故障。

## 原作者37个日期隔离潜力

每行均对应`abs-2510.<ID>.raw`/`.text.txt`，完整题摘及版本史实际读。以下是准入潜力，不是经证据确认的结论。无分数、无正面Evidence、无Books采用。

| 精确v1 | 约束 → 实际增量 → 待重考虑的选择 |
| --- | --- |
| [03584 FrameOracle](https://arxiv.org/abs/2510.03584v1) | 固定视频帧预算丢失变密度信息 → 同时预测帧身份/数量及keyframe监督 → query-conditioned视觉输入预算。 |
| [03588 REFINE](https://arxiv.org/abs/2510.03588v1) | 公共测试可过拟合draft patch → issue/code context、delta多样性与冲突聚合 → 测试与语义正确的分界；必要core已读。 |
| [03595 Deco-G](https://arxiv.org/abs/2510.03595v1) | reasoning与format指令竞争 → TPM格式概率独立于任务prompt并逐token融合 → 格式约束与任务能力分工，不先接受普遍保证。 |
| [03598 HRM image](https://arxiv.org/abs/2510.03598v1) | HRM成功不意味图像归纳偏置充分 → 无augmentation同优化族CNN/HRM的稳定训练但泛化失败 → 递归推理结构的局部适用边界；负面小模型实验不排除。 |
| [03608 DCS](https://arxiv.org/abs/2510.03608v1) | diffusion augmentation语义错位 → classifier-state的prototype-MMD/variance及logit重校准互馈reward → 生成数据与分类增量学习共适应。 |
| [03611 Graph induction](https://arxiv.org/abs/2510.03611v1) | needle retrieval不能代表关系恢复 → 噪声文本诱导图的早期recall下降 → 有效上下文按关系任务测量。 |
| [03612 CPS](https://arxiv.org/abs/2510.03612v1) | 白盒/整网页假设偏强 → 自有listing图文联合偏好操纵 → 第三方内容信任边界；黑盒victim不代表无需白盒surrogate。 |
| [03636 ICL poisoning](https://arxiv.org/abs/2510.03636v1) | 支持集小扰动可改变ICL → label flip及spectral filtering局部负面评价 → flip/accuracy/pseudo-label不能混同；安全core已核。 |
| [03659 SAE utility](https://arxiv.org/abs/2510.03659v1) | 可解释特征未必可控 → 90SAE弱秩相关及Δtoken confidence选择 → interpretability不能充当steering utility。 |
| [03663 UniDoc](https://arxiv.org/abs/2510.03663v1) | 文图孤立评价 → 文档四RAG范式统一candidate pools对比 → 模态互补及joint embedding失效边界；v1仅20%QA人工核验，不用v3全量声明。 |
| [03666 MonitorVLM](https://arxiv.org/abs/2510.03666v1) | 全规则昂贵且小人物难辨 → clause relevance Top-K与region magnifier → 规则召回/延迟和细粒度视觉的局部代价；检测分数不是事故安全保证。 |
| [03696 Mind the Goal](https://arxiv.org/abs/2510.03696v1) | 单轮质量忽略跨轮goal fulfillment → goal segmentation/GSR及root-cause taxonomy → multi-agent评价单位；六个月变化不先归因。 |
| [03706 EmbodiSwap](https://arxiv.org/abs/2510.03706v1) | human/robot embodiment gap → 合成robot overlay及V-JEPA动作训练 → 数据转换/视觉表示选择的零样本条件。 |
| [03721 LAION person](https://arxiv.org/abs/2510.03721v1) | 训练数据bias归因缺标注 → person-centric标注与co-occurrence→model相关分析 → 数据构成与模型偏差的关系；R²不是因果份额。 |
| [03727 MFM/world thesis](https://arxiv.org/abs/2510.03727v1) | 多模态相关理解不具动态/反事实 → structured reasoning、scene graph与可控4D路线 → 世界状态/视觉生成边界；thesis旧成果事件身份仍待核。 |
| [03731 IniLoRA](https://arxiv.org/abs/2510.03731v1) | zero-product初始化可能限制原权重利用 → 近似原权重初始化及α/β变体 → 低秩适配初始化的训练差额。 |
| [03747 LoRA patching](https://arxiv.org/abs/2510.03747v1) | 静态proactive图扰动不应假定generator固定 → gated LoRA+MMFA绕过及警示输出 → 防御在适配后的有效边界；必要core已核。 |
| [03760 EvoEngineer](https://arxiv.org/abs/2510.03760v1) | kernel进化速度与正确冲突 → 信息引导/elite维护/验证联合框架 → 策略归因及验证预算；五测试非所有输入保证。 |
| [03762 Prompt Balance](https://arxiv.org/abs/2510.03762v1) | English few-shot经验未必跨语言 → WSD不平衡样例对非英语影响 → 提示分布的语言依赖，不排局部负面。 |
| [03763 ARSAM](https://arxiv.org/abs/2510.03763v1) | SAM两次梯度开销 → SGD/PSF分解与自适应复用 → 梯度时间相关性/泛化代价；小模型优化机制仍可核。 |
| [03771 OptAgent](https://arxiv.org/abs/2510.03771v1) | subjective rewrite无唯一gold → 多模拟顾客fitness+genetic refinement → 多judge搜索reward的适用性，不先把模拟偏好作真实user收益。 |
| [03777 GuidedSampling](https://arxiv.org/abs/2510.03777v1) | repeated sampling解题路径重复 → concept exploration/generation解耦 → 同预算候选覆盖及训练轨迹多样性。 |
| [03795 CIR variability](https://arxiv.org/abs/2510.03795v1) | 单run“personalization有害” → 多run/多模型反证、pool bias与输入不对称 → 个性化选择和检索评价可信性。 |
| [03799 socio-political frames](https://arxiv.org/abs/2510.03799v1) | deep概念的隐藏表示位置不明 → 关联frame的singular dimensions → representation解释，但相关不作因果；2024 workshop旧身份待核。 |
| [03805 Step Pruner](https://arxiv.org/abs/2510.03805v1) | token罚可被步骤合并投机 → paragraph-based reward与长度上限停止 → step语义/效率收益边界，v1不用后续停止描述。 |
| [03827 LIBERO-PRO](https://arxiv.org/abs/2510.03827v1) | standard LIBERO高分掩盖弱grounding → 四维扰动及无意义指令反例 → VLA评价泛化；不得将所有模型/扰动都写成0%。 |
| [03840 Mirage](https://arxiv.org/abs/2510.03840v1) | visible-artifact dataset高分不代表detect所有fake → Mirage/Chameleon反差及CoT下降 → judge cue dependence；不是全生成模型fingerprint归因。 |
| [03847 SLM agent survey](https://arxiv.org/abs/2510.03847v1) | open生成能力不能代表schema/API任务 → SLM-default/fallback与任务成功成本评价综合 → 若有具体跨条件证据再准入；10–100×断言尚未采用，不借成熟原则评分。 |
| [03865 RAPO](https://arxiv.org/abs/2510.03865v1) | reverse KL可能抑制罕见解 → forward KL+reward-aware reference及pass-k曲线 → 搜索预算/采样支持区分；理论错误与有限样本ceiling已保留。 |
| [03872 power profiles](https://arxiv.org/abs/2510.03872v1) | facility power cap限制throughput → Blackwell workload-aware power recipe → 性能/能耗联合条件，未采用最高百分比。 |
| [03879 ACToR](https://arxiv.org/abs/2510.03879v1) | coverage不等价跨输入语义 → adversarial differential tests循环 → correctness oracle/测试覆盖的区分，必要core已核。 |
| [03891 RFold](https://arxiv.org/abs/2510.03891v1) | fixed torus shape争用/碎片冲突 → homomorphic job shapes+OCS topology共适应 → 网络shape与放置边界；4096node simulator非实集群。 |
| [03903 fine-grained LVLM](https://arxiv.org/abs/2510.03903v1) | classname生成难精细辨识 → VQA reformulation及attention intervention → label-description与视觉注意的收益归因。 |
| [03913 PsychoLexTherapy](https://arxiv.org/abs/2510.03913v1) | naive history丢多轮一致性 → structured profile对比及路径选择 → memory组织局部条件；无clinical/crisis安全采用。 |
| [03978 LongCAP](https://arxiv.org/abs/2510.03978v1) | 短text encoder截断长caption监督 → 512token encoder及新长监督 → representation context/supervision混杂；不是AI for Science领域应用准入。 |
| [05164 SATER](https://arxiv.org/abs/2510.05164v1) | cascade正确性/成本与延迟冲突 → shortest-response preference+confidence rejection → routing两模式的质量/延迟取舍；ID与submitted日相异只作异常身份，不修造。 |
| [06254 SNN distill](https://arxiv.org/abs/2510.06254v1) | BPTT时维成本且弱self-teacher阻收敛 → rate-based梯度及可靠/不可靠teacher拆分 → sparse模型训练与蒸馏信号边界；不以小模型排除。 |

## Curie独立抽检恢复两项（不回填作者原阅读）

2026-10-05作者实际读回 `FINAL_INDEPENDENT_REVIEW.md` 的两项独立完整精确v1题摘/版本史及具体准入判断。原作者42身份/37潜力保留；加独立新增2后本日归并44身份、39日期潜力，四贡献关闭/一管理员删除不变。以下只记录潜力，不评分、不授正面Evidence、不进Books，不声称作者原42次已读它们。

| 精确v1 | 约束 → 实际增量 → 待重考虑的选择 |
| --- | --- |
| [03751 The Overlooked Value of Test-time Reference Sets in Visual Place Recognition](https://arxiv.org/abs/2510.03751v1) | 部署前已有目标域地图/pose参考集 → Reference-Set-Finetuning → 基础视觉表示适配的训练/测试依赖可能改变，不只VPR指标提升。Curie原页L33–55全AB/历史；Recall@1约2.3%只是摘要作者结果、未核实验；submitted 2025-10-04T09:29:58Z不当first-public。 |
| [03689 SAMSOD: Rethinking SAM Optimization for RGB-T Salient Object Detection](https://arxiv.org/abs/2510.03689v1) | SAM适配非主导模态收敛与高低activation梯度不同 → 单模态监督、gradient deconfliction/解耦adapter → 融合与参数适配选择潜力，不因检测领域关闭，也不把模块组合直接当已证贡献。Curie原页L9–27全AB/历史；submitted 2025-10-04T06:02:12Z不当first-public。 |

39项保留一个共同日期请求，但逐项身份如上：需要精确v1的官方公开公告或完全落窗bounds；不能用DataCite注册、submitted、当前收录或年份替代。材料回来只重开具名家族。当前日期隔离不是贡献排除；不存在“因深审费时缩池”。19份必要原文笔记见`CORE_BOUNDARIES.md`，其余未作全文读取声明。Curie FIRST有效，2026-10-05T09:57:23+08:00 DAY与两恢复项窄POST已实际通过，普通复核剩余0。完成态不解除39项隔离，不授Evidence、Books或无遗漏/安全性能保证。
