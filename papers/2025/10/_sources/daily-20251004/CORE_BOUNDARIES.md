# 2025-10-04 有限必要核心边界

作者Huygens；仅本日材料。原件下载不等阅读。以下是实际读到的具体命题及停止点，不是正面Evidence、复现或独立复核；论文first-public仍待真实官方公告/完全落窗bounds。

## 已读必要安全与设计反侧

- [VeriGuard 2510.05156v1](core-2510.05156v1.raw)：§3.1–3.3离线生成约束、PyTest/Nagini Hoare验证及运行时；§4.1数据和§4.4结果、§5.1–5.3限制。验证的是生成的策略程序对形式约束的满足，运行时参数仍由LLM提取；约束歧义可用内部默认值，用户人工审政策仍重要。ASB十场景、EICU和Mind2Web-SC不是所有工具环境。CRP+TEH的0.1% prose与Table3平均0.0字段不能混作严格零风险。停止于形式验证边界，不读无关附件。
- [CS-RLHF 2510.03520v1](core-2510.03520v1.raw)：§4.1定理1、§4.2学习成本、§5.1设置、§6推理安全和Appendix E假设/证明。期望成本惩罚在全局最优等假设下约束的是学习成本，不是逐次真实危害。重要未决：证明以安全策略reward非负作一步，但声明仅有绝对值上界；BoN安全证明亦有此差别。Appendix E Lemma2使用的平方差上界一般还需交叉项条件。此处不能照录无条件“可证明安全”，也不因证明争议删除机制潜力。成本为Llama2-7B判不安全内容，受标注/意图和覆盖限制；停止于这些必要反证。
- [ARMs 2510.02677v1](core-2510.02677v1.raw)：§3.1–3.2攻击/MCP/分层记忆及policy judge、§4.1数据、Appendix A限制、B.1设置；另定点核优化预算段，T=30为最多30次judge反馈，不是单次攻击成功率。StrongReject60行为、JailbreakV80及具名VLM，victim/judge温度0、max1024；模型API与judge相关的自适应试探不是生产安全概率。未遍历30K攻击附件。
- [FocusAgent 2510.03204v1](core-2510.03204v1.raw)：§3、§4.1–4.2检索AxTree行及评测设置、§6–6.2注入威胁/结果讨论。GPT4.1-mini检索不看交互历史，WebArena381子集；DoomArena Reddit114文本banner/popup。过滤攻击也可能过滤关闭按钮，导致popup持续阻挡；文中低至1% ASR同时只有2% TSR，不能单凭ASR声称安全且可用。404/单图页面攻击文本支配观察仍可失效。已解决这一取舍，停止。
- [Reasoning Riddles 2510.02780v1](core-2510.02780v1.raw)：§3–4构建221谜题、50双标注子集和手工rubric，§5.3/§6–8的提示及失败边界。三商业模型，弱开源预试后被排；额外2–3倍tokens不一定带来正确率同比收益。absence/cultural失败是该数据的现象，不是透明推理因果证明。停止于必要负面评价。
- [TRACE 2510.02837v1](core-2510.02837v1.raw)：§3.1–3.3证据bank/最小答案必要步骤/单步grounding与adaptivity judge，§4.1 Meta-GTA/Meta-m&m's人为插错元评价，§5.1–5.2.1 GTA设置。效率仅对正确答案轨迹计算；fake tool近似名人为制造失败，反馈允许继续但计原错误。长答案/图像用embedding相似度，不等事实/图像正确性；LLM evaluator和合成错误不保证所有真实轨迹的真值。已读实际评价协议，不遍历全部附件。
- [Abstain-and-Validate 2510.03217v1](core-2510.03217v1.raw)：§3.1–3.2、§5.1–5.2、§7–8；174内部人报bug、198 NPE live bug、50 sanitizer，不同oracle不能直接合并。事前只看bug报告估计成功token概率；后验build/tests及生成fix spec与LLM judge。filtered-success@k条件在被接受bug/patch子集，不能替换所有bug的成功率；更严过滤减少总体修复数。§7实际错误例：spec漏掉调用点范围，judge接受了错误常量全局修改；受公司/模型/标注和已知fix筛选影响。不以过滤后的指标宣称修复正确性保证。

