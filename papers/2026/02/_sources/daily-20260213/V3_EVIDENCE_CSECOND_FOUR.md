# CSECOND必要证据：10940 / 10949 / 10953 / 10956

四家族完整v1题摘及有限增量已root准入校准，均属于119原字段落窗交集；不以Submitted当public。采用exact-v1；当前abs轻量字段为10940v1、10949v2(06/02)、10953v2(02/25)、10956v3(03/06)，无明确withdraw/correction说明；后版本号本身不触发全史比较。作者必要支持/直接反侧读足即止，root有限必要证据/Only与中心争议处置已核；SOAR获Ch24窄锁待实际写后核，未核artifact或复现。保存原返回CSECONDINITIAL0–3、CORE0–3、MOREA/B/C、LAST/FULL；原Source L不等文件物理行。

## [10940 FastUSP](https://arxiv.org/html/2602.10940v1)

5（2+1+2），具体编译兼容/分布式量化的设计假设反侧深入。§3按compile/reduce-overhead、跨nodeFP8AllToAll、doublebuffer Ring组合路径；可保留Qwen4GPU+Ring触发Inductor tiling失败、dynamicflow需max-autotune-no-cudagraphs这类有限兼容边界，不把成熟kernel/comm overlap本身作为新无损机制。Algorithm1每rank由localmax求s、交换FP8 tensor后用本rank s还原；未披露source-scale交换或共同scale约束，跨rank s不同则对端值还原不能据该伪码保证，实际code未核。<.1%K/V误差未有对应质量表支撑。

