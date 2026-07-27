# AI Research Weekly — 2026-W14

> Coverage Window: 2026-03-30～2026-04-05
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: 27/27 scored candidate families have final Books dispositions; 26/26 scored `20+` Full Source Reviews complete; 1/1 low-score boundary complete; 2 unscored identities remain `Unverified / Blocked / No Books Change`; W14 Source-Family Books Gate Complete; academic cross-index and remaining Infra release coverage keep Archive Completion Gate Open

> **Supersession boundary (2026-08-14):** 本文较早段落中的 `Books pending`、`provisional`、
> `Blocked — Not Started` 与 `Historical Books Gate Closed` 是 Source Review 阶段快照；它们不被删除，
> 但全部由文末 27/27 Final Books Integration Ledger 取代。两个 identity blocker 只保持 Archive Gate Open。

## Executive Summary

旧版 W14 只保留两项 Google Research。本轮按 arXiv first-public date 重放 2026-03-30～04-03
学术窗口，首轮恢复 14 个候选。继续重放 4 月 6～7 日推荐流后，又发现 5 个实际于 4 月 2～4 日
首发的 curation-lag 候选并回写 W14；另把 23 个实际属于更早 ISO week 的条目显式移出。
随后又从后续推荐流回收 4 月 5 日首发的 Combee，以及 4 月 3 日首发、不能误归 W17 的
Stochastic KV Routing。当前共记录 23 个候选，而不是把
推荐页日期误当论文事件日期。

2026-08-12 fixed-source 回放又恢复 Amazon Science 4 月 1 日的 LLM-based TTS 工程研究。它把
autoregressive acoustic-token generation 的 hallucination / truncation 问题，从“只调 sampling”推进为
`phoneme/duration plan -> generation -> post-generation checks -> regenerate/fallback` 的控制流，并让
计划状态同时承担 guardrail 与 debug surface。可是公开证据只有官方工程文章，没有 technical report、
model card、代码、数据/模型 identity、硬件、重复测量或可复现实验包；5%～20% MUSHRA 与“每小时少于
一秒 critical error”也缺少足够完整的样本、baseline、置信区间和 serving SLO contract。因此该项只作为
24/30 的 `Official Engineering Evidence / Artifact Not Available`，暂定 Ch38 Experimental refine；
不把厂商 headline 或“chain-of-thought”命名外推成通用 TTS 结论。

日期复核又发现 MegaTrain 的作者发布页在 4 月 5 日已明确宣布正式开源，早于 arXiv v1 的
4 月 6 日，因此其 Source Family 从 W15 回拨本周。全文与实现审计表明，它不是简单的
“ZeRO-Offload 更大模型”案例，而是改变 state ownership：CPU 保存 parameters、gradients 与 Adam
states 的 authoritative copy，GPU 只保留逐层 transient execution cache；three-stream、double buffer、
event ordering、gradient slab 与 block recomputation 共同决定数据移动能否离开 critical path。
论文支持这一机制在作者披露的单卡合同下扩大可训练模型边界，但 checkpoint ablation、1K context
TFLOPS 与正文叙述存在内部数字不一致，也没有 production SLO、故障恢复或完整成本证据。故只保留
CPU-owned streaming 这一 Experimental 演进分支，不把 1.84×、120B 或 512K headline 外推。

W15 attribution reconciliation 还恢复 SkVM 的唯一 primary identity。其 arXiv v1 首发于 4 月 3 日，
4 月 6 日与 11 日只是 v2/v3 revision，因此完整 Source Family 归 W14。全文与作者 runtime/repository
核验显示，它把 Skill 从“直接塞给 Agent 的文本”提升为可 profile、AOT compile、JIT optimize、version
和选择的 executable artifact：compiler 按 model+harness primitive capability 补偿或替换依赖，runtime
再依据资源与 trace 选择 variant。该机制改善的是 heterogeneous target portability，不证明自然语言 Skill
已获得 bytecode 的确定性语义；capability profile staleness、unsafe substitution、JIT overfit、artifact
invalidation、dependency supply chain 与 rollback 都成为新 failure modes。故只保留 Ch80 Experimental
refine，Ch62/68/74/77 做短 handoff，不把后续 release 行为倒写进 v1。

本轮先完整复核了 HISA：它不是“又一种 Sparse Attention”，而是把 DSA 的 flat token-level
indexing 演进为 block coarse filter → token refinement，同时保持下游 Sparse MLA 的 token-ID
接口。论文证明的是特定 A100 kernel contract 下 indexer 开销下降以及所测模型/任务上的质量
接近，并未证明端到端 serving 的 TTFT、吞吐或 SLO 改善；v1 与 v3 的模型、长度和 speedup
口径也发生变化，不能混成同一个 headline。

本检查点又完成 Kernel-Smith 全文与两个 merged upstream PR 的联合核验。其长期价值不是
“模型一次生成更快 kernel”，而是把 executable evaluator、带 lineage 的候选 archive、稳定
测量与 step-centric post-training 组成持续搜索闭环。论文也提供了必要的证据分层：SGLang
案例中 isolated kernel 的 4.78× 在完整 serving 路径中大多只转化为亚百分比 latency 变化，
说明 operator speedup、engine throughput 与 production SLO 必须分别验证；完成该检查点时仍有
19 个候选待全文复核。

随后完成 Marco DeepResearch 的论文、公开 inference artifact 与相邻章节审计。其新增机制是把
verification 从 final-answer scorer 前移到 QA construction、training trajectory 与 test-time
candidate search；但 graph QA verification 在一个子集上出现负向切片，同一 8B agent 兼任生成器
和 verifier 也没有独立性保证。600 tool-call budget、混合来源 baseline 分数与未公开的训练/合成
pipeline 进一步限制外推。当前仍有 18 个候选待全文复核；W14 Evidence Gate 和 Historical Books
Gate 均保持关闭。

本检查点进一步完成 Combee 的全文、appendix、ACE/GEPA artifact 边界与 Ch72～74、Ch77～78
审计。它将 prompt/context learning 的瓶颈从“如何写经验”推进到“并行 worker 的经验如何合并而不
发生 context overload”：hierarchical scan 控制单次 fan-in，augmented shuffle 给高密度 reflection
重复进入聚合树的机会，controller 在实测 delay curve 上选择 batch。论文在四类任务上支持这一机制，
但 context update 不像 gradient 那样线性、可交换；17× 是特定 API/model/task 的 wall-clock 结果，
当前仓库实现也没有与 W14 paper event 绑定的 immutable release。W14 还有 17 项待全文复核。

本检查点继续完成 Stochastic KV Routing 的 19 页论文、appendix、官方 Apple Research 入口与
Ch18～22、Ch39～41 邻接审计。它沿深度轴而非时间轴减少 KV：训练时每层随机使用本层或任一
前层的 K/V，部署时再按硬件约束选择确定的共享组。论文在 Qwen3-1.7B 从零预训练、三类 7B/8B
QA fine-tuning 和单张 80GB GPU inference contract 下提供了支持，但没有公开 checkpoint/code、
GPU 型号、kernel/backend 版本、重复测量或生产 SLO。因而它是“训练语义与 serving layout 联合
设计”的 Experimental 证据，不是现有 checkpoint 的通用 cache-eviction 配方；W14 现余 16 项待审。

本检查点还完成 MiroEval 的全文、robustness/human-study appendix、公开 benchmark/evaluator
仓库与 Ch62/63 邻接审计。其长期价值是把 report synthesis、atomic-claim factuality、process
intrinsic quality 和 process↔report traceability 拆成四个不可互相替代的证据面，并让 web 与
attachment 冲突显式进入 `CONFLICT`。但过程评估依赖系统暴露 intermediate traces；不同 judge
令绝对分数整体漂移 13～17 分，而产品搜索快照、工具预算、成本和完整运行配置并未 matched。
因此排名不写入 Books，只保留 evaluation-object 分层机制；W14 现余 15 项待审。

本检查点再完成 AgentHazard 全文、taxonomy/results/prompt appendix、公开 dataset/code/trajectories 与
Ch62/68/69/77 邻接审计。它把 safety unit 从单个 prompt/refusal 扩为带 tool calls、outputs、权限和
累积状态的完整 run，并显示同一 backbone 在不同 framework 下有显著差异。但 ASR 主要由单一
Gemini-3-Flash judge 判定，未给 benign control、false-positive calibration、确定性 side-effect
verifier 或 matched framework contract；项目也无 immutable release。因此只保留 trajectory threat
model 和 sensor/authority 分离，不沉淀产品/模型风险排名；W14 现余 14 项待审。

本检查点继续完成 LightThinker++ 全文、Dependency 公式、general/agentic experiments、全部相关
appendix、公开训练/推理代码说明与 Ch22/41、Ch71～74/77 邻接审计。它把固定、不可逆的 hidden-state
gist compression 演进为 `raw step + summary + archive/active state`，并用 `commit / expand / fold`
显式管理可逆 working memory。长期价值在于把压缩从一次性文本变换提升为带 state owner、raw-evidence
archive、restore/fold transition 和 runtime identity 的机制；作者 benchmark 仍受自合成 trajectory、
LLM judge、未匹配的 proprietary baselines、当前 main 无 release tag，以及未披露完整 inference
hardware/SLO 的限制。因此暂定 Ch73 refine，Ch71/22/41/77 只作短 handoff，不沉淀 69.9%、2.5x 等
headline；W14 现余 13 项待审。

本检查点继续完成 SKILL0 的 v1 全文、理论与实验 appendices、v2 revision、作者仓库、ALFWorld /
Search-QA 训练脚本，以及 Ch28～30、Ch71、Ch80 邻接审计。它不是让运行时 Skill registry 退出，
而是把外部 Skill 作为训练 scaffold：按 on-policy helpfulness 过滤和排序，再把 skill budget 分阶段
降到零，检验稳定程序性先验能否在无 Skill context 时保留。公开脚本确认 GRPO、`[6,3,0]`
curriculum、视觉渲染/压缩 reward 与环境 reward 处在同一 recipe，因而现有 ablation 不能完全分离
各机制贡献；“internalization”也是 skill-free evaluation 支持的行为推断，不是参数因果定位。
长期 owner 暂定 Ch29，Ch80/71 只承接 registry 与 context-cost handoff；W14 现余 12 项待审。

本检查点再完成 GrandCode 的 v1 全文、全部公式、submission/code-reward/Agentic-GRPO appendices、
v2/v3 revision 边界、官方项目页、报告与提交代码仓库，以及 Ch28～30、Ch75～78 邻接审计。
其长期价值是把长 multi-stage rollout 的训练状态拆成 stage reward、final correction、token-level
behavior-policy version 与 staleness；但两次 advantage 独立归一化后并不等价于 terminal-reward
GRPO，过旧 correction 还会被丢弃。论文没有 Agentic-GRPO 对标准 GRPO 的独立 ablation，也没有
公开训练代码、完整 GPU/rollout/并发/总成本 contract；live-contest、multi-component pipeline 和
test-time RL 的总成绩不能归因给这一算法。故暂定 Ch29 Experimental refine、Ch77/78 handoff，
不沉淀“超越所有人类”的 headline；W14 现余 11 项待审。

本检查点继续完成 Self-Distilled RLVR 的 v1 全文、全部理论附录、v2 revision、当前公开代码/训练
配置，以及 Ch28～30 邻接审计。它把 privileged self-teacher 从 distribution-matching objective
改成 sampled-token 的 stop-gradient magnitude modulator：verifier/group advantage 决定更新符号，
teacher/student likelihood ratio 只重分配同一 trajectory 内的 credit。这个分离值得进入 Ch29 的
token-credit 演进，但论文的“zero leakage”定理只约束 sign、support 与幅度上界，并不证明
privileged-conditioned magnitude 不会改变参数轨迹；Bayesian evidence 解释也依赖模型近似真实条件
分布的强假设。实验仅覆盖 Qwen3-VL-8B-Instruct、32 张 H200、一个困难筛选数据集和五个多模态
benchmark，缺少 credit components、teacher-sync、lambda schedule 与 matched-compute 的充分消融。
当前代码仓库也没有 event-date immutable release。故暂定 Ch29 Experimental refine，不把作者平均
分数或“leakage-free”升级为通用结论；W14 现余 10 项待审。

随后完成 Towards a Medical AI Scientist 的 30 页论文、唯一 v1 metadata、官方项目页/案例与
Ch62、Ch69、Ch77～78 邻接审计。其有价值的不是“医疗研究已经全自动化”，而是把 domain evidence、
code artifact、实验日志、伦理 gate 与 manuscript claim 放在一条研究 workflow 中，并按 reproduction、
literature-guided innovation、open exploration 提升 autonomy。可是公开项目的 GitHub/Hugging Face
仍为 `coming soon`/404；171 cases 的执行还做过随机子采样，code success 只要求训练完成、loss
下降并产出 weights，不证明科学正确、临床有效或可复现。idea/implementation 也大量依赖同源/未充分
校准的 LLM judges，manuscript 对比只覆盖单一 diabetic-retinopathy task 的五篇生成稿。Ch62 已有
claim-level provenance、judge calibration 和 executable≠ground-truth，Ch77/78 已有 durable state、
approval 与 multi-agent responsibility，因而暂定 `No Change — Already Covered`，不把论文分数写入
Books；W14 现余 9 项待审。

本检查点继续完成 GEMS 的唯一 v1 全文、全部实验/ablation/appendix、官方项目页、当前公开实现和
Ch73/76/77/78/80 邻接审计。它把一次生成演进为 criterion decomposition → generation → binary
verification → prompt refinement，并把 raw attempt artifacts 与模型压缩的 experience 同时放入本次
运行的历史；Skill 则按 manifest→按需全文加载。但公开代码的 verifier 只用字符串规则解析 `yes/no`，
同一个 Kimi-K2.5 承担 decomposition、verification、refinement 与 summary，best-image 又只按等权通过
项数选择。论文所称 persistent memory 在核心实现里仍是进程内 list，也没有 identity、provenance、
version、recovery 或 delete contract；Skill 同样没有权限、签名和撤销语义。Ch73/76/80 已覆盖这些
长期机制和缺口，因此暂定 `No Change — Already Covered`，只把它保留为受 workload contract 限制的
案例，不写入模型排名或 6B-vs-closed-model headline；W14 现余 8 项待审。

本检查点随后完成 Terminal Agents 的 51 页 v1、同周 v2、8 月 v3 revision、完整 appendices 与
Ch68/74/77/79/80 邻接审计。v1 的 terminal-vs-web-vs-MCP 对照混入 off-the-shelf server coverage，
不能推出“MCP 协议不行”；v3 新增的 generic `api_call(method, path, body, query)` ablation 才把主要
变量定位为 action-interface granularity：一个 flexible typed API tool 已恢复大部分 terminal 优势，
filesystem/shell 的剩余价值在 large intermediate state、local transform、batch script 和 broader
protocol。与此同时，typed narrow tools 仍提供 schema、permission 与 audit 优势，browser 在 UI-only /
session-bound state 上仍是合理分支。这个 trade-off 补强 Ch74 的 interface design，而不是证明 terminal
单向替代 tool/MCP；暂定 `Refine — Existing Argument (Experimental)`，Books Gate 关闭期间不改正文。
W14 现余 7 项待审。

本检查点继续完成 MemRerank v1/v3 全文、公开 dataset card 与 Ch29/62/68/72/73 邻接审计。
v1 的 Electronics-only `1-in-5` accuracy 与 v3 的两类目、四 retriever、fixed top-100 MRR
不是同一 evaluation contract；v3 才加入按 rank bucket 构造 reward instances、held-out retriever、
deterministic quality regularizer 和可审计 evidence fields。长期机制是把 raw purchase history 转成
query-independent derived preference view，并以 downstream reranking utility 训练，但同一个 o4-mini
同时提供 reward 与最终评价，购买/五星评论也只是 relevance proxy；没有 code/checkpoint、训练硬件、
隐私同意、纠错、失效和删除 contract。故暂定 Ch73 `Refine — Existing Argument (Experimental)`，
Ch29/62/68/72 只作 reward、evaluation、privacy 与 reranking handoff；不保留论文 headline 数字，
Books Gate 关闭期间不改正文。W14 现余 6 项待审。

本检查点继续完成 ASI-Evolve 唯一 v1 全文、circle-packing appendix、当前公开 pipeline/database/
cognition 实现、release 与 artifact coverage，以及 Ch23/29/62/73/77 邻接审计。可沉淀机制不是
“AI 已经自动做开放科学”，而是把 human priors 与 run-derived lessons 分成两种 memory plane：
Cognition 缩短 cold start，Analyzer 将高维 logs/metrics 压成下一轮 decision state，program database
保存 candidate lineage，sampling policy 决定 quality/diversity。可是 Analyzer/Cognition 的三次重复消融
只在廉价 circle packing 上进行；三项高成本主任务没有相同 causal isolation，GPU 型号、总 GPU-hours、
完整随机性与统计检验也未披露。公开仓库只有通用 loop 和 circle-packing demo，不含 architecture/data/RL
主实验 artifact，且无 release/tag。故暂定 Ch77 `Refine — Existing Argument (Experimental)`，Ch73/62
承接 derived lesson 与 evaluator-feedback 风险，Ch23/29 只作 data/RL case handoff；不沉淀 SOTA 数量或
benchmark headline。W14 现余 5 项待审。

本检查点继续完成 Simple Self-Distillation（SSD）的 v1 全文、理论与实验 appendices、v2 revision、
作者 repository/data-generation/evaluation code、三个公开 checkpoint model cards，以及 Ch20、Ch24～29、
Ch62 邻接审计。它并不是“错误代码也能当知识”，而是先用非单位温度和 truncation 改写 frozen model
产生的 token target distribution，再用普通 SFT 把这种 support compression / within-support reshaping 写入
参数，最后独立选择 evaluation decoding policy。v1 在五个模型、约 10,168 个 competitive-programming
prompts、8×B200 与 LiveCodeBench v5/v6 contract 下提供支持；6 月 v2 才加入 GPT-OSS，不能倒写进 W14。
论文未报告训练重复、置信区间、完整总 compute，也没有显式 Limitations section；当前仓库又只公开
generation/evaluation、没有 Megatron training recipe，且默认删除最短 10% outputs，与论文的“空/单行
stub 最小过滤”并非同一 artifact contract。故评分从 discovery-stage 24 调整为 26，暂定 Ch25
`Refine — Existing Argument (Experimental)`，Ch20/62 仅作 decoding 与 evaluation handoff；W14 现余
4 项待审，Historical Books Gate 继续关闭。

## Coverage and Source Coverage

- 模型与研究机构：保留 Google 3 月 31 日和 4 月 3 日官方研究；已回放 OpenAI、Anthropic、Apple、
  Microsoft Research、Amazon Science、Meta、NVIDIA、Ai2、Cohere、Mistral、Qwen、DeepSeek、Kimi、
  Z.ai、MiniMax、ByteDance Seed、StepFun 与 Tencent 的可访问官方入口。新增 Amazon TTS；Microsoft
  ADeLe、inference energy 与 relevance-labeling 是 2026-04 正式发表/传播节点，但 primary first-public
  分别属于 2025-W11、2025-W39 与更早 source families，不重复计为 W14 新候选。部分官方 archive
  不提供可验证的按日快照，负向覆盖结论仍限于本次可访问页面。
- 论文与学术来源：已重放 Hugging Face Daily Papers 3 月 30 日～4 月 3 日并按 arXiv v1 日期
  去重，恢复 14 个 in-window 候选；4 月 4～5 日、arXiv category export、OpenAlex、DBLP、
  Google Scholar、OpenReview/TMLR 的交叉召回仍未闭合。Hugging Face 仅作 discovery，不作
  mechanism evidence。
- AI Infra：已回放 vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、PyTorch、JAX、KServe、Ray、
  Transformers、DeepSpeed、Megatron Core 与 MLX 的官方 release/repository 入口；未定位到
  2026-03-30～04-05 期间可独立形成长期机制节点的 stable release / RFC。GitHub 历史分页与部分
  release API 无法稳定读取，故这里只关闭“已访问入口没有新增项”的检查点，不把负结果提升为完整
  Infra Discovery closure。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| How many raters are enough? | 3 | 3 | 5 | 4 | 5 | 4 | 24/30 | Worth Watching |
| Behavioral-disposition alignment | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | Worth Watching |
| Improving quality and robustness in LLM-based TTS systems | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching — Full Source Review Complete; Official Engineering Evidence / Artifact Not Available |
| Towards a Medical AI Scientist | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Worth Watching — Full Review Complete |
| HISA: hierarchical indexing for fine-grained sparse attention | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Must Read — Full Review Complete |
| Kernel-Smith | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read — Full Review Complete |
| Marco DeepResearch | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read — Full Review Complete |
| GEMS: agent-native multimodal generation | 4 | 3 | 3 | 4 | 5 | 4 | 23/30 | Worth Watching — Full Review Complete |
| MiroEval | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read — Full Review Complete |
| Terminal Agents Suffice for Enterprise Automation | 3 | 4 | 5 | 4 | 5 | 3 | 24/30 | Worth Watching — Full Review Complete |
| MemRerank | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Worth Watching — Full Review Complete |
| ASI-Evolve | 4 | 4 | 3 | 4 | 5 | 4 | 24/30 | Worth Watching — Full Review Complete |
| Embarrassingly Simple Self-Distillation Improves Code Generation | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Must Read — Full Review Complete |
| HippoCamp | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Worth Watching — Full Source Review Complete; No Change / Experimental case |
| SKILL0 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read — Full Review Complete |
| Omni-SimpleMem | 4 | 4 | 3 | 4 | 5 | 4 | 24/30 | Must Read — Full Source Review Complete |
| S0 Tuning | 4 | 4 | 4 | 3 | 4 | 4 | 23/30 | Worth Watching — Full Source Review Complete; artifact identity conflict |
| Learning to Learn-at-Test-Time (Meta-TTL) | 4 | 4 | 3 | 3 | 5 | 4 | 23/30 | Worth Watching — Full Source Review Complete |
| GrandCode | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Must Read — Full Review Complete |
| Self-Distilled RLVR | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read — Full Review Complete |
| AgentHazard | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Must Read — Full Review Complete |
| LightThinker++ | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read — Full Review Complete |
| Combee: parallel prompt learning for self-improving agents | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read — Full Review Complete |
| Stochastic KV Routing | 5 | 5 | 5 | 4 | 5 | 2 | 26/30 | Must Read — Full Review Complete |
| MegaTrain | 5 | 5 | 5 | 3 | 5 | 4 | 27/30 | Must Read — Full Source Review Complete |
| SkVM | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Must Read — Full Source Review Complete; Experimental Skill compiler/runtime |
| GLM-5V-Turbo product launch node | 2 | 3 | 3 | 4 | 4 | 2 | 18/30 | Weekly Only — Version/Product Fact; mechanism belongs to W18 technical-report node |

分数是 discovery-stage relevance triage，并会在全文后纠正；SSD 因机制与长期价值证据从 24 调整为
26。26 个 scored `20+` 候选均已完成非模板化 Full Source Review；GLM-5V-Turbo 的 18/30 产品节点完成
official-source boundary check，不计作论文 Full Source Review。HippoCamp 的官方 arXiv primary text 已于 2026-08-11
重新可读，原 `Primary PDF Blocked` 已解除；其结论仍受未匹配的 tool/budget contract、点估计与三种
archetypal profiles 限制，不支持通用 Agent 或 Memory 排名。

## Recovered Candidate Queue — Not Full Source Review

| First-public Date | Candidate / Primary Identifier | Discovery Signal | Likely ROADMAP Owner | Review Status |
| --- | --- | --- | --- | --- |
| 2026-03-30 | Towards a Medical AI Scientist — arXiv:2603.28589 | domain-constrained research workflow and evidence boundaries | Ch77, handoff Ch62 / Ch69 / Ch78 | Full Source Review Complete |
| 2026-03-30 | HISA — arXiv:2603.28458 | hierarchical sparse index | Ch39, handoff Ch22 | Full Source Review Complete |
| 2026-03-30 | Kernel-Smith — arXiv:2603.28342 | evolutionary kernel optimization | Ch45, handoff Ch52 / Ch77 | Full Source Review Complete |
| 2026-03-30 | Marco DeepResearch — arXiv:2603.28376 | verification-centric deep research | Ch76, handoff Ch72 / Ch77 | Full Source Review Complete |
| 2026-03-30 | GEMS — arXiv:2603.28088 | criterion-wise multimodal generation loop, task-scoped memory and on-demand skills | Ch76, handoff Ch73 / Ch80 | Full Source Review Complete |
| 2026-03-30 | MiroEval — arXiv:2603.28407 | multimodal deep-research process/outcome evaluation | Ch62, handoff Ch63 | Full Source Review Complete |
| 2026-03-31 | Terminal Agents Suffice for Enterprise Automation — arXiv:2604.00073 | interaction-surface granularity, API-first execution and browser fallback | Ch74, handoff Ch68 / Ch79 / Ch80 | Full Source Review Complete |
| 2026-03-31 | MemRerank — arXiv:2603.29247 | downstream-utility-trained derived preference memory | Ch73, handoff Ch29 / Ch62 / Ch68 / Ch72 | Full Source Review Complete |
| 2026-03-31 | ASI-Evolve — arXiv:2603.29640 | dual-memory evaluator-driven research evolution | Ch77, handoff Ch73 / Ch62 / Ch23 / Ch29 | Full Source Review Complete |
| 2026-04-01 | Improving quality and robustness in LLM-based TTS systems — Amazon Science | planned acoustic-token generation, post-generation guardrails and regenerate/fallback control | Ch38, handoff Ch40 / Ch62 / Ch68 | Full Source Review Complete — Official Engineering Evidence / Artifact Not Available |
| 2026-04-01 | Self-Distillation Improves Code Generation — arXiv:2604.01193 | temperature/truncation-shifted self-targets compiled into model parameters | Ch25, handoff Ch20 / Ch62 | Full Source Review Complete |
| 2026-04-01 | HippoCamp — arXiv:2604.01221 | personal-file contextual-agent evaluation | Ch62, handoff Ch72 / Ch73 / Ch68 | Full Source Review Complete — No Change / Experimental Case |
| 2026-04-02 | SKILL0 — arXiv:2604.02268 | external skill scaffold annealed into a skill-free policy | Ch29, handoff Ch80 / Ch71 | Full Source Review Complete |
| 2026-04-01 | Omni-SimpleMem — arXiv:2604.01007 | multimodal memory tiers and autoresearch-owned system optimization | Ch73, handoff Ch72 / Ch62 / Ch68 / Ch77 | Full Source Review Complete |
| 2026-04-01 | S0 Tuning — arXiv:2604.01168 | recurrent launch-state adaptation with zero per-token adapter compute | Ch26, handoff Ch22 / Ch31 / Ch46 | Full Source Review Complete — Artifact Identity Inconsistent |
| 2026-04-01 | Learning to Learn-at-Test-Time — arXiv:2604.00830 | learned cross-episode reflection/adaptation policy | Ch76, handoff Ch62 / Ch73 / Ch77 | Full Source Review Complete |
| 2026-04-03 | GrandCode — arXiv:2604.02721 | multi-stage immediate reward, delayed correction and staleness | Ch29, handoff Ch77 / Ch78 | Full Source Review Complete |
| 2026-04-03 | Self-Distilled RLVR — arXiv:2604.03128 | verifier-owned direction and privileged-teacher magnitude modulation | Ch29, handoff Ch28 | Full Source Review Complete |
| 2026-04-03 | AgentHazard — arXiv:2604.02947 | sequence-level computer-use harm | Ch68, handoff Ch62 / Ch77 | Full Source Review Complete |
| 2026-04-04 | LightThinker++ — arXiv:2604.03679 | reasoning compression as reversible working-memory management | Ch73, handoff Ch71 / Ch22 / Ch41 / Ch77 | Full Source Review Complete |
| 2026-04-05 | Combee — arXiv:2604.04247 | scalable parallel prompt learning | Ch73, handoff Ch77 / Ch78 | Full Source Review Complete |
| 2026-04-03 | Stochastic KV Routing — arXiv:2604.22782 | training-time adaptive depth-wise KV sharing | Ch19, handoff Ch40 / Ch41 | Full Source Review Complete |
| 2026-04-05 | MegaTrain — author release + arXiv:2604.05091 | CPU-owned persistent state and streamed single-GPU execution | Ch35, handoff Ch32 / Ch34 / Ch31 | Full Source Review Complete |
| 2026-04-03 | SkVM — arXiv:2604.03088 | model+harness capability profiling, AOT Skill compilation and JIT/runtime variant management | Ch80, handoff Ch62 / Ch68 / Ch74 / Ch77 | Full Source Review Complete — Experimental |
| 2026-04-02 | GLM-5V-Turbo product launch node — official GLM-V repository | product availability only; mechanism not disclosed at event time | Ch34 follow-up to W18 technical-report family | Low-score Boundary Verified — 18/30；Weekly Only |

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Current score rows | 27 | 2 baseline + 25 recovered；14 at `25–30`, 12 at `20–24`, 1 below 20 |
| Recovered candidate families | 25 | 24 个论文/研究/工程 families 加 1 个 official product-event node，均按可核验 first-public date 归入 W14 |
| Current `20+` Full Source Reviews | 26/26 | 两项 baseline 与 24 个恢复候选均已完成非模板化 Source Review；HippoCamp 原 primary-text access blocker已解除；Amazon TTS 为 official engineering packet，不伪装成论文全文 |
| Academic discovery window | Partial | HF 03-30～04-03 已重放；04-04～05 与其他索引待交叉召回 |
| Official / Infra discovery window | Partial — Reviewed Checkpoint | fixed model/research list 已回放并恢复 Amazon TTS；主要 Infra release/repository 入口已检查，但历史分页/API 缺口阻止完整 closure |
| Unverified / Blocked Backlog | 2 | `Backdoor Attacks on Decentralised Post-Training`（03-31）与 `Cactus`（04-05）只有 W16 attribution identity；primary identifier/text 未定位，不评分、不分配 owner、不阻塞 cursor |
| Recorded Candidate Evidence | Complete | 26/26 `20+` reviews 与 1/1 low-score boundary 已闭合；0 current-review pending |
| W14 Forward Candidate Evidence Gate | Passed | 两个 primary-identity blocker 已显式隔离，不阻塞 cursor；forward cursor 移至 W15 |
| W14 Discovery Gate | Open | official Research checkpoint 已推进；academic cross-index 与剩余 Infra 历史 release coverage 仍未闭合，不得把 candidate queue 完成误报为整周 Evidence Gate 通过 |

## Curation-Lag / Cross-Week Spillbacks

下列条目出现在本周 discovery feed，但 arXiv v1 / first-public date 早于 3 月 30 日，因此不计入
W14 scoring。显式保留它们是为了区分“看见”与“本周发生”，后续回写各自 owner week：

| First-public Date | Candidate | arXiv ID |
| --- | --- | --- |
| 2026-03-20 | Sommelier | 2603.25750 |
| 2026-03-20 | SEAR | 2603.26728 |
| 2026-03-20 | FIPO | 2603.19835 |
| 2026-03-23 | Lie to Me | 2603.22582 |
| 2026-03-25 | MedOpenClaw | 2603.24649 |
| 2026-03-25 | Composer 2 | 2603.24477 |
| 2026-03-25 | ClawKeeper | 2603.24414 |
| 2026-03-26 | Hybrid Memory | 2603.25716 |
| 2026-03-26 | Trace2Skill | 2603.25158 |
| 2026-03-26 | Natural-Language Agent Harnesses | 2603.25723 |
| 2026-03-26 | Density-aware compression | 2603.25926 |
| 2026-03-27 | Learning to Commit | 2603.26664 |
| 2026-03-27 | TAPS | 2603.27027 |
| 2026-03-27 | DataFlex | 2603.26164 |
| 2026-03-27 | Ask or Assume | 2603.26233 |
| 2026-03-27 | XpertBench | 2604.02368 |
| 2026-03-28 | EpochX | 2603.27304 |
| 2026-03-28 | daVinci-LLM | 2603.27164 |
| 2026-03-29 | Emergent Social Intelligence Risks | 2603.27771 |
| 2026-03-29 | PRBench | 2603.27646 |
| 2026-03-29 | MuSEAgent | 2603.27813 |
| 2026-03-29 | KAT-Coder-V2 | 2603.27703 |
| 2026-03-29 | LongCat-Next | 2603.27538 |

MegaTrain 是相反方向的 curation-lag：arXiv v1 在 W15 的 4 月 6 日提交，但作者于 4 月 5 日已发布
“officially releasing”公告并链接公开仓库，因此 Source Family 的 first-public owner 是 W14。
当前 README 的 4 月 12 日 VERL 集成和 4 月 17 日 multi-GPU data parallel 属后续 artifact evolution；
后者超出 W15 乃至本周窗口，均不得倒写成 4 月 5 日首发机制或论文实验证据。

后续 Weekly attribution ledger 还暴露三项 W14 回拨。`Backdoor Attacks on Decentralised Post-Training`
（03-31）与 `Cactus`（04-05）当前只有名称和日期，仓库、通用搜索及可视浏览均未返回可定位的 arXiv ID、
作者页或正文；二者因此进入 `Unverified / Blocked Backlog`，不评分、不猜测机制和 ROADMAP owner，也不
阻塞 forward cursor。GLM-5V-Turbo 的官方 GLM-V repository 则记录 04-02 产品节点；event-time 没有公开
technical mechanism，故只作 18/30 `Version/Product Fact`。其 04-29 technical report 及 CogViT、MMTP、
multimodal RL/runtime 机制仍由 W18 拥有，不能倒写成 04-02 已公开事实。

fixed-source 回放还发现三个 Microsoft Research 的同周 publication / communication nodes，但它们不构成
W14 first-public candidates：ADeLe 对应论文 arXiv:2503.06378 在 2025-03-10 已公开，2026-04-01 是
Nature 发表与官方解读；inference energy 对应 arXiv:2509.20241 在 2025-09-24 已公开，2026-04 是 Joule
publication；LLM relevance labeling 则延续 2024 已公开的论文 family。它们进入跨周 revision/publication
ledger，不重复评分，也不把 journal date 当技术首发。

## Evidence Level

两项 Google 条目是作者研究；HISA 为带版本历史、正文、实验和公开 artifact 的作者论文；
Amazon TTS 是机构官方工程研究，公开了 plan/check/regenerate 控制流与若干作者测量，但没有论文、
技术报告、模型/数据卡、代码或 immutable artifact；其 Evidence Level 为 `Official Engineering Evidence /
Mechanism Disclosed / Artifact Not Available`，只能支持受限机制与 failure taxonomy，不能支持通用性能结论。
Kernel-Smith 已联合核验 v1/v2 metadata、论文正文、公开仓库与 merged upstream PR，但模型、
agent code 和训练数据并未完整公开；Marco DeepResearch 已联合核验论文全文与公开 inference
artifact，但训练/合成 pipeline 并未公开；Combee 已覆盖全文与 appendix，论文指向 ACE/GEPA
项目，但未提供与 event-date 实验绑定的
immutable Combee artifact；Stochastic KV Routing 已覆盖 19 页正文、appendix 与官方研究入口，
但没有公开 checkpoint/code，且 inference benchmark 未披露具体 GPU 型号、backend 与测量方差。
MiroEval 已覆盖全文、robustness/human-study appendix 与公开 evaluator repository，但不同产品的
search/tool/budget contract 不匹配，且 process evaluation 依赖可见 intermediate trace。AgentHazard
已覆盖全文、appendix、dataset/code/trajectory artifact，但 project repository 无 release，ASR judge
也没有 benign-control calibration。LightThinker++ 已覆盖全文、公式、general/agentic experiments、
appendix 与公开代码/模型/数据入口；仓库没有 release/tag，paper 与当前 README 的 search provider
描述存在实现版本边界，且完整 inference hardware、运行方差、成本与 SLO 未披露。SKILL0 已覆盖
v1 全文、理论/实验 appendices、v2 revision 与公开 ALFWorld/Search-QA recipes；当前 main 无
immutable release，v2 新增 WebShop 结果不能倒写为 W14 v1 事实，且 recipe 把 curriculum、视觉
压缩和 reward 组合在一起。GrandCode 已覆盖 v1 全文与全部相关 appendices、v2/v3 revision、
官方项目页、报告及提交代码 artifact；只公开论文和 contest submissions，没有训练代码、模型、
完整 infrastructure 配置或 Agentic-GRPO 独立消融。Self-Distilled RLVR 已覆盖 v1 全文、理论
附录、v2 revision 与当前公开训练实现；其实验 contract 披露模型、长度、batch、rollout 数与
32 张 H200，但没有完整 wall-clock/成本、随机种子/方差或关键机制 factorial ablation。论文的
Bayesian credit 解释依赖一致条件分布近似，所谓 zero-leakage 只证明方向/support isolation 与幅度
有界，不能外推为 privileged information 对最终参数路径没有影响；当前代码也没有与 W14 事件绑定
的 immutable release。Medical AI Scientist 已覆盖 30 页正文、方法/结果/限制、唯一 v1 metadata 与
官方项目页；公开 code/model/data links 仍为 coming-soon/404，Med-AI Bench manifest、运行日志、
生成 manuscript 与容器没有可重放 artifact。它的 executable success、idea/manuscript judge 和单任务
human comparison 只能支持有限 workflow/evaluation 观察，不能证明科学新颖性、临床 validity 或
端到端 autonomous discovery。GEMS 已覆盖唯一 v1、完整方法/实验/appendix、项目页与当前核心实现；
论文未披露硬件、API/token/cost、wall-clock、concurrency、SLO 或充分随机性，代码中的同源 MLLM
verifier、字符串 `yes/no` 解析、进程内 history 与无治理 Skill 也限制“persistent / scalable”主张。
Terminal Agents 已覆盖 v1/v2、v3 的新增 granularity/open-weight/limitations/reproducibility/ethics、
全部 appendices 与相邻章节；公开代码、dataset、environment 和完整 traces 仍承诺 acceptance 后发布，
主矩阵也没有全量多次重复，且 binary success 未衡量 partial/wrong side effects。MegaTrain 已覆盖唯一
v1 的 method、algorithm、完整 evaluation、Appendix A/B、作者 4 月 5 日发布页与当前 repository；它支持
披露的单卡合同下 layer-wise streaming 与显式 state lifecycle，但 checkpoint-interval ablation 和 1K-context
TFLOPS 都存在表格与正文冲突，current repo 的 RL 与 multi-GPU 扩展也不是 event-time paper evidence。
所需 rater 数取决于 variance、
effect size、aggregation 与决策风险；behavioral consistency 依赖 prompt、language、model
version 与 sampling policy；HISA 和 Kernel-Smith 的性能数字都只在论文披露的 workload
contract 内成立。

