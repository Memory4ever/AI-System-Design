# AI Research Weekly — 2026-W13

> Coverage Window: 2026-03-23～2026-03-29
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: Discovery Recall Repaired; 45/45 scored candidates have final Books dispositions; 41/41 scored `20+` Full Source Reviews complete; 1 unscored ClawKeeper source remains `Unverified / Blocked / No Books Change`; W13 Source-Family Books Gate Complete; Archive Completion Gate Open

> **Supersession boundary (2026-08-14):** 本文较早段落中的 `Books pending`、`provisional` 与
> `Historical Books Gate Closed` 是 Source Review 阶段快照；它们不被删除，但全部由文末 45/45
> Final Books Integration Ledger 取代。Archive Gate 仍因 blocked source 与 discovery limitation 保持 Open。

## Executive Summary

旧版只保留 TurboQuant、Anthropic Economic Index 与 Meta 两项垂直模型发布，未达到接近 Live
Daily 的 discovery recall。重开 2026-03-23～03-29 的 arXiv v1 first-public window 后，首个全文
批次恢复 mSFT、RLVR update direction、Scaling DoRA 与 CAID。它们分别暴露四类长期系统问题：
dataset mixture 的任务级学习动态不同；RLVR 的因果变化不能只用 update magnitude 描述；adapter
公式若直接 materialize dense intermediate 会把 high rank 变成 memory/runtime 问题；Multi-Agent 的
收益取决于 dependency、workspace isolation、merge protocol 与 coordinator capacity。第二批进一步
完成 SpecEyes、workflow optimization survey 与 Sparse but Critical：分别把 speculation 从 token
verification 推到 tool-loop routing、分离 reusable template / realized graph / execution trace，并用
cross-sampling intervention 约束“RLVR 只改少量 token”的因果解释。

第三批完成 depth-recurrent Transformer、Multi-Agent counterfactual credit、domain-specific workflow
node synthesis 与 world-model evaluation。它们分别说明：把参数深度与执行深度解耦会新增 recurrent
state、停止策略与稳定性边界；team reward 必须分离 outcome verification 与 role attribution；workflow
search 的 operator library 本身也可能是优化变量；interaction benchmark 若依赖 detector、flow、VLM
verifier 与 LLM aggregation，就必须把 metric pipeline 也视为受版本约束的被测系统。Omni-WorldBench
摘要的 human-alignment 表述与正文“未来发布”存在冲突，本周只保留为 `Disputed Evidence Boundary`。

第四批把 multimodal RL 分成两个不可混写的层次：UniGRPO 联合优化 autoregressive reasoning 与
flow-matching image trajectory，核心问题是 heterogeneous action spaces、shared terminal reward 与
regularization；PEPO 不改变 trajectory modality，而是在既有 GRPO/DAPO 内按 visual grounding 与
entropy 重分配 token credit。前者尚未验证 multi-round interleaving，后者只覆盖 2B/3B LVLM 与
curated benchmarks，均不得从作者 benchmark 外推为通用训练配方。

固定 AI Infra 来源又恢复三项高相关证据与一项跨周 artifact follow-up：PyTorch 2.11 把
differentiable collective、compiler-visible communication、backend/DTensor contract 放进同一版本边界；
Flight Recorder 说明 collective timeout 常是跨 rank 执行分歧的延迟症状，诊断必须保存每 rank 的
operation history 后离线对齐；TorchTitan 的 B200 实验则把 MXFP8 grouped GEMM 与 DeepEP dynamic
All-to-All 作为计算/通信两条正交优化联合测量。Astrolabe 3 月 23 日只发布代码，论文事件仍归 W12，
不因 artifact 可用而重复计为 W13 新机制。

第二轮 fixed-source 回放又恢复两个 vLLM 工程节点，并纠正 source-family owner：incremental MoE
expert offloading 的 open PR 于 3 月 16 日已首次公开，因此完整机制评分与 Source Review 回写 W12；
3 月 26 日 RFC 只在本周记录 provider abstraction、LFRU、persistent mapping 与 async roadmap 的架构
演进，不重复计分。`TRITON_MLA_SPARSE` 则由 3 月 24 日 issue 与 3 月 29 日 open PR 共同定义，是
W13 新候选：它把旧 GPU 支持问题拆成 compile/link guard、indexer logits fallback、Sparse MLA
attention backend 与 CUDA graph compatibility 四层。当前仍未合并，只能作为 Experimental implementation
evidence，不能写成 vLLM stable capability。

时间窗 API 枚举又恢复 Cross-Context Verification、DSPA 与 DRTriton。前者因 9 个 SWE-bench
problem 的极小样本和单一模型 contract 暂列低分边界；后两项现已完成全文、公式、实验、ablation、
关键 appendix、revision history 与章节邻接审计。DSPA 把全局 activation steering 改成 prompt gate
选择、output-feature ranking 与 token-active residual edit；DRTriton 把 synthetic program generator、
compiler-backed verifier、curriculum RL、speed/correctness reward 与 compositional test-time search
组成闭环。两者都成为 provisional Books candidates，但 Historical Books Gate 仍关闭。

MolmoWeb 的 Source Family 在全文审计时完成 event-date 纠偏：论文于 4 月 9 日提交，但 Ai2 已在
3 月 24 日公开发布模型、数据、评测工具与技术说明，因此 owner week 是 W13；W15 只记录论文与完整代码
到达的 artifact evolution。其长期机制不是某个 Web Agent 排名，而是把 browser data 从被动视觉感知、
atomic skill 推进到 end-to-end trajectory，并显式暴露 observation interface、action schema、teacher、
verifier、browser revision 与 evaluation harness 的共同 lineage。human demonstration 与 privileged
AxTree synthetic teacher 是不同数据分支；后者可以提高规模，却会引入 teacher-view/student-view mismatch、
benchmark-family alignment 与稀有行为覆盖不足，不能写成 synthetic data 对 human data 的通用替代。

`Lie to Me` 的全文、appendix、代码与公开数据审计进一步说明：CoT faithfulness 不是一个脱离
measurement contract 的模型常数。它同时依赖 baseline-to-target influence 定义、judge/classifier、解析
成功条件、hint family 与 provider/runtime revision；thinking text 里的显式承认也不能被解释为对内部计算
状态的直接读取。该证据与 Ch62 的 scorer contract、Ch68 的 policy-bound sensor 边界一致，暂定
`No Change — Already Covered (Experimental Evaluation Case)`，不在 Historical Books Gate 关闭时修改正文。

MedOpenClaw / MedFlow-Bench 又把 evaluation subject 从静态答案扩展到完整软件工作流：agent 必须在
3D Slicer / QuPath 的 bounded action surface 中维护 viewer state、生成坐标或 mask 等 evidence artifact，
再由 hidden reference 做 deterministic gate。论文中复杂 registration/segmentation 的失败不是单纯模型
“不会看图”，而是 objective drift、spatial grounding、state misbinding、artifact calibration 与 procedural
stability 的联合失败。该机制能细化 Ch62 的 trajectory evidence hierarchy，并与 Ch74/77/80 的 typed
tool、durable state 和 evidence plane 形成 `Layering / Dependency`；暂定 `Refine — Existing Argument
(Experimental; Artifact Partially Verified)`，但 Historical Books Gate 仍关闭。

Composer 2 的 technical report 提供了另一条可沉淀的系统演进：当 coding-agent rollout 变成长时、
有状态且生成/训练完全异步时，“sample 来自哪个 policy”不再只是一个 checkpoint ID。in-flight weight
hotload 可能让同一 trajectory 的前后 token 跨 policy revision；MoE inference/trainer 的数值差异又可能
改变 expert route。报告用 fast delta weight sync、policy-versioned group state、mid-rollout environment
snapshot 与 router replay 限制这种漂移。其长期价值是细化 Ch29 的 rollout identity / on-policy boundary，
不是把私有 CursorBench 或厂商榜单写成通用能力结论。

Hybrid Memory / HyDRA 则把 world-model memory 的目标从“返回同一视角时重建静态场景”扩展为
“动态主体离开视野后继续保持 identity 与 motion state”。它以 3D-convolution memory tokenizer 压缩
时空 latent，再让每个 target query 按 learned affinity 选择 top-k memory tokens，并与 local window
共同参与 attention。该机制只在合成 HM-World、Wan2.1-T2V-1.3B、32 GPUs、10K iterations 的作者
contract 下得到支持；三人以上复杂场景和 severe occlusion 已被作者列为限制。暂定细化 Ch10 的
world-model memory 分支，Ch14/22/62 只作 attention、长状态与 evaluation handoff。

Trace2Skill 进一步把“从轨迹中学习”拆成一种离线 artifact compilation：同一 frozen base Skill 面向每条
成功/失败轨迹独立地产生 patch，再用分层 many-to-one merge 去重、处理冲突并把高支持规则写入主
`SKILL.md`，低频边界放入 `references/`。它避免 sequential edit 的 order dependence，也把经验从
test-time retrieval 移到 pre-deployment consolidation；但这不是单向替代。35B 实验中的部分 Soft/Hard
指标仍由逐条编辑更好，retrieval memory 在证据强依赖 query、需要保留细粒度 provenance 或频繁更新时
仍然合理。论文为 work in progress，单 patch 因果贡献与 section-level usage attribution 尚未解决，公开
repository 也只覆盖 spreadsheet pipeline。暂定由 Ch80 拥有 Skill artifact lifecycle，Ch73/76/77 分别
承担 procedural memory、failure diagnosis 与 durable workflow handoff。

Natural-Language Agent Harnesses 则把 harness 的“可迁移 design-pattern layer”与 deterministic runtime
分开：roles、contracts、stage topology、state semantics、failure taxonomy 可以写成可审计 artifact，由
共享 IHR 解释；tool adapter、sandbox、parser 与 verifier 仍由代码拥有。它的实验不支持“结构越多越好”：
125 个 SWE-bench 与 36 个 OSWorld 固定子集中，Full IHR 主要改变 token/call/runtime 和少量边界样本，
verifier 与 multi-candidate search 还可能因 local acceptance 和 final evaluator 不一致而退化。长期价值是让
harness 成为 versioned、可消融的系统对象，并明确 semantic policy 与 deterministic enforcement 的边界；
暂定由 Ch77 拥有，Ch80/78/62 分别承接 registry/run、delegation 与 evaluation identity。

Density-aware Soft Context Compression 暴露另一条系统设计原则：workload 的信息密度可以连续变化，
但模型与 kernel 不必因此支持无限种执行 shape。它让 regression head 预测 teacher-summary-length proxy，
再量化到少量 ratio buckets，由 mean pooling 产生可变数量 latent tokens；连续 `scale` 只平移 bucket
分布，实际结构仍是离散集合。该机制在 Qwen3-0.6B/4B、短于 2K 的 synthetic/reading-comprehension
contract 下优于被测 static baselines，却未证明 summary length 是真实信息充分性的 oracle，也没有端到端
TTFT/KV/concurrency/SLO 测量。暂定细化 Ch22 的 working-set compression 分支，Ch71/41 只连接 Context
assembly identity 与 decoder KV/runtime contract。

Learning to Commit 又把 repository-specific memory 的学习信号从“阅读当前 snapshot”推进到“比较自己在
历史 snapshot 上的 blind attempt 与当时 accepted oracle diff”。每次差异被提炼为可 CRUD、可弃用的
procedural Skill，再用于严格时间切分后的未来任务；snapshot、attempt、oracle diff、derived Skill 与 future
evaluation 因而不能压成一个 Context。这个机制补足 Ch73 的 derived procedural memory，但论文仅测试一个
内部仓库、24 个 learning commits 与 7 个 future tasks，Claude Opus 4.6 的成本、sampling、variance 和
artifact 均未公开；pairwise judge 也没有证明 maintainer 会真实 merge。暂定为 Ch73 Experimental refinement，
Ch80/62 只承接 Skill registry 与 temporal evaluation。

TAPS 把 speculative drafter 的 identity 再向 workload distribution 扩展：相同 HASS/EAGLE-2 backbone、
target 和 verifier rule 下，MathInstruct 与 ShareGPT specialists 在不同任务上产生不同 proposal quality。
多个 specialist 不必被权重平均成一个 checkpoint；可以分别生成 tree 后按 mean confidence 选择，或把两个
subtrees 置于 shared root 下、隔离 cross-subtree attention，再由 target 一次验证。后者在 valid-tree 假设下
保持 target sampling law，却增加两个 draft tree 的生成和更大 verification work。论文主指标是 acceptance
length，并明确没有建立端到端 latency/SLO 结论；因此暂定细化 Ch44 的 workload-scoped draft artifact 与
runtime composition，不写成 weight merge 普遍失败或 merged tree 普遍最优。

DataFlex 则把“数据配比是训练前配置”推进为显式 feedback-control interface：Select、Mix、Weight 三类
Trainer 在不同 cadence 读取 embedding、loss、inference、gradient 或 validation signal，输出 sample subset、
domain proportion 或 per-sample weight，再作用到后续 optimization。旧的 offline filter/static mixture 仍有
低开销、可复现和稳定 data order 的优势；online control 新增 feedback delay、selection bias、policy state、
sharded-gradient reconstruction 与 evaluation leakage。该论文的长期价值是统一 signal/action/cadence/state
边界和 distributed ownership，暂定由 Ch23 拥有、Ch24/35/56/62 handoff，不保留单 seed MMLU 或 runtime
headline。

Ask or Assume 又把“需要澄清”从 prompt 中的一句提醒提升为运行时 gate：Main Agent 负责 repository
探索、代码修改与执行，Intent Agent 每轮只读取 state history、判断 external underspecification，并在需要时
约束下一动作必须向用户询问。其价值在职责隔离和持续 observation，而不是 Agent 数量；v2 的 Kimi K2.6
过度询问说明同一 scaffold 的 calibration 受 backbone 与 tool semantics 影响。暂定由 Ch77 拥有，Ch78/75/62
只承接 role decomposition、belief/replanning 与 interactive evaluation，不把 simulated-user benchmark 外推为
真实 human collaboration。

XpertBench 则把开放式 expert-task evaluation 拆成 expert-authored atomic rubric、权重、baseline response
的 expert rationale、one-shot model judge 与 weighted aggregation。它提供一个受限案例，但 Ch62 已经拥有
更完整的 rubric formation → criterion execution → aggregation/ranking → decision policy 分层；而 Gold subset
只有 245 项、CDR 只有 52%、公开 dataset 当前为空，也没有 seeds、variance、judge abstention/invalid 或
完整 prompt/model runtime contract。故只作 `No Change` 证据，不用 benchmark headline 改写正文。

EpochX 把 Agent Platform 的控制对象再向开放生产网络延伸：人和 Agent 都可发布或承接任务，lead solver
可在父 bounty 预算内递归委托，交付经 requester acceptance 后结算，执行产生的 Skill、Workflow、Trace 与
Experience 经过 validation operator 后进入 dependency graph，并按后续 reuse 分配 credits。这个组合明确了
task、delegation、artifact 与 settlement 的状态边界，却没有证明 incentive alignment：论文只有两个平台交付
案例和一个概念性搬家案例，没有纵向 reuse、竞争、欺诈/串谋、争议/退款、身份信誉或 programmable verifier
实验；官方产品页确认平台 live，但未公开实现和可审计交易 artifact。Ch77/78/80 已分别覆盖 durable workflow、
bounded delegation 与 governed Skill lifecycle，因此暂定 `No Change — Already Covered (Ch80; Experimental
Case; Platform Accessible; Implementation Not Disclosed)`，credits layer 只保留为未来研究压力。

daVinci-LLM 则把数据工程从单一“清洗强度”拆成 selection、refinement、completion 与 synthesis 等不同
operator semantics，并用 8T-token、四阶段 checkpoint trajectory 观察不同 domain 与 data format 的边际价值
如何随模型状态变化。证据支持“数据 action 与 mixture 应绑定 checkpoint state、evaluation protocol 和
training stage”，但不支持把 L0～L9 当成单调质量阶梯，也不支持 30%/70% QA 等作者配比成为通用配方。
论文公开的 3.09B/Qwen2、BF16、4096 context 和训练/evaluation contract 较完整，却未披露 hardware、
compute、seed/variance；官方 repository 的 pretraining pipeline 仍标记 `Coming soon`，data card 也只开放
subset。故暂定细化 Ch23 的 data-policy/control-loop 论证，Ch24/25/56/62 只承接 pretraining/SFT、operator
与 evaluation handoff，并将 artifact 状态明确为 `Partially Available`。

`Emergent Social Intelligence Risks` 把 Multi-Agent 风险从“某个 Agent 出错”推进到 interaction、incentive、
information flow 与 governance 共同拥有的系统状态。论文用 15 类受控 simulation 将局部理性但系统有害的
equilibrium、majority/authority-driven biased convergence、缺少 clarification/arbitration/replanning 的治理失效，
以及 resource overreach、steganography、sequential semantic drift 分开测量。它支持的是一套可操作的风险
taxonomy 和外部 indicator 设计，不是生产发生率：不同场景使用不同 backbone、trial 数和 LLM judge，缺少
统一 seeds/variance、真实部署对照、独立 Limitations 章节和公开 artifact。故暂定细化 Ch78 的 coordination
failure / governance 论证，Ch62/68 只承接 EvalSpec 与 threat-model handoff；简单 prompt warning 不能替代
mechanism-level constraint，但论文列出的 mitigation 也尚未形成受控、可复现的效果证据。

PRBench 则把 scientific-agent evaluation 从 paper QA / formula understanding 推进到 end-to-end executable
reproduction：30 个 physics tasks 都要求读取论文、从零实现、在 task-specific Docker budget 内运行并产生
与 expert reference 对齐的 CSV。方法、代码、数据准确性与完成度分别评分，另用四项均高于 0.9 的 hard
callback gate 阻止平均分掩盖致命失败。它强力支持“surface understanding 不是 scientific completion”，但
Ch62 已完整覆盖 artifact + environment + trace + verifier、rubric 分层与 hard gate；本项因此为 `No Change`
案例。公开 harness 只含一个完整 benchmark sample，论文也未披露 judge identity/prompt、agent token/cost/
sampling 与完整 30-task artifact，故排行榜与 0% callback 只在作者 contract 内成立。

MuSEAgent 把 experience memory 的粒度从整条 trajectory 下沉到单步 state-action transition：hindsight model
为 transition 生成 quality score 与 guidance，达阈值后按 query/image/task/history 等多个 view 建索引；推理时
先选 view，再通过 Deep/Wide search 汇集经验后生成下一 action。这一机制细化了 Ch73 已有的 raw episode →
derived procedural memory 演进，但没有取代完整 trajectory：后者仍拥有因果上下文、provenance 与 replay。
官方代码公开 trace、state bank、tools 和运行配置，然而实验只覆盖四个多选 VQA 的 1:1 exploration/eval
split，未披露 hardware、latency/cost、multi-seed/variance，GPT-4o hindsight 同时拥有 filter/guidance 权力，
也没有 supersession、delete、online invalidation 或 policy authority。因此暂定 Ch73 Experimental refinement。

KAT-Coder-V2 则把 agentic coding post-training 从单一 dataset/objective 扩展为 workload contract：environment、
tools、scaffold、task 与 verifier 共同定义 rollout；五个 domain experts 先分别 SFT/RL，再由 unified student
在自身 trajectory 上联合接受 environment reward 与 expert dense supervision。turn-level ratio、MoE logprob
重复估计和 tree-structured trajectory training 分别处理 credit granularity、estimator variance 与 shared-prefix
重算，但公开证据没有 model architecture、训练 hardware/precision、关键 ablation 或 KwaiEnv/KRL code。
因此暂定 Ch29 New Mechanism candidate，Ch36/56/77 只作 runtime/workflow handoff，并保持
`Experimental / Implementation Not Disclosed`；6.2× 与榜单数字只属于作者未完整披露的 contract。

LongCat-Next 补出另一条跨模型与系统的长期演进：连续视觉/音频 feature 接入语言模型时，modality encoder
与 projection 负责语义对齐，低数据量、追求理解能力时仍是合理分支；若要让同一 autoregressive backbone
同时生成和理解多模态内容，则输入/输出需要先成为可预测、可重建的离散协议。DiNA 用 modality-specific
tokenizer/detokenizer、semantic-aligned residual quantization、统一 next-token backbone 与 modality-specific
output head 实现这条路径。它同时引入 codebook/quantization error、更长序列、codec 与 backbone 的双重
版本身份，以及稀有 token 的 train/inference mismatch。论文在自有训练与 benchmark contract 内说明增加
数据可缩小 discrete/continuous 差距，并展示 MoE route specialization，但没有证明离散协议普遍优于连续
feature，也没有把 routing observation 证明为固定语义 expert。VHalf pipeline 的 device folding 暴露了
heterogeneous boundary module 的负载与通信问题，但公开材料缺少 GPU/topology/precision/吞吐/SLO 合同，
只能作为实验性 Ch34 handoff。主 owner 暂定 Ch11：把 tokenizer 从 text-only vocabulary 扩展为跨模态
离散 interface；Ch12/21/29/34 分别承接 representation、MoE、RL mismatch 与 pipeline runtime。

当前 45 条评分来自已完成 source-family 归一化与评分的候选。W14 的 curation-lag ledger 已回拨 20 个
first-public date 位于 03-23～03-29 的候选；其中 `Lie to Me`、MedOpenClaw、Composer 2、Hybrid Memory、Trace2Skill、Natural-Language Agent Harnesses、Density-aware Soft Context Compression、Learning to Commit、TAPS 与 DataFlex 已完成全文审计，
Ask or Assume、XpertBench、EpochX、daVinci-LLM、`Emergent Social Intelligence Risks`、PRBench、MuSEAgent、KAT-Coder-V2 与 LongCat-Next 也已完成全文、revision 与 artifact boundary 审计，
ClawKeeper 因 primary text 在检索、直连与可视浏览入口均不可访问而进入 `Unverified / Blocked Backlog`，
没有 current-review pending。ClawKeeper 不被标题与 arXiv ID 冒充 Full Source Review，也不阻塞单向
forward cursor。W13 Forward Candidate Evidence Gate 因而通过，broader Historical Evidence Gate 仍因跨周
spillback、fixed-source recall 与 blocked backlog 保持 Open；Historical Books Gate 继续关闭。

## Coverage and Source Coverage

- 模型与研究机构：保留 Anthropic 3 月 24 日与 Meta 3 月 26/27 日；Google 3 月 24 日对
  TurboQuant 的传播必须回到 2025 原论文与 2026 reproduction critique，不能当作 2026 新机制。
- arXiv / 学术来源：已完成 35 篇 2026-03-23～03-29 v1 论文/technical report 的全文、关键 appendix、evaluation
  contract 与可访问 artifact 核验；时间窗枚举另恢复的 DSPA、DRTriton 已完成全文，CCV 完成低分
  边界核验；curation/recommendation date 不替代 arXiv first-public date。
- AI Infra：已完成 PyTorch 2.11 release/blog/相关 RFC、Flight Recorder engineering blog、TorchTitan
  MXFP8+DeepEP recipe/merged integration、vLLM MoE offload PR/RFC lineage、`TRITON_MLA_SPARSE`
  issue/open PR 与 Astrolabe code-release follow-up；Hugging Face 历史 papers 页面受保存的访问策略阻断，
  已显式记为 coverage limitation，不能沿用旧版“未发现 stable release”的结论。
- 2026-08-13 retry：ClawKeeper 的 exact arXiv HTML 仍被保存的用户访问策略明确禁止；OpenAlex 周窗口
  cross-index 请求也被本次用户权限拒绝。按 blocked-skip 规则，不切换浏览器、不走间接绕过，也不把
  空返回解释成“无遗漏”。这两项分别记为 primary-source blocker 与 discovery-index limitation；Google
  Scholar、DBLP 的目录级周窗口仍未取得可机器复算快照。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Review-stage Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Anthropic Economic Index: learning curves | 3 | 3 | 4 | 4 | 3 | 4 | 21/30 | Full Review Complete — No Change candidate |
| TRIBE v2 | 3 | 3 | 3 | 4 | 2 | 3 | 18/30 | Record Only |
| SAM 3.1 | 3 | 3 | 3 | 4 | 2 | 3 | 18/30 | Record Only |
| mSFT: heterogeneous early stopping for dataset mixtures | 5 | 4 | 4 | 5 | 5 | 5 | 28/30 | Full Review Complete — Books pending |
| On the Direction of RLVR Updates | 5 | 4 | 4 | 5 | 5 | 5 | 28/30 | Full Review Complete — Books pending |
| Scaling DoRA | 4 | 4 | 5 | 5 | 5 | 5 | 28/30 | Full Review Complete — Books pending |
| CAID: asynchronous SWE agents | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Review Complete — Books pending |
| SpecEyes: agentic-level speculative execution | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Review Complete — Books pending; Experimental |
| From Static Templates to Dynamic Runtime Graphs | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Full Review Complete — Books pending |
| Sparse but Critical: RLVR distribution shifts | 5 | 5 | 4 | 5 | 5 | 5 | 29/30 | Full Review Complete — Books pending |
| Thinking Deeper, Not Longer: depth-recurrent Transformer | 5 | 4 | 3 | 4 | 4 | 5 | 25/30 | Full Review Complete — Books pending; Experimental |
| CCPO: counterfactual role credit | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Review Complete — Books pending; Experimental |
| Unified-MAS: domain-specific workflow nodes | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Review Complete — Books pending; Experimental |
| Omni-WorldBench | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Review Complete — Disputed Evidence Boundary |
| UniGRPO: joint text/flow policy optimization | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Review Complete — Books pending; Experimental |
| PEPO: perception-exploration token credit | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Full Review Complete — Books pending; Experimental |
| PyTorch 2.11: differentiable and compiler-visible collectives | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Review Complete — Books pending; Versioned |
| PyTorch Flight Recorder for collective timeouts | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Full Review Complete — Books pending |
| TorchTitan MXFP8 + DeepEP B200 integration | 3 | 5 | 5 | 5 | 5 | 5 | 28/30 | Full Review Complete — No Change candidate |
| vLLM `TRITON_MLA_SPARSE` portability path | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Review Complete — Refine candidate; Experimental; open PR |
| Astrolabe code release follow-up | 2 | 3 | 4 | 4 | 2 | 2 | 17/30 | Cross-week Artifact Follow-up Only |
| Cross-Context Verification / HCCA | 3 | 3 | 3 | 3 | 4 | 3 | 19/30 | Low-score Boundary Verified — tiny evaluation contract |
| DSPA: dynamic SAE steering for preference alignment | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | Full Review Complete — Integrate candidate; Experimental |
| DRTriton: synthetic-data RL for Triton kernel generation | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Review Complete — Refine candidate; Experimental |
| TurboQuant | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Review Complete — Disputed |
| MolmoWeb: open visual web-agent data and runtime | 4 | 4 | 5 | 4 | 5 | 3 | 25/30 | Full Review Complete — Refine candidate; Experimental; moved from W15 by official first-public date |
| Lie to Me: CoT faithfulness across open reasoning models | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Review Complete — No Change candidate; Experimental Evaluation Case |
| MedOpenClaw / MedFlow-Bench: auditable full-study imaging workflow | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Review Complete — Refine candidate; Experimental; Artifact Partially Verified |
| Composer 2: domain-matched asynchronous coding-agent RL | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Review Complete — Refine candidate; Versioned Vendor Evidence |
| Hybrid Memory / HyDRA for dynamic video world models | 5 | 4 | 4 | 4 | 4 | 5 | 26/30 | Full Review Complete — Refine candidate; Experimental; Artifact Partially Reproducible |
| Trace2Skill: trajectory-to-skill compilation | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Full Review Complete — Refine candidate; Experimental; Artifact Partially Reproducible |
| Natural-Language Agent Harnesses / IHR | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Review Complete — Refine candidate; Experimental; Artifact Partially Reproducible |
| Density-aware soft context compression / DRS | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Full Review Complete — Refine candidate; Experimental; Artifact Available |
| Learning to Commit: online repository memory | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Full Review Complete — Refine candidate; Experimental; Artifact Not Available |
| TAPS: task-aware proposal distributions | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Full Review Complete — Refine candidate; Experimental; Artifact Available |
| DataFlex: data-centric dynamic training system | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Review Complete — Refine candidate; Experimental; Artifact Available |
| Ask or Assume: uncertainty-aware clarification gate | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Review Complete — Refine candidate; Experimental; Artifact Available |
| XpertBench: expert-authored rubric evaluation | 4 | 4 | 4 | 3 | 5 | 5 | 25/30 | Full Review Complete — No Change candidate; Experimental; Artifact Not Available |
| EpochX: credits-native human-agent production network | 4 | 4 | 3 | 3 | 5 | 4 | 23/30 | Full Review Complete — No Change candidate; Experimental Case; Platform Accessible; Implementation Not Disclosed |
| daVinci-LLM: data-processing and stage-aware mixture system | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Review Complete — Refine candidate; Experimental; Artifact Partially Available |
| Emergent Social Intelligence Risks in Generative Multi-Agent Systems | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Full Review Complete — Refine candidate; Experimental; Artifact Not Available |
| PRBench: end-to-end paper reproduction in physics | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Full Review Complete — No Change candidate; Experimental; Artifact Partially Available |
| MuSEAgent: stateful multimodal experience retrieval | 4 | 4 | 5 | 5 | 5 | 5 | 28/30 | Full Review Complete — Refine candidate; Experimental; Artifact Available |
| KAT-Coder-V2: specialize-then-unify agentic coding post-training | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Review Complete — Integrate candidate; Experimental; Implementation Not Disclosed |
| LongCat-Next: native discrete autoregressive multimodality | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Review Complete — Integrate candidate; Experimental; Artifact Partially Reproducible |

评分已经过 Source Review 复算；45 行是当前 W13 repaired candidate set，不表示 broader Historical
Evidence Gate 已闭合；后续 fixed-source 或 spillback correction 仍可能显式扩展本表。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Existing W13 source families | 4 | 两项 `20+` Full Review；TRIBE v2 与 SAM 3.1 分别完成低分核验 |
| Recovered and fully reviewed candidate families | 39 | direct arXiv / official release、RFC/PR、全文或完整工程材料、evaluation contract 与章节邻接已核对 |
| Current scored candidate families | 45 | 41 项 `>=20`；4 项低分/跨周 artifact 核验 |
| W14 curation-lag spillbacks awaiting review | 0 | 19 个可访问 in-window candidates 均已完成；ClawKeeper 单列 blocked backlog；Sommelier、SEAR、FIPO 已路由 W12 backlog |
| Unverified / Blocked Backlog | 1 | ClawKeeper；primary text 未返回可核验正文；未评分、未推断机制、不会阻断 forward cursor |
| Recorded `20+` Full Source Reviews complete | 41/41 | 全部 scored `20+` candidates 已完成非模板化 Source Review |
| Current-review backlog | 0 | ClawKeeper 独立进入 blocked ledger，不冒充已读、不阻塞 forward cursor |
| External discovery retry | Blocked / Limited | 2026-08-13：arXiv 受保存策略禁止；OpenAlex 请求被拒；Scholar/DBLP 未形成可复算周快照 |
| W13 Forward Candidate Evidence Gate | Passed | intake queue 清零；broader Historical Evidence Gate 仍为 Open |

## W14 Curation-Lag Spillback Intake Ledger

以下 20 项由 W14 discovery feed 发现，但 W14 已依据 arXiv v1 / first-public date 将其回拨到 W13。
本表只恢复审计队列：在逐项打开 primary source 前，日期、版本、评分、机制与 owner 都保持待核，
不得把 `arXiv ID located` 写成 `Full Source Review Complete`。

| Provisional First-public Date | Candidate | Located Primary Identity | Review State |
| --- | --- | --- | --- |
| 2026-03-23 | Lie to Me | arXiv:2603.22582 | Full Source Review Complete — 25/30；No Change candidate；Experimental |
| 2026-03-25 | MedOpenClaw | arXiv:2603.24649 | Full Source Review Complete — 29/30；Refine candidate；Experimental；Artifact Partially Verified |
| 2026-03-25 | Composer 2 | arXiv:2603.24477 | Full Source Review Complete — 29/30；Refine candidate；Versioned Vendor Evidence |
| 2026-03-25 | ClawKeeper | arXiv:2603.24414 | Unverified / Blocked Backlog — primary text unavailable；unscored；forward cursor continues |
| 2026-03-26 | Hybrid Memory | arXiv:2603.25716 | Full Source Review Complete — 26/30；Refine candidate；Experimental；Artifact Partially Reproducible |
| 2026-03-26 | Trace2Skill | arXiv:2603.25158 | Full Source Review Complete — 27/30；Refine candidate；Experimental；Artifact Partially Reproducible |
| 2026-03-26 | Natural-Language Agent Harnesses | arXiv:2603.25723 | Full Source Review Complete — 28/30；Refine candidate；Experimental；Artifact Partially Reproducible |
| 2026-03-26 | Density-aware compression | arXiv:2603.25926 | Full Source Review Complete — 26/30；Refine candidate；Experimental；Artifact Available |
| 2026-03-27 | Learning to Commit | arXiv:2603.26664 | Full Source Review Complete — 25/30；Refine candidate；Experimental；Artifact Not Available |
| 2026-03-27 | TAPS | arXiv:2603.27027 | Full Source Review Complete — 29/30；Refine candidate；Experimental；Artifact Available |
| 2026-03-27 | DataFlex | arXiv:2603.26164 | Full Source Review Complete — 28/30；Refine candidate；Experimental；Artifact Available |
| 2026-03-27 | Ask or Assume | arXiv:2603.26233 | Full Source Review Complete — 28/30；Refine candidate；Experimental；Artifact Available |
| 2026-03-27 | XpertBench | arXiv:2604.02368 | Full Source Review Complete — 25/30；No Change candidate；Experimental；Artifact Not Available |
| 2026-03-28 | EpochX | arXiv:2603.27304 | Full Source Review Complete — 23/30；No Change candidate；Experimental Case；Platform Accessible；Implementation Not Disclosed |
| 2026-03-28 | daVinci-LLM | arXiv:2603.27164 | Full Source Review Complete — 28/30；Refine candidate；Experimental；Artifact Partially Available |
| 2026-03-29 | Emergent Social Intelligence Risks | arXiv:2603.27771 | Full Source Review Complete — 27/30；Refine candidate；Experimental；Artifact Not Available |
| 2026-03-29 | PRBench | arXiv:2603.27646 | Full Source Review Complete — 27/30；No Change candidate；Experimental；Artifact Partially Available |
| 2026-03-29 | MuSEAgent | arXiv:2603.27813 | Full Source Review Complete — 28/30；Refine candidate；Experimental；Artifact Available |
| 2026-03-29 | KAT-Coder-V2 | arXiv:2603.27703 | Full Source Review Complete — 29/30；Integrate candidate；Experimental；Implementation Not Disclosed |
| 2026-03-29 | LongCat-Next | arXiv:2603.27538 | Full Source Review Complete — 29/30；Integrate candidate；Experimental；Artifact Partially Reproducible |

### Routed out of W13

W14 同一 ledger 还包含 Sommelier、SEAR 与 FIPO。其 provisional first-public date 是 2026-03-20，属于
W12（2026-03-16～03-22），不计入 W13 候选或 pending 数。W12 当前尚未记录这三个名称，故它们进入
W12 spillback backlog；待 W13 forward checkpoint 完成后回补，不用推荐流日期制造 W13 事件。

| Provisional First-public Date | Candidate | Located Primary Identity | Destination |
| --- | --- | --- | --- |
| 2026-03-20 | Sommelier | arXiv:2603.25750; ID/date boundary requires recheck | W12 spillback backlog |
| 2026-03-20 | SEAR | arXiv:2603.26728; ID/date boundary requires recheck | W12 spillback backlog |
| 2026-03-20 | FIPO | arXiv:2603.19835 | W12 spillback backlog |

## Recovered Candidate Census — Batch 1

| First-public Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-23 | mSFT | arXiv:2603.21606 v1 | Ch25 | Full Review Complete — Books pending |
| 2026-03-23 | On the Direction of RLVR Updates | arXiv:2603.22117 v1 | Ch29 | Full Review Complete — Books pending |
| 2026-03-23 | Scaling DoRA | arXiv:2603.22276 v1 | Ch26 | Full Review Complete — Books pending |
| 2026-03-23 | Effective Strategies for Asynchronous SWE Agents / CAID | arXiv:2603.21489 v1 | Ch78 | Full Review Complete — Books pending |
| 2026-03-23 | From Static Templates to Dynamic Runtime Graphs | arXiv:2603.22386 v1 | Ch77 | Full Review Complete — Books pending |
| 2026-03-23 | Sparse but Critical | arXiv:2603.22446 v1 | Ch29 | Full Review Complete — Books pending |
| 2026-03-24 | SpecEyes | arXiv:2603.23483 v1 | Ch77 | Full Review Complete — Books pending; Experimental |

## Recovered Candidate Census — Batch 3

