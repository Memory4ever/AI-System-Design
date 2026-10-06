# 02/20 第十三有限必要包：16687 / 16689 / 16697 / 16702

精确v1核心/关键control/counter读足拟命题即停；当前四官方事件页完整题摘、Comments字段及history已实际核，均只有v1，无明确纠错/撤回声明，不扩版本史。root四项必要PRE及16687/16689/16697实际正文/完整邻接/自身末注POST通过，16702标准仅报告通过；三窄写锁已释放，非日级验收。位置为 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`。

| ID | v1 Submitted UTC | 同ID DOI Registered UTC | 北京公开范围（官方bridge推定，含起不含止） |
| --- | --- | --- | --- |
| 16687 | 2026-02-18T18:32:46Z | 2026-02-19T02:52:27Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:52:28+08:00 |
| 16689 | 2026-02-18T18:34:07Z | 2026-02-19T02:52:30Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:52:31+08:00 |
| 16697 | 2026-02-18T18:44:21Z | 2026-02-19T02:52:42Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:52:43+08:00 |
| 16702 | 2026-02-18T18:49:56Z | 2026-02-19T02:52:49Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:52:50+08:00 |

Registered沿首包官方公告/DOI桥接只作公开上界推定（1秒精度），Created只raw；不授DataCite自身定义正文公开。

## [Scaling Open Discrete Audio Foundation Models with Interleaved Semantic, Acoustic, and Text Tokens](https://arxiv.org/html/2602.16687v1)

2+2+2=6，typed-token loss/compute差额深入。§3（124–130）cold-start Qwen3 decoder、Mimi12.5Hz/前8 RVQ=100tokens/s、utterance级audio-first/text-first两种序列。§4.2（143–146）150M/10B text-token ratio sweep，不是原始小时比例；§4.3/Table1（148–188）同3e20FLOPs/1.7B/30Btokens/Yodas下semantic-only vssemantic+acoustic vs加transcript，增加acoustic codes改善Salmon却损害sBLIMP/sWUGGY，加text主要打开crossmodal读写。固定total token/FLOP不固定音频时长/每种token暴露，不能独立归因“声学竞争天然破坏语义”；选择的是整个typed-token预算接口。

§5.1（191–201）64models/7budgets、Libri dev-clean all-token NLL，对ASR/TTS相关强但semantic sBLIMP在这一区间近chance，Salmon有saturation。§5.2（203–222）C≈6ND、每budget二次fit minima再log-linear；得到data exponent大于model，且作者明确小规模flat curves/token-rate/dataquality可影响，只为本codec/mixture/≤3e20范围的loss-optimum，非通用audio信息密度/1.6x定律。§6.1（228–229）500B包含audiofirst/textfirst及约4epoch重复，不写500B独立音频信息；推理负载可选overtrain，不让train-optimum替deploymentcost。§6.2–6.3（347–369）scale后Salmon停滞/ASR与text收益不同，warm-start text知识更强但此recipe有spikes/ASR更差，不授cold-start普遍优。Limitations419–422：tokenizer/rate/RVQlossweight尚未测。

A.3（770–780）TPUv5p，WSD/AdamW/QKnorm/4096token与largebatch512；precision/独立seed Not Disclosed。未核implementation/复现。采用不依headline数值，不将author-only NLL相关授真实生成/语义保证。

actual `TRAIN-PRETRAINING` Ch28:114–137已tokenizer/lossmask与PPL≠任务分数；`MULTIMODAL-REPRESENTATION` Ch23:204–216已RVQ前缀/语义首层与重建权衡，但没有**固定compute的audio token composition改变可见时长和task-family收益，all-token NLL的loss-optimum不可直接作为semantic或部署最优**。拟只Ch28 PPL段后一个自然段，把typed-token人口/codec-rate、任务分账与loss-optimum范围连起来；不重复codec实现或另写Scaling law指数，不授text-first/cold-start统一排名。

## [Are Object-Centric Representations Better At Compositional Generalization?](https://arxiv.org/html/2602.16689v1)

2+1+2=5，representation/resource边界差额深入。§3.1/3.2（99–144）CLEVRTex/Super-CLEVR/MOVi-C属性组合holdout、easy/medium/hard、40k训练图；DINOv2/SigLIP2 patch vs在每dataset variant额外训练SlotAttention bottleneck的7slots；T5 question+2/5层分类reader。oracle GT属性仍可COOD失败，表示正确不充分。匹配表示shape通过downstream jointlytrained cross-attention；footnote143明确**不计CA compute**，额外OC pretraining也非fullpipeline等费，不能把downstream FLOPs写端到端。

§4.1/4.2（307–333）ID随组合少变易，COOD下降；小reader/更难COOD下OC有局部优势，大reader/easy下dense可反胜；k-means扩更多tokens可接近部分配置，不能把任意slot天然当对象或更细causal模块。§4.3/4.4（335–362）matched downstream FLOPs/data-size/diversity切片与dense高资源追回，不证明独立唯一object-binding因果。B.3/C（826–842）b128/lr1e-4CE，DINO最大配置600k收敛，其他按ratiocheckpoint且小表示饱和后cap；joint CA/readout工作量与额外pretrain要另计。synthetic labeledVQA不授real worldstate/permanence/action safety，precision/hardware/seed uncertainty Not Disclosed于采用段，未核复现。

actual `MULTIMODAL-REPRESENTATION` Ch23:383–391有posterior commit与slots residual分配/串行成本；Ch25:382–410有persistent address/state真值，但未承载**object bias优势随组合diversity、样本和downstream reader预算改变，dense在充足条件仍可共存**。拟Ch23 slot allocation论证前最多一段：先按任务/reader/资源比较对象槽与dense，区分下游matched budget和全生命周期，不把objecttoken当composition证书；不重复持久worldstate或控制安全。

## [Protecting the Undeleted in Machine Unlearning](https://arxiv.org/html/2602.16697v1)

2+2+2=6，安全定义反侧深入。§2.1（160–171）CountMod toy task中攻击者控制大multiset并逐轮删除，使释放变成对未删D的counting queries；single-shot DP不授多release联合安全。§2.2（184–192）更小反例：initial随机z，删除后z XOR sampled-undel-y，各次边际均uniform，联合两次却暴露未删y；依共享state/previousrelease，不能把独立分布测试当jointview保证。未采用ω(1) headline/完整batch reconstruction定理，因此不扩AppB。

§3.1 Def3.1（195–212）sim只拿initial output+deleted values模拟整个updated transcript，不是逐时刻不同simulator。明确允许初始f(D)固有泄漏，不保护deleted points的自愿风险；203明写删除语义不是安全定义本身，故privacy-safe不等erase正确。§3.2 Def3.3（215–233）static-controlled Y+SideInfo/orderadaptive的sim更强，动态variant未作额外通用采用。§4 Example4.1及median反侧（267–273）：single DP sum后只减deleted value满足受限undeleted privacy但不保护deleted values；exactmedian删一个controlled1可揭中间w，不是每种任务可安全perfectretrain。§4.1/4.2（289–309）初始DP range/SQ stats再减删项只适用充分统计可DP的function，额外state/cost与utility/initial leakage另审；不授任意LLM可用线性减法实现unlearning。

理论命题无硬件benchmark需要，不作实现/法律合规保证。actual `PLATFORM-SECURITY` Ch72:388–424已有joint release/composition/不同privacy unit；2628–2636已有forget-set/retrain参照与retain utility，未承载**合乎perfectretrain仍可让他人删除泄露未删数据，安全基线是整个删除transcript不超initialoutput+deleted values，且与擦除正确性分权**。拟在Unlearning入口参照两段后一个自然段，保原重训的erase参照作用，新增retained privacy而非废弃retrain；释放/查询预算、允许初始泄漏、state与DP统计成本及限制发布回退就近。

## [Saliency-Aware Multi-Route Thinking: Revisiting Vision-Language Reasoning](https://arxiv.org/html/2602.16702v1)

2+1+2=5，标准完成拟仅报告。§3.1/3.2（175–195、274–314）以短文本principle提议多routes，population elite/evolution用consensus/diversity/uncertainty/evidence ordinal映射加权；不是新模型参数或机械执行保证。B实现（942–978）原图在每principle call可见，无regioncrop回输入；grounding summary只是count/size，SAM+captioner labelmap给fitness。Evidence只校验img/object **index是否来自grounding outputs**，不证明reason确实被该object支持；diversity/uncertainty由同model自报，consensus≠truth。最终optional aggregation输入p/g与summaries，不能称所有最终步骤必然重新视觉读取；无强制reconsult行为或因果grounding控制。

§4.1/4.2（525–579）同frozen Qwen3VL8B，μ2/λ2/τ2/T2、16bench/VLMEvalKit与answerprotocol；作者称comparable generatedtokens，但grounding/externalcaptioner、多次prefill/selection/calls、精度/GPU/重复seed成本未统一披露。不采“全部同compute低延迟”或把headline平均差额归因renewedvisualevidence。§4.3（615–620、647–662）路线/evolution组合negative、fitness偏好随aggregation变化；singledevice SAP反而更慢，parallel settings才有时延收益，机数/同步成本不授生产。Limitations907–911也承认parallel/templatedependence。

actual `MULTIMODAL-REPRESENTATION` Ch23:531与955已原图派生状态回读、visual extraction/reasoning/task证据分权；`MODEL-SAMPLING` Ch20:236–251已parallel sampling vssequential token预算区别；`AGENT-REFLECTION` Ch80:45–62已同modelfeedback与mechanical checker对象权限。SAP具体population/grounding-index算法不是全被书覆盖，但原源未证明新的reconsult成立条件；成熟搜索/加权feedback的局部组合经验与软prompt可仅报告，不因缺principle配方强造新长久机制或改分。保留实际有限证据，不删除已准入家族，不写Books。
