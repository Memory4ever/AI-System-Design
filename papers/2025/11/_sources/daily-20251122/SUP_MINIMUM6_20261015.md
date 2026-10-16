# Nov22 最后七门必要决定域

作者Noether。只解决已观察MULTIMODAL/GENERATION_WORLD/LG七M，不追加导航。实际原调用与返回：[HEAD](SUP_WEB_MINIMUM6_HEAD_20261015.raw)、[定位](SUP_WEB_MINIMUM6_LOCATOR_20261015.raw)、[CORE](SUP_WEB_MINIMUM6_CORE_20261015.raw)、[MORE](SUP_WEB_MINIMUM6_MORE_20261015.raw)、[决定](SUP_WEB_MINIMUM6_DECISION_20261015.raw)、[边界](SUP_WEB_MINIMUM6_BOUNDARY_20261015.raw)、[尾](SUP_WEB_MINIMUM6_FINAL_20261015.raw)。下列是作者真实读取域/决定提案，不冒全Methods、图像已视觉核、实验复现、公开日或独立通过。

## MobileVLA-R1 2511.17889v1：M→受限P

实际§III原L96–144：外部模型生成CoT，SFT/Step数据的answer按固定结构映到连续Vx/Vy/yaw及离散动作，GRPO分开方向cosine、离散exact match与格式奖励。这给出推理文本→混合控制接口及分离监督潜力；格式正确不认证动作安全，方向cosine不约束速度大小/动力学稳定，CoT不自动等因果解释。没有采用成功率/实时/真实全场景保证，不因SFT+GRPO组合本身评分，不扩全轨迹/全部实验。

## FT-NCFM 2511.16233v1：M→P

实际§3.1/3.2原L99–140/必要评价L157–170：同下游架构轻训练guide，以LiSSA近似influence，再对topK构造固定语言/动作而改变视觉的有限模板反例；原/反例对d_test梯度内积差经tanh调制基础权重，再消费于分布匹配蒸馏。这是具体选择/权重消费者，不只是“多样数据更好”。d_test用于选择的权限、guide/Hessian近似与模板覆盖须保留，不能把benchmark test已独立或模板反例必然语义最小当事实；正文D→ABCD与表ABC→D口径亦不合并。只保机制潜力，不采用泛化/80%或总费用优势，不读全LIBERO/所有baseline。

## AeroVerse 2408.15511v2：M→具体贡献C

实际§VI/VII原L281–324：2D模型四视图逐caption后拼接、单前视图/路径caption等按任务改输入；运动决策闭环仍future。SkyAgent为InternVL微调CoT，X按perception→reasoning→navigation→planning固定课程联合训练；指标为文本相似/按提示GPT4judge及有限专家标注。实际新增为航空具身任务数据、环境与已有CoT/课程的组合，未给新的动作/状态更新、课程选择规则或一般可归因失败条件，不因UAV/无实验排除。不同模态输入与评判不能证明闭环world-model能力/真实安全；不采用榜单，不扩全城市/图表或为新任务名写书。

## vLLM/TGI 2511.17593v1：M→受限P

实际§3原L121–271、完整Table1 L285–299及§4.5/5.4必要域：A10080GB、FP16、Llama2 7/13单卡及70B四卡TP，vLLM0.6.1/TGI2.3.0，声明warmup100/measurement1000/三次median。所报同模型TTFT与TPOT/总延迟方向不同，是“吞吐优胜不等首响应优胜”的具体局部证据潜力，而非机构/框架名字准入。不同concurrency结果不能拼成同SLO吞吐优势；poisson长度/ShareGPT、调度参数/队列/质量目标披露不充分，Table1与“更可预测尾延迟”的宽讨论也须分开。没有控制实验可将差别唯一归PagedAttention；不采用数字/当前版本推荐、量化结论或生产SLA，不追加全服务框架。

## Hierarchical contamination 2511.17602v1：M→受限P

实际§3.1–3.3/4.1/4.4/5.2及A.1：MinK、embedding/DBSCAN/分布异常合取、CoT ngram结构与paraphrase性能落差分别消费，不是只有相似度名称；扩展逐token去重所漏的评价通路，可保机制潜力。MinK概率/阈值口径及层号前后混写、near-concept/相同解法不等训练成员真值，BLEURT>.7不认证任务等价；受控生成与专家标签不是实际预训练曝光证明。性能cliff还可由改写难度/格式引起，paired test不自动排这些原因。无采用F1/18%/生产可用/“全三benchmark污染已证”，不追所有references/全数据；这不是因污染安全域就自动授强证据。

## Tensor Gauge Flow 2511.17616v1：M→窄P

实际§2.1/3原L102–206必要定义：learned vector field减去scalar加权的tensor-gauge作用，经方向收缩与bundle projection进入同一ODE，具体扩大1-form连接的参数化空间。higher-rank不是更高时间阶ODE；可保生成流向量场参数化潜力，不将fiber定义自动等equivariance/稳定性/表达效率定理或实际改善。未核全证明/高斯实验，不因数学形式或无代码关闭，也不借全部理论保证为其评分。

## Video counterfactual 2505.12114v2：最终具体C（Ohm§22撤销§20恢复）

实际§III-C/IV/V必要域L177–216/225–229/263–287/355–409：固定音频/文本，以StyleGAN inversion→属性边界编辑，另inversion-only控制重建影响；随后输出分布/选择阈值指标与平均预测误差分账。原P提案→Ohm§19接口层C→§20局部恢复P的阅读/轨迹均保留；Ohm§22最终撤销其§20恢复、维持具体C：平均误差与下游选择敏感性分责在本项仍是既有反事实公平审计的域内使用，没有新的基础模型机制或一般成立条件，不能借成熟原则作新增贡献。原新表真实读过不自动建立项目贡献，也不是因日期/成本关闭。成熟控制原则不借作新机制，inversion对照存在但不排编辑共变。classifier只测感知属性转换不证身份/语义不变；阈值刻意突出差异，组别覆盖有限，不授全部人群公平、因果歧视、真实招聘有效性或法律判断。第一印象标签不等工作能力；未实施人物编辑、采用分数或读全图。

七门最终**5P2C、M0**：MULTIMODAL11为10P1C；GENERATION_WORLD12为11P1C；LG7为7P。Mobile/FT/Aero及三LG实际层有效，Interview仅按Ohm§22最终具体C，不重原域。连同FIRST10=10P、MODEL15=12P3C、LEARNING15=14P1C、CURRENT19=14P4C1W、SYSTEM11=7P4C，新100完整题摘层为**85P14C1W**。§20若Interview=P则应86P13C1W而非其旧85/14；最终C才对应85/14，不能用相同总数掩盖不同准入。作者已同步最终决定及算式；此前P/计数均只阶段轨迹。这仅贡献分层，不授85当窗、正式候选、全方法Evidence或Books。四具名安全/理论反侧已Ohm§21、日期归并已§22实际通过，完整six DAY/保存完成态FINAL继续。
