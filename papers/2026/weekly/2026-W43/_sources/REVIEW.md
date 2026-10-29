# Weekly 2026-W43 — 独立新增来源复核

复核者：`live1025_weekly_review`（非新增来源作者，非报告/Books作者）。窗口：2026-10-18～2026-10-24 BJT。

## 本批范围与结论

已读 AGENTS、研究合同、Report合同、统一Prompt、ROADMAP、来源使用说明/每周组，以及项目背景、学习理念、写作指南、相关checkpoint。本批逐项检查 `WEEKLY_NEW_SOURCES.md` 的10个候选家族、原始必要证据与7个实际owner正文；不重新扫描Daily组、不重审七份Daily全部论文。复用Daily原证据不等Weekly家族数可以直接相加。

**当前结论：通过，实际五处写后与六部分Weekly最终验收见末节。** 以下首批记录是写前的准入/必要证据及owner差额判断，不能单独替代末节的实际验收。所有10家族可保留为受限的新验证/设计边界候选，不应按10家族机械地产生10处Books整合。独立核查的性能/回归均为作者记录，本次没有运行GPU/训练/服务测试。

来源边界合理：每周29源用官方目录/发布页，普通PR仅围绕release具名正确性信号打开，没有把宽列表扩成所有PR队列。Ai2 Papers与EverMind无日期主页的限制不可变成全目录Coverage通过；报告必须保留原文限制、可接受替代与定点重开条件。

## 日期与事件去重

独立打开METR两文，页面日期分别Oct22、Oct20；Prime官方发布Oct19、Ai2官方FairStress发布Oct20。GitHub官方API的 `published_at` 独立核到：DeepSpeed v0.19.8 `2026-10-20T15:21:47Z`；vLLM v0.32.0 `2026-10-18T06:50:48Z`；SGLang v0.5.22 `2026-10-19T02:55:19Z`；FlashInfer rc5 `2026-10-20T04:30:32Z`、rc6 `2026-10-22T07:58:40Z`、post1 `2026-10-23T18:38:46Z`；Transformers v5.20.2 `2026-10-19T17:45:37Z`；EverOS v1.5.0 `2026-10-21T13:38:00Z`。转BJT均落窗，特别post1为Oct24，HF为Oct20。

release交付与更早PR公开不是同一事件，不能把9月/10月上旬PR说成当周新发明/新漏洞。FlashInfer网页索引仍呈旧Open状态，不能据此推翻现态；独立官方PR API已核 `merged=true`、`2026-10-13T19:26:34Z`、merge `1ad1ed9245f0417cba0011ae85a43488129cca35`，与Source一致。三个FlashInfer release只计一个家族，不相加compare提交数。EverOS rc1→1.5.0仅release/preinstall变化不再算机制贡献。

对Daily19～24 README独立检索具名PR、文章slug和release家族，未发现同事件已审冲突；这只是具名去重，不是字符串零命中证明全周无遗漏。Daily25尚由root处理，最终归并需结合其实际保存结果，不由本批预签。

## 10家族逐项：证据 → 实际正文 → Books判断

### 1. METR / OpenAI monitoring：可整合最小缺口

[原始公开报告](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/) Findings/design ideals已独立读。2+2+2=6成立，可靠性边界应深入相关域。7月21日前系统的eligible与实际监控分母不同；compaction未触发和等待交还控制权，能使合资格轨迹未送达/监控无限延迟。约一成估计有日志不足的不确定性，不能把99.2% eligible写成监控成功率。OpenAI已独立发现/试点期间修复是历史事实，不是METR复验当前系统；未公开61页不能补作证据。

`PLATFORM-MONITORING` Ch67实际529～565讲外部telemetry、独立观察路径、压缩与wiring；其中534～537针对训练进程共享失效域，并未拆 eligible、trigger、delivered、reviewed 的人口及被观测Agent能拖延trigger的问题。`PLATFORM-EVALUATION-SYSTEM` Ch66 5129～5132已有选择性上报与异步检测/预防区别，不应重复写那里。

可补的最小命题：监控触发和送达对账不能依赖Agent主动归还控制权，独立inference/monitor记录需要核对实际轨迹覆盖，包括compaction边界。其余“monitor不是安全真值”等原则已有，无须再加。

### 2. Prime IPO：可整合最小缺口

