# Jun12 B4 有限必要证据与实际 owner

仅处理已由root完整AB校准的有限候选，不新增发现。11755的arXiv公告联合界仍成立，但精确publisher纸本/在线日期冲突另隔离，不能把64准入线索写成64确定Jun11首次公开；其余63的日期层复用已核原件。本文作者supp_jun12；唯一非writer审阅者jun12_review_finish，canonical§40起。

## 11755 — Acoda（具名首次公开日期保留，非贡献N/中心H）

- exact-v1 HTML frontmatter L48列ICSE-Companion Apr12–18与publisher DOI10.1145/3774748.3793624。不能拿会议时间自动当正文公开；随后只定点取[精确Crossref](https://api.crossref.org/works/10.1145/3774748.3793624)，完整原响应存[SUP_ACODA_PUBLISHER_DOI_20261026.json](./SUP_ACODA_PUBLISHER_DOI_20261026.json)：title一致，published-print/published/issued date-parts为2026-04-12，published-online与publisher PublicationHistory assertion=2026-09-09，created=2026-09-09T21:41:26Z。ACM正文页403，不因一次失败授整批阻断。print是paper-specific字段，online不消去它；Jun11 arXiv公告不能证明它才是全球first-public。reader与root要求本项隔离归属，不给确定当窗新候选/Books；不把它迁到某April Daily或重计。
- 可接受恢复：精确publisher纸本/正文实际可用性日期、明确online/print更正或其他可读早期原始正文，足以消除第一公开可能早于Jun11的冲突。只重开本项日期/受影响采用层，不全版diff/无限搜索，不以社交/搜索收录日替代。原AB准入准备依据保留，但本次不评分或作为确定当窗新增实证数，不以访问/归属情况改成贡献N。
- 已实际必要exact-v1 §3.1三阶段变换及§3.2/Alg1、4.1–4.3/Table3与§5直接反侧。只保架构/evaluation用途，不在Books传播具体攻击payload。CodeNet Python先过滤原程序测试失败/过长等；三小模型参与进化、四指标与辅助LLM将自然语言拒绝判高分/分析判低分，等价性只有限unit-test，不证明所有语义不变。
- ASR为refusal+test-failure两个口径的和，不能把拒绝当语义误解/机密保护。Gene使DS/CodeLlama refusal升，但CodeGemma ASR50低于Rand62，weakalignment只是作者解释，不是已定位内部因果；7新模型transfer/最高70不证明自适应清洗/专门deobf模型或人类逆向不可解。源三模型参与search不同于heldout，运行原程序开销不含所有模型调用/进化搜索/人审。硬件/precision/全search预算/CI未在已采用域披露；代码/图像素/复现未核。保这些已读反侧但日期未闭，不继续为了I补owner或SAVE。

## 11745 — BridgeVLM

- [exact-v1](https://arxiv.org/html/2606.11745v1)完整§3/§4核心Table1–5/Limit、AppB1/C/D/E/F1直接反侧；2+2+2=6，表示身份/边监督差额深入。learnable variable queries跨图读dense视觉，lowrank MLP诱导adjacency，rowNorm后双向用不同transform聚合，再node→graph→node融合与原视觉/query一起供decoder。不是decoder每层强制执行SCM的do-operator；DAG penalty是额外训练约束，不因名称就证明真实因果或有限优化得到严格无环。M3S按availablelabels激活edgeBCE/description对齐；Hungarian匹配为节点身份对齐后再施加边监督，是重要条件，不能先让oracle adjacency替latent端点命名。
- Table3 GraphAlign-only31.0低于answer-onlyBridge35.6，NodeAlign54.4，AttBias59.8，组合GraphAlign60.2。完整component Table2用AttBias而default不启用，不能把59.8的消融因果和54.4headline混口径；DAG置allones、Node同时去RAMP/nodeinject、Graph同时去global/fusion，非完全容量匹配各单一新因素。Slot baseline也同时换多个结构，不唯一归因路由。F1 variable→description匹配频率Q1 .27/.43/.30、Q2 .38/.31/.31，提示身份不稳，不是已证唯一原因；GraphAlign 100F1称byconstruction/已知scene，不能当真实未知图发现。
- Causal3D/CausalVLBench按已见scene内label-stratified8:1:1，宏平均不是全样本micro；CELLO zero-shot63.1低NoFT66.2，额外适配90.3高83.7只说明有监督新bench。文字/图先验原dataset生成条件不授权真实环境因果，未声称AIscience结果。2A100、LoRA/5epoch/earlystop、batch8，Table7 batchlatency128.26→228.97ms不授小开销/线上SLO，precision/seedCI未披露；全数据/描述/匹配、适配与新旧消费者回归均付费。未核代码/图像素/复现，不采用optional schema-routing执行recipe或真实动力学。
- **actual owner**：`MULTIMODAL-REPRESENTATION` Ch23；实际读object-centric bottleneck2602-16689完整段与随后residual-evidence两段。旧段区分object token/组合reader预算，却没有“监督边前先绑定latent端点”这项具体干预。拟16689完整段marker后/residual-evidence前，保其已描述的下一步slot分配交接，不重复Ch25环境动力学。
- **唯一拟稿，待reader必要/actualowner/PRE：**

视觉slots若要承载带标签的关系图，边监督之前还须先确定每个端点指哪个变量。可以让共享queries读多图形成变量候选，按节点描述匹配latent身份，再分别用可用的描述与边标签约束tokens和邻接，最后以方向区分的message passing及global tokens交给decoder。描述、端点对应、路由矩阵与最终答案是不同对象；稀疏/无环先验或名为causal的token都不自动获得真实因果身份。

[受限多图对照](https://arxiv.org/html/2606.11745v1)中，只有oracle边监督可比answer-only更差，节点对齐更有用；后验匹配显示端点身份仍可能分散，支持先验图与latent语义分开核，而非宣布所有图监督无效。双向message passing与多模块消融不证明唯一SCM机制，同scene留出和额外适配也不授未见因果场景泛化。图/描述制备、匹配、结构分支和全部训练/回归均付费，batch延迟不是免费；身份、结构或质量失配时保留dense/普通slots、显式可信变量与独立任务核验，不由较高edge F1签发真实干预结论。

## 11743 — TacCoRL

- [exact-v1](https://arxiv.org/html/2606.11743v1)实际完整§3/4/Table1–2/Limit与AppA/B1–3/C/D相关参数。2+2+2=6，policy-facing接触接口/realanchor差额深入。触觉history10×1536经CNN/projector到prefix+suffix8+8，threshold.4/count1 contactgate按最近history参与；这一gate/双路fusion本身已有TacVLA主线，不重复当新成立。先sim/realflow co-train，再sim128env PPO+realBC anchor；critic/reward/privilegedstate训练期用、部署不继承权限。不是真实无数据/无新增示教。
- 长期差额是sim训练接触纠错时joint-response与policy-facingnormaltaxel均须对齐。B1每joint10秒sweep拟Kp/Kd/feedforward+跟踪差/差分SPSA，heldoutJ4特选最大改善不当所有task统计；B2只normalchannel springdamper/threshold/activecount/centroid/hist/temporal差，未恢复shear/fullforce。仿真状态可算reward不代表现实受测安全，触觉分布匹配亦不等充分动力学保真。
- 四bimanual近rigid任务，每task50real+20simteleop扩200sim、20realtrial，单π0.5/PiPER平台。Base直接sparseRL全0，co-training后再RL有效；explorationnoise降低start，stage表不能混不同noise baseline当纯RL唯一因果。Assembly#2 β0 real45、β.1/1为80、β5下降，即最低BC loss不等最优真实控制；α0没simdemo real25，表明warmstart有效人口，不普遍认定所有sim/real比例。
- Table4 realanchor episodes200与§4.2/表3 real50口径不闭，不补literal唯一数据量配方。硬件训练GPU/precision/seedCI/端到端控制尾延迟Not Disclosed，controller频率/步长不能捏造；单位/传感器标定与realdata是成本，未核代码/视频/复现。任务digitaltwin手工建设、可变形/流体未覆盖；平均72.5/20trial不授物理安全或任意接触迁移。
- **actual owner**：`MULTIMODAL-EMBODIED-VLA` Ch26；实际读TacVLA contactgate两段与未来预测触觉两段。gate已有，不为此改书；新增sim接触后训练的policy-facing校准/realanchor有效范围非旧gate或forecastproducer。拟TacVLA2603-12665第二完整段marker后/未来监督段前两段，不锁章。
- **唯一拟稿，待reader必要/actualowner/PRE：**

触觉条件可读还不等于policy已经学会接触后的纠错：成功示教很少覆盖卡住、偏斜与遮挡后的恢复。一条替代训练分支先让模拟器与真实controller响应、传感器的normal taxel统计共用可比接口，用混合示教获得可探索初值，再在仿真任务reward旁保留真实轨迹的监督anchor。训练critic可见的特权state不交给部署actor，接触flag也不替模拟保真或真实动作验收。

[TacCoRL的有限对照](https://arxiv.org/html/2606.11743v1)中，直接稀疏RL不能从base启动，而过强realanchor虽降低监督loss却压制真实控制改善；因此校准、初始化和anchor强度必须与实际反馈一起核。只对齐normalchannel、少量近刚性任务与单平台试验不覆盖shear、流体或未知接触，real数据量口径未闭也不能补成唯一recipe。数字孪生、标定、示教、仿真rollout与真实回归全付费；接触模型、传感器或任务支持失配时，保真实示教、较保守适配及独立controller/接管，不以模拟成功或小平均loss批准物理安全。

## 11700 — CompRank

- [exact-v1](https://arxiv.org/html/2606.11700v1)实际§3/4/5/Table1–2、AppA1–3/B/E/Table4/F。2+2+2=6，文档state/消费attention/候选评分分责gap深入。独立causal docblock/interdocmask、每doc相同localposition、query固定Coffset读全部docs；docK/V可理论预算但受模型/mask/template/截断身份绑定。压缩只最终query→doc消费支集，非删去docsideforward/全部KV/所有层重编码；uniform segment/last-k/文档selfsaliency不是queryaware真实相关性。
- 固定layer20、一个completionfirst监督token、meanhead attentionmass perdoc，同一score经τ.05softmax作positive-document CE训练，部署直接排序，不生成ID。CopyNet目标受有标签candidatepool约束，attentionmass不自然是校准relevance/事实支持；没有ID语法错误不保证相关性或答案。Mistral7B fullparameter/MSMARCO50k/30doc×256token、oneepoch/8H20/bf16；所有方法BM25top100 BEIR共池但basefinetune/目标预算非全部matched。
- Table1 uniformStep10平均39.2低Full39.7，Step5更多token39.1，selftopk/lastk更差但部分domain反转；不能宣称均匀总最优。TREC-COVID50queries从train30到test500，DirectListmissing/truncated人口严重且outputbudget/decoder协议影响，narrowfloor不是所有listwise无法泛化。AppF明确single-run无CI。
- Table2 fullforward含doc重算11.72s vsqueryforward .05s只是simulatedpreencoded分解，当前pipeline仍重算、无优化cache存取，234x不能当部署净收益；12s endtoend/500doc单配置不授RAG整体SLO。全部docencoding/cache驻留加载刷新、训练/检索/attention与reader验原文全费。未核代码/图像素/复现，不采压缩所有quality无损或生产缓存已实现。
- **actual owner**：`AGENT-RAG` Ch76，实际读prefix三分支/FusionRAG完整两段/MiniReranker2606-10759完整段及OfflineIngestion交接，另MVP queryconditioned setanchor一段。已有分支处理cache边界，却没有同attentionmass的candidate级训练/直接排序与uniformcoverage-v-selfsaliency、模拟cache分解的具体接口。拟MiniReranker marker后/OfflineIngestion标题前两段，不复制KV底层或注意力归一理论。
- **唯一拟稿，待reader必要/actualowner/PRE：**

重排若已经用query到文档的attention mass评分，还可以让训练直接监督同一份candidate分数，而不先学生成ID再改读另一种内部量。独立document blocks与共享局部位置使文档state不依赖本次query/候选次序，最终query侧另选少量token参与评分，再在输入候选空间内训练pointer目标并直接排序。独立编码、消费支集与评分目标各有身份；不生成ID只排除了该输出格式错误，不认证相关性或事实支持。

[CompRank的有限对照](https://arxiv.org/html/2606.11700v1)中，均匀片段覆盖可优于文档自身saliency，却有压缩质量损失，更多token亦非单调；长候选表的ID失败反侧限受测训练/解码协议。当前实验仍重算document blocks，预编码query-only时间只是模拟，不含cache存取/驻留/刷新，不能当已交付加速。语料/模型与mask版本、训练、完整编码/检索/评分和reader取证都计费；局部证据稀疏、cache复用或净质量预算不合时，保完整tokens、普通重排与原文核验，不由无ID错误或短online快照签RAG可靠性。

## 11672 — LLM Agents vs SAST（具体NC提案）

- 采用非writer唯一首备canonical§60，作者已实际完整读取该节必要支持/反侧，不重复Methods。原5=2+1+2保持：仅Snitch固定prompt/逐文件Ollama三tag、三repo224files101816LOC；Bandit medium/high作为reference，位置/类别full或partial match1/.5，potentialFP条件分母不是自然良性FPR。新增未被Bandit报的漏洞未独立确认，工具reference与真值冲突不能替任一方签完整recall；单run/小时估算不授全部现代Agent或精确SLO。
- **actual owner与具体NC**：`PLATFORM-EVALUATION-SYSTEM` Ch66，实际读“为什么选一个分数不是评估”完整问题/分布对象段、2604-22597 reference资格完整段、SpecBench2605-30314历史concern未列保Unjudged/不能叫开放precision完整段及2610-22158真实无缺陷-v-提示缺陷、条件分母完整段。已承载reference非truth、未列gold保Unknown与条件检测不等全请求分母；本项受测低match及作者上限判断不足增加通用Agent替换SAST机制。故建议标准完成/已有覆盖、不改Books；具体局部相对工具/人工结果留报告，非贡献前N，不因安全名词造正文。待reader独核actualowner/NC，不自行授终态。

## 11652 — IAPO

- 唯一首次必要由非writer执行并存canonical§61，作者已完整消费并采用其精确证据/反侧，不第二Methods。原6=2+2+2。两turn视觉编辑/答题、六row/column工具及语义块；自产toolcall logprob的input梯度乘embedding范数归块，非标准baseline-path IG，不继承completeness/implementationinvariance。teacher-actor块分布KL扣outcome后组内标准化广播token，只额外监督，不是因果credit或执行权。
- 保Qwen2.5VL3B actor/同集7BGRPO teacher/冷启与额外训练预算，A10040GB、Chart/Table分训与两turn人口。256条工具误用proxy相关非有益因果；8Bteacher、λ1有反退，不授越强越重越好。TRM/ToRL实现差别与precision/seedCI/全预算ND留存，未核代码/复现。
- **actual owner**：`AGENT-TOOL-CALLING` Ch78，实际读2601-18631合法tool身份与过程reward完整段，及2609-22910同前缀真实crop/随机crop/不调用三分支归因完整两段。现reward validity/outcome与真正干预credit不同，没有teacher/actor输入块梯度分布对齐的受限代理。拟18631过程reward完整段后/“编译器反馈可以前移”标题前两段。
- **唯一拟稿，待reader actualowner/PRE：**

没有唯一规范调用轨迹时，训练还可比较teacher和actor对同一输入语义块的敏感度分配，而不强迫逐步照抄工具序列。对各自产生的tool-call logprob取input梯度，与embedding相乘后按块聚合范数，再把两份归一分布的差异作为结果reward旁的惩罚；该信号约束“此模型对哪些输入敏感”，不是证明这些块实际有益，也不是标准路径积分归因的完整性证书。

[IAPO的有限两turn视觉工具对照](https://arxiv.org/html/2606.11652v1)支持这条额外监督接口，但更强teacher或更大惩罚均可能反退，额外teacher训练与双侧反向也未变成免费预算。工具调用率、归因块更像teacher与最终答案/合法执行须分别验收，不能外推长期Agent因果。语义分块、teacher制备、rollout/梯度与完整新旧任务回归都计费；teacher、块定义或真实效用失配时保留普通SFT/GRPO、实际工具反馈与独立outcome verifier，不由较小KL批准调用权限或任务完成。

## 11648 — Dummy Backdoor as a Defense

- 唯一首次必要由非writer执行并存canonical§62，作者已完整消费原源命题/反侧，不第二Methods。原7=2+2+3保持安全深入。主动种known dummy trigger再clean/refusal目标清理；同attack objective下TAC平均activationdelta cosine仅提示共享，不证明唯一因果电路。未知trigger不等未知目标，C3不同任务NegSentiment→jailbreak几乎无效为采用中心边界。
- 三7/8B模型/三trigger类型，Alpaca20k及dummy/clean200、LoRA训练；“50%剪枝”只LoRA/allparams约.15%，不可扩到全权重。99keyword refusal ASR不等真实harm、MTBench均值不等全部旧效用，Qwen局部utility下降/无完整CI不授等价。两阶段费不能由同超参对照叫matched总预算，设备/precision/seedCI/全时ND、未核代码/实施/复现。
- **actual owner**：`PLATFORM-SECURITY` Ch72，实际读2603-23268稀疏mask/移除/保护三分责两段及随后2509-03985输入贡献-v-参数位置完整两段。原可定位后修参数，不持有可控dummy任务作为未知trigger清理proxy的条件；拟23268第二完整段后/输入贡献段前两段，不宣传后门构造recipe。
- **唯一拟稿，待reader actualowner/PRE：**

未知trigger未必要求先逐一恢复其字符串：在受控隔离模型中，可以植入一个已知dummy任务，再用该trigger配可信clean响应微调清理，检验同攻击目标的未知trigger是否随之减弱。这里可控代理提供的是待测训练方向；不同trigger的平均activation差相近，不证明唯一共享因果电路，更不能把“trigger未知”扩大成“攻击目标也任意未知”。

[有限dummy清理对照](https://arxiv.org/html/2606.11648v1)的跨任务代理几乎不能修复另一目标，说明任务匹配本身就是边界；keyword拒答ASR与少量utility也不认证实际无害或全部旧能力保留。种入/清理、原与候选artifact隔离、全部攻防和效用回归都计费，LoRA剪枝比例不等全参数删除。目标、代理或回归失配时保可信原checkpoint、受控更新与独立输出/effect gate，必要时不发布，不让可清理一个dummy成为未知自适应后门的安全证书。

## 11643 — Cross-Format Robustness / FormatMix

- 采用非writer唯一首备canonical§63（其reach建议已由本人纠正），作者完整消费必要原源/反侧，不第二Methods。原5=2+1+2保，具体eval差额深入。source-item先split，再四format/各三改写投票；11842源题142104实例非独立题。any格式成功/all格式成功与比率回答breadth-v-consistency，不是普通samplingpass@k或参数是否有知识的直接测量。TF原错项/开放去选项改变信息，有限同义人审/多数judge不使全部语义等价。
- GLM4-9B一epoch/8H20/30%扩1.9×instances，MCQmatched只同instances非tokens/FLOPs，4×非同预算upperbound。Targeted与random偏目标不同，Llama目标筛选不稳，BBH TF .6054低base.6214；不授更强formatmix普胜。筛选/改写/judge/选样训练与全回归费用，precision/seedCI/完整预算ND、未核代码/复现。
- **actual owner**：`PLATFORM-EVALUATION-SYSTEM` Ch66；实际读2605-16023白盒format/readout完整段、下一2605-20530类别菜单-v-自由诊断完整段及已有12117格式elicitation两段。它们没有source-item对齐下any-v-all格式的breadth/consistency以及扩样预算分责。拟16023完整段marker后/“诊断能力的评价…”前两段，不改任务本身真实语义由谁核。
- **唯一拟稿，待reader actualowner/PRE：**

格式鲁棒性还须以同一源题对齐，而不把不同格式的平均accuracy直接并列：先按源题划分训练与测试，再制备多种输出格式及有限同义改写，分别统计任一格式可解的覆盖与全部格式均解的一致性。两者可以不同，格式中的选项、真假命题或自由作答也可能改变可见信息；“同题”与“语义等价”仍需独立核验，不由改写器自签。

[有限FormatMix对照](https://arxiv.org/html/2606.11643v1)把这两种对象连到训练mix选择，但有BBH/目标筛选反退，三改写投票和LLMjudge亦非真值。配平实例数没有配平tokens、改写筛选与训练compute，较少源题扩格式也不等普遍最优比例。制备/核验、全部选样与训练、旧能力和留出format回归均付费；语义、预算或目标人口失配时保原格式/原分数、随机或较窄扩增与独立人审，不把any-format提升当作所有接口均可靠。

## 11634 — SWARR

- [exact-v1](https://arxiv.org/html/2606.11634v1)完整§3/4/5/Limit及A1.3–4/A2.2–3必要；2+2+2=6，具体架构适配/数据选择差额深入。SA权重直接换固定window，SFT同数据/设置，再同CISPO系recipe的on-policy RL。长期主张不是新RL算法，而是只看conversion+SA来源SFT会误判SWA的数学长输出可行性。42B私有mathheavy SFT、49k AceReason、1.5B主/4B补充，64k生成；不是免预训/免训练转换，原SFT数据不公开。
- Table1同900step与约500GPUh额外RL时间两套口径分别保，总费用还含SFT。8k gap−.4、4k约同时间+.1在bootstrap不确定内，不授优于SA；2k仍落后。跨SFT取各架构2500步内best-checkpoint正确轨迹、1kbin匹配length、3.3Btoken，SWA来源同时改善SA，支持数据分布影响但不证明独有locality因果。SA-SFT参考下probabilitygap不是熵/MI，正确且>8k筛选人口不代表全生成；stride“lowerbound”未作一般保证。轨迹文本重申案例仅illustrative。
- A1.4长输入理解不带SmoothReading时平均落后26.24，另加agentpipeline不能与原数学结果混；4B RL步2200vs2500不叫同预算。bootstrap对重复评价不是多训练seed。A2 recipe同时有groupzero过滤/allpass筛选/async旧policy/entropy earlystop等，不唯一归onpolicy；不采完整精确loss/稳定性recipe或架构memory消失。
- timing是真slidingKV丢旧项，不是保留mask。65GB约束32k最大batch下6.2×不同batch比较，不授同batch/SLO/generalkernel收益。GPU型号/全精度与seedCI未在采用必要域明示，policy-loss FP32不等全部权重FP32。私有SFT/训练框架未核，不因不可选实现阻正文证据；所有转换/SFT/RL、源轨迹生成/筛选与跨任务回归付费。
- **actual owner**：`MODEL-LONG-CONTEXT` Ch22，实际读“Immutable Task Prefix 与Recent Reasoning”完整定义/训练段与ThinkStream相反state边界两段；旧prefix可见性训练没有比较fullSA-v-local架构来源轨迹与onpolicy适配后可行性。拟PrefixSliding完整训练局限段后/滑动窗口密集观测段前两段，保仍可回完整历史。
- **唯一拟稿，待reader必要/actualowner/PRE：**

限制attention窗口后，训练轨迹本身也成为适配对象：固定的full-attention示教可能反复依赖窗口外信息，直接模仿后性能下降，并不单独证明局部架构不能完成该任务。可在相同局部可见性下采样并强化成功轨迹，再用跨架构来源、正确性与长度分布对照检查数据是否更适合当前读写限制；这与保留task prefix是可组合但不同的选择，不恢复已丢失的精确历史。

[受限数学长生成对照](https://arxiv.org/html/2606.11634v1)中，较大窗口经RL可缩小与SA的差额，过小窗口仍受限，长输入检索又明显退步。来源轨迹也改善SA，参考模型的locality proxy和筛出的正确长轨迹不证明唯一因果或任意任务无须长记忆。同step、相近额外RL时间与总SFT加RL预算须分开结算，最大batch吞吐不签同延迟SLO。转换、造数、全部训练/回归与真实sliding-cache执行都付费；数据、窗口或任务失配时，保更大/full历史、显式重申或检索，不由一套成功recipe宣布长程状态已无用。

## 11614 — DMIL

- [exact-v1](https://arxiv.org/html/2606.11614v1)完整§3/4、6.1–3与7.1/7.2相关实现/直接反侧；2+2+2=6。先模态内VAE把Z拆M/N（M有task监督），再冻结前阶段，以分布对齐提R/unique，N1/N2/elementwise product作synergy支路，最后各component线性读出/gate样本加权并jointfinetune。没有真实PID标签/唯一识别，factorizedq与KL/reconstruction不自动证明真实因素独立/完整信息无损，N无独立targetloss不等已证N与Y独立；不采用“纯冗余/唯一/协同语义已分离”。
- Th1条件信息恒等式给lowerbound，C=f(X,Y)、Z=φ(X)等条件保留；大lowerbound不是“高I必须最小H(C|Z)”的必要性定理，也没有建立将网络gate直接读为真实逐样本PID的桥。采用可比较训练分支与交互人口，不复制强理论证明。Eq9 synergy只是joint正确/两unimodal均错的有限行为统计，ensemble可联合弱证据，不授所有latefusion天然零synergy。
- 5runs mean/std、ResNet18/ViT/Transformer，audio/visual/text benchmark未等完整训练预算；阶段10+5–10+joint不等单joint同费。CMUMOSEI主体binary与appendixthreeway口径不闭，KSViT mAP81.83与后表81.50不同，不照抄泛性能数。合成R/U/S人工数据生成可检验受控混合，casegate=1不是语义因果真值。Classheldout OOD只称distinguish representations、读出训练未完整披露，不能视为未见class分类保证。
- 7.2的elementwiseproduct可把toyXOR线性分开，但不证明所有真实协同因子可被当前latent恢复。GPU/precision/全训练时/SLO Not Disclosed，扩展三modal也换为仅ID分解，不把三modal实证当同一二modal理论。未核图像素/代码/复现；所有encoder/decomp/reconstruction/gate、超参/训练与独立行为和旧任务回归全费，不延展医学应用分支。
- **actual owner**：`MULTIMODAL-REPRESENTATION` Ch23，实际读2605-15868 shared/private删除资格与SUPRA2605-24684独立head/aggregationbypass完整段，以及后ICL对应路径两段。现有分流未持有先模态内分解再跨模态一致/残余product、逐samplecomponent读出的交互人口接口。拟SUPRA完整marker后/融合后ICL段前两段，不授真实因素本体。
- **唯一拟稿，待reader必要/actualowner/PRE：**

融合也可以先把“单模态可预测的部分”与“需要组合才有用的候选”分路训练，再对前者做跨模态一致/特有分解，让各支路独立读出并按样本混合。残余间的乘性交互可以提供简单线性读出没有的表达；但支路命名、Gaussian潜变量或重构loss都不证明已恢复纯粹的冗余、唯一与协同语义，样本gate也不是信息分解真值。

[DMIL的有限合成与多模态对照](https://arxiv.org/html/2606.11614v1)支持把交互组成纳入融合选择，而非认定joint或late ensemble统一最优。其信息lowerbound没有为实际latent语义建立可识别性，joint正确/单模态均错的synergy统计也不能排除弱证据组合或读出差异；三模态扩展与类留出又改变协议。多阶段编码/重构、对齐、所有读出与gate训练都计费，质量或分解资格失配时保原表示、简单joint/latefusion与独立单模态/组合对照，不由漂亮latent标签签无损信息与通用OOD。

## 11599 — SteerBoost

- [exact-v1](https://arxiv.org/html/2606.11599v1)实际§2/3/4/5、E/F/G及H反侧。2+2+2=6，具体早期干预诊断/搜索费用差额深入。每α先steer生成k个token，再unsteered对完全相同已实现序列teacherforce一次，对token/layergrid的geometry/dynamics/condition特征拟GBDT三类under/success/over。固定实现序列的hidden差是局部介入效果，不是自然unsteered后续输出因果；gainimportance也不等因果根由，单feature组与多grid组总和importance不可直接比。
- 150concept×50Alpaca prompt×2methods×三1.7–3B、1.42M生成是相关配置非独立自然任务。GPT5nano judge/600人审κ.83只是有限agreement，otherjudge/人审不授所有标签真值；120ID/30OODconcept、prompt6:3:1与5seedtree训练不等5独立LM/生成人口。succ最难，20–37%被误判under；部分cross-method仅一Qwen且dropcondition重训，不授任意model/steeringfamily迁移。
- 搜索对全部α预生成earlytrace/无干预forward后按successprob排topK并rollout、用judge已知success早停。itemgridoracle上界是本有限网格/标签不是全参数最优。98%grid success用decodedtokens11%/IGS-A40%只这proxy，tokens未含第二unsteeredprefix前向、activation读取/驻留、feature/XGBoost/所有judge与离线vector数据制备，不等全费用/墙钟11%。15A6000每modelmethod约1.5day造数据，precision/servinglength并发SLO未披露，未核代码/图像素/复现。
- **actual owner**：`WORLDVIEW-REPRESENTATION` Ch5，实际读2602-12418同core配对/保residual两段、2509-10809读写方向完整段与下一2507-06427输入改写段。既有方向选择/剂量回归未持有“同已实现早prefix双forward→预测under/over→候选α排序”的受限省fullrollout接口。拟2509-10809完整marker后/输入检查触发段前两段，不改变外部控制权。
- **唯一拟稿，待reader必要/actualowner/PRE：**

方向已确定后，还可以先预测本次剂量会不足、有效还是过强，再决定哪些候选值得完整rollout：对每个候选强度生成少量steered tokens，用同一已实现序列再做unsteered前向，比较跨层/跨早期位置的变化并训练结果分类器。它观察的是固定prefix下的局部介入与所选标签的关联，不是自然无干预续写的对照，也不证明早期状态拥有结果真值。

[SteerBoost的有限小模型对照](https://arxiv.org/html/2606.11599v1)支持这种候选搜索顺序，却最容易漏掉刚好有效的剂量；未见concept与跨方法迁移亦不能推出任意模型可控。完整搜索仍要支付全部候选的短生成、第二前向/activation、分类器与judge，decoded-token节省不能直接换算总费或墙钟。向量/标签制备、模型层位与全部原行为回归也计费；预测、剂量或质量失配时保较弱干预、完整网格/原hidden和独立行为验收，不由高macroF1或预测成功签发安全编辑。

## 11576 — AVIS

- [exact-v1](https://arxiv.org/html/2606.11576v1)实际§3/4/5/Table1–5、AppA2/B1–4/D必要。2+2+2=6。先headwisekey对均值方向角阈值删视觉token，再用仅visualembedding Conv/MLP的difficultyhead选K=1/3/5/7，多rollout共享prefill，最后多数/plurality答案。两轴分阶段而非学到联合最优，AppD明确真正jointpolicy未解；同图不同Q的纯视觉head无从区分问题难度，不补questionaware实现。
- 校准5k例/每例10次base正确率>=.5二值监督。softmax输出是“该阈值事件”的分类置信，不是单轨迹p；Eq5二项correct-v-rest只binary近似多类plurality，不能将分类器输出代入为已校准最优K证明。中间budget多、两端少只是校准启发式，bins具体边界未给，不照抄literalrecipe。ρ正文时而pruned/时而retained且Eq2符号未一致，不采精确计算公式，但共享vision/prefill+各分支decode分责可保。
- Qwen2.5VL7B/12image6video，32B过滤MCQ及5次格式过滤/二值校准人口不是自然线上；5k分类训练/校准split有限、无全部seedCI。K1greedy vsK>1温度.7/topP.9改变sampling，不能独归rolloutcount。Table1 AVIS MMStar61.6<vanilla62、BLINK56.7<56.8，Rethinker Mathvista/Star等退，Table5 one-axis局部更好，不授每项Pareto支配。静态keydiversity不保证保留微小任务关键证据，平均“97.99%accuracy”非逐例无损。
- Table3单L40 48GB/vLLM.10.0/100imagepair/sharedprefill decoding795→757s约1.05而纯prune558更快；理论/FLOPs收益不能冒完整请求大倍率或SLO。precision与batch并发/全calibration/training时未披露。KDV/visualencoder仍付费，未核实现/图像素/复现；所有造数/10rollout、分类训练/阈值、全部视觉编码/cache驻留和真实答案回归计费。
- **actual owner**：`MULTIMODAL-REPRESENTATION` Ch23，实际读固定预算H3/2610-22957 coverage加slot完整段、DocPrune2604-22281完整段及12412可恢复两段。现有“表示缺多少再扩slot”没有“视觉上下文与reasoning rollout共预期预算、calibration head概率身份”的接口。拟2610-22957完整marker后/DocPrune前两段，不迁调度/SLOowner或基础采样公式。
- **唯一拟稿，待reader必要/actualowner/PRE：**

视觉证据预算还可以与回答搜索预算共同结算：先以视觉keys的多样性提出保留子集，再用预先训练的难度分类器为不同输入分配rollout数量，让同一份视觉编码与prefill供各分支共享。这是一种分阶段的预期预算分配，不是已解出的联合最优；当分类器只读图像时，同图不同问题的难度差不会自动进入决策。

[AVIS的有限对照](https://arxiv.org/html/2606.11576v1)支持比较两轴配置，但二值“多次作答正确率越阈值”的分类置信不等单次正确概率，多类投票也不能直接继承binary多数公式的最优分配。部分任务或单轴配置更好，删掉任务关键细节更不能靠更多推理补回；shared-prefill下的小墙钟收益亦不同于理论FLOPs。校准造数、分类器/阈值、视觉编码/保留cache、全部解码和独立grounding回归都付费；支持、概率或净质量预算失配时保原图/dense tokens、固定小K与独立答案核验，不由自适应预算签无损理解或生产SLO。

## 11400 — Steering Where to Listen

- [exact-v1](https://arxiv.org/html/2606.11400v1)实际§3–6/Eq1–5/Table1及直接位置切片。保原5=2+1+2。相同audio、focus与generic instruction末token hidden差构成向量；各生成step norm-preserving注入，比较steered/base text→audio attention，末半层比值加权汇总后取定长窗口最大值。这是可干预的时间读出，不证明attention因果解释全部行为/训练无关普适机制。
- 500三事件合成：非重叠4.5–5.5s不同标签animal6/language4，间隔1s匹配能量noise；窗口W使用ground-truth duration，direct prompt也获duration。overlap是GT覆盖率而非IoU/未知长度检测。Qwen2Audio7B32层/AF3 28层，λ.1/后半16–31与14–27。Figure48例5s不替全部500。Table1 Qwen Begin36.9/Middle73.39/End72.32，AF3 Begin73.98/Middle48.31/End83.87；正文“两者middle最弱”与Qwen行不符，且AF3 direct Begin98.91优于73.98，不授各位置改善。MMAUmini仅attention诊断，非同协议定位QA证明。
- 固定音频的positive/negative构向量forward、base/steered forward、attention提取/层窗选择与独立定位核验全费；未披露全硬件/precision/seedCI/全请求SLO。无代码/复现/原图像素核验；不把两次attention比较说成只需两次总forward，不授自然并发/未知duration或真实ASR改进。
- **actual owner**：`MULTIMODAL-REPRESENTATION` Ch23；实际读NAACA2605-13651完整门控段及后encoder层身份2604-02043两段。前者决定送哪个声学窗，后者决定读哪个checkpoint/layer，均未有同音频instruction contrast改变时间attention读出的接口。拟NAACA完整段marker后/“选择语音 encoder 的层之前…”前两段，非Ch66通用attention解释复述。
- **唯一拟稿，待reader necessary/owner/PRE：**

选好声学窗口之后，还可检查语言条件是否改变模型在窗口内读取哪个时间位置。固定同一音频，以聚焦指令和一般指令的hidden差提出方向，再对后续计算作受限注入，与未注入路径比较text-to-audio attention；按层汇聚其变化，可提出目标事件的时间区间。这里改变的是条件化读出，不是取得新声学信息，也不把attention峰直接认成完整语义或唯一因果机制。

[受限三事件定位对照](https://arxiv.org/html/2606.11400v1)用已知目标时长选窗口，只支持非重叠合成事件中的诊断；GT覆盖率不等未知长度检测或IoU，各位置也非都胜直接提示。构向量的对比forward、base/steered路径、attention提取与层窗选择均付费，免训练不等在线零开销；自然重叠、时长或读出失配时保原音频、专用定位器与独立声学核验，不由attention重新集中批准理解、转录或持续监测可靠性。

## 11396 — PLUME

- [exact-v1](https://arxiv.org/html/2606.11396v1)实际§3/4、5/Table1–3、A、C、E/F/G必要与直接反侧；保原6=2+2+2。有true sim参数/失败轨迹的WAE把不同参数与reward映到共同latent，MMD对齐normal prior；flow matcher以known/unknown mask联合建模belief particles/action/nextobs，Mamba2保存动作观测历史。部署只推断belief不更新模型权重，非无参数监督/普遍Bayesian posterior。滤波时generated particles互相不可读、known不可读unknown，以免间接通信坍缩；Z-estimation FM项对参数encoder stopgrad，非整个表示永久freeze。可支持的接口是参数belief与action-conditioned预测共同更新而非点估计先固定。
- 规划多候选H步、decoded reward与inverse-dynamics flow-loss likelihood proxy加权，非精确校准density/安全certificate。C明确average plan log-likelihood阈值为heuristic，先无earlystop trials后hoc调阈值；非校准OOD风险界。4sim任务150trials、硬件screwdriver30trials，valid先排unmate/drop，goal distance常条件于valid，不拼全样本成功。2/30 unmate仍在；single particle valid82.7>81.3，detached85.3/.80优81.3/.88，NoBelief valve.52优.59，不采所有组件各任务皆优。UWM过滤失败、baselines无规划/停止，不当全部预算匹配因果。
- Allegrov4 PD/Xela/Vicon，IsaacLab除bucket SAPIEN；仿真监督/shape预训真实依赖，少量hardware不授所有未知物体/真实安全。训练8h×2RTX5090；各task规划.26/.37/.18/.68s、belief更新.03/.05/.03/.03s不等controller尾延迟。precision/完整所有seedCI/同B/K预算未在采用域披露。全sim/失败数据、参数表示、历史、particles与候选rollout/阈值和真实接触核验付费；未核代码/视频/复现，不补算法局部未闭变量为literalrecipe。
- **actual owner**：`MULTIMODAL-WORLD-MODELS` Ch25；实际读Pinductor/PatchWorld及sigma-history2509-04213完整两侧。已有程序候选belief和已知sensor滤波，未有学得参数粒子与动作/观测联合flow建模及独立采样防坍塌。拟2509-04213完整段marker后/“状态分路也可以保持相同的预测时间单位…”前两段，Ch26只消费规划而不重复参数模型。
- **唯一拟稿，待reader necessary/owner/PRE：**

参数不确定性也可以直接进入学得的transition接口，而不先选定一组摩擦或形状再规划：用模拟器已知参数与reward学习共同latent，维护多份参数假设和动作—观测历史，再用带known/unknown mask的同一flow模型提出belief更新、动作与下一观测。滤波时还须阻断生成粒子之间以及经known token绕行的通信，避免把多个样本坍缩成同一个答案；部署更新的是参数belief，不是在线重新训练权重，也不因此得到真实后验校准。

[PLUME的有限操作对照](https://arxiv.org/html/2606.11396v1)支持这条联合接口，但point/no-belief或其他消融在部分任务更好，失败过滤与规划预算也限制归因。用inverse-dynamics loss近似轨迹likelihood、再按事后调阈值停止，只是经验OOD启发式；valid条件下的距离和少量真实接触不能代签全部执行成功或物理安全。模拟参数/失败数据、表示与历史训练、全部particles/候选rollout、阈值调节和真实观测回归均付费；参数支持、观测或预算失配时保留多个假设、已知模型/可信simulator与短horizon实测重规划，不让想象分数取得真实环境提交权。

## 11386 — Full-Duplex State Inertia

- [exact-v1](https://arxiv.org/html/2606.11386v1)实际§3–7、A1–4/B/F/H/I必要。保原6=2+2+2。双流user/model，logitlens下一user codec与model text/audio affinity为内部读出proxy；offline可见futureuser，非在线stateoracle。100合成turn分析，ZBB另50subjects×真假2=100，关键主体放首词，无filler；先5s生成再打断与无preceding generation人口不同，声学/streamconditioning并未单独控制，不授唯一stateinertia因果。
- 按独立convo生成perception-minus-generation方向，layer/α/span扫描；部署energy onset触发短3step衰减，不持续注入、不依赖onlinefuture affinity。PersonaPlex49→28→45正确/IWOR74→40→72，Moshi43→22→34，Raon10→3→17仍低，不把recovery200%当普遍能力。A4 ASR Parakeet0.6b+GPT4.1mini，IWOR只显式首entity/同义词，裸yes/no即0，不认证真实听见/因果知觉；分开correct与IWOR。F延长span退；H FDB Persona3.34→3.41/Moshi3.45→3.36/Raon2.41不变，原作者withinuncertainty表述不授无害；I随机false triggers越频繁judge质量越退。grid选最优未给独立heldout校准，不授所有部署最佳层/α。
- B披露L40S，未训练/finetune不等全部代价小；precision/并发/真实audio总延迟及完整seedCI未披露。合成/提取向量、模型驻留/层注入、VAD/onset与false-trigger回归、ASR/judge/人审均计费；未核代码/真音频/复现，不采推荐新VAD已实现或真实系统安全。
- **actual owner**：`MULTIMODAL-REPRESENTATION` Ch23；实际读primary/third-party配对2604-17358两完整段及后DM-ASR。原段明确turn-based不授full-duplex，欠缺“输出流占用时关键首词的表示切换/触发短干预”这一具体诊断。拟2604-17358第二完整marker后/“说话者、时间和词内容也可以分别生产…”前两段，不重复Ch66通用时延score。
- **唯一拟稿，待reader necessary/owner/PRE：**

完整turn的角色辨别还不能保证模型一边发声一边接住新输入的首个语义单位。对双流语音模型，可分别读出hidden对user后续codec与model输出的亲和，再用关键主体一开始就出现的打断问题，分报完整回答正确性和主体是否显式进入回答。内部读出是诊断proxy，主体出现也不是“确实听见”的因果证明；此前是否诱导模型持续说话会同时改变上下文与声学状态，不能据两组差额把所有失败唯一归于状态切换惯性。

[受限双工干预](https://arxiv.org/html/2606.11386v1)在检测到输入onset后短暂注入perception方向，可恢复部分首词与回答表现，却未消除错误；延长注入或误触发会退步，带filler的普通打断分数也可能掩盖首词压力。向量制备、层/强度选择、持续双流推理、触发器与ASR/judge回归均付费，免finetune不签实际尾延迟；触发、声学或质量支持不稳时保原声、明确等待/重述或半双工路径，不把合成短问题和一次内部恢复扩成连续监听安全。

## 11889 — Task-Aligned Stability

- [exact-v1](https://arxiv.org/html/2606.11889v1)实际§2–4/AppA与Table1–2/Fig3–5直接反侧；保原5=2+1+2。冻结normalized CLIP，用hazard prototypes maxcos−normal prototypes maxcos定义margin，阈值0；embedding L2 drift、abs margin drift与sign flips分账。同一输入corruptions可在全表示几何相近而任务读出翻转，新增具体判别边界，不授真实hazard truth/自动驾驶安全。
- 2k BDD100K validation图×7corruptions×5severity；prototype AppA为6hazard/5normal短文本，具体CLIPcheckpoint/size未披露。表FPR/FNR是clean自身判定到corrupt判定的方向性flips且以全人口计，不是真实ground-truth类条件falsealarm/miss。腐蚀可真正移除语义，不能先授label-preserving。JPEG Spearman.711/occlusion.266，motionblurflip24.2/JPEG10.8只证明受测population/corruption依赖；重复severities非独立运行，CI构造/完整seed/硬件precision/SLO未披露。
- 固定argmax的Cauchy-Schwarz局部式不采用为全局诊断；author说argmax切换失bound并非必然：unit text下各max是1-Lipschitz，差全局2-Lipschitz是作者之外可推导界，**不把自己补的式反写作者证明或Books**。只采用empirical几何与task-readout分责，图示斜率不当certificate。全corruption制备、双编码/prototype/scoring、分方向核验及独立truth校验费保；未核代码/图像素/复现。
- **actual owner**：`PLATFORM-EVALUATION-SYSTEM` Ch66；实际读自报confidence/语义保持2507-06489完整段与前黑盒surrogate、后CarryOn。旧段说embedding阈值不能替标签，但未解释同表示几何变化与具体固定readout margin的失配/clean-relative flips分母。拟2507-06489独立marker后/“拒答还要沿同一问题的澄清轨迹验收…”前两段；不将驾驶应用重写为新传感器或Ch26安全。
- **唯一拟稿，待reader necessary/owner/PRE：**

固定encoder的鲁棒性还应把表示移动和任务读出移动分开测量：对同一输入保存clean/corrupted embedding，再冻结文本原型、max聚合和阈值，分别记录表示距离、任务margin差与判定翻转方向。几何移动大不一定穿过当前边界，移动小也可能翻转接近阈值的样本；因此单一embedding drift不能替具体consumer的稳定性，而较小margin drift同样不能证明输入语义或原判定正确。

[受限道路图像对照](https://arxiv.org/html/2606.11889v1)显示两种drift的关系随corruption变化，但其正负翻转相对于clean模型自身判定，不是独立标注的危险漏检或误报率；遮挡也未被证明保持原标签。corruption生成、全部编码/prototype评分与方向分账、真实标签和heldout校准均付费，相关性不授逐例保证；原型、阈值或语义支持失配时，保原输入/分项读出、独立人工或任务真值与Unknown，不由表示稳定或一个危险margin批准实际控制安全。

## 11568 — 4DP-QA（采用reader唯一首备§77，仅actual owner）

必要原件/直接反侧完整采用canonical§77，不第二Methods。原准入camera/object运动混杂不变，不因深入更改评分。实际读Ch23单次密集geometry15876、motion basis2509-05297整段及后共享mask读出23279；现有是consumer侧prior，未有固定query camera重投影提供对照监督的reference-frame资格。唯一owner `MULTIMODAL-REPRESENTATION` Ch23；拟2509-05297完整段marker后/共享视觉特征mask前。未迁Ch25 dynamics或宣称3D真值。

**唯一拟稿，待reader actualowner/PRE：**

监督中的运动标签也须先声明参考系：同一物体的3D轨迹，逐帧投影到移动camera会混入相机运动；固定query时刻的camera外参再投影，则得到另一份固定视角的2D轨迹。两者可作为互补tracking监督，帮助区分“画面中怎样移动”与“相对于指定视角怎样移动”，却不使后者自动成为完整3D运动、真实力或未来动力学。

[4DP-QA的有限对照](https://arxiv.org/html/2606.11568v1)在固定样本预算中以tracking替换部分QA，外部运动任务局部获益，普通QA和更高替换比例仍会退步；geometry分支在real人口反退，不能把合成收益或新增几何模块归为普遍因果。depth/camera/pose/segmentation、caption改写与阈值共同决定标签资格，heldout frames也不等独立video。全标注/重投影、encoder与适配训练及真实运动回归都付费；参考系、非刚体/微小运动或标签支持失配时保留原视图、显式camera信息与专用tracking核验，不由QA分数批准真实世界动态或几何安全。

## 11562 — GraphInfer-Bench（采用reader唯一首备§78，仅actual owner）

必要与直接Table6/N反侧采用canonical§78，不第二Methods。实际读Ch66 OrderProbe2601-08626整段及前语言-v-事实、后COHERENCE逐slot-v-bijection完整段；已有结构-v-解释分账，但没有图neighborhood集合任务相对node/path lookup的证据人口及label-format/extra-node分母。唯一owner `PLATFORM-EVALUATION-SYSTEM` Ch66；拟OrderProbe完整marker后/COHERENCE前两段，不复制Ch76检索实现。reader§87已就具体新增校准2+1+2=5，不由深读上调。

**唯一拟稿，待reader actualowner/PRE：**

图上的答案还应区分单节点可查、沿路径可取与必须汇聚邻域才能决定的对象。可以固定提供的局部图、节点字段和结构规则，分别测关系/主题、异常节点与分区，再把hard结构标签和自由解释的相似度分开；语言流畅或段落接近reference不能代替节点集合、分区或关系正确，额外虚构节点亦不能在取交集后静默消失。

[GraphInfer-Bench的受限比较](https://arxiv.org/html/2606.11562v1)支持这类任务分账，但只title可见、有限邻域与自动筛选共同限定人口；Table6也不支持“所有任务GNN皆优”的摘要泛化。label格式、parser失败和停止失败须保在各自分母，SFT/zero-shot/GNN的信息与训练预算差异不能归成唯一架构瓶颈。构图/筛选/人校、全部编码训练与hard/soft判分均付费；标签或可见性不稳时保原图、简单node/path基线与独立结构oracle，不由相似解释或跨任务均分批准通用图推理。

## 11559 — HERO（采用reader唯一首备§79，仅actual owner）

完整必要/直接反侧采用canonical§79，不第二Methods。实际读Ch29 privileged-selfteacher18734整段、CREDIT11613与OPRD21496局部reminder完整段及GUI-SD下侧。OPRD只reminder寿命，未有完整终局future压为当前turn诊断、以next observation对齐后对原action重评分的训练接口。唯一owner `TRAIN-SFT` Ch29；拟OPRD21496独立marker后/GUI-SD前两段，不重复Ch80运行reflection。reader§88已就具体新增校准2+2+2=6，不由深入加分。

**唯一拟稿，待reader actualowner/PRE：**

多turn的privileged反馈还须与原decision context对齐，而不把整段成功后续或终局评价直接塞给每一步。可在rollout结束后读取完整interaction，将其压成逐turn诊断，再让selfteacher只在原context与对应next observation、局部hint下为原action tokens提供分布监督；部署student不读取这些future信息。压短改变监督接口，不消除privilege，也不使诊断文字、JSON confidence或无符号分布差成为真实因果credit。

[HERO的有限环境对照](https://arxiv.org/html/2606.11559v1)支持局部hint分支，人审却发现hindsight泄漏、错误归因和不可用动作；mean@4不是pass@4或在线成功保证，旧能力亦有局部退步。不同rollout数、学习率与反思/EMA开销不构成总预算匹配，较少更新墙钟不能代签完整训练省费。全部环境轨迹、反思制备、双路评分/更新、人审和旧任务回归均付费；hint、动作资格或保持能力失配时保留可信next observation、普通蒸馏/verified targets与原policy，不由自教名称签零外部信息或安全改进。

## 11521 — Counterexample Guided Learning（采用reader唯一首备§80，仅actual owner）

必要/直接反侧采用canonical§80，不第二Methods。实际读Ch80规则发现02485两完整段、主动程序分裂15669整段与CoSPlay双池两段。旧接口靠sampled input/代理expected labels，未有已知regex target DFA对称差→全称symbolic cluster、RepairScore与外部Equiv分责。唯一owner `AGENT-REFLECTION` Ch80；拟02485完整marker后/主动分裂15669前两段，不扩形式化验证主线或普遍CEGIS完备。reader§89已就具体新增校准2+2+2=6，不因必要投入改变。

**唯一拟稿，待reader actualowner/PRE：**

目标规则本来已知且可编成DFA时，反例可以由candidate与target的对称差产生，而不是让模型猜哪条测试最能区分假设。把相同automaton转移上的字符合成class，再将有限接受路径组织为symbolic counterexample clusters，可一次表达一组需共同满足的positive/negative约束；cluster的全称语义不同于多给几条随机样本，也不等已枚举无限语言差集。

[有限regex归纳对照](https://arxiv.org/html/2606.11521v1)仍把compile、已见例满足与外部language equivalence分开，repair的代理最高分或重试耗尽不授等价。cluster/path展开、字符串长度及retry预算有限，简单Single分支还可更token高效，反思/regularization也非全部必要；不把局部算法记号补成普遍可执行或完备recipe。候选生成、DFA/反例构造、全部修复和独立判等都付费；目标语法、oracle或预算不支持时保原witness、可信固定测试和Unknown，不让reflection自行认证正确性或真实程序安全。
