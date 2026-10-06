# 02/13 CFIVE：11021 / 11047 / 11065 / 11072

仅本窗exact-v1，准入已root独立校准；四项均在119逐项落窗交集中，沿公告下界/created上界的保守包络，不用Submitted等同public。必要HTML与定点评价已读至支持/直接反侧停止，原返回CFIVECORE0–3/MORE0、1、3/LAST0、1/TAIL0–2。当前abs轻量检查未见具名withdraw/correction；11047有v2/v3而不因版本号展开，v2提交时间不直接授public或重要修订。未核代码、未复现。以下作者判断，尚待非作者必要复核。

## [ContactGaussian-WM](https://arxiv.org/html/2602.11021v1)

原窄5分不变；采用共享render/collision geometry接口，拟差额深入。CORE0 III L115–183：固定isotropic sphere/frozen rotation，先geometry-map拟合且freeze appearance，再freeze geometry拟合appearance；中心和2×scale半径共同进入collision union。LSE minimum与负穿透sigmoid/penalty是平滑proxy，不是任意penetration的真实signed distance，投影还依赖非零梯度。已有complementarity-free friction/impedance动力学是借用机制，不计成新contact定律。图像loss经render→predicted rigid state→physics优化参数；geometry只通过collision支路更新，L183明确不从render直接改geometry，避免外观补偿掩盖接触几何。

MORE0 IV L208–276：MuJoCo fall/rebound、push有限人口，Dreamer100条轨迹且GT逐步条件、其他单轨迹/既有真实mesh，非统一sensor/geometry/预算。Camera translation ours.0043高于PIN.0027，Rubber .0218高于CEM.0128，不能授所有误差最好。真实LEAP用手机初始化/RealSense、train:test1:4、先几帧拟合initial state；没有GT state只能PSNR，不能由拟合视频授物理参数可识别。No-opt有限自消融不是sphere/analyticgradient独立2×2。40Hz是RTX4090图像生成，不是真实MPC deadline；MPC只MuJoCo。明确deep penetration、rigid-only与render fidelity限制，precision/batch/concurrency、CI、完整训练成本及真实控制SLO Not Disclosed。

拟PRE：MULTIMODAL-WORLD-MODELS Ch25 L120–124的simulator/learned取舍与157–181 action-conditioned分责未承载**可渲染和接触共用geometry、限制appearance与geometry更新路径**。拟在显式simulator论证后两段：sphere collision proxy与render state同参数减少两套几何漂移，但不能从视觉拟合推出真实接触/动力学可识别；先分阶段外观/几何，再受控physics gradient，deep penetration/rigid-only和simulation/真实观测回退就近保留。不搬借用contact公式或40Hz成绩，不授物理安全。现owner/相邻Ch24/26实际已读，等待root必要源/owner PRE及Ch25窄锁，不先写。

## [Embedding Inversion via Conditional Masked Diffusion](https://arxiv.org/html/2602.11047v1)

原6分安全变化受影响深入；拟**深入完成/仅报告**。CORE1 L51–148/A166–185：cached embedding conditioning以AdaLN进入MDLM，多mask token并行去噪；adaptive remask与顺序greedy是不同预算分支。每target encoder分别用2M C4配对训练，**仅inference不调用target encoder**，不是无需训练encoder访问/paired data、一个decoder跨所有encoder。32token范围，freeze/tied GPT2词表50,257与Table1大词表字段不一致，270Mtotal/78Mtrainable/312MB身份也不明确，不采用绝对统一规模/速度结论。alpha=e^(-5t)在t=1不严格allmasked、1/t的解释与masked程度不符，不为本篇ELBO或全流程保证背书。

Table2 Qwen顺序.585低于two-stage.591，Table3 remask .05局部优于无remask而.2反退，不授所有配置最优或81.3%/0.87为同人口。训练单A10048h/计划200k与best checkpoint步骤分开；150ms顺序/50msEuler只每32token片段，推理batch/steps/precision/concurrency/完整成本、holdout identity/seedCI Not Disclosed。当前abs v1 02/11、v2 02/12、v3 02/18提交史只作轻量identity，未见明确修正信号，不加载后版本内容。

Ch72 L330–367已实际承载embedding等observable channels、观察权限/auxiliary knowledge绑定、重建测量≠DP/全域安全；本篇新增局部parallel decoder分支与特定短文本攻击证据只报告，不声称该算法已经正文覆盖。风险反侧不改变既有权限/泄漏审计长期原则；词表/规模/训练身份不一致隔离，不授encoder-free training、普遍跨域风险或生产速度，不因此撤回已校准候选。

