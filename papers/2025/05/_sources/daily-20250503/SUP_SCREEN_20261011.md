# 2025-05-03 补充筛选记录

只处理新增窗口 2025-05-02 完整 BJT 自然日；基线旧窗口和有效研究冻结。四组主题 discovery 共 143 unique 题名，是提交日期代理/当前版本线索，不是 May2 新公开论文分母。model/systems/agent/multimodal 返回分别 106/7/77/38，各自 start=0、max_results=200、total<200。宽词带来的传统控制、领域预测噪声仅作题名查漏，不变成全分类全文队列。

准入表129个2505身份均实际读完整精确v1题摘，通常原件为`SUP_ABS_<ID>v1_20261011.html/json`；03790复用Cicero的具名v1abs raw，00598按实际v1 HTML正文AB恢复错配。后述14题名查漏不声称已读AB。P不等于当窗候选或Evidence完成；公开日未确定不评分、不采用、不进入Books。当前官方页143个发现身份轻核另存`SUP_CURRENT_<ID>_20261011.raw/json`，逐项核标题/comments/history/withdrawal/notice；后版不替代v1贡献。早期`SUP_CURRENT_2504.raw`/`SUP_CURRENT_2505.raw`为错误短文件名缓存，已弃用，不能作逐ID current证据；正确逐ID原件另取得。00503 state correction只是机制，00174实际纠错及00359撤回/00225重要纠错另具体处置，不授整体无标记。

P 的共同未读边界：除下述必要准入片段外，实验可信度、实现、完整附录均未做一般 Evidence 审阅；潜在贡献明确仅日期未知即可停止。统一精确日期请求为：该 ID 的官方 May2 公开列表/公告，或作者/出版方明确 first-public 自然日。不得用 API published（submission）或月份编号补造。官方 advanced search 实际提示 announcement 只支持年月；同日范围参数报错。日期列表 `/list/cs.CL/2025-05-02` 与 LG 同入口均 HTTP400，未取得日级历史列表，不 catchup。

