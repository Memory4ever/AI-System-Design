# 定点原文边界 — 2025-10-06

这里只维护必要安全/反侧与含糊准入事实。35份exact-v1 HTML和1份PDF实际读下列位置，不宣称完整全文/附件审毕，不授日期隔离材料正面Evidence。文本行号只为定位；原件和请求均在本目录。除04145外文件名为 `core-2510.ID.raw` / `.text.txt`；04145是 `corepdf-2510.04145.raw`。下载、提取、后续机器pass均不证明阅读。

| ID | 实际位置与最小判断 |
| --- | --- |
| 03984 | §2/3、购物§4.3 Session B（text95–128、295–315）：两persona跨session可见prior偏好carryover稀释新目标；是评价盲区/有限case，未测真实长期用户满意度 |
| 03992 | §3.2–3.6/4.1–4.2（133–181）、§7：inject-only攻击者不能改原工具/retriever，M300/top10、k5、R1/5/10，五seed；每次完整trial一个Bernoulli，95% Clopper-Pearson只约束指定intent+refinement分布，不把文中worst-case措辞外推任意攻击/已授权effect安全 |
| 03993 | §3.4 Theorem1（179–191）：有界/Lipschitz loss、伪标签error及Rademacher项和risk reduction前提；不由Bayes-optimal用词推出任意未标注分布的无条件泛化，Appendix H限制未逐项读 |
| 03999 | §3.3/4.1/4.2/5（126–141、201–220）：后验auditor读全轨迹，14任务、20轨迹、跨模型共同事件seed，trust也是supervisor模拟状态；欺骗/信任相关非真人长期部署因果保证 |
| 04013 | §3.3、6.1、7（151–160、488–502、568–586）：首tokenhidden state可预测受测正确性，PKS在TriviaQA有信号但MMLU近随机；预测分类/AUC不是verifier，不推通用校准或保证答案正确 |
| 04019 | §4.1/4.3/5（116–156、166–178）：MC在真实unmask timestep上重建masked状态，μ=1完全on-policy；LLaDA8B LoRA、固定长度与训练/评价remasking不同；不把无偏估计推成无限预算优势 |
| 04020 | §5（140–152）：SEVIR/Marine Heatwave/PDEBench/CFD与CSI/TKE等科学任务，按scope关闭，不借World Model字样重纳入 |
| 04023 | §3（232–239）、§7.3（902–905）：作者587→约200→45文献筛选，2023–25；>90%说的是所选论文缺显式机制，不是实测事故率/全行业风险，不声称复核45系统实现 |
| 04031 | §3/6（98–115、236–240）：counterfactual不翻类时回DP，替换器偶改非mask词产生DCR噪声；行为决策改变不单独证明faithfulness |
| 04032 | §III-A/D、IV（84–91、130–144、285–301）：17模型、MedMCQA/MedQA/PubMedQA/摘要Unitxt EM/F1；有通用优于专训的局部负结果，非ED患者流程/风险/硬件可用性验证，表含9B与“≤8B”叙述需保留不一致 |
| 04041 | §3.2/4.1/6/7（105–116、245–263）：100 curated SIMPLER轨迹、oracle simulator奖励，增加动作选择计算；真实部署、失败state暴露、确定性world model均有限，不推sim成功即闭环安全 |
| 04045 | §2/3.2/6/7（71–85、102–108、367–372）：VK/OpinionQA、Llama8B/Qwen7B；Claude3.7从CoT重建答案只测充分性，Moderation API测offense；需in-domain labels、1500–2000 A100h，不当mechanistic忠实性/无害证明 |
| 04058 | §3.3/4.1/5（137–164、345–350）：Markov Gaussian kernel和参数mean-field假设的variational目标；DDPM三数据集/SD feature实验，分布近似可能无效，不推出精确抹除/不可恢复 |
| 04067 | §4.2（277–290）：Qwen/Pythia/GPT2及mixed，Wiki/C4/GitHub log-log拟合；EE拟合好而其他项不稳，是受测相关性，不证明所有frontier regime因果驱动 |
| 04071 | §3、4.2–4.6（168–181、236–256）：Qwen3-0.6B架构、3B sampled token、120epoch、BF16；AR+mask几乎FullDLM、MLP dropout/weight decay亦改数据效率。保留替代原因，不因小模型关闭，也不泛化单epoch/frontier训练 |
| 04081 | §3.2、5.3（151–174、496–504）：无题目CodeCoT生成仅执行/结构过滤，不匹配known answer；100K质量比较用Qwen3-32B judge，验证后仍有错误。可执行≠NL问题语义正确/无污染 |
| 04120 | §5.2/5.3/Limitations（365–381）：context移除/shuffle局部反例；English、无few-shot/finetune、dimensional reduction选择未定；行为实验不证明真正内在repository机制 |
| 04142 | §2.1/3.4/4（108–119、450–459）：多教师轨迹concept drift形式化、MIMIC-CXR MT/APO消融；MT单独部分病种退化、APO改善，不推所有异构teacher无偏、跨域/临床部署有效 |
| 04145 | v1 PDF pp15–16、24–25（另结果例pp21–23部分）：两位建筑经验researcher各25报告与Copilot75报告；法规人工逐条核验，例中harness遗漏/无关training规定。有限人评真实存在，不能写全自动合规或零遗漏；贡献关闭不抹去安全反侧 |
| 04212 | §3.1/3.2、4、Discussion/Limitations（82–103、216–236）：GPT2/OpenWebText同batch replay，4A10080GB、BF16 forward/FP32 backward；重复max使PV舍入偏置，动态softmax shift β2–8可underflow，β7复现稳定；特定失败修补非所有FP8/大模型通用稳定保证 |
| 04214 | §5/8/Limitations（142–152、170–175）：Qwen3-32B LoRA64、best checkpoint，30生产conversation约150turn+45badcase约225turn，人expert主评。GRPO reference失败未报告为同等baseline，不能外推通用reward-hacking免疫 |
| 04226 | §4.1/6.1/Limitations（125–138、203–207、287–289）：27模型、200prompt、20网页baseline；分解双annotatorτ=.53/.39、LLMjudge相关.60/.68，有真实有限validation但仍噪声；claim diversity不等事实准确/所有RAG |
| 04234 | 方法constraint projection、§V-B2/3/4及adaptation（185–202、309–310）：对生成joint position/rate逐元素clip与reward；1k仿真环境/3ksteps，投影计划变量不能推出闭环真实状态安全；保留模型/执行误差 |
| 04257 | §III-B、VI-C、VIII（112–120、282–283、637–641）：77任务三网站，自动score>.8作ASR，作者称manual/rule validation未披露该段样本量；stealth与效果有显著取舍，不把ASR写任意真实网站事故率 |
| 04284 | §3.1/3.2/4.2、伦理/Appendix C（144–170、733–736、767–774、1744–1758）：LLM patient+LLM reward，安全veto优先；五非医学annotator判断体验，明确不适于直接clinical。真实human validation成立但非专家准确性验证 |
| 04303 | §2/4/6/7、A.1/A.2（78–125、145–150、184–192、240–252）：MI bounded estimator需独立seed及期望等于真实MI假设，A.2将无偏等式直接使用；200seed/task和600审计不证明10^-3总体FPR，OR多个检测器尚需合并误差控制。保留理论/校准未充分证明，不采用通用collusion保证 |
| 04311 | §2.2/4.1（61–86、92–105）：独立capability/agent output、q相同、正确聚合概率r假设；900 DyVal+2500写作、Qwen2.5-32B debate，深度相对gain不意味着绝对成功或同token成本普遍优胜 |
| 04317 | 架构/IV（106–135、271–285）：用户选择DP/EO/mitigation，Adult/LawSchool，threshold .02–.09、误差约±.005是受测局部控制；不替代规范公平定义、不保证任意敏感数据 |
| 04340 | §2、3.2、4.4/4.5、5（149–162、185–191、244–253）：GPT4.1与Qwen7B replication线索；训练提示可局部抑制trait，test prompt易重诱发、单token差异/traits耦合、只研究SFT；不是unlearning或永久后门消除 |
| 04347 | §3.2/4、5.1（85–96、165–174）：input-agnostic rare-trigger攻击、BERT/DistilBERT/ALBERT分类、20%clean validation；95percentile/ALBERT65校准不同。不能从encoder实验推出decoder通用防御 |
| 04365 | §IV-B、V-D、Limitations（123–135、331–335、539–542）：dual-head预测历史噪声/坐标log variance并传递、A80080GB100epochs；interaction-heavy UNIV适应下降，未验证复杂交通部署，不能推行人安全 |
| 04371 | §2 Assumption/Proposition与side effects、§4（218–236、304–314）：并发预启动无外部effect/可rollback，指数独立latency和猜测；“lossless”不含OS lossy last-write-wins，后者不能抹去中间effect/已有性能损害；额外calls成本仍存在 |
| 04392 | §2.1/3/Discussion（75–86、154–162、527–530）：固定retrieval分解生成/端到端一致性，GT参与paraphrase生成；lexical BLEU reward偏表面，一致错误亦可一致，非safety-critical部署保证 |
| 05173 | §3/5.1/5.2、RQ6/Discussion（182–195、258–271、779–803）：EOSrecognizer的19860样本约80%训练；NudeNet代理检测P4D、两类EOS adaptive，AASR1.84%限受测攻击/SD1.4；无证明任意攻击或所有unsafe类别上界 |
| 05179 | v1 §3/6（115–143、250–261）；本日own官方六月页Highlights/Methods/real-v-eval限制（10–18、48–60、125–139）：16模型、虚构binary dilemma，无真实部署misalignment证据；CoT“认为real”不能证明真实belief。中心命题六月首公开，未将Oct arXiv收录当新安全结论 |
| 08595 | §3/5（58–67、138–145）：1000 GSM8K training-split、GPT3.5生成/GPT4omini分析；整trace失败给每句失败标签，可混杂后续错误与句类型，judge待验证；不是句级能力因果或human认知结论 |

## Books窄决定

0正式候选与0正面Evidence，因此0Books提案/写入；不能据此宣称所有潜力已有覆盖。定点比较04371相关现有owner [AGENT-TOOL-CALLING](../../../../../books/part-07-agent/78-tool-calling.md)“可预测的只读调用可以与Decoding重叠”“Speculative Effect必须延迟提交”（实际body724–745）与相邻 [AGENT-PLANNING](../../../../../books/part-07-agent/79-planning.md)开头typed plan/belief/observation（1–52）：现正文已区分provisional和commit、可取消只读/权限gate、误预测成本、不可逆串行回退。论文的指数独立latency推导与OS lossy实验未形成可直接采用的长期差额；日期/独立校准若恢复后只重开该family，不能预先在日报§3填“已有覆盖”。其他潜力未作正文覆盖断言。
