# CtD10169：必要学习机制与Ch5窄差额提案

[exact-v1](https://arxiv.org/html/2601.10169v1)；首8准入已独判潜力。拟2+1+2=5标准，具体gap受影响深入。必要原件increment-core-find1、first3-core4、ctd-marr-core5、ctd-method-repo覆盖§2.1–3.3、§4、§5/Table2与单target/Qrc反侧、AppG/J；作者实际读相应内容，不claim整750行或代码复现。新机制不是VQ/STE发明，而是Oracle控制共享单概念多target形成codebook，再消费同接口组合knownconcept的有限学习分工；zero-shot compose也已付第一阶段训练费。

方法：singleconcept targets至少两、共享Oracle concept而非人工无监督自然发现；先以sendertarget平均representation取nearestcode，compose抽预定l个code组合bag-of-words。perceptualagents与communicationmodule分开，任务CE/BCE/MSE与codebookloss同优化；EMA/重启inactivecodes为借用方法，不授唯一语义词典。仅codebook/组成接口与局部迁移被核，不宣称训练期全模型冻结或一般形式语言。§G标注dictionary/commitment名称与常见归属不统一，不抄recipe。

实验与关键反侧：5种数据Thing/Shape/MNIST/COCO/Qrc，30k/1k/1k，compositephrase标签disjoint但knownconcept仍见；五seed Table2。CB对CtD/C-D，GS/QT两阶段未见利好未报告全部；Qrc非compositional pretrainedcodebook由.98降.95、zero-shot .48，COCO弱。单target可保高游戏accuracy而组合metric近随机，不把multi-target条件普遍必要/充分。MNISTzero-shot .89比进一步compose .81好，loss目标可冲突且valcombinedloss选择不同于task-only。Oracle concept数决定词表大小和l；无自然新concept发现、变长/重复词（如11）解决保证。A10040GB单卡、batch10、通常200epoch约10h、model<10MB是作者配置；第一阶段/搜索/多seed/Oracle标注/validation选择都费，无全预算matched end-to-end speed，precision/SLO NotDisclosed，非LLM性能外推。

日期：DataCite SubmittedJan15T08:17:26Z、Updated-v1Jan16T01:28:22Z、正式IDregisteredJan16T02:48:54Z，结合已实际核官方announcement/ID规则，正常无提前公开二界均BJTJan16，非registeredalone。正文明确借用egg_qtc与vqvae-pytorch，代码要contactauthors；轻核actual官方repoREADME SHA304655d...（increment-ctd-gh-readme），仅旧EGG toolkit介绍/EMNLP2019/2021citation，无CtD/decomposition/codebook同全文信号，不把旧artifact当本文早firstevent，未遍历完整commit史。若出现可定位本篇同机制早稿，精准隔离而不搬旧归属。

Owner拟WORLDVIEW-REPRESENTATION Ch5。作者actual读30–115、286–317、359–389、428–442；现有compositionalusefulness及primitivecodebook→frozenexecutor→testlatentsearch、信息存在/读出/使用分责，尚未承载“Oracle控制shared-factor多target先形成单概念接口→先前未见knownconcept组合消费”学习支持域分工。拟仅compositionalusefulness后短一段，不新增paper节、不称人类同概念：限定共享因素训练与组合测试分离、对单target/非组合数据检验、Oracle/l/训练费用和普通端到端基线共存。若独判现owner实际已有该机制，按具体Existing而非强行diff；目前仅PRE提案，无Books写锁/修改/独立通过。
