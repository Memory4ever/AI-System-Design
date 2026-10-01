# 2026-04-21 最小贡献消歧：独立复核

## 首批范围与结论

本次为非作者有界准入复核，访问日期为北京时间 2026-09-27。已重新完整读取当前 AGENTS、Research Contract、Report Contracts 与统一 Prompt；沿用此前实际读取的每日来源与 arXiv 路由。窗口仍为 `2026-04-20T09:00:00+08:00`～`2026-04-21T09:00:00+08:00`。16818 不在当前最小消歧队列，按任务许可改为 16965。

实际范围是七项官方 `/abs/...v1` 完整标题、摘要、版本历史和撤回提示检查，以及下述 HTML 必要方法、对照或限制。未重抓 1,260 项库存，未新增发现池，未做全附件遍历，未修改 Report、Books 或共享 checkpoint。本次没有发现这七项的官方撤回提示；这不替代独立的公开日期归属或全量 correction 审计。

| 家族 | 独立准入建议 | 解决的具体疑问 |
| --- | --- | --- |
| 16339 | 前分母关闭 | 有具体 intent/precondition 结构，但治理层级组合与配置模拟没有提供新的重要执行保证或独立失效边界。 |
| 16430 | 前分母关闭 | energy/C-DLA 特征选择加 probe 支持受限检测 operating point，不支持其因果机制命名。 |
| 16606 | 前分母关闭 | 成熟模块组合的隐私核心保证未被实际信任合同支撑；不能把该文的过强主张本身当长期贡献。 |
| 16909 | 保留窄潜在贡献，作者继续必要审查 | 不采 taxonomy 的内部因果解释；同 1-shot 下 reasoning SFT 的跨维反收益提供具体优化边界线索。 |
| 16965 | 保留窄潜在贡献，作者继续必要审查 | 接口双时钟和两相模拟的请求时序错误，可以使内部 DRAM 统计与 application 性能脱钩。 |
| 17053 | 前分母关闭 | 伦理判定被 norm framing 翻转，不等于突破实际 harmful-action policy；未分离新的安全执行路径。 |
| 17240 | 前分母关闭 | 有限循环、投影与安全 fallback 的假设性组合，不是一般企业 policy 的新收敛或可执行安全保证。 |

五项关闭是 family-specific 贡献裁决，不是“读不完”或按题目关键词拒绝；两项潜在贡献也不是已冻结候选、已完成 Deep Review 或已进入 Books。作者仍负责实际时间组合、去重、证据审阅与最终 disposition。