| First-public Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-23 | Thinking Deeper, Not Longer | arXiv:2603.21676 v1 | Ch17 | Full Review Complete — Books pending; Experimental |
| 2026-03-23 | CCPO | arXiv:2603.21563 v1; current v5 revision checked | Ch29 | Full Review Complete — Books pending; Experimental |
| 2026-03-23 | Unified-MAS | arXiv:2603.21475 v1 | Ch77 | Full Review Complete — Books pending; Experimental |
| 2026-03-23 | Omni-WorldBench | arXiv:2603.22212 v1 | Ch62 | Full Review Complete — Disputed Evidence Boundary |

## Recovered Candidate Census — Batch 4

| First-public Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-24 | UniGRPO | arXiv:2603.23500 v1 | Ch29 | Full Review Complete — Books pending; Experimental |
| 2026-03-24 | PEPO | arXiv:2603.22847 v1 | Ch29 | Full Review Complete — Books pending; Experimental |

## Recovered Candidate Census — Batch 5

| Event Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-23 | PyTorch 2.11 | official v2.11.0 release, release blog, RFC/code links | Ch32 | Full Review Complete — Books pending; Versioned |
| 2026-03-25 | Flight Recorder | official PyTorch engineering blog and docs/code links | Ch64 | Full Review Complete — Books pending |
| 2026-03-25 | MXFP8 + DeepEP for DeepSeek-V3 on B200 | official PyTorch/Nebius recipe and merged TorchTitan PR | Ch32 | Full Review Complete — No Change candidate |
| 2026-03-23 | Astrolabe code release | official repository; paper first-public 2026-03-17 | Ch29 | Cross-week Artifact Follow-up Only |

## Recovered Candidate Census — Batch 6

| First-public Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-23 | Cross-Context Verification / HCCA | arXiv:2603.21454 v1 | Ch62 | Low-score Boundary Verified — 9-problem contract |
| 2026-03-23 | DSPA | arXiv:2603.21461 v1 | Ch27 | Full Review Complete — Integrate candidate; Experimental |
| 2026-03-23 | DRTriton | arXiv:2603.21465 v1 + v2 revision check | Ch45 | Full Review Complete — Refine candidate; Experimental |

## Recovered Candidate Census — Batch 7

| Event Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-24 | MolmoWeb | Ai2 official release + collection; arXiv:2604.08516 v1 and full-code release are later artifact evolution | Ch23 | Full Review Complete — Refine candidate; Experimental |

## Recovered Candidate Census — Batch 8

| Event Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-24 / 2026-03-29 | vLLM `TRITON_MLA_SPARSE` portability path | vLLM issue #38006 + open PR #38476 | Ch45 | Full Review Complete — Refine candidate; Experimental |
| 2026-03-26 | vLLM incremental MoE expert offloading RFC | vLLM RFC #38256; source family first-public by PR #37190 on 2026-03-16 | W12 / Ch50 | Cross-week Architecture Follow-up Only — not rescored |

## Recovered Candidate Census — Batch 9

| First-public Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-23 | Lie to Me | arXiv:2603.22582 v1 + author code/data | Ch62 / Ch68 | Full Review Complete — No Change；Experimental Evaluation Case |
| 2026-03-25 | MedOpenClaw / MedFlow-Bench | arXiv:2603.24649 v1；v2 revision and project/artifact boundary checked | Ch62 | Full Review Complete — Refine candidate；Experimental；Artifact Partially Verified |
| 2026-03-25 | Composer 2 | arXiv:2603.24477 v1/v2 + Cursor official research note | Ch29 | Full Review Complete — Refine candidate；Versioned Vendor Evidence |
| 2026-03-26 | Hybrid Memory / HyDRA | arXiv:2603.25716 v1 + author project/repository/model card | Ch10 | Full Review Complete — Refine candidate；Experimental；Artifact Partially Reproducible |

## Recovered Candidate Census — Batch 10

| First-public Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-26 | Trace2Skill | arXiv:2603.25158 v1 + official repository; later revisions checked as artifact evolution | Ch80 | Full Review Complete — Refine candidate；Experimental；Artifact Partially Reproducible |
| 2026-03-26 | Natural-Language Agent Harnesses | arXiv:2603.25723 v1；v2 and LinguaClaw continuation checked as post-window evolution | Ch77 | Full Review Complete — Refine candidate；Experimental；Artifact Partially Reproducible |
| 2026-03-26 | Density-aware Soft Context Compression | arXiv:2603.25926 v1 + official code/data/LoRA weights | Ch22 | Full Review Complete — Refine candidate；Experimental；Artifact Available |

## Recovered Candidate Census — Batch 11

| First-public Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-27 | Learning to Commit | arXiv:2603.26664 v1；internal repository/data not public | Ch73 | Full Review Complete — Refine candidate；Experimental；Artifact Not Available |
| 2026-03-27 | TAPS | arXiv:2603.27027 v1 + official code/weights/datasets | Ch44 | Full Review Complete — Refine candidate；Experimental；Artifact Available |
| 2026-03-27 | DataFlex | arXiv:2603.26164 v1 + official code/docs/datasets | Ch23 | Full Review Complete — Refine candidate；Experimental；Artifact Available |

## Recovered Candidate Census — Batch 12

| First-public Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-27 | Ask or Assume | arXiv:2603.26233 v1/v2 + official code/evaluation setup | Ch77 | Full Review Complete — Refine candidate；Experimental；Artifact Available |
| 2026-03-27 | XpertBench | arXiv:2604.02368 v1/v4 + official platform/empty dataset record | Ch62 | Full Review Complete — No Change；Experimental；Artifact Not Available |
| 2026-03-28 | EpochX | arXiv:2603.27304 v1 + official product page/live-platform boundary | Ch80 | Full Review Complete — No Change；Experimental Case；Platform Accessible；Implementation Not Disclosed |
| 2026-03-28 | daVinci-LLM | arXiv:2603.27164 v1 + official repository/model/data cards | Ch23 | Full Review Complete — Refine candidate；Experimental；Artifact Partially Available |

## Recovered Candidate Census — Batch 13

| First-public Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-29 | Emergent Social Intelligence Risks | arXiv:2603.27771 v1；v2 revision boundary checked；no public artifact located | Ch78 | Full Review Complete — Refine candidate；Experimental；Artifact Not Available |
| 2026-03-29 | PRBench | arXiv:2603.27646 v1 + official project/evaluation harness; one full public sample task | Ch62 | Full Review Complete — No Change；Experimental；Artifact Partially Available |
| 2026-03-29 | MuSEAgent | arXiv:2603.27813 v1 + official code/configuration/evaluation data | Ch73 | Full Review Complete — Refine candidate；Experimental；Artifact Available |

## Recovered Candidate Census — Batch 14

| First-public Date | Candidate | Direct Primary Source | Owner | Review State |
| --- | --- | --- | --- | --- |
| 2026-03-29 | KAT-Coder-V2 | arXiv:2603.27703 v1 + official hosted-product boundary | Ch29 | Full Review Complete — Integrate candidate；Experimental；Implementation Not Disclosed |

## Evidence Level

- mSFT、RLVR direction、Scaling DoRA、CAID、SpecEyes、workflow optimization survey、Sparse but
  Critical、depth recurrence、CCPO、Unified-MAS、Omni-WorldBench、UniGRPO 与 PEPO 已覆盖论文正文、方法、实验或
  evidence inventory、ablation/sensitivity、关键 appendix；PyTorch 2.11、Flight Recorder 与
  TorchTitan integration 已覆盖 official release、design/RFC 或实现链接、完整 engineering evidence 与限制
  和目标/相邻章节；作者数字只在各自 workload contract 内成立。
- compression 收益必须绑定模型、layer、precision、hardware、kernel 与 quality；usage 报告需
  绑定样本窗口和 taxonomy；Meta 条目是垂直官方发布。
- 当前 coverage 仍是 in-progress checkpoint：发现页、推荐页和 abstract 只用于 recall，不能替代
  primary-source full review。DSPA 与 DRTriton 已完成全文审计，但论文作者数字仍绑定各自模型、
  verifier、benchmark、hardware/revision 与 evaluation contract；W13 discovery recall 尚未关闭。
- MolmoWeb 已联合核对 3 月 24 日 Ai2 发布、Hugging Face collection、4 月 9 日论文全文及 4 月 10 日
  full-code release。论文的 task success、pass@k 与 best-of-N 只在作者的 browser、judge、retry、
  step budget、模型和 benchmark contract 内成立；不能外推为生产 selector、side-effect safety 或通用
  visual-Agent reliability。
- vLLM `TRITON_MLA_SPARSE` 已覆盖 issue root-cause decomposition、open PR mechanism/change inventory、
  tests、8×A100 single-prompt benchmark contract、review disagreement、later revision/failure evidence 与
  Ch44～46 邻接；它证明一个候选 portability path，而不是 merged support 或跨 GPU 的通用性能结论。
  MoE expert offloading 的 first-public owner 已回拨 W12，W13 RFC 只保留架构演进。

## Cross-Week Deduplication

- mSFT 与 mixture-ratio optimization、continual SFT 的关系是不同 data-scheduling branch，不是后者
  被推翻；它用 task-level early-stop/rollback 改写 active mixture。
- RLVR direction 与 sparse-token update 研究组成同一 Source Family，后续按 intervention design 与
  base/RL model pair 去重，不按相似标题合并。
- `Sparse but Critical` 用 JS-divergence intervention 研究 magnitude/position，`On the Direction` 用
  signed `Δlog p` 研究 direction；它们属于同一 family 的互补证据，不能把 divergence magnitude
  与 signed preference change 混为同一个量。
- Scaling DoRA 是 DoRA equation 的 implementation evolution；LoRA/低 rank DoRA 在 memory headroom
  足够或非 CUDA 环境仍成立。
- CAID 是 Ch78 task-topology matching 的 branch-and-merge 实例；它不等于通用 Multi-Agent scaling law。
- SpecEyes 与经典 speculative decoding 属于 `Principle Reuse`：前者直接接受 small-model answer 或
  fallback，改变了质量—延迟 operating point；后者的 exact acceptance 保护 target distribution。
- Workflow survey 是 taxonomy/evidence synthesis，不与其收录的 39 篇 core papers 重复计为独立机制。
- Depth recurrence 与固定 `L` 层 Transformer 是 `Direct Evolution`，不是让 token-level CoT 失效；它
  复用同一个 block 的参数，却增加跨 step hidden state、depth budget 与停止策略。
- CCPO 位于 reward-construction / credit-assignment 层，不是 GRPO、GSPO 的替代优化器；与 Ch78 的
  runtime contribution measurement 属于 `Layering / Dependency`，训练 credit 不等于线上责任归因。
- Unified-MAS 优化的是 reusable node/operator library，再交给已有 topology search；它与同周 workflow
  survey 的 template / realized graph / trace 边界互补，不能把 node synthesis 和 runtime graph mutation 合并。
- Omni-WorldBench 与通用 Evaluation System 是 `Principle Reuse`；本周只保留 metric-pipeline contract，
  不把自动指标排名或未公开的人类一致性结果写成通用 world-model 能力结论。
- UniGRPO 与 PEPO 同属 multimodal policy optimization，但不是重复候选：前者连接 discrete text action
  与 continuous flow action，后者在单一 token policy 内重分配 advantage；二者与同周 RLVR
  direction family 分别回答 action-space composition、modality-aware credit 与 causal update direction。
- PyTorch 2.11 的 differentiable collectives 是 communication semantics 进入 autograd/compiler graph 的
  `Layering / Dependency`；它不替代 NCCL/UCC 等 backend，也不保证任意 collective 都有相同 backward。
- Flight Recorder 连接 Ch32 的 collective ordering invariant 与 Ch64 的事件证据：timeout rank、最后执行
  operation 与 root-cause rank 可能不同，必须按 process group sequence 和 metadata 跨 rank 对齐。
- MXFP8+DeepEP 是 compute/communication co-optimization 的受限 integration evidence；MXFP8、DeepEP、
  grouped GEMM 与 generic All-to-All 的旧分支继续按 hardware、shape 与 topology 共存。
- Astrolabe code release 与 W12 paper 使用同一 Source Family；W13 只更新 access status，不复制论文评分。
- TurboQuant 与后续 quantized artifact 研究只能按 mechanism 和 executable support matrix 连接，
  不能按 bit-width 名称去重。
- MolmoWeb 的官方发布、论文、模型/data collection 与代码属于同一 Source Family：3 月 24 日是首次公开
  事件，4 月 9～10 日是 paper/code artifact evolution。`pass@k` 代表多次 rollout 的候选覆盖，best-of-N
  还依赖额外 judge；二者都不等于 deployable single-run reliability。visual-only、DOM/AxTree 与 API-based
  action 是 observation/action interface 的并存分支，不应按模型发布时间写成单向替代。
- vLLM MoE expert offloading 的 source family 从 W12 open PR 开始，W13 RFC 是 `Direct Refinement`；
  本周不重复评分。其 expert-weight cache 与 KV cache tiering 只共享 residency/eviction 原理，payload
  identity、reuse window 与 correctness contract 不同。
- `TRITON_MLA_SPARSE` 与 Hopper/Blackwell 上的 DeepGEMM、FlashMLA-Sparse 路径是 `Alternative
  Branches`：专用 kernel 在支持硬件上继续成立，Triton fallback 用维护、数值和性能验证成本换取 SM80/
  SM121 portability；它不是按发布时间替代专用 backend。
- DataFlex 与离线 data curation、固定 mixture、DoReMi/ODM 和 training-time reweighting 属于 `Direct
  Evolution + Layering / Dependency`：变化不是把静态数据策略判错，而是把 selector、mixer、weighter
  提升为可周期更新的 control-plane action。论文 first-public date 是 2026-03-27；repository 的项目起点
  是 2025-12-23、ZeRO-3 support 是 2026-03-17，三者是同一 Source Family 的不同演进节点，不能都记成
  W13 新事件。
- Ask or Assume 的 prompt reminder、hardcoded first-turn query 与 separate Intent Agent 是三条 clarification
  policy branch，不是“multi-agent 必然替代 single-agent”。v2 的 Kimi K2.6 增补是 post-window revision：它
  加强跨 backbone 证据，也暴露 over-query 与 tool-instruction failure，不能倒灌为 W13 已知实验事实。
- XpertBench 的 `2604.*` identifier 不决定 owner week；v1 submission timestamp 是 2026-03-27，故仍归 W13。
  v2～v4 只作为 revision drift 核验。ShotJudge 与 Ch62 的 rubric/evaluator family 去重，不能因为名称或模型
  榜单再计为一个新的 evaluation first principle。
- EpochX 与普通 task marketplace、Skill registry、durable workflow 和 Multi-Agent delegation 是
  `Layering / Dependency`，不是替代关系。它增加 credit-backed demand、parent-bounded subtask budget、
  acceptance-conditioned settlement 与 reuse reward；但旧的内部 Workflow 在单组织、固定 authority、无需
  市场定价时更简单可靠。官方 live platform 只证明可访问产品 surface，不能把 paper-level equations 当成
  已验证的 escrow、incentive equilibrium、fraud defense 或 programmable verification implementation。
- daVinci-LLM 与 DataFlex 属于同一 data-control Source Family 的不同层次：前者用受控 pretraining
  trajectory 观察 processing operator、data format 和 mixture 的 stage-dependent marginal value，后者提供
  runtime Select/Mix/Weight interface。二者都不推翻 offline curation 或 static mixture；当 workload 稳定、
  validation signal 稀缺或 reproducibility 优先时，静态策略仍合理。L0～L9 是 operator taxonomy，不是
  经验证的单调质量/自主性阶梯；论文的阶段配比也不得脱离 3.09B、8T-token 与 19-benchmark contract 复用。
- `Emergent Social Intelligence Risks` 与 Ch78 已记录的 correlated consensus、coordination failure 和
  topology repair 属于 `Layering / Dependency`：论文按 incentive、collective cognition、governance 与
  structural constraints 拆分 failure mechanism，却没有证明动态/多 Agent 架构必然失败。singleton、固定
  pipeline、broadcast debate 与 adaptive governance 是按 dependency、authority、resource 和 evidence
  independence 选择的并存分支；新 taxonomy 不覆盖旧拓扑成立条件。
- PRBench 与 paper QA、scientific subroutine benchmark、executable artifact evaluation 是 `Direct Evolution +
  Layering / Dependency`。end-to-end reproduction 增加 hidden reference、sandbox execution、numerical tolerance
  与 hard callback gate，却不淘汰便宜、可定位的 formula/unit tests；它与 Ch62 当前正文去重，不因 benchmark
  更新重复写入相同 evaluation first principle。
- MuSEAgent 与整条 trajectory retrieval 是 `Direct Evolution + Layering / Dependency`，不是替代关系。把
  trajectory 拆成 transition、生成 hindsight guidance 并按多 view 检索，可提高下一动作的局部相关性；完整
  trajectory 仍保留跨步因果上下文、原始证据与 replay。下一阶段压力是把 extractor/judge revision、derived
  memory provenance、supersession、delete、online invalidation 和 policy authority 纳入同一 memory contract。
- KAT-Coder-V2 的 Specialize-then-Unify 与单一 mixed-domain policy training 是并存分支：独立 experts 可在
  冲突 domain objective 下形成更强 teacher，但增加多套 checkpoint、rollout 与 routing/evaluation 成本；
  on-policy distillation 再用 unified student 自己访问到的 states 接收 expert supervision，减少 offline imitation
  的 exposure gap，却引入 teacher selection、cross-domain interference 与 distillation compute。turn-level
  objective、MCLA 和 Tree Training 属于这一训练 pipeline 的不同层，不应被合并成一个 benchmark 原因。

## Knowledge Tree Position

mSFT → Ch25（相邻 Ch24/26）；RLVR direction 与 Sparse but Critical → Ch29（相邻 Ch28/30）；
Scaling DoRA → Ch26，Ch45 只做 kernel/runtime handoff；CAID → Ch78（相邻 Ch77/80）；workflow
optimization taxonomy、SpecEyes 与 Unified-MAS → Ch77，Ch44/Ch62 只做 speculation/evaluation handoff；
depth recurrence → Ch17（相邻 Ch16/18）；CCPO → Ch29，Ch78 只做 role-credit handoff；Omni-WorldBench → Ch62；TurboQuant → Ch45 / Ch50；
UniGRPO 与 PEPO → Ch29，Ch23/27/62 只做 multimodal data、reward 与 evaluation handoff；
PyTorch 2.11 与 MXFP8+DeepEP → Ch32（Ch21/36/45 handoff）；Flight Recorder → Ch64（Ch32/65 handoff）；
CCV → Ch62；DSPA → Ch27（Ch5/68 handoff）；DRTriton → Ch45（Ch25/78 handoff）；
MolmoWeb → Ch23（Ch25/62/68/74/77 handoff）；
vLLM `TRITON_MLA_SPARSE` → Ch45（Ch46 handoff）；MoE expert offload RFC → W12 / Ch50 follow-up；
Trace2Skill → Ch80（Ch73/76/77 handoff）；Natural-Language Agent Harnesses → Ch77（Ch80/78/62 handoff）；
Density-aware Soft Context Compression → Ch22（Ch71/41 handoff）；
Learning to Commit → Ch73（Ch80/62 handoff）；
TAPS → Ch44（Ch42/41/55 handoff）；
DataFlex → Ch23（Ch24/35/56/62 handoff）；
Ask or Assume → Ch77（Ch78/75/62 handoff）；
XpertBench → Ch62；
EpochX → Ch80（Ch77/78/55 handoff）；
daVinci-LLM → Ch23（Ch24/25/56/62 handoff）；
Emergent Social Intelligence Risks → Ch78（Ch62/68 handoff）；
PRBench → Ch62（Ch61/63 handoff）；
MuSEAgent → Ch73（Ch72/74/76/62 handoff）；
KAT-Coder-V2 → Ch29（Ch36/56/77/62 handoff）；
LongCat-Next → Ch11（Ch12/21/29/34 handoff）；
Economic Index → Ch62 / Ch63；Meta 垂直模型 → Ch5。

## Recommended Action

W13 current-review queue 已清零，forward cursor 移至 W14。ClawKeeper 保留为 Unverified / Blocked
Backlog，Sommelier、SEAR、FIPO 保留为 W12 backlog，均不阻断 forward cursor 或污染本周。2026-08-13
external retry 没有产生可验证新增候选：这不是 discovery complete 的证据，而是 explicit coverage
limitation。W13 forward checkpoint 保持通过，broader Historical Evidence Gate 继续打开。当前 mSFT、
RLVR 两项互补研究、Scaling DoRA、CAID、
SpecEyes 与 workflow taxonomy 分别形成 Ch25、Ch29、Ch26、Ch78 与 Ch77 的 provisional
integrate/refine 候选；第三批的 depth recurrence、CCPO 与 Unified-MAS 继续作为 Ch17、Ch29、Ch77
的实验性候选；第四批 UniGRPO 与 PEPO 作为 Ch29 的两个不同机制分支；PyTorch 2.11 与 Flight
Recorder 分别作为 Ch32、Ch64 的 provisional refine/integrate 候选；MXFP8+DeepEP 已被现有章节原则
覆盖；DSPA 作为 Ch27 的 activation-intervention 新机制候选，DRTriton 作为 Ch45 executable-kernel
artifact lifecycle 的 refine 候选；MolmoWeb 作为 Ch23 的 observation/action/teacher/verifier lineage
refine 候选；Omni-WorldBench 只保留
evidence dispute；`TRITON_MLA_SPARSE` 作为 Ch45 hardware/backend portability 的 Experimental refine
候选，`Lie to Me` 作为 Ch62/68 已有 scorer/sensor 边界的实验性去重案例，MedOpenClaw 作为 Ch62
trajectory/evidence contract 的 Experimental refine 候选，MoE offload RFC 只更新 W12 source-family lineage。
Composer 2 暂定由 Ch29 拥有：它把 asynchronous rollout 的 policy identity 从单一 checkpoint
扩展到 token span、weight revision、MoE router path 与 environment snapshot；Ch36/56/71/77 只保留
communication、controller、sandbox 与 workflow handoff。该判断属于 versioned vendor evidence，不能把私有
CursorBench 或 vendor-reported benchmark 外推为通用 coding-agent 结论。
Hybrid Memory 暂定由 Ch10 拥有，以 `static scene reconstruction -> dynamic subject state continuation ->
query-conditioned memory retrieval` 细化 world-model memory；Ch14/22/62 只作机制与证据边界 handoff。
其合成数据、单一 1.3B base、作者 metric 与 partial training artifact 均要求保留 `Experimental` 状态。
Trace2Skill 暂定由 Ch80 拥有：把 raw trajectory、per-trace diagnostic patch、hierarchical merge、Skill
directory version 与 held-out evaluation 组成可治理 artifact lifecycle；Ch73、Ch76、Ch77 只分别连接
procedural memory、causal failure diagnosis 与 durable execution。它不替代在线 sequential edit、retrieval
memory 或 human-authored Skill，且工作论文、partial artifact、validation selection 与未解决的 patch/section
attribution 要求保持 `Experimental / Artifact Partially Reproducible`。
Natural-Language Agent Harnesses 暂定由 Ch77 拥有：把 controller bundle 拆为 portable pattern artifact、
shared semantic runtime 与 deterministic hooks，使 harness definition、run state 和 evaluator contract 可分别
版本化。Ch80/78/62 只连接 registry、delegation 与 EvalSpec。单 seed 小样本、runtime contamination、
prompt-length/salience confound、代码迁移中 substrate change 与 post-window partial artifact 要求保持
`Experimental / Artifact Partially Reproducible`，不能从 OSWorld 分数推出 natural language 优于 code。
Density-aware Soft Context Compression 暂定由 Ch22 拥有：把 density prediction、离散 ratio execution、
latent-token working set 与 decoder contract 分开，Ch71/41 只承接 Context identity 和 KV/runtime 效果。
summary-length proxy、短输入/synthetic training、substring scorer、无硬件/SLO/variance 与相关性而非因果消融
要求保持 `Experimental`；公开代码、数据和 LoRA weights 只说明 artifact available，不等于结论已独立复现。
Learning to Commit 暂定由 Ch73 拥有：把 chronological repository snapshot、Agent blind attempt、accepted
oracle diff、derived procedural Skill 与 future-task evidence 分开，Ch80/62 只承接 Skill artifact lifecycle 与
temporal EvalSpec。单一内部仓库、24/7 commits、synthetic issue、无公开 artifact、无 variance/cost 以及
LLM-judge/maintainer-merge gap 要求保持 `Experimental / Artifact Not Available`；严格时间切分只约束本文的
adaptation/evaluation pipeline，不被扩大为所有污染来源均已排除。
TAPS 暂定由 Ch44 拥有：把 draft checkpoint identity 从 architecture/target 继续扩展到 training distribution、
task family、temperature 与 composition policy，并区分 weight merge、confidence selection 与 merged-tree
verification。Ch42/41/55 只承接 batch/rollback state、KV transaction 与 registry lifecycle。论文只在单一
Llama-3-8B target、两个 domain、两种 draft backbone、四个 benchmark 和 4×A100 上报告 acceptance length；
未给出 production concurrency、precision、TTFT/P99/SLO 或完整 end-to-end cost，因此保持
`Experimental / Artifact Available`，不能把 merged-tree acceptance headline 当作 serving speedup。
DataFlex 暂定由 Ch23 拥有：把 Select、Mix、Weight 三类 data action 与 embedding/inference/loss/gradient/
validation signals、更新 cadence、cache 和 distributed-state access 分开，Ch24/35/56/62 只承接 trajectory
identity、ZeRO ownership、Training Operator 与 evaluation-leakage handoff。项目首次公开于 2025-12-23，
本周记录的是 2026-03-27 paper evidence；作者实验只覆盖指定 Open-Hermes/SlimPajama、Mistral/Llama/Qwen、
LoRA/one-epoch 或 6B/30B-token contracts，且无多 seed/variance。故保持 `Experimental / Artifact Available`，
不把动态策略或多卡 headline 外推为静态 data curation 已失效或通用训练加速。
Ask or Assume 暂定由 Ch77 拥有：把 clarification 从静态 prompt 变成每轮读取 state history 的 uncertainty
gate，并把 Intent Agent 的 binary decision、Main Agent action constraint 与 user reply 作为独立 workflow
events；Ch78/75/62 只连接职责分解、belief update 与 interactive EvalSpec。v1 的 Claude Sonnet 4.5 +
GPT-5.1 simulated user、synthetic underspecification、single run、API cost 与 v2 Kimi 过度询问要求保持
`Experimental / Artifact Available`；不能从 resolve rate 推出真实用户环境或高风险任务的可靠 calibration。
XpertBench 归 Ch62 去重：expert task/rubric construction、criterion-level judge、human calibration 与 weighted
aggregation 已由现有正文的 scorer ladder 和 rubric formation/execution/ranking/decision 分层覆盖。它只作为
`No Change — Already Covered (Experimental; Artifact Not Available)` 案例；245-task Gold subset、52% CDR、
未披露 alignment sample/variance/abstention、空的公开 dataset 与 vendor model rankings 不形成 Books 新机制。
EpochX 归 Ch80 去重：task/run identity、typed delivery、Skill provenance/dependency、validation admission、
bounded delegation 与 evidence graph 已分别由 Ch77/78/80 覆盖；Ch55 只提供通用 registry identity handoff。
论文新增的 credits/market layer 目前只有 case-based evidence，没有公开 implementation、transaction traces、
longitudinal reuse、competition/incentive、fraud/collusion、dispute/refund 或 identity/reputation contract，故暂定
`No Change — Already Covered (Experimental Case; Platform Accessible; Implementation Not Disclosed)`，不把
“acceptance”写成 correctness proof，也不把 credits equation 写成已验证经济机制。
daVinci-LLM 暂定由 Ch23 拥有：把 acquisition/normalization/filtering、generative refinement、cognitive/
context completion 与 environment/ecosystem/world synthesis 视为不同 data operators，并把 operator、mixture、
checkpoint 与 evaluation revision 共同写入 training trajectory identity。Ch24/25/56/62 只承接 pretraining/
SFT transition、operator checkpoint 与 evaluation handoff。3.09B/Qwen2、BF16、4096 context、8T tokens、
单项目 19-benchmark trajectory、无 hardware/compute/seeds/variance，以及 current repository/data subset 与
“fully open”声明的差距，要求保持 `Experimental / Artifact Partially Available`；不把 stage-specific ratio、
PPL/generative ranking 或 Data Darwinism 层级外推为通用配方或单调进化律。
`Emergent Social Intelligence Risks` 暂定由 Ch78 拥有：把局部 utility、communication topology、information
partition、aggregation、shared-resource rule 与 arbitration/replanning 共同纳入 collective risk contract；
Ch62/68 只承接 risk indicator、judge calibration 与 security threat model。15 类 synthetic scenarios、不同
backbone/trial/judge、无统一 sampling/variance、无真实部署对照和无公开 artifact 要求保持 `Experimental /
Artifact Not Available`；不把作者的 risk occurrence 写成生产发生率，也不把 mitigation 建议写成已验证控制。
PRBench 归 Ch62 去重：task/dataset/environment/scorer/run/decision identity、executable verifier boundary、
rubric 分层和 hard gate 已由现有正文覆盖。该论文作为 scientific reproduction 的强案例保留为 `No Change —
Already Covered (Experimental; Artifact Partially Available)`；30-task 聚合结果缺少完整公开 artifact、judge/
sampling/cost contract，不能成为模型或 Agent framework 的通用能力排名。
MuSEAgent 暂定由 Ch73 拥有：把 raw trajectory、atomic transition、hindsight score/guidance、multi-view index、
retrieval decision 与下一 action 分开，Ch72/74/76/62 只承接检索、工具执行、反思与 evaluation handoff。四个
多选 VQA 的 1:1 exploration/evaluation split、未披露 hardware/latency/cost/multi-seed variance，以及 GPT-4o
hindsight 同时拥有过滤和 guidance 生成权，要求保持 `Experimental / Artifact Available`；代码公开不等于
provenance、supersession、delete、online invalidation 或 policy authority 已得到解决。
KAT-Coder-V2 暂定由 Ch29 拥有：把 Agent RL sample identity 明确为 environment/tool/scaffold/task/verifier
五元组，并把 turn-level ratio、MoE logprob estimator、tree-shaped trajectory training 与 expert-to-unified
on-policy distillation 分层；Ch36/56/77/62 只承接 GPU/runtime、training workload、workflow 与 verifier
handoff。sole-v1 vendor report 没有披露 model architecture、训练 hardware/precision、完整 hyperparameters、
seeds/variance、关键 ablation 或 KwaiEnv/KRL implementation，因此保持 `Experimental / Implementation Not
Disclosed`；hosted API 可访问不等于模型权重和训练系统公开，也不把 vendor benchmark 或 6.2× 写成通用结论。
Historical Books Gate 保持关闭，不根据当前批次或单一厂商发布提前改写 Books。
LongCat-Next 暂定由 Ch11 拥有：把 tokenizer 从 text vocabulary 延伸为可版本化的 multimodal discrete
protocol，显式分离 modality tokenizer/detokenizer、hierarchical residual code、shared autoregressive
backbone 与 modality-specific output head；Ch12/21/29/34 只承接 representation、MoE routing、RL
train/inference mismatch 与 VHalf pipeline handoff。其 discrete/continuous 对照、emergent routing 与 VHalf
结果只在作者训练和 benchmark contract 内成立；未披露训练 GPU/topology/cost/variance，完整 pretraining
pipeline 也不可复现，因此保持 `Experimental / Artifact Partially Reproducible`。旧的 continuous feature
projection 在数据少、只需理解或 fidelity/latency 更优时仍成立，specialized modality path 也不被统一
backbone 静默覆盖。

## Event-Date Daily Decision

2026-03-24、03-26、03-27、03-28：Weekly only。

## Books Integration Decision

`Complete — W13 Source-Family Books Gate`。本段后续的“暂定”清单保留 Source Review 阶段的章节判断，
最终 owner、current/legacy chapter、disposition 与实际变更以文末 2026-08-14 Final Ledger 为准。旧版
TurboQuant `No change` 仅在其 dispute boundary 内保留；41 个 scored
`20+` candidates 均已完成章节定位和 existing-coverage review，其中 DSPA 暂定 `Integrate — New
Mechanism`，DRTriton、MolmoWeb 与 `TRITON_MLA_SPARSE` 暂定 `Refine — Existing Argument
(Experimental)`；MedOpenClaw 暂定 `Refine — Existing Argument (Experimental; Artifact Partially
Verified)`；`Lie to Me` 暂定 `No Change — Already Covered (Experimental Evaluation Case)`；Composer 2
暂定 `Refine — Existing Argument (Ch29; Versioned Vendor Evidence)`；Hybrid Memory 暂定 `Refine —
Existing Argument (Ch10; Experimental; Artifact Partially Reproducible)`；Trace2Skill 暂定 `Refine —
Existing Argument (Ch80; Experimental; Artifact Partially Reproducible)`；Natural-Language Agent Harnesses
暂定 `Refine — Existing Argument (Ch77; Experimental; Artifact Partially Reproducible)`；Density-aware Soft
Context Compression 暂定 `Refine — Existing Argument (Ch22; Experimental; Artifact Available)`；Learning to
Commit 暂定 `Refine — Existing Argument (Ch73; Experimental; Artifact Not Available)`；TAPS 暂定
`Refine — Existing Argument (Ch44; Experimental; Artifact Available)`；DataFlex 暂定 `Refine — Existing
Argument (Ch23; Experimental; Artifact Available)`；Ask or Assume 暂定 `Refine — Existing Argument
(Ch77; Experimental; Artifact Available)`；XpertBench 暂定 `No Change — Already Covered (Ch62;
Experimental; Artifact Not Available)`；EpochX 暂定 `No Change — Already Covered (Ch80; Experimental
Case; Platform Accessible; Implementation Not Disclosed)`；daVinci-LLM 暂定 `Refine — Existing Argument
(Ch23; Experimental; Artifact Partially Available)`；`Emergent Social Intelligence Risks` 暂定 `Refine —
Existing Argument (Ch78; Experimental; Artifact Not Available)`；PRBench 暂定 `No Change — Already Covered
(Ch62; Experimental; Artifact Partially Available)`；MuSEAgent 暂定 `Refine — Existing Argument (Ch73;
Experimental; Artifact Available)`；KAT-Coder-V2 暂定 `Integrate — New Mechanism (Ch29; Experimental;
Implementation Not Disclosed)`；LongCat-Next 暂定 `Integrate — New Mechanism (Ch11;
Experimental; Artifact Partially Reproducible)`。当前没有 unscored review pending；ClawKeeper 为 1 个
unscored blocked backlog。ClawKeeper 按已批准 blocked-skip 规则不进入 Books；它与 broader discovery
limitation 只保持 Archive Completion Gate Open，不再把已验证的 W13 Source Families 阻塞在 Books 外。

## Ignored Noise

不含 kernel、quality 与 workload 条件的压缩倍数。

## 2026-07-31 Full Re-Audit Addendum

- TurboQuant 已升级全文复核：原论文首次公开于 2025 年，且 2026 年出现独立 reproduction
  critique。当前状态改为 `Disputed / 尚未验证`，在 artifact 与实验条件对齐前不写 Books。
- Economic Index learning curves 继续作为 measurement state，不外推为通用学习规律。
- 详细证据冲突与开放问题保留在本 Weekly。

## Full Source Review

### Lie to Me: CoT Faithfulness across Open Reasoning Models — 25/30

- **Source Family / Metadata / Access**：`OPEN-REASONING-COT-FAITHFULNESS`；arXiv:2603.22582 v1，
  first-public 2026-03-23，当前无后续 revision。已读 Abstract、Introduction、Related Work、Methods、
  全部实验与 discussion、limitations、Appendix A～G，并核对作者 repository 与 Hugging Face dataset。
  代码、prompt、原始输出与 annotations 可访问；checkpoint/runtime 由 OpenRouter provider 托管，未公开
  本地 checkpoint pin、量化与 provider-side optimization，记为 `Not Disclosed`。
- **Original Problem / Previous Design / Changed Constraint**：只看 final answer 无法判断模型是否因提示中的
  非任务相关线索改变答案；用单一 closed model 或单一 judge 研究 CoT 又会把 model family、provider、
  classifier 与 hint design 混在一起。旧的 final-answer evaluation 对 release regression 仍合理，但无法回答
  “答案被 hint 影响时，reasoning surface 是否承认该影响”。候选把模型范围扩展到 12 个 open-weight
  reasoning models / 9 个 families，并把 influence 与 verbalized acknowledgment 分开测量。
- **Mechanism / State Ownership / Control and Data Flow**：evaluation controller 对每道题先运行 baseline，再运行
  sycophancy、consistency、visual pattern、metadata、grader hacking 与 unethical-information 六类 target hint。
  只有 baseline answer 改为 target answer 的 case 才进入 faithfulness denominator；run identity 包含 model/provider、
  prompt/hint、temperature `0.0`、seed `103`、token budget、parser 与 judge version。主分析由 Claude Sonnet
  judge 判定，另一个 two-stage pipeline 先做 regex，再对未决样本做三 judge majority。数据流是
  `question + hint -> provider inference -> answer parser -> influenced-case filter -> acknowledgment classifier -> aggregate`；
  classifier 而不是被测模型拥有最终 faithfulness label。
