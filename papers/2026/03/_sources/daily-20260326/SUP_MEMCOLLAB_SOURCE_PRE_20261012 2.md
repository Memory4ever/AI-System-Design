# MemCollab necessary Source / sole Ch77 两PRE

2026-10-12，原2+2+3=7/date25保持。[2603.23234v1](https://arxiv.org/html/2603.23234v1) actual必要§3–5/Eq1–8/Alg1–2/T1–3、A/C/D必要解释与G完整相关prompt；F仅文字代表例，不宣称全部轨迹图或artifact/复现。支持与直接反侧足够停止。

## 独立可采用命题 / 必要负侧

同task异构两agent各生成含工具反馈的轨迹，groundtruth/executable verifier判断最终输出，再由强backbone摘要其结构差异为(enforce invariant;avoid violation)候选，bank存抽象约束而非原trace/答案；consumer先模型分类(c,u)严格过滤，再相似排序取得guidance。这里共享的是构造/消费接口，不是不同模型的全部hidden状态或事实权限。G有trigger→enforce/avoid模板及固定allowed类别/subcategory规则，可读，但prompt宣称grounded/not-speculative不是验证器。

Eq2/Alg1只检查weak正确则选weak，否则选strong，**未检查strong是否正确/双对/双错**；strong摘要模型也可能臆造原因，不将capacity标签当success/failure标签。可采用对比派生proposal/另验其适用条件，不采用完整preference构造recipe或认定所有memory已验证。分类或同类别不保证约束可迁移，严格filter/空桶/错类fallback未披露；C实际TF-IDF top3 samples、每sample最多3 entries，不混成总3条memory。构造存task类别，异构consumer分类版本也应绑定，不能由同schema假定所有模型同标签。

§3.4/D假设τ=f(s,b)/m=ψ(s)，MemNCE明确只是解释proxy而非实际优化目标，无识别可证明“删除所有agentbias/恢复唯一invariants”。§4.5 branching剪枝ρ式假设每层独立减k个错误，真实guidance是softprompt，并未证明只删除错误分支/不误剪正确路线；无指数复杂度或可靠性保证。Top-p过多反退，classifier/error labels GPT4o-mini与同backbone共享偏差不能当独立truth。

T1 Qwen32 HumanEval86.6<selfcontrast87.8；T2 Llama MBPP49.8<selfcontrast51.4。§4.2.2正文LlamaMATH74.4 vsT2MATH42.4/GSM74.4不统一；平均质量改善仅有限作者protocol，不推任意模型全部任务。T3 Qwen7平均turns2.7→2.2/1.8→1.6/3.1→1.4/3.3→1.5不是token/wallclock/SLO/净费；bank双轨迹与strong摘要、分类/TFIDF/读取/context/code执行仍另计。

§4.1写从每数学dataset取1000建bank与disjoint500 eval，但A称MATH500总500，未明确是parentMATH train身份或另样本；不能自补划分/称确定leak，也不能认证全独立评估。代码MBPP974/HumanEval164未给建bank/eval具体split；memory与evaluation数据身份仍需核才采用强迁移结论。C 8RTX6000/CUDA12.8/CodeAgent/temp0/top-p.8/seed42；重复seed/CI、precision/context长度/B/concurrency/最大turn/独立训练和总耗时未披露。GT/verifier拥有结果判定，不自动验证CoT每步或物理/权限正确。

## actual owner 差额与原锚

actual Ch77完整394–436 late-construction/ACTOR/dual-loop/异构model-profile适配及Query-localentity段；650–680 ReasoningBank/procedural粒度与abstractbrowsermemory亦读，Ch77/76/78开篇实际读。原07711分责writer/readermodelprofile改变呈现，没有承载同task跨agent轨迹差异→trigger/enforce/avoid约束构造与task-filtered读资格。sole AGENT-MEMORY Ch77，不复制Ch82多agent调度或Ch66真值评价。

拟SF2606-07711两完整原段+marker之后、下一Query-local construction完整段之前两PRE+纯证据注。保全部原summary/raw/profile和query-local路线。未独核/锁/实际写/POST。

## 两逐字PRE

改变记忆构造的数据来源，还可以把同一任务上不同模型的轨迹放在一起比较，而不只适配一个模型写出的摘要。一个受限分支把轨迹差异提炼成带触发条件的“应遵守什么、应避免什么”约束，存入共享 bank；消费时先按任务类别筛选，再取少量相似经验。这使共享对象从某个模型的具体解法变成候选推理指导，却不保证抽象规则已消去模型偏差，类别相同也不是适用或正确性的证书。原轨迹、判定来源、构造模型、分类与消费者版本仍须可追溯，派生规则不取得事实或执行权限。<!-- source-family:SF-2026-ARXIV-2603-23234 -->

对比的前提仍需单独验收：按弱模型是否答对选择轨迹，并不保证另一条一定错，也不保证弱模型答错时强模型正确；摘要器可能把共同错误误写成规则。有限跨模型实验和较少平均推理轮次不能证明任意任务迁移、净节费或无偏，过多检索还会引入噪声。任务分类、约束适用条件与独立结果验证要分开，数据划分和原文指标身份未闭时不采用更强保证；双轨迹生成、强模型摘要、分类、检索、Context 与工具验证均计费。规则冲突、错类或来源不可信时回读原经验、扩大无类别检索，或保留专属摘要、固定提示和无该记忆的基线，不让共享 bank 自签推理可靠。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23234` — [MemCollab exact-v1](https://arxiv.org/html/2603.23234v1)必要§3–5/Eq1–8/Alg1–2/T1–3、A/C/D/G；仅同task跨模型轨迹差异→trigger/enforce/avoid候选构造与分类后读取资格。保weak-only配对非双标签验证、MATH划分及正文/table身份未闭、softguidance非无偏/指数剪枝证明、反退/单seed/平均turn非净费和全成本；不采通用迁移、完整recipe/事实权限，未核artifact/全部轨迹图/复现。
