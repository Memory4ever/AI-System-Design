# Jan14 deciding8 独立准入 delta6（2026-10-08）

复核者：review_jan15_delta（非作者）。本轮仅 root 明确授权的 07449 / 06943 / 07821 / 06599 / 07060 / 07219 / 07366 / 06972，沿 admission-audit 末表问题定点补读。沿用本日独立上下文、当前合同及 BJT Jan13 完整自然日补充窗；不重开原17项或改变原报告窗口。完整题名/摘要已独立读本日 increment-abstracts-1/2/3/4/5-20261007.json 对应八项，摘要提交字段只作发现身份，不证明 public date。

结论：7 项具名潜在贡献明确，进入作者必要证据/日期/当前官方信号/评分与实际 owner 判断；06599 贡献前关闭。这里不是 7 项正式入选、score / Evidence / PRE / POST / DAY PASS。没有用 Books 既有覆盖、实验尚待可信度验证、领域名称或工作量关闭候选。未改 Books、Report、LS、索引，未 stage / commit / push。

## 已保存必要原件

- [core1](./increment-deciding8-core1-20261008.json)：RLPO §4.1、§5.1–5.2、AppD；VideoDR §4.1、必要 §4.2–4.4 与限制；FARL §III–IV、VI-A/B1/B3；06599 §3/4、AppA.4、§6–7。
- [core2](./increment-deciding8-core2-20261008.json)：PALM §3.4 / Table1、AppA.3/C.1；VENUS §4.2–4.3、§5.2/5.4；HiVid §3.4.1–3.4.4、§4.3、App8。
- [ASR](./increment-deciding8-asr-20261008.json)：06972 exact-v1 官方 PDF 必要 p2–8 与 p14 的 §2/3/4、限制、AppG。HTML 404 与 web PDF Internal Error 均只是访问路径故障；官方 HTTPS PDF 后已恢复必要正文，不以故障关闭。

HTML 原件使用官方 exact-v1 页面，保存可读文本与 math alttext；只消费表内决定事实的段落，不称整篇/所有附件实读。JSON 中个别 notfound 是标题定位失败的原观察，已由同项随后成功的精确必要片段补足，不作证据。06972 仅提取指定页，未审完整附件或历史版本。06599另轻读当前官方abs：current v4 / last revised 2026-07-30 / comments ACL 2026 Main，页面未见具体撤回/纠错说明；版本号变化本身不当重要修订，不比较整历史。

## 逐项裁决

