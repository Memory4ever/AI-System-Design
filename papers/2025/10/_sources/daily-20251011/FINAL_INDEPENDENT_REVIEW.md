# 2025-10-11 最终独立复核

最新结论：通过。09898精确v1潜力恢复、99身份/1关闭/98潜力及44必要命题的作者窄同步已实际回核；以下旧待办为过程记录，不覆盖末节DAY裁决。

复核者 root / Codex，非作者 Mill。仅本日默认窗口，已重新读取 AGENTS、研究及 Report 合同、来源使用/每日/arXiv、Prompt、ROADMAP 与本日停点。FIRST 的六份精确 v1 潜力校准及四份必要核心保持有效；两个普通遗漏已交作者定点修补，不授 DAY 完成。

## 必要核心实际阅读

在 FIRST 四份原件核心之外，本次从 arXiv 精确 v1 原始 HTML 实际阅读以下六份的必要段落；PDF 单独注明物理页。只核威胁、方法成立条件、评价及反证，不声称全文/附件全审、实现核验或实验复现；这些日期未准入的材料不支持本窗正面 Evidence 或 Books。

| 身份 | 实际范围与限定判断 |
| --- | --- |
| 2510.07985 剪枝触发 | Threat Model、Experimental Setup、General Evaluation、calibration estimation/mitigation 与 Appendix ASR/BR：攻击者控制发布 checkpoint，用户具体剪枝选择未知；五个指令模型、七配置，未剪枝 utility 与剪枝后行为同时评价；安全 calibration 对 SparseGPT/Wanda 的效果和 utility 代价不同，不能说可靠防御；GPT-4.1-mini 与目标词度量不等真实危害概率。 |
| 2510.09269 GoBA | Adversary objective/capabilities、Victim dataset and models、Evaluation metrics、主结果/伦理及 Hardware：LIBERO 演示污染，OpenVLA 与 pi0，两种建模机制；FR/BadVLA ASR 不能替代三层目标完成；三次重复均值/标准差，约 5,000 A100-80GB GPU hours；不外推真实机器人部署或所有触发。 |
| 2510.07642 Role Refusals | Dataset augmentation、Problem Formulation、三 Settings、metrics、Results/Discussion/Limitations：确定性 RBAC 标注与推理时 LLM verifier 是不同角色；EX 只在正确 PERMIT 条件下计算。Setting3 重用原 Spider test questions，再以不重叠 (db_id, role) 与 questions 划分，不能声称完全新 schema 泛化；静态角色/明确策略不覆盖动态委派与多轮隐式权限。 |
| 2510.08464 GLUESTICK | 精确 v1 PDF 物理 p5–7 与 Appendix B.1–B.3（p15–16）：权重差的低秩 SVD 修正只保证矩阵 Frobenius 最优，不保证行为/安全最优；四 LIBERO suites 各 10 tasks x50，导航 100/1,077 scenes，L40S-48GB；WorldVLA chunk25 因剪枝无效动作改 chunk1，不能当默认运行等价；安全是限定模拟指标与阈值，memory matched 不等所有成本相等。 |
| 2510.08646 EDS | §3 的标签/EBM/选层/逐 token 干预，§4 评价/多轮/开销，Appendix B 的训练数据、评估、调参/硬件：主 LLM 权重不变不等不训练外部 EBM；受控 512 prompts 的 1.60→1.65s 不外推 workload。Appendix harmful CR 定义为拒绝，而正文解释又按有害 compliance，另 CARES-21K/SafeMedEval-21K 名称有差异；不替作者消解，不合并安全保证。SafeDial evaluator 正文 GPT-4o-mini 与图注另一型号的差别保留。 |
| 2510.09689 CREST-Search | Threat Model、Targets/Baselines/Configuration、Metrics、Experiment Setup、fine-tuning ablation/Mitigation/Deployment clarification：黑盒完整 search pipeline；任一 detector 判风险就计 RDR，输出与引用网页事件不同；1,500 cases/run、各 query 三次、商业模型微调和版本限定；过滤/再训练是建议而非已验证生产防御。 |
| 2510.09849 VLM 文本注入 | tested models/OCR 条件、Evaluation setting/metrics、baseline/best-grid/preprocessor comparison、Conclusion/Limitations：500 Pet images、Llava-Next-72B 四选一，untargeted 错误与 targeted 命中不同；仅报告所搜网格最优，严格/放宽预处理不同；大模型/清晰文字/启发式限制不等全部 VLM 可迁移。 |

