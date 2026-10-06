# 2025-09-25 作者记录（扫描继续）

作者James；窗口2025-09-24T09:00:00+08:00 ～ 2025-09-25T09:00:00+08:00。本日重新完整加载AGENTS/研究与Report合同/来源使用说明Daily及arxiv/Prompt/ROADMAP和月checkpoint路由。只写本日README与_sources；不改Books/共享进度，不自授FIRST/DAY。21已释放。

本日实际32初始请求见[fetch-results.json](fetch-results.json)，本日Qwen核心/Robotics原核心/Seed CN及arxiv日路径/advanced见[narrow-fetch.json](narrow-fetch.json)。均本日独立执行，不拿相邻来源结论当覆盖。来源扫描和arXiv分页/题摘尚在继续，作者普通待办不为0。

## FIRST-GEMINI-25：交root局部准入

[Gemini Robotics 1.5官方事件](https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/)原HTML：[DEEPMIND_ROBOT.raw](DEEPMIND_ROBOT.raw)。本日实际完整主体已读：两模型角色/agentic配合、环境理解/15bench、Thinks before acting、Learns across embodiments、安全/ASIMOV、部署权限。视频未播放，图像未据像素实核，不声称动作实验或生产验证。

日期：原`article:published_time`与JSON-LD`datePublished`均`2025-09-25T00:00:00+00:00`→25日08BJT，落窗。不用修改时间2026-07-06反推首次公开，也不凭无证据CMS猜测取消。

拟准入最小贡献：直接instruction→motor的VLA压力，以及跨平台动作训练不可直接迁移→本文披露VLA动作前可生成任务/子任务/动作多层推理、跨ALOHA2/Apollo/Franka训练任务迁移无需每新embodiment specialize、ASIMOV增加tail/annotations/question/video→重考虑推理与动作策略联合监督及跨embodiment迁移/语义安全评价的条件。Owner候选`MULTIMODAL-EMBODIED-VLA` Ch26（动作策略与闭环），邻接Ch25环境预测与Ch72安全边界；不是把已有高层ER planner+低层VLA组合计作新贡献。

应核反证：可见自然语言过程不证明忠实因果解释/碰撞安全；原Blog声称迁移不等于所有硬件或零数据适配；ASIMOV变化本身需要验证新增blind spot/风险约束而非仅增题。15benchmark aggregate不能无协议采SOTA。厂商选伙伴权限与ER API公开是release事实，不是验证实物执行。安全项应按研究合同§4深入核受影响内容，具体分数待root FIRST，不自授。

官方[Tech Report](https://storage.googleapis.com/deepmind-media/gemini-robotics/Gemini-Robotics-1-5-Tech-Report.pdf)已定点请求保存，见[robot-report-fetch.json](robot-report-fetch.json)；当前尚未读必要方法/对照/限制，未冒充深审。等root FIRST可推进具体命题的精确版本和必要证据。

首批材料补充：已实际读所取62页报告**完整标题/摘要及pp1–2引言**，文本在[robot-report-cover.txt](robot-report-cover.txt)。标题为“Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer”。摘要明确三增量：novel architecture+Motion Transfer、multi-level reasoning/action interleaving、ER embodied reasoning。pp1–2直接写multi-embodiment pretraining后已有ALOHA/Franka/Apollo不需robot-specific post-training，并可zero-shot skill transfer。PDFmetadata Creation/Mod `D:20250924224747Z`仅辨识所取版本，不替代官方原事件公开时间。方法/实验/反证仍待root FIRST后必要深审；没有根据abstract采纳安全/迁移普遍保证。

## 代表性拟关闭：Qwen3-Max

本日实际60对象配置严格落窗一项：[qwen-window-config.json](qwen-window-config.json)，原`2025-09-24T04:00:00.000Z`→24日12BJT在25窗；实际[原核心JSON](qwen3-max.tokens.raw)、[完整顶层文本](qwen3-max.core.md)全部读，包括Introduction/Base/Instruct/Thinking/Develop/References。

原文明确沿Qwen3 MoE/global-batch loss范式，给1T参数/36T tokens、named PAI-FlashMoE multi-level pipeline、旧ICML25 ChunkFlow、SanityCheck/EasyCheckpoint/scheduling；没有解释新pipeline/故障恢复机制或新的可比运行配置。30% MFU、3x throughput、1/5故障时损没有hardware/parallel/workload/基线预算细节，不能据此建立新质量/资源边界。Instruct排行榜及Thinking未发布的tool/test-time100%不补机制。建议关闭本次技术贡献（不是因是产品、大模型或未开源）；若root认为需追named pipeline的新增执行机制，只重开该点。旧机制引用不是本次新论文事件，不扩扫ICML/旧Qwen3全文。

## OpenAI 本日真实RSS与核心

[openai-window-rss.json](openai-window-rss.json)实际三项。Research403原记录保留；必要核心通过web官方页读，不将辅助Research故障等同核心不可得。

- [Pulse](https://openai.com/index/introducing-chatgpt-pulse/)原RSS25日00GMT落窗。实际读官方主体：nightly asynchronous research从memory/history/feedback取context、Gmail/Calendar默认off可撤销、每日短暂结果/可保存、用户curate/反馈、可能建议已完成项目。建议贡献关闭：已有定时研究+持久memory+可选connector+feedback/展示的产品组合，未披露新的执行/恢复/可靠性机制；不把“主动Agent”重命名算delta。默认off和stale feedback局限如实留，不声称安全有效性。
- [OpenAI for Germany](https://openai.com/global-affairs/openai-for-germany/)原RSS24日04GMT落窗。实际读官方主体：SAP/Delos Azure计划2026提供sovereign公共服务及4000GPU扩容。未披露主权控制/密钥/执行隔离/模型训练或风险接受机制，合规/安全承诺不是已验证约束；建议关闭本次技术贡献。
- [ENEOS](https://openai.com/index/eneos-materials)RSS24日17GMT；标题/完整RSS描述明确ChatGPT企业制造/HR应用及工作流提效，没有相关纠错/安全反证信号或foundation机制线索，范围关闭，不虚构读正文。

本日后续继续14源有限目录与arxiv主题分页/完整题摘。FIRST-GEMINI-25只请求上述家族和代表关闭项，不以root11 Next或22 FSF批准代替。
