# 02/13 必要证据：10468 / 10471 / 10478 / 10480

本日 exact-v1；只采用下面实际读到的机制/对照。候选日期仍须相关公开batch确认。独立Source/Books判断待root，不授完成、实现验证或复现。

## [2602.10468v1](https://arxiv.org/html/2602.10468v1)

5标准，因具体Ch36知识差额拟深入局部。§3 actual L107–159、§4 L164–228与§5 L238–282：以traffic matrix的masked adjacency powers承载topology/round/hop分配，成本下界为dR+TΣround maxhop；只有同轮同hop不共享link才变成等式。Theorem1只是k=1、等大小流、固定hop T与重配R；最优下界不一定可实现（n8,d3反例），不能变成通用k近似保证。对称+expansion使新增短路径能删除整轮，不只是减少个别流hop；degree-k分别生成Circulant/GenKautz再选成本，greedy packing/contracting仍不是全局最优。

htsim packet simulator，800Gbps/500ns、4MBchunks，n8/16/32/64、k1/2，uniform/random/Zipf factor.4，8–64MBpair或mean。重配只在当前flows全部完毕后进行，store-forward且chunk优先；没有真实光交换器、GPU训练步/SLO/端到端收敛测量，model/precision/sequence/batch不适用。Fig11/12的39.66%/47.35%是扫R后挑最大收益配置，不是固定真实R的普遍平均；Fig14固定R成本模型选d有邻近d更好的误差，Zipf n64k2/MixNet与n8k2/FAST反侧保留。最大gap<=2.22（n<=64）、4.54（n<=4096）为已枚举规模，不是所有规模常数因子定理；模拟runs/uncertainty Not Disclosed。

拟TRAIN-DISTRIBUTED-TRAINING Ch36：当前855–874已有placement/path/schedule joint search、plan identity与仿真回退，但没有collective内重配的round-level可兑现收益条件。窄差额是短path只有删整轮才减少maxhop账、dR与传输成本共同择d，拓扑/round completion必须保持；不写作者best-case数字或一般最优保证。源锚点V3_EVIDENCE_10468_INITIAL.txt L126–159/164–228；V3_EVIDENCE_LAST_TAIL_0.txt L238–282。

## [2602.10471v1 TestExplora](https://arxiv.org/html/2602.10471v1)

5标准、暂拟仅报告。§3真实PR→测试invoke到patched function→过滤→before/after F2P以1,552PR/482repo/2,389tasks作为最终构造人口；12,227是rawPR，§4 L222又称评价12,227，保留口径冲突不借大分母。DocAgent生成documentation并给测试模型，故不是完全没有author-generated intent信息的自然探索；AppendixB L546–561实际Reader依赖target代码与repo内部context、禁internet，未明确pre/postcommit身份，不能声称绝无goldpatch泄漏，也没有证据证明已泄漏。无需读全2,801行脚本日志。

HP为test-level，F2P Eq2为PR-level至少一个test的basefail/headpass；§4 L230–236却解释为整suite所有tests均正确才pass，与Eq2不一致，因此不采用‘更多tests必稀释发现率’为因果定律。固定人口、entry coverage/changed-line coverage与F2P需分责；时间bucket和域间排名没有独立污染控制，不能推出训练已污染。六model Qwen3Coder30BA3B/GPT4o/GPT5mini/o3mini/o4mini/Gemini2.5pro，whitebox implementation+deps、blackbox入口+doc，Lite330PR/517samples按人doc质量选择，3重复；硬件/precision/token预算/temperature/latency Not Disclosed，数量不是同compute比较。GPT5mini Lite11.84%仅作者协议；没有运行artifact。

核心paper足够支持受限任务与人口/metric区分，不支持稳定新评价规律；拟仅报告具体原因是中心suite解释与实际Eq2不同、doc source身份缺失，不改Ch66现有testing/oracle分责。源V3_EVIDENCE_10471_INITIAL.txt L113–206，V3_EVIDENCE_LAST_TAIL_1.txt L222–243，V3_EVIDENCE_LAST_FINAL_0.txt L546–561。

## [2602.10478v1 GPU-Fuzz](https://arxiv.org/html/2602.10478v1)

6D安全受影响深入。§3–5 constraints保证API参数域，SMT随机dim排除/hashmix排除hashclass增加多样性，不证明完整覆盖；具体有效参数stride200/input(10,40000,2)能触发host64→32计数截断和CUDA grid/index错误，compute-sanitizer报告OOB写，Python是否crash/数值oracle不能代替memory oracle。作者13unique bugs与5×4GPUhour PyTorch106±8 occurrences分开（26±5memory/80±7configuration），后者不是106独立漏洞。NNSmith293±19 inconsistencies/3±1exceptions是不同oracle，不能作为所有bugs提升率；13列表中11confirmed/1reported/1fixed仅作者披露状态，未独立复现或审所有issue。

