# 第十八包：教师接口、动态监督与压缩消费者

完整PRE，未SAVE。Books上下文/ROADMAP有效；actual Ch28 Distillation两完整段/独立marker、跨tokenizer完整段及teacher-specific恢复完整段，Ch27/29开头交接已读。Ch23完整stitching两段、Switch-KD两段、离线推理表示对齐完整段与其后冻结producer/空间proposal完整段，三阶段gold-mask两完整段与GRIP完整下段均实际读。必要只消费R8/R17/R20及原本日已成最小层，不第二Methods/实现/复现。三独立差额，不用teacher主题相似判NC，不跨owner复制同机制。

## 12184 CompoDistill / 2+1+2=5 / TRAIN-PRETRAINING Ch28

R17 §4.1–4.3/T2–3首必要有效。当前Ch28 prefix/KL和文本事件对齐尚未承担**视觉key列attention群组对齐与冻结teacher projector/维度adapter分别消费**；Ch23 Switch-KD是student视觉输出进入完整teacher consumer，不是同一监督对象。唯一插位在Distillation两段/独立SF2605-16826后、完整跨tokenizer段前；不拆原source-family，Ch23不再另写。

正文：

视觉语言蒸馏还要声明究竟匹配哪种中间接口，而不只选KL方向：可将teacher若干attention层按窗口分组，把视觉key列的群组读数与student对齐；另复用冻结teacher projector，用可训练的维度映射接入student，分阶段训练这两条路径。[受限组合蒸馏分支](https://arxiv.org/html/2510.12184v1#S4)把“语言查询怎样读取视觉位置”和“视觉feature怎样进入消费者”分开，较近attention或feature仍不是相同语义、完整理解或兼容证书。层/头聚合、视觉位置、维度映射、冻结参数与每阶段数据须共同绑定，不能用一个相似度loss掩盖对齐对象不同；原印式损失方向未闭时不补精确优化配方。两个组件单用在不同任务有反退，联合均分也不识别唯一瓶颈或全能力无损。教师前向/中间状态、projector与adapter、全部阶段训练及新旧任务回归均付费；空间/词表、监督对象或净质量失配时，保同接口普通输出蒸馏、独立student训练或已验单路径，不由更小student和较高综合分批准任意异构替换与净降费。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12184 -->`

本人末注：

- `SF-2025-ARXIV-2510-12184` — Herschel，Daily2025-10-16补Oct15；消费Cicero R17 exact-v1 §4.1–4.3/T2–3首次必要，2+1+2=5，仅视觉key列attention群组/冻结teacher projector与维度映射的监督对象差额深入。保三stage全费、VAT单用GQA与TAF单用Winoground反退、Eq4负KL方向未闭，不授唯一瓶颈/任意异构或免费。未第二Methods/代码/复现；整体PRE/SAVE/fullselfread/solePOST只本日canonical实际层。

## 12283 DL-DKD++ / 2+1+2=5 / MULTIMODAL-REPRESENTATION Ch23

R8与本日原SUP_THIRD_FOURTH_MINIMUM/独核§11 III-C–F/IV-C–E有效必要已消费；原partial323492B/无结束html权限保留，不重抓。当前离线teacher解释/人工校核后对齐段尚未承担**hard human anchor、teacher/branch softscore的样本比例/插值与KD时钟分别控制**。唯一插位完整SF2605-16080段/inline marker后、完整`冻结视觉producer还可接受下游proposal给出的空间条件...`前；上下完整源论证已读。

正文：

监督的资格还可以随训练改变，而不始终把teacher相似度当固定标签：保留人工hard anchor，在选定样本中逐渐混入teacher或分支预测的soft target，另用独立时钟减弱蒸馏权重，部署再由两份student读出融合。[受限部分相关检索分支](https://arxiv.org/html/2510.12283v1)因此至少有“哪些样本改标签”“hard与soft怎样插值”“teacher约束多强”三个控制对象，不能把它们统称一个蒸馏比例或让模型预测自己取得真值。人工标签、样本选择、teacher/student版本、插值/权重时钟及最终融合须共同保存；cosine直接进入概率损失的归一化和样本slice边界未闭时，不替作者补成可执行recipe。动态目标在某些切片仍弱于固定目标，低相关也不证明两分支拥有独立互补能力。教师制备/前向、双student训练、选参与双读出全付费；伪标签、时钟或真实检索质量失配时，保人工监督、固定teacher目标或已验单分支，不由推理不运行teacher批准零总费、全部相关关系正确与普遍收益。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12283 -->`

本人末注：

- `SF-2025-ARXIV-2510-12283` — Herschel，Daily2025-10-16补Oct15；消费Cicero R8及本日原III-C–F/IV-C–E/TableII–V必要/独核§11，2+1+2=5，仅human hardanchor/softscore样本alpha、插值beta与KD权重w时钟分责差额深入。原HTML323492B partial无结束html，不冒全附件；保KL/InfoNCE归一与slice未闭、Charades R@5 dynamic7.1<fixed7.3及teacher/双student全费，不授所有指标优或独立互补。未第二Methods/代码/复现；整体PRE/SAVE/fullselfread/solePOST只本日canonical实际层。

## 12793 ViCO / 2+2+2=6 / MULTIMODAL-REPRESENTATION Ch23

R20 §3.1–3.2/4.4/4.6首次必要已成。当前gold-mask监督selector/预算条件GRIP未承担**先混合压缩connector训练consumer、再单独学习patch router的两阶段职责**。唯一插位在完整gold-mask第二段/inline SF2604-17087后、完整`Selector 的训练也可以把预算作为输入...`GRIP段前；两个gold-mask段与GRIP完整段已读，不拆两段旧论证。

正文：

选择器之前，也可以先让语言消费者学会读取不同压缩接口：用多种connector随机混合提供压缩视觉表示，让冻结的未压缩reference以输出分布约束训练，再另训patch级router决定当前输入走哪份connector。[受限自适应压缩分支](https://arxiv.org/html/2510.12793v1#S3)将压缩后的可消费性与“选哪种压缩”分成两阶段；未压缩teacher不是事实oracle，按历史分位数产生的router标签也不是真实语义难度。直接把router装到原backbone会明显退步，匹配平均压缩率的随机路由又较差，支持联合验收这两份artifact，而不证明某一个分支独占收益。原图/patch位置、各connector、reference、consumer训练与router校准人口应共同绑定；router之前仍需视觉编码，不能把较短LLM输入称整条视觉链免算。Teacher与全部混合训练、router拟合、视觉前向和选择/生成均付费；LLM first-token吞吐不等完整VLM或尾延迟SLO。预算、校准或真实回答质量失配时，保已验固定connector、更低压缩或未压缩原路径，不由局部吞吐和更少tokens批准证据充分、全能力无损与净降费。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12793 -->`

本人末注：

- `SF-2025-ARXIV-2510-12793` — Herschel，Daily2025-10-16补Oct15；消费Cicero R20 exact-v1 §3.1–3.2/4.4/4.6首次必要，2+2+2=6，仅mixedconnector消费者训练→独立patchrouter差额深入。保frozen未压缩reference/forwardKL、历史percentile非真难度、原backbone直接router反退/随机matchedrate反侧；10patch与64/512text、32threads/2000请求仅LLM first-token层，视觉encoder/router/训练全费，不授E2E或SLO。未第二Methods/代码/复现；整体PRE/SAVE/fullselfread/solePOST只本日canonical实际层。

请sole reader整体审三完整正文/独立marker/本人注，未SAVE/不预POST/日级；三gap互斥，无全章锁/root第三批准。
