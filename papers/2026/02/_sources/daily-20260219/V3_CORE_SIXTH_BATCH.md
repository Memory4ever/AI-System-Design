# 第六批必要核心

## 2602.15338v1 ObjDisco — 2+1+2=5，标准必要核心完成

[精确v1](https://arxiv.org/html/2602.15338v1) §2–5、AppendixA.3–4/A.7及两个人类研究实际读。用多checkpoint response trajectories、当前组合C的高残差prompt选择proposer候选，再用judge interpretability与trend函数检验、greedy降低held-out Obj-Error，形成少量可解释reward surrogate；不是唯一真实内部目标发现。DIR拟合原RM scalar，不拟合含KL的全部训练目标；trajectory相对endpoint可增加局部信息，不能据此唯一因果识别。OE的monotone-submodular/cardinality贪心(1–1/e)只针对固定sample上的解释fidelity+diversity目标，不授全局objective discovery最优。

Llama3.1-8B/Qwen3-4B PPO/GRPO、TLDR/HH/Alpaca/Sky，controlled3objective合成与DeBERTa/Skywork真实RM分开。A.4：100candidate prompts取残差top25、GPT4omini每3trajectories提2objectives、linear C；最后checkpoint held-out但时间相关，interpret/trend随机50、阈.15/.12，Model-Fit两组各100test inputs mean/SE。一般objective scoring GPT4omini，interpret ensemble GPT4omini/GPT4.1nano；实际validation PPO另用GPT4.1mini，KL/init/warmup和score-normalization另分配置。3trials声称同预算但重复reward函数训练/生成judge/rubric费用非零；主Fig3有6trial等具体口径，不混统一重复数。Hardware/precision/E2E费用未具体披露，未核实现/复现。

Model-Fit是DIR重训policy的原RM平均reward/原alignedpolicy原RM平均reward，可>1作者不罚，不是90%variance explained或90%causal coverage。GPT2-large helpful GRPO局部misalignment四trial检出3vs≤1，不是未知属性全召回。OE20AMT参与者400judgments、4trajectory/4options，39.9±6.5vs25.5±5.8(chance25)，不是400独立人；所谓causality-study16人480judgments选择四个回答的style/tone/content匹配，DIR35.6±4.3 vsIter16.7/Zero27.1/Base20.6，只支持行为再现偏好，多个相关objective可有相同结果，不授内部因果唯一性。LLM生成rubric/calibration又评分有共同偏差，proposer随机/阈值敏感、judge费用与偏差在A.7明确；独立human validation/真实行为与旧固定属性audit共存。必要核心/反侧足够，Books与独立必要源待核。

## 2602.15379v1 — 2+1+2=5，标准必要核心完成

[精确v1](https://arxiv.org/html/2602.15379v1) §3–5、Table4/6–9及§5.2warm-start/5.6实际读。Scope有GPTNeo/Whisper/SDUNet等具体模型GPU计算，不是仅移动应用。编译schedule预定weight首次/末次使用与chunktransform，以profile loadcapacity安排disk→unified→2.5D texture，kernel template branch-free prefetch/compute，必要时拆fusion恢复load插入边界。这改变的是预载/转换/execute的memory lifetime与coldstart取舍，不把CP-SAT名字当新机制或所有optimal。150s solver限多数FEASIBLE，只有GPTN-S OPTIMAL；512GDRAM/AMD5995WX offline费用未计online数字，dynamic graph执行顺序问题out-of-scope。

OnePlus12Adreno750/16GB主，3其他phone有界portability，11模型、FP16/32非quant、B1、50均值作者称variance negligible但未给全部置信区间；Table7 integratedInit+Exec对baselineInit+Exec，solver不算。warm-start SmartMem同model连续3–12次后可反快，故不授稳定serving throughput/TTFT/TPOT/SLO；未统一披露token/input/image长度，SD-UNet不是完整imagepipeline。Table8 average memory不是globalpeak hard保证，persistent W另加Mpeak；convtransform不可overlap反侧保留。Fusion/preload/texturelayout同时作用，incremental3项局部ablation不意味主headline只streaming因果。额外disk传输可更高power、cold integrated energy较低，不宣称所有能耗更好。未核实现/复现，Books及独立源待核。

## 2602.15382v1 — 2+2+2=6，标准必要核心完成

[精确v1](https://arxiv.org/html/2602.15382v1) §3–4、Tables1–5、AppendixB/D.4实际读。每frozen VLM独立latentrollout→Perceiver universalcodec→hub affine ridge→receiver decoder/gate→dummyimage residual vision-span写入，不是发送自然图像或零训练通用token同坐标。O(N)是permodel对hub maps而非每pair，shared D也不授semantic alignment；memoryconcat会随message数增长，固定image-span不意味history全部信息/所有roundcost恒定。αnorm/gate和affinefamily假设变化需重新验收，额外anchors可能必要，text route共存。

B1默认3000anchor pool、90weakpool，400stepsB2共800draws，weak约8.9遍曝光；6layer8headsdrop.1，universalD512/K1024，imageK256/T1024latent。前置codec训练/anchor提取/ridge费用未算online，label-free不等无训练。Main smallheterogeneous two/fourbackbone及角色配置，9固定task，A6000单/双GPU，greedy、maxnewtokens2048–20000按task/nominalB12/8/4但OOM可12→8→4→2→1；batch_time/batchsamples不是交互p99。Text message generation vs fixed1024latentstep改变实际reasoning通道/预算，即使role/prompt/max输出tokens一致，也不能全收益只物理通信成本归因。

Table2有GSMaccuracy80.8→76.2、GPQA某配置42.4→34.9、code/某配置0.57–.93×速度退步；作者macro1.87×/+6.3pp非逐项支配。CombinedMAS是含同model不同configuration均值，不是证明每single胜过；text-only latent baselines适配失败未获可靠quantitative对照，不能宣称所有latentmethod最优。无独立训练seed/CI与生产并发SLO；precision未统一披露。每模型codec/visualport能通信不授消息truth/provenance或权限，未核代码/复现。Books与独立源待核。

## 2602.15329v1 — 2+2+2=6，标准必要核心完成

[精确v1](https://arxiv.org/html/2602.15329v1) §3–4/Tables1–5、AppendixA.1实际读。1FPS/grayscalehist Pearson<.2（至少8frames）边界不是语义oracle；固定STM32frames内event FIFO迁出、当前长event n>K后K/n reservoir给frame uniform inclusion，不保证每罕见关键event/细节保留。LTM firstframe+MLLM caption/embedding/changelog是derived record，工具回看anchor/STM OCR/DINO可补证但不是全历史visual可逆。Qwen4Bcaption/Embedding.6B、top3>.3检索另有计算/storage/失配成本，历史event数增长不授constantmem或真正无限视频保证。

Qwen3VL8B、MovieChat10k/VideoMarathon labels，八A10080，GRPO G8 B64 1epochlr1e-6/KL0；训练video预处理成memory模拟online，不是live perception throughput测试。OVO/Streaming仅querytimestamp前可见，main不同model/frames/train预算不单独归因。Table3 sameagent fixed30s segment对event层次60.16→60.75/76.80→77.00，是bundleevent+reservoir局部小收益无seedCI；Table4 w/oOCR realtime反更高68.80>68.29，工具不是处处有益。Streaming总体77.00仍低StreamForest77.26；≤32是STM，不等全部LTM/tool视觉预算。Terminalcorrectness reward不授每toolneed或historyfacts真值，未披露完整querylatency/precision/并发SLO。采用有限层次采样与按需取证分工，旧fixedFIFO/定长仍在边界稳定时合理；未核代码/复现，Books/独立源待核。

完整精确题摘与具体准入链见[V3_ADMISSION_SIXTH](V3_ADMISSION_SIXTH.md)；候选准入/独立源与Books处置分开。97身份不等97候选，不因安全标签遍历所有附件。

## 2602.15344v1 — 2+2+2=6，安全必要深入完成

[精确v1](https://arxiv.org/html/2602.15344v1) §3–5、Tables2–6、AppendixB/C/G实际读。content-based看过interaction而未知未来query；question-targeted已知目标q、伪造answer，一/二条perq；不要把两setting合并为看不到全部content的同一黑盒。对mem/query embedding近邻的instruction/contradiction/noise八primitive及ensemble影响top-k读取；余弦≥阈值不是top-k命中充分条件，更不证明semantic imperceptibility。主采用是stored adversarial-memory→retrieval→behavior链，retainingcorrectmemory并不确保正确回答，不授所有memory架构根本必然漏洞。

LoCoMo10不含adversarial questions；Llama3.2-3B主、Gemma3-27B/GPToss20B，A-memMiniLM vsMem0nomic不同writer/retriever/evaluator人口。主k10→20/30攻击命中更高，而cleanoverall23.60→26.14→25.57非严格单调。Table4 GPToss/A-mem content攻击仅−2.4/−4.2/−4.7，与Mem0大降不同，不能所有强模型同率；Table5有些open-domain F1攻击后反高。F1/BLEU overlap降幅不等harmful-action ASR，v1root可点对应Table。

B声称同interaction路径无privileged API；C3/G6却只明确aftercleanmemoryconstruction inject textualrecords，未唯一披露每attack经过extract/update/filter的接受率；采用已stored条目影响，不认证现实写入admission都可穿透或零权限能力。content生成使用每cleanmemory，但理论agnostic说不见store：可来自既往interaction，不能加上‘不知全部history’。G6 timestamp-null retrieval计数是logging标记，不直接证明真实deploy不可察觉。Ollama .13.3同runtime，Mem0T.1/max1500/topP.9而A-memdefaultT.5；固定settings不是cross-memory一切归因同预算，GPU/precision/seeds/总代价未披露。G1称supplementary scripts但未核artifact，不称复现。没有测得防御成功，人工confirmation/filter/leastauthority旧route保留。Books与独立源待核。

## 2602.15364v1 — 2+2+2=6，安全必要深入完成

[精确v1](https://arxiv.org/html/2602.15364v1) §2–5、Theorem4.1–2/Table1–2/Fig4与Limitation实际读。no-box无watermark encoder/decoder/生成模型，训练仅clean COCO/GenImage的edge-weighted Gaussian proxy，频带FFT+learnable masks/fusion denoise，再frozenRealESRGAN；额外模型训练/decoder/SR不为零成本。High-frequency扰动不表示所有watermark都该域，noise-basedGaussianShading直接限制保留。

100images perwatermarker，A6000、224patch、10kcleanimages80/20、500epochsB80Adamlr.001；四scheme固定BA阈值69/61/70/73，MarkSweep SS66.83/Yu59.24/HiDDeN51.32低于对应阈值，但PTW72.19仍高于70，不能四种全erase。LPIPS/PSNR/SSIM各取舍，MarkSweep w/oSR有些数值更好，原‘不降quality’不采用；0.64sSS/.14sHiDDeN是作者perimageattack，VAE更快，未计离线500epochs或全部image/watermark/精度/批并发。

理论采用边界：Markov链和独立exogenous noise支持DPI非增，不推出严格降低；Theorem4.2以Fano下界变大推出实际Pe变大，且whole-message Pe换bitBA，推理不成立。不采用‘必然unrecoverable’安全保证。具体反例（本审阅数学推导）：w=(w1,w2)独立均匀bits，xw全揭两bit，变换只保留w1使MI2→1，但固定decoder两侧都读w1且把w2猜0，则期望BA均.75，没有严格下降。该争议只隔离理论/通用保证；有限检测失败与generationartifact/质量取舍的有效证据不推倒。需要root定点独立核该证明和安全反侧，Books实际owner待比较，未核代码/复现。