2XeonSilver4510/H100PCIe Ubuntu24.04.2 driver580.82.07 CUDA12.8.93 Python3.11.13、PyTorch2.3.1cu121/cuDNN8.9.2、TF2.20/cuDNN9.13、Paddle2.6.1绑定版本。2628Python tests/13operatorfamilies，100–150LoC/family人工modeling；不授所有最新框架/shape安全，sanitizer只查memory，不查silent numerical/performance；OOM已排除。未给production多租户exploit或普遍恶意可利用性，不能改写为真实攻击成功。

拟INFER-TENSORRT-LLM Ch49当前70–77有lowering→numeric/runtime commit但不含valid API边界参数与低层memory安全的独立oracle。差额是合法参数空间仍能暴露layout/count/grid的整数范围条件；受约束operator fuzzing与sanitizer补充数值/模型测试，不替代其语义质量。源V3_EVIDENCE_10478_INITIAL.txt L110–150、METHOD L154–210、V3_EVIDENCE_LAST_TAIL_2.txt L211–236；书稿需root核后窄锁。

## [2602.10480v1 NeSyS](https://arxiv.org/html/2602.10480v1)

5标准，暂拟仅报告。§4 L110–162：LLM K候选概率p被exp(γΣwjfj)重排，fj有限[-1,1]且γ有限，因此是soft reweight，不是零概率hard constraint，候选缺正确状态不能凭rule创造；text belief是truncated history，不是可识别真实state。dev residual聚类→gpt5mini rule→dev正确率提升才accept，最多3reflection，再按nonzero rulecount k=0全部保留/其他1/k抽样；k只是规则激活数，不是正确性/覆盖保证，coordinate descent权重也依赖dev。

§5与E是expert trajectory构造的multiple-choice nextobs/reward/inventory，Webshop90:5:5 trajectory split并人为buy-fail插入、用Llama3.21B错误答案做distractor；不是真实online长rollout安全。Llama3.21B/Qwen3-4B，symbolicteacher gpt5mini，ScienceWorld45%、Webshop60%、Plancraft35%训练例，不能写‘固定一半compute’：teacher/rule/reflection/validation和不同例长费用未披露，硬件/precision/seq/batch/epochs/seed uncertainty Not Disclosed。Fig4 rule-guidedvsrandom原neural单独近似，combined才差异；LlamaWebshopPhase1 combined80.9<symbolic83.4直接反侧；训练XGBoost router83.2/84.6与oracle91/94.1不同。

仅报告理由：局部候选重排+dev规则选择有真实新增机制与实验，但有限MCQ支持不授deterministic约束、真实worldstate/长rollout、等总成本替数据保证；不因ScienceWorld名字排除一般模型方法，也不把领域应用入Books。源INITIAL L110–150、METHOD L150–162、LAST_TAIL_3 L197–240、LAST_CLOSE_RAW L295–332、LAST_FINAL_1 L445–464。

## 旧 PRE 当前正文比较收束（作者）

10468：实际Ch36 L865–879 placement/path/collective plan identity、仿真回退及其他重配段未承载collective内dR+各轮maxhop的成本轴，缩路径只有改变完成轮账才可兑现。拟放collective成本/round讨论内两短段，保留contention使下界不能取等、固定hop/等流量条件、模拟不等训练提速；待Ch36窄锁。

10478：最终已有覆盖/NoChange。实际Ch49 L1460–1476 model–kernel callgraph/shape/buffer/launch→symbolic memory/thread oracle与host变量联合约束、具体反例回放，已承载“API合法不证明低层访存安全”；L1492–1496独立reference/tolerance与错误控制补数值责任，L2015–2017调用序列也不从operator数推覆盖。GPU-Fuzz的整数count/grid/stride边界是这一合同的局部反例而非新的memory oracle owner。把原笔记70–77误作唯一owner的缺口纠正；不声称具体GPU-Fuzz算法或当前13bug已在书稿，不为补论文名制造diff。具体有限原源/版本与未复现限制保留。

最终状态同步（2026-10-04）：本组必要源/处置独立通过：10468 Ch36实际两段/完整邻接/末注root非作者POST通过；10478具体已有覆盖/NoChange已独立认可，10471/10480仅报告，均不授production或具体算法已在书稿。日级另验。
