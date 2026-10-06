# 最小核心后的具体准入判断（待独立校准）

原始完整题摘不重复读；核心只读能决定准入的段。本表判断不代表证据或Books自动完成，不因数量/审阅费时裁剪。

| ID | 最小核心 | 决定与实际差额 |
| --- | --- | --- |
| 12995 | [原段](./decisive_min4.txt) §3.2.2/4.3 | **拟准入**：不是graph标签+普通clip名称；SCAE按正确/错误样本分层，辅助reward在正确层只许非负bonus、错误层只许非正penalty，公式保证advantage符号不会被structure reward翻转。Qwen3-8B相同RL设置去SCAE三bench退步；只支持该sign-priority分支，不保证无reward hacking。2+1+2=5建议标准。 |
| 12247 | [原段](./decisive_min3a.txt) §4.2/5.2/AppA.2 | **拟准入**：AppA.2匹配低confidence-bin、每step只额外提交一个token；planning pool为空回退Random以匹配commit数，平均confidence差≤.01，planning优于随机的局部质量/NFE支持“先提交哪个低confidence anchor”而非更多commit或高confidence偏差。双filter验证未来highconfidence top1不flip不是semantic真值；NFE非runtime。2+1+2=5。 |
| 12719 | [原段](./decisive_min3a.txt) §3.3/4.4 | **拟准入**：budget先定LCHA/SSA数，再学习相同block counts的resolution切换布置，不只是linear+local+DP组合。匹配trainingcompute/schedule的attention消融与same-setting hourglass对照，128→256head dim反而FID/FVD更差；iPhone16ProMax latency含shape条件、fullattn OOM不证明其质量无损，fullattention质量仍更高。候选仅布局与资源分支，2+1+2=5。 |
| 13976 | [原段](./decisive_min2b.txt) §3.5/3.6/4.3 | **拟准入**：推理nonCoT本身沿用Aux-Think，不当新增；实际改变是先训练nonCoT取得soft actions再反向约束text/visual/multimodal CoT模式，共享参数交替优化，去alignment SR0→2.44而ISR2.39→11.01。全四mode不是每个指标优于每个子组合；是mode冲突与deployment路径的局部训练接口，不授内部学会真实世界因果。2+1+2=5。 |
| 12277 | [原段](./decisive_min3a.txt) §3.1/5.3 | **贡献关闭**：明确采用已有shortcut objective的two-half-step self-distill、3DUNet futureobservation+CEM navigation；所选消融验证pretrain/randomtrajectory/anchorinitialization及CLIP/BLIP/SigLIP规划loss的任务效果，未展示不同sampling step在同生成质量下的闭环资源新边界，当前delta是nav recipe。不是因WorldModel/smallmodel整体范围外，也不因latency数字低拒绝有新边界研究。 |
| 13304 | [原段](./decisive_min4.txt) §3.2/3.3 | **贡献关闭**：Qwen3VL30B A3B加三个512px生成初帧，三次repeat碰撞+2.40/轨迹+2.20、遮挡小退步；没有匹配额外image/evidence budget或消融区分explicittrajectory管线与更多视觉线索，不能由textdrift叙述推新可归因因果机制。geometry/volume/deformation/collision一致性作者仍开放；本次只有taskpipeline和增添模拟证据，不据低收益规模关闭。 |
| 13238 | [原段](./decisive_min2b.txt) §3.3/5/7 | **贡献关闭**：六项rainparameters+multiscaleadditive layer及multiplicative localillumination，成熟physicalattack/CMA-ES优化组合；component/regularizer扫点只改变这一合成雨配方ASR，未给区别既有structuredphysical扰动的具体新失效条件。部分CLIP反而低于ITA；未证明realrain或fog/snow，不从天气space名称认定新的长期security边界。保留安全相关原段供复核，不归为访问失败。 |
| 12294 | [原段](./toolprm_decisive.txt) §5.1/5.3 | **贡献关闭**：不同rewardmodel在GTA/BFCL n8 bestof搜索收益与offline准确率相关，低于50%模型负收益；cost按API/Together价格估计，PRM按base价代替实际成本。原AB所称offline/online差异本身未给独立具体新盲区，所选原段只有通用不可靠评分器会误导search与新benchmarkproxy验证，不采用其reliableproxy/production承诺为新增系统原则。 |
| 13243 | [原段](./decisive_min4.txt) §6.2 | **仍定点决定准入**：已发现no_think ARC下输入长不能解释strategy tokenheavy-tail、adversarialdebate最高meancost仅中accuracy，failed集中高cost人口。需§5.1确认同model/evaluator/workflowturn预算，决定是否足以修正“inputlength即可估计MAS成本”的具体条件，而非只重复complexity≠accuracy。 |
| 12179 | [exact-v1 PDF](https://arxiv.org/pdf/2601.12179v1) pp3–11 | **拟准入**：8-layer BabyBERTa masked objective，人工grammar/二元规则分别控制types、exceptions及4/10epochs；heldout words+1000pairs surprisal，跨TP threshold分段回归jump不显著，二元每设置3init。具体反证是type-only N/lnN阈值及quantal学习预测不适用于此模型，重复exposure改变learnability；不否定人类TP或外推LLM。HTML404，PDF可得，图4截图接口失败，未补造点值。2+1+2=5；不是所有human-analogy错误，也未确认Books使用此阈值。 |

以上为过程记录，最新独立校准：12995/12247/12719/13976/12179准入5及必要核心通过；12294/13243/13238/12277/13304贡献关闭均经root实际定点原文复核通过。13243不再待§5.1，12179已进入README必要证据与Only处置且非作者通过。关闭理由仅本次无具体新条件，不授安全/研究价值普遍结论，不额外追与处置无关日期。
