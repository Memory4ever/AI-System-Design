# 2603.09331 — Reward-Zero必要Source与具体已有覆盖（非作者通过）

[Reward-Zero exact-v1](https://arxiv.org/html/2603.09331v1)。第二包root完整AB准入通过。作者实际§3完整、§4.1完整含Tables1–2、§4.2–4.3完整文字/figure captions、§5；未实际读取曲线像素或Appendix A，不采用依赖这些材料的精确RL速度/最高成功率，不把HTML可读当已读figure。current仍v1/comment under review，未见accepted/纠错/撤回信号。

SUP_EXACT_BATCH2.json原v1Mar10UTC08:07:49，owning arxiv.content/findable DOI registeredMar11UTC02:10:54上界＋official no-advance/deadline最早Mar11BJT08下界同日夹证，原字段待root核；不拿Submitted/Updated/registered单独public。2+1+2=5：稀疏奖励/语言完成感可能错位→caption embedding与CLIP直接图像reward proxy具体比较及终态/进度bonus→需重看进度仪器和实际奖励路径；单reward组件、可重复的代理校准边界，不给成熟cosine/PBRS或普遍RL主张创新分。

## 必要方法与边界

§3原caption/goal cosine Φ，VLM丰富caption/LLM丰富goal，sigmoid(k(Φ−τ)) ×(1+max(0,Φt−Φt−1))加rbase（可Φ或未discount差）。默认τ.7,k10,β.5；实际§4.1后续RL改为CLIP-direct Eq5：.7sim(image,goal)−.3sim(image,initialframe)，不是§3文字embeddingpipeline。departure惩罚可以奖励离开初态但不独证朝正确目标，初始观察是episodecondition不是无条件universalreward。hardcodedthreshold/scale与终态goal描述仍要校准，不能采用“无需任何task engineering”或补造caption路径是实际RL的事实。

Eq3 max有kink，§3声称连续且处处可微不成立，但policy-gradient score-function本身不要求reward对Φ处处可微（本书分析）；不据此否认全部RL效果。Eq4附加sigmoidbonus不是γΦ(next)−Φ(current)的telescoping形式，且rbase可Φ/未discount差；不继承§2介绍的PBRS policy invariance，不采用所有最优策略不变的结论。作者未给正式本方法invariance定理，局部数学边界不升级整篇中心Disputed。停在原公式与直接反侧，不展开无关传统PBRS证明。

## 实际可采用的评价

§4.1 only6successful ManiSkill episodes/5env、24frames/18forward transitions，初稿figcaption写2–4frames而正文/表全4，采用Table1具体人口。仅成功轨迹/forwardkeyframes，不能据此说RL episodes总向前或真机retreat/cycle可校准。终态goal而非动作命令，作者明确命令可在0%让caption回声任务语言；evidence-gating模板给“No actions completed”fallback导致0/18与0/6，只是该模板/该6episode负例，不否定所有证据gate。

Table2 CLIP13/18 forward、6/6jump、2/6wholeepisode mono；Qwen2.5VL3B+MiniLM caption progress12/18,5/6,2/6，observeonly12/18,6/6,1/6，gating0/18。说明端点检测与中间单调不同，CLIP比caption多1/18不是大人口普遍优越。定义Monotonicity称pair fraction但Tablecaption列wholeepisodefraction，两者不能当一分母；Spearman定义却无主表数值，不造数字。caption幻觉peg0%“partially inserted”与句编码近似混淆是作者直接分析，不授独立全样本failuretaxonomy。

Table2每frame单A30 CLIP约5ms/caption约2sec，400倍仅该rewardinstrument推理，不是RL训练/控制闭环或相同完整policy延迟。CLIP决定性只指固定该model/config，非整个RL可复现。视觉显著改变较易，fineobject/遮挡较噪，ViTB16更高分辨率只是建议不是实测。

§4.2只有ANYmalC Reach的Fig5/6 caption称2Msteps下曲线均值，不披露本轮采用所需全training model/hardware/precision、并行env、reset/termination、环境奖励怎样混入、seeds/run/CI与反侧曲线值，不把suite/generalization或stablecritic归因写成已核结果。§4.3 β.05/.1/.2 default.1与§3β.5冲突，所谓Eq5 β实在Eq4；频率25/50，完整eval预算/质量SLO未披露。code willreleaseafterpeerreview，本轮未核实现或真机；未来realdeployment不当已完成。拟采用仅上面已读mini benchmark边界，不采用精确训练性能，因此不为曲线/optionalcode另建必需材料hold。

## 已有覆盖的具体owner（不强加Books diff）

唯一owner `MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。actual290–314完整局部/开篇及Ch25/27交接有效上下文复用，530–575可见progress段本輪仅相关段读，完整邻接未假称。现302的2601.06748明确progress差作rewardconsumer、sensor非成功真值、遮挡/错阶段/非单调可奖励错误、sensor/update/intervalsearch与reset费用、proxy回归停适应；561的2601.07060又限定threshold切换与独立readiness、不饱和/早切/费用。它们具体承载本次可采用的“proxy completion不能自证/进度与终态不同/频率阈值必须付费校准”稳定判断。

本次caption-vs-CLIP六episode与一模板负例是对上述边界的有限佐证；§3 activation/默认参数和§4实际reward路径/配置并未足够锁定新的可重用执行合同，因此不把一个不确定recipe强加正文，也不把caption新增错误模式说已有逐项研究。拟Books `已有覆盖`（NC），只复用上述具体稳定论点，日报保留该小人口比较、参数/口径冲突和未采用的universal/完整RL速度。若未来必要精确实现与独立grounding/闭环对照锁定新奖励机制，再定点比较Ch26此处，不重扫其他材料；本轮NC仍需root必要Source/原日期和actual具体owner独核，未授DAY。

实际独核：root已实读v1§3–5必要原证/Eq1–5/mini Tables1–2、原DOI owning/findable与official下界同BJT日字段，以及Ch26 progress reward与threshold/独立readiness两处实际正文。接受5分标准Source及具体已有覆盖，仅采用proxy≠成功、终态/中间非单调及配置频率费用边界，不采用400×完整RL或通用PBRS。无Books新写，不授DAY。
