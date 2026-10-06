# 本日贡献筛选依据（冻结74家族，日级验收通过）

本窗：2026-01-23 09～2026-01-24 09 BJT。AB1 的108条是按提交buffer、CL/LG/AI及模型术语取得的发现线索，不是108个公开事件或候选。完整摘要只有在贡献判断需要时读取；CV/DC月目录仅在ID15380～16220附近读取相关标题，不扩全月队列。API原XML当前comments轻量检查发现15423纠错信号。

有限来源发现已停止。108线索与61份exact-v1题摘并集134身份，61份exact题摘实际完整读，另外AB1的相关选择有已读完整摘要，但不称全部134已读。原冻结76在15812必要核心发现无新增评价边界后，由root原AB/核心贡献复核改为75；15914原完整题摘/§2–4进一步只旧预算原则的avatar实例，改为74。原证据不删除、不是成本降级。

15914 The Latency Wall：原准入假设是CPU视觉质量/延迟联合约束反侧。实际原AB和core58–80/121–148/177–217只是现成FER在avatar/human两个域的准确率比较和i7原配置五run平均；检测版本差额未控架构/训练，140ms外部预设而capture/render假设10ms。没有新增机制、特定失效成立条件或可改变本项目foundation/infra选择的可比反证；“目标域与latency共同测”成熟原则不计新贡献。root实际AB/§2–4指出此具体误判，作者复核原完整题摘与必要core后贡献关闭，原5分仅当时假设不作最终评分。所有exact/core必要读取保留，非医学/负结果一概拒，也不因为费时或Books覆盖关闭。

15812 ErrorMap/ErrorAtlas：原准入假设是wronganswer可来自format/calculation/data噪声而不是reasoning弱的具体新盲区。实际core §5.1/§6/Table3及limitations仅跨模型taxonomy/失败组成、Gemini4.8%差额分解和95.2%coverage/92% assigned-label-vs-random一致；没有新的评价失效条件或可控归因方法。root实际完整AB及这些必要核心确认，具体贡献关闭，不评分不Books；旧诊断原则、新taxonomy条目本身不计本日增量。所有已读exact/core保留，若出现控制性新证据只定点重开该差额。

## 首批独立校准

root实际读取原完整AB7项，5条拟准入链通过：15394（teacher知识/训练样本memorization不能泛化为普通隐私迁移）、15482（鞅valuation/prune须核假设）、15498（low-margin放宽验证不是lossless）、15593（generation-order依赖诊断）、15609（有限batch偏置）。初步校准不等于日期/证据/Books验收。

15390 FedUMM：完整AB中的LoRA-only聚合是已有通信比例收益；单BLIP3o异质性实验未展示新聚合机制、收敛或隐私成立条件，贡献排除，root通过。15457 RAG chunking：完整AB是既有RAG/rerank的局部总体faithfulness比较，没有token-vs-character具体新失效证据，贡献排除，root通过。不是按领域名称、成熟模块或仅局部实验笼统拒收。

## 必要修订信号

15397 LOGIC：root实际打开v1、v2与当前页；v1提示较新版本withdrawn，v2因内部机构publication approval暂时撤回；Sep v3/v4已恢复。按当前合同，本日不采用已撤回旧公开链v1、不评分、不进Books，仅保留必要排除依据；不称科研造假或整个family至今撤回，不用Sep恢复稿替代Jan事件。

15423 Lattice：v2 comments明确更正primary estimand、移除误导SOTA对比；原v1 transformer约0%来自invalid cross-backbone transfer，不能用于证明composition不帮助强encoder。只恢复受影响命题，不把May/June修订当Jan本窗事件。

root已定点实际读v1方法、协议、5.2–5.4和消融，许可贡献关闭：Kmeans距离percentile gate+Markov hybrid成熟组合，LSTM任务增益与shift零激活只是实现fallback；strong backbone0%反侧已无效，不能授OOD正确率、epistemic humility或任意模型安全。协议70/15/15与80/10/10不一致，进一步不支持强benchmark断言。已读core_15423.json保留，不因Books覆盖/费时缩池，也不展开无关Science/金融附件。

