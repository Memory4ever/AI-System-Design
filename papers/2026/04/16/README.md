# Daily Research — 2026-04-16

**规范：** V3
**窗口：** 2026-04-15T09:00:00+08:00 ～ 2026-04-16T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-27T18:44:00+08:00

## 1. 结论

最明确的长期增量是：知识覆盖与任务格式分别验收，正确文本过程与最终readout分离，base checkpoint与后训练尺度联合验收，以及trained KV共享、schema-aware speculation、event调度和质量预算驱动的straggler控制。已有39项实际Books增量通过非作者源与正文写后，包括本次恢复核验的LPC、表示诊断以及安全sensor/删除统计/watermark责任分支，以及负例梯度配比、ICL访问和batch形状责任，以及稀疏目标、存储视图与量化校准的四个条件分支。本次五项把域可辨性、训练teacher与部署执行、异常与失败分层，以及可编辑trace/旧文本光学view嵌入Ch26/75原主线，均实际写后通过。

486是旧created-day原始去重身份库存，不是当天有效论文数或全文队列。实际浏览486标题并对184个项目相关/含糊条目读完整题摘，最终冻结为86个arXiv与1个官方SDK，共87个唯一家族：39已实际整合、15已有覆盖、28仅报告、5窄争议终态隔离。必要证据、具体Books处置与日级非作者验收已通过，普通待办0。争议不支持正面采用，不声称87项都已证实有贡献。

8类官网历史入口/日期限制精确隔离，不宣称全源零遗漏。旧V2.1报告无损保存在[旧稿](../_sources/daily-20260416/V2_1_README_BEFORE_V3.md)，不继承Complete/评分/Books模板。[实际筛选与审阅](../_sources/daily-20260416/v3-reopen-notes.md)、[有效非作者范围](../_sources/daily-20260416/V3_INDEPENDENT_FOUR_CALIBRATION.md)可复查。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 相邻日完整News RSS的 Agents SDK `2026-04-15T10:00:00Z`；本次独立实际读发布正文 sandbox/manifest/harness-compute 分离与snapshot-rehydration | 受阻 | 1个软件发布事件；本次 RSS直接请求403不否定有效原始记录。Research完整历史分页仍是精确缺口，RSS不替代。 |
| SRC-ANTHROPIC | 实际研究目录 `publishedOn` 邻域04-14T13:01Z→04-22T14:12:30.673Z | 已检查 | 官方目录无本窗新条目，不重读04-15已核 AAR。 |
| SRC-GOOGLE-AI | 本次独立打开Research April月页9项与Simula正文；相邻日DeepMind历史p3及FlashTTS JSON-LD `2026-04-15T15:00:00Z`，本次独立读FlashTTS正式发布正文 | 受阻 | FlashTTS 1个确定本窗发布；Simula仅04-16日级日期须单项定点判断，不冒充09:00前。synthetic-neuron文章为AI for Science标题关闭。Publications年358列表没有首公开日级停点，精确隔离。 |
| SRC-META-AI | 相邻日Research空提取后blog p1/p2混排04-08/04-06→03-27，Publications替代路由呈2016–2020 | 受阻 | 有界替代仍无可靠本窗历史停点；需要正确历史分页/可复查日级目录，不写零事件。 |
| SRC-QWEN | 60 静态+40 动态官网研究目录；本次重新 GET 动态 API 并读 Qwen3.6-35B-A3B 全文，`extra.date` 与文章 JSON-LD 都是 `2026-04-15T10:00:00+08:00` | 已检查 | 1 个发布事件；35B/3B、open weights、preserve_thinking 与评估 harness 事实，不把 headline 当机制证明。 |
| SRC-DEEPSEEK | 实际news16条04-24→2025-12-01跨本窗 | 已检查 | 该公开目录无条目，不扩组织旧commit。 |
| SRC-MOONSHOT | Blog26条止2025-11-07，KimiK2.5 release空；组织新仓库目录止2023 | 受阻 | 新仓库有界无项；Blog缺2026历史停点，单独隔离。 |
| SRC-TENCENT-HUNYUAN | 相邻日实际 publicList 全部9条，04-23/04-30→02-13跨本窗 | 已检查 | 该公开列表无窗内条目；未列作者稿不作全网零声明。 |
| SRC-ZAI | 相邻日实际16条官网研究目录，04-29→04-07→04-01，release邻域跨窗 | 已检查 | 该可见目录无窗内条目。 |
| SRC-BYTEDANCE-SEED | 相邻日官方论文API已分页越左界到04-09；Seedance2.0卡日级04-15，具体arXiv14148v1 field `01:04:49Z`晚于本窗 | 受阻 | 有贡献信号但首公开时段未证，只隔离这一个家族；卡片后改/Submitted都不证明首次公开。 |
| SRC-BAIDU-ERNIE | Blog10项04-30→04-15ERNIE-Image→02-06；相邻日已恢复官方App JS正文和HF card | 受阻 | ERNIE-Image仅日级日期，不能凭04-15标签断定前/后09:00；版本事实保持，事件归属隔离，不无限重试超时API。 |
| SRC-XIAOMI-MIMO | 官方Paper8条06-29→03-13→02-03跨窗，blog14无日期，新仓库止2025-05 | 受阻 | Paper可见列表无项；Blog历史日级停点缺口，不当全源零。 |
| SRC-MINIMAX | EN12项05-26→03-18，CN13项04-27→03-18跨窗；TechBlog空、llms.txt48无历史日级字段 | 受阻 | 两语言可见Blog无项；TechBlog历史停点精确隔离。 |
| SRC-ARXIV | 486旧created-day宽身份全标题实际看过；184完整题摘按贡献分支而非关键词筛选，必要证据及准入已独立验收 | 已检查 | raw≠candidate；有限184题摘不称486全文审阅。日期采用组合链与自身字段，晚字段单项隔离，不支持零遗漏。 |

可见目录与全源历史入口分开判断。有事件而贡献排除不写成零命中；Daily未扫每周来源，宽库存只作主题有界查漏。

## 3. 候选与判断

