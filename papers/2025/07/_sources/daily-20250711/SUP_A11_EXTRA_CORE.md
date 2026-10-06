# July11：额外四项准入决定核心

root 作者实际读取，2026-10-11。对应 Ptolemy 在完整精确 v1 题摘校准中提出的四个 N；不扩大附件队列。四份精确 v1 HTML 均 HTTP200，见 [请求记录](SUP_A11_EXTRA_REQUESTS.json)；下载不等于全文审阅。下面均明确保留 **P（贡献潜力，必要公开日期未核）**，不评分、不计确定当窗候选、不授候选 Evidence 或 Books。

## [FedPhD — 2507.06449v1](https://arxiv.org/html/2507.06449v1)

实际读取 §IV-A/B/C/D、Eq16–25、Algorithm1及 §V-C/D 的剪枝/通信反侧；[精确原文](SUP_A11_EXTRA_2507.06449v1.html)、[提取](SUP_A11_EXTRA_2507.06449v1.txt)。层次式 diffusion 训练中，单按样本量/固定边缘节点聚合会保留 non-IID 失配；本文以客户端/边缘累积标签分布与目标分布的距离形成 SH，并同时改变聚合权重及客户端选边缘节点概率（后者兼顾累积负载），同时把结构化剪枝置于云端共同模型而非任意客户端独立删不同形状。具体潜力是 **训练数据分布、参与者 placement 与聚合权重不能当作互不相关的系统选择**，路由 `TRAIN-DISTRIBUTED-TRAINING`；不是因为 diffusion+FL+pruning 名称组合而准入。

保留必要反侧：Eq19 将 q_e 称为 distribution，但分子旧 q_e 没显式乘旧样本量，不能静默修正为正确累计概率；Eq22/24/25 的 ReLU 归一化需要非零分母，正文没有为所有超参/负载给成立保证。标签分布上传不是 privacy guarantee，§IV-D 明确 DP/MPC 尚未实现。§V 的通信成本是距离×数据量模型，不是大模型集群端到端网络 benchmark；44%到61%/74%剪枝后质量退化不支持任意压缩比例无损。上述没有被验证的普遍保证不采用，局部选择规则已足以保留贡献潜力，不将其记为必要证据已完成。

## [Speech Tokenizer — 2507.06802v1](https://arxiv.org/html/2507.06802v1)

实际读取 §2/Eq1–7、§3.2–3.4/Table2–4；[精确原文](SUP_A11_EXTRA_2507.06802v1.html)、[提取](SUP_A11_EXTRA_2507.06802v1.txt)。不是泛称 speech+semantic/acoustic：RVQ 首分量由 HuBERT semantic guidance 约束，下一残差分量引入 ECAPA-TDNN acoustic guidance/attention alignment，解码时可以换第二分量保留第一分量，形成可检验的表示取舍。作者 token-swap/情绪任务更好但相同 50token/s 下 Qwen2-1.5B ASR WER 0.290 对 SpeechTokenizer 0.253 更差，**保留声学信息与最大化语义识别不是同一个目标**；路由 `MULTIMODAL-REPRESENTATION`。这里只判断该 trade-off 值得核验，不把单指标宣传计为普遍提升。

Eq5 以残差量化输出与 acoustic 表示写 KL，但正文未清楚建立二者归一化概率域，不能猜测代码用了 softmax；该目标数学适用性保留待核。SER 的 tokenizer 未情绪微调不等于 classifier 无训练（BERT 训练30epoch），ASR 也训练3epoch/LibriSpeech500h。未采用无训练泛化、完全解耦或全成本优势；所有数字只作原文必要反侧，不授复现或可靠性能结论。

## [SEAT — 2507.06829v1](https://arxiv.org/html/2507.06829v1)

实际读取 §2.1–2.3/Eq1–4、§3.1及§3.4的 collapse 个例；[精确原文](SUP_A11_EXTRA_2507.06829v1.html)、[提取](SUP_A11_EXTRA_2507.06829v1.txt)。每轮 N 条独立输出，下一轮将上轮答案共同写进 prompt；固定模式用校准语义熵阈值，adaptive 模式用第一轮 SE 作基线，遇到更低 SE 停止。具体潜力不是“多生成即可更好”，而是 **复用上一轮答案形成相关共识后，低熵不必表示正确；停止规则必须面对 diversity collapse**，路由 `MODEL-SAMPLING`。§3.4 R7B/N8 单例从12.5%→37.5%→0，熵却持续下降，支持保留停止信号的局部失效反侧；不是总体因果证明。

Eq3/4 基于回答片段概率估计簇质量，作者脚注明确可能出现负 SE，未校正；不要直接当标准概率分布的 Shannon entropy。Secretary problem 是启发，跨轮答案条件化不满足未说明的随机次序/独立候选假设，不能移植全局最优保证。固定阈值 §2.2 用1000问题，§3.1用10000且剔5%尾点，这个校准口径差异保留；实验完整执行最多8轮以分析结果，不能据选定停止轮直接认领实测端到端节省。必要决定事实已明确，性能证据和校准适用性并未关闭。

## [UniConv — 2507.07030v1](https://arxiv.org/html/2507.07030v1)

实际读取 §3.1–3.5/Eq1、§4.1/4.5–4.8及 Limitations；[精确原文](SUP_A11_EXTRA_2507.07030v1.html)、[提取](SUP_A11_EXTRA_2507.07030v1.txt)。同一个 decoder 用 EOS representation 检索并从 query representation 生成，单纯联合 retrieval/generation 目标不能保证使用检索证据时的训练接口一致；CII 将 query⊕positive passage 与目标/错误回答做 contrastive 对齐，DDM 用真实 query/passage/response 三元组替代把回答当段落再把段落当回答的错位监督。§4.5 明确 **CII 改善生成却损害 retrieval**，提出分阶段训练只是未来工作。具体贡献潜力是检索/生成共享参数时的目标干扰与监督对象错位，而非“单模型比两模型浑然天成”；路由 `TRAIN-SFT`。

§4.6 分离系统用不含 CII 的 generator，比较并非只改变模型是否共享，不能把全部可靠性收益归于 unified architecture；§4.8相同历史检索结果仅支持其特定 generator 对照。Mistral2-7B、LoRA/8A10040GB、长度/批次/训练配置限制仍需必要证据审阅，不采用通用低成本保证。7B retriever 的 latency concerns 明确未被“以后减少rerank”证明消除。公开日期及可能 ACL 同稿先公开仅凭会议标签不能认定，后续只核具名必要身份，不遍历会议。

## 交付边界

四项作者普通准入决定待办已处理：4P/0N/0C；仍须 Ptolemy 实际独立校准上述核心与反側，作者不代写通过。它们是 root96 内身份，不增加154个新发现身份分母。旧候选/日期/评分与连续正文不变，未写 Books/State/index，未stage、commit或push。
