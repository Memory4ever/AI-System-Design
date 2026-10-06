# 11351 Novelty Adaptation：真实增量的最低评分

mar14_supplement；精确[2603.11351v1](https://arxiv.org/html/2603.11351v1)，缓存`SUP_GATE_CORE_11351.raw`。五作者完整题摘/v1身份和当前v3可见history已核，current说明没有具名撤回/纠错/重要变化事件；版本号不触发全版diff，也不采用晚版正文。owning/findable DOI/official URL/arxiv.content、registered Mar13 01:53:31UTC与 v1 Wed22:38:05UTC，合用官方正常公告/非预分配下界支持 Mar13BJT 日级日期。`SUP_DATE_SECOND.md`/`SUP_DATE_11351.raw`保留实际字段，不用submitted/registered单独作首公开。

已校准窄准入保持：缺operator导致原planner无路径→LLM提出一个operator、symbolic lookahead早停、ordered effects分phase→local连续域配置改变探索与奖励候选分配。最低 **1+1+2=4**，新增是既有BFS/ToT/selfconsistency与PDDL、PPO/ordered reward curriculum、多候选淘汰的局部结合，没有证明新的operator语言/可执行保证、反馈可靠性或可推广资源边界。不给借用的高低层分责、真实effects验证原则、任意模块间传递或GT假设扣回的成熟边界另计重要机制/System Reach。不是“只要组合就排除”，该局部机制已准入，最低投入由新增命题支持范围决定。

实际必要范围：§II-C相关继承、§III-C问题假设、§IV–V Alg1–3完整行/效果排序与executor保留、§VI/ TablesI–II及§VII–VIII直接反侧。LLM每状态至多补一个operator，symbolic BFS/lookahead只证明给定符号模型有路径，不证明真实动作可执行；predicate集合足够、novelobject已能识别/分类是前提。Alg3先达到当前effect再解锁后者，三reward/PPO候选按阶段成功淘汰、续用最优旧snippet，并不赋LLM reward真值权。CheckEffectSatisfied当前直接用ground-truth state并查其它实体未意外改变，不是已部署perception；真实机器人、predicate invention/多并发novelty均未来工作。

十seed仿真与API规划对照、one-million-step OD cap不能证明同总训练/LLM/候选预算下统一优势；Coffee-drawer TableI 7/10而非all domains guaranteed。额外候选与API开销、符号/感知/仿真条件都保留，不由SEM/p-values推完整机制因果或物理安全。**已关闭/仅报告、Books0**；不因RO小场景、既有Books、文章长或费时取消贡献，actual operator/feedback接口原证保留。mar13_admission_review实际必要core/身份日期/最低关闭独核通过，见本日SUP_INDEPENDENT_REVIEW_20261009.md；不授正面标准 Source 或 DAY。
