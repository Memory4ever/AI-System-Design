# 12 日 API 恢复后的定点筛选

2026-10-06T13:41:05+08:00，作者Bacon。原429保留；本次实际`arxiv-recovered-1345.raw`200/374412 bytes，请求与20秒/3MB上限在同名request.json。12分类和模型/Transformer/MoE/Agent/diffusion/GPU/vision-language/world-model主题，submittedDate=[202509101800,202509111800]，start0/max200升序，153/153停止。

153标题实际读完；与原24不同的87项相关/含糊标题已读完整题摘，原文与精确当前版本在`recovery-scoped-abstracts.json`。52当前v1、35后续v2～v5，后续版本不能倒填2025证据。以下60项作者潜力/27建议关闭，与原24合并111唯一家族题摘=83潜力/28建议关闭；查询另46条是明确领域应用标题范围关闭，未声称读摘要。原518月邻段不成为分母/全文队列。原24四项未被此次查询返回，仍保留。

全部潜力尚缺完全落窗首次正文公开证据，API published/submitted、月份ID、后续updated不授日期；正式本窗候选仍0，不评分、不进Books。当前题摘不是核心方法/实现/复现。

## 60 项潜力的具体增量

下列ID均加前缀2509；当前版本见JSON，不能默认为v1。

| ID | 原约束→题摘实际增量→可能改变的选择 |
| --- | --- |
| 08897 | 图文/跨层信息丢失→recurrent gating融合→统一multimodal检索 |
| 09737 | world conditional难控制→random-access AR/结构抽取/新token再训练→条件化预测；因果主张待证 |
| 08908 | 跨域动作不稳→diffusion timestep语义/像素取舍→特征选择 |
| 08910 | PromptGuard伤害预防与理论界主张→真实威胁模型/控制保证待核；安全争议不普通排除 |
| 08940 | T2I平均分掩盖输入差异→进化搜索属性/prompt偏差→模型比较 |
| 08959 | 小数据global attention失local bias→CoSwin融合→局部/全局选择，不因规模关闭 |
| 09009 | 跨数据/规模比较混杂→同compute轴reference runs→训练比较 |
| 09013 | VLM visual math失败→counting/识别组合/符号复杂度分解→评价归因 |
| 09043 | willingness与abuse分类混同→信号分离/格式交互→诊断；不推主观意愿 |
| 09071 | aggregate parity→同条件bargaining程序差异→Agent评价反证 |
| 14252 | input重建目标→JEPA embedding预测→LM训练目标替代 |
| 09118 | 噪声图文token→gradient-attention mask→alignment训练 |
| 09121 | ecommerce MoE资源→大专家/节点内EP、token OT偏好→专家/目标取舍，须核v1 |
| 09135 | 不规则时间value不稳→HJB gradient iteration→连续RL条件，主线桥待核 |
| 09742 | 不传原video仍泄漏→gradient inversion/参考帧/extractor条件→隐私边界 |
| 14253 | soft prompt单任务→shared/private learned组合→受控跨任务迁移 |
| 09168 | 固定token合并→层Pareto/信道适配→质量/资源选择 |
| 09172 | 理想检测评价→sharing/redigitization及人类反侧→真实检测边界 |
| 09192 | defect准确率→diff极性counterfactual稳定→表面cue负面证据 |
| 09194 | LLM代码错误→scenario events与属性验证→局部可靠性接口，不授通用保证 |
| 09208 | constraint附近训练不稳→提前渐增penalty/误差界→安全RL优化，非硬安全 |
| 09215 | Agent追责→trace/arbitration/reputation分层→保留风险主张，真实控制/信任界待核 |
| 10569 | watermark协议不齐→detectability/robustness/quality统一评价→安全评价；toolkit名非贡献 |
| 09263 | 长video隐含时间丢失→timestamp token/时间正则采样→DATE时间表示 |
| 09286 | code-only复杂chart失败→双reward选择code/direct→条件化推理路径 |
| 14254 | hallucination probe跨域退化→动态层加权/freeze反侧→可靠性评价 |
| 09311 | language/vision-only分类互补→类别精度融合与改标对照→模态使用条件 |
| 09321 | task数量≠难度→leaderboard dispersion/format/constraint→Agent benchmark校准 |
| 09332 | 2D/硬3D与机器人约束→3D gated fusion/embodiment-aware→可执行规划 |
| 09356 | 常查询VLM成本→query显式action→学习何时请求外部指导 |
| 18127 | SAE低频safety feature难解释→预选择/segment simulation→解释成本；安全界待核 |
| 09387 | HPO试错昂贵→history/SHAP zero-shot建议→成本比较，med实验不普适 |
| 10572 | 生成规则/代码可靠性→RAG/guardrail主张→风险潜力，需核新保证 |
| 09488 | prompt盗取未知seed→CPU seed范围漏洞/seed恢复→真实白盒/算力/修复约束待核 |
| 09498 | memory噪声→replay admission/utility consolidation→写入/整理策略，当前v3非2025实现 |
| 09505 | agent context memory wall→flattened array/非对称量化/FA→HW选择，模拟非实机 |
| 09524 | 单label忽略annotator→specific预测聚合soft labels→训练/评价边界 |
| 09525 | sandbox重建→OS memory templates/CXL/RDMA、浏览器共享→运行时成本，v1 Agent段待核 |
| 09541 | composition classical局限→quantum表示/CLIP正负对照→表示替代，主线桥待核 |
| 09547 | video DiT feature弱→encoder辨别/时间一致性选择与alignment→训练目标 |
| 09550 | codec序列唯一/bit敏感→FSQ冗余、encoder distill反侧→表示/传输条件 |
| 09560 | 串行低频→perception/generation异步分解与public context→staleness/吞吐取舍 |
| 09593 | emotion类别≠context self-report→细粒度失配反侧→局部评价盲区，不作医疗采用 |
| 09594 | image-relative控制绑姿态→object-relative costmap解耦→跨embodiment控制 |
| 09595 | 长avatar语义/细节冲突→blueprint与parallel first/last subclips→生成分解 |
| 09754 | heuristic KV budget→residual loss/head/layer动态预算→generation/extraction选择 |
| 09614 | 短代码bench→跨文件长context评价/退化→LoCoBench盲区，label质量待核 |
| 09629 | planner/grounder独立微调gap→交替joint alignment→协作训练，单调界假设待核 |
| 09631 | TTS串行/continuous目标→discrete flow factorized prosody/acoustic→采样路径 |
| 09650 | 算术token计算不明→mean ablation/attention routing last-token subgraph→条件化解释 |
| 09658 | accuracy不测拒绝→false-option rejection→abstention评价，非普适谦逊 |
| 09660 | MoE专家行为→paired activation与test-time deactivation→安全反证，白盒权限待核 |
| 09667 | motion prior欧氏结构→pose/velocity/acceleration几何field→生成表示 |
| 09671 | MoCap噪声/retarget串行误差→soft scopes联合track/retarget→控制学习 |
| 09672 | locality归因架构→linear denoiser/data统计反侧→diffusion解释 |
| 09675 | RLVR entropy collapse→actor perplexity/critic variance bonuses→探索，不授variance保证 |
| 09674 | VLA监督昂贵→trajectory/parallel rendering/loss、pushcut探索→RL训练分支 |
| 09677 | 短task饱和→给plan隔离execution/self-conditioning→长程执行评价 |
| 09679 | 固定rotation无法适配outlier→learnable Givens butterfly→量化校准 |
| 09680 | T2I平均alignment掩盖长prompt→分轨reasoning评价→数据/bench设计，混杂待核 |

