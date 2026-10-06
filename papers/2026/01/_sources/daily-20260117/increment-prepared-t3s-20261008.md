# T3S10348：轨迹proposal与两个mask consumer

exact-v1 https://arxiv.org/html/2601.10348v1；root完整AB准入校准支持潜力，拟2+1+2=5标准；实际长期差额受影响深入。必要原件increment-t3s-method/eval/necessary/identity/current-find-20261008.json，已实际读§2.3一step干预、§3.1–3.6 Eq3–11、§4.1/4.3–4.5 Tables3–8、AppA transfer反侧、AppE、G预算对照、H1/2 loss-transfer。不是整附件/代码复现；宽库存不作全文任务。

增量：单checkpoint reference confidence阈值不足辨认本设置早更新的干扰集合；先用训练accuracy最低checkpoint θb与初始化θ0的teacher-forced logp差形成离线token proposal。AR把Δc>0位置从CE target排除，但该词仍在历史中；dLLM借同tokenizer家族AR selector，取Δc<−τ集合与random corruption mask做union，改变输入可见条件并重建全部union位置，不是沿用AR排除同一组。Proposal不是reasoning语义真值/因果必要词，AppH明确Other只是轨迹label非semantic。

归因与反侧：BOBA/S1K各200固定prompt、正确teacher trace随机选1，无法生成正确者teacher-specific discard；各16traces温度.6、max32768，训练batch64/LR1e−5/50steps，AIME24/25平均16 evaluation runs，不等16独立training seeds/CI。Table3 T3S优于SFT与inverse−T3S；§4.5/G初始confidence高/低同约20%mask budget对照及checkpoint anchor-only one-step在局部支持轨迹选择，2D gradient sketch不授所有static signals永不分离或两token组不能一般共存。H四subset同data/optimizer/steps，loss-transfer是局部模型/训练目标干扰，不授所有CoT/自然部署mechanism。Teacher mixing50×teacher数总step随teacher数增，不能当纯diversity收益/等总费。dLLM S1K全文、usablecontext16K、LLaDA2Mini20epochs、AR selector代理；τ=.2选5.24%得53.33，τ0选81.36%仅32.92、τ>=.3退步，sharedtokenizer跨model比self弱，不能任意tokenizer/selector推广。

成本：训练accuracy必须gold或可靠自动verifier；最低checkpoint定位/两checkpoint scoring、teacher 16traces、selection pilot与正式train/threshold/回归都费，§3.6仅提议周期监控minimal overhead，无实际matched全链cost/硬件/precision/E2Elatency披露。lossmask不剪完整forward/历史反传；Table6 generatedtokens减少不是diffusionNFE/latency/SLO证书。Bottleneck argmin为已观察轨迹，在线如何判断谷底未给通用停规则，不采minimal overhead推广。

日期/current：increment-datacite-10348原SubmittedJan15T12:45:05Z、v1UpdatedJan16T01:41:29Z、正式IDregisteredJan16T02:53:14Z。依已核官方normalannouncement Jan16UTC01最早+不可提前正式ID的registered存在上界，普通无提前发表条件下均BJTJan16；不是提交/登记单独first-public。当前官方abs实际v2May21，commentsAcceptedICML2026，未见显式撤回/纠错/安全说明；题摘机制与v1一致，版本号/acceptance不触发全diff。可见必要正文仅既有工具/data/baseline引用，无本篇更早项目正文信号，不扩全internet；dated同事件早稿出现再精准重开。

actual owner TRAIN-SFT Ch29，已实际顺读93–148 supervision mask/IG/在线高reference概率门/Focusedview与154–158 corruption分工，以及385–432 distillation/scope邻接。现有131–137高单checkpoint confidence门与genericmask/currentcontext分账，不承载“训练accuracy谷底两checkpoint Δconfidence→监督proposal→AR loss排除 vs dLLM输入union破坏”具体轨迹分支；Ch24已有maskedparadigm拥有范式，不应再把本文目标policy双写owner。拟Ch29在线概率门两段之后、focused-view之前短一段，保原完整verified CE/原checkpoint退路、gold/pilot/阈值与family身份成本、不采用semantic truth/在线谷底保证。当前仅PRE ready，不写Books，待root独核与具体窄锁。
