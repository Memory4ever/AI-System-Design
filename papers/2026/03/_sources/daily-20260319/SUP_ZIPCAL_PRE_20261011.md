# ZipCal 2603.16105：必要原证 / actual owner / 窄 PRE

作者 resume_mar18；仅03-19补BJT03/18。2+1+2=5给不用模型前向的词汇边际覆盖选择及多域组合接口；具体知识差额必要深入，不借成熟校准原则增分。[exact-v1](https://arxiv.org/html/2603.16105v1)必要§3/Algorithms1–2/Lemmas3.1–3.2、§4.1–4.2/Tables1–5、§5与直接Limitations、AppendixA实际已读，支持与关键反侧足够，不遍B全部结果或代码。当前abs为v4/EMNLP2026，Apr/May/Aug普通修订无已见具体撤回/纠错，不扩新版diff；本批公开日期夹证限定复用，Submitted非firstpublic。

## 机制与采用边界

低成本选择先把tokens转小写、移除special tokens及子词标记，逐次最大化尚未覆盖的词汇集合增量，平局偏更多独特词；这是sanitized lexical set，不是语义或activation outlier覆盖证明。正文说random candidate pool而Algorithm1扫描D\S，未核代码不授精确实现；greedy亦不授全局最优。多域先各自抽k形成mk池，再用轻量表示的k-center/farthest选择最终k，随机首点；具体表示模型/距离未披露，不据此认证语义均衡或每域硬配额。O(nk)把窗口w固定，实际O(nkw)；多域还要计mk²d距离，不称联合变量皆线性。

默认128×2048校准；Llama3.1-8B/Gemma2-9B instruct用于下游，相应base用于PPL。Wanda/2SSP25%、GPTQ/AWQ W4A16、LM-harness zero-shot及GSM8k五shot协议分开。COLA兼activation和数据统计，不只是PPL排名。Tables1–4平均改善有逐任务反退，T3 Llama GPTQ平均60.89低于61.02；不采“全设置优于random”或所有任务无损。T5 multi-domain Llama2SSP18.52高于single15.81、Gemma2SSP14.18高于12.41，GPTQ混域亦可反退；词汇覆盖不消域混杂。§5 context/samplebudget改变结果，2SSP偏长窗口，不把样本越多或多域总更好当定律。

10.7s对2443/2790s只curation选择费用，不含剪枝/量化、重构或部署执行；扩展图的model-agnostic一次选择不等完整端到端同硬件公平加速。作者约1200GPUhours不是生产预算认证。具体选择测量hardware/CPU线程、precision/library、repeat/CI、完整I/O、batch/concurrency/output/SLO未披露；English-only，不授其他文字体系/MoE/多模态泛化。未核实现/复现。

## actual唯一 owner

已重载Books背景/学习方法/写法/ROADMAP与本日LS路由；实际Ch49 927–969完整表示/粒度→static calibration→下游接口、Ch48/50首22行交接已读。957确有代表性数据和漂移分责，但没有低成本词汇边际选择及多域候选→最终集合的具体消费者/校准权限边界。soleINFER-TENSORRT-LLM，拟957之后/原下游action DiT接口之前一段，不复制TRAIN-DATA通用数据采集机制。Source/PRE待独核，未获Ch49锁、未写。

### 一段逐字 PRE

代表性校准的第一笔费用发生在选样本时，不必总先为所有候选跑模型前向。一条[受限低成本分支](https://arxiv.org/html/2603.16105v1)先规范词项，再逐次选择对已覆盖词汇集合新增最多的样本；多域时先各自产生候选池，再用轻量表示的距离选择最终集合。这把昂贵的模型相关评分换成词汇覆盖代理，却没有证明覆盖了真实 activation、稀有 outlier 或所有下游能力，也不保证贪心全局最优或固定域配额。校准 owner 须保存 tokenizer 与规范规则、原数据切片、随机起点、域组合及样本预算，压缩 artifact 仍另验真实统计、未参与校准的任务和目标 kernel；混域与逐任务均可能反退，选择阶段省时不是量化执行或完整服务提速。代理失配、任务回归或预算不利时，保留随机/目标域样本、模型相关校准及较高精度路径，不以词汇多样性批准发布。<!-- source-family:SF-2026-ARXIV-2603-16105 -->

### 静态来源注

- `SF-2026-ARXIV-2603-16105` — [ZipCal exact-v1](https://arxiv.org/html/2603.16105v1)必要§3/Algorithms1–2/Lemmas3.1–3.2、§4/Tables1–5/§5与AppA；词汇边际覆盖/多域候选选择只校准proposal，固定窗口复杂度、逐任务/混域反侧和curation-only费用近文，不授activation覆盖/语义配额、全局最优或服务加速；未核实现/复现。