## 官方旧事件说明

Google Jan23 GIST博客核心已读。其Paper原文2405.18754 v1 May29 2024、v3 Oct20 2025；博客介绍同一MDMS目标、1/2近似、0.5584 hardness、ImageNet单次子集实验，并未新增机制或实验。排除本日新贡献，不请求不影响判断的博客精确时刻。

## 第一批证据边界

15482 MFS v1 §4.1–4.3、§5.1–5.5、§7和Appendix A实际读。V(a)条件期望由rollout估算，伪码直接F_t−F_(t−1)；剪枝阈值为均值+λσ，early stop ε=1e−6。正文没有给有限估计误差/校准条件下的正确性保留界；Doob分解与bounded submartingale convergence本身不证明confidence=correctness或永不剪正确解。可采用同beam/rollout条件下score和early-stop局部accuracy/FLOPs差异，不采纳provably converges to correct answer。Table3固定beam8、λ=.8替换score；两RTX3090、vLLM.9.1/PyTorch2.7、temperature.7。FLOPs=6nP估算，不是wall time/SLO结果；精度、batch、concurrency和输入输出长度Not Disclosed。不需要追全文参考文献或无关代码。

15498 MARS v1 §3.3–3.4、§4完整必要配置和ablation读。ratio=第二logit/第一logit，不是softmax probability ratio；接受runner-up draft，θ=.9。该ratio不对加性logit偏移不变，不授普遍calibration robustness；作者也明确lossy。H10080GB，<=32B单卡、更大8卡，K7/topk10、temperature1，与对应EAGLE3草稿同设置。HumanEval主accuracy指标pass@4、GSM8Kfinal EM；Table2 Qwen3-32B长草稿accuracy不单调，有真实下降。batch、precision、concurrency、长度、SLO Not Disclosed。采用近似质量/接受长度/成本条件，不写lossless guarantee。

15609 RLVR v1 Eq3/Th2.2/AppendixB存在中心推导争议：Jhat=Σ(N_i/G)A_i logπ_i−βKL(π||ref)，而所称闭式πhat∝ref exp(N_i A_i/(βG))并非该目标的普通驻点；对π的reward导数带1/π，AppendixB对w=logπ的KL导数漏π因子且未处理归一化依赖。已向root请求有限独立数学核验。不能授闭式有限batch定理、geometric interpolation或其下游semantic-coupling保证；并非因此降分/删反证。必要实验仍可独立核验后保留，不把中心争议变成论文无贡献。

root已实际重开15609 Eq3/Th2.2/AppB427–448并确认漏项；负c_i还可能令logπ目标无界。定点隔离Th2.2及其衍生保证，不扩全篇证明。实验独立核后才可采用窄经验结论。

root已实际核15394 PDFv1 §2/§3/§6、15482 §4/§5/Table3、15498算法/配置/Table2、15593 §4/§5/A7，四条窄经验采用通过。15593 A.2/A.3/no-slowdown理论隔离：j≠i影响系数忽略frozen位置的自依赖；L=1且无更新时α=0却是identity核，不具有唯一稳态/TV收缩。state-dependent选择也不由block-conditionals单独推出P*不变。仅保留一次product投影CTC恒等及AFP/τ局部诊断，不把隔离推成全篇冻结。

第二批root实际完整AB校准通过16208/16065/15906/16163/15678的窄增量，15867/16155具体排除理由通过。日期、后续证据与Books未授完成。

## 有限筛选尾部与日期归属

当前发现身份：AB1 108与61份exact题摘去重并集134，另Qwen原作者家族15621为独立定点线索；不含无效updated100，不含月库存所有条目。61份exact题摘完整读；其他AB1题摘仅本次相关选择已读，不声称全部108或134已完整AB初筛。冻结74，15645等必要准入已独立通过；普通待办0，最终日级Gate通过，外部日期/源缺段/中心争议保持精确隔离。

