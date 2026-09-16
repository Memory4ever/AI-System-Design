# 2026-05-14 Round5 Root Books Synthesis Queue

**状态：** `5 pending root writebacks`  
**边界：** 只处理 fresh non-author 终审点名的六个 false negatives；其中五个需要写回 Books，`2605.13821` 为 concrete No Change。作者未编辑 Books。

Root 应按章节主线与日期顺序写入 Review notes 之前的机制正文；下面文字是可直接吸收的中文语义，不是论文摘要拼贴。每项完成后再添加唯一 source-family marker，并交 fresh non-author 复核。

## `MODEL-SELF-ATTENTION` · Ch14

### `SF-2026-ARXIV-2605-12879` — Train-then-compile 的 Attention 分支

Sinkhorn attention 在训练和推理中重复执行 matrix scaling，训练时利用双边 marginal 归纳偏置很合理，但部署时继续支付每次 forward 的迭代成本；简单减少迭代次数虽然更快，却会把已训练层换成另一个 finite operator。一个条件分支是在训练结束后冻结 teacher，用未标注 calibration activation 拟合 sliced potential 到 closure-ready source dual，再在推理中以预测 dual 和固定的 two-sided entropic c-transform 构造 attention plan。这样训练仍拥有 Sinkhorn semantics，部署则把反复在线迭代转成可版本化的离线 compile artifact。

这条分支没有让 attention 稀疏或 subquadratic：dense QK score 与 value mixing 仍在，calibration dataset、teacher 的 finite-update convention、coefficient 和 activation distribution 都成为 layer identity。分布漂移会要求重校准，linear dual map 也可能损失 teacher fidelity；主文的 square uniform marginal 不覆盖 strict causal mask。无法摊销 compile、causal marginal 尚未定义或分布不稳时，原 Sinkhorn 仍是 fidelity baseline；不需要双边 marginal 时，row-softmax/dense attention 继续成立。exact-v1 证据限于 `§4–§6` 与 Appendix D.3 所测 frozen layer 和 vision/text encoder replacement，不证明通用 decoder 加速。

## `MULTIMODAL-EMBODIED-VLA` · Ch26

### `SF-2026-ARXIV-2605-13316` — Action Diffusion 的三轴复用状态

Action diffusion 每轮完整 denoising 最容易维持控制一致性；固定 interval 或只沿 denoising timestep 复用 feature，则在 observation 和 rollout dynamics 变化后容易读到不再匹配的 residual state。若再为每个 timestep 单独运行 pruner，pruning control 本身甚至会吞掉稀疏 decoder 节省的时间。一个受限演进是共享 condition encoder，一次批量生成所有 timestep mask，并让 pruner 与 decoder 异步重叠；同时以 `block × denoising timestep × rollout iteration` 的 3D lattice 组织 current-forward、previous-timestep 与 earlier-rollout 三类缓存，由 gate 在重算和三方向 reuse 中选择。

该 gate 只拥有加速 proposal，不拥有 action commit。三轴 cache、trajectory-level gate training、异步 buffer 和 freshness bookkeeping 都是新增状态；gate 若来自已过期 observation，会把复用错误跨控制环放大。身份或 freshness 不完整、环境突变、接触阶段或 safety-first workload 应触发 dense refresh，并回退完整 denoising与保守 controller。exact-v1 `§3–§4` 只支持 Tesla A40、Diffusion Policy/RDT-1B、模拟 manipulation 与 50-episode 指标；所谓 lossless 不能外推实机安全，GitHub 链接也未在本轮完成 commit-level reproduction。

## `TRAIN-SFT` · Ch29

### `SF-2026-ARXIV-2605-12913` — Teacher/Student 混合 Occupancy 的 DAgger 分支

Offline SFT 使用完整 teacher trajectory，在 teacher 与 student 访问相同状态时最便宜且稳定；长程 tool interaction 中，student 的早期错误会改变后续 state distribution，使稠密 teacher labels 落不到部署时真正访问的 prefix。纯 student on-policy distillation 可以覆盖这些状态，却可能在冷启动时持续产生无价值或不可恢复的轨迹。DAgger 提供中间分支：按 iteration 衰减 teacher intervention，在每个 turn 随机选择 student 或 teacher 执行动作，或让 student 先控制 prefix 再由 teacher 接管；无论谁执行，teacher 都为 visited state 提供 action label，student 再用监督损失更新。

