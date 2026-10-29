# NVSHMEM 2606.05951v1 必要缺层/actual owner/最小PRE

作者supp_20260606_author，2026-10-25。[exact-v1](https://arxiv.org/html/2606.05951v1)，A6/R4完整题摘/准入/日期层直接复用。原Jun05候选 `3+3+3=9` 保持，不把旧评分当本次贡献已证/另提分；所需投入为深入必要域。旧trace/完成标签不授采用。未扩大旧日材料池或搬旧归属。

## 旧有效Source与首次必要缺层

已具名读Jun05 V2_archive仅本ID Source：对称内存/registration/remoteaddress/proxyIBGDA/ordering/collective定位和H200硬件摘要有效，复用。未把其中泛泛“改变ownership”替代具体证据；给出的artifact DOI是出版引用而非核过运行实现，不能承诺已核artifact。当前Ch36只有daily-books-trace语义一行，不是已写机制/真实POST的证明；本次补actualowner而不在旧trace改日期。

实际补读exactv1 III-B/IV–VII/VIII/IX–X必要域及直接反侧：heap VA预留与physical commit分离，远程offset加对端base保持object映射，P2P可直解地址；非P2P仍用注册handle与transport，GPU API发起不等CPU-free，IBGDA存在则GPU post NIC，否则描述符交host proxy。`fence`只序同目的PE操作、`quiet`完成/可见，`sync`与包含completion的`barrier`不同，不把发起、通知和consumer可读合一。

VI-D一个device collective只由thread/warp/block threadgroup完成；同team共享pSync，不能据多个CTA发起同team就自动获得多CTA并行。本文版本on_stream多CTA限指定collective和NVLS可用路径，创建duplicate teams分离同步state；deviceRMA和built-incollective不互代。VI-B LL128链路/原子保证与bufferfee有条件，不将所有128byte store当跨PCIe保障；本次只采用scope分责，不移植完整protocolrecipe。

VII明确仅selected microbench非全面评估：CoreWeave H200SXM5/每node8卡144GB、NVLink4/NVLS与8ConnectX7；CUDA13.0.88/NVSHMEM3.3.9，RMA perftest32CTA×256thread，remote scalar另调RC/CTA/thread；collective float sum/CUDAGraphs，8trial，NCCL-tests。模型/输入输出token/batch在微基准不适用，message/参与PE/launchscope才是条件；并发业务与训练step/SLO未验。VII-B bulkput/get/scalar有不同依赖，不能从RMA接近单rail推AllReduce；VII-C inter-node collective反侧含timeout缺测、device单CTA与on_stream/NVLS比较同时改scope/资源，故不归给库名优劣。少数microplot未看像素，不采用精确吞吐/latencycurve或普遍排行榜，未运行复现。

VIII DeepEP只v1：HT按localindex跨节点/节点内转发，8P2P卡假设；LL按expert分工，same-node也可能直copy，metadata/payload/counternotification不是一份完成语义。只在关键RDMA点借NVSHMEM，不称整个DeepEP由NVSHMEMcollective实现。VIII-C性能为转述GINpaper而非作者新增rerun，不作为本日独立性能证据；不为这段转述追原benchmark，因为拟采命题不依赖1–2%结果。全部heap/registration、proxy或NICqueue、pSync/teamduplicates、polling、launch与完整step回归收费；版本/transport/作用域改变需重验。支持与直接反侧足以限定这次小gap，未要求全API或代码复现。

## actual owner与原两段PRE（首次待独核）

实际读Ch36开篇/通信分层完整节、下节成本模型及相关device-kernel交接，Ch35/37开篇。唯一 `TRAIN-DISTRIBUTED-TRAINING` Ch36承载通信公共语义。既有semantic/algorithm/runtime/transport/topology分层说明责任却没有“GPUinitiated与CPUproxy、scope/team同步资源”具体分离；marker一行非已有覆盖，不将这项称新runtime。

拟在分层节“这不是一条所有系统都必须逐层经过的固定协议栈。…重要的是在性能或故障分析时不混淆责任。”完整段之后、紧接的“例如，‘AllReduce 很慢’至少可能表示：”及其完整诊断代码块之前插以下两段；不是跨过中间诊断段插到下H2。后续由rootfresh确认此两锚，不改其他body/注。

通信由GPU代码发起，也不意味着进度完全由GPU独占：对称内存接口可以用对象在heap中的offset定位对端，但是否能直接访问仍取决于peer映射与transport。一个[受限实现分析](https://arxiv.org/html/2606.05951v1#S5)中，非直接映射的操作可能由GPU向NIC提交，也可能只写入描述符，再由host proxy推进；API的发起位置、真实执行路径和完成可见性须分别记录。发起成功或通知到达不等consumer已能读取全部结果，ordering与completion/visibility也不能互换。

调用作用域还会改变可用并行度与同步状态：device侧单threadgroup collective，不能靠多CTA同时使用同team自动升级为安全的多CTAcollective；特定on-stream路径用duplicate teams分开pSync资源，又依赖可用拓扑与算法支持。RMA、节点内collective与跨节点collective因此必须分别比较，不能从一个microbenchmark批准另一类通信或完整训练step。Heap/注册、queue或proxy、team同步资源、polling和launch都计费；版本、作用域或完成条件无法验证时，保留原host-launched collective、串行化合法team调用与显式完成检查，不以“device-initiated”替代正确性或全局性能验收。<!-- source-family:SF-2026-ARXIV-2606-05951 -->

本人注拟：`SF-2026-ARXIV-2606-05951` — supp_20260606_author，Daily2026-06-06补Jun05；exact-v1 III-B/IV–X必要/直接反侧，保原3+3+3=9/唯一Ch36。只GPU发起/进度与scope/team同步状态分责，旧有效机制/硬件摘要复用，不由旧trace授I。保version/transport、inter-node反侧/timeout、RMA非collective和完整费用；GIN转述非本日rerun，不授性能/收敛或SLO。未看全图像素/核代码/硬件复现；首次必要/PRE/root新窄授/实际SAVE/唯一POST按后到事实记，不预I/DAY。