## Cross-Week Deduplication

与 W04/W09 的 character/persona 工作属于 `Layering`：evaluation 测量行为，interpretability
提出内部机制，policy 规定 desired behavior。HISA 与 DSA 是 `Direct Evolution`：保留细粒度
token selection 与下游 Sparse MLA 接口，在 indexer 前增加 block-level coarse pruning；它不是
对 dense attention 或原始 DSA 的无条件替代。Kernel-Smith 与 AlphaEvolve 属于
`Principle Reuse`，并与 Ch45 的 heuristic / specialized kernel search 构成 `Layering / Dependency`：
它把搜索状态、执行反馈和 artifact lineage 工程化，而不是用 Agent 替代 compiler、library 或人工
kernel engineering。

Marco DeepResearch 与现有 RAG/Reflection/Workflow 是 `Layering / Dependency`：retrieval 产生
evidence，verifier 对候选和约束做受限判断，Workflow 拥有 retry/reset/budget 状态。它不是
“更多 tool calls 必然更可靠”的 `Direct Evolution`；没有独立 verifier 时，额外搜索也会放大同源错误。

Medical AI Scientist 与通用 AI-scientist pipeline 属于 `Direct Evolution`：通用 idea→code→paper
workflow → domain task/data/evidence schema → clinician/engineer role decomposition → ethics/quality gate
→ 分级 autonomy modes。它与 Ch62 claim provenance、Ch69 production contract、Ch77 durable workflow、
Ch78 responsibility decomposition 是 `Layering / Dependency`；domain prompting 和同一 GPT-5 的多个
roles 没有产生独立 evidence，伦理 reviewer 也不是 IRB、data-license verifier 或 clinical approval
authority。Reproduction 与 human-led research 继续适用于高风险、证据不足和需要独立复现的阶段。

GEMS 与 one-shot generation、random search 和 last-only refinement 属于 `Direct Evolution`：一次生成
→ 多次采样 → 原子 criterion feedback → raw attempt + compressed experience → 按需 Skill。它与 Ch73
的 working-memory lifecycle、Ch76 的 verifier/reflection loop 和 Ch80 的 Skill registry 属于
`Layering / Dependency`。同源 MLLM 的多个角色不产生独立 evidence；任务内 list 也不是 durable
memory。低延迟、弱 verifier、简单 prompt 或昂贵 generator 下，one-shot / bounded retry 仍是合理分支。

Terminal Agents 与 narrow tool catalog、generic API、terminal/filesystem 和 browser 不是单线替代。
关系是 `Direct Evolution`：many narrow endpoint tools → one flexible typed API call → filesystem-backed
transform/batch/protocol escape hatch → terminal-first + browser fallback；MCP 只负责连接协议，因此与
Ch79 是 `Layering / Dependency`。Typed domain tools 在 schema、least privilege、approval 与 audit 上
仍合理；browser 继续拥有 rendered/session/UI-only state。长期 owner 是 Ch74 的 interface contract，
不是把 terminal 当成新的 Workflow 或把 shell 当成 security boundary。

Combee 与 Ch73 的 derived memory/consolidation 是 `Direct Evolution`，与 Ch77/78 的 parallel
workflow 和 coordination tax 是 `Layering / Dependency`：sequential experience update → naive
large-batch fan-in → hierarchical aggregation with redundancy → future async/versioned merge。它没有
证明自然语言 context update 具备 distributed gradient 的代数性质。

Stochastic KV Routing 与 MQA/GQA/CLA、temporal eviction 和 KV quantization 不是单线替代关系。
它与 CLA 属于 `Direct Evolution`：固定跨层共享 → 训练时随机暴露多种 KV source → 部署时选择
确定共享组；与 temporal eviction / quantization 属于正交 `Layering / Dependency`。它也没有证明
任意现有 checkpoint 可安全删掉逐层 KV；训练得到的 query-to-KV alignment 是机制成立的前提。

MiroEval 与 Ch62 现有的 final-outcome、trajectory、claim provenance 与 rubric 分层属于
`Layering / Dependency`：report quality ≠ factuality ≠ process quality ≠ process-report alignment。
它不是用 process score 替代 outcome；closed-source trace 缺失、judge drift 和 live-web drift 会让
不同 evidence planes 具有不同缺失机制，不能简单平均成绝对能力。

AgentHazard 与 prompt-level jailbreak/refusal evaluation 是 `Direct Evolution`：single prompt →
cumulative task description → tool-mediated execution trajectory → side-effect/authorization evidence。
它与 Ch68 的 policy sensor、least privilege、sandbox 和 approval 属于 `Layering / Dependency`；
trajectory judge 可以发现累积风险，但仍不是执行 authority，也不能替代 deterministic tool policy。

LightThinker++ 与固定 interval summary、irreversible gist/cache-token compression 属于
`Direct Evolution`：full history → fixed lossy bottleneck → dual-form raw/summary entity → model-directed
archive/expand/fold。它与 Ch71 的 Context assembly、Ch73 的 working-memory lifecycle、Ch77 的
authoritative workflow state 属 `Layering / Dependency`；与 Ch22/41 的 hidden-state/KV reduction 只共享
“缩小 active working set”的 `Principle Reuse`。显式 memory action 没有把模型输出升级成可靠 state
transition，runtime 仍须验证 target ID、保存原始 evidence、限制 budget，并处理 stale reference/replay。

SKILL0 与纯 inference-time skill retrieval 属于 `Direct Evolution`，但不是单向替代：runtime
检索并注入 Skill → 训练时让 Skill 充当可观测 scaffold → 按 on-policy helpfulness 过滤、排序并逐步
撤掉 context → 在 skill-free evaluation 中检查稳定行为是否保留。它与 Ch29 的 grouped rollout、
reward measurement 和 curriculum 属 `Layering / Dependency`，与 Ch80 的 versioned Skill registry、
provenance、permission 和 rollback 属于共存分支。稳定程序性先验适合训练吸收；新事实、tenant
policy、可执行资源、权限和需要 hot-fix 的行为仍应留在运行时 registry，不能压入不可撤销的权重。

GrandCode 与 terminal-only GRPO 属于 `Direct Evolution`：等待完整 trajectory → stage reward 到达即
更新 → final reward 到达后用 `r_N-r_t` 修正 → 按 token behavior-policy age 降权或丢弃。它与 Ch77
durable workflow state、Ch78 multi-component ownership 是 `Layering / Dependency`；与 test-time
best-of-N/LoRA adaptation 只是同一系统中的另一条优化轴。由于 immediate 与 correction 分别做
group normalization，其和不恢复标准 terminal advantage；早反馈降低延迟，却新增 double-update、
correction loss、policy-version storage 和 biased credit 的风险，严格同步 terminal update 在任务较短、
verifier 较快或 sample efficiency 优先时仍成立。

Self-Distilled RLVR 与 sequence-uniform GRPO credit 属于 `Direct Evolution`：同一 sequence advantage
作用于所有 tokens → privileged self-teacher 给 sampled tokens 计算 evidence ratio → verifier 保留
reinforce/penalize 的符号权、teacher 只调节幅度 → teacher guidance 退火回 uniform GRPO。它与
PPO/GRPO clipping 是 `Principle Reuse`，不是同一约束：前者限制 policy ratio，后者限制 credit
multiplier。它也不否定 sequence-uniform credit；当 reference 不可靠、额外 teacher forward 成本过高、
all-equal group 无 verifier signal 或需要最清楚 objective 时，旧分支仍成立。

MegaTrain 与 ZeRO/FSDP offload 是 `Direct Evolution`，不是单向替代：GPU-resident replicated state →
DP-domain sharding → 部分 state/compute offload → CPU authoritative store + per-layer transient GPU cache。
它与 activation recomputation、flat-buffer DMA、stream/event ordering 属 `Layering / Dependency`；与 PP 都
使用 overlap/pipeline 只属 `Principle Reuse`。模型能驻留 HBM、需要通用 autograd/graph capture，或多 GPU
collective 能提供更高吞吐和成熟恢复时，原有分支仍成立。

## Knowledge Tree Position

Ch39 Prefill 为 HISA 主 owner，Ch22 Long Context 作短 handoff；Ch45 GPU execution 为
Kernel-Smith 主 owner，Ch52 / Ch77 仅承接 system-evidence 与 workflow handoff；Ch76 Reflection
为 Marco DeepResearch 主 owner，Ch72 / Ch77 连接 evidence sufficiency 与 durable budget/reset；两项 Google
研究位于 Ch62 Evaluation → Ch68 Security；Amazon TTS 由 Ch38 主 owner，因为它扩展 inference request
state machine 的 model-internal plan、post-generation validation 与 retry/fallback；Ch40 只承接
autoregressive acoustic-token dependency，Ch62/68 分别承接 measurement 与 guardrail handoff，不把它
误写成 Prefill/Decode kernel 优化；MiroEval 由 Ch62 主 owner，Ch63 只承接 run/process
telemetry 的采集边界；AgentHazard 由 Ch68 主 owner，Ch62/77 分别承接 EvalSpec 与 durable run
state；LightThinker++ 由 Ch73 Memory 主 owner，Ch71/22/41/77 分别承接 Context projection、模型内部
压缩、KV footprint 与 authoritative workflow handoff；Ch73 Memory 也为 Combee 主 owner，Ch77/78 连接
aggregation workflow 与 coordination；Ch19 KV Cache 为 Stochastic KV Routing 主 owner，Ch40/41
分别承接 decode data path 与 runtime lifecycle handoff；SKILL0 由 Ch29 主 owner，Ch80/71 分别保留
运行时 Skill identity 与 context-cost 分支；GrandCode 也由 Ch29 主 owner，Ch77/78 只承接 durable
stage state 与 multi-component responsibility；Self-Distilled RLVR 同样由 Ch29 主 owner，Ch28 只承接
terminal reward 到 token credit 的问题定义；Medical AI Scientist 由 Ch77 主定位，Ch62/69/78 的现有
contracts 足以完成 evidence、production boundary 与 role-ownership handoff；GEMS 由 Ch76 主定位，
Ch73/80 的现有 memory/Skill contracts 已覆盖可沉淀机制；Terminal Agents 由 Ch74 主 owner，
Ch68/79/80 分别承接 credential boundary、MCP protocol 与 platform governance；MemRerank 由 Ch73 主
owner，Ch29/62/68/72 分别承接 reward learning、evaluation leakage、personal-data governance 与 reranking；
ASI-Evolve 由 Ch77 主 owner，Ch73/62 承接 derived lesson 与 feedback/evaluator boundary，Ch23/29 只作
data-curation 与 RL-search case handoff；Simple Self-Distillation 由 Ch25 主 owner，Ch20 承接
sampling-policy 与 parameterized distribution transformation 的边界，Ch62 承接 benchmark / pass@k
证据合同；恢复队列还涉及 Ch28、
Ch52、Ch69、Ch73～77、Ch80。

MegaTrain 由 Ch35 ZeRO/offload 主 owner，Ch32/34/31 分别承接 link overlap、pipeline analogy 与
checkpoint atomicity，Ch36 只保留 future multi-GPU composition。

GLM-5V-Turbo 04-02 product node → Ch34 / W18 technical-report handoff；只记录 version availability，
不拥有 CogViT、MMTP、multimodal RL/runtime 机制。

## Recommended Action

保留 baseline；继续补齐 academic cross-index 与剩余 Infra 历史 release 覆盖，并在 primary identity 可访问时重试两个 blocked
spillbacks。Amazon TTS、HISA、Kernel-Smith、Marco DeepResearch、MiroEval、Terminal Agents、MemRerank、ASI-Evolve、Simple Self-Distillation、AgentHazard、LightThinker++、SKILL0、GrandCode、Self-Distilled RLVR、Combee、Stochastic KV Routing 与 MegaTrain 均暂定
`Refine — Existing Argument`，但只在全历史 Evidence Gate
通过后进入 Books；Medical AI Scientist、GEMS 与 HippoCamp 暂定 `No Change — Already Covered`；
HippoCamp 仅作为 Ch62 的 Experimental evaluation case 保留在 Weekly。不新增通用 rater threshold，
也不把 kernel speedup 写成 serving speedup。
GLM-5V-Turbo 04-02 节点保持 `Weekly Only — Version/Product Fact`，机制审计留在 W18。已发现候选的
Evidence Gate 通过，forward cursor 移至 W15；W14 Discovery Gate 仍 Open，后续 backlog sweep
继续补覆盖，不把本检查点误报为 W14 完整 Discovery closure。

## Event-Date Daily Decision

历史回填不补造 Daily。26 个 scored candidates、2 个 blocked identities 与显式日期/跨周归属边界直接
记录在 Weekly，并按 first-public date 归周。

## Books Integration Decision

`Complete — W14 Source-Family Books Gate`。下列暂定清单保留逐项 Source Review 时的 owner 推理，
最终 disposition、Stable Node 与实际变更以文末 2026-08-14 Final Ledger 为准。baseline 两项当时暂为
`No Change`；Amazon TTS 暂定
`Refine — Existing Argument (Experimental; Official Engineering Evidence; Artifact Not Available)`（Ch38
主 owner、Ch40 / Ch62 / Ch68 handoff）；它补充 state-machine 机制，但必须等全历史 Gate，且不得写入
未披露模型实现或 headline 数字。Medical AI Scientist 暂定
`No Change — Already Covered`（Ch77 主定位；Ch62 / Ch69 / Ch78 已覆盖证据、治理与责任边界）；
GEMS 暂定 `No Change — Already Covered`（Ch76 主定位；Ch73 / Ch80 已覆盖 memory lifecycle 与
Skill governance）；
Terminal Agents 暂定 `Refine — Existing Argument (Experimental)`（Ch74 主 owner、Ch68 / Ch79 /
Ch80 handoff）；
MemRerank 暂定 `Refine — Existing Argument (Experimental)`（Ch73 主 owner、Ch29 / Ch62 / Ch68 /
Ch72 handoff）；
ASI-Evolve 暂定 `Refine — Existing Argument (Experimental)`（Ch77 主 owner、Ch73 / Ch62 / Ch23 /
Ch29 handoff）；
Simple Self-Distillation 暂定 `Refine — Existing Argument (Experimental)`（Ch25 主 owner、Ch20 /
Ch62 handoff）；
HISA 暂定 `Refine — Existing Argument`
（Ch39 主 owner、Ch22 handoff）；Kernel-Smith 暂定 `Refine — Existing Argument (Experimental)`
（Ch45 主 owner、Ch52 / Ch77 handoff）；Marco DeepResearch 暂定
`Refine — Existing Argument (Experimental)`（Ch76 主 owner、Ch72 / Ch77 handoff）；
MiroEval 暂定 `Refine — Existing Argument (Experimental)`（Ch62 主 owner、Ch63 handoff）；
AgentHazard 暂定 `Refine — Existing Argument (Experimental)`（Ch68 主 owner、Ch62 / Ch77 handoff）；
LightThinker++ 暂定 `Refine — Existing Argument (Experimental)`（Ch73 主 owner、Ch71 / Ch22 / Ch41 /
Ch77 handoff）；
SKILL0 暂定 `Refine — Existing Argument (Experimental)`（Ch29 主 owner、Ch80 / Ch71 handoff）；
GrandCode 暂定 `Refine — Existing Argument (Experimental)`（Ch29 主 owner、Ch77 / Ch78 handoff）；
Self-Distilled RLVR 暂定 `Refine — Existing Argument (Experimental)`（Ch29 主 owner、Ch28 handoff）；
Combee 暂定 `Refine — Existing Argument (Experimental)`（Ch73 主 owner、Ch77 / Ch78 handoff）；
Stochastic KV Routing 暂定 `Refine — Existing Argument (Experimental)`（Ch19 主 owner、
Ch40 / Ch41 handoff）；Omni-SimpleMem 暂定 `Refine — Existing Argument (Experimental)`（Ch73 主 owner、
Ch72 / Ch62 / Ch68 / Ch77 handoff）；S0 Tuning 暂定 `Refine — Existing Argument (Experimental;
Artifact Identity Inconsistent)`（Ch26 主 owner、Ch22 / Ch31 / Ch46 handoff）；HippoCamp 为
`No Change — Already Covered / Experimental Evaluation Case`（Ch62 主 owner、Ch72 / Ch73 / Ch68
handoff）；Meta-TTL 暂定 `Refine — Existing Argument (Experimental)`（Ch76 主 owner、
Ch62 / Ch73 / Ch77 handoff）；MegaTrain 暂定 `Refine — Existing Argument (Experimental)`（Ch35 主
owner、Ch32 / Ch34 / Ch31 handoff）。W14 和全历史 Evidence Gate 通过前，
不进入 Historical Books Integration，也不修改 Books。
GLM-5V-Turbo 04-02 节点为 `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`；W18 report
已拥有机制与 provisional Ch34 disposition，不重复建立 Books candidate。两个 blocked identities 不进入 Books。
SkVM 暂定 `Refine — Existing Argument (Experimental)`（Ch80 主 owner，Ch62 / Ch68 / Ch74 / Ch77
handoff）；它补充 Skill compiler/runtime 的 target-profile、variant identity 与 lifecycle contract，但必须等
全历史 Evidence Gate，且不能把语言编译类比外推为确定性执行保证。

## Ignored Noise

将单一实验的 rater 数量写成所有 benchmark 的固定最佳实践。

## Full Source Review

### Improving quality and robustness in LLM-based TTS systems — 24/30

- **Candidate / Week / Score**：Amazon Science 的同名官方工程研究；2026-W14；24/30（TN 4、SI 4、
  PV 4、SR 4、PR 5、L 3）。
- **Source Family / Type / Date**：`AMAZON-LLM-TTS-PLAN-GUARDRAIL-RETRY`；Amazon Science official
  engineering article，2026-04-01 首次公开，本次访问 2026-08-12。没有链接到独立 technical report、
  paper、system/model card、repository、release 或 dataset artifact；因此 `Full Source Review` 指完整覆盖
  当前唯一官方材料，不冒充 paper full read。
- **Original Problem / Previous Design / Changed Constraint**：traditional modular TTS 与 non-autoregressive
  FastSpeech-style pipeline 显式拥有 grapheme/phoneme、duration 与 acoustic stages，容易定位 duration 与
  pronunciation failure；LLM-based autoregressive TTS 用逐 acoustic token generation 换取自然度与统一建模，
  却把 duration 隐入生成过程，产生 repetition、hallucination、early cutoff、heteronym 和 accent leakage。
  旧 cascade 仍适合可替换、可观察、严格 duration control 的 workload；新约束是需要在保留 autoregressive
  expressiveness 的同时建立 production reliability contract。
- **Mechanism / State Ownership / Control Flow**：locale-weighted data augmentation + LoRA 调整 polyglot
  pronunciation；CFG 生成更 expressive 的 reference audio；模型在 acoustic tokens 前先生成 phoneme sequence
  与 total/per-phoneme duration plan。该 plan 是 model-produced derived state：generation 后 guardrail 比较
  actual duration、phoneme count 与 predicted plan，异常则由外层 agent 改 sampling 重试或进入 fallback。
  ASR metric 与 attention-derived metric 联合过滤训练数据。控制流因此是
  `text -> phoneme/duration plan -> acoustic generation -> duration/length checks -> accept | regenerate | fallback`；
  official article 没有披露 retry budget、fallback owner、plan persistence、streaming commit point 或 cancellation
  semantics。
- **Implementation / Evaluation Contract**：官方事实只说明 locale-specific LoRA、CFG-conditioned reference、
  phoneme/duration prediction、post checks、agentic retry 与 ASR+attention filtering；没有参数规模、architecture、
  tokenizer/codec、training corpus、precision、hardware、batch/concurrency、streaming chunk、tail latency、cost、
  seeds 或 code。文章报告九个 locale 的 MUSHRA relative improvement 与 generic long-form text 的 critical-error
  duration，但没有披露 listener/sample count、confidence interval、matched baseline identity、文本分布、语言
  分层、并发、SLO 或完整错误计数，故数字只保留在 Weekly evidence packet，不写 Books。
- **What the Evidence Proves / Does Not Prove**：它支持“显式生成计划可以成为 autoregressive media generation
  的 validation oracle 和 debug surface”，也支持“生成后检测必须连接 bounded retry/fallback”；它不证明
  hidden chain-of-thought、任意 TTS architecture、所有语言/声音或通用 Agent retry 都会提高可靠性，不证明
  公开数字可复现，也不证明端到端 streaming latency 或成本改善。`chain-of-thought` 在此只是厂商对可见
  phoneme/duration plan 的命名，不应与自然语言 reasoning trace 等同。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：额外 plan tokens 增加 latency/compute，错误 plan
  会把 guardrail 变成 correlated verifier；阈值过严造成 false retry 与 tail amplification，阈值过松漏过静默
  corruption；retry 消耗 capacity，并要求 idempotency、budget、fallback 与 partial-audio commit policy。模块化
  G2P/duration/acoustic pipeline 在 deterministic control、可替换组件、低算力或强审计场景仍合理；hybrid
  pipeline 可让 plan/check 留在显式模块而由 autoregressive decoder 负责声学质量。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：`Direct Evolution`：implicit autoregressive duration
  -> explicit model-produced plan -> post-generation checks -> bounded regenerate/fallback；与 traditional modular
  duration predictor 是 `Principle Reuse`，不是“回到旧 pipeline”。已读 Ch38～40；Ch38 主 owner，Ch40、
  Ch62、Ch68 短 handoff。暂定 `Refine — Existing Argument (Experimental; Provisional; Historical Books Gate
  Closed)`；只可能补充 plan/validate/retry state contract，不沉淀厂商 benchmark 或未公开实现。
- **Open Questions**：plan 与 audio chunk 的 commit/rollback 怎样原子化？streaming 中何时允许播放、何时还能
  regenerate？阈值如何按 locale/speaker/calibration version 管理？retry/fallback 如何进入 admission、tail SLO、
  cost 与 abuse guardrail？独立 ASR/verifier 怎样避免与生成器共因失效？

### GLM-5V-Turbo product launch node — 18/30 boundary verification

- **Source Family / Event Boundary**：`GLM-5V-TURBO-MMTP-MULTIMODAL-RL-RUNTIME`。official GLM-V
  repository 将产品节点标记为 2026-04-02；technical report arXiv:2604.26752 v1 于 2026-04-29 首次公开，
  归 W18。本条只核验 W14 product availability，不把后续 report 的 CogViT、MMTP、joint RL、runtime
  或 benchmark 倒写成 04-02 已披露机制。
- **What the Evidence Proves / Does Not Prove**：official repository 支持“GLM-5V-Turbo 在该日形成产品
  family 节点”；event-time 没有可定位 model card、architecture、weights、training/runtime contract 或
  immutable release，因此不能从产品能力反推参数、tokenization、parallelism、RL 或 serving 实现。
- **Evolution / ROADMAP / Disposition**：`product launch -> later technical-report mechanism disclosure` 是同一
  Source Family 的 `Layering / Revision Evidence`，不是两个独立机制。18/30；`Weekly Only — Version/Product
  Fact / Mechanism Not Disclosed`。W18 technical-report packet 已由 Ch34 主持并保留 Experimental evidence
  boundary；W14 不重复建立 Books candidate。

### Two attribution-only identities — Unverified / Blocked Backlog

- `Backdoor Attacks on Decentralised Post-Training`（provisional first-public 2026-03-31）与 `Cactus`
  （2026-04-05）来自 W16 second-pass attribution ledger。当前仓库没有 arXiv ID、作者或 artifact identity；
  搜索与浏览入口也未获得可核验 primary metadata/正文。
- 二者不计入 score row 或 Full Source Review，不根据标题推断 backdoor、decentralised training、Agent、
  memory 或 serving 机制，不分配 ROADMAP owner。状态为 `Unverified / Blocked Backlog`；primary identity
  可访问后从 metadata 开始重审，不阻塞 forward cursor。
- **Post-forward retry（2026-08-12）**：再次以完整候选名、日期和可能的 arXiv 入口执行精确检索，仍未定位
  可验证的 identifier、作者或正文。W14 backlog retry checkpoint 完成但两项继续 blocked；不评分、不分配
  owner，post-forward sweep 可继续 W15。
- **Blocked-skip ledger review（2026-08-13）**：复核确认二者仍未进入 Candidate Scoring、Full Source
  Review、ROADMAP owner 或 Books disposition；同一 arXiv/OpenAlex 访问限制已在 W13 本轮检查点得到
  明确确认，因此不重复尝试受禁止的外部路径，也不从名称补写机制。W14 Candidate Gate 保持通过，
  backlog cursor 进入 W15；broader Discovery/Historical Evidence Gate 继续 Open。

### SkVM: Revisiting Language VM for Skills across Heterogeneous LLMs and Harnesses — 29/30

- **Candidate / Source Family / Date**：`SKVM-SKILL-COMPILER-RUNTIME`；arXiv:2604.03088 v1 2026-04-03，
  v2 04-06、v3 04-11 仅作 revision boundary；author repository/current releases 用于验证 runtime surface，
  不倒写 v1 artifact state。
- **Access / Full-read Coverage**：已读 metadata、v1/v2/v3 revision、paper problem/background、primitive
  capability model、AOT compiler passes、dependency substitution、environment binding、DLP/ILP/TLP extraction、
  runtime selection、JIT recompilation/code solidification、resource-aware scheduling、evaluation/ablations、
  limitations 与关键 appendix；并核对作者 repository 的 profile、compile、run、bench、proposal review、
  cache layout 和 artifact lifecycle。
- **Original Problem / Previous Design / Changed Constraint**：raw `SKILL.md` 直接注入 context 对单一
  model+harness 简单且保留作者原意；跨模型、工具 schema、sandbox、dependency 与 context budget 后，同一
  Skill 会因 primitive capability 缺失、工具名/参数差异或执行粒度不匹配而失效。约束变化是 Skill 从私有提示
  变成跨 target 分发的长期 artifact。
- **Mechanism / State Ownership / Flow**：profiler 生成 `(model, harness, revision)` capability profile；AOT
  compiler 依据 primitive capability 做补偿/替换，绑定环境依赖并抽取 data/instruction/task parallelism，产出
  target-specific variants；runtime 按 profile、dependency 与资源状态选择 variant，monitor 记录 trace，JIT
  可产生新的 proposal，经 review 后 solidify。registry/compiler 拥有 raw Skill、target profile、dependency
  graph、compiled variant 与 lineage；runtime 拥有本次 selected variant、resource lease、trace 与 failure state。
- **Implementation / Evaluation Contract**：论文覆盖 8 个 models、3 个 harnesses、118 个 tasks，并比较 raw、
  compiled 与 optimized Skill 的成功、token 与 latency；作者 repository 当前 benchmark corpus 已演进，不能
  当作 event-time immutable snapshot。公开材料没有完整硬件、API provider capacity、cost、并发、p95/p99、
  SLO 与跨租户 failure injection；headline 只属于作者合同。
- **What the Evidence Proves / Does Not Prove**：证据支持 target profiling + compilation + runtime adaptation
  能在作者 heterogeneous matrix 中改善 portability/efficiency，也支持 parallelism extraction 与 resource-aware
  execution 是 Skill 的系统问题。它不证明自然语言 Skill 拥有 bytecode 的确定语义，不证明 LLM-generated
  substitution 安全、JIT 单调改善，或任意 model/harness 都能由有限 primitive set 完整描述。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：新增 capability-profile staleness、compiler
  hallucination、dependency supply-chain、unsafe substitution、variant explosion、cache invalidation、JIT overfit、
  trace poisoning、non-deterministic reproducibility、parallel fan-out 与 rollback/revocation。target 稳定、Skill
  简单或高风险动作需要人工签审时，raw/interpreted Skill 与 narrow deterministic workflow 仍合理。
- **Evolution / ROADMAP / Decision**：`raw Skill text -> target capability profile -> AOT target variant ->
  runtime selection -> trace-driven JIT proposal -> reviewed solidification` 为 `Direct Evolution`；与 compiler/
  VM 只是 `Explanatory Analogy + Principle Reuse`，不证明实现等价。已读 Ch62、Ch68、Ch74、Ch77、Ch80；
  Ch80 主 owner。`Refine — Existing Argument (Experimental; Historical Books Gate Closed)`。
- **Open Questions**：target profile 何时失效并触发 recompile？dependency、tool schema、model revision 与
  sandbox policy 如何进入 artifact identity？JIT proposal 怎样做 held-out validation、签名、canary、in-flight
  pinning、revoke 与 rollback？resource scheduler 如何限制 compiler 抽取的 parallelism 不放大 cost 或 side effect？

### Towards a Medical AI Scientist — 24/30

- **Candidate / Week / Score**：Towards a Medical AI Scientist；2026-W14；24/30。
- **Source Family ID / Type**：`MED-AI-SCIENTIST-DOMAIN-RESEARCH-WORKFLOW`；arXiv paper + official
  project page + public case-study pages。第三方摘要不作机制证据。
- **Event Date / Revision History**：arXiv 仅有 v1，2026-03-30；无后续 revision。官方项目页当前把
  GitHub 标为 `coming soon`，链接到 `CUHK-AIM-Group/Med-AI-Scientist` 返回 404；Hugging Face 链接
  同样返回 404。不能把计划公开当成已有 artifact。
- **Access and Full-read Coverage**：已读 30 页论文的 metadata、Introduction、全部 Results、三种
  autonomy modes、171-case benchmark construction、idea/implementation/execution/manuscript evaluation、
  两个完整 case-study 主线、Discussion、Limitations、Idea Proposer、Experimental Executor、
  Manuscript Composer、Med-AI Bench、performance/human evaluation 与 Related Work；并核验项目页、
  evidence-enhanced ideas、case-study 入口和缺失的 code/model/data repository。论文无独立 appendix
  正文、无公开 run artifact、benchmark manifest、generated papers 或 container image。
- **Original Problem**：通用 AI-scientist workflow 能生成看似合理的研究，却不自动理解 clinical
  task、heterogeneous medical modalities、dataset/license/ethics、domain metric 与 code feasibility；
  idea、implementation、experiment 和 paper 之间还可能发生 claim drift。
- **Why Previous Design Was Reasonable**：通用 single-agent 或 idea→code→paper pipeline 对低风险、
  标准数据和明确 evaluator 的研究迭代成本低，roles 少、state 简单。人工研究则保留真正 domain
  authority、伦理责任与独立复现。两者在开放 artifact、不确定 clinical consequence 或高风险决策中
  仍成立，不应被“更多 domain roles”直接替代。
- **Changed Constraint / Principle**：医疗研究把 domain evidence、data modality、ethics、execution
  contract 和 manuscript reporting 同时变成 workflow constraints。长期原则是让 domain specialization
  进入 typed inputs、gates 和 artifact lineage，而不是只靠 persona 名称。
- **Mechanism**：系统提供 reproduction、literature-inspired innovation、task-driven exploration 三个
  逐级提高 autonomy 的入口。Idea Proposer 由 Analyzer/Explorer 检索 clinical/engineering evidence，
  Preparer/Surveyor 连接论文与 code，clinician-engineer co-reasoning 反复匹配临床合理性和实现可行性，
  Assessor 做 quality/ethics gate；Executor 在 Docker 中按 Investigator→Planner→Executor→Judger→Analyst
  流动，将 logs/metrics 回馈修正；Composer 从 structured implementation/results 生成 sections/figures，
  再做 ethics/reporting、cross-reference 与 LaTeX compilation checks。
- **State Ownership / Control and Data Flow**：长期正确实现需要 workflow owner 持久化 task/dataset/
  paper/code identities、research-plan version、execution protocol、container/dependency、logs/checkpoints/
  metrics、judge feedback、claim-source mapping、ethics/license/approval 与 manuscript revision。论文描述
  role flow，却没有公开 state schema、transaction/retry/idempotency、approval authority 或 failure recovery；
  同一 GPT-5 的多个 roles 也不能被当成独立 clinician/engineer evidence owners。
- **Implementation Details**：所有 agents 以 general-purpose LLM（论文举 GPT-5）为 base，文献检索
  包括 OpenAlex/Google Scholar，工程侧检索 open-source repositories；实验在 predefined Docker
  environment 执行，成功要求无错误完成、loss 单调下降、无 gradient explosion、生成 valid weights
  与 quantitative test results。论文未披露 prompts、模型 snapshot/API version、sampling、tool budget、
  Docker image、GPU/CPU、dataset size、run duration、cost、retry limit、network/secret policy 或完整代码。
- **Evaluation Contract**：Med-AI Bench 从六种 modality、19 tasks 各选三篇论文并分 easy/medium/hard，
  每篇构造三种 input mode，共 171 cases/57 papers；但为加快执行又对数据随机子采样，未给 seed、比例
  或 manifest。Idea 由 LLM+三位 experts 按六维 Likert 评；implementation fidelity/completeness 由两个
  LLM judges；57 instances 的 code execution 由 human quantitative check；manuscript study 只在 diabetic-
  retinopathy classification 上比较 5 篇生成稿与 MICCAI/BIBM/ISBI 各 5 篇，10 位 experts 评分，并用
  Stanford Agentic Reviewer 复评。
- **Baselines / Ablations / Sensitivity / Overhead**：baseline 是 GPT-5 与 Gemini-2.5-Pro，在“identical
  input”下比较，但系统本身也使用 GPT-5，增加 retrieval、roles、tooling 与 iterative execution；论文
  没有 matched model-call/token/tool/wall-clock/compute budget，也没有拆分 domain retrieval、co-reasoning、
  ethics gate、executor refinement 或 composer 的消融。三位 idea experts、两位 LLM judges 与十位
  manuscript experts 的 agreement/calibration 未完整报告。
- **What the Evidence Proves**：论文给出一个 domain-constrained research workflow 和多层 evaluation
  design；公开结果支持在作者构造的 benchmark、judge 和 execution criterion 下，完整系统优于两个
  direct-LLM baselines。它也清楚暴露 research artifact 从 idea 到 code、run 再到 prose 的 lineage 问题。
- **What It Does Not Prove**：训练完成、loss 下降和 weights 产出不证明算法忠实、结果正确、统计有效、
  临床可用或可独立复现；manuscript judge score 和一次 ICAIS acceptance 不证明 MICCAI-level science。
  不证明 role decomposition、clinician persona 或 ethics prompt 具有真实 domain authority，也不证明
  general-purpose autonomous scientific discovery。未公开 artifact 使 headline 结果无法独立重放。
- **Limitations / Threats to Validity**：作者承认设计过度复杂会在实现时隐式简化，evaluation 仅在
  predefined datasets，缺跨域/OOD，generated methods 未稳定达到 SOTA。额外威胁包括 benchmark paper
  依 citation rank/subjective difficulty 选择、随机 data subsampling、同源 GPT-5 candidate/judge blind
  spots、非 matched baseline workflow、单一 manuscript task、Likert ceiling/style bias 与 publication
  selection。Ethics reviewer 只检查报告/声明，不能替代 IRB、consent、license、privacy 或 clinical safety。
