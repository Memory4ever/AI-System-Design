# 本日B必要证据：10525 / 10531 / 10538 / 10545

均为精确v1、准入已校准；root实际Source/处置复核通过：10525/538仅报告，10531/545具体owner差额支持，待逐项date和写锁；不授日级完成。原返回按实际Source L定位，不把保存的无关文本称为已读附件。

10531证明勘误限制：Appendix A L350把conditional expectation写为hatθ_t有误，应为αθ*+(1−α)hatθ_t；主recurrence独立total variance可成立，不背书整证明无误，也不采用GPT setting冲突编号。

## [LHAW](https://arxiv.org/html/2602.10525v1)

5（2+1+2），评价反侧定点深入。§3.1–3.5实际先筛fully specified可解人口，再删1/2段并以3次trial的checkpoint terminal tuples判outcome-critical/divergent/benign；TAC只13原任务、部分checkpoint≥50%，SWE需≥3 F2P及各reference pass@3>0，MCP native≥75%checkpoint成功。285 variants由不同原任务人口抽样，类别不是开放请求的语义真值或永久失败证明；new-task过滤另依赖LLM judge。ask_user simulator知道原prompt/被删内容且只答相关问题，非真实用户验证。

§4.1–4.4五API模型（Opus/Sonnet4.5、Gemini3Pro/Flash、GPT5.2），每variant3独立trial。MCP Opus47→78 pass@3仍低于原100；SWE Sonnet没有澄清gain，是直接反侧。persona三prompt控制主观打扰成本，不是测量用户耗时/金钱；Gain/Q是aggregate比值，不能推导单问题因果价值。生成长度、temperature、API版本timestamp、真实E2E资源/统计CI Not Disclosed；API实验precision/hardware非本地模型可比配置。

拟仅报告：具体受控ambiguity评价增量成立，但选择人口、有限trial与有GT simulator限制了转为通用澄清policy/cost函数，不能从这些结果给生产授权或可靠性条件。没有因此删候选或降分。必要原源：`V3_BNEXT_NEXT_0.txt` L163–181/196–251/275–324（Table3还见`V3_EVIDENCE_10525_INITIAL.txt`）；支持/反侧足够即止，不展开persona/模板附件。

## [From Collapse to Improvement](https://arxiv.org/html/2602.10531v1)

5（2+1+2），标准并核采用定理的必要证明。§3 one-hot fixed-context categorical empirical proportions，每代样本条件iid来自α_t P*+(1−α_t) P_hat_prev，R_t=E squared parameter error；Theorem3.1的recurrence来自total variance，AppendixA L338–364实际核。fresh P*抽样不是固定有限human anchor再采样；真实Transformer/共享context表示不在定理内。Cor3.2固定n以n0=n收窄，α下界>0且n_t→∞有一致性；α下降时Prop3.4是充分非必要采样条件且α未知。纯synthetic不增加关于P*的新信息，不是推断所有合成训练都无益。

§5.1 K50、T200、100重复均值/CI比较α=.1及衰减与n固定/增长；§5.2/C.3 nanoGPT16M、4层4head/256、context128、Adam3e−4、B32、10轮/10随机文档split重复，每轮scratch，500文档heldout，生成约150words。作者机器描述28nodes/8×A40 48GB不等实际每arm占用，precision及准确token/算力预算ND；每实验30–40min、约3000epoch不授规模化。原文setting2实际3/4fresh却写α=.25；最后setting3既不改进又改进编号冲突，**GPT各setting方向不采用**，保留原证而不改分/排除。

拟Ch27差额：当前354–378已讲corpus/parameter recursion、fixedhumananchor及distribution geometry阈值，却未分清fresh P*样本与固定经验anchor，也未把每代n_t作为不同控制轴。仅拟补“freshness/mixture/每代sample-size需分开验收、conditional toy recurrence非生产比例”，不采用未知α最优配比/GPT矛盾编号。需root判是否长期缺口、必要深入和写锁，尚未写。原源：`V3_BNEXT_CLOSE_0.txt` L104–134/338–364；`V3_BNEXT_METHOD_2.txt` L154–187；`V3_BNEXT_STOP_1.txt` L253–283；`V3_BNEXT_CONDITIONS_RAW.txt` C.3 L691–696。

