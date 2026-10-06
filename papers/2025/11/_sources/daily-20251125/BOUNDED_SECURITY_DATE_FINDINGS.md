# Nov25 有限证据与日期恢复停点

只记本日具名材料，不新增宽月表全文队列。raw-security-controls-locations、raw-security-api-correction-core、raw-finite-date-correction2、raw-named-artifact-date3、raw-author-release-boundaries4、raw-artifact-release-and-method5、raw-micro-method-location6、raw-official-date-provenance7、raw-murmur-earlier-public-trigger8、raw-api-caller-and-earlier-version9、raw-finite-mechanism-controls10均包含实际request/response；新调用request对象保留实际执行参数，不补造未执行的分页。

## MURMUR：受影响安全深入，不以日期含糊删反侧

[exact-v1](https://arxiv.org/html/2511.17671v1) §3.1～3.3、§4.1～4.2、§5.1～5.3及§6/ethics已定点读。攻击者是普通用户、不能编辑历史；代理读取全局history/tooltrace，而良性用户只见本组消息。ASR要求为良性用户服务时出现攻击动作，APR条件在至少一次成功攻击的session上，不是总体生产风险率。有限模拟与作者自控账号支持传播路径，不证明所有部署脆弱。task-clustering用GPT-4o-mini分组后限制history可见，仍有组内攻击、classifier错分与Slack/Airline TSR退化；不采“根本无法隔离”或零ASR=安全保证。只采用身份/任务可见性不对称的受限风险，未核实现或复现。

日期：DataCite v1 Updated=`2025-11-25T01:03:55Z`、created在03:54，不从跨截止上界直接排除。具名检索两轮未找到可核作者精确公告；作者Peiyao个人页可见论文但无精确首公开。搜索发现具体OpenReview `wwXP9eqWeW`，已触发按需原身份恢复：官方forum进入challenge、API2 notes单次403，raw及murmur-openreview-receipt.json保留。该论文可能有早于arXiv的公开匿名稿，不能将arXiv submitted当首次。只重开此forum的public-date/version字段与必要旧版命题，绝不扫会议全部评审。日期未解决前不进入确定本窗候选或Books；安全笔记保留给非作者核验。

## UI-CUBE：局部负证据已收窄

[exact-v1](https://arxiv.org/html/2511.17131v1) §4/5、Table5～8、§7已读。仅采用五套受测agent中simple/complex完成率差；分辨率表也存在同resolution差，不能把平均表完全归为4K混杂。复杂任务另有JSON格式/流程长度/应用陌生度差异，human61.2%不是普遍能力上限；各agent内部harness不同，原文未固定披露本评估的max-steps/temperature/重复CI，因此不归因架构或某组件。当前官方仓库README有运行器max_steps参数，不证明论文实际使用了该值。

Updated/created均在Nov24 01Z之后，可提供本窗可得上界但不单独证明首次公开的下界。作者仓库原页与release API首10条实际为空（ui-releases.json），不是无代码或无首次公开。停止无依据的commit=public推断；重开需本篇原作者/官方明确公告时刻或完全落窗首公开范围。

## HaNoRec：目标式已确认实际增量

[exact-v1](https://arxiv.org/html/2511.18740v1) §3 Eq4～12已读，并非摘要目标说明即可收。offline item-hardness与online reward-gap responsiveness共同改变β，policy输出/LoRA噪声进入DPO式；确有具体目标改动。Eq12参考分母仍写pi_ref，正文声称两侧扰动的范围与公式不完全一致，不采已解决fixed-reference跨模态偏差保证。item catalog/image anchor限定推荐场景，须必要对照支持收益才采用。日期上界跨截止；不因含DPO名造通用贡献，尚未授确定候选/Books。

## MR-RLVR / MicroMoE：必要机制及反侧读到停止

MR-RLVR [exact-v1](https://arxiv.org/html/2511.17473v1) §4/Eq4～6、§5.1/Table1～3已读：mask-entity/text匹配或step-position匹配是参考轨迹奖励，不是证明数学步骤真值；Stage I只用一种过程任务，Stage II outcome-verification。两个小model、64次解码、temp0.6/top-p0.95/4096、8张A100/A800，teacher清理/标注亦有成本。Table1 Qwen AIME24 P@5/P@8反退，Table2同数据量仍有局部反退；不采所有指标一致提高或等总训练成本。当前v1 HTML含动态排版日期August24,2026，不据此改变v1身份/首次公开，也不将其当历史出版时刻。必要date仍需官方first-public范围。

MicroMoE [exact-v1](https://arxiv.org/html/2511.16947v1) §4～5、§7.1～7.6及必要C.1/C.2已读：每microbatch LP分配expert replica load，再local-first路由；distributed scheduler在同global counts下确定性求解，overlap隐藏开销，expert placement另处理长期偏斜。主实验4节点×8 H100、BF16、EP4/MicroEP8、PP跨node、TP关闭且EP限制node内；网络仅2×400Gbps/node，Smart/Flex为作者移植，不是原库公平认证。极端skew需要placement改变，“零附加开销”不成立（组合优化仍0.4ms dispatch）。不将47.6%最高吞吐外推跨nodeEP或所有MoE。只是可审局部机制，日期上界仍不是first-public下界。

## Rynn / TBIK / political correction：新日期信号

Rynn作者[官方仓库](https://github.com/alibaba-damo-academy/RynnVLA-002) News明确`[2025.11.10] Upgrade WorldVLA to RynnVLA-002. Release models, training code and evaluation code...`。这证明存在官方宣称更早release，不能用Nov24索引为同机制首公开；但尚未证明当时完整论文正文已公开或Nov24论文无新增证据。release API单页为空。下一步仅定点核此早release对应artifact/正文差额，或将事件身份不明精确隔离，不能直接按日期关闭贡献。

TBIK作者[项目页](https://zirui-ray-liu.github.io/projects/)只有November2025，指向Notion Blog和同代码仓库；仓库release API实际为空（tbik-releases.json）。最后可执行恢复是此具名作者Blog元字段，不扩SGLang全部PR。

[political-even-handedness](https://www.anthropic.com/news/political-even-handedness)受影响§Method/Opposing perspectives/配置/caveats/changelog已深入：更正28→35只是counterargument acknowledgement，不是even-handedness94%的改分；只可描述这项比率更正，不能由1pp与Grok差异判排名。Sonnet grader、1350pairs、prompt/thinking跨provider差异及单轮US人口限制保留，未从agreement升级真值。官方published仍Nov13、modified为2026-09-10；Nov24 changelog日精度/时区未定。具名官方检索与关联repo没有精确更正release（political-releases.json为空），不借initial-date归Nov25。若无官方历史时刻/全落窗界限，本窗隔离此纠错日期，原28%不继续作正面证据；重开只核更正记录，不读初公开所有正文。

以上尚不授日级完成。安全与纠错必要正文已处理，未定日期仍不作本窗正面Evidence、Books或零命中；拟贡献池继续有限初筛，不改变此前root准入校准。
