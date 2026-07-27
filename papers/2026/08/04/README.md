# AI Research Daily — 2026-08-04

> Research window: 2026-08-02 01:48 至 2026-08-04 01:48（过去 48 小时，Asia/Shanghai）
>
> Accessed: 2026-08-04（Asia/Shanghai）
>
> Scope: 官方 Research / Blog、arXiv recent、学术 discovery index、官方 GitHub Releases
>
> Organization: 模型与研究机构 → arXiv / 学术来源 → AI Infra 与工程项目

## Executive Summary

周一 arXiv 新批次补上了昨天凌晨尚未公开的论文。本轮保留三项系统候选：TokTier 把
tokenization 从每请求无状态前处理提升为有 correctness contract 的会话状态；Aries 把 Agent
Serving 的性能对象从单次模型请求提升为完整 trajectory；CAGE 讨论 typed tool return 在离散
provenance 与连续数值同时漂移时，为什么点式授权和分离检查都可能失效。

三项证据都来自 2026-07-31 提交、2026-08-03 recent batch 首次可见的 arXiv preprint，尚无
独立复现。它们证明的范围不同：TokTier 给出较完整的实现、reference-equivalence 验证和
Serving 实验；Aries 提供 trajectory observability 与资源联动的初步实证；CAGE 在明确、受限
的 threat model 下证明联合不确定邻域的必要性。作者 workload 和 benchmark 均不外推为通用
性能或安全结论。

Books Integration 只吸收 TokTier 揭示的长期机制：在长会话、小增量、prefix KV 高复用的
workload 中，Tokenizer 也会成为有 identity、lifetime、fallback 和 verification 的 runtime
state。Aries 的核心观点在 Ch80 已有章节级 owner；CAGE 仍缺跨 turn、tool selection 与任意
prompt injection 的证据，先保留到本周 Weekly。今天是 Tuesday，不生成 2026-W32 Weekly。

## 1. 模型与研究机构

### Source Coverage

按 `CODEX_DAILY_RESEARCH_PROMPT.md` 的固定顺序扫描。机构页面在访问时没有显示 8 月 3～4
日、同时提供可核验机制的新模型报告或 Research 发布。

| Order | Institution / source | Actual observation | Decision |
| ---: | --- | --- | --- |
| 1 | OpenAI | Research 首页未见窗口内新增研究 | No Material Update |
| 2 | Anthropic | 最新可见 Research 仍为 2026-07-28 cryptanalysis，已进入 W31 | Deduplicated |
| 3 | Apple ML Research | 未识别到窗口内可核验的一手更新 | No Material Update |
| 4 | Google DeepMind | News 首页最新可见项目仍为 2026 年 7 月条目 | No Material Update |
| 5 | Google Research | 最新可见 Blog 仍为 2026-07-30 ScientistOne，已进入 W31 | Deduplicated |
| 6 | Meta AI / FAIR | Blog 未显示窗口内新增研究 | No Material Update |
| 7 | Microsoft Research | Blog 未显示窗口内新增研究 | No Material Update |
| 8～26 | NVIDIA；xAI；Amazon；Cohere；Ai2；Mistral；国内一线模型与研究机构 | 定向检查未发现窗口内新的 technical report / model card | No Material Update |
| 27 | Hugging Face Blog | 近期条目主要为 community / partner 内容，未形成可独立核验的长期机制 | Ignored Noise |

### Evidence Level

- **官方事实**：上述公开入口在访问时没有显示符合窗口与证据门槛的新条目。
- **边界**：页面排序、索引延迟、时区与未公开渠道均可能造成漏项。
- **不得推断**：不能由公开 Blog 无更新推出机构内部没有新研究。

## 2. arXiv / 学术来源

### Source Coverage

依次检查 `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR` 与 `stat.ML` recent。三项主候选的
arXiv v1 均标注 2026-07-31 提交，但在 8 月 3 日 Monday batch 才进入 recent 列表；W31 在
8 月 2 日已经闭合，故本 Daily 如实记录“延迟可见事件”，并保留 first-public metadata，不能
把论文伪造成 8 月 4 日提交。

