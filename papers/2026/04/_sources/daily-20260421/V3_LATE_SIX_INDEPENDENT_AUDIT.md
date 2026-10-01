# 04/21 late six：有限独立采用核验

复核者：`apr21_late_adopt`（非报告作者）。实际检查：2026-09-27 15:53 北京时间。

范围固定为 [V3_BATCH_17064_17073.md](./V3_BATCH_17064_17073.md) 与 [V3_BATCH_17078_17093.md](./V3_BATCH_17078_17093.md) 的六项作者证据/Books 边界，以及 17082 的前分母排除。17087 由另一个复核者处理，本文件不审。已亲自读取 AGENTS、当前研究/Report 合同、统一 Prompt、每日/arXiv 来源路由、ROADMAP 与本日 checkpoint；重新打开下列官方 exact-v1 必要段落，并阅读当前具体 owner 正文。没有重扫 raw、附件全集、版本史或另一日期。

本日窗口仍为 `[2026-04-20T09:00:00+08:00,2026-04-21T09:00:00+08:00)`。本轮不复核日期组合或全日 Coverage Gate，不能由本文件新增首发证明；尤其不把 Submitted/Updated/DOI 元数据单证叫首次公开。未复现实验、未逐行核全部证明、未写 Books、未修改作者记录或正式 README。

## 结论

| 家族（均 exact-v1） | 本轮裁决 | 支持的作者处置 |
| --- | --- | --- |
| 2604.17064 | PASS | 6 分标准完成、仅报告；不外推默认 AI 平台 runtime |
| 2604.17067 | PASS | 5 分标准完成、仅报告；不外推 Transformer/Adam 收敛 |
| 2604.17068 | PASS，窄反例独立成立 | 6 分纠错深入、暂缓中心依赖/安全预算保证 |
| 2604.17073 | PASS | 5 分标准完成、仅报告；语义 reference 不升级为事实/概率保证 |
| 2604.17078 | 暂缓处置支持；保留分支的措辞须修正 | 6 分纠错深入、暂缓 enforcement→statistical WD 保证；修正见下 |
| 2604.17093 | PASS | 5 分保护行为深入、仅报告；语言配合不升级为真实 EDA effect |
| 2604.17082 | PASS，仅前分母排除 | 不评分、不 selected、不扩全文队列 |

这是 5 项有限 PASS、1 项精确措辞修正与 1 项排除 PASS，不是日级通过，也不冻结候选总数。

## 17064 — Sarus Suite

