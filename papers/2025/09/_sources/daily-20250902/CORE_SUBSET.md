# 2025-09-02 必要 core / 负侧限定记录

作者 Aristotle；窗口 Sep1 09:00 至 Sep2 09:00 BJT。日期未成立不免除必要复杂度、安全或设计反证核查。本记录不是全文审阅、当窗 Evidence 或 Books 采用。实际抓取版本、时间、状态和哈希在各 `*.request.json`；只声称下列实际读过的部分，未运行代码，未核全部图像/附录或跨模型复现。

## TConstFormer 2509.00202v1

[原始 HTML](tconst-v1-core.raw) / [请求](tconst-v1-core.request.json)。实际读引言周期更新、§2.1 信息路径切断、§3 双窗口机制的相关段、§4.1–4.3 完整复杂度公式、§5.2 KV 公式与失效时机、§8 限制、结论相应声明。

**发现中心计算主张内在不一致。** §4.1 将窗口滑动后的第一个 token 同初始 token 一起列为 cache miss，明确给出 `C1*N+C0`，其中 `C1=2*D*W_oh`；§5.2 说明每生成固定 `W_og` 个 token 就发生此重算。固定窗口、深度和维度下，周期平均成本含 `C1*N/W_og`，不能从其公式推出随历史 N 的摊还 O(1)。不能用只看 cache-hit token 的常数成本替代全周期成本，也不能把固定 KV 缓存当全部历史输入存储均恒定。若实际实现仅更新固定 state，需要原算法/实现解释为何上述 N 项不再随历史增长；当前正文没有在已读部分消除这个矛盾。

保留固定状态/切断直接历史路径的设计潜力及压缩取舍，不授整体 O(1) 推理、无损 full-context 或无限历史能力。§8 明示约41M模型，逐字精确检索尚无定论；不是因小模型关闭，而是不能把固定状态推广成精确回忆证明。未读全部实验表/图、代码、Appendix A 推导全文；现有主文公式已足够阻止正面复杂度采用。状态：中心计算命题争议保留，定点重开为准确全周期复杂度及实现状态/历史访问说明。

## Unlearning 2509.05316v1

[原始 HTML](unlearning-v1-core.raw) / [请求](unlearning-v1-core.request.json)。实际读§2.2–2.3邻居与采样定义、§4.1–4.3数据生成/设置/评价、§5.2、§6–7、Appendix 0.A.5 memorization。未读所有算法附录/结果表、图像或独立攻击评估。

MELU确为按 forget entity 配对其 retain 邻居，general set 随机分配 forget；不是一项新的基础 unlearning loss。WPU的20目标扩展，间接邻居和QA由同族LLaMA3.3生成，LLaMA3.1-8B先在所有数据上微调，再以LoRA做GD/NPO/DPO。FE由ROUGE-L/条件概率/语义相似度构造，DPO target可为“I don't know”；这些输出指标不能证明预训练基础权重知识被抹除、抗提取或隐私消除。

1:1每epoch用98 retain，cyclic/MELU遍历1801 retain并重复 forget；同4epochs比较不等计算/曝光预算。脚注另报1:1 DPO随机采样100epochs FE0.79/MU0.78，因此不能把当前等epoch劣势表述为不可有效忘记。作者明确尚不能解释 cyclic/MELU 稳定性原因；间接关系生成、实体可分离假设、未独立完整syntactic集合、仅少数算法/一个模型家族是限制。保留“邻居构造和采样会改变测得forget/retain取舍”的局部评价纠错潜力，不授通用最优或稳定性因果证明。

## Safe-LLaVA 2509.00192v1

[原始 HTML](safellava-v1-core.raw) / [请求](safellava-v1-core.request.json)。实际读§3至§3.1.1完整PRISM/清洗定义、§4.1–4.3叙述、§5、Appendix B与E/E.1的文字协议。未读全部Table2/3单元、Fig8性能像素、图内完整judge prompt、Appendix F统计表或代码；不授全部性能/统计检验。

