# 后七家族：必要原证与 Books 比较（作者实读，待非作者核）
本次事件均 exact-v1；补03/17日级夹证/实体见 SUP_SECOND_DATE，已校准潜力不等于以下 Source 通过。所有性能未明确项均 Not Disclosed，未跑实现或复现。HTML 采用 https://arxiv.org/html/2603.<id>v1；具体保留原文 O–Z，不遍历全文附件。

## 14893 — LLMs as Signal Detectors
准入差额：校准指标混合辨别与响应偏差 → 温度改变答案人口而不只是 criterion → AUC/ECE 不能当同人口能力改善。3+2+2=7，深入作者必要§2–5.5（METHOD O/P）。
三模型 Llama3-8B Inst/Base、Mistral7B Inst，llamaCPP3.16/Q5_K_M/Vulkan/AMD7900GRE16GB；TriviaQA5000与NQ3000、七温度168k试次；4AFC各2000。不把 mean answer logprob 当真值：teacher-forced gold 的 NLP 比错误生成低，fluency是重要替代解释。UVSD Gaussian 拟合用20等宽T1边界/10starts/10kbootstrap，Mistral quantile 与 parametric dA 有敏感差异；标签5%子样本1200出现30.1% mismatch和1.3% FP，不能由统一噪声主张证明跨温度人口无偏。AUC提高同时accuracy降低不证明latent factual能力提高；H2与H3并非普遍成立。未披露完整serving长度/batch/concurrency/SLO，心理学criterion类比不是控制器。
已有覆盖提案 PLATFORM-EVALUATION-SYSTEM/Ch66：实际1186明确 teacher forcing流畅度不等correctness，2515校准与排序分离并绑定decoder，2619–2621分别 reward/排序及population identity。采用的长期命题由这些正文承载；不采用精确Gaussian拟合为新通用定律，不加论文段。

## 14903 — ExPosST
原流式新增source会挤动既有target位置 → 预留source positions并在块满后另分配新块、按真实read/write policy构造训练mask → 缓存可复用性需训练时位置/可见性契约。2+2+2=6，因实际缺口深入§2–4及AppendixA（O/Q/X）。
slot默认16，target位置不因后续source插入改变；不是只改index就保证所有hidden states不变。已生成target不可看未来source，训练使用policy-consistent masking。Llama3.1-8B/Qwen2.5-7B、五IWSLT17语言对，质量BLEU/COMET与LAAL是算法延迟指标非端到端时延；GFLOPs会计非serving throughput。LoRA r32/alpha16，两epoch、batch64、BF16、AdamW2e-4/decay.1/warmup500/maxseq512；硬件/并发/SLO Not Disclosed。训练16而推理4/8退步，32/64不是全局严格差于16，mask消融示policy失配。
拟整合 MODEL-KV-CACHE/Ch19，实际229–237 Position/Prefix已有语义不变条件，但没有流式两侧交替追加的位置预留分支。仅一段插在Prefix语义后、Cache没有解决什么前；非Ch13编码公式或Ch45 runtime调度owner。需逐字PRE/窄锁后才写。

## 15159 — PriCoder
文档RAG提供API身份不等掌握调用 → 从API规格生成样本并记录生成provenance DAG、迭代组合与可执行/语法/语义过滤 → 可把调用策略作为SFT数据学习，而不无限加检索文档。图边(u,v)表示v由u合成，不是程序API调用的执行依赖，不严格要求每seed单API或所有调用。2+2+2=6，具体拟缺口深入§3–7.3必要Oracle、graph、main/ablation（Q/R/V/W/X）；root必要方法实核纠正图语义后窄修。
ndonnx/numba-cuda是2024新公开库，“private/unseen”是代理，不证明无预训练泄漏。GPT5.2知道库并参与任务初稿，五人约150h检查参考，169/187任务每项>9tests且≥4API。Oracle准确文档后仍失败支持知识暴露与学会行为分离，但不是所有RAG最优上界。6k/20k合成样本、初始/迭代1:2、三backbone6.7B/7B/8B，LoRA一epoch/batch16/8A10080GB，10samples temp.5/top.95；精度/完整token和制作预算/SLO ND。baseline超参在NdonnxEval上grid search，不授独立超参heldout；HumanEval RAG加入不相关库文档不能证明所有RAG损害泛化，PriCoder在两模型自身pass下降2.07/1.41点，不能沿用negligible无退化保证。图过滤依赖LLM自judge不独立gold。
拟整合 TRAIN-SFT/Ch29：实际222–240已有dependency-aware tool trace/teacher及filter偏差，但不是API schema→primitive调用→可执行组合图循环的训练课程。须只补这条具体数据生成分支，保留teacher/eval成本与原人工demonstration，不重复泛化trace合同。逐字PRE/锁未授。

