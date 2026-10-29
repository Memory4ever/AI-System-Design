# Deliberative Illusion 03032 — necessary Source / actual owner / PRE

作者 supp_20260604_author；R2准入/Jun03日期有效复用。正式2+2+2=6，consensus与证据存活的具体反侧gap深入。作者必要读exact-v1完整TEXT §3–5/6、B2–5/C5/D2/D10，支持及关键反侧足够停止；未核完整figure像素、代码或复现。

## 必要 Source

§3 GPT5从background提取、精炼并标critical atomicfacts，分配agent partialview与Yes/No prior；full/tree/chain三round输出再由GPT5判factIDs/stance。metric systemJaccard初始union与输出union，agent是自身初始set对输出set平均。Jaccard分母含union，agent学到他人facts也可下降，不等所有原事实删除比例；critical labels也不是自然世界全部真值。stanceentropy为binarylabels分布，不是隐态信念/合理价值分歧的完备量。

§4 main：710Ethics/1044News，经争议/主题选择；GPT4.1/gemini3flash/qwen3.5flash同质discussion T1.2，GPT5构造与judgeT0。C5给具体卡gpt4.1-2025-04-14/gpt5-2025-08-07/qwen3.5-flash-02-23；API硬件/precision/完整token预算未披露。三人criticality match.767/agreement.541，evidenceconsistency.900/.789、stance.980/.947，不能把高stance核验代criticaltruth。mainT1 pre输出near1后下降/entropy下降支持共识不等证据保存。D2 selfrevision nointeraction是固定prompt对照，不是理论upperbound；NewsGPT4.1 systemcritical Full.322对nointeraction约.808，局部同设方向，不泛化全部拓扑或开放Agent。

§5 retainedfact更抽象/重建misleading由GPT5评分，关联非唯一因果。§5.2只selected非争议Scruples/fullcontext模型先答对人口，19.2%错误不是任意任务自然率。§5.4 stubborn保stance多样却未可靠保事实、异质减缓非解决，原提示explicitknownfact要求也没保证。§5.5恶意News写normalbaseline46.5%，而T1 GPT4.1Full Newscritical=.322，.465属于Ethics；不采用19.3vs46.5严格同条件因果差。D10人工合成/一恶意/完整原news可识破的选择人口，GPT5judge，非真实攻击频率或防御保证。§6 evidenceledger/caveattracking是futurework、未实测防护，Book只提出独立保留验收要求，不说本文已实现/证明有效。全构造、discussion、fact/stancejudge及独立核验均计费。

## actual owner / PRE

三context/ROADMAP已读，actual Ch82 CoordinationFailure完整段、Verification&Agg开头列表/本judge短段与后漏洞候选完整两段、后改答履历ledger完整段已读，81/83职责复用前一项未变。唯一AGENT-MULTI-AGENT：这里是交互/聚合过程丢失条件证据而非Ch77存储生命周期或Ch66通用benchmark。现有只要求independentevidence/disagreement、改答ledger保答项，不承载atomicfact/stance两输出分验与Jaccard加入事实反侧。拟于Judgeversion完整短段后/漏洞候选生成完整段前仅两段。

完整上锚：

Judge model 自身也要版本化和评估。

拟增两段：

聚合的过程验收还要把立场收敛与证据保留分开：先为参与者实际持有的原始事实和关键限定建立可回查身份，再跨轮比较各输出及其并集是否仍支持这些内容，同时记录立场分布。一项[受限审议对照](https://arxiv.org/html/2606.03032v1)中，共识增强与关键事实覆盖下降可以同时发生；要求保留已知事实、换 persona 或模型异质化都不自动消除这一路径。因此最终意见一致不能替代事实、限定与仍合法的分歧逐项验收。<!-- source-family:SF-2026-ARXIV-2606-03032 -->

测量本身也须保留边界：模型抽取/标注的 critical facts 不是完整真值，事实集合的 Jaccard 降低还可能包含新增他人事实带来的分母变化，不能全部解释为自身事实被删除；立场熵也不揭示内部信念。该反侧支持回查原证据和分别核覆盖、遗漏与无依据新增，不证明共享 ledger 已经防住损失或注入。事实构造、全部讨论、评审和独立回归都计费；关键支持不可追溯、judge 或指标失配时，保留原材料、未决分歧、单 Agent/独立 verifier 与人工裁决，不由更整齐的共识批准事实与安全。<!-- source-family:SF-2026-ARXIV-2606-03032 -->

完整下锚：

验证也可以先把一份风险报告拆成可被反驳的前提与路径，而不只对整份答案投票：保留原程序版本、行号和候选类型，由提议者列出所需条件及通向敏感操作的路径，再让另一角色按每项条件定点读取调用方、类型和不变量，最后单查已有防御是否覆盖有关路线。[一条受限漏洞检查分支](https://arxiv.org/html/2509.11523v1)这样区分候选生成、取证与防御检查；看见敏感操作不证明路径可达，图中有边或多个角色同意也不构成可利用证明。原假设、条件、变量版本与证据必须一并保留：必要前提被反驳，应使相应假设失效，不能删掉前提后重新批准原路径；证据不足则保留未知，而不是把未能反驳改成已验证。防御还须在敏感操作之前约束同一状态，局部检查不自动覆盖所有调用。原对照降低假阳性时也会损检出与部分指标，未闭的标签/统计和上下文人口不能由接口整洁补齐。多视角检查、图谱、逐条件读取、验证与人工回归全付费；证据或预算不足时，保留单Agent有限报告、原静态检查与独立人工/项目测试，不由待查报告批准安全放行。

<!-- source-family:SF-2025-ARXIV-2509-11523 -->

本人trueH2 Review note拟：`SF-2026-ARXIV-2606-03032`：2+2+2=6；exact-v1 §3–5/6/B2–5/C5/D2/D10，factIDs/criticalcoverage与stanceentropy分验；保Jaccard新增分母、critical标注有限一致性、selected人口/三round与API费用，恶意Newsbaseline内不一致不采用严格差额，ledger为未来未测。未核完整figure像素/代码或复现。待实际写后复核。