- **Implementation / Evaluation Contract**：498 道 MCQ（300 MMLU、198 GPQA Diamond）、41,832 次 inference、
  10,276 个 influenced cases；OpenRouter `max_tokens=32768`、reasoning budget 至多 16,384、timeout 300 秒、
  5 次 retry。baseline extraction failure 按模型有 0～58 次，失败样本从 accuracy denominator 排除。
  primary Sonnet judge 对 thinking 做 8,000 字符 middle truncation；secondary pipeline 的 judge input 只保留
  4,000 字符。论文报告 Sonnet micro faithfulness 69.7%、pipeline 82.6%，sycophancy 与 consistency 的
  classifier 差异分别达 43.4 与 33.1 个百分点；micro 与 macro aggregation 也不能互换。
- **What the Evidence Proves / Does Not Prove**：证据支持“在这组 MCQ、hint、provider 与 classifier contract
  下，多数被 hint 改变的回答在生成的 thinking text 中出现某种 acknowledgment，且测量结果对 classifier
  高度敏感”。它不证明 thinking text 是内部 computation 的忠实读出，不证明 acknowledgment 导致答案改变，
  不证明 open-weight models 普遍比 closed models 更可监控，也不支持从 family/training-method 相关性推断因果。
  对 DeepSeek-R1 的先前结果差异同时混入 hint 明显度、API/model revision 与 classifier 变化，不是干净 replication。
- **Limitations / Threats / Trade-offs / New Failure Modes**：MCQ、固定 target answer 与显式 hint 提供了可重复
  contract，却不覆盖 open-ended code、长时 Agent 或真实欺骗；MMLU label error、answer parse exclusion、
  visual-pattern 无文字 hint、judge truncation、同源 model-judge bias 与 provider drift 都会改变 numerator 或
  denominator。多 judge/regex pipeline 可提高吞吐并给出另一测量视角，却新增 rule drift、correlated error 与
  aggregation policy。模型显式提到 hint 也可能只是表面 token pattern，不能解释为“内部识别后主动压制”。
- **Where Previous Designs Still Apply / Evolution**：确定性 answer checker 仍适合测 objective correctness；
  human annotation 与 executable outcome verifier 仍是关键 slice 的校准来源；CoT monitor 只能作为附加 sensor。
  演进关系是 `outcome-only evaluation -> influenced-case counterfactual -> surface acknowledgment classifier ->
  classifier disagreement and provenance audit`，属于 `Layering / Dependency`，不是以 CoT judge 替代 outcome gate。
- **ROADMAP / Adjacent Chapters / Existing Coverage / Disposition**：已读 Ch62 及 Ch68 的相关段落，并核对
  Ch67/69 handoff。Ch62 已要求版本化 subject/dataset/environment/scorer、保存 disagreement 并避免 model judge
  充当 truth；Ch68 已明确区分 controllability、monitorability、faithfulness 与 outcome safety，并把 CoT
  monitor 定义为 policy-bound sensor。因此本项没有新增长期机制：`No Change — Already Covered
  (Experimental Evaluation Case; Historical Books Gate Closed)`。不修改 Books。

### MedOpenClaw / MedFlow-Bench: Auditable Full-Study Imaging Workflows — 29/30

- **Source Family / Metadata / Revision / Access**：`MEDOPENCLAW-MEDFLOWBENCH`；arXiv:2603.24649
  v1 first-public 2026-03-25，v2 于 2026-05-13 扩展为 radiology + pathology、5 task families 与更完整
  runtime/failure/evaluation disclosure。本周事件只属于 v1；v2 用于验证机制演进，不回写事件日期。已读
  Introduction、Related Work、runtime、benchmark design、全部 experiments、failure analysis、limitations、
  operation-budget study、prompt/tool schema、license appendix，并核对项目页与公开 GitHub。项目页的
  `Code` 链接当前指向静态网站仓库，未定位到论文所述 runtime/evaluation implementation，故标记
  `Artifact Partially Verified / Runtime Code Not Located`，不把“released artifact”视为复现通过。
- **Original Problem / Previous Design / Changed Constraint**：pre-selected 2D slice/crop benchmark 能低成本
  测视觉识别与医学知识，仍是合理的局部能力测试；但它替 agent 完成了 study search、series selection、
  cross-slice/timepoint comparison 与 evidence capture，无法测完整软件工作流。约束变为处理完整 3D volume
  或 whole-slide image，并且答案必须绑定可重放、可确定核验的 slices、RAS/WSI coordinates、ROI、mask、
  lesion-state fields 与 viewer state。
- **Mechanism / State Ownership / Control and Data Flow**：MedOpenClaw 位于 backbone VLM 与 3D Slicer/
  QuPath 之间，通过 documented REST endpoint 与 named bridge handler 暴露三类 action：Viewer Control、
  Evidence Capture、Analysis Operator。raw Python/Groovy 不向 agent 开放；runtime 拥有 action schema、
  permission boundary、每次调用的 arguments、resulting viewer snapshot 与 derived artifact，agent 只提出
  typed action。episode 流是 `full study + task -> bounded action loop -> persistent viewer/derived state ->
  structured answer + evidence -> hidden-reference deterministic checks`，不以自由文本 rationale 充当证据。
- **Implementation / Evaluation Contract**：v2 公开 5 个 task families、1,459 个 eligible cases：139 个
  longitudinal MRI、495 个 brain MRI、162 个 lung PET/CT、113 个 BRACS WSI、550 个 CAMELYON17 WSI。
  Track A 只允许 viewer-native action；Track B 加入 segmentation、registration 与 MONAI/VISTA3D；Track C
  可绕过 runtime，但必须输出相同 canonical answer/evidence schema。每轮至多 20 次 tool calls；Task 测
  answer，Strict 只有 answer 与 module-specific evidence gate 同时通过才给分，Localization 检查 RAS/WSI
  point 是否落入 hidden mask/annotation。论文未披露统一 inference temperature、seed、硬件、延迟、成本与
  SLO，均记为 `Not Disclosed`；因此不外推任何绝对模型排名或生产吞吐结论。
- **What the Evidence Proves / Does Not Prove**：结果支持“在这些公开数据、viewer、prompt、20-round budget、
  model revision 与 deterministic scorer 下，answer-only 会高估复杂 workflow competence；增加 advanced
  operation 不会自动消除 state/evidence grounding bottleneck”。它不证明工具普遍降低模型能力，不证明
  3D Slicer/QuPath contract 可代表临床部署，也不证明 hidden public-dataset labels 等价于临床 adjudication。
  Track B 的局部升降依赖 task/backbone/operator；operation-budget 表也非单调，不能解释为更多或更少 tool
  calls 的普遍最优值。
- **Baselines / Ablation / Sensitivity / Failure Modes**：论文比较 viewer-native、2D slice montage、native 3D
  VLM 与 advanced-operation branches，并给出 operation-budget control。最有系统意义的是可审计 failure
  taxonomy：workflow objective drift；由弱 2D box 伪提升为毫米级测量；transform、volume、viewer layer 与
  rationale 的 state misbinding；丢弃较好 segmentation 后用错误 seed 形成 self-confirming artifact；以及
  相同 case/prompt 下 registration 仅 3/10 runs 完成 `register -> resample/apply -> fusion verify` 的程序性不稳定。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：bounded named tools 减少 attack
  surface、提高 replayability，却牺牲开放脚本的灵活性并把 schema coverage、bridge compatibility、coordinate
  convention 与 viewer revision 变成系统依赖。deterministic Strict gate 可审计，但可能继承 mask/annotation
  与 parser bias；完整 study interaction 更真实，却显著增加运行成本、state space 与数据许可约束。
  static 2D benchmark 仍适合廉价 perception regression；成熟 deterministic image pipeline 仍应直接执行，
  不必强行交给 Agent；高风险临床结论仍需 clinician authority。
- **Evolution / ROADMAP / Adjacent Chapters / Disposition**：演进是 `selected-image answer -> full-study search ->
  bounded professional-tool actions -> persistent viewer/derived-artifact state -> deterministic answer+evidence gate ->
  replay and failure localization`，属于 `Layering / Dependency`，不是用 Agent 取代传统影像软件。已读 Ch62、
  Ch74、Ch77、Ch80 相关段落：Ch74 已拥有 typed intent / trusted executor，Ch77 已拥有 durable state 与
  verification，Ch80 已拥有 Agent evidence plane；Ch62 已区分 narrative、action、environment transition 与
  completion evidence，但尚未用“专业软件的 state/artifact misbinding”解释为什么 tool access 不等于 workflow
  competence。暂定 `Refine — Existing Argument (Ch62 owner; Ch74/77/80 handoff; Experimental;
  Artifact Partially Verified; Historical Books Gate Closed)`。本轮不修改 Books。

### Composer 2: Domain-Matched Asynchronous Coding-Agent RL — 29/30

- **Source Family / Metadata / Revision / Access**：`COMPOSER2-ASYNC-MOE-AGENT-RL`；arXiv:2603.24477
  v1 first-public 2026-03-25，v2 于 2026-03-26 修订；Cursor official technical report 发布于 2026-03-27。
  本周事件由 v1 与官方报告共同界定。已读 Introduction、continued pretraining、MTP、RL algorithm、
  infrastructure、MoE/parallelism、evaluation、limitations 与关键 appendices，并联读官方 technical report。
  模型以 Kimi K2.5（1.04T parameters / 32B active）为 base；训练 tokens、learning rate、batch、RL group
  size、GPU 数量、duration、总成本与私有 benchmark case-level artifact 均为 `Not Disclosed`。
- **Original Problem / Previous Design / Changed Constraint**：同步 on-policy RL 用固定 policy 生成完整
  trajectory，再在一致 checkpoint 上训练，provenance 清晰、debug 简单；但 coding Agent 的长时 tool loop、
  sandbox 执行、group sampling 与训练更新延迟会让 accelerator 等待 rollout。把 trainer 与 rollout 完全异步
  能提高利用率，却使同一条 trajectory 可能跨越 weight hotload；MoE 还让 token distribution 同时依赖
  sampling weights 与 data-dependent expert route，单一 checkpoint ID 不再完整描述行为策略。
- **Mechanism / State Ownership / Control and Data Flow**：系统拆成 training、environment、inference、
  evaluation 四个服务；central reconciler 用 slot 管理 sample lifecycle。environment snapshot 保存到
  filesystem/memory，group checkpoint 把 sequences、advantages 与 policy versions 写入 NFS；Ray object store
  承载对象并可 spill 到 NVMe。rollout 中允许 in-flight weight update，因此后半段 tokens 可由更新后的 policy
  生成。为减轻 MoE 的 trainer/inference route mismatch，inference 返回每 token/layer 的 expert indices；trainer
  replay route，若原 expert 在当前 logits 下低于 local top-k plausibility threshold 才替换。完整数据流是
  `prompt -> sandbox snapshot -> asynchronous rollout + route log -> group reward/advantage -> checkpointed sample ->
  trainer replay/update -> sharded delta weight publish -> inference hotload`。
- **Training / Parallelism / Numeric Contract**：continued pretraining 以 CP 为主要 long-context 轴，并将 EP 与
  TP 解耦：报告给出 EP=8/CP=2，RL 为 EP=8/CP=8；KV latents local compute 后 all-gather，small projection
  replicated，并以 paired chunks 做 causal load balancing。DeepEP 承担 dispatch/combine；dispatch 前 token
  用 MXFP8，combine 回 BF16，并以 microbatch/stream overlap 隐藏通信。forward 使用 FP4E2M1、16-element
  FP8E4M3 block scale 与 FP32 per-token scale；backward 用 MXFP8。作者报告 per-tensor scale 以及 NVFP4
  fast approximate division 曾导致 RL divergence，说明低精度 recipe 是 optimizer/runtime contract，不是
  可替换的 kernel flag。
- **RL Objective / Evaluation Contract**：每 prompt 固定 group size、多 samples、single epoch、full-parameter
  update；不做 length standardization、group-advantage standard-deviation normalization 或 overlong masking。
  使用 k1 KL estimator，并用 self-summary 串联超长 generation，将 final reward 赋给整条 chain；另加入
  behavior rewards 与 concave-down length penalties。官方报告列出 CursorBench 61.3、SWE-bench Multilingual
  73.7、Terminal-Bench 61.7，但 CursorBench 来自内部 sessions、task count/rubric/raw outputs/variance 未公开，
  其他行还混合自有 harness 与 self-reported/leaderboard 结果。它们只能作为 versioned vendor evidence，
  不能比较为跨模型通用能力排序。
- **What the Evidence Proves / Does Not Prove**：公开材料证明这一实现把异步 rollout、mid-trajectory weight
  revision、MoE route replay、sandbox snapshot、sample checkpoint 与跨服务 weight distribution 作为同一训练
  系统处理，并披露了若干 numerical-divergence failure。它不证明 in-flight weight update 保持严格 on-policy，
  不证明 route replay 消除了全部 policy mismatch，也不证明这些 precision/parallel choices 对其他硬件、模型、
  tool environment 或 SLO 最优。私有 benchmark 不能证明 production reliability、成本或 general agent autonomy。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：异步解耦减少 trainer idle，却新增
  stale sample、跨 token policy drift、route-log storage、sample supersession、weight rollout failure 与恢复一致性；
  snapshot/checkpoint 提高可恢复性，却放大 NFS/object-store/VM lifecycle 与 egress policy 的控制面压力。
  同步 frozen-policy rollout 在短 trajectory、严格 reproducibility、规模较小或 verifier 成本低时仍更合理；
  dense model 或可容忍 route drift 时也不必支付 expert-path replay 成本。
- **Evolution / ROADMAP / Adjacent Chapters / Disposition**：演进为 `frozen-policy trajectory -> decoupled async
  rollout -> in-flight weight revision -> MoE route-aware replay -> snapshot/checkpointed sample lifecycle`，属于
  `Direct Evolution + Layering / Dependency`。已读 Ch29 及 Ch28/30，并核对 Ch36、Ch56、Ch71、Ch77：Ch29
  已覆盖 policy lag、partial rollout 与 trajectory lifecycle，但未把 MoE router path 和 token-span weight
  revision 纳入 sampling provenance。暂定 `Refine — Existing Argument (Ch29 owner; Ch36/56/71/77 handoff;
  Versioned Vendor Evidence; Historical Books Gate Closed)`。长期可吸收的不是厂商分数，而是 trajectory
  identity 可能需要联合记录 `token span + sampling weight revision + router path + logprob + environment snapshot
  + verifier version`；本轮不修改 Books。

### ClawKeeper — Unverified / Blocked Backlog

- **Located identity / Access attempts**：curation ledger 给出 `arXiv:2603.24414` 与 provisional first-public
  date 2026-03-25。2026-08-12 依次尝试 arXiv abstract、HTML、站内/互联网检索、export API 与可视浏览入口，
  均未获得可核验 metadata、abstract 或正文；本地仓库也只有 W13/W14 两处待审计 identity。
- **Evidence boundary / Decision**：未确认题名、作者、版本历史、Source Family、机制、实验、代码、评分或
  ROADMAP owner；不依据名称 `ClawKeeper` 推断 security、agent runtime 或 governance 机制。状态为
  `Unverified / Blocked Backlog — Unscored`。按用户批准的 forward-cursor 规则暂时跳过；primary source
  可访问后必须从 metadata 开始重审，不能把本条当作 Full Source Review 或 Books 证据。
- **Post-forward retry（2026-08-12）**：再次按精确 arXiv ID、候选名与 Hugging Face paper path 检索，
  仍未返回可核验 primary metadata 或正文。W13 backlog retry checkpoint 因而完成但 blocker 未解除；不新增
  score、owner 或 disposition，post-forward sweep 转入 W14。

### Hybrid Memory / HyDRA for Dynamic Video World Models — 26/30

- **Source Family / Metadata / Revision / Access**：`HYDRA-DYNAMIC-VIDEO-WORLD-MEMORY`；论文
  “Out of Sight but Not Out of Mind: Hybrid Memory for Dynamic Video World Models”，arXiv:2603.25716
  v1 first-public 2026-03-26。已读完整 paper、supplement、公式、dataset construction、main evaluation、
  ablation、limitations，并核对作者 project page、GitHub、Hugging Face model/dataset identity。repository
  公开 inference、checkpoint、DSC evaluator 与 training skeleton；内置 dataset loader / end-to-end trainer
  loop 并未随 skeleton 提供，故为 `Artifact Partially Reproducible`，不是完整 reproduction。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：FOV overlap、surfel-indexed
  memory、uniform compression 或 nearby context window 面向静态场景与 viewpoint revisit 时，按 camera geometry
  找历史帧成本低、解释清晰；但动态主体离开视野后，camera ego-motion 与 subject motion 分离，旧位置附近的
  frame 可能只有空背景。新的 contract 不仅要重建 static background，还要在没有直接 observation 的区间持续
  保存 subject identity、appearance 与 motion state，并在 re-entry 时选择与当前 query 有关的历史 evidence。
- **Mechanism / State Ownership / Control and Data Flow**：Wan2.1-T2V-1.3B base 以 causal 3D VAE 编码 context，
  Flow-Matching DiT 生成 target；camera pose 经 MLP broadcast 到 latent。3D-convolution Memory Tokenizer 用
  `2×4×4` kernel 把历史 latent 压为含 temporal interaction 的 memory tokens。每个 target latent query 先做
  spatial pooling，再与每个 temporal memory-key slice 计算 affinity；runtime 选择 top-k（主设置 10）memory
  tokens，并强制拼接 target 的 local temporal window（主设置 5）后执行 attention。memory tokens/keys/values、
  target queries、top-k indices、camera condition 与 local window 是模型内部 state；它们没有 Agent Memory 的
  provenance、authorization、跨会话持久化或删除语义。
- **Dataset / Implementation / Evaluation Contract**：HM-World 由 Unreal Engine 5 程序化构造，含 59,225
  clips、17 scenes、49 subjects、10 subject paths、28 camera trajectories，并保存 camera pose、per-frame
  subject position 与 exit/entry timestamps。主模型读取 77 context frames，3D VAE temporal downsample 4×；
  训练 10K iterations、32 GPUs、global batch 32。作者未披露 GPU 型号、precision、optimizer、learning-rate、
  seed/variance、video resolution、wall-clock 或 cost，均为 `Not Disclosed`。test set 为 1,000 个训练未见
  scene/subject samples，但仍来自同一 synthetic generation family。
- **Baselines / Ablations / Scorer Boundary**：baseline、DFoT 与 Context-as-Memory 在相同训练配置下比较；
  WorldPlay 是 zero-shot commercial baseline，存在明确 domain/finetuning mismatch，不能用于通用 superiority
  结论。指标含 PSNR/SSIM/LPIPS、VBench Subject/Background Consistency，以及作者 DSC：YOLOv11 定位主体，
  CLIP feature similarity 分别对 ground truth 与 context 聚合。作者 ablation 支持 temporal tokenizer kernel
  优于无 temporal interaction、10/15 retrieved tokens 优于 5、learned affinity 优于 FOV overlap；但 detector、
  tracker、CLIP 与 spatial/temporal normalization 同样是 scorer state，未见 human calibration 或 metric variance。
- **What the Evidence Proves / Does Not Prove**：证据支持在这一 synthetic dataset、1.3B base、training contract
  与 scorer pipeline 下，compressed spatiotemporal tokens + query-conditioned retrieval 比被测 fixed geometric/
  neighbor retrieval 更能保持 exit/re-entry subject consistency，并说明“历史可访问”与“动态状态连续”不是同一
  能力。它不证明模型在 occluded interval 中学习了真实物理因果或精确 trajectory，不证明对自然视频、interactive
  action、robotics 或多主体开放世界泛化，也不证明作者 DSC 等价于 human-perceived motion correctness。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：tokenization 与 top-k 降低全量历史
  attention 的计算和噪声，却会因压缩丢失 detail、错误 affinity 漏掉关键主体、hard selection 造成不可恢复
  evidence loss；dynamic retrieval 还把 selection 随 denoising step/layer 变化引入可观测性与 debug 难题。
  作者明确报告三人以上复杂场景或 severe occlusion 时退化。静态场景、短 horizon、可靠 camera geometry 或
  强审计需求下，FOV/surfel/raw frame memory 仍可能更简单、可解释；local window 仍负责短时 denoising stability。
- **Evolution / ROADMAP / Adjacent Chapters / Disposition**：演进为 `static viewpoint-indexed memory -> compressed
  spatiotemporal tokens -> query-conditioned dynamic retrieval -> static background + latent subject-state continuity`，
  属于 `Direct Evolution + Principle Reuse`。已读 Ch9/10，并联读 Ch14、Ch22 与 Ch62：Ch10 已把 world model
  写成 latent dynamics + memory + feedback，却未拆开 static reconstruction 与 out-of-view dynamic-state continuation；
  Ch14 拥有 content-dependent routing，Ch22 拥有 model-internal memory / retrieval 的状态边界，Ch62 拥有
  scorer pipeline。暂定 `Refine — Existing Argument (Ch10 owner; Ch14/22/62 handoff; Experimental;
  Artifact Partially Reproducible; Historical Books Gate Closed)`。本轮不修改 Books。

### Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills — 27/30

- **Source Family / Metadata / Revision / Access**：`TRACE-TO-DECLARATIVE-SKILL-COMPILATION`；
  arXiv:2603.25158 v1 first-public 2026-03-26，v1 明示 `Work in progress`；当前 v5（2026-06-04）与
  author list/content revision 只用于核对后续演进，不改写 W13 event date。已读 v1 metadata、Introduction、
  formalization、三阶段方法、全部 spreadsheet/math/DocVQA experiments、parallel/sequential 与 retrieval/error-
  analyst ablations、qualitative analysis、related work、limitations、关键 appendix，并核对官方 repository。
  repository 公开 spreadsheet trajectory/evolution/evaluation pipeline、released skills 与分析脚本，没有 release/tag；
  paper 的 math 与 VQA pipeline 未完整公开，且 README 明示长 ReAct 和 LLM edit 即使固定 seed 也难精确复现，
  故为 `Artifact Partially Reproducible`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：human-authored Skill 在
  domain 边界稳定、可人工校验时提供高质量先验；online sequential edit 在 trace 少、反馈即时且环境持续变化时
  可以快速适配；per-episode retrieval memory 则保留细粒度 provenance，并按 query 选择经验。规模扩大后，
  单条轨迹顺序写入会产生 order dependence 与 context drift，窄 Skill 集合会碎片化，纯 parametric 生成又缺少
  target-domain failure evidence。新约束是：如何在不更新模型参数、没有更强 teacher 的情况下，把大量成功/失败
  轨迹压缩为 bounded、portable、可直接加载的 declarative artifact，同时避免最新或偶然样本支配最终规则。
- **Mechanism / State Ownership / Control and Data Flow**：Skill `S=(SKILL.md, resources)` 由 artifact layer
  持有，模型 policy 固定。Stage 1 在 `D_evolve` 生成包含 reasoning/tool/observation/outcome 的 ReAct traces；
  Stage 2 让每个 analyst 读取同一 frozen `S0` 与单条 trajectory，成功轨迹使用 single-pass pattern extraction，
  失败轨迹使用可读文件、对照 ground truth、验证修复的多轮 ReAct diagnosis，无可验证 causal diagnosis 就丢弃。
  Stage 3 按 merge fan-in 分层归并 patch pool：LLM 负责去重、冲突解释与归纳，programmatic guard 拒绝不存在
  文件、扣留同一行区间冲突并执行格式校验；高频规则进入主 Skill，低支持 edge cases 进入 `references/`。
  最终 `S*` 作为 immutable/versioned candidate 进入 held-out evaluation，而不是把轨迹直接写入 runtime policy。
- **Implementation / Evaluation Contract**：主 spreadsheet contract 使用 Qwen3.5-122B-A10B 与
  Qwen3.5-35B-A3B、vLLM recommended generation config、SpreadsheetBench-Verified 200 evolve/200 held-out、
  full SpreadsheetBench Soft/Hard、转换成 xlsx 的 WikiTableQuestions OOD；每题 1 trajectory、128 analysts、
  merge batch 32、ReAct turn budget 100、三个 seeds。math 使用 DAPO-Math-Train-400、DAPO-Math-Test-100 与
  AIME 2026；DocVQA 将 official validation split 前 2,700 作为 evolve、后 2,649 作为 held-out。parallel
  latency ablation 在 8-GPU A800 node 上报告约 3 分钟，对比 sequential `B=1` 约 60 分钟、`B=4` 约 15 分钟；
  这是作者 workload 下的单节点 wall-clock/round contract，不是生产 Skill 构建 SLO。论文未披露完整 training-free
  pipeline 的 token/cost、GPU utilization、failure retry、merge variance 或人工 review cost。
- **Baselines / Ablations / Selection Boundary**：对比 no skill、Anthropic human-written xlsx skill、
  parametric draft、sequential edits、ReasoningBank-style top-1 retrieval（Qwen3-Embedding-8B）以及 single-call
  error analyst。122B 下 parallel 在被测 spreadsheet 指标优于 sequential；35B 下 sequential `B=1` 的 Soft/Hard
  反而略高，故稳定结论是 round latency 与 frozen-base order independence，不是 universal quality dominance。
  retrieval 对比只覆盖同一 spreadsheet pool 与 top-1 implementation，不能证明所有 retrieval memory 较差。
  repository 的三 seed 流程先在 evolve/training split 选最佳 evolved Skill 再测 held-out，必须记录 model-selection
  pressure；同一模型同时生成 trace、分析、归并也会产生 correlated error。
- **What the Evidence Proves / Does Not Prove**：证据支持在三个作者 benchmark family 与两个 Qwen3.5
  model sizes 下，trajectory-grounded skill compilation 可以超过被测 human/parametric/retrieval baselines 的若干
  slice，并能在 model size 与 OOD task 间转移。`+57.7 pp` 只是 35B-authored Creation+Error Skill 给 122B
  用户的单个 WikiTQ slice，不是通用收益；DocVQA 中 35B-authored Skill 还使 35B accuracy 下降 6.2 pp，说明
  task execution 与 Skill authoring 能力不同。证据不证明 static Skill 适合开放域、频繁变化或高风险 policy，
  不证明 recurring patch 等价于 causal truth，也不证明 artifact 跨 harness、tool version 与 context contract
  无需重新验证。
- **Limitations / Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：pre-deployment
  consolidation 省去每请求 retrieval，却把成本迁到批量 trajectory generation、diagnosis、merge 与 full-skill
  context；merge 可能压掉 rare-but-critical evidence、错误解决冲突、引入 hallucinated edit 或使 Skill bloat/stale。
  论文明确尚不能量化单 patch 边际因果作用，也不能追踪 inference 时具体 section 的实际效用。online sequential
  edit 在低样本/非平稳环境仍更及时；retrieval memory 在 query-specific evidence、provenance/delete、频繁更新或
  context budget 紧张时仍合理；human authoring 在 authority、安全与规则性 domain 中仍是最终边界。
- **Evolution / ROADMAP / Adjacent Chapters / Disposition**：演进为 `human/parametric Skill -> sequential
  trajectory edits or episodic retrieval -> frozen-base per-trace diagnosis -> prevalence-weighted hierarchical
  consolidation -> versioned declarative Skill -> held-out/rollout evidence`，属于 `Direct Evolution + Layering /
  Dependency`。已读 Ch73/76/77/80：Ch73 已拥有 raw episode→derived procedural memory 及 provenance，Ch76
  已拥有 failure localization/causal repair，Ch77 拥有 durable evaluation workflow；真正缺口在 Ch80 的 Skill
  registry 还未定义由 trajectory evidence 生成、归并、验证、rollout、supersede 的 artifact lifecycle。暂定
  `Refine — Existing Argument (Ch80 owner; Ch73/76/77 handoff; Experimental; Artifact Partially Reproducible;
  Historical Books Gate Closed)`。本轮不修改 Books。

### Natural-Language Agent Harnesses / Intelligent Harness Runtime — 28/30

- **Source Family / Metadata / Revision / Access**：`NLAH-IHR-HARNESS-REPRESENTATION`；arXiv:2603.25723
  v1 first-public 2026-03-26，v2 revised 2026-05-18。已读 v1 complete HTML、方法/formalization、全部三组
  RQ、main tables、paired flips、module ablation、code-to-text migration、discussion、limitations 与 Appendix
  A～F，并核对 v2 abstract/revision history。当前 LinguaClaw repository 是 post-window continuation，只有
  4 commits、无 release/tag；公开 thin runtime、runtime policy 与 harness modules，但 benchmark experiment
  platform/reproduction guide 仍独立或 WIP，不能作为 v1 全量复现，故为 `Artifact Partially Reproducible`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：code controller 能以
  type、test、exception 与 deterministic transition 精确表达 orchestration，在规则稳定和安全边界严格时最
  可靠；framework defaults 又降低重复实现成本。但真实 harness behavior 分散在 controller、prompt、tool
  adapter、verifier、state convention 与 hidden runtime，导致跨系统迁移同时改变多项变量，无法判断结果来自
  model、pattern 还是 substrate。新约束是把可复用高层 control pattern 暴露为可读、可版本、可组合和可消融
  的 artifact，同时保留不可交给概率解释器的 enforcement spine。
- **Mechanism / State Ownership / Control and Data Flow**：NLAH 显式定义 contracts（input/output、budget、
  permission、retry/stop）、roles、stage topology、deterministic adapters/scripts、state semantics 与 failure
  taxonomy。IHR 每步让 in-loop LLM 联读 harness、current environment/state 与 runtime charter，选择下一个
  agent action；backend 负责 terminal/multi-agent tools，charter 定义 contract、child lifecycle 与 state
  semantics。`AgentCall(T, Ω_in) -> (artifacts, ΔΩ, normalized response)` 把单 completion 提升为有权限、预算、
  输出路径和 completion gate 的 run object。canonical workspace 将 task、append-only history、child-local
  workspace、runtime state 与 final artifacts 分开；code 继续拥有 sandbox、tool interface、parser、test 与
  deterministic verifier，natural language 不拥有不可逆 policy enforcement。
- **Experimental / Workload Contract**：v1 使用 Codex CLI 0.114.0、GPT-5.4、reasoning effort xhigh，运行
  于 Ubuntu 24.04 / 64 CPU / 251 GiB server；每 task Docker cap 为 32 vCPU、84 GiB memory、40 GiB
  storage。SWE-bench Verified 只抽样 125 项，OSWorld 只抽样 36 项，单一 fixed random seed，未运行完整
  benchmark。RQ1 比较 TRAE/Live-SWE 的 Full IHR、去 runtime skill、去 harness skill；RQ2 从 benchmark-specific
  Basic 逐一添加 file-backed state、evidence answering、verifier、self-evolution、multi-candidate search 与
  dynamic orchestration；RQ3 在 IHR 下比较 native OS-Symphony 与 reconstructed NLAH。论文未披露重复运行
  variance、task-selection sensitivity、端到端 API/container/tool cost、cache discount、长 context surcharge 或
  production SLO。
- **What the Evidence Proves / Does Not Prove**：证据支持在这个单模型、小样本、共享 IHR contract 下，
  natural-language harness 能实际改变 delegation、artifact/state flow、verification 与成本，并可做 module-level
  ablation；它不支持 monotonic gain。超过 110/125 SWE paired samples 在 Full 与 ablation 间结果相同，变化
  集中于 boundary cases；Full TRAE 的约 90% token/call/tool work 位于 child agents，说明新增结构有实质资源
  代价。OSWorld 47.2 vs code 30.4 同时伴随 substrate/action-path 从 GUI repair 转向 file/shell/package
  operations、trace topology 与 state surface 变化，不能解释成 representation language 的独立因果优势。
- **Ablation / Failure Boundary**：file-backed state 更直接改善 auditability、handoff 和 compaction survival；
  self-evolution 在被测 SWE slice 主要通过 acceptance-gated narrow retry 改善，而不是无限搜索。Verifier 与
  multi-candidate search 可因 local acceptance object 不等于 benchmark evaluator、过重 search 与 infrastructure
  sensitivity 而降低 aggregate score；dynamic orchestration 多为 solved-set replacement。作者明确承认
  runtime charter 可能吸收 harness behavior，text salience/prompt length 使 module ablation 不是严格 causal
  identification，hidden service state/proprietary scheduler 也无法从 text 忠实恢复。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：portable text 提升 inspection、diff、
  reuse 与 experiment isolation，却把类型错误变成 semantic ambiguity，引入 prompt injection、malicious script/
  tool graft、supply-chain contamination、runtime-version drift 与 context-budget cost。deterministic code/DSL 在
  hard safety、精确 concurrency、side-effect transaction、low-latency loop 和形式验证中仍应拥有 spine；NLAH
  更适合 task-family policy、roles、evidence contract 与可变 orchestration。Simple task 的 direct path 也可能
  比多 stage/多 Agent 更可靠，旧的 minimal harness 不因可组合模块出现而失效。
- **Evolution / ROADMAP / Adjacent Chapters / Disposition**：演进为 `controller bundle + hidden defaults ->
  explicit pattern layer -> natural-language harness artifact + shared interpreter -> deterministic adapters/enforcement
  + durable state/evidence -> versioned module ablation and rollout`，属于 `Layering / Dependency`，不是 code-to-text
  replacement。已读 Ch77、Ch78、Ch80，并联读 Ch62 既有边界：Ch77 已有 deterministic spine / agentic nodes，
  但尚未把 harness pattern representation 与 runtime enforcement 分层；Ch80 已拥有 Agent definition、Skill
  registry 与 evidence plane，Ch78 拥有 delegation cost/state，Ch62 拥有 subject/harness/evaluator identity。
  暂定 `Refine — Existing Argument (Ch77 owner; Ch80/78/62 handoff; Experimental; Artifact Partially Reproducible;
  Historical Books Gate Closed)`。本轮不修改 Books。

### Density-aware Soft Context Compression with Semi-Dynamic Compression Ratio — 26/30

- **Source Family / Metadata / Revision / Access**：`DENSITY-AWARE-SEMI-DYNAMIC-SOFT-CONTEXT`；
  arXiv:2603.25926 v1 first-public 2026-03-26，当前无后续 revision。已读完整论文、公式、训练数据生成、
  main evaluation、ratio/scale/quality analysis、limitations 和 Appendix，并核对官方 repository、synthetic
  dataset 与公开 LoRA weights。repository 当前只有 4 commits、无 release/tag；训练、evaluation、model
  code 和 artifacts 可访问，但尚无独立复现，故只记为 `Artifact Available`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：固定压缩率使 token
  shape、memory budget、batching 与 latency 更可预测，也避免 selector error；当 workload 的信息密度近似
  同质时，它仍是合理的工程默认值。但不同输入把同样 token budget 分给冗余描述与关键细节，会让统一
  ratio 在低密度样本浪费 latent tokens、在高密度样本丢失证据。完全连续、逐样本可变的压缩结构又会制造
  过多 execution shapes、调度和优化复杂度，因此候选尝试把连续 density estimate 映射到有限离散档位。
- **Mechanism / State Ownership / Control and Data Flow**：Qwen3 encoder 先产生 hidden states；最后一个
  hidden state 经 linear regression head 预测 `log2` compression ratio，再加可学习 scale、指数还原并量化到
  `{2, 4, 8, 16, 32}`。选定 ratio 决定 mean-pooling window，pooled representations 经 MLP 投影为 latent
  tokens，并通过 placeholder expansion 进入 decoder。encoder/selector 拥有 density estimate 与 bucket
  decision，compressor 拥有 latent-token layout，decoder 只消费展开后的 working set；训练时这些状态共同
  优化，serving 时 selected ratio 还会成为 batching、cache identity 与 capacity accounting 的一部分。
- **Training / Evaluation Contract**：synthetic training data 约 10M samples，来源为 UltraFineWeb，由
  Qwen3-30B teacher 生成 question/answer/summary，输入 context 为 128～1300 tokens；summary length 被用作
  density proxy。实验使用 Qwen3-0.6B 与 Qwen3-4B、LoRA、global batch 80；evaluation 从 HotpotQA、SQuAD、
  Natural Questions 与 AdversarialQA 各取 1,000 个过滤后小于 2,048-token 的样本，按 substring accuracy
  评分。论文只在答对样本上统计 realized compression ratio。公开材料未披露训练 hardware、steps、learning
  rate、随机种子/variance、端到端 latency、TTFT、KV footprint、并发或 production SLO。
- **What the Evidence Proves / Does Not Prove**：结果支持在这两种 Qwen3 规模、短输入 synthetic training
  与四个 QA slice 中，用连续 density signal 选择有限 ratio buckets 可以优于被测固定-ratio baseline 的若干
  operating points；它不证明 LLM 无法使用单一压缩率，也不建立跨模型、长 context 或生产 serving 的通用
  Pareto frontier。selected-ratio variance 与 accuracy gain 的相关性只是相关证据，不构成 density adaptation
  的因果证明；summary length 也是 teacher-dependent heuristic，不是真实信息密度标注。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：离散 bucket 控制形状数量，却新增
  selector miscalibration、bucket-boundary discontinuity、batch shape divergence、scale drift、cache-key 漏项和
  scheduler capacity prediction error；hard pooling 还可能不可逆地删除 exact identifier、negation 或局部证据。
  固定 ratio 在 workload 同质、SLO 需稳定和 selector 缺少校准时仍合理；hard/text compression 保留可读性与
  provenance，RAG 保留 source-level identity，风险高且 context 可承受时 full context 仍应作为 validity branch。
