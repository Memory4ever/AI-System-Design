# GigaWorld-Policy17240：动作先行与可选动作条件未来

resume_mar17，仅03-20补03/19自然日。原批6/独核§17的2+2+2=6和日级identity夹证复用；current-v2仅Added references轻量信号，不全diff。恢复实际重读AGENTS、Research/Report合同、Sources/Prompt/ROADMAP、本日README/STOP及Books约束。未自授Source/PRE/safe、未写Books，不扩发现。

## 1. 必要原证与停止

实际[exact-v1](https://arxiv.org/html/2603.17240v1)§3.1–3.4/Eq1–12 L99–172、关键§4/T2–7 L173–282与直接反侧、Appendix A配置/基线284–294及T8 295–327若干直接任务反侧。L67–82只动机；图仅文字/图题，不冒精确图像曲线。未读T8余行、其余附件/代码或旧修订。支持及直接反侧够所采接口即停止。

## 2. 采用接口及重叠的明确边界

RGB三视图compose到原总分辨率，VAE当前/未来，state/action投影，与共享5B Wan2.2 QKV处理；语言从外部crossattention进入，不在selfattention的四块因果顺序。To/Ts互读、不能读Ta/Tf；Ta读当前obs/state、不读future；Tf可读当前obs/state/action。这是计算图依赖，不是物理因果识别或全部训练泄漏审计。不要将块间列表误解为动作不能内部自读。

视频预训练后以action/video两flow目标posttrain（action5/video1），共享参数使video训练仍影响action；训练目标和在线future消费须分开。默认在线只instantiate action，future tokens完全不建；如需未来，原文另提供joint去噪或消费action denoising保存KV再生成future两路线。后者KV内容、每层/solver时间与重建协议未完整披露，不授无损cache配方、两模式动作完全相同或免费诊断。

actual Ch26已有DreamZero16666完整段：动作不读future、两支分别读当前帧、共训塑形、测试删video，只此命题是具体已有覆盖，不重写。尚有有限差额是future额外读action的单向条件，以及同一模型action先生成后按需生成其条件未来；不是把旧“auxiliary可删”改名。Ch25一般action-conditioned transition已覆盖世界预测，缺这个action critical path与可选visual消费者的运行边界。拟只在Ch26现DreamZero完整段后补一段；root非preparer裁可分采差额或具体NC，不能按忙碌改处置。

## 3. 有限评价、直接反侧与费用

p48/Δ12→4未来帧、5B、A100推理、RoboTwin50任务/每任务100episodes、clean2500/random25000示范已披露。PiPER6DoF四任务各20trials，每trial最多5attempts；真实pickplace采用半分抓握/半分放置，不能混成单次binarysuccess。T3 action-only360ms/Motus3231ms约8.975倍但不同路径/模型，ours模拟.86低于Motus.88；T2 clean/rand.87/.85低于.89/.87，HandoverBlock/Mic/Cabinet等直接退。T3 pi0.5模拟.48与T2 .43/.44不同aggregate。T4 oursQR.75仅持平；平均.83 vs.76约7个百分点，非普遍7%相对增益。

T5 Δ0列SR.60但L274称.65→.83；Δ0为K0 sentinel，不执行floor48/0；不采精确差额或recipe。T6 causal .83 vsunrestricted .81，PSNR28.41 vs27.87/SSIM.901 vs.892，L277–278误引T7而actualT6；无CI/匹配路径计时，不能授unique因果/质量无损或两在线模式相同。T7 scratch.45/videoInit.57/embodied.73/both.83是有限训练比较，不控制全部pretraining人口费用而识别唯一physics原因。图示10%样本效率不采用精确倍率。T1估计hours合计11185而文字approximately10000，不将估算口径等同完整charge。A预训练6000GPUhours/globalbatch256/AdamW与LR有披露，不写全部ND。

pretrain硬件/precision、采样步/全部视图费用、controller执行chunk与刷新频率、p48实时时长、完整闭环tail/SLO、重复runs/CI、后训练/编码/actiondenoise/可选未来的全预算必要段未披露。sharedQKV和低action-only平均计时不证明cache/诊断免费、接触安全或deadline；不采用所有WAM都必须future的泛比较。一次强桥请求为匹配两在线模式/solver-KV trace及完整预算、fixedtrial/attempt/gradedscore分母与controller时序、T5口径与独立回归。所采有限计算图不以这些强保证先闭合为前提。

## 4. actual sole owner 与一 literal PRE（待非准备者裁）

实际Ch26完整360–468：world-action的三路线/GigaBrain/teacher/MVISTA、DreamZero16666、future使用/latentfreshness、training-only交接；Ch25 286–328 actionconditioned/inverse/generaltransition与Ch27入口。sole `MULTIMODAL-EMBODIED-VLA`，拟DreamZero16666完整段（当前418）后、未来时序干预段前。只图方向/可选消费者差额，不重复旧删future结论/一般世界模型。

让动作不读未来，还可以与“未来读取动作”组成单向接口：当前观测与state先支持action chunk，视频支路再以动作表示为条件提出未来，而不是反向给动作提供线上证据。同一共享backbone可只建动作tokens，也可在需要可视化时另生成动作条件future；[受限实现与对照](https://arxiv.org/html/2603.17240v1)还提出复用动作去噪保存的KV，但具体solver/cache身份与两模式一致性仍须验收，不能由mask宣称免费或输出完全相同。共享视频训练可塑形动作参数，生成画面却不是动作已执行后的事实，也不替独立controller批准提交。action-only局部延迟、模拟/实机分母及质量反退须分验；编码、共训、动作采样与可选未来均付费。缓存失配、预测不可靠或闭环预算不足时，保留经过验证的action-only/direct policy、短chunk及真实观测刷新，不用自洽未来替物理反馈。<!-- source-family:SF-2026-ARXIV-2603-17240 -->

静态注：

- `SF-2026-ARXIV-2603-17240` — [GigaWorld-Policy exact-v1](https://arxiv.org/html/2603.17240v1)必要§3/Eq1–12、§4/T2–7与A配置/直接任务反侧。仅动作先行、future读取action的单向可选消费者；原删future机制已有覆盖。保共享训练、KV/solver协议未认证、模拟/attempt/graded分母、反退/T5冲突与全费；不采物理因果、两模式无损、唯一加速/样本效率、免费诊断或安全deadline，未核代码/复现。

准备交root非preparer必要Source/actual差额/literal裁，未授权写入。

## 非准备者必要 Source / actual owner / PRE

root 实际核 exact-v1 §3.2–3.4、§4 的评价人口与 Tables2–7。future 可读 action、action 不读 future，以及 action-only / joint / 保存 action KV 后生成 future 的接口均有原文依据；不是把共训删 video 的旧命题改名。共享参数和两种在线路径的全输出一致性没有证明，KV 的具体 solver/version 配方不能补造。局部延迟、实机 graded/最多五 attempts 与模拟 binary success 分开；表中任务反退、Table5 的 .60/.65 冲突和未闭合总费用均保留，不采独特物理因果或安全实时保证。

实际 Ch26 398–428 的完整 DreamZero→未来干预交接，one literal/static 与上述有限原证相容。仅新增动作先行、未来读取动作的可选消费者，旧动作不读 future 和共训接口保留。必要 Source、实际差额及 PRE PASS，原6分不变；授 resume_mar17 sole Ch26 原 DreamZero 完整段后 one literal 与本人注窄写，写后 root 一次非writer actualPOST。未写后验收前不计实际 I/DAY。

## 窄授权后 writer 实际落实

按root唯一Ch26本family窄锁，仅原one literal/static逐字写新424与本人静态尾注。writer完整407–443与末8实际顺读，DreamZero旧动作不读future与共训保持；新未来读取动作的可选消费者后仍接时序干预与latent freshness。实际正文和静态注逐字回批准稿，新增本family只有一段+注，限定diffcheck0。交root一次nonwriter actualPOST，不自授safe/DAY，不循环identity注。

## 非写入者实际写后复核（2026-10-12）

root 实际顺读 Ch26 407–445 与末9行，正文 one literal 和本人注与上述批准稿相符。旧 DreamZero 共训/部署删除 future 的完整论点保留；新增段只接动作先行、future 读取动作的可选消费者，随后仍进入 future 时序干预和 latent freshness。KV/solver 身份、两在线模式一致性、物理反馈及完整费用限制均在机制附近，没有由局部延迟授予实时安全或免费诊断。必要原证与直接反侧的有效裁决复用，不重读附件。实际 POST **PASS**，root 接纳本 family 为实际整合并释放 Ch26 窄锁；本日有限来源收尾、最终分母与 DAY 尚未验收，不能据此增加日级完成数。
