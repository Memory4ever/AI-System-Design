# Daily Research — 2026-05-09

**规范：** V3
**窗口：** 2026-05-08T09:00:00+08:00 ～ 2026-05-09T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-18T22:02:17+08:00
**补充窗口：** 2026-05-08 ～ 2026-05-08
**窗口说明：** 用户授权仅补已有日报遗漏；原小时窗、原候选日期/评分及有效证据保留。旧完成声明只描述既有审阅；本轮补查完整日级复核见R37，不以旧声明替代。
**冻结候选日期：** [补查前原件](../_sources/daily-20260509/baseline-before-supplement-20261018.md)

## 1. 结论

本轮仅补 05-08 北京时间完整自然日；原 ERNIE 5.1 保留 05-09 的旧归属与有效审阅，不搬移。有限 arXiv 发现的51份完整题摘归并为39个当窗新增家族、6项贡献/早事件关闭和6项资格隔离；加官方 Teaching Claude Why，共40新增。当前单表原1＋新40＝41家族，新31项实际 Books 整合、9项具体已有覆盖均已非作者核验，普通Source/Books差额0；保留项不算正面Evidence或无遗漏。六部分完整独立DAY R37通过，本轮已完成；来源/日期的终态限制不被完成标签消除。详[唯一补查记录](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

**恢复 checkpoint（2026-10-18，用户明确恢复）：** 原A13暂停由明确恢复覆盖，所有本日必要Source、31项新增正文及本人注实际POST、9项具体NC和六资格有限停止均已分批通过，完整六部分R37已验收。有效证据未重审，全部Books窄位已释放，无本日普通研究/Books待办，不stage/commit/push。

原小时窗口没有 arXiv scheduled announcement batch；旧报告据此写成零候选是正确的局部事实，但它只检查了 arXiv，不能满足当前 Daily 合同。旧轮补查 13 个每日机构入口后恢复 1 个当窗事件：Baidu 在官方 Blog 发布 ERNIE 5.1，页面 metadata 给出 `2026-05-09T00:00:00Z`，即北京时间 08:00，明确落入原窗，不将此日期搬到本轮补充自然日。

该发布把三条已经分别存在的路线组合进同一模型生命周期：多维 elastic sub-network、训练/推理/奖励/Agent loop 的全异步解耦，以及多专家 on-policy distillation 后针对高熵任务保留 online RL 分支。它提供的是厂商实现与版本事实，不是独立复现；6% 训练成本、K3 KL 降低 50% 和各项 benchmark 均缺少可复算的完整 workload、硬件、precision、batch、并发和 SLO 合同。本次评分为 `2 + 3 + 2 = 7`，完成深入审阅；对读 Ch21、Ch31 与 Ch33 后判定为已有覆盖，不重复添加版本型正文。

旧轮原 ERNIE 范围的 Coverage、Evidence 与 Books 判断已闭合，并通过非作者独立复核；这不覆盖本轮补窗。动态历史目录的分页缺口已隔离，
没有参与正向证据或“全站绝无更新”断言。

## 2. 来源覆盖

本轮只检查 Daily 来源，不扫描 Weekly 来源。以下按本日实际[A11/A24入口与停止位置](../_sources/daily-20260509/SUP_SOURCES_20261018.md)更新，不继承他日来源成功或旧报告完成标签；完整日级独核R37已通过，受阻/有限范围仍保留。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/News 历史入口与本窗定点检索 | 受阻 | 未恢复可按 24 小时窗口分页的历史目录；不支持“官方绝无更新”的断言，也不支持候选或 Books |
| SRC-ANTHROPIC | Research/Alignment 公开列表及 May08 Teaching Claude Why 必要原文；May07 Donating 相邻 | 已检查 | 新增 Teaching Claude Why 已实际整合；目录日期不补造时刻，不授全机构无遗漏 |
| SRC-GOOGLE-AI | DeepMind / Google Research Publications 有界检查本窗与相邻日期 | 受阻 | 历史列表日期粒度和分页停止点不足；隔离为 Coverage limitation |
| SRC-META-AI | 官方 Research 当前空正文、官方域 May08 定点查询与本窗 arXiv family 身份交叉 | 受阻 | 未恢复必要历史日级列表，不从空响应授 Coverage 或零遗漏 |
| SRC-QWEN | 官方 retrieval API zh-CN 实返无序40条，全部按 extra.date 筛；Apr30→May19跨窗，未见May08 | 已检查 | 仅当前40条日期元数据；无可用分页字段，不证明完整历史或所有语言 |
| SRC-DEEPSEEK | 官方 `/news/` 历史索引；相邻可见研究事件为 04-24 与 06-24 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 官方仓库的本窗定点检查 | 受阻 | 缺稳定的历史分页停止点；不支持零遗漏断言 |
| SRC-TENCENT-HUNYUAN | Research 动态入口失败后实际官方 publicList POST page1/size100/renderType0；code0、total9、实返9且全英语，displayPublishTime Apr30→Jul08跨窗，无May08 | 已检查 | 只闭合此英语9条响应；中文/历史删条未证明，不继承旧Apr30/May21双语范围 |
| SRC-ZAI | 智谱 Research 列表；相邻日级条目为 04-29 与 05-20 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 官方JS目录API type1/page0实18→page20实20跨May16至Apr15后停止（next40/true）；type2实15、next空/false而total20；实际切片无May08 | 已检查 | 英语实返与total不一，不授全语言历史完整；2605.09233当前目录May10不等首次公开日，不由PublishDate覆盖arXiv合证 |
| SRC-BAIDU-ERNIE | ERNIE Blog 目录与 `ernie-5.1-0508-release` 正文；HTML metadata=`2026-05-09T00:00:00Z` | 已检查 | 1 个当窗事件；厂商技术博客没有独立复现或完整 system card |
| SRC-XIAOMI-MIMO | MiMo Papers 可见列表与 Blog 历史入口定点检查 | 受阻 | Blog 缺可复查的历史日级分页；隔离，不支持候选或零遗漏断言 |
| SRC-MINIMAX | 官方 Research/Blog 历史列表；相邻事件为 03-18 与 05-26 | 已检查 | 无 |
| SRC-ARXIV | 原小时窗无 scheduled batch；补窗May08按A4/A6有限主题与官方12类邻接题名检查，51完整题摘及188具名旧事件去重，主要发现收口；A35/R25六资格有限原始入口已收尾 | 已检查 | 51不是候选/全文队列；六资格不支持当窗候选，未授全学科召回或无遗漏；不用Created/catchup代实际日期 |

无法恢复的历史目录停止点已作为终态限制隔离：它们不支撑候选、Books 或“无遗漏”断言；若未来获得目标时段的官方归档，只重开相应来源与日期。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [ERNIE 5.1 Officially Released](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) | 2026-05-09T08:00:00+08:00 | 把 elastic sub-network、四子系统异步 RL 与 multi-teacher OPD/online-RL 分流组织为同一模型生命周期；`2 + 3 + 2 = 7` | 深入完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)；相关边界见 MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md) 与 TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Teaching Claude Why](https://alignment.anthropic.com/2026/teaching-claude-why/) | 2026-05-08 | 同分布拒绝示教分数不能代替跨情境 alignment；响应重写、OOD 困境 advice、SDF/环境多样性的受限对照；`2 + 2 + 3 = 7` | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，§为什么少量高质量数据也可能有效；非作者必要证据及实际写后复核通过 |
| [Relay Buffer Independent Communication over Pooled HBM for Efficient MoE Inference on Ascend](https://arxiv.org/html/2605.06055v1) | 2026-05-08 | 稳定 symmetric-HBM 地址域下 direct expert-window placement / consumer read，分开 payload 中转与紧凑协调；`2 + 2 + 2 = 6` | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，kernel 内 remote-memory / Purlin / ThunderEP 及 MoE offset-readiness 具体正文；非作者 Source 与 NC 通过 |
| [Tackling the Data-Parallel Load Balancing Bottleneck in LLM Serving: Practical Online Routing at Scale](https://arxiv.org/html/2605.06113v1) | 2026-05-08 | 共享 decode barrier 下按 safe margin 的非对称 F-score 在线 admission，短 horizon 与实际预测回退；`2 + 2 + 2 = 6` | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，非作者必要 Source、写前及实际写后复核通过 |
| [FalconGEMM](https://arxiv.org/html/2605.06057v1) | 2026-05-08 | LCMA group-local 复用与就地输出组合，按 shape/算术/带宽和精度选择普通 GEMM；`2 + 2 + 2 = 6` | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，GEMM shape 后；必要 Source、写前与实际写后通过 |
| [ResiHP](https://arxiv.org/html/2605.06374v1) | 2026-05-08 | block-diagonal packing 的平方长度和与真实 pipeline DAG 先解释健康迭代，再验证剩余异常；`2 + 2 + 2 = 6` | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，Failure 节；必要 Source 与含假设修复的实际写后通过 |
| [AgenticRAG: Agentic Retrieval for Enterprise Knowledge Bases](https://arxiv.org/html/2605.05538v1) | 2026-05-08 | 广证据需要与深读策略的失败边界，调用效率不等质量、完整 token 成本分账；`1 + 2 + 2 = 5` | 标准完成 | 已有覆盖：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，固定 Context 工作集的 depth/diversity/downstream/sufficiency 与菜单-open-use 分账；非作者具体 NC 通过 |
| [MiA-Signature: Approximating Global Activation for Long-Context Understanding](https://arxiv.org/html/2605.06416v1) | 2026-05-08 | 派生摘要用于检索不代表适合追加回答 Context，分接口验收及任务反退；`1 + 2 + 2 = 5` | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，摘要树后；必要 Source、写前与实际写后通过 |
| [PoTAcc](https://arxiv.org/html/2605.06082v1) | 2026-05-08 | PoT码宽不等PE中间位宽，转换须同步scale/bias并验packing/prepare/实际算子路径；`2 + 1 + 2 = 5` | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，INT4例后；必要Source、写前与实际写后通过 |
| [TokenStack](https://arxiv.org/html/2605.05639v1) | 2026-05-08 | vertical capacity/compute分域与非对称K/V布局，资格、量化和迁移共同计价；`2 + 2 + 2 = 6` | 深入完成 | 整合：INFER-GPU-MEMORY [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)，CD-PIM后；必要Source/PRE/实际POST通过 |
| [Teaching LLMs Program Semantics](https://arxiv.org/html/2605.06184v1) | 2026-05-08 | trace-CPT结构与thinking的交互，分账violation发现、holds保持、解析和超时；`2 + 1 + 2 = 5` | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，阶段QA后；必要Source/PRE/实际POST通过 |
| [OBLIQ-Bench](https://arxiv.org/html/2605.06235v1) | 2026-05-08 | 同verifier的真实/gold-injected pool诊断候选发现与给定后验证差额；`2 + 1 + 2 = 5` | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，单向量域迁移后；必要Source/PRE/实际POST通过 |
| [SIRA](https://arxiv.org/html/2605.06647v1) | 2026-05-08 | 两侧词表扩展以库DF约束、仅online要求存在，保词面-v-相关性边界；`2 + 1 + 2 = 5` | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，Online Pipeline词法总述后；必要Source/PRE/实际POST通过 |
| [ROSE](https://arxiv.org/html/2605.06534v1) | 2026-05-08 | 独立虚拟KV地址域借物理页，按TTFT/TPOT双余量接纳rollout；`2 + 2 + 2 = 6` | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，Rollout服务首段后；必要Source/PRE/实际POST通过 |
| [VideoRouter](https://arxiv.org/html/2605.05848v1) | 2026-05-08 | 固定帧预算下局部细节与全局覆盖路由及预算反转；`2 + 1 + 2 = 5` | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，relevance/coverage双支与局部/跨事件粒度；非作者具体NC通过 |
| [EGA](https://arxiv.org/html/2605.05674v1) | 2026-05-08 | 零残差与局部hinge停止仍须验累计全局漂移；`2 + 1 + 2 = 5` | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，REZE后；必要Source/PRE/实际POST通过 |
| [DeScore](https://arxiv.org/html/2605.05922v1) | 2026-05-08 | 训练CoT随机mask/专用reward-query读出与辅助BT排序分工，部署仍think后score；`2 + 1 + 2 = 5` | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，teacher理由后；必要Source/PRE/实际POST通过 |
| [Active Task Selection](https://arxiv.org/html/2605.05703v1) | 2026-05-08 | 已标任务pool的近似信息选择与图实际更新分责，结算selection全费；`2 + 1 + 2 = 5` | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，图/prompt训练后；必要Source/PRE/实际POST通过 |
| [MASPO](https://arxiv.org/html/2605.06623v1) | 2026-05-08 | peer版本改变后刷新beam评分，local/lookahead/终局judge分账；`2 + 1 + 2 = 5` | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，Active Task后；必要Source/PRE/实际POST通过 |
| [Prologue](https://arxiv.org/html/2605.06137v1) | 2026-05-08 | 辅助码直接承接AR梯度、视觉码重建；共享encoder间接更新仍在；`2 + 1 + 2 = 5` | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，VideoFlexTok后；必要Source/PRE/实际POST通过 |
| [wAR-Tok](https://arxiv.org/html/2605.06148v1) | 2026-05-08 | 当前step的target/proxy可预测性压力与重建分责；跨step target更新冲突不作recipe；`2 + 1 + 2 = 5` | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，Prologue后；受限Source/PRE/实际POST通过，target配置争议隔离 |
| [NOVA](https://arxiv.org/html/2605.06298v1) | 2026-05-08 | 共享INR的weight-offset状态与加性dynamics/action分工，可编辑性不等物理准确；`2 + 1 + 2 = 5` | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，Latent dynamics首段后；必要Source/PRE/实际POST通过 |
| [FFDC-WAM](https://arxiv.org/html/2605.06222v1) | 2026-05-08 | 执行chunk时以真实新观测对照计划future，小verifier触发重规划；`2 + 1 + 2 = 5` | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，Action chunk首段后；必要Source/PRE/实际POST通过 |
| [VLA-GSE](https://arxiv.org/html/2605.06175v1) | 2026-05-08 | SVD共享/专用adapter与期望初始化补偿，非逐输入函数保持；`2 + 1 + 2 = 5` | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)，SVD/条件adapter局部；必要Source/PRE/实际POST通过 |
| [FREPix](https://arxiv.org/html/2605.06421v1) | 2026-05-08 | 正交state坐标、异质path、低高频预测职责和time-weight分开；`2 + 1 + 2 = 5` | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，flow路径局部；必要Source/PRE/实际POST通过 |
| [EMO](https://arxiv.org/html/2605.06663v1) | 2026-05-08 | 训练document-pool/global balancing与部署validation-subset分责；`2 + 1 + 2 = 5` | 标准完成 | 已有覆盖：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)，受限pool/全局统计与条件子网选择；非作者具体NC通过 |
| [ReasonMaxxer](https://arxiv.org/html/2605.06241v1) | 2026-05-08 | 固定离线mixed-support有符号CE对照分离目标与on-policy探索；`2 + 1 + 2 = 5` | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，EG-GRPO后；Source/PRE/实际POST通过 |
| [TurnGate](https://arxiv.org/html/2605.05630v1) | 2026-05-08 | response-conditioned pre-delivery gate与经验阈值分责，非生成前审题或真值；`2 + 1 + 2 = 5` | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，stop隐藏边界后；Source/PRE/实际POST通过 |
| [SLAM](https://arxiv.org/html/2605.05443v1) | 2026-05-08 | key/文档身份选SAE carrier方向子集与白盒重放检测分责；`2 + 1 + 2 = 5` | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，重写水印后；Source/PRE/实际POST通过 |
| [MemReranker](https://arxiv.org/html/2605.06132v1) | 2026-05-08 | teacher相对偏好训练检索读出不认证跨query绝对概率与完整答案；`2 + 1 + 2 = 5` | 标准完成 | 已有覆盖：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，offline utility/蒸馏embedding与consumer版本段；非作者具体NC通过 |
| [Rubrics](https://arxiv.org/html/2605.06283v1) | 2026-05-08 | criteria/测量粒度/聚合与表面改写分账，自一致非外部效度；`2 + 1 + 2 = 5` | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，criterion调用/聚合及generator×reader×domain正文；非作者具体NC通过 |
| [Litespark](https://arxiv.org/html/2605.06485v1) | 2026-05-08 | 较宽int8执行容器绕紧码unpack，物理格式/成本/任务质量分账；`2 + 1 + 2 = 5` | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，三值packing-v-较宽码consumer及完整成本；非作者NC通过 |
| [VISD](https://arxiv.org/html/2605.06094v1) | 2026-05-08 | verifier定sampled-token方向、正受限teacher权重调幅，不保参数梯度/真值；`2 + 1 + 2 = 5` | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，Verifier方向/Privileged Teacher幅度完整正文；非作者NC通过 |
| [Automated Safety is Harder Than You Think](https://arxiv.org/html/2605.06390v1) | 2026-05-08 | proxy解释与相关证据聚合两层条件风险不因更多自动研究消失；`2 + 1 + 2 = 5` | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，外部效度/共享盲区与panel独立发现边界；非作者NC通过 |
| [TextPro-SLM](https://arxiv.org/html/2605.05927v1) | 2026-05-08 | ASR decoder内容流与重构声学流来源/目标分责，非语义韵律解耦；`2 + 1 + 2 = 5` | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，语义anchor目标后；Source/PRE/实际POST通过 |
| [Metonymy vision models](https://arxiv.org/html/2605.06095v1) | 2026-05-08 | 全图feature后mask不能撤销混入，early值隔离仍条件于全图生成mask；`2 + 1 + 2 = 5` | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，f-CBM后；Source/PRE/实际POST通过 |
| [AEN-SAE](https://arxiv.org/html/2605.05341v1) | 2026-05-08 | 固定dictionary/权重的强凸最优code稳定性非联合训练或语义证书；`2 + 1 + 2 = 5` | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，sparsemax SAE后；Source/PRE/实际POST通过 |
| [UniSD](https://arxiv.org/html/2605.06597v1) | 2026-05-08 | 多context只调主teacher权重，scalar divergence cap非参数gradclip；`2 + 1 + 2 = 5` | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，short/full-context后；Source/PRE/实际POST通过 |
| [Efficient Pre-Training with Token Superposition](https://arxiv.org/pdf/2605.06546v1) | 2026-05-08 | 同主头next-bag/丢序后恢复NTP，以更多data换作者等FLOPs质量；`2 + 1 + 2 = 5` | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，future-token边界后；Source/PRE/实际POST通过 |
| [Conditional Diffusion Under Linear Constraints](https://arxiv.org/html/2605.05387v1) | 2026-05-08 | measurement normal可行性与未知conditional tangent质量分开，有限BAOAB非exact；`2 + 1 + 2 = 5` | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，InpaintSLat后；Source/PRE/实际POST通过 |
| [Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key](https://arxiv.org/html/2605.06638v1) | 2026-05-08 | 固定可核生成规则下任务结构/课程与step-token-FLOPs预算分责；`2 + 1 + 2 = 5` | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，课程自博弈职责后；Source/PRE/实际POST通过 |

## 4. 证据与知识整合

### [ERNIE 5.1 Officially Released](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/)

**身份与日期。** 官方页面的可见日期为 2026-05-09，HTML 同时披露 `published_time/datePublished=2026-05-09T00:00:00Z`；换算为北京时间 08:00，落在本日报左闭右开窗口。它是 Baidu 的模型发布与技术博客，不是独立论文或复现实验。

**旧方案为何合理、约束如何改变。** 为每个规模单独预训练、让 rollout 与 update 同步共置、再按 SFT→混合 RL 串行后训练，最容易保持模型身份、样本 freshness 和故障边界。但多规模部署、长 horizon Agent RL 和多领域能力融合会分别带来重复训练成本、阶段空转与目标互相干扰。

**机制与状态所有权。** 官方说明把 ERNIE 5.0 的深度、expert capacity 与 Top-k sparsity 作为可采样的 sub-network matrix，再抽取 ERNIE 5.1；这使 sub-network configuration 成为模型 artifact identity，而不是 runtime 随意关闭层或专家。RL 部分以 RL Controller 为控制中心，将 training、inference、reward 与 agent loop 分开部署和扩缩，通过网络数据组件连接；trajectory 的 policy/router/precision lineage 仍必须在 trainer admission 前一致。后训练再把领域 experts 并行训练，通过 student on-policy samples 与 token-level reverse KL 做多教师能力合并；对于 high-entropy chat/creative tasks，官方明确保留 online RL，而不把 distillation 当作统一解。

**评价与边界。** 页面报告约 1/3 total parameters、约 1/2 active parameters、相对“同规模模型”约 6% pre-training compute、R3 的 K3 KL divergence 降低 50%，以及若干 Arena/AIME/GPQA 等结果；但对照模型、训练 token、硬件、precision、batch、并发、SLO、完整 ablation 与独立 evaluator 均未完整披露。因而这些数字只能作为厂商版本主张，不能被提升为通用成本或稳定性结论。FP8 operator 统一也不证明训推 bitwise 一致；异步解耦会新增 stale trajectory、queue backpressure、partial failure、跨池资源公平与 controller single-point-of-failure。模型规模固定、RL horizon 短或 freshness 比利用率更重要时，独立模型与同步共置仍是可验证的旧路径。

**Books 对读。** Ch21 已用 ERNIE 5.0 技术报告承载 elastic depth/width/sparsity 的模型边界；Ch31 已区分 on-policy distillation、teacher reliability、reverse-KL mode pressure 与 high-entropy 任务的替代分支；Ch33 已把 rollout service、trainer-owned policy epoch、reward/environment evidence、freshness admission、异步队列和 phase-aware resource scheduling 组织为同一控制链。此次发布提高这些路线已被整合到一个厂商模型生命周期的可信度，但没有提供足以改变现有 owner、fallback 或 evaluation contract 的新增公开证据，因此判定 `No Change — Existing Coverage`，不为了留下产品版本制造 Books diff。

### [Teaching Claude Why](https://alignment.anthropic.com/2026/teaching-claude-why/)

官方日期 May 8；不是以搜索或观察时间归属。Sonnet/Haiku-class 内部实验把正确拒绝行为过滤、改写高质量用户可见理由与 OOD difficult-advice 分开：针对 honeypot 的低失误未必迁移到更广自动审计；同 8k transcripts 的部分控制支持响应质量有差额，但不等于完整等算力。该节 extended thinking 关闭，理由不是内部 CoT。

另一分支先在 base 上做原则文档/正面故事的 SDF，再用 generic chat SFT 适配交互，检查 harmlessness RL 子集中的持久性；工具定义/system prompt 增强在固定 user prompt 下改善部分持出评测，不能被写成实际工具执行已安全。作者明确不解决鼓励 reward hacking 的奖励环境，有限 0% 不授开放环境安全、persona/prior 仍是解释假说，跨 scale/architecture、lab 与完整训练成本未建立通用保证。必要方法、主对照与直接限制见[本轮 A5](../_sources/daily-20260509/SUP_SOURCES_20261018.md#a5--p1-必要深入-source-prepared待非作者核验不预授books)。

Ch29 原文已有示教质量与分布漂移的原则，但没有这组固定行为、响应改写与跨情境训练的受限替代分支。因此在其少量高质量数据节加入两段，保留普通 verified demonstrations、原 checkpoint 和独立 OOD/旧能力审计作为回退；不重复改 Ch66。root 已独立核必要证据、逐字 PRE、实际两段/完整局部邻接/本人末注 POST；单项完成不等于本日日级验收。

### [Relay Buffer Independent Communication over Pooled HBM for Efficient MoE Inference on Ascend](https://arxiv.org/html/2605.06055v1)

精确 v1、同 DOI `arxiv.content/findable/registered` 与官方 EDT 公告下界合证 arXiv 公告日为 May 8，不使用 Created。必要 §3–6 支持 stable symmetric-HBM 地址域下 dispatch 直接到 expert window、combine 消费侧远端读取与紧凑 count/offset/address 协调；prefill 保显式规划、decode 收窄控制路径，不等于零状态、零通信或无同步。实际 serving 中 TTFT 降而 TPOT 从 30.10 到 31.31ms 变差，配置与内存测量不足不授通用收益/SLO。

Ch36 的 kernel 内 remote-memory 已明确预注册布局、peer/topology、lifetime、ordering/completion/failure；紧邻 Purlin/ThunderEP 已有布局协调、pull/push、consumer release、减少 relay 与 phase 分责，MoE 节还承载 count/offset 稳定地址与 combine 数值次序。因此判定具体 `No Change — Existing Coverage`，不为 Ascend 实例强写相同原理；root 已独立核必要原证及实际 owner 局部，6 分不因不写书下降。详见[本轮 A8/A10](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [Tackling the Data-Parallel Load Balancing Bottleneck in LLM Serving: Practical Online Routing at Scale](https://arxiv.org/html/2605.06113v1)

精确 v1、同 DOI 登记方/状态/registered 与官方公告下界合证 May 8。必要 §2–6 把同一 barrier 域的 resident work 最大值与总量之差写成目标，并得到 `F=Δ−G·max(0,Δ−m)` 的非对称 admission 分数；`m=M−L` 是实际 work 余量，不是空槽数。原文从空槽最多推 safe 不一般成立，不能照录；短 horizon 的 oracle 与部署 termination 预测分开，失配仍需无预测回退。

PD late-binding KV transfer、等待池、stateful proxy、状态陈旧及搜索都是代价。Azure 切片只含长输出与重载，scaling/sweep 用 oracle，主配置正文又有 96/144 NPU 计数冲突；不采精确扩展比、全局最优或生产 SLO 保证。Ch56 原 barrier/routing 主线只缺该可求值 solver 分支，因此已在其现论证后保存两段及纯 source note；必要 Source、写前与实际写后复核均已非作者通过，单项完成不等于本日日级验收。详见[本轮 A8/A10/A13](../_sources/daily-20260509/SUP_SOURCES_20261018.md)与[独核 R5](../_sources/daily-20260509/SUP_REVIEW_20261018.md#r5-用户暂停时的实际停点)。

### [FalconGEMM](https://arxiv.org/html/2605.06057v1)

精确 v1 的 LCMA 系数来自算法库；group-local 输入复用与就地 CombineH 减少额外片外中间往返，A/B 组合仍可物化。选择须结算 GEMM、加减、实际 bytes/带宽与数值开销；cost 单位必须相容，不移植原文跨 SM 无冲突的强保证。传统 FLOPs 归一的“超峰”不等物理超峰，GPU prefill 的离线权重组合与较小中间误差不授全模型质量/逐 bit/收敛等价。Ch49 原 shape 选择后新增该算法选择分支，保普通 GEMM 回退；root R6/R7 已核必要源、写前及实际一段/完整邻接/本人注写后。具体配置和未证边界见[补查 A12/A16](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [ResiHP](https://arxiv.org/html/2605.06374v1)

只有采用阻断跨文档 Attention 的 packing，固定 token 总量下的相关 Attention 成本才随各段平方和变化；再沿真实 pipeline DAG 与 warmup 预测健康迭代，将未解释异常交 validation。25% 是作者配置，不是通用阈值；profiling、模型失配、reconfiguration 与状态恢复付费。缺可信 state 仍回 committed iteration，短程注入故障/loss 重合不证明所有失败或最终等价；Table5/正文数字与延迟倍率方向不采用。Ch36 Failure 段补诊断层，root 实际写后指出并核实 block-diagonal 假设修复后通过，见[补查 A12/A16/A18](../_sources/daily-20260509/SUP_SOURCES_20261018.md)及[独核 R7](../_sources/daily-20260509/SUP_REVIEW_20261018.md)。

### [AgenticRAG: Agentic Retrieval for Enterprise Knowledge Bases](https://arxiv.org/html/2605.05538v1)

同一 proprietary search backend 的单轮与 agent 对照不等于等预算胜过全部 retriever；Pony 约6.9 gold docs 而整体约1.9时，coarse-to-fine 深读无法代替广度。Multiquery 减少调用但不保证 R@1 更高；总 token 含 thinking/tools/results，FinanceBench 约7.8倍单轮 token。15轮强制结束与摘要引用保留不证明证据充分或生产就绪。Ch76 已要求 depth、跨源 diversity、关键依赖和 downstream success/sufficiency 同时验收，并区分菜单出现、实际读取与使用，故5分具体已有覆盖；root 已实际核原域和该正文，不重复写书。详见[补查 A14/A19](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [MiA-Signature: Approximating Global Activation for Long-Context Understanding](https://arxiv.org/html/2605.06416v1)

同 backbone 的有限 narrative 对照支持 query-signature 改变检索，但把 signature/累积 evidence 全交回答器可能在 NarrativeQA/NovelHopQA 反退。离线摘要、额外编码与迭代更新付费；原 chunk 与派生 prior 分权，不采用全目标 submodular 保证、统一 FirstK 配方或开放域效果。Ch76 摘要树后补检索条件状态与回答 Context 分门验收，保原 query/chunk/hybrid 和必要证据 reader 退路。root R8/R9 已实际必要 Source/PRE/一段完整邻接及本人注 POST；不是整日通过。详见[补查 A14/A19](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [PoTAcc](https://arxiv.org/html/2605.06082v1)

精确v1 III-A/IV/V支持格式到执行产物的受限机制：最大shift、符号和零值决定真实PE中间宽度，int8转换后恢复PoT码还须修weight scale并同步bias，最后才packing给匹配consumer。prepare预置全部权重DMA需容量和准备时间；CPU fallback/搬运可反转收益。CNN accuracy不能给synthetic-weight ViT/DeiT测时补质量，idle-subtracted energy不是全板总能耗。Ch49 INT4例后补一段，保普通整数/浮点路径及完整任务/准备成本验收；root R8/R10已实际Source、逐字PRE与保存后完整新增/两侧/本人注POST通过。详见[补查A14/A21/A24](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [TokenStack](https://arxiv.org/html/2605.05639v1)

精确v1 §4–8的dense容量层/PIM计算层是容量-v-算力分域，不同于已有CD-PIM只分配计算bank；K按token/V按维度布局减少对应reduction，但广播、TSV、跨卡、反量化/转置不免费，K8V4不可逆。阈值代入、negative-reuse驱逐和层顺序口径矛盾不采用；Ramulator2/AttAcc/Python/CACTI模拟不等实芯，队列膝点939倍与自定p50门不是raw kernel或生产P99。Ch54新增受限分支，root R10/R13/R14必要Source、PRE、实际一段/完整两侧/本人注POST通过；未核代码或复现。详[补查A15/A25/A28](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [Teaching LLMs Program Semantics](https://arxiv.org/html/2605.06184v1)

精确v1 §3–6/Table1仅支持单Qwen3-8B/C/五property/500平衡任务。Bug-focused HTML traces配thinking提高violation发现，却把holds90.7降至78.0；同文件code-only不等tokens/compute，扩大语料混入组成变化，无显式去重不能授无污染。四inference reps不是四训练seed，binary verdict非formal witness；unparsed/timeout按固定分母保留。Ch28阶段QA后新增trace-CPT分支，root R10/R13/R14必要Source、PRE与实际正文/完整两侧/本人注POST通过。详[补查A17/A25/A28](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [OBLIQ-Bench](https://arxiv.org/html/2605.06235v1)

精确v1 §3–5把同reasoning reranker用于真实检索池与gold-injected诊断池，定位隐含风格/属性的“能给定后验证≠能先找到”。Gold注入不是线上收益/完备真值或全局上界，LLM标注、pool构造与verifier错误限制解释；改写还可抹风格，pool/rerank/属性抽取/搜索均计费，不宣dense无用。Ch76单向量域迁移后新增该反事实诊断，root R10/R13/R14必要Source/PRE/实际完整新增、两侧与本人注POST通过。详[补查A17/A26/A28](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [SIRA](https://arxiv.org/html/2605.06647v1)

精确v1 §3–4离线扩doc词、在线补query证据词，再按库DF筛并加权一次BM25；仅online要求DF>0，DF不认证相关或truth。Frozen共同Qwen有限结果缺组件独立消融/离线全语料预算，局部retrieval反退保留；answer-string coverage不与他文generated QA accuracy比较。Ch76词法总述后补接口并保原BM25/dense/hybrid，root R10/R13/R14必要Source/PRE/实际正文、完整两侧与本人注POST通过。详[补查A17/A26/A28](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [ROSE](https://arxiv.org/html/2605.06534v1)

精确v1 §4–6只采独立virtual KV/共享物理页与TTFT/TPOT双余量共服；回收rollout页须abort/reroute，不能把其他模型KV直接改属。稀疏权重差额依赖正确旧版本/shard，非bitwise或原子发布证明；额外借入GPU不等同预算优胜，页回收、重算、压缩/传输、profiling全费。Ch33 Rollout服务首段后补受限共服分支，保专用rollout/静态预留/完整快照及trainer freshness。root R10/R13/R16已实际必要Source/PRE/完整新增、两侧及本人注POST；详[补查A25](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [VideoRouter](https://arxiv.org/html/2605.05848v1)

精确v1主方法、评价与必要附录支持固定帧预算下global coverage/local detail取舍；64/128帧反转及mixed-query标注错误限制统一结论，前四层shadow classifier和三阶段训练不授任意视频或生产节省。Ch23既有CLASP类别路由→relevance/coverage双支、局部细节/跨事件粒度及Tempo分预算/非单调反侧已实际承载这些条件，故5分具体已有覆盖；不以新case强添冗余段。root R11/R17 Source与实际owner NC通过，详[补查A20/A27](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [EGA](https://arxiv.org/html/2605.05674v1)

精确v1 §3–5/A.3–A.4的零初始化残差与局部triplet hinge可让满足margin的样本停止直接压力，但累计参数路径仍能改变全域表示；Jacobian路径积分不是input Lipschitz或AdamW无条件OOD保证，方向安全是conjecture。ANN几何recall与语义检索分开，保Food/CIFAR反退及搜索/训练/重编码全费。Ch76 REZE后补该残差适配差额，保冻结向量回退；root R11/R17/R18实际Source/PRE/完整新增、两侧及本人注POST通过。详[补查A20/A27](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [DeScore](https://arxiv.org/html/2605.05922v1)

精确v1 §3–4/I：随机mask CoT发生在cold-start训练，数值读出也学视觉信号；部署本实验仍think→reward-query→score，不证明无解释同质替代/理由忠实。生成式RL辅以BT的消融支持保排序目标，不认证概率校准；teacher子维度非人类真值，motion/artifact弱项、tie人口和两阶段/CoT/额外读出费用保留。Ch31 teacher理由后新增该接口，root先纠正初稿训练-v-部署混用再R17 PRE/R18实际完整POST通过；详[补查A27](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [Active Task Selection](https://arxiv.org/html/2605.05703v1)

精确v1 §4–6及A.1.3–4/D.2/B.6在已知答案pool中用ensemble实际执行和单步EKI/Gaussian近似选任务，图实际学习仍可REINFORCE；非无标签EIG/全局最优。缓存仅同ensemble复用，selection费常高于train；benign与部分attack均值CI跨零。Ch82图/prompt训练后补预算先选哪些任务分支，保随机/代表采样、固定图与独立终局验收；root R12/R17/R18必要Source、PRE及完整实际POST通过。详[补查A18/A28](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [MASPO](https://arxiv.org/html/2605.06623v1)

精确v1 §3–4按拓扑轮换prompt搜索，peer改变后重比旧beam与当前best；local validity、直接后继lookahead与最终judge分账。judge偏好非因果credit，一跳更划算非普律；共同Gemini judge优化/评价、50未标任务/两拓扑/有限agent族及calls非全token成本限制解释。Ch82 Active Task后新增陈旧评分刷新，保版本/trace/全费与固定prompt退路；root R12/R17/R18必要Source/PRE/完整实际POST通过。详[补查A18/A28](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [Prologue](https://arxiv.org/html/2605.06137v1)

精确v1 §2–4把AR直接梯度经辅助codes更新，decoder仍用视觉codes；共享encoder仍有间接梯度，只有Post变体冻结已有visual路径。辅助prefix熵不免费，H(zp|zv)非负不能证明无坍缩或联合AR更容易；部分生成改善伴随重建反退，CFG schedule/compact AR/full AR/prefix全费。Ch23 VideoFlexTok后新增梯度分工，保two-stage codec/原codes及两侧验收；root R15/R20/R22必要受限Source/PRE/完整实际POST通过。详[补查A22/A31](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [wAR-Tok](https://arxiv.org/html/2605.06148v1)

精确v1 §4/Algorithm1与F.1–F.3只采用当前step target/proxy逐token logprob差、STE到tokenizer及aggregate proxy/重建分责；score forward stopgrad不是跨step冻结。Alg1 step7/8 target CE+联合更新与F.1固定随机target存在未解释冲突，不能自补两模型或训练阶段；target recipe、严格WGF/保证下降隔离，待作者勘误/配置/代码可消解才重开。Ch23 Prologue后保留这一接口及显式争议，不采用可执行固定/联合recipe；root R15/R20/R22受限Source/PRE/完整实际POST通过。详[补查A29/A31](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [NOVA](https://arxiv.org/html/2605.06298v1)

精确v1 §2–5/AppE必要域以共享INR base和每帧weight offset表示状态，IDM由相邻offset反推latent action，state演化/action forcing加性组合。Action仍混入亮度/位置，换内容可能带走坐标；joint predictor的OOD物理误差更低，故可编辑性不等物理准确性免费增强，也不是已标定真实控制量。只采MovingMNIST/PhyWorld，不采用WeatherBench科学应用、未闭loss记号或严格disentanglement。编码/render、IDM/GCM训练及每步生成全费；Ch25 Latent dynamics首段后补该状态对象分支，保普通latent/pixel dynamics、短horizon与真实观察。root R15/R20/R22必要Source/PRE/完整实际POST通过，详[补查A23/A32](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [FFDC-WAM](https://arxiv.org/html/2605.06222v1)

精确v1 §3–4/A.1在计划时保存future/动作/指令，执行中由小verifier对照真实新observation触发重规划。0.5是作者配置、人工corruption非所有失败真值，分数非校准概率或controller安全许可；缓存future tokens对更新观测的依赖尚需实现澄清，不授任意mask下KV精确复用。长chunk训练与基线不同，真机两任务成功改善却比短chunk有更多调用/时间，不能全归verifier或宣全费下降。Ch26 Action chunk首段后补该执行检查分支，保短chunk、状态重建、真实闭环与独立controller；root R15/R20/R22必要Source/PRE/完整实际POST通过，详[补查A23/A32](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [VLA-GSE](https://arxiv.org/html/2605.06175v1)

精确v1 §3–5/A.1/B受影响公式/D.4以SVD分共享always-on与专用top-k adapter；初始化补偿只在期待weight层成立，router依输入，非逐样本输出相同。B的期待积拆分还缺独立/条件统计假设，不采精确等梯度定理；trainable2.51%含action head而非全adapter，部分VLM retention仍低于base，D.4 FFT更快。SVD/router/搜索/训练/部署全费。Ch30新增这一条件adapter分支，root R19/R21/R23必要Source/PRE/实际完整POST通过，详[补查A30/A33](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [FREPix](https://arxiv.org/html/2605.06421v1)

精确v1 §3–4/B/E.4/F/G.1以正交Haar无损换state坐标、低高频异质schedule、主干预测低频/条件detail decoder及time-only训练权重分责；低频非全部semantic，population conditional mean不推出受限网络保全部原flow。ImageNet FID/IS与recall反退保留，单forward GFLOPs不含全ODE/CFG/训练，非实测端到端SLO。Ch24 flow路径局部新增分支，保普通pixel flow与独立质量/全费验收；root R19/R21/R23必要Source/PRE/实际完整POST通过，详[补查A30/A33](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [EMO](https://arxiv.org/html/2605.06663v1)

精确v1 §3–5/A.1–A.2/B.2–B.4/C支持训练整document pool/global-DP-batch balancing和部署validation子集选择分责；整文信息不自动逐prefix可得，也非未知query域自动识别。Fullmodel部分项低于baseline，Other小subset反退、shots/格式/selection/finetune和全部训练成本保留，少参数不证明latency/SLO。Ch21受限pool与global统计、条件子网及分域验收正文已承载本项最小命题，root R19/R21实际Source与完整owner具体NC通过，不因新实现强写同义段；详[补查A30/A33](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [ReasonMaxxer](https://arxiv.org/html/2605.06241v1)

精确v1必要方法与Table2支持固定离线mixed-support的signed CE，区分离线目标、teacher构造和额外on-policy探索；shifted并非零，不能从替teacher或全分歧构造证明RL无学习。Ch33 EG-GRPO后新增受限离线基线与全部数据/训练费，保在线探索和可靠verifier；root R24/R27/R28实际Source/PRE/完整POST通过。详[补查A34/A38](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [TurnGate](https://arxiv.org/html/2605.05630v1)

精确v1 gate读取prompt及已生成response，属于交付前而非生成前；经验t*和自定义F1不是真值或发布概率。Ch72隐藏stop边界后新增输入身份、训练/调用/阈值成本及误拒/漏检回退，不以局部F1授普遍安全。root R24/R27/R28必要Source/PRE与实际完整POST通过，详[补查A34/A38](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [SLAM](https://arxiv.org/html/2605.05443v1)

精确v1以key/文档身份HMAC加权选SAE方向子集，不是已实现±符号编码；hidden干预会改变logits，重放检测需要白盒结构/模型权限。固定prompt FPR、四candidate选择费及DIPPER反退限制解释，非零费语义不变或通用黑盒水印。Ch72重写水印后新增carrier与检测权限分责，root纠正初稿后R24/R27/R28实际Source/PRE/完整POST通过。详[补查A34/A38](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [MemReranker](https://arxiv.org/html/2605.06132v1)

精确v1 §3–5以ensemble偏好→BT相对分→归一软标签/BCE→InfoNCE形成排序读出；归一/sigmoid不证明跨query绝对概率校准。固定Top100/50排名非完整QA或memory真值，API失败分母、R@20/CMedQA反退及latency口径冲突/全费保留。Ch76现有offline utility pairwise proxy→soft分布蒸馏embedding、history consumer版本与固定池-v-真实召回/答案正文已承担最小条件；Ch66保BT尺度测量职责，不在Ch77重复。root R26/R32实际Source/具体NC通过，5分保持。详[补查A36/A41](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [Rubrics](https://arxiv.org/html/2605.06283v1)

精确v1 §3–7/A在两个英语域/两模型比较analytic/holistic、示例/调用粒度及表面edit；criteria、gold选择与预算混杂不授analytic稳定更好。Kendall/Pareto/yes-ratio测量对象不同，自身一致非对人效度；更多例子/复杂判据可反退，专家/调用/统计范围保留。Ch66已有criterion逐条判分与最终聚合分责、独立校准及generator×reader×domain/外部效度完整段，故具体NC而非再写新case。root R26/R32实际Source/NC通过，5分保持，详[补查A36/A41](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [Litespark](https://arxiv.org/html/2605.06485v1)

精确v1 §4–7/A仅采用int8三值执行容器、row activation quant/int32积累与dispatch的取舍；2B int8约2GB与556MB冲突，14×/L3/RSS及unsigned×signed的缺失zero-point recipe不采用。附录V2 prefill反退、decode接近和单模型/未匹配总费用保留；整数dot仍有硬件乘法。Ch49现有三值pack更紧但decode更慢、较宽码/实际consumer/完整驻留及质量分账已承载本机制，故5分新验证具体NC。root R29/R33 Source/实际owner通过，详[补查A37/A42](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [VISD](https://arxiv.org/html/2605.06094v1)

精确v1 §3–4/B/C/D/E/G以EMA teacher在同completion重放hidden answer/evidence/feedback，top16并sample支持内分别归一，正weight仅保advantage符号；不保参数梯度方向、无偏全词表目标或因果credit。Judge不见原video frames，不能认证视觉真值；EMA gradnorm与topK切片反侧、step非全费及评测帧数身份保留。Ch33现有Verifier方向/Privileged Teacher调幅完整两段已承担最小分责与teacher bias/全费/回退，不因video case重复正文；R30/R33实际Source/NC通过。详[补查A39/A42](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [Automated Safety is Harder Than You Think](https://arxiv.org/html/2605.06390v1)

精确v1 §2–5为条件概念反证：即使non-scheming代理，也仍面对可测proxy到真实安全的解释、跨报告相关不确定性聚合；不是已测事故率或自动安全普遍不可能。少选论文转移selection judgment，容易子任务的decomposition仍有用，BBN仅建议；共享研究假设与reviewer可能共错，量不等独立证据。Ch66目标→spec→scorer→aggregation链、外部效度、共享盲区与panel稳定-v-独立发现完整局部已承担最小条件，5分具体NC；root R30/R33实际Source/NC通过。详[补查A39/A42](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [TextPro-SLM](https://arxiv.org/html/2605.05927v1)

精确v1 §3–5/A–F区分ASR decoder内容流与mel重构声学流，再pool/分组交错给LLM；N/T两词表不作严格逐词对齐，重构不证明纯韵律解耦。ASR-only同骨干基线、负面任务/绝对质量、平均gap抵消、全部预训练/合成/训练费及等待整句边界保留，不授TTS或实时流式。Ch23语义anchor目标后补双流来源/训练责任，不重写已有字段监督；root R26/R34/R36实际Source/PRE/完整POST通过。详[补查A36/A43](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [Metonymy vision models](https://arxiv.org/html/2605.06095v1)

精确v1 §3–6/A/F/G支持late mask读出不能撤销全图backbone混入，而early各层hard attention隔离值通路；STE反向近似非soft forward零泄漏。Stage1 mask仍由全图生成，global ensemble不能继承纯local承诺；PS/MPPO不等因果或真实mask边界，分类反退/两阶段成本保留。Ch23 f-CBM后新增mask生效层条件，root R30/R34/R36实际Source/PRE/完整POST通过。详[补查A39/A43](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [AEN-SAE](https://arxiv.org/html/2605.05341v1)

精确v1 §2–5/A.1–3/B/C只采固定D/非负权重、正L2下最优非负code的强凸/稳定对象，不移植到联合训练/浅层encoder/真实语义。Oracle活动权重与极限不由有限clip满足；正文§3/4频繁feature罚权方向冲突隔离，不写recipe。低L0 dead反退和EV损伤、EMA/搜索/全费保留，Ch5 sparsemax SAE后新增这份稳定性分责。root R29/R34/R36实际Source/PRE/完整POST通过，详[补查A37/A43](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [UniSD](https://arxiv.org/html/2605.06597v1)

精确v1 §2–3.5/A/B/C/G使多context agreement只调主teacher蒸馏权重、EMA随step变化，非独立teacher真值投票；对汇聚scalar divergence设cap非参数gradnorm裁剪。正负context可含gold，非零监督；视图非单调/保持指标与任务反退、所有视图/rollout费保留，JSD/PPL非完整旧能力证书。Ch29 short/full-context后补条件分支与可靠teacher/verified-target回退，root R29/R34/R36实际Source/PRE/完整POST通过。详[补查A37/A44](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [Efficient Pre-Training with Token Superposition](https://arxiv.org/pdf/2605.06546v1)

精确v1 PDF §3–7/A/C/D/E，页4–6/9/10/20实际视觉核验：连续s-token embedding平均、同主头对下一bag各出现位置平均CE，保两端表示再恢复标准NTP；粗阶段丢序不能直接正常采样，重复词与loss常数条件保留。8/64B200、DCLM/混合语料等配置下更多data换作者等FLOPs质量，不是同data免费收益；同data baseline更低loss、E表任务反退与Figure3/表s8-s6冲突不泛化。单run/较大模型未全调、恢复/数据/搜索全费保留。Ch28 future-token后新增主目标阶段切换，root R31/R34/R36实际Source/PRE/完整POST通过，详[补查A40/A44](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [Conditional Diffusion Under Linear Constraints](https://arxiv.org/html/2605.05387v1)

精确v1 §2–4/Alg1/D与§5假设声明支持满行秩无噪声测量的normal score解析、未知conditional tangent仍有错配；在noisy normal切片的有限BAOAB后逆过程不是exact posterior，理想slice也不消原条件偏差。只采机制分责，不转写未完整逐证KL保证；Gaussian mixture/entropy/敏感性/间隔与learned-score/离散误差分开。三256²数据集LPIPS/FID非coverage证书，100有效NFE依赖缓存并非同walltime，未披露hardware/precision/batch等不补造；全部先验/投影/调用费保留。Ch24 InpaintSLat后新增测量nullspace分责，root R31/R34/R35实际Source/PRE/完整POST通过，详[补查A40/A44](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

### [Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key](https://arxiv.org/html/2605.06638v1)

精确v1 §3–5/A/C–F/H/I采用固定可核proof-tree题目下depth/expressiveness/课程分轴；Z3每配置1000题审计不证明全shortcut消失。Qwen3-4B/8B、8B200/G8/8192下主T是首次验证90%Pass@1的step数，FLOPs/token/GPU-h指数不同；有限深度单seed拟合非普遍多项式定律。固定D/约100step仍混结构/token，quantifier/reuse等未全分离，Avg@8非Pass@8、32768 OOD预算下仍有深度边界；题目/验证/全部生成更新费保留。Ch33课程职责后补固定生成规则分支，root R31/R34/R36实际Source/PRE/完整POST通过，详[补查A40/A44](../_sources/daily-20260509/SUP_SOURCES_20261018.md)。

## 5. 缺口与下一步

- **普通待办：无。** 用户明确恢复后仅接[本日 A13](../_sources/daily-20260509/SUP_SOURCES_20261018.md#a13--暂停checkpoint用户明确要求作者ownership释放)差额，扫描/有限筛选、40新增必要Source、31整合/9具体NC、完整六部分DAY R37及完成态实际FINAL R38均闭合；全部窄位释放。51题摘不是全文队列，不扩新发现，本日结束，不重研究层。
- **六资格终态隔离：** [Hidden Coalitions 06696](https://arxiv.org/abs/2605.06696v1)、[MidSteer 05220](https://arxiv.org/abs/2605.05220v1)、[Attribution 05285](https://arxiv.org/abs/2605.05285v1)、[Governed Metaprogramming 05248](https://arxiv.org/abs/2605.05248v1)、[MACS 05225](https://arxiv.org/abs/2605.05225v1)与[Internalizing outcome/process 05226](https://arxiv.org/abs/2605.05226v1)，精确身份与有限可得原始入口已按A24/A35、root R25核回。早提交/DOI区间不能唯一绑定May08，必要更早原稿公开日仍缺；现不计候选、完整Source、Books或无遗漏证据。05220的作者repo/OpenReview归属已纠正，旧串位透明保留；只在取得具名dated原稿/官方归档或必要公开说明后定点重开。

- **后续触发：** 若获得本窗受阻机构入口的官方历史归档，只重开对应来源与日期；普通Books待办0，完成状态不扩大已有证据权限。
**终态保留项：** Google AI、OpenAI、Moonshot 与 MiMo 的历史日级目录/分页停止点未完整恢复；这些限制不支持正面证据、Books 或无遗漏断言。
**定点重开条件：** 若取得目标窗口的官方归档快照、带精确发布日期的官方索引
或可唯一定位到本窗的原始发布链接，只重开相应来源与 Source Family，不重跑已闭合的 ERNIE 证据链。

## 6. 复核

本轮补查复核者：`/root`（非本报告作者）。全部40项新增必要Source、31项实际Books完整正文/两侧/本人注POST与9项具体NC已分批通过，实际范围、代表排除抽检及纠错见[独核R1–R36](../_sources/daily-20260509/SUP_REVIEW_20261018.md)；六日期资格身份修复/有限停止经R25通过，只是隔离终态而非正面Source。原ERNIE整行/日期评分、原小时窗与连续旧§4已机器逐字比较保留，本轮V3/本地引用/限定diff检查继续执行，不能替代语义核验。

**本轮日级结论：通过。** 非作者root已实际连续读完整六部分并独立重跑V3、41行/41证据URL守恒、91本地引用及原冻结/限定两层diff检查，见R37；31新实际整合/9新具体NC、六资格与历史来源限制均按实际层验收。2026-10-18T22:02:17+08:00保存完成态已由非作者root实际FINAL R38读回通过，无剩余普通待办；不重Source/PRE/POST，也不把限制算全Coverage或Evidence通过。以下为旧轮有效复核。

复核者：`/root`（非作者 fresh-context 复核）；详见 [V3 独立终审](../_sources/daily-20260509/V3_INDEPENDENT_FINAL_AUDIT.md)。

结论：通过

窗口、候选身份、评分、证据边界和 `No Change — Existing Coverage` 均已逐项核验。`validate_research.py`、
本地 Markdown 链接与 `git diff --check` 通过；机器检查未被用来替代语义判断。
