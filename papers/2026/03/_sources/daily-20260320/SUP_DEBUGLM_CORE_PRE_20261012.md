# 03-20 DebugLM17884 必要原证与最小 SFT 接口准备

准备者 resume_review17_18，2026-10-12。仅本03-20补03/19自然日：重新实际读AGENTS/研究合同适用准入、评分、证据、Books与复用内容，Report时间/独核/完成条款，Prompt、本日窗口/STOP及九尾原packet§5。作者非准备者准入/date已通过；2+2+2=6不变。本文exact-v1/current身份和自然日夹证复用[九尾packet](./SUP_AGENT_TAIL_ADMISSION_PREP_20261011.md)、[九DOI原字段](./SUP_FINITE_TAIL_SCREENING_20261012.md)，不全版本diff/新query/别日。

## 1. 必要 exact-v1 范围与停止

[DebugLM exact-v1 HTML](https://arxiv.org/html/2603.17884v1)，实际读§2.1–2.3/Eq1–6 L99–149；§3.1方法/两stage L172–186、§3.2–3.7关键评价/T1–4 L153–171/191–270；§4仅277–283强claim及§5/Limitations/Ethics284–293；A/T5 342–352、B/T6 353–364；C365–384仅语义扰动构造/标签评价直接反侧；D1–2 387–419数据与baseline输入协议。必要机制、对照与直接反侧够本分采接口即停，未核repo/代码/复现、未读references或另扫附件，不冒图2/3/4像素或全部matrix数值读过。

下面来源事实用于定位，不照录作者“exact provenance/无损/零over-refusal/无成本”结论。我们的反例与权限推断单列，不把推断说成实测。

## 2. 实际机制与中心边界

§2训练同一(x,y)的普通目标与debug目标：[DEBUG]+x预测[y;source-tag]，标签为扩展词表的dataset special token；weighted CE学习条件行为关联。另一remediation目标把采样控制tag放在prompt前：与样本source标签匹配则监督拒答，不匹配则监督原y。**不是**先生成来源tag、运行时读它再决定拒答；两种学得的行为共享参数，但原稿没有独立外部causal solver/ACL。

我们只拟采用该条件监督设计。强桥§4 L277“exact self-reporting”不采：训练标签是数据来源分类监督，标签正确率不证明某条回答的唯一因果来源。最小条件反例（自行推导，不声称实验）：若两个source都有完全相同(x,y)，debug输入历史相同而监督末tag不同，CE最优只拟合标签频率；不能为同一输出签发唯一真实来源。重采样得到两个tag也不会改变这点。需要归因仍使用Ch27外部artifact/operation lineage、受控删换数据和独立任务验收。

§2.3 Eq5–6只定义label-match训练人口；不推出所有部署query准确拒答、所有不相关域无伤害，更不证明unlearning或参数中的知识已删除。prefix控制也不是caller认证：独立trusted执行层须管输入/权限，但本文未提供这层实现，拟文不把<DEBUG>字符串视为不可伪造秘密。训练阶段/data-mixture访问、标签扩展/覆盖重叠及后续stage遗忘仍是条件，Limitations承认百万重叠source不明，Ethics承认tag spoofing。

## 3. 关键对照、直接反侧与费用

五source异质池：四组SFT后WMDP GRPO。TSR是标签exact match，任务正确性另验；跨source overlap/同题不同tag、反事实源删除与模型原预训练来源均未认证。D2明确外部检索/classifier只读已生成response，Debug可读prompt与生成历史；尤其单letter MCQ使外部response几乎无信息，format-robust实验不能单独证明causal tracing优于公平同输入classifier。T1平均95.89/95.68低于外部1B的97.95/98.57，不照录绝对upper-bound。

T2 Llama WMDP68.31低于无tag训练74.86；A/T5两骨干MMLU/ARC均退（Llama58.57→52.11、79.18→73.55；Qwen70.10→68.70、90.78→88.48），不能授无损或仅宏平均utility。自由QA由同Llama70B judge、WMDP exact match分账；拒答matrix文本宣称近对角/非对角零不等所有攻击/开放部署安全，不补未读像素数。

B定义multi-source成功为N=10采样合集至少各出现一次必要tag，不验证每份回答tag与内容的联合precision或对多余tag惩罚；高temperature改变标签覆盖/任务质量。T4任务utility约30/21不随高TSR变可靠。C的576 heldout合成QA保同作者事实，100% dataset-tag不是独立未知source/反事实归因。T6默认行99.60与T4两骨干列口径还需保留其实际各表身份，不能拼成一个数字或单次answer保证。

完整训练recipe（β/三目标配比、更新/词表初始化、GRPO reward与seed重复）、硬件/precision/训练和推理batch/concurrency/输入输出长度/SLO/CI：必要范围未披露完整规格。双目标扩序、控制tag数据/拒答训练、第二stage、judge/合成、模型生成及N10重复、tag审计均计费；“单forward”是AR生成回路而非一次全序列前向测量，不授零额外部署费用。此处不请求全部code；有限监督接口不依赖精确配方，强保证留在不采用边界。

## 4. actual 唯一 owner 与最小 literal PRE（未 PASS、未写）

实际独读Ch29完整67–116（CE→rollout EBFT→ConceptTokens→entropy/多语/softtarget）；Ch27 1194–1210真实record/token-lineage、1250–1263endpoint-relative influence及counterfactual；邻Ch28/30各1–27的pretraining/parameter-update交接。采用owner唯一 `TRAIN-SFT` / [Ch29](../../../../../books/part-04-training-system/29-sft.md)：**原ConceptTokens L98完整段后、下一demonstration entropy分支L100前**。ConceptTokens只更新输入embedding，并不承载全模型debug输出末tag与match/mismatch拒答目标；Ch27承载外部真实lineage/影响估计，不将该learned标签提升或复制到Data/Security。因这条具体差额才拟写，不是主题相似或为了产出；若作者发现实际同接口已具体承载，可明确NC。

两literal PRE：

条件监督还可以把“通常怎样回答”与“在诊断模式报告哪个训练标签”拆成同一模型的两种目标：普通样本继续预测原回答，带debug前缀的样本则预测回答及其数据源标签。来源标签来自训练管线，新增词表token使它成为可学习的输出接口；它不是模型自行恢复的不可篡改lineage，也不能证明该回答只由这个数据源造成。[DebugLM的必要目标与对照](https://arxiv.org/html/2603.17884v1)支持这种条件关联分支，真实artifact/变换记录和受控数据干预仍由[第27章](./27-data.md)分责；标签、词表、训练混合、checkpoint和读出条件须共同标识，不能用更准的标签分类替代回答质量或因果归因。

该分支还可另行监督控制标签与训练样本source匹配时拒答、不匹配时保留原回答；它并不是先读取生成标签再做外部安全判决，也不删除权重中的知识。部署是否接受控制前缀与调用权限须由可信执行层决定，字符串本身不构成认证。原能力与部分任务仍会退步，response-only外部分类对照也不等同模型所见prompt人口；多来源标签还使用多次采样合集，不能继承为单个回答的完整溯源。双模式/拒答训练、生成、采样和独立回归审计都付费；标签重叠、未知来源、后续更新或质量回归时，保留普通verified CE、外部lineage与独立行为检查，不以自报标签签发无损、安全或免费修复。<!-- source-family:SF-2026-ARXIV-2603-17884 -->

静态注 literal：

- `SF-2026-ARXIV-2603-17884` — [DebugLM exact-v1](https://arxiv.org/html/2603.17884v1)必要§2/Eq1–6、§3/T1–4、Limitations/Ethics、A/T5、B/T6、C直接扰动与D对照。仅条件CE的来源标签读出及另训match/mismatch拒答接口；保分类非因果lineage、prefix非认证、对照输入不齐、原能力/任务反退、N10标签合集非单答案归因与全费边界，不授exact provenance/unlearning/无损安全或零成本；未核代码/复现。

交resume_mar17非准备者必要Source/actualowner/原literal与static裁；准备者不自行授Source/PRE、安全处置或DAY，不写Books直至root明确窄锁。普通必要审阅尚可执行，不转外部受阻。

## 5. 非准备者必要源／actualowner／literal一次裁（2026-10-12）

resume_mar17已重载本20适用合同与停点，非本文准备者。实际独读exact-v1 §2.1–2.3 L99–149/Eq1–6、§3 L153–270/T1–4、Limitations/Ethics L287–293、A/B L342–364/T5–6、C365–384必要扰动及D387–419 baseline人口；未核图matrix像素/代码/复现或无关附件。actual Ch29完整67–116、Ch27完整1194–1210/1250–1263与Ch28/30入口1–27实际顺读；两原literal及静态注逐字核对通过。TRAIN-SFT/ConceptTokens后差额真实，标签分类与外部真实lineage/反事实影响分责准确，不是假NC或安全机制换名。

Eq2–4训练debug输出tag，Eq5–6另训输入控制tag匹配标签的拒答，支持原两PRE；准入packet§5旧“生成tag再触发”一句已窄纠而保6分，准备者旧提案的同措辞仅为历史初筛，不用作采用事实。相同(x,y)多源监督的频率反例成立；T5能力退、T1弱于外部分类器、D2 response-only输入不对称及N10集合覆盖均实际核，不能授因果来源/ACL/unlearning/无损/零费用。有限Source/actualowner/两literal＋static PASS，尚未写或POST，须root协调soleCh29窄锁后落实；不是safe/DAY。

## 6. root窄锁后实际 writer 落实（非 POST）

root已明确授resume_review17_18唯一Ch29本family窄锁。本reader实际加载Books三背景合同/ROADMAP的TRAIN-SFT及本日路由，写前顺读CE→EBFT→ConceptTokens完整段→entropy两侧与当前章末源注。仅按§4已由author非准备者通过的原两literal PRE实际写入Ch29 L100/102（ConceptTokens完整98后/entropy104前），追加静态自身注L1486；原两侧正文和全部既有注未改。写后实际完整90–112与末1477–1486本人/邻注回读，来源标签、另训控制tag拒答、真实lineage/权限分责及反退/全费均在原PRE范围，未复制动态验收身份。

本family仅新增两段及静态注共6行，file diff基线28/0→34/0，scoped diff-check无输出；原有和并发改动保留，不stage/commit/push。交resume_mar17一次实际nonwriter完整88–120及1476–1486（本人/邻注）POST；writer不自行授POST、安全处置或DAY，root收到真实结果后释放窄锁。

## 7. 一次非writer actualPOST

resume_mar17实际顺读Ch29完整88–120与1476–1486本人/邻注，两新正文100/102及静态注1486逐字回§4原PRE/static，与已核Eq2–6及T1/T2/T5、D2输入/N10反侧一致。ConceptTokens输入参数权限→debug条件监督→demonstration entropy的衔接完整；不将generated标签变运行时gate，外部lineage/执行权限与原能力退/全费近文，旧HypoTerm/PreSafe/Autocurriculum注未改变。限定diffcheck0，有限actualPOST PASS；root可接纳释放，不再改Book静态身份，本项不授DAY。