- **Trade-offs / New Failure Modes**：domain evidence 与 toolboxes 提高可执行性和 traceability，代价是
  更长 critical path、更多 correlated agents、检索污染、dependency drift、judge cost 和 artifact state。
  clinician/engineer consensus 可能是同模型的 correlated confidence；iterative debugging 会把“能跑”
  优化成 proxy；composer 可能为已有 artifact 生成过度自信的 narrative；伦理 policy 过期或缺少真实
  authority 时会产生 false assurance。
- **Where Previous Design Still Applies**：复现已有方法、风险高、数据不可外发、evidence 冲突或结论
  需要临床/统计/伦理责任时，应保持 human-owned plan、approval、analysis 与 independent replication；
  evaluator 明确、artifact 开放的小型工程实验可用 single agent + deterministic tests，避免多 Agent
  coordination tax。
- **Evolution Relationship**：`Direct Evolution`：generic research assistant → end-to-end AI-scientist
  workflow → domain evidence/tool schema → clinician/engineer decomposition + ethics gate → graded autonomy；
  与 Ch62 claim provenance、Ch69 production contract、Ch77 durable workflow、Ch78 responsibility
  decomposition 是 `Layering / Dependency`，不是“domain persona 自动等于 domain authority”。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch62 Evaluation、Ch69 Production Best
  Practice、Ch77 Workflow、Ch78 Multi-Agent。Ch62 已有 run→claim provenance、judge calibration、
  executable≠ground-truth；Ch69 已要求 artifact/evidence/security/recovery contract；Ch77 已拥有 research
  loop、approval 与 independent replication；Ch78 已说明同源 roles 的 correlated error。论文提供的是
  domain case 和版本事实，没有补出这些章节尚缺的长期机制。
- **Integration Decision**：`No Change — Already Covered (Provisional; Historical Books Gate Closed)`。
  现有 Ch62/69/77/78 已完整覆盖可沉淀的机制；benchmark 数字、产品式 autonomy claim 与缺 artifact 的
  implementation 不进入 Books。若将来公开可重放 benchmark/runtime，并证明 domain-specific gate 的
  独立增益，再重新评估。现在不修改 Books。
- **Open Questions**：何时公开 immutable code、container、benchmark manifest、prompts、generated
  manuscripts 和 full run logs？怎样把 IRB/license/privacy/clinical approval 变成真实外部 authority，
  而不是 LLM reviewer？在 matched GPT-5 calls、tokens、tool/runtime cost 下，增益来自哪个 component？
  如何用 independent replication 和 statistical review 验证“能跑”之后的 scientific validity？

### GEMS: Agent-Native Multimodal Generation with Memory and Skills — 23/30

- **Candidate / Week / Score**：GEMS；2026-W14；23/30。
- **Source Family ID / Type**：`GEMS-MULTIMODAL-ITERATIVE-GENERATION`；arXiv paper + official project
  page + author repository + core Agent implementation。第三方榜单不作机制证据。
- **Event Date / Revision History**：arXiv 只有 v1，2026-03-30。当前作者仓库 main 有 8 commits，
  无 tag/release；它用于核验公开实现边界，不被倒写成 2026-03-30 的 immutable artifact。
- **Access and Full-read Coverage**：已读 metadata、Abstract、Introduction、Related Work、完整 Agent
  Loop/Memory/Skill 方法与公式、九类任务的 setup/results、loop/memory/skill/efficiency ablations、
  prompts、evaluation/baseline details、完整结果、qualitative cases、Limitations 与 Conclusion；核对官方
  项目页、README、`agent/GEMS.py`、inference/evaluation 入口和 release 状态。公开仓库只完整提供
  CREA/ArtiMuse evaluation code，其余任务要求采用官方设置。
- **Original Problem**：通用图像生成器在多约束 prompt 和专业下游任务上容易漏条件；one-shot rewrite
  没有反馈，last-only refinement 丢失较早失败，完整轨迹直接堆入 context 又增加冗余；每个专业任务
  单独编排 workflow 还会形成不可复用的孤岛。
- **Why Previous Design Was Reasonable**：one-shot generation、有限 random search 和 last-result retry
  状态少、延迟低、无需维护 verifier/memory/Skill registry；当 prompt 简单、generator 已强、judge
  不可靠或单次生成成本高时，它们仍比五轮 agent loop 更可控。任务专用 workflow 在 schema、tool 和
  evaluator 真正不同的高风险场景，也可能比通用 prompt Skill 更安全。
- **Changed Constraint / Principle**：复杂 prompt 让“整体好不好”不足以定位失败，长 trajectory 又让
  context budget 成为运行时约束。长期原则是把目标拆为可验证 criteria、把 raw evidence 与 derived
  summary 分层，并只在命中任务时加载专门知识；这些状态仍必须由 runtime 而非模型自述来治理。
- **Mechanism**：Planner 从 manifest 选至多一个 Skill 并重写 prompt；Decomposer 从原始用户 prompt
  生成原子 yes/no criteria；Generator 产图；Verifier 对每项返回二元判断。全通过则 early stop，否则
  Refiner 结合当前 prompt/image/feedback、thought 与历史生成下一 prompt；达到五轮上限时按通过项总数
  返回 best image。Memory 保留每轮 prompt/image/verification，并把冗长 thought 压缩为短 experience；
  Skill 只常驻 name/description，命中后加载完整 `SKILL.md`。
- **State Ownership / Control and Data Flow**：理想 runtime 应分别拥有 immutable user intent、criterion
  schema/version、generation artifact、verdict/evidence、attempt lineage、derived experience、Skill digest
  与 stop/budget state。公开核心代码实际把 `attempt_history` 保存在进程内 list，将 image bytes、passed/
  failed criteria 和模型 summary 传回下一轮；没有 durable ID、transaction、crash recovery、TTL/delete、
  supersession 或 rollback。因此论文的“persistent memory”只能解释为本次 run 持续可见，不能外推为
  跨进程/跨会话存储语义。
- **Implementation Details**：论文用 Kimi-K2.5 作为 MLLM，Z-Image-Turbo 6B 与 Qwen-Image-2512 20B
  作为 generator，最大五轮，并提供 Creative Drawing、Aesthetic Drawing、Text Rendering、Spatial
  Intelligence 四个 Skill。当前代码以最多 10 个线程并行 criterion verification，通过
  `"yes" in answer and "no" not in answer` 解析结果；Planner/Decomposer/Verifier/Refiner/Compressor
  共享同一 MLLM family，Skill manifest/markdown 通过 prompt 与 regex 使用，不含签名、权限或 sandbox。
- **Evaluation Contract**：主流任务为 GenEval、GenEval2、DPG-Bench、OneIG、WISE；专业任务为
  LongText、SpatialGenEval、CREA、ArtiMuse。baseline 包括 Rewrite、Promptist、5-way random search、
  最多三轮 Maestro 和最多五轮 CRAFT。GenEval2 ablation 在 Z-Image-Turbo 上取三次运行平均；论文
  未披露 GPU、API/model snapshot、token/call cost、seed、wall-clock、并发、tail latency 或 SLO。
- **Baselines / Ablations / Sensitivity / Overhead**：作者报告 GenEval2 从 base 31.0 到 loop 52.4，
  再加 memory 9.0、Skill 2.1 到 63.5，并明确 loop 部分收益来自多次采样；memory 分解显示 prompt+
  feedback、images 和 compressed experiences 各有贡献，full thought 增益有限。early stop 将有
  memory/Skill 时的平均轮数从上限五轮降到 2.80。没有 verifier independence/calibration、criteria
  weighting、Skill interaction、compression fidelity、matched token/call/wall-clock 或多 seed sensitivity。
- **What the Evidence Proves**：在作者披露的两类 generator、指定 MLLM、最多五轮和九类 benchmark
  contract 下，criterion-wise feedback、历史 artifact 与按需 domain instructions 的组合优于作者实现的
  baselines；ablation 支持“只有最后一步”不是唯一可行的 refinement state。当前代码也证实论文描述的
  主要控制流确实存在。
- **What It Does Not Prove**：不证明 6B generator 在 matched harness/judge/compute 下普遍超过闭源模型，
  不证明通过全部自生成 criteria 等于满足完整用户意图，也不证明同源 MLLM verdict 是独立 ground truth。
  best-by-count 不证明高优先级约束没有退化；进程内 list 不证明 durable memory；markdown prompt file
  不证明 Skill 可治理、可复现或安全。
- **Limitations / Threats to Validity**：作者承认 inference latency、预定义 workflow、仅覆盖 image、
  generator 缺 image-editing 能力。额外威胁包括 decomposition omission、二元 judge/style bias、脆弱的
  yes/no 字符串解析、同源角色 correlated error、criteria 等权、公开 evaluation code 不全、current-main
  artifact drift，以及不同模型/公开榜单的 evaluator 与 compute contract 不匹配。
- **Trade-offs / New Failure Modes**：细粒度 feedback 提高可诊断性，却新增 criterion drift、false pass/
  fail、等权优化和 verifier cost；raw image + summary 保留更多历史，却增加 context/storage/privacy 成本，
  derived experience 还可能压缩掉关键反例；按需 Skill 降低常驻 context，却新增路由错误、版本漂移、
  prompt injection、权限和撤销问题；多轮 search 提高成功机会，也增加 tail latency 与 correlated retry。
- **Where Previous Design Still Applies**：简单 prompt、强 generator、严格 latency/cost budget、弱或不可
  校准 verifier、隐私敏感图片以及缺少 durable state owner 时，one-shot / bounded random search / human
  review 仍成立；需要专业 tool/schema/authorization 的任务不应被单个 prompt Skill 替代。
- **Evolution Relationship**：`Direct Evolution`：one-shot generation → random/rewrite search →
  criterion-wise iterative refinement → raw artifacts + compressed experience → on-demand Skill；与 Ch73
  memory lifecycle、Ch76 verifier/reflection loop、Ch80 Skill governance 是 `Layering / Dependency`，不是
  generator architecture 的直接替代，也不是多个同源 role 自动形成独立 multi-agent evidence。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch73 Memory、Ch76 Reflection、Ch77 Workflow、
  Ch78 Multi-Agent、Ch80 Agent Platform。Ch76 已有 constraint-wise audit、structured feedback、stop/budget、
  verifier independence；Ch73 已有 raw archive 与 derived summary、provenance/version/rollback；Ch80 已将
  Skill 定义为带 digest、permission、evaluation、revocation 的 governed artifact；Ch77/78 已覆盖 durable
  state 与 correlated roles。GEMS 提供具体案例，但没有补出新的长期机制。
- **Integration Decision**：`No Change — Already Covered (Provisional; Historical Books Gate Closed)`。
  保留 Source Review 与 evidence limits，不复制 benchmark 或版本实现到 Books。若未来 artifact 提供
  independent verifier calibration、durable memory schema、versioned Skill lifecycle 或新的机制证据，再
  重新评估；现在不修改 Books。
- **Open Questions**：怎样从自然语言 criteria 构造带优先级和 coverage guarantee 的 EvalSpec？verifier
  与 generator/decomposer 同源时如何量化 correlated blind spots？experience summary 如何携带 source
  artifact ID、uncertainty 与 supersession？Skill 如何加入签名、ACL、sandbox、version、rollback 与
  canary evaluation？在 matched calls/tokens/wall-clock 下，各 component 的真实增益和 tail cost 是什么？

### Terminal Agents Suffice for Enterprise Automation — 24/30

- **Candidate / Week / Score**：Terminal Agents Suffice for Enterprise Automation；2026-W14；24/30。
- **Source Family ID / Type**：`ENTERPRISE-AGENT-INTERACTION-SURFACE`；arXiv preprint revisions +
  appendix prompts/evaluation contract。作者承诺 acceptance 后公开 framework、datasets、environments、
  documentation 与 traces；review 时未发现可重放的官方 code release，不能把承诺当作 artifact。
- **Event Date / Revision History**：v1 2026-03-31，v2 2026-04-03，v3 2026-08-05。W14 事件以 v1
  归档；v2 同周，v3 是后续纠偏/扩展证据。v3 将 MCP agent 更准确地改称特定 `tool-use` catalog，
  新增 generic API-call、open-weight、terminal-first browser fallback、formal limitations、reproducibility
  与 safety；这些不能倒写成 v1 当周已经存在的 ablation。
- **Access and Full-read Coverage**：已读 v1 的 51 页正文与全部 appendices：Related Work、StarShell、
  three-paradigm setup、main/documentation/Skill experiments、failure analysis、single-vs-multi/hybrid、task
  generation、validators、tool-error taxonomy、完整结果、task/tool lists、prompts 和四个 trace cases；并读
  v2 metadata 及 v3 的 revised claims、generic API ablation、open-weight study、limitations、uncertainty、
  ethics/safety 与新 appendix。OpenReview PDF 可检索但当前受 browser challenge，未作为额外证据。
- **Original Problem**：enterprise Agent 需要在 GUI 的通用可达性、curated tool 的结构/治理和直接 API
  的表达力之间选择 interface。GUI trajectory 长且 observation 大；窄工具 catalog 可能漏 operation/
  fields；直接 shell/API 又扩大 action surface。问题不是“哪个框架名字最好”，而是把 action vocabulary
  的粒度、可达性、状态外置与控制边界放在哪里。
- **Why Previous Design Was Reasonable**：GUI 保留 human-visible/rendered/session state，不要求 API parity；
  typed domain tools 压缩探索、限定 schema/scopes，并让权限、审批和审计更直接；单 Agent 避免 planner/
  executor coordination tax。它们在 UI-only tasks、弱模型、高风险写操作和稳定 workflow 中仍然合理。
- **Changed Constraint / Principle**：当平台已有 expressive API、任务要求任意 filtering/payload/operation，
  每个 endpoint/field 都预先包装成窄 tool 会产生 coverage debt。长期原则是按 workload 选择最小但足够
  expressive 的 interface，并将 expressivity 与 authority 分离：general API surface 不等于 broad credential。
- **Mechanism**：StarShell 只给 model terminal + filesystem，由它以 `curl`/script 发现和组合 platform
  API，文件系统承载 docs、intermediate data 和可复用 Skill。对照组使用 Playwright web actions 或
  off-the-shelf MCP narrow-tool catalogs；hybrid 同时给 terminal/browser；planner-executor 把 schema 探索
  与执行分开。v3 新增一个单一 typed `api_call(method,path,body,query)`，无 shell/filesystem，用于分离
  “flexible API request”与“terminal substrate”。
- **State Ownership / Control and Data Flow**：task/environment owner 提供 isolated platform snapshot、
  credentials、docs 与 deterministic validator；model 提出 command/API/browser action；sandbox/runtime
  执行并返回 observation；filesystem 保存 task scratch 与跨任务 Skill；validator 比较 before/after live
  state 或 final answer。生产实现应让 workflow 拥有 action identity、idempotency、approval、side-effect
  evidence 和 rollback，credential proxy 拥有 authority；shell、model 和 Skill 都不是 authority owner。
- **Implementation Details**：v1 基于 OpenAI Agents SDK/LiteLLM，在 containerized ServiceNow、GitLab、
  ERPNext 实例上运行；模型为 Claude Sonnet/Opus 4.6、GPT-5.4 Thinking Medium、Gemini 3.1 Pro，默认
  sampling，provider endpoints 分别经 Bedrock/Azure/Vertex。每 task reset environment；command timeout
  为 30 秒。Skill experiment 按固定 dataset 顺序保留 agent-written files；其他实验不跨 task 保留状态。
  v3 明确当前 harness 把 auth headers 放在 agent 可读 env vars 中，尚未实现 credential proxy。
- **Evaluation Contract**：729 个 single-session tasks：ServiceNow 330、GitLab 192、ERPNext 207；指标为
  deterministic post-state/final-answer binary success、token-priced inference cost，附 tool calls 与 wall-clock。
  v1 main matrix 比较四个 proprietary backbones；v3 generic API ablation 只测两个 Claude models，
  open-weight extension 测 Gemma-4-31B-it 与 Qwen-3.6-27B。没有 production users、multi-session/cross-
  platform workflow、human approval、SLO、真实 credential policy 或 failure severity contract。
- **Baselines / Ablations / Sensitivity / Overhead**：v1 包含 all tasks 与 444-task feasible subset、docs on/off、
  sequential Skill on/off、single-vs-planner/executor、terminal/web/hybrid。v3 generic API-call ablation恢复大部分
  terminal-vs-narrow-tool gap，说明主要变量是 interface granularity；targeted repeats 只覆盖 Gemini/
  ServiceNow 与 GPT-5.4/GitLab 的三个 runs，全矩阵未重复。Skill 顺序固定且只用 Sonnet，存在 curriculum/
  leakage、write-policy 和 earlier-task exposure confound；docs 结构与 pretraining familiarity 也未完全分离。
- **What the Evidence Proves**：在披露的三平台、任务分布、模型、server/tool catalogs 与 pricing contract
  下，direct programmatic interfaces 通常以较短 observation/action path达到较好的 success/cost；窄 catalog
  的 operation/field coverage 是明确 bottleneck。v3 的单一 generic API tool 支持“主要收益来自 flexible
  request surface，不是 shell 本身”；filesystem 对大中间态、本地 transform、batch 与多协议仍有独立价值。
- **What It Does Not Prove**：不证明 terminal 普遍优于 typed tools/browser，不证明 MCP protocol 导致
  低分，也不证明 729 个 sandbox tasks 代表 production enterprise automation。binary success 未判断错误写入、
  partial side effect、权限越界和 failure severity；作者未公开 artifact，无法独立重放。Skill gain 不证明
  自动写入的经验可信、安全或跨版本有效；多 Agent 对照也只覆盖同模型 planner/executor。
- **Limitations / Threats to Validity**：off-the-shelf MCP servers 在 v1 中大量缺 tools/fields，主比较不完全
  matched；v3 虽补 generic API control，发生在事件四个月后。任务是 single-session、三平台，API/UI
  parity、model pretraining familiarity、文档结构和 task mix 都影响结果。定价会随 provider 变化；default
  sampling 与有限 repeats 限制小差异；web observation/token accounting、Skill order 和未发布 traces 也
  影响复现。作者承认未测 adversarial tasks，当前 auth headers 对 agent 可见。
- **Trade-offs / New Failure Modes**：越通用的 interface 越少 coverage debt，却把 endpoint discovery、
  payload construction、protocol handling 与错误恢复交给 model，并扩大 credential blast radius；越窄的
  typed tools 越易验证/授权，却可能丢 fields、组合性和新 API。filesystem/shell 提供 scratch、batch 和
  escape hatch，也引入 command injection、secret exposure、untrusted Skill persistence 与 local artifact
  lifecycle。browser 看见 rendered state，却增加长 trajectory、routing error 和 observation cost。
- **Where Previous Design Still Applies**：高风险、稳定的业务 operation 应优先 typed domain tools +
  semantic validation；UI-only/session-bound/rendered state 使用 browser；只读、可恢复、大规模 transform 或
  API coverage 快速变化时 generic API/terminal 更合理；短、顺序清晰任务保持 single agent，只有 schema
  探索与执行确实可分时才增加 planner。
