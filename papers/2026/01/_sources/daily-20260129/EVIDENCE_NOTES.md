# 2026-01-29 evidence notes（逐项推进，非全日完成）

当前语义状态以本段和README为准，下面保留历史待核标签不表示新增普通任务：冻结42确认窗唯一家族=41阳性必要源/Books判断实际root通过（6整合/5文件、2Existing、33Only）+1中心争议/暂缓。DART19278原已知遗漏项恢复的必要原源/成本/大batch反侧独立通过，19400必要公式争议处置通过；9同稿first-public日期终态隔离不计确认窗分母。执行侧普通待办0，仅整日报告日级验收尚待；不重审有效源/POST，不扩发现。

## 19278 DART — 原已知清单遗漏恢复，root必要标准证据与限定Only通过

完整原题摘AB3.md/PRIMARY_19278.md；SubmittedJan27 07:04:24Z与createdJan28 02:59:26Z，官方schedule下界01Z，BJT[Jan28 09:00,10:59:27)完全落窗。模板ICML关键词不当明确accepted旧公开信号，不扩会议。原2+2+3暂定表并非最终评分，实际局部分支2+1+2=5：target低/中/高hidden拼FC后一层并行预测prefix-only future marginals，shifted output与隔离maskblock KL teacher privileged future targets；不是iterative denoise或true联合conditional，Ngram仅surface continuity。

v1 §3–5/Tables1–5/B–D与Table7关键负侧已定点读：H20-3e141GB×8 server/90CPUcores/900GBRAM/PyTorch2.8、defaultb1/d8；ShareGPT+UltraChat280K/context6400/3epoch/AdamW2e-5/clip.5，EAGLE3复用公开权重，same sources不是严格同训练总预算。Table1 Qwen1.7 τ3.60<EAGLE3 3.80却speed2.61>2.01，不能只最大化接受长度；γ.6仅局部取舍，γ.5更高firstposition但τ低，Table2 Ngram有接受改善不认证语义。draftforward1.5ms加tree2ms不能叫零开销，singlepass不证明成本完全与d无关。

3gram trie1.3Bnodes/43.5GBdisk/~100GBCPU RAM，C++OpenMP同NUMA、warmquery6μs非端到端；k25/w20/θ59，未核ancestor closure/完整stochastic verifier代码，不认证lossless分布。Qwen3-8B HumanEval b64 DART仅1.01×、EAGLE3.98×，并发/SLO/TTFT/precision/IOlimits/seedCI ND。OnlyReport为具体并行drafter+CPU树ranking的局部资源质量取舍，不改变已知correct verification责任或授通用Serving保证；root实际准入、必要标准原源与限定Only复核通过，整日报告仍待日级验收。

## 19048 NuiWorld — root标准必要证据与限定Only通过

