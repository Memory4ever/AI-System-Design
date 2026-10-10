# 10463 Learning to Wander：active-observation协议必要反证 / 拟终态

只03-13补Mar12 BJT自然日；第三完整题摘/窄贡献与DATE3日级原件非作者校准有效复用。本次实际完整SUP_ABS3_10463.txt五作者/v1唯一history、无可见venue/withdraw/correction；SubmittedMar11T06:24:10Z、SUP_DATE3_10463.raw registeredMar12T02:02:13Z，与官方正常公告下界形成Mar12日级，不把Updated或index当公开。官方 https://arxiv.org/html/2603.10463v1 GET200/457540bytes/UTC2026-10-10T02:08:14.253489Z，SUP_CORE_10463.raw/txt及manifest/result保存。

## 窄增量与实际投入

单图地理定位不测试通过环境动作增加观测→本文提供带GPS的可导航panorama graph、模型生成难度/位置和互动重新猜测→需要区分**给模型更多观察/turn预算**与**更好信息选择/可执行覆盖协议**，不是32K/19模型排行榜或地理领域准入。反思→动作→新观察循环是成熟结构，本包不计新基础。

**2+1+2=5，协议设计反证必要局部深入，争议/暂缓Books0**：静态与主动观察的评价对象及声明的可执行coverage条件改变设计解释2；限定一个多模态benchmark/evaluation组件1，不凭model/action/environment名词抬跨层；可执行题目支持与信息预算须区分的具体资格2，不借通用EvalSpec/主动感知原则抬3。最初可以最低关闭的局部配方核查遇到Eq4/5直接断点后，加深受影响证据，不因时间/成本降分或撤销准入。root非准备者实际Source/owner终态已通过，受限formal，不授DAY。

## 实际必要原件 / 决定性反侧

直接读§3.1–3.2完整390–627（含Table2自提位置diversity）、§3.3 Eq1–5及覆盖声明627–778、§3.4–3.5完整1136–1145；§4.1–4.2完整1442–1520的设置/metric、4.2.1直接1530前后及1950–1967统计/趋势说明；§5.1–5.2/§6全部1968–2058。直接Table5代表LLaVA/Gemma/InternVL/o3/Gemini/Claude行与对应delta，不逐项审其余全部排行/Table4统计。Figure onlycaption，未看pixels；没有代码/图路径复现或现实物理动作执行。首次长owner rg和一次混合输出被截断只发现；实际目标局部另完整读，未把截断未读当完成。

原地点由LMM按大陆/难度提出，再看zoom16 satellite与标记点，自行接受/拒绝、增补panorama直到它认为难度/空间特征符合。3.4问题/“correct answer”也是LMM派生；GPS坐标来自地图服务可描述节点位置，不认证每题语义答案或独立难度校准。Table2是归一化地理分布diversity，不是独立解题困难、可辨识性或动作选择效率。本文自生成/自判population资格保留，不能推广所有自然地点。

**Eq4/5精确coverage断点：** 定义B={v∈V:deg(v)=1}，声明min_{v∈V}min_{b∈B}d(v,b)≥10，保证从任意节点至少十步不触boundary/不回溯。若B非空，选择v=b给d(b,b)=0，因此字面条件不能成立；若B为空，min需要单独约定，不能单凭空集合保证任意探索路线十步。最小两节点单边graph已示反例，长链含端点也相同。不擅把min换max/限制起点为中心，更不补造实际代码筛graph算法；这是**所写coverage保证**不由式推出，不否定导航graph数据存在、所有定位结果或全部方法。声明起点分布/实际allowed action与boundary行为必要但未闭合。

§5 Eq7只给o_t=f(I_t,h_t)→action→T(I_t,a_t)，反思缺线索后转30°/移动，新图再猜；实际history保存/观测切片、legalstep选择、cost/最大turn与stop条件未在所读机制定义。没有同预算随机/固定view/同数量多图或更多CoT baseline，不能把Table5增益唯一归给“行动推理”，也不能拿没有训练当免调用/导航费用。接口确提供互动观察测试，但不授观察主动选择最优、减不确定性校准或真实执行安全。

Table5所读例子o3distance318.8→180.3、streetF1 .525→.607；GeminiFlash222.1→166.2、streetF1 .505→.510；InternVL378B1442→1253、streetF1 .159→.164；LLaVA4081→3007有局部改善。保作者结果与不同收益规模，不说已反证实际定位改善。Table4/直接4.2.1注明Qwen系列coverage20/50/80趋势可不单调；coverage/样本分组/独立重复与CI未完整披露，不从三coverage或ANOVA授普遍泛化/稳定。19摘要与20实验设置model-count口径不强行合并；不指控造假。

公开API闭源、ms-swift/H200部署开源、temperature0/greedy；具体artifact revision、H200数量/precision、每episode观察/turn/token/导航距离/latency/full调用cost、scorer匹配口径和tailSLO Not Disclosed。当前32,741panoramas/1,047地点/39,442edges是库存身份，不等独立执行样本或更多输入免费的matched试验。题目标注/获取地图/renderer/多turn/模型生成题库都付费；确定性解码不认证独立统计。

## actual owner / Books终态与重开

ROADMAP唯一 `PLATFORM-EVALUATION-SYSTEM` Ch66，实际完整90–119目标→EvalSpec、154–167文件依赖负控制→任务生成/难度/预算人口与逻辑oracle完整局部已顺读。它已有eligible population/scorer/uncertainty、生成器难度≠能力下界、输入信息预算/更换题目人口不合因果的具体条件；**没有写入或认证本稿新图/实验**。Ch26动作/安全、Ch78动作执行effect只是handoff，不用地理导航主题建第二owner。

本稿新的可导航/自生成评价协议有窄准入价值，但字面coverage条件、独立难度与matched信息选择主张未闭合，拟中心协议受限争议/暂缓Books0，不将新实验称已有覆盖，不造抽象“已吸收”两段。必要局部方法/反侧已足，不扩所有ranking/图片/地图artifact。精确重开：本ID revised/勘误给合法start-node集合与boundary/step过滤规则，独立题目/难度验证、明确action/view/history/stop/cost预算及等信息/等调用对照，才核受影响protocol与owner差额；不请求完整全站历史或时分秒。

没有Books写/PRE/POST需求。root非准备者已实际核Eq4/5、§5.1/7、Table5代表行/5.2–6与Ch66完整局部，5分受限协议争议终态PASS，正式暂缓Books0；不否定全部graph/定位结果，不授DAY。普通未读artifact不是外部blocked。
