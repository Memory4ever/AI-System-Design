# 已发现 QUERY 的有限收束：7 家族

本窗原始 Submitted 均在 2026-01-27T19:00Z～01-28T19:00Z；官方通常公告最早下界 Jan29T01Z，DOI Created 是已可访问上界，不是首公开时刻。原值见 V3_DATE_RAW_FIELDS.json。以下必要方法/评价由作者实际定点读，root实际core准入校准及全包必要命题/反侧复核通过；PURGE中心争议终态不作正面Evidence或Books，其余Only。不声称代码/复现，最终日级另见本日README。

## [MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization](https://arxiv.org/html/2601.20577v1)

2+1+2=5，标准。原同形任务不能直接重放轨迹→§4.2/4.3 定义相同任务/机器人/依赖结构下，低 overlap 区域内几何变换和高 overlap reusable segment ratio→必须先判断 motion reuse 条件，再复用高层计划或局部轨迹。物理原文186–224，评价263–294、377–398；直接反侧 Appendix D/E 953–985。概率乘法 Eq4 未明确独立/逐单位恒定失败率，不能采用为 success lower bound。

DeepSeek-V3、24-core i9-14900HX、MuJoCo MeCoBench六类多臂任务，S1随机/S2相似/S3不同，每task30随机seed；报告成功/规划时间/token。Pack Grocery cache>30 后 search 耗时反弹，S3规划时间约增6%；直接复用旧轨迹的消融近零成功、移除相似过滤某些低-overlap高度相似任务不退步。最大cache40/30/700/50/9/9按task调，阈值手调；截尾标准差忽略>5σ outlier，不能据此授尾延时。这里只支持模拟、已知几何/依赖、黑盒LLM规划；非一般语义cache、真实机器人安全或异构导航保证。OnlyReport：新增可采用的是该任务族的reuse定义和反侧；区域/轨迹结构依赖及人工阈值未形成可移植 foundation/VLA 机制，不将经典cache原则当书稿缺口。

## [SAPO: Self-Adaptive Process Optimization Makes Small Reasoners Stronger](https://arxiv.org/html/2601.20312v1)

2+1+2=5，标准。PRM评分与reasoner分布失配→score-gap预测位置后仅核相邻两rollout并迭代同步verifier→局部纠错/预算接口。实际108–131 Eq8–13、346–383 实验及反侧。Eq9是 c_j−c_(j−1) 却argmax作first error，case(b)/(c)预测与真t不等方向及重复端点有逻辑/符号疑点；不证明实现错误，亦不宣称首错定位必然正确。

Qwen2.5-0.5B/Llama3.2-1B full FT、Gemma2-2B QLoRA，2×RTX3090；GSM8K/MBPP训练、MATH/HumanEval OOD；GSM_Process3786/MBPP_Process1499是GPT4o首错标签筛选而非数学oracle。CoT/SFT/RFT/RFT+DPO/RPO/SFT+GRPO与ORM/Omega/Shepherd对照，验证效率仅0.5B单3090的FLOPs/elapsed含代码compile；Qwen GRPO math最好与小模型/代码较差反侧保留。未披露多training-seed或全部预算严格匹配。OnlyReport：采用局部score-gap→邻接核验诊断，公式歧义和proxy首错标签限制尚不足提供可复用的正确性/最小成本合同；不以成熟PRM/RL原则扩书。

## [Reinforcement Unlearning via Group Relative Policy Optimization](https://arxiv.org/html/2601.20568v1)

2+2+2=6，因明确 formal/security contraction claim 加深受影响推导。原 forbidden-mention reward→作者Theorem1采样mixing下点态收缩→若成立会改变unlearning验收。实际Eq13/16/17、Assumption1、Appendix A.2 Eq33–37 已读且 root 定点实核。全零reward组归一advantage为0；policy=reference时KL梯度也0，PPO clip不强制每个forbidden sequence (1−ηε) 收缩。不能从clipping或effective mixing叙述推出该必然收缩；不是用证明错排除潜在贡献。

终态争议/暂缓、NoBooks：词集合泄露proxy不等参数知识删除；中心保证不得正面采用，亦不借局部禁词输出下降给安全背书。重开只需作者补全与实际GRPO更新匹配的条件、修正定理/证明或反例回应，或可独立支持更窄命题的正式勘误；不继续泛读其他附录/旧版。评分不因争议降分。

## [CE-RM: A Pointwise Generative Reward Model Optimized via Two-Stage Rollout and Unified Criteria](https://arxiv.org/html/2601.20327v1)

2+1+2=5，标准。各response自拟rubric可不一致→query-only共享criteria与criteria/chosen/rejected三条件adv分组→评分条件身份需保留。92–114 Eq1–3及controlled Qwen3-Max统一/各自/隐式criteria；379–410 Eq8–10和训练；562–577 RL实践/直接限制。不是把benchmark≠RL成熟结论算新增。

