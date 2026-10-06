# B第六组必要证据：10680 / 10693 / 10715 / 10764

四家族准入已非作者校准，均119日期交集，无新增早公开线索。采用精确v1；当前abs仅10680/10693/10764窗外修订，10715仍v1，未见明确withdraw/correction声明，不扩版本史。作者必要审阅完成，root已独立核四项必要证据与处置通过；10693/10764实际正文整合POST亦通过（Ch24已改noise-to-intermediate），不授日级；未复现/未核代码。原源BSIX_INITIAL/CORE/TAIL索引0–3依本标题顺序；LAST_1为current abs，LAST_2含DE-CM反侧及VESPO配置，PROOF_JUDGE只采用必要证明/评价协议段。

## [10680 nonlinear autoencoder](https://arxiv.org/html/2602.10680v1)

5（2+1+2），实际评价反侧定点深入。§1 whitened双latent spiked模型，centered且dependent-but-uncorrelated使v方向不在covariance；单hidden neuron、tied weights且特定非线性可读higher-order依赖，不是所有非线性都成功。§4 Theorem4.2受spherical radius、正交spikes、L²/Hermite与四次可微、C2<0及C3/C(3,1)非零等条件约束，只到weak recovery阈值；tanh在k*=2可失败，radius改变可推翻正侧分类。online SGD dlogd是heuristic尚未控制噪声，ERM replica-symmetric结果明确未rigorous，不合并成通用优化证明。

§6 Eq24是点态投影最优性：对固定w，线性正交rank1 projection有不高于沿w任意非线性重建误差，但下游标签专取hidden spike，故重建loss较低仍可丢任务结构。仅人工依赖类别/小labels且假定finetuning不能改初始化，不能泛化LM CE或所有自监督表示。主numerical d2000/fullbatchAdam lr.1/800epoch/无decay/30instances±std，AMP d10000/72seed是另协议；HW/precision ND。ReLU比ELU高重建loss仍更佳toy下游，linear更早恢复u而牺牲v；非线性有sample tradeoff。

仅报告提案：Ch5实际255–263区分reconstruction score、独立decodability与行为使用，本文提供特定高维反例，不为其单神经元/RS与受选toy任务建立普适系统控制律。不是EX，也不假称该exact模型已有覆盖。支持与直接反侧足够；不授全文证明无误或真实大模型因果。原源INITIAL0 89–142；CORE0 192–284；TAIL0 285–311。

## [10693 VESPO](https://arxiv.org/html/2602.10693v1)

6（2+2+2），标准且拟差额定点加深。§3+AppB固定mu/pi正支持、可归一且可行的约束问题，一阶变分给Q∝mu W^alpha exp(-lambda W)；这是所声明KL混合+E_Q W条件的proposal，不是原policy无偏梯度。E_Q W只是约束proxy，不能单独证明实际phi² A² score梯度方差或任意长序列收敛；Q依theta也不等任意on-policy∇E_Q reward。实际按advantage符号选择tunable(c1,c2)，detach weight乘完整sequence logprob，无1/T。需要behavior/current scoring与支持，不认证无额外memory/engine一致性。

§4同base/DAPO-Math/8responses/1500updates、MathVerify、16k上限，Llama3B/Qwen8B/30BA3B；mini256，改变global=N×256控制批内stale，N4–64并不等版本时间差64倍或固定wallclock。best checkpoint用全部4测试平均选，avg32/16/4协议不混pass@k。F实际sync32H20，async48rollout/16train、每4updates同步保留inflight，lr1e−6/Ttrain1/Teval1 topp.7/KL0；precision、多训练seed、wallclock/SLO ND。R2还能改善，说明不替代数值/route一致性。

直接反侧：Table1/2同标N8的Qwen30B VESPO平均57.2与66.9不一致，GSPO亦不同；不拼成唯一准确率。§3.4/4.1/Alg设A+ (2,3)、A−(3,2)，§4.6末解释却写负c2=3/正=2，参数解释冲突；采用已明确kernel接口，不宣称全公式/最优非对称参数无误。长度归一消融局部崩溃不是所有lengthnorm必失效。

