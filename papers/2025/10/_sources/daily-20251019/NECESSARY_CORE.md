# 2025-10-19 必要核心位置与停止

作者Curie实际限定阅读25家族（24份精确v1 HTML及1份v1 PDF），root独立有效核该25并新增MLCPD/Edge两家族，合27必要命题检查。新增两项不回填作者阅读；不是下载/投影数量、全文或复现证明。均未获完全落窗first-public，不计正面Evidence、评分或Books采用。HTML原件为`core-<ID>v1.raw`，派生阅读定位为同名`text.txt`；表中行号只定位派生原文本。未读附件不隐瞒也不作完成队列。

| ID / 原精确版本 | 实际必要位置 | 处理的命题及反侧 | 停止 |
| --- | --- | --- | --- |
| [2510.16292v1](https://arxiv.org/html/2510.16292v1) | §3.1 joint QKV/缓存重构，95–114；§3.3量化，140–156；§4.4/5，855–859 | 缓存的是共享低秩Cqkv，再重构KV，不是随意丢弃原KV。RTX4070 12GB/batch1/4K下baseline部分CPU offload，13.1x不是纯同驻GPU算子加速；HallusionBench局部改善不授通用幻觉抑制。 | 已解决缓存身份/性能归因边界，不读全部accuracy表或附录。 |
| [2510.16295v1](https://arxiv.org/html/2510.16295v1) | §4.1–4.2，167–187；§7/8，679–714 | member/nonmember来源时段混杂可仅凭图像特征识别；public-data OpenCLIP-LLaVA保证样本身份。仅LLaVA1.5 7B/gray-box输出概率，不外推MIA不可能或隐私安全。 | 对照混杂与威胁边界足够。 |
| [2510.16340v1](https://arxiv.org/html/2510.16340v1) | §6–9，372–438 | think/answer标签由GPT4o及人审，OOD相关变弱是输出测量；不能称读到真实内部思维或证明战略意图。单model instance、固定学习率/epochs未隔离训练动态。 | 反侧与限制明确，不读提示词全集。 |
| [2510.16380v1](https://arxiv.org/html/2510.16380v1) | §3评价，196–214 | 专家rubric和judge最低类别macroF1校准有具体测量增量；闭源trace summaries与开放实际trace不严格可比，文本过程分不证内部因果faithfulness。root另核197–207 Eq1：sgn(p)*r*p=abs(p)*r，正负方向取决于r编码而该段未明示反向编码，保留未核代码的公式方向疑点，不默修或采用争议分值。 | 不遍历1000情境/伦理rubric附件。 |
| [2510.16381v1](https://arxiv.org/html/2510.16381v1) | §3.2，110–137；§4信任/安全，269–274 | offline theory、online axiomization、symbolic prover有明确边界。作者自己承认攻击仍能改事实输入；规则完整性不等语义输入完整性，撤除端到端prompt-injection免疫推断。 | 此安全命题已处理，不读全部insurance案例。 |
| [2510.16415v1](https://arxiv.org/html/2510.16415v1) | §3.1，88–121；§4假设/Theorem1，211–247；§5.1，250–251；§6，466–468 | NDB接管/skip/recompute/low-rank改变故障时梯度。相对误差δ、smoothness、方差假设才支撑momentumSGD rate，不是精确轨迹/Adam一般保证；32 A100/4node与per-iteration failure设置。 | 假设和必要限制足够，不遍历证明/全部模型附录。 |
| [2510.16439v1](https://arxiv.org/html/2510.16439v1) | §5，581–595；§6/限制，770–807 | token-attribution删词的任务依赖与math退化；random/bottom保留表现提示可能contamination而非确证。API采样temperature1，不把provider价格表当端到端成本/碳实验。 | 负面结果/替代解释足够，不扩全配置表。 |
| [2510.16442v1](https://arxiv.org/html/2510.16442v1) | §III，75–87/127/170–175/204；§IV-D/E，602–606 | ST-SIT跨帧表示与两阶段reasoning有潜力；facial JSON是模型条件输入，未见独立硬验证器保证解释faithfulness。GT伪造mask用于标注、分类消融/定性rationale不证通用可信推理。 | 只处理表示与解释安全边界，不读补充视频。 |
| [2510.16476v1](https://arxiv.org/html/2510.16476v1) | §3 data，102–105/170；Appendix A.2–A.3，793–796 | instance/verifier/heuristic提供RLVR任务，不把TSP多起点近邻+local-search参考当精确optimal ground truth。Qwen2.5 7B/8A800/十任务局部。 | 已核奖励基准身份，不跑全部NP生成器。 |
| [2510.16505v1](https://arxiv.org/html/2510.16505v1) | §3.3/3.4/4.1，145–182；限制531–535 | no-context MCQ捷径与结构化JSON对照是一般多模态评价测量信号；JSON后仍非随机，20%人工语义核，不能称完全debias。只保留通用测量潜力，不开展科学文献分析应用/附件。 | AI-for-Science应用暂停；此测量消歧已足够。 |
| [2510.16552v1](https://arxiv.org/html/2510.16552v1) | §4.1前半78–87；§6，378–383；Appendix8.1，541–545 | gold-label leakage与raw经验忽略是具体反侧；reward-agnostic reflection/relevant abstraction仍需数值reward，额外长序列/summary成本，不能当免费语言reward替代。 | 已读必要collapse定义/例头，不遍历全部prompt。 |
| [2510.16565v1](https://arxiv.org/html/2510.16565v1) | §4.1–5，523–540 | query语言影响path overlap的观察；作者明确未来需intervention/circuit patching，故不采用“文化知识主要储于语言路径”的因果定位结论。 | 只核关联/因果权限，不扩全部country表。 |
| [2510.16567v1](https://arxiv.org/html/2510.16567v1) | §4，317–336；§6/限制，539–551 | 四轴ASR错误结构有测量潜力；root纠正§5/Fig3主要为metric inter-correlation，不能概括为全部与WER相关。SDist逆余弦及Eq6的1-SDist方向疑点未核代码，不能默修/采用；English、embedding与人为权重不授临床/法律风险或跨语种通用检测。 | 必要限定足够；不把题摘或争议数值作正式采用。 |
| [2510.16606v1](https://arxiv.org/html/2510.16606v1) | §III，165–181；§IV setup，210–215；§IV-C/V，272–285 | best-effort RDMA把丢包交ML层，20B+32B DCQCN应区分；FPGA原型/128-node仿真及MTBF估算，不授tensor/PP/MoE任意丢包正确性或生产resilience。root另核182–207：lossy timeout使用按时到达数据完成step，不是等齐精确collective，不授TP/EP精确语义。 | 已收窄执行语义/测量权限，不看全部NIC引用。 |
| [2510.16677v1](https://arxiv.org/html/2510.16677v1) | §III，128–137；discussion/IV，192–196 | record-split、3seed、group bootstrap下GRU/小Transformer在分类/预测任务次序不同，是局部反侧，不因小/医疗自动关闭。θ基于全语料统计guard不等无任何选择偏差；没有on-device延迟实测。 | 不授临床或通用架构优劣，停止领域样例。 |
| [2510.18893v1](https://arxiv.org/html/2510.18893v1) | 架构181–183；§7.2，375–409 | Yjs SEC/字符收敛不等语义无冲突。作者只核60/600语义样本、无human评分、max5agents，N>5为推算，也未比CRDT/OT/consensus原语。 | 关键协调反侧足够，不读所有生成代码。 |
| [2510.21783v1](https://arxiv.org/html/2510.21783v1) | §V-A，369–399 | MIA对照CIFAR随机50/50与StableDiffusion LAION成员/COCO非成员要分开；后一数据源差异有混杂可能，不借小噪声攻击成绩声称纯membership泄露或所有扩散模型脆弱。 | 此隐私反侧已明确，不全扫噪声参数。 |
| [2510.16641v1](https://arxiv.org/html/2510.16641v1) | §3.1–3.2，305–321 | Oracle历史与SelfPrediction不同，gold GPT4o风格上下文有提示收益/评价耦合；小模型增益和多轮<50%不能直接当真实交互能力曲线。 | 不遍历647对话。 |
| [2510.16645v1](https://arxiv.org/html/2510.16645v1) | §5，285–301 | thinking-mode任务条件/初始化提示影响有潜力；divergent在math可劣于CoT，显式auditable链仍不证faithfulness。 | 处理负侧后停，不遍历Web实例或多agent全部实现。 |
| [2510.16333v1](https://arxiv.org/html/2510.16333v1) | §3.1，143–158；§6，487–494 | PIVOT posttraining改变encoder表示的反常识潜力保留；实际对比是SFT vs DPO（作者称RL），同对数不等同全部算力，不外推到在线PPO/GRPO。 | 不把标题RL误解为所有RL；无需旧版/未来v2。 |
| [2510.16660v1](https://arxiv.org/pdf/2510.16660v1) | PDF pp3–5及p20（派生520–538），`utap-pdf.raw` | frozen surrogate可梯度训练扰动、masked/attention drop后迁移未知encoder；900patch/224px/10epochs/ε20/RTX4090。黑盒指目标未知，不是攻击训练无模型访问；线性probe下降不等真实临床损害/所有foundation安全保证。 | HTML404后必要PDF已读；不遍历38页/补充图。 |
| [2510.16356v1](https://arxiv.org/html/2510.16356v1) | 80–113；352–375；440–455 | RWPO近端非线性attention与dot-product比较；方向一致性条件D≥γ√I和log-Sobolev假设不可省略。Laplace b≥a、Gaussian τ²≥σ²等是条件，不授任意Transformer全局凸性或普遍更快。 | 理论权限与实验范围已明确，不遍历证明附件。 |
| [2510.16591v1](https://arxiv.org/html/2510.16591v1) | 75；268/280/286/295；323–325 | 对称性约束与无约束二次表示的学习条件比较是一般表示/学习理论潜力；CLT/RG受控案例不证明所有物理对称性都必要或所有无约束网络均较差。 | 保留一般学习命题，不开展科学领域应用。 |
| [2510.17885v1](https://arxiv.org/html/2510.17885v1) | 104–113；198–199 | RTX3090/batch100等设置下ONNX FP16对ResNet50改善、对ResNet18可恶化，不能以FLOPs/precision单调预测runtime。SmoothQuant的OPТ成本结论仍绑定设置；不授所有模型memory-bound因果。 | 保留运行配置/架构交互的负面潜力，不因“小模型/已有指标”排除。 |
| [2510.16474v1](https://arxiv.org/html/2510.16474v1) | 69–84；227/229中实际可见设置；301–305 | group-adaptive kernel以学习φK和权重融合表示、variational objective是机制潜力；DTI/NIR两领域评价不授跨领域有效性，也不由此开展药物科学应用。 | 一般表示机制身份足够，不遍历领域实验/全部特征。 |

## root独立新增反侧（不回填作者阅读）

已实际读取[root FINAL](FINAL_INDEPENDENT_REVIEW.md)的2026-10-05T11:26:49+08:00记录，以下属于root新增必要阅读；原有效位置不重读：

- MeCeFO §3.2–3.4/Alg2–3与§4：跳过接管rank的MHA backward、仅平均未故障/非接管DP ranks，低秩及周期SVD有误差与成本。momentum SGD及relative-error/bias假设不授AdamW精确梯度或任意真实故障效率。
- SHALLOW §5/Figure3主要为metric之间相关，不能统称全部与WER相关；§3 SDist逆余弦而Eq6用1-SDist有方向疑点。未核代码，不替作者修公式/照用争议数值；英语/GPT4o synthetic与医疗示例不授临床真值。
- UTAP PDF pp16–20：七ViT/CRC7180patch/TCGA六类子集的clean-feature线性classifier限定。WSI、FDA/proprietary端到端、CNN、segmentation及对抗训练免疫未证，不授端到端诊断通攻。
- root后续窄读MoReBench 197–207的Eq1与Celeris 182–207已同步对应表格；仅该安全边界，不回填为作者新增阅读、不扩附件。NP-Engine启发式TSP参考是suboptimal，不称最优真值。

另外：[2510.16309当前官方页](https://arxiv.org/abs/2510.16309)明确整稿withdrawn，理由attribution/citation accuracy，v3撤回说明已核；不入选、不评分、不Books，不把可取得旧v1当有效安全证据。

## root独立恢复两项（作者不重复core）

依据[root FINAL最新分层与恢复记录](FINAL_INDEPENDENT_REVIEW.md)，仅这两项误关闭恢复日期潜力，不扩领域池、不评分/采用：

| 精确v1 | root实际必要位置 | 恢复依据、反侧与停止 |
| --- | --- | --- |
| [MLCPD 2510.16357v1](https://arxiv.org/html/2510.16357v1) | 完整AB/history及§3.2–3.4/Alg1–2/§3.5/§5 | universal AST structural-homogeneity保留syntactic-heterogeneity，有表示/验证接口潜力，非仅数据集。lossless与去whitespace/Alg1 skip delimiters矛盾，O(1)仅单节点访问不授整树遍历/语义等价或迁移收益。未核artifact/七百万records/代码，必要限定足够，不再扩附件。 |
| [Edge speech 2510.16497v1](https://arxiv.org/html/2510.16497v1) | 完整AB/history及III/III-D/VI | cloud encoder offload、decoder留edge及平均logits/SNR触发有新执行边界，非仅语言应用；16GB/1.7GHz电脑/NetLimiter和两文本长度条件下，低于512KB/s局部延迟劣化及长文本传输成本保留。不授真实手机/任意网络/准确性，未核代码/训练附件，必要限定足够。 |

上述是作者25加root新增2，共27必要命题限定检查，不是27家族标准/深入审阅完成数；root原25有效读取复用，日期隔离仍在。各项达到必要停止后不扩附件。root五具名关闭样本及十四有限source/六部分已核，2026-10-05T11:59:28+08:00 FINAL末节实际变化POST/DAY通过；本日报已完成，无剩余core或复核待办，终态隔离不变。
