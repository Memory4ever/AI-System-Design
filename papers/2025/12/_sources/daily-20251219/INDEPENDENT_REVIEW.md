# 2025-12-19 非作者独立复核

复核者：Feynman（非本日报告作者；作者 Nash）。实际检查时间：2026-10-02T19:58:38+08:00。
结论：未通过。T5Gemma 2 release 的日期、准入和限定证据通过本轮源审；普通身份处置补正和共享 Books 写后检查尚未闭合，不把外部日期保留当成这些普通待办的豁免。

## 范围与日期

已重读 AGENTS、研究合同、来源使用说明/14 每日组及 arXiv 主题边界、Report V3、Prompt、ROADMAP 与本日 CHECKPOINT；实际读 README、SOURCE_STOPS、两份 ADMISSION、Books 提案、四组查询的入口/响应数/停止依据，以及系统全三标题、compute 全标题和其余精确遗漏身份。没有将宽列表全量变成逐篇队列，没有扫描周源。

窗口独立核为 [2025-12-18T09:00:00+08:00,2025-12-19T09:00:00+08:00)。查询 submitted 缓冲、月列表身份、只有日精度的原机构目录及 committedDate 均不授 first-public。Seed type1/type2 是两个独立原始邻接段；15/49 是该次响应，不用后来 18/45 的响应改写旧计数。DeepMind `/blog/page/4/` 与 Alignment 的精确邻接可以支持本段观察，不支持整个 Research 历史零事件。14 行到期源均存在；缺失历史入口有有限失败和具名重开条件，不将其记为覆盖通过。

实际读 GITHUB_WINDOW/GITHUB_WORLDPLAY 原响应并核本日时刻；Video1.5 三条在右界之后，WorldPlay 十条中六条 committedDate 落窗，均不因此取得公开时间。独立打开 WorldPlay d290dee、b26dfb3、8b0b8b9、86988c0 精确官方 patch；合并输出截断的 b26dfb3 已单独补读受影响代码。token 维广播后分片、module 调用入口与显式返回 positive/negative KV 的差额确实存在；不以未运行的 patch 证明 SP8/offload 正确或性能改善，日期继续隔离。

## T5Gemma 2：源审与 Books

