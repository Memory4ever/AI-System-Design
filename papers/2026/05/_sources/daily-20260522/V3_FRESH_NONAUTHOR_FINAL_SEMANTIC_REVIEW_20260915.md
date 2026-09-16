# 2026-05-22 Daily V3 fresh non-author final semantic review

**Reviewer:** fresh non-author reviewer（未参与本日 author corpus 或 root Books 写回）  
**Reviewed at:** 2026-09-15T21:34:52+08:00  
**Gate:** **FAIL — 保持 Ongoing**

## 结论

当前账面算术可复算，但 `150 retained` 不是可接受的语义冻结集合。V3 renderer 把 80 个恢复项、owner 和分数预先硬编码，再以正则模板为其余 517 项生成 closure；抽查已经同时命中 false negative、false positive、score inflation 与 exact-v1 版本污染，因此不能用 `667→150` 的比例或 JSON 自洽替代 denominator Gate。

三项 root Ch66 写回本身通过本次 fresh 写后语义复核；失败发生在 author screening / Evidence / No Change corpus，不要求撤回三段 Books 正文。

## 机械对账

- owner batch：`1334 = 22823 - 21490 + 1` 个全分类连续 ID；covered ledger 为 667 个唯一 arXiv ID / 667 个唯一 source family，范围均在 `2605.21490..2605.22823`。
- owner receipt route：`667 = 513 official OAI direct + 154 revision recovery`；官方公告时刻 `2026-05-21T20:00:00-04:00 = 2026-05-22T08:00:00+08:00`，早于 09:00 截点。
- 当前 ledger：`667 = 150 retained + 517 pre-denominator closure + 0 withdrawn`。
- 当前 Evidence / Books projection：`150 = 149 complete + 1 isolated blocker = 3 Integrate + 146 No Change + 1 Deferred`。
- 当前 score projection：`150 = 74 score-7 + 57 score-8 + 19 score-9`；同时 `150/150` 的 Design Delta 都被赋为 3，这一分布不是 Gate 失败的单独依据，但与下述逐项反例一起证明评分规则被机械化误用。

这些等式只说明当前文件彼此自洽；由于集合语义错误，不能登记为 canonical final arithmetic。

## Denominator blocker

### 生成方法不是逐项语义审阅

`render_v3_author_recert.py` 中 `RESTORED_IDS` 直接硬编码 80 个新增 retained，`OWNERS` 直接硬编码 owner；`score()` 只把总分 7/8/9 映射成 `3+2+2`、`3+2+3`、`3+3+3`。其余项目由 `closure_family()` 按 title/category 关键词选择固定理由。retained 的 `screening_reason` 则只复制摘要中第一句含 `propose/present/show/...` 的句子，没有合同要求的“旧约束 → 原文新增 → 被迫重考虑的选择”。

因此受影响的有界重审范围不是重扫来源，而是当前 author 新建 corpus 的 `597 = 80 hard-coded restored + 517 regex closure`；旧 70 个 identity/version/claim 未变的 replay 项可继续复用，除非受具体反例影响。

### 已确认的 closure 反例

下列项目的现有 closure 理由声称“无新机制 / 仅局部质量 / 仅综述”，但本地保存的 full abstract 已明确给出可定位的主线机制或评价反例。它们至少必须恢复到 contribution re-screen；这不是直接判 Integrate，仍须完成 exact-v1 Evidence、评分和当前 Books 比较。

