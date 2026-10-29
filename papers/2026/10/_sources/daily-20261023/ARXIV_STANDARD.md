# arXiv 标准必要审阅 — Daily 2026-10-23

窗口：2026-10-22 BJT自然日。作者：oct23_live_arxiv。本轮只写本文件与必要原件；不再扩发现，不改ARXIV本体、报告、State、Books或索引，不stage/commit/push。

本轮预告root的10家族：2610.29378、2610.29498、2610.29545、2610.29671、2610.29832、2610.29933、2610.28770、2610.28871、2610.29427、2610.29965。均原5–6标准层；不重做root8、ORG15及本人此前18项有效Source。28714真实TAG纠错线索另外定点核，不计这10项。标准审阅核问题/机制/对照/收益/全费和边界，actualowner足够可NC/仅报告，不默认写Booksgap。

## 公告分组定点复核

原始12页保存于[日公告原件](./arxiv-official-listings.json)。原件有各页日期和New/Cross/Replacement数量，但每条entry未单列group；新增[201ID精确分组映射](./arxiv-official-listing-groups.json)，仅依该页原有entry顺序与各section计数标出组，不从submitted推公开。原页若缺0条的分组，其计数按0；position沿原页连续编号。该派生辅助不替代原始页眉/内容审阅，不证明全球firstpublic。

root已存Books8篇均不是replacement：28895 CL New#13/LG Cross#159；29348 LG New#73/CL Cross#120；29136 CL New#22/AI Cross#121；28671 AR New#1；29013 CL New#18/LG Cross#172；29210 CL New#28；28947 LG New#33/PF Cross#2；28815 AI New#5。原页日期均Oct22。

三个次日v2 cue的本窗事件亦明确是New/Cross，而非replacement：29385 LG New#77/AI Cross#147；29680 AI New#52/LG Cross#219；29203 RO New#23。因此恢复exact-v1是恢复本窗首次arXiv公告对应版本，不是借replacement重收旧v1。其后来v2不能因submission在Oct22而自动归本窗；若出现独立重要revision公开信号，再只审该实际版本，不普遍diff旧稿。

201ID中仅28620/2603.03403列Replacement，均此前已排除；其余有New/Cross关联。28637另有ACM Sep2更早正文线索，仍退出Oct22首次候选；不能从New组推全球firstpublic。

## 标准层材料

本文件分批保存实际已读的标准层与actualowner比较；没有保存的Source/独核/实际Books，不预签完成。以下版本均exact-v1，日期/身份沿既有公告精确映射，不以正文submitted替公告公开。

### S1 — 2610.29378 OnQ；2+1+2=5；建议Books No Change

