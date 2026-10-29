# 2603.11243v1 必要证据与 owner PRE

作者 mar14_supplement；首批准入/日级日期已由root独核，复用不重复。评分建议 **2+2+2=6**：CTC encoder复用与信心/likelihood双门构成具体推理分支，跨acoustic encoder–LLM解码接口，受限ASR质量/成本取舍可复用；不因作者leaderboard、模型规模或Books写法抬分。已实际标准审阅必要机制、评价与反侧，未运行实现/复现；独立Source/PRE待root。

## 原文与采用边界

精确版本：[v1 HTML](https://arxiv.org/html/2603.11243v1)，保存 `SUP_CORE_11243.raw/.txt`；取得身份/时间见 `SUP_CORE_FIRST_MANIFEST_RESULT.json`。实际读§1的适用限制、§2.1–2.3/Eq1–7、§3.1–3.5/Table1/Table2/Fig2–5及§4；不以引用/宣传替代正文。`inspect_source.py`仅便于定位原HTML数学alttext，B19、B25–41、B42–68、B71–108可重现定位。

- CTC greedy路径折叠重复和blank为全文hypothesis。Eq3要求**所有frame**entropy低于τCTC才直接接受全文；非平均entropy，也不是标准ratio/rejection sampler。Eq5在因果mask下单次LLM前向parallel计算每个draft token在draft prefix下的likelihood，所有token均大于τSLM即可接受。否则在第一个likelihood≤阈值的位置前保留prefix，之后AR续跑。末式argmax是假设greedy fallback，未建立sampling target-law等价。
- 必须已有CTC训练的冻结acoustic encoder，在projector训练及LoRA阶段仍冻结；只适用于ASR，不支持把相同框架用于translation/QA。作者注1说失败后整个utterance从拒绝点AR续跑；重新动态接回CTC的localDP在batch中低效。低接受率会同时支付验证和较长fallback。
- 这是**改变解码策略的质量/成本分支**。CTC acoustic grounded hypothesis可能比流畅的SLM greedy更忠实，但§3.4明确是作者对互补error/LM bias的解释；Table2几个例子不足以证明完整因果或所有ASR/真实部署。不能以更低WER宣称保持target distribution。

## 评价条件与明确反侧

§3.1：1B granite4.0-nano、440M/16层conformer CTC、37M两层q-former、rank64LoRA；训练90,000h ASR、21,000h合成translation，encoder20epochs/batch256，projector+LoRA3epochs/900k/batch128。训练覆盖部分测试数据的训练分区；GigaSpeech/SPGI/TED未入训练。本文是同一训练资产的decode-policy比较，不是免训练得到新ASR能力。另比较existing2b/8b与两官方模型harness，不能据此给跨架构普遍排序。

§3.2/Table1：单H100、BF16、按音频长度排序的adaptive batch(max50K tokens)；CTC+LLM与AR分两阶段batch，失败utterance的acoustic embeddings在两pass间CPU offload；合并LoRA、单独LLM实例启FA2、只计算verification位置logits。该RTFx是audio duration/processing time的批量吞吐指标，**不是在线单utterance latency、交互TTFT或SLO goodput**。audio/token长度分布、并发、在线到达/SLO：Not Disclosed；无需编造固定batch size。Fig2表示高精度encoder和fallback占主要时长。

高精度τCTC0.7/τSLM0.2；高吞吐τCTC3.0/τSLM0.1。Table1 OpenASR平均AR为WER5.75/RTFx564；高精度5.58/548，高吞吐6.56/2491。因此4.4×约对应2491/564，**质量不是免费**；6.56相对5.75增加约14.1%，不是摘要写的12%relative increase（以新值作分母得到约12.35%，但不能叫相对AR增幅）。不沿用这句宣传。高精度整体RTFx548<564；Earnings22从391降至278、CVEn从954降至716且WER6.52→6.56，直接反驳§3.5“all corpora/no loss”字面强断言。Table1是可用局部反侧，不因此排除机制/删候选。

§3.3/Fig4的拆门消融：去CTC门高精度相近而高吞吐差；去LLM门无法达到最低WER但高RTFx可匹配。本证据支持不同门负责不同Pareto区间，不证明任何校准阈值普遍最优。Table1标two-proportion z-test(p<1e-4/p<.05)，未见配对word-errors的完整计数、多个trainingseed或CI；不把标星外推所有人口显著性。主要采用机制与失败条件，不承诺4.4×生产性能。

## 当前 Books 实际差额与拟稿

唯一owner：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../../../books/part-05-inference-system/48-speculative-decoding.md)。实际读Ch48 `它不是近似替代`→`当Draft可能优于Target`及`Lossless Verification是分布契约`相邻完整段，邻章Ch47开头逻辑paging语义与Ch49章节交接。Ch48现有稿已明确exact vs utility arbitration、放宽接受必须声明质量/rollback；这部分已有覆盖，不新增第二owner或重复公式。

具体差额是**从目标网络已有非AR模态头产生整句draft，按输入confidence直接提交，或以条件likelihood整句verify、prefix fallback**的接口；正文当前只讲通用proposal/utility与self-spec block/earlyexit，未说明这种省独立drafter却引入整句失败成本的分支。若root认为该具体差额值得写入，建议紧接当前`当Draft可能优于Target，系统进入效用仲裁分支`的第一段后（其source-family末注前）窄插两段；不改变经典exact sampler。

拟正文（尚未写入）：

> 在带非自回归模态头的模型里，便宜的proposal也可能已经在输入编码时产生。语音识别的一个分支复用冻结CTC encoder：先把逐帧greedy路径折叠为整句文本；只有所有frame的entropy都低于阈值，才直接提交该句。否则让LLM在同一因果前向里计算draft各token在draft prefix下的条件likelihood，逐token均过门才接受；在首个失败点停止接受，并从已保留prefix续跑AR。它省去独立drafter和额外训练，却不是target-law不变的验证：输入confidence拥有一条绕过target的路径，likelihood阈值也不同于ratio acceptance和residual correction。
>
> 这条分支的合同是ASR误差与批量处理成本，而非复现LLM原输出；流畅的target输出也可能较不忠实于声学证据。两个门分别控制直接接受和较保守的verify，校准必须覆盖当前语言、噪声与utterance长度。失败后仍要支付整句verify与余下AR的成本；低接受率、在线单句延迟目标或没有合适CTC头时，普通AR仍成立。单H100/BF16、按音频长度排序并将verify/fallback分批的结果，只支持该批量配置下的局部Pareto取舍；较低平均WER不保证每个语料都更准或更快，不能把RTFx提升读成无损或在线SLO认证。

拟Review note仅来源/证据界限：`2603.11243v1 §2.1–2.3/Eq3–7和§3.2–3.5/Table1支持CTC复用的lossy ASR分支；highRTFx质量回退及highAccuracy语料吞吐回退保留，未核代码/复现/在线SLO。` Books窄锁仍需root，未写任何共享正文。
