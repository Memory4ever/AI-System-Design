# L20 Post-training Learning Suite

这套材料用于在公司 NVIDIA L20 环境中完整走通 SFT、Reward Model、DPO、PPO、RLOO 与 GRPO。目标是理解每条训练
路径消费什么监督、创建什么状态，以及 AI Infra Runtime 必须替模型开发者管理哪些资源与恢复边界；它不是一组未经
约束的调参 recipe。

当前状态是 **E0：实验材料与本地结构校验**。仓库内没有 L20 运行结果，所有训练收益、显存占用和性能指标均为
`Not Run`，必须在目标环境运行后填写报告。

## 先消除两个名称歧义

- `Preference` 不是一种单独算法。这里拆成 Reward Model：学习标量偏好函数；DPO：直接从 chosen/rejected pair
  更新 policy。
- `RPO` 不是 OpenRLHF 0.10.2 中唯一对应的算法名。本实验同时准备 DPO 与 RLOO。若你看到的 RPO 来自某篇特定论文，
  需要先用论文标题和公式确认身份，不能仅凭缩写把它并入现有 stage。

因此实验链不是一条“新算法依次替代旧算法”的直线：

```text
Base
  -> SFT
      -> Reward Model -> PPO
      -> DPO
      -> verifier -> RLOO
      -> verifier -> GRPO
```

PPO 使用 actor、critic、reward、reference 和 rollout state；RLOO/GRPO 不训练 critic，但要求同一 prompt 产生多个
samples，并对组内 reward 构造不同 baseline。它们在 Runtime 成本上不是同一种 Job。

## 固定实验问题

模型接收整数算术题，并被要求只输出：

```json
{"answer": 42}
```

这个任务故意简单，因为 exact correctness、格式、OOD transfer 和 reward hacking 都能自动核验。训练 reward 与最终
evaluation 分开调用：训练器可以消费 reward，但是否真正答对由 held-out evaluator 决定。

数据由固定 seed `3407` 生成：

| Dataset | Rows | Owner |
| --- | ---: | --- |
| `sft_train.jsonl` / `sft_valid.jsonl` | 120 / 30 | demonstration |
| `preference_train.jsonl` / `preference_valid.jsonl` | 120 / 30 | chosen/rejected pair |
| `prompts_train.jsonl` / `prompts_valid.jsonl` | 120 / 30 | online rollout prompt + label |
| `evaluation.jsonl` | 66 | independent in-distribution and OOD evaluation |

## Profile 不是性能承诺

| Profile | Model default | GPU | Purpose |
| --- | --- | ---: | --- |
| `smoke-1xl20` | `Qwen/Qwen3-0.6B` | 1 | 先验证完整数据、checkpoint 和 rollout 控制流 |
| `standard-2xl20` | `Qwen/Qwen3-8B` | 2 | 进行主要算法学习对比 |
| `full-4xl20` | `Qwen/Qwen3-8B` | 4 | 展开 PPO 多角色状态与较大 rollout group |
| `scale-27b-4xl20` | 必须显式设置 | 4 | 8B 证据链完成后的可选规模实验，默认禁用 |

这些参数是保守起点，不表示一定达到某个吞吐或显存水位。`configs/profiles.json` 是 GPU、batch、length 与 model 的
机器事实源；调整后必须把实际值写入 run report。

27B 实验需要 Hugging Face trainable checkpoint，例如包含 `config.json`、tokenizer 与 Safetensors shards 的目录。
GGUF 是推理 artifact，运行器会拒绝 `.gguf`，不能把本地 27B GGUF 直接当训练 checkpoint。

## 目录与身份

```text
configs/profiles.json       model/hardware/workload profiles
configs/stages.json         stage inputs, outputs and OpenRLHF flags
data/                       deterministic fixtures
scripts/build_dataset.py    dataset generator
scripts/reward_func.py      OpenRLHF reward contract
scripts/run_stage.py        config -> command -> optional execution
scripts/generate_outputs.py independent vLLM evaluation generation
scripts/evaluate_outputs.py held-out verifier
scripts/render_job.py       profile -> Kubernetes Job JSON
jobs/profiles.json          CPU/memory/GPU resource requests
reports/                    report template and run receipts
```

默认 artifact lineage：

```text
artifacts/sft
artifacts/reward
artifacts/dpo
artifacts/ppo
artifacts/rloo
artifacts/grpo
```

