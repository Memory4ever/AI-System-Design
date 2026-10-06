# 本日增量证据笔记（持续整理，非完成验收）

补窗2026-03-09 BJT；只对72题摘冻结集合中的48候选作必要证据。全部为作者精确v1结果，未复现/核执行实现。root已完整72题摘准入并定点校准10 EX；这里逐项保存实际正文位置、采用边界及Books PRE，不另授日级Gate。全部48项作者必要机制/评价/直接反侧审阅已齐。初稿中的“待PRE/待最后核/待保存”保留过程语义，以每项下方实际结果及独立复核为准：实际Books逐项比较见[supplement-books-pre](supplement-books-pre-20261009.md)。只有原证/采用命题未变化的结果可复用；全部48必要Source/PRE采用界限已由root及review_mar10_remaining实际独核；四项整合POST通过，候选侧可执行0，只有六部分DAY/最终检查待验，不授增量完成，不是外部hold。


## FlashPrefill — 2603.06199v1

6=2+2+2；标准审阅。已实读§3.1/3.2/3.4、§4 baseline与InfiniteBench/RULER、TTFT、threshold ablation、AppendixA；同目录supplement-evidence-core-flash-20261009.json。原始平均pool-key score的AM–GM为真贡献下界，跨block排序依赖低intrablock variance；不是普遍严格保序。fused tile reductions/global normalization降低discovery workspace，max-relative alpha省score排序但保留indices compaction/稀疏kernel成本。保留sink256/local512、block128，alpha按4K约70%密度校准，不能作为全模型default。H20/FlashAttention2.8.3 baseline；Table3 Llama均分48.39→46.32、Qwen3 37.83→36.23，故不称lossfree。128K vLLM TTFT3.02/2.45/5.02×与operator的16.87–22.67×分开，模型/长度绑定，batch/concurrency等没有直接披露不补造。§3.5 index jumping及Table4完整相关质量切片仍待最后定点核，不先授完成。
实际Books PRE：INFER-PREFILL Ch43正文95–150 approximate discovery/row-max与成本，182–209 pooledblock/错误budget、458–470具体W10原证，已承载本次稳定机制及fallback；不要求新写，不扩已完成Weekly研究。邻接Ch44起始decode状态读过。Books决定已有覆盖，root必要Source/PRE已通过；最后作者补读§3.5/Table4及threshold完整反侧已完成：index-driven jumping只免dense loop masked-block控制开销，仍需实际index/稀疏kernel；Llama64K84.93<86.29、Qwen3均92.68<93.28，不授无损。原待补读句保留为历史过程说明，不再是普通未读。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / INFER-PREFILL。Ch43 95–150、182–209、458–470：approximate discovery、row-max/pooled block 下界与选择费用。不是一般保序或无损。root 必要 Source/PRE 已通过；§3.5/T4 作者最后补读已完成。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## BoN — 2603.05739v1

7=3+1+3；深入审阅必要内容，理论不套性能实验模板。已实读§2.1–2.3、Thm3–5/Prop1、§4变分策略/Remark1、§5.1 proof decomposition、§7 limitations；supplement-evidence-core-bon-20261009.json。固定prompt可取外期望、i.i.d. πref、bounded rewards及π*≪πref；改变优化对象为相对于πref的pairwise win-rate，不把ordinal error当MSE，也不把win-rate归结为真实任务正确率。BoN upper是Nεpw×log与EM tailcoverage的tradeoff；Thm4对non-atomic πref的worst-case存在下界，只匹配到log而非每实例精确optimality。regularized top ceil(N/M) uniform、随机ties，需要调M，Thm5的EM+Mεpw+1/N上界可随N改善，不由该式独自保证所有实例观测win-rate严格单调；不授adaptive sampling、吞吐或生产安全。匹配下界和regularized proof与general comparator必要条件待定点读足。
实际Books PRE：MODEL-SAMPLING Ch20 §Parallel Sampling325–369明确coverage/selection和额外评分成本，缺目标对象改变如何影响最优性与pairwise error/coverage的边界。拟root窄写2段，独立source→owner证据通过后才进入Books；我不写共享Books，写后实际POST。

实际整合及非写入者POST（2026-10-09）：root写Ch20 Parallel Sampling coverage段后2段与末注；supplement_20260310独立顺读325–362完整局部前后与末注，回对精确v1 Thm4/5、§4/Remark1。采用目标对象改变、pairwise误差/尾部覆盖与M/N分离；最坏情形/非原子、有限样本及实际monotonic差异、完整费用与旧BoN/verifier路径均保留，POST通过。Books决定整合；不是DAY、未复现。

当前实际处置（覆盖初稿待PRE状态）：整合 / MODEL-SAMPLING。root 写 Ch20 Parallel Sampling 后两段与末注：win-rate 目标、pairwise error/coverage 与 M/N 分责；作者实际独立 POST 通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## NOBLE — 2603.06492v1

5=2+1+2；实际确认长期layer graph缺口，必要差额深入。已实读§3.1–3.4（架构/CosNet/LR/overhead）、§4.1–4.2、activation-depth ablation、§5 function smoothness与tradeoff、§6；supplement-evidence-core-noble-20261009.json。每个projection xW+b增加σ(xWdown)Wup，从pretraining起训练基座与支路且不能线性merge；不是冻结base的LoRA。作者OpenWebText250M/1.5B target-baseline-loss，8×H100/bf16/compile等条件；多参数和独立up/M LR缩放同时改变，不能把加速唯一归因cos symmetry。rank64–128 step额外6.8–11.5%、target-loss wallclock约1.17–1.21×限该预算；永久infer6–12%FLOP且未测完整serving。bounded cos output不约束learned frequency/gradient，sin有零导数，频率和symmetry解释为hypothesis。ViT同augmentation只有+0.11/+0.14pp、关Mixup top1总体约67而非74；不以较低trainloss建议关augmentation。scale最大1.5B与image tokenizer单一保留。
实际Books PRE：MODEL-TRANSFORMER-LAYER Ch17 residual38–74/layer186–211，Ch16开头linear/nonlinear、Ch30前125冻结低秩与参数/更新边界均实际读过，未承载永久低秩非线性projection分支。建议唯一owner Ch17并交接Ch30，不双写；root亲读后决定窄写/路径，我不写共享Books。

实际整合及非写入者POST（2026-10-09）：root写Ch17「为什么顺序是Attention再MLP」主流设计后2段与末注；supplement_20260310独立顺读165–215 residual例→主流block→新分支→Layer堆叠完整邻接与末注，回对精确v1架构/CosNet/LR/overhead、OpenWebText与ViT反侧/限制。不可线性merge、永久推理成本、step与wallclock、augmentation与频率/梯度不保证均近文，唯一Ch17 owner与Ch30 handoff一致，POST通过。Books决定整合；不是DAY、未复现。

当前实际处置（覆盖初稿待PRE状态）：整合 / MODEL-TRANSFORMER-LAYER。root 写 Ch17 184–186 与末注：不可 merge 的永久低秩非线性支路/训练与部署代价；作者独立 POST 通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## BRTR — 2603.06503v1

5=2+1+2；标准必要core已读并保存supplement-admission-core-brtr-20261009.json：§3.1/3.2.2/3.3、§4.4/4.5。同ClaudeOpus4.6/50任务FINCH subset/工具+hybridretrieval，对比planner+specializedcontext与monolithic保留iterative loop的NoPlanner；88vs68%，312Kvs521K token、248svs175s latency。少token≠少latency的新受限复现有价值，不能以“成熟组合”关闭；分解与专用context共同变化，不独立归因planner。subset含全部6个失败任务、类别分布±4%；不是随机广泛generalization。FullContext20%本来无文件/超window、NoLoop不回传outputs的0%，不可代替NoPlanner有效反侧。多模型领先/production caching宣称不采用。
Books拟已有覆盖，但尚待actual Ch81/Ch75相应论点和邻接读取，当前不是Books完成。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / AGENT-CONTEXT。Ch75 38–72、244–282：capacity、程序化回读/子调用与 compressor+target 总时延；Ch81 292–310 调度费用。少 token 不等少 latency 已承载。50subset 的两组件联合对照仅报告，不称 planner 单因果。 root实际必要Source/PRE已通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## R4T — 2603.06397v1

6=2+2+2；标准审阅，撤销原拟“通用推荐范围EX”：set-valued非可分目标经RL transducer→jointretrieval tensor蒸馏具有模型训练/部署替代。§2.1/2.2.1/2.3–2.5、§3.1/3.4与AppendixA实读，supplement-admission-core-r4t-20261009.json；AppendixF决定性implementation另实读待保存。OAR target来自库实际contentembeddings，WSCR用subqueryembeddings，行随机置换适应无序目标；nearestneighbor保证库对象身份不保证事实可信/证据支持。冻结embedding/retriever/database和显式reward是训练条件；库或embedding漂移需重新校准/再训，不宣布免更新。AppendixF “single pass”实际256-step SDE solver，maink10但trainL12，不写一次denoiserforward或把256采样费删掉。53.9M versus4B generator测fanout12–20×仅作者局部wallclock；测时hardware/precision Not Disclosed，F的训练TPUv6e不可补为测时硬件。前置RL、128 samples/query、10M diffusion steps均非免费，音乐库proprietary、judge质量及reference set非唯一gold限制。
Books实际差额/已有覆盖待Ch76/Ch24与邻接PRE，不先统一整合。

