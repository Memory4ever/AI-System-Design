# 02/20 第二十七有限证据包：变长离散标识与合成评估

## 2602.16375v1 — Variable-Length Semantic IDs for Recommender Systems

2+1+2=5，拟AGENT-RAG Ch76标识/解码预算差额深入。exact-v1 V3_REVIEW_2602.16375v1.html §3:155–252、评价314–395、Tables2/5反侧416–453/632–681、REINFORCE684–721/scale725–762实际读。日期桥lower2026-02-19T09:00+08，sameID Registered02:44:41Z+1秒upper10:44:42+08；事件无可见撤回/勘误。不是仅推荐场景指标：固定identifier长度→学习content/stopping分账，改变generative retrieval ID与上下文token成本。

dVAE AR共享词表+soft residual GumbelSoftmax，长度单独stopping hazard不用EOS，truncated geometric prior；expectedlength penalty减length entropy与prefixweightedreconstruction/词表KL联训。实践0.9q长度+0.1均匀prefix、βwarmup/freebits，不等纯未改ELBO或无偏hard discrete gradient。§3:164同token同语义是结构假设，不认证人类可解释，short code非unique item；downstream明确追加unique token解决碰撞。Code/stop/decoder/mapping应共同版本化为工程推断。

Yambda268k/82M、VK900k/95M、Amazon305k/12M；过滤低频、temporaltest last1/4week，reconstruction按interactionunigram而非uniformcatalog。5/10%testuser样本、8layer512recommender与512token历史固定；变长带来更多events，故不是同事件预算纯quality因果。REINFORCE共享架构参数但EOS vs separatedlength/VAEKL不同，不能证明optimizer普遍优劣；stronglengthcost伤recon/冷item更长。Table2 VK fixeddVAE.123/varlen.146均逊Rkmeans.102，Amazon冷item也反退；不授全reconstruction无损。Maxlength5/vocab4096/batch8192/5–10epoch，加大T或V增强质量但增加长度/输出head，hardware/precision/inferbatch/beam/wallSLO未披露。reported更短非部署加速；coverage非所有item公平。

Actual Ch76:126–128已持identifier→document映射、beam剪枝和标识维护，未有同内容编码长度与停止分账/频率weighted vs catalog平均接口。Ch11明确仅texttoken，不占其owner；请求Ch76该段后1窄段+ownnote，写变长discrete ID的content/stop tradeoff与collisionunique token费用、冷尾/不同分母/更多historyconfound，保fixedID/lexicalhybrid回退。不推广真实RAG已验证或自然语言Zipf定律。待rootPRE，未写。

## 2602.16481v1 — Leveraging Large Language Models for Causal Discovery: a Constraint-based, Argumentation-driven Approach

2+1+2=5，拟OnlyReport，待root限定处置。exact-v1 V3_CORE_2602.16481v1.html §4:119–146/§5:149–171/§6:174–198/§7:200–202、costC3.3:1124–1129、consensusdirect1325–1329实际读。日期桥lower09:00/Registered02:47:13Z+1秒upper10:47:14+08；无可见撤回/勘误。采用有限模型评估/semanticprior配置，不重新引入科学应用路线。

Gemini2.5Flash由metadata提议required/forbidden arrow，FlashLiteparse，五次intersection并非独立事实认证。实际先高confidenceCI永久删skeletonedge、discard冲突required，然后其余LLMconstraints是hardfacts，低confidenceCI再relax；不能照intro称一切semantic可被defeasibly推翻或已实现confidencecalibration。RandomDAG→CauseNet inducedsubgraphisomorphism+heuristiccompactness/specificity/semanticdistance，随机CPT合成data。只降低整图直接检索机会，基础CauseNet公开/关系可被记忆；GTgraph辅助LLM写metadata有语义泄漏风险，不是未见真实因果真值或污染证明。54DAG5/10/15nodes、5000samples/50data seeds但每graph同一LLMconstraintset，不能称50独立LLMtrial。observationalMEC+semanticorientation/acyclicsufficiencyfaithfulness，不授干预识别。

Matchingbaseline同CItesting α.05、ABAPC/LLM两者同skeletonreduction，局部SHD/F1/SID改善与noisyprior微伤保留；consensusprecision↑常排空constraintset，非全F1支配。额外APIs/extractor/heuristicgraphsearch/clingo/CI计费，runtime对所有方法均排除外部LLM API（actual1126），不得授完整统一成本。Actual Ch66:3100–3106已经维护原pool/组合身份、源污染风险与无controlledexposure不能读污染效应；本作特定CauseNet组图/metadata管线尚未证明新的普遍anti-memorization条件，保局部stressprotocol仅报告，不强写通用措辞。重开具体新机制/受控metadata leak或memorization证据才作增量判断，不请求所有附件。

## 停点

两项必要证据/actual owner准备，请rootPRE/Only限定处置；16356独立准备实际kinematic state差额，不因一般scenegraph名映射自动入书。仍未日级冻结。

## 独立处置追加（2026-10-05）

16375 Ch76 body128/122–136完整邻接/own1535 root实际POST通过；16481有限Only处置root实际独核通过，runtime已精确为所有方法排除外部LLM API。两项终态，锁释放；README93=56POST+14争议+5已有+18Only，最后3待实际写后与终稿非作者验收。