Google Scholar、Semantic Scholar、OpenAlex 与 DBLP 只用于 discovery、metadata 与去重，
不用于替代全文或证明机制。本轮技术判断全部回到 arXiv HTML 正文。

### Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TokTier | 5 | 4 | 5 | 4 | 5 | 4 | 27 | Must Read；Refine Ch11 |
| Aries | 4 | 5 | 4 | 4 | 5 | 5 | 27 | Must Read；Weekly synthesis |
| CAGE | 5 | 4 | 4 | 4 | 5 | 4 | 26 | Must Read；Status: Experimental |
| ResKV | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Full review complete 2026-08-13；v1 owner 回拨 W31；Experimental |
| SLIM | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Full review complete 2026-08-13；v1 owner 回拨 W31；Experimental |

评分中的 `SR=4` 表示可阅读全文、实现或 artifact 证据较完整，但仍是作者 preprint；不等于
peer review、独立复现或 production validation。

### Deep Analysis 1 — TokTier

**Why。** 传统无状态 tokenizer 面向一次性请求很合理：实现简单，也容易与 checkpoint 的
reference artifact 对齐。但 Agent 会在同一 session 中反复发送长前缀和短 append。后端即使
命中 prefix KV，前端仍扫描完整文本，累计工作可能随会话增长而快速放大。

**Principle。** Tokenization 并不满足简单拼接律：`tok(A) ++ tok(B)` 一般不等于
`tok(A ++ B)`。Normalization、pre-tokenization 和 BPE merge 都可能跨越 append 边界；增量
优化必须以“结果逐 id 等于冻结 reference tokenizer”为 correctness contract。

**Mechanism。** TokTier 维护每个 session 的 token ids、byte spans、tokenizer content hash /
version 和 family-specific boundary certificate。新 append 到来时只重算受影响 suffix，找到
稳定相等边界后复用更早结果；无法证明时扩大窗口并最终回退完整 reference。GPU full path
服务 state miss，unsupported family / short input / failure 留在 CPU reference path；sampled
shadow verifier 比较 reference 并 quarantine mismatch。

**Trade-off。** 增量状态比 KV state 小且可拥有不同 lifetime，却新增 session affinity、
replication、version invalidation、admission 和 recovery。作者报告的收益依赖其 workload：
153,951 次 Claude Code / Codex CLI calls，median append 约 1.4K characters、context 约
86K～123K tokens、prompt-cache hit 94.1%；系统为 dual AMD EPYC 9115、4×RTX PRO 6000
Blackwell 96GB、vLLM 0.25。作者还观察到 fully prewarmed cache 在较短输入可更快，而 KV
容量失效并触发完整 prefill 时，tokenization placement 也不再主导。上述数字不能外推。

**Connection。** 主 owner 是 Ch11；它与 Ch46 的 prefix KV reuse 是 `Layering / Dependency`。
书稿吸收 correctness、state ownership 和共存边界，不复制作者 speedup。

**Evolution。** `stateless full tokenization → prefix KV 暴露上游重复工作 → verified incremental
tokenization → tokenizer/KV state 分离治理`。旧方案在短请求、大 delta、不支持的 tokenizer
family 或 prefix cache 已失效时仍成立。

### Deep Analysis 2 — Aries

**Why。** TTFT、TPOT 和单请求吞吐只覆盖模型调用，Agent 的 end-to-end critical path 还包含
harness、tool、sandbox、持久 context 与多轮因果关系。

**Principle。** 优化对象应是一个 user task 的 ordered trajectory，而不是把每次模型调用当作
独立样本。模型、工具和环境事件需要共享 trajectory id、因果关系与顺序 metadata。

**Mechanism。** Aries 分离 task specification 与 execution specification，以 adapter 连接 LLM
和 stateful sandbox，并把 model invocation、tool result、harness decision 汇入统一事件流。
这样才能把排队、KV 容量、tool tail、sandbox burst 与最终 task outcome 放在同一 critical path。

