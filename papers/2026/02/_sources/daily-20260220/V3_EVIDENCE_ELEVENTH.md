# 02/20 第十一有限必要包：16570 / 16587 / 16596 / 16601

只保作者实际读过的精确v1支持、关键反侧与actual owner差额。当前官方事件页完整题摘/Comments/history已实际核；16570 v1、16587 current v3、16596/16601 current v2。无明确撤回/纠错声明；后来标题/三benchmark/blackbox新增内容不回填v1，也不因版本号遍历全部历史。root四项必要PRE通过，16570实际正文/完整邻接/自身末注POST通过，锁释放；16587仅报告、16596/16601中心争议隔离通过，不授整日。位置统一 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`。

| ID | v1 Submitted UTC | 同ID DOI Registered UTC | 北京公开范围（官方bridge推定，含起不含止） |
| --- | --- | --- | --- |
| 16570 | 2026-02-18T16:11:17Z | 2026-02-19T02:49:33Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:49:34+08:00 |
| 16587 | 2026-02-18T16:38:21Z | 2026-02-19T02:49:57Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:49:58+08:00 |
| 16596 | 2026-02-18T16:51:13Z | 2026-02-19T02:50:10Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:50:11+08:00 |
| 16601 | 2026-02-18T16:56:36Z | 2026-02-19T02:50:17Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:50:18+08:00 |

Registered为arXiv公开事件上界推定，不是DataCite字段本身定义正文公开；沿首包两官方桥接/1秒精度。Created仅原JSON，未采用。16601 current Comments Accepted ICML2026不搬首公开；16587 v1的2009 conference/placeholder DOI模板不是实际早出版事件。

## [Steering diffusion models with quadratic rewards: a fine-grained analysis](https://arxiv.org/html/2602.16570v1)

2+1+2=5，必要理论条件/差额深入。核心§2/3（100–136）：目标是 `p exp(r)`，bounded support、全x/σ精确base score oracle；linear tilt通过平移score query加已知向量，而非只在当前x加reward gradient。精确score误差仍open，W2结论非任意TV/真实生成quality。§5 Th5.2/Alg2（194–244）PSD `A=.5LᵀL`、rank r=O(1)、bounded C/‖L‖/D时，Hubbard–Stratonovich将目标写成linear-tilt mixture；潜变量z的权重含 `Z(z) exp(-‖z‖²/2)`，不是直接抽Gaussian z。grid与telescoping Monte Carlo估normalizer（223、247–262）支付约exp(r)规模/多次oracle求值，条件tractable不等生产便宜。

直接反侧§4 Th4.1及caveat（155–168）、§6（337–339）：rank1 NSD reduction用 `−(d+5)wwᵀ` 可有指数大entries；只排除poly(d,C)且不依‖A‖的通用算法，不排除poly‖A‖，因此不能写“负号/低rank自动难”或将复杂度结论迁learned score。理论材料无benchmark，model/hardware/precision/SLO不适用，未核实现/复现。

actual `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24:260–262已有h回归/MC终点引导及rare-event/误差权限；1088–1090已有离散粒子tilt目标/预算。尚未承载**连续quadratic reward的sign、rank和entry scale决定是否能借linear query-shift构造目标，而低rank不是统一可行性证明**。拟在h/MC接口后最多一自然段，保精确oracle/有界support、normalizer/grid费用、NSD规模caveat及原保守guidance共存；不展开另一个理论小节。

## [Why Thinking Hurts? Diagnosing and Rectifying the Reasoning Shift in Foundation Recommender Models](https://arxiv.org/html/2602.16587v1)

2+1+2=5，拟标准完成/仅报告。v1 §3.1–3.2（107–142）CPMI只是fullposterior与CoT-conditioned prior的代数分解，PCA/attention SDI不是causal identification；think-off已经高SDI，thinking下length/attention分母改变不证明独立General Subspace机制。§4.1（148–172）另一个instruction LLM将raw CoT压成单句preference模板，不是实际正交subspace projection或可强制保证。§4.2（330–362）expert(history+compressed)、amateur(null history+raw CoT)、baseline(history-only)，候选集内各自Z-score再线性差分；Eq8没有正部clip，amateur低于baseline时也能增加分数，不能照录“只删除无根据excess”的保证。raw CoT本由history生成，null history评分也不表示CoT不含用户信息。

关键control §5.1–5.2（367–381）v1仅Ad/Product各1000固定seed、Qwen1.7B/8B、SID beam32；think-on先采chain再decode。Table2（173–323）是off/on/Ours组合对照，没有compression×contrastive独立控制或匹配全部calls/token预算；p<.05未披露采用位置独立重复，hardware/precision/总walltime Not Disclosed。只支持此SID输出接口下free-form CoT非单调收益与组合rerank的作者局部经验，不采current v3“三benchmark”或文字因果根因。

