# 2603.10877v1 ARMADA：03-13 独立必要 Source / 5分 / 争议处置

复核者 `mar13_admission_review`，准备者 root。只处理既有 2026-03-13 Daily 的 Mar12 北京时间自然日补充窗。启动重读当前 AGENTS、Research/Report/Prompt、Sources 使用说明/Daily/arXiv、ROADMAP 与本日停点；原题摘准入及主独核 §23 的日级公告夹证有效复用，不重做日期，不加载其他日期材料。本篇不授 DAY。

## 身份与实际范围

实际读 [root 准备包](./SUP_ROOT_EVIDENCE_10877.md)后回 [精确官方 v1 raw](./SUP_ROOT_CORE_10877.raw)、[manifest](./SUP_ROOT_10877_MANIFEST_RESULT.json)：`https://arxiv.org/html/2603.10877v1`，GET200、818243 bytes、2026-10-10T03:47:02.593605Z。实际从原 HTML 顺读完整 §3.1–3.3/Prop1–2/Eq1–7、§4、完整 Tables2–5（HTML IDs S4.T2/S5.T3–T5）、§5–6 必要正文及消融、完整 Table17、结论/Limitations；仅为成本边界追加实际 AppC 配置文字。数学直读 alttext，不采笔记 B 编号为原文页码。图只读正文/caption，不认证坐标；未扩无关全图/附录、旧版、代码或复现。

[完整 v1 题摘及可见 history](./SUP_ABS3_10877.txt)已实际回读：四作者 Ayan Sengupta/Shantanu Dixit/Md Shad Akhtar/Tanmoy Chakraborty；标题 From Images to Words: Efficient Cross-Modal Knowledge Distillation to Language Models from Black-box Teachers，唯一显示 v1，无显示纠错/撤回或具名早稿说明。不由这一轻量检查证明完整版本史；Mar11 Submitted 不作公开日。

## 方法与理论：可支持与不可支持分别保留

§3 的实际接口是冻结生成教师产生表示 → 有任务监督的 TS Aligner → 纯文本学生任务损失/aligner 输出匹配、投影表示损失和辅助头。§3.1 两路使用 ground-truth task labels；不把冻结生成器等同 aligner 不训练。AppC 明确 online distillation 同时训练 teacher-side aligner/student，GLUE/SuperGLUE10 epochs、seq128、batch32/8，LLaMA-7B LoRA rank8/3 epochs。此处只保留论文给出的 recipe，不认证完全实现。

**Prop2 反例资格独立通过。** 其 statement 只以两投影空间同胚为前提；没有另列投影/任务头在样本支撑上可逆，或输出点数等于 batch size。取两个相同表示支撑 `{0,e1}⊂R768`、identity projections（正交且可逆），同胚取恒等；aligner 的线性任务头取第一坐标，student 任务头取零映射。两个输出像分别含2点和1点，均是连续线性映射的像，但不可能同胚。辅助头也可作同样构造。这满足命题所列表示同胚前提；证明后来直接宣称所有输出空间点数等于 batch size，是未证推断，不能反过来作为新增假设排除此反例。若更正明确另假定各任务头/投影在支撑上连续双射，则这是更强的新命题，不是本次已证明。

证明还把 orthogonal projection 的转置当双侧逆；正交投影一般可降维，Table1 的 `h/d→768` 也不自动给双射。反例使用 identity，故不依赖这一记号争议。**表示同胚不能在现前提下担保输出同胚/有效知识迁移**，但这不否定局部任务训练的经验收益。

Prop1 的 `mean||a_i−b_i||≥||mean(a_i−b_i)||` 确由三角不等式支持；原 Eq3 是未归一化内积的 `1−<mean a,mean b>`，证明却在内积前再乘两范数，非一般距离恒等式。即使补成单位向量，`a=b` 时三损失皆0，原严格 `>` 也不能无条件成立；数值损失的排序更不等于优化/泛化正则效果严格排序。本次只隔离该理论保证，不把所有目标函数或训练结果一并判错。

## 评价、黑盒与直接反侧