实际整合及非写入者POST（2026-10-09）：root写Ch76 setwise段后567/569两段及1342末注。supplement_20260310实际顺读549–577完整邻接与1337–1347末注，回对exact-v1 §2.3–2.5、3.1、3.4及Appendix A全部必要原证。采用固定retriever/database/reward→RL teacher→joint目标张量→diffusion→NN对象这一部署接口差额；联合采样非单denoiserforward、预付/漂移再验、局部计时非索引/reader/SLO、NN身份非事实支持均保留，旧query expansion/rerank/setwise路径仍合理，POST通过。不是DAY。

当前实际处置（覆盖初稿待PRE状态）：整合 / AGENT-RAG。root 写 Ch76 setwise段后567/569两段与1342末注：固定 retriever/库/reward→RL fan-out→joint target tensor→diffusion→NN对象部署接口。supplement_20260310实际顺读549–577完整邻接与1337–1347末注、回对§2.3–2.5/3.1/3.4/AppA全部必要原证，非写入者POST通过。迭代采样/预付/漂移再验和事实support边界保留，不授完整RAG加速。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Safer Reasoning Traces — 2603.05618v1

6=2+2+2；实际隐私约束反例必要内容深入。已实读§2.1–2.5、§3 leakage/budget/gatekeeper、Limitations，core-05618原文待保存。有限syntheticEnglish11PII、blackbox单轮prompt内token resurfacing；不涉及训练数据抽取、cross-user、隐式/释义泄露、隐藏CoT或无日志架构。plain直接请求PII vsCoT hijack+JSON同时改prompt，不能因果声称内在reasoning导致差额。不同gatekeeper按风险weightedF1/recall及目标模型排序不同，理论混合保护并未部署/验证，不授无漏检。
原文冲突：§3.2模型名单/Opus排除与后述Llama、2550总实验vs450/model、六PII又说五、§2.5 recall leaked/token和missed文字不能统一；不采用精确全局budget曲线与固定+34pp宣传为普遍机制。SPriV是泄露token/outputlength密度，长输出分母变化不等泄露概率变小。不同API/quantization Not Disclosed；单A100-80GB宣称全部open模型的精度/执行策略未核，不补造。当前可支持的是可见trace是额外观测泄露面与detector按对象验收，不是通用CoT危害定律。
实际Books PRE：PLATFORM-SECURITY Ch72 238–280 detector是目标分布/policy sensor、PII population风险，394–429 secret substrate/端到端observable flow/获授权final-tool-process trace分测与U/V预算均实读，已有正文具体承载此次可采用命题；不是仅因privacy主题相似。Ch66邻接行为Gate亦实际读。决定已有覆盖，无新安全保证写入；核心实验计数争议隔离，不采用正面隐私曲线。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / PLATFORM-SECURITY。Ch72 238–280、394–429：detector 是分布/policy sensor，final/tool/获授权 process trace 分测及 U/V 预算。root 已核必要 Source/PRE；计数与曲线争议不采用。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Sparse Crosscoders — 2603.05805v1

5=2+1+2；标准必要core实际§2.2/3/4/5，core-05805保存（§2.2补片待保存）。等active参数的5layer dense/MoE、~1Btokens三域各1/3、2epochs，读layer3；比较的是诊断器所发现feature而非模型事实容量。标准crosscoder norm差把cos≈0甚至−1 features归shared，既有λs/λf=.1–.2不迁移到独立训练结构，约.7才能改善reconstruction；sharedfeatures显式tie后cos≈1有设计性，不能作为独立语义验证。FVE≈87%不证monosemantic/causal；910MoE-only/3226dense-only/18940shared是阈值/字典条件的计数，不证MoE更“专注”定律，作者无qualitative semantic验证且非trimodal。局部诊断迁移失效证据值得保留，若core后的无新设计条件EX不可用已有Books或小模型理由替代。
实际Books PRE：PLATFORM-EVALUATION-SYSTEM Ch66 256–284内部解释测量合同→跨模型字典分区/共享偏置/假阳性→独立行为steering验证，当前论点实际承载诊断器迁移失配与representation exclusivity不认证概念唯一；决定已有覆盖。MODEL-MOE不因词中MoE取得本项诊断owner。不将摘要“MoE特殊/集中”的解释写成已证。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / PLATFORM-EVALUATION-SYSTEM。Ch66 256–284：跨模型重建偏置、字典分区/假阳性与独立 steering，exclusive 不等概念唯一。root 已核 Source/PRE。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Moral Scaffolding — 2603.05651v1

5=2+1+2；标准必要§3.2/3.3/3.3.1/3.3.3、§4/4.1/4.3/5实际读完，core-05651保存。2939 AITA与四API/open指令模型，T=.4；200例15次baseline的runs2–15 entropy对held-out run1 flips避免同样本直接泄漏，仍是局部关联而非内在道德因果。1200 protocol实例按GPT4.1 run1标签分层，100 baseline文本×4model中结构化protocol pairwise flips22.8/22.5/28.0%，比免费输出映射更可靠；open-advice由GPT4.1-mini映射五类，人类κ=.57、二类κ=.76，所以不把51–55%全作为纯协议效应。内容改写100审计94%全部检查通过，point-of-view可能改变agency/intent salience，不能声称所有改写严格保持道德事实。有限ontology、temperature、四模型和generator文风限制；不把解释文风当真实内部reasoning。可采用协议身份是评价对象组成部分的局部复现；实际Books PRE：PLATFORM-EVALUATION-SYSTEM Ch66 285–313完整adapter/serialization/retry/stop/environment/scorer身份及338–356固定答案prompt扰动的judge测量漂移/人工anchor，与前后邻接实读，已有正文承载受限protocol-bound评价结论；决定已有覆盖，不追加案例名单、不授道德安全定律。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / PLATFORM-EVALUATION-SYSTEM。Ch66 285–313、338–356：adapter/serialization/retry/environment/scorer 与固定答案 judge prompt 漂移/人工 anchor，协议不等模型内在道德。root 已核 Source/PRE。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Structured Tensor Transformer — 2603.05727v1

5=2+1+2；标准必要§5.1/5.2/谱attention、Thm19/Norm remark、§5.11/5.13/FLOPs-vs-wall、§6.2/6.3/6.5/6.6实际读完，core-05727保存。将embedding feature划p片，DCT-II正交变换后各片width d/p标准attention/FFN，再逆变换；不是沿序列降复杂度，T²d仍在。只核心slice-wise等价，原域slice Norm非线性使全层不严格谱可分；不能照录§5.11的完整compact-transformer等价或仅由逆/正变换就证明跨片交互。PM baseline是1完整width层vs4窄片层，改变深度/图，局部容量取舍不是单变量DCT因果。IMDB/AGNews从scratch4层三seed，width768不等于预训练BERT；T4单GPU mixed precision具体dtype未披露，T128、train/infer batch128/256或64/128。窄width128/256训练慢约30%，width768才257→241s、1.95→1.66GB；encoder 4×参数减少但总模型51.4→30.2M，不能声称完整4×压缩/服务4×加速。具体Books处置待Ch14/17已有结构化projection与预算论点PRE。

当前实际处置（覆盖初稿待PRE状态）：仅报告 / MODEL-TRANSFORMER-LAYER。Ch17 74–112 Norm 跨 hidden dimensions/位置与变换责任；14 108–135 完整 attention 读取。DCT feature slices、窄分支/深度共同变化是此结构分支的有限预算对照；没有证明全 Norm 层谱可分或普遍 Transformer 等价，不将具体模块写为新稳定默认。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Knowing without Acting — 2603.05773v1

6=2+2+2；真实白盒安全边界必要深入。§3.1–3.4、§4.1–4.4.2/限制及AppC implementation实际读完，core-05773与extra保存。Llama3.1-8B/Mistral7B/Qwen2.5-7B，harm/benign canonical/masked四状态、Sahara选heads、双差logistic probe与动态steering；40train/10val/50heldout，AmbiguityBench100完全训练外。可支持两提取方向行为影响不同与拒答/有害识别不能等同的受限干预，不证“pure”独立轴：加性分解是postulate，共同bias不数学保证logistic w与artifact正交，masked head也可能改别的功能。注入/减向量改变行为不单独证明必要/充分或普遍唯一bottleneck，词表投影不验证认知语义。Llama benignRR96/64而Mistral42/6/Qwen18/28，强模型/数据差异；Table4/5多处REA低于静态或joint，不照录universallySOTA/全oversteering避免。LlamaGuard3判断、openweight白盒text-only，hardware/precision/采样详细运行Not Disclosed；不扩为黑盒API漏洞或生产安全保证。Books必要MODEL-TRANSFORMER-LAYER/PLATFORM-SECURITY已有拒答读取与外验收论点待PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MODEL-TRANSFORMER-LAYER。Ch17 395–406 readout、minimal pair、patching、weight revision/utility 外验；Ch72 588–603 refusal 管理访问不等消除能力。受限方向干预不签独立/唯一 harm-refusal 内因。 root实际必要Source/PRE已通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## RouteGoT — 2603.05818v1

