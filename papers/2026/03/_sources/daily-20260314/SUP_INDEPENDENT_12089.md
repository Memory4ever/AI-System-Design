# 12089 EmbTracker：独立必要 Source／评分／owner／PRE

复核者 mar13_admission_review（非准备者）；2026-10-10。只核 03-14 Daily 补充的 2026-03-13 北京时间完整自然日与本项 exact-v1。重新完整读取当前 AGENTS、Research／Report 合同和统一 Prompt，以及 Sources 使用说明／Daily 分组／arXiv 范围、本日 README 停点、最新相关 checkpoint 与 ROADMAP owner 路由。此前本项题摘／当前事件信号和十项日级日期独核有效复用，不重查首稿、旧版或其他日期。

## 原件与真实必要阅读

实际读 `SUP_EVIDENCE_12089.md`，但不以准备者结论替代原文。实际核 `SUP_NARROW_WATERMARK_MANIFEST_RESULT.json` 中 `https://arxiv.org/html/2603.12089v1` URL／final URL、GET200、340597 bytes、UTC 2026-10-10T01:52:01.115372Z；实际读 `SUP_NECESSARY_12089.raw` 原标题身份及 `SUP_NECESSARY_12089.txt`。

实际必要范围：III-A／B threat model、IV-A–E 全部拟用机制与 Eq3–4；V-A setup、V-B 完整 TableII／VI 定义、V-D／E 完整 TablesIII／IV；V-F 人口规模混杂、V-G 参考制备人口、V-H poison 与训练条件、V-I training-time 口径、V-J 直接变换反侧、V-K overwrite／TableVII／timestamp 和 CA 提议，及结论。未读图像 pixel 数字、代码／复现、全联邦平台或全部附件／引用，未遍历旧稿；未把图 caption 读取称为图数值验证。

## Source 边界：受限 PASS

实际新增是共享水印载体与个性化发行的分责：server 仅初次训练 universal trigger 的 embedding，保存该向量；发行时将它替换到各 client-specific token 行，并恢复 universal token 的原向量。client 更新 PEFT modules、embedding 保持冻结；server 聚合 modules 后恢复 universal watermark embedding、以水印数据强化与 client 同范围的 modules，再作个性化发行。初始化不是每 client 重训，server 每轮仍有 reinforcement；不能从“只训一次 embedding”推出全流程免训练、零通信／存储成本或任意 full fine-tune 持久性。

III 的 benign server、client 遵循训练协议／不知水印／不串谋是安全条件，不是材料证明了恶意 server／合谋安全。V-K 单 client 知道一般机制但不知道 assigned embedding 的 overwrite 不消去这些范围限制。TableVII 原 watermark VR 从100变98.43、新 watermark99.67，并存而非自动排除伪归因；timestamp／CA registration 是作者建议的扩展，没有相应责任排序协议／攻击安全实验或不可伪造证明。

IV-B 签名认证的是个人 message；hash 再映射有限 tokenizer 词表中的 trigger。原段没有完整无碰撞分配、重试／注册或具体发行 artifact 签名绑定协议；RSA／SHA 名称不直接认证这些缺口。若两 client 映射同 trigger，不能满足彼此排除的归因条件。保存 message／映射／发行／更新身份及检查冲突属于由接口推导的验收要求，不能写成作者已认证的协议。

Eq3 的规则是自身 VR≥γ，并且其他 client 的 VR 各自<γ；Eq4 的 VR 是分类 target-label 命中或生成 preset-target substring 命中，不是语言真值、所有权概率或泄漏阻止。V-B VI=自身VR减其他client的平均VR；平均值低不证明每个他者均<γ。保留有限行为矩阵检测为辅助取证，不将其升级为零FPR、法律责任或完整 confidentiality。

V-A 主条件实际核到：BERT、Llama-2-7B、Qwen2.5-VL-7B；10 clients 全参与、20轮、local3epochs、Dirichletβ=.5，server 有自有数据；watermark Adam lr2e-5／5epochs／batch4／10%poison。TraMark 分类受类别数≥clients 限制，并非全部任务同能力 baseline；相同 watermark 样本数也不等总训练预算。V-J 主结果 FP16／FlashAttention2；完整硬件、local PEFT 配置、serving 并发／SLO、重复seed／CI和完整 CA／网络成本在所读必要原证未披露，不补造。

