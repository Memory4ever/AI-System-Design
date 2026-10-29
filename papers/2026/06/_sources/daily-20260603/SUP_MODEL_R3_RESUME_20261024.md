# 06-03 MODEL R3恢复：四身份校准与两篇必要采用

作者：jun03_model_r3；2026-10-24。仅06-03补Jun02 BJT；root唯一本轮Books/Report/State writer。本文件不冻结原73提案、不重做已完成首四、不扩其他日期/来源。旧字段与有效层不迁移。

启动已读AGENTS、Research/Report合同、Sources使用说明/每日与arXiv恢复、Prompt、完整ROADMAP、State仅2026相关块、原MODEL尾部R3。Books判断前已读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE及下列实际owner/邻接。四份完整v1题摘/history复用[原JSON](SUP_MODEL_V1_ABSTRACTS_20261023.json)；RCSP决定性旧有效片段复用[CALIBRATION](SUP_MODEL_CALIBRATION_20261023.json)。新完整HTML仅为必要域可复查原件，未声称全文/全附件读完。独立准入校准已由jun03_resume_reader消息确认两入/两排，正式记录在同日该reader复核文件R2；未自签Evidence/PRE/POST。

## 1. 四身份准入校准

- **2606.00869 CPT：入。** 直接response-side abstention示范可能提高拒答却伤answerable保留 → 原文用含reference的四类trace pair比较作policy自身的NTP监督、之后回到无reference生成，并与相同后续math RL的SUM-SFT比较 → 应把外部比较、生成时拒答和answerable保留分别验收。增量不是pairwise/SFT新颖，更不是已证明内部元认知circuit。原“internalize质量边界”过强，采用下述限定命题。
- **2606.00919 RCSP：入，撤销原close。** 固定多目标权重不说明时间路径是否影响拒答/事实取舍 → 同冻结backbone软接口的fixed μ与scheduled μ消融给出具体局部差额 → 除监督目标和可训练面外还须验目标权重的训练路径。不是因loss组合/参数少/排行榜准入。原close撤回依据是新增决定性Eq2/T4，而非工作量或Books结果。
- **2606.00947 Silent Failures：贡献前排除，不评分。** 完整v1AB给taxonomy/benchmark landscape和研究议程，未呈现新的检测实现、具名行为监测失效验证或足以修改现有设计的实证反例。隐私可见性限制是背景，不能重命名为新机制。没有相关撤回/纠错信号；日期非决定项，不另追日期。
- **2606.01800 Multilinguality：贡献前排除，不评分。** 完整v1AB描述资源组结构距离与posttraining后语言关系保留；未明确挑战哪个表示假设，或何项设计选择与成立边界因结果而改变。不是因为描述性分析天然无价值，而是本AB尚无具体项目增量，不凭Ch5可路由即收；无相关纠错信号，日期非决定项。

以上仅校准本四项。原MODEL其余队列、共同错误理由的受影响范围与官方模型补检留原停点，不冒此处已处理。

## 2. 2606.00869 CPT：必要Source与唯一owner提案

