# Jan02 安全/评价四项必要审阅（作者及非作者原源、两项Books写后完成）

四个exact v1原源已实际读下列必要机制、评价和关键反证；日期原值见DATACITE_POTENTIAL.json。结合官方holiday/noadvance-ID可推定[Jan1T01Z,各created+1秒)，不以Submitted或注册=首公开。没运行攻击或对任何外部服务做测试。分数按拟采用窄命题；不把安全研究的宣传结论当已确认。

## [RepetitionCurse — 2512.23995v1](https://arxiv.org/html/2512.23995v1)

2+3+3=8，安全/设计反证深入。§3.1–3.4 threat/metric/placement、§4.1 router模拟/§4.2本地kernel和remoteAPI、§4.3侧信道替代解释、§5.1–5.3长度/分布/defense及ethical statement。旧训练load balance不保证inference同负载；repetitive输入能集中routing，而**expert集中是否成为device straggler取决于placement和top-k**。TMI=设备数×min(k,每设备expert数)/k为静态理论上界，不是实测延迟或所有MoE脆弱证明；同top2若位于两设备，EP2可仍平衡。

139个config调查不是139份runtime攻防；14模型的vocabulary coverage使用router输出模拟，token数仅latency代理。Local vLLM 200attack/200LongBench normal、同20000token，EP2/4/8测bottleneck MoE kernel；hardware/precision、batch/concurrency与SLO阈值Not Disclosed，不从kernel→端到端可用性保证。Remote 100+100、20000token、max_new_tokens1避免输出长度混杂，报告平均TTFT比和95%lower-confidence-bound，不是tail latency或服务停机；未检查并发victim损失。文中2个dense参照不足识别隐藏架构，网络/缓存/provider路径是替代解释，远程异常不证明ChatGPT用MoE或EP大小。EPLB响应窗口/自然输入分布改变会重验。

§5.3 PPL筛查是建议，有额外模型延迟及误拒可能；vulnerability-aware placement只有greedy覆盖模拟，未实测完整mitigation/后端SLO，不授权安全保证。拟长期增量是负载观测还须含输入分布、placement epoch及worst-case输入，而非只看训练均值。MODEL-MOE Ch21已有训练balance/Capacity及“Router选择Expert，Placement决定...”承载分层，但未明确这种adversarial输入与remote不可识别边界；拟该placement节窄两段，待root必要证据及写锁。

## [Encoder-only Audio Attack — 2512.23881v1](https://arxiv.org/html/2512.23881v1)

2+2+3=7，安全反证深入；§3 latent目标、§4 threat/baselines/config、§5 Tables1/2和§6。固定audio encoder、projector/decoder，不反传decoder，仅用encoder gradient优化一个target-specific通用waveform扰动，逐frame cosine靠近一次TTS参考encoder轨迹；encoder知识边界不等于decoder安全边界。每target独立扰动（非一个扰动任意目标），固定padding/trimming长度、L∞=.02，不能称人耳不可觉察或物理播放robustness已证。

Qwen2-Audio7B/Whisper-large-v3，LibriSpeech train-clean-100 30000iterations；heldout LibriSpeech-other/MInDS英语3accent/SpeechCommands，每dataset1000。normalized exact-transcript match（wake别名另计）只证明输出目标转录，**不证明门锁/删数据执行或系统授权已被越过**，也不是开放域任意harmful instruction。Random通用噪声5draw同budget作为替代解释；不存在跨不同decoder或不同encoder的model transfer实验，不能由共享encoder猜所有proprietary系统同样受损。

RTX6000Ada上1000iteration、physical batch1/accum64的end-to-end CE与encoder-only cosine效率比较只测优化工作，目标不同；不能把3.7×优化throughput拼入30000-step ASR成为等攻击成功预算优势。precision、最终decode温度/长度Not Disclosed，无production concurrency/SLO。§6防御为建议，未验证。PLATFORM-SECURITY Ch72已有isolated encoder test与完整modality-transform run identity，但仅测试分类不足覆盖“可公开复用encoder梯度成为攻击者的灰盒能力”；拟最小接口威胁增量，先root证据/owner判断，不写共享书。

## [Jailbreaks vs Content Safety Filters — 2512.24044v1](https://arxiv.org/html/2512.24044v1)

