# EmotionNeurons17231：gate 地址与生成控制的分验

resume_mar17，仅03-20补03/19；当前适用合同/ROADMAP/停点与Books写作约束已重载。Batch6/独核§17完整AB及日级夹证准入有效复用，原2+1+2=5不变。准备者不自授Source/PRE、safe或Books写锁。

## 1. 必要原证与停止

[exact-v1](https://arxiv.org/html/2603.17231v1)实际§3.1–3.5/Eq1–8（111–209）、§4/Table1（210–227）、§5.1–5.6/Tables2–6/图题及直接限制（228–385）与§6（386–391）。当前[官方abs](https://arxiv.org/abs/2603.17231)完整header/Comments/history仅v1、11pages10figures，未见具体撤回/纠错。只必要支持与关键反側，未读全部图像细节、references、代码或复现，不扩旧相关论文/版本史。

## 2. 所采接口与必要反证

记录对象是语言decoder gated MLP 的非线性后 gate g=φ(u)，在g⊙v与Wout之前的标量维度，不是MLP输出/residual，也不是把全gate置零。先记录全部生成token tensor，随后按目标情绪SER匹配和内容WER过滤成功人口；§3.2明确WER阈值0.15，不是0.1。内容WER来自LALM自身伴随音频输出的decoded text对source transcript，明确不通过另一ASR转录生成audio，因此不能授实际音频逐词保持/文本音频一致。每情绪成功集cap c，positive activation概率按token计数；LAP频率、LAPE熵、MAD概率偏离、CAS top-vs-second margin定义分开，不把MAD名当幅值均值差。CAS仅归top emotion，再取全hooked空间floor(rN)掩码。

运行时冻结weights，在选定gate维度作gain1+α、标量add/floor或zero；它改变forward函数，既不等权重编辑，也不等训练免费。self/cross masks与等稀疏random对照支持局部选择/干预差别，不鉴定单一情绪槽位、唯一机制、与内容能力正交或全部模型可迁移。样本筛选与地址选择共同定义干预身份，不能只保存“情绪方向”名称。

三LALM/ESD十English speaker，neutral→四情绪；6/2/2 speaker与seen utterance-index分割。T1 unseen001–350和seen ID集合有数字重叠，不能由正文概述授全局speaker与utterance两轴都不重合，只按表中联合speaker/utterance身份保存。emotion2vec在原ESD500样本97.6%不授生成音频truth，补充Qwen judge另有偏差。T2正文把Kimi15.62和Qwen11.93比较混了两个judge列，不能用这对数字作同judgebaseline排名。

T3 Qwen CAS情绪提升同时WER19→29.65；MAD也WER24.22，Mini CAS在emotion2vec self−.20而另一judge+.40，Kimi亦WER2.82→4.74/UTMOS退。T4 α2 WER203.65而UTMOS仅略退直接反证自然度=内容保持；α.3/.5局部较保守仍不是所有条件无损。20听者评同100pairs（每情绪25），平均62/11/27偏好仅情绪选择，不是2000独立音频或content审计。human/SER neuron平均Jaccard.118/directmatch20.63%，layer JSD.021低不授地址一致；CAS-H仍有内容WER退。

§5.5图题count只是被选neuron分布非effectsize；语言decoder中后层和synthesis MLP同设置对照T6可局部分采，后者CAS gap负/近零不能证唯一路径或全部合成模块无情绪信息。§5.6 unseen happy近零/略负、sad明显弱，保speaker/情绪迁移边界。greedy/temp0 when available及16kHz/默认c50,r.5%,α1已披露；hook/统计/筛选、SER/human、调强度、多完整生成/回归均计费，完整硬件/precision/batch/并发/tailSLO/CI来源及端到端延迟费用ND。需要强保证只一次请求音频独立转录与text/audio一致的盲验、掩码地址/筛选/strength冻结、匹配预算random及跨speaker内容/情绪切片和完整费用；所采有限接口不依赖该强保证。

## 3. actual sole owner 与差额

sole `MODEL-FFN` / [Ch16](../../../../../books/part-02-model/16-feed-forward-mlp.md)。实际完整138–202的gate/SwiGLU与STEM分责、238–279的执行/知识关联/probe/weightedit及Ch15/17入口已读；Ch23已有音频控制/感知题材不拥有通用MLP gate寻址与介入身份。现SemanticRelations263只probe-space sparse feature联合验收，下一weightedit段是改weights的recall/locality；未承载成功过滤人口→postactivation gate地址→冻结weights的生成干预与音频/伴随text分验。拟原263完整后/265weightedit前两段，维持读出、activation介入、weightedit三类责任，不增结构或重复多模态codec。

## 4. 两段 literal PRE（未裁）

读出关联之后，还可在冻结权重下直接测试生成时的gate介入，但必须明确地址：对gated MLP的非线性后gate选定维度，在与另一内容分支相乘及输出投影之前缩放、加偏移或置零，而不是修改整个residual或权重。一个受限语音生成分支先按目标情绪匹配与内容误差筛选成功样本，再从其激活概率差别选稀疏地址，以同情绪、跨情绪及等稀疏随机掩码比较输出。筛选人口、模型/layer、hook位置、掩码与强度共同定义该干预；相关地址和局部效果不证明单一情绪槽位，也不证明它与内容能力正交。<!-- source-family:SF-2026-ARXIV-2603-17231 -->

[生成gate干预的有限对照](https://arxiv.org/html/2603.17231v1)同时暴露情绪、内容与自然度的不同边界：情绪匹配可升而内容误差恶化，自然度仍近似不变；其中内容WER取模型伴随输出的text而非独立转录生成audio，不能把它当作音频逐词保持证书。自动与人选地址只部分重合，跨speaker/情绪迁移也有反退，语言decoder和下游synthesis的局部对照不授唯一因果位置。识别、judge、人工筛选、强度搜索、额外生成与回归均付费；失配或内容退步时，保留原forward、保守强度及独立音频/文本检查，不从冻结weights或听感自然推出无损控制。<!-- source-family:SF-2026-ARXIV-2603-17231 -->

静态注：

- `SF-2026-ARXIV-2603-17231` — [EmotionNeurons exact-v1](https://arxiv.org/html/2603.17231v1)必要§3/Eq1–8、§4/T1、§5/T2–6与直接迁移/内容反侧、§6。仅成功人口→postactivation gate稀疏地址→生成控制的接口与分验；保伴随text WER非audio转录、judge/人选差别、强度/迁移反退和全费，不授语义纯净、唯一因果、内容正交/无损或完整部署保证，未核代码/复现。

支持与关键反证够证即停，交reader非preparer一次必要Source/actualowner/literal PRE裁，root另授窄写才落实；普通未审材料不改EX/center。

## 5. 获准实际窄写与 writer 读回

reader§27原两PRE有限通过/root授soleCh16本family锁后，作者逐字写新265/267及静态本人368。writer完整251–285与末9本人/Semantic/STEM邻注读回；gate地址/冻结weights控制与probe读出/weightedit三类责任衔接准确。scoped本family实际diff仅两正文+静态注，diffcheck0。未自授actualPOST/safe/DAY，交reader一次nonwriter完整局部和静态本人注核，不改验收人员身份。
