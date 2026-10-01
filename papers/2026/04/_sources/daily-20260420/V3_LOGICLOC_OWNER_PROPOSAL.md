# LogicLoc 有限 source→owner 提案

作者：`/root/apr20_resume`；尚未独立采用、未写Books。必要原文与反证见[v3-reopen-notes最后五项](./v3-reopen-notes.md)，原始[2604.16021v1](https://arxiv.org/html/2604.16021v1) §3.1–3.4.3、§4/T2–4、§5。

评分2+2+2=6；实际Ch76窄缺口决定深入比较，不以新名称抬分。`AGENT-RAG`的“procedural index”把corpus派生成导航plan，并要求回到原文；邻接GraphRAG已有构图identity/source span。尚未具体承载**结构化查询返回空关系时，mutation只能是diagnostic且不得静默放宽用户条件**。这不属于Ch78有副作用授权，也不属于Ch77持久化memory；owner是RAG检索计划/证据可用性的边界。实际顺读Ch76:405–432、528–568及Ch77开篇，旧lexical/chunk路径保留。

拟在procedural index段末、`RAG不消除Hallucination`前嵌两段；不用另起论文小节，literal如下：

> 对结构约束明确的代码或关系库，另一个分支把source解析成带位置的facts，让模型只提出逻辑查询，再由确定性引擎执行。parser通过只证明语法可执行，结果仍可能因猜错identifier、join或predicate顺序而为空；也可能因为原条件确实没有匹配。可以对中间空关系做有界字符串放宽或单条件移除，观察哪条限制影响结果，把变体identity、row count和有限tuple样例作为修订反馈。变体返回的记录不是原查询答案，不能为“找到东西”静默削弱用户条件；最终查询仍须保留明确意图并回指source。
>
> 这把深层结构遍历从模型token交给facts和query engine，却增加解析覆盖、facts更新、查询合成与诊断执行成本。所有探针仍为空或执行失败，只说明在这组有限探针下未恢复结果，不证明开放代码库不存在答案；放宽后非空也不证明原限制错误。受限Python定位实验支持这条diagnostic分支，未证明完整程序语义、跨语言覆盖或普遍低延迟，额外反馈在部分配置反而增加时间。关系不稳定、事实抽取不完整或无法确认查询意图时，应保留原条件、报告未决并回到原文检索/人工核对；有明确标识符的简单任务继续使用词法或chunk检索。

对照边界：225人工构造非空query/9Pythonrepos与单repo负例，不是同题随机去keyword干预或泄漏排除；前25子集VAL→full Qwen时间104→136秒而ExecSucc不变，表内Claude分母未统一。正文不采用表内ranking、39.3秒/16.2ktokens为生产SLO，也不把“stable-empty”升级为形式化absence certificate。唯一成熟复用是Datalog确定执行，新增的是**empty-result诊断与原query authority分开**，不是所有检索可证明完备。

拟Review note需保：source-family `SF-2026-ARXIV-2604-16021`、exact v1、上述有限段落/反证；只有独立源→当前owner通过、协调写锁、真实body写入及非作者write-after完成后才计Integrate。

## root 非作者有限采用复核

实际打开官方 v1 §3.3、§3.4及§3.4.3、§4.3/§4.3.4和§5，比较当前Ch76 procedural index与前后原文authority、Ch77状态边界。五种mutation确为probe而非最终答案；stable-empty明确还包括执行失败，fragile-empty不证明原条件错误。Table4 Qwen VAL→Full时间104→136秒、ExecSucc均84.12，Claude比例分母与“前25”描述未统一，故不采用普遍低延迟/完备否定或表内全面优越。两段具体缺口与共存路径成立，source→当前owner窄采用通过，实际写后另验；不预支整合和日级完成。

实际写后：root顺读Ch76 procedural index、两段新正文及其后groundedness；source-family锚点在机制正文，变体不冒充原答案、有限失败不证明不存在、解析更新/反馈成本与词法/chunk回退均保留。没有把Datalog名字或作者质量排名代替设计论证。非作者实际写后通过，Review note与正文一致，不是实验复现或日级Gate。