实际 TableII 直接负侧保留：OK-VQA IID ACC49.74→46.30（-3.44pp）、NonIID46.06→43.83；CoQA NonIID70.48→68.67。TableIV SCAFFOLD CoQA73.69→70.67（-3.02pp）。这不支持统一“1–2%以内／无损”。V-F client数量改变同时每client样本500→100，不签固定数据规模下可扩展性的唯一因果；TableV NQ1%poison VR13.76、5%96.43，参数选择会改变检测能力。V-I 图仅20轮 training-time 比较，无图像数值或完整服务成本，不采用精确净开销优势。V-J pruning≤30%局部测试和已测finetune／噪声不能扩成任意更新或移除攻击；量化仍高VR却显著损伤ACC。原文把强pruning后能力下降称作无需保护，不能替目标威胁审计作普遍豁免。

## 独立评分与 actual owner

接受 Design2 + Reach2 + Durability2 = 6。Design 是一次通用载体训练、client token 行个性化与共享更新的替代接口；不是 backdoor、签名、hash、PEFT 本身的新发明。Reach 是 server 发行／client 更新／聚合强化／黑盒验证的实际跨边界联动，不借章节数或性能宣传。Durability 是发行身份、持久性条件和检测责任的可复用约束，不授密码或法律基础。标准必要 Source 已足；实际长期 owner 差额触发局部深入，不因采用 Books 倒推分数。

唯一 owner 是 ROADMAP 的 `PLATFORM-SECURITY`／`books/part-06-ai-infrastructure/72-security.md`。实际完整顺读178–224：可信执行／confidentiality → 权重外传取证非预防 → 同方向shares协作门限 → 生成组件水印 → 重构／不可伪造 → trace行为取证及下一标题；另读529–560的提取审计／secure-aggregation attribution 完整局部。实际读 Ch71／Ch73 的职责入口，仅交接未变职责。

现有协作门限段控制共享白盒验证权和同方向shares，不承载“共同PEFT modules＋发行embedding个性化＋API按client验证”的副本归因。组件水印段已承载替换／更新持久性与费用，但未承载此聚合／再发行机制；trace段针对学习输出的学生，secure-aggregation attribution 针对训练数据影响update，并非泄漏的 client model instance。因此不是按水印主题默认 NC，而是有明确未覆盖的发行对象与检测条件差额。通用 soundness／unforgeability 和模型访问控制仍由原局部承载，不重复宣称这项拥有相同保证。

## PRE：一处阈值精确化后 PASS

插在完整协作门限两段之后、生成系统组件水印段之前；保留前段白盒权限假设和后段组件／不可伪造责任。第二段原“响应过阈值／各自不过阈值”容易把≥／<边界写混；按实际 Eq3 最小改为“响应达到阈值／各自低于阈值”。其余机制、费用、直接反侧和回退可采用；发行身份绑定清楚标为接口推导要求，不认证作者已有协议。

冻结准确两段如下，供 root 实际写；此为 PRE，非 POST。

共享验证权与追查哪份发行副本外泄，是两种不同问题。若可疑服务只允许黑盒查询，另一条分支可先在服务器训练通用 trigger 的 embedding，再把同一向量映射到每个 client 的不同 token 行；客户端只更新 PEFT modules，服务器聚合并用通用 trigger 强化这些共享 modules，随后重新发行个性化 embedding。[EmbTracker 的受限联邦对照](https://arxiv.org/html/2603.12089v1)据此避免为每个 client 单独重训 watermark，但持久性依赖 embedding 在客户端更新中保持冻结，不是任意 full fine-tune 的承诺。这里归因对象是发行给 client 的 model instance，不是该 client 的私有训练数据、前述门限 key 的完整性或被阻止的泄漏。<!-- source-family:SF-2026-ARXIV-2603-12089 -->

验证须同时要求本 client 的 trigger 响应达到阈值、其余 client 的响应各自低于阈值；其他 client 的平均响应低，不能替代逐个排除。签名 message、有限词表中的 trigger 映射、发行模型与 PEFT 更新身份、验证样本/阈值及后续变换应绑定留档，这些是据接口推导的验收要求，不是作者已认证的发行协议或不可伪造证明。当前原研究依赖可信 server、遵循本地训练且不串谋的 clients；新增 overwrite 测试仍保留新旧水印并存，timestamp/CA 排序只是建议。初始化与每轮强化、个性化发行存储和逐 client 查询均付费，VQA/部分联邦优化及量化质量反退保留；超出冻结 embedding、攻击或校准人口时保留 Unknown，回退签名 origin/provenance、访问控制与独立取证，不由高 VR 认定法律责任、零误报或完整 confidentiality。

## 本有限包终态

Source 受限 PASS；6分／具体 owner 差额 PASS；上述最小修正版 PRE PASS。只有本项独核文件被写入，不改 Report／Books／State／共享 ledger、不stage／commit／push。没有授实际写后 POST、全日 DAY、全来源覆盖或完整安全保证；root实际写入后仍须非 writer 顺读实际两段／完整邻接／本人末注回源。
