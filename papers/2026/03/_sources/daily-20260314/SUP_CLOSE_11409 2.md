# 11409 Speak or Stay Silent：最低实际增量 / 关闭提案

mar14_supplement；仅03-14补Mar13 BJT。root已校准完整题摘、七日期日级arXiv事件有效独核复用；[exact-v1 ABS](./SUP_ABS_11409.txt)四作者Kratika Bhagtani / Mrinal Anand / Yu Chen Xu / Amit Kumar Singh Yadav、Comments Submitted for review to Interspeech2026只投稿非具名早公开正文。当前未见具名撤回/纠错信号，不为此遍历会议库。

实际读取[exact-v1 HTML原件](./SUP_NECESSARY_11409.raw)/[投影](./SUP_NECESSARY_11409.txt)，必要§3–4/B22–32、60/82、85–88；完整Tables1–3/B22–27/33–59/61–81；§5/Table4–5及直接结论B89–118。首次大输出截断的B1–59已拆两小段恢复，B60–118完整可见复用；不读全部参考/附录示例/代码或figure像素，未复现。

准入保持：把pause直接作可发声机会→逐participant binary Speak/Silent并区分address/context/no-reference/third-person-reference→核多方voice assistant何时参与，而不是只生成何种回复。**拟1+1+2=4最低关闭/仅报告Books0**。1只计next-speaker数据重述为target binary和四category平衡/SFT局部训练配置；Reach1限定参与决策，Durability2是局部采用界限，不借“silence是可靠性重要”成熟原则、120k/23pp或章节映射抬DD。P不撤回为EX/NC，不因任务小或费时停。

决定性机制/不能强化的评价：B60真实label是transcript下一utterance由target实际说则Speak，其他Silent；不是独立规范性oracle“should speak”。AMI约100hour四人会议、Friends脚本电视剧、SPGI earningscall，120160总decision points不等120k独立真实assistant conversations。每boundary为全部non-speaking participant生成，80/10/10按category拆、exactcontext去重；未给conversation/session级group split，不能认证相邻context/同场景从未跨split。

训练是已有LoRA attention/MLP r32 α64/dropout.05、AdamW1e-4、batch32、FP16/3epochs、validation F1选checkpoint；2048末turn截断(gptoss1536)，1–8A10080GB/FSDP。Reasoning mode由Gemini2.5Flash拿ground-truth label生成一句解释，label-consistent不证明解释为模型真实因果；四category各25%采样改变训练人口，非新参与安全不变量。temperature0 identicalprompts八LLM是受限文本offline测量，不测实际pause detection、prosody/audio、重叠说话、在线prompt-history或所有prompt variants。

Table2 GPT5.2 Friends S1提升10pp、gptoss Friends+5.10等直接反侧，使B90“重复prompt≤3points”不能解释为全部category成立。模型低分只在此label/protocol，不能从重复systemprompt一次排除所有instruction/design混杂或证明context-aware能力绝不emergent。Table3 Mistral AMI BalAcc+23.35，但Qwen3-4B SPGI+26.69超过prose up-to23；不采用唯一最高收益。gptoss SPGI43.74Acc/49.66BalAcc且S1/S2反退，不能说所有模型SFT必改善；其internalizedCoT冲突原因只是作者解释，无matchedcausal训练干预。

Table4三人Friends360sample κavg.492、S2约27.67%、BalAcc60–66显示transcript行为label与规范参与判断并不一致；不是model surpasshuman所有设置的证书。Table5同FriendsQwen2.5加入GT条件teacher解释Acc63.64→70.84而BalAcc66.60→68.46，未匹配生成长度/calls成本或独立reasoning信号；r32优于16/64只此设置。合并三域的训练后仍测试三域各test，不是完全heldout domain/OOD迁移实证，也没有人类独立blank/noaudio协议补齐。

最低处置充分：实际新增是已有next-speaker监督的binary/category接口及LoRA+label-conditioned reason recipe的受限比较，没有本稿认证新的pause truth、normative参与oracle或跨域泛化/生产时机保证；新增模型数/训练解释术语不自动长期机制。故不做Books ownergap/PRE/POST或继续全附件，保留零样本Speak偏置和模型/人类/训练负侧而不采“显式训练是唯一必要条件”。训练/teachertrace/额外token/calls/voice实时费用保留，batch并发/onlineSLO/重复CI未披露。最新root实际必要HTML/完整AB/T3/数据label/T4/T5非准备者独核通过，主ledger已记，正式已计最低4/仅报告Books0；不授DAY。
