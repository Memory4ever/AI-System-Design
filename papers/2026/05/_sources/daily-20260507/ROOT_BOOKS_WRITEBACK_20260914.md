# 2026-05-07 Root Books Writeback

本记录只证明共享 Books 的按序写回已经执行；它不替代 2026-05-07 的非作者最终语义复核。

## 最终作者修复后的补充写回

- `SF-2026-ARXIV-2605-04279` → `MODEL-MULTI-HEAD-ATTENTION` / Ch15：补充共享 token trajectory 与 radial shadow 使 head 正交不推出逐 head 动力学独立；Radial Dominance 仅是受限充分条件。
- `SF-2026-ARXIV-2605-04291` → `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24：补充由预训练 LM 条件分布定义 Glauber-style 局部重采样的分支，并保留有限步非稳态、NFE、streaming 与 AR fallback 边界。
- `SF-2026-ARXIV-2605-04569` → `INFER-TENSORRT-LLM` / Ch49：补充 query-risk 驱动 full/Taylor sparse attention 路由；proxy 只提议，runtime 与 full attention fallback 保留提交权。

三项均具有唯一 `semantic-body-binding` marker，正文位于唯一 `## Review notes` 之前，exact-v1 trace 位于 notes 内；局部 `git diff --check` 通过。root 的检查不是新的非作者终审。

## 已执行

- `2605.04830` → `MULTIMODAL-GENERATIVE-PARADIGMS`：加入 critical-window 诊断、调度边界和受限证据。
- `2605.04932` → `PLATFORM-EVALUATION-SYSTEM`：删除其专属 Jacobian drift 绑定；保留不依赖该来源的一般 deployment-drift 原则。
- `2605.04956` → `PLATFORM-EVALUATION-SYSTEM`：加入 compile、semantic correctness、hardware efficiency、portability 四段 verdict。
- `2605.04971` → `MODEL-TRANSFORMER-LAYER`：分离 residual coherence 与非线性 symmetry breaking。
- `2605.05066` → `MODEL-LONG-CONTEXT`：加入 compute、state、exact recall 的条件性不可能三角。
- `2605.05138` → `MULTIMODAL-WORLD-MODELS`：加入可执行、可反证的 symbolic world-hypothesis 分支。
- `2605.05176` → `MODEL-SELF-ATTENTION`：加入 Attention-as-Featurizer 的构造性 ICL 路径。
- `2605.05189` → `MODEL-LONG-CONTEXT`：将容量绑定 top-1/listwise 读取合同。
- `2605.05204` → `TRAIN-SFT`：加入少步 diffusion 的 student-owned rollout 与 privileged teacher 分支。
- `2605.04061` → `MODEL-SELF-ATTENTION`：区分单位置可解码性与必要/充分因果控制，并加入单点、多点干预和行为验证的诊断阶梯。

## Root 自检

- 九个新增 source-family marker 在 Books 中各出现一次。
- `SF-JACOBIAN-VELOCITY-BOUNDS-FOR-DEPLOYMENT-RISK-UNDER-COVARIATE-DRIFT` 已从 Books 删除。
- 新增正文均包含旧基线、约束变化、机制或状态责任、trade-off、failure/fallback 与证据边界。
- `git diff --check` 对七个目标章节通过。

## 尚待独立验收

- 须由新的非作者 reviewer 验收当前全部 148 项 disposition 与实际 Books；在此之前日报保持 `进行中`。
