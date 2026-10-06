# MR 29518：必要证据与窄 owner 差额

root恢复本日旧EX被完整题摘反例重开的必要层，不扩发现。原精确v1题摘、current事件/正常复合日门原字段复用；[精确正文](https://arxiv.org/html/2603.29518v1)已缓存于`SUP_RESUME_CORE_2603-29518v1_20261013.json`。

## 本轮实际读到哪里

完整题摘、§4/5、§6.1/6.2方法与Table8、§6.3两实际评价人口及Tables9–10、§6.4完整和§6.5必要Tables11–13及人工选择限制。§3读了任务/采集差异和Table5核心，未称完整逐例；§6输出中间被截断处另以具体小节切片补读，不将首个截断输出冒作全文审阅。没有附件/代码/媒体或复现。

## 准入与必要Source

`2+1+2=5`：不是把新增示例当新算法，而是示例与语义人口共同改变评价有效性。原示例组合EX不足：相同MR的参考多样性、reference聚合与无属性样本排除会改变测量对象；单参考恰在demonstrator时可产生完美拷贝，不能只由高分判适应或泛化。四语料、GPT-2 Medium、5-fold、5epochs/B8、每MR五输出/max80/T1；训练和部署输入均改变，不能归全部收益给in-context。§4仅按DA、DA+属性数、DA+属性集合选固定示例；此选择不是事实核验或值完全相同保证。

Table8中更细示例在EMPATHIC改善部分参考分数，却在其他三人口多项低于baseline。§6.4高reference人口较低分是受限关联，不能断言改变reference数量的唯一因果；reference内容/采集共同变。Slot Accuracy排无属性样本（两语料约40%），与全请求/DA分类不是同分母；DAO scorer自身EMP验证约.68，不能签真实意图。人评挑最大metric差异，未独立校准全人口；不同量纲的BLEU/LaBSE绝对值大小不直接证明优劣。小于1%的参考与示例重合片段是具体告警，不泛称所有train/test泄漏。模型/precision/hardware/总训练和示例费用未充分披露；弱指标不保证完全语义、安全或上线。

## Owner 实际比较

root实际Ch74 1–175将示例的质量、顺序、覆盖与schema分责，但不拥有评价聚合；其一般框架不等本文条件化验证。Ch66 139–159完整局部已有reference几何、MOS调制、prototype误排与具体scorer identity，但没有“同一目标的多合法reference平均”及demonstrator/reference身份重合这一测量接口。canonical拟为`PLATFORM-EVALUATION-SYSTEM`，Ch74只消费已有Prompt原则，不重复插段。只填这个长期评价差额，不采用全部NLG配方或某metric普遍更优。

## 拟正文（一个段落，ProtoBias段后、语音conditional metric段前）

同一目标有多个合法表达时，参考集合的聚合方式也改变评价对象。把输出与每个reference的相似度取平均，测到的是它与这份参考人口的平均接近程度，不是“是否实现了输入要求”；合法表述更多样时，正确输出也可能得到较低平均分。若示例又恰好包含唯一reference，拷贝可获满分，却未检验独立生成或泛化。[受限对话生成研究](https://arxiv.org/html/2603.29518v1)提供了这两种诊断，但不同语料的参考数量和内容共同变化，不认证数量的单因果或BLEURT普遍优于embedding。应共同保存目标、参考集合、demonstrator来源及聚合规则，把属性覆盖与表达相似分开；无属性样本被排除后的slot准确率也须保留其条件分母。参考制备、示例匹配、模型/指标调用和独立人审都有成本；参考不足、与示例重合或scorer未校准时，保留原输出、输入条件与固定分母的人工/任务检查，不以一个平均分或完美拷贝批准能力。<!-- source-family:SF-2026-ARXIV-2603-29518 -->

## 拟本人末注

- `SF-2026-ARXIV-2603-29518` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29518v1) §4–6必要方法、Tables8–13及§6.4，2+1+2=5。仅采用多reference平均的测量对象、demonstrator/reference重合与条件slot分母；四语料/5-fold GPT-2 Medium/五输出、共同输入训练改变及最大差异人评限制保留，不采跨量纲指标优劣、参考数量单因果、所有split泄漏或通用泛化。未核代码/复现或生产。

Source/逐字PRE待非准备者独核；未写Books，不预授整合或DAY。
