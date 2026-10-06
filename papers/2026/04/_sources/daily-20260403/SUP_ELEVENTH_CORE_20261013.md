# 最后两项有限 core 与明确停止

仅既有题摘集合，必要方法/评价/直接反侧已读；root Source/准入待核，未授 Books 锁。

## 01161 Reasoning Shift：拟 2+2+2=6

[v1](https://arxiv.org/html/2604.01161v1) §3–4/A/B：同数学题比较 isolated、两独立子题、64K Shakespeare前缀、第二turn；OpenRouter各模型固定vendor/defaultsampling/80Kthinking budget。Subtask tokens除2是每题分摊，不是同单题预留budget；Kimi multi-turn token30421>baseline29615，不能写所有条件/模型都缩短。IMOAnswerBench四模型，Qwen27B .745→.624 subtask/.678 longinput，math500 Olmo各checkpoint下降幅度小；judge Gemini3ProPreview自动评价，数学之外尚未测。Qwen3-32B reasoning3824→2741，但first candidate位置925→939未检正确性；sentence role与final-answer→stop57→68%属行为测量，不是解释内部原因。重要同prefix反侧：去last50tokens再相同量resample，</think>出现率baseline21%、128prefix26%、16K46%，复查词下降；限定已选Longinput traces，不等真实跨题所有tokenbudget的因果中介。可采用 context-dependent stop行为/有效reasoning预算的盲点，不授长文本semantic influence绝无、compaction/recursivecall有效或质量必由verification短造成；没有已开发mitigation。追加prefix本身prefill费用，少生成token不等总成本低。

## 01170 ORCA：拟 2+3+2=7，完整流程风险资格必要深入

[v1](https://arxiv.org/html/2604.01170v1) §3.2–3.4/4/Tables2–5、AppendixA/B：每step先score后update，未停止时fast probe对pseudo-target0做Brier梯度；outer对累计0→1标签经unroll学习初始化/QK/η，冻结base LM。不把未停止推成实际错误或novelty当truth；consistent label=full-budget answer一致，不是correctness。LTT校准**完整自适应随机算法**而非静态分数；题间重置fast state、fixed outer独立cal集、同数据P及随机机制、ordered grid+fixedsequence有效检验才有marginal risk，非每题保证或任意OOD。没有合法阈值时A.2写λ0但未定义其风险，不能私加“full-budget自动安全”。5K math3/1/1 split，R1-671B生成trajectories、Qwen3-32B标correct/GPT4.1评价；各Qwen2.5/QwQ32B/Llama70B独立训其embeddings，不是直接跨weight复用。累计首次正确以后全1的error定义不证明之后答案不反转，亦须恢复实际部署trajectory与teacher trace是否一致，未独核不授on-policy实验合格。

实际noQK在δ.1 supervised savings.475/err.110、static.380/.105；meta+update vs标准samearch.239/.095有有限机制对照，QK.414/.103 vs标准.394/.108差额小。OOD GPQA noQK.715/.300、QK.665/.210，consistent .653/.328；大于δ不是formalproof反例（P变了），但不可称OOD risk已控制。saving主要step/token，未含teacher trajectory生成、标注、meta-training、多个阈值校准运行、特征提取与每step更新的全墙时/钱。采用差额候选仅score-then-update与完整流程risk校准责任/同分布边界，formalrisk细节待root独核；不授部署recipe或“在线就on-policy”。

## 当前发现与审阅停止

原有限68完整v1题摘中需必要core者均已到具体采用/贡献关闭/日期出口；未扩分类列表、全版本或代码。剩余 ordinary 为 root 逐项独核/作者修正、已通过项 owner差额/PRE及正式report六部分闭合；00199更早ICLR全文精确首公开日无法恢复时保持独立日期隔离，不计4月2日新首发。各外部历史source HOLD仍保留，不用ordinary工作迁移状态。未自授Source全日、DAY或Complete。