- **Evolution Relationship**：`Direct Evolution`：large narrow tool catalogs → one flexible typed API tool →
  terminal/filesystem for scratch, batch and protocol escape → terminal-first with bounded browser fallback。
  与 MCP 是 `Layering / Dependency`：MCP 能承载窄工具或 generic API，协议本身不决定 granularity；与
  Security 是 `Principle Reuse`：authority 应绑定 credential/proxy/policy，而不是 shell command name。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch68 Security、Ch74 Tool Calling、Ch77 Workflow、
  Ch79 MCP、Ch80 Agent Platform。Ch74 已有 typed contract/authorization 和“agent-friendly tool 不等于
  CLI wrapper”，但缺少 narrow-domain↔generic-API↔terminal/filesystem↔browser 的完整 design continuum；
  Ch79 已明确 MCP 不决定 tool semantics；Ch68/77/80 已拥有 credential、side-effect、state 与 governance。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate
  Closed)`。Gate 通过后由 Ch74 补足 interface granularity、API parity、escape hatch 与 coexistence；
  Ch68/79/80 仅作短 handoff。不沉淀模型排名、成本 headline，也不把 v3 机制倒写为 W14 v1 事实。
- **Open Questions**：怎样按 task risk/coverage/volume 选择 narrow tool、generic API、terminal 或 browser？
  generic API 如何保留 typed policy、field-level authorization、idempotency 与 audit？Skill 顺序应如何随机化并
  防跨 tenant/版本污染？在公开 artifact、matched server coverage、failure-severity 和 long-horizon contract
  下，interface granularity 的结论是否仍成立？

### HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention — 27/30

- **Candidate / Week / Score**：HISA；2026-W14；27/30。
- **Source Family ID / Type**：`HISA-HIERARCHICAL-SPARSE-INDEX`；arXiv paper + HTML revisions +
  author artifact。
- **Event Date / Revision History**：arXiv v1 2026-03-30，v2 2026-04-01，v3 2026-04-06。
  本周事件以 v1 归档；v3 仅用于核验演进，不能把后续实验倒写成 v1 当周事实。
- **Access / Full-read Coverage**：已读 v1 与 v3 metadata、Abstract、Introduction、Related Work、
  DSA background、完整方法与公式、复杂度、Implementation、全部主实验、NIAH/LongBench、
  sensitivity、Discussion/Limitations、Conclusion、算法 appendix 与实验设置；核对公开仓库。
- **Original Problem**：DSA 的 Sparse MLA 只读取 top-k token，但 indexer 仍为每个 query 扫描
  全前缀，layer-level indexing 仍呈二次增长；长上下文下，找出稀疏位置本身会成为主要成本。
- **Why Previous Design Was Reasonable**：flat token scoring 保留 query-specific、细粒度选择，
  直接输出 Sparse MLA 所需 token IDs，不引入 block proxy 的信息损失；在较短序列或 indexer
  尚非瓶颈时，它的简单性和精确度仍有价值。
- **Changed Constraint / Principle**：当 L 增长、Sparse MLA 已把读取降到 O(Lk) 后，indexer 的
  O(L²) 不再可忽略。核心原则不是放弃细粒度选择，而是用便宜表示缩小昂贵精确评分的候选域。
- **Mechanism**：把 prefix 按 B 个 token 分块，对 indexing keys 做 mean pooling；query 先对
  L/B 个 block representatives 粗排并取 top-m，再只在 mB 个候选 token 上执行原始 DSA score，
  最终仍输出 top-k token IDs。要求 mB≥k；当 t≤k 时走 dense，当 k<t≤mB 时等价于原始 DSA，
  t>mB 才发生 hierarchical pruning。
- **State Ownership / Control and Data Flow**：pooled block indexing keys 可随 KV cache 增量维护，
  属于 serving-side derived index state；每个 query 的 block/token selection 是 ephemeral state；
  downstream Sparse MLA 与 KV layout 不变。论文接口兼容性不等于 production runtime 已实现
  cache invalidation、prefix sharing、continuous batching 或 recovery semantics。
- **Implementation / Complexity**：每 query indexing 从 O(L) 变为 O(L/B+mB)，每 layer 从
  O(L²) 变为 O(L²/B+LmB)。v1 使用 TileLang DSA reference；主要 kernel 测试为 NVIDIA A100，
  query chunk 1024、B=128、m=64、k=2048，长度 4K～128K。
- **Evaluation Contract / Revision Drift**：v1 报告约 32K 2×、128K 4× 的 indexer kernel
  speedup，并用 DeepSeek-V3.2 NIAH/LongBench、DeepSeek-V2-Lite IoU/sensitivity 检查质量。
  v3 改为 A100、q_len=1024、k=2048、B=128、最高 64K，并报告 4:1 sparsity 2.16×、固定
  8K budget 3.75×；模型扩为 DeepSeek-V3.2 与 GLM-5。v3 appendix 说明 vLLM online serving、
  FP8、定制 RULER、lm-eval，以及默认 concurrency=20、GLM 因 OOM 对部分任务降到 1/2。
  两版数字不能混合引用。
- **Baselines / Ablations / Sensitivity**：与原始 DSA indexer 比较，检查 block size、selected
  blocks、token overlap/IoU 和长上下文任务；v1 未提供与所有 intra-block compression 方案的
  直接系统级对照，也没有端到端 TTFT、吞吐、continuous batching 或 speculative decoding
  联合实验。
- **What Evidence Proves**：在披露的 A100 kernel contract 下，hierarchical index 减少 indexer
  工作并随长度扩大收益；在所测模型与任务上，质量接近 baseline。它支持“稀疏 attention 必须
  把 discovery/index cost 纳入总账”的系统结论。
- **What It Does Not Prove**：不证明所有 topology/hardware/model 都有同等收益，不证明 mean
  pooling 始终保留重要 token，也不证明 kernel speedup 自动转化为在线 serving SLO 改善。
- **Trade-offs / New Failure Modes**：mean pooling 可能淹没 block 内 outlier token；固定 block
  边界与语义边界错位；B、m 与 k 新增质量—计算调参面；derived index 带来更新、一致性与
  prefix-sharing ownership 问题。更强 coarse representation 又会增加 index cost。
- **Where Previous Design Still Applies**：短序列、indexer 非瓶颈、对孤立 token recall 极敏感、
  或缺少可靠 block-state lifecycle 的 runtime，仍可选择 flat DSA；dense attention 仍是短上下文
  和高密度依赖的合理分支。
- **Evolution Relationship**：`Direct Evolution`：dense scan → flat token-level sparse index →
  block coarse filter + token refinement；并与 serving KV/prefix state 构成 `Layering / Dependency`。
- **ROADMAP / Chapters Read / Existing Coverage**：主 owner Ch39，handoff Ch22；已读 Ch22、
  Ch39 及其相邻上下文。Ch39 已要求把 discovery、selection、index-build 成本算入 sparse
  prefill，Ch22 已有 DSA 演进；HISA 新增的是具体的两级索引机制、状态边界与 revision-aware
  evaluation contract。
- **Integration Decision**：`Refine — Existing Argument (Provisional; Historical Books Gate Closed)`。
  Gate 通过后在 Ch39 强化两级 index evolution，在 Ch22 仅增加短 handoff，不复制论文摘要。
- **Open Questions**：如何与 paged KV、prefix cache、chunked prefill 和 continuous batching 共同
  维护 pooled keys？block boundary 与 semantic segmentation 的质量差异如何？端到端 TTFT、
  throughput、tail latency 与 memory overhead 在相同 SLO 下是否仍受益？

### Kernel-Smith: A Unified Recipe for Evolutionary Kernel Optimization — 28/30

- **Candidate / Week / Score**：Kernel-Smith；2026-W14；28/30。
- **Source Family ID / Type**：`KERNEL-SMITH-EVOLUTIONARY-KERNEL-SEARCH`；arXiv paper +
  author repository + merged SGLang / LMDeploy pull requests。
- **Event Date / Revision History**：arXiv v1 2026-03-30，v2 2026-04-23。本周按 v1 归档；
  v2 用于识别 revision，不能把后续材料倒写成 W14 首发事实。
- **Access / Full-read Coverage**：已读 metadata 与 revision history、Abstract、Introduction、
  Related Work、完整 Agent/evaluator/training 方法、实验协议、NVIDIA/MetaX 结果、三项真实案例、
  Conclusion 与 prompt appendix；核对作者仓库以及 SGLang PR #20778、LMDeploy PR #4345。
  公开仓库仅提供报告、生成 kernels、benchmark/doc 入口，明确不公开模型权重与 Agent code；
  训练数据需邮件申请，因此 artifact reproducibility 不完整。
- **Original Problem**：高性能 kernel 不是“生成一份能编译的代码”，而是在 fusion、tiling、
  layout 与硬件约束组成的非凸空间中持续寻找 correctness-preserving improvement。单条多轮对话
  容易锚定早期实现；错误或有噪声的 timing 又会跨代淘汰好候选、保留伪收益。
- **Why Previous Design Was Reasonable**：one-shot generation、compiler heuristic 与人工局部
  refinement 的状态少、验证链短；对常见算子、成熟 library 或一次性 workload，它们仍比维护
  population、archive 与分布式 evaluator 更便宜、更易复现。
- **Changed Constraint / Principle**：当目标是 hardware/workload-specific kernel 且可自动执行
  correctness 与 timing，额外 test-time compute 的价值取决于能否保持探索多样性和可信 evaluator，
  而不只取决于 base model 的一次生成能力。Evaluator 是 executable specification，也是搜索状态
  的事实 owner。
- **Mechanism**：OpenEvolve-style population/archive 同时采样 top-performing 与 feature-diverse
  candidates；feature space 包含 kernel complexity 以及 compile/correctness/speed 组合分数。
  每轮 evaluator 返回编译状态、数值一致性、runtime、hardware metadata 与 error log，模型据此
  生成下一变体。训练侧把长 trajectory 压缩为局部 improvement samples：首个 PyTorch→Triton
  translation 保留正确样本，后续 Triton→Triton edit 只保留正确且 speedup>1 的样本；RL 从
  40 轮 teacher evolution 中选择 best steps，以 parent-relative speedup 作为 GRPO reward。
- **State Ownership / Control and Data Flow**：task specification 与 reference implementation 由
  evaluation service 拥有；archive 拥有 candidate code、lineage、feature 与历史指标；worker 只
  执行 backend-specific compile/test/profile；model proposal 是不可直接部署的候选 artifact。
  流程为 reference + sampled parents + feedback → proposal → compile/hack detection → correctness
  → stable timing → archive selection → next generation → upstream tests/review/merge。
- **Implementation Details**：NVIDIA 路径生成 Triton，MetaX 路径生成 MACA；backend abstraction
  将 task、orchestration 与 metrics 同 compiler/runtime 分开。测量先 warm-up，再重复并剔除
  outlier，并用 CUDA Graph 降低 launch variance；论文称波动控制在 1% 内。runtime detector
  阻止直接调用 native PyTorch 的明显 reward hacking，但“只改 trivial elementwise op”等工程
  无价值优化仍需额外规则或人工判断。
- **Training Contract**：从公开 GitHub 代码静态抽取并归一化 59K `nn.Module`、20 个 functional
  families，embedding/graph 去重后由 LLM 补测试并执行过滤；trajectory 由
  DeepSeek-V3.2-Speciale 和 cluster-seeded expert tasks 合成，最终 SFT 超过 200K 单步样本、
  context 64K。RL 的 cluster-seeded tasks 用 Gemini-3.0-pro 演进 40 轮，每项采样 8 个 GRPO
  candidates。论文未披露 optimizer、learning rate、batch、GPU、训练时长、总 token 或成本。
- **Evaluation Contract**：所有模型进入相同 40-round Agent，temperature=0.6、top-p=0.95，
  input/output 各上限 32K；每个 module 单元测试 100 次。KernelBench 分 Level 1/2/3，指标为
  hack-detected correctness、`fast_1` 与把 speedup<1 置零后的平均 speedup；MetaX 使用 45 个
  CUDA→MACA operators。论文未完整披露 NVIDIA GPU 型号、Triton/CUDA/PyTorch/driver 版本、
  correctness tolerance、warm-up/repeat 具体次数、timeout、clock control 与 confidence interval，
  因而 headline model ranking 不能外推。
- **System-level Evidence**：SGLang merged PR 的 H200 isolated metadata kernel 在 batch=32、
  page_size=1、context=8192、pool=1024、1000 iterations 下报告 4.78×；同一 PR 的
  Llama-3.1-8B-Instruct serving latency 在 batch 16～128、input/output 64～2048 的多数切片仅改善
  0.11%～1.75%，且一个切片为 -0.35%。LMDeploy merged routing kernel 在 H200 的 isolated
  contract 下约 1.36×；DeepSeek-V3.2、TP=8、max batch=512、1K～16K 输入/输出的端到端吞吐
  报告 1.85%～3.00%。这些是作者与 upstream PR 的版本化案例，不是通用收益保证。
- **Baselines / Ablations / Sensitivity**：模型比较固定 Agent harness，但没有把 population/archive、
  noise controls、hack detector、teacher/data filtering 各自做完整 factor ablation，也没有与相同
  wall-clock/token/evaluator budget 的 compiler autotuning 或人工专家做严格成本对照。MetaX
  benchmark 规模较小，且输入已有 correctness-verified CUDA reference。
- **What Evidence Proves**：在论文 evaluator 与 40-round search contract 下，稳定执行反馈、
  diverse archive 和 improvement-centric training 可以让收益跨轮累积；两个 merged upstream PR
  证明至少部分候选跨过了目标项目的测试与 review 门槛。isolated→end-to-end 对照直接支持
  “局部 kernel 收益必须经 engine/workload/SLO 重新验证”。
- **What It Does Not Prove**：不证明模型能自治维护 production kernels，不证明 benchmark 排名
  跨 GPU/software/model version 稳定，也不证明生成代码优于成熟 vendor library、compiler 或专家
  实现。merged PR 证明特定 patch 被接受，不证明长期 regression、维护成本或所有 traffic 均受益。
- **Trade-offs / New Failure Modes**：更多 generation/evaluation budget 换取更广搜索，却新增
  evaluator overfitting、measurement noise amplification、reward hacking、archive contamination、
  duplicate candidates、backend drift 和昂贵回归测试。训练只保留高收益 edit 可能丢失失败路径与
  长期信用分配信息；由 LLM 补测试还可能让 candidate 与 evaluator 共享盲区。
- **Where Previous Design Still Applies**：成熟 cuBLAS/cuBLASLt/compiler coverage、动态 shape、
  低调用频率、验证成本高或 correctness oracle 不完整时，通用 library/heuristic 或人工优化仍更
  合理。Evolutionary search 适合稳定、热点、可 sandbox 且有强 executable oracle 的 operator。
- **Evolution Relationship**：`Principle Reuse`：one-shot code generation → conversational local
  refinement → evaluator-driven population search；与 Ch45 的 library/compiler/specialized kernel
  分支、Ch77 的 durable evaluator workflow 构成 `Layering / Dependency`，不是 Agent 对前者的
  `Direct Evolution` 或替代。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch43～46、Ch52、Ch62 与 Ch77；Ch45
  已覆盖 operation descriptor、library heuristic、specialized kernel 与完整 workload contract，
  Ch77 已覆盖 evaluator-driven search 的 lineage/held-out verification。Kernel-Smith 新增的是
  kernel-specific archive state、measurement stability、step-centric training，以及真实 PR 中
  operator evidence 被 Amdahl-like dilution 后的量级边界。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后由 Ch45 吸收 kernel-search/evidence ladder，Ch52 / Ch77 只作短 handoff；不保留
  模型榜单，也不把 PR benchmark 写成通用框架能力。
- **Open Questions**：v2 相比 v1 的实质差异是什么？如何公开重放完整 evaluator、训练数据与
  search budget？archive 如何跨 compiler/runtime/hardware upgrade 失效？系统应怎样为负收益切片、
  数值 corner case 与长期 maintenance cost 设置 promotion/rollback gate？

### Marco DeepResearch: Unlocking Efficient Deep Research Agents via Verification-Centric Design — 25/30

- **Candidate / Week / Score**：Marco DeepResearch；2026-W14；25/30。
- **Source Family ID / Type**：`MARCO-DEEP-RESEARCH-VERIFICATION-CENTRIC`；arXiv paper +
  author inference repository/model entry。
- **Event Date / Revision History**：arXiv v1 2026-03-30；截至核验时无后续 arXiv revision。
- **Access / Full-read Coverage**：已读 metadata、Abstract、Introduction、Related Work、两类 QA
  synthesis、trajectory construction、test-time scaling、SFT/GRPO 公式、全部 evaluation/ablation、
  implementation、Conclusion 与公开仓库的 runner/config/tool/context-management 边界。论文没有
  独立 Limitations/Threats 章节；将未披露项和可由实验观察到的边界单独列出，不替作者补结论。
- **Original Problem**：deep research 的错误会在 data ground truth、teacher trajectory 与 inference
  三个阶段串联传播。只用“teacher 最终答对”的轨迹，会隐藏未检查的中间 evidence；只增加搜索轮数，
  也可能让早期 tool error 与错误假设占满 Context。
- **Why Previous Design Was Reasonable**：单 Agent ReAct、answer-first QA 与固定轮数 search 的状态
  简单、成本低；在答案唯一、检索路径短或有 deterministic oracle 的任务上，额外 verifier 可能只是
  重复计算。强 teacher 直接过滤 final answer 也曾是合成稀缺长轨迹的实用起点。
- **Changed Constraint / Principle**：当问题需要多源、多跳、长 horizon evidence 时，最终 outcome
  不足以定位上游 ambiguity。Verification 应成为数据生产、行为学习和运行时搜索共享但版本化的
  control signal；它必须检查 uniqueness、grounding、constraint satisfaction 与停止条件，而不只
  判断答案文本是否“像对的”。
- **Mechanism — QA Synthesis**：graph 路径先采样目标 entity 与五类 attributes，再 reverse-search
  4～8 个 intermediate nodes；Generator 生成 2～3 条初始约束，Attacker 搜 counterexample，Analyzer
  追加区分约束，最多 10 轮，最后执行 leakage/closed-book checks。Web pipeline 则先构建 evidence
  graph，再由独立 search agent 求解、verification agent 检查 factual consistency、depth、shortcut
  与 alternative answer，并用 diagnosis→revision 修复失败样本。
- **Mechanism — Trajectory / Inference**：training synthesis 使用 main/search/verifier 三角色，分别
  分解、求解与独立 web verification，再压成单 Agent ReAct trajectory；失败轨迹依据 verifier
  diagnosis re-rollout，只保留恢复到正确答案者。Inference 在 degeneration 时执行 `Discard All`：
  删除 tool/reasoning history，仅保留 query/system prompt 后重启；每个 candidate 用 rules + 同一
  Marco agent judge，budget 结束或收敛后做 Joint Verify。
- **State Ownership / Control and Data Flow**：QA generator 拥有 provisional question/evidence graph，
  verifier 输出 acceptance/diagnosis；trajectory builder 拥有 subtask/correction trace；inference
  runtime 应拥有 candidate set、tool-call budget、reset/convergence 和 final selection，不能让模型
  文本自行宣称 budget 或 state 已重置。公开 runner 将 profile、benchmark、model、tools 与 output
  分层配置，并记录 reasoning steps、token usage 与 execution time，但论文没有定义 durable replay、
  evidence digest 或 verifier-version migration。
- **Training / Implementation Contract**：Qwen3-8B + YaRN 128K；超过 12K synthetic QA，另留
  2K+ QA 用于 RL；trajectory teachers 包括 Qwen3.5-Plus、GLM-5、Kimi-K2。SFT 只对 assistant tokens
  计算 cross-entropy；GRPO 用 group-relative binary outcome reward，Qwen-Turbo-Latest 初判、低置信
  样本升级 GPT-4.1。SFT/RL 使用 64×A100、Megatron；Redis page/query cache、exponential backoff、
  async tools/reward pipeline 和独立 WebVisit summarizer。未披露 A100 容量、训练时长/tokens、batch、
  optimizer/LR、GRPO group size/clip/KL、cache hit、网络成本与失败率。
- **Evaluation Contract**：六类 deep-search benchmark；作者运行最多 600 tool calls，temperature
  0.7、top-p 0.95、最大 generation 16,384 tokens。主表混合官方报告分数与作者复现分数，baseline
  的 search provider、page snapshot、tool schema、budget、summary model 与 endpoint 并非全部
  matched；因此跨模型排名不是受控的 model-only comparison。
- **Ablation / Sensitivity**：同量 graph QA 加 uniqueness verification 后，四个切片为 -0.4、+2.3、
  +1.7、+1.3；verified multi-agent trajectory 相对 single-agent trajectory 为 +0.2～+5.2；RL 相对
  SFT 为 +0.8～+6.7。`Discard All + Verify` 相对 RL baseline 的四项作者实验提升较大，但只给组合
  与 `Discard All` 对照，没有 matched-cost 的 independent-verifier、same-model verifier、multi-
  rollout voting、no-reset 等完整 factorial ablation。64K→128K SFT 仅测两个子集，改善 +0.8/+2.3。
- **What Evidence Proves**：在作者的数据、judge、web harness 与 budget 下，显式 verification
  可以改善多个阶段，尤其说明“增加 test-time compute 前先定义可验证进展与 reset/stop control”
  是合理机制。graph QA 的负向切片同时证明 verification 不是无条件单调收益。
- **What It Does Not Prove**：不证明 synthesized answer 唯一性达到形式保证；Attacker 搜不到反例
  只提供有限搜索证据。也不证明同一模型自验证具有独立性，不证明 600 calls 在 latency/cost/SLO
  上可接受，不证明 8B/30B 的表格差异来自模型规模而不是 harness、budget 或 source freshness。
- **Trade-offs / New Failure Modes**：verification 增加 model/tool/judge 成本和 critical path；同源
  generator/verifier 可能共享盲点，judge escalation 会产生 provider/version drift；Discard All 可逃离
  错误轨迹，也会删除仍有效的 evidence/provenance、重复访问页面并触发 non-idempotent tool 风险；
  合成数据的 verifier blind spot 还会同时污染 SFT 与 RL reward。
- **Where Previous Design Still Applies**：短问题、强 deterministic oracle、昂贵/受限工具、不可重复
  side effect 或已有可靠 evidence state 时，应保留 single-pass、局部 repair 或 selective reset；完整
  history 也应在 provenance archive 中保留，而不是物理删除。独立 verifier 只在其增量错误独立性和
  成本经过测量时值得引入。
- **Evolution Relationship**：`Layering / Dependency`：final-answer filtering → intermediate evidence
  verification → verification-shaped trajectories → budgeted verifier-guided search。它与 Ch72 的
  sufficiency/claim evidence、Ch76 的 constraint-wise feedback 和 Ch77 的 durable state/budget 相连，
  不是用后阶段 verifier 覆盖前阶段质量控制。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch72、Ch74～78 与 Ch62。Ch72 已覆盖
  query/compression/verification/stop 联合 policy，Ch76 已覆盖 feedback independence、bounded repair
  与 stopping，Ch77 已拥有 retry/replay/budget state。新证据最适合在 Ch76 强化 verification across
  lifecycle 与 selective reset boundary；Ch72/77 仅需短 handoff，不重复论文框架。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后由 Ch76 吸收“verification as lifecycle control signal”和 reset/provenance trade-off；
  不保留榜单或固定 600-call recipe。
- **Open Questions**：Attacker/Analyzer 的真实 acceptance calibration 与人工 inter-annotator agreement
  是多少？同模型与独立 verifier 在 matched compute 下如何比较？怎样保留 verified evidence 而只
  丢弃污染 reasoning？网页 snapshot、search ranking、judge 与 summarizer version 如何进入可重放 run？

### Combee: Scaling Prompt Learning for Self-Improving Language Model Agents — 28/30

- **Candidate / Week / Score**：Combee；2026-W14；28/30。
- **Source Family ID / Type**：`COMBEE-PARALLEL-CONTEXT-AGGREGATION`；arXiv paper + ACE/GEPA
  implementation families。论文没有独立 Combee repository/tag；当前 GEPA release 后续出现
  “ComBEE-style” extension point，属于 revision follow-up，不倒写成 W14 artifact。
- **Event Date / Revision History**：arXiv v1 2026-04-05；截至核验时无后续 arXiv revision。
- **Access / Full-read Coverage**：已读 metadata、Abstract、Introduction、Background、context-overload
  evidence、三项设计与公式、全部四类实验、ablation/robustness、Related Work、Conclusion、Limitations、
  formalization、distributed-training analogy 与 qualitative appendix；核对 ACE/GEPA 官方仓库和 release
  history，以区分 paper claim 与当前实现。
- **Original Problem**：generate→reflect→update 的 prompt learning 在 batch=1 时串行且慢；直接把
  大量 parallel reflections 一次交给 curator，虽然 token 未超 128K window，仍会把具体、高价值规则
  压成少量 generic advice，使并行度越高、共享 context 越贫乏。
- **Why Previous Design Was Reasonable**：sequential update 保留清楚的 context version 与 credit path，
  小 batch 也让 curator 能逐条吸收细节；在 trace 少、adaptation 不紧急或 consistency 优先时，这一
  旧方案仍比多层 merge 更易审计。naive batching 则是最简单的 wall-clock 并行基线。
- **Changed Constraint / Principle**：当并行 agents 或历史 traces 大量增长，瓶颈从 execution 转移到
  shared-context fan-in。Context capacity 不只受 token limit 约束，还受 curator 的有效选择/压缩能力
  约束；因此需要限制每次 aggregation fan-in，并显式管理信息丢失概率与同步 delay。
- **Mechanism**：Map 阶段用同一 `C_t` 并行产生 trajectories/reflections；Reduce 把 n 项分成
  k≈floor(sqrt(n)) 组，各组先生成局部 update，再合并 k 个 updates。Shuffle 将每条 reflection
  复制 p 次（默认 p=2）后随机分配，给被一次 curator 忽略的信息多次进入不同分支的机会。Controller
  对候选 batch 实测 iteration delay `d(bs)`，估算 `T_epoch=d(bs)N/bs`，拟合 `A bs^-alpha`，在边际
  delay reduction 低于固定 tau（实验为 peak slope 的 1.6%）处选 plateau batch。
- **State Ownership / Control and Data Flow**：worker 只拥有 task-local trajectory/reflection；
  aggregation tree 拥有 intermediate updates；context service 应拥有 `C_t→C_{t+1}` revision、parent
  set、duplicate identity 与 publication gate。论文的同步 iteration 假设让所有 workers 读同一版本；
  future async path 会新增 stale reflection、concurrent merge、supersession 与 rollback 问题。
- **Implementation / Evaluation Contract**：主要 base LLM 为 Together AI 的 DeepSeek-V3.1，另在
  Formula 上测 GPT-OSS-120B；框架为 ACE 与 GEPA。AppWorld 用 90 train tasks/Test-Normal；
  Terminal-Bench 2.0 用 60 条 DeepSeek-3.2 trajectories 训练、29 held-out tasks，Accuracy@1 三次；
  Formula 500、FiNER 1000 samples。Top-K baseline 用 text-embedding-3-large、K=5、batch=50；成本为
  provider API cost。论文未披露 endpoint concurrency/rate limit、网络分布、curator decoding、完整
  prompt/version、重复运行方差（除 Terminal 三次）或自托管 GPU contract。
- **Evidence / Ablation**：naive Formula batch 1→100 时 playbook entries 264→21、accuracy 87.0→72.5；
  FiNER entries 246→11、accuracy 76.0→70.6。AppWorld Combee batch40 用 7 分钟、$1.67，作者报告
  65.8 average，sequential ACE 为 86 分钟、$1.62、58.1；Terminal Combee batch30 为 2.4 分钟、
  $0.17、35.6%，sequential 为 42.4 分钟、$0.24、37.9%。Figure ablation 检查 controller、shuffle、
  subgroup size 与 GPT-OSS transfer，但公开 HTML 没给所有 point 的数值/置信区间。
- **What Evidence Proves**：在这四类作者 workload 中，限制 curator fan-in、增加冗余 exposure 并按
  delay plateau 选 batch，比 naive large-batch aggregation 更能保持质量，且 wall-clock 可下降。它
  证明“并行经验生产不等于可并行的可靠经验合并”是一个真实系统问题。
- **What It Does Not Prove**：不证明 17× 跨 provider/hardware/queue 稳定，不证明更多 playbook tokens
  就是更高质量，不证明 duplicate-and-shuffle 保留的是正确而非错误 reflection，也不证明 ACE/GEPA
  之外的 program/skill/vector artifacts 可直接兼容。`context≈gradient` 仅是 `Explanatory Analogy`：
  文本 update 通常非线性、非交换、非结合，不能像 AllReduce 平均梯度那样推导等价性。
- **Trade-offs / New Failure Modes**：两层 aggregation 增加 curator calls 与 provenance depth；复制
  reflection 增加 cost，并可能放大高频错误；随机 shuffle 带来 run variance；固定 tau/power-law 可能
  在 bursty API、heterogeneous tasks 或 rate-limit 下误选 batch；同步 barrier 会被 straggler 拖慢。
  多个 local summaries 还可能产生冲突、遗漏 minority evidence 或重复 rule。
- **Where Previous Design Still Applies**：少量高价值 traces、强顺序依赖、需要精确 provenance、
  context update 不可安全合并或错误代价高时，sequential/small-batch consolidation 仍是首选。
  Deterministic dedup、typed rule merge 或人工 review 也可能比 LLM hierarchy 更可靠。
- **Evolution Relationship**：`Direct Evolution`：sequential update → naive parallel fan-in → bounded
  hierarchical fan-in + redundant exposure + delay controller；future async merge 是尚未验证分支。
  与 distributed training 只属 `Explanatory Analogy`，与 Ch77/78 属 `Layering / Dependency`。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch72～74、Ch77～78。Ch73 已覆盖 raw
  trajectory→derived memory、provenance、consolidation、supersession 与 delete/rollback；Ch77/78 已
  覆盖 authoritative state 和 coordination tax。Combee 新增的是 parallel write/consolidation 的 fan-in、
  redundancy、synchrony 与 batch-control 机制，主 owner 应为 Ch73。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后在 Ch73 补“并行 consolidation 不等于线性 merge”，Ch77/78 只连接 version/barrier/
  coordination；不保留 17× headline 或固定 tau/p=2 配方。
- **Open Questions**：怎样让 reflection 带 source/result/provenance，使重复与冲突可确定处理？异步 worker
  在读取旧 `C_t` 后提交 update 时用 merge、rebase 还是 reject？quality controller 能否同时观测遗漏率、
  contradiction 与 minority evidence，而不只拟合 delay？当前公开实现如何锁定 paper 的 exact commit？

### AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents — 26/30

- **Candidate / Week / Score**：AgentHazard；2026-W14；26/30。
- **Source Family ID / Type**：`AGENTHAZARD-SEQUENCE-HARM-EVALUATION`；arXiv paper + author project
  page + public dataset/code/10K+ trajectory repository。仓库当前 main 有 16 commits、data/generator/run/
  traces/config，但没有 GitHub release/tag；当前 artifact 可审计，不能直接视为 event-date immutable build。
- **Event Date / Revision History**：arXiv v1 2026-04-03；核验时无后续 arXiv revision。
- **Access / Full-read Coverage**：已读 metadata、Introduction、Related Work、taxonomy、seed generation/
  execution filtering、dataset statistics、全部 experiment setup/results、guard/strategy/multi-step analysis、
  applications、Conclusion、detailed taxonomy/results 与 evaluation/system-prompt appendix；核对 project
  page、dataset/code/trajectory repository 和 release absence，并读 Ch62、Ch68～69、Ch77。
- **Original Problem**：prompt-level refusal/jailbreak 只看局部输入输出，无法捕捉多个表面合理步骤经
  context、tool、file 和 shell state 组合后形成的越权或不可逆副作用；模型回答安全也不等于 agent
  没有通过 framework routing 和权限完成危险动作。
- **Why the Previous Design Was Reasonable**：single-turn classifier/refusal 便宜、低延迟、易部署，
  对显式恶意请求和无工具 chat 仍是必要入口层；tool-level allowlist/sandbox 又能确定性限制部分动作。
  在无持久状态、无外部副作用或每步都独立授权时，完整 trajectory judge 未必值得其成本。
- **Changed Constraint / Principle**：computer-use agent 引入 persistent state、重复 tool use 与实际
  environment mutation，harm 是 action sequence 的函数，不是单条文本属性。Safety subject 应写成
  `model + framework/system prompt + tool router + permission boundary + environment + full trajectory`；
  monitor 只能提供 risk signal，authority 必须在 tool/workflow policy 中执行。
- **Mechanism — Benchmark Construction**：从公开 vulnerability knowledge 与 prior agent-security
  work 建立 10 risk categories × 10 attack strategies；每项包含 task context、executable constraint、
  partial artifact 和 target harmful action。8,000+ seeds 先由 Qwen3-Coder 在 Claude Code/OpenClaw
  sandbox 执行过滤，再由 Gemini-3/GPT-5.4 核验 objective/trajectory alignment，最后人工去重、修正
  taxonomy。保留 2,653 项，平均 decomposition 11.55 steps、10K+ trajectories；分布刻意不均匀。
- **Mechanism — Evaluation**：记录 user inputs、agent responses、tool calls/outputs，Gemini-3-Flash
  在 cumulative `round_1...round_all` 上输出 harmful binary + severity 0～10；ASR 是被 judge 判 harmful
  的比例。另将前 k 个 decomposed task-description steps 拼接给 Llama Guard/Qwen3Guard，测 unsafe
  detection。论文把任务描述 guard 与执行 trajectory judge 分开，这是 sensor placement 的比较，
  不是 end-to-end defense implementation。
- **State Ownership / Control and Data Flow**：benchmark instance 拥有 threat category、strategy、
  expected harmful objective 与 workspace；framework 拥有 context/tool routing；sandbox 拥有可执行
  state；trace store 保存 input/action/output；judge 读取 cumulative trace；生产 authority 应由 workflow
  持有 policy snapshot、action arguments/digest、approval、side-effect/result 和 stop/rollback。论文没有
  实现 per-action deterministic policy、risk accumulation state machine 或 prevention/recovery loop。
- **Evaluation Contract**：framework 为 Claude Code、OpenClaw、IFlow；OpenClaw 每项运行在 Ubuntu
  22.04 / Node 22 Docker，2 CPU / 4GB、无持久 state，Claude Code 为 restricted shell，IFlow 细节较少。
  models 经 OpenAI-compatible API 使用 Qwen2.5/3、Kimi K2/K2.5、GLM-4.6 等。未披露 framework/model
  exact version、provider endpoint、temperature/seed、token/tool/turn/time budget、retry、API policy、
  host kernel/container privileges、run repetitions、cost 或 confidence interval，因此 ASR 只属于作者
  harness。论文正文也未提供 formal Limitations section。
- **Evidence / Sensitivity**：同一 Qwen2.5-Coder-32B 在 Claude Code/OpenClaw/IFlow 的作者 ASR 为
  57.80/64.06/74.70%，支持 framework 是 subject 的一部分；cumulative round 曲线在 IFlow/OpenClaw
  到 round3 大幅上升，但 `round_all` 又低于 round4，显示 judge/context aggregation 并非单调。
  guard detection 随更多 steps 上升，但最佳 full-input 仅 27.03%；没有 benign controls，故不能知道
  specificity/false positives，也不能据此选择 operating point。
- **What the Evidence Proves**：在作者构造、sandbox 和 judge contract 下，局部合理的多步任务能
  诱导公开模型/framework 产生被 judge 视为 harmful 的执行轨迹；同一 backbone 随 framework 改变，
  说明模型 alignment 不能单独代表部署 safety。逐步 trace 比只看首轮暴露更多风险信号。
- **What It Does Not Prove**：不证明 ASR 等于真实成功副作用率；主要 verdict 是 model judge，论文
  没有把目标 condition 全部交给 executable verifier。也不证明任务对正常用户分布的 prevalence，
  不证明 guard 在可接受 false-positive 下无效，不证明某产品/模型当前版本更危险；construction 使用
  同类模型执行筛选还可能选择性保留其易执行模式。项目页的单张 production alert 不是总体 external validity。
- **Trade-offs / New Failure Modes**：完整 trajectory logging 增加隐私、敏感 payload retention 与
  evaluator exposure；累计 classifier 提高 context/cost，也可能被早期 benign steps 稀释。sandbox
  降低真实伤害但改变权限/网络/side effects；仅在最终 judge 判定会错过中途已发生又被清理的动作。
  安全 policy 过强会阻断 legitimate debugging/admin workflow，必须通过 benign paired controls 校准。
- **Where the Previous Design Still Applies**：prompt/input guard 继续负责早期廉价过滤，model refusal
  负责语义层，tool allowlist/least privilege/sandbox 负责确定性边界，human approval 负责高风险例外；
  trajectory monitor 是其上的 stateful detection layer，不替代任何一层。无工具 chat 仍可用 prompt-level eval。
- **Evolution Relationship**：`Direct Evolution`：prompt refusal → cumulative intent detection → full
  action/output trajectory evaluation → executable side-effect/authorization verifier；后两步尚不能互相
  替代。与 Ch68/77 的 least privilege、approval、sandbox、durable state 属 `Layering / Dependency`。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch62、Ch68～69、Ch77。Ch68 已有“Safety
  Evaluation 单位是 Run”与 sensor/authority 分离，是主 owner；AgentHazard 新增 locally-plausible
  sequence、framework-as-subject 与 cumulative-round non-monotonicity 的受限证据。Ch62 只承接 EvalSpec/
  calibration，Ch77 只承接 authoritative action/approval/side-effect state，Ch69 无需重复。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后在 Ch68 refine sequence-level threat model、paired benign calibration 与 executable-effect
  evidence；Ch62/77 仅短 handoff。不写入模型/framework ASR 排名或 guard 的固定阈值。
- **Open Questions**：怎样为每类 harm 定义 deterministic effect/authorization verifier？如何构造
  matched benign twins 计算 specificity、ROC 与业务 cost？同一 immutable model/framework/policy 在
  多 seeds、预算和权限层级下方差如何？trajectory monitor 在何时阻断、如何保留 forensic evidence，
  又怎样避免 judge 本身接触可执行 payload？

### LightThinker++: From Reasoning Compression to Memory Management — 25/30

- **Candidate / Week / Score**：LightThinker++；2026-W14；25/30。
- **Source Family ID / Type**：`LIGHTTHINKER-REVERSIBLE-WORKING-MEMORY`；arXiv v1 paper + author
  repository + general/agentic model、data 与 pipeline documentation。仓库当前 main 有实现与 Hugging Face
  artifact 入口，但没有 GitHub release/tag，不能把当前 commit 自动视为 2026-04-04 immutable artifact。
- **Event Date / Revision History**：arXiv v1 2026-04-04；核验时 abstract history 只有 v1。项目 README
  把发布月份写为 2026-03，不能替代 arXiv first-public timestamp，本周仍按 4 月 4 日归档。
- **Access / Full-read Coverage**：已读 metadata、Introduction/Related Work、LightThinker attention mask
  与公式、LightThinker++ memory action/state machine、trajectory synthesis/pruning/SFT、general reasoning
  与 long-horizon agent 全部实验、Dependency definition、数学推导、training/evaluation/timing appendix、
  failure cases、discussion/conclusion；核对 top-level、general_reasoning、agentic_reasoning README、公开
  model/data 入口与 release absence，并读 Ch22、Ch41、Ch71～74、Ch77。
- **Original Problem**：长 CoT 与 tool/observation history 让每个新 token 或 agent round 继续依赖全部旧
  tokens；简单截断会丢证据，full history 的 active Context、KV capacity、Prefill/Decode 与注意力依赖则
  随 horizon 增长。一次性 summary 又可能把数字、变量绑定或原始网页证据不可逆地抹掉。
- **Why the Previous Design Was Reasonable**：full history 在窗口足够时保留最高 fidelity、无需 memory
  action policy 或外部 archive；固定 token/thought interval 的 gist compression 结构简单、可在标准 SFT
  与定制 attention mask 中训练。在短推理、冗余自然语言或精确回读不重要时，这些方案仍比多轮
  archive/restore 更易实现和测量。
- **Changed Constraint / Principle**：当 logical units 信息密度不均、任务需要 backtracking，固定容量
  bottleneck 会在高密度 step 上永久丢失关键 anchor。应把“何时压缩、何时恢复”建模为显式、可逆的
  working-memory transition；active Context 是 archive 的 projection，不是 source of truth。
- **Mechanism — Implicit Branch**：LightThinker 将 reasoning trace 分段，在每段后插入 cache tokens `C`
  与 resume token `[o]`；压缩阶段的 `C_i` 只看 question、先前压缩表示和当前 thought，生成阶段只看
  question 与压缩历史。训练仍是 next-token prediction，但 attention mask 强制后续 reasoning 依赖 gist
  representation。它压缩模型内部 hidden/KV state，旧细节不可直接恢复。
- **Mechanism — Explicit Branch**：LightThinker++ 把每个 step 实例化为 `I_k=(R_k,Z_k)`，其中 `R_k`
  是 raw reasoning/TAO interaction，`Z_k` 是 semantic summary；`sigma_k in {active, archive}` 决定下一次
  Context 注入 raw 还是 summary。`commit(R,Z)` 创建并归档 step，`expand(k)` 恢复 raw，`fold(k)` 再次
  收起，`answer` 终止。Environment-aware teacher synthesis 在真实压缩后的下一状态继续生成；训练数据
  又按 lifecycle completeness、expand→fold symmetry、anti-jitter 和重复规则过滤，再拆成 state→action SFT。
- **State Ownership / Control and Data Flow**：raw `R_k`、summary `Z_k`、stable step ID、visibility state、
  action log 与 budget 应由 runtime memory service 持有；模型只提出 commit/expand/fold。Context assembler
  根据经过验证的 state 投影下一次 prompt，workflow owner 负责 target existence、transition legality、
  termination、replay 与 recovery。若 raw evidence 没有独立持久化，所谓 reversible expand 只是接口幻觉；
  若 summary 或 ID 可被覆盖，旧 trace 也可能回读到不同事实。
- **Implementation / Training Contract**：general reasoning 使用 Qwen2.5-7B 与 Llama3.1-8B R1-Distill
  backbones；17,315 个初始题由 DeepSeek-V3.2 合成长轨迹，过滤后 13,855 条。LightThinker++ 使用 8×A800、
  max sequence 16,384、3 epochs、batch 32、temperature .7，并对每例三次独立 sampling。Agent branch
  从 Qwen3-30B-A3B-Thinking-2507 全参 SFT；paper 报 8 GPUs、Vanilla max 32,768/global batch 32，
  LightThinker++ max 16,384/global batch 64。当前 repo 说明 Python3.12/CUDA12/PyTorch2.7/FlashAttention、
  general inference batch32，agent default 100 rounds/110,592 reasoning tokens；这些 current-main 配置
  未绑定 event-date tag。
- **Evaluation Contract**：general reasoning 测 GSM8K、MMLU subset、GPQA、BBH subset，指标为
  accuracy、wall time、Peak visible tokens 与作者定义的 Dependency area；Throughput 与 Budget 两种
  token allocation 不能混用。timing 总 concurrency 为 32，但完整 GPU 型号、serving backend、kernel/
  driver、warmup、功耗、queueing、tail latency 与 SLO 未披露。Agent branch 测 xbench-DeepSearch-2510、
  BrowseComp-EN/ZH，以 GPT-5-2025-08-07 judge 计算 Pass@1/Pass@3；paper 写 Google Search API + Jina/
  Qwen-Flash，当前 repo 写 Serper + Jina，说明 harness revision 必须进入 run identity。
- **Baselines / Ablations / Sensitivity**：general baseline 包含 Vanilla、TokenSkip、commit-only
  `LThinker*`、H2O/SepLLM/AnLLM 和 prompting。commit-only 对 Qwen throughput setting 的平均准确率
  53.60，full actions 为 60.02，支持 reversible retrieval 在该 contract 中有增量价值；implicit branch
  也给 cache-size sweep 与 numerical-detail failure。Agent branch比较 base、Vanilla SFT、commit-only 与
  all actions，但 proprietary-agent 行不是 matched model/tool/budget comparison。训练集由 teacher、
  correctness judge 和 lifecycle heuristics共同选择，尚缺等成本 human-verified、random-policy、oracle-
  retrieval、不同 summary quality 与多 seed/置信区间的完整 factorial ablation。
- **What the Evidence Proves**：在作者模型、数据与 harness 中，保留 raw/summary 双形态并允许按需恢复，
  比固定不可逆 compression 更能维持所测任务的 accuracy，同时缩小 active token footprint；论文还提供
  了“压缩节奏应随 logical density 改变”和“working Context 可以是持久 archive 的可逆 projection”的
  有限实验支持。
- **What It Does Not Prove**：不证明模型自主 memory policy 在开放生产 workload 中可靠，不证明 summary
  正确或 step ID/provenance/authorization 已解决，不证明 Dependency 等于实际 FLOPs、HBM bytes 或 SLO，
  也不证明 69.9% Peak/Dep reduction、2.42 accuracy gain、2.5× action efficiency 可跨硬件、模型、search
  provider 与预算外推。论文没有独立 Limitations/Threats section；作者对 context rot、premature stop 与
  semantic denoising 的解释多为机制推断，而非因果 isolation。
- **Trade-offs / New Failure Modes**：每次 commit 要生成 summary 并追加 archive，expand 增加 Prefill/
  tokens，fold/expand 还可能抖动；错误 summary 会成为高频控制状态，错误 target 会恢复无关或敏感 raw
  evidence。模型同时生成 reasoning、summary 与 memory action，三者可能共因失败；raw archive 容量仍
  无界，删除/授权/跨租户隔离、crash recovery、concurrent transitions 与 stale-reference migration 均未
  由论文解决。过强 compression 会触发重复生成，过弱 compression 则退回 full-history 成本。
- **Where Previous Design Still Applies**：短 trajectory、必须精确引用全部历史、side effect 不可重放、
  不允许保留 private raw traces，或 runtime 无法保证 archive identity 时，应继续 full Context、typed
  workflow state、deterministic retrieval 或人工选择。固定 implicit compression 仍适合冗余、低风险、
  训练分布稳定的 within-model reasoning；它不应被 explicit Agent memory 叙事整体否定。
- **Evolution Relationship**：`Direct Evolution`：full history → fixed lossy gist/summary → raw+summary
  dual-form state → model-directed reversible projection；`Layering / Dependency`：Ch71 Context assembly、
  Ch73 working-memory service 与 Ch77 workflow authority；`Principle Reuse`：Ch22/41 的 hidden/KV working-
  set reduction。它不是 durable user memory、KV eviction 或 RAG 的替代物。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch22、Ch41、Ch71～74、Ch77。Ch71 已覆盖
  Context compression loss、source-linked projection 与 identity；Ch73 已覆盖 compact control state +
  exact evidence archive、working memory、provenance、forgetting 和 concurrency，是主 owner；Ch77 已拥有
  authoritative transition/replay。新增缺口是把 reversible visibility state、模型 proposal 与 runtime
  validation、raw archive unboundedness 连成完整机制。Ch22/41 只承接 implicit compression/KV cost。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后由 Ch73 refine“active Context 是 dual-form archive 的受控 projection”及 commit/expand/fold
  failure semantics；Ch71/22/41/77 只短连接。不保留作者 headline、固定 action set 或具体模型榜单。
- **Open Questions**：summary 和 raw artifact 如何共享 immutable ID、ACL、expiry 与 delete propagation？
  如何用 executable evidence 判断 expand 是否真的必要，并校准 model action 的 false-expand/false-fold？
  archive growth、summary drift、Prefix/KV invalidation、crash recovery 与 concurrent transition 的总成本
  如何测量？在 matched hardware/tool/provider/budget 下，收益还有多少来自 trajectory data 而非 memory
  mechanism 本身？

### MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome — 25/30

- **Candidate / Week / Score**：MiroEval；2026-W14；25/30。
- **Source Family ID / Type**：`MIROEVAL-DEEP-RESEARCH-EVIDENCE-PLANES`；arXiv paper + author
  benchmark/evaluator repository + project page。公开仓库包含 query/result schema、factual/synthesis/
  process evaluators、sample outputs 和 attachments，但 GitHub 没有 release/tag，不能把当前 main
  无条件当作 2026-03-30 实验快照。
- **Event Date / Revision History**：arXiv v1 2026-03-30；核验时无后续 arXiv revision。
- **Access / Full-read Coverage**：已读 metadata、Introduction、query construction/privacy、三层
  evaluation methodology、公式、13-system setup、outcome/process/further analysis、Related Work、
  Limitations、data/report statistics、feature/rewrite taxonomy、judge robustness、human study、case-study
  appendix；核对 repository 的 data schema、factual/synthesis/process pipeline、config 与 release absence，
  并读 Ch62/63 及 Ch72/76/77 的相邻职责。
- **Original Problem**：只给 long-form final report 一个固定 rubric 总分，会把“写得完整”“claim
  有外部证据”“研究过程合理”和“报告能回溯到实际过程”混为一谈；静态 text-only synthetic tasks
  还遗漏附件、真实需求分布和知识时效。结果可能流畅，却由浅搜索、重复路径或未记录推断产生。
- **Why the Previous Design Was Reasonable**：final-output rubric 成本低、接口统一，不要求厂商暴露
  private reasoning/tool trace；在短答、确定性 artifact 或只关心交付物的低风险任务中仍是可靠回归
  层。固定 benchmark 也提供跨版本可比性，避免 live web 和动态 rubric 同时漂移。
- **Changed Constraint / Principle**：Deep Research 是多步、异构证据、长报告 workflow；evaluation
  object 必须从一个文本扩为 `query/attachments + report + claims/evidence + process trace`。不同证据面
  应先独立评分，再由 intended use 决定聚合；缺失 trace 不等于零分，web/attachment 冲突也不应被
  二元 fact checker 强制抹平。
- **Mechanism — Dataset**：100 tasks = 65 user-pattern-derived（35 text、30 multimodal）+ 35
  trend-generated text。前者先在受控内部环境过滤敏感内容、替换实体，再按七维分类路由到六类
  difficulty rewrite；后者从 12 topics/36 subtopics 生成 180 项，经 search availability、deep-research
  necessity、no-search baseline inadequacy 三层过滤后人工选 35。两条路径可重跑，但 refresh 会改变
  distribution，因此每次 run 必须锁定 dataset snapshot。
- **Mechanism — Four Evidence Planes**：synthesis 由固定 Coverage/Insight/Instruction-following/Clarity
  加 1～3 个 task-specific dimensions；附件任务先抽 key facts 形成 grounding criteria，再由 judge
  生成 dimension/criterion weights 并逐项 0～10 打分。factuality 将 report 拆成 atomic statements，
  主动检索 web 与 attachments，输出 `RIGHT/WRONG/CONFLICT/UNKNOWN`。process 先把异构 trace 结构化
  为 atomic steps/dependencies/findings，再评 breadth、depth、refinement、critical thinking、efficiency；
  最后分别检查 `Process→Report`、`Report→Process` 与 contradiction handling。
- **State Ownership / Control and Data Flow**：benchmark owner 持有 query/attachment snapshot、rewrite
  lineage 与 refresh generation；evaluator owner 持有 judge model/prompt、generated rubric、criterion
  weights、search/tool config 和 structured-trace transform；system adapter 提供 report 与可观测 process；
  result store 应分别保存 criterion、claim verdict/evidence、process units、双向 alignment 和 missingness，
  不能只留 Overall。公开 repo 的 input schema含 `rewritten_query/response/process/files`，factual pipeline
  还依赖 OpenAI/Serper keys 与 MiroFlow；这进一步说明外部服务版本属于 evaluation identity。
- **Evaluation Contract**：100 tasks、70 text/30 multimodal；2026 年 3 月在各系统 official interfaces
  采集，13 个系统中 3 个只测 text。作者用 GPT-5.1 judge synthesis、GPT-5.2 process、GPT-5-mini
  factuality。仓库 synthesis config 示例 temperature .1、20 workers；论文未披露所有产品的 search
  provider/snapshot、tool schema、call/token/time budget、retries、provider endpoint、成本、完整 sampling
  与 process-export fidelity，因此表格不是严格 matched-compute/model-only comparison。
- **Human / Robustness Evidence**：query validation 用 3 位 graduate-level annotators，作者报告
  validity/non-triviality Fleiss kappa .74～.83、overall precision 92%。judge 重跑只在 30 multimodal
  tasks × 4 systems 做 3 runs，Overall std .3～.6；换 Gemini judge 只测 70 text × 6 systems，绝对
  Overall 上移 13.2～16.9、rank 保持；prompt sensitivity 只测 30 multimodal × 4 systems。human ranking
  只抽 5 queries、5 volunteers、10 systems，报告 Kendall tau .91 / Spearman rho .95。
- **What the Evidence Proves**：在作者 March-2026 snapshot 与 judge/harness 下，四个 evidence planes
  捕获非冗余 failure signatures；尤其 `Process→Report` 高而 `Report→Process` 低，支持“最终报告可能
  超出已记录研究证据”的审计问题。不同 judge 的 rank 稳定但 absolute calibration 大幅漂移，反而
  证明 release gate 不能直接复用未锁定 judge 的绝对阈值。
- **What It Does Not Prove**：不证明 process score 因果预测 outcome；相关性可能由系统规模、trace
  verbosity 或同源 judge 共同造成。不证明未记录 trace 等于没有推理，不证明 `CONFLICT` 中哪一方正确，
  不证明 100 tasks 覆盖生产分布，也不证明作者系统的榜首来自模型而非 harness/budget。动态 rubric、
  live search 与 refresh 同时变化时，跨时间 score 不天然可比。
- **Trade-offs / New Failure Modes**：多层 evaluator 增加 search/model cost、latency 与 external drift；
  LLM structuring 可能丢失或重写原始过程，generated rubric 可遗漏隐藏约束，claim decomposition 可切分
  失真，attachment extraction 可丢表格/布局语义。要求 reasoning trace 还会奖励 verbosity、暴露隐私/
  proprietary state，并使 closed systems 缺失非随机。把四层再压成 Overall 会重新掩盖 trade-off。
- **Where the Previous Design Still Applies**：确定性 tests/schema、短答案、隐私不允许保存 trace、
  厂商无法提供可比过程或只关心最终 artifact 时，应保留 output-only evaluation；static snapshot 负责
  稳定 regression，live refresh 负责 temporal coverage。人工/executable verification 在高风险 slice
  仍优先于多层 model judge。
- **Evolution Relationship**：`Layering / Dependency`：final report rubric → claim/evidence factuality →
  structured trajectory quality → bidirectional process-report provenance；dynamic/live refresh 与 static
  benchmark 是互补分支，不是后者替代前者。`Process→Report` 测 evidence utilization，`Report→Process`
  测 provenance sufficiency，两者不能互换。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch62/63 与 Ch72/76/77。Ch62 已覆盖 model/
  system/runtime/agent objects、claim-level provenance、trajectory evidence、rubric formation/execution 与
  judge calibration，是唯一主 owner；MiroEval 新增可复用的四平面拆分和双向 alignment。Ch63 仅负责
  低成本 telemetry/trace capture，Ch72/76/77 不重复评分机制。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后在 Ch62 refine “report/factual/process/provenance 四平面”和 trace missingness；不写入
  产品排名、固定模型 judge、固定 100-task recipe 或总体分数。
- **Open Questions**：怎样在不暴露 private chain-of-thought 的情况下提供 action/evidence-level process
  trace？如何分别版本化 dataset refresh、web snapshot、rubric generation 与 judge calibration？
  `CONFLICT` 如何结合 source authority/temporality 决议？process verbosity 与真实质量如何解耦？

### Stochastic KV Routing: Enabling Adaptive Depth-Wise Cache Sharing — 26/30

- **Candidate / Week / Score**：Stochastic KV Routing；2026-W14；26/30。
- **Source Family ID / Type**：`RCLA-DEPTHWISE-KV-SHARING`；Apple 作者 arXiv paper + Apple
  Machine Learning Research publication entry。未找到与论文实验绑定的公开 checkpoint、训练代码、
  inference implementation 或 immutable artifact；后续 Apple publication page 只作机构归属核验。
- **Event Date / Revision History**：arXiv v1 首发 2026-04-03；核验时 abstract history 只有 v1。
  Apple Research 后续收录和 workshop 页面不是新的 W14 event，也不补足实现证据。
- **Access / Full-read Coverage**：已读 19 页 v1 PDF/HTML 的 metadata、Introduction、Related Work、
  standard KV dynamics、CLA 与 cache-strategy 形式化、R-CLA 训练、pre-training、fine-tuning、全部主表、
  deterministic/random ablation、inference efficiency、Limitations、Conclusion 与 Appendix A～D；并核对
  Apple Research 入口和公开 artifact absence。目标与相邻章节已读 Ch18～22、Ch39～41。
- **Original Problem**：标准 decoder 为每个 token、每个 Attention layer 保存 K/V，容量近似随
  `layers × sequence × batch × KV heads × dtype` 线性增长。时间轴 eviction/compression 会面对
  query-dependent relevance、重算或信息丢失；既有跨层共享又常绑定固定 pattern、增加 encoder/
  iterative prefill，或因模型从未学过跨层 feature alignment 而只能有限 post-hoc sharing。
- **Why the Previous Design Was Reasonable**：逐层 KV 保持每层 Query 与本层 K/V 的训练分布一致，
  无需额外 alignment、routing metadata 或质量校准；MQA/GQA 只在 head 轴共享，风险边界清楚。
  对已有 checkpoint、短上下文、低并发、训练资源不可用或质量风险高的服务，完整逐层 cache 仍是
  最可预测的默认方案。temporal eviction 在明确 sliding-window/recency workload 下也仍合理。
- **Changed Constraint / Principle**：长上下文和高并发使 KV 容量与 HBM traffic 同时成为瓶颈，
  且同一模型可能部署在不同 memory budgets。关键不只是 runtime 判断“删哪些 cache”，而是训练时
  让 Query 对 KV source 变化具备鲁棒性，再把 deployment policy 与模型允许的 sharing contract 对齐。
- **Mechanism / Formulation**：设可持有 cache 的层集合为 `S`；未入选层 `l` 使用最近的前置
  cached layer `mu(l)=max{j in S | j<l}`。R-CLA 训练时每层、每次 forward 采样 Bernoulli：论文表述
  为以 `p` 采用本层 K/V，否则从任一前层均匀采样 K/V；全部 Transformer layers 仍执行，改变的是
  K/V source，不是 structured layer dropout。Inference 则固定 group/strategy，group leader 计算、
  写入 K/V，其余层跳过自己的 K/V projection 并复用 leader cache。
- **State Ownership / Control and Data Flow**：模型 checkpoint 拥有“哪些跨层 source 已在训练分布
  内”的语义；deployment planner 选择确定的 `S`/group size；runtime/cache manager 应持有
  `layer -> cache owner` mapping、分配与生命周期，kernel/backend 执行 projection skip 与 shared
  read。若调度器在没有 checkpoint capability metadata 的情况下自行改变映射，会把内存策略变成
  silent model-semantics change。论文未定义 capability schema、per-request dynamic switch、prefix
  cache identity、mixed-retention batching、rollback 或 failure recovery。
- **Implementation Details**：pre-training 使用 Qwen3-1.7B-style 28-layer decoder、OpenWeb subset、
  context 2,048、34B tokens、AdamW `(beta1=.9,beta2=.99)`、weight decay .1、gradient clip .1、
  5% warmup 到 `1e-4` 后 cosine decay，H100；比较 `p in {.25,.5,.6,.75}` 与 7/14/17/21/28-layer
  baselines。fine-tuning 使用 Qwen3-8B、Mistral-7B、Llama-3.1-8B，50,000 steps、batch 128、
  max input 8,192、AdamW `(.9,.95)`、weight decay .1、1.5% warmup 到 `5e-6` 后线性归零，
  五个 QA sources 并做 question/context 顺序与 HotpotQA passage permutation augmentation。
- **Evaluation Contract**：quality 评估覆盖 HotpotQA、SQuAD v2、MSMarco、TriviaQA、RepLiQA，
  比较 100%/50%/25% cache retention；ablation 在 Llama-3.1-8B 上比较 R-CLA、固定 CLA@2/@4
  与随机启用固定 pattern 的 RD-CLA。inference microbenchmark 使用 Qwen3-8B-scale 36-layer、
  hidden 4096、32 query heads、8 KV heads、head dim 128、bfloat16、单张 80GB GPU；输入 512～32K、
  group 1/2/4/8、batch 1～16，报告 peak/KV memory、TTFT 与 decode throughput。未披露具体 80GB
  GPU 型号、软件/backend/kernel/driver、输出长度、warmup/repetition、variance、功耗、并发 arrival、
  queueing 或 SLO；quality decoding 和样本量/置信区间也未完整披露。
- **Baselines / Ablations / Sensitivity / Overhead**：34B-token pre-training 中 `p=0 -> .75` 的
  eval loss 从 2.424 到 2.461，支持“未失稳”但不等于同质量；同 cache budget 的 full-depth sharing
  优于更浅模型。QA 表中 R-CLA 在低 retention 明显比未适配 base 更稳，但 full-retention 在
  RepLiQA 的 Llama/Mistral F1 为 -0.9%/-0.2%，并非全面提升。固定 CLA 在自己匹配的点偶尔可优于
  R-CLA，随机多 pattern 的优势主要是跨 retention robustness。group=4 的作者 microbenchmark 在
  8K、batch1 将 KV 1170MB 降到 293MB、throughput 34.0→41.6 tok/s；batch16 baseline OOM、group4
  可运行。这些数字只属于上述未完全披露的单卡 contract。
- **What the Evidence Proves**：在作者训练与 QA workload 下，显式训练 Query 适应跨层 K/V source
  可让一个 checkpoint 在多种确定的 depth-sharing pattern 下比 post-hoc 删除本层 cache 更稳；
  group leader 方案确实按 group size 减少逻辑 KV allocation，并可跳过 non-leader K/V projection。
  论文也支持“depth axis 是时间 eviction、head sharing 和 quantization 之外的独立设计轴”。
- **What It Does Not Prove**：不证明“无信息损失”在开放任务、长生成、multi-turn、MoE、不同
  precision 或组合压缩上普遍成立；不证明 runtime 可对普通 checkpoint 安全动态切换；不证明
  作者单卡 throughput/TTFT 可外推到 continuous batching、paged cache、TP/PP、PD separation 或
  production tail SLO。所谓 regularization 只由 data-constrained curves 与部分 full-retention gains
  支持，尚无 matched regularizer、seed variance 或 causal isolation。
- **Trade-offs / New Failure Modes**：需要预训练或全参 fine-tuning 资源；训练收敛变慢，shared
  representation 可能损失层特异信息；更多可选 retention 增加 checkpoint capability、cache layout、
  prefix identity 与 serving calibration 状态。固定 group 容易与 heterogeneous request quality/SLO
  不匹配，dynamic group 则引入切换一致性、batch fragmentation 和决策成本。与 temporal eviction、
  KV quantization、GQA/SSM 组合可能累积误差，论文未验证。跨层复用若不能在 SRAM 保持，Attention
  仍从 HBM 读取相同规模 K/V；作者明确把进一步 fusion/SRAM reuse 留给 backend future work。
- **Where the Previous Design Still Applies**：标准 per-layer KV 仍适用于未适配 checkpoint、质量
  first、短上下文/小 batch 或需要最简单 failure semantics 的场景；固定 CLA 适用于部署约束稳定且
  可为单一 retention 专门训练的模型；temporal methods 适用于时间 locality 明确、无法改训练的模型；
  MQA/GQA 和 quantization 仍可独立选择，而不是被 depth sharing 取代。
- **Evolution Relationship**：`Direct Evolution`：per-layer KV → fixed/post-hoc cross-layer sharing →
  stochastic multi-pattern training + deterministic deployment mapping；`Layering / Dependency`：与
  MQA/GQA、temporal eviction、quantization、PagedAttention 和 runtime scheduling 正交组合。它没有
  把 KV Cache 从模型状态降级为纯内存对象，反而强调 cache layout 必须服从 checkpoint semantics。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch18～22 与 Ch39～41。Ch19 已定义逐层
  `L` 进入容量公式和“架构 trade-off 不是 runtime 免费压缩”，因此是主 owner；新缺口是把 KV
  reduction 明确拆成 head/time/depth/precision axes，并解释训练允许的 cross-layer ownership。
  Ch40 只需连接 projection skip/read data path，Ch41 只需连接 capability identity/lifecycle；Ch22
  已有“减少或分层管理 KV Cache”，不重复展开。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`。
  Gate 通过后由 Ch19 吸收“depth-wise sharing 是 training-serving co-design，而非任意 eviction”；
  Ch40/41 仅短 handoff。不把 4×、22% 或 batch16 OOM 写成通用 serving 结论。
