# Jan14 独立必要复核 delta12：07041 CLEAR /06521 BabyVision

复核者：review_jan15_delta（非报告作者）。仅 root 本轮具名两项，未接 owner-proposals 中后续组，不扩附件、旧候选或版本对比。换日恢复完整重读 AGENTS、Research/Report 合同、Daily 来源使用说明与分组、Prompt、ROADMAP；只恢复 Jan14 supplement 与相关 checkpoint。Books 边界判断前读 PROJECT_CONTEXT、学习方法、写作指南和目标实际邻接。补窗仍 BJT 2026-01-13 完整自然日，原17、原窗口/日期/评分不动。本文件仅独立审计，不修改 Report/Books/LS/索引，不 stage/commit/push，不授 DAY。

## 实际采用与身份边界

两项完整题摘实际读本日 increment-abstracts-5-20261007.json 对应完整行；准入不依靠论文名称、主题映射或先评分倒推。作者 prepared 原件实际完整读：

- [07041 exact-v1](https://arxiv.org/html/2601.07041v1)：increment-necessary-core-2601.07041v1-20261008.json 的 §3、§4、Limitations，分别 8025、14482、1240 字符；§4 分段接续读完，未以摘要或作者结论替代方法与直接反侧。
- [06521 exact-v1](https://arxiv.org/html/2601.06521v1)：increment-necessary-core-2601.06521v1-20261008.json 的 §3–6，分别 4745、3175、19430、12330 字符；§5 接续读完。未读取无关附录、执行代码或声称复现。

日期复用本日已核正常公告/ID 界限，结合 increment-date-bounds-rest-20261007.json：07041 Updated-v1 Jan13 01:54:26Z→registered03:53:31Z；06521 Updated-v1 Jan13 01:24:09Z→registered03:41:26Z。只记 BJT Jan13，不拿 Submitted 或 registered 单证、不追秒；必要正文未出现改变归属的更早发布线索。读取 increment-current-identity-next10pair1-20261008.json 两项原观察后，本轮再次独立轻读两官方 abs：CLEAR 当前 v1，BabyVision 当前 v2/Jul07；未见具体撤回/纠错公告。不把 v2 默认当重要修订，也不将当前摘要的说法冒充 exact-v1 新增机制。

## 07041 CLEAR — 2+1+2=5 / 标准 OnlyReport PASS

准入链：语言资源或相近文字可作为便宜的语言选择启发，但不能直接决定外部证据权重。新增的是十语言、两种不同 QA 任务、四递进冲突场景中的任务依赖反转及 query-language 条件差异；它提示事实检索与 reasoning conflict 不能合成一张无条件语言信任序。这是有具体切片的负侧验证，不因局部实验或未形成生产 selector 在贡献前关闭。

必要机制与人口：PopQA 898 entity queries、StrategyQA 1000 reasoning queries；Gemini2.5Pro 翻译后有人审与 entity presence 检查。closed-book 回答正确/错误只定义操作人口，不认证内部 belief，也不证明翻译与 native-language 知识难度相同。SR 在初答正确者上给 contradiction，PR 在初答错误者上给 support，分母随语言、模型与任务改变；不能将这两个不同条件率当全人口互补或机制归因。四设置区分闭卷、单语言、跨语言与竞争双来源，并绑定 query/output language 和 evidence order。

六个实际模型为 GPT4o-mini、Gemini2.5Flash、Qwen3-8B/80B、Llama3.1-8B、AyaExpanse8B，thinking 在可控时关闭；Gemini2.5Flash 语义 judge 没有独立跨语言可信度认证。Table1 caption 的“eight”与正文/名单的六不一致，不借此扩实验范围。Table3 caption 的 TT/TF/FT/FF 是两份 evidence truthfulness，§4.7 却按 parametric-memory quadrant 解释，不能把两份身份拼接后证明 latent memory 因果。这一解释隔离不抹去已明确设置下的局部输出行为。

关键反侧：任务与语言组合不支持统一资源/affinity 优势，Aya 在 StrategyQA 的 query-negative 差值为 +3.5，而其他多为负；不同小节对 bn 的 resource 标签也不统一。query priming、知识暴露、script 和资源未由匹配控制独立识别，不能授资源或文字相近的唯一因果、跨任务稳定 selector 或所有低资源语言更强。十种译制语言/两个 English-origin QA 不外推 native culture、长对话与端到端检索。翻译、人审、双场景和 judge 调用均是成本；单 A10080GB 与 80B 运行叙述未闭合精度/执行配置，完整重复、置信区间与全流程成本 Not Disclosed，不授性能复现。

Books 实际顺读 Ch66:1490–1508：翻译派生任务须保 invariant/lineage、语言不等于 locale；3060–3090：causal estimand/assumptions/失败降级及 diagnostic authority。它们承载本次采用边界，但不假称精确 CLEAR 四场景已经覆盖。当前贡献是有限语言/任务行为校准，不另推出新可运行协议、机制或长期 selector；故标准仅报告，不因为“能映射 Ch66”升为整合，也不假称具体 Existing。可以正式同步5分 Only，不写 Books、无需锁。

## 06521 BabyVision — 2+1+2=5 / 标准 OnlyReport PASS

准入链：知识丰富或文字 reasoning 分数高，不保证细粒度视觉几何任务可靠。新增不止排行榜：388题/22 subtype 的视觉原语切片，与独立 280题/21 subtype 的 image-overlay 输出任务及 evaluator 校验，使文字答案与视觉外部化的失败可以各自定位。这一任务/output/evaluator 人口分离具有具体选择价值；不要求先证明“语言导致视觉失败”才准入。

§3 的四族为细粒度区分、视觉追踪、空间感知、视觉模式，135 MCQ+253填空；平均25.9词且包含 OCR/数字，不授完全无语言。约100人工 seed→reverse image search 候选→标注/双专家核验，筛选质量不等无污染或通用视觉真值。§4 Gen 用最小 circle/line/arrow/text overlay，平均22.9词，三人 reference consensus；280不是388的同一全人口，也无 human Gen baseline。Gemini3Flash 的 NanoBananaPro 输出人审一致269/280（96.1%、F1 .924）只支持该 generator/条件，不自动认证其他 generator 或未来 judge。

§5 保留最高 reasoning、不同 API/模型温度与三次平均 pass@1（不是 pass@3）。儿童各年龄20人、同校、Mini20题/45min；16成人评 full388，不能把 full-model 分数与儿童年龄合成同人口梯度。4B thinking14.6高于8B13.1不识别规模因果。Gen 的 Nano18.3±2.2、GPTImage9.8±1、QwenImage4.8±.7与 text task 不直接可比；maze/connect-lines零分是所测条件的负侧，不证明所有视觉外部化路径无效。

§6 qualitative 错误和语言瓶颈故事没有匹配 encoder、latent/output 干预识别唯一原因。Qwen3VL8BThinking 的1400训练例 RLVR、8 H800约3天/18epoch、rollout10/16k 有真实成本；训练起点34.2与 BabyVision13.1属不同分布，整体+4.8且 tracking 少增或退，不授所有视觉原语已修复或更长思考有效。视觉生成例子也有错误，不能由图片对比授 bypass language 因果优势。收集/QC、reference、人审、judge、重复调用、生成与 RL 都须分账；闭源接口、snapshot/精度与全流程硬件缺口不授速度/生产收益。

Books 实际顺读 Ch66:56–80 的 contract/semantic quality 对象，706–745 的同题输入消融、任务必要性与可见证据分母，3060–3090 的 causal gate。已有合同支持这些边界，未精确覆盖 BabyVision image-overlay judge 配方；不据一般映射称 Existing。采用的是局部 visuospatial task/evaluator 校准，尚无新的永久系统路径或语言因果机制，标准仅报告足够。可以正式同步5分 Only；不改 Books、无需锁。

## 本组状态

两项5分标准 Only 终判通过，证据与直接反侧已够，停止必要读取；无普通 Books 待办、无 actual POST 或共享写锁请求。仅本组闭环，不代表 Jan14 普通工作清零或 DAY。后续组须独立具名授权/ready，不从 owner-proposals 标题自动展开。
