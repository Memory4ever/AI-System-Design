# Activation Watermarking necessary safetySource / sole Ch72两PRE

2026-10-12，[2603.23171v1](https://arxiv.org/html/2603.23171v1)，原2+2+3=7/date25不改；只v1不借当前v3题摘/修订保证。actual必要§3–6/Alg1/Eq4–8/T1–5及D1–2/C威胁人口，B GPU/训练资源实际读；未读全部攻击/图例/实施攻击或复现。

## 独立可采用命题 / 直接反侧

Provider控制微调与内部hidden读取，攻击者只黑盒API、知道算法不知secret seed/方向，不得读activation/gradient。全模型update+frozenreferenceKL，同时harmful标签从estimatedonsetΔ后对keyGaussian向量cos对齐、benign离开；linear ramp增强后段，response全assistanttoken平均cos超benignholdout分位阈值报警。不是输出归属水印，不是预防/阻断，更不是已取得KB知识的完备sensor。key保密/算法公开改变surrogate转移信息条件，这一具体接口值得保留；实测keymis-match未零、S6明确无provableguarantee，不采§1 irrespectivecompute/无界query安全。Detector/模型/targetlayer/policylabel/onset/threshold与key必须共同绑定，换key须重新适配与校准，不描绘无需重训的runtime rotatingkey。

Eq5benign+cos最小化推向**负方向而非orthogonal**，正文概述orthogonal不可当严格实现；J空/单token ramp的guard未披露，不自造recipe。KL有限惩罚不提供函数保持。T1 conditionalASR先保base已harmful，再算逃检，不等totalattacks/harm生成概率；ActWM Beaver.332>QwenGuard.196、Jailbroken.4592>ActProbe.3296且AUROC.9292<.9653，非allstrongest。T1 vsT3同7B AUROC多攻击数不一致（.9229 vs.9082/.9619vs.9541/.9048vs.8866），§5.9 DeepTPR.211与T1逃检.6702亦不能自合人口，留原协议不补单统一倍率。T2 GSMMath/IFEval/Truthful有退，GSM.8423→.7710明显，不授无损/微扰安全。不同size与surrogate模型、各key200harmful+200benign及条件筛选不能认证完整adaptive或无界query，仅有限empiricaltransfer。

Secretgame特别隔离：N20syntheticfictional/3000train（100eval）/100×Ntest，CE取代一般KL、uniform全token取代onsetlinear为不同训练事件；seed实际watermark_id整数与通用secretseed身份不自证明等强保密。is_harmful/patternPII标签不是真实敏感访问，entityID归因不是payloadexact恢复。D417把correctentity当detection，跟Eq7 maxscore>τ/全Q无alarm的stealthygame定义不等；F5每entity FPR1e-4/平均TPR约.8不是max20家族aggregateFPR，更无给足benign样本数/置信界，不推每10K必<1alarm。本文未知key一般response接口独立，不借此secretgame撑保证、真实PII或完整上线能力。

Qwen2.5Instruct7B/14B、BeaverTails1epoch，labelsQwenStreamGuardonset/GPToracle；D1 72configs layers6/14/23×lr1–3e-5×λ1.5/3/5/7×uniformlinear，std acrossconfig不是同config独立训练重复。B实际singleRTXA6000/AdafactorBF16/maxseq512/microB4+accum，训练约4GPUh/adaptive约14h/promptgenerationeval约.5h与原总约18h不合完整sum，不造更精确总费；D饱和B不补未披露accum，generatedmax128–256；精确samplingparams/部署B/concurrency/SLO/完整端到端time未披露。O(Kd)每token不是全response或systembound，hidden拷贝、全生成、Kpolicykeys、reference/标签训练与校准/审计全计费；表训练一F省略frozenref不当净费测量。streaming正文称possible，但Alg1检测是全response平均，未验earlyprefixdeadline/累计FPR，不能称实时token阻断。

## actual Ch72差额 / 锚

actual Ch72完整662–717 Policy-as-Data（policyartifact→sensor→effectgate→message/account→DeepContext/成对history→guard分支）与192–218权重泄漏/门限/发行/latent水印完整邻接，Ch71/73开篇有效复用。权重/decoder水印为origin取证，动态policy/historysensor没有秘密方向与部署hidden读取共同适配的具体信息权限差额；sole PLATFORM-SECURITY Ch72，不复制隐私DP或表示component数学。

拟Policy-as-Data首完整“关键边界是最后一步…”段（末“同一安全边界。”）之后、下一“安全策略的生效对象也不能只写…”message/account原段前两PRE+本人注，保原policy/静态classifier与enforcement，未独核/锁/写入/POST。

## 两逐字PRE

当对手能够近似公开 guard 时，监测接口还可以改变对手可见的信息，而不只换一个分类器。一个受限分支由 provider 保存秘密方向，并微调生成器，使被标注为违反 policy 的后段激活沿该方向变化、正常回复避开它；部署读取指定层的激活，聚合助手回复的投影分数，再按良性校准人口提出告警。算法可公开，方向与适配后的模型、层位、policy 标签及阈值却须共同绑定；这属于内部行为监测，不是生成内容的来源水印，也不让换一份 key 自动继承原检测资格。<!-- source-family:SF-2026-ARXIV-2603-23171 -->

对未知 key 的有限转移攻击较弱，不证明无界查询或更强自适应对手无法绕过，白盒激活/梯度访问也不在已验假设中。原回复级聚合不认证流式前缀已及时告警，告警更不等有害内容已经被阻断；实体归因实验的标签和检测定义未闭合，不能继承为真实秘密访问或多策略整体误报保证。适配仍会损伤部分能力，内部读取、逐 token 投影、全部生成、标签/参考训练与校准审计都付费。Key、模型或良性人口漂移时，保留 Unknown、原外部 guard、确定性释放规则与人工升级；先重验安全/效用和误报，再由独立 enforcement owner 决定阻断或事后响应，不由水印分数授发布许可。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23171` — [Activation Watermarking exact-v1](https://arxiv.org/html/2603.23171v1)必要§3–6/Alg1/Eq4–8/T1–5、C/D；仅secretkey/适配模型/内部hidden读取的回复级监测信息合同。保黑盒权限/非零转移/无证明、benign负向非orthogonal/口径差、secretgame检测定义/家族FPR隔离、utility反退/流式未验和全费；不授无界adaptive、真实PII、零误报、安全阻断或SLO，未核code/全部图例/实施攻击或复现。
