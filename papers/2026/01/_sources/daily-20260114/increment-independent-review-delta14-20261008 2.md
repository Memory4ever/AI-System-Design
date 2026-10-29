# Jan14 独立必要复核 delta14：07395 MCP-ITP /07226 NoisyBench

复核者：review_jan15_delta（非报告作者）。只接 root 当前两项；重新读 AGENTS、当前 Research/Report 合同、Daily 来源/Prompt/ROADMAP 与本日停点，未变化的 Books 学习/写作上下文复用，实际目标邻接另读。补窗仍 BJT Jan13 自然日，原17及原窗口/日期/评分不动。不改 Report/Books/LS/索引，不 stage/commit/push，不授 DAY。

## 07395 MCP-ITP — 2+1+2=5 / 标准完成、具体 Existing PASS

完整题摘实际读 increment-abstracts-4-20261007.json 的该行。[exact-v1](https://arxiv.org/html/2601.07395v1) 必要原件 increment-necessary-core-2601.07395v1-20261008.json 的 §3 Threat Model、§4 Methodology、§5 Experiments、Limitations、Ethics 已实际完整读，未扩 payload 模板、代码、其他附录或现实攻击执行。

准入链：只审被执行的工具或工具实现，会遗漏仅作为 model-facing metadata 的输入影响；本材料在 trusted host/user、untrusted server、看得到 benign catalog 但未知真实 query 的 black-box 条件下，令 dormant poisoned-tool 描述与合法工具一起进入 merged system context，再改变另一合法高权限工具的选择；因此未被调用不等于无行为影响，source input 与 action authority 必须独立判断。贡献是这个明确的失败边界及其受限自动化验证，不是 MCP 名称或成熟搜索算法本身。

采用边界：原文 Eq1/5/6 优化/evaluation 主要匹配 target tool name，不能据此授参数越权、真实 exfil 或已执行 effect。Alg1 将构造的 TK 重用 TG 符号，且 exact-stop=m 与 prose 近m阈值不同；不自补完整可运行搜索配方，也不把对抗搜索器当权限 owner。Ethics 明确受控环境、随机 PII、未部署到真实 live systems，故保留工具名 proposal 与现实 effect 的分界。

关键评价：MCPTox 1497 中 implicit 548 subset，来源45 server/353 tools；12 agent settings（不是12独立模型）、每 setting 单次。DeepSeek-V3 attacker/Qwen3-32B evaluator/Qwen3-8B detector，N5/W1/T3；ASR 排除 invalid/failed/irrelevant，MDR 分母仅 valid detector output，不估全部 attempt 或生产事故率。Table1 reasoning-mode Qwen8B 7.44→40.5 支持所测模式差异，不能归因为能力更强普遍更危险。Table2 relevance R 并不全改善：DeepSeek78.4→71.8、Gemini47.6→39.7；更强 evaluator 亦不全提升，early-stop 解释不是独立已识别的唯一原因。检测、候选树、shadow queries、跨模型调用和 catalog 装载均付费；精确 snapshot/precision/hardware、重复不确定性及完整费用 Not Disclosed，不授净收益、零误报或全生态防线失败。

实际顺读 PLATFORM-SECURITY Ch72:664–702 完整近文及2945–2962交接：673 已明确工具描述即使中性也可成为 behavior-guiding input；678–688 已将 source sensor、runtime influence、authority registry、step guard、deterministic tool policy 分责；694–696 绑定 model-facing artifact，tool-name proposal 不等真实读取/外传，清洗不签发 authority；2954–2957 已要求 metadata 参与决策之外的 argument-level provenance/egress 验收。其原则不以 offending tool 被调用为前提，恰好承载本次 dormant metadata→另一个 action 的边界，无须再添加同义段落。具体 Existing 不是宣称既有全文实现了 MCP-ITP 搜索器；本轮不采用该搜索器为新的可靠防线。

日期复用本日已核正常公告/ID 界限，结合 date-bounds-rest 的 Updated-v1 Jan13 02:14:58Z→registered04:01:50Z，只归 BJT Jan13；不是 Submitted/registered 单证。current-identity-next8pair2 原观察已读，本轮再次独立轻读官方当前 abs v1，无具体 withdraw/correction 说明，不追完整版本史。5分标准具体 Existing 可同步；无需 Books 锁或写后检查。

## 07226 NoisyBench — 2+1+2=5 / 标准 OnlyReport PASS，冲突命题精确隔离

完整题摘实际读 increment-abstracts-4-20261007.json 对应行。[exact-v1](https://arxiv.org/html/2601.07226v1) 原件 increment-necessary-core-2601.07226v1-20261008.json 的 §3、§4、§5 与必要 A.2/A.3/B.7/C 已实际完整读，不扩 F/G payload/示例、全图线或其他附件。

准入链：clean benchmark、更多 reasoning 或带工具的 workflow 是合理但不充分的鲁棒性启发；新增同任务无噪/随机文档/随机对话/hard-negative 的有限对照，揭示 clean 排名与噪声条件表现不一致，workflow 在该切片反退、输出努力增加却不保证正确，并尝试 gold-reference span 奖励；需要分别验收 context 相关性、噪声类型、输出努力、答案与来源支持。局部/负面验证有贡献，不因仅为 benchmark 或现有 Context 主题在贡献前关闭。

评价身份：11个数据集/4任务族，2766样本每 setting；RD 从 RULER-HotPotQA、RC 从 WildChat、HN 按 question 合成，过滤2.7%，并非真实部署噪声 prevalence。各 bench 不同 k/default8；TauBench Pass^k 测重复一致成功，其他 Pass@k 测至少一次成功，11个异 metric 的 harmonic aggregate 不变成一个共同正确性事件。k1温度0、k≥2温度.6/top-p.95、可调时 high reasoning，max output=context-input 随模型而变；Math-Verify 阴性再 Gemini2.5Pro final-answer judge，可能共享偏差。当前 source 所印分项与本文有限对照可报告，不授净化后的所有输入/服务已鲁棒。

RARE 的实际结构是对 <reference> 内 copy/paraphrase helpful-gold span 作 binary judge，与 outcome/format signal 一起 GRPO；标出支持内容不是证明模型真正用它、内部 faithful 或不存在 reward hacking。NoisyInstruct 合成 hints/hard negatives、过滤与训练一起变化，SFT 退步不能唯一归因 catastrophic forgetting，RL 收益也不能单独归因 RARE。A.2/A.3 明确 gpt-oss-120b reward，而 §4.2 为 gpt-oss-20b；不自补 judge 身份或签发完整可复算训练 recipe。该 exact recipe 未用于 Books/正面性能认证，有限监督结构和噪声对照不因此被全部抹掉。

决定性负侧与数字隔离：按所印 Table2 分项比较，Qwen4B HN 的 RARE 相对 OR 在 AIME25 25.5<27.2、Musique20.5<22.4；DeepSeek8B HN Seal22.8<26.9、Multihop45.0<47.0，而 GPQA38.1>37.1，不能称所有分项改进。Table2 caption 又称 method rows 为 absolute improvements，正文却按 absolute scores 解读，不能暗修表意。复核者对 Qwen4B RD RARE 所印11数 [37.6,72.4,63.2,33.4,28.8,32.5,73.3,50.4,89.2,39.5,40.5] 独立重算 harmonic=44.64925959385875、arithmetic=50.98181818181818，均不等印出的55.5；不采用该行55.4%总收益或据自算值替换原实验结论。本轮仅称“所印分项的反侧”，不认证所有数值人口一致或中心聚合收益。

§5 的 similarity bin、output length 与 accuracy 是条件关联；B.7 明确每题生成五回答再按已生成长度排序，没有随机施加 compute budget。不能从这种长度选择授“更多计算导致失败”因果或通用 inverse scaling law。top-ten logprobs 与最高十个 token entropy 的聚合不是完整 posterior 正确概率；wrong/correct attention 对比也不能证明 distractor attention 唯一导致错误。保留这些观察，不采用 causal compute/confidence/attention 解释。

A.3 实际披露8 A10040G inference/16同卡training，SFT bf16/8192/1epoch/lr1e-5/8GPU，RL3rollouts/bs32/4096prompt/8192response/lr1e-6、actor/reward 分配；不同 API、teacher/reward、CE配置和数据/训练/筛选费用不等同总预算。合成、过滤、judge、CE/agent工具、重复采样与训练付费，完整独立重复/总time/fee仍 Not Disclosed。原文只测所选 thinking 模型与单模态，不外推 base/instruct 或多模态。

实际 Ch75:496–548 完整读：520 已述 context 边际价值/干扰风险，534–539 有界主动读取和 exhaustion 不等正确；Ch33:253–302 完整读（分段补齐被工具输出截断的273–281），269–271 实际承 source-support/终点正确与 process proxy 分账，其他局部 credit 与字段/verifier 接口也不授内部因果。这是拟采用边界的 owner 交接，不声称精确已有 NoisyBench/RARE recipe。新增主要是该有限噪声人口的失效校准和成熟 reference-support 奖励验证，未确立新永久因果/可运行鲁棒机制；标准 OnlyReport 足够，不强造 Context 或 GRPO 两段。

日期复用本日正常公告/ID 界限，结合 Updated-v1 Jan13 02:05:32Z→registered03:57:49Z，只归 BJT Jan13，不用 Submitted/registered 单证。next8pair2 原观察已读，本轮官方 current abs 再轻读 v1/Preprint，无具体撤回/纠错公告。

精确重开条件：官方澄清20B/120B训练 judge 身份、Table2 method-row 表意及该聚合行/分项一致性，才恢复完整 recipe 与相应聚合收益；要采用 compute/attention 因果则需对应预算干预或 identification/control，不遍历版本史。本轮5分不降分、不前关，也不把上述被隔离命题当 Evidence/Books 通过。标准 Only 可同步，无 Books 锁。

## 本组状态

07395具体 Existing、07226标准 Only 两项终判已完成。NoisyBench 精确配方/聚合与因果解释限制保留，有限采用范围不受替代；无新Books差额/写入/POST。不授整日完成，等作者最终六部分 READY 后再按 root 路由验收 DAY，不启动其他日期。