6=2+2+2；标准必要§3.2–3.5、§4.1/4.2/4.3/4.6及AppB.1/C.1/C.4实际读完，core-05818与extra保存。三action绑定4B direct/8B CoT/30B decomposition，success与ordinal最低成功cost分位数训练分开，训练all-fail不拟budget阈值；decomposition cost含完整下游graph。推理估计cost mask、reserve synthesis、深/宽限、先付plan后预测超限转SolveWithPlan，是避免把每节点预算当全图费用保证的具体分支；UNSOLVED标记不证明合成不幻觉。20k离线训练三策略全部运行计费，迁移到中间节点未有真值，static cost estimate与正文在线median口径不能混成精确cost oracle。GPQA198与QA每域100固定seed，无外部retrieval，Qwen30B自己blind judge非独立事实oracle；4×A6000，30B TP2/其余各1GPU驻留，precision/concurrency/SLO Not Disclosed。w/o ordinal regressor在MoreHop78高于full77、full QA几处比RTR更慢；输出token省不等总tokens/延迟，input表也实际读过。采用ordinal budget与plan fallback局部成立条件，不采用严格budget/safety或普遍Pareto。具体Books差额待AGENT-PLANNING/CONTEXT现文PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / AGENT-PLANNING。Ch79 191–230 搜索预算/训练 teacher 与 runtime controller、297–310 不确定性与实际费用、368–388 完整 verifier。ordinal 成功路径路由 recipe 和 QA full 更慢仅报告，不将 all-fail 删除后的 proxy 当部署质量保证。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Many-Shot Prompting — 2603.05829v1

5=2+1+2；§3/4.1–4.5/5必要core实际读完，core-05829保存，AppA.2/A.3/A.5/A.6已实读并存extra；max5390 demos/128K、MiniLM384同文本余弦排序、labelwise balance特定分类假设；GPQA教师+verifier生成133/198 traces的训练/评价隔离不清，不采用该GPQA scaling。固定总N比较balance/random/similarity，Banking77 n是每类shot而N=n×77；十次order随机化仍2–3pp变动。similarity小N强、N扩大退而random更稳是局部选择条件，不以更多context线性提升；70B/8B来自不同Llama代不能把全部差额因果归model capacity。GPQA CoT4例后饱和的注意力解释为作者hypothesis，非内部因果；开放/结构任务若采用具体差额还需A7评价对象。不把prompt update说成权重训练，不授deployment可靠性。Books待AGENT-PROMPT/CONTEXT相应已有论点实际PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / AGENT-PROMPT。Ch74 67–94 示例质量/覆盖/顺序，Ch75 38–72、244–282 容量与前置成本；固定 N 选择/顺序边界。root Source/PRE 通过；GPQA test 生成/过滤不采用。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## CoCA — 2603.05881v1

6=2+2+2；标准必要§3.2/3.3、§4配置/主表/seq-vs-joint/segment反侧、AppB.1/B.3实际读完，core-05881与extra保存。confidence先于answer，rollout组正确率为当前policy目标，置信段与回答段各自标准化advantage联合更新；不是准确置信的真值标签。same-group estimate含自身、G小/稀疏reward噪声，外域校准不保证。Qwen2.5 1.5/3/7B只math RL训练，Ascend910B/C、max4096、T1、128×16；主比较1epoch，answer-first/segment对照.5epoch，sequential2epoch所以不能单独归因seq奖励调度。segment math accuracy49.90低于joint52.75，部分AUROC低于probe，不采全面优胜。TTC约10只到confidence前token而非完整回答/servinglatency；没有routing/early-stop实际闭环验证，hardware精度与concurrency/SLO Not Disclosed，未复现。Books待TRAIN-GRPO/MODEL-SAMPLING已有credit-mask/校准论点PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / TRAIN-GRPO。Ch33 369–387 prefix confidence/scorer 与 outcome/update 目标分责，802–855 segment credit 边界，870–904 reward 测量身份。Brier segment 配方局部评价保留，不由自采 target 授独立正确率/因果 credit。 root实际必要Source/PRE已通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## FPGA Gated DeltaNet — 2603.05931v1

6=2+2+2；标准及物理实现反侧受影响内容深入，IV-A–D、V-A、VI-A–E实际读完，core-05931保存。单Qwen3Next-style GDN层32 FP32 128²状态2MB常驻BRAM，代数重排把updated-state输出改为old-state双乘+rank1 correction、1read/1write，GVA两valuehead共享q/k但各自state；输入/host AXI和prepare/compute/store仍付费。U55C/HLS2025.1，H100PCIe官方PyTorch recurrence batch1/1000 warmup calls不是最优fused CUDA。最好Hiter8只HLS综合周期×目标clock，Hiter4实际routing失败88725signals，只有Hiter2 P&R263MHz；不能把4.5×或全部设计说实测可部署。GPU350W TDP vs FPGA9.96W Vivado片上估算分母不一致，62×能效不是实测。可采用容量足够时状态驻片/流水与物理routing才决定可交付并行度的受限反例；不把GPU必每token HBM roundtrip或无cross-headparallel当定律，不授完整LLM/SLO。Books待MODEL-LONG-CONTEXT/INFER-GPU-MEMORY具体正文PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / INFER-GPU-MEMORY。Ch22 460–560 GDN 状态数学；Ch54 16–35、120–142、488–550 片上减少物化/HBM往返、真实生命周期与 hardware verification。root Source/PRE 通过，特定 FPGA layout/P&R 与估算数字仅报告。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Omni-Masked Gradient Descent — 2603.05960v1

5=2+1+2；标准必要§3/4 assumptions/lemma/Thm4.6/4.8/Prop4.9、§5.4/5.5、layerwise algorithm与AppB.4实际读完，core-05960与extra保存。有限ERM mask×sample无放回全遍历、mask sum=M1和反比例gradient scale使cycle balanced，不是每步conditional unbiased。L-smooth、noise bound、固定有限N/M及PL另条件；O(ε^-3)/PL Otilde(ε^-1)不覆盖AdamW LM。LISA-wor周期middlelayers不重选、embedding/head常活且scale NL/γ，实践AdamW与完整mask-sample随机遍历/理论SGD不同；Algorithm2剩余pool<γ即reset，不能不条件称每坐标等次。GPT2-124M/OpenWebText1024、100ksteps；memory切片Llama7B/C4/RTXPro6000、micro16×accum32。19.56GB是LISA与wor共享的局部内存，而非wor独有70%收益；switch K太小能退，不采largestγ普遍最优。Books待TRAIN-PRETRAINING/机制现文PRE，不请求证明全文或生产保证。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / TRAIN-PRETRAINING。Ch28 298–336、512–545 活跃更新/optimizer state，800–915 layer LR 非活跃集合；Ch30 149–175 轮换原参数层/历史 optimizer 驻留。只采更新顺序/coverage 的条件分支；root Source/PRE 通过，不授逐步无偏/AdamW LM 理论率。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## EvoESAP — 2603.06003v1

5=2+1+2；标准必要§3.2/3.3/3.4及§4.1–4.3实际读完，core-06003保存。固定within-layer expert importance order，整数跨层预算level-switch保持总B；fitness是固定teacher-forced answercontexts全词表min(p,q)=1-TV，不是在线speculative acceptance或正确率。OLMoE/ERNIE/Qwen3 7–30B、同1024code calibration/64math search、seed42、P32/elites4与model-specific50/20/10代搜索，bf16/L40S；前置search5–5.8h继续计费。REAP Qwen25%搜索反退code−4.9pp/MC−4.1pp，WildBench多处退；不授统一generation保持或全任务增强。SPEC-DEC29.49h2GPU vs ESAP1.64h1GPU硬件和执行protocol不同，18×不当同预算服务提速；统计多seed/SLO/concurrency未披露。主张只采用allocation与selection独立轴及固定prefix proxy边界，Books待MODEL-MOE/INFER-TENSORRT-LLM实际已有论点PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MODEL-MOE。Ch21 600–640 layer budget、离线 contribution/teacher 特定校准；Ch49 780–817 执行状态费用。层内排序与跨层预算分责已承载。固定 teacher-forced overlap/搜索仅报告，非 online acceptance，反退和不同 GPU 费用保留。 root实际必要Source/PRE已通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## SmartCrop — 2603.06123v1

5=2+1+2；标准必要§3/4与Table1/2、δ/随机canvascontrol、§5/6/7实际读完，core-06123保存。一次完整forward后由EOS logits product-survival给截断proposal、后续crop canvas；product边缘概率需要独立/条件hazard才能成为真CDF，原文未证，只采用启发式阈值而非校准置信bound。唯一LLaDA8B/EOS-padding四Englishbench，无外推omittedEOS模型；T=Lnew或QA64，crop同时改变每stepunmask密度，QA ROUGE与长度敏感，不能将变化独立归因隐藏length awareness。τ=.99 HumanEval .4592→.4106、全部GSM切片略低，不称free/lossless；δ过crop20%后骤退，batch长度异质需额外enginegroup/padding。只给FLOPs估算、未披露完整wallclock/precision/hardware/concurrency/SLO，不采98%为真实服务收益或统一compute-saving。Books待MULTIMODAL-GENERATIVE-PARADIGMS/INFER-DECODE canvas/EOS责任具体PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS。Ch24 1778–1807 长度 admission、画布坐标、EOS/VOID 与 commit/质量分责；首 full pass 代理/τ recipe 仅报告。root Source/PRE 通过，FLOPs 非 wall-clock。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Partial Policy Gradients — 2603.06138v1

