# AI Research Weekly — 2026-W15

> Coverage Window: 2026-04-06～2026-04-12
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: 31/31 scored candidate families have final Books dispositions; 25/25 accessible scored `20+` Full Source Reviews complete; 5/5 low-score boundaries complete; GameWorld remains one scored `Unverified / Blocked / No Books Change`; W15 Source-Family Books Gate Complete; broader Archive Completion Gate Open

> **Supersession boundary (2026-08-14):** 本文较早段落中的 `Books pending`、`provisional`、
> `Blocked — Not Started` 与 `Historical Books Gate Closed` 是 Source Review 阶段快照；它们由文末
> 31/31 Final Books Integration Ledger 取代。GameWorld 只保持 Archive Gate Open。

## Executive Summary

旧版 W15 只保留四个拆分后的机构 Source Families，不能证明完整论文窗口和 AI Infra 固定来源
没有其他候选。本轮重放 4 月 6～10 日 discovery feed、逐项核对 first-public date，恢复 14 个
in-window 学术候选，并将 9 个实际首发于 W11/W13/W14 的 curation-lag 条目移回 owner week。
ByteDance Seeduplex 将语音交互从 half-duplex 推向 full-duplex，暴露新的 runtime 问题：
同时 listen/speak 需要 interruption、turn-taking、noise suppression 与 latency stability
共同工作。Meta Muse Spark 与 Google 的 academic agents / user-simulator 研究提供模型和
评测案例，但没有同等系统证据。

本检查点完整复核 TriAttention。它从 post-RoPE attention observation 的短窗口局限出发，利用
pre-RoPE Q/K concentration 把未来 key importance 分解为 distance-sensitive trigonometric score
与 norm complement；这是一条“历史统计 → 离线校准 → 周期性 runtime eviction”的直接演进，
不是对所有 KV compression 的无条件替代。作者实验支持特定模型、KV budget 与 A100/H100
contract 下的 accuracy/memory/throughput trade-off，但未提供 production scheduler、prefix sharing、
tail latency 或多租户 SLO 证据。Memory Intelligence Agent（MIA）进一步把外部 workflow memory、
Planner 与 Executor 组织为“检索经验 → 规划/执行 → 压缩成功和失败轨迹 → 在线更新 Planner”的回路。
这条机制补充了 Agent Memory 从 raw trajectory 到 procedural policy 的演进，但公开证据不支持把它写成
可逆的“双向记忆转换”：memory unit 被清理后，参数更新缺少逐条 provenance、delete propagation 与
rollback；同一 Qwen3-32B family 又同时承担 Manager 和 unsupervised judge，错误可能相关地进入 memory
和 weights。SkillX 则把 procedural experience 拆成 planning、functional 与 atomic 三层，并用
pseudo-plan 作为中间 retrieval query；它补全了“相似任务检索”到“按当前执行步骤检索”的演进，
但同一 skill composition 对不同 base model 并非单调有益，反复 text refinement 也会 overfit。
PTE（Prefill Token Equivalents）的全文审计又把“Agent 用了多少 token”推进到 trajectory state cost：
每次 tool pause 后若 KV 不可复用，累计 context 会重新 Prefill；之后每个 decode token 又在更长 KV 上
付费。但它是带明确假设的 analytical proxy，不是 end-to-end latency 真值：8×H200/TP=8/256 并发验证
排除了 tool/network time；跨五类硬件只按理论峰值 HOI 对同一批 trajectories 重算，并未逐设备实测。
因此长期价值是把 cache reuse、context growth 与 tool schedule 纳入 EvalSpec，而不是保存模型 PTE 排名。
Agentic Skills in the Wild 又把“把正确 Skill 直接塞进 Context”拆成 selection、retrieval 与 adaptation
三道独立 failure surface。作者的 progressive setting 说明 curated-skill 上界不能代表真实 registry：
同一 model 与 harness 在 distractors、34K pool retrieval 和移除 task-specific skills 后会逐级退化，甚至低于
no-skill baseline。Query-specific refinement 可以在 retrieved evidence 已有足够 coverage 时恢复部分能力，
但它需要额外完整探索和 self-evaluation，也会在 Kimi/SkillsBench 条件下造成回归；因此它是受 retrieval
ceiling 约束的 task-local synthesis，不是从缺失知识中“自我创造 Skill”。MARS 再把多 token 候选从
独立 drafter/head 转成同一 AR backbone 的 masked-prediction capability：训练保持 causal attention、
right-shifted logits 与 left-to-right commit，同时用 clean AR loss 抵抗 block size 增大造成的 signal decay。
但它并非零成本或 lossless runtime optimization：训练序列翻倍，低 confidence threshold 会改变输出，
block-level KV cache 又引入 batch 内最慢请求同步与 idle。在 MARS 检查点，按最终 event-date 纠偏后的
14 个 `20+` 候选计，已有 7 项完成 Full Source Review。
FP4 Explore, BF16 Train 进一步展示了“低精度应按职责使用”：NVFP4 只扩大 deterministic diffusion
candidate search，保留 extreme seeds；BF16 重新生成实际训练 targets 并更新 policy。它减少的是被丢弃候选的
生成成本，不证明 quantized trajectory 可直接成为高精度 objective 的样本。理论界限又依赖 Lipschitz vector
field/reward、bounded error 与 i.i.d. Gaussian reward assumptions，不能替代逐 workload rank calibration。
Flux Attention 又把固定 dense/sparse layer 配比改成 prompt-conditioned layer routing：Router 只在 Prefill
读取 prompt 边界表征并决定每层走 Full Attention 或 Sparse Attention，Decode 复用该硬路由。它说明动态性
不能只看算法粒度：head-level routing 更灵活，却可能造成 mixed-length memory access 和 intra-layer
long tail；layer-level routing 损失细粒度，却更容易让 sparse layer 整体跳过远端 KV traffic。作者实验支持
单卡 A800、batch 1、BF16、特定 sparse kernels 下的 prefill/decode speedup，但 Decode 只是 kernel-level，
也没有 continuous batching、prefix sharing、TTFT/TPOT/p99 或 route/KV identity 证据。当前共 9 项完成
Full Source Review；Evidence Gate 仍打开，也不据论文摘要直接改写 Books。

SkillClaw 随后把“单个用户手工维护 Skill”推进为共享的 evidence-to-release loop：白天汇集多用户
session，按被引用 Skill 聚合成功不变量与失败修正目标，夜间生成 candidate，并在相同 environment/toolchain
下比较 old/new Skill 后才发布。全文与 artifact 审计同时否定了“共享经验会单调改善”的强说法：论文只报告
60 个任务中 4 类代表结果，executor、evolver 与 validator 均使用 Qwen3-Max，且没有独立 judge、held-out
隔离、统计不确定性、privacy/consent 或跨租户 poisoning contract。当前 repository 的 dashboard、Claude/Codex
integration 和 LongHorizon harness 又晚于 W15，不能回写成事件时实现。长期上，这篇论文支持的是
session evidence → candidate Skill → validation → governed rollout 的控制回路，而不是自动把用户轨迹写进
全局 registry；Ch80 已经覆盖 immutable Skill identity、provenance、canary、in-flight pinning、rollback 与
global-memory 写入边界，因此暂定 `No Change — Already Covered`，评分从 25 调整为 24。W15 现为
10/14 retained Full Source Reviews；其余 4 项继续逐项全文审计。

DMax 再把 diffusion LM 的 parallel decoding 从“一次 mask→token 后不可逆”推进到“已解码位置持续参与
self-revision”：On-Policy Uniform Training 用模型自己的预测错误构造 denoising 输入，Soft Parallel Decoding
再以 top-1 token embedding 与 mask embedding 的 confidence-weighted interpolation 保存不确定性，并在 block
预测稳定或全体 confidence 达阈值后提交。它不是 AR speculative decoding，也不是纯 runtime trick：模型必须
经 OPUT 学会处理 self-generated errors，直接把 SPD 用到原模型会 collapse。作者实验绑定 LLaDA-2.0-mini、
math/code self-distillation、8×H200 训练、2×H200 TP、batch 1、2048 生成长度；没有并发、queueing、KV/cache、
TTFT/TPOT/p99、energy、variance 或通用任务证据。评分因 work-in-progress 与 revision/artifact drift 从 26 调为
25，暂定 Ch40 Experimental refine、Ch29/44/52 handoff。W15 现为 11/15，余 4 项；Books Gate 仍关闭。

Externalization in LLM Agents 的 54 页全文把 weights → context → harness 解释为 representational
transformation：Memory 把跨时间状态从 recall 变成 retrieval，Skills 把临时 improvisation 变成可复用
procedure，Protocols 把自由文本 coordination 变成 typed contract，Harness 再以 loop、sandbox、approval、
observability、policy 与 context budget 协调三者。其有价值的部分是分层边界和双向代价，而非“外部化越多越好”：
外部 artifact 会引入 retrieval/routing latency、context contention、staleness、poisoning、protocol spoofing 与
governance overhead，稳定、低延迟、通用能力仍可留在 weights。该文是 narrative synthesis，没有 systematic
search/inclusion protocol、原始实验或可复现 artifact；现有 Ch71～80 已分别覆盖 Context/Memory/Tool/Workflow/
MCP/Platform ownership、version/provenance/rollback 和 model-harness evaluation boundary，因此暂定
`No Change — Already Covered`。W15 现为 12/14，余 KnowU-Bench、SPPO 两项。

KnowU-Bench 把 personalized/proactive Agent evaluation 从静态 intent recovery 推进到 live GUI 中的
feedback-conditioned policy：Agent 只看到 behavioral logs，hidden profile 由 user simulator 持有；Agent 必须
在 execute、ask/confirm 与 remain silent 之间决策，并在 rejection 后停止。它的可迁移价值不是某个模型排名，
而是把“主动性”拆成 Act、Silent、Stop 三个互相制衡的 operating points，并用 deterministic environment
checks 与 rubric-conditioned judge 分开验证 hard side effects 和 soft preference alignment。全文、Appendix、
project 与 current code 已核对；但四个 synthetic personas、LLM-generated logs、gpt-4o simulator、仅 26 条
human-rated judge calibration、无 simulator-human fidelity validation、无 uncertainty/hardware/cost/SLO 使结果
只能绑定作者 benchmark。Ch62 已有 feedback-conditioned trajectory 与 hybrid verifier 原则，但尚未显式冻结
initiative/restraint 的多轴 EvalSpec，故暂定 `Refine — Existing Argument (Experimental)`，Ch68/73/75/77/80
handoff。MolmoWeb 的完整复核随后确认 Ai2 已于 3 月 24 日首次公开模型、数据和评测工具，故该 Source
Family 连同完整 packet 回归 W13；4 月 9 日论文和 4 月 10 日完整代码只作为后续 artifact evolution。
W15 现为 13/14，仅余 SPPO。

SPPO 的 sole-v1、全部正文与 Appendices、控制任务、公开 verl fork、training scripts 和 Ch28～30 邻接
现已完成审计。它不是“无 Critic 的 GRPO”，而是在 token-state Critic 与 group empirical baseline 之间加入
prompt-only scalar Critic：单次 rollout 的 binary outcome 减去当前 policy 对 prompt solvability 的估计，再把
同一 advantage 广播到全部 response tokens。这样以 Critic state、forward/backward、calibration 与 policy-version
耦合换取 `N=1`，避免每 prompt 的 group rollout；它绕开 token-level temporal attribution，却没有识别哪一步
真正导致成败。作者只在 1.5B/7B math RLVR 与五个 deterministic sparse-reward control tasks 上给出证据，
且 `beta_KL=0`、无多 seed/uncertainty、critic 只做相关性而非完整 calibration audit。故 26 分不变，主 owner
修正为 Ch28，Ch29 handoff，暂定 `Refine — Existing Argument (Experimental)`。W15 recorded `20+` queue
达到 14/14；Discovery Recall Gate 仍因 fixed-source coverage 未闭合而保持打开。

固定来源回放随后恢复 7 个独立 source families。Meta Advanced AI Scaling Framework v2 把一次性
model evaluation 扩展为 threat model、capability/uplift assessment、deployment-context residual risk、
mitigation validation、named decision owner 与 preparedness-report refresh 的控制回路；它是厂商自述的
governance contract，不是外部安全认证。SGLang v0.5.10 则同时暴露三个不能混写的 runtime mechanism：
piecewise CUDA Graph 降低复杂控制流的 graph/memory 开销，Elastic NIXL-EP 在部分 GPU 故障后重分配
expert ownership，PD staging buffer 把分散 GQA head slices 聚成连续传输；release headline 未披露完整
model、precision、length、并发、topology 与 SLO，故不能写成通用倍数。

4 月 11 日 arXiv replay 又恢复 CodeComp、FinTrace 与 SinkTrack。CodeComp 把 attention-only KV eviction
推进为 query-conditioned chunk retrieval、Code Property Graph structural prior、per-chunk budget 与 span
protection；它支持“压缩 policy 必须理解 workload semantics”，却依赖 Joern/language coverage，且缺少
production concurrency/tail-SLO 与公开实现证据。FinTrace 把 tool-call success 拆为 action correctness、
efficiency、process quality 与 output quality；作者数据说明“选对工具”仍可能无法正确利用返回信息，但
LLM judge、FMP tool universe、金融分布及后续 revision 都限制外推。SinkTrack 则把被动 attention sink
改造成 BOS context anchor：硬替换会破坏原计算，静态融合受强度与 pooling 制约，dual-track cross-attention
才在指定层更新 BOS 并保留其余 token 的 causal self-attention；收益只绑定 3B～12B 作者模型与六个
benchmark，且 source context、cache identity、kernel/graph compatibility 与 server batching 仍是新增状态。

`Think in Strokes, Not Pixels` 的日期也已纠正为 4 月 6 日 v1。它将单次 image generation 变成
plan → draft → inspect → refine 的 interleaved text/visual trajectory，并以 scene-graph incremental data、
self-sampled correction 与两类 intermediate consistency supervision训练；这是 multimodal workflow 的
实验性机制，不证明 verbal planning、可解释性或多步生成在其他 modality 上普遍成立。Microsoft 4 月 9 日
New Future of Work 页面是多研究综合而非新的系统 mechanism，保留为 19 分边界事实。至此 W15 为
24 个 scored families、20/20 `20+` Full Source Reviews。

4 月 12 日 academic cross-index 随后解除原 attribution identity blocker：GameWorld、Process Reward Agents、
BERT-as-a-Judge、Many-Tier Instruction Hierarchy、SCOPE 与 Tracing the Roots 均恢复出 arXiv identifier；
后五项还恢复正文并完成非模板化全文审计。GameWorld 的 identity、abstract、project 与 repository
也已核对，但 23 页 primary PDF 当前没有稳定可读入口，故不计为全文审计。SkVM 也已定位，但其 v1 是
4 月 3 日，4 月 6/11 日只是 v2/v3，故完整 Source Family 回拨 W14。随后固定 Infra 入口复核补记
TensorRT-LLM `v1.3.0rc11` 这一 18 分
pre-release boundary：它只证明 4 月 9 日存在候选版本和 release-note surface，不证明 RC 功能已经形成
稳定、可迁移的 runtime contract。最终 W15 为 31 个 scored families、25/25 accessible `20+` reviews、
1 blocked、5/5 low-score boundaries。academic 与当前可访问的 immutable Infra checkpoint 均通过；
全历史 Evidence Gate 与 Historical Books Gate 仍保持打开。

## Coverage and Source Coverage

- 模型与研究机构：保留 Meta 4 月 7 日 Scaling Framework v2、4 月 8 日 Muse Spark、Microsoft
  4 月 9 日 Future of Work、Google 4 月 8/9 日与 Seed 4 月 9 日；OpenAI、Anthropic、Apple、
  DeepMind、NVIDIA、Amazon 与 Ai2 的可访问官方索引已回放，其他动态/不可变历史边界继续列为限制。
- 论文与学术来源：Seeduplex 性能为厂商研究且无独立复现；HF 04-06～10 已作第一轮
  discovery replay；04-11 的 CodeComp、FinTrace、SinkTrack，以及 04-12 的 SCOPE、Tracing the Roots
  已由 arXiv metadata/full HTML 补回；OpenAlex、DBLP、Scholar 与 Semantic Scholar 用于 metadata/
  duplicate cross-check，机制证据仍回到 arXiv/作者 artifact。W15 academic cross-index checkpoint passed。
- AI Infra：SGLang v0.5.10 已按 4 月 6 日 official release 补回并审计；vLLM v0.19.0 已确认是
  W14（4 月 3 日），不能误归 W15；TensorRT-LLM `v1.3.0rc11` 按 4 月 9 日 official release 保留为
  18 分 pre-release boundary。PyTorch、JAX、CUDA、Triton、Dynamo、Ray、KServe、Kubeflow、Kubernetes、
  Transformers、Accelerate、DeepSpeed、Megatron、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA 的
  可访问 official release/repository 历史入口未恢复出本窗口内另一个稳定机制节点。历史分页和动态页面的
  负向覆盖能力有限，因此这是 forward checkpoint，不是对完整互联网的绝对无遗漏证明。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Seeduplex full-duplex speech LLM | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Worth Watching |
| Muse Spark | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Record Only |
| Academic agents | 3 | 2 | 3 | 4 | 3 | 3 | 18/30 | Record Only |
| ConvApparel user simulator | 3 | 2 | 3 | 4 | 2 | 3 | 17/30 | Record Only |
| TriAttention | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read — Full Review Complete |
| Memory Intelligence Agent | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Worth Watching — Full Review Complete |
| SkillX | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Worth Watching — Full Review Complete |
| Beyond Accuracy / Prefill Token Equivalents | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Must Read — Full Source Review Complete |
| Agentic Skills in the Wild | 4 | 4 | 5 | 4 | 5 | 3 | 25/30 | Must Read — Full Source Review Complete |
| MARS multi-token generation | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Must Read — Full Source Review Complete |
| FP4 Explore, BF16 Train | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Must Read — Full Source Review Complete |
| SkillClaw | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Worth Watching — Full Source Review Complete |
| DMax | 5 | 5 | 4 | 3 | 5 | 3 | 25/30 | Must Read — Full Source Review Complete |
| Externalization in LLM Agents | 4 | 4 | 4 | 3 | 5 | 3 | 23/30 | Worth Watching — Full Source Review Complete |
| KnowU-Bench | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching — Full Source Review Complete |
| Flux Attention | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Must Read — Full Source Review Complete |
| SPPO: Sequence-Level PPO | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full Source Review Complete — Refine candidate; Experimental |
| Meta Advanced AI Scaling Framework v2 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Refine candidate; Version-Grounded Governance Evidence |
| SGLang v0.5.10 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete — Refine candidate; Version-Grounded Runtime Evidence |
| Think in Strokes, Not Pixels | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental workflow evidence |
| FinTrace | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete — Refine candidate; Experimental Evaluation Evidence |
| SinkTrack | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full Source Review Complete — Refine candidate; Experimental |
| CodeComp | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Source Review Complete — Refine candidate; Experimental |
| Microsoft New Future of Work 2026 page | 2 | 3 | 3 | 5 | 3 | 3 | 19/30 | Record Only — Research Synthesis / No New System Mechanism |
| GameWorld | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Unverified / Blocked Backlog — primary PDF full read unavailable |
| Process Reward Agents | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full Source Review Complete — Experimental Inference-time Guidance |
| BERT-as-a-Judge | 4 | 5 | 5 | 5 | 5 | 2 | 26/30 | Full Source Review Complete — Bounded Reference-based Scorer |
| Many-Tier Instruction Hierarchy | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Source Review Complete — Experimental Security Evaluation |
| SCOPE (OPD) | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental Training Mechanism |
| Tracing the Roots | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Source Review Complete — Experimental Data-lineage Mechanism |
| TensorRT-LLM v1.3.0rc11 | 2 | 3 | 3 | 5 | 3 | 2 | 18/30 | Pre-release Boundary Verified — Weekly Only |

当前 31 行包括 4 个拆分后的 frozen baseline、26 个 in-window recovered `20+` candidates 与 1 个
pre-release boundary。完成状态逐项见下方 packet；25 个 accessible `20+` reviews 与低分 boundary queue
已清零，GameWorld 留在 blocked backlog。W15 forward discovery checkpoint 按 blocked-skip 规则通过，
但这不等于 W01～W30 Historical Evidence Gate 通过。

## Recovered Candidate Queue — Not Full Source Review

| First-public Date | Candidate / Primary Identifier | Discovery Signal | Likely ROADMAP Owner | Review Status |
| --- | --- | --- | --- | --- |
| 2026-04-06 | TriAttention — arXiv:2604.04921 | pre-RoPE KV importance / eviction | Ch41, handoff Ch22 | Full Source Review Complete |
| 2026-04-06 | Memory Intelligence Agent — arXiv:2604.04503 | parametric + non-parametric agent memory | Ch73；handoff Ch29/31/62/75～77 | Full Source Review Complete |
| 2026-04-06 | SkillX — arXiv:2604.04804 | hierarchical skill knowledge base | Ch73；handoff Ch74/75/80 | Full Source Review Complete |
| 2026-04-06 | Agentic Skills in the Wild — arXiv:2604.04323 | skill selection/retrieval/adaptation benchmark | Ch62；handoff Ch74/75/77/80 | Full Source Review Complete |
| 2026-04-07 | Beyond Accuracy — arXiv:2604.05404 | cache-miss/context-growth-aware trajectory cost proxy | Ch62, handoff Ch39～41 / Ch63 / Ch77 | Full Source Review Complete |
| 2026-04-08 | MARS — arXiv:2604.07023 | architecture-preserving multi-token generation | Ch44；handoff Ch40/41/52 | Full Source Review Complete |
| 2026-04-08 | FP4 Explore, BF16 Train — arXiv:2604.06916 | precision-separated rollout and update | Ch29；handoff Ch31/32/35 | Full Source Review Complete |
| 2026-04-08 | Flux Attention — arXiv:2604.07394 | context-aware layer routing for FA/SA | Ch22；handoff Ch39～41/52 | Full Source Review Complete |
| 2026-04-09 | SkillClaw — arXiv:2604.08377 | shared skill evolution across users | Ch80；handoff Ch62/68/73/77 | Full Source Review Complete |
| 2026-04-09 | DMax — arXiv:2604.08302 | self-refining parallel diffusion decoding | Ch40；handoff Ch29/44/52 | Full Source Review Complete |
| 2026-04-09 | Externalization in LLM Agents — arXiv:2604.08224 | memory/skills/protocol/harness synthesis | Ch80；handoff Ch71/73/74/77/79 | Full Source Review Complete |
| 2026-04-09 | KnowU-Bench — arXiv:2604.08455 | interactive preference/consent evaluation | Ch62；handoff Ch68/73/75/77/80 | Full Source Review Complete |
| 2026-04-10 | SPPO — arXiv:2604.08865 | prompt-level scalar Critic with sequence-broadcast advantage | Ch28；handoff Ch29 | Full Source Review Complete — Refine candidate; Experimental |
| 2026-04-06 | SGLang v0.5.10 | Elastic NIXL-EP / PD staging / piecewise CUDA Graph | Ch51；handoff Ch46/48/52 | Full Source Review Complete — Version-Grounded refine candidate |
| 2026-04-06 | Think in Strokes, Not Pixels — arXiv:2604.04746 | interleaved text/visual process supervision | Ch77；handoff Ch17/20/23/62 | Full Source Review Complete — Experimental |
| 2026-04-07 | Meta Advanced AI Scaling Framework v2 | risk threshold → mitigation-validation → deployment decision | Ch68；handoff Ch62/69/77/80 | Full Source Review Complete — Version-Grounded governance evidence |
| 2026-04-11 | FinTrace — arXiv:2604.10015 | trajectory-level financial tool-use evaluation | Ch62；handoff Ch25/30/74/77 | Full Source Review Complete — Experimental |
| 2026-04-11 | SinkTrack — arXiv:2604.10027 | BOS attention-sink context anchoring | Ch22；handoff Ch39/41/45 | Full Source Review Complete — Experimental |
| 2026-04-11 | CodeComp — arXiv:2604.10235 | program-structure-aware KV compression | Ch41；handoff Ch22/43/46/77 | Full Source Review Complete — Experimental |
| 2026-04-08 | GameWorld — arXiv:2604.07429 | state-verifiable multimodal browser-game evaluation | Ch62 provisional；handoff Ch20/74/77 | Unverified / Blocked Backlog — metadata/project/repository reviewed; primary PDF full read unavailable |
| 2026-04-10 | Process Reward Agents — arXiv:2604.09482 | retrieval-grounded online step reward + tree search | Ch52；handoff Ch28/29/62/72/77 | Full Source Review Complete — Experimental |
| 2026-04-10 | BERT-as-a-Judge — arXiv:2604.09497 | compact reference-conditioned semantic scorer | Ch62；handoff Ch23/63 | Full Source Review Complete — Bounded scorer |
| 2026-04-10 | Many-Tier Instruction Hierarchy — arXiv:2604.09443 | dynamic privilege interface and conflict benchmark | Ch68；handoff Ch62/74/77/80 | Full Source Review Complete — Experimental |
| 2026-04-12 | SCOPE — arXiv:2604.10688 | outcome-routed adaptive on-policy distillation | Ch29；handoff Ch28/30 | Full Source Review Complete — Experimental |
| 2026-04-12 | Tracing the Roots — arXiv:2604.10480 | multi-source dataset lineage graph reconstruction | Ch23；handoff Ch55/62/68 | Full Source Review Complete — Experimental |

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Current score rows / source families | 31 / 31 | 19 at `25–30`, 7 at `20–24`, 5 below 20 |
| Recovered candidate families | 26 | 按 first-public date 归 W15；RAGEN-2 回拨 W11，MolmoWeb 回拨 W13，vLLM 0.19.0 与 SkVM v1 留在 W14 |
| Current accessible `20+` Full Source Reviews | 25/25 | 原 20 项 + PRA + BERTJudge + ManyIH + SCOPE + Tracing the Roots；GameWorld 不计入 |
| Review / boundary packets | 30 complete + 1 blocked | 25 Full Source Reviews + 5 low-score verifications；GameWorld 仅完成 metadata/artifact boundary packet |
| Academic discovery window | Checkpoint Passed | HF 04-06～12 与 arXiv metadata/full-text replay；Scholar/OpenAlex/DBLP/Semantic Scholar 作 metadata/duplicate cross-check；mechanism claims 回到 primary source |
| Official / Infra discovery window | Checkpoint Passed | 可访问官方机构索引与固定 Infra release/repository 入口已审；SGLang 为完整 review，TensorRT-LLM RC 为低分 boundary；历史动态分页限制保留为 coverage limitation |
| Unverified / Blocked Backlog | 1 | 原 7 项均已定位；SkVM 因 04-03 v1 回拨 W14，PRA/BERTJudge/ManyIH/SCOPE/Tracing Roots 完成全文审计；GameWorld primary PDF full read unavailable |
| W15 Forward Candidate Evidence Gate | Passed under blocked-skip rule | 25/25 accessible Full Source Reviews、5/5 low-score boundaries、1 explicit blocked、0 current-review pending；forward cursor 可跳过已通过的 W16～W18 recorded checkpoints |
| W15 Forward Discovery Checkpoint | Passed | academic cross-index 与当前可访问 fixed official/Infra 入口均完成；动态历史分页限制留在 backlog，不冒充全历史 Evidence closure |

## Curation-Lag / Cross-Week Spillbacks

