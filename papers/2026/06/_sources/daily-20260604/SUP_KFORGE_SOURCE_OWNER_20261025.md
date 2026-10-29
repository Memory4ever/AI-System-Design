# KForge 2606.02963v1 首次必要 / actual Ch49 / 原两段PRE

R55准入/notice/Jun03联合日证复用，不第三。作者正式拟2+1+2=5，新增为native profile到建议的候选生成接口、功能/性能反馈分流与跨后端参考可用性边界，主要kernel单组件，可复用；不按两agent/四厂六语言或速度数加分。actual长期缺口深入受影响域。尚无新授/未写，待首次Source/score/owner/PRE，不预I/DAY。

## 证据与读界

https://arxiv.org/html/2606.02963v1 GET exit0，原HTML127072字元无trunc；保mathannotation完整TEXT35123字元真存`2606.02963v1.fulltext.txt`。实际III-A/B/C/D完整、IV-A/B含T1–3与V完整限制、I/II关键比较已读足；未读全部refs/图像像素、实现/复现或四厂六语言各自测试。篇幅短但仍只核支持/直接反侧，不把abstract架构声称当完整验证。

III：两agent并非独立证明。生成器消费问题/历史代码/建议，性能分析器消费当前代码与原生text metrics或GUI screenshot，输出单条优化建议给下轮。模型可配置，迭代/单次/重复采样模式靠prompt配置；不是统一typedIR/跨backend自动等价证书。五状态generation failure/compile failure/runtime error/numerical-or-shape mismatch/correct把错误反馈与性能改写分开，correct仅返回tensor在给定shape/数值tolerance下匹配。原生profile只是观测，建议可错，下一候选仍须验证；III-B引用长上下文检索退化为分角色动机，非本系统实测消融/两agent不可替代证明。

III-D required/banned patterns可限制downcast/fastmath/globalprecision更改，但用户可改prompt、辅助代码和measurement hooks；不是不可绕过sandbox或形式化正确性。每model/iteration保存prompt/response/候选/eval/profile便于追溯，不等独立评价、完整统计或运行过当前代码。

IV-A：Claude Opus4.6 high-effort两case；B200/gpt-oss20b/TRTLLM1.3.0rc9，nsys top10后仅选sourceavailable的三个kernel，不优化closedcubin。512requests、1024prefill/8192decode/batch8、7独立测量；autotuner不确定影响计时，baseline与变体都关闭autotuner且锁1500MHz，结果只此协议。T1 Bias+RoPE+KVupdate在batch8反退3.10→3.12µs；其他batch/kernel速度不等全模型收益。T2吞吐2601.55→2656.61/墙钟1612.24→1578.82仅本执行设置；CV<.1%是run重复不是搜索seed/行为质量无损。原文未充分披露全模型生成质量/所有dtype/TP/LLM总调用费用，不补造，预算/代码未知非外阻。

IV-B：B580/Triton，37个GEMM+tail KernelBenchL2，每题5迭代取best，对faster(torch.compile,eager)，不是B200vendorreference或matchedsearch对照。T3四代表手审提示fusion/FP16 XMX与FP32accum/postprocess、reduction和partition共同变化；5.13geomean不授纯算法/双agent归因、等精度或全模型加速。表列t.comp而正文称两baseline择快，本次不拼完整分母复算。无独立profile-feedback/角色消融，不能因框架可接metrics/GUI就证明该输入在每case必要或普遍跨平台。

V：当前仅PyTorch源；数值测试dtype-dependent tolerance，跨输入differential/formal equivalence是未来；两case均源码reference seed，闭源行为规格+binary oracle仍未来，不把“缺handtunedreference”写成“无源码语义参考”。ISA/PTX生成及attention/MoE完整组件joint优化未来，局部更快会改变register/sharedmemory/autotuner邻居选择。代价包含LLM调用、prompt/辅助代码准备、compile/run/失败隔离、profiler采集/截图解释、调优搜索和端到端重跑；没有全部费用不签生产净收益或自治可靠。

## Actual owner / 具体缺口

已读Book三上下文、ROADMAP Ch48/49/50职责及各开篇；唯一`INFER-TENSORRT-LLM`，actual `books/part-05-inference-system/49-tensorrt-llm.md`。完整相关读`Learned Kernel 只是 Candidate Producer，Compiler 与 Verifier 仍拥有 Admission`及其所有相关验证/回放段，后侧`Kernel Verification...`与`Kernel 能加速多少...`，另`Kernel Agent 应生成 Typed Schedule...`及deviceinitiated correctness-first/performance-slowpath交接。已有正文承载候选/验证分责、测量/端到端质量与预算，不重复泛门或因已有主题NC。