| arXiv | closure 与摘要的直接矛盾 | 建议 owner / 定点重开命题 |
| --- | --- | --- |
| `2605.21661` | 将 reward-guided diffusion 的昂贵 test-time guidance 改为 hierarchical variational、amortized / semi-amortized policy，并显式形成 few-step quality–cost trade-off。 | `MULTIMODAL-GENERATIVE-PARADIGMS`；guidance control 在采样步中的 owner 与回退。 |
| `2605.21674` | 不是普通安全背景：THREAT 把 jailbreak discovery 写成多 LLM 迭代 search / non-convex optimization，并报告 attack-cost 边界。 | `PLATFORM-SECURITY`；攻击预算、搜索状态与防护评价。 |
| `2605.21834` | 明确指出 offline consistency SFT 的 memorization / capability regression，并提出以模型自身 response 为状态的 on-policy consistency objective。 | `TRAIN-RLHF`；on-policy state distribution、safety/capability trade-off。 |
| `2605.21911` | 现有理由写“术语/版图整理”，摘要却把 Fisher information ODE 定义为 state、noise schedule 定义为 control，并给出 KL sampling-error 上界与可调 schedule。 | `MULTIMODAL-GENERATIVE-PARADIGMS`；noise schedule 作为 control。 |
| `2605.22011` | 明确识别 DiT token reduction 的 input-similarity / recovery-error objective mismatch，并提出 prior-step output similarity、interval schedule 与 frequency-aware matching。 | `MULTIMODAL-GENERATIVE-PARADIGMS`；生成恢复误差与 token reduction。 |
| `2605.22012` | 明确指出 text CoT 会压缩连续 audio-visual evidence，并提出 interleaved latent state、feature supervision 与跨模态时间对齐。 | `MULTIMODAL-REPRESENTATION`；latent reasoning state 与 temporal identity。 |
| `2605.22223` | 给出 Transformer accessible output sequences 的架构上界，并解释即使 context / compute 无界仍出现的 sequence-capacity failure。 | `MODEL-DECODER-ONLY`；架构表达边界与输出容量。 |
| `2605.22372` | 明确指出局部 attention score pruning 被 sink 误导，并用 cumulative transition / lazy random walk 的 diffusion distance 改写 token-selection state。 | `MODEL-SELF-ATTENTION`；attention-flow pruning 与 sink failure。 |
| `2605.22534` | 9,799 个 human-reviewed agentic PR 与 717 个案例显示 merge/reject outcome 混入 workflow constraint 与 reviewer intervention，直接反驳 outcome-only evaluation。 | `PLATFORM-EVALUATION-SYSTEM`；interaction-aware EvalRun identity。 |
| `2605.22596` | 把每 factor 独立 control policy 的组合爆炸改为单一 shared diffusion score，并把 score error 传递为 closed-loop trajectory-tube certificate。 | `MULTIMODAL-EMBODIED-VLA`；factor composition、controller 与证据边界。 |
| `2605.22668` | 明确指出 uniform RoPE scaling 的 global-structure / fine-detail trade-off，并按每步 latent spectral energy 动态分配 attention scaling。 | `MULTIMODAL-GENERATIVE-PARADIGMS`；resolution extrapolation control。 |
| `2605.22671` | 明确指出短 horizon latent 与 static execution alignment 的 failure，提出 long-horizon behavior state 与 phase-conditioned action decoder。 | `MULTIMODAL-EMBODIED-VLA`；behavior state、progress control 与闭环边界。 |
| `2605.22705` | 不是局部任务结果：ToaST 以 split-tree inference 和 IP/LP vocabulary selection 直接改写 tokenizer construction，并给出 compression / LM 证据。 | `MODEL-TOKENIZER`；tokenizer objective、推理过程与上下文 trade-off。 |
| `2605.22765` | 明确发现 UDM plug-in ELBO 与常用 denoising objective 不匹配，给出 leave-one-out posterior 精确转换和 absorbing-state reformulation。 | `MULTIMODAL-GENERATIVE-PARADIGMS`；discrete diffusion objective / reverse dynamics。 |
| `2605.22818` | 把稀疏、因果不完整轨迹的刚性执行改为 reasoner 补全 secondary motion，并用 confidence-aware guidance 控制服从 / 修正。 | `MULTIMODAL-GENERATIVE-PARADIGMS`；motion-control state 与生成 fallback。 |
| `2605.22821` | 以 LP/convex optimization 替代 BPE/Unigram 的 greedy vocabulary construction，并提供距目标最优值的 certificate。 | `MODEL-TOKENIZER`；全局 tokenizer objective 与可证边界。 |

### 已确认的 retained 反例 / owner 错配

以下现有 retained reason 只复述摘要中的应用或资产描述，不能支持当前 `Design Delta=3` 与 owner；至少要退回 contribution calibration，除非作者能从原文给出合同要求的三段准入链：

- `2605.21821`：ABLE 是“用 LLM 生成 malware sandbox bypass rules”的垂直安全应用；摘要没有改变模型自身安全、Agent control ownership 或通用平台接口。当前 `PLATFORM-SECURITY` / 7 分属于误收。
- `2605.22602`：ToM persuasive-dialogue task、dataset 与 local reasoning framework 不等于 multi-agent coordination；当前 owner `AGENT-MULTI-AGENT` 明确错配，且摘要尚未给出可迁移的多 Agent 状态/协议增量。
- `2605.22720`：conflict-context scenario suite 提供领域评价资产与观测失败率，但摘要没有新增可迁移的 EvalSpec / scorer / release mechanism；当前 `PLATFORM-EVALUATION-SYSTEM` / 7 分不能成立。

这些反例跨越 `no_durable_ai_system_delta`、`local_model_or_task_quality_delta` 与 retained 集合，说明不能只定点修 16+3 项；须按上面的 597 项受影响范围重做语义筛选。

## exact-v1 / score / Books blocker