每条完整实验链应把 `artifacts/` 指向持久存储中的独立 lineage ID；同一链中的 SFT、Reward、PPO 等 stage 共享这个
root 才能消费上游 artifact，不同实验链不能共用可写目录。每次重试再在报告和 checkpoint metadata 中记录 attempt ID。

## 0. 本地材料校验

这一步不需要 GPU，也不安装 OpenRLHF：

```bash
cd labs/08-post-training-branches/l20-rl-suite
python3 scripts/build_dataset.py
python3 scripts/validate_suite.py
python3 -m unittest discover -s tests -v
python3 scripts/run_stage.py --stage grpo --profile smoke-1xl20
```

最后一条只渲染命令，不执行。生成的 receipt 状态固定为 `Not Run`，避免把“配置可解析”误报成“实验完成”。
带 `--execute` 时运行器会自动写入 `artifacts/receipts/<stage>.json`。即使命令返回 0，状态也只是
`Process Exited 0`，Experiment Gate 仍为 `Pending Checkpoint Reload and Held-out Evaluation`；进程成功不等于实验验收。

## 1. 准备 L20 环境

推荐在 NVIDIA PyTorch container 内安装固定版本，CUDA/PyTorch 由基础镜像提供：

```bash
python3 -m pip install -r requirements-l20.txt
python3 scripts/validate_suite.py
python3 scripts/capture_environment.py --output reports/<RUN_ID>-environment.json
```

开始前核验：

```bash
nvidia-smi
nvidia-smi topo -m
python3 -c 'import openrlhf; print(openrlhf.__version__)'
python3 -c 'import torch; print(torch.cuda.is_available(), torch.cuda.device_count())'
```

容器、driver、GPU topology、OpenRLHF、vLLM、DeepSpeed 和 Git dirty state 都属于结果身份，不得只记录“4 张 L20”。

## 2. 先保存 Base Baseline

```bash
python3 scripts/generate_outputs.py \
  --model Qwen/Qwen3-0.6B \
  --output outputs/base.jsonl

python3 scripts/evaluate_outputs.py \
  --outputs outputs/base.jsonl \
  --report reports/base-evaluation.json
```

后续 checkpoint 使用完全相同的 `evaluation.jsonl`、seed、temperature 和 output budget。不能在看到结果后替某个算法更换
有利的 prompt 或 evaluator。

## 3. 跑通 0.6B 完整链

Offline stages 由 DeepSpeed 直接启动：

```bash
python3 scripts/run_stage.py --stage sft --profile smoke-1xl20 --execute
python3 scripts/run_stage.py --stage reward --profile smoke-1xl20 --execute
python3 scripts/run_stage.py --stage dpo --profile smoke-1xl20 --execute
```

Online stages 需要 Ray head。以下只是单机 smoke 路径；同一条 SFT -> Reward -> PPO lineage 应共享 artifact root：

```bash
ray start --head --node-ip-address=0.0.0.0 --num-gpus=1
export RAY_ADDRESS=http://127.0.0.1:8265

python3 scripts/run_stage.py --stage ppo --profile smoke-1xl20 --execute
python3 scripts/run_stage.py --stage rloo --profile smoke-1xl20 --execute
python3 scripts/run_stage.py --stage grpo --profile smoke-1xl20 --execute

ray stop --force
```

不要并行执行上面三个命令，它们默认共享 GPU 与 artifact root。完成每个 stage 后先验证 checkpoint reload 和 held-out
evaluation，再进入下一条分支。

## 4. 扩展到 8B

0.6B 的完成条件是控制流正确，不是结果足够好。只有以下 Gate 全部通过后，才切换到 `standard-2xl20` 或
`full-4xl20`：

- 数据与 split identity 已冻结；
- base 与 SFT checkpoint 能独立 reload；
- RM 对 held-out chosen/rejected 的排序优于随机，并记录 calibration；
- online run 没有 NaN/Inf，reward、KL、entropy、length 和 policy revision 可观测；
- evaluator 能发现 reward 提升但 exact accuracy 不提升的反例；
- checkpoint 中 actor、critic、optimizer、reference 和 sampler state 的保存边界已记录。

8B 运行只换 profile，不换 task：

```bash
python3 scripts/run_stage.py --stage sft --profile standard-2xl20
python3 scripts/run_stage.py --stage grpo --profile standard-2xl20
python3 scripts/run_stage.py --stage ppo --profile full-4xl20
```