5=2+1+2；标准并理论中心冲突定点深入§2/3、Lemma1–3、greedy/K-horizon、§5及AppA.2 Thm4/5证明/AppF，core-06138与extra保存。截断credit未来奖励范围可改变优化的条件目标；offline无importance weighting是logged-policy rewardweightedlog surrogate，不声称无偏onlinePG。固定n、非负可prefix因果分解reward必要；lemma1把任意非monotone f取prefix max会改变终值，不可称WLOG保原reward。Thm5采用独立trajectories、bounded reward×score坐标及相关项绝对值和给最坏Hoeffding上界，subset只改善该upperbound，不证实际方差/速率普遍更快（可能项相消）。ConsistentLLMs每域6500 trajectories/5200train/1300test，two8B/3epochs/4096/bf16 A100FSDP，GPT4omini evaluator与Llama70B模拟环境；局部reward horizon随数据/领域改变，greedy Qwen教育rollout低于base，fullPG therapy也能退，不采用universal胜PPO。实际依赖回报不由人为截断变独立；centertheory强断言争议已报root，候选保留有限credit-scope/step-vs-rollout边界，Books暂不正面采用该定理，具体PRE待TRAIN-PPO/AGENT-PLANNING。

当前实际处置（覆盖初稿待PRE状态）：暂缓强理论 / TRAIN-GRPO。Ch33 369–387/802–855 前缀估计与分段监督不能自授终局等价。prefix max 改终值、未校正离线 ρ/actual variance 强 claim 争议隔离；窄 shaping recipe 仅报告。需原作者明确目标/采样校正才能重开，不跑代码绕公式冲突。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## SPOT — 2603.06222v1

6=2+2+2；标准及中心alignment归因争议定点深入§2.2/3/4必要主表/消融/limits、AppA.5/A.7，core-06222与extra保存。随机.3 spanDrop替换单pause，head/embedding冻结作softexpected-embedding投影，pause CE masked；RFT多插入pattern选正确最短后只放开pause embedding，推理仍外部spanschedule、非自行决定emit。单student support、uniform teacher marginals下OT唯一plan固定，Eq4普通entropic OT（非debiased Sinkhorndivergence）平方距离mean=sumdist/n=到teachermean的MSE+constant；所谓更丰富tokenstructure与pooledMSE优胜归因未建立，AppA.5 normalize/numericalsolver可能改其他条件不能无证补因。该中心争议报root；可采用冻结接口/外插pause/RFT稳定具体分支，不采用OT独有语义/内部reasoning解释。DeepSeekR1DistillQwen7B/LoRA64、2RTX5880/bf16/train4096、10decode seedsT.6/p.95/max16384；AIME2024仍退，G2/3更短但损准确，teacher/RFT候选费用继续计。只输出token长度无完整latency/servingSLO；LLMjudge只邻接连续性/未显式bridge且允许triviallyinferable，不验证latent实际计算。Books中心暂缓与有限机制已有覆盖需MODEL-SAMPLING/AGENT-CONTEXT实际PRE。

当前实际处置（覆盖初稿待PRE状态）：暂缓强归因 / MULTIMODAL-GENERATIVE-PARADIGMS。Ch24 1278–1300 冻结表示与迁移上限、Ch23 653–669 对齐不等几何真值。理想 fixed ε/marginal 下 OT 退为 mean φ(h) 的推导由我们给出，不授额外 token 结构；pause+mapping 窄分支仅报告。root 必要公式独核通过，需作者解释 pooling/归一/ε/数值差额。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## ROSE — 2603.05878v1

5=2+1+2；§4.1/4.2/5.1/5.3/5.4/5.5实际读完，core-05878保存。SparseGPT逐序补偿随未剪权重减少，用初始Wanda估候选loss、block/column重排让高估误差先剪；只在loss相对range>.5的columnar层，保持block-masking与恢复排列。80%权重变化<30%为观察而非mask不变证明；pseudo-preprune不能知道补偿后的精确最终mask。128 C4×2048、block128、Llama2/3/Mistral7–70B，Llama3-8B60%与Mistral80%PPL有退步，70%损失仍远于dense，不能称无损。模型剪枝时间4.76→5.15/8.45→9.34min，离线重排不删除前置费用；2:4CUTLASS推理ROSE1450 vsSparseGPT1458几乎一致，未披露测时长度/batch/concurrency/precision/SLO，不采为完整服务新加速。作者称48GB4090，硬件报告无法当标准规格/真实性独立核验；无实现执行。AppB完整算法已实读并存alg，X列匹配置换与最后W还原支持部署无需新增permute；Books待INFER-TENSORRT-LLM具体pruning现文PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / INFER-TENSORRT-LLM。Ch49 505–517 稀疏 artifact、局部重构/真实 kernel admission，2183–2199 更新顺序与误差度量分责。两级大误差优先剪枝是局部新 recipe，仅报告；不迁移量化 fixed-order 等价证明。root Source/PRE 通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Entropy-Based Uncertainty RL — 2603.06317v1

5=2+1+2；§2.1/2.2/3/4、AppA.1–A.3实际读完，core-06317与extra保存。固定base多次T1生成的kernel vonNeumann entropy，经held-out correctness Platt映射作为target，再训练独立LoRA uncertainty阶段，answer先生成后冻结；回答不变来自执行隔离，不是LoRA普遍防遗忘证明。reward=1−max(.05,abs(pred−target))在小误差有平台。Qwen2.5-7B，TriviaQA/NQ18000训练/2000heldout，H200NVL一张10–14h/GRPO1000steps/32×16/T1.5/LoRA16；答案T.1、GPT4omini labels。ID/OOD ECE较Brier好但AUROC81.53<83.36/66.73<66.89，Spearman仅拟合teacher calibration target；Platt具体校准split与GSM8K适配未说明，不能据局部ECE授普遍跨分布可靠性。precision/最大生成预算/concurrency/SLO未披露，多样本生成/embedding/标签/校准前置成本不删。Books待MODEL-SAMPLING/TRAIN-GRPO校准对象与answer隔离具体PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / PLATFORM-EVALUATION-SYSTEM。Ch66 723–738 evolving uncertainty sensor 与独立 correctness、Ch33 369–387 prefix BCE/relative margin 目标不同；VN entropy→Platt→confidence LoRA recipe 仅报告，低 ECE 不认证 Brier/AUROC/OOD 每实例。 root实际必要Source/PRE已通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Gradient-Flow Softmax Polarization — 2603.06248v1

5=2+1+2；§2/3.1 assumptions/Thm3.2/3.3/3.2 regression/limits、§4.1 pretrained/4.2，决定冲突的AppB logistic gradient与no-crossing proof实际读完，core-06248与extra保存。不遍历其他proof。独立可训练V与a、uniform a0、strict projection order、aligned target/gflow是stylized假设，regression还须rank-one/zero V0，非Transformer一般训练定律。正文Eq6/7和AppB Eq15/16打印−γ，而AppB前面的dV/da/du与实际no-crossing proof使用+γ；我们由loss链式法则推导亦应+γ。正文任意i≠j gap同时增大不成立，proof末段限定i<j；保留原文冲突，不静默替作者修定理。可支持参数化/优化选择改变注意力稀疏性的受限观察，而非全部attention sink唯一成因。7B softmax/sigmoid同预算forward Pile的max-logit mass是诊断量，不等输出重要性；toy单token扰动效果在多head/layer消退，不授生产robustness。强理论采用争议隔离，Books有限机制待MODEL-SELF-ATTENTION实际PRE。

当前实际处置（覆盖初稿待PRE状态）：暂缓 / MODEL-SELF-ATTENTION。Eq6/7 与 Appendix15/16 符号冲突、pair 求和口径不一致；Ch14 108–135 attention 路由/Value 方向不等语义贡献可复用，但不能补其中心证明。需作者更正公式与适用条件。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Stem — 2603.06274v1

6=2+2+2；§2.1–2.3、§3.1–3.4必要对照/ablation/latency实际读完，core-06274保存。position-decay把预算向早query分配，value-norm OAM与QK粗block score组合、128block anti-diagonal/downsample/maxpool，再topk精算；初/local4块且最低54块。causal依赖拓扑只说明潜在传播路径，不证误差必放大；Eq5向量残差和可相消，个体贡献范数最大不是一般最优subset。Eq7截断与β.2、downsample不等Eq6 exact ranking，不能认证最优/无损。Qwen/Llama8B/H20/bf16/batch1/PyTorch/FA2，LongBench同近似总预算uniform→TPD→OAM局部收益成立，OAM若干子任务退；Qwen31.64/32.01、Llama41.48/42.02非lossfree。128K1540→420ms含90ms metric的局部prefill测量不等完整serving；完整coarse QK仍N²/B²且实际预算按N比例，不能照录严格全局linear complexity/2–3× memory。训练稀疏模型额外budget reduction保留模型特异条件，无concurrency/SLO。Books待INFER-PREFILL实际已有预算/score proxy论点PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / INFER-PREFILL。Ch14 123–135 mass、Value 尺度/方向/抵消与执行选择费用，Ch43 95–150/182–209 approximate selector/error budget。TPD/OAM proxy 与 anti-diagonal/minimum/sink recipe 仅报告，不授全模型最优或语义因果。 root实际必要Source/PRE已通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## MoEless — 2603.06350v1