**Trade-off。** 统一telemetry增加 schema、clock/causality、trace volume 和跨组件 ownership；
stateful sandbox 的 scale-to-zero 还可能被 snapshot/restore 成本抵消。作者 controlled study 使用
OpenHands / Hermes / OpenClaw、三类 benchmark，每类 20 tasks、5 repeats，Qwen3.6-35B-A3B
FP8、SGLang、96-core host 与 H100 94GB；production trace 也没有完成跨层时钟同步。因此工具
耗时占比、KV capacity 和 queue 数字都是所测 workload 的观察，不是通用比例。

**Connection。** Ch80 已有 trajectory、control/execution/evidence plane、跨时间尺度 scheduling
和 task-level evaluation；本项是 `No Change — Already Covered`。Weekly 可用它校验现有论证，
不在 Ch62/65/66/77 重复同一段。

**Evolution。** `request-centric serving → multi-step Agent runtime → trajectory-visible serving`；
单请求指标仍是局部诊断量，但不能单独代表用户任务 SLO。

### Deep Analysis 3 — CAGE

**Why。** 典型 tool gate 只检查模型实际返回的一个 typed value。即便离散 provenance 变化和
连续数值小漂移分别看都安全，二者联合变化仍可能跨越 policy boundary。

**Principle。** 分量安全不自动组合成联合安全。若返回值为 `z=(s,x)`，授权应覆盖离散邻域与
连续 ball 的笛卡尔积，并在任一邻近分支无法证明安全时 abstain。

**Mechanism。** CAGE 枚举离散邻域，并对每一分支认证连续范围；Exact 适用于可执行 affine
policy，Lipschitz / randomized smoothing 适用于 learned gate，MILP 作为离线 ceiling。只有
Exact 对 policy fragment 给出 policy-level certificate；learned gate 的 certificate 仍受其与
真实 policy fidelity 限制。

**Trade-off。** 机制依赖 validated constructor、complete mediation、可枚举的低维 typed state
和已校准 threat budget。它不覆盖任意 prompt injection、tool selection、跨 turn 累积、MCP
metadata 或 multi-step execution；staleness 超出 freshness window 也会逃逸。保守认证会在安全
边界附近增加 abstention。论文在 OpenFisca、Kubernetes/Kyverno、MCP side effects 等 authored
policy 上实验，但这不是通用 Agent 安全证明。

**Connection。** 与 Ch68 的 deterministic authorization 是 `Direct Evolution` 候选，与 Ch74 /
Ch79 是短 handoff。由于目前仅一篇受限 preprint，先标记 `Status: Experimental`，不立即把其
认证算法写成平台默认设计。

**Evolution。** `model proposal → point validation → deterministic authorization → uncertainty-aware
joint certification`。旧的点式 gate 在输入已经由可信系统确定、没有需要覆盖的 return
uncertainty 时仍合理。

### Evidence Level

- **论文实验结论**：三篇论文的机制、实验设置和 limitations 来自作者正文与 artifact。
- **官方事实**：submission metadata 与 revision 来自 arXiv；当前均为 v1 preprint。
- **自己的推断**：TokTier 的长期 owner 归 Ch11、Aries 已被 Ch80 覆盖、CAGE 等待跨来源确认，
  是基于本仓库知识树的 integration judgment。
- **不得推断**：作者 speedup、延迟占比、certification rate 和 chosen threat budget 均不得外推
  到未披露模型、硬件、并发、输入长度、SLO 或安全环境。

## 3. AI Infra 与工程项目

### Source Coverage

按固定项目顺序检查 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、
TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Hugging Face、DeepSpeed、Megatron-LM、
Unsloth、MLX、llama.cpp、ONNX Runtime、OpenXLA 与 MCP。

