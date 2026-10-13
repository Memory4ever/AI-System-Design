# Sep21 最小决定事实与边界

这些是作者实际读到的必要局部，不是完整Evidence/复现/Books通过。所有本日`SUP_curl-core-<ID>v1_20261012.raw`及request保存精确HTML；16297 HTML404后恢复PDF。判断日期仍不以submitted归属。Anscombe已读相同必要层可精确复用，不全篇重复。

| 身份 | 实际位置及局部判断 |
| --- | --- |
| 16413 Pico | §3.1/3.2/Limitations：MAML PER压缩/恢复与loss同步，ReLoRA BLiMP退化/gradient illconditioning；窄P局部反侧，不按模块工具关闭，不把相关当原因。checkpointstorage/production扩规模未证 |
| 16633 MPA | §3.2/3.3/4.1及其嵌入ablation表：teacher annotation/answer一致且student不一致挑parityset，再AR SFT；窄P选择监督与预算。teacher自洽不是truth，500人工样本是局部proxy，dataset/预算不同不采普遍优于gold |
| 16457 PEvo | §3、transfer/cost/Limitations：over/underrepresented行为gap决定persona描述编辑，保持identity；窄P群体creditassignment/implicitsteering漂移，SME分布+LLMclassifier不证真实人群，后期显式行为指令是failure，不能用优化小费用覆盖全仿真API成本 |
| 16663 UQ | §3.1/3.3/Conclusion：条件CDF/coupling变换→Gaussian-independentspace；窄条件P，但边际normal与whitening不保证jointindependence，需正确conditionalcopula或jointGaussian。未采用任意分布保证/Sobol真值，不因争议改分或排除 |
| 16521 mmExpert | §2.2/2.3/2.5、3.2/3.4/3.5、5.3：motion描述时序、合成传感配对、randomization与形成表示的选项；窄P局部数据形成/transfer边界，旧CLIP/LoRA非新增贡献，RF模拟/合成caption不自证物理真值，非领域accuracy单数字准入 |
| 16522 Etude | III-D/IV-F全section：外部beat框移出TinyREMI tempo与属性，relativePos靠beat恢复绝对timing；同数据PiCoGen2*对照支持representation/factorization窄P。非全音乐保证/beat可靠性证，objective极值也不等humanbalance |
| 16407 WarpSpeed | §4.2/4.3/6.7：reservationmarker+128bit morallystrong store-release/read条件，fingerprint仍需fullkey验证；sparse-tensor contraction无delete支持专用kernel。窄P GPU并发算子边界，CPU/GPU时间不采LLM端到端数字 |
| 16444 Domain CAI | II-A/II-B/III-D：same1B general/specificprinciple与部分vague替换、SFT critique后RLAIF；窄P operationalprinciple具体化对评价的局部效果，不以mentalhealth词排除。selfassessment及resource字串得分不证安全/医疗效果 |
| 16610 LLMsPark | §3.4/4.5/Limitations：single/multiround行为反差、场景依赖，与Elo榜单分开；窄P interaction协议边界，不采用跨任务统一skill/训练原因，未证leaderboard等全局能力 |
| 16597 MCP | §3.1/3.2/4.3/5.3：复杂度vector、TD3路由与reward任务权重、static/random局部对比；窄P但中心模块“正交”/速度/策略梯度论证未认证，标准RL公式不是独立因果证明；本MCP不是Model Context Protocol |
| 16713 OPEN-THEATRE | §5.1–5.3/6.3/8：scene/turn decay、retrievalimportance回馈、event→summary/archive，director-global减少call但judge主观proxy；窄P execution/memorycost对照，memorytier名称不独自准入，不证长期truth或所有模型 |
| 16452 KRAST | IV-B/V-A：semantic/hierarchy/discriminative prompt结构对照及frames32后收益饱和；窄P表示/监督与temporalbudget，不借95.22%单个应用数字，dendrogram相关不是语义正确性证明 |
| 16360 RephQA | §2.2：专业vocab tokenweights重新分配sentence reward、group统计优势；窄P tokencredit与readability/informativeness约束，不把medicalreadability当safeorcorrect，需注意length/term-token化边界 |
| 16343 VRA | §2/4.2/4.3：多visionquery交叉核、drafter/revisor共享memory三轮，成本与robustness需分开；窄P实际查询/反证接口，crossverify不自证truth，作者把hallucination/adversarial验证明确列future，不能授保证 |
| 16513 Trace Replay | 正文（2页规模）至项目状态：MIT dataloader、heterogeneity/multitenancy、trace replay/rescheduling、Gym接口；100ms GPU/10s CPU→1s仿真，powerconversionloss；窄P资源调度测量/仿真责任，不把early PPOreward或虚拟硬件当已验证multi-tenant policy |
| 16673 MedCutMix | §2完整方法/3.3（table2后未另扩附件）：disease词选sentence、pairedattention定位latentmix、恢复encoding加入contrastloss；窄P成对语义mix及samples/layer边界，不将科学应用指标作为一般结论。无需通过Data owner引入诊断知识 |
| 21356 Phrase FC | §2.1/2.2完整与Conclusion：否定/位置/替换合成负样本，非diagonal crossmodal supervisedcontrast及location/veracityheads；窄P phrase-grounding对照，不把0.997 CCC当truth，omittedfindings尚future，source预处理label/box会传播错误；不采用临床结论 |
| 16394 Conflict Dialogue | §3.3完整/4.5/Limitations：语言词表、anger轨迹、策略distribution不是同一能力，Claude语言marker与strategy差异；窄P评价盲区，不以rank准入，roleplayhuman与BERTemotionproxy不是真实谈判truth |
| 16325 Overhearing | §5.2/6.1/6.2：被动记录/同步与异步、可见consent和可撤回/可编辑suggestions、多建议时效队列；既有引用/通用bestpractice，是否独立新机制仍请Anscombe局部校准，安全文句已读不借“alwayslistening”泛保证 |
| 16628 VCASFT | §3.2/6/9：Gemini caption人工纠错/补信息、Hindi译文修正，noimage ablation仍可回答；窄P视觉评价文本旁路与labelformation边界，ScienceQA教育问答不按科学应用标题排，caption自包含信息/人审成本不省略 |
| 16297 Designed to Hallucinate | PDF23页，仅实际p14/17/18/19及定位窗口：12模型×每condition10次shutdownprompt，automaticscoring self-preservation语言；§6.5明确scaffold/architecture混杂，§7.2–7.4不可消除架构结论没有实现/形式proof。设计反侧必要已读，准入裁决仍请独核：不能把这套实验当架构不可消除幻觉证明，也不按哲学体裁关闭。非全文已读 |

