# Batch D 四项完整PRE

writer Locke / sole reader Chandrasekhar。R20实际owner比较、writer此前必要支持与R12/R13关键反侧复用；writer现已实际读Ch72档案/通信/优化段、Ch76代码闭包/层级索引及邻Ch71/73、Ch75/77交接。四项均2+1+2=5，具体安全/长期差额深入；无payload/攻击实施，不授安全保证。每项仅一段/独立marker与唯一H2 Review notes下本人注，保全部旧段/他注；尚未保存Books，不全章锁。

## D1 Genesis / PLATFORM-SECURITY / Ch72

文件：`books/part-06-ai-infrastructure/72-security.md`。已有semantic archive、有限风格库内bandit，不含本轮log归纳为新策略再改变后续候选生成的增长库。只安全campaign状态接口，不给攻击模板。

### 完整前邻接

archive 增加可重放性，也会把语义分箱、judge error 和搜索预算固化为盲区。有限 prompt/model 实验只能给出已发现攻击的
下界；未知 cells、低严重度或 tool/state 未覆盖时不能宣称安全，传统 curated red-team set 仍是稳定回归基线。

<!-- source-family:SF-2026-ARXIV-2606-00801 -->

### 完整新增与marker

档案还可以反过来改变候选的生产，而不只保存case或在固定库里分配尝试：从本轮交互日志归纳可复用策略，写入增长中的库，再检索这些策略指导后续候选生成。[Genesis的受限研究](https://arxiv.org/html/2510.18314v1)支持这条反馈接口，但归纳只是对已见结果的可错解释，不能把更多库条目当新增独立风险证据。测试过程中若继续扩库，后续样本面对的搜索状态已变，须保存每次库快照、来源日志、检索和候选谱系，分开冻结库泛化与在线适应。原测试人口披露有冲突、移除组件的消融又同时改变进化与库，不能独归总结机制或用pass@10推单次真实损失率。全部失败/成功交互、归纳、检索与再搜索均计费；库污染、重复模式或预算失配时，回退冻结curated suite、原档案与独立effect/良性效用核验，不由增长库自行签发全威胁覆盖。

<!-- source-family:SF-2025-ARXIV-2510-18314 -->

### 完整后邻接

攻击档案也可先制成有限的风格参数库，再在查询目标时按反馈分配尝试，而不每次重新训练攻击器：各style的LoRA与离线prompt侧reward形成一份资产，线上target-response反馈只更新选择哪个arm的状态。[Red-Bandit的受限分支](https://arxiv.org/html/2510.07239v1#S3)分开这两个消费者，所称rule-based实例仍有模型classifier，最终无拒词率与本方PPL也不是有效有害内容或人类可读真值。选择频率受探索、生成器和判据共同影响，不能解释为目标内在漏洞图；跨prompt/target变化的reward也不自动满足固定bandit理论。须保存bank/adapter、目标与反馈版本、尝试历史和query预算，@10任一成功不能与@1等费比较。全部离线逐style训练、guard、切换/驻留、目标查询、失败与独立人核都计费；反馈资格、非定常人口或预算失配时，保curated攻击回归、固定小库和独立effect/正常效用核验，不由自适应选择或较高ASR授全攻击覆盖、最优性与生产安全。<!-- source-family:SF-2025-ARXIV-2510-07239 -->

### 本人注

本人注：`SF-2025-ARXIV-2510-18314` — Locke，Daily2025-10-23补Oct22；writer exact-v1 §3.2–3.5支持，reader R12 §3.6/4关键反侧，2+1+2=5，日志→策略归纳→增长库→后续生产接口深入。保840/600与200人口冲突、pass@10/顺序扩库非冻结泛化、消融耦合及全费；不提供/执行payload，不授全覆盖/防御，未核实现/复现。PRE/SAVE/全自读/sole actualPOST仅本日实际层。

## D2 RESCUE / AGENT-RAG / Ch76

文件：`books/part-07-agent/76-rag.md`。已有dependency closure与摘要key，新的双载荷为abstract guideline与security-focused code slice，查询保多个安全facet共同消费。Ch72保功能/安全验收，不双写；不是CWE领域标签独占新owner。

### 完整前邻接

层级入口也可以由模型生成，而不只是读取现成标题：从同一文档产出outline、core摘要及原子chunks，多路径采样后按边界清晰度和条件重建分数选样，再蒸馏给较小reader。[MoM的受限分支](https://arxiv.org/html/2510.14252v1#S3)把摘要key与原段组织成可检索的派生对象，却不让较低perplexity或教师偏好认证事实完整；反向生成的思路也是训练标签而非真实阅读过程。多层向量优于融合向量的结论依查询分布与表示估计假设，不能由均值推出所有查询的概率保证。教师生成/选样、训练、三层索引和回读均付费；结构、原段对应或独立答案失准时保原文chunk/可信heading与人工核验，不把“document memory”变成事实源或Agent已记住的保证。

<!-- source-family:SF-2025-ARXIV-2510-14252 -->

### 完整新增与marker

同一代码安全语料还可以派生成两种不同载荷：按漏洞类别归纳抽象指南，同时沿修复处的程序依赖提取聚焦代码片段；查询端从草稿与诊断提出原因、接口等多个facet，逐层检索并融合指南与例子交给生成器。[RESCUE的受限实现](https://arxiv.org/html/2510.18204v1)把规范性提示与可参照代码分开，不使归纳指南成为权威规范，也不保证slice保全所有必要上下文；多facet还会增加相关但不适用的噪声。须保原漏洞/修复、切片与总结版本、各查询来源和回读关系，生成后仍分别验功能与安全。原SecurePass只是同sample通过unit test与CodeQL的交集，Semgrep反馈也不是独立真值或未知CWE证明。语料制备、依赖分析、草稿/诊断、检索融合与最终生成全计费；指南冲突、切片缺依赖或质量失配时，回读完整可信修复、保普通hybrid/原代码上下文与独立安全检查，不由更多检索层批准安全代码。

<!-- source-family:SF-2025-ARXIV-2510-18204 -->

### 完整后邻接

层级索引还可由受训练的句间关系生成，而不是依赖原文标题或生成摘要：先聚合多head/layer的attention并对称化，逐次合并关系最强的两组，保存原句叶节点与递归聚合表示；查询沿固定树做beam search，同时收集不同层的候选。这样的内部节点可能连起非相邻句子，不是原文连续section，递归两子均值也不等所有叶子等权。应保原span、叶集合与树/encoder版本，不能把attention强、树连通或父向量当完整语义证据。

### 本人注

本人注：`SF-2025-ARXIV-2510-18204` — Locke，Daily2025-10-23补Oct22；writer exact-v1 §2.1–2.2支持，reader R12 §3.1/3.5/B.3关键反侧，2+1+2=5，抽象指南/依赖slice双载荷与多facet消费者差额深入。保总结漏信息、SecurePass同sample交集/非全输入安全、反馈工具非truth及多draft/调用全费；未核实现/复现。PRE/SAVE/全自读/sole actualPOST仅本日实际层。

## D3 SafeCoop / PLATFORM-SECURITY / Ch72

文件同D1。Ch26已有坐标变换；新安全差额只消息空间声明→接收者frame→本地perception/multisource风险消费，不复制几何推导或把共识当truth。

### 完整前邻接

受限环境实验不能代表开放协议。生产系统应验证 sender identity、message provenance、权限与最终 action evidence；不可信边无法隔离时回退单 Agent 或人工仲裁。

### 完整新增与marker

当peer消息含空间声明时，还需把文本核验接到接收者的观测坐标：先将声明映射到本地frame，再分别检查与本地perception及其他来源的时序/空间一致性，而不只问措辞是否可信。[SafeCoop的受限协同驾驶模拟](https://arxiv.org/html/2510.18123v1)提供这条消息—几何sensor接口，但坐标转换不能恢复遮挡信息，local perception与多数来源也可能共同出错。各字段max与跨来源/层平均的风险聚合还可能稀释单个高风险，不能把trust名称当单票否决。应同时记录原消息、sender/frame/时间、映射与各sensor版本，另由控制器核动作；CARLA同步等模型输出后才推进的ET不是wall-time截止保证。解析、变换、多次模型/感知检查及等待均计费；几何支持、通信时效或deadline失配时，隔离消息、保本地可信观测和保守controller/停机，不由语义一致或恢复的模拟表现批准实车安全。

<!-- source-family:SF-2025-ARXIV-2510-18123 -->

### 完整后邻接

身份、schema 和消息签名能限制伪造，却不能排除合法输出选择中携带的隐蔽信息。一个更窄的通信准入分支把 policy revision、公开随机种子、消息链、latent/schema 与 tool/environment receipt 绑定到同一 envelope；生成器可以提出消息，独立 verifier 先检查固定 predicate，再允许 transcript 前进。证明或 attestation 只覆盖该 predicate，不能替 message 获得最终 effect authority，更不能证明未纳入 predicate 的语义选择无泄漏。

### 本人注

本人注：`SF-2025-ARXIV-2510-18123` — Locke，Daily2025-10-23补Oct22；writer exact-v1 §4.1–4.2支持、reader R13 §4/5.1关键反侧，2+1+2=5，仅消息frame→本地perception/多源风险消费者差额深入，坐标机制仍Ch26。保risk方向/平均稀释、遮挡/多数串谋、CARLA32情景/同步ET非wall-time与全费；未核实现/复现，不授实车安全。PRE/SAVE/全自读/sole actualPOST仅本日实际层。

## D4 Backdoor / PLATFORM-SECURITY / Ch72

文件同D1。已有优化后安全revision与trigger邻域；新反侧是蒸馏语料未见完整组合不等未见可传信号，非一般“派生均重验”再贴名。

### 完整前邻接

量化后门把这条原则进一步收窄：即使高精度 checkpoint 在既有 targeted test 上通过，many-to-one rounding 仍可能让某些触发行为只在部署格式中出现，且同一恶意构造可能跨多个 quantizer 转移。因此 release gate 必须测试**实际将部署的 model × quantizer × bit width × calibration × kernel**，不能用 FP16 结果或平均 BLEU/accuracy 代替 targeted behavior。它增加每种部署 artifact 的安全回归成本，也仍无法穷举未知 trigger；高风险路径应阻止未测 artifact 发布，低风险内部实验才可在明确隔离下保留快速路径。`arXiv:2608.27512v1` 的结果限作者构造的翻译后门、模型和量化器，不证明所有量化都会产生后门。

<!-- source-family:SF-2026-ARXIV-2608-27512 -->

### 完整新增与marker

蒸馏还要检查监督信号的粒度，而不只搜索训练语料中是否出现完整trigger：完整组合很少见，组成词却仍可在普通语料中出现并携带受污染teacher的输出信号，student之后才在组合条件下表现异常。[受限语言模型蒸馏对照](https://arxiv.org/html/2510.18541v1)否定“未见完整组合即已被蒸馏洗净”的推断，不证明任何teacher或任何KD都会转移；攻击者能植入teacher并预期下游数据/语言重叠仍是前提。安全验收须分别保teacher来源、蒸馏人口/组成词覆盖、student revision、完整触发与无触发误激活，并把正常任务质量和异常行为分验。Teacher前向、全部KD与独立行为回归均付费，本研究未提供有效通用防御；来源或触发覆盖不足时，保可信teacher/原artifact、隔离派生产物及外部输出/effect gate，不因普通语料标签或能力保持批准安全发布。

<!-- source-family:SF-2025-ARXIV-2510-18541 -->

### 完整后邻接

### 可组合 Prompt 也是 Versioned Supply-chain Artifact

Adapter、model weight 与 executable package 容易被识别为供应链对象；可热插拔 prompt、soft prompt 或视觉 prompt 往往被当作无害配置。在 prompt 只做静态模板且无外部来源时，这个简化合理；当 prompt component 可下载、拼接并在运行时改变模型功能时，它已经拥有 artifact identity、producer、依赖、compatibility 与 activation scope，必须经过 admission、签名与可回滚版本管理。

### 本人注

本人注：`SF-2025-ARXIV-2510-18541` — Locke，Daily2025-10-23补Oct22；writer exact-v1 §4.2高层支持、reader R13 §4.1/5/5.2/限制关键反侧，2+1+2=5，仅完整trigger缺席与组成词监督信号两粒度差额深入。保teacher植入/预期数据重叠、ASR/FTR分母、局部模型/能力评价及无有效防御，不提供毒化recipe、不执行攻击/复现。PRE/SAVE/全自读/sole actualPOST仅本日实际层。