| 2505 exact-v1 | 裁决 | 实际增量或明确关闭理由 |
| --- | --- | --- |
| 00091 | P | 必要§III-B/C、IV-B已读：语言tuple后Gaussian任务场、流场平滑与局部vortex分配的实际替代执行路径；不采模型解析排行榜或城市部署保证 |
| 00105 | P | float8/int8/PCA 同存储压缩下质量取舍，改变 embedding 存储/维度选择 |
| 00114 | P | 小规模本地文化数据对大量非本地翻译数据的反向结果，改变 dialect 数据选取与评价 |
| 00127 | P | 长度与正确性不单调及难度失配，短答偏好干预挑战无差别推理扩展 |
| 00134 | P | 解剖语境精度/提示方式受控变化，模型复杂度不保证诊断表现；不按医疗名关闭 |
| 00135 | P | disparity-warp 对透明/镜面场景失效，直接视频生成视角作为替代 |
| 00136 | P | Python绑定异步task运行时 vs 仅低层BLAS并行的扩展取舍，GP为测试载体 |
| 00147 | P | skill提示伤简单题小模型，按失败及缺失技能选实例而非总注入 |
| 00150 | P | 已核必要core：先定位有害语义来自单/联合模态，再选修改模态；随机选模态对照暴露改错无效 |
| 00153 | P | 已核必要core：高频被动感知输出造成过载，输入降频增加迟延，输出端 novelty/permanence 状态化过滤的局部取舍；不采安全保证 |
| 00156 | P | 已核必要core：相似架构/词表下内部后层融合，early/branch 对照支持融合位置条件；边际与联合配置矛盾不照录最优参数 |
| 00162 | P | bi-fidelity surrogate line search 降高保真查询数，含黑盒语言模型微调及收敛条件 |
| 00174 | C | 对机构研究产出主题的文献计量及部署可观测性政策建议，无新模型/系统设计或实际可靠性实证；current纠错Academic→Corporate已核v2风险统计相关段，不授实际模型安全反证 |
| 00186 | P | proto-object 替代固定patch降低attention表征复杂性与训练成本，视觉RL不是自动范围外 |
| 00190 | P | nested SAE 重建/相似性优势与剪枝SAE可解释性反向取舍 |
| 00195 | P | 同时行动的数据集体使孤立干预效力下降，暴露多方数据操纵的交互条件 |
| 00204 | C | 已核必要core：价值频率映射归一化，kappa只验证映射一致，没验证实际安全量具；gate仍建议 |
| 00209 | P | point-track 运动表示比FVD等敏感，关联人评且可局部定位，改变生成视频评价 |
| 00212 | P | 责任agent与decisive-step归因低可靠性，强推理模型不等于可靠自动调试 |
| 00216 | P | 黑盒ensemble在线反馈/本地优化均衡机制；可访问/可优化假设留Evidence |
| 00227 | C | 科学数据渐进重构/误差控制GPU实现，未建立模型训练/推理执行或表示机制的具体关联；不以GPU词准入 |
| 00234 | P | 成功轨迹库、collection/exemplar按经验效用选择可替代任务定制知识工程 |
| 00237 | C | energy-based障碍轨迹与MPC几何约束的传统导航，无foundation/VLA/模型驱动Agent知识链新增 |
| 00240 | C | 已核必要core：BERT变体分类+规则/树处置+Docker，无新的执行机制或传统方法可比失效边界 |
| 00254 | P | 超长流视频EKG在线索引与检索生成替代整视频上下文，成本与语义丢失留Evidence |
| 00259 | P | Hessian-guided pack 重构保留跨block依赖，量化粒度替代而非仅榜分 |
| 00263 | P | 已核必要core：controlled recall/no-context暴露parametric记忆掩盖retriever质量；不泛化BM25优势 |
| 00268 | C | 一致性定义/现状/研究缺口综述，无具体新增机制或修正重要判断的证据 |
| 00275 | C | v1是专病视频Video-LLaVA微调/指标应用，未给新通用机制或失效条件；不借新版latent题名 |
| 00282 | C | MARS是外部descriptive/causal estimand统计推断，不是模型推理计算/交付机制；非把inference当serving |
| 00284 | P | v1 LightEMMA 12 VLM预测、时间与成本局限，场景解释不等于可靠控制；不借后版纵向评价 |
| 00299 | C | 既有A3C用于一般microservice调度，不给AI训练/推理负载新约束或学习机制 |
| 00304 | P | 连续动作、未测混杂下policy value识别/估计及policy-gradient界，学习有效性条件 |
| 00315 | P | expert-choice按head内容稀疏，同预算/perplexity-matched资源对照 |
| 00322 | C | bicycle动态+hypergraph交通轨迹产生TTC安全指标，无VLM/模型系统评价反证；具体安全信号不是模型漏洞 |
| 00334 | P | quaternion wavelet/time-aware conditioning 在denoising阶段融合，结构/感知取舍 |
| 00337 | P | 人评、law hint及counterfactual揭示物理一致性被像素/美学指标遗漏 |
| 00347 | P | optimizer超低bit的signal swamping/梯度方差两失效及log quant/momentum方案 |
| 00350 | P | preservation sets指导剪枝量化的关键特征/资源取舍；safety不是自动系统安全保证 |
| 00358 | P | 语义重分域+训练梯度Gram混合，改变预设域与额外评价成本 |
| 00364 | P | 多粒度tree coarsening/perturbation/routing突破固定粒度解释限制 |
| 00367 | P | LLM对显式标记与依赖语境分类的专家差异，synthetic-label有效性边界 |
| 00368 | C | 必要§III-IV已读：holon层级/三步安全check/LLM交通编排是conceptual scenario，无可核执行契约、故障语义或实际安全验证；不是交通或安全标签关闭 |
| 00389 | P | decoder结构单forward contrastive表征，降低重复计算 |
| 00415 | P | selective meta-learning防异域负迁移、adaptive expert扩展，学习/表示机制而非仅工业指标 |
| 00416 | P | next-action与历史backtracking共同训练，增加GUI动作演进学习信号 |
| 00422 | C | 必要§3-5已读：BERT/EfficientNet两token标准Transformer及共识/置信selftrain，单模态/噪声image/半监督消融只证本任务模块收益；置信不保证正确是既有限制非新实际反证 |
| 00426 | P | diffusion discriminator关联ICP、pushing-away处理overlap，零标签组装机制 |
| 00443 | P | topic-aware random-walk peer检索/消息取舍，不把去中心化当隐私保证 |
| 00455 | C | Q&A+annotation外显专家知识服务dataviz，未给模型/执行/可信新成立条件 |
| 00467 | P | 临床red-team发现开发者可能漏掉的伤害路径且跨模型复核；2024 workshop不证明同稿公开日 |
| 00472 | P | 已核必要core：deadline分高/低计算路径、calls/similarity/precision Pareto选候选及memory反馈；不采VoI最优/CPU可靠性 |
| 00473 | C | 扩展transformer多输出预测物理动态系统，范围是科学/工程领域预测，不新增基础模型知识链 |
| 00479 | C | dependency parsing/transformer用于法规提取的应用指标，无新机制/评价失效条件 |
| 00482 | P | noise-dependent权重和unbalanced timestep在RGB-depth联合/条件任务之间统一 |
| 00488 | P | nominal+adaptive corrective policy在未知载荷/地形下的策略适配边界；不采普遍控制安全 |
| 00500 | P | partial observation到implicit SDF、RL探索repr微调，减形变策略的状态/采样约束 |
| 00503 | P | density-aware variational OOD state correction，优化结果/密度联结的离线策略边界 |
| 00506 | P | hallucinaton detector任务/长短context/输入表示差异，不从最佳排行榜推条件 |
| 00509 | P | self-ablation局部专门化增强但全局稀疏降低，反驳稀疏=解释性的单调假设 |
| 00515 | P | adversarial diffusion guidance结合物理可行性selection，改变安全压力集现实性条件 |
| 00527 | P | interaction atomic skill与spatial chaining的long-horizon组合泛化接口 |
| 00533 | P | high-certainty实例相关对齐替代missing source correlation，免backprop机制及理论条件 |
| 00540 | P | 单learner定期共享模型、隐式角色reward替代全agent学习的计算/通信路径 |
| 00546 | P | 直接forecast belief避免recursive误差累积，并支持多步bootstrap |
| 00551 | P | 必要§2.1.3/Fig3及§3.3已读：实际同源数据依赖图、去污染记录及不同CoT长度分布，改变独立数据集/无重叠比较假设；不是R1算法汇总自动准入 |
| 00557 | P | HIP vs null-fusion局部幻觉压力反证，HQP有效性留Evidence |
| 00562 | P | STL graph编码+flow匹配处理一般spec与OOD，改变固定spec神经planning |
| 00568 | P | 同一masked multimodal预训练模型适配任意模态子集，无架构修改，缺模态有效性条件 |
| 00570 | P | 低频KV固定缓存迭代压缩连接训练和推理长context |
| 00580 | P | circulant/diagonal因子化与non-square block避免构weight delta，用1D FFT |
| 00582 | P | block circulant adapter及stable训练heuristic；与00580共同作者/会议，同家族关系尚未采用 |
| 00590 | P | 观测时点adaptive linear weights与变量表征处理不规则采样/asynchrony |
| 00596 | C | DetPOMDP有限状态controller/MCVI传统planning，无foundation model机制关系 |
| 00598 | P | abs页AB误配攻击benchmark；实际exact-v1 HTML题名/AB/§2一致是outlier-free attention与Germ-T小步续训，免from-scratch但低bit恢复较弱的适配/PTQ取舍。只按正文机制保留，不采abs页攻击主张 |
| 00603 | P | 类比检索recall与因果结构precision分离，对人/模型error对照 |
| 00610 | P | 查询转时序logic并以MCTS/MDP树证据约束解释；AAMAS extended abstract首稿身份待核 |
| 00615 | P | 单图face评价区分posed/neutral geometry，DINO per-pixel normal/uv约束3DMM；不是仅新dataset规模 |
| 00624 | P | 已核必要core：gradient TopK SAE特征、seed cosine域数据与pruning/distillation联结，恢复知识取舍；没证独立SAE因果优势 |
| 00626 | P | task/BOS代理role shortcut，position-ID边界信号，不采完整注入防御保证 |
| 00627 | P | hypergraph多模态融合+动态个体kernel adapter，模型适配机制而非仅病种准确率 |
| 00631 | P | 多敏感属性近似公平的instance-dependent阈值及group-membership条件，通用评价/学习约束 |
| 00649 | P | 已核必要core：merge alpha过大会覆盖IR知识，不同模型/域无共同最佳alpha，需局部calibration；不只18% headline |
| 00651 | C | IoV轨迹的prompt迭代+fed轻edge/cloud+synthetic组合，AB不提出新的模型/执行或隐私成立条件 |
| 00654 | C | 已核必要PDF：预设不学概念映射，同条件概率不识别到完全不能理解无逻辑桥；不是因负面关闭 |
| 00661 | P | data-matched ICL/SFT泛化差异，reversal在更大知识结构中资格条件，inference增广 |
| 00662 | P | step multi-perspective critique-of-critique与MC正确性RL，改变浅judge反馈 |
| 00663 | P | Wasserstein policy flow投影更新同时用Q-action梯度/一般随机policy，无reparameterization条件 |
| 00675 | C | memory表示/六操作taxonomy与资源综述，没有具体新失效证据或机制 |
| 00679 | P | 已核必要core：开放style prompt会copy target/改meaning，register约束及对照揭示style强度不等于语义保留；不采任意style无损 |
| 00681 | P | 视频reasoning traces暴露temporal localization/perception而非logical主导，答案分不能辨归因 |
| 00684 | P | region zoom+image-as-map聚焦视觉计算/记录，成本收益留Evidence |
| 00685 | P | power transform+Gaussian training noise的normality normalization及宽深batch条件 |
| 00687 | P | 原分辨率guidance与latent diffusion分支隔离，VAE conditioning丢结构的替代 |
| 00693 | P | sketch对象时空符号→keypoint→3Daction，改变语言空间歧义接口 |
| 00703 | P | semantic/token两级CoT同一步BiCoT-GRPO优化，视觉生成reasoning接口 |
| 00704 | P | 必要§4.1/4.3/5.3后改原C：连续strength map、temporal模块移除使瞬态雨雪失效，sim/gen/real分别提供控制/泛化/真实性条件；非只天气编辑榜分 |
| 00749 | C | 已核必要core：MCP封装/thread/钱包服务概念叙述，无可核wire/schema/故障语义，规格承认会变 |
| 00751 | P | self-attention maps/cross-attention values分别控制结构与attribute，训练free细粒度修改 |
| 00753 | C | HAS组成/人类反馈/orchestration综述，无具体新可靠性反证/执行机制 |
| 00759 | P | evaluator主动prompt、static评测效率与human correlation对照，需核相同排名是否遗漏风险 |
| 01456 | P | multimodal unlearning攻击比单模态更强、internal residual删除条件 |
| 01457 | C | 已核必要core：现成region/page/OCR+RRF+Yes rerank，榜分混bugfix/模型，无新模块成立条件/具体纠错影响 |
| 01458 | C | simulator特性/硬件/资源选型综述，没有新的sim-to-real机制或关键失效证据 |
| 01459 | P | entropy token routing、xLSTM expert及balancing应对rare/common token计算取舍 |
| 01462 | C | affect tag/episodic记忆思想类比与moral standing推测，无可核学习/系统机制或有效性条件 |
| 03788 | P | consistent-but-wrong高置信，cross-modal grounding与grounder自身calibration |
| 03792 | P | counterfactual识别action-critical token、软RL针对性exploration及改进界 |
| 03793 | P | Hessian PAC-Bayes/NTK scaling预测fine-tuning动态，降低model selection试训成本 |
| 14845 | P | test-retest/措辞/roleplay比较揭示常规人格量具不稳定，评价instrument有效性边界 |
| 02846 | C | 政策SDT分析监管红黄绿期望cost，不是模型release/evaluation实际反证或新系统机制；补记已读AB，不计新候选 |
| 00302 | P | 时间特征构动态graph并与temporal变化保持一致，替代固定graph的表征边界；不采交通指标普遍保证 |
| 00307 | P | cross-time/variate分解及双轴gating，可接LLM-based forecasters，改变表征/计算选择而非仅预测榜分 |
| 00310 | C | R-learner利用prognostic/predictive side information估CATE，统计因果效应估计，未建立模型能力/系统机制新增联系 |
| 00382 | P | DQN至SDDE的Wasserstein-1逼近界和target delay稳定性条件，通用RL学习理论而非算法名称复述 |
| 00752 | P | static/dynamic template融合与按特征激活ViT层，质量/计算的动态执行路径，非仅夜间跟踪指标 |
| 00757 | P | Hailo只4D张量而3DConv需5D，编译tensor变换不改模型的执行兼容边界，非4D radar榜分 |
| 00586 | P | soft/hard地图双编码、agent type条件及control→kinematic轨迹参数化，生成表示/物理可行性的替代路径 |
| 03787 | C | MobileNet式depthwise轻CNN与SHAP/GradCAM的ECG应用，无新压缩机制或可比资源成立条件；不以医疗域关闭 |
| 00560 | P | sub-item embedding动态pruning safe-up-to-K精确不漏，替代全catalog算分与ANN近似的资源/有效性边界 |
| 00561 | C | QLSTM调QAOA组合问题量子电路，未给foundation模型学习或执行的机制联系；不是泛化所有优化为模型训练 |
| 00690 | P | 必要§3.3/§6已读：asset cache+GPU vectorized varied scene采样替代统一场景同步batch，scene数对照揭示训练多样性/运行时取舍；不采泛多GPU线性扩展 |
| 00490 | P | 多任务skill/preference/help查询以UFL有界近似和belief规划降低人类交互成本，改变单任务学习查询选择，不采普遍自动控制 |
| 00210 | C | 制造控制prediction/policy/quality/knowledge taxonomy及未来方向，未给新generative模型控制机制或实际失效证据 |
| 03790 | P | 必要§III-B3/IV-D-E后：constant-tail padding令均匀MSE下降却输出恒定，变化区间weight/MSE交替是局部纠正；window1预期被3/5反向。train+test评价合成/权重fit/单数据边界保留，不采augmentation普遍收益 |
| 00225 | C | v1必要ExperimentalSetup/LTT/Results已读：标准featureembedding+timePE+Transformer lastupdate及customer-asymmetric loss/CSI的局部应用，无新增可保留机制或条件。current重要纠错实际核完但属后事件，不能回授v1P；旧精度/CSI不采用 |
| 00171 | C | 完整AB：类别embedding+attention用于NMIBC预测/识别新临床factor，无新模型机制或评价有效性条件；非medical标签关闭 |
| 00339 | C | 完整AB：四研究综合/Bloom-SOLO/反馈/伦理三阶段的OneClickQuiz应用指引，无新执行或模型可靠性机制/实际安全反证；非education标签关闭 |
| 00668 | C | 完整AB：现成PPO用于booth placement及AQI/coverage/entropy领域指标，无新RL目标/优化或公平成立条件；非RL标签关闭 |

