# 10578 R4-CGQA：最低关闭判断（待非作者）

仅03-13补Mar12 BJT自然日。第三完整题摘/core窄准入与DATE4实际字段非作者日级夹证复用：submittedMar11T09:28:49Z/registeredMar12T02:04:56Z。当前SUP_ABS3_10578.txt题名/四作者/完整abstract/history直接重核，onlyv1、无可见撤回说明；不是以submitted本身作公开。SUP_ADMISSION_DECIDER_MANIFEST_RESULT.json官方 https://arxiv.org/html/2603.10578v1 GET200/223454bytes/UTC2026-10-09T12:52:43.672812Z，SUP_DECIDE_10578.raw/txt本日原件，无需重抓。

## 具体增量与拟最低投入

本文让CLIP内容topK先缩候选，再用现成REIQA质量embedding相似与内容相似等权平均，选一个示例description；未过相似阈值就不给例子。新原文贡献为这个CGQA任务的content/quality配方与3.5k图文描述/QA评价资源，不借RAG、FAISS、Bayes/MAP或hybrid rerank成熟原则准入。拟 Design1+Reach1+Durability1=3：局部两现成feature排序/提示配方1，单CGQA检索负载1，当前数据/模型实现观察1；未额外确立通用检索机制、稳定融合条件、证据校准或可复用部署恢复规则，不借“质量相似不等正确”的成熟约束增分。不是按题名/domain排除、未读/工作量降分或Books有相近主题倒定分数。拟已关闭、不进一步采用Books0，非贡献EX/非新实验已有覆盖，待非作者。

## 最低判断实际原证

直接读§3完整dataset/annotation/split（260–380）、§4.1–4.2 Eq1–13/proxy assumptions、两stream/threshold/prompt（385–1189、Table1后prompt）、§5.1–5.3全部setup/Tables1–4/反侧与§6（1189–1900）。图只文字/caption，未看图像pixels或curve精点，未读另链接supplement/code，也不认证人类一致性/实现/复现；这些不是当前关闭结论的外部阻塞。

15个有gaming/CG经历的受训annotator，每图至少三个salient维度及总判断；3,500images来自wallpaper/game/CGIQA和购买素材，base3190/validation90/test220，validation/test问答由GPT4o依description生成、每类至少5，合>5k。QA总数不是独立图片/人审repeat数；同render/style或near-duplicate隔离、inter-annotator agreement、blind annotation、不同独立人类测量未在该段披露，不能签完整质量真值或跨renderer泛化。Test图本身没有声明进入base library，故不能自动指控retrieval test泄漏。

§4.1从直接utility最优换proxy posterior：view-specific exponential similarity、conditional independence及uniform prior是所设近似，不是实际quality/content独立或fusion能最大化真实回答utility的证明。§4.2 CLIP cosine→FAISS topK；仅候选中REIQA cosine与CLIP等权平均、argmax一个example，threshold低则只query image+question。K是**候选池**不是最终同时给K个描述，不因本文叫two-stream补成双reader/多证据验证；例子描述也不认证query图的质量事实。

§5.1 choice/yesno对GT直接accuracy、free-QA GPT4omini对GT评分；部分Ollama其余A80080GB PyTorch。精确quantization、token长度/batch/latency/全retrieval与judge费用、重复训练/推理seed/CI/全QA每项有效数、评分prompt全文在此必要段 Not Disclosed，不当training-free等零费用或生产更快。

Table1十一VLM局部作者结果均正，幅度从大到小随模型不同；Q&A原始尺度0–5，正文写百分号不能补成accuracy，不能把混合三指标Average当端到端效用。正文说nine Q&A而Table1实际十一行有值，原口径冲突保留，不替作者改人口。Table2 validation中Llava Full yesno59.9低quality-only60.4，Full虽choice59.8/Q&A2.38较好，不能说双路每项稳胜；content-only Llama choice61.0低Base65.3，额外例子可误导。Table3 Pixtral多图choice68.5低Base70.8，但yesno71.6高Base68.3；multi-image+R4与text-only R4各取舍，非所有VLM multi-image无用。Table4 K1→5较好，K7/9回退；该局部选择不签普遍K5或T.8最优。阈值T1不给description的反退不是校准probability/release gate；caption曲线未实看，只有正文T.7–.9较稳定口径，不补精确曲线值。

## 不进一步采用与owner边界

ROADMAP `AGENT-RAG` Ch76是retrieval/candidate/context选择owner；不是由CG名字新开Ch23/Ch66独立笔记。本次直接完整读Ch76 130–160 query→candidate→fusion/filter→rerank→context及task-relation/候选人口验收、proxy/全费用与回退边界。已有这些长期原则不等本稿新CGQA数据/实验已吸收。本文新增仍是特定内容+质量example-selection与当前CGQA评价配方，未独立支持超出局部用途的新可靠通用机制/部署选择，故不制造Books正文或泛称已有覆盖。

如果新增受控same-description信息预算/随机与相同质量相似候选、多renderer独立人评、明确假设下融合/阈值选择和全费用的可复用新条件，可以定点重开该新增命题；本次不为这些未来可能性扩supplement或另实验。当前不formal，需非作者核身份/date有效复用、实际新增评分与具体最低关闭理由，不授DAY。
# 后续实际非准备者最低裁定

mar13_admission_review原件两stream/topK→单description/threshold、Tables1–4正负侧与actual新增独核，1+1+1=3、不进一步采用Books0 PASS见SUP_INDEPENDENT_MINIMUM_10578.md；root已读该独核并许可formal第30项。准入/date有效、不改EX/不称新实验已有覆盖，不授DAY。