- **Open Questions**：怎样把 allowed sharing strategies 编码进 model/config 并参与 prefix/KV identity？
  dynamic per-request retention 如何在 continuous batch 中校准质量且可 rollback？和 GQA、KV quant、
  temporal eviction、MoE 叠加时误差是否独立？公开实现能否复现单卡表格，并补齐 GPU/backend、
  output length、重复测量、功耗与 SLO contract？

### SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization — 25/30

- **Candidate / Week / Score**：SKILL0；2026-W14；25/30。
- **Source Family ID / Type**：`SKILL0-EXTERNAL-SCAFFOLD-INTERNALIZATION`；arXiv paper +
  revision + author repository + executable training recipes。后续 SKILL1、SDAR、OPID、SEED、
  SkillRise 与 AgentOPSD 是新的 source families / revision follow-ups，不倒写成 W14 证据。
- **Event Date / Revision History**：arXiv v1 2026-04-02，v2 2026-05-15；作者仓库 README 称
  2026-04-03 发布 paper/code。W14 以 v1 为 event；v2 新增 WebShop 与训练说明，只用于识别
  revision，不把其结果归入首发周。
- **Access and Full-read Coverage**：已读 v1 metadata、Abstract、Introduction、Related Work、Agent
  Loop、Skill management、visual Context rendering、ICRL objective、adaptive curriculum、完整实验、
  training dynamics、skill-budget/helpfulness/validation-interval ablations、Conclusion/Limitations、
  理论与实现 appendices；对照 v2 revision，并核验作者仓库、SkillBank 目录和 ALFWorld/Search-QA
  3B training scripts。仓库当前 main 有 33 commits、包含后续工作且无 immutable release/tag，
  因而代码只能证明当前 recipe 可见，不能证明 event-date commit 与论文实验逐字一致。
- **Original Problem**：inference-time Skill retrieval 能提供程序性指导，但会检索无关 Skill、占用
  context，并让能力依赖每次注入；训练目标是利用外部 Skill 形成学习信号，同时让最终 policy 在
  没有 Skill context 时仍完成任务。
- **Why Previous Design Was Reasonable**：运行时 registry 可热更新、按租户授权、保留 provenance，
  还能携带代码、工具和资源；当知识变化快、任务长尾或模型尚未具备该能力时，检索比重新训练
  更便宜、更可治理。其 token/retrieval 成本是换取 updateability 与可撤销性的合理代价。
- **Changed Constraint / Principle**：对稳定、重复、高频的程序性模式，持续检索相同 Skill 会把
  context 和 retrieval noise 变成常驻税。原则不是“删除外部 Skill”，而是把可观测 scaffold 逐步
  撤掉，检查 policy 是否在分布外任务上保留了行为；训练 scaffold 与部署 registry 是两个平面。
- **Mechanism**：SkillBank 将 general 与 task-specific `.md` 按任务/类别分组；agent 看到 history
  与选中 Skills 的视觉渲染，同时输出环境 action 和压缩比例。训练分 `N_s` 个阶段线性降低最大
  Skill 数；每隔 `d` steps 在匹配 validation subtasks 上估计每个 Skill 的
  `Delta_k = Acc(with skill)-Acc(without skill)`，过滤 `Delta_k<=0`，对正值排序后取 top-M，最终
  令 M=0。奖励将 task success 与 success-conditioned log compression 项组合，policy update 使用
  同 prompt/group rollout 的归一化相对 reward、clipped ratio 与 reference KL 约束。
- **State Ownership / Control and Data Flow**：训练 runtime 拥有 SkillBank、task/category mapping、
  validation slice、helpfulness estimates、stage/budget 与版本；environment 产生 observations/reward，
  rendering layer 生成视觉 context，policy 产生 action/compression，trainer 聚合 group rewards 并
  更新 checkpoint。部署后的 skill-free policy 不再拥有外部 Skill 的 source identity，因此不能仅凭
  成功行为回答某条知识来自何处、何时过期或如何撤销。
- **Implementation Details**：公开 ALFWorld 3B script 使用 Qwen2.5-VL-3B-Instruct、GRPO、group
  size 8、train batch 16、validation 128、max prompt 3072、response 512、最多 50 environment
  steps、skill schedule `[6,3,0]`、compression reward coefficient 0.01、四卡、180 training steps；
  Search-QA recipe 使用 train batch 128、validation 512、prompt 4096、同样 group size 8，并通过
  本地 E5 retrieval server 连接环境。脚本确认机制组合，却不构成 event-date binary/release。
- **Evaluation Contract**：v1 在 ALFWorld 3,827 tasks 与 Search-QA 八个数据集上评估 3B/7B
  Qwen2.5-VL，作者披露四张 H800、最多 180 steps；Search-QA 以 NQ/HotpotQA 训练，其他集合主要
  测 OOD。作者报告相对 AgentOCR 的 ALFWorld/Search-QA 增益与每步小于 0.5k context，但这些数字
  只属于该模型、SkillBank、renderer、retriever、环境和 reward contract，不写成通用收益。
- **Baselines / Ablations / Sensitivity / Overhead**：比较 text/text+skill、AgentOCR 与固定/递减
  skill budgets；`[6,6,6]` 在撤掉 Skill 后退化，`[6,3,0]` 的 skill-free evaluation 更稳；去掉
  helpfulness filter 或改随机排序均下降，较短 validation interval 略有收益但增加 evaluation 开销。
  论文未给完整 factorial ablation 来分别归因视觉渲染、compression reward、curriculum 和 group RL；
  helpfulness 还需额外 with/without-skill validation，训练成本、方差和墙钟总账未完整披露。
- **What the Evidence Proves**：在作者的两个交互环境与公开 recipe 中，先给外部 Skill、再按测得
  helpfulness 逐步减小可见 Skill 的 curriculum，比一直依赖 Skill context 的若干 baseline 更能在
  skill-free evaluation 保留成功行为；它支持“外部 scaffold 可作为训练 curriculum”的机制判断。
- **What It Does Not Prove**：不证明知识被定位到特定参数，不证明所有 Skill 可被可靠内化，也不
  证明 inference-time registry、RAG 或工具资源可以被淘汰。理论 appendix 的 Lipschitz bound 与 Skill
  additive utility 是分析假设；真实 Skill 可能强交互。没有完整因果实验把 curriculum 与视觉压缩、
  reward shaping 分离，也没有生产级 latency、权限、更新、revocation 或 SLO 评估。
- **Limitations / Threats to Validity**：作者明确承认初始 SkillBank 质量依赖与新领域重新分组成本。
  进一步的系统边界是：`Delta_k` 由有限 validation accuracy 差估计，可能受噪声、顺序效应与
  validation overfitting 影响；多个 Skill 的互补/冲突破坏 additive 排序；当前 main 后续演进和 v2
  WebShop 结果也会造成 revision leakage。
- **Trade-offs / New Failure Modes**：减少 inference context 与 retrieval noise，换来额外训练 rollout、
  双条件验证、curriculum state 和不可直接撤销的 parameterized behavior。Skill 被吸收后可能过时、
  无 provenance、难以 tenant-specific override；错误 Skill 还可能被固化。保留 runtime registry 则有
  token/retrieval/selection tax，但拥有版本、权限、hot-fix、delete 和 rollback。
- **Where Previous Design Still Applies**：最新事实、政策、tenant 约束、可执行代码/资源、低频长尾
  工作流、安全敏感行为和需要审计/撤销的能力，应继续作为 versioned runtime Skill；稳定、重复、
  可验证且不依赖外部资源的程序性先验，才适合作为 curriculum 候选。
- **Evolution Relationship**：`Direct Evolution`：runtime retrieval-only → external Skill as training
  scaffold → dynamic helpfulness filtering/ranking → zero-skill curriculum；与 Ch80 的 registry/control
  plane 是 `Layering / Dependency`，不是 replacement。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch28 PPO、Ch29 GRPO、Ch30 DPO、Ch71
  Context、Ch80 Agent Platform。Ch29 已有 grouped rollout、reward measurement 与 curriculum 风险，
  但缺少“外部 scaffold 退火到 skill-free policy”的完整演进；Ch80 已定义 Skill identity、provenance、
  permission、version 与 rollback，正好限制“internalization 替代 registry”的错误外推。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books
  Gate Closed)`。Gate 通过后由 Ch29 沉淀 scaffold→curriculum→skill-free evaluation 机制；Ch80/71
  只增加运行时 Skill 共存与 context-cost handoff。现在不修改 Books。
- **Open Questions**：如何用置信区间而非单点 `Delta_k` 做 Skill selection？如何测量 Skill interaction
  与负迁移？checkpoint 如何携带被吸收 Skill 的 provenance、expiry 与 revocation hook？怎样以
  matched total compute 分离 curriculum、renderer、compression reward 和 policy optimization？

### GrandCode: Achieving Grandmaster Level in Competitive Programming via Agentic Reinforcement Learning — 26/30

- **Candidate / Week / Score**：GrandCode；2026-W14；26/30。
- **Source Family ID / Type**：`GRANDCODE-MULTISTAGE-AGENTIC-GRPO`；arXiv technical report +
  revision + official project/blog + report repository + contest-submission artifact。项目仓库从
  `deepreinforce-ai` 重定向至 `ornith-ai`；公开 artifact 只有报告和提交代码，不是训练实现。
- **Event Date / Revision History**：arXiv v1 2026-04-03，v2 2026-07-13，v3 2026-08-05；W14
  只按 v1 归档。后续版本作者列表发生变化但主体目录/机制未显示独立新实验；v2/v3 只能用于
  revision boundary，不能把后续组织/作者信息倒写为 v1 事实。
- **Access and Full-read Coverage**：已读 v1 metadata、Introduction、三场 contest contract、System
  Overview、Agentic GRPO 全部公式、test generation、hypothesis policy、continued pretraining/SFT/
  summarization、multi-component RL、RL infrastructure、test-time RL、Conclusion、submission details、
  code reward、Agentic-GRPO analysis 与 submitted-code appendix；对照 v2/v3，核验官方项目页、
  report repository 和三场 contest code repository。论文没有独立 Limitations/Threats section，
  也没有公开模型 checkpoint、training code、数据 manifest 或 immutable release。
- **Original Problem**：长 agentic code rollout 包含编译、执行、测试、修正等多阶段，每个 evaluator
  可耗时较长；若等待终局 reward 才更新，trainer 空转且 rollout 期间 policy 已变化，整个 trajectory
  可能由多个 behavior-policy versions 生成。
- **Why Previous Design Was Reasonable**：terminal-only GRPO 将同一最终结果统一作用于完整 trajectory，
  objective 简单、不会重复更新同一 stage，也无需保存迟到 correction。对较短 response、快速 verifier、
  同步 rollout 或强 terminal specification，它仍提供更清楚的 on-policy boundary。
- **Changed Constraint / Principle**：当 multi-stage environment 产生有意义的中间结果，而 final reward
  延迟超过多次 policy update，及时使用局部信号可缩短 feedback latency；但终局 outcome 仍必须纠正
  局部 proxy。系统原则是把 reward arrival、policy version 与 stage identity 都提升为训练状态。
- **Mechanism**：对 stage `s_t` 的 K 个 rollouts，用同 stage rewards `r_t` 形成 group-normalized
  advantage 并立即做 clipped update；终局 `r_N` 到达后计算 `delta_t=r_N-r_t`，独立归一化并以更窄
  `epsilon_2<=epsilon` 再更新旧 stage。每个 token ratio 的 denominator 是实际生成该 token 的
  `pi_(theta_u,beh)`，而非假设整条 trajectory 来自单一 checkpoint。异步 pipeline 再按 token age
  `d_t`：阈值前权重 1，中间指数衰减，超过 `K_2` 直接丢弃。
- **State Ownership / Control and Data Flow**：rollout runtime 必须持久化 trajectory/stage/token identity、
  immediate reward、terminal linkage、behavior-policy version/logprob、age、verifier/test-set version 与
  correction status；trainer 拥有 current policy、staleness rule 和两套 clip/normalization。Workflow
  将 main solver、hypothesis、summary 与 CPU sandbox 分开调度，不能靠自然语言 handoff 重建这些状态。
- **Implementation Details**：主 solver 是大型 Qwen3.5-397B MoE，hypothesis/summary 使用较小 dense
  models 并在独立 GPU pools 异步服务；code execution/brute-force/test generation 位于 CPU sandbox。
  hybrid DeltaNet+softmax attention 采用 pipelined context parallelism，多 micro-batches 摊薄 recurrent
  startup/drain；按 difficulty/历史 completion time 组 batch、动态选择 CP，并在 RL 中冻结 MoE router。
  论文没有披露 GPU 型号/数量、K、`epsilon`、`K_1/K_2/lambda`、optimizer、rollout concurrency、
  wall-clock、故障恢复或 checkpoint protocol。
- **Evaluation Contract**：系统证据包括三个 2026-03 live Codeforces contests 的 standings/submissions、
  50 个历史问题的 adversarial-test filtering、200 问题 hypothesis subset、100 问题五难度 benchmark，
  以及 base→continued training→SFT→full RL→test-time RL 的阶段结果。公开提交代码支持“这些账户提交了
  可接受程序”，但没有独立证明训练 pipeline、模型身份、计算预算、搜索并行度或 human assistance
  完全匹配论文描述；paper 自身还说明为了 joint score 等待人类接近完成后提交。
- **Baselines / Ablations / Sensitivity / Overhead**：continued training 与 SFT 有阶段消融；summary 加入
  后在 100 题上略降。test generation 从 42/50 到 48/50，利用 submission feedback 后 50/50，但最后
  一步使用外部 judge feedback，不是盲测。论文没有 standard GRPO vs immediate-only vs delayed-
  correction vs staleness-control 的独立 ablation，也没有 multi-component、test-time RL、更多 parallel
  samples 的 matched-compute factorial；pipelined CP utilization 是 schedule/table claim，缺硬件实测协议。
- **What the Evidence Proves**：报告给出一套可执行的 multi-component coding workflow、形式化的
  immediate/correction/staleness update，以及 contest submission evidence；它证明“agentic RL 的
  trajectory 需要 stage、token policy-version 与 late-reward lifecycle”是值得审计的系统问题。
- **What It Does Not Prove**：不证明 Agentic GRPO 单独造成 contest 成绩，不证明两阶段 update 是
  unbiased terminal GRPO，也不证明系统在一般 coding/agent tasks、相同成本或无 online adaptation
  时优于替代方案。三场 live contest 不是随机、独立、compute-matched benchmark；“超越最强人类”
  是作者对特定参赛记录的 headline，不能写成通用模型能力结论。
- **Limitations / Threats to Validity**：附录承认未归一化 immediate+correction 可分解为 terminal
  signal，但分别除以不同 group std 后不再等价；作者把这解释为 balanced credit，而不是提供
  bias/variance 定理或消融。过旧 correction 会因 `K_2` 被丢弃，早期 proxy 可能永远不被终局修正。
  另外数据含多家 proprietary model synthesis，benchmark/data contamination、human operational role、
  exact contest policy compliance 与 infrastructure contract 均未完整披露。
- **Trade-offs / New Failure Modes**：更早训练反馈与 pipeline utilization，换来同一 stage 两次更新、
  per-token policy lineage、correction queue 和更复杂的 replay/recovery。局部 reward 可被 exploit；
  separate normalization 可放大低方差信号；stale correction drop 引入系统性 censoring；多组件 reward
  会出现 blame ambiguity；test-time per-instance LoRA 新增污染、rollback 与 deadline risk。
- **Where Previous Design Still Applies**：短 trajectory、终局 verifier 快、局部 proxy 不可信、严格
  on-policy 或需要容易复现 objective 时，terminal-only GRPO/同步 rollout 更合理；组件少且单 solver
  headroom 足够时，single-agent + deterministic tests 仍可避免 coordination 和多模型状态。
- **Evolution Relationship**：`Direct Evolution`：terminal-only sequence reward → stage-immediate update
  → final-difference correction → token-version staleness control；与 Ch77 durable state 和 Ch78 component
  ownership 是 `Layering / Dependency`，与 test-time best-of-N LoRA 是正交 adaptation 分支。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch28 PPO、Ch29 GRPO、Ch30 DPO、Ch75
  Planning、Ch76 Reflection、Ch77 Workflow、Ch78 Multi-Agent。Ch29 已讨论 partial rollout、policy
  version、staleness 与 segment credit，但没有具体的 immediate+delayed normalized update；Ch77/78
  已拥有 durable state 和 component boundary，足以作为短 handoff，Ch75 不应成为训练算法 owner。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books
  Gate Closed)`。Gate 通过后在 Ch29 加入两阶段 credit 与不等价/丢失 correction 边界；Ch77/78
  只增加 stage lineage / component responsibility handoff。现在不修改 Books。
- **Open Questions**：与 terminal GRPO matched compute 时，收益来自低 feedback latency 还是不同
  objective bias？如何用 importance correction 或 replay 处理被 `K_2` 丢弃的 terminal evidence？
  correction crash/retry 怎样 exactly-once？不同 stage reward scale、group std 和 verifier drift 如何校准？

### Self-Distilled RLVR — 25/30

- **Candidate / Week / Score**：Self-Distilled RLVR（RLSD）；2026-W14；25/30。
- **Source Family ID / Type**：`RLSD-PRIVILEGED-CREDIT-MAGNITUDE`；arXiv paper + revision +
  current author code/config artifact。Hugging Face 仅作 discovery；机制证据来自论文和作者仓库。
- **Event Date / Revision History**：arXiv v1 2026-04-03，v2 2026-04-08；W14 按 v1 归档。
  v2 补充了 GRPO+OPSD 与 MOPD 的关系和相应讨论，但没有形成新的 event。当前 GitHub 仓库有
  8 次提交、可运行配置与数据入口，却没有 tag/release 或可证明对应 4 月 3 日实验的 immutable commit，
  因而只作 implementation cross-check，不能倒写为 event-date artifact。
- **Access and Full-read Coverage**：已读 v1 metadata、Abstract、Introduction、Preliminaries、OPSD
  empirical failure、KL/gradient decomposition、RLSD 三步方法与 Algorithm 1、统一 token-advantage
  视角、完整 experimental setup/results/dynamics/case study、Related Work、Conclusion、Limitations，
  以及 A.1～A.6 的 proofs、pilot variants、shared-parameter trilemma、Bayesian interpretation 与
  zero-leakage theorem；对照 v2，并核验作者 README、依赖、数据入口、RLSD/GRPO config 与启动脚本。
- **Original Problem**：RLVR/GRPO 常把一个 sequence-level verifier reward 复制给回答内所有 tokens，
  credit 粗糙；on-policy self-distillation 让同一模型在额外 reference/reasoning context 下当 teacher，
  能提供 dense signal，却可能把学生推向部署时不可见的 privileged conditional distribution。
- **Why Previous Design Was Reasonable**：uniform sequence advantage objective 清楚、只依赖可验证结果，
  不需要额外 teacher forward 或 reference；OPSD 则在 verifier 稀疏、teacher context 可信时，用全词表
  distribution matching 获得更密集监督。短训练、单一任务或 teacher/student information 对称时，二者
  都是合理分支，而不是等待被新方法淘汰的错误方案。
- **Changed Constraint / Principle**：目标是在不让 privileged teacher 单独决定 reinforce/penalize 方向的
  前提下，仍利用它区分同一 trajectory 内 token 的相对贡献。长期原则是把 supervision 分成
  `direction authority` 与 `magnitude estimator`，并分别审计其来源、版本与故障。
- **Mechanism**：学生先按 `pi_theta(.|x)` 为每个 prompt 采样 `G` 个 responses，由 binary verifier
  形成 group-normalized sequence advantage `A`。同一模型再带 ground-truth answer `r` 前向一次，
  计算 sampled token 上的 stop-gradient
  `Delta_t=log pi(y_t|x,r,y_<t)-log pi(y_t|x,y_<t)`；令
  `w_t=exp(sign(A)*Delta_t)`，再把 clipped positive multiplier 与 uniform advantage 混合，得到
  `A_t=A*((1-lambda)+lambda*clip(w_t))`。正 trajectory 中 teacher 更支持的 token 得更大正 credit；
  负 trajectory 中 ratio 反转，teacher 不支持的 token 受更大惩罚。训练前 50 steps 将 `lambda` 从
  0.5 线性降到 0，最终回到 uniform GRPO。
- **State Ownership / Control and Data Flow**：dataset owner 提供 question、image、ground-truth answer；
  rollout policy 产生 response/token logprobs；verifier 独占 sequence sign；teacher snapshot 只提供
  stop-gradient magnitude，trainer 管理每 10 steps 同步、`lambda` schedule、`epsilon_w` clipping、
  group statistics、mask 与 optimizer state。若 reference、teacher version、verifier identity 或
  tokenization 丢失，无法重放 credit provenance。
- **Implementation Details**：论文基于 VERL/EasyR1，base 为 Qwen3-VL-8B-Instruct；训练/评估均为
  8192 context（prompt/response 各最多 4096），batch 256，每 prompt 8 rollouts，temperature 1.0；
  GRPO-family learning rate `1e-6`，policy clip low/high 为 0.2/0.28，不使用 KL/entropy loss，
  `epsilon_w=0.2`。训练数据 MMFineReason-123K 由 Qwen3-VL-4B-Thinking 四次全失败筛出；OPSD
  baseline 还使用 Qwen3-VL-235B-A22B-Thinking 蒸馏并验证的 reasoning traces。硬件为 4 nodes ×
  8 NVIDIA H200 140GB。当前代码基于 EasyVideoR1/veRL/Ray/vLLM，公开 RLSD 与 GRPO configs，
  但没有 event-bound checksum、完整日志或 checkpoint。
- **Evaluation Contract**：五个 multimodal reasoning benchmarks（MMMU、MathVista、MathVision、
  ZeroBench、WeMath）报告 accuracy，比较 Base、GRPO、OPSD、SDPO、GRPO+OPSD 与 RLSD；training
  dynamics 覆盖 200 optimization steps，并给两个 token-credit heatmap case。作者报告 RLSD 在该
  contract 下平均 56.18、比 GRPO 高 2.32 points；这些数字只属于上述模型、数据、长度、硬件与
  evaluation recipe，不可外推为一般 RLVR 收益。
- **Baselines / Ablations / Sensitivity / Overhead**：OPSD 的 full-vocabulary、teacher-top-1、student-
  top-1 pilot 用于支持 leakage-bandwidth 叙述；主表比较多个训练 objective，也记录 entropy 与 3%～6%
  credit clip ratio。但没有 RLSD 的 `no sign inversion`、不同 `lambda`、`epsilon_w`、teacher sync 频率、
  answer quality、group size、dataset difficulty 或额外 teacher forward 的 factorial ablation；不同
  baseline learning rates、privileged information 强度也不一致。作者称额外 forward 相对 rollout
  “negligible”，却没有 wall-clock、utilization、energy 或 matched-total-compute 数据。
- **What the Evidence Proves**：方法形式上保证 multiplier 为正，因此 privileged signal 不会翻转
  sampled token advantage 的正负，且只作用于 student-sampled support；clipping 给它有界影响。
  论文实验支持在一个 8B multimodal contract 下比所列 baselines 更高的作者评测分数，并显示 OPSD
  pilot 的 early gain/late degradation 现象。
- **What It Does Not Prove**：不证明 likelihood ratio 是 token 对最终 correctness 的因果贡献，不证明
  privileged signal 对参数轨迹为零，也不证明 verifier 方向正确。`A=0` 或 all-equal group 时，teacher
  无法创造方向；错误、可 exploit 或过粗的 verifier 仍会稳定地产生错误 sign。论文不证明对纯文本、
  code、视频、其他模型规模或生产训练成本普遍成立；Limitations 中提到的这些扩展只是 preliminary
  author claim。
- **Limitations / Threats to Validity**：Bayesian interpretation 假设同一模型近似真实 prior/posterior
  conditionals；实际每个 `x` 只有给定 reference，conditional mutual information 并未被直接估计。
  zero-leakage theorem 将“leakage”限定为 gradient sign/support channel，但 magnitude 仍依赖 `r`，
  因而会改变参数更新向量和后续 sampling distribution；更准确的边界是 `direction isolated and
  magnitude bounded`。另外正文称用 `lambda` “逐步转向 uniform”，Algorithm 1 与实验确实把
  `lambda` 从 0.5 衰减至 0，但 Eq. 16 没有显示 interpolation，构成论文内部 specification ambiguity。
  两个 heatmaps 是事后解释，不是 causal token-credit validation。
- **Trade-offs / New Failure Modes**：获得比 sequence-uniform reward 更细的 sampled-token weighting，
  换来每 response 额外 teacher forward、reference availability、teacher snapshot lifecycle 与新的
  clipping/schedule。reference wording 或错误答案会把 magnitude 偏向 spurious tokens；同步周期使
  magnitude evaluator stale；较强 clipping 压平信息、较弱 clipping 增大方差；正负 trajectory 使用
  反向 ratio 还可能放大 teacher 罕见 token 的惩罚。privileged answer 的 ACL、污染和 provenance 也
  成为训练数据治理问题。
- **Where Previous Design Still Applies**：reference 缺失/不可信、verifier 快且强、额外 forward 昂贵、
  objective 可解释性优先或任务本身 response 很短时，uniform GRPO 更合理；teacher 能公开稳定地提供
  完整目标分布且信息对称时，标准 OPD 仍是直接的 distribution-matching 分支；process verifier 真正
  可执行时，直接 step reward 比 likelihood-based proxy 更容易解释。