| Project | Latest primary-source state observed | Decision |
| --- | --- | --- |
| vLLM | 最新稳定 Release 仍为 `v0.26.0`，2026-07-27 | W31 deduplicated |
| SGLang | 最新 Release 仍为 `v0.5.16`，2026-07-25 | W30/W31 deduplicated |
| NVIDIA Dynamo | 最新可见项仍为 2026-07-27 Kimi K3 dev snapshot | W31 record only |
| TensorRT-LLM | 2026-07-31 的 `rc23` 属 pre-release 且早于本窗口 | W31 coverage note；不作为今日事件 |
| MCP | 最新稳定规范仍为 `2026-07-28` | W31 deduplicated |
| 其余项目 | 未识别到窗口内改变 correctness、state ownership、failure semantics 或 SLO 的正式 Release | No Material Update |

普通 dependency bump、continuous build、未合并 PR 与缺少设计说明的 patch 不进入候选。

### Evidence Level

GitHub Release / signed tag 只能证明版本事实；没有对应文档、代码路径和 workload contract 时，
不能推断生产成熟度或性能收益。

## Knowledge Tree Position

| Candidate | Primary owner | Adjacent chapters read | Books decision |
| --- | --- | --- | --- |
| TokTier | Ch11 Tokenizer | Ch10, Ch12；检查 Ch46 handoff | Refine — Existing Argument |
| Aries | Ch80 Agent Platform | Ch79 与 Ch80；对照 Ch62/65/66/77 | No Change — Already Covered |
| CAGE | Ch68 Security | Ch67～69；检查 Ch74/79 boundary | Weekly Only — Experimental |

没有新增 ROADMAP node、Part 或章节。每项技术只设置一个主 owner，跨章节不复制全文。

## Recommended Action

- 已在 Ch11 补入“无状态 full tokenization → verified incremental session state”的机制、正确性
  contract、state lifetime、fallback 与新旧方案共存边界。
- 在 2026-W32 结束时重新评估 CAGE：只有出现独立证据、跨 turn 扩展或与现有 policy-gate
  机制形成稳定演进链，才考虑 refine Ch68。
- 用 Aries 作为 Ch80 现有 trajectory runtime 论证的验证来源；除非 Weekly 发现新的 owner
  缺口，不重复修改 Ch62/65/66/77。
- ResKV 与 SLIM 已在 2026-08-13 完成全文；因 v1 均为 2026-07-31，owner 已回拨 W31。8 月 4 日
  Daily 只保留 delayed-discovery 节点，不在 W32 重复计分。

## Books Integration

### Absorbed

- `books/part-02-model/11-tokenizer.md`：新增会话级增量 tokenization。正文保留旧无状态实现成立
  的条件，并将 exact reference equivalence、版本绑定、稳定边界、fallback、shadow verification、
  state lifetime 与 failure modes 写入长期机制。
- `docs/LEARNING_STATE.md`：同步这一稳定认知，不把论文性能数字沉淀为通用结论。

### Not Absorbed

- **Aries**：Ch80 已明确把 trajectory 作为 Agent Platform 的 observability、scheduling 与
  evaluation 单位；论文提供支持证据，但没有形成新的章节机制。
- **CAGE**：联合认证具有机制价值，但 threat model 受限，跨 turn 和任意 tool-chain 未覆盖，
  暂不把 preprint 算法写成 production security 默认项。
- **ResKV / SLIM**：2026-08-13 已完成全文 Source Packet；分别形成 Ch41、Ch52 的 Experimental
  refine candidates。Historical Books Gate 关闭，未修改 Books。

## Ignored Noise

- 8 月 3 日 recent list 中与 AI System Design 关联弱、只有标题或摘要的新论文。
- Tool Specifications Matter、LightMem reproduction、Model or Harness 等可能有交叉价值、但未进入
  本轮三项 deep-analysis 名额的条目；保留 discovery，不伪装成已全文审计。
- Hugging Face community challenge、模型排行榜、搜索引擎重收录与营销 benchmark。
- 缺少模型、硬件、precision、input/output length、batch、concurrency 与 SLO 的性能 headline。

