# 第三批五项：命题匹配必要证据及实际owner差额

准入已root独立校准。作者实际读取以下精确v1必要方法、关键对照和直接反侧；block号不是文件行。未核代码或复现。本批root必要原源/实际owner及4处正文、完整邻接、ownnote POST均通过：21454 Ch22 body487/475–499/own1316；21461 Ch24 body947/932–954/own2121；21472 Ch28 body682/670–696/own1787（经纠正每设备batch利用率与增加nodes通信代价的区别）；21477 Ch76 body189/180–210/own1557（83–91证明各scope各coarse+portals和staticcluster agent-specific fine IDs）；21467 Ch25 actual857–872具体Existing通过，未改书。4整合/1已有覆盖终态，窄锁释放；以下保留原源与原PRE提案，不表示仍待写。原文外围公式/协议错误仅隔离相应命题，不吞掉有效经验。

## 21454 When Learning Hurts: Fixed-Pole RNN for Real-Time Online Training — 2+1+3=6；具体理论边界深入

[v1](https://arxiv.org/html/2602.21454v1) §§II–IV，blocks13–126。线性零初态SISO，K个互异非零pole与非零gain的指数和；无噪声h前N≥2K项可以恢复unordered参数（32–73），已知输入x[0]≠0时有限卷积的下三角可逆再恢复h。不是有限 noisy online数据/未知初态的一般可辨识保证。K≥2时pole置换有多个零loss有序参数点，中间组合不是原系统，故ordered参数目标非凸（74–85）；K=1不存在非恒等置换，不抄无条件K≥1措辞。

决定命题在98–109：K=2、两gain固定1、c,d∈(0,1)、无限impulse-response平方误差，其最优Hessian是导数序列u_c[n]=(n+1)c^n与u_d的Gram；c≠d时PD但c→d条件数无界，且不需要靠近unit circle。111–120以PSD全Hessian主子块的Rayleigh边界扩展下界。这把forward稳定与训练可辨识/曲率分开，不采“所有RNN不可训练”。122–126的wireless32neurons局部比较只作背景：κ(Wrec)不是κ(loss Hessian)，硬件、数据噪声、seed、训练预算未充分披露，不能用梯度plateau强证普遍fixed-pole胜出。固定dynamics只训练readout仍付表达能力/预设basis代价。

MODEL-LONG-CONTEXT Ch22 actual475–493完整SSM分支已拥有固定卷积/输入相关transition、时变有界性非梯度证书，却未具体说明“稳定pole彼此接近仍可使学习曲率病态”的独立边界。拟在SSM固定transition说明后加一窄段：forward稳定不是learnable-pole好优化，有限线性识别条件与pole collision；数据/online预算受限可固定basis只学readout，不能当foundation模型替代或通用收敛。邻Ch21小结917–925、Ch23开篇1–28实际读；只请求Ch22局部一段+ownnote。

## 21461 VecGlypher — 2+1+2=5；坐标serialization的具体表示差额深入

[v1](https://arxiv.org/html/2602.21461v1) blocks43–69/72/75–96/110–113。SVG单path的原生d命令直接tokenize；UPM1000、baseline对齐、坐标0.1舍入，无新vector tokenizer。absolute/relative命令表达同geometry却改变学习序列；4B相对坐标R-ACC73.96高于绝对66.66，但Chamfer4.29差于3.75；27B绝对R-ACC94.91/CD1.98反而优于相对92.81/2.31（Table6/7 block95–96）。两个Gate不能以一个OCR分数代替。R-ACC是Qwen3VL OCR生成/GT比值，可超过100，不是绝对准确率。CD200点归一到[-1,1]不保证closure/topology。

Google-only与Envato→Google两阶段包含额外数据/epoch，不归因唯一staging；4B8A100 B32、27/70B32A100 B128、LR1e−5按GPU√放缩，不由70B更好宣“30B必需门槛”。仅Latin62chars/cross-font OOD，非开放SVG程序、复杂fill/stroke或普遍视觉生成。生成/白盒模型、数据清洗、额外阶段与typed解析成本均保留。

MULTIMODAL-GENERATIVE-PARADIGMS Ch24 actual920–950 typed统一生成已有parser/schema、coordinate frame/quantization与正确性分权，但未承载“同geometry的absolute/relative输出字符串也会随model容量改变辨认/geometry取舍，parse合法≠两个质量Gate”的serialization选择。拟该段后单窄段，不写字体专节/规模定律；明示配套data/codec与matched训练、任务geometry检查，简单schema或专用head仍回退。Ch23/25相邻开篇已读。请root裁具体差额是否已有，不因新名强写。

## 21467 Geometric Priors for Generalizable World Models via Vector Symbolic Architectures — 2+1+3=6

[v1](https://arxiv.org/html/2602.21467v1) blocks20–79与119–133。FHRR unit-phase状态/动作以逐元素complex乘法bind，inverse用conjugate、composition phase相加；binding/inverse/orthogonal losses约束latent。它只能直接承载相应commutative action algebra，不自动表示nonabelian group。每2step nearest-state cleanup使用全部已知state codebook，不是新增environment observation；MLP也同频cleanup对照。

10×10 no-wrapGrid400transition holdout20%state/action pairs，非新state/action：500epoch单步all96.3/heldout87.5对MLP80/0；100step不cleanup1.8，cleanup38.6，不能说漂移消失。FHRRdim512 vsMLPstate64/action16、LR.007 vs.0005不matched容量/recipe；3060TiFHRR.1528ms/cleanup.2421比MLP-S.1174/.1743更慢，seed Not Disclosed。no-wrap边界不可逆，与group-action理论假设不符；只保受限learned结构/cleanup路径，不采全环境等变/一般长rollout保证。

拟已有覆盖：MULTIMODAL-WORLD-MODELS Ch25 actual864–868已具体拥有identity/inverse/composition probes、group-action/可辨识state假设、latent等式不认证环境正确，以及真实rollout回退；实际412附近group-recurrent coordinate假设亦承载作用代数条件。本研究binding替代只提供上述既有论点的有界验证，未控制容量/recipe且实验不满足完整group环境，不加phase专节。拟Existing而非把理论外围问题整项Disputed；root请核实际864–868具体匹配。

## 21472 The Design Space of Tri-Modal Masked Diffusion Models — 2+2+2=6

[v1](https://arxiv.org/html/2602.21472v1) blocks73–101/193–200，仅logical/physical batch命题。CompleteP与SDE AdamW reparameterization为借用基础；κ=(Dbase/D)^γ(B/Bbase)，lr√κ、β^κ、ε/√κ共同改变更新时间尺度。原79把D误写model size，实际81/96和量纲明确token horizon，不搬该错误。~3000pilot320M(其中240Membed)、13Btokens、baseB256；cosine+1kwarmup≤总steps25%、固定width/depth128。physicalB≤Bcrit时可近似对应virtualB及virtualsteps，D=L*Btilde*Stilde；超过critical会离散化失效，而不是batch任意放大不损失。

88/90文字的B/S及临界方向相互矛盾，采用82图caption与90 Bcrit=D/(L*Scrit)一致的B≤Bcrit即S≥Scrit；不采字面错误方向。γ≈.44只是作者该schedule/data/形状的fit，101明确schedule改变可移动最优γ。193–197节点/每GPUbatch对照说明并行wallclock与FLOP利用不同：小batch GPU闲置，更多nodes通信sublinear；“doubling约half”不授任意集群SLO。这里loss为exp(ELBO)，不认证实际生成quality；tokenizer费用排除在训练FLOP外，硬件精度未充分披露，不采用总体3Bheadline。

TRAIN-PRETRAINING Ch28 actual659–686已拥有global/micro/accumulation与固定tokens下steps/gradientnoise，722–726已强调相同ELR不是完整optimizer状态。实际差额是“硬件physical batch和更新过程virtual batch可经lr/β/ε联合reparameterization分开，但只在经目标loss校准的critical区间”，不是简单accumulation。拟在batch段一窄段：配套更新状态/时间尺度、crit/schedule重新校准、噪声/通信相反压力、普通固定recipe回退；不复制γ定律或错误方向。Ch27/29相关交接此前实际读。

## 21477 Pancake: A Hierarchical Memory System for Multi-Agent LLM Serving — 2+2+3=7

[v1](https://arxiv.org/html/2602.21477v1) blocks33–61/63–101/104–141。近时L0/cache-patternL1/persistentL2只是背景。采用具体差额：共享coarse HNSW cluster portals跨static corpus/agent data导航，agent-private fine profile只记录hotvector IDs而不复制payload；scope不是ACL。distance<α*recent-agent-average可earlyreturn但非recall证书，backgroundfullsearch有真费用。Eq88的efconnect=min(...,1)再1/efconnect作概率可能>1，不采用该概率公式/拓扑证明；不影响已测有限共享导航方案。

GPUhotclusters、CPUinsert buffer(128阈值)、query合并两处新旧candidate；异步新cluster allocate/copy完再switch，shared/exclusive locks与替换增加双驻留、split spike/metadata、失效管理成本，原文未证明完整publication/reader life/crash一致性。不授零freshness损失/完全linearizable。EPYC9534/8H10080GB、MSMARCO8M E5dim1024、agent5datasets，single ANN B8以recall/latency比较；shared coarse→profile局部消融减11.6%再21.8%vectorcomparisons，端到端1.12–26.18x混框架/LLMruntime不matched，不当通用吞吐。5–15GBplateau只当前trace，weight/KV共驻会改变预算；split延迟尖峰是直接反侧。

AGENT-RAG Ch76 actual183–199已有可信ACL/kernel admission与RBAC物理分区，207–231及1031–1045已有图导航/向量分离和并发revision发布；但尚未具体承载“跨agent共享coarse导航、private fine IDs不重复payload、scope≠authority”的分层索引复用差额。拟183前或tenantfilter后单窄段，在scope/ACL邻接解释该替代分支及heuristicearlyexit、CPUbuffer/GPU旧cluster合并、copy/switch与双驻留/分裂费用；不重写publication协议或把distance阈值称qualitycertificate。邻Ch75总结628–660与Ch77开篇1–45实际读；请求Ch76一窄段+ownnote，由root裁placement。
