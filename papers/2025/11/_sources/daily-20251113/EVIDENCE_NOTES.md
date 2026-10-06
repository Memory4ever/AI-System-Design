# 11/13 首批必要证据笔记

仅本日材料。root已准入校准7项；以下是作者实际必要审阅，不是独立Evidence/日期/Books通过。首公开仍需逐项核定，未确认者不进正式当窗候选。原始读取保存于 raw-web-19 至28；仅读必要方法、对照、限制及直接相关附录，不授实现核验或复现。

## [Pairwise Reranking v1](https://arxiv.org/html/2511.07555v1)

5分，必要标准审阅已收束。§3/§4/Table1–4/Limitations：两私有单正确文档语料，975/736查询，最多512 token/doc，四A100；UL2到T5-XL、TopK25到5、bf16、单向比较及单token输出逐步叠加。61.36到0.37秒是组合配置，不是单项算法或端到端RAG SLO；batch/concurrency/尾延迟未披露。Dataset1 Recall@1从0.58降到0.52，不能写“同质量166倍”。§3.6在test set选择prompt，独立调参/验收分离未明确；不采用无损泛化。保留局部质量/成本取舍，Books倾向仅报告：这是指定语料与成熟手段组合的局部测量，不独自改变长期重排机制。

## [Procedural Knowledge v1](https://arxiv.org/pdf/2511.07568v1)

5分，必要标准审阅已收束。PDF§4/Algorithm1、§5–6：相同文件环境、H=100，对比No-TN/Human-TN/LLM-TN；内部步骤由LLM verify，最终用人工脚本验收。TP是简化单目的地43题，另有20题recipe与BW/UM。Human-TN可让20B在局部设置超过120B No-TN，不证明模型规模普遍无用。§6指出No-TN反复读文件而不记notes的harness失败；部分收益可能来自流程/记忆脚手架，不是纯规划能力。手写HTN成本未量化。HTML首屏日期2026-08-24与PDF首页2025-11-12不同，采用精确v1 PDF而不拿HTML日期作公开归属；核心机制与PDF一致处才复用。Books待具体owner比较，不宣称HTN名称缺位是缺口。

## [SCALAR v1](https://arxiv.org/html/2511.07572v1)

5分，必要标准审阅已收束。§3–5、AppendixE/J：连接按integrated gradients排序，逐步消融并计输出KL曲线面积；Staircase共享上游feature切片。activation稀疏不等于连接稀疏。相对分数除以潜在连接数，添inactive features可改善分母；绝对分数又偏小字典，必须双报。GPT2-small三层/三prompt的relative改善与absolute退化并存，不采用“电路普遍更稀疏/因果更可解释”。toy更换DyT以简化Jacobian，不能外推任意LN大模型。Ch5现有标签identity/干预论点已定点读取，但不是本篇交互稀疏机制的具体已有覆盖；是否需补该局部指标接口待root，不强造整合。

## [Orion v1](https://arxiv.org/html/2511.07581v1)

6分，必要标准审阅已收束。§3/Algorithm1、§4/Table2–5、§5：轨迹SFT后GRPO；生成think/query并消费MiniLM检索反馈，推理beam按相关性陈述perplexity剪枝。BRIGHT同1.2B Base/SFT/GRPO nDCG=.104/.207/.212，主要质量差来自SFT，RL额外差较小；ranking先恶化后恢复是回退proxy，不认证真实反思。FEVER输给专门检索器，一部分baseline数字来自原论文。没有实际latency数据；beam、retriever与teacher轨迹成本不能由参数比例替代。只采用静态检索任务上的策略学习分支，不采用200–400倍运行收益或生产可靠性。

## [Output Drift v1](https://arxiv.org/html/2511.07585v1)

6分，必要标准审阅已收束。§3/Table3–5：三任务、T=0/.2、concurrency1/4/16、每条件16次，edit-distance identity与citation/数值invariant分开。Qwen/Ollama对比Granite/watsonx同时换模型/后端；云内多模型也未控制架构、precision、kernel/batching与相同model跨路径。小模型16/16的Wilson下界80.6%，不是确定性保证；不采用规模因果或法规合规tier。480总量与多模型/并发分组描述不能替代逐run可核分母，原始manifest未实际取得。Ch20“Random seed与确定性边界”已明确kernel/precision/runtime/model等共同条件；这是具体已有覆盖的候选处置，仍待独立确认，不新增法律判断。

## [Private-RAG v1](https://arxiv.org/html/2511.07637v1)

实际拟采用差额是文档级持续发布的selection/accounting接口，评分修为2+2+2=6；不用成熟DP定义支撑Durability3。涉及隐私保证，仍深入必要内容。§3/Algorithm1–2、AppendixC/D：add/remove document邻接，public LLM独立于私有corpus，per-document filter耗尽后停用；预算对通过threshold的全体计费，不仅最终top-k。adaptive bins必须互斥，noisy prefix阈值与RAG分账，停止目标k独立于数据；任意私有quantile不可替换并继承定理。NQ/Trivia各100题低复用时MuRAG好，MQuAKE400相关问时Ada好；这是重叠条件下效用差，epsilon10不是通用安全等级。未核代码或生产动态语料更新。Ch72 DP§已读，现有内容讲unit/composition、sanitized root复用和accountant同构，未承载该threshold前后计费接口。

具体条件式Books提案交root：若日期与必要证据独立通过，在`PLATFORM-SECURITY` Ch72现有DP表后/production contract前插入持续RAG分支：查询总数与每文档实际暴露不同；筛选必须保持document-local selection前提，计费覆盖阈值筛选而非只看最终top-k；相关查询下自适应筛选自身付费，耗尽则停止该文档使用并降低utility。不重复DP基本定义、不扩Ch76 owner、不写入epsilon10/攻击未成功的安全保证。此处是实际接口差额，不是缺MuRAG名称；未确认归属前不请求root实际写入。

## [ResearchRubrics v1](https://arxiv.org/html/2511.07685v1)

6分，必要标准审阅已收束。§3–4/Table6–7：101题、2593 criteria、三阶段人工构造；9人对303responses标注。Binary把partial计未满足，MacroF1 .72–.76高于ternary；定点例子改善、LLM扩写降低一致性，支持rubric语义也需版本化校准。mandatory/optional与负criterion分开；长报告相关性不证明冗长致质量或内在架构上限。商业agent具体运行预算/硬件/SLO未披露，不采用普遍排名、35分钟崩溃阈值或跨benchmark均值拼接。Books待Ch66具体rubric论点比较；不因增加benchmark就整合。

## 尚可执行的停点

- 7项首公开：已有精确v1/部分DataCite/OAI，但缺2025官方实际当日公告/list身份，不把一般schedule补造为lowerbound。有限恢复后只隔离不能确认的身份，不扩全文池。
- 追加Project Fetch及5份窄主题拟准入仍待root校准；3D4D已读核心§SystemFramework/Evaluation，待代表性排除校准。
- 14源实际范围/分页/查询日志汇总与官方相关标题有界补检未收束；不是日级Coverage通过。
- 必要Books比较、独立证据/Books复核、V3日报与机器校验尚未完成；实际改书0。
