# Morphemes Without Borders 2603.15773：必要反证与具体已有覆盖

作者 resume_mar18；日期/首批准入复用 root 的本日夹证校准；本文件不授独核或 DAY。2+1+2=5，评分对象是结构 alignment/fertility 不能代签 productive behavior 的局部反证，不因 Arabic 范围排除、不把成熟原则本身计高分。

[exact-v1 PDF](https://arxiv.org/pdf/2603.15773v1)必要 §3.1–3.3、§4 Tables2–3、§5/5.1（文本 L145–545、651–698）已实际读；未遍全部 qualitative appendix 或核代码/复现。七模型 tokenizer 的 corpus/architecture/training/optimization 不同，不能识别 tokenizer 的独立因果。ATB3/BOLT Egyptian 清理后去 diacritics，使仅由元音/gemination 表现的差异不可观察；fertility、boundary F1/precision/recall 与 whole-morpheme coverage 是不同统计，后者容许更大 token 包住整个 morpheme，不等 productive understanding。

行为测试是13 patterns的130 unique real root-pattern forms，不是130 real roots；nonce为20合成roots×5 patterns=100组合，人工核验有限 root/pattern 组合而非所有 Arabic。best-selected 一致 prompt、temperature .6，但 GPT/ALLaM max_tokens8、其余80，输出包含正确词即 lenient 接受，非所有预算/格式一致。具体 API 版本、硬件、precision、重复生成/不确定性与生产 I/O/concurrency/SLO = Not Disclosed。GPT4 高 fertility4.01/低 alignment 与 nonce92%并存，ALLaM fertility1.24/更高 coverage 却 nonce20%；Fanar52%不能写成完全无 nonce 能力。跨模型相关反侧支持不得以结构代理指标单独批准生成质量；不能推出 higher fertility 有益、alignment 永不必要或 instruction reasoning 已被证明是替代机制。训练、instruction-following、prompt selection 与长度预算混杂保留。

实际唯一 owner MODEL-TOKENIZER / Ch11 275–324完整邻接已读：283明确 tokenizer 不能单独决定多语言能力；285–296把 fertility 归成本/可达性，不决定 held-out quality；308要求词表/长度改变后验证模型行为；310–312明确 morphology/allocation parity 不保证 outcome parity，有限语料/seed/任务反侧与简单 MDL/BPE 分支并存。这里承载拟采用的长期论点，而不是仅名字相同。故具体 NC；不声称现文已有精确 Arabic root-pattern 指标或本实验数字，不新增正文/末注来复制案例。请独核必要 Source 与以上实际正文判断。