## 版本/家族

- RelRepair实际精确HTML§4.1/4.2/4.3/6.3（本次输出部分过长截断，未新声称全局成本完整已读）：queryrewrite/candidatepool/优先intrafile、test触发signature→snippet，窄P；Anscombe§5有效决定层复用。targetsimilarity与perfectFL局限保持。
- PLLM精确v2完整AB与§3.5/4.3/5.3/6.3/7.1及Table2已读，只有taxonomy/既有引用/未来gap，具体EX非survey体裁。per-userPEFT privacy无证明不采。无相关实质修订信号，不全34页diff。
- PING正文/PDF403后，官方API及v2 sourceXML `SUP_curl-ping-v2-xml_20261012.raw`200实际恢复。XMLarticle-version1.2、v1pubSep19/v2pubSep20；完整AB与revisionfn实际已读：`Figure 3 caption adjusted; removed latex formatting from abstract; slightly adjusted introduction wording`。本次v2为具名行政修订关闭，未新增机制/纠错实验或安全约束；不移旧Sep19 first到本日，不称v1 Evidence/Books完成。未diff全文，复核本次声明边界而非证明所有字符无变化。
- SFT16596 adminoverlap2409.15825：旧精确v1题摘/版本已恢复实际读，旧为dataamount/memorylevel QA激活，新token/parameter restoration在新AB不同；还需新精确v1相关§4/5比对必要命题，不能以overlap自动同事件或把旧v1当本日公开。
- AIPsycho16530评论说CogSci August已发表，必要出版方入口actual403；尚需有限原出版日期恢复，不以comment做已证outside，不追小时。

