# 第二包：两具体已有覆盖提案与一整体PRE（均待reader）

## 11938 FlexPipe / 2+2+2=6 / INFER-DYNAMO 已有覆盖提案

实际exact-v1完整题摘、§3.2–3.3/§5/§6.1–6.3/Alg1/§7–9.6必要（9.2中段输出截断不算完整，非采用必须域）。负载CV/queue选择stage数与batch粒度，旧pipeline继续服务期间异步同步token-valid KV再更新路由，CPU参数副本与host亲和缩短再装载。只采用运行中重配置需要KV/权重/新路由身份及临时费用，不采用原“无中断”或完整一致性证明：mask乘合并未闭合并发write/frontier/cutover。Alg1的nu是到达强度导数、正文为arrival interval CV，不拼可执行recipe。Eq1排队表达维度/稳定性前提不足，亦不以它保证最优stage。42server/82GPU/100Gbps/Azure trace与Splitwise，precision、完整input/output、并发/SLO协议未闭；WHISPER-9B/BERT-21B身份及12000 requests与requests/s不合，20QPS两小时也不能直接拼headline，故不采倍率/生产安全。

实际owner Ch52“Failure与正确性”“有计划重配置”和“Live PP 重配置先验收临时状态，再提交新布局”完整现文已读：已有current∪target双驻留容量、dirty slot增量迁移、最后尾写同步/原子提交和退路，明确target由profile选择而不保证最优；Ch56“何时值得重算”段另承载求解/迁移/旧计划服务成本，不能把CV选数宣传作新正确性。拟采用的最小接口已被实际论证承载，不增加段/marker/注；不是所有FlexPipe机制已证明，核心性能/正确性未采用。请reader核该具体NC，不第三Methods。

## 12044 Hierarchical Alignment / 2+1+2=5 / TRAIN-LORA 已有覆盖提案

actual exact-v1 §3–4、AppendixA表3及C必要：按三分depth在attention上选择LoRA mask，hh-rlhf DPO，同DeepSeek-R1比较；Local/Mid/Global与full更新面不同。功能映射只hypothesis，不由层位证明语法/logic/factuality唯一位置。v1没有当前后版摘要中的exact参数匹配/3seed slidingwindow/人评，不倒填；AppendixA Llama Local coherence −.08、factuality −.01，Mid coherence −.06，与“全部避tax”宣传不一致；原约996/998/997人口亦分别保留。只保placement/rank/更新support及目标/原能力需分验，不采全局层角色、精确预算优势或因果胜出；GPU/precision/完整token预算Not Disclosed。

actual Ch30:初始化继承后“同时改变低秩参数化、更新支集与基座冻结，需classifier-only、浅层adapter和逐步解冻控制”与紧邻source2603.27707五seed/预算/每任务回归、后续2510.08564 trainable mask/target与retain双验三完整段，已明确承载本次有限采用。改变三段depth是该更新support的一个实例，未有新成立条件可脱离该论证；拟具体已有覆盖，不改正文/末注。请reader核，不用“已读完”替NC依据。

## 12071 Stagewise Data Attribution / 3+1+3=7 / TRAIN-DATA 整体PRE提案

actual exact-v1 §2.2–2.3/Eq1–2的局部posterior敏感度/两phase全协方差分解、§3两层线性toy/LOO与time-ablation相关、§4 Pythia结构token组/5限制、AppendixB估计/归一/独立梯度与covariance数据角色/C2–C5必要。Local RMSProp-SGLD与localization定义checkpoint附近分布，LM实际改用Pearson而非原cov，token多类/不穷尽且排除same-token。Pythia相关曲线不证明SGD精确Bayesian动力学或唯一电路因果；toy选择与LOO相关最高的hyperparam，不能称完全独立盲验。Alg1正cov return与定义负cov符号差不补统一recipe。对同item不同训练阶段可异号/峰值的有限证据足以改变终点固定“好/坏数据”判断；不采用普遍最优课程、部署数据排序或免费计算。多checkpoint/SGLD/样本loss矩阵/重训对照均计费；未核代码/复现。

唯一Ch27已有动态选样/gradient/validation反馈，但没有明确把**训练数据的影响归因对象**绑定checkpoint、局部抽样分布和目标observable，或区分LOO干预与posterior局部敏感度。actual Ch27:210–218完整controller/独立Evaluation与下一当前通过率/gradient选择段，及Ch26/28交接已读。

精确位置：Ch27原完整五行controller段之后（末行“side-effect policy；否则 privileged structural teacher 编译出的 screenshot-only 行为会失去关键 lineage。”），原“训练题的当前通过率还不能代理它对目标任务的更新价值”段之前。两侧不改。

正文：

给数据分配贡献时，还须先固定“对哪个模型阶段、哪个目标量的影响”。同一样本的终点排序可以掩盖训练中途的异号或峰值；一条[受限阶段归因分支](https://arxiv.org/html/2510.12071v1)在各checkpoint附近抽样参数，以样本loss与目标observable的负协方差估局部posterior敏感度，再分别用toy重训干预和语言模型token组轨迹核其变化。局部敏感度不是该样本在真实SGD历史中的完整因果贡献，LM中的Pearson归一读数也不能无条件沿用原covariance量纲或与删样本重训互换；Bayesian近似到非平衡SGD仍有缺口，相关曲线不认证唯一内部电路或最优课程。应保存checkpoint、局部抽样/归一规则、样本与query人口及observable，不将某一时刻的好坏标签永久写回corpus。多快照采样、loss矩阵和重训对照全费；估计、支持或干预效果不可靠时保留原mixture与独立目标回归，不由归因峰值直接批准在线改训练分布。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12071 -->`

本人末注：

- `SF-2025-ARXIV-2510-12071` — Herschel，Daily2025-10-16补Oct15；[exact-v1](https://arxiv.org/html/2510.12071v1) §2.2–5/B/C2–C5必要，3+1+3=7。仅checkpoint-conditioned局部敏感度与LOO/SGD因果分责；保Pearson/cov尺度、toy选参、非平衡理论缺口与算法符号未闭/全费，不采最优课程或直接改corpus。未核代码/复现；整体PRE、真实SAVE/完整自读与sole actualPOST仅据本日canonical实际后到层。
