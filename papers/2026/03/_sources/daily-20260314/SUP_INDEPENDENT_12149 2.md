# 12149 Linking Perception：独立最低关闭复核

复核者 mar13_admission_review（非准备者）；2026-10-10。唯一范围为03-14补充2026-03-13北京时间完整自然日的本项 exact-v1。重新完整读取当前 AGENTS、Research／Report 合同、统一 Prompt，Sources 使用说明／Daily 分组／arXiv 主题范围，以及本日 README、最新相关 checkpoint 与 ROADMAP 路由。原完整题摘准入／当前可见事件与十项日级日期独核有效复用，不重做venue或旧稿恢复；本包不加载异日材料。

## 1. 身份及实际必要原证

实际读取准备者 `SUP_CLOSE_12149.md`，不以摘要替代原文。核 `SUP_NARROW_CONFIDENCE_MANIFEST_RESULT.json`：官方URL／final URL为 `https://arxiv.org/html/2603.12149v1`，GET200，347546 bytes，UTC2026-10-10T02:02:00.663176Z。实际读取 `SUP_NECESSARY_12149.raw` 的题名 Linking Perception, Confidence and Accuracy in MLLMs，与 `SUP_NECESSARY_12149.txt` 的必要决定段。

实际范围：§3.1／3.2.1 的原图／CLIP attention噪声配对与训练人口；§3.2.2 Eq3–4全定义；§3.3.1 Eq5–7的confidence投票／Voter输出；§3.3.2–3的critique、reflected answer与VCD Eq8–10及投票接口；§3.3.4完整exactly-once Planner；§4.1模型与benchmark／baseline配置；§4.2完整实现细节和完整Table2；完整Table4；§4.5直接case与结论；Appendix A.1–2角色说明、B数据来源／manual filtering的必要决定段、D confidence讨论。未核主Table1全行、其余附表／全prompt图像／所有曲线／代码／复现，不授其已完成；支持与直接反侧已足，未扩附件。

## 2. 真实增量与限定

原潜力准入保留：原图和noised image成对生成，把confidence差与正确／错误标签关联的奖励加入GRPO，再与confidence投票、专家critique和VCD结合，提供局部适配／推理配置可核验增量。不是只有主题关联，不因幻觉／校准名称或三个模块自动增分；成熟GRPO、VCD、投票、多角色原则不计其新增贡献。

原 Eq3 的 C 为每步top-k log-probability的负均值，再对序列平均，非实际生成token自身likelihood或独立正确性概率；正文称低C表示更确定。Eq4使用原C减noised C的ΔC及 `(2correct−1) Cnorm`，没有给出能统一高低方向的完整Cnorm变换；Eq6又以正C作为票重。Appendix D将NMLP称作Normalized Mean Log-Probability，未在必要定义中统一其与Negative Mean Log-Probability的关系。若按原C并取正α／β，原图更确定时的ΔC<0给负perception项；这是条件解释，不能判全部代码必反向或全部实证无效。§4.2 α=.5、β=.1明确属于Self-Check VCD配置，不能补为Eq4 reward的已披露系数。不会为了修复符号而补造唯一实现或要求无限追查可选代码。

§3.3.4 Planner只给三模块的permutation，明确每个恰好执行一次，结果是贡献到共享vote字典；未提供可靠confidence下skip／提前退出的费用门。Voter verbal概率、reflection或VCD都是模型提案，不是外部真值。§4.5一个case先错后改，不证明独立于同一专家的全系统验证，也不消除所有single-point failure。

实际费用：Qwen2.5-VL-7B作base、Gemini2.5Pro作专家；CDRL full-parameter finetune使用8×H100141GB、BF16、batch2、4原／noise rollout pairs，noised输出不参与gradient并不使其生成免费。CA-TTS每问题8samples、T1／top-k40、三个票重.5、VCD额外原／噪图求值、Voter最多3retry。专家Planner／Voter／Critic、图像噪声和训练数据过滤均计费；服务并发、在线SLO和完整专家／OCR／calls成本未由本必要原证给出，不能采用free lunch或同总费用优势。

Table2 CDRL的MathVision OE18.46低于base24.24，而MC34.16高于21.71，局部取舍必须保留。CA-TTS行OE与ALL同为37.99、MC42.95；原表／正文没有足够口径解释，不补成确定无误的统一整表指标。Table4 Origin ECE64.57→62.24、AUC54.81→59.42，noised AUC60.00→60.19，支持该模型／该切片／该metric局部变化，非部署人口校准或“真正知道不知道”。CD方向与C变换仍未有完整协议，原图／扰动配对不单独隔离全部训练质量／视觉信息变化，也不证明perceptual bluntness是所有幻觉的唯一根因。主文LLM filtering与B的manual assessment叙述未统一；1936条训练集制备和噪声是treatment的一部分，不能把改善全归于唯一reward机制。

## 3. 独立评分／最低处置

接受 Design1 + Reach1 + Durability2 = 4。Design是已披露的局部confidence reward／推理配置recipe，并非新的可执行校准有效条件、独立视觉证据权限或强预算选择机制；没有借用成熟PG／VCD原则提高分数。Reach主要影响单个适配和推理组件，不按模块数量、专家角色或潜在章节数量计跨系统Reach。Durability2保留成对扰动confidence目标和实际校准／任务取舍的可复用配置价值，不给摘要free lunch、SOTA或唯一根因加分。

因此最低关闭成立：**已关闭／仅报告，Books0**。保留候选和实际有限结果，不改判EX，不称已有Books具体承载新实验的NC，也不把“未进一步采用”包装成中心机制已证真。无本次要写的长期命题／具体owner gap／PRE，不因工作量、访问状态或章节已有主题关闭。当前必要材料和身份／日期要求已满足，符号披露歧义以限制保留，不需要为了本最低处置重建作者唯一代码或展开全benchmark。

## 4. 权限及检查

本有限包通过最低评分与关闭理由复核；不授全文Source／实现正确／实验复现或DAY。只写本文件，不改Report／Books／LEARNING_STATE／共享主ledger、不stage／commit／push。本日仍有其他普通可执行工作，不将单项结束当整日报完成。
