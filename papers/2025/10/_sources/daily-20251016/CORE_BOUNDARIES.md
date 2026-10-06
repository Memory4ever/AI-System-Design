# 2025-10-16 必要核心边界

作者Euler。原40加新增三组，共43精确v1论文必要安全/设计反侧或决定准入相关段，加Coral/Paddle两个官方core已实际读；不是43完整全文，也不是正式Evidence完成。全部日期隔离，不授权评分、安全保证、性能采用或Books。下列原响应保留实际位置；Locator/下载成功不算已读，未遍历无关附件。

| 身份 | 实际必要节/原响应 | 可以保留的边界与不能采用的结论 |
| --- | --- | --- |
| 13237 VLA attack | RAW_NECESSARY_CORES_A、RAW_CORE_LOCATORS；v1 §3.1～3.2 L50～182、限制L244～246 | encoder参数访问、224图像中50patch、LIBERO任务/仿真；多camera/物理遮挡未解决。公式label与prose有交换，不采用错误式子；非黑盒/真实机器人安全证书 |
| 12966 Pyramid SD | RAW_CORE_LOCATORS L48～157；CICERO-core-12966v1 S3.p1/S3.SS1.p1–2文字段实际窄补 | 将标准随机SD说成logit差阈值0/top精确匹配是简化，不作一般lossless验证推导；fuzzy有质量取舍/shared tokenizer；Table1 std跨配置非重复seed，非target分布无损证明 |
| 12672 CALM | RAW_SAFETY_CORE_C L108～152 | SVD概念K/正交projection；decode O(d²)，4000 paired校准数据/PPL与独立harm评测分开；无训练不等无数据/无推理成本 |
| 13190 SHIELD | RAW_SAFETY_CORE_C L76～126 | Alg1类别→动作由prompt concat完成；Block标签不是runtime权限gate/不可绕过安全边界 |
| 13351 Protect | RAW_SAFETY_CORE_C L85～119；RAW_SAFETY_FIND_A LoRA L263～281 | Gemini teacher/temp0及human抽样，非无human验证；prose与Table3反向改标签数有冲突，21% changes不等label accuracy；audio承文本label，不等独立多模态真值 |
| 13290 MERA | RAW_SAFETY_CORE_C L157～220 | disjoint iid校准、Hoeffding/union over K、空集合abstain；vstar/alpha负号与lambda式符号、nonlinear mixing定义冲突，停止采用公式，不称普遍不退化安全 |
| 13183 DSCD | RAW_SAFETY_FIND_A L129～163/L200/L421～435 | JSD层选择/qH-qS+qT heuristic；部分任务低于vanilla，MODE2受限layer集合不是因果定位 |
| 13900 Narrow FT | RAW_SAFETY_FIND_A L191～223 | 随机方向/model差异、40k FT混0～80k C4；Gemma/Qwen迹象不同，消bias不等消所有风险，不以窄FT代理一般对齐 |
| 13901 RAID | RAW_SAFETY_FIND_A L89～115/L316；CICERO-necessary-gap-web2 L281–305/328–338实际窄补 | Eq18 gradient descent减gradient，而Alg3 L302加gradient，更新方向内部不一致；GCG prose80/table88、92.35又不能概称四模型perfect。white-box/refusal critic、ASETF原结果非重跑，不与黑盒query预算等价、不采用普遍成功率 |
| 13512 LDP RLHF | RAW_SAFETY_D §3 L121～194 | RR对人类偏好label提供local DP；BT、bounded/realizable F、concentrability约束；不保护prompt/response完整内容，不普遍RLHF隐私 |
| 13543 Browserfuzz | RAW_SAFETY_FIND_E §3.1～3.2 L124～277/Table2～3 L835～857 | hidden link/blob的controlled page机制；表中100迭代例数据明确illustrative，不作为观测到的vendor attack rate |
| 13928 Brain Rot | RAW_SAFETY_FIND_E L75～183 | M1长短/流行度、M2 GPT4omini和3grad抽检76%agree、四模型/剂量控制；control继续训练也改变安全，不能把所有变化归junk或外推人类认知 |
| 13915 Readability | RAW_COUNTER_F §3 L75～95；RAW_FINAL_CORE_O L57～60；RAW_FINAL_CORE_P L67/L126～147 | 人类CLEAR可读性相关不等生成coherence人类真值；共享synthetic生成/域内coherence与域外collapse，TableA3统计仍异，不声称全统计严格匹配 |
| 13154 MENAValues | RAW_SAFETY_FIND_E L386～388；RAW_FINAL_CORE_M L124～142/L397～405 | 七模型、WVS/AOI16国、human核翻译/MCQ；描述性民意不是规范good，高alignment score可复刻bias |
| 13272 VERITAS | RAW_COUNTER_F L162～163；RAW_FINAL_CORE_M L115～160 | 50样本human作者对照和Claude标签RM；think-answer regexp presence不能证明reasoning因果faithfulness，不称无human验证 |
| 12587 FUT | RAW_COUNTER_F L67～77/L260～264 | belief expression按重复采样一致性校准，事实correctness另评价；不能当正确概率/知识真值保证 |
| 12697 Judge Debate | RAW_COUNTER_F L93～97/L206～248 | maxT/consensus、EM两混合BetaBinomial、KS<.05连续两轮仅稳定停止；形式正确性依mild assumptions，稳定不等truth |
| 12710 Reflective VLA | RAW_COUNTER_G L133～191/L204～215/L243 | 受限reward component库/JSON；successful replay质量也依reflection reward，去SFT出现reward hacking；task成功不等全局alignment |
| 13080 Counting | RAW_COUNTER_G L193～212/Table2 | FID与CHR在dataset/solver下反转，DDPM亦有弱格；只说明具体blindspot，不泛称FID无价值 |
| 13334 DefensiveKV | RAW_COUNTER_G L128～147 | historical max+prior floor近似未来重要性，32-token observation/FlashAttention约束；非未来token worst-case保证 |
| 13912 Debater belief | RAW_COUNTER_G L268；RAW_FINAL_CORE_O L114～120；RAW_FINAL_CORE_P L175～208 | 300主观题、Haiku judge/second-order偏置，无human accuracy真值；原belief criterion未满足，不能认模型belief就等诚实/正确 |
| 12668 PRAG | RAW_COUNTER_H L57/L78/L177～189 | 部分检索vs完整组合；组合对raw text无效率优势，flattened LoRA相似度仅suggestive，不证明知识容量 |
| 13551 Tandem | RAW_COUNTER_H L50～51/L73～96/L170～186 | same-tokenizer GSM8K REINFORCE随机senior/junior handoff proxy；无human主观可理解性验证，collusion仍可能 |
| 12702 NL2Contract | RAW_COUNTER_H L98～109/L337～348 | precondition减少invalid-input误报；14/19 verifier-capable bugs与34～39%spec不同denominator，CrossHair/Pynguin不同，非一般验证真值保证 |
| 12637 COSTAR-A | RAW_ADMISSION_I/J PDF §3.5 p7～8及p15 | 五开源模型、50token、deterministic/CPU、七demographic模拟；Answer收益Qwen/Llama不同，保留预算/输出directive增量而非人群正确性 |
| 13214 ARE | RAW_ADMISSION_I 方法§2～3/Table1～3 | whole vs step校验、正确step复用在困难AIME与简单题成本收益不同；全错时step overhead，不把摘要50%泛化 |
| 13248 NeTestLLM | RAW_ADMISSION_K L200～206 | small artifact repair vs large testcase revision→human escalation；bug/config/code/test异因routing是潜力，不把领域结果等自动生产保证 |
| 13106 TRUSTVIS | RAW_ADMISSION_K III L81～135 | 有human ground truth，TUR为predicted unsafe precision；VicunaS5低37.5%及class imbalance，正文117/126差异保留；非无human校准或完整trust guarantee |
| 12608 StyleDecipher | RAW_ADMISSION_K III L129～248 | discrete rewrite/ngram edit/BERT pooled cosine/XGBoost；classifier概率非身份凭证，rewrite保语义不是形式保证 |
| 13202 LGSA | RAW_FINAL_CORE_M PDF L630～717；RAW_FINAL_CORE_N L783～829 | 5%human sample/阈值revise、敏感题human强制；小构造cash classifier/三个naive swap反例提示label fidelity，非一般公平/隐私保证 |
| 13285 IDS | RAW_COUNTER_L L124～152 | positive-prompt PCA/Mahalanobis95th percentile适配strength，fit distribution内连贯性不等global OOD安全 |
| 12689 Delegates | RAW_FINAL_CORE_N L239～247 | LLM模拟voters/美国专家共识，无human welfare验证；不能以model judgment授权覆盖用户偏好 |
| 12864 RID | RAW_FINAL_CORE_N L128～165 | 20author-defined ground truth/一人manual、gpt4o temp.1；strict budget override例不能授model越权；RQS含主观性 |
| 13501 CRew | RAW_FINAL_CORE_N L85～127/L204 | answer mean probability proxy仅closed end；DPO先gold正确/错误再confidence pair，非label-free；低confidence训练受限数学可反优 |
| 13554 Attention credit | RAW_FINAL_CORE_O §4.1/5 L109～184 | 70GSM8K/Qwen4B生成后attention、forced topk测Jaccard内容重叠不是因果内部reasoning；额外eager forward vsFlash成本不免费 |
| 13903 Communication | RAW_FINAL_CORE_O L323；RAW_FINAL_CORE_P L245～269 | finite monoid/prefix scan N宽log深/ΩN size等受限算法族；组通信lower bounds不直接等真实LLM墙钟加速 |
| 12950 EHR privacy | RAW_PRIVACY_FINAL_R §3.1～3.3 L84～117/§6 L219～224；初次必要方法原读取§4.1～4.4 | prompt/embedding抽取与个体/子群风险分开，benchmark已知training cohort；低距离不等高风险，probe依embedding访问，六测试不穷尽；不是临床诊断采用或无泄漏证书 |
| 13108 DriveCritic | RAW_TITLE_CORE_Q L115～162；L143–162分母窄补 | 镜像trajectory避免LK=0捷径；4564/1166、test单主作者5年经验。608/663(91.7%)属Case1 lane/progress，Case2为304/503(60.4%)；train Case1 pseudo人偏好、Case2 GPT5。76%偏好准确率非驾驶安全保证 |
| 13291 WOWService | RAW_TITLE_CORE_Q L201～249/L327～359 | 60%domain/40%general SFT再rule RL；online字符串/工具cheap检查vs offline多agent/human，badcase regex局限；作者93.5%recall/近100precision不作生产保证 |
| 13481 Tahakom | RAW_TITLE_CORE_Q L294～376 | tokenizer/pretrain子集分离、固定128k、1/pi语言重权、Llama1B继续预训练；fertility降低非下游增益，最佳分布匹配仍开放，不把配方全附件列队 |