| Source Family / 原文 | 决定准入的实际增量 → 改变哪项选择 | 直接反侧与限定 | 裁决 / 后续最窄路由 |
| --- | --- | --- | --- |
| 2601.07449v1 [RLPO](https://arxiv.org/html/2601.07449v1) | §4.1 把 query–item 的点式 score 与 last-hidden representation 交给列表 MHSA/MLP，再加标量 residual；列表交互由全文 token 域转入表示域。AppD 明示每加入一篇时同 backbone/decoding 栈的增量比较，不只是电商榜单或泛称轻量。可重新考虑单项语义编码与跨项重排序是否必须共同重算。 | §4.1 冻结 backbone / 只训 residual，与 §5.1 两阶段全参表述冲突；不拼实际训练 recipe。表示依赖 query/模型身份，不能任意跨 query 缓存；列表头仍 N×N。K50 与点式差距缩小、各域有反侧。AppD 的 per-review 与 per-list 单位不同，不能签通用吞吐；还须纳入 SFT/CoT/头训练、初始列表成本，且 representation 的具体 token pooling 未在此定位闭合。 | 继续：表示级 residual 的信息/资源接口。拟 AGENT-RAG / Ch76 排序选择；只是路由，不授 Existing 或改书。 |
| 2601.06943v1 [VideoDR](https://arxiv.org/html/2601.06943v1) | §4.1 同一批100题、同一模型家族、同 think/search 工具比较显式中间视频线索文本与单 agent 的视频→搜索组织；§4.2/4.3 存在模型依赖的无收益/回退，足以限定“end-to-end agentic 必然优于 workflow”，不是新增任务条目即贡献。 | 不匹配总 token/调用/时延；调用数与耗时已明显不同。两组织均无研究期 video revisit，未单独干预 anchor persistence，所以“线索丢失是唯一原因”、外置文本必更可靠及普遍长度规律均不采用。100题、Long仅10题、外部 binary judge与单次测量限制统计外推；模型名字在设置与表中有差别，不扩历史版本解释。 | 继续：同任务同模型有限组织反侧；拟 AGENT-MEMORY / Ch77 状态外置与保留，必要核采用人口而非整份 benchmark。 |
| 2601.07821v1 [FARL](https://arxiv.org/html/2601.07821v1) | §IV 把短近未来约束预测接到任务动作的执行前筛选，超界改由离线固定 recovery policy 实际执行，再以实际 task/recovery transition 训练在线 task policy。相对既有整 episode safety-Q / 临时 MPPI 的替代分支有实际组件对照，改变探索期间 predictor、recoverer 与被更新 policy 的身份分工。 | IR 在 FailureBench 是越界/碰撞等定义的干预代理，非证明物理损坏；未把命名本身算新理论。需120 recovery轨迹及20k–200k失败 transitions，不是免费安全。TableII虽局部改善但 FARL仍大量 failures；Franka Fragile Wall final return低于Uni-O4。未审/采用 §V 保证，且实际recovery动作训练不自动给PPO无偏或安全保证。 | 继续：短视界风险 sensor→固定恢复执行→在线训练数据分责；拟 MULTIMODAL-EMBODIED-VLA / Ch26，保现有 recovery RL 共存。 |
| 2601.06599v1 [How Context Shapes Truth](https://arxiv.org/html/2601.06599v1) | §3 的对象是强制支持/反驳、固定 first-token位置与标签对应的 activation difference；新增角度/幅值的 layer/context 几何描述。AppA.4 的80/20探针比较用于支持此测量，并非 train-no-context/test-context 的部署传递失效审计。 | §2 明确本作区分于已有 probe transfer；§6–7 将成果定位几何lens、相关非因果、干预未来。没有建立跨context probe实际失效、参数选择/读出改变或新的有效性条件；不将 theta≠0 推成truth oracle失效、上下文知识冲突因果。关闭不源于小模型/局部实验，也不否定其学术描述价值。 | 贡献前关闭，不评分、不授方法/实验全面通过；仅几何现象不足以改变本项目具体解释/选择。[当前abs](https://arxiv.org/abs/2601.06599)已轻核，未见具体撤回/纠错说明。public date本轮未另授，原身份材料保留。 |
| 2601.07060v1 [PALM](https://arxiv.org/html/2601.07060v1) | §3.4 joint action/progress 输出并不是只有辅助head；AppC.1 明确 progress threshold 终止当前 sub-policy、触发下阶段。Table1去progress与阈值消融给过早切换/不饱和停滞的有限反侧，改变“阶段完成”如何成为 action boundary。 | 90%是CALVIN局部选值，不给通用完成/物理安全阈值；progress是learned指标不是已验证任务真值，扰动下单子任务曲线不认证所有状态。四affordance teacher、DiT、追踪与闭环计算计费；不由已有蒸馏组件自动签整方法贡献或推普遍91.8%。 | 继续：连续阶段进度的实际切换 consumer 与阈值反侧；拟 MULTIMODAL-EMBODIED-VLA / Ch26。进一步只核采用所需标签/控制关系。 |
| 2601.07219v1 [VENUS](https://arxiv.org/html/2601.07219v1) | §4.2 图交集成为 preserved-background source prompt，目标为差集新关系+交集；source用于 inversion/CFG，不是直接把完整scene-graph再拼一次。§5.4移除source与同编辑backbone+GT target对照支持这个条件分工的有限收益，可以重新考虑旧全场景source与保留关系source的选择。 | 不授20–30s相对6–10m的等资源提速。EditVal accuracy .32低于SGEdit .53；PnP分支PSNR和LPIPS有回退，Table3按GT prompt评估的ImageReward也反侧。模型/cap15关系/77-token限制、MLLM解析错误与空间定位须保；一般CFG/inversion均成熟，不算独立新机制。 | 继续：编辑语义差分与保留条件分别送consumer，非“scene graph+diffusion组合”总括；拟 MULTIMODAL-GENERATIVE-PARADIGMS / Ch24。 |
| 2601.07366v1 [HiVid-Narrator](https://arxiv.org/html/2601.07366v1) | §3.4 Eq2–12 用ASR queries读取视觉形成fused ASR；scene queries读 fusedASR+vision，再让event queries只读 fusedASR+scene，最后 global-scene→timestamp/event 交给LLM。这是实际跨模态瓶颈/两级consumer关系，非只新增叙事dataset；§4.3分别增scene/event容量给压缩/质量的局部取舍。 | App8 的per-ASR-segment S+N E/Dv公式与正文全视频 S+N(1+E)、timestamp及“Dv dimensionality=384”口径未完全一致，不照录82.59%总输入/总费用收益。事件query按frame复制的时间身份需采用前核清；ASR/清洗teacher错误非视觉事实，更多二阶段训练和前端/压缩费用未等于省时。 | 继续：scene先汇聚、再进入event压缩的支持域和输出layout；拟 MULTIMODAL-REPRESENTATION / Ch23。只沿该接口必要核，不追整数据标注附件。 |
| 2601.06972v1 [Categorize Early, Integrate Late](https://arxiv.org/pdf/2601.06972v1) | §2.3–2.6标准化encoder-block深度/linear readout、同测量套件跨24已训模型，提供模型族的feature peak profiles；§3.4/3.5与AppG另有目标/模型异质性，允许重新考虑ASR任务表现相近不等中间线性readout层相同。该有限观察/诊断选择有潜力，不因控制尚非完美关闭。 | 17 Transformers/7 Conformers非同pretraining实验；回归只明确控log(params)，同Whisper语言pairs/删一outlier与AppG描述不隔离architecture、objective和训练人口。故不授architecture因果、default hierarchy或全部非Whisper一致。前端在Layer0前、linear accessibility≠全部信息；p7 truncation/streaming/人口公平性均未来预测，不签29% depth=实测latency/earlyexit效用。 | 继续：限定已训人口的线性readout profile及目标/前端混杂诊断；拟 MULTIMODAL-REPRESENTATION / Ch23；可以最后Only，但须按实际增量评分，不能借成熟probe原则/因果宣传抬分。 |

## 停点与交接

八项的决定准入事实均已取得，本组无“等全文”待办。7项交作者逐篇执行剩余必要证据、日期/当前身份、评分与具体owner判断；作者可复用以上已读必要核心，不重复抓整篇。06599留贡献前关闭的明确理由，不能从其他七项的潜力推正式计数。本轮未读这些七项的 actual owner 局部，不授 Existing/Integrate，root仍协调共享 Books 锁。整日普通工作不为零，本轮绝不授 DAY。