## 15389 — When Does Sparsity Mitigate the Curse of Depth
准入：PreLN后层近identity与variance传播可能有关 → 稀疏mask/WD/context/GQA/MoE的条件化反证 → 降variance不等深度有用性或质量，不能只按稀疏率选设计。2+2+2=6，理论/设计反侧触发深入§2–4+B6/7+C（R/V/W/X/Y/Z）。
Th1假设独立随机线性权重与mask/状态、第二矩alpha与density rho，给上界而非真实trained variance，作者也指出learned mask打破独立。L12→32参数900M→2.3B不matched；least-squares layer替换lossratio>1.1“有用比例”不等可删层真值。WD1.2B/16layer/Fineweb5Btokens/batch128/lr1e-3，lambda.1 PPL14.83 vs0 15.63，却lambda3方差低/PPL773直接否定单指标控制。context T256→8192同token/反向步数不等相同attention FLOPs；8192质量更差。GQA参数/训练tokens均不同，B6把sequence分组独立head平均近似当GQA，实际共享KV不由该证明涵盖；B7均匀且独立expert的局部固定gate不能证明learned routing。MoE只matched activeparams而非total/width/router/shared；Hopper类别/混合精度，具体GPU/dtype ND，非真实在线SLO。
已有覆盖提案 MODEL-TRANSFORMER-LAYER/Ch17：实际245–260初始化传播不是训练永久保证，369–376有界信号与容量/质量分开，395–401冗余需实际干预。拟采用的成熟边界全部已有；新统一“稀疏调方差”在GQA证明/多组预算下不足以升级普遍规律，不另写指导recipe，保留候选与反证而非删池。

独立核定：局部实验与成熟边界 Source scoped/NoChange通过，但中心统一理论隔离。B6组内ng=n/G个独立均值应给Gσ²/n，非σ²/(Gn)；Eq85另加1/G、共享KV头非独立，Eq89从n项变为ng项，未连接实际GQA。§2 bounded norm借Weierstrass推convergence/identity亦不成立。单一中心请求：官方修正Lemma1到identity的必要条件、B6真实共享KV/聚合公式并连接C4实测。未取得前不授中心理论或通用稀疏recipe；不把隔离子命题算证明，不降分删候选。

## 15611 — Code-A1
固定tests不会随policy新错误扩展 → 分离code/tester策略、GT校验有效assertion再对错误代码学习 → adaptive tests不取得最终correctness authority。2+2+2=6，安全reward设计深入§3–4/Alg/F/A3–4（V/W/Y及原文定点）。
tester reward把validity和旧/新代码区分组合，TopVar只取G=8组中一组，并非collusion消失定理。GT答案oracle替换测试预期后才核candidate，明确需要可信solution，只支持单Python函数assertion；mistakebook删已通过与AppendixA3频率增减/零清除不是完全同一协议。9688KodCodeHard，Qwen2.5Coder1.5/3/7B，预先TestSFT/111GRPOsteps，code/test各8样本/test组5assertions、alpha.5；32samples温度.7/top.95 eval。mutation部分不如selfplay，测试validity提高不保证coverage。八H20/CUDA12.8/verl/vLLM/FSDP；资源表CodeA1单policy GPU字段4而baseline8，两策略+额外tests/GT/book成本不授matched total compute。sandbox10s/health30s/retries5只是受测执行合同。HTML日期宏Aug24不覆盖arxivv1 Mar16history，不据宏移公开归属。
**已有覆盖提案 TRAIN-GRPO/Ch33**：作者实际755–771正文已明确同一code↔test双策略、GT-validity、failurebook版本/过期、collusion/oracle/sandbox及hidden tests，2833本人CodeA1来源存在但不是凭末注授采用。所拟长期机制已在完整正文，No Change，不重复段落。仅保留本次实际必要原证/反侧。

