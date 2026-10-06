# 2025-09-19 首批贡献与日期校准交接

19:59:25+08非作者独核最新：原65份v1中14943经§3～5实际对照撤回旧关闭；原月段含糊15089/14504/15048补完整v1题摘，15089恢复自纠错潜力、另两项具体关闭。总完整题摘68＝63潜力/5关闭，另MiMo先发潜力，正式0/Evidence0/Books0。FIRST和DAY按[实际独立验收](./INDEPENDENT_DAY_REVIEW.md)通过，日期/历史缺段保持精确隔离；下面作者61/4及旧关闭均保留作历史，不覆盖本差额。

14:27:32+08有限重开：14834 RES、14851 Empathy-R1、15027 CLEAR据新取得的具体消融/训练退化/安全评价边界与虚构引用反侧撤回旧关闭；65题摘现61潜力/4关闭，仍未获原公开日期，不评分、不进正式候选或Books。[差额证据](./NARROW_SOURCE_SAFETY_HANDOFF.md)列实际读到的位置与限制。保留下面原关闭记录作改判历史，不授重读65篇或整日通过。

作者Tesla；当前合同§3。下列精确v1完整题摘已实际读取（各`2509.*v1.raw`），不是全文审阅。HF19页19标题只因本日arXiv主题请求20秒超时而触发，推荐日不作first-public。17篇原始v1题摘中16潜力、1关闭；其他两明确领域标题不扩读。首次公开尚未获原始公告，均不评分、不列正式候选。请root独立校准以下理由及必要负侧；作者不自授通过。

