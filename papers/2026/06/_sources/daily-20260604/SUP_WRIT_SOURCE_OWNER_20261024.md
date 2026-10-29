# WRIT 02908 — necessary Source / actual owner / PRE

作者 supp_20260604_author；R2 准入/Jun03 日期有效复用。正式 2+1+2=5；训练数据构造两轴的具体缺口加深。exact-v1 完整流 TEXT 已实存，作者必要读 §2–4/T2–4/Limitations/D/E/I，支持与关键反侧足够停止；未核代码或复现。

## 必要 Source

§2–3 将 task=(userrequest,initialDB,goldwrites,goldfinalDB) 与 conversationtrajectory 分开。write 原型→合法 DB 参数→隐藏 backend IDs 的偏好请求；multiwrite 拼接有程序冲突检查。read-heavy 固定一个 goldwrite，扰动包含 goldarg 的 readcall 参数得到 evidencepool，再由 LLM 生成要求比较全部证据且恢复唯一 goldarg 的请求；LLM verifier 检查 readcallcoverage/recovery/writeconsistency。不是确定性证明用户语义或最小必要读数。脚本只改披露/纠正/施压方式，按构造维持 goldgoal；不覆盖真人改变目标。goldwrites 在 sandbox 执行得到 finalDB，模拟保留到达该 state 且无 toolerror 的 clean successes；终态匹配不保证每步合规/意图真实/所有权限安全。

§4 主比较各 2K trajectories，Retail/Airline 各 1K，不是等 token/生成/训练 compute。三 backbone full SFT：Qwen3-4B-Instruct-2507、Llama3.1-8B、Qwen2.5-14B。T3 4B w/o readheavy 的 AirlineHard Pass1 57.50→41.25、Pass4 40→15；w/o script 和 multiwrite 各有退步，但未匹配全 token预算、未给训练 seed 独立重复/显著性，不说普适独立因果。四次 eval 的 ± 是 trial sample SD，非训练 seed CI。Pass^k 是 k 次全成功，不是至少一次 Pass@k。Hard 是 hardestdecision约≥6 reads，非所有线上任务的客观难度尺。

E/I：4×RTX PRO6000 96GB，BF16 fullSFT2epochs/lr1e-5/AdamW/cosine10warmup/maxseq16384。合成agent Qwen3.6Plus T.2，usersim GPT5.1 T.7；evalagentT0，usersim GPT4.1 T.5。T4 outputtoken只agentcompletion，不含 input/tool/usersim、本地GPU、制备/筛选/训练费，不能签总成本优越。Limitations：两轴主要分别研究，multiwrite同时readheavy组合及最佳mixture未充分研究。B全尺寸对照只是核抽样混杂，不使 headline 规模/总费可比。保真实轨迹、人工语义/政策审计与独立 heldout 回退。

## actual owner

三 Books context、ROADMAP与actual Ch27开头/合成数据相关论证、Ch28开头、Ch29 SFT数据质量/Scaffold与交接已读。唯一 TRAIN-DATA Ch27：此项改变 sample task 支持与生成条件，不改变 Ch29 SFT objective，也不是 Ch81 线上写授权。Ch27 Synthetic data 开头已有 generator/judge同源风险，后侧 HybridResearcher 是跨source loadbearing桥，491条件行为树是branch触发；没有“writecount × 每write的readburden”这条样本复杂度分支。选在Synthetic开头两句后、HybridResearcher完整段前，仅两段。

完整上锚：

最直接的 synthetic-data pipeline 是让模型生成任务、回答或 Agent trajectory，再由另一个 model judge
过滤。它便宜、覆盖开放语义，在 verifier 难以形式化的任务中仍然合理；但 generator 和 judge 可能共享
事实错误、风格偏好与同源 blind spot，语言上自洽不等于环境中可执行。

拟增两段：

面向会修改环境的多轮 Agent，样本难度还应区分写决策有多少与每次写前需要比较多少读证据：增加后续写操作训练长程执行，却不必然训练一次提交前的广泛查找。一条[受限合成分支](https://arxiv.org/html/2606.02908v1)从合法初态与 gold write 出发，保持写目标不变、改变候选读调用及其证据池，让自然偏好而非 backend ID 指向目标参数；再单独改变用户披露、纠正与施压的方式。这使任务支持、读证据负担与对话实现成为可分别记录的生成条件，而不是只按轨迹长度或工具调用总数定义覆盖。<!-- source-family:SF-2026-ARXIV-2606-02908 -->

这条路径仍用模型审核请求是否要求读齐并恢复目标参数，再按 sandbox 终态与工具错误过滤示教；终态正确不证明全过程合规，脚本维持原目标也不覆盖真实用户改变意图。两个服务域的等轨迹数消融支持补充读密集样本，却不等 token 或完整训练预算，且尚未充分研究两轴组合与最佳 mixture。生成、全部失败模拟、用户与审核模型、执行筛选、SFT 和独立行为回归均计费；请求歧义、政策或目标支持不足时，保留可信真实示教、人工/独立语义核验与原配方，不把 clean success 或较少线上输出 token 当作完整监督真值与净省费证明。<!-- source-family:SF-2026-ARXIV-2606-02908 -->

完整下锚：

合成跨工具任务时，还应让一种来源的输出真正成为另一种来源的必要输入，而不只把两个单源数据集混在一起。可以从已验证SQL或搜索seed抽bridge entity，围绕它构造缺失的另一端，再检查桥接值未泄露在问题/最终结果中、删去关键predicate确实改变结果，以及干扰证据不能单独回答。[HybridResearcher的有限分支](https://arxiv.org/html/2610.24899v1#S3)将这种load-bearing设计用于训练数据，但membership、mask judge和合成唯一解仍不穷尽所有shortcut，也不认证真实web依赖。最终答对、同judge多数与单源能力局部保持不能分别替代路径必要性、真值和任意遗忘回归。Seed、合成文档/数据库、执行与质量过滤、teacher轨迹及全部SFT/RL均计费；桥接不足或迁移回退时保留真实跨源轨迹、独立执行验证与原single-source能力回归，不由更多混合条目签发组合推理已学会。<!-- source-family:SF-2026-ARXIV-2610-24899 -->

本人 true H2 Review note 拟：`SF-2026-ARXIV-2606-02908`：2+1+2=5；exact-v1 §2–4/T2–4/Limitations/D/E/I，写数与读证据负担两轴、固定goldgoal脚本与终态过滤分责；保LLM verifier非语义证明、等2K不等token/总费、Pass^k全成功及四trial非训练seedCI、两轴组合/mixture未充分研究。未核实现或复现。待实际写后复核。
