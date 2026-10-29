# Oct07作者剩余限定Source（逐项推进，不自签）

作者oct07_missing；root已逐项完整题摘准入校准。只限本日具名家族必要层，普通未读不叫外部；未核代码/未复现。日期合证统一按已实际核的官方历史公告/发号规则及精确DataCite client=arxiv.content/state=findable；不把registered当实际公开时刻。下面三官方abs现读唯一v1、无具名撤回/纠错，未遍历完整版本史。所有最早公告界Oct6 00:00Z，registered均当天，整个possible区间BJT Oct6。

## 04537 PhaseGate

原证 https://arxiv.org/html/2610.04537v1 ，core-04537v1.raw.html；实际§2–4/所有主表与§5限制（导航8–62）。官方abs唯一v1 2026-10-03T14:07:04Z；精确datacite registered2026-10-06T04:36:15.000Z。

增量不是一般“按phase调度”：统一内存CPU HNSW随机访问对decode干扰远大于prefill，校准分别选择p/d cap，TimeGate匹配同cap/高低时间占比/切换频率却不看LLMphase，验证alignment而非平均并发是受测必要差额。Runtime非抢占，进入decode只停新admission，不强制砍active，必须核drain。

配置：4bitQwen2.5-1.5B/MLX-LM0.31.3，M4Mini主要、M4Air/M2/M2Pro有限复核；2048tokenIDs+128逐tokenforward，非自然生成，排tokenization/sampling/质量。FAISS HNSW100k×384/M32，每call16queries单线程，队列active期间backlogged；它不是当前response必须等待的检索，未测检索等待尾或E2ERAG。

关键证据：M4 calibration3×100request/candidate，B=1.25最小共同可行所测预算，不是普遍阈值；selectedFixed1/4→1冻结，7paired随机×250requests，均7/7满足两p95约束，1.6vs.78kQPS；TimeGate相近1.5k但0/7合规，TPOT+60%。M4 p95-of-request-p95 vsM2 p95-of-request-mean定义不同，不能跨机拼成相同tail指标；M2Pro无TimeGate/pageoutfree对照，只支持排序。4→0反比4→1差原因未解，不能假设cap越小越好。

反侧：p95drain26.6ms/max31.5，active>1占decode1.06%但admission高cap仅.003%，二者不是相同界。transition p95额外5.2ms，smallpageouts保confound；oneperdevice、固定模型/trace，长非抢占作业、变负载在线调整和真实RAG未验证。输出变长收益缩窄。拟6分2+2+2，因真实phase/cap/共享带宽与非抢占尾边界。

拟owner INFER-SCHEDULING Ch56，实际读Host Control Plane容量合同完整局部；它解释CPU发射饥饿，尚无CPU随机检索共享内存的phase-asymmetric干扰与matchedphaseblind反证。Ch55/57交接已读；不是Ch76检索质量/索引机制。拟在host干扰局部补最小一段，未PRE/未写。

## 05748 MOLT

原证 https://arxiv.org/html/2610.05748v1 ，core-05748v1.raw.html；实际§2.3–5.6（导航29–114），§6只核对baseline角色。官方abs唯一v1 2026-10-05T03:53:21Z；registered2026-10-06T05:06:53.000Z。

增量：autoscaling最小replica不能回收秒级空闲memory，coarse整sample回收重启浪费step；保存activation为细粒度slot，fixedVA backingstate变更，不搬数据；forward/每backward访问按实际backing选择save/recompute，handover不中断完整训练step。reback仅step边界，非每时刻最优。Pinned保weights/LoRA params/grad/optimizer/intermediates，输入等不可重算slot不unback，不把全部trainingHBM都称可撤销。

安全必要事实§4.4：CPU dispatch与GPUcompletion不同，保护窗口含completion前一layer至dispatchfrontier，callback到下一layer才清标；handover snapshot冻结dispatch并延后callback，GPU可继续执行，排掉TOCTOU。TP各rank窗口取union且选相同slot，否则recompute路径collective不匹配。Offlinecap最小不延长step，cap太小GPU等CPU，非无成本throttle。

配置：Mistral24B H100TP1/2，LLaMA70B H100TP4/B200TP1，rank8LoRA，ShareGPT inference/Alpaca tuning，seq768/2048/1024/512绑定各deployment；vLLM0.11/PyTorch2.8派生原型。数值precision/完整并发与输入输出分布必要主配置未披露，不补。SLO是同deployment inferencealone mean的TTFT/TPOT各3倍，非固定客户毫秒SLO，trace driven不是真生产验收。

证据/反侧：samepool且continuousvsstep-level唯一改handover时点；T2 continuous SLO99.7–100%，tuning较discard1.9–3.3x，但LLMStation-only在两24B tuning更快/Serving SLO失败，不能称Pareto支配任意点。TP4 continuous与step相同64.5tokens/s，只改善SLO；T2不少TPOT分位比SIRIUS更高（TP4 p95 136.8vs105.1），不能写所有尾延迟更低。dispatchcap消融各点one run，±5%人为容忍非误差带；cap4 step+13.1–24.6%。回收IPC/unback/pagezero均计，handover p99≤1.6ms局部条件，不是任意故障/多租户保证；无adapter最终质量或数值一致验证不能自签。

拟6分2+2+2，因细粒度backing/recompute与多rank异步安全接口有直接差额，已深入必要正确性。拟owner INFER-GPU-MEMORY Ch54，实际读生命周期/Peer GPU/EMA借还完整局部；已有安全requestboundary peer租借，不含runningtrainingstep activation slot撤销/union保护。Ch53/55交接已读，不复制Ch35 checkpoint或LoRA本体。建议Peer GPU借还段后最小段，未PRE/未写。

## 06394 HarnessHOI

原证 https://arxiv.org/html/2610.06394v1 ，core-06394v1.raw.html；实际§3.2–3.4/4.1/4.3/T3–4（导航30–91），未泛读HOI任务附件。官方abs唯一v1 2026-10-05T14:16:28Z；registered2026-10-06T05:24:32.000Z。root已读决定准入的完整core事实，采表示接口非HOI领域指标。

增量：global/discovery/crop候选先绑定persistentinstance与原图坐标/sourceview，保每identity多框；依据identity/category/visibleextent的同一MLLM选择唯一候选，所有action/role共享该box/category，防每role各自选择相互矛盾grounding。只有一个候选不另选。Relationunknown保未知，不等漏检修复完成；归一化answerlogit不是经独立校准的概率/几何真值。

T4固定candidateboxes/imageviews，relation-agnostic criterion 比 relation-conditioned criterion（两者都 one shared geometry） +.41HICO/+.47/.54VCOCO，支持局部选择口径，不是所有整体pipeline收益都归G；T3firstcandidate32.95vs33.20、VCOCO44.38/49.48vs44.65/49.70，差额小且未据此自签显著。全frozenQwen3.5-9B、最多2localobs、trainset选prompt/policy，HICO9658/VCOCO4946/IoU.5。跨方法backbone/roleprotocol不一致，不采用榜单倍数；质量、sameMLLM相关错误、候选覆盖缺失仍限制。每候选问答、crop、坐标关联、sharedselection和最终任务回归均付费；并非新独立几何verifier。后续独立Source及D4/E2/E4/E5必要边界已由reader2 R2-10实际核实；此作者早期笔记不代独立层。

拟6分2+2+2；owner初拟MULTIMODAL-REPRESENTATION Ch23 sceneIR/几何事实邻接，已有合法IR≠视觉真值但缺跨role共享persistentgeometry接口，需实际再读最小插位后literal。当前未独立Source/PRE/写入。
