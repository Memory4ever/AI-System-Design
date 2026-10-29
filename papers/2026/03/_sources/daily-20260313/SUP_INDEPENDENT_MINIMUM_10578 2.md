# 10578 R4-CGQA：非准备者最低关闭复核

复核者：`mar13_admission_review`；准备者：`mar13_supplement`。仅03-13增量补查，补充窗口为2026-03-12北京时间完整自然日。本项独立记录，不改root主ledger、Report、Books或LEARNING_STATE；不授DAY。

## 实际范围与复用

本次实际重读AGENTS、当前RESEARCH_CONTRACT、REPORT_CONTRACTS、统一Prompt、Sources使用说明/Daily组/arXiv主题边界，ROADMAP的`AGENT-RAG`路由、LEARNING_STATE最新路由及03-13 README开头/§5停点。既有完整题摘准入与DATE4非作者日级夹证有效复用：本项已确认Mar12归属，不重开提交时刻或公开时刻。

实际完整读准备包`SUP_MINIMUM_10578.md`，直接对照本日官方exact-v1原件`SUP_DECIDE_10578.txt`：§3数据/标注与split，§4.1 Eq1–7的utility→proxy及假设，§4.2 Eq8–13与单示例prompt，§5.1–5.3/Tables1–4与直接负侧、§6。这里只看文本及caption，不读外链supplement/code、图像pixels、旧版或引用论文。

原件manifest `SUP_ADMISSION_DECIDER_MANIFEST_RESULT.json`实际条目为 https://arxiv.org/html/2603.10578v1 ，GET200，223454bytes，2026-10-09T12:52:43.672812Z，final URL相同。另实际读取`SUP_ABS3_10578.txt`完整题名/四作者/abstract/显示history；其保留官方页面仅显示v1，无可见撤回或纠错说明。该轻量检查只支持保留页可见范围，不宣称遍历所有当前公告。

## 决定性原证

1. **两流不是两个reader或top-K描述同时注入。** Eq9–10为CLIP cosine/FAISS top-K候选池；Eq11–13只在候选中计算REIQA quality cosine，与content cosine各半相加，argmax选一个library image的description。最大融合相似度低于阈值时不给示例，只送query image/question；prompt只使用选中description。K改变候选人口而非最终示例个数，阈值是检索proxy，不是已校准回答正确概率或执行授权门。
2. **Bayes解释保持原资格。** Eq2的真实回答utility最优被Eq3的proxy posterior近似代替；Eq5的exponential similarity、条件独立与uniform prior是建模假设。原文没有证明实际content/quality独立，也没有把该proxy与真实回答utility闭合。无需为关闭结论另求一般质量定理，也不把成熟MAP/融合原则计入本文新增分数。
3. **数据与评价是局部新增，不能擦除正面证据。** §3为3500图、15受训CG/gaming参与者，每图描述至少三个显著维度；base3190/validation90/test220，后两组QA由GPT-4o依描述生成，合计>5k问答不是>5k独立图。§5.1明确choice/yes-no对GT准确率，free Q&A由GPT-4o-mini对GT评分，部分模型经Ollama、其他用A80080GB/PyTorch。Table1实际十一VLM行均有三项局部正向结果；Q&A是五分尺度，正文nine与表十一的口径不一致，不能补成统一准确率或端到端效用。原文没有说test图进入base，故不指控检索test泄漏。
4. **直接负侧限制的是具体配方，不否定所有收益。** Table2 Llava Full yes/no59.9低于quality-only60.4，而其choice59.8/Q&A2.38较好；Llama content-only choice61.0低于base65.3。Table3 Pixtral multi-image-only choice68.5低于base70.8，但yes/no71.6高于68.3，不能认定多图普遍无用。Table4 Llava在T=.8时K1→5改善、K7/9回退，不能认证通用K5。阈值曲线仅复用正文T=.7–.9相对稳定、T=1无description时yes/no下降的口径，未读像素或补精确曲线点。

精确量化、token/batch、完整retrieval/judge费用与服务时延、重复seed/CI等不在本次必要段披露；training-free不等于免费或生产更快。这些限制不被提升为本项外部阻塞，也不用于机械否认局部结果。

## 评分与关闭裁定

**通过：Design1 + Reach1 + Durability1 = 3；已关闭、不进一步采用，Books0。** 新增对象是既有CLIP/REIQA feature的局部等权重排与single-example/threshold配方，加上当前CGQA描述/QA评价资源：设计变化局部，实际受测影响限于这一检索负载，当前支持的是具体数据/模型配置下的工程观察。受测多个VLM不自动把单负载升为跨系统边界；RAG、FAISS、Bayes/MAP、相似度非真值等成熟原则不抬分。

该裁定保留先前潜在贡献准入及实际读过的正负结果，不改成贡献EX；也不是要求本文先证明普遍质量、做全费用实验或公开代码才允许入选。直接原证足够判断新增增量当前止于这条局部配方，没有必要继续附件以完成0–4分最低审阅。

实际对回ROADMAP唯一`AGENT-RAG` owner及Ch76完整125–165局部：现有online retrieval链明确query→authorized candidates→hybrid fusion/filter→rerank→context，已有任务关系、候选人口、proxy/成本/回退边界。这只能定位接口和避免重复成熟原则，**不声称本稿CGQA新数据/实验已吸收，也不以已有覆盖倒定低分**。本项无需PRE、Books新写或POST。

若以后真实新增受控评价发现可改变检索选择的适用边界，或明确融合/阈值条件与可复用部署取舍，只重开该新增命题；本次不为未来可能性补实验、扩图像/附件或建立待全文队列。本项最低关闭复核已完成，日级其余普通工作仍由本日停点管理。