独立 HTTP 读取[官方 Blog](https://blog.google/innovation-and-ai/technology/developers-tools/t5gemma-2/) JSON-LD：`datePublished=2025-12-18T18:30:00+00:00`，即本窗 12/19 02:30+08；`dateModified=2026-03-19T17:48:17.592801+00:00`。这是 release 身份，不把时刻赋给论文首次公告，也不称当前页面是不可变发布快照。

实际读[精确 v1](https://arxiv.org/html/2512.14856v1)完整题摘、§2、§3、Table1–5 和相关讨论。三处 embedding 共享、decoder Q 来自 X 而 K/V 来自 [X;H] 的共享投影、联合归一化与可见性 mask 有具体结构差额，不能等同两次独立 softmax。2+2+2=6 可接受，不按机构或参数规模评分。

Table1 的 Gemma2/400B/PrefixLM+KD 消融与最终 Gemma3/约2T/UL2 配方分开；减少 cross-attention 层的退步和跨模型配置混杂已保留。支持局部参数/架构取舍，不证明严格非劣性、所有任务支配、蒸馏普遍无用或端到端加速。官方 Blog 仅发布 pretrained checkpoints，轻量 posttraining 图不授 production/IT 产物。作者现有必要结论未越过这些证据。

实际对读 `MODEL-DECODER-ONLY` Ch18 开头至100行，尤其 Encoder-decoder 小节标准两套 stack/cross-attention 段；相邻 Ch17 开头至100行、Ch19开头至90行亦读。标准信息流边界合理，但不承载共享投影/联合归一化分支。`BOOKS_T5GEMMA_PROPOSAL.md` 的 Ch18 局部替换方向成立，保留标准结构和质量反例，唯一 owner 不转去 cache 章。当前未见该局部修改实际落实，需 root 协调，再由非 writer 写后核验；不能预签“已有覆盖/整合完成”。

## 必须补正的已发现身份

四组原始查询与 ADMISSION 对读发现以下12个身份未有可复查具体处置。现已由非作者实际读各自 exact v1 完整题摘；应由作者补入当日记录并同步普通待办，非重新扩池。

| 精确身份 | 本轮具体判断 |
| --- | --- |
| [19741 EdgeFlex](https://arxiv.org/html/2512.19741v1) | 定点§V–VII后贡献前关闭可接受：实际方法是 activation percentile pruning/AMP/既有量化顺序；没有新增调度或模型函数机制。A100 上未经任务适配的 CIFAR10 约随机准确率，不建立其声称的质量约束下 edge 可行性；不采用6倍/安全保证，也不因“组合”二字直接关闭。 |
| [15980 ClassLAR](https://arxiv.org/abs/2512.15980v1) | 关闭：类名/包名语言 embedding 做 Java 模块恢复，新增论证限定软件架构相似度/运行时间，未改变模型表示形成或 Agent 执行机制。 |
| [16019 Social navigation perception](https://arxiv.org/abs/2512.16019v1) | potential：同用户 ICL 与运动特征消融可改变主观反馈 evaluator 的个体化条件；不等同真实机器人控制改善。 |
| [16036 Higher education](https://arxiv.org/abs/2512.16036v1) | 关闭：课程政策 topic-model/LLM 分类，实际新增是该文本分类应用表现，不是 GenAI 的可靠性控制。 |
| [16143 SegGraph](https://arxiv.org/abs/2512.16143v1) | potential：SAM segment overlap/adjacency 图与 view-direction weighted 2D→3D 融合，具体解决几何/segment一致性，不按part-segmentation领域标签关闭。 |
| [15249 Medical fairness](https://arxiv.org/abs/2512.15249v1) | 范围关闭：实际贡献围绕皮肤/眼底疾病诊断 certainty 与 subgroup漏诊，AI for Science 暂缓；不采用临床保证。 |
| [15562 Channel estimation](https://arxiv.org/abs/2512.15562v1) | 关闭：CSI 预测先验与 pilot measurements 融合的无线估计系统；摘要的 generalizable 宣称没有建立通用模型学习或主线执行机制差额。 |
| [16948 AVM](https://arxiv.org/abs/2512.16948v1) | 范围关闭：冻结 ViT/subject modulation 用于 mouse V1 神经响应建模，贡献仍是生物领域建模，不能由未来 biologically inspired 动机重引入。 |
| [15414 Packed malware](https://arxiv.org/abs/2512.15414v1) | 关闭：byte-plot CNN/传统特征检出 packed executable，安全用途不等于 LLM/Agent 的安全反证或新执行机制。 |
| [15088 SigMA](https://arxiv.org/html/2512.15088v1) | potential：定点§3及§5，lifted subpath 的截断 signature 后作 attention，将输入长度与模型维度分离并有 stride/精度取舍；保留表示替代设计，不采用金融/电池应用成果或将截断当无损。 |
| [15248 Moralization](https://arxiv.org/abs/2512.15248v1) | potential：实际 prompt 条件比较中详细指令比 few-shot/explanation 更有效，并暴露主观 annotation 依赖；只保留 prompt/evaluator 有效条件，不以新语料数量准入。 |
| [15564 SAM3 remote sensing](https://arxiv.org/abs/2512.15564v1) | potential：semantic/geometric/hybrid 输入、监督量和形状的比较揭示 text alignment/边界误差条件；只保留 foundation 表示迁移反证，不采用遥感领域产出。 |

这些 potential 全部仍 first-public hold，不评分、不成为本日确定候选、不进入 Books。明确关闭的身份无需继续追不影响处置的日期。

## 两项原负侧应重开

- [15957 CAMP-VLM v1](https://arxiv.org/html/2512.15957v1)：实际读§3.2–3.3、§4.2–4.5/Table4–5。保留为 potential 的最小差额是相同预测设置中 semantic similarity 与 exact action accuracy 分离、人数增多的质量边界，而非把 scene graph/SFT/DPO 包装成新控制机制。没有独立无SG消融，不采用 SG 单机制收益；原“摘要无新机制/主要下游准确率”理由遗漏可读评价反证。
- [15082 FEAML v1](https://arxiv.org/html/2512.15082v1)：实际读方法 prompt/生成执行/筛选和 Ablation。metadata 与 label-cooccurrence 消融有局部提示信息条件，不能声称只任务提分无具体条件；保留 potential。Eq2 的 conditional probability 分母按印刷式为 count，而 Eq1 已除 n，存在归一化需核；静态检查 + exec 不证明 runtime safety。只保留待核解释，不采用普适收益/安全保证。

## 安全、反证与分层负侧

本轮除 T5 完整題摘/正文外，独立实际读40个唯一官方 exact-v1 完整题摘：

- 安全/设计反证18项：15081/15235/15617/15688/15892/16029/16030/16041/15649/15468/15163/16059/15782/15792/15275/17953/15423/15596（均2512）。各项potential和证据收窄无新增本窗采用；模拟 monetary loss、privileged agent风险、DP审计经验、judge一致性、OCR与长上下文等均不升级为一般保证。
- 风险负侧及按模型/系统/数据/评价理由分层18项：19741/15980/16019/16143/15562/15249/16948/15088/15353/15722/15957/15943/15082/15798/15979/15397（2512）及2601.06047、2602.23367。15353只引用既有诗歌攻击结果而没有新增葡语实验；2601.06047哲学解释未形成可核新干预/理论假设；HumanMCP新增persona数据但未给可靠性测试，原关闭可保留。其余闭合理由未变化，不称已全量深审附件。
- 另四项遗漏身份全文题摘：16036/15414/15248/15564（2512），具体判断见上。

另独立打开 GPT5.2Codex addendum §3–4.2/Table4、Vend2 的核心失败/限制、wellbeing 核心与全部修订脚注、精确 dated Model Spec definitions/U18节及当前 Skills specification。Codex 冲突编辑 RL 有潜力但跨模型0.75→0.76非干净因果；Vend2同底座共振/退款替换折扣不授CEO盈利因果；wellbeing旧70与当前91及编辑年代矛盾不能静默覆写历史；当前Skills schema不是Dec18旧版。现有日精度/历史版本隔离可保留，不反复同接口。

未独立逐项打开所有其他 datehold potential 的全文和所有标题明确范围外库存；这些没有被当作确定入选或书稿采用，抽读不称全量验证。

## 待协调与验收

作者应补12个已发现身份的具体记录及两项负侧改判，同步 README§1/§5 的 ordinary0 声称。root协调 Ch18局部 Books 修改或提供实际已有覆盖段；共享写入后非作者核上下文/引用。两类均普通可执行待办，不能作为终态外部项。

此前本日 V3 格式校验通过，不代语义验收；本记录和§6写入后再次校验。日期外部保留继续隔离。报告状态保持进行中，下一日20独立重读上下文，不等本日 Gate。

## 2026-10-02T20:11:01+08:00 Books局部POST

root已将Ch18原Encoder-decoder末段替为两段。非writer实际重开v1§2–3/Table1并复用已核Table2–5，顺读新段前后Encoder-only/Decoder-only及Ch17/19开篇；全embedding共享、[X;H]投影/共同softmax和global-only退步准确，Gemma2-2B/400B/PrefixLM+KD不倒填最终Gemma3配方。局部POST通过，仅改本family授权末注POST状态，不改正文，不授加速/能耗或全任务非劣性。12漏项/两负侧及README实际处置同步尚待作者，日级仍未通过。

## 2026-10-02T20:46:02+08:00 作者差额闭环

本日恢复重读七项上下文和checkpoint，实际回查AUTHOR_REVIEW_RECONCILIATION全部14行及正式§1–5；12遗漏的具体close/potential和两误关重开与本记录具名exact-v1/必要原文相符，保留CAMP评价proxy与FEAML归一化/执行安全边界。T5正式处置已同步root真实整合及非writer POST，本家族无Books任务。未变化的40项题摘/具名必要源审复用，不冒称重复全文或全库存验证。

语义独立结论通过；无未处理扫描、准入、必要阅读、Books或实质作者差额。§5已有隔离/精确重开条件但未显式满足完成态接口“终态保留项/不用于正面证据”，已通知作者仅补该措辞，未越权改§1–5。metadata暂进行中、§6分行通过并明确这一格式待办；该项不是外部受阻，落实后只做完成态复验。

## 2026-10-02T20:59:07+08:00 授权窄修与完成态复验

用户明确授权与18相同的状态措辞窄修：仅同步正式§1/§5已验收后的旧句、显式终态隔离及不用于正面证据字段，metadata完成、§6移除旧格式待办。未改材料处置、证据结论或共享Books，未重读未变化原文。完成态V3校验实际通过，限定两文件git diff --check通过。普通可执行项0，日级非作者结论通过；保留项仍不授Evidence/Coverage通过或无遗漏保证。