## 必要 core 的实际边界

- `00150/00156/00204/00240/00263/00472/00654/00749/01457`：Cicero原件与必要位置见 [SUP_INDEPENDENT_20261011.md](SUP_INDEPENDENT_20261011.md) §4；作者实际读其具名方法/关键对照或定点记录，未重读无关附录。00156参数边际/联合矛盾、00263模型记忆与recall注入对照、00150改错模态反侧均不删。00654 PDF仅思想实验必要段，HTML404不是C理由。
- `00624`：`SUP_FINE_SCOPE_CORE_20261011` §3/§4.1、TopK gradient式、域数据与pruning baseline；只判SAE数据选择及知识恢复机制，不以跨模型单榜分授独立因果。
- `00649`：`SUP_TASK_ARITH_CORE_20261011` §3、§5/Table3/§6；标准task-vector成熟，实际新增是alpha/IR知识边界，不采跨域无调参保证。
- `00679`：`SUP_REGISTER_CORE_20261011` §3、§5、§6；actual style copying/meaning drift对照改变双目标评价，不把prompt组合本身作突破。
- `00153`：`SUP_AUDOSIGHT_CORE_20261011` §3.3.2、§5.3-5.4、§6.2；Guardrail是成熟模块，安全保证未核。实际新增普通局部输出novelty/permanence过滤及输入降频latency代价，潜力仅限此，未读一般部署附录。
- Amplify：`SUP_AMPLIFY_HTML_20261011` exact2504.14105v1 §4、§6.1-6.5，及May2 Blog核心说明。已有专家招募/训练、去重、区域审核pipeline与field reflections，未做LLM安全盲区比较或验证新模型评价条件；May2说明未给相对此稿的具体新增设计/release内容。暂作者C，仅关闭本次博客新增贡献，不从dataset名关闭；交Cicero校准。