中心硬件冲突：Table3同时写RTX5090 32GB和NVLink900GB/s；NVIDIA原Specs明确NVLink No（[官方规格](https://www.nvidia.com/en-gb/geforce/graphics-cards/50-series/rtx-5090/) L566/593，MOREB原返回）。这不是小幅性能差额或准入EX理由；原硬件/拓扑和“NVLink上comm仅5–10%”归因暂不采用，须作者更正实际GPU/PCIe或NVLink topology与对应测量才能重开。Algorithm2只伪码不能确认completebuffer/readiness实现。

原protocol PyTorch2.8/CUDA12.8、FP8weights optimumquanto、30steps，FLUX12B1024²与Qwen1024×768，para_attn USP baseline，2–3warmups后同步GPU/barrier墙钟exclude modelload。Table4有限2/4/8GPU FLUX8.64→7.46/7→6.25/5.22→4.67s、Qwen2GPU16.33→14.92s原值仅争议作者记录；compile/FP8/Ring未全factorial，Table5microseq2048非端到端归因。batch/concurrency/SLO/重复seed/CI、quant配对quality和actualtopology Not Disclosed或冲突。处置：审阅结果争议，Books暂缓；有限compatibility/量化metadata反侧可报告，硬件/性能中心隔离，不进入Books或正面性能保证，不降分隐藏争议。原CORE0 L187–262与INITIAL0 L270–307；硬件MOREB L566/593。

## [10949 Lyapunov Initialization](https://arxiv.org/html/2602.10949v1)

5（2+1+2），固定宽度深LeakyReLU的初始化假设反侧定点深入。§3独立同分布d×d、无bias、α非0；entrydensity有界/finite2ndmoment/identity邻域positive，或scaledHaar absolutelycontinuous/locallypositive。LLN/lognorm与CLT不是LayerNorm/residual Transformer性质。Gaussian λ=logσ+I(d,α)、Haar λ=logη+I(d,α)−I(d,1)用numericalquadrature提议λ0 scaling；Table1He低宽negativeλ、unscaledorthogonal不自动抵消非线性。λ0只去掉线性depth drift，原§4明确lognorm仍O(sqrtdepth)波动，非所有sample激活bounded。

直接限制：Lemma3.5纯ReLU/positive-onlymatrix失败，tanh CLT不沿用。Theorem3.4写对所有α≠0及Haar γ>0有明显degenerate例：α=1且Haarscaledorthogonal使norm恰η^l|x0|、中心化lognorm恒定，不能有strictpositivevariance；这是作者本轮直接代入反例，不声称整份proof已核。因此不采用原全条件CLT、universallystable或“zeroλ→smoothloss/长期optimization”保证。Alg2挑O(sqrtdepth)候选以输入期望norm近1另付多次forward，未核该数量对任意inputdistribution的uniform成功概率。

§5 width2/depth40拟合五次polynomial，7methods×100seed×12hp=8400runs；score3Gaussian mixture width2depth30、4methods×15seed×8hp。Adamweightdecay、eachmethod independently chosenHP，best80%testloss seeds选择HP再报告这些的median/smoothedloss；不是unselectedseed median、独立heldoutHP或同总初始化compute。J附加input/outputlayer、quadraticLRdecay，curvewindow100/10/1000；conventionalorthogonal中程胜sampledGaussian直接反侧。hardware/precision/实际wallclock/CI与totalcandidate成本ND，不授现代宽Transformer训练速度。处置提案：OnlyReport窄理论/低宽训练反侧；原CLT严格正方差普遍保证隔离，不移数学处方入Books。Ch28现349–354只承载parameterization scale与featurelearning分责，不称已覆盖本篇Lyapunov算法；局部训练本身未建立生产recipe。MOREA L172–266、MOREB L299–387、MOREC L399–424、LASTFULL L1492–1519。

## [10953 SOAR](https://arxiv.org/html/2602.10953v1)

5（2+1+2），标准与拟接口缺口定点深入。§3 PBS探索的是unmask位置，所填token仍argmax，不是vocabbeam；每个candidate累积tokenmaxprob的平均confidence排序，不是sequencejointlikelihood/正确性。每个beam分支高confidence位置存在则全部超过τ提交；候选合并重排后，只有最高score分支来自parallel模式才collapse到单一路径；否则扩topK位置（K2）single-position分支，依当前confidence保留beam，已经提交位置不回改。fixedparallel n2破坏位置搜索收益、beamwidth线性成本，是位置探索预算与并行commit预算不同的证据。

LLaDa8B/Dream7B、T0、max256/512，单A10080GB、HumanEval0shot/MBPP3/GSM8K4，基于harness，总benchmark inferencewall对greedy SpeedUp；τ分别.95/.9。Table1SOAR相对adaptiveparallel可慢（LLaDaavg1.62 vs2.19），DreamGSM8K256 speed.95<1，不授所有workload更快。普通PBS平均speed.54，提升quality需要搜索成本；更多beam不免费，固定并行PBSquality退。§4.4method-level confidence与ARness相关不能解释全部因果；同模型不同采样改质量/难度人口，“entropy sink”是hypothesis。Table2替换margin/NegEntropy、Table3DreamOn变量长度有限支持，非任意长度/词表/模型proof。precision/batch/concurrency/SLO、timing完整边界/seed不确定性ND。

Ch24实际差额：actual300–336已有goldplanner/window/entropy boundary、单路径 vs多样本探索与positiontemperature；新增316/318融入同状态探索位置而内容argmax、per-beam门槛及合并排序后仅最佳parallel-origin分支collapse接口。score不是jointprob、commit仍不可撤销、beam预算与parallel预算分账及greedy/保守fallback。root必要源/current owner PRE通过后，实际POST核当前300–333及末注，写后通过、窄锁释放；第27家族实际整合，不授日级。CORE2 L102–202，MOREA L206–267，Table1见INITIAL2；不展开无关appendix或code。

## [10956 Temporal Attention Diagonal Sink](https://arxiv.org/html/2602.10956v1)

5（2+1+2），标准与数学主张直接反侧定点深入。§3/A给singlelayerlinearQKVsoftmax的value/key/queryJacobian，querypath只在i=j非0；residual另加δijI。对j做uniform平均的valuepath是||WV||/T，keypath上界CK/(T sqrt dk)。这不是每个指定offdiagonal的均值，也不是C随T恒定的证明；CK/CQ含value/query/key norm，未给统一长序列界。Eq8把offdiag条件仍用1/T而非条件归一T−1且把diagquery项乘alpha_ii，A的querysum实际遍历全部m，不由现式推出该乘法因子；upperbound较大也不证明sink必然存在或residual实际norm稳定下界。核心恒等链仅作诊断分解，不授“长窗远程信息必O(1/T)衰减、对角O(1)保证”或任意LLM因果。

METR-LA，temporalattn8heads→singleGCN(fwd/backlearnedadjacency)，input12/predict12，absolute tAPE；AdamWcosine150epochs/5warmup/lr.001、4seed mean±sd，penalty−.1/dropout.2经过选择。Table1fullmask多数不胜noreg，dropout/penalty小幅局部改善；Table2input/predict36的dropout多数退，penalty也非allmetricbest（MAPE36 14.1929>noreg14.0347），Table2宣称±SD但未列SD。选最佳regularizer额外校准，未给independenttuningtest划分、hardware/precision/batch/生产SLO或总成本ND；不外推causaldecoder、全residualnet或longcontextcapacity。处置提案：OnlyReport局部regularization反侧，争议普遍sink定理隔离、不入Books；不是范围排除（modelmechanism有准入潜力），Ch14实际121–123路由mass与value/下游误差不同的通用原则不冒充已载本篇公式。CORE3 L71–111/168–212足够；不读无关图/所有proof。