推荐流日期不等于论文事件日期。GrandCode、Self-Distilled RLVR、AgentHazard、Meta-TTL、
LightThinker++、Combee 与 MegaTrain 已按 4 月 2～5 日回写 W14；XpertBench（3 月 27 日）归回 W13。
MegaTrain 的 arXiv v1 虽在 4 月 6 日提交，但作者 4 月 5 日发布页已明确宣布正式开源，故以更早
first-public date 为 owner；current repository 的 4 月 12 日 VERL 集成只作 W15 artifact evolution。
RAGEN-2 的 arXiv v1 虽在 4 月 7 日提交，但作者官方 repository 已明确记录 3 月 12 日 release，故连同
完整 Source Review 回拨 W11；current ICML Oral 状态只作 later publication boundary。
W16 discovery feed 才浮现的 SPPO 以 arXiv v1 2026-04-10 为准回填本周，不能记成 W16 事件。
MolmoWeb 虽于 4 月 9 日提交论文、4 月 10 日发布完整代码，但 Ai2 官方博客和 collection 已于 3 月 24 日
公开模型、数据与评测工具；完整 Source Review 归 W13，W15 只保留 source-family artifact evolution。

W16 second-pass attribution 列出的 7 个 identities 已完成回溯。SkVM 为 arXiv:2604.03088，v1 04-03、
v2 04-06、v3 04-11；按 first-public 归 W14，W15 只记录 revision evolution。GameWorld 2604.07429、
PRA 2604.09482、BERTJudge 2604.09497、ManyIH 2604.09443、SCOPE 2604.10688 与 Tracing the Roots
2604.10480 均按 v1 归 W15。推荐/修订日不再替代事件日；identity blocker 清零，GameWorld 转入明确的
primary-text blocked backlog。

2026-08-13 blocked-skip ledger review 再次确认 GameWorld 只拥有 metadata、abstract、project 与 repository
边界证据；primary PDF 未完成全文读取，所以它没有计入 25/25 accessible Full Source Reviews，也没有形成
最终 Books disposition。相同 arXiv 访问限制已在本轮 W13 明确确认，不通过其他浏览器或间接入口绕过。
W15 Candidate/Discovery checkpoints 保持通过，backlog cursor 继续 W16；broader Historical Gate 仍 Open。

## Evidence Level

官方页面证明 architecture direction 与发布状态；TriAttention、MIA、SkillX、PTE、Agentic Skills、MARS、
Sol-RL、Flux Attention、SkillClaw、DMax、Externalization、KnowU-Bench 与 SPPO review 为已阅读全文及
相应 evidence/artifact 的作者材料；当前 accessible `20+` queue 已清零，GameWorld primary text 保留 blocked。
Agentic Skills 的 task success 绑定
model+harness pair、SkillsBench/Terminal-Bench Docker environment、三次运行和 automated verifier；它不能拆出
纯模型能力，也没有披露本地 serving hardware、总 token/tool/refinement cost 或统计区间。PTE 的 observed latency evidence 只覆盖
DeepSeek-V3.2、8×H200、TP=8、256 并发、100 个串行相关 steps 的纯 generation time；hardware sweep 是
theoretical-HOI sensitivity replay，不是五类设备实测。MIA 的 Qwen3-32B judge、在线 Serper 与未公开
in-house datasets 使其结果只能绑定作者 evaluation contract；厂商对 naturalness、latency 与 concurrency
的主张缺少可跨系统比较的完整条件，论文 benchmark 也只能绑定披露的模型、hardware、precision、
length、sampling、KV budget 与 batch contract。

## Cross-Week Deduplication

full-duplex 不是普通 voice model 的版本升级，而是 runtime state machine 变化；与后续
realtime audio 模型应按 interruption/overlap contract 去重。TriAttention 与 H2O/SnapKV/R-KV/
LazyEviction 为 `Direct Evolution`：从 fixed heuristic → historical attention observation → delayed
observation → pre-RoPE calibrated future-distance estimation；它与 GQA/MLA、paged KV 和 scheduler
只是 `Layering / Dependency`，不能混成同一层优化。MIA 与 ReasoningBank/传统 RAG memory 是
`Direct Evolution + Layering`：raw trajectory retrieval → success/failure workflow consolidation →
Planner-visible procedural memory → online parameter update；后一步没有消除外部 memory，反而新增 model
revision、judge feedback 与 deletion/unlearning 边界。SkillX 与 trajectory/workflow memory 是
`Direct Evolution`：raw trace → flat insight/workflow → multi-level procedural skill → plan-conditioned
step retrieval；它与 tool schema、Planning 和 Skill registry 是 `Layering / Dependency`，不是把这些
authoritative contracts 交给生成的 skill 文本。

PTE 与 raw output-token/tool-call count 属 `Direct Evolution`：flat count → 按 turn 累加 full-context
refill → 用 model/hardware `gamma` 把 context-dependent decode memory traffic 折成 prefill-token equivalent。
它与 KV retention/eviction、tool-response compaction、scheduler/queueing 和 workflow tool order 属
`Layering / Dependency`。当 prefix/KV 可部分复用、tool/network 主导 latency 或 batching 改变 roofline 时，
必须回到 trace-level measured time；PTE 不能覆盖这些旧而必要的 measurement branches。

Agentic Skills 与 curated skill benchmark 属 `Direct Evolution`：force-loaded task-specific artifact → agent
self-selection → distractor-aware selection → large-registry retrieval → no-curated-skill adaptation → task-local
refinement。它与 Ch74 tool discovery、Ch75 task exploration、Ch77 durable run 及 Ch80 registry governance 属
`Layering / Dependency`。Query-specific refinement 在 evidence coverage 充分时可组合已有 signal，但不能跨过
retrieval recall ceiling；静态 curated allowlist、人工安装或 no-skill baseline 在高风险、低复用或 registry
质量不足时仍是合理分支。

MARS 与独立 draft model / auxiliary MTP head 属 `Alternative Branch + Principle Reuse`：它不先生成可由
target exact-verify 的外部 draft，而是在同一 fine-tuned backbone 上对 `[MASK]` block 并行预测，再按
confidence 连续提交 left-to-right prefix。与 block diffusion 则是 `Direct Evolution`：保留 masked future，
但恢复 causal attention、right-shifted logits、left-to-right order，并用 clean AR loss 保住单 token 能力。
它与 KV cache、continuous batching 和 scheduler 属 `Layering / Dependency`；block cache 的同步成本不会被
“tokens per forward”自动消除。标准 AR 在不允许质量漂移、训练/serving stack 不支持 mask block，或高并发
batch synchronization 吞掉收益时仍成立；经典 speculative decoding 在必须保持 target distribution 时仍成立。

Sol-RL 与“统一低精度 rollout+update”不是简单新旧替代，而是 `Alternative Branch`：direct quantized target
尝试用同一低精度样本更新 policy，importance correction / unified precision 尝试修复 policy mismatch；Sol-RL
则把 low precision 降级为 seed-ranking proxy，选中后用 BF16 deterministic regeneration 恢复 optimization
artifact。它与 larger group/selective GRPO 为 `Direct Evolution`，与 Blackwell NVFP4、Transformer Engine、
reward service 和 policy synchronization 为 `Layering / Dependency`。当 proxy rank 不稳定、sampling 非确定、
BF16 regeneration 不可复现或 candidate pool 较小时，直接 BF16 rollout 仍是更清楚的旧方案。

Flux Attention 与固定 global/local、DuoAttention/PruLong 的静态层/头分配属 `Direct Evolution`：固定
dense/sparse topology → context-aware head-level budget → context-aware layer-level hard route。后一步不是单向
替代：head granularity 保留更细的 retrieval capacity，layer granularity 则换取 contiguous execution 和整层
KV traffic bypass。它与 NSA/DSA 的 learned sparse selector 属 `Alternative Branch + Principle Reuse`，与
Prefill sparse kernel、Decode KV layout、continuous batching 和 scheduler 属 `Layering / Dependency`。
短上下文、strict exactness、route uncertainty、prompt 中途改变任务或 mixed-route batch 无高效 kernel 时，
dense FlashAttention 或固定 hybrid topology 仍是更可预测的旧方案。

SkillClaw 与 user-local/manual Skill maintenance 属 `Direct Evolution`：单用户手工修订 → 多 session evidence
aggregation → candidate Skill → same-environment comparison → accepted revision；它与 Ch73 procedural memory、
Ch62 EvalSpec、Ch68 tenant/privacy policy 和 Ch77 durable workflow 属 `Layering / Dependency`。共享更新可以
减少重复探索，却不会自动保证单调收益：validator、task distribution、model/tool version 或数据权限变化都会
使昨日通过的 revision 在新 slice 上退化。隐私敏感、高风险、低复用或不可建立独立验证集时，user-local、
人工 curated allowlist 与静态 versioned procedure 仍是合理旧分支。

DMax 与普通 MDLM 属 `Direct Evolution`：mask→token one-way commit → self-predicted noisy-state correction →
confidence-carrying hybrid token/mask state → block convergence commit；与 AR/speculative decoding 属
`Alternative Branch`，因为它改变生成分解、训练目标和 commit semantics，而不是让 target exact-verify draft。
它与 Ch29 on-policy training、Ch41 state/cache、Ch42/52 scheduling 和 streaming 属 `Layering / Dependency`。
保守 MDLM、UDLM、AR 与 exact speculation 在低并行、无需 extra fine-tune、成熟 KV stack 或严格分布保持时
仍成立；新路线新增 revision state、oscillation、block-tail、delayed stream 与 threshold drift。

Externalization in LLM Agents 不是一条可按发布日期排序的直接替代链，而是对既有系统分层的
`Explanatory Synthesis + Principle Reuse`：稳定、通用且低延迟的能力保留在 weights；request-specific
事实与约束进入 context；跨 run 可复用 evidence 进入 memory；可组合 procedure 进入 Skill；typed action
boundary 进入 protocol；permission、lifecycle、observability 与 failure recovery 由 harness 协调。它澄清了
“模型能力”与“系统能力”的边界，却不证明越多 externalization 越好：retrieval/context contention、版本漂移、
poisoning/spoofing、权限组合和运维成本都会增长。约束稳定、延迟敏感且不需要独立治理的能力继续留在
parametric model；短期、一次性约束仍适合 request context；只有需要更新、复用、审计或撤销的状态才值得
进入长期 external control plane。

KnowU-Bench 与 static preference recovery / intent recommendation 属 `Direct Evolution`：给定完整偏好做离线
匹配 → 从 noisy history 推断偏好 → 缺失时主动询问 → 在 live environment 中选择 act / ask / silent → rejection
后停止并核验 side effect。它与 Ch73 memory retrieval、Ch75 constrained planning、Ch77 approval/workflow、
Ch68 least privilege 和 Ch80 Agent identity 属 `Layering / Dependency`。新 benchmark 没有否定 static suites：
静态 intent、deterministic GUI regression 和 offline memory retrieval 仍更便宜、更可重复，也更容易隔离单个
failure surface；interactive simulator 提高 deployment resemblance，却新增 simulator bias、feedback leakage、
role stereotyping、judge coupling 和 higher evaluation cost。

SPPO 与 token-state PPO、GRPO 构成 baseline-granularity 的 `Alternative Branches`：token-prefix Critic +
GAE 试图估计每步 return；prompt-only scalar Critic 估计当前 policy 的整题成功率并把 `R-V(prompt)` 广播给
全部 tokens；GRPO 用同 prompt 多次 rollout 的 empirical mean/std 代替 learned Critic。SPPO 用 Critic
parameter/optimizer/forward/backward、calibration、staleness 与 version coupling 换取 `N=1`；GRPO 用更多
generation/reward compute 换取免 learned baseline。uniform sequence advantage 避开 noisy temporal value，
但不等于解决因果 credit assignment：成功轨迹中的冗余/错误步骤仍被共同强化，失败轨迹中的有效步骤也被
共同惩罚。open-ended reward、step-level side effects、stochastic/partially observed environment 或需要局部
归因时，token-state Critic、process reward、group baseline 或 offline preference 仍是合理分支。

AASF v2 与 one-shot safety benchmark 属 `Direct Evolution`：capability snapshot → threat-scenario/uplift
assessment → deployment-context residual risk → mitigation validation → named decision/refresh。它与 Ch62 EvalSpec、
Ch69 release gate、Ch77 workflow/tool context 和 Ch80 platform governance 是 `Layering / Dependency`；确定性
authorization、sandbox 与 external review 没有被厂商 framework 替代。SGLang v0.5.10 内部又包含三条独立演进：
monolithic graph → piecewise capture，fixed EP + full restart → membership-aware redistribution，scatter RDMA →
contiguous staging + bulk transfer。它们共同依赖 request/KV/expert/membership epoch，却分别拥有 failure semantics。

SinkTrack 与 native long-context / RAG 不是替代关系。它从 passive sink 经 hard/soft injection 演进到 dual-track
context anchor，新增 source/cache identity 与 malicious-context amplification；CodeComp 则从 attention-only
eviction 演进到 semantic chunk + program structure + protected-span floor。二者都说明 KV policy 不再只由 token
position/attention 分数定义，却依赖不同 workload contract：前者保护 source context，后者依赖可解析 code graph。
FinTrace 与 Tool Calling component metrics 属 `Direct Evolution`：call/schema correctness → trajectory process/
information-use/output axes → domain/executable outcome；旧 component tests 仍用于低成本定位。Think in Strokes
把 single-pass visual output 扩成可监督 intermediate trajectory，和 Ch77 durable workflow 只有 `Principle Reuse`：
模型内部 visual states 尚不具备 production workflow 的 durable identity、approval、compensation 与 replay。

## Knowledge Tree Position

Ch41 KV Cache 为 TriAttention 主 owner，Ch22 Long Context 作短 handoff；MIA 主 owner 修正为
Ch73 Memory，Ch29/31/62/75～77 作训练、artifact、评测与 workflow handoff；SkillX 同样由 Ch73
拥有 procedural representation，Ch74/75/80 分别承接 tool-schema、plan 与 registry boundary；其余候选分布于
Ch29、Ch35、Ch40、Ch45、Ch48、Ch52、Ch62、Ch68、Ch71～77、Ch80。
PTE 的主 owner 为 Ch62 Evaluation；Ch39～41 只承接 Prefill/Decode/KV 机制，Ch63 承接生产 SLI，
Ch77 承接 turn/tool/response lineage。Agentic Skills 的主 owner 也是 Ch62，因为新增的是 Skill evaluation
ladder 与 model+harness/environment 证据边界；Ch74/75/77/80 只分别承接 discovery、task exploration、run state
与 registry provenance。MARS 的主 owner 修正为 Ch44：它补的是并行候选、acceptance contract 与
speculative/parallel decoding 的分支关系；Ch40 承接 AR dependency，Ch41 承接 block-cache state，Ch52
承接 confidence threshold、batch synchronization 与 SLO-aware policy。
Sol-RL 的主 owner 为 Ch29，因为新增的是 rollout search、selection 与 update evidence 如何保持身份；Ch31
承接 BF16 policy / NVFP4 explorer revisions，Ch32/35 只承接 worker synchronization、precision 与 memory cost，
不把它误归为通用 ZeRO 或 quantization 章节。
Flux Attention 的主 owner 为 Ch22，因为它改变的是长上下文模型的 dense/sparse Attention contract 与训练后
迁移路径；Ch39 承接 Prefill kernel/TTFT，Ch40～41 承接 Decode route 与 KV traffic，Ch52 承接 mixed-route
batch、fairness 和 SLO。不能把论文的 layer router 写成通用 serving request router。
SkillClaw 的主 owner 修正为 Ch80：其可迁移机制是跨用户 Skill registry 的 evidence ingestion、candidate
validation、version publish 与 sync control loop；Ch62/68/73/77 分别承接 evaluator independence、tenant/privacy、
procedural-memory provenance 与 durable run pinning。Ch80 已覆盖 Skill immutable version/digest、publisher/source
provenance、evaluation/policy/supersession/revocation、canary、in-flight pinning、rollback，以及不得直接把轨迹
写入 global memory 的边界；因此该论文暂不形成新的 Books 缺口。
DMax 的主 owner 修正为 Ch40，因为它补充的是 AR 之外的 alternative Decode state machine：可修订的 block
state、convergence 与 commit boundary；Ch29/44/52 分别承接 on-policy training、非 exact speculation 边界与
variable-progress scheduling。Ch48 只看到 2×H200 TP 执行配置，没有新的 distributed request/KV/control-plane
机制，不应作为主 owner。
Externalization review 的主 owner 为 Ch80，因为它讨论 memory、Skill、protocol 与 harness 如何组成 Agent
platform，而非提出单一 memory 或 tool algorithm；Ch71/73/74/77/79 分别承接 context budget、memory
provenance、tool authority、durable workflow 与 protocol lifecycle。已读这些目标及相邻章节：Ch71 已把 context
视为受预算约束的 runtime resource；Ch73 已区分 raw evidence 与 derived memory；Ch74/79 已区分 tool capability、
authorization 与 protocol lifecycle；Ch77/80 已把 workflow、policy、observability、versioned artifacts 和 rollback
放入 control plane。因此本文提供的是有用的统一解释框架，而不是尚未覆盖的新机制。
KnowU-Bench 的主 owner 为 Ch62，因为新增的是 personalization/proactivity 的 evaluation object、environment、
failure taxonomy 与 multi-axis metric contract，而不是一种新的 memory store 或 permission system。Ch68 承接
consent/least-privilege 与 over-action 风险，Ch73 承接 authorized behavioral evidence，Ch75/77 承接 act/ask/silent
policy 和 rejection transition，Ch80 承接 deployment autonomy。Ch62 已覆盖 feedback-conditioned trajectory、
hidden evaluator state、programmatic outcome、hybrid judge、slice 与 uncertainty；缺口是把 proactive calibration
明确拆成 initiative、restraint、post-rejection compliance，而不折成单一 success/safety score。
SPPO 的主 owner 从 Ch29 修正为 Ch28，因为它保留 learned Critic 与 PPO token-ratio/clipping，只把 Critic
输入和 advantage 粒度从每个 prefix 改成 prompt/sequence；Ch29 仅承接 learned scalar baseline 与 group
empirical baseline 的状态—采样 trade-off。已读 Ch28～30：Ch28 已覆盖 actor/critic/rollout lifecycle，Ch29
已覆盖 sequence reward uniform broadcast 与粗粒度 credit 边界；新增缺口是把 baseline granularity、Critic
calibration/current-policy identity、rollout multiplicity 与局部 attribution 明确组织成共存设计空间。

新增 fixed-source families 的主 owner 分别为：AASF v2 → Ch68，SGLang v0.5.10 → Ch51，Think in Strokes →
Ch77，FinTrace → Ch62，SinkTrack → Ch22，CodeComp → Ch41。相邻章节已分别读取并只保留 handoff：AASF
连接 Ch62/69/77/80；SGLang 连接 Ch46/48/52；visual process 连接 Ch17/20/23/62；FinTrace 连接 Ch74/77；
SinkTrack 连接 Ch39/41/45；CodeComp 连接 Ch22/43/46/47/77。Microsoft synthesis 只作 Ch62/77 background，
不拥有章节结论。

## Recommended Action

保留 Seeduplex 为未来 realtime Agent runtime 演进证据；SkillClaw 暂为 `No Change — Already Covered`
（Ch80 主 owner，Ch62/68/73/77 handoff）；DMax 暂为 `Refine — Existing Argument (Experimental)`（Ch40
主 owner，Ch29/44/52 handoff）；Externalization 为 `No Change — Already Covered`（Ch80 主 owner，
Ch71/73/74/77/79 handoff）；KnowU-Bench 暂为 `Refine — Existing Argument (Experimental)`（Ch62 主 owner，
Ch68/73/75/77/80 handoff）；SPPO 暂为 `Refine — Existing Argument (Experimental)`（Ch28 主 owner，
Ch29 handoff）；recorded review queue 已清零，继续缺失来源召回。TriAttention 与 MIA 暂定
`Refine — Existing Argument`，但 Historical Books Gate
通过前不修改 Books。MIA 只支持实验性双平面 memory/Planner update 机制，不支持通用 lifelong
learning、可逆转换或 production-safe online training 结论。SkillX 暂定 Ch73 refine，但不能把
“hierarchy”写成固定三级 taxonomy，也不能把作者 strong-to-weak benchmark 外推为任意 model/tool ecosystem。
PTE 暂定 Ch62 refine，但只沉淀“trajectory cost 必须绑定 cache policy、context growth 与 measured workload”这一
原则；不沉淀模型排名、静态 `gamma` 表或把 proxy 当 production latency/SLO。
Agentic Skills 同样暂定 Ch62 refine：长期结论是 Skill 必须在 selection/retrieval/adaptation 的真实 control path
中评估，且 refinement 受初始 evidence coverage 与额外探索成本约束；不沉淀具体模型排名或 34K pool 数字。
MARS 暂定 Ch44 Experimental refine：只沉淀“并行候选不等于 exact verification；training objective、acceptance
policy、KV commit 与 batch cadence 必须共同定义”这一分支，不沉淀 1.71× headline，也不把 one-token benchmark
上的作者结果写成严格 superset 证明。
Sol-RL 暂定 Ch29 Experimental refine：长期结论是 exploration proxy 可以使用较低 fidelity，但进入 gradient
的 artifact 必须由 objective-compatible policy/precision 重建，并保存 seed、ranker、precision、solver 与
policy-version lineage；不沉淀 4.64× convergence headline，也不把 diffusion deterministic regeneration 外推到
autoregressive LLM rollout。
Flux Attention 暂定 Ch22 Experimental refine：长期结论是 conditional attention 的 routing granularity 必须
同时匹配信息需求与硬件执行粒度，并把 route policy、KV retention 和 fallback 视为同一 artifact contract；
不沉淀 2.8×/2.0× headline，也不把单卡 kernel 结果外推为 production serving goodput。
DMax 只沉淀“parallel progress 需要可撤销 intermediate state、matched training distribution 与明确 commit/
convergence contract”这一 Experimental 分支；不沉淀 TPF/TPS、固定 threshold、block length 或把 batch-1
两卡结果称作 serving goodput。
SPPO 只沉淀“baseline granularity 是 state cost、rollout cost、variance 与 attribution fidelity 的交换”：
prompt-only Critic 必须绑定 policy version、training distribution、calibration slice 与 refresh cadence；uniform
outcome advantage 不应被表述为已解决 reasoning-step credit。不沉淀 5.9×、12.8% 或 benchmark 排名，也不把
`beta_KL=0`、single-sample 或 small-Critic 配置外推为通用 RLVR recipe。
新增六个 `20+` families 均只保留 provisional integration decision：AASF v2 沉淀 residual-risk control loop，
SGLang 沉淀 graph/failure/transfer 三种 ownership boundary，Think in Strokes 沉淀 intermediate-state workflow，
FinTrace 沉淀 component-to-trajectory evaluation ladder，SinkTrack 沉淀 context-anchor/cache identity，CodeComp
沉淀 workload-semantic KV policy。全历史 Gate 通过前不修改 Books，也不保存 vendor/paper headline 数字。

## Event-Date Daily Decision

历史回填不补造 Daily。31 个 scored candidates 与 1 个 blocked primary-text boundary 直接记录在本
Weekly，spillback 按 first-public date 回写 W11/W13/W14；SPPO 从 W16 curation feed 依 v1 日期回填 W15。

## Books Integration Decision

`Complete — W15 Source-Family Books Gate`。下列暂定清单保留 Source Review 阶段的 owner 推理，
最终 Stable Node、disposition 与实际变更以文末 2026-08-14 Final Ledger 为准。Seeduplex 暂为
`Emerging / Experimental`；TriAttention 暂为
`Refine — Existing Argument`（Ch41 主 owner、Ch22 handoff）；MIA 暂为
`Refine — Existing Argument (Experimental)`（Ch73 主 owner）；SkillX 同为 Ch73 Experimental refine、
Ch74/75/80 handoff；PTE 暂为 `Refine — Existing Argument (Experimental)`（Ch62 主 owner、Ch39～41 /
Ch63 / Ch77 handoff）；Agentic Skills 暂为 `Refine — Existing Argument (Experimental)`（Ch62 主 owner、
Ch74/75/77/80 handoff）；MARS 暂为 `Refine — Existing Argument (Experimental)`（Ch44 主 owner、
Ch40/41/52 handoff）；Sol-RL 暂为 `Refine — Existing Argument (Experimental)`（Ch29 主 owner、
Ch31/32/35 handoff）；Flux Attention 暂为 `Refine — Existing Argument (Experimental)`（Ch22 主 owner、
Ch39～41/52 handoff）；SkillClaw 为 `No Change — Already Covered`（Ch80）；DMax 暂为
`Refine — Existing Argument (Experimental)`（Ch40 主 owner，Ch29/44/52 handoff）；Externalization 为
`No Change — Already Covered`（Ch80 主 owner，Ch71/73/74/77/79 handoff）；KnowU-Bench 暂为
`Refine — Existing Argument (Experimental)`（Ch62 主 owner，Ch68/73/75/77/80 handoff）；SPPO 暂为
`Refine — Existing Argument (Experimental)`（Ch28 主 owner，Ch29 handoff）；AASF v2 暂为 Ch68
`Refine — Existing Argument (Version-Grounded Governance Evidence)`；SGLang v0.5.10 暂为 Ch51
`Refine — Existing Argument (Version-Grounded Runtime Evidence)`；Think in Strokes 暂为 Ch77、FinTrace 暂为
Ch62、SinkTrack 暂为 Ch22、CodeComp 暂为 Ch41 的 Experimental refine；25 个 accessible `20+`
candidates 均已完成 review，5 个低分项维持 Weekly-only。
新增六项分别给出 provisional disposition：GameWorld → `Unverified / Blocked Backlog`（Ch62 仅为
provisional mapping，不进入 Books），PRA → Ch52，BERTJudge → Ch62，
ManyIH → Ch68，SCOPE → Ch29，Tracing the Roots → Ch23；SkVM 完整 decision 由 W14/Ch80 拥有。
W15 的 academic 与 accessible fixed-Infra forward checkpoint 按 blocked-skip 规则通过；全历史
Evidence/Books Gate 尚未通过，因而本周仍不修改 Books。

## Ignored Noise

只用主观 demo 断言通用 full-duplex robustness。

## Full Source Review

### Attribution reconciliation — resolved

- **Identity result**：七项均已定位 primary identifier；SkVM v1 属 W14，余六项属于 W15。
- **Evidence result**：PRA、BERTJudge、ManyIH、SCOPE 与 Tracing the Roots 的 metadata、正文、
  evaluation/appendix 与相关 artifact 已审；GameWorld 的 identity/project/repository 已审，但 primary PDF
  full read unavailable，保留 `Unverified / Blocked Backlog`。后续 revision 只用于核验差异，不覆盖
  event-date v1。

### GameWorld — 27/30

- **Candidate / Source Family / Date**：`GAMEWORLD-STATE-VERIFIABLE-MULTIMODAL-AGENT-EVAL`；
  arXiv:2604.07429 sole v1，2026-04-08；project/repository 的 04-15/19 artifact 发布只作 revision boundary。
- **Primary-source Coverage / Mechanism**：已核对 arXiv metadata/abstract、official project page 与作者
  repository 的 benchmark/catalog/env/runtime、replay 和 monitoring layout；当前访问路径未能稳定取得 23 页
  PDF 正文，因此不声称已逐页阅读全文。公开 primary surface 支持 two-interface design、34 games / 170 tasks、
  Semantic Action Parsing、state-verifiable metrics、18 model-interface pairs、repeated-run robustness 与
  realtime/context-memory/action-validity analyses。Computer-use 路径让 model 直接拥有 keyboard/mouse proposal；semantic 路径由
  deterministic parser 把 typed action 映射到环境，environment state/checker 才拥有 outcome truth。
