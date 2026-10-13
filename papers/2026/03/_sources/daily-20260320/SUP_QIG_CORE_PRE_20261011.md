# QIG17809：token校准接口与有限PRE

fresh03-20补03-19，resume_mar17，5分2+1+2不变，AB/date/CVF身份独核§3有效复用。只必要[exact-v1](https://arxiv.org/html/2603.17809v1)§3–4/Eq1–7/T1–6、A completeness和B objective/format实际核；不读repo/全附录图，返回C/D不作为全已审或需遍历队列。拟采用token误差代理与scale-search的接口，支持/直接反侧够证即停，不授通用质量/完整公式实现。

## 必要原证与未采用命题

§3.1 Eq1既有CWE，activation按channel inverse scaling、weight正scale；Eq3沿xq→x路径对FP与quantweight的block-output差积分，IQR剪裁/归一得到token权重，Eq6/7只重加权原CWE误差而非运行时改token bit。WA baseline量化input；WO激活仍浮点，采用zero baseline。B L358–362实际scalar目标是每outputtoken跨channel的meanabsgap，32积分步，不是未聚合向量。该每outputtoken目标对哪些inputtoken梯度聚合、对角或跨token消费仍未充分说明；不补造代码已核。

A Eq14严格completeness是G(x)−G(xq)，只有baselineG(xq)=0才等总quantgap；有baseline贡献不能由完备性授因果真值，clipping后也不保原恒等。Signed IG即使scalargap非负也可负，Eq5分母可能抵消/为零；IQR剪裁与sum=1不保证所有lambda非负，带负lambda的GPTQ XᵀΛX不自动PSD。Table4/§4.3又写g(x)=f(x)−f(xq)，若xq固定其导数等f'(x)，不同于Eq3的quantmodel差/实际B abs目标。保这三层口径，不把T4当精确Eq3的因果消融。当前有限PRE不采用signed精确归一recipe/PSD或全部敏感性保证；若要执行，请一次精确请求scalar/跨token聚合、nonnegative/zero-sumguard与真实paired ablation trace，勿扩全repo。

评价：A80080GB、128 ShareGPT4V改COCO imagecaption，targetchat格式；LLaVAonevision7B/Qwen2VL7B/InternVL2 8/26B，W3A16 asymmetricgroup128与W4A8 pertokensymmetricactivation/perchannelweight，LMMsEval。T1固定条件只换proxy/granularity：SFTgradient token55.78/55.65低modality57.36，不能由更细自动更好。T2 LLaVAW4A8 ChartQA74.52<MBQ74.92、Science94.25<94.70；QwenW3A16 Chart77.76<MBQ79.18等反側，不采“每benchmark最佳/次佳”。T3 Intern26B W3A16 MMMU50.89<MBQ51.67；T5 LLaVA AI2D76.65<76.81，不采一致收益。T6计calibration/activationcollection/scale-search GPUh，0.55→.58与.95→.99非零开销，未给实际inferencekernel/端到端latency/并发/长度合同，不把negligible latency当已测。重复/seed、全部超参搜索与公开代码复现未核；baseline/模型/全費限定，未采W8A8lossless宣称。

## actualowner差额

Ch49 `INFER-TENSORRT-LLM`实际930–1067、1300–1353已顺读。961静态/动态calibration一般接口，963样本选择是poolcoverage；978 probe与983 channelcoverage、1314后二阶梯度已有统计目标/最终质量分账，但没有按FP–quantblockgap的路径积分生成跨模态token权重再消费CWEscale-search这条具体分支，故不假NC。Ch48必要交接/Ch50开头及Ch23 1–76已实际顺读：Ch23拥有modalityrepresentation，量化proxy/scale/产物仍soleCh49。不新node；拟961后、代表性pool选择前两短段，未授Books锁。

## 逐字PRE（待非准备者）

同一模态内部的 token 也不必共享相同校准权重。一个受限分支沿参考 activation 到当前 activation 的路径，对浮点与量化 block 的输出差进行积分梯度估计，再把 token 级代理用于原 channel-wise equalization 的 scale search；weight-only 与 weight–activation 的参考路径不同，这不是运行时动态分配 token 位宽。校准 artifact 因而还要绑定 reference、标量误差目标、跨 token 聚合、剪裁与权重归一规则，而不能只登记“用了梯度”。<!-- source-family:SF-2026-ARXIV-2603-17809 -->

[有限方法与对照](https://arxiv.org/html/2603.17809v1)也说明更细粒度本身不保证更好：普通任务梯度的 token 权重可比模态权重更差，误差代理则仍有任务反退。路径归因的 completeness 包含 reference 处的误差，剪裁后不再是原恒等；signed attribution 也不能直接当非负 importance 或正定曲率，原方法式、实现目标与消融口径须先对齐。这里只采用校准接口，不照搬未闭合的精确归一配方或授敏感性真值。额外前后向、积分与 scale search 属于制备成本，有限 GPU 校准时间不证明部署 latency；proxy、数值 guard、真实任务或预算不匹配时，保留较粗模态校准、成熟 activation-aware 方法与局部高精度，另验最终 artifact 和真实执行路径。

静态注：`SF-2026-ARXIV-2603-17809` — Daily2026-03-20补03-19；[exact-v1](https://arxiv.org/html/2603.17809v1)§3–4/Eq1–7/T1–6、必要A/B。仅quantgap路径归因→tokenweightedCWE校准接口；baselinecompleteness、signed/zero-sumguard与method/B/T4口径不授精确recipe，SFTtoken/部分任务反退及全部制备/部署费用分开。未核repo或复现。
