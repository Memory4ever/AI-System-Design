# 2025-09-30 作者证据与Books差额交接

作者 Archimedes，仅建议；root FIRST尚待，作者不授采用/POST/DAY、不改Books。当前合同§3–6，owner以ROADMAP为准。未复现、未核候选代码。以下全部6家族拟2+2+2=6，评分只取具体命题，不借成熟原则/硬件倍率/排名。

## Sora 2：拟差额，PLATFORM-SECURITY

原公开RSS三条`Tue, 30 Sep 2025 00:00:00 GMT`即30日08BJT，见`openai-rss.xml`。原Sept30[七页system card](https://cdn.openai.com/pdf/50d5973c-c4ff-4c2d-986f-c72b5d0ff069/sora_2_system_card.pdf)，本地`sora-systemcard.pdf`，`recovery-fetch.json`，实际§1–6与Table1视觉读。发布Blog当前停服/character用语不回填Sept。

具体链：photorealistic generation可描绘真实身份 → 初始只允许验证consent的cameo、owner限定谁可用及撤销；初始无video-to-video/无public-figure text-to-video → 人物相似性许可与generated-content provenance必须分账。撤销只约束产品内许可/草稿，不授外部拷贝可撤回。frames/audio transcripts/scene captions与人工/举报是分层sensor；C2PA、水印、内部detector不证明所有内容可验来源。Table1 not_unsafe/not_overrefuse各一分母概念，selected adversarial prompts/autojudge，N/CI Not Disclosed，不授生产recall。

实际owner[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 602–628、1080–1116、1495–1535、1884–1972：模型verdict非authority、目的/同意/删除链、provenance互补；当前检索及实际段落未见人物likeness的验证授权、创作者scope与未来使用撤销的对象分账。建议在现provenance段1088–1102后自然接一段：可验证生成来源不表示有权使用被描绘者身份；分别绑定consent主体、许可用途/creator、撤销未来使用、产品内存量处置，不能由detector代签同意或承诺互联网删除。成本是身份验证、范围与撤销状态/误拒，未验证则限制真实人物路径/人工确认；保留原provenance路径。邻接[Ch71](../../../../../books/part-06-ai-infrastructure/71-multi-tenant.md)隔离与[Ch73](../../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)发布验收不接管该权限语义。建议定位，非已写。

## DeepSeek-V3.2-Exp：拟差额，MODEL-SELF-ATTENTION

官方原贴[1972604768309871061](https://x.com/deepseek_ai/status/1972604768309871061)的官方嵌入接口实际200：`deepseek-tweet.json` created_at=`2025-09-29T10:10:00.000Z`、@deepseek_ai、未编辑，即29日18:10BJT，`glm-tweet-fetch.json`保留请求。Git commit不承担first-public。

精确[Sept29固定报告](https://raw.githubusercontent.com/deepseek-ai/DeepSeek-V3.2-Exp/840f3c924a6b1604b1998baebf0c5f167e10375a/DeepSeek_V3_2.pdf)，`deepseek-report-sept.pdf` / `deepseek-version-pdf-fetch.json`，526189B、SHA256 f8ef04ddf50f924a7d251861d4453d7605ff5711f3941ae8320e1ea780dc3041，与此前实际读过main PDF逐字节相同。有限path commits两条见`deepseek-report-commits.json`，固定版本是正文身份，不是公开时间。实际6页§1–3、Eq1–4、Fig1–3、Appendix A。

具体链：先完整dense attention再TopK不减少选择开销 → 低维FP8/ReLU multihead lightning indexer计算评分并训练TopK支集，主要attention只读k位置 → selector训练、保留质量与实际attention计算应单列。Indexer仍O(L²)，core O(Lk)，不称全算法线性。MQA共享latent为kernel效率约束。冻结主模型dense indexer warmup1000步/2.1B后sparse continued943.7B/15000步、k2048，KL的selected-set target/独立gradient不能省略；相同postpipeline并非单因子同预算实验。GPQA/HLE/HMMT退步、reasoning length不同，不写无损；H800/$2GPU-hour估计/短序列masked-MHA分支不授生产SLO/QPS。

实际owner[Ch14](../../../../../books/part-02-model/14-self-attention.md)110–140：路由mass不等知识贡献，2609.37879先算dense再删，不是加速；随后SLA2分支。建议在该dense再选择反侧之后/SLA2之前自然一段：cheap learned selector改变稀疏训练与读取接口，需teacher/indexer warmup、稀疏继续训练、质量条件；支集省核心计算但选择仍二次且有TopK/gather成本，短序列/选择不准保留dense fallback。当前正文尚未实际承载这一训练合同。实际[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)2118–2140已讲indexer/TopK/gather融合与reference/阈值回退；因此不重复kernel段。相邻[Ch13](../../../../../books/part-02-model/13-position-encoding.md)1–32拥有位置、[Ch15](../../../../../books/part-02-model/15-multi-head-attention.md)1–32拥有head子空间；不要将DSA选择训练另设owner。

## Sonnet4.5：已有覆盖建议，PLATFORM-EVALUATION-SYSTEM

[官方发布](https://www.anthropic.com/news/claude-sonnet-4-5) schema2025-09-29T17:00:00.000Z即30日01BJT；当前page modified2026不作Sep修订。当前官方149页card原件`sonnet-systemcard`及`card-fetch.json`。实际cover/changelog，§7.2 PDF59–63，§7.6.1–3 PDF88–92，§7.6.4 PDF99–103，PDF104–111 multi-turn，PDF112–115限制。Oct10 footnote24作者与Dec3§9.3.5 parenthetical保留身份，不称冻结Sept整份。

具体命题：verbalized-awareness过滤不覆盖潜在识别；SAE/model-diff与干预提供局部条件证据，不能由低行为率外推部署。100synthetic/temperature0、未steer0/100与部分方向8–9%、十个同norm random directions为局部对照；strength ad hoc、feature混合伦理/awareness、排除degenerate限制因果。multi-turn50prompt/较早auditor/无realism-filter，financial crime awareness10%但misalignment0；research sabotage少数/50，非战略欺骗。1000probe是较早snapshot且包含response，post-hoc不作cause；弱预测、非英语/image未覆盖。SWE500题10runs/200K与1M78.2 inference issue、82parallel patch预算不能合并。

实际[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)194–270、4018–4055，尤其4038–4042明确representation/verbalization/control、decode/verbal/steering/部署分账与probe可能读template/data/posttraining。拟采用最低命题已有具体承载，不为加入厂商名改书；版本与局部证据只报告。相邻[Ch65](../../../../../books/part-06-ai-infrastructure/65-kai-scheduler.md)/[Ch67](../../../../../books/part-06-ai-infrastructure/67-monitoring.md)开篇已读，monitor不接管verdict。

## Claude Code checkpoints：已有覆盖建议，AGENT-WORKFLOW

[官方原发布](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously)同17Z，本地`claude-autonomy.html/.text.json` core Checkpoints12–58。恢复code/conversation可分别或共同，**仅Claude edits，不覆盖user edits/bash commands**，仍需VCS；不是全environment rollback。具体发布恢复约束，非界面/SDK改名贡献。

实际[Ch81](../../../../../books/part-07-agent/81-workflow.md)580–624已将context与environment joint state、snapshot受控scope、replay memory不replaytool、外部network/process/payment compensation与Git非transaction rollback说清。最低长期命题已有覆盖，厂商范围仅报告，不制造diff。相邻[Ch80](../../../../../books/part-07-agent/80-reflection.md)/[Ch82](../../../../../books/part-07-agent/82-multi-agent.md)开篇已读，reflection无权回退外部effect、分工不自带恢复。

## Parental controls / Combating CSEA：请求root独立准入及最小差额判断

两独立家族原RSS均Mon29Sep03GMT即29日11BJT，原core在`30ordinaryweb1.json`，不是沿用RSS标题作证。

[Parental](https://openai.com/index/introducing-parental-controls/) Getting started/Stronger safeguards/Notifications/Looking ahead：模型flag→小组trained human审急性风险→有限通知，而非向父母开放全聊天；teen可unlink并通知、guardrails可能bypass/false alarms、age prediction当时未来计划。页面明示2026-07-13 violent alerts/Study Mode不回填。拟贡献是发布时安全告警与披露权限跨角色分账，不授安全有效率。

[CSEA](https://openai.com/index/combating-online-child-sexual-exploitation-abuse/) Train/Detect/Patterns：known-CSAM hash与novel classifier分责、flag后expert review；上传被要求描述/roleplay显示只拦生成请求不足，不载入有害材料/不提供规避细节。没有P/R或全bypass保证；厂商政策/法律叙述不作法律事实或合规保证。

实际Ch72上述sensor/purpose/authority及602–628、1884–1972能承载一般分责。拟优先**已有覆盖/仅报告**，但不能仅“成熟原则”否定其具体发布条件：请root核原core是否还需最小自然句说明家长通知不等全chat grant，或跨模态输入分析也进入content审查对象。若需要，放在现policy gate/sensor附近，明确输入/输出/收件人三对象、误报/可绕过、人工与最小披露成本；不追加两篇发布摘要。作者未写，root裁决后同步正式Books字段。
