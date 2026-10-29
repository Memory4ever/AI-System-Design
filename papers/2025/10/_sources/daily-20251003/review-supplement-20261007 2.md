# Oct03 补查首批独立校准

记录时刻：2026-10-07T21:47:25+08:00。当前补查作者为用户指定的 Helmholtz；复核者为本线程 Codex / Huygens，未参与本轮作者包写入。原日报作者也是 Huygens，因此本文**只独立审 Helmholtz 的新增补查**，不重新认证自己的旧正文；原 root FIRST / Euler DAY 仅按其已核、未变范围复用。

本轮 fresh 读取 main 的 AGENTS、Research/Report 当前合同、Sources 使用说明/每日14源/arXiv历史入口、Prompt、ROADMAP、相关 State 路由及 Oct03 README/独立停点。只处理补充自然日 **2025-10-02**，不移动原窗口、旧候选日期或评分。未使用 catchup，未展开其他日期/Weekly，未执行 Git 写操作或 model override。

## 1. 裁决与精确返修

**FIRST-CALIBRATION: CHANGES REQUIRED，限 R1 两项误关闭；不是 DAY。** 实际完成18/18新增精确v1完整题摘校准，支持原15项保留潜力，重开2项，支持1项关闭，即 **17潜力 / 1关闭**。这不是17个确定当日候选；正式候选、评分、正面Evidence采用与Books提案均仍为0。

作者包：[首批快照](first-calibration-supplement-20261007.md)、[当前作者停点](supplement-20261007.md)、[当前日报](../../03/README.md)。27请求首批快照与后续61请求总执行分开，不能互相覆盖。

### R1. 两项关闭重开，其他有效判断不推倒

