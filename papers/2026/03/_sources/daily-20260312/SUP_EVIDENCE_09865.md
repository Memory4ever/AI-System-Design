# 2603.09865 — GAST必要Source/PRE/实际POST通过

[exact-v1](https://arxiv.org/html/2603.09865v1)，题名GAST: Gradient-aligned Sparse Tuning of Large Language Models with Data-layer Selection。第二包完整题摘/current由root独立校准通过，潜力不由score倒推。current仅v1、comment空，未见现页撤回/纠错或具体先稿信号；不扩全版本/全网负面证明。

## 身份与公开日

SUP_EXACT_BATCH2.json保存exact-v1同题摘和原字段：Tue10Mar16:28:48UTC提交；官方no-advance最终ID/DOI与公告deadline规则给earliest Tue20EDT=Mar11BJT08下界；arxiv.content owning、findable DOI registered Mar11UTC02:23:46给已经可发现上界，两界同属03-11BJT。只夹证arxiv公开日，不把Submitted/Updated/registration单独当公开或伪造实际公告时刻；本页无具体更早稿信号。该单项日期待root原字段独核。

## 必要实际读取与命题

作者实际读exact-v1§3完整方法/理论/Eq1–11/Algorithm1、§4方法实验和Tables1–5、AppA.3两实现、B.2支持集合、B.3资源/Table6及B.4逐任务Table7直接反侧。恢复本轮再次完整读§3及A.3/B.2–4，不把取回或其他附录算审阅；不采用全部附录证明/实现。拟评分2+1+2=5（联合逐样本×逐层更新重要分支、单训练组件、可复用选择/资源约束），具体Ch30长期gap触发受影响内容深入，而非为Books提高分。

原静态target modules、单独筛选数据把同一batch各样本在各layer的作用合并。§3.2对每layer取support gradient，计算每sample adapter gradient与之inner product；批内mean/std标准化后softmax，stochastic选K个index，仅聚合这些index用于该layer更新。不同layer可选不同sample，基座冻结但其他forward/backward不自动省去。实际Eq9–11不是只保留全部正投影的hard filter，也不是每sample直接裁掉全模型layer。K_select默认8/训练batch16；支持小batch K_sup默认4，文中同符号须消歧。

§3称held-out support，但AppB.2明确默认整TRAINset为support，再每步小样本估计；这不是独立held-out质量验证。支持梯度只是当下proxy，支持集合身份、抽样/归一化、选择规则与adapter/优化器需一起验收（本书推断）。noise鲁棒文字不等controlled label-noise实验；不得把train-support下降签泛化保证。

## 中心理解边界：不采用逐步必优/全局最优

§3.1 Eq1的all-positive平均不由弱假设保证≥任意fixed data-subset平均：一个固定、非按alignment选出的子集仍可偶然包含很大的正投影和很小负投影，其平均高于all-positive平均。小反例投影[100,1,-1]，fixed subset[100,-1]：hybrid正均值50.5、subset49.5尚未反驳；把正集改为[100,1,1,-1]、fixed subset[100,-1]，hybrid34而subset49.5，正集合非空且负幅度不主导，同满足原三弱条件，但Eq1对data-selective失败。这是作者分析，待非作者独算，不让原宣称遮盖反侧。

Eq3还有L*eta²*E(norm(g)²)/2，较大一阶inner-product且仅各自norm“有界”不保证较大真实loss下降；Eq4最小loss结论不由该bound推出。Eq6/8把第一阶Taylor写成finite-step精确等式，省remainder，不认证任意非线性适配。实际stochastic softmax也未必排除负投影，因此theory D+与实际选择不同。只采用可核训练选择机制/有限对照，不采用最快逐步下降、普遍泛化/最优。

## 评价条件、直接反侧与费用

§4作者LLaMA7B/13B、GPT-J6B、Llama3-8B；八commonsense joint training/test，数学10k train、GSM8K/AQuA/MAWPS/SVAMP test。batch16/3epochs；LoRAr32/alpha64/dropout.05、Q/K/V/up/down；两adapter bottleneck256，LR1e-4/warmup100/ctx256；singleA10080GB，precision/训练seed/CI Not Disclosed。部分GPT-J/Llama基线取旧文Hu2023，不记全matched同run。

LoRA7B avg74.7→77.5、IST76.5，但BoolQ68.9→68.2；Llama3 IST84.6→84.8avg但PIQA88.3→87.4、OBQA86.6→85.0，平均不授所有任务提升。Table4 random76.4/TopK66.4/stochastic77.5，而AppTable7 random76.9（原字段冲突，不拼统一精确random数字）；TopK反退与support只proxy相容，不把“最大对齐”当必优策略。

AppA.3 compute-efficient缓存至少一层各Linear per-sample gradients，一次FW/BW聚合，额外gradient存储；memory-efficient第一轮算scores即释放，再第二轮FW/BW按index聚合，增加计算。CPUoffload/asynchronous aggregation仅潜在工程建议，本轮未核实现，不能授实际overlap。

Table6同14GB权重/batch16/80GB A100：LoRA43.4GB/10h，IST36.6GB/10h，GAST memory-efficient51.5GB/19h、compute-efficient66.9GB/11.5h。AppB.3 prose LoRA“7h”与Table6“10h”冲突，不采用精确加速ratio；两GAST成本均高于LoRA，memory-efficient亦非vanilla内存完全相同。这里支持质量/资源替代选择，不支持省PEFT参数即step更便宜或总加速。

## actual owner差额与逐字提案（未写Books）

作者读取当前ROADMAP及完整Books上下文，Ch30当前175–250完整局部、Ch29/31开篇/已读未变化交接。目标唯一owner `TRAIN-LORA`：[Ch30](../../../../books/part-04-training-system/30-lora.md)“Rank与target modules决定更新空间”，静态LayerLoRA placement段后、nominal/effective-rank段前。现195的CKA静态layer placement不能承载每步per-layer各自data-index聚合；235输入rankrouter及后续token gate改变部署执行不是同机制；336initial projected-gradient energy是静态选择。本项不重述这些既有分支。以下两段正式逐字供root Source/PRE，root独占共享写入，未授PRE/POST：

静态 placement 在任务与预算稳定时便于固定训练接口；若同一批样本在不同层产生不同更新方向，还可以选择“哪条样本梯度写入哪层”，而不先改变 rank 或部署时的 router。一个受限分支将每层 adapter 的逐样本梯度，与小支持批次的该层梯度作内积，再在批内归一化并随机选择部分样本，只聚合被选梯度更新这一层。各层因此可以消费不同样本，基座仍冻结，forward/backward 不会因更新稀疏自动消失。[必要机制](https://arxiv.org/html/2603.09865v1#S3.SS2)的支持集合默认来自训练集，不是独立验证集；对齐只是当前训练目标的 proxy，不能把一阶方向分数当成有限步必优或泛化证明。支持集合、抽样与选择规则应随 adapter 和训练配置保留，这是由该接口推得的验收要求。<!-- source-family:SF-2026-ARXIV-2603-09865 -->

这条选择支付逐样本梯度与支持梯度的费用：缓存再聚合可少做一轮反传，却增加梯度存储；先算分数并释放，再按选择重算则增加 forward/backward。[有限对照与直接反侧](https://arxiv.org/html/2603.09865v1#A2.SS3)中，两种实现的峰值内存和训练时间都高于普通 LoRA，确定性 Top-k 选择还明显差于随机选择，部分任务也退步。少更新一些样本—层对因而不等于免费加速，平均质量提高也不替代逐任务回归；更大梯度投影没有控制二阶项，不能发布最快下降保证。支持代理失配、样本噪声或资源预算不合算时，保留普通 LoRA、已验证静态 target modules 或单独的数据选择，不把本分支覆盖成统一稀疏训练规则。<!-- source-family:SF-2026-ARXIV-2603-09865 -->

拟本人末注（保留提案时态）：`SF-2026-ARXIV-2603-09865` — Daily2026-03-12补查；exact-v1§3/4/AppA.3/B.2–4，2+1+2=5，联合data×layer gradient aggregation与静态placement具体差额深入。train-support proxy不是独立泛化；Eq1/4/Taylor逐步必优中心不采用，stochastic与D+不同，TopK反退、单任务回归及两实现额外资源近正文。Table4/AppTable7 random与Table6/文字LoRA时长冲突，不采精确ratio/全matched；precision/seed/CI Not Disclosed，未核实现/复现。必要Source/逐字PRE待非作者实际核，root写后须非writer实际POST，不授DAY。

当前实际状态：root已经实际核本项原日期字段上下界、必要v1§3.1/3.2、§4.1–4.4及A.3/B.2–4，Source与上述逐字PRE通过并写入Ch30两段。非writer supplement_20260312实际顺读新197/199、181–252完整局部邻接及本人953末注，回对本轮原证，POST通过。root只调后nominal句为“无论采用哪种样本与层选择，nominal rank仍只是参数化上限”；静态CKA、因子几何/共享与部署router等旧分支未被覆盖。已通知root本人末注更新，作者不写共享章；不授DAY或复现。
