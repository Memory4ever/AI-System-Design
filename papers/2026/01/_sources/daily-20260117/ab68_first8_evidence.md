# AB6–8 首批八项：必要标准证据与 Books 判断提案

root完整AB准入校准通过；只exact-v1，完整题名按本日XML/原HTML，不借DataCite后改标题。正常Submitted cohort、官方公告下界和registered上界给完全落窗区间；原字段在all_date_fields。未运行代码/复现实验。缓存只供复查，不称所有附录已读；以下待root必要核与终裁，不自动因recipe未写产生长期gap。

## 09823 NanoSD — 2+2+2=6，标准，拟OnlyReport

实际§3.1–3.5/§4.1–4.6/Table1–5：删E4–Mid–D4，六stage shape-compatible变体各自feature L2蒸馏，32,768组合后用teacher-aligned FID与latency/param两套目标BO，选UNet后freeze再distill VAE并end-to-end fine-tune。taFID比相同prompt-seed教师输出，不是标准datasetFID或exact manifold preservation。Qualcomm NPU W8/A16的Table1为UNet搜索：315M/27ms与160M/28ms说明参数少不等快，不把摘要20ms当完整pipeline SLO。VAE和多个任务adapter/重训均另付费，Table5 depth质量明显弱于Marigold，Table2亦非各指标全面占优。确切chipset/完整请求batch/concurrency/SLO未披露于本次必要范围，不授生产效率。

拟Only：这是局部SD1.5 surgery/蒸馏与条件Pareto可行性；Ch49现typed shape/layout/target硬件与真实measurement、Ch24 codec/denoise/decoder预算已拥有约束，没有支持把特定block库/teacher-taFID配方新增为长期通用机制。不冒已有本次实验，保留局部验证。

## 09896 LAP — 2+1+2=5，标准，拟Existing Ch27

实际§3.1–3.4/§4.3：6.5阈值、LAD已有4.5+截断入口与caption-regex PMI，是文本提及与保留概率的关联，不是真实人口分类器/过滤唯一社会因果；MET249,351与WikiArt81,444亦有馆藏/medium混杂。标注来源photography/AI-art与relative challenge ratings混成absolute rating，支持score不等人口中性质量，不能推出每个slice均受相同因果伤害。Ch27 L233–244具体已承载model过滤继承偏好，必须报告retention及语言/领域/来源分布变化，既有覆盖该采用边界；不冒其已含本次艺术实验。

## 10102 Persona — 2+1+2=5，标准，拟OnlyReport

实际§3.1–3.3/Table3/§5–6：53场景，role×payoff 2×2，四角色由同一model分别prompt，固定action顺序、每配置5次；Qwen无persona+visible在economic slice得65/90% NE，Llama/Mistral仍0。NE是作者game定义，不是人类正确偏好；family关联非architecture单因果，环境其他slice可退。完整precision/hardware/cost ND。本地控制支持persona/payoff作为Eval配置，不能推出所有role必压倒激励。Ch82已经角色/通信/runtime分责，但不假称其有这个精确交互；有限game结果不形成新通用设计定律，拟Only。

## 10310 SENSIA — 2+1+2=5，标准，拟OnlyReport

实际§2.1/2.2、§4–5直接消融、Limitations及必要C：Backpack sense mixture meanpool与last-context各InfoNCE，加target LM loss；三phase最后freeze senses/weight network，backbone/LM head仍训。GPT2 English BPE四Latin-script、OPUS bitext，150Ksteps B64 LR5e-5 FP16 seed1234；matching tokens FT/MCL有局部比较，单seed和Chinese过分切词限制保留。Top1/uniform替换weight损CE说明依赖soft mixture，不认证每slot是真实sense；Procrustes/Gram相关不是语义真值。Ch12初始lookup/context/geometry与迁移身份已给边界；特定parallel losses/phase配方未证明跨script或LLM普遍学习分解，拟Only而非精确已有覆盖。

## 10702 STITCH — 2+1+2=5，标准，拟OnlyReport