- **Evolution Relationship**：`Direct Evolution`：sequence-uniform GRPO → privileged distribution
  matching → verifier-owned direction + teacher-owned magnitude → teacher guidance annealed to uniform
  GRPO；与 PPO/GRPO clipping 是 `Principle Reuse`，不是同一个 ratio 或 trust-region guarantee。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch28 PPO、Ch29 GRPO、Ch30 DPO。Ch28 已
  定义 terminal reward 的 token credit problem；Ch29 已说明 uniform sequence advantage、process
  verifier 与 all-equal group，但缺少 direction/magnitude supervision decomposition。Ch30 的 offline
  preference objective 不应成为该 on-policy机制 owner。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books
  Gate Closed)`。Gate 通过后由 Ch29 沉淀 supervision authority、magnitude proxy 与 specification
  ambiguity；Ch28 只加短 handoff。现在不修改 Books，也不写入作者 benchmark headline。
- **Open Questions**：如何用 process-level ground truth 验证 `w_t` 与真正 causal credit 的相关性？
  reference corruption、teacher-sync lag 和 all-equal groups 对 bias/variance 的联合影响多大？能否用
  matched wall-clock 和 H200-hours 分离 dense credit 的 sample efficiency 与额外 forward 成本？
  “leakage”应如何定义成可测的 deployment behavior，而不是只按 gradient sign/support 定义？

### ASI-Evolve: AI Accelerates AI — 24/30

- **Candidate / Week / Score**：ASI-Evolve；2026-W14；24/30。
- **Source Family ID / Type**：`ASI-EVOLVE-DUAL-MEMORY-RESEARCH-SEARCH`；arXiv paper + author
  repository + runnable circle-packing demo/current code paths。Repository 公开通用 pipeline、cognition store、
  program database、sampling algorithms 与 circle-packing outputs，但不含论文 architecture/data/RL/DTI
  主实验 code、configs、checkpoints、raw logs 或 complete experiment tree。
- **Event Date / Revision History**：arXiv v1 2026-03-31；核验时只有 v1。作者仓库当前 13 commits、无
  GitHub release/tag；current main 可说明机制边界，不能被当作 event-date immutable artifact。
- **Access / Full-read Coverage**：已读 metadata、Introduction、task-length framing、完整 Researcher/
  Engineer/Analyzer/Cognition/Database 方法、architecture/data/RL 三项 task formulation/method/results/analysis、
  circle-packing framework/model/sampler comparisons、Analyzer/Cognition ablations、DTI transfer、Conclusion、
  全部 configuration/cognition appendix；核对仓库 README、experiments coverage、pipeline/database/cognition
  关键代码与 release absence，并读 Ch23、Ch29、Ch62、Ch73、Ch76～78。
- **Original Problem**：昂贵 AI research loop 每个候选可能需要长训练、改大型 codebase，并输出 loss、
  benchmark、efficiency 与错误 trace 等高维反馈。只用一个 scalar fitness 会丢失失败原因，完全从零搜索
  又会重复已知 dead ends；把全部 raw logs 直接回灌 Context 则不可扩展。
- **Why the Previous Design Was Reasonable**：在 verifier 便宜、代码短、目标清晰的 circle packing/kernel
  search 中，candidate→score→selection 的简单 evolutionary loop 已能工作；human expert 直接提出少量
  hypotheses 在实验昂贵、ground truth 弱或风险高时仍更节省且更可问责。raw logs 也保留最高 fidelity，
  在短 loop 中无需另设 Analyzer-derived memory。
- **Changed Constraint / Principle**：当 `execution cost × search-space openness × feedback complexity`
  同时上升时，应把先验、候选 lineage、实验执行、反馈解释与 selection 分成独立 state owners。先验用于
  cold start，run-derived lesson 用于 sustained search；二者若混成一个无版本“memory”，就无法区分人类
  假设、模型归因与真实实验事实。
- **Mechanism**：每轮从 program database 按 UCB1/random/greedy/MAP-Elites 采样 parent/context nodes，
  再以其 motivation/analysis 查询 embedding-indexed Cognition；Researcher 生成 full program 或 diff 及
  motivation；Engineer 经 experiment-specific script、timeout、quick/static checks 与可选 judge 运行候选；
  Analyzer 读取 code、raw logs、metrics 和 best sampled node，产生 decision-oriented analysis；新 node 把
  motivation/code/results/score/analysis/runtime/success 写回 database。主架构任务另加 complexity/chunk/
  causal-mask static checker、runtime debug agent 与 motivation-similarity novelty filter。
- **State Ownership / Control and Data Flow**：human/problem owner 必须拥有 task contract、mutable variables、
  hard constraints、budget 与 deployment approval；Evaluator/Engineer 拥有 executable environment、metric
  version 与 raw run evidence；Database 拥有 candidate ID、parents、code digest、results 与 lineage；Cognition
  store 应拥有 source/version/trust/scope；Analyzer 只生成 derived diagnosis。当前代码把 nodes JSON/FAISS
  本地持久化，`max_size` 满时按最低 score 删除 node；它没有独立 artifact store、retention/legal hold、
  evaluator digest、ACL、transactional recovery 或 derived-analysis supersession contract。
- **Implementation Details**：当前 repo 提供 Python 3.10+、OpenAI-compatible API、可选 W&B、并行 workers、
  local JSON/FAISS persistence 与 circle-packing demo。论文 circle-packing ablation 使用 GPT-5-mini、4 workers、
  300s timeout、database max 70、5-island MAP-Elites、cognition top-k 5/threshold .4、judge disabled、每条件
  3 runs；Qwen3-32B comparison 的 decoding/seed 另行披露。论文未披露主任务 GPU 型号、cluster/topology、
  framework versions、总 GPU-hours、API tokens/cost、失败重跑成本或端到端 wall-clock。
- **Evaluation Contract — Architecture**：约 150 条/100 papers cognition；1,773 rounds、1,350 generated
  candidates。exploration 用约 20M/8-layer model、1B tokens/2,000 steps、10 benchmarks×500 samples，fitness
  混合 sigmoid-normalized loss/accuracy 与 LLM judge；verification 扩为约 340M/1B tokens，105 个超过
  DeltaNet；只选 5 个在约 1.3B/100B tokens、16 benchmarks（含 6 held-out）验证。作者承认未生成
  optimized kernels，judge efficiency 不能保证 wall-clock efficiency。
- **Evaluation Contract — Data / RL / Transfer**：data strategy 先在每 category 500 docs 执行、由 Analyzer
  评 50 pairs，再将 selected Nemotron-CC pipelines 用于 3B models、500B-token matched training、18 benchmarks；
  这同时包含 strategy search 与一次巨大 downstream validation。RL search 以 4B/150 steps/6 math tasks
  exploration、14B verification，Table 3 又写 Qwen3-14B/Skywork-OR1/SIIRL/250 steps，存在 250/300-step
  specification inconsistency；300 rounds 后 10 项过 exploration、5 行报告、正文称 3 项跨域显著，但
  未给显著性检验细节。DTI 从 DrugBAN 出发，100+ rounds，在四 datasets/四 splits 上报告单次表格。
- **Baselines / Ablations / Sensitivity / Overhead**：只有 circle packing 对 OpenEvolve/GEPA、GPT-5-mini/
  Qwen3-32B、MAP-Elites/UCB1/random，以及 full/no-Analyzer/no-Cognition 做较完整 3-run control。Cognition
  主要提高初始 climb；无 Analyzer 仍有 raw score、偶尔也达 SOTA，但更易 plateau；无 Cognition 慢启动后
  仍可持续提升。三项主任务没有 matched full/no-component/sampler/model ablation，也没有 total-compute-
  matched human search、candidate survival bias、multiple-testing correction 或 independent replication。
- **What the Evidence Proves**：在作者 circle-packing contract 下，预置 priors、structured analysis 与
  quality-diversity sampling 对 search trajectory 有可见且角色不同的影响；公开实现验证 loop 确实把 code、
  score、analysis 和 parent selection 连接起来。主任务表明该 pattern 能在作者环境中生成可训练候选并通过
  staged evaluation，但只支持受限 case evidence。
- **What It Does Not Prove**：不证明 Analyzer 做了 causal analysis，而只证明模型生成了下一轮可用文本；
  不证明 105 个架构彼此独立、具备 kernel/serving 效率或经外部复现，也不证明 data/RL gains 由 framework
  而非 expert-seeded cognition、fitness design、selection budget 或 experiment-specific engineering 造成。
  “fully open-sourced”不等于论文主实验可重放；DTI prediction 也不是 wet-lab discovery 或 clinical utility。
- **Limitations / Threats to Validity**：论文无独立 Limitations section；主任务 hardware/compute、seeds/
  variance、API/provider snapshots、raw artifacts 与 statistical tests 大量缺失。反复使用 development fitness
  会造成 search-level overfitting；LLM judge 同时影响 fitness 与 analyzer narrative；Cognition 包含 target/
  SOTA knowledge（circle packing 明示约 2.635 target），加速不能等同于 novel reasoning。data pair judge、
  architecture novelty similarity 与 RL qualitative coherence 都可能成为 proxy attack surface。
- **Trade-offs / New Failure Modes**：Cognition 降低无效试验，却收窄 hypothesis prior、继承 literature
  错误并造成 benchmark leakage；Analyzer 压缩高维 evidence，却会把相关性写成因果、遗失 minority failure
  或反复放大自家解释。MAP-Elites 保留 diversity，代价是更多低分计算；top-score eviction 控制 storage，
  却会删除失败证据、破坏 lineage/审计。debug agent 节省失败预算，也可能悄悄改变研究 hypothesis；static
  checks 防已编码约束，不保护未编码语义。
- **Where Previous Design Still Applies**：短函数、便宜确定性 verifier 可用简单 evolutionary search；
  expensive/weakly observed/irreversible 研究应由 human 选择少量 hypotheses、锁定 protocol 并独立复现；
  无可信 cognition 时允许从零探索但扩大 budget，prior 强且任务稳定时可从人工 baseline 做 local search。
  原始 logs 必须作为 evidence archive 保留，不能被 Analyzer summary 替代。
- **Evolution Relationship**：`Direct Evolution`：candidate→scalar fitness → lineage-aware population search →
  human-prior cognition + run-derived analysis → held-out/independent replication；`Layering / Dependency`：Ch77
  Workflow 拥有 loop/authority，Ch73 拥有 derived lesson lifecycle，Ch62 拥有 evaluator independence，Ch23/
  Ch29 只拥有被搜索 data/RL mechanism 的验证。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch23、Ch29、Ch62、Ch73、Ch76～78。Ch77 已有
  problem compilation、evaluator cascade、program database、quality/diversity、lineage、held-out 与 human
  deployment，是主 owner；Ch73 已有 raw episode→derived strategy 与 judge-error feedback。新增可 refine 的
  是把 prior cognition 与 run-derived lesson 明确分成 cold-start/sustained-search 两平面，并禁止 Analyzer
  summary 冒充 causal evidence。Ch62 已覆盖 state-evolution evaluator risk，其他章节无需重复论文案例。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate
  Closed)`。Gate 通过后由 Ch77 补足 dual-memory research loop、component role 与 artifact/evidence boundary；
  Ch73/62 仅短 handoff。Ch23/29 不写入作者发现的具体清洗/RL 算法，除非其机制被独立全文复核。
- **Open Questions**：公开三项主任务 immutable configs/code/logs/checkpoints 后能否重放？在 matched total
  compute 与 expert priors 下，Cognition/Analyzer/sampler 各自增益多少？Analyzer diagnosis 与 causal ablation
  的一致性如何测？如何防 evaluator/judge gaming、multiple-testing/search overfit，并让失败节点在 storage
  compaction 后仍可审计？什么 evidence 才允许候选从 research database 晋级为 deployable artifact？

### Embarrassingly Simple Self-Distillation Improves Code Generation — 26/30

- **Candidate / Week / Score**：Embarrassingly Simple Self-Distillation Improves Code Generation；
  2026-W14；26/30。全文复核后由 24 调整为 26：它给出可推导、可消融的 distribution-transformation
  机制和部分官方 artifact，长期价值高于 discovery 摘要；但训练 artifact、重复实验与独立验证仍不足。
- **Source Family ID / Type**：`SIMPLE-SD-TEMPERATURE-TRUNCATION-SELF-TARGETS`；arXiv v1/v2 paper +
  Apple Research page + official repository + data-generation/evaluation code + three official checkpoint model
  cards。第三方摘要、下载量与当前 stars 不作机制或质量证据。
- **Event Date / Revision History**：arXiv v1 于 2026-04-01 首发，v2 于 2026-06-24 修订；W14 只归档
  v1 的五模型证据。v2 才加入 GPT-OSS-20B、把叙述改为六模型/三 family；Apple Research 页面当前标注
  July 2026，也不能替代 first-public date。仓库 3 月 30 日已有 first commit，4 月 3 日发布 README，
  4 月 7 日发布 checkpoints，4 月 16 日才加入 data-generation pipeline；当前无 tag/release。
- **Access and Full-read Coverage**：已读 v1 的 metadata、Introduction、完整 SSD objective、sampling /
  training / inference、五模型主实验、decode-only temperature sweep、训练/推理 temperature interaction、
  lock/fork hypothesis、toy 与 real-model analysis、完整理论 appendix、vLLM decoding pipeline、全部实验
  设置、OOD transfer、高温坏数据 stress test、Related Work 与 Conclusion；再核对 v2 revision、README、
  `data_generation/config.yaml` / `generate.py`、`evaluation/eval.py` / `benchmark.py`、checkpoint cards、commit
  history 与 release 状态。论文没有独立 Limitations / Threats section；公开仓库没有 Megatron training code、
  optimizer/checkpoint conversion recipe、主实验 configs/results 或 immutable environment。
- **Original Problem**：高质量 code demonstrations 需要人工、强 teacher 或 execution verifier；单次全局
  decoding policy 又必须同时服务两类上下文：`lock` 位置要求压掉 distractor tail，`fork` 位置要求保留多个
  plausible branches。只调一个 temperature 会在 precision 与 exploration 之间折衷。
- **Why the Previous Design Was Reasonable**：verified synthetic SFT 在 correctness oracle 便宜时能阻止错误
  targets；强 teacher distillation 在 student capacity 足够且 teacher 可用时提供外部能力；RLVR 在可执行
  reward 下直接优化 outcome；decode-only tuning 无训练状态、易回滚。它们分别拥有更明确 correctness、
  capability ceiling、credit 或 operational simplicity，不能被无验证 SSD 单向替代。
- **Changed Constraint / Principle**：当 prompt pool 可得、verification/teacher/RL 成本成为瓶颈，而 frozen
  model 已在概率 tail/head 中包含未被单一 decoding policy 同时利用的能力时，可以把 sampling policy
  视为 **target-distribution compiler**。关键不是自生成文本天然正确，而是 non-unit temperature 和
  truncation 先改变监督分布；普通 cross-entropy 再把这一变换参数化。generation policy 与 deployment
  policy 是两个独立但耦合的控制面。
- **Mechanism**：对每个 prompt 从 frozen model 只采一个 solution，先以 `T_train` 重标 logits，再应用
  top-k/top-p support gate；不执行、不按 correctness 过滤，随后用 response-level cross-entropy 做 SFT，
  serving 时再以独立 `T_eval` 解码。若 `T_train=1` 且不 truncation，population expected score gradient
  为零；truncation 将 loss 分成 retained-support mass 与 within-support CE，non-unit temperature 再对
  support 内相对概率做 power reshaping。peaked lock 的 retained set 小，主要获得 tail compression；
  flatter fork 的 retained set 大，允许 head 内 alternatives 重排。局部 ideal-fit 下两温度以
  `T_eff=T_train*T_eval` 组合，但只在 fixed support / local-fit 假设内成立。
- **State Ownership / Control and Data Flow**：可复现系统必须持久化 base checkpoint/tokenizer/chat template、
  prompt-pool/dedup version、generation runtime/seed/`T_train`/top-k/top-p/max length、raw sample 与过滤
  provenance、SFT optimizer/data order/checkpoint、以及独立的 evaluation benchmark/sandbox/
  `T_eval`/sample seeds。SSD 本身是一轮 compile→train→deploy，不提供持续自改进的 acceptance、rollback
  或 contamination owner；若迭代执行，还必须增加 parent/student lineage 与 regression gate。
- **Implementation Details**：v1 从 rSTARcoder `seed_sft` 只取 prompts，whitespace-normalized exact dedup
  后约 10,168 题；每题一个 sample，vLLM 0.11.0、8-way tensor parallel、128K max sequence。论文只删除
  empty response 与 single-line stub。Megatron-LM 在 8×B200 上训练，MoE 用 EP=8；AdamW
  `beta=(0.9,0.95)`、weight decay 0.1、cosine LR `5e-6→1e-6`、global batch 32、sequence length 65,536；
  instruct 2,500 steps / 250 warmup，thinking 300 / 50 warmup。当前公开 generator 使用 BF16，但默认
  temperature=1.5 且丢最短 10% outputs；这与论文 Qwen3-4B-Instruct 的 1.6 和“最小 degeneracy filter”
  不同，只能视为 later example pipeline，不能声称精确复现主实验。
- **Evaluation Contract**：v1 覆盖 Llama-3.1-8B-Instruct、Qwen3 4B/30B instruct/thinking 五模型；主集
  LCB v6 为 2025-02～05 的 131 题，次集 LCB v5 为 2024-08～2025-02 的 374 题；每题生成 10 个
  independent samples，报告 pass@1/pass@5 与难度切片。headline `42.4→55.3 pass@1` 只属于
  Qwen3-30B-A3B-Instruct、LCB v6、作者指定 generation/SFT/evaluation settings 与代码执行 harness；
  不能脱离 8×B200 training contract、prompt pool、sampling config 或 benchmark 时间窗引用。
- **Baselines / Ablations / Sensitivity / Overhead**：作者将 SSD 与 frozen base 的官方 sampling 和广泛
  `T_eval` sweep 比较；用无 truncation grid 支持 `T_eff`，再用 top-k 5/10 说明 support compression
  提高 ceiling；toy FSM、real-token cumulative mass/entropy 和 `T_train=2` 无 truncation 坏数据 stress
  提供机制交叉证据，OOD 评估覆盖 AIME、HumanEval、CruxEval、MMLU。可是 hyperparameter search 与
  headline 都在 LCB v6 上，没有独立 tuning set；论文未披露训练 seeds/repeats、置信区间、统计检验、
  data-generation/training wall-clock、GPU-hours、energy/cost、evaluation concurrency 或 SLO。小模型 OOD
  trade-off 比 30B 更不稳定，也没有 verified-SFT、teacher-distillation 或 matched-compute RLVR 直接对照。
- **What the Evidence Proves**：在作者披露的五模型、prompt pool、训练和 LCB v5/v6 contract 下，先改变
  self-sampling distribution 再做 SFT，能超过 frozen model 的 global decode-only sweep；temperature 与
  truncation 都产生非零 learning signal，support compression + within-support reshaping 是与 toy、real
  logits 和 grid ablation 一致的解释。官方 checkpoints/model cards 证明至少三项研究权重已公开。
- **What It Does Not Prove**：不证明 raw wrong programs 提供了新的语义知识，也不证明任意 domain、任意
  model 或多轮 self-training 都会提高正确性；高温 stress test 依赖 evaluation truncation 且收益更脆弱。
  `pass@5` 增益大于 `pass@1` 只与 coverage/diversity 相容，不直接测量轨迹独立性或 selector 能力。
  理论依赖 population expectation、teacher-visited contexts、fixed support 与 local ideal fit，不是有限样本
  deep-network convergence theorem；v2 的 GPT-OSS 结果也不是 W14 event-time 证据。
- **Limitations / Threats to Validity**：论文缺显式 limitation section；主要威胁包括 code-only domain、
  单一 prompt source、benchmark 上调参和评测复用、无 run variance、minimal-filter 定义与 later code
  不一致、未公开训练 pipeline、未测 contamination/memorization、较小模型 OOD regression，以及模型自己
  生成的系统性错误被 SFT 固化。公开 evaluator 用 6 秒 test timeout，运行 untrusted code 的 isolation/
  resource/security contract也没有在论文中成为实验变量。
- **Trade-offs / New Failure Modes**：SSD 省去 teacher/verifier/RL runtime，却仍支付一次 full generation +
  SFT，并把 correctness filtering 换成 sampling/optimization selection risk。truncation 清理 tail 也可能删掉
  低概率正确 branch；高温扩大 coverage 也扩大 garbage 和长输出成本；窄 code prompts 可提高 LCB，亦会
  造成 specialization/forgetting。独立调 `T_train/T_eval` 增加可控性，也新增 configuration search、
  checkpoint-policy coupling 与 deployment skew；多轮迭代可能放大 mode bias 或 collapse。
- **Where Previous Design Still Applies**：高风险 code、可靠 tests、需要 provenance 或系统性错误严重时，
  verified synthetic SFT / RLVR 仍优先；strong teacher 有独立能力且成本可接受时，teacher/context
  distillation 仍提供外部 signal；模型已足够好、不能训练或需按请求回滚时，decode-only policy 仍合理；
  general capability 需要保护时应保留外域 mix、regression gate 或不更新 checkpoint。
- **Evolution Relationship**：`Direct Evolution`：global decode-only tuning → temperature/truncation-shifted
  self samples → SFT-compiled distribution → separately tuned serving decode；与 verified self-training、
  teacher distillation、RLVR 是 `Alternatives / Coexisting Branches`，不是后者被替代。Ch20→Ch25 是
  `Layering / Dependency`：sampling 先定义 targets，SFT 再把 target geometry 写入 weights；Ch62 只拥有
  independent evaluation 与 workload contract。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch20、Ch24～29、Ch62。Ch20 已说明 global
  sampling 不创造知识、processor order/seed/version 属于 contract，但尚未显式区分“只在 runtime 采样”与
  “把 transformed sampling distribution 编译进参数”；Ch25 已有 synthetic-data verifier、teacher/context
  distillation、forgetting 与 training-serving skew，却缺少 self-target fixed point、support gate 和独立
  train/deploy decoding policy。Ch27～29 的 reward/verifier 路径是共存分支，不应成为主 owner。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate
  Closed)`。Gate 通过后由 Ch25 补足 self-generated target distribution、fixed-point escape、support
  compression / reshaping 与共存边界；Ch20/62 只加短 handoff。当前不修改 Books，不沉淀跨模型通用
  gain，也不把 v2 或 later repository behavior 倒写为 W14 v1。
- **Open Questions**：在独立 validation set 选择 `T_train/T_eval/top-k/top-p` 后，held-out code 与非 code
  任务是否仍增益？matched prompts/compute 下，unverified SSD 与 correctness-filtered SFT、teacher
  distillation、RLVR 的收益/成本如何分解？多 seed 的方差和迭代 self-distillation 是否出现 collapse？
  current repository 何时公开 event-aligned Megatron recipe、main configs、dataset manifest、checkpoint
  lineage 与 raw results？怎样检测错误 mode 被 support compression 放大，而不是只看 aggregate pass@k？

### MemRerank: Preference Memory for Personalized Product Reranking — 22/30

- **Candidate / Week / Score**：MemRerank；2026-W14；22/30。
- **Source Family ID / Type**：`MEMRERANK-DOWNSTREAM-UTILITY-PREFERENCE-MEMORY`；arXiv v1/v3
  paper + author dataset card。未找到作者 code、checkpoint、训练配置仓库或 immutable release；公开
  artifact 只足以核对数据 schema，不能重放 extractor training 与 top-100 reranking。
- **Event Date / Revision History**：arXiv v1 2026-03-31，v2 2026-04-02，v3 2026-06-17；本周事件按
  v1 归档。v3 comment 只写 metadata author-name correction，但正文将单类目 `1-in-5` 改成两类目、
  四 retriever 的 top-100 contract，并新增 reward/data/evaluation，属于实质 revision，不能倒写为 W14 事实。
- **Access / Full-read Coverage**：已读 v1/v3 metadata、Introduction/Related Work、dataset construction、
  完整方法与 reward 公式、baselines、implementation、main results、prompt/history-length 与 v3 component
  ablation、Limitations、Conclusion、prompts/data appendix；核对 Hugging Face dataset card、split/schema、
  source/license 与 viewer failure，并读 Ch29、Ch62、Ch68、Ch72～74。
- **Original Problem**：把长 purchase history 原样塞给 reranker 会增加 token/cost，也混入与当前商品
  类目无关、过时或弱相关的行为。静态 profile 又可能只优化语言压缩质量，而不知道哪些摘要真的改变
  downstream ranking。
- **Why the Previous Design Was Reasonable**：raw history 保留最高 fidelity，无需 extractor training、
  derived-state lifecycle 或额外 judge；短历史、强 session intent、需要逐条证据审计时仍更可靠。
  query-conditioned retrieval 在意图变化快时也比一次预计算的长期 profile 更敏感。
- **Changed Constraint / Principle**：当同一用户历史被多次复用、Context 有限且 ranking 是明确下游任务时，
  可把 preference memory 视为 query-independent materialized view，并用 task utility 而非 summary fluency
  选择 view；但 optimization target、provenance 与 user-control 必须成为 memory contract 的一部分。
- **Mechanism**：Qwen2.5-7B-Instruct 将目标交互之前的历史按 target category 分成 within-category 与
  cross-category，输出 `M_W` 或 `M_WC`。GRPO 为同一 history 采样一组 memories；o4-mini 对一个 positive
  加四个按 top-100 rank bucket 采样的 negatives 做五次 setwise selection，positive-selection fraction
  是 utility `u5`。v3 再用 `r=u5+lambda*q(M)` 加入小权重 deterministic regularizer，约束 tags、长度、
  repetition、placeholder 和 evidence support；inference 时预计算一份 memory，再经多次五候选比较聚合
  fixed top-100 ranking。Evidence snippets 被保留用于 audit，但在 reward 与最终 reranking 前被移除。
- **State Ownership / Control and Data Flow**：source owner 持有带 timestamp、category、verified flag 的
  immutable interactions；memory service 持有 extractor/prompt/reward version、source IDs、derived profile、
  confidence、expiry、supersession、consent 与 delete lineage；retriever 持有 candidate-pool identity；reranker
  只消费 query、candidate set 与经过 policy 的 profile。论文实现让 model 生成 derived view、API reranker
  给 reward，却没有定义生产 write approval、correction、revocation、staleness 或 delete propagation。
- **Implementation Details**：v1 只用 Electronics，train/dev/test 为 905/194/194；candidate 是 Qwen3-8B-
  Embedding 检索的一正四负，memory output 上限按 within 或 within+cross 设 512/1024。v3 改为 Electronics
  与 Beauty & Personal Care、75:15:10 split、BM25/BLAIR-large/Qwen3-Embedding-8B seen retrievers 与 held-out
  Linq-Embed-Mistral；训练 5 epochs、rollout size 8，metadata 截至 120 words。GPU、训练时长、token/API
  cost、checkpoint、seed、并行、功耗、serving latency 与 SLO 均未披露。
- **Evaluation Contract**：v1 是同类目一正四负、GPT-4.1-mini/o4-mini 各采样五次的 1-in-5 accuracy，
  `+10.61` 只属于 o4-mini + think-tag 的特定配置；v1 的 `Ablation Study` 标题为空。v3 才在 full corpus
  fixed top-100 上报告 MRR@10/MRR@5，并把未召回 positive 的 query-retriever pair 记零。作者按 category
  用 dev reranking 选择 memory target/checkpoint；主表 Electronics 用 `M_WC`，Beauty 用 `M_W`。
- **Baselines / Ablations / Sensitivity / Overhead**：v1 比 no-memory、raw/product context、base extractor、
  GPT-5.2、MR.Rec、Mem0，并检查三个 prompts、history length 与 think tag；v3 改为 GPT-5.5、MR.Rec、Mem0、
  no-RL，并控制相同 metadata window，消融 `M_W`/`M_WC` 与 `lambda=0/.4`。v3 的 row-level gains 有正有负，
  只有 category/macro average 与两个 held-out-retriever rows 最优；没有 multi-seed/confidence interval、
  user study、online conversion、freshness/delete test、cross-domain 或不同 reward/final reranker 的独立性消融。
- **What the Evidence Proves**：在作者两类目、synthetic query、fixed-pool、o4-mini setwise contract 下，
  compact learned derived memory 的 macro-average MRR 高于所测 baselines，held-out dense retriever 也有增益；
  `M_W`/`M_WC` 结果支持跨域历史不是单调有益，quality regularizer 在四个 category-target 配置中改善均值。
- **What It Does Not Prove**：不证明购买或五星评论等于真实当前偏好，不证明 query-independent profile
  对开放商品、自然用户 query、更多类目/语言/模态或 online SLO 有效，也不证明 GRPO 单独造成收益。
  同一个 proprietary o4-mini 是 training reward 与 final judge，可能把 judge preference 写入 memory；
  held-out retriever 只检验 candidate-source shift，不是 reranker、domain、user 或 time shift。
- **Limitations / Threats to Validity**：作者明确只测两类 Amazon 类目、text metadata/purchase history，且
  reward/evaluation 依赖高成本 proprietary API。query 来自 5-star review 再经 o3-mini 删除 brand/spec/
  price/personal-preference details，positive 是 target interaction；这会把 label、query 与 memory 的因果关系
  变成 synthetic proxy。dataset card 写 history cut at first positive-purchase time，论文写 before target 并
  remove positive，边界措辞需 artifact-level 再核对；release 保留 user ID，且未只筛 verified purchases。
- **Trade-offs / New Failure Modes**：预计算 profile amortize 重复读历史的成本，却引入 stale preference、
  taxonomy-dependent partition、cross-category contamination 与 derived-state invalidation。downstream reward
  提高 task alignment，也会 reward hack、固化 reranker bias、放大 popular-item/proxy preference；删去 evidence
  后消费端更短，却削弱在线可解释性。原始历史有隐私与 token 风险，浓缩 profile 则把敏感行为变成更易复用、
  泄漏和跨场景误用的高密度状态。
- **Where Previous Design Still Applies**：短/一次性 session、意图突变、要求逐条引用、低复用或 consent
  不足时使用 raw/selected evidence；偏好稀疏或跨类目 transfer 不稳定时只用 within-category；无可靠
  write/delete governance 时宁可不持久化 derived profile。高风险推荐仍需 deterministic policy 与人工控制，
  不能把 reward-trained memory 当作用户确认事实。
- **Evolution Relationship**：`Direct Evolution`：raw history injection → prompt-extracted summary →
  downstream-utility-trained derived view → source-linked、versioned、consent-aware profile；与 Ch72 的
  candidate retrieval/reranking、Ch29 的 reward optimization、Ch62 的 evaluator independence 和 Ch68 的
  personal-data governance 是 `Layering / Dependency`。
- **ROADMAP / Chapters Read / Existing Coverage**：已读 Ch29、Ch62、Ch68、Ch72～74。Ch73 已有
  derived semantic view、source episodes、downstream-utility-trained selector、provenance/supersession/delete、
  user confirmation 与 evaluation contract，是主 owner；MemRerank 新增的是“query-independent profile
  作为 task-optimized materialized view”、category-conditioned scope 与 reward/judge feedback-loop 的受限
  evidence。Ch72 只承接 first-stage candidate identity/setwise reranking，其他章节只作风险 handoff。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate
  Closed)`。Gate 通过后由 Ch73 补足 task-optimized derived view 的 objective/version、judge leakage、
  category scope 与 coexistence；Ch29/62/68/72 只短连接。现在不修改 Books，不保留作者 headline 数字。
- **Open Questions**：用独立 open-weight reward/evaluator、真实 user queries 与 online/offline matched
  contract 时增益是否仍成立？purchase/review、preference 与 relevance 如何分离？profile 如何支持 consent、
  inspect/correct/delete、time decay、category migration 与 source-level provenance？完整训练/serving 成本相对
  每 query retrieval/compression 的 amortization break-even 在哪里？

### How many raters are enough? — 24/30

- **Source Family ID / Type / Date**：`RATER-SAMPLING-UNCERTAINTY`；Google Research
  2026-03-31 官方研究页及其论文/appendix。
- **Full-read Coverage**：已覆盖任务与 rating protocol、rater sampling、aggregation、置信区间、
  sensitivity 和局限；没有把实验中的 rater 数当作固定生产阈值。
- **Problem / Previous Design / Changed Constraint**：少量 rater 对低方差、强效应、低风险比较
  成本合理；模型差距缩小、prompt 异质和 subjective criteria 增大后，sampling error 可能大于
  被测改进。
- **Mechanism / Ownership / Flow**：item、rater 和 repeat 构成多层 sampling；evaluation owner
  必须依据目标 effect size、variance、aggregation 和 decision loss 设计 power/uncertainty，
  不能由 benchmark harness 隐式决定。
- **Evidence / Limits / Trade-offs**：研究证明其设定下样本量与结论稳定性的关系，不证明存在
  通用 rater 数；增加 rater 降低 sampling error，却增加成本、漂移和 population mismatch。
- **ROADMAP / Chapters / Decision**：Ch62 主 owner，已读 Ch61～63、Ch69；
  `No Change — Already Covered`，当前章节已有 uncertainty 与 decision threshold。

### Behavioral-disposition alignment — 21/30

- **Source Family / Coverage**：`BEHAVIOR-DISPOSITION-MEASUREMENT`；Google Research
  2026-04-03 官方研究页与关联论文；已覆盖 disposition 构造、跨 prompt/语言测量、相关性和限制。
- **Mechanism / Evidence Boundary**：重复行为模式可被外部 probe 量化，但 behavior consistency
  不是内部价值、causal mechanism 或 deployment safety 的充分证据；sampling policy、model
  version、prompt distribution 和语言均属于 measurement contract。
- **Evolution / Decision**：与 Assistant Axis/Persona Selection 为 `Layering / Dependency`，沿
  observation→intervention→replication 证据梯度定位。Ch5、Ch62、Ch68 已读；
  `No Change — Already Covered`。

### HippoCamp: Benchmarking Contextual Agents on Personal Computers — 23/30

- **Candidate / Week / Score**：HippoCamp: Benchmarking Contextual Agents on Personal Computers；
  2026-W14；23/30（3 / 4 / 4 / 4 / 4 / 4）。评分维持：benchmark/evidence schema 具有长期系统价值，
  但只有三个 archetypal profiles，baseline tool/budget 并未全局匹配，也没有生产生命周期或独立复现。
- **Source Family ID / Type**：`HIPPOCAMP-PERSONAL-FILES-CONTEXTUAL-AGENT-EVAL`；arXiv metadata/
  primary paper + official project page + author GitHub repository + official Hugging Face dataset/card。
  project、dataset 与 repository 用于核验 released artifact，论文正文拥有机制与实验 claim。
- **Event Date / First-public Date / Revision History**：arXiv:2604.01221 仅有 v1，2026-04-01；W14
  归档正确。GitHub history 显示 initial public release 为 2026-03-26，3 月 29～30 日重组 release docs、
  增加五种 advanced RAG strategies，4 月 2 日仍在更新文档；GitHub 无 Release/tag。paper event、
  preprint revision、repository commit 与 later leaderboard state 必须分开。
- **Access and Verification Status / Full-read Coverage**：2026-08-11 已通过 official arXiv primary-text
  rendering 完成全文复核，覆盖 metadata/v1 history、Abstract、Introduction、Related Work、benchmark
  construction、profile selection/interviews、trajectory/evidence schema、atomic units、annotation/QC、task
  taxonomy、difficulty、complete experiments、capability/failure analysis、evaluation regimes、metrics、judge
  audit 与相关 Appendix；同时复核项目页、dataset schema/viewer、repository history/release 和 reproduction
  entrypoints。arXiv 仍没有独立 HTML URL，但这不再构成 primary-text blocker。
- **Original Problem**：现有 Agent benchmark 多测 web、tool use 或 software automation；即使加入 RAG，
  也常把 personal context 压缩成短文本或干净 corpus，难以同时测量在 device-scale heterogeneous files
  中的搜索、multimodal evidence perception、entity/time grounding 与跨文件 profile inference。
- **Why the Previous Design Was Reasonable**：标准文本 RAG 与静态 QA 在 corpus 可解析、evidence unit
  清楚、privacy 风险低时便宜、易复现，也适合单独诊断 retrieval。terminal/browser Agent 在工具覆盖
  不完整、文件类型多样时保留环境操作能力。HippoCamp 的公开材料没有证明两者应被单一“personal
  memory architecture”替代；它评测的是外部文件环境中的 contextual behavior，不是内部 memory
  write/update/delete implementation。
- **Changed Constraint / Principle**：personal-computer workload 把规模、模态、folder topology、metadata、
  entity、时间和隐私同时放进证据契约。长期原则是将 `evidence discovery → perception/normalization →
  entity/temporal grounding → multi-hop synthesis → answer/profile claim` 分层评估；最终答案正确不能解释
  中间哪一层成立，检索命中也不等于证据被正确理解。
- **Mechanism**：benchmark 从 100+ participant interviews 与筛选规则构造 3 个 archetypal profiles、
  27 种文件类型、42.4 GB、2K+ files 与 581 QA；分 factual retention 和 profiling 两条 track。
  annotation 把 question/answer、最小支持文件集、file-local evidence、reasoning step 与 search/perception/
  reasoning labels 分离；Atomic Unit 再把 PDF page/region、image region、audio/video timestamp 等 decisive
  evidence 映射到统一 locator。它不是 headline score，而是用来区分“命中文件”和“定位正确证据”。
  论文将典型 failure chain 归纳为 retrieval mismatch → grounding avoidance → hallucinated evidence →
  entity misbinding → missing verification，并据此说明 post-retrieval pipeline 可以成为主要瓶颈。
