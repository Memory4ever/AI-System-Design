# Jan28：恢复后五项必要证据复核

复核者：root（非 Report 与 Books 作者）。原件为本目录 `supplement-core-<ID>-20261008.json` 的 exact-v1 HTML；以下仅认证注明的必要命题与反侧，不认证代码复现、整篇附录或日级完成。已有准入与分母不改。

## 2601.18698v1 — GAP

实际读 §3.1–3.2、§4、§5.1、§5.4–5.5：500 个 GLDv2 地标各选一张人工 canonical reference，GPT-5.1 据参考生成描述；Sora 2 每地标一个四秒竖视频，统一抽五帧。整体质量、参考匹配与人类/VLM 评分分责；所谓 Patch-CLIP 实际使用 DINOv2-Large，keypoint 聚合取五帧最大值，而 patch 与 judge 取平均，不能互换为整段时间一致性或模型内部知识。低相关不证明因果解耦。

必要反侧：50 地标短/长 prompt 比较只支持该样本的表达变化；区域 practical equivalence 的容差是 1.0 Likert 单位，不能签发全球公平。reference、matcher、采帧和 judge 都可能改变代理测量；硬件、精度、并发、SLO 与总成本未披露。停止于这套受限评价协议，不继续扩审所有地理数据或训练归因。拟仅报告：质量与事实支持分责已是现有评价主线，本项单模型地标代理尚不构成通用地理知识判据；作者仍须具体 owner 比较，不将“仅报告”当未读。

## 2601.18722v1 — SP3F

实际读 §2 的两阶段与 Eq2–4、§3、§4.3/Table3/Fig5：先翻译 question/CoT 做 SFT，再 DR.GRPO；只有 judge 看 English reference，student 看目标语言问题。答案、格式、≥70% language classifier 三个二值 reward 与 N 个 rollout 的 pairwise win-rate 分开；双输入顺序平均减少位置偏差，不认证无 bias、transitivity 或逐步真值。N=8 对比具有二次 judge 请求成本。

关键反侧：Table3 两者答案均正确的拼接项，privileged judge 77.16 低于非特权 81.08；两者答案均错的拼接项 59.90 对 46.53，仅是按答案正确组拼接出的 CoT/answer 检验，不是独立 step truth。Qwen2.5-7B、18 languages、1000 SFT/500 RL steps、每题八次平均不是 pass@8；1/8 数据比较未匹配 teacher 翻译、judge 或算力。hardware/precision/concurrency/SLO 未披露，不声称端到端降本。

Ch31「Teacher、future reward model 与反馈可信度」实际已有 teacher/reward version 与权限分责，但未承载 reference-only judge + batch ordinal feedback 与 objective verifier 分拆的这一接口。可补一个受限机制段，明确少样本冷启动、teacher 权限、pairwise 成本、循环偏好与 verifier 回退，不写普遍 judge 更准。必要 Source 支持这一最小范围；待作者拟文与 PRE/POST。

## 2601.18735v1 — Agora

实际读 §3.2 Eq4–5、§3.3 Algorithm1、§4.2–4.5 与 Appendix D.3 容量/成本定义。Eq4 收端仅增加 `(1−ξ_j)T`，而 Algorithm1 第11行加完整 `u_i[k]`、忽略 `amt` 后清空发送端；Eq5 与附录容量也不一致。

可复算直接反例：`u_i=1,u_j=0,c_i=1,c_j=2,ξ_j=.75,T=1` 且容量足够时，Eq4 预测成本差 −.5，按字面 Algorithm1 则成本从1变2。由此不能采用“每次交易成本下降、此算法局部最优”的中心保证；不是宣称所有 cost-aware routing 不可能。实验报告五 VLM pool，active expert 是 prompt/role 配置；API 定价与 A100 描述不足以恢复统一端到端计算合同，消融仍可作为作者受限观察，与中心证明分离。

中心争议终态隔离，不能复制冲突更新或保证进入 Books。重开材料：对应精确版本的纠正公式/算法与实现，明确真实转移、容量和计费规则；在此之前保留实验与反例，不以争议删除冻结候选。必要审阅到此停止，无需遍历无关附录。

## 2601.18760v1 — GCAI

实际读 §2–4、§5–6.6、Table6–8、§8/limitations：contextual preference justification 与 task-independent general values 是两种证据流。实际用了 HelpSteer2 与 PRISM 两个人群，不是同一群体联合意愿；GPT 生成/嵌入/聚类后摘要，contextual 按 preference prediction 排序，general 按 diversity/consensus proxy，K=10 各取五条并非投票批准。

关键反侧：whole constitution 的51人偏好与原则单独评分50人不是同一试验，不能把组合协同当已证明因果；Mistral7B 两流程 MMLU/BBQ 近似，100 ALERT prompts 的作者定性编码不认证部署安全。正文 §8.2 明确生成的是 candidate constitution、排序指标不是 stakeholder support，须讨论/ratification；两数据源与无完整组件消融限定归因。模型生成可能误解理由，聚类无法完美代表冲突观点。

