# Jun03 第四批：CFG并行验证、hybrid转换与范式比较 / 待独核

作者`supp_jun03_close`。仅Jun02 BJT；原完整v1题摘/R26/R28联合日证复用。精确registered：00722 `2026-06-02T03:58:12Z`、01774 `04:23:37Z`、02544 `04:41:53Z`、02241 `04:34:41.000Z`，不作实际公开时刻。当前官方abs：00722Oct04v2、01774Aug04v2、02544Aug08v2、02241唯一v1，均未见withdrawn/removed/erratum；只用精确v1，不由版本号遍历旧新全文。实际owner比较前上下文沿本日有效层；无Books写入/预I/POST/DAY。

## 00722 EPIC — 2+2+2=6，Ch24 CFG组一段提案

[v1](https://arxiv.org/html/2606.00722v1) / [原件](SUP_CLOSE_2606.00722v1_20261025.html)。实际读§3–5/T2–4、D1–3、E4环境、F2/T6–7。CFG terminal是lexeme而模型token是第三种alphabet；partialtoken经lexer映为completion-language ENFA，真正门是CFG∩completion非空。Memo key保localprefix/suffix配置、同lexicalmap复用不改变语言；Earley式parser直接在ENFA witness检验，省掉每次determinize/minimize，非所有CFG最坏复杂度改善。Regularcover是CFG超集，便宜预筛可拒绝cover都不相容的subset，**通过cover不提交**，必须exactCFG再验；失败分裂再序列fallback，不是以approximatechecker换语法保证。

D3 RTN flatten忘掉callreturn匹配只增路径，作为superset有效，但soundness相对声明lexer/CFG/长度支持，不认证代码语义。Rejectedbudget耗尽用witness完成，不采原模型分布；约束下快于unconstrained部分因为提前EOS而unconstrained跑满schedule，不是负的checker成本。四7/8B模型、C++/JSON与SMILES仅形式语言人口（不采用化学AI机制）、maxgen256、16–256steps/greedy、计时seeds42–44；RTXA6000/Threadripper3960X，软件版本仅作者配置未独立核验。F2恢复前后合法率与functional分开，有99.4/99.8非全100，syntax高而functional低不可互签；JSON DFAfree单组件可慢、SMILES小grammar收益弱、一些256step配置慢于baseline。总时间/3次runtime不等统计quality多seed或并发SLO，precision/批并发未齐不补。全grammar/lexer编译、memo、regularcover、exactverify/fallback和功能测试计费，未核代码/复现。

actual完整读Ch24“Diffusion Constrained Decoding必须验证仍可完成”起始三段、DConstrain局部程序/路径目标段、Diffinity软约束与DiffuRank匹配完整组；Ch51grammar输入状态/语义可完成性组已读。现有可完成性gate与局部程序复用不说明**superset预筛并行候选batch仍由exactchecker批准、直接图parser的责任**。唯一`MULTIMODAL-GENERATIVE-PARADIGMS`。拟在原00612独立marker后/现“仍存在合法补全只回答feasibility”段前加一段：

> 可完成性检查自身还可能吞掉并行生成的收益：一次提出多个token后，逐项串行验证会重新引入提交瓶颈。可先复用未变局部lexing结果，直接在completion图上做CFG witness检查，再用CFG的regular超集便宜筛出候选batch；[EPIC的受限分工](https://arxiv.org/html/2606.00722v1#S4)中，超集通过只提出并行集合，仍须exactCFG检查，失败就缩小集合或回序列验证。它保留声明语言的可完成性门，不保持原采样分布，也不证明程序功能；预算耗尽的witness补全更是语法fallback而非模型采样。Memo、cover、parser和额外失败检查均付费，简单grammar可无益甚至更慢，提前EOS收益须与纯检查成本分账；语言接口、支持或净费用失配时保留原exact顺序checker、完整功能验证或AR约束生成，不由近满syntax分批准语义与SLO。<!-- source-family:SF-2026-ARXIV-2606-00722 -->

## 01774 FLARE — 2+2+2=6，Ch24兼容转换一段提案

[v1](https://arxiv.org/html/2606.01774v1) / [原件](SUP_CLOSE_2606.01774v1_20261025.html)。实际读§3/式4–8、§4、§5.1/T1–2、§5.2–3/图注与§6限制、D1配置；未核全部A kernel推导/代码或复现，故不授完整kernel正确性。Cleanstream保持AR，两个互补randommask覆盖每个response token各一份diffusion监督，与一份AR单位加权；clean不读noise、noise只读precedingclean及本块bidirectional，packed文档另隔离。Hybrid recurrent不是贴mask即可：noiseblock从相应cleanboundary state起步，本块末state供其各位置读且不流向别块；不同于普通causal线性attention无条件复用。

同checkpoint两种commit：DiffusionTrust暂时denoise不写live recurrentstate、finalblock需causalreplay；ARTrust只commit接受prefix，不只是裁KV还要rewind recurrentstate。式8 residual只对持有与真正采样draft相同q有效；低费approxq/argmax路径不借reference exactness。本文不把训练前seed分布与转换后cleanstream相同。

§4同Qwen3-1.7B/9000step约10Btoken、4096/batch256/12task，比四数据mix及固定Mix1累计消融；dataeffect只在这组objective与mix内，未证明任何目标/data普遍支配。新mix同时改trace长/域/IF，empirical weights和ARproxy筛选有选择费用。§5 Qwen3.5-2/4/9B仍有IF/knowledge退步，DiffTrust在code明显更弱，“*underreported”不能删除真实失败；不同公开model训练/质量/activeparams预算不等不采绝对先进排行。D1作者列32A100或32H100、AdamW1e-5/warm500、12–36h；评价max32768/T1/p.95/k50。Fig9固定2048、ignoreEOS、单A10080G/bf16/C8测TPS不是自然终止用户SLO；更高MFU是吞吐利用率，不取消额外work：A.5明确双流加complementary masks约4× **per-input-token attention work**，不是2×总work。首稿2×写法已按R182及本人实际回读A.5定点纠正，正文原literal仅写额外work不受影响；RouteII大B也可不如RouteI。构造/筛数据、clean/noise、边界state/重放/verify/graphmode和独立质量全费。

actual完整读Ch24 ARweights→masked兼容桥/同corruptionteacher、MARS/PA-BDM、同model双可见性2509.04185两完整组及邻strictstream/turn-boundary；现有保AR与masked双目标/causalizeKV不能泛NC或再复制。真实未承载是**softmax可见性到recurrentstate读写/重置的lowering，以及两个生成mode不能共享同一live-state commit**；token-balanced互补监督作为这条兼容桥的输入，不另起同义“保AR”知识。唯一Ch24，Ch22架构/Ch49kernel/Ch48spec仅职责引用，不扩多个owner。拟在2509.04185独立marker后/“因果可见性、监督位置与提交粒度其实是三个独立选择”前补一段：

> 把同一clean/noisy接口迁到hybrid recurrent backbone时，可见性还须落实为state读写日程，而不只是softmax mask：noiseblock从其前方cleanboundary state起步，只在本块吸收noise，不能污染别的block或packed文档。[受限FLARE转换](https://arxiv.org/html/2606.01774v1#S3.SS2)用互补mask给每个response token一份denoise监督并保AR路径；部署时diffusion暂态不写live state，整块完成后causal重放，AR验证模式则只提交已接受prefix的recurrentstate。共享checkpoint不允许共享错误的commit状态，也不保证原seed能力或分布未变；持有draft概率的严格验证条件不能转授给便宜近似路径。数据mix、两流训练、state重建/rewind、kernel与模式化graph均付费，固定输出TPS/MFU不抵消额外work，部分code与指令任务仍退；状态、能力或净预算不合时保原AR、较小块及可重放的独立mode，不由一张visibility图批准兼容与生产收益。<!-- source-family:SF-2026-ARXIV-2606-01774 -->

## 02544 SimSD — 2+2+2=6，实际同family具体NC

[v1](https://arxiv.org/html/2606.02544v1) / [原件](SUP_CLOSE_2606.02544v1_20261025.html)。实际读§3–4/式1–5/T1–4与distribution分析。Paireddata/mask位置共享temporal label与RoPE坐标，draft提出token及顺序，target一次forward读更早draft、不直接看自己/未来data；但深层间接影响使之只是sequentialdenoise近似，§4.3明确非losslessreplay。式2ratio后拒绝说直接sampletarget，未明确经典[p−q]+residual，§3.2“preserve inducedtarget”的全保证不由此成立；不替作者补残差recipe。高top1agreement/.94或.975不证明joint分布，crossmodelKL还混合drafttarget差。

SDAR1.7Bdraft/8Btarget、B4/8、max512、T1/p1、batch1/FP32/KV，2RTXPRO6000Blackwell分GPU；VanillaTP2与CGon/off、modelparallel之间架构不同。7.46×对无CGVanilla，matchedCG均值71.6/51.8约1.38，decodeTPS排prefill/200例不等全请求；GSM/MBPP质量微退不能以四任务mean升洗去，gamma也非越大越快。双模型/复制layout、state/verify、KV/graphs和质量回归全付费，无生产SLO/复现。

actual完整读Ch48“Diffusion Draft需要重新建立可验证前缀”及02544同family**Temporal-causal Verification Layout两完整段**、直接前feature-draft组与后完整blockcopies/orderproposal组；邻Ch47/49开篇核执行职责。正文已具体承载data/prediction分离、temporalorder/RoPE、mask/position/block身份、额外KV/layout和不能证明原分布时回原blockdenoise，直接覆盖本项可采用机制和限界；不因同familymarker冒已审eventduplicate，也不为新增速度名或更细公式再写Book。拟6分深入完成/具体已有覆盖。

## 02241 BlockGen — 3+1+2=6，Ch24训练block可行集与额外AR评分提案

[v1](https://arxiv.org/html/2606.02241v1) / [原件](SUP_CLOSE_2606.02241v1_20261025.html)。实际读§3/式10–12/§4/T1、B1–5设置。同denoiser条件于blocksize，密度是各blockfactorization的**mixture**，训练随机/stratified选block优化较松meanELBO，评价logsumexp需全M组ELBO；lowerbound不是exactlikelihood，固定block采样也不是免费采整个mixturedensity。Causalcleanprefix可共享KV，timestepembedding置零而非声称所有noiselevel有精确等价。

ARPC从diffusionproposal另作同checkpointL'=1前向，以proposal token的ARloglikelihood选低分位置再noise；无需独立verifier不等不付额外forward，也不拥有correctness或exacttarget分布。170M/12layer/768/12heads，TinyGSM250ksteps→GSM8K执行代码再exactmatch；OWT1M/context1024/GPT2，LM1B用BERTtokenizer不跨数据合PPL；Adam3e-4/batch512/mixedprecision，3e-4/EMA/dropout与extraMkernel编译均为配置。所读设置未明确GPU/全wallclock不补。T/GE/warmup与gamma扫选bestfrontier，不是equalallsearchbudget纯sampler因果，EIPCsingleblock与ARPCmixedtraining也不同；ARgreedy仍最好、matchedtotalNFE整段diffusionGenPPL可胜blockARPC。

具体新证据是uniform ancestral更好、ARPC且高NFE时masked反超，与更少步uniform占优共存；它修正按corruption名称决定胜负的设计判断，故D3限这条条件排名反证，不借所有mixture数学加分。17.5与AR16.7相差+0.8，正文“below”算术方向不采用。GenPPL/entropy不是correctness，ARPC多一pass/NFE、temperature/schedule搜索与全部训练回归计费，不授权fullSLO或普遍masked优。

actual完整读Ch24 blockdiffusion起始size/pareto组、objective与commit分责/2602.15014范式frontier完整组及现MARS双目标组。已有“比较sampler须控条件”原则，不等已承载**同一模型在多blocksize受训后调用ARmode指导correction，从而改变masked/uniform排名**这一具体机制与反例。唯一Ch24。拟在起始“固定blocksize只是策略之一…”完整段后/现overlap后块段之前补一段：

> 可选block宽度还可以进入同一模型的训练支持：按blocksize混合优化各自条件目标，让size1的AR模式与较大块的diffusion模式共享参数；训练时随机选一宽度的平均ELBO，与评价全部宽度的log-sum-exp bound不是同一计算口径。[BlockGen的受限corrector](https://arxiv.org/html/2606.02241v1#S3)另付一次AR前向给当前proposal逐token评分，再重噪低分位置，而不是增加独立真值verifier。在这套训练/采样条件下，uniform的ancestral优势会在高NFE的AR-informed correction下缩小甚至反转，不能由corruption类型或较低bound预先选胜者。共享模型不免额外求值、混合训练与schedule搜索，局部数学/GenPPL趋势也不认证事实或全流量优势；质量、预算或KV支持不合时保留固定宽度、原sampler与AR，并分别验bound、真实输出和端到端费用。<!-- source-family:SF-2026-ARXIV-2606-02241 -->

## 交付

本批四ready交root。00722/01774/02241只请求以上Ch24具体自然段位置，02544无Book改动请求；未授独核/正式计数/I/DAY。原MODEL18现仅读完15的必要层（本包含4），余三普通：01839ConServe、01065Leyline、00866MORI；另02358/00289/02502/02576及有限发现收束继续。此前三批未变不第三。
