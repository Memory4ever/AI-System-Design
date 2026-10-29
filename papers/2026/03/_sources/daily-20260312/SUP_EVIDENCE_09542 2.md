# 2603.09542 — NS-VLA exact-v1 必要证据与 Books 提案

## 身份、窗口与评分

Daily 2026-03-12补充自然日2026-03-11。复用本日SUP_EXACT_BATCH3、SUP_ADMISSION_BATCH3及独立AB/日期夹证；首次公开归属只取官方公告lower与owning arxiv.content/findable upper同日，不取Submitted。当前v3存在但删除checklist/版本号本身不构成本窗重要修订，未见撤回/纠错；本次只采用[exact-v1](https://arxiv.org/html/2603.09542v1)。2+2+2=6，固定计划指针与实际完成谓词的具体owner差额深入；不借成熟RL/TopK原则加分。

## 实际读到的必要证据

§4.1–4.3/Eq2–19、§5/Table1/Fig5–8文字数值、Appendix F及G。episode开始生成固定primitive plan；masked classifier只允许原索引或下一索引，重复primitive优先advance。对象/operation query筛Top32 tokens并池为一个向量，causal Transformer读取历史/primitive/proprioception输出H=8 open-loop chunk。solver是学习型连续控制器，不是形式逻辑求解器。online只更新classifier/solver，冻结VLM与plan；segment milestone把指针变化当reward，latent prototype potential提供proxy。不得把单调指针或潜在距离当真实完成/碰撞安全，不照采KL必然稳定或最优策略保持强结论。

Table1作者LIBERO每任务一条demo的SR69.1、full-demo训练LIBERO-Plus79.4，backbone/训练/online交互及额外primitive标注不同，不能把总数据/成本等同只有一条demo；F明确1shot后仍online RL，3seeds但未给CI，LIBERO50episodes/task、Plus1episode/task。Fig5有删除classifier79.7 vs98.6、无RL91.6，支持有限组件依赖，不唯一分离预算/分类约束因果。CALVIN ABC→D为训练分布内到D的模拟迁移，不授真机开放世界。F给224RGB/归一化、Qwen3VL2/4/8B、plan最多6；hardware/precision/完整在线rollout预算、尾延迟/concurrency/SLO Not Disclosed，不引图中未核像素的速度。

G直接反证：未真正pick就提前进入place；grounding失败最常见；chunk边界不连续和slippage即使计划正确也失败。固定plan且pointer不能回退，动态错误不由单调性自动修复。指针的形式性质只保证索引不回退，不能签发subgoal completion或当前world事实。未核artifact、复现或全部附录证明。

## Books 对比与逐字 PRE（未写）

唯一owner MULTIMODAL-EMBODIED-VLA，Ch26；实际读State ownership 530–574、Skill Postcondition/Next-skill Readiness 1019–1058及闭环层级114–175，Ch25/27交接仍需本轮定点确认后方可写。现有正文已有plan是proposal、freshness、controller验证后pop、handoff完成分责；未明确单调索引可被classifier错误推进以及重复primitive advance的代价。拟最小一段插入“长任务的派生数据库也要遵守这条所有权链”段之前，保留旧段：

> 长任务还可把固定 primitive plan 的执行进度压成单调索引：分类器每次只选择当前或下一 primitive，低层学习型 solver 再读取当前观测、primitive 与自身历史输出 action chunk。这减少阶段来回抖动，却以不能回退或重新排列计划为代价；重复 primitive 的推进规则也不证明前一步已完成。[有限模拟证据](https://arxiv.org/html/2603.09542v1#S4)中，提前把 pick 切到 place、对象 grounding 错误及 chunk 边界不连续仍会失败。因此指针、分类器和计划版本只记录 policy 的进度 proposal，真实 postcondition 仍须由新观察与独立控制验收；证据不足时停止推进、重新规划或回退短 horizon controller。primitive 标注、视觉筛选、solver 与在线交互都需计费，一条示教后的在线 RL 不等于一条示教的总训练预算，单调性也不授物理安全。

Ch25/27开篇交接本轮已实读；reviewer必要Source/date/PRE通过，root授Ch26逐字单段窄锁。作者已按获准文字写入State ownership中、VLM-DEWM段之前，实际完整530–554邻接已顺读，限定diff-check通过，锁已释放。root非writer本轮实际顺读Ch26 530–556（所有权→think_on→新pointer→derivedDB→monitoring）及本人2083末注后确认POST PASS，必要Source与正文整合完成；不自签日级完成，未核artifact/复现。