原件：[exact-v1必要文本](./arxiv-standard-source-2610.29378.txt)，官方[HTML](https://arxiv.org/html/2610.29378v1)。实际读§3.1–3.2方法、§4评价/§5主结果、§6.2控制及A.2–A.7必要协议；没有核实现或复现。

旧约束→增量→选择：固定teacher轨迹不覆盖低比特student自身错误前缀；OnQ让冻结BF16 teacher在量化student自己的rollout上给下一token分布，更新latent权重/scales、固定zero，使低比特恢复可以选择student-induced state distribution，而不是只增加固定离线teacher样本。DKL借自Jung2025，不是本文新散度理论；top20 teacher/student并集加保留梯度的residual mass，不是裁词表后简单重归一。

必要证据：uniform asymmetric W2/W3 group128、BF16 activation，先BlockAP/EfficientQAT校准到可用student，再25,600多域prompt、每步128 prompt一次采样/一次更新；LR1e-6、1.7B400步/4B与8B300步。九项math/code/knowledge/IF评价使用thinking、temp.6/topk20/topp1、32k cap并有PTQ特例，三个evaluation seed不是三次独立训练。Table3匹配校准及response-token loss预算，但固定response与OnQ仍非同prompt/data pool，不能把全部收益唯一归因于on-policy。Table4共享1.7B W2 coldstart/DeepScaleR/400步的目标比较更窄：DKL并非每任务胜FKL（HumanEval反侧）。教师rollout、logits存取、初始化QAT与更新均付费；fake quant训练结果不证明packed kernel或服务净加速。

actualowner：实读Ch31 `TRAIN-RLHF`“后训练分支本质差异StateDistribution”及其PrefixOPD邻接：已具体区分静态SFT/teacher与student自身状态、producer/policy/teacher/reward revision、staleness和rollout费用；Ch49 PTQ/QAT段已具体区分fakeQDQ、teacher/data/quantizer身份与部署artifact。本文借用DKL，在低比特student上验证同一状态覆盖原则，未形成现owner尚缺的长期分支。保source贡献作报告标准项，Books NC不是把source判为无贡献；无需再读全附录制造gap。

### S2 — 2610.29498 RoCo；2+1+2=5；有限gap提案

原件：[exact-v1必要文本](./arxiv-standard-source-2610.29498.txt)，官方[HTML](https://arxiv.org/html/2610.29498v1)。实读§3–4方法、§5.1–5.2直接评价、§6.1–6.4、B.1–B.3、C.1–C.2、E.1–E.3与F的相同backbone控制；其余表/附件不冒全读。

旧约束→增量→选择：process labels常需人标/MC/auxiliary verifier；本文把MoE native selected-expert probability mass汇为token信号，轨迹内归一后的overall/head/variation组成C=M+H−D，定位最低分step并重生suffix；也用强MoE轨迹C作前缀回归标签，训练可供dense模型使用的PRM。这改变可用process-supervision producer，而非router affinity自动等于正确率。

必要证据：三个MoE、六任务，五随机seed，routing比logit相关更强只13/18设置。rethink实际是完整轨迹生成后replay router，再whole-trajectory归一、择点、重生并重新评分，最多三轮；extractable answer用初始与各轮majority/tie最近，HumanEval/IFEval用latest。random/LECO同suffix machinery与round budget支持择点比较，但不是token/walltime matched；SC八条整轨迹与三轮重生预算也不可等同。MC revision-value分析来自原先错误轨迹和有限GT rollout oracle，不代表自然请求人群校准。PRM为Qwen2.5-7B scalar MSE、LoRA一epoch/final checkpoint、max1024截断、4GPU/global128；监督构造不截断，5%validation只报告C拟合而非真值。teacher生成/路由replay/PRM训练与test prefix scoring都收费；无target routing不等于无额外模型。

actualowner：实读Ch80 `AGENT-REFLECTION` UPTURN prefix修复与“cheap trajectory sensor→slow diagnosis→bounded repair”完整邻接，已保proxy非事实置信、domain shift及critic非oracle；Ch21 router affinity非correctness也已有。仍缺“architecture-native routing可作为post-hoc修复/可迁移label producer，但whole-trajectory相对标尺不能直接接online gate”的具体接口。唯一owner Ch80，不在MoE dispatch章重复。

供root选择的窄PRE（尚未写Books）：
> cheap sensor也可来自模型内部的计算分配，而不只来自输出熵。MoE routing的selected-expert mass可在完整轨迹内按step聚合，用相对低分位置提出suffix重试，或由强teacher生成前缀回归标签供dense模型使用。但完整轨迹replay与轨迹内归一得到的是post-hoc相对信号，不能直接充当逐token在线阈值或校准正确率；蒸馏也只转移teacher的proxy关系，不产生独立真值。应把路由采集、teacher生成、PRM训练/评分与重生token计入总费，并保留held-out校准、随机同预算修复和失败后退出。有限MoE/任务对照支持这一候选producer，不证明免verifier、任意任务迁移或端到端净收益。

S2精确插点（作者实际顺读当前完整邻接）：Ch80以下完整上段后、下段前，保上方cheaptrajectorysensor代码块和原abort完整段不拆分。PRE即上一引用段，仅此一段。

上段全文：Token entropy、embedding cluster entropy 等只是 proxy，不是 factual confidence；threshold 会随模型、retriever和 domain 漂移。未校准或高风险任务仍应直接使用 deterministic verifier/strong review，slow critic 的输出也必须经过第 77 章的 Memory write gate。分层监控优化的是 critique allocation，不是让 self-reflection 成为 oracle。

下段起句：廉价monitor也可直接提议abort，而不再购买慢critic。下段末句：monitor训练、ensemble每成员和持续重校均付费；误杀风险、人口或净费用不合时，保留完成运行、固定硬预算/较窄检查与独立终验，不以低monitor价格或costperretainedsolve最小批准任意停止。

### S3 — 2610.29545 PACE；2+1+2=5；有限gap提案

原件：[exact-v1必要文本](./arxiv-standard-source-2610.29545.txt)，官方[HTML](https://arxiv.org/html/2610.29545v1)。实读§3误差模型、§4通道干预、§5.1–5.3、§6评价、§7.1及§7.3–7.5/§8；未核实现/全附录/复现。

旧约束→增量→选择：recurrent state每token写回低比特会反复舍入；PACE以少量token decode buffer延长state rounding周期，再按key-axis分组并按head分配位宽，选择的已不只是bitwidth，而是“何时舍入/哪些轴共享scale/哪些head保高位/buffer精度”联合配置。独立舍入误差/归一key/近似平均衰减下的Eq5只解释重复误差积累，不是所有GDN长序列质量保证。

必要证据：四个hybrid gated-delta模型Qwen3.5-4/9/27B、Qwen3.6-35B-A3B；chunk-prefill256与decode周期分开。周期8 int4 state/int8 buffer、scale/zero和buffer均算residentbits；payload alone不等resident memory。head选择一次8×2048校准窗口。§7.3同residentbits对照支持key-axis比value-axis较低ppl、head allocation局部收益，IFEval27B仍存在DAMP更高反侧；Q-Mamba DSQ为不含原finetune的重实现，不冒完整方法优胜。§7.4 Qwen4B首512 WikiText token的median-layer relative Frobenius drift随周期下降，另35B方向一致，不是任意长序列证明。IFEval/RULER残余gap仍在，prefill损伤不被decode周期自动修复。单H100PCIe/4B/context512/batch1–128 Triton，INT4从batch16起TPOT低于per-tokenBF16，但大部分收益来自BF16 decode buffer，INT4增量较小；不授混合4/8配置实测加速或生产尾延迟。增加buffer、校准/packing、quant/dequant与prefill仍付费。

actualowner：Ch22 GDN recurrence/chunk-parallel段已解释更新与state容量，但不是数值量化策略；Ch49低精度、PTQ/QAT及KV低精度段没有“会重复写回的recurrent state舍入周期/临时buffer”控制。因此唯一owner建议Ch49 `INFER-TENSORRT-LLM`量化数值契约，链接Ch22递推而不改其机制主体；不是把固定大小recurrent state写成KV压缩。

供root选择的窄PRE（尚未写Books）：
> 对会被每token写回的递归状态，低精度误差还取决于写回频率。可将最近少量更新暂存于decode buffer，隔若干token才合并并舍入持久state，再按更新结构选择scale共享轴与高精度head；这样用buffer容量、更新kernel与校准费用换较少的重复rounding。比较必须按state+scale/zero+buffer的residentbytes，而非仅state payload bit。有限gated-delta实验支持周期化与key-axis grouping的联合选择，但不保证长周期单调改善任务质量，不能修复prefill既有损伤，也不能把BF16 buffering带来的主要吞吐收益都算给INT4；失配时保留较高位宽或原更新路径。

S3精确插点（作者实际完整顺读Ch49该局部）：在“粒度与校准决定谁共享同一份误差预算”section内，下列SemanticDialect完整段后/静态calibration完整段前；位于quantization-axis/跨时步一致性之后，引入反复写state的另一个时间轴，不打断后续static/dynamic calibration链。PRE即上一引用段，仅此一段。

上段全文：粒度细化还可能破坏原本相关的输出：视频 diffusion 中，相近空间 token 或同一区域跨帧的 activation 可因局部统计略变而选到不同数值格式；逐块重构误差较小，不保证整体时空一致。一条受限分支以 attention 作为相关性代理，让 anchor 与相关 token 共享覆盖不同动态范围的 **sub-formatbook**，但仍各自选择 dialect，而非强迫它们使用同一网格。它用跨块选择约束换取格式一致性，同时增加 attention profiling、关联窗口、覆盖冲突和随 denoising step 更新的状态；窗口过大或更新过密也可能退步。[SemanticDialect exact-v1](https://arxiv.org/html/2603.02883v1)只在两种 Open-Sora 架构中验证该分支，多个质量指标不单调改善，attention 也不等于语义真值。相关性不可靠时保留独立块选择或提高精度；v1 的 CUDA kernel 与 RTL 成本评估仍属未来工作，不能由四比特表示推部署吞吐。<!-- source-family:SF-2026-ARXIV-2603-02883 -->

下段全文：静态 calibration 提前用代表性数据确定 activation 范围或重构目标，运行时路径较轻，但分布漂移会使旧 scale 失配；动态量化根据当前输入计算 scale，降低对固定范围的依赖，却把 reduction、转换和 metadata 带入热路径。Weight-only 的最简单方案也可以直接从权重统计定标；是否需要校准样本取决于量化目标，不能把所有 PTQ 都写成同一种准备流程。

### R1 — 2610.28714 TAG真实纠错线索定点闭合（不计10项；维持贡献排除，不评分）

原件：[exact-v1必要文本](./arxiv-standard-source-2610.28714.txt)，官方[HTML](https://arxiv.org/html/2610.28714v1)。实际读§3.1–3.5协议、§4必要对照、§5全部风险、§6–7与AppendixD精确pins/代码行线索。未亲核remote代码或运行released code；paper自身也以代码取证而非运行证明。

真实风险不是“TAG应用”标签：released CLEGR @72acb02 Cora loader把cora.content行序text和PyG Planetoid位置label混接，作者重建2692节点/五seed60-20-20，misaligned TFIDF29.1±1.5与aligned80.9±1.2，支持该代码路径身份错误。不能证明该released path生成了原28.7–29.7公开行；不据此宣布全部Cora结构充分结论被推翻。GNNasJudge测试mask进入agreement/SFT目标的代码线索同样不证明发布行实际走该路径。test-gridbest选择、重复baseline表、同split不同features/settings解释了比较混杂；12/22可检验LLMreference仍显著更好，non-significant不是equivalent，固定maskseed方差不含重采图/节点人口方差。

项目实际受影响检查：在Ch66及model/Ch76目标scope按LLM4HeG/KCoT/LLMNodeBed/ENGINE/LLaGA找不到被采的具名结论；实读Ch66 claim/evidence/inference/decision、完整evaluation-subject identity、held-out selection与“数值可复算不等于复现了同一个实验”完整两段。现owner已具体要求cohort→render/prompt→resolved model/call→annotation→analysis provenance，条件变化即new evidence revision，禁止由可复算数值保留原排名。本文实际新增限TAG node-classification具体方法/loader/比较，不支持更一般基础模型或系统设计的新结论，也没有纠正项目已采用的具体命题，因此维持贡献排除；现通用provenance覆盖仅用于风险影响检查，不是由Books已覆盖倒推贡献排除。reader已独立读上述原证、扩核CLEGR/GNN-as-Judge亦无被采主张，接受此定点风险闭合。若root/reader发现具名被采TAG主张，只重开该实际段落，不扩大历史扫描。

### S4 — 2610.29671 Uni-Mem；2+2+2=6；Ch77有限gap提案

原件：[exact-v1必要文本](./arxiv-standard-source-2610.29671.txt)，[HTML](https://arxiv.org/html/2610.29671v1)。实读§3–4、§5.1及5.3–5.5/Limitations、C.1必要coldstart/selection、F.1同harness控制；未核实现/全附件/复现。

旧约束→增量→选择：终局QA失败混合bank未保存与reader未找到；Uni-Mem训练时用annotated evidence-chunk索引当前record，冻结answerer绕过learnedretrieval估存储充分性，construction同dialogue从空bank多rollout、retrieval共用同一snapshot建的bank，交替更新共享manager。失败retrieval仅在bank proxy支持正确答案时得0，否则⊥排除；按triggering chunk/query对齐event而非按toolcalls位置，每event内全部calls共advantage，later update/delete lineage扩充write credit。由此可选择分阶段条件控制，而不是把两个stage共变的最终QA reward广播。

必要边界/成本：QA在dialogue后才到，并未实证任意交错在线流；annotated E只训练可用，Index充分性是frozenanswerer/judge的proxy，不是真实因果或证据完整。对应event前序bank仍可分岔，未变成相同state反事实；⊥必须从groupstats与loss都排、valid<2或零方差丢组、无KL。Qwen3-4B manager、GPT-OSS120B answerer/GPT4omini judge；LoCoMo2:1:7及LongMemEval OOD。SFT另四syntheticconversation/773QA，GPT5.4 teacher、BF16/16k/8GPU，validation选862而非最高pass@1停点。F.1同harness把SFT与RL分开，standardGRPO仅小幅提升、full方法在SFT前后都有增量；§5.3顺序增量消融不证明所有组件独立交互。LongMemEval/judgeprompt敏感性不转移普遍保证；原件F.2另Qwen3.8 answer/judge训练曲线不是主表同配置。构建多bank、额外indexed-answerer/judge、lineage、SFT与检索调用均收费，需GT证据/强模型、资源密集。

actualowner：实读Ch77“Outcome Reward→Content-level Credit”完整邻接，已具体有固定retrieval masking、Video-EMem freezewriter诊断、entry-lastwriter分账及Hy-Memory chunkcredit；因此不重复“归因非真值”通用论。仍缺同一sharedmanager交替训练时的group条件：固定bank才能把失败归给reader、无可答proxy者从统计与loss同时排除、更新lineage扩credit但不变证据原索引。唯一owner `AGENT-MEMORY` Ch77；Ch33只交叉组统计，不另写。

条件窄PRE（未写Books）：
> 同一manager同时学习写入与检索时，应先拆开bank未保存必要信息与reader未找到信息。可在训练中用有标注来源的record集合让固定answerer估计bank可答性，再交替比较同dialogue的construction rollouts与共用一个bank的retrieval rollouts；bank proxy也无法答时，不把retrieval失败当作reader负例，并从组统计和loss同时排除。按触发事件对齐信用、沿update/delete lineage追到后续修改者，能减少两stage共同变化的混淆，却不是相同state反事实或真值归因；它依赖证据标签、answerer/judge并支付额外建库、评分与lineage成本。缺标签、proxy失配或共享policy回归时，保留outcome-only、固定writer/reader及原episode，不由被排失败制造更高表面成功率。

S4精确锚（作者已完整读）：Ch77现有Video-EMem完整段及其SF2610-24537 marker后/下列“只用最终QA…”完整段前。PRE不重复旧masking机制，只增加sharedpolicy训练group条件。

上段全文：未来query未知时，writer还可先按source保留而非开发QA成功来演化：逐级压缩caption并回查遗漏、另选与text互补的原帧，冻结memory后才用QA失败调整reader的定位和组织。[Video-EMem的受限控制](https://arxiv.org/html/2610.24537v1#S3.SS4)把memory缺失与reader漏读分开，前者不能算后者的定位错误；但caption和语义match仍是proxy，source未观察到的事实不能由更多压缩容量补回。分阶段优于jointQA的局部差额未独自证明overfit因果，query-time或持久payload变小也未包含全部构建/演化费用。caption、原帧、全部候选/审核、索引和query调用都计费；source保留、版本或后query回归不合时保原episode、curatedmemory与完整读取，不由writer分数或低存储批准完整事实和任意未来可答。

下段全文：只用最终 QA reward 训练 memory policy 成本低，也适合短链路、固定 schema 和容易人工检查的任务；但它不能回答某段中间 memory content 是否真正帮助了最终答案。一个实验性分支是固定 retrieval/answer interface，对 memory token 或 span 做 masking/counterfactual scoring，把对 answer score 的变化映射为 local process reward，再与 global outcome reward 合并。它把“这次答对了”推进为“哪些被写入的内容可能贡献了这次答案”，从而给 admission、update、compress 与 discard 更稠密的学习信号。

### S5 — 2610.29832 S-EDL；2+1+2=5；训练语义校准有限gap提案

原件：[方法/评价](./arxiv-standard-source-2610.29832.txt)、[必要B.1–B.5](./arxiv-standard-source-2610.29832-B1-B5.txt)、[结论/限制](./arxiv-standard-source-2610.29832-conclusion.txt)，[HTML](https://arxiv.org/html/2610.29832v1)。实际读§3–4、§5.1、§5.4–5.6、§6限制及B.1–B.5，不冒全表/证明；只采用接口，不采收敛/普遍校准定理。

旧约束→增量→选择：固定类别head不能覆盖prompt-specific semantic classes，sample histogram又无直接likelihood梯度；S-EDL将生成likelihood的p^(β−1)按可核等价类加总归一，形成e_s=Nπhatβ(s)、α=e+1的Dirichlet-MSE辅助SFT。选择的是直接调整generator的语义class marginal，而非只训练独立confidencehead或把多数票一致当真值。总strength=N+类别数由预算固定，不是学得的epistemic evidence。

关键实现边界：missing correctclass训练时另teacherforce goldcompletion并加loglikelihood−4.6 penalty；这是supervised finitecandidate混合目标，已不是纯MC估计，不把纯采样一致性命题授给实际所有case。evalmissingclass记0count；语义聚类依math-verify或GPT-OSS20B。三7/8B base+LoRA、四STEM集、50generations评smECE/semanticmajority与独立pass@1、三seed；不授code/longcontext/难定义等价域。prose非GSM说12samples，而表Formula部分为8，故不采用全可执行recipe。DrGRPO只匹配EDL active steps且group8，不等总sample/token/训练费用；Formula跨域在所有方法都失效后统一加physics hints，是不同评价条件，不采原OOD普适性。find-first减少oracle调用仍有representative读长/误聚类及采样、teacherforce、SFT/judge与训练全费；O(N) calls不是O(N)完整token工作。pooledtoken profile接近SFT不证明仅语义重分配的唯一因果。

actualowner：实读Ch33 confidence block双reward/共享参数与独立校准边界完整段；其训练接口是另输出数值confidence，并非在变动语义类上用likelihood作为可微监督。Ch66已有selector/calibration/release分责，属于测量验收而非训练机制。因此唯一owner建议Ch33 `TRAIN-GRPO`校准训练分支，保语义等价oracle、固定strength和missing-gold混合界，不在Ch66重复测量原则。

条件窄PRE（未写Books）：
> 校准还可直接作用于generator在语义答案类之间分配的质量，而不另生成一个confidence数字：从多份续写中建立prompt-specific等价类，按序列likelihood温和重权，再用这些class masses形成可微的evidential辅助目标，与原SFT共同训练。但等价类来自verifier/judge而非模型真值，Dirichlet总strength由采样预算固定，也不等学得epistemic certainty；正确类未被采到而另加入gold likelihood时，实际目标已经混合监督候选，不能继承纯MC解释。必须另验pass@1、语义majority与held-out校准，计入全部采样、聚类/teacherforce和训练费用；等价定义、域移或预算不合时，保留普通SFT/RL和独立外置校准，不由更低校准误差批准答案或安全发布。

S5精确锚（作者已完整读）：Ch33数值confidence双reward段及其下述完整failure段后/视觉confidence完整引入段前，完整calibration训练链不拆。PRE为上一段，仅增加生成分布本身的semanticclass分支。

上段全文：把 loss 位置分开仍不隔离共享参数和前缀依赖，后段校准更新可以改变前段生成；要观察真实两路梯度与 held-out 质量，而不是由 mask 宣布优化互不干扰。负绝对误差也不自动具有 strictly proper scoring rule 的概率一致性，有限 group 的目标方差下降更不保证所有参数梯度方差归零。[必要方法与直接反侧](https://arxiv.org/html/2603.09117v1)只支持所测 Qwen3-8B 数学训练中的有限分支，不采用普遍单轨迹 collapse、必然梯度冲突或无损一致校准定理；部分准确率及校准子指标仍有反退，原表 PCE 与 ECE 的序关系还不满足正文同分母定义，须先澄清指标人口与聚合协议，不能照录其降幅。输出协议与不同读出也不能合成同条件因果。完整轨迹、额外 confidence tokens、verifier、组统计、训练和独立校准均计费；解析、组信号或真实质量失配时，保留原 outcome-GRPO、经独立验证的外置校准器和完整答案 gate，不让自报概率兼任安全保证。<!-- source-family:SF-2026-ARXIV-2603-09117 -->

下段全文：置信监督缺少视觉标签时，还可把视觉描述与后续推理分成不同输出段，用原图与高比例遮罩图的logit变化、以及描述token的entropy构造受限伪目标，再经batch-relative标准化映射给视觉confidence。答案正确性仍由原verifier持有；两份自报confidence的harmonic组合只是训练读出，不是感知/推理联合正确概率。遮罩敏感性说明分布改变，不认证原描述已grounded，batch-relative目标也不能跨人口当绝对perception真值。<!-- source-family:SF-2026-ARXIV-2604-09529 -->

### S6 — 2610.29933 ThreadRAG；2+1+2=5；建议Books No Change

原件：[exact-v1必要文本](./arxiv-standard-source-2610.29933.txt)，[HTML](https://arxiv.org/html/2610.29933v1)。实读§3.1–3.3、§4.1–4.4/限制、D segmentation与E.1–E.3必要对照。非核代码/全附录/复现。

旧约束→增量→选择：symbolic triples/生成rewriting可能丢上下文；source以保留docID/字符span的原文节点加narrative/semantic/lexical边，anchorPPR/prune+BFS可达后按docrelevance与文内offset确定性linearize，最多三轮sufficiency/缺项检索。改变图用于选择、原文用于reader消费的representation接口，不是PPR路径自动成正确解释或全部原文不失。

必要证据：Hotpot/2Wiki/MuSiQue支持+干扰passage corpus，三个LLM、hybridtop5，四A6000。AppE相同retrieval/prompt/预算的GraphFree、相同图预算BFS/DFS，以及主文拆分/EDP消融支持局部选择增量；但graphfree替换整个STG+EDP，不能唯一归因linearization。RoBERTa+MLP一次用100Wiki documents/1553teacher-silvernode训练，50disjointdocs/719teacherboundaries核agreement非人类语义真值；非无准备。Table3“construction0”仅LLMtokens，不包含silver生成/segmenter训练、embedding、索引图与PPR全部计算；100query token账不能授生产延迟。稀疏链接/单文档收益有限，预算filter仍可丢桥、offset顺序不保跨文档逻辑chronology，sufficiencycritic非oracle。

actualowner：实读Ch76 ingestion原始span/结构补全与图导航、GraphRAG citation绑定实际traversal/支持子图、Relink query-scoped source-backed关系、bridge与semantic贡献分离、有界querypolicy/后置证据DAG完整邻接。已具体分清“图导航选择→原文支持→独立entailment”，并保原文locator、预算/构图版本和小任务plainretrieval退路。本文PPR+segmentation提供同一设计选择的局部实现证据，未带来当前owner缺失的稳定边界；因此保source为5分报告标准项、Books NC，不用“路径”术语另造owner或为新数字重复一段。

### S7 — 2610.28770 ReAPO；2+1+2=5；Ch33有限gap提案

原件：[exact-v1必要文本](./arxiv-standard-source-2610.28770.txt)，[HTML](https://arxiv.org/html/2610.28770v1)。实读§3.1–3.3、§4.1–4.5及限制；不采需全证明支持的无偏/优化保证，未核代码/全附件/复现。

旧约束→增量→选择：独立同题rollouts会重复失败；ReAPO只在verifier失败后把旧答案+固定反馈续入context，再生成下一attempt，按全部实际attempt rewards pooled mean/std，但每个attempt的advantage只更新该attempt生成tokens。成功retry不把早先失败重标成功。这同时改变failure-conditioned探索人口和attempt-level信用，不只是部署时多次重试。

必要证据：默认G16/K2，0.6B/OLMo1B在GSM8K，Qwen1.7B/4B在Polaris53K，trajectory总responsecap2048/4096跨attempt共享。评firstresponse、无inference verifier，SCoRe-Stage2是省去Stage1的二次response比较，不等完整SCoRe被胜；Mean@32与Pass@32分验。作者同时画steps/generatedtokens/wallclock，早期GRPO有竞争力，后期本方法更好；doublegroup/doublesteps及wholetrajectorycredit、unconditionalretry控制支持两组件选择。0.6B8seed、4B主图3seed，OLMo/1.7BK3部分single-seed；K3边际收益有限、GPQA不继承数学增益。理论以reward sufficient statistic、futureexpectedattemptcost与index无关等简化作动机，实际finiteK有截断bias、居中/归一改变估计、onpolicy无KL；不能声称Eq8实际是一般SSP无偏梯度。串行context增长有计算/显存/并行度成本，verifier/失败prompt与全部rollout/训练都计费；尚未验证code/agent域。

actualowner：实读Ch33 failure corrective LIFO branch完整段及其前后、uniform→selectivecredit邻接；已有失败重采与deployment/train分责，但未具体区分同一串retry内“failedattempt保持低advantage、success只更新自己span”与整轨终局成功广播。唯一owner `TRAIN-GRPO` Ch33，不在Ch80重写修复prompt。精确插点建议当前“最后，普通 GRPO 把成功和失败都留在下一批统一采样中…”完整段后/“把 trajectory-level advantage 均匀广播到所有 token…”完整段前；两侧已实际全文读。

条件窄PRE（未写Books）：
> corrective采样与credit还要在attempt边界上分别声明：只在可信verifier判失败后续入旧答案和反馈，可以把预算集中于未解问题；但后一次成功不应自动把前一次失败的全部tokens标成成功。一个受限选择是将实际生成attempts放入同题reward人口，各attempt只消费自己的advantage，成功则停止、总token和重试次数有界。这会改变训练人口、串行上下文与组统计，不是部署时免费取得答案oracle，也不保证有限预算/归一后的更新等价于理想最短路径梯度。应分验first-attempt质量、高k覆盖及全部生成/验证/墙钟费用；反馈失准、重试低收益或状态不可安全续接时，保留独立rollout、原sequencecredit和可靠过程监督。

### S8 — 2610.28871 Looped TBPTT；2+1+2=5；Ch28负面边界gap提案

原件：[exact-v1必要文本](./arxiv-standard-source-2610.28871.txt)，[HTML](https://arxiv.org/html/2610.28871v1)。实读§2 exactmeasurement/protocol、§3必要trainedmodel设置、§4–5全部直接成本反证与§7限制/takeaways。不采用全附录几何界，未核实现/复现。

旧约束→增量→选择：反传窗口k需在显存/费用与credit损失间选择；source给每loop共享权重贡献与exact g−gk测量，并直接反证“冻结checkpoint上的丢梯度比例能预测实际训练质量代价”的充分性。persequence normratio median不等expectedgradient relativebias、clippedbatch update或loop-onlyratio；数值还随文本、probe、checkpoint改变。测量是诊断当前截断移除了什么，不自动成为优化k的控制器。

必要证据：Huginn/Parcae/Ouro及两自制SmolLM loop与两个PartII小模型；ρ^k只是信号几何衰减/方向相容近似，Ouro增长不能套infinitegeometric。fine-tune为GSM8K600steps、8×512tokens、AdamW，固定steps非固定compute，LR只为fullBP选、未按k调；主要cost全/截断/k0差额5seed。预注册S11两小模型5loops，lostgradientcurve误差.037与不测量k-only.036近似，不能声称普遍证明proxy无用；S6blending预测失效，Adam后的方向解释posthoc未被跨模型预测支持。§4在300steps lostgradient下降、heldout同任务也下降，k2截断也下降；不能由trainedcheckpoint冻结统计授全训成本。某SmolLMloop未比unloop更好，probe部分权重/precisionbug旧study作废；本稿不把它们混为普通LLM预训练可用recipe。fullbackward/perloopVJP、heldout探测与配对训练全部收费，参数梯度缓存也占memory。

actualowner：实读Ch28 GradientHorizon section完整上下段，现有blocklocal objective/finalquality与RTRL替代强调credit/费用分责；没有“冻结模型的relativegradientnorm损失不能直接预测经Adam适应后的质量代价”的具体负面边界。唯一owner `TRAIN-PRETRAINING` Ch28，Ch22只forwardrecurrence引用。精确插点：完整CNN/VGG限制段及其SF2605-04346 marker后/“缩短gradient horizon并不自动减少每层算子的费用…”完整段前；已实际完整读两侧。

条件窄PRE（未写Books）：
> 对共享权重的looped模型，还应把“截断丢掉多少原始梯度”与“训练最终损失多少质量”分开。可以在冻结checkpoint上对同一held-out序列比较full与最后k轮反传，但per-sequence normratio、batch平均/clip后比例和loop-only比例不是同一量；训练继续后这些读数也会移动。有限预注册fine-tuning对照没有让冻结丢梯度比例稳定优于只看k的简单预测，Adam对缩放与方向的处理又不同，因此它只诊断当前credit损失，不能独自选择窗口或保证固定算力更优。应绑定probe、文本、checkpoint、clip/optimizer与反传窗口，再按匹配预算验真实质量；探测或预测失配时保留更长窗口、原完整BP与直接小规模对照，付清全部探测和训练费用。

### S9 — 2610.29427 EMPO；2+1+2=5；Ch33 ratio接口gap提案

原件：[exact-v1必要文本](./arxiv-standard-source-2610.29427.txt)，[HTML](https://arxiv.org/html/2610.29427v1)。实读§4.1–4.3、§5.1–5.5、B限制、C.1局部factorization/实际tokenweighted式、D.1–D.3必要协议。未核代码/全附录/复现，不采一般effect-policy无偏梯度或单调改进。

旧约束→增量→选择：不同text response可执行同一action，但各自advantage×各自text方向可能相互干扰；EMPO保留baseGRPO/GiGPO advantage，只把valid/nontruncated、同contextkey与canonicaleffect且size≥2的cell中response长度归一几何ratio先平均，再让members共享ratio。改变的是policy-update coupling而非另估credit、另加reward或把动作同名当state相同。

必要证据/边界：abstract effect-score identity固定context、theta独立parserψ且完整sum；实际有限cells/长度归一/oldpoint局部分解只是surrogate，tokenweighted loss的差额是Cov(TA,s)，不是任意θ和clipping下精确marginal policy。外cell回原tokenratio。相同action不证明history等价，h需要可靠规范化；structuredinterfaces外未验证。ALFWorld/WebShop Qwen1.5/7B、Sokoban QwenVL3B、同initial/config/budget、G8/3seed，lengthnorm/ratio-sharing/randomgroup消融与受控一步dispersion支持coupling；steps-to60%不等墙钟或全训练省费。WebShop eligiblecoverage仅约23–25%，不能宣传所有tokens受益；新增parser/cell构造、ratio聚合/gradientmixing、所有环境与训练都计费，无新增critic不等零费。

actualowner：实读Ch33 hierarchy-ofgroups完整两段、状态图/知识bitset邻接，现有组结构主要定义reward/advantage人口；也已有geometrymeanratio非整串importance的GAGPO边界。尚缺“保原advantage、在同effectcell共享ratio而改变credit–direction配对”这一独立更新轴。唯一owner `TRAIN-GRPO` Ch33。精确插点：完整“层级分组改善 context inconsistency…”段后/“搜索状态还可以按‘已经取得哪些任务条件’…”完整段前；两侧已实际完整读。

条件窄PRE（未写Books）：
> 分组还可只改变policy更新的耦合，而保持原advantage不变：在可比较context与同一canonical执行effect的有效响应中，先按长度归一各response的ratio、再在cell内共享平均ratio，使不同文字实现共同提出这个effect的更新方向。它不同于重估组reward，也不意味着文字相同或action同名就拥有相同隐藏状态；size不足、执行无效或截断者保留原目标。有限cell、长度归一和PPOclipping得到的是局部surrogate，不是完整effect-policy的无偏importance ratio或单调改进证书。Parser/contextkey、成员与token聚合须随更新冻结，另验真实任务质量、cell覆盖与全部分组/训练费用；别名、支持或净质量不合时，保留原response-wise更新和明确的state/critic监督。

### S10 — 2610.29965 CORD；2+1+2=5；建议Books No Change

原件：[exact-v1必要文本](./arxiv-standard-source-2610.29965.txt)，[HTML](https://arxiv.org/html/2610.29965v1)。实读§3.1–3.4全部投影/证明/费用、§4.1/RQ1必要设置、§4.3选择gate与方向/反侧、§4.4及§5；未核代码/全部附录/复现。

旧约束→增量→选择：RL+OPD naive sum会相抵；source在明确protected objective后，只投影另一当前objective梯度、选择conflict-only或alwaysgate，再交optimizer。沿用A-GEM单约束几何，不是新projection原理；带来joint-agent配置的明确优先级/gate/λ与aggregation选择。保护teacher不等teacher更真，梯度正交不保证另objective下降。

必要证据：先各loss在相同参数版本累积后投影，microbatch先投不等价；O(d)额外gradientstorage/运算、shard dot/normreduce、独立objectivegradient即便共享forward也有费用。固定mini-batch损失的first-order descent仅rawcombinedgradient，AdamW momentum/adaptivedecay改变实际位移，不能签生产reward不降。Qwen2.5-3B、ALFWorld≤50step/WebShop≤15、8A10040GB、150updates、G8/cap512，三个hostpairedskillbank相同；单trainingseed、四temperature.4evaluationpasses的±是decodevariance，不是trainseed方差。WebShop自跑500tasks vs引用published128不公平合并。main三host ALFWorld均增/WebShop仅二增；λ.001protectdistill+always显著反退，PCGrad同λ最高mean，不声称CORD普胜。taskscore/严格success/重复动作各异，actor开销不能直接当全iteration测时，rollout/teacher/env与训练全费。

actualowner：实读Ch28当前一阶多loss累积再仲裁段（SF2509-07252）、GridUMM冲突proxy反证两段、实际optimizer后aux/RL投影段（SF2602-09396）完整局部。已具体覆盖accumulation不能与nonlinearprojection换序、固定参数/归一/buffer与rankreduce、raw梯度和optimizer后位移不同、较低conflict不能验收heldout质量。Ch31 OPD状态/teacher identity也已充分。本文把成熟单约束投影用于三个jointagenthost，新增是局部配置与paired empirical evidence，未新增当前owner缺的长期分支，因此标准报告保5分，Books NC；不为了新方法名复制一份多目标optimizer原则。

## 本10批作者保存态与精确余项路由

预告10项的必要Source/actualowner处置已全部保存，3项建议NC（29378/29933/29965）、7项条件gap提案；非独核或实际Books完成。28714另外纠错定点核通过，不计10。无全篇/全附件/核代码/复现声明。所有保留均非由数量或访问状态决定。

以下余项仅按177初分表、扣root8/此前13/ORG15/本10的已分配有效层生成，**不是新发现或冻结准入**，也不能覆盖root另有未通知我的分配。28711/29357已有决定准入核心补读但尚无正式标准必要层，仍列供root判断复用；30089只保非Sci track。5–6标准层98项（其中有明确反证/真实gap者仍受影响域深入）：

2610.28801（6）、2610.28827（6）、2610.28858（5）、2610.28954（5）、2610.29229（6）、2610.29232（5）、2610.29380（5）、2610.29408（6）、2610.29441（5）、2610.29537（5）、2610.29552（5）、2610.29581（6）、2610.29590（5）、2610.29688（6）、2610.29811（6）、2610.29854（6）、2610.29915（5）、2610.29989（5）、2610.30036（5）、2610.30089（5）、2610.30120（5）、2610.30127（5）、2610.30129（6）、2610.28814（6）、2610.28880（5）、2610.28882（5）、2610.29161（6）、2610.29168（5）、2610.29203（6）、2610.29246（5）、2610.29264（6）、2610.29282（6）、2610.29302（5）、2610.29329（5）、2610.29646（6）、2610.29692（5）、2610.29702（5）、2610.29716（5）、2610.29730（5）、2610.29866（5）、2610.30097（5）、2610.30105（5）、2610.30117（6）、2610.30125（5）、2610.30136（6）、2610.29088（6）、2610.29357（6）、2610.29443（6）、2610.29507（5）、2610.29767（6）、2610.29823（6）、2610.29995（6）、2610.30103（5）、2610.30116（6）、2610.30132（5）、2610.28707（6）、2610.28785（6）、2610.28798（6）、2610.28811（5）、2610.28958（6）、2610.28998（5）、2610.29172（6）、2610.29281（5）、2610.29355（5）、2610.29385（5）、2610.29426（6）、2610.29458（6）、2610.29538（6）、2610.29734（6）、2610.29927（6）、2610.29932（5）、2610.29999（6）、2610.30009（6）、2610.30014（5）、2610.30068（5）、2610.30076（6）、2610.30107（6）、2610.29489（5）、2610.29873（6）、2610.29523（5）、2610.28711（6）、2610.28698（5）、2610.28891（5）、2610.28905（6）、2610.28909（6）、2610.28934（6）、2610.28989（6）、2610.29023（5）、2610.29110（5）、2610.29135（5）、2610.29139（6）、2610.29467（5）、2610.29491（6）、2610.29680（5）、2610.29822（5）、2610.29934（6）、2610.30041（5）、2610.29464（5）。

7分深入4项：2610.29410、2610.29722、2610.29435、2610.30074。4分身份/日证关闭与作者纠错例外沿原表/具体材料，不进入默认全文队列。