- [Work Zones 2510.02803v1](core-2510.02803v1.raw)：§3失败条件与场景图，§4.1代码生成/自验证，§5.1及5.2迁移。ADE/FDE是像素不是米；代码通过或到重试上限都可被存入库，不是全库已安全。所谓physical evaluation为15工区100图片及两作者标轨的open-loop，并非闭环上路。减位移误差同时P4/P8 CR可增；整体Qwen/GPT字段在表与prose有混用，不采用统一性能数字。负面规划/约束迁移潜力保留，不签真实驾驶安全。
- [Recall/Reasoning 2510.03366v1](core-2510.03366v1.raw)：§3–4.6、§5.3和§6–8。60地理问题/Qwen2.5-7B/A100/eager，最终输入token的attention/MLP统计；template与输入提供事实的差异可能混杂。top50由初始全数据选再5fold，不授独立泛化；作者明示头ablation未有因果验证。相关性不等独立recall/reasoning电路，保留这一必要反侧。
- [Plan Verification 2510.03469v1](core-2510.03469v1.raw)：III–VI完整相关方法/评测。LLM同时生成NuSMV状态和LTL；模型检查只核生成表示。PlanBench简化二分类，unknown排除于指标分母；GPT5直接判断99.59%与形式路径95.89%不支持普遍性能提升。作者实际观察到通过验证却未保留原计划意图；不授NL→formal语义忠实或现实安全。
- [SurveyBench 2510.03120v1](core-2510.03120v1.raw)：§3.1–3.3、§4设置/4.1发现。20主题；参考survey生成quiz、关键词完整性过滤与LLM证据判别均可能影响测量，要求“不看已有综述”不证明执行未看。内容流畅/局部coherence高分与quiz缺细节/综合能力可同时出现；不同writer/scaffold/backbone不因同topic就等预算。原文对DR训练原因的解释不当已公开因果证据。保留评价盲区，不把quiz分当通用学术能力。
- [SEER 2510.03490v1](core-2510.03490v1.raw)：§4–7、§8–10及Limitations。单句200非neutral、五句200组包含neutral，二者人口不同。单句先GPT4.1标签再双人agree筛选/类别平衡；五句人标无GPT筛选。span F1/embedding与count处罚，hallucination仅归一后文字不在输入。14模型BF16/A40、五run，部分prompt先门槛筛模型。neutral误报与CoT反向效果是受测证据，不把情绪标签正确等同证据定位或临床同理心。
- [Carotid 2510.02922v1](core-2510.02922v1.raw)：II-A/B/D/E、III-A/B及IV限制。72病人59高风险/13低，按病人三fold避免帧级泄漏，LoRA与普通MLP适配；原图ICA文字可能导致“识别解剖”偏置。zero-shot分类塌到单类；AUC高仍可specificity差，帧多数/病人AUC不同。此非新架构贡献，但实际偏置与受限适配反侧可改变VLM评价选择，保留日期潜力，不声称临床部署。
- [NICE RAG 2510.02967v1](core-2510.02967v1.raw)：§2.1–2.2/2.4、§2.6和§4–6。300指南、9296合成query分15%验证/85%测试与70人工QA；weighted RRF+crossencoder是既有组合。必要例显示indentation令同源judge错误拒绝受源支持答案；99.5%faithfulness不是99.5%临床正确。单指南QA，不充分测拒答/跨源真实临床复杂查询；正文“防止发明信息”不是已证明保证。因具体judge假阴性边界保留潜力，不只按领域应用关闭。
- [KG-MASD 2510.06240v1](core-2510.06240v1.raw)：§4.1–4.2.6（含Theorem4.1、Assumption4.2/Theorem4.3证明）、§5.1。五角色/GraphRAG/LLM验证triples/LoRA；Blackwell dominance、consistent predictor、PL/smoothness/无偏梯度及gamma-降variance是额外假设，不由自验证自动成立。4.3把步长(0,2/L)下递推收缩简化为1-alpha*mu的一步还需alpha<=1/L，gamma仅降低variance不在固定曲率项中。线性Laplacian模拟不证明LLM执行可靠性；不借这些成熟理论给组合流程签确定收敛。保留机制潜力与证明未决，停止而不读全理论附件。
- [LegalSim 2510.03405v1](core-2510.03405v1.raw)：§3–4及§5设置、§6–8。13抽象动作、两stationary judge、十seeds，PPO两层MLP在heuristic对手300episodes后冻结；GPT4o只是另一policy，并非PPO微调LLM。规则合法动作仍可累积burden/delay，属于模拟中的系统反侧；无真实司法数据、粗规则/指定reward不授现实漏洞或法律建议。保留主线Agent环境机制潜力，安全必要命题已收窄。
- [Structured Argumentation 2510.03442v1](core-2510.03442v1.raw)：Implementation/Mining/B-ABA、Fact Checking/Feedback与Limitations。fine-tuned literal extractor+ModernBERT relation classifier产生argument graph，SAT求admissible extension；外置facts.md手工挑矛盾展示，不是自动事实真值。单向fact edges及深度截断是修改理论/工程限制，classifier 512token与0.79–0.81F1不授所有hallucination检测；GPT4.1参数规模推测不作事实。保留验证接口潜力而非可信保证，不读无关部署附件。
- [PLSemanticsBench 2510.03415v1](core-2510.03415v1.raw)：§3.2、§4设置、4.1非标准语义讨论、4.2/4.3结果讨论。IMP operator交换/罕见文字obfuscation，SOS/K两种规则表示；更复杂两个split仅选Human-Written表现最佳三家模型。reasoning/GPT4o-mini三run，其余非reasoning温度0；最终状态准确并不保证规则/trace准确，KeywordSwap掉点仍受形式长度/熟悉度混杂。该必要反侧不证明唯一pretraining因果，停止于解释边界。

