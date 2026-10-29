# I5–I12 完整窄稿，待sole整体PRE

四个既成段I1–I4已actualPOST通过；本稿不是其重审。仅下列新段/各独立marker/各本人注；完整直接两侧由`REPAIR_BOOKS_CONTEXT2_20261029.json`保存，writer另实际自读。未获PRE不写Books，不锁章；所有采用均未实现/复现。

## I5 AGENT-PROMPT / CodeAdapt

文件：`books/part-07-agent/74-prompt.md`。在“固定示例数之后”完整段及marker后，`**Schema**`前。

```markdown
示例本题答对，还不等它适合教下一题。可以先让同一批候选轨迹分别作为其他题的示例，以后续解题效用选择可复用轨迹，而不只按原题reward排序。[CodeAdapt的受限分支](https://arxiv.org/html/2510.20909v1#S3)因此把单题正确、跨题teaching utility和最终任务质量分开；相同base但不同版本的生成器与learner不构成完全同模型对照，数学切片也存在原reward排序更好。效用依赖下游任务人口、示例顺序与consumer版本，不能固化为轨迹本身的永久质量。全候选/失败重试、跨题验证、工具和最终prompt都计费；少输出token不等整条选择更便宜。跨题收益或全费不稳时，保留原题reward、固定少量示例、相似检索与独立答案verifier，不由正确轨迹批准通用教学价值。

<!-- source-family:SF-2025-ARXIV-2510-20909 -->
```

本人末注：
```markdown
- `SF-2025-ARXIV-2510-20909`：Daily2025-10-28补Oct27；exact-v1§3–4/限制必要、2+1+2=5，R14受限Evidence通过。仅跨题示例utility与本题reward分责，保跨版本/AIME反侧与全部候选验证费，不采普遍省时或正确教学保证；未核实现/复现。完整PRE/SAVE/全自读/sole actualPOST按同日canonical实际层，不预签。
```

## I6 PLATFORM-EVALUATION-SYSTEM / clustered missing

文件：`books/part-06-ai-infrastructure/66-evaluation-system.md`。“这个式子只提供直觉”完整段后、“同一题的重复评分还可先保留有限类别计数”前。

```markdown
聚类相关之外，还须先确认哪些响应进入了均值：只平均已观察的message，可能估计的是被选择的人口，而不是全部请求。一个[受限缺失校正分支](https://arxiv.org/html/2510.20928v1#S3)把response indicator、propensity和outcome回归组合为`R(Y-mu)/pi+mu`，再按独立cluster汇总影响量；message等权与用户等权是不同estimand。双稳健仍需要MAR、positivity及相应nuisance-rate、cluster-size和方差条件，不能修复未知MNAR，接近零的propensity也会放大噪声。序列缺失须把历史写进条件，bootstrap不能忽略同cluster相关。OpenAssistant上的缺失是模拟产生，不是生产机制已经验证；缺失模型拟合、历史/标签制备、方差估计与独立敏感性回归都付费。选择机制或支持未明时，保留原观察人口、分层结果和Unknown/敏感性区间，不由校正公式签全流量风险或跨模型迁移。

<!-- source-family:SF-2025-ARXIV-2510-20928 -->
```

本人末注：
```markdown
- `SF-2025-ARXIV-2510-20928`：Daily2025-10-28补Oct27；exact-v1§2–3/5–7必要、2+2+2=6，R14定理条件与模拟人口已核。仅cluster缺失estimand/DR条件/方差单位，保MAR/positivity/小propensity/历史与全费；不采生产覆盖保证或MNAR自动修复。未核全附录/实现/复现，PRE/SAVE/完整自读/solePOST只据同日实际层。
```

## I7 INFER-GPU-MEMORY / xMem

文件：`books/part-05-inference-system/54-gpu-memory.md`。“只测 idle model memory”完整段后、“串行多阶段生成还须分别核容量”前。

```markdown
预测峰值时，tensor存活量还应与allocator保留的segment分开。一条[受限训练分析分支](https://arxiv.org/html/2510.21048v1#S3)先在CPU短跑收集参数、gradient与optimizer生命周期，将gradient释放对齐实际zero_grad，再用两级round/split/coalesce/cache模拟物理段峰值；它不是把所有tensor字节相加，也不是已经在目标GPU量过。CPU与GPU算子、workspace和backend差异仍可破坏映射，baseline容器依赖差异也限制归因。当前证据限singleGPU和有限模型，distributed/FP8不能当现成功能；CPU/RAM、庞大trace、顺序分析及目标硬件校准都有成本。应绑定训练配置、清梯度/optimizer规则、allocator与backend版本，再用真实峰值验收；映射失配或分析不合算时，保实机profile、保守margin和原容量计划，不由零目标GPU分析宣布零代价、准确多卡调度或已兑现内存节约。

<!-- source-family:SF-2025-ARXIV-2510-21048 -->
```

