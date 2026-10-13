# Sep07 必要局部与普通停点

作者 Schrodinger；仅补 Sep06 完整 BJT 自然日。精确 v1 原件均在本目录 `SUP_<name>_20261011.raw`，请求保留 URL、执行时间、状态、字节数与 SHA。段号由 `SUP_inspect_20261011.py` 对原 HTML 的 headings/paragraphs 顺序产生，不是论文页码。本文不是独立签字、当窗候选 Evidence 完成或 Books 已有覆盖。

61/61 精确 v1 完整题摘已实际读；首批 5P/2EX 已获 Anscombe §4 校准。其余准入与必要局部逐项交付；公开日尚未核定，不评分、不把 submitted 当公开，也不把所有 P 都说成已完成。

## 已准备单篇必要层

| 精确材料 / 原件名 | 实际作者读取与判断 | 不能采用的结论 |
| --- | --- | --- |
| TIP 2509.05755v1 / `tip-core` | §3.1/3.2/4.1 段35–47、§5 段56–83、§7 段105–119及表格：恶意 external tool 可配置、受控 MCP client、每条件10次手工尝试；保留接口信任边界的窄 P。伦理129–132采用独核实际层，不称作者全文已读。 | API模拟反思不等真实client完整防护；§5.1 total interaction tokens 与§5.4只计恶意注入/返回且不计baseline/completion冲突，不采用端到端成本；不读或整理攻击payload。 |
| ArGen 2509.07006v1 / `core-2509.07006` | 奖励/政策组合的必要方法与消融，独核§7实际65–101/209–220/236–260/270–281层复用；窄 P。 | Python规则主要训练reward，未实现独立OPA pre/post filtering，与hard-block/<2ms宣传不合并；reward-only近似完整表现，不能说policy必要或合规保证。 |
| OpenEgo 2509.05513v1 / `core-2509.05513` | §3–4段12–30的六源统一、MANO21/camera frame/visibility/时间primitive、既有ViLT与0.1%数据实验，作者与独核实际层一致；EX。 | 资源有价值但没有替代统一设计对照支持新增形成条件；horizon变难本身不改变主线选择，不因dataset体裁关闭。 |
| LatticeWorld 2509.05263v1 / `core-2509.05263` | 作者§3–4段16–50；§8段94–104沿用Anscombe实际层。P限32×32符号layout、height-conditioned视觉投影/阶段训练及engine decode接口。 | 预设动态agent不是action-conditioned dynamics；90x manual比较依赖现成assets，不授完整生产成本。 |
| GENBA 2509.05668v1 / `core-2509.05668` | §3.2–4.2段43–66完整，固定16B token预算下1:1/9:1混合、词表fertility递减收益；P。 | 不是全局最优语言比例，延迟Bavarian理由不是干扰因果实验；硬件配置不等效率测量。 |
| Orchestrator 2509.05651v1 / `core-2509.05651` | §3段18–46、§4–5段47–58：entropy proxy/行为cost/threshold提示调整；P含hard GPT4.1-nano FE84.62%→加orch71.88%的反侧。 | planner预设，不是概率VFE/全局最优；不能用零baseline倍数证明普遍收益。 |
| ProfilingAgent 2509.05584v1 / `core-2509.05584` | 作者§4实际反馈层（17–19窄补读）；§5段14–40中评价层按Anscombe实际记录复用。P：反馈改layer pruning质量资源选择。 | quant ALL Linear与layer-selective冲突；substring accuracy、weights+buffers不是完整运行峰值；LLM因果/不同runtime速度未证。 |
| Scaling pretraining 2509.05258v1 / `core-2509.05258` | §II段9–24完整：120–350M BERT binary-code、2TB→25GB/本地驻留、128 nodes与batch184→20容量压力；窄 P。 | 不是frontier LLM的network普遍无瓶颈，不以成熟实践借用或小模型身份决定准入。 |
| FlowSeek 2509.05297v1 / `core-2509.05297` | §3.3–4.2段36–59完整：depth进入motion bases vs raw depth，对照静态收益/运动object退化；P。 | 非任意动态场景物理模型，3090/8x数字不是贡献依据或完整公平预算证明。 |
| reasoning poisoning 2509.05739v1 / `core-2509.05739` | 作者§3.1段23–25及§4–5段33–70；独核§3.3/6边界复用。安全 P：Qwen32B/s1-LoRA数学代码条件、thought hop与final wrong分开。 | architecture separation是假说，非因果或推理免疫；控制标记及filter高误报反侧保留，不整理操作trace。 |
| memTrace 2509.05449v1 / `core-2509.05449` | §3–4作者已读必要段；此次补36–37完整RF训练/已知member-nonmember、5fold/80-20。P：白盒feature下归属推断边界。 | 不授black-box、个体归属确证；output-only基线信息预算不同，semantic neighbor低recall/ngram依赖。 |
| camouflage 2509.05471v1 / `core-2509.05471` | §5段98–110、§6–7必要段，截断128–132本次补全。安全 P：rubric方向与复杂有害/简单benign混杂。 | 377/400称across-three但三模型identical，未澄清不采94.25%跨三总比例；GPT4o judge不等现实危害或防护保证。 |
| SuMa 2509.05625v1 / `core-2509.05625` | §3–4段21–59必要层，截断35–45此次完整补读：TI早/末token subspaces、projection+regularization、CA loss、窄概念SD1.4/1.5；安全 P。 | 不能把DUO组合宣传当全概念/NSFW已经完整清除；时间成本、CCE/UD有限测试保留。 |
| DualAlign 2509.10538v1 / `core-2509.10538` | 方法23–30与limitations94–98完整：临床属性/症状分布prompt及LLM标注；EX领域应用。 | privacy-preserving表述不支持隐私测量保证；100notes/3cases评估、15%细粒度标注错及残余同质性保留，不把临床效用引回模型主线。 |
| biomedical RAG 2509.05505v1 / `core-2509.05505` | 评价89–105及限制115完整：既有MiniLM/FAISS/QLoRA组合，300QA的BERTScore；EX领域应用。 | BERTScore语义相似不等事实正确/临床安全；不采用0.843 vs0.838为可泛化可靠性证明。 |

