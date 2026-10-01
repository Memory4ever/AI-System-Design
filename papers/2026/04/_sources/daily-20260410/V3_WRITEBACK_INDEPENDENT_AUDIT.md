# 2026-04-10 Books 写后独立复核

复核者 root；2026-09-26。仅检查下列两处 author apr03 的实际写入与必要官方 PDF v1，不替代日级来源、准入或日期验收。

- `2604.07874v1`：官方 PDF §4.1–4.2、§5、§7 对读 Ch56 的 operator boundary → channel preemption → quarantine/失效通知 → framework recomputation。正文正确区分 page-fault-free 与内容有效，保留 Pascal/Turing 条件、冷却校准与 MIAD headroom 的代价及回退，不采用不一致的 8,054/8,045 fleet 精确数字或普遍 SLO 保证。主张与原文一致，真实正文及 Review notes 可定位。写后通过，未验证 driver/artifact 或复现实验。
- `2604.07815v1`：官方 PDF §4.1–4.2、§5 表格与脚注对读 Ch22 的相邻 timestep 候选复用。当前 query 的 fine selection 消费上一轮 coarse candidates、当前 coarse 为下一轮预取；INT4/低维的是选择索引，不冒充所有 KV 都量化。正文区分有损近似与 dense exactness；GLM 的四项 RULER 排除、batch 6 对 batch 1 的混杂保留在 Review notes。漂移检测/fallback 被明确标为设计建议，不冒称作者已测机制。写后通过，未验证 artifact 或复现实验。

两处均在主 Review notes 之前且与相邻正文自然衔接。本文不宣称整日报告完成。

## 两项表示/蒸馏增量写后核对

root，2026-09-26。重新打开07466 HTML v1 §3.1–3.2/Tables1–3和07467 HTML v1 §2–4/Limitations，与作者apr03的实际两处正文及相邻论证对读。07466原文接口在本轮必要段落与官方PDF身份/机制记录一致，未采后版或未披露代码事实。

- `07466`：Ch29原有byte投影与token映射之后，实际新增训练期辅助输出分支、byte KL/CE及原token CE，并在训练后卸载辅助接口。正文准确区分teacher的byte-prefix条件概率与student只取token-prefix hidden state及位置的并行heads，不伪称逐byte AR或概率无损。十byte监督截断、IFEval退步/任务排序和byte-student损失没有删除。实际增量与上下文连贯，写后通过。
- `07467`：Ch23 semantic/acoustic分责之后，实际新增lexical tone可承载词义、连续特征信息不自动经量化保留及phone粗码+逐帧residual分支。正文没有把phone/tone可探测性当端到端语义保证；保留对齐、语言差异、均值聚合损失、码数非同bitrate和连续feature替代。写后通过，不证明全部prosody或TTS质量。

两项均位于主Review notes前。核对不是实验复现，也不替代Apr10其余候选及日级Gate。

## Weight Decay 与表示可读性写后核对

root非作者对读`2604.07380v1`官方HTML §2、§4–6、§9、§10.4及Ch28新增两段与相邻decay论证。实际正文区分任务行为、线性reader、非线性reader与参数几何，不把probe下降当信息丢失；同checkpoint改变后期decay的局部分支、Table1任务准确率并非严格等价、移除与扰动非同幅及随机对照未配范数均保留。正文在主Review notes前，无普遍grokking因果或frontier配方保证。写后通过，未复现实验，不替代整日Gate。

## Noisy Verifier 写后非作者复核

apr03，2026-09-26：独立对读root所写Ch33相关误差段、相邻trigger失效论证与`2604.07666v1`官方HTML §3–5/6.3、Table1及Limitations。噪声每次重采样与固定可利用偏差、test/completion/group结构、best/final checkpoint分账、模型verifier的precision/accuracy共同变化及主要单seed边界均准确；不采用通用15%阈值或precision普遍最优保证。

提出一处必要收窄：MBPP的三个tests只支持测试合同，不证明完整程序语义。root已修为“按独立测试合同测得的task outcome；测试通过仍不等于完整程序语义正确”，apr03再次实际读取正文确认落实。写后通过，真实SF marker和方法正文在主Review notes前，与原相关误差/可利用trigger逻辑连贯。未复现实验，不替代整日Gate。
