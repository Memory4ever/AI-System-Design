# Apr14 第十四批五项有限非作者采用复核

复核者：apr02（非Apr14报告作者、未写本批Books）。2026-09-27实际重开下列官方exact-v1必要局部，并对读相关当前章节；不检查全日日期/来源、所有附件或复现实验。三项仅报告、两项窄缺口提案通过；提案不是实际整合，仍须授权写入及写后验收。

## 10135 Think in Sentences：5分标准，仅报告通过

实际读[官方v1](https://arxiv.org/html/2604.10135v1) §2、§4.1–4.3/§6。固定长度与随机同数分隔对照支持输入结构而非仅多token的受限效应；attention可视化不证明唯一因果。对读Ch75结构化pruning/derived view，所测精确配方未有长期统一优选证据，不能冒称整算法已有覆盖。保SaT/额外token/SFT成本及规模边界，不采用free-lunch与句子唯一自然推理单元。

## 10158 Tracing LC0：5分标准，仅报告通过

实际读[官方v1](https://arxiv.org/html/2604.10158v1) §2、§3/Algorithm1与§4所需干预。MLP transcoder与稀疏attention替换得到近似图；规则验证和被选feature限制解释范围，部分高precision伴极低recall。对读Ch14:228–232诊断/多点干预及Ch17组合交接，LC0局部结果值得保留但不建立通用LLM完备字典，不因棋类/小模型拒绝；不用棋步概率替代世界正确率，保持仅报告。

## 10180 Tessera：7分深入，Ch49窄采用提案通过

实际读[官方v1](https://arxiv.org/html/2604.10180v1) III-A–D、IV及V必要配置。PTX访存区间→保持顺序RAW图→异构kernel placement与send/recv/event、跨迭代副本/delta，是Ch49 phase/backend计划尚缺的细粒度依赖分支，Ch55仍拥有PD阶段。间接访存同GPU回退、collective原同构组、full weights复制及MILP无显存容量约束明确；不由离线profile推任意地址/图均可异构化，不外推平均吞吐或窗口队列策略为完整SLO。可最窄嵌phase-aware runtime，固定同构执行继续合理；未写后。

## 10182 Credit-Budgeted Coding：5分标准，仅报告通过

实际读[官方v1](https://arxiv.org/html/2604.10182v1) §3.2–3.3/4.1–4.5。API/test/hint/time加权credit、wrong submission penalty排序与停止合同不同；48题Bronze资格筛分母，跨API令时间系数0。对读Ch66subject含budget/environment/adapter与Ch70实际goal成本，比赛协议是有限评价实例，非平台真实账务，也不证明纯策略瓶颈。保五次重复与swarm成本，标准仅报告，不声称完整机制已在书中实现。

## 10187 WaveTune：6分缺口深入，Ch49窄采用提案通过

实际读[官方v1](https://arxiv.org/html/2604.10187v1) §3.2–3.3/4.1–4.5/5.1–5.5。Ch49当前typed expression/shape/kernel profile只给一般合同，尚无wave分桶双线性cost与micro loop-anchor表的联合校准分支。macro/micro受资源耦合，不是独立全局最优；五GPU分别profiling，MHA/单组近似、Step在MI355X退步及离线摊销保留。Prefill为Qwen3-30B-A3B/SGLang0.5.8/单GPU/batch4/512～16384输入，不推全部服务收益；近似失配回实测，不能采用消除取舍。窄提案通过，未写后。

## 交付边界

五项必要来源与实际owner判断通过，未写共享Books、未改Apr14作者报告或notes，未验收日期/覆盖/整日Gate。10180/10187可交作者最小正文写入，其他三项保留具体有限证据即可，不扩附件或候选池。

## root实际写入后的有限复核

apr02重新顺读Ch49实际新增正文及两侧衔接，复用上述未变的必要v1依据，不再重读附件。10180位于phase-aware backend后、“从Linear语义到GEMM执行”前的“异构Kernel Placement先证明依赖，再决定放置”两段（当前273/275行）：保持原顺序RAW图、复制delta与等待职责明确，间接地址/collective回退、full weights容量需另验及profile不保证SLO均保留；与前一phase-level选择、后一kernel执行粒度顺接。实际写后通过。

10187位于GAC硬件对齐shape选择后、Tensor Core分层前两段（当前444/446行）：wave桶与loop-anchor成本近似及资源耦合未误写独立最优，五GPU重新校准、MHA代理、MI355X退步、离线摊销与Prefill-only/batch4边界就近保留；在library heuristic→shape联合选择→更细kernel选择的原链中成立。实际写后通过。两项均有真实Source Family正文标记；本轮只读书稿，未修改Ch49，不代替Apr14全日Gate或实验复现。