- **2510.02157v1 VIS-ReAct：重开贡献潜力，唯一拟归属 AGENT-CONTEXT。** 旧判断把它压成分析→改写分工。[精确v1 §3、§4、§5](https://arxiv.org/html/2510.02157v1)实际以程序比较相邻工作区，提取cluster/highlight/note变化，再联合旧报告、变化和当前工作区规划局部修改；§5还报告直接让LLM比较工作区不可靠、连续局部修改会积累杂乱、意图是否吻合仍未知。原有整篇重生成或只送变化会分别造成无关改写/上下文丢失 → 显式变化提取与保留上下文的更新接口 → 应重新考虑增量输入和局部编辑范围。35对工作区、单模型/单数据集的局部评价不能授通用状态一致性或用户真实意图保证。当前arXiv提交为BJT10/03；这只限制该事件日期，不关闭贡献。
- **2510.01651v1 LadderMoE：重开贡献潜力，唯一拟归属 MODEL-MOE。** [精确v1 §3.2、§5.1、§5.4–5.5](https://arxiv.org/html/2510.01651v1)给出中间层ladder-side MoE adapter：class token与平均池化图像token形成各adapter路由信号，top-k专家混合后经可学习gate逐层融合，冻结CLIP骨干而训练adapter/router/gate/decoder。固定骨干的异质输入适配 → 侧路稀疏专家及层间融合 → 有核验参数更新位置和专家分配的局部设计增量，不能称未辨识新增adapter机制。OSF掩码训练与专家数消融不自动证明资源收益；没有等预算PEFT对照或通用吞吐保证，稀有类别经过样本过滤，专家激活非均匀。仅保留这条机制潜力，不把金文识别精度外推为基础模型普遍改进。

作者只需修正这两项身份处置、总数及关联日期缺口，不新增batch、不重审18或宽库存。同类错误检查只限本包已明确关闭的集合，MIMIC未因此自动重开。

### R2. 必要核心的中心争议和采用边界

这是作者停点已列的普通核心工作，不是新外部故障；作者目前没有采用以下强结论，故不把它们误报为已发布的正面结论错误。DAY前需把实际处理写回作者记录，可复用本文定点证据，不要求重复全文。

- **PSR 2510.01270v1：保留潜力，隔离预测器和统一防御强说法。** [§3.2、§4.1–4.5、Limitations](https://arxiv.org/html/2510.01270v1)中的training-free仅指基础LLM；MLP另需训练。最小轮数公式与“记录首次触发harmful flag”的标签叙述并不等同，不能直接授最优安全轮数。§4.2称N=8所有攻击低于30%，而Table2的Llama3.1-8B-Instruct / CodeChameleon为70.71%；保留冲突，不能用概括文字消去反侧。二元自评、漏判、推理开销及测试攻击范围均限制采用；不声明已验证adaptive防御。这里只核上述争议，未核代码/复现。
- **Support Basis 2510.01643v1：保留潜力，通用有符号输入理论保证暂缓采用。** [精确v1 Theorem1.4/1.5、D.3–D.4、G.1、I.1/I.5 Eq44](https://arxiv.org/html/2510.01643v1)区分独立sub-Gaussian单阈值与多阈值/sketch路线，后者误差和运行时依赖B、epsilon等，不能授无条件固定精度近线性。I.1的b为最小绝对entry，Eq44却用exp(b²)下界归一化项：取n=2,d=1、Q两行均1、K两行均-2，则b=1，每行D=2exp(-2)，不是至少2exp(1)。这是复核者对该证明步骤的反例，不是原作者结论，也不证明整篇所有路线失效。G.1还出现bucketing epsilon<0、后文使用正参数的冲突。当前只核官方v1 HTML；需作者明确隔离，若拟正面采用该通用定理，再定点对照PDF/澄清，不能以日期未知把争议删去。

## 2. 全部18份题摘的独立准入判断

均实际读本地精确v1题名、完整摘要、当前Comments及可见版本史；未看到这些页面中的明确撤回/纠错说明，不以此证明完整版本史没有说明。后出版本不覆盖历史v1。下表P指值得核验的贡献潜力，C指本项目关闭；均不是评分或Evidence Gate。

| 身份及原题摘 | 校准 | 最小增量与待核选择 / 唯一拟owner |
| --- | --- | --- |
| [2510.01161v1 M2PO](supplement-20261007/abs-2510.01161v1.txt) | P保持 | 过旧RL rollout失稳 → importance weight第二矩约束/极端token控制 → stale数据更新条件；TRAIN-PPO，不授256更新的生产保证 |
| [2510.01270v1 PSR](supplement-20261007/abs-2510.01270v1.txt) | P保持 | 生成中反思/回退与轮数分配，PLATFORM-SECURITY；强命题按R2隔离 |
| [2510.01336v1 HiSpec](supplement-20261007/abs-2510.01336v1.txt) | P保持 | target验证瓶颈 → early-exit中间验证和跨阶段状态复用 → 验证层/回滚成本选择；INFER-SPECULATIVE-DECODING |
| [2510.01394v1 Optimal Stopping](supplement-20261007/abs-2510.01394v1.txt) | P保持 | 固定Best-of-N → 未知reward分布下Pandora/UCB停止与归一化 → 继续生成的条件；INFER-SCHEDULING，不混成请求SLO实证 |
| [2510.01624v1 Quagmires](supplement-20261007/abs-2510.01624v1.txt) | P保持 | SFT分数不可靠地指示RL起点 → 数据/长度/重复设置反侧与代理指标 → 起点筛选；TRAIN-SFT，不因局部任务关闭 |
| [2510.01643v1 Support Basis](supplement-20261007/abs-2510.01643v1.txt) | P保持 | 稀疏大项与稠密小项分解/多阈值理论放宽路线，MODEL-SELF-ATTENTION；通用保证按R2隔离 |
| [2510.01645v1 Privacy](supplement-20261007/abs-2510.01645v1.txt) | P保持 | 训练记忆中心的隐私评价 → 生命周期风险/研究分布盲区 → context、外部输出、属性推断的威胁覆盖；PLATFORM-SECURITY |
| [2510.01832v1 SCRIBES](supplement-20261007/abs-2510.01832v1.txt) | P保持 | 每页LLM抽取 → layout信号驱动可复用脚本/迭代标签 → 成本摊销与结构漂移；TRAIN-DATA |
| [2510.01857v1 IRL Reward](supplement-20261007/abs-2510.01857v1.txt) | P保持 | 模仿expert风格 → adversarial IRL token reward及训练/重排复用 → 过程正确性辨识；TRAIN-RLHF，限v1评价 |
| [2510.01994v1 CLAST](supplement-20261007/abs-2510.01994v1.txt) | P保持 | 示例改写破坏可执行性 → 切分与AST受限回写 → 可读性/语义效力双约束；AGENT-CONTEXT |
| [2510.02228v1 xLSTM](supplement-20261007/abs-2510.02228v1.txt) | P保持 | 训练FLOP单视角 → scaling/context/部署耦合比较 → recurrent与Transformer选择；MODEL-LONG-CONTEXT，不借新版加强结论 |
| [2510.02324v1 CASAL](supplement-20261007/abs-2510.02324v1.txt) | P保持 | 在线activation干预 → 单层steering摊销入权重 → 在线成本与拒答边界；TRAIN-SFT，数字待可比条件 |
| [2510.02345v1 Dynamic MoE](supplement-20261007/abs-2510.02345v1.txt) | P保持 | 负载/冗余/通信约束 → 聚类、shared base/低秩residual、层级路由和异精度offload → 联合取舍；MODEL-MOE |
| [2510.02287v1 Action Video](supplement-20261007/abs-2510.02287v1.txt) | P保持 | 文本条件不足 → 多模态动作对齐/保留与轨迹正则 → 条件控制及漂移；MULTIMODAL-WORLD-MODELS，不授物理安全 |
| [2510.02373v1 A-MemGuard](supplement-20261007/abs-2510.02373v1.txt) | P保持 | 条件污染和回写放大 → 多记忆共识/独立lesson memory → 信任及错误反馈边界；AGENT-MEMORY |
| [2510.01635v1 MIMIC](supplement-20261007/abs-2510.01635v1.txt) | C保持 | 完整题摘给出persona引导playstyle多样性与游戏覆盖/完成率，未辨识超过此策略组合的新执行机制或有成立条件的质量/资源边界；不以游戏领域、小模型或日期未知关闭 |
| [2510.01651v1 LadderMoE](supplement-20261007/abs-2510.01651v1.txt) | C→P | 按R1重开，MODEL-MOE；仅冻结骨干侧路专家路由/融合增量 |
| [2510.02157v1 VIS-ReAct](supplement-20261007/abs-2510.02157v1.txt) | C→P | 按R1重开，AGENT-CONTEXT；仅增量输入与局部更新边界 |

17潜力中02228/02287/02157当前arXiv提交已是BJT10/03，故该事件不可能在补充10/02内；如恢复更早作者公开稿，仅核那个事件。其余14项首公开具体日仍未知，LadderMoE提交BJT10/02也不能替代公告日。Advanced年月公告与submitted都不授日级准入，未知日期不使P变C/Q。

## 3. 必要安全/设计反侧与分层抽样

本轮另实际读9篇精确v1的必要章节，不称9份候选Evidence完成。PSR/Support Basis见R2；LadderMoE/VIS-ReAct见R1。其余定点边界：

| 精确版本与实际位置 | 支持的准入边界 / 未证明的内容 |
| --- | --- |
| [2510.01645v1 Privacy §3.1–3.5、§4.1–4.3](https://arxiv.org/html/2510.01645v1) | 训练记忆、服务存储、RAG/Agent输入输出、属性推断/聚合是不同风险面；1322篇为选定8类会议和GPT4.1分类，含小样本人核，不等真实威胁发生率。仅支持评价盲区潜力；未独立核各新闻/法律/服务政策或采纳“预训练泄漏无重大风险”的概括 |
| [2510.01624v1 Quagmires §2.1–2.2、§3.1–3.2、§4.1及§4.2相关段](https://arxiv.org/html/2510.01624v1) | 数据量/epoch/LR与RL最佳checkpoint选择需区分；重复训练例不全是等计算对照。Pass大k/held-out loss的预测相关不等因果或普遍规则；保留数据配方影响后续RL的局部反侧 |
| [2510.02373v1 A-MemGuard §3.2、§4.1–4.2、§5.1–5.3及§5.4相关表](https://arxiv.org/html/2510.02373v1) | 假设少数污染、多数可信；共识不等独立真值，异常路径写lesson仍有误反馈风险。Table1 ASRr与ASRt、Table2间接攻击及Table3效用分别读，95%不是全部指标/攻击总体保证；未授自适应串谋安全 |
| [2510.01336v1 HiSpec §3.1–3.3、Algorithm1/2、§4–§6](https://arxiv.org/html/2510.01336v1) | 中间接受先缓冲，最终提交仍经target验证；拒绝后剪KV/hidden state及后缀，不能把周期验证误述为跳过最终验证。要求已训练的early-exit层，4×H100/HF及局部负载结果不等服务吞吐；TopPredictions算法本身不授任意随机采样分布等价 |
| [2510.01994v1 CLAST §III-A/B、§IV、§V-A/ V-C、§VII](https://arxiv.org/html/2510.01994v1) | LLM只提供注释/名称再AST受限回写，完整代码改写会破坏测试；效力保持的RQ1为4开源Java项目的两类各500测试，工业项目不在该RQ1。切分含方法名写入启发式，局部四指标保持不等所有程序语义证明；保留必要输入质量反侧 |

分层不是按字母抽样凑数：题摘潜力层15/15全部核，明确贡献关闭层3/3全部核，其中2项以核心消歧纠正、1项关闭保持；安全/设计/理论层按上述9项定点实际核。宽入口层只核查询语义、ID和停止：例如world宽匹配不等world-model主题，未把340库存余项称逐一贡献关闭。旧标题范围关闭与旧94/23不重读或重新授通过；本轮没有另起库存筛选队列。

## 4. 来源与真实执行范围校准

独立解析61份request记录并核原响应字节/SHA256：**59个200、2个403，无transport failure**，起止为`2026-10-07T12:05:32.204719+00:00`至`2026-10-07T12:53:51.259600+00:00`。403为具名OpenAI入口；成功下载、抽取与题名库存不当阅读完成。

八份Advanced原响应独立解析各50个abs身份、全部第一页，真实URL为Computer Science/cross-list、all字段、from2025-10/to2025-11、announced_date_first升序、size50（首屏等效start0）。表单只支持年月，回显区间Oct1–Nov30。Next存在而未执行后页是有界停止，不是故障；没有使用catchup或API错误授阴性。

| 查询原响应 | 第50身份 / 实际停止 |
| --- | --- |
| [language model](supplement-20261007/advanced-language-start0.raw) | 2510.00276 / 首50 |
| [mixture of experts](supplement-20261007/advanced-moe-start0.raw) | 2510.09594 / 首50 |
| [LLM inference](supplement-20261007/advanced-systems-start0.raw) | 2510.02324 / 首50 |
| [reinforcement learning language](supplement-20261007/advanced-rl-start0.raw) | 2510.02212 / 首50 |
| [vision language](supplement-20261007/advanced-multimodal-start0.raw) | 2510.01049 / 首50 |
| [world model宽匹配](supplement-20261007/advanced-world-start0.raw) | 2510.00694 / 首50，未逐项关闭 |
| [world model phrase](supplement-20261007/advanced-world-phrase-start0.raw) | 2510.15041 / 首50，相关性收窄 |
| [tool/RAG/memory phrase](supplement-20261007/advanced-agent-phrase-start0.raw) | 2510.02995 / 首50，三个OR短语 |

400出现/340唯一、30旧身份/310旧池外，与[机械库存](supplement-20261007/advanced-inventory-eight.json)的身份和old_identity标记一致。这里旧池是本日8个Atom原件的**106发现身份**，不是94完整题摘：30交集里28在94题摘，另2510.01571与2510.02567只在旧发现池。不得把这2项仅有身份重叠说成已读题摘/已审重复；不因此重开其旧范围判断或跨日扫池。

已对照日报14源的有限执行/停止叙述；未本轮重抓整机构，未授十四源完整召回。各源历史缺段、浏览器不可用、Seed85/94可见差额与有界后页未读分别保留。Google Pubs年度关键词首15/37和文本日期0/0不等按日无事件；OpenAI/Meta/Qwen/MiniMax辅助搜索空或当前页不等历史无事件。作者仍须做同身份必要日期恢复、R1/R2与实际来源差额的具名闭合；本轮未收到作者DAY READY，不能提前把普通待办置0。

**新增PASTA artifact差额已核：** 实际解析[Kaggle卡原响应](supplement-20261007/google-pasta-dataset.raw)JSON-LD的identifier6267952、version1、引用2412.10419、dateModified2024-12-09、CC BY-SA4.0及五轮/16图/Gemini1.5Flash描述。modified/缩略图日期都不证明首次公开，未辨识Oct2新版本；支持作者不凭传播或卡日期制造新候选。未下载数据或核运行/法律合规。旧PASTA核心与RBAC未变结论仅复用其独立有效范围，不由原作者本人重新认证；write-up公开日仍不能用事故时间替代。

复核者新增外部读取仅为上述9个精确v1官方HTML及其指定章节，经web工具读取；没有声称另存9份HTTP原件或独立HTTP状态/hash。公式反例为本地算术核查，exp(-2)=0.1353352832、exp(1)=2.7182818285；不是论文实验复现。其余来源事实由作者已保存原件和请求记录定点核，不补造查询或分页。

## 5. 下一步与写入范围

1. Helmholtz落实R1：两项C→P，同步17P/1C及14未知日/3当前arXiv事件晚于补充日，旧候选日期/窗口/评分不动。
2. 在作者必要核心记录中落实R2以及§3采用边界；安全/理论争议不能外部包装，也不要求为未采用的所有数字重读全部附件。
3. 仅对14个未知日潜力作必要公开事件恢复；另外3个当前arXiv事件已经晚于补充日，只有出现同身份更早作者稿线索才恢复那个事件，不强制漫查更早全网。完成普通工作后给非作者DAY READY。若当日候选成立，按当前合同处理其评分/证据和具体Books比较，准备好的单篇立即交root，不等待无关项。
4. 后续复核只核实际返修及具名来源/日期差额，不重审18/旧94/23或宽340。原普通工作未完成时不给DAY；终态缺口不授无遗漏、正面Evidence或Books。

当前没有日级准入且经独立证据复核可写入的单篇Books差额，**Books提案/写入0**；以上Stable Node仅是潜力路由，不是已做正文比较/已有覆盖。Support Basis中心争议可先交root作为MODEL-SELF-ATTENTION的禁止强采用证据，不自行改书。

本线程只新增本sidecar；作者README/原件/作者包、旧独立文件、Books、State、合同、ROADMAP、索引均不写。运行前保护574个文件，写入前hash复核仅发现共享LEARNING_STATE的并行变化，未回退或修改；所有受保护Oct03作者材料、Books和其他合同文件均未变。静态/链接与写后范围检查另记下方，机器通过不代替FIRST返修或DAY。

### 写后核：2026-10-07T21:52:32+08:00

当前合同bundle、Sources registry、Stable Node IDs、作者日报V3、sidecar Markdown/本地链接/尾空白/NUL检查均无错误。对本新增文件作no-index限定diff-check，无错误输出；返回1表示相对空文件有新增内容，不冒充无diff。实际读回新增正文和返修范围。

574文件写后hash对比：受保护的Oct03 README/作者包/原件/旧独立记录和其他合同均未变；本日_sources新增文件只有本sidecar。共享LEARNING_STATE及`books/part-03-multimodal-world-models/23-multimodal-representation.md`发生并行变化，均非本线程写入、未回退，不声称共享文件全局不变。检查只读，未stage/commit/push；当前停点仍为R1作者修正与R2/具名日期普通工作，**未授DAY**。

### 接续核：2026-10-07T22:18:53+08:00

按用户最新授权只接续实际变化，fresh读取当前AGENTS、Research/Report合同、Sources使用说明/每日/arXiv、Prompt、ROADMAP和相关State路由，未加载其他日期候选池。实际读回作者补查记录，并定点检查首批包、日报和本日停点：作者记录仍为15P/3C，明确“尚未作者READY或DAY”；R1的17P/1C、R2中心争议/必要采用边界和具名日期恢复尚未写回。旧停点的历史完成不能替代本轮READY，State中的ownership分配也不计完成。

因此本次没有新增差额可授写后通过，沿用上述18题摘/9必要核心的有效复核范围，不重新读全批、不另起来源扫描。仍为**FIRST返修待作者落实，非DAY**；未执行的准入同步、必要边界记录和日期恢复继续作为普通待办，不能改称外部故障。作者具名READY后只核这些实际差额及整日剩余工作；若可授DAY，再独立读回作者实际完成态、V3、链接和限定变化范围。未知日期/来源材料只在必要恢复实际执行并留下身份、入口及停止事实后按合同安全隔离，不调整旧日期/窗口/评分，不将340库存转为队列。此次只追加本review，作者文件及共享Books/State/index不写。
