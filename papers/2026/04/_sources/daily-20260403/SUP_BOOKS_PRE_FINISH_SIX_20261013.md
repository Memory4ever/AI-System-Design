# 04-03 恢复：六个必要 Source 后的逐字最小 Books PRE

作者：`apr03_author_finish`。只接本日原六家族；必要 Source 复用原 ADMISSION 顶层独核，不重读正文。完整题摘：799/829/913复用已有效层，903/1151/1161本轮实际读现存matching pinned-v1全文摘要并经`apr03_reader_finish`独核准入通过。各2+2+2=6；日期仍须复用原有效上下界链，不用题摘Submitted。以下均尚未写Books、尚未授锁或计新增实际I。

## 01161 → MODEL-SAMPLING / Ch20：PRE待非准备者独核

已实际读Ch20 EOS完整最小闭环、Sampling长程行为、Test-time Budget与轨迹内Feedback Control连续§198–292；Ch75 Context evaluation/相邻Scratchpad段§470–532。Ch20现有论点承载runtime外层预算、stop policy与model/runtime identity，却未解释相同问题/名义cap在无关context、多turn或subtask条件下改变模型自主stop的有效计算；Ch75拥有assembly/压缩与事实视图，不接管model stopping。故非topic映射，不因gap自动I；具体差额仅加入context-conditioned stop身份及不能由token缩短认证有效预算节省。

位置：Ch20 `Test-time Budget 是 Runtime Policy，不是免费能力` 中，现句“`reasoning budget + stopping policy + model/runtime version` 绑定到同一 evaluation subject。”之后、现“文本信号还可以定义一种不同于答案正确率的停止风险”之前，只插下段：

