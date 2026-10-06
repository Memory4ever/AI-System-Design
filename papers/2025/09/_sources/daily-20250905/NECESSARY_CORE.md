# 05 必要定点核心（作者，不自授DAY）

只读判断所需机制、控制与反侧；不是86篇全文完成。HTML优先，编号由本日inspect.py解析原件。所有日期潜力不得进入正面Books链。

## 安全、评价与失效反侧

- **03768v1 RAGuard** §3.4/4.1/4.2/4.3/5.2/5.3（45–63/69–75/85–95）：双索引固定knowledge/safety槽位与overfetch只保证配额，不保证法规语义；100人工问题，dense基础technical/safety recall=.925/.0425，RAGuard=.665/.5175，SafetyClamp=.790/.4375；全条款compliance仅7%/6%，其余接近0。保留配额/完整覆盖分离的反侧，不授“绝对安全”。CPU本地indices和4K假定不授端到端LLM速度。
- **03888v1 probes** §3.1–3.2/5/6（19–30/39–54）：ID20%split，OOD换benign/malicious源；GPT4o清洗保语法去恶意、再改instruction格式，XSTest安全触发词检假阳性。近98%ID与15–99pp OOD下降属于实际组合，不泛化所有probe失效；清洗/改写分布混杂存在，不能证明模型完全没有语义理解。
- **03647v1 evaluator steering** §2.1/2.3/3（9–14/24–29）：XSUM1000，Llama judge/GPT3.5候选；gold为Phi4/DSV3/Claude3.5多数（不是独立人类真值），翻两顺序排positional，分合法自偏/非法自偏/无偏。97%偏票翻转同时合法票不稳定；不把flip率当faithful评价或通用guard。
- **12221v1 MEUV** §4.4–4.6/5.1（73–113）：encoder→投影→敏感topicprototype→rank1方向干预；分桶多forward成本随topic桶数M增长。约束要求逐样本softplus小、CE gap单调/Lipschitz和可选hidden Lipschitz；router误路ρ必须计入，不由近正交自动推出行为安全。GPT3.5合成zh/en三topic+harmless，ASR是无拒绝串/firsttoken快速指标，不是任务有用性、授权或通用不泄露证明。
- **05367v1 TRIAL** §3/5.1/Limitations（18–30/34–39/56–58）：保留伦理dilemma多轮顺从压力与judge+人工复核界限，不抄具体攻击模板。GLM4plus攻方经选择、GPT4o helper可能拒绝；不可框为较小恶的任务和强对齐helper是失败边界。未建立“推理越强必越不安全”普遍因果。
- **05362v1 scambaiting** §4.1/4.2/4.5/5.2.7–8/6/AppendixE（45–63/96–105/148–161/260–279）：FedAvg10模拟clients/30round，0.1/0.8 noise非完整ε/δDP账户；engagement为lexical diversity/length/question bonus、relevance为SBERT，低PII打分不证明实际无泄漏。§4声称secure aggregation，§6说可进一步加入，实施状态不一致。保留moderation/utility/风险测量取舍，不授real-time真实诈骗保护或梯度重构安全保证。
- **03730v1 Personality Illusion** §4（65–76）：traitpersona三提示方法；logistic回归控制prompt/temperature/model，selfreport变化显著但risk-taking/sycophancy行为变化弱/不一致，只局部行为任务，不授真实“内在性格”。
- **03736v1 behavioral coherence** §3.4–3.5/4.1/4.2/4.3（48–53/57–61/76–89）：美国家庭人口属性、openness/preference两维、LLM judge依agent换模型；最大偏好差仍3.5–3.7/5 agreement，Bonferroni六检分表面趋势与深层对话一致性，不外推所有人类替身/任务。
- **03805v1 grounding** §3.2–3.3/5/6/Limitations（38–45/71–83/90–108）：150selfplay games三轮；提取precision .99/recall .55/F1 .66有漏收，不能拿高precision授全量。56/150轮相同GT可inflatesuccess，GPT4.1差1.10 vs human .08；no-guess-sharing提示减弱。CLIPScore高不等于协作成功，架构/训练透明性不足不能归因RLHF本身。
- **04373v1 gender metrics** §3/5.4/6（24–30/64–80）：四任务2×2 salience/instruction设计，有些任务组合不成立；>60%非pronoun时排除，会改变小模型分母。discrete翻转放大vsprobability稳定不是潜在偏见消除；“testing mode”是解释假说，不证明意识到测评。
- **03615v1 OCR** §II-B/III/III-A/IV（23–26/35–53）：同图/标准prompt，T4+4vCPU16GiB，groundtruth对齐的semantic打分由Qwen3-8B；proprietary54languages，专用pipeline仅支持5languages。F1 .457/precision .5426等只局部模型；CPU实际比较QwenVL与Sprinklr，8coreXeon64GiB，69.38s/10.8GiB vs4.36s/.89GiB，不拿专用pipeline15x/35x或复合归一分92.6授全资源/全语言优胜；保留边缘资源反侧。
- **04534v1 biomedical quantization** §2/3/4.2–4.5（8–25/30–37）：4/8bit BitsAndBytes NF4、doublequant+fp16 compute，12模型8任务；实验主要4×A10040GB不是消费40GB单卡部署证明，latency受load影响。§2.1/3明示减weightmemory却增加response latency，§2.2 HuatuoGPT-o1/Med42 8bit局部严重下降而4bit不能概括同趋势，§2.4 longprompt仍增长KV。恢复有限precision/memory/latency/任务非单调反侧潜力，不能以“量化已知+医学域”关闭，未授安全/可靠保真保证；root FIRST认可恢复，核心仍交DAY独核。
- **04537v1 social dynamics** §2.2/3.2/4（15–18/28–40）：同GPT4o引擎、memory回注、1000steps/10runs、crowding阈60%；观察clustering先于crowd与不完全优化，但没有分离prompt/context/communication/pretraining的因果控制。“pretraining内在动机/非prompt artifact”不成立；仅模拟行为轨迹、不是新模型/系统机制或已核安全反证，拟贡献关闭。