## 27 项完整题摘后的建议关闭

| ID | 具体理由 |
| --- | --- |
| 08911 | matrix LEA/量子应用未建立模型学习或系统具体桥；不是因理论关闭 |
| 08920 | contextual embedding用于文档心理测量factor分析应用 |
| 08947 | camera/display测量pipeline，无当前模型机制 |
| 08960 | 葡语谚语数据资源，未建立新评价混杂/机制证据 |
| 08970 | global constraint分工/assembler，初实验未建立新增执行/一致性或失效边界 |
| 2510.15899 | 既有两阶段LLM Verilog正确性/PPA应用，未建立新机制/验证条件，月份编号不授日期 |
| 09066 | few-shot用于cold-start推荐，未建立新因果/预算/语义机制 |
| 09082 | 多视角RL信息抽取只述提高指标，未建立与既有训练差额；root可核含糊方法 |
| 09101 | Bangla代码数据/model/Pass@1，未建立数据设计新边界，不因小模型 |
| 09131 | BGE/Blockwise与hard negatives越语适配，未建立新资源/失败条件 |
| 09140 | Betti拓扑预测专用研究，无主线具体桥 |
| 09146 | ML选择ISP peering，不是LLM通信runtime |
| 09151 | dataset/bias/architecture观点归纳，未给新修正证据，不排斥所有综述 |
| 09152 | brain fMRI encoding library，AIS暂缓 |
| 09154 | 六模块空间框架/路线，未建立已验证新机制或边界 |
| 09198 | 灵长动物vocal/脑活动研究，AIS暂缓 |
| 09200 | 专用human trajectory refinement，未建立foundation/world/action-conditioned模型桥 |
| 09210 | 自动驾驶motion forecasting动态图，未建立当前模型主线桥 |
| 09219 | RDDL事实图传统RL政策，未建立foundation/LLM系统桥 |
| 25200 | LLM empathy cue HRI应用，未建立模型机制/控制边界 |
| 09226 | 教育QA模拟distillation，未给新蒸馏机制或条件 |
| 09234 | 既有SQL/example/verify/refine与领域accuracy，未建立新状态/反馈保证 |
| 09272 | 三KG工具QA比较，未给足以修正解释的控制/混杂证据 |
| 09470 | 文献地域筛选→RPA提交，未建立新权限/一致性机制 |
| 09574 | selfish human探索信息分享博弈，未建立当前模型/系统桥 |
| 09597 | generic图对齐spectral/map，无当前foundation/system具体桥 |
| 09613 | robot形变机械/animacy问卷，无AI机制 |

root首批建议核09737/14252/09560/09754/09679/09672机制及有限适用边界，普通08970/09082/09234与原09292；安全08910/09742/09172/09488/09660不按普通关闭。必要原文未读就明示，不授复现或保证。恢复原公开区间后，定点核精确v1与准入/核心方法/反侧，再作实际Books owner，不无限追查库存。