Ch31「Human Feedback 不等于抽象 human values」实际 population/rubric 段已有一般边界，但未说明 contextual distribution 不会自动显露已满足或罕见风险原则，以及两流不同排序→候选→ratification 的具体责任。可补一个相邻段，保留 provenance、任务条件和批准权限、费用及直接征询/窄域原则回退，不赋予聚类民主合法性。必要 Source 支持该最小范围；待作者拟文与 PRE/POST。

## 2601.18790v1 — MortalMATH

实际读 §3–7 与 limitations：10 个 MATH level4 algebra ×5 urgency ×3 variants 共150文本情境；无 boxed answer 是 refusal proxy，math_verify 是答案正确指标，reasoning tokens 是 latency proxy，三者不是同一事实。原文明示 boxed 假阳性/阴性、人工 subset 数未披露、文本场景局限，以及不能因果归因 RLVR。

直接反侧：§5 的 Safety Sandwich 示例先 warning 后 math；因此整答 tokens/完成耗时不能证明 first-safe-message 被同样延迟。10–15秒叙述未绑定 deployment timing；hardware/precision/batch/concurrency/SLO 未披露，不用 token 数签发 time-to-help。仅观察任务坚持与安全优先的冲突，不推广所有 reasoning model 或真实医疗效果。

拟仅报告：受限诊断保留，不能用未经验证的 proxy 改写稳定安全结论；Ch66 release gate 已明确 safety hard constraint 与 quality/cost/latency 分责，作者须保留本项独有的 proxy 反侧。既有原则非本材料新增贡献，不能为造 diff 重写。必要审阅停止；无新增临床建议或实现能力断言。

## 2601.18699v1 — 遗忘机制的实验来源与中心争议

root 定点恢复读取本日 `supplement-core-18699-20261008.json` 的实际原文：§4.1/4.3 声称通过专有模型 API 微调并保留 checkpoint、optimizer 与 gradient；§4.5–4.8 又需要 head ablation、层激活、完整梯度、Hessian 及 checkpoint interpolation。论文未交代这些内部访问权限、具体 endpoint、模型 revision 和对应可审阅执行记录，不能从普通 API 输出反推可取得全部内部状态。§1/§2 采用六模型 109B–1.5T 声明，但 limitations 又称实验最高400B、尚未研究超过1T；这是正文内部的规模范围冲突，不把估算的专有参数量当厂商披露。

§Data/Code Availability 提供 GitHub `olaflaitinen/mechanistic-forgetting-analysis` 与 Hugging Face `olaflaitinen/ssr-continual-learning`。2026-10-08 本次具名重开前者为404，后者工具不可访问；分别是实际响应与访问限制，不能等同“从未存在”或据此指控伪造。正文提出的 gradient interference/CKA/curvature 是研究假说与作者声明；当前中心实验的身份、内部访问与数据支撑不可核实，整项保留为争议，不进入 Books，不采用相关系数、因果解释或跨专有模型普遍结论。

所需材料：精确实验模型/访问接口和内部状态取得协议、与其一致的训练/干预日志或可复查数据，以及统一后的实验规模范围；可接受作者公开的修订方法、实验附件或具体可核 artifact。材料到达只重开这些中心证据和依赖的命题，不继续无关全文、也不把中心材料缺失伪装成普通未读。当前必要审阅到此停止。

## 2601.18702v1 — 有理算术不等于无损语义与零幻觉

root 定点读取 `supplement-core-18702-20261008.json`：§4 Algorithm2 将有理状态先转浮点、经 Encoder/Decoder 再投射到固定有理 codebook；§4.5 的 RationalSoftmax 使用有限 Taylor 截断，且将缩放改为整数移位。§4.7/Appendix A 的位宽上界依赖每 K 步截断回固定 codebook，Appendix B 使用 logistic map/recursive matrix recall 与 Python Fraction；它们不是大模型事实问答、推理正确性或幻觉的受控评价。

中心反侧是原文自身的条件：固定有限 codebook 的投影对任意有理状态不可能全部单射，通常会改变状态；有理数可精确表示截断多项式的运算结果，却不等于精确原指数或原 softmax。定理先假设 `b_t=b_(t-1)+alpha` 再求有限间隔和，没有从任意复合注意/非线性运算推导固定 alpha；即便在该递推及 reset 假设下获得位宽界，也不能同时认证任意输入的零误差、无损语义、无限深推理或消除幻觉。不用算术表达精度给事实正确性签发证明。

当前争议终态：不进入 Books，不采用零误差/零幻觉/全深度 O(1) 的中心宣传。重开只需与实际投影/近似一致的修订定理与误差预算，明确适用输入及 codebook 条件，并提供可复查的对应实现与匹配任务/计算预算评价；新的窄命题可单独核验。支持与直接反侧已足够，不再遍历其他附录或全部硬件愿景。