6=2+2+2；§3.2/3.3/4.1–4.3/5/6.1/6.2/6.5/6.6实际读完，core-06350保存。batch层负载predictor复用/按layer target微调gate副本，预测前d层→memory-cap贪心replica→warm-start优先/least-load placement，非expert模块仍DP；预测错误不改变原router内容但影响资源性能。残差similarity不保证所有层/分布预测，d增大以accuracy换overlap；异步CUDA stream/keepalive不普遍保证零成本/无coldstart。Mixtral/Phi3.5/Scout、Azure token traces/LMSYS/ShareGPT、Megatron每秒聚批模拟非真正continuous batching；Oracle改路由影响质量，EPLB/Megatron比较层forward。reported43.19%/21.89%是层CDF聚合而非TTFT/TPOT/SLO；memory×latency cost proxy不可当92–95%真实账单/完整资源费用。三组件同时移除的ablation不独立证明各项因果。GPU/PCIe/NVlink叙述未独立核、不把A6000+PCIe5/8card pairwise规格当确认硬件；precision、并发、SLO Not Disclosed。全部replica权重/placement/前置calibration保留费用；Books待MODEL-MOE/INFER-SCHEDULING owner已有routing-vs-placement/资源执行论点PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / INFER-TENSORRT-LLM。Ch21 780–857 router 语义与 replicas/placement epoch，Ch49 696–780 前层预测 expert cohort→暖复制与 async 费用、正常 router 仍权威。采用的早预测分责有具体 coverage；CDF×latency 不签 SLO/账单。 root实际必要Source/PRE已通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## DC-DiT — 2603.06351v1

6=2+2+2；§3.1–3.5、§4.1–4.4及batched padding实际读完，core-06351与extra保存。P1 latent→full-grid conv encoder→2D neighborhood cos boundary/STE→compressed DiT→confidence Gaussian blend/nearest boundary plugback→full-grid decoder，保留original2D position与gated residual。ratio loss只是软平均目标，每batch向max保留数补入次高prob tokens，非所有sample硬compute cap；full-gridconv、pairwise retained-distance/smoothing与decode不免费。ImageNet256/VAE/class/1000trainnoise/250DDPM/FID50K，B138M/XL690M、400k×256AdamW/MI325X/MI300X，precision/实际throughput batch/concurrency/SLO未披露。isoparam DC FLOPs更高，isoflop匹配仍params不同；random boundary B4×16.69→13.51支持内容路由局部增量，recall数处略退。timestep emergent compression不证边界是语义gold。upcycle先前DiT7Msteps+5kactivationwarmup后50k不是从零12.5%总成本，naive20k FID184.74反侧明确。只采用2D chunk/plugback与conditioning freeze稳定边界；Books待MULTIMODAL-GENERATIVE-PARADIGMS实际PRE，不授通用更多token必优/服务加速。

实际整合及非写入者POST（2026-10-09）：root写Ch24全局patch段之后1274–1276两段及1859末注。supplement_20260310实际顺读1258–1285完整局部前后与1853–1864末注，回对精确v1 §3.1–3.5/4.1–4.4：2D encoder/router压缩、Gaussian/nearest plugback、完整grid residual/decoder、soft-ratio训练、所有路由/恢复/teacher费用、uniform/随机/冻结反侧及两模型条件均近文。confidence非objectboundary、预算非硬保证、teacher预付与旧全局patch/少步student边界保留，POST通过；root恢复后确认。不授DAY。

当前实际处置（覆盖初稿待PRE状态）：整合 / MULTIMODAL-GENERATIVE-PARADIGMS。root 已写 Ch24 1274–1276 全局 patch 段之后两段与1859末注；supplement_20260310非写入者实际顺读1258–1285完整邻接、1853–1864末注，回对§3.1–3.5/4.1–4.4必要原证，POST通过。非均匀2D grid→Gaussian/nearest plugback→fullgrid decoder/residual，软预算/全部费用/teacher条件与旧路径边界近文，不授DAY。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Multi-Constraint Adapter Bandits — 2603.06403v1

6=2+2+2；§2/3/Thm4.1/Remark4.2/§5，决定runtime/metric疑点的AppB/E及realizability条件实际读完，core-06403与extra保存。frozen multimodal repr+reward/cost heads，initial exploration/LP估dual radius，逐round多预算dual penalty+SquareCB-style选择，预算跨round耦合而非请求SLO。理论MLLM estimator sublinear regret明确open problem，不照录普遍√T保障。首CLS attention池化在标准causal Qwen执行中看不到后文；未披露改mask，故完整语义汇聚机制未核（我们条件推断，不称代码运行事实）。local latency Eq26=(Tin+Tout)/FLOPSdevice量纲不合，主文trace/E中simulation不能视为统一实测；ROUGE-L表[.15,3)与[.3,.4)重叠，1–5评分不证跨任务质量可比。实验只平均budget超限前executed rounds与目标total reward不同，5seed不消除此选择人口混杂。后台五模型/API、本地hardware/precision/运行预算和pooling实际路径Not Disclosed，中心保证不采用。Books暂缓中心机制/性能，需mask与CLS位置/实际runtime、dimension-consistent latency记录、reward映射及所有请求/拒绝/成本分母；有限dual/探索路径不另当新稳定recipe。root已收到具体争议，停止全proof/代码扩查。

当前实际处置（覆盖初稿待PRE状态）：暂缓 / MODEL-SAMPLING。cost/latency 单位、causal CLS 读取未来和 reward 区间口径冲突；Ch20 230–282 校准排序/预算不等 correctness 可复用，不补齐中心目标。需实际 mask/cost objective 原件。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## SpeakInContext — 2603.06505v1

5=2+1+2；§3.2–3.6/§4.1/4.2及context/CL/未见语言反侧/limits实际读完，core-06505保存。frozen WhisperTurbo+EuroLLM1.7B，只训downsample4/two-layer GELU connector，speech/context mean+L2 InfoNCE与CE加权；train context从gold转test CTC粗转写、hotwords+distractor训练词库，额外CTC完整成本不删。11语言1571h/1507train/32test、2epochs/batch8/beam2、history1/hotwords最多3×3、distractor1；硬件/precision/延迟/SLO未披露。context对若干语言退；CL/history平均15.42优于联合15.57、Portuguese historyCL32.09→36.66等反侧，不采总context更多就更好/普遍alignment提升。不同WER/CER算术平均不是共同token风险；联合信号竞争是作者hypothesis非证明，单数据/decoder未保证OOD。采用context来源/噪声与对齐任务匹配的窄选择条件；Books待MULTIMODAL-REPRESENTATION已有具体论点PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-REPRESENTATION。Ch23 518–546 input/训练/部署信息责任、653–669 对齐与原模态 evidence 分责、727–743 encoder/时间/provenance。speech-context contrastive connector 与 gold→CTC retrieval 迁移仅本配方，不授语音内容/对齐真值。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Safe-Night VLA — 2603.05754v1

6=2+2+2；真实物理安全约束必要深入，III-A–C/IV训练与三任务/V-A/B2/C实际读完，core-05754保存，硬件/总table与VI局部limitations已实际读extra：FrankaPanda/RealSense/Topdon224²，静态几何/精确state条件，动态障碍未验。thermal/depth pseudo-color+frozenGR00T RGB backbone，仅projector/DiT action训练；多模态观测、QP执行filter、任务完成分别验收。pointwise joint displacement QP λ正定不自动给予离散采样/误差下全局安全，min-distance h的平滑/不可行fallback未说明，不采用标题safety guarantee。600demos/5000steps/bf16/128effective，四modality独立重训同布局zero mask，低光是RGB亮度程序衰减非真实全夜场景。RGB-T normal部分优于full；镜像仅1step20cm方向openloop，blocked action记failed而非安全恢复成功；filter反复挡住但policy不lift/recenter是task failure。10episodeattention correlation .081不证热力学内部推理；模拟fixedwall/热源/浅埋特定条件，不授普遍机器人安全。Books待MULTIMODAL-EMBODIED-VLA实际对照PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-EMBODIED-VLA。Ch26 725–815 全感知/transfer/controller 链费用，882–965 safety envelope，1170–1226 sensor/projection/真实控制 guard。pseudo thermal/QP 局部机制保留，不授全局安全或 recover。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## EmboAlign — 2603.05757v1

6=2+2+2；III-A–D/IV-B/D/E及TableI–III实际读完，core-05757保存；任务/执行装置extra已实际读：六DobotNova2任务、10次各，初始视觉proposal不是feedback闭环。相同VLM keypoint functions作用于video candidates与retargettrajectory，先VJEPA预测discrepancy排序、逐个3D约束筛，再固定grasp/object rigidtransform/SLSQP软惩罚refine，是把video proposal与约束执行分离的具体分支。latent predictable≠物理可执行/事实，estimateddepth affine校准与tracking误差可放过坏proposal；firstthreshold pass不保证全部约束真值，softcost也非硬safety或无解fallback。六real任务各10次，相同LVP video→selection23.3→48.3→opt68.3%，支持两阶段局部改善但多个感知/初始化同时变化，不证明唯一causal机制。failure包含artifacts通过筛/错keypoint/depth/rigidretarget，不把单初始观察/openloop执行写闭环可靠性。原生ReKep/Novaflow与ablationcounts不同保留各自protocol。Books待MULTIMODAL-EMBODIED-VLA/WorldModel接口具体PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-EMBODIED-VLA。Ch26 882–965 imagined proposal/constraint/controller 分权、1170–1226 约束投影与独立动作验收。两次 VLM+retarget/SLSQP recipe 和 6×10 有限联合对照仅报告，非 soft target=hard physical safety。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## LIPAR — 2603.05811v1

