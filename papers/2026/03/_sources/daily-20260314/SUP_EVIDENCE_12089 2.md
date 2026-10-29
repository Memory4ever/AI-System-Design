# 12089 EmbTracker 必要Source、具体 Ch72 差额与 PRE

mar14_supplement；只03-14补充Mar13 BJT。精确v1题名 EmbTracker: Traceable Black-box Watermarking for Federated Language Models，九作者身份与完整题摘/Work-in-progress说明已实际读；非准备者本日十项日期包已核本ID arXiv事件日Mar13，未见具名更早公开正文或撤回/纠错，未遍历完整版本。候选/评分与Books仍待非准备者独核。

## 实际原证与停止

SUP_NARROW_WATERMARK_MANIFEST_RESULT.json 官方 https://arxiv.org/html/2603.12089v1 GET200/340597bytes/2026-10-10T01:52:01.115372Z，SUP_NECESSARY_12089.raw/txt。本人实际读 III-A/B(B55–76)、IV-A–E/Eq3–4全部(B77–104)、V-A/B完整TableII(B105–145)、V-D/E完整TablesIII/IV(B149–165)、V-F–K(B166–203)与Conclusion209；前述1–54仅身份/问题与关联说明，不称必要全证明；146–148其他模型只读正文/图caption，194–203关键量化/自适应反侧。未读图像pixel的坐标/数值、全部参考、代码/复现、联邦全平台实现或无限旧版本。

实际新增不是backdoor/sig/PEFT本身，而是**一次训练通用trigger embedding → 每个client不同token行替换同一embedding → 聚合仅PEFT modules → server以通用trigger强化共享modules → 再个性化发行**。第三步PEFT不更新embedding是持久性的关键条件；server并非完全免训练，初始化外每round有reinforcement。黑盒Eq3须本client VR≥γ且其余各client VR<γ，Eq4分类目标标签/生成目标substring匹配，不认证自然语言真值或token概率。本文VI是本人VR减其他client平均VR；平均泄漏低不能直接认证Eq3要求的每个异client全部低于阈值。

III假设benign server、客户端遵循FL训练/不串谋/不知道水印，能力已含全model可见；V-K仅扩到知道一般机制但不知道原embedding位置/trigger的单客户端overwrite。TableVII原VR98.43/新99.67并存，timestamp+CA是作者建议扩展，不是已验证的抗伪归因/责任排序协议。Client signature只核其身份message，经hash映射有限token词表；必要原段未给完整无collision构造/重试/注册协议，不能由SHA/RSA名称推出词表映射不冲突或行为不可伪造，也不能让模型响应代替发行链证据。签名本身未在此认证具体artifact与发行记录的完整绑定。

10client全参与/20轮/local3epochs、Dirichletβ.5、server自有dataset；BERT分类/Llama2-7B QA/Qwen2.5-VL7B VQA。水印Adam lr2e-5/5epochs/batch4/10%poison；主要FP16/FlashAttention2，硬件、精确local PEFT配置、serving batch/并发/SLO/重复seed CI及完整CA/网络成本在必要段Not Disclosed。TraMark要求类别≥clients、只DBpedia/Yahoo分类及改写生成target，对照不是所有任务同算法能力；同水印样本数不等全训练费用。

TableII OK-VQA IID ACC49.74→46.30（-3.44pp）、NonIID46.06→43.83，CoQA NonIID70.48→68.67，不能统一说1–2%无损。TableIV SCAFFOLD CoQA73.69→70.67（-3.02pp）。V-F client数改变同时样本500→100，不授固定数据的可扩展性因果。V-H NQ1%poison VR13.76，5%96.43；V-I仅20轮训练time比较，未读图数值不造开销比例或端到端净优势。V-J pruning仅≤30%局部信号，其上质量反退不能豁免目标威胁审计；量化VR保持伴ACC显著退步，未给图pixel具体bit阈值，不认证任意compression/finetune/蒸馏/合谋。有限VR和VI不是总体零FPR、真实盗版司法归因或泄漏阻止。

## 评分及 actual owner

提案2+2+2=6标准完成，个性化发行/共享聚合/验证责任差额触发窄深入。Design2是共享backdoor载体跨token映射替代每client重训，保留embedding与公共PEFT更新分责；Reach2是server发行、client更新、聚合/验证接口联动而非单个backdoor参数；Durability2是发行身份/持久性/检测责任稳定条件，不给法律归因、宣传百分比或章节映射加分。

实际读 PLATFORM-SECURITY Ch72完整185–218可信执行→confidentiality→权重取证→协作门限→组件水印→不可伪造→trace行为取证，以及535–558 extraction与secure-aggregation attribution。现197取证非预防、199/201同方向shares是共享白盒验证权，203不同生成组件，207/209密码签名责任，211/213 trace蒸馏；都不承载**共享PEFT更新而发行embedding个性化、行为矩阵的各异client拒绝条件、API查询按client发行对象归因**。550的数据水印反推update是另一对象，不是外泄model实例。通用soundness/unforgeability无需重写，但不能用它们主题NC本具体发行/聚合接口。Ch71/73交接仅定位未变化路由，无新owner。

拟在Ch72协作门限水印两段之后（现201）、生成系统组件水印之前窄两段，不改其白盒权限假设、旧family、其他段。root独核后root写/作者非writer实际POST，不自行写Books。

### 逐字两段 PRE

共享验证权与追查哪份发行副本外泄，是两种不同问题。若可疑服务只允许黑盒查询，另一条分支可先在服务器训练通用 trigger 的 embedding，再把同一向量映射到每个 client 的不同 token 行；客户端只更新 PEFT modules，服务器聚合并用通用 trigger 强化这些共享 modules，随后重新发行个性化 embedding。[EmbTracker 的受限联邦对照](https://arxiv.org/html/2603.12089v1)据此避免为每个 client 单独重训 watermark，但持久性依赖 embedding 在客户端更新中保持冻结，不是任意 full fine-tune 的承诺。这里归因对象是发行给 client 的 model instance，不是该 client 的私有训练数据、前述门限 key 的完整性或被阻止的泄漏。<!-- source-family:SF-2026-ARXIV-2603-12089 -->

验证须同时要求本 client 的 trigger 响应达到阈值、其余 client 的响应各自低于阈值；其他 client 的平均响应低，不能替代逐个排除。签名 message、有限词表中的 trigger 映射、发行模型与 PEFT 更新身份、验证样本/阈值及后续变换应绑定留档，这些是据接口推导的验收要求，不是作者已认证的发行协议或不可伪造证明。当前原研究依赖可信 server、遵循本地训练且不串谋的 clients；新增 overwrite 测试仍保留新旧水印并存，timestamp/CA 排序只是建议。初始化与每轮强化、个性化发行存储和逐 client 查询均付费，VQA/部分联邦优化及量化质量反退保留；超出冻结 embedding、攻击或校准人口时保留 Unknown，回退签名 origin/provenance、访问控制与独立取证，不由高 VR 认定法律责任、零误报或完整 confidentiality。

此为必要Source/PRE提案，非非作者通过/实际写入/日报DAY。无代码或复现认证。