FIRST 中 RefDiv 实际 v1 AB 为 o3，v1 正文/表为 o3-mini，不能只称 v3-v1 型号漂移。本轮已交作者将这个内部冲突，以及 Role split、EDS 指标/数据命名边界，定点同步原筛选记录。

## 来源检查进度

实际读 fetch/recovery/pinpoint/safety_pinpoint 四份请求记录的原 URL、UTC 执行时间、HTTP/失败与范围。结构化读四 Atom 原响应及 model/agent 补页：原 30/4/30/30，补 70/98 到 total100/128，恢复尾页成立；提交发现字段仍不证明首公开。

实际读官方 RSS 的本窗切片：HYGH 在 10/10 00:00 GMT，即 BJT08:00，窗前；不能由零窗内 feed 条目推全站零事件。Seed 原 JSON 五页 19/15/19/19/13=85/total94，最后 false；Blog 三页 17/18/6=41/total49，最后 false；语言可见数与后端 total 不混。混元原 API total11/list11 日期均 2026，不能授2025历史覆盖。

实际原 HTML 文本核 Qwen 旧 Blog 最新09/23及迁站限制、Moonshot09/16→11/06、MiniMax英12/中13及历史尾、ERNIE页2六条/末1/2、ZAI页2最早12/07/没有更多、DeepMind原 gzip 解压当前2026研究壳，以及 Google正确2025/search首15/37和Blog第二页末页。余下来源原结构/本窗邻界与新尾部/12风险修补仍待实际核实，DAY 尚未通过。

Books 正面采用/实际写入0；无stage、commit、push。本文件只是实际独立工作的续点，不把文件写出或格式检查称为日级完成。

## 十二遗漏信号的实际独立补核

十二精确v1官方完整题摘及Submission history已实际读取；以下再读相应原HTML必要段，08614单独读精确v1 PDF物理p4–9。不是依据作者txt的已读标签，也不声称全部附件、代码或实验复现。共通first-public缺口不赋本窗采用权；风险/纠错信号仍须处理到限制。

| 身份 | 实际原件范围与裁决 |
| --- | --- |
| 08158 | 原HTML paragraphs14–22、29–30、35–49：580例/人工三态、四模型、多轮上下文不同；三归因方法与缓解，安全/不安全服从同时上升，不能只抄robust safety。另实际打开官方v2页，withdrawn/Errors in paper；v3存在不证明错误已修或v1全部撤回。作者称四种缓解的计数仍须澄清，正文只列三种策略；不改变未采用状态。 |
| 08211 | paragraphs10–14、17–25、35、38–45：honesty两评价器及format排除；1%与8%效果因模型而异，模拟personas/十场景反馈与KTO/SFT不同，不当真实用户或普遍污染阈值。 |
| 08240 | paragraphs10–22、31、55：双方奖励/unsafe-overrefuse标签、DIR、两actor独立轨迹和更新；初阶段冻结不等全程冻结，REINFORCE++规范化有具体单位；单8B/英文/一轮feedback，FTR不是延迟或完全安全。 |
| 08329 | paragraphs21–27、35、44–57、69、96–98：弱安全generator、训练verifier/Guard2 judge不同；难度筛选、MiniLM多样性与搜索预算边界；人工200例三专家不能授权全7K或生产攻击覆盖。 |
| 08604 | paragraphs15–22、28–30：白盒参数/activation、十base加三防御身份、159HarmBench；低perplexity不代表所有自然攻击，600 benign/FPR0.5%是限定对照，不授黑盒迁移或人类实际危害。 |
| 08614 | v1 PDF物理p4–9：117过滤病例/GPT4V成功读图/排除hard、六模型/每prompt三次；persona属于模型而非患者。诊断一致性按正确/错误状态，不是三个字符串完全相同；未评临床性别必要性真值，一致地错也可一致。 |
| 08624 | paragraphs20–30、69–72：单GPTOSS20B六任务；framing同时改变wrapper/回答约束，不能隔离意识。regex非代码执行/DOI解析，配置声明未复现，不授一般工具正确性。 |
| 08859 | paragraphs15、24–29、32、37–39：300目标/十二模型/四turn/20迭代，Vicuna攻击与GPT3.5 judge不同；any/best及预算不同，模式关联不识别训练遗传或工具effect安全。 |
| 09004 | paragraphs10–34、38–39、44–60：4K安全/12K一般、SFT/DPO与预算不全相同；rank8主方向/max-entry不等完整子空间。AppendixE对两套full n×n orthogonal bases的span正交假设不能当一般矩阵事实，条件线性分解也不保证非线性行为；局部judge保持不能授终身安全。 |
| 09033 | paragraphs12–21、37–41、49–51：两开放模型/固定事实模板，subject关联与attention事件分开；每类1,000训练/200测试、五seed，probe测回忆不等真值。局部AUROC和分布重叠不能证明所有truthfulness不可表示。 |
| 09062 | paragraphs9–37：10K traces/~8K过滤/2K RL、70%旧错和30%fresh，四trajectory/KL0，四奖励组合；hint错转对披露与QwQ32B文字一致性不是内部忠实性。Plain低置信表达覆盖改变AUROC人口，预算匹配也不隔离单一tag因果或系统成本。 |
| 09275 | paragraphs8–18、21–27、32–35、40–42、47–57：三seed/中文和翻译/800病例×四扰动，GPT4.1生成/判定与limitations不同模型字样冲突；三专家30题/Gwet子集，不授全部临床效用。80%重复bootstrap子集不能当十次独立实验；最多三次修补不证明所有约束总满足。 |

