# 第十八包：AB10运行时仿真、attention变换与oracle迁移（待非作者PRE）

续既有23036/23057/23065，不扩池。精确v1完整题摘/必要HTML与当前事件Comments已读。FETCH_AB10_CORE执行2026-10-05T20:56:09～14Z。23036当前v2为March23窗外；23065窗内v2只见版本与journal reference，未见已核的重要纠错/撤回说明，版本号码不自动触发全文diff。以下拟3I，均非safe、无lease或Books写入。

## 日期

原v1均晚于02/25 19:00Z；原公告政策下界02/27 09:00+08，同identityregistered秒精度加1秒上界。DataCite非primary技术/首公开公告。

| ID | Submitted UTC | registered UTC | 本次arXiv公开区间+08 |
| --- | --- | --- | --- |
| 23036 | 02/26 14:22:17 | 02/27 03:00:55 | 02/27 09:00～11:00:56 |
| 23057 | 02/26 14:42:16 | 02/27 03:01:26 | 02/27 09:00～11:01:27 |
| 23065 | 02/26 14:53:26 | 02/27 03:01:37 | 02/27 09:00～11:01:38 |

## 23036 LLMServingSim 2.0，2+2+2=6，拟Ch56一窄段

[原v1](https://arxiv.org/html/2602.23036v1)blocks36–104实际读。单operator静态profile可在配置稳定时快速估算；prefixcache命中、KV缺页/迁移、动态batch与expert routing改变真实执行图后，profile本身不再决定队列性能。机制把requestrouter/MSG batch-memory policy放入runtime loop，每批根据当前驻留/容量生成operator DAG，将KV transfer、load/store与通信同步显式插入，再由改造ASTRA-sim/Chakra评估拓扑/带宽争用。单decode-block model-device profile需一次采集（作者70B/H100约2.1h），不能把复用profile当零成本或保证全部batchshape/multitenantkernel可迁移。

direct calibration区分time-series与aggregate：A6000/H100时间序列误差5.66%/2.98%，聚合throughput/latency0.85%/1.59%；average小不授tail/局部每时刻准确。vLLM原生GPU prefix block16 vsLMCache host-sharing256不是同cachegranularity；CPU共享两instances可验证其部署，不能推出CXL全球pool或disaggregatedPIM硬件已真测。TPUv6e只single-instance dense可实际校准，其PD/cache为假设仿真。PIM256×1GB/2000MTs、256requests128in512out是模拟；SBI缩小GPU有效batch时无收益且额外耗能，是负侧，不将1.43x/32.3%外推真实PIM TCO。其他simulator不支持配置分开列N/A，支持更广不自动证明在相同配置更快。

4RTXA6000/XeonGold6326、8H100-SXM80GB/TP4、TPUv6e1，Llama3.1-8B/70B、Phi-miniMoE/Mixtral8x7B；通常300ShareGPT请求/Poisson10rps，energypulse与cachebursty另有协议。原73把A6000 capacity写40GB，实际硬件规格/使用cap未解释，不把该字段当独立硬件认证。precision、软件精确revision、tail-SLO误差、profile方差/重复次数、质量保持未披露；operatorprofiler、simulation运行时间与server费用分别付费，较轻Vidur/TokenSim模拟更快。功率active/standby/idle与其他常数项为模型，unit/外推域须另核，不采用“watts/token=普遍节能”的保证。

实际owner `INFER-SCHEDULING` Ch56 1010–1065与1468–1493完整邻接已读：1014–1023已有profile/planner/online三个权限和domain外canary，1473–1484已有taskDAG trace模拟的端到端校准。差额是**缓存/批次/路由决策反馈到下一批operator图，真实迁移/争用作为图的工作而非事后固定服务时长**；拟在simulator小节内一段，保operatorprofile绑定/动态图/平均与局部误差分账、PIM/CXL未证与保守实测回退，不另建硬件综述或机械重复上面的控制权原则。

## 23057 Affine-Scaled Attention，2+1+2=5，拟Ch14一窄段；局部mass/entropy叙述隔离

[原v1](https://arxiv.org/html/2602.23057v1)blocks19–82/85–118/124–125/130–131/135–139实际读。sink减小整体读取而outputgate过滤已聚合结果；原机制在softmax权重上做query/head scale alpha(X)与beta=(alpha_ma−alpha)/N，EMA从0、rho=.9。按所写每query scalar门控，`a_i=alpha*(P_i−1/N)+alpha_ma/N`，是**缩放偏离均匀的部分并保EMA共同分量**；sum a_i=alpha_ma，不等于query-adaptive total mass，也不是改变logit temperature。alpha>alpha_ma时部分a_i可负：N2、alpha=.8、alpha_ma=.4、P=(.1,.9)给a=(-.12,.52)。故不认证非负概率/convex聚合或直接Shannon entropy，alpha=0也保均匀EMA读取、不等精确no-op。公式与71–82所称per-querysum/entropy叙述的shape/mask/normalization解释未齐，**隔离该子命题，不推实现必错或整项D**。实际实现还须明确N为因果允许key支集、bias不重新启用maskedfuture、EMA统计轴与冻结/恢复身份；这些是必要采用条件，不冒称原artifact已核。

所测0.5/1/3B学生fromscratch KD、对应Qwen1.5/Llama3.2/3.3teacher，20BFineWebEdu、seq2048、globalbatch1024、9ksteps1epoch、LR1e−3（先5e−4～5e−3 sweep）、WD.1、100warmup/WSD，lm-eval0.4.9零样本六commonsense+C4PPL。standard/sink、gated＋affine及sigmoid/clippedlinear是直接对照；整体平均有改善不等每项支配（1B PIQA/BoolQ等退）。run-specificMAD spike阈值不能直接统一为绝对divergence次数；k6的affine spike可多于baseline，gradientvariance↓不授全部稳定。仅KD moderate-size，无CE-pretraining/broaderdata/teacherfactor控制；HW/precision、latency/额外backward/EMA通信、重复seeds/CI未披露。10C4短序列诊断不授权“更高entropy=真实相关性/grounding”或无损机制。

实际owner `MODEL-SELF-ATTENTION` Ch14 246–285与405–425完整邻接已读：254–271已有simplex/no-op/null与valuegate分责，415已有signed centered高阶残差，但无**query scale＋EMA DC补偿的非概率权重与总量约束分账**。拟归一化小节一段，不替换旧sink/softmax，不把训练配方数字正文堆砌；注明writtenformula只支持centered-gate条件解释、mask/EMA成本和原baseline回退，需root实际决定局部机制是否足以采用。

## 23065 TransFuzz，2+2+2=6，拟Ch66一窄段

[原v1](https://arxiv.org/html/2602.23065v1)blocks41–53/57–113/122–129/137–171/179–198实际必要读，不遍历9类全部bug报告/artifact。跨CPU/GPU或crashoracle只能覆盖某些silentbug；机制将已确认issue+fix的**API功能、triggercontext、oraclepredicate**分开抽取，经context-free functionality匹配候选target，再改写trigger与oracle，运行instrumentedtest，并分别验bugtype/actualsymptom、无bug假设下oracle是否仍触发、源issue判bugcriteria是否适用于target。真实runtimeflag只是可疑case，不是bugtruth；LLM反侧并未替代developer/文档语义。

直接反例mul的交换律不能迁移给fmod、argmax不传梯度不能迁给amax；clamp空输出oracle与clip正确异常信息不同。instrumentation AST打印可能涉及额外求值/同步，原semantic-preserving声明不授任意Python/DL状态精确等价；NVIDIA A6000/Ubuntu20.04/256GB测试环境、PyTorch2.6/2.7、o3mini提取/4omini生成/4.1mini核验、固定pipeline和3次AND重复均为作者范围。不检查全部CVE、也不由31reportedbugs宣称独立证实全部漏洞/框架无遗漏；precision控制更严格可能漏真bug，初批10无发现即止也不保证剩余top1000安全。

关键negative149：多次flex_attention梯度bug迁multiheadattention的compiled/eager数值差，全部自核通过而developer判合法compiler数值差。78curated(22real/56nonbug)与Table11指标存在分母疑问：.8442/.6552/.9048/.7600同时符合TP19/FP10/FN2/TN46的77/21人口，不能按所写78/22解释为统一精确率或普遍召回保证；采用存在三方法受控比较与该局部反侧，数字暂不并入正式性能结论。100historicalissue pairwise9900含方向重复/共享issue，不是9900独立实验。约89.07USD为作者该campaignAPI账，生成35,909程序/运行/人工最终复核及索引提取不能从文字计费数推出总生产成本。

实际owner `PLATFORM-EVALUATION-SYSTEM` Ch66 364–399与1652–1677完整邻接已读：385–387已有historicalbug→interactionpatterns→executeartifact→independentadjudication，已有generatedtests/oracle/requirement分责。具体差额是**同一源oracle的有效语义条件须在targetAPI重证，运行flag即使复现也可只是新oracle错误/合法数值行为**；拟在historicalpattern段之后一段，用上述三个独立判定接口与一个具体反侧，保predicate权限、实际执行和最终adjudication、费用/漏报/成熟固定suite回退，不制造“有LLM+fuzz”名词gap。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：23065：原必要blocks63–70/102–113/149及采用相关prepared控制/反侧与actual owner独核；Ch66正文406/完整392–414/own5677 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。
