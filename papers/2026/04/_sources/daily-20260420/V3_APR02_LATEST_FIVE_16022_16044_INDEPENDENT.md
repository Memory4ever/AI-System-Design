# Apr20 最新五项：有限非作者处置与 owner 复核

复核者：`/root/apr02`；依据当前 AGENTS、V3 Research/Report 合同。实际检查作者已有必要证据记录、下列官方 v1 决定性方法/评价/反证，以及 STOP、Tokenizer 的当前机制正文与相关交接。不重扫原始库存、不审全部附录、不核整个日期 Gate，不写 Books 或作者日报。来源访问日：2026-09-27；日期仍由 Apr20 作者的联合公告依据与日级独立复核承担，本记录不把 submitted 当首次公开。

## 16022 SocialGrid — 6，标准完成，仅报告：通过

[官方 v1](https://arxiv.org/html/2604.16022v1)，实际 §2.1–2.6、§3.1–3.2、指标定义及必要 C.2。任务完成、到达、已完成任务中的路径效用和非 skip 投票中的判断准确率是不同分母；导航阶段的 A* 建议不是执行成功 oracle。独立核到 C.2 对动态候选集的机会基线说明，因此不能把全程随机判断统一当 33%。导航组与联赛组人数/配置不同，也不能并成同一能力测量。

新协议和受限失败证据值得报告，但不能从关键词行为或简单分类的相关观察推出模型内部社会推理普遍失效。当前 Ch66 的 protocol / opportunity / composite-outcome 分账原则不需要为该游戏另写主干；保留具体协议，不把整个算法签为 Existing。此次未复现实验或核全体模型配置。

## 16027 输出多样性 — 6，标准完成，仅报告：通过

[官方 v1](https://arxiv.org/html/2604.16027v1)，实际 §3.1–3.3、§4.1/4.2/4.4、§5 与必要任务表。Instruct SFT 从 Think SFT 初始化，再换多源数据和 DPO 设置；RL-Zero 跳过中间阶段，部分 checkpoint 又延长训练，不能把这组 lineage 当只改变教师数的 matched 因果实验。正确答案子集须至少两项，选择后的支持集并不固定；SBERT 与 Vendi 共用 kernel，也不是独立的两次证明。

写作与 IFEval 有局部多样性恢复，不能采用“从不恢复”的强句。较高多样性还伴随部分质量退步。支持保留 post-training lineage / 质量与多样性分账的受限证据；不证明数据组成是唯一因果或通用 diversity floor，不新增 Books。

## 16029 STOP — 6，gap 深入，Ch20 窄增量写前：通过

[官方 v1](https://arxiv.org/html/2604.16029v1)，实际 §3.2/Eq4、主评价定义及 F.1–F.2/Table16。冻结基模型的 prefix cache 上临时追加检查 token，经 LoRA 与分类器打分，随后丢弃检查分支；正常生成明确关闭 LoRA。MC32 continuation 的软标签是相对于生成器及解码策略的成功估计，不是逻辑真值。

实际对读 `books/part-02-model/20-sampling.md` 的“从请求级 Budget 到轨迹内 Feedback Control”：已有双向内部信号、硬外预算及 artifact 绑定，但未承载 **临时评分分支不提交到继续生成轨迹** 的状态责任。作者 `V3_STOP_OWNER_PROPOSAL.md` 的两段只补这一职责，Ch19/45 接 KV 实现、Ch79 接搜索，owner 合理。

收益必须保留 avg@K 与 query-level success 区别；F.2 单 H100 / DS-Qwen-7B / batch16 / prefix2048 的完整吞吐仍下降，检查成本不为零，训练标签构造也另有成本。支持有界写前采用，不代表实际 Books 已写、写后通过或日 Gate 通过。

## 16037 Stochastic Tokenisation — 6，标准完成，窄 Existing Ch11：通过

[官方 PDF v1](https://arxiv.org/pdf/2604.16037v1)，HTML 本次不可用；实际必要 pp2–8，§4.1–4.3、§5.1–5.3、§6.1、Tables2–3/Fig5。STOK-UNI 仅对每 token split count 条件化均匀；UNIFORM-K 才覆盖字符串级给定 edit-distance 的支持集，MDD 构造有成本。不是所有 sampler 都全支持均匀。训练多个分词与 ICL 单个分词示例不是同总预算。

实际 Ch11“Tokenizer 与 checkpoint 是联合行为接口”已明确同字符串不同 segmentation 改变 embedding/position/attention/概率，绑定 tokenizer / checkpoint、行为回归、增强成本与 canonical 回退，完整承载拟采用的一般命题。具体 sampler 与一层/Lipschitz 条件理论仍是本报告受限案例，不声称整套算法在 Books 已有。表中 canonical 或 CSQA 的局部退步、有限攻击范围保留，不采用任意 LLM 的认证鲁棒性保证。

## 16044 SNR-t Bias — 6，纠错深入，中央普适保证窄争议：通过

[官方 v1](https://arxiv.org/html/2604.16044v1)，实际 §4–6 决定性结果、B Eq22/27–28 及 C 中必要递推。Eq27 将向量二阶矩拆成均值范数平方加 **范数本身的方差**；一维等概率 ±1 使左边 1、右边 0，确是原公式而非提取丢失。conditional Jensen 可独立支持平均能量不增，但不能因此推出 Eq22 的标量缩放加 Gaussian 误差。

二元先验经 Gaussian 观测的理想 posterior mean 为有界连续 tanh：非退化 Gaussian 残差无法提供该有界形式，而零残差的固定标量缩放又只有两值。这反驳其一般性桥，不否定满足额外分布假设的条件代数。递推中的噪声平方和还须对应联合关系，不能单凭各边缘 Gaussian 得到。

隔离“任意 reverse 每步必然低 SNR”及唯一原因解释；保留作者局部实测和 differential / wavelet 控制的经验，不否定全部实现。无需写 Books；重开要求合法误差/联合分布假设及条件化保证，不请求全附件或普遍复现。

## 有限终核结论

五项作者窄处置均通过；仅 STOP 是具体 Books 写前 gap，其余为两 Only、一窄 Existing、一中央保证争议。未实际写 Books，不签整日报 Complete；上述通过可由作者复用到相应单篇终态，来源/日期和其他普通待办仍独立推进。
