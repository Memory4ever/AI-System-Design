# Apr22 四项有限非作者处置核验

复核者 apr01；非本日报作者。实际重新打开四项官方 HTML v1 的必要定义、打印规则与关键反证，并读取正式 README 对应行及 Ch66 聚合/有限样本的实际正文。未核日期/全日来源，不复现实验，不改报告/Books，不扩全部附件。所请求“四争议”实际现稿为两 Only、两窄争议，以下分别判定，不机械统一标签。

## [2604.19071v1 HoWToBench](https://arxiv.org/html/2604.19071v1)

实际读取 §3.1–3.3、§4.6、§5/Table3、§6.2/Table7。5 标准 Only 通过，**不需要改全家族争议**：按 instruction 预定权重、leaf 分责和隐式聚合是不同测量对象；50 样本的段落删减/重复/genre 转换给有限仪器反证，非写作真值或长度的因果证明。Ch66「Per-verifier Outcome 与 Aggregation Rule 都属于 Evaluation Identity」已讲明 typed outcomes、聚合函数/权重/revision 的责任，但不声称本文全部算法已有。

需要作者轻量纠正：Table7 的 Auto-planning 在 Drop=-.06、Rep=-.30，反升发生在 genre 转换 .08/.04/.20/.82；不能写成 Drop/Repeat 本身都让该方法反升。此外 §4.6 明确 137/1302 原人类参考被专家选择的 LLM 响应替换，不把参考统一称纯人工。保局部受控结果与选择边界即可，不因这些有限边界否定所有相关性。

## [2604.19162v1 SHADE](https://arxiv.org/html/2604.19162v1)

实际读取 §4 Eq1–6、§5.1–5.3/Table3。5 标准 Only 通过，不采用真实完整 alphabet/Shannon 保证：Eq5 文字说 subtract、打印加项；`sum p*=k_obs/estimated_support` 通常不等 1，因此该打印读出只能按 proxy 分数解释。N100 是有限采样 reference，不是完整支持 oracle。作者自己的 Table3/正文明确 n8/10 简单 proxy 的 mean AUC 可更高，MAE 与检测排序不能互代。

这是有限 QA 的支持估计与经验检测，不是被证明精确的概率恢复；本研究也没有给普遍准确的开放风险保证。保留这些窄算法/比较范围与采样、NLI、spectral 成本即可；不为局部公式口径问题机械将所有经验隔离或强写 Books。

## [2604.19398v1 GRASPrune](https://arxiv.org/html/2604.19398v1)

实际读取 §3.1–3.2 Eq1–5/Project 与 nonempty guard。6 纠错深入、窄争议通过：先按 p 排序取 cost≤B 的 prefix，再给空 group 最高 p 单元置 1，却没有扣回预算/重投影。A 有两单元、B 一单元、cost 都为 1、budget=2、scores=.9/.8/.1，prefix 成本 2 后补 B 成本 3；A 一个+B 一个的可行解确存在。只否定打印组合的无条件每步可行性，不证明代码没有另作处理。

parameter-footprint proxy 不等 latency/KV runtime cap，STE 也不等离散最优。实测成本、有限质量与反向结果仍可报告。重开需要 protected-group 预算预留、扣款/再投影或真实每步 mask-cost 依据，不靠更多平均指标替代。

## [2604.18842v1 Global Expert Mapping](https://arxiv.org/html/2604.18842v1)

实际读取 III-B/Eq4–9、Algorithms1–2。6 纠错深入、窄争议通过，但现稿反例应改为符合正文 `m>n` 的实例：取 m=3、n=2、c=(2,2)，w 三行为 (1,0)、(1,0)、(0,1)。唯一 LP 最优相应三项都是 1，满足全部 assignment/capacity。L=ceil(log2 3)=2 时 Algorithm1 的打印 floor/mod 小数位对 x*=1 全为 0；所有候选为空，返回全零而 OPT=3，任意 ε<1 的 Eq6 不成立。

此修正避开原 m=n=2 与 III-B scope 的额外争论。Algorithm2 的 fallback 是另一打印流程，不能反向证明 Algorithm1 的完整 assignment/近最优桥。只隔离这组保证，不断言已运行代码同错、静态 domain map 无价值或全部实验无效。重开需明确 endpoint=1 的处理、实际算法和相应证明。

## 结果

2 标准 Only、2 窄争议的实际处置均支持；需作者同步 HoWToBench 扰动方向和 GEM 的有效域反例。以上不是 Apr22 日期/来源/整日 Gate，没有实际 Books 写入。
