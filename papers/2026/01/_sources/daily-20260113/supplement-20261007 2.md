# 2026-01-13 增量补查停点

检查时间：2026-10-07T16:55:45+08:00 起。作者：supp_jan13。状态：完成，root非作者完整日级验收通过。

## 范围与复用

用户授权只补既有 Daily 遗漏；原窗口、50 家族（49 论文 + Kimi CLI 0.76）、日期、评分与有效审阅不改。新增窗口是北京时间 2026-01-12 完整自然日。旧 50 仅供去重，原 24 Books 整合、15 具体已有覆盖、11 仅报告及非作者验收保留；不采旧Weekly；原“不写Books”为未授锁阶段限制，之后仅逐项接受root窄锁写入对应25篇差额及自身末注，不写LS，不stage/commit/push。

已完整重读 AGENTS、当前 Research/Report 合同、统一 Prompt、Daily 来源与主题路由、ROADMAP 与 2026 增量停点；只加载本日材料。完整题摘集合冻结46个具名项（10+32+月页相关4），不是46候选。最终30新增候选=25长期差额深入整合+5低分报告关闭；9贡献前关闭、2窗前、5日期held。独立46 AB与必要PRE见同日admission-audit；25实际正文/完整邻接/自身末注已由root非Books写入者逐篇POST PASS。root已实际顺读完整六部分、新30表/证据、14源有限停止及五held边界，DAY PASS，本日完成；不自接下一天。

## fresh 有限来源检查

实际原 HTTP 紧凑字段见 [institution-fresh-20261007.json](institution-fresh-20261007.json)。下列网页返回均为本轮 fresh 打开，不复制旧扫描的阴性结论。

| 来源 | 实际入口、停止与结果 | 限制/恢复条件 |
| --- | --- | --- |
| SRC-OPENAI | Research/RSS；feed HTTP200，本窗邻接 Jan9 SB Energy/Datadog、Jan13 Zenken、Jan14 Cerebras；一次feed不继续旧正文 | 当前feed不证明已删除历史完整；web XML不支持通过原HTTP恢复 |
| SRC-ANTHROPIC | Research HTTP200，嵌入publishedOn Jan9 constitutional classifiers→Jan14 property-based-testing跨窗；止于该slice | 不授全站无发布 |
| SRC-GOOGLE-AI | Research January月页，Jan12 NeuralGCM降水为暂缓科学应用；DeepMind Blog首页/有限page4恢复失败，pubs year2026失败 | Google pubs与DeepMind历史本窗dated列表未恢复，外部终态隔离，不作零命中 |
| SRC-META-AI | Research正文0行 | 必要历史dated目录不可得；不作零发布 |
| SRC-QWEN | 旧blog redirect；真正research-list API HTTP200/60条，最新Dec23 2025；不继续旧正文 | 官方目录缺2026切片，本窗历史未恢复 |
| SRC-DEEPSEEK | 主入口及updates HTTP200，2026 Apr24→2025 Dec1邻接，跨窗停止 | 单页不能恢复已删事件 |
| SRC-MOONSHOT | Platform Blog当前列表及kimi-cli releases per_page100 page1；Jan12 13:11:16Z的0.76与原家族同事件，复用有效review | 不重复计两个PR；不扫别的仓库 |
| SRC-TENCENT-HUNYUAN | Research超时；POST publicList page1,size20,renderType0 HTTP200/9条，最早Feb3，停本页 | Jan12历史不在当前有限列表，不能认证完整 |
| SRC-ZAI | 首查Research HTTP200；GLM-Image createAt Jan13T16Z、GLM4.7Flash Jan19T16Z，窗后；原字段createAt不当论文首公开 | 当前目录历史有限，媒体createdAt不作事件公开 |
| SRC-BYTEDANCE-SEED | 真正v2 API按2026升序，论文type1,count20实19,total82,next20；原PublishDate=1768838400000毫秒换算BJT Jan20；blogtype2实14,total19,next空，原1770825600000换算BJT Feb12；跨窗停止 | 原UTC Jan19/Feb11文字经root独核纠正为BJT；raw保留，返回差额隔离，空next不等完整历史 |
| SRC-BAIDU-ERNIE | 中文Blog有限首页这次已恢复Jan15榜单与Jan8榜单邻接，无Jan12可见项，停止不读窗外榜单正文 | 当前目录不能保证已删事件 |
| SRC-XIAOMI-MIMO | 首页Paper dated邻接Jan8 report/Feb3 HySparse；Blog当前无dated完整历史，有限首页止 | 无日期Blog不进本窗；收到准确本窗官方事件才定点重开 |
| SRC-MINIMAX | 英/中文Blog有限首页，Jan27/Dec23跨窗；Agent TechBlog目录15行无dated全历史 | 无dated Agent历史不能认证无发布 |
| SRC-ARXIV | 四主题有界API及下面月页band题名恢复；catchup失败保留；未扫Weekly、全类题摘或无关附件 | Submitted只是发现线索；日期/必要原文不够的具体隔离 |

