# Tokenforge：必要证据与 owner 增量（root 实际写后通过）

原源：[2601.00065v1 HTML](https://arxiv.org/html/2601.00065v1)。已实际读 §3–4.3、§5.1–5.3 和 Appendix B 的必要范围。标题以本次 exact-v1 的 The Trojan in the Vocabulary: Stealthy Sabotage of LLM Composition 为准，不用后来的改名版本代替。日期依据见 date-fields-screened.jsonl；原 Submitted Dec31T19:00:03Z，官方假期与不可 advance 规则给 Jan5T01Z lower，registered Jan5T02:19:31Z 只与身份/排程合取作 upper，不作直接公开时刻。仍需 root 核该具体合取及作者更早公开信号。

## 原文事实与反证

§3 的攻击面是 donor tokenizer/embedding artifact 可被修改，base checkpoint 已知且可提取其 shared-token anchors/feature direction。迁移先在 donor shared-row basis 求系数，再在 base anchors 上复用；攻击优化让新行在 donor 特征上弱、在 base 迁移后特征上强。固定 donor 上的 row/utility 检查因而不能担保组合产物。这不是 token ID 自身携带固定语义，也不是任意 donor→base 都必然失效。

§4 是 frozen 模型与新 row 的优化，training-free 不等于无需优化、统计或 feature collection。§5.1–5.2 的正文受控矩阵为五个小模型的 20 directed pairs，SER 是指定目标 token 的采样发出率，不能替代真实有害行为率。原 donor utility、正常 OMP transplant、攻击 transplant 与扰动 baseline 分账；clean transplant 本身也会回归。§5.3 一轮 LoRA 能抑制原 SER；恢复实验随后额外增大 row norm，不能写成“未经修改的攻击持续穿透 fine-tuning”。Appendix B 的 post-transplant emission/utility、不同 context/temperature 检查是可采的验证方向，不是已证明完备的防御。

## 当前覆盖与拟写入范围

ROADMAP owner 为 MODEL-EMBEDDING，Ch12。现正文“向量关系从训练目标中形成”已有 checkpoint 坐标系不能直接比较，但没有 donor coefficient reuse 将低风险新行变成另一模型高响应方向的具体组合边界。Ch11 的 tokenizer/checkpoint 联合迁移已拥有 token→ID/分词/初始化资产身份；只作交接，不在两章重复机制。Ch13 拥有位置，不改。

以下两段已获 root source→owner 与窄 ownership 许可，实际插入 Ch12 L104–108；root 对读实际新增与 Ch11/13 交接后，非作者写后通过。原提案保留如下：

“跨 checkpoint 扩展词表时，一种合理初始化是先用共享 token 的 donor rows 表示新增行，再把相同线性系数用于 base rows。这保留了词表身份之间的锚点关系，却没有保留两个模型的全部几何与读出：donor 中对某个内部特征或输出方向的低响应，不推出迁移后的 base 行仍低响应。新增行、共享锚点、迁移算子及 base 的 embedding/output head 因而共同定义组合产物；只验 donor 的近邻或整体任务质量，不能把其行为信任自动传给组合后的模型。”

“这条边界要求迁移后再验新增 token 的发出行为、原任务回归，以及不同上下文和采样条件，而不是取消旧的 lookup 或所有线性初始化。一个受限攻击实验通过修改 donor artifact 并利用已知 base 几何构造了这种差异；它不证明任意模型对都会受害，也不提供完备防御。后续 fine-tuning 可能抑制异常，额外调整行范数则又改变了被验收的产物。分词和 token-ID 的联合版本交接仍由 Ch11 承担，本章只拥有行几何及其与后续读出的耦合。”

已另加首项 primary-source Review note，明示 exact-v1/§3–5/B、作者受控结果、SER 非实际 harm、LoRA 后 norm 修改条件及未复现实验；源注已同步 root 实际非作者写后通过。Ch12 锁已释放，单篇采用不替代 Jan06 日级 Gate。
