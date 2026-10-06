# Nov22 新训练与消费十五题摘

作者Noether；本轮相关标题中十五份新原abs完整title/AB/comments/history实际逐一读完，精确版本见链接/表；不是全LEARNING54逐篇AB/Methods。每份同名receipt保本轮输入/返回。决定提案ready交Ohm，M继续具体原域，不等日期或全部来源。

| 原身份 | 决定/具体理由 | 限制或决定性最小域 |
| --- | --- | --- |
| [17308v1 SpatialGeo](SUP_AB_2511.17308_20261015.html) | P：CLIP语义对几何有损，hierarchical adapter接vision-only几何与random feature dropping防止只依CLIP的trivial解 | 不授损失的唯一原因/8%或内存数字 |
| [17262v1 SlsReuse](SUP_AB_2511.17262_20261015.html) | M：prompt统一异构function语义＋多级prune/retrieval尚不清相对已有检索的新消费约束 | 只补平台/语言/service属性与pruning如何约束候选，不把110query Recall即新机制 |
| [17027v1 ReVul-CoT](SUP_AB_2511.17027_20261015.html) | M：RAG vulnerability库＋CoT是否仅成熟组合，必要安全域 | 具体retrieval/label泄露与split/evaluator，非全12070数据/所有漏洞修复 |
| [16900v1 AUV](SUP_AB_2511.16900_20261015.html) | M：diffusion候选→Lyapunov critic双约束→LLM外环选择/精修函数，是否有具体消费者与稳定条件 | 必要LLM到critic接口/约束，不能直接授stability/真实控制安全，非因应用场景关闭 |
| [16883v1 PersonalizedRouter](SUP_AB_2511.16883_20261015.html) | P：user/query/model/选择行为异构图，将固定全局cost-quality目标改为个体偏好条件路由 | 1000 simulated users/LLM judge不是1000真实用户，few-shot/收益不普遍化 |
| [16664v1 Nemotron Elastic](SUP_AB_2511.16664_20261015.html) | P：共享嵌套子模型、router/两阶段curriculum，group-aware SSM与异构MLP/depth选择适配reasoning多预算 | 不授所有预算零质量损失/constant memory所有状态，未采用360x/7x |
| [16450v1 FLARE](SUP_AB_2511.16450_20261015.html) | M：message quantization＋container/file streaming只给名，新增相对large-object streaming不清 | 仅补量化边界/容器拆解与接收消费/峰值内存，不扩联邦隐私证明 |
| [16435v1 LDAG](SUP_AB_2511.16435_20261015.html) | P：属性语言替support image元指导，LLM属性多样化＋visual-text prior/MaA应对modal shift | 不授unbiased/所有unseen class，非仅新segmentation指标 |
| [16414v1 EvoRec](SUP_AB_2511.16414_20261015.html) | P：定位偏好改变相关adapter子参数，forget-update控制active-user更新对inactive-user干扰 | 30% LoRA/两数据集不能证明全局不遗忘，不因推荐任务排除具体选择性更新机制 |
| [16324v1 SDA](SUP_AB_2511.16324_20261015.html) | P：用户instruction条件的推理期分布重分配可与训练对齐共存，改变不微调控制接口 | 未授3H效果/harmlessness保证；必要受影响消费者与代价按具体域补，不全8模型实验 |
| [16132v1 Emotion SHAP](SUP_AB_2511.16132_20261015.html) | P：SHAP指导LLM synthetic数据与seed量条件，效用相近但词汇/个人/时间复杂度缺失可修正“效用代表真实性”判断 | 不是responsible标签即安全，未授少数类泛化/隐私保证；局部生成指导/限制待必要域 |
| [16108v1 SkyRL-Agent](SUP_AB_2511.16108_20261015.html) | P：异步pipeline dispatcher＋AST tool影响rollout有效性/训练费用，超越backend互操作名称 | 不将naive async基线或SWE跨任务数值当全服务SLO，框架支持不授复现 |
| [16046v1 JEDIS-LLM](SUP_AB_2511.16046_20261015.html) | P：chunk流式speaker prompt cache在线更新/预注册profile及word-level监督，改变短训长推与speaker identity状态 | 不把offline cascaded对照合并同延迟，不采SOTA/零训练全条件 |
| [15192v2 COPYCHECK](SUP_AB_2511.15192_20261015.html) | P：file segmentation与uncertainty clustering替经验threshold的membership推断接口 | copyright/member真值与可访问信号需必要受影响域；不采用90%/跨模型法律或隐私证明，v2具体修订未知 |
| [15168v2 Selenium Forms](SUP_AB_2511.15168_20261015.html) | C：synthetic/human数据fine-tune生成Selenium脚本并按syntax/executability/field coverage评价，完整AB未给新增执行机制/混杂反证或一般选择条件 | 不是因软件任务/小模型关闭，数据量与比GPT4o高不足准入；日期不影响此C，不扩全数据集 |

本包互斥15 AB=10P4M1C；13v1/2current。SDA/SHAP/COPYCHECK仅保受限潜力，不直接采用安全/隐私效果；必要原域仍按具体需求继续，不把全部P升级全文队列。与MODEL15/首十不重身份，当前不是日级总算式。

## 当前局部更正

已实际读回Ohm本日§12：15168v2在真实§III-B/IV-C、完整TableII和§V-C/D给出filter对不同模型执行/覆盖方向分离，以及wrapper/input、hidden/disabled、同名跨form错绑。原AB初判C恢复为窄P：可执行训练过滤不认证语义field coverage，也非所有模型同向。复用该真实非作者原域，不冒作者自行读TableII或浏览器执行。只改此identity，不扩全C或全Methods；原初判/依据保留，新增current修订/公开责任。结合[MINIMUM3](SUP_MINIMUM3_20261015.md)四M的3P1C提案，当前本十五应为14P1C/M0，非旧13P2C；该归并尚待Ohm对作者minimum实际核，不预日级通过。