- 79 个 `official arXiv exact-v1 HTML live author recheck` 中，只有 3 个 Integrate (`2605.21492`、`2605.21515`、`2605.22714`) 有具体 section locator；其余 **76 个**统一写成 `exact-v1 full-text method/mechanism sections` / `evaluation/results sections` / `discussion/conclusion/limitations`，且没有 method/evaluation/limitations excerpt。这不能证明已读 exact-v1，更不能支撑 `deep_complete_author_side`。
- 这 76 项恰好全部投影为 No Change，因此 `146 No Change = 70 replay-backed + 76 generic-live` 虽然集合算术成立，后 76 项 Books comparison 没有可审计 adopted proposition / evidence boundary，整体 No Change Gate 失败。
- 150 个 candidate 全部被机械赋 `Design Delta=3`。对局部应用、单 benchmark 和窄模型改进仍应按材料实际 delta / reach / durability 评分；不能因想进入 deep review 倒推到 7–9 分。
- `2605.22714` 的 report、ledger 与 Evidence 把 **后续版本摘要**的 `84,088 API calls / 12 models / 5 providers` 写进 `arXiv:2605.22714v1`。当前官方 v1 明确是 `75,898 / 11 / 4`，且 paired ratio 等统计也不同；必须用 v1 正文修正 README、ledger adopted claim 与 Evidence，或明确切换所选版本后重新建立版本身份。

## 三项 Ch66 写后审查

三项正文均位于首个 `## Review notes`（当前行 3576）之前，start/end 各一次且全局唯一：

| Source family | marker 行 | fresh semantic judgment |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-21515` | 267 / 271 | PASS。保留 symbolic-program baseline，说明 prompt program 的 LLM/temperature/context 约束变化；release/evaluation owner、versioned prior、iid/exchangeability failure、held-out fallback 与受限实验边界完整。 |
| `SF-2026-ARXIV-2605-22714` | 1130 / 1134 | PASS。把 conversation history/polarity 明确为 Evaluation Identity，保留 fresh-context baseline、cache trade-off、balanced-history 非完备性、English/binary/three-domain 边界与 deterministic/human fallback。正文没有写入错误的 84,088/12/5 数字。 |
| `SF-2026-ARXIV-2605-21492` | 2129 / 2133 | PASS。保留 single-checkpoint attribution baseline，加入 collinearity/Rashomon constraint、seed/model-ensemble owner、tie/group trade-off、非对称因果/target drift failure 与 single-model disclosure fallback。 |

所以这三项 Books implementation 可以登记为 fresh post-write PASS；overall report 仍因 denominator / Evidence 失败保持 Ongoing。

## 已隔离保留项

- `2605.21545` 仍只保留 denominator identity；缺 official exact-v1 method/evaluation/limitations，不用于正面证据、No Change 或 Books。
- `SRC-META-AI` 空目录响应与 `SRC-TENCENT-HUNYUAN` 目录错误仍是 source-local terminal reservation；README / materials request 已明确不据此声称“无遗漏”。

这三项隔离本身合格，不是本次 FAIL 的原因。

## 精确返修队列

1. 不扩窗、不扩源；只重审当前 `597 = 80 restored + 517 closure` 的 title + full abstract。每项写可定位的“旧约束 → 新增机制/反例 → 被迫重考虑的选择”，先修上列 16 个漏收与 3 个误收/错 owner，再扩查共享模板理由的全部受影响项。
2. 对重审后的真实 retained 集合重新评分；删除 `score()` 的统一 `Design Delta=3` 映射，保存逐维理由。
3. 对最终 retained 中当前 76 个 generic-live 项及新恢复项，补 official exact-v1 的具体 method / evaluation / non-proof locator、采用命题、关键反证与边界；受阻则精确隔离，不得标 deep complete。
4. 修正 `2605.22714v1` 的版本污染：v1 为 `75,898 calls / 11 models / 4 providers`；若要采用 84,088/12/5，必须选择并声明对应后续版本而非继续标 v1。
5. 以修正后的 candidate / Evidence 集合重算 Books：现有 3 个 Ch66 binding 保留 PASS；重新逐项比较 No Change，只有发现真实新缺口才生成 root serialized queue，不由 author 修改 Books。
6. 完成后重新冻结 arithmetic / README / JSON，再由非 author 做 final semantic Gate。当前 reviewer 没有修改 Books，也没有把 author corpus 改判写回，因此本记录只是一份 FAIL queue，不冒充修复后的验收。

## 方法限制

本轮按 doubt-driven self-questioning 执行；由于这是 delegated non-interactive lane，skill 建议的 cross-model second opinion 未运行。该降级不改变上述直接可复算的代码、JSON、full-abstract 与 official exact-v1 反例。