## 三新增必要边界

| 精确v1 | 作者实际相关段与最小结论 |
| --- | --- |
| [13161 Mirror-SD](https://arxiv.org/html/2510.13161v1) | CICERO-core-13161v1：S3.SS1文字段、S4.SS1/2相关p及A2(AppB)文字段/A6.SS1(AppF1)。verified draft conditional law parity前提下说明接受长度统计相同，不证明任意branch selection或全部输出同分布；完整公式/proof未自称全读。batch1/gamma7/topk8/midexit、UltraChat draft/eight M2 Ultra；0.6M/0.6B文字不一致、Thunderbolt5连线仅作者主张未核，不采用lossless/性能。Cicero更广方法段/附录阅读不回填作者。 |
| [13271 Concept](https://arxiv.org/html/2510.13271v1) | CICERO-core-13271v1：S3.SS1/2/3文字段及S4.p1/2；100games/语言，static10 guesses、dynamic随原human猜次数；nonreason10 output/temp.1 vsreason1000/temp1，human总found92/93%而63%十猜内，不等预算比较。exactmatch及prompt层级/信息量不同，不授全LLM推理失败。Cicero另实际核截断计错/不同语种与limitations，作者不称这些全节已读。 |
| [13316 Interestingness](https://arxiv.org/html/2510.13316v1) | CICERO-core-13316v1：S3.SS1/2、S4.SS1/2文字段及S6.p1/2。1000图/258workers/5HIT，单图几乎全positive，高agreement可退化；2500pairs/553workers，36%swap偏置筛除仅留1599，66.2%整体/73.8%人consensus/56.5%dissent只该筛后切片，95.5%模型自一致非偏好真值。未把S6其余段/Cicero广范围回填作者。 |

## 两官方core（既有有效范围）

[Coral NPU](https://research.google/blog/coral-npu-a-full-stack-platform-for-edge-ai/) RAW_CORAL_TITLES L104～162：MLIR/IREE progressive lowering、scalar/vector RVV1/matrix外积设计，matrix unit仍开发，CHERI being designed，Gemma合作未来态，不授实现/性能/安全。未知TZ Oct15日名隔离。

[PaddleOCR-VL](https://ernie.baidu.com/blog/posts/paddleocr-vl/) RAW_TARGET_CORES_B L14～26：动态NaViT encoder+0.3B Ernie4.5 LM、layout→element recognition两阶段；Repo packing/最新OCR SFT是窄说明，不证明精确历史artifact机制。未知TZ Oct16日名隔离。

## 实际Books比较范围

只读具名基线与相邻正文：[AGENT-PROMPT Ch74](../../../../../books/part-07-agent/74-prompt.md) L32～112已有source/trust、parse/schema→semantic→authorize→execute及CoT非因果；[AGENT-CONTEXT Ch75](../../../../../books/part-07-agent/75-context.md) L1～45区分accepted length、effective use、working state与derived memory。SHIELD prompt策略、RID override输出、long-context引用评测不能跨这些信任/利用边界。

[PLATFORM-EVALUATION-SYSTEM Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) L10～105已有claim/evidence/measures/decision及scorer/provenance/slices、transport/semantic/Policy/outcome分层；[PLATFORM-SECURITY Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) L1～90已有subject/asset信任链及privacy/federation邻接。Protect/TUR/MERA/BrainRot的有限结果不能改写为全局安全；label-LDP不等完整内容隐私。

以上是具体边界比较，不声称112潜力都已有覆盖。由于无精确落窗first-public，Books窄整合提案0、实际写入0；不写共享Books，不强造diff。独立复核若发现具体新证据，只重开受影响命题。