6=2+2+2；§4.1–4.3/5.2–5.3/6.1–6.2/7.1–7.2/limits实际读完，core-05811保存。源video latent短/长时差定mask，少queries，恢复K/V从zero-noise clean cache而非重复带噪token，m最近RoPE旋转copy后复原fullgrid。clean-cache/bidirectionalcleancondition是成立条件，当前source-conditioned V2V不外推T2V。重复IID噪声确改变相关性，但linearized投影分析不证全部层的统一error；topm sum只是下界，最近位置不是一般最大RoPE exponent、无tailbound不授strict最优近似。固定72frame/480×832/RTXA6000十runs varyingkept线性回归≠全局O(n)证明/预先精确SLO。51video-text/fixed10/20/32%mergecontrol，32%12.2vs8.4FPS作者全pipeline局部，imgquality.676<.678dense不称无损；恢复/zero-noisestep/源video和短长motion检测费用保留。precision/batch/concurrency未披露，人类偏好只当前视频。Books待MULTIMODAL-GENERATIVE-PARADIGMS可重用状态与噪声身份实际PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS。Ch24 1302–1345 mutable denoising state 与 clean 条件、1350–1440 per-phase anchor/cache budget 与 refresh。clean zero-noise KV/近期 RoPE identity 采用范围具体覆盖，不授 exact/无限时长。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## HiLAM — 2603.05815v1

5=2+1+2；§3.1–3.3/4.1/4.2.1–4.2.3/5实际读完，core-05815保存。固定pretrainedIDM latentactions→HNet动态边界/层级chunk→nextlatent+FDMframe监督→stage2 skill展开每步；hierarchicalpolicy pretrain observation-only之后freezehigh-level、low-level用真动作finetune。latent重建与视觉chunk不自动证semantic skill/无监督可执行动作，actionlabels只pretrain舍弃不表示部署不需动作监督。Human/robot数据+100kpretrain/100kfinetune/BAKU/T5/UniSkill，LIBERO10tasks×50demo，humanstage2+rawlatent94对flat91；robot90与层级1相同，技能层并非普遍更深越优。10%demos45vs23只同局部数据，不把旧IDM/FDM/全部pretrain费用当免费；真实环境/safety尚未验证，hardware/precision/repeats/latency未披露。Books待MULTIMODAL-EMBODIED-VLA高低policy与latent action具体PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-EMBODIED-VLA。Ch26 135–153 high-level latent target→embodiment decoder/controller、1170–1226 latent 监督非可执行动作。freeze high/finetune low 条件分支及更深未更优仅报告，不授 observation-only 部署。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## AnyCamVLA — 2603.05868v1

6=2+2+2；III-A/B、IV-A1–4/IV-B1–3实际读完，core-05868保存。已知train/testcamera内外参与共同coordinate frame，feedforwardLVSM把当前view转训练view供frozenpolicy；不凭图像合成消除校准/遮挡/geometry误差。LIBERO sim需491scenes×64multiview对LVSM域适配，w/oFT33.2低于noadapt49，完整88.6仍低original92.4；冻结policy不是全pipeline免训练/全能力不变。OpenVLA/π.5两模型局部条件，不能任何RGB VLA/任意camera保证。RTX4090 BF16/256²两进两出36.55ms是adapter latency，不是零新增/全部robotloop。realFrankaPanda/ZED2/4tasks×20demos、π.5先LoRA10k，再unmodifiedLVSM换view10trials/task；handheldArUco只有suppvideoqualitative，不授动态pose错误鲁棒性。源/合成view、adapter训练、pipeline/controller预算另验。Books待MULTIMODAL-EMBODIED-VLA perceptionidentity/transfer分工实际PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-EMBODIED-VLA。Ch26 725–815 camera/coordinate/calibration、adapter费用与全 loop 验收。视图重绘 adapter→frozen policy 具体 recipe 留报告，sim 还要 LVSM FT、real policy 先 LoRA，不称任意 camera 免训练/安全。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## IGAR / ICBench — 2603.06001v1

6=2+2+2；评价反证/动作安全强断言必要深入，§3.1/3.2/4.1/4.2/5.1–5.6实际读完，core-06001保存。fixedscene配不满足的语言扰动，旧standard-task SR不代表遵从当前指令；LGS差值只是对扰动敏感，降低SR也可能genericdisruption，hover/emptygrasp不认证识别矛盾或安全abstain。30LIBEROtasks×50rollouts/3VLA，normalπ.5 Object98.4→94.4、SpatialV4contra97.6→99.6反升，不写uniform保留能力。spike/top5/τ20/γ3、visualsinkfraction≤.4选择、减textsink.6向non-sinktext比例分配；不能混写从visualsink直接转语言或attention因果。threshold在Goal搜索而统一本地部署不等未知分布无需校准。realFranka3/twoD435单cube图无trial数/风险budget；硬件precision/looplatency/concurrency未披露，白盒权重干预需独立效果验收。Books待MULTIMODAL-EMBODIED-VLA/PLATFORM-EVALUATION-SYSTEM区分语言遵从/任务完成已有正文PRE，强安全不进书。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-EMBODIED-VLA。Ch26 1170–1226 sensor敏感与controller guard、1350–1378 task/sensor attack 与 clean recovery；Ch66 285–313 评价对象身份。normal/contradictory instruction 分测已承载，LGS 敏感不是识别矛盾或安全 abstain。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## GenHOI — 2603.06048v1

5=2+1+2；§3.2/3.3.1/3.3.2/4.1–4.4/4.6实际读完，core-06048保存。reference/mask/noisylatent channel HCU、head-specific reference时间位置及token softgate是受限条件注入分工。RoPE score并非一般随距离单调下降，不采用普遍衰减解释。中心hardmask Eq8 M=0/1、Eq9 softmax(M⊙QK)只把blocked logit置0，exp0非0；按所列公式不阻断通道，不能认证zeroresponse/严格背景隔离；需真实−∞mask/执行材料才重开（我们代数推断，未核代码）。Wan14B/19kvideo/16H10080G/3days，additional157M不是证明训练只更新这157M；50self+50cross、81/401frames、30participant60videos有限评价。selfablationHSRoPE vsbbox有FVD/OC反侧、SAG两gate联合变化不独立硬mask收益；firstlastframe质量依赖生成器，非物理可执行。precision/采样步/全部延迟SLO未披露。Books中心严格隔离争议暂缓；有限多headreference位置/门控不单凭现配方进书。

当前实际处置（覆盖初稿待PRE状态）：暂缓 / MULTIMODAL-GENERATIVE-PARADIGMS。Ch14 132 binary multiply mask 不等−∞可见性、Ch24 79–81 区域编辑/decoder验收；中心 hard isolation 与 Eq8/9 冲突隔离，RoPE 非一般单调。需作者真实 mask/公式原件，窄 gating recipe 仅报告。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## RMD — 2603.06136v1

6=2+2+2；§3.1–3.4/4.1–4.5必要机制与noise/schedule反侧实际读完，core-06136保存。resolution-specific logSNR映射、fake-score分布matching、lowSNRwarmup与上采样再噪，是换分辨率时需重验noisestate的具体分支。scalarlogSNR相同不证fullstate distributions相同；α²+β²=1且predicted/upscaled noise不IID，不自动保Gaussian marginal。mainthreshold−2.5/Table4 vs正文default−5，step分配文字亦与table方向不一致，不采用统一recipe；centerconditional approximation明示非exacttrajectory/JointsKL证明。SDXL/PixArt/SD3.5/Wan14B，singleA100/512→1024或480→720，4或6step与teacher40/50×CFG不同费用对象；同4step2+2有1.56/1.68作者local值而非普遍33.4×。video82.51<83.75dense等反侧、3+1 HPS24.79大退、3stage最快HPS31.03<31.99，不授无损。teacher/fakescore/warmup预付和codec计费，precision/batch/video长度/concurrency/SLO未披露。Books待MULTIMODAL-GENERATIVE-PARADIGMS跨resolution state身份既有正文PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS。Ch24 939–1028 跨 resolution draft/semantic lock、1125–1345 noise/parameterization/solver/codec身份。logSNR state 切换分责已承载；fake score recipe、threshold 冲突与 teacher 费用仅报告，不授 full distribution match。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## WorldCache — 2603.06331v1

6=2+2+2；§4.1–4.3/5必要table，AppD.2/E.3 uniform/random/skip直接反侧实际读完，core-06331保存；AppendixA/C已实际读：只有ε对速度²可忽略或随scale²变化才保scale不变；A800/50prompt/40single+10three，warmup次数与batch/precision未披露。last3 FULL tokens算acceleration/velocity² proxy、按percentile stable reuse/linear extrapolate/chaotic smoothstep blend，再accumulated chaotic surrogate drift触FULL。这里cache drift不是观测真误差/physical world motion，“curvature”未投影法向不是真几何曲率；oldvelocityblend不普遍conservative/noovershoot。fixedε破精确scalerescaling不变，scalarfeature rescaling也不消modal-specificanisotropy/modelshift，不能用一个η签所有time/distribution。A800/13B-Voyager512×76849frames与5B-Aether480×72041frames，baseline超显存CPUoffload比较保留，WorldScore/pose部分低dense不称lossfree或端到端environmenttransition可信。uniformlinear PSNR18.01 vsreuse22.74、randomSSIM.710 vsheterogeneous.791支持局部分组选择；Nmax只在blend饱和而Algo1无单独forcedFULL cap，未授权精确skipping保证。完整cachedhistory/percentile/trigger开销与评测ND保留。Books待MULTIMODAL-GENERATIVE-PARADIGMS denoisingcache身份已有正文PRE，不因worldname改owner为world-state真值。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS。Ch24 1350–1440 FULL anchor/每chunk phase/累计displacement/proxy触发refresh、identity与全部费用。分组近似 proxy 非观测误差/物理曲率，scale条件与缺hard cap仅报告。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## PSIVG — 2603.06408v1

