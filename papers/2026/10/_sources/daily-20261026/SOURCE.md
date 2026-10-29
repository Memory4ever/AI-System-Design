# Daily 2026-10-26：本日来源与证据

本窗为2026-10-25北京时间自然日；检查于2026-10-26。只检查每日14个Source ID及由具体材料触发的原件，不扫描每周来源、不恢复其他日期。root为作者，独立reader为`live1026_review`。没有把上一日完成声明当本日覆盖。

## 来源范围与停止点

| Source ID | 本轮实际入口、停止位置与结果 |
| --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)→[Research News](https://openai.com/news/research/)首批最新10-23，随后10-21/19及更早；越过目标日即停，不点Load more遍历历史。无确定10-25事件。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)最新列表10-23，随后10-20/16；首屏越窗即停，无确定10-25事件。置顶专题不代日期排序。 |
| SRC-GOOGLE-AI | [DeepMind News](https://deepmind.google/blog/)第1页至9月；相关10月模型原文为[Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)10-13、[安全](https://blog.google/innovation-and-ai/technology/safety-security/gemini-4-model-safety-security/)10-13、[Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/)10-13、[EmbeddingGemma2](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)10-06，未当本日候选。[Research Blog](https://research.google/blog/)一次超时后web恢复，第1页最新10-23至9月，停止。AI for Science标题不进入方法队列。[Publications](https://research.google/pubs/)为年份/会议目录，无法据此穷尽10-25首次公开，隔离此日级缺口，不扫全年430篇。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)文本0行；原始[Blog](https://ai.meta.com/blog/)可读但混序，最新可见7月，不能据它宣称10月无发布。已穷尽本轮可用主入口，日级Research目录仍隔离；需官方10-25列表或具名原文重开。 |
| SRC-QWEN | [旧站](https://qwenlm.github.io/)迁移至[Research](https://qwen.ai/research)，文本抽取0行、浏览器超时后，独立reader依实际969.js/framework/research-index公开请求恢复[retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)：success true/40项全身份日期已读，最大09-20；research-list config60项最大2025-12-23、latest-advancements config19项最大2025-09-24，均读完整返回且无分页元数据，不以混序首项截断。精确路径与边界见[REVIEW R3](REVIEW.md)。这是成功恢复而非来源受阻，内容滞后仍不授全站零发布。[qwen-code releases API](https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=8)仅8份身份/日期，本窗desktop与前日stable精确同commit `b475278c4a300acebe6cfc990a9e1b1d18819bfc`，去重不扩全部changelog。 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/)→[研究与动态](https://www.deepseek.com/en/news/)及[更新日志](https://api-docs.deepseek.com/updates/)；研究最新6-24、动态9-10、日志10-17，止于越窗。无具体本窗新研究线索，不扩所有仓库/PR。 |
| SRC-MOONSHOT | [平台Blog](https://platform.kimi.com/blog)25条可见项最新2025-11-07，覆盖滞后限制不抹去；定点[kimi-code release API](https://api.github.com/repos/MoonshotAI/kimi-code/releases?per_page=5)5条，2.3.2为本窗候选，随后10-23、10-21与9月止。不从repo Updated推论文日期。 |
| SRC-TENCENT-HUNYUAN | 首查[Research](https://hunyuan.tencent.com/research)文本0行，依网站实际公开请求使用[publicList](https://api.hunyuan.tencent.com/api/blog/publicList)，POST只读`{pageNum:1,pageSize:1000,renderType:0}`，code0、total11/返回11，全部标题/日期已读。身份100119/100116/100100/100091/100087/100064/100041/100039/100061/100015/100025；最新两个displayPublishTime1790006400为9-22，publishedAt分别1789959110/1789749798更早，均非本窗；不把空UI归零。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)首屏15项至2025-12，最新GLM5.3Flash08-26；时间降序已越窗，不查看更多旧项。无确定本窗候选。 |
| SRC-BYTEDANCE-SEED | [Publications](https://seed.bytedance.com/en/public_papers)Newest→oldest，第1/13页、1–20/247；新首项Recycler10-25，随后09-28及更早即止。[官方原页](https://seed.bytedance.com/zh/public_papers/recycler-cost-free-latent-reasoning-via-hidden-state-recycling)HTML正文日期10-25、完整摘要与官方PDF真实href均读取；候选1。 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)可见8项最新05-09，越窗即停；未把旧模型/普通产品文当本日研究。无确定当窗候选。 |
| SRC-XIAOMI-MIMO | [首页](https://mimo.xiaomi.com/)Paper8项、Blog15项：Paper最新06-29；前6项原文为09-27/09-22/材料暂缓范围/06-10/06-08/05-30。独立reader实际核More是展开`blog-more`内09–15七项的button，不是未取得分页；沿官网manifest→预加载页/iframe核其余日期：ASR/TTS为2026年4月，V2.5Pro04-27、V2.5 04-22、V2Pro/Omni/TTS03-18、Flash2025-12-16、HSS2025-12（正文22/metadata19均远窗外）。全部15项均已判断本窗，未读旧Methods、不遍历其他manifest路由；原“隐藏More缺口”已纠正，详[REVIEW](REVIEW.md)。 |
| SRC-MINIMAX | [Blog](https://www.minimax.io/blog)首批最新10-22，随后10-19与8月；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)最新10-20两项，随后10-08与9月。越窗即停，无本窗具名研究线索。 |
| SRC-ARXIV | 实际核[官方日程](https://info.arxiv.org/help/availability.html)、[状态](https://status.arxiv.org/)与12个recent日期导航：cs.CL/LG/AI/DC/OS/PF/CV/RO/AR/PL/IR/MA。最前批Mon26Oct，较小类下一批Fri23Oct，无Sun25Oct；大类只看日期导航/本批标题，不读26日论文。10月夏令时，Sun20EDT公告落BJT周一26，不是本窗25。状态页只见28日计划维护，不当历史全正常证明。DataCite精确`client.client-id:arxiv.content AND registered:[2026-10-24T16:00:00Z TO 2026-10-25T15:59:59Z]`，page1/size100返回total0/totalPages0/items0；仅辅助交叉检查，不把registered单独等同公开日或证明全网无稿。本轮确认本窗常规arXiv批次0。 |

有界搜索只作补线索：Recycler精确全题名、`site:seed.bytedance.com Recycler`、`site:qwen.ai/research 2026 10-25`、`site:ai.meta.com "October 25, 2026" research`、`site:deepseek.com 2026 10 25`、Moonshot官方域与October2026。返回首批实际已读，未采用第三方/无关命中，搜索空不证明零发布。没有catchup90天，也没有把26日列表反填25日。

## 两个拟入选家族与代表排除

1. Recycler：普通生成已有KV跨步上下文，不可概括成“只剩离散token、全部连续信息丢失”。具体新增为上一token顶层hidden经RMSNorm+linear后与下一token embedding相加的额外通路；训练/Prefill并行近似与生成递归有不同支持和费用。拟`2+2+3=7`，等待独立准入校准与Books实际比较。论文称cost-free不是本轮结论。
2. Kimi Code2.3.2：默认委派与swarm可用性的真实兼容/权限变化，拟`1+2+1=4`；因具体行为/权限影响，深入相关域，不为新通用原则加分。预期仅报告，尚未凭主题相似签已有覆盖。
3. Qwen desktop-v0.26.1：API发布`2026-10-24T17:06:46Z`，落本窗；与v0.26.1精确同commit，后者已在[前日报](../../25/README.md)处理。只去重该代码事件，不冒称桌面端所有打包/安全均已测试，不新列候选或重审整个changelog。
4. Google/DeepSeek/MiMo具名旧文、暂缓材料研发和学术搜索回传TMLR全年目录不入本窗队列；不把无关搜索命中写成完成初筛几百篇。

## Recycler 必要证据已读范围（待独立复核/Books）

官方[PDF](https://lf3-static.bytednsdoc.com/obj/eden-cn/hyvsmeh7uhobf/recycler_arxiv%20(2).pdf)18页，首页Date October25,2026；实际读取§2、§3各对应评价与直接反侧、§4/5相关分责。网页PDF抽取失败后以原官方URL成功取原bytes，通过pypdf内存解析；未核图像素/代码/复现实验，不保存截断全文为原件。原文没有精确arXiv ID可确认，不补造编号或submitted公开日。

`A(h)=Linear(RMSNorm(h))`，token路径仍在；训练以浅层多pass重用前pass的前一位置hidden，非精确完整序列递归，所有pass各有NTP loss。零初始化linear、tied embedding为作者配方，不证明所有backbone自动兼容。自回归decode递归深度随输出增长；Prefill一pass与两pass是不同工作点，后者额外完整prompt计算。更大模型/更多数据出现深度外推loss回退，作者补部分三pass训练；不采用无界深度稳定保证。

Token效率不等总训练效率：预训练两pass增加计算，Fig8是估算累计FLOPs且各stage只在同suite内比，不能跨suite平均；模型β同大小baseline训练轨迹更短，原文明确非三终点equalbudget。SFT Table1存在IFEval/ArenaHard等局部退步，不能写全部任务改善；prefill配置与训练匹配很重要。RL以不同SFT起点、代码revision/rollout schedule的完整路线比较，原文承认不能当RL单阶段严格equalcompute因果；中途人工停止，非收敛天花板。未披露具体模型α/β规模、硬件、precision、完整输入输出长度、batch/concurrency/SLO与端到端计时，均Not Disclosed，不照录倍率为服务收益。论文Intro称解决MTP验证，但采用范围未提供该算法原件，不能自补speculative正确性/commit规则。

拟长期命题只为：跨token continuous feedback与同tokenloop、额外latent token不同；它改变训练/Prefill支持、可恢复状态与消费者接口，需要质量/完整费用配对。额外session/版本/前缀一致性属于本项目系统推断，不冒称本文测过迁移/故障安全。当前KV仍在，不能把旁路称替代KV。无公共实现/复现被验收。

## Kimi2.3.2 实际受影响证据

实际读[4386](https://github.com/MoonshotAI/kimi-code/pull/4386)、[4384](https://github.com/MoonshotAI/kimi-code/pull/4384)核心Why/changes/兼容边界，以及各files API（9/16文件身份）。4386只核`agent.md`相关diff：改变prompt而非执行层强校验。4384实际读`agentSwarmTool.ts`在resolveExecution与execution双处检查、`swarmService.ts`拒绝tool-trigger enter、`swarmOps.ts`忽略旧tool enter、`foldFacts.ts`不由旧tool记录重启mode。当前工具仍在列表中；运行资格不由工具可见性授予。历史marker仍保留，不是删除历史；print/ACP没有用户开关入口，官方说明因此不能启动swarm，不外推普通Agent工具全部不可用或所有API安全。

实际核的是公开diff与作者描述，未运行测试/终端/SDK，不把测试文件出现当本轮验证。没有性能命题，hardware/workload/concurrency/SLO不适用。两PR属于同一release家族，分别说明prompt偏好与execution资格，不重复计分。仅报告此版本事实，不据常见授权分责强行新增Books，也不声明已扫描其他所有风险。

## Recycler 当前owner与最小稿（待独立PRE）

实际读取ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE，比较Ch17跨位置回馈与Ch18 latent接口及Ch16/18交接。唯一拟owner为`MODEL-TRANSFORMER-LAYER` Ch17，不在Ch18/训练/推理多头重复写。Ch17现有17993高低层旁路、25076单core state/Jacobi、25086双slot均有有效机制；缺少的是“保留每个可见token并让完整顶层hidden与下一embedding同走、浅pass逐层NTP监督/训练深度外推与Prefill分账”的具体配对，不是重新发明recurrent。Ch18只保本来latent/可见轨迹接口，不据本文改架构结论。

拟在Ch17 `2610-25076`完整单state段之后、ACT停止器起段之前接以下两段，旧两肩不动：

> 这种跨位置旁路还可以保留每一步可见 token：将上一位置的顶层状态 `h_t` 经 RMSNorm 与学习投影 `A`，和下一 token 的 embedding 相加，再运行原 Transformer：`h_(t+1)=T(Emb(x_(t+1))+A(h_t))`。这里增加的是顶层到输入的直接通路，普通 causal Attention 的 KV 历史仍在，不能说原模型只保留了离散 token 或新状态替代了 KV。与只循环同一 token、只回馈 middle core 或新增不可见位置相比，这一选择保持原可见生成接口，却给训练与 Prefill 新增了跨位置依赖。
>
> 为保留序列并行，可用前一 pass 的 shifted hidden 近似当前 pass，并在各 pass 都施加 next-token loss；[受限 Recycler 对照](https://lf3-static.bytednsdoc.com/obj/eden-cn/hyvsmeh7uhobf/recycler_arxiv%20(2).pdf)采用零初始化适配器及 tied embedding，但浅训练深度不保证长生成稳定，较大配置已出现外推回退，需要额外训练。单 pass 与双 pass Prefill 是不同质量/准备成本工作点，少量 adapter 也不免除多 pass 训练和状态驻留。部分任务退步、较短 baseline 训练轨迹及不同 RL 路线配置，均不支持“免费能力”或严格同总计算优势；未披露完整硬件、精度和服务负载时，更不能由相近逐 token 算子数批准端到端 SLO。训练支持、深度外推或总预算失配时，保留原固定栈、已验 core 反馈与显式 token 路径，分别验质量、准备和 Decode 费用。

独立marker：`<!-- source-family:SF-2026-SEED-RECYCLER-20261025 -->`。

本人true H2 Review notes新注拟：`SF-2026-SEED-RECYCLER-20261025`，官方10-25日期稿§2–3/直接反侧；2+2+3=7，仅顶层→embedding反馈及浅pass监督/Prefill/深度外推分账；KV不被替代，保局部质量回退、非等预算路线与未披露服务条件。未核实现/图像素或复现。独立PRE与实际POST以本日REVIEW为准，未授DAY。