以下87个唯一家族是本次冻结集合，各项证据与Books处置已独立复核；5窄争议只作安全终态隔离，不是正面证据通过。评分不由原始量/章节匹配倒推；争议仍保留贡献与精确反证。arXiv日期为官方永久ID分配、常规公告slot、连续/OAI批界与自身原字段联合支持的08～09区间推断；原字段原值见§4，不把submitted/Updated/DOI改名公告时间。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/) | 2026-04-15T18:00:00+08:00 | harness与compute分離、外置run状态恢复的官方接口事件；1 + 2 + 2 = 5 | 标准完成 | 已有覆盖 — AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；具体分权见§4 |
| [Caption First, VQA Second: Knowledge Density, Not Task Format, Drives Multimodal Scaling — 2604.13054v1](https://arxiv.org/html/2604.13054v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 任务格式替换与知识语义覆盖是两条验收轴；2 + 2 + 2 = 6 | 深入完成 | 整合 — TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)；实际正文与非作者写后通过 |
| [Correct Chains, Wrong Answers: Dissociating Reasoning from Output in LLM Logic — 2604.13065v1](https://arxiv.org/html/2604.13065v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 正确文本过程与最后答案readout可能分离；2 + 2 + 2 = 6 | 深入完成 | 整合 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；实际正文与非作者写后通过 |
| [LPC — 2604.13066v1](https://arxiv.org/html/2604.13066v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 可逆字典编码不保证模型完成编码态语义操作；2 + 2 + 2 = 6 | 深入完成 | 整合 — AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)；实际正文与非作者写后通过 |
| [Detection Without Correction: A Robust Asymmetry in Activation-Based Hallucination Probing — 2604.13068v1](https://arxiv.org/pdf/2604.13068v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 生成前检测可用不等于该方向可以纠错；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [OmniTrace — 2604.13073v1](https://arxiv.org/html/2604.13073v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | attribution option一致性不拥有输入source真值；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [Learned Representations Outrun Behavior — 2604.13082v1](https://arxiv.org/html/2604.13082v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | encoder表示形成与decoder可读性可能迟滞；2 + 2 + 2 = 6 | 深入完成 | 整合 — WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；实际正文与root非作者写后通过 |
| [Token Gradient Cancellation — 2604.13088v1](https://arxiv.org/html/2604.13088v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | token抵消公式缺少参数梯度几何条件；2 + 2 + 2 = 6 | 争议 | 暂缓 — 中心保证的精确争议与重开条件见§4/§5，不入Books |
| [FAD — 2604.13108v1](https://arxiv.org/html/2604.13108v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 架构导航artifact与writer/process可靠性分账；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [Spectral Entropy — 2604.13123v1](https://arxiv.org/html/2604.13123v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 谱熵是受限sensor而非训练停止authority；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [Exploration/Exploitation Errors — 2604.13151v1](https://arxiv.org/html/2604.13151v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 探索策略改变机会暴露集和评价分母；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；机会暴露集、条件错误率与任务结果共同验收已承载，root必要源/实际owner独立通过 |
| [Unleashing Implicit Rewards: Prefix-Value Learning for Distribution-Level Optimization — 2604.13197v1](https://arxiv.org/html/2604.13197v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | sequence aggregate弱识别与prefix value接口分开；2 + 2 + 2 = 6 | 深入完成 | 整合 — TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)；实际正文与非作者写后通过 |
| [Numerical Instability — 2604.13206v1](https://arxiv.org/html/2604.13206v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 有限数值扰动不能等同理想Jacobian/任务质量；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [KV Packet — 2604.13226v1](https://arxiv.org/html/2604.13226v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 训练wrapper换取immutable KV在线不重算；2 + 2 + 2 = 6 | 深入完成 | 整合 — INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)实际正文及相邻衔接经apr01非作者写后通过 |
| [Better/Worse with Scale — 2604.13275v1](https://arxiv.org/html/2604.13275v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | context类型与模型尺度的局部交互；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [Multilingual Post-training — 2604.13286v1](https://arxiv.org/html/2604.13286v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 语言覆盖/任务与总训练预算混杂；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [MOONSHOT pruning — 2604.13287v1](https://arxiv.org/html/2604.13287v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 输出重构和training-loss代理改变块近似结构；2 + 2 + 2 = 6 | 深入完成 | 整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与root非作者写后通过 |
| [CLTs for ViTs — 2604.13304v1](https://arxiv.org/html/2604.13304v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 跨层视觉MLP归因不证明知识唯一存储owner；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [Concrete Jungle — 2604.13313v1](https://arxiv.org/html/2604.13313v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | concreteness难度改变负例与梯度配比；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；实际正文与root非作者写后通过 |
| [WebXSkill — 2604.13318v1](https://arxiv.org/html/2604.13318v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | skill指导与直接执行的可行性依赖模型能力；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — guided/macro两部署模式的受限反转值得保留，但未改变既有asset/competence/utility设计；不将底层动作预算不匹配外推为模式通则 |
| [Tensor Memory Engine — 2604.13319v1](https://arxiv.org/html/2604.13319v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | CPU计算与FPGA内存布局消费者分责；2 + 2 + 2 = 6 | 深入完成 | 整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与root非作者写后通过 |
| [Orientation — 2604.13321v1](https://arxiv.org/html/2604.13321v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 方向可probe恢复不等于多模态答案可读出；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [Event Tensor — 2604.13327v1](https://arxiv.org/html/2604.13327v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | symbolic event依赖编译为静态/动态megakernel；2 + 2 + 2 = 6 | 深入完成 | 整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过 |
| [CONCORD — 2604.13348v1](https://arxiv.org/html/2604.13348v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | owner-only语音证据与协商补充上下文权限分开；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [OBF — 2604.13349v1](https://arxiv.org/html/2604.13349v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | KV淘汰后V子空间残差补偿、K保持不变；2 + 2 + 2 = 6 | 深入完成 | 整合 — AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)实际正文及相邻衔接经apr01非作者写后通过 |
| [PST — 2604.13356v1](https://arxiv.org/html/2604.13356v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | peer reference加权自训练不是独立真值；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [Diffusion dynamics — 2604.13366v1](https://arxiv.org/html/2604.13366v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | conditioning形态与warm-start步数在deadline下交互；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [Linear Probe Accuracy — 2604.13386v1](https://arxiv.org/html/2604.13386v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 单层monitor对旋转及多probe选择敏感；2 + 2 + 2 = 6 | 深入完成 | 整合 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；实际正文与root非作者写后通过 |
| [CoRAP — 2604.13395v1](https://arxiv.org/html/2604.13395v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 受限逐步conformal credit不能推开放轨迹保证；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [Multimodal ICL — 2604.13403v1](https://arxiv.org/html/2604.13403v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | query formulation影响表示可访问性；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；实际正文与root非作者写后通过 |
| [Dataset-Level Metrics Attenuate Non-Determinism: A Fine-Grained Non-Determinism Evaluation in Diffusion Language Models — 2604.13413v1](https://arxiv.org/html/2604.13413v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | input-run变异与固定配置跨样本方差不可混算；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [MaMe/MaRe — 2604.13432v1](https://arxiv.org/html/2604.13432v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | token merging与任意batch保持是不同算子分支；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；实际正文与root非作者写后通过 |
| [WIN-U — 2604.13438v1](https://arxiv.org/html/2604.13438v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | retain-free路径仍依赖离线曲率和参照目标；2 + 2 + 2 = 6 | 深入完成 | 整合 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；实际正文与root非作者写后通过 |
| [KL quantization — 2604.13440v1](https://arxiv.org/html/2604.13440v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 输出KL与raw-logit误差不等同量化目标；2 + 2 + 2 = 6 | 深入完成 | 整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与root非作者写后通过 |
| [Gaussian-mixture reverse kernels — 2604.13470v1](https://arxiv.org/html/2604.13470v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 受限GMM reverse kernel的表达能力与假设；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；实际正文与root非作者写后通过 |
| [FiMR — 2604.13491v1](https://arxiv.org/html/2604.13491v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 中间图像评价触发与消费feedback时点不同；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；实际正文与root非作者写后通过 |
| [Cluster-aware Upcycling — 2604.13508v1](https://arxiv.org/html/2604.13508v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | dense到MoE初始化仅保局部线性结构；2 + 2 + 2 = 6 | 深入完成 | 整合 — MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)；实际正文与root非作者写后通过 |
| [RTR-DiT — 2604.13509v1](https://arxiv.org/html/2604.13509v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | reference-conditioned streaming KV的pin/update边界；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — reference/cross-attention/上一帧刷新是具体streaming策略，已有identity/invalidation/pin合同承载边界；不证明新条件exact状态或无界实时质量 |
| [SFT–GRPO overlap — 2604.13515v1](https://arxiv.org/html/2604.13515v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | SFT与RL prompt交集影响不同验收对象；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — 阶段prompt交集实验值得保留，但难度未匹配/answer injection改任务，0/30/100排序不支持稳定overlap策略 |
| [ToolSpec — 2604.13519v1](https://arxiv.org/html/2604.13519v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | schema与自由value draft分责但都由target核验；2 + 2 + 2 = 6 | 深入完成 | 整合 — INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；实际正文与非作者写后通过 |
| [ATLAAS — 2604.13523v1](https://arxiv.org/html/2604.13523v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | MLIR截断算子不支持所称普遍饱和语义；2 + 2 + 2 = 6 | 争议 | 暂缓 — 仅隔离饱和泛化保证，Stage1/有限bit证明不全部否定 |
| [RiskWebWorld — 2604.13531v1](https://arxiv.org/html/2604.13531v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 专门化GUI checkpoint对prompt缩短退化更大；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [YoloFS — 2604.13536v1](https://arxiv.org/html/2604.13536v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | filesystem proposal/journal与用户commit分权；2 + 2 + 2 = 6 | 深入完成 | 整合 — AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md)实际正文及相邻衔接经apr01非作者写后通过 |
| [CoDIT — 2604.13538v1](https://arxiv.org/html/2604.13538v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | chat/base对照信号与plausibility admission分开；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — 同prefix双教师logprob差构造监督是真实替代配方，但Taylor局部/调测同用及退步不足支持instruction-only或长期新责任 |
| [UniRect — 2604.13540v1](https://arxiv.org/html/2604.13540v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 理想prompt纠错目标不同于原prompt选择权；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；实际正文与root非作者写后通过 |
| [DynamicGate concurrency — 2604.13546v1](https://arxiv.org/html/2604.13546v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 动态gate并发保证依赖序列化或快照条件；2 + 1 + 2 = 5 | 争议 | 暂缓 — 中心保证的精确争议与重开条件见§4/§5，不入Books |
| [YOCO++ — 2604.13556v1](https://arxiv.org/html/2604.13556v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 先mix再物化的trained跨层cache共享；2 + 2 + 2 = 6 | 深入完成 | 整合 — INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；实际正文与非作者写后通过 |
| [MM-Doc-R1/SPO — 2604.13579v1](https://arxiv.org/html/2604.13579v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | similarity trajectory baseline的偏差和有限收益；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [C2 — 2604.13618v1](https://arxiv.org/html/2604.13618v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | rubric扩展仍继承原偏好label而非新truth；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — 同偏好label生成rubric与拒绝后双查询是受限抗误导实现，不产生独立truth；既有judge共有盲点与外部promotion主线无需扩成新算法authority |
| [(How) Learning Rates Regulate Catastrophic Overtraining — 2604.13627v1](https://arxiv.org/html/2604.13627v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | base cooldown与SFT更新尺度共同影响可微调性；3 + 2 + 2 = 7 | 深入完成 | 整合 — TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；实际正文与非作者写后通过 |
| [CSD — 2604.13634v1](https://arxiv.org/html/2604.13634v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | semantic rescue会改变target distribution；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — 作者明确lossy acceptance；有限OCM/SCG经验与开销边界，不入Books |
| [Sim-and-Real Co-Training — 2604.13645v1](https://arxiv.org/html/2604.13645v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | sim/real表征混合应保留action差异domain条件；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与root非作者写后通过 |
| [OLS Transformer — 2604.13656v1](https://arxiv.org/html/2604.13656v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 按当前X/Y构造weights不是fixed-forward通用OLS；2 + 1 + 2 = 5 | 深入完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [Weight Patching — 2604.13694v1](https://arxiv.org/html/2604.13694v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 参数差分source与activation传播接口分开；2 + 2 + 2 = 6 | 深入完成 | 整合 — WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；实际正文与root非作者写后通过 |
| [Co-FactChecker — 2604.13706v1](https://arxiv.org/html/2604.13706v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 编辑trace和抑制旧verdict是control artifact；2 + 2 + 2 = 6 | 深入完成 | 整合 — AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)；实际正文与root非作者写后通过 |
| [TimePro-RL — 2604.13715v1](https://arxiv.org/html/2604.13715v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 物理audio时间token与模态输出接口；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；实际正文与root非作者写后通过 |
| [Repository Compression — 2604.13725v1](https://arxiv.org/html/2604.13725v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 训练/backbone差异不支持纯表示因果比较；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [VLAJS — 2604.13733v1](https://arxiv.org/html/2604.13733v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 临时teacher方向regularizer与部署状态分离；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与root非作者写后通过 |
| [OffloadFS — 2604.13743v1](https://arxiv.org/html/2604.13743v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | metadata/block grant与offload compute分责；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — 受限inode/block并发与peer预处理是具体工程分支，尚未改变样本lineage/worker曝光与恢复主线；不把读密集实例外推通用近数据最优 |
| [Cognitive Companion — 2604.13759v1](https://arxiv.org/html/2604.13759v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | monitor检测与guidance任务收益不可混同；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [RealVuln — 2604.13764v1](https://arxiv.org/html/2604.13764v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | coverage分母和F-beta排序影响安全headline；2 + 1 + 2 = 5 | 深入完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [MAGE — 2604.13777v1](https://arxiv.org/html/2604.13777v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | memory-graph自生成监督仍非独立遗忘真值；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [QuantileMark — 2604.13786v1](https://arxiv.org/html/2604.13786v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | CDF消息bin/重叠与detector目标分别验收；2 + 2 + 2 = 6 | 深入完成 | 整合 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；实际正文与root非作者写后通过 |
| [FIDeL — 2604.13788v1](https://arxiv.org/html/2604.13788v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | anomaly阈值与VLM失败过滤分别验收；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际正文与root非作者写后通过 |
| [Syn2Seq-Forcing — 2604.13793v1](https://arxiv.org/html/2604.13793v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | exo/ego序列与条件输入的受限表示取舍；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [DASH-Q — 2604.13806v1](https://arxiv.org/html/2604.13806v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 有限校准下对角曲率代理的偏差—方差分支；2 + 2 + 2 = 6 | 深入完成 | 整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与root非作者写后通过 |
| [UI-Copilot — 2604.13822v1](https://arxiv.org/html/2604.13822v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | tool/action分训后runtime组合不等joint-on-policy；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [BehR — 2604.13824v1](https://arxiv.org/html/2604.13824v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | logged action likelihood不等完整world一致性；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — frozen-reference单个logged-action likelihood代理有受限证据，不证明完整策略/闭环一致性；既有真实性与行为价值分账无需新增配方 |
| [CARP/SAS — 2604.13833v1](https://arxiv.org/html/2604.13833v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | prompt-relevance offset可能与安全偏好冲突；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — relevance特征与安全偏好反转、差阈值回BT是受限recipe；保rawBoN/安全退步，不采用prompt重构是真因果或新稳定规范 |
| [SparseBalance — 2604.13847v1](https://arxiv.org/html/2604.13847v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | SAB重排与DST改变attention预算分别控制；3 + 2 + 2 = 7 | 深入完成 | 整合 — TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；实际正文与非作者写后通过 |
| [DiPO — 2604.13902v1](https://arxiv.org/html/2604.13902v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 近似PPL理论不能保证真实模型entropy；2 + 1 + 2 = 5 | 深入完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [SparseGen — 2604.13905v1](https://arxiv.org/html/2604.13905v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 3D query预算与view偏差的受限对照；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [Compiler Remarks — 2604.13927v1](https://arxiv.org/html/2604.13927v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | compiler反馈质量与变换正确性分账；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md)；compiler诊断与功能/effect验收分权已承载，root必要源/实际owner独立通过 |
| [ASTRA — 2604.13938v1](https://arxiv.org/html/2604.13938v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | reference identity与目标canvas空间绑定不同；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；实际正文与root非作者写后通过 |
| [HINTBench — 2604.13954v1](https://arxiv.org/html/2604.13954v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 整轨迹风险与first-risk执行前定位不同；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [GEM3D-CIM — 2604.13969v1](https://arxiv.org/html/2604.13969v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 电路能耗估算不能证明LLM serving收益；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [FinePhrase — 2604.13977v1](https://arxiv.org/html/2604.13977v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | prompt/generator/source mix与训练效用分账；2 + 2 + 2 = 6 | 深入完成 | 整合 — TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)；实际正文与非作者写后通过 |
| [Adaptive Conformal — 2604.13991v1](https://arxiv.org/html/2604.13991v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | claim过滤安全阈值的分位方向有反例；2 + 2 + 2 = 6 | 争议 | 暂缓 — 中心保证的精确争议与重开条件见§4/§5，不入Books |
| [Reward Design — 2604.13993v1](https://arxiv.org/html/2604.13993v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | foreground attention reward只是visual reliance代理；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |
| [Learned or Memorized — 2604.13997v1](https://arxiv.org/html/2604.13997v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 改写敏感度不证明训练membership或记忆血缘；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [Diffusion LM for ASR — 2604.14001v1](https://arxiv.org/html/2604.14001v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | sequence MC重排与位置概率CTC融合不同；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；实际正文与root非作者写后通过 |
| [Memory Transfer Learning — 2604.14004v1](https://arxiv.org/html/2604.14004v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 抽象memory与原轨迹fallback的跨域边界；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过 |
| [EPI — 2604.14010v1](https://arxiv.org/html/2604.14010v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 重要性mask应约束最终optimizer delta；2 + 2 + 2 = 6 | 深入完成 | 整合 — TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)；实际正文与root非作者写后通过 |
| [MAny — 2604.14016v1](https://arxiv.org/html/2604.14016v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | conditional projector输出与语言矩阵merge分责；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；实际正文与root非作者写后通过 |
| [Stochastic Trust Region — 2604.14017v1](https://arxiv.org/html/2604.14017v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 接受的TR step反驳通用步长下界；2 + 2 + 2 = 6 | 争议 | 暂缓 — 中心保证的精确争议与重开条件见§4/§5，不入Books |
| [POINTS-Seeker — 2604.14029v1](https://arxiv.org/html/2604.14029v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 旧文本转图像、近期协议保文本需训练适配；2 + 2 + 2 = 6 | 深入完成 | 整合 — AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)；实际正文与root非作者写后通过 |
| [Shallow ReLU Symmetry — 2604.14037v1](https://arxiv.org/html/2604.14037v1) | 2026-04-16T08:00:00+08:00 ～ 2026-04-16T09:00:00+08:00 | 浅层ReLU等价类不直接迁移深LM融合；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4 |

6分真实知识缺口及5分安全/纠错反证使用深入override，不抬分触发Deep；具体必要范围见逐项证据。未经实际写后复核的拟增量不计已整合。

## 4. 证据与知识整合

### [The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)

原发布正文Native sandbox execution / Separating harness from compute与News RSS原时间2026-04-15T10:00:00Z支持本窗事件。Manifest描述workspace，harness与compute分离，外置state支持snapshot/rehydration；这是官方接口声明，不是跨provider等价/安全/性能实测。1 + 2 + 2 = 5，标准审阅。Ch84 AgentRun/Workflow state明确run、context、memory和Tool/Environment副作用的owner；Ch81 Toolspace段分开registry、sandbox process/filesystem与workflow版本。已有覆盖，不重复正文或推snapshot撤销外部effect；非作者采用终核待完成。

### [Caption First, VQA Second: Knowledge Density, Not Task Format, Drives Multimodal Scaling — 2604.13054v1](https://arxiv.org/html/2604.13054v1)

官方 HTML §3.2–3.4、§4.2：同图像/架构/总训练预算下，caption/VQA 比例从28%/17%改45%/0，synth-VQA保28%/17%；3B模型的综合均值.6018/.5973/.6050，但 MMBench .7507→.7000、ScreenVIVOv2 .3805→.3333（synth .2801），不能写所有指标都保持。pair-image描述/MLLM过滤扩充语义是受限构造，不是直接测量知识总量；一个固定3B实验不能证明普遍 scaling bottleneck。拟2+2+2=6，若Ch27确缺“任务格式替换与语义内容密度分别验收”，按知识缺口深入；当前读过Ch27质量/lineage和Ch23 encoder基线，该机制现已获得真实正文承载。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:00:26Z`，DataCite初始created `2026-04-16T01:43:08Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13054`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)；实际正文与非作者写后通过。已完成真实写入和root/apr02单篇非作者源→owner/写后；具体范围见[独立复核](../_sources/daily-20260416/V3_INDEPENDENT_FOUR_CALIBRATION.md)，不预支日Gate。

### [Correct Chains, Wrong Answers: Dissociating Reasoning from Output in LLM Logic — 2604.13065v1](https://arxiv.org/html/2604.13065v1)

官方 HTML §3、§4.5–4.7：九种Boolean operator、五模型/至八运算符的外部可核任务。Claude深度7原ETT cohort 34/300错误均是trace最终计算true而声明false；另seed 31错例的新会话extractor Claude31/31、GPT30/31，两个分母不得混。ETT局部0/300不是开放任务或内部推理保证；约140额外token；max256截断制造30–54pp假collapse。已实际对读Ch66过程/结果分账与Failure Direction；拟2+2+2=6、知识缺口深入，窄命题是可外部验证的文本过程与最终readout仍可分离，不能称内部trace faithful。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:00:41Z`，DataCite初始created `2026-04-16T01:43:25Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13065`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；实际正文与非作者写后通过。已完成真实写入和root/apr02单篇非作者源→owner/写后；具体范围见[独立复核](../_sources/daily-20260416/V3_INDEPENDENT_FOUR_CALIBRATION.md)，不预支日Gate。

### [LPC — 2604.13066v1](https://arxiv.org/html/2604.13066v1)

实际官方 exact-v1 §3.1–3.6、§4.2、§5.2–5.3/Tables1–2、§7。用 whitespace 单位搜非重叠子串，替换 meta token 并附字典；节省条件将字典与meta token也计入，软件可重建不等模型在编码态正确完成分析。模板解压测试的Claude3.7/Nova与算法解压aggregate Levenshtein不是同一指标，后者.909并非exact match；未测试目标analytics。§4.2/§7称解压为理解下界缺证明，查字典/复制成功仍能分析失败。Ch75已有任务相对充分性/raw fallback与时间break-even，但原先缺可逆字典codec与LLM语义操作的接口区别；Ch78确定性输出重建不代替此输入理解问题。2+2+2=6，知识缺口深入，apr02必要源→owner已通过；Ch75压缩主线真实正文已补codec-vs-target-task合同，不采用下界或普遍无损理解保证，root实际正文与相邻衔接非作者写后已通过。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:00:42Z`，DataCite初始created `2026-04-16T01:43:26Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13066`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置：整合 — AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)压缩主线中实际两段及证据区已落实；apr02于2026-09-27非作者实际重开必要官方v1、正文及前后交接通过，见[恢复写后复核](../_sources/daily-20260416/V3_RESTORE_INDEPENDENT_WRITE_AFTER.md)。未复现实验，不预支日级Gate。

### [Detection Without Correction: A Robust Asymmetry in Activation-Based Hallucination Probing — 2604.13068v1](https://arxiv.org/pdf/2604.13068v1)

采用官方 PDF（HTML本次不可用），§3.4–3.6、§7.1–7.6：552 factual labels/三数据集/七117M–7B模型，训练fold内PCA95%+nested5fold logistic，pairedfold AUC；single L40S48GB/float16。仅Pythia1.4B与Qwen2.5 7B有显著早峰，GPT2XL p=.054不显著、Pythia6.9近乎平；不能推统一1B阈值或posttraining因果。局部0 steering corrections不能证明不存在可干预节点，短1–2token生成可能限制传播。已实际读Ch66“可解码 Failure Direction 不拥有自动纠错权”及internal/verbalization/steering/deployment分账；拟2+2+2=6标准审阅已有覆盖。apr02已独立核§3.4–3.6/§7.4：steering的层/强度/干预样本分母未披露；0%只作为作者报告，不能当充分因果反证，采用范围仅检测≠纠错的既有边界。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:00:46Z`，DataCite初始created `2026-04-16T01:43:29Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13068`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [OmniTrace — 2604.13073v1](https://arxiv.org/html/2604.13073v1)

实际[exact-v1](https://arxiv.org/html/2604.13073v1) §3.2 Algorithm1、§4.2、B.2/B.3。每生成 token 将 attention/gradient signal 聚合到 source unit，再按 POS/confidence 对输出 chunk 投票；audio/video 的 source unit 依赖 ASR segmentation 和 timestamp。B.3 的 93.84% 是 attribution argmax 与所选答案 option 的一致性，不检查答案正确，也不是因果 faithful；标签含 LLM judge，26.6% 子集人工对照不能给全域 provenance 真值。Ch66“Model Self-report 不能拥有输入来源真值”已明确 authoritative lineage、cue intervention 与 sensor 分责，具体承载可采用判断，不把 agreement 升级为 source authority。2+1+2=5，标准已有覆盖 `PLATFORM-EVALUATION-SYSTEM`；apr01必要原文与实际owner定点核已通过，不追加正文。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:00:51Z`，DataCite初始created `2026-04-16T01:43:36Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13073`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [Learned Representations Outrun Behavior — 2604.13082v1](https://arxiv.org/html/2604.13082v1)

实际官方HTML §4–6、AppB.1.1/B.2/B.3/D/E/F，并打开官方PDF v1确认标题和§5.2/同结构干预。base8 Collatz encoder的parity可读出早于序列答对；冻结成熟encoder、换新decoder/rewind与反向transplant分别测，不能把fresh probe等同原路径使用。pretraining成熟encoder的费用不含在2.75倍后阶段比较内；3seed的端点54.4/93.6、62.0/95.9异质，不能把主run97.6%当普遍值。跨base改变长度，Collatz/GCD改变输入格式；AppB.1.1没有明确说明online采样排除固定heldout整数，故不采用已充分证明未见数字泛化。Ch5:183–215已分decodability/intervention/实际use、训练augmentation与runtime访问，但没有把训练迟滞拆为表示形成与decoder-readout的freeze/transplant诊断。拟2+2+2=6，最窄Ch5该节加入条件诊断分支，若独立判已有覆盖则真实指其论点，不因小算法任务关闭。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:01:02Z`，DataCite初始created `2026-04-16T01:43:49Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13082`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；本次实际正文与root非作者写后通过。2026-09-27 root重开必要v1、实际段落及相邻交接完成独立复核；未复现实验，具体采用边界与写后记录见[v3恢复笔记](../_sources/daily-20260416/v3-reopen-notes.md)。

### [Token Gradient Cancellation — 2604.13088v1](https://arxiv.org/html/2604.13088v1)

官方PDF-v1封面/Cor3.2与HTML-v1一致，已排除raw后改IBPO摘要。实际必要§3.1–3.4、§4–6、§8/AppC/K偏差相关段；shared identical context-token + centered A +同effective coefficient下抵消成立，而高频token不是已证明reward-irrelevant集合。Min-Replace/Adv-Orthogonal stop-grad变换改变importance估计，本身biased；同生成token/steps/rollout预算和两Qwen数学代码实验不足以证明所有熵塌陷的必要原因。Cor3.2 Eq5共同c(x)>0缺梯度几何条件：softmax p=(.6,.3,.1)，两个等回报输出a/b、相同detached κ，在对两者等权更新g=.5[(e_a−p)+(e_b−p)]时，log(p_a/p_b)一阶变化=.5η[(e_a−e_b)·(e_a+e_b−2p)]=−.3η，但其κ_a−κ_b=0；即一般线性组内更新不满足该式。Cor3.3的A=(1,1,−2)、u=(1,3,2)满足A·u=0，只说明全u相等不是抵消的必要条件；原文已保留degenerate/zero-measure例外，不能把这一例独立写成推翻Cor3.3。争议集中在Eq5缺失的参数几何/更新算子条件，不否定两样本toy、近似变换或全部实验。2+2+2=6，反证深入、争议/暂缓，不写Books；重开需说明Eq5所需几何或明确其代理近似性质。apr02已独立核必要原文与−.3η反例，窄争议终态PASS，不扩全附件。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:01:09Z`，DataCite初始created `2026-04-16T01:43:58Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13088`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：暂缓 — 中心保证的精确争议与重开条件见§4/§5，不入Books。apr20_resume已独立复用未变必要原文核与该反例，对这一窄隔离终态通过，见[六项有限复核](../_sources/daily-20260416/V3_APR20_BOUNDED_SIX_DISPUTE_REVIEW.md)；不代表本日日级Gate。

### [FAD — 2604.13108v1](https://arxiv.org/html/2604.13108v1)

实际官方 exact-v1 §2–3.5与Tables，24定位任务×4format、15artifact/process Rust tasks、96错误注入writer runs。format差异不显著不证明格式无关，silently-corrupted S-expression与解析失败分开；自动生成与人工curated差异p=.515不证明短描述造成优势。first-author7012-session观察有before/after变化，但post读取/不读取均1.65，不能识别阅读因果；编辑/开放architecture治理未测。材料可采用的artifact导航和格式writer可靠性由Ch75“Context Map是轻量导航状态，不是事实副本”(354–358)、Context Identity及Ch78 Tool Contract声明/真实入口分权具体承载，不把descriptor当事实authority。2+1+2=5，拟标准已有覆盖，等待独立裁决；不以成熟主题自动关闭受限对照。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:01:37Z`，DataCite初始created `2026-04-16T01:44:27Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13108`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [Spectral Entropy — 2604.13123v1](https://arxiv.org/html/2604.13123v1)

实际官方HTML §3–12，1layer d128/4heads/FF512、p97 arithmetic，AdamW1e-3/WD1/batch512，10seed、普适性5seed，512固定probe每200step float64 covariance。混合z与相邻sample再算loss会改变训练输入/目标几何，norm匹配不能单独识别entropy因果；MLP已出现entropy collapse却无grokking，任务阈值变化，LOO接近终点预测误差与早期lead不能合并为生产早停保证，相关系数/CI也有不一致。Ch28:1254实际正文已要求谱诊断作sensor、尺度校准与heldout/noisy fallback而非learning-rate/停止authority。2+1+2=5，拟标准已有覆盖，只采用局部诊断/非充分性的边界；不采用通用必要性、因果或86%节省。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:01:56Z`，DataCite初始created `2026-04-16T01:44:50Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13123`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [Exploration/Exploitation Errors — 2604.13151v1](https://arxiv.org/html/2604.13151v1)

实际官方HTML §3–7与官方PDF v1 §4 Eq1/Table1及§7复核一致。环境区分observed/邻域unobserved/unknown，pending task与未观察cell共同定义四种opportunity；gain不够，还跟踪无进展段的loop/reuse，推进时reset，属显式策略约定而非任意合理策略无误判定理。case-normalized分母由自身轨迹选择，不能脱离success/demand作能力排行；3seed、T0，steps只统计成功轨迹；structured harness组合和semantic干预不能作单memory组件因果。Ch66:2070–2094已有neutral探索/first causal error/opportunity与exploration-vs-exploitation，但未说明策略改变case暴露分母/同success不同opportunity分布。拟2+2+2=6，Ch66该段最窄补机会集和轨迹分母分账；不复制grid算法为开放环境通用规范。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:02:24Z`，DataCite初始created `2026-04-16T01:45:31Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13151`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；机会暴露集、条件错误率与任务结果共同验收已承载，root必要源/实际owner独立通过。root本轮已实际重开必要exact-v1并对读对应正文与相邻主线，独立裁决通过，未复现实验；保留本文局部机制/反证，不把主题相似写成精确算法已覆盖。

### [Unleashing Implicit Rewards: Prefix-Value Learning for Distribution-Level Optimization — 2604.13197v1](https://arxiv.org/html/2604.13197v1)

官方 HTML §2.2/3、§4.2/4.3：sequence aggregate logratio不能唯一识别局部prefix value；length-normalized prefix BCE用最终outcome label，不是校准正确率/step truth。DistRL给old-policy高概率candidate集合的TD branch与采样token GAE，共享online IPVRM；no extra rollout不等于零RM/full-vocab成本。ProcessBench likelihood与prefix口径不同，早步weight助ProcessF1、晚步助BoN；Table6使用DPO/旧Implicit RM时不稳定超GRPO，不能归因为所有candidate更新普遍有效。实际对读Ch32已存coherent prefix value/MC/TD，尚缺aggregate weak-identification与候选词表更新接口，拟2+2+2=6知识缺口深入，Ch33 owner已独立对读并实际整合。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:04:25Z`，DataCite初始created `2026-04-16T01:46:42Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13197`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)；实际正文与非作者写后通过。已完成真实写入和root/apr02单篇非作者源→owner/写后；具体范围见[独立复核](../_sources/daily-20260416/V3_INDEPENDENT_FOUR_CALIBRATION.md)，不预支日Gate。

### [Numerical Instability — 2604.13206v1](https://arxiv.org/html/2604.13206v1)

实际官方HTML §III–V，Llama3.1-8B双RTX A5000、GPTOSS20B在i9-10900X，TruthfulQA/AdvBench，bf16/FP32/FP64。f为unembedding前最后hidden state；有限epsilon quotient不能直接等同理想Jacobian导数，更不能以人工near-tie prompt/全部4096方向推所有输入普遍chaos。§IV-F paired noise均值改测量对象、额外10～100forward并非已测免费；未实测Agent失败因果/语义修复。Ch49:1508–1518实际已有precision/reduction/kernel/artifact与数值重放、允许容差和速度共存。2+1+2=5，拟标准仅报告：局部有限算术诊断有可保留反证，但尚无足以改变部署路径的任务质量/成本证据，不为了‘数值’主题强行新增Books；将中心广义主张明确收窄，不把整个实验伪称无效。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:04:39Z`，DataCite初始created `2026-04-16T01:46:56Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13206`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [KV Packet — 2604.13226v1](https://arxiv.org/html/2604.13226v1)

实际官方HTML §2–4.5、官方PDF-v1标题/§2–3绑定一致。冻结base，独立文档与全局Header/Trailer soft token一起prefill成immutable packet；以full-context teacher续写KL训练wrapper，在线只realign RoPE/拼接/query与decode，文档内部状态仍未看到其他文档，不采用Fig2 caption的数学等价或零全部成本。§4.3摘要Qwen2.5与setupQwen3-4B身份冲突保留；TTFT含CPU/GPU传输但不含离线训练/预缓存。Biography训练跨到Hotpot表现.18低于NoRecompute.24，MusiQue也存在full-recompute质量差距。Ch45:180–186已有chunk concat因果修复与full fallback，341–347是anchor-conditioned局部重算；缺冻结base、训练wrapper换取在线不重算的替代分支。拟2+2+2=6、缺口深入，主owner Ch45，在causal repair之后窄补训练/缓存版本、近似质量和回退，不承诺任意压缩codec或生产SLO。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:05:45Z`，DataCite初始created `2026-04-16T01:47:26Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13226`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) `SF-2026-ARXIV-2604-13226` 两段已实际写入选择性因果修复之后。root必要源→owner采用核与apr01本次实际正文/相邻衔接写后均通过，未复现实验；详见[八项有限独立核验](../_sources/daily-20260416/V3_APR01_BOUNDED_EIGHT_INDEPENDENT_AUDIT.md)。

### [Better/Worse with Scale — 2604.13275v1](https://arxiv.org/html/2604.13275v1)

实际官方HTML §2–4/AppC Table3–6。47关系、Cerebras/Pythia两families，在四种context插入条件读gold/distractor logits；Table3 gold−distractor margin变化支持语义与随机/无关条件尺度趋势不同，而单独distractor logit的加性基准不固定，不能直接等同概率上升或copy机制。训练数据/架构跨规模未受控，induction/filter只为解释；负margin的log-log拟合没有明确取绝对值协议，不采用精确通用指数。Ch75:414–425及465已有noise slice/admission边际价值，但该实验未测完整答案/Agent行为或生产选择，不能用主题相同作“完全已覆盖”。拟2+1+2=5标准仅报告，保留有界context-type×scale反证，不写普遍更大更抗干扰或稳定copy机制。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:09:21Z`，DataCite初始created `2026-04-16T01:48:38Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13275`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [Multilingual Post-training — 2604.13286v1](https://arxiv.org/html/2604.13286v1)

实际官方HTML §3–6/Tables1–3。翻译构造11语言两任务，Qwen/Gemma不同尺度；同每语言样本量、6epoch而新增语言增加总数据/更新预算，validation混合语言亦变，不能以§3.2“isolating volume”或回归项证明语言多样性单因果。0.6B API有退步，数学/大模型不同；API exact-match不是真实工具副作用成功，显著不异也非等价证明。Ch29现有multilingual retain、train budget/目标回归覆盖一般策略，但这项具体crosslingual容量对照不因主题成熟而排除。拟2+1+2=5标准仅报告：局部观察保留，尚不能给独立于训练体量的mixture选择规则或取消直接低资源语言监督。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:09:52Z`，DataCite初始created `2026-04-16T01:48:54Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13286`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [MOONSHOT pruning — 2604.13287v1](https://arxiv.org/html/2604.13287v1)

实际官方HTML §2.1–2.3/Alg1、§3.2–3.4/Table3、AppA.3及A.7相关段；PDF入口本次internal error，但HTML必要命题足够，不泛称正文受阻。局部output reconstruction与empirical-Fisher training-loss代理共同加权、按全零损失归一；Fisher非一般真实Hessian，且假设dense点梯度近零。shared XXᵀ基底+row-specific低秩梯度项用Woodbury，精确性只针对已选block近似，λ=0端点不能套基底逆；实际LLM为省成本只attention多目标、projection仍reconstruction。Hessian通常只算一次，λ按train PPL/损失调，离线成本不免费；1B2:4平均41.32→41.24退步，不能录“全设置改善”。Ch49当前2:4敏感度/annealing与local reconstruction边界未分两个代理怎样改变块结构、重算/标定成本和质量选择。拟2+2+2=6缺口深入，窄owner Ch49两种稀疏段附近，不采用普遍最优/整网质量或端到端速度保证。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:09:56Z`，DataCite初始created `2026-04-16T01:48:56Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13287`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与root非作者写后通过。具体写入与反例限域见本日恢复笔记；root已核实际正文及相邻交接，未复现实验。

### [CLTs for ViTs — 2604.13304v1](https://arxiv.org/html/2604.13304v1)

实际官方HTML-v1 §3.1–3.2/§4.1–4.2/§5.1–5.2/Table5。三角decoder跨层重构MLP输出，训练teacher activation与运行replacement activation有shift；贡献归一分母是重构值，keepTop4/dropTop1剪的是最后重构项，不是原模型早层因果删层。CLS/晚层配置与全patch replacement退步须分账；CIFAR base61.65/full61.31/keepTop4-all59.96并非所有简化保持原accuracy。Ch5“解释模型也有自己的Faithfulness Budget”实际正文217–230已要求replacement reconstruction、未替换attention、graph pruning、原模型intervention与选择范围；能承载此受限实现，不能宏观以“知识分布式”否定局部稀疏路径。拟2+1+2=5标准已有覆盖。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:11:08Z`，DataCite初始created `2026-04-16T01:49:21Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13304`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [Concrete Jungle — 2604.13313v1](https://arxiv.org/html/2604.13313v1)

实际官方HTML-v1 §2.1–2.3/Eq1–4、§3.1–3.3/Tables2–3、Limitations。InfoNCE正例pull=hard/easy负概率总和；hard-logit margin改变hard/easy比例，但正例概率也变，不能采用作者“hard增加必等量挤掉easy”绝对梯度说法。psycholinguistic concreteness用于caption/image编辑与margin，不证明语义negative真实有效；visual difference相关不是生成负例验真。batch大小/通用uniformity与composition判别有取舍，adaptive54.18对static54.07接近，WG-group7.75低于static8.50、SugarCrepe83低于DeGLA89.23，general任务亦有退步。Ch23:395–418现有多目标/正负margin说明，尚无batch中easy质量聚合与hard-margin reweight取舍分支。拟2+2+2=6真实缺口深入，主owner Ch23全局对齐段窄补相对信号分配、负例有效性和通用表示回归，不采用统一margin、规模保证或concreteness真值。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:11:37Z`，DataCite初始created `2026-04-16T01:49:34Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13313`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；实际机制正文与root非作者写后通过。2026-09-27 root独立重开必要v1并顺读真实段及相邻论证，具体写入位置和代价/回退见[v3恢复笔记](../_sources/daily-20260416/v3-reopen-notes.md)；未复现实验。

### [WebXSkill — 2604.13318v1](https://arxiv.org/html/2604.13318v1)

实际官方HTML-v1 §3.1–3.3/§4.1–4.2/§5.1–5.3。每skill同时保存parameterized browser程序与step guidance；grounded runtime自动执行序列，guided Agent逐步动作并观察，URL/元素过滤不证任务意图匹配。GPT-5 grounded69.5/guided68.8近似，Qwen3.5-122B-A10B guided53.9胜grounded48.7，模型/训练混杂不能推出强弱模型通用因果选择；Mix也非免费最优。154 cleaned WebArena/11 live网站、30 interaction-step宏调用不能等同底层动作/实际成本一致；GPT4.1 judge、synthetic轨迹训练边界保留。skill调用完成仍可因post-skill推理失败。Ch84:150–249实际mixed asset/competence routing/paired utility尚未明确同资产的自动宏执行vs逐步guidance部署分支。拟2+2+2=6缺口深入，主owner Ch84在混合资产与competence交接补mode、scope与任务验收，不重复权限总则。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:12:18Z`，DataCite初始created `2026-04-16T01:49:42Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13318`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — guided/macro两部署模式的受限反转值得保留，但未改变既有asset/competence/utility设计；不将底层动作预算不匹配外推为模式通则。root本轮已实际重开必要exact-v1并对读对应正文与相邻主线，独立裁决通过，未复现实验；保留本文局部机制/反证，不把主题相似写成精确算法已覆盖。

### [Tensor Memory Engine — 2604.13319v1](https://arxiv.org/html/2604.13319v1)

实际官方HTML-v1 §3/Eq1–3、§4–5、§6.1–6.2。CPU compute不迁移，显式alias地址窗口/配置由FPGA模块分解scatter请求并聚合cacheline，consumer按导出layout运行而免materialized中间视图；这不是一般PIM计算或软件零成本transpose。ARM A53/KR260 FPGA300MHz/DDR4/Linux22.04/GCC11.4-O2有限tensorops；MatMul主计算掩盖transpose时间，只减WSS，Conv2D因重复/失去SIMD反慢。1byte fragments可能为64B缓存行触发64个DRAM完整burst，有效cacheline利用率不等物理带宽减少。Ch49:299–301 FILCO是片上memory/tile可编程视图，未明确memory-transaction层虚拟重排与consumer kernel联合验收的替代分支。拟2+2+2=6缺口深入、主owner Ch49，限地址视图/实际transaction/kernel成本；不外推GPU、LLM或生产SLO。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:12:31Z`，DataCite初始created `2026-04-16T01:49:43Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13319`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与root非作者写后通过。具体写入与反例限域见本日恢复笔记；root已核实际正文及相邻交接，未复现实验。

### [Orientation — 2604.13321v1](https://arxiv.org/html/2604.13321v1)

[exact-v1](https://arxiv.org/html/2604.13321v1) §3–5；固定 scene 的不同旋转用于训练/测试 ridge probe，不是未知 scene 泛化。feature substitution 的测量对象仍是线性方向 decoder，不能当作原 VLM 的因果干预；背景旋转也影响前景估计。Ch5“信息存在、可读与被使用”与 Ch23 的写入/读取分账已承载可采用结论，不将分布式 probe 可读性解释为唯一 MLLM 失败成因。2+1+2=5，标准已有覆盖 `MODEL-WHAT-NEURAL-NETWORKS-LEARN`；有限非作者处置已通过，见本节当前处置。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:12:45Z`，DataCite初始created `2026-04-16T01:49:46Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13321`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [Event Tensor — 2604.13327v1](https://arxiv.org/html/2604.13327v1)

实际官方HTML §2.1–2.4、§3.1–3.4、§4.1–4.5及Tables1–3。把event的wait-count/notify/wait提升为symbolic-shape IR tensor；MoE的topk决定哪些expert counter更新，exp_indptr决定ready时触发的GroupGEMM tiles。编译器lower为整数counter与静态per-SM queue或device push/pop，动态路径是global-memory centralized queue，不是无成本/无争用；static路径形状采样取下一个更大queue，数据依赖保守退化至共同E[0]，不能说static也完整保留动态精细依赖。必要证据的反向：Table3动态dense TP速度.82～.89，Table2单token动态.95；Qwen3-32B TP4端到端SGLang仍快，warmup35s另有离线107s编译，不把coldstart节省叫全生命周期无编译。作者8B200/NVLink/PyTorch2.8/CUDA13/driver580.82；Qwen3-32B/30B-A3B decode input512/output100、batch1～128，precision/concurrency/SLO未在采用段披露，不采用通用收益数字。实际Ch49 persistent executor拥有typed host ring和resource竞争，PERSEUS段有completion信号，但没有把symbolic event图编译为shape/data-dependent megakernel及static/dynamic选择这条分支。拟2+2+2=6 gap深入，最窄Ch49 persistent executor后两段；不写成所有动态图支持或内存可见性形式证明，该必要范围现已获非作者源与实际正文审查通过。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:13:40Z`，DataCite初始created `2026-04-16T01:49:55Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13327`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与非作者写后通过。已完成真实写入和root/apr02单篇非作者源→owner/写后；具体范围见[独立复核](../_sources/daily-20260416/V3_INDEPENDENT_FOUR_CALIBRATION.md)，不预支日Gate。

### [CONCORD — 2604.13348v1](https://arxiv.org/html/2604.13348v1)

[exact-v1](https://arxiv.org/html/2604.13348v1) §2.1–2.3、§3.1、§4.1。先 speaker verification 筛 owner 转录，再用 metadata/A2A 请求补全实体，relationship/sensitivity 判断控制披露；语言推断的关系不证明 consent 或 authenticated authorization。Ch72 PrivacyGate 已要求 recipient/purpose/data-subject/reference monitor 分账，具体支持这一边界。合成对话与 VoxConverse 前端不是一个真实隐私部署验证；§4.1 的 FPR .8%、TPR 99.2% 与 FNR 12% 缺同分母解释，不能合成统一安全率。2+1+2=5，安全深入后拟已有覆盖 `PLATFORM-SECURITY`，不采用 universal bystander privacy 保证，有限非作者处置已通过。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:15:41Z`，DataCite初始created `2026-04-16T01:50:26Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13348`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [OBF — 2604.13349v1](https://arxiv.org/html/2604.13349v1)

[exact-v1](https://arxiv.org/html/2604.13349v1) §4.3 Eq3–9、§5/Table1。硬淘汰 KV 后，以被删除 V 在保留 V span 之外的分量做 PCA/attention-demand 加权，并均匀 backfill 保留 V；K 不变。这是 eviction 后重建的一种有损补偿，不是 Ch82 接收方条件化 XKV translator。在 Ch82 latent relay 的 payload/eviction 段后已写窄分支，保留重建代价、rank8 及均匀分配可能改变 attention response。Qwen3-14B、40 latent steps、单 RTX PRO 6000 Blackwell/BF16/三 runs 的 Table1 并非所有任务提高，H/L 分支均有退步；不采用全9改善、exact information preservation 或跨模型通用承诺。2+2+2=6，知识缺口深入；必要源→owner采用核与apr01实际写后均通过。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:15:42Z`，DataCite初始created `2026-04-16T01:50:27Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13349`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置：整合 — AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md) `SF-2026-ARXIV-2604-13349` 两段已实际写入latent relay/XKV论证之后、Behavioral belief之前。root必要源→owner采用核与apr01本次实际正文/相邻衔接写后均通过，未复现实验；详见[八项有限独立核验](../_sources/daily-20260416/V3_APR01_BOUNDED_EIGHT_INDEPENDENT_AUDIT.md)。

### [PST — 2604.13356v1](https://arxiv.org/html/2604.13356v1)

[exact-v1](https://arxiv.org/html/2604.13356v1) §3/Algorithm1、§4、§5.2、§6。将排列末端模型 response 当 reference，经 PMI/sigmoid 权重缩放各模型自己的轨迹 CE；reference 并非独立真值，正权重仍可强化错误原答案。Algorithm1 含末端模型与文字的 non-final 表述有局部实现说明缺口。ODE 的能力-gap 收敛以单调 gap 驱动为假设，不能证明真实 CE 梯度满足；受限三模型算术/LoRA 十 runs 不改变部署 reference admission 的长期设计。2+1+2=5，标准仅报告，保留真实机制而不把成熟知识迁移话题当完全同义覆盖，有限非作者处置已通过。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:16:01Z`，DataCite初始created `2026-04-16T01:50:38Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13356`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [Diffusion dynamics — 2604.13366v1](https://arxiv.org/html/2604.13366v1)

实际[exact-v1](https://arxiv.org/html/2604.13366v1) II-C/II-E、III-A/B。inpainting joint input-observation 模型与只预测 future observations 的 FiLM-conditioned 模型在 full-chain 与 warm-start 截断下排序不同；D2、400步轨迹的320 context/80 prediction、作者约40ms预算对应5/100 denoising steps，CNN/inpainting受损较大，CDT在 OOD 较好但 ID 仍输 deterministic baseline。单 A100 被明确披露为训练环境，必要段没有给完整线上精度/并发/SLO，不把40ms预算当生产延迟合同。真实 MPC/机器人验证仍是未来工作，diffusion样本多峰不证明 uncertainty calibration。2+1+2=5，标准仅报告：保留deadline与conditioning形态交互的受限案例，但小型随机动力学试验还不足以替换Ch25真实 observation/controller与少步 rollout 验收链；没有新实机安全承诺或普遍生成方案推荐。有限非作者处置已通过。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:17:16Z`，DataCite初始created `2026-04-16T01:50:53Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13366`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [Linear Probe Accuracy — 2604.13386v1](https://arxiv.org/html/2604.13386v1)

[exact-v1](https://arxiv.org/html/2604.13386v1) §3.2–3.4、§4.4–4.5、§5。先用612对 contrastive prompts 训练单层 probes，随后按 double-fault 选择共同错误较少的层，二层混权、三/五层另训 stacking；ensemble 的80/20划分包含目标任务标签，不是完全零样本跨任务迁移。没有一套二层组合改善全部任务，已有强 detector 还会退步；方向余弦与 AUROC 差的相关性不证明真实意图因果，短上下文/角色扮演也不验收部署长上下文。Ch72 Learned Security Sensor 已写多关键层窗口/持续触发，却未分开“按单层最高分选层”与“按共同错误选组合”的校准分支，Ch66:1861 supervised ensemble 总则不承载这个选取条件。2+2+2=6，拟安全/知识缺口深入，主 owner Ch72，只补共同错误、目标标签/重新校准及固定单层回退，采用结果见本节当前处置。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:20:05Z`，DataCite初始created `2026-04-16T01:51:23Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13386`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；本次实际正文与root非作者写后通过。2026-09-27 root重开必要v1、实际段落及相邻交接完成独立复核；未复现实验，具体采用边界与写后记录见[v3恢复笔记](../_sources/daily-20260416/v3-reopen-notes.md)。

### [CoRAP — 2604.13395v1](https://arxiv.org/html/2604.13395v1)

[exact-v1](https://arxiv.org/html/2604.13395v1) §3.1–3.2 Eq1–7、§4/Tables1–3、Appendix B Theorem3.1–3.2。loss 是返回集合中存在被外部 V 接受且答案为gold的 trace，不是所有 traces 全正确。固定模型、finite grid、i.i.d.与独立 sampling 支持 LTT/FWER 的总体风险；Shapley 子集保证另明确要求删除 coalition 的误差由贡献和 ξ 界住，初看“任意Shapley无法保证”的疑虑在读到该假设后撤销，不能标无条件数学反例。实用 influence/unlearning 近似、分组预筛与未测 ξ 不自动继承精确重训 coalition 保证。两视觉 QA 数据、1500 calibration/100 test、8 trials、temperature1.2/top-p.85/Kmax16，不证明所有开放生成都可认证。2+1+2=5，标准仅报告：有条件的联合 trace/answer coverage 与归因区别值得保留，但缺实际可部署、可验 ξ 的全链，暂不修改 Ch66，不伪称已有完全相同算法。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:21:23Z`，DataCite初始created `2026-04-16T01:51:36Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13395`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [Multimodal ICL — 2604.13403v1](https://arxiv.org/html/2604.13403v1)

[exact-v1](https://arxiv.org/html/2604.13403v1) §4.1–4.2/Table2、§5.1–5.3 Eq1–3/Table3、Limitations。demo label 对 visual evidence 的注意力峰与 query 最后token的读取分开；MGI取平均熵最低中层的 label→image pattern，加入后层 query→demo image attention 并重归一。最低熵不证明 mapping 真正确，广泛 uniform image-attention 干预可破坏多条视觉路径，不能据此证明唯一失败原因。4-shot、Qwen2.5-VL7/32B和Gemma3 12/27B、三seeds、数值 exact/text keyword scorer 的增益小且有持平，超参有额外校准成本；不把效果写作根除 perception–reasoning 错位。Ch23 当前 fusion/对齐已分信息形成与消费，但缺 demonstration-grounding 与 query-time task application 的控制分支。2+2+2=6，拟缺口深入 Ch23，在 fusion/对齐交接窄补读取对象与有限干预，采用结果见本节当前处置。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:22:26Z`，DataCite初始created `2026-04-16T01:51:48Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13403`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；实际机制正文与root非作者写后通过。2026-09-27 root独立重开必要v1并顺读真实段及相邻论证，具体写入位置和代价/回退见[v3恢复笔记](../_sources/daily-20260416/v3-reopen-notes.md)；未复现实验。

### [Dataset-Level Metrics Attenuate Non-Determinism: A Fine-Grained Non-Determinism Evaluation in Diffusion Language Models — 2604.13413v1](https://arxiv.org/html/2604.13413v1)

实际官方HTML §3.2/§4/§5、Tables1–5、AppG，LLaDA/LLaDA1.5 8B、PIQA/WinoGrande/ARC与HumanEval/MBPP。Fig1按同input跨config的prediction flip，确有平均正确率相近而具体输出改变的受限证据；FVA Eq1–4是所选factor/settings的平方和诊断，不是所有因果来源。然而Tables2/3 caption明确sample Std/SE是“固定configuration跨不同samples”，§3.2采用命题却定义 `Var_c(z_i,c)`。反例：所有config对前半样本都对、后半都错，则跨config每题variance为0，但固定config跨样本Std=.5；不能把这些表的.4～.5直接说成每input instability幅度。保留这个局部测量口径问题，不扩大为所有具体flip无效。实际Ch66“平均值、切片与不确定性”及regression重复预算已有per-example/环境身份/重复证据，足以承载窄结论；6分，必要反证深入，Books倾向已有覆盖，FVA/表比值不正面采用。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:23:15Z`，DataCite初始created `2026-04-16T01:52:03Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13413`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [MaMe/MaRe — 2604.13432v1](https://arxiv.org/html/2604.13432v1)

[exact-v1](https://arxiv.org/html/2604.13432v1) §3.1 Eq2–10/Batch Processing、§3.2–3.4 Eq11–18、§4.1/Table2、§4.2/Table3、§4.5。similarity/column weights 以矩阵操作代排序/离散scatter，未关联 source 保留；batch 内任一样本需保留某source就全batch保留并撤掉对应融合列，因此可执行 shape 与压缩量受batch组合影响。存 W 后反向散布是近似重建，不是被合并信息的逆映射；Eq11–12 的索引/缩放文字不能承诺完全恢复。矩阵计算仍有 O(MNd) 与保存 W 的开销，§3.2简化概率面积不证明所有部署省时。A100/b64/FP32/ImageNet224与3090/FP32/CLIP224、SigLIP512为不同合同；VideoMAE-B也只有很小吞吐收益，SLO未披露。Ch23 feature-merge主线有层/质量取舍，却缺batch统一保留形状与恢复payload状态分支。2+2+2=6，拟缺口深入 Ch23，限执行/表示交接，不用“inverse”宣称信息无损，采用结果见本节当前处置。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:24:25Z`，DataCite初始created `2026-04-16T01:52:32Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13432`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；实际机制正文与root非作者写后通过。2026-09-27 root独立重开必要v1并顺读真实段及相邻论证，具体写入位置和代价/回退见[v3恢复笔记](../_sources/daily-20260416/v3-reopen-notes.md)；未复现实验。

### [WIN-U — 2604.13438v1](https://arxiv.org/html/2604.13438v1)

[exact-v1](https://arxiv.org/html/2604.13438v1) §3.2–3.3 Eq12–16/Algorithm1、§4.1–4.2、§5.1–5.3/Table2、Appendix A.6/C.1必要配置。删样本后用 H−Hf 而不是原 H 的局部 Newton 方向，Woodbury减少反演维度；请求阶段只访问 forget set，仍需要预先聚合全训练曲率，不是从未使用 retain 信息。实际LLM用微调数据 diagonal GGN inverse+LoRA+MC pseudo-labels，并非原完整 Hessian；λI被作为PD前提，不能写任意非凸Hessian自动PD。线性二次损失精确解不升级为非凸从头重训等价，作者明确local warm-start。单H100NVL96GB/TOFU1.2B/r8的forget10前后QA .226→.592、utility .420→.587及411s，不支持不可重学或全任务更快。Ch72遗忘验收已有retraining/attack reference，却未说明 retain-free request 与离线 retained statistics 的分账。2+2+2=6，拟安全/知识缺口深入 Ch72，以预计算曲率生命周期、近似局部目标与完整重训回退为唯一增量，采用结果见本节当前处置。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:25:24Z`，DataCite初始created `2026-04-16T01:52:40Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13438`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；本次实际正文与root非作者写后通过。2026-09-27 root重开必要v1、实际段落及相邻交接完成独立复核；未复现实验，具体采用边界与写后记录见[v3恢复笔记](../_sources/daily-20260416/v3-reopen-notes.md)。

### [KL quantization — 2604.13440v1](https://arxiv.org/html/2604.13440v1)

[exact-v1](https://arxiv.org/html/2604.13440v1) §3/Algorithm1、§4.1 Eq1–6、§5.2/§6.1 Tables2–3、§7.1–7.3/Table4。单层量化 forward 比较输出分布，再以敏感性选较高位宽；raw-logit SQNR不直接等价行为保持。teacher→student KL 的PPL恒等式以teacher law为分布，不能将teacher softmax与真实test law静默互换；Table2反向KL经验排序较高，不能拿正向理论等式证明反向经验保证，文字SQNR平均值也与表有出入。Intel Lunar Lake/OpenVINO latency mode100迭代的Mamba130M/1.4B CPU和Mamba2-130M GPU配置不同，QDQ/部分高精度算子并不统一内存或真实低bit执行收益；请求长度/并发/SLO未披露。Ch49量化段有冻结output、补偿与发布Gate，但缺输出概率与raw-logit距离的量化层预算选择分支。2+2+2=6，拟缺口深入 Ch49（不是Ch39），保方向/评价分布和实际runtime验收，采用结果见本节当前处置。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:25:35Z`，DataCite初始created `2026-04-16T01:52:44Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13440`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与root非作者写后通过。具体写入与反例限域见本日恢复笔记；root已核实际正文及相邻交接，未复现实验。

### [Gaussian-mixture reverse kernels — 2604.13470v1](https://arxiv.org/html/2604.13470v1)

[exact-v1](https://arxiv.org/html/2604.13470v1) §2的path-KL拆分、§3 Assumptions3.1/3.4/3.13与Theorem3.17、§4 Proposition4.1/Theorem4.2/Remark4.3必要证明。fixed Gaussian components 的feature-conditioned mixture weights以ReLU logits逼近reverse conditional law；feature sufficiency、正性/连续性/矩及log-odds regularity是前提，不由训练流程保证。拆分保留 terminal mismatch、有限mixture误差与neural logit误差；exact terminal matching才得到零KL逼近的存在性。terminal项是这条路径的误差上界项，不能凭上界平台期推所有架构输出都具有严格正误差下界。响应空间D的维数灾难没有由低维feature自动消除。Ch24现diffusion/DDPM/离散多峰分支尚未分reverse-kernel表达力、feature缺失与terminal mismatch的条件误差合同。2+2+2=6，拟缺口深入 Ch24，只补存在性与学得/优化/少步runtime三者区别，不宣称训练必可找到或推理普遍更快，采用结果见本节当前处置。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:27:22Z`，DataCite初始created `2026-04-16T01:53:56Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13470`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；实际正文与root非作者写后通过。本次root实际顺读四条正文与相邻主线、复用有效必要v1通过，未复现实验，不预支日级Gate。

### [FiMR — 2604.13491v1](https://arxiv.org/html/2604.13491v1)

[官方 PDF v1](https://arxiv.org/pdf/2604.13491v1) 首页、§3.2/Table2、§4、§6.2/Table5、Appendix A.3；HTML 必要段与 PDF 一致。库存“FiRe/GRPO”不符合正文：实际是分解VQA→显式反馈→局部修改的SFT，不继承那个方法。扰动368/2212个内部判No的rationales，第二轮整体.82与未扰动.82相近，不能由此证明每例完全不用反馈；FiMR显式/隐式反馈第三轮.86/.85、颜色属性.76/.77，亦非全面改善。GenEval detector/CLIP proxy不是视觉真值。Ch24现多路径分歧/局部remask和Ch66 trace fidelity还未把regeneration trigger与feedback语义消费者分开；2+2+2=6，拟缺口深入 Ch24，只补反馈干预→真实修改的验收，保留全图重生与额外judge/edit成本，不写所有自反思无效。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:29:06Z`，DataCite初始created `2026-04-16T01:54:28Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13491`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；实际正文与root非作者写后通过。本次root实际顺读四条正文与相邻主线、复用有效必要v1通过，未复现实验，不预支日级Gate。

### [Cluster-aware Upcycling — 2604.13508v1](https://arxiv.org/html/2604.13508v1)

[exact-v1](https://arxiv.org/html/2604.13508v1) §3.1–3.4 Eq7–13、§4.1/4.4。dense activation spherical k-means、cluster covariance下第一FFN线性层的truncated SVD、centroid router，再用dense EMA expert mixture监督top-k；实际不是求解Eq7，也不是全非线性FFN保持等价。克隆/随机router保原初始化更直接，cluster-specific近似引入校准域、秩与额外teacher成本；低entropy不证明routing正确。CLIP B/16、B/32、8expert/top2/64H200/1.3B额外seen samples，EESD单独非稳定改善。Ch21:668独立领域experts+ridge router不同，缺同base activation分区初始化的分支。2+2+2=6，拟缺口深入 Ch21，不采用通用function-preserving或规模收益保证。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:29:58Z`，DataCite初始created `2026-04-16T01:54:54Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13508`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)；同base activation初始化的两段实际写入，root必要来源/真实owner及正文相邻交接写后独立通过，未复现实验，未日Gate。

### [RTR-DiT — 2604.13509v1](https://arxiv.org/html/2604.13509v1)

[exact-v1](https://arxiv.org/html/2604.13509v1) §3.4、§4.1/4.3–4.4/Table2。rolling cache满后pin reference；prompt/reference切换时cross-attention重新初始化，3D history仅保上一frame，新reference重新pin。缓存包含不同条件责任，保留上一帧是过渡设计而非新条件下exact prefix；长期漂移/quality不保证。50段5s、832×640/24fps、单H20（商业模型不同环境）、两denoise steps；reference pin和换风格仅qualitative，Table2 CLIP-F多项反向。Ch45 head-aware retention/identity已有总则，未分reference anchor与条件切换的不同invalidate scope。2+2+2=6，拟缺口深入 Ch45，限scope/history过渡，精度/并发/SLO未披露，不录无条件realtime收益。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:29:59Z`，DataCite初始created `2026-04-16T01:54:55Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13509`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — reference/cross-attention/上一帧刷新是具体streaming策略，已有identity/invalidation/pin合同承载边界；不证明新条件exact状态或无界实时质量。root本轮已实际重开必要exact-v1并对读对应正文与相邻主线，独立裁决通过，未复现实验；保留本文局部机制/反证，不把主题相似写成精确算法已覆盖。

### [SFT–GRPO overlap — 2604.13515v1](https://arxiv.org/html/2604.13515v1)

[exact-v1](https://arxiv.org/html/2604.13515v1) §3.4–3.5、§4–6/Table3。同SFT checkpoint、约16K RL prompts/同超参控制0/30/100%与20K SFT pool重叠；同source配比却未正式验证难度一致。answer injection把待求数值加到问题，formalization translation与独立求解不可混算；compile与semantic judge分账。Qwen3-8B/no-thinking/n8与H200受测，0%优于100%而30%训练reward最高，不证明所有RL必须用新题。Ch33 SFT→RL与offline rollout reuse未明确跨阶段prompt交集这个选择对象。2+2+2=6，拟缺口深入 Ch33，保checkpoint×pool交集及held-out对照，少量同题纠错仍共存。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:30:16Z`，DataCite初始created `2026-04-16T01:55:04Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13515`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 阶段prompt交集实验值得保留，但难度未匹配/answer injection改任务，0/30/100排序不支持稳定overlap策略。root本轮已实际重开必要exact-v1并对读对应正文与相邻主线，独立裁决通过，未复现实验；保留本文局部机制/反证，不把主题相似写成精确算法已覆盖。

### [ToolSpec — 2604.13519v1](https://arxiv.org/html/2604.13519v1)

实际HTML §4.1–4.3、§5/§6.1；FSM按toolname/parametername/parametervalue/ordinarytext转换，前两类schema draft；free value用TR和历史successful toolcall的hidden cosine top3+suffix5/6/7 proposal，再target speculative sampling验证。结构合法不是业务/权限正确，retrieval不能直接commit。batch1，Qwen2.5/Llama/API-Bank/ToolAlpaca/BFCLv2/ToolBench受测；Eagle训练required/OOD不是公平通用winner。实际Ch48 semanticretrieval与Agent block hint段解释proposalauthority/检索代价，却未完整解释schema状态分责，拟2+2+2=6知识缺口深入、Ch48最窄分支。AppB.2的实际设置已由apr02独立核为2×A100-PCIE40GB、batch1、torch2.5.1/CUDA12.4、fp16；保留质量差异，不采用无条件3.5～4.2x或把实验全面证明数学exactness。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:30:26Z`，DataCite初始created `2026-04-16T01:55:10Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13519`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；实际正文与非作者写后通过。已完成真实写入和root/apr02单篇非作者源→owner/写后；具体范围见[独立复核](../_sources/daily-20260416/V3_INDEPENDENT_FOUR_CALIBRATION.md)，不预支日Gate。

### [ATLAAS — 2604.13523v1](https://arxiv.org/html/2604.13523v1)

实际HTML §3.1–3.3、§4.1–4.5/Table2/Table4。RTL ASV→MLIR八pass→TAIDL硬件primitive/宏控制、非匹配退opaque确有可检查的替代设计，Gemmini/VTA验证和Spike受限结果可报告。但§3.2 PhaseB与Table2 B5把 `ext(trunci(x))` 叫saturation/clamp；官方MLIR [arith.trunci](https://mlir.llvm.org/docs/Dialects/ArithOps/#arithtrunci-arithtrunciop)丢高位、[arith.extsi](https://mlir.llvm.org/docs/Dialects/ArithOps/#arithextsi-arithextsiop)复制signbit，不能仅由这两操作推出clamp。8bit反例：128截断后signextend=-128，而clamp到[-128,127]=127；256回绕0而clamp=127。overflow flag也只产生poison并非饱和。§4.3/Table4 PE证明写 `sext(a*b+trunc(c))`，并没有给B5泛化clamp所缺的范围前提/完整比较选择编码；不会据此否定bit-exact PE或DMA有限证明，也不把Stage3可选clamp说成全pass已证明。拟2+2+2=6，核心语义反证深入、争议/暂缓Books；重开只需精确B5完整pattern及输入域/等价证明或作者勘误，非要求全仓库/全部附件。

日期依据：自身原始v1 metadata Updated 2026-04-16T00:30:47Z、DataCite初始created 2026-04-16T01:55:16Z与官方ID公告分配、连续/OAI批界、常规公告slot联合支持08～09有据推断，不是两字段直接等同首公开。家族 SF-2026-ARXIV-2604-13523；2 + 2 + 2 = 6，具体算子反证深入，root必要反证已核。

当前处置：争议／暂缓，只隔离Table2 B5饱和泛化保证；需要精确转换实现/勘误解释。有限bit证明与实验不全部否定，未写Books。

### [RiskWebWorld — 2604.13531v1](https://arxiv.org/html/2604.13531v1)

[exact-v1](https://arxiv.org/html/2604.13531v1) §4.1–4.2、§5.1–5.3/Table3。原先安全 benchmark 的共同关闭不够精确：同Qwen3-VL-30B来源的BU-30B在详细/简短prompt下32.4→15.9，而base30B为24.2→21.8；这个prompt×专门化checkpoint交互值得保留，不把‘GUI专门化优于通用’作无条件判断。1,513任务中443 Challenge是从有SOP的Standard任务去掉SOP而来，不是额外独立原始任务；hijackments是CAPTCHA、popup和页面变化，不是已验证prompt injection。2+1+2=5标准仅报告受限的harness/prompt敏感性，Ch66模型与harness共同身份已有一般合同，但不假称已有同一受控证据，也不采用scale是唯一原因的headline。恢复这一家族，不再扩全部安全benchmark。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:31:16Z`，DataCite初始created `2026-04-16T01:55:28Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13531`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [YoloFS — 2604.13536v1](https://arxiv.org/html/2604.13536v1)

[exact-v1](https://arxiv.org/html/2604.13536v1) §4.1–4.5、§5.1–5.2。Linux stacking在真正路径访问点调权限，变更先进入flat content store+path override tree+journal；travel保留dead分支而不抹除错误证据，user另行commit。读取已泄漏不可回滚，permission仍需effect前；journal/内核挂载域也不覆盖网络/进程所有effect。Claude Code2.1.45/Sonnet4.6、11个10–41LoC隐藏副作用任务，8自纠正/3用户可拒绝，不代表生产风险消失；290public reports无发生率分母。Ch78:537现preventive/evidential gate及Ch81:559受控snapshot边界没有physical mutation staging与non-destructive audit lineage。2+2+2=6，拟安全/缺口深入主owner Ch78，最窄分支不重复一般沙箱宣言。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:31:31Z`，DataCite初始created `2026-04-16T01:55:36Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13536`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md) `SF-2026-ARXIV-2604-13536` 两段已实际写入effect gate链、Typed proof之前。root必要源→owner采用核与apr01本次实际正文/相邻衔接写后均通过，未复现实验；详见[八项有限独立核验](../_sources/daily-20260416/V3_APR01_BOUNDED_EIGHT_INDEPENDENT_AUDIT.md)。

### [CoDIT — 2604.13538v1](https://arxiv.org/html/2604.13538v1)

[exact-v1](https://arxiv.org/html/2604.13538v1) §2.1–2.2 Eq1–6、§3.1/Table1、Appendix C.1。post/pre token log-ratio在post plausibility集合选response，再训练可不同架构student；原式无独立β系数。Taylor只近似，不证明移除全部世界知识或纯instruction能力。250333相同instructions、三个teacher×三个student、LLMjudge；MTBench被用于α选择不能同时当独立held-out，部分LC/MTBench反向，额外base forward要计生成成本。Ch29当前capability投影/temperature target未包含post/base output contrast的corpus构造对象。2+2+2=6，拟缺口深入 Ch29，普通teacher采样与独立validator仍共存。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:31:52Z`，DataCite初始created `2026-04-16T01:55:39Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13538`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 同prefix双教师logprob差构造监督是真实替代配方，但Taylor局部/调测同用及退步不足支持instruction-only或长期新责任。root本轮已实际重开必要exact-v1并对读对应正文与相邻主线，独立裁决通过，未复现实验；保留本文局部机制/反证，不把主题相似写成精确算法已覆盖。

### [UniRect — 2604.13540v1](https://arxiv.org/html/2604.13540v1)

[官方 PDF v1](https://arxiv.org/pdf/2604.13540v1) §4.2–4.3 Eq6–12、§5.1/5.4与HTML一致。理解分支生成c_ideal，CLIP embedding loss通过look-ahead/decoder回传latent，不是“模型prompt loglikelihood”；候选selection另用原用户prompt的CLIP score，仍无独立事实真值。Jacobian链乘不是自动正交投影/流形保证。50步、窗口5–10/每步3次、H800；K5反退且Omni counting/BAGEL position反向，不叫free lunch。Ch24:936 IABEdit是训练期anchor，不是推理期proposal/selection分责。2+2+2=6，拟缺口深入 Ch24，只补双目标与额外搜索梯度代价，保普通sampler回退。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:32:01Z`，DataCite初始created `2026-04-16T01:55:42Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13540`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；实际正文与root非作者写后通过。本次root实际顺读四条正文与相邻主线、复用有效必要v1通过，未复现实验，不预支日级Gate。

### [DynamicGate concurrency — 2604.13546v1](https://arxiv.org/html/2604.13546v1)

[exact-v1](https://arxiv.org/html/2604.13546v1) §3、§5.3–5.7 Eq6–15、§6.2/Table1。Prop1明确先算output再更新，Prop2写active-W更新却以inactive-W不贡献作为理由；§5.7复制/periodic snapshot适用于dense也适用。时间索引dense f(x;W_t)本身定义明确，混合版本读才是问题；两层读旧w1/新w2可无对应已提交snapshot，稀疏或gate-only不自动原子化。这个反例只否定“结构天然保证真正并发”的广主张，不否定先forward后update或固定snapshot条件式。soft mask非零也不能按m=1集合当完整active范围。Dense在实验全部SKIP，无同等snapshot adaptation对照。2+1+2=5，核心保证反证深入，拟窄争议/暂缓Books；不因稀疏无收益而拒绝所有受限adaptation。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:32:13Z`，DataCite初始created `2026-04-16T01:55:51Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13546`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：暂缓 — 中心保证的精确争议与重开条件见§4/§5，不入Books。争议只隔离上文缺失条件/公式保证；重开需精确修正或实现解释，apr20必要源/有效反证独立终核通过，采用保证精确隔离。

### [YOCO++ — 2604.13556v1](https://arxiv.org/html/2604.13556v1)

实际HTML §3–4/Table1–2；bottom-half标准Transformer先把自身KV与底层KV加权混合、缓存combined KV，中间层的混合cache给tophalf复用；不是在Decode给每层读取多份历史KV，也不是可无训练应用既有checkpoint。初始化保持YOCO，lambda35助参数学习；无scale/无key residual退步。1.1B22层/32Q4KV、100B SlimPajama从零训练、32H80080G/512Ktoken批；H20 96G测prefill/maxthroughput不同batch，不能称同并发SLO吞吐不变。Ch45现有跨层共享/feature残差主要training-free重构/selector，缺这个训练架构与cache物化顺序的替代分支；拟2+2+2=6知识缺口深入，正文不采用通用50%prefill收益或lambda最优。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:32:41Z`，DataCite初始created `2026-04-16T01:56:06Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13556`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；实际正文与非作者写后通过。已完成真实写入和root/apr02单篇非作者源→owner/写后；具体范围见[独立复核](../_sources/daily-20260416/V3_INDEPENDENT_FOUR_CALIBRATION.md)，不预支日Gate。

### [MM-Doc-R1/SPO — 2604.13579v1](https://arxiv.org/html/2604.13579v1)

[exact-v1](https://arxiv.org/html/2604.13579v1) §3.2.2 Eq4–5、§4/Table1、Appendix A.4。用冻结BGE-M3的整条trajectory cosine归一权重替代均值baseline；这不是逐中间state的conditional-value估计，权重依赖当前trajectory也不能直接推出无偏policy gradient，cosine式未披露负值/零分母处理。MMLongBench-Doc1082题、Qwen3-4B/8B+VL7B，8B准确率44.7→49.7是受限实验；SPO agent154.44s比未训109.32s更慢，并非免费探索。Ch33实际“Hierarchy of Groups”已要求state/context条件与不能以语义相似冒充同分布；论文的整轨迹权重没有提供可采用的更强条件保证。2+1+2=5标准完成，拟仅报告该受限设计，保普通GRPO/显式state分组，不按DocVQA领域直接排除。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:34:25Z`，DataCite初始created `2026-04-16T01:56:41Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13579`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [C2 — 2604.13618v1](https://arxiv.org/html/2604.13618v1)

[exact-v1](https://arxiv.org/html/2604.13618v1) §4.1–4.4、§5.1–5.2/Table1–2。偏好gold label下比较有/无rubric的log margin，筛能翻对且增margin的helpful与相反misleading，再DPO训generator、GRPO训verifier的rubric assessment；运行时拒绝后另作rubric-free查询。它仍依赖binary preference，不是label-free真值判断；5K原题扩14K训练实例，3seeds/两8B模型/4评测，追加数据与合成、回退查询均计成本。Ch31现versioned Reward DAG/外部promotion只覆盖更新权，未说明同一judge把rubric当可拒绝输入并以无rubric路径作回退。2+2+2=6缺口深入，拟Ch31最窄rubric admission分支；不把higher gold-margin当所有真实偏好或事实正确。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:36:51Z`，DataCite初始created `2026-04-16T01:57:39Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13618`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 同偏好label生成rubric与拒绝后双查询是受限抗误导实现，不产生独立truth；既有judge共有盲点与外部promotion主线无需扩成新算法authority。root本轮已实际重开必要exact-v1并对读对应正文与相邻主线，独立裁决通过，未复现实验；保留本文局部机制/反证，不把主题相似写成精确算法已覆盖。

### [(How) Learning Rates Regulate Catastrophic Overtraining — 2604.13627v1](https://arxiv.org/html/2604.13627v1)

实际HTML §3–5/Limitations；四1B模型HH-SFT constant-warmup、相同loss下LR更高→MPA drift/OOD下降；2layer diagonal toy支持机制直觉，不证明loss一样就参数距离一样。预训五checkpoint系列的sharpness采用Gaussian parameter扰动后output KL proxy，14M对照只是proxy核验；SmolLM3B/Apertus8B WSD cooldown同期变化。Limitations明言decay→sharpness链只有correlation，需要modifiedannealing重训才可claimcausality，故不采用标题caused或普遍取消decay建议。实际Ch28 schedule/分组LR、Ch29同loss/forgetting段未分出base cooldown checkpoint与SFT update尺度的不同风险；拟3+2+2=7 Deep，窄Ch28 schedule→Ch29交接，保留一般decay/SFT低LR和held-out验收。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:37:43Z`，DataCite初始created `2026-04-16T01:57:52Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13627`；评分 3 + 2 + 2 = 7。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)；实际正文与非作者写后通过。已完成真实写入和root/apr02单篇非作者源→owner/写后；具体范围见[独立复核](../_sources/daily-20260416/V3_INDEPENDENT_FOUR_CALIBRATION.md)，不预支日Gate。

### [CSD — 2604.13634v1](https://arxiv.org/html/2604.13634v1)

[exact-v1](https://arxiv.org/html/2604.13634v1) Algorithm1/§4.3及Limitations已明确heuristic acceptance偏离target distribution，旧审阅遗漏此披露，故撤销将exactness作为永久争议的判断。OCM记发散对，SCG按频率/target-logit门槛恢复被拒draft；p=(.6,.4)、q=(.4,.6)、τ=.6且频门通过时b输出.6而非.4，只说明这条有损分支，不反驳其已披露合同。§5.1/主表采用Llama-70B/1B、Qwen72B/7B、singlebatch、2H20载target、greedy T=0；精度/长度/并发SLO未完整披露。离线校准、组件单独退步及尚无vLLM/高并发OCM同步验收均保留。2+2+2=6，深入消歧后仅报告受限经验，不把任务accuracy称distribution identity，不把配方完整判Existing或强写Books。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:38:04Z`，DataCite初始created `2026-04-16T01:58:02Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13634`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 撤销遗漏作者lossy披露造成的旧争议；保留具体机制/经验/成本边界，不请求已经公开的lossy说明。Apr20非作者提出遗漏，作者实际重开上述局部确认；具名非作者记录随日级汇总，不预支日Gate。

### [Sim-and-Real Co-Training — 2604.13645v1](https://arxiv.org/html/2604.13645v1)

[exact-v1](https://arxiv.org/html/2604.13645v1) §2.1 Eq1–3、§3、§4.2/§5.1–5.2/Table2。共享latent可转移，却不能在两域相同观察对应不同action时把domain信息抹除；作者用domain one-hot条件与ADDA对齐其余表示，mix ratio同时改变经验权重与表示，不只重加权。受控toy人工移动manifold；ResNet18+Transformer diffusion、三操作任务，sim每checkpoint200trials/real30trials；实机只测balanced regime，OT/ADDA平均14.3/30低于普通cotrain15.3/30，组合21/30不是普遍20点增益。Ch26多来源数据只写sim gap与action-schema对齐，缺“对齐但保留domain可辨性”这个相反压力。2+2+2=6缺口深入，拟Ch26数据演进段两段；不把相关性/作者kernel最优解当所有VLA因果机制，保real-only与普通mixture。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:38:42Z`，DataCite初始created `2026-04-16T01:58:19Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13645`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；实际窄正文及相邻衔接经root非作者写后通过，见[五项实际写后](../_sources/daily-20260416/V3_ROOT_FIVE_ACTUAL_WRITE_AFTER.md)。未复现实验，不代表日级Gate。

### [OLS Transformer — 2604.13656v1](https://arxiv.org/html/2604.13656v1)

[exact-v1](https://arxiv.org/html/2604.13656v1) §2.1–2.3 Eq2–8。full-column-rank X下WQ=WK=WV=L由当前X协方差求得，head P=LᵀXᵀY/n还依赖待拟合Y。代数存在式成立，但∀X,Y∃weights不等于∃fixed weights∀X,Y的一次forward solver；n500/一维scalar L实验也把P按当前X,Y算入，不能证明未见回归无需计算逆矩阵或预处理。无softmax/normalization线性attention不能代表标准Transformer“本质”。2+1+2=5，headline解释范围反证深入后拟仅报告这个conditional construction，不否定原定理存在式、不写普适OLS能力或伪称已构成Books新的求解机制。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:39:12Z`，DataCite初始created `2026-04-16T01:58:35Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13656`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [Weight Patching — 2604.13694v1](https://arxiv.org/html/2604.13694v1)

[exact-v1](https://arxiv.org/html/2604.13694v1) §III-A–E Eq7–16、IV-C–F、V Scope。同架构base/SFT、固定输入，参数slice移植与跨模型activation移植都用同anchor；前者测posttrain差分是否足以恢复，后者只测传递/聚合位置，不能把必要relay当写入source。head换Q/O、MLP完整gate/up/down；梯度近似用于筛选，必要的top部分再actual replacement。6IFEval任务/3模型scale、English-Capital细案例，carrier相对checkpoint差分与粒度，不是不可分最终起源；merge表多个任务仍退步。Ch5已有decodable/use与probe/intervention阶梯，却未拆activation relay必要性与parameter-difference sufficiency。2+2+2=6缺口深入，拟Ch5证据阶梯后最窄分支；不写唯一知识槽或attention从不储存。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:41:09Z`，DataCite初始created `2026-04-16T01:59:31Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13694`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；本次实际正文与root非作者写后通过。2026-09-27 root重开必要v1、实际段落及相邻交接完成独立复核；未复现实验，具体采用边界与写后记录见[v3恢复笔记](../_sources/daily-20260416/v3-reopen-notes.md)。

### [Co-FactChecker — 2604.13706v1](https://arxiv.org/html/2604.13706v1)

[exact-v1](https://arxiv.org/html/2604.13706v1) §3.2 trace-edit/continuation、§6.3/§7。expert反馈译成remove/modify/guide，旧verdict及end-of-thinking被抑制，再以edited prefix续生成，而非append整个旧对话。可见trace是可编辑control artifact，非原始因果心智；oracle自动评测可看GT与rubric，真人仅2专家+3研究者、14claims/3轮，误译反馈会使后续难恢复、检索不足仍错。理论§4以MI/Bayes-risk单调作假设，many-to-one本身不推出reachable-set严格包含，故不采用普适严格优越。Ch75现derived context可隐藏/重读，但未明确可修改推理prefix、旧结论抑制与源证据保留的职责。2+2+2=6缺口深入，拟Ch75共享scratchpad最窄分支，保append-only/原文恢复及额外editor/replay成本。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:41:36Z`，DataCite初始created `2026-04-16T01:59:49Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13706`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)；实际窄正文及相邻衔接经root非作者写后通过，见[五项实际写后](../_sources/daily-20260416/V3_ROOT_FIVE_ACTUAL_WRITE_AFTER.md)。未复现实验，不代表日级Gate。

### [TimePro-RL — 2604.13715v1](https://arxiv.org/html/2604.13715v1)

[exact-v1](https://arxiv.org/html/2604.13715v1) §2.1–2.2、§3.2/§4.2/Table3。在音频特征之间插入显式物理时间token，数值字符串subtoken均值初始化且冻结，并经SFT适配；不是仅保存timestamp metadata或依赖RoPE。随机初始化使多数指标退步，正确初始化也不等于所有输入时间范围可迁移：750tokens只覆盖0–30s/25Hz，插入额外token有序列成本。GRPO的主奖励乘辅助项在主奖励全零时仍全零，不采用“解决所有advantage degeneration”。Qwen2/2.5音频7B、LoRA r8、3SFTepochs+10200samples/1RLepoch/group4，AG/SED/DAC受限指标而非真实交互时延。Ch23:425时间/provenance已有记录总则，尚缺物理坐标对模型可读性与初始化的输入接口分支。2+2+2=6拟缺口深入Ch23，保普通位置编码和显式输出监督。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:42:27Z`，DataCite初始created `2026-04-16T02:00:03Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13715`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；必要原文/实际owner与本次真实两段正文及相邻衔接由root非作者复核通过，具体位置见本日恢复笔记，未复现实验，未日Gate。

### [Repository Compression — 2604.13725v1](https://arxiv.org/html/2604.13725v1)

[exact-v1](https://arxiv.org/html/2604.13725v1) §3、§4.3–4.5/Table1。T2V经过StarCoderData及目标ComplexCodeEval两阶段训练，T2T默认training-free，T2I用QwenVL而其他用QwenCoder，故不是同模型/同训练预算的纯representation因果比较。single A10080G、bf16训练、greedy；quality经vLLM而效率切换nativeHF，BLEU/Edit/EM不能推出代码执行正确或完全无损，generation的图像路线也比full text弱。2+1+2=5标准仅报告这个task-conditioned可行性/代价case，不以28.3% BLEU判消除噪声、不取全局固定压缩倍率；Ch75任务相对充分性和总时延break-even能承载一般合同但不假称同算法覆盖。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:43:05Z`，DataCite初始created `2026-04-16T02:00:18Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13725`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [VLAJS — 2604.13733v1](https://arxiv.org/html/2604.13733v1)

[exact-v1](https://arxiv.org/html/2604.13733v1) III-B–III-E、IV、VI/TableII。训练时稀疏VLA delta经插值形成短窗方向正则，不直接执行teacher动作；reward趋势递减查询与正则，最终移除，运行时仅state-based PPO。direction loss不约束gripper，near-zero teacher跳过；文中mean reward>3与Alg中delta>3不统一，不采用通用阈值。Ch26训练期geometry teacher与运行时slow/fast分层不能替代这条transient action prior路线。PickPlace-v1/LiftPeg-v1等PPO亦可反胜；实机三个任务各20trials，不宣称全面超teacher/物理安全。2+2+2=6，apr01必要源→owner核验与root实际正文/相邻写后均通过，保persistent辅助与普通PPO。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:43:58Z`，DataCite初始created `2026-04-16T02:00:31Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13733`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)相应机制正文已实际写入；apr01必要源→实际owner核验通过，root非作者实际正文与相邻衔接复核通过。详见[五项写后核验](../_sources/daily-20260416/V3_ROOT_FIVE_ACTUAL_WRITE_AFTER.md)；未复现实验，不代替日级Gate。

### [OffloadFS — 2604.13743v1](https://arxiv.org/html/2604.13743v1)

[exact-v1](https://arxiv.org/html/2604.13743v1) §III/III-A–C、V、VI-B2/VI-C。initiator独占inode/extents，先分配再授权具体blocks并在远程task结束前禁止冲突访问；target只运行有限读写，truncate/directory等元数据操作不下放。免DLM是收窄并发合同，不是多writer通用FS；application决定cache bypass或粗mtime检查。过载拒绝后本地执行、token-expiry公平性另有调参成本。ML预处理读密集受限实验中peer compute优于storage，不能由near-data名字推出总是更快。Ch27数据lineage/Streaming尚缺预处理compute placement与block/cache ownership耦合的执行分支。2+2+2=6拟缺口深入Ch27，不把它当LLM算子或通用一致性证明。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:44:30Z`，DataCite初始created `2026-04-16T02:00:47Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13743`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限inode/block并发与peer预处理是具体工程分支，尚未改变样本lineage/worker曝光与恢复主线；不把读密集实例外推通用近数据最优。root本轮已实际重开必要exact-v1并对读对应正文与相邻主线，独立裁决通过，未复现实验；保留本文局部机制/反证，不把主题相似写成精确算法已覆盖。

### [Cognitive Companion — 2604.13759v1](https://arxiv.org/html/2604.13759v1)

[exact-v1](https://arxiv.org/html/2604.13759v1) §1.2、§4.2–4.4、§5/§6。仅35个proxy-labelled probe samples，检测AUROC与实际guidance收益是不同对象；output_hidden_states/窗口池化不等零显存/零walltime，小模型干预触发却无quality proxy改善，structured task可反向。主要Gemma4E4B/两初始sessions与后续六任务、self-referential judge，不能读成统一3B尺度阈值。可采用结论是sensor可靠性与intervention/task效用必须分账，Ch66 FailureDirection/internal→steering→deployment及Ch72监控非authority已实际承载。2+1+2=5，保证/安全signal深入后拟已有覆盖；不全盘否定受限feasibility，不写新通用并行monitor。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:45:18Z`，DataCite初始created `2026-04-16T02:01:12Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13759`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [RealVuln — 2604.13764v1](https://arxiv.org/html/2604.13764v1)

[exact-v1](https://arxiv.org/html/2604.13764v1) §3.3–3.4、§4.1–4.2、§5.1/§6.1。26教育/CTF Python仓库/796labels，strict_micro把未输出仓库计FN，micro却剔除；beta改变名次，API/agentic预算与覆盖范围须绑定。安全专门化两系统分别73和8.4(F3)，不能采用整个安全架构tier都胜通用/规则的headline；Kolega内部proprietary也不能归因模块。受限同corpus/sameprompt对照仍有价值，但不证明production漏洞发生率或固定F3最优。2+1+2=5，安全/评价反证深入后拟仅报告；不以没有新Book为准入排除，不将教育集的排名当真实漏洞扫描采购建议。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:45:29Z`，DataCite初始created `2026-04-16T02:01:19Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13764`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [MAGE — 2604.13777v1](https://arxiv.org/html/2604.13777v1)

[exact-v1](https://arxiv.org/html/2604.13777v1) §4.1–4.2、§5/§6.3。从anchor反复elicitation形成mention频率图，再按路径合成forget与不含anchor的neighbor QA，答案span更新；corpus-free不等于correctness-free证明，Table1明确无独立正确性检查。高benchmark覆盖/幻觉混入后部分指标稳定，不能证明图与真实训练记忆相同；TOFU稀疏实体与邻居替换退步、图构造查询成本保留。Ch72 concept-wide目标与S_full不可枚举边界已承载核心验收，具体自提取图是有用受限监督路线但缺独立coverage/授权范围，2+1+2=5标准仅报告，不假称已有同一算法，不把拒答当擦除。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:46:09Z`，DataCite初始created `2026-04-16T02:01:39Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13777`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [QuantileMark — 2604.13786v1](https://arxiv.org/html/2604.13786v1)

[exact-v1](https://arxiv.org/html/2604.13786v1) §3.2–3.4、§4.1–4.4/Table2、A.3。CDF等质量bins改变分配对象；一个token可跨多个bins，detector用overlap posterior而非硬投票。均匀message/随机key的平均无偏不保证固定message/key逐次保持原分布；单token低熵容量与message长度仍约束恢复。Ch72 watermark provenance/多跳攻击已有，但没有message-dependent概率预算与可观测token歧义的channel分支。Llama2-7B/C4与3.1-8B/LFQA、300tokens/24bits/topk128/T1，paraphrase的AUC可低于MPAC；whitebox teacher forcing与配置绑定不可省。2+2+2=6拟缺口深入Ch72，不赋予水印独立origin真值。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:46:44Z`，DataCite初始created `2026-04-16T02:01:52Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13786`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；本次实际正文与root非作者写后通过。2026-09-27 root重开必要v1、实际段落及相邻交接完成独立复核；未复现实验，具体采用边界与写后记录见[v3恢复笔记](../_sources/daily-20260416/v3-reopen-notes.md)。

### [FIDeL — 2604.13788v1](https://arxiv.org/html/2604.13788v1)

[exact-v1](https://arxiv.org/html/2604.13788v1) III-B–III-F、IV、VI。名义示教patch经OT对齐，split-calibration估计time/patch异常阈值，再用Qwen2.5-7B过滤良性偏离；名义false-positive校准并不直接保证最终任务failure漏检/误检，后级改变标签与错误对象。Ch26 monitor proposal/authority已有，但未显式拆anomaly→task failure的两个校准对象。BotFails/ACT soldering观察级受限测量，postfilter74.8%TNR/85.8%TPR非物理安全，demo覆盖和VLM额外成本仍在。2+2+2=6，apr01必要源→owner核验与root实际正文/相邻写后均通过，只补标签/校准交接，保简单确定性监控与人工回退。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:46:54Z`，DataCite初始created `2026-04-16T02:01:55Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13788`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)相应机制正文已实际写入；apr01必要源→实际owner核验通过，root非作者实际正文与相邻衔接复核通过。详见[五项写后核验](../_sources/daily-20260416/V3_ROOT_FIVE_ACTUAL_WRITE_AFTER.md)；未复现实验，不代替日级Gate。

### [Syn2Seq-Forcing — 2604.13793v1](https://arxiv.org/html/2604.13793v1)

[exact-v1](https://arxiv.org/html/2604.13793v1) §3.3、§4.1/§4.3 Tables3–5。把同步exo/ego拼成人工顺序，中间WFLF伪插帧与pose interpolation为训练target，推理再联合生成bridge+ego；不是取得真实同步过渡或省去pose条件。三类EgoExo4D/9frames/256²、额外生成teacher与20+150epochs训练，像素/感知分数不验证3D物理真值。frame-only与pose+frame对照值得保留，但缺跨任务的训练路径/成本条件结论；2+1+2=5标准仅报告这条受限序列重构，不机械以可映射Ch24就写书，也不以领域应用名排除。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:47:15Z`，DataCite初始created `2026-04-16T02:02:02Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13793`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [DASH-Q — 2604.13806v1](https://arxiv.org/html/2604.13806v1)

[exact-v1](https://arxiv.org/html/2604.13806v1) §3–5/Eq8–11/Algorithm1、§6.1/§7.2–7.4。用校准activation的对角二阶统计作权重，交替固定离散Q、拟合带ridge的scale/offset，再round；闭式子问题不等于整个离散量化全局最优。有限calibration中保留off-diagonal降低bias却增估计variance，因而对角化是统计取舍而非所有相关项无用。Ch49曲率/Output Gradient段已有数值风险，但没有明确“估计batch稳定性与完整相关性代价分离”的条件分支，拟2+2+2=6缺口深入 `INFER-TENSORRT-LLM`。作者五模型W2/W3/W4 weight-only、128×2048 WikiText2、group32/64/128、RTX PRO6000/CUDA13；图1只Llama2-7B第10层，不能称普遍noise诊断。部署兼容说明不是E2E serving/SLO加速证据，保更充足校准下full-covariance与较高精度旧路径。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:47:50Z`，DataCite初始created `2026-04-16T02:02:23Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13806`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；实际正文与root非作者写后通过。具体写入与反例限域见本日恢复笔记；root已核实际正文及相邻交接，未复现实验。

### [UI-Copilot — 2604.13822v1](https://arxiv.org/html/2604.13822v1)

[exact-v1](https://arxiv.org/html/2604.13822v1) §3.1/3.3、§4.4及limitations。TIPO训练期不运行copilot：tool-call在single-turn专家history上更新，action在multi-turn自产summary上更新且不含tool calls；runtime组合两条，不应伪称完整copilot交互joint-on-policy。MS/AT/MC与tool/action消融提供受限history-matching证据，Qwen2.5VL7B/AndroidWorld/MemGUI，不同copilot与benchmark比较未固定所有backend/预算；摘要与正文Android增量口径不一致不采用。2+1+2=5标准仅报告这一分训/运行组合方案；Ch33 on-policy action并不保证所有state条件同分布、Ch75 source与summary分账已有，未证明更普遍的新训练可行性边界，不同算法不假称完全已有覆盖。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:48:30Z`，DataCite初始created `2026-04-16T02:02:46Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13822`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [BehR — 2604.13824v1](https://arxiv.org/html/2604.13824v1)

[exact-v1](https://arxiv.org/html/2604.13824v1) §4.1–4.3、§5.2–5.4、§6/Limitations、AppC/K/L。冻结Qwen3-8B比较同一logged next action在真实/预测state下的平均logprob，并以差值指数给WM reward；它不是两个完整action分布相同。小的任务关键信息丢失可比大段无关文本更伤行为；single-step EM、agent排序、逐任务false positives与lookahead收益分开验收。Ch25末段已有真实性/行为价值/克制分账，尚缺行为likelihood代理与完整functional consistency的交接，拟2+2+2=6缺口深入 `MULTIMODAL-WORLD-MODELS`。两文本环境/两个WM backbone，参考模型与一eval backbone重合；近ceiling可持平/退步，WebShop K5/200任务的额外BehR收益小，不能称普遍agent-independent或安全planning。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:48:35Z`，DataCite初始created `2026-04-16T02:02:49Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13824`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — frozen-reference单个logged-action likelihood代理有受限证据，不证明完整策略/闭环一致性；既有真实性与行为价值分账无需新增配方。root本轮已实际重开必要exact-v1并对读对应正文与相邻主线，独立裁决通过，未复现实验；保留本文局部机制/反证，不把主题相似写成精确算法已覆盖。

### [CARP/SAS — 2604.13833v1](https://arxiv.org/html/2604.13833v1)

[exact-v1](https://arxiv.org/html/2604.13833v1) §3.1–3.4、§4 Tables1–4/§6。用response SAE向量重构prompt embedding，冻结decoder的重构误差作BT margin offset；偏好标签仍在，不是无label真值。加性分解/TopK稳定性是假设，平均artifact抑制不自动识别真实prompt因果；重构相关性可惩罚安全拒答且可奖励事实错误的on-topic回答，τ超界关闭该项回BT。Ch31 Goodhart段已有artifact/独立评估，尚未展开“prompt relevance proxy可以和安全偏好冲突、门控offset而非改truth”的具体分支，拟2+2+2=6缺口深入 `TRAIN-RLHF`。Gemma2B/9B受限RewardBench，安全分类较vanilla退步；BoN8 raw winrate相同，LC变好不证明task truth或消除hacking。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:49:04Z`，DataCite初始created `2026-04-16T02:03:03Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13833`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — relevance特征与安全偏好反转、差阈值回BT是受限recipe；保rawBoN/安全退步，不采用prompt重构是真因果或新稳定规范。root本轮已实际重开必要exact-v1并对读对应正文与相邻主线，独立裁决通过，未复现实验；保留本文局部机制/反证，不把主题相似写成精确算法已覆盖。

### [SparseBalance — 2604.13847v1](https://arxiv.org/html/2604.13847v1)

实际HTML §IV-A/B/C、§V-A/B/C/D、TablesI–IV。DST不是只重排同一dense工作：瓶颈microbatch削减attention budget、非瓶颈增预算到profile anchor；routing-score累计覆盖C_i(k)约束是模型/质量proxy，不是任务质量保证。SAB在CPU按最近DST预算EMA+单层lookup预测，先DP后microbatch bin-pack，范围局限当前global batch。Eq6可行集可能空、Eq7 max未给fallback；不能采用始终命中anchor的保证。单节点Qwen2.5-3B/ChatQA2、DP2PP4/mb2/gbs16，TableI SAB单独1.21低于LBB1.23，组合DST才1.35高于1.28；质量QA整体接近却summarization26.14→25.63、code67.41→66.54、64K NIAH97.60→97.53，p=.2/Min进一步退步。主实验0.5B/3B及LoRA，4node×8H200与作者所写H20环境，精度未在必要设置披露；H20被写141GB需保留厂商规格疑点，正文不采用容量数。实际Ch36“长上下文训练负载不能只按Token数均衡”已有平方proxy/kernel校准，Ch38已有readiness/stage balance；均未把attention质量预算作为straggler控制输入、与预批次预测分责。拟3+2+2=7深入，最窄Ch36现有长上下文负载段之后，保留固定budget+重排基线/任务验收，不声称原objective完全不变，有限非作者处置已通过，见本节当前处置。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:49:48Z`，DataCite初始created `2026-04-16T02:03:25Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13847`；评分 3 + 2 + 2 = 7。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；实际正文与非作者写后通过。已完成真实写入和root/apr02单篇非作者源→owner/写后；具体范围见[独立复核](../_sources/daily-20260416/V3_INDEPENDENT_FOUR_CALIBRATION.md)，不预支日Gate。

### [DiPO — 2604.13902v1](https://arxiv.org/html/2604.13902v1)

[exact-v1](https://arxiv.org/html/2604.13902v1) §3.2–3.3/Eq9–11、§4 Tables2–3、AppA.1–A.2。两batch PPL/reward queue找阈值，在全错低PPL组奖励max-PPL轨迹、全对高PPL组惩罚它，额外objective和verifier reward分开，不把错误答案改判正确。AppA明确忽略clip/跨context更新、假设F差可忽略并作近似趋势，不能采用Theorem1/2为真实模型普遍entropy保证；不同group非零梯度也不等于共享参数梯度正交。Qwen数学/function-calling仅有限经验，BFCL若干子项退步、系数过大退步。2+1+2=5、保证反证深入后拟仅报告；Ch33已有collapsed-group分流/代理和truth authority，没有理由把该PPL recipe升级为通用必需或为近似理论单独扩正文。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:53:18Z`，DataCite初始created `2026-04-16T02:04:47Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13902`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [SparseGen — 2604.13905v1](https://arxiv.org/html/2604.13905v1)

[exact-v1](https://arxiv.org/html/2604.13905v1) §3.2–3.4/§4.2–4.6 Tables3–6。learned3D anchor queries扩局部Gaussians，改变固定容量预算与input-view bias；rectified-flow/3Dpos/learnable-query消融和conditioning-vs-novel-view gap分开看，不能拿opacity使用率证明几何真值。ShapeNetCars/CO3D两类、512queries→5120Gaussians、L40生成测量，one/two-view与baseline checkpoint身份不同；‘600×’是对iterative Viewset、不是同one-shot路径。2+1+2=5标准仅报告受限query-budget分支；既有Ch23 representation budget/Ch25 geometry evidence原则不否定此局部模型证据，但当前未证明该组合改变更一般表示/生成选择，未为效率headline写Books。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:53:35Z`，DataCite初始created `2026-04-16T02:04:51Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13905`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [Compiler Remarks — 2604.13927v1](https://arxiv.org/html/2604.13927v1)

[exact-v1](https://arxiv.org/html/2604.13927v1) §3–5/Tables1–2。编译失败的笼统warning与带源位置/data dependence的反馈不是同一种observation；手工precise remark有受限收益，歧义可能诱导破坏loop dependency。Ch78 Compiler Feedback段已有syntax/type authority/后置验证，尚缺optimization-analysis反馈语义质量与变换正确性必须分账，拟2+2+2=6缺口深入 `AGENT-TOOL-CALLING`。Qwen2.5Coder7B/TSVC151 loops/100trials、Clang21.1.8与Intel2025.3、T.2/.8/1.2；可直接vectorize的loop被排除，source differential test非formal equivalence。WAW precise收益有限、ArrayBounds/Libcall有负例，不能采用‘bottleneck不是agent’为普遍因果，编译/优化成功仍不拥有完整语义truth。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:54:44Z`，DataCite初始created `2026-04-16T02:05:27Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13927`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md)；compiler诊断与功能/effect验收分权已承载，root必要源/实际owner独立通过。root本轮已实际重开必要exact-v1并对读对应正文与相邻主线，独立裁决通过，未复现实验；保留本文局部机制/反证，不把主题相似写成精确算法已覆盖。

### [ASTRA — 2604.13938v1](https://arxiv.org/html/2604.13938v1)

[exact-v1](https://arxiv.org/html/2604.13938v1) §3.2/Eq3–8、§4.1/4.4/Table4。reference identity token使用累积offset重索引，pose token位置与待生成canvas相同；不是彻底去除reference位置，而是避免把参考图布局当目标布局。统一RoPE/统一UNOPE与非对称编码对照支持这条条件分支，DSM仍同时影响identity与pose，不能照录“完全不影响pose”。Ch23时间/空间identity已有追溯要求，却未展开reference和canvas必须采用不同空间绑定对象。2+2+2=6缺口深入拟Ch23；Flux.1-dev/LoRA512/8H200、32Kpairs/128Kimages/100Ksteps，COCO pose与DreamBench受限，DINO并非所有表最佳；curation模型与训练/组件组合不构成通用因果证明，保只读结构condition与普通位置编码。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:55:16Z`，DataCite初始created `2026-04-16T02:05:42Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13938`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；必要原文/实际owner与本次真实两段正文及相邻衔接由root非作者复核通过，具体位置见本日恢复笔记，未复现实验，未日Gate。

### [HINTBench — 2604.13954v1](https://arxiv.org/html/2604.13954v1)

[exact-v1](https://arxiv.org/html/2604.13954v1) §3.1–3.3、§4.1–4.3/Limitations。benign指令/有效tool/非对抗反馈下，629合成轨迹中523风险/106安全、均33steps，不是生产风险发生率。trajectory风险、typed step定位、first-risk后截断的平衡prefix监控是不同测量对象；强完整轨迹得分不推出执行前检测能力，1000prefix亦非新增独立原始轨迹。Ch72已有sensor/locator/stepguard分责、Containment过程状态和持续窗口检测；这项补充受限评估证据，不形成新的执行authority。2+1+2=5安全深入后拟已有覆盖；保合成/最早risk标注不确定与类别不平衡，不取guard排名作通用部署保证。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:55:53Z`，DataCite初始created `2026-04-16T02:06:06Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13954`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [GEM3D-CIM — 2604.13969v1](https://arxiv.org/html/2604.13969v1)

[exact-v1](https://arxiv.org/html/2604.13969v1) §III–V/VI-A–E。SRAM/eDRAM上下层的transpose复制/交换及mixed-signal乘加，涉及DAC/comparator、LFSR code与LUT转换，不是消除外围开销或任意精度MAC。GF22nm transient/1000 Monte Carlo、4×4验证和32×32估算，比较部分节点归一与操作energy另有excluding peripheral口径；没有真实LLM kernel/模型质量或Serving负载。2+1+2=5标准仅报告具体内存操作路线；Ch54容量/带宽/面积能耗合同不能由这个电路case升级成可部署LLM架构选择，不以“foundry compatible”称已制造，不假称已有同一电路。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:56:44Z`，DataCite初始created `2026-04-16T02:06:28Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13969`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [FinePhrase — 2604.13977v1](https://arxiv.org/html/2604.13977v1)

实际 exact-v1 §2–5 与 Limitations。1.2B、21B token、64 H100/bf16、固定来源/teacher 的 prompt 对照；generator 扩大在多数格式无优势，但复杂 Guided Rewrite 的4B优于1B，不能采用通用1B阈值。合成/原始 mix 和生成源分开控制；纯合成对NLU有损。输出格式完成率高不等于下游收益，template 多样性只观察到跨家族相关，非独立模板干预；重复样本补足token不是相同unique-data。已实际对读 Ch27 quality/synthetic/recursive corpus，缺口是prompt要求×generator能力×raw mix 的联合选择及格式执行率与训练效用分账，而非再讲多样性。拟2+2+2=6，真实缺口深入、Ch27 Synthetic 导入后窄分支，已向 root 提必要独立校准，现已实际整合，见下述当前处置。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:57:05Z`，DataCite初始created `2026-04-16T02:06:39Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13977`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)；实际正文与非作者写后通过。已完成真实写入和root/apr02单篇非作者源→owner/写后；具体范围见[独立复核](../_sources/daily-20260416/V3_INDEPENDENT_FOUR_CALIBRATION.md)，不预支日Gate。

### [Adaptive Conformal — 2604.13991v1](https://arxiv.org/html/2604.13991v1)

[exact-v1](https://arxiv.org/html/2604.13991v1) §2.2/Eq3–6、§2.3/Eq8–12、§3.1。长文F_t={s≤t}随阈值增加保留更多claim，V定义最大安全阈值，却采用Q_(1−α)(V)保证全部保留正确。直接反例：每题一个错误claim且s=U~Uniform(0,1)，V=U；α=.1、大样本阈值趋.9时空集/全部正确概率只有.1，而非.9。此反例针对长文过滤的分位方向与对象，不否定MCQ Eq7 LAC的真类集合覆盖，也不否定embedding-conditioned三split校准的受限经验。2+2+2=6反证深入，拟争议/暂缓，不入Books。重开需精确修正V/错误集合、分位方向或coverage解释；正的normalizer与exchangeability条件同样不可省，不把经验conditional改善升级成普遍conditional保证。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:57:45Z`，DataCite初始created `2026-04-16T02:06:59Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13991`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：暂缓 — 中心保证的精确争议与重开条件见§4/§5，不入Books。争议只隔离上文缺失条件/公式保证；重开需精确修正或实现解释，apr20必要源/有效反证独立终核通过，采用保证精确隔离。

### [Reward Design — 2604.13993v1](https://arxiv.org/html/2604.13993v1)

[exact-v1](https://arxiv.org/html/2604.13993v1) §3.3/Eq5–8、§4.1/Table1及消融。format/accuracy/rubric与内部foreground attention是不同reward，后者以raw RGB非白区域和最后Q/K计算，是visual reliance代理而非独立空间真值；面积归一不消除attention归因歧义。GraniteVision3.3-2B、GRPO1epoch/group8/bf16/max512/4A10080G，PhyX的MCQ与OE分开；部分domain退步且judge为GPT-oss120B。此项研究奖励设计，不因physics应用就判AI-for-Science，但没有分离可迁移的新reward校准或因果credit机制。2+1+2=5标准仅报告这个受限reward比较，不把foreground attention升级成正确性或通用物理推理保证。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:57:49Z`，DataCite初始created `2026-04-16T02:07:02Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13993`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

### [Learned or Memorized — 2604.13997v1](https://arxiv.org/html/2604.13997v1)

[exact-v1](https://arxiv.org/html/2604.13997v1) §2.4–2.5/Eq2–3、§3.3–3.4、§4/§5.4。五次BART改写按cosine drift排列，代码只用identifier alpha-renaming，task平均distance取相邻最大performance drop；并非已知训练membership。8models/19datasets/5tasks的敏感度是稳健性观察，既不能由低敏感推没记忆，也不能由高敏感证明泄漏。作者§5.4明确未知训练数据/噪声容忍；保这条局限，而非判全文理论错误。Ch66 contamination injection段要求已知注入/未污染counterfactual，否则只报疑似污染，实际承载可采用边界。2+1+2=5，headline反证深入后拟已有覆盖；不采用推断训练语料的确定性排名，保具体任务结果而非否定全部测量。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:58:03Z`，DataCite初始created `2026-04-16T02:07:08Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-13997`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [Diffusion LM for ASR — 2604.14001v1](https://arxiv.org/html/2604.14001v1)

[exact-v1](https://arxiv.org/html/2604.14001v1) §3.1–3.2、§4/Tables。MDLM重排用Monte Carlo masked-token伪似然，complementary masks让每位置计分；whole-length与per-mask-count归一改变权重，不能叫精确joint likelihood。USDM每位置vocab概率可与CTC帧—折叠token对齐并在每次去噪log-linear组合；接口不同，不把两类DLM任意互换。LibriSpeech、24×1024或12×768、10240subwords，WER/PPL上界分账，AR joint基线仍更强，MC样本/denoising成本不免费。Ch24有masked/noise正确性主线但没有sequence reranking与位置概率跨模型融合这两种接口选择。2+2+2=6缺口深入拟Ch24最窄ASR条件分支，不给普遍速度/精确posterior保证。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:58:08Z`，DataCite初始created `2026-04-16T02:07:14Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-14001`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；实际正文与root非作者写后通过。本次root实际顺读四条正文与相邻主线、复用有效必要v1通过，未复现实验，不预支日级Gate。

### [Memory Transfer Learning — 2604.14004v1](https://arxiv.org/html/2604.14004v1)

[exact-v1](https://arxiv.org/html/2604.14004v1) §3–4/§5.Tables与负向对照。轨迹、workflow、reasoning summary、去任务细节insight是不同检索对象；目标benchmark从source pool排除，系统prompt注入embedding topN，额外LLM rerank/rewrite可比简单embedding更差。三个runs/pass@3没有控制全部memory长度/模型成本，task-agnostic收益约1.1点不能推所有原轨迹无用。Ch77 ReasoningBank段及子问题—过程检索已明确可复用策略由episode派生、适用条件不能丢、原轨迹回退；跨任务实验是这条具体路径的受限证据，不是新事实authority。2+1+2=5标准拟已有覆盖，不假称已有该全文实现。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:58:22Z`，DataCite初始created `2026-04-16T02:07:18Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-14004`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：已有覆盖 — AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)；具体既有命题见§4，apr01具体源与实际owner独立终核通过。具体承载论点如上；不是因为主题已有而初筛排除。

### [EPI — 2604.14010v1](https://arxiv.org/html/2604.14010v1)

[exact-v1](https://arxiv.org/html/2604.14010v1) §2.3–2.5、Tables2–3。当前训练aggregate gradient平方的EMA不是已验证旧任务Fisher/Hessian；先layer minmax校准再global top保护，非各层相同quota。每H steps刷新mask，真正阻止的是最终AdamW参数delta（含weight decay），不能只说零梯度即足够；moment/选择state是否更新另属实现。静态/动态、layer校准与raw-global对照支持刷新/尺度两个对象；频繁抖动与陈旧保护取舍仍在，1%是实验配置不是知识只有1%。Ch29当前data×mask selector与方向保护尚未展开统计量刷新和最终optimizer-delta的区别。2+2+2=6缺口深入拟Ch29 continual保护段，只补可撤销mask/更新坐标接口，不给通用比例或遗忘保证。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:58:47Z`，DataCite初始created `2026-04-16T02:07:27Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-14010`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)；可撤销mask与最终AdamW delta两段实际写入，受测大语言模型多任务SFT范围已纠正，root必要来源/真实owner及正文相邻交接写后独立通过，未复现实验，未日Gate。

### [MAny — 2604.14016v1](https://arxiv.org/html/2604.14016v1)

[exact-v1](https://arxiv.org/html/2604.14016v1) §4.2–4.3/Eq8–11、§5.1–5.5/Tables1–3/AppA.1必要代数。视觉侧按冻结encoder的task prototype混合projector输出，不是直接平均非线性projector权重；语言侧LoRA转换为实际矩阵delta，以累计XᵀX递归合并后加到base。RLS等价限固定特征/可逆完整covariance，低秩截断、backbone更新使后续feature变化、λ缩放都不能继承全网最优；存储也含task projector和统计量。LLaVA/InternVL7B、LoRA16、λ3/γ.999，两continual benchmark；单任务值/FFM并非全表最优，“zero-shot低”不证明无预训污染，训练仍需每task tuning。Ch23共享encoder/projector链未展开conditional输出路由和静态language consolidation的不同演进对象。2+2+2=6拟缺口深入Ch23，保replay/独立task adapter，不宣称全流程training-free。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:58:54Z`，DataCite初始created `2026-04-16T02:07:36Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-14016`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；必要原文/实际owner与本次真实两段正文及相邻衔接由root非作者复核通过，具体位置见本日恢复笔记，未复现实验，未日Gate。

### [Stochastic Trust Region — 2604.14017v1](https://arxiv.org/html/2604.14017v1)

[exact-v1](https://arxiv.org/html/2604.14017v1) §3/Algorithm1、§4/Lemma4.1。原文由两个upper bounds推步长下界a≥2(1−c0)/(L−c0)、a≤1。取n1、f(x)=x²/2、L1、x1、g1、Δ.1、c0.1，step=−.1，actual/predicted=.095/.095=1被接受；满足无偏/strong growthρ1和插值，却a=.1不可能满足所称a≥2。直接反例只否定缺条件的步长下界及依赖它的普遍复杂度保证，不否定经典TR ratio/有限经验或所有算法分支。2+2+2=6反证深入拟争议/暂缓，不写Books；重开需修正Lemma假设/不等式推导和相应定理，不追整个版本史。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:58:56Z`，DataCite初始created `2026-04-16T02:07:38Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-14017`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：暂缓 — 中心保证的精确争议与重开条件见§4/§5，不入Books。争议只隔离上文缺失条件/公式保证；重开需精确修正或实现解释，apr20必要源/有效反证独立终核通过，采用保证精确隔离。

### [POINTS-Seeker — 2604.14029v1](https://arxiv.org/html/2604.14029v1)

[exact-v1](https://arxiv.org/html/2604.14029v1) §3.6、§4/Tables2–3。历史超过8K后把旧工具observation逐项render为图像，action全部留文本，最近K项observation仍文本；需要5K fully-rendered SFT样本混合适配，非任意模型免费光学压缩。all-image比mixed/stale-only差，freshness与表示选择需共同验收；WebSearch原返回已含Qwen235B summary，raster视图不是原网站事实副本。8B与selected hardset、BC-VL44.4/42.6等受限评价，不证明端到端时延节省；基于QwenViT/Qwen3Base初始化的from-scratch不是随机从头训练。Ch75现artifact active slots保留像素证据，但未描述把旧文本observation转图像、精确近期协议保文本的接口分支。2+2+2=6缺口深入拟Ch75，只采用derived-view/freshness/supervision分账，保原文本恢复。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:59:24Z`，DataCite初始created `2026-04-16T02:07:56Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-14029`；评分 2 + 2 + 2 = 6。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：整合 — AGENT-CONTEXT [Ch75](../../../../books/part-07-agent/75-context.md)相应机制正文已实际写入；apr01必要源→实际owner核验通过，root非作者实际正文与相邻衔接复核通过。详见[五项写后核验](../_sources/daily-20260416/V3_ROOT_FIVE_ACTUAL_WRITE_AFTER.md)；未复现实验，不代替日级Gate。

### [Shallow ReLU Symmetry — 2604.14037v1](https://arxiv.org/html/2604.14037v1)

[exact-v1](https://arxiv.org/html/2604.14037v1) §1/Defs、Theorem1/最小形思路。对象为单隐藏层的realization map，permutation/positive scaling及ReLU(x)−ReLU(−x)=x给出不同参数同函数；同有限dataset loss不是同全输入函数。作者完整classification与generic dense-fibre结论限所列浅层结构，不能推所有参数仅一orbit或任意深LM merge。已核直接恒等式、对象/前提与分类必要结构，不声称全部长证明/代码复现。2+1+2=5标准仅报告这个受限identifiability结果，不把数学classification变成优化/LoRA融合可部署规则；保作者更强定理为未作全证明验算的报告事实。

日期依据：自身原始v1 metadata Updated `2026-04-16T00:59:52Z`，DataCite初始created `2026-04-16T02:08:09Z`只作登记邻界。两者不是逐篇公告日志；与官方[ID分配/公告规则](https://info.arxiv.org/help/availability.html)、连续/OAI批界共同支持本日08～09有据推断。家族 `SF-2026-ARXIV-2604-14037`；评分 2 + 1 + 2 = 5。已读上文实际必要采用范围，不声称全部附件/全部定理复现。

当前处置（覆盖早期提案时态）：仅报告 — 受限机制/反证不足改变长期设计，具体理由见§4。保留具体方法/反证，不假称相同宏观主题就是同算法覆盖，不为局部recipe强行加书。

## 5. 缺口与下一步

**普通待办：**无。39项必要Books已真实写入并通过非作者写后；15已有覆盖、28仅报告和5窄争议已完成有限独立终核，root来源/日期/准入及日级验收通过。没有把486宽库存变成逐项全文队列。

**撤回/勘误轻量检查：**2026-09-27T02:24:19+08:00前已实际取得86个工作arXiv家族及日期隔离的14148共87个官方当前abs页，标题/摘要身份均有效；当前可见Comments中没有withdrawn/勘误通知。另核exact-v1身份与40个暴露的Comments字段；13536的self-correction、13634的Online Correction Memory和13997的data leakage均是研究内容，不是撤回或纠错公告。该检查仅覆盖官方标题、摘要与可见Comments，不声称审过全部版本历史或据此证明正文不存在任何错误。

**外部来源/日期终态保留项：**

- OpenAI Research历史分页：RSS支持SDK但不替代研究目录。需要本窗官方历史目录/存档，原SDK日期不因此失效。
- Google Publications年358列表无首公开日级停点；Simula仅Apr16自然日，需原时区精确时间或完整落窗区间才单项重开，不扩全年。
- Meta空Research、替代2016–2020/混排Blog：需正确历史分页或本窗目录，不写零研究。
- Moonshot Blog止2025/release空：需2026本窗历史入口，新仓库有界检查不代替Blog。
- ERNIE-Image仅Apr15日级；Seedance2.0/2604.14148v1字段01:04:49Z晚于截点：需原始公开时段，Submitted或card不能证明本窗。
- MiMo无日期Blog、MiniMax TechBlog历史缺字段：需本窗官方目录；各自Paper/两语言Blog的跨窗停点仍有效。
- arXiv13175/13301/13426/13662后改字段、旧14084/14116及tail14044起：不得套早段推断，仅对真正有贡献项恢复首次公开日期；不机械迁下一日报、不扩当前窗。

被隔离项不支持无遗漏、正面证据、Books、性能或安全保证。争议按§4具体条件重开，不追全版本史。本次可执行工作已完成；材料到达后只定点重开受影响项。

## 6. 复核

复核者：root（本次报告非作者）；apr02早期独立单篇记录只复用其实际未写的来源/正文核验范围，apr02现为本次恢复作者，不担任本次日级独立Gate

结论：通过

root非作者日级验收已通过：实际核十四来源停点、日期组合与隔离、轻量撤回范围、准入及报告集合，复用有效39项必要源→owner/实际正文与相邻衔接写后，不无差别重读全部附件。终态87=39整合+15已有覆盖+28仅报告+5窄争议，普通待办0。五争议和八类覆盖/日期限制只作安全隔离，不算Evidence或零遗漏通过。

[15项已有覆盖终核](../_sources/daily-20260416/V3_APR01_FIFTEEN_EXISTING_FINAL_AUDIT.md)由apr01完成：13068/13108/13151复用未变有效必要源，其余定点原文及15个实际owner对读；13348三数定位误判已撤销，同分母缺口保持。该记录末“89候选”是笔误，正式唯一分母为87。[28项仅报告终核](../_sources/daily-20260416/V3_ROOT_ONLY_TERMINAL_AUDIT.md)由root完成：8项有效范围复用、19项本轮必要原文与13634披露有损合同纠正；另按六类抽检13468/13630/13849/13600/13085/13100完整题摘，13630/13849补安全必要核心，不称全量否定侧检查。[五窄争议及CSD纠正](../_sources/daily-20260416/V3_APR20_BOUNDED_SIX_DISPUTE_REVIEW.md)由apr20完成：13088/13523有效必要反证复用，13546/13991/14017定点原文；13634已披露lossy，改仅报告，不永久等待重复披露。实际范围如上，不声称验算全部定理或复现实验。

39项实际写入记录见[既有核验](../_sources/daily-20260416/V3_INDEPENDENT_FOUR_CALIBRATION.md)、[恢复笔记](../_sources/daily-20260416/v3-reopen-notes.md)、[八项写后](../_sources/daily-20260416/V3_APR01_BOUNDED_EIGHT_INDEPENDENT_AUDIT.md)与[最终五项写后](../_sources/daily-20260416/V3_ROOT_FIVE_ACTUAL_WRITE_AFTER.md)。作者汇总非作者结果，不以自身审阅充当日级独立Gate。87候选行、87唯一身份及87证据小节一致；当前validator与限定git diff --check通过，只证明可判定一致性，不替代语义验收。保护既有dirty/staged，不stage、commit或push。
