# 2603.11243v1：CTC 复用与两级效用仲裁

root 必要审阅；只处理本日新增候选，不认证日级完成。精确 [HTML v1](https://arxiv.org/html/2603.11243v1)，实际缓存 `SUP_CORE_11243.raw/.txt`；完整读 §2.1–2.3 Eq2–7、§3.1–3.5 Table1、verification ablation 与直接限制。当前官方事件未见撤回信号；本日独立日期夹证已通过，日期不再重查。

## 新命题与证据边界

旧方案让 AR decoder 完成每次转写，语言先验可能覆盖声学证据；作者复用已有 CTC-trained frozen acoustic encoder 的 greedy alignment collapse 作一次完整 utterance proposal，而不是新增独立 drafter。全帧 entropy 小于阈值直接结束；否则一次 causal forward 对全部 draft token 求条件 likelihood，均超过另一阈值才接受。首个未通过位置后丢弃 suffix，仅保留验证前缀并继续 AR。低 entropy 不是识别正确概率，likelihood 阈值也不是经典 p/q acceptance 与 residual correction；输出允许偏离 target，价值由任务质量与成本判定。

本稿单 H100、BF16、按 audio length 排序、动态 token 上限50K，verification 与 fallback 两次分别组 batch，失败 utterance acoustic embeddings 期间 CPU offload；另合并 LoRA、FA2 与仅求验证位置 logits。Granite Speech 4.0 1B text LLM + 440M CTC encoder + 37M projector；90K h acoustic corpus与21K h synthetic translation训练，不能称没有模型训练，所提推理分支不要求另训drafter。输入输出长度依各 corpus 未逐项统一报告，并发线上SLO、性能重复/不确定性 Not Disclosed。

Table1 Open ASR eight English test sets平均：AR WER5.75 / RTFx564；高准确阈值0.7/0.2 WER5.58 / RTFx548，吞吐并非同步提高（Earnings22 391→278、SPGI666→592）。高吞吐3.0/0.1 WER6.56 / RTFx2491，约4.4倍RTFx伴随约14.1%相对WER增幅；摘要“12%”与本表直接算值不同，不直接合并。不是每请求实时latency，不能平均数字反推生产p99。Fig4去掉LLM验证达不到最佳WER，去掉CTC gate损失高吞吐端；仅支持该模型/ASR负载的两级策略，而不是两级gate普遍最优。作者的 z-test 未充分说明相关词错误的统计人口，正文不采用其普遍显著性保证。

限制：需可复用且冻结的CTC encoder；当前仅ASR，不含翻译/语音QA/实时对话。utterance verification失败需从首reject到结尾AR，不能免费重新接回draft；低接受率与CPU搬运/分批开销可能抵消收益。未核代码或复现。

## 当前 owner 与实际差额

唯一 owner `INFER-SPECULATIVE-DECODING`，Ch48“当 Draft 可能优于 Target”解释一般 utility arbitration，后续 exact acceptance、context asymmetry 和 lossless边界有效；当前没有 CTC proposal 的两级终止权、全帧条件/首次失败前缀以及分batch/offload费用。这是具体 workload 分支，不以 ASR 名称映射当作缺口。已读该处完整前后论证、末尾总结/Review notes，以及Ch47结论/Ch49入口；生成表示仍归Ch23，在线调度归Ch46/56，不重复推导。

评分拟 `2+2+2=6`：组件复用+两级仲裁改变 proposal/commit路径，跨 acoustic encoder / LLM runtime，形成可复用条件但不抬为长期普遍基础。因实际 owner 的缺口，已深入受影响机制，不要求读无关参考文献。

## 拟整合正文（尚未写入，等待非作者 PRE）

位置：Ch48效用仲裁分支之后、回到经典target分布说明之前。小标题“声学草稿让验证分成两级仲裁”。

在语音转写中，语言 decoder 更流畅，不代表更忠实于声音，因此先让 decoder 逐 token 完成全部输出虽简单，却可能同时支付串行费用并引入语言先验错误。若 speech-aware LLM 已有经过 CTC 训练的声学 encoder，可以复用其并行帧预测，折叠 blank 与重复标签形成完整转写草稿：所有帧 entropy 足够低时直接接受；否则用一次 causal forward 计算全部草稿位置的条件 likelihood，再接受满足阈值的连续前缀，从首个失败位置继续 AR。前一道门决定是否省去 LLM 验证，后一道门决定声学候选是否值得保留；两者承担任务效用仲裁，而非经典 p/q 与 residual 校正。低 entropy 不证明转写正确，条件 likelihood 超过阈值也不保证 target 分布等价；如果要求忠实复现 target，必须关闭这种仲裁或采用有相应证明的 exact verifier。

这条分支把另训 drafter 的成本换成已有 encoder 的复用，但只能在具备该 CTC 接口的 ASR 模型上成立，不自动推广到翻译、语音问答或实时对话。拒绝以后保留前缀、丢弃 suffix，再承担余下整句 AR；若 verification 与 fallback 分别组 batch，还要结算 acoustic embedding 的暂存与搬运，不能只看接受比例。受限单 H100/BF16、长度排序和 token-budget batching 的作者结果显示，高质量配置平均 WER 改善却不保证吞吐同步上升，高吞吐配置则付出 WER 代价；这不是交互 latency 或服务 SLO 的保证。阈值应按实际语料和风险重新校准，接受率低、搬运太贵、缺乏有效质量评估时，完整 AR 或已有双遍转写仍是合理选择。

本处无 Books 写入、未获 PRE/POST、不授 DAY。
