# 22413：必要定理与一个反例（中心争议，非排除贡献）

原 [2602.22413v1](https://arxiv.org/html/2602.22413v1)，本地 `V3_BLOCKS_2602.22413.md`：§2/37–77 与§4/184–190。固定 competence、i.i.d. tasks、给定truth跨agent/time条件独立；T−1轮可取得每次private decision的真实反馈，Beta正确/错误计数更新；最终公开gate只消费此前反馈。confidence是P(p>.5)而不是本条LLM自报概率。本文LLM实证仍为futurework/207，MonteCarlo仅binary理想模型，不外推相关hallucination。

Theorem1给出成功下界 `1-exp(-m^2/(2c))`，`m=sum_i(2p_i-1)q_i`，`c=sum_i((T-1)(2p_i-1)^2+4)`；假设没有写 `m>0`。原proof/187以epsilon=m应用单侧Azuma，负margin不满足这一步。

一个完全在所写假设内的反例：N=1000相同agent、p=.25、T=2、Beta(1,1) prior、critical=.5、abstain=.5。唯一learning trial正确时posterior Beta(2,1)，P(p>.5)=.75而publish；失败时Beta(1,2)该概率=.25而abstain。因此q=.25，最终独立public vote取+1/.0625、−1/.1875、0/.75，mean每票−.125。原所写下界是 `1-exp(-1000*.125^2/(2*(.5^2+4)))≈.841`；实际胜选概率由Hoeffding至多 `exp(-2*(1000*.125)^2/(1000*2^2))≈.000405`。不需要全文proof或实验复现即可暴露符号条件缺口。

这不否定有**正的gate后weightedmargin**时的集中分析，也不以中心错误将准入改EX；需要作者澄清正margin条件与适用人口，才能采用该保证。Theorem3/198还由平均p>.5与competent非退化gate推正margin，agent-specific prior下需额外核这座桥，目前不延伸声称已纠正该定理。仅保模拟人口观察，不据此写Books或授群体安全。本窗建议Disputed/暂缓终态隔离，重开所需是修正的精确定理假设/作者论证，不能用更高MonteCarlo曲线替代。

Actual owner Ch82 153–164已读：同题采样非正确证据独立、mode条件、aggregation与oracle覆盖分责已有；中心未可采用则无新增Books保证或正文，不将“已有投票主题”作为贡献排除理由。
