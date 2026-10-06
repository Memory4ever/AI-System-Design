# LEAFE16843：复原经验到监督动作的有限接口

root仅准备本19既有准入，2+2+2=6不改变；本日公开日期夹证复用SUP_LATER_METADATA_MISSING5_20261011.json:93，不把Submitted当公开。实际[exact-v1 HTML](https://arxiv.org/html/2603.16843v1)完整题摘、§3/Eq1及两CE loss、§4/Tables1–6/§4.5、A Algorithm1和B.1/B.2/B.3/B.4必要实现范围已读。current abs只有v1/Submitted to ICML2026，未见影响本接口的撤回或勘误；不扩会议史、全部图像/示例、代码或复现。

## 必要证据与反侧

§3恢复不是只把context截短：Reset环境、Replay原动作前缀，真实抵达所提议tau，再用经验e条件化新动作，BFS和attempt/depth预算管理分支。反思由同policy提议tau/e，不保证因果根因。成功轨迹的20%做rehearsal，每任务3个branch实例做修复CE；学生仅看原history/q，不读e。Alg1 line11在分支执行前收集refl样本，并无最终成功判定；正文称improved不能理解成每个目标经过终局成功认证。

受限Qwen2.5-7B/72B及Llama3.1-8B/70B交互/CodeContests，LEAFE初始化于GRPO模型再做SFT，而非与GRPO同总训练预算。SFT b128/LR1e-6/2–3epochs，GRPO代码n8/3epochs；训练precision/hardware/seed-CI、完整replay/反思token与墙钟费用ND。B4 EarlyExp为重实现、ACE为扩展且加在GRPO上，不能归因于唯一loss或通用算法优劣。

T1 Qwen WebShop pass1 66.50<GRPO67.45/ACE68.65；ALFWorld两个模型pass1均低GRPO，ScienceWorld Llama22.70<24.25；T2 Qwen72B pass1 17.12<GRPO20.45。Pass128相对较好并非支持集合或能力天花板定理，只是固定环境/采样预算的经验覆盖。T4增加修复CE Qwen14B pass1 37.17→36.50，pass128 67.33→72.00，表明coverage与singletry可反向。T6 LlamaALFWorld加EE pass1升/128跌96.43→93.57；不推 outcome RL必只能sharpen。T3同execution-attempt预算的branch对照未匹配所有反思、replay、模型/训练费。§4.5承认reset可靠及诊断feedback前提，真实不可逆/随机环境不能用文字重建假装复原；ScienceWorld只是交互benchmark不扩大AI for Science研究。

## actual owner 与逐字 PRE

sole `TRAIN-SFT`。实际Ch29 506–530完整teacher-text→privileged branch→contextdistillation、645–680 deployment-derived strategy，及Ch28/30入口已读；前者single-token teacher branch续写不承载环境动作重放+无e原history的纠正action监督，后者OEL全context策略不同。Runtime rollback仍交Agent owner，不复制BFS/commit实现。建议原522后、Context Distillation标题前一段，保持原teacher单分支适用性。

有可复原的交互环境时，修复监督还可以来自真实执行分支，而不只是 teacher 对原 prefix 的建议。一条[受限经验蒸馏分支](https://arxiv.org/html/2603.16843v1)让 policy 从反馈提出回退位置和诊断，先 reset 环境并重放原动作前缀，再由诊断条件化新动作；训练时把该动作配回不含诊断的原 history，并混入成功轨迹 rehearsal。这改变的是监督 target 与部署条件的配对，反思位置不是因果根因，分支产生的动作也不自动取得终局成功资格；只截短文本不能复原环境副作用。须分别保存原观察、重放后状态、诊断来源、target 接纳与 checkpoint，并独立验收无诊断部署下的质量。有限结果中多次采样覆盖改善仍可伴随单次成功率反退，Pass@k 不是新能力支持集合的证明；反思、reset/replay、分支采集与额外 SFT 都付费。环境不可逆、反馈不可靠或修复 target 失真时，保留已验证成功轨迹、原 teacher 监督或运行时受限恢复，不把 offline 蒸馏当线上安全回滚保证。<!-- source-family:SF-2026-ARXIV-2603-16843 -->

静态注：`SF-2026-ARXIV-2603-16843` — [LEAFE exact-v1](https://arxiv.org/html/2603.16843v1)§3–4/Tables1–6/§4.5、A/Alg1及B.1–B.4必要范围。仅环境真实复原分支→无经验history的动作CE与rehearsal接口；target非自动成功、reset/反馈前提、pass1/passk反向和完整费用保留，不授支持扩张、全能力或生产回滚保证；未核全图、代码或复现。

非准备者resume_mar17已独立读取exact-v1必要方法/两CE、T1–6反侧、A/Alg1和B1–4、current事件页，并实际顺读Ch29 506–540/645–680及Ch28/30入口；Source、唯一owner具体差额及上述逐字PRE通过。target非自动成功、Pass@k非支持定理、完整费用界限保留。root接纳，只own Ch29此一段及静态源注窄写；实际非writer POST仍待，不计安全完成或DAY。

## resume_mar17 非writer实际 POST

已实际顺读Ch29 513–545完整teacher续写/特权单token分支→新524→Context Distillation邻接，以及1269–1282 Review notes开头/本人静态源注1275和PriCoder、SeGP-CL邻注。新524与本packet逐字PRE完全相同，source-family仅正文与静态注两处；回对本人已独核必要v1方法/两CE、Alg1 line11先收样本后执行、Tables1–6直接反侧及B1–4，reset/replay真实状态前提、无e部署history、target非自动成功、pass1/passk分账和完整费用/回退边界均准确。静态注所列范围与未核代码/全图/复现的限制真实，不添加动态人员收据。限定Books diffcheck通过。一次非writer实际局部POST PASS，可由root接纳释放该family Ch29窄锁；仅本项，不授整日DAY或未采能力/支持集合/生产回滚保证。未修改Books、Report、LS或其他家族。