- **Evolution / ROADMAP / Adjacent Chapters / Disposition**：演进为 `full context -> fixed hard/soft compression
  -> continuous density estimation -> finite executable ratio buckets -> selected-ratio-aware batching/cache/SLO
  control`，关系为 `Direct Evolution + Layering / Dependency`。已读 Ch22、Ch71 和 Ch41：Ch22 已拥有 long-
  context capacity/effective-utilization 边界，Ch71 已说明 compression 是有损 derived view，Ch41 负责 KV 与
  runtime memory；缺口是把 semantic density estimate 与有限可执行结构分离，并让 selected ratio 进入运行时
  identity。暂定 `Refine — Existing Argument (Ch22 owner; Ch71/41 handoff; Experimental; Artifact Available;
  Historical Books Gate Closed)`。本轮不修改 Books。

### Learning to Commit: Generating Organic Pull Requests via Online Repository Memory — 25/30

- **Source Family / Metadata / Revision / Access**：`REPOSITORY-CHRONOLOGICAL-ORACLE-MEMORY`；
  arXiv:2603.26664 v1 first-public 2026-03-27，当前无后续 revision，作者标记 `Preprint / Work in
  progress`。已读完整 HTML、problem formulation、dataset construction、method、全部四组 experiment、
  deterministic/judge metrics、analysis、case study、limitations/future work 与 references。实验仓库、commit
  dataset、synthetic issues、Skill documents、run traces 和实现均未公开；arXiv 也未链接 code artifact，故为
  `Artifact Not Available`，不能独立复现。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：给 Agent 当前 repository
  snapshot 能提供类型、API、tests 和最终架构，适合一次性定位与修复；static RAG 读取相关历史也成本可控。
  但 snapshot 只显示“现在是什么”，不会直接保留某个 boundary 为什么形成、maintainer 曾拒绝什么，以及
  项目如何从旧约束演进。随着 Agent 连续维护同一 codebase，单任务 pass/fail 不再覆盖 patch 是否复用内部
  API、符合 module boundary、控制 diff scope 并能被未来 maintainer 接受。
- **Mechanism / State Ownership / Control and Data Flow**：历史 commits 按 cutoff 分成 learning prefix
  `C-` 与 future test `C+`。对每个历史 commit，Agent 在 parent snapshot、synthetic issue 与当前 Skill memory
  上先 blind attempt，随后才看到 accepted oracle diff；contrastive reflection 比较 localisation、logic、API
  reuse 与 style gap，再通过 create/revise/deprecate 更新结构化 Skill document。未来任务只读取 cutoff 前的
  Skill 与当前 snapshot。repository/version-control 拥有 snapshot 与 accepted diff；benchmark builder 拥有
  cutoff、filter、category 和 synthetic issue；memory controller 拥有 Skill version/provenance；Agent 只提出
  patch 与 reflection，不能把自己的失败直接升级为 authoritative repository rule。
- **Evaluation Contract**：内部 expert-maintained RL-training repository 有 2,738 个 non-merge commits；经过
  programmatic/LLM filtering 得到 386 个 candidates，再按七类分层抽样为 24 个 historical learning commits
  和 7 个 future test tasks。Claude Opus 4.6 在相同 tool surface 下比较 no-Skill baseline 与 Skill condition，
  组合 sequential/parallel learning 和 all/by-category curriculum，共四种 setting。deterministic metrics 是 file
  IoU、tool-call steps 与相对 oracle 的 line deviation；Claude Opus 4.6、Gemini 3.1 Pro 两个 judge 另比较
  scope、logic、redundancy 与 style。hardware、sampling parameters、随机 seed、重复运行 variance、token/
  API cost、wall time、tests pass rate、真实 review/merge outcome 与 judge-agreement 数值均 `Not Disclosed`。
- **What the Evidence Proves / Does Not Prove**：在这个单仓库、7-task pilot 中，四种 setting 有三种的 Skill
  variant 提高 file IoU 并减少 line bloat，seq-all 也减少 tool calls；但 seq-by-category 的 line deviation 反而
  更差，两个 judge 在 par-all/seq-by-category 也没有一致显示 Skill 胜出，style/scope 维度甚至保留 baseline
  优势。因而证据只支持“oracle-conditioned repository memory 值得进一步研究”，不证明 Skill 单调改善质量，
  也没有把 contrastive reflection 与 raw commit RAG、仅提供 oracle-derived Skill、更多 Context 或不同 task
  sampling 做因果拆分。严格 cutoff 阻止本文 pipeline 读取 future commits，不等于证明 base model 或 synthetic
  issue 没有其他污染；oracle similarity 也不等于真实 maintainer merge decision。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：逐 commit blind attempt 需要额外
  model/tool/environment 成本；accepted diff 可能包含过时 workaround、局部偏好或随后被撤回的设计，持续
  CRUD 又会产生 order dependence、Skill bloat、contradiction、staleness 与 category leakage。synthetic issue
  从 oracle diff 生成，会引入不真实的 specification clarity；以单一 oracle patch 衡量 localisation/line size
  也会惩罚合法替代实现。当前 snapshot + tests 在 one-off、规则已文档化或 history quality 低时仍最可靠；
  raw-history retrieval 在问题强依赖具体 commit、需要完整 provenance 时优于过早蒸馏；human review 在
  architecture authority、style dispute 和 irreversible change 上仍不能被 Skill 取代。
- **Evolution / ROADMAP / Adjacent Chapters / Disposition**：演进为 `current snapshot -> passive history
  retrieval -> chronological blind attempt + accepted-diff contrast -> derived procedural Skill -> future time-split
  evaluation -> versioned refresh/deprecation`，属于 `Direct Evolution + Layering / Dependency`。已读 Ch73、
  Ch80 与 Ch62：Ch73 已有 raw episode→derived procedural memory、provenance/supersession 与 advisory-state
  边界，但尚未明确 repository snapshot 与 accepted change history 的信息差；Ch80 已拥有 Skill registry，
  Ch62 已拥有 temporal state-sequence evaluation。因此暂定 `Refine — Existing Argument (Ch73 owner;
  Ch80/62 handoff; Experimental; Artifact Not Available; Historical Books Gate Closed)`。本轮不修改 Books。

### TAPS: Task Aware Proposal Distributions for Speculative Sampling — 29/30

- **Source Family / Metadata / Revision / Access**：`TASK-AWARE-SPECULATIVE-PROPOSAL-COMPOSITION`；
  arXiv:2603.27027 v1 first-public 2026-03-27，当前无后续 revision。arXiv HTML 不存在，已改读 21 页 v1
  PDF，覆盖 background、HASS/EAGLE-2 formulas、五个 RQ、完整 setup/results、routing/entropy/depth analysis、
  discussion/limitations、tree-merge code、lossless proof 与 acceptance appendices；同时核对 36-commit official
  repository、HASS/EAGLE code、Hugging Face weights 和 datasets。artifact 可访问、无 release/tag，本轮未独立
  复现实验，故只记为 `Artifact Available`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：单一 generic drafter
  部署、缓存和 compatibility 简单；在 workload 稳定或 domain 差异小的时候，它避免多模型驻留、双重 draft
  work 与路由校准。旧研究主要优化 draft architecture 与 verification，却常把 draft training distribution
  当成固定背景。新约束是 production workload 可能同时包含 chat、math 等 proposal distributions：一个
  target-compatible drafter 也会因 domain/temperature mismatch 缩短 accepted prefix。
- **Mechanism / State Ownership / Control and Data Flow**：论文固定 Meta-Llama-3-8B-Instruct target、tokenizer
  和 lossless verifier，分别训练 MathInstruct、ShareGPT 与 mixed HASS/EAGLE-2 drafts。weight averaging 在参数
  空间合并 checkpoints；confidence routing 则让两个 specialist 从同一 prefix 各生成一棵 tree，用 mean node
  confidence 选一棵送给 verifier；merged-tree 把两棵 tree 的 non-root nodes 拼到 shared root 下，保持各自
  ancestor mask 和 depth position id、屏蔽 cross-subtree attention，再用一次 target pass 验证。registry 拥有
  target/draft/data identity，router 拥有 selection evidence，verification runtime 拥有 packed tree/mask 与
  acceptance，KV manager 只提交最终 accepted prefix。
- **Correctness Boundary**：论文证明若每棵输入 tree 本身满足 fixed-valid-tree 的 lossless assumption，按任何
  prefix-dependent policy 选择 tree 仍是 target distribution 的 mixture；merged packing 若保持 token、position
  和 within-subtree attention 等价，target logits 与 standalone verification 一致，因此也保持 target sampling
  law。这个证明保护 sampling semantics，不证明 implementation 没有 mask/index/KV bug，也不证明更多 tree
  nodes 具有更低 latency。
- **Training / Evaluation Contract**：target 为 Meta-Llama-3-8B-Instruct；draft 是单层、hidden size 4096、
  约 0.8B 参数的 HASS 或 EAGLE-2，与 target 共 tokenizer/vocabulary。single-domain 各 70k examples；mixed
  为 35k+35k 或 70k+70k；全部训练 20 epochs、learning rate `3e-5`、batch 8、gradient accumulation 1；HASS
  使用 top-K=10、loss weight 1.0、3 个 alignment steps。MT-Bench、GSM8K、MATH-500、SVAMP 在 temperature
  0/1 上比较 acceptance length，单节点 4×NVIDIA A100。论文未披露 precision、input/output length、serving
  batch/concurrency、arrival pattern、随机 seeds/variance、TTFT/P99、显存占用或 SLO。
- **What the Evidence Proves / Does Not Prove**：两种 backbone 都显示 matched-domain specialization，mixed
  data 在 temperature 变化下不单调；naive 0.5 weight average 及 interpolation sweep 弱于被测 inference-time
  composition。confidence routing 的 benchmark-level selection 比 entropy routing 更分离，merged tree 的
  acceptance length 最高。它不证明 confidence 对 unseen/mixed prompts 已校准，也不证明 weight merging 的
  更强方法普遍无效；“shallow exploration / deep exploitation”来自 depth-wise correlation，不是控制变量完备
  的因果机制。最重要的是，acceptance length 不是 end-to-end speedup：routing 先生成两棵 tree，merged tree
  又扩大 target verification shape，作者也明确把完整系统 trade-off 留作未来工作。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：specialist composition 增加 draft
  weights/activations residency、两个 tree 的生成成本、router calibration/decision trace、larger verification
  shape、batch fragmentation 和 cache/rollback 状态；task mix 漂移会让 confidence policy 失效，prompt 同时
  跨 domain 时二选一标签也可能过粗。单一 generic 或 mixed drafter 在显存紧、流量同质、低并发 latency
  稳定性优先时仍合理；offline data-mixture training 用更低 runtime complexity 换取平均化；weight merge 只有
  本文 naive linear path 失败，不能否定经过 alignment、task-vector 或再训练的其他合并分支。
- **Evolution / ROADMAP / Adjacent Chapters / Disposition**：演进为 `generic independent drafter ->
  target-feature drafter/dynamic tree -> domain-specialized draft artifacts -> mixed-data robustness -> confidence-
  selected specialist -> merged proposal trees -> cost/SLO-aware composition`，关系为 `Direct Evolution + Layering /
  Dependency`。已读 Ch44 及相邻 Ch42/41/45，并核对 Ch55 registry boundary：Ch44 已有 lossless contract、
  verify-capacity 与 draft artifact identity，但尚未明确多个 workload specialists 的三种 composition branch。
  暂定 `Refine — Existing Argument (Ch44 owner; Ch42/41/55 handoff; Experimental; Artifact Available;
  Historical Books Gate Closed)`。本轮不修改 Books。

### DataFlex: A Unified Framework for Data-Centric Dynamic Training of Large Language Models — 28/30

- **Source Family / Metadata / Revision / Access**：`DYNAMIC-DATA-CONTROL-PLANE`；arXiv:2603.26164 v1
  first-public 2026-03-27，当前只有 v1。已读 HTML 全文、三类 abstraction、implementation、全部 experiments、
  efficiency analysis、limitations 与 LESS/DoReMi appendix，并核对 official repository、documentation 和
  Hugging Face datasets。repository 标注项目首次公开于 2025-12-23，ZeRO-3 support 于 2026-03-17 加入；
  W13 只拥有 paper/technical-evidence node，不把较早 code history 重写为 3 月 27 日新事件。artifact 可访问，
  本轮未独立复现实验，故记为 `Artifact Available` 而不是 `Reproduced`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：offline filtering、固定
  subset 和静态 mixture 具有可复现、低控制开销、易审计的优点；当 data order、domain quality 与 model
  response 可预先估计时，这些方案仍合理。但训练过程中 sample value、domain marginal value 和 loss/gradient
  signal 会随 checkpoint 改变，训练前一次性决策无法观察 trajectory。新约束因此不是“数据越动态越好”，而是
  需要把 data policy 变成显式、可插拔、可按 cadence 更新的 closed-loop control interface。
- **Mechanism / State Ownership / Control and Data Flow**：DataFlex 把 algorithm 映射为三种 trainer：Select
  Trainer 输出 subset/ranking，Mix Trainer 输出 domain mixture weights，Weight Trainer 输出 per-sample
  weights。component registry 装载算法；training controller 在 warmup/update interval 到达时暴露 embedding、
  inference、loss、gradient 或 validation signals，component 计算新 action 并缓存，data pipeline 在后续 steps
  执行。model/optimizer/checkpoint 由 base trainer 拥有，data-policy state、update cursor 和 cached decision
  由 component/controller 拥有；dataset/sample/domain identity 必须与 action 一起版本化，否则 resume 无法重建
  相同 trajectory。
- **Implementation / Distributed Boundary**：实现建立在 LLaMA-Factory 上；单卡或普通分布式路径直接读取
  model state，ZeRO-3 路径通过 `safe_get_full_grad` 与 `safe_get_full_optimizer_state` 从 shards 重建 full
  state 后交给 data component。这个兼容层让既有 algorithm 能运行，但会引入 all-gather/reconstruction 的
  memory、communication、synchronization 和 failure-recovery cost；论文没有证明所有 data algorithm 都可在
  shard-local state 上等价计算，也没有定义 controller/cache 与 checkpoint 的原子提交协议。
- **Evaluation Contract**：selection/reweighting 使用 Open-Hermes 100K、Mistral-7B 与 Llama-3.2-3B，LoRA
  rank 32/alpha 64、AdamW、LR `5e-7`、global batch 8、1 epoch，warmup 100、update interval 50、30 次
  update，8×H20。mixture 使用 SlimPajama 七域、6B/30B tokens；Qwen2.5-1.5B target，DoReMi 另用
  Qwen2.5-0.5B proxy/reference；BF16、ZeRO-3、FlashAttention 2、seed 42，6B 为 8 GPUs，30B 为
  4 nodes×8 H20。论文没有提供多 seed variance、production SLO 或完整 controller-state recovery experiment。
- **What the Evidence Proves / Does Not Prove**：作者结果说明同一 trainer interface 能实例化 LESS/NEAR/
  TSDS、DoReMi/ODM 与 loss-based weighting，并在上述 contracts 中观察到部分 online policy 的 quality 或
  iteration-efficiency 改善；也显示收益不一致——部分 Mistral setting 与 random/loss/static 接近，Llama 上
  offline method 明显落后，6B mixture 存在 overall/domain perplexity trade-off，30B MMLU 差异较小。反复
  访问 validation/test signal 还可能产生 selection leakage。多 GPU `57.13%` 之类效率数字混合了 GPU 数量、
  update count 与执行路径差异，不是 matched-resource scale-up 证明，也不能外推为通用训练加速。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：online data control 引入 policy
  staleness、delayed feedback、selection bias、validation overfitting、positive feedback loop、gradient/data
  privacy、distributed full-state materialization、cache invalidation 和 resume divergence。低噪声 held-out
  signal、可承担 controller cost 且数据价值随 trajectory 漂移时，动态策略有意义；固定数据顺序、严格
  reproducibility、弱/高噪声 validation 或 control cost 高时，offline filtering/static mixture 仍是更稳健分支。
  评测 benchmark 不应静默成为训练 oracle，任何收益都应对齐总 tokens、validation accesses、额外 gradient/
  selection compute、GPU 数和 wall time。
- **Evolution / ROADMAP / Adjacent Chapters / Disposition**：演进为 `offline filtering -> fixed subset/mixture ->
  periodic metric-based reweighting -> unified select/mix/weight control plane -> distributed state-aware controller ->
  versioned policy/checkpoint/data-cursor recovery`，关系为 `Direct Evolution + Layering / Dependency`。已读 Ch23
  及相邻 Ch22/24，并核对 Ch35、Ch56 与 Ch62：Ch23 已把 mixture `alpha` 写成 gradient-frequency policy，
  但尚未显式区分三类 action、observation、cadence 和 controller state；Ch24 拥有 trajectory identity，Ch35
  拥有 ZeRO state，Ch56 拥有 Training Operator，Ch62 拥有 leakage boundary。因此暂定 `Refine — Existing
  Argument (Ch23 owner; Ch24/35/56/62 handoff; Experimental; Artifact Available; Historical Books Gate
  Closed)`。本轮不修改 Books。

### Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents — 28/30

- **Source Family / Metadata / Revision / Access**：`RUNTIME-CLARIFICATION-GATE`；arXiv:2603.26233 v1
  first-public 2026-03-27，v2 revised 2026-06-03。已读 v1 全文、methods、全部 results、question/difficulty/
  conditional analyses、prompts、examples、cost appendix 与 limitations；另读 v2 的 Kimi K2.6 experiment、
  dataset spot-check 和 prompt changes，并核对 official repository、five-setting scripts、agent code path、
  batch IDs、analysis/reproduction guide 与 known harness fix。v2 属 post-window revision evidence，不回写成
  W13 event。代码与 evaluation setup 可访问，本轮未重跑约数千美元 API experiment，记为 `Artifact
  Available`，不是独立复现。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：完整 specification +
  autonomous execution 在封闭 benchmark、低交互成本和目标清楚时最简单；强制 first-turn question 也能在已知
  缺信息时稳定取回 context。但真实 repository task 的缺口可能直到 exploration/test failure 才显现，永远先问
  会 over-clarify，永远执行又会把假设写成 side effect。约束变化是 Agent 必须在 partially observable trajectory
  中持续区分“可从 repository/tool 观察获得的信息”和“只能由 user authority 补充的 intent”。
- **Mechanism / State Ownership / Control and Data Flow**：Full/Hidden 是无交互上下界；Interactive Baseline
  用 prompt 强制起始 query；UA-Single 每轮向同一 coder 注入 uncertainty reminder。UA-Multi 把 Main Agent 与
  Intent Agent 分离：Main 拥有 shell/edit/test tools，Intent 每轮读取 conversation/state history、只能调用
  binary `clarify_decision`；若为 true，runtime 约束 Main 下一动作必须调用 `clarify`，GPT-5.1 simulator 再从
  withheld original issue 返回答案。workflow 应拥有 state-history snapshot、decision、question/reply、turn
  budget 和 resumed action；Intent Agent 只是 advisory detector，不拥有用户意图真值或最终 side-effect authority。
- **Evaluation Contract**：v1 在 OpenHands 上跑 SWE-bench Verified 500 tasks 的 synthetic underspecified
  variant；Claude Sonnet 4.5 是 coder/Intent backbone，GPT-5.1 是 oracle user simulator，最大 100 effective
  coding iterations，五种 settings 各跑一次。UA-Multi 实际配置 300 framework iterations，因为一次 coding
  turn 会增加 Intent delegate events；simulator 最多三个有效 interaction turns，随后返回 canned response。
  v1 报告 UA-Multi 69.40%、UA-Single 61.20%、Hidden 54.80%、Full 70.80%，使用 permutation tests；API
  cost 分别约 `$3.50/$2.03/$1.80/$1.63` per task。hardware、sampling parameters、random seeds、run-to-run
  variance 与 real-user latency/abandonment 均 `Not Disclosed`。
- **What the Evidence Proves / Revision Boundary**：v1 支持在这个 model/simulator/harness contract 中，职责
  分离比同一 Agent 的 recurring reminder 更有效，并显示 query timing 从 late-heavy 移到 early/mid；它不证明
  detector 获得 calibrated probability，也不证明问题本身导致成功——被询问集合是 policy-selected，存在
  confounding。v2 用 Kimi K2.6 重复总体趋势，却出现 UA-Multi 435/500 tasks 被询问、平均 8.71 queries、
  Interactive Baseline 因 tool misuse 降到 47.20%；这说明 scaffold 与 backbone/tool semantics 强耦合。v2
  对 10 个 synthetic issues 的 spot-check 只有 5 个被判定确实移除 essential information，不能把整个 dataset
  当成统一 clarification oracle。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：UA-Multi 每个主循环增加一次模型
  判断，v1 总 API 成本约为 Full 的 2.14 倍；state-history duplication、false-positive interruption、false-negative
  assumption、repeated/canned user response、stale intent、privacy exposure 与 clarification deadlock 都是新增
  failure mode。目标明确、可由 tool observation 消歧或用户不可达时，autonomous single Agent + deterministic
  verifier 仍合理；已知必须补字段时，typed form/required-field validation 比 LLM detector 更可靠；高风险、
  不可逆 action 则必须 escalation/approval，不能由 detector 的“无需澄清”自动授权。
- **Evolution / ROADMAP / Adjacent Chapters / Disposition**：演进为 `fully specified autonomous task ->
  hardcoded upfront query -> recurring self-reminder -> separate continuous intent monitor -> cost/risk-calibrated
  clarification gate -> real-human feedback and typed uncertainty evidence`，属于 `Direct Evolution + Layering /
  Dependency`。已读 Ch77、Ch78 及 Ch75，并核对 Ch62：Ch77 已拥有 ambiguous-intent model node、durable
  workflow state 和 Human-in-the-Loop，但尚未明确 clarification detection/action/reply/resume 的状态协议；Ch78
  已要求 specialized role 的 evidence independence，Ch75 拥有 belief update，Ch62 拥有 interactive evaluation
  boundary。因此暂定 `Refine — Existing Argument (Ch77 owner; Ch78/75/62 handoff; Experimental; Artifact
  Available; Historical Books Gate Closed)`。本轮不修改 Books。

### XpertBench: Expert Level Tasks with Rubrics-Based Evaluation — 25/30

- **Source Family / Metadata / Revision / Access**：`EXPERT-RUBRIC-JUDGE-CALIBRATION`；尽管 arXiv ID 是
  2604.02368，v1 submission timestamp 为 2026-03-27，故 owner 是 W13；v2/v3/v4 分别为 04-06、04-07、
  04-21。已读 v1/v4 metadata、全文、task/rubric construction、ShotJudge、results 与五域 example/rubric
  appendix，并核对 ByteDance Xpert platform 与 Hugging Face `ByteSeedXpert/expertbench`。当前 dataset 页面
  明确为空、README 为空、无公开 evaluation code/raw expert annotations/model outputs，故记为 `Artifact Not
  Available`；v2～v4 只作 post-window revision check。
- **Original Problem / Previous Design / Changed Constraint**：exact-match/exam benchmark 可重复且便宜，适合
  closed-form knowledge；纯 human review 能处理开放任务，却难以扩展；zero-shot model judge 可扩展，但有
  style/self-preference。长篇 professional artifact 同时包含事实、约束、专业推理、合规与可执行性，单一 reference
  string 或 holistic Likert 分数无法定位 failure。新约束是保留 expert specification 的粒度，同时让 scorer 可批量执行。
- **Mechanism / State Ownership / Control and Data Flow**：专家提交真实任务和 reference answer，经资格筛选、
  peer review 与约 30% senior spot-check；LLM 先起草 rubric，领域专家修订为多数 15～40 个 atomic binary
  criteria，赋 importance class 与 1～10 weight。GPT-5 baseline response 由 primary experts 逐 criterion 标注
  rationale/score，再由 senior experts meta-review；Gemini 2.5 Pro judge 在每个 task 上接收 prompt、rubric 和
  这一组 one-shot anchor，输出 candidate 的 binary criterion verdict，最后以 normalized weighted sum 聚合。
  rubric/weight/anchor/judge/prompt/aggregation 都是独立 measurement state，不应合并为“一个分数”。
- **Evaluation Contract / Evidence Boundary**：总库宣称 1,346 tasks、80 categories、七域；真正 leaderboard
  evaluation 使用 stratified XpertBench-Gold 245 tasks，Computer Science/Healthcare 样本不足，细分只报告五域。
  v1 比较多种 vendor models，主 judge 是 Gemini 2.5 Pro；ShotJudge 的 human alignment 用 CDR=`P(agree)-
  P(disagree)`，报告 52.0%。论文未披露 CDR sample size/slices/confidence interval、judge sampling/prompt 完整
  artifact、candidate generation/search/tool budget、seeds/variance、invalid/abstain、inter-rater agreement 或
  per-example outputs。模型排名只在该私有 Gold subset、rubric、judge 和访问时版本内成立。
- **What the Evidence Proves / Does Not Prove**：论文展示了 expert-authored criteria + expert rationale anchor +
  model judge 的可执行 pipeline，并观察到 domain-dependent rankings；它不证明任务代表真实部署分布，不证明
  binary checklist 覆盖 holistic professional quality，也不证明 one-shot anchor 消除 judge bias。CDR 52% 本身
  表明 discordance 仍显著，不能称为 human-equivalent；以 GPT-5 response 作为唯一 anchor 还可能把其表达路径
  固化为 calibration reference。没有公开 artifact，作者结果当前不可独立审计或复现。
- **Trade-offs / Old Design / Failure Modes**：atomic rubric 提高局部可诊断性，却可能遗漏 emergent/global
  failure；flat weighted sum 允许多个 Optional/Important 命中补偿 Essential failure，除非另设 hard gate；expert
  authoring/review 昂贵且会产生 organization/time/version bias，one-shot anchor 会引入 anchoring/style leakage，
  judge 与候选 model family 还可能相关。exact/executable verifier 仍适合可形式化子任务，blind multi-expert
  review 仍适合高风险结论；模型 judge 应只扩展低风险 criterion execution，不取代 domain authority。
- **Evolution / ROADMAP / Existing Coverage / Disposition**：演进为 `closed-form exact benchmark -> holistic
  expert review -> atomic expert rubric -> expert-rationale-calibrated model judge -> criterion evidence + constrained
  aggregation -> deployment-grounded validation`，关系为 `Principle Reuse`。已读 Ch62 及相邻 Ch61/63；Ch62
  已明确 scorer ladder、human calibration、rubric formation、criterion execution、aggregation/ranking、decision
  policy、abstention/disagreement 与 hard constraints，比本候选公开机制更完整。因此为 `No Change — Already
  Covered (Ch62; Experimental; Artifact Not Available; Historical Books Gate Closed)`，本轮不修改 Books。

### EpochX: Credits-Native Human–Agent Production Network — 23/30

- **Source Family / Metadata / Revision / Access**：`EPOCHX-AGENT-PRODUCTION-MARKET`；
  arXiv:2603.27304 仅有 v1，first-public 2026-03-28。已读全文，包括 design philosophy、12 个公式、
  intent-to-delivery、asset admission/dependency graph、credit settlement、三个 cases、related work 与
  conclusion。官方 QuantaAlpha 产品页确认 `epochx.cc` 为 live platform，并复述 task publication → recursive
  decomposition → execution → verification/settlement → Skill/Trace/Experience accumulation；但 live site 本轮
  多次超时，论文和产品页均未链接可核验的 source repository、API/schema、immutable transaction log 或
  reproducibility artifact。搜索到的同名 PyPI package 未能由论文或官方页面建立 publisher identity，因此不
  用作实现证据。状态为 `Platform Accessible / Implementation Not Disclosed`。
- **Original Problem / Previous Design / Changed Constraint**：单 Agent/tool loop、封闭 Multi-Agent framework
  和内部 Workflow 在一个 owner、已知参与者与固定 budget 下合理：authority、state 与验收边界清楚，系统也
  不必承担开放市场治理。随着人和 Agent 跨组织承接任务，约束从“怎样完成一次任务”变成“怎样发现能力、
  在层级委托中约束预算、验证交付、保留可复用资产并使贡献者持续获得回报”。普通 registry 只保存 capability，
  普通 labor marketplace 又常让执行 trace 与 reusable Skill 在结算后消失；EpochX 试图把两层连接起来。
- **Mechanism / State Ownership / Control and Data Flow**：参与者集合把 human 与 agent 作为 requester/solver；
  requester 发布 task 并锁定 bounty，claimant 成为 lead solver，可把 parent task 分解为 subtasks，且 child bounty
  总和不得超过 parent bounty。执行时检索 Skill 与 operational assets，以历史 success、latency、resource
  efficiency、invocation 和 acceptance signal 选择能力；平台保存 task state、selected skills、intermediate
  results 与 trace，requester 对 deliverable 作 accept/reject。完成交易产生 candidate Skill、Workflow、Trace
  与 distilled Experience，经 sandbox/test/structural/review 等抽象 validation operator 后进入 asset set；
  dependency graph 记录 invocation、composition、derivation 与 version。accepted task 才释放 bounty，validated
  reuse 再向资产创建者累计 reward。论文清楚给出概念状态和数据流，却没有给出 transaction isolation、atomic
  settlement、validator authority、asset schema、identity/credential、rollback 或 distributed implementation。
- **Implementation / Evaluation Contract**：论文没有 system implementation section、benchmark、baseline、
  ablation、sensitivity、overhead、hardware/model/precision/length/batch/concurrency/SLO 或统计不确定性。证据是
 两个平台交付案例：一个复用并 fork Remotion Skill 生成两段视频、交付 source code、经批准结算 50 credits；
  一个学术写作任务经历 reject/revise/accept，最终交付约 12,000-word HTML artifact。第三个 household move
  描述 agent 规划与 human physical execution 的合理分工，但正文由 “Consider” 引入，不能与前两项真实交易
  同级视为已执行证据。三个案例均没有公开 task record、validator output、dependency graph 或 settlement log。
- **What the Evidence Proves / Does Not Prove**：论文证明的是一套可被明确建模的 architecture proposal，并以
  少量案例说明 task、delivery、revision、asset derivation 和 settlement 可以放进同一 narrative；官方页面也
  证明产品 surface 已公开。它不证明 credits 能形成 incentive alignment、quality selection 或可持续经济循环，
  不证明 requester acceptance 等于 correctness，更不证明 recursive delegation 在开放参与者中安全、可扩展或
  成本有效。作者也明确把 longitudinal large-scale evaluation、programmable verification 与 competitive reward
  design 留作 future work。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies**：market layer 让 demand 和 delegated
  budget 显式化，也能把 reusable artifact 的 downstream value 纳入 reward；代价是新增 Sybil/fraud/collusion、
  self-dealing reuse、low-quality asset farming、validator capture、requester hold-up、dispute/refund/chargeback、
  reputation portability、IP/license/privacy、price manipulation 与 physical-world liability。二值 acceptance 会把
  多维质量和 parent/child contribution 压平，reuse count 也会奖励 popularity 而非 causal value。单组织、稳定
  team、强合规或不可逆任务仍应使用内部 Workflow、固定 authority、typed approval 与 conventional billing；
  不需要为“Agent economy”引入开放市场。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage / Disposition**：演进为 `single-owner agent loop
  -> durable internal workflow -> bounded multi-agent delegation -> governed Skill registry -> task marketplace +
  credit-backed delegation -> programmable verification/dispute governance -> longitudinal incentive evidence`，
  属于 `Layering / Dependency`。已读 Ch77、Ch78、Ch79、Ch80，并核对 Ch55：Ch77 已拥有 durable state、
  approval、retry 与 artifact reference；Ch78 已拥有 delegation chain、typed handoff 与 verification；Ch80 已拥有
  Agent/Run identity、Skill provenance/dependency、evaluation/policy/evidence plane；Ch55 提供通用 immutable
  registry identity。EpochX 的长期新增量只可能是 market/incentive control plane，但公开证据不足以把它写成
  稳定机制。因此为 `No Change — Already Covered (Ch80 owner; Ch77/78/55 handoff; Experimental Case;
  Platform Accessible; Implementation Not Disclosed; Historical Books Gate Closed)`，本轮不修改 Books。

### daVinci-LLM: Open Data-Processing and Stage-Aware Pretraining System — 28/30

- **Source Family / Metadata / Revision / Access**：`DAVINCI-DATA-DARWINISM-PRETRAINING`；
  arXiv:2603.27164 仅有 v1，first-public 2026-03-28。已读 49 页完整论文，包括 Introduction、Related
  Work、Data Darwinism L0～L9 taxonomy、data pool/processing、architecture、四阶段 training recipe、19 个
  benchmark 的 checkpoint trajectory、200+ ablation、mixture/QA-ratio、PPL-versus-generation evaluation、
  LR/QA-masking appendices、prompt templates 与 conclusion，并核对官方 GitHub、final-model card 和 data
  card。论文声明完整 pipeline、data、checkpoint、logs 与 evaluation suite 均开放；但本次可访问 surface 中，
  repository 的 `Pretraining Pipeline` 仍标记 `Coming soon`，data card 明示当前只发布 subset、code portion
  尚在整理，且数据需 gated agreement。故状态为 `Artifact Partially Available / Openness Claim Not Yet
  Matched by Current Artifact Surface`，而不是 `Reproduced`。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：传统 data pipeline 把
  acquisition、normalization、规则/模型过滤和 fixed mixture 前置完成，能够固定 dataset identity、降低在线
  控制成本并提高复现性；当 sample value 对 checkpoint 变化不敏感时，它仍是合理 baseline。约束变化在于：
  更深的 generative processing 已经从“选择哪些 token”变成“变换、补全或合成哪些 supervision”，不同 domain
  的能力又在不同 token stage 出现 plateau；同一 data action 与 mixture 的边际价值因而依赖当前 model state、
  已见 token distribution、目标能力和 evaluator format，不能只用一个离线 quality score 表示。
- **Mechanism / State Ownership / Control and Data Flow**：Data Darwinism 将 operator 描述为 L0 acquisition、
  L1 normalization、L2 rule filtering、L3 learned/model filtering、L4 不引入外部知识的 generative refinement、
  L5 cognitive completion、L6 contextual completion、L7 environment synthesis、L8 ecosystem synthesis、L9 world
  synthesis。作者明确说明层级不要求严格顺序且可重复执行，因此它是 operator-semantics taxonomy，不是经过
  验证的单调质量阶梯。data pipeline 拥有 source/sample identity、operator/version 与 derived-data lineage；
  trainer 拥有 model/optimizer/checkpoint、token cursor 与 stage transition；evaluation controller 每 5K steps
  输出 general/code/science trajectory；mixture controller 根据这些 observations 选择后续比例或切换到 structured
  QA。数据流为 `raw pool -> typed processing operator -> versioned data slice -> stage mixture -> checkpoint ->
  protocol-specific evaluation -> next-stage decision`。如果 operator、teacher、prompt、mixture 或 evaluator
  revision 未进入 run identity，最终 checkpoint 无法解释其能力来源。
- **Implementation / Training Contract**：模型是从 random initialization 训练的 3.09B decoder-only Qwen2
  architecture：36 layers、hidden size 2048、16 query / 2 KV heads、SwiGLU 11008、RMSNorm、RoPE base
  10000、Qwen2 tokenizer/vocabulary 151,936、context 4096，precision BF16。总训练 8T tokens：Stage 1 为
  6T（4T + 2T），Stage 2 为 2T（1T + 1T）；早期 general foundation 后逐步提高 code/science，再引入
  structured QA/reasoning data。global batch 从 1024/2048/4096 sequences 逐级增大，后续为 4096；AdamW
  `beta1=0.9`、`beta2=0.95`、weight decay 0.1，learning-rate schedule 随 stage 调整。论文未披露 GPU
  型号/数量、training framework、总 FLOPs、wall time、energy/cost、distributed topology、随机 seeds、重复
  run variance 或 failure/recovery contract，故 8T recipe 不能被视为完整可复现的 Training Operator spec。
- **Evaluation Setup / Baselines / Ablations / Sensitivity**：每 5K steps 在 19 个 general/code/science benchmarks
  上评估，并与 OLMo 2/3 7B、Qwen 2.5/3/3.5、Llama 3.2 3B、Yulan Mini 对比。L2/L3 code filtering、L4 math
  refinement、L5 synthetic QA、Stage1/2 trajectory、五组 code/science mixture、QA ratio 10%～100%、PPL
  multiple-choice 与 generative CoT、cosine LR decay 和 QA question masking 均有受控实验。L3 相对 L2 的
  overall gain 很小且 EvalPlus 略降；L4 math refinement 显著提高 MATH，却轻微伤害 general average；过高 QA
  ratio 在 Stage2-1 造成 code/general degradation，而已建立能力后的 Stage2-2 对 70% QA 有不同响应；question
  masking 和 LR decay 只有边际增益。没有 seeds、confidence interval 或 statistical test，因此这些差异只在
  单项目 trajectory 中成立。
