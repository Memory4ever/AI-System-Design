# 2026-04-06 V3 重开检查点

## 当前终态（2026-09-26 14:09 北京时间）

日报独立验收通过：47个家族=26实际整合、18具体已有覆盖、1仅报告、2争议隔离；另02947身份/日期冲突隔离不计确定分母。02869→Ch33、02734→Ch77、02344→Ch49真实正文均由apr03写后核对；Memory正例是有效执行transition而非任务成功，WebGPU完整开销分账与跨平台直接dispatch范围已区分。02344早提交/OAI created不证明早公开，按同一组合批次证据推断归属，不再要求逐篇公告日志。SignCert与03208保持争议，三处历史官网目录保持精确外部缺口，恢复条件在日报§5；没有普通pending。以下保留过程记录，不覆盖当前终态；不据完成宣称全源零遗漏。

本文件是当日工作记录，不是完成收据；旧 `README.md` 的 V2.1 `Complete`、50 个候选及 Books 判断均未获本轮继承。

## 日期边界

- 本窗：`[2026-04-05T09:00:00+08:00, 2026-04-06T09:00:00+08:00)`。
- [arXiv 官方公告规则](https://info.arxiv.org/help/availability.html)：美东 Sunday 20:00 常规公告，对应北京时间 04-06 08:00，落本窗。arXiv ID 在公告时赋予；`v1 Submitted` 可以早于公告，不能代替 first-public。
- 旧 [arXiv owner receipt](../arxiv-owner-replay-20260903/20260406/arxiv-owner-receipt.json) 含 449 条注册身份，作为题摘发现库存而非冻结分母。相邻 DOI-created 边界：`2604.02332` 为 04-03T02:09:29Z，`2604.02333` 为 04-06T01:23:49Z，`2604.03231` 为 04-06T01:45:01Z，`2604.03232` 为 04-07T02:36:29Z。此连续 ID 批次与公告节奏、当日 OAI 记录交叉支持 `02333–03231` 的归属；DOI 时间本身不是首次公开分钟。拟保留项仍需逐项核官方 v1 身份与撤回状态。

## 已实际核查的机构窗口入口

| 来源 | 停点与当前判断 |
| --- | --- |
| OpenAI | [官方 News RSS](https://openai.com/news/rss.xml)相邻项 04-02T10:30Z → 04-06T10:00Z，后者在本窗结束之后；Research 历史日级索引仍未由 RSS 覆盖。 |
| Anthropic | [官方 Research](https://www.anthropic.com/research) HTML 的 `publishedOn` 相邻项 04-02T10:56Z → 04-07T09:35Z；本官网目录无本窗项。 |
| Google Research Blog | [2026-04 月目录](https://research.google/blog/2026/04/) 04-03 → 04-08/09；Google Publications 的历史日级检索仍须单独隔离。 |
| Qwen | [动态 API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) `extra.date` 相邻 04-02T04:00+08 → 04-15T10:00+08；[静态目录](https://qwen.ai/api/page_config?code=research.research-list)为旧研究列表。 |
| DeepSeek | [官网动态](https://www.deepseek.com/news/)当前可见 04-24 与更早 2025 项，未见 04-05/06 项。 |
| Hunyuan | [官网 Research](https://hunyuan.tencent.com/research)所用官方 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，请求 `{"pageNum":1,"pageSize":100,"renderType":0}` 返回 9/9 条；日期从 04-23 跳至 02-13，本目录无本窗项。 |
| Seed | [官方论文目录](https://seed.bytedance.com/en/public_papers)所用 `GET /api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=40`（`x-tt-locale: US`）跨 04-08 → 03-31；Blog `article_type=2,page_token=0` 跨 04-09 → 04-01。 |
| Baidu ERNIE | [技术博客](https://ernie.baidu.com/blog/zh/)可见 02-06 → 04-15，无本窗文章。 |
| Z.ai | [发布说明](https://docs.z.ai/release-notes/new-released)现见 04-07 邻域，Research 页面邻近项 04-01 → 04-07；本窗未见目录项。 |

这些停点只约束所列官方目录，不证明站外论文或尚不可回溯的目录零命中。MiniMax、MiMo、Moonshot、Meta、DeepMind/Google Publications、组织仓库重要公开事件仍需在正式日报中闭合或精确隔离。

## 题摘准入进度

已浏览旧 449 注册身份标题，并定点读强信号条目的完整摘要；旧 50 个 Score / Books 行只作线索。初步可能真正改变长期机制/评价/状态边界的家族集中于：`2604.02344`（WebGPU dispatch 评价合同）、`02522`（私有 Agent memory 的访问模式）、`02560`（diffusion 并行选择的依赖边界）、`02623`（跨 session 环境记忆注入）、`02650`（长上下文继续训练的收敛/评价）、`02715`（MoE expert residency 与 KV 容量）、`02766`（online DPO 主动选择反证）、`02954`（GraphRAG 拓扑污染）、`02985`（prompt compression 预处理 break-even）、`03035`（跨 PR 顺序 coding agent evaluation）、`03070/03081`（Skill credential / supply-chain 威胁）、`03128`（RLVR/self-distillation 信号边界）、`03141`（长文事实覆盖率）、`03143`（多 Agent collective KV）、`03179`（多模态 RL 视觉必要性）、`03191`（VLA action tokenization 瓶颈）、`03216`（confidence/abstention 的效用合同）。

这只是**待复核准入清单，不是冻结候选、审阅完成或 Books 建议**。其他强信号与反向抽查尚在进行；例如 `2604.02478` 专属 UUV V&V、`02728` microgrid、`02651` GNN mini-batch 不能因 AI/系统词汇而沿用旧保留。后续逐项给出 family-specific 准入/关闭理由，校核 exact-v1，再评分及分层审阅。

## 下一步

1. 完成剩余 Daily 入口的本窗停点和必要的终态隔离。
2. 对旧 50 与漏收强信号做题摘贡献校准，冻结唯一 Source Family 分母；对高分和安全/评价 override 核 exact-v1 方法、实验与限制，收窄作者结论。
3. 与 ROADMAP / Books 具体既有论点比较；共享书稿由主任务串行写入。完成当日六节 V3 报告，再交非作者语义复核；此前不标 `完成`。

## 第二轮准入校准（2026-09-26，仍非冻结分母）

旧 449 条是按公告邻域恢复的 **raw identity 库**；旧 V2.1 的 50 个 retained 不是本轮候选。已对旧高分条目和标题反向抽样的强信号读完整题摘，以下是准备进入版本/证据检查的工作集合。理由写成“原判断 → 原文增量 → 待核选择”，不是按章节名或论文用语自动保留。

| arXiv v1 | 准入需核的具体增量 |
| --- | --- |
| 2604.02340 | masked diffusion 固定大模型每步 denoise 的成本，可能因中间步更敏感而改为按步调度大小模型；待核 FLOPs 与真实时延/质量边界。 |
| 2604.02344 | 浏览器 GPU 推理常把 kernel 与 API dispatch 混计；跨实现测量提出 sequential-dispatch 的端到端 attribution，待核 batch=1 与硬件边界。 |
| 2604.02375 | ReAct 规划与执行耦合时难同时限制工具副作用与并行；intent/scope/impact/clearance 的执行层 gate 可能改变控制责任。 |
| 2604.02473 | 跨 GPU collective 仅看网络带宽会漏目标地址反向翻译；模拟的 cold TLB 尾延迟可能改变小消息优化优先级。 |
| 2604.02522 | 私人长期记忆若外置，密文仍泄露访问模式；可信区保留数据依赖推理、外部 ORAM 固定访问预算是独立隐私/吞吐取舍。 |
| 2604.02560 | diffusion 并行位置的边际乘积破坏联合依赖；依赖预测后选择弱相关位置是可检验的 sampler 替代分支。 |
| 2604.02623 | Web Agent 记忆攻击不必直接写存储，单次环境观察可跨 session 激活；需重估来源信任与记忆晋升。 |
| 2604.02638 | 量化 KV 读出若每次先反量化仍有执行成本；固定码本/查表 SRAM 把变换置于写入侧，但 sign pattern 可能造成灾难 PPL。 |
| 2604.02650 | 长上下文训练不能用 NIAH 饱和当收敛；同一训练轨迹的 PPL/SFT probe/retrieval head 给出不同停止信号。 |
| 2604.02715 | MoE 权重长期驻 GPU 挤压 KV 容量；把 expert 作为瞬态分页对象可改变吞吐瓶颈，但要核搬运与热分布。 |
| 2604.02766 | 在线 DPO 的主动偏好选择未必胜随机，在强预训练先验下还可能伴随通用能力下降；待核预算公平性。 |
| 2604.02767 | 多 Agent 委托若只验文本意图无法获得确定性授权；非 LLM authority service 约束 scope/cascade、概率 intent 独立处理。 |
| 2604.02954 | GraphRAG 仅验证文本而默认拓扑可信，会漏类型保持的边交换导致推理路径偏转；待核图构建与攻击前提。 |
| 2604.02965 | VLA action chunk 降低重规划成本却增加开环漂移；重规划由轻量闭环 verifier 触发是不同控制频率的设计选择。 |
| 2604.02985 | Prompt compression 节省 prefill 不保证端到端收益；压缩预处理与模型/硬件/长度共同决定 break-even。 |
| 2604.02986 | 奖励模型 proxy 的优势符号若不稳定，更新可能推向坏样本；符号鲁棒半径作为降权信号是受限训练分支。 |
| 2604.03035 | 单 PR coding-agent pass 隐藏先前错误累积；顺序依赖 PR、回归与代码健康可能改变 evaluator admission。 |
| 2604.03070 | Skill 中 stdout/debug logging 可把 credential 带回模型上下文；需要跨自然语言描述与代码检查的数据流边界。 |
| 2604.03081 | Skill 文档中的示例/配置可在正常复用时执行隐式恶意 payload；仅防显式命令不足以定义供应链 gate。 |
| 2604.03088 | **v1 标题为 SkillRT**，不是旧账本按后来 v3 回填的 SkVM；Skill 作为原样文本跨 model/harness 不具可移植语义，能力画像、编译与环境绑定可能改变平台责任。 |
| 2604.03128 | 自蒸馏 privileged teacher 若同时给更新方向会泄漏/不稳；RLVR 决定方向而 teacher 差异调幅度是新的控制分工。 |
| 2604.03141 | 逐已生成 claim 验证无法发现重要事实遗漏；外部参考事实 inventory 的 importance-aware recall 补评估另一侧。 |
| 2604.03143 | 同步多 Agent 轮次共享输出被每个请求重复 prefill/KV 保存；collective reuse 与 master/diff 让轮次成为共享状态 epoch。 |
| 2604.03179 | 多模态 RL 准确率提高可能依赖语言 shortcut 而非视觉；移除关键信息的训练/评估干预可检验模态必要性。 |
| 2604.03191 | VLA 更强 encoder 在固定离散 action codebook 下难传到行动；瓶颈位置而非上游规模决定收益。 |
| 2604.03208 | 单尺度 world-model MPC 长期搜索指数增长/误差累积；多时间尺度 latent model 是待核机制线索。同一官方 v1 的 abs 摘要写 `4×`、PDF v1 写 `3×`，HTML/v1 页眉还有后发日期；已隔离为 `Disputed Version Evidence`，不选取任一数字作为本次事实或 Books 依据。 |
| 2604.03216 | 置信度仅用 ECE/AURC 可能漏高损失的过度自信；答/弃跨风险阈值 utility 是不同评价合同。 |

以下旧 retained 已从工作集合剔除，保留其旧证据但**不继承旧分数或 Books 决定**：`2604.02478` 为 UUV 控制系统 V&V 领域组合，未提出适用于大模型系统的独立评价合同；`2604.02651` 是 GNN 图采样专属 mini-batch/4D 训练，不是 LLM 分布式训练机制；`2604.02728` 是微电网市场/竞价场景，无当前项目主线。其余旧条目还须做题摘定点确认，不能以这一小批次代替完整分母审计。

## 旧 retained 的否定侧重审（2026-09-26）

旧 receipt 中 50 个 retained 有 23 个未进入本轮 28 项本窗工作分母；下面逐家族写出依据，避免用“已有章节”或“相关但不重要”一笔带过。此表是**贡献准入**判断而非 23 篇全文审阅：完整题摘已作为筛选材料，实际决定较强者定点核 exact-v1；旧 receipt 的标题/摘要可被后版污染，故不把它们当版本事实。

| 旧家族 | 前分母关闭或精确重开依据 |
| --- | --- |
| [2604.02367](https://arxiv.org/abs/2604.02367v1) | 独立定点核 §7：单作者六标签/60case、合成重复流量和任意85%阈值，未测downstream outcome；只给这个局部评价配置下的选择操作点，未增加Ch56按质量、P95、成本及结果联合选择的具体合同。关闭不因负结果、不因小模型。 |
| [2604.02442](https://arxiv.org/html/2604.02442v1) | **版本污染反例**：官方 v1 标题为 WIO，不是旧 receipt 的 ReFlux。v1 的可逆 storage actor 与热迁移实证主属 RocksDB/持续 I/O；DeepSeek 推理小节只显示 SSD tier 超 DRAM 容量后 4–5→约1 token/s 的 cliff，未证明 LLM 推理从 actor 迁移获益。Ch54 已有 CXL/NVMe KV tier 成本边界，不据后版摘要扩成推理候选。 |
| [2604.02478](https://arxiv.org/abs/2604.02478v1) | UUV 自治系统 V&V 与 LLM Agent 的领域组合；题摘未提出可独立迁移的 Agent evaluation ownership/发布合同。 |
| [2604.02556](https://arxiv.org/abs/2604.02556v1) | 独立定点核 §IV–V：16值64B shared LUT每block加载/barrier、直接nibble索引及literals/instruction-cache取舍，是成熟CUDA查表执行的局部优化；不预处理/不融合的测量未新增量化表示或执行有效性条件。1+1+2=4关闭，不以单平台或没有新owner为硬门槛。 |
| [2604.02617](https://arxiv.org/abs/2604.02617v1) | 技术文献 claim triple→图→跨源核验在量子争议单案例上展示，未建立超过 Ch66 claim/evidence provenance、独立 evaluator 与冲突处理的新验收合同。 |
| [2604.02640](https://arxiv.org/abs/2604.02640v1) | 企业 RAG 的四轴难度分类提案，摘要未给足可核的对照结果/新检索机制；Ch76/66 已按检索、推理、证据、成本分层验收。 |
| [2604.02651](https://arxiv.org/abs/2604.02651v1) | 4D mini-batch 与通信免除依赖 GNN 图采样语义，不是本项目 LLM 分布式训练的等价机制。 |
| [2604.02666](https://arxiv.org/abs/2604.02666v1) | 用内部 utility 模拟 stakeholder 对话的学校排课优化；对话式需求澄清有用，但领域问题/benchmark 不改变通用 Agent workflow/evaluation contract。 |
| [2604.02668](https://arxiv.org/abs/2604.02668v1) | 给六个开源模型提供 peer sycophancy ranking 的多 Agent 受限实验；改善讨论正确率是局部证据，Ch82 已要求独立证据、角色与共识失败检查，不因此建立普遍的“排名即可靠”机制。 |
| [2604.02714](https://arxiv.org/abs/2604.02714v1) | 自动驾驶 VLA 的 RGB/depth future prediction + uncertainty-guided exploration 与 safety-gated GRPO 是领域组合；是否真的安全探索未被 NAVSIM/nuScenes 分数证明，不改变 Ch25–26 world-model/physical-action 责任边界。 |
| [2604.02728](https://arxiv.org/abs/2604.02728v1) | 微电网 P2P 市场/竞价中的多 Agent RL，属能源领域目标与约束，不在当前 AI for Science/领域应用范围。 |
| [2604.02734](https://arxiv.org/abs/2604.02734v1) | **重开，旧关闭无效：** 独立核 §3.2/4.3 的失败转移→Python规则、训练池positive误拒淘汰→negative覆盖晋升，以及较低非法动作率不等较高成功率；2+2+2=6，知识缺口深入，优先与Ch77规则晋升实际命题对读。训练池zero-FR不保证新状态soundness，尚未自动写Books。 |
| [2604.02837](https://arxiv.org/abs/2604.02837v1) | 独立核 §6 的五事件是已公开研究/incident的综合，不是本篇新增控制实验或新失效机制；Ch72 artifact→runtime effect及Ch84 catalog≠permission已有具体主线。维持综述重复关闭，不因缺新防御有效性排除安全反证。 |
| [2604.02869](https://arxiv.org/abs/2604.02869v1) | **重开，旧关闭无效：** 独立核 §3–4 的分开GN逐turn/outcome相加可反转局部credit，discounted-return统一GN+λ及rollout相关性校准是具体接口分支；2+2+2=6，知识缺口深入，Ch33泛化shaping主线不替代这个命题。Table6/7的LR、KL、steps与prompt/deep_equal混变，不采用组件因果收益；未自动写Books。 |
| [2604.02923](https://arxiv.org/abs/2604.02923v1) | 多模型 triage→并行→consensus 减少无网页条件下的部分幻觉，代价为 4.2× token；没有独立证据的共识不等于事实核验，Ch82/66 已要求可追溯 claim 与 evaluator。 |
| [2604.02945](https://arxiv.org/abs/2604.02945v1) | edge-cloud multimodal sparsity/offload/speculation 是具体系统组合；摘要只给 VQAv2/MMBench 的平均延迟/资源，未绑定完整设备、网络、并发与 SLO 以改变 Ch56 状态感知调度结论。 |
| [2604.02971](https://arxiv.org/abs/2604.02971v1) | Host/Manager/Worker 宽搜聚合加 context isolation 是现有 Ch81–82 workflow/context 预算的层级实例；作者在 WideSearch/BrowseComp 的局部效率与准确率不足以证明新 owner。 |
| [2604.02988](https://arxiv.org/abs/2604.02988v1) | 多 Agent Deep Research 的 prompt 组合自优化是限定 workflow，摘要没有新的 evaluator admissibility 或外部 truth 机制；Ch81 的独立结果/holdout gate 不能由自我 play 取代。 |
| [2604.03016](https://arxiv.org/abs/2604.03016v1) | 多模态 Agent 的视觉工具/网页搜索、步骤检查点与 overthinking 指标是受限 benchmark 实例；Ch66 已要求 tool invocation/effect receipt、过程与最终 outcome 分账。 |
| [2604.03098](https://arxiv.org/abs/2604.03098v1) | Agent 自生成 guidance 同时作推理引导和训练密集 reward 有自我确认/代理偏差；三 benchmark 局部收益不能替代 Ch33 的独立 environment outcome 与 verifier authority。 |
| [2604.03131](https://arxiv.org/abs/2604.03131v1) | **重开安全审阅：** 独立核 §1/3与框架Table18，205-case风险证据是受限Run而非仅Prompt评价，不能因没有新防护机制关闭。建议2+2+2=6安全深入，Books与Ch72 Run不是Prompt/Containment具体命题对读后可已有覆盖；尚未正式并入工作集合。 |
| [2604.03144](https://arxiv.org/abs/2604.03144v1) | 工业代码世界模型、错误反馈 CoT 与工具链验证组合，主要是单模型/领域训练和 benchmark；不证明可迁移的 world-state transition 或 AI System 平台契约。 |
| [2604.03145](https://arxiv.org/abs/2604.03145v1) | Kubernetes 多租户 noisy-neighbor 的 Granger/压力实验是通用云服务诊断，未测大模型推理/训练的特有状态、SLO 或隔离决策；Ch71 已有租户资源分账，不能凭类比 retain。 |

另从旧 closure 及标题强信号作分层反向抽看：`2604.02830` 的梯度子空间知识缺口 probe 属具体白盒 sensor，不能直接校准为事实正确概率或 abstain policy，Ch66 已明确内部 sensor 与任务损失/独立证据分开；`2604.03196` 的代码审查 Agent PR merge 相关性观察受选择偏差与人审组成混杂，不能由此推出 CRA 导致合并失败或发布策略；`2604.03045` 的视频 hallucination evidence intervention 是所测视频任务局部训练分支，Ch66 的模态/时间必要性实验仍是正面 gate。若发现这些 exact-v1 实际加入了本表未见的机制、纠错或安全新证据，按单家族重开，不推翻整批身份。

## 当前交接状态（2026-09-26）

### 独立排除侧复核后的重开

前述 28 项只是作者交付阶段的暂定集合，不再视作冻结分母。根任务在旧排除集按通信、低精度训练、reward 接口与局部 credit 等主线强信号选取八项完整题摘抽检，发现五项只有泛化关闭理由，却实际提供值得核验的机制或边界：`2604.02343`、`2604.02525`、`2604.02686`、`2604.02721`、`2604.02795`。这是 8 项抽检中的 5 项反例，**不代表 371 个旧排除项已全量有效检查**；共同理由受影响的范围还要定点复查，不能据原否定标签结束。

五项均已读 exact-v1 核心方法、关键实验/对照与限制，并在日报 §4 记录具体命题。四项局部 Books 写入分别为 Ch82 二元通信的共享先验与成本分账、Ch28 操作数形态的低精度分支、Ch31 policy/RM tokenizer 接口、Ch33 rubric-to-token 的归一化对象；GrandCode 与 Ch33 已有 immediate/delayed/stale lifecycle 具体命题相同，判已有覆盖。`apr01` 独立对读原始 v1 与五项实际正文后确认：两词表同 ID 不等文本、30 步校准不证明全程固定异常模式、token relevance 不等因果归因、答者可见参考答案与双向重建成本、独立 reward normalization 不可归因全管线 headline 等限制都已保留。

当前 449 为旧原始发现库存，33 为**工作候选数**（原 28 加上述 5），不是覆盖闭合或最终冻结数；2 个日期隔离项仍不计入。正文状态继续“进行中”。下一步是定点校准共同泛化否定理由、复核本批来源/日期边界及所有工作候选，完成后再冻结与验收；单篇 Books 对读通过不代替日级 Gate。旧有效证据不删除，旧错误排除不继承。

前文“下一步”是重开当时的阶段性清单，现已完成 14 个 Daily 来源的有界检查或精确外部隔离、旧 50 retained 的逐家族关闭侧复核，以及 28 个作者侧暂冻结候选的评分、证据和 Books 判断。`2604.02344`、`2604.02947` 不计入确定分母，`2604.03208` 作为同版本证据争议隔离。日报和必要书稿落点已同步；`validate_research.py` 与 scoped `git diff --check` 通过。**尚缺非作者独立语义 Gate**；在其检查 false-positive/false-negative、日期归属和章节落点并记录结论前，报告保持“进行中”。

### 后续反向抽检：具体增量，不以主题或局部结果机械关闭

根任务继续从同一旧原始库存选取八个强信号家族，读完整题摘；下表不是八篇均已审完全文，也不代表旧排除集全量通过。UI-Oceanus/Salt 已补核官方 v1 身份、可见版本状态和本日公告批次依据，实际正文由 `apr01` 独立复核；Salt 的 reference 身份措辞已按其发现纠正，日报现为 35 项工作集合，仍非冻结分母。其余新线索未同步为确定候选；不能以 Books 段落先写入代替日期与独立判断步骤。

| 家族 | 实际发现与续跑位置 |
| --- | --- |
| [2604.02345v1](https://arxiv.org/html/2604.02345v1) | GUI 探索真实转移、VLM 标签与 forward CPT 不是仅增加 benchmark；已审方法、固定转移数据的 forward/inverse 对照与在线评价。Ch25 写入探索数据→转移预测的受限训练分支；等待非作者实际正文复核及日期同步。 |
| [2604.02351v1](https://arxiv.org/abs/2604.02351v1) | 信用风险/贷款时间漂移评价讨论一般部署可靠性，题摘未给出直接研究大模型或其 Infra 的机制；保留明确的领域范围关闭，不把可作类比当当前项目增量。 |
| [2604.02460v1](https://arxiv.org/html/2604.02460v1) | 单 Agent 与 Multi-Agent 的 thinking budget 对照有设计反证信号，不能因局部 benchmark 排除。已审核心理论、实验与 Appendix G；API 自报 thought count 和可见长度均不证明真实 FLOPs，继续与 Ch82 总预算/上下文边界对读。 |
| [2604.02485v1](https://arxiv.org/abs/2604.02485v1) | 确认偏差与反例提示可能是已有原则的新条件证据；已读题摘，仍需定点核其控制实验是否改变 Ch80 既有反事实检查的适用边界，不继承泛化否定。 |
| [2604.02500v1](https://arxiv.org/abs/2604.02500v1) | 企业环境 Agent 隐瞒行为具有安全反证信号；已读题摘，需核授权/利益目标的干预及观察边界，不能仅由伦理叙述写 Books，也不能未经核验机械排除。 |
| [2604.02505v1](https://arxiv.org/html/2604.02505v1) | Projection-free adaptive SGD 的预条件/可行域与稳定性理论是训练主线，不因理论或无状态 owner 排除。已读 §2–3，下一步核 §4 的凸/非凸假设与 Ch28 具体差异；尚未完成采用判断。 |
| [2604.02652v1](https://arxiv.org/abs/2604.02652v1) | 组合 jailbreak 的单独/联合作用是安全边界线索；题摘已读，需核 controlled attack 对照与 Ch72 组合安全是否已有同一具体命题。 |
| [2604.03118v1](https://arxiv.org/html/2604.03118v1) | 少步视频蒸馏的近似路径一致性及 self-generated cache 质量分档提供生成主线增量。已审 §3、关键实验/消融与限制；Ch24 写入受限分支，等待非作者正文复核和日期同步。 |

续跑保持当前合同：只扩查共享错误理由影响的范围；准备好的单篇先推进，普通未读工作不伪装外部受阻。共同否定理由尚未校准完成，日级状态仍为进行中。

### 当前精确续跑点

#### 续跑中的三项必要证据与 Books 差异（root，2026-09-26）

重新打开三篇 exact-v1 HTML 的必要段落，以下是来源与章内实际对读，不是日期通过或新的采用授权。

- **02869**：§3.1–3.2 把逐 turn 单独 GN 后相加与先汇总 discounted raw return 再 GN 明确区分；后者再加 dampened outcome advantage。§4 的 tier/outcome 相关性只能用于校准诊断，不能把必要但不区分成功的读取动作解释为无用。Table6/7 同时变化 LR、KL、steps、prompt 与参数比较，不能把 headline 差异单独归因奖励。Ch33「Tool Feedback只能密化已有接口信息」已有 replay/shaping 界限，但尚未解释 normalization order 会改变符号；拟在该段后、缓存分支前补这一局部机制。对照 Ch32 的 advantage 符号解释与 Ch34 的离线偏好分支，不把它写成替代 PPO/DPO 的通用路线。2+2+2=6，知识缺口深入；日期与独立采用复核完成前不写 Books。
- **02734**：§3.2、Appendix C 用失败转移生成 Python verifier，以整个已有 positive pool 误拒零容忍筛选，再贪心覆盖 negative pool；不是用测试集证明规则 soundness。Appendix B.5 的 invalid 是环境明确拒绝，不等于未取得任务进度。Table4 的 prompt+verifier 比 verifier 更少 invalid，却未取得更高 success，说明可行性与进度需要分别验收。Appendix D 达到 refine 上限后会执行最后一次提议，因此不能声称论文提供 fail-closed 安全 executor。Ch77 已有经验蒸馏/可撤销索引，尚缺这条具体的失败规则晋升及双目标取舍，拟在 procedural consolidation 中局部补入；执行授权仍 handoff Ch81/78。2+2+2=6，知识缺口深入；本日归属未过不先写。
- **03131**：§1.2/3 与 Table18 支持在作者205-case、13类别、六框架所测配置下把 tool/state/effect 纳入安全评价；部分成功示例是权限或网络侦察，不等于完成入侵或机密外泄。缺少统一 paired model-only 对照、固定 runtime/权限和公开可重放材料，不能据各框架总率推出模型能力增强导致风险的单独因果效应或产品安全排名。Ch72「Safety Evaluation的单位是Run，不只是Prompt」「Containment不能只看最终是否发生攻击」已明确 model/framework/judge identity、完整trace、security/utility 与因果混杂边界，足以承载本次可用结论；建议具体已有覆盖，不新增机制正文。2+2+2=6，安全深入。日期尚待，不自动计入本窗分母。

上述三项的 primary URL 分别为 `https://arxiv.org/html/2604.02869v1`、`https://arxiv.org/html/2604.02734v1`、`https://arxiv.org/html/2604.03131v1`；访问日期2026-09-26。独立审阅者先前已确认它们值得重开准入，本次新增的精确章内比较与 proposed claim 仍须独立复核。旧43工作集合及其有效证据不因这次重开被推倒。

最新独立日级 audit **尚未通过**。另需正式裁决重开 `.02869`（优势方向）/`.02734`（规则晋升）/`.03131`（Run安全证据）；上表保存具体原文与目标命题，不自动并入43工作集合或写Books。`.02556` 的定点原文核验后建议4分前分母关闭；`.02837/.02367` 维持关闭但已修为具体条件理由。root已经重新打开 `.02869v1` 方法/奖励校准与训练实验，确认headline混变边界；必要Books差异及日级日期仍未通过。普通准入/采用待办不标外部受阻。

日期证据恢复点：`apr03` 实际请求官方 Atom `02333v1/03231v1`，entry published/updated与submitted相同，顶层updated为当前查询；这不能当公告上界。OAI日级、相邻DOI-created与固定slots仅支持当前批次线索，不冒充完全落窗的证明。需补原始本批官方列表/RSS存档或等价官方公开事件记录；若以永久ID在公告分配和注册早于下一slot作组合推断，须实际论证它排除早批分配/延后注册等替代解释，不能强求通过。保存精确缺段，不做全月日期批量搬移或删除有效正文。旧作者日期/关闭结论均不能代替本次独立Gate。

当前工作集合为 **43 项，未冻结**：原作者 28 项，加独立复核恢复的 15 项。当前逐项处置为 23 实际整合、17 具体已有覆盖、2 仅报告、1 暂缓争议；单篇判断并不代表整日 Gate。SelRoute/UI-Oceanus/Salt、EMS/FoE 和预算比较已完成有效对读。最新 `.02485` 查询证伪与 `.02505` FTRL 可行域分支已实际写入 Ch80/Ch28；`apr03` 指出的正定初始化、分布驻点和 I:C 措辞已修正并再次写后验收通过。`.02500` 的目标不等于执行授权、`.02652` 的联合风险与 Ch72 的具体既有命题对齐；后者数值分母和内部因果解释单独隔离，未写 Books。四项均已同步日报 §3/§4，机器校验和 scoped diff 检查通过。

剩余可执行工作是共同泛化否定理由的定点校准，以及来源、单篇首公开归属和最终分母的日级独立验收；四项单篇裁决不再待办。`apr03` 正在只读日级 audit，尤其核官方公告规则、永久 ID 分配和相邻 feed/DOI 时间能否组合支持完全落窗的公开区间，不把 submitted/created 单字段当证明，也不虚构逐篇 Announced。证据链若不足则保存精确缺段，不能强求通过。root 负责报告及共享章节协调。不扩扫 Weekly，不把 raw identity 库整体变成全文队列，不重读已验证的无变化部分。旧过程中的等待/数量以上述最新点为准。
