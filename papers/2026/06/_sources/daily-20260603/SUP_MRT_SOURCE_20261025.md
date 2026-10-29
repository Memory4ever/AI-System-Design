# 00544 MRT：prompt覆盖与response覆盖是两种预算

root，只补06-03的Jun02自然日，R26/R28完整v1题摘/贡献与联合日证有效复用。原未冻结SCREENING初分3+1+2=6留存，不修改旧Report既选分。[当前官方页](https://arxiv.org/abs/2606.00544)所见唯一v1、无撤回/勘误说明，本次用[exact-v1](https://arxiv.org/html/2606.00544v1)。实际读§2–3/5–6、B.1–B.3与C.2；未采用§4的完整uniform generalization bound、GRADES细节证明、所有selector网格/附件、代码或复现。访问2026-10-25 BJT。

## 必要命题与理论边界

目标是分布式条件输出拟合，不是必须唯一正确答案/最大reward。经验风险先对每个prompt的K个回答平均，再对Np个prompt平均；这将prompt人口与conditional response人口分开。固定theta、prompt iid、回答在给定prompt后独立同分布且有有限方差时，total-variance给出Var(empirical loss)=Vprompt/Np+Vresponse/(Np*K)。增加K只压第二项，重复相同答案不自动产生独立conditional信息，相关生成还会增加协方差项。该式是固定模型风险估计的方差，不是训练后能力或所有gradient variance/泛化保证；不采用未读§4广泛界。B.1的bounded-loss通过clip构造并含近似gap，也不能把普通无界CE默当该广泛证明的全部前提已满足。

成本模型B=Np(Cp+KCr)用正的prompt/response单价代入后给连续正K的平方根极值；Vprompt或Cr为0的边界另需处理，模型未含所有生成、筛选、训练、存储和审核的非线性费用。B.3明确连续K*>1不充分保证整数2胜1，整数阈值多一个2；因此不把§3口号直接用作部署采集recipe。小pool在reference checkpoint估计方差须减去组内均值噪声，估计被截零也不证明真prompt方差为零/应无限增K。这里不采用精确最优K数字。

§5 Random-K-of-N在候选池iid且与value无关选择时保生成器q的目标；仅q=P才对原目标无偏，有限池condition-on-pool还有不同有限人口方差，不能据均匀抽样把生成模型认证成真实目标。Reward topK针对reward目标可能合理，对分布拟合则会改变target；不是reward训练必然错误。GRADES的1−1/e只属于非负quality/similarity的facility-location surrogate，不是population risk/质量/coverage真值。真正mode未知，embedding diversity与真实有效回答多样性不等。

## 评价与反侧

§6.1为已知三mode合成分布/mixture-density NLL，reward刻意偏中mode；支持预算/target-mismatch的受控例，不等LLM真实采样分布已知。§6.2/C.2主要Llama3.1-8B-Instruct LoRA r16/alpha32、多projection，LR1.2e-4、per-device batch1/accumulation16、匹配optimizer steps，四数据集Gold/CodeContests/Nectar/UltraFeedback；更多K暴露更多不同response、小K更多epoch，并非所有token/FLOPs/生成审核等预算。不同回答长度也改变曝光，不能从step匹配得全成本因果。

Gold七backbone的reference CE改善与受测覆盖曲线是作者局部结果；reference为benchmark整理的输出人口，不等全部有效/真实答案。Coverage取16生成与reference的MiniLM最大cos，diversity是两两cos距离，best-of16 reward共享Skywork选评代理；低loss、相似度覆盖、语义正确/代码执行与安全不是一个量。CodeContests另有test执行仍非所有程序正确证明；硬件、统一precision、完整输入/输出token、独立seed/区间、完整采集训练/服务费用在已读必要域未充分披露，不补SLO。

Table1只有四数据集的reference-checkpoint方差比与有限R1→R2关系，不证明跨全部训练阶段的因果分配律。Table2在相同监督pair条件测paraphrase与response分布，Similar的coverage0.714仍高于Diverse0.712/显式MRT0.713，而loss较差，不能照“所有指标更弱”；4×4 upper bound又改变总pair预算。未采图像精确点/selector全优或MRT任意目标普遍更好。全部prompt采集、过生成/选样/去重、标注、训练和独立目标回归均计费。

## actual owner / 拟6分 / 最小两段

实际读Ch27重复曝光权重的完整上段、网页问句频率/真实需求完整下段、同item标签分布与预算、重复数据/unique的具体组；Ch29分布CE与diversity/目标loss相关组表明监督目标归SFT，但采集单位与预算归唯一`TRAIN-DATA`。现有重复不等新信息/标注分歧不能具体代替prompt方差地板与conditional response采样这一缺口。相邻Ch26/28开篇、owner链已读；不另在SFT复制相同公式或把多模态/偏好例全部扩池。

正式拟2+1+3=6：具体数据采集/分布目标选择、单data组件、长期统计边界；不把经典total variance的新应用视作普遍训练能力设计纠错。原准备D3+1+2=6仅未冻结初分留原JSON，本日报尚无该项；正式字段待独核，因具体知识缺口深入必要条件与反侧，不为省审改分。

完整上锚：

模型不会自动知道哪些内容是“高质量事实”，哪些只是高频重复。若某段文本出现一千次，它在经验风险中获得的权重就可能接近一千个独立样本，即使重复并没有增加新信息。

拟新增两段：

同一prompt的不同有效回答却不能一概当成上述重复：若目标是拟合多种合理输出，新增prompt覆盖输入人口，新增response补同一条件下的输出模式，两者解决不同不确定性。固定模型、独立prompt与给定prompt后独立回答时，经验loss的方差可拆成 `V_prompt / N_prompt + V_response / (N_prompt × K)`；K是每题保留回答数，第二项随它下降，第一项不会。[受限多回答研究](https://arxiv.org/html/2606.00544v1#S3)由此提出预算分配，但这只是固定模型/采样假设下的风险估计，不保证训练后能力随K增长。相关生成、重复错误和稀有输入缺失仍需分别处理，更多回答不能替代更多独立问题。

选哪些回答也会改变学习目标：均匀随机保留只对给定候选分布保持无偏，不让生成器成为真实答案分布；按reward选最高分适合追该reward，却可能缩窄原本需要保留的有效模式。Embedding多样性同样只是覆盖代理。应共同保存prompt身份、候选生产者、保留数和selector，以真实目标及相同总预算验证；连续成本模型给出的K不能直接充当整数或全流程最优。过生成、审核/选择、更多训练token与回归都付费，有限实验的reference loss和cosine覆盖也不等事实正确或净省费；输入覆盖更缺、答案近于确定或采样/质量不稳时，保留更多独立prompt、可信单回答及原有采集策略，不为多样性配额制造答案。<!-- source-family:SF-2026-ARXIV-2606-00544 -->

完整下锚：

网页里的问句也不等于真实用户的提问。FAQ 模板、搜索优化和机器生成页面会把某些问句反复刊登；按网页出现次数构造 QA 训练配比，测到的是发布/抓取频率，不是人类需求频率。若目标是服务真实用户，来源 host、页面用途、采样单位与真实交互日志的可用性必须分开记录；后者又带来隐私和代表性约束。网页问句仍可作为语言覆盖材料，只不能在没有校准的情况下充当需求分布。<!-- semantic-body-binding:SF-2026-ARXIV-2609-24106 -->

当前首次必要/正式6/actual Ch27与原两PRE待独核，不写Books或预I/DAY。支持与关键反侧足，停止未采用的泛化证明/全附件；下一MODEL项由路由独立续接。