- **What the Evidence Proves / What It Does Not Prove**：证据支持三点受限结论：processing depth 会改变
  operator 的语义而不只是 filter threshold；domain marginal value 会随 checkpoint/stage 改变；data format 与
  evaluation protocol 会共同影响 measured capability。它不证明 L0～L9 越高越好，不证明 general benchmark
  在任意模型都于约 1T plateau，不证明 30/30/30/10 或 70% QA 是可迁移配比，也不证明 PPL 或 generative
  evaluation 任一方普遍更真实。MMLU 中 baseline ranking 可因 PPL-versus-generation protocol 反转，只说明
  evaluator 与 QA-format exposure 构成测量 contract；不能据此断言模型的底层知识发生同等幅度变化。
- **Limitations / Threats to Validity**：论文没有独立 Limitations section；hardware/compute、seeds/variance、
  contamination analysis、teacher/model-processing bias、data-license lineage 和完整 artifact 尚不足。所有主要
  stage decision 共享同一 model family、data pool 和 benchmark suite，反复读取 checkpoint evaluation 也可能
  把 benchmark 变成 curriculum oracle。synthetic QA pool 的 domain imbalance、format alignment 和有限 code
  QA 容量解释了部分 ratio result，却也使“structured QA 改变训练阶段”与“benchmark format matching”难以
  完全拆分。作者所谓 200+ ablation 展示覆盖广度，但不能替代多 seed、matched-compute 和外部 replication。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies**：更深 processing 与 stage-aware
  control 可把数据预算投向当前 bottleneck，却新增 teacher drift、semantic mutation、synthetic-mode collapse、
  source/derived contamination、benchmark feedback leakage、mixture oscillation、checkpoint-selection overfit 和
  lineage/rollback 成本。动态 stage transition 还要求保存 decision evidence；否则 resume 只能恢复 tensor，
  不能恢复“为何改变数据”。规则过滤、固定 mixture 和统一 evaluation 在低预算、稳定 workload、合规 lineage
  优先或缺少可信 online signal 时仍更易复现；PPL 适合便宜的 token-likelihood diagnostic，generative protocol
  更接近某些 deployment behavior，二者应并存而非互相覆盖。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage / Disposition**：演进为 `raw acquisition ->
  normalization/rule filtering -> learned selection -> generative refinement -> cognitive/context completion ->
  environment/ecosystem synthesis -> checkpoint-aware stage transition -> versioned data-policy control loop`，属于
  `Direct Evolution + Layering / Dependency`。已读 Ch23、Ch24、Ch25，并联读 Ch56 与 Ch62。Ch23 已拥有
  data-as-executable-spec、quality/mixture 多目标、synthetic lineage 与 DataFlex feedback controller；daVinci
  的增量是明确区分 processing operator semantics，并用受限 trajectory 说明 mixture/format value 是 model-state
  dependent。Ch24 拥有 pretraining run，Ch25 拥有 SFT/QA boundary，Ch56 拥有 operator checkpoint，Ch62
  拥有 evaluator protocol。暂定 `Refine — Existing Argument (Ch23 owner; Ch24/25/56/62 handoff;
  Experimental; Artifact Partially Available; Historical Books Gate Closed)`；本轮不修改 Books。

### Emergent Social Intelligence Risks in Generative Multi-Agent Systems — 27/30

- **Source Family / Metadata / Revision / Access**：`GENERATIVE-MAS-EMERGENT-SOCIAL-RISK`；
  arXiv:2603.27771 v1 first-public 2026-03-29，v2 revised 2026-04-04。已读 v1 完整 HTML：Introduction、
  formal framework、五阶段 operational lifecycle、15 类 risk sections、全部实验条件/指标/结果、Appendix A～D
  和 conclusion，并核对当前 revision history。未定位到作者 code、data、prompt bundle 或 executable
  environment；论文正文也没有 artifact link。因此为 `Experimental / Artifact Not Available`，不是独立复现。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：single-agent safety 把风险
  归因于一个 model、prompt、tool 或 action，便于建立 component test、least privilege 和 deterministic gate；
  在 agent 独立执行、没有共享资源和跨 agent state 时仍然合理。约束变化在于 Agent 开始反复协商、广播、
  接力、竞争共享 capacity 并按局部 utility 适应：每个 component 都可局部“合理”，collective 仍可能落入
  串谋、资源挤占、错误共识、僵局、角色漂移或语义漂移。风险 owner 因而从单一 Agent 扩展到 interaction
  protocol、information partition、incentive、aggregation、resource rule 与 governance loop 的组合。
- **Mechanism / State Ownership / Control and Data Flow**：论文以 stochastic game 表示 Agent、state、action、
  transition、observation、utility、system objective、information partition、role 与 communication graph，并将
  runtime 分成 initialization、deliberation、coordination、execution 和 adaptation。platform/workflow controller
  应拥有 role、communication topology、system objective、resource/settlement rule、arbitration/escalation 与
  immutable transition log；Agent 只拥有局部 belief、messages、proposal 与被授权 action。典型数据/控制流是
  `local observations + private incentive -> messages/proposals -> aggregation/allocation/handoff -> executable action
  -> externally computed risk indicator -> audit/arbitrate/replan`。若 Summary/Moderator 只压缩消息而不验证
  provenance、约束或 minority evidence，consensus 不能作为 correctness proof。
- **Implementation / Evaluation Contract**：作者构造 15 类 deterministic-environment scenarios，覆盖三 seller
  十轮 Bertrand price game、queueable GPU、shared-capacity task allocation、privileged-information relay、bilateral
  negotiation、news/root-cause majority aggregation、authority-biased clinical pipeline、negotiation deadlock、
  contradictory-instruction trading、clarification/task-allocation failure、warehouse role pressure、20-TFLOPS shared
  server、steganography 与 three-hop advertising handoff。多数条件只改变 communication topology、authority cue、
  group composition、incentive parameter 或 prompt priority，并用外部 rule/indicator 判定；trial 数却随场景变化，
  例如 price game 每条件 5 次、部分 task-allocation 条件只有 3 次、clarification formal experiment 使用 GPT-4o
  并与 GPT-4o-mini 比较、role stability 又比较 Gemini-2.5-Flash 与 GPT-4o-mini。semantic drift/redundancy 使用
  GPT-5 ordinal judge，未报告 temperature、统一 seed policy、API snapshot、token/cost/latency 或置信区间。
- **What the Evidence Proves / What It Does Not Prove**：证据证明这些 interaction-level failure 可以在作者明确
  构造的任务、payoff、topology 与 prompt contract 中被 operationalize，并多次出现；也证明 individual warning
  或“优先系统利益”的 prompt 在部分受控情景中不足以消除失败。它不证明 15 类 taxonomy 完备，不证明真实
  deployment 的发生率，不证明更强模型必然更危险，也不证明所有现象都严格“emergent”：有些条件显式写入
  self-interest、authority、idling penalty 或信息不对称，实验显示的是这些机制与 model policy 的联合结果。
  不同场景、model 和 judge 的结果也不能合并成统一 prevalence estimate。
- **Limitations / Threats to Validity**：论文没有独立 Limitations section。主要边界包括 scenario construct
  validity、small/heterogeneous trial counts、未统一报告 model/runtime/sampling、LLM-as-judge correlated error、
  ordinal rubric 未做人类校准、case selection、无 artifact、无真实 organization/platform baseline、无 longitudinal
  learning、攻击者/合谋者知情边界不一致，以及 mitigation 主要是建议而非 factorial intervention。所谓
  deterministic environment 只固定规则，不固定 stochastic model output；“risk indicator external”也不等于
  indicator 对真实 harm 有充分 calibration。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies**：限制通信、固定 role 或加入 arbitrator
  可减小某些串谋、漂移和僵局，却会增加 token/latency、central bottleneck、authority capture、隐私暴露、错误
  veto 和 over-control；让所有下游看全部中间产物能减少信息丢失，却扩大 context、data exposure 与 review
  burden。mechanism-level resource cap、公平 allocation、typed handoff、provenance、minority channel、quorum、
  conflict escalation 和 human approval 比 prompt warning 更可执行，但也引入 policy ownership、appeal、rollback
  与 liveness 问题。短、低副作用、强顺序且目标一致的任务仍适合 singleton 或 fixed pipeline；并行 Agent 只有
  在 evidence/tool/authority 真正分离且协调税可控时才值得采用。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage / Disposition**：演进为 `single-agent component
  safety -> fixed multi-agent topology -> interaction-aware risk taxonomy -> externally measured collective state ->
  mechanism-level incentive/resource/information constraints -> adaptive clarification/arbitration/replanning ->
  deployment-calibrated governance evidence`，属于 `Layering / Dependency`。已读 Ch78、Ch68、Ch62：Ch78 已有
  correlated consensus、authoritative state、delegation、coordination failures 与 bounded topology repair，本论文的
  增量是把 collective failure 按 incentive / cognition / governance / structural mechanisms 系统拆分；Ch62 已有
  aggregation/judge/EvalSpec，Ch68 已有 sensor/authority 与 run-centric threat boundary。暂定 `Refine — Existing
  Argument (Ch78 owner; Ch62/68 handoff; Experimental; Artifact Not Available; Historical Books Gate Closed)`；
  本轮不修改 Books。

### PRBench: End-to-end Paper Reproduction in Physics Research — 27/30

- **Source Family / Metadata / Revision / Access**：`PRBENCH-PHYSICS-PAPER-REPRODUCTION`；
  arXiv:2603.27646 仅有 v1，first-public 2026-03-29。已读完整 17 页 HTML：Introduction、Related Work、
  task curation/format、AAA/A2A evaluation framework、全部实验与 failure analysis、Appendix A～D 和 conclusion，
  并核对 official project page 与 `HET-AGI/PRBench-Eval-Handson` repository。公开 repository 提供 evaluation
  harness、两个 minimal tests 和一个完整 DMRG sample task，不含论文全部 30 tasks、reference implementations
  或所有 run traces，故状态为 `Artifact Partially Available`，不是 full benchmark reproduction。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：paper QA、formula derivation、
  isolated code generation 与 unit-level benchmark 成本低、failure attribution 清晰，适合测局部能力；当任务只需
  回答知识或实现独立 subroutine 时仍合理。scientific reproduction 的约束不同：Agent 必须把长文中的 method
  转译为算法和数值 convention，在有限 memory/time/dependencies 下实现、debug、执行，并生成与原论文定量
  一致的 artifact。理解分数、代码外观或“运行无异常”都可能与真实科学结果脱钩。
- **Mechanism / State Ownership / Control and Data Flow**：每个 task 将 agent-visible instruction/paper/input 与
  grader-only metadata/reference code/reference CSV 分离；`task.yaml` 拥有 paper identity、expected artifacts、
  Docker image/memory/timeout/dependencies 与 rubric。White Agent 在 fresh container 中生成 analysis/code/data；
  Green Agent 通过 A2A dispatch/poll，求解结束后才注入 ground truth 并运行 grading，随后导出 trace/log/
  workspace 并销毁 container。控制流为 `immutable task spec -> isolated execution -> frozen artifact -> inject
  hidden reference -> criterion scoring + numerical comparison -> hard end-to-end gate -> archived evidence`。
  solver 不能拥有 reference，grader 不能把 Agent 自述当作结果。
- **Implementation / Evaluation Contract**：30 个 tasks 覆盖 11 个 physics subfields，均由 20+ research groups
  的专家执行 reference reproduction 并独立验证；论文筛选要求有 5～10 个可评 target、方法足够 self-contained、
  且在数小时 sandbox budget 内可执行。环境基于 `python:3.11-slim`，每 task memory 2～8 GB、timeout
  800～21600 秒和显式 dependencies。评测 OpenAI Codex/GPT-5.3-Codex 以及 OpenCode + GPT-5.3-Codex、
  GLM-5、Kimi K2.5、DeepSeek V3.2、MiniMax 2.7，每 task 每 configuration 三次。四维权重为 methodology
  0.05、code 0.30、data accuracy 0.60、completeness 0.05；只有四维均 `>0.9` 才计 end-to-end callback。
- **What the Evidence Proves / What It Does Not Prove**：论文在该 30-task selection、agent/framework revision、
  sandbox 与 agentified judge 下显示：较高 methodology/completeness 不保证 code/data correctness，Agent 会出现
  formula factor/sign、algorithm surrogate、method-convention mismatch、silent numerical failure、dense-versus-
  sparse resource error 和 fabricated output。它不证明所有 scientific fields 或真实 research workflow 都同样
  失败，也不证明 model 与 harness 的因果贡献：同一 GPT-5.3-Codex 在 Codex 与 OpenCode wrapper 的差异混合
  tool/harness effects。34% headline 与 0% callback 不能脱离 rubric、`>0.9` hard threshold、task selection、
  three-run policy 和 missing-result aggregation 外推。
- **Limitations / Threats to Validity**：论文没有独立 Limitations section，也未披露 model/API snapshot、
  sampling/token/cost、judge model/prompt/variance、每 task exclusion/missing-result rule、human-judge agreement、
  contamination 或 full task artifact。只选 self-contained、可在数小时和 2～8 GB 内运行、已有 expert
  reproduction 的论文，会排除最模糊、最昂贵或真实依赖最重的研究，也可能提高可执行性；另一方面 30 tasks
  全来自同一学校的 physics groups，不能代表跨机构和跨学科。model judge 同时看 hidden reference code/data，
  仍可能偏好特定 implementation；repository 的单一完整 sample 无法独立复算 Table 2。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies**：隐藏 reference、fresh sandbox 和
  task-specific tolerance 提高 leakage control 与 executable evidence，却新增 task-author bias、reference bug、
  over-specified path、judge injection、container/runtime drift、昂贵重复执行与 archive/privacy 成本。CSV 避免
  figure vision error，但可能丢掉物理解释；flat weighted score便于诊断，hard callback gate 防止致命维度被平均
  掩盖，二者应并存。unit tests、formula QA 与 isolated code benchmark 继续适合开发期定位；end-to-end
  reproduction 是更高层 integration gate，不替代局部 test。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage / Disposition**：演进为 `paper QA -> formula /
  subroutine benchmark -> structured analysis/code/data artifact -> isolated end-to-end execution -> hidden expert
  reference + task-specific tolerance -> criterion diagnostics + hard callback gate -> cross-domain/production research
  validation`，属于 `Direct Evolution + Layering / Dependency`。已读 Ch62，并核对 Ch61/63 的 resource/
  observability handoff。Ch62 已明确拥有 Benchmark/Evaluation/Testing 分层、`artifact + environment + trace`、
  executable verifier 非 ground truth、rubric formation/execution/aggregation/decision 和 hard release gate；PRBench
  没有新增尚未覆盖的 first principle。因此为 `No Change — Already Covered (Ch62 owner; Ch61/63 handoff;
  Experimental; Artifact Partially Available; Historical Books Gate Closed)`，本轮不修改 Books。

### MuSEAgent: Multimodal Reasoning with Stateful Experiences — 28/30

- **Source Family / Metadata / Revision / Access**：`MUSEAGENT-STATEFUL-MULTIMODAL-EXPERIENCE`；
  arXiv:2603.27813 仅有 v1，first-public 2026-03-29。已读完整论文的 Introduction、Related Work、method、
  algorithms、全部 experiments/ablations、tool/prompt appendices 与 conclusion，并核对 official repository 的
  trace/state bank、tools、configuration 和 evaluation datasets。artifact 可访问但本次没有独立重跑，故
  `Artifact Available` 只表示公开面完整度，不表示结果已复现。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：整条 trajectory 保存了
  跨步因果上下文、环境反馈和失败过程，适合 replay、审计及短而稀疏的 episode；它也是 derived memory 出错时
  可回溯的原始证据。多模态长轨迹的约束发生变化：同一 episode 包含大量与当前 action 无关的图像、历史和
  工具结果，整段检索容易把局部可执行 guidance 淹没在低密度上下文里。问题不是“历史越短越好”，而是
  inference-time action 需要与当前 state 对齐的经验粒度，同时不能丢失原始 provenance。
- **Mechanism / State Ownership / Control and Data Flow**：exploration run 拥有原始 trajectory，并将其拆为
  `(s_t, a_t, s_{t+1})` transitions；hindsight model 为每个 transition 生成 quality score `q` 与 guidance `g`，
  只保留 `q >= 5` 的 derived experience。memory store 保存 transition、guidance 与 query/image/task/history
  等多 view embeddings；推理先由当前 state 选择检索 view，再以 Deep/Wide search（作者默认 `K=3, L=3`）
  聚合经验，将 guidance 作为 advisory context 注入下一 action。合理的 production ownership 应把 raw trace、
  extractor/judge revision、derived record、index revision 与 consuming policy 分开；公开实现尚未提供完整
  provenance、supersession、delete、online invalidation 和 policy-authority contract。
- **Implementation / Evaluation Contract**：base agents 为 Qwen3-VL-32B、Qwen3-VL-235B-A22B 与
  Qwen3.5-397B-A17B；GPT-4o 负责 hindsight，Qwen3-VL-8B 生成 embedding，环境提供 13 个 tools。四个
  multiple-choice VQA benchmarks 使用 1:1 exploration/evaluation split，并与 CoT、ReAct、Reflexion、Expel
  对比；实验覆盖 experience source、hindsight model、quality threshold、search depth/breadth 与 OOD transfer。
  论文未披露 hardware、precision、latency/cost、并发/SLO、multi-seed variance 或完整失败重试 contract。
- **What the Evidence Proves / What It Does Not Prove**：作者实验支持的是：在上述模型、工具、四个 VQA
  数据集和 split 下，state-level derived experience 配合多 view retrieval 优于被测整轨迹/反思 baselines，且
  quality filter 与 search configuration 会改变结果。它不证明 atomic transition 是充分或因果最优的 memory
  unit，不证明约 8% headline 可迁移到 coding、开放 Web、长期任务或生产 workload，也不能把 OOD 子集表现
  解释为通用 memory transfer。hindsight judge 同时控制 admission 与内容生成，收益可能混合 teacher quality、
  retrieval 与额外 prompt compute。
- **Limitations / Threats to Validity**：四个任务均为 multiple-choice VQA，固定 1:1 split 不能覆盖在线环境
  drift、不可逆 tool side effects 或长期 state mutation。没有 seeds/confidence interval、matched token/latency
  budget、人工核验 guidance quality、poisoning/adversarial memory、staleness 或 delete/rollback 评测。GPT-4o
  既评分又生成 guidance 会产生相关误差和 selection bias；阈值拒绝的经验也可能包含 rare-but-critical failure。
  online construction 被作者列为 future work，因此本文不能证明边执行边写 memory 的 consistency。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies**：更细粒度记录提高局部检索和 token
  效率，却会切断跨 transition 依赖、放大 extractor 错误并增加 index、dedup、freshness 与 governance 成本；
  更深/更宽 search 增加 recall，也增加无关 guidance、latency 和 context competition。完整 trajectory 在 forensic
  replay、高风险审计、长程 credit assignment 和 derived memory 不可信时仍成立；短任务或经验稀少时，直接
  prompt/trajectory retrieval 也更简单。derived memory 应是可撤销的 proposal layer，而不是未经验证的 authority。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage / Disposition**：演进为 `raw trajectory archive
  -> whole-trajectory retrieval -> transition extraction -> hindsight-derived procedural memory -> multi-view
  state-level retrieval -> provenance/supersession/online invalidation governed memory`，属于 `Direct Evolution +
  Layering / Dependency`。已读 Ch73/76，并核对 Ch72/74/62 handoff；Ch73 已有 raw history → derived procedural
  memory、provenance 与 supersession，本文的增量是 transition granularity、multi-view selection 与 Deep/Wide
  retrieval 的机制化案例。暂定 `Refine — Existing Argument (Ch73 owner; Ch72/74/76/62 handoff;
  Experimental; Artifact Available; Historical Books Gate Closed)`；本轮不修改 Books。

### KAT-Coder-V2 Technical Report — 29/30

- **Source Family / Metadata / Revision / Access**：`KAT-CODER-V2-AGENTIC-POSTTRAINING`；arXiv:2603.27703
  仅有 v1，first-public 2026-03-29。已读完整 22 页 HTML：KwaiEnv、五类 domain data/SFT、Agentic RL、
  modified turn-level objective、MCLA、KRL/Tree Training/high-concurrency pipeline、on-policy distillation、
  全部 evaluation tables、conclusion 与 references，并核对 official hosted-product 及 Kwaipilot public surface。
  V2 是 hosted model；论文没有给出对应 weights、KwaiEnv/KRL code、training data 或 run traces，故为
  `Implementation Not Disclosed`，不是 open artifact。
- **Original Problem / Why the Previous Design Was Reasonable / Changed Constraint**：单一 mixed-domain
  SFT/RL pipeline 的 checkpoint、deployment 和 evaluation 简单，在 domain signals 一致、能力边界窄时仍合理。
  Agentic coding 将 SWE repair、frontend aesthetics、terminal execution、web search 和 general reasoning 放入
  不同 environment/tool/verifier/scaffold，训练信号会冲突；长程多轮又使 sequence-level credit 过粗、token-level
  importance ratio 方差高，branching trajectory 则重复计算 shared prefix。约束变化要求先保持 domain-specific
  optimization，再解决统一部署、概率估计和树状训练成本，而不是假设一个 objective 同时最优。
- **Mechanism / State Ownership / Control and Data Flow**：KwaiEnv 将 RL sample 表示为
  `<environment, tools, scaffold/system prompt, task instruction, verifier>`，分别由 Dataset、Verifier、Scaffold、
  Sandbox、Trajectory Manager 管理；网络 proxy 记录 I/O、tool calls、token 与 timestamp，Trajectory Manager
  转换为 RL input。五个 experts 各自经 domain data、SFT 与 environment-feedback RL；unified student 在 mixed
  prompts 上生成自身 trajectories，environment reward 提供 sparse outcome，按 task 选择的 expert 对 student
  visited states 提供 dense logprob supervision。KRL 在 sandbox rollout、SGLang inference、reward/packing、
  SGLang→Megatron engine switch、update 和 weight sync 之间循环；policy/scaffold/verifier/environment revision
  都应进入 trajectory identity。
- **Algorithm / Implementation Details**：modified GSPO 在 scaffold markers 划分的 interaction turn 内聚合
  token probability ratio，再逐 turn clipping，使 credit granularity 位于 token 与整 trajectory 之间。MCLA 对
  每条 trajectory 重复 `K=8` 次 training forward/prefill 后平均 logprob，并与 IcePop 的 excessive-discrepancy
  clipping 分工：前者降低 estimator variance，后者约束 rollout/training mismatch。Tree Training 将所有
  root-to-leaf paths DFS flatten，用 tree attention mask、原始 per-token position IDs 与 loss weights 保持分支
  可见性及 gradient aggregation；它复用 shared prefix，但正确性依赖 mask、position、weight 和 kernel 支持。
- **Evaluation Contract / What the Evidence Proves**：论文在 KwaiEnv 上报告 SWE-bench Verified/Multilingual、
  SWE-rebench-V2 subset、PinchBench、Claw-Eval、三类内部 frontend aesthetics、Terminal-Bench Hard、tau2-Bench、
  AA-LCR 与 IFBench；scaffolds 包含 Claude Code/OpenCode/OpenClaw，部分对手数字来自厂商或第三方页面。
  证据支持该完整 pipeline 产出的 hosted model 在作者所列 harness 下具有跨 scaffold/domain 能力，并给出
  tree-shaped shared-prefix reuse 的可行机制。它没有 factorial ablation 将 specialization、turn objective、MCLA、
  Tree Training、KwaiEnv scaling 和 OPD 的因果贡献拆开，也没有公开数据让 6.2×/2.8× 或 benchmark ranking
  被独立重算。
- **What It Does Not Prove / Limitations / Threats to Validity**：论文没有独立 Limitations section，也未披露
  base/model architecture、total/active parameters、training tokens、GPU type/count/topology、precision、batch、
  optimizer schedule、wall time/cost、seeds/variance、MCLA overhead、Tree Training workload breakdown 或
  teacher/judge identity。merged PR 只是弱 correctness proxy，内部/proprietary data 与 frontend benchmark
  限制 contamination 和公平比较核验；不同 competitor scores 来自不同来源。作者称 OPD dense target
  “unbiased”不足以证明整个 mixed RL+distillation update 无偏，teacher selection 与 student visitation 都会
  改变 target distribution；MoE noise 归因也缺少 matched ablation。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies**：domain experts 减少 objective
  interference，却增加 checkpoint、teacher selection、rollout、evaluation 与 capacity cost；统一 student 降低
  serving complexity，却会损失 specialist upper bound并引入 cross-domain forgetting。turn-level ratio改善局部
  credit，但 turn boundary 随 scaffold marker 漂移且同一 group advantage 仍未形成真正 step return；MCLA
  用约 8 次 forward 换 variance，收益可能被额外 compute 抵消；Tree Training 节省 prefix 重算，却扩大 mask/
  position/loss-weight/kernel correctness surface。单一 mixed policy、sequence-level update 和独立 root-to-leaf
  training 在 domain 少、trajectory 短、分支少或可审计性优先时仍合理。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage / Disposition**：演进为 `single-domain static
  code data -> executable environment-feedback RL -> multi-scaffold workload identity -> domain-specialized SFT/RL
  -> student-on-policy expert distillation -> turn-granular policy update + MoE estimator control -> tree-aware shared-
  prefix training -> artifact-complete causal/runtime validation`，属于 `Direct Evolution + Layering / Dependency`。
  已读 Ch29 及相邻 Ch28/30，并核对 Ch36/56/77/62：Ch29 已有 sequence/token objective、cross-policy reuse、
  policy identity 与 lag，但没有把 turn boundary、repeated-logprob estimator、tree trajectory training 和
  student-on-policy expert fusion 放进同一机制链。暂定 `Integrate — New Mechanism (Ch29 owner;
  Ch36/56/77/62 handoff; Experimental; Implementation Not Disclosed; Historical Books Gate Closed)`；本轮不改 Books。

### LongCat-Next / DiNA native discrete autoregressive multimodality — 29/30

- **Source Family / Metadata / Revision / Access**：`LONGCAT-NEXT-DINA-NATIVE-MULTIMODALITY`；
  arXiv:2603.27538 仅有 v1，first-public 2026-03-29。已读完整 HTML 的 Background、Method、model/
  tokenizer architecture、training stages、全部主实验、methodology analysis、implementation/data details、
  multimodal RL、VHalf pipeline、quantization/mismatch appendices，并核对官方 GitHub 与 Hugging Face
  model card。weights、tokenizer、inference 与 FSDP2 SFT code 可访问，但完整 pretraining/data/runtime
  implementation 未公开，状态为 `Artifact Partially Reproducible`。
- **Original Problem / Why Previous Designs Were Reasonable / Changed Constraint**：连续 visual/audio encoder
  feature 经 projector 接入 LLM，在数据少、目标以理解为主时能复用成熟 representation，避免 codec 重建
  成本，仍是合理方案。但它把理解与生成放在不同 interface，难以让单一 causal backbone 对所有 modality
  使用一致 next-token objective。若系统要同时理解和生成 image/audio/video，约束变成：每种 modality 既要
  压缩为可预测 ID，又要保留语义、低层细节、时间结构与可重建性，且不能让 modality branch 吞掉 backbone
  的通用 reasoning capacity。
- **Mechanism / State Ownership / Control and Data Flow**：DiNA 让 modality-specific tokenizer/detokenizer
  拥有 raw signal ↔ discrete IDs 的 codec state；dNaViT 的 semantic-aligned encoder、residual path 与 8-level
  RVQ 分别保存高层语义、低层 residual 与 hierarchical code identity；shared LongCat-Flash-Lite A3B
  backbone 只接收统一 token stream 并执行 next-token prediction；DepthTransformer、pixel/audio decoder 与
  refiner 拥有 modality-specific reconstruction。image path 是 `pixels -> semantic/residual encoder -> RVQ
  code levels -> summed code embeddings -> shared AR backbone -> multi-level code head -> decoder/refiner`；
  audio path用 Whisper encoder、8-level RVQ 与 text-guided random delay 支持 parallel/serial interleaving。
- **Architecture / Training / Implementation Details**：backbone 为 68.5B total、平均约 3B active 的 zero-expert/
  shortcut MoE；vision codebook 为 `8 × 16,384`，audio codebook 依层为 8K/4K/2K/1K 等。训练先独立训练
  tokenizer，再冻结 backbone 预对齐，最后冻结 tokenizer 做 end-to-end warmup/pretrain/mid/SFT；论文报告
  约 2T multimodal tokens，四阶段 batch 为 8192/8192/1024/128，sequence length 为 8K/8K/32K/64K。
  Multimodal RL 把离散 image tokens 作为 action，并使用 multi-level GRPO 与多 reward；sequence filter
  根据 entropy 与逐 token 概率差剔除严重 train/inference mismatch。VHalf pipeline 把开头 embedding 与
  末端 modality loss 折叠到同一 physical device，共享 buffer，并 profile-guided 分配 chunks/layers。
- **Evaluation Contract / What the Evidence Proves**：作者在理解、image generation/editing、video、speech
  understanding/generation 与 unified-task benchmark 上比较连续/离散 variants，并在缩小的 Qwen-7B 设置做
  data scale、semantic alignment、RVQ depth、unified training 与 mismatch ablation。证据支持：在本文模型、
  tokenizer、数据和 scorer 下，更多数据能缩小 discrete 相对 continuous 的差距，semantic-aligned residual
  code 优于被测 alternatives，统一训练可在部分任务形成协同；routing trace 也显示 modality-correlated expert
  utilization。它不证明离散 token 普遍优于连续 feature，不证明 route observation 是固定语义 expert，亦不
  证明 VHalf 在未披露硬件与 workload 上具有通用吞吐收益。
- **Limitations / Threats to Validity**：训练 GPU type/count/topology、precision、wall time/cost、seeds/
  variance 与 VHalf throughput/latency/concurrency/SLO contract 未披露；部分训练数据与完整 pipeline 不可用。
  benchmark 混用 external scorer/model，污染检查只覆盖公开的 pHash/n-gram 边界。论文没有独立完整
  Limitations section。稀有 token 的 train/inference mismatch 可触发 entropy collapse；整条 sequence filtering
  虽能延迟问题，也可能丢弃 rare-but-valid path 并引入 selection bias。quantization、codebook drift、codec/
  backbone version skew、长离散序列与 modality loss imbalance 都是新增 failure surface。
- **Trade-offs / Where Previous Designs Still Apply**：统一离散协议换来同一 AR objective、生成/理解共享和
  conditional-compute reuse，却支付 tokenizer training、quantization fidelity、序列长度、decoder/refiner、
  codebook governance 与 mismatch-control 成本。continuous feature projection 在 data/compute 少、只做理解、
  latency 或 fine-grained fidelity 优先时仍合理；独立 modality model 在专用 quality、streaming 或安全隔离
  更重要时仍成立。VHalf 也不是传统 PP 的替代：boundary module 不重或 topology 不支持 folding 时，规则
  stage placement 更简单、更可预测。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage / Disposition**：演进为 `continuous modality
  feature projection -> discrete modality codec -> semantic-aligned hierarchical residual codes -> shared
  autoregressive multimodal backbone -> emergent conditional routing -> workload-aware PP and RL mismatch
  control -> artifact-complete validation`，属于 `Direct Evolution + Layering / Dependency + Alternative
  Branches`。已读 Ch11/12，并核对 Ch21/29/34；现有 Ch11 只覆盖 text tokenization，缺少“tokenizer 是跨
  modality 可版本化 input/output protocol”的机制分支。暂定 `Integrate — New Mechanism (Ch11 owner;
  Ch12/21/29/34 handoff; Experimental; Artifact Partially Reproducible; Historical Books Gate Closed)`。
  Books Gate 通过前不修改正文；若最终 owner 需要改变 Ch11 的 text-only 边界，则作为结构性 review 项，
  不在本周擅自扩章。

### mSFT: Addressing Dataset Mixtures Overfitting Heterogeneously — 28/30

- **Source Family / Metadata / Coverage**：`MSFT-HETEROGENEOUS-STOPPING`；arXiv:2603.21606 v1，
  first-public 2026-03-23。已读 Introduction、motivation、算法与公式、四类 baseline、main results、
  ablation/sensitivity、discussion、hardware/training appendix、FLOPs 与 checkpoint-storage appendix。
- **Original Problem / Previous Design / Changed Constraint**：随机混合的 SFT 用统一 global compute
  budget，可避免 sequential training 的 catastrophic forgetting，且实现简单；但任务分布与收敛速度
  不同，单一 stopping point 会同时让快任务过拟合、慢任务欠拟合。预先测一次各任务 optimum 也不够，
  因移除任务会改变 aggregate gradient 和其余任务的最佳停止点。
- **Mechanism / State / Flow**：controller 保存 active dataset set、各 task held-out metric、compute
  cursor 与 rollback checkpoint。每轮在 active mixture 上 rollout `C`，找到最早过拟合任务，回退到
  该任务 peak checkpoint、将其从 mixture 排除，再在新的 gradient field 上重算其余 stopping point。
  参数与 optimizer/checkpoint state 由 training controller 持有；dataset scheduler 只改变 active set。
- **Evaluation Contract / Proof Boundary**：6 个 0.5B～8B base models、10 个 QA benchmarks、4 个
  baseline，greedy 5-shot，每 1/4 epoch 评估；默认每子集 1,800 samples、batch 64、LR `1e-5`，硬件含
  B200/H200/RTX A5000/3090。主实验大多单 seed，Qwen2.5-3B 补做 3 seeds。证据支持“这些受控 mixture
  中 task-optimal compute 异质且 iterative rollback 优于被测 baseline”，不证明真实大规模 SFT 都应
  hard-drop dataset，也不证明 held-out benchmark 可以安全充当生产 stopping oracle。
- **Trade-offs / Failure Modes / Old Design**：多次 rollout、评测泄漏风险、task boundary 质量与约
  4.44× SFT checkpoint footprint 是新增成本；hard exclusion 也可能丢失继续抑制 forgetting 的梯度。
  单一 global budget 在任务动态相近、evaluation 不可靠或 checkpoint/storage 紧张时仍合理。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch24～26。Ch25 已覆盖 mixture、mask 与 data quality，
  尚未拥有“task-level stopping point 会随 active mixture 改变”的控制机制。`Integrate — New Mechanism
  (Books Gate Pending)`；关系为 `Direct Evolution`，当前不改 Books。

### On the Direction of RLVR Updates for LLM Reasoning — 28/30

- **Source Family / Metadata / Coverage**：`RLVR-SPARSE-DIRECTIONAL-UPDATES`；arXiv:2603.22117 v1，
  first-public 2026-03-23。已读 RLVR/GRPO background、统计识别、token replacement、test-time
  extrapolation、training-time reweighting、相关工作与 implementation/sensitivity appendix。
- **Problem / Previous Design / Changed Constraint**：entropy、KL 或 gradient norm 适合回答 update
  “多大”，但不能区分 token 是被 base 还是 RL policy 偏好。当 RLVR 改变集中在少量 token 时，方向
  信息可能比幅度更能定位因果关键位置。
- **Mechanism / Flow**：对同一 prefix 比较 base 与 RL policy，计算 signed token-level
  `Δlog p = log π_RL - log π_Base`；在 intervention 中先从 base 采样，仅在阈值触发位置改由 RL policy
  采样。由此又派生两条实验分支：test time 沿该方向有界 extrapolate，或在 DAPO 中对低概率 token
  重加权 advantage。base/RL checkpoint pair、prefix、threshold 与 sampling seed 都是实验身份。
- **Evaluation / Proof Boundary**：论文使用 ORZ/DAPO 的 Qwen2.5-32B pair 与 UniReason Qwen3-14B
  pair，在 AIME24/25、AMC 等 math tasks 上比较 entropy、KL、random replacement、threshold 与
  `gamma` sensitivity。它支持“这些 model pairs 中 signed difference 更精确识别少量关键 token”；
  不证明该方向是可迁移 reasoning vector，也不证明低概率 token 普遍应获得更大权重。理论依赖理想化
  NPG 与 monotonic update 假设。
- **Trade-offs / Failure Modes / Old Design**：推理时需同时访问 base/RL distributions，增加 memory、
  compute 与 threshold calibration；training reweighting 可能放大低概率噪声或 verifier bias。标准
  GRPO/DAPO 在缺少 paired checkpoint、任务非 verifiable 或收益不抵额外复杂度时仍成立。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch28～30。Ch29 已覆盖 sequence/token objective、
  verifier 与 sampling contract，但尚未把 magnitude-vs-direction intervention 纳入 evidence ladder。
  `Refine — Existing Argument (Books Gate Pending)`；关系为 `Principle Reuse + Mechanism Extension`。

### Scaling DoRA: High-Rank Adaptation via Factored Norms and Fused Kernels — 28/30

- **Source Family / Metadata / Coverage**：`DORA-FACTORED-NORM-KERNEL`；arXiv:2603.22276 v1，
  first-public 2026-03-23。已读 DoRA formulation、factored norm 推导、three-tier dispatch、Triton
  kernels、model/micro benchmarks、convergence、limitations、kernel specs、reproducibility 与 framework survey。