- **Problem / Evolution / Evidence Boundary**：video-game evaluation 从异构 interface + heuristic judge 演进为
  standardized action contract + environment-state verifier + replay。它能区分 perception、planning、control、
  latency、invalid action 与 memory sensitivity，却仍只证明 browser-game harness 下的 observed behavior；
  PDF 未完成逐页读取，硬件、provider latency、cost、并发与 production SLO 也不能从 repository 推断。
- **Trade-offs / Previous Scope / Decision**：semantic action 提高可比性，却抽象掉 low-level motor/GUI difficulty；
  raw computer-use 更接近 interface reality，却放大 timing、rendering 和 coordinate noise。state checker 仍可能漏掉
  hidden side effects，游戏成功也不等于现实 autonomy。已读 Ch20、Ch62、Ch74、Ch77；Ch62 主 owner。
  在 PDF 全文可访问前记为 `Unverified / Blocked Backlog — Primary metadata and artifact reviewed`；不计入
  Full Source Review，不阻塞 forward cursor，也不得进入 Books。
- **Post-forward retry（2026-08-12）**：再次读取 arXiv abstract、HTML、PDF、official project 与 author
  repository，当前 reader 仍未返回 primary paper text。既有 metadata/project/repository packet 保持有效，
  但不能补足 Method、Evaluation、Limitations 与 Appendix；W15 backlog checkpoint 完成后继续 W18。

### Process Reward Agents — 28/30

- **Candidate / Source Family / Date**：`PRA-ONLINE-RETRIEVAL-GROUNDED-SEARCH`；arXiv:2604.09482 v1
  2026-04-10，v2/ICML acceptance 2026-06-01 只作 revision boundary；已读 v1 全文、method、stage batching、
  training/evaluation、ablations、prompts 与 impact statement。
- **Problem / Previous Design / Mechanism**：post-hoc PRM 或 final-answer reward 简单、便于 batch，却只能在错误
  已传播后评分；把 retrieved documents 直接塞给 policy 又增加 context 并不保证使用正确证据。PRA 将 frozen
  policy、retriever 与共享-parameter action/reward model 分开：每个 partial trace 决定 `search|reward`，再给
  step reward；beam search 生成 `B*b` candidates、按累计 reward 保留 top-B。全局 queue 按 policy generation、
  retrieval、reward readout stage 重组 batch，runtime 而非 policy 拥有 trace/beam/evidence state。
- **Evaluation Contract / Not Proved**：v1 使用 Qwen3-4B policy、Qwen3-235B teacher、MedCPT、MedQA 训练与
  六个 OOD medical sets；SC 64 traces 对齐 PRA `B=4,b=16` 的 policy sampling budget，但额外 retriever/PRA
  calls、latency、hardware、并发、cost 与 SLO 并未 matched。结果支持作者医学环境中的 online guidance 和
  cross-policy transfer，不证明 reward 正确、clinical safety 或 production deployment；作者明确称其不是
  medical decision system。
- **Trade-offs / Evolution / Decision**：`outcome reward → post-hoc process reward → retrieval-grounded online
  step reward → search-guided decoding` 为 `Direct Evolution`。新增 reward hacking、stale KB、off-policy
  judge drift、beam starvation、stage queue fairness、deadline/cancellation 与 evidence provenance。final verifier、
  RAG 与简单 decoding 在可验证或低预算任务仍成立。已读 Ch28/29、Ch52、Ch62、Ch72、Ch77；Ch52 主 owner，
  因机制改变 inference-time scheduling object。`Refine — Existing Argument (Experimental; Books Gate Closed)`。

### BERT-as-a-Judge — 26/30

- **Candidate / Source Family / Date**：`BERTJUDGE-REFERENCE-CONDITIONED-SEMANTIC-SCORER`；
  arXiv:2604.09497 v1 2026-04-10，v2/COLM 2026 revision 2026-07-20；已读 36 页论文、protocol、training、
  compute-aware baselines、OOD/multilingual/size ablations、human-label audit、appendices，以及 model/data card。
- **Problem / Mechanism / Ownership**：regex/exact parsing 便宜可重复，却把 formatting compliance 混进能力；
  generative LLM judge 更语义化却昂贵且有 prompt variance。作者以 question-candidate-reference triplet 训练
  EuroBERT-210M binary encoder，约 1M synthetic labels、8 MI250x、20 GPU-hours；scorer artifact 拥有 input
  schema、checkpoint、threshold 与 calibration identity，不能把概率直接当 ground truth。
- **Evidence / Limitations**：36 open-weight models、15 English right/wrong tasks、3,212 human annotations 对
  synthetic labels 作局部核验；论文支持该 reference-based 分布上介于 lexical metric 与 generative judge 之间的
  cost/semantic trade-off。不支持 open-ended writing、trajectory、multimodal、事实随时间变化或无 reference
  的任务；synthetic teacher 的共享错误、threshold drift 与 adversarial paraphrase 仍存在。
- **Evolution / Decision**：`exact/regex → learned reference metric → compact semantic judge → calibrated human/
  executable hybrid` 为 `Direct Evolution`，旧 exact verifier 在 schema/math/code 中仍更强。已读 Ch23、Ch62/63；
  Ch62 已有 scorer ladder，新增证据主要 refine compact task-specific judge 的适用边界。
  `Refine — Existing Argument (Bounded Evaluation Evidence; Books Gate Closed)`。

### Many-Tier Instruction Hierarchy — 27/30

- **Candidate / Source Family / Date**：`MANYIH-DYNAMIC-PRIVILEGE-CONFLICT-EVAL`；arXiv:2604.09443 v1
  2026-04-10，v2/v3 04-13/14；已读全文、PPI、853-task benchmark、coding/IF construction、sensitivity、
  correctness-vs-style、human validation 与 prompts/examples appendix。
- **Problem / Mechanism / Ownership**：固定 `system > user > tool` 角色层级在多个 developers、skills、tools、
  memories 与 agents 共存时过粗。Ordinal/scalar Privilege Prompt Interface 把 privilege 从 message role 解耦，
  由 trusted deployer 在 inference time赋值；programmatic conflict graph 选择每组最高 privilege instruction，
  model负责遵循，外部 policy/control plane 才能拥有 provenance、authentication 与 authorization。
- **Evaluation / Evidence Boundary**：ManyIH-Bench 覆盖 up to 12 tiers、427 coding + 426 instruction-following，
  coding 用 AST/token check；100 个 LLM-generated constraint/check 中人工只判 81 faithful、11 unclear、8 incorrect。
  约 40% headline 说明当前模型在该 synthetic contract 上脆弱，不证明现实 agent permission failure rate；文本
  privilege tag 可被 spoof，论文也不提供 privilege inference 或确定性 enforcement。
- **Trade-offs / Evolution / Decision**：`fixed role hierarchy → explicit many-tier privilege metadata → authenticated
  policy decision + least-privilege executor` 是 `Layering / Dependency`，不是让模型自己成为 authority。更多 tier
  提高 expressivity，却增加 ordering、conflict graph、stale metadata 与 escalation surface。已读 Ch62、Ch68、
  Ch74/77/80；Ch68 主 owner。`Refine — Existing Argument (Experimental Security Evaluation; Books Gate Closed)`。

### SCOPE — 27/30

- **Candidate / Source Family / Date**：`SCOPE-OUTCOME-ROUTED-ADAPTIVE-OPD`；arXiv:2604.10688 v1
  2026-04-12，v2 05-30；已读 v1/v2 method、derivation、training/evaluation、ablations、temperature/cost appendix
  与作者 code boundary。
- **Problem / Mechanism / State**：uniform OPD 对 correct rollouts 可能收缩 diversity，对 flawed prefix 又可能让
  teacher 提供高熵噪声。SCOPE 先由 outcome verifier 分出 correct/incorrect：correct branch 用 student PPL
  group-normalized weight 强化低信心正确轨迹的 MLE；incorrect branch 用 inverse teacher PPL 加权 token KL，
  只偏向 teacher 能解释的 prefix。trainer 拥有 prompt group、verifier outcome、student/teacher logprob、
  temperature 与 normalization state；它仍是 sequence/prefix weighting，不等于 causal step credit。
- **Evidence / Not Proved**：六个 math benchmarks、DeepSeek-R1-Distill-Qwen-1.5B student、Skywork-OR1-7B
  teacher，并有 branch/weight ablation、temperature 与 compute analysis；作者改善只绑定该 recipe。PPL 是
  confidence proxy，不保证 teacher correction factual；无开放 reward、multi-domain、production convergence、
  failure recovery 或独立复现证据。
- **Evolution / Decision**：`uniform OPD → outcome-routed dual path → group-calibrated sample weighting` 为
  `Direct Evolution`；旧 uniform KD 在 teacher/student close、prefix clean、低复杂度任务仍合理。代价是双模型
  logprob、verifier dependency、group composition sensitivity 与 diversity/accuracy再权衡。已读 Ch28～30；Ch29
  主 owner。`Refine — Existing Argument (Experimental; Historical Books Gate Closed)`。

### Tracing the Roots — 27/30

- **Candidate / Source Family / Date**：`POSTTRAIN-DATASET-LINEAGE-GRAPH`；arXiv:2604.10480 v1
  2026-04-12；HTML 显示后续 manuscript date 但不能覆盖 v1 event。已读全文、83 seed datasets、multi-agent
  pipeline、relation taxonomy、topology/intersection/contamination analyses、root-node diversity construction、
  implementation appendix 与 author code/project boundary。
- **Problem / Mechanism / Ownership**：逐样本去重适合直接 copy，却难重建 dataset 的 vertical refinement、
  horizontal aggregation 与 contamination propagation。中央 pending queue 先校验 HF/artifact 日期，再由 sourcing、
  extracting、tracing、aggregation agents 联合读取 README/GitHub/blog/paper，输出带 derivation-relation edge 的
  lineage graph；graph store 拥有 dataset/version/node/edge/evidence identity，agents 只是 proposal producers。
- **Evidence / Limitations**：作者在 math/code/general/science 生态上展示结构冗余、exact contamination path 与
  lineage-aware root sampling；这支持 lineage graph 能发现 sample matcher 不易表达的 evolution，不证明 agent
  抽取的每条 edge 为真。documentation 缺失、rename/fork、synthetic derivation、LLM common-mode error、83-seed
  selection 与 later artifact drift 限制 completeness；下游 diversity metric 也不等于 model quality。
- **Evolution / Decision**：`sample-level dedup → dataset artifact identity → typed lineage graph → contamination/
  diversity propagation policy` 为 `Direct Evolution`。逐样本 exact/semantic match 仍用于验证 graph claim；图方法
  新增 stale edge、false ancestry、license/consent propagation 与 delete/supersession。已读 Ch23、Ch55、Ch62、
  Ch68；Ch23 主 owner。`Refine — Existing Argument (Experimental; Historical Books Gate Closed)`。

### How Well Do Agentic Skills Work in the Wild — 25/30

- **Candidate / Week / Score**：Agentic Skills in the Wild；2026-W15；25/30，维持 discovery score。论文把
  Skill utility 从理想化 prompt augmentation 提升为 end-to-end selection/retrieval/adaptation evaluation，且
  公开代码与数据；但 model 与 native harness 无法解耦、服务硬件和完整成本缺失，Longevity 保持 3。
- **Source Family ID / Type / Date**：`AGENTIC-SKILL-REALISTIC-EVALUATION`；arXiv evaluation paper + author
  code/data artifact。arXiv 只有 v1，2026-04-06 00:10 UTC 首发，归 W15；current GitHub 仅一个可见 commit、
  无 release/tag，Hugging Face dataset 也无 dataset card，均不能证明 immutable event-date artifact snapshot。
- **Direct / Related Primary Sources**：直接来源为 arXiv v1 全文、author repository、公开 34K skills/search
  index/precomputed trajectories dataset 和 release boundary。SkillsBench、Terminal-Bench 2.0、Harbor、各 native
  harness 与 Anthropic skill-creator 是 evaluation dependencies；它们不是本文结果的独立复现。
- **Access / Full-read Coverage**：已读 metadata、Abstract、Introduction、Related Work、skill collection、
  search/index/RRF 方法、六级 progressive settings、三 model+harness 实验、query-specific/query-agnostic
  refinement、Conclusion、Ethics/LLM disclosure，以及 Appendix A～D 的 index 参数、agentic-search protocol、
  benchmark exclusions、model/harness versions、timeout、Docker/verifier、完整 refinement prompts 与 GPT-5.4
  coverage judge；并核对 current repository 的 data/config/task/search/refinement/result scripts、HF dataset、
  单 commit 与无 release 状态。
- **Original Problem / Previous Design**：把少量人工编写、与 task 强对齐的 Skill 直接放入 Context，能隔离
  retrieval noise、提供清晰上界，也适合受控回归和固定高风险 workflow。但这种设置把“Skill 内容有用”与
  “Agent 能找到、选择并适配它”混为一体；真实 registry 规模增长后，metadata、distractor、权限与部分相关
  内容都会进入 control path。
- **Changed Constraint / Principle**：Skill 从 benchmark fixture 变为独立 registry artifact 后，utility 是一条
  乘法链而不是 Skill 文件的静态属性：候选 recall 决定 ceiling，selection 决定是否 load，content coverage
  决定是否包含所需知识，Agent/harness 决定是否正确使用，environment verifier 最后判断 outcome。任一环节
  失败都能让“高质量 Skill”对当前 run 无效。
- **Mechanism**：作者从 permissive-license GitHub repositories 收集、清洗并按文件内容去重 34,198 个 Skill；
  metadata 与完整 SKILL.md 分别建立 Qwen3-Embedding-4B dense index 和 SQLite FTS5/BM25 sparse index，hybrid
  以 RRF 合并。Agentic search 允许模型迭代改写 query、查看 candidate 与读取 detail，再选择 top-5。Evaluation
  依次比较 force-loaded curated、curated self-select、curated+distractors、34K retrieval 含 curated、移除
  curated 后 retrieval、no-skill 六种条件，把 selection、retrieval 与 adaptation failure 分离。
- **Refinement Mechanism**：query-agnostic 路径对每个 retrieved Skill 独立生成 synthetic tests、比较 with/without
  Skill 并离线重写，运行时便宜但不知道目标 task、不能跨 Skill composition。Query-specific 路径在 task Docker
  内读取全部 retrieved Skills、先探索任务、在看不到 ground-truth verifier 的条件下 self-evaluate，再把多份
  部分相关内容合成 task-local Skill；它能组合 evidence，却为每个任务增加一次完整探索和错误自判风险。
- **State Ownership / Control and Data Flow**：registry/index 拥有 source Skill identity、license/filter 与 search
  representation；retrieval agent 只提出 query、shortlist 与 load decision；refiner 产生 derived task-local artifact，
  不能覆盖原 Skill；Harbor task environment、timeout 和 automated verifier 拥有 outcome；model/harness pair
  拥有执行 policy。生产平台还必须补 version/provenance、authorization、sandbox、cache、supersession、revoke
  与 delete，不能让生成后的 Skill 获得新的 tool authority。
- **Implementation Details**：sparse index 对 name/description/content 使用 10/5/5 field weights；dense query 加固定
  instruction；RRF 默认 sparse/dense 各 0.5、`k=60`，content semantic weight 经 synthetic query sweep 取 0.05。
  `/keyword`、`/semantic`、`/hybrid`、`/detail` 暴露检索；scripts 分别 prepare/collect retrieval、top-k copy、
  task-specific/agnostic refinement、Harbor run、result aggregation 和 skill-usage/coverage analysis。current repo
  依赖 live model APIs、SGLang/local model、Docker、HF data 与 Harbor main branch，复现必须固定这些外部身份。
- **Evaluation Contract**：SkillsBench 使用排除 3 个已知 environment/verifier 问题后的 84 tasks；Terminal-Bench
  2.0 使用全部 89 tasks。Claude Opus 4.6+Claude Code 2.1.19、Kimi K2.5+Terminus-2、Qwen3.5-397B-A17B-FP8+
  Qwen-Code 0.12.3 各自端到端执行 retrieval/refinement/task，因此结果是 pair-level system evidence。每 task/
  condition 运行 3 次并由 benchmark verifier 判定；SkillsBench timeout 统一 1.5x，Terminal-Bench 对本地 Kimi/
  Qwen 为 2x、Claude 为 1x。论文未披露本地 GPU 数量/型号、SGLang revision、sampling、token/tool budget、
  wall-time/cost、seed、置信区间或失败相关性。
- **Results / Ablations / Sensitivity**：在 curated skills 可检索时，agentic hybrid content search 的 Recall@5 为
  65.5%，说明 best retrieval 仍遗漏约三分之一 ground-truth skills。Progressive settings 中 Claude 从 force-load
  55.4% 逐步降到 no-curated retrieval 38.4%，后者只比 no-skill 35.4% 高 3 点；Kimi/Qwen 的 no-curated 条件
  低于各自 no-skill baseline。Query-specific refinement 在 9 个组合中改善 7 个，但 Kimi/SkillsBench with-curated
  从 33.5% 降至 26.7%，Claude no-curated 也从 38.4% 降至 37.9%。Terminal-Bench 三个 pairs 均上升；这些是
  3-run means，不等于跨版本/流量稳定收益。GPT-5.4 coverage judge 显示 refinement 成功组初始 coverage 较高，
  但该分析没有独立 human calibration，相关关系不能证明 threshold 或因果。
- **What the Evidence Proves / Does Not Prove**：证据支持：在作者这两套 coding/terminal environments 中，
  Skill 收益会随 autonomous selection、large-pool retrieval 与缺失 task-specific content 而明显衰减；query-specific
  synthesis 只在 retrieved evidence 具有足够 coverage 时较常恢复收益。它不证明 agentic search 普遍优于固定
  retriever，不证明 refinement 会生成缺失知识，不证明增加 load rate 导致 success，也不证明任何一个 model
  本身优于另一 model，因为 harness、serving、timeout 与 tool surface 同时变化。
- **Limitations / Threats to Validity**：ground-truth retrieval label 来自为 SkillsBench task 人工配套的 curated
  Skills，本身带 idealized bias；34K pool 只覆盖两个聚合站、permissive-license GitHub 内容并按 exact content
  dedup，可能仍有语义重复、质量/安全/版本偏差。SkillsBench 与 Terminal-Bench 偏 coding/CLI，不能外推业务、
  多模态或高风险 action。三次重复、不同 timeout、无 uncertainty/cost/hardware disclosure 和 pair-level confound
  限制比较；coverage judge、self-evaluation、live APIs/dependencies 与 current one-commit artifact 限制复现。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：agentic retrieval 增加 recall 与解释机会，也
  增加 model calls、latency、Context、search nondeterminism 和 prompt-injection/supply-chain exposure。Task-specific
  refinement 获得 composition，却把 exploration cost、environment access、self-confirmation、derived-artifact
  provenance 与 stale/revoke 问题带入每次 run。Curated allowlist/force-load 在稳定、高风险任务仍合理；simple
  semantic/BM25 在 latency/cost 受限且 metadata 质量高时仍合理；registry signal 不足时 no-skill/fail-closed 可能
  比加载误导内容更安全。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：`Direct Evolution`：task-specific force-load →
  autonomous selection → distractor-aware selection → registry retrieval → general-skill adaptation → task-local
  synthesis；`Layering / Dependency`：Ch74 tool/catalog discovery、Ch75 task exploration、Ch77 durable execution、
  Ch80 registry/governance。已读 Ch62、Ch73～75、Ch77、Ch80；主 owner 为 Ch62，因为论文真正补全的是
  evaluation condition ladder 与 pair-level evidence boundary，不是新的 universal Skill runtime。
- **Existing Coverage / Integration Decision**：Ch62 已要求 subject identity 包含 prompt/tool/workflow/environment，
  并以 Agent outcome 和 trace 为对象；Ch74 已有 tenant-aware catalog retrieval，Ch80 已有 Skill identity/provenance。
  缺口是评估必须逐层移除 curated oracle，分别测 selection、retrieval、adaptation 和 derived refinement，并同时
  保存 no-skill/fail-closed baseline。暂定 `Refine — Existing Argument (Experimental; Provisional; Historical
  Books Gate Closed)`；Gate 通过后只 refine Ch62，其他章节短 handoff，不保留具体模型排名和固定 index 参数。
- **Open Questions**：怎样在同一 model/harness/tool/timeout/cost contract 下隔离 selection、retrieval、adaptation
  的因果贡献？如何把 candidate recall ceiling、load precision、task success、security deny、latency 与 total
  exploration cost组成 EvalSpec？Derived task-local Skill 的 source lineage、TTL、authorization、revoke/delete 与
  cross-run reuse由谁拥有？什么信号应触发 no-skill/fail-closed，而不是强行 refinement？

### Beyond Accuracy: Prefill Token Equivalents for Tool-Integrated Reasoning — 26/30

- **Candidate / Week / Score**：Beyond Accuracy / PTE；2026-W15；26/30，维持 discovery score。它提供
  可操作的 system metric 与公开 artifact，但 `gamma` 是理论 proxy、硬件 sweep 非实测、端到端 tool/network
  latency 被排除，因此 Longevity 保持 3，不能升级为通用 latency model。
- **Source Family ID / Type / Date**：`PTE-TOOL-TRAJECTORY-COST`；arXiv evaluation/performance paper +
  author framework。v1 2026-04-07 属 W15，v2 2026-04-14 属 later revision boundary；2026 年 7 月 ACL
  final publication 只证明后续 peer-reviewed status，不倒写为 W15 事件。current repository 只有一个可见
  commit、无 release/tag，不能证明 event-date code snapshot。
- **Direct / Related Primary Sources**：直接来源为 arXiv v1 全文、v2 metadata、ACL Anthology final record、
  author repository 与 result-analysis/runtime documentation。论文引用 Continuum/KVFlow、DistServe 与 Roofline
  作为 cache、Prefill/Decode 和 hardware-modeling 背景；它们解释依赖，不是 PTE 结果的独立复现。
- **Access / Full-read Coverage**：已读 v1 metadata、Abstract、Introduction、Related Work、完整公式/假设、
  latency/hardware validation、五 benchmark 实验、四类 inefficiency analysis、correctness correlation、
  Conclusion、Limitations、Ethics，以及 Appendix A～G 的 architecture/HOI/sensitivity、benchmark、implementation、
  prompt/judge、完整结果、case、pattern heuristic、difficulty control 与 pricing comparison；并核对 current code
  的 tools、rollout trace、reward、timing/PTE scripts、JSONL schema 和无 release 边界。
- **Original Problem / Previous Design**：output-token count、uncached-token count、tool-call count 与 API price
  都容易采集，也适合 quota/billing；在短单轮请求或 cache policy 稳定时它们仍有价值。多轮 TIR 中，同样一枚
  token 的成本却取决于它是 parallel Prefill 还是 serial Decode、前序 tool response 扩大了多少 context，以及
  tool pause 后 KV 是否仍可复用。flat count 因而丢失 trajectory 的 state/recompute placement。
- **Changed Constraint / Principle**：Agent workflow 让 LLM 请求被 tool execution 切成多 turns；如果 cache 在
  pause 期间超时、被压力驱逐或系统本身无状态，每轮会重放累计 context。之后 Decode 还需读取随 context 增长
  的 KV。于是成本单位必须从“生成多少 token”扩为“在哪个 context state、以何种 cache policy 处理 token”。
- **Mechanism**：对 k-turn trajectory，作者定义
  `PTE=sum_i(D_prefill_i + gamma * L_seq_i * D_decode_i)`。`D_prefill_i` 是该轮累计 context 的 Prefill
  tokens，`D_decode_i` 是输出 tokens，`L_seq_i` 是 Decode 开始前累计长度。FP16 KV 每历史 token 的逻辑
  bytes 近似 `4*n_layers*d_model`，再按 GQA 的 `H_kv/H_q` 或 MLA 的 latent+RoPE dimensions 修正；
  `gamma=(2*n_layers*d_model*HOI)/N_active`，HOI 用 peak FLOPS/peak memory bandwidth，把 memory traffic
  折成一个 Prefill-token equivalent。
- **State Ownership / Control and Data Flow**：evaluation harness 按 turn 保存 prompt/tool response、prefill/decode
  token counts、sequence length、model/config、tool schema、timing 与 correctness；PTE calculator 消费 trace 和
  `gamma` 产生 derived metric。真实 KV retention、eviction、prefix identity、queueing 和 batch composition 仍由
  serving runtime/scheduler 拥有，不能由 evaluator 假定后反向改写。Workflow 拥有 tool order、response
  compaction 与 stop/retry；Monitoring 拥有生产 measured SLI；Evaluation 负责声明哪个 proxy 足以支持哪个结论。
- **Implementation Details**：统一框架以 vLLM 驱动多轮模型调用，Search/Visit 分别使用 Serper/Jina，Python
  使用 SandboxFusion；YAML 配置 tool schema，rollout decorator、reward/evaluator、result analysis 分层，结果
  JSONL 同时保存 messages、turn record、evaluation config 与 inference/tool/wall-time timeline。current README
  支持最多 256 concurrency 的 no-summary stress path，也暴露 external API/model secrets、service version 与
  webpage drift 都属于 reproduction contract。
- **Evaluation Contract**：能力实验覆盖 13 个公开 dense/MoE model configurations；MATH500、AIME24/25 使用
  Python，SimpleQA 与 WebInstruct-Verified 各随机 500 条，分别使用 Search+Visit 和 Search+Visit+Python；
  同一 system prompt/tool definitions，WebInstruct 的 correctness 用 DeepSeek-V3 judge。主 benchmark 没有披露
  完整 serving hardware、precision/quantization、vLLM/model revisions、sampling、batch/concurrency、subset seed、
  API snapshots、tool latency 或 SLO，故模型排行不可跨环境比较。
- **Latency Validation / Sensitivity**：单独在 DeepSeek-V3.2、单节点 8×H200、vLLM TP=8、256 parallel requests、
  Wikidata-derived synthetic tool QA 上取 N=100 per-step samples；只记录 model generation latency，明确排除
  tool execution 和 network。作者报告 PTE 与 step time `r=0.9253`，output tokens `r=-0.3750`，并提醒同一
  trajectory steps 串行相关，p-value 仅 descriptive。Appendix pricing 表的 naïve uncached-token count 是
  `r=0.625`，与前述 output-token 指标不同，不能混成一个 baseline。H100/H200/A100/V100/4090 的 >0.95
  Spearman 是把同一 WebInstruct traces 用 datasheet peak HOI 重新计价，并非在五类 GPU 上 rerun。
- **Ablations / Failure-pattern Analysis**：论文没有对 full-cache reuse、partial prefix hit、TTL、batching、
  quantization、kernel、speculation 或 scheduler policy 做 factorial ablation。四类 pattern 由 heuristic 识别：
  answer 后再调用 tool 的 confirmatory use、同轨迹多 tool types、空/错误执行作为 weak prior、JSON/schema error
  作为 format collapse；这些 detector 可复算但会混入合理 verification/multi-tool plan、tool outage 与 parser bug。
  difficulty-stratified results仍显示 failure 常伴随更高 PTE，但控制 difficulty 后 partial correlation 只有
  `r=-0.040`；统计显著不等于强效应，更不等于高 PTE 导致错误。