## 其他发现与恢复条件

1. `00509` ICLR2025 workshop、`00610` AAMAS25 extended abstract、`00580/00582`共同作者IJCAI标签：必要首稿身份/公开日只查指定文章或具名正式条目，不扫会议全站。当前无正式日证，不扩本窗或重复评分。
2. Gemini 2.5 Flash Preview安全card：May2辅助报道仅恢复官方原件URL `https://storage.googleapis.com/model-cards/documents/gemini-2.5-flash-preview.pdf`，该必要原件实际HTTP403。当前model-card目录为September26修订，不能代旧版；安全回归潜力保留，需原始card/明确公开自然日，不采用二手数字，不评分。
3. 所有P仅为逐ID潜力请求，未做family归并，因此不把身份数称当窗候选家族数，也不靠date未知删池。

## 最后有界查漏与准入修正

四组143发现中，先111份完整exact-v1 AB，再针对含糊的通用学习/运行时/生成题名补14份、current明确纠错00225补1份、独核要求的3个含糊应用题名补3份，共129；不是把全部宽命中变为逐项全文队列。`02846`已在先111原件中、前表漏记，此处补行不重复计读。`03790`由Cicero完成必要core，作者亦读实际原件题摘与§III-B3/IV-D-E。最终129身份为96 P/33 C，不是本窗确认家族数；Amplify另C。其余14个题名查漏为13明确范围外/1官方撤回，如下不声称已读AB。普通作者准入/core未读0。