3+2+3=8，评价反证深入；§3.1–3.3完整对象与Eq5–10、§4.1–4.3、Tables1–5/Limitations、Appendix A.1–A.4必要配置。Base-model ASR与input/output filter双阶段漏检回答不同问题；417 harmful+417topic-aligned benign，攻击/过滤器/GT标签不能只作一个排行榜。**Eq8 Pass仅两个filter未检出的indicator，并未显式乘Judge的harmful-output成功indicator**，不把Pass当最终可执行harm条件概率、不自行以1-DR_I/1-DR_O独立相乘。Fig1成功攻击子集的DR与全测试Table1/2保持分母区别。

目标Llama2/3.1/Mistral/Vicuna/Qwen2.5及GPT4o-2024-1120/GPT4Turbo1106preview；GPT4judge温度0/top-p1、localA10080GB、输出512，filterOmni-moderation-latest/Guard/GradSafe/O3。PromptGuard harmful=injection+jailbreak阈值.99，GradSafe .25且只有input；guard身份正文Llama2与链接Guard3不一致，不视为精确一致复现。主张“过滤器获胜/minimalcost”越界：攻击没有共同adaptive-defense预算、API查询预算限制、无tool-enhanced或跨run保障；normal set PromptGuard FPR=1展示operating point失效，不证明所有阈值总误拒。

Table4 latency header是s/sample，§4.2正文同数却写ms/sample（.028/.455/7.22/40.67），故**不采用时延倍率、生产成本或推荐某filter**；price/version漂移亦不当前保证。采用是ASR、双阶段漏检、benign falsepositive及end-to-end成本须各自保留，并以共同目标/预算验收。PLATFORM-EVALUATION-SYSTEM/PLATFORM-SECURITY具体已有coverage仍须查现有论点；必要原源待root独立。

## [Future/Past and Language Safety — 2512.24556v1](https://arxiv.org/html/2512.24556v1)

2+2+3=7，安全/评价反证深入；§3 factorial/labels/validation，§4 Tables2–6/8、§5讨论与§6.1–6.3限制/§8.1未来mechanistic work。60base harmful goals×2language×4framing，3目标模型=1440 evaluations；nativeStandardHausa/back-translation，Gemini2.5Flash judge、270human审（κ.692，86.7%agreement）与150GPT4o审。控制同goal有具体价值，**surface-framing成组变化不证明模型内部tokenization/semanticfilter/temporal circuit机制**；complex interference是行为解释假说，未有因果干预或正式交互效应检验。

Hausa不普遍更弱：不同目标在aggregate及language×tense cell方向不同；不能用平均English/Hausa差覆盖所有四格，更不将future改写当安全防御。3模型品牌被作者直接归因RLHF/Constitutional/scaling与training数据偏见没有primary内部证据，全部不采用。Judge confidence.99不是accuracy；150audit中Gemini judge与GPT4o对Gemini3的safe率不同也不足认证后者为无偏gold或精确lower-bound。API精确snapshot/解码预算/temperature、hardware/precision Not Disclosed；相关同goal8variants及3目标不能按1440独立样本简推显著性。

Books已有覆盖：PLATFORM-EVALUATION-SYSTEM Ch66“平均值、切片与不确定性”508–537明确language/region与safety分层、per-example和same-prompt相关性不能朴素iid CI；本次补language×framing局部验证，未成立新内部mechanism，不追加作者叙事为规律。PLATFORM-SECURITY Ch72run identity已有goal、transform、judge、attempt条件及alignment不授release。root已实际读必要原源及Ch66具体论点，NoChange通过。

非作者复核：root实际核23995 §3.3 Eq3/4、§3.4/4.1/4.2/4.3/5.3；23881 §3/4/5两表/6；24044 Eq3/4及Eq8–10、Tables4/5、§4.2/limitations/A.1/A.3；24556 §3 factorial与两audit、§4.2/4.4/§6。四项窄证据及分数通过，未授安全保证、内部架构或因果机理。

具体落实：23995已在MODEL-MOE Ch21 placement合同之后779/781写两段，末注985；23881已在PLATFORM-SECURITY Ch72 run非因果边界之后717/719写两段，末注3986。root已实际读两处新增diff及前后邻接，非作者POST通过，末注同步；非日级验收。24044对读Ch72 540–570独立region输入合同、组合处理次序与ASR/utility同模型人口及成本/阈值另验，另有Ch66组件失败相关性；该设计分账已有覆盖。Eq8 Pass不含Judge与s/ms冲突仅作为此论文评价口径限定保留，不声称正文覆盖该特定公式或错误，不新增通用定律；root既有论点对读后该处置通过。
