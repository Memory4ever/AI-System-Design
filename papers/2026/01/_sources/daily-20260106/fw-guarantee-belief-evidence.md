# Jan06：第二批必要原源与当前 owner 判断

精确版本未变时复用本记录；不是日级验收。三完整v1题摘准入由root实际校准通过。日期原字段在date-fields-screened-02.jsonl，合取依据见queries-and-screening；不把registered当公开时刻。

## [FwPKM 2601.00671v1](https://arxiv.org/html/2601.00671v1)

实际读§2/3.1–3.5/4.1–4.3/§6及A/B必要范围。product-key两子表寻址，V按chunk reconstruction梯度写入、K按marginal addressing更新；同row竞争聚合、lookahead与gating是特定配方，不授精确单步记忆。12层/4K训练、两类各5B tokens，PPL串行4K/batch1延续fast state；NIAH500例、五key/value，测试chunk改为整haystack并读1–4遍，不是单遍128K无损。添加memory大增参数，FLOPs相近但实际samples/s更低；hardware/precision/重复不确定性Not Disclosed，不授生产吞吐。

MODEL-LONG-CONTEXT：实际Ch22 630–660已完整承载static PKM→chunk-local sparse fast weights、collapse/aggregation/lookahead、真实效率与session-owned mutable state；本次候选仍保贡献与证据，但无需制造diff。2+2+2=6标准完成；root实际原源必要范围及当前630–660完整sparse可写slots/训练M0-runtime Mt与回退已核，具体已有覆盖通过；不采用Eq20未决符号或理论收敛保证。

## [Probabilistic Guarantees 2601.00641v1](https://arxiv.org/html/2601.00641v1)

实际读§2、3.1–3.4/Algorithm1、§4。固定input/oracle、i.i.d. generation与稳定qTP/qFP是条件；重复存在率不等选择正确率。Theorem3.1的事件是无judged-positive，不是所有输出真的错误；不以fresh context证明独立。Qwen3-4B三短提取、10000 samples/runs及独立synthetic label-flip judge，只验证受控模型，不证明真实LLM judge独立。§3.4 binomial下界ceil(K/2)与strict majority在even K不一致，作者实验odd K；不照抄通用公式。

MODEL-SAMPLING：实际Ch20 331–358/388–407已有selector不拥有acceptance、coverage与相关错误/独立oracle及完整预算。本次保有条件理论证据，2+2+2=6标准完成、已有覆盖正面条件；通用任意低幻觉/独立性断言不采用，不给章内不存在的错误造纠错diff。root实际原源必要条件及当前331–358/388–407核验，具体已有覆盖通过；空judged set/偶数majority不外推。

## [Belief Poisoning 2601.00240v1](https://arxiv.org/html/2601.00240v1)

实际读§3/4/5/6、A2.1/A2.4必要范围。威胁要求可修改profile或memory，reflection写入并反复消费；保护依赖对方身份belief时，污染可改变模拟分配。gpt4o-mini/AgentScope64agent，human只是framing标签；LLM belief probe与human-norm script是作者机制解释，非内部因果识别或真人harm。prototype gate有限对照，不授完备防御；A1 payoff列方向与主文有矛盾，不采用方向性数字。hardware/precision、独立seed/每setting总trial未完整披露，不据此外推发生率。

AGENT-MEMORY：已对读Ch77 65–137与1122–1153、Ch76小结/Ch78开头。现有derived/reflection provenance与safety summary目的限制，不明确保护开启条件的identity anchor与普通belief更新分权。root 实际核本缓存必要原段与owner提案并授窄锁；两段实际写入1136/1138，首源注1681。root再次实际顺读新增及前后共享/safety summary后，非作者POST通过，锁已释放。3+2+2=7安全深入；该单篇不替代Jan06日级Gate。
