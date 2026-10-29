# 11228 必要 Source 与具体 owner PRE

作者 mar14_supplement，2026-10-09。精确原件 [v1 HTML](https://arxiv.org/html/2603.11228v1)，缓存 `SUP_GATE_CORE_11228.raw`。日期采用 `SUP_DATE_SECOND.md` 中 owning/findable 官方 ID 上界与发布批次下界的日级夹证；不是 submitted/registered 单独当首次公开。完整题摘及决定 core 已由 root 实际准入校准。

## 必要证据与停止范围

实际读 §3.1–3.5、§4、§5.1–5.4 和 §6（B27–151）；标准 Markov 证明不作为新增理论，不读全部附录/曲线。每次独立调用只接当前句子，固定模型、prompt 和 decoding，且不携带历史/记忆：因此固定 kernel 的条件是操作性接口，不是任意 Agent 天然 Markov。固定 greedy 映射可能进入 fixed point/短 cycle；sampling 增加可达表面字符串、延迟 exact recurrence。Literal string recurrence 不等事实确认、语义保持或全部信息停止增长。Prompt alternation 的 kernel 不再 time-homogeneous，除非扩展状态含 schedule；段落在 50 次内整体 exact recurrence 少，不能把句子结果外推。

§3.4 只借标准性质：KL 在同一随机 kernel 下收缩；entropy 只有 doubly stochastic 时保证不减，一般 LLM kernel 无该保证。不能把“更低 KL”“更多不同句子”当正确性。§5.4 无参数更新，与训练生成数据导致的 model collapse 分开。

实证为 BookSum、ScriptBase-alpha、BBC News2024 各150首句，共450 seeds，每条50轮；Mistral-7B-Instruct、Llama-3.1-8B-Instruct、Qwen2.5-7B-Instruct、GPT-4o-mini。比较 greedy 与 temperature .7 / top-p .9；可用 seed 时按 chain 固定，否则 API 为随机 realization。Figure2 一标准差不是受控总体因果保证。有限 prompt 两变体、交替、段落和 roundtrip 对照保留；Google Translate v3 近确定性对 sampling LLM 不是同 sampler 比较。METEOR/ROUGE/BLEU/TFIDF 衡量表面相似，未独立测 semantic fidelity；§6明确 cumulative drift 可并存。硬件、精度、总调用费/生产 SLO未披露，不采用性能或通用安全保证；未核 artifact/未复现。

## 评分与实际 owner 差额

新增受控迭代机制边界：2+1+2=5，标准；具体缺口使受影响 owner/PRE 深入。不是把成熟 Markov 数学另加分。唯一 owner `AGENT-REFLECTION` / Ch80，实际顺读开头基本循环、Stopping Policy连续205–295及typed epistemic stopping，Ch79/81入口和 Ch20 sampler交接。

现正文已经解释无参数更新、可能振荡、verifier/预算停止和表面重写不等 evidence gain；尚未承载“只回送当前输出的固定改写接口→sentence-kernel identity与exact recurrence检测→sampling打破表面回环也不等新增证据”的具体条件。不是因缺论文名而写。建议在 Stopping Policy 的 Runtime 持久化句之后、历史 recheck sensor之前补两段；不改通用 token sampling owner，不把 rewrite 实验外推为有工具/全历史的 Agent。

## 逐字拟正文（待 root 实际 Source/PRE，作者不写共享 Books）

当迭代只是把上一轮输出交回固定模型、prompt 与 decoding，且每次独立调用不携带历史或外部反馈时，可以把当前文本视为状态、整个改写接口视为同一个转移 kernel；这比有工具、记忆和环境变化的 Reflection 更窄。固定 greedy 可能很快进入同一字符串或短周期，runtime 因而可以同时记录表面 recurrence 与独立 evidence delta：前者帮助发现重复调用，不能证明当前答案正确，后者也不能由“文字终于稳定”替代。Prompt、decoder 或 schedule 改变后应重新识别这条状态转移，不能静默沿用固定 kernel 的解释。<!-- source-family:SF-2026-ARXIV-2603-11228 -->

受限改写对照中，sampling 延迟 exact recurrence、产生更多不同表面句子，却没有因此证明语义忠实或事实增长；段落整体重复也比单句少。这是固定 checkpoint 下的 inference-time reuse，不是重新训练生成数据的 model collapse。[作者的450首句、每条50轮实验](https://arxiv.org/html/2603.11228v1)只支持这条有限接口边界；更多采样增加调用预算并可能累计偏移，不能作为无限反思或安全早停保证。需要真实改进时仍应回到独立 verifier、外部 observation 和原有预算上限；缺乏新证据时可以保留原文、停止或升级人工，而不是只为摆脱字符串重复提高 temperature。

PRE 未通过前不写；还需实际独立原证/owner 与写后 POST。不授本日 DAY。
