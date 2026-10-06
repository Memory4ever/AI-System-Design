# ProRL Agent18815：必要原证与最小 dataflow PRE

准备者resume_mar18，仅03-21补BJT03/20；fresh合同/ROADMAP/Books上下文与本日原停点已实际重载。首批准入非本项，后批十一潜力root完整AB独校已通过；本v1 DOI/availability日级夹证原SUP_FIRST_ADMISSION L58复用，不冒精确公告或无其他公开。旧2025 artifact仅具体去重/接口差额核，不跑2025日报。

## 旧公开与实际新增事件

[官方作者discussion#15](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/discussions/15)实际原heading日期Dec17,2025、具名相同核心authors；已公开HTTP把trainer/agent/inference分开、task/serveravailability/result三queue、CPU/GPU独立部署与DAPO动态补充/取消/跨迭代重用，以及Qwen3-4B的SWE/Math/Code实验。本v1不是该Blog同标题论文，不拿旧artifact证明论文早发，但不为旧服务拆分/三queue/DAPO原则新评分。必要日期/原字段与root裁定见同SUP_FIRST_ADMISSION，不扩repo全history或后来Polar。

本日[exact-v1](https://arxiv.org/html/2603.18815v1)实际§1–3.4、§4.1–4.4/Tables1–3与§5必要边界：新增/明确INIT–RUN–EVAL AgentHandler分阶段pool/异常结果与原生成tokenID/logprob的训练交付接口，rootless runtime作为具体执行条件。拟2+2+2=6，以generation→trajectory publication→learner语义与资源阶段分责计分，不采成熟service拆分或Table1框架排行。未核代码、部署或复现。

## 必要机制、关键评价与直接反侧

- §3.2.1 handler有init/run/eval三独立接口、每stage exception与final_result序列化；§3.3各pool/queue独立，RUN后cleanup runtime才进EVAL，必须由显式artifact/result handoff承载后续评价，原文没有披露任意任务完整验证闭包，不补造所有测试都在仍活sandbox运行。三个阶段pool不是旧Blog三种task/serveravailability/result queue的同一切分。
- §3.2.2 Singularity子进程session、TERM→KILL、127.x loopback allocator、可选network none及fakeroot；SIF/Jinja缓存Scratch/Versioned/Lock说明运行人口与准备费，不授生产多租户、任意HPC兼容/根less绝对隔离。版本或lockfile相同也不自证全部外部依赖一致。§3.2.3 direct pty/IPython/UDS只是降低局部工具路径开销；IPython仍有持久状态，不授全trajectory无network开销或零费。
- §3.3.3 prompt_ids/response_ids与generation-time logprobs/input_ids/output_ids原样传播，旧assistant turn保留原token、只tokenize新environment message；该语法身份避免retokenization，但不自动证明生成policy/checkpoint、mask/action population及logprob convention与当前learner一致。
- §3.3.2 heap listing称in-flight，prose又一次/task递增不减、formula解释totalcalls；不采用精确负载公式/公平无同步保证。clear/re-register backend声称后续rollout用新weights且不打断pipeline已有job，但没有给跨多turnjob完整policyepoch承诺，不能授on-policy稳定；§3.4carryover unfinished与§3.3cancel丢弃并释放runtime两路径如何保持旧prefix/trajectory状态也未闭合，不补无损恢复。
- §3.3.4 PausableTimer只active INIT/RUN/EVAL计时，排队不计；这是execution预算，不是wallclock deadline。error serialized不等valid训练样本；§4.1明确errors不进gradient。cancel skip/discard、cancel async task、close runtime与completion event是不同可核事件，原正文声称immediate/无orphan不替实际cleanup证据或任意effect撤回。
- §4.1主要训练32H100，batch32/minibatch8、8rollouts/prompt，DAPO、KL1e-4/LR1e-6；§4.2 SWE-Gym293、Qwen3 4/8/14B；RL后提升不识别服务器接口唯一因果，SkyRL reported非全部reproduced且训练预算/实现不同。旧Blog32A100/4B结果不能混作相同预算的before/after。
- §4.4.2单组件对照Qwen3-14B-Instruct-2507/8H100，LB用equalinstance、EB回OpenHands bash、SC等全部完成。Table3 Action Time(.42/.78)、GPUutil78/42/68/65与throughput.37/.25/.29/.30仅该训练配置；无workerpool/queueclock独立收益对照，hardwareprecision/servingbatch/concurrency/contextlength/repeatseed/CI/full CPU/启动镜像/网络资源和尾deadline Not Disclosed。§4.4 node扩展图未给全部nodetype/重复，不采用普遍近线性/最优吞吐；discard慢/错样本还可能改变训练人口（工程验收问题），只成功率不能排除此偏差。

## Actual sole owner 与最小差额

`TRAIN-DISTRIBUTED-TRAINING` Ch36 actual1510–1536已有rollout/update分池和policyidentity、1614–1681版本化dataflow/typedtrajectory stream及toolfrontierplacement；相邻Ch35/37开篇实际读。Ch84 actual140–171/475–495已有typedSession与sandbox/executionauthority，不另复制worker/learner交付机制。Ch36当前stream仍没有显式**原生成tokenID/logprob不经retokenize交付，以及初始化/生成/评价active阶段时间与queuewallclock分开**。一个短接口分支可接现dataflow成熟主线1632 marker之后/trajectory FIFO前，保原通用dataflow与policyidentity段不覆盖。

## 两段逐字 PRE（待非准备者与锁）

把 rollout 暴露为独立服务后，trainer 收到的不能只是可重新分词的最终文本。可让初始化、生成与评价各由独立 worker pool 消费明确的阶段结果，生成侧保留原 prompt/response token IDs、逐 token log-probabilities 和已有 assistant turns；新的环境消息另行编码，再以这份原始轨迹表示交给 learner。它把资源阶段的排队与训练样本的语法身份分开，避免文本往返改变采样序列；但 token 一致仍不等于 policy revision、mask 或 log-probability 口径一致，模型后端换代和跨迭代续做必须另验旧 prefix 与新 policy 能否共同采用。<!-- source-family:SF-2026-ARXIV-2603-18815 -->

这种边界新增阶段 queue、镜像/工具状态、结果序列化和取消清理成本。[受限 ProRL Agent 实现说明](https://arxiv.org/html/2603.18815v1)把 timeout 只累计在活跃阶段，不能把排队除外后的 execution time 当端到端 deadline；错误结果能够返回也不取得训练资格，取消请求亦不证所有容器或副作用已回收。局部工具与负载对照只支持所测配置，不能把 RL 总分提升归因接口、或由 rootless 签发生产隔离。完整初始化、推理、工具、评价与等待均记账；阶段产物、policy 身份或清理无法确认时，保留同步 trainer loop、固定后端与原 token 轨迹，丢弃不合格结果，而不是让更高吞吐覆盖样本一致性。

## 静态源注 PRE

- `SF-2026-ARXIV-2603-18815` — [ProRL Agent exact-v1](https://arxiv.org/html/2603.18815v1) §3.2–3.4/4.1–4.4/Tables2–3；仅阶段worker/原token与generation logprob交付、active-stage clock与完整deadline分责。旧Dec17,2025作者Blog服务拆分/DAPO不重复计新；backend换代/未完成任务续做、heap口径、取消清理/训练资格、rootless边界与全资源费用保留，不采任意on-policy恢复、普遍线性扩展或生产隔离，未核实现/复现。

## 非准备者必要 Source / actual owner / PRE：有限通过

root实际读exact-v1 §3.1–3.4及§4.1–4.4/Tables2–3、组件消融，并定点核作者2025-12-17 discussion#15的旧接口；实际Ch36版本化dataflow及trajectory交接、Ch35/37开篇和Ch84 typedSession邻接回对两段PRE。Source、2+2+2=6评分、唯一owner与原两段/静态注有限PASS：阶段INIT/RUN/EVAL pool与生成token/logprob直接交付不重复旧HTTP三queue/DAPO原则，active阶段时钟不冒充端到端deadline。

新后端与跨迭代任务没有完整policyepoch保证、heap原文inflight/累计口径冲突、cleanup在评价前、取消与carryover未给统一恢复协议等反侧均保留，不采用实现即生产隔离或RL收益唯一因果。root授resume_mar18 Ch36原15565 marker之后/trajectory FIFO之前两段及自身静态注窄写；写后root一次实际正文/完整邻接/自身注POST才计safe、释放，不预支DAY。

## 非写入者 actual POST：有限通过

root实际读Ch36完整1620–1653（版本化dataflow→原两段1634/1636→trajectory FIFO及下一节）、末五行自身source注和相邻旧注，逐字回原PRE/上述有效必要Source。文本保持原token身份≠policy/mask口径、阶段active clock≠端到端deadline、错误≠训练资格和取消≠完整清理；无模型总分因果或生产隔离外推。正文/自身注各唯一，原有效段未覆盖。非writer actualPOST有限PASS；Ch36窄锁释放，本项可计I，不预支最终分母或DAY。