> 名义上限相同，也不意味着模型实际使用了相同推理预算：同一道题加入无关长前缀、换成第二轮或嵌入子任务，可能改变模型自主结束thinking的行为。因此还应把context条件、turn位置、子题分摊规则与实际生成/验证行为写入评价身份，分别检查最终质量和完整Prefill/Decode费用。[受限context对照](https://arxiv.org/html/2604.01161v1)观察到verification文本与生成长度变化，同prefix末段重采样支持有限stop差额，却不证明质量变化全由少验证造成；个别模型/条件也生成更长，子题token除二不是同单题budget。无关前缀本身增加Prefill，较短trace不自动节省总成本，外层cap和deadline仍保留；条件变化或质量退步时应回到原单题/turn人口与独立答案验收，不把compaction或继续生成视为已经验证的修复。<!-- source-family:SF-2026-ARXIV-2604-01161 -->

本人末注拟追加在Ch20 Review notes内部，不新增机制于其后：

> - `SF-2026-ARXIV-2604-01161` — Daily `2026-04-03`；[Reasoning Shift exact-v1](https://arxiv.org/html/2604.01161v1) §3–4/必要A/B。2+2+2=6，限定context-conditioned stop/effective-budget差额；same-prefix重采样非完整质量中介，subtask分摊非同budget，个别长生成与Prefill费用保留；work-in-progress，不授已开发mitigation、内部推理因果或生产保证。必要Source复用有效独核，准入本轮补核；PRE/实际POST待完成，未核代码/复现。

## 00829 → TRAIN-SFT / Ch29：PRE待非准备者独核

实际读Ch29 `Distillation不是Teacher越强越好`、同prefix音频/文本CORD与`Privileged Teacher Evidence`完整相关邻接。现有论点已要求teacher不是gold、共享prefix/输入配对/双模型成本，却没有frozen text-query teacher直接读取student multimodal K/V的监督依赖边界；冻结权重不恢复原语言teacher的独立输入。Ch23拥有感知/融合接口，objective及监督资格归Ch29。只插一段在现`### 跨 Tokenizer 蒸馏需要共享概率接口，而不只是共享文本`之前：

> Teacher权重冻结，也不意味着监督仍来自独立的原语言路径。视觉语言适配中，可让原LM的text queries逐层读取student产生的multimodal K/V，以共享记忆提供vision-conditioned监督，再按数据来源决定是否采用该teacher信号；此时memory provenance、层坐标与来源资格须进入objective身份，teacher和student的一致不能作为独立真值。[受限选择性蒸馏对照](https://arxiv.org/html/2604.00829v1)支持这个无部署新增adapter的训练分支，却同时改变uniform/selective的权重与温度，不能把净差额全归于选择器；OCR、DocVQA及部分语言任务仍退步。部署撤去teacher不消除训练中的双模型forward、activation与memory费用。来源信号失配或模态/语言回归时，保留原student、可靠配对SFT或经单独验收的统一KD，不从语言平均恢复推出全部能力保留。<!-- source-family:SF-2026-ARXIV-2604-00829 -->

本人主Review notes内拟追加：

> - `SF-2026-ARXIV-2604-00829` — Daily2026-04-03；[LinguDistill exact-v1](https://arxiv.org/html/2604.00829v1) §3.1–3.2/4.1–4.4/5/6、Tables7–10。2+2+2=6，frozen teacher读取student K/V与来源监督资格差额；保α/T共变、OCR/DocVQA/语言反退及训练双塔全费，未授独立原teacher真值、所有能力保留或生产保证。PRE/实际POST待独核，未核代码/复现。

## 00903 → PLATFORM-SECURITY / Ch72：PRE待非准备者独核

实际读Ch72 `Privacy Boundary必须覆盖全部Observable Channels` §422–478完整相关段：既有DP联合view、跨substrate unlearning、采样hook局部suppression与MeGU重定向；这些没有区分授权个性化仍允许私照训练与公开生成图的身份关联威胁。最小差额只新observer对象/循环优化责任，不搬DreamBooth机制至安全章。插在现`Unlearning 更要显式声明 secret substrate 与 observer`段之前：

> 允许个性化训练，不等于允许公开生成结果被关联回真人。保护公开reference照片以阻止未授权训练，与获授权消费私照后降低公开output的face-recognition linkability，是两种不同威胁；后者可在临时个性化更新与私有训练图像优化之间交替，用当前生成模型的denoised预测构造身份抑制目标，再继续更新个性化模型。私照扰动在这里是内部训练变量，不是公开输入保护，也不是DP或知识删除。[受限model-side对照](https://arxiv.org/html/2604.00903v1)显示关联代理下降伴随生成质量退步，held-out识别器仍可高度关联；stage/joint局部取舍也不证明不可关联。私照、参数与公开output的观察权限、FR评价人口和效用目标应分别冻结，reference微调、PGD、多个FR及完整生成全部计费；正文与主表ρ不一致不拼默认recipe。关联风险或utility未验时应缩小发布、保留人工复核或不公开结果，而非用授权训练和低代理分数批准隐私安全。<!-- source-family:SF-2026-ARXIV-2604-00903 -->

本人主Review notes内拟追加：

> - `SF-2026-ARXIV-2604-00903` — Daily2026-04-03；[IDDM exact-v1](https://arxiv.org/html/2604.00903v1) §3.3/4.1–4.3/5.1–5.3、Tables4/9/10。2+2+2=6，安全受影响深入；采用authorized personalization/public-output linkability分责。保质量退步、held-out高关联、stage/joint局部范围及ρ冲突，私照PGD非公开照片保护/DP；不授不可关联或生产隐私保证。PRE/实际POST待独核，未核代码/复现。

## 01151 → PLATFORM-SECURITY / Ch72：PRE待非准备者独核

实际读Ch72 `Learned Security Sensor与Reference Monitor必须分层`完整相关§1034–1084与`Hidden-state Monitor需要稳定Observation Point`§1085–1095；Ch82通信/策略belief与群体评价相关完整段。现有正文承载单模型layer组合、roleplay非真意图、token观察点和外部gate；未承载跨agent聚合群体feature、observer/指令标签与round人口差异的collusion资格。只把防守sensor接口接在Hidden-state Monitor标题后、现“内部 probe 若只在固定 suffix”前：

> 监控对象从单模型扩大到多Agent时，先聚合各成员的deception方向分数、差异或相似度，可以提供group-level风险线索，却不能从某成员高分直接判定群体合谋。聚合规则、成员身份、观察层/token/round、标签生成与monitor权限须共同冻结：秘密指令标签不等于实际执行，剔除未执行样本与mean-round/final-round提取又改变评价人口。[受限群体probe对照](https://arxiv.org/html/2604.01151v1)中不同特征的迁移方向会反转，AUROC只支持排序，未给阈值安全gate；缺privileged observer控制、未测adaptive攻击及初步schematic token图也不授隐写定位或普遍恶意识别。多成员activation、标签和校准均付费，闭源权限不足或transfer失稳时，保留文本/行为证据、人工升级与独立action gate，不让群体sensor取得授权或无告警安全权。<!-- source-family:SF-2026-ARXIV-2604-01151 -->

本人主Review notes内拟追加：

> - `SF-2026-ARXIV-2604-01151` — Daily2026-04-03；[Multi-Agent Collusion exact-v1](https://arxiv.org/html/2604.01151v1) §3.1–3.3/4.1–4.4/Table1及39 matched局部分析。2+2+2=6，安全受影响深入；采用group sensor/observer资格，保指令标签/4剔除/round差异、transfer反转、privileged observer缺口与adaptive未测；schematic非像素因果，不授阈值gate/universal detector。PRE/实际POST待独核，未核代码/复现。

## 00799、00913 → PLATFORM-EVALUATION-SYSTEM / Ch66：各自PRE待独核

实际读Ch66视频模态/时间资格完整相关§878–930，含输入消融、几何支持集/估计器代理与过程谓词；Ch23几何encoder/语言consumer完整相关§178–198。现有几何段是生成视频的背景/动态前景测量，不包含三视图同语义物体换pose的局部consistency；模态必要性段不包含diagram/video同一步组装状态与加入/替换description的人口变化。仅新增两项测量对象及输入资格，不以低分宣布感知信息丢失。

位置：Ch66 `### 视频评估先确认模态与时间信息是否必要`之前新增以下标题与两段，799/913各一个body且可分别验收。不是两个论文摘要节；顺序从同semantic identity/局部geometry到不同depiction/input policy。

> ### 多视图几何与跨 depiction 输入要分别验收
>
> 同一物体的semantic identity正确，不意味着不同视图中的pose与局部几何一致。可以保留静态三view与真实物体，只将中间view替为另一pose，配上self-paste/no-change负控制，独立检查局部跨view inconsistency；这不同于生成视频的背景重投影，也不等于开放式3D重建。[受限三view对照](https://arxiv.org/html/2604.00799v1)人工筛得615 pairs，控制人口仍高于chance且存在selection bias，inpainting范围也改变结果，因此低识别率不能认证所有3D推理失败或合成artifact已排除。真实view、替换/遮挡处理、人工筛选与多模型评价都有成本；bbox正文20%与生成default5%口径不统一，不拼配置。构造伪迹或支持不稳时保留原图、人审及语义/几何分项，不能用对象识别分数代替局部一致性。
> <!-- source-family:SF-2026-ARXIV-2604-00799 -->
>
> 几何对象固定后，还须确认不同depiction是否让模型看到了同一任务证据：video、diagram、加入description和以description替图是不同input政策，文本代理不会自动取得原视觉真值或同信息预算。按步骤/任务分列这些条件，能发现某类对齐收益与另一类步骤判断退步并存；[受限跨depiction对照](https://arxiv.org/html/2604.00913v1)中description对D2有益而T1/T3可退，不能由aggregate winner批准统一替换。人工description核验、解析失败计错、匹配样本与额外推理均计成本；CKA接近零和局部attention变化不证明视觉信息不可恢复或encoder瓶颈因果。任务支持或文字真实性未验时保留原video/diagram、分项测量与人工检查，不把文本更强升级为普遍视觉失明。
> <!-- source-family:SF-2026-ARXIV-2604-00913 -->

本人主Review notes内各拟追加：

> - `SF-2026-ARXIV-2604-00799` — Daily2026-04-03；[三view局部consistency exact-v1](https://arxiv.org/html/2604.00799v1) §3.2–3.4/4.1–4.3、Tables1–4。2+2+2=6，semantic identity/局部pose分责；手工筛选615pairs非6151，self-paste/no-change高chance/selection bias与inpaint残余保留，bbox20/5冲突不拼，不授全部3D失败或artifact排除。PRE/实际POST待独核，未核像素/复现。
> - `SF-2026-ARXIV-2604-00913` — Daily2026-04-03；[跨depiction评价 exact-v1](https://arxiv.org/html/2604.00913v1) §3.4/4.1–4.3/5.1、Table5。2+2+2=6，input-policy/任务切片资格差额；保V+T与TextOnly不同人口、D2/T1/T3反侧、CKA/attention非不可恢复或因果，不授统一描述增强/替图或视觉失明。PRE/实际POST待独核，未核代码/复现。
