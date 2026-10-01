# 04/29 三项独立 source→owner 复核

复核者：root（非04/29作者）；2026-09-30。仅24819、24921、24952，不重开已经有效的其他审阅，不签整日日级Gate。

本轮实际重新打开三篇 exact-v1 的必要方法，并对照当前 Ch27 Failure-driven Curriculum / Typed Lineage、Ch26 VLA动作表示 / 异步控制、Ch34 Probability-geometry Gate 的正文与交接。原作者必要评价与反证逐项核对；这不是从旧Complete标签继承结论。

- [24819 ProDa](https://arxiv.org/html/2604.24819v1)：§4.1–4.3共同节点身份支持具名修补提案；Eq5输入分流不证明生成实例不重合，LLM错误分类不证明因果诊断。现有Ch27有失败驱动和一般lineage，却没有共同知识层级同时帮助定位并引入共源/适应性污染的明确分支。批准采用包页首两段，唯一owner `TRAIN-DATA`；保留外部能力回退与独立holdout，不采用无污染、全能力保持等强保证。评分3+2+2=7，深入审阅。
- [24921 Libra-VLA](https://arxiv.org/html/2604.24921v1)：§3.1–3.4的粗离散动作串行条件化连续refiner，不是平行完整动作平均。现有Ch26二择表示与异步队列不能替代这段coupling；批准两段进入 `MULTIMODAL-EMBODIED-VLA`。训练teacher→预测切换、FIFO stale intent、平均延迟与成功率共同变化和监督真机边界必须保留。2+2+2=6；已确认知识缺口，定点深入，不外推学习难度均衡或开放安全。
- [24952 Semi-DPO](https://arxiv.org/html/2604.24952v1)：§3.3时间段margin符号改变标签身份，和Ch34仅调gradient幅度的gate确实不同。批准采用包两段进入 `TRAIN-DPO`；保clean anchors、proxy共识不等人类真值、阈值调整不等独立校准。Appendix6.2方差分账不证明次优收敛，晚段信号与迭代成本的反证仍有效。2+1+2=5；已确认缺口，定点深入，非通用偏好恢复保证。

## 实际写后

三处均已真实存在，root再次顺读前后正文：Ch27在HardGen的failure→curriculum之后、Terminal完整环境身份之前；Ch26在离散/连续瓶颈比较之后、物理接口之前；Ch34在只调梯度的gate之后、训练loop复杂度之前。上述source marker及原始链接实际位于机制正文，非只在Review notes。

三项写后通过：既有论证、例子与证据保留，没有把共享图冒称独立验收、粗意图当安全授权或margin当真值。Ch34后文“无需显式Reward Model training/serving”指fine-tuning loop，并不否认此前proxy筛选成本。三处只授窄段，均已释放；日期、最终63候选、其他普通待办及日级验收仍由本日流程独立完成。
