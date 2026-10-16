# Apr30 补充线索：root 定点核验

root 不是本日报作者。仅接手从 May2 的旧有限发现中确定归属 Apr30 的前五个具名身份；其余由 Godel/Newton 处理，不接管整日报。每日报告仍独立，日期跨日只交接精确身份及实际归属，不沿用别日来源成功。已重读 AGENTS、适用研究/报告合同、来源日组、Prompt、ROADMAP 与本日停点。

## 1. 新遗漏的精确身份与原件

May2 [root 独核 §10](../daily-20250502/REPAIR_REVIEW_20261016.md)一次限定 50 个精确 DOI 的完整官方回应，已逐项核身份、arxiv.content/findable、唯一 v1 Submitted 与 registered；全部 v1 公告联合界在 Apr30。五个 20493/20752/20835/20922/20964 已在本日处理，另外 45 个是现在明确归到本日的遗漏线索，不是 45 个自动准入/评分或深入审阅任务。不能在已知这些可执行工作后提前签本日完成。

root 一次 GET `https://export.arxiv.org/api/query`，`id_list` 为该 45 个精确 ID 加 v1，`max_results=50`；不查询 catchup、月前缀或全分类。HTTP200/exit0，完整 [Atom](ROOT_REVIEW_ABS45_20261016.raw) / [headers](ROOT_REVIEW_ABS45_20261016.headers.raw) 保存；45 entries/total45、45 唯一且逐项带 v1，恰等于上述50减五个已处理身份，摘要无缺失。SHA256 为 `0163ae619948a3573c3113b49c7b7ac34efb9d637f779b4b2d64fdf0517d46e9`。`published/updated` 与 v1 Submitted 相同，绝不改称公告日；公告日来自此前联合界，不来自 Atom 字段名。

45 个 ID 可以从该 Atom 完整重建；已分工 root 只审 20434/20437/20456/20459/20462，Godel 处理其余40。root 实际读这五份完整 v1 题摘/作者/comments，另单次取得各精确 v1 HTML 到 `/tmp/ai-system-{arcs,galore2,assd,sas,tamo}-<ID>v1.html`，五请求均 exit0。下文逐项说明必要阅读域，不以下载完成等同阅读。未核实现、跑实验或读未列附件。

## 2. ARCS20434：准入需收窄，拟贡献前关闭

实际读精确 v1 §3～6 全部机制/评价/限制及 Tables1～3。v1 只有 RAG→分解→执行→反馈的成熟组合、三种节点/提示 tier 与最多五轮修复；“MDP”形式化不建立新的学习或搜索保证。后版题摘的终止/单调/成本保证不能回填：v1 没有相应定理或预算界。§4.3 的 prompt 特异度/一致性变量只是概念定义，未提供可核阈值或对应隔离实验。

表2确有更大 tier 退步，但同时改变分解、检索、调用和循环预算，没有清楚隔离哪个新控制机制或可迁移失效条件。正文还将91.5称超过91.6、将0.835称低于0.798，局部 CodeBLEU/差值口径不一致；不以这些文本给出增益/因果结论。复用成熟执行反馈并用于代码场景、报告整体分数提高，不足以建立本项目所需的新增机制或经支持的条件边界。故拟将基于 current 后版摘要的旧窄P改为贡献前关闭，不评分、不写 Books；保留上述原证/改判原因供 Newton 准入校准，不能以审阅成本或日期排除。

## 3. GaLore2 20437：受限 Source/6分通过，Books 待具体比较

实际读 v1 §3～7、Appendix A/C 全及 Tables1～7。增量是梯度低秩 optimizer 的子空间刷新成本/稳定性与 FSDP 生命周期组合，不是 LoRA 冻结基座的另一个名称。拟 2+2+2=6：投影/刷新选择2、optimizer 与分片更新接口2、坐标状态和完整质量—成本边界2；不为500B或机构名称加分。

低秩 moments 在紧凑梯度空间更新，再映回完整权重；基的选择、随机截断 SVD、rank 与刷新间隔影响更新，随机投影/过度量化有质量退步。随机 SVD 仍需逼近谱，不等随机选一组方向；符号不定与随机性会让频繁刷新不稳定，作者在200～500步间隔观察不显著，不是所有训练自动无影响。§4.3 声称按层 reduce-scatter 后调用 optimizer 并丢梯度、跨设备复制 SVD 结果，但未闭合任意分片形状、accumulation、global clipping 与全局更新等价；不将概述当当前 PyTorch 支持保证。Appendix C 也不能证明 FSDP 通信总量必小于 DDP。

