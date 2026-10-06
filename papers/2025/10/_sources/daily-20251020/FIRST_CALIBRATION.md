# 2025-10-20 首批准入校准请求

作者窗口：2025-10-19T09:00:00+08:00 ～ 2025-10-20T09:00:00+08:00。
未收到独立校准，以下不授正面 Evidence、评分或 Books 采用权限。

## 潜在贡献

- [Celeris / Reimagining RDMA Through the Lens of ML](https://arxiv.org/abs/2510.16606v1)：可靠且有序 RDMA 是默认前提 → 将重传/有序保证移出 NIC、让训练管线处理丢失 → 是否可在特定训练容错与尾延迟约束下放宽传输契约。摘要中的 2.3x/67% 不作为验证结论。
- [MeCeFO](https://arxiv.org/abs/2510.16415v1)：邻居接管失败节点会增加内存/算力 → 丢弃 MHA 反向、重计算 FFN、低秩梯度近似 → 接管策略应否改变训练更新语义，而非仅重启/弹性缩容。不能把摘要收敛率外推到任意训练。
- [More with Less](https://arxiv.org/abs/2510.16786v1)：固定回合上限约束所有任务 → 按需申请延期的动态策略 → 是否应采用任务依赖的推理预算；初查API为v2，root FIRST已实际核精确v1完整题摘，first-public仍未确认，不能继续称v1未核。
- [Visual Autoregressive Models Beat Diffusion Models on Inference Time Scaling](https://arxiv.org/abs/2510.16751v1)：连续采样搜索难做早剪枝/复用 → 离散逐序列搜索与 verifier 比较 → 生成范式是否改变搜索效率；不是依据2B/12B单个数字收录。初查API为v2，root FIRST已curl恢复ROOT-2510.16751v1.html并核完整题摘/历史，first-public仍hold。
- [Facts in Stats](https://arxiv.org/abs/2510.16096v1)：更多改写常被笼统视为改善事实泛化 → 控制语境结构、多样性和训练时长的合成实验 → 区分事实召回与统计泛化及优化瓶颈。小模型/合成实验不自动排除。
- [CodeCRDT](https://arxiv.org/abs/2510.18893v1)：并行输出合并与语义一致性容易混淆 → CRDT 零合并失败同时仍有语义冲突及任务相关减速 → 是否需要分别评价文本收敛和任务正确性。负面结果不排除。

以上身份由本日独立主题查询取得，`published` 原值实际为提交字段，不证明首次公开；日名相交、月列表身份和后来的注册日期均不足以准入本窗。

## 分层排除样本

- BRAINCELL-AID 2510.17064：生物细胞注释，AI for Science 暂缓，不能借 RAG 通用 owner 重新纳入。
- Guide-RAG 2510.15782：Long COVID 临床问答数据选择，非当前主线知识增量。
- Attn-JGNN 2510.15583：#SAT 专用 join-graph 网络，题摘没有服务大模型机制链。
- BPL 2510.16076：推荐偏差校正，题摘没有改变模型形成或 LLM 系统的具体判断。
- Beyond Pipelines 2510.16720：综述分类与趋势，本题摘未显示新的设计反证或机制边界。
- TDD spreadsheet framework 2510.15585：明确为待实验的 position framework，不能把成熟 test-first 原则计入新增贡献。

必要安全/反侧线索：ATA 2510.16381 的 prompt-injection immunity、DistilLock 2510.16716 的 TEE/不可信加速器边界、fine-tuning auditing 2510.16255、attention-sink backdoor 2510.17021、SentinelNet 2510.16219。它们不能仅以摘要指标或日期不明写成已审排除。

## 复核请求

请独立核首批全部潜力及上述代表性排除项、当前题摘与历史版本权限、查询是否过宽，以及日期隔离是否保留必要的安全反侧工作。作者不填通过。
