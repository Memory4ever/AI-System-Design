# 补检16具名贡献的有限准入提案

当前root实际完整16AB/必要decisive校准：12项潜在贡献准入；10090/10168及纠正10582均1+1+2=4贡献后最低关闭Only（不是pre-denominator无贡献删除）。10200具体avatar配方preclose保留。日期核后FastThinkAct09708首次v1公告上界Jan15 10:52:23北京时间在窗前，仅01/16恢复线索；其他11必要审阅与3最低关闭正常落窗，正式追加14。10582原‘无模型’已纠正：V-H/TableXIII/footnote#确有ONNX MobileNetV2，其余RAG/SLM模拟，beta不识别GIL、affinity非真edge，不授E2E。以下原提案/被纠正依据保留，不覆盖本段。

完整v1题摘已实际读，见jan17_category_exactAB.xml与jan17_LG_exactAB.xml。本包不是16篇全文队列；以下只决定准入的新命题，日期/必要Evidence/Books仍分别待核。先提root校准，不自行正式准入。方法切片为同ID的`2601.IDv1-admission-method.txt`，只列所读段；FlowAct/FastThinkAct/WildRayZer/DeFlow题摘潜在增量已清楚，不以实验细节未知前置全文。

## 具体拟关闭两项（不以数量/负面/领域标签拒）

- 10582 GIL：实际IV-D及V-A。beta由thread CPU与wall差构成，没有分离I/O和GIL wait；评价为10ms Python微任务，LLM inference 10–50token/s只作动机，非实际模型/Agent运行路径。EWMA/hysteresis/veto线程池不新增foundation训练/推理或Agent执行适用条件。一般Python事件层类比不足，不授E2E收益。日期无需为此扩恢复。
- 10200 ELITE：实际§3.3/3.4。DIFIX启发的SD-Turbo单步image translation，以avatar degraded rendering+clean face reference训练triplets，再用生成图做TTA；换视角/表情及脸参考是局部合成设置。原新增命题仍是avatar模块组合/速度，方法未建立独立identity hallucination约束、foundation先验失效条件或新的通用生成机制。60x与ID-preservation不自行扩大贡献。

## 值得核验的具体潜在增量（非已确证或长期Books gap）

| ID | 原约束→实际新增命题→可能改变的选择；初分/最低范围 |
| --- | --- |
| 10117 VICL | prompt融合与layout同时训练混淆→冻结fusion/backbone、各layout残差MLP单独适配，选top4后jointFT→核是否值得隔离布局先验与语义重建；2+1+2=5标准。原文held-out test排名选择必须留泄漏边界，不能把layout功能原因视作证明。 |
| 10107 MULTI-VQGAN | all-support融合可能遮fine cues→以similarity把high/low/all分为独立producer层流、all作为consumer query跨层读两支→核context partition与fusion位置取舍；2+1+2=5标准。不把branch数/DRL命名或midlayer假说计机制保证。 |
| 10103 FlowAct-R1 | 连续视频chunk产生误差累积与响应压力→chunkwise diffusion forcing+self-forcing变体→核rollout训练/streaming边界；2+2+2=6标准必要。25fps/TTFF不是贡献证明，精确config待核。 |
| 09708 FastThinkAct | 文本CoT延迟与动作执行衔接→verbalizable latent teacher蒸馏加trajectory preference携带linguistic/visual planning→核compact planning-action接口；2+2+2=6标准必要。早ID不自动判窗外，日期单独核。 |
| 10716 WildRayZer | camera/object动态破坏static多视图一致→camera-only renderer残差产pseudo mask，训练motion estimator并mask token/gate gradient→核pretraining对象从dynamic全图转background completion；2+2+2=6标准必要，不认证动态物理真值。 |
| 10090 DGS | generative distillation只匹配源统计，task难度分布可能失配→pretrained classifier difficulty量化原/生成池，按原10bin scaled distribution后采样→核固定easy/hard采样与task-relative分布匹配替代；2+1+2=5标准。IB是解释不是新信息定理，classifier置信不是真实难度。 |
| 10165 VadR1Plus | 文本格式/风险reward未约束视频证据依赖→预测abnormal删除预测段再生成作正reward，normal删除首尾导致翻转作负reward→核temporal evidence干预reward分支；2+1+2=5安全/设计反证必要深入。PerCoAct模板/三级risk不独立计增量，删片可变人口不授causal真实证据。 |
| 10168 RAG3DSG | 遮挡crop caption聚合传播噪声→对象pointcloud最佳可见view重渲caption，CLIPagreement聚类选可靠子集，低不确定对象给高不确定邻居context→核caption evidence来源与RAG人口分账；2+1+2=5标准。agreement不等校准uncertainty/scene truth，不授renderer去遮挡恢复真实未知几何。 |
| 10491 GradESTC | 静态basis漂移而全轮SVD传basis费用高→残差error-SVD候选与旧basis按coefficient squared norm竞争top-k，只传替换indices/vectors/coefficients→核通信压缩的跨轮状态更新替代，而非普通error feedback改名；2+2+2=6标准并仅必要affected algebra/同步假设，不授任意LLM训练保证。 |
| 10015 CAFEDistill | 把exit当client的相似选择偏向单client、共同backbone冲突→先各client浅exit再同depth相似选择、final-exit teacher权重近似共用→核client×depth联合选择/训练取舍；2+1+2=5标准。代理是参数余弦而非实际gradient oracle，成熟distillation原则不计原创。 |
| 10251 X-SAM | SAM perturbed gradient可能未降top曲率→周期power iteration+平行/垂直分解后修改更新→核SAM适用边界/计算替代；2+1+2=5设计反证必要深入。Eq5/6二阶loss量不等Hessian变化，Eq11 sign factor不能自行修，eigenvector符号/层拼接条件须核。 |
| 10471 DeFlow | flow policy value优化需ODE反传或牺牲iterative生成→冻结/解耦manifold、data-derived trustregion内轻量refiner→核action分布与value优化接口；2+2+2=6标准必要，不以OGBench数字或stable improvement宣传采用。 |
| 09831 PnP-PGD | 非expansive限制与prior mismatch让denoiser-guided推断条件不明→target MMSE/prox重写，Id−denoiser contractive与mismatch条件下受限收敛→核所需denoiser/数据项假设是否可放宽；2+1+2=5必要理论。只该算法条件，不将inverse problem域名当拒因，也不授任意neural score生成保证。 |
| 09926 ProPer | helpfulness/verbosity评分漏initiative的overreach与underreach→explicit/implicit unmet维度预算和独立绝对rubric分别惩两侧→核主动介入评价与覆盖选择；2+1+2=5标准必要。DGA/rerank/RGA成熟组合不独立计增量，GPT5 judge非意图真值；Eq7负alignment项与prose鼓励alignment相反，若采用该算法须受影响深入，不自行补sign。 |

下一步：root具体准入校准后只对准入者核正常v1日期、方法/关键评价/直接反侧；本包清楚潜在增量不代表已支持采用，不自动Books写入。14每日源有限停止不扩，222/189不作逐项关闭队列。
