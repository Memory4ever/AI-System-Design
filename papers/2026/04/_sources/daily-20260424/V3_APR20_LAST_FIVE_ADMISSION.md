# Apr24 最后五项有限准入校准

独立复核者：apr20_resume；作者：apr01。恢复实际重读 AGENTS、当前三合同、Prompt、ROADMAP 与月 checkpoint；仅核 `V3_SCREENING_NOTES.md`“最小消歧收口六”五项的决定贡献/否定段落及必要反证。不是全162项复核、候选冻结、Books采用或日Gate；没有修改共享Books。

## 21461 EgoPoint：5分标准准入通过

[官方v1](https://arxiv.org/html/2604.21461v1) §3.2、§4.5/error analysis、Limitations：模拟指尖射线与遮挡验证给label，真实8名参与者另采1162帧，不能把生成几何标签直接当模型使用gesture的因果证明。400个失败分离 proximal distractor、gesture neglect 与正确grounding后reasoning失败；rescue 57–72.4%仅属于所选失败子集，而非全体反事实干预。新评价分账能核验手势定位与后续推理的不同责任，足够进入受限标准审阅；不因规模/具身局部关闭，也不以11K数量或“近手偏置唯一原因”准入。真实域收益较模拟域小、单轮短题边界保留。

## 21590 AgenticQwen：6分标准准入通过

[官方v1](https://arxiv.org/html/2604.21590v1) §3.3四阶段/Algorithm1、§4：线性trajectory扩为条件行为树后，反推 environment/mock tool、user/mock user、agent/SOP 三种输入，使被选branch成为所需路径；改变的是合成数据的条件支持，不是仅加随机难题或用流程术语改名。失败重写、同Qwen3-235B三次一致及rubric不能成为独立truth或真实工具执行保证。没有匹配剥离双flywheel的独立消融，总体排名不证明各组件因果。此机制分支支持潜在贡献，尚不签Books。

## 21592 Sculpt4D：5分标准准入通过，必须纠正反证行

[官方v1](https://arxiv.org/html/2604.21592v1) §3.2–3.3、Table2、Appendix TableA1：保留全部T×P token状态而稀疏attention连接，首帧全局读权加 `u mod s(d)=v mod s(d)` 的时间距同余规则，不等删除远帧表示；同block index也不保证实际3D点对应。有限可行分支足够标准准入，不因4D任务局部硬拒。

作者notes“移除anchor几何更好”与实际表相反：**无anchor** CD .0986/IoU .3442/F .3375，**Ours** .0972/.3451/.3383；前者三项均较差。PFLOPs分别169.8/186.3。应保的反例是 **conservative schedule** .0968/.3454/.3388/PF233.6，以及 **full attention** .0958/.3466/.3402/PF425.7，几何较好但计算更多。有限no-anchor消融支持该设置中的anchor收益，不证明普遍必要/全局最优；不能用错误反证支持Only。FLOPs不等实测完整SLO，此修正不改变受限准入。

## 21677 GEM：5分标准准入通过

HTML不可取，实际读[官方PDF v1](https://arxiv.org/pdf/2604.21677v1) §2.1–2.3、§3 CUDA实现、§3.2/3.3/3.5/3.6、§4.3/4.4必要表。正半轴 `x^(2N+1)/(1+x^(2N))` 与零负半轴的C^(2N)接合、scale/negative-branch变体是具体算术选择，不仅是换名称。基型/EGEM负半轴仍死梯度，SE才改负分支；高N的CNN退步与BERT/GPT epsilon排序反向必须保留。三seed小BERT 3k步差异小于seed波动，GPT2 124M 5k步不外推大模型普遍胜出。GTX1080Ti/FP32 elementwise CUDA受带宽约束，少运算不证明fused FFN或端到端加速。受限替代可报告，不因小模型/negative证据关闭，也不新增通用activation保证。

## 21766 AUDITA：具体前分母关闭通过

[官方v1](https://arxiv.org/html/2604.21766v1)完整题摘、§3.2–3.3、§5/Table4/§5.1–5.2：人写知识密集音频trivia、语义类型/属性匹配且作者复核的MCQ distractors、IRT共同构成有价值资源，但该贡献尚未分离改变本项目评价选择的新控制条件。实际确有question-only/transcript/raw-audio消融（free QA .0001/4.26/8.86，MCQ 1.29/7.05/15.65）；不能沿“无消融”旧理由关闭。知识缺失78.23%的错误分类、低于chance和转录丢失非语言cue，不分别识别知识/perception/时间必要性，更不证明唯一systematic miscalibration机制。关闭基于当前无新增适用边界，不是音频领域、benchmark名称或单纯“成熟组合”；保留原有效数据/实验，不否定资源学术价值。

## 有限结论

四项潜在准入与一项具体关闭成立；21592须先修正定点反证才可沿用其审阅笔记。未核其余157项，不评估本日首公开/全源覆盖，不给实际整合或日报完成背书。