- **What the Evidence Proves / Does Not Prove**：在作者声明的 cache-miss cost model 和 H200 stress setting 下，
  turn-aware PTE 比单步 output-token count 更贴近纯 generation latency；trajectory analysis也支持 late detour、
  long tool output 与 schema failure 会累积后续推理成本。它不证明 tool call 必然清空 KV，不证明 PTE 是
  end-to-end wall time/cost/energy，不证明静态 peak-HOI `gamma` 能描述实际 kernel utilization，也不证明某 model
  在生产中更高效或“多用工具导致更差答案”。
- **Limitations / Threats to Validity**：公式默认每轮 `D_prefill_i` 为累计 context，无法表达 retained/partial/
  shared prefix、paged cache、KV offload 或 resumable session；Decode 还需读 weights，Prefill/Decode bottleneck 会
  随 batch、length、MoE routing、quantization、kernel 和 hardware utilization 变化，未必等于理论 roofline。
  queueing、admission、tool/network、summary/compaction、failure/retry 和 side effects 均在 proxy 外。单模型、
  单硬件实测与相关 steps 限制外部效度；LLM judge、live APIs、随机子集和无 immutable artifact 限制复现。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：PTE 获得可离线计算、能体现 context debt 的
  trajectory proxy；代价是 model/hardware/config calibration、trace cardinality、cache-policy assumption 和误把
  estimated cost 当 observed latency。它可能惩罚必要 verification 或合理 tool composition，也可能因实际 cache
  hit 高估成本。raw tokens/tool calls 仍适合 billing、quota 和简单回归；actual TTFT/TPOT/wall time/goodput 仍是
  production SLI；trace-level profiler 在要诊断 scheduler、kernel 或 tool tail 时不可替代。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：`Direct Evolution`：flat tokens/tool count →
  per-turn uncached token count → cache/context-aware analytical trajectory cost → trace-measured latency/SLO；
  PTE 与 Prefill/Decode/KV mechanics、tool-output compaction、workflow state 和 Monitoring 是 `Layering /
  Dependency`。已读 Ch39～41、Ch62～63 与 Ch77；主 owner 为 Ch62，因为新增的是 EvalSpec/derived metric
  evidence boundary，Ch39～41 只解释物理项，Ch63 保留 observed SLI，Ch77 保留 turn/tool lineage。
- **Existing Coverage / Integration Decision**：Ch62 已要求 runtime evaluation 绑定硬件/workload并把 cost/SLO
  与质量并列，Ch63 已要求 TTFT/TPOT/goodput 和 workload contract；缺口是 Agent trajectory 的后续 state debt
  不能由 flat token/tool count表达，以及 analytical proxy 与 observed SLI 的严格边界。暂定
  `Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`；Gate 通过后可 refine
  Ch62，不在 Ch39～41 重复公式，不保留 model ranking、静态 gamma 表或相关性 headline。
- **Open Questions**：怎样用 cache-hit/TTL/prefix identity、batch composition、quantization/kernel revision 和
  actual per-turn timings校准 PTE？tool/network 与 LLM time 应合成一个 metric 还是保留 cost vector？怎样区分
  necessary verification/tool composition 与冗余 detour？在 production traffic 上，proxy residual 是否按 tenant、
  length、model、tool 和 scheduler slice 稳定，何时必须废弃/recalibrate？

### SkillX: Automatically Constructing Skill Knowledge Bases for Agents — 24/30

- **Candidate / Week / Score**：SkillX；2026-W15；24/30。原分 25；论文明确是 work in progress，
  hardware/total cost 与统计不确定性未披露，current artifact 也不能等同 event-time code，故 Source
  Reliability 4→3。
- **Source Family ID / Type / Date**：`SKILLX-HIERARCHICAL-PROCEDURAL-KB`；arXiv paper + author
  repository/skill library；v1 2026-04-06，v2 2026-04-19。W15 事件以 v1 为准，v2 只用于 later-revision
  核验；两版 arXiv file size 相同且无 changelog，不能据此断言内容完全相同。
- **Access / Full-read Coverage**：已读 v1 全文及全部 appendix/prompt，核对 v2 method/evaluation/
  limitations 边界；覆盖 problem formulation、三级 skill schema、rollout/extraction、merge/filter/update、
  exploratory expansion、pseudo-plan retrieval、三 benchmark setup/results、cross-model transfer、component
  analysis、ablation、case studies、baseline reproduction、FAISS/HNSW/MMR 参数与 prompts；已核对 current
  GitHub pipeline、AppWorld SkillKB、checkpoint surface 与无 formal release 的 artifact 状态。
- **Original Problem / Previous Design**：raw trajectory replay 保真且实现简单，flat reflection/workflow
  压缩成本低；在任务相似、tool schema 稳定、历史不大时合理。但单体 experience 难同时满足 compact、
  executable、composable 与跨模型 transfer，弱 agent 自己抽取经验又受自身 capability ceiling 限制。
- **Changed Constraint / Principle**：长程 tool task 同时包含 task decomposition、multi-tool subroutine 与
  single-tool constraints，不同粒度应该分别形成 procedural state；检索也应从“query 像哪个旧任务”演进为
  “当前计划的每个 step 需要什么 skill”，同时避免把 hallucinated pseudo-plan 本身作为执行指令。
- **Mechanism**：GLM-4.6 对每个训练任务 rollout 四次，从成功 trajectory 抽取 planning（有序高层步骤）、
  functional（name/document/content 的多工具 subroutine）与 atomic（单工具 usage/constraint/failure）skills。
  每轮将新技能按 embedding 聚类/merge，以 general filter 和 tool-schema filter 拒绝不便移植或无效调用，
  再 add/modify/keep；experience-guided exploration 按可靠/失败/未使用 tools 生成探索与 synthetic tasks。
  inference 先检索 planning skills 并生成不注入最终 prompt 的 pseudo-plan，再逐 step 检索 functional/atomic
  skills、dedup、LLM self-filter 后一次性注入 system prompt。
- **State Ownership / Control and Data Flow**：trajectory 与 reward 是 source evidence；SkillKB 保存由 extractor
  派生的 advisory procedures；tool catalog/schema 仍应由 executor/platform 拥有；pseudo-plan 只是 retrieval
  state，final plan 与 workflow transition 仍由 Ch75/77 runtime 验证。论文 `D^(k+1)=D^(k) union phi(S^(k))`
  只表达逻辑累计，不定义 tenant ACL、immutable version、source lineage、conflict/supersession、revocation、
  rollback 或 delete propagation。
- **Implementation / Evaluation Contract**：BFCL-v3 base multi-turn 随机 50 train/150 test；AppWorld 90
  train、Test Normal；tau2-Bench 使用其 domain splits。Qwen3-32B、Kimi-K2-Instruct-0905、GLM-4.6 为主
  executors；GLM-4.6 strong extractor，temperature 0.9，四 trajectories/task；最多三轮 refinement，expansion
  每 training task 一次、temperature 1.0；Qwen3-Embedding-8B。retrieval 用 FAISS HNSW，top-100、cosine
  >=0.45 且距 best <=0.08、>0.95 dedup、MMR lambda 0.75、最终最多 8 skills。hardware、并发、wall time、
  extraction/API cost、p95/p99、置信区间和显著性 `Not Disclosed`。
- **Baselines / Evaluation**：No Memory、A-Mem、AWM、ExpeL 均按 initial query retrieval + system-prompt
  injection 统一表面协议，并分别比较 self-extract 与 GLM-extract；BFCL/AppWorld 报四次独立 run 的 Avg@4/
  Pass@4，tau2 各 task 四次后报 Pass@1。baseline 的 original storage/retrieval/runtime semantics 被适配，
  因而结果证明的是作者 reproduction contract，不是所有原实现的普遍排序。
- **What Evidence Proves**：在上述任务与 prompts 内，三级表示及两阶段 retrieval 通常比所测 flat baselines
  带来更高 task completion；strong extractor 的 experience 可以迁移给较弱 executors。Qwen3-32B 例如从
  BFCL Avg@4 53.67→63.67、AppWorld 27.68→35.12，但这些数字必须绑定四-run、split、model 与 retrieval
  contract。代码证明 extraction/filter/merge/checkpoint surfaces 已公开，而非 production registry 完成。
- **What It Does Not Prove**：不证明固定三层是唯一或跨 domain 最优 taxonomy，不证明 strong-to-weak
  transfer 总是有效，不证明减少 steps 等于降低总成本，也不证明 generated skill 可获得 tool/workflow authority。
  GPT-4.1 self-extract 的 BFCL Pass@4 从 58.39 降到 56.67；closed/proprietary model snapshots 与 server
  settings 不完整，不能归因于 architecture alone。
- **Ablation / Sensitivity / Failure Modes**：Qwen3-32B 加 Functional/Atomic 可能因 over-imitating retrieved
  skills 而退化；更强模型的 pseudo-plan 也可能误表环境 dynamics。AppWorld Vanilla Iter3 低于 Iter2，作者
  明确承认 limited-data text optimization 会 overfit；tau2 未做 iteration/expansion ablation。固定 similarity/
  MMR thresholds、top-8 budget、random split、merge correctness、filter false reject、schema drift 与 skill
  poisoning 没有系统 sensitivity。压掉 exploration/backtracking 可提升 concise reuse，也可能删除 rare failure
  evidence；summary 覆盖原 tool response 会损失 exact provenance。
- **Where Previous Design Still Applies**：小历史、exact replay/debug、tool schema 高频变化或不能容忍派生
  procedure 误导时保留 raw trajectories；单一稳定 workflow 用显式版本化 procedure 更可预测；需要按需加载
  大型 code/resource skill 时 progressive disclosure 仍比一次性 prompt injection 合理。模型能力与任务不同，
  只启用 planning 或 functional+atomic 都可能优于全层组合。
- **Evolution Relationship**：`Direct Evolution`：raw trajectory → flat insight/workflow → hierarchical
  planning/functional/atomic skills → pseudo-plan-conditioned step retrieval → iterative refinement/expansion；
  `Layering / Dependency`：tool schema validation、Planning、Workflow 与 registry governance 不由 SkillKB 替代。
- **ROADMAP / Chapters Read / Existing Coverage**：主 owner Ch73；handoff Ch74、Ch75、Ch80；已读 Ch73～75、
  Ch77、Ch80。Ch73 已覆盖 raw→derived procedural memory 与 advisory-state boundary，Ch74 已拥有 tool schema
  authority，Ch75 已拥有 plan version，Ch80 已拥有 skill identity/provenance/revocation。新增可沉淀点是
  multi-granularity procedural representation、query→pseudo-plan→step retrieval，以及 per-model skill composition。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后在 Ch73 精化 representation/retrieval evolution，在 Ch74/75/80 只作短 handoff；不固化论文三级
  命名，不复制 benchmark table。
- **Open Questions**：SkillKB 怎样绑定 source trajectory、extractor/tool-schema version 与 tenant？merge 后怎样
  selective delete 或 rollback？如何独立验证 pseudo-plan/self-filter，而不是让同一 model 同时提出和批准？
  固定 total tokens/tool calls/wall time 后，强 extractor 的一次性成本多久才能被复用收益摊销？

### Memory Intelligence Agent — 24/30

- **Candidate / Week / Score**：Memory Intelligence Agent（MIA）；2026-W15；24/30。原分 25，
  因 evaluation/artifact 可用但独立性、复现条件和 production contract 不足，Source Reliability 4→3。
- **Source Family ID / Type / Date**：`MIA-DUAL-MEMORY-TTL`；arXiv paper + author repository +
  model/dataset artifacts；v1 2026-04-06，v2 04-07，v3 04-09，均属于 W15；v4 04-19 仅用于
  revision 核验，不回写为 W15 新事件。
- **Access / Full-read Coverage**：已读 v1～v3 与当前 v4 metadata；全文 Abstract、Introduction、
  Related Work、Manager-Planner-Executor 方法、全部训练/TTL 公式与算法、Implementation、11 个
  benchmark 的 setup/results、closed-source executor、tool-call analysis、cumulative ablation、
  unsupervised self-evolution、Conclusion，以及 training/test/baseline/retrieval/dataset/algorithm/prompt
  appendices；已核对 GitHub、Hugging Face model tree 与 21,287-row dataset artifact。仓库 04-14
  以后 streaming TTRL 等变化只作 artifact drift，不当作 W15 证据。
- **Original Problem / Previous Design**：直接保存并检索相似 trajectories 简单、无需改模型参数，
  在任务分布稳定和 memory 规模可控时合理；但历史增长会抬高 storage/retrieval/context cost，纯
  similarity 也会忽略 trajectory 成功率、rare strategy 和失败约束。
- **Changed Constraint / Principle**：deep-research Agent 需要跨任务复用 procedure，而不是无限回放
  原始 trace。可把 exact evidence 留在外部 memory，把较稳定的 search policy 放入 Planner；但两种
  状态的 provenance、更新频率和删除语义不能混为一体。
- **Mechanism**：Memory Manager 用 frozen Qwen3-32B 将图像转 caption、trajectory 压成 structured
  workflow，以 semantic similarity、value reward 和鼓励 long-tail 的 frequency reward 检索成功与失败
  经验；Planner（训练目标 Qwen3-8B）读取 memory 生成 plan，Executor（Qwen2.5-VL-7B）按 ReAct
  搜索，可触发一次 reflect/replan。两阶段 alternating GRPO 先冻结 Planner 训练 Executor，再冻结
  Executor 训练 Planner。TTL 对每个 test batch 生成 G 个 plans/trajectories，以 grouped advantage
  更新 Planner，同时保存最短成功、随机失败和 contrastive plan pair，并选择性清理 memory units。
- **State Ownership / Control and Data Flow**：外部 workflow/meta-plan units 由 Manager 拥有；Planner
  weights 是另一份可变 parametric state；Executor 与 tools 产生原始 trace；Qwen3-32B judge 决定 success
  signal。论文展示的是 external memory→Planner update，以及新 Planner 输出再生成 external experience，
  不是可逆的逐条 state conversion。memory unit 清理后，单条来源无法从 weights 定位或删除。
- **Implementation / Evaluation Contract**：veRL；Executor Qwen2.5-VL-7B、Planner Qwen3-8B、
  Judge/Manager Qwen3-32B。training 使用 wiki25/E5-base-v2/FAISS top-3 与 Serper image cache；evaluation
  对部分任务切到在线 Serper text/image top-5。TTL 一 epoch、learning rate `1e-6`、每样本 4 rollouts。
  FVQA train/test 4,856/1,800，另含 InfoSeek、LiveVQA、SimpleVQA、MMSearch、2 个未公开 in-house
  sets，以及 2Wiki、HotpotQA、SimpleQA、GAIA-text。hardware、总 compute、batch/concurrency、延迟、
  SLO、重复 seeds、confidence interval 与显著性检验均 `Not Disclosed`。
- **Baselines / Ablations / Sensitivity**：比较 no-memory、RAG、Mem0/A-Mem、ReasoningBank、ExpeL、
  Memento 与多种 open/closed models；不同 memory method 使用不同 prompt/trained executor variants，
  因而不是纯 memory-layer substitution。ablation 是 Base→Only Memory→Only Plan→Memory for Planner→
  Reflect→Trained Planner→TTL 的累计加法，不能分离交互项，也没有 retrieval score component、memory
  replacement、clear policy 或 update cadence 的 sensitivity。
- **What Evidence Proves**：在作者 11-benchmark contract 下，MIA 比所测 open baselines 得到更高的
  judge accuracy；结果支持“把压缩成功/失败 workflow 放在 Planner 前，比简单把 memory 塞给 Executor
  更可能有效”，并证明 Planner/Executor alternating training 与 batch-level TTL 可实现。论文报告 MIA
  multimodal 七列为 69.6/65.5/64.9/43.1/62.6/31.8/37.7，必须绑定上述模型、tools 和 judge。
- **What It Does Not Prove**：不证明 memory 一般优于 no-memory，不证明更多 tool calls 因果带来正确性，
  不证明同一 test set 多 epoch 提升是 open-world continual generalization，也不证明 “online update 不中断
  reasoning”。closed-source executor 实验移除了 TTL，只验证 wrapper 组合；vendor snapshot 与总成本不完整。
- **Limitations / Threats / Failure Modes**：同一 model family 充当 Manager、三 reviewer 和 Area Chair，
  可能产生 correlated blind spot；其信号同时控制 memory selection 与 weight update，错误会形成反馈回路。
  shortest-success 可能丢失稳健 evidence，random-failure 信息质量不稳，similarity replacement 会覆盖冲突
  history。在线搜索和私有数据削弱复现；论文未定义 model-version swap、concurrent request isolation、
  cache invalidation、checkpoint/rollback、tenant ACL、poisoning recovery 或 crash consistency。
- **Where Previous Design Still Applies**：要求可审计 deletion、强 provenance、低更新频率或任务分布不稳定时，
  版本化 external memory + frozen policy 更安全；数据稀少或 reward 不可信时只保留人工确认的 procedural
  memory；高复用、稳定且可独立验证的策略才值得离线蒸馏进 weights。
- **Evolution Relationship**：`Direct Evolution`：raw trajectory replay → retrieval-guided success/failure
  memory → structured workflow consolidation → Planner-visible procedural memory → online Planner update；
  `Layering / Dependency`：它依赖 GRPO、judge、tool runtime、checkpoint/model registry 和 evaluation harness。
- **ROADMAP / Chapters Read / Existing Coverage**：主 owner Ch73；handoff Ch29、Ch31、Ch62、Ch75～77；
  已读 Ch72～77、Ch29、Ch31、Ch62。Ch73 已覆盖 fact/policy state 分离、raw trajectory→derived strategy、
  provenance/supersession/delete；新增缺口是“external procedural memory 与 parametric Planner state 共存”
  以及 memory clear 不等于 weight unlearning。Ch76 必须保留 reflection 不更新参数的定义边界。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后只在 Ch73 精化双平面状态与 conversion/forgetting 边界，在 Ch29/31/76/77 使用短 handoff；
  不写 benchmark headline，也不把论文命名固化为通用架构。
- **Open Questions**：如何给 memory unit→training example→Planner revision 建立可删除 lineage？并发 serving
  如何原子切换 Planner version？judge poisoning 如何阻断？在固定 tokens、tool calls、wall time 与 p99 SLO
  下，参数更新是否仍优于只读 external memory？

### TriAttention: Efficient Long Reasoning with Trigonometric KV Compression — 28/30

- **Candidate / Week / Score**：TriAttention；2026-W15；28/30。
- **Source Family ID / Type / Date**：`TRIATTENTION-PREROPE-KV-EVICTION`；arXiv paper + HTML +
  author code；v1 2026-04-06，当前无后续 revision。
- **Access / Full-read Coverage**：已读 metadata、Abstract、Introduction、RoPE 与 compression
  related work、全部公式与方法、Implementation、reasoning/memory/throughput experiments、
  baselines、ablation、calibration sensitivity、Limitations、Conclusion，以及 RoPE derivation、
  additional baselines、LongBench/RULER、MLA validation 与 OpenClaw deployment appendices；
  已核对公开仓库入口。
- **Original Problem / Previous Design**：StreamingLLM 的 sink+window 简单且无 learned state；
  H2O/SnapKV/R-KV/LazyEviction 用历史 post-RoPE attention 观察内容相关 importance，在未来与
  最近历史相似时合理。但 RoPE 令 query direction 随位置旋转，可代表未来的 observation window
  很短； dormant retrieval token 可能在再次被需要前已永久 evict。
- **Changed Constraint / Principle**：长 reasoning 让 KV memory 与未来依赖距离同时增长，不能只
  用最近 attention 当未来需求。若 pre-RoPE Q/K 围绕稳定非零中心集中，则 RoPE attention 可近似
  为 Q-K distance 的 trigonometric series；系统可用稳定统计预测未来位置偏好，再用 norm 补足
  concentration 较弱的 heads。
- **Mechanism**：离线 calibration 估计每 head/frequency band 的 query center、expected norm 与
  Mean Resultant Length `R`。runtime 对 cached pre-RoPE key 计算 trigonometric distance score，
  加上按 `(1-R)` 加权的 norm score，并对多个 geometric future offsets 取最大值；每 128 decoded
  tokens、cache 超过 budget 时保留 top-B。GQA 先在各 query head 内 z-score，再跨共享 KV head
  取 max，避免不同 head scale 直接相加。
- **State Ownership / Flow**：calibration statistics 属于 model-revision-owned immutable state；
  request runtime 拥有逐层 KV 与 eviction schedule；top-B selection 改写 request-visible history。
  论文没有定义 prefix-shared block 的引用语义、copy-on-write、rollback、跨 worker transfer、
  cancellation 或 failure recovery，production integration 必须另行补齐。
- **Implementation / Evaluation Contract**：四个 reasoning models：Qwen3-8B、两种 DeepSeek-R1
  Distill 7B/8B、GPT-OSS-20B；通常 NVIDIA A100 80GB、BF16、FlashAttention-2，GPT-OSS 使用
  H100/FlashAttention-3；max generation 32,768、temperature 0.6、top-p 0.95，默认 KV budget
  2048，DS-Llama/MATH 500 为 512；AIME 每题采样 8 次，MATH 500 每题 1 次。吞吐在单 A100、
  16K decode、maximum batch size 下测量，但具体 batch size 未披露。
- **Baselines / Ablations / Sensitivity**：主对照 Full Attention、SnapKV、R-KV；appendix 增加
  LazyEviction、H2O、TOVA、RaaS、StreamingLLM、PyramidKV、KnormPress 等。去掉 trig score、
  norm complement 或 concentration weighting 均退化；future offset range/spacing 与 50K～960K
  calibration tokens 做了 sensitivity。Recursive State Query 用 80 samples/depth 检查 backtracking
  memory，但它是作者设计 proxy，不等同真实 agent state correctness。
- **What Evidence Proves**：在上述合同内，pre-RoPE statistics 能比所测 post-RoPE observation
  baselines 更好维持 accuracy-memory trade-off；论文报告 AIME25 同 accuracy 下 2.5× throughput
  或 10.7× KV reduction，以及跨 GQA/MLA 的 concentration/reconstruction evidence。
- **What It Does Not Prove**：不证明所有模型/head 都稳定 concentrated，不证明 calibration 对
  model fine-tune/adapter/quantization 后仍有效，不证明 average tokens/s 等于 TTFT/TPOT/p99，
  也不证明 periodic top-B eviction 与 continuous batching、prefix cache、paged allocation 和
  speculative decoding 可无缝组合。
- **Limitations / Trade-offs / Failure Modes**：需要保存/访问 pre-RoPE keys 与校准统计，周期性
  global scoring/pruning 有额外 kernel 和 synchronization cost；作者明确把专用 hardware-aware
  kernel、更多 coding/agentic domain、head-specific budget 留作未来工作。低-concentration head、
  distribution shift 或 future-offset mismatch 会错删 dormant token；eviction 不可逆，错误可能
  只表现为流畅但错误的生成。
- **Deployment Boundary**：OpenClaw appendix 是 Qwen3-32B AWQ INT4、单 RTX 4090 24GB、初始
  prompt >15K、读取 6 个 Markdown 文档的单一 demo；它证明该示例避免 OOM，不是并发、质量、
  latency 或可靠性 benchmark。
- **Where Previous Design Still Applies**：短 context、充足 HBM、要求 exact reproducibility、
  calibration 不可信或共享 KV lifecycle 尚未支持安全 eviction 时 Full Attention 仍合理；简单
  sink/window 适合稳定 streaming locality；attention-observation 方法适合未来需求与近期访问
  高度相关且不愿维护 model-specific calibration 的 workload。
- **Evolution Relationship**：`Direct Evolution`：fixed eviction → historical attention scoring →
  delayed observation → calibrated pre-RoPE future-distance scoring；与 paged memory、scheduler、
  GQA/MLA 为 `Layering / Dependency`。
- **ROADMAP / Chapters Read / Existing Coverage**：主 owner Ch41，handoff Ch22；已读 Ch19、Ch22、
  Ch40、Ch41。现有 Ch41 已覆盖 lifecycle、ownership、evict/offload correctness，Ch22 已覆盖 KV
  compression 分支；新证据补足的是 importance-estimation evolution、calibration identity 与
  irreversible eviction failure boundary。
- **Integration Decision**：`Refine — Existing Argument (Provisional; Historical Books Gate Closed)`。
  Gate 通过后只在 Ch41 精化 eviction policy 的技术演进和 state identity，在 Ch22 加短 handoff。
- **Open Questions**：adapter/quantization/model revision 是否必须重新 calibration？如何把 top-B
  eviction 映射到 paged blocks 而不破坏共享 prefix？相同 p99 TPOT/SLO 下，scoring overhead、
  fragmentation 与重新计算成本是否仍优于 baseline？

### FP4 Explore, BF16 Train: Diffusion RL via Efficient Rollout Scaling — 27/30

- **Candidate / Week / Score**：FP4 Explore, BF16 Train / Sol-RL；2026-W15；27/30，维持 discovery score。
  它把 low-precision hardware gain 绑定到 rollout selection 的容错职责，而不直接污染 update target；但只覆盖
  diffusion RL、单节点 B200、自动 reward models 与 deterministic samplers，Project Relevance 保持 4。
- **Source Family ID / Type / Date**：`SOL-RL-PRECISION-SEPARATED-ROLLOUT`；arXiv method/system paper +
  NVIDIA project + Sana repository/recipes。arXiv 仅 v1，2026-04-08 首发，归 W15；repository 是多项目持续演进
  main branch、无 Sol-RL immutable release/tag，2026-08 的后续内容不得倒写进 W15 artifact identity。
- **Direct / Related Primary Sources**：直接来源为 arXiv v1 全文、project page、Sana current repository、Sol-RL
  docs/config family 与 April release note。DiffusionNFT/AWM/FlowGRPO/DanceGRPO、Transformer Engine/NVFP4 和
  reward models 是 algorithm/runtime dependencies，不是作者 headline 的独立复现。
- **Access / Full-read Coverage**：已读 metadata、Abstract、Introduction、GRPO/FP4 preliminaries、rollout-scaling
  bottleneck、direct-quantized degradation、proxy ranking、两阶段 pipeline、全部 experiments/ablations/analysis、
  Related Work、Conclusion，以及 Appendix A～C 的 perturbation/EVT derivation、完整 hyperparameters、rollout
  pipeline、reward identities、rank correlations/extreme-match；并核对 single-node launchers、五类 config family、
  reward checkpoints、current repository news 与版本漂移。
- **Original Problem / Previous Design**：统一 BF16 rollout/update 给每个 trajectory 同一数值语义，最容易维持
  policy/target identity；在 candidate pool 较小或 hardware 不支持原生 low precision 时仍合理。但 selective
  group RL 生成 `N` 个候选、只训练 top/bottom `K` 个，`N-K` 的高精度 generation 被直接丢弃，rollout 会取代
  backward 成为主要成本。直接用 quantized trajectories 更新又会把 distribution/numerical error写进 target。
- **Changed Constraint / Principle**：当 exploration 只需辨认“哪些 seed 值得昂贵评估”，它对 pixel-level
  fidelity 的要求低于 gradient target；同一 pipeline 的不同阶段不必共享 precision，只需共享可追踪的 candidate
  identity。原则是把 approximation 放在可验证、可重放、不会直接进入 objective 的边界，并在 irreversible
  update 前恢复高 fidelity。
