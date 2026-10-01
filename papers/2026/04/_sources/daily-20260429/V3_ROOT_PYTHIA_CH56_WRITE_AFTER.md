# Pythia Ch56 实际写后非作者复核

- 复核者：root；写入者：apr20_resume。范围只含 [arXiv exact-v1](https://arxiv.org/html/2604.25899v1) §4.1–4.2、§5、§7，`books/part-05-inference-system/56-inference-scheduling.md` 的 Infrastructure-aware Multi-Agent 前后及后文 Workflow Critical Path/ProgramState。不是 04/29 整日独立 Gate。
- 通过：新增正文从“共享当前负载仍看不到 workflow identity”自然引出三种轻量身份→Serving 自有 profiler→共享预测供 cache、priority、capacity 提案；runtime/cache/scheduler 仍验证真实资源并拥有最终提交，未让 Agent 自封资源权限。后文已有联合 critical-path 状态，没有再复制 Pythia 的算法清单。
- 事实边界通过：冷启动、路径漂移、不受控流程仍回 reactive；历史经验分位数不能单独保证未来边际尾概率，因而不采用论文“distribution-free strict”总保证。证据只称真实轨迹映射到单机八张 A100 的受限试验，不称原生产系统已验收。`forecast` 的有效期是工程推断，不冒充作者已实现功能；已在正文改成“工程上还应”。
- 结果：本家族 Ch56 的实际 Books 增量写后通过；04/29 候选总分母、来源与其他家族仍在审阅，不能把这次通过等同日报 Complete。
