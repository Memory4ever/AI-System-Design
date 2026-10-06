# 2025-10-15 独立有界补检

Cicero，非作者Euler。2026-10-05T08:54:44+08:00。只因作者既定五个标题页web失败而定点curl恢复，不扩分类或全年全文队列。CL/LG skip900、CV skip600、AR skip25、IR skip100，各show25、max10秒一次，全部HTTP200。原响应为CICERO-arxiv-{CL,LG,CV,AR,IR}.html及headers；实际读取125个标题后停止五页，不追more/all/下一页。这些月目录的标签、排序与提交日不证明全网首次公开窗外或落窗。

只对CL页14个尚未覆盖且可能关联主线的标题取精确v1完整题摘，均HTTP200：CICERO-abs-{ID}v1.html及headers。没有把其余111标题转成题摘或全文队列，也不宣称它们全部独立关闭。以下是贡献潜力校准，仍无官方历史first-public时刻/完全落窗bounds，不评分、不授正面Evidence/Books。

| v1身份 | 实际AB后的增量或关闭理由 |
| --- | --- |
| [DMTD11958](https://arxiv.org/abs/2510.11958v1) | 重复遍历全部层 → cyclic masking与晚层复用、不做post-verification → 解码质量/内存带宽取舍；不等lossless speculation。 |
| [Context-Folding11967](https://arxiv.org/abs/2510.11967v1) | 长任务context膨胀 → branch/fold摘要与FoldGRPO过程奖励 → 状态压缩及任务分解的可学控制分支。 |
| [Conjecturing11986](https://arxiv.org/abs/2510.11986v1) | formalisation测试已给正确conjecture → seen/unseen分离 → 评价输入泄漏与机械/语义核验边界。 |
| [SAGE11997](https://arxiv.org/abs/2510.11997v1) | 通用模拟用户缺业务条件 → ICP与agent infrastructure双向grounding → 评价bug暴露与模拟真实性边界。 |
| [Logical Questions12001](https://arxiv.org/abs/2510.12001v1) | 关闭：形式语言/生成规则与线性算法用于离散数学出题，LLM仅题目难度比较对象；未建立模型能力或系统机制变化。不是因小实验关闭。 |
| [UQ12040](https://arxiv.org/abs/2510.12040v1) | 关闭：AB给既有UQ方法分类与代表方法实证，没有指出具体新控制条件、反证或设计修正；不按综述体裁自动排除。新具体反例到达才定点重开。 |
| [APCE12051](https://arxiv.org/abs/2510.12051v1) | 长context质量/成本 → query语义相似度选input chunks → summarisation局部保留输入与KV成本取舍，不以减少输入等同lossless。 |
| [PACE12110](https://arxiv.org/abs/2510.12110v1) | 创造性人工评价/污染 → parallel association chains及人与模型关联模式比较 → 自动关联指标的构念与人类差异待核，相关排名不证明完整创造性。 |
| [ModalityGap12116](https://arxiv.org/abs/2510.12116v1) | speech/text性能差 → 方向/长度与token alignment干预 → 对齐训练与后验诊断成立边界。 |
| [ParallelSurvey12164](https://arxiv.org/abs/2510.12164v1) | 关闭：AB归纳non-interactive/interactive/efficiency taxonomy与应用挑战，没有具体新机制、预算可比反证或失效条件。不是以Books已覆盖关闭。 |
| [ContinuousScaling12167](https://arxiv.org/abs/2510.12167v1) | latent reasoning确定性 → dropout多路径及PRM/ORM负结果 → pass@N潜力不等可识别正确路径，不能因局部负结果排除。 |
| [TemporalBias12185](https://arxiv.org/abs/2510.12185v1) | audio语义正确不等时间准确 → TBI/MAE及长度、事件、位置控制 → 多模态时间身份与评价边界。 |
| [Segmentation12195](https://arxiv.org/abs/2510.12195v1) | supervised segmentation质量/延迟折衷 → preference-tuned segmentation → 三语言simultaneous translation的目标/时延局部取舍，未证明通用DPO优势。 |
| [HALF12217](https://arxiv.org/abs/2510.12217v1) | 无差别公平性均分掩风险 → harm-tier权重与demographic variants → 聚合权重/人口及部署权限边界。 |

14份完整AB中11潜力、3具体关闭。若作者实际读取并纳入本日，原32 AB加14为46篇；原32潜力家族加11为43（原CPR/MPR一族、nuGPR关闭和FlexPipe/Coral处理不变）。不是43正式候选或Evidence完成。当前每个新增家族均缺first-public，submitted字段只用于身份/发现。

## 七组必要反侧

已实际读取精确HTML原件CICERO-core-{ID}v1.html与headers，按以下章节停，不遍历全部附录。HTML Math双显示不连成数字。

- DMTD11958v1 §2–2.2、3.1–3.2、3.4、5：cyclical refilling恢复缺KV但不验证输出分布；Qwen3-4B SFT约1.5B tokens/一epoch，质量batch32、速度单A100-40GB/随机input1024+output1024/batch1–8不同评价。cycle4为相对基线96.3%、cycle6为82.1%；没有speculative decoding直接实验。不得把无verify与缓存恢复写成同分布/无误差传播保证。
- Conjecturing11986v1 §3.1–3.3、4、5.2：457改写题，seen给gold conjecture；ConJudge仅100人标sample校准，Typecheck只是编译、BEq+可能FN，back-translation+LLM Grader仍可错。错置factorial例子通过Typecheck/Grader却未通过BEq+；13/7题是作者有限结果，不是1313/77或自然语言整体正确证明。few-shot/多采样收益并不一致，不外推Lean-FIRe普遍收益。
- SAGE11997v1 §3.3–3.4、4.1–4.2、5.2、7：shared environment、sentinel/turn budget；低分50sample的94%含bug与74%bug-list overlap只校准该样本，高分50中仍4错误。两agent、五runs；120人标interaction/两annotators仅RAG case，single-goal/one knowledge，未直接比较真实user logs。模拟发现bug不等真实发生率、全检率或购物tool动作安全。
- ModalityGap12116v1 §3.2–3.3、5.3、Limitations：单轮英语合成speech/637283样本，Whisper WER过滤；四模型/two epochs/16 A100训练和VoiceBench4947。sd-qa干预用对应text embeddings（额外信息），Angle projection 6/8改善或持平，Length normalization多数下降；只是post-hoc probe，不等可部署普遍speech修复或因果完备解释。
- ContinuousScaling12167v1 §3、4.1–4.3、5.2、6：仅latent阶段dropout，COCONUT backbone的model-specific latent；GSM8K/MC10、训练平衡1:1、10epochs/单A100。PRM BoN最佳33.36%相对31.08%，低于pass@N42.61%；分类precision与F1有限，固有bias/几何原因是解释假设，不证明所有continuous模型不可能扩推理预算或预算与text可比。
- TemporalBias12185v1 §2.1、3.1–3.2、4：TBI signed mean与MAE absolute不可混称；STARSS22/oracle event classes、无效输出剔除、四LALM与监督SED，长度/循环事件/位置条件不同。40GB GPU而具体型号/precision未披露；§3.2把MAE称bias不建立signed方向，§4单TED片段attention展示与start/end措辞冲突不授普遍因果或架构不可修复结论。不用现场时间精度/部署安全保证。
- HALF12217v1 §3–5、6.1、Limitations、A.4、D.4/D.9：nine domains/12datasets/eightmodels，3:2:1为价值权重；人口prompt变化与sigmoid跨模型标准化是测量设计，不是临床/法律真值。模型集合变更可改变标准化（由D.4/D.9公式推导），遗漏dataset排除的分母不能单独证明不同任务组合可比。Llama3.2的1B/3B与3.1的8B非严格同训练scale隔离；不从排名授部署许可或大模型/推理模型造成公平性变化的因果。

上述7加原13为20必要组实际非作者读取。其余新增潜力仅完整AB，不把它们说成标准/深入Evidence完成。对日期保留项安全隔离的判断成立，但作者仍需同步新增范围及以下来源/理由窄修，之后才DAY回核。

## 作者窄同步

1. 读取并纳入以上14 AB/7必要反侧的身份、具体判断与日期权限；不要只是按数量抄录。
2. Qwen本日Research由Cicero own入口、main与p_research-index恢复；原件已保存。不声称拿到2025历史，也不重抓有效原件。
3. 12190完整AB理由用FIRST所核frame caption/incident/fine-grained组合、ensemble/BlindA-B/CIDEr而无具体设计差额，不能仅以dashcam场景关闭。
4. Google ownOctober是实际page1首12到Oct9、可见2页；不是读了page2。Blog不代Pubs，正确Pubs失败已有效。
5. FlexPipe future conference单独不是错版证据；保留L68的2026 trace与当前v1身份疑点，不用它授性能/日期。

仅这些变化回核，不重读原32题摘/13cores/十四源，也不写共享Books/索引/LEARNING_STATE。新11潜力仍无采用命题，现有0Books提案/写入可保持，不强造NoChange等于全部已覆盖。