实际§2.1–2.3/§3–5.1/Limitations：LLM诱导scope/event/entity三标签，structural overlap cardinality先排序，semantic仅tie-break；coreference rewrite仍依上游标签，不是latent goal真值。CAME是synthetic closed-world，144/168/61 trajectories与LongMemEval50/50/15 subsample，4,096 retrieval budget；统一GPT5mini backbone/4.1mini judge与paired t-test仅条件支持。细event损synthesis、N50buffer迟识新event、ingestion多次LLM与完整online成本ND。Ch77 L26–40明确task-scoped区分状态/非authority，L203–205语义相似不等执行相容；具体标签密度配方与本地bench不改变这些长期边界，拟Only，不冒完全相同算法已有。

## 10712 MatchTIR — 2+2+2=6，标准，拟OnlyReport待校准

实际§3 Eq1–11、§4.1/4.3/4.5/4.6/Limitations及必要B：toolname gate+参数Jaccard/值exact形成score；KM一对一不重复消费gold，OTsoft质量分配不同，turn内平均、末turn answerF1，global组归一加same-turn index的discounted-return组归一。不是无偏因果credit，也不认证gold唯一正确path/顺序；mask外部toolresponse tokens。Qwen3 4/8B、B256/G16/L10/3epochs/8A800、λ0/γ.9；更强penalty伤recall，toolcall少不等总墙钟少，open deep-research缺gold明确限制。Ch33 L219–223已承载局部process signal与trajectory shift叠加及预算/非语义oracle边界；本次gold-set匹配的受限配方未给通用真实credit保证，拟Only而非自动长期gap。若root认为gold capacity分配本身构成可复用新机制，另裁其最低必要采用范围，不凭工具方便预定。

## 10714 Alterbute — 2+1+2=5，标准，拟OnlyReport

实际§3.2–3.5/§4.1/4.3/§5：same VNE不同图reference，target background/mask是条件；训练可改intrinsic/extrinsic，推理重用source场景，非投影约束/背景严格保证。1×2grid/左half loss，VNE由Gemini2Flash从OpenImages标注，物理Eq3仅问题形式非可运行renderer。in-place/IR/DINO reference消融支持所测supervision选择，不隔离每因素唯一因果。100Ksteps/B128/512×1024/128TPUv4约24h；30objects/100case/166美国参与者联合prompt与identity偏好，不授真实身份认证。粗bbox background artifacts及rigid shape失败直接反侧。Ch24现reference/condition支持域和编辑保真分责未被具体VNE配方改变，拟Only。

## 10710 CLI — 2+1+2=5，标准必要已读，拟长期接口深入/Ch23待root核

实际§3.2 Eq4–9、§4.1/4.3 Table4/直接density反侧：多个vision layer各LoRA+旧projector，learned q_v/q_h汇总visual和当前LLM hidden再gate。**Eq9只在visual-token positions累加visual residual，非文本位置crossattention更新；gate非语义正确性证书。** 多LLM injection consumer区别Ch23 L79–81单classification readout的多层summary融合，不只是多层特征数量。0.5B half-data直接AMP-only微小/AGF强，全projector+AGF更高但参数更多；medium density弱于sparse，不能用heatmap叫层功能causal。LLaVAOV/1.5原协议，训练/额外features与gate容量付费，18榜合计不是统一统计/全部slice普胜，latency/hardware/precision/SLO未披露于必要主文。拟只写多层表示的producer与LLM跨层consumer/visual mask耦合、读取预算和旧末层projector共存；不授必须dense injection、universal bottleneck或免费plug-in。需root确认真实owner差额后才窄写，不将本批其余recipe都升deep。
# 最新终裁（纠偏口径）

root已实际必要源/owner核八项：09823/10102/10310/10702/10712/10714按原5–6分标准Only；09896具体Existing Ch27 Quality过滤；10710真实producer×consumer接口差额最低必要深入采用，Ch23 L83/85与末注1147实际POST通过、锁释放。下列拟判断保留为必要证据过程，不再表示当前普通待办；未改变命题/版本无需重复全附件。
