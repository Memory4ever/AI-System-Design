# 10564 Adaptive RAN Slicing：最低关闭判断

仅03-13补Mar12 BJT自然日。第三完整exact-v1准入及决定core校准有效复用；本次直接重对 SUP_ABS3_10564.txt 的题名、五作者、完整abstract/Comments/history，仅v1、无可见撤回/纠错说明。DATE4原字段非作者日级夹证有效：submittedMar11T09:14:56Z、registeredMar12T02:04:37Z，不把Updated当公开。SUP_ADMISSION_DECIDER_MANIFEST_RESULT.json官方 https://arxiv.org/html/2603.10564v1 GET200/249318bytes/UTC2026-10-09T12:52:43.672608Z，SUP_DECIDE_10564.raw/txt为实际原件，不重抓有效source。

## 实际新增与拟评分

有限history下Actor在线出动作，离线Reflector读已完成完整轨迹、给step二值标签与建议动作；对negative prompt多次重生成，按是否匹配建议动作造positive，再KTO更新。准入保的是这个未来视角建议→语言匹配扩充的局部训练配方及实际人口边界，不是RAN领域数字、Actor-Critic改名、KTO成熟目标或“reward-free”宣传。

拟 Design1+Reach2+Durability1=4：新增本地reflect-label/match/prune配方1，真实环境反馈经教师离线标签进入policy learner跨边界2；所提供的证据仍是Qwen3-4B/DeepSeek-R1与一个RAN simulator的工程观察1，未额外确立新的通用credit、反事实执行、admission/recovery机制或稳定选择界。不会把借用的“教师建议不等真实反事实/需独立验收”成熟约束抬到Durability2，也不因Books主题/阅读成本/潜力数决定分数。拟4分最低关闭、不进一步采用，Books0；非准入EX/非已有覆盖新实验，未formal。

## 为判断实际读足的原证

直接读§III R-MDP反馈/implicit reward定义（660–875必要段）、§IV完整Actor/Reflector/bi-perspective与Algorithm1/2（875–1695）、直接KTO loss/labeling说明（1695–1885/1950–2065）、§V setup/两个traffic配置/TableI–III/对照/全部结果和§VI限制（2065–2445）。未看图曲线像素精点/代码/真实网部署，不把可选未读附件列外部受阻；不将Eq7描述性argmax当新的证明。

Algorithm1 Actor只读决策时过去history，Reflector动作建议含完整未来H，是离线监督而非部署未来输入；建议本身没有执行替换后的trajectory。Algorithm2 line11–14只 π(I_t)→Extractor→动作等于建议即positive；正文的“matches or aligns”比伪代码exact equality宽，精确匹配实现/阈值ND。Line16 probability>ρ后停止该prompt重生成，但ρ、概率估计/校准、rollout m与optimizer具体数值在这些方法/评价中未披露。§V明确这种refine-rollout **without additional environment interaction**，不能叫真实反事实搜索/验证过的动作效用。去handcrafted scalar reward不等无监督：environment M/任务目标、DeepSeek评判及KTO二值偏好仍是监督；§III仍定义implicit r_lang。原“fine-tuning rather than gradient updates”不是数学互斥，只不采该措辞强推。

§V custom Python/ns-3 simulator，urban propagation/on-off流量、300-step trajectory、100ms决策周期；该周期是模拟设置，不是测得Qwen3实时完成时延。Qwen3-4B Actor/DeepSeek-R1 Reflector，Reflexion同backbones，但新系统六次KTO迭代/重复sample/更新预算与只prompt记忆不同，未做相同总费用或单组件/同标签来源对照。RL80round×20trajectory=1600，与本文一训练轨迹可说明作者环境交互数不同，不等总sample/全训练费用、泛化到开放control更高效。硬件、precision、batch/LR、训练/反思/生成token总费、独立训练repeat seed/CI及heldout traffic/channel协议在这些评价 **Not Disclosed**。

TableIII SF SE5.354低SAC5.748，QoS violations8.561高PPO1.997，只有联合utility25702.2最高；较Reflexion25314.69的联合结果及reconfiguration21.091 vs29.454保留，不能说每项统治。Fig3文本“一轨迹六次KTO/约33%少reconfiguration”描述作者受限运行，不认证counterfactual建议质量。Chosen/rejected KTO rewards趋零是模型/reference score，不等全部可行动信息已学完或真实policy稳定；共同Reflector误差可被重复采样放大。§VI明确slow inference阻碍real-time部署，不授100ms生产控制、现实无线网络安全或连续长时generalization。

## 不进一步采用与owner路由

ROADMAP唯一训练信号owner `TRAIN-RLHF` Ch31。本次实际完整读Ch31 176–194多轮trajectory preference/反事实与credit分责、889–903事后teacher条件和原student input/独立outcome/全费、1030–1067 terminal/step credit及弱future-sampling资格。现文已有事后教师监督与实际状态/反事实验证分开，不把模型生成建议签step因果信用；这不是把本稿数据/新实验说已整合。新配方目前没有超出局部matching/KTO重复采样的稳定可验证设计选择，故无需制造第二owner或Books差额。Ch33不是KTO owner，不因preference名转GRPO；RAN只评价负载，不新开网络控制章。

若提供独立执行的建议动作/反事实trajectory、同标签/同费用/多traffic稳定对照和新的可核admission或恢复规则，可定点重开新增命题。本次不为这些未来可能性遍历代码/附录或另做实验，也不把一般未披露标外部精确阻塞。请非作者核实际增量/4分最低关闭理由与必要原件；未formal、未授DAY。
## root非作者后续实际裁定

root直接读Algorithm2全部/完整RfR邻接、TableIII多指标反侧及§VI实时限制，与有效日期/身份层复用，最低1+2+1=4、不进一步采用Books0 PASS已记录主独核ledger；已正式同步本日报第28项。局部配方仍为贡献通过，不改EX；没有声称全实验复现/新的长期约束已吸收，不授DAY。

