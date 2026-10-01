# 2026-09-23 新增 Source Family 定点证据与 Books 判断

访问日：2026-09-23。以下 arXiv 身份均出现在官方 2026-09-22 New 公告（北京时间 09-23 08:00，本日报窗口内）；HTML/PDF 顶部 `Submitted` 是投稿标记，不单独证明最早公开。若之后查到更早可证的作者公开 artifact，应移交真正 owner 日，不重复评分。

## 2609.24194v1 — 评估分数的表面残差化

- Primary：[exact-v1 HTML](https://arxiv.org/html/2609.24194v1) §2–7、Appendix；Evidence Level：作者受控干预 + 观察性切片实验。
- 旧方案：长度/格式校正能降低明显的 scorer shortcut，在有确定标签保持干预时值得做；但“分数与表面特征相关”不表示表面特征与目标构念无关。
- 机制与控制权：冻结原 scorer 与构念标签，cross-fit 表面特征对分数的预测部分并扣除；预先声明错误切片、记录切片内对齐变化及全体/切片外代价。调整器拥有审计诊断，Evaluation owner 保留原分数与发布决定。
- Evaluation contract：353 道 MBPP 的正确/错误代码 × 仅注释/文档字符串改写形成受控对照；NLI/QA 有 held-out 和独立标注者复现，但正向结果只限预声明切片。全体对齐与 QA 同问题排序在报告正向切片增益的设置中下降；四个当前代 judge 探针未通过预设 loading gate。
- 未证明与 failure mode：去相关不证明构念效度恢复；标签构念与表面特征纠缠时可能删掉有效信号。标签来源/切片挑选错误和模型选择都可能改变结果。旧的未经校正分数在固定任务且偏差未证实时仍是受限基线。
- 评分/处置：2 + 2 + 2 = 6/9；`PLATFORM-EVALUATION-SYSTEM` Ch66 Integrate，仅将 residualization 作为受限审计分支，不作为通用修复。

## 2609.24380v1 — 信息时间 PPO

- Primary：[exact-v1 HTML](https://arxiv.org/html/2609.24380v1) §3–5、Appendix A/B；Evidence Level：作者理论分析 + Qwen3 数学 RLVR 实验。
- 旧方案：token-time GAE/固定 clipping 简单且可复现；若低信息 token 很多，非零折扣可能使终局监督在 token 长度上过度衰减。
- 机制与状态：冻结旧策略的下一 token 分布，取归一化熵作为局部 information-density proxy；沿序列累计这个代理量计算折扣和 trace decay，并使 clipping 随局部密度变化。Policy owner 保存旧策略、归一化尺度、熵和更新步；代理由旧策略重算但不能冒充真实因果 credit。
- Evaluation contract：论文报告 Qwen3 4B/8B/14B 和五项竞赛式数学任务，对 token-time PPO 比较；定理依赖所定义 information-time MDP 及 policy divergence 与密度关系。未证明跨模型、非数学奖励、工具动作或长尾 serving 效果。
- Trade-off/回退：需额外熵计算、归一化和漂移复核；熵高可能仅表示表达自由度而非关键推理，代理错配会改变 credit。若条件不满足，保留普通 GAE/固定 clip。
- 评分/处置：2 + 2 + 2 = 6/9；`TRAIN-PPO` Ch32 Integrate，作为条件分支。

## 2609.24504v1 — LoRA 合并中的未训练行为

- Primary：[exact-v1 HTML](https://arxiv.org/html/2609.24504v1) §3–7、Appendix A/C/D；Evidence Level：作者 LoRA 合并实验。
- 旧方案：merge parent 的原训练任务回归是必要但不充分的发布检查；一个 adapter 也可能携带未被明确训练的可观察行为。
- 机制与状态：固定 base 合并 LoRA deltas；分别度量训练目标和 held-out emergent behavior，merge partner 是否也携带该行为会改变保留曲线。Registry 拥有 parent/merge/digest lineage，Evaluation owner 分别验收两类行为，不能用一个总分取代。
- Evaluation contract：两个独立测试床（activation oracles、emergent misalignment）及三模型家族；作者在若干 dilution 强度下比较 trained 与 emergent retention。危险的广泛 misalignment 消失，不能证明窄域训练危害也消失。
- 未证明与 failure mode：全部实验为冻结 base 的 LoRA-space 合并，不是全参数插值；misalignment 依赖 LLM judge，未知行为无法穷举。简单可信 artifact 不合并时保留单一版本最直接。
- 评分/处置：2 + 2 + 2 = 6/9；`PLATFORM-MODEL-REGISTRY` Ch59 Integrate；不把“涌现能力更脆弱”写成普遍定理。

## 2609.24885v1 — Copy Ceiling

- Primary：[exact-v1 HTML](https://arxiv.org/html/2609.24885v1) §3–11、§17；Evidence Level：单一策展 ontology 上的作者实验和判分审计。
- 旧方案：只比较裸模型与 RAG 答案，容易把输入中已经完整提供的答案计为模型推理提升。复制已暴露上下文是便宜、可复算的 no-op 参考。
- 机制与数据流：对每个 gold item 保存是否被输入暴露、是否由答案恢复，形成四格计数；同一 matcher 比较原样复制输入与答案，得到 signed gain over copy。Corpus/context owner 拥有暴露事实，reader 只拥有恢复，scorer 保留 matcher 与语义审计边界。
- Evaluation contract：作者 8,146 类的单一 ontology、1,136 target instances × 十模型；另有分层语义判分，检查词面 matcher 的误判。Copy ceiling 是 exposure-recall 参考，不是理论上界；净增量可隐藏遗漏与新增抵消。
- 未证明与 failure mode：冗长复制可抬高 recall；精确词面匹配漏掉改写且可能错认关系，模型 judge 也有误差。不可枚举 gold 或开放问答应采用更强的 sufficiency/claim-level 评价。
- 评分/处置：2 + 2 + 2 = 6/9；`PLATFORM-EVALUATION-SYSTEM` Ch66 Integrate，RAG Ch76 只保留原有阶段归因 handoff。

## 2609.22897v1 — 端侧开放类更新

- Primary：[exact-v1 HTML](https://arxiv.org/html/2609.22897v1) 的方法、实现、30 站点回放和限制；Evidence Level：作者系统实验。
- 旧方案：静态端侧类集和未知项云回退简单，但反复遇见本地新类时每次都付网络与人工/云调用。新路径由云 VLM 提名，站点合成标签数据，重训/验证 compact classifier 后把新能力以端侧 artifact 更新；LLM 不拥有标签真值或部署权。
- 状态/控制：上传选择、标签来源、训练集、模型 revision 与回滚应分离；断网时旧本地能力继续服务。通信能耗为估算，不是现场链路测量；Jetson Orin Nano 15W、30 站点回放不能外推总体节能。
- Failure/共存：云标签错误可污染自训练，class drift、断网、持续现场行为未覆盖；类集稳定或云始终可用时固定模型+有界回退仍合理。
- 评分/处置：2 + 3 + 2 = 7/9；`MULTIMODAL-EMBODIED-VLA` Ch26 Integrate，端云 control contract 受限分支。

## 2609.23269v1 — 多机共享感知 latent

- Primary：[exact-v1 HTML](https://arxiv.org/html/2609.23269v1) 的方法、实验、消融与限制；Evidence Level：作者受控模拟 + 真机 hazard 解码。
- 旧方案：共享位置/运动学消息便宜可解释，但不能传递他者相机见到的路由危险。冻结共享感知 encoder 让 sender 广播 64D latent 与位置锚点，receiver 用 team reward 学 route head；固定带宽、一步延迟和拓扑是实验条件。
- 状态/控制：消息 identity 需绑定 sender、encoder、pose/time；payload 是否包含信息与 receiver 能否通过探索学到动作是两项不同 Gate。Rendered-pixel 路由近最优和 102/102 真机 hazard 解码，均不证明真实协作任务成功；连续速度控制即使给 oracle bit 仍可能失败。
- Failure/共存：共享 encoder 漂移、消息延迟/恶意和探索不可达；不具备共享表示时保留显式几何消息与保守控制。
- 评分/处置：2 + 2 + 2 = 6/9；`MULTIMODAL-EMBODIED-VLA` Ch26 Integrate。

## 2609.23551v1 — 文本层级位置编码

- Primary：[exact-v1 PDF](https://arxiv.org/pdf/2609.23551v1) 的方法/小模型实验/限制；Evidence Level：作者受控小模型结果。
- 关闭理由：paragraph/sentence/token 轴改变 attention，真实结构相对密度匹配随机轴只有部分 corpus 可分辨；8 层 d512、1024 context、每语料 5,000 步和三 seed 没有下游大模型或 serving 证据。Ch13 已有多轴位置表达与训练窗口边界，这里不足以改变长期选型。Status：候选前关闭，不评分、不做 Books。

## 2609.23976v1 — 观察还是出手的时间选择

- Primary：[exact-v1 HTML](https://arxiv.org/html/2609.23976v1) 的停止边际、理论、Isaac Lab/Go2 对照及实机演示；Evidence Level：作者理论假设 + 受控仿真。
- 旧方案：固定 release 时刻和 confidence-only gate 简洁，但多观察一步可能错过不可逆的拦截窗口。作者比较当前出手价值与等待成本，使 activation 有停止边际；策略启动后仍由低层控制器执行。
- Evaluation contract：仿真 50Hz motor/10Hz timer、三 seed；同参数 learned gate 与作者基线比较。实机只展示 feint 修正，未给通用定量安全。理论依赖充分决策态、单交叉与近似误差界；belief 在主要控制实验由模拟器给出。
- Trade-off/回退：估计误差、过早/过晚 commit、现实状态不足；无法验条件时用保守时限或人工接管。
- 评分/处置：2 + 2 + 3 = 7/9；`MULTIMODAL-EMBODIED-VLA` Ch26 Integrate。

## 2609.24996v1 — 示教与部署共用 guardrail

- Primary：[exact-v1 HTML](https://arxiv.org/html/2609.24996v1) 的 guardrail 生成、轨迹反馈与三项真机任务；Evidence Level：作者小样本机器人实验。
- 旧方案：human teleoperation 直接收集示教数据，部署时独立过滤 action，接口简单；但不可执行示教会污染训练分布。代码 Agent 提出 `G(s,a)`，保存 proposed/executed/state/video/outcome，三轮反馈修正后将同一规则用于示教收集和 policy action 过滤；它仍只是待验证的过滤建议。
- Evaluation contract：Pi0.5、三项实机任务，每条件十 trial；某些 guarded data 提升采集成功，但 wine 任务 success-only 无 guardrail 50% 高于 guarded 40%。不是普遍性能或安全保证。
- Failure/共存：runtime 只看 proprioception，不见滑移、物体或液体；代码漏洞、跨任务/硬件漂移和过度过滤未闭合。独立安全层与人工接管仍保留。
- 评分/处置：2 + 3 + 2 = 7/9；`MULTIMODAL-EMBODIED-VLA` Ch26 Integrate。

## 2609.22246v1 — 伪多源新闻对概率预测的干扰

- Primary：[exact-v1 HTML](https://arxiv.org/html/2609.22246v1) §II–VI、§VIII；Evidence Level：作者模拟语料注入/ForecastBench 对照，不是已观察的互联网入侵。
- 机制与评估：向 17.4M 篇 Common Crawl News 的时间过滤检索环境定点注入合成文章，对 500 个已结算二元事件、三个 7–8B 预测器观测概率移动、flip、Brier、检索存活与中性文章 placebo。注入在实验 corpus 内实现，不证明文章真的被公开发布、被现实爬虫接收。来源标签变更不能替代独立性或真实性验证。
- 设计/失效边界：公开 evidence owner 必须区分 publisher identity、独立事实来源与同源转载；概率输出另需 calibration/proper score。Ch76 已有证据来源和 claim support，Ch72 有 corpus poisoning，Ch66 有概率校准，三者联合已覆盖可行动合同。新论文提供受限威胁量化，不改变 owner；无须为它追加重复段落。
- 评分/处置：2 + 1 + 2 = 5/9；标准 Source Review 完成；Books `No Change — Existing Coverage`。独立审阅确认。

## 2609.24243v1 — CoT 可监控性与答案质量分离

- Primary：[exact-v1 HTML](https://arxiv.org/html/2609.24243v1) 的机制干预、训练与实验；Evidence Level：作者所测 VLM/监控器的行为和 activation 干预。
- 机制/边界：奖励优化可以改变答案准确率，同时降低可从 CoT 看到的证据；SAE 局部特征抑制和训练正则给出所测任务中的干预线索，却不能证明输出 CoT 普遍忠实或 SAE feature 是稳定因果实体。
- Books 判断：Ch66/Ch72 已要求将内部解释、可监控过程、外部 outcome 与安全保证分账。此文没有改变独立 evaluator、行为证据和 release gate 的权责；只作为受限案例保留日报，不在书稿复述模型/监控器实验。
- 评分/处置：2 + 1 + 2 = 5/9；标准 Source Review 完成；Books `No Change — Existing Coverage`。独立审阅确认。

## 2609.24895v1 — 交互式证明的条件边界

- Primary：[exact-v1 HTML](https://arxiv.org/html/2609.24895v1) 的互动证明框架、假设与限制；Evidence Level：条件性形式分析，缺少验证所需前提的生产实证。
- 机制/边界：多轮人机质询只有在每轮错误通过率上界、人的检查执行率和自然语言到形式命题映射可被外部给出时，才可能累积 anytime false-accept 控制；自由文本辩论自身不提供这些前提。若人类忽略关键挑战或正式化遗漏语义，所谓置信保证失效。
- Books 判断：Ch84 现有 independent verifier/anytime acceptor 路线已要求外部可检的 acceptance contract；新文章重述一条条件结构，不提供可直接改变 Agent 平台验收的实测边界。不能将理论条件升级为通用正确性证书。
- 评分/处置：2 + 1 + 2 = 5/9；标准 Source Review 完成；Books `No Change — Existing Coverage`。独立审阅确认。