补充必要位置：`00091` §III-B/C、IV-B；`00368` §III-IV（`SUP_HOLONIC_CORE_20261011`）；`00422` §3-5（`SUP_MEDDEVICE_CORE_20261011`）；`00551` §2.1.3/Fig3/§3.3（`SUP_R1_SURVEY_CORE_20261011`）；`00598`正文AB及§2（`SUP_GERM_IDENTITY_CORE_20261011`）；`00690` §3.3/§6（`SUP_URBANSIM_CORE_20261011`）；`00704` §4.1/4.3/5.3（Cicero原件）。这些是决定准入，不是完整Evidence；00150§5.3和00263§4.2/5.2/6亦已作者实际读到，不把空selector当阅读。`00174`current明确有Academic→Corporate纠错，作者取v2实际风险统计段（`SUP_GOVERNANCE_CORRECTION_CORE_20261011`），不授未发现任何勘误的总体断言。

Amplify必要core作者/Cicero均C：仅关闭May2博客增量，不用April18提交日期证明窗前公开，不把领域安全数据叫已验证模型盲区。

## 题名明确范围外的有限查漏

这14条只是主题宽词检索带来的查漏，13条明确非主线未进入贡献判断、1条已官方撤回；不以关键词或dataset名一键关闭。实际题名已读，current轻核另存逐ID原件；00225纠错与3个含糊题名已从本表移到完整AB表，未静默沿用题名关闭。

