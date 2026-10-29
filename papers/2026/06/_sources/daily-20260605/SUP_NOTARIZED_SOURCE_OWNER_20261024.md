# 04193 Notarized Agents：必要Source与actual-owner最小提案

作者supp_20260605_author，2026-10-24。本次恢复重读AGENTS/当前研究与Report合同、Prompt、来源说明/每日/arXiv/恢复、ROADMAP、仅本2026路由及本日停点；实际采用reader R13–15准入和Jun04联合日证，不第三。R19–20既成两I已行政同步，累计新增I5，旧Kimi另保、DistIL7双中心争议不变。当前只交本一ready，不等05158/04945；无本项Books写入授权，未写共享正文。

## 精确原域与必要深读范围

[官方exact-v1 HTML](https://arxiv.org/html/2606.04193v1)已实际保存为同目录`SUP_2606.04193v1_20261024.html`；官方abs/版本史和exact DOI联合日期原件继续复用。必要读§3威胁模型、§4收据/owner-key绑定/完整验证流程/撤销、§5全部直接安全反侧、§6检索完整性、§7.1–7.3方法/数字/未测网络和§8.1–8.3限制/未来接口。§2只定位成熟密码组件与adjacent方案，不扩全引用；未下载或运行代码、未复现密码实现/测试向量。因安全信号和actual owner知识缺口，6分仍深入受影响域，不因工作量改分。

## 机制及其信任边界

§3四角色是owner、agent、service、witnessed public log。对手能控制agent/operator/网络与其telemetry、读公共log及提交任意bytes，但不持合法service Ed25519 signing key或owner HPKE secret；另假设所调用service至少一个诚实且未被攻陷。全部串谋不能检测，不能写成零信任或所有receipt独立真值。

§4.1/4.2：service先验JWS发行方签名，从签名claim提取owner_hpke_pk而非采信agent另报key；同token还可绑定目标log列表。它构造含action及input/output SHA256摘要的CBOR body，先HPKE加密给owner，再对加密envelope作COSE_Sign1签名。protected header含kid、版本、raw-token-bytes的SHA256 token_ref和log_url；并非全metadata私密，也不是保存完整I/O。不能从摘要重建未另保留的输入输出。

§4.3 owner按token_ref查询可信logs，逐份核返回log_url、witnessed root下inclusion proof、registry kid、service签名，再以protected header作AAD解密/验body。§4.4 JSON签名registry及24h freshness只是v0.1临时identity方案；撤销使用log integrated time而非service自报clock以免简单回填旧时刻，但此时间不证明真实action clock或已知key compromise时刻。本文§5明确是informal security analysis，不补造formal theorem或密码原创性/全球首创。

## 关键反侧与不采用的保证

§5.5：agent绕开参与service或根本不call时无receipt；空集不能区分没行动/网外行动。service可串谋伪报，持自身key还可把旧event重新加密签名；秒级tuple去重不是强freshness或普遍anti-replay。至少128bit token熵是要求，token holder仍可计算同ref，kid/ref/log_url仍暴露关联metadata；owner丢私钥后旧body不可恢复，escrow未解决。

§5.4/§6最重要区别：对已经返回的每份receipt都验过inclusion/signature，仍不能证明“所有匹配项都返回”。log/indexer可返回20份中的10份而让10份全通过；还有未索引自定义header、查询错log的遗漏。v0.1 Rekor adapter明确discovery-only，不是集合完整性证明。authenticated exhaustive query、完整log扫描、多log冗余在文中是补救设计方向，不能当本实现已提供的保证。只由服务签发和合法key证明其陈述来源，不证明服务诚实、底层副作用真实或全链路执行完成。

§8.1/8.3实际adoption尚无；production identity bootstrap、heartbeat suppression detection、合并trace做divergence detection及PIR都未实现。旧operator trace在可信instrumentation、请求因果/排障上仍合理，此协议补receiver见证，不能替掉trace或effect ledger。

## 评价能支持什么

§7.1–7.3是作者first-party本机crypto microbenchmark：Apple M2 8核/24GB，macOS26.2，Node24.16/V8/OpenSSL3.5.6，repo8b0da95；Node OpenSSL绑定的X25519、Ed25519、ChaCha20Poly1305、HKDF/SHA256，local in-process mock log而非hosted网络。每run先GC并500 warmup，N10/100/1000分别3/5/10runs，先每run统计p50/p95/p99再跨run取中位；batch verification每run仅一个timed event。繁忙开发机load6–10/Spotlight仍开，不采用“生产tail一定更好”的作者外推。无模型/precision/生成长度/batch，因不是LLM inference试验而不适用；真实service concurrency/SLO与hosted-log延迟未测。

Table2 N1000 receipt creation median0.454ms、single verify0.281ms，有限重复只能说明该crypto/mock路径成本，不是网络/存储/查询/effect整体延迟。§7.3异步提交可以让响应先返回，但因此response returned不证明receipt已经获得durable witnessed inclusion；要验审计提交仍依靠独立ack路径（工程推断，非本文已验证生产合同）。半KB来自只保I/O摘要，不是免费完整行为重建。sign/encrypt、identity/key维护、log提交/保留、检索和完整性补救全有费用。

## 评分与actual-owner差异

2+2+2=6保持：具体新增为receiver独立producer＋token绑定owner加密的receipt接口，并明确单份可验/检索集合完整性的边界；不是给成熟签名/加密原则本身加分。唯一owner `PLATFORM-TRACE`，当前Ch69 `## 安全与成本`：现段只有span敏感字段及instrumentation开销/高风险audit另路，未解释operator telemetry可被同源篡改时如何引入receiver receipt及其不能证明的集合。已实际读Ch69字段/provenance/采样/安全成本相关组、后Root-cause入口与邻Ch68/70开头；定点读Ch68可靠传输的durable-ack完整组，那里拥有“producer→sink已持久化”而非“producer是否仍在operator信任域”。不把新机制复制到Ch68/Ch72，也不让Ch69接管权限或effect真值。

精确建议窄位：Ch69下列完整前段之后、完整后段之前；不是新H2或章末摘要堆积。当前仅PRE提案，待非writer必要Source/actual-owner/PRE与root明确新授。

前完整锚：

> Instrumentation overhead 应被度量：serialization、context propagation、collector queue、export failures 与 storage cost。Trace 系统故障不应阻塞普通请求，但高风险 action 的 audit 要另有可靠路径。

拟新增两段literal：

> 可靠传输仍默认producer值得信任；当Agent与operator本身可能改写telemetry时，可让被调用service成为另一证据producer：先验证授权token中签名绑定的owner加密公钥，再把action及输入输出摘要加密给owner，由service独立key签名并提交witnessed Merkle log，owner按token reference发现并逐份验证。这样把“Agent自报做了什么”与“接收方声明看到了什么”分开，却不使签名等于真实副作用；服务串谋、key compromise或网外调用仍越出保证，摘要也不能恢复未另保存的原内容。
>
> 单份收据可验还不等于集合完整：log或indexer少返回匹配项时，每份已返回收据仍能通过inclusion和签名检查。Notarized Agents v0.1的discovery adapter不提供穷尽性证明，空集也不能区分没行动与绕过参与服务；完整查询承诺、全log核对或多log补证仍须另验。合法service仍可重签旧事件，秒级tuple去重不提供强freshness保证。公开header还会泄露服务/token关联，owner key丢失会失去旧内容访问；加密签名、身份维护、提交保留与检索全部付费。本机mock-log的crypto成本不是线上SLO，异步返回也不是审计已提交。需要完整追责而证据不齐时，保留原trace、独立durable audit与Unknown，不以receipt数量或合法签名批准effect。<!-- source-family:SF-2026-ARXIV-2606-04193 -->

后完整锚：

> 当所需证据只是每个 kernel 访问过哪些 memory objects，而不是每个访问地址的因果序列时，collector 还可把分析位置移到 device：在 GPU 上按对象计数，kernel 结束只回传聚合 map，避免 raw trace buffer 满后反复传 CPU、停顿和逐事件分析。这个 summary 能回答特定 working-set 问题，却已丢掉原事件次序，不能冒充完整 trace、并发 live-memory peak 或根因证明。[受限 device-summary 对照](https://arxiv.org/html/2602.22103v1)在 A100/RTX3060 与若干 DNN/语言模型上比较完整 profiling 过程，但 CPU 对照常单线程，NVBit 还包含 SASS 解析；倍数不能只归因 placement 或当作原任务吞吐。额外 helper、计数、驻留和 instrumentation 仍会扰动执行，开销随事件类型/数量改变，4MB 示例也不是通用上界。应绑定 capture scope、object identity、丢弃字段，并按相同事件/evaluator计收集、传输、分析及原 workload 的费用；需要完整时序、范围未覆盖或扰动不可接受时保留 raw trace/CPU分析、较粗采样与明确 unknown，不因 passive 未改程序数据就宣称零干扰。<!-- source-family:SF-2026-ARXIV-2602-22103 -->

## 当前交接

本项必要Source/actual-owner/literal已就绪，非writer复核未做、无新窄授/实存/POST/I。05158/04945尚普通必要Source，不为了等本项独核扩大Methods；机构差额/其余有限题摘停点不变。本阶段交root即释放作者slot，不表示本日结束/暂停；累计新增I5、DistIL7争议、本日未DAY。未改State/index、其他日期或共享Books技术正文，未stage/commit/push。

## 当前R21–22采用与真实SAVE

上述“当前交接”为前一准备阶段保存态；本轮实际读回R21–22，按R21唯一补句将service replay/freshness限制加近正文，其余literal不变。root明确新窄授后，Ch69 Instrumentation overhead完整段后/GPU device-summary完整段前两段及现有true-H2本人注已真实保存。当前待唯一非writer actualPOST，不预I/DAY；累计新增有效I仍5。05158/04945及来源/题摘普通停点保持，不扩Methods。

## 当前R23已成事实

reader R23唯一非writer actualPOST已通过，本项整合生效、窄位释放，累计新增I6。作者本次仅行政同步README/本人H2注及当前记录，不重必要Source/正文或第三POST，不授DAY；旧Kimi另保、DistIL7争议不变。后续仅05158/04945普通必要层。
