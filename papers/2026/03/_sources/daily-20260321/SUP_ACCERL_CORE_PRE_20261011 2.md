# AcceRL18464：必要Source/actual owner/最小PRE

resume_mar18准备，仅03-21补BJT03-20；原65完整题摘/root独校潜力复用，不扩发现。尚未非准备者Source/date/PRE、无写锁，不计safe/DAY。此前消息18364为口误，实际唯一ID2603.18464，不创造另family。

## 身份/新增命题

[exact-v1 abs/history](https://arxiv.org/abs/2603.18464v1)完整AB/currentheader/history实际读完；[exact-v1 HTML](https://arxiv.org/html/2603.18464v1)为本次原证。v1 Submitted03/19T03:50:45Z，v2Submitted03/20T01:43:50Z、currentv3Jun12；未见明确withdraw/correction/accepted先稿信号，不按版本号扩revisiondiff。实际[DataCite](https://api.datacite.org/dois/10.48550/arxiv.2603.18464)created03/20T02:13:14Z、registered15Z/statefindable；v1Updated03/20T00:33:05Z、v2Updated03/23T00:21:08Z、v3UpdatedJun15均不同事件。沿本批官方availability/DOI夹证只限定BJT20 arXiv首版事件，不把同日本次v2Submitted冒公开或无其他先稿。

同步VLA收集/更新受step/episode/cluster尾部约束→policy、observation/reward模型各自trainer/inference池与真实/imaginary双buffer、不同更新频率→不仅policy stale，还须区分真实转移训练预测/合成轨迹训练policy的资格和模型版本。拟2+2+2=6，只此预测—rollout—learner接口，不给旧三池/批处理/GIPO/全局advantage原则或200×宣传加分。题摘增量已明确后仅读必要机制/直接反侧，不默认逐项全文。

## 必要原证与反侧

实际§3.1–3.5/L132–220、§4/L221–239、§5必要配置/公式、§6.1–6.6/Tables1–2及§7/L280–353支持与直接反侧足够；未核实现/复现、全部曲线图像/引用工作和后两版本差异。

- §3.1完成轨迹推replay、trainer并行采样，每batch后NCCL向inference actors同步policy；§3.2环境observe异步请求集中pool，|Q|≥B或最早请求等待≥Tmax触发batch。timeout是dispatch条件，不是逐请求端到端deadline或所有阻塞消除。τ保observation/action/reward、behavior logits μ、value/bootstrap/done；必要原文未披露完整policy/model revision标记与atomic publish、跨请求checkpoint切换/恢复协议，不补造实现。
- §3.3重算最新critic值/GAE、全局advantage三统计AllReduce、GIPO log-ratio Gaussian停止梯度trustweight；并非全部中心语义无barrier/critic正确/任意stale等价onpolicy。§3.5background prefetch重算有其自身revision快照/下一batch消费时间差，near-zero loading不含全部tensorization/前向费用。DWR failurewindow+ε仅给非零采样，不证明防遗忘。
- §4为observation/reward各配独立trainer+inference，真实转移入Bwm训练二者，实际episode内帧作短horizon imagination起点；imaginary轨迹入Bimg训练policy。替代的是有限训练experience生成，不是实际观测/环境真值。Mobs预测nextimage、Mreward预测success/termination，policy与两模型不同Tobs/Treward更新并按实际更新同步；没有完整joint revision/predictedlabel校准、真实与虚拟完整人口混合recipe，不将共享pool接口称高保真证明。真实环境在评价是MuJoCo/LIBERO，非真实机器人试验。
- Eq13 shaping为Φ(s′)−Φ(s)，而Eq4另含γ；必要原件没有声明γ=1与terminal potential条件，故不采policyinvariance。γ<1时不等标准γΦ(s′)−Φ(s)；有限horizon即γ1也须terminal边界，rewardhead又是预测proxy。Eq12与文本训练supervised/likelihood-style日志不支持Fig5声称“analyticgradients from differentiableWM”；不编端到端model梯度更新policy。方法RL模型间合成数据接口可与这些强claim独立分采，待非preparer裁。
- §5actionhead只切256action词表/保持原weight行，新的归一和valuehead/tokenobjective多项联合改变；tokenratio与整chunkratio不是数值logspace实现的无条件等价，“precisecredit”不采。GIPO是既有方法，不给本篇旧成熟机制新分或重新全审priorproof。
- §6H2001→7trainerGPU/ZeRO2，14.13→104.22SPS（约7.38×）同时每GPUmicrobatch因状态分片增大；不是固定perGPUbatch纯asynchrony加速或所有瓶颈消除。rollout64近线性是有限曲线声明，inferencepool GPU/shape、TP、precision、totalhardware/allstage预算/总wallclock/尾延迟/CI等未完整披露，不外推生产。
- Table2 LIBEROGoal98.8低于SimpleVLA-RL99.2，是“全部category都优”直接反侧；共同代码/data/seed/checkpoint/训练预算未齐，不归接口唯一因果。WM评价特意弱BCcheckpoint约.6初始、1000offline轨迹预训练，10k环境步/.8和<400updates的曲线没有matched全部offline/model训练与GPU成本；200×不是零预算或全部sampleefficiency。Fig5return/评价独立population细则未完整披露。
- §6.5criticrevalue与6.6GIPO有限curve不授任意stale稳定。L343–344作者明确最初成功短episode先到形成乐观统计：这是完成人口偏差，不被value重算/importance单独消除；强“formalguarantee”在本必要原文没有对应完整新证明，不采用。所有候选trace/推理、预测训练和真实采集费用须同账。

## Actual sole owner与差额

sole `TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)完整1249–1290实际读：1261trajectory/policy/environment/reward/actor身份与freshness，1277已有VLA异步offpolicy/queue/恢复分责，1280真实fleet完整episode上传/episode间换policy，1282–1284完成顺序偏差和窗口。现文实际承载三池异步/到场偏差，不把这些当新增；未具体承载observation/reward与policy三种独立更新面、真实Bwm监督与Bimg策略消费、真实起点短想象轨迹资格。拟在1277完整D-VLA语义段marker后/1280真实fleet前一段，不接管算法owner或物理动作。actualCh25完整75–110有真实采集/worldmodelreplay→imagined训练边界，但非三个训练/发布时钟的分布式payload资格。Ch35/37开篇交接已actual读。

## 一段literal PRE（待非preparer）

若 rollout 的环境也由可训练模型提供，异步边界就不止 behavior policy 一种版本。[一条受限分支](https://arxiv.org/html/2603.18464v1)分别训练并发布 observation、reward 与 policy 模型：真实环境转移进入预测模型的监督 buffer，真实 episode 的观测提供短 horizon 想象起点，而由预测观测、奖励和终止信号组成的合成轨迹进入 policy buffer。三个更新频率可以不同，这让模型内采集不必等待完整物理 episode，却也让一次梯度同时依赖行为策略和两个预测器的状态。Runtime 因而应保留真实/合成来源、起点、horizon 与对应模型身份；仅重算最新 critic 或修正 policy ratio，不能把预测 reward/termination 变成真值，也不能消除成功短 episode 先到的样本 mix 偏差。独立常驻池又增加模型训练、权重发布、跨池请求、buffer 和预测误差费用；所测超线性 trainer 吞吐同时增大 micro-batch，较少在线环境步也预付了离线 world-model 数据与训练，不等端到端免费加速。奖励差分保持原 policy 最优的条件与完整版本提交协议没有由该接口得到认证。预测支持、版本或全账不可信时，限制想象 horizon，补真实 replay，并保留固定预测器、直接环境采集和已有同步/有界异步路径，不能让快到的合成轨迹越过 objective admission。<!-- source-family:SF-2026-ARXIV-2603-18464 -->

静态注：- `SF-2026-ARXIV-2603-18464`：[AcceRL exact-v1](https://arxiv.org/html/2603.18464v1)，必要§3–6/Eqs1–13/Tables1–2和§7；仅真实Bwm/合成Bimg与三个模型更新/消费分责。保revalue非truth、提前完成人口偏差、Eq13 shaping/analyticWMgradient桥未采用、Goal反退、ZeRO2/microbatch混杂和offline预付/全费；不授任意stale稳定、200×端到端/生产安全或完整checkpoint协议，未核代码/复现。

请root非准备者裁支持与强claim是否可独立分采/actual差额；已有覆盖需具体论点，不为新框架强造diff。如中心不可分仅保争议，仍留原分数/反侧，不降分缩池。

## 非准备者必要 Source / actual owner / PRE 裁定

root实际v1 §3.1–3.5全部132–220、§4全部三训练面/Eqs12–13、§5关键接口、§6/7全部人口/两表/单项反侧/完成顺序偏差；独立DataCitecreated03-20T02:13:14/registered15和三个版本字段，与原本日availability相容。actualCh36完整1249–1296、原onePRE/static逐字核。有限Source/date/具体soleowner差额/PRE PASS，6分不变。仅三个模型更新和真实Bwm/合成Bimg的训练资格接口新增；原三池/版本/到场偏差已承载，不重复算增量。

Eq4 γ与Eq13无γ/terminal条件不能导policyinvariance，§4数据消费与Fig5 analyticgradient并无实现桥；14.13→104.22同时microbatch扩大且1000offline预付，Goal98.8<99.2，未授消除所有barrier/高保真/200倍端到端。构造可与这些强claim独立采用。PRE“完整物理episode”请准确改为“完整真实环境episode”，紧邻说明本文真实采集对照是MuJoCo/LIBERO而非真实机器人；其余受限措辞可原样。必要支持与反侧够即停，不扩大代码、旧GIPO证明或全部版本。

授resume_mar18 soleCh36原D-VLA完整段后/真实fleet前窄写修正onePRE与自身static；未计safe/I/DAY，写后root一次actual完整局部/注POST。

## 授锁后实际写入（待nonwriter POST）

已按root指定将“完整物理episode”准确改为“完整真实环境 episode”，紧接明确MuJoCo/LIBERO非真实机器人；其余原受限接口/反侧不变。actual Ch36新1280一段、自身2194静态注；作者完整1268–1297与末五行实际顺读，marker/本人注各唯一，限定diff-check空。采用三个训练/发布面与Bwm/Bimg资格，不重复原三池或到场原则评分。仅写已授family，无新source或全附件阅读；root nonwriter POST之前不计safe/I/DAY。

## 非 writer 实际写后验收

root 完整读回实际 Ch36 1268–1297 与本人末注：新段位于已有 D-VLA 异步语义之后、真实机器人 fleet 的提交边界之前；三个更新面、真实/合成 buffer 的训练资格及 MuJoCo/LIBERO 非真实机器人限定均实际存在。旧异步原则、fleet 提交和到场偏差正文保持，PRE 的预测误差、费用与强结论边界未丢失。实际正文、完整局部交接及本人末注 POST PASS；释放本 family 的 Ch36 窄锁，可计实际 Integrate。只验单篇写回，不授整日 DAY 或其他 family 验收。
