# 本日第四批有限核心与准入判断

root复核入口：15173本节完整核心/反侧，15307本节具体ablation与声学共现解释，15274本节决定scope的传统hardwired应用EX；不要由潜在评分倒推准入。

日期采用各自原始身份的 [DataCite字段](V3_DATACITE_DATE_BOUNDS.json) 和官方 announcement 下界共同限定；日期成立不代替准入。当前版本摘要仅作发现，下列原文均为精确 v1。尚无 Books 写锁或独立源验收。

## 2602.15173v1 — 潜在准入 2+1+2=5，标准必要证据完成

[精确v1](https://arxiv.org/html/2602.15173v1) §2–8、AppendixC.4 实际读。原先以答题能力或一份收益描述推定风险选择稳定→原文比较显式 probability/payoff 与20/100次抽样历史、解释提示和训练 checkpoint，对同类收益选择形成 description-history gap 与非单调 explanation effect→选择模型/提示时必须分别验证输入表示及行为目标，而不能把较长解释当更稳定的策略。

20模型、360美国Prolific受试者、有限三组 prospect pairs；模型 temperature1 每输入10次，输出最大1024，选择比例只在合法答复中计算。所谓经验是给定模拟 history，不是交互学习。多数 conversational 模型给短解释后更像 risk-neutral expected-utility reference，长数学解释反而回退；reasoning模型也有例外。Open Qwen/Olmo配对与顺序checkpoint支持局部关联，不支持“数学训练必导致理性”。C.4明确没有 DPO/RLVF 系统差异，SFT主要来源只是 hypothesis，且Olmo Instruct-SFT从Think-SFT初始化，不能作训练阶段因果隔离。

四参数 prospect model 的范围 .01–1000，多项碰边；参数可描述但不可作唯一内部机制或精确人格。§8未匹配人类全部解释提示，未拆 decide/explain顺序；20/100聚合会有sample-size效应，因素交互/Simpson混杂未全面控制。参考 prospect 特意放大human与expected-utility差异；相似经济理性不是价值/安全正确。硬件/模型推理精度 Not Disclosed；不要求吞吐硬件来证明这里有限行为效应，未复现。Books待实际owner比较，最终准入待root校准。

## 2602.15307v1 — 潜在准入 2+1+2=5，标准必要证据完成

[精确v1](https://arxiv.org/html/2602.15307v1) §II–IV 实际读。同一 audio representation 在未见任务有线性可分性，不代表其neuron绑定语义标签→原文对 class-conditioned positive activation 做归一化entropy/响应筛选并定点ablation，发现跨任务共享同时包含声学背景和概念属性→需要把表示可读出、响应相关与局部功能性干预分开。并非因为换成audio的LAPE本身新颖而保留；局部反侧改变“class-specific意味着唯一语义概念”的解释。

M2D0.7 ViT 12层/MLP3072，与同架构从头AudioSet supervised分支；EVAR线性head，ESC50/GISE51/VoxForge6语/VC1 gender与35country/CREMA/GTZAN/NSynth/Surge等各自人口。先剔底部5%弱响应，再以任务不同的低entropy百分位（ESC/GISE2%，其余1%）与class响应top5%筛选，非统一阈值的通用coverage证书。VC1 SL49% vs SSL100%只是这个分类人口。共享neurons包括train与wind、cough与dog等背景共现，不能等同高层语义。

定点ablation只涉及GTZAN classical/jazz和CREMA angry/happy，并有同数量random对照；targeted消融对其他genre部分还改善，不是每个class唯一neuron或全功能消失。相关性与局部干预不证明训练因果；SSL/SL objectives/data差异未形成全同预算因果对照。§IV总结未增加部署/全任务保证，跨任务taxonomy、training budget/重复run区间及hardware/precision部分 Not Disclosed；没有运行代码。Books待实际owner，最终准入待root校准。

## 2602.15274v1 — 范围/贡献决定后排除，不追补日期

[精确v1](https://arxiv.org/html/2602.15274v1) 完整题摘以及§3–5、7决定核心实际读。它研究硬编码grid foraging agents：round-robin strategy budgets，episodic年龄类型moving-average distributions、按logloss择predictor、采样地图A*，并报告运动定位噪声增大时memory/planning可输给greedy、冻结memory后漂移退化。15×15/50env/20days及30×30局部步数对照，日内/跨日更新和有限memory容量是已知closed-world机制的局部实现；没有foundation/model-driven planning接口，也未挑战模型表示、训练或系统的基础假设。这里不是因无LLM关键词排除：决定核心仅提供传统foraging应用和解释性类比，未新增足以改变本项目设计选择的机制或受控认知反证。

均值与median/worst-day分别，Mac laptop数秒不是模型runtime收益；progressive budget在30×30还可能比合适固定budget均值差两倍。未把复杂agent优于greedy当通用知识。此项明确EX，不再为不影响处置的日期追加材料请求；保留原文边界供root代表性排除校准。
