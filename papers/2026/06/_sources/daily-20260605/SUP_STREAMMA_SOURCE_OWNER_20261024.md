# 05158 StreamMA：必要Source/实际owner与最小PRE提案

作者supp_20260605_author，2026-10-24。恢复重读当前AGENTS/适用合同/Prompt/来源/ROADMAP、Books公共三上下文与仅本日停点，实际采用R23–24既成事实：04193已I，累计新增I6，旧Kimi另保/DistIL7争议不变；无第三旧Source/POST。05158准入与Jun04联合日期R13–14复用，不重AB/date。本轮只推进本单篇，不等04945，也不扩机构/宽导航。

## 精确来源与读域

[官方HTML exact-v1](https://arxiv.org/html/2606.05158v1)实际返回`No HTML`/转换不可用页，6399bytes原件保留；转取[官方PDF exact-v1](https://arxiv.org/pdf/2606.05158v1)，974790bytes/28页，实存`SUP_2606.05158v1_20261024.pdf`。使用PDF技能只读提取；实际像素核p3 Alg2与p8 Fig4/5，未把抽取文本当图形布局。必要读§3–4/§6及A.1/A.2核心定义与证明接口、A.5–6成本/流水条件、A.7–9设置/伪码/prompt及A.11–12风险/人口。A.3–4只定点定位固定上游perturbation来源，不扩全部化学推导/参考文献；science题目是通用推理协议评价切片，不把领域机制另收。未运行artifact或复现API调用。

## 核心接口及不应补造的执行语义

§3.1/Alg2/p3、A.8/Alg3/p26：root一次streaming调用，以END_STEP边界发出完整step；各node FIFO逐条取上游消息，append context后再次调用LLM，自己输出亦append保历史。正文将non-root描述为S次调用、共用prefix可复用KV；不是向同一次已运行decoder任意插入新context，也不是token逐粒透传。DAG向每个successor发送，多前驱按到达顺序处理，无全前驱barrier。Alg2/3抽象stream循环与“每消息一次响应”的实际粒度仍须实现核验，本文只采用有界step交接设计，不伪称实现已审。

已有文字只讲部分上下文影响质量，本增量还改变后续步骤开始时机、累计上下文与调用数量。前缀可能尚会被晚到纠错推翻；原协议没有给出通用版本撤销/已发副作用回滚、queue背压、close/cancel与不可逆action提交协议。由此要求runtime保存边界/顺序并独立处理失败是工程推断，不是论文已验证分布式一致性。只适用于可step分解的推理任务，非开放creative、单token分类或外部effect安全证明。

## 质量支持、反侧与理论权限

§3.2/A.2将上游step正确概率pj、正确/错误带来的平均增益δ/损失ε参数化，采用位置无关加性期望，把stream看前缀、serial看全串，得head/mean/tail weighted sCorr排序。sCorr是理论step correctness量，不是直接已证明任意LLM终态accuracy定理；假设不能由更早位置自动满足，也不能由短prefix自签“更可靠”。不采用全球首创、普遍protocol selector或任意DAG严格质量保证。

§4.2.3固定上游clean/perturbed两条LLM构造轨迹，6种代表mask、每mask100次下游试验：污染tail时Stream可高24pp，污染head时可低36pp。它直接支持“位置依赖可逆转选择”，不是天然轨迹总是head强tail弱的因果证明；构造轨迹还参考gold/错误答案。§4.2.2只有一个GPQA case加模型judge，不能普遍识别何处开始错误。主Table1三拓扑均值较好也有逐cell退步（GPT tree LCB-T 99.25→99.17）。

§4.3.1/像素Fig4在HMMT26、GPT-5.4 medium、A/S2–64网格、每cell4次、cache disabled；S由prompt改变不是同token/调用预算无成本拆分。热图有明确反退：A32时S32→64为73.5→69.7，A16时S16→32为74.3→69.7；均值也非严格单调。因此不采用标题式“每agent step增加必同时提升质量/效率”的普适scaling law。

## 实验与成本边界

§4.1/A.7/A.9/A.12：Claude Opus4.6 high与GPT-5.4 medium商用API、provider默认解码/OpenCompass；8 benchmark含30题AIME25/26、33题HMMT26、198题GPQA-D，HLE/LCB依配置加载不补造n。普通cell3runs，小数学集8；judge需时用GPT-5.4。Stream与Serial共用角色prompt基础，但Stream加END_STEP及root solver前言，不能声称完全零prompt差异、同总预算；无完整CI/等token预算。硬件、部署precision/quantization、service batch/排队/并发容量/SLO为Not Disclosed，输入输出长度随任务/step变化，不能当固定吞吐基准。

§4.3.1的26.9x是“各agent API调用耗时之和 / Stream实测wallclock”，不是独立实跑Serial耗时比；远端queue/共享资源不由此消除。§3.3/A.5理论上限从chain finish recurrence与可比workload近似得到，AS/(S+A−1)还需decode主导、prefill/cache读影响弱，不能拿成生产加速保证。A.6按全部input/output/cache价计费，模式output ratioρ、prefill α、cache β会改变符号。文中A=S4/ρ≈1数例full cache为0.925ρ、no-cache为1.375ρ；即缓存可使例子从便宜转贵，不采现代stack已普遍达到full hit的宣传。

§4.3.2 Fig5为A3/S3 chain、Claude、HMMT、N1/4/16 replicas＋majority、4runs。h0→h1价格带是cache-hit情景成本核算，不是实测cache改造、硬件加速或无损生产保证；API价为文中历史条件，不查询或外推当前报价。即便输出费用主导，所有额外prefill、cached读、调用/排队、buffer、重复修订与最终验收仍付费。

## 评分/actual owner与精确提案

2+2+2=6保持：新增是通信粒度改变下游执行时机的step/FIFO接口及早错传播反侧，跨agent/runtime成本边界可长期复用；不把成熟pipeline原理或API版本名计分。因Ch82执行时机知识缺口及安全反侧，深入必要域而不全附件。

唯一owner `AGENT-MULTI-AGENT`，Ch82 `**Pipeline**`现仅“固定角色顺序，实际更接近Workflow”，未具体承载同拓扑下full-response→step handoff、重入调用和质量/时延/费用的分离。实际读Ch82典型拓扑、通信receiver-interrupt与conclusion-compaction相关组及邻Ch81/83开头；interrupt是接收者停发送再接轮次，不等step每到就并发下游；已有共享board是worker读部分发现，不提供本接口的调用/时延代价。Ch81保durable control/effect，Ch83保连接协议，不复制新owner。

建议仅在Ch82下列完整前段之后、完整后段之前原位补两段；无新Books授权、未写正文，待非writer必要Source/actualowner/PRE。

前完整锚：

> 固定角色顺序，实际更接近 Workflow；不应仅因每步使用模型就称为自主 multi-agent system。

拟新增literal两段：

> 同一推理拓扑还可以改变交接时机：完整答复易保留晚到纠错，却让后继空等；可分解任务则能在一个reasoning step完成时送入后继FIFO，让后继读取当前前缀并生成下一份响应，与上游余下生成重叠。StreamMA的受限分支让下游按收到的step反复调用、累计自己的历史，多前驱消息按到达顺序处理，不是在同一次decoder中任意插入上下文。step边界和暂定内容并非事实或commit，晚到纠错、取消和不可逆effect仍须独立runtime规则，不能由无barrier推出一致性或安全执行。
>
> 早交接也会更早传播错误：受控tail污染时流式可受益，head污染时却可明显输给完整交接；位置加性模型的step-correctness排序不是终态正确保证。更多step还增加调用与累计prefill/cache读，有限网格有质量反退，不能当普适单调scaling law。所报调用耗时之和对流式wallclock的比值不是独立Serial实跑加速，full-cache价格带也不是生产命中率实测。应分别验质量、真实墙钟与全部调用费用；早步不可靠、晚纠错关键、队列或预算不合时，保留完整交接、较粗step和单Agent，不因提前启动就批准结果。<!-- source-family:SF-2026-ARXIV-2606-05158 -->

后完整锚：

> 部署前选择图，也要区分无扰准确率与受扰后的退化曲线。固定节点数和边上限时，可让每轮各 Agent 独立以概率 $p$ 给出随机回复，测绝对性能 $F(p)$，再用 $R=\int_0^1F(p)\,dp/F(0)$ 比较相对韧性；R 高不说明基线已足够好，$F(0)=0$ 时该定义更不能使用。一条受限分支先用 task-aware GCN 预测多个扰动点的正确率，作为图生成器的训练代理，再固定图，用邻居 prompt 及 correct→wrong、wrong→correct 样例优化各角色 prompt，学习何时借鉴或忽略 peer。图与邻接条件由此成为两个阶段的控制对象，而非增加 Agent 就获得容错。<!-- source-family:SF-2026-ARXIV-2601-04694 -->

## bounded交接

本单篇必要层与两段PRE提案已就绪，不等04945；非writer必要Source/owner/PRE尚未做，无新授权/Books SAVE/POST/I。HTML格式失败已由exact PDF恢复，不冒外部受阻；机构/剩余有限发现题摘ordinary保持，当前新增I6+DistIL7争议，旧Kimi另保、未DAY。未改State/index/他日/共享Books正文，未stage/commit/push。

## 当前R25–26实际采用与真实SAVE

本轮恢复重读当前合同/Books公共上下文/本日停点，实际读回R25–26。reader R25必要Source/actual-owner/原两段PRE通过；root明确新窄授Ch82 Pipeline完整段后/受扰图完整段前原两段逐字不变及本人true-H2注。已实际apply_patch保存并真实完整自读新增两段、完整直接两侧和本人注；与写前完整Ch82快照限定核对只增加两正文段及本人一注，原其他内容逐字保持，正文family marker恰一处，原literal两段逐字存在。当前待唯一非writer actualPOST，不预I/DAY；既成新增仍6I、DistIL7争议，旧Kimi另保。04945/机构/题摘ordinary保持，不等POST扩Methods，交root即释放写入阶段slot。未改State/index/他日，无stage/commit/push。

## 当前R27已成事实

reader R27唯一非writer actualPOST通过、本项整合生效、窄位释放，累计新增I7；R28本批保存态窄核通过。作者仅行政同步README/本人注及记录，不第三Source/正文/POST，旧Kimi另保、DistIL7争议/未DAY不变，后续只04945必要层与机构/有界题摘ordinary。