- **State Ownership / Control and Data Flow**：benchmark owner 持有 immutable raw snapshot、profile/QA ID、
  hidden gold evidence、file locator、rationale/capability labels 与 scorer version；agent 只应看到声明过的
  exposure view。raw files → search/tool observations → perceived evidence → reasoning trajectory → answer/
  cited files → deterministic/semantic/judge scores。若把 `HippoCamp_Gold` parsed text、viewer parquet、
  annotation JSON 或 answer-bearing evidence 暴露给被测 Agent，会把 benchmark 变成 label leakage。
- **Implementation Details**：公开 artifact 提供 raw profile archives、six dataset configurations
  （Adam/Bei/Victoria × fullset/subset）、RAG/search 与 Docker terminal-agent paths，以及 answer metrics、
  retrieval/file-list precision/recall/F1 和 LLM-judge entrypoints。fullset 分布为 Adam 344 files/123 QA、
  Bei 875/235、Victoria 711/223，总计 581；其中 profiling 各 profile 20 条。dataset viewer 暴露
  `file_path`、`file_text`、`gold_text`、`evidence`、`rationale` 等字段，只能用于审计或受控 scorer，
  不能直接作为 raw-environment input。部分 metadata 生成脚本包含 macOS-specific behavior，环境重放
  不能只复制文件内容。
- **Evaluation Contract**：所有系统使用 profile-isolated corpus，不允许 web/external data；但实验明确分为
  native retrieval、Docker terminal 与 hosted Agent 三种 regime。它们共享 corpus/access boundary，却没有
  matched low-level interfaces 或全局统一 budgets。terminal path 提供 list/read/metadata 等工具；hosted Agent
  是 upper-bound-style reference，并不等价于 tool-parallel terminal runtime。answer 由 binary correctness、
  0～5 GPT-4o judge 与 file retrieval precision/recall/F1 测量，能力分数是未加权 subcategory mean。581 QA
  的 profile/task 分布不均，aggregate 不能替代 profile、task、modality、evidence breadth 与 difficulty slice。
- **Baselines / Ablations / Sensitivity / Overhead**：比较 Standard RAG、Self-RAG、ReAct、Search-R1、
  多种 Terminal Agent 与 ChatGPT Agent Mode。论文采用 method-appropriate 而非 globally matched budget；
  重试只处理 malformed/empty/tool failure/timeout，不重试“成功返回但答案错误”，stochastic systems 多为
  point estimate。作者披露 hosted Agent 常需 10～15 分钟/query 且运行不稳定，但没有提供统一 hardware、
  token/tool/cost budget、多 seed/confidence interval 或完整 sensitivity contract。因此 48.3% profiling
  accuracy 等数值只能属于该 paper snapshot，不能解释为通用 Agent 上限或 model-only causal effect。
- **What the Evidence Proves / Does Not Prove**：公开 artifact 证明可以把 personal-file contextual-agent
  evaluation 组织为 realistic raw environment、hidden hierarchical evidence 和 capability-level diagnosis；
  也显示当前 evaluated systems 在指定 artifact/leaderboard contract 下存在 retrieval、perception、grounding
  与 attribution failures。它不证明这些 files/queries 代表真实人口分布，不证明 profiling accuracy 等于
  useful/safe personalization，不证明 benchmark 测到长期 memory lifecycle，也不证明公开榜单差距来自
  某个内部模型或 memory mechanism。
- **Limitations / Threats to Validity**：只有 3 个聚合而成的 archetypal profiles；contributors 同时承担
  domain-aware annotation，虽有 cross-check/secondary review/adjudication，仍可能引入 profile-specific bias。
  论文的 judge audit 只覆盖 stratified ambiguous cases，正文未给出足以跨环境复用的完整 agreement/sample
  contract。external benchmark augmentation 被改写并控制为少数补充，但人口、语言、职业与文件生态仍不
  代表真实部署分布。static filesystem QA 不能测 memory write/update/supersession/delete/forgetting、
  consent change、interactive side effects 或 online adaptation；profiling 还会把分散 traces 升级成 derived
  sensitive claims。项目页的 46.1K annotations 与 artifact 中其他计数单位不能在 schema mapping 前互换。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：更真实的 raw files 提升 ecological
  validity，却显著增加下载、sandbox、parser、metadata 与 modality dependency；hierarchical gold 改善诊断，
  也扩大 answer leakage 和 annotation maintenance surface；profiling 提升 personalization coverage，同时
  引入 consent、purpose limitation、re-identification、derived sensitive inference 和 deletion propagation。
  干净 text RAG benchmark 仍适合 isolated retrieval regression；typed tool benchmark 仍适合 action semantics；
  online memory benchmark 才能覆盖 lifecycle。三者应分层共存，而非以后者否定前者。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：`Layering / Dependency`。主 owner 应从旧 queue 的
  Ch74 调整为 Ch62：它首先是 evaluation object、dataset governance 与 evidence contract；Ch72 接收
  retrieval/perception boundary，Ch73 接收“static personal-file QA ≠ memory lifecycle”的边界，Ch68 接收
  profiling/derived-sensitive-data threat model。已读 Ch61～63、Ch68、Ch71～75 的章节结构与相关论证；
  现有 Ch62 已覆盖完整 subject/environment/scorer identity、claim-bound evidence、dataset governance 与
  judge calibration；Ch72 已覆盖 retrieval relevance、context sufficiency、grounding/verification 的分层；
  Ch73 已明确 external file retrieval 不等于 memory lifecycle；Ch68 已覆盖 derived sensitive inference。
- **Integration Decision / Rejection Reason**：`No Change — Already Covered / Experimental Evaluation Case`。
  全文补强了 personal-file benchmark 的机制案例，但没有形成超出现有章节的长期新原则，也没有推翻既有
  结论。保留在 W14 供 Ch62 future review 使用；Historical Books Gate 关闭期间不修改 Books，后续也不以
  current leaderboard 或单篇 post-retrieval observation 重复扩写正文。
- **Open Questions**：如何在 matched tool permissions、parallelism、tokens/calls/wall-clock 与多次运行下
  重测三种 evaluation regime？Atomic Unit 如何在不发布 raw personal media 的前提下支持独立 scorer audit？
  profiling utility 与 consent/privacy harm 如何形成双目标 gate，并让 derived claim 支持 correction/delete？

### Omni-SimpleMem — 24/30

- **Candidate / Week / Score**：Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent
  Memory；2026-W14；24/30（4 / 4 / 3 / 4 / 5 / 4）。保留原评分：机制与项目相关性强，工程实用性仍受
  两个 benchmark、API-dependent ingestion、缺少生产 lifecycle 与不完整 resource contract 限制。
- **Source Family ID / Type**：`OMNI-SIMPLEMEM-MULTIMODAL-MEMORY-AUTORESEARCH`；arXiv paper v1/v2 +
  author repository + v0.2.0 official release + benchmark/config/code surfaces。后续 EvolveMem 与 unified
  v0.3.0 属 5 月 source family extension，不回写为 W14 event evidence。
- **Event Date / First-public Date / Revision History**：arXiv v1 2026-04-01，标题/正文使用 `OmniMem`；
  v2 2026-04-02 统一为 `Omni-SimpleMem` 并把 code link 指向 SimpleMem repository。v0.2.0 于 2026-04-03
  发布。三者都属于 W14，但必须区分 paper v1 claim、v2 naming/link fix 与 release artifact；current main
  的 v0.3.0 auto-routing、EvolveMem、multimodal MCP 和 later models 不是该周机制证据。
- **Access and Full-read Coverage**：已读 v1/v2 metadata、Abstract、Introduction、Related Work、完整
  AutoResearchClaw loop、三项 architecture mechanism/公式、benchmark-specific optimization、Experimental
  Setup、全部五-backbone results、ablation、efficiency、case study、Conclusion、Ethics、Reproducibility；
  Appendix A/B benchmark/baseline、C architecture/hyperparameters/graph schema、D 23-stage pipeline、E/F
  complete optimization trajectories、G prompts 均已覆盖。另核验 author repository/current implementation、
  v0.2.0 release、reproduction entrypoints 与 version drift。
- **Original Problem**：长期 Agent 同时积累 text、image、audio、video 时，raw retention 造成 storage/context
  bloat 与 retrieval noise；text-only structured memory 又丢失非文本 evidence。设计空间还同时包含 ingestion、
  storage、retrieval、prompt、data pipeline 和 benchmark adapter，手工少量调参容易把 harness bug、数据缺失、
  architecture 与 hyperparameter gain 混在一起。
- **Why the Previous Design Was Reasonable**：raw embedding retrieval 在数据少、单模态、query 简单时 state
  最少、证据保真；text summary/structured memory 在对话型 workload 中压缩比高、可快速搜索；manual design
  对高风险或弱 evaluator 任务保留人类因果判断。它们并未失效：Omni-SimpleMem 自己在 Mem-Gallery 发现
  full original dialogue 比 summary 更适合 token-overlap F1，证明“先压缩再检索”不是全局单调改进。
- **Changed Constraint / Principle**：当 raw evidence 成本跨越数个数量级，memory 必须把 cheap control/index
  state 与 expensive exact evidence 分层；read policy 不再只选 top-k，还要决定何时从 summary 展开到 detail/
  raw。系统优化只有在 evaluator 快、模块边界清晰、artifact versioned 且 rollback 可靠时才适合 autonomous
  closed loop；否则 metric improvement 可能只是 scorer alignment 或 data repair。
- **Mechanism**：ingestion 先用 modality-specific novelty filters：相邻 visual frame 的 CLIP similarity、audio
  VAD、text Jaccard dedup；保留项编码为
  `MAU=<summary, embedding, raw pointer, timestamp, modality, links>`。hot tier 保存 summary/embedding/metadata，
  cold tier 保存 full text/raw media。query 同时走 normalized dense FAISS 与 BM25，保留 dense order 并 append
  BM25-only set；pyramid retrieval 先返回约 10-token summary，超过 similarity threshold 才展开 full text/
  caption，再按 similarity-per-token 与 budget `B` 贪心加载 raw evidence。LLM 抽取 typed entity/relation，
  entity resolution 后做 bounded h-hop、distance-decayed graph expansion。
- **State Ownership / Control and Data Flow**：memory platform 必须分别拥有 immutable raw asset、MAU/summary
  revision、embedding/index version、timestamp/modality、graph node/edge provenance、entity merge/split lineage、
  authorization/retention/delete state；retriever owner 持有 dense/sparse/graph candidate set、score/order、expansion
  threshold、token budget 与 fallback；research-loop owner 持有 hypothesis、code commit、dataset/split、config、
  run artifact、metric、decision/revert lineage。若只回滚 code 而不回滚 index、derived MAU/graph 或 benchmark
  cache，`PROCEED/PIVOT` 并非可重放 transaction。
- **Implementation Details**：论文实现约 13,300 行 Python/11 subpackages；MAU JSONL、FAISS、filesystem/S3
  cold storage，central orchestrator 873 lines。paper event 使用 FAISS、BM25、frozen CLIP ViT-B/32、GPT-4o
  JSON entity extraction；default top-k=20、theta=0.4、B=6,000，graph expansion h=2、decay beta=0.7。
  LoCoMo/Mem-Gallery 的 embedding、top-k、budget 与 per-doc memory 不同。current README 改为 OpenVision CLIP
  ViT-L/14、12 relation types、126 tests/MCP/unified package，和 paper 的 CLIP ViT-B/32、7 relation types 形成
  implementation drift；不能用 current main 反证或替换 event-time result。
- **Evaluation Contract**：LoCoMo 为 1,986 QA/10 conversations、五类问题、token-level F1；pipeline 在
  conv-26 的 199 QA 上迭代，再跑完整 benchmark。Mem-Gallery 为 1,711 QA、240 multimodal dialogues、1,003
  images，按小 subset 快速迭代后评完整 benchmark。约 50 个 experiments/约 72 小时；LoCoMo 9 accepted
  iterations + 2 reverted，Mem-Gallery 39 experiments/7 phases。最终比较 6 baselines × 5 backbones；正文未
  披露执行这些约 50 runs 的 CPU/GPU 型号、API snapshot、总 tokens/cost、并发、network/retry accounting，
  因而 throughput 和 research velocity 不能外推到生产 SLO。
- **Baselines / Ablations / Sensitivity / Overhead**：baselines 为 MemVerse、Mem0、Claude-Mem、A-MEM、
  MemGPT、SimpleMem。LoCoMo component ablation 在四个 backbones 上报告移除 pyramid、BM25、LLM summary、
  降 top-k、移除 metadata 的 mean delta；但没有 knowledge graph、novelty filtering、entity resolution、
  cold-storage failure、threshold/budget sensitivity 或 ingestion quality 的完整独立消融。单 worker 时
  OmniMem 是 1.05 q/s，低于 SimpleMem 1.68；8 workers 利用 read-only indices 达 5.81 q/s，但 Gen 仍为
  821 ms、retrieval aggregate 461 ms，论文未给硬件、request mix、memory footprint、p95/p99 或 update/read
  contention，因此“3.5x faster”只绑定该并行 benchmark contract。
- **What the Evidence Proves**：在作者给定的两个 datasets/splits、prompts、metrics 与五个 backbones 上，
  hybrid candidate preservation、progressive expansion 与 compact/raw separation 是有 ablation support 的
  有效组合。optimization log 还证明该 harness 中最大增益来自 missing JSON response format、corrupted
  timestamps、BM25 tokenization、full-text exposure 与 prompt placement；这支持一个更长期的系统原则：
  **先确认 evaluation/data pipeline correctness，再把剩余 delta 归因给算法。** 四次 Mem-Gallery final runs
  在 0.791～0.797，只支持该 phase 的局部 plateau。
- **What It Does Not Prove / Claim Boundary**：`+411%/+214%` 相对的是 deliberately naïve initial
  configurations，不是相对 prior SOTA；相对 best baseline 的绝对/相对差距应另算。F1 上升不证明 storage
  “lossless”、真实长期 user utility、因果上由 autoresearch 而非 evaluator-aware human framing 导致，也不证明
  autonomous pipeline 比同预算专家或 Bayesian/search baseline 更优。只在最终完整 benchmark 跑一次不能排除
  iterative dev-subset overfitting、prompt/scorer coupling 或 benchmark-specific branches。
- **Limitations / Threats to Validity**：论文无独立 `Limitations` section；可从 contract 明确看到只有两个
  academic benchmarks、无 real user/online writes、无 adversarial memory poisoning、conflict/correction、
  deletion/forgetting、consent change、multi-tenant ACL、crash recovery 或 index rebuild evaluation。graph triple
  与 summary 都由 LLM 派生，错误可被 merge/expansion 放大；novelty filter 是 destructive gate，discarded
  rare evidence 无法由后续 retriever 恢复。token-overlap F1 会奖励 exact copying 和 format alignment，且论文
  没有 matched human-search/AutoML baseline、run-level variance for main cross-system table 或 statistical tests。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：selective ingestion 节省 storage，却引入
  irreversible false-negative、threshold drift 和 modality bias；hot/cold separation 降低 steady-state context，
  却新增 pointer lifecycle、availability、authorization 与 delete propagation；dense+sparse union 保住 lexical
  recall，却扩大 candidate set 且没有统一 calibrated score；graph expansion补 relation，却引入 entity collision、
  stale edge 和 sensitive profiling。deterministic pyramid 避免额外 judge call，但用同一 cosine score控制不同
  modality/level，未必校准。raw full context 在 small/high-risk corpus、simple text RAG 在 latency-critical workload、
  manual review 在 weak/noisy evaluator 仍合理。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：`Direct Evolution` from SimpleMem text-only memory；
  与 Ch72 hybrid/agentic retrieval、Ch62 feedback-conditioned evaluation、Ch68 privacy、Ch77 research workflow 是
  `Layering / Dependency`。主 owner 为 Ch73，因为长期稳定机制是 memory representation/tiering/read policy/
  lifecycle boundary，不是 tool API。已读 Ch72～74、Ch62、Ch68、Ch77 及邻接结构；Ch73 已有 compact control
  state vs exact evidence archive、read policy、consolidation/deletion，Omni-SimpleMem 可在 Gate 后 refine 为
  multimodal evidence tiering 与 destructive-ingestion trade-off，而非新增孤立案例。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate
  Closed)`。待全历史 Gate 通过后，只考虑把 hot metadata/cold evidence、progressive expansion、derived graph
  provenance 与 “harness/data repair precedes algorithm attribution” 机制吸收进 Ch73/Ch62；不写 SOTA 榜单、
  repository feature list 或 fixed thresholds。
- **Open Questions**：在 immutable raw archive 前保留 novelty-filtered rejected candidates 的成本是多少？
  如何对 summary、graph edge 与 index 做 source-linked delete/rebuild/rollback？matched human/AutoML search budget、
  held-out benchmark family、run variance 与 full compute/cost contract 下，autoresearch 的独立贡献还剩多少？

### S0 Tuning — 23/30

- **Candidate / Week / Score**：S0 Tuning；2026-W14；23/30（4 / 4 / 4 / 3 / 4 / 4）。全文后将
  Source Reliability 从 4 降为 3：论文的核心机制与实验表格可读，但作者 model card 对 layer/state shape、
  training hardware 与 base identity 的描述和论文不一致，中央 HumanEval 10-seed artifact 也未公开。
- **Source Family ID / Type**：`S0-RECURRENT-LAUNCH-STATE-ADAPTATION`；arXiv v1/v2 + author repository、
  package releases、experiment documentation、trained-state model card 与 training dataset card。
- **Event Date / First-public Date / Revision History**：arXiv v1 2026-04-01，v2 2026-04-03；W14 事件按
  v1 归档。PyPI 0.1.0/0.1.1 于 03-30、0.1.2 于 04-02；current repository/model card 只能用于 artifact
  核验，不能倒写为 v1 已证明的版本事实。
- **Access and Full-read Coverage**：已读 v1/v2 metadata、Abstract、Introduction、Background、GatedDeltaNet/
  Mamba-2 recurrence、完整方法/算法/公式、Experimental Setup、主结果、matched/alternate baselines、controls、
  mechanistic analysis、Related Work、Discussion/Limitations、Conclusion；并覆盖全部 appendices 中的 hyperparameters、
  layer/alpha/data sensitivity、per-seed tables、matched-parameter LoRA、pass@k、probing 与 scale experiments，核验
  author repository、tests/experiments、PyPI、HF state 与 dataset cards。
- **Original Problem / Why Previous Design Was Reasonable**：LoRA 等 weight adapter 为新任务提供持久参数化，
  适用于 Transformer 与 recurrent model，也便于训练/合并；prompt/prefix 则不改权重但会持续占用 context 或每层
  compute。对含 recurrent layers 的 hybrid model，是否存在只改 recurrence 初始条件、在生成每一步不再执行
  adapter 的更窄控制面？旧方案仍合理，因为它们跨架构、容量可调，且不依赖 initial-state influence 能穿过长 prompt。
- **Changed Constraint / Principle**：hybrid recurrent/attention model 暴露了权重与 prompt 之外的第三个适配面：
  每层 recurrent state 的 launch condition。长期原则是把 adaptation artifact 定义为“改变哪段 state transition、
  生命周期多长、每 token 是否持续付费”，而不是把所有 PEFT 统称为 weight delta。
- **Mechanism**：冻结全部模型权重，对每个 recurrent layer 学习与 native state 同形的 `S0^(l)`，并从
  `alpha*S0` 启动 recurrence；目标为 completion-only cross-entropy 加 L2 regularization。GatedDeltaNet 中
  `S_t = alpha_t S_{t-1}(I-beta_t k_t k_t^T)+beta_t v_t k_t^T`，Mamba-2 中
  `S_t=Abar_t S_{t-1}+Bbar_t x_t`。artifact 只在 t=0 注入，因此没有 LoRA 那样的 per-token adapter matmul；
  但加载、选择、batch 对齐、state 初始化和缓存身份不是零成本。
- **State Ownership / Control and Data Flow**：trainer 拥有 task-specific S0 tensor、alpha、base-model revision、
  layer/state-layout schema 与 optimization provenance；serving runtime 在 request/session admission 时选择并校验
  artifact，把它注入匹配的 recurrent layers，再由冻结 transition 传播。KV/recurrent state、prompt prefix、
  adapter identity 与 speculative/rollback lineage 必须共同进入 cache/batch identity；模型本身不应拥有 artifact
  registry、租户授权、eviction 或 rollback。
- **Implementation Details**：论文对 Qwen3.5-4B 报告 24 GDN + 8 attention、约 12.6M state parameters
  （0.3%），FalconH1-7B 报告约 34.6M（0.5%）。S0 用 Adam、lr 1e-3、20 steps、batch 1、L2 5e-4、
  bf16，在单张 A10G 24GB 上约 3 分钟；主 LoRA 为 rank 24、约 4.7M parameters、50 steps、约 5 分钟。
  当前 HF card 却写 Qwen 为 27 layers、21 GDN + 6 attention、`16x192x128` state，并写单 A100；虽然参数量
  近似相同，这仍是不能静默消解的 artifact-identity conflict。
- **Evaluation Contract**：HumanEval 共 164 题，0～79 作为训练 problem、80～163 共 84 题测试；每个训练题
  最多保留一个 execution-verified solution，论文称约 48 个。另测 MATH500、GSM8K、Spider；Qwen 主结果
  10 seeds，Falcon 3 seeds，Spider alpha scan 只有 single seed。除训练 A10G 外，evaluation hardware、runtime、
  decode/batch、input/output length、quantization、并发、tail latency 与 SLO 均未披露。
- **Baselines / Ablations / Sensitivity / Overhead**：Qwen HumanEval 从 48.8 到 72.2（+23.6±1.7pp），最佳
  rank-24 LoRA 为 61.5±5.1；但 LoRA 参数量未 matched。rank-64 matched-parameter LoRA 在相同固定超参下
  8/10 seeds collapse，只证明该 recipe 不稳，不证明 matched LoRA 的能力上限。Falcon S0 71.8±1.3 与 LoRA
  71.4±2.4 在 3 seeds 下不可区分。state-offset +27.1 但每步有 overhead。MATH500 +4.8±1.4、GSM8K
  +2.8±1.6、Spider +0；early/middle/late layer 与 10/25/50 solution studies 多为 single/3 seeds，alpha 对架构
  高度敏感。pure-Transformer prefix tuning 的九组负结果不是 S0 对纯 Transformer 的直接对照。
- **What the Evidence Proves / Does Not Prove**：在作者给定的两个 hybrid recurrent architectures、少量
  verified solutions 与 benchmark contract 下，learned initial states 能显著改变部分生成行为；27 个 fail→pass
  中 23 个在首个生成字符分叉，且 prompt 末端直接 KL influence 仅约 0.03%，支持“持久效果由早期 trajectory
  branching 放大，而非 prompt 末端仍有强直接作用”。state probe AUC 0.930 vs residual 0.905 是描述性证据，
  不是因果定位。结果不证明通用 PEFT 替代、长 prompt 稳健性、跨 domain transfer、production latency gain
  或无 per-request state-management cost。
- **Limitations / Threats to Validity**：作者明确承认 code→math transfer 较小、SQL 无收益、方法目前只覆盖
  matrix-valued recurrent states；先前 diagonal Mamba-1 initial-state 方法可能弱于 LoRA；训练依赖 verified
  solutions，HumanEval 可能存在 pretraining contamination，且受个人 GPU 预算限制。额外风险是 train/test
  同属 HumanEval、主结果 artifact 不全、base revision 未锁定、paper/model-card layout 与 hardware 冲突、
  scale curve 被不同 baseline behavior 混杂。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：S0 避免逐 token weight-adapter compute，
  却把适配容量绑定 state shape/层数，并新增 alpha collapse、长 prompt washout、wrong artifact/layout injection、
  cache contamination、tenant mix-up 与 rollback 问题。LoRA 在纯 Transformer、需要更大/分层容量、希望 merge
  权重或长序列稳定影响时仍成立；prefix/prompt 在无需 artifact registry、低风险临时 steering 时仍成立；
  per-step state offset 以持续 compute 换更强控制，也不是被 S0 单向淘汰。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：`Direct Evolution`：prompt/prefix control → weight
  adapters → recurrent launch-state artifact → per-step state offset；与 recurrent model internal state 是
  `Layering / Dependency`，与 Agent long-term memory 仅是 `Explanatory Analogy`。主 owner 为 Ch26 LoRA/PEFT，
  handoff Ch22（recurrent state ≠ durable memory）、Ch31（artifact identity/checkpoint）与 Ch46（dynamic loading/
  batching）。已读 Ch26、Ch31、Ch22 相关段落与 Ch46；Ch26 已覆盖 parameterization/objective/artifact/dynamic
  loading，但尚缺 state-initialization 这类非 weight、非 prompt adaptation surface。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Artifact Identity Inconsistent;
  Provisional; Historical Books Gate Closed)`。Gate 通过后可在 Ch26 扩充 adaptation-surface taxonomy 与 state
  artifact contract；在 exact base revision、layer layout、hardware 与 public result artifact 对齐前，不写入
  具体 checkpoint/layout 或通用性能结论。
- **Open Questions**：哪一 base revision 与 state layout 产生论文主结果？A10G/A100、24+8/21+6 的差异来自
  typo、版本 drift 还是不同 artifact？长 prompt、continuous batching、prefix/KV sharing、speculation/rollback、
  multi-tenant dynamic loading 下如何定义 S0 identity 与 isolation？在 matched parameter、tuned hyperparameters、
  independent dataset family、公开 10-seed artifact 与 end-to-end serving contract 下，S0 相对 LoRA 的边界在哪里？

### Learning to Learn-at-Test-Time (Meta-TTL) — 23/30

- **Candidate / Week / Score**：Learning to Learn-at-Test-Time: Language Agents with Learnable Adaptation
  Policies；2026-W14；23/30（4 / 4 / 3 / 3 / 5 / 4）。全文后将 Source Reliability 从 4 降为 3：
  v1 的任务/模型/episode contract 可核验，但没有 seed、variance、hardware、token/API cost、sampling snapshot
  或 statistical test；current code 与论文 episode/model/selection contract 也存在明显 drift。
- **Source Family ID / Type**：`META-TTL-LEARNED-REFLECTION-POLICY`；arXiv v1/v2/v3 + author repository、
  dependency snapshot、inner-loop evaluation 与 outer-loop training entrypoints。W14 结论只以 v1/v2 为事件证据；
  7 月 v3 的第三 benchmark、prompt-optimizer/parameter-update baselines 与 adaptation-space ablations 是后续 revision。
- **Event Date / First-public Date / Revision History**：v1 2026-04-01，v2 2026-04-02，v3 2026-07-15。
  v1/v2 HTML 的核心结构与表格未见实质差异；v3 新增 `tau^2-bench`、TextGrad/EvoPrompt/EvoTest、parameter-
  based TTL 与多项控制，不能倒写为 W14 已有证据。author repository 当前仅 2 commits、无 release/tag，
  不能提供 immutable event-time artifact identity。
- **Access and Full-read Coverage**：已读 v1/v2 metadata、Abstract、Introduction、Related Work、POMDP/TTL
  formulation、W-AUC、prompt-based adaptation、完整 inner/outer algorithms、实验设置与四张主表、OOD/机制分析、
  Conclusion、Appendix A 的 normalization、B/C 的 optimized prompt structure、D 的完整 26-iteration trajectory、
  E 的 ID/OOD cases；并阅读 v3 变更区与 later controls，核验 repository structure、frozen dependencies、
  Jericho/WebArena baseline、inner-loop 和 meta-training entrypoints及 release 状态。
- **Original Problem / Why Previous Design Was Reasonable**：Reflexion 或手写 retry rule 直接依赖通用 LLM
  从一次失败生成 feedback，开发成本低、行为可读，并且在任务少、风险高、环境 reward 稀疏或历史 evidence
  不足时更容易人工审计。问题是同一固定规则未必知道怎样跨 episode 做 credit assignment、保留有效经验、
  控制 exploration，也没有被“后续表现是否真的改善”这个目标直接优化。
- **Changed Constraint / Principle**：当一个 workload 允许相同任务从 reset state 重复执行，并提供可比较的
  trajectory reward，Reflection 本身可以被提升为一个独立、可版本化、可离线优化的 adaptation policy。
  但 runtime 使用的 mutable actor prompt 与 offline learned meta-prompt 必须分层：前者是 session state，后者是
  deployed policy artifact；二者都不能覆盖平台 safety/authorization policy。
- **Mechanism**：每个任务是有限时域 POMDP；一场 TTL session 包含 K 个从相同初态 reset 的 episodes，并用
  later-episode 权重 `w_k=k` 的 normalized W-AUC 评价持续改善。inner loop 中 frozen actor 以系统 prompt
  `rho_k` 执行，meta-agent 在读取 `H_k={tau_1...tau_k}` 后按 meta-prompt `phi` 产生 `rho_(k+1)`。outer loop
  采样 parent `phi` 与 training task，在同一任务做 local improvement gate，再在全部 validation tasks 上更新
  per-task expert pool；最终按 validation average（Jericho 另作 candidate-population z-score）选一个 frozen
  `phi*` 部署到 held-out tasks。
- **State Ownership / Control and Data Flow**：evaluation/workflow owner 必须持有 task/environment version、reset
  semantics、episode/trajectory lineage、reward、W-AUC、budget 与 terminal decision；meta-training registry 持有
  candidate prompt digest、parent、proposer/model snapshot、train/validation exposure、per-task score 与 selection
  history；session runtime 持有 `rho_k` version 与 evidence links。meta-agent只能提出下一 actor prompt，不能
  修改 authorization、tool scope、hard constraint、environment truth 或长期 memory policy。
- **Implementation Details**：v1 固定 Gemini 3 Flash actor，分别以 Gemini 3 Flash、GLM-5、GPT-5 作为
  meta-agent；Jericho 用 3 个 ID games/3 个 OOD games、每 session 6 episodes，WebArena-Lite 用 3 个 ID/
  2 个 OOD domains、每 session 5 episodes。作者展示 GPT-5/Jericho 26 proposals、约 27 小时，其中 16 个
  过 local gate、6 个提高 aggregate validation score。current repository README/entrypoints 则示例 3-episode
  Jericho、4-episode WebArena，training defaults 2/3 episodes，并委托 current GEPA package、GPT-5.2 proposer；
  这些是 later runnable surface，不是论文 v1 的 exact reproduction contract。
- **Evaluation Contract / Baselines**：v1 baselines 为 Static、Reflexion、Memory Agent 与相同 actor+meta-agent
  但未优化 meta-prompt 的 Naive；指标为 average score 与 W-AUC。Jericho reward 较密，WebArena success 二元。
  作者报告 GPT-5 meta-agent 的 Jericho ID W-AUC 0.18→0.41、OOD 0.23→0.28；WebArena 增益较小。
  这些数字没有绑定公开 model/API snapshot、temperature、tokens、price、hardware、parallelism、p95 或 SLO。
- **Ablations / Sensitivity / Overhead**：v1 没有 matched outer-optimizer、adaptation-space、model-call/token cost、
  seed/variance、task-count sensitivity 或 safety-policy ablation；这些对照到 v3 才部分加入。v1 自身已暴露边界：
  Zork 3 所有方法随 episode 下降；WebArena OOD 增益主要来自与 ID Shopping 结构相近的 Shopping Admin，
  Reddit 上 GLM-5/GPT-5 基本不增。Jericho post-hoc z-score 依赖本次 candidate population，也会随搜索轨迹变化。
- **What the Evidence Proves / Does Not Prove**：在两个 benchmark、固定 Gemini actor、给定 episode budget 和
  author harness 下，优化 meta-prompt 能比作者实现的手写/naive feedback rule产生更高的跨 episode aggregate
  reward；优化轨迹显示 structured diagnosis、explicit credit assignment、grounded facts 与 bounded exploration
  可作为可学习 policy primitives。它不证明通用 agent 会持续自我改进，不证明 OOD 是语义/界面都远离 training
  distribution，不证明 learned prompt 比所有 hand-designed/gradient methods 更优，也不证明 prompt 改写保持
  safety invariants。后续 v3 controls只能作为演进证据，不能补造 v1 的消融。
