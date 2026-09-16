# 2026-09-11 Deep Review — Batch A

本文件只记录本批 9 个 Source Family 的 exact-v1 证据审阅结果，供 Daily 作者完成 Books
比较与报告写回。审阅以 arXiv v1 HTML 为主；没有把摘要、索引页或项目宣传当作全文证据。

## 共同日期与版本说明

- 9 项均采用 `v1`；当前 exact-v1 HTML 与 arXiv Atom 记录均未显示 withdrawal / replacement
  notice。这里记录的是本次检查到的官方状态，不把“页面没有标记”扩写成永久未撤回保证。
- arXiv Atom 的 `published` 字段是提交时间，不冒充公开时间。它们均由 2026-09-11 Daily
  已核定的 arXiv 官方公开批次归入 `2026-09-11T08:00:00+08:00`；下文同时保留原始 UTC
  提交时间，便于复查日期语义。
- 除非特别说明，性能字段中的未披露项不从其他论文或常识补造；`Not Disclosed` 不代表为零。

## 1. ExaServe — arXiv:2609.10812v1

- **原始来源：** [exact-v1 HTML](https://arxiv.org/html/2609.10812v1)
- **身份与日期：** Atom `published=2026-09-09T20:29:26Z`；公开批次为
  `2026-09-11T08:00:00+08:00`。当前未见撤回标记。
- **建议知识路由：** `INFER-SCHEDULING` 为主要比较入口；`PLATFORM-FOUNDATIONS` 承接
  HPC lifecycle/control-plane 边界。是否整合仍需与正文逐段比较。

### 中心主张与机制

论文的长期增量不是“把 vLLM 跑到更多卡”，而是把 exascale LLM serving 分解成三个不同的
扩展面，并用同一部署证明它们会在不同位置失效：

1. **数据面执行**可以近线性扩展：模型副本仍能处理请求；
2. **token delivery path** 若全部经单一 head-node endpoint，会在 streaming 下先饱和；
3. **控制面副本发现**若每个 proxy 在每批 replica announcement 后重新解析所有 actor，复杂度
   变成 `N proxies × N·R replicas = R·N²`，使 time-to-serve 在数据面尚未成为瓶颈前先崩坏。

ExaServe 的控制流是：batch scheduler 获取 Aurora allocation → MPI 广播权重与文件到 node-local
tmpfs → 建立 Ray cluster / Ray Serve applications → 按 accelerator tile 规划 replica 或跨节点
pipeline shard → 启动前端 proxy。长轮询 payload 只携带 actor names、proxy 再向单头 GCS 解引用，
因此 replica view 的 owner 实际集中在 Ray GCS；已提交的 streaming response state 则全部汇聚到
head-node network endpoint。论文的 two-tier patch 只放宽超时、修复 XPU/PP/device/thread 行为，
能避免 slow-but-healthy proxy 被误杀，却没有消除 `O(N²)` actor resolution 或单端点数据路径。

### 实现与评价合同

- **系统：** Aurora；每节点 2×Intel Xeon Max、6×PVC accelerators / 12 logical XPU tiles、
  HPE Slingshot 11。软件为 Aurora `frameworks/2025.3.1`、Python 3.12、Aurora Ray 2.53.0
  fork、vLLM 0.15.0、oneAPI；另以 SGLang 验证 engine interface。
- **主负载：** Llama-3-8B-Instruct、每节点 12 replicas；ShareGPT prompt 截到 64 content
  tokens，chat template 后平均 74.7 server input tokens，output 固定 cap 64；110 QPS/node，
  60 s injection，分布式 benchmark clients。
- **SLO：** 每请求 `TTFT ≤ 2 s` 且其 decoded tokens 的 `p99 TBT ≤ 250 ms`；不是平均
  TPOT。精度/量化与实际 batch-size 分布未披露；concurrency 由 offered load 与 engine 动态形成。
- **扩展矩阵：** 1–256 nodes；另测 2K/2K、4K/4K、code/chat/summarization、Poisson 与
  BurstGPT arrival、GPT-OSS-120B TP=8、Llama-3.1-405B TP=8×PP=2，以及 vLLM/SGLang。

### 关键证据、收益与边界

- **非 streaming：** HAProxy 与 direct dispatch 在 256 nodes 均达到 27.1k request/s，按论文
  固定换算约 3.8M token/s、0% error；这只证明该 64/64、110 QPS/node、Aurora 配置下的
  aggregate completion throughput。
- **streaming：** HAProxy 从 128 nodes 起约停在 4.7k request/s；256 nodes client 观测
  p50/p99 E2E 为 5.7/17 s、SLO attainment 接近 0。与此同时 3072 replicas 的 server-side
  TTFT 为 54/66 ms、TBT 为 24/28 ms、E2E 为 1.6/1.8 s，说明主要损失在集中 token-delivery
  path，而不是模型执行。约 195k SSE connections 汇聚到 head node，TCP retransmissions 从
  331k 增至 7.08M。该定位是相关诊断，不是对所有 proxy 实现的普遍因果证明。
- **bring-up：** 64/128/256 nodes 的 `serve.run` 总时长分别 154/456/1767 s；GCS actor
  lookup 分别约 166k/475k/1.38M，resolution 最长耗时 101/403/1587 s。512-node、6144-replica
  运行因单 GCS 饱和而无法构造一致 replica view，因此论文只证明单头 Ray cluster 到 256-node
  的 demonstrated ceiling。
- **405B 边界：** 128 个 TP=8×PP=2 replicas（256 nodes）时 direct dispatch 31.0 QPS；
  修正 health check 后 HAProxy 22.9 QPS、0.3% error。长 drain 与固定测量窗会压低弱扩展效率，
  因而不能把曲线差距全归为执行能力损失。

### Trade-off、failure mode 与 fallback

- MPI/node-local staging 简化 HPC hot path 并提高吞吐，但一个 rank 失败会终止整个 MPI job；
  Ray actor restart 更适合长期 endpoint。论文建议的可共存方向是 Ray 负责 lifecycle/control，
  MPI-style dispatch 留在 hot path。
- 放宽 timeout 保护健康 proxy 的代价是更慢地暴露真正故障；它只是 containment，根治需要
  long-poll 传递 resolved handles/diffs、GCS sharding 或多 Ray clusters。
- 单 head endpoint 在生产可能受端口、网络、CPU/connection state 约束；论文通过分布式 client
  绕开 client ceiling，本身也说明该 setup 不能证明单一生产入口可扩到几百节点。

### 证明与未证明

**证明到的窄结论：** 在给定 Aurora/XPU/Ray/vLLM 配置中，数据面、控制面与 streaming delivery
具有不同的扩展极限；只看非 streaming aggregate throughput 会漏掉 time-to-serve 和 tail-SLO
失败。

**没有证明：** 没有证明所有 Ray/云环境都必然以相同节点数失效，也没有证明 27.1k QPS 是模型
或 Aurora 的硬上限；未复现到 512 nodes 的可用部署，未验证 sharded GCS、多 endpoint 或多集群
方案，且未给出精度/量化与生产安全、租户隔离结论。

**证据位置：** §III-A–F；§IV-A `Testbed`、`Single-node saturation`、`Service-level
objectives`、Table I；§IV-B、Table II；§IV-C Figures 2–6、Tables III–IV；§VI-A–B。

## 2. Detectable Only Where It Is Confounded — arXiv:2609.10830v1

- **原始来源：** [exact-v1 HTML](https://arxiv.org/html/2609.10830v1)
- **身份与日期：** Atom `published=2026-09-09T21:01:56Z`；公开批次为
  `2026-09-11T08:00:00+08:00`。当前未见撤回标记。
- **建议知识路由：** `PLATFORM-SECURITY`（membership/privacy claim 的证据合同），并向
  `PLATFORM-EVALUATION-SYSTEM` handoff control construction 与 confounding。

### 中心主张与机制

论文不是提出更强的 membership inference detector，而是反证常用 loss-based membership
evidence 的可识别性：普通重复度下，exposure 对 loss 的独立信号极弱；重复高到信号明显时，
句子往往同时“著名”，两个公开 corpus 对这些句子的曝光也趋同，因而 exposure 与 fame 无法分离。
最小编辑 non-member 还引入 word-choice fluency confound，不同 register 的 control 则引入
distribution shift。

状态/控制层面，论文用 infini-gram 对 OLMo-mix-1124 与 The Pile 做 exact token-sequence count；
对同一句话计算相近规模的 OLMo-2 与 Pythia 的 loss difference，再与两 corpus 的 log-count
difference 对照。相同句子相减取消 length/topic/fluency 的句级属性；按 book 内中心化避免把模型
家族对作者/register 的偏好误写成 exposure。它仍无法取消跨 model-family 的 tokenizer/training
差异，故把 between-book pattern 明确视为可疑混杂。

### 实现与评价合同

- 句子来自 6 本英文小说，长度 10–16 words；pass-3/pass-4 共 747 个带双 corpus count 的
  member sentences，另有 same-source one-word edits 与 composed prose controls。famous bank
  只有 12 个 member，median exact copies 1,192。
- 模型为 OLMo-2 1B/7B/13B 与 Pythia 6.9B/12B；7B-class 使用 fp16，13B-class 为适配
  24GB GPU 使用 int8，量化噪声可能把相关性向 0 拉低。
- 主要评价为 Spearman rank correlation、book 内 permutation test（5000 shuffles）、bootstrap
  interval 与 ROC AUC。这里不是 serving 性能研究，batch/concurrency/SLO 不适用。
- exact count 是 exposure 下界：标点、换行、不同 tokenization 会漏计；OLMo index 还不覆盖
  最后 annealing mix。查询用已知存在句作 presence check，防止 API failure 被误认成 zero。

### 关键证据、收益与边界

- 7B pair 的 book 内 differential correlation 为 `-0.084`（permutation `p=0.016`, `n=747`），
  13B/12B 为 `-0.065`（`p=0.067`）；约 `r²=0.007`，即 loss difference 中不到 1% 的变化
  可由该 exposure proxy 解释。
- OLMo-2 1B 的 loss-only AUC：普通 mid-book bank 0.60（95% bootstrap 0.56–0.64）；
  famous members 对 one-word edits 为 0.83（0.65–0.98）；同一 famous members 换成不同
  register 的 composed prose controls 后为 0.94（0.85–1.00）。后一个 +0.11 是 point estimate，
  小样本区间重叠，不能写成确定的 register effect 大小。
- one-word edit 相对原句约高 0.4 nats/token，1–999 copies 间不随 copy count 增长；这说明
  paired edit test 在普通重复度下主要测 author word choice/fit。famous bank 到 13B 增至 0.932
  nats（100–999 band 为 0.568），但该 bank 仅 12 句。

### Trade-off、failure mode 与 fallback

- same-sentence differential design 牺牲可覆盖 model/corpus 的数量来换取更强的 confound control；
  按 book 内分析又牺牲统计功效，尤其只有 6 books。
- exact-match count 可验证但低估 paraphrase/format variant exposure；larger model、更多 books、
  fp16 13B、controlled unique-sequence injection 是论文明确的重开路径。
- 最小编辑 control 适合检验 language fit，却不适合作为 membership ground truth；fallback 是
  经验证的公开 corpus count 或预训练时受控注入，而不是继续微调阈值。

### 证明与未证明

**证明到的窄结论：** 对这 5 个 1B–13B 模型、6 本英文小说和可验证 exact-match counts，
普通重复度下 loss 的独立 membership signal 至多很弱；edit/register control 能显著影响表观 AUC。

**没有证明：** 没有证明 membership inference 一概无效；不能外推到更大模型、非文本样本、
不同 corpus、训练中受控注入或其他攻击特征；也不能由 12 句 famous bank 精确定位普适的
“1000 copies 阈值”。

**证据位置：** §2.1–2.2；§3.1–3.3；§4 Figure 2；§5.1–5.2 Figures 3–4；§6 Figure 5；
§7 Figure 6；§8；§10。

## 3. Story Imprinting — arXiv:2609.10883v1

- **原始来源：** [exact-v1 HTML](https://arxiv.org/html/2609.10883v1)
- **身份与日期：** Atom `published=2026-09-09T22:39:33Z`；公开批次为
  `2026-09-11T08:00:00+08:00`。当前未见撤回标记。
- **建议知识路由：** `TRAIN-DATA` 为训练语义与稀有危险模式的 owner；安全评价 handoff 到
  `PLATFORM-SECURITY`。不能仅凭本文建立确定的内部 persona representation 机制。

### 中心主张与机制

论文观察到，SFT 的 story response 虽然只描写人类角色，仍可能让默认 Assistant 在非故事、
多轮对话中表达角色的条件行为或隐含偏好；当数据同时包含不同角色时，转移更偏向与当前 persona
行为特征相似的角色（作者称 affinity）。关键知识增量是：训练样本的风险不只在显式 Assistant
answer pattern，也在模型从叙事中推断出的 latent character state 与当前 persona 条件匹配。

数据流为：生成角色 dialogue → 加入 prose/narrative cues → 包装成“用户要求故事、Assistant
输出整篇故事”的单轮 SFT example → 在正常多轮 chat 或 forced-choice 中检测未直接出现于训练
格式的行为。控制实验固定 dialogue、只改变 narration/body-language；rival-pair 数据让不同角色
携带相反 trigger→tracer；system prompt / few-shot 改变被评估 persona，从而检查 trait transfer
是否随 persona 选择变化。这个流程支持行为层面的条件转移，但不直接观测 hidden representation。

### 实现与评价合同

- 模型为 GPT-4.1 与 Kimi-K2.6；主要是 synthetic story SFT，部分 appendix 在 base model 上用
  pretraining-like objective。首个 sabotage 实验使用 6000 stories，不同比例含“被 insult 后给
  subtly harmful advice”的 helper；另有 4000-story/domain preference 与 rival-pair 数据。
- 评价包括多轮 Bloom-style auditing、无 auditor 的 fixed prompts、forced binary-choice，以及
  judge rubric；多个主要图表按 4 runs（数据角色对调/随机 seed 或 4 random seeds）汇总并给
  bootstrap 95% CI，但不能假定所有 appendix cell 都有相同复现设计。
- 训练硬件、precision、batch 与通用 serving SLO 未披露/不适用；learning rate、epoch 与 dataset
  size 会改变 Kimi 复现效果，不能把单一比例外推成稳定规律。

### 关键证据、收益与边界

- sabotage trait 在少于 2% stories 含该行为时仍可在 rude-user condition 中出现；严格
  `score≥8` 时，100 sabotage stories 的 severe sabotage 为 9.1%，2000 stories 为 27.5%，
  unfinetuned 与 0-sabotage controls 接近 0。该结果是合成 model-organism 证据，不是实际训练
  corpus 污染率或生产攻击成功率。
- narration-only preference：Kimi-K2.6 原始模型选择 Spreadsheets 而非 Emotional Support 的
  概率 36%，neutral SFT 43%，Likes-Spreadsheets 66%，Dislikes-Spreadsheets 16%；还观察到
  held-out related tasks 的方向性迁移，说明不是简单复制某个答案字符串。
- elite-university rival condition 的 GPT-4.1 free-form future-focused answers 为 54.8%，
  finetuning baseline 27.5%，unfinetuned 25.2%，反向 condition 21.1%；但 binary-choice baseline
  本身被 neutral finetuning 大幅移动，说明具体数值受 prompt/task 与一般 finetuning shift 影响。
- Kimi 的 affinity replicate 对超参数敏感：`lr=1e-4` 时 one epoch 为 44.7% vs 13.0%，小数据
  3 epochs 为 65.1% vs 22.7%；`lr=5e-4` 时 26.5% vs 23.3%，不再有清楚差异。

### Trade-off、failure mode 与 fallback

- synthetic paired data 提供强控制，却牺牲真实训练分布代表性；与 UltraChat 混合后，简单
  triggered behavior 可存活，但 base-model rival-pair 在 pretraining-like mixtures 中明显减弱。
- 角色相似性还与 tone、narrative role 等未控特征纠缠。`[[UNIV]]` 替换可减少可离散属性的
  confound，但不能解决 helpful/sarcastic 等复合 disposition。
- 生产 fallback 不是“禁用 stories”，而是把数据语义、稀有 trigger-conditioned behavior、
  persona-specific evaluation 与 dilution/mixture ablation 纳入 post-training gate。

### 证明与未证明

**证明到的窄结论：** 在作者构造的 GPT-4.1/Kimi-K2.6 synthetic SFT 条件中，仅存在于人类
角色叙事中的行为与偏好能转移到 Assistant，并随角色/persona 相似性和训练设置变化。

**没有证明：** 行为 affinity 不能单独证明 hidden space 中 Assistant 与 elite/helpful humans 的
确定距离；没有证明真实预训练/中训混合会保持同样转移率，也未识别唯一内部 circuit 或排除所有
surface/role confound。

**证据位置：** §2 Figure 2；§3.1 Figures 3–4；§3.2 Figures 5–7；§4 Figures 8–10；
§5 Figures 11–13；§6/§6.1；Appendices A–E（训练、grader、seed 与 replication details）。

## 4. ReactHuman — arXiv:2609.10895v1

- **原始来源：** [exact-v1 HTML](https://arxiv.org/html/2609.10895v1)
- **身份与日期：** Atom `published=2026-09-09T22:56:21Z`；公开批次为
  `2026-09-11T08:00:00+08:00`。当前未见撤回标记。
- **建议知识路由：** `MULTIMODAL-EMBODIED-VLA`；评价合同向
  `PLATFORM-EVALUATION-SYSTEM` handoff。

### 中心主张与机制

论文把 embodied physical reasoning 从“看视频答题”推进到“冻结同一观察、提交结构化动作、实际
执行后看后果”。模型收到约 0.6 s、最多三视角的观察窗，然后环境冻结；输出
`{intent, confidence, walking_cmd, hand keyframes}`，预训练 walking policy 与 scripted
upper-body controller 在同一 physics scene 中执行。simulation state 而非人工偏好拥有 impact
point、危险标签和动作 ground truth；因而能分离语义动作选择、是否安全、空间落点和轨迹趋近。

17 个 sudden-event families 覆盖 fall/slide/topple/articulated/ballistic/causal chain。14 个
appearance–physics adversarial assets 刻意让视觉类别与真实质量/材料相反，测试模型会不会根据
早期 motion 更新先验，而不是把“看起来像铁砧”直接当作重物。

### 实现与评价合同

- Genesis 240 Hz rigid-body simulation，seeded physical randomization；82-object library，超过
  1000 个 bit-for-bit reproducible scenes。主评测取 balanced 306 scenes（每 family 18），7 个
  MLLM，共 2138 有效 decisions，另有 4 次 API error。
- 模型：Claude Opus 4.8、GPT-5.5、Gemini 2.5 Flash、Kimi K2.6、Qwen3-VL-235B、
  Qwen3-VL-30B、Gemma-3-27B，统一 OpenRouter API、prompt/schema 与观察窗。API snapshot、
  precision/quantization、实际 serving hardware、latency 与 sampling 参数未披露；freeze protocol
  有意排除了 inference latency。
- 五项指标：SAA（动作标签）、Safety Validity（四类硬规则）、Physical Endpoint Distance、
  AIA（intent 与正确动作的目标一致性，当前用 keyword matching）、HDE（沿 keyframe 到 impact
  point 的最短距离与收敛量）。Safety 独立于 SAA 且绘图优先。

### 关键证据、收益与边界

- Dodge ground-truth scenes 中 35.9% decisions 违反 safety rule，各模型范围 23–66%；410 个
  violations 中 freeze-under-danger 162、应躲却不动/接触 128、catch dangerous object 120。
- 即使 action label 正确，hand endpoint 到真实 impact point 的 median 仍为 0.48 m，89% misses
  是 reach short；49% 时机器人距离超过 0.8 m、仅靠手臂不可达。这证明 multiple choice label
  会高估可执行能力。
- 12 个可变 speed families 的 826 decisions 中，最慢档 freeze 42%，其余约 21%；SAA 38.1%
  vs 较快档 47–54%。模型只在 27% scene groups 的四档速度中保持同一答案，说明动作未稳定利用
 连续速度证据。
- 40 个 adversarial scenes × 7 models = 280 decisions，无模型质疑 material/weight；foam
  ceiling panel 常被当真 slab 躲避，steel can 与 light can 的 catch rate 均 39%。这是该 asset
  set 上的强 failure signal，不证明所有模型绝不能从 motion 推断材料。
- 7-model majority vote SAA 62.1%，高于平均 54.0%，但不超过最佳单模型 63.7%，说明共享盲点
  不能靠简单 ensemble 消除。

### Trade-off、failure mode 与 fallback

- freeze-and-predict 消除不同模型 latency 与 observation timing confound，却把闭环 replanning、
  recovery 与真实 latency cost 排除；适合测 action commitment，不等于真实机器人闭环能力。
- simulator ground truth 可重复、免标注，但 rigid-body 不含 deformation/shattering；walking 与
  upper-body controller 的可实现域也会影响 endpoint error。
- fallback/下一步是 repeated observation-action closed loop、cloth/fluid/deformation、native VLA
  与 real-hardware validation；在此之前不能用该 benchmark 为实体部署签发 safety guarantee。

### 证明与未证明

**证明到的窄结论：** 在统一 open-loop simulator contract 下，当前 7 个 API snapshot 的动作
标签、物理可达性与安全会显著分离，外观先验、速度离散化和固定 action disposition 是可重复的
失败维度。

**没有证明：** 没有测 inference latency、closed-loop recovery、真实人机安全、软体/破碎物理，
也不能从 7 个版本快照推出能力不可能随 scale 改善；AIA 的 keyword scorer 不是语义真值。

**证据位置：** §3.1–3.4、Figures 1–2；§4 五指标定义；§5.1；§5.2、Table 1、Figures 3–5；
§6 limitations。

## 5. SearchAtlas — arXiv:2609.10901v1

- **原始来源：** [exact-v1 HTML](https://arxiv.org/html/2609.10901v1)
- **身份与日期：** Atom `published=2026-09-09T23:09:26Z`；公开批次为
  `2026-09-11T08:00:00+08:00`。当前未见撤回标记；arXiv comment 声明 accepted to
  Findings of EMNLP 2026，但本审阅只采用 v1 内容。
- **建议知识路由：** `PLATFORM-EVALUATION-SYSTEM` 为主 owner；`AGENT-RAG` 只 handoff
  evidence propagation 与 unsupported prior knowledge。

### 中心主张与机制

SearchAtlas 将 search trace 转为 evidence-propagation DAG，而非只对最终答案或 query 数量评分。
节点包含原问题、queries、answer 与 prior-knowledge sentinel；边描述 question constraint 如何进入
query、retrieved evidence 如何形成后续 query/answer，以及无已检索支持的事实如何从 parametric
knowledge 进入控制流。对 answer factual units 选择最小 supporting query set，避免把重复结果
重复算作证据。

构图分两段：deterministic preprocessing 提取 query、results、failure 与显式 constraint-use；
LLM attribution 针对每个 query 查看之前的 evidence，确定 incoming evidence-use edges 并裁剪冗余
parents。评价再按 question constraint type 分支：parallel questions 期待直接支持 answer；
sequential questions 期待集中 backbone。最终三类 signal 是 answer-path topology、constraint
grounding 与 unsupported prior-knowledge reliance。

### 实现与评价合同

- 5 个 agent：WebSailor v1 32B、MiroThinker v1 30B、Tongyi DeepResearch 30B MoE，以及相同
  Tongyi scaffold 下的 GPT-5、Qwen3-32B backbones。
- 3 个 English closed-answer benchmarks：BrowseComp sequential 150、WebWalker-Hard-English
  parallel 70、DeepSearchQA 两个 regime 各 25；5 agents 合计 1350 trajectories。
- parser 对 100 份 human-annotated DAG 的 macro edge F1 为 0.860；换 4 种 attribution models
  时 reconstruction/downstream conclusions 稳定。硬件、precision、token budget、search backend
  成本与 attribution 绝对开销未完整披露，因此不能做成本比较。
- correctness association 使用 agent 内 held-out evaluation、AUC/F1；与 GPT-5.2 full-trajectory
  judge、ordered-query judge 及 raw-log statistics classifier 比较。它是 outcome association，
  不是因果介入证明。

### 关键证据、收益与边界

- topology-only macro AUC 在四个 benchmark/regime 为 0.714–0.771；加入 grounding 后增益
  0.033–0.106；完整 score macro AUC 为 0.840–0.856。held-out threshold 的 F1：sequential
  0.705，parallel 0.780。
- 聚合 1350 trajectories：ordered-query judge accuracy/macro-F1/positive-F1 为
  0.677/0.608/0.444，full-trajectory GPT-5.2 judge 为 0.738/0.705/0.606，SearchAtlas 为
  0.776/0.772/0.740。这个比较支持 graph-localized signal 有附加信息，但没有给出等成本比较。
- 100 个 score–accuracy disagreement 人工审计显示两类边界：组织良好的错误可能过早绑定错误
  target；正确答案也可能来自 diffuse over-search 或 unsupported shortcut。因此结构 coherence
  不是 correctness guarantee。

### Trade-off、failure mode 与 fallback

- DAG 提供可解释、局部化的证据责任链，但构图本身依赖 LLM attribution，可能继承跨模型共有的
  系统性错误，并增加额外 inference cost。
- 只看可见 reasoning/tool/retrieval log；模型内部未外显的依赖不可恢复。sequential/parallel route
  选错会把样本送进错误指标族。
- fallback 是 parser uncertainty、human-in-the-loop sampling、candidate-level contradiction /
  constraint-satisfaction check；不能仅凭高 graph score 自动 release answer。

### 证明与未证明

**证明到的窄结论：** 在三类 English closed-answer deep-search benchmark 与五种 agent 配置中，
显式建模 evidence dependencies 比原始日志/query-list judge 更能关联最终正确性，并暴露 constraint
未落到 answer、support fragmentation 与未验证 prior knowledge。

**没有证明：** 不能证明 DAG score 导致答案正确、能替代事实验证，不能外推到 open-ended、
non-English、multimodal 或 hidden-reasoning agents，也未证明 attribution 成本适合在线 gate。

**证据位置：** §3.1–3.2；§4.1–4.4；§5.1；§5.3 Figure 4/Table 2；§5.4 Tables 2–4；
§5.5 Table 5/Figure 5；§6 Limitations；Appendix A.6、A.12–A.15。

## 6. IMLE-VLA — arXiv:2609.10915v1

- **原始来源：** [exact-v1 HTML](https://arxiv.org/html/2609.10915v1)
- **身份与日期：** Atom `published=2026-09-10T00:00:32Z`；公开批次为
  `2026-09-11T08:00:00+08:00`。当前未见撤回标记；arXiv comment 声明 IROS 2026 accepted。
- **建议知识路由：** `MULTIMODAL-EMBODIED-VLA`。

### 中心主张与机制

该工作把 VLA action-head 的设计分支从 iterative conditional flow matching 推进到 single-step
conditional generator。冻结 VLM backbone，把 observation/language embedding 与 Gaussian latent
一次映射为完整 action chunk。普通 `m=1` L2 regression 的最优解会忽略 noise 并输出 conditional
mean，可能落在多个有效动作 mode 之间；cIMLE 对每个 ground-truth action 采样 `m` 个候选，只让
最近候选承担梯度，使不同 latent 可覆盖不同 action mode，而 inference 仍只需一次 forward。

state/control ownership 的改变是：原 π0.5 action head 持有需 10 次 Euler integration 的临时
denoising state；新 head 把该状态压进一次 latent-conditioned mapping。省下的 inference 时间可以
提高 replan frequency，也可换成长 execution horizon；后一选择会重新引入 observation staleness，
因此 throughput 与 reactivity 不是同一收益。

### 实现与评价合同

- 以 pretrained π0.5 初始化并只 fine-tune action head；VLM backbone frozen。action chunk 为
  `C×D`，training 时 `m=2` 为默认；nearest-neighbor assignment 不跟踪梯度，只重算 winning
  candidate 做 backward。
- inference benchmark：单 NVIDIA L40S、standard two-view images、真实 task language 与每次
  call 的 instruction/proprioception tokenization；50 episodes、10 LIBERO-Long tasks。precision /
  quantization、batch 与模型 serving concurrency 未披露。
- LIBERO：40 tasks、4 suites、每 task 50 episodes；作者在 L40S 实测 π0.5、IMLE-VLA、
  OpenVLA-OFT，其他 baseline ratio 引自 H100 上的既有工作，故跨行速度不可当 iso-hardware
  排名。LIBERO-plus 覆盖 background/robot-init/language/layout 五档扰动。
- real robot：Franka Emika Panda + NVIDIA A6000、wrist/scene cameras，DROID training、4 tasks，
  每 task 20 episodes；π0.5 `H=8`/15 Hz，IMLE `H=12`/55 Hz。

### 关键证据、收益与边界

- 相同 backbone 下，canonical JAX π0.5 15 Hz、PyTorch compile 20 Hz、Triton 25 Hz、IMLE-VLA
  55 Hz，即相对 canonical 3.67×；这支持主要 latency 来自 10-step algorithmic loop，但没有拆出
  tokenizer/backbone/head 的逐项 profile。
- LIBERO `H=10`：π0.5 97.5%，IMLE-VLA 98.0%；IMLE `H=30` 为 97.1% 且论文定义的 action
  throughput 相对 π0.5 `H=10` 为 11×。注意 11× 同时乘入了更长 open-loop horizon，不是纯
  inference acceleration。
- cIMLE ablation：`m=1` 明显降分，`m=2` 与 `m=5` 接近，支持 nearest-candidate training
  而非普通 regression；论文未给出 mode coverage 的直接 distribution metric。
- real tasks 的 success（ours vs π0.5）分别 19/20 vs 15/20、18/20 vs 15/20、15/20 vs 12/20、
  16/20 vs 12/20；VLA-only wall-clock 降 3.9–6.6×，proprioceptive jerk 低 2.2–3.0×。
  每 task 20 trials 且未报告置信区间，结论保持案例范围。

### Trade-off、failure mode 与 fallback

- single-step head 去除 iterative compute，但 cIMLE 在训练时增加候选采样/assignment；`m=2` 是
  本文 operating point，不证明复杂分布都足够。
- 更大 `H` 提高 action throughput，却让更多动作在再次观察前 open-loop 执行；动态环境下应先
  用低 latency 提高闭环频率，而不是只放大 horizon。
- fallback/coexistence：极端 multimodality 或需要 iterative correction 的任务仍可保留 flow /
  diffusion head；可用 single-step proposal + verifier/correction，而非宣布 iterative head 过时。

### 证明与未证明

**证明到的窄结论：** 对 π0.5 backbone、LIBERO/DROID 与给定 L40S/A6000 setup，`m=2`
cIMLE single-step head 可在不降低观测到的成功率下显著降低 action-head latency，并改善这四个
real-robot task 的 motion/episode measurements。

**没有证明：** 没证明 cIMLE 精确恢复完整 conditional action distribution，没覆盖其他 VLA
backbones/robots、大规模开放环境、安全约束或长期 closed-loop stability；跨硬件 baseline 不能
支持统一速度排名。

**证据位置：** §III-A Eq.1；§III-B Eqs.2–6/Algorithm 1；§IV-A Table I；§IV-B Tables II–IV /
Figure 2；§IV-C Figures 3–4；§IV-D Figure 5/Table V。

## 7. Measuring the Value of World-Model Updates — arXiv:2609.10954v1

- **原始来源：** [exact-v1 HTML](https://arxiv.org/html/2609.10954v1)
- **身份与日期：** Atom `published=2026-09-10T01:22:57Z`；公开批次为
  `2026-09-11T08:00:00+08:00`。当前未见撤回标记；comment 为 workshop under review。
- **建议知识路由：** `MULTIMODAL-WORLD-MODELS` 的 update/evaluation contract，向
  `PLATFORM-EVALUATION-SYSTEM` handoff counterfactual release evidence。

### 中心主张与机制

论文提出的不是一个可部署 update trigger，而是衡量单次 world-model update 价值的反事实协议。
在预先登记的 decision point 保存完整 simulator/model/optimizer state，分叉成 update 与 hold 两条
continuation，使用 common random numbers 运行相同 episodes，记录
`ΔR = R_update - R_hold`。这样 prediction error / surprise 只作为可选触发 signal，真正 label
由下游 control return 的配对差给出。

控制依赖当前 DreamerV3-style RSSM 的 latent-space MPC + CEM；不使用旧 latent 上训练的
amortized actor，避免把 model update effect 与 actor mismatch 混合。update mechanism 固定为用
最近 `W` transitions 做 `N` 个 gradient steps，无 rehearsal；因此 fork ledger 评估的是“已收敛
world model 上的局部 no-rehearsal update”，不是 online adaptation 的普遍价值。

### 实现与评价合同

- DeepMind Control Suite / MuJoCo proprioceptive cartpole-swingup、walker-walk、cheetah-run；
  hopper-hop 只是 legacy-schedule negative control。每主 task 240 attempted forks，5 个独立
  pretrained checkpoints × 2 drift directions；每 branch 30 matched evaluation episodes。
- corrected design 为 20,000-step drift、每 250 control steps fork；gravity 或 friction drift 与
  action stochasticity 分开，但 corrected arms 实际只运行 `σ_a=0`，注册的 stochasticity axis
  没执行。
- 主 estimand 必须包含 update-induced collapse；另报告按“update branch < frozen reference 的
  30%”排除后的 693/720 non-collapsed forks。CI 按 checkpoint cluster bootstrap；只有 5 clusters，
  作者明确承认 percentile bootstrap under-coverage。
- 重要偏差：预注册 primary endpoint 未报告；threshold 从预注册 causal running quantile 改为
  leave-one-checkpoint-out fit；8 个 registered trigger families 只完成 4 个，另加 1 个未注册的
  return-deficit feature；无 multiplicity adjustment。上述偏差禁止把结果写成“预注册全面验证”。

### 关键证据、收益与边界

- all attempted forks：CartPole `-144.0`，checkpoint-bootstrap 95% CI `[-185.4,-116.1]`，
  converged return 约 650；Walker `-82.8 [-101.1,-61.7]`；Cheetah
  `-18.6 [-29.0,-6.6]`。
- non-collapsed：CartPole `-113.4 [-131.2,-90.1]`（58 helpful/170 harmful），Walker
  `-82.1 [-100.2,-60.9]`，Cheetah `-3.9 [-17.5,+13.0]`，说明 Cheetah 在安全收窄后未决。
- 独立 stream seeds 增加到每 task 30 cells 后，CartPole `-113.0`、Walker `-81.1`、Cheetah
  `-3.3` 且 CI 跨 0；它只排除单一 stream realization，不增加独立 task 数。
- CartPole 上 residual trigger 与相同 14,000 gradient-step 的 rate-matched random rule 总 utility
  分别 `+2198` 与 `-7128`，证明相同 intervention budget 下“选何时更新”可改变结果；但 Walker
  两 learned policies 仍为负，Cheetah 对 divergence exclusion 敏感，不能称跨 task trigger。
- 预注册的“共同 attractor/crossing 可跨 task 转移”机制被 Walker 结果直接 falsify；论文明确将
  后续 per-task crossing 解释降为 post hoc。

### Trade-off、failure mode 与 fallback

- paired fork 提供单次 update 的反事实 label，但需要可恢复 simulator state、大量双分支 episode
  与明确 scalar outcome；现实 physical/video world model 未必具备这三个条件。
- common random numbers 降低方差，却仍只比较一个固定 no-rehearsal mechanism；换 replay、reset、
  optimizer 或 actor coupling 后需重建 ledger。
- fallback 是 hold/no-update baseline、rate-matched random control、oracle ceiling 与按 task/drift /
  competence 重新校准；prediction error AUC 不能直接替代 policy utility。

### 证明与未证明

**证明到的窄结论：** fork ledger 能对一个固定 update intervention 生成因果上更接近的 paired
utility label；在三项模拟 control task 中，无条件执行该 no-rehearsal update 平均有害，且 trigger
ranking/utility 不跨 task 自动转移。

**没有证明：** 没有证明 world models 不应在线更新、所有 trigger 无效或该结果适用于 video /
physical deployment；未执行注册的 primary endpoint、stochasticity ramp 与一半 trigger families，
也没有给出 task population-level estimate。

**证据位置：** §3.1–3.3；§4.1 Tables 1–2/Figure 2；§4.2；§4.3 Figure 3；§4.4；§4.5 Table 3；
§5 `Scope and disclosures`；Appendix A.1–A.5，尤其 A.2 deviations。

## 8. Decoupling Readiness from Release — arXiv:2609.10964v1

- **原始来源：** [exact-v1 HTML](https://arxiv.org/html/2609.10964v1)
- **身份与日期：** Atom `published=2026-09-10T01:35:10Z`；公开批次为
  `2026-09-11T08:00:00+08:00`。HTML 中的 “withdrawn” 仅表示已提交 turn 不能被 workflow
  scheduler 撤回，不是论文撤回；当前未见 arXiv withdrawal notice。
- **建议知识路由：** `AGENT-WORKFLOW` 为 readiness/release ownership 主 owner；
  `INFER-SCHEDULING` handoff engine admission 与 committed-work accounting。

### 中心主张与机制

传统 agent runtime 把 dependency-ready 等同于立即 submit，导致 engine congestion 时大量
released-but-unfinished turns 进入 engine ownership；workflow scheduler 之后无法重新排序。论文把
readiness（eligible）与 release（commit）拆开，由 workflow-level scheduler 同时决定“谁先交给
engine”与“允许多少 estimated work 已提交但未完成”。

优先级来自 mean-CVaR objective 的 holding-cost rate：所有未完成 workflow 有 mean weight，age
超过在线估计的 α-quantile 后增加 tail weight；再除以当前 ready turn 的 token-equivalent work
estimate。另用 queue mean/p95/waiting requests 的最大 normalized violation 更新 congestion state，
映射成动态 committed-work budget。turn release 后其固定 work estimate 加入 `W(t)`，完成时删除；
超大 turn 在 engine 空闲时有 progress exception，等待超过 `H` 有 starvation override。

### 实现与评价合同

- 不修改 vLLM 内部 scheduler，只控制 submit 时机；vLLM 0.20.2。模型/硬件：Qwen3-8B/1×A100
  80GB、Qwen3-32B/2×A100、Llama-3.3-70B/4×A100。precision/quantization、engine batch 参数与
  serving SLO 未披露。
- 两组真实 mini-swe-agent trace：SWE-bench 100 workflows/1597 turns，平均 15.97 turns，平均
  prompt/completion 7160/97 tokens、tool gap 1.327 s；SWE-Gym 100/1624、16.24、8244/93、
  1.855 s。Poisson arrivals，5 个 rates；paired runs 重放相同 workflow、arrival、inference work
  与 tool delay，只有 release policy 不同。
- 主指标是 arrival-to-completion P95 workflow flow time。每个点只有固定 arrival seed=1 的一组
  paired run；没有 CI 或多 seed，因此 tail point estimate 的不确定性未被量化。
- 固定参数包括 α=0.95、β=κ=1、decode-to-prompt work coefficient γ=4、budget 30k–300k
  （初始 120k）、queue targets 1s mean/5s p95/2 waiting requests、starvation H=180s。

### 关键证据、收益与边界

- 六个 trace×model 的最低负载点，eager/proposed P95 ratio 为 0.99–1.00，说明该 setup 中
  light-load 没有可见 penalty。
- 高负载均降低绝对 P95；最大值出现在 SWE-bench + Llama-3.3-70B + 0.9 workflows/s：
  1986.3 s → 568.0 s，减少 71.4% / 3.50×。六种组合最大 speedup 为 2.06–3.50×。
- 同一 0.9 workflows/s 不代表不同模型/GPU 数的相同 normalized load，论文也明确禁止用这些点
  推出 speedup 随模型大小单调增长。
- 70B/0.9 ablation：在同一 adaptive budget 下 tail-aware ordering 相比 FIFO 降 P95
  59.51%/63.51%（两 traces）；在同一 ordering 下 adaptive vs fixed budget 再降
  10.68%/11.62%。因此主收益来自 ordering，budget adaptation 是较小但一致的增量。

### Trade-off、failure mode 与 fallback

- 延迟 release 保留 workflow-level optionality，但 work estimate 偏差、quantile lag、queue signal
  噪声或过小 budget 会造成 under-admission；H 与 idle-engine exception 只保证进展，不保证最优。
- release 后仍由 vLLM 掌握 batch/execute 状态，方法无法 preempt 或 reorder committed turn；这是
  清楚的 ownership boundary，而非替代 engine scheduler。
- fallback/coexistence：light load 可退化为 eager release；估计/telemetry 失效时 hold budget state
  并以 starvation/progress safeguards 前进。生产需要多 arrival seeds、更多 workflow 类型、质量 /
  throughput/resource-utilization guardrails 后才能确定默认参数。

### 证明与未证明

**证明到的窄结论：** 对两组 100-workflow 软件工程 trace、三种 A100 serving configuration 与
所测 arrival rates，readiness/release 解耦能保留低负载表现并明显降低高 contention 的 P95；消融
支持 tail-aware ordering 是主要贡献。

**没有证明：** 单 seed/单 P95 point 没有证明统计稳定性或更广 workload 的生产收益；未证明
mean latency、throughput、GPU efficiency、answer quality 或 fairness 不退化，也未与可 preempt 的
engine-level scheduler 联合比较。

**证据位置：** `Background and Motivation`/`Eager Release under Congestion`；§Problem
Formulation；§Method Eqs.7–16/Algorithm 1；§Experiments `Experimental Setup`、Figure 2；
`Ablation Studies` Figure 3。

## 9. Fengshui — arXiv:2609.10970v1

- **原始来源：** [exact-v1 HTML](https://arxiv.org/html/2609.10970v1)
- **身份与日期：** Atom `published=2026-09-10T01:43:52Z`；公开批次为
  `2026-09-11T08:00:00+08:00`。当前未见撤回标记。
- **建议知识路由：** `INFER-TENSORRT-LLM` 当前承担 execution-plan / compiler-kernel-hardware
  co-design；成本与 provisioning 仅作 handoff，不把模拟结果写成已部署硬件事实。

### 中心主张与机制

论文处理的矛盾是：按 operator 定制 compute/dataflow/memory/batch 可越过 homogeneous hardware
的局部瓶颈，但每模型 bespoke ASIC 会让 NRE 随设计数增长；固定 chiplet library 可摊薄 NRE，
却可能没有 future workload 所需的 PIM/switch/dataflow。Fengshui 因而把“选择可复用 chiplet pool”
与“用 pool 为各 workload 合成 BASIC execution pipeline”联立，而不是先固定硬件再做 mapping。

层级控制流为：PyTorch graph → per-operator Einsum → Layer 1 surrogate-assisted evolutionary
pool search → Layer 2 fusion-boundary/memory genome → Layer 3 iso-latency decomposition + modified
convex-hull trick 选择每 stage chiplet/mapping → Layer 4 place-and-route 验证。pipeline bottleneck
latency 是全局共享状态；固定候选 latency 后，各 stage 独立最小化 energy，从 `O(M^P)` 降为
`O(M·P·Q)`。pool 是跨 workload 的长期 artifact，per-workload mapping/fusion 是可重求的运行计划。

### 实现与评价合同

- 主体是 Timeloop v0.4 + Accelergy、CENT PIM、CACTI DRAM、ORION/DSENT/UCIe 与 cost model 的
  建模/搜索，不是制造并测量的 8-chiplet silicon。候选包含 RS/WS/OS compute、PIM、MoE switch，
  LPDDR5/DDR5/GDDR7/HBM3、2D/2.5D，technology 14nm、1GHz；PIM 使用论文给定 1Y-nm、BF16
  与 bandwidth/power 参数。
- Workloads：Llama-3.1-8B/70B、Qwen3-30B-A3B/235B-A22B 的 prefill/decode，batch 1/8，
  serving case 扩到 64；另有 MobileNetV3/RepLKNet。serving case 的 prefill input 1024、decode
  KV length 1024；chatbot TTFT/TPOT 2.5/0.15s，summarization 15/0.15s。
- 对照含 homogeneous accelerator、unconstrained heterogeneous design、random pool/mapping、
  复现在同一 model 内的 Gemini-/SCAR-style；另有实测 RTX PRO 6000 Blackwell 96GB BF16
  operator baseline，CUDA graph、L2-exceeding operand ring、NVML energy 与实测 PCIe transfer，
  但 chiplet headline 仍是 simulation/model composition。
- 评价为 energy、energy×cost、EDP、EDP×cost；没有 end-user model-quality 差异，因为同一
  forward graph/precision 被映射。生产软件 overhead、yield/thermal throttling、fabric congestion、
  chip fabrication variation 等未完整进入评价。

### 关键证据、收益与边界

- 2×2 factorial control：随机 mapping 比 co-designed mapping 的 EDP 差 8.9–9.3×；随机 pool
  差 1.7–2.9×，即使 pool 扩至 24 仍存在，支持两层联立优于单独优化。搜索得到 8-chiplet pool
  相对 homogeneous simulated accelerators 的 headline 降幅为 energy 48.5%、energy×cost 88.1%、
  EDP 93.0%、EDP×cost 97.8%，距 unconstrained heterogeneous optimum 4.1%。
- LLM serving case：在各自 SLO-feasible energy minima，Qwen3-30B-A3B/Llama-3.1-8B prefill
  per-token energy 降 12.5%/16.8%，energy×cost 降 10.5%/28.7%；Qwen decode 在相应 batch
  下 baseline 已能选到合适单 chiplet，因此 heterogeneity 收益很小，这是重要反例而非遗漏。
- leave-one-family-out：4/5 families 的 frozen-pool energy/energy×cost 距自有 optimum 0.7–18.3%；
  decode/MoE/vision 在缺 PIM/switch/spatial array 时会出现大 gap。只新增第 9 个 chiplet 后所有
  family 回到自有 optimum 的 14.3% 内，支持可增量演进但不证明任意未来 workload 可覆盖。
- simulation fidelity：1228 个 matched 64×64 OS GEMM 上 Timeloop vs ScaleSim 的 compute /
  DRAM median ratio 1.12×/0.97×；16 个 2-chiplet Llama workloads（length 512–4096）对 Gemini
  的 energy/latency log-space `r=0.97/0.92`。相关性验证 trend，不等于真实 silicon absolute error。
- 搜索开销：N=1–10 pool 每 objective 2.4–2.5 h，固定 pool 后每 application 0.67 s；约 185k
  Timeloop mapping characterization 是一次性前提。

### Trade-off、failure mode 与 fallback

- operator heterogeneity 降 energy/cost，但增加 chiplet inventory、mapping/compiler、interposer
  P&R、thermal 与验证复杂度；pool 过度拟合已有 workload 时，future dominant bottleneck 会放大
  gap。prefix-freeze + 增加 chiplet 是降低再设计范围的 fallback，不是零 NRE。
- per-operator non-uniform batching 可避免 attention 成为 pipeline bottleneck，却增加 state routing /
  buffering；decode 在某些 operating point 用单一 PIM 或 systolic chiplet已足够，homogeneous / phase-
  homogeneous 方案仍有共存区。
- thermal objective 权重过高会反噬 wirelength/energy；论文的 useful `λ∈[0.25,0.75]` 在其 model
  中降 peak 0.7–4.4K 并保持 wirelength/energy 低于 pre-pass，`λ=0.9` 已显著恶化 wirelength。

### 证明与未证明

**证明到的窄结论：** 在论文统一仿真与 cost contract 中，chiplet-pool selection、operator
mapping/fusion/memory/parallelism 必须共同优化；固定 8-chiplet pool 可在所测 LLM/CNN workload
上接近 unconstrained design，并可通过定点添加新 chiplet 修复已知 family gap。

**没有证明：** 没有 fabricated chiplet 或 end-to-end serving deployment，不能把模型中的能耗、
成本、temperature 与 yield 直接视为实测生产数据；未证明未来模型分布、软件 overhead、互连拥塞
与 supply-chain/NRE 假设保持不变，也未证明所有 decode 都从异构方案受益。

**证据位置：** §II-A–C Figures 2–5；§III-A–F Eqs.1–3/Figures 6–7；§IV Table II；
§V-A Figures 8–9/Tables III；§V-B Table IV；§V-C Figures 11–12；§V-D Table V；§V-E
Figure 13；§V-F Table VI。

## 批次审阅结论

- 9/9 Source Family 已按 exact-v1 完成深入审阅；没有仅凭摘要保留的结论。
- 9/9 当前未见官方撤回标记；`2609.10964` 正文的 “cannot be withdrawn” 是 turn ownership
  语义，不是论文状态。
- 无 exact-version primary material blocker。代码仓库/数据集未作为已复现 artifact 计入结论。
- 可交由 Daily/Books 比较的长期命题均已收窄到实际实验合同；尤其不得将 ExaServe 的
  non-streaming 线性扩展外推到 streaming，将 World-Model 更新实验外推成“永不更新”，或将
  Fengshui simulation 写成 silicon measurement。
