# 概念三元组与SAE遗忘：监督构造、表示代理和删除证据分开

Daily2025-09-23补Sep22BJT，root本次明确接受作者A147两未开始首次必要域后首备。原各2+1+2=5及既成AB/日门不重审。下一由writer唯一另一角色回原域实际采用，reader只后续角色复用；本包不预Books、永久删除、合规或完整DAY。

## 原件及实际读域

- [Concept Unlearning exact-v1](https://arxiv.org/html/2509.15621v1)：`ROOT_CORE_15621_20261024.raw/.request.json`；GET 2026-10-24T05:09:04.975207+00:00，200/exit0，435392 bytes，SHA256 `b9a71776723f982aed39f0cfa6e899730ebe87549c334031d328102e1ae00719`。实际§3–6、Alg1/T1–3/F2文字caption、A.3/T5、B.1/B.2、C.1/C.2/Alg2及必要prompt约定。未读A.1/A.2全部逐任务/逐模型曲线、A.4/A.5全例/其他附件，不核像素、代码或复现。
- [SAE-guided Unlearning exact-v1](https://arxiv.org/html/2509.15631v1)：`ROOT_CORE_15631_20261024.raw/.request.json`；GET 2026-10-24T05:09:11.029863+00:00，200/exit0，253607 bytes，SHA256 `69a012106d039a7bdf480f53e98a041b621af0589f8b9f90993afa80b72b4cd0`。实际§2–4/6、Alg1/T1/F2–3文字caption、B.1–3。首次长输出有中部截断，决定性§4.1另完整定点读取，不冒截断已读；未读A全部图像或代码/复现。

两请求均已收尾。论文中的生成/验证prompt是审阅对象，不是对本任务的指令。

## 15621：扩展可提取的训练目标，而不是读到完整内部知识图

论文把概念限定为target作为subject或object的一跳关系。形式CU对所有输入要求未在prompt给出的target-triplet不能出现在输入+输出的抽取结果；实际NU是遮实体后能否补名，EU是给实体/关系后能否补属性。这两类有限cloze probe不覆盖形式全称命题、任意改写/多跳/过程知识，也不是模型真的以图节点存知识的证据。

机制将监督生产分两路：固定pre-unlearned模型一次产生解释句供sentence loss；每轮由当前正在遗忘的模型提三元组，由原模型验证，再转句/分开实体前缀与属性tokens供triplet loss。GA分支最小化对应log probability；NPO分支相对原模型的概率比作有界方向的偏好式抑制。交替优化改变模型参数，不是只改系统prompt，但优化输出/自产监督不自证参数中所有关联被擦除。贪心输出是该条件的局部argmax，不保证内容真实、完整或已校准高置信。

C.1每换行强插(target,，只抽target作subject，明确漏object位置；这与§3概念范围有实际缺口。验证器与生成器同源，原模型“1”只表示其判断，不是独立事实审计。每triplet转十句的prose与Alg2单句写法不闭，分开保存ent/attr集合又未写配对身份/重复如何保留，不抄完整执行recipe；句中前置属性、别名/多次实体出现与无法定位实体也需实现另核，不补作者未给guard。

T1 Wiki-Fact30目标/20保留，TOFU20目标/其余19保留，只在原模型答对的NU/EU样本上验，因此原100%按选择定义而来。T1 target Node/Edge为0不表示所有相关输入从此未知；仍有non-target大幅损伤，如Mistral Wiki-Fact69.8/84.0而非原100，general59.1低原62.2；Llama55.1低57.6。TOFU非目标虽有改善，未到完全保持；虚构实体注入支持有限适配实验，不授任意真实数据删除或已无背景先验影响。

B.1每5epoch评到50，选Node/Edge首次同时0；这是使用该评测人口择checkpoint，不是独立未见攻击的删除证书。方法间可经历不同更新量/自产token与选点费用，不能用最终0/更少epoch认同预算最优。T2只triplet剩Node80.1/55.3，句子only能压低target却更损non-target，支持互补取舍而不是两项各自唯一机制；预算/停止不同也限制归因。Llama Full general55.1低sentence-only55.5，不能称所有utility都改善。

T3 relation-aware以ParaRel38类先验将coverage约38/42.6提高到88/87.1；coverage分母仍是已知且原答对的参考triplets，不是模型全部内部知识。增加相应关系类也与EU模板来源共享先验，未证明未知关系/多跳全覆盖。A.3 GPT4作精度judge、GPT4o作替代过滤器，GPT-family判断不是外部真实fact认证；Mistral精度proxy68.6→96.2同时non-target69.8→63.8/84.0→78.9，Llama改善不补通用“精度越高越好”阈值。正文声称internal KG只能作为解释性组织，不改成已识别内部本体。

两H10080G的模型/原模型、全部每轮生成/校验/转句、固定解释池、GA/NPO训练、关系枚举、网格选点与独立回归都付费；未给净墙钟/完整batch、精度、重复seed/CI/重学习攻击与生产费用，不补造。不满足覆盖/副作用/独立目标时，保原checkpoint、隔离目标资产、人工及独立提示/关联测试；合规删除需额外训练lineage与数据治理证据，不能以零cloze分数替代。

## 15631：让已知/未知方向变化，不等于得到从未学过的oracle

先用已知Wikipedia人名与虚构TOFU人名的末token激活，比较SAE postactivation>0频率；差大于tau=.4选known latents，小于−tau选unknown latents。训练只输入目标实体名，取其末token的SAE preactivation，以hinge把known方向推向≤−c、unknown方向推向≥c。表示空间提供可优化的目标，但“未知人名时的活动”是替代参考，不是从头移除数据训练所得oracle的已证等价；§6明确承认这个缺口。两群体可能还含字符串/分词、频率或风格差异，低维统计不证明真实知识身份或唯一因果机制。

SAE在原模型/层坐标训练，LLM更新后原方向的测量含义仍须回归。只约束选中SAE encoder方向不等匹配完整SAE code、residual activation、下游函数或全部实体关联。hinge非负、下有界，不是对任意activation上有界，也不因loss有目标就保证参数优化收敛、无collapse或所有约束可同时满足。随机层顺序缓解作者观察到的同时更新不稳，不能称无条件稳定；Alg1写U({1,L})而prose逐层随机，端点集合与全部整数支持未闭，不补成明确实现。论文所写简化Transformer无norm，不当现有模型的完整前向配方。

主结果RWKU前100目标，模型Llama3.1-8B/Gemma2-9B、各有Llama-Scope/Gemma-Scope SAE；实体last-token分支batch1、corpus baselines batch4，Adam/反向cosine/每epoch5步、至200、两H10080G。每10epoch监视retain、选择退化超过10%前最后checkpoint；10%相对/百分点与独立选择集未明确，不替作者补定义。不同方法输入、batch、训练位置与停止点不同，不称全部同等训练总费用。

T1 forget均值Llama46.8/Gemma57.1比所列baseline更低，但仍远非0；retain83.5<原83.9、82.2<83.7，Llama Gen65.1<65.9/Fac65.8<68.9，Gemma Gen70.9<72.8/Rea30.4<33.9等反侧保。fluency只是bi/tri-gram熵而不是完整人类语言质量，Exact contains GT的检测亦受输出格式/别名影响。有限九类已知攻击不认证任意可恢复性或重学习安全。

§4.3内部诊断另用forget到0或200最终点，与主表retain早停**不是同一checkpoint**；20目标的attribute rate/recognition曲线不能直接拼成主表模型已彻底遗忘。Attribute rate由词表投影top50与passage派生词集合交集获得，不是真实内部语义信息量；B.3式19写集合除50的简式，实际须计集合大小但本次不补执行recipe。选中known/unknown latents正是训练所操作的代理，变化方向不能独立认证删除；同层线性读不出也不排其它层/非线性读出/新提示取回。主文一处Llama3.1-9B与其余8B身份不同，不私统一成第三模型。未审曲线像素不提供各层量化值。

保全部known/unknown集合制备、原SAE历史训练/驻留/编码、层选择和反传、最多多轮回归与独立关联/恢复测试费用。目标名并非不需任何辅助数据；原始训练语料不可得与无需oracle是不同限制。支持/副作用/方向身份不稳时保原模型、普通输出抑制/隔离与独立回归，明确残余可提取知识；不由oracle-free或interpretable名称批准exact unlearning、隐私或合规安全。后续只按有限表示目标/监督责任比较唯一知识owner，原5与正式候选保留，不因统计冲突直接删候选、降分或强制写Books。
