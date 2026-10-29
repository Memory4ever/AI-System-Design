# Sep23 必要证据：任务级置信预测与逻辑评测构念

作者A104实际确认15356/15587两首次必要域未开始/无CORE/无在途，root明确接受后唯一首备；原AB、日门和各5分复用，不第三。作者负责唯一非准备者回原件实际采用及具体owner比较，reader只复用已闭角色层；本包不预Source通过、Books或整日完成。

## 原件、范围与未核内容

两独立GET均于2026-10-24 UTC02:39:55～57真实结束，200/exit0，无在途；本日同base request记录精确版本、实际执行时刻、状态、bytes和SHA，不把此次获取当公开日。

- [2509.15356v1](https://arxiv.org/html/2509.15356v1)：`ROOT_CORE_15356_20261024.raw`，278980 bytes，SHA256 `6699a1185e578df7fb1e26e1bc5da6e6609eacca13c78ead314783fa9d82381e`。实际完整读§3方法/全部proxy、§4.1–4.3设置与直接结果文字/必要图注、Limitations、A.12完整模板和A.15硬件。未核全部A.2数字表/所有曲线像素、额外回归附件、folktexts源码或复现，不把未读可选域变外部hold。
- [2509.15587v1](https://arxiv.org/html/2509.15587v1)：`ROOT_CORE_15587_20261024.raw`，245009 bytes，SHA256 `c2b3fe015a577c53e16df9c854b06b9b9bbbb5dddeec053afa69b2df4b9527c2`。实际完整读§2构造/判项/Eqs1–2、§3全部三项干预、§4设置/结果/直接Tables2–7、Limitations、F/G指标范围与解释及I评价prompt。没有核全部Table9/额外图像素、PDF像素、全源码或模型复现；Table4差额明确只针对所读exact-v1 HTML，不冒原PDF已核。

## 15356：任务可用性预测、逐题排序和概率校准是不同消费对象

31个公开tabular dataset，每个最多随机1000行转“Feature: Value”，A.12固定单字母正负选项；从token输出分布取risk score，另一次让模型文字给guess和其正确概率。两者不是同一概率：前者是标签事件，后者是模型对自己所选guess的口述置信。确切token集合、全词表质量、候选归一与parser/无效回答不能由本包补成统一已验scorer，完整template/model revision与实际消费者仍需绑定。

只提供任务描述直接预测AUC/1–5整数/0–1小数，和逐行口述置信/MCP/其标准差、risk标准差，是不同信息预算。Masking则从其它列预测一个feature，连续列按median二分、分类列按是否mode；排高缺失/极端频率并每dataset取10列，产生285辅助任务。其label来自可观察feature值，不是所有proxy都无需标签；预测真实业务目标时不拿目标label，不等完全没有监督或额外数据。不同feature任务共享dataset/row，也不是316个独立域。

直接证据支持的是局部适用性诊断：同dataset换目标列的AUC可从低于.5到高于.9，平均其它列预测质量并不可靠替代目标任务。文中“ICC=within/overall”与随后“19%由dataset解释”的口头定义不一致，本包不将该精确方差分量当独立已核估计；保其任务内差异的受限观察，不据此宣判所有domain没有可迁移信息。以受监督XGBoost AUC作分母的相对分数只是另一proxy，不等已知Bayes最优；ratio也不是线性消除任务难度。

个体risk的ECE差、失败预测排序却可能有用：原任务AUC、以MCP辨正确/错误的另一个AUC、标签概率校准三者分开。作者报告失败预测AUC约.4～.9，低于.5的反侧不能抹掉；高原始AUC与好失败排序的相关性也不证明“能力导致自知”，更不能无标签选择一个有保障的abstention阈值。ECE基于人口与bin、AUC只看排名，二者不互为真值或实际损失。

任务级上，风险分数的spread比平均自信更相关，作者给GPT4o/Llama的R² .605/.270；但原文明确有高方差/低表现outlier，不签单调保证。对GPT4o-mini以sd≥.4筛后的平均AUC .8417对全体.7186，是在此任务集合的selection条件均值，不是每个保留任务≥.84、风险上界或已固定阈值的独立部署验收；未给保留比例/完整分位不补。无标签risk的边际分布本身不能识别真实AUC：本包的有限解释例中，保同一组risk而把binary标签对调，risk分布不变，AUC可由1变0。它不否定原population相关，却要求外部分布与独立真实标签校准。

201个分位点训练XGBoost预测task AUC，5fold按dataset分组，避免同dataset的列跨train/test；但训练target仍是由历史真实labels算出的AUC，不能称整套元预测器无监督。LOESS的95%带不是每任务有效prediction interval，5fold也不自动覆盖未来domain/model revision。文中所谓“与parameter count一致”不能作闭源GPT参数事实或规模因果；模型家族、训练与接口共同变化。GPT4o median .82和原31-task mean .77是不同汇总，不能误当数值矛盾。

公开语料可能在预训练中出现，跨列不完美或serialization变形不能排除部分熟悉度；固定模板、binary label、只四个可取token概率模型不推广任意生成/CoT。A.15本地Llama/Mistral单Tesla V100、全部实验80GPUh只是作者该部分费用，GPT走API不等无计算费；API精确snapshot/总token与调用、dtype/length/batch/并发、bin/阈值选择和重复不确定性、总墙钟/SLO未完整披露。所有serialization、每行两路信号、285额外任务/目标制备、元模型训练与独立新域回归均收费。有限采用“以实际预测人口的统计做任务筛查提案，另验真实label、逐题排序/校准与部署决定”；失配保直接有标签holdout、常规预测器/保守拒用，不授模型可自证适用性或统一高variance规则。

## 15587：语义选项身份的一致性不是概率置信，更不是逻辑过程证明

先由命题变量/蕴含规则及外部solver构造entail/non-entail候选，剔单一premise可直接推出的答案，再生成3c1e/3e1c/missing-premise题型；NLI句子实例化变量，GPT3.5造模板与修语法，LCS比例>.5过滤改动并人工批准。Solver首先认证的是symbolic命题，字符串相近和语法人审不自动证明自然语言语义/否定映射仍等价。总12589、人工polished测试900、三题型平衡；人工/自动生成预算与oracle资格不能被“合成可验证”抹去。

对四个循环选项排列，Circular要求每个排列都答对；PartialCircular用`(c/4)*(1−H_4(p))`，p是映回原**语义选项身份**后四次答案的经验频率，不是A/B/C/D位置频率、模型token概率或独立人类confidence。原例同identity两次、另两identity各一次给c2/H=.75/PC=.125，本包复算一致。若误按字母计数，始终答同一语义正确项会呈四字母均匀而被罚零，故映射不可省。F的alpha只改变accuracy和一致性的权重，不恢复概率校准；G的[0,1]界有效但不证明构念faithful。

**本包新增有限反证，保命题而不替作者修数。** 按定义，同一题/同一人口下若Circular=1，则c4且p集中在真选项，PC=1；其它Circular=0而PC≥0，所以平均PC≥Circular。所读HTML Table4却给DivLogicEval原CIR16.4/PC6.3、NoLR CIR15.8/PC5.2，与此不相容；Table2/7又采用通常PC较高关系。不能擅把Table4两行交换、混不同protocol替作者解释，或以该表证明NoLR的指标比较完整成立；也不据此断言实际实现必错/全部benchmark无效。

另用四次**独立均匀猜语义identity**的256种等概率序列枚举，PC期望约.0845013、Circular期望1/256=.00390625；四次经验频率并非每次都均匀。因此“random guessing不给credit”最多指恰好经验四身份各一次的样本，不是随机策略期望为零。此枚举只是对印式的有限算术，不是模型复现；不把较低分误当去掉所有luck，也不由输出一致读出内部逻辑。

NoLR只是提示“不要逻辑推理”的干预，不能证明对应内部机制真的被关掉；语气/长度/策略也改变。Wikipedia unigram KL只测词频proxy，低值不证明任务iid、逻辑/模板无偏或测试风险更接近真实用途；支持集/平滑/词频口径要明确。GPT3.5错误选项exact-match .2%未排除所有记忆；SNLI/MNLI追加LoRA后SNLI+12.7pp而本集+1.2pp是该干预的敏感性，不等所有污染免疫或完全独立预训。body说SNLI+MNLI而T6caption只SNLI，不能合成已闭训练人口。

五次Gemini的CV只是该模型/配置的有限稳定性观察，不能因PC/CIR排序符合另一benchmark就证明哪个更真实；其不同mean使CV还受分母影响。Table7 GPT4自然语言三示例ACC32.2→27.2/CIR12.3→7.2/PC22.1→17反退，symbolic ACC39.1→38.1仍降、CIR16.3→18.7/PC27→28.1升，不能写所有symbolic指标改善。替换表达和示例会改变token/提示支持，不独证“反直觉性”唯一因果。

o1成本限制只取前40题，非随机同人口；其它模型在subset较差不证明o1结果是full-set保守lower bound。四位CS学生先通过>80%symbolic资格才测60题，86.7%是该筛后群体/小样本，不是所有人的同预算基准。模型结果按实际revision/zero-vs-three-shot/题型/人口绑定，部分few-shot反退保留；未核所有额外表/像素就不采完整排名或51.3%的统一分母。调用次数、temperature/seed、token长度/batch/硬件与总latency/SLO未完整披露，不由新metric给安全/推理算法证书。

全部symbolic生成/solver、NLI取句、模板/反复修订/人工语义核、每题四排列×多模型×重复/三示例及全独立回归计费；相同题数不等相同调用或预算。有限采用为“对位置置换保持语义身份，再联合测正确与稳定；形式标签、语言呈现和指标聚合分别验”。表口径、标签语义或真实用途未闭时保普通accuracy/逐排列完整分布、原solver与人工审核，不以高一致性授权真正逻辑理解或随机性已消除。

两篇原5分/候选保持，未核可选域不设无限任务；交作者唯一实际采用有限必要支持/直接反侧和成本后，具体owner由作者新层准备，reader仅角色复用本Source。不预NC、I、中心D或DAY。
