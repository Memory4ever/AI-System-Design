# 11394 必要 Source 与具体 Ch66 PRE

作者 mar14_supplement；2026-10-09T13:19:32Z。root实际决定core准入已通过；此文件只推进必要证据/owner，不自授独核或DAY。

## 身份、日期、评分与实际读取

[精确v1](https://arxiv.org/html/2603.11394v1)，本地`SUP_GATE_CORE_11394.raw`；完整title/8作者/AB/当前可见history为`SUP_TITLE_ABS_11394.raw/.txt`。未见当前事件具体纠错说明；可见v2/v3存在不证明重要修订，不追版差。日级arXiv夹证见`SUP_DATE_SECOND.md`及`SUP_DATE_11394.raw`：v1 Thu00:14:35UTC晚Wed截止，owning/findable registered Mar13 01:54:32UTC给同日上界，不单用Submitted/Registered当first-public，未识别具名早稿信号。

实际必要阅读Methods全部B20–34/Eq1、Results B35–47及Discussion/Limitations B48–55（恢复时重读B16–55连续）。不读所有临床案例/参考文献或附件。新增命题评分 **2+1+2=5**：固定题目事实但partition answer-space产生正确保持/安全abstention/true-vs-false switch三个不同测量边界，重要评价设计delta；仅局部conversation evaluator，不借用泛Agent安全或跨生命周期加Reach；人口/分母可复用。最低标准审阅已够；发现Ch66具体信息身份差额后必要深入owner，不把全主题关联当gap。

## 支持与反側

固定临床事实/问题，single-shot全选项对二元初始选择；positive以truth为target，negative删truth改NA，后续每轮新distractor，首错误即停止。C_T=(1/n)sum_i prod_{t=1..T}1(answer=target)使用初始同n，是累计survival；它不是到达该turn人口的conditional accuracy，乘积下降不能单独因果识别模型退化。Two-turn flexibility仅从初始正确NA人口继续，对下一轮true answer与another false distractor的switch分别统计，不能混作所有初始题目的正确率。

15开源1–72B、4家族8bit/llama.cpp/A100或H100，两商业API GPT4o指定snapshot/GPT5.2 Jan2026；temperature .7、fewshot开发/测试分离。开源每数据集1200、API400个unique samples是不同人口；invalid parsing排除，未认证全部真实用户。MedQA/MedMCQA/JAMA CC仍是MCQA option perturbation，即便原 vignette非结构化也不是真实诊疗多轮日志。

Results positive degradation是多数而非所有模型；<4B部分模型多轮优于single-shot，故不采用所有conversation必恶化。negative在本文protocol反侧更差；JAMA GPT5.2真建议switch93%/错误20%，GPT4o94%/53%说明真信息采纳率高本身不认证selective use。无需引用临床准确数入书。RLHF/sycophancy仅conjecture，没有matched training checkpoint的因果干预；不能由本文建议减少澄清、泛化所有Agent任务或给医疗操作建议。重复seed/CI、全部distractor-order控制和端到端费用、商业precision/输出长度/SLO为Not Disclosed；线上SLO不适用本文离线判分。预算、上下文长度和option presentation同时变化，未全隔离内部机制；无artifact核验/复现。

## 实际 owner 差额

ROADMAP唯一owner `PLATFORM-EVALUATION-SYSTEM` / [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。实际连续读2680–2745：Stateful保存turn frontier/生成policy，随后Context Length vs Intent Supersession明确真实revealed/withdrawn values、current intent与配对no-change control；没有解释**事实不变、仅候选分次提供**的另一控制轴，positive保持、safe abstention和true-vs-false switch的原始/conditional人口也未分开。实际175–215 stream局部已有OAKS真值Change/Stay，但其真证据phase更新不等本稿选项压力。Ch65/67入口确认评估身份/分母属于Ch66，不将在线monitor sensor或Reflection重写。

拟窄写在`### 多轮评估要区分 Context Length 与 Intent Supersession`下前两段之后、用户执行中修订的配对轨迹段之前。原no-change/intent/sideeffect边界全保留；两段拟文如下，待root实际Source/PRE与写锁。未写共享Books。

## 逐字两段提案

事实没有改变，也不代表交互协议没有改变。还可以固定问题与事实，把原本一次给出的候选分到后续轮次：先让模型在正确答案与一个错误候选之间选择，或在缺少正确候选时选择“None of the Above”，再逐轮加入错误建议。评价应分别观察初始正确选择的保持、安全拒答的保持，以及从初始拒答转向真新候选和错误候选的比例；只看“会随着新建议改答案”，无法区分有益吸收与盲目顺从。[受限的 stick-or-switch 对照](https://arxiv.org/html/2603.11394v1)提供了这个区别，但这里新增的是候选的可见性，不是事实或用户意图的 supersession，不能与真实任务修订共用一个更新成功率。

这类序列的分母和停止规则也属于 EvalSpec。若首个错误就终结，累计保持率应以最初全部题目为分母，并把此前任一错误持续计为失败；到达下一轮后的条件准确率则描述不同人口。从初始正确拒答者继续测真、假建议的切换，又是另一个条件切片。判分时保留这些分项，并绑定事实快照、候选/顺序、prompt、sampling与轮次预算；否则更高的真建议采纳率或平均末轮分数可能掩盖错误建议的采纳。代价是配对调用和轨迹保存，证据仍限定于MCQA候选扰动及所测模型，不证明真实对话必然随轮数退化或RLHF导致该行为。事实、授权或标签不可独立核对时，返回Unknown并保留固定题/独立outcome对照，不能由conversation score替代真实更新验收。<!-- source-family:SF-2026-ARXIV-2603-11394 -->

Review note拟记录：精确v1 Methods/Eq1、Results正负保持/真假switch和直接Limitations；必要Source/PRE通过后实写、非writer POST待实际；无artifact/复现/诊疗或普遍安全保证。root可作为writer，作者作实际nonwriter POST。
