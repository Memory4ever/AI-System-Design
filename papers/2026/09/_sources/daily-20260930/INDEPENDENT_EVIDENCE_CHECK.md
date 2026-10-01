# 2026-09-30 独立 Evidence / Books 判断复核

- 复核者：`sep30_evidence_check`，非 Report 作者；初始独立复核指定 12 个材料家族。未创建 Report、未 stage/commit/push；后续有限 Books 授权与作者身份转换见末节，不能对自己的写入做独立验收。
- 窗口：`2026-09-29T09:00:00+08:00` ～ `2026-09-30T09:00:00+08:00`；证据笔记完成后检查时间：`2026-09-30T14:41:44+08:00`。
- 已重读 AGENTS、Research/Report 合同、统一 Prompt、Sources 使用说明/每日/主题路由、ROADMAP 与本日 PROGRESS。运行前已有大量暂存修改；证据笔记初次交付后 root 授予有限 Books 写入，实际写后状态在后文另记，不能自验通过。
- 首先独立读完 12 项题摘并校准具体增量，再读取精确 v1 HTML 的方法、关键对照及限制；HTML 分批下载曾超时，必要部分已读取，五份续传恢复。没有以下载失败、已有主题或读文工作量缩池；没有声称附件全部读完、实现已核验、复现或生产可用。
- 下列“深入完成”仅针对明确写出的拟采用命题及关键反证。它不是整篇全部定理、附件或 artifact 的认证；Books 建议尚需作者落实和独立写后检查，不能据本笔记宣称 Report 已完成。

## 1. 日期、精确版本与准入校准