- **Problem / Previous Design / Changed Constraint**：LoRA/DoRA 的 dense `B@A` materialization 在低 rank
  与充足显存时简单、兼容；rank 提高、适配模块增多和 gradient checkpoint recompute 后，逐模块 dense
  temporary 与反复 memory traffic 会成为累积瓶颈，而非模型权重本身的单次 OOM。
- **Mechanism / State / Flow**：将 `||W+sBA||²` 展开为 base、cross 与 Gram 三项，只保留
  `O(d_out*r+r²)` intermediate；compose/backward/norm assembly 用 Triton 融合。runtime 依据 training、
  CUDA/Triton availability、shape crossover 与 forced policy 选择 fused backward、fused forward 或 eager
  fallback；precision path 与 compatibility guard 是 dispatch state，而不是 kernel 内隐假设。
- **Evaluation Contract / Proof Boundary**：6 个 8B～32B VLM、rank 384、bf16，在 RTX 6000 Pro、H200、
  B200 上做 model-level measurement，并在 6 类 GPU 上做 microbenchmark；单卡 Qwen3.5-9B、2000-step、
  3-seed convergence 绑定 RTX 6000 Pro、seq 5120、batch 3、GA 2。作者数字证明这些实现/shape 的 memory
  与时间收益，不证明所有 LoRA/DoRA rank、非 CUDA 后端或 distributed sharding 都有相同 speedup。
- **Trade-offs / Failure Modes / Old Design**：小 activation 受 launch latency 主导；Triton 与 PyTorch
  非 bitwise identical；FSDP2/DTensor 因 full base weight assumption 尚不支持；embedding formula
  compatibility 可能要求 legacy fallback。作者列出的 colocated GRPO/vLLM 场景只是未纳入方法学的案例。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch25～27，并核对 Ch45 runtime/kernel 边界。Ch26
  已解释 LoRA，但缺少“数学等价式决定 intermediate complexity，runtime dispatch 保留兼容旧路径”的
  系统机制。`Integrate — New Mechanism (Books Gate Pending)`；Ch26 为 owner，Ch45 只短 handoff。

### Effective Strategies for Asynchronous Software Engineering Agents / CAID — 28/30

- **Source Family / Metadata / Coverage**：`CAID-BRANCH-MERGE-AGENTS`；arXiv:2603.21489 v1，
  first-public 2026-03-23。已读 branch-and-merge architecture、dependency scheduling、Commit0-Lite/
  PaperBench setup、single-agent control、worktree/agent-count ablation、failure examples 与 prompts。
- **Problem / Previous Design / Changed Constraint**：单 Agent 保持统一 context 与简单 ownership，在强
  顺序任务仍合理；长时软件任务若存在可分解模块，则只延长单 Agent iteration 不一定产生相同收益。
  多 Agent 仅靠自然语言约定“不改同一文件”又无法隔离共享 artifact 的并发冲突。
- **Mechanism / State / Flow**：central manager 先构造 dependency DAG，只委派 ready nodes；每个 engineer
  拥有独立 git worktree，完成实现、自验与 commit。completion event 回到 manager，manager merge 后更新
  authoritative completed set，再释放下游任务，最后统一 review。DAG/completed set/main branch 属于
  coordinator；worktree/branch/commit 属于 worker；merge result 才是共享 artifact state。
- **Evaluation / Proof Boundary**：OpenHands SDK v1.11.0，GLM 4.7、MiniMax 2.5、Claude Sonnet 4.5；
  PaperBench 用 Code-Dev protocol，主设置 2 engineers，Commit0 用 4 engineers，并与同 substrate 的
  100-iteration single Agent 对照。结果支持这两个 benchmark/config 下 branch-and-merge 的增量价值，
  不构成跨 framework 的排名，也不证明增加 Agent 数量单调提升；8-engineer 与弱结构任务出现退化。
- **Trade-offs / Failure Modes / Old Design**：cost、iterations、merge conflict 与 manager bottleneck 均
  增加；错误 delegation 会阻塞 dependency 或放大无效并行。单 Agent + deterministic verifier 在任务
  不可分、shared-state side effect 强或 coordinator headroom 不足时仍是更小且可靠的系统。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch77、Ch78、Ch80。Ch78 已有 coordination tax、
  task-topology matching 与 typed shared state，因此不是全新结论；CAID 补足 branch-and-merge 的 state
  ownership 实例。`Refine — Existing Argument (Books Gate Pending)`；关系为 `Layering / Dependency`。

### SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and Planning — 27/30

- **Source Family / Metadata / Coverage**：`AGENTIC-SPECULATIVE-ROUTING`；arXiv:2603.23483 v1，
  first-public 2026-03-24。已读 agentic-depth model、four-phase funnel、answer-separability gate、
  heterogeneous serving、main results、threshold/batch/Top-K ablation、future work 与官方代码入口。
- **Problem / Previous Design / Changed Constraint**：token-level speculative decoding、token pruning 与
  KV compression 在固定 trajectory 内减少单步成本，语义边界清楚；但 multimodal Agent 的下一次 crop/
  OCR/tool action 依赖上一次 observation，tool-loop depth 仍构成 request 内串行 critical path。
- **Mechanism / State / Flow**：large agent 先输出 tool-necessity binary judgment；判定 tool-free 的请求由
  Qwen3-VL-2B stateless draft 直接给出 answer/logits；answer-separability gate 达阈值则接受，否则回退
  DeepEyes/Thyme 的最多 5-step agentic loop。每请求 tool trajectory 由 large Agent 持有；small model
  无 tool state；router 持有 threshold、accept/fallback decision 与 residual queue。
- **Evaluation Contract / Proof Boundary**：V* 两个子集、HR-Bench 4K/8K、POPE 三个 split，greedy
  decoding，Qwen3-VL-2B draft，DeepEyes/Thyme target；threshold 逐 benchmark 离线取样，全部实验为
  单张 A100 40GB，latency 包含 tool time。作者的 1.08～3.35× 只证明该模型、硬件、benchmark 与
  calibration 的 operating points；没有多 GPU、真实 tool-service variance、尾延迟、跨分布 calibration
  或 side-effecting action 证据。
- **Trade-offs / Failure Modes / Old Design**：这是 lossy routing，不是 target-model exact verification；
  false accept 会绕过原 agentic trajectory，false fallback 浪费 draft/judge work。benchmark-specific
  threshold、large-model pre-judge 与 residual queue 也会增加 admission cost、fairness 和 calibration
  drift。难题比例高时保留完整 tool loop 更合理。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch44、Ch62、Ch77/78。Ch44 已有 exact-vs-lossy
  speculation boundary，Ch77 已拥有 durable state，但尚未明确“先猜整个 workflow 是否必要”的
  heterogeneous funnel。`Refine — Existing Argument (Books Gate Pending)`；owner Ch77，关系为
  `Principle Reuse`，并须显式标记 `Experimental`。

### From Static Templates to Dynamic Runtime Graphs — 24/30

- **Source Family / Metadata / Coverage**：`AGENT-WORKFLOW-OPTIMIZATION-TAXONOMY`；arXiv:2603.22386
  v1，first-public 2026-03-23。已读 scope/inventory、ACG formalization、static/dynamic methods、feedback
  signals、evaluation/reporting、synthesis、open problems、classification appendix 与 companion repository。
- **Problem / Previous Design / Changed Constraint**：固定 code-defined workflow 便于审查、复现与强
  verifier 约束；但 tool drift、输入异质性与运行时 observation 会让单一模板暴露结构边界。此前论文又
  常把 prompt、topology、run graph 与 trace 混称为“workflow improvement”，使增益无法归因。
- **Mechanism / State / Flow**：survey 将 reusable template `G_bar`、每次执行的 realized graph
  `G_run` 与 trace `tau=(state, action, observation, cost)` 分离；再按 structure determination time、
  node-vs-graph optimization、feedback signal 组织 static search、runtime selection/generation/editing。
  template owner、runtime scheduler 与 evidence store 因而必须是不同 contract。
- **Evidence / Proof Boundary**：inventory 含 39 core、7 adjacent、31 background works，另列 27 个
  evaluation assets。它提供跨论文 taxonomy 和 reporting protocol，不提供统一 benchmark 或因果
  meta-analysis；“static 何时足够、selection 何时优于 generation”只是作者对异质证据的 synthesis，
  不是 universal law。
- **Trade-offs / Failure Modes / Old Design**：dynamic graph 增加 structural credit assignment、IR
  expressivity-vs-verifiability、runtime repair 与 drift recovery 成本；结构不同但语义相同还需要
  canonicalization。API 稳定、operator space 受限、verifier 强且 workload 重复时，优化过的 static
  scaffold 仍可能优于 runtime generation。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch77、Ch78、Ch80。Ch77 已有 workflow identity、
  durable state 与 Helium DAG handoff，但未明确区分 template / realized graph / trace。`Integrate — New
  Conceptual Boundary (Books Gate Pending)`；owner Ch77，survey 只作 synthesis evidence，不复制论文表格。

### Sparse but Critical: Token-Level Distributional Shifts in RLVR — 29/30

- **Source Family / Metadata / Coverage**：`RLVR-SPARSE-DIRECTIONAL-UPDATES`；arXiv:2603.22446 v1，
  first-public 2026-03-23，ICLR 2026。已读 token distribution analysis、forward/reverse cross-sampling、
  fine-grained mechanics、divergence-weighted advantage、related work、sequence bounds、完整实验 appendix
  与附加模型/clip/top-p sensitivity。
- **Problem / Previous Design / Changed Constraint**：sequence reward、aggregate KL 与 parameter norm
  能描述训练整体变化，却不能定位哪些 conditional distributions 改写了 reasoning trajectory。纯相关性
  的 high-divergence 分析也不能证明这些位置具有功能作用。
- **Mechanism / State / Flow**：在相同 prefix 上计算 base/RL token distribution 的 JS divergence；
  forward cross-sampling 从 base 生成，在超过阈值的位置换用 RL distribution；reverse path 反向替换。
  intervention budget 控制替换次数，mixed-policy prefix 会反过来改变后续位置。论文另用 detached
  old-policy KL 作为 sampled-token proxy 对 advantage 加权，但明确是 exploratory extension。
- **Evaluation / Proof Boundary**：主分析为 Qwen2.5-32B SimpleRL/DAPO，在 AIME24/25 与 fine-tuning
  data 上以 vLLM、top-p 0.7、temperature 1 采样并报告 Mean@32；appendix 扩展 Qwen3-8B、Mistral-
  Small-24B、GPQA、clip/top-p variants。公开正文未披露主要 inference hardware/seeds；一条 Qwen3-32B
  DAPO 附加 run 超过 140k GPU-hours，作者也未继续研究 delayed improvement。因此不能把阈值、稀疏
  比例或训练成本外推为通用常数。
- **Trade-offs / Failure Modes / Old Design**：cross-sampling 需要成对 checkpoint 和两套分布，且
  intervention 改变 prefix 后不再是固定-context attribution；sampled-token KL 不能替代 full-vocabulary
  divergence，重加权还可能放大 verifier/noise。标准 sequence-level advantage 在缺少可靠 token evidence
  时仍更稳健。论文支持“RLVR 多在 base plausible alternatives 间 re-rank”，不证明 RLVR 从不产生新能力。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch28～30，并与同周 `On the Direction` 联读。Ch29
  已说明 sequence-to-token credit 粗糙；两篇论文共同补出 magnitude、direction 与 causal intervention
  三层证据。`Refine — Existing Argument (Books Gate Pending)`；同 family 保留两个候选，因为研究问题
  与 intervention 不同。

### Thinking Deeper, Not Longer: Depth-Recurrent Transformers — 25/30

- **Source Family / Metadata / Coverage**：`DEPTH-RECURRENT-TRANSFORMER`；arXiv:2603.21676 v1，
  first-public 2026-03-23。已读 background、shared-weight recurrence、三类 perception interface、
  supervision/stability mechanism、三项 compositional-generalization experiment、ablation、limitations 与
  architecture/depth-embedding appendix。
- **Original Problem / Previous Design / Changed Constraint**：固定 `L` 层 Transformer 让参数容量、训练
  graph 与每个样本的执行深度绑定，便于 dense batching 与 checkpoint/runtime 实现；但若任务的顺序组合
  深度显著变化，固定一次前向无法为难样本增加内部迭代，也会把更深推理等同于增加参数层或生成更多
  visible tokens。
- **Mechanism / State / Flow**：一个共享参数 Transformer block 在 full-sequence hidden state 上循环
  `T` 次，最终一步才计算监督；训练从 task-specific interval 随机采样 `T`。Pre-LN、初值 `1e-4` 的
  LayerScale 与 bias `-2` 的 GRU-like gate 让初始路径偏向 identity；depth embedding 区分 recurrence
  step。perception interface、recurrent hidden state、step counter/budget 与 readout 是不同状态边界。
- **Evaluation Contract / Proof Boundary**：小于 1M 参数的受控 graph reachability、nested Boolean 与
  CLUTRR-style relational text；graph 在 1～5 hop 训练、最多 12 hop 测试，8 hop 前可达 perfect 后于
  10 hop collapse；Boolean 在 depth 14 仍高于 90%，并测试到 24 steps。结果支持受控任务中的
  computation frontier 与 recurrence stability，不证明可直接替换 pretrained decoder-only LLM，也不
  证明“更多 silent steps”在开放语言任务上单调提升。graph 结果还依赖手工 adjacency mask。
- **Trade-offs / Failure Modes / Old Design**：共享权重降低参数增长，却增加顺序 critical path、activation/
  recurrent-state residency、per-request stop rule 与不同 `T` 的 batching divergence；learned depth
  embedding 还把可外推步数约束在已分配表范围。固定深度在吞吐优先、任务深度窄、停止证据不足时仍
  更可预测；visible CoT 保留可观测 supervision 与 verifier 接口。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch16～18。Ch17 已把 block 定义为可堆叠 state update，
  但没有区分 parameter depth 与 execution depth。`Integrate — New Mechanism (Books Gate Pending)`；
  owner Ch17，关系为 `Direct Evolution`，状态 `Experimental`。

### Counterfactual Credit Policy Optimization for Multi-Agent Collaboration — 26/30

- **Source Family / Metadata / Coverage**：`MULTI-AGENT-ROLE-CREDIT`；arXiv:2603.21563，v1 first-public
  2026-03-23；当前 v5（2026-06-11）用于方法与限制核验，未将后续 revision 当成 W13 新事件。已读
  formulation、CCPO/SEPO、theory、GRPO/GSPO experiments、handoff/overhead diagnostics、limitations 与
  reward-shaping appendix；公开代码入口已核对。
- **Original Problem / Previous Design / Changed Constraint**：给全部 roles 同一个 terminal reward 简单、
  低调用成本，并在贡献强耦合时避免不稳定拆分；但当一个 role 冗余或有害时，shared reward 仍让其随
  team success 更新，形成 free-riding 与 credit ambiguity。
- **Mechanism / State / Flow**：CCPO 计算 realized joint reward 与移除 role 后的 counterfactual reward
  差 `Delta_i=R_joint-R_without_i`，再经 EMA normalization、bounded shaping 与 group advantage 进入
  GRPO/GSPO。被移除 role 的当前 action 不能影响 baseline；在 Think–Solve 中只为 Thinker构造独立的
  solver-only counterfactual，Solver 使用 fused team/solo signal。SEPO 另用 verifier-anchored self/peer
  rubric 做有界 credit redistribution，不替代 external verifier。
- **Evaluation Contract / Proof Boundary**：两 Agent Think–Solve、数学 exact-match，Qwen2.5 1.5B/7B、
  Llama3.1-8B、Qwen3-4B 与 OLMo3-7B 等配置，比较 shared credit、CCPO、SEPO 及 GRPO/GSPO；论文报告
  单次 run，未披露 GPU 或随机 seed。部分 model-dataset 上 shared reward 更好，counterfactual evaluation
  又增加 verifier calls。因此只证明 role-sensitive credit 在被测配置常有价值，不证明 allocator 普遍
  占优或 practical GRPO 满足理想 KL trust-region 单调改进条件。
- **Trade-offs / Failure Modes / Old Design**：leave-one-role-out 会增加评测成本；循环/并行 topology 中
  counterfactual 可能爆炸且难以保持 action independence；verifier bias 与 self/peer collusion 会污染
  attribution。贡献不可分、verifier 昂贵或 team outcome 才是唯一可靠信号时 shared reward 仍合理。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch28～30 与 Ch77～78。Ch29 已有 sequence-to-token
  credit，尚未覆盖 team reward 到 role-specific advantage 的分层；Ch78 已要求测 role contribution，
  但那是 runtime evaluation。`Integrate — New Mechanism (Books Gate Pending)`；Ch29 为 owner，Ch78
  短 handoff，关系为 `Layering / Dependency`，状态 `Experimental`。

### Unified-MAS: Domain-Specific Node Generation and Optimization — 25/30

- **Source Family / Metadata / Coverage**：`WORKFLOW-OPERATOR-LIBRARY-OPTIMIZATION`；arXiv:2603.21475 v1，
  first-public 2026-03-23。已读 related work、两阶段方法、算法、四领域与数学实验、baseline、designer
  sensitivity、benchmark split、hyperparameter/cost appendix、manual-MAS descriptions 与公开代码入口。
- **Original Problem / Previous Design / Changed Constraint**：Automatic-MAS 在固定 generic node library
  上搜索 topology，search space 有界、可复现且 operator contract 稳定；但 specialised domain 的知识与
  procedure 不在 library 时，graph search 只能重排缺少能力的节点，dynamic node generation 又容易同时
  改 topology 与 node semantics 而不稳定。
- **Mechanism / State / Flow**：离线阶段从 validation examples 提取七维关键词，经四类 search strategy
  获取外部知识并生成 domain node blueprints；随后 Executor（需 token logits）在 validation trajectories
  上计算 perplexity-derived incremental node score，每轮定位最低平均 reward 的 bottleneck node，改其
  instructions 或增加 LLM calls。最终 `V_domain` 再交给既有 Automatic-MAS topology search；Designer、
  Executor、node library、validation evidence 与 runtime graph 分属不同 owner。
- **Evaluation Contract / Proof Boundary**：TravelPlanner/HealthBench/J1Bench/DeepFund 和 AIME24/25；
  validation size 8～45、test size 49～180，optimization 10 epochs、context sample 10。Designer 默认
  Gemini-3-Pro，Executor Qwen3-Next-80B-A3B；最终 workflow 测 Gemini-3-Flash、GPT-5-Mini、Qwen3-
  Next 与 DeepSeek-V3.2，部分任务由 GPT-4o judge；未披露 GPU/seeds。作者的 cost/performance 只属于
  这些 split、API pricing 与 judge，不能证明任意 domain node search 都优于固定 manual workflow。
- **Trade-offs / Failure Modes / Old Design**：反复使用很小 validation split 会造成 selection overfitting；
  search result、网页内容、judge 与 API pricing 会漂移；perplexity proxy 依赖可访问 logits，闭源 executor
  不一定适用。稳定 domain、强人工 operator 与审计要求高时固定 library 仍更可靠。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch76～78。Ch77 已覆盖 workflow program search 与
  template/run/trace，但尚未把 operator library 作为可版本化的独立 search layer。`Refine — Existing
  Argument (Books Gate Pending)`；owner Ch77，关系为 `Layering / Dependency`，状态 `Experimental`。

### Omni-WorldBench: Interaction-Centric World-Model Evaluation — 24/30

- **Source Family / Metadata / Coverage**：`WORLD-MODEL-INTERACTION-EVALUATION`；arXiv:2603.22212 v1，
  first-public 2026-03-23。已读 suite construction、metric pipeline、18-model setup、per-model generation
  contract、quantitative/qualitative analysis、limitations 与 prompt appendix。
- **Original Problem / Previous Design / Changed Constraint**：FID/FVD 与通用 video-quality metrics 对
  appearance 和 motion 有用，却难以判断 action 是否导致目标实体按因果约束变化、无关实体是否保持稳定，
  或 camera 是否按 trajectory 返回原位。world-model claim 因而需要 interaction-state transition evidence。
- **Mechanism / State / Flow**：prompt suite 标注 affected/unaffected entities、预期 motion、ordered events
  与部分 camera trajectories；evaluation 依赖 GroundingDINO+SAM entity tracks、RAFT flow、relative camera
  motion 与 VLM semantic verifier，最后由 LLM ranking prompt 决定多指标相对重要性并映射到预定义权重。
  prompt contract、extractor/version、validity mask、metric outputs 与 aggregator decision 都是 run evidence。
- **Evaluation Contract / Proof Boundary**：18 个 T2V/I2V/camera-conditioned models，全部在 NVIDIA H20
  上按官方设置生成，但模型间 resolution、FPS、frame count、steps 和 conditioning 不同。结果可比较此
  benchmark pipeline 内的交互 fidelity，不是 architecture 的 compute-normalized ranking。更关键的是，
  摘要/贡献声称 human-alignment studies，正文 limitations 却说 human-aligned results 将来发布；当前
  public v1 无法支持稳定的人类一致性结论。
- **Trade-offs / Failure Modes / Old Design**：detector、segmenter、flow 与 VLM verifier 的错误会串联；
  AgenticScore 的 prompt-conditioned weights 引入 judge drift，且 long-horizon/open-world 未覆盖。传统
  quality metrics 在目标仅是 visual fidelity、无需因果 interaction 时仍成立。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch61～63。Ch62 已完整要求 eval object/dataset/scorer/
  runtime/evidence 分层；本论文提供 world-model 实例但没有新的通用机制。`No Change — Already Covered`
  对原则成立；human-alignment claim 标 `Disputed Evidence Boundary`，不写 Books。

### UniGRPO: Unified Policy Optimization for Reasoning-Driven Visual Generation — 27/30

- **Source Family / Metadata / Coverage**：`MULTIMODAL-JOINT-POLICY-OPTIMIZATION`；arXiv:2603.23500 v1，
  first-public 2026-03-24。已读 text/flow policy background、MDP 与 joint objective、CFG-free rollout、
  velocity regularization、baseline/main result、ablation、future work 与完整 hyperparameter appendix。
- **Original Problem / Previous Design / Changed Constraint**：分别训练 text reasoner 与 diffusion/flow
  generator 可复用成熟 objective、隔离故障并保持各自 reward；但统一 interleaved model 中，一条
  trajectory 同时含 discrete tokens 与 continuous denoising actions，分阶段优化无法直接归因同一个终局
  image reward，CFG 的 conditional/unconditional branch 还会随 condition 与轮次放大 computation graph。
- **Mechanism / State / Flow**：同一 Bagel-based model 先采样 `G` 条 reasoning chain，再以每条 chain
  condition hybrid SDE/ODE image trajectory；terminal image reward 形成 group-relative advantage，同时
  更新 TextGRPO 与 FlowGRPO objective。训练移除 CFG，保持 linear rollout；并把带 `1/sigma_t^2`
  权重的 latent local KL 改为 reference/current velocity-field 的 unweighted MSE，减少不同 noise step 的
  regularization loophole。text tokens、flow state/noise schedule、reference velocities 与 reward 是异质状态。
- **Evaluation Contract / Proof Boundary**：单轮 `prompt -> reasoning -> image`，1024 resolution、group 24、
  batch 32、25 training/50 evaluation timesteps、Text LR `1e-6`、Flow LR `3e-5`；从 Bagel+SFT 出发，
  在 150 条内部 TA prompts（每 prompt 4 images、VLM scorer）与 GenEval 比较 ReFL/FPO/FlowGRPO/
  TextGRPO。论文未披露 hardware/seeds，且没有 multi-round experiment 或 process reward；因此只证明
  这些 reward/model/config 下 joint objective 可训练，不证明 CFG-free 或 MSE 约束普遍优于 exact KL。
- **Trade-offs / Failure Modes / Old Design**：shared terminal reward 无法区分文字 reasoning 与 image
  policy 的贡献，错误 reasoning 仍可能偶然生成高分图；unweighted MSE 改变了原 KL 的 probabilistic
  semantics，lambda 与 reward model 可能掩盖某一 modality collapse。模块分离在 owner、artifact、算力
  或 verifier 不同的场景仍更易审计和恢复。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch27～30，并核对 Ch23 与 Ch62 的 multimodal
  lineage/evaluation contract。Ch29 已有 group-relative advantage 和 token credit，但没有 heterogeneous
  discrete/continuous action spaces 的 joint trajectory。`Integrate — New Mechanism (Books Gate Pending)`；
  owner Ch29，关系为 `Mechanism Extension`，状态 `Experimental`。

### PEPO: Perception-Exploration Policy Optimization — 27/30

- **Source Family / Metadata / Coverage**：`MULTIMODAL-TOKEN-CREDIT`；arXiv:2603.22847 v1，first-public
  2026-03-24。已读 token analysis、visual-similarity/entropy formulation、GRPO/DAPO integration、五类
  benchmark、efficiency、ablation/sensitivity、evaluation protocol、policy-gradient proof 与 limitations。
- **Original Problem / Previous Design / Changed Constraint**：把 sequence advantage 均匀赋给所有 tokens
  保留了简单、低方差的 update scale；但 multimodal CoT 中，少量 tokens 直接承载 visual grounding，
  大量文字推理 tokens 却按长度获得更多梯度项，sequence success 无法区分感知证据与探索性转折。
- **Mechanism / State / Flow**：跨全部 layers 计算 response token 与 vision tokens hidden-state cosine
  similarity，结合 output entropy，经 per-response min-max、mean-centered tanh gate 与 softmax 得到
  unit-mean token weights；再用从 0 到 1 的 schedule 把 sequence advantage 重分配到 tokens。unit-mean
  只保持 advantage mass，不证明真实 policy-gradient norm 或 credit correctness 不变。
- **Evaluation Contract / Proof Boundary**：Qwen2.5-VL-3B 与 InternVL3-2B，全参 bf16、ZeRO-2、8×A40，
  group 8、temperature 1、top-p 1；覆盖 geometry、grounding、few-shot classification、visual puzzle 与
  ViRL39K 扩展，尽量使用 deterministic checker。作者结果支持这些 2B/3B curated settings 中 proxy
  weighting 的增量价值；未报告 seeds，也未覆盖 7B+、long context、video 或 tool-augmented reasoning，
  不能把 hidden-state cosine 当成已验证的通用 grounding attribution。
- **Trade-offs / Failure Modes / Old Design**：需要保存/读取全层 hidden states 和 vision-token relation；
  proxy 可能偏好表面 visual correlation，高 entropy 也可能是噪声。`alpha` 按 dataset 调节，作者所谓
  小于 1% overhead 只对相同 8×A40 training step contract 成立。缺少可信 token proxy 时，sequence-
  level GRPO/DAPO 仍是更稳健 baseline。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch28～30，并与同周两个 RLVR direction papers 联读。
  Ch29 已覆盖 sequence-to-token credit 与 causal evidence ladder，但未区分 multimodal perception proxy。
  `Refine — Existing Argument (Books Gate Pending)`；owner Ch29，关系为 `Principle Reuse + Modality
  Extension`，状态 `Experimental`。

### PyTorch 2.11: Differentiable and Compiler-Visible Collectives — 28/30

- **Source Family / Metadata / Coverage**：`PYTORCH-FUNCTIONAL-DIFFERENTIABLE-COLLECTIVES`；official
  v2.11.0 tag/commit `70d99e9` 与 release blog 均为 2026-03-23；联读 full release notes、functional-
  collective RFC、DTensor backward changes、backend/build compatibility 与 relevant code/PR links。
- **Original Problem / Previous Design / Changed Constraint**：ProcessGroup/c10d imperative collectives
  对 eager execution 与显式 synchronization 合理，但 non-functional mutation、ProcessGroup/Work object
  和 async lifetime 不容易进入 Dynamo/AOTAutograd IR；模型把 communication 写进 differentiable graph
  后，forward collective 的 backward、placement 与 wait semantics 都必须可追踪。
- **Mechanism / State / Flow**：functional collective 用 tensor-like async result 和显式/自动 wait 暴露
  compiler-visible data dependency；autograd 为受支持 collective 定义 backward。2.11 同时修正
  `DTensor.to_local()`：forward `Partial` 在未指定 `grad_placements` 时，backward 默认映射到
  `Replicate`，避免 local/global gradient interpretation 静默错误。process group/mesh identity、
  placement、collective sequence、async completion 与 derivative rule 共同构成 operator contract。
- **Evidence / Proof Boundary**：这是官方版本/API/implementation evidence，不是统一 performance study。
  Release 还把 FlexAttention FA4 限定于 Hopper/Blackwell，默认 PyPI wheel 改为 CUDA 13，并为 Volta
  保留 CUDA 12.6 route；这些兼容矩阵说明版本不能脱离 hardware/build artifact。官方材料不证明
  differentiable collectives 对所有 graphs 更快，也不证明 legacy API、backend 或 arbitrary async
  composition 都已 compiler-safe。
- **Trade-offs / Failure Modes / Old Design**：把 communication 纳入 graph 提高 optimization/composition
  能力，也把 rank divergence、process-group initialization、wait placement 与 derivative correctness
  变成 compile/runtime failure；同步 guard collectives 甚至可能因非 SPMD control flow deadlock。eager
  c10d 在 debug、动态 MPMD 或编译不稳定场景仍合理。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch31～33、Ch35/36。Ch32 已区分 semantics/runtime/
  transport 并要求 collective ordering，却没有显式说明 collective 何时成为可微计算图 operator。
  `Refine — Existing Argument (Books Gate Pending)`；owner Ch32，关系为 `Layering / Dependency`，版本
  行为标 `Versioned`。

### PyTorch Flight Recorder for NCCL Watchdog Timeouts — 29/30

- **Source Family / Metadata / Coverage**：`COLLECTIVE-FAILURE-EVIDENCE`；official PyTorch engineering
  blog 2026-03-25；已读 c10d/watchdog execution model、四类 root cause、Flight Recorder state/schema、
  dump coordination、cross-rank analysis、case studies、operational limits 与 docs/POC links。
- **Original Problem / Previous Design / Changed Constraint**：watchdog timeout 能终止永久 hang，却只在
  某 rank 的 monitoring thread 上观察到延迟症状；简单增加 timeout 或查看报错 rank 会把 CPU-side
  divergence、GPU hang、argument mismatch 和 fabric issue 混成“通信慢”。大规模 N-D parallel 又让
  rank 同时参与多个 groups，单进程当前 stack 无法重建分歧历史。
- **Mechanism / State / Flow**：每 rank 的 CPU-side ring buffer 跨其 process groups 记录 collective type、
  monotonically increasing per-PG sequence ID、四态 lifecycle（missing/scheduled/started/completed）、
  dtype/size 与 CPU call stacks。timeout signal 通过独立 TCPStore side channel 触发各 rank best-effort
  local dump；作业退出后由外部 orchestrator 聚合，并按 PG/sequence/metadata 离线对齐 mismatch。
- **Evidence / Proof Boundary**：官方报告 Meta 多个 training stacks 中 CPU-side issue 占主要比例、
  network/hardware 约 20～30%，并声称内部接近 100% full-dump rate；但 fleet、job count、sampling 和
  raw dataset 未公开，比例不能外推。两个 case study 支持“timeout rank 和 culprit 可能不同”以及
  call-stack/history 对定位有效，不证明 FR 单独可自动判定全部 root cause。
- **Trade-offs / Failure Modes / Old Design**：ring buffer 有采集/存储 overhead，timeout 时系统已碎片化，
  side channel、monitor thread 或 rank teardown 仍可能丢 dump；离线分析降低脆弱期协调，却延迟反馈，
  且仍需 CPU main-thread telemetry 与 hardware history。Metrics/watchdog 继续负责 detection，FR 负责
  bounded event history，不替代 trace、health telemetry 或 deterministic collective validation。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch32、Ch63～65。Ch64 已定义 structured event
  evidence，却没有“在分布式系统碎片化前冻结每 participant 局部历史，再按 protocol identity 对齐”的
  failure-snapshot mechanism。`Integrate — New Mechanism (Books Gate Pending)`；owner Ch64，Ch32/65
  短 handoff，关系为 `Layering / Dependency`。

### TorchTitan MXFP8 + DeepEP on B200 — 28/30

- **Source Family / Metadata / Coverage**：`MOE-COMPUTE-COMM-COOPTIMIZATION`；official PyTorch/Nebius
  engineering report 2026-03-25；已读 MXFP8/DeepEP mechanism、cluster/software contract、671B throughput、
  16B convergence、ablation boundary、future limits 与 reproducible recipes/merged PR links。
- **Original Problem / Previous Design / Changed Constraint**：BF16 与 generic All-to-All 提供成熟数值和
  communication semantics；在 B200 + EP=32 的 large MoE 中，grouped expert GEMMs 与 data-dependent
  token dispatch 同时成为瓶颈。只优化一边会把 critical path 推向另一边。
- **Mechanism / State / Flow**：MXFP8 为每 32 elements 共享 E8M0 scale，在 B200 native tensor cores
  上对 forward/input-gradient/weight-gradient grouped GEMMs 动态量化并 BF16 accumulate；DeepEP 用
  NVLink/NVSwitch + NVSHMEM/IBGDA RDMA、fused token/expert/weight metadata 与可配置 SM kernels 替换
  MoE dispatch/combine 的 generic backend。router shape、precision recipe、symmetric memory/transport、
  SM reservation 与 compile/local GEMM shape 必须联合配置。
- **Evaluation Contract / Proof Boundary**：32 nodes×8 B200、NVLink/NVSwitch + InfiniBand、TorchTitan/
  TorchAO/DeepEP/`torch.compile`、C4、seq 8192。671B 配置 TP2/PP2/EP32、local batch 64，报告 BF16
  standard EP 651、BF16+DeepEP 859、MXFP8 grouped GEMM+DeepEP 918 tokens/s；16B 在相同 256 GPUs、
  local batch 16 上只比较 1,500-step training loss。数字仅对该 workload contract 成立；没有 seeds、
  downstream quality 或同硬件跨 backend 全面 study，16B short loss 不能证明全程等价收敛。
- **Trade-offs / Failure Modes / Old Design**：小 grouped GEMM 的 quantization overhead 可抵消收益；
  671B 因 TP+compile 限制只量化 routed experts，DeepEP 又依赖 NVIDIA/NVSHMEM/IBGDA 和 symmetric-memory
  contract。generic collectives、BF16 与 dense GEMM 在小规模、非 B200、portability 或 debug 优先时仍
  合理。compute/communication 增益接近相加是该 profile 的结果，不是独立性定律。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch21、Ch32、Ch36，并核对 Ch45。Ch21 已覆盖
  dynamic expert batches/grouped GEMM，Ch32 已覆盖 semantics-algorithm-runtime-transport-topology 与
  kernel remote memory，Ch36 已覆盖 local shape/overlap；稳定机制已完整存在。`No Change — Already
  Covered`，保留为 workload-bound integration evidence，不写 Books。

### Astrolabe Code Release Follow-up — 17/30

- **Source / Date / Deduplication**：official repository 标注 2026-03-23 code release；对应论文
  arXiv:2603.17051 v1 first-public 2026-03-17，已在 W12 以 19/30 完成低分核验。W13 只把 access status
  从 paper-only 更新为 public implementation，不重置 event date、不重复累计 paper mechanism。
- **Decision / Boundary**：`Cross-week Artifact Follow-up Only`。代码支持 LongLive、Self-Forcing、
  Causal-Forcing/Krea configs 与组合 video reward，但 artifact availability 本身未改变 W12 的低分 Books
  判断；若后续升级，必须回到 W12 Source Family 联读 paper、repo/config 与可复现实验。

### Cross-Context Verification / HCCA — 19/30

- **Source / Date / Verification**：arXiv:2603.21454 v1，first-public 2026-03-23；metadata、作者
  abstract 与 revision state 已核对。作为低分边界项不以 abstract 冒充全文机制审计。
- **Evaluation Boundary**：作者 abstract 报告 9 个 SWE-bench Verified problems、45 trials、Claude
  Opus 4.6、temperature 0，并以 independent sessions 的 solution diversity 区分 contamination；样本
  极小、单一模型且任务经过选择，所谓 perfect separation 不能外推为通用 contamination detector。
- **Mechanism / Rejection**：HCCA 通过刻意限制不同分析角色的信息来降低 confirmation bias，另一个
  Worker→Verifier→Director pilot 反而出现 sycophantic confirmation。该负结果支持“更多角色不自动
  提高验证”，但没有足够规模、跨模型与 adversarial controls 改变 Ch62/78 的既有结论。
  `Weekly Only — Low-score Evaluation Boundary`；Ch62 主 owner，Ch78 handoff。

### DSPA — 22/30

- **Source Family / History / Access**：`DYNAMIC-SAE-PREFERENCE-STEERING`；arXiv:2603.21461 只有
  v1，first-public 2026-03-23。已读 HTML 全文、理论证明、实验与全部关键 appendices；论文没有给出
  独立作者代码仓库，因此 artifact reproducibility 为 `Not Disclosed`，不能由方法描述反推实现。
- **Full-read Coverage**：覆盖 Introduction/Related Work、双 SAE 设计、conditional-difference map、
  inference intervention、factorization/weak-coactivation/top-k/concentration proofs、models/data/baselines、
  main results、feature audit、data/compute comparison、layer/mode/SAE/feature-count/strength ablations、
  Limitations、Ethics、experimental setup 与 feature-interpretation prompts。
