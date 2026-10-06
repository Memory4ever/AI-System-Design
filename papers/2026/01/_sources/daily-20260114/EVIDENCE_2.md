# Jan14 必要证据批次2（具名必要证据与 Books 处置已独立通过）

只有四项已校准的具体增量；不扩大标题库存。原返回在CORE_6_INDEX、CORE_7–11，字段日期在DATE_FIELDS_0。原分保持，未运行代码/复现，不授日级完成。各自arXiv版本条件公开区间均为[Jan13T01Z,registered+1秒)，联合官方no-advance-ID及正常周一20ET公告规则；这不是精确first-public日志。未见确定窗前正文线索，若出现则只重开该归属。

## [MHLA: Restoring Expressivity of Linear Attention via Token-Level Multi-Head](https://arxiv.org/html/2601.07832v1)

2+1+3=6。实际核§3.1–3.2/4.1–4.3、AppC和Table1/2/5/6/7；拟采用的是从单summary改为block-summary bank的表示容量与资源取舍，不是“恢复全部softmax函数”。每块形成S_b/z_b，M×M learned系数为每个query-block混合summary；原文未给由输入重新计算m_i的router，不能称动态content router。Query的phi(q)内积仍有内容依赖，因此普通linear attention完全不能按query reweight的宣传过强。

§4.3/Table1列O(Nd²+M²d²)、state O(Md²)；固定或满足M²≤N等布局时才可讨论随N线性，总是固定小block长而M=N/C时不能沿用该结论。Rank上界min(N,sum_b min(N_b,d))须相应满秩/独立行空间方可达到，不是任务能力保证。Table7增M不保证质量/吞吐单调；视频full-MHLA不在所有指标胜FA，hybrid另有替代与成本，训练/硬件配置不能移成Serving SLO。

子命题隔离：AppC用weighted block-prefix却在当前块输出写tildeS_(i-1)，当前块三角mask与block-transition重混合成本未完整给出，故不采用AR cache精确性/普遍每步常数和全部causal pipeline。NLP正文10B FineWebEdu与AppD 5B SlimPajama人口矛盾保留，不用PPL headline撑采用。两者不否双向/视觉blockbank机制及局部实验。

实际owner `MODEL-LONG-CONTEXT`：[Ch22](../../../../../books/part-02-model/22-long-context.md)，已读444–468单累加器与551–580 rank/feature-order论证。现有段未分“一份压缩矩阵”与“多块局部summary+跨块混合矩阵”；root必要原源和实际owner写前通过，授权rank/feature-order段后至渐进解锁段前2段。实际572/574正文及1263源注已写，明确block-address与content query不同、状态/混合成本、布局校准与dense/单累加器回退；jan01_v3实际顺读545–583及末注POST通过，仅复用root必要源授权而未重新读附件。窄锁释放，不扩AR定理，不等日级Gate。

## [d3LLM](https://arxiv.org/html/2601.07568v1)

2+2+2=6。实际§3.1–3.2、§4 setup/Table5及A6/A7必要对照。Pseudo teacher trajectory只决定mask/unmask顺序，即使teacher最终内容错，训练masked positions仍以ground-truth labels做CE；训练顺序提示不是teacher内容正确性或语义dependency真值。Curriculum noise/window与LoRA训练付成本，noise单独会降低accuracy，合用才局部恢复，不能写独立普胜。

五block状态中fully unmasked还处于stabilizing；1–2轮不用缓存forward并刷新前块，再转completed缓存，另有periodic refresh。已显露token不等可永久复用KV。Dream/LLaDA训练人口与epoch不同，H100 BF16训练、HF single H100/A100 batch1推理；TPF/AUP不是总FLOPs或墙钟，EAGLE3比较target model不同，不授完整成本公平。Dream MATH/MBPP有退步，kernel/vLLM集成是未来工作。