独立获取 [cs.CL 当前官方公告](https://arxiv.org/list/cs.CL/new?show=2000)，页头为 `Wednesday, 30 September 2026`、`New submissions (showing 145 of 145 entries)`；指定 12 个 ID 全部在该页出现。这是身份定点检查，不是把 145 个条目建立为逐项审阅队列。[官方 availability](https://info.arxiv.org/help/availability.html#announcement-schedule) 指明随公告公开，Tuesday 20:00 Eastern US 对应本批常规时刻 `2026-09-29T20:00:00-04:00`，即 `2026-09-30T08:00:00+08:00`。这是官方批次＋日程推定，不是实际秒级切换观测；不是由 submitted 字段推定。该日不在页面列出的 2026 holiday 中。

12 项当前 abs 与题摘/history 均已取得；只有 v1，未见页面上的撤回、删除、勘误或重要修订公告。没有遍历完整历史或全网来证明“绝无更早正文”。原始 UTC 提交字段如下，**均不是首次公开时刻**：

| 精确版本 | Submitted UTC 原值 | 当前批次判断 |
| --- | --- | --- |
| [2609.35808v1 MATE](https://arxiv.org/abs/2609.35808v1) | 2026-09-20 03:12:49 | 本窗首次 arXiv 公告；事件页无更早正文线索 |
| [2609.35817v1 LUDI](https://arxiv.org/abs/2609.35817v1) | 2026-09-21 13:25:07 | 本窗公告；作者链接的 LUDI 仓库当前空，仓库更新时间不证明更早论文正文 |
| [2609.35860v1 Detectability Gap](https://arxiv.org/abs/2609.35860v1) | 2026-09-25 17:12:24 | 本窗公告；事件页无更早正文线索 |
| [2609.36178v1 ProVer](https://arxiv.org/abs/2609.36178v1) | 2026-09-28 19:48:05 | 本窗公告；事件页无更早正文线索 |
| [2609.36452v1 RPD](https://arxiv.org/abs/2609.36452v1) | 2026-09-29 01:15:11 | 本窗公告；不能因提交刚早于窗起点否决公告归属 |
| [2609.36590v1 SEED](https://arxiv.org/abs/2609.36590v1) | 2026-09-29 03:06:13 | 本窗公告；SEED 仓库建立于9月7日但当前 size=0，不能用空仓库创建日期否决正文归属 |
| [2609.37044v1 ThinkOPD](https://arxiv.org/abs/2609.37044v1) | 2026-09-29 08:51:21 | 本窗公告；事件页无更早正文线索 |
| [2609.36903v1 MultiTalk](https://arxiv.org/abs/2609.36903v1) | 2026-09-29 07:25:29 | 本窗公告；数据 artifact 与首次研究正文事件分开 |
| [2609.37930v1 MGPO](https://arxiv.org/abs/2609.37930v1) | 2026-09-29 16:17:32 | 本窗公告；事件页无更早正文线索 |
| [2609.37891v1 SYNTH](https://arxiv.org/abs/2609.37891v1) | 2026-09-29 15:58:02 | **旧项目的本窗新增完整研究/对照证据事件，不是 SYNTH 首公开**，见下 |
| [2609.37533v1 E-MoE](https://arxiv.org/abs/2609.37533v1) | 2026-09-29 13:18:50 | 本窗公告；事件页无更早正文线索 |
| [2609.37371v1 adaptation compiler](https://arxiv.org/abs/2609.37371v1) | 2026-09-29 12:27:51 | 本窗公告；作者仓库 created_at=2026-09-29T12:04:47Z 也落窗，但不把创建等同公开正文时刻 |

### SYNTH 的实际旧 first-public 与本窗 delta

从论文链接的 [HF 作者 card](https://huggingface.co/datasets/PleIAs/SYNTH/blob/main/README.md) 定点进入 [作者首次技术正文](https://pleias.ai/blog/blogsynth-the-new-data-frontier)，其明示 `November 10, 2025`，已公开 Wikipedia seed、backreasoning、约束语法、辅助小模型生成、单阶段训练和 Monad/Baguettotron 结果。该页直接链接的 [Synth Beta 作者正文](https://pleias.ai/blog/blogsynth-beta-engineering-knowledge-for-ai) 明示 `April 29, 2026`，已经公开三个 dense tiers＋MoE、seed 外 abstention、epistemic markers 与 10–140× token 口径。旧机制与这些 headline 不可重新计为本日发现或重评分。

本窗可继续审的是 v1 §4.2 的 **同600M架构/tokenizer/训练预算的 data ablation、trace removal 对照**及 §5.1 的 **seed 内/外事实覆盖反证和明确评价协议**。这些超出两篇旧作者正文披露的对照，足以构成当前完整报告的实质新证据事件；准入仅针对这部分，不用“首次 arXiv”包装旧 release。没有恢复2025年或4月 Daily，也未扩扫作者历史目录。

### 准入和评分建议

全部 12 项均存在具体可核增量，未发现仅凭 owner 映射或宣传数字准入的项；SYNTH 必须缩到上文新证据事件，而非删去已经读到的支持/反证。分数针对下列命题，不针对成熟原则或可联想到的章节。低于7分而深入的原因列在各项内，不能反向将其升分来配合 Books。

| 材料 | 约束 → 实际增量 → 重考虑的选择 | D+R+Durability | 本轮 |
| --- | --- | --- | --- |
| MATE | 成功/relevant旧轨迹仍会诱发invalid action → 冻结规则的检索后动作规范化及因子对照 → 不把memory compression与接口兼容混作同一收益 | 3+1+2=6 | 深入完成；设计反证 |
| LUDI | uniform reverse ELBO强平滑且token corruption身份不明 → 清洁目标loss＋per-token time → 区分UDLM目标/条件身份与few-step并行度 | 2+2+2=6 | 深入完成；Ch24具体机制缺口 |
| Detectability Gap | aggregate agreement detector掩盖高一致错误 → 划分/检测耦合审计与冻结regime换signal → 不用循环定义证明异质性 | 3+1+2=6 | 深入完成；评价设计纠错 |
| ProVer | 终局advantage均匀广播无法局部归因 → judge只提segment，恢复两端状态并续跑估credit → 分离选址与数值credit authority | 2+2+2=6 | 深入完成；Ch33具体机制缺口 |
| RPD | 同pass高confidence不能保证joint commitment → 层内稳定性＋未解决上游熵budget → 从单点confidence转向带依赖的commit policy | 2+1+2=5 | 深入完成；Ch24具体机制差异 |
| SEED | cheap early exit丢深层信息，MTP重复full forward → verification缓存深表征，末两层读取raw embedding起草 → 自推测的cost/quality边界有第三分支 | 2+2+2=6 | 深入完成；Ch48具体机制缺口 |
| ThinkOPD | student-prefix on-policy不保证共享trace兼容 → group reward gain＋TRD路由response权重 → teacher优势与可转移监督分开 | 2+1+2=5 | 深入完成；Ch29具体机制差异 |
| MultiTalk | 短双人评价无法覆盖长多方双语 → 长多方real-recording评价＋固定架构data规模/多样性对照 → 不以dyadic成功外推多人长期能力 | 2+2+2=6 | 标准完成 |
| MGPO | 新memory state效用包含继承成分 → 相邻rewrite对同future targets的增量，potential/control-variate关系 → 不把总效用当本次write credit | 2+2+3=7 | 深入完成 |
| SYNTH新证据 | 旧synthetic efficiency headline不能归因 → 同架构data/trace ablation＋seed外反证 → 区分数据形状、知识覆盖与总成本 | 2+1+2=5（仅新证据；旧机制不重评） | 标准完成 |
| E-MoE | factorized parallel reverse限制joint样本 → 离散route latent＋clean/noisy router匹配 → correlated生成不必另置连续VAE | 2+1+2=5 | 深入完成；Ch24机制缺口；不采用全文定理认证 |
| adaptation compiler | 固定LoRA program不适应episode且穷举成本高 → 学预测多维adaptation geometry再择program → amortization与未知family/default风险联评 | 2+1+2=5 | 深入完成；现有Ch30不含该离线择程序机制 |

## 2. 逐项证据与 Books 建议

### [MATE exact-v1](https://arxiv.org/html/2609.35808v1)

读取 §3.1–3.4、§4.1–4.4.4、Tables1–3、§5。机制为固定retrieval后过滤旧control context、抽condition/action/effect、仅对exact matched支持项应用冻结action map，再按供应的benchmark级profile渲染与2048-token预算序列化；未匹配动作保持原文，不推断未知语义，profile不是learned router。ALFWorld134任务/252旧成功轨迹、固定BGE-M3/k10/manifests，Qwen2.5-14B/72B温度0/seed0/30步；论文使用paired McNemar与分family Holm，aggregate-only baseline仅描述。

支持：legacy/current action schema失配可以让成功记忆负迁移。19/877行规范化使14B raw full的20.1%变82.1%，未改变全文长度到紧凑数量；MATE为81.3%，不是比uncapped normalized full更高。去normalization落至51.5%，预算去掉准确率不变但tokens增至7861；主支持是接口兼容而非压短本身。与source-matched动作序列79.1/91.8差异不显著（pH=.70/.73），不能宣称transition字段独立提高准确率。14B比无检索提升未过调整后的显著门槛（pH=.065）。fresh memory、ScienceWorld和TravelPlanner保留full trajectory有竞争力甚至优于MATE；不是通用替代。

Books：建议窄整合到 `AGENT-MEMORY` / [Ch77](../../../../../books/part-07-agent/77-memory.md) 的“写入时保留lossless source，读取时再构造derived memory”之后。现有约1399–1410行已实际讲query-time构造/不可逆压缩/回读，却未讲**历史动作schema规范化与长度、结构字段的因子分离**。raw source保留，展示可含normalized view；verified map不认证precondition当前成立。代价是映射治理与漏匹配，规划/新鲜轨迹仍保留full/context fallback。

### [LUDI exact-v1](https://arxiv.org/html/2609.35817v1)

读取 §3.1–3.2、§4.1–4.2、Tables1–3、局限和实际效率说明。LU去掉uniform smoothing、保留压低错误token与抬高清洁token的两项；per-token Beta time以均值保持全局corruption marginal，时间提示经AdaLN进入模型，不能称真实corruption oracle。AR→block UDLM使用context-causal mask/label shifting/complementary noise/auxiliary AR loss；7B初始化Qwen2.5-7B-Instruct，Dolci约2M samples、2500steps、batch256、block32。小scale170M/1B同配置loss比较支持目标差异，7B性能也受AR适配策略影响，不能把全部收益归LU一项。

必须限：3 token/step为理论并行度，§4.2称实际小batch加速仅1.30–1.92×；4.39×/3.45×为loss算子时间/显存比较，不是整训练或serving。未从零预训练大UDLM；模型错误与随机corruption不同，现有工作没证明普遍self-correction。

Books：`MULTIMODAL-GENERATIVE-PARADIGMS` / [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 的objective/commit分支可增加uniform-state diffusion的强平滑＋condition-target身份机制。现有263–298行谈objective/commit、masked/AR桥，965附近区分跨denoising-step稳定性，不含该loss及per-token time。数学采用只需干净目标与提示身份，不引用本轮未核完的渐近证明为普遍定理；保留masked/AR路线与高batch实际成本边界。

### [Detectability Gap exact-v1](https://arxiv.org/html/2609.35860v1)

读取 §2–7，包括定义、circularity、固定regime换signal、single-seed trajectory实验。四模型（LLaDA8B、Dream7B、Qwen2.5-7B、Llama3.1-8B），TriviaQA/HotpotQA/PopQA、K3随机seed；gold alias标签在diffusion与AR分别用token/substring规则，不能把标签等同开放事实真实性。Ghost/Flickering是operational partition，不是两类latent机制。

raw AUC gap .35–.46与regime定义极强相关，作者明确不把它当独立异质性证据。冻结regime后whole-response lexical/semantic dispersion的12setting positive gap由2000 prompt bootstrap支持；不是完全统计独立，因为仍共享生成响应。更强的single-seed diffusion feature/out-of-fold detector在LLaDA三dataset显著；Dream同向但仅PopQA显著。Ghost AUC .60–.79，**不是不可检测**。模型间matched prompts可换regime，不是question固有属性或AR/diffusion普遍排序。

Books：`PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 2094附近已有“低熵/高共识可稳定地错”、421–470有slice和隐藏regime；它们不包含**定义slice的统计量与被评估sensor耦合会自造gap**。建议只补该循环评价防护及冻结partition→换计算→single-seed的证据阶梯，不追加“Ghost无法检测”或部署保证。

### [ProVer exact-v1](https://arxiv.org/html/2609.36178v1)

读取 §3.1–3.5 Eq2–4、§4、§5 Tables1–3。judge比较mixed-success group内成功/失败轨迹，只提最多四turn的非终局segment；恢复pre/post含history与environment状态，用生成该group的固定current policy各采K8续跑，取terminal success均值差，只将正估计加到segment训练token。续跑不进入训练batch。段advantage的无偏解释条件含**deterministic segment execution、无中间reward、gamma1、可恢复状态与固定policy**；positive-only筛选和最终clipped objective不能继承无偏估计为“训练无偏/因果token attribution”。

Qwen3.5-2B/4B、100updates、G8、16groups；ALFWorld/WebShop/SearchQA。Budget-Matched GRPO、SPO-chain/tree和同judge的CriticSearch支持不是多采样或judge直接标签唯一解释。ProVer不是所有setting最优；4B WebShop略低CriticSearch。Qwen4B policy generated token增2.4/11.6/16.8%，step time比GRPO3.39→3.73、.82→2.00、1.39→2.25分钟：不能把“fine-grained方法中更快”写成比普通GRPO训练降本。局部Qwen9B judge在WebShop低于GRPO，judge选择仍task-dependent。

Books：`TRAIN-GRPO` / [Ch33](../../../../../books/part-04-training-system/33-grpo.md) 572“语义Segment credit”与797“derived skill utility”已有分段、proxy与reward authority，但没有**judge选址、可恢复两端current-policy续跑、正段bonus不将续跑当训练样本**的执行机制。建议补条件性outcome-based verification分支，fallback终局GRPO/既有critic，不声称不可回滚真实环境可直接采用。

### [RPD exact-v1](https://arxiv.org/html/2609.36452v1)

读取 §2、§3 Eq4–7、§4.1–4.5 Tables1–2。同一个forward中final layers的token persistence＋confidence drop过滤候选；left-to-right选集合时，累计其前方仍masked（含非候选/已拒绝）的entropy，已同批选中的前方位置不计入；high-confidence也受entropy budget，空集合回退首W masked内最高confidence，避免停止。RPD-block只在32token block做稳定候选，不含全canvas累积熵。

LLaDA8B/Dream7B、GSM8K/MATH500/HumanEval/MBPP、共同prompt/evaluator、输出上限256、A6000单卡batch1/sync，TPS包含decoding-loop开销但不代表服务SLO。**Table1“最高吞吐”为variants择一整体口径，不是full RPD每项最高。** full RPD在Dream MBPP/GSM8K等比Fast-dLLM慢；full更偏高质量端，block偏吞吐。LoPA低NFE却较慢，保留NFE≠latency反证；CE/no-block与PP-only/CD消融支持依赖顺序与稳定性作用，而非joint correctness theorem。

Books：`MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 965–975已有**跨denoising steps**early convergence和pairwise compatibility，不同于**同pass跨final layers稳定＋尚未解决上游熵**。可窄补这一commit分支，声明语义上游不等严格因果graph；预算/阈值失准时回退fixed blocks/conservative sampler。不复制到Ch48，RPD不是AR speculative exact verification。

### [SEED exact-v1](https://arxiv.org/html/2609.36590v1)

读取 §4.1–4.3 Eq3–8、§5.1–5.4 Table1与split/block/loss ablations。将大多数层视为encoder、最后两层为decoder；full verification产生下一轮需要的deep KV，draft阶段raw token embedding直接进薄decoder读取已验证前缀cache，无新增独立cross-attention模块。训练同时AR CE与block-causal speculative objective（block10、lambda1），不是training-free layer skip。重新训练后的target是verification authority，不能声称joint训练保持原checkpoint分布或比原AR同distribution而更高质量。

Qwen3-1.7B/4B-Base按每个任务分开SFT，greedy、A6000 48GB单卡，GSM8K/KodCode/ScienceQA/CNN-DM；2.6/2.7×是该task-specific fine-tuning协议下平均throughput，非生产goodput/所有模型。更大decoder提高draft质量同时降低吞吐，lambda质量/acceptance trade-off保留；“planning ahead”来自probe/CKA解释，不是已证明的独立因果归因。作者代码链接当前空，论文机制可采用但不能称实现复现。

Books：`INFER-SPECULATIVE-DECODING` / [Ch48](../../../../../books/part-05-inference-system/48-speculative-decoding.md) 460–500已有hidden-feature EAGLE、MTP和latent probe，却没有**full verifier refresh deep cache、薄last-layer raw-embedding draft及训练支持**。建议第三条件分支和cache/accepted-prefix回退边界；保留独立drafter与不可重训target的旧路线。

### [ThinkOPD exact-v1](https://arxiv.org/html/2609.37044v1)

读取 §3.1–3.5 Eq3–8、§4.1–4.2 Tables2–5与efficiency/interventions。student产生fresh sibling responses，固定teacher在student-visited prefixes＋共享离线think trace上重新计算dense分布；TRD累积有限window discounted sparse forward KL并response汇总，只是trace-response compatibility proxy。response-level reward gain与TRD先group z-score再sigmoid/exponential组合及group normalization；权重stop-gradient，dense token KL不变。

matched Uniform control共享bank、teacher、student rollouts、训练预算/selection；primary Qwen1.7B math三独立run，其他pair/task/interventions主要point estimates。32GPU、BF16 full-parameter、100steps/batch64；完整GPU型号等未在所读主文披露。TRD reverse、无reward、替代rawKL/length/support代理控制支持联合路由的局部作用，不证明TRD识别真实reasoning route或低KL就是正确。异步队列single-version groups最多滞后一个update；不能写strict零staleness。recurring time1.31 vs OPD1.0，不是全训练免费；offline trace生成与bank成本不能隐去。

Books：`TRAIN-SFT` / [Ch29](../../../../../books/part-04-training-system/29-sft.md) 现有teacher兼容与student-state匹配并未覆盖**同一prompt共享privileged trace对兄弟response差异兼容＋group归一response路由**。可窄整合，词汇区分teacher优势、路由proxy、下游outcome；teacher/trace/support或任务变化需再校准，fallback uniform/plain OPD。runtime异步工程不另占owner。

### [MultiTalk exact-v1](https://arxiv.org/html/2609.36903v1)

读取 §2.1–2.3、§3.1–3.3、Tables2–3及size-matched额外分析。57.6k小时数据含54.4k PT/3.2k FT、synthetic scripts/TTS/emotion/voice独立采样与同speaker nonoverlap、crossspeaker overlap；不是57.6k真实录音。训练保留Moshi双流架构，所有非target speakers混到user channel，没有新的per-speaker runtime state architecture。real recordings构造104evaluation samples、平均32.6min；persona由离线LLM生成，judges content score与参与span系数不直接测turn timing。

规模/多样性控制：FT fraction固定上一stage单调改善，size-matched800小时三speaker-only/short-only弱于random，支持所测data composition；更长/更多speaker仍明显差。模型13.15远低human68.74，MiniCPM multi-party IQ9.00仍高于8.56。20samples×5models的human/judge相关支持迭代评价可用性，不是所有slice judge无偏。另有response-onset/stop/continuation/ignore测量，不能将offline final score当实时延迟保证。

Books建议：**仅报告**，不增加新architecture owner。现有 `MULTIMODAL-REPRESENTATION` / [Ch23 §Full-duplex输入](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 已实际分离incoming stream、fusion、interrupt/commit；`PLATFORM-EVALUATION-SYSTEM` / [Ch66 §Duplex Agent Evaluation](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 3433–3451已经要求timing/content/turn与端到端trajectory分账。这里的实验性长多方双语data/benchmark是有价值新证据，但不改变上述长期分工；不能为新数据体量强造架构机制。准入仍保留，不以已有覆盖删候选。

### [MGPO exact-v1](https://arxiv.org/html/2609.37930v1)

读取 §2.1–2.4 Eq4–13、§3.1–3.4、Tables1–2、AppendixA.2/A.4的potential/gradient边界、F sparse training targets、G scope。固定reader/target，比较同target下相邻memory状态，MG为当前到未来targets增量和；G再累积未来rewrites。Φ来自pre-rewrite memory、在当前action采样前确定，telescoping使expected score-function gradient等价factual objective。**这不自动证明EMA scale、length-normalized token clipping/KL后的实际优化等价，亦不是coalitional credit或方差必降定理。**多个rewrite协同产生的新效用在实现可见时记给当前rewrite，后续return才影响早期动作，非逐rewrite完整因果分摊。

memory writer Qwen3-8B、frozen reader14B、chunk1024/memory budget256；SciREX structured IE的additive micro-F1 surrogate（held-out rho=.988），另测AIPAN privacy-policy转移和six readers。它是通用bounded-memory机制在document IE的验证，不是AI for Science应用研究准入。single MC reader估F，有sampling noise；79%缩短仅in-domain相对base202→43tokens，OOD241→168不是同样79%。Table1原learned-readers与统一14B-readers分别看，不能直接归所有跨family差为MGPO机制。Full/Factual/Myopic/Terminal对照支持减去继承效用和future horizon作用；24.9%方差降有CI但只under fixed untrained policy。full matrix成本随目标/trajectory长增长，训练仅对带attributed gold的chunks评分减call，推理不做counterfactual matrix；不能声称长程credit免费。

Books：`AGENT-MEMORY` / Ch77 142–154“content-level credit”已有span masking/proxy，1597–1605已有delayed future reward；都没有**adjacent rewrite marginal/inherited utility、固定reader的跨future-target potential及其非coalitional边界**。建议深入窄整合为learned-memory信用分支，与MATE检索后兼容不是同机制；必须保留成本、surrogate、部署事实authority和静态规则fallback。

### [SYNTH exact-v1 新增证据](https://arxiv.org/html/2609.37891v1)

读取 §3–5、§7、Tables8–9对应解释及seed内/外设置；先按上文旧正文纠正事件。新600M data ablation同架构/tokenizer预算；web分支额外SmolTalk+MMLU格式SFT约.2%compute，synthetic分支训练目标原含instruction/reasoning，不能称优化过程每个因素全匹配。去trace保持queries/answers与tokens/steps/unique samples/seed，MCQ基本不变、open-ended下降且ConflictQA改善，不能声称trace对全部能力通用增益。

500seed entities事实评价是知识保真/记忆定向测量，不是未知知识泛化；600held-out entities上MoE拒答67%而非seed内20%，attempted precision82→62%，web baseline已有更多这些实体。训练158B等token不能同4T/36T基线直接归因架构或普遍算力优势；generator/teacher/API/多轮试验总成本要另记。有限seed支持knowledge ceiling、English-seed文化偏差与大模型/代码/Agent能力未验证；seed grounded并不保证每条synthetic真。

Books建议：**仅报告本窗新受控证据**。`TRAIN-DATA` / [Ch27 synthetic分支](../../../../../books/part-04-training-system/27-data.md) 306–311已有具体联合prompt/generator/source/mixture与格式≠效用、token≠unique/生成成本；这里对受控形状与seed覆盖的新增实验证据不需要重写已公开旧pipeline，也不足以推普遍单阶段替代pre/mid/post training。本窗保留exact-v1反证；旧release不重计。

### [E-MoE exact-v1](https://arxiv.org/html/2609.37533v1)

读取 §3.1–3.3 Eq5–11、Table1、§5.1–5.3 Tables2–4与AppendixB.3 routed实现。reverse为给定route条件下factorized分布的mixture；latent为per-token/per-layer expert route，并非“每sequence所有位置同一个expert”。训练shared router的clean posterior与noisy prior、KL匹配、straight-through Gumbel/top2但forward active1；需要两forward，inference只noisy prior单forward。原文p/q prior/posterior符号在若干位置互换，本轮采用clean/noisy语义，不复制不一致符号或声称整定理已验证。

synthetic2D20k、binarizedMNIST、LM1B小DiT/length128/1Msteps/batch512/65Btokens。same active参数不等same total存储、训练FLOPs或墙钟成本；MNIST总param2.49M vs MDLM2.07M，text有8experts。LM1B few-NFE genPPL/MAUVE在近matched unigram entropy改善，NFE高时优势缩小甚至落后SEDD/VADD，AR128step PPL67.97明显更低；不是复杂reasoning大LLM生产加速证据。不存在“所有MoE routing自发消除factorization”的结论，clean/noisy训练支持不能省略。

Books：主owner `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24，非MODEL-MOE（后者只供应router组件）。现有965–975 pairwise compatibility为推理时近似校正，不含**训练route latent→mixture of factorized reverse→noisy prior sampling**。建议补correlated reverse参数化条件分支，明确active/total/two-pass成本和低NFE边界；可继续factorized或block/AR路线，不输出未核的普遍posterior-collapse消除/吞吐保证。

### [Adaptation compilation exact-v1](https://arxiv.org/html/2609.37371v1)

读取 §3–11、400/100/100 latent-spec split、三test seeds、四budget近匹配LoRA programs（early-depth/middle-depth/late-depth层区域的rank16、full-stack全层rank4 LoRA），预测acquisition/transfer/boundedness/preservation多维geometry，utility可变不重训predictor。early/mid/late不是训练时间阶段，full-stack不是full-rank或末四层。不是生成任意optimizer程序或推理期动态rank，不是hardware compiler；prior adaptations穷举成本前移而非消失。

Llama3.1-8B held-out balanced utility .607 vs objective-fixed .600、oracle .618，paired gain .0072 CI[.0011,.0136]；有意义但小、22改善/7退化/71同值。episode-only signal与全features可比，不能宣称gradient probes必要。leave-one-family-out MAE .339、compiler .533低于global .556；Gemma重新校准/重训而非Llama零shot迁移，compiler .435不超global .436/objective .438，oracle .461只说明headroom。confidence-aware fallback在discussion是未来设计建议，**作者没有事后实现该安全规则**。

Books：`TRAIN-LORA` / [Ch30](../../../../../books/part-04-training-system/30-lora.md) 185–187的input-conditioned serving rank与483的spec→neural artifact均非本项；本项选择的是**训练前episode-conditioned depth/rank program及多维行为预测**。可窄整合到target modules/rank选择之后，写清meta-data建设、未知family/小预测margin/不同backbone的实测失败及strong-default/targeted-search工程fallback；不得将backbone深度作为知识内容固定模块化位置。

## 3. 本轮剩余边界

- 指定12项的本轮题摘、日期校准、采用命题证据与Books差异判断已完成，没有普通未读工作被伪装为外部blocked。
- 论文能支持的命题均按上文边界采用；LUDI/SEED空artifact只禁止实现验证/复现断言，不阻塞可支持的方法论。MGPO HTML末尾limitations有转换提示，本轮已经读到的higher-order attribution边界可用；未以未显示尾段建立完备部署/理论保证。
- 本文件没有认证root的全部来源覆盖/stop范围、其余候选或排除样本、正式Report与Books实际写入。作者完成这些后须再交非作者语义终审；本轮不得签整日“通过”。
- 技能路由仅用于限定为研究复核，不引入代码实现或额外任务。历史记忆仅提醒submitted与availability、checkpoint/状态不等证据，本轮事实均用当前合同/原文验证。

## 4. 后续有限 Books 授权与写后复核交接

root在证据笔记完成后授予Ch24/29/30/33/77独占有限写入；本reviewer因此是下列11项Books正文作者，不能独立验自己的写入。AGENTS指定Books上下文、目标论证与相邻章节衔接已加载，只增加机制段与章末精确来源说明，未写正式Report、Ch48、Ch66、索引或LEARNING_STATE，未stage/commit/push。

| 已写材料 | 实际正文位置 | 固定来源marker |
| --- | --- | --- |
| E-MoE | Ch24，训练反向核也可以引入共享 Route Latent（训练objective侧） | SF-2026-ARXIV-2609-37533 |
| LUDI | Ch24，Uniform Corruption 的目标与 Token Time 是两种训练接口 | SF-2026-ARXIV-2609-35817 |
| RPD | Ch24，Early convergence 与 high confidence，既有跨步/二阶解释之后的层内稳定与上游熵段 | SF-2026-ARXIV-2609-36452 |
| ThinkOPD | Ch29，共享 Trace 的监督权重要与 Student Response 兼容 | SF-2026-ARXIV-2609-37044 |
| OLIVE | Ch29，Teacher Text Continuation 可以免去 Logit 接口，但不能免去状态与成本 | SF-2026-ARXIV-2609-36246 |
| adaptation compiler | Ch30，Episode Geometry 可以选择适配程序，但必须保留 Default | SF-2026-ARXIV-2609-37371 |
| ProVer | Ch33，语义 Segment 可以成为 Token 与 Episode 之间的 Credit Boundary，定位者/数值估计者段 | SF-2026-ARXIV-2609-36178 |
| AdviSD | Ch33，Advice 的预测敏感性可以选择监督，但不证明执行因果 | SF-2026-ARXIV-2609-38142 |
| MGPO | Ch77，Memory Rewrite 的总效用与新增贡献不是同一个 Reward | SF-2026-ARXIV-2609-37930 |
| MATE | Ch77，写入时保留 lossless source，读取时再构造 derived memory，action-schema因子对照 | SF-2026-ARXIV-2609-35808 |
| Mnemon | Ch77，同一lossless/lazy小节，decision/rank与waves/总判断/ECI成本补充 | SF-2026-ARXIV-2609-36059 |

新增3项材料仅在接到明确授权后定点读取，没有自行扩候选扫描：

- **OLIVE 2609.36246v1**：[精确正文](https://arxiv.org/html/2609.36246v1) §3.1–3.3/Eq1、§4.1–4.3、§5.1–5.2和AppendixA的top16配置已亲读。每轮student prefix后teacher自身AR continuation，CE仅suffix；跨tokenizer靠student重分词，不需teacher logits。多轮student动作/环境observations全部mask出loss；depth3是lag上界，partial teacher suffix无correctness过滤并不保证修复不可恢复prefix。8H200/GPU-hour对照与top16近似OPD不能支持exactKL胜负。root给出的2+2+2=6/具体缺口深入，与现有DAgger/混合occupancy相比增量只取teacher-text suffix接口/lossmask/成本；本项日期/准入最终归root独立账本，未重新扫整个批次。
- **AdviSD 2609.38142v1**：[精确正文](https://arxiv.org/html/2609.38142v1) §5.1–5.3 Eq3–5、§7 Tables2–3及AppendixE Scope已亲读，complement提供§4 fixed-teacher分析提案。两路分数均由advisor预测同recorded executor response，并不调用executor counterfactual；donor仅评分不发送；abstention另保留，GRPO原advantages全部保留。matched-count random在control自己rollouts匹配，非同batch因果干预。3training runs×4evaluations的std不同于非训练control随机std；cross-executor不足替代专门训练，Claude ACEBench multi-step可弱于GRPO。保持complement2+2+3=7的实际执行接口缺口；不采用changing-teacher convergence。
- **Mnemon 2609.36059v1**：[精确正文](https://arxiv.org/html/2609.36059v1) §4.3 Proposition1/Eq3、§6.1 cost、§6.2–6.7/Tables1–4、§7已亲读。已有raw-authority/late-construction不重写，只补strictly increasing且固定1/2的decision/rank合同、waves≠totaljudgments、ECI排除read/write与search随历史增长。各benchmark参与过开发、每configuration一次、不同grader且某些榜单只是published claims；未验证替换判定器的完整system。保持complement2+2+3=7为具体预算/消费合同，而不宣称raw-lazy全机制新缺口。

本轮只完成限定diff空白检查与本地链接/段落顺序检查，**不构成独立语义验收**。11项实际正文由root非作者核对应精确原文、自然邻接、采用深度和日级账本；SEED文字提案已交infra作者，Detectability位置/非循环审计阶梯已交root，MultiTalk/SYNTH仍为报告/具体已有覆盖。

### 非作者反馈实际发现的纠错

root实际写后指出Ch30初稿将early/mid/late误写成时间阶段、full-stack rank4误写成full-rank末四层。本人已重新定点读取v1 §4 Configuration space/AppendixG.1：候选为早/中/晚层深区域rank16 LoRA或全层rank4 LoRA，Gemma层段0–10/15–25/31–41，target为attention/feed-forward projections；原笔记上面的简写也已澄清。root持Books写锁修正实际正文，不能掩盖为初稿即正确。root还发现Ch33 ProVer插入导致旧milestone限制的“它”指代漂移，root负责将新分支移至旧限制之后；本作者不把这项写后工作签为独立验收。

## 5. Root实际写入Ch66的非作者定点复核

只读root新增的两项，未写Ch66或审自己11项。采用证据范围和当前实际正文已对读，root已落实本reviewer提出的纠错：

- **Detectability Gap**：Ch66低熵/高共识错误小节，`source-family:SF-2026-ARXIV-2609-35860`。先交代同源稳定错误，再读非循环分组→冻结partition换whole-response dispersion→独立切分的单轨迹检测阶梯，自然衔接旧段。v1 §7/AppendixI/N/T与前文方法支持所采用命题；跨signal不是独立新dataset、trajectory仅diffusion、LLaDA三任务/DreamPopQA显著及其他同向不精确、goldalias标签限制、难组非原理不可检测均在正文。最初“只覆盖部分模型/任务”有未测/不显著混淆风险，现已精确修正。**限定source→实际正文与相邻衔接非作者复核通过**；非整章或日级认证。
- **AnswerPool**：Ch66 MCQ接口/输出事件段之后、history干预段之前，`source-family:SF-2026-ARXIV-2609-37494`。本人亲读exact-v1 §3.1–3.2/3.4、§4.1–4.3、§5：合并候选后的one-use coupled assignment、同题unique有效答案、不同题gold不共用pool选项、三种guessing分母、同questions/golds/prompt/poolsize只替wrong的无关池对照均与实际正文一致。root按复核新增“不同题正确答案不共用同一池选项”，避免重复gold使assignment不可行的遗漏。未采用§3.3缺答案变体、ranking是原benchmark真实能力或任意大pool免长context混杂；保留固定MCQ基线与成本。**限定source→实际正文与自然邻接非作者复核通过**；不是替root其余材料/Report终审。