## 14672 — Seamless Deception
规则/强梯度改写可检测不代表prompt隐匿可泛化检测 → unrelated故事黑盒同模与跨model+topic留出对比 → 未检出不证明没有隐匿，不能当开放world可靠保证。3+2+2=7，深入§2–5/AppA/B/E/F（live核心、Y/Z）。
三模型8B/7B/12B与5个非危险知识topic，construct honest/conceal label不等自然部署内心真值。RT/GA/DPO伤害style可被探测>95%；prompt策略现实leavebothmodel/topicout接近chance；更大detector和API模型出现单类collapse不证明永远无黑盒方案。闭源parameter size ND不采用headline“each>70B”。human10CS students/10样本有标注anchors，仅小样本人类诊断。多数inference实验8A40约46GiB/CUDA12.6/EPYC7502，concealer训练2H100另记；closedAPI实际推理硬件与完整batch/长度/SLO ND，不将concealer训练硬件误记ND。LoRA3epoch与detector通常<4/上限50分别计成本，seed5是图披露范围。reader必要原文实核后窄修。
已有覆盖提案 PLATFORM-EVALUATION-SYSTEM/Ch66：实际213人工organism与自然行为/能力上界分离，2286–2288 knownvariant检测与未知真值分离，4641–4652 detector大小/参考人口/FPFN/Unknown≠Negative/不能认证分数。采纳检测适用域与负结果限权由实际正文承载，不把局部conceal域改名为生产通用audit；No Change需独核确认。

## 15417 — TTRL Safety Amplification
自consensus可在无label测试期训练 → final-answer奖励优化数值/拒绝表面，harm+numeric复合提示绕过format filter → update/admission覆盖面不能代表完整completion安全。3+2+2=7，深入§2–4.5/AppA必要训练Table5（T/V/W/X+liveA）。
模型Qwen2.5 .5/1.5B、Llama3.2 1/3B及Llama3 8B；math-only并非全部恶化，但初始已高ASR模型Table1为90→92；Table2 harmful artifact injection同模型90→88才是该协议的直接反侧，两协议不合并。plainmix可被numeric admission挡住，HarmInject配数字仍通过。majority parser0/1不是独立safe oracle；refusal末尾一致性与harm ending多样性共同改变reward。混入60%AMC训练350steps不等纯250完全同math exposure；UltraFeedback50良性样本也有局部harm提升，不授通用能力提升或必然解对齐。reader必要原证实核后窄修。
ASR LlamaGuard3-8B非独立人类真值，eval16/temp.6/top.95；trainvote64/generation32/maxprompt1024/maxresponse6144/batch8/mini1/micro2/250step，actor5e-7/critic9e-6/KL0/LoRAr64alpha32/TP-FSDP8GPU，GPU具体硬件/精度/完整成本/SLO ND。不扩大附录无关taxonomy。
拟整合 TRAIN-GRPO/Ch33：实际730–749 correlation与false-positive触发/visitation已覆盖generic错reward，但没有“答案format admission漏整个有害completion”的TTRL具体差额。只一段接在相关错误→动力学→Verifier双策略交接处，采用工程推断：格式与安全门分别绑定完整prompt/response，独立回归/停更回退，不称paper提供保证安全filter。需逐字PRE及root共享Ch33窄锁后才写。