主文及 Appendix A 的非方阵 shape 有冲突：m≤n 时 U[:,:r] 是 m×r，PᵀG 是 r×n，而文中 P/R/M/V 维度写法混用 n×r；不照抄成可执行矩阵配方。原 SVD15倍只对应该子操作，Table1 两卡/单batch/2048与4096长的显存测量，不是256 H100/500B token长跑相同配置。500B Llama7B采用1024长、rank1024、T500及先10B调alpha/学习率，长程validation与下游均有输赢，没有多seed/区间或全生命周期速度/预算闭合。质量接近不是更新数学等价或全部能力保持，调参、SVD/基存储、通信与恢复都计费。

唯一拟 owner 为 TRAIN-ZERO/Ch39：低秩 optimizer 状态与分片是可组合的不同轴。实际已读当前48～88低bit/低rank activation/Oja与Stage2交接；它没有完整讲明直接梯度谱投影与 activation-basis 的分支差别，具体缺口仍需与相邻训练/LoRA边界比对后决定，不预签整合或已有覆盖。

## 4. ASSD20456：受限 Source/6分通过，Books 待具体比较

实际读 v1 §2.4、§3～6 全、§7.1/Table1、§9、Appendix A/B 全与D.3/D.4。增量是 any-subset 模型以两种 mask 同时提供条件独立 draft 与给定顺序的联合密度，从而用同模型 rejection correction 恢复目标采样；不是把多个位置的边际相乘就当真实 joint。拟 2+2+2=6：factorization/correction2、模型 mask/训练与 sampler 接口2、目标分布与计算预算边界2。

已见 prompt 内互看、待生成位置按原索引固定相对顺序，减小需拟合的分解路径；draft 各位置只读同一已见条件，oracle 在 permuted causal-like mask 下读已提议前缀。用 min(1,target/proposal) 接受，拒绝时按正差重采样；同模型首 token 的两条件相同故必接受，两个前向至少确定两个token，最后仅一个token时可省验证。Appendix B 的 min+正差恒等式支持的是**学得目标模型、固定条件/顺序及准确概率**下与其串行采样同分布，不证明真实数据分布、回答正确或任意 diffusion 架构都具备接口。Alg1 的 T/N 记号和Eq8下标不一致，不默改原文为已核可执行代码；定性采用只依赖正文与证明中明确的相同条件/目标分布。

110M XLNet需 joint teacher-forced 续训与mask curriculum；不是把未改任意模型直接提速。WikiText 640条、512长、95%mask、k5，Table1 的434.1 NFE/16.50秒对486/18.21，是该配置且包含 self draft 的前向；n-gram另有422辅助调用，不能只比target NFE就称总计算最低。GPT2-Large生成PPL和词频entropy两个代理相近不构成统计检验或逐分布等价证明；等价来自条件数学论证。训练四天/五设备与masked数据制备、两种mask/缓存状态都付费，arbitrary-order KV/FlashAttention仍future，不授生产batch/SLO或现有causal cache无改复用。仅采用模型联合密度接口与纠正机制；owner 拟 MULTIMODAL-GENERATIVE-PARADIGMS/Ch24（生成条件/顺序语义），Ch48不重复拥有一套该模型结构。当前Ch48同模型speculation已有，但任意子集联合密度/固定相对顺序不同，Books 尚待实际局部比较。

## 5. SAS20459：受限 Source/6分通过，Books 待具体比较

实际读 v1 §III～VI 全及 Tables I/II。LLM不直接产生每个控制周期的八轴速度，而提出8维 attenuation，乘在已有能击球的低层controller输出上；每轮真机执行所得轨迹进入下次 context，Summarize/Analyze/Synthesize 是梯度自由的参数候选搜索，不是模型权重反向更新、VLA预训练或已识别物理因果。拟 2+2+2=6：低维controller调制与反馈搜索2、语言目标/轨迹与真实执行两侧2、候选—物理验收及预算边界2。真实机器人/ICRA接受本身不计贡献。

坐标轴/范围和目标要在prompt声明；检索旧参数与合成新参数分开评价。两个平移后的优化函数、2/8维、50次各100步不代表通用全局优化：8D Rastrigin上LLM差于Adam，梯度法的额外估计与LLM调用成本不匹配，不能由最终函数值授同预算胜出。10指令/100次检索平均Top1约39.4%，两目标低于10%；真机仅24左侧seed逐轮向右的局部轨迹，未提供独立长程安全、全部初态/复杂接触或尾延迟验证。模拟三目标各20次/30轮的终点距离局部改善不能授解释忠实或新参数每轮单调改善。LLM相关性叙述只是搜索假设，更多轨迹context、模型调用、launcher/reset/机器人试验均计费，物理controller和安全约束仍独立。拟唯一 MULTIMODAL-EMBODIED-VLA/Ch26，Books 待对读现有controller调制与部署期适应分支。