- **Mechanism**：Stage 1 为每 prompt 采样 `N=96` initial noise seeds，用 NVFP4 compiled policy 与 6-step
  deterministic ODE solver 生成 previews，reward model 排名并保留 top-12/bottom-12 seeds。Stage 2 用当前 BF16
  policy 和 10-step solver 从同一 24 seeds 重新生成 high-fidelity images，只用这些 samples 执行 DiffusionNFT
  update；新 weights 再 in-place quantize/sync 到 NVFP4 explorer，不重新 compile。low-precision sample 本身不进入
  BF16 regression target。
- **State Ownership / Control and Data Flow**：BF16 trainable policy/LoRA、optimizer 和 update step 是 authoritative
  state；NVFP4 compiled explorer 是由该 policy revision 派生的 serving replica；candidate ledger 拥有 prompt、
  seed、proxy reward/rank、precision、solver/steps、reward-model identity 与 selected status；regenerator 产出新的
  BF16 trajectory。权重 sync 后 explorer generation 才可服务下一轮，不能把 stale proxy ranks 与新 policy 混组。
- **Implementation Details**：SANA-1.5 1.6B、FLUX.1-dev、SD3.5-L 用 LoRA `r=32, alpha=64`、AdamW
  `3e-4`、BF16 update、8 GPUs；micro-batch/accumulation、solver、resolution、gradient clipping 依模型不同。
  NVFP4 路径依赖 NVIDIA Transformer Engine/Blackwell，docs 暴露 `diffusionnft`、`naive_scaling`、`compile`、
  `naive_quant`、`sol_rl` 五类配置；current repo 宣称 recipes/datasets released，但 paper 没有固定 commit/hash。
- **Evaluation Contract**：全部实验在单节点 8×NVIDIA B200；训练/eval prompts 来自 PickScore split，ImageReward、
  CLIPScore、PickScore、HPSv2 分别作 training objective 并用四指标评估。主对照含 AWM、DiffusionNFT、FlowGRPO、
  DanceGRPO；FLUX.1 表按相同 GPU-hour budget，precision/steps/pool/selected-count 如上。未披露 prompt counts 的
  held-out size/seed、重复 runs、variance/CI、reward-model inference cost breakdown、power/energy、interconnect、
  exact TE/kernel/commit、host pipeline 或 multi-node scaling。
- **Results / Ablations / Sensitivity**：作者报告 `N=24→96, K=24` 的 HPSv2 单调上升，preview steps 6 达到局部
  饱和；NVFP4/BF16 在三模型上的 IS/CLIP 接近，但这些 global metrics 不能单独证明 seed rank。Appendix rank
  test 报四 reward 平均 Spearman 0.927、Kendall 0.798、Top-4 match 96.9%，说明在作者 distribution 中 proxy
  可筛 extreme seeds。`24-in-96` 相比 BF16 naive scaling 的 rollout speedup 为 1.41～2.41×、iteration
  1.25～1.62×；所谓最高 4.64× 是达到某 reward level 的 convergence speedup，不是单 iteration throughput。
- **Theory Boundary**：Appendix 把 FP4/solver error 建模为 bounded perturbation，要求 vector field 和 reward
  Lipschitz，再把 per-seed reward error界为常数 `Delta`；随后假设同 prompt rewards i.i.d. Gaussian，用 extreme
  range 约 `2*sigma*sqrt(2 log N)` 得到 selected range 下界减 `4*Delta`。它是条件性说明，不测量真实 Lipschitz
  constants、相关 seeds、heteroscedastic/error-rank correlation 或 reward saturation，不能称为生产保证。
- **What the Evidence Proves / Does Not Prove**：证据支持：在上述三种 diffusion models、deterministic seed
  regeneration 与 B200 contract 下，NVFP4 preview 可较好保存作者 reward ranks，BF16 regeneration 避免直接
  拟合 quantized images，并减少 large-pool rollout wall time。它不证明 FP4 rollout on-policy，不证明 reward
  ranking 等于人类偏好，不证明 LLM token trajectories 可由 seed 精确重生，也不证明 `N` 无限扩大会持续获益。
- **Limitations / Threats to Validity**：论文没有独立 Limitations section；主要威胁包括 automated reward
  Goodhart/bias、PickScore-domain concentration、single-node/vendor-specific hardware、无 uncertainty、current-code
  drift，以及同一 reward 既 selection 又 optimization 时的 correlated error。减少 preview steps 与 quantization
  同时变化，主收益不能完全分解；BF16 regeneration 仍需 `K` 次昂贵 rollout，reward scoring 也未消失。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：分精度 pipeline 扩大廉价搜索、保护 update
  fidelity，却新增两套 model representations、每 step quantize/sync、seed/proxy lineage、rank false positive/
  negative 和 stale explorer。若 sampler 含不可重放 randomness、tool/environment state、autoregressive branching
  或外部 side effects，保留 seed 不足以重建同一 trajectory。BF16 brute-force 在 rank drift 高、`N≈K`、
  reward昂贵或 B200/TE 不可用时仍合理；统一低精度 + importance correction 是另一分支，不应被否定。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：`Direct Evolution`：group rollout → larger candidate
  pool + contrastive subset → low-fidelity proxy pool + high-fidelity regeneration；`Alternative Branch`：direct
  quantized rollout、importance correction、unified low-precision rollout/update；`Layering / Dependency`：NVFP4/
  TE、reward service、policy sync。已读 Ch28～32、Ch35；主 owner Ch29，Ch31/32/35 短 handoff。
- **Existing Coverage / Integration Decision**：Ch29 已覆盖 rollout bottleneck、group size、measurement-as-reward、
  partial/cross-policy trajectory lineage，但尚未明确“approximate exploration artifact 与 objective-bearing
  training artifact 分离”以及 deterministic regeneration 的适用边界。暂定 `Refine — Existing Argument
  (Experimental; Provisional; Historical Books Gate Closed)`；Gate 后只 refine Ch29，不写固定 FP4/Blackwell recipe。
- **Open Questions**：怎样在线校准 proxy rank drift 并决定 fallback BF16 fraction？reward model 版本、seed、solver、
  precision 与 policy revision 怎样形成可恢复 ledger？当 trajectory 不可 deterministic replay 时，能否以高精度
  re-evaluation/importance correction 替代 regeneration？在 matched reward-service cost、energy 与 multi-node
  synchronization 下，exploration/update 分精度的 break-even 在哪里？

### MARS: Enabling Autoregressive Models Multi-Token Generation — 26/30

- **Candidate / Week / Score**：MARS；2026-W15；26/30，维持 discovery score。它把多 token generation
  从额外 drafter/head 转为同一 AR backbone 的可选能力，并公开训练与 batch-cache 实现；但只有两个模型规模、
  7B 只测 block size 4、runtime contract 窄且无独立复现，Longevity 保持 3。
- **Source Family ID / Type / Date**：`MARS-MASK-AUTOREGRESSION`；arXiv method/system paper + author code。
  arXiv 仅 v1，2026-04-08 首发，归 W15；current repository 无 release/tag，README 与论文在 7B tested block
  sizes 上出现 `4` 对 `4/8/16` 的漂移，不能把 current main 当 immutable event-date artifact。
- **Direct / Related Primary Sources**：直接来源为 arXiv v1 全文、metadata/revision history、author repository、
  training/evaluation/benchmark entrypoints 与 release boundary。Block Diffusion、Jacobi、Medusa/EAGLE、MTP 和
  speculative sampling 是作者比较的演进依赖，不是 MARS headline 的独立复现。
- **Access / Full-read Coverage**：已读 Abstract、Introduction、Background/Related Work、四类 AR/block gap、
  双流 attention mask 与 losses、sliding-window inference、全部主实验、Conclusion/Limitations，以及 Appendix
  A～D 的 training cost、完整 threshold sweep、Jacobi baseline 和 acceptance-metric sensitivity；并核对 repository
  的两阶段训练参数、one/multi-token harness、block-cached benchmark 命令和无 release 状态。
- **Original Problem / Previous Design**：标准 AR 每步只提交一个真实 token，语义简单、与任意 sampling policy
  兼容，KV append 与 streaming commit 也清楚；独立 drafter + target verification 可在不改 target distribution
  的条件下减少 target serial steps，auxiliary heads 则提高候选相关性。它们合理但增加第二模型、额外参数、
  target/draft artifact coupling 或 verification orchestration。
- **Changed Constraint / Principle**：如果 pretrained AR backbone 已学会 next-token distribution，能否只通过
  continued SFT 让同一 head 在未知 future positions 上产生多个候选，同时保住原 AR mode？关键不是放弃
  causality，而是只保留不可避免的 placeholder gap，把 attention pattern、logit alignment 和 commit order
  重新对齐 AR contract。
- **Mechanism**：response 按 block size `B` 切分；单次 training sample 连接 clean stream 与全 `[MASK]`
  noisy stream。clean stream 标准 causal attention；noisy block 内仍 causal，只能看到同 block 的 mask positions，
  并跨流读取之前 completed blocks 的 clean prefix。`L_mask` 学习 incomplete-context prediction，等权
  `L_AR` 继续 next-token SFT。没有 clean loss 时完全 clean-context 的 masked positions 比例约为 `1/B`；
  双流后作者用 `(1+1/B)/2` 描述 AR-like loss-term fraction，防止 block 增大时训练信号单向漂移。
- **Inference / Acceptance Contract**：runtime 在 prefix 后追加 `B` 个 masks，一次 causal forward 得到各位置
  logits，从左到右连续提交 `max_v p(v)>=tau` 的 greedy predictions，且至少提交一个；再补齐 masks 并滑动。
  `tau=1` 被实现为单 token mode，降低 threshold 增加 accepted tokens，也会改变输出。这里没有独立 target
  model、`p/q` residual correction 或 exact verification，因此它是 learned lossy parallel decoding policy，
  不能沿用经典 speculative sampling 的 distribution-preserving 结论。
- **State Ownership / Control and Data Flow**：checkpoint/tokenizer 拥有 mask capability、block size 和训练身份；
  request runtime 拥有 prefix、mask window、confidence policy、accepted cursor、KV 与 streamed-token commit；
  scheduler 拥有 batch membership 和 operating point。训练 artifact 不能替 runtime 决定 SLO；confidence score
  不能越过 left-to-right prefix 直接提交；KV state 与用户可见 token 必须在同一 accepted boundary 上提交。
- **Implementation Details**：先在 Dolci-Instruct-SFT 约 2M examples 上做 5 epochs AR SFT，再用同一数据做
  5 epochs MARS；max length 512、BF16、8×H200、AdamW、`5e-6`、effective batch 384。MARS 将 clean/noisy
  序列连接，作者报告训练 H200-hours 约为 AR SFT 的 2.0～2.2×、peak memory 约 1.5×；“无额外参数”并不
  等于无额外训练成本或现有 serving engine 可直接启用 multi-token path。
- **Evaluation Contract**：Qwen2.5-0.5B-Instruct 测 `B=4/8/16`，Qwen2.5-7B-Instruct 只测 `B=4`；六个
  benchmarks 均 greedy、最多 256 new tokens，shot 设置依任务而异。one-token baseline 包含 5-epoch AR SFT、
  10-epoch compute-matched AR SFT 与 0.5B Block Diffusion；没有 seed、variance、置信区间、长输出、sampling、
  multi-turn、continuous/adversarial arrival、TTFT/TPOT/p99 或能耗。
- **Results / Ablations / Sensitivity**：one-token mode 的六项均值在作者设置中高于 5-epoch AR SFT，但这只是
  两个 checkpoint-family 的 empirical result，不足以证明 universal strict superset。去掉 clean AR loss 时，
  0.5B 的 block size 4→16 平均分由 28.4 降到 22.2；加入后为 30.4→29.7，支持 loss 防 signal decay。
  `tau=0.95` 时作者报告约 1.46～1.68 tokens/forward，但平均分比各自 one-token mode 低 1.1～1.6，IFEval
  约低 5 points；更激进 threshold 会明显退化。Entropy/top-2 margin 只在 GSM8K 显示相近 frontier。
- **Block-Level KV Cache / Wall-Clock Boundary**：无 cache 时 MARS 在 batch 4/8/16 分别只有 AR 的
  0.90/0.49/0.23×。作者每个 cache block 先计算 prefix KV，再让 batch 内样本用 cached prefix 推进 masks；
  cache cursor 只能按最小 accepted progress 前移，快样本等待慢样本。Qwen2.5-7B、GSM8K 256 questions、
  `tau=0.95` 下，最优 `B_cache` 随 batch 改变，作者最高报告 batch 4 的 1.71×、batch 16 只剩 1.34×；
  论文没有披露该 inference benchmark 的 GPU 型号、precision、prompt/output 分布、warmup、kernel/runtime
  revision 或 tail latency，故 headline 不能外推。
- **What the Evidence Proves / Does Not Prove**：证据支持：在作者 checkpoint/data/greedy benchmark 内，恢复
  AR-compatible attention/alignment/order 并保留 clean loss，能让同一 backbone 同时具有 one-token 与
  confidence-gated block prediction；block-aware KV reuse 是 wall-clock 收益的必要条件。它不证明输出分布与
  原 AR 完全相同，不证明 confidence 已校准，不证明任意模型/采样/SLO 获益，也不证明“无架构修改”等于
  无 tokenizer、training、runner、cache 和 scheduler 修改。
- **Limitations / Threats to Validity**：作者明确只在 7B 测 `B=4`，低 threshold 质量下降，block cache 在大
  batch 受同步限制。再加上单一 instruction dataset、greedy-only、无 uncertainty、repository drift、缺失
  inference hardware/runtime identity 和无 production traffic，外部效度有限；one-token improvement 也可能受
  fine-tuning path/data order 影响，10-epoch AR overfit baseline 不能单独排除全部 compute/data confound。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：MARS 省去第二模型和额外 heads，却把成本
  移到双长度 training、mask-capable checkpoint、confidence error、variable progress 与 block-barrier idle；
  false-high-confidence token 一经提交不会被 target rollback。标准 AR 适合质量/可复现优先或 runtime 不支持
  mask path；经典 exact speculative sampling 适合必须保持 target distribution；auxiliary drafter/head 在无需
  改 target weights、或已有成熟 verification kernels 时仍合理。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：与 block diffusion 为 `Direct Evolution`：masked
  future + bidirectional/out-of-order → masked future + causal/right-shifted/left-to-right；与 independent drafter、
  Medusa/EAGLE/MTP 为 `Alternative Branch + Principle Reuse`；与 KV cache、batching、scheduler 为
  `Layering / Dependency`。已读 Ch40、Ch41、Ch44、Ch48、Ch52；主 owner 为 Ch44，Ch40/41/52 短 handoff。
- **Existing Coverage / Integration Decision**：Ch44 已覆盖 exact/lossy acceptance、MTP/drafter evolution、
  KV transactional commit 与 verification capacity，足以拒绝“multi-token = lossless speculation”的混写；
  缺口是同-backbone masked proposal 这一替代分支，以及 block-boundary synchronization 如何令 algorithmic
  tok/forward 与 wall clock 分离。暂定 `Refine — Existing Argument (Experimental; Provisional; Historical
  Books Gate Closed)`；Gate 后只精化 Ch44，其他章节短 handoff，不保留固定 speedup/threshold 数字。
- **Open Questions**：如何用 matched sampling policy 量化 distribution drift？confidence calibration 是否跨
  domain、length、temperature、quantization 与 adapter 稳定？cursor-based asynchronous cache 能否消除 batch
  barrier 而保持 KV/token atomic commit？在相同 TTFT/TPOT/p99、concurrency、energy 和 training amortization
  下，它何时优于 exact speculation 或普通 continuous batching？

### Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference — 26/30

- **Candidate / Week / Score**：Flux Attention；2026-W15；26/30，维持 discovery score。论文把固定
  dense/sparse topology 改为 prompt-conditioned layer routing，并同时报告质量、Prefill E2E 与 Decode kernel
  latency；但只有作者实验、无独立复现，production serving contract 与 immutable release 也不完整，
  Source Reliability 保持 4、Longevity 保持 3。
- **Source Family ID / Type / Date**：`FLUX-CONTEXT-LAYER-ATTENTION-ROUTING`；arXiv method/system paper +
  author repository。arXiv 只有 v1，2026-04-08 首发，归 W15；current GitHub 有 27 commits、无 release/tag，
  论文/README 给出的 model collection 仍是空链接，不能把 current main 当 event-date checkpoint。
- **Direct / Related Primary Sources**：直接来源为 arXiv v1 全文、metadata/revision history、author repository、
  training model forks、Block-Sparse-Attention dependency 与 nano-vLLM integration tree。DuoAttention、PruLong、
  TriangleMix、Elastic Attention、NSA/DSA 是比较或演进依赖，不是 Flux headline 的独立复现。
- **Access / Full-read Coverage**：已读 Abstract、Introduction、Preliminary、router/soft-hard routing、sparsity
  constraint、deployment、全部主实验与 Analysis、Conclusion，以及 Appendix A～F 的 artifact、Related Work、
  entropy baseline、latency protocol、training/baseline/kernel config、data/pooling sensitivity 和 error cases；
  已核对 repository README、training/eval model paths、sparse kernel dependency、nano-vLLM tree 与无 release 边界。
- **Original Problem / Previous Design**：固定 dense/sparse layer 或 retrieval/streaming head 划分可预测、可提前
  编译，适合 task distribution 稳定的服务；head-level dynamic allocation 能为每个 input 保留更细 budget。
  但固定配比无法区分 retrieval-intensive 与 holistic prompts，动态 mixed heads 又会形成不规则 KV load、
  intra-layer straggler 与 synchronization tail，使理论 FLOP reduction 不等于 Decode wall-clock gain。
- **Changed Constraint / Principle**：当 workload 的长程 retrieval 需求随 prompt 改变，路由应感知 context；
  当 Decode 受 memory bandwidth 和 kernel regularity 支配，决策粒度又必须与可整块跳过的硬件执行单元一致。
  因而 routing granularity 是 quality flexibility 与 executable regularity 的共同设计变量，而非越细越好。
- **Mechanism**：每层 Layer Router 从 incoming query tensor 取 prompt 前后各 100 tokens，经 pooling 与 MLP
  产生 FA/SA logits。训练冻结 backbone，以 Gumbel-Softmax 形成 Full/Sparse Attention convex mixture，配合
  task-category sparsity target 和可学习 Lagrange coefficients；inference 取 argmax 硬路由。该决定在 Prefill
  执行一次并缓存给后续 Decode；sparse layer 只保留/读取 sparse kernel 所需的 sink/local/selected KV，
  retrieval layer 仍使用完整历史。
- **State Ownership / Control and Data Flow**：checkpoint/config 拥有 router weights、pooling、FA/SA implementation
  与 sparsity policy；request runtime 必须拥有 prompt-derived route vector、每层 KV retention identity、position
  和 fallback reason；kernel 执行具体 full/sparse path；scheduler 仍拥有 batch/admission。路由与 KV layout
  不能独立变化：把同一 prefix 的 KV 分享给 route/config 不兼容的 request 会产生 silent semantic corruption。
- **Implementation Details**：Qwen3-4B/8B 与 Llama-3.1-8B-Instruct backbone；65,536-token BF16 training，
  8×A800、global batch 48、300 steps、FSDP hybrid sharding、AdamW。训练集混合 ChatQA2-Long-SFT、MuSiQue、
  CoLT-132K、GovReport、XSum，共约 0.74B tokens、1K～64K。Block-Sparse-Attention 使用 block 64、chunk
  16,384、sink 128、local 2,048；current README 的 A100/H100 environment 与论文 A800 contract 不同，
  也未提供可定位 model artifact。
- **Evaluation Contract**：质量用 LOOM-Eval 覆盖 LongBench-E、RULER 8K～256K、LongBench-v2、GSM8K、
  AIME24；baseline 为 dense backbone、DuoAttention、PruLong、TriangleMix，并测试 SSA/XAttention/Triangle
  sparse layer。Decode latency 单张 A800 80GB、PyTorch BF16、batch 1、10 warmups + 50 iterations，报告
  单 token average kernel wall time；Prefill 报 256K E2E speedup。并发、continuous batching、TP、queueing、
  TTFT/TPOT/p95/p99、quantization、energy、seed、variance 与 confidence interval 均 `Not Disclosed`。
- **Results / Ablations / Sensitivity**：作者最高报告 256K Prefill 2.8× E2E、Decode 接近 2.0× kernel speedup；
  二者口径不能合并成 serving speedup。不同 backbone/task/SA kernel 的质量并非单调，表中 sparse-decode
  rows 还依赖 PDF shading 才能区分。Router 约 0.20 ms/layer 的表述没有给出 batch/并行/计时边界。data mix
  偏斜会使 routes homogenize；pool 超过前后各 100 tokens 反而引入 noise，retrieval tasks 可能被过度 sparsify。
- **What the Evidence Proves**：在作者三种 backbone、训练 mix、sparse kernels 和单卡 batch-1 latency contract
  内，prompt-conditioned layer-level hard routing 可以学到不同 task/context 的 FA/SA 配置，并比所测
  head/static baselines 更容易把 KV traffic reduction 转成 wall-clock gain。它也证明 router training 可在冻结
  backbone 下完成，而不是证明 model semantics 完全不变。
- **What It Does Not Prove**：不证明 route 对 unseen domain、adversarial prompt 或 prompt 中途 phase change
  稳定，不证明 sparse output 与 dense exact-equivalent，不证明 layer granularity 普遍优于 head/block/token
  granularity，也不证明 2.8×/2.0× 可外推到 multi-request serving。部分 score 高于 dense baseline 可能来自
  finite evaluation/regularization；无 uncertainty 不能据此声称 sparse Attention 提升通用 reasoning。
- **Limitations / Threats to Validity**：论文没有独立 Limitations 章节；仅三个 4B/8B backbones、作者训练数据、
  单一 A800 latency path、batch 1、无 uncertainty 和 current artifact drift 限制外部效度。边界-token pooling
  假设 instruction/query 位于 prompt 首尾，balanced curriculum 又成为新的 distribution dependency；硬路由
  固定整个 Decode，无法响应 tool result、长 generation 或 context append 后的需求变化。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：layer routing 获得规则执行和整层 KV
  bypass，却牺牲 head-level budget flexibility，并新增 route misclassification、train/inference soft-hard gap、
  per-request route/KV identity、mixed-route batch fragmentation、prefix-cache incompatibility 与 fallback/rollback。
  Dense FlashAttention 在短 context、strict exactness、unseen workload 或 kernel 不支持时仍是可靠基线；固定
  hybrid topology 在 route overhead/variance 不可接受时更可预测；head-level allocation 在硬件能高效执行
  heterogeneous heads、且细粒度质量价值更高时仍合理。
- **Evolution Relationship**：`Direct Evolution`：fixed hybrid topology → context-aware head budget →
  context-aware layer hard route；`Alternative Branch + Principle Reuse`：NSA/DSA 的 token/block selector；
  `Layering / Dependency`：Prefill sparse execution、Decode KV traffic、batch composition 与 scheduling。新方案
  没有否定旧方案，而是把约束从纯模型稀疏扩展到 hardware-contiguous runtime。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch22、Ch39～42、Ch52。主 owner 为 Ch22，因为
  新增的是长上下文 Attention contract、迁移与 granularity trade-off；Ch39 只承接 sparse Prefill E2E accounting，
  Ch40～41 承接 Decode route/KV identity，Ch52 承接 mixed-route batch 和 SLO。Ch22 已覆盖 linear/hybrid、
  NSA/DSA 与 hardware-aligned sparsity，缺口是 input-conditioned layer granularity 以及 route 生命周期。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后只在 Ch22 精化 static→fine dynamic→hardware-aligned coarse dynamic 的演进，其他章节短 handoff；
  不保留固定 speedup、router latency、pool size 或训练 recipe。
- **Open Questions**：route vector 怎样进入 prefix/KV cache identity，并支持 policy/model update 后 invalidation？
  mixed-route requests 如何 batching 而不产生 kernel explosion 或 fairness regression？tool result/Decode phase 改变
  retrieval demand 时是否允许 re-route，若允许怎样迁移/补建已丢弃 KV？什么 confidence 或 OOD signal 触发
  dense fallback？在 matched TTFT/TPOT/p99/goodput、TP 与 concurrency 下，layer granularity 何时仍优于 static/head？

### DMax: Aggressive Parallel Decoding for dLLMs — 25/30

- **Candidate / Week / Score**：DMax；2026-W15；25/30。Technical Novelty/System Impact/Project Relevance
  保持 5；Source Reliability 因 work-in-progress、无 uncertainty、只有单一 16B base family、event-time artifact
  晚一天发布且后续 revision drift，从 4 降为 3，总分 26→25。
- **Source Family ID / Type / Date**：`DMAX-SELF-REVISING-DIFFUSION-DECODE`；arXiv method/system paper +
  author code/model/data artifacts。v1 于 2026-04-09 14:35 UTC 首发，归 W15；v2 04-20、v3 05-15
  只用于 revision boundary。repository 记录 paper/code/model/data 于 04-10 发布，05-25 又增加 general-purpose
  DMax-16B；current main 45 commits、无 release/tag，不能当作 W15 immutable snapshot。
- **Direct / Related Primary Sources**：直接来源为 arXiv v1 metadata/HTML/PDF、author repository、dFactory/
  dInfer integration、Math/Coder model cards 与 self-distillation datasets。LLaDA-2.0-mini、dParallel、Hierarchical
  Decoding、uniform diffusion training 是 base/baselines；后续 DMax-16B 是 later evolution，不进入事件结论。
- **Access / Full-read Coverage**：已读 metadata/revision、Abstract、Introduction、Preliminaries、OPUT 公式与
  training flow、SPD 公式/Algorithm 1、全部 experiment setup/results、accuracy-TPF curves、training/inference/
  convergence ablations、Related Work、Conclusion；论文没有独立 Limitations 或 Appendix。已核对 repository
  training/evaluation instructions、model/data cards、`generate_spd` entry、commit/release boundary。
- **Original Problem / Previous Design**：MDLM 以 fully masked block 开始并逐步把 mask 转成 token，已提交 token
  为后续预测提供稳定、离散 context，runtime 简单且进度清楚；但 aggressive parallel promotion 会同时提交多个
  错误，之后不能修正，错误作为 context 级联。UDLM 能 token-to-token re-denoise，却从 uniform random tokens
  起步，输入远离 natural-language manifold，训练和生成不稳定。
- **Changed Constraint / Principle**：若目标是在一个 forward 推进更多位置，就不能只提高 promotion rate，还要
  为错误提供 correction path。长期原则是：parallel progress 的上限由“错误是否可撤销”和“训练是否覆盖 runtime
  中间状态”共同决定；把可变状态只加入 inference 而不改变 training distribution 会形成 contract mismatch。
- **Mechanism**：OPUT 对 clean sequence 先按固定 noise ratio 产生 masked input，再用当前模型在 masked positions
  采样 self-predicted noisy sequence；masked input 与 predicted input 分别 forward，均对全位置 clean target 做
  cross-entropy，保留 mask denoising 并学习纠正自己的预测。SPD 以 block 为单位，从左到右提升连续 high-confidence
  prefix；已提升位置不立刻冻结，而以 top-1 token embedding 和 mask embedding 按 confidence 插值并归一化，下一
  step 重预测。连续两步 top-1 稳定或全位置 confidence 超过 acceptance threshold 时，才 commit whole block。