本人末注：
```markdown
- `SF-2025-ARXIV-2510-21048`：Daily2025-10-28补Oct27；exact-v1§3/4.1/6必要、2+2+2=6，R14受限Evidence通过。仅CPU生命周期→allocator segment峰值与真实GPU映射资格，保singleGPU/容器/workspace差额与全部分析费；MCP不是已部署节约，未核实现/复现。完整PRE/SAVE/全自读/solePOST仅本日实际层。
```

## I8 MULTIMODAL-EMBODIED-VLA / PhysVLM-AVR

文件：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。“同样的模型准确率在不同环境”完整段后、“有限动作词库还可先把”前。

```markdown
动作有时不是立即完成任务，而是先取得回答所缺的观察；这要求把“识别当前证据不足”“选择补观察动作”和“消费新证据”分开验收。[PhysVLM-AVR的受限对照](https://arxiv.org/html/2510.21111v1#S3)中，较高的不足识别率仍伴明显较低的最终回答率，simulator揭示问题相关物体的指标也不是最优信息增益或真实安全动作。合成caption/推理数据与少量真实交互轨迹的权限不同，读到遮挡并不证明能规划正确抓取或移动；OpenEQA判分与文字相似度更不能替真实闭环。新增视角/交互、重建与标注、模型训练及补观察后的最终任务回归均付费。遮挡、动作可行性或deadline不合时，保留请求明确观察、可信传感/人工接管和独立controller，不因模型知道“还不知道”就批准物理执行。

<!-- source-family:SF-2025-ARXIV-2510-21111 -->
```

本人末注：
```markdown
- `SF-2025-ARXIV-2510-21111`：Daily2025-10-28补Oct27；exact-v1§3–4/6必要、2+2+2=6，R16受限Evidence通过。仅缺证识别/主动补观察/后续整合分责；保IGR oracle、152k合成与640真实轨迹、最终约39%口径和全费，不采最优动作或闭环安全。未核实现/复现，PRE/SAVE/fullselfread/solePOST仅本日真实层。
```

## I9 MULTIMODAL-GENERATIVE-PARADIGMS / BFM

文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。joint noise coupling完整段及end marker后、`### Velocity 目标的混合表示`前。

```markdown
网络容量还可按积分时间分工，而不让一份大velocity network覆盖所有时刻：把时间切成若干区间，每段训练较小网络，采样只执行当前段；共享预训练语义特征后，还可用轻量residual近似段内变化。[Blockwise Flow Matching的受限分支](https://arxiv.org/html/2510.21167v1#S3)中的block指时间区间，不是token block或KV，单步更便宜却增加总参数、分段模型驻留与边界误差。语义encoder、第二阶段近似训练和基点刷新都付费，FLOPs倍率不能改名墙时倍率；ImageNet类条件结果也不授权文本或视频迁移。应共同保存分段、时间方向、各velocity/特征版本、solver与完整质量/运行费用；边界、近似或预算失配时，保一份共享网络、真实特征刷新与原solver，不由较小active network签全链加速。

<!-- source-family:SF-2025-ARXIV-2510-21167 -->
```

本人末注：
```markdown
- `SF-2025-ARXIV-2510-21167`：Daily2025-10-28补Oct27；exact-v1§3–4/复杂度/限制必要、2+1+2=5，R16受限Evidence通过。仅分时velocity与feature/residual成本；保6段/246NFE、FLOPs与A100实测墙时不同、总参数和单图像域，不采video/T2I或净SLO。未核实现/复现，完整PRE/SAVE/全自读/solePOST只本日事实。
```

## I10 MULTIMODAL-WORLD-MODELS / PhysWorld

文件：`books/part-03-multimodal-world-models/25-multimodal-world-models.md`。“learned world model 用数据学习 transition”完整段后、“显式物理模型的辨识成本还可分成”前。

```markdown
显式simulator还可承担数据工厂，而把快速预测交给另训模型：先从短视频粗到细校准物性，再按语义part的相似关系对物性作相关扰动，生成交互数据训练GNN，最后用真实轨迹在冻结GNN上细调物性。[PhysWorld的受限路径](https://arxiv.org/html/2510.21447v1#S3)避免把每个粒子的随机扰动都当独立，却不证明语义part等于真实材料或参数已唯一辨识。截断仿真梯度、少量真实帧和合成分布均会影响迁移，快速GNN也不继承MPM全部守恒与接触资格；无GT新动作的画面平滑分数不是真实动力学。重建、校准、相关采样、全部仿真与GNN训练和真实闭环回归都付费。物性/接触或长rollout失配时，保可信显式模型、更短预测和真实反馈，不由数据工厂或实时预测名称批准物理安全。

<!-- source-family:SF-2025-ARXIV-2510-21447 -->
```