Qwen3-4B-Instruct-2507，SFT batch64/lr1e-5/3epoch，RLmini64/4mini/step lr2e-6 KL1e-3，4criteria+16evaluation=20trajectory/instance，temp0推理；硬件/多seed Not Disclosed。RewardBench/2、RM-Bench等与Qwen3-8B Tulu3随机50k、250steps GRPO8 on-policy ArenaHard judge比较，与32B Compass、无统一criteria、4×test-time scaling分列，不能把预算不同数字合并。Pointwise absolute calibration仍缺anchor，tools在math/code/facts有益却使general chat下降。OnlyReport：采用此模型/协议局部接口和对照，不授共享rubric生成正确、跨prompt cardinal score真值或通用RL最优。

## [Memory Retrieval in Transformers: Insights from the Encoding Specificity Principle](https://arxiv.org/html/2601.20282v1)

2+1+2=5，标准。词与recall相关不足定位使用→匹配数量随机token的K perturbation反侧→可区分targeted cue影响与普通破坏。100–138方法；138–171结果/限制已实际读。Counterfact等token长度prompt Q/K/V swapping仅input、首token后恢复，first-word exact match/Δlogit/PPL；Gutenberg input512/output40/step30只取原模型ROUGE-L Recall=1，集合随model变化，是选择后memorization slice。

GPT4o anchor与K投影/LXT keyword各20，targeted perturb随机token数量匹配；Llama2-7/13B、NeoX20B heads2/3/4，Llama3.1/Qwen2.5/Phi4 heads1/2/2，OLMo全部heads/layers是不同干预预算；首head排除heuristic。硬件/多seed Not Disclosed。ROUGE/BERTScore下降同时PPL/repetition/MAUVE质量退化，Llama2 random可能同样下降，非所有模型selective；同一sample选择/keywords/head选择限制generalization。K置0只令对应dot-product=0，不使softmax权重0，不等完全不能attend，更不等权重知识删除。OnlyReport：采用有限cue干预负侧，非把生成损伤升级为存储位置/因果knowledge deletion保证。

## [Spark: Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning](https://arxiv.org/html/2601.20209v1)

2+1+2=5，标准。uniform rollout浪费局部步预算→policy生成<explore>触发forest分叉、active-leaf N封顶→信号与预算执行接口分开。128–187 Eq3–7；228–247、499–530及1051–1057必要评价/配置；626–630直接能力限制。标签是policy proxy，不是已校准epistemic uncertainty。

Qwen2.5-1.5/7B instruct、ALFWorld/ScienceWorld/WebShop（仅环境Agent机制非AI-for-Science领域研究），KimiK2每环境300 coldstart SFT轨迹（10%real、90%gold-path retroannotation），120RLsteps batch16 N8/M4/B2；4×A10080G、temp.4、512response、30steps、history5、prompt2k/4k/6k、actorlr1e-6 KL.01，evalbatch128/seed0。同N8 GRPO比较局部prefix共享token6.9/47/11.2%减少，非同训练总算力/E2E latency结论；closed-source成绩不同训练/模型条件不作可比优越。低能力policy未emit有效tag会漏探索，未多training-seed或开放环境校准。OnlyReport：操作性tag/预算可用但此数据、环境及能力条件内，无真不确定性或普遍search-quality保证。

## [Trajectory2Task: Training Robust Tool-Calling Agents with Synthesized Yet Verifiable Data for Complex User Intents](https://arxiv.org/html/2601.20144v1)

2+1+2=5，标准。最终DB outcome可遮蔽中途forbidden动作/intent改动→动态intent与forbidden action evaluation接口→任务验证不只最终成功。140–206、457–481原core已获root准入；361–393与455–489必要评价/限制实际读。不是POMDP+SFT pipeline本身准入。

Tau2-Bench Retail-3I生成1099复杂任务，Ambiguous/Changing/Infeasible与General控制；七模型，各task3独立模拟trial报告Pass^k不是pass@k（要求全k成功），Qwen3-4/8B用2872trajectory 3epoch Adamlr1e-5 β.9/.95，hardware/多training-seed Not Disclosed。最终无害工具拒绝仍可记录issued forbidden call，不推成功hack或真实副作用；SFT零shotAirline小幅转移不是全域泛化，用户模拟LLM非人类日志/稳定population。OnlyReport：该合成任务接口支持有限诊断，不新增可部署policy安全保证；未验收实tool ecosystem与真人分布。

FPL20224实际59–89 CLIP classprototype ridge+blend纯局部adapter/metric组合、没有新的选择有效性条件，root EX通过；MemCtrl20831/CiMRAG20041/SEER20305的最小core EX沿原校准复用，保留所读证据，不能由shared-space断言升级realizability。以上排除不计7家族候选。
