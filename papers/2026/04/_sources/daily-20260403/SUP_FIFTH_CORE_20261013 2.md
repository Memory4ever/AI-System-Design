# 余项第五批决定性Source

仅有限现有题摘，方法/评价/直接反侧实际已读；拟准入/分数待root原证核，不等Books或日级通过。

root 非作者实际核 QMask00161 §3.1–3.2 not-decoder-input/aux，而非先mask后answer；CI00209 Tables2/5合轴与Llama2反退，两项各6有限Source通过。Refusal00228 §3.1–3.3 freshcontext/empirical label/300×3population及strict/lenient/spotcheck原证均已root实际核，5分Source限定通过。可准备唯一owner/PRE，不由本回执授锁或日级；FGR尚未由这三项继承通过。

## 00161 Q-Mask：拟2+2+2=6

[v1](https://arxiv.org/html/2604.00161v1)§3.1～3.4/4.1/5.1/5.3：mask仅取image/query隐藏状态，不取answer-state；标准AR因果结构下可在answer前计算。实际§3.2明确mask**不是LM decoder显式输入**，是joint mask/NTP监督regularize shared表示，不能照题摘说每次先取得mask再据mask生成。10M同数据/同Stage2反侧CQMD改善Text/InfoVQA但OCRBench831→826；SPI recall升而F1降40.09→35，整体均值升不代表所有grounding更好。R2T exactmatch与T2R IoU.5 greedy-matching分开，unsupported计0会混入接口因素。CQMD153.76M、Qwen2.5VL3B/Qwen3VL2B、64H800、26.7M+22.3M数据，local latency+2.71%缺完整runtime配置不授SLO。新增限制answer-conditioned training mask的可用时点与aux grounding分责，不采用causal inference或mask=真实证据权限。

## 00209 CI steering：拟2+2+2=6，安全深入

[v1](https://arxiv.org/html/2604.00209v1)§3.1～3.4/4.2/5.1～5.4/必要AppendixE：500对concept、200behavior、每三维500synthetic；PCA/probe concept可读不等behavior不泄漏。三个CI方向相加，单轴CONFAIDE反增泄漏而合轴降低，五轴又可能退步；新选择是干预目标不能视单privacy轴，非任意CI三维足够。Llama3.1-8B/Qwen2.5-7B/Mistral7B/Llama2-7B、greedy256、GPT4o-mini judge，NCR不是1−Leak还计refusal/incoherence。Llama2 CONFAIDE α1由23.7→43.3退步，不授跨模型普遍安全。Table1 leak5.0与正文/AppendixE .5及PPI.988冲突，不采用该精确synthetic降幅；仅Table2/直接合轴反侧受限判断。label规范、hidden访问、方向迁移、独立输出评价成本保留，不把解码方向当实际principals授权/法定合规。

## 00228 Refusal introspection：拟2+1+2=5，安全深入

[v1](https://arxiv.org/html/2604.00228v1)§3/4.5～4.6/5：先预测拒答/1–5confidence，fresh-context生成真实回应，再按full/partial refusal/compliance二元归并；300base×3variants，empirical behavior非harm规范真值。高d′仍可bias/poorECE；confidence5筛选Llama仅76.3不是通用98.3routing保证。strict vs lenient拒答definition令Claude/GPT accuracy变化15–32%、排名反转，说明部署sensor必须锁定response标签而非harm词。四model特定API版本；paraphrase样本非900独立base，freshcontext不含对话历史，classifier只100stratified spotcheck/边界缺formalhuman。新贡献局部测量资格及拒答定义反证，不采用安全policy训练导致introspection因果或仅高信任就授权执行。

## 00242 FGR-ColBERT：拟2+1+2=5

root 非作者实际§2–4/Tables1–2必要原证通过：反向document-to-query含Eq4索引记法不自补公式，positive-only bias、110/140M不一致、precompute2×与inline费用已核；2+1+2=5限定Source，可继续owner/PRE，不授新公式或部署SLO。

[v1](https://arxiv.org/html/2604.00242v1)§2～4/必要0.A：late-interaction换document-token对query的MaxSim方向，加residual FFN和sigmoid/BCE提span，ranking原分数保留；positive-only supervision实际偏向总找相关span，不能授no-evidence判定。140query/doc三human annotator、MSMARCO局部F1 64.51 vs62.82非显著胜LLM/真实推理证据；R@50 97.12低ColBERT98。on-the-fly变换不增index而有计算，precompute变2×index；RTX3090 h128/h2=768 top100 5.94ms+FFN.7679ms非productionRAG/SLO。110M/140M正文表冲突不采用245×精确参数宣称。新选择是retrieval同时返回query-conditioned span与index/compute取舍，而非事后LLM extraction；不得把token plausibility当faithfulness、授权来源或断言证据完整。