本人末注：
```markdown
- `SF-2025-ARXIV-2510-21447`：Daily2025-10-28补Oct27；exact-v1§3/4.1/4.3/5必要、2+1+2=5，writer已读支持/直接反侧待sole校准。仅语义相关物性扰动/模拟数据工厂/快速模型再校准分责；保同视频7:3/截断梯度/无GT代理与全费，不采唯一物性或守恒/闭环保证。未核实现/复现，PRE/SAVE/全自读/solePOST仅后到实际层。
```

## I11 MULTIMODAL-GENERATIVE-PARADIGMS / FSG

文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。“引导‘稀有样本’之前”完整JEPA段及marker后、`#### Guidance 可以前移到 Prior`前。

```markdown
运行时guidance也可先校准当前state，再交给unconditional sampler推进，而不只在每次velocity上加同一方向：用条件与无条件路径在一个有限时间区间内的一致性构造fixed-point迭代，并把较长区间/较多迭代优先放在早期。[Foresight Guidance的受限分支](https://arxiv.org/html/2510.21512v1#S3)把区间、算子、强度日程和迭代数拆成四个旋钮；经验golden path不证明全局存在/唯一/可达，局部收缩和流形支持也不能靠名称继承。区间太大或迭代太多仍会退化，NFE与全部条件/无条件求值均付费；偏好/CLIP改善不认证真实语义或同预算墙时。应绑定原模型、time direction、sampler与所有旋钮，独立验终态质量和净成本；收缩、支持或预算不合时，保普通CFG/CFG++、更短区间与原solver，不由多次校准自签全局最优或生产加速。

<!-- source-family:SF-2025-ARXIV-2510-21512 -->
```

本人末注：
```markdown
- `SF-2025-ARXIV-2510-21512`：Daily2025-10-28补Oct27；exact-v1§3/4.1/ablation/限制必要、2+2+2=6，writer支持/反侧待sole校准。仅runtime calibration与denoise分离及区间/迭代预算，保local contraction/heuristic schedules、50/150NFE与全费，不采全局goldenpath或净服务保证。未核实现/复现，完整PRE/SAVE/全自读/solePOST只本日实际层。
```

## I12 MODEL-MULTI-HEAD-ATTENTION / HeadPursuit

文件：`books/part-02-model/15-multi-head-attention.md`。Scalpel局部均值干预完整段及marker后、`## 为什么 head 数不是越多越好`前。

```markdown
选择干预对象还可以先解释一批样本上的head输出，而不只看attention热图：把unembedding中的语义token方向作为固定字典，用多样本稀疏拟合挑出能解释目标概念方差的heads，再作rescaling或sign inversion。[HeadPursuit的受限对照](https://arxiv.org/html/2510.21518v1#S3)用同layer/count的随机head和LogitLens作反侧，支持有限概念选择的差额，却不证明概念只存这些head；改它们还会改变后续间接贡献。字典不全、线性近似和共享语义会带来旁损，增加颜色词也可能降低整体caption质量；毒性proxy下降不认证全部有害输出被阻断。activation采集、字典筛选/拟合、全部干预与任务/安全回归均计费。选择或行为保持未验时，保原head、较弱干预与独立输出验证，不由少数head可控签发语义真值、无损编辑或安全保证。

<!-- source-family:SF-2025-ARXIV-2510-21518 -->
```

本人末注：
```markdown
- `SF-2025-ARXIV-2510-21518`：Daily2025-10-28补Oct27；exact-v1§3–5/限制必要、2+1+2=5，安全干预深入。writer支持/反侧待sole校准；仅SOMP语义字典选择head，保随机layer控制/间接作用/词与分类器proxy、CIDEr旁损与全费，不采唯一因果或安全归零。未核实现/复现，完整PRE/SAVE/全自读/solePOST只本日后到事实。
```

## 作者整体自读

本稿八段全文、八独立marker与八本人注已逐字自读，支持/反侧只复用本日对应必要层；新增差额分别为跨题teaching、聚类缺失estimand、allocator模拟映射、主动补观察、分时velocity、part相关合成动力学、runtime fixedpoint校准和语义head选择，不用一般“状态/控制”词替新机制。PLAN有更早出版原件而退出本日整合，不进入本稿。其余候选Books判断仍继续，不授DAY。