实际owner `MULTIMODAL-GENERATIVE-PARADIGMS`：[Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，已读256–277 masked/commit/window及1474–1505 freshness/reopen。后者已承载提交≠永久KV，因此不再重写generic cache规则；但提交顺序的训练来源与content labels尚未分责。拟mask schedule首段后、资格窗口段前1自然段：order-only teacher和gold content两个authority→同推理计划/训练成本/quality独立验收，必要时短接stabilizing而非列五状态教程；固定提交/完整重算回退。

## [Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference](https://arxiv.org/html/2601.07667v1)

2+1+2=5。实际§4/5/Table2–9及C3运行设置。从Lmin起记录最近Lobs层top-k相关attention的relative variance，以阈值选择何时永久缩小后续prefill token集合；这种rank稳定是代理，不是evidence真值/删除证明。首pass在该层后继续仅selected tokens，早层KV另由SnapKV限预算；two-pass GemFilter则选后从layer0重跑，两者表示/计算身份不同。Full-before-selection与先被预算压缩再选择的信息支持也不同。

Tables不支持全部质量胜/阈值单调，two-pass Llama RULER等有退步；小context selector开销可能使latency更差。H10080GB/HF Transformers/FA2（PyramidInfer eager），batch/concurrency/precision未披露，KV预算不等全峰值memory：pooled scores/rank和额外prefill须分账。B2 .028/.015与实际Table5 .28/.15不一致，不采用细数理论速度推断。

实际owner `INFER-PREFILL`：[Ch43](../../../../../books/part-05-inference-system/43-prefill.md)，已读136–177 sparse selection→Full/Shared cached indices。该段复用每层selector的index tensor，未讨论“选择哪一层开始不可逆缩小后续prefill输入支持”。拟FullShared成本/fallback段后、FlatTokenIndex标题前一段，分选择深度与跨层index复用、one/two-pass与完整输入支持、KV/selector/重跑预算；失败时full-prefill或独立每层选择，不授attention rank稳定=证据充分。

## [Are LLM Decisions Faithful to Verbal Confidence?](https://arxiv.org/html/2601.07767v1)

3+1+2=6，反证相关范围深入。实际§2/3/B1 pipeline及§5限制。以reported confidence c和wrong penalty λ定义回答阈值λ/(1+λ)；PC和normalized regret测动作是否一致于该reported-belief rule，不测真实条件正确率。AUARC排名、ECE/Brier概率校准和acceptance utility是不同对象；外部scaffold按阈值替换动作不证明模型学得内在adaptive policy，更不证明模型“明知但拒绝”。

HLE/GSM128子集与GPQA Diamond、10模型API/open mixture、GPT4o-mini解析/判分，solver不见gold，MC/free-form judge不同；unsupported images跳过，unknown-gold校准排除但coverage另计。单次固定子集、penalty提示及置信报告可能改变人口，runtime/HW和完整API预算未披露；表中高ECE与有限ranking收益不授通用confidence可靠。

具体已有覆盖 `PLATFORM-EVALUATION-SYSTEM`：[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)当前2286–2338：confidence feature≠evidence authority、校准/排名/接受政策及奖罚独立，收益改善不说明模型更知道能力；active/submitted人口与成本政策另分。因此报告保留本次有限行为反证，不追加该局部RiskEval recipe，不声称书已含其PC公式或研究全部结果。root实际§2及B.1必要原源/具体owner对读通过，原6不变，SpecificExisting终处置通过，不授全部附件。

最新实际层同步：d3原6经root必要source/owner通过，已在Ch24:266及1778note落实1段；jan01_v3实际258–276及note顺读POST通过。ASL原5经root必要source/owner通过，已在Ch43:176及506note落实1段；jan01_v3实际156–184及note顺读POST通过。两位非作者范围分账，jan01仅写后不冒称重读root已核原源。两锁释放；本批MHLA/d3/ASL三实际整合、Risk一具体已有覆盖，本日连GPU共4实际整合，仍不等日级完成。
