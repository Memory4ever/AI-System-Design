# TARo18411：必要原证 / actual owner / 最小 PRE

准备者resume_mar18，仅03-21补BJT03/20；已校完整AB/官方日级夹证复用，无先公开具体信号，不遍venue/旧版本。2+2+2=6拟给step preference→trained gate→双模型decode消费/迁移身份的实际新增接口，不给现有logit steering、fixed interpolation或MoE名称新分。必要差额深入，未独核/锁/写/safe/DAY。

## Necessary exact-v1 / 直接反侧

[HTML](https://arxiv.org/html/2603.18411v1) §3.1–3.3/4.1–4.3/5.1–5.4/Tables1–6；A router/reward配置、B参数、C–E直接feature/成本/粒度反侧实际读，没有核代码/复现或全部生成prompt图像。

- Reward LM先在Math-StepDPO-10K同correct prefix的正负step续写作pairwise preference，以该step token loglikelihood和作为reward；标注粒度是step，不因此识别每个token逻辑真值/因果credit。Llama用DeepSeek-R1-Distill-Llama8B/Qwen用.5B，旧模型预训练能力仍存在，不将收益全归新reward数据。
- 固定base/reward，两份同prefix logits组成router输入，full2V或各TopK值+可训练token-index embedding；两层Tanh/128→sigmoid权重。gold token NLL可选λ Bernoulli-entropy训练gate，不是监督“哪个模型真实正确”，entropy偏硬也不认证可靠专家。两LM不更新不等整个系统无训练：reward LoRA rank8/α16、AdamW2e−5/batch32/3epochs；router每数据1000/3epochs、LR5e−6/batch32/H128、1–4H100 BF16。
- §3.1 pi_base+α pi_reward不归一，Fig2/§3.3混logits，而Final guided decoding写convex probability mixture；softmax((1−α)z_b+αz_r)不等(1−α)softmax(z_b)+αsoftmax(z_r)，因此不抄精确采样配方或把两口径效果等同。只可提案采用明示learned per-token gate的接口/需绑定operator及vocab身份，不绕过中心歧义授具体公式。原“scale/architecture agnostic”仅同family同词表实测，inputshape及tokenIDs/embedding对应必须核，不授不同tokenizer任意搬运。
- Table1 Qwen TARo Math64.8比base60.8好，但OOD9.8<11.8、Alpaca21.6<33.6；且OOD9.8=GenARM9.8，不照“consistently exceeds”叙述。Llama全logit、QwenTopK/λ选择不同，不能以均值认证所有任务保持；UniR旧paper结果不等samebudget实验。temperature.5、length512/2048披露；evaluation judge/完整rubric/重复seedCI未由所读原文闭合，ND。OOD临床这里只当通用迁移反侧，不开展医学应用知识。
- Table4 LlamaTopK1000+entropy math50.6<full54.4但Med14.5>13.2，不从硬gate推独立能力；Table7 fullbase+reward logits math最好但OOD不总最好，Table9 hiddenstate promptgate33.2→token49.6同时Alpaca22.1→18.7。不能把该旧hiddenvariant对照与默认54.4串成唯一因果或所有任务必须token。
- Table6 QwenTopK TPS85.9≈GenARM85.6，但QPS.0448<.0651，与§5.4“QPS更低开销”文字相反；Llamafull TPS32.5<80.7而QPS.0161>.0141，长度/吞吐分母分账，非省总walltime。8H100单node，fullV大router约33M/TopK含V×d表、模型state/两forward/训练/TopK/index/gate全部计费；B精确参数formula疑有隐藏bias差不作budgetrecipe。Table8 TFLOPs是单forward2048token估算，不是生成训练所有费用，临床majority10.6>TARo9.8直接反側，不采用泛4×服务节省。
- Table5“成功推理”示例在年底存款条件错误使用x³+x²+x而非1+x+x²；x1.1时其左式3.641而非3.31。最终gold10正确不能认证展示过程faithful/逻辑有效，更不以αtokenlist认定数学能力因果。上述数值只定点必要反侧，未扩全图像/全部样例。

## Actual sole owner / 最小差额

`MODEL-SAMPLING` Ch20，actual完整289–329 semantic steering/SAE→prefill静态vector controller→同checkpoint双system-logit→local双模型不同tokenizer→soft/discrete router，以及524–532 safety-expert差异sensor；Ch19/21开篇实际读。已有两份logit与逐步risk sensor，但没有**以step preference训练第二LM，再以gold NLL独立训练当前两logits上的逐token混合gate及词表迁移条件**。Ch31学习reward并非本接口消费owner，不另写reward训练。拟Ch20当前307双system-logit成本/退路后、309 Answer-first标题前一段＋本人静态源注，保原固定guidance与硬verifier分责。

## 一段逐字 PRE（待非准备者）

固定双分支的强度还可改成逐 token 学习，而不只在请求开始时选择一个常数。一条受限分支先用共享正确前缀下的正负步骤续写训练 reward LM，再冻结它与 base LM，让小 controller 读取当前两份 logits（或带 token 身份的 Top-k 特征），以 gold-token likelihood 和可选门控 entropy 学习每步的混合权重。这里学习的是解码选择，不是每个 token 的逻辑真值；迁移首先要求词表坐标、模型与已提交前缀身份能对齐，不能由同输出维度推任意模型通用。[TARo 的受限对照](https://arxiv.org/html/2603.18411v1)存在 logit 与 probability 插值口径差异，不能直接照为统一采样配方；部分非训练域任务弱于原 base，硬门控与更高数学分数也不保证全部能力保持。双模型前向、reward/controller 训练、词表特征与状态都付费，token 吞吐与请求吞吐须分账，不由少量 controller 参数或单次算量估计宣称免费推理。混合算子、身份、质量或预算无法验收时，保留固定强度、普通单模型采样与独立 verifier，而不让门控权重替答案签发正确性。<!-- source-family:SF-2026-ARXIV-2603-18411 -->

## 静态源注 PRE

- `SF-2026-ARXIV-2603-18411` — [TARo exact-v1](https://arxiv.org/html/2603.18411v1) §3–5/Tables1–6与必要A–E；只采用step偏好reward与gold-NLL逐token gate的训练/消费接口。logit/probability算子身份未统一、同词表迁移条件、OOD/粒度/entropy反退、TPS/QPS与估算成本、gold对但推导错误示例保留；不授无训练、任意跨模型迁移、全部能力保持或逻辑真值，未核代码/复现。

## 作者窄写 / 等待非writer POST

root非preparer必要Source/actualowner/一literalPRE及static正式有限PASS并授唯一Ch20窄锁后，作者按原稿实际新313一段与705本人静态注。实际顺读293–325完整邻接（新增313已在双system-logit成本段后/Answer-first前）、末七行含PolicySampler邻注与本人注；写后逐字回对原PRE，marker/static各唯一、限定diffcheck空。只采learned gate接口，不采算子歧义recipe或泛收益，不修改已通过Policy静态注；交root一次nonwriter实际正文/完整邻接/本人注POST前不计本项safe/DAY。

## root 非准备者：必要 Source / actual owner / PRE 有限通过

root按03-21独立上下文，实际读exact-v1 §3.2–3.3的step likelihood、两logits/Top-k token index、gold-NLL与entropy、Final guided decoding，以及Table1/§4.1–4.2、§5.4/Table6；实际Ch20完整semantic-steering至Answer-first/局部协作交接（当前293–339）及Ch19/21开篇、本人PRE/静态注。2+2+2=6限定在学习gate与消费身份增量，不给通用插值原则新分。必要Source/actual owner/一逐字PRE及静态注有限PASS。

§3/Fig2与final probability mixture不一致不妨碍只保留无具体算子保证的接口，PRE明确隔离该recipe；不能外推所有能力保持。Table1 Qwen OOD9.8<11.8、Alpaca21.6<33.6且OOD等于GenARM、Table6 QwenQPS .0448<.0651与文字矛盾、Llama TPS32.5<80.7但QPS .0161>.0141均已实际回核，不能用平均数学收益/少量router参数作完整成本保证。正文不引用这些性能数字，无须为此重读不采用的所有附录/案例图。共享词表/前缀身份、controller训练与双前向成本、独立verifier和原采样退路充分限定。未写Books/未POST/未DAY；PolicySampler实际POST已接纳，Ch20该锁释放，可另授TARo一段窄锁。

## root 非 writer actual POST：有限通过

作者按已通过一段PRE实际写Ch20后，root实际顺读293–329完整semantic-steering→双system logits→新增313→Answer-first/跨tokenizer分支，以及本人静态注及前两邻注；原PRE逐字一致，有限Source回核结论未变，新增marker与本人注匹配。学习gate不替代logical truth、operator歧义不照recipe、identity/完整成本与退路近正文，交接自然且未改前文有效机制。actualPOST PASS；释放Ch20窄锁，可归并实际整合，未授整日DAY。
