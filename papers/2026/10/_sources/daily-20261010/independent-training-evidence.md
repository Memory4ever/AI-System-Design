# 本日五项训练证据独核

独立复核者：`live1010_evidence`。仅 own 本 note，不写 README、Books、Learning State，不 stage/commit/push。窗口为 2026-10-09 北京时间完整自然日，服务 Daily 2026-10-10；历史补查按最新 Learning State 暂停路由保持暂停。本批首批准入已由 root 独校，本人另实际读五项完整题摘与必要 exact-v1 core。以下是受限 Source/owner 写前结果，不是 DAY、全来源 Coverage 或实际 Books POST。

## 身份、日期与复用边界

五项均在 [官方 cs.CL recent](https://arxiv.org/list/cs.CL/recent?skip=0&show=2000) `Fri, 9 Oct 2026` 首段出现 exact-v1 身份，实际缓存见 [official-titles](./arxiv-official-titles.json)；只复核本五项交集，不把整个宽列表变成队列。API 的 10-08 submitted 字段不是公开日期。复用 author 的 [当前事件门](./arxiv-identity-signals.json)：11291/11247/11659/11854 当前 abs 仅 v1、无撤回/纠错信号。12161 原 abs native SSL EOF 后，web fallback 仍 cache miss，2026-10-10 本次通过 urllib 成功取得 [官方 abs v1](https://arxiv.org/abs/2610.12161v1)，Submission history 仅 v1（Thu, 8 Oct 2026 15:39:09 UTC），27 pages，未见 withdrawn/corrigendum/erratum/retracted 字样；不把先前 transient failure 留作材料受阻。五项无已读材料中的先稿另行归属信号，不声称遍历全部版本史或互联网首稿。

共同评分仍 **2+1+2=5**：新增机制/边界、局部训练组件、可复用但尚非普遍定律。KL 与两 OPD 设计反证、以及拟写 Books 的具体缺口均按合同加深受影响 core；不因“蒸馏/entropy 是长期知识”借分。实际只读本文下列必要方法、主评价、直接反侧与配置，没有核可运行代码、复现或部署。

## 2610.12161：独立 KL 与 reward gate 不共享停止条件

[Exact v1](https://arxiv.org/html/2610.12161v1)：§3 Eq1/F1–F7，§4 Eq2，§5 Table1/F1-B/F1-C 与 F3 说明，Appendix A 配置/数值成本、I 证据范围。独立 KL 在 reward branch 被 clip、共同前缀梯度抵消或全组 reward 相同时仍可有非零更新。ZCPO 先跳过 G<2 或 max absolute centered reward 为零的组，把全词表 conditional KL 的每响应均值组内居中，与 max-normalized reward 合成 C，再 stop-gradient 进入原 surrogate；因此共享 joint-coefficient gate。零和 C 不保证一般梯度抵消；正 reward 的 C 仍能翻负；不是原 sequence-KL gradient 的无偏改写，也不授每步 reward↑/KL↓或 hard trust region。

主评价 Qwen2.5-32B/DAPO-Math-17K、verl/AdamW、G16、512 prompts、token mean、AIME24/25 avg@32、3 seeds、按累计 GPU compute 对齐且不靠测试选 checkpoint；ZCPO 56.8/48.5 对无 KL 47.3/37.1，系数口径不同不可把 β4 与 β0.001 当同强度。F1-B/C 单独支持 clipped-token gate 的局部作用，完整 method gains 不等七条各自因果成立。主数学两组均已过滤相同 reward，所以不用于 F3 的实证；F3 仅引用长上下文 group-gating 分支。BF16 下 KL 二阶小量有 rounding risk，作者重算 FP32 output projection/全词表 reduction，局部增费约0.5%；硬件/通用端到端 SLO 未披露，不移作全局免费。

Books PRE：`TRAIN-GRPO` Ch33。现有 clipped objective（原148–181行）只说 KL 放置/estimator 有差异，DAPO 原573–590行只讲零优势/动态过滤；Ch32 原284–325行已有 old/reference 与 clipping/KL 分责，但没有上述 **reward gate 关闭仍留下独立 KL** 及 joint coefficient 的具体差额。建议在 Ch33 clipped objective 后窄整合机制＋反侧两段；Ch32 不再复制推导。受限 Source/owner 写前通过，实际 POST 尚待 root 改后。

## 2610.11291：固定初始 student support 可以优于持续 fresh support

[Exact v1](https://arxiv.org/html/2610.11291v1)：§2.2 Eq2–3/top64 overlap，§2.3 Fig2，§3，§4 Fig4–7，§5 Fig11，Appendix A。Semi-OPD 一次生成初始 student 全轨迹，teacher logprobs 可缓存，current student logprobs/advantage 每步重算；不是只做普通静态 teacher SFT。17对内匹配 prompts、训练参数与 cap，14对 normalized shared-horizon AUC 正；高 overlap 对仍可更偏好 OPD。Overlap 是相关 sensor，不是已验证跨域选择阈值或“只有高 overlap 才能 OPD”的普遍定理。Teacher-rollout 替换、等总训练 tokens 的 prefix truncation 消融分别检查 producer 与全 reasoning-stage coverage；base student 初始轨迹太弱时 Semi 劣于 OPD，明确否定无条件冻结。

局部条件 DAPO-Math、128 prompts/1 rollout、BF16 AdamW LR1e-6、17对覆盖三模型家族、1–8节点各8 H100、AIME24–26/HMMT avg@32、32K（Nemotron40K）评价。主图非thinking cap4K、thinking16K，Table1 的 OPD cap16K，两个比较不可静默合并；速度须包含一次性生成/teacher scoring 与重用周期，本文不签完整 serving 净收益。题摘 +13.6 与正文 Table3 最大 last-step +13.1 的口径未消解，报告不采用13.6或补造其归因，保留14/17 shared-horizon AUC。主张只取 frozen student support 与 fresh support 的条件分支。

Books PRE：`TRAIN-GRPO` Ch33 原1111–1130的 OPD 可达状态/teacher错配已有上位原则，但没有 **固定 initial student rollouts、current-weight 重算和双边 overlap/初始质量条件**。Ch31 原734–744的 freshness controller 针对异步缓存失配，不意味着所有缓存都须刷新。建议紧接现有 OPD 主线窄整合两段，不反转普通 OPD 或离线蒸馏的既有成立条件。受限 Source/owner 写前通过，POST 待改后。

## 2610.11247：剩余 mismatch 与实际 update 信号必须分账

[Exact v1](https://arxiv.org/html/2610.11247v1)：§3 top16 surrogate，§4 Table1–2，§5.1–5.3 Prop5.1/Thm5.2，§6 Table4，§7，Appendix C S1–S3、E proxy/cross-fit/config/single-run口径。Idealized flow 把 full-KL loss gradient 分为 detached per-prefix g 与 occupancy h；衰减量依赖 g 强度与 h 相对方向。作者 preclip minibatch grad-norm平方/残余 surrogate 的 μhat 会含 sampling variance，既不等 population g平方，也不测 AdamW 实际更新。Top16 objective 不是完整非负 KL，若其变负不能解释为 KL decay。七主对每条件仅一次、200updates、code avg@4/math avg@8；25.1/96.2 是 final reduction 平均，不是 Table2 minima。

Self-RL 条件解释是 **同架构/参数坐标/tokenizer/vocab/temp/interface、common support、固定 prompt 与参数无关 stopping/masking、有界score及finite rollout、Lipschitz Hessian、局部 flow 时域与低曲率 residual**；不涵盖异参数大 teacher，亦不独属于 self-RL 来源。小相对 displacement/高 CKA 在成功和停滞均出现，不证明 representation causal ceiling、可达最优已失去或真实 AdamW 保证；full-logit 与8-rollout有限额外对照只收窄近因，不消除 LR/budget/seed 混杂。FP32 diagnostic、teacher查询、额外rollout及训练probe均计费，真实全部硬件成本未统一披露。

Books PRE：`TRAIN-GRPO` Ch33 原1115–1121已有“大teacher不必更有用/错配”与“不会凭空扩能力上限”解释，但没有 **remaining objective 与 noisy update proxy/occupancy 分拆**；原2320–2326泛瓶颈分账也不承载这一诊断。建议在 OPD 段接入两段，明确不把本文当 universal capacity/representation 定理，不推翻旧 teacher/state 边界。受限 Source/owner 写前通过，POST 待改后。

## 2610.11659：同 log-ratio 不等同监督价值

[Exact v1](https://arxiv.org/html/2610.11659v1)：§3.1–3.3 fixed-density/random-replacement 反侧，§4 Eq3–9/Prop1–2，§5–6 Tables1–2/β sweep，Appendix B。两边绝对概率都很小时可有大 log ratio；DIAL 用 logarithmic mean^β×abs(log ratio) 排名，每response保固定数量，masked loss仍用 signed原reward，mask/reward detach，unselected token仍留context。β1是 absolute gap，β>1还会压低 one-sided useful disagreement；不能把低概率认定无用或把概率尺度当 correctness。低低替换与同数量 random replacement 对照支持该受限选择，过度β反退，逐项bench不皆更好。

四对Qwen Base0.6/1.7B学生与4/8B Instruct teachers、DeepScaleR800steps、BF16 AdamW LR5e-7、batch32、train cap1024、matched20/40% retention、七数学bench分avg@4/@8/@16与pass。只减少 loss positions，完整生成/teacher评分仍需，未测完整 wallclock/硬件/seed不确定性，不签省60% teacher或训练成本。Baselines包含改写后的selection与替代reference，不能称所有原始方法同配置复现。

Books PRE：`TRAIN-GRPO` Ch33 原1196–1239已有 task-relevance/progress conflict，不拥有 **log-ratio与absolute probability scale混淆**；两者是不同选择维度。建议在 Selective Distillation 的现有论证中插入两段，同原signed loss/context和低低/one-sided反侧衔接。受限 Source/owner 写前通过，POST 待改后。

## 2610.11854：生成预算不等实际 update 人口

[Exact v1](https://arxiv.org/html/2610.11854v1)：§3.2 Eq2–4，§3.3 Prop3/Eq7，§3.4 Prop4/Eq9/algorithm，§4 Tables1–3，§5 limitations，Appendix B1。完整原group的advantage–surprisal covariance给局部KL-prox entropy proxy，先删最负贡献后恢复非positive原advantage，最终只删selected positive；retained advantage需recenter。Theory使用真实sequence probability，实际filter/recenter length-normalized logprobs，不能将Eq9的精确old-measure抵消直接授给实际参数更新。Restore步骤及recenter会再次改变covariance，初步candidate constraint不保证最终entropy不下降。它保留loss form却改变update人口/权重，不是原GRPO objective无偏等价。

Qwen3 1.7/4/8B、DAPO17K一epoch、128prompts/G8、response8192、AdamW LR1e-6、无refKL/entropy bonus基线、十bench；主评价固定sample seed，不是多training seeds。相同8仍全生成，Qwen4B平均7.03是排除全零组后的10checkpoint **update人口**，12.1%不减生成budget；无recenter两模型collapse，概率加权在4B仅+0.03，不同规模仍有强baseline更好、QA反退。摘要embedding diversity不是真实过程正确/探索能力保证；理论独立logit/局部prox与shared neural SGD不同，不适用single-rollout，very-small group待验。完整hardware/cost/SLO未披露。

Books PRE：`TRAIN-GRPO` Ch33 原2271–2286有可学习样本/entropy flow原则，原573–590 DAPO有group过滤，却没有 **正向rollout选择、偏采样后recenter与两只budget时钟**。建议在现有“Verifiable Reward不等每样本可学习”与entropy flow邻接处窄整合两段；保留可靠reward及普通全group回退，不搬到runtime freshness段。受限 Source/owner 写前通过，实际 POST 尚待。

## 可写入 README 的限定复核结论

`live1010_evidence` 独立复核上述五项 exact-v1 完整题摘、必要方法/主评价/设计反侧与现有 Ch33/相关Ch31–32局部，五项受限 Source 与 owner PRE 通过；均保持2+1+2=5，具体 Books 缺口按本文定位。已限制“on-policy总优”“大teacher必迁移”“mask/delete即省生成成本”“理论sensor授真实entropy/表示因果”等过度主张。未核代码/复现，未检查其余候选或全部来源，也未授 actual POST 或六部分 DAY。待 root 实际写入后，本人再回对本文原证顺读新增/完整邻接及自身末注；报告在此之前不得把拟整合计已完成。

## Actual POST：首次顺读及定点修复请求

root 已实际写五项各两段。本非写入者实际顺读 Ch33 新183/185与145–202完整clipped局部，新1139–1145与1110–1165完整OPD邻接，新1214/1216与1204–1271完整Selective Distillation局部，以及新2306/2308与2281–2323样本admission/entropy-flow交接；回对本note已核 exact-v1 原证。五项本批未新增对应 Review notes，因此不虚构自身末注已验收。限定 diff-check 无报错。

首次 POST 暂不授通过，具名两处修文已交 root：12161 的“组过滤后独立KL仍更新”必须限定为 reward branch 门控而非整组移除，F3 明确是相同 reward 但 group 仍参加更新；11854 的“只有人口选择验证后才采用token-flow”不应把可独立选择的两个分支写成必经前置链。其余机制、成本、反侧与旧路径回退符合上述受限原证。root修后只重开这两处及完整局部，不重复未变化的 Source/PRE。

### 修复后 actual POST：通过

root 已修，非写入者 `live1010_evidence` 再实际读 Ch33 175–202 clipped完整局部及2293–2325 admission/entropy-flow完整邻接：183明确“组仍参加更新”与“整组已被过滤则不属此情形”；2308明确人口筛选和token-flow可独立选择、分别验收，而非必须先删再调。两项问题已消解，未变化三项及全部原证/PRE直接复用。

本批实际整合 **5家族/10段/唯一 TRAIN-GRPO Ch33**；新183/185（12161）、1139/1141（11291）、1143/1145（11247）、1214/1216（11659）、2306/2308（11854），各自上述完整邻接均已实际顺读。原证限定、费用、直接反侧与旧路径回退在正文，未写成摘要列表，也未借来源声望/成熟原则升级结论。限定 Ch33 与本note 的 unstaged diff-check无报错；未新增本批自身Review notes，不虚构该项。五项 actual POST通过，可由author将README相应Books改为真实整合，并引用本note；其余候选/全来源Coverage/六部分DAY不在本次授权结果内。未核实现/复现，未stage/commit/push。
