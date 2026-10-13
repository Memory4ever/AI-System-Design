# Contextual invariance necessarySource / sole Ch66 两PRE

2026-10-12，[2603.23485v1](https://arxiv.org/html/2603.23485v1)原2+1+3=6/date25保持。actual Results/Methods/Discussion L28–164必要正文/F1–4 captions/T1/Eq1–2；不是全部补图/数据/code/复现。局部测量反侧支持独立设计差额，CbD强解释隔离。

## 采用与直接反侧

360WinoPron templates/180成对职业-participant句，固定target及明确antecedent，只在前置句为另一referent提供gender标记；五contexts为unprimed/female/male/“The sky is blue.”/“North is south.”两个null。这改变非target语境，不把所有语用信息称严格完全等价，也不能推广所有task。强制genderbinary只为这份测量，50/50是作者无偏norm不是未知性别真值；不评价全部genderidentities。互换选项顺序、valid>99.5%仍过滤无效响应，279/360可匹配独立rolefemininityrating不是完整人口；correlation降低不是bias消除或culturalprior因果证明。

F1/2/3相关文字支持有限context改变输出概率、role相关指标可能随语境失效；MI只是统计信息不是内因果定位/faithfulmechanism。Nullcontexts也移分布，Llama null与discourse差异例外，不统一全部模型同幅。Methods H200/除Gemma4bit，Gemma不量化；GPTOSS20B/Phi4/Gemma3-12B/Llama3.1-8B/Qwen2.5-7B，T.5/newtokens6/topk40，GPT额外T.3/.7与无generationhead复测仅该模型。重复每template具体次数/independentseedCI/batch/concurrency/fullSLO未在必要正文披露，不能由Bernoulli估计或样本360授权单prompt准确公平。全cue生成、valid过滤、重复采样、分类统计/null对照与量化身份校准均计费。

**必要中心反证：**Methods156–157把jointexpectation写成两个marginal乘积，即设a=E[X1o1], b=E[X2o1], c=E[X1o2], d=E[X2o2]，第一项变|ab-cd|。对a,b,c,d∈[-1,1]，|ab-cd|=|a(b-d)+d(a-c)|≤|b-d|+|a-c|，因此原Eq1按其给出的joint计算必ΔC≤0，不能得到Eq2>0/T1的19–52%。可能真实实现有另joint而文字错，未披露，不能自补或照录“扣所有latent因素后不可约/量子contextuality”保证。本文T1比率仅作为原报告待核，不用于Books正面。F/Results的实测边际概率变化接口不依该CbD数学解释成立，仍准入6，不整体HOLD/降分逃审；具体Eq/joint采样+原代码实现勘误为重开条件。

## actual owner 差额 / 锚

实际Ch66完整255–335固定subject/指纹marginalnull/harnessidentity/freshpaired→scorer重判→TRACE边界，以及Ch65/67开篇；既有harness字段/pairedruns未承载固定target下另一referent的非targetcue和nullcontext/optionorder交叉测量，及marginal变化不授强依赖解释的具体入口。sole PLATFORM-EVALUATION-SYSTEM Ch66；不在语言表示或公平治理另建owner。

拟TRACE2610-11678完整第二段（“不由聚合分数给模型能力或部署可靠性签字。”）之后、下一物理交互3DGS段之前原两PRE+本人纯注。保此前对象固定和后续环境oracle，未独核/锁/写。

## 两逐字PRE

固定被测对象后，输入中的非目标语境也要进入预期不变量。一个受限诊断保持目标句和待判断对象不变，只在前置句给另一对象增加属性线索，再与无前置语境、无关句和选项顺序交换分别配对；反复采样得到的是条件输出分布，不是一次回答的真值。已有属性或偏差指标若随这些条件明显变化，就不能把孤立模板的均值当成模型在所有语境中的稳定属性；也不能要求本来改变任务信息的所有变体同分。<!-- source-family:SF-2026-ARXIV-2603-23485 -->

分布变化还须与更强的依赖解释分开。边际频率、相关性或互信息改变可以提出诊断，却不独占内部因果；用边际乘积代替共同测量，又不能认证已排除全部潜在因素。有限强制选项、过滤后的有效响应、量化不同的模型和未匹配角色人口都限制外推；原文不可约依赖公式与报告比例未闭，不由此批准公平或安全保证。保存 target、cue/null、选项顺序、模型与解码身份，计入重复采样和统计校准；条件关系含糊、样本不足或估计不稳时保留独立人工/任务锚和局部切片，不用单个偏差分数替代真实使用场景验收。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23485` — [Contextual invariance exact-v1](https://arxiv.org/html/2603.23485v1)必要Results/Methods/Discussion/F1–4文字/T1/Eq1–2；仅固定target下非targetcue/null/order条件分布诊断。原joint由marginal乘积定义时ΔC≤0与19–52%不可约比例未闭，强CbD/因果解释隔离；保binarynorm/valid与279角色人口/quantization混杂/全部复测费用，不采通用公平、安全或单prompt真值，未核全部补图/code/复现。