## RapidGNN 窄未决

同一家族2505.10806v1与2509.05207v1，不以admin text overlap直接全部OLD。作者本次实际读早稿§III/IV段44–67、新稿§3段33–48；确定性采样、hot set cache、double buffer、prefetch及PRNG假设早稿已有。早稿49写features组合后transfer GPU，新稿38显式steady device cache、34/40/46 SSD streaming与device memory bound；随后早稿90–93及新稿90–97实际读，早稿92 CPU memory增加，新稿93–94 CPU近似相同/GPU增加、新增Papers100M，支持保留device驻留/SSD streaming窄修订P。不同batch/epochs能耗不能作前后改进证明，不重复评分。公开日仍需必要门，不把潜在修订当已落窗。

## 后续已准备局部

- BRKGA2509.09707v1 HTML404，PDF实际200，`brkga-pdf`；bundled pypdf作者实际读PDF第8/13/23/31/33页，独核同层已通过。人工从10候选筛4近线性metric，数值计算由验证pipeline完成，LLM输出alpha/beta静态偏置注入优先级decoder。P限外部指导与搜索接口的兼容条件；random4部分优于curated4，不能归人工预算为LLM能力、free API为零延迟、未测简单监督替代为不可能。不是NP-hard应用名字即准入。
- player-profile2509.05624v1方法/评价/限制段18–45完整读，P限530维96.6%BERT→176维72.7%且行为10→48维/temporal变化下的表示和分类盲点。多因素同时变化，LLM合成静态36profile；不授semantic fundamental ceiling/人类intent不可识别定律或必须对话。
- staff messages2509.05484v1必要方法10–18及含HIPAA/PHI的段落实际读；现成Azure prompt分类/院内dashboard，EX无主线新机制或成立条件。HIPAA-compliant称述不等作者验证合规，PHI不公开不当Evidence访问失败或privacy已证明。
- GRAPE2509.04501v1 §6.1段179–235及理论说明310–314实际读。P限category rubric/verifiable或critique score/confidence聚合至relative advantage的新训练设计；proposal尚未实验，confidence逆方差是假设且非所有权重降方差，sample-level clipping有collapse风险；不因tutorial体裁关闭。
- SLM tool-use2509.04518v1 §IV/V段57–66/87–97实际读；JSON reward0.5→0.125和extraneous零reward/argument优先的capability-aware形成取舍，P。currentv2摘要这些机制原v1已有，非新版本贡献；未授strict reward全域必要。
- Emotional safety2509.04512v1 §2段13–26/§3.3–伦理37–55实际读；P仅4bit Llama3family下supervision vs size的分类/资源反侧。1B SFT vs70B fewshot预算不同，synthetic reappraisal风格混杂，全六类单run/三高数据类五run，A100 maxallocated不是真实edge、全process memory或privacy测量；不授临床安全/安全嵌入模型。
- WatchHAR2509.04736v1 §3段18–30/§6–安全47–62实际读；P限trainable audio preprocess进入runtime、LOPO vs PLOPO fusion质量/资源取舍。既有nnAudio/STFT/encoders/gated fusion来源明确；真实in-the-wild降效、无longitudinal/精细电量，不能授长期运行或完全privacy保证。
- Quantization2509.04534v1 §3/4段20–37实际读；NF4/FP16 compute/doublequant以及4×A10040GB、任务max输出50/200，窄P限12模型/8数据任务下资源质量条件。所谓consumer40GB不由A100实机证明；latency受serverload，precision转换不等原生lowbit算术普遍加速，本地部署不等privacy/clinical安全。
- Polysemantic Dropout2509.04655v1 §2.2段12–19/§3段30–38/limitations79–80实际读。P限dropout-tolerance NCM+layer pvalue有效merge；i.i.d. calibration/test条件才有falsealarm界，GPT4o语义判断和多次模型调用，不等免费/不依赖评估模型；最大drop仍不变可undefined并漏判OOD，增层有成本。
- Transformer manipulation2509.04549v1 §4/5段40–58及结论110–111作者实际读，独核额外§6.1/94–111。最初AB理论/实验声明曾保留P，必要原文实际为既有PPLM/LoRA/ROME/MEMIT说明、rank-one/orthogonality条件声明及illustrative outputs，新增>90%/安全组合最佳缺对应新对照/证明；据新决定证据改EX，不按体裁或已有Books主题关，不采用安全保证。
- CoRe-GS04859、Light-field04824、SLVM05012曾拟以singlemodal/定制场景EX，独核指出抽象理由不足。恢复为窄P：coarse semantic→PoI selective refinement/filter及修订time-to-PoI条件、Sub-SS非冗余scan/SSM spatial-angular保留局限、illumination-sensitive feature分离/decoupled multi-task融合。只保留精确v1机制潜力，不将currentv4大数字倒采，不用task名称缩池；仍需公开日后决定具体Evidence/Books。

