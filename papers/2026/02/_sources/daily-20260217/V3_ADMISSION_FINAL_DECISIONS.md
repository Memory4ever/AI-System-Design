# 最后36项作者贡献裁决

完整题摘/具体链见 V3_ADMISSION_FINAL_ABSTRACTS.md。root已实际读36份完整题摘：30项贡献准入通过，12684一次core准入另通过；5项12544/12714/12746/12756/12876需要一次决定性核心，不把作者35项提案当正式准入或全文队列。四个决定事实另单次core完成，以下只校正本项论点：

- 12566：Table2实际multi400steps2166.4GPUh，域内各200steps（math2172.8/coding3187.2等）不是matched全budget。准入是mixed-vs-merge实际能力干扰的受限比较，不授mixed免费协同/原verifier eliminates rewardhacking。只采用非Science能力对照，不扩Science研究。
- 12635：HiF4三层64/8/4scale与NVFP4global scale不同，4.5bits/element vsMX4.25不称同storage。Key/Value/activation次序不同：activation NV优于HiF、Value INT优于MX，直接修正“更多层级一律更好”/单format全张量适配；不授本文格式为新发明，HiF4引用既有Luo2026。V3_ADMISSION_12635_FINAL_CORE B65–88。
- 12746：同总20experts、相同replay/loadbalance比较2/4/6/8与其他分配，含2/2/8/8更深但更差，具体容量分配效用不是只有expert+replay名；replay去除尤其English灾难但不认定layer配置普适。必要core B98–120。
- 12670：exact-v1是84tasks/11domains，不继承current87/8。同task无/curated/selfgenerated和harness差别是评价增量；module数量分层并非同task随意增加数量的causalablation，2–3最优与length效应均收窄，16tasks负面保留。B156–192局部反侧/limits已读，Science应用任务不采用。

12684单次core已揭示具体cleanprefixcopy shortcut→RoPE offset+Λmask限制later directattention→reactivity/continuity交接。作者准入2+2+2=6，原mask限制不保证间接路径绝对无泄露；不用80ms consumerGPU数字作准入。V3_ADMISSION_12684_CORE B33–45，必要证据还需有限控制/实际部署边界。

13197 root已明确具体EX通过：普通ResNet18/MLP RGB-mask/2Dgoal grasp学习，未建立本主线新增机制；并非所有机器人方法范围外。12966成熟diagnostic组合EX通过，反证/原证保留。

此前47贡献准入继续复用，本批31项及12746固定容量allocation已root校准，12618较早publisher事件退出本窗firstpublic。最后3一次core EX（12714/12756/12876）已root独立打开exact-v1核心通过，具体成熟工具/领域forecast/扩题库理由与保证信号见V3_ADMISSION_LAST_FIVE_DECISIVE.md，普通准入待办0；当前贡献通过78、EX51。12544必要dated forum外部403日期终态、12618较早事件恢复线索均隔离。12499 official abs ICLR2026及具名OpenReview同题同摘要原稿已有限核identity，必要forum timestamp 403无法恢复，root裁决日期终态通过，不授本窗首公开，留下精确datedforum重开条件。故当前77项日期确认贡献候选，其余有效身份原证复用；后续具体新日期反证只纠偏该项。来源已有限收口，不扩库存/会场。