| 身份 | 题名语义范围/停止理由 |
| --- | --- |
| 2505.00359 | 官方v2于2026-05-06撤回，明确回指v1§6.4参数设置与§4.2 Skeleton Set不严谨；按官方撤回退出采用/评分链，不按普通范围C，日期无需另求 |
| 2505.00375 | delivery/pickup的配送时间估计 |
| 2505.00402 | logistics及时率的时空预测 |
| 2505.00755 | 足压/运动传感器的姿态估计，不是VLA或生成基础模型 |
| 2505.07832 | optimal power flow的环境设计，暂缓的领域科学应用 |
| 2505.00495 | tropical cyclone路径领域预测，AI for Science暂缓 |
| 2505.00526 | consumer search结构估计器预训练，统计经济结构估计非模型执行 |
| 2505.00530 | SMILES验证辅助drug design，AI for Science暂缓 |
| 2505.00625 | material property的graph/symbolic预测，AI for Science暂缓 |
| 2505.09630 | biological agent-based model的diffusion surrogate，AI for Science暂缓 |
| 2505.00173 | fuzzy逻辑识别medical image nerves，传统识别应用 |
| 2505.00316 | Cellular-Potts模型surrogate的UNet segmentation，AI for Science暂缓 |
| 2505.00462 | coral monitoring视频stitching，传统视觉领域工具非生成/模型系统 |
| 2505.00525 | Parkinson检测各模态方法综述，领域应用而非基础模型机制 |

