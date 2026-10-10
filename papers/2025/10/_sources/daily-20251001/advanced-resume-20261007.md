# 2025-10-01：Advanced 历史发现续跑与非作者复核入口

作者续跑身份：Codex（接续 Euler 的本日作者工作，不充当 Dewey）。Checkpoint：2026-10-07T17:01:39+08:00。只拥有 `papers/2025/10/01` 和 `daily-20251001` 来源范围；本轮未写其他日期、Books、State、合同、索引，未 stage/commit/push。

已重读 main 工作树当前 AGENTS、统一 Prompt、研究/Report 合同、来源清单每日组及 arXiv 主题说明、ROADMAP、State 首段路由、本日 Report、Euler 补查停点及 Dewey 首批独立复核。工作树原有暂存/未暂存内容保留。最新用户指令优先：**没有调用 catchup，不用其历史限制停止查漏。** 原请求事实和旧原件均保留，新增请求另存 [advanced-resume-20261007](advanced-resume-20261007/)。

## 1. 接续范围与执行时间

本日原窗口、补充窗口 `2025-09-30 ～ 2025-09-30`、OpenAI 七案例家族的日期、`2+1+2=5`、有效深入审阅和仅报告处置不变。Euler 已写入的 R1 三撤回、R2 Qwen 全日期边界、R3 EQUISeg 机制重开、R4 EOE 混合优化均保留；本作者只核对返修及必要原件，没有授予独立通过。

新网络请求记录逐项保留 UTC 开始/结束、实际 URL、HTTP、原件及停止点。首批始于 `2026-10-07T08:44:48.160057+00:00`；六主题有效响应、已知身份对照、月表和七身份 API 的请求结束至 `08:51:01.248194+00:00`；FP8 官方页定点检查记录为 `08:54:19 UTC`。这些是执行时间，不是材料公开日。四个辅助日期搜索实际执行但仅得到二级索引/无关 STAC 同名结果及仓库，未恢复可采用的原始日证据，不据其 snippet 日期归属。

## 2. Advanced 参数恢复、实际分页与停止

实际 [表单原件](advanced-resume-20261007/boundary/advanced-form.html)明确：Announcement date 只支持年/月。CS checkbox 使用 `classification-computer_science=y`，include cross-list；查询字段与完整 URL 保存在各 `*.request.json`，不由参数猜测过滤效果。

首批 `2025-09` 至 `2025-09-30` 六查询均返回 HTTP200/no results；加入 CS archives=all、将起点展开为 `2025-09-01` 后仍空。原件分别保存在根目录和 `repair/`，**不视作有效零命中**。换至 `2025-10-01` 上界后，六查询返回下面结果，实际逐项显示 `originally announced September 2025`；有界月度发现权限来自返回字段，不把该上界理解为具体日查询。已知 RServe 身份对照恢复 1 项旧家族。没有证明空响应的服务端根因；不把异常包装成已验证的日期算法。

| 主题及 AND 查询（引号为实际短语） | 实际返回/总数 | 停止与限制 |
| --- | --- | --- |
| all=`"large language model"` AND all=`inference` | 1～50/427 | start=0 一页，末 SPECTRA 2509.24189；未请求 start=50。宽月命中不转全文队列 |
| all=`"language model"` AND all=`quantization` | 1～50/63 | start=0 一页，末2509.09550；余13未请求，不宣称该月全召回 |
| all=`"language model"` AND all=`"reinforcement learning"` | 1～50/331 | start=0 一页，末 VTPerception 2509.24776；未请求 start=50，不把331逐篇排队 |
| title=`"world model"` | 1～39/39 | 此查询无下一页；只读标题用于发现，并定点读3项完整题摘，不授39项贡献/Evidence |
| title=`memory` AND all=`agent` | 1～25/25 | 此查询无下一页；定点读 Mem-alpha，其他标题不自动成为当窗候选 |
| title=`multimodal` AND all=`"foundation model"` | 1～23/23 | 此查询无下一页；定点读 interaction-aware MoE，未把领域应用全部纳入 |

有效六页的完整原件、题摘与实际 next 链接在 `boundary/`；三种参数批次都保留，未覆盖旧请求。本轮浏览六页全部237条标题，跨页去重227身份；这不是237篇当天论文，也不是227项逐篇贡献筛选。

