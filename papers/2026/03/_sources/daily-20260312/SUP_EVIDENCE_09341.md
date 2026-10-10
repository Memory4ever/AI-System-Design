# 2603.09341 — 结构重排与跨 hop binding 分责

Primary [TaSR-RAG exact-v1](https://arxiv.org/html/2603.09341v1)。实际读 §3.1–3.6/Eq1–27、Table1–4、§4.9–4.10、Appendix E；未复现、未核其余曲线像素或代码。完整题摘与 current/撤回检查复用 SUP_EXACT_BATCH3.json，owning arxiv.content/findable registered Mar11UTC02:11:09 上界与已核 announcement/no-advance 下界同为 Mar11BJT；模板 Woodstock2018/Received2009/XXXX DOI 非发表证据，不构造先稿。

Score 2+1+2=5；具体 query/document 类型与 latent binding 接口可补 AGENT-RAG，不为七个 QA 数据集或 RAG 名称入选。Access 可读，Evidence Experimental；等待独立 Source/owner/PRE，不授完成。

## 必要结论与边界

初始 E5/FAISS top-K0=10 固定池；提取 document triple，Schema.org 粗到细两层 head/tail typing；问题拆成有顺序、显式变量的 triple。Eq16 的结构分数只有 head/tail 类型，relation 在 Eq18 的角色前缀向量 cosine 中，不把它说成关系逻辑验证。Eq20 max triple、Eq21 max/mean 后阈值重排；每步 LLM 回答并将变量加入 binding table，下步替换后重排**同一池**，没有从未检索语料补回 gold 的机制。JSON/temperature0 不认证 triple/类型/绑定正确。

Qwen2.5-7B/72B、7QA、E5+FAISS、K0=10/θ=.3/t=3 是披露条件，未完整给 hardware/precision/length/concurrency/SLO。T1 的7B平均EM35.9与正文37.0冲突，72B主表 Hotpot38.7/2Wiki51.8/Bambo45.6 与消融 full46.2/35.6/45.1不同，未解释协议，不拼成统一提升或唯一组件因果。两层类型相对三层的有限反退、类型/triple错误、错误 substitution 传播可解释代价；§4.9是 gold 已在池内的人工错误子集，不当全部请求失败率。效率图未完整锁配置/全调用成本，不采普遍低延迟或 graph-free 胜所有 graph。完整生成验证仍为未来工作。

## 实际 owner 与逐字 PRE

已实读 Ch76 90–125 的 query/结构分层、可撤销table IR及 persistent map；现有段承载 provenance 和结构权威边界，但没有有序变量 binding 驱动同池逐 hop 重排、及固定池不能补漏的接口。拟在“Structured Retrieval 是可撤销...”原块完整结束后、Persistent Corpus 小节前插入一段，不复制 Ch77 记忆权威。

多跳查询还可把这种中间表示限制在本次已检索的候选池内：将问题拆成带 latent variable 的有序 triple，用 head/tail 类型兼容与角色分开的语义相似共同重排，当前回答暂存为 binding，下一 hop 替换变量再选择证据。这能减少实体混淆，却不把类型匹配变成关系证明；错误抽取或早期绑定仍会沿后续步骤传播，固定池也不能找回最初漏掉的文档。[有限 QA 对照](https://arxiv.org/html/2603.09341v1)中的类型细化有反退，主表与部分消融数字不在已解释的同一协议下，不据此宣布统一增益或端到端低延迟。Triple/类型生成、逐 hop 回答与重排都付费，binding 应保留原证据与可撤销身份，而非取得事实 authority；池召回、类型或绑定不足时，回退原文/hybrid 检索、重新取证或保留 Unknown，由独立答案核验接手，不让顺序执行自证整条结论。<!-- source-family:SF-2026-ARXIV-2603-09341 -->

mar12_independent_continue 非作者实际 Source/date/owner/逐字 PRE 通过；root 实际在 Structured Retrieval 原完整块后窄写单段与本人末注；该 reviewer 另读实际完整邻接、新段及本人末注并回对必要精确原证，POST 通过，窄锁释放。旧块保持，不授 DAY。
