# 2603.09046 — FlexServe必要Source与Ch72窄差额（Source/PRE/actualPOST通过）

[FlexServe exact-v1](https://arxiv.org/html/2603.09046v1)，题名FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation。第二包root完整AB准入已通过。作者实际必要§3/4/5/6/7/8/9全部HTML文字及Table1，不授全部图像、代码或实现复现；本次准备后重新完整读§3/4/7。方法、安全边界与直接性能反侧已足够，停止无关附件。

## 身份、日期与采用信号

SUP_EXACT_BATCH2.json原v1 Mar10UTC00:31:25提交，official no-advance finalID/DOI及deadline给arxiv最早公开下界Mar11BJT08；owning arxiv.content/findable DOI registeredMar11UTC02:04:09给已经可发现上界，同属03-11BJT，夹证日而不是把Submitted/Updated/registered单独作公开。现v3 July1窗外，题摘与v1一致、comment13页11图，当前未见accepted/重要纠错信号；不因v2/v3编号扩审或倒填。具体原字段待root独立核。

必要Books去重发现Ch56旧note1698引[2606.23370](https://arxiv.org/abs/2606.23370)，官方当前页L8/23/31–32实际为v2 withdrawn，comment明确重复上传错误并指回2603.09046。这是同一家族误重上传，不是更早首公开、独立采用证据或新事件。旧Ch56仅通用notes未承载本次采用的具体隔离机制；不能拿未有效的June note证明已有覆盖。本任务仅向root报告需定点修复的June身份/依赖，不写其他日报或共享Ch56，也不凭误上传把March有效v1清退。

评分2+2+2=6：固定TrustZone连续区面临GB级碎片/设备切换→stage2/SMMU保护普通物理页并分开管理权/访问权→安全资源交接与明文边界的重要替代分支；跨CPU/DMA/NPU边界，稳定的权属交接约束。成熟paging/LRU/流水线本身不加创新分；安全约束和Ch72具体gap触发受影响内容深入。

## 核心机制与前提

§3.2假设初始kernel代码良性且secure boot保护，随后kernel可被攻陷；secure-world组件和Flex-Monitor可信。normal-world client本身不受保护，侧信道/物理/DoS在范围外。§4.1 FlexMem仍是TrustZone normal物理内存，但EL2 monitor从normal-world stage2删IPA→PA；secure OS给TA映射。DMA亦从其他设备SMMU表移除，stage2拦SMMU基址MMIO并隔离表页，授权NPU仅可触FlexMem，不能认为CPU页表保护单独覆盖DMA。

§4.2 daemon不可信，只协调mmap/pin和请求；框架选择释放、clear后monitor重映射。lazy reclaim允许不立即清，但page仍不在normal stage2，reuse时monitor负责overwrite/remap，即使kernel不改也保证清。freelist登记不等已经把残留秘密交给kernel；具体TLBI/drain/错误中断/物理别名状态机本轮未核，不补造实现。§4.3 NPU独占protected模式，MMIO对kernel撤销；复用driver代码/数据进入额外S2sandbox，NPU DMA限制FlexMem。作者以task launch stateless断言残余driver状态不影响；本轮没有独立reset/state-sanitize或攻击测试证据，不能由该句证明任意驱动残余安全。

§4.4仅FlexMem和FlexNPU均完全释放才关stage2；secure EL3给EL2代码/数据包括S2表hash后freeze，恢复S2再验证。EL2无秘密，只核完整性。§5.1四阶段allocate/load/decrypt/compute：密文DMA先入unprotected页，load完保护后才在secure-world解密，和下一层流水重叠；密文完整性/具体model binding实现未核，不由加密直接认证任意权重。§5.2–3 layer-prefix cache、LRU coldKV加密flash、已知workflow prefetch是成熟原语；zero-stall line条件依赖target prompt distribution，不是未知工作负载最优律。§5.4 vendor-signed TA/secure boot、secure session、prompt+modelindex加密与response/request hash签名；TEE标准接口名称不自动证明全实现安全，normal client被攻陷可在验证后改结果，响应证明不认证答案质量。

## 评价、费用与直接反侧

§6/7 NanoPC-T6开发板RK3588，16GB、8CPU、6TOPS NPU，Linux6.1.57/OPTEE4.5。monitor约4.5KLOC、TA3.3KLOC，closed vendor runtime无法接入，使用community逆向INT8 GEMM/CPU反量化，并加blocking/coherence/CPU-NPU流水/Neon；总体收益不能全归纯资源隔离。不是商用手机或所有NPU已验证。

三对照：NWBase普通世界不保护且NPU/流水；Strawman TrustZoneCPU+CMA；StrawmanOPT secureNPU+流水+CMA。默认stress-ng驻留8GB而特意避免CPU/带宽争用，不能外推任意后台负载。Table1 8GBalloc568.58 vs6440.67ms；reclaim80.50 vs732.85ms（算术约9.1×，正文12.6×冲突保留，不采精确回收倍率）。NPU模式0.21ms不含SMMU8GB435.48ms或算子；task launch1.28ms不含compute；S2boot0.13/hash2.83ms；8GBload3265.34/decrypt1319.16ms均真实费用。

§7.3 coldcache-off INT8 Llama3.2-3B/Llama3.1-8B/Qwen3-1.7B/8B，正文TTFT平均7.15×/1.85×而abstract10.05×/2.44×不一致，不合成一个精确总体倍率；对NWBase仍4.41%TTFT/3.01%decode平均损失。prompt128、0～10GB压力，0GB时NPU基线相近，10GB时8B仍disk swap/TTFT升，非压力免疫。§7.4多model随机requests/4GBcache与single cold是不同population；所谓agent response latency只包含首模型完整生成+次模型TTFT，不含第二模型全输出或任务完成，不采用完整agent端到端倍速。

§7.5 prompt128 prefetch配置够放全模型，不能当4GB同cache matched控制。§7.6 SQLite3GBdataset/1GBsubset、固定不同CPU、后台8GB，FlexServe仍最高1.31×延迟；SPEC active虚拟化平均2.46%，ondemand OFF不免active负担。硬件主配置、INT8与部分input切片已披露；完整输出长度、batch/concurrency/tailSLO、run/seed/CI、thermal/energy、独立attack audit、质量一致性和完整firmware/device trustchain Not Disclosed。不读图估造所有points。

§8是作者安全论证，不是攻击bench或形式完备证明；§9 pVM overhead论述非matched pVM系统测量，GPU/MoE/更快NPU仅未来可能性。独立硬件边界继续适用，不能用fragmented页性能换掉原threat model。

## 已读owner与逐字PRE提案

唯一owner `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。实际读170–202完整局部及章节开篇、Ch71/73开篇交接；现173 Weight Streaming段解释可信on-die ingress/AESCTR/SMMU/scrub明文边界，不承载secureOS/monitor对normal物理碎片页的动态权属交接。1180–1207响应完整性局部已读，不复写通用response proofs。Ch56仅June旧notes不足以NC，June误上传待root单独修复。拟在SF-2604-23205 sourcebinding末后、“一旦threat model已允许取得明文权重”前两段，不覆盖片上原分支。

可信片上 ingress 与动态可信执行是不同分支。固定 TrustZone 连续区对密钥等小状态简单合理，但当推理需要借用数 GB 碎片页时，内存管理权不必与明文访问权一起交给普通 OS：可信 monitor 可用 stage-2 撤销 kernel 对选中页的映射，并同步限制其他设备的 SMMU；secure-world 框架才把这些页映射为权重、KV 与临时状态。密文可以先由普通世界加载，页保护完成后才解密；释放或延迟清理也必须保证旧明文在恢复普通访问前已覆盖，不能让“已归还 freelist”成为访问授权。NPU 独占保护模式还须撤销 kernel 的 MMIO、隔离复用驱动并限制 DMA 目的地，不能从 CPU 页隔离直接推出设备隔离。[必要机制](https://arxiv.org/html/2603.09046v1#S4)。<!-- source-family:SF-2026-ARXIV-2603-09046 -->

这种分离用 monitor、驱动交接、映射与清理费用换取页级弹性；全部受保护资源释放后才能暂停保护，并由更高可信层保存、恢复验核 monitor 的完整性，不是敏感任务活动时免费关掉虚拟化。[有限开发板对照](https://arxiv.org/html/2603.09046v1#S7)中，碎片页分配避免了 CMA 大区合并，但内存压力仍可触发换盘，设备映射、解密与后台开销也仍存在；它不认证任意手机、驱动残余状态、物理/侧信道防御或完整 agent 任务延迟。普通世界 client 仍可能在验证后泄漏或改写输出，可信推理不替代可信 I/O 边界。交接、驱动信任或清理前提不能验证时，应保留目标威胁下已核验的静态 TEE、适用的独立硬件/隔离边界或拒绝敏感请求，而不是回到可被同一 compromised kernel 读取的明文 host 执行。<!-- source-family:SF-2026-ARXIV-2603-09046 -->

拟本人末注：SF-2026-ARXIV-2603-09046；Daily2026-03-12补查，v1§3–9文字/Table1，2+2+2=6；stage2/SMMU与管理权/访问权分离的安全gap深入，lazy-reclaim保护与NPU sandbox交接近正文。初始良性/secureboot、normal-client/physical/sidechannel/DoS边界保留；RK3588开发板INT8、CMA对照与时间分账，不采用conflicting reclaim/总体TTFT倍率或完整agent完成延迟。June2606.23370官方误重上传撤回指回March，不作独立采用；root待核必要日期/Source/逐字PRE及写后POST，不授实现、复现或DAY。

## 实际落地与POST（更新上面原提案的待核状态）

root实际必要§3.2/4–5.1/6/7（Table1、有限负载与压力/正常世界费用）/8/9、原日期夹证字段、Ch72 165–205及71/73交接PRE通过，root实际写Ch72新191/193两段及本人4399末注，并只定点将Ch56 1698撤回June旧note纠正为官方误上传和canonical handoff。非writer supplement_20260312实际顺读Ch72 171–211完整邻接、新段及自身末注，回对上述必要原证；实读Ch56 1689–1706完整notes邻接、1698链接及actual Ch72标题anchor，POST通过。动态隔离不替代可信on-die、normalclient/driver/物理负侧和成本不删；June不作为有效独立采用，未移动任何Daily日期或候选。本人末注已请求root同步actualPOST状态，未stage/commit/push，不授DAY/实现/复现。
