# root末三提案的非提案作者实际复核

复核者：mar14_supplement；本日03-14、补充窗口03-13北京时间自然日。仅单项Source/owner/PRE或最低关闭，不是正式报告DAY。

## 11395 ARROW — Source与逐字PRE通过

实际读精确v1 `SUP_ROOT_CORE_11395.raw` 的§3.1–3.4（B30–48）、§4.1–4.4.1（B49–75）、§5.1–5.2.1与§6（B116–146），并实际读官方v1题名/六作者/完整摘要与当前Comments。已有本ID官方日级夹证独核复用，不将Submitted独立当公开日，也不比较无关v2/v3。

FIFO与random-key highest-key reservoir两512×512容量、每batch两人口均匀采样、跨episode splicing reset和world model→imagined actor/critic由方法直接支持。论文与Dreamer/TES-SAC总容量同2^19，不采用对默认1M的公平减少宣称。五seed、中位数/IQR不是新的无条件置信保证；single-task ARROW/random归一化不同于任务accuracy。默认CoinRun .492M/1.638M、Atari ARROW未达2.02与two-cycle3.113M/3.441M反侧均实核；只采用旧经验覆盖/保留与当前任务学习预算取舍。§3.4预定per-environment reward scale及§6极端奖励差异、有限容量/固定50:50/robotics未来工作完整保留。

实际顺读Ch25 398–435完整computer-use→continual组件诊断→persistent state邻接，以及Ch24/26开篇交接。现416/418已解释逐组件forgetting与真实replay，但未解释有限容量内双经验人口、chunk/reset接口；缺口具体，不只是同主题。root `SUP_ROOT_MINIMUM_SECOND.md` 11395逐字两段PRE与原证匹配，2+2+2=6及因具体缺口深入通过：reach来自经验分布经RSSM影响imagined controller，不为成熟reservoir原理再加新颖分。两段承接组件诊断、保留旧近期FIFO合理性，不将stored sample/reset升级为环境权威，不声称最优比例/无遗忘/生产能力。可由root窄写该处并做本人末注，随后仍需非writer实际POST；当前没有Books写入或POST完成声明。
## 11397 UGSD — 标准完成与具体NC通过

实际读 `SUP_ROOT_CORE_11397.raw` §3.1–3.3/Eq1–4、§4 Implementation及两语言prompt/人口、§5.1 Tables2–4/直接成本解释、§5.2–5.3/Table5、§6（B24–105），并读官方v1题名/六作者/完整AB，复用本ID已独核Mar13日级门。block最大entropy过门只让高不确定span上云；云处理prefix+draft IDs+抽象audio feature、top-R接受/首拒绝argmax/丢suffix/edge状态对齐，明确不是target-law采样。自适应仅三个配置值与连续两块全接纳条件，不认证全设备最优controller。

Table3/4动态L低于full-cloud多数指标；Tables中的数值不完全符合正文“最佳fixed L=7”综合措辞，故不采用唯一最优长度。332/332录音、受控CPU FP32/A100 BF16 emulation、R20搜索与caption字面指标限定通过。18.2%只计draft token而非prefix/feature总bytes，隐私不由Table5打勾认证；feature仍可带speaker/content信息。没有实核完整通信实现/无线尾延迟/并发SLO或复现。

实际顺读Ch48 78–108效用仲裁→CTC bypass/likelihood→exact分支、644–676 edge/cloud身份/连续prefix/rollback与发送成本、853–873停止/offload边界完整局部。已有正文具体承载有损路由≠exact acceleration、阈值校准及双边成本/保守fallback；SEC专门R20与token上传率没有额外长期gap。1+2+2=5标准完成/已有覆盖Books新写0独核通过，不是主题相似NC。

## 11447 GCL — 最低4分关闭通过

实际读 `SUP_ROOT_CORE_11447.raw` §3.1–3.3/Eq1–7（B29–58）、§4.1–4.2/Tables1–2（B60–102）、§4.4/4.6/§5（B111–128），及官方v1完整题摘/四作者。复用本ID已独核日级门与家族去重。两模型共享监督+learned pooling/InfoNCE与JS局部联合目标、SFT表现分guide较低LR和capacity分温度是两个独立配置，不把成熟contrastive/JS/温度原理或12配对规模再计新机制分。

§4.1明确无physical robot实验；Action-F1/BERT与sentence-cos近似标签匹配不认证行动安全/控制闭环。同data独立SFT不是双模型训练无成本，baseline非穷尽调参。温度的局部最佳网格和door误判不授统一温度必失败、跨架构最优或安全性能。Eq7/其后“mathematically guarantees optimal”不作为采用结论，未认证该简写梯度为完整定理。1+1+2=4已关闭/仅报告Books0通过，保持原窄贡献候选不降EX。没有进一步全附录/代码/全模型组验证需要，最低关闭不是全实验认证。