actual `MODEL-SAMPLING` Ch20:238–275已单轨迹预算、更多token非普遍quality、phase≠内部状态和干预的version/proxy边界。SID任务的负例有实际准入价值，但v1中心“subspace alignment/选择性移除无根据bias”没有被上述控制成立；成熟压缩+linear scoring的局部组合结果不自动构成长期开新机制。拟仅报告具体输出接口负例与局部方法，非宣称整套三context算法已被现Books完全覆盖；不因缺SID配方强写书。

## [Sequential Membership Inference Attacks](https://arxiv.org/html/2602.16596v1)

2+2+2=6，隐私claim反侧深入。§2/3.1（105–114、182–208）控制canary insertion τ，stationary Gaussian empirical-mean模型中已知τ的LR只依插入前后两统计；unknownτ的uniform-mixture/max GLR不是同一个knownτ最优测试。§4.1–4.2（273–307）SGD接口用θτ−1下reference gradient mean/cov与target gradient/两checkpoint增量；Gaussian batch近似、reference人口/clip/noise须一致，不普遍每种optimizer或blackbox。§5.2/6（333–342）whitebox完整参数轨迹、knownτ、b64/T10/δ1e-4，最高Mahalanobis canary，logistic F-MNIST/frozenVGG最后层CIFAR/128-FC Purchase100；loss baselines未知τ不匹配全部观察权。原v1把blackbox扩展列future，不采current v2已实现的摘要。

必要中心反证§5.1（321–330）和直接AppG（899–907）：置信半径反复写 `sqrt(log(ξ/4)/(2N))`，在有效failure probability 0<ξ<1 下无实数值；AppG DKW公式同样如此，不是抽取漏掉负号。无法由其写法授Lemma5.1 high-prob ε lowerbound，更不能照录Figure3为已认证tighter privacy budget。作者统计角色/参数权限仍可仅报告，未核实现是否另有正确半径；不擅改原式后当作者已证明。

actual `PLATFORM-SECURITY` Ch72:393–421已privacy unit/发布对象、runtime canary/accounting与checkpoint共享轨迹非独立；尚未具体承载known-insertion下前后transition的membership sensor，局部mechanism可独立存在。不过本包拟**暂缓中心高置信审计保证，有限攻击方法/作者结果仅报告**，不把无效confidence桥接写入Books；重开只需同版勘误/正确uniform-CDF界与实际采用实现/协议，不要求无关全附录或新LLM实验。

## [Error Propagation and Model Collapse in Diffusion Models: A Theoretical Study](https://arxiv.org/html/2602.16601v1)

2+1+2=5，具体theory/counter深入。§1/2（103–137、170–214）fresh α混上代generated q_i再训练score，学习目标不是原pdata；continuous OU、t0截断，初始化Gaussian误差/离散求解误差未量化。§3（219–319）path RN density投影terminal可抵消，η是conditional martingale variance/pathenergy比；A1finite energy/A2true martingale、A3uniform higher density moment/A4normalized quadratic-variation moment、smallerror和ηpositive是不同条件，state-dependent神经误差“expect positive”不等独立证明。路径error非零本身不推出terminal mismatch，η下界/perturbative门槛不能抹去。

§4.1（323–334）中心persistent claim写非summable scoreenergy推出D_i“cannot converge to0”。定点必要F.1/F.2（1080–1104、1125–1162）actual proof仅得到ΣD_i=∞；F.4 line1135更弱写“cannot converge to0 AND be summable”。非summable正序列仍可趋零（如1/i），因此正文不能由此桥接到不趋零；证明丢掉D_n后给下界也需谨慎。uniform positive scoreerror floor是更强前提，不与非summable混同。另Th4.2（339–362）依A5tail及summable误差，式23加C_bias；不采简单fresh比例充分或所有递归pipeline collapse保证。当前v2无纠错说明，不为版本号展开全文。

actual `TRAIN-DATA` Ch27:368–398已有corpus/parameter recursion、finite anchor与fresh sample区别及条件几何/每代增长，未承载diffusion路径误差到terminal的observability。不过拟**暂缓中心累计误差不趋零/完整discounted保证，局部η框架仅报告**；保持关键反证，不以少一个diffusion配方造可采理论保证。重开正文/附录结论一致化、正确累计界条件及必要证明；无需所有image附件。理论采用不依经验数值，未核图示全部配置不授positive验证、LLM迁移或生产。无Books写入。
