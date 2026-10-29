# Jun03 CRAM与ProtoAda必要证据、同作者近邻及实际owner

两项完整题摘/Jun02资格沿R75，不能由“多模态持续学习”关键词自动准入。现分别真读核心与必要附录；同四作者换一作、同backbone/bench/相同baseline表，属于高度相关的同研究线，不能当两份独立复制。方法不同：CRAM保expert pool、从warm-up增量决定rank并用视觉centroid混合；ProtoAda显式训练target格式码、推理预测再检索共享group/global/residual层级。不是同一发布的镜像或仅新名字，暂按两个具体增量家族交独核，不把重复baseline/格式遗忘现象算两份支持。当前官方abs分别为CRAM Aug28 v3（EMNLP接受注）、ProtoAda Jun03 v2，有限所见无撤回/纠错；本包首稿误写“只见v1”，已回当前原页纠正该元数据，不影响精确v1正文采用。没有重要变更说明则不自行全文版本对比，后版不倒填Jun02。未核代码、图像素或复现。

## 02502 Cram — 必要完成，Ch30单段差额提案

[v1](https://arxiv.org/html/2606.02502v1) / [原件](SUP_CLOSE_2606.02502v1_20261025.html)。实际读§1/3–6/T1–6、A伪码、B完整format实验、C配置、D/E几何与loss、F/G顺序/OOD及H费用。拟2+2+2=6：每任务固定rank或共享覆盖→warm-up增量谱值与对已有LoRA输入子空间的残余共同筛rank、冻结旧视觉centroid而允许新expert竞争→参数扩张与复用gate须分开验，非把“正交防遗忘”成熟/未证原则借作新贡献。

一级frozen CLIP文本semantic-margin分group，二级meanpool视觉表示对各expert RBF centroid软权重；语义margin不是格式判定真值，group center仍更新，旧centroid冻结也不冻结softmax式归一竞争：加新expert可改变全部旧权重。warm-up5%、temporaryr48，SVD保σ>.08及对历史Aᵀ union的QR残余比>.99才重建expert。该几何测试不等功能缺口/任务难度，filter选近正交方向不等硬投影全部update；E明确penalty为soft，与NLL共同优化，不保证hard orthogonality/无遗忘。Eq10 gamma写同Eq8完整group之权重和即1，却文字称历史依赖；未闭old/new集合区别，不补作者精确动态权重recipe。Eq7 tildeV未完整定义、首group/单group第二margin未闭，不据此给可直接实现的全算法。

B ArxivQA交集控制同底题但Short删options、YesNo改为两statement，输入信息/难度也变，不把全部效果归纯syntax。FWCC为规则提取语义等价，不认证真实理解，MCQText→Letter不对称属局部观察。LLaVA1.5-7B/CLIP-L14-336、4RTX5090、attn LoRA、AdamW2e-4/B8/1epoch/3%warmup；精确precision/多seed未披露。T6 baseline有Attn+FFN/FFN/softprompt及不同epoch/rank，正文一概相同protocol不等同参数/compute；T3 r8对齐平均7.94只该ablation，T1 baseline r16。T1/2各任务有退、GGG Humanities47.34<48.47，不能“matching”或无OOD损失；反序/随机仍退，H图“negligible”未给全数/测seed/推理费，不授所有费用常数或任意长序列bounded growth。全部CLIP/vision前向、warmup/SVD/QR、pool扫描/存储、训练/回归计费。

actual完整读Ch30“Continual LoRA需要把Program Memory与共享权重分开”program bank及fallback、retrievable参数记忆、denseFisher分支、ContinualVLM prototype/evolution段，和随后无taskdata的子空间合并/跨层routing两段及reconstruction discriminator两段。现文已承担pool演化/错误识别与几何不是语义，但未承担**有当前任务数据时，用短warmup增量+历史LoRA输入子空间决定新增rank、再独立校准冻结centroid的竞争性混合**。唯一`TRAIN-LORA`，拟放ContinualVLM完整段及`SF-2026-ARXIV-2605-07494:end`之后、现“task prototype适合仍有任务样本可校准路由的条件”之前，加下段；不拆原段：

> 有当前任务数据时，expert扩张还可先问新更新在已有pool之外需要多少方向，而不为每个任务固定同一rank。一条[受限MCIT分支](https://arxiv.org/html/2606.02502v1#S4)先在临时LoRA上warm-up，对更新作SVD，再同时按谱值和对历史LoRA输入子空间的残余筛选新增rank；文本语义先提出group，组内视觉centroid另决定expert混合。几何残余只是容量proposal，不等未掌握能力；冻结旧expert/centroid也不冻结加入新expert后的归一竞争，soft正交罚项不提供无遗忘保证。不同插入模块/预算、格式转换的信息差异与部分任务反退限制其比较，全部warm-up、SVD/QR、编码/路由、pool驻留和新旧任务回归均计费。方向筛选、路由或总预算失配时，保留固定rank、独立adapter、可信rehearsal与base回退，而不让参数更少替协议或能力保持签字。<!-- source-family:SF-2026-ARXIV-2606-02502 -->

## 02576 ProtoAda — 必要完成，Ch30相邻独立单段差额提案

[v1](https://arxiv.org/html/2606.02576v1) / [原件](SUP_CLOSE_2606.02576v1_20261025.html)。实际读§1/3–6/T1–3/Limitations、A投影完整证明、B训练/推理伪码、C格式统计及D顺序对照。拟2+2+2=6：语义相近任务共享adapter会混响应协议→用训练target得到格式统计teacher、部署只从输入预测格式码来构造group检索→必须验证train-only格式oracle与真实输入侧路由资格，不让语义接近或oracle成绩批准实际retrieval。这一具体接口不同于CRAM只CLIP文本分group，未把投影定理本身当新贡献。

格式code由target长度/离散token分布/模板统计组构造，C增加unique ratio、tokenidmean/std/band；所谓tokenid统计“tokenizer-independent”不成立，必须绑定tokenizer。两层MLP用text descriptor预测训练code，推理无target；cosine>.91只是code相近不等协议正确/稀有格式保障。训练prototype为task平均，推理单sample，冷group统计阈值初始化、Norm学习和组漂移未完全闭合。FFN hiddengradient norm而非平方energy，TopM加positive历史usage是reuse prior不是抑制多用层，不能私改负号。特定任务matrix增量/LoRA因子坐标在purification/投影/concat/SVD的具体实现未全闭；A仅Frobenius投影最近点与正交分解，不证明group-compatible语义、保旧或projection后任意LoRA坐标等价。定期promote global并删除residual还需验证更改后的权重/路由，而不是coverage比率自行授权删除行为。

同LLaVA1.5-7B/CLIP、4RTX5090、AdamW2e-4/1epoch/3%warmup；r0TriGap8/UCIT16、residualr2、M24、K5，未披露precision/B/seed/完整推理与训练账。T3称全部r8但baseline60.79复用T2值而别处baseline预算不同，不能净归format。T1十项按表直接均值46.928%而印47.23%，精确headline/gap不采用；UCIT各项平均74.655与74.66相符。FloodNet74.03等有明显反侧；Reverse70.83/Random71.17低于74.66，非顺序不敏感。固定“128M→111M”仅十任务局部存储不是长序列亚线性定理，global/group/residual/prototype/MLP全计费，非所有memory；一次生成forward不含外部双编码/检索/合成所有准备。未采用完整SOTA优越/无遗忘或格式因果唯一性。

实际owner及相邻内容沿上项完整读。现文有versioned task prototype、cold routing/漂移，但没有**由训练target格式统计构造teacher、部署输入预测code而形成oracle-vs-real-routing两人口接口**。拟在上项CRAM段后、同一个原“task prototype适合…”段之前补以下独立单段；若CRAM处置变化，可直接接既有07494完整marker后，不依赖其书稿存在：

> 语义prototype还可能把需要不同响应协议的任务放进同一组，因而格式信号的取得方式也属于路由合同。[ProtoAda的受限分支](https://arxiv.org/html/2606.02576v1#S4.SS1)用训练target的长度、token分布和模板统计构造格式码，部署时不读target，而由输入侧描述预测此码，再与图文表示共同提出group。必须分开验oracle格式码、预测码误差与实际group/协议结果：code cosine高不保证正确路由，task均值训练也不自动覆盖单query或新格式；token-id统计更要绑定tokenizer。按group投影保shared增量、另存低秩residual只是参数组织，Frobenius最近点不等语义兼容或无遗忘，周期合并/删残余仍须行为回归。有限任务/预算与表内人口不一致不授普遍优越，全部target统计、编码器、预测器、检索/组合、存储维护和新旧任务验收均付费；格式不可预测、prototype漂移或维护不合时，保留显式协议分组、独立adapter与可信rehearsal，不由语义相近自动批准共享。<!-- source-family:SF-2026-ARXIV-2606-02576 -->

## 交付

两项首次必要/actualowner ready，literal只是具体申请，未写Books。原MODEL18与另四具名必要均已读到支持/关键反证足够，本日不再以未读附件延伸普通队列；root独核和已授具体SAVE/POST继续，有限发现stop准备另交，不授DAY。
