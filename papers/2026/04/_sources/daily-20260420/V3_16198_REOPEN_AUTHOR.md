# 2604.16198v1 REA-Coder：从“成熟自检组合”前关闭的定点复核提案

作者 `apr20_resume`。本篇先前完整题摘表以“需求重述/自校验循环仅提升 benchmark、无 spec authority”拟前关闭。否定侧抽检对[官方 exact-v1](https://arxiv.org/html/2604.16198v1) §3.1–3.3、§4.2–4.4、§5.1–5.2 Tables 1–2、§6.1 Table 3 的必要段落后，认为“无最终 spec authority”正确，却不足以关闭其**前置需求理解探针和后置代码→需求反向校验的分工**，暂撤销该前关闭，待非作者按当前§3有限核；不预记正式候选。

后续状态：具名[root 有界非作者核](./V3_ROOT_16198_FINITE_INDEPENDENT.md)已通过 `2+1+2=5` 标准／仅报告与 Ch79 现有责任对照；本日正式 §3–4、具名首次公开联合链均已同步。上一段的“待核”只记录作者提案时的状态，不是当前待办；整日 Gate 仍未完成。

§3.1 在代码生成前从原需求的多个维度让模型生成 question checklist 与 reference answers，再让生成模型回答，逐项比较误解项并补充到保留原文的增强需求；§3.3 在代码失败后遮蔽需求关键语义片段，依据生成代码反推遮蔽片段，发现与原需求不一致再更新 checklist。这比泛泛“让模型再检查”多了明确的两个可互相定位的检查点：**输入理解是否错，输出代码是否体现给定需求**。它可能影响 coding-agent 是先多采样代码/只做 execution repair，还是先花预算检查约束理解的选择；只属单工作流的验证机制，不等新的用户授权/最终语义 oracle。

§4 Table 2 对四模型×五 benchmark 分别去掉 QA 或 MASK 的有限消融，多数分数下降；如 Qwen3-Coder CodeContests 33.33%，无 QA 30.30%，无 MASK 25.45%。§6.1 的 first-generation（只有 QA，尚无后轮 MASK）相对 zero-shot 提升，支持“收益不全来自多轮生成”，但 token/时间未匹配，Table 1 的 full REA-Coder 明显多花调用（Qwen 2.65h/11.78M tokens，相比 zero-shot 0.34h/0.74M；DeepSeek 2.78h/9.74M 对 0.32h/0.37M），不能宣称 QA 是唯一原因、净生产收益或低成本默认项。所有 reference answers 仍由 LLM 据需求与少量人工示例生成，模型同时判比较；public tests 只是停止条件，并非完整用户意图证明。benchmark 的 Pass@1 是作者多阶段方法最终输出的受限分数，不可混作“单次模型采样”或实际软件验收。主文未给代码污染、并发、CI、真实 repo 成本与独立用户 sign-off。

拟准入语义为：在已有“输出测试≠需求被正确理解”的约束下，原文提供**生成前问题/答案逐项探针 + 生成后遮蔽片段反向对齐**的可拆验证分支与有限消融，值得标准核以确定其边界；不是标题、任务得分或成熟组件重新命名自动准入。暂拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5` 标准、`Only`。实际[Ch79](../../../../../books/part-07-agent/79-planning.md) 已有 collect requirements→implementation→tests 与 machine-checkable milestone/独立 commit 分权，该论文无新 authority owner；其 recipe 与基准仍可在本日受限报告，不为“已有章节”泛判整篇 Existing。请非作者只核上述 §3.1/3.3、Tables 1–3 对照与 Ch79 两处现有命题；若认为其没有超出成熟 prompt checklist，请明确哪个已有机制和受控证据使该局部选择不值得准入，而不是沿“无 spec authority，所以关闭”的旧理由。