| 精确版本 | 原有约束 → 原文增量 → 待核设计选择 |
| --- | --- |
| [15207 FlowRL](https://arxiv.org/html/2509.15207v1) | 奖励最大化可能集中优势路径 → learnable partition function及flow balance匹配奖励分布 → 探索/多样性目标是否应不同于仅max reward。不是摘要10%即授收益。 |
| [15194 EVOL-RL](https://arxiv.org/html/2509.15194v1) | 无标签多数奖励缩探索 → majority anchor+semantic novelty/asymmetric clip/entropy → 自训练稳定性与多样性分开控制；须消融共同预算。 |
| [15020 Mind the Gap](https://arxiv.org/html/2509.15020v1) | MCQA单token概率协议看似无关空格 → space与答案字母分词改变accuracy/calibration及排名 → 评价prompt/token边界不能视为能力差异。 |
| [14760 Align3](https://arxiv.org/html/2509.14760v1) | 动态场景spec不等于统一拒绝策略 → hierarchical reflection/revision及safety-helpfulness取舍 → 哪种test-time约束核对可靠。原HTML部分下载但完整abstract实际可解析，abs/v1另核。 |
| [14476 AToken](https://arxiv.org/html/2509.14476v1) | 视觉tokenizer重建/理解及模态分离 → shared4Dlatent+4DRoPE、perceptual/Gram无GAN目标 → 表示统一与任务损失取舍。 |
| [15185 ST-AR](https://arxiv.org/html/2509.15185v1) | AR视觉NTP局部依赖/跨步不一致 → self-supervised训练不借representation teacher → 生成目标如何附加语义表示约束。 |
| [15130 WorldForge](https://arxiv.org/html/2509.15130v1) | 预训练视频先验难几何控制 → 步内递归refine/flow-gatedlatent/双路径纠偏 → 免训练控制成本与轨迹误差。不是标题World即归world dynamics。 |
| [15212 RynnVLA](https://arxiv.org/html/2509.15212v1) | 人视频到机器人动作gap → futureframe→keypoint联合pretrain及ActionVAE → 初始化/动作压缩分离；须同下游与预训成本。 |
| [15221 ScaleCUA](https://arxiv.org/html/2509.15221v1) | GUItrajectory稀缺/跨OS迁移 → agents+human闭环六OS数据 → 数据扩规模/迁移边界；不是只按发布声望保留。 |
| [14233 Apertus](https://arxiv.org/html/2509.14233v1) | 开放权重不等于权利/可复查训练 → retroactive robots过滤/Goldfish与多语预算 → 数据权利/记忆损失的具体代价。v1实际标题非当前推荐标题；发布与论文分事件。 |
| [15178 STVG](https://arxiv.org/html/2509.15178v1) | MLLM融合属性动作不充分 → 子查询、logit-guided reattention、temporalassembling → grounding表示与测试时优化边界。 |
| [13399 EdiVal](https://arxiv.org/html/2509.13399v1) | 单VLM/CLIPjudge指令遵循不准 → objectdetector结合judge的人评一致性/多轮内容失真 → 评价不同轴不能聚成一个总分。 |
| [13160 FinSearchComp](https://arxiv.org/html/2509.13160v1) | searchagent领域时效与工具地域混杂 → web/plugin及country影响的局部比较 → 端到端评价是否把工具可达性误计模型能力。不是金融应用自动关闭，须条件反侧。 |
| [10402 Developer conversations](https://arxiv.org/html/2509.10402v1) | 多轮聊天不等于代码错误已修 → 真实对话errors跨轮持续/explicitfix效果 → 闭环需执行验证；fragment缺上下文可能替代解释，未授83%生产错误率。 |
| [10397 RecoWorld](https://arxiv.org/html/2509.10397v1) | retention模拟器反馈可能与用户状态混为一谈 → dualview、更新mindset及反思指令 → 可训练反馈与真实性gap。仅blueprint，决定准入所需实现/评价事实仍需窄补，未机械排除领域。 |
| [14638 MultiEdit](https://arxiv.org/html/2509.14638v1) | 噪声imagecaption与编辑种类偏差 → visualadaptive指令/编辑双MLLM数据流程及旧任务保持 → 数据选择偏差/迁移取舍；具体归因事实待窄补，不因107K数据集直接授增量。 |

代表关闭：06216 SASE全文题摘明示conceptual scaffold/research roadmap，ACE/AEE及callback命名未给新的执行/可靠性机制或验证反证；不排除协议论文整体。Materials characterization、FSG remote-sensing change detection标题明确领域应用，不引入AIforScience或全部CV。

官方必要反侧：Sensible Agent Sep18Blog核心已读（19core0），v1 09255题摘动态what/how/低干扰在先，无需用n=10排除；Blog是否有新事件未证。TTD-DR Sep19核心draft-first/selfevolution/retrieval/消融已读，原稿2507.16075v1与Blog对应；Agentspace一句availability不披露新机制/兼容或安全边界，拟关闭本次再阐述，不声称旧稿已审完成。DIVE Sep18publication页及2507.13383v1题摘对应，人口分层harm差异有价值，但本次页面未新增结果，拟关闭再收录事件，不授首次公开日。请root核这三项关闭，尤其安全反证DIVE。

MiMo-Audio官网Sep19为date-only无时区，可能与窗口相交；已回官网GitHub/官方Blog核心，patchencoder4步→6.25Hz/decoder25Hz+8RVQ值得核。不能拿12月arXiv2512.23808当9月版本。正在核历史artifact/公告，缺9月准确版本/落窗前不采用。

Books拟增量0，不意味着已有覆盖；以上未获date/Evidence独立复核，尚未与实际owner论点比较。精确恢复：对应版本原公告/作者先发上下界完全落本窗→root准入→§4–6必要证据和owner比较。

## 月段查漏的实际题摘判断

实际完整标题62个，相关/含糊另48篇精确v1题摘已读，45HTML200；15114、15255、15478 HTML404后abs/v1题摘200恢复。没有据月ID决定日期。总计65篇v1题摘（17HF+48新增），不是65当窗事件/全文审阅；以下42新增潜力、6关闭，加前16潜力为58日期未决论文家族。暂不评分或Books采用，root尚未独核。

| v1 ID | 实际增量/限制，保留潜力不授证实 |
| --- | --- |
| 14526 | Delta-KD保存teacher SFT分布shift，不假定teacher/student同最优表征；WIP及ROUGE不能授广泛知识保持。 |
| 14543 | ICL风格在structured/informal不同，多指标400作者/40k生成可检personalization盲区，不是艺术应用自动排除。 |
| 14545 | linguisticfeatures标签SFT相对prompt的输出难度控制/稳定性；人工difficulty metric不能代替任务质量，待控制。 |
| 14624 | 无forget全集条件，用optimizedprompt揭示自生成forget+迭代PEFT；未证明不可恢复/隐私擦除。 |
| 14635 | repo问答跨文件依赖/上下文策略的评价盲区潜力；576条目录本身不足，需具体对照结论。 |
| 14651 | frame语义+MCTS多轮attack与earlyintervene防御，局部安全路径/误拒及总budget待核。 |
| 14653 | UMA英文subtoken/少于3frame失效，聚合frame split两token再CTC替代，具体语言-token粒度约束。 |
| 14671 | tabletext结构损失/image细语义冲突，2.59M三路径gate+仲裁；避免全MLLMfinetune收益需所有encoder调用成本。 |
| 14689 | speech自蒸馏低秩teacher离散监督压缩，Arabic表征保持边界不是普遍LLM低秩结论。 |
| 14712 | 无goldlabel条件leaveoneout构groundtrust，不同judgment差异；selfagreement不等groundtruth，评价替代解释有价值。 |
| 14735 | languageprior conflict，proxyLLM解耦pretrain+visualrelevance动态loss；是否脱离数据风格混杂待核。 |
| 14738 | jointunderstand/generate数据mutualreinforcement潜力，240K量本身不准入；决定贡献事实需控制训练预算/数据。 |
| 14749 | CLIR第一阶段bi-encoder/MT与secondreranker交互，强reranker减translation边际却noMT仍严重退化；条件必须并列。 |
| 14814 | 多语steervector从parallelcorpus隔离，fixed/trainable保持任务能力；语言正确与质量双轴。 |
| 14837 | 语义visualedit替粗像素扰动，positive/negativehead贡献及跨semantic层复用差异；干预offtarget待核。 |
| 14882 | 精确v1标题为interleavedsemantic/acoustic（非月页Exploringlimits），更多quantizer提高声学却降语言，长期连贯取舍。 |
| 14886 | adaptiveinterview难度/动态judgeweight，相对random与fullcoverage相关性成本；相关性不能授逐项正确。 |
| 14900 | FURINA声称selfroute角相似/共享magnitude/expertloss可完全merge；输入相关稀疏选择与线性merge是否等价为必要反側。 |
| 14930 | speech引入损害纯text能力，T2T/S2T双蒸馏修正；跨模态知识保持负面证据。 |
| 15038 | CurDKV以value相关CUR保attentionoutput，attentionmass不保证output；定理假设/选择成本/实际E2E待核。 |
| 15114 | 4模型概率minimalpair将低频/语法/语义/语用分离，无独特ungrammaticalsurprisal；不以概率代理syntacticknowledge。 |
| 15148 | v1名A1，onlineconformal异步校准/3阶段reject；56.7x与4.14x非同分母，exchangeability/失配风险待核。 |
| 15174 | 自生成正确/错误label解释作preference+跨模型二阶段，低监督输出设计；classificationF1不授解释忠实。 |
| 15188 | diffusion长window远端relevance失效，softconvolutional归一化不硬分块+rejectiveFT，bidirectionality/步数/质量取舍。 |
| 15206 | groupfairness加GPTQroundobjective，4bit成本与fairness/accuracy关系；90%保留≠无性能损失或群体无偏。 |
| 15211 | slidecaptionembedding与ColPali存储/检索质量替代，纳局部RAGdesign，非因slides应用关闭。 |
| 15218 | LNE污染检测调Blocking强度，试恢复precontaminationgreedy；干预本身damage/知识擦除替代解释待核。 |
| 15248 | interdocument关系synthesizer+compute-matched3B/1T与repeatbaseline，数据重复→合成选择的实质对照。 |
| 15255 | 三tokenizer在Dzongkha fertility/continuedwords/length/runtime不同的条件比较；不授SentencePiece所有语言最佳。 |
| 15260 | Singapore4languages3scenarios安全guardrail缺口潜力，非新目录即增量，须原实验具体反例。 |
| 15335 | German同事实x-phemism minimalpair，judgmentalwords比politicallean影响，objectiveprompt未纠，事实判定混杂。 |
| 15339 | 精确v1题名QuantifyingSelfAwareness（非月最新名），AQE题面shortcut vsSCAO模型signal；prediction强不等真正自觉。 |
| 15350 | lengthspecialists+subcategoryguidance分别机器生成/润色/翻译，缩粗MGTbinary评价，长度路由成本待核。 |
| 15361 | counterfactual核心/伪相关训练+modalityexpertroute，sarcasm/sentiment局部机制，不外推一般因果无偏。 |
| 15362 | WolofspontaneousdataCPT speechencoder相对已有regionalmodel，speechLLM/CoT转录比较潜力；数据预算需核。 |
| 15373 | 三textaugmentation+TTS仅用原标签数据，4低资源语言WER对照，合成资源/去重与不同teacher贡献待核。 |
| 15403 | posthoc/modelagnostic及noiserobust自然解释uncertainty保证；解释置信不等论证事实或推理忠实。 |
| 15430 | BiRQ原inputanchors防collapse，intermediate自label与Gumbel一阶bilevel，无外部labelencoder取舍。 |
| 15447 | persona→normalizedpsycholinguisticschema steering，25persona3模型consistency/diversitytradeoff，humanquality无显著差异也保留。 |
| 15476 | sarcasm两语audio最强single，textaudio/audiovision胜trimodal，模态增加非单调的负面融合证据。 |
| 15478 | 26redteamers726prompts/四模型，textonly略强multimodal，须promptattack公平预算/annotator协议，不授全模态防护。 |
| 15485 | conformalset内renormalizedprob weightedordinaloutput替argmax，QWK减少远levelpenalty；coverage与输出pointaccuracy不同，虽readability应用仍可保留替代输出设计。 |

6新增关闭：14515 FD-SLM综述是taxonomy/fragmentedmetric归纳，未给改变同步设计的新增对照；14752 KAIO难度/私有threshold80目录，未呈现具体污染反证或新可靠评价机制；14834 essayroles+rubric+discussion相对Vanilla QWK，题摘未给超出既有分工/共识的新增执行机制、因果归因或可靠性条件；14851 emotion/cause/intention定序CoE再SFT/RL、局部humanWin44.3只支持该taskresponse，未呈现新learner/可靠心理支持边界，不授医疗有效性；14943 syntheticimplicitIE再LoRA，题摘只有该数据fit提高，未给新学习机制/稳健迁移边界；15027 CLEAR57metric描述ArgImpshortening/wordlength/persuasion，无保真/系统正确性反证或新生成机制。不是按规模/应用/benchmark统一排除，root可据具体新增事实重开。

月段余12标题不扩为全文队列：医学/临床/gambling/eatingdisorders、领域情感、humanitarianmine、patent预训、历史压迫prompt等明确领域用途，14504OmniGEC为语法纠错silvercorpus；无本窗相关纠错/发布安全标记线索。月页无历史公告头，原尾截断不授整月完整覆盖。

MiMo补核已取得最早commit完整README（`mimo-initial-readme.raw`是contentsAPI原JSON含base64）及repoAPI：created_at09/19T00:46:49Z，commit00:48:29Z，当前visibilitypublic。可证明artifact身份/提交，不单独证明当时public；必要first-public上界仍待官方公告/历史公开事件。9月原README已包含同architecture，不用12月稿冒充9月。普通author待办只剩root准入/最终独核及必要审阅依日期恢复；外部日期项继续隔离。
