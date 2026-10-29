# JRS17372：同类有害输入的行为方向与图像增量修正

resume_review17_18，2026-10-12，仅03-20补03/19。root明确sole准备；原本日Batch6/独核§17准入、2+2+2=6及03/19自然日夹证有效复用。实际恢复重读AGENTS/Research与Report合同、每日/arXiv Sources/Prompt、ROADMAP、Books约束与本日README/STOP；无新发现或换日，不自行Source/PRE PASS/safe/DAY，不写Report/LS/Books。

## 1. 身份与必要原证停止

当前[official abs](https://arxiv.org/abs/2603.17372)完整题摘/history实际读：仅v1，Submitted03/18，无具名撤回/纠错。题摘潜力不是结论；日期复用本日Batch6已核DOI ID、registered03/19T02:30:38Z与官方公告/ID公开夹证，不以Submitted或检索推荐为首日，不追精确时刻。

实际[exact-v1](https://arxiv.org/html/2603.17372v1)必要§3–5/Eq1–3/T1–5 L85–249、Limitations L253–254，A1–5 L291–344数据/分析人口、B L346–360匹配baseline设置、C1/T6/C2 L361–428标签/警告词、D3/T8–9 L441–485直接utility/残余反侧。图只读题注和正文，不冒像素数值；未遍D1/2全部图、全部case/references、代码或旧版diff。支持与直接反侧够证即停。

## 2. 必要机制与强桥隔离

先区分两个分类对象：harmful/benign是输入语义标签，jailbreak/refusal是模型完整输出由judges分的行为标签。本文在明确有害文本仍在的样本上取末token各层hidden，观察PCA/距离/线性probe的类别分离；警告词只是输出包含风险语言。可读出有害标签、不同簇或生成警告，不证明模型在生成时因果使用正确风险概念，不足排除所有perception失败或识别唯一内部state。显式文本人口与隐式图像人口不能合并成“所有jailbreak非感知失败”的定律。

对每个模型/层，以50jailbreak与50refusal HADES样本的centroid差归一化定义d（从refusal指向jailbreak），而不是benign→harmful方向。对相同文本，比较image+text与去image的text-only末位置，得到Δh；s=Δh·d，归一化s/||Δh||仅是方向投影。本文在首个生成token时，对超过正阈值的层从multimodal hidden减去s d，保留其余图像增量。这是对增量沿某经验方向的局部修正，不是删除所有visual tokens、全部图像影响、harmful知识或一条已证唯一因果机制；subtraction不能逆转此前所有网络非线性影响。逐层参考、首token/hook、model/d/threshold、text-only/image分支及position identity须绑定，这是工程采用要求，不冒论文已核完整执行guard。

||Δh||为0的归一化、移除图像导致末token身份变化、多层修正后下一层参考重算、方向estimators近零差等guard未在必要说明给全，不补成精确recipe。threshold0.2是有限安全/utility经验选择，低阈值仍损utility，不是校准概率或通用最优。预先已有较强LLM backbone alignment是Limitations明示条件；text-only自身弱安全时不能凭该参考自签防御。

Gaussiannoise/CLIP相关度分层同时改变图像可读内容和输入统计，direction本身由模型行为标签拟合；相关shift/ASR不构成严格mediation或唯一原因。随机配对/等幅正交干预、held-out方向人口、独立行为标签与自适应白盒攻击仍须独立验。保有限防御分支，不因中心解释未证转EX或降分。

## 3. 标签、反侧和全费用

A1HADES750文本×3类型2250、MM-Safety1680×35040、RedTeam2000×36000；分析harmful前两全集7290，benign来自LLaVA-Instruct150k随机3000（与正文4.2Instruct80k引用不直接统一）。方向使用50+50 HADES，C1抽方向时只保三个判据全一致/drop-conflict，测试多数票保全部；方向易分类人口与实际部署不确定人口分开。没有明确披露方向50+50与同HADES测试样本是否剔除、probe train/test split及人工groundtruth，不能称独立zero-shot所有holdout。跨dataset测试支持有限迁移，不能消除同judge/风格共偏。

ASR用refusal字符串规则+Qwen3GuardGen8B+LlamaGuard4-12B多数票，无refusal字符串即ruleharmful并非真正有害；两个LLMjudge也可能误判复杂/不完整输出。C2警告词不含refusal，但“please note”等形式不是独立正确意图认知。T2的65.1等是percentagepoint差，不是相对65.1%或普遍zeroASR；例如LLaVA RedTeamSD+TYPO仍21.9，隐式HADES仍35.3、MM-Safety19.1，T4残余>0。缺guard-awareadaptive攻击和真实tool effects实验，不授安全保证。

T5 LLaVA MM-Vet32.1→31.6反退；D3 InternVL39.5→38.3反退，ScienceQA/MME某些表值持平只属所测人口。ScienceQA混text-only2224与multimodal2017，整体持平不能认证全部视觉能力无损；MM-VetGPT4评分与harmjudge不同，MMEYes/No配对也不是开放真实任务。没有全良性误拒/拒绝边界、敏感但合法任务或生成内容groundtruth协议；不照录“withoutdegradingutility”。

B AdaShield用static版本，ECSO删初始selfcheck后由LLaVA caption256，ShiftDC也用LLaVAcaption，CMRM采用blankimage样本版；这些改变与额外模型费用影响公平性，不能由表格证明所有实现均被严格dominance。本文称仅两个additionaltokenlevelforward且长回答>128token可摊销，但缺基于image/textprefix的实际执行/TTFT/端到端budgettrace；去image参考与受限hooks均有成本，不能由token数直接授实时“negligible”。hardware/precision、batch/concurrency、输入长度、decoder配置、seeds/CI、方向构造/label/judge全费、tail/SLO Not Disclosed。未核代码/复现。

一次强桥请求：方向/测试精确split与独立人工标签、完整层与末位置/分支guard、等幅对照/自适应防御感知攻击、合法敏感任务误拒及匹配完整TTFT/utility预算；缺这些不支持唯一成因、完整安全或免费部署。有限下述分采不依赖这些强断言。

## 4. actual sole owner 与 literal PRE（待非准备者裁）

实际读Ch72开头、完整606–682 capability/跨模型direction→GRAM→router→policy交接、本人末注邻接；Ch16 246–275现probe-space与生成gate介入分责、Ch71/73开头相关交接。sole拟 `PLATFORM-SECURITY` Ch72原619跨模型direction限制完整段后、GRAM621前两段。现有正文承载跨模型concept映射、representation相关非authority，却没有同有害人口的jailbreak/refusal方向、image-vs-text增量及首token局部修正；不是复制Ch16一般activation编辑，训练路由GRAM与inference修正不同。

同一模型的安全方向也须先说明由哪两类行为定义：有害与无害输入的差，不等于同为有害输入时越狱输出与拒答输出的差。一条受限推理分支用后一对模型行为标签构造逐层方向，再比较同一文本在有图与去图时的末位置表示，只对图像增量沿该方向的正投影超过阈值者作首个生成token的局部减除。它保留其他图像增量，不是删除全部视觉证据；方向、标签筛选、层/末位置、参考分支与阈值共同定义干预身份。表示簇和警告语只能提供诊断线索，不能由此认证唯一越狱原因或已正确识别真实有害意图。<!-- source-family:SF-2026-ARXIV-2603-17372 -->

[行为方向与增量修正的有限对照](https://arxiv.org/html/2603.17372v1)仍有攻击残余和良性效用反退；抽方向时丢弃judge冲突、测试时采用多数票，两个人口及已有语言骨干安全条件必须分开。构造标签与方向、去图参考、额外前向/hooks及独立回归都付费，长回答摊销不能批准首token延迟或生产实时SLO。方向失配、骨干弱对齐、合法视觉任务误拒或费用回归时，保留原forward、显式输入/输出policy与独立审核，而不是扩大未经校准的修正；完整输出和工具effect仍由独立安全/授权边界验收，不让内部方向取得执行许可。<!-- source-family:SF-2026-ARXIV-2603-17372 -->

静态注：

- `SF-2026-ARXIV-2603-17372` — [JRS exact-v1](https://arxiv.org/html/2603.17372v1)必要§3–5/Eq1–3/T1–5/Limitations、A1–5/B/C1–2及D3/T8–9。仅同有害人口的模型行为方向、图像增量投影与首token局部修正；保probe/警告非唯一因果、方向标签筛选/测试分母、弱骨干与zero/positionguard、非零ASR/utility反退和额外前向全费，不授完整recipe、通用安全、无损或实时保证；未核代码/复现。

准备后交resume_mar17一次非preparer必要Source/actualowner/原literal与static；未授Books锁，不自行通过或计safe/DAY。

## 5. 非准备者必要 Source/actualowner/PRE

resume_mar17实际独读exact-v1 §3–5/Eq1–3/T1–5 85–249及Limitations253–254、A1–5 291–344/B346–360、C1–2 361–428与D3 441–485；actualCh72完整606–682、Ch16 246–275及71/73入口，逐字回原两literal PRE/static有限PASS，6分/date不变。同为有害文本的人口下模型jail/ref方向、image-vs-text增量与首token层局部修正，确有inference分责差额，不是旧跨模型concept迁移或GRAM训练更新。

原Eq3明确归一投影超阈值才减非归一s*d，不把相似度直接当幅值；保留其余增量是局部代数不认证后续视觉能力。首token、text-only末位置与zero/multilayerguard未认证，PRE只接口不授精确recipe。drop-conflict构造方向与majority全测试人口不同，50+50方向heldout及独立truth标签未披露；warnings/PCA/probe不识别唯一原因。非零ASR、LLaVA32.1→31.6/InternVL39.5→38.3效用退、ScienceQA混模态分母、baseline改配/额外前向成本、weakbackbone条件实际准确。未读D1/2全部图、代码或旧史，足证即停。请root授reader soleCh72旧跨模型限制完整后/GRAM前两PRE+static，由作者一次nonwriterPOST；未实际写后通过不计safe/DAY。

## 6. root 窄锁后实际 writer（待作者一次 POST）

root接纳author非preparer§5并明确授reader soleCh72本family旧跨模型限制完整段后/GRAM前两literal+本人static。reader实际现有608–629及末注读后，逐字写新618/620与static4469；完整608–652跨模型方向限制→本模型行为方向与图像增量→GRAM/训练隔离及末4461–4469本人/邻注实际读回。本family scoped diff只两正文+静态注，diffcheck无输出；旧有效段未覆盖，原PRE/static不变，不循环身份注。交resume_mar17一次nonwriteractualPOST，不自授POST/safe/DAY。

## 7. 非writer实际POST

resume_mar17实际完整读Ch72 608–652与4461–4469本人/邻注，逐字回有效Source/两literal/static。新618/620承接跨模型direction限制，再区分本模型同有害人口的行为方向与image增量修正，后接GRAM训练隔离；原有段落与marker保留。首token局部修正不授唯一越狱成因，方向筛选/测试分母、弱骨干、ASR残余/utility反退与全部费用近文准确，static4469无过程身份。限定diffcheck0；一次nonwriter有限actualPOST PASS，交root接纳释放Ch72，不授DAY或重复Source。
