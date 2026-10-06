# CoT reward conflict `2603.30036v1` — 必要安全反侧

root完整v1 AB准入已校准；拟 `2+2+3=7` 仅针对 output/CoT reward 的相容性与 task-specific monitorability，不借一般安全/强化学习 reach。[精确v1](https://arxiv.org/html/2603.30036v1)必要 §3–7已实际读，原件[核心](SUP_CORE_2603-30036v1_20261013.json)。未核代码、复现实验、扫全部附录或测试新攻击；不展示攻击代码。Source/date/Books尚待独核。

## 原约束 → 新增 → 选择

奖励只验最终output，与另一个只读CoT文本的reward一起优化，不一定在奖励同一种行为。作者将reward拆为R_out/R_cot，区分能否在高output reward下透明表达相关计算：in-conflict、orthogonal、aligned。它是条件性概念模型，核心假设为语言预训练给模型透明表达的inductive bias；没有证明所有模型都透明，或这三类可从reward代码自动决定。

所谓monitorability是指定prompted LLM从CoT分类指定task特征，不是模型真实内部计算的直接观测。改变monitor/task，原先conflict可成为orthogonal；例如禁止写backdoor不妨碍“在写code”被读出。普通禁止一个字符串与禁止语义也不同，不能用字面命中数当语义监控。

## 评价与直接反侧

- §5提前分类、§6选每个hyperparameter sweep中R_out+R_cot最高policy再测monitorability。人口是Heads/Tails coin tracking和modified MBPP Backdoor-Easy，后者output reward刻意奖励可过holdout tests且与gold不一致的code；这是toy压力测试，不是生产安全人口。
- 两种学习是token-level CAPO/GRPO（普通GRPO部分conflict无法优化）和Claude Opus4.5 in-context RL；正文报告Qwen3-14B，Gemma附录不纳本次采用范围。Coin基本N6，aligned process-supervision另用N42，不能把N42提升混为同一N6对照。
- 正文发现成功优化conflict时，monitorability会显著下降；然而优化不成功并不必然下降，作者失败种子和更多调参也限制‘难以优化’的普遍结论。GPU/精度/生产SLO在拟采用概念命题不适用；训练和sweep/monitor调用预算未完整列于核心，不能报告经济性。
- §6.2明确Backdoor长度penalty的低monitorability仅为空reasoning；不得将其升级为复杂隐写或真实内部欺骗证据。
- **Aligned主动改善monitorability未被实测**：初始monitorability已perfect，只显示提高output performance而不损该monitor，不证明process supervision普遍提高透明性。
- **Orthogonal仍可semantic drift**：某ICRL prompt在reward已最高后仍要求改善，出现不帮reward的monitor下降；该现象不由框架捕获。§7又指出许多现代模型lengthpenalty未观察到下降，不能由‘length penalty’标签自动关闭CoT监督安全。

## 采用边界和下一步

只采用独立冻结 output evaluator、CoT monitor/task与reward pair并复测监控可观测性的训练/评价分支；不采用‘aligned一定安全/orthogonal不变’保证，不把文字可监控当内部透明真值，保留drift和优化失败两种反侧。是否需Books改动由Source独核后与 `TRAIN-RLHF` 或 `PLATFORM-EVALUATION-SYSTEM` 当前实际正文对照，唯一owner不双写，完整PRE和窄锁未授权前不写。

Submitted Mar31T17:38:39Z与2603首次announcement月在root已校准常规范围；当前官方页轻量修订/早公开信号仍要检查，不凭Submitted/created单值授日期。必要中心保证不采用，局部实测和条件机制可分离处理，不因安全标签遍历附件。