## 边界题义修正与停点

追加实际局部：Pain16727精确v1 §3生成22–43、§4.1/4.2全含Table2已读；rigging/ControlNet/Hunyuan texture均已有引用，不自称新生成primitive；只AU-specific查询定位与heatmapteacher→RGB输出/feature监督的窄P，17class正文/16class表/±1/±2容差不同必须保留。FairTune16491按实际完整AB负面形成证据改P，不采生理或普遍公平。VCASFTnoimage文本旁路P、UNIPHY/Forest具体范围EX沿独核层保持。

SFT16596新精确v1 §4/5（含Table3/4/5）与旧2409.15825v1完整AB已实际对比：旧dataamount/memorylevel，新top10-renormalized logits KL与参数变化排序恢复有独立事件差额P。恢复20%参数可覆盖>90%总variation，不是90%参数数量；局部recovery可改善不证明全知识抹除/通用安全，不因textoverlap自动同事件。

Shift必要same-family比较本日原件：`SUP_curl-core-2507.11830v1_20261012.raw`旧§2为何不能TP/DP、§3真实cachelayout不变/SP×TP=P与weightshard映射已读；`SUP_curl-core-2509.16495v1_20261012.raw`新§3.2/3.3已读（长输出一处算法截断，不声称全算法或实现复现）。旧May29博客web实际date/title/core片段可见、本地403不伪成功。新稿GQA SP>KVheads邻域复制/重排、mixed SP/TP headorder与HopperFP8 slicing vsdualmodels memoryoverhead有必要技术细节差额，不借相同名称关闭全部贡献为重复；新paper/重要事件first日仍需原发布，不把旧公开基本Shift当新Sept20事件。

Epistemic Suite精确v1 PDF实际67页（AB说65不当新版本）。HTML404后PDF200恢复；作者仅实际必要p26/p34/p35/p47及p55 B3Step7/B4；Anscombe实际§13另核p26–28/55–56：ETP是practitioner-invoked，不是autonomouscontroller；两连续弱/无materialshift循环suspend，visible rationale/context/provenance/resumptionconditions，prompt-rephrase不clear原warrant。具名权限/停止规则足极窄P，原EX撤销；不扩67页全文，没有形式验证、runtime强制/独立truth或安全保证。

20375 AI-textDetector完整AB的maxvote未超过single，Anscombe实际§13已校准极窄负面P，仅既定ChatGPT3.5/250对abstract、既有classifier/feature和maxvote3对该proxy的比较，不採通用作者身份认证或新检测算法。HTML404、PDF请求timeout只收到部分body，保留失败原件但未解析/声称全文已读；完整AB足此最小准入，额外全文不再是必要普通任务，不因失败改EX。

原14title关闭中5项含糊已定点重开，`SUP_curl-exactv1-boundary5_20261012.raw`精确v1全5AB实际读；API完整AB现105，title层9。16628转窄P并必要core如上；16727是AU rigging合成疼痛数据/heatmapteacher，16345PPG生化预测、16346生态ALS/TLS条件DDPM、16491physiologicalHR公平性为具名范围/应用层意见待独核，不借通用模型关键词回引科学任务。未读另9title项完整AB，不能称全114AB。

研究普通0，Google注册入口有限恢复、Shift实际§14、Sources及全六部分DAY§15已实际读回通过，剩完成态窄FINAL。SFT、Overhearing、16297、边界5与两改判必要层不重复列未读；AIPsycho出版方curl403/web robotcheck有限入口穷尽后只保更早首公开日需求，不把comment当已证窗外。98潜力first/event未知为终态保留、不要求全文，不支持正面Coverage/Evidence/Books或无遗漏。未确认候选不评分；没有Books写入或actualowner已有覆盖断言。