[exact-v1](https://arxiv.org/html/2606.00869v1)；[本次HTML原件](SUP_MODEL_R3_2606.00869v1_20261024.html)自标`arXiv:2606.00869v1 [cs.LG] 30 May 2026`。读§3–5全部必要定义、Table1–3/§5.3与§4.4配置；没有核代码、复现、整理论附录或所有benchmark审计附件。

日期沿有效联合证据定点复算：[v1题摘history](SUP_MODEL_V1_ABSTRACTS_20261023.json)唯一v1提交May30 19:53:19Z，正常最早公告Jun1 20:00EDT=Jun2 08:00BJT；[DC query原件](SUP_MODEL_DATACITE_20261023.json)第11行`requests[0].links.self`原请求URL带`client-id=arxiv.content`（reduced data对象本身不含client字段），同精确DOI findable、registered=`2026-06-02T04:01:46Z`即12:01:46BJT。整个最早/最晚区间位于Jun02，沿当前合同的发号规则限定公告日，不把registered叫实际公开时刻，也不证明全球无更早稿。当前history另列v2，不拿v2新增内容回填；无已见撤回/勘误标签。

**评分2+1+2=5，标准必要域完成，具体采用差额深入到训练/部署条件与直接反侧。** D2：reference-conditioned trace comparison到无reference生成的替代监督接口；R1：同policy后训练与生成行为局部；D2：监督权限/迁移与coverage取舍可复用。不为成熟pairwise/NTP或能联想到安全章节加分。

§3明确pair输入是problem、reference answer、两条reasoning；输出短comparative analysis和four-way label，标准next-token SFT。四类含双方同好/同坏，intra/inter/small-correct-large-wrong及随机换位减少model size、长度或答案捷径；这是作者设计意图，不认证捷径消除。下游只给problem，不携带reference或pair，没有额外独立verifier。§3.2关于external→internal的解释明确依赖generations与外部trace接近/criterion稳定/后续RL drift受限，不采用它为已识别内部circuit或保证。

§4–5：Qwen3-4/8/14B，Llama3.2-3B-Instruct，Olmo3-32B；32B只有midtraining无math RL，不能与Qwen的后RL因果合并。CPT约70K比较实例、标准math-SFT/math-GRPO，verl/FSDP/gradient checkpointing/vLLM；GRPO group16、temperature.9/top-p.95、max response12288、lr1e-6。拒答一个greedy rollout，math多样本temperature.5平均accuracy，rule/semantic后GPT4.1-mini fallback。训练hardware、precision、完整总算量/全部搜索预算未由所读必要域完整披露；不作服务batch/concurrency/SLO性能保证，亦非复现实验。

§5.3的SUM-SFT+RL用23K可拒答teacher-CoT+57K answerable math实例，与CPT同后续math RL；SUM的拒答F1更高却Precision/answerable accuracy更低，证据只支持有限训练配方中的utility取舍，不是所有response abstention训练必然overfit。实例数接近不等同teacher/rollout/token预算相同。T3 4B NormalF1低于SFT80K，3B在math和NormalF1均不及SFT80K；不能称跨scale全面优。AB headline的+5.2 F1与T3的60.8→66.4(+5.6)不齐，不采用精确headline，也不因非中心数字差推翻所读接口。后续保留独立回归/原checkpoint为项目推导。

### Books实际比较与逐字PRE（尚未写）

唯一owner：`TRAIN-SFT`，Ch29 [29-sft](../../../../../books/part-04-training-system/29-sft.md)“恢复训练可看见失败历史，但不模仿失败动作”末端。当前原文已有single-trace yes/no自评、失败路由与校准不等价；尚无含reference的four-way pair监督→无reference生成/后RL及SUM拒答覆盖对照。Ch34拥有logratio preference objective，不接管普通NTP；Ch31拥有后续reward，非本次比较监督owner。已读Ch29该小节完整组及前后节，Ch28/30开篇与Ch30 objective边界；不创建新小节或附录摘要。

上锚（完整直接前段，含原marker）：

> 失败文本还有第三种角色：不成为 reasoning 的模仿目标，却作为判断该尝试是否正确的条件。先由外部任务验证器给当前模型的轨迹打标签，只把成功轨迹送入 reasoning 监督；所有成功与失败轨迹则转成“题目、该尝试→yes/no verdict”的评估监督，与生成任务共同训练同一个模型。这不同于前述 expert-only 恢复 loss，也不等于对错误前缀做全 response NTP；成功样本承担生成与 yes 两个任务，失败样本只承担 no 判断。推理后同模型的 yes/(yes+no) 是指定 prompt 与 logprob 接口下的 confidence readout，不是外部真值或独立 verifier。[受限迭代 SFT 对照](https://arxiv.org/html/2601.06786v1)中，排序能力与绝对概率、OOD 校准并不一致：部分 Llama1B 的 ECE/Brier 比基线更差，Qwen8B 的 GSM8K ECE 也退步。额外 K 次采样、外部验证、自评任务、温度/模型合并搜索及部署自评调用全部计费，不由少量样本或更好 AUROC 推同总预算。标签不可靠、成功样本稀缺或共享任务互相干扰时，保留 verified correct-only、独立验证器或不附加自评；这里仅采用成功/失败的数据路由，不补未核的逐 token loss、完整调参 recipe 或普遍消除 collapse 的保证。<!-- source-family:SF-2026-ARXIV-2601-06786 -->

拟新增完整一段（root唯一writer，待独核）：

> 比较监督还可以让同一policy学习“题目、reference answer、两条trace→短分析与四类相对质量标签”，包括双方同好或同坏，而非把偏好pair直接交给DPO。训练可借reference和外部teacher，部署却只给题目、由模型自己生成；因此外部trace比较正确不等于生成时已具可靠自评。[受限比较训练对照](https://arxiv.org/html/2606.00869v1#S3)中，response-side拒答示范可得更高拒答F1却拒绝更多answerable题，pair监督也在小模型或部分指标落后普通SFT。应同时验有/无显式拒答指令、可回答题保留及后续RL后的行为，不由F1或假设性boundary解释签发内部元认知保证。多模型rollout、teacher比较与过滤、额外SFT和后续训练均计费；标签或迁移不可靠、能力回归时，保留verified demonstrations、独立任务验证与原checkpoint。<!-- source-family:SF-2026-ARXIV-2606-00869 -->

下锚（完整标题及直接首段）：

> ## 为什么少量高质量数据也可能有效
>
> SFT 通常不是从零创造语言能力。Pretraining 已经形成大量表示与生成模式，SFT 的任务更像是选择、组合和稳定目标行为。

本次不声称已整合/POST。

拟本人Review note（待独核、root写）：

> - `SF-2026-ARXIV-2606-00869` — Daily2026-06-03补Jun02；exact-v1 §3–5/T1–3/5.3必要域，2+1+2=5。仅reference-conditioned four-way比较NTP到无reference生成的权限/验收分责；保SUM更高F1但过拒、3B/4B反侧、实例数非全预算与全部费用，不采headline不齐数、普遍内部元认知/circuit或完整理论保证。未核代码/复现；独核及实际写后按后到事实记录。

## 3. 2606.00919 RCSP：必要Source与唯一owner提案

已实际读[exact-v1](https://arxiv.org/html/2606.00919v1) §4–7/Eq1–4/Tables2–4及Appendix0.A/Table5，[HTML原件](SUP_MODEL_R3_2606.00919v1_20261024.html)自标2606.00919v1 /30May2026；旧CALIBRATION的Eq2/T4有效片段复用，不做旧新全稿比较。无已见撤回/勘误标签；当前AB history有v2，不用其新增回填。

日期：[原AB history](SUP_MODEL_V1_ABSTRACTS_20261023.json)v1唯一May30 23:02:33Z，最早公告同Jun2 08:00BJT；[DC原件](SUP_MODEL_DATACITE_20261023.json)精确DOI、findable、同arxiv.content query，registered=`2026-06-02T04:02:58Z`=12:02:58BJT。联合区间位于Jun02，沿当前合同限定公告日，非registered直接等公开。

**评分2+1+2=5，标准必要域完成，差额只深入目标时间路径及反侧。** D2：冻结基座同软接口的监督路径对照；R1：单组件适配；D2：时间路径/拒答/事实保留取舍可复用。不把成熟KL/CE/curriculum原则或参数少计成增量。

§4/Eq2：`(1-μ) CE(a) + μ CE(f) - λ CE(h) + βcontrast KL(pθ||pref)`，μ从μstart线性转到μend，另有utility factual CE+KL。a/f/h分别是abstention/factual/hallucinated target，答案span token平均CE；负CE压低错误target likelihood，不提供正确答案认证或有界安全保证。基座冻结，但梯度仍穿过全模型到输入soft prompt；部署prepend选定prompt，无online更新，需可访问embedding层，不等同仅公开text API可用。KL只是软约束，保留原能力需独立测。

§5/6/Appendix0.A：contrast训练HaluEval首8000+TruthfulQA首600，utility TriviaQA27000；作者称heldout TruthfulQA217、其余固定500评估。GPT4.1 judge使用reference和改SimpleQA rubric；generation temperature0/top-p1/beam1，输出截去trailing artifacts/重复prompt/multiparagraph再判，非原始长输出的安全评价。L4/A100/H100按可用性运行，但具体表项设备对应、完整precision/训练搜索总费、推理输入输出长度/batch/concurrency/SLO未齐，不拼低参数数为端到端省费。Table5 Gemma学习率3e-5/batch32/3epochs，λ1/βutility3.8/βcontrast1，μ.4→.9、T0→.6；Llama4epochs及其他超参不同，非严格单变量跨架构归因。

Table4同Gemma3-12B/TruthfulQA配置下重训，scheduled full HALL65.90/FACT31.33，去schedule fixedμ为71.43/26.73；只采该局部权重路径可影响取舍。fixedμ实际值、seed/repeat/CI未披露，不认证curriculum普遍全优/唯一原因。Table2/3也有直接反侧：Llama HaluEval HALL从base59.67升到60.67，SimpleQA90.67升到92；MedHallu FACT22→19且F23.24→20.73。医学集仅这里的通用QA评价人口，不扩AIforScience机制。多数F提高不能掩盖这些反退；§7明确相同F可对应不同拒答/事实profile。

### Books实际比较与逐字PRE（尚未写）

唯一owner：`TRAIN-SFT`，Ch29同“条件最大似然”论证中的输入接口段。已读该段完整前后：Concept Tokens限定冻结输入接口、否定控制增拒答却降正确率；后段是训练搜索离散chunk code。这些已有原则不再重写，差额仅“同冻结soft interface的目标权重时间路径”。Ch30开篇及“LoRA没有改变SFT objective”明确参数化与监督目标分责，故不因PEFT/少参数放Ch30；无需Ch66另写一份loss机制。

上锚（完整直接前段）：

> 更新权限还可以进一步收窄到输入接口，而非 response 上的全部适配参数：在多份 concept definition 中把概念名替换为 special token，冻结模型及其他 embedding，仅用普通 LM cross-entropy 学习这个 token 的 input embedding。它尝试把定义条件压成一个可调用的行为入口，仍支付全模型前向和到输入的反向传播；定义来源、tokenizer、embedding 与冻结 checkpoint 必须共同标识。它不是新事实的存储证书，也不等同普通 response SFT。[Concept Tokens 的局部对照](https://arxiv.org/html/2601.04465v1)中，否定控制主要增加 abstention，正确率与 precision 反而下降；单定义 lossless 或一般组合能力未证明。接口控制、事实质量与校准须分别验收，压缩不可靠时保留显式定义 context 和原 verified SFT。<!-- source-family:SF-2026-ARXIV-2601-04465 -->

拟新增完整一段：

> 同一冻结基座的输入软接口还须区分“更新哪些参数”与“沿什么监督路径更新”：对已知事实/幻觉答案，可在错误target的负CE之外混合拒答与事实target的CE，让权重随训练从偏拒答转向偏事实，并另保留utility监督与对基座的KL软约束。[局部软prompt消融](https://arxiv.org/html/2606.00919v1#S6.SS2)中，改变为固定权重会改变幻觉/事实取舍，但单配置且固定权重与重复运行未充分披露，不能认证课程普遍更优或KL保证能力不变。其他任务仍有幻觉率上升、事实率下降；应分报事实、错误和拒答，不由单一F-score批准可靠性。负CE目标不是新事实真值，冻结主干也不免全模型前反向、标签制备、prompt选择及回归费用；路径或质量失配时，保留verified CE、固定配比与原冻结checkpoint。<!-- source-family:SF-2026-ARXIV-2606-00919 -->

下锚（完整直接后段）：

> 条件接口还可以由训练搜索提出，而不由人工给每段标注概念：在固定层为每个token chunk选择一个离散code，将对应向量加到这段hidden；训练期对已知目标采样多条code序列，选conditional likelihood较高者，再联合监督router、codebook与语言模型。[这条受限适配分支](https://arxiv.org/html/2605.14323v1)改变的是内部控制条件与训练环，不是添加可见推理token或MoE expert，也不能继承理想策略搜索的全局最优保证。目标答案可用于训练选code，部署却只有router；主文与附录搜索数不一致、解码和完整费用未闭，不能给出通用运行配方。同数据/步数不等同候选搜索预算，去code后的退步也不证明语义唯一或原能力无损。所有候选前向、路由/先验与联合训练均付费；控制失配、collapse或质量/总费不合算时，保留普通verified SFT与显式条件，不用可命名code代替独立行为验收。<!-- source-family:SF-2026-ARXIV-2605-14323 -->

拟本人Review note（root写，按后到实际事实同步）：

> - `SF-2026-ARXIV-2606-00919` — Daily2026-06-03补Jun02；exact-v1 §4–7/Eq1–4/T2–4/Appendix0.A/T5，2+1+2=5。仅冻结输入softprompt的监督权重时间路径与拒答/事实分责；保fixedμ取值/重复未披露、Llama HALL/FACT反侧、judge/输出处理及全费，不采普遍课程最优、KL能力保证或少参数等净省费，未核代码/复现。独核及实际写后按后到事实记录。

## 4. 交接状态

四项准入由独立reader R2通过；本两Source/2+1+2评分/actual Ch29与逐字PRE由同日[独核记录](SUP_RESUME_REVIEW_20261024.md)R6–7通过（jun03_resume_reader实际消息）。本处仅行政同步，不自签；日期client原URL定点位置已交reader，无新增GET。仅root实际写入后由非writer真实POST验收，当前不称已整合。无本代理Books锁；不stage/commit/push。73旧提案、四定义待准入、官方模型入口、两跨作者交接、DEPOT及日期保留均留原队列，未被本四项归零。日报仍进行中，不授DAY。
