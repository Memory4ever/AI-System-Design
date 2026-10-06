# A后段四项必要证据（待root Source/Books复核）

## [MI300A execution 2602.10262v1](https://arxiv.org/html/2602.10262v1)

5=2+1+2，标准后受具体中心冲突深入，拟暂缓性能采用。§4实际单MI300A/RHEL8.10/ROCm7.2.0/amdgpu6.14.14/gfx942，CPU/GPU affinity、500iteration opcode timing、稀疏50runs/10warmups；库kernel不是同quality LLM训练/Serving。§5总activewavefront=block数，§6 occupancy另变fraction概念；256waves只13.7%所归一peak，不是已逼近steady理论peak。§6 concurrencyoverlap可增但sharedcache/LDS争用，当前fairness与scheduling attribution均为作者microbench，不证明queue scheduler公平定理。

§7中心稀疏解释有冲突：所述同60配置一处rectangular1.6–1.76×却随后整域0.97–1.02×/无shape突破；§4 fairness为1−range/mean，§7改min/max不能合并；§7.2 throughput中single sparse52.1低dense59.98却又sameallconcurrency perstream1.3，定义还写sparse时间除dense时间，不能直接照录更快；8192³ GEMM减半算术在300TFLOPS约毫秒量级，所称4.6μs和32k³超128GB的理论推导缺真实layout支持，非稳定overhead下界。Sparsehardware存在已由AMD CDNA3 ISA原primary查得，但不解决此论文benchmark归因与显示冲突；没有否定AMD本身。

原文noartifact（待acceptance公开）不是单独否定依据；中心对照/数值需要精确作者纠错、实际timing/shape/FLOPs与fairness定义才可重开性能采用。孤立microbench现象不足写Ch49/63新的数值阈值；保留争议不授Books、不把未读当受阻。原证 INITIAL L123–200；METHOD L270–369；NEXT_LOC含§6L236–269（另下批原源可读）。硬件/精度已列，模型/seq/SLO不适用GEMM，部分repeat/CV误差具体值未披露。

## [AgentPI 2602.10453v1](https://arxiv.org/html/2602.10453v1)

6=2+2+2，安全评价受影响深入。§6五类中toolname指定action switching不是全部动态observation任务；parameter extraction/conditionalbranch/functioncalc/delegation给context参与的不同role。Benchmark中显式允许读取外部context不等无限继承其中权限；task-definedgroundtruth和implicit安全边界需分清，cannot infer universal trust boundary。§7 GPT4omini + Banking16/Travel11/Workspace30/Slack9 tools，原文abstract/intro说8defenses而§7说9但实际列表/表5为8。sample数量、重复runs、uncertainty、judging实现、hardware/precision/API revision Not Disclosed。局部对照没有证明全防御均不可能达到安全utilitylatency，也不是三元impossibilitytheorem。

§7.2 Table5 baseline7.61s/4507input/465output，TaskShield时间310.78%；Progent78.58%与utility<.3关联earlyrefusal，不能当同completedtask成功加速。参数/branch攻击可保持合法tooltype，作者图结果支持这个population，不证明全部自然流量或原existingbench完全静态。FD3 data-only参数却禁止所有branch等方案仅futureproposal，不采用其‘ensures reasoning truth’。

拟具体**已有覆盖**：PLATFORM-SECURITY/Ch72 1638–1644已有toolshape不等observation任意binding授权、蓝图provenance/遗漏/误拒/合法集合中错误选择；PLATFORM-EVALUATION-SYSTEM/Ch66 727–740已要求nonresponse与固定分母task完成、paired风险及benign/should-refuse controls分别评价。这两个owner承载该论文可支持的“动态context执行可靠性不能由合法tool授权与拒绝率/低成本单独背书”而不接收不可能三元定理。无新确定防御实现，仅为该局部protocol验证，不造diff。原证 METHOD L310–390；NEXT_FINAL_0 L519–536（仅提出建议与tools数，非完成实现）；不全taxonomy/攻击附件。

## [Unlocked Backpropagation 2602.10461v1](https://arxiv.org/html/2602.10461v1)

5=2+1+2，标准完成拟仅报告。§2PMP只是necessarystationarity，liftsolver τ与depth t，invertiblewaves+localresiduals进行forward/backward upwind transport，Alg1每层局部更新parameters与boundaryscatter，并不把有限τstep变成exactglobalgradient。Energyidentity非无条件convergence；requires passiveboundaries/dissipativeforcing、Θ与t独立等声明。§6每τstepparallelO(1)不等总优化O(1)：传播lightcone仍depth/c，acceptable residual需多τsteps，新增transientwave state；discreteCourant/junctionstability与实测trainingquality/walltime明确future work。不能写pipelinebubble/activationmemory被通用消除，也不等PMP全局最优。纯理论机制hardware/precision/modelbenchmark不适用，无可比实测gain。

拟OnlyReport保留具体localwave替代算法/条件，不用‘理论新颖’强制所有proof或Structure新增；当前仍欠discrete稳定与训练质量条件，不能推动真实distributedtrainingbaseline替代。原证 INITIAL L74–247；NEXT_FINAL_0 L248–275；METHOD L474–485。未采用optimizer阻抗形式定理，无需扩全物理analog章节。

## [Authenticated Workflows 2602.10465v1](https://arxiv.org/html/2602.10465v1)

6=2+2+2，安全受影响深入。§II L1cryptohardness/L2trustedregistry-policy-controlplane/L3nonbypassPEP和framework APIs被固定；应用控制不含PEP memory/binary/systemcompromise。MAPL caller/resource/orgpolicy交集+denyunion+requiredattestations，缺policy默认为不添限制（不是全场景failclosed）。Invocation签operation/args/policy/context，receiver重新取有效policy，completedservice签result→后续dep证明。attestation证明签发者宣称完成，不验证语义执行correctness；合法origin恶意content仍可签，policy授权action可符合却违背用户自然意图。

§VII主要证明conditional encodedpolicy和hashreplay边界，Lemma7实际PEP被攻破又假设L3正确/不允许corrupt的冲突不授任意Byzantine；哈希链不证明本来输入安全，ephemeralkeyexpiry不自动前向保密。§VIII174testcases/18variants/6explicitcategories，Atlas是作者emulation而非实际对厂商生产部署；100%recall/0FP只既定violations/policies，customPII/promptjudge可误判。§IX commodity8core16GB；ECDSA256/SHA256 ~.2mscryptoonly/≤1mswithoutLLM，150–500mscustomLLMdominant；CPU型号、重复/CI、同actualworkflowE2E、网络/provider/revision Not Disclosed。没有production universal guarantee/零成本/无缺失policy风险。

拟具体**已有覆盖**PLATFORM-SECURITY/Ch72 1618 proof-derivedartifactgraph→deterministicauthorizer→digestcapability，已含前序outcome/attestation、rules≠realconsequence和key/controlavailability；78 563 toolattestation与formalstatement分别验证，83 177–179admission/call分权。MAPLpolicy组合和签origin是作者受限实现branch，不再写第二份通用policyowner；以实际正文而非主题相似。原证 INITIAL L78–218；METHOD L312–424（核心policy-proof+174tests+localcost），不全九框架附件。
