# Nov25 AMD 公告与窄通信命题独立复核

复核者root，非报告作者。检查时间2026-10-04T16:33:08+08:00。仅 [SYSTEMS_CALIBRATION_TAIL](SYSTEMS_CALIBRATION_TAIL.md) 的AMD单项，不复核其他三个日期保留项或本日全部来源。

实际读取AMD原新闻/正式署名分发/作者公告中的report release与链接，原件raw-amd-official-release-sparoa18.json。正式分发字段Nov24 09:01 ET，IANA纽约转北京为Nov24 22:01；分钟范围[22:01,22:02)落窗。核的是厂商明确technical report发布公告事件，不把这个时刻改成arXiv最早公开或submitted。身份与采用范围相容。

实际读取exact-v1 §III-A/B/C及必要硬件/rails-only、optimizer上下文，raw-tail-core22/controls23/24。可支持的窄命题是作者MI300X/xGMI配置下，subgroup参与者、collective类型和计算重叠共同限制有效通信；训练有反向计算重叠，长上下文推理不能继承同样余量。正文§III-C直接说明这一条件，图注为RCCL microbenchmark而非端到端训练普遍收益；不将NVSwitch/AMD比较写成所有硬件定律。

未采用§V-D相邻rank SendRecv作为任意超大tensor的正确替代AllGather；它的有效性依赖分片跨rank情况。§V-B二维Muon约束与后续分配表述不一致亦不采用。不核实测复现、源码或全模型领先，shape/保存数字只是原稿上下文，不外推生产成熟。

准入与2+2+2=6通过；受限标准证据及 **仅报告** 判断通过。实际对读Ch36开篇、Alpha-Beta通信模型、有效带宽受topology/message/concurrency/overlap影响的正文及collective参与者/completion层次；Ch35开头和Ch37 TP degree/节点内高速域非绝对规则交接亦核。既有设计已要求按实际group和硬件测量，未发现必须替换该长期决策链的增量；不因AMD名字未出现制造diff，也不声称具体xGMI带宽数据已被书稿逐条覆盖。实际Books写入0，无POST。

本项不会让其他日期保留获得正面Evidence/Books，也不替代Nov25最终六部分/普通工作验收。作者同步该单项即可，已核原文不重复深读全部附录。
