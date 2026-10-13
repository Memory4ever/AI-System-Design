# L2A2603.17484：必要 Source / actual owner / 最小 PRE 准备

resume_review17_18，2026-10-11；只03-20补03-19自然日。恢复已实际重读AGENTS、研究/Report合同、Sources使用/每日/arXiv、统一Prompt、ROADMAP、本日README/STOP与相关LS路由；不继承其他日期。原准入/date复用本日独核§13及SUP_ADMISSION_BATCH5，原2+2+2=6不变。准备者不自授Source/PRE PASS、安全计数或DAY；未写Books/Report/LS。

## 1. 精确身份、实际必要读取与停止

[exact-v1](https://arxiv.org/html/2603.17484v1)：实际§3.1–3.4 L101–160、§4.1–4.5/Tables1–2 L164–233；A Eq8–17/训练credit L306–339，C Alg1 L359–404；D仅Table3–5 L409–414，E仅NSA对照实现边界416–420及E1阈值/窗口/冻结FFN L424–448；F训练条件与评价定义L449–478。Figures仅正文/图题定性，不冒像素曲线或精确速度值。未读全部related works、references、GitHub代码或新版全文，不声称复现。

[当前官方事件页](https://arxiv.org/abs/2603.17484)实际title/完整AB/comments/history L9–28：v2为ICML与26页/11表，未见具体纠错/撤回声明；原本日轻量信号为6→11表，不凭表数扩全版本diff。首次公开自然日夹证继续复用既有本日准入，不把Submitted03/18改成公开日期。当前AB不替代v1必要Source。

## 2. 支持的有限机制与直接反侧

§3先对所有位置算LocalAttn得到s，再由sigmoid(Ws)阈值门决定是否调用对历史s的GlobalAttn，输出s+d·a；不是全局分支读取原始x，也不是跳过整层FFN。硬门前向/STE反向加soft-score平方成本；不计算a的关闭位置缺NTP门credit，正则可推动全关。训练以约0.1概率在整次迭代计算全部global输出但保留原门乘法，给关闭门提供代理credit，不等无偏离散梯度或保证避免collapse。所有token仍写global K/V供未来位置读取；query稀疏本身不省这一完整缓存。另有训练后按层删global模块的步骤，应独立做信息路径/质量验收，不与token跳读混算。

C active-Q compact→原位置Q_idx causal eligibility→全K/V tile→scatter原位置，支持执行身份契约。但未采用Alg1完整可执行recipe：L366 Q_idx tiling记号n/n_c不齐；L386旧output rescale写逆指数，L390–392最终统计写T_q而非实际key迭代终点。这些与标准online归一化关系不一致，不据它授数值精确或kernel正确。A Eq12有1/(nL)，Eq15/16正则项缺n；Eq17把跨token共享W的sum收缩为本token项，实际一阶Δz_t含其他s_u与s_t内积，不推出所有门都按单token两项单调变化。只采forward/credit消失及补算接口，不采解析速率/全局稳定保证。

评价保留：Table3 Qwen2.5-7B引用生成8K CLP24.2/L2A17.2，64K4.8/4.1，MRCR128K21.3/19.3；Table4 1.5B RAG五长度均退、MRCR128K14.3/9.4；Table5 Qwen3-8B平均128K44.0/42.5、引用64K12.3/5.2。平均接近不等每任务无损，“seed-level variability”未给独立seed/CI，不采。NSA非官方顺序执行实现、selected-block由16改128，不能把对照速度写为原NSA架构天生更慢。

Table2/F作者Qwen2.5-1.5/7B与Qwen3-8B，128K、BF16、H200，训练batch4M/6M tokens、16.7B/25B训练tokens；CLP及L2A attention/LN更新、FFN冻结，仍非整个模型能力不变。H200单kernel倍率非端到端；64K/128K平均TTFT无生产tail/SLO、concurrency/evaluator完整合同。§4.3只1.5B删15/28 global模块，§3.4称held-out而§4.3称small training subset，保选择集口径冲突、不采精确pruning recipe或所有模型50%缓存。E1增λ/推理阈值省global会退质量；SWA-0转全global，不授gate是真实依赖oracle。完整训练/λ搜索/compaction/额外local读写/pruning校准费用计入，生产全费Not Disclosed。

一次精确重开请求（只针对不采用的强实现/保证）：提供修正并可对照的Alg1归一化/索引迭代，A的n归一化与共享W跨token门更新推导，以及独立pruning选择集及任务/服务回归。有限接口准备不等待这些强命题，也不把本family整篇改EX或虚称已有覆盖。

## 3. actual sole owner 与差额

sole `MODEL-LONG-CONTEXT`，[Ch22](../../../../../books/part-02-model/22-long-context.md)。实际完整205–274、272–376的必要局部（重复边界仅为完整段）：211–217是每query少读keys及关系复杂度；228–235是local/global互补；272–299是prompt-conditioned整层route和head-block状态；308以后是选哪些keys、teacher-owned/forward-selector及未选span credit。它们不含每token是否调用完整global、关闭query仍写全K/V、偶发全计算但门仍关闭的训练credit组合。故不以同有router/KV泛主题作NC。

相关交接actualCh21入口1–40（MLP容量路由非记忆读取）及Ch23入口1–38（表示身份非条件global）；Ch19完整1–72缓存来源仅用于query读取与key写入分责，不复制其缓存基础正文。

拟在Ch22原235互补算子结束marker后、237 Immutable Task Prefix前写两段，保持原formal-local/global理论边界，也与后文窗口删除/固定route分支分开。不提出结构候选或另一章重复owner。

## 4. 两段 literal PRE 与静态注（未写）

local/global互补还可以把选择粒度从“读哪些历史位置”移到“当前query是否调用全局读取”。一条需继续训练的分支先为所有token计算local表示，再由各层token门决定是否对这些表示的完整causal历史执行global attention，并把结果加回local路径。关闭的是当前query的global计算，不是整层MLP，也不是该token对未来的可见性：global K/V仍须写入，不能据query稀疏率声称缓存等比例缩小。执行时可先compact活跃queries，但causal mask与输出scatter必须保留原位置身份；训练后另删某些global模块则是改变信息路径的第二项设计，需要独立质量回归。<!-- source-family:SF-2026-ARXIV-2603-17484 -->

门的学习也不能只奖励少算。若关闭路径根本不计算global输出，next-token loss对这道门的代理credit会消失，成本正则可能把它继续推向关闭；有限训练分支偶尔为全部queries计算global输出、仍保留硬门的forward乘法，以给关闭门提供STE训练信号。这不授无偏梯度、全关不会发生或精确kernel recipe。[L2A的有限对照](https://arxiv.org/html/2603.17484v1)仍有检索、引用及多轮指代退步，阈值/局部窗口、继续训练、补算、query搬移与完整KV都计费，单kernel速度或平均TTFT不能认证服务SLO。短上下文不偿额外local/router成本、关键远程依赖漏读或无法再训练时，保留原dense/固定hybrid与任务回读；只有独立校准并回归后才采用整层pruning，不把它与跳过当前读取混为一项收益。<!-- source-family:SF-2026-ARXIV-2603-17484 -->

拟末注：

- [L2A2603.17484 exact-v1](https://arxiv.org/html/2603.17484v1)：必要§3–4/T1–2、A路由credit、C索引/归一化、D T3–5、E1与F训练/评价定义；采用token调用global/全KV保留/训练credit及原位置执行接口。保任务反退、pruning选择集冲突、A推导与C伪码限制；不采无损、无偏/收敛、完整kernel recipe或生产SLO，未复现。<!-- source-family:SF-2026-ARXIV-2603-17484 -->

## 5. 非准备者裁决

resume_mar17非准备者实际重载本20适用合同/Books上下文，独读v1§3.1–3.4/Eqs2–7与关键§4/T1–2及pruning选择集、A Eq12–17、C Alg1、D Tables3–5、E NSA执行反侧/E1阈值窗口与冻结FFN、F1训练配置及F2所采用任务定义；没有重读无关references/代码/新版全文或假称复现。actual Ch22完整205–376相关读取/互补/固定route/selector credit链、Ch21入口1–42/Ch23入口1–38/Ch19缓存基础1–72实际顺读。

有限Source/sole实际差额/原两literal PRE与静态注正式PASS。Eq4 global确实消费local s，Eq5硬门乘法与§3.3偶发整次补算保门一致；§3.4明确所有token全KV保留，非query稀疏同比删缓存。A跨token共享W实际更新含各s_u与s_t内积，Eq12与15/16的n因子不齐；C旧输出逆rescale和T_q终点不授精确recipe，这些反侧不推翻仅采用的读取/credit/索引身份接口。已核T3–5任务反退、H200/BF16/128K与训练token条件、pruning held-out对training-subset口径、非官方NSA顺序实现及选块128的限定。原PRE不采用无偏/单调收敛/所有任务保持或生产SLO，因此可有限分采，不假NC/EX或整篇center。

Ch22原235互补算子完整end marker后、Immutable标题前两段sole差额成立；原固定query选keys/固定layerroute及未选span credit均未承载“是否调用完整global＋关闭query仍写KV＋补算保门”的组合。原6分保留；root随后协调共享Books窄锁，准备者/本裁均不授写入、POST、安全计数或DAY。

## 非 writer 实际 POST

resume_mar17在reader按root唯一Ch22 family窄锁写后实际顺读222–274完整互补理论→新237/239→Immutable/ThinkStream/Context Anchor链、1379–1387自身及ProtoT/CRAM/ThinkStream等邻注。两正文逐字回原PRE，静态注回有效Source、仅source/scope/边界不复制过程身份，限定diffcheck0。当前query是否调用global与全KV保留/模块pruning分责明确；保STE非无偏、任务反退、校准/成本/原dense与回读退路，原formal互补与后续固定窗口语义未覆盖。正式有限actualPOST PASS；可由root接纳释放并作者归并，不授最终DAY。

## 6. 授权后的 writer 实际落实（不是独立 POST）

root收到§5非准备者裁决后明确授resume_review17_18唯一Ch22两原PRE与本人静态注窄锁。已逐字写入新237/239及本人静态1387，无额外机制改写；writer实际完整222–274（dense/sparse语义→原local/global完整论证→新两段→Immutable完整分治与ThinkStream→anchor入口）和1379–1387静态本人/相邻源注读回，scoped本family两正文+本人注与diff-check0。未改旧formal段/邻family或过程身份注。交resume_mar17一次非writer actual POST，未由writer授POST或计safe/DAY。
