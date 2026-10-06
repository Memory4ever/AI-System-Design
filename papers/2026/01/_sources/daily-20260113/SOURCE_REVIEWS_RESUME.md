# Jan13 必要原文审阅（作者记录，非日Gate）

只记录实际已读必要位置及停止边界；准入校准、日期、Books与POST分账。每条均 exact-v1 HTML；core-* 文本按标注段落保留方法/评价、结果表可能省略，未采未读数值、未运行代码/复现。截取中个别数学不等式因HTML抽取缺损，不据缺损符号推断精确阈值。

| ID | 实际位置 | 可采用增量 / 直接反侧 | Books提案（待独立） |
|---|---|---|---|
|05366|§3–5，core-05366.txt|BFCL-v4 multiple、英式schema/value约束下区分intent错与值语言surface错；PAR/全译/PT/PRE/POST，post处理会语义漂移、低资源理解错误不因surface校准消失；不是生产多轮执行|Ch78 canonical值与用户语言不同层的窄差额|
|05414|§2–4，core-05414.txt|批输出与stateless独立输出两人口，temp/top_p随机性不认证用户要求数值分布；W1/KS/KL等检验受样本与重尾条件限制，不采“无内部sampler”因果断言|Ch20/Ch78可信sampler分责已有，具体Existing待核|
|05445|§3–5.4，core-05445.txt|真实对话、分支重试、本地策略抽象/bitset搜索复用；10turn/两harm datasets、GPT4o judge；本地overwrite非伪造目标history，有限三防御不证明实际危害或普遍攻破|Ch72攻击搜索支持/历史分责，或既有多轮闭环具体Existing|
|05451|§3–4，core-05451.txt|schema-independent SQR模板先约束SQL骨架、后NL重述；32手工模板、4k/1k，LLM重述不继承编译正确性，DDL/关联假设限制|Ch27可执行结构与语言增强分责可能已有|
|05455|§3–4，core-05455.txt|support/attack tree，intrinsic+BT相对judgment→DFQuAD传播；竞争说服分不是真值概率，deterministic trace不是内部因果faithfulness，强judge/CoT反例保留|先Report-only：受限score组合不新建论证系统|
|05475|§2–3，core-05475.txt|max-return需累计best u；frozen policy推理搜索，不是LLM policy RL更新；未来改善value在单路径训练/beam推理的分布变更下可退步；§3.2 level重复写法矛盾不采逐level数字|Ch79累计best/未来改善分责窄差额|
|05488|§3–4.4，core-05488.txt|更新建新时间戳并引用旧entry、Merge保留证据；synthetic session-QA共享reward、dominant retrieval count加权不是因果credit；固定answerer、三dialog sets/公开Memory-R1来自原论文、α过大/稀疏reward退步|Ch33检索proxy与因果credit分责/Ch77版本链已可能覆盖|
|05503|§3–5.4，core-05503.txt|answer accuracy与abstention双人口/固定成本系数TPC；594+594平衡、三unanswerability类型、judge/human非完美、search上限/历史影响；negative corpus插入未必retrieved，fewshot过拒绝成本|Ch76/Ch66 answerability与检索负证据已有，具体缺口待核|
|05543|§3–4.6，core-05543.txt|speech/text共享policy但按模态单独中心化，speech reward以当前正确text为moving reference；无正确text就退回base；encoder/projector冻结、7B/合成TTS/QA、MRR对原text而非更新后text；hidden similarity非真reasoning因果证明|Ch33同组不同reward人口中心化有窄增量|
|05560|§2–4.4，core-05560.txt|共同base task vector，reasoning低梯度/task高梯度不同mask，重叠索引双方都排除；局部gradient敏感性不是存储位置普遍定理；addivetest/Qwen-Llama有限模型、safety低ASR可能output collapse|Ch35/Ch30 merge冲突已有，selection方向反例可能窄差额|
|05593|§2–3.3，core-05593.txt|parallel轨迹只保留conclusion，message集合须fit window，合成能力另训且过滤voting可解样本；cache池/非独立首round生成、总tokens非wallclock等预算；allwrong→correct不证明底层原始轨迹faithfulness|Ch82结论压缩与合成训练分责窄差额|
|05600|§3–4.4，core-05600.txt|scenegraph对引用子图做局部结构扰动，Jaccard中区+diversity选hardnegative，然后DPO；GPT4o抽图不是真实视觉gold，图正确性/CoT可读性非faithfulness；5MLLM/A-OKVQA/eval7切片|Ch34偏好pair的结构污染与监督truth分责|
|05647|§3–4.1，core-05647.txt|conditional score gradient energy仅A1–A4可辨识，实际MSE+LRP近似读图/Top-k；深attention非因果、latent/instant effects直接退步、复杂人口数据饥饿/timeout excluded|Ch5预测统计与因果识别假设的具体Existing或窄差额|
|05679|§3–6，core-05679.txt|top100 contrastive SAE features→token injection+FP/FN falsification，所测196contextdependent无genuine；64token语料/有限模型SAE及严格individualfeature标准，不排除分布式机制；steering少量反例非全因果排除|Ch5标签/激活/干预/语义不变性有必要窄补充|
|05461|§3–4，core-05461.txt|事实分解/来源核→多轮rewrite+reasoning+history检索；history提高recall不认证implicitbridge与generation，GPT4o评价/200human/相关turn人口|Ch76 retrieval表示/上下文依赖具体Existing待核|
|05465|§3–4，core-05465.txt|先Planner/Solver GRPO，再冻结专家，Inspector消费真实trace residual+teacher auditlabels；不新optimizer，gain减regression，成功trace mining偏置/Inspector成本；非inference-only反思|Ch33 stagedtraining/audit分责，先独立source-owner|
|05549|§3–5，core-05549.txt|temporal t-prefix嵌在Matryoshka fullrepresentation截断前缀，保留semantic tail；六TEM/有限TNP-TimeQA与NQ、LoRA/contrastive、α高伤semantic、低维可能无收益|Ch76检索表示 temporalprefix的两段缺口，待锁|
|05707|§2–5.2，RESUME_EVIDENCE.md|条件PPL/直接WER/10-best reranking人口分别验收，joint decoding更贵；语言覆盖/数据量混杂，attention非因果|Ch23分段可读/可访问与生成/rescore不同的窄差额|
|05930|§2/3.4/6.2/C.4，RESUME_EVIDENCE.md|verifiedprofiling→forecastfilter→execute验证，不执行枝无testgroundtruth；0.7gate不是安全剪枝认证|通用ML搜索人口/预测与执行分责；标准评价其余还待|
