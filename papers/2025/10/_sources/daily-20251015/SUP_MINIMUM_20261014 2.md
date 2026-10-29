# Oct15三个具名最低/必要风险有限提案

作者Kierkegaard，2026-10-14T10:38:20+08:00。供root即时独核，不等待日期或six，不预签正面Source/Books。

最新覆盖：root [独核§11](SUP_INDEPENDENT_20261014.md)已actual完整提案/原v1题摘及所列必要域，Spare/TBAC/HE三个窄P与必要边界通过；Spare最低N已闭合，不再ordinary。不授公开日/评分/完整Source/Books或双owner写入，已读域不重。

## 12948 SpareCodeSearch：N→窄P提案

实际[精确v1 PDF](SUP_SPARE_v1.pdf)请求exit0/200、813442字节/4页；已读§II–IV完整方法、Tables I–IV及limits，引用/在线附录不采用（本地输出含引用不算审阅）。

Zoekt每revision独立shard，completion前后文与原file差分作query来源，Tree-sitter提取identifier构造19组，按frequency/proximity/AND→OR等逐步放宽，第一nonempty即停；rank文件或snippet并按token余量打包。**窄P仅跨revision retrieval的时间身份与命中率/生成正确性分责**：TableIII跨shard命中增，而§IV明确未对single-shard的completion质量做比较，hit与quality相关性没证；跨shard没revision顺序会从未来取context，增益可能含泄漏。这个具体对照/资格缺口能修正“低成本检索命中增即completion改进”的判断，不以成熟keyword检索组合或榜单第一准入。

原private Kotlin/Python chRF与public分开；§III 18/12min是两集合完整请求与retry的总墙时，不是单query0.2s性能/无总费。M3 Air/default1CPU/8GBcontainer，不签等质量优semantic search/低资源普遍可部署。未知公开日不score/入表；相关未来论文/全代码和线上Appendix非本最低门必要，不机械扩读。唯一潜在owner AGENT-RAG，Books未做。

## 11414 TBAC：具体双门P提案与必要安全反侧

作者实际精确v1 ABS完整AB/三作者/单v1，及本日[HTML](SUP_TBAC_v1.raw)请求exit0/200/105378字节；§III–VIII完整定义、流程、两个概念use cases与讨论已读，数学保TeX不删除。root消息亦已实际同域，不请求第三遍。

静态task-policy查表不能覆盖新任务→LLM提出 `(Π,Rcomp,υ)`，manifest有外部资源风险ρ，任一risk/uncertainty越阈值先human approval、否则CTS发短期capability token交PEP执行→**窄P提案只双门状态/模型建议与最终授权分责接口**，不是风险加不确定性名称本身、通用成熟least-privilege或已证明安全。风险门提供业务资产代价、模型门提供建议不确定信号，两种不同来源不能由一个低分互相抵消。

必要反侧：§V-B提供MC dropout/ensemble/stochastic disagreement几种可能法，V-C实际流程仍让同judge自估υ/计算Rcomp；self-report或disagreement不证明校准安全/计划正确。max风险只按resourceρ，不自动按transaction/effect或整个数据flow算风险；语法合法Π不证明最小权限。§IV明示prompt injection风险但主贡献只前两风险，§VIII将注入防御/校准留future。§VII相同task缓存整个tuple却未给manifest/policy/model/主体权限版本的cache失效规则，不能重复利用旧token/授权。两个use cases是示意、没有ASR/latency受控实测，不采“robust/trustworthy”。只接口提案潜力，无完整执行实现/生产授权保证，未知日不score/Books；唯一owner候选PLATFORM-SECURITY待资格后具体比较。

## 12343 HE token-order：窄P与root已经实读的必要权限

作者本日实际[精确v1 ABS](https://arxiv.org/abs/2510.12343v1)完整AB、五作者/单v1，34页不变机械工作量；Advanced当前与原Atom含该ID只元数据，不借原Atom存在称原47已读此稿。

token顺序在普通onehot lookup本可重排等价，但HE的approx onehot使embedding误差对相邻token距离敏感→TSP ordering＋postprocess减少该近似引入的误差→**窄P：token编号/算子近似耦合会改变加密推理表示稳定性条件**，不是宣称全LLM隐私/无损、仅引用TSP成熟名或collapse宣传。

必要原域沿root本轮actual消息：已实际精确v1 HTML§1.2/§2/§3.1–3.3前段，Algorithm1后处理不保证exact/归一，隐私角色只honest-but-curious，不授通用恶意server/客户端输出/侧信道安全。本文明确将此必要读层归root，不伪称作者已读全部34页理论/实验或其余段；若root保存该层可直接引用，无需再次下载。未知日无score/正式/Books；唯一owner潜在INFER-TENSORRT-LLM的数值执行接口或PLATFORM-SECURITY的威胁分责，日门若恢复再取拟采用命题唯一owner，当前不双写。

三项均准入/必要边界提案，没有DAY/FINAL。Spare最低门现在已有具体事实可以裁决，不继续当普通N待全文；TBAC/HE供root按实际已读域即时校准，日期出口另一次有限集合，不为所有P深审。