## [Why Agentic Theorem Prover Works](https://arxiv.org/html/2602.10538v1)

5（2+1+2），标准理论条件。有限horizon、compact goal embedding与bounded goal mass把formalprover变成reachability MDP；verifier完整state/Markov sufficiency是假设，不是LLM embedding自然保证。§6.2 Lemma3/Theorem4实际uniform Q* score误差ε给greedy每步≤2ε、全程≤2Σ ε；不是任意beam保留集合、worstcase theorem容易或所有搜索减少complexity。

§6.4/D margin条件需在实际occupancy上near-tie尾部小；D.4明确失败时只线性误差/排名不稳定。D证明有局部“regret≤best-vs-second gap”方向不一般成立，greedy上界仍由§6.2 uniform-error直接支持；**不采用泛top-k/beam fast-rate保证**。Theorem6主文squaredERM到uniform声明不能只靠martingale deviation；必要AppendixF L905–966把Q Lipschitz、η-net逐点m个条件无偏独立Q* targets、extension/类投影列明。普通continuation rollout得到其policy value，不自动是Q*；未展示真实prover有该oracle/coverage。采用边界仅条件性greedy score误差框架，不授实际训练样本/效率保证。

拟仅报告：这是一组理想空间、oracle target和coverage下的统计解释，没有验证真实pipeline满足这些条件；条件框架不能替换现有planning的外部verifier和独立终局验收。理论材料HW/precision/batch/benchmark收益不适用，无实测速度。保留具体反侧不靠删项避争议。原源：`V3_EVIDENCE_10538_INITIAL.txt` L167–207；`V3_BNEXT_CLOSE_1.txt` L321–451；`V3_BNEXT_NEXT_2.txt` D L774–814；`V3_BNEXT_LOCAL_1.txt` L818–844；`V3_BNEXT_CONDITIONS_RAW.txt` F L905–966。未遍历其余Appendix。

## [μpscaling Small Models](https://arxiv.org/html/2602.10545v1)

6（2+2+2），标准；若落实以下长期缺口则受影响深入。§2.1 biasfreeMLP integerwidth clone用1/k_input重标权重；SGD lr乘k_output/k_input且same data/randomness使函数轨迹精确等价，必要归纳证明已读；一般optimizer需homogeneous entrywise update并联动lr/decay/epsilon。D实际midtrain迁移namedbuffers及momentum/exp_avg按gradient scale、exp_avg_sq按其平方，缺state只能是新训练不授exactcontinuation。零noise保持symmetry不利用新容量，μP尺度noise解锁容量却允许loss shock；实际不是函数保持与新容量无成本同时获得。formalgeneralTensorProgram/finitewidthgeneralization未全核，不采用普遍architecture定理。

§4/F.3 GPT2 12层12head、perhead16/32/64；FineWebEdu CC-MAIN-2013-20、train11.8B/val5.5M，effectiveB.5Mtokens、每阶段10000step=5Btokens；AdamWβ(.9,.95)/WD.1/clip1/constantLR、BF16+TF32、2H200141GiB DDP。基线wide从scratch5B，warmstart还需base5B与small-system两个sweeps，fixed postgrowth steps不是同总token/FLOPs。MLP/ResNet五随机run/minmaxbands；ResNetwarmstart validation更差，不能把更低trainingloss当普遍泛化。width128/256/512、k2局部noise/LR sweep稳定不保证任意scale/architecture。

拟Ch28具体差额：现220–244讲mapping/activation/symmetrylock/reset/rewarm，却未给joint lr/epsilon/state-moment尺度形成**等价continuation分支**，也未把对称保持与新容量noise明确作为两种不同目标。最多两段融原statecontract：窄MLP条件、moment阶数匹配、noise/旧训练预算及ResNet反侧；不把原reset/rewarm合理分支静默替换。Source/owner及邻章核后才申请写锁。原源：`V3_BNEXT_NEXT_3.txt` L169–215/331–370；`V3_BNEXT_FINAL_2.txt` L234–263/286–307；`V3_BNEXT_LOCAL_0.txt` L892–905；`V3_BNEXT_STOP_0.txt` L1513–1537。formalgeneralall附件不展开。
