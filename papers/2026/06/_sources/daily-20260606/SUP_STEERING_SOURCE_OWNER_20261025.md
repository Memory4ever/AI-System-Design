# 05958首次必要／评分／actual owner与最小单段PRE

作者jun06_continue，2026-10-25，仅Daily2026-06-06补Jun05。R19 exact-v1完整AB/date/准入有效层复用；原件身份与采用范围未变，不第三题摘或日证，不加载别日池。按当前AGENTS/研究及Report合同，只审已准入具名材料，不扩87导航。

首次拟2+2+2=6：设计2给对比文本→向量重算仍可保持来源一致却改变安全行为的具体反例，reach2给辅助数据/干预artifact与运行时应用的信任交接，durability2给provenance与行为资格分责；不把成熟供应链或一般steering原则重复计分。

## 必要原件与采用限界

已实际读[exact-v1](https://arxiv.org/html/2606.05958v1)§3–5/Limitations与A的应用层表、B协议对照、D文字caption、E/F/G直接反侧；未核图像素、代码或复现。白盒open-weight模型为攻击者可见，发布bundle含contrastive pair texts/vector/weight及可本地重算的equivalence说明；用户验证向量来自所给文本，只能证明派生一致，不证明文本/干预的安全。论文称cryptographic certificate，本次未核证书实现/密码学协议，不改成已验证签名系统。模型权重本身不变，文本表面良性与属性span保留仍不排除派生向量在另一人口改变拒绝。只为责任边界读攻击方法，不保存payload、优化操作recipe或可执行代码。

评价仅Gemma2-2B-IT与Llama3.1-8B-Instruct、BF16、选定层/四属性共八组合；每组合20对contrastive文本，三优化seed，评估100 harmful和100 harmless prompts与方向估计人口分离。作者控制bundled weight，clean/poisoned同强度比较不是独立held-out强度选择；ASR为三LLMjudge多数票，loop/offtopic按safe且缺票tie也safe，高interjudge一致不变行为真值。属性AC用regex/language-ID，非generalutility或安全。主协议只prefill施加，B仅两组合较低weight测allsteps；原同weight下allsteps会loop，故model/tokenizer/layer/strength/application protocol须共同绑定，不能迁移headline。

关键支持及反侧：主文局部ASR升而大部分benign属性保持，证明良性sanity不足，不采普遍不可见攻击。Gemma lowercase clean AC=.14已会被认真sanity拒绝，不计该combo的stealth主张；norm比一个1.78×异常，不采全八norm不变。§4.5有实体/词性改变，embedding近不等语义保真或人类不可察觉。§4.6 safety-auditor对960 poisoned texts仅17flags，controls128harmful全flag/128harmless与320clean零flag；这只是受测rubric未识别大部分样本，不证明所有审核无效或任意删掉flag仍保攻击效果。

§4.7去已知拒绝相关方向能减少本攻击lift，但仍有残余，benign AC最大变化.09；不能由平均82%恢复宣全防护。E仅一Llama lowercase cell/三seed/有限cap sweep；主文定义r为anti-refusal、E却写-r为阈值方向，符号不齐，不照录唯一threshold执行recipe/适应攻击普遍保证。B应用协议、D norm反侧、F judge定义足以限制采用，不采图中未读数。Limitations只白盒/≤8B/一个拒答目标，crossmodel迁移与其他恶意目标未测。AppendixK理论未用于本采用命题，不为附件完整性扩读或继承局部最优/安全结论。

G称A10064GB每cell/seed一GPU，attack约4 GPUhours、evaluation约8却总称15，费用加总不闭；另约100K judge API不计GPUhour。只记原口径冲突和独立API费用，不录统一总预算或“廉价安全”。前向/hidden读取与重算、数据审校、选层/强度/协议、行为评价/judges和防御重新验收均计费；线上batch/concurrency/SLO未披露，不补生产能力。

## actual owner与已有覆盖差额

实际读唯一`PLATFORM-SECURITY` Ch72“模型文件与训练代码是不可信输入”全段及列表、其后固定checkpoint被编辑为steering的两完整段、直接PromptInjection开头；亦读steering规范解释/行为权限两段，Ch71/73开篇交接。现有正文已清楚说数据格式/加载成功不证明行为安全，artifact身份与正常/触发回归分开，不能再当新增一般原则。可是既有案例需checkpoint写权限，本次是不改weights而由共享辅助contrastive数据派生runtime干预，验证派生一致与只做良性属性检查也不足。此auxiliary bundle/application身份链是最小具体gap，而非只同主题换论文名。定点精确ID/题名未见本family真实正文；未读其他日报反推覆盖。

拟最小单段补这条独立输入面，不重复旧两段的release程序。若reader确认actual正文已承载等价派生链则具体NC优先，不能由generic安全宣言或trace硬NC。

## 原单段PRE（未SAVE）

拟位Ch72 2604.12359第二完整段及inline marker之后、H2 Prompt Injection 与 Tool Boundary之前。仅此单段/末唯一marker+trueH2本人注，须首次必要/正式6/actualgap/PRE后root本轮fresh窄授，不提前写。

不改checkpoint也能引入同类风险：从上游对比文本派生、加载到runtime的steering向量，是另一份须单独验收的输入。[受限共享向量对照](https://arxiv.org/html/2606.05958v1#S3)中，本地重算可确认向量确由所给文本产生，良性查询也仍表现出声明属性，却不能排除另一输入人口上的拒答抑制；派生一致性不是行为安全证书。应把文本/向量、model/tokenizer、layer、强度和prefill或逐步应用协议共同绑定，分别验声明效用与风险行为；改为逐步应用还可能使原强度退化成循环。已知方向的投影只能算受测缓解，不能由有限残余下降批准未知方向或新模型。重算、审校、参数/协议校准与独立行为回归都有费用；身份、方向或安全切片不合格时，关闭未信steering，保可信基座与原release gate，不凭来源可复算或benign sanity放行。<!-- source-family:SF-2026-ARXIV-2606-05958 -->

本人注拟：`SF-2026-ARXIV-2606-05958` — jun06_continue，Daily2026-06-06补Jun05；R19AB/date/准入复用，2+2+2=6/唯一PLATFORM-SECURITY Ch72。exact-v1 §3–5/Limitations及A应用表/B/Dcaption/E/F/G必要，只辅助steering派生一致与行为资格/应用身份分责。保弱stealth combo、norm异常/语义不保真、prefill/allsteps差、有限judge/残余与E方向符号及G费用口径差；未核图像素、代码/证书实现或复现，不采普遍隐蔽/适应防御或生产SLO。必要/PRE/rootfresh/真SAVE/唯一POST按后到事实记，不预I/DAY。

## 既成采用（2026-10-25，仅行政同步）

R27必要/正式6/actualCh72原单PRE通过，root本轮fresh新窄授后A33逐字真存/完整自读，[R28唯一actualPOST](SUP_REVIEW_20261025.md#r28--05958唯一actual-post)实际通过，I11生效/窄位释放；前文未SAVE/拟态只保历史过程，不再表示普通未完。不第三必要/正文，不授DAY。
