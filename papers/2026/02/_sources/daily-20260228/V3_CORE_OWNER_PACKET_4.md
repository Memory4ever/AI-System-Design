# 第四包：必要反侧与实际owner差额

仅列已读的必要精确v1方法、对照和直接限制，不要求全proof/artifact。日期原abs于DATE_BATCH2抓取，同ID registered与官方公开下界形成完全本窗的范围，注册时刻不是精确首公开。以下待root actual PRE，不先写Books。

## 22426 SimpleOCR，2+1+3=6，具体差额需深入

原§4/blocks29–43：从text channel去掉question，完整原图下方新增canvas渲染问题，随机font/CJK/color/18–42pt；standalone训练全VQ、标准C_orig测试。HybridNoisyRollout不是相同更新协议：half rollout VQ但原C_orig更新。§5/blocks46–79：8.5K数据，greedy，MathVerify/GPT4o分任务；7B Geo3K43.4低于GRPO44.3，OOD52.6对51.2仅局部。随机渲染对照支持格式泛化，50%混合可更弱，振荡的具体原因仅作者假说；与其他RL方法30×数据非等总代价。§Limitations/87：依赖已有latent OCR，长问题受resolution限制，不能称创造通用视觉能力或总是消除text shortcut。

Actual Ch23 460–472已读：text-as-image现有目的是token压缩、原文authority及OLM训练可见性，未承载**已有OCR可读≠任务实际使用的训练elicitation分支**；Ch27 773–804 packing/lineage承载输入协议身份，不重复该训练算法。请求Ch23 text-as-image/OLM附近一段+自身note：渲染是增加视觉读取必要性而非压缩收益，standalone训练/标准测试与hybrid分开，原图canvas、OCR/resolution/负切片/额外RL费用及原text回退同段。

## 22427 HubScan，2+1+2=5，具体alert预算差额需深入

原§3–4/blocks49–90：写index与query/encoder知情攻击、50%随机doc+50%cluster query，10K扫描query/k20，MAD等scores不是恶意truth。§4/112–123及§5/141–186：15 benign universal hubs+10 domain adversarial hubs，global top-K=H预算recall0，但global ROC-AUC .995，故不是“统计不可见”；自然universal hub占掉有限alert预算。domain查询可恢复，依赖代表性范围/人口；攻击污染>5%可退，1M MSMarco扫描不是实测线上对抗部署，adaptive attacker未验证。

Actual Ch76 335–345已读任意embedding写入/自然hub非恶意，1067–1090已有tight-domain监测与写路径quarantine。具体缺口是**global ranking很好仍被自然hub抢占有限告警预算**，不以“需要domain监测”主题造gap。请求Ch76 hub几何负侧附近一段+自身note，保alert-budget/scoped query条件与误报、攻击权限/漂移和provenance处置，不能由scan score直接删文档。

## 22441 Latent supervision，3+1+3=7，深入完成提案

原§2 blocks26–32分outcome/end-latent与fine-grained监督；§4/43–67 GPT2 fullft/Llama3.2-1B LoRA，两合成/增强任务，终止latent后的最后embedding Gaussian σ100扰动，latent仍部分正确而explicit CoT几乎0。只扰动最后embedding，不删除所有早latent/KV，单例attention也非唯一因果，因此采**答对不足以认证实际消费中间latent**，不采全latent无用。§5/73–100 early-stage混合训练纠偏但训练recipe/budget并未完全单因素隔离；100次temp1 hybrid与deterministic text prefix有差异，latent Pass@100高而Maj@100低，diversity不授BFS或可交付正确性。不同方法表格不因果分离监督强度；Table4 greedy34.09与paragraph78 41.06不一致，不采用这一精确收益数字。

Actual Ch8 290–315已读convergence≠verification、latent-width proposal与selector分责，但缺**终点正确/latent长度不能证明中间状态被消费，干预保留KV的证据权限**。请求Ch8 latent-width后、emergence前一段+自身note：监督/计算路径分别验，末state perturbation有限反证、早stage训练代价与探索/多数反侧，显式CoT/固定预算/工具验证回退。Ch66不重复latent认知机制。

## 22450 SilentEgress，2+2+3=7，采用网络effect范围，争议数值隔离

原§4/59–64本地Ollama qwen2.5:7b、temp.7/max512、敏感值已在context、minimal sys、HTML前500chars；30×16配置=480，加120 benign，非真实服务总体。§5/77–84 egress是实际collector请求，不自动等secret leakage；Leak@k按any-sensitive first-k定义必单调，但Table4/99给sharded .263→.158，数值/stealth论证不兼容，**不采此定量结论**。§6/108–123 domain allowlist仅对攻击域在表外有效，prompt和monitor results不授所有攻击安全；dynamic taint是提案。可采用独立的URLpreview/redirect隐式外发不由干净回答认证；不采单模型比率、sharding定量保证或零安全。

Actual Ch72 1313–1345已读search-query实际egress先于回答过滤、累计query-family，以及跨合法toolcall的信息流/允许sink；2910–2932 metadata→外发与多调用分责也覆盖。建议具体Existing/NoChange仅网络effect采用链，数值子命题争议保留；若root认为sharding是不可分中心则整项Disputed隔离，不用降分或删反证替代。

## 22457 CCCL，2+2+3=7，深入完成提案

原§2/27–39 DAX mmap+cudaHostRegister+CXL↔GPU DMA，非HBM coherent zero-copy；实际3H100节点/6×128GB Micron/TitanII/Gen5，200Gb IB对照。§3/55–80共享池无硬件fine interleave，以collective规律预分配rank/device regions，rooted轮转与N-to-N互斥device范围不同；规模/设备配额条件不能任意外推。81–93 write/read stream+chunk doorbell，先完成D2H写再READY/flush，consumer invalidate/read后取数据；发布可读不说明故障恢复、跨次buffer回收，伪码不完整memorder proof。§4/96–130 3节点真硬件，6/12nodes emulator依独立均匀device BW假设；>256MB AR1.05×仅小增，RS .48–1.9×、A2A .7–1.9×有慢侧，12node AR contention8.7–12.2×时间。Llama3-8B/Wikipedia/FSDP3node1.11×作者，不完整batch/precision；switch价对比非TCO。

Actual Ch36 61–69共享memory/消息分工、221–229现transport/SHARP、345–391 remote-memory/ready/consume/reuse已读，未有**CXL pool不是同一HBM对等路径、规律collective放置避免共享device争用**具体选择。请求Ch36 remote-memory分支一段+自身note：DAX/DMA pool+按collective布局/doorbell，真实3node与模拟大规模分开、慢侧/完整成本/故障回收未证明、普通NCCL/IB回退；不复述现release协议为paper新贡献。