## 必要公开日期/身份请求的边界

表中每个P只保留一次该精确ID first-public自然日请求；该请求是进入May2确定候选的必要门，不把May1 submission、May编号、正式会议日或搜索抓取时间当日证。恢复后仅重开此ID事件并做family去重、贡献校准、必要Evidence/Books，不重跑整月。

`00509`已定点核官方workshop同题poster与Apr28活动日期，但活动日不证明正文first-public，OpenReview QcmEb490bK forum challenge/API403；`00364` OpenReview KEUPk0wXXe同样API403。`00610`官方IFAAMAS p2405恢复同extended abstract，但May19-23会议/后正式发表不解决首稿日。`00467`2024具名workshop只有活动说明，不能把本稿推至2024。必要原件均在Cicero文件，不扫会议全站。

`00580/00582`具名IJCAI官方独立条目1021/560用于区分作者与题名/方法身份；正式版本不证明May2首稿日，仍不计确认家族。`00598`exact-v1 HTML已恢复题名/作者/正文AB一致的outlier稿；abs错误攻击摘要保留为metadata anomaly，不采用也不与正文拼接。未来只按正文实际机制重开其日期/后续Evidence。

尚未知日期的P及Gemini旧card原件缺口均不用于正面证据、Books或无遗漏断言；不是已通过Coverage/Evidence。

最后current轻核实际发现`00359`撤回和`00225`重要纠错，不能沿用“所有题名无signal”。00225作者/Cicero实际读v1 ExperimentalSetup（Sx2）、LTT（Sx3）、Results（Sx4.SSx1）及v2§III/V/VI/VIII：v1单行baseline对多历史LTT混杂；current承认cohort/评价失误，v2去cancelled/censored、lifetime改causal、backward/self-exclusion、CSI需error magnitude、cadence-matched/统一loss/grouped CV修正。作者原判v1成熟应用C，独核初把current反侧赋给旧稿而暂改P；事件拆分后双方撤销v1P，最终v1C/v2纠错P窗外。后修订不搬May2，旧数字不采用；v2具体first-public自然日未知，作为窗外后续修订恢复线索，只定点恢复该版本，不顺跑2026或整月。原件`SUP_OUTAGE_V1_CORE_20261011`/`SUP_OUTAGE_CORRECTION_CORE_20261011`保存。
