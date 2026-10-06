# Jan02 第二批必要命题证据（作者及非作者必要原源复核完成）

日期字段保存于DATACITE_POTENTIAL.json；下列区间均以真实holiday最早announcement Jan1T01Z及不能advance提供ID/DOI、已注册ID的公开上界推断，不把Submitted或注册时刻等同首次公开。未发现同正文的更早作者公开信号；当前事件说明只读现页，不遍历旧revision。

## [B-Trans — 2512.25063v1](https://arxiv.org/html/2512.25063v1)

2+2+2=6，标准必要审阅完成（原源§3–6及算法、实验条件、局限）。推定公开[2026-01-01T01:00:00Z,2026-01-01T03:26:44Z)。输出temperature不能区分同一条件模型内部的token探索与跨轨迹模型扰动；该文在normalization加入Gaussian offset，按sequence采一次并缓存、整条AR保持同一扰动，更新mean参数仍为确定性的，rollout才启用noise。这是参数扰动近似posterior，不是已识别的Bayesian posterior或校准uncertainty；isotropic方差是超参数。

作者Qwen3/Llama3.1的数学pass@k及GRPO/TTRL只支持所披露模型/任务中的探索分支。GRPO为400道难度分层题、SimpleRLZoo配置和<1%参数LoRA；group、更新预算、hardware、precision与最大长度正文Not Disclosed，不能宣称等全成本或训练加速。TTRL以majority final answer作正信号，没有GT训练标签；峰值并非稳定性能，consensus不是真值。σ=.02的sequence与token扰动比较同时改变噪声相关结构：MiniLM余弦是文本embedding多样性，不是逻辑coherence/语义正确性测量。1.7B/1.8B正文标法不一致，不合并数字。未运行伪代码；缓存变量拼写不能当实际实现已经核验。

Books比较：MODEL-SAMPLING Ch20“局部校准误差会复合成序列级多样性坍缩”及前面temperature段已解释token-level分布与sequence多样性不等价，但未承载“sequence固定norm噪声是另一个受控状态”。本项6分仅报告：有限探索案例尚未确立可部署posterior/selection可靠性及匹配预算；mean更新/noise-rollout的likelihood一致性未证明，不把主题相似算已有覆盖。root实际§3–6/7/limitations核验及此限定处置通过；不写Ch20。

## [Thought Gestalt — 2512.25026v1](https://arxiv.org/html/2512.25026v1)

2+2+3=7，必要深入审阅完成；§3.1–3.3、§4全套决定性对照/消融、§5限制。推定公开[2026-01-01T01:00:00Z,2026-01-01T03:25:48Z)。采用命题不是“语义向量比token普遍更好”，而是**visible memory容量与训练依赖图深度必须分开**。每句causal self-attention完成后从EOS的第7层线性readout形成一句向量；rolling M=40保存未按各cross layer预投影的key/value，key含位置、value为句表示，每层自行投影。后续句cross-attention读先前句向量，后续LM loss可通过memory write回传到生成先前表示的参数。推理的可见M有限，并不阻止祖先递归依赖形成更长training graph；作者因而只在训练按S句reset，以30起、每5epoch+12的curriculum控制反传深度，validation/test不作这种reset。模型不是test-time fastweight更新，不能混写成在线训练。

对照固定WikiText103 subsets、lexical-token PPL和相同validation earlystop，排除EOS/EOD label不把易预测特殊token作收益。数据扫12–50M tokens、约85M非embedding参数；参数扫.34–21.3M、固定50M数据，拟合截距移动不证明工业scale-law。sentence-marker-only和固定25/50/75token-span、gist-mask对照分别检查分段、结构和压缩替代解释。§4.3 father-son1000例/condition为**in-context单token**probe；reverse margin仍-2.5→-1.1，未解决parametric reversal curse或一般推理。

§4.4 Table1提供关键质量/训练成本反证：30M tokens、85.6M参数single A40、无model/data parallel，detach at write从29.8 PPL/21sent/s变35.0/24；precision Not Disclosed，不转成推理tokens/s。Self→Cross多容量114M及17sent/s混入参数/算力，不用其29.4证明免费优势。其他architecture与packing/curriculum仍是整体设计，非唯一因果或统计普遍律；没有工业LLM/生产长流/ACL事实回读保证。