6=2+2+2；§3.1–3.3.1/4/5.1–5.3实际读完，core-06408保存。generatedtemplate→singleframe mesh/background4D/camera/两framevelocity→MPM初始化→前景simflow/背景templateflow→GwtF+test-timeprompt/feature modulation，TTCO用sim对应warpedfirstframe50iterations与早noise700–1000。materialqualitative→parameter映射由GPT5猜测、geometry/velocity不真值；sim-valid并不证真实物理属性/动作安全，foreground/backgroundhybridflow不可当完整simulatorstate。SAMmIoU/CorrMSE是对simulatorguidance的符合，32participant偏好不能代真实physicsgroundtruth。TTCO .009→.007/.93→.95局部收益，基础template/image/perception/sim/render/50opt/后generation全费；无新增数据不等无训练/免费。大rotation看不到firstpixels则用simrender，背景最小影响不是严格不变。硬件/precision/分辨率/样本数/端到端latency未披露，controls拿相同simcondition仍模型预算不同。Books待MULTIMODAL-WORLD-MODELS imaginedproposal与simulator验收接口具体PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-WORLD-MODELS。Ch25 1185–1223 Reason/Execute/Render 不同状态、1266–1272 veracity/influence/克制三证据；Ch26 882–965真实控制。simulator 合法/偏好非世界真值，hybridflow/TTCO recipe 留报告。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## WanderDream — 2603.06445v1

5=2+1+2；§3 数据/路径构建、§4 task/judge/realworld评价实际读完，core-06445保存。HM3D robot路径为Habitat shortestpath/5m，ScanNet++“human”路径是PRM/Dijkstra capsule/垂直罚的合成规则，不代表实际人类轨迹或物理控制。13,906 train/1882 val、21panorama、GPT5 phase QA与metadata/SoM，human80场景800QA审查只覆盖局部。real26videos/2scenes/182QA；groundtruth观察相对start的收益不等生成器创造可执行状态的因果收益。生成end/path在部分任务有效但start变差，MindJourney31.9<start38.5；real finetune43vsPE38.8不同处理，不合成普遍world imagination结论。judge1–5分×100不是binary accuracy，Spearman.9722只对应所列human800。每trajectory35–283s包含生成规划分支，hardware/precision/concurrency未披露。有限贡献是分开状态想象保真、观察相位与下游推理，不把视频变robot控制证据。Books待MULTIMODAL-WORLD-MODELS与evaluation邻接具体PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-WORLD-MODELS。Ch25 1185–1223 visual proxy非世界真值、1266–1272 状态真实性与下游决策效果分测。合成路径/GPT QA/real observation 相位只有限评价人口，不能将可视化认作真实可执行状态。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Diversity Visual Pruning for VLN — 2603.06480v1

5=2+1+2；§3 selection/history、§4 sim/ablation与§5 real部署实际读完，core-06480保存。CLS-cos salience与迭代novelty乘积、history maxcos currentselected加α.5/MMR是局部token选择，而非instruction因果显著性；空集合初始化细节未明，不授通用选序保证。StreamVLN R2R/RxR val-unseen以729/14672→218tokens，原voxelpruning因implementation不可用移除，baseline身份变化保留。90% R2R SR47.63<dense55.74、RxR45.71<56.53，即使OS上升不等STOP可靠性。4090 ablation diversity-only80% 54>joint53.29、merging54.21，不称联合规则必需/merge一般较差。90%local231.34→213.4ms/4.32→4.68fps，TFLOPs表为操作量而非明确每秒速率。realGo2/JetsonThorT5000/3cam/IsaacVSLAM，4-action生成1.43→1.25s不是独立peraction0.8Hz全motionloop，qualitative trials无数；FlashAttention更快只hypothesis。precision/repeats/concurrency/SLO未披露。Books待MULTIMODAL-EMBODIED-VLA observation/control预算与Ch23 selection接口具体PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-EMBODIED-VLA。Ch23 518–546 selector/proxy/原token/预算分责；Ch26 725–815全loop费用和action identity。salience×novelty/history MMR recipe 与 joint 反侧仅报告；OS≠STOP success、生成4-action latency非控制Hz。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Omni-Diffusion — 2603.06577v1

6=2+2+2；§3.1–3.4/4.1/4.3实际读完，core-06577保存；AppA/SDVI已实际读，core-omniex保存：Dream7BInstruct/3072训练长度/AdamW、γ.6/γp.5/L−100位置罚；60k跨模态合成样本，采样hardware/precision/batch/concurrency未披露。统一masked-token任务仍由MAGVIT-v2/8192图像codebook、SenseVoice连续speech input→MLP、GLMVoice12.5Hz/16384输出codec组成，不能写所有原始模态已经相同离散表示或无外部decoder。tail-pad mask率缩小γ<1减pad训练权重、低entropy先填、末段logits缩放γp软约束次序与begin-speech放0.25L都是具体mask/control分支；位置重复解释是作者假说，logit缩放只改变entropy不是硬顺序。ASR初长0.2×speech、TTS3.5×text及并行text/speech预填不保长度/语义对应；codec、后处理/CFG均需计费。7B，ASR WER7.05比GLM4Voice2.82更差；TTS3.07比Cosy2.89更差，CLIP-T.235低Emu.286；speech-to-image用CosyVoice2合成COCO10k不是自然spoken分布证明。image256→10step质量.235/.667→.226/.650，TTS0.5L→0.125L WER3.07→4.83，不把forward数当端到端无损加速。Books待MULTIMODAL-GENERATIVE-PARADIGMS unified路径/variable-length既有正文PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS。Ch24 1020–1125 typed unified路径不删codec、1778–1792 PAD/EOS/length与commit分责。tail mask/logit熵软位置/initial length是局部recipe，不授同codec或硬顺序/无损加速。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## CodeScout — 2603.05744v1

6=2+2+2；§4.1–4.4/5/6.1–6.3/6.6/8实际读完，core-05744保存。AST entity graph→LLM scope≤15→逐实体role/fixhint/alternativehypothesis→relevance过滤→独立issue增强，具体比较预先付费scope与trajectory内自增强，不能把增强spec当原始用户事实或已验证reproduction。SWEBenchVerified/3scaffold×3LLM，SWEagent三模型costcap1/1/.75USD而OpenHands80step不是同资源；SWEagent table绝对125/209/207对114/194/183，no-filter GPT190低default194，intrajectory109/177/158低default。crosssynthesis DeepSeek baseline108不同table114，应各协议保留，强augmenter换弱runner不写同模型免费增益。token图包含augmenter费用只支持Qwen/DeepSeek当前效率对象，缺闭源/Python以外验证，runtimehardware/precision/tokenlength/repeats/SLO未披露。候选保留独立preparation与runtime边界的局部反侧，不推普遍无法selfaugment。Books待AGENT-CONTEXT与AGENT-WORKFLOW具体已有论点PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / AGENT-CONTEXT。Ch75 70–109 dependency事实/AST-symbol派生view/assembly 与独立生成提示，244–282 prep+target费用；Ch81 1091–1098 exact code verifier。issueaugmentation只派生提案，scope/filter/newrunner identity不能当实际reproduction；局部独立prep优于trajectory内增强不普遍化。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## InfoGatherer — 2603.05909v1

6=2+2+2；§2.1–2.3/3.1–3.4/4及limits实际读完，core-infog保存。固定有限hypotheses、boundeddepth DAG，LLM把文本证据分配singletons/≤2 subsets/fullframe ignorance，K-way conjunctive冲突一次转fullframe而非反复nonassociative Yager，hypothetical singleton answers→BetP加权信息收益，先nonspecificity后discord、confidence.85/15turnabstain，是明确uncertainty表示与主动问询分工。LLM BBA与图不等事实概率/相互独立证据，repeated evidence相关性、有限hypotheses之外truth与confidence校准未证，不以越确定越正确。合成client/curated corpus/GPT5nano与Qwen32B T.5/topP1；samepointprob/unknownuniform variant61.3→66.5/67.5→69.3，但representation与提取fallback同时变，不归因DS唯一。Medical LLMDocs74.6>retrieved69.3，externalgrounding非均优；graphsyntheticSHD1.4±.9 onlyASIAlocal，不给实际医疗/法律可用建议。原始domain是测试fixture，采用仅主动信息获取机制；hardware/precision/预算与turn全费用/repeats/SLO未披露。Books待AGENT-PLANNING uncertainty/acquisition已有正文PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / AGENT-PLANNING。Ch79 297–310 calibrated prior/expected info gain→ask/explore/cost/fallback。BBA ignorance/discord recipe未成事实概率，representation+fallback联合改变不授DS唯一收益；root实际必要Source/PRE独核通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## ProEvolve — 2603.05910v1