## arXiv 查询、恢复与日期权限

[fresh四主题原返回](arxiv-fresh-20261007.json)：提交缓冲202601081900～202601091900 UTC，model主题103行（start0=100/start100=3）、systems2、agent97、multimodal41；每页max100、submittedDate升序，已到各主题total。243行有跨主题重叠，不能写243新论文。主题覆盖language/Transformer/MoE；LLM/GPU/kernel的系统分类；agent/reasoning/tool/retrieval/memory；multimodal/diffusion/world/VLA。这些不是逐项全文队列。

真正月页是ISO `/list/<category>/2026-01`；旧`/2601`原HTTP404，catchup web cache miss，不当零。CL/CV/PL各有限第一页show2000仅提取05300～06030 ID band题名作命名机制查漏，CL74/CV60/PL2行见 [月页切片](arxiv-month-title-slice-20261007.json)；不读全部月题摘，也不把band等同公开日。具体相关新题名TIME05300/TAGRPO05729/SceneFoundry05810/VideoAR05966已定点完整AB；TIME日期隔离、另3完成限定证据/Books/POST，不扩全类。

完整精确v1题摘与真实DataCite字段分批保存在 [batch1](abstracts-new-batch1-20261007.json)（10具名）和 [batch2](abstracts-new-batch2-20261007.json)（32具名）。它们只是已完成题摘判断的材料，不是42候选或42已审阅。四查询去重后192具名线索仍不转全部题摘队列。首批6清晰机制、3边缘、3代表负侧已由root实际完整AB独立校准，见下；只推进已明确贡献与决定准入的歧义。