拟Ch33窄差额：current2194–2204已载stale版号/ratio/整组admission条件人口，但尚无这种sequence soft-reshaping所改proposal、不是unbiased恢复与sign-conditioned kernel分支。若PRE通过，只一段机制一段条件/反侧，不采用表格冲突数字、通用variance guarantee、无限stale或无成本。原源INITIAL1 120–200；CORE1 216–276；PROOF_JUDGE 413–455；LAST2 542–561。

## [10715 LoCoMo-Plus](https://arxiv.org/html/2602.10715v1)

5（2+1+2），评价反侧深入。§4 cue/trigger合成人工筛选、BM25/MPNet低相似过滤，再插LoCoMo gap；测试隐含state/goal/value/causal约束是否消费，不等用户真实授权或内在因果memory。§6.3固定base与metric仅切task disclosure可改变task-wise profile，这是matched prompt条件反侧；length-score曲线跨模型不能单独识别纯长度因果。跨LoCoMo vs Plus差额同时改任务/构造，不当纯记忆效应。

GPT4o writer基线、top5retrieval与多open/closed models；100cases/memorytype长度压力、生成T.7/max256/每relation50是data生成不是evaluation统一推理配置。judge按task三档/二档，human2人~.903与Gemini.801/.820只协议一致度；跨judge差≤3.33不等正确性保证，参考有错例不证明judge普遍更可靠。English/synthetic/有限backbones；完整testcase总数、human agreement抽样/不确定性、所有evaltemperature/precision/HW/batch/SLO ND，不从均分表反推。

仅报告提案：Ch77实际1610后recall→context activation/commit、1617episode constraint/decision而非相关fragment已有具体消费边界；本文诊断披露/生成式评分与低相似cue局部失效，但尚不能区分encode/retrieve/read瓶颈，不能把新bench的低分改写为全系统memory保障或全language可靠judge。保留新的评价反侧，不声称exact benchmark已有覆盖。原源INITIAL2 123–165；CORE2 201–244；TAIL2 245–263/307–327。

## [10764 Dual-End CM](https://arxiv.org/html/2602.10764v1)

5（2+1+2），标准且拟机制差额加深。§4把endpoint maps分三簇：t→1 consistency、t=s instantaneous FM boundary、0→t N2N，增加right-time输入，JVP与teacher双端velocity/周期N2N update；mix先Euler再CM而不是每step独立renoise。不采用Eq8从平方和拆分为数学恒等式，Eq12逗号代减号/Alg g_n2n用F_cm记号亦不当可执行完整公式，接口与实测component关系可保留。

ImageNet256/LightningDiT/VA-VAE32×16×16/675M，50kimages FID，250epoch/AdamWlr1e−4约3天；C2I硬件/precision/seed、Table1 latencybatch/HW ND。T2I100k subset/SD3.5Medium/LoRAr64/lr5e−4/64A100约2天是另一协议，不拼成相同成本。matchedTable3 FM+CD FID50=1.78 vs加N2N1.26；去CD一步极坏，说明fewstep/distinctboundary，不证明所有CM不稳定。velocitynorm去掉2step1.30优于full1.33，非所有组件逐点必要。Table4 mix4/8/12/16为1.41/1.51/1.53/1.42，对应CM1.56/2.37/3/3.72及Euler76.15/8.26/3.61/2.38，局部采样收益不认证生产延迟。§6明确JVP与FSDP/FlashAttention不兼容且显存高，限制大规模训练。

拟Ch24窄差额：current449把分布匹配与flowmap组合一致分开，但没有把一致性终点、instantaneous diagonal、noise→intermediate三个训练接口和mix启动分工联起来；新增是子轨迹选择与成本/边界，不授完整数学、普适稳定或fewstep质量无损。PRE前不写。原源INITIAL3 106–164；CORE3 205–250；TAIL3 293–301/348–360；LAST2 359–383。