PRISM分显式soft/hard问题的拒绝率及3种开放回答的属性泄露保护分数 `1-mean(B_j)`；后者不是同一个拒绝指标。正文§4.2把97.1%称“leakage rate”与自身指标方向不一致；不按该句宣称高泄露或消除泄露。GPT-4/Gemini两个judge给出的保护分数不同，不能作人工真值。训练清洗由GPT-4o改显式问题为拒绝、隐式属性为中性词；Appendix B称7B baseline与处理组仅数据不同，支持其局部对照设置，不能由自动清洗宣称所有属性已移除。

正文用通用视觉任务作语义保持代理，并非逐样本faithfulness或中性问题false-refusal的直接测量；已读协议没有足够证据支撑“无误拒绝/隐私保证”。必要反侧保留：更短回答本身会少泄露，作者也将0.5B优于7B部分归于回答长度；一般任务代理不能消除此混杂。保留双方向评价和显/隐式数据清洗潜力，不授所有属性零泄露、语义等价或全面安全。

## 两种 hallucination 2509.00371v1

[原始 HTML](hallucination-v1-core.raw) / [请求](hallucination-v1-core.request.json)。实际读§2–3.3、§3.4问题解释、§4的centroid/hidden-steering机制段、§5.1设置/§5.2–5.4叙述、Appendix B–D文字。未读§3.4完整SID代数推导/§4全部公式、所有表格或图像，不授精确性能排名或已排除所有因果替代。

负侧协议真实具体：LLaVA1.5-7B greedy，COCO/POPE object yes/no，VCD被报告减少false negative却增false positive；应分账，不以总体分数解释为统一纠错。VPFC把top25% visual-attention token求centroid，在等面积方区做轻度增强，用hidden-state差分steering；其优势依赖存在/不存在对象的attention集中/分散观察。定位attention与“已编码语义”、同现偏差与fabrication之间仍是作者解释，局部干预改变yes/no不证明排他的两种根因。

评价另用Qwen-VL-7B、MME、CHAIR500图、LLaVA-Bench；Appendix C称head比例过高会降分，正文centroid消融在adversarial上退化；不授参数无条件稳健。Appendix D明确不直接针对fabrication suppression，主张主要为少omission且不额外fabrication，不把它扩写成消除两类hallucination。保留局部反证与校准机制，日期仍hold。

## BAI 2509.00309v1

[原始 HTML](bai-v1-core.raw) / [请求](bai-v1-core.request.json)。实际读§3–4.1、§4.5–4.6开头的负侧定义/比率叙述、§4.7、§5–6。未读全部length图、benchmark表、case附录，不授曲线像素已核/跨seed复现。

两步参数线性合并确为先均权instruction/reasoning SFT，再按alpha混入原pretrained；§4.5.1亦可只合并base与reasoning，不能把两步均为所有负侧对照必用。实测为Seed-MoE-2.5B/25B、PPO actor/critic学习率1e-6、batch4096/mini512，通常1600steps，纯reasoning与0.6/0.4部分跑3000。比率改变既初始行为也至reference/rollout分布，不从RM轨迹推出已证明reward hacking消除或保留base知识。

作者声称纯distillation→RL早期长度崩塌与RM hockey-stick、混合缓解；保留初始化条件反证，不当作RL必然退化。§4.7讨论training-policy对sampling-policy KL，不自动等于对固定SFT reference的KL。比率/长度分桶、模型家族、未核seed与实验轨迹是采用边界；“optimal/consistent eliminates”不推广到通用训练保证。

## 处置与未覆盖

以上五项均只完成必要subset，不能写为五项完整Evidence；没有给日期hold项评分、授Books或强制全文队列。若拟采用性能/安全/数学的更强命题，再定点核依赖它的公式、表图、反侧或artifact。普通准入判断可继续，外部first-public缺口不覆盖本文方法缺口。APRIL按root摘要校准：现有APO+RLVR组合和单一总收益没有具体新协作证据，贡献关闭；不继续开全文队列。Radio保留semantic等价prompt负侧的通用评价潜力，不采科学应用结果。