## 精确撤回/恢复，不全家族偷换

- **06996** `abs-06996.raw` 当前明确“paper withdrawn by arXiv Admin”，v5=2025-12-01 1KB withdrawn，generative-AI authorship policy；v1=09-04 2623KB，旧HTML可取得不撤销当前article警示。取消本次候选/潜力与正面采用链，保留v1题摘及撤回证据；不无依据指称所有实验虚假或将v5日期移动进本窗。重开需官方撤回解除/有效原始替代并核当窗版本/事件。
- **04104** `abs-04104-v1.raw`明确本精确v1 withdrawn/license权利，`abs-04104-v2.raw`官方历史v1withdrawn、v2=2025-11-04恢复VoR相关DOI。排除当窗v1，不撤销later有效家族；v2不冒充09-04已可采的版本，不为避读把当前版本删除。

## Anthropic官方安全论证

[biorisk](https://www.anthropic.com/research/biorisk)，原件0–44完整已读（不是生物操作建议）：expert quiz→internet-only vs去safeguards Claude4两日plan由专家rubric评分有uplift；2024basic wetlab n=8未见uplift，计划更大study，不把文字计划授实际实验能力。input/output constitutionalclassifier对无法排除能力uplift的Opus4 precautionaryASL3，既有classifier架构不是新算法；评价代理/现实能力断层有具体有限反侧。独审发现正文article:published_time/datePublished/visible time均2025-09-05T00:00Z，root实际独核接受当窗08:00BJT发布事件，正式2+2+2=6；原配置-only hold撤销。dateModified=2026-07-08T20:53:48Z仅标当前正文版本，不授所有文字冻结2025。采用是明确的LLM安全measurement边界，不是科学应用、安全风险已实证或新classifier算法，Books由root具体正文比对裁决。

## 理论、训练与生成的必要假设

以下也是实际定点读核心，不是仅获取原件；公式/表格只有直接影响本段判断者进入采用范围。

- **03733v1** §4.1/4.3/6.3（34–46/54–60/145–148）：soft-anchor可微range entropy及halfspace-aware修正，data-dependent margin bound含margin与复杂度项；结构注意力正则只train时施加。结论依赖非平凡margin与指定range family，不授所有attention运行时稳定性；训练开销保留，不用理论标签授无条件收益。
- **04154v1 AFA** §2.1/3.2/3.6/4.5（9–14/124–125/145–150/276–281）：线性SDE、零均值Gaussian noise、可逆C、可对角化A/Q等前提；full算子代价m²d³，naive tensor中间量m²d。等实部与isotropic noise才降为实用矩阵运算；小角度/变换后常模长使RT近似NormAttn，而非任意dot-product attention的精确Bayesian filter。未遍历无关证明附录。
- **04419v1 UPG** §3.2/3.4/B.1（28–41/59–73/145–149）：expected reward减固定behavior-policy adherence KL，reference换测度须覆盖policy support；mask/clipping是稳定化surrogate。HPT用多verifier rollout表现阈值选择SFT/DrGRPO，不把推导授任意clip下无偏、无目标冲突或安全收敛。
- **04063v1 ARFM** Method（38–59）：标准化return指数重权flow loss，alpha=0回到vanilla；大alpha提升梯度方差，自适应J做收益/方差取舍。bisection对应R与CFM loss的正态近似，大batch估计moments；不授任意数据分布、全局优化或稳定性保证。
- **04027v1 CoT space** §2.3/3.1/3.2/3.3（39–53/56–66/71–91/97–107）：连续语义空间、到可达正确答案的距离损失、无偏噪声估计与white-noise SGD类比；PAC-Bayes是iid有界0–1条件。泛化上界随verbosity增大、经验损失下界随长度减小，不共同强制真实expected risk呈U形；保留中心论证争议，不采用普遍最优CoT长度或RL收敛断言。
- **03581v1 dynamic planning** §3/5.3/Limitations（24–47/82–91）：单个LLM的三概念policy，不是三个实训模型；planning advantage未显式计算，token penalty、可暂停游戏使latency≈0。8B SFT重要，早期动态规划有利但后期plateau接近；自主Best-of-N100与human20不同budget，不作matched普遍成功/实时保证。
- **03646v1 HICRA** §2.1/3/4.3.3–4.5（20–30/50–59/79–87）：成功rollout 3–5gram经Gemini标注/manual扩展标出策略token，是proxy而非已证内部planning；正/负credit非对称放大，alpha=.2。Llama3.1缺procedure foundation时探索可损GRPO，保留成立前提；高分叉semantic entropy不独立证明规划因果。
- **03803v1 CaPL** §3.2/3.3/4.3（21–44/61–70）：Brownian bridge shared→class-specific CLIP feature，交换shared s_i/class d_j经MLP并赋label j，辅以self-reconstruction。feature swap、t-SNE与cluster不证明真实因果可辨识；15dataset和训练耗时是局部范围，潜力来自可执行分解接口而非“causal”命名。
- **03934v1 SelfAug** §3.3/4.1–4.3/Limitations/AppendixB（33–40/47–71/93–103）：原模型input-logit KL与response NLL分位置，reference多一次forward；CRAG官方validation训练/test评估，RAG-Instruct及IFEval/MATH等检查遗忘。五次实验取best、grid search不等于均值置信；logit shift与IFEval下降共变不独立证明所有遗忘因果，知识分数未明显下降。>32K/full-finetune扩大验证尚未完成，不授无成本或任意模型稳定。
- **04185v1 SBD** §2.2–2.3/4（23–39/59–70）：causal prefix+双向block，NTP/MATP共同训练，exact KV是prefix reuse，不是native NTP联合采样分布等价；后者还需条件独立。entropy阈值调质量/并行取舍；3–5NFE降低与H100 FP8 roofline推算wall-clock不同，不当实测3–5倍runtime。

## 局部可靠性与评价信号

- **03626v1 KG-SMILE** §4/5.3/5.4（49–57/90–97/141–156）：图组件移除、response inverse Wasserstein/cosine similarity拟合加权线性surrogate。所谓faithfulness是10prompts ATT-AUC与外部模型benchmark accuracy相关，T0=.933/T1=.070，不是内部reasoning因果真值；Jaccard只稳定性。保留图扰动接口潜力/中心faithfulness争议，不采用解释真实性保证。
- **03990v1 MPR** §3.3–3.5/4.2–4.4（31–59）：C(s)验证后resample/fallback只覆盖已写约束；failure predicate训练更新、部署freeze。60train/74test，MPR一次对Reflexion六次test refinement的适应预算不同；87.8/86.9不能独立证明通用优胜，训练不授现实全安全。
- **04304v1 Facts Fade** §3/4/5/6（23–51）：16,501 review记录/512结论更新；gold人工校订与silver抽100(问题95%、标签92%)分开。old/current label宏F1比较存在模型异质差异（Llama+7.4、OLMo+2.9），不能把全部LLM描述为同方向失效。OLMo Dolma ngram频率仅相关，closed模型cutoff未知；不把预训练归因当受控因果。
- **04059v1 sheet-music** §4.1/4.2/6（33–41/62–64）：规则可验题、text/image版本与shuffle；visual Gemini55.44 vs text DeepSeekR1 93.63不是同模型matched因果perception证明。8192tokens/T=.7，GRPO300steps 128batch/8rollout、无KL/entropy只是局部训练条件，不能推所有跨域reasoning转移。
- **03867v1 Drivel** §3.3/3.4/4/6/Limitations（25–38/47–59）：7annotators(4作者+3paid)、排争议；GPT4.5distractor/GPT4.1judge非独立全语用真值。约半中文、零样本三prompt平均、大budget未验；文化/主观多解限制，实际盲区不证明所有LLM只能统计而无理解。
- **05378v1 Code Like Humans** §6.1–6.2/7/Limitations（76–83/95–114）：expert spans对agent+retriever分离提取/检索故障；加hard-negative候选含gold oracle不等于真实检索recall。罕见/高频code取舍，MDACE/MIMIC同院/有噪声且未全70K codes验证，不授端到端临床安全。
- **2510.24719v1 itinerary** §3.1–3.2/4–5（17–33/57–77）：无overlap、min API flightduration、max 2×min、minstay两天；确定性shift后重验。三模型各100、4–6城；“100%正确”仅所定义可调整实例/约束，不含已发布航班、签证、预算和所有deadline。缺格式retry影响原始分母，三次reprompt仍可引新错。
- **04198v1 computer-use** HTML404，PDF物理7–9/11–12：UiPath2023.4 Community vs ComputerUse commit99502f5/Sonnet4-20250514/computer_use_20250124，Ubuntu Docker/16,384tokens/last3截图。P2 agent9/10 vs RPA10/10、109.8s vs53.9s；P3只首4invoice agent6/10 vs RPA10/10、202.8s vs20s，不授全分页流程。开发时间单人stopwatch/RPA内计时、P3 prompt适应迭代，不是生产统计保证。
- **03828v1 OMOP MCP** HTML404，PDF物理3–8：FastMCP/Claude或GPT4o keyword→Athena REST，48 MCP/NoMCP同prompt对照 validID100% vs0%，5.49s vs2.13s。150词human142/150有效，共同142中模型12/142(8.5%)语义错误，human多候选取最好而LLM单候选。tool-only真实catalog ID不能授语义正确/零幻觉；root FIRST保留这项有限counterevidence，非MCP新算法。
- **04343v1 persona agents** §3–4.3（21–32/42–62）：60问自报persona不是独立人格真值；固定独立vote/共享blackboard/private reflection协议，NONE/EXPERT控制，writing/game local测试。Thinking/Feeling条件defection .9/.5、switch .07/.16、honesty .54/.33局部行为差；message/action不绑定，不泛化人格真实性、心理因果或安全，root FIRST实际核核心后恢复潜力。

## 后补必要安全反侧（非新增发现队列）

- **03787v1 adversarial RAG** §3–4/Limitations（40–80/83–119）：22/27 TREC queries、单/配对/512words overlap256 passages和8:2 evidence skew；GPT5只单文档，其余组合GPT4.1；Gemini stance judge与GPT4omini kappa .90/.82而非全部人类真值。TREC2021 neutral helpful98.2% vs harmful37.7% vs Liar4.4%只所选条件；helpful占优可恢复，order差CI多重叠。top10 MonoT5已有pool实验不等于全实际retrieval安全；training exposure解释未受控，不授任何size/architecture都必失败。
- **03985v1 NeuroBreak** §5/7.1/7.3/8（60–81/100–131）：linear lasttoken probe 3600:400训练验证，SALAD classifier评ASR；SNIP attribution去utility neuron，parameter alignment+activation projection四象限，再gradient影响/实际break干预。Llama3百analysis/百eval每attack，Full/LoRA/TSFT对照<.2%更新；部分case打断后和probe方向反侧不一致，说明方向不独立授真实安全因果。synthetic既有attack、非线性与动态attack未验，不授全jailbreak防御或完整内部安全机制。
- **04018v1 FPC-VLA** §III-C–E/IV（26–83）：gripper变化阈值触发supervisor，Yes/No定向离散修正，pose相似度+衰减融合不用于gripper；成功轨迹导出的grasp关键帧不是全真实失败counterfactual。最多3次supervisor、非关键.176s/关键1.766s；真实5tasks×32、每task1000in-domain demo+1000correction pairs。移除模块/pose perturb局部反侧可留，不授碰撞/人身安全、所有动作覆盖或无延迟执行。
- **04292v1 Inverse IFEval** §2/3/B.1（16–35/38–56/75–81）：1012=506zh+506en，八非惯常指令types；最佳pertype judge/template/sys优化88→98%是在其人类校验协议，不授全OOD真值。thinking/nonthinking比较、普通IFEval排名变化是失效切片；SFT习惯归因缺隔离训练干预。Best-of32挑最高评分不是自主已找到正确答案，不授训练后必改善或安全指令逆转。
- **04403v1 RMS** §3.3–3.4/4.2–4.3/Limitations（22–43/60–84）：COCO pattern→LAION augmentation，由Gemini生成、InternVL review+500人工抽样；safety response显式揭risk可产生judge shortcut。InternVL被选judge再评direct response非独立金标；同大小dataset训练比较支持局部隐蔽跨模态评价界限，不由22%安全率外推真实部署风险或通用安全。只一个inspiration case，未验所有分布。
- **09700v1 CLAP** §3–6/A.2–A.3（23–75/82–87）：所有layer EOS降维128+encoder，greedy+同prompt sampled同batch；threshold取ID val，先greedy→alternative→abstain。不幻觉率是non-abstained分母，ROUGE1 .3/YES-NO surrogate将refusal也当non-correct。2B–8B/三个closedbook tasks，OOD是五dataset二十pairs，不覆盖03888那类prompt-trigger clean反侧；所有layer因果/大模型与全域安全未验。

## 决定准入所需的关闭补读

- **03658v1** §3.3/4.2/5.4（36–44/62–67/89–94）：isotropic规范化保纵横比、16 PCA白化保99.7%variance、diffusion MLP与scene Transformer组成已有轨迹配方；sparse-route较endpoint多future信息，−40%minADE没有隔离信息量或新物理控制责任边界。root独读同核心认可关闭：不是按车辆领域/小模型标签关闭。
- **04549v1** §5–6（55–58）：线性FFN/近正交rank1是既有ROME论证概述，prompt/LoRA/PPLM/ROME/advfinetune为illustrative比较，未新增数学证明、成立条件或受控反侧；Banach/Hilbert类比不授新理论。root核心FIRST认可关闭。
- **04250v1** §2–5（26–38/49–60/82–105）：Llama/MedGemma生成临床Poisson-Gamma超先验、单NSCLC 468人125sites、LPD与subsampling仍以患者/试验设计为所得对象，无模型形成/LLM系统评价/Infra增量；科学应用本阶段暂缓。80%固定测试LPD略优不能自行推出同统计功效或实际少招患者；这个批评不另造主线贡献。作者、DAY reviewer独立发现同范围界限，root完整v1题摘FIRST认可关闭。

## DAY定点反例补读

- **10526v1** §2.2/3.1/Limitations（25–61/90–95/123）：网络DAG/topology GAT特征、定长group binary channel mask；n=1组合优化，n>1序列决策。self-competition按FLOPs先达目标再优化accuracy，不是hard runtime/所有episode不越预算的保证，resource仅实际FLOPs非端到端latency/HBM；EMA reward nonstationary，作者Markov论证不作为普遍定理。CIFAR VGG/ResNet训练轨迹是局部控制，policy绑定architecture/dataset/target，LLM/ViT和超大模型仍future，仍有模型压缩决策的新接口潜力，不因CNN关闭。
- **19305v1** §III-B–E/IV（33–65/69–88）：生成states非actions，Haar DWT低/高分带、STFT+CFFC跨频条件、双diffusion→IDWT+inverse dynamics动作。D4RL四环境/H96/五seeds，loss首/末10frequency modes ratio比较Decision Diffuser；Hopper none/low/high条件消融支持有限匹配，不能从loss ratio授真实动力学/闭环稳定证明或所有扩散模型结论。真实环境/high-frequency噪声优势只是future理论解释，不授实测安全。
- **04169v1** 只需完整题摘（`exact-title-reopen-v1.raw`）：LiRA适配+forecast DTS攻击、LSTM/NHiTS数据用户/记录实验，echo LLM未给可迁移privacy机制；root FIRST认可具体贡献关闭。HTML请求404保留原始记录，但不是必要全文受阻，未为足判再遍历PDF。

实际作者核心：44个arXiv家族（含准入关闭的必要补读）+Anthropic1，共45；另2精确撤回状态轻核。68 arXiv潜力保留日期隔离，未授全89 FullEvidence。root FIRST实际范围是20完整题摘+8潜力完整题摘、后续04343/03658/04549核心、04534改判及04250题摘/03828边界，新增10526/19305/04169三个精确v1完整摘要；另Anthropic全文与出版字段/Books独核，不冒充日级DAY。