这里必须分开两类 owner：mixture rollout policy 决定 occupancy，teacher 只提供 label，environment/test verifier 才决定 outcome。它以额外 environment 与 teacher inference、复杂 trajectory/version identity、teacher bias 和 context overflow 风险换取 covariate-shift 修正与早期恢复。teacher/student occupancy 已接近、成本优先时保留 offline SFT；teacher 不可用时回退 student-only OPD 或 RLVR，并接受 sparse-feedback 边界。exact-v1 `§3–§4` 与 Appendix B/F 只支持 Qwen3 students、固定 Qwen3-Coder teacher、OpenHands/SWE-Gym/SWE-Bench Verified，不能证明跨 Agent domain 或高风险代码自动发布。

## `PLATFORM-SECURITY` · Ch72

### `SF-2026-ARXIV-2605-12863` — 统一 Generated Code 与 Scaffolding 的 Type/Effect Boundary

Typed tool schema、命令字符串权限和 effect-time authorizer 在动作边界拦截调用，适合工具集合明确的 Agent；当模型开始生成递归程序，而 developer scaffolding、retry loop 与 generated code 又可能分别触发 effect 时，外围字符串规则难以统一表达 capability、data provenance 与 information flow。一个更强但更窄的分支，是把整个 Agent application 放进同一 pure typed host：模型只提出带期望类型的程序，type/effect checker 在执行前验证允许的 effect、capability 与 value flow，解释器只运行通过检查的程序；递归子 Agent 继承相同或更严格的 effect type，不能自行放宽 authority。

这不是“type-safe 即业务安全”。Well-typed 只排除被 type/EDSL 表达的违规，不证明意图、终止、结果正确或动态远端状态；symlink/path resolution 等仍需 runtime check。代价还包括受限 host language、可信 checker/EDSL、type-retry 与 policy vocabulary 维护。无法建立闭合 effect system 时，继续使用 typed tool contract、deterministic authorizer、sandbox、approval 与 effect receipt。exact-v1 `§3–§4` 仅给出 Haskell/TypeGuard 的 provenance、filesystem 与 information-flow case studies，不构成跨语言生产安全证明。

## `AGENT-TOOL-CALLING` · Ch78

### `SF-2026-ARXIV-2605-13228` — Abstract Intent 到 Primitive Tool 的有界 Resolver

Planner 直接生成 primitive typed call，在工具少且目录稳定时最透明；异构工具库扩展后，高层意图可能没有单个 schema 对应，参数缺失、语义近邻替代和复合分解若都塞进 planner，会把局部 action grounding 与全局完成判断混在一起。一个条件分支将 action 分成 executable primitive 与 abstract intent：registry/schema 已匹配则直接执行，否则 resolver 只在当前 action 范围内 repair arguments、substitute tool 或 decompose 成 lower-level calls，并把规范化 observation 返回 root planner。resolver 不得输出 `Finish`，root planner 保留 evidence-sufficiency，executor/policy 仍在 effect time 验证并提交真实调用。

层级 grounding 降低 planner 对 primitive inventory 的耦合，却增加错误 substitution/decomposition、递归循环、预算膨胀、tool metadata 维护与 context pressure；更多调用也不保证更多有效证据。小型稳定目录继续 direct typed call，无法唯一 grounding 时必须返回 typed failure、澄清或人工处理。exact-v1 `§4–§5` 与 Appendices A/B/C 只支持 Qwen3.5-9B、MVTL 与三项 video QA full-system evaluation；不同 baseline 的 preprocessing/runtime 并不完全同构，也不证明高风险副作用安全。

## Concrete No Change

### `SF-2026-ARXIV-2605-13821` — `AGENT-PLATFORM` · Ch84

无需新增正文。Ch84 的“Harness Controller 是版本化策略，不是模型的隐式习惯”“自适应 Harness 只能提交保持成功约束的干预”以及章节小结，已经把 model/tool/evaluator/cost/harness 注册为配对 artifact，把 accumulated history、intervention proposal、external evaluator/holdout、budget、effect receipt、rollback 与 static-workflow fallback 连成完整主线。AEvo 的 process-level state、meta-edit 和 evaluator isolation 均没有改变这一结论；保留 exact-v1 Review note 即可，不为论文名称重复机制。