具体Books缺口：MODEL-LONG-CONTEXT Ch22“将历史压入状态”末尾只说训练activation未消失；“先定义写入目标”与fast-state credit horizon谈在线参数写入，不等于这份training graph。root已实际§3.1–3.3/4.1/4.3/4.4/Table1/B/C.1/§5原源通过并许可窄锁。已在“将历史压入状态”的一般容量讨论与线性Attention桥梁之间实际加入两段，把有损句向量状态、visible window、梯度祖先与detach/reset成本连在一起；不改状态容量定理，不复制实验数值作为规律。root已实际读全部新增diff及前后邻接，非作者写后通过；末注已同步，不代表日报完成。

## [Diffusion Language Models are Provably Optimal Parallel Samplers — 2512.25014v1](https://arxiv.org/html/2512.25014v1)

3+2+3=8，理论机制/反证深入完成；§2定义、§3 Theorems3.1–3.3构造、§4 Theorems4.1/4.2/4.5及证明和最后remark。推定公开[2026-01-01T01:00:00Z,2026-01-01T03:25:30Z)。条件是同一轮given visible state的位置预测条件独立、独立random bits、指定circuit复杂度与workspace，冻结token不再修改的路径区别于remask/revision。不是学习到的Transformer、训练算法或硬件速度证明。

§3：N门、深度d、宽w的目标circuit，一次写后冻结的CoT构造用L=N、D=d；remask用L=2w+2ceil(log(d+1))、D=d+1，revision用L=w+ceil(log(d+1))、D=d+1。后两构造的每步predictor/F/G depth O(log d)，不能当d(n)增长时仍固定深度或无成本全局最优；空间、迭代深度与每步计算须分开。每轮并行L位置Attention并非AR-cache只新增一位置的同work；定理步数不等于总FLOPs/wallclock。

拟采用最小反例是§4的**均匀even-parity分布采样**，不是给输入计算parity。Revision两轮先生成n-1个独立临时prefix变量y并令最后y=0，再以相邻XOR改写输出z；共享临时state使最终位置相关，但每轮conditional factorization仍成立。冻结路径在L=n、无额外CoT、predictor与unmask选择器均AC0/poly-size时不能O(1)步exact采样；不是TC0或任意现实Transformer下界。Remask构造明确允许依赖步号的predictor/selector，不能泛化成所有时间齐次sampler。关键新知识是可重写位置还能回收**临时计算符号/工作空间**，不仅修复错误。

Books具体差异：MULTIMODAL-GENERATIVE-PARADIGMS Ch24“Masked generation”已讲factorization/条件相关、保守提交和更多mutable work以修错换并行，但未讲临时符号与最终输出的身份分离、workspace复用。root实际§2/3.1–3.3/4.1/4.2/4.5证明/末remark原源通过并授窄锁。已在“后一步没有否定保守unmask...”后实际加入一段受限parity两轮桥梁及一段复杂度边界，保留旧confidence schedule，不引申DLM普遍快于AR。root已实际读全部新增diff及前后邻接，非作者写后通过；末注已同步，不代表日报完成。

## [Estimating the Entropy of English with Language Models — 2512.24969v1](https://arxiv.org/html/2512.24969v1)

2+1+3=6，标准机制/评价边界完成（§2–4及必要Appendix的数据采样、单位与training control）。推定公开[2026-01-01T01:00:00Z,2026-01-01T03:24:24Z)。采用是**conditional code-length曲线随context及训练成熟度变化，不是最大窗口即内容量**。实际cross-entropy/code length L与模型自己分布的conditional entropy s不同，更不等于真实英语entropy；Qwen自身entropy偏低也不证明真实可压缩性。OLMo2/Llama3.2/Qwen3/DCLM跨tokenizer换chars单位、C4/Wikipedia/Poetry和9genres切片，content/training-membership混杂不能忽略。有限N约1e4的曲线下降，不能外推infinite entropy=0、exact recall或长程推理。

DCLM1.7B训练控制28B tokens、2048context、8H100、每GPU batch6×48accum、seed1337，precision Not Disclosed；pretraining snapshots与其他posttrained模型不是匹配architecture因果对照。MI至93chars的巨大采样仍有有限样本floor；长相关不直接证明长range interaction必要性，后者依赖stationarity及指定模型假设。字符串crop/长度过滤和corpus成员未知限制泛化，不把字符跨度当任意事实检索能力。

Books处置已有覆盖：MODEL-LONG-CONTEXT Ch22“相同Token Length仍可能承载不同Information Load”的三段已把长度与内容/单位/模型版本解耦、要求分层EvalSpec且保留相关非因果边界；本次有限code-length曲线仅补局部验证，不改变该具体设计判断。**并非称现有density段已经覆盖code-length/真实entropy的数学命题**，也不追加作者entropy外推。root实际Eq1–5/语料/单位/训练Appendix B/C及此窄NoChange判断通过。