先检查渲染命令和内存预算，再增加 `--execute`。模型路径可用 `MODEL_ID=/models/trainable-checkpoint` 覆盖。

## 5. Kubernetes Job

Job renderer 输出 Kubernetes 接受的 JSON manifest。PVC 必须包含本仓库和持久 artifact 路径；image 必须已经安装
`requirements-l20.txt`：

```bash
python3 scripts/render_job.py \
  --stage grpo \
  --profile full-4xl20 \
  --image <company-registry>/openrlhf:0.10.2 \
  --pvc <workspace-pvc> \
  --run-id 2026-09-01-grpo-8b-seed3407 \
  --namespace <namespace> \
  --output generated-jobs/grpo-full-4xl20.json

kubectl apply -f generated-jobs/grpo-full-4xl20.json
```

这是单 Pod、单节点多 GPU 的最小 Job。生产 Runtime 还要补 admission、queue、node placement、gang semantics、artifact
promotion、resume policy、credential injection、log/metric collection 和 cancellation；这些不能隐藏在训练脚本内部。
Ray runtime environment 只分发代码和小数据，显式排除 `artifacts/`、`outputs/` 与 `reports/`；多节点 worker 必须以相同
绝对路径挂载持久存储，不能依赖 Ray 上传 checkpoint。

## 6. 必做故障实验

1. 翻转一部分 preference pair，观察 RM/DPO train objective 与 held-out exact 是否分离。
2. 以 `REWARD_MODE=shortcut` 启动 RLOO/GRPO，让包含 `verified` 的错误答案获得高 reward，验证独立 evaluator 能拒绝它。
3. 将 samples per prompt 从 8 降到 2，比较 RLOO/GRPO advantage 的零方差组、variance 和 sample efficiency。
4. 保留旧 rollout 后更新 actor，验证 Runtime 是否记录 rollout policy revision，并观察 KL/off-policy signal。
5. 单独报告 `division_ood`、`negative_ood` 和 `compositional_ood`，不要用总体平均值掩盖分布外退化。

故障实验必须写入新的配置/receipt 和报告，不直接修改 canonical dataset 后覆盖原结果。

## 7. Runtime 最小接口

一个可复用 RL Job 不能只有 `command`，至少要显式管理：

```text
spec:
  algorithm + execution mode
  actor / critic / reward / reference identity
  dataset / prompt / label / verifier identity
  rollout and update budgets
  GPU topology and colocation policy
  checkpoint, resume and artifact promotion policy
status:
  admitted -> preparing -> rolling_out -> updating -> evaluating
  -> checkpointing -> completed | failed | cancelled
```

关键状态 owner：

| State | SFT | DPO | PPO | RLOO / GRPO |
| --- | --- | --- | --- | --- |
| Demonstration / pair / trajectory | demonstration | pair | trajectory | grouped trajectory |
| Reference policy | no | yes | yes | yes when KL enabled |
| Critic | no | no | yes | no |
| Reward model | no | implicit preference | yes | verifier/custom reward |
| Rollout engine | no | no | yes | yes |
| Policy revision attached to rollout | no | no | required | required |

Job controller 应该验证这些契约并生成 framework args，而不是要求模型开发者理解 Ray placement、DeepSpeed state 与
checkpoint 目录细节。

## Evidence Boundary

本目录目前证明的是：数据、reward、配置渲染和 Job manifest 可以在无 GPU 环境进行结构校验。它尚未证明 OpenRLHF
在公司的具体 container、driver、网络、PVC 和 L20 topology 上成功运行，也没有证明任何算法提升模型质量。完成定义
遵循 [Lab Contract](../../LAB_CONTRACT.md)，GPU 实验只有在 correctness、controlled comparison、failure boundary 和
report 都齐全后才能从 E0 提升。

## Source Boundary

- [OpenRLHF 0.10.2 Quick Start](https://openrlhf.readthedocs.io/en/latest/quick_start.html)
- [OpenRLHF SFT / RM / DPO](https://openrlhf.readthedocs.io/en/latest/non_rl.html)
- [OpenRLHF RL Training Guide](https://openrlhf.readthedocs.io/en/latest/agent_training.html)
- [NVIDIA L20 product brief](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/l20/PB-11773-001_v01.pdf)

框架 flag 绑定 OpenRLHF `0.10.2`。升级版本前必须重新核验 `configs/stages.json`，不能假设旧参数仍能解析。