Z.ai page2嵌入nextPage3/hasMorefalse及“没有更多”实际核；Google October页2实际October7/2/1，next/last按钮disabled、data-max-pages2，末页停止成立。Seed pinned与PublishDate、DeepSeek十研究/五动态、Moonshot26条、MiniMax三入口、MiMo八Paper/十五Blog与More、Meta/Qwen历史壳限制均已核到所声明有限范围，原历史缺段不授Coverage。

新model/agent尾部相关完整题摘、必要信号与分层关闭抽检仍待作者收束和本复核者定点核验；本文仍未授DAY，旧三十二潜力及上述十二信号不扩大成全文队列。

## 尾部变化实际复核

实际读两尾页原Atom及执行记录，54/54的本窗提交发现切片交叉归并87标题、55定点完整题摘为作者范围。非作者完整读原返回版本的08966v2、09017v3、09827v1、09913v1、09541v3、09852v1、09338v2与09776v1题摘：graph memory、value gate、优化norm组合、segment模型切换、dLLM likelihood上下界、router倾斜聚合及条件理论均保留潜力，不以框架/应用名或小模型排除；当前v2/v3不冒充历史v1。没有将其余全部55题摘二次重读或把168响应转全文队列。

二十必要精确v1实际阅读下表text原响应位置，并对GloVE、政治评价、trait probe、数列judge、视觉mask与水印方法定点读原HTML完整段；较大输出被截断的09253及09351/09544部分已另完整读取。非作者读的是原文而非作者判断标签；不证明实现或实验复现。

| 身份 | 实际必要范围及独立限定 |
| --- | --- |
| 08750 / 09717 | 08750 text148–165/178–191/388–394；09717 123–148/186–207/432–433。PAN2014英语相似度与跨client隐私不同；FDR是集合平均错误控制，已知非成员calibration/分布相似/i.i.d.是必要条件，v1 subtraction estimator不借后版JKBB。 |
| 09253 / 09260 | 09253 138–162/431–453；09260 99–131/194–205/713。uncertain手工变public、类别不平衡与GPU不同不能识别模型规模因果；RLHF annotator只控有限标签，violent+anger子人口、seen/generalized ASR分开，不授全情绪或黑盒泛化。 |
| 08120 / 08132 | 08120 113–144/183–196/218–243/344–359/683–689；08132 366–395/642–649。LIME词支持的concept verifier与规则fidelity不等内部因果，18人理解差异不显著；domain分类错误/保留准确不等参数已删除数据，domain标签与CLIP few-shot/三seed边界保留。 |
| 08236 / 12818 | 08236原HTML paragraphs16–25/31及text218–224；12818 text86–115/135–157。八模型PCT三类annotator一致并不消除量表效度问题，persona/翻译人口有限；STS与局部人工低分位样本只能支持输出推理差异，不证明隐藏计算或临床损害。 |
| 09738 / 09905 | 09738 83–143/144–161；09905 83–104/172–181。三annotator/1,994人口中correlation、agreement与z阈值不同，human-like不是事实真值；81 persona bundle及memory注入有混杂，v1未提出缓解，不能借v2补历史。 |
| 09595 / 08931 | 09595 64–83/2895–2913；08931 99–127/482–503。季度cutoff无突变不证明无污染，pass@k与token成本分账；RADAR所谓causal effect/patching实为entropy proxy，30/100样本的93%不能认证训练污染。 |
| 09709 / 09008 | 09709 text83–98/453–456及原HTML paragraphs19–25；09008 text192–201/1837–1849及原HTML25/29。724×五模型、o3 judge有受限人工预评/两prompt；视觉PGD 200步、逐baseline阈值、mask损视觉/增加时延/Q-Former失效，不授无成本幻觉消除。 |
| 09714 / 09351 | 09714 119–139/146–158/210–223；09351 232–250/837–849。accuracy/adherence与BLEU不同，四cipher RL实验与结尾未用RL措辞冲突，不授监控普遍不可规避；八judge及PRM域迁移、greedy/T1差异，只测可见trace而非隐藏忠实性。 |
| 09544 / 09776 | 09544 164–181/665–683；09776 170–198/375–387。dLLM步骤与端到端时间不同，有限模型/BigGSM/单卡网格不证明所有结构失败；stationary AR(p)、高斯噪声、无Softmax LSA及teacher forcing/rollout区别，不外推完整Transformer。 |
| 08915 / 13829 | 08915 text117–131/506–516及原HTML20–22/26/38；13829 text382–394/807–834及原HTML14–17/20–24。三模型/英文首消息、probe可读与因果使用不同；POS lookup水印依赖corpus/tagger、0.5–1B/三语言三任务、500例/temperature.7和平均bias校准，perplexity非全质量/身份或真伪认证。 |

