# InfoShot17374：无 query 的镜头代表与局部偏离双角色

resume_review17_18，2026-10-11，仅本03-20补03/19。resume_mar17明确分配sole准备、root已告知，作者未读core；原批6/独核准入date与2+1+2=5复用。恢复实际重读AGENTS/适用研究与Report合同、每日Sources/Prompt、ROADMAP及Books约束、本日README/STOP；无新发现/query、无Books/Report/LS写入，不自授Source/PRE、safe或DAY。

## 1. 必要原证与停止

实际[exact-v1](https://arxiv.org/html/2603.17374v1)§3.1–3.5/Eq1–9 L91–148、关键§4.1–4.4/Eq10/T1–3 L149–216、§5/T4及直接budget/feature反侧217–247、A1理论桥302–324、A2/Alg1 325–373、A3仅直接时间失败377–382、A4数据与评价407–422。图仅正文/图题，未冒像素曲线，未遍其他case/references/代码/PDF/旧修订；支持和直接反侧足以准备下面有限接口即停。

当前[official abs](https://arxiv.org/abs/2603.17374)完整AB/history只有v1，未见具名撤回/纠错；Submitted不替已核03/19日夹证。TikTok部署只属作者说明，未见独立deployment protocol/数字，不采用生产能力或严格安全证据。

## 2. 核心分采与不采用桥

冻结pretrained视觉特征→cosine affinity→左右窗口内凝聚度相对跨窗口相似度的差提出分界→greedy划成预算决定的若干段，不是已验证真实语义shot或完整似然检验。每段common按高平均相似/低局部波动取代表，unique排除common后按低典型性/高邻域波动取另一帧；主文两个角色是稳定背景与短偏离的采样代理，不是learned query selector、异常语义真值或motion因果。仅采用角色分责，不照录λ/α/固定窗口的完整recipe。

Eq4–5/9只是MI设计原则，原文明确不直接估计MI。A1在outlier独立宏观结构且固定f=1的模型下单帧条件MI为0，不足推出任意集合增益为0/greedy最优：联合条件仍可有协同信息；也不能由feature-space最近邻失真低推出semantic信息/真实异常全保。原随机游走与piecewise-stationary近似未在真实所有视频被验证，不采用MI最优、GLRT显著性或普遍保真定理。

M=floor(K/2)按每段两帧保留，预算不是自然shot数；singleton只取一个，奇数K可少一帧。主文L137明确union必要时truncated以满足|K|≤K，但Alg1 L371直接return而省略这一截断步：K=1时M=0仍初始化一段，伪码可能选两角色，不能据此说整篇从未有≤K上界。主文上界、伪码省略与§4各方法恰K的评价合同仍须分账，奇数补足/截断优先级、窗口边缘、min/maxshot长度、邻域/相同分数归一与tie等退化guard未全给，不授全输入exactK实现。主文窗口右侧起点t与Alg1两段[a,t]/[t+1,b]边界含义也须明确，不拼成精确recipe。必要长期接口只要求给背景与偏离分别留候选、由执行前budget/索引校验控制，不声称本文实现完整guard。

## 3. 评价条件、直接反侧与全费

SynFlash为8000合成视频、每类2000，三个Panda测试clip拼接短于30s，640×480/24fps注入ImageNet内容；16000 MCQ按metadata生成，选项有text LLM distractors，解析选项算Acc，理由只定性。ResNet-50 ImageNet预训练与插入类别同来源，不能由这一人口推开放未知语义异常；feature改变同时改变selector信号，T4不证明唯一原因。主文2–5帧与A4 camouflage/PiP 5–7帧时长不统一，TO正文相对macroscopic event与A4 clip级标签身份也不完整，保population/protocol边界。

§4.2固定.5fps，K=ceil(.5L)，Qwen2.5-VL同prompt/temperature0（参数量、precision/平台未披露）；T1有总体R/AR/TO局部收益，但Curtain R88.45低于VSUMM93.75、AR73.15低于74.95，Camouflage TO60.70低于TransNet61.95、Curtain TO61.10低于66.50。A3明确命中异常却缺参考事件导致TO错，命中与关系证据应分验。T4 ResNet-R84.66与T1 84.70小口径差别不混成精确统一统计。HIVAU .1fps ER仅任一帧落事件区间，CR是所有事件各命中一次，非覆盖事件每个时刻；UCF ER持平69.44。Video-MME .25fps仅short/medium，短71.5低于uniform71.8、平均同67.0，不授一般Video-QA提升。

§4.2称600帧block且10fps similarity只影响memory，但原24fps上的短事件能否在10fps候选化与block边界仍保同证据/排名未闭合，不能授仅存储变、全预算公平或所有瞬时事件可达。全文所需框架不依赖这些数值recipe。先解码/提全候选features、affinity/segmentation/选帧再减少VLM输入，selector不是免费；全视频离线分段还读取未来，非causal streaming/实时deadline。

hardware型号、GPU数量（仅A4多GPU并行）、precision、batch/concurrency、feature/affinity/解码完整时延与峰值memory、重复runs/CI、生产tail/SLO/误报及moderation数量协议Not Disclosed。同保留fps不等matched全部compute，作者TikTok叙述不签实机安全/无漏检。一次强命题请求为fixedsplit与真实时间标签、候选抽样/blocks/奇数及退化预算trace、按角色消融、同完整预算效用及真实部署protocol；缺这些不将本有限接口改EX或假NC。

## 4. actual sole owner 与 literal PRE（待非准备者裁）

实际读[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)1–18、完整614–681，Ch22/24开头交接；sole拟 `MULTIMODAL-REPRESENTATION` 原query-conditioned temporal granularity/event budget段结束marker648后、stage删除信息650前两段。既有temporal graph/clustering按query分预算与内容区间merge不承载未知query时“同段背景代表+高偏离例外”的双角色；不重复一般稀有事件/质量指标警告或创建benchmark owner。

问题尚未知时，按query分配事件预算之外还可保留无query的两种帧角色：先用冻结特征与左右窗口相似性差提出分段，在每段保留一个高典型、低局部波动的背景代表，再保留一个不同的低典型、高局部变化候选。这样不让长静态背景或镜头边界独占全部候选，但分段与偏离仍是表示代理，不认证真实shot、异常或任务关键性。镜头数随预算改变，两帧也未必足以同时说明短事件和参照关系；索引、时间与特征revision应随采样集保留，奇数和退化区间另验预算，不从信息论动机宣布严格最优或全输入配方。<!-- source-family:SF-2026-ARXIV-2603-17374 -->

[背景与偏离双角色的有限对照](https://arxiv.org/html/2603.17374v1)中，命中注入事件不保证时间关系答对，一般视频任务也有持平与反退。事件命中、全部事件各命中一次、背景/关系证据与最终答案须分账，不能用feature失真或局部recall签开放异常完整性。全候选解码、特征、相似度/分段及VLM均付费，同保留fps不等同全部计算；离线读取未来也不授causal实时服务。偏离信号失配、关系证据不足或选择成本不合算时，提高参照帧预算、重读原视频或回退均匀/dense输入，不把两帧代理当作证据充分性。<!-- source-family:SF-2026-ARXIV-2603-17374 -->

静态注：

- `SF-2026-ARXIV-2603-17374` — [InfoShot exact-v1](https://arxiv.org/html/2603.17374v1)必要§3/Eq1–9、§4/T1–3/Eq10、§5/T4与§6、A1–2和A3直接时间失败/A4评价。仅无query分段后背景代表与偏离例外的双角色；保代理非语义/MI最优、命中非关系充分、切片反退、预算/候选时间/blocks/索引未闭合及全费，不采精确recipe、生产recall/causal实时或安全保证；未核代码/复现。

准备完成交resume_mar17非preparer必要Source/actualsole/literal裁决，不自己授PASS或提前写Books/DAY。

## 5. 非准备者必要 Source/actualowner/PRE

resume_mar17仅恢复本20适用合同及Books上下文，独立实际核exact-v1必要§3/Eq1–9 91–148、§4/T1–3与§5/T4及§6 149–247、A1 302–324/Alg1 325–373/A3直接TO失败377–382/A4评价407–422，actualCh23完整614–681及22/24表示交接。原两literal PRE及静态注逐字有限PASS，保5/date；未知query时每段背景代表+不同高偏离候选，确有差额，不等已覆盖query-conditioned事件预算或区间merge。只双角色接口分采，不授真实异常、MI最优/GLRT或全配方。

实际L137明确truncation ≤K，notes经窄修定点final正确：Alg1省该步与exactK评价分开，不声称全篇从未给上界。λ/α/shot窗口等正文有披露，不以缺完整guard冒全部配置缺失；奇数补足/退化及10fps与24fps短事件、时间关系参照仍保边界。Curtain/TO/Video-MME反退、事件命中非关系充分、同源合成人口与全部selector/VLM费用/离线未来读取准确。未采用图像曲线精确值、全部case、代码或部署protocol；支持与直接反侧够即停。请root授reader soleCh23原648 marker后、stage删除前两literal+static窄锁；未actualPOST不计safe/DAY。

## 6. root窄锁后实际 writer（不授自身POST）

root明确授权soleCh23本family原648 marker后两literal及本人静态注。resume_review17_18在现有完整637–670及末注邻接读后，逐字写入650/652，自身静态注1734；完整两侧 query-conditioned→无query双角色→stage删除、末1726–1734本人/邻注实际读回。原PRE/static不改命题，限定diffcheck无输出。只两段与本人注，不同步流程identity；交resume_mar17一次nonwriter实际POST，未自授POST/safe/DAY。

## 7. 非 writer 实际 POST

resume_mar17恢复本20合同与Books约束，实际完整读Ch23 637–674及1724–1736本人/邻注，逐字回对已有效必要Source、两literal PRE和静态注。新650/652位于query-conditioned temporal graph完整marker之后、stage删除之前，无query背景代表/偏离双角色及命中非关系充分、预算/离线未来与全费用边界近文准确；既有semantic binding和相邻分层剪枝未改。静态本人注1734不含过程身份或新保证。限定diffcheck0。一次nonwriter实际POST有限PASS，交root接纳释放Ch23；不授整日DAY，不重开有效源或循环改身份注。