## [ConversationGoT](https://arxiv.org/html/2602.11065v1)

原窄5分不变；标准完成拟**仅报告**。CORE2 L165–230：未committed second nodes在句提交时折成sentence node，causal selector只取past anchors，加recent committed cache与within-sentence buffer再由T5生成rationale。新增时序state接口成立，不把speechact labels或GoT名计贡献；teacher的retriever标注近似posterior不是因果truth，causal mask只约束时间可见性，不证明解释faithful或ASR改写/commit检测可靠。

MORE1 L240–316、TAIL0 L313–326：120h主要synthetic，真实Candor只evaluate；mono16k/1sec/90secW，SA和GoT分两阶段，B8/GPU15epochs fp16、A6000训练18h/5h。seed42及5runs局部不等production tail。random-selector复用reasoner是局部matched选择反侧，但latency ours.74±.12/random.73±.11；GPT4o2.98/GPT5thinking16.98不同模型预算/服务硬件，不能授20×生产速度。GPTjudge与teacher家族偏置、人评HMA高/低.97/.77对GPT.78/.93、GPT5若干quality更高就近保留。end2end ASR/SA/selector、真实commit error、推理hardware/batch/concurrency/SLO ND。

Ch75 L130–147的provisional view/foreground assembly、L249–272 query条件压缩与Ch23 L825–851 stream identity是一般原则，不声称已覆盖本篇seconds→sentences算法。该局部人工/synthetic评价未提出足以另改长期state authority的可靠性条件，只有有界fold/cache recipe及有限对照；Only保留具体新增证据，而非因‘已有覆盖’撤准入或把所有causal graph解释成因果机制。

## [Hibiki-Zero](https://arxiv.org/html/2602.11072v1)

原6分；拟采用对齐与探索support差额深入。CORE3 L92–163：12.5Hz Mimi、16codebooks、temporal/depth双轴，2frame acoustic delay=160ms而非zero buffer。sentence对齐训练插随机delay/silence，target可在source sentence尚未结束前开始；不是去除全部对齐或时间戳，仍有transcripts、target TTS wordtimestamps及每8sourceword的reward时间。BLEU process reference包括**当前已开始的完整sentence**，未必只包含已听到词；full/reference训练监督不是部署future输入。

MORE3 L164–220：约3B，Helium2B init、500k coarse B96/160k小时4语种、<200h fine、depth distill20k；RL B32/G4/LR2e−7/2000updates/old刷新20/T1500/.8topk250/alpha.4/eps.2/text100audio1，无KL不等onpolicy全局优化保证。AudioNTREX synthetic4L300/lang/3TTS与Europarl1024/lang分开，Whisper-medium ASR/COMET/WavLM及EndOffset/LAAL是内容/语义lag指标，不是设备wallclock SLO。valid每200择best quality-latency，训练/推理HW、dtype、inferbatch/concurrency、重复seedCI/总TTS成本ND。

LAST1 L222–284、TAIL1 Tables5–6 L365–401：同style synthetic valid BLEU~60 vsrealtest30；long FR ASRbase29.7>Zero28.7、speaker67.5>61.3，long DE30>28.3，Italian追加后多旧语言speaker/latency反退，不能授quality/retention全胜。§4.7固定alpha/nw的关键反侧：full-reference较慢；若base只学整句结束才输出，RL仍约6秒且没学会提前开始；去句内随机silence质量/延迟均退。它支持先建立早发探索support，不证明GRPO普遍能突破任意alignment数据支持或无需GT。

拟PRE：MULTIMODAL-REPRESENTATION Ch23现188–220 codec-prefix/teacher身份与825–851 runtime可见prefix/interrupt未承载**跨语word alignment可放宽为sentence随机delay，但先建立提前发声支持，training reference与arrived prefix分开**。拟streaming论证融两段：coarse alignment改变监督时序support，不改变推理只读已到达观测；参考reward可看GT已开始sentence不是听到词，句尾only base的探索失效与质量/音色/lag成本保留。只写表示/监督时间接口，不复制GRPO公式/codec双轴，不授zero latency或production安全。actual owner相关上下文已读，等待root必要源/owner PRE与Ch23窄锁。

本批4项必要证据已获root独立复核；11047/11065仅报告通过。11021已实际融Ch25正文126/128、末注1561，11072已实际融Ch23正文829/831、末注1205；root实际顺读新增两段、邻接与来源末注，非作者POST通过，两窄锁释放。累计104/112=98必要审阅+6低分关闭，余8普通；32实际Books POST通过，不授日级。
