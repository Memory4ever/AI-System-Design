# 本日余下四项已校准潜力：逐篇必要审阅

2026-10-08最新终判：08017标准/actual Ch23具体Existing、08010实际Ch20新段/完整邻接/selfnote POST、08726中心expected-wealth争议信号、07963首次公开/本次增量未建立的日期隔离均已review_jan15_delta非作者通过。本文下面是原prepared/历史停点，不再有这四项普通待办，具体正式六部分以本日README为准；不扩大日期或附件。

作者supp_jan15；仅具名08017/08010/08726/07963，不扩216库存。last4-core0/1/2保必要原件，以下逐篇ready，不授其它未读项。日期08017/08010/08726复用dates47正常announcement下界/正式ID存在上界，原件链轻核无early完整稿/纠错提示；07963另待日期。Books写锁均已释放，等待非作者source/actual owner裁决。

## 08017 Representations of Text and Images Align From Layer One — 2+1+2=5，标准必要完成；具体Existing提案

Late logitlens失配不等无早层信息→text概念方向反向优化可转移prototype→可恢复、自然输入分布对齐与native调用分开。实际exact-v1 §2.1–2.3/§3.1–3.2/§5、AppE/F/G：100词均值center text、grey image center patches；概念相似度×centerGaussian加权聚合，multiresolution DAS/shiftnoise优化448²图。该inverse合成是局部存在性证据，非自然text/image总体同分布，也不授原模型已使用该路径；优化失败不证明信息不存在。Gemma3 4B/7layers/>100concepts，InternVL3 8B仅animals；600steps/SGD momentum.9/batch8，lr与tau分层调；hardware/precision/concurrency/SLO/seed/fullfees Not Disclosed。

GPT5分类hint与无hint两个协议/每图10responses，GPT5mini binary rubric；无hint只有animals可靠，部分objects/cities靠图中文字，未量化text-in-image比例，不把recognition当全人类可解释。Mean pooling中层仍collapse，但InternVL无同collapse，loss/model影响不能授真实信息消失。95%CI和response重复不是全部优化seed；训练及评估API/gradient/backprop成本不免，作者no auxiliary仅无需辅助训练而evaluation仍外部judge。Current exactabs只有v1/无撤回标记、没有early完整paper链接，normal date方法限定不宣称全网无早稿。原件last4-core0/1/2＋alignrequired3（§3/5/AppE/F/G已实际读）；其它四项不随此授完成。

actual MULTIMODAL-REPRESENTATION Ch23:87–90已直接承载可恢复/可访问/可表达三能力，probe新增监督/容量费且不证明原模型能自行调用；91–94方向存在/当前decoder使用/适配后使用与原input回退分账。本次拟采用逆合成的局部recoverability不能外推自然输入或native行为、hint与图中文字条件反侧，均不改变已有这些判定；拟NoChange—Existing，不为inverse prototype方法名另写段。若非作者发现未被承载的必要机制差额则单项重开，不自行授Existing。

## 08010 CASHEW — 2+1+2=5；必要源ready，Ch20窄差额提案

已实际读exact-v1 §4–6/主要Tables1–3、AppC与D1–3；last4-core0/1/2、required4/5保原文。固定N8/K4/T3，多候选先GroundingDINO阈值.35核object keys，再对subset生成新trajectory、迭代而非只select原答案。对象存在检出不授关系/每步逻辑/总体真值；DINO同error可传播，阈值/模型/输入身份必须独立。Table6同NKT无DINO到有DINO在ScienceQA/POPE/Ego/VSI分别增1.4/.4/2.2/1.7pp，不将全部base增益归DINO。T7 SFT-only两任务退步；T4更多开销与边际/退收益，bootstrap10k不是全训练/生成seeds。4B另训练而非8B权重直接迁移。8H100推理/16H100 LoRA，precision/latency/SLO/完整calls fees Not Disclosed；NKT多生成与DINO计账，teacher30B/30kSFT/200kRL有离线费。Eq13–14实际softmax reward-weighted likelihood+KL，不照录为标准ratio-GSPO执行recipe。

actual MODEL-SAMPLING Ch20:366–401候选身份/selection vs acceptance及visualcue uncertainty已承载判定边界，但还没有object-sensor先标注/验证候选→subset synthesis产生新候选→再次验证的consumer状态循环。拟仅在候选选择状态后补一短段，把融合新trace与投票/筛原trace区分，独立grounding误差与总预算/退路放近文；不抄训练配方/全部模块。日期dates47正常界复用；v1 abs一度不可达，currentabs仅轻核v1–3 history/无撤回标记，不采用新v3机制，exact-v1原AB/HTML身份有效。等待独立source/owner PRE，不写Books。

## 08726 Non-Ergodic DRL — 2+1+2=5；中心命题争议提案ready

实际§2–5/Alg1–2/AppA1–3必要原证在last4-core0/1/2、required4及identity6。两toy均非LLM训练实证，但直接揭示学习estimand条件；DQN当前wealth输入、常规Bellman target未改成time-growth目标。AC Alg2一次抽f后重复M轮、reward=WM−W0、仍expected-return policy gradient，状态只W0；论文摘要/结论称不改reward/objective便近Kelly。作者finite实验的40DQN/20AC、M1/2/5/10/20及随机p fullpolicy趋势保留，后者需更多episodes且更难稳定，不因此当无研究价值。

但在其独立同分布乘法赌局、固定f、同p条件下，E[WM|f]=W0[1+f(E[R]−1)]^M，M>0只改变单调强度，不把expected wealth最大化变成Elog增长；当E[R]≠1仍偏端点而非内点Kelly。这个反例绑定Alg2的固定f/独立回报前提，不宣称所有path-dependent RL无法优化增长。正文Eq12的p括号亦与Eq14不同，不采用该字面solver。增加horizon的数值/优化/抽样改变不能证明新estimand；作者近Kelly曲线与中心解释冲突，拟终态中心争议，不把实验抹去、降分或关准入。仅在明确目标/状态/回报依赖或更正Alg2并提供与Kelly相符推导时定点重开，不索取所有RL证明。hardware/precision/fullfee/SLO Not Disclosed或toy不适用，DQN Adam.8/batch2等作者配置不作训练recipe。日期正常界＋abs轻核可复用；无Books正面采用，等待非作者中心信号核。

## 07963 3DGS-Drag — 必要源已读，日期正在轻核

必要core/§4.1–4.4/AppC的copy-paste几何→synthetic view repair→3Dfit已有实际原件；原SubmittedJan12T19:57:31只是发现，另核正式ID上界/直接早正文信号。Ch24:1467–1477已实际读generatedview→reconstruction/render及合成非几何真值费用边界，待具体新增drag-state/版本承担与低分Only比较，不先Books。

下面为先前未ready历史停点；不代表08010/08726仍未读。

方法/评价/关键反侧尚未读足，普通待办，不是外部受阻或已关闭；按各已校准贡献补足最低必要内容/日期与actual owner后单篇发PRE，不等此整组。08010已读多trajectory subset/GroundingDINO object verification与RL composite reward到Eq12；尚待主要evaluation/C-D费用与teacher/onpolicy接口。08726已读toy wealth state/DQN Bellman target与重复horizon到growth界；尚待实际toy/portfolio评价与App参数，不把horizon替代objective保证。07963已读geometry copy-paste→diffusion correction/annealing与progressive relocation到§3.5；尚待主要对照/成本/limitations及日期，不把synthetic corrected views授真实观测。
