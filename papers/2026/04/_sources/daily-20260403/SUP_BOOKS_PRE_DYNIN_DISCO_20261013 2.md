# Dynin / DisCo：实际 owner 差额与单段 PRE

root实际Source6/5通过，日期00007原27与00849 EXTRA。当前Books公共上下文、Ch12输入行/输出读出两段及相邻Ch11/13、Ch23完整reference/identity/AnyID→声学交接已读；各仅申请一段+本人注，不改原论证、不授锁。

## 00007 / MODEL-EMBEDDING / Ch12

文件 `books/part-02-model/12-embedding.md`。现donor共享锚点迁移新增行与readout耦合已有，但没有词表扩展后old/new typed rows在model merge中的来源分责；不是重复Ch11 tokenizer映射迁移或Ch23新depth。

完整左锚：

> 这条边界要求迁移后再验新增 token 的发出行为、原任务回归，以及不同上下文和采样条件，而不是取消旧的 lookup 或所有线性初始化。一个受限攻击实验通过修改 donor artifact 并利用已知 base 几何构造了这种差异；它不证明任意模型对都会受害，也不提供完备防御。后续 fine-tuning 可能抑制异常，额外调整行范数则又改变了被验收的产物。分词和 token-ID 的联合版本交接仍由 [Ch11 Tokenizer](./11-tokenizer.md#vocabulary-adaptation-是-tokenizer-与-checkpoint-的联合迁移) 承担，本章只拥有行几何及其与后续读出的耦合。

右锚现完整“连续输出目标还会改变这组坐标是否可辨识…”段，保其collapse反例和loss/读出全部。之间拟一段：

词表扩展后的model merge也不能把所有行当作同一来源的可平均参数。一条新增speech tokens的有限分支，让embedding与output head的旧词表行取原模型、新speech行取适配stage，再仅对其它同形参数插值；输入行、输出行与token type因此各有来源身份，不能用没有新行的基座去平均新增符号。保旧行仍不等旧函数保持，因为其它层和后续训练会改变读出。[有限stage/merge对照](https://arxiv.org/html/2604.00007v1)恢复部分text/vision能力，却牺牲相对未merge stage的ASR/TTS；共享旧行也平均与全Stage1词表有不同取舍，不授typed-row万能最优。额外stage、merge、重训和回归均计费；行身份、shape或旧新任务不兼容时，保留独立模型、原词表路径与明确的局部适配，不能由保留原embedding行自签零遗忘。<!-- source-family:SF-2026-ARXIV-2604-00007 -->

本人末注一条：`SF-2026-ARXIV-2604-00007` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00007v1)§3.1/4.2/7.1/Table9及必要Table11，2+2+2=6，仅expanded-vocab old/new embedding/head rows与同形参数merge来源分责；保Stage1/shared-row反侧、ASR/TTS退步与全部stage费用，不授零遗忘或全模态最优，未核实现/复现。

## 00849 / MULTIMODAL-REPRESENTATION / Ch23

文件 `books/part-03-multimodal-world-models/23-multimodal-representation.md`。现AnyID primary/aux和identity/attribute双轴已表达reference冲突；缺的是edit prompt中entity名称与reference identity信号争用时，名称给grounder而pronoun给edit条件的具体producer分路。只补此接口，不复述通用多目标取舍。

完整左锚：

> 身份保持和属性变更要分别验收：前者可让评者看多参考，后者只看 primary 与变更说明；只有两轴同优的样本再用于偏好训练，仍会选择性丢掉真实取舍。[AnyID 的有限名人参考对照](https://arxiv.org/html/2603.25188v1)支持这条条件分工，但外部基线只有 primary 且底座不同，去 auxiliary 的某项 element 分数还略高；人评把自然度混进属性一致性，也不是独立几何或身份真值。多参考编码、长序列、描述制备、双轴人审与适配训练都付费；属性冲突、参考污染或质量/预算失配时，保留单参考、完整变更描述和显式属性核验，不由较高相似度或人偏好授权真实身份与物理动作。

右锚现完整“语言响应与声学表达之间也需要明确条件的责任…”段，保intent/strategy/声学全部。之间拟一段：

条件冲突还可以来自编辑文字本身：entity名称既提示身份，也参与要改什么的语义，未必应与reference信号交给同一个consumer。一条受限分支仍把实体名给grounder定位reference，却在edit条件中换为pronoun，再用reference-aware reward重联身份与编辑质量。只做这种分离，identity相似可升而prompt adherence/quality下降；通用image reward又可提高质量而损subject，故不是删名字或叠GRPO就解决全部控制。[有限消融](https://arxiv.org/html/2604.00849v1)支持该条件分路的取舍，attention变化不证明视觉独占或唯一因果，SAM crop与小量人评也限制identity指标。grounder/VLM、偏好构造、reward训练及采样优化均计费；定位或条件失配时，保留实体reference回读、原edit文字与分别验收的identity/adherence，不由更高相似度批准主体或事实保持。<!-- source-family:SF-2026-ARXIV-2604-00849 -->

本人末注一条：`SF-2026-ARXIV-2604-00849` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00849v1)§3.2–3.3/4.1/4.3，2+1+2=5，仅entity-grounder/pronoun-edit条件分路与reference-aware reward取舍；保identity/adherence/IR反侧、SAM/人评人口和全部费用，不授视觉独占/attention因果或万能编辑，未核实现/复现。

两个单段PRE待实际核与窄锁。actual后给root完整邻接/本人注POST，不授全日。

root实际完整两PRE/当前锚通过并授权Ch12/23各单段+本人注。作者逐字写后顺读Dynin Ch12 97–113/107正文+428注、DisCo Ch23 412–423/416正文+1992注，限定diff通过。root随后实际Dynin103–111+本人注、DisCo412–422+本人注 nonwriter POST PASS；来源行/wholefunction和identity/adherence反侧吻合、旧邻接保留，Ch12/23窄锁释放，正式报告已计这2项。不授DAY，旧申请态只履历。
