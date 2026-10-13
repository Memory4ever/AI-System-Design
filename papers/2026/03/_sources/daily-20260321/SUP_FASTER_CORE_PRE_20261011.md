# FASTER 2603.19199v1：必要证据与逐字 PRE

本材料仅服务 03-21 补 03-20 自然日。准备者/拟 writer：root；非准备者 Source/PRE 与非 writer POST 尚未通过。已通过本日首批准入及日级 arXiv 日期夹证；不重算旧候选或扩大日期。本项拟 2+2+2=6，因实际长期接口缺口深入审阅相关内容，而不是把近端单步的宣传倍率当贡献。

## 实际原证范围

[exact-v1 HTML](https://arxiv.org/html/2603.19199v1)：§3 反应定义/同步与异步假设，§4.1–4.3/Eqs5–6、§5.1–5.3/Tables2–4，补充 D.3/D.4/Table6–7、E.2/Table10、E.3 与 F 的直接训练/部署反侧。只读支持本项接口与限制所需部分，未核代码、复现、全部附件或全部图像点值。

- 同步和异步分析均固定推理/执行周期，事件发生相位被假定均匀；“事件随机”本身不足推出均匀分布。Table2 的 expected reaction 与 Table3 的概率/严格优势是该分析模型结果，不是实测网络 tail、任意环境响应分布或物理安全证明。
- 标准 flow action expert 对整个 chunk 共用一个时间步。HAS 将其改为按动作位置的向量：hit time 随位置变化，局部进度 `tau_i=max(0,(rho-u_i)/(1-u_i))`；设 `u_0=(N-1)/N` 后近端首动作可一轮 action-expert 更新完成，远端继续去噪。TTFA 仍包含 VLM 编码，不是整个 VLA 变成一轮或端到端得到 N 倍收益。
- 训练按概率混合 HAS 与原 constant schedule。只用 HAS 会使近端训练输入常为真值且扩大预训练/微调差异；Table10 的纯 HAS/混合参数均出现长程退步。“没有额外训练成本”只表示纳入原微调路径而非可忽略适配训练、无需微调或零新增系统开销。
- server 立即发出已完成位置，client 追加 action buffer；持续运行要求动作获得率足够，不能由 streaming 名称承诺无 underflow。只生成实际执行 prefix 所需位置后可提前停止，未执行远端被丢弃。同 chunk 后续动作继续消费同一 VLM 表示，不是每个动作都得到新观测。
- 实测绑定 π0.5/X-VLA、RTX4090/4060、30Hz；实机为 AgileX Piper 与有限 table-tennis/pick-beverage/fold-towel任务。D.4 LAN/websocket，部署 d/s 稍增以容纳 network/local processing/I/O，而非正式 worst-case budget；Table6 披露各模型/任务 batch/horizon/训练 steps。推理 precision、服务 batch/concurrency、tail SLO：Not Disclosed。不要把训练 batch 当 serving batch。
- Table4 π0.5 LIBERO96.9→96.5、CALVIN4.313→4.292；X-VLA98.0→97.0/4.151→4.058。仿真质量轻微退步且不被真实网络 latency 影响，不能用它授无损控制。E.3 X-VLA duration仅成功rollout，与主图人口不同；Kinetix为4层MLP不是VLA，不能混作大模型实机证据。

## 实际 owner 差额

唯一 owner `MULTIMODAL-EMBODIED-VLA`，Ch26。实际顺读 Latency 前导、Streaming局部完整段与后续 Fast-Slow/Action Chunk；Ch25结尾是环境预测/证据，Ch27开头负责样本/训练分布，不复制生成器动作时间语义。

已有 Streaming 写 observation/buffer identity、rolling denoising更新观测与旧KV晚步接管；Action Chunk 分预测长度/执行prefix。尚未解释**同一次 flow 推理中按动作位置分配去噪进度，使近端先发布、远端继续，以及这必须和混合时间步微调共同成立**。只补此窄差额，不能把成熟 controller/缓存安全原则另算本项新贡献。

## 两段逐字 PRE

插在 Streaming 节“固定 observation window…”段之后、“把整个 action chunk…”段之前，使固定观测的近端先生成与下一分支跨观测 rolling 明确分开。不删除原文。

流式接口本身还不能让近端动作先算完：若同一 chunk 的所有位置共用 flow 时间步，controller 仍须等到整段去噪结束。一条替代分支在同一次观测条件下，为各动作位置分配不同的去噪进度；近端位置先到终点即发布，远端继续迭代，需要执行的 prefix 全部完成后可提前结束本轮。首动作只用一轮 action-expert 更新，仍须先支付 VLM 编码；后续动作继续消费本轮表示，并非每步重新感知。它也不是纯 serving 改动：微调时须混合位置相关与原统一时间步，避免近端反复读真值输入和预训练时序失配，不能把改采样器当作无需训练的通用捷径。<!-- source-family:SF-2026-ARXIV-2603-19199 -->

这条分支以调度适配训练、分段发布与 buffer 协调换取较早动作和较短重规划间隔；动作获得率不足仍会 underflow，局部更快也可能损害长程质量。[FASTER 的受限对照](https://arxiv.org/html/2603.19199v1)只涉及 π0.5/X-VLA、RTX4090/4060、30Hz 与有限实机任务，LIBERO/CALVIN 的若干质量指标退步。其反应时间分布依赖固定周期和均匀事件相位，不认证网络尾延迟或物理安全；完整编码、训练、传输、controller 与重规划均计费。发布动作仍应绑定本轮观测和已执行 prefix，controller 保留逐步执行与中断权；质量退步、动作迟到或环境变化超出适配条件时，回退同步完整 chunk、短 horizon 或已验证低层控制，不由近端单步授安全。

## 拟本人章末静态注

- `SF-2026-ARXIV-2603-19199` — [FASTER exact-v1](https://arxiv.org/html/2603.19199v1)，必要§3–5/Eqs5–6/Tables2–4、D.3/D.4及E.2/E.3/F直接边界；同观测位置相关flow时钟、混合微调和prefix早停的有限接口，保留VLM成本、长程反退、恒定周期/均匀相位假设及buffer条件。不授无损、网络tail/物理安全或代码核验/复现。

## 下一步

非准备者必要 Source/actual owner/逐字 PRE 裁决→通过后 root 仅写两段及本人静态注→非 writer actual 局部完整顺读与本人尾注 POST→作者同步报告/本日停点。此笔记不是本日 DAY。

## 非准备者必要Source / actualowner / PRE裁决

2026-10-11 resume_mar18独立实际精确v1 §3/固定latency和eventphase反应定义、§4.1–4.3/Eq1–6与mixedschedule/streaming/earlystop、§5.1–5.3/Tables2–4，必要D.3/D.4/Tables6–7与E.2/E.3/Tables9–10直接质量/费用边界。actualCh26 814–864完整latency/控制、918–964完整Streaming→rolling→FastSlow→ActionChunk，Ch25现结尾正文和Ch27开篇交接分别属环境证据与训练人口。不是重复准备者笔记代Source，不读无关附件/版本diff，未核实现/复现。

**必要Source/soleowner/两段原逐字PRE和本人静态注正式有限PASS。** Eq5–6/混合微调与当前observationalrepresentation/首AEstep/prefix早停形成独立机制；原packet未把u0的单步扩大到完整VLM或新观测，不把constantlatency+uniformphase理论结果变网络tail，不授zeroadaptation/长期质量或物理安全。原PRE在932固定观测精确性后/934跨观测rolling前，分别保同观测位置时钟与更新观测buffer，完整两段衔接成立，无需改PRE。

评分定点纠正：本轮初判DD3曾把“平滑异步=及时反应”当待纠结论，但actualCh26 **855已经显式‘执行状态对齐仍不保证策略及时响应新观测’且‘不以接续平滑代替控制安全’**；847亦已有tail/jitter要求。该旧机制不是本项新纠错贡献。实际新增命题为同观测位置相关flow时钟/混合schedule/prefix早停的重要替代设计，故DD2+Reach2+Durability2=6与原packet相符；定点深入仍因明确知识缺口/采用边界，不因减少工作量或实验反退降分。原7初判依据及实际纠正理由保留于此，最终Report按此新证据同步，不移动旧候选/窗口/连续§4。

Table10混合p=.5仍CALVIN4.058<baseline4.151、pureHAS3.112；D.3真机dmax10只覆盖所定义333.3ms窗，D.4略放大d/s只是配置，不是最坏预算；E.3仅成功duration不跨主图比较。首动作的参数索引/encoding、训练8A800与推理RTX分开，static已保必要边界。未授实际写后POST/DAY；root协调此family窄锁后可写，写后一次nonwriter完整邻接/静态注POST。

2026-10-11 resume_mar18一次nonwriter actualPOST正式PASS：root获窄锁实际写Ch26两段934/936及2236静态注；本人实际完整924–954上下两侧（固定观测/flow→新两段→跨观测rolling→旧KV接管/FastSlow）与末尾2230–2236本人注/邻注逐字回原PRE和有效必要Source。流时钟、混合微调、单步只AE而VLM仍付费、同观测/underflow/长程退步与独立controller/均匀相位限定准确；marker/static各唯一，限定diffcheck无输出。不改静态注验收身份，不预支DAY。