- **State Ownership / Control and Data Flow**：checkpoint/training artifact 拥有 OPUT learned correction capability；
  request runtime 拥有 block boundary、mask/token sets、hybrid embeddings、previous top-1/confidence、step count、
  convergence state 与 committed prefix；scheduler 拥有 batch/forward budget；stream 只能暴露 committed block，
  不能把可修订 token 当最终输出。model revision、threshold、block length 与 convergence rule 共同定义 decoding
  policy identity；它们变化时 cache/graph/profile 也须重新验证。
- **Implementation Details**：base 为 LLaDA-2.0-mini 16B MoE；OPUT fixed mask ratio 0.75，full-parameter fine-tune
  2 epochs、batch 8、learning rate 2e-6 cosine、block 32、8×H200。masked 与 predicted inputs 分开 iteration
  优化以避免同时驻留的额外 memory。Math/Coder targets 由 base model 自蒸馏，confidence 0.95、block 32、
  max 2048，丢弃未完成样本，得到约 0.7M math 和 1.0M code samples。model/data artifacts 页面显示 04-20
  update，晚于 v1/event-day release，artifact identity 不是严格同日证据。
- **Evaluation Contract**：math 为 GSM8K、MATH500、Minerva-Algebra、ASDIV，code 为 HumanEval-Instruct、
  MBPP-Instruct；zero-shot、generation length 2048、batch 1、dInfer、2×H200 tensor parallel。DMax-Math
  threshold 0.5，Coder 0.65，acceptance 0.9；baseline 为 base threshold 0.95、Hierarchical low threshold 0.2、
  dParallel-SFT 和 matched-setting uniform diffusion training。precision、TP degree 数值、warmup/repeats、seeds、
  variance、energy、TTFT/TPOT/p99、continuous batching 与 request concurrency 除 batch 1 外 `Not Disclosed`。
- **Results / Ablations / Sensitivity**：作者在该 contract 下报告 average TPF 2.8→6.2 且 accuracy 接近，单项
  TPS 约 512～1557；这些不是 production goodput。OPUT-only 在 threshold 0/0.5 显著降低 collapse；soft hybrid
  state 把 threshold 0 的 GSM8K 68.2% 提到 90.4%，而原模型直接套 SPD 为 0%。contiguous prefix 的增益较小；
  consistency 是主要 stop signal，confidence 可省最后一次 forward。低并行下的 accuracy 增益缺少 uncertainty，
  不能据有限 benchmark 认定 self-revision 普遍提高 reasoning。
- **What the Evidence Proves**：在 LLaDA-2.0-mini、作者 self-distillation、两类 domain、block 32、batch 1
  和 2×H200 contract 内，training on self-generated noisy states 是 soft self-revision 成立的必要条件；组合 OPUT
  与 SPD 能把更 aggressive block progress 转化为较好的作者 accuracy-TPF operating points。Ablation 证明的是
  训练与中间状态机制的耦合，不是任意 dLLM 或 AR model 都能获得相同结果。
- **What It Does Not Prove**：不证明 output distribution 与 base model exact-equivalent，不证明 token/embedding
  revision 能跨 base families、general domain、long context、sampling policy 或 quantization 稳定，不证明 TPF/TPS
  能外推到多请求 goodput 或 tail SLO，也不证明自蒸馏数据没有 benchmark overlap/selection bias。两 H200 与
  batch 1 的 throughput 不能称为通用 serving capacity。
- **Limitations / Threats to Validity**：论文没有 Limitations 章节，且标记 work in progress。只训练一个 16B
  MoE base 的两个 domain variants；无 seed/variance、unseen-domain、adversarial/long-context、multi-batch、
  failure recovery 或 independent reproduction。丢弃 2048 内未完成的 self-distillation samples 改变训练分布；
  confidence calibration 决定 progress/quality，却没有跨 domain/model drift 分析。v2/v3、45-commit current repo
  和 05-25 general model 说明 source family 快速变化。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：self-revision 放宽 early commit，换取额外
  full-block forwards、hybrid-state memory、threshold calibration、oscillation/convergence risk、streaming delay 与
  更复杂 scheduler accounting。普通 MDLM 在保守 threshold、低并行、无需额外 fine-tune 时更简单；UDLM 在本就
  以 token-to-token denoising 训练时仍是独立分支；AR 在需要严格 left-to-right streaming、成熟 KV cache 和 exact
  sampling contract 时仍合理；speculative decoding 在必须保持 target distribution 时仍合理。
- **Evolution Relationship**：`Direct Evolution`：binary mask→committed token → on-policy revisable token state →
  confidence-carrying hybrid embedding → block convergence commit；`Alternative Branch`：AR/speculative decoding；
  `Layering / Dependency`：OPUT training、block scheduler、KV/cache/kernel/graph、stream commit 与 EvalSpec。
  DMax 没有否定 AR/MDLM，而是用可修订状态交换更高的并行潜力与更复杂的模型-runtime contract。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch29、Ch40～44、Ch48、Ch52。主 owner 为 Ch40，因为
  它改变 Decode 的 dependency/commit state machine；Ch29 承接 on-policy training state，Ch44 只说明它不是
  exact speculative verification，Ch52 承接 variable forward progress/convergence scheduling。Ch48 不拥有该
  机制：两 GPU TP 只是执行配置，并没有 distributed request/KV/control-plane 新设计。Ch40 当前只完整解释 AR
  逐 token依赖，确有一个“alternative decoding state machine”缺口。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后可在 Ch40 加一个受限分支：AR 的不可撤销顺序依赖不是所有生成模型的唯一状态机；diffusion/block
  路线以可修订中间状态换并行，但训练分布、commit/convergence、streaming 与 scheduler 必须共同改变。只做
  Ch29/44/52 短 handoff，不保存固定 threshold、TPF/TPS 或 DMax 名称为长期定义。
- **Open Questions**：hybrid token states 怎样进入 KV/cache/compiled-graph identity，re-predict 时哪些 layer state
  可安全复用？多请求 continuous batching 如何给不同 convergence rate 的 blocks 分配 token/forward budget？
  oscillation、max-iteration、deadline 与 cancellation 如何 fail closed？block commit 前能否低延迟 streaming？
  在 matched quality、TTFT/TPOT/p99/goodput、energy 与 training amortization 下何时优于 AR speculation？

### KnowU-Bench: Interactive, Proactive, and Personalized Mobile Agent Evaluation — 24/30

- **Candidate / Week / Score**：KnowU-Bench；2026-W15；24/30（Technical Novelty 4、System Impact 4、
  Practical Value 4、Source Reliability 4、Project Relevance 5、Longevity 3），维持 discovery score。论文、
  project 与可运行代码公开，evaluation object 对 Agent system 很相关；但 synthetic users、simulator/judge
  coupling、无 uncertainty 和 event-time/current artifact drift 仍阻止更高证据等级。
- **Source Family ID / Type / Date**：`KNOWU-INTERACTIVE-PERSONALIZED-PROACTIVE-EVAL`；arXiv benchmark/
  system paper + official project + author code。arXiv 只有 v1，2026-04-09 16:50 UTC 首发，归 W15；HTML
  manuscript masthead 写 2026-07-29，但 submission history 才是 first-public owner。repository README 记录 code
  04-07、experiment Docker 04-11 发布；current main 20 commits 且没有可见 release/tag，不能当作 immutable
  04-09 artifact snapshot。
- **Direct / Related Primary Sources**：直接来源为 arXiv metadata、v1 全文、project page、author repository、
  environment/task/user-profile/log/agent/runtime/evaluator 目录及 release boundary。MobileWorld 与改造的 Android/
  app code 是 environment dependencies；被比较模型和先前 benchmarks 不是本文结果的独立复现。
- **Access / Full-read Coverage**：已读 Abstract、Introduction、Related Work、POMDP/environment、user-agent
  hidden-profile contract、三类 task、hybrid scoring、全部 experiment setup/results/ablation/error analysis、Conclusion，
  Appendix A～F 的 pipeline、GUI action space、23-app inventory/packaging、profile/log schema、prompt/rubric入口与
  success/failure cases；并核对 project leaderboard 和 current repository 的 install、Docker/KVM、CLI、task/agent/
  app registry、RAG/noise switches、trajectory viewer。论文没有独立 Limitations；hardware、API sampling 与 total
  cost 多数未披露。
- **Original Problem / Why the Previous Design Was Reasonable**：static preference/intent benchmark 通过固定
  history 做离线 recovery 或 ranking，成本低、可重复、易于隔离 perception/retrieval；deterministic GUI suite
  通过 explicit instruction 测 execution，也有清楚 oracle。它们合理地把系统拆成可控单元，却无法判断信息不足
  时是否会澄清，也无法测无用户指令时应 act、ask 还是 remain silent，更不能核验 rejection 后是否停止。
- **Changed Constraint / Principle**：personal assistant 的目标从“按明确指令完成动作”变成“在 partial
  observability 下代表特定用户决定是否行动”。长期原则是：**autonomy evaluation 必须同时测 opportunity、
  authority、information acquisition、environment outcome 与 abstention/rejection behavior**；只测成功动作会把
  过度主动奖励成能力，只测拒绝又会把永久沉默奖励成安全。
- **Mechanism**：每个 task 在 rooted Pixel 8 AVD container snapshot 中初始化，FastAPI/controller 把 typed GUI
  actions 映射到 ADB，并重置 backend、callback、history 与必要的 device time。GUI agent 只见 instruction、
  screenshot/state、exposed behavioral log `H` 与 interaction history；gpt-4o user simulator 独占 structured profile
  `P`，在 `ask_user` 后生成 preference reply 或 accept/reject。General tasks 给明确目标；Personalized tasks 隐藏
  preference 并允许澄清；Proactive tasks不给目标，要求 direct execute、proposal/confirmation 或 silence。
- **State Ownership / Control and Data Flow**：benchmark/evaluator 持有 hidden profile、task oracle、environment
  snapshot、rule callbacks、rubric、step budget 与 final verdict；user simulator 持有被隐藏的 profile view 与
  dialogue response policy；Agent 只拥有当前 observation、exposed logs 与 proposal history；workflow/controller
  拥有 action dispatch、reset、timeout 和 trace。flow 为 task/profile/environment init → bounded observations/logs →
  act/ask/silent proposal → optional simulated feedback → authorized GUI transition → rule/semantic evidence → verdict。
  hidden profile 不能泄露给 Agent，否则 preference inference 退化为 lookup。
- **Implementation Details**：42 general、86 personalized、64 proactive tasks，共 192 tasks、23 app scope；current
  README 同时说明 checkout 的 task registry 只直接引用 17 app identifiers，属 scope/implementation 口径差异。
  profiles 是 Developer、Grandma、Student、Researcher 四个合成 archetypes，YAML 顶层含 identity/location/
  digital context/habits/preferences/decision criteria/social graph；logs 由 LLM 按 profile 生成再人工检查，noise
  variant 注入约 25% distractors，默认不会向 Agent暴露 label/category。full-history 与 embedding RAG、clean/noisy
  形成 memory ablation；max steps 50，current CLI 支持并发 emulator workers，但论文实际并发与机器规格未披露。
- **Evaluation Contract**：11 个 GUI/general/closed models；main setting 为 full-log noisy，general/proactive 报
  Success Rate，personalized 同时报告 strict SR 与 weighted score；Efficiency=`50/AverageSteps`，Interaction
  Efficiency=`mean(S_i/max(c_i,1))`；proactive 分别报告 warranted-action 的 Act、unnecessary-action 的 Silent、
  explicit-rejection 后的 Stop。hard state/side effect 用 rule judge；semantic preference/communication 用 rubric
  judge，并按 task-dependent `lambda_i` 加权。model exact revision/API date、temperature、hardware、parallelism、
  token/tool/latency/cost、seeds、variance、confidence interval 多数 `Not Disclosed`。
- **Results / Ablations / Sensitivity**：作者在该 contract 下报告 general→personalized/proactive 明显下降，并把
  strongest tested model 的 personalized failure 主要分为 Clarify/Partial、proactive failure 主要分为 Intervention/
  Passive；这些是单模型 error taxonomy，不是所有 Agent 的固定比例。三模型 memory ablation 中 full/RAG 与
  clean/noisy 排名不一致，支持“retrieval interface 取决于 model/workload”，不支持 RAG 普遍优于 full context。
  hybrid judge 只在固定 26 trajectories、四名 human experts 上以 MAE 对照 rule-only；标题虽写 simulator
  sensitivity，正文没有真实用户对 simulator response/accept/reject fidelity 的独立验证。
- **What the Evidence Proves**：在四个 synthetic profiles、作者 tasks/apps、gpt-4o simulator、50-step Android
  environment 和 hybrid judge 下，明确 GUI execution 分数不能预测 personalized/proactive performance；把
  Act、Silent、Stop 分开能暴露 initiative 与 restraint 的不同 operating points；可执行 state check 与 semantic
  rubric 的组合比只看 Agent narrative 更接近完整 outcome evidence。
- **What It Does Not Prove**：不证明被测模型“理解真实用户”，不证明 Claude/Seed/Qwen 的相对排名可跨 API/
  model revision、language、culture、device 或 app ecosystem 保持，不证明 synthetic role/log/simulator 代表真实
  preference formation、consent 或 disagreement，也不证明 hybrid score 等于 trustworthiness。`100% general easy`
  只属于小型明确 slice，不能推出 GUI execution 已普遍解决。
- **Limitations / Threats to Validity**：四个 archetype 容易固化 role stereotypes；profiles/logs/tasks 同源构造，
  可能让 simulator、rubric 与 oracle共享 latent assumptions；同一个 gpt-4o simulator 把 feedback quality 和 model
  capability 耦合；26-trajectory judge calibration 样本小且未报告 disagreement/uncertainty。没有真实用户 consent、
  longitudinal preference drift、conflicting household/organization policy、多用户 authority、malicious history、
  network/service failure、real-device variance 或 production cost/SLO。current repo 与 v1 artifact 又无 tag 锁定。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：live interaction 获得 clarification、initiative、
  restraint 与 executable side-effect evidence，却增加 simulator bias、feedback leakage、role-profile overfit、judge
  correlation、environment flakiness、cost 和 reproducibility burden。Static intent benchmark 继续适合 cheap
  regression；deterministic GUI suite 继续定位 execution failure；human study 对真实 preference/consent validity 仍
  不可替代；full history 在 recall ceiling/历史较小时合理，RAG 在 context/noise 成本较高时合理但可能漏掉关键证据。
- **Evolution Relationship**：`Direct Evolution`：explicit/static intent → noisy-log preference inference → online
  clarification → act/ask/silent policy → post-rejection restraint + executable outcome；`Layering / Dependency`：Ch73
  memory evidence、Ch75 constraint/policy、Ch77 approval state、Ch68 authorization/consent、Ch80 deployment autonomy。
  新 benchmark 扩大 evaluation object，不覆盖便宜、确定的旧 suites。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch61～63、Ch67～69、Ch73、Ch75、Ch77、Ch80。主
  owner 为 Ch62；Ch68/73/75/77/80 作 security、memory、planning、workflow 与 platform handoff。Ch62 已有
  feedback-conditioned trajectory、hidden evaluator state、programmatic outcome、hybrid scorer、failure slices 和
  uncertainty，但尚未明确把 proactive policy 的 false intervention、false passivity 与 post-rejection violation
  分开，也未冻结 `act/ask/silent/stop` 的 opportunity-conditioned metric vector。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后只在 Ch62 精化“autonomy 不是单一 success/safety score”：用 opportunity-conditioned initiative、
  restraint、consent/rejection 与 grounded outcome 共同定义 EvalSpec；Ch68/73/75/77/80 只作短 handoff。不沉淀
  model 排名、具体 error 百分比、四 persona taxonomy 或把 synthetic benchmark 称为用户信任证明。
- **Open Questions**：怎样用真人 paired study 校准 simulator 的 clarification、accept/reject 与 role fidelity？
  Act/Silent/Stop 的 denominator、risk weight 和 cost-sensitive threshold 如何按 deployment harm 定义？如何区分
  preference retrieval miss、clarification policy、constraint composition、GUI execution 与 authorization failure？
  preference/consent 变化怎样 version、withdraw、delete 并在 replay 中保持当时有效的 policy？

### Externalization in LLM Agents: From Context to Memory, Skills, Protocols, and Harnesses — 23/30

- **Candidate / Week / Score**：Externalization in LLM Agents；2026-W15；23/30（Technical Novelty 4、
  System Impact 4、Practical Value 4、Source Reliability 3、Project Relevance 5、Longevity 3），维持 discovery
  score。它把分散于 memory、Skill、protocol 与 harness 的工作整理为统一 systems vocabulary；但属于 narrative
  review，没有系统检索协议、原始实验或可复现 artifact，不能因覆盖面广而提高 Source Reliability。
- **Source Family ID / Type / Date**：`AGENT-EXTERNALIZATION-HARNESS-SYNTHESIS`；arXiv narrative review /
  conceptual systems synthesis。arXiv 只有 v1，2026-04-09 13:19 UTC 首发，归 W15；54 页，CC BY 4.0；
  没有作者代码、dataset、benchmark 或 release。后续引用和工业实现只用于理解 taxonomy，不构成本文结论的
  独立复现。
- **Direct / Related Primary Sources**：直接来源是 arXiv metadata 与 v1 全文。论文综述的 memory、Skill、
  protocol、MCP 与 Agent harness 文献是 related sources；本 packet 不把被综述论文的各自实验结果合并为一个
  跨系统 benchmark，也不把产品文档当作本文理论的独立验证。
- **Access / Full-read Coverage**：已读 metadata、Abstract、Introduction、从 weights→context→harness 的问题
  建模、memory 类型与 architecture、Skill 表示/选择/组合/演化、tool/agent/user protocol、MCP boundary、harness
  loop/permission/sandbox/human oversight/observability、跨模块交互、model I/O 与 failure taxonomy、parametric 与
  externalized trade-off、future directions、Conclusion，以及与核心主张有关的 figures/tables/references。论文没有
  systematic-review search strategy、inclusion/exclusion criteria、原始 implementation、Evaluation、Ablation、
  Limitations 或 Appendix；相应字段明确为 `Not Applicable / Not Disclosed`，不以篇幅替代证据强度。
- **Original Problem / Why the Previous Design Was Reasonable**：model-centric 叙事容易把“Agent 能完成任务”
  全归因于 weights，而忽略 runtime 提供的状态、procedure、action schema 与 control loop。把稳定、通用且需低
  latency 的能力放进 weights 原本合理：它不占 request context，不依赖外部 service，也减少 runtime failure surface；
  把一次性 instruction 放进 prompt 同样简单、可见、易于调试。
- **Changed Constraint / Principle**：long-horizon、动态知识、跨 run 学习、可复用 procedure、异构 tools/agents、
  权限与合规要求，使 weights 更新太慢、prompt 过长且无法独立 version/revoke。论文的长期原则是
  `externalization is a representational transformation`：memory 把 recall 变成 retrieval，Skill 把 improvisation
  变成 procedure composition，protocol 把 ad-hoc interaction 变成 typed contract，harness 把这些 component
  编排成可治理 execution；这不是“所有能力都应搬出模型”。
- **Mechanism**：memory 向模型注入 contextual evidence，Skill 注入 instructional procedure，protocol 约束
  谁能以何种 schema 交换 action/message，harness 则在 loop 中进行 discovery、selection、context assembly、
  execution、observation、permission、monitoring 与 recovery。论文进一步用 representation、acquisition、
  selection、execution、composition、evolution 六个维度比较 components；这些是分析框架，不是一个被实验证明的
  universal architecture。
- **State Ownership / Control and Data Flow**：长期 evidence 由 memory store 及其 provenance/lifecycle owner
  持有；procedure artifact 由 Skill registry/version owner 持有；capability schema 与 session lifecycle 由 protocol
  endpoint/control plane 持有；run state、permission、budget、retry、approval、audit 与 rollback 由 harness/workflow
  持有；model 只消费选择后的 context 并提出 next action。典型 flow 是 observation/evidence → policy-filtered
  memory write → retrieval/Skill selection → bounded context assembly → model proposal → protocol validation/
  authorization → tool execution → observation；任何一步都不能把 model text 自动升级为 authoritative state。
- **Implementation Details**：论文没有实现一个 reference harness，也没有给出 store schema、retrieval index、
  Skill package manifest、protocol transport、sandbox、scheduler 或 recovery code，因此这些均 `Not Disclosed`。
  文中的 component interaction 与 layered diagram只能用作 design vocabulary，不能反推任何具体产品的内部实现。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead**：无原始 benchmark、hardware、model、
  precision、length、batch、concurrency、SLO、seed、variance、baseline、ablation 或 overhead measurement。作者把
  component ablation、cross-model transfer、long-horizon adaptation、governance 与 cognitive overhead measurement
  列为未来研究方向；这恰好说明“外置层带来能力提升”的 causal claim 尚未由本文建立。
- **What the Evidence Proves / Does Not Prove**：它证明一套内部一致、能组织既有文献和系统边界的 taxonomy，
  并使 memory/Skill/protocol/harness 的不同责任可被明确讨论；不证明所有 Agent 架构都收敛到该分层，不证明
  externalization 对质量、成本或安全有净收益，不证明 harness 比 model 是更主要的“智能来源”，也不证明引用
  文献间的不同 benchmark 可以横向比较。
- **Limitations / Threats to Validity**：没有系统综述方法与 evidence grading，选择哪些论文/工业系统可能有
  selection bias；memory、Skill 与 protocol 在实现中常重叠，taxonomy 边界不是物理定律；工业来源会 version
  drift；distributed cognition、operating system 等 analogy 具有解释力但不是 empirical evidence。缺少 poison、
  spoof、permission composition、tenant isolation、delete propagation 与 recovery 的统一实证，使 governance
  结论仍是研究议程。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：externalization 获得 updateability、reuse、
  inspectability、policy enforcement 与 rollback，却增加 retrieval/serialization latency、context contention、
  stale state、provenance loss、Skill poisoning、protocol spoofing、permission confusion、dependency drift 和运维
  成本。稳定/低延迟/generic competence 继续适合 parametric weights；一次性或 request-local constraint 继续适合
  prompt/context；只有需要跨 run 更新、共享、审计、撤销或独立治理的状态才应进入 external component。
- **Evolution Relationship**：`Explanatory Synthesis + Principle Reuse`：weights → context → memory/Skill/
  protocol → harness control plane；`Layering / Dependency`：Ch71 context budget、Ch73 memory provenance、Ch74
  tool authority、Ch77 durable workflow、Ch79 protocol lifecycle、Ch80 platform governance。它不是按时间用
  harness 替代 model，而是揭示不同约束下的共同存在与 ownership 分工。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch71、Ch73、Ch74、Ch77、Ch79、Ch80 及相邻章节。
  主 owner 为 Ch80；Ch71 已把 context 建模为预算资源，Ch73 已覆盖 raw evidence→derived memory 与 provenance/
  supersession/delete，Ch74 已区分 capability schema 与 authorization，Ch77 已覆盖 stateful workflow/replay/
  approval/side effects，Ch79 已覆盖 protocol discovery/invocation/lifecycle，Ch80 已统一 definition、run、context、
  memory、tools、workflow、evaluation、policy、observability、versioned artifact、canary 与 rollback。本文没有形成
  未覆盖且证据更强的新长期机制。
- **Integration Decision**：`No Change — Already Covered (Provisional; Historical Books Gate Closed)`。保留为
  Ch80 的解释性 primary source 与跨章 mapping 证据；不把 taxonomy 重复粘贴进 Books，也不因“外置”叙事改写
  parametric/context 分支。若未来有 component-level causal ablation、跨模型迁移、长期运营、攻击面与 cost/SLO
  对齐证据，再判断是否精化 Ch80 的 partition rule。
- **Open Questions**：怎样以 update rate、latency、context budget、reuse、governance 和 blast radius 定量决定
  一个能力应位于 weights/context/memory/Skill/protocol 的哪一层？跨层 artifact identity 如何 version、trace、
  revoke 与 replay？如何做 component ablation 而不把 model、retriever、Skill selector、tool availability 与 harness
  policy 混为一体？external state 被污染或冲突时，谁拥有 quarantine、supersession、delete 与 rollback？

### SkillClaw: A Skill-Learning Agent Through Collective Experience — 24/30

- **Candidate / Week / Score**：SkillClaw；2026-W15；24/30。全文复核后将 Source Reliability 从 4
  调整为 3、总分由 25 调整为 24：论文和代码公开，但论文标明 work in progress，完整 benchmark
  只报告 6 类中的 4 类代表结果，executor/evolver/validator 使用同一模型，且没有 uncertainty、独立 judge、
  held-out contamination control 或不可变 event-date release。
- **Source Family ID / Type / Date**：`SKILLCLAW-COLLECTIVE-SKILL-EVOLUTION`；arXiv system/method paper +
  author repository。arXiv 只有 v1，2026-04-09 15:38 UTC 首发，归 W15；官方 repository 于 4 月 10 日
  宣布开源，但无 release/tag。04-14 后的 Hermes、04-20 Codex/Claude、04-22 dashboard 与 08-06
  LongHorizon harness 均属 later artifact evolution，不能写成 W15 实现。
- **Direct / Related Primary Sources**：直接来源为 arXiv v1 metadata、24 页 PDF、author repository、
  `evolve_server`、client proxy/session capture、pipeline/storage/engine/validation trees 与 releases page。
  WildClawBench 是论文内 evaluation asset；当前仓库的新增 integration 只能核对实现方向，不能替代 event-time
  snapshot 或独立复现。
- **Access / Full-read Coverage**：已读 Abstract、Introduction、Related Work、architecture、session/evidence
  aggregation、evolution/validation protocol、全部主实验、candidate accept/reject tables、limitations、Conclusion
  及 prompts/history/implementation appendices；并核对 repository README、client/server boundaries、workflow
  与 agent engines、validation/publish modes、tests、commit/release 边界。
- **Original Problem / Previous Design**：user-local Skill、人工 curated registry 和静态 versioned procedure
  易审计、tenant boundary 清楚，适合高风险或稳定 workflow；代价是不同用户反复解决相同失败，反馈不能形成
  shared improvement。直接把所有 trajectory 写进全局 Skill 又会混入偶然步骤、private data、malicious sessions
  与 distribution-specific hacks。
- **Changed Constraint / Principle**：当 Skill 被多用户、不同 session 重复执行，平台可以把 execution evidence
  作为候选改进输入；但“可学习”不等于“可直接发布”。长期原则是将 evidence collection、candidate synthesis、
  validation 与 deployment 分离，并为每一阶段保存 identity、provenance 和 policy decision。
- **Mechanism**：每个 session 记录 prompt、actions/tool calls、feedback、response、referenced skills、tool errors
  与 coarse quality；系统按 referenced Skill 聚合 session group，也保留 no-skill group。Agentic evolver 从成功
  session 提炼 invariants、从失败 session 提炼 correction targets，并选择 refine/create/skip。夜间 validation
  在相同 environment/toolchain 下分别运行 old 与 candidate Skill，由 model judge 比较 task success/stability；
  只有 accepted candidate 合并进 shared pool 并在下一周期同步。
- **State Ownership / Control and Data Flow**：client/proxy 拥有 session capture 与 user/run context；evidence store
  拥有 raw trace、skill reference 和 feedback；evolution pipeline 拥有 candidate 与 source links；validator 拥有
  old/new executions 与 decision evidence；registry/control plane 才能拥有 current version、publish/revoke 与 sync。
  In-flight run 应 pin Skill digest，emergency revoke 可覆盖旧 run。论文未定义 tenant authorization、consent、
  delete propagation、immutable digest、canary 或 rollback，这些不能由“nightly sync”隐式承担。
