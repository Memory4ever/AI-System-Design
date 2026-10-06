# Oct03 本轮首批准入校准包

本轮作者：当前 Oct03 ownership 执行者 / Codex；原报告作者 Huygens。待 root 非作者独立校准，本文不是 FIRST/DAY 裁决。

用户于2026-10-07明确将本日补查交接；保留原窗口、旧候选日期/评分及有效审阅。新增窗口仅北京时间 **2025-10-02 ～ 2025-10-02**。本轮未用 catchup，未写共享 Books/State/合同/索引，未执行 Git 写操作。

## 1. 实际发现与停止

原报告已保存 [运行前副本](baseline-before-supplement-20261007.md)。原94完整题摘、23必要核心和原 FIRST/Euler DAY 的未变判断保留；仅定点读取旧 Atom 身份做去重，没有重读94/23或改原日期/分数。

本轮27个实际 HTTP 请求均200：Advanced 表单1、八个查询各首50结果、18个精确v1题摘。执行区间 `2026-10-07T12:05:32.204719+00:00` 至 `2026-10-07T12:42:44.285957+00:00`。每条实际 URL、起止时刻、状态、字节数、SHA256 在 [新原件目录](supplement-20261007/) 的同名 `.request.json`，旧原件未覆盖。下载与抽取不等阅读。

Advanced 公告表单 [实际原响应](supplement-20261007/advanced-form.raw)明示 **announcement date supports only year and month granularity**。八查询使用 Computer Science + cross-list、`from=2025-10` / `to=2025-11`、`announced_date_first` 升序、size50/start0；真实回显区间是 **2025-10-01 至 2025-11-30**，不是单日或仅十月。每页 Next 存在；全部停止第一页第50题名，未执行 start50，未读后页属于有界停止，不是外部故障。

| 原响应 | 实际 terms-0-term / all字段 | 总结果 / 本轮题名导航 |
| --- | --- | --- |
| [language](supplement-20261007/advanced-language-start0.raw) | `language model` | 4812 / 首50 |
| [moe](supplement-20261007/advanced-moe-start0.raw) | `mixture of experts` | 146 / 首50 |
| [systems](supplement-20261007/advanced-systems-start0.raw) | `LLM inference` | 506 / 首50 |
| [rl](supplement-20261007/advanced-rl-start0.raw) | `reinforcement learning language` | 548 / 首50 |
| [multimodal](supplement-20261007/advanced-multimodal-start0.raw) | `vision language` | 1087 / 首50 |
| [world 原宽入口](supplement-20261007/advanced-world-start0.raw) | `world model` | 1805 / 首50；多词匹配明显含无关应用，未逐项关闭 |
| [world 收窄](supplement-20261007/advanced-world-phrase-start0.raw) | `"world model"` | 96 / 首50；用于相关机制导航 |
| [agent 收窄](supplement-20261007/advanced-agent-phrase-start0.raw) | `"tool calling" OR "retrieval augmented" OR "agent memory"` | 384 / 首50 |