实际重开 [exact-v1](https://arxiv.org/html/2604.17064v1) 的 §2–3、§4.2.1（Execution model / Namespace semantics / Privilege model, failure handling, and cleanup）、§5.1、§5.4–5.5、§6/Table 2 与 §7 的 Ray manifest 解释。源中 rank 进入共享 user/mount namespace、其余 host namespace 和 Slurm 生命周期责任明确；普通 Podman baseline 已启用最低功能，并非未经适配的完全默认配置。§5.4 的 mock-data、关闭 eval/checkpoint、按 GPU 数放大全局 batch，支持弱扩展下的受限运行比较，不支持训练质量、故障恢复或默认 runtime 普适优越性。§6 单节点 warm-import 启动测试不能替代冷 acquisition 或多节点尾延迟。§7 是 manifest 在本地 engine 中的解释，不是 Kubernetes controller 语义验收。

实际 owner 对读：`PLATFORM-FOUNDATIONS`，Ch57 [Paved Road 与 Escape Hatch](../../../../../books/part-06-ai-infrastructure/57-what-is-ai-platform.md#paved-road-与-escape-hatch)，当前正文第 135–148 行要求自定义 runtime 仍声明 provenance、拓扑/失败语义与实验 blast radius；`PLATFORM-KSERVE`，Ch61 第 16–66 行明确服务控制面不重新实现推理、容器运行不等服务就绪。新材料的具体 HPC integration 有受限工程贡献，但不足改变这两项判断。PASS“仅报告”；不是以已有主题为由宣称全文实现已有覆盖。

## 17067 — Trajectory-restricted optimization

实际重开 [exact-v1](https://arxiv.org/html/2604.17067v1) 的 §2.1/A1 与 proximal update、§3.1/Definition 5/Theorem 1/Corollaries 1–2、§3.2/A2/A3/Theorem 2，以及 §3.3 的 polyhedral/Hoffman 边界。Theorem 1 的下降不等式代入 restricted PL，确实给当步收缩；乘积率依赖每步满足相应集合条件，tail 率依赖“已进入并持续留在集合”。这是 rate 与 identification 的分离，不是识别算法。PL→EB 的 A2/A3 不能省略；局部 smoothness 分支也不能凭单点曲率自动使用较大步长。未审全部 appendix，不给全定理正确性背书。

实际 owner 对读：`WORLDVIEW-REPRESENTATION`，Ch5 第 10–16、141–168 行区分目标塑造的表示、训练误差/部署泛化以及具有 architecture/curvature 前提的受限优化解释。该材料提供可保留的条件性学习/优化认识，但没有把相关条件落到现代训练器的桥，不能写自动停点或一般 Transformer 收敛。PASS“标准仅报告”，不因无 LLM benchmark 排除，也不伪造 Books 缺口。

## 17068 — SWD：小 KL 不上界总依赖

实际重开 [exact-v1](https://arxiv.org/html/2604.17068v1) 的 Alg1、§4.1/Eq5、§4.2/Eq6、§5.1、§5.6–5.7/Table4、AppA.1–A.4/Eq9–24，以及 Table5 的负向 slice。Eq19 明确把总依赖拆成新增 context 的信息与非负 residual；因此 Eq5/16 的下界本身不能证明 Eq6 所称总 MI 预算上界。Alg1 的 `D(p_previous || p_current)` 与理论/AppA 的相反方向也确实不一致。Table4 给出了受测总时延和显存，不能说论文完全没有 wall-clock evidence；但 NFE 仍不是生产 SLO，受测时延也不使安全桥成立。

独立演算，而非照录作者：令 A 与 B 独立，B 为公平 Bernoulli，C=B；旧 context 为空，本轮只揭示 A。真实条件分布 `p(B|A)=p(B)`，故两个 KL 方向均为 0；同时 `I(B;C|A)=ln 2`，且 `I(B;A,C)=ln 2`。残余依赖完全落在 Eq19 的第二项，直接否定“小 temporal KL 足以认证剩余解耦”的推断。反例不否定在一致真实 joint 下 Eq10 的期望 CMI 恒等，也不否定受限经验 proposal。另用 p=(.5,.5)、q=(.9,.1) 检查，两个方向分别约 .5108 和 .3681，不能无条件互换。

实际 owner 对读：`MULTIMODAL-GENERATIVE-PARADIGMS`，Ch24 第 175–210、423–429 行已有 unmask/修订/commit 的取舍，attention/confidence 非独立性或真值、entropy 非步骤结束的分权。PASS 窄暂缓，不向现章加 safe-unmask certificate。重开仅需方向一致、模型条件分布与真实 joint 的桥、有效 upper bound 或明确撤回认证主张改成经验 heuristic；不索全版本史。

## 17073 — Abstain-R1

实际重开 [exact-v1](https://arxiv.org/html/2604.17073v1) 的 unanswerability 定义、§4.3/Eq2–6、§5.1–5.3/Table1、§6.5–6.6/Table4 和 AppA/Table5–6。symbolic answer check、格式/拒答 check 与 reference clarification 的语义判定是不同证据路径。训练/评价 judge 分开不证明 reference 完备或评价为外部事实真值。AppA 明写按 Abstain-Test-SUM 选 SFT checkpoint，不能把相同 selection population 再称完全未用于选择的 heldout。Table1 的 A-FU 两个上升 slice、Table4 的 SFT/ICL trade-off 确实需要保留，不支持“所有可回答指标无损”。

实际 owner 对读：`TRAIN-RLHF`，Ch31 第 326–333 行有 checked span / 完整行为边界；`PLATFORM-EVALUATION-SYSTEM`，Ch66 第 896–915 行保存 generator/filter/verifier/answerability population，第 1489–1505 行把 risk-coverage sensor 与外部事实/verifier 分开。本篇提供受限奖励接口与评价分母证据，但不能把其完整 clarification 算法称已覆盖，也不足由单 reference/judge 合成路径建立开放可靠性保证。PASS“标准仅报告”。

## 17078 — 内部正交到跨任务正交的桥

实际重开 [exact-v1](https://arxiv.org/html/2604.17078v1) 的 §4.2.1–4.2.4、§4.3/Definition4/Eq8/Theorem2、§5.1/Table1–2、G.4.2/Eq97–105 与 G.4.3/Lemma3 的两部分。Eq8 是单任务更新矩阵自己的 Gram 惩罚；G.4.2 在 Eq101 后另加入不同任务独立随机采样，G.4.3 又明确 uniform Stiefel。惩罚没有建立这组 sampling 条件。作者 I/I 反例真正成立：单层 ΔW_t=ΔW_j=I₂，两项惩罚皆 0，向量化内积为 2、两范数均 √2，cosine=1。它不是这组独立均匀假设的反例，也不反驳 TFS+NTK 的理想充分条件或 Table1 的有限 CLIP 结果。

还需一处独立限定：G.4.3 的零均值与绝对 cosine 不能一起无条件保留。取 m=d=1，独立均匀 A,B∈{−1,+1}，完全满足声明的 Stiefel sampling；Z=AB，所以 E[Z]=0，但 |cos| 恒为 1。Part2 没有排除此维数，也未给定量集中界，仅以几何直觉推“sharp peak”。这证明零均值本身不蕴含 E|cos|≈0；不宣称所有高维分支失败。

精确修改建议（由作者改原记录）：把“保留 G.4.3 独立均匀 Stiefel 条件分支”收窄为“保留独立均匀采样的零均值结论；高维集中与绝对 cosine 近零仍需明确维数/集中界，且不得外推到优化所得更新”。README 第 143、777–779 行与批次记录中的同一措辞应一致。该修正不改变 6 分深入暂缓处置；不是因读得多而升分。写后检查已实读作者同步后的正式 §4 与批次正文，两处正确加入 scalar 反例与上述限定；候选表第 143 行同样须去掉笼统“条件 Stiefel 分支”表述。本复核者没有改作者文件。

实际 owner 对读：`TRAIN-LORA`，Ch30 第 522–540 行把谱兼容筛选、真实任务输入/输出、组合后 Evaluation 分开。I/I 与 scalar sampling 两个反例说明不能追加无条件 merge/WD 保证；现有有数据校准、独立 adapter 与组合回归分支继续合理。重开为惩罚→所需 sampling 条件及明确角度界，或收窄为经验正则器，不新增 Books 写入。

## 17093 — HarmChip

实际重开 [exact-v1](https://arxiv.org/html/2604.17093v1) 的 §III-A/B/C、§V-A/TableII、§V-B–D 与 §VII–VIII。difficulty 由六模型既有响应筛出，评价池包含这些模型；judge 也在被评池，排除 clustering 不解决 ASR 的 judge 独立性。方法段写每 tier 360，其他段写 across tiers 360，不能据此自行合成可靠总分母。§VII 明写 EDA compile/simulate/synthesize 为后续工作，language compliance 不是 fabrication effect。默认 OpenRouter 解码并未充分冻结服务 revision/输出长度/硬件等 identity。这里的新安全 slice 值得报告，但模型总体安全排名与“硬件漏洞已实现”均不能采用。

实际 owner 对读：`PLATFORM-EVALUATION-SYSTEM`，Ch66 第 215–224 行说明 judge bias/人工 anchor，第 697–711 行说明 judge 不拥有 environment truth，第 896–915 行说明生成/筛选 population 会改变分母。本篇不足改变这些原则，PASS“保护行为深入、仅报告”，不把语言内容升级为可执行 witness 或生产风险率。

## 17082 — D-Prism：仅前分母关闭

独立重开 [abs/v1](https://arxiv.org/abs/2604.17082v1)，完整读取题名/摘要、Comments 与当前可见 submission history。原始题摘研究 structured dynamic object 的几何/运动重建：primitive surface 与 3DGS 绑定、deformation network、primitive count 的 adaptive control。这里 control 是拟合表示的控制，不是 policy action 的环境干预接口。可见 Comments 只有 CVPR 接收与项目入口，未读到纠错、安全、撤回信号；没有扩展隐藏版本史或用无标记证明绝无信号。

实际 owner 对读：`MULTIMODAL-WORLD-MODELS`，Ch25 第 14–35 行区分视觉生成、observation prediction 与 action-conditioned transition。题摘没有给改变当前 foundation-model/world-model 主线的机制或反证；不是“非 LLM”或“所有 CV 不收”的硬排除。PASS family-specific 前分母关闭，日期不再为此追全史，不评分、不 selected、不索全文。

## 边界与交接

本文件只新增这 6+1 项的有限复核证据。17078 的保留分支措辞需作者定点同步；其余作者处置在上述最小范围内通过。没有共享文件写锁、没有 Books 改动或真实写后验收，不能增加 Integration 数，也不宣称全日完成。完成本有界任务即回报，不接下一日或全日 Gate。

### 精确修正已闭合（2026-09-27 15:57 北京时间）

已实际读取作者修正后的三处：正式 README 候选表第 143 行、§4 第 777 行，以及 `V3_BATCH_17078_17093.md` 第 7–9 行。表格已改为“保留独立均匀零均值/TFS/CLIP；集中及绝对 cosine 与优化采样桥未证”，两份正文保留 scalar 反例、明确维数/集中界与优化采样条件缺口；未抬分、未新增 Books 正面保证。因此本文件上方 17078 的精确措辞问题已经闭合，当前结果为六项有限证据/处置 PASS（含两项窄暂缓）与 17082 前分母排除 PASS。文件新增内容空白检查无报错，本地两批引用及 owner 链接目标存在。本轮只写此专属审计文件，不验收全日 Gate，不新增 Integration 数；6+1 项有界任务结束。
