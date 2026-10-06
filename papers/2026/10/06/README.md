# Daily Research — 2026-10-06

**规范：** V3
**窗口：** 2026-10-05T09:00:00+08:00 ～ 2026-10-06T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T09:32:51+08:00

## 1. 结论

本窗值得保留的是两项可观测判断的边界：RL ratio接近一不证明rollout/replay条件相同；sleep成功不证明物理HBM已交还。UniRL三项main合入纠错给出具体反侧，已在Ch33和Ch36各融入一段。Qwen Code0.25则交付带Linux身份与目录前提的默认恢复配置，并修正Host native拒绝与permission/upstream判定顺序；默认启用不等于重启恢复保证。

正式候选2个唯一家族，均6分、因具体正确性/发布约束深入受影响部分完成；1家族整合至2个既有owner，1家族仅报告。不是两篇新论文，也不把同release的SDK/desktop或多个PR重复计数。14每日入口均按主题有限处理，Google CAPS研究议程排除、D2K同家族artifact去重；arXiv只恢复两个完整题摘身份，不将230个提交查询线索变成队列。

arXiv目标Tue6公告仍不可恢复，Qwen Research与MiniMax中文动态目录，以及MiMo UltraSpeed日期范围保留；这些不授正面Coverage/Evidence、Books或“零新论文/无遗漏”。正式报告最终非作者复核通过，普通待办0；未运行代码或复现实验。周二不创建当前Weekly，不扩其他日期，不stage、commit或push。

## 2. 来源覆盖