前六查询300次出现/248唯一题名、15旧身份；八查询合计400次出现/**340唯一题名、30旧身份、310本日旧身份集合之外**。具体身份/原响应/排名在 [机械库存](supplement-20261007/advanced-inventory-eight.json)。这是本日定点去重差额，不是340篇已筛选、310篇当天新论文或逐项全文队列。未将其他日期旧材料搬入本日；其他日期若存在同身份有效结果，后续仅定点核复用。

只从近窗机制及重要负侧线索选择18项，实际逐一读完整精确v1题名/摘要、当前页面 Comments 与版本史可见字段。未见这些页面中的明确撤回/纠错说明，不声称全站/全部版本无标记；当前新版本存在本身不证明重要修订，未拿新摘要覆盖历史v1。

## 2. 全部拟保留贡献潜力：15项

以下 **未评分、未授正面 Evidence、未进入 Books**。原文增量与待核实验分开；不是15个确定当日候选。root请核全部15份精确题摘与本节准入理由，不需全读340库存。

| 精确v1及本地题摘 | 旧约束 → 原文增量 → 值得核验的设计选择 / owner |
| --- | --- |
| [01161 M2PO](supplement-20261007/abs-2510.01161v1.txt) | 异步RL过旧rollout易崩溃 → 约束importance weight第二矩、定点抑制极端token → 能否容忍更大staleness而保留有效更新；TRAIN-PPO。256更新及等效性能是待核作者结果，不授所有异步系统 |
| [01270 PSR](supplement-20261007/abs-2510.01270v1.txt) | 安全自反思有推理开销 → progressive反思加轻量轮数预测 → 风险条件下计算分配与防御/效用取舍；PLATFORM-SECURITY。必须核攻击预算、adaptive攻击与predictor漏判，不把ASR数字当安全保证 |
| [01336 HiSpec](supplement-20261007/abs-2510.01336v1.txt) | draft加速仍受target验证限制 → early-exit中间验证与draft/verifier/target状态复用、周期target校验 → 验证成本/缓存兼容及精确性边界；INFER-SPECULATIVE-DECODING。摘要的without compromising accuracy不等采样分布等价 |
| [01394 Optimal Stopping](supplement-20261007/abs-2510.01394v1.txt) | 固定Best-of-N预算不适应reward → Pandora/UCB停止和跨prompt reward归一化 → 分布未知下何时继续生成；INFER-SCHEDULING。理论假设与reward模型代价需核，少生成不自动端到端加速 |
| [01624 Quagmires](supplement-20261007/abs-2510.01624v1.txt) | 常用SFT分数挑RL起点 → 多设置反例及held-out loss/Pass@large k代理 → 数据同质/长度/重复预算如何影响后续RL；TRAIN-SFT。重要设计负侧，不能因局部数学任务或Books可能已有主题而关闭 |
| [01643 Support Basis](supplement-20261007/abs-2510.01643v1.txt) | bounded-entry近似限制softmax应用 → 稀疏大项精确+稠密小项多项式、多阈值理论 → 放宽假设后的精度/运行时条件；MODEL-SELF-ATTENTION。不把渐近保证当已实现GPU吞吐 |
| [01645 Privacy](supplement-20261007/abs-2510.01645v1.txt) | 将隐私风险缩成训练记忆 → 全生命周期taxonomy/案例及1322篇研究偏向分析 → context/agent/deep-inference威胁是否被遗漏；PLATFORM-SECURITY。保留重要安全反侧，不以position/survey关闭；案例是否新增可支持边界需必要核心核验 |
| [01832 SCRIBES](supplement-20261007/abs-2510.01832v1.txt) | 每页面LLM抽取成本与泛化限制 → 站内layout相似作RL信号、可复用脚本及迭代合成标签 → 稳定结构摊销与结构变化失效；TRAIN-DATA。脚本质量及QA收益不当生产抓取保证 |
| [01857 IRL Reward](supplement-20261007/abs-2510.01857v1.txt) | 直接模仿expert风格不等过程质量 → adversarial IRL学dense token reward，训练/固定预算rerank复用 → reward是否区分正确性与表面形式；TRAIN-RLHF。仅此v1的GSM8K/Llama3/Qwen2.5范围，不借后出版本扩大 |
| [01994 CLAST](supplement-20261007/abs-2510.01994v1.txt) | ICL单测示例可读性改写会破坏执行语义 → 程序分析+分解/LLM改写，报告保留测试效力并改善后续ICL → 示例清晰度和可执行性不能互相替代；AGENT-CONTEXT。保留局部设计证据，不称新的LLM架构 |
| [02228 xLSTM](supplement-20261007/abs-2510.02228v1.txt) | 只看训练FLOP忽略context/部署 → IsoFLOP/拟合、compute-optimal与overtraining及推理context比较 → recurrent/Transformer选择与上下文长度耦合；MODEL-LONG-CONTEXT。v1不是最新摘要的Pareto-dominate加强说法 |
| [02324 CASAL](supplement-20261007/abs-2510.02324v1.txt) | 在线activation干预有运行成本 → 单层子模块摊销steering进权重 → 可否保留拒答/知识边界而减在线介入；TRAIN-SFT。30x/20x需预算与质量条件，不称生产就绪 |
| [02345 Dynamic MoE](supplement-20261007/abs-2510.02345v1.txt) | 专家负载/冗余/通信三重约束 → 参数+activation聚类、shared base/低秩residual、层级路由/异精度offload → 重排与压缩耦合取舍；MODEL-MOE。局部GLUE/WikiText不授大规模通信实测，机制潜力不因数字未核关闭 |
| [02287 Action Video](supplement-20261007/abs-2510.02287v1.txt) | text条件缺精细控制 → proprioception/force/muscle等多模态动作对齐、保留各模态信息并正则trajectory causality → 预测漂移与动作条件表示的选择；MULTIMODAL-WORLD-MODELS。模拟精度不等真实机器人安全 |
| [02373 A-MemGuard](supplement-20261007/abs-2510.02373v1.txt) | 孤立entry检查漏上下文触发并回写放大 → 多相关记忆reasoning共识+单独failure lesson memory → 信任、纠错与反馈污染边界；AGENT-MEMORY。95% ASR下降仅摘要待核，不能授adaptive/多次污染安全 |

15项里 **02228/02287当前arXiv v1提交分别为UTC10/02 17:14/17:57，即BJT10/03**，当前该arXiv事件不可能在本轮10/02自然日内；如有更早作者公开稿，只恢复那个事件身份与日期，不搬日期。其余13项也不能用submitted证明first-public，Advanced月公告不能给具体日。未知日期不是贡献关闭。后续必要日期恢复只针对这些身份，不能概括为2025论文查不到。

## 3. 代表性明确关闭：3项

三项都读完整精确v1题摘，日期未核实但关闭不依赖日期。不以小模型、局部结果或未知日期为理由。

| 精确题摘 | 原文实际内容与具体关闭理由 |
| --- | --- |
| [01635 MIMIC](supplement-20261007/abs-2510.01635v1.txt) | 游戏测试中persona引导不同playstyle，报告coverage/task completion提高；题摘没有辨识新的Agent执行机制、失效条件或可迁移质量/资源边界，仅应用策略多样性组合 |
| [01651 LadderMoE](supplement-20261007/abs-2510.01651v1.txt) | 金文数据、检测→识别与CLIP ladder MoE adapter，用于跨拍摄/拓片/描摹及长尾字符；题摘贡献落在识别pipeline/该领域准确率，未辨识可改变基础模型/系统选择的新增adapter机制或成立条件，不仅因考古领域排除 |
| [02157 VIS-ReAct](supplement-20261007/abs-2510.02157v1.txt) | visual workspace的semantic interaction由分析agent解释/规划，refinement agent改报告；case study验证targeted refinement/fidelity/透明度。没有辨识超出既有分析→改写分工的新增执行/状态一致性机制或失效边界，不用Agent命名准入 |

02157 v1提交UTC10/02 16:08（BJT10/03），这是额外日期事实，不是关闭理由。root请检查上述三种理由是否误关闭；任何重开只影响该项或相同错误理由集合。未对库存余项给出贡献关闭，无需扩340全文。

## 4. 精确 checkpoint

**首批包可独立校准；未获得本轮 FIRST/DAY。** root需实际检查八查询边界/停止、15拟保留和3代表关闭（全部18完整精确v1题摘），尤其PSR/Privacy/Quagmires/A-MemGuard负侧及LadderMoE/CLAST分界。无需重复旧94题摘/23必要核心，也无需读340库存。

作者可执行工作仍有：本轮14每日来源的实际有限补查/必要恢复、来源正文写回、被校准项的必要核心与具体日期事件恢复，以及任何成立的候选证据/评分/Books比较。它们是普通待办，不包装成外部故障。受首批准入影响的深入采用在独立校准后推进；没有未知日期就先关掉的 shortcut。共享Books若有长期差额仅提交唯一owner提案给root，不直接写入。

**首批落盘后同轮进展：** 14源有限入口及真实边界已继续执行/写回README，最终61请求及具名PASTA artifact卡差额见[作者记录](supplement-20261007.md)。本包上文27请求为首批发现快照，不覆盖后续真实执行。18题摘判断未变，仍等待root校准；不因此重抓八查询或扩340库存。后续必要核心/日期事件恢复及成立候选的证据/Books/非作者DAY仍属可执行工作。