日期须联合[官方ID首次公告分配与排程](https://info.arxiv.org/help/availability.html)、精确v1 Submitted所处normal Thu14～Fri14 EST批次、逐ID真正registered可访上界，并查当前官方作者/项目更早版本信号。normal批次的最早公告自然日为BJT Jan12，registered Jan12限制ID已存在上界；registered本身、Submitted、Updated均不单独授首公开。只判断日期，不追秒。首6abs现有外链恢复见 [date-links](date-links-first6-20261007.json)。

已经发现早公开反证：05972 Categorical Foundations for CuTe Layouts，v1作者GitHub README指向[Colfax原文](https://research.colfax-intl.com/categorical-foundations-for-cute-layouts/)；该页Revision History写2025-09-21 Initial release、09-24 typos/exposition，正文已有Tuple/Nest、tractable、composition/division兼容理论，并链接paper。因此Jan12 arXiv不当首次新贡献；不为证明改名或无新版本扫描174页。窗外首公开线索留Sep21，仅重开对应旧归属，不阻塞本窗；没有本窗重要修订的具体信号时不列新候选。repo July23 created只作线索，非正文公開证据。

## 当前准入校准范围

root完整AB校准：05684 FLRQ、05607 DHPO、05823 SendVAE、05588 AR ranking、05637 GenCtrl机制入口通过，仍须日期及必要证据；PAC不扩普遍控制，probe不作因果。05972 CuTe早公开排窗外。05336 GAMMA的VLM+gaze技能组合、05473 ESS教育概念框架贡献前关闭。边缘05437有intervention，不能按局部probe自动排除；05495只在state reuse/dependency歧义处定点；05564核真实event timing与silence/overlap评价；05487不得自动按工具组合排除，补写作时证据循环。该校准只计一次，未增平行审计。

### 日期补充隔离

GenCtrl官方[OpenReview HJTFgDYoLO](https://openreview.net/forum?id=HJTFgDYoLO)与SendVAE官方[匿名稿 bsmKEJfaar](https://openreview.net/forum?id=bsmKEJfaar)有真实更早版本信号，但forum验证挑战、API2 id/forum及API1均403，未恢复可靠首公开自然日。检索的“last year/7 months”不授日期。Apple GenCtrl正式页March2026、SendVAE repo createdApr1/两次初始commitApr1–3都不能否定更早匿名稿。两项日期未知具体终态隔离；有效题摘/定点方法保留，不以registered Jan12覆盖，不绕date继续深审。只在官方forum首公开dated历史可访后重开。

FLRQ官方Nov2025 poster名录仅有标题，不证明原文更早公开；AAAI正式页dated2026-03-14。DHPO官方repo为ACL2026 Findings；其OpenReview检索相对日期不能单独证明更早公开。ARR精确题名2025检索未恢复官方早稿。其余已正常公告批次下界+DataCite真ID上界的联合口径送root校准，未追秒。

### 四个准入歧义的历史定点结论（保留改判前证据；终态以下节为准）

| 家族 | 实际必要原文、具体判断与停止 | 拟评分/处理 |
| --- | --- | --- |
| 05437 Moral Foundations | [v1 §5.3、§7、B.3.2](https://arxiv.org/html/2601.05437v1)：Llama宏方向受norm纠缠时SAE微方向恢复，Qwen可分离时宏更强，改变不分geometry一律选稀疏steering的判断；两7–8B英语MFT问卷，base/aligned未分离。作者“无meaningful能力损失”与MMLU微steering最大4.3/4.9点下降并列保留；附录±2 sweep描述与Qwen±100实报不一致，不能授安全无副作用。核心/直接反侧已读即停，不全附录。 | 2/1/2=5；因中心收益宣传/反侧冲突定点加深，日期及独立复核未完成 |
| 05495 MMViR | [v1 §4.2–4.3](https://arxiv.org/html/2601.05495v1)：CLIP/KTS切scene、现成MLLM三级caption、Contriever timeline top-k再展开，没有新state reuse/dependency机制；Limitations明确summary索引漏细视觉。优势不能让现成分段/检索组合自动准入，具体贡献前关闭。 | 不评分、不深审 |
| 05564 HumDial | [v1 §4/Table3](https://arxiv.org/html/2601.05564v1)：在语义节点演绎overlap而非random track mixing，Interruption五类/Rejection四类分别评价含backchannel/side-talk/silence；最快0.624s系统总55，1.260s最高76.6，说明单快答指标遗漏不应响应事件。只准入可观测交互contract，不因新task名称。A6000 Docker固定环境；情绪track不搬为该机制证据。 | 2/2/2=6；标准review，日期及独立复核待 |
| 05487 EvidFuse | [v1 §4.2/§5.4/AppendixA](https://arxiv.org/html/2601.05487v1)：writer在待写claim前request+pause，chart/caption实际返回后resume；w/oWriter明确全叙事完成后再render，对照的是证据到达与叙事固定的顺序，不发明dependency/version/commit协议。表8例如OWID API43.2/1511.4s，对Direct3.4/179.33s，并保留代码失败导致证据不足。只支持本报告生成负载；没有复现生产保证。 | 2/2/2=6；拟准入，顺序边界送root校准，未据高指标自动收 |

### 首批正常落窗入口的历史必要证据进度（其后的PRE/POST已覆盖待项）

05684 FLRQ精确v1已读§Method/R1-FLR/BLC、Table8–10。不能把amax proxy写成全局最优精度：rank-1 deflation按q/k、memory x、slope t停止；收益结合BLC。Table9 LLaMA2-13B fixed64为avg4.44bit/PPL4.98，flexible21.9为4.24bit/PPL4.98；BLC Table10也有OPT13B W4 10.11→10.13反侧，不能“每条件提升”。A100量化时间与AutoGPTQ融合kernel延迟代价4–6%分别归属，不混成无延迟成本。拟2/1/2=5标准；独立证据/owner差额待。

05607 DHPO精确v1已读Eq8–11/§4.1/Table1/branch-clip ablation。先分别clip再mix才实际增量，系数stop-gradient entropy minmax，不声称给sequence scalar advantage创造新token因果credit。Qwen3 1.7B/4B/30B-A3B，32H100，SimpleRL8192，rollout512×16，train4096response/eval16K，temperature1；4B固定mix均55.4高于entropy54.3，不能普遍动态mix更优。拟2/1/2=5标准；独立证据/owner差额待。

05588 ARR精确v1已读§3假设与§4.2–4.3：DE complete-ranking容量边界使用Euclidean distance及任意encoder；ARR infinite-capacity hidden function与增强embedding满秩，仅expressivity不证明有限模型会学到。token/item reweight及trie marginal是ranking目标增量；footnote7 teacher forcing后续prefix train/infer mismatch保留。实验/完整必要边界未读完，普通待办。拟2/2/2=6标准，具体知识差额若成立再加深；日期及独立review待。

其余已读AB的具体贡献理由/负侧提案已传root，未由于topic/node match自动准入，也未因工作量缩池。05542 testoracle、05882 objective/shift、06002 graph合成、05467 transpiler均只在决定准入必要时定点补核心；尚未宣布关闭或必要证据完成。

## 冻结与必要证据进度

### 46个已读题摘的分层终态（保留校准过程，最终分层不变）

- 原提案贡献前关闭13；非作者完整46AB复核发现共同理由过粗，重开05713 DTI、05722 RotateCharacter、05502 DOM、05603 TREC，并定点复核05344 Im2Sim。旧理由与以下反证保留，不为省审阅缩池。当前贡献前关闭9：05336 GAMMA、05344 Im2Sim、05403 financial scenario bias、05473 ESS、05495 MMViR、05570 CrisisBench、05751 gender persuasion、05835 news framing、05911 Pantagruel。GAMMA/ESS/MMViR已有root校准；Im2Sim精确PDF §1.1明确复用旧[17]量化方法，新贡献主要定性例子，未新增控制/失效判据，因此维持关闭，理由不是仿真领域本身。其余负侧原完整AB保留，未把相同领域或可连owner作为判断。
- 明确窗前2：05972 CuTe见上；05564 HumDial官方[12-13结果](https://aslp-lab.github.io/HumDial-Challenge/track2/results/)已有同三分轨、A6000环境、same 0.624s/55与1.260s/76.6。官方[Track2 description](https://aslp-lab.github.io/HumDial-Challenge/track2/description/)列五种interruption/四种rejection；[dated Dec13 readme](https://github.com/ASLP-lab/Hum-Dial/blob/afd63679cb5ca077e8dba987fcc5daa4835717b9/Full-Duplex_Interaction/evaluation/readme.txt)已含五/四分轨与三延迟均值，真实API commit Dec13T08:48:06Z。主页dated news为Nov17 test/rules release、Dec13结果，不把计划timeline、email私发Oct10当公开。论文构造细节尚无本日重要修订信号，不借该细节把同benchmark重计Jan12；实际完整方法已读保留，root已独立核日期反证，窗前终态。
- 日期未知具体终态5：05823 SendVAE、05637 GenCtrl、05680 AGDC、05870 IIB、05300 TIME。AGDC官方anonymous ICLR全文[3xvyPnKUpv](https://openreview.net/pdf?id=3xvyPnKUpv)已含joint discrete/continuous与EOS/长度正则，但forum挑战，早稿exact release缺失。IIB官方[anonymous ACL全文 WICf5wRXJ7](https://openreview.net/pdf?id=WICf5wRXJ7)有latent branching/IB filter，forum挑战、API1/2各一次403，搜索相对年龄不授日期；只在准确forum历史恢复后重开。TIME Submitted Thu Jan8T13:24UTC位于更早normal批次，registeredJan12仅能夹Jan9～Jan12，不能用相邻IDband授Jan12；准确公告日恢复才重开。均不绕date全读。
- 定点非作者校准后低分候选关闭5：05713 DTI、05502 DOM、05542 TestOracle、05467 STELP、05529 Safety404。DTI实际hidden均值→有限差分2×2 tensor提供局部分析工具，但单例/剪枝未来，orientation的π周期不授因果信息流；1/1/2=4。DOM有Lighthouse CLS回退而semantic audit不退的真实反侧，单试验/代理指标不授生产UX；1/1/2=4。TestOracle必要RQ1/RQ2/§V有CUT/MUT/prefix×prompt对照（36bug、2模型、5repeat），buggy正确失败70.84%而fixed正确通过58.13%，更长CoT/ToT也可反退；1/1/2=4，局部经验边界，仅报告。STELP ASTProcessor/SafeExecutor是restricted AST逐node执行+timeout/proxy局部实现，未见新隔离保证；1/1/1=3，仅报告。Safety404 complete ASCII仅30/model且按模型/难度不同，masked vision的always-B偏差不能转换为iid机器人灾难率；1/1/2=4，仅报告。身份/公开日仍按本窗联合口径核实；独立必要原文位置见同日admission-audit，不重复无关附件。
- 拟准入22的日期/必要审阅清单：05684 FLRQ、05607 DHPO、05848 GoalForce、05866 FACTUM、05688 SketchVL、05588 ARR、05589 ACR、05384 Conformity、05420 NoisyJudge、05437 Moral、05693 Circular、05776 Romanization、05858 CLewR、05913 SubDistill、05939 CEI、05487 EvidFuse、05513 LEAPS、05675 CHDP、05882 preference shift、05729 TAGRPO、05810 SceneFoundry、05966 VideoAR。前三批正常落窗的联合日期口径如上；未以Submitted/零检索结果单独确认。月页4的完整AB/DataCite在[batch3](abstracts-new-batch3-20261007.json)，TIME隔离，其余3送root原AB校准；不是把136标题全部转摘要。
- 独立定点核心修正后新增窄准入3，以上22变25：05722 RotateCharacter §3.2–3.3/4.5 Fig7的canonical→camera分阶段与joint忽略camera对照（定性，不授全因果）；05603 TREC §3–4/Table1的22/826高分歧人审样本可反转旧单assessor，τ2021 .41～.62，但保留选择偏差及转录/原音频额外上下文；06002 MoleSyn §3/5.1/6是随机走强teacher behavior-transition graph再由instruction模型合成，不只是化学比喻，Table2也未全面胜强teacher。各2/1/2=5，先核日期，再必要review/owner；Mole必要附录只15.1 sampler/15.2 RL初始化。46冻结分区为9贡献前关闭+2窗前+5date-held+5低分候选+25具体差额深入完成/实际整合POST通过。

后续完整AB独立校准已收到：GoalForce/SketchVL/ACR/Conformity/FACTUM/NoisyJudge/Circular/Romanization/CLewR/IIB都有具体机制入口；IIB随后日期held，不保准入。原增量分数不从headline或可连owner反推。

### 必要证据与owner历史提案（下节25实际POST为当前状态）

ARR §5已完成：Mistral7B-v0.3，WordNet5000/ESCI310测试；ESCI teacher是Gecko embedding rank，不是human relevance。Table2 trie marginal nDCG97.21>95.23 NTP而R@1约70<95.16；10k steps、WordNet1024/ESCI8192、greedy likelihood proxy不是全corpus beam throughput证据。提出AGENT-RAG Ch76现有generative identifier分支的ranking目标/trie marginal与条件expressivity差额，不替DE/CE生产检索。标准2/2/2=6；有限方法/核心评价/反侧已读，无实现复现。

FACTUM [v1 §3、§4.3–4.6/Table2–3](https://arxiv.org/html/2601.05866v1)：CAS按source-doc attention加权cosine、BAS first-token sink/attention、PFS FFN update magnitude、PAS attention/FFN update cosine。NeuCLIR2024 Llama3.2-3B/3.1-8B，report-level10fold、train平衡/test不平衡；labels为70B ARGUE，100human审核仅有限一致度，AUC最高.737不是实际truth gate。所谓PAS随scale反转只在8B LR为负，8B EBM/LGB仍正；长度/模型/选择组件共同变，不能归为pure scale causal law。仅内部风险sensor，4特征不是因果证明。2/2/2=6；拟AGENT-RAG Ch76 citation verdict旁补internal telemetry须外部证据校验，owner实际357–385已读，未写。

NoisyJudge [v1 §2–4/Prop5–7、§5–7](https://arxiv.org/html/2601.05420v1)：同人口iid binary、MCAR随机独立calibration、n/m正有限与q0+q1>1/interior条件下，EIF residual correction与optimal PPI++/MLE渐近等价，降低RG误分类反演的方差放大；不由standard PPI授efficient，不扩continuous/ordinal nonlinear。真实Arena三pair 414–494，10%随机human/1000split/90% CI为human preference估计，不是客观正确率；连续案例需一致nonlinear μ。2/2/2=6；实际PLATFORM-EVALUATION Ch66现有generic PPI/估计不确定度已覆盖，唯一新差额拟只补RG/PPI++等价成立条件与nonlinear边界，不重复generic human residual原则；未写。

FLRQ owner更正：实际Ch49 §量化为什么不自动加速及1391–1408 SVDQuant/静态rank分支承载量化残差/灵活rank最直接；先前Ch54建议不写重复runtime精度controller。DHPO拟唯一TRAIN-GRPO Ch33 GSPO旁的branch-specific clipping后mix，Moral拟TRAIN-RLHF Ch31宏/微表示干预geometry边界，EvidFuse拟AGENT-WORKFLOW Ch81 evidence/write顺序分支。均只有proposal，实际Books由root协调，不标整合完成。

SketchVL定点[v1 Eq1–8/Table2/§5](https://arxiv.org/html/2601.05688v1)：group terminal mean advantage＋长度加权居中FinePRM/action-KL偏差，先相加再按全轨正负号clip，clip前零和不授clip后严格守恒，也不让负轨好步骤翻成正advantage。图像标记先后回读已有ChartSketcher，不重复归新；新差额是signed step credit。Qwen2.5VL3B/7B、FinePRM7B、16A80040G、24rollouts，Table2 randomPRM/无actionKL多个项不退，7B PlotQA55.84低于base63.44；不是普遍action regularization收益、精准causal credit或free training。2/2/2=6标准，日期/实际owner差额仍待。

CLewR定点[v1 Algorithm1、§3/Table1–2](https://arxiv.org/html/2601.05858v1)：BLEU/COMET/METEOR归一平均从低similarity（easy）到high（hard），每epoch重复固定全数据顺序，不是optimizer reset；旧CurriDPO只各难度阶段一次。真实DPOP/CPO/ARPO与Gemma2/Qwen2.5/Llama3.1/GemmaX2翻译六/三语言；DPOP分支多处低于无curriculum，例如Qwen BLEU24.43→23.59，不可宣称全PO稳增。原避免forgetting是作者解释，目前未用独立旧easy retention证明causal机制。拟2/1/2=5，必要差额是跨epoch数据支持重访，不泛化所有任务。核心/反侧已读，日期及实际owner待。

有限early source checks追加（均精确题名+2025，不扫作者全库）：SketchVL→后CVPR2026正式稿；ACR→只有arxiv/非primary mirror；CLewR→无官方early全文；SubDistill/CEI/preference shift→无官方early full信号；CHDP→后AAAI2026稿，Nov2025标题名录不证明全文。检索无命中不写从未公开。IIB恢复anonymous full后按上面terminal isolate停，不继续其他附件。

### 余项必要核心（其后25限定命题PRE/实际POST已通过，不授全篇或实现）

下面均为本日精确v1；只保存实际机制、关键评价/反侧与下一owner差额，未读普通待办不改成外部缺口。作者未核artifact/复现。normal批次+ID registered联合日期口径复用；精确题名2025有界early检查、当前abs官方外链未发现明确同稿更早公开信号不等于从未公开。TAGRPO/SceneFoundry/VideoAR现项目页与后续v2只作身份/早公开信号，不借新版技术证据。

| 家族 / 拟分数 | 已读精确必要位置、采用边界与实际停止 |
| --- | --- |
| SubDistill05913 / 2+1+2=5 | [§3.1–3.2/4/5](https://arxiv.org/html/2601.05913v1)：center teacher后固定orthogonal U(d×K)，student投影V(K×K)受Stiefel约束，逐层α匹配目标能量；PRCA从teacher top1/runnerup margin导出response surrogate，β→0回PCA。未读证明A，不采用无条件0loss→CKA1保证。CIFAR100/ImageNet CNN/ViT、4层/3initialization及有限数据，Domestic Cat PCA75.1>PRCA73.1，中心化/归一也有负侧；teacher margin不是gold，投影/orthogonal维护有费。Ch29现多层projector/CKA承担一般问题，差额仅固定任务条件teacher子空间与能量标度，获PRE/窄锁未写。 |
| CHDP05675 / 2+2+2=6 | [§4.1–4.3/5 Tables1–2](https://arxiv.org/html/2601.05675v1)：先离散latent diffusion→nearest VQ code，再condition continuous diffusion；discrete更新固定replay连续动作，continuous/codeword更新用已更新discrete sg(e)，Q训练codeword，非反传整条离散选择。K仍可随2^n组合增长；8 PAMDP纯仿真、5runs/final5eval，去Seq HardGoal32.8<75.9，完整主表79.5与消融75.9属不同配置不合并。两路采样、码本/双Q有费，hardware main Not Disclosed；不授VLA真机控制。Ch26 actioncodec分支差额已PRE并授锁。 |
| GoalForce05848 / 2+2+2=6 | [§3.1–3.3/4/5.1–5.3](https://arxiv.org/html/2601.05848v1)：direct/goal-force与relative-mass Gaussian条件通道，球/多米诺paired cause-outcome与random mask区分条件/待预测结果。Wan2.2 high-noise first10 DiT ControlNet/frozenbase、3K/batch4/4A10080G、81frames16fps；不是metric Newton参数。pool50先筛valid22再success12，54.55%valid即24%all，不拿条件成功率作全部人口；视觉质量可退，26seed/5domino有限，人审10×25场景而非闭环安全。Ch25 support分离后差额已PRE并授锁。 |
| Romanization05776 / 2+1+2=5 | [§2–4/6](https://arxiv.org/html/2601.05776v1)：同文档/固定compute从头训练149M ModernBERT，native/URoman ASCII/UConv保diacritic，mono/multi分开；5任务/6文字语言/5seeds。任务需求不同，Chinese/Japanese NER/script-sensitive反退，窄转写部分修复；10K词表只边际损失不是任意共享都好。碰撞/fertility/任务fidelity一起验，不热换decoder词表或授lossless。Ch11 normalization后已有generic collision，差额是受控encoder×task边界；已PRE/授锁。 |
| Circular05693 / 2+1+2=5 | [§3.2–3.3/4](https://arxiv.org/html/2601.05693v1)：高entropy reflection可先于文本循环，last-layer sentence均值的linear probe→CUSUM累积+正常calibration阈值与persistence。每model balanced≥50loop/50normal，不给自然rare-loop prevalence；EDR.64–.76伴FPR.24–.34，约40–50句/1500tokens提前量不是latency SLO。内部关联不是attractor因果或已验缓解器，probe/calibration/白盒费；拟Ch20现repetition penalty邻接补forecast sensor，非直接阻断。 |
| LEAPS05513 / 2+2+2=6 | [§3.2.2 Alg2/§3.2.3 Eq4–6/3.3/4–5](https://arxiv.org/html/2601.05513v1)：posterior SFT attribute组合→backend search/verifier，RL多query reward；HR precision/exclusive harmonic、GR dedup pool precision（非recall）、ER以PRE dedup候选数作分母，避免仅奖励多重复查询，但可能操纵overlap。current equalquota/QPS feedback不写future RL预算controller。2M titleinverse/200Kposterior/50K RL、800K verifierpairs，eval1Kquery/20Kpairs；14B verifier overallF1 85.19，不照录allF1>93宣传；作者A/B CTR9.39→10.93/LRR24.88→16.98缺独立随机化/CI。hybrid/OCR保留，query/verifier/分页费用；拟Ch76 queryplanner差额仅pre/post过滤reward分母，actual owner待。 |
| Conformity05384 / 2+2+2=6 | [§2.2/4.1–4.1.4](https://arxiv.org/html/2601.05384v1)：line/RGB/dot先筛model-alone100images p0=1，再给文本confederates/ally/unanimity，不是同题真实多Agent。64trials/condition、difficulty10×50，difficulty相关.657、logitconfidence p=.46不能证明置信因果。isolated能力与群体行为分母分开；fresh exactHTML无§4.3/temperature；不授采样recipe，必要条件敏感性命题已PRE/Ch82独立votes后实际POST通过。 |
| PreferenceShift05882 / 2+2+2=6 | [§3.1–3.3/5.1–5.2/6.1](https://arxiv.org/html/2601.05882v1)：source→target shift里teacher生成答复自动chosen、原reference自动rejected，非相对preference judge已校准；offline SFT/pair目标与online RM+PPO/GRPO不同。Llama3.3-70B每prompt三候选/temperature.7，SFT83.37 win仍伴semantic diversity.06–.07/syntax.86→.51；online留多样性未必适应shift。10%synthetic近fulltarget依该人口，QA~3%gap vsSumm50不合并。§4必要模型/训练/evaluator已核：GPT5nano2025-08-07、order随机、diversity500prompt×16/T1，teacher3×T.7不是greedy；Ch31 objective×target差额已PRE/实际POST，不从胜率授teacher真值。 |
| TAGRPO05729 / 2+2+2=6 | [§3.2 Eq12–19/§4.1–4.4](https://arxiv.org/html/2601.05729v1)：SDE旧/新π在sample-i x_t上评best/worst下一latent的cross-trajectory clipped surrogate，并与普通GRPO组合，不是Euclidean latent distance或无偏onpolicy。FIFO bank旧latent/reward，未披露age correction/硬件bank长度。Wan2.2highnoise/HY1.5t>900、G8/γ1、320p53frames16stepsCFG3.5/internal10K；TAGBench200从TRAIN抽样非heldoutgeneralization。HPSv3 2fps均值与QsaveVQDQIA不同，Qsave HY8.01→8.05/Wan8.73→8.81有限；bank/noalignment曲线非等总费用。拟Ch33 diffusion GRPO邻接，actual owner待。 |
| SceneFoundry05810 / 2+2+2=6 | [§3.2–3.6 Eq1–13/Alg1–2、§4.1–4.7 Tables1/3–5](https://arxiv.org/html/2601.05810v1)：diffusion layout→nearest asset，count emptylogit BCE、articulation延长bbox IoU、同位置shrink/retrieve直到walkable阈值或maxiter/无replacement。floor减sum footprints只是面积proxy，不保障connectivity/机器人width，失败终止不授navigation。3DFRONT14629/3DFUTURE16563/GAP8489part，100/count5–16；collision .191→.109仍非零，walk .822 vs .774，FID29.02反差于Diffu25.00。约束梯度sign/叙述未合成执行recipe；B.1 heuristic复杂关节可过保守/不足、dataset偏差；D.2–D.3已定点读，single3090 24GB/i9-12900K，约1500训练h/3room约300s，batch128、原文称130000epochs不自行换成steps，拟Ch25可行生成/real-state分界。 |
| VideoAR05966 / 2+2+2=6 | [§4.1–4.2 Eq5–9/5.1–5.3/6.1](https://arxiv.org/html/2601.05966v1)：causal3D tokenizer去非causal temporalop、frame独立multiscale quant；past-frame KV+nextframe/coarsescale，time-ramped bitflip及后一帧firstscale继承先前flip范围、randomcausalwindow mask。UCF8K/101与proprietarypretrain/T17–65，4B4sec384×672；reconstruction rFVD61差于Omni42，same1000steps ab gFVD96.04→94.95→93.57→92.50局部；randommaskquality78.63→79.78但semantic66.64→65.89。30steps .86sec不能在硬件/预算未匹配时归单机制，20secqual非longcoherence保证；A/C已定点读，mixedprecision/checkpoint，tokenizer2000epochs/batch128；8FPS/384×672与highdynamic drift明确限制，A/C硬件仍Not Disclosed，不追无关附件，拟Ch24 AR exposure分支。不同Sep2025 VideoAR2509.24081作者/题名不同，不合家族。 |

## 当前25项实际POST与日级停点

上述“待”是保留的分批历史进度，不是当前普通待办；采用身份/精确版本/窄命题未变时复用有效PRE，不无差别重读附件。独立jan10_books_audit已完成46完整AB/九歧义/25必要原证与真实owner PRE；root非Books写入者已逐篇实际顺读新正文、完整局部邻接与自身末注，25全部POST PASS，所有窄锁释放。TREC补核exact-v1 §4 Human Assessor Agreement：826明确为|原TREC−majority LLM|>2高分歧pool，随机22；旧正文正确，无技术改写。报告80=原50+新30（25整合16owner+5低分仅报告），五dateheld、两窗前、九前关闭不混入候选。

当前实际source-family锚点/自身末注坐标如下；它们是10-07写后文件定位，前面root顺读时的完整邻接历史坐标因后续本章插入可移动。根审实际完整邻接范围见逐批消息并已核；不是仅核锚点。

| 家族 | 实际owner/正文锚点/自身末注 | 当前独立结果 |
| --- | --- | --- |
| 05684 | Ch49 [正文锚点1395](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)；末注2775 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05607 | Ch33 [正文锚点608](../../../../../books/part-04-training-system/33-grpo.md)；末注3006 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05588 | Ch76 [正文锚点134](../../../../../books/part-07-agent/76-rag.md)；末注1619 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05437 | Ch31 [正文锚点528](../../../../../books/part-04-training-system/31-rlhf.md)；末注1370 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05487 | Ch81 [正文锚点213](../../../../../books/part-07-agent/81-workflow.md)；末注1558 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05866 | Ch76 [正文锚点926](../../../../../books/part-07-agent/76-rag.md)；末注1621 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05420 | Ch66 [正文锚点2475](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；末注5728 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05688 | Ch33 [正文锚点233](../../../../../books/part-04-training-system/33-grpo.md)；末注3008 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05858 | Ch27 [正文锚点527](../../../../../books/part-04-training-system/27-data.md)；末注1590 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05939 | Ch23 [正文锚点1141](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；末注1471 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05913 | Ch29 [正文锚点258](../../../../../books/part-04-training-system/29-sft.md)；末注1199 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05675 | Ch26 [正文锚点177](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；末注1480 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05848 | Ch25 [正文锚点68](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；末注1306 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05776 | Ch11 [正文锚点154](../../../../../books/part-02-model/11-tokenizer.md)；末注437 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05722 | Ch24 [正文锚点268](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；末注1796 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05603 | Ch66 [正文锚点345](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；末注4571 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 06002 | Ch27 [正文锚点349](../../../../../books/part-04-training-system/27-data.md)；末注1320 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05693 | Ch20 [正文锚点149](../../../../../books/part-02-model/20-sampling.md)；末注584 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05589 | Ch75 [正文锚点259](../../../../../books/part-07-agent/75-context.md)；末注672 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05513 | Ch76 [正文锚点77](../../../../../books/part-07-agent/76-rag.md)；末注1296 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05384 | Ch82 [正文锚点166](../../../../../books/part-07-agent/82-multi-agent.md)；末注1080 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05882 | Ch31 [正文锚点352](../../../../../books/part-04-training-system/31-rlhf.md)；末注1177 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05729 | Ch33 [正文锚点315](../../../../../books/part-04-training-system/33-grpo.md)；末注2505 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05810 | Ch25 [正文锚点132](../../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；末注1304 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |
| 05966 | Ch24 [正文锚点1166](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；末注1794 | root非writer actual POST PASS；近文成本/反侧及旧路径共存保留 |

扫描/初筛/必要证据/书稿普通待办0；不支持正面证据的外部历史源限制与五日期held按README §5精确条件终态隔离。日报六部分、原50连续表及原§4保留已整理；本日V3校验通过，报告226/supplement33/audit3共262本地引用存在，27报告Stable IDs在ROADMAP，限定cached/unstaged diff-check无错误。编辑前原50表段SHA256=90b11f515251fbf2a8efde2ffae705aea92dacaa8a80f16dd08ad5f681e81be2与原§4前缀=13d79441bbfe237f73fd5083fb9902cf6f373ec4e50d05ed797dc8aeb9b8a875均一致（表衔接空行只为连续不改原行）。root已非作者完整DAY PASS，本日停；LS/索引由root协调，本作者不接别日、不写LS。未stage/commit/push。

## 历史首7停点（保留实际校准范围）

首7独立PRE见[同日准入校准](admission-audit-20261007.md)，root逐项授窄锁后已实际写对应owner与自身末注。FLRQ Ch49正文1395/1397、完整邻接1387–1418、末注2775，DHPO Ch33正文599/601、完整邻接591–622、末注2996；root非Books写入者已实际顺读并POST PASS。余5同样获root实际POST PASS：ARR Ch76正文130/132、完整邻接123–149与末注1613；FACTUM同章正文922/924、完整邻接914–940与末注1615；Moral Ch31正文523/525、完整邻接501–549与末注1364；NoisyJudge Ch66正文2471/2473、完整邻接2450–2488与末注5722；EvidFuse Ch81正文213/215、完整邻接199–226与末注1558。逐项核采用命题、完整交接与近文反侧，无新增未经PRE采用的技术claim，首7锁释放；这些是单项实际Books验收，不是本日日级验收。

1. 首12及后续46实际AB已独立校准；具体改判和日期联合口径送root，纠正共同理由只重开受影响集合。
2. 通过项核公开自然日与早公开信号，按3×0～3分及具体gap决定必要审阅；日期跨窗/未知具体隔离，不绕过date做深审。
3. 46完整题摘集合冻结，不再扩池；原243/192发现线索与136月题名不转逐项AB队列。
4. 新准入必要方法/评价/反侧完成后提出唯一owner差额，由root协调实际Books；未改不写整合完成。
5. 新结果融入原六部分，V3/localrefs/diff检查后交root非作者日级验收，未验收不写完成。
