# 第二包末三项：按实际增量结束最低必要投入

root准备，非正式报告作者；只补03-14的Mar13北京时间自然日。完整精确题摘/准入校准和本ID日级日期夹证复用 `SUP_ADMISSION_SECOND.md`、`SUP_DATE_SECOND.md`，不移动旧候选。精确v1原件由 `SUP_ROOT_CORE_MINIMUM_MANIFEST_RESULT.json` 标明三个GET200/URL/字节/2026-10-09T15:53:41UTC。以下是准备者的裁决与必要PRE，尚待非作者实际核验，不自授Books/POST/DAY。没有读代码、复现或遍历无关附件。

## 11395 ARROW：6分具体World Model replay差额

实际完整读§3.1–3.4、§4.1–4.4.1、§5.1人口/图caption、§5.2.1样本效率与§6直接反侧/限制。不是用neuroscience类比解释新增机制：FIFO只有新经验，固定总容量下另一半采用随机key保留最高key的reservoir，保存512步spliced rollout并用reset flag区分拼接episode；每个minibatch对两个buffer均匀采样。该经验训练RSSM世界模型，actor/critic只消费其imagined轨迹。容量是两512序列×512观测共2^19，与DreamerV3/TES-SAC同总容量，不能拿Dreamer原1M默认量宣称本文减少了一半公平对照成本。

六Atari/六CoinRun扰动、default/reverse/two-cycle（后者总环境步同）、五seeds，归一化return基于single-task ARROW/random不是无条件accuracy。旧任务保留与新任务学习速度分账：CoinRun default阈值Dreamer .492M vs ARROW1.638M，Atari default ARROW不能达到选定2.02阈值，two-cycle Dreamer3.113M vs ARROW3.441M；不采用全面样本效率优势。固定50/50及有限两排序，不授动态最优配比或robot/continuous-control推广。虽无显式task ID，§3.4仍用single-task基线给定per-environment reward scale，§6极端reward disparity只学高return任务；不称完全task-agnostic奖励。只采用双人口buffer与reset边界，不采用部署安全、全部无遗忘或模型内部表征优越的因果断言。hardware/precision/完整端到端wallclock及部署SLO未在本次必要证据确认，正文不写性能保证。

2+2+2=6：具体长期/近期经验分配2，经验分布经world dynamics影响imagined controller2，可复用retention/plasticity合同2。actual `MULTIMODAL-WORLD-MODELS` Ch25 398–435完整局部已读，现416/418解释逐组件forgetting与真实replay回退，但没有在有限容量下分配近期FIFO/全局reservoir及跨episode reset的接口。Ch24生成范式/Ch26行动controller开篇交接已读，训练buffer在本World Model链解释，非Agent记忆或训练全章第二owner。具体owner缺口触发必要深入；准备两段插在416/418完整段后、Persistent world state标题前。

### 逐字PRE

逐组件诊断之后，还要决定有限 replay 怎样覆盖经验。只保留近期 FIFO，在任务稳定或必须快速适应时最直接；任务持续切换时，它会把旧 transition 人口逐出，预测器保留能力与 actor 重学都失去原始依据。一条受限分支在固定总容量内分出近期 FIFO 与长期 reservoir，后者给轨迹块随机 key、只保留固定数量的最高 key，再从两个人口混合采样训练 World Model；actor/critic仍从该模型的 imagined rollout 学习。长 episode 可以切成定长块，拼接不同 episode 时保留 reset flag，不能让模型把两段无关轨迹当作一次真实转移。这里是把既有重放原理用于 world dynamics 的数据分布，不是 learned Agent memory，也不改变真实观察与 imagined state 的权威边界。

长期人口会占用近期样本与训练预算，保留旧任务不等于更快学会新任务。[同总 buffer 容量的有限对照](https://arxiv.org/html/2603.11395v1)显示这一取舍受任务共享结构与顺序影响，部分配置的新任务阈值到达反而更慢；固定一半一半不是最优容量定律。方法虽不显式输入 task ID，仍采用按环境预定的 reward scales，极端奖励差异可能让 controller 只学高收益任务。采集、存储/切块、采样与 world-model/actor训练都付费；容量、reset或奖励尺度失配时，应检查真实旧经验覆盖与各组件退化，调整混合人口或回退近期 replay/独立任务训练，不让较低 forgetting 指标签发开放世界持续学习保证。<!-- source-family:SF-2026-ARXIV-2603-11395 -->

## 11397 UGSD：5分标准完成、具体已有覆盖

实际§3.1–3.3/Eq1–4、§4全部Implementation、§5.1直接成本解释/§5.2–5.3/Table5及§6。新增是SEC负载中block最大draft entropy过门才发送，云端在accepted prefix+draftIDs+抽象audio feature上做top-R rank接受，保留连续合法前缀、首失配argmax替换、丢剩余suffix，edge对齐state；纠正后缩block、连续两次全接纳后增block。不是全部token都由target验证，不是ratio/residual校正的exact sampling；entropy不是错误概率或事实置信度，R20校准不授普适正确。FP32双CPUcore Qwen2.5Omni3B/A100 BF16 Qwen3Omni30B-A3B受控emulation，两语言各332录音，caption字面指标不是情绪真值/事实性。18.2%只计draft token上传比例，还反复发送prefix和audio features，不能当全通信bytes或隐私证明；原文也承认feature可能包含speaker/content。7B verifier增益小，仅局部caption质量/费用，不授所有model-size、无线tail或并发SLO。

1+2+2=5，局部任务应用1，edge/cloud发送与确认接口2，可复用有损效用/资源限定2，不借成熟speculation原理加分。actual `INFER-SPECULATIVE-DECODING` Ch48 78–108：confidence直通/likelihood阈值仲裁不是target-law加速，需按声学质量/费用校准与AR回退；644–676明确prefix/rollback身份与网络成本，853–873阐明停止与offload估计/保守fallback。该三条具体正文已承载本次需要保留的“有损条件路由不能冒充exact acceleration、跨云费用/条件独立校准”。R20、SEC模型和18.2%留本报告受限实现证据，不另写第二机制。拟标准完成/已有覆盖/Books新写0，不把主题相同当覆盖；未核实现是否实际只发这些载荷。

## 11447 GCL：4分局部后训练关闭

实际§3.1–3.3/Eq1/3/4/5、AGO两种分派、§4.1–4.2实施与§4.4直接温度反侧、§4.6/§5。原文具体增量是两模型联合监督+batch跨模型语义contrastive+JS概率正则，guide角色按SFT表现取较低LR，温度则独立按参数大小分派2/3；角色与capacity不是同一标签。它是有限双模型目标/超参策略，不是新跨embodiment动作状态合同。小模型能超过guide只授这个人口，两个模型共同学习/同数据不能推出无cost蒸馏；语义cosine/Action-F1与GT图的近似不是独立物理安全。8 RTX8000/ZeRO3/AdamW，两导航dataset，特定对模型/温度反侧及door误判保留。不采用统一温度必须失败、架构无关最优分派或真实机器人安全。

1+1+2=4：单训练配置局部目标/分派1，有限组件1，稳定的受限优化取舍2。保留原准入潜力与具体必要证据，不因已有覆盖/耗时改为EX；identity/date/dedup有效，已关闭/仅报告/Books0。最低关闭不授完整梯度定理或全模型组实证核验，核心以上权限定足即止。