## 当前普通待办

上述来源header/正确分页、MiMo原日期、ZAI发表字段/release、MiniMax Agent modified≠published、Rapid最小差额、InterAct/RLC身份、current轻量信号已实际处理，见Sources/Screening；不是原待办继续悬置。当前普通工作为六部分整理、精确日期保留表、独核两条补回与DAY/完成态FINAL，具体修复继续，不把独核等待当全范围结束。

## BAME安全必要层与TIP具体Books预比较

BAME2509.04515v1 HTML404后PDF200（`bame-pdf`34页），作者实际读页3/4/5/11/12：25职业组、batch24、三LLM/方法的5400stories；manual迭代query与1500sample抽取、国籍到ethnicity映射、uniform targets限定测量。模型解释只是textual artifact，不是内部reasoning或训练数据因果；不授所有fairness或质量不变。独核页3–6/12层独立有效，页11截断不冒充独核全页；作者页11完整层保留。不读冗长样例或攻击附件。

TIP预比较实际读取AGENT-MCP Ch83的“MCP不等于ToolAuthorization”及“ServerAdmission”段（151–211）、AGENT-TOOL-CALLING Ch78执行链/真实principal段（78–93）、PLATFORM-SECURITY Ch72资产/主体/trust边界（1–40）。Ch83已经明确server annotations/descriptions不可单独作信任、host policy与effect-time授权分离；Ch78拥有parse/schema/canonical/真实principal/semantic approval；Ch72外部工具不是可信主体。这只承载一般边界，不冒称已覆盖TIP受控十次实验、token分母争议及API模拟反思的具体新证据。TIP日归属未核，当前不能采用为本窗Books整合或“全部P已有覆盖”；本轮实际Books写0，未确认需共享写入的差额，取得可信公开日后只重开对应命题与owner比较。未读取的其他Books全文不称已比较。