16027 CS-VAR：完整v1AB与§4.5 Eq8–10、§5.3实际读；teacher key-patch partial-view/full gold分责的view-matched平方loss是已知监督原则实施，w/oD移除全部蒸馏，没有global-teacher与view-matched直接对照或新增失效/可靠性条件。原增量是直播风险PatchNet组合配方/领域增效，不改变本项目LLM/infra选择；root实际定点读并通过贡献关闭，不因耗时、缺配方或Books覆盖关闭。所有原core保留。

15509 sentiment：完整题摘后决定准入的PDF Table1、§4–8已读。Table1含binary SST-2 DistilBERT head与未披露同任务head的BERT/RoBERTa/ELECTRA，18条作者business-insight gold、classwiseF1是成熟评价；没有head/label-schema/routing匹配控制来辨认新的Transformer neutrality机制。CSR routing与后续NLG不同条件不支持原systemic architecture归因。贡献关闭，依据point_qwen15509.json实际核心，而非未读/低可信度即删；root实际核Table1及§7，mandatory具体关闭通过，不采用结构性反证。

15669 Dualformer：root实际§3.1/3.2准入depth-specific QKV frequency-band读取，2+1+2=5；既有lowpass/rank collapse引用不计新贡献，harmonic lowerbound只series分解/L=mτ/λ>4，不给语言模型、causal attention或global high-frequency保留保证。

15621 Qwen3-TTS：初始commit d8146d5305c4291ec5b0b6533c0c1718fb276899 Jan22 09:57:04Z含assets/Qwen3_TTS.pdf；qwen_blob.json首页2026-01-22、同标题/团队/dual-track/25Hz/12Hz/5M hours摘要，水印submit7184591 Jan22。同稿身份支持早正文线索，但commit不是public push时刻，官方repo News展示Jan22无timezone，不确认01/23为唯一owner。终态日期隔离：优先核01/23，需News/同稿公开timestamp才重开精确首次归属；不授本窗确定候选/Books/覆盖正面，不阅读前日报或重跑旧窗口。

17063 FlashMoE：提交Jan22不是公开；date_17063.json v1 UpdatedJan27 01:01:54Z、registered03:41:11Z，对应更晚公告批次，移出本窗，留01/27恢复线索。2602.13214 BotzoneBench/13215 AMOR的v1 UpdatedFeb17 01Z、registered03:45Z；2602.15844 TaRL v1 UpdatedFeb19 01Z、registered02:32Z，均延后本窗，不因API的Jan21/22 submitted收入Jan24，留真实日期恢复线索。

Moonshot月级K2.5 release已经官方Kimi Help确认Jan27（bounded_lastdate.json），窗外，repo实际Jan30创建也不当发布时刻。MiMo Jan23日期补检取得的是Jan26计费通知，其发布日期Jan23仍只运营计费，不涉及研究机制/可靠性变化，范围关闭；不能当未定时blog历史全部恢复。

Hunyuan原bundle确切publicList POST一次403；Seed SSR242列表?page7仍首屏；三主题API429、updated100字段回传不匹配必要公告范围，均停止恢复，准备本窗精确终态隔离，不扩大队列。

15721 CoNRec：完整原AB已读，root实际核原摘要。next-negative-item目标被推荐顺序污染、未来多日反馈改变reward，是既有推荐曝光偏差问题的领域target/reward调整；未指出新的LLM评价失效机制或可迁移控制边界，具体贡献关闭，不以推荐领域名称排除。

15645 Confidence评估：root实际核完整AB及信息梯度核心，准入窄5分：单次完整信息静态confidence排名不能外推逐步累积证据。作者实际§3.1–3.3/§4.1–4.4，六量级同病例，三数据171/231/181，accuracy/confidence相关及AUROC/AUPRC分责；信息顺序/随机采样/多seed控制未披露，不宣称概率校准、缺信息的因果效应或主动澄清可靠性。医疗RAG配方不计新增。

15664 UniPic3：root实际核§4.3直线FM连续CM、有限差分及配置，窄2+1+2=5准入通过；latentconcat继承不计原创，100→8仅步数不是同质量walltime；组件缺消融保留。15676 CoFi：root实际核门控/MMAR1000/RTX6000表及失败边界，窄2+2+2=6标准证据通过；所有请求cloudgate、62%是tool比例，不授端侧部署或校准置信。