## Repository Changes

- 新增 `papers/2026/08/04/README.md`。
- Refine `books/part-02-model/11-tokenizer.md`。
- 同步 `docs/LEARNING_STATE.md`。
- 未修改 ROADMAP、`docs/DECISIONS.md` 或 Weekly index；未生成 provisional `2026-W32`。
- 保留运行前已有的 `docs/DECISIONS.md` 修改与未跟踪 `interview/`；未执行 stage、unstage、
  commit、push、reset、checkout 或 clean。

## Recovery Addendum — 2026-08-13

- ResKV arXiv:2607.29591v1 与 SLIM arXiv:2607.29575v1 均标注 2026-07-31；W31 是唯一 owner。
- ResKV 已核验 main/residual fixed-budget cache、shared-softmax、dynamic gate、LongBench/RULER、
  single-A100 条件及 residual refresh / serving coverage limitations。
- SLIM 已核验 saturation-aware attention traffic model、configuration selection、2/4 H100 条件、
  calibration error 与 communication/interference 外推边界。
- 本 Addendum 修复访问状态与 owner week，不伪装成 8 月 4 日实时全文阅读，也不修改 Books。

## Open Questions

1. TokTier 的 stable-boundary certificate 能否覆盖更多 WordPiece、normalizer 与 added-token 路径，
   且在 tokenizer revision 后低成本重新认证？
2. Tokenizer session state 在多 replica、failover 与 KV-independent eviction 下应由 gateway、
   scheduler 还是 tokenizer service 拥有？
3. Aries 的 trajectory telemetry 如何处理跨 host clock、partial trace 和工具不可观测区，才不会
   用不完整 critical path 误导调度？
4. CAGE 如何扩展到跨 turn uncertainty accumulation、tool selection 和多步 side effects，同时
   避免 certification-induced abstention 破坏可用性？

## Sources

访问日期均为 2026-08-04。

### Model and Institution Sources

- OpenAI Research: https://openai.com/research/
- Anthropic Research: https://www.anthropic.com/research
- Google DeepMind News: https://deepmind.google/blog/
- Google Research Blog: https://research.google/blog/
- Meta AI Blog: https://ai.meta.com/blog/
- Microsoft Research Blog: https://www.microsoft.com/en-us/research/blog/
- Hugging Face Blog: https://huggingface.co/blog

### Academic Sources

- TokTier abstract and metadata: https://arxiv.org/abs/2607.29678
- TokTier full HTML: https://arxiv.org/html/2607.29678
- Aries abstract and metadata: https://arxiv.org/abs/2607.29069
- Aries full HTML: https://arxiv.org/html/2607.29069
- CAGE abstract and metadata: https://arxiv.org/abs/2607.29190
- CAGE full HTML: https://arxiv.org/html/2607.29190
- ResKV: https://arxiv.org/abs/2607.29591
- SLIM: https://arxiv.org/abs/2607.29575
- arXiv cs.AI recent: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent: https://arxiv.org/list/cs.LG/recent
- arXiv cs.DC recent: https://arxiv.org/list/cs.DC/recent
- arXiv cs.IR recent: https://arxiv.org/list/cs.IR/recent
- arXiv stat.ML recent: https://arxiv.org/list/stat.ML/recent
- Google Scholar: https://scholar.google.com/
- Semantic Scholar: https://www.semanticscholar.org/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/

### Engineering Sources

- PyTorch Releases: https://github.com/pytorch/pytorch/releases
- vLLM Releases: https://github.com/vllm-project/vllm/releases
- SGLang Releases: https://github.com/sgl-project/sglang/releases
- NVIDIA Dynamo Releases: https://github.com/ai-dynamo/dynamo/releases
- TensorRT-LLM Releases: https://github.com/NVIDIA/TensorRT-LLM/releases
- MCP Releases: https://github.com/modelcontextprotocol/modelcontextprotocol/releases