## 6. TAMO20462：准入仍须具体机制校准，不采因果与修复保证

实际读 v1 §III/IV 全部公式/设置/结果与Tables I/II。工具把log pattern/keyword与trace-KPI作为两条件diffusion的分支，将重构特征送FFT/attention/GAT做定位/分类，再把预测及系统context交GPT4写建议；不是端到端模型直接读全部原始观测。原文把按幅值argtopk称高通滤波、attention依赖称因果图，但没有相应频率阈值或因果识别/干预依据，不能当物理根因真值。MaxPool到BCE的概率接口及部分GAT索引也未闭成可执行recipe。

两个故障注入数据集、固定seed/RTX3090、异质entity下部分baseline分开训练，不能将整体比较单归diffusion融合。去diffusion同时去log模态，去branch/FFT有局部反侧；TableII某macro recall移除FFT反而更高，全文“移除任何组件均退化”超出逐指标。GPT4只给一个定性case，没有独立建议执行/恢复时间/安全评价。当前看到的是领域观测处理模块组合与下游case指标，尚未定位可迁移到本项目模型/系统设计的独特机制或受支持的新条件；不因“多模态/agent”名称直接入选。拟贡献前关闭，不评分/Books；交Newton针对这一范围/增量理由独立校准，若指出具体可采用模型机制则只重受影响域，不重全文或因为日期/费用改判。

本包不是日级验收。两项拟关闭尚待校准；三篇受限 Source 可以先进入当前owner比较，不等这两项或其他40关闭。原33家族、原日期/历史分及已完成书改不撤销，新增45仍有可执行工作，不写普通0。

三明确候选另作当前官方事件页轻核：root 各单次 GET `/abs/2504.20437`、`/abs/2504.20456`、`/abs/2504.20459`，均 exit0；实际读标题、comments 和完整 history，三页均仅 v1，精确提交分别 Apr29 05:27:02Z/06:33:13Z/06:39:20Z，与 Atom/DataCite 相同，SAS comments为 ICRA2025，另两无 comments。所见域无撤回/勘误声明，不外推全渠道无信号或把会议接纳当更早公开。没有再获取或比较两版全文。

## 7. 准入校准纠正及实际可复用范围