## 16339：Semantic Consensus

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16339v1)、[官方 HTML v1](https://arxiv.org/html/2604.16339v1)。必要定位：§4.2–4.4、§5.3、§6.2–6.4。

SIG 保存身份、对象及前后置状态；CDE 按互斥状态、共同前置条件失效与并发因果依赖检测；CRP 依次用 policy、authority、先注册优先及人工升级。这是实际结构，不能称完全空泛。但 §5.3 实现仍是规则、同义词与前后置条件；§6.2 是模拟三种框架的交互/置信度配置，不是三套真实框架端到端部署；§6.3 Judge-Agent 使用预校准 recall/precision。没有从这些组合中分离出新执行有效性条件。故关闭，不以工作流完成率推导完整治理保证。

## 16430：HalluSAE

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16430v1)、[官方 HTML v1](https://arxiv.org/html/2604.16430v1)。必要定位：§3 Eq.2、§4.1–4.3 Eq.3–9、§5.2 Table2、§5.3 Table3–5、附录 Training Pipeline。

GPE 是相对 factual feature centroid 的距离，按类别均值差选 layer zone；C-DLA 用 wrong/correct token 对比方向选 SAE features，随后训练 logistic probe。必要实验是 layer/feature selection 对照及高激活样本归纳；在这些方法和结果段中没有直接 feature intervention 的因果验证，§5.2 将定点干预列为后续方向。能支持特定 Gemma 检测配置的局部收益，不支持发现幻觉必然因果阶段。尚未给足以改变长期机制选择的独立条件，因此关闭；不是因 SAE/probe 组件成熟而拒绝。

## 16606：SafeLM

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16606v1)、[官方 HTML v1](https://arxiv.org/html/2604.16606v1)。必要定位：§3、§4.3–4.7 Eq.2–8、§5.1–5.3 Eq.9–12。

§3 将 server 设为 honest-but-curious；§4.4 加密和之后 §4.5 写“解密后”做 median，却没有交代密钥及解密主体的信任接口。须纠正一个容易误判的点：Eq.2 是 ±1 二值，已知参与数时 aggregate sum 足以推导多数/median，不能说求和必然无法算 median。真正的问题是该信任边界缺项，以及 §5.2 从 IND-CPA/DCRA 推出任意 inversion 的固定 PSNR 上限，后者不能仅由 ciphertext indistinguishability 推得。收敛又预设 cosine alignment，而非证明该阈值必满足。模块组合和这些过强保证不构成可靠的新隐私机制贡献，故关闭；不把论文缺陷自动升级成安全候选。

## 16909：PRISM

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16909v1)、[官方 HTML v1](https://arxiv.org/html/2604.16909v1)。必要定位：§2.1–2.2、§4.1 Table3、§4.2、§6。

仅按语料来源、模型 cutoff 和任务类型预分 KE/KM，并不能证明内部究竟“存错”还是“缺失”；§4.2 attention 图也不是这种内部状态的因果 oracle。不能为四分类命名入选。然而 §4.1 Table3 确实在 Llama3.1-8B 的 1-shot 设置下报告：reasoning SFT 改善数学 RE，同时使 KE/KM/IFE 明显变差。保留这个跨维反收益分支，而不是整套 causative taxonomy；作者后审应核该 SFT 的训练、数据和预算合同。§6 仍承认 cutoff 不披露及 contamination 风险。本次实际用 v1 URL，官方 history 另列后续 v2；没有用 v2 替代，也没有宣称 HTML 与 PDF 字节级等同。

## 16965：Different Perspectives of Memory System Simulation

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16965v1)、[官方 HTML v1](https://arxiv.org/html/2604.16965v1)。必要定位：§2、§3.1–3.4、Listing1、Figure2–5。

不是“模拟器要验证”的泛原则：DAMOV 关闭 clock scaling 后将 CPU/DRAM 时钟混用，恢复后整数 `ceil` 比率又产生误差；Listing1 改为两域时间累计追赶。另一个独立问题是 ZSim Bound 阶段用一周期内存响应，已送进 memory simulator 的请求时序不能由第二阶段回补，因而错误重叠依赖访问；§3.4 用前窗 latency 反馈减小两相差距。这是内部统计不能代替 application-level 验证的具体反证。保留窄 memory/evaluation 贡献；仅实核 Skylake/ZSim/Ramulator 条件，未验证 LLM/GPU 实验，不把 §3.5 一般适用主张当既有硬件事实。

## 17053：Morality Attacks

来源：[官方题摘 v1](https://arxiv.org/abs/2604.17053v1)、[官方 HTML v1](https://arxiv.org/html/2604.17053v1)。必要定位：§3.1–3.2、§4.2、§5.3、附录 D.3。

四种攻击以 reverse/vague/fake/biased norm 引导 moral/immoral 判断。§5.3 ASR 计的是 gold ethical label 翻转；不等于被诱导执行一个原禁止操作。§4.2 用输入和生成结果两类 guard，D.3 确实补原始/定制原则对照，不能说完全没有 prompt 控制；但这些仍属于既有 norm-framing/persuasion 的任务压力测试，没有在必要段落分离新的权限或安全执行失效机制。故关闭，保留理由而不采用其高 ASR 的通用 jailbreak 外推。

## 17240：CAMCO

来源：[官方题摘 v1](https://arxiv.org/abs/2604.17240v1)、[官方 HTML v1](https://arxiv.org/html/2604.17240v1)。必要定位：§IV-B、§V-A Algorithm1、§V-B Theorem1/Proposition1、§VI-A–D。

文中已经区分连续凸 projection 与离散 minimum-edit constraint search；不能说它完全忽略离散动作。Algorithm1 显式最多 Kmax 轮后返回 fail；Theorem1 的有限终止并不证明 Kmax 内找到可行解，risk 单调还另需 agent 对 multiplier 单调响应，安全 fallback 的全状态可行性是所设假设。三类企业模拟不足以建立一般 OPA/policy 编译正确性。尚未分离出比既有 shielding、风险惩罚、有限重试新增的重要成立条件，故关闭；不把法规、零 violation 或 theorem 命名当贡献。

## 交接与验收边界

- 七项的最小准入疑问已实际收口；建议作者将五项写为具体 pre-denominator closure，两项只沿上述窄分支推进。
- 已核当前官方题摘和必要 HTML；没有因后续修订默认做前后全文对比，也没有把 URL/version label 当无污染的绝对证明。
- 未阅读目标 Books 命题，因此没有声称 Existing Coverage、已 Integration 或无需修改任何章节。
- 本文件仅构成这七项的独立消歧证据，不证明 Apr21 来源完整、全部题摘完成、分母冻结或整日 Gate 已通过。

## 第二批：六家族准入与保证边界

本批再次核对当前 AGENTS、Research Contract、Report Contracts 和统一 Prompt；实际读取以下六项官方 v1 完整题摘、版本 history、撤回提示及解决疑问所需 HTML 方法和评价。仍使用首批窗口，不将 `Submitted` 字段改写为 first-public。没有发现这六项的官方撤回提示；没有遍历附件或完整修订史。17121、17104 官方 history 有后续版本，本批只读取显式 v1，不用当前最新正文替代；URL 标签本身不是字节级无污染证明。

| 家族 | 独立准入建议 | 可采用边界 |
| --- | --- | --- |
| 16615 | 保留窄潜在贡献 | 音频通过 pooled context 条件化 rank-space posterior，是 feature fusion 之外的具体适配分支；不采用已校准可靠性保证。 |
| 16657 | 保留窄潜在贡献，与 16615 明确关联 | frame-level cross-attention 形成 per-token posterior，不能当成同标题重复，也不能当成独立校准复现。 |
| 16677 | 前分母关闭 | QR reranking 加成熟 CP/SMD 应用未分离新有效性机制；尤其不采用 action-selection 后的安全/覆盖保证。 |
| 16686 | 保留窄潜在贡献 | 在 continuous contrastive tilt 外增加复制 no-context logits 的条件性硬回退；不是识别 gold correctness。 |
| 17121 | 前分母关闭 | 对已有 state-tracking/recurrence 结果作 taxonomy 和议程整理，未提供新的下界或解决具体分歧的新综合证据。 |
| 17104 | 保留窄潜在贡献 | tensor bit-sketch、压缩比例预测和在线 base reassignment 是具体存储规划分支；不以纯内存吞吐推生产 I/O。 |

### 16615：CoCo-LoRA

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16615v1)、[官方 HTML v1](https://arxiv.org/html/2604.16615v1)。必要定位：§2.2 Eq.2–13、§4 Table2–3、§5。

与原 C-LoRA 只用本层 low-rank text feature 不同，pooled audio 一次映射成共享 context，再经 layer heads 进入 Gaussian posterior 的 mean/variance；随机性留在 rank×rank latent，而不是完整 LoRA factor。这直接改变外部模态如何进入参数适配，不只是在临床分类头拼特征，建议保留窄机制。表中主要是 segment-level 五折 AUC，不能证明概率校准或噪声增强时 uncertainty 必单调增加；§5 也承认 rare-positive labels 可由 fusion baseline 占优。mean posterior 与 Monte Carlo averaging 是两条成本不同的推理路径，不能统称免开销。

### 16657：CALIBER

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16657v1)、[官方 HTML v1](https://arxiv.org/html/2604.16657v1)。必要定位：§2.2 Eq.3–15、§4 variants/training protocol、§4.1 Table3–5。

作者与 16615 相同，但这里的 query 来自 token low-rank feature，keys/values 来自 audio frames；posterior 是每层每 token 的 rank-space latent。CALIBER-G、X、shared-KV 给出全局 context 与局部注意力的具体设计对照，因此不是仅改论文标题；也不能把两稿计作独立研究团队的重复验证。推理用十次 stochastic passes，五折 speaker separation 与 AUC 可支撑受限任务比较，不支撑 calibrated confidence；也没有证明这种 conditioning 总比 fusion 好。保留局部/全局条件化这一分支，不把 attention posterior 改写成零成本或可识别所有 acoustic uncertainty。

### 16677：ReconVLA

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16677v1)、[官方 HTML v1](https://arxiv.org/html/2604.16677v1)。必要定位：§IV-B Eq.5–10/Algorithm1、§IV-C、§V-C/TableII、§VI-A。

校准残差为 true error 减 QR prediction；Eq.6 却取 `Quantile_alpha`，同段定义 alpha=0.1 为 miscoverage，并声称 90% upper coverage。这个方向与该 residual 的 upper-tail correction 不一致，不能照录 finite-sample 保证。此外 Eq.9 各候选加相同 q，Eq.10 argmin 排名与未加 q 完全一样；TableII 没有 raw-QR/CQR 对照，选择收益不能归因于该校准常数。普通单样本 marginal coverage 也不能自动转为 selected action/整条相关轨迹的安全。现有必要材料仍为成熟 QR ranking、CP 与 SMD 的 VLA 应用，未分离重要新条件，建议关闭；不是因 VLA 或负面证据而排除，也不为这篇的错误保证自动扩池。

### 16686：No-Worse Context-Aware Decoding

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16686v1)、[官方 HTML v1](https://arxiv.org/html/2604.16686v1)。必要定位：§3.1–3.3、§4.1–4.4、附录 B/C。

低 JS 与 no-context top-1 margin 同时满足时复制 no-context logits；否则用 context 或 contrastive fallback。这是 continuous tilt 外的明确条件性硬回退，保留。其同 token 保证只比较共享当前 prefix 下的 greedy argmax；整序列等同独立 no-context 输出须每步均走该 gate。margin 大不等于答对，JS 小也不证明 context 无信息。附录 B 明示 8B controlled slices 调阈值没有单独 heldout dev；阈值迁移至另外两模型不能补成该 8B 的独立验收。两路 forward 的成本及 helpful-context 过度回退代价仍须保留。

### 17121：The Topological Trouble With Transformers

来源：[官方题摘 v1](https://arxiv.org/abs/2604.17121v1)、[官方 HTML v1](https://arxiv.org/html/2604.17121v1)。必要定位：§2–5、Table1/Figure4–5。

§3 按 recurrence axis 和输入/循环比例区分 architecture；§4 明确 lookup 不等于 dynamic state，并保留 lookback、parallel parity 与 CoT 等 workaround；不是简单声称所有 feedforward 模型不能跟踪状态。但 serial-capacity、linear SSM expressivity 与深层 state accessibility 依据均来自已列引用，§5 主要提出研究方向，没有本稿的新下界、原始实验或可解决具体知识分歧的综合条件。建议前分母关闭；不因综述标签拒绝，也不把原文的无限动态 state 表达性讨论外推为当前 Transformer 一概失效。

### 17104：TensorHub

来源：[官方题摘 v1](https://arxiv.org/abs/2604.17104v1)、[官方 HTML v1](https://arxiv.org/html/2604.17104v1)。必要定位：§4.1–4.4/Algorithm1、§6.1、§6.2.2 Table3、§6.3–6.4。

TensorID 处理 exact dedup，TensorSketch 估计 bit-Hamming 相似，TensorPred 不先 materialize delta 就预测比例，FlexSplit 根据新 arrivals 提升成员为新 base，并计入 full base 的容量代价。由内容/压缩收益而非仅模型家族决定物理共享，是具体增量。实际读了 Ch59“物理共享不能合并逻辑模型身份”，当前正文已有 family/delta 与恢复边界，但没有这个 sketch→prediction→在线拆簇分支；这只是增量定位，不是已作 Books Decision。ZipLLM 对照本身也可用 bit distance，不能称旧方案全依赖 metadata。Table3 明确 192 threads、全内存、无 storage I/O；不能推任意 Hub 的下载 SLO、I/O 吞吐或无损可用性。

### 第二批交接

六项必要准入疑问已完成实际复核：四项保留窄潜在贡献，两项建议具体关闭。结合首批，本文件覆盖十三项，但没有审查全日候选或所有 Books；尚未冻结分母、确证首发落窗或验收整日 Gate。作者依据上述证据作最终裁决，已读且未变化的必要段落可以复用，不因此再遍历附件。

## 第三批：六家族必要证据与准入校准

再次对照当前 Research Contract 的贡献入口、必要消歧和证据边界，并实际读取作者本批 Screening/Evidence Notes。实际核六项官方 v1 完整题摘、history/撤回提示与下述必要正文；未发现六项撤回提示。16349、16358 有后续 v2，本批使用显式 v1 材料，不把 URL 标签当字节级无污染证明。保留官方提交字段，不由其推断 first-public，也不宣称六项均已确证落窗。

16322 使用官方 PDF 的方法与评价；16363 在 HTML 不可读后，使用作者从官方 PDF URL 恢复的 `/private/tmp/apr21-16363-v1.pdf`，实际抽读 PDF 页 3–8（§3–5.3）。没有读取其全部 54 页附件，也没有把原摘要升级为全文审阅。16322 的网页截图尝试失败，未声称完成视觉验收；下述判断只基于可读正文、公式和表格文本。

| 家族 | 独立准入建议 | 需要落实的限定 |
| --- | --- | --- |
| 16320 | 保留标准级窄反证，非通用机制重写 | canonical 高分不等于新输入实例可靠；输入 mutation 与 MPT 是分开实验。 |
| 16322 | 保留标准级条件化 curriculum | 累积 witness/checker 拥有可行性，actor 拥有难度/停止信号；有限测试不是全语义证明。 |
| 16332 | 保留具体训练切片反证，支持作者继续窄 Books 判断 | 四 encoder 有 FullFT 对照；两个 decoder 只有 LoRA。不能外推为全部模型的 rank 因果定律。 |
| 16349 | 保留标准级动态评估案例 | execution-time oracle 与 repaired workflow revision 是具体对象；已有一般合同不等于所有实现均已有覆盖。 |
| 16358 | 保留窄训练机制，不因 safety 标签自动扩审 | prefix min/mean 影响全轨迹回报，不提供逐 token 因果信用或硬安全保证。 |
| 16363 | 保留标准级 query-only lineage 机制 | Beta 对象是有限 probes 的归属频率，不是未知模型身份后验或所有权证书。 |

本批六项均有可辨认的窄机制、负面证据或评估对象，未发现需要用“成熟模块组合”整体关闭的充分依据；也不因此把六项都升为 Deep Analysis。作者现有 5/5/6/5/6/6 分数可在上述边界内采用；16332 因具体 Books 缺口进一步审阅合理，16358/16363 的安全相关性本身不是强制深审证明。

### 16320：实例扰动不等于函数等价变换

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16320v1)、[官方 HTML v1](https://arxiv.org/html/2604.16320v1)。必要定位：§3.1、§4.1–4.2 Table1–3、§5 Table7、§5.1。

输入 mutation 产生新执行实例，必须重新执行取得答案；MPT 只改变代码，且只在原输入核输出相同，不是全域等价证明。两类分别测，联合干预仍是 future work。684 程序各十个有效新输入的 PSR 与 canonical accuracy 区分出具体可靠性缺口；异常 any-match、substring 和多个断言任一正确的 extraction 是宽松 oracle，不能据此判世界模型存在与否。异常提示又可能损害正常输出，不能称无代价修复。实际对读 Ch66“动态知识系统需要关系型回归”已有关系验收/独立 gold/版本边界，可支持只报告受限代码反证，不证明本稿所有条件均已在书中。

### 16322：可解性 Witness 与难度 Actor 是两个接口

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16322v1)、[官方 PDF v1](https://arxiv.org/pdf/2604.16322v1)。必要定位：PDF 页 3–5 §3.2–3.4 Eq.2–8，页 6–9 §4.1–4.3。

Schema 含参数与 AST checker；新增约束时先更新 witness，要求所有旧新 checker 加 functional tests 通过，再用 actor 的两类 pass rate 决定停止或继续。后续 schema composition 使用状态转移统计，mutation 另验 positive witnesses，因而不是自由改写文本的同义包装。成立条件仍是 checker/test 充分性，actor failure 不证明难度普遍成立；三代指标也非全部单调。实际对读 Ch27“Coverage Contract”已区分可验证 composition、policy difficulty、独立 verifier 与 lineage，因此标准级具体案例合理；不把已有原则覆盖冒充全部 sampler 已覆盖，亦不采用有限 n-gram 无重叠证明无泄漏。

### 16332：有用反证不需要升级为普遍因果机制

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16332v1)、[官方 HTML v1](https://arxiv.org/html/2604.16332v1)。必要定位：§3.1–3.3、§4.2 Table2、§4.3、§5、Limitations。

100 人标注分布是外部 disagreement，不是模型 uncertainty；训练样本的 weighted loss/AULC 与任务质量仍须分别解释。四 encoder 有 FullFT，decoder 仅 LoRA；IA3 只在 RoBERTa/SNLI，因此不能写六模型都经相同 FullFT/IA3 控制。MNLI 效应减弱，存在多重比较不显著与缺 seed；梯度/校准机制分析主要单 seed。§5 的 soft-label 对照仍出现 loss 上升，也使“只改成软标签就已解决”不成立。实际查 Ch30 rank/loss 条件与梯度重耦合段，未见这条 disagreement×逐样本轨迹反证，支持窄补充；提高 rank/改 loss 是待验证选择，不是已证明 remedy。

### 16349：动态真值不能只靠 workflow 没报错

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16349v1)、[官方 HTML v1](https://arxiv.org/html/2604.16349v1)。必要定位：§3.1–3.3、§4.1 Figure4/Table2、§4.3 Table3。

相对日期在执行时解析，再从实时 DOM 取答案，区别于定期刷新固定 answer；生成 workflow 先文本/截图对照并人工初验。Repair 由 runtime error/null 触发，不能检测所有静默语义漂移；复用 L1 oracle 的多 hop 样本也不是独立真值来源。Time-anchor 对照更换测试日期，不能把变化全归因于补 anchor。实际对读 Ch66 run identity、snapshot 和 repaired harness version 已承载一般边界；这支持标准级案例 No Change，却不证明当前章已有 execution-time relative-date oracle 的全部实现细节。

### 16358：训练 shaping、评价阈值与安全保证分账

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16358v1)、[官方 HTML v1](https://arxiv.org/html/2604.16358v1)。必要定位：§4.4 Eq.17–21、§5.1、§5.3–5.4 Table5。

Tutor 同时产下一攻击和评分；prefix minimum/mean 再求 trajectory return，统一 advantage 更新整条 assistant tokens。它不是把晚轮失败逐 token 因果归属给早轮，Eq.18 的历史 s 指代也须谨慎。TCSR/feedback 去除有受限消融，可保留新 shaping 分支；共享 judge 误差、长短轨迹 return 比较及阈值评价仍限制解释。十轮内 right censoring 不证明无限安全；turn-average threshold 不是所有 turns 均安全。未独立读 Ch33 目标命题，因此不声称已有覆盖或必须 Integration；不因标题 safety 自动扩大附件审读。

### 16363：行为分布归属不等于法律身份

来源：[官方题摘 v1](https://arxiv.org/abs/2604.16363v1)、[官方 PDF v1](https://arxiv.org/pdf/2604.16363v1)。必要定位：PDF 页 3–8 §3–5.3，尤其 §4.4–4.5 Eq.6–12/Table1。

无需预埋 watermark 的 query-only 组合欠指定 prompt→CLIP 类别分布→Wasserstein 最近 base 是实际探针分支；六 families/十三 variants 不覆盖未知 lineage。Beta(1,1) 加每个 candidate 的 probe 归属计数，估计的是投票比例，不是归一化模型身份 posterior；95% credible interval 亦非已校准 OOD false-positive contract。prompt 独立与组合稀有保留行为是条件，不是任意微调/自适应服务保证。实际对读 Ch59 行为指纹段已有 query budget/reference/测量 revision 与“不是所有权证书”，可以只报告窄 T2I 实例，无需重复同一保证；没有独立重做实验。

### 第三批交接与范围

六项已完成上述必要消歧；16363 从摘要受阻推进为同版必要主文可读，未继续恢复附件。只建议标准级或具体缺口审阅，不重新扩大候选池。累计本文件 19 项有界复核不等于 19 项完整全文审阅，更不等于 Apr21 全日 Gate、Books Integration 或来源覆盖验收。作者仍负责日期身份 reconciliation、全部候选终态、必要 Books 落地与最终独立验收。