[v1](https://arxiv.org/html/2601.19048v1) §4.2/5/Tables2–4/B.2：把chunk VecSet V×c放channel，使token数R×C而非R×C×V；attention长度项省V²但投影channel成本不零。冻结DINOv2 sketch crossattn+row/col+size embedding，rectified flow，CFG dropout.2。非action-conditioned dynamics，不把静态3D生成当可预测world transition。scenario各自训练、NanoBanana/Trellis2生成数据不是真实几何groundtruth。default推理给gold R/C，size predictor使medievalCD .373→1.070；宽度/压缩消融同时depth24→16，VRAM70GB，不授独立compressor无损因果。

2L40S/b24/depth16/width1536、7200train800validation、320epochs/lr1e-4；XL额外1800大场景finetune4L40S/lr5e-5，40×40样例不等零适配泛化。15×15 embedding5.96s但decode64.61s，18×51 5.56+276.76s；Trellis不同image vs sketch/shape条件，不比较裸5s作端到端胜利。precision/推理hardware/B/seed/CI/采样步/并发SLO ND。2+1+2=5拟Only：具体静态场景factorization/capacity局部分支，未改变通用world dynamics/生成执行contract。

## 19285 ScoreSmoothing — root标准必要证据与限定Only通过

[v1](https://arxiv.org/html/2601.19285v1) §3.2/4/5/Table1/B.1：去noise输入的weighted DSM Eq9与按noise threshold/TopK温度target，T=max(σcollapse/σ,1)；作者明确temperature学smoothed proxy而不是真pMN score。两最近center/shell几何与局部expansiveness不是大模型generalization或隐私安全证明。noise-level mismatch令unconditioned ODE fail，修正要nearest-training-point估σ，retrieval成本另计；SDE局部selfcorrect不授所有schedule正确。

NCSN++/VE-SDE，CIFAR10 b128/1Miterations、CatCaracal1200 b64/40K、CelebA64 b64/700K、lr.0002/EMA.9999/seed42，最佳checkpoint不同选择；4L40S/2H200主配置，2L40S前1000batch成本单列。Table1 CIFAR FIDtest conditioning6.56/unconditioning7.34，temperature pixel51.08→feature7.98仍差baseline；CelebA局部改善7.81→7.34。feature KNN依pretrained encoder/proxy，不能由小samplecost宣称dataset独立常数。dtype/生成B/IOconcurrency/重复seedCI ND；NN比率在CIFAR不辨识memorization也是直接反侧，不扩所有图表/appendix。2+1+2=5拟Only：局部score-target替代和schedule失败条件，不授统一privacy或foundation-model分布保真规则。

## 19895 KEEL — root精确v1 PDF必要证据与Ch17 Existing通过

PDF Jan28页首/v1 Jan27身份已定点核，HTML July28模板日不用于firstpublic。精确PDF Eq8/§3.1/3.3实际是LN(αx+F(LN(x)))，α=L，L含attention与FFN子层；首二子层移除α/outerLN变PreLN。不是摘要dynamic-gate接口。Eq18残差path norm仅O估计，Eq19把近似当limit且不含完整transform Jacobian，不能授全网络下界、所有训练轨迹稳定或无限深保证。

§5.1 MaxLR仅warmup divergence定义，loss plateau/spike/slow-training人工标准；§5.3 B1024/seq4096/190B+60B/AdamW.9,.95/wd.01/clip1/2500warmup，1024子层=512decoder blocks、Keel LR.0045 vsPreLN.003非相同LR。Table3均值57.9→60.9但ARCE80.4→80.3、64layerARCC33.7→33.6、128HumanEval17.1→15.9。3B固定budget 512×1024/128×2048对比与1T主run b2048/750B+250BCPT不同，1T均58.7→62.5、sameWinogrande66.7；不能合并质量/数据和depthgrid成本。hardware/precision/训练耗时/seedCI/推理B长度并发SLO ND。2+1+2=5：Ch17 319–349已明确可控carry/transform、scaled PostNorm与Keel局部极深窄模型及normalization/residual/depth/width/LR/data联合选择；拟采用命题已被实际承载，ExistingCoverage待root，而非声明α所有细节现正文都有。

## 19132 INC — 具体差额深入与Ch36实际POST通过

[v1](https://arxiv.org/html/2601.19132v1) Low Precision Data Types L110–115：Core-INC中partial accumulator须上送，扩大位宽可抵消理想2×流量节约；首个真正reduction switch不等首hop，上送upcast、root再castdown的成本依树拓扑。Edge-INC可按index range在NI本地保宽accumulator。Ch36原SHARP受限类型/顺序/资源/fallback缺这一跨switch数值表示与流量关系，现213/215两段整合；至少翻倍仅原源策略/拓扑分析。2+1+2=5，具体知识反证深入，不扩六障碍/无关证明。root必要源PRE及实际213/215、211/217–223与末注POST通过，窄锁释放；日级Gate未授。

L129–150固定树/reproducibility与Amdahl模型是关键反侧；fixed8GiB352→151ms仅性能模型，不能把34%整step或10×当实测。硬件/precision/batch/模型/通信并发/质量/SLO不构成实测配置，Not Applicable于这项概念边界。并非所有Core-INC一定无益；局部NI/混合路径、有限现有类型与普通endpoint reduction共存。

## 19239 Project-scale vulnerability — root必要评价反证与限定Only通过

[v1](https://arxiv.org/html/2601.19239v1) III–VI/TablesI–VII：5LLM工具/2static、C/C++/Java八CWE、known222与latest24projects是不同人口。known TP定义命中vulnerable program point，不全标非漏洞space；平均recall27/128与69/204是tool-case分母，不是222独立样本总体率。latest由二作者每tool/project最多10warnings双标/讨论，共385/>150人小时，SFDR97% RepoAudit与94.4%IRIS只是被采样报告比例，不当全代码FPR/未来traffic。RepoAudit known给exactsource/sink仍13controlflow/11concurrency misses，三层深度与sanitizer/平台互斥路径反侧限定snippet→project外推。

released package原backbone/建议参数，Claude3.5Sonnet/O3mini/GPT4跨工具非同model成本控制；latest RepoAudit用defaults不同known人工source/sink。API运行于dualXeon6388/512GB/4A800/Ubuntu20.04；precision/推理batch/IOlimits/concurrency/seed/CI未披露。TableVII RepoAudit max225493.97K input而introduction误写38310.33K，LLMDFA max4638min；不照录“static仅秒分钟”，CodeQL max378.95min。2+1+2=5，代码评价/安全设计反证深入。拟仅报告有限project/tool/population的新测量，不伪记Ch66 exact已有覆盖，不把该率或代码建议变为普遍可靠性规则；若root认为具体owner缺口成立再定点PRE。

## 19249 GLOVE — root受控drift必要证据与限定Only通过

[v1](https://arxiv.org/html/2601.19249v1) §4.1–4.2/§5/Table1–2/B1–B5。state-equivalence依task matching，连续pth低历史frequency才probe，同state/action重试α、删除counterparts替经验分布；要能重访/重放，低频不是drift真值。采用的具体增量是同memory方法在20轮统一人工drift中source优势可变hidden劣势，activeprobe也并非全修复：GPT4o GenerativeAgent WebShop hidden75+GLOVE仍75，VanillaFrozenLake source47.5→35。implicit WebShop warmcolor黄→红/goal reward互换仍有reward反馈，不称无任何外部监督或环境ground truth。

Backbones/API异构，20round不是20独立seed/CI；hardware/dtype/temp/B/IOlimits/CI、probe总成本和实际阈值未披露，曲线spikes不授negligible端到端cost。仅保受控memory-vs-drift反侧2+1+2=5；不采用Hoeffding/finiteK理论为开放任务检测/安全保证。Ch77 29–37与949–963已有history条件、unknown-current、重取fresh证据原则；这里具体same-action可重放并替counterpart只是局部分支，拟仅报告而非ExactExisting这些细节，不恢复旧7分或全freshness扩展。

## 19312 LightSBB-M — root必要假设与局部评价限定Only通过

[v1](https://arxiv.org/html/2601.19312v1) §3–4/§5–7/B：可变volatility与drift代价β、GMM解析score+neural inverse transport交替训练。dual控制要求finite second moments、β>1/T与Hessian<βI；formal optimal solution不等finiteGMM/MLP训练已收敛，作者明确无algorithm convergence proof。inference端score在T未定义，以T−δ=.99近似；不授simulation-free等于精确/一网络forward或全部heavy-tail可行。

2D10Ksamples/5seeds/W2mean±sd，β10–100依task，β1/T1失败；Table1不同task采用各bestβ，B的N→moons K25而其他默认K5，不照录统一5次。70K FFHQ/60Ktrain10Ktest→512D ALAE是qualitative image样例，无FID/配对identity/costmatched量化因果。单A100SXM4 40GB/B512/lr1e-3/15000epochs；2D<10min/10Ksample<1min不授大基础模型serving，dtype/seed具体值/IOconcurrency ND。2+1+2=5，拟仅报告生成transport的局部替代与明确假设，未建立离散/多模态主线的统一采样选择或全维度可靠solver，不扩大到financial time-series/应用路线。

## 19404 RPO — root标准必要证据与限定Only通过

[v1](https://arxiv.org/html/2601.19404v1) §3/4/Tables1–4/§5：缓存旧回答，uniform m截去尾部，固定prefix条件下只新rollout suffix；不声称只对suffix反传，因为Eq5/8仍写全trajectory sum。cache初始samples未保证正确，ε-greedy最高reward/否则suboptimal，非始终verified hint。长度aware sigmoid reward用于allcorrect仍区分长度，分数中心是有限训练取舍，不采用Eq9无条件variance不等式或所有GRPO不适合lengthreward结论。没有length reward时1.5B GRPO49.1→47.5、7B65.6→63.6；正确quality条件反侧必要。

DeepSeekR1distillQwen1.5/7B、open-rs7K、4epochs/B576/G6/temp.7/max4096、8H20 96G，但sampling仅1GPU；cacheinit全GPU/vLLM B256约20min。L800主时间77.28→8.37h/84.53→23.50h，L300 suffix145.88/147.06tokens不可混成同时间setting；prefixprefill/update/cache成本与训练结束质量绑定。zero-shot3runs，其他ablation1run，precision/evaldecode/seeds/CI ND。maxlength更大RPO exploration反而更弱、length参数α非单调。2+1+2=5，拟仅报告有限缓存prefix训练分支：改变exploration/context与reward，质量收益依配方，不能授onpolicy等价、一般无损训练加速或不含初始化成本保证。

## 19611 MEA — root标准必要证据与限定Only通过

[v1](https://arxiv.org/html/2601.19611v1) §4/5.1/5.2/C/F：K/V head-level mixing加GroupNorm实际RMSNorm，RoPE线性保证同position下mix移动；GN缺失在作者smallupdate/有限训练setting退化观察，不采所有THA等价/无表达增量定理。Llama3.2-1B架构untiedembeddings、20Mtokens B/500Btotal，50Btoken4LRgrid按各architecture最大stableLR选择；非统一LR唯一因果。Table1MEA46.39≈DFA46.36，OBQA19.8<21/Wino54.14<56.04。未给newhead机制与GN完整factorial交互证明。

virtualhead KV是SVD basis/reconstruction近似4→2，Qwen3-30B-A3B/48layers middle12–35或deep/full；AdamW peak1.6e-5/B68Mtokens/1epoch、C中22B高质量subset，full-recovery额外1Ttokens，不能无cost同质量。总scorebase58.68/CPT54.39/half52.94/full47.89/recovery52.36，math65.12→50.48基线亦退；compressed不原forward精确无损。hardware/precision/seq/seed/CI/实际memory吞吐/latency ND，F只是approx部署形式非production复现。2+1+2=5，拟仅报告head-recombination/conditional compression配置，未建立KV基础ownership/factorization新通用保证，不因half-memory数字授透明替代。

## 19657 DLM Sink — root标准必要证据与限定Only通过

[v1](https://arxiv.org/html/2601.19657v1) §3.2/Eq6/Tables1–5/§4.4/A.1：extra token只selfattend，其他tokens可见、各diffusionstep保持，限制其读取context但不证明embedding/层输出纯零或普遍语义中性。moving-sink低valuenorm/attentionmass是作者100K inference-step统计、不是100K独立tasks或因果唯一机制。Stable vszero-value近似效果以及1/2/4和front/end控制只支持有限offloading branch；不能由1token饱和推出唯一原理。

Qwen2.5base.5/1.5B转DLM、Fineweb30/100Btokens，scratch.5B SMDM/SlimPajama100B；AdamWβ.9/.95/wd.1、cosinelr1e-4(min1e-5)或scratch2e-4(2e-5)、batch512/4096/scratch256、GSM8K SFT10epochs/context2048。0.5BSIQA40.28→37.82、1.5BRACE37.80→37.61/LAMBADA66.58→66.41、scratchARCc25.09→22.35/GSM35.17<GA36.39，非所有能力改善。hardware/precision/trainseq/generationdenoising预算/methodeval/seeds/CI/latency ND，‘negligible’无端到端time数字。2+1+2=5，拟仅报告有mask边界的局部DLM attention分支，不代替一般sink分析、denoising质量或零成本保证。

## 19675 LoPRo — root标准必要证据与限定Only通过

[v1](https://arxiv.org/html/2601.19675v1) §3.1–3.4/4.1/4.3–4.5/C、DOM S4.SS5必要Table5恢复文件：scaled lowrank分离后的residual按diagH/meanabsR排序，important前部identity，其余相近block Hadamard，输入按inverseperm/rotation再加lowrank；R1SVD迭代rank1、U/Vfp8/Σfp16。Eq13 effectivebit含group scale/lowrank/permutation等metadata，不混裸2bit。Table5 2.2bit OQ no/full/partial PPL8.4/9.49/7.39、accuracy53/51.5/57.8支持fullrotation破坏保护的局部边界；VQ6.53同时改quantizer，不独立归permutation。Theorem7无限制非增loss未读证明且不采用，实际量化非无条件error guarantee。

单A10040GB dense、A80080GB Mixtral，C4随机128seq×2048calibration、WT2 PPL Llama2context4096/Llama38192/四zeroshot lm-eval acc非accnorm。主scalarLoPRo Llama2-7B 2.17effectivebit PPL7.39劣GPTVQ2.13bit6.89，不全SOTA或同bit。量化LoPRo7B26.4min仍慢GPTQ25.2，Mixtral2h；inference GPTQModel W4A16 baseline、rank16/B1/16/64，7B93.3→83.7tok/s/总latency+10.3%，13B62.4→56.1/+10.1%，正文‘below10%’略超，非加速serving。input/outputlength/concurrency/SLO/seeds/CI ND，activation16bit不是KV压缩。2+1+2=5，拟仅报告具体partial residual rotation+低rank成本recipe，单负侧不改‘rotation与outlier保护需协同’的一般既有约束，不写所有矩阵/生产保证；未因HTML问题放弃必要反证。

## 19620 R³ — root标准必要证据与限定Only通过

[v1](https://arxiv.org/html/2601.19620v1) §3.2/Eq3/§4–5/Table2–3：SERR以top-p token entropy高且全trajectory entropy低的Pareto dominance count排序，线性赋Rmax reward给failed/truncated轨迹。排序反映exploration/stability代理而非正确性，tie break与全同排序情形未有明确处理，不能授一定恢复有益梯度。Replay用同query UID历史opposing rewards；Eq3 α乘全部mixed-group std，非逐off-policy样本独立权重或完整importance correction。ISR改prompt population；额外历史上下文、replay/entropy成本未量化。

DeepSeekR1DistillQwen1.5/7B、DeepScaleR约40K数学数据、Qwen2.5Math symbolic evaluator，正确输出额外长度reward、max32768；5bench每question16responses。Table3 w/oSERR AIME47.5→36.88可支持有限模块取舍，不能认证entropy为truth；Table2 JustRL AIME53.5>R³47.5、AMC82.2>77.3、Pass16亦局部胜负。基线训练预算/主hardware/precision/batch/trainsteps/seeds/temp/CI/端到端成本Not Disclosed；高entropy曲线或后期下降不是数学收敛证明。2+1+2=5，拟仅报告新proxy credit局部recipe，不改变正确性verifier职责或授全部zero-advantage可用信号。

## 19634 AC²-VLA — root标准必要证据与限定Only通过

[v1](https://arxiv.org/html/2601.19634v1) §3.2–3.4/Alg1/§4/Tables3–5：previous action、当前visual mean/max、instruction embedding、action-head step与cache cue进入router；cache key是quantized action-delta norm+vision hash，不是状态等价证明。Alg1先运行fvis再查cache，hit只免后续VLM，不免sensor/vision encoder。Token compaction保原RoPE position、layer active subbatch/scatter，dense-teacher action/features distill与budget/temporal penalties；有限接口增量可核而非三个成熟稀疏模块自动准入。

CogACT Prismatic7B+DiTBase、freeze vision/language只训router/actionhead8denoise不变；RTX5090 node、Bridge/OXE3000steps/AdamW/B48/lr1e-6/H15、pruning上限.6/cachethreshold.2。SIMPLER Google3Hz/513Hz sim/80steps、WidowX5Hz/500Hz/120steps；主dense74.8→76.8/1.79×/29.4%FLOPs有限实测，不保全面成功率。variant61.6<EfficientVLA63.2，DrawerApple46.8<dense50.9。Table4组件反侧完整；Table5一次只开一轴，其r.4为68.9/1.63×不同于联合76.8/1.79×，87.1 cacheonly亦不同配置；token.2下降33.3。本文没有action condition单独去除/匹配视觉router对照、hash碰撞/错hit压力评价、真实robot safety/latency尾部；GPU数量/precision/inferbatch/IOlength/seeds/episode分母/CI/timingscope ND。2+1+2=5，拟仅报告action/context-driven局部稀疏执行，未给通用cache正确性或闭环安全新contract，保留碰撞与旧state重用风险。

## 19672 ProToken — root标准必要证据与限定Only通过

[v1](https://arxiv.org/html/2601.19672v1) §4/Alg1–2/Eq3–10/§5.1–5.5：global-input绑定的client layer outputs点乘global token-logit gradient、跨selected late attention-out/MLP层和tokens累加、softmax归client。参数线性平均的preactivation分解不等整个非线性Transformer严格因果分解；Eq3–4带ρ，Eq7 score未显式ρ，当前等样本clients不覆盖不均权重比例忠实。算法实际需要逐client模型权重/层访问和global backward gradients，未rawdata不等DP、secure aggregation兼容或权限隐私证明，客户端更新本身敏感。

Gemma3 270M/SmolLM2 360M/Llama3.2 1B/Qwen2.5 .5B，4domain仅归因测试人口；6clients各2048/10rounds/all参与/1epoch/FedAvg，2H200+A100/2CPU1GPU每client/B32/AdamWlr5e-5/wd.001。!!!BadMagic!!!在clients0/1植固定refusal sentinel；主评价选5个已触发且生成sentinel输入，98.62%均值/40–100%范围非自然outputs因果source率或独立client唯一标签。gradient ablation另20触发输入逐层平均66.34vs35.71，不混同sequence98.62。5samples/round10成本Gemma1.10–1.42秒、最深1.87秒，非TTFT/逐token生产SLO。55clients各200coding/25malicious/10随机参与/15rounds，92/95.24%只须归任一指定恶意群成员，非细分25client贡献。precision/IOlength/concurrency/seeds/CI/DP预算/secureagg权限/真实天然provenance ND。2+1+2=5，拟仅报告受控activation-gradient→client接口，不改变provenance证书、因果归责或隐私保护通用contract；必要源足够，非扩大所有domain应用。

## 19747 RTL-AGENT — root标准必要证据及仅报告处置通过

[v1](https://arxiv.org/html/2601.19747v1) §3–5.1/Table2，PRIMARY_19747.md、PRIMARY_19747_SETUP.md、PRIMARY_19747_ABLATION.md：首个waveform divergence→read/write cone→仅suspect blocks patch→首次失败更晚或同首次失败更少mismatch才接受，确有局部执行/accept改动，不以成熟组件组合一概关闭。209任务/K≤10、GPT5.2组件组消融；返回functional test pass，不等全部形式正确或NL specification faithful。2+1+2=5，root实际准入、必要支持与关键反侧通过。

仅报告，不伪记已有覆盖：AGENT-REFLECTION Ch80 92–98已有局部repair/restart取舍、119–159已有diagnostics/affected-state gate与localize-attribute-repair；AGENT-WORKFLOW Ch81 60–85有event/preconditions runtime，但未实际承载RTL cone与(tf,m) gate细节。本次新增是可复用的RTL局部recipe，依waveform/dependency cone和给定tests；组消融不单独定位accept rule，self-generated contract/miter与functional pass未支撑一般代码因果或新正确性contract，因此不改通用知识链。此为具体长期不足理由，不以工作量或访问成本关闭；root已实际复核此处置通过。

## 19798 Youtu-VL — root标准必要原源与仅报告处置通过

[v1](https://arxiv.org/html/2601.19798v1) §2/3.3/5及A.1 RefCOCO/A.2评价。continuous SigLIP2 input与discrete visual-token target非对称，DINOv3 geometry/SigLIP2 semantics tokenizer K150K/D768，visual与text CE λ.5；dense输出从category token logits映回视觉位置，不额外task-specific decoder。Stage3 1.8T/Stage4 .6T多模态混合有数据变化；wo/VLUAS曲线仅限定recipe，不授普遍scaling ceiling因果。4B模型一般多模态MMMU61.1<Qwen3VL4B67.4、POPE86.4<89.3，depth/pose亦非所有专用模型最优。

RefCOCO实际draw box、crop padding1.2/shortside1280、DenseCRF；无extra head不等无postprocess或额外compute。A.2 hybrid exact/LLM judge身份ND、dynamic patches与selectiveCoT不等全基线匹配。主要hardware/precision/batch/concurrency/seed/latency在必要源Not Disclosed。2+1+2=5，拟仅报告：特定视觉target与dense读取recipe增加局部接口实例；模型规模/混合配方/后处理与任务评价未分离，尚无足以替换现有表示/生成factorization或通用资源判断的新条件，不写普遍视觉能力保证。

## 19827 Iterative RAG — root标准必要原源与仅报告处置通过

[v1](https://arxiv.org/html/2601.19827v1) §3.1–3.2/Table1/4.2/5.3。No Context、Gold Context含全部oracle hop paragraphs、Iterative最多5queries，mandatory首query top10、当前与两轮旧chunk、至多18chunks；1186 ChemKG 1–4hop、220words/50overlap、domain embedding、GPT5mini answer judge，领域仅作RAG评价人口，不采AI for Science应用。11model平均gold69.14±7.22 vsiter80.89±5.8是跨模型离散，不是seed CI。GPT4o输出10 vs448.63tokens，GPT5 713 vs5592；非reasoning模型static只final string，iter可partial answers/跨步state，预算与允许推理方式混杂。Mistral iter unique13.8%/net2.7%表明亦丢掉gold成功，非单调优势。

hop coverage/anchor/self-reported sufficiency不等事实充分性；difficulty由11model正误定义且分档未覆盖全部错误数，非通用难度真值。价格×tokens为估算，token CV非实际latency/SLO，hardware/precision/batch/concurrency/seed ND。2+1+2=5，拟仅报告：oracle静态证据不必是本协议upper bound的局部反证值得保留，但不能单独归因同步retrieval、不建立新通用context scheduling最优或科学有效性；不替换Books retrieval/state边界。

## 19834 Visual World Models — root标准必要原源与仅报告处置通过

[v1](https://arxiv.org/html/2601.19834v1) §3–5、8.1–8.3及9。BAGEL/Qwen2.5家族、7tasks，比较visual/verbal/implicit CoT，但multi-hop manipulation/ball tracking未设verbal world-model arm，不是每task全三路。paper folding/multi-view cube等视觉状态瓶颈有局部提升，maze/sokoban无益；MMSI overall34.8→38.4但Obj-Obj31.2→29.5/Obj-Reg29.1→25.8。四倍SFT sample efficiency不等FLOPs或端到端效率。只采经验瓶颈/非瓶颈反侧，不采KL分解/conditional-MI为普遍性能保证。

任务train/test分别2357/480、2000/480、2254/1024、8448/480、7715/480、2500/480、10661/522。SFT8GPU/RL64GPU型号/precision ND，SFT lr3e-5、CE:MSE1:10、warm200/seqperrank32K；RL B128/minib32/G16，visual KL.1/verbal0。fidelity评verbal符号matrix vsGemini3Pro visual shape-only，因RL format drift采用SFT fidelity与RL answer不同checkpoints；probe两层MLP 8:2/5×5maze不能证明因果使用。blur/corrupted detail/position failure仍存在。2+1+2=5，拟仅报告特定训练评价人口的视觉瓶颈边界，不能给一般任务预授visual rollout收益或human-like能力，不重写world-model闭环保证。

## 19847 AdaRAS — root标准必要原源与仅报告处置通过，gate实现范围子命题保留

[v1](https://arxiv.org/html/2601.19847v1) §3/4/Tables1–4、A.2/B/C.1。correct/wrong label trajectories的mean difference和polarity flip选择K50 neurons、每decoder步稀疏加α；不是因果neuron证明。§3.3 gate称用input prompt早期activations，训练failure predictor，不用test oracle correctness。C.1却称all token activations attentionpool/global reasoning state，Table9给256-ReLU-drop.3-linear1而未澄清pool/token范围；不授无需额外rollout、零训练或无探测成本，未定实现范围子命题隔离，不把它自行判为oracle。offline correctness labels与F-stat features、BCE/Adam1e-4/100epochs确需训练。

greedytemp0、Qwen3 1.7B/4B vs异family posttrained1.5B未匹配训练预算。AIME24/25 test23/22，7/8留RCN probe；AMC91/HumanEval149，非完整原test，全小样本无CI。AMC Probing73.63>Ada70.33、random steer34.78<base47.83、woadaptive56.52<full60.87是有限对照。主文α搜索.1–.3/分析峰.4不同范围。4A100+8RTX3090；precision/batch/maxlen/concurrency和probe/train/serving成本ND。2+1+2=5，拟仅报告white-box局部干预/风险gate经验，不改普遍可靠性contract；gate全部token到底prompt还是含reasoning未解决，不支持无extra pass收益。

## 19156 — 标准必要证据形成，独立复核待核

[v1](https://arxiv.org/html/2601.19156v1) §3.2–3.4、Theorems1–2/4、§5/F.1–F.2、H.4。非凸有下界、operator/nuclear smoothness、iid无偏有限Frobenius variance；以nuclear-norm stationarity比较NS/SVD/SGDM，不是所有accuracy比较。NS是Taylor-truncation pκ，不涵盖原实践ad-hoc(3.4445,-4.7750,2.0315)多项式；后者不满足tau单调收缩，H.4明确guarantee不适用。χq还依统一δ0=sup_tδt,0<1；不能只称与q有关、不管condition number或T依赖。κ/q增大提高近似也增加GEMM代价，walltime efficiency model非通用GPU保证。

主CifarNet2M/CIFAR10，50epochs/B512/5seeds mean±std、共同warmup+cosine，所有Muon额外weight-renormalization；正文数值例可支持受限q取舍不等整个实际optimizer无改实现。FineWeb附录仅标8RTX3090、124M/1.3B、10Mtokens，不凭较大模型标签授规模普适；precision主setup Not Disclosed，不另读其他应用实验。2+1+2=5，仅报告条件理论/有限近似分支；无Books默认差额，不把已有有限NS工程名当新知识缺口。

## 19221 — 标准必要证据形成，仅可采用设计可行性

[v1](https://arxiv.org/html/2601.19221v1) §3.1/3.2、§4.1–4.3/Table1/Fig3。单层多head RWKV state flatten→DiT-B/4 conditional noise学习；参数分支生成Wr/Wk/Wv再与static权重插值，联合LM CE与参数diffusion。当前condition实际仅取首tokenembedding，不能把抽象variable-length/global-context宣传当已验证整段全局信息。RWKV7 0.1B/Pile子集：state主要tSNE/persona与三条qualitative输出，自己的generated state错主题、interpolation案例未定量评分；参数分支只给下降loss，无matched static/hypernetwork任务对照。数据量、seed、hardware、precision、diffusion步数/端到端成本未披露。

2+1+2=5，机制可核但只报告proof-of-concept，不授稳定state editing/结构噪声已消除/适合生产/泛化收益；state合成与parameter合成是不同接口。标准必要支持与关键反侧足够，不读prompt全集或代码。独立复核待核。

## 19089 EPAS — 标准必要证据形成

[v1](https://arxiv.org/html/2601.19089v1) §2.1–2.2/Alg1、§3.1–3.4/Tables4–8：确定interval从深到浅扩大QK sharing区，V仍每层计算；训练后可重选compute/sharing区，不保证各模式原模型等价。Pretrain只4000steps/1Btokens，不至收敛，Table4所有final validation loss略退（7B2.99→3.04）。TinyLlama continual两组同data4Btokens/2000steps/8device/batch8accum16/seq2048；Table6 5/22sharing EPAS54.47仍低普通全compute56.70，无损宣传不采用。Table8 single/multiple block各任务互有胜负，不采用“consistently superior”或全depth共享定理。

V10032GB/910A32GB/910B64GB，实测训练和生成throughput绑定作者setup；生成batch/input/outputlength/precision与完整seed/CI Not Disclosed，FLOPs不换算生产SLO。2+1+2=5，仅报告局部渐进适应/可变compute配置与质量代价，无通用透明KV复用保证。CanadianAI2026只有conference名且无旧same-public信号，不扫会议批。必要日期/独立证据复核待核。

## 19026 — 必要机制与关键反侧已读，Books PRE 待独立核

[exact-v1](https://arxiv.org/html/2601.19026v1) §3–5/Table1、Appendix F.2–F.3/K。窄局部分布下缩小block可提高scale舍入误差的相对权重；UE4M3有限dynamic range还使scale下溢，UE5M3把未用sign位转为exponent位，最低非零scale从2^-9扩至2^-17。真实LLM权重与正常iid零均值模型是不同证据人口，不能授所有张量单调反退。Llama2没有所述inversion；Table1 Llama3.1的UE5M3与动态global-prescale UE4M3-S仅相近且有指标略差，均非BF16无损。4nm、八SIMD lane PE逻辑综合的0.5%面积与4ps仅作者设计，非现成GPU kernel或serving吞吐。

理论子命题保留：F.1定义s=xmax/m,m=6；F.3/Eq40却以xmax<smin/2作为zero-scale条件，缺m因子，与前述变量变换不一致。不采用精确概率/threshold公式；实测block inversion与scale-format分支可以独立限定采用。必要理论纠错以作者统一变量定义/修正Eq40重开，不遍历其他附录。评分对象2+1+2=5的有限格式边界；具体Ch49差额仍深入，不因已读工作量升分。现粒度段875–883只讲通常更贴分布、metadata和跨token一致，尚无scale有限range的小block倒增边界。

## 19061 — 安全反证必要深入已读，Books PRE 待核

[exact-v1](https://arxiv.org/html/2601.19061v1) §3/4.2.2、§5.1–5.3、§6。仅修改reasoning traces，保留原query和正确answer；目标任务不在训练集，不能由label正确推出trace完整性。Qwen2.5 1.5B–14B、主要s1K1000、code20K，通常1%污染/3epochs/4H100FSDP；100target及100non-target queries，匹配目标行为的binary评分与GPQA/MATH500/AIME24 utility分别计。LLM合并成本与随机性另计；不是已证明绕过所有检测。

小模型可同时掉utility；增加thinking budget效果非单调。清洁/混合continuedFT未清除14B该局部行为，3B Step-DPO两epoch把ASR60降51但数学utility也退，不能外推任何alignment必败。100poison/100clean检测中PPL与Gemini2.5Pro consistency人口与domain有限，高FPR仍可能漏，no universal detector certificate。3+1+2=6；安全信号强制深入。Ch27 reasoning likelihood263–267已分scorer与质量，但不含正确query/answer仍无法认证跨域reasoning trace完整性的具体差额。

## 19231 — 安全反证必要深入已读，Books PRE 待核

[exact-v1](https://arxiv.org/html/2601.19231v1) §3.1–3.2、§4.1–4.2/Fig4–7、Appendix A.3–4。1000Alpaca-GPT4 benign samples的refusal-prefix SFT与同数据/同hparams普通FT、randomprefix作对照；refusal prefix仍输出却跟随后续unsafe completion，prefix rate不是最终safety verdict。13open模型0.6B–70B，主要fullparam/4H200141GB，表7模型LR/epoch不同；商业3模型使用完整Alpaca且具体内部FT不披露，不能当1000fullparam同协议。AdvBench500、Sorry440、HExPHI330由LlamaGuard4/专用Mistral judge分别评，judge不是实际effect验证。

SQL与数学utility可退，data继续增加可导致质量坍塌，没有retainset或保证保utility；LoRA并非所测模型均能删除refusal。§3.3有局部Jacobian/Lipschitz与强prefix假设，只采用经验反证，不授所有alignment等于memorization或通用理论证明。3+1+2=6，安全约束强制深入。Ch72 604–606已有benign preference更新与distribution外safety审计，但未明确refusal prefix与实际completion可分离的SFT评价差额；先比较实际owner再决定写入。

## ODC — 2601.19362v1

Primary: https://arxiv.org/html/2601.19362v1 。已读 §2 FSDP barrier、§3 mechanism/implementation、§4 balance、§5.1–5.4 eval、§6.1–6.2直接限制。精确版 v1；不采用以后版本。Submitted Jan27 08:44:46UTC 为首次可能公开下界的输入，不是发布时间；TITLE_LEADS 的 DOIcreated Jan28 03:02附近为公开上界（精确值以TSV为准）。

- §2 Eq1：collective runtime按各层各microbatch最慢设备求和。§3将allgather拆为按需parameter shard gather、reducescatter拆为scatter-accumulate。State仍按FSDP分片且worker/server同设备，不宣称发明parameter server。
- §3.2 CUDAIPC(intranode)/NVSHMEM(internode) RDMA使target不主动参与，gradient累加用lightweightdaemon；orderedmessage sender/receiver不是其ondemand保证。§3.1/§6保留minibatchbarrier，同步优化，不是asyncSGD或boundedstaleness。
- §4 LB-Mini先分平衡总compute，再每设备按memorypackmicrobatch；避免单长sample memoryO(s) vs computeO(s²)的不可匹配条件。FSDP+LB-Micro与ODC+LB-Micro分离通信贡献，LB-Mini仅适用ODC。
- §5.1：SFT LongAlign/SWE-Smith，RL verl GRPO AIME；DeepSeekR1DistillQwen1.5–32B；最多32A10080GB，NVSwitch，RoCE800Gbps/node；RL最大14B/16GPU。RL明确只计training，排除rolloutforward。运行precision未在该核心setup披露：Not Disclosed，不补造。
- §5.2：SFT最高36%；RL最高10%，受verl每device相同sample数和较短tail限制。minibatch=1无增益；更多packing/更大batch让baseline改善而缩小差距。§5.3单因素控制与golden1.5B/LongAlignMax64K/minibatch4/8devices/ratio1支撑负载条件，而非普遍速度保证。
- §5.4/§6.1：multi-node ODC primitive bandwidth明显低NCCLcollective；放弃hierarchical拓扑优化是真代价。longcontext用computeoverlap隐藏，但shortmicrobatch需hybridsharding：param/gradient在node内，optimizer跨node，内存增加。Elasticity/faulttolerance/async为§6.2未来方向，不是已实现。
- 可采用：sharding state layout与synchronization granularity不是同一决定；同步优化可保留minibatch一致性而避免每层straggler累积。不能采用：所有workload36%、rollout端到端加速、透明容错/弹性、multi-node通信更快。
- Score首批root准入校准2+2+3=7；深入证据已形成，Books判断待目标现有论点与独立证据复核。未运行公开实现、未复现实验。

## SDFT — 2601.19897v1

Primary: https://arxiv.org/html/2601.19897v1 。已读§3方法/假设、§4.1设置、§4.2–4.4结论及小模型反例；§4.5成本/§4.6teacher设计对照待补读，尚不声称标准审阅完成。

- 同模型teacher读取demo，student不读取；student自己sampletrajectory上的reverseKL signal不同于复制expert离线轨迹。teacher默认EMA，不能写固定权重或另一个更大teacher。
- §3.2 ICLteacher需足够接近optimal behavior且保持与base接近；作者ToolAlpaca teacher100%和50人工trace只支持局部验证，不证明一般taskoptimality。
- §4.1 Qwen2.5-7B-Instruct，skill为ToolAlpaca/medical/scienceQA，knowledge为2025Wikipediadisaster corpus约200Ktokens生成QA；一般skills retention是6套基准平均；不引入AIforScience应用路线。
- baseline SFT/DFT/reinvoke，knowledge比较CPT/oracleRAG；各自hyperparametersweep选targetvalidation最好。§4.2 oracleRAG本身仍可高于SDFT，不能写distillation普遍替retrieval；pass@k≤128对照降低纯entropycollapse解释。
- §4.3只有3技能顺序实验与局部retention；§4.4 Qwen3B弱ICL让SDFT差于SFT，是关键反证。只能采用demonstration→onpolicyteacher的一条可行路径，非无遗忘保证。
- 首批原评分2+1+3=6通过准入；需要依据原增量而非成熟onpolicy原则修订Durability，第二批统一重评前保留原记录。Books及成本对照未完成。

## Axe — 2601.19092v1

Primary: https://arxiv.org/html/2601.19092v1 。已读§1增量、§2/§3布局定义与compiler核心片段；§4完整eval对照待补读，尚不声称深入审阅完成。

- namedaxes表示device/thread/memorybank，tiling/sharding/replication/offset同一physicalcoordinate空间。§2 set-valuedlayout处理replica，不把逻辑shape或byteaddress当全部layout。
- §3同一DSL既有threadlocalloop又有scope-relativecollective，tensor载shape/layout/scope/pointer/dtype；distributed signature有runtime consistency checks。统一语义不是所有schedule自动最优，也未证明训练端到端收益。
- 首批原评分2+2+3=7通过；需要实际§4B200、多GPU和异构backend比较后才收敛采用边界。Books owner拟INFER-TENSORRT-LLM，未读现有正文，不能凭主题给已有覆盖。


## 证据更新：上述待办的实际完成情况（2026-10-04）

### ODC

root 已独立读精确v1§3–5/§6负侧PRE通过；Ch39 Communication之后三段及末注已写，root实际完整204–242前后链路与384末注POST通过，并完成限定cached/unstaged diffcheck。Books：整合TRAIN-ZERO。DataCite created精确2026-01-28T03:01:27Z，与Submitted下界构成arXiv上线本窗区间[01:00:00Z,03:01:28Z)，不以registered或Updated赋firstpublic。

### SDFT

已实际补读§4.4–4.6及§5成本/限制，标准所需支持与反证足够。Qwen3B弱ICL反例；3技能序列retention不是无遗忘。§4.5 Olmo3-7BThink answer-only医疗实验用length作为reasoning保留proxy而非证明所有推理质量。§4.6同teacher离线SFT/offlineKL/onpolicy对照区分teacher质量与trajectory分布。§5约2.5倍FLOPs、4倍wallclock于SFT；相较GRPO单trajectory少组采样不是同协议通用成本优势。spurious“Based on text”prefix masking只是heuristic修补。知识适应仍不及oracleRAG；基模型ICL弱、特定skillsdegrade保留。拟新增机制demo-conditioned selfteacher+unconditioned studentonpolicyKL可支持2+1+2=5，不借成熟continual/onpolicy原则给Dur3。Books判断普通待办，未声称改书。

### Axe

已实际补读v1§4.1–4.3全部核心评价与§5近侧替代：DGXB200 CUDA13.0/driver580.82.07，1000warmup、3000repeat，FP16GEMMbatch8192模型weightshape；≥97%cuBLAS；Axe FP16kernel约250Pythonlines且手工指定warproles/sync/cluster，不是全部自动。FP8blockGEMM只有92–96%DeepGEMM，不能保证最快。Qwen3-30BA3B fusedFP16MoE相较FlashInfer1.20–1.36x，SGLang1.02–1.23x随tokenbatch配置。DGXB200 GEMM+ReduceScatter最高1.40x最佳baseline，对比cuBLAS+NCCL未融合且TritonDistributed的GEMMbackend质量不同，不能纯归因layout。Trainium1 trn1.2xlarge FP16squareGEMM匹配NKI，noncausalMHA最高1.44x/平均1.26x；不证明所有hardware或训练端到端收益。§5 CuTe同stride arithmetic但Axe namedaxes与R/O set-valued扩展；linear-layout power2限制可被另一表示放宽，Axe可互操作不普遍替代。完整必要深证据已形成，Books需读实际owner。DataCite精确恢复created2026-01-28T02:54:59.000Z；Registered02:55:00仅保原值不用于边界。

### 19400 Muon理论定点 — root必要公式实际复核通过，最终争议/暂缓

v1§2.1 Assumption2.1各样本L-smooth、有下界，独立无偏/有限variance stochasticgrad；Alg1 Step9 exact orthogonal projection，不把finiteNS列为已证明。§3.1 Theorem3.1/§3.2 Cor3.1给momentum、η与b联合bound，不需PL。O(1/T)需η~1/T且b~T²，或exponentialb，迭代速率不等于oracle budget效率；fixedη/fixedb只能到含η和1/sqrt(b)误差floor。原genericbroader主张收窄为这些具体假设/代价，拟2+1+2=5。标准理论必要假设与命题已核，不遍历proof；Books仅报告理论分支，不声称有限NS实际训练胜出。

**中心争议纠正（保留上方原待核判断）：** 实际继续核v1 Cor3.1(i) L195–201、Theorem3.1 L156–161及AppendixA(i) L405–409，D1=η^-1 C1+(1−β)^-1 C3，原上界首项为C1/(ηT)。若采用正文声称η=c/T，且初始optimality gap C1>0固定，该项为C1/c并不衰减；因此不能从此bound推出该配置O(1/T)，增大b不消除这项。固定η下隐藏常数随η变，不可在η随T变化后仍当常数。这里只指出原推导不足，不声称算法必不收敛或所有渐减LR结论错误。此中心速率争议需作者提供保留全部T-dependent常数的正确推导/勘误；在此以前隔离不作正面理论证据、不进入Books。已经读的必要原公式保留，未逐版本/全proof扩审。

### SDFT 实际 owner 比较

Ch29 Context Distillation §444–491实际已有：student on-policy同prefix，teacher额外privileged context，full-vocab reverse KL、teacher刷新持久状态、额外forward与回归。§515–521已有同base/ICL能力与失败、成本条件。SDFT只以demonstration/EMA实例化这一接口，实际采用命题已有覆盖TRAIN-SFT；3B失败、oracleRAG更好及2.5x FLOPs/4x walltime是本文局部证据，不另造章节diff。独立owner比较待root确认。

## 19001 FROST — 标准必要证据及理论子命题争议

精确v1 §3.3/Eq1、§4、§5、§6/Tables2–4、AppendixE/F1/J实际读；Softmax1=exp(z)/(1+sumexp(z))替attention normalization，LoRA CE在OpenR1训练，而非删除已生成句子的后处理。Table2同训练的Phi4比较支持局部activation干预质量/长度变化；Minerva Entmax15更好，注意力/entropy不是因果重要性证书。2×H10080GB、bf16、LoRA r8/α16、训练batch8/accum4/5000maxsteps、deployment batch256、temp.6/topp.9/max4096（TALE例外）；其他baseline沿各原论文hyperparams/训练数据，因此Table5不是统一准备预算。作者未披露完整重复/CI，variance≤2%不是置信区间。AppendixJ三学生判断错误移除8%会伤答案，但样本数不明。

理论Assumption5.1把σ1称映到总和1 simplex且shift-invariant，**与Eq1本身不一致**：有限z权重总和<1，加常数改变额外1相对分母；tail contraction也被假设，不由该公式证明。故不采用无损剪枝/推理保持定理或LoRA小即能力不变，理论子命题精确隔离待正确operator定义/推导。仅采用有限训练控制中的activation→质量/长度取舍；拟2+1+2=5，OnlyReport（局部替代与对照，不确定一般outlier因果/无损）。标准必要支持与反侧已读，不追无关heatmaps；root必要证据待核。

## 19055 User Edits — 标准完成

v1 §2–4/Assumptions1–3/Theorems1–3、§5/Tables1–2实际读。同(x,y,y′)可形成监督、preference或edit cost；用户编辑与两个独立reference samples分布不同。条件理论依knownβ balance equation、最优编辑非零概率、policy/cost可实现、finite类及concentrability；pessimistic cost RL一般计算不现实且**未实验**，不称所有真实user最优。SFT/DPO的取舍由编辑收敛程度与coverage分别限定；lateUCB会为探索付代价。

Llama3.1-8B学生、Qwen3-32B模拟user（test迁移70B），email10K/summary20K，online200、3seeds，greedy/max1000；weak只改部分偏好且test一直strong。所有方法重复200chars后截断，validation loss选hyperparams未必对齐在线效用。更少edit不是truth/safety。2+1+2=5；仅报告条件理论与模拟user局部验证，不从这组identity-specific assumptions补通用产品规则。标准必要证据足够，未复现，root待核。

## 19060 PixSearch — 标准完成

v1 §3.2/Eqs1–5、§4.2–4.3、§5.1–5.3/5.6、AppendixA实际读。生成search token→query modality/text或mask crop→API text info→继续生成。LLaVA/PLUM13B加内部mask decoder；GPT4.1每题5轨迹及pseudo-query labels，两阶段混合保护segmentation。Information lossmask仅去该位置CE，**不由Eq10证明所有通过context的梯度detached**，不采用原无gradient宣传。

同PixSearch控制CRAG Full acc37.7/hall40.7对Whole31.5/50.5、Text18.2对NoSearch19.8；truthfulness仍−3。1:9训练混合ADE mIoU9.85对PLUM55.08，7:9恢复55.98；搜索2–3call多收益，4后趋饱和。bf16、LoRA r8、训练1024²/maxtext512、batch6/accum10、20+6epochs；硬件与完整离线/API时延费用Not Disclosed。外部retrieval可信度/视觉mask失败仍存在，不保所有MM-RAG降幻觉。2+1+2=5；OnlyReport为具体联合训练接口与局部检索/segmentation取舍，未形成通用可靠性保证，root待核。

## 19062 Disempowerment — 标准完成

v1 §3.2/§4.1/4.4/4.5、§5、§6反侧与AppendixB.1实际读。采用命题仅**self-selected Claude Thumbs中**moderate/severe potential与positive approval并存，满意度不是autonomy proxy。不是把1.5M一般traffic当此相关性的样本；thumbs另563612，月stratified。Potential依authentic values潜在、transcript markers与Opus4.5分类，Haiku筛/Clio clusters；50conversations350分类human validation exact74.29%，不是精确危害率。

§5conversation级rating且没有turn-level counterfactual，provider/user selection/遗漏图片/模型分类错误，不证明因果或长期真实伤害。§6 360合成高风险prompts/BoN32/Sonnet4.5显示standardPM**未显著增减**此率，不能把approval相关性外推所有preference training鼓励disempowerment。bootstrap95%只表抽样不确定性，不消除这些混杂。2+1+2=5；OnlyReport保留观测人口及proxy反侧，未给通用系统安全contract。root必要证据待核，未复现实验。

## 当前结果同步（覆盖前文待核标签，不扩大已核证据）

root实际原源复核已通过19001、19055、19060、19062；19055因旧同稿首次公开身份仍日期隔离。19089 EPAS与19221 DREAMSTATE标准必要证据已由root实际核通过，均2+1+2=5仅报告；EPAS不采用未独立核Table8的单block普遍胜负。19026、19061、19231及Axe/ODC实际正文与邻接POST已通过，SDFT具体已有覆盖通过。以上不是整日完成。

## 19213 M²XFP — 必要标准审阅待独立核

精确v1 §4.2–4.4/§5/§6必要原源见PRIMARY_19213.md。EBW=(k·B_elem+B_meta+B_scale)/k将metadata算入预算；组32且共享scale的MSE控制只支持局部格式选择，fixed-scale ElemEM的top1~top2与adaptive-scale SgEM的bit分配分别成立。权重可offline adaptive，activation须在线选top1与确定tie/clamp；clamp不等无损（作者最大PPL差.02）。不能把metadata在线成本隐藏为纯4bit。

LLM评价W4A4/E8M0、组32/子组8等效4.5bit，Llama/OPT/Mistral/Falcon及R1Distill局部Wikitext/QA/推理；原NVFP4等效4.5bit，而额外加入本方法metadata的M²-NVFP4等效5bit，不能把这一扩展收益当同bit。Table2部分NV更好，Table3 OPT的BlockDialect PPL11.31优于M²XFP11.34。1.91×/1.75×来自DNNWeaver cycle simulation，Verilog/TSMC28nm/500MHz Design Compiler与CACTI7面积/能耗模型；不是GPU实测。32×32PE/324KBbuffer，额外PE面积4%与全芯片0.26%分母不同。quality-matched某些层upcast8bit，不能外推原生4bit端到端或生产SLO。seed/CI与实际GPU吞吐Not Disclosed。拟2+1+2=5，仅报告局部格式/在线硬件协同实例，不把一种尚未实测GPU的recipe升级通用执行保证。

## 19280 GDRO — root必要原源标准复核通过

精确v1 §3–5/§7及AppendixA；原源PRIMARY_19280.md和PRIMARY_19280_SETTINGS.md。Online pass@8分组/hysteresis，Prompt-GDRO在实际训练中重加权clipped advantage而非物理重采prompt；EMA与frequency debias控制intensive difficulty，但unnormalized权重也改变step scale。Rollout-GDRO离散arm、shadow μ、DP精确均rollout预算4，两个controller独立，没有联合最优证明。square-root variance proxy依iid有界正variance/连续放松；no-regret凸条件只解释surrogate，不保证LLM非凸收敛。

DAPO14.1K，Qwen3Base1.7/4/8B，无SFT/frozen ref；BF16/FA2，B256/val128、1000steps、AdamW1e-6、KL.001、clip.2/.28、advclip±5，训练G4验证G8、temp.6/topp.8/topk20。GPU/输入输出length/重复seed Not Disclosed。主表peak checkpoint与last pass@8不同，不合并；比较单独controller而非factorialjoint，外域/verification噪声未证。mean rollout预算不等walltime中性，driver advantage控制约.043秒基线/.355 Prompt/.446 Rollout额外成本；不可称免费compute或统一最优课程。拟2+1+2=5，仅报告明确在线分配接口与局部数据验证，不补通用RL保证。

## 19334 DeconIEP — root必要原源标准复核通过

精确v1 §4/§5/Table2–4，PRIMARY_19334.md。固定离散prompt，embedding加ζ·tanh(G)的有界干预，四层decoder generator以reference KL+CE训练；reference是same-architecture base/earlier checkpoint，**仅预期更少benchmark exposure**，不是真clean证书。理论KL bound只动机不保证算法，cosine接近1不证明semantic invariance或恢复原能力。

Mistral7B/Llama3-8B/Qwen同pretrained初始化，OpenOrca加exact/semantic/domain benchmark泄漏与clean OpenOrca匹配总样本数；aux400与test不重叠，ζ1e-3/LR1e-5/drop.2，leak频次1/3/5。Table2残余污染RC非零：Mistral TruthfulQA exact .246；Qwen semantic Shortcut Neuron .005优于ours .101，TED .369（非.005）；Llama MMLU exact .165。Table4大ζ可降低RC但BUD增，reference轻度污染0–30局部测试非真正无泄漏认证。硬件/precision/seed/训练时长Not Disclosed于必要主文，不宣称复现/清除训练记忆。2+1+2=5，仅报告评价干预人口改变与代价，不改通用去污染保证或书稿；root必要原源实际复核通过，曾纠正对照行归属错误。

## 19773 EviMed — root标准必要原源与仅报告处置通过

精确v1 §2–5、Limitations、AppendixA/D；PRIMARY_19773.md。采用机制为将完整信息推理与交互获取分开测量，atomic evidence disclosure可直接计ICR，不采用医疗应用/真实临床能力。五个各200案例，GPT5mini拆atom；patient每次最多2 facts，reporter未有测试结果直接Normal，二者history1/temp0减少漂移但改变任务人口。ICR计reference atom，不是必要信息唯一集合；缺severity/时间/依赖、alternative E与expert agreement。SR由LLM matching judge，身份未披露于必要评价说明，不当独立临床真值。

Table2静态强模型未必交互较好；Qwen高ICR/低SR反侧使相关性非因果充分性。16 turns上限，REFINE的verifier反馈可改善局部人口，Table3 Derm/GPTmini SR66低于SC66.5、MedQA68低于SC69.5，不能以更多coverage保证正确。Table4异构collector带额外调用而非等算力通用最优。AppendixD单A6000/vLLM/Qwen2.5-7B、五数据均值，每turn REFINE16.48×baseline，不是整个系统成本；dtype/B/input-output长度/seed/CI Not Disclosed。2+1+2=5，仅报告评价盲区及有限过程测量，旧验证/信息控制原则不借为Dur3。

## 19781 Phonological Tokenizer — root标准必要原源与仅报告处置通过

精确v1 §3/Eq1–2、§4.1–4.5/Tables1–4；PRIMARY_19781.md。WavLM21st-layer经differentiable k-means single-codebook joint ASR CTC/AED与speaker-conditioned HiFiGAN reconstruction，speaker encoder冻结，token入口不保vocoder。2000codes/50Hz/548.3bps、30hLibri centroid初始化+44hVCTK，背后pretrained大模型不能称从零仅44h训练；30epochs先冻结SSL/centroid后60epochs joint，α=.1。基线不同pretrain数据/码率，非全等资源。

ER51.7高于DiscreteWavLM41.7，SID29.5高于ASR-only20.6，ASR14.6/18.5劣于Discrete14.3/17.1，非零speaker泄漏/全面胜出。LJS-trained vocoder对TIMIT/Expresso OOD，后者WER12.6对WavLM12.2、SpkSim.724对.737反侧，UTMOS/Whisper proxy不是human MOS。speechLM Qwen2.5-.5B/LibriLight6000h四epoch，linguistic分数不及纯phonetic但UTMOS更好；α增加会让speaker回流和ASR变差，α1损SpkSim。GPU/precision/B/seqlength/seeds/latency Not Disclosed；不授严格disentanglement或runtime自由调属性。2+1+2=5，仅报告具体representation目标recipe及混合取舍。

## 19786 Accent DSRT — root标准必要原源与仅报告处置通过

精确v1 §3.1–3.3、§4–6/Table1；PRIMARY_19786.md。将resynthesis recoverability与ABX accessibility拆开，固定text不同speaker/同accent triplets，GenAID在train选100频词/lowest10% accentword组合后heldouttest；所谓model-free ABX仍依supervised AID选人口，只四seenaccent可够triplets，非所有accent有效。HuBERT/HuBERTft/Whisper English-only24layer，RepCodec Libri100/200Ksteps；VCTK13手分region/test50/训练45四region，HiFiGAN100Ksteps，crossaccent源46人与target四SouthernEnglish，控制target但不是所有声线/口音。

§5.1 accent recoverability L6/9而accessibility L12；§5.3缩codebook32–2048同时损accent/phonetic/speaker，不是解耦certificate；ASR监督与layer选择较码率更重要只是所测英语表示。AID/SVcosine和PPG/WhisperWER相互有accent混杂，非人听音真值。Table1 proposed content L18/HuBERTft256codes对Vevo32，content-accent HuBERTL9/8192对L18/8192，模型/layer/codebook共同变不能归因单一。硬件/precision/B/seqlength/seeds/latency Not Disclosed，§6不覆盖multilingual/moreSSL。2+1+2=5，仅报告受控token评价反侧，不授通用disentangle/真实accent保证。

## 19320 StableQAT — root标准必要原源与仅报告处置通过

精确v1 §3/Eq4–5/§3.2、§4.1–4.3、§5/Tables2–3/Figs5–8，原源PRIMARY_19320.md。硬forward保留，backward用rotated damped Fourier surrogate，M=0/A=.21，A=0退STE，需避ill-conditioned amplitude；它是surrogate不是hard round真实导数，L2 rotated-function逼近和uniform-clipping-range variance结论不自动证明LM非凸收敛。higher M仅有限改善并增加数值复杂度，不采用论文所有全局稳定宣传。

Llama3.2-1B/3B weight-only 2–4bit，SlimPajama/FineWebEdu1:1，按行匹配10/20/30B tokens与LR的ParetoQ/DSQ作者复现对照；八lm-eval任务，Table3 3B/4bit67.15低于FP16 68.46，且3B/2bit63.05低于DSQ63.78，正文“均胜/超过FP16”不能照录。未量化同token FP16续训故不能把高于原base归因无损量化。B4/seq128/20repeats的latency/memory是backward microbench，不是end-to-end serving；GPU/dtype/主训练B/seqlength/确切seed数与CI Not Disclosed。Figure6混seed+LR dispersion非固定协议CI。2+1+2=5，仅报告surrogate局部替代和质量/预算边界，不授普遍无损/免费训练或生产kernel性能。

## 19402 PROTEUS — root标准必要原源与仅报告处置通过

精确v1 §2.2–2.3/§3–4/Table1–4/§5，PRIMARY_19402.md。runtime τ直接condition Beta μ，训练batch accuracy反馈dual λ、learned γ∈[2,8]非线性cost；推理λ固定1，不进行在线正确性dual更新。需要per-query/per-model correctness训练标签；不是免监督/硬SLA。router DeBERTa22M/MLP256，单A10010Ksteps约4h，§2说B32而§3实现B64不合，保留配置争议不补造；dtype/输入输出length/concurrency Not Disclosed。

RouterBench405K11model 70/15/15与SPROUT45K14model officialsplit，accuracy evaluator不同不合并。静态τ范围RB.85–.91/SP.85–.95 test floor100%，±2% matching仅44%/11%；动态4scenario各1000queries/5seeds floor77%与82–86%，不是always-meet。cost旧benchmark labels/估算$/1K而非实时API定价；DeBERTa“<2ms”与Table3单query8.7ms/batch8 2.9ms不同，吞吐用1000/p50，不能外推batch总throughput或LLM端到端尾时延。λ消融精度−.27/−.53且cost−8/−25%，γ只SP有益，标注成本/持续drift需更新/latency目标未来工作。2+1+2=5，仅报告单policy目标接口与有限统计target matching，未形成生产约束保证。

## 19605 Decompose-and-Formalise — root标准必要原源与仅报告处置通过

精确v1 §3.2–3.4/§4–5/Limitations、AppendixA/C/D/E/F，PRIMARY_19605.md。entailment tree bottom-up、各atom autoformalize Φ，Isabelle失败diagnostic只改implicated explanation再重构，已证subroot升为parent support；θ entity/event/role模板与robertaMNLI.9筛选不认证NL逻辑等价。Alg1局部递归无形式终止/最小repair保证；formal certificate仅由Φ与axioms构造支撑，prover-valid可NL意图错误。

refinement人口FOLIO122过滤错误/unknown、ProofWriter150 boolean D5/PrOntoQA150 fivehop/EntailmentBank150；逻辑reasoning另FOLIO182、PW225三类、Pr200，不混verified-rate与end-task accuracy。GPT4o/GPT5nano/Grok4fast nonthinking temp0、DeepSeekV3.1terminus/Qwen3maxpreview thinking不限effort，5backbone均值不是seedCI。Table2 full LT2.88iterations对FR3.51/ER4.02、去atomic3.31；θ ablation只GPT4o/Qwen两者。faithfulness通过逻辑→ruleNL cosine .893非semantic真值，depth alignment本身也不排任意新增axiom/commonsense缺失。API repeatedLLM/prover成本、timeout/结构错误可能全局重构，硬件/precision/tokenlimit/总预算/seed/完整latency数 Not Disclosed于必要证据；AppendixF只有图没有可提取数值，不编造cost saving。2+1+2=5，仅报告局部proof-repair接口及限定人口，不升级NL忠实保证。

## 19487 LLM-VA — root必要原源安全深入复核通过

精确v1 §3–5/§7及AppendixD/E/G，PRIMARY_19487.md。SVM从标注benign/toxic与answer/refusal方向、选cosalignment×classifieraccuracy，以minimum-Frobenius rank-one权重更新匹配向量；迭代重取方向，T≤30择val最好，并非无需label/训练成本。origin无bias是经验局部假设，向量相似不是安全causality证书。

12个3–15B instruction模型/5family，每模型每数据集选择500原始失败样本8:1:1（test50），ASR/ORR/F1依Qwen3GuardGen8B，不是自然traffic发生率或独立安全验证。2A10080GB、temp0/seed42单次；baseline沿原hyperparams或同family转移，precision/batch/input-output长度/latency Not Disclosed。主表8/12最好非全胜：Phi4-4B SEvalAttack ASR60→70。平均utility保持95.92%掩盖GSM8K约91.6%；过多层/迭代会降utility且小Phi/Qwen需要调参。AppendixE同judge参与方向筛选与评价，换双judge可ORR100，标准依赖不是truth认证；AppendixG未见任务Llama ASR .58→7.69、Gemma F1 .4059→.3809，保留反侧。无adaptive threat/CoT长推理/CI、多seed或生产保护证明。拟2+1+2=5，安全相关故深入受影响内容；仅报告局部weight intervention，不把binary latent recipe授通用安全契约。