## 三份准入消歧

- [CoDA 2510.03194v1](core-2510.03194v1.raw)：§3、4.1–4.3、4.7/5.1–5.3。角色组合不是独自准入依据；metadata、全局TODO、反馈halt及1/3/5迭代收益–成本饱和、去TODO与search的受限消融可改变资源预算选择，故保留潜力而不因局部任务已有覆盖关闭。Gemini2.5Pro/最大3/threshold.85，execution和条件VSR不同；不是等预算普遍优势。
- [Topic Modeling 2510.03174v1](core-2510.03174v1.raw)：§2–3.3、4.1–4.3。long input+output、topic-card与keyword assignment，NYT100054预处理30–50词，kimi-k2 judge与assignment lexical偏置。题摘“多数NTM过时”不能普遍采用；具体输入对称性/传统指标与语义抽象冲突有评价边界潜力，不按旧NLP或弱实验直接排除。
- [Financial Risk 2510.03521v1](core-2510.03521v1.raw)：§2–3、5。RAG提取/聚合后peer contrast prompt，按人工research报告ROUGE/BERTScore，无时间意识且无真实exposure测量。具体新增是领域比较流程与文本相似度收益，没有辨识通用检索/推理机制或使设计判断改变的证据，贡献关闭；不借金融风险语言升级安全研究。

共21份有限core：18必要安全/设计反侧、3准入消歧。正文均实际读到对应命题停点；不等21篇全文/附录已审或独立复核。Anthropic完整官方core另计1；OpenAI Oct3安全release短core另计1，日期隔离。