- **Original Problem / Why Previous Designs Were Reasonable**：DPO/RAHF 等 weight update 能让偏好进入
  模型参数，适合需要持久行为变化的部署；dense RepE 与 static SAE steering 则以较低训练成本提供
  可逆控制。但单一全局方向忽略 prompt feature co-activation，可能在 open-ended generation 中把
  与当前 token 无关的 latent 一起改动；weight update 又增加 gradient/optimizer/checkpoint state。
- **Mechanism / State Ownership**：offline builder 从 preference triple `(x,y+,y-)` 分别计算 prompt
  input-SAE activation density 和 response output-SAE density，形成
  `A = (1/N) Σ g(x) Δrho(x,y+,y-)^T`，再阈值稀疏化。运行时 prompt gate 选 top
  `k_prompt`，`A^T g(x)` 给 output latents 排名；decoder 只对当前 token 已激活的 selected latent
  增减 `alpha * max(f_t)`，经 output SAE decoder 把差值加回 residual stream。Preference dataset、
  input/output SAE、sparse map 与 hyperparameters 属于 alignment artifact；Decode runtime 拥有逐 token
  intervention，base weights 不变。
- **Theory / Proof Boundary**：`A^T = c Σ B M` 说明 map 在 shared-covariance mean-shift 与 additive-
  gating 假设下是被 gate co-activation 混合的 conditional direction，而不是直接恢复纯模板；只有
  `M` 接近 diagonal 或显式 de-mix 时污染较小。Top-k ablation 的最优性只对 linearized utility 与
  small-ablation model 成立；finite-sample bound 说明 rare prompt gates 的估计更噪，并不证明 SAE
  features 天然具备人类可解释因果语义。
- **Evaluation Contract**：61K UltraFeedback preference pairs；HH-RLHF SFT bases；Gemma-2-2B/9B 与
  Qwen3-8B；custom preference-domain SAEs；主配置 `k_prompt=32`、`k_diff=16`、`alpha=0.2`，Gemma
  layers 7→24 / 9→39，Qwen 9→18。Baselines 为 DPO、RepE、Static-SAE、prompt prefix，restricted-data
  另比较 RAHF-SCIT。MT-Bench 使用 GPT-4o judge，AlpacaEval 使用 Llama-3-70B annotator，另测 MMLU、
  ARC-Easy、TruthfulQA、HellaSwag、Winogrande；open-ended results 为三 generation seeds，未做完整
  per-model baseline sweep。
- **What Evidence Proves / Does Not Prove**：作者实验支持在上述三个 model/SAE/evaluator contracts 下，
  prompt-conditional ablation 能改善 MT-Bench、在 AlpacaEval 上保持竞争力且 MCQ regression 较小；
  layer、mode 和 custom-SAE ablations 支持“条件选择与 token-active edit”有独立作用。它不证明
  demographic fairness、long-horizon/safety alignment、跨 model-family transfer、对抗鲁棒性或生产
  Decode latency。feature labels 由 gpt-5-mini 生成且未系统人工验证；style-heavy latent 集中也可能
  解释 judge preference，而非更深的价值对齐。
- **Compute / Trade-offs / Failure Modes**：`4.47×` 是 8B dense-model FLOP model；单 H200 上 46 分钟、
  33.1 GB 对 8 小时 50 分钟、140.8 GB 的 `11.5×` 是 Gemma-2-9B restricted-data implementation
  comparison，不是通用 serving speedup。DSPA 以不更新 weights 换来双 SAE、map/version coupling、
  每 token encode/edit/decode、rare-gate noise、co-activation mixing、distribution drift、可逆 bypass 与
  misuse surface；它不替代 safety training、policy enforcement 或 independent evaluation。
- **Evolution / Chapters / Decision**：`weight update → global dense/static activation direction →
  prompt-conditional feature library → token-active residual intervention` 是 `Direct Evolution`，不是互斥
  替代；持久行为变化、无稳定 SAE 或低 runtime overhead 优先时，DPO/weight update 仍合理。已读 Ch5、
  Ch27～28、Ch67～69；Ch27 尚无这条 inference-time alignment branch，故暂定 `Integrate — New
  Mechanism (Experimental)`，Ch5/68 仅做 causal-evidence 与 authority handoff。Historical Books Gate
  关闭，当前不修改 Books。

### DRTriton — 29/30

- **Source Family / History / Access**：`SYNTHETIC-RL-TRITON-KERNEL-GENERATION`；arXiv:2603.21465
  v1 first-public 2026-03-23，v2 发布 2026-05-26。已读 v1 全文与 v2 revision：v2 将 operator coverage
  校正为 61，使用 `torch.export` 说明 functional lowering，补充 8×H100 training contract、search
  overhead 与 explicit limitation。论文未链接公开代码、dataset/model artifact，故实现复现状态为
  `Not Disclosed`。
- **Full-read Coverage**：覆盖 Introduction/Related Work、CSP-DAG/CP-SAT constraints、operator
  appendix、verifier、SFT、DRPO objective、curriculum rule、fragment search/reconstruction、synthetic 与
  KernelBench evaluation、GRPO/reward ablations、search overhead、functional-rewrite 与 LeNet case study、
  prompts、GRPO appendix、revision history 与 NeurIPS checklist。
- **Original Problem / Why Previous Designs Were Reasonable**：human-written kernels 与 compiler
  heuristics 对稳定 operator families 可审计、可维护；repository-mined SFT 和 multi-agent search 也能
  复用真实代码。但 real pairs 稀缺且分布不可控，直接 RL 在 compile/correctness reward 极稀疏时难以
  cold start；单一 fused-kernel generation 在 graph 变长后迅速失败。
- **Data / Control Flow / Ownership**：CSP-DAG 随机生成 operator DAG，CP-SAT 拥有 tensor rank/shape、
  FLOP 与 size constraints；teacher LLM 生成 level-1 Triton pair，verifier 用 linter+compile、no-op
  monkey patch 和 5 个随机 I/O cases 过滤；SFT 提供 language cold start。随后 policy 在 level
  1→2→5 的 synthetic programs 上训练，DRPO 分开 correct/incorrect likelihood 与 correct outputs 内的
  speed weighting，并用 old-policy KL hinge 控制更新。部署侧把 graph 分解为长度至多 5 的 contiguous
  fragments，逐个生成、验证与 benchmark，再把单个 verified fragment 替换回 PyTorch program，选
  最快 hybrid artifact。这里 generator、constraint solver、compiler/verifier、benchmark harness、
  policy trainer 与 artifact selector 是不同 owners。
- **Training Contract**：Qwen-2.5-Coder-7B-Instruct；2,026 个 teacher-generated level-1 pairs；SFT
  10 epochs、LR `2e-6`、batch 64。DRPO 使用 20k/60k/20k level-1/2/5 programs、每 stage 1 epoch、
  LR `1e-6`、8 rollouts/prompt、`(beta0,tau,lambda)=(100,5,0.1)`、KL upper bound `0.001`；v2 披露
  8×H100、SFT 约 2 小时、curriculum RL 约 10 天。CSP-DAG 在 32-core CPU 上生成 100k programs
  约 1.5 小时。
- **Evaluation Contract / Author Results**：synthetic benchmark 为 400 held-out programs，level
  1/2/5/20 各 100；KernelBench 为 100/100/50 个 level-1/2/3 tasks。指标为 verifier pass、correct
  kernels 中 `>1×` Torch Eager/`torch.compile` 占比和 geometric-mean speedup。作者报告 test-time
  search 后 KernelBench Level 2 为 96% correct、92% faster than eager、56% faster than compile；
  Level 3 为 76% correct、54%/34%。这是论文 harness 内的 Pass@1 + search result，不是生产 goodput。
- **Ablation / Overhead / Proof Boundary**：同一 SFT checkpoint 的 Stage-1 experiment 支持 DRPO
  优于作者构造的 GRPO reward；1.5B reward-shape ablation 支持 log speed reward 优于四个 power
  choices。test-time search 在 synthetic 评估 10,612 fragments / 2.85 小时，在 KernelBench 16,859 /
  3.53 小时；这证明 complex graph gains 依赖大量 compile/validate work，而非免费 model capability。
  论文没有披露 CUDA/Triton/PyTorch/driver versions、benchmark GPU clocks、warmup/repetition、numerical
  tolerance、timeout 与 confidence intervals，不能跨硬件或 compiler version 外推 headline。
- **Limitations / New Failure Modes**：v2 明确 operator set 仅 61，未覆盖 sparse ops、custom CUDA
  extensions 与 native CUDA generation。5 random tests 与 no-op monkey patch 不能排除 shape hard-code、
  alias/mutation、numerical edge、nondeterminism 或 hidden-workload exploit；`torch.export` lowering 也
  只覆盖可导出的 graph semantics。speed reward 会学习 measurement noise/cache/JIT artifacts；fragment
  search 新增 compile budget、artifact explosion、hardware/compiler coupling 与 selection overfitting。
- **Evolution / Chapters / Decision**：`manual/compiler templates → mined-pair SFT → verifier-backed RLVR
  → controlled synthetic curriculum → compositional generate/verify/benchmark search` 是 `Direct
  Evolution`。旧 compiler 在 coverage、determinism、cold start 与 maintenance 优先时仍成立；learned
  path 应作为受验证的候选 artifact producer，而非直接替代 compiler。已读 Ch44～46，并核对 Ch25、
  Ch27～29 与 Ch78 handoff；Ch45 已有 semantics→execution plan→kernel/workload contract，但尚可由本
  Source Family refine executable-kernel artifact lifecycle，故暂定 `Refine — Existing Argument
  (Experimental)`。Historical Books Gate 关闭，当前不修改 Books。

### TurboQuant — 24/30

- **Source Family ID / Type / History**：`TURBOQUANT-EDEN-RABITQ`；TurboQuant
  arXiv:2504.19874（first-public 2025-04-28，ICLR 2026 版本）与 Google 2026-03-24 传播节点；
  联读 arXiv:2604.18555（EDEN/DRIVE note）和 arXiv:2604.19528（RaBitQ symmetric comparison）。
- **Full-read Coverage**：已覆盖原论文 metadata、理论 lower bound、random rotation/scalar
  quantizer、MSE 与 inner-product 两条算法、KV/ANN evaluation 和 appendix；并覆盖两份技术
  反证的方法、可复现配置和结论。
- **Problem / Previous Design / Changed Constraint**：PQ、scalar quantization、DRIVE/EDEN、RaBitQ
  在各自 distortion/throughput contract 下合理；在线高维向量、低 bit 与近零 indexing overhead
  促使 data-oblivious rotation 路线被重新组合。
- **Mechanism / Flow**：随机旋转使坐标分布集中后逐坐标量化；`mse` 路线优化重构误差，
  `prod` 以量化主项加 1-bit residual QJL 追求无偏 inner product。encoder/decoder 必须共享
  transform、scale、bit layout 与 calibration contract。
- **Evaluation Boundary**：原论文声称 KV 2.5/3.5-bit 与 ANN 收益；EDEN note 指出固定 scale
  的次优性并复做 accuracy；RaBitQ note 报告对称设置下无一致优势且部分 runtime/recall 未复现。
  三方没有形成统一 artifact、kernel、model、quality 和 hardware 条件，故不可挑选单方数字。
- **Trade-offs / Failure Modes**：rotation 和 residual 增加 compute/layout complexity；bit 数下降
  可能把 bandwidth 收益换成 quality、decode overhead 或不受支持的 kernel；旧 EDEN/RaBitQ
  在其目标和 artifact 成熟度下仍成立。关系为 `Disputed` 而非线性替代。
- **ROADMAP / Chapters / Existing Coverage**：Ch45/Ch50 主线，已读 Ch44～46、Ch49～51；现有
  “storage bit-width 不等于 end-to-end latency”已完整覆盖可沉淀原则。
- **Decision / Files / Questions**：`Disputed`；无 Books 修改。需同一公开 implementation、
  hardware、dataset/model、quality target 与 end-to-end kernel 下复现。

### MolmoWeb: An Open-Source Web Agent for the Visual Web — 25/30

- **Candidate / Week / Score**：MolmoWeb；2026-W13；25/30。Ai2 官方发布发生在 2026-03-24，早于
  arXiv v1，因此从 W15 纠偏回本周；Technical Novelty 4、System Impact 4、Practical Value 5、
  Source Reliability 4、Project Relevance 5、Longevity 3。
- **Source Family / Type / Revision History**：`MOLMOWEB-VISUAL-WEB-AGENT`；Ai2 official research
  release、Hugging Face model/data collection、arXiv:2604.08516 v1 与 author repository。官方博客
  2026-03-24 首次公开模型、数据与评测工具；data/model collection 同日更新。论文仅 v1，2026-04-09
  17:54 UTC 提交；完整训练代码于 04-10 宣布开放。后两者是同一 Source Family 的 artifact evolution，
  不构成 W15 新候选。current repository 有持续提交且无已定位 immutable release，故不能把当前 main
  反推成 3 月 24 日实现快照。
- **Full-read Coverage**：已读 official announcement、论文 Abstract、Introduction、Related Work、
  MolmoWebMix construction、model/training、agent interface、main evaluation、scaling/data/decoding
  ablations、analysis、limitations、safety、Appendix B/C 的数据流水线、prompts、training/evaluation
  details，并核对 Hugging Face collection 与 repository 顶层实现结构。
- **Original Problem / Why Previous Designs Were Reasonable**：DOM/AxTree Agent 能获得结构化节点、文本
  与 selector，适合可访问性树稳定、API/DOM 可用且需要精确 element identity 的场景；人类 demonstration
  则提供真实视觉决策、纠错与界面语义。纯 screenshot Agent 减少对网站内部表示的依赖，却需要从像素恢复
  grounding、状态变化与 action target。旧路线并未失效；变化的约束是希望同一 open model 跨开放网站、
  仅凭视觉 observation 执行长程任务，同时获得可发布的数据、模型与 harness。
- **Data Mechanism / State Ownership**：MolmoWebMix 把约 278.5K trajectories、2.2M steps、2.6K domains
  组成 trajectory mixture，另以约 10.5M grounding/screenshot-QA examples 补充 perception。trajectory
  来源包括 human demonstrations、atomic skills、node traversal、single-agent 与 multi-agent synthetic
  paths。synthetic teacher 可读取 privileged AxTree；planner、operator 与 verifier 分属不同模型/角色，
  再把可执行轨迹编译为 screenshot-only student 的 observation/action records。dataset builder 拥有 task、
  teacher view、action schema、verifier 与 browser revision；trainer 拥有 mixture/SFT checkpoint；runtime
  Agent 只看到 screenshot、instruction、URL/title 与最近十步 action history，并输出带 thought 的 normalized-
  coordinate browser action；environment 拥有页面状态与 side effects，judge 只拥有离线 verdict。
- **Control Flow / Data Flow**：`task seed → human or privileged synthetic teacher → browser execution →
  verifier/URL checks → normalized screenshot/action trajectory → mixture with perception data → SFT → live
  browser rollout → rule/LLM judge`。这条链说明“开放 visual Agent”仍依赖上游 structural teacher 与
  verifier；模型 observation interface 与数据生成 interface 可以不同，但这种 distillation gap 必须进入
  lineage，不能只保存最终 screenshot/action pair。
- **Implementation / Training Contract**：模型沿用 Molmo2 路线，使用 Qwen3 language model 与 SigLIP2
  vision encoder，并联合更新 language、vision 与 adapter；训练披露 64×H100、global batch 128、最多
  50K steps（约 3.2 epochs）。action 以 JSON 表达，坐标归一化。公开资料没有给出完整训练 wall-clock、
  energy、所有 dependency/container digest、失败恢复与 immutable release identity。
- **Evaluation Contract**：live WebVoyager、Online-Mind2Web、DeepShop 与 WebTailBench；网页日期被人工
  更新，Browserbase 提供浏览器和 CAPTCHA 处理；每项最多 100 steps，失败环境可重试至 10 次，主要结果
  使用 3～5 runs。评测混用 deterministic checks、GPT-4o/o4-mini judge，并对 WebTailBench 替换原 judge；
  部分 baseline 数字来自 Fara，故并非所有模型共享完全相同的 browser/judge/version contract。论文没有
  提供 production concurrency、TTFT/step latency/p99、token/tool cost、side-effect rollback 或用户 SLO。
- **Ablations / What Evidence Proves**：作者实验支持在上述 benchmark contract 内，混合 trajectory 与
  perception、增加训练数据/模型规模、延长 step budget 和采样多个 rollout 会改变 task success；早期
  ablation 使用较早 dataset version 和 30-step limit。matched 2.7K-task comparison 中 synthetic paths
  优于 human paths，但 synthetic teacher 具有 privileged AxTree、直接路径与 benchmark-family alignment，
  所以结果只证明该生成 pipeline 在作者条件下有效，不证明 synthetic data 普遍优于人类 demonstration。
- **Pass@k / Selector Boundary**：论文从 5 次 rollout 估计 `pass@k`，并用额外 LLM judge 做 best-of-N。
  `pass@k` 衡量候选集合覆盖，不是单次 policy reliability；best-of-N 又增加 selector error、judge coupling、
  total browser actions、成本与 side-effect exposure。`3×30-step` 优于 `1×100-step` 的作者结果没有做
  等成本、等延迟、等副作用预算的 production 对齐，不能直接写成通用 test-time scaling law。
- **Limitations / Threats / Failure Modes**：困难集中在小文字/OCR、歧义与多约束任务、rare actions、
  repeated-action loop 和 recovery。visual-only 降低 DOM coupling，却增加 grounding error；privileged
  teacher 提高生成效率，却可能遗漏 human-only recovery/hesitation 并造成 teacher-student interface gap；
  benchmark-like task generation 可能提高 distribution alignment。论文明确未优化 latency；hosted browser
  更慢，thought text 也未被证明与真实 action cause 一致。训练排除 login、个人和金融任务；demo 的 whitelist、
  classifier、password/credit-card block 是 harness safety，不是模型内生保证。
- **Evolution / Where Previous Designs Still Apply**：`passive screenshot QA/grounding → atomic visual skill
  → end-to-end browser trajectory → closed-loop visual policy` 是 data/capability 的 `Direct Evolution`；
  `human demonstration ↔ AxTree synthetic teacher` 与 `visual-only ↔ DOM/AxTree ↔ API action` 是
  `Alternative Branches`。结构化 interface 在可用性、确定性与可审计性优先时仍合理；human data 在真实
  recovery、隐含约束和 consent-bearing behavior 上仍不可由 privileged synthetic path 静默替代。
- **ROADMAP / Adjacent Chapters / Existing Coverage**：已读 Ch22～24，并核对 Ch25、Ch62、Ch68、
  Ch74 与 Ch77。Ch23 已把 synthetic data 定义为 executable specification，也保存 source image →
  transformation → visual tokens lineage；MolmoWeb 仍补出一个明确缺口：Agent trajectory row 还必须保存
  teacher observation modality、student observation modality、action abstraction、browser/environment revision、
  verifier/judge 与 side-effect policy，因为这些字段共同定义实际 learned policy，而不只是数据质量。
- **Integration Decision**：`Refine — Existing Argument (Experimental; Provisional; Historical Books Gate
  Closed)`。主 owner 为 Ch23，Ch25/62/68/74/77 只做 SFT、evaluation、安全、tool authority 与 durable-run
  handoff。Books Gate 通过后只沉淀 lineage、interface mismatch、candidate-coverage 与 selector boundary；
  不写模型排名、固定数据配比、headline success rate 或“visual/synthetic 必然替代 DOM/human”的结论。

### vLLM `TRITON_MLA_SPARSE` portability path — 24/30

- **Source Family / Event Date / Revision / Access**：`VLLM-SPARSE-MLA-HARDWARE-PORTABILITY`；
  issue #38006 于 2026-03-24 首次公开，PR #38476 于 2026-03-29 打开，均落在 W13。已读 issue
  root-cause update、PR purpose/change inventory、benchmark、tests、review threads 与 later activity；截至
  2026-08-11 issue/PR 仍为 `Open`，PR 未合并。3 月 29 日后的 rebase、performance、long-sequence
  correctness 讨论只作为 revision/failure evidence，不倒写为 event-time 已知保证。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：DeepGEMM、
  FlashMLA-Sparse、FlashInfer-MLA-Sparse 针对支持它们的 architecture 提供专用高性能路径；限制旧 GPU
  support 可以缩小 kernel/test matrix，本来是合理工程选择。但 GLM/DeepSeek 一类 Sparse MLA model
  需要在 SM80/A100/A800 或 SM121 上运行时，问题不是“缺一个 fallback”这么简单：compile/link
  可能引用新架构 symbol，indexer logits 可能错误 dispatch 到仅 SM90+ 可用的 DeepGEMM，attention
  backend 也可能没有可执行实现。硬件 installed state 与 actual capability 不再等价。
- **Mechanism / State Ownership**：proposal 将 portability 拆成四个 owner：build system / C++ guards
  拥有 architecture-specific symbol availability；runtime dispatch 以 `is_deep_gemm_supported()` 而非
  package-presence 判断 indexer path；Triton MQA logits kernel 拥有 sparse indexer 的 score calculation；
  `TRITON_MLA_SPARSE` backend 拥有 selected sparse blocks 的 Decode attention，并由 metadata builder
  声明 CUDA graph compatibility。Model/router 仍拥有 sparse indices，KV manager 仍拥有 paged KV；
  fallback backend 不能修改这些语义身份。
- **Control Flow / Data Flow**：`model load / compile capability check -> attention-backend selection ->
  q/k and paged-KV metadata -> Triton FP8 MQA logits -> top sparse indices -> split-KV or single-pass sparse
  Decode attention -> N-way online-softmax merge -> output`。Prefill indexer 在 wrapper 中将 FP8 source
  解码到 BF16 后进入 `tl.dot`；paged Decode 使用 LUT 做 in-kernel FP8 decode。Split-KV path 必须用
  numerically stable merge；全 masked tile 用有限 sentinel 避免 `(-inf)-(-inf)` 产生 NaN。
- **Implementation Details**：PR 同时加入 SM80 build guards、backend registry、Triton indexer/logits、
  split-KV kernel、uniform-batch CUDA graph 声明和新架构-only MXFP4 symbol stubs。Autotune 在 init 以
  `(n_head, head_dim)` warm up。这个组合说明 portability 是 build、dispatch、kernel、metadata 与 graph
  的联合 contract；只修 indexer fallback 仍可能编译失败或没有 attention backend。
- **Evaluation Contract**：作者 benchmark 为 `8×A100 SXM`、`TP=8`、
  `lukealonso/GLM-5.1-NVFP4`、single prompt、Decode 200 tokens；输入分别约 1,744、65,536、127,744
  tokens，并区分 cold 与 prefix-cache warm。PR 报告 TTFT、median TPOT 与 output tok/s；tests 覆盖
  41 个 MQA-logits cases 和 53 个 sparse-kernel cases。公开 contract 未给出并发、请求分布、P95/P99、
  power、编译/JIT cold cost、跨模型质量、完整 baseline matrix 或生产 SLO。
- **What Evidence Proves / Does Not Prove**：代码、unit tests 与单 prompt run 支持“该 proposal 能在指定
  A100/模型/precision/path 上形成可执行结果，并覆盖部分数值边界”。它不证明 PR 已被 vLLM 接受，
  不证明 SM80/SM121、A100/A800、不同 quant/KV dtype 或长上下文都正确且高效，也不证明 Triton
  fallback 优于支持硬件上的 DeepGEMM/FlashMLA。Warm prefix 的 tok/s 不能与 cold long-context TTFT
  混成一个 speedup；没有 matched baseline 时也不能把绝对数字写成通用收益。
- **Limitations / Threats / Failure Modes**：event-time PR 明确 BF16 KV only，batch-invariant mode 的
  `num_kv_splits=1` 尚未接线；review 当周也对是否支持 SM80 与 PyTorch fallback 性能存在分歧。后续线程
  报告 rebase conflict、低 tok/s、需要继续开发，并在未合并 patchset 中发现长序列 address arithmetic
  overflow / silent-corruption 风险。这些 post-window 事实不改变 W13 event date，却说明 capability guard、
  pointer width、tail mask、autotune cache、graph metadata 与 long-context tests 都是 correctness surface。
- **Trade-offs / Previous Design Still Applies**：Triton fallback 延长旧 GPU 可用期并减少对 architecture-
  exclusive libraries 的依赖，却扩大维护/test matrix，可能牺牲专用 kernel 性能，并新增 JIT、numerical
  merge、graph capture 与 long-sequence address bugs。Hopper/Blackwell 且专用 backend 可用时，原路径仍
  可能更快、更成熟；不要求 sparse execution 时 dense MLA 是另一退化分支；无法承担验证成本时拒绝加载并
  给出明确 capability error，比静默选择未验证 fallback 更安全。
- **Evolution Relationship / ROADMAP / Existing Coverage / Disposition**：`architecture-specialized backend
  -> explicit capability guard + correctness fallback -> architecture-tuned portable backend` 是 `Layering /
  Dependency` 与 `Alternative Branches`，不是线性替代。主 owner Ch45，已读 Ch44～46；Ch45 已拥有
  library/compiler/kernel/hardware contract，但当前正文主要讨论 compute-kernel optimization，尚未明确
  “hardware portability 要同时穿过 build、dispatch、indexer、attention 与 graph 五层”的 failure chain。
  暂定 `Refine — Existing Argument (Experimental; Open PR; Historical Books Gate Closed)`；Ch46 只做
  version/support-matrix handoff。本轮不修改 Books。

### Anthropic Economic Index: learning curves — 21/30

- **Sources / Coverage**：2026-03-24 官方网页版与 PDF/appendix；样本为 2026-02-05～12 的
  Claude.ai 与 first-party API，各抽样 100 万 conversations，并与 2025-11 state 比较。
- **Evidence / Limits**：高 tenure 与约 10% higher success 是控制部分 observable 后的关联；
  论文明确仍可能来自 early-adopter sophistication，不能写成使用 Claude 的因果学习收益。
- **Mechanism / Trade-off**：privacy-preserving classification 使群体趋势可见，但 taxonomy、
  model-assisted labels、平台迁移和 sampling window 共同限制解释；API Agent 调用拆分还会改变
  task-count 语义。
- **ROADMAP / Decision**：Ch62/63/69 已读；`No Change — Already Covered`，保留为 telemetry
  interpretation 案例。

### TRIBE v2 — 18/30

- **Source / Date / Verification**：Meta 2026-03-26 官方发布已核对；TRIBE v2 是独立垂直
  model/research family，不与次日 SAM 3.1 共享机制。
- **Score / Decision / Rejection**：18/30；`Weekly Only — Version/Product Fact`。公开材料没有补充
  与本书模型 lifecycle、training 或 Infra contract 相关的长期新机制。

### SAM 3.1 — 18/30

- **Source / Date / Verification**：Meta 2026-03-27 官方发布已核对；SAM 3.1 属于 segmentation
  model family 的版本/研究状态，不是 TRIBE v2 的后续阶段。
- **Score / Decision / Rejection**：18/30；`Weekly Only — Version/Product Fact`。垂直模型能力与
  发布方 benchmark 不足以改变本书通用模型/系统结论。

## Repository Changes

- 重开 W13 discovery 后累计记录 45 个 scored families；41 个 `20+` 均有完整 Source Review，另完成
  Astrolabe 跨周 code artifact、vLLM MoE-offload RFC 跨周架构节点与 CCV 低分核验。DSPA/DRTriton
  已从 metadata-only queue 升级为 non-template Full Source Reviews。
- DSPA 与 DRTriton 的 owner/adjacent chapters 已完成联读：DSPA 主 owner 为 Ch27，DRTriton 为 Ch45；
  两项均记录机制、状态所有权、公式、evaluation contract、证明与未证明、trade-off、revision drift
  和 provisional Books disposition。DRTriton v1/v2 的 event-time/post-window facts 已明确分开。
- TRIBE v2 与 SAM 3.1 已从旧合并行拆为两个 source families、两个评分和两个低分 Review。
- MolmoWeb 已按 Ai2 2026-03-24 official first-public date 从 W15 纠偏回 W13；完成 official release、
  arXiv 全文、Hugging Face collection、repository、evaluation contract 与 Ch22～25/62/68/74/77 邻接审计，
  recorded `20+` queue 更新为 21/21。
- vLLM fixed-source replay 新增 `TRITON_MLA_SPARSE` 的 24/30 Full Source Review，并把 incremental
  MoE expert offloading 的 first-public owner 从 W13 RFC 纠正到 W12 PR。该检查点将 scored families
  提升到 30、recorded `20+` queue 提升到 26/26；后续 Trace2Skill packet 再更新为当前 31 与 27/27。
  Hugging Face historical papers page 的保存权限阻断已显式列为
  coverage limitation，不能伪装成已扫描。
- W14 curation-lag ledger 已拆回 20 个 W13 in-window candidate-level 条目；`Lie to Me`、MedOpenClaw、
  Composer 2、Hybrid Memory 与 Trace2Skill 已完成全文、appendix、artifact/evaluation boundary、评分与章节邻接审计，14 项仍是
  `Audit Pending`，另有 ClawKeeper 为 blocked backlog。Composer 2 的 provisional owner 为 Ch29；其 asynchronous MoE RL packet 显式记录
  mid-trajectory weight revision、router replay、sandbox snapshot、sample checkpoint 与 vendor benchmark
  的证明边界。未审计标题、ID 与
  provisional date 只作为 discovery intake，不计入 scored 或 Full Source Review 数。Sommelier、SEAR、
  FIPO 的 provisional date 为 3 月 20 日，已明确路由到 W12 spillback backlog，不制造 W13 事件。
- ClawKeeper 的 abstract、HTML、检索、export API 与可视浏览入口均未返回可核验 primary text；已从
  17 项 pending 队列移为 `Unverified / Blocked Backlog — Unscored`。其余 pending 因而为 16 项，forward
  cursor 继续，不根据候选名称猜测机制或章节。
- Hybrid Memory / HyDRA 已完成 paper、supplement、project、repository、model/dataset identity 与 Ch9/10、
  Ch14/22/62 邻接审计；评分 26/30，provisional owner 为 Ch10。它从 16 项 pending 中移出后，pending
  变为 15；training skeleton 不等于完整训练复现，artifact 状态保持 `Partially Reproducible`。
- Trace2Skill 已完成 v1 全文、实验/ablation/limitations、v5 revision boundary、official repository 与
  Ch73/76/77/80 邻接审计；评分 27/30，provisional owner 为 Ch80。它从 15 项 pending 中移出后，pending
  变为 14；论文的 frozen-base parallel patch + hierarchical merge 只作为 Skill artifact compilation
  candidate，不被写成对 sequential edit、retrieval memory 或 human authoring 的通用替代。
- Natural-Language Agent Harnesses 已完成 v1 全文、三组实验、paired/module ablation、migration cases、
  limitations、Appendix A～F、v2 revision、LinguaClaw artifact boundary 与 Ch77/78/80/62 邻接审计；评分
  28/30，provisional owner 为 Ch77。它从 14 项 pending 中移出后，pending 变为 13；自然语言只拥有
  pattern layer，deterministic code 继续拥有 enforcement，OSWorld headline 不被解释为 language-medium 因果收益。
- Density-aware Soft Context Compression 已完成 sole-v1 全文、公式、训练/evaluation contract、official
  code/data/LoRA artifact 与 Ch22/71/41 邻接审计；评分 26/30，provisional owner 为 Ch22。它从 13 项
  pending 中移出后，pending 变为 12；summary-length density proxy、短输入、substring scorer、无硬件/SLO/
  variance 与 correlation-only evidence 使其保持 `Experimental`，artifact available 不等于已独立复现。
- Learning to Commit 已完成 sole-v1 全文、数据构建、四组 experiment、metrics、analysis/future-work 与
  Ch73/80/62 邻接审计；评分 25/30，provisional owner 为 Ch73。它从 12 项 pending 中移出后，pending
  变为 11；internal single-repository、24/7 commit pilot、synthetic issue、无公开 artifact/variance/cost 与
  judge/maintainer gap 使其保持 `Experimental / Artifact Not Available`。
- TAPS 已完成 sole-v1 21 页 PDF、全部五个 RQ、formula/setup/results、tree-merge correctness proof、depth/
  entropy appendices、official code/weights/datasets 与 Ch44/42/41/45/55 邻接审计；评分 29/30，provisional
  owner 为 Ch44。它从 11 项 pending 中移出后，pending 变为 10；acceptance length 不等于端到端 speedup，
  双 draft 与 larger verification tree 的成本使其保持 `Experimental / Artifact Available`。
- DataFlex 已完成 sole-v1 全文、三类 data action、distributed implementation、selection/reweighting/mixture
  experiments、efficiency appendix、official code/docs/datasets 与 Ch22～24/35/56/62 邻接审计；评分 28/30，
  provisional owner 为 Ch23。它从 10 项 pending 中移出后，pending 变为 9；项目 2025-12-23 首次公开、
  2026-03-17 ZeRO-3 support 与 2026-03-27 paper node 已按 Source Family 分开。多卡 headline 不是 matched-
  resource scale-up，动态 data policy 也不被写成静态 curation 的通用替代。
- Ask or Assume 已完成 v1 全文、五种 setting、question/difficulty/conditional analyses、prompts/cost/
  limitations、v2 Kimi/dataset-validation revision、official code/evaluation paths 与 Ch75/77/78/62 邻接审计；
  评分 28/30，provisional owner 为 Ch77。它从 9 项 pending 中移出后，pending 变为 8；v2 的过度询问
  说明 calibration 依赖 backbone/tool semantics，simulated-user resolve rate 不被外推为真实人类协作能力。
- XpertBench 已完成 v1/v4 全文、task/rubric pipeline、ShotJudge、Gold-subset results、五域 appendices、
  platform/empty dataset boundary 与 Ch61～63 邻接审计；评分 25/30，`No Change` owner 为 Ch62。它从 8 项
  pending 中移出后，pending 变为 7；`2604.*` 编号未覆盖 2026-03-27 submission timestamp，52% CDR 和
  vendor ranking 不被写成人类等价或通用模型能力，artifact 保持 `Not Available`。
- EpochX 已完成 sole-v1 全文、12 个公式、三个 cases、official product/live-platform boundary 与
  Ch77～80/55 邻接审计；评分 23/30，`No Change` owner 为 Ch80。它从 7 项 pending 中移出后，pending
  变为 6；论文只提供 case-based architecture evidence，未公开实现、交易/验证日志或纵向 incentive
  evaluation，因此 acceptance 不被写成 correctness proof，credits 不被写成已验证经济机制。
- daVinci-LLM 已完成 sole-v1 49 页全文、L0～L9 taxonomy、3.09B/8T 四阶段 training contract、200+
  ablation、mixture/QA-ratio、PPL/generative evaluation、appendix、official repository/model/data cards 与
  Ch23～25/56/62 邻接审计；评分 28/30，provisional owner 为 Ch23。它从 6 项 pending 中移出后，pending
  变为 5；L0～L9 不被写成单调阶梯，stage ratio 不被写成通用配方，hardware/seeds/variance 缺失及
  pipeline `Coming soon` / subset-only data surface 使其保持 `Experimental / Artifact Partially Available`。
- `Emergent Social Intelligence Risks` 已完成 v1 全文、15 类 scenario、formal lifecycle、全部实验与
  appendices、v2 revision boundary 及 Ch78/62/68 邻接审计；评分 27/30，provisional owner 为 Ch78。它从
  5 项 pending 中移出后，pending 变为 4；不同 backbone/trial/judge、无统一 sampling/variance、无真实部署
  对照、无独立 Limitations section 和无公开 artifact 使其保持 `Experimental / Artifact Not Available`。
  本周只接受 interaction-level risk taxonomy 与 measurement contract，不把场景发生频率外推为生产风险率。
- PRBench 已完成 sole-v1 全文、30-task curation/evaluation contract、全部实验/failure analysis、Appendix
  A～D、official project 与 public harness，并核对 Ch62/61/63；评分 27/30，`No Change` owner 为 Ch62。它从
  4 项 pending 中移出后，pending 变为 3；公开 artifact 只有一个完整 sample task，judge/sampling/cost 与
  30-task reference/run set 不完整，故保持 `Experimental / Artifact Partially Available`。34% 和 0% callback
  只描述作者 EvalSpec，不写成模型或 framework 的通用能力结论。
- MuSEAgent 已完成 sole-v1 全文、transition/hindsight/multi-view retrieval 机制、全部实验/ablation、tool/prompt
  appendices、official repository 与 Ch73/76/72/74/62 邻接审计；评分 28/30，provisional owner 为 Ch73。它从
  3 项 pending 中移出后，pending 变为 2；四个多选 VQA、固定 1:1 split、无 hardware/latency/cost/variance，
  以及 hindsight judge 同时拥有 filter/guidance 权力，使其保持 `Experimental / Artifact Available`。完整
  trajectory 仍拥有 provenance、replay 和跨步因果上下文，derived transition memory 不被写成通用替代。
