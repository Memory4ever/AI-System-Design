# 2604.22438v1 SSG：否定侧有界独立准入与 Ch72 比较

审阅人：apr20_resume；作者：apr01。本核只读当前 `AGENTS.md`、[研究合同 §3–6](../../../../../docs/RESEARCH_CONTRACT.md)、[作者待核段](V3_SCREENING_NOTES.md#否定侧新发现260422438-水印注入分组待独立准入)、[官方 exact-v1](https://arxiv.org/html/2604.22438v1) §4.1–4.4/§5.1/5.4–5.5、[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 当前 provenance/watermark 相邻正文与 ROADMAP `PLATFORM-SECURITY`。未读全附件、后续版本或旧 408 raw；未改正式日报、Books 或共享 checkpoint。

## 裁决

**恢复为具名贡献候选，建议 2+2+2=6 标准审阅；源→实际 owner 的窄知识缺口成立，Books 建议经日期确认与另一人协调后做 Ch72 最窄 Integrate，而非自动 `Existing` 或泛化 Deep。** 旧 receipt 以“局部模型/优化方法、无可复用 state/data/control ownership”关闭不成立。项目内可保留的命题不是 SSG 名称或单次 TPR 上升，而是：KGW 式 keyed green/red 若只按词表*数量*随机分边，在 code/math 的少数高概率 token 分布中可能使注入前概率质量 `p_g` 接近 0/1，固定 bias 的统计移动接近零；logit 邻近 token 成对 keyed 分边是一条受限注入侧替代。它会改变生成端分组、key/上下文身份及 detector 重放的共同设计选择。当前 Ch72:827–850 已承载“watermark 只是 sensor、低熵承载容量有限、key/模型概率/采样配置必须对应”，且其 CDF 等概率消息区间是**多 bit 编码**分支；没有明确 KGW 单 bit 注入中“等词数不等概率质量”的条件，不能仅凭主题相近判全算法 Existing。System Reach=2 只指 generator partition→detector replay 的真实跨边界，不是联想到其它章节；Durability=2 指此概率质量条件，而非作者 scheme 的普遍最优。

**窄正文若采用，应说：**低熵时先量测有效高概率候选在 keyed 分区中的质量；随机等词数不保证等概率质量。按当前 logits 邻近配对能降低高概率候选同侧的注入失败，但实际 top-k 配对、其余随机、key/context 与 detector 重放须同版记录；最终 verdict 仍是可错的统计证据，不等来源真值或授权。无需搬整套 SSG 配方、TPR 表或“任意低熵保证”，并与已有 CDF 多 bit 分支及 provenance/签名共存。

## 决定性原文与反证

- §4.1 Eq(5)–(6)：`f_ws=(e^δ−1)√[p_g(1−p_g)]/[1+(e^δ−1)p_g]`，`p_g→0/1` 时趋 0。§4.2 Algorithm 1 对 top-k 排序相邻配对，以 `hash(key, pair token IDs, context)` 给每对分绿/红，余下词表随机；§4.3 检测复用 KGW-family 并示范 entropy-weighted detector。排序/重放要取得同版模型 logits，不能把“detector有 key”误当可脱离原 prompt/模型状态。
- §4.4 Eq(7)–(10) 的 `[(1−p1)/2,(1+p1)/2]` 概率质量区间建立在**全词表相邻配对**上，且 `p1→1` 时所得水印强度下界趋零。实际 Algorithm 1 仅 top-k 配对，其余随机，并无同一确定性区间的证明。一个可核的离散反例：概率按序为 `(.30,.22,.20,.18,.06,.04)`，`k=2, γ=.5`；top2 配一绿一红、余下四个中随机取两绿时，可得 `p_g=.30+.20+.18=.68>(1+.30)/2=.65`，也可得 `p_g=.22+.06+.04=.32<(1−.30)/2=.35`。因此只能保原文条件化理论与有限实测，不能把 Eq(10) 当 top-k 部署下界或“极低熵严格正检测”保证。此反例仅反驳该外推，不声称实验代码实现错误。
- §5.1 的原提示、有限 Qwen2.5-Coder-7B/LLaMA-3-8B/DeepSeekMath-7B、HumanEval/MBPP/GSM8K 及固定 `h=1, δ=2, γ=.5` 是受限质量—检测对照。Table 1/2 有 P@1 下降格；同表亦有上升或检测改善，不能说 SSG 总损质量或总优。§5.4 Tables 3/4 在无原始 prompt 的一般提示下 SSG 效果有正有负，例如 Qwen Code EWD HumanEval T@1 43.3→28.0；§5.5 paraphrase 后 TPR 普遍下降、DSMath 鲁棒性弱，均阻止普遍来源认证或抗改写保证。
- §4.2 明言全词表排序每 token 成本高，top-k 为效率折中；§5.3 仅归一 EWD 解码速度，未给可与生产 batch/concurrency/SLO 横比的完整开销。§2 还承认 concurrent WaterMod 有相近概率平衡划分，故本次以*可保留的概率质量边界*准入，不宣称 SSG 是唯一或首个这类算法。

## 状态和核验范围

本核通过贡献准入与 source→Ch72 窄 gap，不替作者确认 04/27 first-public。官方 [abs v1](https://arxiv.org/abs/2604.22438v1) 只给 `2026-04-24T10:55:50Z` submitted；作者笔记的 Updated、DOI created、OAI datestamp 也各自不是首公开单证。04/27 日期 owner 须按本日实际公告/相邻 ID 原始批次链独立确定；未定前正式分母不自动 `35→36`，不能签 Books 写入或整日 Gate。若日期归属成立，先给 root 对共享 Ch72 的最窄写锁，实写后另做非作者相邻正文核；本文件不是 write-after。

按怀疑驱动检查了作者提案的旧关闭理由、与 Ch72 既有 CDF 段可能重合、全词表证明对 top-k 的外推及负面表格。此为**非作者但同模型家族的有界复核**；跨模型二次意见在此子任务未获用户逐次授权，未调用外部 CLI，仍需 root 的日级独立 Gate。
