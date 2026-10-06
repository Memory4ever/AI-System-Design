# Pre-CoT Safety17368：生成前输入表示的训练期拒绝监督

resume_review17_18，2026-10-11，仅03-20补03/19；author明确未读本core并交本reader准备，后由resume_mar17非preparer裁。AGENTS/当前研究与Report合同/Prompt、Sources每日-arXiv/本日停点、ROADMAP与Books PROJECT/学习/写作约束实际重读。原批5准入/date§13有效复用；保持2+2+2=6，不自授Source/PRE PASS、safe、Books锁或DAY。

## 1. 必要源与停止位置

[exact-v1](https://arxiv.org/html/2603.17368v1)实际读§3 L95–123/Eq1–5，关键§4.1–4.6/Tables1–3 L124–253，必要A1–5/训练与采样L310–360、B身份/构造L362–381、C judge身份/伪真值/基线L382–408、D1–4/Table7–8 L409–457。初段只Fig1–3正文/图题背景，不把图像数值当已读。没有读references/全部qualitative案例/代码；C图9/10像素prompt未审，不授精确judge配方或独立安全真值。[当前official abs](https://arxiv.org/abs/2603.17368)完整AB/comments/history只v1/v2，未见具名撤回/纠错说明；v2号本身不触发全版本diff，不采用未读v2正文。

## 2. 可支持接口与直接反侧

§3.1先从teacher实际拒绝行为制binary label，再训练BERT query分类器；分类器输出拒绝概率，不是groundtruth harmfulness或内部真实决策。§3.2用输入prompt生成前的last-layer token表示masked mean pooling，经训练期linear head，BCE拟合该软概率，联合普通行为SFT；梯度进入可训练backbone/LoRA。head和BERT部署时移除，最终仍由同一LM生成回答/拒绝，**不是部署前硬gate，也无强制早拒保证**。A1主T1使用7B CoT-OFF与DeepSeek-V3 teacher；D1自teacher另实验，不混成全部同源或无外部teacher。

关键有限消融T3 7B在作者人口下align=0→full的ASR11.2→5.4/53.6→18.8支持额外训练信号，但不能独立证明真实决策时点或唯一机制。§4.4比较参数变化量是相关定位，非因果中介证明。T1对GCG 8B/8B-Qwen等R2D仍更低，StrongReject Qwen8B4.5高于R2D1.5；Wild仍14–24.8残余，不能授所有基线优势/零风险。T2良性拒绝7B4→11.4、8B4.4→7、14B7.8→8.8、Skywork9→13.8；非全面无overrefusal。D1 T7 14B AIME56.7→49.3/Math91.8→91.2/MBPP62.2→61.9及7B AIME50→46，不能授无能力损伤。

CoT-OFF是另运行条件而非时间因果实验；D1 OFF仍有非零ASR且能力降低，“只有CoT后才失安全”不采为普律，ASR也不直接记录拒绝首token相对CoT时序。D3图题/正文关于长度只作者定性，不冒像素趋势；D2较高随机性更弱为原文定性。C2没有human truth，四模型多数/2:2轮换产生pseudo groundtruth再择judge，不能把其accuracy/F1当独立可靠性认证；不同judge/teacher设置不合并。

5k harmful+3k benign/GPT5构造与BERT约一半人口，LoRA r16/alpha32/allmodules/B64/2epochs、align.5、teacher greedy/eval temperature.6 topp.95原证可核；数据生成prompt请求6k与最终约5k为不同阶段，不自行补过滤计数。HW/precision/输入输出长度上限/并发/SLO、seed/CI、完整teacher/classifier/训练搜索/部署成本未完整披露。不外挂head只省该部署组件，不证明端到端免费或更快。

一次强命题重开条件：给出精确CoT-OFF操作与匹配解码/预算、拒绝首token/CoT开始的独立时序或干预证据、teacher标签与held-out人审及安全/良性效用回归。当前有限监督接口不依赖这些强保证；不将中心only-after、安全永久或真实决策解释写入Books，也不降分/改EX快关。

## 3. actual sole owner与具体差额

sole `TRAIN-SFT` / [Ch29](../../../../../books/part-04-training-system/29-sft.md)。实际完整845–909读：现867–874 on-policy安全蒸馏是在student已访问prefix上由特权teacher选择翻转token并KL监督；887生成前probe只是动态配KL/NLL的critic，不是teacher行为→BERT软概率→prompt token pooling/auxiliary BCE的训练目标。故本有限差额不是泛安全SFT或已有probe重复；相邻output-head共同偏差保持合理。

拟原on-policy safety完整绑定end后、Distillation output-head标题前两段；不改变已核on-policy占用/外部safety gate。Ch28入口1–35/Ch30入口1–32及Ch72入口1–38实际读：优化与低秩参数化仍各自owner，真实授权与独立行为发布归Security/评价，不让训练辅助信号取得放行权。不建新结构。

## 4. 两段literal PRE及静态注（待非preparer裁）

安全监督也可以在任何推理文本生成之前作用于输入表示，而不只拟合已访问的输出token。一条受限分支先把teacher对query的实际拒绝行为训练成query分类器，再以其软拒绝概率监督student输入token的末层表示：masked mean pooling接训练期linear head，辅助BCE与普通行为SFT共同更新模型。它把监督位置移到生成前，不证明真实安全决策已在那里完成；teacher拒绝与分类器概率也不取得有害性真值。部署移除分类器和head后仍由原LM产生拒绝或回答，不是独立硬阻断器。<!-- source-family:SF-2026-ARXIV-2603-17368 -->

[生成前辅助监督的有限对照](https://arxiv.org/html/2603.17368v1)支持在作者模型/人口下额外训练信号，但仍有攻击成功、良性过拒和能力反退；CoT开关及参数变化图不能认证拒绝的真实时点、唯一原因或通用安全。Teacher行为标签、分类器泛化与模型judge共偏须另验，输出拒绝、首拒绝时序、良性效用和独立安全结果分账。Teacher采集、分类器训练/标注、辅助forward/backward与行为回归均计费，移除部署head不等总成本为零。信号不可靠、分布漂移或任务/安全回归时，保留经核验的refusal示范、原on-policy/off-policy监督与外部行为发布门，不让latent概率自行批准放行。<!-- source-family:SF-2026-ARXIV-2603-17368 -->

静态注：

- `SF-2026-ARXIV-2603-17368` — [PreSafe exact-v1](https://arxiv.org/html/2603.17368v1) §3/Eq1–5、§4/T1–3、必要A/C/D1–4/T7–8。仅teacher拒绝→query软信号→生成前表示auxiliary BCE/联合SFT接口，部署移除head非硬gate；保teacher/模型judge资格、攻击/过拒/能力反退与全费，不采only-after-CoT普律、真实决策时序/唯一因果或通用安全。未核实现/复现。

此为准备稿，等待resume_mar17必要非preparer原证/actualowner/PRE裁；未经root授权不写Books。

## 5. 非准备者必要源与 PRE 裁

resume_mar17在本20恢复重读适用合同/Books约束后，实际独立exact-v1 §3/Eq1–5 L95–123、T1/§4.1–4.2 L124–200、T2 L202–213及head消融§4.6/T3 L237–253，必要A1–5 L310–360、C2/C3 L393–408与D1–4/T7–8 L409–459；未逐图像素或附录E全案例。actual Ch29完整845–914及Ch28/30/72入口实际读，与原两literal PRE/静态注逐字回对。teacher拒绝行为→BERT软概率→prompt last-layer masked pooling/auxiliary BCE联合SFT可分采，部署head移除不等硬gate；on-policy已访问输出KL/critic配权不承载该具体监督目标差额。T1 R2D局部更好、T2过拒/T7能力退/C2非人审共识与全费均原证一致，强only-after及真实决策因果不采。必要Source/actual唯一owner/两PRE及static正式有限PASS，保持6；请root协调Ch29窄写，未POST不计safe/DAY。

## 6. 限定实际写入

root授resume_mar17唯一Ch29本family窄锁后，author仅原两literal PRE实际875/877＋静态本人1476。writer实际完整867–895及1468–1476自身/邻注读回；原on-policy输出监督→生成前auxiliary监督→head共偏及critic分支责任顺接。原6分保持，scoped本family实际diff仅两段/注、git diff --check 0；未授POST/safe/DAY，下一由未写Books的reader一次actualPOST，不循环改静态注验收身份。

## 7. 一次非 writer actual POST

resume_review17_18仅本20、非Books写入者，恢复合同/本日停点后实际顺读Ch29完整861–902（on-policy完整绑定→新875/877→output-head共偏→时间KL/输入critic配权→后续训练分支）及1466–1476本人/PACT/CoTrace/TPD/TASTE/HypoTerm邻注。逐字回原两literal PRE/静态注、本packet已核必要Source及author非preparer§5；scoped本family实际diff只两正文+注、diff-check0。新增auxiliary目标而非运行时硬gate的差额、teacher/judge资格、攻击/良性过拒/能力退、真正决策时点未证、全费与原行为发布门均近文保留，原监督/共同偏差链未被替代。实际POST正式有限PASS，通知root释放；不改Book注身份、不重读有效核心、不授DAY。