[v0.10.0固定文档](https://github.com/PrimeIntellect-ai/prime-rl/blob/v0.10.0/docs/ipo.md) Masking、ablation、阈值、reproducing独立读。2+2+2=6成立。双边 `abs(exp(train_logprob)-exp(infer_logprob))>eps` 与advantage符号无关，是区别于ratio mask的具体选择；按所采token/其他的二分可解释为TV，不能当全词表TV约束。GLM-4.5-Air SWE、64-step lag/no router replay只支持局部消融；eps0.1坍缩与通常IcePop也稳定必须保留，不签普遍更优或无偏。

`TRAIN-GRPO` Ch33 2752～2760已有低熵ratio noise与entropy gate；2825～2835已有behavior/current revision、prompt级drift admission改变条件人口。这里未讲绝对概率差双边mask及其与advantage解耦。可紧接异步noise段补这一个替代分支，沿用既有版本/支持域/丢样成本和同步回退，不重讲异步RL通用治理。

### 3. METR / Anthropic review：可整合最小缺口

[原文](https://metr.org/blog/2026-10-20-misalignment-risk-report-august-2026-review/) Scope/summary及covert-capability段已独立读。2+2+2=6成立。hidden-CoT评测移除了“理由使monitor相信行为被许可”的生产可见通道，因此不能自动称更宽松的攻击评测。该判断来自公开协议差异与具名事件，非未公开案例的全面认证；METR未断言rationalization是蓄意，1%/50%作者反事实不是全局漏检率。

`PLATFORM-EVALUATION-SYSTEM` Ch66 5120～5132已有matched interface、零检测不安全、选择性上报和异步检测边界；1688附近已有CoT可读不等忠实，但未写“删去CoT也可能删去攻击通道”。可在监控评价论证补一个最小反例：更少可见信息并不必然构成更保守安全压力测试，评测须匹配生产monitor实际消费通道。不能顺势宣称action-only普遍更好。

### 4. FairStress：已有覆盖，不必新写Books

[官方Oct20发布](https://allenai.org/blog/fairstress)、[70页原报告](https://allenai.org/papers/fairstress)摘要、§3.1及D.1 Tables33～36已独立核。2+1+2=5成立：原始选择率相似仍可有压力抵抗不对称，且同题/同weights下wording与scoring都会改变方向。不能只归因loglikelihood，也不把activation可分性当因果解释。

实际已有论证：Ch66 431～432明确“中性选择率接近一半不等双向压力对称”，要求matched A/B cue、valid-choice与拒答/无效/重试分母分开；979～981明确选项logits可能读到理由首token，direct/CoT/生成后抽取不是同一输出事件；4923～4925明确固定题目/权重下harness配置可由脆弱items改变排名；265明确平均似然不等生成选择概率。故`PLATFORM-EVALUATION-SYSTEM`可NC，保留FairStress为这些已陈述边界的新受限验证；无需重复公平性方法综述。

### 5. DeepSpeed v0.19.8：已有原则覆盖，具体故障仅报告

[8382](https://github.com/deepspeedai/DeepSpeed/pull/8382)与[8539](https://github.com/deepspeedai/DeepSpeed/pull/8539) Root cause/Fix/verification独立读。1+2+2=5成立，具名正确性信号需深入；GPU CI通过不覆盖CPU type-string漏bucket，mean/相同rank梯度可掩盖缺归约；独立Gloo后台handles不继承CUDA单stream FIFO，末handle wait不认证前面完成。CPU/gloo world-size2～3作者回归不是本次复现，更不证明CUDA原路径已坏。

Ch36实际119～121拆API发起、真实路径、ordering、completion/visibility，要求显式完成检查；321规定不能取消wait，329～331拆input readiness、store完成、stage回收与所有shard drain；580～582要求实际归约域、零/None梯度参与和matched gradient，而非只看loss。因此`TRAIN-DISTRIBUTED-TRAINING`的通用论证已承载所需设计判断。dtype字符串改dtype、逐handle wait可在报告保留精确修复事实，不为新增几条实现bug复制一段成熟同步原则。若root认为仍有独立稳定缺口，应先指出现有段不能承载的命题，不能仅以fix标签判I。

### 6. vLLM SHM认证：可整合最小缺口

[59357](https://github.com/vllm-project/vllm/pull/59357) Summary/具体变更与tests独立读；2+2+2=6成立，安全变化深入。cache key/address/id签名、get/touch前验证、clear不重置ID与bounds/scale-out输入校验，共同约束句柄的授权和slot复用身份。仅可选SHM路径，默认LRU不受该问题影响；秘钥在服务端SHM中，不防本机内存权限攻击者。作者74passed/1skipped不是本地验收。

`PLATFORM-SECURITY` Ch72 2536～2542已有principal-specific cache namespace及causal state provenance；2787已有deserialize生命周期隔离，但没有说明“地址相同与对象身份/可反序列化权限不同”、clear后旧句柄重放/slot复用。可在cache trust论证补这一生命周期反例及相应认证位置，不重复整个能力授权框架、不认证整版无漏洞。

### 7. SGLang grammar/recurrent commit：已有覆盖

[43029](https://github.com/sgl-project/sglang/pull/43029)相关commit/描述与retained-prefix回归信号已独立核；2+1+2=5成立，正确性局部深入。grammar可能比spec verifier接受数量再截断，boundary计数应属最终retained run，不能把中间accepted值当checkpoint已写。

`INFER-SPECULATIVE-DECODING` Ch48 743～776已完整推导recurrent state不能只移动KV pointer，verifier为唯一commit owner，KV/recurrent/accepted length/streamed output跨同一frontier，否则被拒token污染后续历史。此次具体grammar截断正是该命题的实例，未提出另一state algebra或commit机制。可NC并保留版本/PR事实，不能扩说所有spec decoding、模型或后端都错误/都修好。

### 8. FlashInfer LL collective：已有覆盖，具体修复仅报告

[5652](https://github.com/flashinfer-ai/flashinfer/pull/5652) Description与官方现态API独立核；1+2+2=5成立，correctness局部深入。peer DSM访问前需要初始cluster rendezvous，post-store/lifetime barrier不替代初始同步；CUDA Graph changing-input/PDL是作者覆盖，不是本次Blackwell/Rubin复现。

Ch36 329～331已分input readiness、store完成、stage回收、barrier/FIFO、peer访问条件及runtime completion；119～121也明确通知不等可读。`TRAIN-DISTRIBUTED-TRAINING`已有覆盖，可将该实现信号只留报告，不另用新标题重复readiness与lifetime原则。rc6无独立机制不加家族/分。

### 9. Transformers EP bf16梯度：已有覆盖，保留受限新验证

[49688](https://github.com/huggingface/transformers/pull/49688)明确条件、PREMUL_SUM与per-expert whole-batch oracle及实际diff独立核。2+2+2=6可保留；拓扑 `tp<ep<fsdp*tp`，torch≤2.13该NCCL bf16路径可归零，修为sum后本地divide。**分母不是此次修复对象**：实际diff保留 `set_gradient_divide_factor(fsdp_size)`，因为dispatch后的expert梯度覆盖该数量的batch；改变的是所有backend均强制sum再divide，不可改写为“应使用更小expert group分母”。作者4×B300下0/0.0889/FP32 0.0887是局部证据，不认证所有torch/NCCL。

Ch36 580～582已明确`D`是实际gradient-average域而非整个job，并特别指出expert子域/零梯度参与；243～245要求类型、operator和数值容差共同验收；328～331保留backend/版本与完整数值验收。它们承载的不是“有梯度即可”而是实际域与数值检查。此次PREMUL_SUM故障是这些原则的新受限验证，可NC/具体版本仅报告，不必新增另一个“验证数值”的段落。

### 10. EverOS：可整合最小缺口

[v1.5.0 release](https://github.com/EverMind-AI/EverOS/releases/tag/v1.5.0) async queue、failed/non-atomic retry、startup identity及session-lock说明已独立读；2+2+2=6成立。202为durable inbox接收，不是episode抽取成功；memcell已写后取消不能让派生提取搁浅，写前timeout与写后提取责任分开。失败默认不自动重试、crash replay次数不提供exactly-once。旧index补登记不证明历史identity；probe失败warn/skip不能称全量fail-closed。

`AGENT-MEMORY` Ch77 1345～1360已有admission/visibility/recovery和store恢复不等计算恢复，1361～1372已有并发/CAS；但1654虽有移出critical path标题，实际紧接eviction，没有durable accepted→source/memcell commit→derived extraction状态/取消边界。因此可补这一最小生命周期差额；embedding model identity的通用owner是Ch76，不在Ch77重复扩写向量索引升级全链。

## 分层抽检与未检查范围

除全部10候选外，抽检明确排除的两类：Sakana QD-Rec原始技术说明的Introduction/任务定义（固定候选推荐、item–hypothesis搜索，不凭通用search类比纳入模型/系统机制）；Mistral Voxtral3官方核心说明（三stage语音组合、SDK功能和宣传延迟，不凭发布身份或功能数准入）。未发现共同错误理由需重开同类集合。Recursive Updates浏览器原件本次不可达，复用Source作者核心阅读，不把该项计为本人的独立原件抽检。其余范围外、无窗内release与明确产品/活动排除未逐条二次重读；来源目录停止点复核以Source真实记录为依据，不冒充独立全网召回。

## 一次实际Books写后与六部分Weekly最终验收

复核者：`live1025_weekly_review`，非Report作者，亦非下述五处Books作者。**结论：通过。** 实际Books writer为 `live1025_weekly_sources`，root负责报告及统合；不把root的授权/作者自检当本人的独立写后。

收到真实保存通知后，本人实际完整读到五个新增自然段、完整直接前后段及真正 `## Review notes` 下本人来源注：Ch67 539/626 `SF-2026-METR-20261022-OPENAI-MONITORING`；Ch33 2762/3033 `SF-2026-PRIME-RL-010-IPO`；Ch66 5134/5496 `SF-2026-METR-20261020-ANTHROPIC-REVIEW`；Ch77 1349/1973 `SF-2026-EVEROS-150-MEMORY-COMMIT`；Ch72 2538/3637 `SF-2026-VLLM-PR59357-SHM-HANDLE`。这五处均为真实写后检查，不沿用前述差额判断代签。

五项POST通过：监控触发/人口分母紧接独立观察路径，保历史日期、日志不确定与修补未复验；IPO紧接低熵ratio noise，保双边mask、二分TV而非全词表、删样人口及eps反退，未取代原ratio/sync退路；METR评测反例接选择性上报/异步检测段，保非蓄意判断与非通用action-only优越；EverOS置于实际transaction boundary后，accepted/cell/derived与取消责任清晰，保非原子失败及非exactly-once，不扩写embedding；vLLM置于namespace之后、causal provenance之前，明确key/address/ID签名、clear生命周期、解引用前验证及本机内存威胁边界。新增机制、适用条件、成本、反侧和原方案退路均留在正文，不靠来源注补救正文泛化。另5项NC已有具体承载段，不需制造diff或追加POST。

已实际完整读取 [Weekly六部分](../README.md)，不是只核标题或完成字段：

- 窗口为Oct18～24 BJT，运行周日Oct25所属W43；Daily19～25头部窗口连续对应Oct18～24，均已保存完成。逐份读其§6并定点核20的 `SYSTEMS_READER_POST_CORE.md` §G、21的R229/终态、22的R154/R155、23的R69/R70、24的R17及25最终日级验收；Daily19以其实际§6中的独立root身份与检查范围为准，不虚构不存在的同名REVIEW文件。有效原审/POST复用，不重审612论文。
- 独立数实际Daily候选表为0/64/220/105/189/32/2，共612条；定点解析得594个互异arXiv基ID，另18个官方事件条目。它们是已审事件记录，不是612项独立新贡献。OpenAgentCore 808/811→819→846、MiMo-Code2695→2703、Qwen Code15104等→v0.26.1新scope的同项目身份归并成立，各事件的分数、不同Books处置与实际日期必须保留。按这三个项目归并可得608复用家族、加新增10得618，但报告当前不声称这一总数，避免把事件计数与材料家族边界混成新的贡献数；也不把两个METR独立报告合并。未发现需要重开某个Daily判断的具体冲突。
- §2实数43到期来源＝14日级＋29周级，Daily复用与Weekly新增范围分清；按需未出现独立扫描触发，不因必要原件读取而扩站。七个外部子范围（Google、Meta、Qwen、Moonshot、MiMo、Ai2、EverMind）都明确隔离，不被“已汇总”升级为完整Coverage；混元Oct25当前11/11目录恢复的具体解除边界不外推删除稿/历史修改。
- §3全部10新增家族与§4一一对应，日期、评分与必要审阅深度保持；5真实整合、5具体NC与本次POST一致。FlashInfer三release重叠不加家族，HF实际diff分母纠正已进入Source/报告，没有恢复“应改expert小组分母”的误述；背景PR不搬移首公开日期。
- 三条跨材料关系是状态身份/派生完成、测量与筛选人口、真实数值/提交边界的原理复用，不虚构直接演化谱系；引用Daily具名范围与新材料必要证据，没有借类比制造额外整合。§5保留七来源子范围及Daily21两项中心争议/日期资格的原隔离与定点重开，不升级为正面证据、Books许可或全面无遗漏保证。未读普通材料没有被包装成外部受阻。

机械检查：本人重跑 `python3 scripts/validate_research.py --report papers/2026/weekly/2026-W43/README.md`，1份V3通过；Weekly及五个Books限定 `git diff --check` 无诊断。机械检查不替代上述实际语义验收，不证明全仓清洁或实验复现。

读取时报告仍保留“进行中/待实际写后/未通过”的此前真实状态；以上已经完成这些普通工作。root可据本记录一次同步开头状态、§1/§3/§5/§6为完成/通过，清除已完成的普通待办，保留全部外部限制、证据边界与原事件处置。无需额外行政复核、重复原文或再验相同五处正文；实质采用内容变化时才重开受影响部分。本人只修改此REVIEW，没有修改Report、Books、State、索引或Git index。
