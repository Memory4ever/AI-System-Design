# 2603.08835 — MASEval必要Source与Ch66具体已有覆盖（非作者通过）

[exact-v1](https://arxiv.org/html/2603.08835v1)。第四包完整题摘已root独核；作者实际§3–5完整/Table2–3，§2只背景非采用证据，不核无关Appendix/代码或运行。fresh官方abs/current仍v1/comment空/无withdrawn或已见纠错；没有accepted先稿信号，不因项目有code link就重建其全release史。

SUP_EXACT_BATCH4.json原字段/freshhelper一致：Mar09UTC18:46:17截止后提交，下一批official noadvance/deadline最早Mar11BJT08为下界；arxiv.content owning/findable DOI registeredMar11UTC01:59:03为已可发现上界，落同BJT03-11夹证。Submitted/Updated/注册不单独public，待root实核。

2+2+2=6标准：固定Agent setup容易把系统表现当模型属性→3model×3framework×3benchmark交叉及mandatorytool/errorhandling与模型交互反例→整体评估身份和预算/adapter条件须随比较冻结。新增是这组系统混杂/交互证据，成熟BYO接口/trace/插件抽象不独自加分；跨模型、harness与评价，是可复用而非通用同等效应定律。

§3 agentadapter最小run/messagehistory接口，task/environment/agent/evaluator分层，setup→execute→collect→evaluate→report重复执行，清registry及git/pkg元信息支持追溯但不认证可复现/productionquality。统一runtime不保证不同native framework语义/预算等价；library feature宣称/安装可用不算作者或本轮实现验证。

§4.1全27configuration、三个benchmark各2domains：MACS pGSR、ConVerse security 1−ASR、MultiAgentBench researchcompletion/bargainingTS不是相同指标。GPT5mini/Gemini3Flash/Haiku4.5同一tier，仅T1/topP1；user/topology/tool/eval/limits拟固定但step granularity映射，framework本身systemprompt/toolmount/errorhandling刻意不对齐，所以比较的是bundled setup，不是某一framework抽象或topology唯一因果。judge/environment/attackers统一Gemini3Flash可控制身份差异，不消除共误。

Table2有model×framework方向变化，无一个framework所有模型占优；Haiku MACSTravel smol90.4 vsLlamaIndex59.5相差30.9pp，说明身份不能从模型名字移除。六domain平均range model14.2/framework12.4与SD7.5/6.5只是异质六slice描述，非统计效应等同、置信区间或所有能力tier的普遍比较。§4.2作者trace分析GPT5mini/smol mandatorytool使反复clarify，碰5turn上限后同工具重试达23次、≥10倍token只是该组合定点现象，本轮没独跑原trace、不授循环已复现/漏洞已修。需要完整工具/错误消息/预算与adapter身份，不能只优化model再签全系统可用。

Table3 LoC不计prompt/data且format/docstring/ablation已调整，35–57%仅两重新实现代码规模不是维护工时/完整可靠性或运行成本节省。§3.5借DISCO 1%task/2pp文献估计非MASEval本实验不能拼cost；硬件/precision、精确model/provider/frameworkrevision、总token/延迟/费用、seed/repeat人口与CI本轮必要主文Not Disclosed。只采用上述有限交互与测量身份边界，不采用排行榜最优/productionquality/所有library兼容保证；可选代码无需为该边界另建hold。

唯一owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。actual285–310完整局部：287 promptadapter/toolserialization/retry/timeout/env初始化影响行为；289 model×benchmark×harness×environment×scorer，轨迹/componentreceipt与adapter语义等价；297统一层增加兼容/版本/运行费、稳定专用脚本共存；299/301比较需realized配置/受treatment影响范围等价，不从两个run完成认证因果。actual1049–1087模块probe固定其他组件但不取代完整rollout与publication bundle、1495–1527mock测试只证剩余orchestration/真实integration分责；Ch66/65/67开篇交接已读。具体上述身份/反复retry/实现捆绑比较与有限反例都被正文实际承载，不只是同为evaluation主题，拟已有覆盖/NC，无Books新段。必要Source/日期/具体NC待非作者核，未授DAY。

实际后续裁决：root非作者已读精确v1§3–5/Tables2–3、原owning/findable字段与Mar09截止后→Mar11BJT夹证、Ch66 285–310完整identity/realized论点，接受6分标准Source及具体已有覆盖。保留27configs的bundled setup、六异质slice描述范围、作者trace与LoC边界；未复现、未写新Books，不授DAY。