6=2+2+2；§4.1–4.4/5.1–5.3及Table1/2实际读完，core-proe/proextra保存。schema/tool typed graph completion/saturation/deprecation→testspec先于implementation→tasksubgraph→reachablefacts/statewise user progression，贡献为环境版本变化下successcriterion和replay一起重验；graphformalism本身不保证generated代码完整正确。50轨迹/200环境/3000任务、Opus4.5全建构与usersimulator，100%modifiedcode coverage但pass90.83%；20环境54fail中39tests错/15invalidinputnoncritical由作者分类，不删除失败后声称全部有效。五models/每task4seedsT0/k5memory，GPT5 history0.786→.407在deprecation，Qwen反思overall.450<baseline.511，record未等预算且各环境任务不同，不把成功变化纯归因某graphedit/任意replay负面定律。statesuccess平均≠endpoint完成，generatedoracle/LLMextractor共源偏差，APIestimatedcost不合实际deployment，hardware/precision/tokenlimits/SLO未披露。Books待AGENT-WORKFLOW环境/任务版本合同与AGENT-MEMORY交接实际PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / AGENT-WORKFLOW。Ch81 177–209 template/runtime graph/trace，931–967 synthetic环境先验结构/语义/可行性与test版本；1091–1098 verifier identity。coverage≠pass、环境/任务共变与memory反退仅报告；root实际必要Source/PRE独核通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## DeepFact — 2603.05912v1

7=3+2+2；评价纠错深入§4 microgold、§5 AtS、§6/Table1/2、B.5/B.6、AppG/H及limits实际读完，core-fact/factextra保存。challenger提出verdict+rationale、auditor择证据修改B版本再score，需frozen snapshot或同B重评分archive；hiddenmicrogold/超过约5%更新再human校准是明确反漂移合同，future100%目标不是现在能力。944claims/20reports，test621/15reports含143microgolds（120人工注错）与323CSvalidation；human60.8→90.9是有限构造锚点并非全领域expert上限/全部test真值，posthoc99.3确认非盲独立复核，nonmicro92.7一致不是accuracy。重复同claims审读/agent所供evidence+humanlearning联合，不能归因更强agent唯一；2.8%human被错误agent带错保留，“nonregressive”只是所测pairings。20k paired reportbootstrap正确以15reports群组，R3-R2+4.9 CI1.4–7.9不授一般单调。DeepFact516.9K+18.6K/$1.16 vsgroup10 93.5K+3.5K/$0.21质量83.4→76.3，与literal“minimalquality”冲突；400expert-hour前付/搜索摘要/fullcontext费用，APIhardware/precision/concurrency/SLO未披露。不采用领域研究结论，只采用benchmark版本/纠错测量边界。Books待PLATFORM-EVALUATION-SYSTEM gold维护/challenger漂移具体PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / PLATFORM-EVALUATION-SYSTEM。Ch66 1534–1538 trace反例→owner裁定→固定version及修前后重跑，865–892 typed verifier/聚合可重算；采用纠错权限/同版本重评分已有覆盖。hiddenmicrogold/5%再校准具体recipe仅报告，posthoc一致非accuracy；root实际必要Source/PRE独核通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Interactive PDDL Planning — 2603.06064v1

6=2+2+2；III-A–C/IV-B–D/V-A/C/E实际读完，core-pddl保存。STRIPS typed interactive simulator7tools/MCP与完整plan独立验证，适用action回执≠goal-distance/unsolvability证据；当前state是外部真实模拟反馈，不能照录它为“self-generated”，缺的是progress signal而非任何外部grounding。102IPC Blocksworld/Haiku4.5 directT.2retry无failurefeedback与agenttemperature不可配，180swalllimit同而不等token预算；singletrial/i9/128GBFD。65→68success/6earlyexit四个direct可解，是有限负面边界非Agent普遍无效，5.7×tokens per solved包含额外成本。49 co-solved restrict避免生存偏差但不是所有hard题更优，FD87success高于LLM，stepwise与globalheuristic差异未受控，作者explanation待加入goal-distance干预才可归因。numeric/durative/derivedpredicate不支持，云LLMhardware/precision/network SLO未披露，不授physicalplanning。Books待AGENT-PLANNING与AGENT-TOOL-CALLING外部回执/完整验证具体PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / AGENT-PLANNING。Ch79 191–230 symbolic executor合法不等终局计划、368–388 milestone与完整checker；Ch81 931–955 deterministic state测试与model success分测。真实sim observation不等goal-distance，有限65→68/5.7×token负面留报告，不授所有Agent失效。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Boundary-Aware Streaming TTS — 2603.06444v1

6=2+2+2；§2.1–2.3/3.1–3.4/4.1–4.3实际读完，core-tts/ttsextra保存。wordtime弱对齐marker把发声span与未来lookahead分离、prevchunk文本/音频条件窗口重置，LLM更新而CosyVoice2 flow/vocoder冻结，有限ahead与bounded历史仍不证所有acousticstate缓存O(k+f)，首次reference长度/每词speech数等常量需绑定。930k~1000hEnglish、pfull.15/25Hz/min5；5words+2ahead的boundary适配与未适配nativeinterleave、noahead且offlinevocoder slidingbaseline同时变，longWER70.97 vs4.77不能纯归因KV增长/marker；f10,6 longWER12.98劣f10,2 3.03反侧。A40/2warmup+50trials、TTFA1296/RTF.782 vsnative1414/.843，slidingRTF.718但TTFA2588，不合并throughput与firstaudio。50utterance/tierabl，DeepSeek扩280–320词syntheticlong并非自然流任意长，20raters/t-CI不是全人群差异证明；precision/batch/concurrency/真实arrivaltime未披露，lookahead等待需另记。Books待MULTIMODAL-GENERATIVE-PARADIGMS speechstreaming合同及Ch23codec交接具体PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS。Ch24 712–727 有限lookahead chunk renderer/码层vs时间帧、首包费用、RTF≠SLO与播放不可rollback；marker/reset具体训练配方仅报告，ahead等待另计，不授全部状态O(k+f)。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## Pinterest Canvas — 2603.06453v1

6=2+2+2；§4.1/4.1.1/4.1.2/4.2.2–4.2.4/4.2.6/5.1/5.2/AppC实际读完，core-canvas保存。原product分割白底→reconstruct背景训练、生成后原cutout回贴、低分辨率多候选→3×SR后高分辨率原cutout再贴、mask+maskedimage VAEdecoder色彩接缝，具体贡献是原数据只读区跨生成/codec/SR仍需另设identity维护。分割错误/遮挡/边界误差不可能靠“原图回贴”自动保严格全商品identity。双rater任何一人标缺陷即拒、2candidate rewardrank与低scoreprefilter是质量合同而非rewardtruth。996同prompt/input、Canvas未用multi/reward，product84/background54.9/overall47.2分别对应成功事件，不能相加或把84说总通过；第三方overall26.2/28.2/42.5，产品保留更好而background不最高。A/BCTR+18/gCTR+7.6无N/CI/随机单位/期间，不进普遍商业或模型质量结论。primary配置precision/hardware/steps/latency/batch/concurrency/SLO未披露，raters是必要费用。Books待MULTIMODAL-GENERATIVE-PARADIGMS mutable/immutable生成区域与decoder交接具体PRE。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / MULTIMODAL-GENERATIVE-PARADIGMS。Ch24 79–81 local改写不能保未mask区、171 nonlinearcodec mask leakage、1163–1176独立decoder/输出验收。原图/生成region/最终像素分别验收，双回贴/VAEharmonization与qualityfilter工业recipe仅报告，segmentation非全identity保证。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。

## HART — 2603.05828v1

5=2+1+2；§3.2/3.3.1–3.3.5/3.4/4.1/4.2与Table1–3实际读完，core-hart保存。span+context绑定类型/作者errorlabel/外部纠错证据，global evidencepool、multiquery与crossencoder有限ablation提供归因粒度/检索排序独立增量，不因没有内部干预一律EX。labels“mechanism”不是真实生成内因；semanticcos阈值hit只对人工gold等价类，不自动entailment/contradictiontruth，近邻“事实相反可分”是假设。LongFact++/Sonnetweb初标与human采样refinement、ChatGPT5.1选证，多环共源；noise≤τ但w/τ/全标签coverage ND不能当独立有效认证。random70/10/20、34943corpus、mpnet/minilm/RTX5080 16GB/Ryzen9950X；R1.4133→.5172/.6244/.7068与R10.7146/.7146/.8557/.8557说明rerank改善顶位、MQ扩大recall，不授每部独立最高；Table3不同modeldatasetR1.8024/.7522不直接拼合Table1。训练precision/query数/阈值w/延迟/重复/SLO未披露，span已给定不等自动hallucination检测，未检排泄漏/同义gold复用。Books待AGENT-RAG rankingvs事实证据authority已有正文PRE；内部因果强claim不进书。

当前实际处置（覆盖初稿待PRE状态）：已有覆盖 / AGENT-RAG。Ch76 496–500 crossencoder ranking、581–613 relevance/sufficiency/claim-support三层及人工anchor；span/context/MQ/rerank有限诊断保留。equivalence cosine hit非entailment/真实内因；root实际必要Source/PRE独核通过。 独立复核确认的是上述有限采用界限，不是全部宣传；本日DAY仍待root。
