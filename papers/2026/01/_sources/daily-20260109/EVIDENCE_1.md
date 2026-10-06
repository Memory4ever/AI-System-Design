# Jan09 第一批必要证据与 Books 对照

root实际非作者必要原源与具体owner复核：03368/03425标准完成、具体Existing通过；03385/03417标准中心子命题终态暂缓通过，描述性/有效实测不全部否定。03468原6针对具体长期gap深入受影响原源，Ch31:849正文/前后衔接与1208源注已root实际POST通过。无代码运行/复现，日级Gate仍未授；以下提案文字保原审阅过程，现终态以此段及正式README为准。

## 2601.03468 — 2+2+2=6

实际核 §3.2–3.3、§4、补充 §6 APO、§7.2–7.4。同 Janus-Pro-1B/T2I-R1 数据、3 epochs≈3000 steps 对比reward组，单一与HPS+GDino均有局部结构artifact盲区；不是所有结构/模型/ensemble都无效。人判构造同prompt的 artifact/free paired diagnostic：Table2各行202对，GDino/ORM大量tie，不是完整真实部署artifact流行率。Qwen2.5-VL-7B APO学prompt，ArtifactReward为 pNo/(pNo+pYes) 二标签归一，不是校准真值或all-output概率；§6把 D 标training dataset、用gold反思/筛prompt，但必要段未明其与202诊断对的独立切分，故不授Table2 detector out-of-sample准确性。WISE GPT4o composite、LMM4LMM/EvalAlign是额外proxy，不能合并human gold。Table7 HPS/HPS+GDino加Artifact后All并非每组改善，故仅保条件补充信号，非quality全维提升。新增7B视觉判别/APO/标注及训练调用均有预算，必要段未披露完整hardware/precision/concurrency，不授端到端降本/ServingSLO。

当前实际 Ch31:207–217 有mean掩盖must-have失败，Ch31:827–847有独立evaluation/共享RM漏洞，但尚未具体承载“多个功能不同的reward共同漏掉未被各自判据覆盖的局部结构”；这不是aggregate weighting即可恢复的错误。拟 TRAIN-RLHF / Ch31 Evaluation节独立RM段附近一窄段（6分确认此差异再深入受影响§3/4/6/7）：ensemble数量不授覆盖，固定同prompt人判artifact对分别测reward tie/排序与未被优化的结构维度；artifact detector仍proxy、标签独立切分/校准/预算另付，不授消除hacking，回退独立人审/受控样本与保守训练。拟段不放Table2准确率或全域成功结论。等待 root 原源/实际owner判断与写锁，尚未整合。

精确版本均为 v1；公开区间原值见 DATES_1/2、DATE_BASIS。以下不声称代码核验、复现或完整附件审读。root 已校准准入与原分数，必要证据/Books 处置另待核。原文缓存 NECESSARY_CORE_1_RAW.txt、NECESSARY_CORE_2_RAW.txt 按原 HTML L 编号保存；缓存只含必要片段。

## 2601.03368 — 2+1+2=5

实际核 §1.2、§2 假设与式2、§3.2/§4、AppA/B。BPE 每次一对合并改变 slot 总数与事件空间，式19的 count/slots 边际 Shannon entropy 不能直接当原文整体信息量；§4.1 还区分预测 softmax entropy 与实际生成样本边际 entropy。有限 Zipf 模型与 IID 假设是分析条件，不因局部 attention 观察成立；raw QK 阈值/attention 观察不证明独立性或模型功能因果。AppA 是 6-block、256 hidden、128 context 的 GPT2LMHeadModel 受限实验，output/embedding 随 BPE 词表 resize；必要段未披露完整优化器/硬件/训练计算，故不采同预算全模型优势。AppB 语料统计可合并 IMDB train/test，但 GPT2 训练评价另划分，不能混为模型测试泄露。

提案：标准完成，具体已有覆盖 MODEL-TOKENIZER / Ch11:214–234。现正文确有同原文而不同输出分词→监督事件/条件路径/loss人口不同，以及 tokens 非跨 tokenizer 固定分母、byte/information denominator 与 execution shape 分账。该书稿承载本次统计单位改变后的设计判断；**不是说已写 Zipf entropy 公式、IID 或本论文 attention 论证**。局部 entropy/Zipf 结果保留报告，不增加正文。相邻 Ch10 小结/Ch12 入口已核。

## 2601.03425 — 2+2+2=6