月表短路径 `/list/cs.CL/2509?skip=2115&show=100` 实际404，随后使用旧原件中给出的完整年月链接：[官方月表](https://arxiv.org/list/cs.CL/2025-09?skip=2115&show=100)，实际总2215、返回2116～2215，共100个 cross-list 标题，从2509.23962至2509.26628，末尾停止；不翻整月前2115项、不读100份正文。原件在 [repair/cl-month-tail.html](advanced-resume-20261007/repair/cl-month-tail.html)（boundary 保存一次重复请求），不是官方日列表。它弥补自命名机制/反证标题，不证明具体日公开。

六主题与月表合并 **309个唯一原始身份**；与旧四API的125身份交集27，**原始发现差额282**。另1项 RServe 身份对照属于旧家族，不增加差额。全部身份、版本字段、标题与本轮题摘选择见 [实际归并](advanced-resume-20261007/bounded-discovery-delta.json)。282是宽月新命中，不是候选/必审/外部故障分母；其余月度标题只留恢复线索，不声称无贡献、已经审完或确定窗外。

## 3. 23 项定点完整题摘差额

16项来自有效 Advanced 完整摘要；另外7项由月表相关标题定点取 [官方API原件](advanced-resume-20261007/selected-api.xml)，实际 7/7、无分页，当前精确版本与完整摘要在归并记录。23身份均不在旧125集合中。所有下列判断仅为机制/反证潜力，**未评分、未入本日候选、未授历史 Evidence、未作 Books 已有覆盖/采用判断**。公开月已恢复，具体日仍未确认；当前摘要不回填2025 v1。

| 当前实际题摘版本 | 原约束 → 摘要新增 → 待核选择；唯一拟 owner |
| --- | --- |
| [23958v1 RLIR](https://arxiv.org/abs/2509.23958v1) | 视频action-following缺少可验证奖励 → inverse dynamics从生成视频恢复动作 → world transition后训练的奖励代理有效性；`MULTIMODAL-WORLD-MODELS` |
| [24116v2 GLoW](https://arxiv.org/abs/2509.24116v2) | hard exploration局部反馈不足 → trajectory frontier与multi-path advantage reflection → 全局发现/局部试错的预算可比性；`AGENT-PLANNING`（不把文本游戏状态直接写成环境动力学） |
| [24418v2 GSPR](https://arxiv.org/abs/2509.24418v2) | safeguard固定taxonomy → 跨taxonomy policy reasoning/RL → 未见政策的迁移与安全边界；`PLATFORM-SECURITY` |
| [24804v1 DyMoDreamer](https://arxiv.org/abs/2509.24804v1) | 整体观测混合静态背景与动态对象 → inter-frame mask与categorical modulation进入RSSM → dynamics表示/样本效率；`MULTIMODAL-WORLD-MODELS` |
| [24832v2 SemShareKV](https://arxiv.org/abs/2509.24832v2) | prefix精确匹配限制复用 → embedding LSH与RoPE下fuzzy KV共享 → 近似状态复用的误差/成本边界；`INFER-KV-CACHE` |
| [24957v1 DUCHESS](https://arxiv.org/abs/2509.24957v1) | 多分支推理延迟不只由token数量决定 → activation probe控制terminate/duplicate/continue、难度调度 → 同准确率端到端branch成本；`INFER-SCHEDULING` |
| [24967v4 SecInfer](https://arxiv.org/abs/2509.24967v4) | finetuned防御对强注入不足 → system-prompt多路径采样与目标任务聚合 → 自适应攻击下安全/额外算力取舍；`PLATFORM-SECURITY` |
| [25050v2 AWM](https://arxiv.org/abs/2509.25050v2) | diffusion RL与预训练目标不一致 → DDPO noisy matching解释、advantage加权matching → 目标/梯度方差选择；`TRAIN-RLHF` |
| [25175v3 EasySteer](https://arxiv.org/abs/2509.25175v3) | steering执行开销与扩展接口限制 → vLLM集成与fine-grained控制 → 是否有可归因运行时增量；`INFER-VLLM`。摘要模块/倍率不足以证明production-ready，若归属落窗需定点核具体执行机制 |
| [25448v3 LLMPrint](https://arxiv.org/abs/2509.25448v3) | 已发布模型不能预埋provenance → 优化注入prompt提取token偏好并验证 → 衍生模型识别的统计/后处理边界；`PLATFORM-SECURITY` |
| [25598v1 PPR/ReNorm](https://arxiv.org/abs/2509.25598v1) | 非可验证Agent步骤奖励与最终效果不一致 → principle过程评价与outcome/process归一化 → 混合奖励归因；`TRAIN-RLHF` |
| [25678v4 Interaction-aware MoE](https://arxiv.org/abs/2509.25678v4) | 相似性routing不表达跨模态延迟依赖 → 时间间隔的interaction-type专家路由 → temporal fusion取舍；`MULTIMODAL-REPRESENTATION`。只保留跨流表示机制，不采用临床领域结论 |
| [25689v1 Collaborative Compression](https://arxiv.org/abs/2509.25689v1) | 单剪枝/量化在严格容量下质量损失 → expert pruning、mixed precision与activation联合 → 同内存约束下各机制贡献/质量；`INFER-TENSORRT-LLM`，不能仅凭组合与103GB宣称可行性已证明 |
| [25762v2 OPPO](https://arxiv.org/abs/2509.25762v2) | PPO多模型依赖与长尾停顿 → chunk流式overlap、跨步保留长generation → 权重/采样陈旧度、PPO语义及训练效率；`TRAIN-RLHF` |
| [25911v1 Mem-alpha](https://arxiv.org/abs/2509.25911v1) | 固定memory指令不能学会保存/结构化/更新 → 用全history下游QA奖励训练memory操作 → 信息损失、泛化与训练预算；`AGENT-MEMORY` |
| [26114v1 Clip-Low/High](https://arxiv.org/abs/2509.26114v1) | RLVR熵变化被归因奖励 → clipping本身的反向熵偏置/随机reward反证 → 熵控制与探索的归因；`TRAIN-GRPO` |
| [23962v1 CANON](https://arxiv.org/abs/2509.23962v1) | entropy/length单方向先验会偏置 → 指标重分组与组间/组内advantage → 探索方向及性能/成本；`TRAIN-GRPO` |
| [24203v2 Group-relative off-policy](https://arxiv.org/abs/2509.24203v2) | GRPO默认on-policy解释 → 不预设数据分布的推导、更新正则及数据整形 → off-policy使用条件；`TRAIN-GRPO`。Comments明示v2增加参考与实验，不当2025重要修订事件采用 |
| [24269v1 AdvChain](https://arxiv.org/abs/2509.24269v1) | 模仿完美CoT不训练偏移恢复 → temptation/hesitation纠偏样本 → safety/over-refusal取舍；`PLATFORM-SECURITY` |
| [24393v2 Corrective Intervention](https://arxiv.org/abs/2509.24393v2) | 最终答复安全不代表trace安全 → 替换compliance步骤并形成preference pairs → 中间推理对齐和信号归因；`PLATFORM-SECURITY` |
| [25133v1 SIREN](https://arxiv.org/abs/2509.25133v1) | 一般entropy正则在大动作空间/长轨迹下全局爆炸 → top-p/peak-entropy masks与self-anchor → 探索位置而非只熵大小；`TRAIN-GRPO` |
| [25624v3 STAC](https://arxiv.org/abs/2509.25624v3) | 孤立tool调用安全不代表序列安全 → 自动生成、执行验证、反向prompt的closed-loop攻击及自适应防御反侧 → 累积effect威胁模型；`PLATFORM-SECURITY`。当前ToolShield/自适应结果不回填v1 |
| [26354v2 Misevolution](https://arxiv.org/abs/2509.26354v2) | self-evolution收益评价忽略安全漂移 → model/memory/tool/workflow四路径反侧 → 更新时安全约束与执行验证；`PLATFORM-SECURITY` |

未采用上述任何性能数字、安全保证、理论结论或生产能力。日期恢复后只定点核精确2025事件版本、必要方法/对照/预算/反证，不继承当前摘要的实验结果；当有经复核长期差额时再向root提供必要证据和上列唯一owner提案，不直接写Books。目前无可采用的长期差额提案。

## 4. 新撤回/恢复身份冲突：不是普通 held 或访问故障

对六主题227身份实际返回的 Comments 作轻量信号检查，命中旧NVFP4 Eq2 typo与新 [2509.22536](https://arxiv.org/abs/2509.22536)。旧NVFP4隔离有效，不以当前修订公式回填历史。

新FP8官方abs实际位置与完整响应见 [回源输出](advanced-resume-20261007/fp8-withdrawal-web.json)：L19仍声明因数据管线严重bug撤回、实验有效性受影响；L28的v2明确withdrawn，L29～31又列v3～v5正文，页首当前v5本身未标withdrawn。**并存撤回说明与后续正文身份，没有恢复有效性的明确说明。** 因而不冒称全部版本均被官方标withdrawn，也不凭v5可下载恢复旧实验采用。

本轮安全处置：单列撤回/恢复状态争议排除，不准入、不评分、不进入Books、不采用摘要的lossless/性能主张；不请求日证据来继续采用失效命题。只在作者/官方明确澄清撤回适用版本、后续修复及对应有效证据时重开该身份。v2撤回修订日不生成本窗新事件。未为该信号遍历五份全文或仓库。

## 5. 精确停点与非作者窄复查包

**准备好非作者复核，不是本轮完成/通过。** 当前仍是原1家族；新增确定当窗家族0；新题摘机制/反证线索23；新撤回/恢复状态争议1；新增评分0、Evidence深审0、Books写入0。原125分账和Dewey有效首校准不推倒，23新题摘和月度库存不成为当日必须关闭的全文队列。

普通可执行剩余明确为非作者准入/来源及返修窄复查：

1. R1～R4：以 [Dewey首复核](supplement-first-review-20261007.md) 对照当前Report与 [Euler返修](supplement-20261007.md)末节；三撤回、Qwen真正缺口、EQUISeg重开、EOE混合优化、News目标日前边界及旧候选不变。不要无差别重读旧96题摘。
2. 本轮发现权限：六个实际查询/三种边界响应、真正CS checkbox、237/227去重、CL末100位置及309/27/282差额；首月不是日筛选，未请求页不授召回；上述23完整题摘均只提供有限准入潜力。
3. 必须覆盖安全/反证信号：GSPR、SecInfer、LLMPrint、AdvChain、Corrective Intervention、STAC、Misevolution；GRPO off-policy/SIREN/clipping反证与NVFP4/FP8纠错状态；所有23潜力可直接读取已保存题摘，不授全文Evidence。
4. 普通未选月标题按来源/主题/理由分层抽检即可；本作者未把未读完整题摘写成“无贡献”。无新增候选及Books写入，不存在新增性能或Books POST验收。

外部终态保留与普通待办分开：原必要机构历史段/Google原论文first-public请求仍有效；本轮23及旧75潜力缺具体官方公开日，隔离不入候选、不支持Books/无遗漏。恢复材料是含ID的当期官方日公告/快照，或作者/机构可确认精确正文公开日的原件；不以API published、submitted、月ID、月表位置、搜索snippet或一般公告日程代替。公开日恢复只重开相应身份；当前日期缺口不妨碍已执行的有界历史发现。

上述月份的其他命中未被判定真实窗外；它们是宽月恢复库存，非待全文队列，不能冒充其真实归属日已处理。本任务没有启动其他日期/Weekly，也未修改Dewey所有的复核文件。

写后检查（2026-10-07T17:01:39+08:00）：当前Report的V3接口校验通过；本日限定`git diff --check`无诊断，新checkpoint对空文件的diff检查无空白诊断（有新增差异返回1）。两份本地Markdown共18个引用目标全部存在；所有新JSON可解码，三份抓取/归并helper可解析。与现有暂存版本定点比较，原窗口、补充窗口及唯一OpenAI候选整行（含日期/评分/处置）完全相同。对Books及09月Markdown定点检索FP8 ID/精确题名未命中，没有发现需移除的本地已采用链路；这不是对全仓所有间接引用的审计。没有改共享文件或调整索引。机器检查不代替非作者裁决，普通下一步仍是上面的窄复核。
