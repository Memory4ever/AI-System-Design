# CUAAudit exact-v1：必要证据与当前 owner 比较

本日报作者记录，非独立复核或 DAY。唯一 owner：`PLATFORM-EVALUATION-SYSTEM`（Ch66）。准入来自独立首包；本文件不改旧窗口。官方 [2603.10577v1 HTML](https://arxiv.org/html/2603.10577v1) 原件为 `SUP_CORE_10577.raw`，完整正文导出 `SUP_CORE_10577.txt`。实际读完 §1–6、三表、References；未执行代码、重现或核完整版本史。

## 方法与可采用对象

§3 给每位 auditor 相同 task instruction 和 final screenshot，不提供动作/中间状态，输出 done/not done 和 verbalized success probability。五模型为 GPT-4o、Claude3.5Sonnet、LLaVA1.5-7B、InternVL2-8B、Qwen2-VL7B；三个 benchmark 为 macOSWorld、Windows Agent Arena、OSWorld。采用 benchmark 自身 binary evaluator labels，不是本研究新增 human-gold。§3.3 以均方误差定义 Brier，另以逐样本 squared loss 的标准差定义 Std；§3.4 为 pairwise Cohen κ。这些是测量协议，不证明 final screenshot 足以判所有任务。

正文没有提供各 benchmark 的 N、done/not-done class balance、产生终态的 agent identity/version、任务筛选/无效样本/重试处理、完整 judge prompt、API snapshot、具体决策阈值、sampling/seed/repeats、硬件精度或实测判分成本。使用五种模型名字与三表不替代这些 identity。缺失协议仍是原稿证据不足，不伪造外部 blocked。

## 关键结果与反侧

Table1 的 GPT4o accuracy 依次 .91/.71/.77，Claude .89/.75/.79；跨数据集差异不能唯一归因“环境复杂度”，OS、任务人口、oracle/可见性同时变化且未控制。Table2 的 GPT4o Brier .058/.091/.074 与所谓 Std .003/.006/.004；Brier 同时受 discrimination、prevalence 和 calibration 影响，单个均值不能证明过度自信的方向，也没有 reliability diagram/ECE 或逐项数据。Table3 的 GPT4o–Claude κ .76/.66/.71 显示所报协议内不完全一致，不认证哪一位更接近现实真值，也不保证 ensemble 可消去共享盲点。

统计量存在需要澄清的协议风险：如果 §3.3 的 label 是同一 probability 在常用 0.5 阈值的决定，那么误判项的 squared loss 至少 .25；GPT4o/macOS 的误判率 .09、均值 .058 会使逐项 Std 至少 `sqrt(.09*(.25-.058)^2)≈.0576`，与 Table2 .003 不兼容。**本文未给阈值，所以这是条件性一致性检查，不宣称已无条件证明表格造假或全部结果失效。** .003 也不能自动改叫 standard error 或跨 seed SD，因为原公式明说逐项 Std，且 N/repeats 未披露。

§5 自述限于终态可见性、reported confidence 非 intrinsic token probability、binary task completion 非安全/隐私/副作用。隐藏状态和后台效果需要额外 evidence。高 accuracy 不能取代 observable outcome、审计/人工 anchor 或 policy gate；这是可保留的概念分工，但本稿精确比例、跨平台因果和置信度可靠排序均不直接采用。

## 日期新增门

首包已夹证 arXiv 首公告 Mar12 BJT，但读必要正文发现首页 footnote 声称 accepted AAAI2026 TrustAgent。该会议信号新增家族早稿门，不能被首包无先稿信号结论盖住。已定点检索官方/作者来源；搜索定位作者当前 Publications 与 repo 描述实际是 HEAL@CHI2026，而 AAAI 是另一篇 Are We Done Yet。当前 GET 原件正在恢复于 `SUP_CUA_DATE_MANIFEST.json`。需核 footnote 是否错误及可公开 workshop 原文日期；当前不把 arXiv 夹证当家族 first-public 已完全通过，不将三表的统计问题与日期问题混为一个 blocker。

## 评分、处置与 owner 差额

暂保留准入强度 `2+2+3=7`，深入是 final-state auditor 可靠性评价盲区；评分不为少读降级。Evidence拟处置：**争议/暂缓**（协议和数值边界未足以采用实验中心主张），且家族日期门普通待办；不是因只有五模型或 benchmark 论文而贡献前排除。

实际 owner 读取 Ch66 开篇/五成功事件、EvalSpec，以及 `Scorer 不是绝对真相`（2724–2780）、`Trajectory Judge 必须区分叙述、动作与完成证据`（2867–2904）和 `Judge Agreement 不是单一数字`（4482–4500）的完整局部及邻接。当前正文明确：model judge 必须被评估；固定 identity/人工或 executable 校准；final画面外副作用与 history不能省；success/failure recall、平台/可验证性切片；共享盲点 ensemble不授 truth；agreement population/scale/missing/pooling/metric独立保存。因此本稿可保留概念没有新增 owner 设计，**不是声称它三表的新实验证据已经被书吸收**。

拟 Books **No Change**：当前 owner 已有具体 evidence order / final-visible不足 / auditor资格与agreement分权，不采用争议比例和“复杂度唯一因果”。不制造书稿，不写 Books，NC 与 Source/日期终态仍待非作者核。新增0、改写0。

## root 独立裁决（2026-10-09，取代上文临时日期门与评分）

root 实际核过 v1 方法、三表与限制、作者 Publications/repo 以及上述 Ch66 完整局部和邻接。非作者复核记录 §6 的必要 Source 判断可复用；不重复全篇研究。

日期恢复只核首页会议信号涉及的两份原件：[AAAI TrustAgent 官方目录](https://trustagenticai.github.io/AAAI2026/paper.html) 的 Jan27 条目实际是同作者的 [Are We Done Yet? 原稿](https://trustagenticai.github.io/AAAI2026/AAAI-Workshop/14.pdf)，研究 42 个 macOS app/1,260 human-labeled tasks，与本稿三平台 meta-evaluation 身份不相同，不能仅凭同作者和相近任务合并家族。该目录没有 CUAAudit 条目；这只消解本稿 footnote 所指的具名早稿信号，不证明所有互联网目录均无早稿。[HEAL 官方目录](https://heal-workshop.github.io/) 则链接本题名、同作者的 [CUAAudit 原稿](https://heal-workshop.github.io/chi2026_papers/CUAAudit%20Meta-Evaluation%20of%20Vision-Language%20Models%20as%20Auditors%20of%20Autonomous%20Com.pdf)。定点 [该文件的官方仓库历史](https://api.github.com/repos/heal-workshop/heal-workshop.github.io/commits?path=chi2026_papers%2FCUAAudit%20Meta-Evaluation%20of%20Vision-Language%20Models%20as%20Auditors%20of%20Autonomous%20Com.pdf&per_page=10) 返回一条 Apr07 添加 accepted works 的 commit `bdf0bee658cfcaf8cbdd0c8a279dd9271335c673`；此后出现的 workshop 文件不把 arXiv 公告改作 Jan27。作者 Bib 年份 2025 不提供正文公开日期，不据此补造早公开。

在已经通过的官方 arXiv 日级公开夹证基础上，本次具名先稿信号已按实际身份处理，采用 **2026-03-12** 作为本补充的可核首次公开日；不要求证明网上绝无更早版本，也不把 commit 时间当作论文公开时间。后续若出现同一 meta-evaluation 原稿的具名早公开正文，再定点重开本家族，不能混用另一篇论文日期。原日报日期和候选不改。

评分裁为 **2+2+2=6**：本稿新增的是跨平台 auditor 测量及可复用的有效性边界，不把成熟的“judge 非真值”原则另计长期基础 3 分；深入已实际完成，分数修正不减少投入。正式 Source/Books 终态为 **争议 / 暂缓，Books 新写0**。原稿三表缺失的协议和条件性统计冲突未获澄清，故实验中心主张不作正面证据；稳定概念的具体已有覆盖已核实，但不冒称争议新实验已被 Books 吸收。重开只需同一版本的样本/阈值/Std 定义与逐项或可复查统计澄清；不请求未影响此裁决的全部代码、附件或完整版本史。本项日期普通待办结束，无 Books 写锁。