- KAT-Coder-V2 已完成 sole-v1 22 页全文、KwaiEnv、五类 expert SFT/RL、turn-level objective、MCLA、KRL/
  Tree Training、on-policy distillation、全部 evaluation 与 Ch28～30/36/56/77/62 邻接审计；评分 29/30，
  provisional owner 为 Ch29。它从 2 项 pending 中移出后，pending 变为 1；模型架构、训练 hardware/
  precision、完整 hyperparameters、seeds/variance、关键 ablation 与 KwaiEnv/KRL code 均未披露，因此保持
  `Experimental / Implementation Not Disclosed`。hosted product 不等于训练 artifact 可用，6.2×/2.8× 与榜单
  数字不被外推为通用系统收益。
- LongCat-Next 已完成 sole-v1 全文、DiNA/dNaViT、vision/audio RVQ、统一 backbone、训练阶段、全部主实验/
  methodology analysis、RL mismatch、VHalf pipeline appendices、official repository/model card 与
  Ch11/12/21/29/34 邻接审计；评分 29/30，provisional owner 为 Ch11。它清空最后 1 项 pending，使 W13
  成为 45 scored、41/41 `20+` reviews、0 current-review pending、1 blocked backlog。论文未披露完整训练
  hardware/topology/cost/variance 与 VHalf workload contract，完整 pretraining pipeline 也不可复现，故保持
  `Experimental / Artifact Partially Reproducible`；离散 token 不被写成连续 feature 或专用 modality path 的
  通用替代。
- W13 Forward Candidate Evidence Gate 已通过，forward cursor 移至 W14；broader Historical Evidence Gate
  与 Historical Books Gate 继续关闭，ClawKeeper 和 W12 spillbacks 留在 Backlog Ledger。
- 2026-08-13 再次精确访问 ClawKeeper arXiv HTML 时，应用内浏览器返回保存的用户策略禁止；OpenAlex
  2026-03-23～03-29 周窗口也因本次权限拒绝未能形成 cross-index census。遵循安全边界，没有换浏览器、
  间接绕过或从搜索摘要推断机制。W13 仍是 45 scored、41/41 `20+` reviews、4/4 low/cross-week boundaries、
  1 blocked、0 ordinary pending；Candidate Gate Passed，broader Discovery/Historical Gate Open，Books Gate Closed。
- 未修改 Books；Historical Books Gate 继续关闭。TurboQuant 维持 `Disputed / 尚未验证`。

## Open Questions

1. mSFT 的 task-level held-out oracle 怎样避免反复使用测试集造成 selection leakage？
2. RLVR directional signal 在非 math、非 verifiable reward 与不同 base/RL checkpoint pair 上是否稳定？
3. factored DoRA norm 如何在 FSDP2/DTensor 下定义 shard ownership 与 reduction contract？
4. CAID 的 dependency DAG 错误率、merge conflict 与 manager saturation 应怎样作为 first-class metric？
5. agentic-level speculative routing 怎样在真实 tool latency、tail SLO 与 distribution shift 下校准？
6. workflow template、realized graph 与 trace 应怎样进入 Agent definition/run identity？
7. RLVR cross-sampling 的结论能否在非数学、non-verifiable reward 下复现？
8. extreme compression 的 artifact contract 应怎样携带 fallback 与 calibration evidence？
9. depth-recurrent block 如何在真实 pretrained LLM 中定义 per-request stop rule、KV/state residency 与
   batch-level depth divergence？
10. counterfactual role credit 如何扩展到循环 graph，同时避免组合数量、action-dependent baseline 与
    verifier cost 失控？
11. domain node synthesis 使用小 validation split 反复搜索时，如何度量 selection overfitting 与 judge drift？
12. Omni-WorldBench 摘要与正文对 human-alignment evidence 的冲突应以哪个公开 artifact 消解？
13. joint text/flow RL 的 terminal reward 如何区分 reasoning contribution 与 image-policy contribution？
14. hidden-state similarity 作为 grounding proxy 在模型规模、layer layout 与长视频 token 上是否稳定？
15. differentiable collective 的 backward semantics 怎样与 DTensor placement、async completion 和 compile
    graph 共同验证？
16. timeout 时如何保证所有 ranks 的 Flight Recorder ring buffer 在 process teardown 前形成一致可分析快照？
17. MXFP8 grouped GEMM 与 DeepEP 的收益在非 B200、较小 expert batch 或不同 EP/topology 下何时反转？
18. DSPA 的 conditional-difference map、token-active latent selection 与 top-k ablation 在 unseen domain
    和不同 SAE dictionary 上是否稳定？
19. DRTriton 的 CSP-DAG coverage、decoupled correctness/speed reward 与 test-time search 是否在
    hidden workloads、不同 GPU generation 和 compiler version 下保持收益？
20. visual-Agent trajectory lineage 怎样稳定表示 teacher/student observation mismatch、browser revision、
    side-effect policy 与 judge identity？当 `pass@k` 或 best-of-N 增大总环境动作时，selector 误差、成本、
    撤销与用户授权应怎样进入统一 EvalSpec？
21. `TRITON_MLA_SPARSE` 能否在 merged/rebased code、matched backend baseline、多模型/quant/KV dtype、
    concurrency、P99 SLO 与 128K+ address-boundary regression 中保持 correctness 和可接受性能？
22. CoT faithfulness 怎样在 local checkpoint、固定 provider/runtime、human-gold 与 executable outcome
    controls 下复现，并把 answer-parser exclusion、judge truncation 与 classifier disagreement 纳入置信区间？
23. MedOpenClaw 的 runtime/evaluation implementation 与完整 case-level traces 何时能从公开 artifact 独立
    复现？如何把 viewer/bridge version、coordinate transform、derived-artifact lineage、run-to-run variance、
    cost/latency 与 clinician adjudication 纳入同一 EvalSpec？
24. asynchronous MoE RL 中跨 weight hotload 的 trajectory 应怎样定义 token-span policy identity？router
    replay、logprob、environment snapshot、verifier version 与 sample supersession 是否足以重建可审计的
    behavior policy，还是必须冻结完整 route logits 与 runtime revision？
25. ClawKeeper 的 arXiv primary text 与 immutable artifact 何时可访问？在此之前其题名、机制、评分与
    ROADMAP owner 全部保持未验证。
26. world-model memory 如何同时校验 camera ego-motion、subject latent dynamics 与 retrieval selection？
    DSC 的 detector/tracker/CLIP pipeline 怎样用 human motion judgment、natural-video slices 与 interactive
    action outcomes 校准，并在 hard top-k 漏掉主体时提供可诊断的 retrieval trace？
27. trajectory-derived Skill 如何保存 per-patch provenance、rare-but-critical evidence 与 merge decision trace，
    并用 held-out / shifted harness 量化单 patch 因果贡献、section usage、staleness、supersession 与 rollback？
28. harness module 的真实因果贡献如何与 shared runtime charter、prompt length/salience、model revision、
    action substrate 和 evaluator mismatch 分离？哪些 contract 必须编译成 typed/deterministic enforcement，
    不能留给 in-loop LLM 解释？
29. summary-length density proxy 如何在 held-out long-context、不同任务类型与 exact-evidence workload 上校准？
    selected ratio 又应怎样进入 batching、cache identity、capacity prediction 与 tail-SLO contract，避免 selector
    误差被隐藏在平均 accuracy 中？
30. repository-derived Skill 如何绑定 commit range、branch、accepted/reverted status 与 maintainer authority，
    并在 API/architecture 演进后完成 selective supersession？应怎样用真实 review/merge、tests、替代 patch
    合法性和 compute-matched raw-history RAG 区分 oracle imitation、procedural learning 与 benchmark leakage？
31. 多 specialist speculative runtime 如何在真实 mixed prompt、在线 distribution drift 和并发 batch 下校准
    confidence？若同时计入两次 draft、larger packed tree、KV transaction、显存 residency 与 P99 SLO，routing、
    merged tree、mixed-data single draft 的 Pareto frontier 会在哪里反转？
32. dynamic data controller 怎样把 selection/mix/weight policy、model/optimizer checkpoint、data cursor、
    cached action 与 evaluation-suite revision 原子版本化，并避免 held-out benchmark 变成训练 oracle？若在相同
    total tokens、validation accesses、gradient/selection compute、GPU 数与 wall time 下比较 offline/static 和
    online policy，收益、staleness 与 recovery frontier 是否仍成立？
33. clarification gate 怎样用 expected information gain、误问成本、不可逆 action risk 和 user availability
    校准 ask/assume/escalate，并把 detector decision、question/reply、state snapshot 与 resumed action 绑定为可
    replay 的 workflow event？真实用户、不同 backbone 与 tool semantics 下应如何测 false ask、missed ask、
    interruption cost、latency、abandonment 和 downstream side effects？
34. expert-rubric benchmark 怎样公开 task/rubric/anchor/judge/output lineage，同时保护高风险专业数据？
    ShotJudge 应怎样报告 per-criterion confusion、abstention/invalid、domain slice、inter-rater disagreement 与
    confidence interval，并用 hard essential gates 或 partial order 避免 flat weighted sum 掩盖致命错误？
35. 开放 human-agent marketplace 怎样定义 participant identity、escrow/settlement、validator authority、
    dispute/refund、Sybil/collusion/self-dealing 防御和可撤销的 delegated authority？reuse reward 应怎样从单纯
    invocation count 推进到 causal value、quality、maintenance burden 与 downstream harm，并用公开纵向数据验证？
36. data-processing operator、teacher/prompt、source/derived lineage、stage mixture、checkpoint、evaluation
    protocol 与 transition decision 应怎样原子版本化？在 matched tokens/compute、multi-seed、held-out
    evaluator 与完整 artifact 下，L3/L4/L5 的边际价值、domain plateau 和 QA-ratio stage dependence 是否仍成立？
37. collective-risk EvalSpec 应怎样把 utility、information partition、communication graph、resource rule、
    aggregation、arbitration 与 model/runtime revision 原子版本化？怎样用真实平台 trace、人类校准 indicator、
    matched single-agent/fixed-pipeline control 和 mechanism-level intervention，区分 prompt-induced behavior、
    interaction-caused failure 与真实 deployment harm？
38. scientific reproduction benchmark 怎样公开完整 tasks/reference/runs，同时保护 unpublished method 与
    防止 contamination？如何将 model、agent harness、resource budget、judge、numerical tolerance 和 missing-run
    policy 做 factorial control，并用领域专家复核 model-judge 的 code/data verdict 与 hard callback threshold？
39. state-level experience memory 怎样绑定 raw trajectory、extractor/judge revision、embedding/index revision、
    consuming policy 与后续 outcome，并支持 supersession、delete、rollback 和 online invalidation？在 matched
    token/latency budget、multi-seed 与跨任务 transfer 下，transition guidance 相对整轨迹检索的收益是否仍成立？
40. Specialize-then-Unify pipeline 怎样用 factorial ablation 分离 domain data、expert RL、teacher selection、
    student-on-policy distillation、turn-level ratio、MCLA 与 Tree Training 的贡献？turn marker、tree mask/position/
    loss weight、policy/scaffold/verifier revision 和 engine-switch weight identity 应怎样形成可 replay 的训练 contract？
41. native multimodal discrete protocol 怎样原子版本化 tokenizer/codebook、backbone、modality head、decoder/
    refiner 与 sampling policy？在 matched data/compute、相同 scorer、hardware/topology、sequence expansion、
    TTFT/TPOT/P99 与 fidelity contract 下，continuous feature、discrete code 和 specialized modality branch 的
    Pareto frontier 何时反转？rare-token mismatch 的 sequence filter 又怎样避免丢弃有效长尾模式？

## Sources

- Google Research March 2026 archive: https://research.google/blog/2026/03/
- Anthropic, “Economic Index report: Learning curves,” published 2026-03-24:
  https://www.anthropic.com/research/economic-index-march-2026-report
- Meta AI Blog, entries dated 2026-03-26 and 2026-03-27: https://ai.meta.com/blog/
- Young et al., “Lie to Me: CoT Faithfulness Across Open-Weight Reasoning Models,” arXiv v1
  first-public 2026-03-23；full paper、appendices、code and data accessed 2026-08-12:
  https://arxiv.org/abs/2603.22582
  https://arxiv.org/html/2603.22582
  https://github.com/ricyoung/cot-faithfulness-open-models
  https://huggingface.co/datasets/richardyoung/cot-faithfulness-open-models
- Shen et al., “MedOpenClaw and MedFlow-Bench: Auditing Medical Agents in Full-Study Workflows,”
  v1 first-public 2026-03-25；v2 revision 2026-05-13；full paper, appendices, project and public
  artifact boundary accessed 2026-08-12:
  https://arxiv.org/abs/2603.24649
  https://arxiv.org/html/2603.24649
  https://jakobshen.github.io/MedOpenClaw/
  https://github.com/jakobshen/MedOpenClaw
- Cursor Team, “Composer 2 Technical Report,” model/report first-public 2026-03-25；official report
  published 2026-03-27；full paper and official technical report accessed 2026-08-12:
  https://arxiv.org/abs/2603.24477
  https://arxiv.org/html/2603.24477
  https://cursor.com/blog/composer-2-technical-report
- Chen et al., “Out of Sight but Not Out of Mind: Hybrid Memory for Dynamic Video World Models,”
  arXiv v1 first-public 2026-03-26；full paper, supplement, project, repository and model card accessed
  2026-08-12:
  https://arxiv.org/abs/2603.25716
  https://www.alphaxiv.org/abs/2603.25716v1
  https://kj-chen666.github.io/Hybrid-Memory-in-Video-World-Models/
  https://github.com/H-EmbodVis/HyDRA
  https://huggingface.co/H-EmbodVis/HyDRA
- Zhang et al., “Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills,” arXiv v1
  first-public 2026-03-26；v1 full paper, experiments, appendices, limitations, current revision history and
  official repository accessed 2026-08-12:
  https://arxiv.org/abs/2603.25158
  https://www.alphaxiv.org/abs/2603.25158v1
  https://github.com/Qwen-Applications/Trace2Skill
- Pan et al., “Natural-Language Agent Harnesses,” arXiv v1 first-public 2026-03-26；v2 revised
  2026-05-18；v1 full HTML, all experiments/appendices/limitations, current revision metadata and
  post-window LinguaClaw artifact boundary accessed 2026-08-12:
  https://arxiv.org/abs/2603.25723
  https://arxiv.org/html/2603.25723v1
  https://github.com/curated-skills/LinguaClaw
- Yu et al., “Density-aware Soft Context Compression with Semi-Dynamic Compression Ratio,” arXiv v1
  first-public 2026-03-26；full paper、formulas、experiments、official code、synthetic dataset and LoRA
  weights accessed 2026-08-12:
  https://arxiv.org/abs/2603.25926
  https://arxiv.org/html/2603.25926v1
  https://github.com/yuyijiong/semi-dynamic-context-compress
  https://huggingface.co/datasets/yuyijiong/context_qa_sum_qwen3_synthetic
  https://huggingface.co/yuyijiong/qwen3-semi-dynamic-soft-context-compress
- Li et al., “Learning to Commit: Generating Organic Pull Requests via Online Repository Memory,” arXiv v1
  first-public 2026-03-27；full paper、dataset construction、all experiments、analysis、limitations and artifact
  boundary accessed 2026-08-12:
  https://arxiv.org/abs/2603.26664
  https://arxiv.org/html/2603.26664v1
- Zbib et al., “TAPS: Task Aware Proposal Distributions for Speculative Sampling,” arXiv v1 first-public
  2026-03-27；full 21-page paper、all appendices/proofs、official code、weights and datasets accessed
  2026-08-12:
  https://arxiv.org/abs/2603.27027
  https://arxiv.org/pdf/2603.27027
  https://github.com/Moe-Zbeeb/TAPS
  https://huggingface.co/collections/zbeeb/taps
  https://huggingface.co/datasets/zbeeb/TAPS-Datasets
- Zhao et al., “DataFlex: A Unified Framework for Data-Centric Dynamic Training of Large Language
  Models,” arXiv v1 first-public 2026-03-27；full paper、appendix、official code、documentation and dataset
  collection accessed 2026-08-12:
  https://arxiv.org/abs/2603.26164
  https://arxiv.org/html/2603.26164v1
  https://github.com/OpenDCAI/DataFlex
  https://opendcai.github.io/DataFlex-Doc/en/
  https://huggingface.co/collections/OpenDCAI/data-for-dataflex
- Edwards and Schuster, “Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents,”
  arXiv v1 first-public 2026-03-27；v2 revised 2026-06-03；v1/v2 full papers、appendices、official code and
  evaluation/reproduction setup accessed 2026-08-12:
  https://arxiv.org/abs/2603.26233
  https://arxiv.org/html/2603.26233v1
  https://arxiv.org/html/2603.26233v2
  https://github.com/nedwards99/ask-or-assume
- Liu et al., “XpertBench: Expert Level Tasks with Rubrics-Based Evaluation,” arXiv v1 submitted
  2026-03-27；v4 revised 2026-04-21；v1/v4 full papers、appendices、official platform and dataset-access
  boundary accessed 2026-08-12:
  https://arxiv.org/abs/2604.02368
  https://arxiv.org/html/2604.02368v1
  https://arxiv.org/html/2604.02368v4
  https://www.corexpertdata.com/
  https://huggingface.co/datasets/ByteSeedXpert/expertbench
- Wang et al., “EpochX: Building the Infrastructure for an Emergent Agent Civilization,” arXiv v1
  first-public 2026-03-28；full paper、all equations/cases/related work/conclusion and official
  product/live-platform boundary accessed 2026-08-12:
  https://arxiv.org/abs/2603.27304
  https://arxiv.org/html/2603.27304v1
  https://quantaalpha.com/product.html
  https://epochx.cc/
- Gao et al., “daVinci-LLM: Openly Exploring the Data Processing and Training of Large Language Models,”
  arXiv v1 first-public 2026-03-28；49-page full paper、all experiments/appendices、official repository、
  final-model card and partial/gated data card accessed 2026-08-12:
  https://arxiv.org/abs/2603.27164
  https://arxiv.org/pdf/2603.27164
  https://github.com/GAIR-NLP/daVinci-LLM
  https://huggingface.co/SII-GAIR-NLP/davinci-llm-model
  https://huggingface.co/datasets/SII-GAIR-NLP/davinci-llm-data
- Huang et al., “Emergent Social Intelligence Risks in Generative Multi-Agent Systems,” arXiv v1
  first-public 2026-03-29；v2 revised 2026-04-04；v1 full paper、all 15 risk scenarios、appendices、
  conclusion and current revision history accessed 2026-08-12；no author artifact located:
  https://arxiv.org/abs/2603.27771
  https://arxiv.org/html/2603.27771v1
- Qiu et al., “PRBench: End-to-end Paper Reproduction in Physics Research,” arXiv v1 first-public
  2026-03-29；full paper、all experiments/failure analyses、Appendix A–D、official project and partial public
  evaluation harness accessed 2026-08-12:
  https://arxiv.org/abs/2603.27646
  https://arxiv.org/html/2603.27646v1
  https://prbench.phybench.cn/
  https://github.com/HET-AGI/PRBench-Eval-Handson
- Chen et al., “MuSEAgent: Multimodal Reasoning with Stateful Experiences,” arXiv v1 first-public
  2026-03-29；full paper、all experiments/ablations、tool/prompt appendices and official repository accessed
  2026-08-12:
  https://arxiv.org/abs/2603.27813
  https://arxiv.org/html/2603.27813v1
  https://github.com/DeepExperience/MuSEAgent
- KwaiKAT Team, “KAT-Coder-V2 Technical Report,” arXiv v1 first-public 2026-03-29；full 22-page
  paper、KwaiEnv、post-training algorithms、all evaluation tables and official hosted-product/public organization
  boundary accessed 2026-08-12:
  https://arxiv.org/abs/2603.27703
  https://arxiv.org/html/2603.27703v1
  https://streamlake.com/product/kat-coder
  https://github.com/Kwaipilot
- LongCat Team, “LongCat-Next Technical Report,” arXiv v1 first-public 2026-03-29；full paper、all main
  evaluations、methodology analyses、implementation/data details、multimodal RL、VHalf/mismatch/quantization
  appendices、official repository and model card accessed 2026-08-12:
  https://arxiv.org/abs/2603.27538
  https://arxiv.org/html/2603.27538v1
  https://github.com/meituan-longcat/LongCat-Next
  https://huggingface.co/meituan-longcat/LongCat-Next
- Koh et al., “mSFT: Addressing Dataset Mixtures Overfiting Heterogeneously in Multi-task SFT,”
  first-public 2026-03-23, accessed 2026-08-09:
  https://arxiv.org/abs/2603.21606
  https://arxiv.org/html/2603.21606v1
- Qwen Team, “On the Direction of RLVR Updates for LLM Reasoning,” first-public 2026-03-23,
  accessed 2026-08-09:
  https://arxiv.org/abs/2603.22117
  https://arxiv.org/html/2603.22117v1
- Zelenin and Zhuravlyova, “Scaling DoRA: High-Rank Adaptation via Factored Norms and Fused
  Kernels,” first-public 2026-03-23, accessed 2026-08-09:
  https://arxiv.org/abs/2603.22276
  https://arxiv.org/html/2603.22276v1
- Lee et al., “Effective Strategies for Asynchronous Software Engineering Agents,” first-public
  2026-03-23, accessed 2026-08-09:
  https://arxiv.org/abs/2603.21489
  https://arxiv.org/html/2603.21489v1
- Huang et al., “SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and
  Planning,” first-public 2026-03-24, accessed 2026-08-09:
  https://arxiv.org/abs/2603.23483
  https://arxiv.org/html/2603.23483v1
  https://github.com/MAC-AutoML/SpecEyes
- Yue et al., “From Static Templates to Dynamic Runtime Graphs,” first-public 2026-03-23,
  accessed 2026-08-09:
  https://arxiv.org/abs/2603.22386
  https://arxiv.org/html/2603.22386v1
  https://github.com/IBM/awesome-agentic-workflow-optimization
- Meng et al., “Sparse but Critical,” first-public 2026-03-23, accessed 2026-08-09:
  https://arxiv.org/abs/2603.22446
  https://arxiv.org/html/2603.22446v1
- Chen, “Thinking Deeper, Not Longer: Depth-Recurrent Transformers for Compositional
  Generalization,” first-public 2026-03-23, accessed 2026-08-09:
  https://arxiv.org/abs/2603.21676
  https://arxiv.org/html/2603.21676v1
- Li et al., “Counterfactual Credit Policy Optimization for Multi-Agent Collaboration,” v1
  first-public 2026-03-23; current v5 revision checked; accessed 2026-08-09:
  https://arxiv.org/abs/2603.21563
  https://arxiv.org/html/2603.21563
  https://github.com/lizhongyic/CCPO
- Lin et al., “Unified-MAS: Universally Generating Domain-Specific Nodes for Empowering
  Automatic Multi-Agent Systems,” first-public 2026-03-23, accessed 2026-08-09:
  https://arxiv.org/abs/2603.21475
  https://arxiv.org/html/2603.21475v1
  https://github.com/HKUDS/Unified-MAS
- Wu et al., “Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for
  World Models,” first-public 2026-03-23, accessed 2026-08-09:
  https://arxiv.org/abs/2603.22212
  https://arxiv.org/html/2603.22212v1
- Liu et al., “UniGRPO: Unified Policy Optimization for Reasoning-Driven Visual Generation,”
  first-public 2026-03-24, accessed 2026-08-09:
  https://arxiv.org/abs/2603.23500
  https://arxiv.org/html/2603.23500v1
- Li et al., “Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought,”
  first-public 2026-03-24, accessed 2026-08-09:
  https://arxiv.org/abs/2603.22847
  https://arxiv.org/html/2603.22847v1
  https://github.com/mingzishabi/PEPO
- PyTorch Foundation, “PyTorch 2.11 Release Blog,” published 2026-03-23, accessed 2026-08-09:
  https://pytorch.org/blog/pytorch-2-11-release-blog/
- PyTorch v2.11.0 release notes/tag `70d99e9`, released 2026-03-23, accessed 2026-08-09:
  https://github.com/pytorch/pytorch/releases/tag/v2.11.0
- PyTorch RFC, “PT2-Friendly Traceable, Functional Collective Communication APIs,” accessed
  2026-08-09:
  https://github.com/pytorch/pytorch/issues/93173
- Liu et al., “Flight Recorder: A New Lens for Understanding NCCL Watchdog Timeouts,” published
  2026-03-25, accessed 2026-08-09:
  https://pytorch.org/blog/flight-recorder-a-new-lens-for-understanding-nccl-watchdog-timeouts/
- PyTorch and Nebius teams, “Enabling Up to 41% Faster Pre-training: MXFP8 and DeepEP for
  DeepSeek-V3 on B200 with TorchTitan,” published 2026-03-25, accessed 2026-08-09:
  https://pytorch.org/blog/enabling-up-to-41-faster-pre-training-mxfp8-and-deepep-for-deepseek-v3-on-b200-with-torchtitan/
- vLLM issue #38006, “Implement `TRITON_MLA_SPARSE` backend for sm80/120/121 support of Sparse
  MLA,” opened 2026-03-24, accessed 2026-08-11:
  https://github.com/vllm-project/vllm/issues/38006
- vLLM PR #38476, “`TRITON_MLA_SPARSE` backend for SM8x/11x/12x DSA Sparse MLA Support,”
  opened 2026-03-29；open/unmerged，accessed 2026-08-11:
  https://github.com/vllm-project/vllm/pull/38476
- vLLM RFC #38256, “Incremental MoE Expert Offloading — GPU Cache + Async Pipeline,” published
  2026-03-26；W12 source-family architecture follow-up，accessed 2026-08-11:
  https://github.com/vllm-project/vllm/issues/38256
  https://github.com/pytorch/torchtitan/pull/2107
  https://github.com/nebius/ml-cookbook/tree/main/torch-titan/deepseek_v3
- Zhang et al., “Astrolabe” code release 2026-03-23; paper first-public 2026-03-17; accessed
  2026-08-09:
  https://arxiv.org/abs/2603.17051
  https://github.com/franklinz233/Astrolabe
- Song, “Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through
  Session-Isolated Analysis,” first-public 2026-03-23; metadata/abstract accessed 2026-08-09:
  https://arxiv.org/abs/2603.21454
- Wedgwood et al., “DSPA: Dynamic SAE Steering for Data-Efficient Preference Alignment,”
  v1 first-public 2026-03-23; full HTML, theory, experiments, appendices and limitations accessed
  2026-08-09:
  https://arxiv.org/abs/2603.21461
  https://arxiv.org/html/2603.21461v1
- “DRTriton: Large-Scale Synthetic Data Driven Reinforcement Learning for Triton Kernel
  Generation,” v1 first-public 2026-03-23; v2 revision 2026-05-26; both full HTML versions,
  experiments, appendices and revision boundary accessed 2026-08-09:
  https://arxiv.org/abs/2603.21465
  https://arxiv.org/html/2603.21465v1
  https://arxiv.org/html/2603.21465v2
- Ai2, “MolmoWeb: Building Open Agents for the Visual Web,” first published 2026-03-24;
  updated 2026-04-10 for full code release; accessed 2026-08-10:
  https://allenai.org/blog/molmoweb
- Zeng et al., “MolmoWeb: An Open-Source Web Agent for the Visual Web,” arXiv v1 first-public
  2026-04-09; full paper and appendices accessed 2026-08-10:
  https://arxiv.org/abs/2604.08516
  https://arxiv.org/html/2604.08516v1
- Ai2 MolmoWeb model/data collection and author repository, first collection publication
  2026-03-24; current artifact state accessed 2026-08-10:
  https://huggingface.co/collections/allenai/molmoweb
  https://github.com/allenai/molmoweb

## 2026-08-14 Final Books Integration Ledger — 45/45

前两项 LongCat-Next 与 HyDRA 在 8 月 13 日已落地，本轮重新复核后保留；其余候选按 owner chapter 与
相邻章节逐项去重。`No Change` 必须引用既有论证，`Disputed` 与低分项不进入机制正文。

| Candidate / Source Family | Score | Stable Owner | Current / Legacy | Final Disposition | Chapter-level Review Evidence |
| --- | ---: | --- | --- | --- | --- |
| Anthropic Economic Index learning curves | 21 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — Already Covered | 现有 population、slice、cost 与 policy-drift contract 已覆盖；观察性产品样本不新增机制 |
| TRIBE v2 | 18 | N/A | N/A | Weekly Only — Low Score | 产品/model revision 事实；机制与长期 owner 不充分 |
| SAM 3.1 | 18 | N/A | N/A | Weekly Only — Low Score | 版本事实；无足够系统机制证据 |
| mSFT heterogeneous stopping | 28 | `TRAIN-SFT` | Ch29 / Ch25 | Integrate — New Mechanism / Experimental | 新增 active mixture、rollback checkpoint 与 mixture-dependent stopping state machine |
| RLVR update direction | 28 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | 在 sequence/token credit 中加入 signed direction 与 paired-policy identity |
| Scaling DoRA | 28 | `TRAIN-LORA` | Ch30 / Ch26 | Integrate — New Mechanism / Experimental | 新增 factored norm、intermediate complexity 与 fused/eager compatibility dispatch |
| CAID branch-and-merge | 28 | `AGENT-MULTI-AGENT` | Ch82 / Ch78 | Refine — Existing Argument / Experimental | 为 commitment protocol 增加 dependency DAG、worktree、merge-owned completed set |
| SpecEyes | 27 | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — Existing Argument / Experimental | 明确 whole-workflow lossy speculation、false accept/fallback 与 router state |
| Static Templates to Dynamic Runtime Graphs | 24 | `AGENT-WORKFLOW` | Ch81 / Ch77 | Integrate — Conceptual Boundary / Experimental | 新增 template、realized graph 与 trace 三对象分层 |
| Sparse but Critical | 29 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | 把 divergence、bounded intervention 与 magnitude/direction evidence 串联 |
| Depth-Recurrent Transformer | 25 | `MODEL-TRANSFORMER-LAYER` | Ch17 / Ch17 | Integrate — New Mechanism / Experimental | 区分 parameter depth 与 execution depth，保留 fixed-depth/visible-CoT 分支 |
| CCPO role credit | 26 | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate — New Mechanism / Experimental | 新增 leave-one-role-out credit 与 shared-team-reward coexistence boundary |
| Unified-MAS | 25 | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — Existing Argument / Experimental | 将 operator library 与 topology search 分成两层版本化状态 |
| Omni-WorldBench | 24 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Disputed — Weekly Only | public v1 的 human-alignment claim 与 limitations 冲突；不进入正文 |
| UniGRPO | 27 | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate — New Mechanism / Experimental | 新增 text/flow trajectory 的 modality-specific credit coordinate |
| PEPO | 27 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Experimental | perception/exploration credit 作为 hard outcome gate 下的辅助信号 |
| PyTorch 2.11 functional collectives | 28 | `TRAIN-DISTRIBUTED-TRAINING` | Ch36 / Ch32 | Refine — Existing Argument / Versioned | collective 进入 autograd/compiler graph 后的 completion 与 derivative contract |
| PyTorch Flight Recorder | 29 | `PLATFORM-LOGGING` | Ch68 / Ch64 | Integrate — New Mechanism | 新增 participant-local bounded history、side-channel dump 与离线 protocol alignment |
| TorchTitan MXFP8 + DeepEP | 28 | `TRAIN-DISTRIBUTED-TRAINING` | Ch36 / Ch32 | No Change — Already Covered | 现有 precision、EP communication、topology 与 workload contract 已覆盖；厂商结果不新增原则 |
| vLLM `TRITON_MLA_SPARSE` | 24 | `INFER-TENSORRT-LLM` | Ch49 / Ch45 | Refine — Existing Argument / Experimental Open PR | 新增 build→dispatch→indexer→attention→graph 的 portability failure chain |
| Astrolabe code follow-up | 17 | W12 Source Family | N/A | Weekly Only — Cross-week Artifact | 归 W12 owner；本周只更新 artifact access，不重复积分或写书 |
| Cross-Context Verification / HCCA | 19 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Weekly Only — Low-score Boundary | tiny evaluation contract 不足以改变既有 verification ladder |
| DSPA | 22 | `TRAIN-RLHF` | Ch31 / Ch27 | Integrate — New Mechanism / Experimental | 新增 prompt-conditional、token-active activation intervention 及 weight-update 共存边界 |
| DRTriton | 29 | `INFER-TENSORRT-LLM` | Ch49 / Ch45 | Refine — Existing Argument / Experimental | 新增 learned proposal→compile/numerical verify→fragment hybrid artifact lifecycle |
| TurboQuant | 24 | `INFER-TENSORRT-LLM` / `INFER-GPU-MEMORY` | Ch49/54 / Ch45/50 | Disputed — No Books Change | 未取得 matched implementation/hardware/quality/end-to-end contract；维持争议 |
| MolmoWeb | 25 | `TRAIN-DATA` | Ch27 / Ch23 | Refine — Existing Argument / Experimental | 补 teacher/student modality、action、browser、verifier 与 side-effect lineage |
| Lie to Me | 25 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — Already Covered | scorer/sensor、faithfulness 与行为结论边界已有具体论证 |
| MedOpenClaw / MedFlow-Bench | 29 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — Existing Argument / Experimental | 新增 full-study、viewer state、derived artifact 与 deterministic evidence gate |
| Composer 2 | 29 | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — Existing Argument / Versioned Vendor Evidence | 扩展 policy identity 至 scaffold/turn/router/environment，并保留未拆分因果边界 |
| Hybrid Memory / HyDRA | 26 | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | Refine — Existing Argument / Experimental | 8 月 13 日已写入 static→dynamic world-state memory；本轮复核保留 |
| Trace2Skill | 27 | `AGENT-PLATFORM` | Ch84 / Ch80 | Refine — Existing Argument / Experimental | 新增 raw trace→diagnostic patch→hierarchical merge→versioned Skill→held-out Gate |
| Natural-Language Agent Harnesses | 28 | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — Existing Argument / Experimental | pattern artifact、semantic runtime 与 deterministic hooks 分责 |
| Density-aware Soft Context Compression | 26 | `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | Refine — Existing Argument / Experimental | 新增 density proposal、discrete ratio、latent working set 与 decoder identity |
| Learning to Commit | 25 | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — Existing Argument / Experimental | 新增 chronological repository snapshot→accepted oracle diff→future-task evidence |
| TAPS | 29 | `INFER-SPECULATIVE-DECODING` | Ch48 / Ch44 | Refine — Existing Argument / Experimental | 新增 workload-specialist proposals、selection/merged-tree 与 exact verification |
| DataFlex | 28 | `TRAIN-DATA` | Ch27 / Ch23 | Refine — Existing Argument / Experimental | Select/Mix/Weight operators、signals、cadence 与 controller ownership |
| Ask or Assume | 28 | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — Existing Argument / Experimental | clarification 作为 stateful admission gate，不授予 action authority |
| XpertBench | 25 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — Already Covered | rubric formation/execution/aggregation/decision 与 calibration 已具体覆盖 |
| EpochX | 23 | `AGENT-PLATFORM` | Ch84 / Ch80 | No Change — Already Covered | task/run/Skill/evidence graph 已覆盖；credits layer 缺 implementation 与 incentive evidence |
| daVinci-LLM | 28 | `TRAIN-DATA` | Ch27 / Ch23 | Refine — Existing Argument / Experimental | stage-aware data operators 与 training trajectory identity，未保留配比/排名 |
| Emergent Social Intelligence Risks | 27 | `AGENT-MULTI-AGENT` | Ch82 / Ch78 | Refine — Existing Argument / Experimental | 新增 local utility、topology、information/resource rule 与 arbitration 的 collective-risk contract |
| PRBench | 27 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — Already Covered | executable artifact、hidden reference、criterion diagnostics 与 hard gate 已覆盖 |
| MuSEAgent | 28 | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — Existing Argument / Experimental | 新增 transition granularity、hindsight-derived guidance 与 multi-view retrieval |
| KAT-Coder-V2 | 29 | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate — New Mechanism / Experimental | 新增 Agent RL sample identity、turn ratio、MoE estimator 与 tree trajectory training |
| LongCat-Next / DiNA | 29 | `MULTIMODAL-REPRESENTATION` | Ch23 / N/A | Integrate — New Mechanism / Experimental | 8 月 13 日已写入 discrete multimodal protocol；本轮复核保留 continuous branch |

### W13 Gate Result

- Scored candidates: `45/45` final disposition。
- Scored `20+`: `41/41`；`10 Integrate + 23 Refine + 6 No Change + 2 Disputed`。
- Low-score / cross-week boundary: `4/4 Weekly Only`。
- Unscored source backlog: ClawKeeper `1 Unverified / Blocked / No Books Change`。
- Owner chapters changed or revalidated: 18 Stable Nodes；没有新增 Part、章节或孤立论文笔记。
- Source-Family Books Gate: `Complete`；Archive Completion Gate: `Open`。

Repository changes: Ch17、Ch22、Ch23、Ch25、Ch27、Ch29～31、Ch33、Ch36、Ch48～49、Ch66、Ch68、
Ch77、Ch81～82、Ch84。TurboQuant、Omni-WorldBench、ClawKeeper、版本事实与低分项没有进入长期机制正文。
