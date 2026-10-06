# 02/20 第二批四项有限必要证据与 Books 决定

均为 `exact-v1-bodies/2602.<ID>v1.html`，不是旧完成标签或题摘。下列位置按 `V3_extract_html.py | awk 'NF' | nl -ba` 可复查；root 非作者已经实际核原文、owner 差额与两处写后邻接。首公开推定复用 V3_EVIDENCE_FIRST 的同ID Registered 上界桥接，不授伪造公告点。

## [16246 Proxy State-Based Evaluation](https://arxiv.org/html/2602.16246v1)

§3/4（131–175）全轨迹 prefix 推断结构化 proxy state，tool 输出 success 才更新 write state，tool simulator 继续读取它；scenario goal/facts/expected final state 与 behavior 分开，judge 也只是轨迹到判断的映射。§5 原文默认 simulator/tracker/judge 写作 **GPT-5o medium**，不擅自修正该身份。208 synthetic commerce/account scenarios，157 train/51 test，power persona、max10turn。§6.2（229–235）固定其余组件只换 GPT-4o tracker，tool hallucination 1.33±.53→3.61±.88；删除 system/user facts 分别增加对应 hallucination。它说明生成状态与模拟响应的反馈依赖，不能说明 proxy 是真实业务数据库。真实工具效果、生产可靠性或无误判保证均未证明；未核 artifact 或复现。

中心可靠性争议：主文/结论泛称 human–judge agreement >90%，Appendix A（344–361）对随机 n50 conversation 三方 agreement 给 goal completion82.7%、tool/user94.7%；比例与n50精度也没有足够说明。不用总体宣传授 goal judge 可靠性或真值。保留双方，不通过删表或降分解决。局部方法与有限反馈误差仅报告，中心可靠性 **争议/Books 暂缓**；重开只需同版本勘误、原标签与各维度分母/协议，不请求全部无关代码。

actual coverage：TRAIN-DATA [Ch27 Synthetic API State](../../../../../books/part-04-training-system/27-data.md#没有真实后端时synthetic-api-state-只能是派生训练状态) 478–492 已承载 history-conditioned simulator 只能提交派生状态、real backend/effect authority 与可执行状态证据；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#living-world-evaluation外生变化必须进入-run-identity) 1194–1221 已承载 simulator/run identity、同源优化裁决和live-state reference。不能因少一个 full-prefix 配方而把这些已有原则再包装为新增长期链；这些位置不被声称覆盖未成立的 >90 中心结论。本次不写书。

## [16313 MemoryArena](https://arxiv.org/html/2602.16313v1)

§3 构造 multi-session 依赖 shopping/search/travel/reasoning episode；内存起始清空、episode 内持久，不用独立静态 QA 代替行动依赖。§4.1（613–624）同task agent GPT-5.1-mini 比 raw history/external memory/RAG；§4.2（625–630）PS 是子任务完成比例，SR依environment：shopping/travel最终全局约束，search/reasoning末子任务正确；travel另sPS部分约束，不把全局success写成每步全成。原§4.3有GPT-5-mini、§4.1有5.1-mini命名差异，保留不静默修正。

§4.3–4.4（635–650）外memory不普遍优于raw；长search >120k trace 有效窗口不足时 external/RAG decay 更缓，精确重用比重型consolidation更稳。representation/training mismatch 是作者解释，未独立控制唯一因果。§4.5（764–766）端到端subtask latency 与结构复杂度非单调关系；§4.6（769–772）的理想充分belief state不是现存memory能力保证。150 shopping chains、256 search tasks、270 travel scenarios与有限formal task是协议人口，未证真实生产SLO/闭环普遍可靠。

AGENT-MEMORY actual Ch77 1211–1264/1321–1327/1625 已有因果online、组件干预、顺序lifecycle与episode约束；差额是同依赖episode的partial/终态success、depth×latency，已融入评估Neuromem后/隐藏环境前一自然段及末注。root 必要原源/actual owner PRE 与实际正文/完整邻接/末注 POST 通过，窄锁释放。SR依environment释义再按复核做窄明确，不授raw普遍优越或唯一失败因果。未核实现/复现。

## [16444 RoboGene](https://arxiv.org/html/2602.16444v1)

§3.2（190–202）valid task 成功才增scenario/object/skill频率，scenario LFU后semantic子集内取对象/skill候选集，不强迫一对象。§3.3–3.4 反思只是LLM物理/novelty/constraint提案，反馈记忆不是物理证书。§4.1与D（1258–1338）每method900tasks、robot类各300，physical feasibility 五次teleoperation；不是autonomous policy。§4.3（431–446）三个robot每三个task、每task250轨迹，ACT/pi0.5与20rollout，另pi0 pretrain150+150tasks、五unseen各15demonstrations、不同epochs，不能把下游所有收益归LFU。

关键反侧Table5（1282–1327）与F（1406–1423）：加入object sampling后对象685但teleop feasibility .91→.85；反馈memory后719/.99。逐项消融支持多样性与grounding竞争，不证明任意任务生成安全。人力、候选库、反思与采集成本未全量归一，作者未来开源不授已复现。

TRAIN-DATA actual Ch27 610–666 已有semantic/feature/executablecoverage和primitive桶，Ch26 573–621 已有derived data/physicalcontroller；差额仅accepted-task计数、semantic LFU候选集及diversity–feasibility反侧，唯一owner落Ch27 coverage→primitive交接前一自然段及末注。root 必要原源/actual owner PRE 与实际正文/完整邻接/末注 POST 通过，锁释放；未核实现/复现。

## [16520 RLM-JB](https://arxiv.org/html/2602.16520v1)

实际§3/5程序，§6–8（114–182）每backend400 adversarial+200benign，recall92.5/97/98和FPR0/.5/2；directGPT5.2 59.57→98没有匹配多调用预算，不作全部机制归因。其他corpora/定义不同，不合成leaderboard。§9（184–190）adaptive未测、最高3x processing及chunk/threshold/template依赖；multi-turn/agent/indirect threat 是future，不授执行effect安全。代码未来发布，非必要局部论文结论访问障碍。

中心合成争议：摘要/正文称splitpayload跨块组合，Ax1.5–.6（328–377）解析失败 SafeDefault=SAFE；聚合是malicious-chunk OR和已经flagged攻击向量union，再加全文规则。全部SAFE的跨chunk关系不能被该union自行恢复；更高recall不能证明这一执行能力。保留局部分类经验仅报告，中心composition **争议/Books 暂缓**，不写正面Books段。重开需对应同版可执行compositional算法/带all-safe片段的controlled测试、明确parsefailure协议，非遍历所有附件。
