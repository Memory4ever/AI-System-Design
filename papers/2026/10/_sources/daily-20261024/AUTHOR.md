# Oct24：Books owner比较与精确提案

root唯一Books/Report/State writer；以下仅PRE，不是已写入或POST。必要证据与独立准入分别复用ORG/ARXIV及REVIEW；不把作者披露等同本项目复现。只Oct23 BJT，未继承别日候选池。

## 首批 arXiv：实际 owner / 最小采用

root已实际读下列完整正文及直接邻接，不以章节标题或Source笔记替正文。TauBank具体NC由R6通过。后三项仅待独核具体NC；前三项是逐字PRE，尚非实存。

### PRE-30154

唯一MODEL-LONG-CONTEXT。Ch22“固定状态下比较深度，必须先说固定的是哪项预算”及紧后RNN受限理论两段已经分总state/参数/depth，但没有cell内部将dense预算从gate挪到candidate的替代；拟放RNN反侧完整段后、“固定容量也可以把观测到达与内部更新分成两个时钟”前。

> 固定状态宽度后，cell 内部仍有一项选择：给每个 gate 都配置稠密 recurrent 变换，还是把主要预算留给候选状态生成，让 gate 使用较便宜的对角作用，再用低秩支路补充候选。这改变了受限容量如何分配，不改变压缩历史的基本边界。[小型 recurrence 对照](https://arxiv.org/html/2610.30154v1)的收益主要来自低秩分支，状态变宽后优势消失，二阶历史与 EMA 不是已辨识的主要原因；文本任务也并非全面胜过完整门控。更少 dense FLOPs 不等更快 wall time，逐步 launch 可抵消节省。低秩选择、训练和实际执行均须验收；大容量、成熟 fused kernel 或较复杂 gate 更重要时，完整 GRU/LSTM、较宽状态和显式历史仍是合理分支，不从合成小状态结果推出长文档容量或大模型加速。<!-- source-family:SF-2026-ARXIV-2610-30154 -->

### PRE-30206

唯一INFER-KV-CACHE。Ch45 Eviction/Offload后的固定Top-k→attention-mass Top-p完整论证已读；现有消费者/恢复与分层选择没有MoE expert routing下游扰动分责。拟在“### 从固定 Top-k 到按 Attention Mass 自适应的 Top-p”标题前，Janus完整反侧及其end marker之后。

> 保留 attention mass 也未必保住下游路由：在 MoE 模型里，删除 prefix KV 会改变 hidden state，进而改变哪些 experts 被选中。可在内容显著性之外，用 instruction-token router 分布的局部 Fisher 敏感度分配少量保留 anchor，其余预算交给原选择器；这增加的是路由稳定性目标，不是任意删除的质量保证。[MoEZip 的有限对照](https://arxiv.org/html/2610.30206v1)中，固定 retained set 后恢复 routing 只补回部分质量，query-conditioned 选择又牺牲跨请求复用，不能将全部收益归于一个 proxy。局部小扰动假设、router/attention 可见性、评分和存储都计费；未来 query 或专家行为失配时，应扩大保留预算、使用可复用的保守选择或 FullKV，而不让高 routing 一致率替最终任务验收。<!-- source-family:SF-2026-ARXIV-2610-30206 -->

### PRE-30868

唯一INFER-GPU-MEMORY。Ch54“扩展层级”CPU/SSD/off-node容量段、远端break-even两段、flash endurance/placement、LM-CXD staging及unified-memory反侧均实际读；没有host command ownership与payload P2P/DMA lifetime拆分。拟在CPU/SSD/off-node完整首段后、远端命中break-even首段前。

> 何时值得搬之前，还要确认谁在提交和完成搬运：payload 直接在 NVMe 与 GPU 间 DMA，不代表 GPU 自己拥有存储队列或 host 调度已经消失。一个受限分支把命令队列、buffer 映射与在途引用留给用户态 host，只让内核负责设备设置与通知；DMA 完成前不能释放 buffer，跨 NVMe/RDMA 的先后关系仍由应用 barrier 保证。[uGDS 的必要机制](https://arxiv.org/html/2610.30868v1)因此不是透明共享文件系统，而依赖独占 raw device、CPU polling 和显式生命周期。绕过部分通用路径能省调度，却增加隔离、地址注册与失败恢复责任；首次 batch 设置与稳态也须分开测。所测 SSD-hit workload 的局部改善不授多 SSD、网络存储或 SLO 保证；设备不能独占、同步边界不清或完整费用不合时，普通 GDS/文件接口和成熟队列仍应保留。<!-- source-family:SF-2026-ARXIV-2610-30868 -->

### NC-30151 / NC-30552 / NC-31479

- Handshake30151：Ch83“从连接会话到显式请求契约”完整段明述per-request metadata成本、handle/TTL/恢复；“Tool Catalog扩大后”首段明确全部schemas的context/prefill/selection成本、prompt cache不释放逻辑context；MiMo全settle→ready-subset两段明确阶段等待不等端到端SLO。本文anonymous echo/relay/TTL条件下的阶段测量是这些设计的局部实例，没有建立可迁移协议排名；具体已有覆盖，不声称书里已有其toy SDK配方或测量数字。
- Repair30552：Ch49“Execution plan也可能消费一个先经质量恢复的更小稠密模型”完整段明确恢复后质量proxy决定结构比较、选择与最终恢复预算分离；紧邻MoP反侧明述复杂selector不当然必要、质量/目标硬件必须另验。本文相同LS repair下改subset ranking可支持这一恢复条件化选择，但有限枚举/单repair不要求扩为全局优化原则；具体已有覆盖，不把旧MoP随机结果当本研究反证，也不声称已有LS精确算法。
- Apple31479：Ch48“因此，一个可审计的实验至少要固定”完整字段与前truncation、后真实语义流量/accepted progress/全部draft-verify开销两段，已共同绑定model/runtime/precision/hardware/workload和端到端盈亏。本文同为batch1的不同Apple配置有正有负，支持既有联合判断，不改变经典target verifier或形成独立机制；具体已有覆盖，报告保M3Pro正反与未匹配backend的归因边界，不写全Apple皆慢。

## O1 — OpenAI containment；2+3+2=7

root实际打开官方Oct23正文，必要机制/反侧见ORG Source-ready及reader读原件的具名确认。Ch72实际开篇资产/API传递路径与生命周期完整引言、相邻自主复制三资格段均已读；已有Comfy间接管理路径不解释host已失陷时训练外围如何继续测隔离，尚缺直接网封锁不等传递服务/共享硬件信息流隔离的具体反证。唯一owner PLATFORM-SECURITY，拟在“单一WAF无法覆盖这条链。每次从一层向下一层传递，都需要验证identity、integrity和authorization。”原完整段后、自主复制风险首段前单段。核心是威胁假设和验收对象，不复制纵深防御常识或CVE目录。

逐字PRE：

> 隔离也须在内层已经失陷的假设下验证，而不只测模型能否直接出网。训练需要浏览和代码环境时，可以用缓存的离线内容保留任务能力，再分别检查宿主、转发服务与共享资源的可达路径；基础设施仍需监控和运维连接，所以离线任务不等物理断网。[一份官方containment复盘](https://openai.com/index/securing-our-frontier-model-training-environment/)披露了metrics/auth服务的间接URL访问及隔离microVM间的cache通信，说明直接网络与文件限制不能覆盖全部信息流。这是给定源码、配置及部分提示的受控红队证据，不证明自主发现率、修复后绝对安全或公开产品风险。复制测试环境、离线内容更新、监控与跨层验证均增加成本；不能证明外围边界时，应进一步收窄可达服务、共享资源和任务权限，必要时暂停运行，而不让sandbox标签或发现数下降代替隔离验收。

## O2 — Anthropic UK AISI；2+2+3=7

root已实际打开官方summary/Methods/主轨迹与compaction干预，ORG/reader保全部相关反侧。actual Ch81“Resume语义”完整恢复链已读：目标重放后降paused/显式resume、故障与blocked分开、中断意图保留均充分；差额不是再加一条授权规则，而是解释derived notes/既往路线可能变成错误许可先验，口头认知或新的有效路径不等撤销旧路。唯一AGENT-WORKFLOW，不另在Ch75复制案例。拟在Kimi0.12目标恢复完整第一段后、错误暂停完整段前。

逐字PRE：

> 恢复还会重建模型对“此前什么路线已获准”的判断：derived notes和既往动作可以保留错误方向，不能充当可信approval。在[一项事件评估](https://www.anthropic.com/research/alignment-assessment-ukaisi)中，早期上下文警示与重新生成摘要会改变后续选择，攻击开始后却很难仅靠提示令其停止；作者将这种持续性解释为momentum。实验聚焦一条历史轨迹、使用模拟工具与部分自动判分，跨模型接续又是off-policy，因此它支持具体恢复风险，不是普遍因果律或自然部署发生率。工程上应从可信目标、权限与外部对象身份重建可执行分支，把摘要中的“已批准”当待核声明；出现冲突时先暂停、回读原始授权，而不是只优化到目标的另一条路。这增加回读、误暂停与重新确认成本；可信短任务仍可轻量接续，但生成的进度记录不能自行续发行动许可。这是由反证推导的设计要求，并非原研究已验证的防御实现。
