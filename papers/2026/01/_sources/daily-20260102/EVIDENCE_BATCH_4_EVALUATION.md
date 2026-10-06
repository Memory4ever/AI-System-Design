# Jan02 评价/数据预算四项必要证据（必要原源已非作者核；Books待定）

完整v1题摘此前已root准入校准；此处只记录实际必要core/评价/反证，不继承摘要为Evidence。日期原值DATACITE_POTENTIAL，holiday+不能advance-ID联合上界完全本窗；原源当前未显示更早同正文公开。未运行代码或复现实验。

## [OpenForecaster — 2512.25070v1](https://arxiv.org/html/2512.25070v1)

2+2+2=6，标准。实际§3–7/AppendixH；离线月快照同时约束问题合成与retrieval，cutoff不由模型自述取得；发布日期仍可迟于事件发生，训练用min(model-date,pubdate)只是heuristic，test额外查最早resolution。§5 Accuracy+Brier改变低置信正确猜测的reward；只Brier下Unknown约40%、联合约4%为局部行为对照，不是校准=真实不确定性。主要302题test从1000先依grok4.1fast可解性再日期/人筛，selection改变人口；source与train不同但非全世界事件代表。相同retrieval top5×512，非实时search；训练随机0–5chunks。8H100 SFT3epoch约40GPUh，RL5epoch1300steps约1000GPUh；precision/group/完整decode预算未披露。不采“更强预测/AGI”或全模型校准保证；拟仅报告有限合成与reward选择，不把借用proper scoring规则当新数学。

## [Data Efficiency — 2512.24991v1](https://arxiv.org/html/2512.24991v1)

2+1+2=5，标准。实际§2/§3.1–3.3/§4–6，AppendixB/C/D；最低置信10%候选至多2500无标签forward，再32标注的LoRA64梯度两两cosine median预测task AUC，7次重抽、30task留一验证。§3.1的AUC公式是线性n测度的平均，§4描述计算采用data size的log2尺度，两者口径不一致；Fig2的log显示本身不能裁决，**不确定采用唯一AUC测度或据此许诺预算**。其单调最佳可达包络及5000预算内接近human假设不是任意任务sample complexity。power曲线只是从同AUC选择的形状，不能给唯一预算保证。模型间回归系数不能复用，10OOD局部支持且generation F1与accuracy口径不同；MMLU/MedMCQA不饱和时误差升高。2H100用于7/8B、4H10014B，全参最多500step/LR1e-5/有效batch32/2048长度过滤/固定seed，proxy用LoRA非全参训练。成本分析每run固定C/每标签A是假设，非实测部署降本。拟仅报告校准依赖proxy，不替代真实learning curve，Books判断待具体核。

## [Encyclo-K — 2512.24867v1](https://arxiv.org/html/2512.24867v1)

2+1+2=5，标准。实际§3–6/AppendixC/D/E；statement集合→可重抽组合将污染入口与question-instance分开，5seed三模型排序稳定仅局部，不证明巨大组合空间抗memorization。manual3annotators核correct、incorrect仅200sample发现5理由不一致；合成错误/程序组题不自动无错。8–10statement、4–8option、2–4组合，提取正则miss计错；single/多statement/MCQ比较同时改变回答机会，不将降幅全归memory。Table5不同option-position题人口及option-count不同，非paired permutation，不能据各位置accuracy证明无position bias。thinking同权重模式仍3k–5k vs14–1138token，非等budget“纯reasoning”；hardware/precision/temp/max-output未披露。拟仅报告可复查refresh协议及限定，不写“免专家/防污染已解决”。

## [VLN-MME — 2512.24851v1](https://arxiv.org/html/2512.24851v1)

2+2+3=7，设计反证深入。实际§3.1–3.3、4.1/Table2、4.2–4.4及AppendixD.1–D.8。固定zero-shot模型与summary/map agent的CoT变体可下降，不证明所有CoT有害；图上cached四视图/数字candidate/语义caption替代continuous低层导航，仅navigation不评REVERIE grounding。singleA10040GB用于local vLLM，proprietary GPU不等同；precision/temp/输出token与重试/step上限未披露，不当质量-全成本公平排名。

关键反证：D.4说Reflection的Final Decision可触发replan；D.8却说Reflection/Decision只log、不影响control，只extractAction后validate，invalid re-prompt。这是原文控制语义不一致，不能认证实际反思回退已实现或将reflection下降全归context能力。131错误中106loop为受选Qwen map slice，25全local失败hard-negative后另加Qwen3VL oracle/editedinstruction改变能力与人口，不作内部因果。context没超长仅否定纯容量解释，未证明“历史grounding是唯一根因”。拟与Ch26 VLM语义≠闭环控制、Ch80诊断≠修复authority具体论点对读后作Books决定，不追加作者根因叙事。

非作者root实际核四项必要原HTML机制、评价及上述反证；24991的AUC测度冲突按§3.1与§4并存保留。实际处置：25070已有覆盖仅指Ch27 953–957逐transition cutoff、snapshot与timestamp/teacher偏差，联合reward只留局部观察；24991暂缓预算推荐，重开精确AUC实现/澄清与真实learning-curve校准；24851暂缓reflection控制/因果，重开可核执行实现/作者澄清及匹配预算控制。上述三项处置已root核并入README，不把两项争议算正面Evidence完成。24867已在PLATFORM-EVALUATION-SYSTEM Ch66 2907/2909两段及末注实际整合statement-pool/question-instance身份分离；root实际对读2896–2924前后正文与源注POST通过，日报整体验收仍未通过。