- **Limitations / Threats to Validity**：v1 无独立 Limitations section。三项 Jericho training games 容易把
  domain fact bank 混入所谓 task-agnostic rule；论文自己记录 early candidate 把 Detective identity 写死，直到
  后续 mutation 才加 conditional gate。local gate 与 global expert pool反复消费同一 small validation set，存在
  search-level overfitting；reward scale/normalization、environment stochasticity、模型版本漂移、无重复统计、
  same-family feedback blind spot 与 current artifact drift 都限制可复现性。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：learned reflection policy 把经验转成更
  可执行的 diagnosis，却新增 outer-loop compute、validation overfit、prompt bloat、domain-fact leakage、reward
  hacking、unsafe prompt mutation 与 policy rollback；多一个 meta-agent 也增加每 episode latency/cost 和 correlated
  error。手写 reflection 在小样本/高风险/强治理场景仍更易审计；Static 在没有 repeat opportunity 时仍是正确
  baseline；gradient-based TTL 在需要更大适配容量且能隔离 weight lifecycle 时仍是另一分支，而非被 prompt TTL
  否定。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：`Direct Evolution`：fixed reflection prompt →
  task-scoped trajectory feedback → offline search over adaptation policy → frozen meta-policy + mutable session prompt；
  与 Memory 的 derived procedural lesson、Workflow 的 episode/reset/budget state、Evaluation 的 trajectory metric
  是 `Layering / Dependency`。已读 Ch75～77、Ch73 和 Ch62。主 owner 为 Ch76，因为新增长期机制是 Reflection
  rule 本身可以成为可训练 artifact；Ch73 只承接 trajectory/derived fact lifecycle，Ch77 承接 durable control，
  Ch62 承接 W-AUC、held-out 与 uncertainty。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate
  Closed)`。Gate 通过后可在 Ch76 补足 fixed→learned reflection policy、offline policy artifact 与 runtime
  improvement state 的边界；不沉淀模型排名、headline gain、game-specific prompt 或 later v3 feature list。
- **Open Questions**：在 immutable safety policy 下，哪些 prompt fields 可被 adaptation policy改写？怎样用
  independent held-out family、nested validation、repeated runs 和 matched calls/tokens/wall-clock 防止 outer-loop
  overfit？candidate prompt、domain fact、trajectory evidence 与 environment version 如何做 provenance/delete/
  rollback？若环境不能 reset 或 action 有真实副作用，W-AUC 与多 episode学习如何改写？

### MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU — 27/30

- **Candidate / Week / Score**：MegaTrain；2026-W14；27/30。原 W15 discovery score 维持，但
  Source Reliability 从“paper+code”拆成受限的 3：正文存在两处可定位的内部数字冲突，且公开仓库
  没有 event-date immutable release。
- **Source Family ID / Type / Date**：`MEGATRAIN-CPU-OWNED-STREAMING-TRAINING`；作者正式发布页 +
  arXiv system paper + author repository。作者于 2026-04-05 写明 “officially releasing”，故这一天是
  first-public date；arXiv:2604.05091 仅有 v1（2026-04-06）。当前 README 的 04-12 VERL/GRPO 集成仍在
  W15，但 04-17 multi-GPU data parallel 超出 W15；两者都只作 revision/artifact boundary。
- **Direct / Related Primary Sources**：直接来源为作者发布页、arXiv v1 HTML/PDF 和 repository；关系来源为
  论文引用的 ZeRO、ZeRO-Infinity、FSDP、ColossalAI-Gemini 与 Ratel。作者博客能解释设计动机与 Muon/
  activation-offload 未解决项，不能替代 paper evaluation；current README 的 later features 也不能反推
  v1 实现或结果。
- **Access / Full-read Coverage**：已读 metadata、Abstract、Introduction、Background/Related Work、
  architecture、Algorithm 1、三 stream/event protocol、memory/stateless execution、全部 evaluation、
  Conclusion、Appendix A 的 host/GPU/dispatch 实现与 Appendix B 的 Ratel reproduction，并核对作者发布页、
  current README、feature/release drift。论文没有独立 Limitations/Threats section。
- **Original Problem / Previous Design**：标准 DP 复制 parameters、gradients 与 optimizer states；ZeRO/FSDP
  通过分片降低每卡驻留，offload 再把部分 state/compute 放到 CPU/NVMe。这些设计合理，因为 GPU-resident
  autograd、module lifecycle、collective ownership 与 checkpoint tooling 已成熟，也能在模型可容纳或多卡
  可用时保留高 reuse 和通用性。问题是在“只有一张 GPU、但 host RAM 很大”的 post-training 场景，通用
  offload 会因 fragmented tensors、重复 staging、细粒度 transfers 与 graph-managed lifetime 让容量和 PCIe
  critical path 同时恶化。
- **Changed Constraint / Principle**：当总 parameter state 远大于 HBM、单层 working set 仍可容纳，而且每步
  H2D bytes 基本只随模型大小变化时，可以用更大 token batch 增加 layer compute，尝试满足
  `P_i / B_link <= C_(i-1)` 的局部 overlap 条件。由此 CPU 不再是被动 spill tier，而成为 persistent-state
  owner；GPU 则从 model owner 变成逐层 transient execution cache。这是 capacity 与 locality 的重排，
  不是让 PCIe 变得与 HBM 一样快。
- **Mechanism**：BF16 weights、BF16 gradients 与 FP32 Adam moments 按 layer 打成 4KB-aligned contiguous
  host blocks，authoritative persistent footprint 约为 12 bytes/parameter。Forward 逐层 `StreamIn→Bind→
  Compute→Release`，每 K 层留 activation anchor；Backward 从 anchor 重算一个 block，再逆序逐层载入权重、
  local backward 并立即 D2H gradient。CPU 执行 Adam。compute、H2D weight 与 D2H gradient 三条 CUDA stream
  通过 double buffer 和 `Weights-Ready / Backward-Done / Buffer-Free` events 协调；K=12 gradient slab pool
  吸收短期 backpressure。stateless layer template 用 flat-buffer views 动态绑定参数，不保留 global autograd/
  CUDA graph。
- **State Ownership / Control and Data Flow**：CPU master store 拥有 parameter、accumulated gradient、optimizer
  moments 与 update epoch；pinned staging pool 和 GPU weight buffers 只拥有带 layer/step identity 的临时副本；
  activation stack/checkpoint anchors 拥有一个 backward block 的重算状态；event protocol 决定 buffer 何时可复用。
  因此 checkpoint 必须以 CPU master step、optimizer completion、gradient drain 与 data/RNG cursor 为同一 commit
  boundary。论文未给出 CPU update 与下一 step prefetch 的原子切换、crash recovery、partial-gradient handling、
  ECC/transfer corruption、NUMA failure 或 checkpoint/resume contract。
- **Implementation Details**：关键路径由 Python runtime 加 C++/CUDA extensions 构成；CPU pageable master
  store 只通过两块最大层尺寸的 pinned staging buffer 做大 burst DMA，避免 pin 全模型；single-kernel batched
  pointer binding 取代数百次 `copy_`；background CPU thread 用 OpenMP 做 gradient accumulation/Adam；workspace
  预分配、stack lifecycle、`record_stream` 与 expandable segments 控制 in-flight lifetime 和 fragmentation。
  这同时说明所谓 “stateless GPU” 仍有显式 transient state，不能误写成无状态训练。
- **Evaluation Contract**：主系统为单 GH200 superchip（Grace 72-core、96GB HBM3、480GB local host memory、
  NVLink-C2C）与单 H200 SXM（Xeon Platinum 8558、141GB HBM3e、1.5TB host memory、paper 写 PCIe Gen4）；
  模型含 Qwen2.5 7/14/32/72B 与 GPT-OSS-120B MoE。MetaMathQA 395k 随机 70/30、exact match 只在 7B/14B
  做 correctness comparison。扩展实验覆盖 A100 PCIe 80GB/600GB host、RTX A6000 48GB 和 RTX 3090 24GB，
  后两者固定 sequence 8192、checkpoint interval 4；long-context 只在 GH200 7B、batch 随 1K～512K 改变，
  512K 还启用 chunked MLP。没有 production SLO、能耗、总 wall-clock、成本、多 seed 或统计区间。
- **Baselines / Ablations / Sensitivity / Overhead**：比较 PyTorch Native、ZeRO-3 Offload、ZeRO-Infinity、
  FSDP Offload、ColossalAI-Gemini，并另复现 Ratel。double buffering ablation 从 266.3 降至 182.91 TFLOPS；
  gradient slab pool removal 降至 257.55，支持 overlap 是主要性能来源。但 checkpoint interval=1 的表格是
  BS64/240.45 TFLOPS，正文却写 BS32/184.2；long-context 表格 1K 是 284.7 TFLOPS，正文写 264.8，故不能
  采用这些冲突数字作精确结论。Baseline accuracy 33.47/37.58 的身份也未解释清楚；它不能参与“数值等价”
  比较。A100 baseline 虽称按官方建议调优，完整 configs、software versions 与 matched host-memory usage 未披露。
- **What the Evidence Proves / Does Not Prove**：作者结果支持：在披露 hardware/model/batch contract 下，
  CPU-owned flat state、layer streaming、overlap 与 aggressive recomputation 可以把单卡训练的容量边界移到
  host RAM，并在多类单 GPU 上保持可运行；double-buffer ablation 支持 transfer placement 的因果作用。它不
  证明所有 100B+ workloads 都高效，不证明 1.84× 可跨模型/互联复现，不证明 512K 在 matched tokens、quality、
  wall-clock 或 attention backend 下优于 CP/FSDP，也不证明 loss/optimizer trajectory 与标准训练普遍等价。
- **Limitations / Threats to Validity**：除内部数字冲突外，论文把“near-exponential baseline host growth”主要
  归因于实现行为，却没有公开完整 profiler/config；accuracy 只有 MetaMathQA 随机 split，可能与基础数据及
  answer format 相关；没有 optimizer-state/resume equivalence、long-run convergence、MoE expert imbalance、
  Muon、activation offload、multi-GPU、failure injection、NUMA/PCIe contention 或 concurrent workload 证据。
  当前 repository 后来加入 model families、VERL 和 multi-GPU，不能当成 paper artifact 的可复现快照。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：获得的是容量与 deterministic per-layer GPU
  footprint；付出额外 forward recompute、每步重复权重传输、CPU RAM/optimizer bandwidth、较大 batch/latency、
  手写 layer templates、较弱 CUDA-graph compatibility 与复杂 event/buffer correctness。窄层/小 batch/慢 PCIe
  会让 transfer 暴露；超宽层重新推高单层 HBM，CPU/slab backpressure 会形成新瓶颈。模型能常驻 HBM 时 native
  runtime 仍更简单；多卡和高速 collective 可用时 ZeRO/FSDP/TP/PP 保留吞吐、生态与 fault-recovery 优势；
  SSD/tiered storage 只有在更低层延迟也能被调度隐藏时才是下一分支。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：`Direct Evolution`：GPU-owned full state → ZeRO
  shard/CPU offload → CPU-owned authoritative layer store + transient GPU cache；与 activation checkpointing、
  PCIe/NVLink-C2C overlap 和 explicit buffer lifecycle 是 `Layering / Dependency`，与 Pipeline Parallel 的
  fill/overlap 只是 `Principle Reuse`，不是跨设备 stage pipeline。已读 Ch31～36；主 owner 是 Ch35，因为它
  改变 offload 与 model-state ownership，Ch32 承接 link/overlap contract，Ch34 只做 pipeline analogy，Ch31
  承接 checkpoint atomicity，Ch36 保留未来 multi-GPU composition。
- **Existing Coverage / Integration Decision**：Ch35 已写“cold state 移到更大层级、prefetch/CPU optimizer/
  link bandwidth 决定是否有效”，所以不是全新原则；缺口是 CPU 可从 spill tier 进一步升级为 authoritative
  owner，以及它如何把 autograd、buffer、event 和 checkpoint lifetime 变成显式 runtime contract。暂定
  `Refine — Existing Argument (Experimental; Provisional; Historical Books Gate Closed)`；Gate 通过后只
  refine Ch35 的 offload evolution，并在 Ch31/32 做短 handoff，不写 headline benchmark 或 later feature list。
- **Open Questions**：怎样在 CPU update、next-step prefetch 与 checkpoint 间实现可恢复的 model-version commit？
  slab backpressure、NUMA placement、PCIe contention 与 CPU optimizer 怎样进入 SLO/profile？在相同 tokens、
  precision、optimizer、attention backend 和 wall-clock 下，512K 与 CP/FSDP 的真实 trade-off 是什么？Muon、MoE、
  multi-GPU 与 SSD tier 会怎样改变 authoritative state 和 failure domain？

## Repository Changes

- W14 score ledger 从 2 行扩展到 27 行，增加 25 个恢复候选与显式日期/跨周归属边界、Amazon TTS、HISA、
  Medical AI Scientist、Kernel-Smith、Marco DeepResearch、GEMS、Terminal Agents、MiroEval、AgentHazard、LightThinker++、
  SKILL0、GrandCode、Self-Distilled RLVR、Combee、MemRerank、ASI-Evolve、Simple Self-Distillation 与
  Stochastic KV Routing、Omni-SimpleMem、S0 Tuning、Meta-TTL 与 MegaTrain 完整 Source Review；S0 因 paper/model-card 的
  layer layout、hardware 与 base identity 冲突从 24 调整为 23；HippoCamp 已完成 official arXiv primary text、
  Method、Evaluation、Appendix 与 artifact 的完整审计，解除 blocker，最终为 `No Change — Already Covered /
  Experimental Evaluation Case`；Meta-TTL 因 v1 缺少 uncertainty/
  cost contract 且 current artifact drift 从 24 调整为 23；无 pending candidate；
  Stochastic KV Routing 按 arXiv v1 日期从后续 curation feed 回拨；MegaTrain 按作者 4 月 5 日正式发布页
  从 W15 回拨；SkVM 按 arXiv v1 的 4 月 3 日从 W15 attribution ledger 回拨并完成 compiler/runtime 全文
  审计，后续 v2/v3 与 current repository 仅用于 revision/artifact boundary；无历史 Daily 或 Books 修改。
- 跨周 attribution 对账新增 GLM-5V-Turbo 04-02 的 18/30 product node，fixed-source 回放再新增 Amazon
  TTS 24/30 official engineering node，SkVM 再使账本成为 27 scored rows；其
  04-29 technical report 仍由 W18 拥有。另将 `Backdoor Attacks on Decentralised Post-Training` 与 `Cactus`
  明确登记为 2 个 unscored blocked identities。current-review pending 仍为 0，W14 Discovery Gate 因 fixed
  academic cross-index 与剩余 Infra 历史 release 覆盖未闭合继续 Open；Books Gate 未打开。
- 2026-08-13 周级账目复核再次得到 27 scored（14 high / 12 mid / 1 low）、26/26 `20+` Full Source
  Reviews、1/1 low-score boundary、2 unscored blockers、0 ordinary pending；两个 attribution-only blocker
  未被评分、分配 owner 或写成已读。W14 Candidate Gate Passed，backlog cursor 继续 W15；未修改 Books。

## Open Questions

1. Agent trajectory evaluation 的 rater disagreement 应如何与 deterministic checks 合并？
2. 2026-04-04～05 以及 arXiv category、OpenAlex、DBLP、Scholar、OpenReview/TMLR 与剩余 Infra
   历史 release sources 还会恢复哪些旧版未记录候选？
3. Google Research baseline 的 direct paper、revision history 与 appendix URL 应如何从 archive
   landing page 补齐，避免 archive page 单点引用？
4. HippoCamp 的三种 runtime regime 如何在 matched permissions、parallelism、tokens/calls、wall-clock 与
   repeated-run uncertainty 下复测；Atomic Unit scorer 又如何在不泄漏 raw personal media 时开放审计？
5. SKILL0 的 helpfulness estimator 如何加入 sampling uncertainty 与 Skill interaction，而不把
   validation noise 固化为 curriculum 顺序？
6. Agentic-GRPO 在 matched compute 与相同 staleness policy 下是否优于 terminal GRPO；被丢弃的
   delayed corrections 会造成什么 selection bias？
7. RLSD 的 teacher-conditioned magnitude 是否会造成可测的 reference leakage？如何用 matched
   H200-hours、reference corruption 和 process-level causal labels 验证其 credit 解释？
8. Medical AI Scientist 何时公开 benchmark manifest、container、prompts、完整 runs 与 generated
   manuscripts？没有这些 artifact 时，怎样独立复核“executable”到“scientifically valid”的鸿沟？
9. GEMS 如何把自然语言 criteria、verdict、raw image、derived experience 与 Skill version 变成可追溯、
   可恢复、可删除的 state contract；同源 MLLM verifier 的 calibration 和 matched-compute 增益如何验证？
10. Terminal Agents 的 artifact 公开后，generic API、narrow typed tools、terminal/filesystem 与 browser
    如何在 matched permissions、coverage、repeats 和 failure-severity contract 下重新比较？
11. MemRerank 在独立 reward/evaluator、真实 query、更多 domain 与完整 privacy/delete contract 下，
    是否仍能证明 task-optimized derived preference view 优于 query-time selected evidence？
12. ASI-Evolve 的三项高成本主任务在 matched compute、多 seeds、独立 held-out evaluator 与可重放 artifact
    下，Cognition、Analyzer 与 sampling policy 各自贡献多少，search-level overfitting 如何测量？
13. Simple Self-Distillation 在独立 tuning/test split、多 seed、event-aligned training artifact 和 matched
    verified-SFT / teacher / RLVR compute 下是否仍成立；多轮迭代何时放大错误 mode 或发生 collapse？
14. S0 Tuning 的 exact base revision、24+8 与 21+6 layer layout、A10G 与 A100 training hardware 以及公开
    state artifact 如何对齐；在 matched LoRA 和 end-to-end serving contract 下，zero per-token adapter compute
    是否仍转化为可测收益？
15. Meta-TTL 在 independent held-out family、nested validation、repeated runs 与 matched call/token/wall-clock
    contract 下是否仍优于 hand-crafted reflection；不可 reset 或有真实副作用的环境如何定义 adaptation gate？
16. MegaTrain 怎样把 CPU optimizer completion、gradient drain、next-step prefetch 与 checkpoint commit 绑定成
    原子 model-version transition；在 matched token/precision/optimizer/backend 下，其 long-context 与多卡分支
    相比 CP/FSDP 的 wall-clock、能耗、恢复与 tail behavior 如何？
17. `Backdoor Attacks on Decentralised Post-Training` 与 `Cactus` 的可核验 primary identifier、作者、abstract、
    revision 和 artifact 是什么？在取得这些证据前，两者保持 unscored/unowned。
18. GLM-5V-Turbo 04-02 product node 是否存在 event-time immutable model/system card 或 release snapshot？若无，
    怎样防止 later technical report 的机制与 current repository 状态被错误倒写到产品首发日？
19. Amazon TTS 的 phoneme/duration plan 如何在 streaming 下与 audio chunk commit、retry budget、fallback、
    tail SLO 和独立 verifier calibration 绑定；没有 model/artifact contract 时，哪些机制能被第三方复现？
20. SkVM 的 target capability profile 怎样绑定 model/harness/tool/sandbox revision；compiler/JIT proposal 如何
    执行 held-out validation、signature、canary、in-flight pinning、revoke 与 rollback？

## Sources

- Amazon Science, "Improving quality and robustness in LLM-based text-to-speech systems",
  published 2026-04-01, accessed 2026-08-12:
  https://www.amazon.science/blog/improving-quality-and-robustness-in-llm-based-text-to-speech-systems
- Microsoft Research, "ADeLe: Predicting and explaining AI performance across tasks",
  publication/communication node 2026-04-01, accessed 2026-08-12:
  https://www.microsoft.com/en-us/research/blog/adele-predicting-and-explaining-ai-performance-across-tasks/
- Nature, "General scales unlock AI evaluation with explanatory and predictive power",
  formal publication 2026-04-01; source family first-public preprint belongs to 2025:
  https://www.nature.com/articles/s41586-026-10303-2
- ADeLe primary preprint metadata, first-public 2025-03-10: https://arxiv.org/abs/2503.06378
- Microsoft Research, "Energy Use of AI Inference: Efficiency Pathways and Test-Time Compute",
  source-family first-public 2025-09, accessed 2026-08-12:
  https://www.microsoft.com/en-us/research/publication/energy-use-of-ai-inference-efficiency-pathways-and-test-time-compute/
- Energy Use of AI Inference primary preprint metadata, first-public 2025-09-24:
  https://arxiv.org/abs/2509.20241
- Microsoft Research, "On the Use of LLMs for Relevance Labelling", April 2026 formal-publication
  node; related primary papers were public before W14:
  https://www.microsoft.com/en-us/research/publication/on-the-use-of-llms-for-relevance-labelling/
- OpenAI Research index, accessed 2026-08-12: https://openai.com/research/index/
- Anthropic Research index, accessed 2026-08-12: https://www.anthropic.com/research
- Apple Machine Learning Research index, accessed 2026-08-12: https://machinelearning.apple.com/
- Microsoft Research Blog, accessed 2026-08-12: https://www.microsoft.com/en-us/research/blog/
- Amazon Science Blog, accessed 2026-08-12: https://www.amazon.science/blog/
- Ai2 Blog, accessed 2026-08-12: https://allenai.org/blog
- Cohere Labs Research, accessed 2026-08-12: https://cohere.com/research
- Mistral News, accessed 2026-08-12: https://mistral.ai/news/
- Moonshot AI Blog, accessed 2026-08-12: https://platform.kimi.com/blog
- vLLM releases, accessed 2026-08-12: https://github.com/vllm-project/vllm/releases
- SGLang releases, accessed 2026-08-12: https://github.com/sgl-project/sglang/releases
- NVIDIA Dynamo releases, accessed 2026-08-12: https://github.com/NVIDIA/Dynamo/releases
- TensorRT-LLM releases, accessed 2026-08-12: https://github.com/NVIDIA/TensorRT-LLM/releases
- KServe releases, accessed 2026-08-12: https://github.com/kserve/kserve/releases
- Ray releases, accessed 2026-08-12: https://github.com/ray-project/ray/releases
- Megatron Core releases, accessed 2026-08-12: https://github.com/NVIDIA/Megatron-LM/releases
- Historical pagination/API gaps in the release pages above are recorded in Coverage Limitations rather than
  treated as a negative proof.
- Google Research March 2026 archive: https://research.google/blog/2026/03/
- Google Research April 2026 archive: https://research.google/blog/2026/04/
- GLM-V official repository; GLM-5V-Turbo product node dated 2026-04-02, accessed 2026-08-12:
  https://github.com/zai-org/GLM-V
- GLM-5V-Turbo technical report, first-public 2026-04-29; W18 mechanism node, accessed 2026-08-12:
  https://arxiv.org/abs/2604.26752
- Hugging Face Daily Papers, 2026-03-30: https://huggingface.co/papers/date/2026-03-30
- Hugging Face Daily Papers, 2026-03-31: https://huggingface.co/papers/date/2026-03-31
- Hugging Face Daily Papers, 2026-04-01: https://huggingface.co/papers/date/2026-04-01
- Hugging Face Daily Papers, 2026-04-02: https://huggingface.co/papers/date/2026-04-02
- Hugging Face Daily Papers, 2026-04-03: https://huggingface.co/papers/date/2026-04-03
- MegaTrain author release, published 2026-04-05:
  https://mastergodzilla.github.io/posts/2026/04/megatrain/
- MegaTrain arXiv abstract and revision history: https://arxiv.org/abs/2604.05091
- MegaTrain v1 HTML: https://arxiv.org/html/2604.05091v1
- MegaTrain author repository: https://github.com/DLYuanGod/MegaTrain
- HISA arXiv abstract and revision history: https://arxiv.org/abs/2603.28458
- HISA v1 HTML: https://arxiv.org/html/2603.28458v1
- HISA v3 HTML: https://arxiv.org/html/2603.28458v3
- HISA author artifact: https://github.com/MuLabPKU/TransArch
- Towards a Medical AI Scientist: https://arxiv.org/abs/2603.28589
- Towards a Medical AI Scientist v1 HTML: https://arxiv.org/html/2603.28589v1
- Medical AI Scientist official project page: https://cuhk-aim-group.github.io/Med-AI-Scientist-Homepage/
- Kernel-Smith abstract and revision history: https://arxiv.org/abs/2603.28342
- Kernel-Smith v1 HTML: https://arxiv.org/html/2603.28342v1
- Kernel-Smith author repository: https://github.com/InternLM/Kernel-Smith
- Kernel-Smith SGLang merged PR #20778: https://github.com/sgl-project/sglang/pull/20778
- Kernel-Smith LMDeploy merged PR #4345: https://github.com/InternLM/lmdeploy/pull/4345
- Marco DeepResearch abstract and revision history: https://arxiv.org/abs/2603.28376
- Marco DeepResearch v1 HTML: https://arxiv.org/html/2603.28376v1
- Marco DeepResearch author inference repository:
  https://github.com/ATH-MaaS/Marco-DeepResearch/tree/main/Marco-DeepResearch-Family/Marco-Agent-DeepResearch
- MiroEval abstract and revision history: https://arxiv.org/abs/2603.28407
- MiroEval v1 HTML: https://arxiv.org/html/2603.28407v1
- MiroEval author benchmark/evaluator repository: https://github.com/MiroMindAI/MiroEval
- MiroEval repository releases: https://github.com/MiroMindAI/MiroEval/releases
- AgentHazard abstract and revision history: https://arxiv.org/abs/2604.02947
- AgentHazard v1 HTML: https://arxiv.org/html/2604.02947v1
- AgentHazard project and artifact entry: https://yunhao-feng.github.io/AgentHazard/
- AgentHazard author repository: https://github.com/Yunhao-Feng/AgentHazard
- AgentHazard repository releases: https://github.com/Yunhao-Feng/AgentHazard/releases
- LightThinker++ abstract and revision history: https://arxiv.org/abs/2604.03679
- LightThinker++ v1 HTML: https://arxiv.org/html/2604.03679v1
- LightThinker author repository: https://github.com/zjunlp/LightThinker
- LightThinker general-reasoning implementation guide:
  https://github.com/zjunlp/LightThinker/blob/main/general_reasoning/README.md
- LightThinker agentic-reasoning implementation guide:
  https://github.com/zjunlp/LightThinker/blob/main/agentic_reasoning/README.md
- LightThinker repository releases (none at review time): https://github.com/zjunlp/LightThinker/releases
- Combee abstract and revision history: https://arxiv.org/abs/2604.04247
- Combee v1 HTML: https://arxiv.org/html/2604.04247v1
- ACE author repository: https://github.com/ace-agent/ace
- GEPA author repository and revision follow-up: https://github.com/gepa-ai/gepa
- Marco DeepResearch: https://arxiv.org/abs/2603.28376
- GEMS abstract and revision history: https://arxiv.org/abs/2603.28088
- GEMS v1 HTML: https://arxiv.org/html/2603.28088v1
- GEMS official project page: https://gems-gen.github.io/
- GEMS author repository: https://github.com/lcqysl/GEMS
- GEMS core Agent implementation: https://github.com/lcqysl/GEMS/blob/main/agent/GEMS.py
- MiroEval: https://arxiv.org/abs/2603.28407
- Terminal Agents abstract and revision history: https://arxiv.org/abs/2604.00073
- Terminal Agents v1 HTML: https://arxiv.org/html/2604.00073v1
- Terminal Agents v2 HTML: https://arxiv.org/html/2604.00073v2
- Terminal Agents v3 HTML (revision boundary and later controls): https://arxiv.org/html/2604.00073v3
- MemRerank abstract and revision history: https://arxiv.org/abs/2603.29247
- MemRerank v1 HTML: https://arxiv.org/html/2603.29247v1
- MemRerank v3 HTML (substantive revision boundary): https://arxiv.org/html/2603.29247v3
- MemRerank author dataset card: https://huggingface.co/datasets/zhiyuanpeng/amazon-c4-user-purchase-history
- ASI-Evolve abstract and revision history: https://arxiv.org/abs/2603.29640
- ASI-Evolve v1 HTML: https://arxiv.org/html/2603.29640v1
- ASI-Evolve author repository: https://github.com/GAIR-NLP/ASI-Evolve
- ASI-Evolve repository releases (none at review time): https://github.com/GAIR-NLP/ASI-Evolve/releases
- ASI-Evolve current experiment coverage: https://github.com/GAIR-NLP/ASI-Evolve/tree/main/experiments
- ASI-Evolve current database implementation: https://github.com/GAIR-NLP/ASI-Evolve/blob/main/database/database.py
- ASI-Evolve current cognition implementation: https://github.com/GAIR-NLP/ASI-Evolve/blob/main/cognition/cognition.py
- ASI-Evolve current pipeline implementation: https://github.com/GAIR-NLP/ASI-Evolve/blob/main/pipeline/main.py
- Embarrassingly Simple Self-Distillation Improves Code Generation: https://arxiv.org/abs/2604.01193
- Simple Self-Distillation v1 HTML: https://arxiv.org/html/2604.01193v1
- Simple Self-Distillation v2 PDF (revision boundary): https://arxiv.org/pdf/2604.01193v2
- Apple Research page: https://machinelearning.apple.com/research/simple-self-distillation
- Simple Self-Distillation author repository: https://github.com/apple/ml-ssd
- Simple Self-Distillation repository history: https://github.com/apple/ml-ssd/commits/main/
- Simple Self-Distillation repository releases (none at review time): https://github.com/apple/ml-ssd/releases
- Simple Self-Distillation data-generation config:
  https://github.com/apple/ml-ssd/blob/main/data_generation/config.yaml
- Simple Self-Distillation data-generation implementation:
  https://github.com/apple/ml-ssd/blob/main/data_generation/generate.py
- Simple Self-Distillation LiveCodeBench evaluator:
  https://github.com/apple/ml-ssd/blob/main/evaluation/benchmark.py
- SimpleSD-4B-Instruct model card: https://huggingface.co/apple/SimpleSD-4B-instruct
- SimpleSD-4B-Thinking model card: https://huggingface.co/apple/SimpleSD-4B-thinking
- SimpleSD-30B-A3B-Instruct model card: https://huggingface.co/apple/SimpleSD-30b-a3b-instruct
- HippoCamp: https://arxiv.org/abs/2604.01221
- HippoCamp official project page: https://hippocamp-ai.github.io/
- HippoCamp author repository: https://github.com/synvo-ai/HippoCamp
- HippoCamp repository history: https://github.com/synvo-ai/HippoCamp/commits/main/
- HippoCamp repository releases (none at review time): https://github.com/synvo-ai/HippoCamp/releases
- HippoCamp official dataset and schema: https://huggingface.co/datasets/MMMem-org/HippoCamp
- SKILL0 abstract and revision history: https://arxiv.org/abs/2604.02268
- SKILL0 v1 HTML: https://arxiv.org/html/2604.02268v1
- SKILL0 v2 HTML (revision boundary): https://arxiv.org/html/2604.02268v2
- SKILL0 author repository: https://github.com/ZJU-REAL/SkillZero
- SKILL0 ALFWorld 3B training recipe:
  https://github.com/ZJU-REAL/SkillZero/blob/main/scripts/train_alfworld_skillzero_3b.sh
- SKILL0 Search-QA 3B training recipe:
  https://github.com/ZJU-REAL/SkillZero/blob/main/scripts/train_search_skillzero_3b.sh
- Omni-SimpleMem: https://arxiv.org/abs/2604.01007
- Omni-SimpleMem v1 HTML: https://arxiv.org/html/2604.01007v1
- Omni-SimpleMem v2 HTML (naming/code-link revision): https://arxiv.org/html/2604.01007v2
- SimpleMem/Omni-SimpleMem author repository: https://github.com/aiming-lab/SimpleMem/tree/main/OmniSimpleMem
- SimpleMem v0.2.0 release: https://github.com/aiming-lab/SimpleMem/releases/tag/v0.2.0
- S0 Tuning: https://arxiv.org/abs/2604.01168
- S0 Tuning v1 HTML: https://arxiv.org/html/2604.01168v1
- S0 Tuning v2 HTML (revision boundary): https://arxiv.org/html/2604.01168v2
- S0 Tuning author repository: https://github.com/JackYoung27/s0-tuning
- S0 Tuning experiment documentation: https://github.com/JackYoung27/s0-tuning/tree/main/experiments
- S0 Tuning package releases: https://pypi.org/project/s0-tuning/#history
- S0 Tuning Qwen trained-state model card: https://huggingface.co/JackYoung27/s0-tuning-qwen3.5-4b-humaneval
- S0 Tuning verified-solution dataset card: https://huggingface.co/datasets/JackYoung27/humaneval-s0-train
- Learning to Learn-at-Test-Time: https://arxiv.org/abs/2604.00830
- Meta-TTL v1 HTML: https://arxiv.org/html/2604.00830v1
- Meta-TTL v2 HTML (same-week revision boundary): https://arxiv.org/html/2604.00830v2
- Meta-TTL v3 HTML (later controls; not W14 event evidence): https://arxiv.org/html/2604.00830v3
- Meta-TTL author repository: https://github.com/zzzlou/meta-ttl
- Meta-TTL repository releases (none at review time): https://github.com/zzzlou/meta-ttl/releases
- Meta-TTL Jericho outer-loop entrypoint:
  https://github.com/zzzlou/meta-ttl/blob/main/jericho_meta_training/train_meta_agent.py
- Meta-TTL WebArena outer-loop entrypoint:
  https://github.com/zzzlou/meta-ttl/blob/main/webarena_meta_training/train_meta_agent.py
- GrandCode abstract and revision history: https://arxiv.org/abs/2604.02721
- GrandCode v1 HTML: https://arxiv.org/html/2604.02721v1
- GrandCode v2 HTML (revision boundary): https://arxiv.org/html/2604.02721v2
- GrandCode v3 HTML (revision boundary): https://arxiv.org/html/2604.02721v3
- GrandCode official project page: https://ornith.ai/cp.html
- GrandCode report repository: https://github.com/ornith-ai/grandcode
- GrandCode contest submission artifact: https://github.com/deepreinforce-ai/codeforces
- Self-Distilled RLVR: https://arxiv.org/abs/2604.03128
- Self-Distilled RLVR v1 HTML: https://arxiv.org/html/2604.03128v1
- Self-Distilled RLVR v2 HTML (revision boundary): https://arxiv.org/html/2604.03128v2
- Self-Distilled RLVR author implementation: https://github.com/iie-ycx/RLSD
- AgentHazard: https://arxiv.org/abs/2604.02947
- Combee: https://arxiv.org/abs/2604.04247
- Stochastic KV Routing: https://arxiv.org/abs/2604.22782
- Stochastic KV Routing v1 HTML: https://arxiv.org/html/2604.22782v1
- Stochastic KV Routing v1 PDF: https://arxiv.org/pdf/2604.22782
- Apple Machine Learning Research publications: https://machinelearning.apple.com/research/
- SkVM abstract and revision history: https://arxiv.org/abs/2604.03088
- SkVM v1 HTML: https://arxiv.org/html/2604.03088v1
- SkVM author repository: https://github.com/SJTU-IPADS/SkVM
- SkVM architecture documentation: https://github.com/SJTU-IPADS/SkVM/blob/main/docs/architecture.md

## 2026-08-14 Final Books Integration Ledger — 27/27

本轮按新 84 章结构重新读取主 owner 与相邻章节。旧编号 Ch38/39/45/62/68/73/76/80 不再直接作为
当前 owner；所有写入都使用 Stable Node，并保留 legacy mapping。`No Change` 引用现有论证，版本事实与
blocked identity 不进入机制正文。

| Candidate / Source Family | Score | Stable Owner | Current / Legacy | Final Disposition | Chapter-level Review Evidence |
| --- | ---: | --- | --- | --- | --- |
| How many raters are enough? | 24 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument | 将 item/rater/repeat 方差、estimand 与 decision loss 连接为动态预算，而非通用人数阈值 |
| Behavioral-disposition alignment | 21 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument | 分离 self-report、behavior probe 与 deployment outcome，不推断内部人格或因果机制 |
| LLM-based TTS quality and robustness | 24 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Integrate — New Mechanism / Official Engineering Evidence | 新增 plan→generate→validate→bounded retry/fallback；artifact 与 SLO 未公开 |
| Towards a Medical AI Scientist | 24 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — Already Covered | claim provenance、executable artifact、approval、workflow state 与 correlated-role boundary 已覆盖 |
| HISA | 27 | `INFER-PREFILL` | Ch43 / Ch39 | Refine — Existing Argument / Experimental | 新增 block shortlist→token refinement，并显式计入 selection error、index identity 与 TTFT |
| Kernel-Smith | 28 | `INFER-TENSORRT-LLM` | Ch49 / Ch45 | Refine — Existing Argument / Experimental | 在 learned proposal lifecycle 中加入 population/archive、lineage、diversity 与 benchmark admission |
| Marco DeepResearch | 25 | `AGENT-REFLECTION` | Ch80 / Ch76 | Refine — Existing Argument / Experimental | 把 reflection 对象改为 evidence gap，并区分局部 repair、discard-all 与 stop |
| GEMS | 23 | `AGENT-REFLECTION` | Ch80 / Ch76 | No Change — Already Covered | criterion diagnosis、raw/derived memory、Skill admission 与 workflow authority 已有具体论证 |
| MiroEval | 25 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | 分离 report、claim/provenance、process 与 environment/tool 四个 evidence planes |
| Terminal Agents | 24 | `AGENT-TOOL-CALLING` | Ch78 / Ch74 | Refine — Existing Argument / Experimental | 补 narrow tool→generic API→terminal→browser 的 interface-granularity 共存路线 |
| MemRerank | 22 | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — Existing Argument / Experimental | 把 preference profile 定义为 task-optimized materialized view，并补 stale/leakage/delete 边界 |
| ASI-Evolve | 24 | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — Existing Argument / Experimental | 分离 cold-start prior 与 run-derived lesson，绑定 candidate lineage 与 evaluator evidence |
| Simple Self-Distillation | 26 | `TRAIN-SFT` | Ch29 / Ch25 | Integrate — New Mechanism / Experimental | 将 temperature/truncation-shifted self-target 与 serving sampling policy 分离 |
| HippoCamp | 23 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — Already Covered / Experimental Case | raw snapshot、hidden evidence、retrieval、privacy 与 capability/effect planes 已覆盖 |
| SKILL0 | 25 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | Skill 作为可筛选、可排序、可退火 scaffold；不宣称可验证内化 |
| Omni-SimpleMem | 24 | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — Existing Argument / Experimental | 新增 multimodal raw/MAU/index tier 与 destructive novelty-filter failure |
| S0 Tuning | 23 | `TRAIN-LORA` | Ch30 / Ch26 | Integrate — New Mechanism / Experimental / Artifact Identity Inconsistent | 新增 recurrent launch state 适配面及 base/layout/reset/routing lifecycle |
| Meta-TTL | 23 | `AGENT-REFLECTION` | Ch80 / Ch76 | Refine — Existing Argument / Experimental | 固定 reflection rule 演进为 reset-bound learned adaptation policy，保留 immutable safety boundary |
| GrandCode | 26 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | 把 immediate reward、delayed correction、behavior-policy identity 与 staleness 串成 lifecycle |
| Self-Distilled RLVR | 25 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | verifier 决定 update direction，privileged teacher 仅调正幅度；不声称 zero effect |
| AgentHazard | 26 | `PLATFORM-SECURITY` | Ch72 / Ch68 | Refine — Existing Argument / Experimental | 增加 cumulative effect state 与 trajectory-level harm verifier，保留 prompt/action guards |
| LightThinker++ | 25 | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — Existing Argument / Experimental | 从 irreversible summary 演进为 raw/summary 双态、选择性展开与 repair |
| Combee | 28 | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — Existing Argument / Experimental | 新增 shared context version、bounded fan-in、curator-owned commit 与 stale contribution |
| Stochastic KV Routing | 26 | `MODEL-KV-CACHE` | Ch19 / Ch19 | Integrate — New Mechanism / Experimental | 将 depth-wise KV sharing 定义为训练/checkpoint contract，不是 runtime eviction |
| MegaTrain | 27 | `TRAIN-ZERO` | Ch39 / Ch35 | Refine — Existing Argument / Experimental | 扩展到 CPU-authoritative persistent state 与 per-layer transient GPU execution cache |
| SkVM | 29 | `AGENT-PLATFORM` | Ch84 / Ch80 | Integrate — New Mechanism / Experimental | 新增 target profile→AOT/JIT Skill variant→held-out admission→runtime fallback lifecycle |
| GLM-5V-Turbo product node | 18 | W18 Source Family | N/A | Weekly Only — Version/Product Fact | 04-02 只证明 availability；04-29 technical-report mechanism 由 W18 owner，禁止反推 |

### W14 Gate Result

- Scored candidates: `27/27` final disposition。
- Scored `20+`: `26/26`；`5 Integrate + 18 Refine + 3 No Change`。
- Low-score boundary: `1/1 Weekly Only`。
- Unscored identity backlog: Backdoor Attacks、Cactus，`2 Unverified / Blocked / No Books Change`。
- Owner chapters changed: 15 Stable Nodes；没有新增 Part、章节或孤立论文笔记。
- Source-Family Books Gate: `Complete`；Archive Completion Gate: `Open`。

Repository changes: Ch19、Ch24、Ch29～30、Ch33、Ch39、Ch43、Ch49、Ch66、Ch72、Ch77～78、Ch80～81、
Ch84。Medical AI Scientist、GEMS、HippoCamp、GLM 产品节点与两个 blocked identities 没有进入新机制正文。