- §4 确有7学生/不同生成教师、12 NLU/8 reasoning/5 instruction tasks。CoLA MCC、STS-B Pearson 与 accuracy 不同；instruction 的 RougeL 不是事实正确率。T2 三运行均值/SD不授全部后续表同样重复或统一显著性。
- 完整 T2 的 DeBERTa COPA83.7→81.9/78.9/79.9，WiC60.8→59.2/58.2/59.9；完整 T4 LLaMA7B Avg69.0→69.5/69.4/68.9，Winogrande和SingleEq各分支均退。保留局部收益，不认证所有模型/目标或三损失均改善。
- §5.1 所称 Midjourney teacher **明确为 Stable Diffusion + 在100K+ Midjourney images训练的LoRA**。没有由此核验商业 Midjourney 服务、真实黑盒生成输入输出/API权限或内部 hidden 表示可用性；标题的黑盒一般能力与本实际案例分开，不能认证任意黑盒教师接口。
- §6 的随机 frozen aligner 六个 NLU 任务弱于 undistilled，是正文报告的有限对照；未视觉读图，不推精确幅度。§5 alpha=0 反而提高及参数匹配的两组件联合移除对照也说明不能把收益全归单一 logit match/几何对应，更不证明唯一机制。
- **新增必要收紧：shuffle 的强文字与表不能混用。** 完整 T17 的 BoolQ75.8/75.5/76.7，而 T2 BERT-base undistilled75.1、正常 ARMADA75.8/75.1/75.3；按正文所称 BERT-12L/BERT-base 对应，这组数字不支持“BoolQ下降至undistilled以下/约5%”的逐项叙述。若人口/配置另有差异，须先披露对齐，不能自行补造。CoLA shuffle57.9/59.4/60.4确低于T2 undistilled60.8，其余切片有高有低。因此采用“该局部对照显示样本对应关系可能影响结果，存在退步切片”，不认证所有shuffle均有害或同一baseline下全部受损；正文汇总1.8%与p值也不替代这项配置核对。
- Gaussian噪声容忍与打乱样本对应不是同一 treatment；两者都不证明不相关教师自动衰减为安全零影响、一般语义因果或输出同胚。t-SNE/purity/按成功失败筛选的例子也不是这些保证。
- 教师图像20steps/guidance7.5、视频64frames取首帧、音频追加Wav2Vec2；AppC V100/A100、学生/aligner每step .16/.02秒（batch32）是真实披露，但不含已证明的跨负载生成/缓存/预处理/调参与训练总费用。不能由 Limitations “without additional computational overhead” 授免成本或端到端降本；precision、全部负载/SLO及总资源账在必要段 Not Disclosed。

## 独立评分及 Books 终态

认可 **2+1+2=5**：D2 是冻结跨模态生成接口、任务学习的 aligner/表示与输出约束所要求的迁移条件，非成熟 KD/线性投影发明分；R1 是局部训练组件，不以可联想多章升分；Durability2 是可访问接口与表示关系不能直接担保消费者输出的稳定边界。中心理论/黑盒外推直接争议已深入受影响内容，未因争议降分或缩池。

实际核 ROADMAP `MULTIMODAL-REPRESENTATION`，顺读 [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)63–93的encoder/projector、共同空间/正交映射和跨模态任务验收完整局部：现文不从几何对应授任务无损，也保留配对与训练费用。它可以承载将来有效的迁移接口，但本稿 Prop2/一般黑盒保证不能据此写入；**不以主题相似签 NC，也不声称本新实验已被 Books 吸收。**

结论：**必要证据审阅完成；中心保证争议/暂缓，Books新增0。** 受限经验 recipe 与正反结果留本日报；理论保证、任意黑盒教师适用与免费外推隔离，不作正面长期证据。无 PRE/Book 写/POST。本窗重开仅需明确支撑上可逆条件的更正证明、相应投影/任务头实现资格、真实黑盒接口与可比总成本；shuffle精确强结论另需人口/配置与表数值协调。不要求全代码/额外复现或全部附件才结束本单篇，其他普通工作仍继续。
