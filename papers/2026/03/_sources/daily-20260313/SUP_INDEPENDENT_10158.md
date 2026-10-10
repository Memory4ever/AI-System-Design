# 2603.10158v1：XL-VLA 必要Source / owner / PRE独立复核

复核者：mar13_admission_review，非准备者、非 Books writer。仅 2026-03-13 既有 Daily 补充 2026-03-12 BJT 自然日。恢复已实际读 AGENTS、当前研究合同、来源使用说明/Daily/arXiv、Report/Prompt、ROADMAP、最新本日路由与 README 停点；并读 PROJECT_CONTEXT / LEARNING_PHILOSOPHY / WRITING_GUIDE。题摘准入/日级日期有效复用，不重开其他日期或版本史；只 own 本文件，不授 formal / 实际 POST / DAY。

## 精确原件与实际阅读

实际回 [作者准备包](./SUP_EVIDENCE_10158.md)，不是将其摘要代原证。核 [原响应](./SUP_CORE_10158.raw)、[提取文本](./SUP_CORE_10158.txt)、[manifest/result](./SUP_CORE_10158_MANIFEST_RESULT.json)：官方 `https://arxiv.org/html/2603.10158v1`、GET200、397533 bytes、2026-10-10T04:20:38.664175Z；标题 Cross-Hand Latent Representation for Vision-Language-Action Models。实际核本日 [ABS](./SUP_ABS3_10158.raw) 精确 v1/项目 Comments/history，无当前可见撤回或纠错信号；不是全版本无标记保证。

必要原文实际读 §3.1–3.2.2 全机制与 Eq1–4（另从 raw 按 section/数学 alttext 定点回读）、§4 问题/数据/训练配置、§4.1–4.2 全文字、完整 Tables2–5、§5，以及 Appendix6.2–6.4 / 完整 Table6。T5 从 raw 表格逐行核；图4/5/6/7/17只用已读正文/caption，不认证未视觉曲线/格数字。未读全部图库/视频/代码、未运行 artifact 或复现。

## 必要Source裁决：受限通过

1. **独立 codec 生产→冻结 VLA 消费确为原机制。** §3.2 从各本体 hardware joint limits 随机采样姿态，经 source encoder 后由所有 decoder self/cross-decode；L1 是自重构，L2 是 FK 拇指–手指距离/方向，L3 是 posterior 到标准 Gaussian 的 KL。一个 backward joint 优化所有手头。人工手指对应及四指 Paxini 省略 little-finger pair明确，故无需成对示教不等于无需本体范围/运动学/对应关系。Eq1 的“no embodiment degraded”和 KL 的共同分布描述不提供普遍行为等价或安全保证，本次不采用这些强结论。
2. **state/action 消费资格原文明确，但 time packing 不补造。** §3.1 将 previous **executed action chunk** 编成 latent history，替原 state tokens，vision/language 与其共同条件预测下一 latent，再选手型 decoder 返回 joint chunk；VLA finetune 时所有 E/D 冻结、hand ID 不作显式 backbone token。chunk64帧/20Hz披露；§3.2 MLP 以单 q-pos vector定义，未据此确定逐帧或整 chunk 唯一可执行 tensor recipe。拟书稿只采用职责分工，不依赖未披露细节。
3. **主评价保持人口与直接反侧。** T2同 multi-hand/multi-task 数据的 shared π0 对 XL-VLA，完整 Mean为 .32→.72；§4.1正文 .55→.90实际对应PC列，不能作全表均值。Ability PushSugar .30→.30 不支持每任务严格提升。T4两手组 replay .60/.61→.82/.81 是有限真实动作重放，不签任意手型语义。VLA仍使用2000 demonstrations / 2M state-action；“无监督”只限 codec，不能称整个学习流程不需示教。
4. **zero-shot不是从未适配的新手。** Fig4/§4.1 是已经训练 codec 的手型×heldout task 组合；π0+RT是 XHand 全tasks训练再 retarget，训练人口不同。不采用全部格 “never underperforms”，也不认证新手无 codec 自动执行。G1只 Inspire，T6四任务 .525→.825 是另人口。
5. **重构不代跨手几何，几何不代完整物理行为。** 完整 T5去 L2(both) 的自重构Joint/Tip 3.781/2.602优于5.476/3.703，而 pinch/random方向62.733/71.765劣于11.857/10.492；两类质量不能互代。L128有多项更好，不继承“变大皆退化”。noise .05连续性与插值 acceleration/jerk只几何 proxy，未覆盖力/碰撞或全部闭环成功。
6. **费用与有限评价条件近采用范围保留。** 实际8 H100 80GB、60K steps/b128、约10h是policy训练，不是全部codec/示教/标定/部署时间。App6.2/6.3视角、960×540→320×240→224²与每setting10试验、同手固定initial joints/随机objects限制保留。PSR正文 .25/.5/.75/1 与caption/App单臂 .5 口径不统一，不把 partial 与 full success合并，PRE不引用该数字。完整 codec费用、deployment precision/latency/batch/concurrency/SLO未披露，不从64帧推3.2秒无须重新观察。

## 评分及实际owner差额

**2+2+2=6通过**。D2是随机pose/FK跨decode生产独立多手接口的具体替代设计，不借成熟VAE/KL加分；Reach2跨codec预训练→冻结VLA输入输出→目标本体decoder消费；Durability2是可重用的本体几何/动作schema一致性约束，不借通用安全controller加分。具体长期缺口触发受影响深入，支持/反侧足够，不再全附件。

实际顺读唯一 owner [Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 当前23–45接触/latent-goal分支、83–137规范化→canonical25两完整段→Privileged3D完整邻接、279–310共享手部骨架 start–goal 监督及相邻表示分支、1–24与137–154物理提交/多时间尺度合同；Ch25开篇1–48保留环境transition vs policy channel、Ch27开篇1–35保留数据生产 vs action语义职责。无新owner。

现 canonical25 统一 arm/TCP/jaw 几何并以目标kinematic decoder消费，已有手部骨架分支则依赖 human/robot start–goal transition监督和冻结 tokenizer/bridge targets。两者都未具体承载**本体范围随机单姿态→FK跨手自监督decode→独立预训练且冻结的输入/输出codec供共享VLA消费**。故不是主题相近的NC，也不因已有跨本体/codec名称而重复写成熟原则。拟插在 canonical25 两段后、Privileged3D标题前，可承接“共同几何接口如何生产与消费”；旧 canonical / 接触迁移 / shared-skeleton 分支保持共存。

## 两段逐字PRE

已对照准备包“逐字PRE”两段全部事实、收益、费用与回退，**PRE通过，无必要事实修改**。第一段从“不同多指手型还可以共享学习到的动作坐标”到 hand identity/backbone，符合原文职责且将 Gaussian限制为塑形；第二段将 zero-shot限于已有codec组合、分验重构/目标手几何/真实闭环，保留费用、未明time packing和独立控制提交，不采用强无损/无退步/任意本体安全主张。

冻结 schema / decoder revision、短chunk重新观察及controller接管是由证据边界导出的工程选择，不冒称本文已实现全部安全机制。root可按此两段窄写，作者/其他非writer仍须实际顺读写后新增、完整邻接及 root 本人末注再授 POST；本文件不授实际写入或单日完成。