主题范围：foundation/language model、训练/后训练与推理运行时、多模态/World Model/VLA、kernel/compiler、RAG/memory和Agent工具/协作；AI for Science暂缓。完整有限停点与实际阅读角色见[本日来源记录](../_sources/daily-20261006/V3_SOURCE_STOPPOINTS.md)。这里的“已检查”仅指下列切片，不声称全机构/全年覆盖。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research Index](https://openai.com/research/)前8新→旧，最新Sep29→Sep3；root本日实际读取，有限目录无窗内条目，作者不回填为自身阅读 | 已检查 | 无；未扫旧全文 |
| SRC-ANTHROPIC | [Publications](https://www.anthropic.com/research)前10，最新Oct1→Sep4；root实际读取，有限目录无窗内条目，science不扩 | 已检查 | 无；未扫旧全文 |
| SRC-GOOGLE-AI | DeepMind publications第1页/265总项，Sep16→Nov2025；Google pubs15项按年份且含2027不能授本窗；另[Blog](https://research.google/blog/)第1/135页12条Oct5→Aug31，CAPS完整core排除，有限信号已处理 | 已检查 | Google年份目录不支持事件完备覆盖，不据此称全站零 |
| SRC-META-AI | Research空正文后原[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication&q=)第1页首12 Oct2→Jul17，随后混旧；有限目录无窗内条目，停止Next，不追旧科学全文 | 已检查 | 后部非严格时间排序，未授全站覆盖 |
| SRC-QWEN | 旧站跳[Research](https://qwen.ai/research)空CSR；org首10/59更新切片恢复qwen-code0.25与D2K init；release API前5、两core精确tag核验，确定1家族 | 受阻 | Research动态目录不能恢复；不由repo更新证明完整研究覆盖 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/)最新V4.1Flash→原[事件](https://www.deepseek.com/news/deepseek-v4-1-flash/)Sep10，展示不是本窗发布 | 已检查 | 无；停止该原事件 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)26条最新Nov2025；org首10/42 Oct2→Aug3，有限切片无本窗信号 | 已检查 | 无；未扫所有repo |
| SRC-TENCENT-HUNYUAN | Research skeleton/IAB超时后原JS公开API publicList，page1/size10/renderType0，total9/list9，最新publicAt Sep23→Feb3；org首10/83→UniRL窗内8 main合入，确定1家族 | 已检查 | 浏览器失败已由原public API恢复，不保留过期受阻 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)首15 Aug26→Dec2025；org10/53 Oct2→Aug5；release-notes18项最新Aug26，有限切片无窗内信号 | 已检查 | 无；不扫旧全文 |
| SRC-BYTEDANCE-SEED | Research首页Blog5/Paper10，置顶SeedRealtime原Aug5；publicpapers newest第一页1–20/242、1/13页Aug18→May14，有限切片无窗内信号 | 已检查 | 无；不扩暂缓science |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)第1/2页10项May9→Nov2025，有限目录无窗内信号 | 已检查 | 无；停止旧边界 |
| SRC-XIAOMI-MIMO | Homepage Paper8 Jun29→May2025、Blog15标题；前6主题信号定点原页tool repetition Sep27、V2.6 Sep22、Code Jun10、Inference May30均窗外，science#3排除；org10/18最新Oct3 | 受阻 | UltraSpeed原公开时间及未授日期目录范围保留；不把其余标题升级必审队列 |
| SRC-MINIMAX | EN Blog12 Aug13→Oct2025；中文动态壳；Agent docs llms明确入口恢复techblog.md唯一May13 AgentTeam；Code releases首5最新Oct2→Sep29，英文/Agent有限切片无窗内信号 | 受阻 | 中文目录不能恢复，不称中英完全等价 |
| SRC-ARXIV | 12分类/new原heading均Monday5；CL RSS/recent同旧批；有限主题提交query start0/max100/total230只读首两完整entry，未扩其余；[两题摘](../_sources/daily-20261006/V3_ARXIV_TWO_ABSTRACTS.md) | 受阻 | 目标Tue6公告未恢复；Submitted≠公开，首次观察01:06:55Z晚于01:00Z，不授本窗论文覆盖或零命中 |

没有每周源扫描，也没有另触发按需固定来源组。候选所需官方PR/精确artifact是Qwen/Hunyuan入口的定点证据，不把整GitHub变为表外日级全扫。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [UniRL main纠错家族](https://github.com/Tencent-Hunyuan/UniRL/pull/547) | 2026-10-05T03:05:03Z | #547/#528/#403合入事件，训练诊断/API成功可能掩盖错conditioning与wake峰→具体实现反侧/recipe归因纠正→独立验证布局与相位资源；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md#版本窗口与-draft-复用仍须保护-trajectory-identity)，`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md#training-memory-contract-必须覆盖组合峰值)；其余版本事实仅报告 |
| [Qwen Code v0.25.0](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.0) | 2026-10-05T09:44:40Z | 正式交付Linux受限默认恢复与native-only早拒/最终参数upstream检查→默认/平台适用与授权次序不能由UI成功推定；2+2+2=6 | 深入完成 | 仅报告：具体发布配置、局部实现回归，不改变既有长期职责，不授Linux物理重启保证 |

## 4. 证据与知识整合

原始时间均UTC且完全落窗：UniRL #547 merged_at=2026-10-05T03:05:03Z、#528=2026-10-05T03:34:23Z、#403=2026-10-05T09:09:20Z；表内以该家族首个采用事件代表，不称首次bug发现。Qwen release published_at=2026-10-05T09:44:40Z、#13406 merged_at=2026-10-05T07:26:00Z；#13211Oct3仅窗外背景。必要三core/辅助与两exacttag core完成，未审整库或所有release条目。

### [UniRL main纠错家族](https://github.com/Tencent-Hunyuan/UniRL/pull/547)

实际版本与必要位置见[候选证据](../_sources/daily-20261006/V3_CANDIDATE_EVIDENCE.md#c01--sf-2026-unirl-20261005)。#547 exact0a82feb只改BAGEL pipeline三个取prompt helper；先前unwrap后仍查batch字段，导致source_image=None、rollout走另一套图像prefill，trainer replay不同。作者BAGEL7BMoT/LoRA/16×8/512×512、rollout/trainer8×H20、reward另一节点受限对照中，KV长度5938/2263不等但ratio仍≈1；replay old logprob还只是trainer自比。因此采用的是诊断不充分反侧，不把conditioning同时改变后的时延/reward差写成可比净收益。

#528 exact54cc7b6的config validation与engine/trainer证明：Noop saver可以成功返回却不释放HBM；启用saver/CPU backup仍要核wake-before-training-offload组合峰，并支付host副本与搬运成本。Qwen3-4B fp32/2H20有限运行只支持该phase边界，不能得到通用memory fraction。Overflow在组advantage计算后可选删除梯度、保留baseline，改变estimator而非无偏等价；字符clip也不代token预算，均仅报告。

#403最终94e8f26 recipe实际master_dtype fp32、cast_forward_inputs false、ImageBind mode all。旧两seed45rollout的+0.00234/step来自未设master/cast且modeaudio_video的旧配置；最终header明确不是当前配置。Canvas、group、SDE、lr、更新数同时变化及objective/eta共线，使旧斜率、plateau与quality归因不成立；embedding alignment上涨不认证视频artifact质量。这里只纠正公开recipe事实，不授新配置效果。#542 GenEval显式detector路径/GenEval2 fallback与local缺list得0是部署辅助边界，不重复计家族或扩长期owner。

现有Ch33已有policy/group/view身份与概率proxy边界，新增的具体反侧是“同版本/mean ratio≈1仍可错多模态conditioning/KV”；实际写入正文L1382及末注。Ch36已有overlap residency/组合峰和backend状态，新增“sleep API≠物理释放与wake-before-offload”正文L1779及末注。root写前实际对读原源、owner与邻章，授权这两窄处；写后实际正文/完整邻接/末注POST通过，不归因其他既有Books修改。

### [Qwen Code v0.25.0](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.0)

精确tag指向6788c035；[application.yml](https://github.com/QwenLM/qwen-code/blob/6788c035698a0ada471c958d1e789e96c6cddd9b/packages/sdk-java/managed-agent-server/src/main/resources/application.yml)79–115中broker enabled=false，durable local-process与trusted local-reboot recovery=true，operator/verified-workspace=false。这是启用broker后的默认，且原#13211要求Linux machine-id/boot-id与owner UID/0700/非symlink、非workspace内state目录；不满足则startup fail，static provisioner需关闭trusted recovery。LOST-on-reboot问题和精确head物理重启欠验仍是反侧，portable合成身份/Mac测试不代物理reboot；release“No known breaking changes”不能抹除这些启动/迁移条件。

#13406原before/after与[stable Session.ts](https://github.com/QwenLM/qwen-code/blob/6788c035698a0ada471c958d1e789e96c6cddd9b/packages/cli/src/acp-integration/session/Session.ts)14045/15167附近实际实现：native-only confinement早拒在permission前、不调用upstream；允许路径经hooks后，upstream只对最终invocation.params检查一次。原baseline并未泄漏outside文件，修正的是无意义permission RPC先发生的顺序；controlled-provider macOS tests不证明Linux/Windows/真实模型或完整生产安全。仅采用此实现边界，不审整release的普通fix。

Ch84 Primitive Effect/Resume/current-head与Ch72实际effect独立授权仍承担一般责任；本次不把它们改写为Qwen专属框架列表或Linux恢复保证，Books仅报告。昨日13064/13069的旧公开事件只定点复用去重；D2K init同家族artifact不制造新候选。完整细节与精确停止位置见[证据记录](../_sources/daily-20261006/V3_CANDIDATE_EVIDENCE.md#c02--sf-2026-qwen-code-025)。

## 5. 缺口与下一步

普通研究、Books及最终复核待办0。下列为本窗终态保留项，不用于正面证据、Books或无遗漏断言，也不授候选、正面Coverage/Evidence或零命中；定点重开条件分别如下：

- arXiv 12目标分类的Tue6原公告/公开上界：web/native/new、CL recent/RSS仍Monday5，有限提交API首次观察晚于截点。需原Tue6公告或截止01:00Z前已公开的可核登记上界；只重开目标批/身份，不处理230宽线索。04721v1有matched-supervision结构增量潜力，但Submitted3Oct不能确定本窗，未评分/正式准入。04740药物工作流已范围排除，不为不影响处置的日期另追。
- [Qwen Research](https://qwen.ai/research)与[MiniMax中文Blog](https://www.minimaxi.com/blog)动态目录：当前原始正文只是shell，官方repo/release替代仅覆盖实际事件，不证明目录完整。恢复需可读原目录/公开事件feed带日期，定点补本窗，不泛扫历史。
- [MiMo](https://mimo.xiaomi.com/)Blog #5 UltraSpeed原公开时间与未授日期目录范围：前6主题信号已按实际原页处理四项窗外/一项science排除，#5缺公开日期；接受原事件页或官方日期登记，只恢复该信号与受影响切片，后9标题不是已审队列。

Hunyuan公开API已恢复9项，MiniMax Agent techblog.md已恢复May13，MiMo Code/Inference/V2.6已恢复原日期，不保留这些已消除的普通/外部请求。没有窗外新候选的扩大审阅或其他日期任务。

## 6. 复核

复核者：root（报告非作者、Books非写入者）
结论：通过

已完成的实际复核：首批两家族2+2+2=6准入；Google CAPS完整Blog/publication摘要的agenda排除；arXiv04740完整题摘科学排除与04721贡献潜力/日期隔离；C01 #547/#528/#403必要core与immutable代码、#542维护者纠偏；C02 exact stable config/Session以及#13406 before/after，平台/物理重启与旧baseline未泄漏边界；Ch33/36 actual owner与邻章PRE和两段/完整邻接/末注POST。来源分层抽检为OpenAI8、Anthropic10、DeepMind第一页、Moonshot26、Seed第一页20、ZAI15、MiniMaxEN12、ERNIE10、MiMo15标题与具体原事件；不等于无差别读完所有来源正文。

root已实际通读最终六部分、完整候选证据与更新来源停点，独核Hunyuan全部9条元数据、2家族计数/采用与隔离重开条件；Ch33 canvas/reward节点呈现微调POST通过，最终DAY通过。完成态V3机器校验与限定diff/行末空白检查通过，不能替代以上实际语义复核。无实验复现或生产验收。