- **Implementation Details**：论文附录描述 version snapshot 与 evidence file history（如 `vN`、
  `vN_evidence`），并要求修改前阅读历史；current code 分为 local client/proxy、shared storage、optional
  evolve server、workflow/agent engines、candidate validation worker 与 publish mode。当前 52-commit/no-release
  repository 已明显晚于事件窗口，故仅证明架构方向仍存在，不证明论文时点每个 code path 已发布。
- **Evaluation Contract**：WildClawBench 声称 60 个 containerized tasks、6 个 domains、每项 3～27 metrics、
  15～50 steps，并要求 critical errors 为零；论文实际只展示 Social/Search/Creative/Safety 四类。实验持续
  6 天/rounds，模拟 8 个 concurrent users，Qwen3-Max 同时承担执行、evolution 和 validation；hardware、
  model snapshot、sampling、token/tool/cost、seed、variance、confidence interval、独立 judge、privacy/consent
  与 cross-tenant threat model 均 `Not Disclosed`。
- **Results / Ablations / Sensitivity**：作者报告四类分数随 accepted revisions 提升：Social 54.01→60.34、
  Search 22.73→34.55、Creative 11.57→21.80、Safety 24→32；多项 candidate 也被拒绝或进入 plateau。
  `Skill Evolve Lite` 的 30.4→72.5 只来自 3 个 custom queries，不能外推。论文没有跨模型、独立 evaluator、
  held-out user/domain、污染分析、统计区间或真实多租户对照。
- **What the Evidence Proves**：在作者小规模、同模型、模拟多用户、所展示的四类 task contract 下，汇集
  session evidence、生成 candidate、执行 old/new validation 并只发布 accepted revision，可以形成可运行的
  shared Skill improvement loop；reject/plateau 记录也说明候选生成与部署不是同一动作。
- **What It Does Not Prove**：不证明 deployed pool 在 stochastic execution、judge drift、tool/model revision
  或 distribution shift 下单调改进；不证明同模型 self-judge 独立可靠；不证明按 referenced Skill 聚合可正确
  attribution，也不证明 shared Skill 不泄露用户数据、不会被 poisoning、适合跨 tenant 自动同步。
- **Limitations / Threats to Validity**：只展示 benchmark 子集；same-model executor/evolver/validator 形成
  correlated blind spot；training/evolution evidence 与 validation task 可能重叠；“natural ablation”没有控制
  user/environment 差异。缺少 consent、data retention、tenant isolation、malicious feedback、supply-chain、
  rollback、delete propagation 和 longitudinal regression，使“collective”同时成为最大安全边界。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：shared learning 减少重复探索，却新增
  privacy leakage、cross-tenant poisoning、错误 attribution、self-confirmation、version skew、in-flight mismatch、
  stale validation 与 supply-chain propagation。user-local Skill 在隐私/个性化场景仍合理；人工 curated
  allowlist 在高风险行动仍合理；静态 procedure 在约束稳定且需要确定审计时仍合理；raw trace 必须保留为
  evidence，不能被 derived Skill 覆盖。
- **Evolution Relationship**：`Direct Evolution`：manual/user-local Skill → session evidence aggregation →
  candidate synthesis → same-environment validation → controlled shared release；`Layering / Dependency`：Ch73
  procedural memory、Ch62 evaluation、Ch68 privacy/security、Ch77 durable run 与 Ch80 registry rollout。它不是
  “后者替代前者”，而是为可共享场景增加一个需治理的 control loop。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch62、Ch68、Ch73～75、Ch77、Ch79～80。主 owner
  为 Ch80；Ch62/68/73/77 作 evaluator、tenant/privacy、derived-memory provenance 与 run-pinning handoff。
  Ch80 已明确保存 Skill immutable version/digest、publisher/source provenance、evaluation/policy/supersession/
  revocation，并覆盖 canary、in-flight version pin、rollback，以及不得把 trajectory 直接写入 global memory；
  Ch73 已把 derived strategy 定义为可失效、可撤销的 advisory state。论文没有提供更强的新长期机制。
- **Integration Decision**：`No Change — Already Covered (Provisional; Historical Books Gate Closed)`。该论文
  为现有 Ch80 control loop 提供一个 experimental case，但证据弱于书稿现有 governance contract，也未改变
  章节结论；不为制造 diff 重复写入 Books。若未来出现独立 evaluator、真实 multi-tenant、immutable release、
  deletion/rollback 与 longitudinal regression 证据，再评估是否以受限案例精化。
- **Open Questions**：怎样发现“错误 Skill 未被选择”导致的 no-reference failure，而不只按 referenced Skill
  聚合？如何用 tenant-safe/minimized evidence 训练 candidate？validator 怎样与 executor/evolver 解耦并建立
  held-out slices、uncertainty 和 promotion threshold？Skill revoke/delete 怎样传播到 synced clients 与 in-flight
  runs？model/tool/environment revision 后，谁触发全量 revalidation 与 rollback？

### SPPO: Sequence-Level PPO for Long-Horizon Reasoning Tasks — 26/30

- **Candidate / Week / Score**：SPPO；2026-W15；26/30，维持 discovery score（Technical Novelty 5、
  System Impact 5、Practical Value 4、Source Reliability 4、Project Relevance 5、Longevity 3）。
- **Source Family / Type / Revision / Access**：`SPPO-SEQUENCE-LEVEL-SCALAR-CRITIC`；arXiv:2604.08865
  sole v1，2026-04-10 01:58 UTC first-public，ACL 2026 Main/Oral 属 later venue status。已核对论文全文、
  appendix resources/execution commands 与 official repository。repository 是从 `1BIMU/SPPO` fork 的
  verl tree，current main 仅显示 6 commits、无 release/tag；因此 current code 可验证 mechanism entrypoint，
  不能充当 immutable W15 artifact 或证明论文所有 runs 可从同一 commit 重现。
- **Full-read Coverage**：已读 Abstract、Introduction、PPO/GRPO background、sequence-level contextual-
  bandit formulation、scalar Critic/BCE、policy objective、math experiments、all baselines、small-Critic
  comparison、loss ablation、wall-clock/VRAM、value correlation、五个 classic-control RLVR tasks、Related
  Work、Limitations/Risks、GRPO derivation、Critic examples、resource/license table 与 execution appendix；
  并核对 repository 的 run scripts、vendored verl 结构和 `sequence_level_adv` 实现。
- **Original Problem / Why Previous Designs Were Reasonable**：token-state PPO/GAE 在 dense intermediate
  reward 或需要 state-dependent return 时能表达局部 value，且只需每 prompt 一条 rollout；长 CoT 的 sparse
  terminal reward 会让 token-level Critic 学习困难并持有大规模 per-token activation/state。GRPO 不训练
  Critic，以同 prompt 多次 outcome 建立 empirical baseline，对 verifiable task 简单稳健；代价是 group
  rollout、reward evaluation、sequence storage 与 straggler 随 `G` 增长。两者是在 state cost、sampling cost、
  bias/variance 与 attribution granularity 上不同的合理 operating points。
- **Changed Constraint / Mechanism**：SPPO 把 prompt `s_p` 视为 context、整条 response 视为 atomic action，
  Critic 只输出当前 policy 对该 prompt 成功的 scalar probability `V_phi(s_p)`，用 BCE 拟合 binary outcome；
  单次 rollout 的 advantage 为 `A=R-V_phi(s_p)`，再把同一 scalar 广播到所有有效 response tokens，仍使用
  PPO 的 token-level old/current probability ratio 与 clipping。它没有删除 Critic，而是把 Critic 的输入状态
  和 target 从 every-prefix return 降维成 prompt solvability。
- **State Ownership / Control Flow**：rollout policy 拥有 response 与 old token logprobs；verifier 产生
  binary terminal reward；prompt-only Critic 拥有 policy-conditioned solvability estimate、parameters、optimizer
  和 checkpoint；trainer 将 sequence advantage broadcast 到 response mask 并执行 clipped actor update。
  Critic 必须跟随 policy/data distribution 更新，否则 `V(prompt)` 会因 capability drift 变成 stale baseline。
  official code 的 `compute_sequence_level_advantage` 对 reward 求 sequence sum、对 Critic logit 做 sigmoid、
  计算 `R-V` 后按 response mask 广播；loss aggregation 仍是独立 config，因此“与长度解耦”还依赖实际
  token/sequence reduction，不能只由 advantage 公式推出。
- **Evaluation Contract**：DeepSeek-R1-Distill-Qwen-1.5B + DeepScaleR 与 7B + DAPO-Math-17K；AIME24/25、
  AMC23、MATH500、Minerva，evaluation 为 Average@16；baseline 含 PPO、ReMax、RLOO、GRPO `N=8`。
  actor LR `1e-6`、Critic LR `5e-6`、global batch 256/512，standard PPO `gamma=lambda=1`，全部 RL 使用
  boxed-answer `0/1` reward，`beta_KL=0`；1.5B runs 使用 4×A100，7B runs 使用 4×H100。论文另以
  CartPole、MountainCar、Hopper、LunarLander、Pendulum 的 deterministic transition、200/1000 horizon、
  binary terminal success 做受控稀疏奖励实验。
- **Baselines / Ablations / Efficiency Boundary**：PPO+BCE control 仍 collapse，支持收益不只来自 value loss；
  7B policy + 1.5B Critic 是 decoupled-state ablation。作者将 `N=1` 对 `GRPO N=8` 的 wall-clock peak、
  normalized peak VRAM 与 benchmark score报告为效率证据；但 standard PPO/PPO+BCE 因 collapse 在 500 steps
  终止，未披露多 seed、variance/CI、完整 token/optimizer-step matched curves、energy、network、utilization
  或端到端 cost decomposition。`5.9×` 是作者 training-to-peak contract，不是每 token throughput 定律；
  `12.8%` memory reduction 混合了 small Critic 与 verl sharding/memory management，不能外推到任意 runtime。
- **What Evidence Proves / Does Not Prove**：作者实验支持在两种 R1-distill math policies、上述 binary
  verifier 和 4-GPU contracts 中，prompt-only learned baseline 可以用单 rollout 训练并达到与所选 group
  baselines 相近的结果；classic-control testbed 表明 whole-trajectory baseline 不只适用于 token strings。
  它不证明 SPPO 对 open-ended reward、stochastic/partially observed environment、tool/Agent side effects、
  MoE routing、larger models 或 production RL universally better。200 prompts、每题 64 rollouts 的 analysis
  只报告 Pearson/Spearman correlation；Critic predictions 与 empirical difficulty 的分布明显不一致，未提供
  ECE、Brier、reliability curve 或 refresh/staleness sensitivity，不能称为完整 calibration proof。
- **Credit / Theory Boundary**：whole-response policy gradient 本可把 terminal return 作用于所有 sampled
  actions；SPPO 的贡献是 learned prompt baseline + clipped token ratios，不是恢复 token-level causal credit。
  uniform `A` 避开 noisy GAE，却会共同强化成功轨迹中的冗余/错误 tokens，也会共同压低失败轨迹中的有效
  substeps。把 trajectory 称为 atomic action 是有用的 optimization abstraction；在交互环境中实际 action
  仍逐 state 产生，environment transition、partial observation 与 irreversible side effects 并不会因此消失。
- **Trade-offs / New Failure Modes / Previous Design Scope**：SPPO 以少 rollout 换回 Critic state、training、
  version synchronization 与 calibration drift；hard/easy prompt 的 regression-to-mean 会改变 rare outcome
  权重，binary verifier error 会一致传播到全序列。token-state PPO 在 dense/process reward 和局部 value
  可学时仍合理；GRPO 在 Critic 难以跨 policy/version 校准、但 group sampling 可负担时仍合理；RLOO/ReMax
  与 offline DPO 是其他 baseline/data branches。高风险 tool workflow 还需要 step verifier、rollback 和
  side-effect-aware credit，不能只用 final success。
