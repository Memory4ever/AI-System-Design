# OCR2：Jan27 原公开恢复与最小采用包

## 最新层级（恢复后的实际结果）

OCR2 已准入追加1；resume_20260128_audit实际原PDF p1/3–11、p7图5/式1视觉与精确blob身份/Ch23完整邻接/字面PRE通过。root新窄锁后作者写Ch23 415/自身1544；audit实际403–437完整邻接/正文/末注 POST通过，更新自身note后actual轻核通过。窄锁释放，旧hold请求解除；下文待非作者/待PRE/待锁均是历史拟文停点，不再重审。

原旧日期hold解除依据只定点复用root具名检查（同月Jan29 supplement:32）：官方DeepSeek-OCR release diff09eaf52日字段2026/01/27、新repo公开issue1 Jan27读取/运行、原tree16ba51c72bfff2891379d56444380270366fb032含paper。论文家族arXiv2601.20552，不是20522；Jan28 arxiv提交/news不是本次首次公开事件。此新证据重开旧hold，不无理由改原60。

原稿URL https://raw.githubusercontent.com/deepseek-ai/DeepSeek-OCR-2/16ba51c72bfff2891379d56444380270366fb032/DeepSeek_OCR2_paper.pdf 。2026-10-08实际取回本日supplement-ocr2-original-20261008.pdf，921582bytes；git hash-object=d99bcf673675f22f3dfcd9196c1384c818d8cff2，与root树blob吻合，非后来arxiv稿。40s初次部分超时后断点恢复成功，不把部分下载算读。PDF只有15页：作者实际完整题摘p1、p3准入贡献、p4相关query对照、p5–8/§3–4方法训练、p9–11/§5–7 Tables1–4与直接反侧。图5/式1 p7已render实际检查，不依错误文本抽取拼mask。

准入：原固定raster visual prefix不等task reading order → suffix learnable queries与特殊blockmask在encoder生成另一读取接口、只query状态交decoder → 需要把input几何顺序、encoder读出序列与后端AR语义分开。已有QFormer/Cross方向概念不足替具体causal query/visual无反读接口。2+2+2=6，已确认长期表示接口差额而必要深入，不借成熟原理加分。若独立准入通过，本轮新增61=原冻结60+OCR2恢复1，原64不移动。

## 必要 Source（作者实际 STOP，待非作者）

p5–7 §3.2：80M SAM-base+2conv压16×，最后dim896，Qwen2-0.5B LM-style encoder，视觉tokens prefix +等基数queries suffix。式1 mask [onesVV,zeroVQ;onesQV,LowerTriQQ]：visual互相双向且不读query，query读全部visual与自身/前query；queries预置同次masked forward，不是逐query外部采样。仅suffix query输出交3B MoE decoder，非对原patch列表的显式permutation或新增世界观测。global1024→256queries/local768→144，0–6crop总256–1120；跨cropquery/slot不保证唯一semantic correspondence或无损。mBART cross-attention未收敛只作者受限观察，不授所有Cross方案不合理。

p8 §4：OCR占80%，与前代两变化是text/formula/table3:1:1平衡采样、合并layout类别，不是严格固定训练数据。3stage：encoder/lightweight decoder jointNTP约100M pairs/160A100/640batch40K；queryenhance冻结visiontokenizer、更新LMencoder+decoder/160GPU40GB/4stagePP+40DP/global1280/15K；末stage冻结全encoder只训decoder20K。encoder300M→500M/序列内部2m，decoder只n视觉输入≠总计算不增；精度、seed/CI、端到端latency/SLO与总费Not Disclosed。

p9–10 Tables1–3：OmniDocBenchv1.5 1355中英page/9type，87.36→91.09是3.73百分点不是相对3.73%；reading-order ED .085→.057，但Table1该列↑与实际↓矛盾不采方向符号。book文本识别.022→.033、newspaper.131→.139反退；各Rorder局部变好不证明真正2D内部因果或全语义正确。其他模型数取benchmark repo、不等同run config/成本。正文称有限trainingdata改动仍validbaseline，不能将全部提升唯一归causal mask。

p10–11 §5.3/Table4：online userimages repetition6.25→4.17%、PDF3.69→2.88%；作者明确无生产GT，重复率不是准确率/生产安全，未披露log人口/硬件/precision/SLO。§6把genuine2D、多hop长queries和统一音频文本encoder列future，不升级为已实现native multimodality。未核artifact/复现，不扩大全repo审查。

## Ch23 实际比较与逐字拟文（待 PRE / 新窄锁）

MULTIMODAL-REPRESENTATION现Ch23 411–427 Cross query方向→audioquery特权teacher→targetagnostic producer层完整局部已读；现有readout层/同步/producer职责，不含visual双向prefix不读取query、causal query suffix只读出接口。Ch22计算收尾交接/Ch24开篇语义边界复用已读。拟Cross首说明之后、18393之前，仅一段：

Query读取还可以在同一个encoder内形成有序读出，而不只用独立cross-attention：保留双向可见的visual prefix，接等基数learnable query suffix；visual不读取queries，各query读取全部visual与自身及前序queries，最后只把query states交给语言decoder。这个blockmask把原patch几何顺序与learned readout顺序分开，query输出是聚合状态，不是已证明的patch permutation、真实阅读因果或新增观察。[Jan27原OCR2报告](https://github.com/deepseek-ai/DeepSeek-OCR-2/blob/16ba51c72bfff2891379d56444380270366fb032/DeepSeek_OCR2_paper.pdf)的受限文档对照同时改变encoder容量、采样与标签，部分文字类型仍退步；少decoder视觉tokens不消除encoder内部前向与三阶段训练费用，生产重复率降低也不认证准确率。Mask、query集合、crop/分辨率、encoder与decoder版本须共同验收；有序读出失配、密集文字损失或完整成本不值时，保留普通visual encoder/projector、bidirectional queries与原文回读，不从两级causal计算自签一般2D理解或统一模态能力。<!-- source-family:SF-2026-DEEPSEEK-OCR2 -->