具体尚缺原生异构profile（API/截图）→单条建议→下一候选的接口与功能状态分流，以及source-level语义参考和高性能参考可用性分开。不是新造kernelowner，也不在Ch78/66复制细节。拟仅在Learned Kernel小节原Generator/constraint/compiler分责完整段后/原候选多样性完整段前两段+本人trueH2注，保KernelFoundry与所有他段/marker。无新授/未写。

## 完整上下锚

### 上侧完整段

Generator、constraint solver、compiler、numerical verifier、benchmark harness 与 selector 必须分责。少量
随机 I/O、`torch.export` 成功或单机 speed reward 都不能覆盖 alias/mutation、极端 shape、数值 tolerance、
measurement noise 与 compiler drift。Fragment search 还会带来大量 compile work、artifact explosion 和
hardware coupling。旧 compiler/template 在 coverage、determinism、cold start 与维护成本优先时继续成立。

### 下侧完整两段及现有marker

候选搜索还可以主动保留不同代码策略，而不只沿当前最快样本反复变异。一个质量—多样性分支按代码的memory/algo/synchronization静态描述符分格保留elite，用已测parent→child变化作为选父与自然语言变异的经验proxy，再把参数化template的实测调参与算法proposal分开。它扩大探索，却不由静态标签认证真实瓶颈，也不将所谓gradient启发式变成反向传播；prompt与kernel共演化同样只是proposal侧的选择，不能接管compiler或独立verifier的admission。<!-- source-family:SF-2026-ARXIV-2603-12440 -->

[KernelFoundry的必要原证](https://arxiv.org/html/2603.12440v1)仅支持披露任务、硬件与有限数值检查中的搜索分支；archive规格表述不一致、组件缺独立消融、任务过滤与baseline预算差异限制了归因，不能把整体speedup分配给每项模块。搜索fitness即使给incorrect候选非零值，也不是允许部署错误kernel，代表输入的相似度/误差门不等于全部shape与输入正确。生成、编译、template benchmarking、archive维护和held-out回归均计费，孤立kernel对autograd的计时差也不代表完整模型改善；稳定shape或探索预算有限时，保留手写/原template分支，只有独立correctness与workload-bound benchmark通过才接纳产物。<!-- source-family:SF-2026-ARXIV-2603-12440 -->

## 原两段

生成反馈还可以按问题类型分流：先把未生成代码、编译失败、运行失败、shape/数值不匹配与给定测试通过分开，再让原生 profiler 的文本指标或界面截图进入独立分析步骤，收敛为下一轮的一条优化建议；建议与上一候选共同交回生成器，而不是把整份 profile 当作正确性证明。[KForge 的受限接口](https://arxiv.org/html/2606.02963v1)展示了这条分支，但其数值门仍只覆盖指定 dtype、输入和 tolerance。性能建议只改变待验证候选，不能因为上一版通过或某个 profiler 显示高利用率，就跳过新代码的功能回归；按轮保存 prompt、代码、测试与 profile 身份，才能区分错误修复和性能改写。

跨后端还须区分“有语义参考”和“有成熟高性能参考”：缺少后者的设备可以用已有源码算子指导生成，却不能据此声称已经解决闭源 binary 的规格恢复。成熟 vendor runtime 中选取少数可见热点、与新后端的融合/混合精度算子搜索，是不同的比较条件；取有限轮中的最佳 kernel，也不证明反馈角色的独立收益、等精度或全模型更快。源码/辅助示例、模型调用、编译与失败隔离、profile 解释及集成回归都付费，autotuner 与时钟策略须随测量冻结；参考缺失、数值门或端到端预算不合格时，保留原 kernel、专家调优或成熟 compiler 路径，不让生成器自行批准部署。

## 拟本人true-H2注

- `SF-2026-ARXIV-2606-02963` — Daily2026-06-04补Jun03；[KForge exact-v1](https://arxiv.org/html/2606.02963v1) III–V/T1–3必要，2+1+2=5，具体profile建议接口/参考可用性缺口深入。仅功能状态与原生profile→建议→候选分流；保numerical tolerance非证明、source seed依赖/closedbinary仍未来、B200锁钟关autotuner/7测量与B58037题5轮best不同人口、fusion/mixedprecision混杂/小batch反退及全费，不授双agent必要/四厂完整验证/生产净收益。未核图像像素/代码或复现；R55准入/Jun03日证有效，待首次必要Source/正式分/actualowner/原两段PRE，无新授/未写，不预I/DAY。