- **Evolution / ROADMAP / Adjacent Chapters**：`token-state Critic + GAE → prompt-only scalar Critic +
  uniform sequence advantage` 是 PPO 内的 `Alternative Granularity`；`learned prompt baseline ↔ group
  empirical baseline` 是 SPPO 与 GRPO 的 `Alternative Branch`，不是新方法覆盖旧方法。已读 Ch28～30；
  主 owner 从 triage 的 Ch29 修正为 Ch28，Ch29 只作 baseline/sample-cost handoff。Ch28 已覆盖 actor/critic/
  rollout lifecycle，Ch29 已覆盖 uniform sequence reward 的 coarse credit；SPPO 新增的是 baseline granularity、
  Critic policy identity/calibration 与 rollout multiplicity 的统一 trade-off。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate
  Closed)`。Gate 通过后可在 Ch28 精化 critic/advantage design space，Ch29 增加短 handoff；不保存作者
  benchmark 排名、固定 hyperparameters、5.9×/12.8% headline，也不把“绕开 temporal attribution”写成
  “解决 reasoning credit assignment”。

### Meta Advanced AI Scaling Framework v2 — 28/30

- **Candidate / Source Family / Date**：`META-AASF-V2-GOVERNANCE`；official 44-page framework +
  Muse Spark 160-page Safety & Preparedness Report；Framework v2 dated 2026-04-07，Muse report 04-08。
  2025 v1 是 predecessor；后续修改只作 revision boundary。
- **Access / Full-read Coverage**：已读 framework 全文、definitions、scope、threat modeling、thresholds、
  evaluation and mitigation process、deployment types、governance/accountability、transparency、incident response、
  appendices/change log；联合读取 Muse report 的 model/system boundary、evaluation setup、Cyber/Chem-Bio/
  Loss-of-Control evidence、scaffold/tool conditions、mitigations、limitations 与 appendices。
- **Problem / Previous Design / Changed Constraint**：单次 model benchmark 或 release review 在能力增长、
  tool/scaffold 变化、开放权重与受控部署并存时无法拥有持续 residual-risk state。早期“到阈值即 stop/release”
  清楚却过于二元；v2 改为 baseline risk → threshold → mitigation → validation → deployment/development decision，
  并把“substantially contribute”及 deployment context 纳入判断。
- **Mechanism / State Ownership / Flow**：threat model 定义 outcome/scenario；capability/uplift/red-team 产生
  assessment；threshold 将 moderate/high/critical 映射到 security/mitigation obligations；safety case 与 mitigation
  validation 形成 residual-risk evidence；named executives 拥有 decision，preparedness report 在 model、tool、
  workflow、modality 等 material change 时刷新。Model evaluator、mitigation owner 与 release authority 不是同一角色。
- **Evaluation Contract / Evidence Boundary**：Muse report 明确评估 model+scaffold+tools，不把模型分数冒充
  deployment autonomy；多数区间使用 bootstrap，但 evaluation-awareness、covert behavior、agentic cyber 与
  autonomous-research tasks 仍受 artificial setting、harness 和 provider-specific judge 影响。报告支持 Meta 在该
  release contract 下如何决策，不证明风险已被独立消除，也不证明这些 threshold 适合其他组织。
- **Trade-offs / Failure Modes / Previous Design Scope**：连续治理提高 traceability，却新增 evaluator gaming、
  hidden threat-model omissions、mitigation drift、内部 owner conflict 与 report freshness。确定性 policy、access
  control、sandbox 和 external audit 继续成立；framework 也不覆盖所有非灾难性 harm 或 unknown unknowns。
- **Evolution / ROADMAP / Decision**：`one-shot model eval → system/deployment-context assessment → residual-risk
  mitigation validation → named release/development decision → material-change refresh` 为 `Direct Evolution`。
  已读 Ch62、Ch67～69、Ch77、Ch80；Ch68 主 owner，Ch62/69/77/80 handoff。`Refine — Existing Argument
  (Version-Grounded Governance Evidence; Historical Books Gate Closed)`；不沉淀厂商 threshold 为通用标准。

### SGLang v0.5.10 — 29/30

- **Candidate / Source Family / Date**：`SGLANG-0.5.10-RUNTIME`；official signed GitHub release，2026-04-06；
  v0.5.10.post1 是 dependency patch，current main 与后续 releases 不倒写 W15。
- **Access / Full-read Coverage**：已读 release highlights、breaking/runtime changes、piecewise CUDA Graph、Elastic
  NIXL-EP、PD staging buffer、scheduler/cache/streaming correctness fixes 与关联 PR entry points；独立 PR 页面
  无法完整访问时只保留 release-level implementation fact。
- **Problem / Previous Design / Changed Constraint**：完整 CUDA Graph 适合静态 execution，却会为复杂控制流
  扩大 capture/memory；MoE EP 以固定 rank/expert ownership 换简单一致性，但单 GPU failure 通常导致全服务
  restart；PD 直接发送分散 GQA head slices 保持 layout，却形成大量细粒度 RDMA requests。
- **Mechanism / State Ownership / Flow**：piecewise graph 将可捕获 segments 与 eager/control-flow boundary 分开；
  Elastic NIXL-EP 在 failure detection 后重建 membership/expert placement 并恢复 dispatch；PD staging 在 source
  GPU 收集 scattered head slices 到 contiguous buffer，再 bulk transfer 到 Decode owner。三者分别由 graph/runtime、
  EP control plane、KV-transfer plane 拥有，不能合并成“更快 serving”。
- **Evaluation Contract / What It Proves**：release 证明功能进入该 tag，并报告 PD request-count 和 selected
  Qwen3.5 topology 的 TPS/GPU improvement；但 model variant、precision、length、batch/concurrency、fabric、
  failure injection、recovery time、p99 与 quality/SLO 条件不完整。数字仅是 version evidence，不是通用性能律。
- **Trade-offs / Failure Modes / Previous Design Scope**：piecewise capture 增加 graph/eager boundary 和 shape
  cache；elastic EP 新增 membership epoch、weight/state redistribution、in-flight request fate 与 degraded-capacity
  semantics；staging buffer 交换 extra copy/memory、lifetime 与 completion ordering。静态 full graph、restart-based
  recovery、直接 slice transfer 在小规模/低故障率/小 slice count 时仍合理。
- **Evolution / ROADMAP / Decision**：`fixed ownership + restart → membership-aware expert redistribution` 与
  `scatter RDMA → contiguous staging → bulk transfer` 是两条 `Direct Evolution`；NIXL、PD、scheduler 为
  `Layering / Dependency`。已读 Ch46、Ch48、Ch51、Ch52；Ch51 主 owner，Ch46/48/52 handoff。
  `Refine — Existing Argument (Version-Grounded Runtime Evidence; Historical Books Gate Closed)`。

### Think in Strokes, Not Pixels — 24/30

- **Candidate / Source Family / Date**：`INTERLEAVED-VISUAL-PROCESS-GENERATION`；arXiv:2604.04746 v1，
  2026-04-06；v2/v3 同周 revision 已核对，不把后发 Meta publication page 当 first-public event。
- **Access / Full-read Coverage**：已读 v1 metadata、related work、data construction、model/objectives、inference、
  GenEval/WISE evaluation、planner/inspector/PARM baselines、ablations、qualitative analysis、conclusion；无独立
  Limitations section，未发现 immutable code/data artifact。
- **Problem / Previous Design / Changed Constraint**：single-pass image generation 简洁、latency 固定，却不给
  system 可验证或修复的 semantic intermediate state；外部 verbal planner/inspector 又可能无法把文字精确映射
  到视觉更新。复杂 compositional prompts 需要 text plan 与 evolving image 相互约束。
- **Mechanism / Flow**：scene graph 生成 contradiction-free incremental targets；每轮产生 textual planning、
  visual draft、textual inspection 与 visual refinement；BAGEL-7B 以 text CE + rectified-flow image MSE 训练统一
  interleaved sequence，并用 instruction-intermediate conflict、image-instruction alignment 及 self-sampled error
  traces监督 correction。model owns proposed trajectory，dataset pipeline owns intermediate labels；最终 truth 仍需
  external evaluator。
- **Evaluation / Boundary**：62K training samples，GenEval/WISE、BAGEL/Janus/PARM 等 baselines，作者报告
  131 cumulative sampling steps/平均 2.62 reasoning steps及多项 ablation；hardware、precision、batch、latency、
  energy、seed/CI、human preference 与 safety/SLO 未披露。Benchmark gains 不能证明 reasoning faithful、
  interpretable，亦不能外推 video/3D 或 interactive editing。
- **Trade-offs / Evolution / Decision**：`one-shot generation → external plan/inspect loop → model-internalized
  interleaved semantic states + correction` 是 `Direct Evolution`，代价是更长 trajectory、intermediate-state
  storage、self-critique bias、error accumulation 与 stop/rollback contract。single pass 在简单 prompt/低延迟时仍
  合理。已读 Ch17/20/23/62/77；Ch77 主 owner。`Refine — Existing Argument (Experimental; Historical Books
  Gate Closed)`。

### FinTrace — 25/30

- **Candidate / Source Family / Date**：`FINTRACE-TRAJECTORY-EVALUATION`；arXiv:2604.10015 v1，2026-04-11；
  v2/v3 的模型清单、训练表述与结果变化只作 revision history，不倒写 W15。
- **Access / Full-read Coverage**：已读 v1 metadata、benchmark construction、800 golden trajectories、九指标
  rubric、13-model testbed、category/reliability analyses、8,196-trajectory training construction、masked SFT/DPO、
  training results、prompts/annotation/tool lists/training appendices与 conclusion。
- **Problem / Previous Design / Changed Constraint**：call-level tool accuracy 和 endpoint success 便宜且可重复，
  但无法分辨“选对工具、却没有利用返回信息”或少调用导致的伪效率。长程金融任务还要求 intent、numerical
  reasoning、cross-source synthesis 和 final answer 同时正确。
- **Mechanism / Ownership / Flow**：query → MCP/FMP tool trajectory → deterministic tool-F1/efficiency/redundancy
  + metric-specific LLM rubric → four-axis aggregate；experts review candidate golden trajectory。Training 将 tool
  responses mask 出 loss，以 SFT 学格式/策略，再用当前 policy rejected rollout 与 reference trajectory 做 DPO。
  Environment owns tool truth，rubric/judge owns semantic verdict，不能由 agent narrative 覆盖。
- **Evaluation / Evidence Boundary**：800 queries、34 categories、247 FMP tools；100-example selection audit 的
  kappa 0.89 只校准该 selection stage。作者实验显示高 tool selection 不保证 information utilization/final answer，
  9B SFT/DPO 改善 intermediate metrics而 final quality 仍低；它不证明某模型跨金融系统优越，也不证明九指标
  等权、LLM judge、gold trajectory 或 FMP coverage 等同真实合规工作流。hardware/cost/latency/SLO 未披露。
- **Trade-offs / Evolution / Decision**：`tool-call accuracy → full trajectory rubric → intermediate supervision +
  final executable/domain outcome` 为 `Direct Evolution`；更多指标提高诊断力，却新增 judge correlation、rubric
  weighting、gold-path bias 与 metric gaming。call-level/schema tests 仍用于局部回归。已读 Ch62、Ch74、Ch77；
  Ch62 主 owner。`Refine — Existing Argument (Experimental; Historical Books Gate Closed)`。

### SinkTrack — 25/30

- **Candidate / Source Family / Date**：`SINKTRACK-CONTEXT-ANCHOR`；arXiv:2604.10027 v1，2026-04-11；
  v2 与 current GitHub 只作 later revision/artifact boundary。
- **Access / Full-read Coverage**：已读 v1 metadata、attention drift/sink motivation、hard/soft injection、dual-track
  method、six-dataset experiment、injection-frequency sensitivity、information-flow analysis、appendix pseudo-code、
  8K+ drift test 与 efficiency discussion；未见完整 production profiling或独立 limitations section。
- **Problem / Previous Design / Changed Constraint**：保持原模型不变最稳健；hard-replace BOS value 会破坏
  pretrained flow，soft mean-pool fusion依赖手调 alpha 且压缩长上下文。生成变长后需要一个持续可见、又不让
  所有 token 改走新 attention 的 context anchor。
- **Mechanism / State Ownership / Flow**：在每隔五层的指定 injection layer，将 BOS query 对完整 external
  context K/V 做 cross-attention；其余 tokens 保持原 causal self-attention，再拼接输出。更新后的 BOS K/V 可进入
  cache并被后续 tokens关注。模型/runtime共同拥有 injection-layer policy、source context identity、BOS cache state
  与 fallback；source change 必须使 cache失效。
- **Evaluation / Evidence Boundary**：Qwen2.5/MiniCPM3/Llama3.1 与 Qwen2.5-VL/Gemma3，3B～12B；QuAC、
  SQuAD2.0、RealWorldQA、MMStar、M3CoT、POPE，对比 Direct/CoT并做频率/schedule分析。结果支持作者设置下
  anchoring改善 selected QA/hallucination proxy；attention correlation/L1 norm 是机制 proxy，不证明 causal
  faithfulness。hardware、precision、batch/concurrency、kernel overhead、TTFT/TPOT/p99 与 SLO 未披露。
- **Trade-offs / Evolution / Decision**：`passive sink → hard anchor → soft static fusion → adaptive dual-track anchor`
  为 `Direct Evolution`。新增 cross-attention/source storage、graph/kernel incompatibility、stale anchor、malicious
  context amplification 与 shared-prefix identity。原生 long-context、RAG、sliding attention 及无注入路径仍成立。
  已读 Ch22、Ch39～42、Ch45；Ch22 主 owner。`Refine — Existing Argument (Experimental; Historical Books
  Gate Closed)`。

### CodeComp — 28/30

- **Candidate / Source Family / Date**：`CODECOMP-STRUCTURAL-KV-COMPRESSION`；arXiv:2604.10235 sole v1，
  2026-04-11；paper 声明 SGLang integration，但未定位公开 author repository/release。
- **Access / Full-read Coverage**：已读 metadata、related work、query-conditioned retrieval、Joern CPG feature
  extraction、structure-aware allocation、span protection、layer-wise compression、SWE-bench Lite/LCA setup、
  baselines、retention sensitivity、component/feature ablations、generation/latency analysis、appendix；无独立
  Limitations section。
- **Problem / Previous Design / Changed Constraint**：attention-only eviction 对自然语言合理，因为 attention 是
  token utility proxy；代码中的 call site、branch、return 与 assignment 可能当前 attention 低，却决定跨文件
  control/data dependency。Agentic coding 又让 repo context 超过 KV capacity。
- **Mechanism / Ownership / Flow**：query perplexity selects chunks；Joern CPG 提取 call/control/return/assignment
  及 CFG/PDG；structure score 给 chunk 分配 KV budget，structural spans 先保留，剩余容量再由 attention score
  填充；每层独立压缩并保持 position handling。Static analyzer owns structural prior，runtime owns per-layer
  retained KV/block mapping；parser/language revision必须进入 cache-policy identity。
- **Evaluation / Evidence Boundary**：bug localization与 patch generation，Llama3/Qwen3/DeepSeek/Qwen coder，
  retention 0.2/0.4/0.6；span protection 是主要增益，allocation较小，call/control features贡献明显。32B
  generation latency约 112～118 秒只绑定作者 task，hardware、precision、batch/concurrency、SLO 与 preprocessing
  成本未完整披露；没有 production scheduler、prefix sharing、tail latency 或独立 artifact evidence。
- **Trade-offs / Evolution / Decision**：`attention-only token eviction → semantic chunk selection → structural-prior
  capacity allocation + span floor → attention residual fill` 为 `Direct Evolution`；代价是 parser/language coverage、
  analysis latency、stale graph、generated/dynamic code blind spot 与 block fragmentation。attention-only、local window、
  no-compression 在非代码、unsupported language或 strict correctness时仍合理。已读 Ch22、Ch40～43、Ch46/47、
  Ch77；Ch41 主 owner。`Refine — Existing Argument (Experimental; Historical Books Gate Closed)`。

### Seeduplex full-duplex speech LLM — 24/30

- **Source Family ID / Type / Date**：`SEEDUPLEX-FULL-DUPLEX-VOICE`；ByteDance Seed 官方技术
  发布与 project page，2026-04-09；未发现独立论文或可复现 artifact。
- **Full-read Coverage**：已读 architecture/training 的公开范围、continuous listening、interference
  suppression、semantic endpointing、deployment claims 和 evaluation 描述；具体模型结构、
  audio tokenization、hardware、并发、p95/p99 latency 与 SLO 为 `Not Disclosed`。
- **Problem / Previous Design / Changed Constraint**：half-duplex 把 turn boundary 明确化，易于
  scheduling、cancellation 和回声隔离；自然对话包含 overlap、pause、barge-in 与 background
  speech，使单向 state machine 暴露 premature response 和 false interruption。
- **Mechanism / Ownership / Flow**：官方只确认“listen while speaking”、speech+semantic endpoint
  判断和干扰抑制；authoritative turn state 必须协调 input stream、output playback、barge-in、
  tool call 与 cancellation。内部网络与训练机制不得从 demo 反推。
- **Evaluation Boundary**：官方报告 false response/interruption 减半、premature response 降低
  40%、human-likeness +8% 和大规模 app rollout；缺少 dataset、denominator、hardware、load、
  confidence interval 与独立复现，数字仅属厂商 workload。
- **Trade-offs / Evolution**：full-duplex 获得低等待和自然节奏，却新增 echo/overlap ambiguity、
  partial-output commit、tool rollback、resource concurrency 与隐私采集；half-duplex 在高确定性、
  低成本和 transactional tool flow 中仍合理。关系为 `Direct Evolution` 于 runtime state machine。
- **ROADMAP / Chapters / Decision**：已读 Ch38～40、Ch74、Ch77；`Emerging / Experimental`。
  机制尚未达到修改 Books 的跨来源门槛。

### Muse Spark — 19/30

- **Source / Date / Verification**：Meta 2026-04-08 官方发布已核对；模型/产品状态成立，端到端
  机制和跨 workload 系统合同不足。
- **Score / Decision**：19/30 维持；`Weekly Only — Version/Product Fact`。

### Academic agents — 18/30

- **Source / Verification**：Google Research 2026-04-08 官方 research entry 已核对；该条目属于
  academic-task Agent 的应用/研究状态，不与次日 user-simulator 工作共享机制或评测合同。
- **Score / Decision**：18/30；`Weekly Only — Version/Product Fact`。当前材料没有补全 Agent
  runtime 的 state ownership、tool authority、failure recovery 或可迁移 evaluation contract。

### ConvApparel user simulator — 17/30

- **Source / Verification**：Google Research 2026-04-09 官方 research entry 已核对；它研究的是
  apparel/commerce 场景的 user simulation，不是 academic Agent 的后续版本。
- **Score / Decision**：17/30；`Weekly Only — Domain Evaluation Fact`。domain simulator 可作为
  evaluation component，但旧版材料未提供足以改变 Ch62/77 的通用机制、跨域外推或 production
  runtime contract。

### Microsoft New Future of Work 2026 page — 19/30

- **Source / Date / Verification**：Microsoft Research Blog，2026-04-09；页面联合汇总既有大规模分析、field/lab
  studies 与 theory，链接标题仍称 `New Future of Work Report 2025`，不是一项新的 2026 mechanism paper。
- **Evidence Boundary**：它支持“AI adoption、productivity、collaboration 与 expertise effects 分布不均、单一
  productivity proxy 不可靠”的 research synthesis；不同引用研究的 population、method、time window 与 causal
  strength不同，不能把汇总百分比当统一实验或 AI System design proof。
- **Score / ROADMAP / Decision**：19/30；Ch62/77 background only；`Weekly Only — Research Synthesis / No New
  System Mechanism`。不进入 Books，也不把社会观察替代 model/runtime/Agent primary evidence。

### TensorRT-LLM v1.3.0rc11 — 18/30 boundary verification

- **Source Family / Event Boundary**：`TENSORRT-LLM-1.3-RC-SERIES`；NVIDIA/TensorRT-LLM official GitHub
  pre-release，tag `v1.3.0rc11`，2026-04-09。它属于 release-candidate series，不是 stable GA，也不与
  SGLang v0.5.10 共享机制身份。
- **What the Evidence Proves / Does Not Prove**：official release surface 只证明该 RC 在本周形成版本节点，
  并提供当时的 candidate feature/fix inventory；它不证明这些功能已经稳定、默认启用、跨 backend 可用，
  也没有完整 model、hardware、precision、input/output length、batch、concurrency、topology 与 SLO contract。
  后续 RC 或 stable release 的行为不得倒写成本周事实。
- **Evolution / ROADMAP / Disposition**：`development branch -> release candidate -> stable release -> production
  adoption` 是 version maturity chain，不是新的系统机制演进。18/30；`Weekly Only — Pre-release Boundary / No
  Books Change`。若后续 stable family 披露独立 mechanism、code path 和 evaluation contract，由其 event week
  重新拥有。

## Repository Changes

- W15 从 4 个 baseline families 扩展为 31 个 scored families：26 个 `20+` families 与 5 个低分
  boundary。TriAttention、MIA、SkillX、PTE、Agentic Skills、MARS、Sol-RL、Flux Attention、SkillClaw、DMax、
  Externalization、KnowU-Bench、SPPO、AASF v2、SGLang v0.5.10、Think in Strokes、FinTrace、SinkTrack、
  CodeComp、PRA、BERTJudge、ManyIH、SCOPE 与 Tracing the Roots 均完成非模板化 Full Source Review；
  GameWorld 只完成 metadata/project/repository boundary review，因 primary PDF full read unavailable 转入
  `Unverified / Blocked Backlog`。TensorRT-LLM `v1.3.0rc11` 新增为 18 分 pre-release boundary。
- SkVM 已按 arXiv v1 的 4 月 3 日回拨 W14；MegaTrain、RAGEN-2 与 MolmoWeb 分别按更早 primary event
  归 W14、W11 与 W13。W15 当前为 31 scored（19 high / 7 medium / 5 low）、25/25 accessible `20+`
  Full Source Reviews、1 blocked、5/5 low-score boundaries、0 current-review pending。academic 和 accessible
  fixed Infra checkpoint 通过；全历史 Evidence Gate 与 Books Gate 仍关闭。本轮没有修改历史 Daily 或 Books。
- 2026-08-13 ledger review：31 scored（19 high / 7 mid / 5 low）、25/25 accessible `20+` reviews、
  5/5 low-score boundaries、1 GameWorld blocker、0 ordinary pending 再次对账；GameWorld 未被误计为全文
  或 Books-ready evidence。W15 checkpoints 保持 Passed，backlog cursor 进入 W16；未修改 Books。

## Open Questions

1. full-duplex Agent 的 authoritative turn state、barge-in commit 与 tool cancellation 由谁管理？
2. Google academic-agent 与 ConvApparel 分别对应哪一篇 direct primary paper、revision history
   和完整 evaluation contract？当前只核对 official research entries，direct paper URL 仍待补齐。
3. 同周是否存在 speech runtime、streaming inference、audio tokenization 或 realtime serving 的
   arXiv/engineering 事件，能与 Seeduplex 形成跨来源机制链？
4. 动态历史分页或后续 cross-week lineage 是否会暴露本次 fixed official/Infra checkpoint 未召回的候选？
5. TriAttention 的 calibration identity、paged-block eviction 与 prefix-sharing correctness 应怎样
   进入同一 runtime contract？
6. MIA 的 memory-unit deletion 怎样传播到 Planner weights？online update 的 model revision、并发
   request isolation、rollback 与 judge-poisoning gate 应由谁拥有？
7. SkillX 的 merge/filter 怎样保存 source provenance、schema version、selective deletion 与 rollback？
   相同 compute/tool-call budget 下，不同 base model 应怎样选择 skill granularity，而不是默认全层注入？
8. PTE 怎样纳入 partial KV hit、TTL、prefix identity、batch/scheduler、quantization 与 actual utilization；
   tool/network/model generation 应保留 cost vector 还是折成一个单位，proxy residual 何时触发 recalibration？
9. Skill evaluation 怎样在相同 model/harness/tool/timeout/cost 下隔离 selection、retrieval、adaptation 与
   refinement；何时应 no-skill/fail-closed，derived task-local Skill 又怎样 version、revoke 和 delete？
10. MARS 的 confidence calibration 如何跨 sampling policy、domain、length、adapter 与 quantization 保持；
    cursor-based cache 若取消 batch barrier，怎样原子提交 KV、accepted tokens 与 stream？在 matched SLO、
    concurrency、training amortization 和 energy 下，它何时真正优于 exact speculative decoding？
11. Sol-RL 的 FP4 proxy rank 怎样随 policy/reward-model/solver drift 在线校准？不可 deterministic replay 的 LLM/
    Agent trajectory 能否用 high-fidelity re-evaluation 或 importance correction 复用这一分层原则，而不伪造
    on-policy identity？
12. Flux Attention 的 route vector 怎样纳入 model/prefix/KV identity？当 prompt 中途加入 tool result、长生成
    改变 retrieval demand 或 mixed-route batch 破坏 kernel regularity 时，谁触发 dense fallback、re-route、KV
    rebuild 与 fairness correction？
13. SkillClaw 怎样处理未选中正确 Skill 的 attribution blind spot？shared evidence 如何执行 consent、tenant
    isolation、poisoning defense 与 deletion？独立 validator、held-out slices、in-flight pin、revoke/rollback 和
    model/tool revision revalidation 应由哪个 control-plane object 负责？
14. DMax 的 hybrid revision state 怎样与 KV/cache、CUDA Graph、continuous batching 和 stream commit 对齐？
    convergence oscillation、max iteration、deadline/cancellation 与 state rollback 谁负责？在 matched quality、
    TTFT/TPOT/p99/goodput、energy 和 training amortization 下何时胜过 AR/speculative branch？
15. weights、context、memory、Skill 与 protocol 的 placement 能否由 update rate、latency、reuse、governance、
    context cost 和 blast radius 共同决定？跨层 artifact identity、causal ablation 与 poison rollback 怎样实现？
16. interactive personalization/proactivity benchmark 怎样用真人研究校准 simulator fidelity，并把 Act、Silent、
    Stop 的 denominator、harm weight、consent revision 与 false-intervention cost 绑定真实 deployment policy？
17. prompt-only Critic 应以什么 policy-version、refresh cadence、ECE/Brier/reliability slice 校准？当 policy
    capability、verifier 或 task mixture 漂移时，怎样检测 stale baseline？uniform sequence advantage 与实际
    loss reduction 如何共同控制 response-length weighting，何时必须恢复 process/step credit？
18. GameWorld 23 页 primary PDF 恢复可读后，implementation、evaluation setup、limitations 与 appendix
    是否会改变当前 provisional score、owner 或 failure taxonomy？在此之前不得把 metadata/artifact packet
    升格为 Full Source Review。
19. Elastic EP 的 membership epoch、in-flight request fate、degraded capacity 与 weight redistribution 如何形成
    可恢复 contract？PD staging 的 extra copy 何时被 RDMA request-count reduction 抵消？
20. BOS anchor 的 source/cache identity 与 malicious-context amplification 怎样测；CodeComp 的 static-analysis
    latency、language coverage、graph freshness 与 block fragmentation 如何进入 production EvalSpec？
21. FinTrace 的九指标权重、judge disagreement 与 executable financial correctness 如何联合；interleaved visual
    trajectory 的 stop/rollback 和 human-edit semantics 怎样与 generic Workflow 对齐？

## Sources

- ByteDance Seed, “Introducing Seed Full-Duplex Speech LLM,” published 2026-04-09:
  https://seed.bytedance.com/en/blog/introducing-seed-full-duplex-speech-llm-attentive-listening-robust-interference-suppression-enabling-more-natural-interaction
- Google Research April 2026 archive: https://research.google/blog/2026/04/
- Meta AI, “Introducing Muse Spark,” published 2026-04-08:
  https://ai.meta.com/blog/introducing-muse-spark-msl/
- Meta Advanced AI Scaling Framework v2, published 2026-04-07:
  https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2
- Meta Muse Spark Safety & Preparedness Report, published 2026-04-08:
  https://ai.meta.com/static-resource/muse-spark-safety-and-preparedness-report/
- Microsoft Research, “New Future of Work,” published 2026-04-09:
  https://www.microsoft.com/en-us/research/blog/new-future-of-work-ai-is-driving-rapid-change-uneven-benefits/
- SGLang v0.5.10 official release, published 2026-04-06:
  https://github.com/sgl-project/sglang/releases/tag/v0.5.10
- Think in Strokes abstract/revision history: https://arxiv.org/abs/2604.04746
- Think in Strokes v1 HTML: https://arxiv.org/html/2604.04746v1
- FinTrace abstract/revision history: https://arxiv.org/abs/2604.10015
- FinTrace v1 HTML: https://arxiv.org/html/2604.10015v1
- SinkTrack abstract/revision history: https://arxiv.org/abs/2604.10027
- SinkTrack v1 HTML: https://arxiv.org/html/2604.10027v1
- SinkTrack author repository: https://github.com/67L1/SinkTrack
- CodeComp abstract/revision history: https://arxiv.org/abs/2604.10235
- CodeComp v1 HTML: https://arxiv.org/html/2604.10235v1
- GameWorld abstract and revision history: https://arxiv.org/abs/2604.07429
- GameWorld official project page: https://gameworld-bench.github.io/
- GameWorld author repository: https://github.com/gameworld-bench/GameWorld
- Process Reward Agents abstract and revision history: https://arxiv.org/abs/2604.09482
- Process Reward Agents v1 HTML: https://arxiv.org/html/2604.09482v1
- BERT-as-a-Judge abstract and revision history: https://arxiv.org/abs/2604.09497
- BERT-as-a-Judge v1 PDF: https://arxiv.org/pdf/2604.09497v1
- Many-Tier Instruction Hierarchy abstract and revision history: https://arxiv.org/abs/2604.09443
- Many-Tier Instruction Hierarchy v1 HTML: https://arxiv.org/html/2604.09443v1
- SCOPE abstract and revision history: https://arxiv.org/abs/2604.10688
- SCOPE v1 HTML: https://arxiv.org/html/2604.10688v1
- Tracing the Roots abstract and revision history: https://arxiv.org/abs/2604.10480
- Tracing the Roots v1 HTML: https://arxiv.org/html/2604.10480v1
- TensorRT-LLM v1.3.0rc11 official pre-release, published 2026-04-09:
  https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0rc11
- Hugging Face Daily Papers, 2026-04-06: https://huggingface.co/papers/date/2026-04-06
- Hugging Face Daily Papers, 2026-04-07: https://huggingface.co/papers/date/2026-04-07
- Hugging Face Daily Papers, 2026-04-08: https://huggingface.co/papers/date/2026-04-08
- Hugging Face Daily Papers, 2026-04-09: https://huggingface.co/papers/date/2026-04-09
- Hugging Face Daily Papers, 2026-04-10: https://huggingface.co/papers/date/2026-04-10
- TriAttention abstract/revision: https://arxiv.org/abs/2604.04921
- TriAttention v1 HTML: https://arxiv.org/html/2604.04921v1
- TriAttention author code: https://github.com/WeianMao/triattention
- Memory Intelligence Agent abstract/revision: https://arxiv.org/abs/2604.04503
- Memory Intelligence Agent v1 HTML: https://arxiv.org/html/2604.04503v1
- Memory Intelligence Agent v4 HTML (later revision boundary): https://arxiv.org/html/2604.04503v4
- Memory Intelligence Agent author repository: https://github.com/ECNU-SII/MIA
- Memory Intelligence Agent model artifact: https://huggingface.co/LightningCreeper/MIA
- Memory Intelligence Agent dataset artifact: https://huggingface.co/datasets/LightningCreeper/MIA
- SkillX abstract/revision: https://arxiv.org/abs/2604.04804
- SkillX v1 HTML: https://arxiv.org/html/2604.04804v1
- SkillX v2 HTML (later revision boundary): https://arxiv.org/html/2604.04804v2
- SkillX author repository and SkillKB: https://github.com/zjunlp/SkillX
- MegaTrain author release (W14 owner boundary):
  https://mastergodzilla.github.io/posts/2026/04/megatrain/
- MegaTrain arXiv v1 (submitted 2026-04-06; W14 Source Family): https://arxiv.org/abs/2604.05091
- Beyond Accuracy / PTE abstract and revision history: https://arxiv.org/abs/2604.05404
- Beyond Accuracy / PTE v1 HTML: https://arxiv.org/html/2604.05404v1
- Beyond Accuracy / PTE author repository: https://github.com/sqs-ustc/tool-reasoning-framework-PTE
- Beyond Accuracy ACL 2026 final record (later publication boundary):
  https://aclanthology.org/2026.acl-long.339/
- Agentic Skills in the Wild abstract and sole-v1 history: https://arxiv.org/abs/2604.04323
- Agentic Skills in the Wild v1 HTML: https://arxiv.org/html/2604.04323v1
- Agentic Skills in the Wild author code: https://github.com/UCSB-NLP-Chang/Skill-Usage
- Agentic Skills in the Wild public data/artifacts: https://huggingface.co/datasets/Shiyu-Lab/Skill-Usage
- Agentic Skills in the Wild release boundary: https://github.com/UCSB-NLP-Chang/Skill-Usage/releases
- RAGEN-2 official 2026-03-12 release / W11 owner boundary: https://github.com/mll-lab-nu/RAGEN
- RAGEN-2 arXiv v1 (later 2026-04-07 formal source): https://arxiv.org/abs/2604.06268
- MARS abstract and sole-v1 history: https://arxiv.org/abs/2604.07023
- MARS v1 HTML: https://arxiv.org/html/2604.07023v1
- MARS author implementation: https://github.com/Xalp/MARS
- MARS release boundary: https://github.com/Xalp/MARS/releases
- FP4 Explore, BF16 Train abstract and sole-v1 history: https://arxiv.org/abs/2604.06916
- FP4 Explore, BF16 Train v1 HTML: https://arxiv.org/html/2604.06916v1
- Sol-RL project page: https://nvlabs.github.io/Sana/Sol-RL/
- Sol-RL training documentation: https://nvlabs.github.io/Sana/docs/sol_rl/
- Sol-RL current implementation / release boundary: https://github.com/NVlabs/Sana
- SkillClaw abstract and sole-v1 history: https://arxiv.org/abs/2604.08377
- SkillClaw v1 PDF: https://arxiv.org/pdf/2604.08377
- SkillClaw author repository: https://github.com/AMAP-ML/SkillClaw
- SkillClaw release boundary: https://github.com/AMAP-ML/SkillClaw/releases
- DMax abstract and v1/v2/v3 history: https://arxiv.org/abs/2604.08302
- DMax v1 HTML: https://arxiv.org/html/2604.08302v1
- DMax author repository: https://github.com/czg1225/DMax
- DMax release boundary: https://github.com/czg1225/DMax/releases
- DMax Math model card: https://huggingface.co/Zigeng/DMax-Math-16B
- DMax Coder model card: https://huggingface.co/Zigeng/DMax-Coder-16B
- DMax Math self-distillation dataset: https://huggingface.co/datasets/Zigeng/DMax-LLaDA-2.0-Mini-Math-Trajectories
- DMax Code self-distillation dataset: https://huggingface.co/datasets/Zigeng/DMax-LLaDA-2.0-Mini-Code-Trajectories
- Externalization in LLM Agents abstract and sole-v1 history: https://arxiv.org/abs/2604.08224
- Externalization in LLM Agents v1 HTML: https://arxiv.org/html/2604.08224v1
- KnowU-Bench abstract and sole-v1 history: https://arxiv.org/abs/2604.08455
- KnowU-Bench v1 HTML: https://arxiv.org/html/2604.08455v1
- KnowU-Bench official project: https://zju-real.github.io/KnowU-Bench/
- KnowU-Bench author repository: https://github.com/ZJU-REAL/KnowU-Bench
- MolmoWeb: https://arxiv.org/abs/2604.08516
- SPPO abstract and sole-v1 history: https://arxiv.org/abs/2604.08865
- SPPO v1 full HTML and appendices: https://arxiv.org/html/2604.08865v1
- SPPO official implementation, current fork/release boundary: https://github.com/sustech-nlp/SPPO
- Flux Attention abstract and sole-v1 history: https://arxiv.org/abs/2604.07394
- Flux Attention v1 HTML: https://arxiv.org/html/2604.07394v1
- Flux Attention author implementation: https://github.com/qqtang-code/FluxAttention
- Flux Attention sparse-kernel dependency: https://github.com/mit-han-lab/Block-Sparse-Attention
- W16 second-pass attribution ledger（七个 blocked W15 identities 的本地发现来源）：
  ../2026-W16/README.md

## 2026-08-14 Final Books Integration Ledger — 31/31

| Candidate / Source Family | Score | Stable Owner | Current / Legacy | Final Disposition | Chapter-level Review Evidence |
| --- | ---: | --- | --- | --- | --- |
| Seeduplex full-duplex speech LLM | 24 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Emerging / Experimental — Weekly Only | full-duplex interruption/overlap 有系统价值，但公开机制、runtime artifact 与 SLO 不足以写长期正文 |
| Muse Spark | 19 | N/A | N/A | Weekly Only — Low Score | 模型发布事实，不形成独立系统机制 |
| Academic agents | 18 | N/A | N/A | Weekly Only — Low Score | 研究案例缺少可迁移机制证据 |
| ConvApparel user simulator | 17 | N/A | N/A | Weekly Only — Low Score | domain simulator case，不改变 Evaluation contract |
| TriAttention | 28 | `INFER-KV-CACHE` | Ch45 / Ch41 | Refine — Existing Argument / Experimental | 新增 pre-RoPE calibration、周期 eviction 与 model/prefix/block identity |
| Memory Intelligence Agent | 24 | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — Existing Argument / Experimental | 分离 external procedural memory 与不可逆 Planner weight update、delete/rollback boundary |
| SkillX | 24 | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — Existing Argument / Experimental | 把 hierarchy 定位为 pseudo-plan retrieval plan，而非固定三级 taxonomy |
| Prefill Token Equivalents | 26 | `PLATFORM-COST` | Ch70 / Ch66 | Refine — Existing Argument / Experimental | 将 tool trajectory 折算为 cache/context-dependent work，同时保留 measured time/SLO |
| Agentic Skills in the Wild | 25 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | EvalSpec 覆盖 oracle→selection→retrieval→adaptation，不把 curated Skill 当真实 pipeline |
| MARS | 26 | `INFER-SPECULATIVE-DECODING` | Ch48 / Ch44 | Refine — Existing Argument / Experimental | 同一 AR backbone masked proposals 仍需 acceptance、ordered commit 与 KV lifecycle |
| FP4 Explore, BF16 Train | 27 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | low-fidelity exploration 与 objective-compatible high-fidelity artifact 重建分层 |
| SkillClaw | 24 | `AGENT-PLATFORM` | Ch84 / Ch80 | No Change — Already Covered | session evidence→candidate Skill→validation→rollout 已由 Skill compilation/release contracts 覆盖 |
| DMax | 25 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Refine — Existing Argument / Experimental | self-generated noisy state→revision→commit，绑定 matched training 与 rollback boundary |
| Externalization in LLM Agents | 23 | `AGENT-PLATFORM` | Ch84 / Ch80 | No Change — Already Covered | Context/Memory/Skill/Protocol/Harness ownership、cost 与 governance 已分章覆盖 |
| KnowU-Bench | 24 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | 主动性拆为 Act/Silent/Stop operating points 与 hybrid verifier |
| Flux Attention | 26 | `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | Refine — Existing Argument / Experimental | route granularity 与 execution granularity、KV retention/cache identity 联合版本化 |
| SPPO | 26 | `TRAIN-PPO` | Ch32 / Ch28 | Refine — Existing Argument / Experimental | prompt-only Critic 作为 token Critic 与 group empirical baseline 的中间分支 |
| Meta Advanced AI Scaling Framework v2 | 28 | `PLATFORM-SECURITY` | Ch72 / Ch68 | Refine — Existing Argument / Version-Grounded | capability→deployment controls→mitigation validation→residual-risk owner/refresh loop |
| SGLang v0.5.10 | 29 | `INFER-SGLANG` | Ch51 / Ch47 | Refine — Existing Argument / Version-Grounded | piecewise graph、elastic EP 与 PD staging 分别归 execution/recovery/transfer ownership |
| Think in Strokes | 24 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Refine — Existing Argument / Experimental | one-shot→plan/draft/inspect/refine intermediate-state workflow，保留 one-shot 分支 |
| FinTrace | 25 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | tool component→information use/process→domain outcome evidence ladder |
| SinkTrack | 25 | `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | Refine — Existing Argument / Experimental | passive sink→dual-track context anchor，并新增 source/cache identity 与 attack surface |
| CodeComp | 28 | `INFER-KV-CACHE` | Ch45 / Ch41 | Refine — Existing Argument / Experimental | query-conditioned chunk retrieval + code structural prior + protected-span budget |
| Microsoft New Future of Work page | 19 | N/A | N/A | Weekly Only — Research Synthesis | 多研究综合页，不是新的 primary mechanism |
| GameWorld | 27 | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | Unverified / Blocked / No Books Change | identity/project 可定位，但完整 primary text 未完成审计；禁止从摘要反推机制 |
| Process Reward Agents | 28 | `INFER-SCHEDULING` | Ch56 / Ch52 | Refine — Existing Argument / Experimental | inference-time guidance 作为 request-scoped resource，绑定 call budget、freshness 与 SLO |
| BERT-as-a-Judge | 26 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — Already Covered | reference scorer、learned judge、calibration 与 human/executable escalation ladder 已覆盖 |
| Many-Tier Instruction Hierarchy | 27 | `PLATFORM-SECURITY` | Ch72 / Ch68 | Refine — Existing Argument / Experimental | role priority 扩展为 authenticated principal/scope/channel/delegation provenance |
| SCOPE | 27 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | outcome-routed correct/incorrect branches 与 group-calibrated sample weighting |
| Tracing the Roots | 27 | `TRAIN-DATA` | Ch27 / Ch23 | Refine — Existing Argument / Experimental | sample hash→artifact identity→typed derivation graph→contamination/delete propagation |
| TensorRT-LLM v1.3.0rc11 | 18 | N/A | N/A | Weekly Only — Pre-release Boundary | RC availability 不证明稳定 runtime contract |

### W15 Gate Result

- Scored candidates: `31/31` final disposition。
- Accessible scored `20+`: `25/25`；`21 Refine + 3 No Change + 1 Emerging`。
- Scored blocked: GameWorld `1 Unverified / Blocked / No Books Change`。
- Low-score/pre-release: `5/5 Weekly Only`。
- Owner chapters changed: 13 Stable Nodes；没有新增 Part、章节或孤立论文笔记。
- Source-Family Books Gate: `Complete`；Archive Completion Gate: `Open`。

Repository changes: Ch22、Ch24、Ch27、Ch32～33、Ch45、Ch48、Ch51、Ch56、Ch66、Ch70、Ch72、Ch77。
GameWorld、Seeduplex、三个 No Change families 与五个低分/版本边界没有被强行写入机制正文。