实际核 §3.1–3.4、§4.1–4.3、Limitations。读取 prompt 最后 token 的 pre-Top-k softmax routing vector，按 domain ECI 均值/rank、候选跨 domain 频率与 mean/variance Pareto 选择 group；这既不是最终 top-k 实际计算占比，也不是功能因果。三个公开 MoE、MMLU 57→9 domain 的推理观察发现共享高 mass group；OLMoE 改 k 后 retention 明显改变，selection protocol 与 routing width 要绑定。作者自己明确未干预 expert、未测训练 dynamics，故不采语法/推理锚点因果或 load-balance 有害推断。必要机制不需 artifact 复现；performance/ServingSLO 不属于此观察评价。

提案：标准完成，具体已有覆盖 MODEL-MOE / Ch21:630–682（功能 identity 需行为/干预；routing 偏好不等 deployable subset；domain selector/objective 与 overlap 各有权限）。本次 group selection 的受限反证可报告，但不能把 committee 统计直接授裁剪/专家更新或修改 balance。不是宣称书已有本文 Pareto algorithm、Jaccard 数字。无需重复写正文。

## 2601.03385 — 2+1+2=5

实际核 §2–3、§4、AppA、C.2。M=[A,B]，Gram 加和允许确定性 PSD logdet envelope；β=maxeig(B) 本身未知，列范数上界ρ给 βhat=(n−nA)ρ；regularized partial logdet 的描述性轨迹是另一对象，不因 CI 冲突全部删除。LLN 路径需固定 m/iid 等；AppA C=E[vvᵀ] 与正文 covariance 在非零均值下需区分。主文式3.9 σ=Var(XᵀCX)，式3.10/14以σ作 std；AppA 用 XᵀC⁻¹X 并写 σ²=Var。m=1,C=1, Gaussian 时 Var=2 与 std=sqrt2 不同，**仅隔离原 CI/accuracy 保证及据此配置 sample budget；不判所有描述性 proxy 或实测无效**。

C.2 实际：OPT125M，FP16，5 epochs/generation，batch16，lr2e−5，AdamW wd.01；α=0纯 synthetic、64 train blocks、域冻结 prompts 163–200、51 checkpoints、all-MiniLM-L6-v2 384 embedding、δ1e−3/ρ1、固定观察列。n<384 的 regularized Gram 仍可计算，不能借此授全秩 theorem，不断言实现必错。S1 每代 reset、S2 carry weights，但各自用前代 generator 数据，不是两组每代同数据只变 weights 的纯因果实验。两条轨迹有不同/不一致方向，不作普遍 collapse 检测；无 PPL/独立生成质量关联审计，不授 proxy 替代质量。

当前对照 MODEL-EMBEDDING / Ch12:290–314 已实读：几何 estimator、样本/距离/分析对象及读数 vs 数学量 vs能力分责，cheap curve 只定位变化、独立任务验质量。提案：描述性双轨 proxy 标准受限报告，不能重复成熟几何合同作增量；CI 精确冲突保留暂缓子命题，root 决定该 family 的安全终态标签。原分不变，不以争议删候选；若中心需要 CI 才能满足论文核心 accuracy 承诺，则 Books 暂缓、不写。重开只需作者更正式3.9/3.10/14与AppA的对象/方差参数及对应置信实验，不读全数学附件。

## 2601.03417 — 2+2+2=6，必要机制有精确训练权限缺口

实际核 §3.1–3.3、§4.1–4.7 与 Limits。1024 chunk/128 overlap、每 chunk 最多32 triples、global150 edges；同时存 materialized E 与 latent Embed(h,r,t) U，query bilinear hard-top30选择后仍 string serialize 给 frozen reasoner。故 latent retrieval 不等隐式唯一存储或原始事实权威。StageI CE 经 Extract/StringSerialize 指向 builder；StageII TopK STE 只说明 hard selection 的 surrogate；StageIII alternating retriever/builder。但正文未给离散 triples extraction / string tokenization→frozen F loss 到 builder 参数的 tensor/surrogate 路径，TopK STE 本身不补该接口。**隔离 builder QA-gradient/联合训练机制归因，不宣称所有实验或实作必错**；作者精确 surrogate/grad path/相应训练结果可定点重开。

评价：20,800 train QA 与2600 held-out任务、builder/retriever Qwen2.5-1.5B LoRA、跨 frozen reasoner size；NarrativeQA并非所有指标最好。100 samples/长度的 Table2：6–10k ours12–14秒 vsMemGen8–15秒，不是每长度更快；top30读取不抹随context增长的construction或cap150遗失信息。核心未披露设备/精度/完整训练预算和并发，不授 ServingSLO。Ch77:805–817已有query读取预算 vs bank/provenance/facts分责，但不足解决离散 serialize 训练权限，不能用泛主题覆盖抹争议；暂缓提案待 root 必要原源核。