root 实际读 Newton [§28～29](REPAIR_REVIEW_20261016.md#28-root首五与作者首批准入的真实校准tamo窄潜力不能按效果争议关闭)及所指旧精确 v1 决定域。ARCS 在实际 v1 增量范围贡献前关闭通过。TAMO 的拟 C 不通过：条件化 log/trace 去噪到共同 entity 表示，是具体替代接口，不应因混杂消融和未证因果而连表示机制一并排除。保留 §6 的全部反侧，撤回其贡献前关闭提案。

对 TAMO，root 此前已实际阅读的 §III/IV 足以支持受限标准审阅：两条件 patch-Transformer 去噪表示交给异构实体工具，下游 LLM 只消费工具输出；不支持因果识别、自动修复或可执行概率配方。采用命题拟 2+2+2=6（条件表示接口、观测与工具消费者两侧、可复用的输入/预测权限边界），不计整体指标或成熟模块本身。独立校准已实际核同一原域和反证；后续仅比较 Ch23 当前具体覆盖，不第三次重读全部 Source，不自动授 Books 整合。其余三篇 Source/6分与 ARCS C 的已核层保持。

root 另实际单次 GET 官方 Advanced Search 表单成功，原件在本次运行 `/tmp/ai-system-arxiv-advanced-form.html`，实际字段 `date-date_type=announced_date_first` 的说明明确只支持 year/month granularity；页尾也说明 announcement 排序使用 v1 公告年月。它可以发现历史材料，但该已观察表单不能独立将现有跨日区间缩到某个日，不据此声称 arXiv 历史论文不存在或所有恢复路径已穷尽。未调用 catchup。

## 8. 三项实际 Books 差额均已写后通过

root 实际读作者 §28 三份具体 owner 比较/逐字拟文，顺读 Ch24 1190～1265 的 target 构造、draft–verify 与 correction 完整交接，Ch26 373～441 的 RL head、test-time LoRA、视觉进度 warm-up/后续 PPO 完整局部，以及两章当时末注。ASSD 任意子集条件模型的双 mask 接口、SAS 固定低层控制器之上的无权重更新搜索均有具体缺口；分别授对应单段/marker/本人末注，不改旧机制、其他作者注或前后文。它们不是把论文摘要加到章末。

作者实际保存后，root 非写入者直接顺读 Ch24 1198～1221、Ch26 402～426 的完整新段/marker与前后段/标题，及各本人末注、前一完整他注和限定 diff。两项正文逐字保持已核采用边界：ASSD 同一学得 target/条件/顺序与准确概率、独立 proposal 不当 joint、训练及验证/缓存费用；SAS 低维速度调制不当动作逐周期/模型学习、真实执行反馈、物理验收与原 controller 退路。原前后段/marker/他注保持，限定 diff-check 无诊断。**两项实际整合通过，许可释放**；作者只同步本人注的既成事实，直接进入报告，不再回环原 Source/PRE。

GaLore2 由 root 分担实际写入：先实际读 Ch39 1～225 与完整末注、Ch38/40 的机制交接、Ch30/36/39 精确相关词定位，确认现低秩段只有 activation-basis/Oja 分支；在同小节新增直接梯度谱投影段，并只改原 activation 段首句使之自然承接。新段用明确定义的 m×n/r 自洽 shape 解释投影/完整权重更新，同时显式不冒原文已核 recipe、任意 FSDP 等价或恢复正确性；原 OASIS 机制全部保留。本章启动时两层 diff 为空，实际差额只有此段/首句/本人注。Newton §31 非写入者实际顺读49～105完整局部及首注/后注、限定差额并通过；root 实际读回该检查，接纳本项并释放指定位置，只同步本人注既成状态。没有改 Draft 或未授权文件，三项均不代表整日验收。

TAMO 随后也已实际保存并通过：root 非写入者顺读 Ch23 79～102 的完整新段及前后段/marker、本人完整末注与前一他注，并读限定5新增0删除差额和无诊断的 diff-check。log/trace 条件化时序去噪交给实体工具、LLM 消费预测的权限边界清楚；派生表示不冒新观测、振幅恢复不等高频保真、attention 不作因果证据，混杂消融与成本/退路均保留。接纳实际整合并释放单段许可；作者仅同步本人注既成状态、归并报告，不再回环原证。本节四项 Books 通过不代表45项或整日通过。

## 9. 受约束表示的单段范围

实际读Newton§33完整Source/当前owner比较及收紧稿，复用其独立原证判断，不第三次Source。root已顺读当前Ch12 77～125向量训练几何/完整扩词交接、335～380几何诊断及完整末注，并核Ch11/13输入输出交接。PSD因子构造与单位trace不是同一保证，Newton修订稿准确收窄；采用仅为普通词向量之外的受约束表示/消费者分支，不替换本章Transformer的lookup shape，也不授量子硬件或质量优势。授Godel按Newton§33收紧版在完整“但不能把距离近…”段后/跨checkpoint扩词段前一自然段、本人marker/末注，保护当前并发；保存后由Newton做一次实际完整两侧/本人注检查，未预签整合或DAY。其余§33/34具体No Change可直接进报告，不需root再签同Source。

Ch12随后实际保存，Newton§35非写入者完整新增/两侧/本人注与限定差额POST通过；root已实际消费并接纳释放，不再重复该Source/正文或另建收据。

## 10. ACE与Hoyen的具体单段范围

root实际读Newton§37/38受限Source、当前owner及逐字稿核验，并完整读作者§34/36拟段。再顺读Ch72 1434～1490工具边界/固定图/轨迹归纳连续论证、Ch78 617～644程序状态/压缩/历史/视觉fallback及两完整末注。ACE缺不可见工具目录的抽象规划与独立具体绑定；Hoyen缺按当前intent逐层收窄DOM及whole-form/填值历史的局部grounding。两稿只补这两个接口，不把静态图/schema/coverage当授权、安全或完备性。授Godel按原两锚点各一自然段/marker/本人末注，保护并发，保存后由Newton一次实际写后核验；当前不是已整合或DAY。已独核NoChange直接归并，20653当前官方撤回按独核§36不入选/评分/Books，不能混成贡献C或整个家族永久废除。

另实际读Newton后到DishCOVER独核与作者§37单段，顺读Ch79 210～253完整search/剪枝、后侧谱系及末注和Ch80开篇交接。两已有结构间沿编辑路径提出中间候选是具体proposal分支，与普通token改写/树搜索不重合；其语义有效性、value筛选、novelty人口及全费用不能互代。授Godel原Pruning段后/开放环境剪枝段前一自然段/marker/本人注，保存后Newton一次实际POST，不授料理/Science扩展或创造力/安全保证。

三项随后真实保存，Newton§41非写入者逐项实际完整新增/两侧/本人注和限定差额检查一次通过；root已实际完整消费该裁决，接纳三项并释放指定位置。当前正文均同获准稿，原机制、他注与并发层保持；作者仅同步本人注和报告，不第三Source/正文或再造接纳收据。其余普通Source未完，不代表整日通过。
