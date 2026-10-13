# HEAR 2603.16086：必要原证、有限机制提案与评价争议

准备者 resume_review17_18；本次仅03-19补BJT03/18自然日，root具名授权本family必要Source/actualsoleowner/PRE。已独立实际重读AGENTS、完整适用合同/prompt/ROADMAP、每日来源/主题与本日README/STOP/独核；保留2+2+3=7。不写Books/Report/LS、索引或脚本，不stage/commit/push；准备者不自行授Source/PRE PASS、写锁、actualPOST或DAY。

## 1. 身份与实际必要范围

[exact-v1 HTML](https://arxiv.org/html/2603.16086v1)，Chang Nie等五作者；本日已独校准入/官方公告日夹证有限复用，Submitted03/17不等firstpublic。current[官方abs](https://arxiv.org/abs/2603.16086)显示Sep18 v2/IJRR2026 accepted，无本次已见具体撤回/勘误说明；版本/接受标签本身不触发全新版或会史重读。本次实际v1完整题摘、§3–4/Eqs1–23、§5/Tables1–2的音频生产/因果接口、§6.1–6.4/Tables3–8必要设置/全部直接反侧、§7.2–7.3限制。定性图只读caption/正文，不授图内全部点、声波/视频视觉核、project/code、真实日志或复现实验。

## 2. 支持的接口与不能越过的桥

§3/Eqs2–8先按传感器延迟边界定义window。固定window可能丢失已结束且离开窗口的事件，这只是Eq7条件成立时的证据缺口，不能宣称所有chunk必然漏声。§4.2/Eq13以旧到新packet、causal patchifier/stateful transformer更新有限memory，episode初态清零；每次decision只读已到达的delayed boundary之内样本。§6.1披露16kHz/640samples=40ms packet、16memorytokens/4layers/width256/4heads、4s固定window。这是可区分的采集/压缩与决策时钟；学习压缩不保证所有事件永久保真，Eq14是有效保留horizon的设计目标而非已证明memory容量保证，memory更不在当前openloop中直接改命令。

§4.3高层Qwen3-Omni联合窗口/记忆/视觉/指令/qpos形成semantic latent与stage-text，低层Qwen3-0.6B消费高层条件/qpos交actionfeature。原文称reuse KV但跨骨干投影/层形状与更新频率实现不完整，不补成直接共享AR cache或fresh高频policy。§4.4/Eqs17–19以下一delayed-boundary音频的Mimi codes作CE目标，训练塑形当前latent；部署不必生成future codes，动作不读取真实未来音频。训练样本包含到下一边界的整段音频，不证明forward将未来target喂入当前policy；同样仅凭数学causal定义也不能认证真实loader/缓存/训练mask不存在泄漏。完整episode的video-to-audio合成即便只切过去音频，生成源仍可能使用未来画面，原文未给此信息捷径的独立对照；不能把synthetic sounds当物理已发生事实。

§4.5/Eqs20–22由当前低层feature条件化flow actionhead，Gaussian→expertchunk直线目标，test固定8步Euler；joint targets由PD在30Hz跟踪、H32默认openloop。这里training-only prediction、当前streammemory、动作采样与物理controller分责成立；不能授未来音频为部署world-state、生成动作天然平滑/免机械噪声、立即中断当前chunk或碰撞安全。

## 3. 必要评价、预算与决定性反侧

§5约120k OpenX-Sound episodes/100skills，视频生成音频只预训练，人工500episodes/两annotators称100ms容忍同步98.7%；不等microphone真值/50–200ms事件严格时刻或无幻觉，§7明承认遗漏/时移/幻声与域差。两阶段200k预训、模拟50k/真实30k每task、globalbatch256、AdamW/lr1e-4/wd.05及噪声增广已披露；训练/评价Ubuntu22.04、2RTX5090/PyTorchCUDA。完整高层模型尺寸、precision/runtime版本、walltime/search、独立training seeds/CI、真实demo数量和全音频生产/标注/缓存/八次flow/控制费用未齐，不由相同步数/接口授相同容量或总预算。

Tables3/4每task100trial，模拟七task全model约.81；Franka单workspace mic/两RGB/四task平均.54，但Moka.18、Phone.15仍大多数失败，sim Pour.51，不宣称普遍可靠。T5 noHistorizer.57、GRU.67、EMA.62、noAdvancer.73、regression.70支持受限选择，SST参数/容量与其他baseline联合不同，不能授唯一时间机制因果。T6按commanded关节推得end-effector<2mm低运动比例，不是实测轨迹smoothness、正确等待或冻结的独立标签；任务本就需要静止等待，不能把比例更低自动当更安全/更平稳。

实际时延：§6.1只说真机timestamp sensing/command logs估计tau_sys，未报数值/分布/分项或tail/SLO；sim默认tau_sys=0。默认H32/30Hz约1.07s，而window4s；在固定delayed边界、连续采集且查询间隔不超过4s条件下，相邻window覆盖重叠，未给默认评测中Eq7事件出窗的实际人口/发生比例，故不照录默认全部baseline因gap漏声的归因。传感器延迟+新decision间隔也不等即刻反应界限，丢声与动作不及时须分别验收。

决定性争议一：§6.4.3正文的首动作wrapper是执行a0后保持H−1步，而非每步requery；T7 .71 vs halfchunk.80/full.81不可证明“逐步更频重规划必退步”，它同时改变动作轨迹/执行wrapper。决定性争议二：§6.4.5明定义FT为t_goal<t_snd、MD为t_snd≤T<t_goal，两者同trial互斥；T8 OpenVLA .91+.57=1.48、pi .89+.52=1.41，同人口比例不可能。若用不同条件分母/多次触发事件，必须修改原定义与给出分母；不能自行补解释，也不把两率当安全错误概率。Eq10仅要求t_snd≤t_goal≤T，允许同cycle，且没有反应delay上界；“strict after”“immediate reset/safe”不得由它代签。上述反证不令贡献EX或降分，不升级为全部实验/实现虚假。

## 4. actual sole owner 与拟差额

本人实际Ch26 123–165闭环/三时钟与层级交接、421–449 future supervision→双时钟→remote旧图→contactgate、620–655episode state/reset/记忆评价；另Ch25/27前22行交接。现437是fast动作读fresh image/slow预测条件；现639是视觉读出双EMA，现453以后是泛training-only foresight。它们没有具体承载“音频packet独立采集更新有限memory→低频融合决策→训练-only nextaudio code监督→当前条件flow动作”的瞬态证据与动作时钟区别，不假NC。soleMULTIMODAL-EMBODIED-VLA提案放现437双时钟后/439remote producer配对前，两段最小机制，不在Ch25/27重复音频worldmodel或合成数据实现。

## 5. 最小逐字 PRE（待非准备者裁决，不是已采用）

双时钟还需区分“动作能读到新观察”和“短促事件已被采集保留”。对持续、易辨的声音，固定音频窗口或ASR条件仍简单；若声音在两次查询之间结束并离开下次窗口，可让独立音频支路按到达顺序把短packet更新为episode内的有限状态，再在低频决策时融合窗口、状态、图像与proprioception。状态只能消费已到达的传感器边界，并在新episode清空；它保留的是可错的派生摘要，不是当前物理真值，也不直接改写正在执行的openloop chunk。另以接下来音频区间的离散codes监督当前latent，再由当前条件的flow head产生动作chunk，是训练与部署的另一处分责：未来codes用于训练，部署不必生成或读取真实未来声音。<!-- source-family:SF-2026-ARXIV-2603-16086 -->

[有限音频控制机制](https://arxiv.org/html/2603.16086v1)需要把采集覆盖、压缩保留、决策年龄与实际响应分别验收；触发后到达目标的规则不证明即时反应、无泄漏实现或安全中断。相同窗口/训练步数也不控制全部模型容量与费用，错误率分母及执行wrapper存在未闭合处，不采用其错误概率、唯一归因或更频重规划结论。视频合成音频、状态维护、辅助目标、推理/动作采样及真实传感与控制都付费，名义控制频率不能替代尾延迟；单麦克风重叠声、机械噪声、摘要失真或deadline不足时，应重新观测/校准，保留可靠持续窗口、短chunk/reactive policy与经验证的独立controller，不由记忆或预测目标自授动作提交权。

### 拟静态来源注

- `SF-2026-ARXIV-2603-16086` — Daily2026-03-19补03/18自然日；[exact-v1](https://arxiv.org/html/2603.16086v1) §3–7/Eqs1–23/Tables1–8必要方法/评价/直接反侧，2+2+3=7。仅拟采用delayed-boundary音频packet/state与低频决策、training-only future-code/current-flow动作的分工；错误率定义/分母、执行wrapper与实际latency未闭合，不采用即时反应/唯一归因/错误概率或安全保证。未核code、日志/无泄漏实现、实验复现或taildeadline。

## 6. 精确裁决与一次请求

### root 非准备者裁决

独立实际核exact-v1 §4.1–4.6/Eqs12–23、§6.4/T5–8及§7直接限制；Ch26双时钟→远端旧图完整局部回读。接口本身由因果packet递推和明确训练/部署定义支持，可与错误率人口、wrapper及真实时延未闭合分开采用；不采用“解决全部漏声”、低运动即smooth、更多replan有害或任何错误概率。原两段PRE/静态注与具体差额PASS，原七分保持；批准只这两段，尚无actualPOST/safe/DAY。关键反证足够停止，不扩全code或新版附件。

请root非preparer定点核必要§3.4/Eq10、4.1–4.6与§6.1/6.4/T5–8及相关actualowner；决定§5有限职责链可否与隔离反证共存采用，或将本family作为中心终态保留。若暂缓，仅一次请求：与FT/MD定义一致的同trial分母/事件计数；首动作hold与真正逐步requery分开的wrapper/原始协议；timestamp传感可用边界与所有模块cost/动作响应分布、默认窗口内实际漏声人口；当前输入/未来target分隔和合成源时序的可核协议。接受相同精确版本的修订说明、评测协议/受限trace或可读实现；只重开受影响桥，不遍全部case、源码或新版附件。以上为准备阶段历史状态，当前以本节root裁决和§7 actualPOST为准。

## 7. 一次非 writer actualPOST

root必要Source/actualowner/原两段PRE独立PASS并实际窄写后，resume_review17_18本19独立合同上下文内实际完整顺读Ch26 429–451：future使用/latent-prefill边界→双时钟→HEAR新439/441两段→远端旧图→contactgate及forecast交接；实际2220–2226静态本人2226及ReMem/FastWAM/S-VAM邻注，scoped diff定点确认本family仅两段和静态自身源注，限定diff-check无输出。新正文逐字回§5原PRE一致；静态注只保必要原证、采用范围及未核边界，未复制人员/验收停点。causal delayed-boundary派生state/episode reset、training-only future codes/current条件flow动作分工与原必要证据一致；错误率/hold-wrapper/默认漏声人口/latency争议未被绕成正面保证，旧连续窗口、短chunk/reactive及真实controller退路完整。一次actualPOST局部正式通过，可释放本family Ch26窄锁并归并实际整合；不改Books注、不写Report/LS、不授DAY或全部headline Evidence。