分层关闭抽检实际完整读09244v1原Atom综述、09898v2原Atom、08902v1原Atom BioNER与08588v1官方题摘，另复用Sonnet card修订和Google邻界；不把样本当所有范围外标题验证。**09898须局部重开**：本次官方精确v1题摘和HTML§3–5实际提出cross-framework评价不足、三指标及人类修复/不同ground truth人口，不是v2摘要只20样本/ICL的同一贡献描述。保留潜力与日期/版本，不据v2关闭所有历史事件；20例intrinsic由两个developer/test cases核，100例extrinsic无可运行test且costly LLM作ground truth，score相关<0.3、fix-step非真实耗时，不能授功能等价或性能保证。此定点反侧在20项之外新增一项；不要求全部附件。

其余关闭未见共同错误理由。08588开发集字典改善但blind test退步只能表述任务特定post-processing负例，未建立foundation机制或可迁移条件，不按医学名或“负面结果”关闭；08902 symbolic tagging/selector与双语联合属于NER任务方案，题摘只提供领域指标/泛化主张，无相关纠错信号。本轮不展开其余88标题或全年。

十四来源有限范围及原缺失、Sonnet卡片作者脚注无实质变化、Books无正面采用/提案/写入0、六部分均已实际核到终態边界。08158三策略窄修已在README/SCREENING读回通过。DAY仅余09898恢复潜力及99总身份/关闭1/潜力98与新增必要反侧的作者窄同步；同步后只回核变化，不重跑有效43原组或十四源。历史日期/版本/中心争议不授正面Evidence、Books、Coverage或无遗漏保证。

## 作者窄同步与最终DAY

结论：通过

实际回读最新README的§1/3/4/5/6、SCREENING尾页归并/关闭段/T2J必要限定及CURRENT_STOP：09898已明确从当前v2整家族关闭恢复历史v1跨框架评价潜力；99完整题摘唯一身份、关闭1/潜力98、原43必要作者阅读与新增T2J root阅读合计44且角色分开，没有将潜力授分数、正面Evidence或Books。二十tail、十二安全补核、原十一必要、八完整尾部潜力AB和分层样本、十四源有限停止及Sonnet脚注修订的有效独核复用，不再打开完整附件。

普通研究/Books/独立语义复核剩余0，正式候选/正面Evidence/Books提案及写入0。first-public、版本、历史目录缺段和原中心定义争议继续具名隔离，不支持正面证据、Books、Coverage、零事件、无遗漏或性能/安全保证；只在对应官方原事件/完全落窗bounds或作者纠错到达时定点重开。No Change基于无采用/无长期差额提案，不冒称全owner已有覆盖。

实际V3结构校验通过，机器不能代语义。交作者按本实际裁决同步完成态、§5/6与停点，再由root检查最终结构及计数；不要求作者再次审相同原件。本复核只写独立记录，未stage、commit、push或扩月份/Weekly。
