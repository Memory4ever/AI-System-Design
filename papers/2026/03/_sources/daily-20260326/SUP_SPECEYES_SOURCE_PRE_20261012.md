# SpecEyes necessary Source / sole Ch81 两PRE

2026-10-12，[2603.23483v1](https://arxiv.org/html/2603.23483v1)原2+2+3=7/date25保持。actual§3–5/Eq1–16/T1、F3–6文字必要反侧；未核全部图点值/code/复现。

## 具体采用 / 限制

四phase：先**large**原图+query单binary token判断是否toolrequired；仅toolfree进入small直接完整answer/fulltokenlogits；gate接受直接返回，拒绝或toolrequired仍走原large完整工具loop。不是tiny先规划也不是target模型verifydrafttoken，本次规范将原准入“提出计划”收窄为完整tool-free答案/终止资格，不改原7/date。Lossy回答路由，不保持原target分布/正确率exact；fallback非安全证明。

标准化leadinglogit相对topK平均/方差后，分别mean/min/bottom-r聚合+sigmoid；min避免均值掩盖低分位置，但token正确与margin单调关系只是Prop1假设，unionbound只≤Σerror，未披露校准函数/长度依赖，因此min不认证answer错误率或“最紧所有策略”。ε破坏严格scaleinvariance极小方差仍有numerical/不同长度和tokenizer边界。K增大speed↑accuracy↓，不能由topK或score高授绝对正确/任意开放生成。

Eq4把B并发query的吞吐写B/ΣL，单query状态依赖不要求跨query全串行；Eq16 1/(1−βα)忽略前端、资源争用/残余任务难度，只这份简化serialbaseline下近似，不授全servingthroughput bound。Eq9 cJ+βcS+residualcost还须绑筛选/接纳与实际条件难度，原轻量overhead“negligible”不代测。Screen仍要large图encoding/prefill，small候选+logits/topK+reject重复执行全计费。

V*191/HR4K8K各800/POPE3splits各3000；Qwen3VL2B draft+DeepEyes/Thyme两large工具模型、max5toolsteps、greedyT0、singleA10040GB、含tool latency。Precision/image处理/生成长度/batch主表/完整concurrency/queue/SLO、重复seed/CI未披露；F5batch曲线非productiontail。正文§3 smallheldoutthreshold vs§4.1每benchmark跑一次收confidence operatingpoints+§4.2选择保baselineaccuracy最佳point，独立holdout具体split/thresholdfreeze未闭，不能授部署校准或评价独立。F3 KDE/peakdistance不是概率calibration，可能重叠/漂移。

T1min-ThymeHR8K .95×速度反退；mean DeepEyes V*Attr78.26<90.43、HR8K67.38<71.43；宣传最高3.35×来自mean/Pos，不能与min全质量绑。推荐min局部均值更好不等每request无损；draftonlyPOPE部分好于large不能证明全tool不必要。SpecReason414tokens/3.48rounds是另一工具能力/候选路径预算，不独归confidence公式。Multidepth/有tooldraft是future；高副作用action不可借本imageQA结果取消权限gate。

## actual Ch81 gap / 锚

actual Ch81开篇、254–310 workflowadmission→现有轻量directanswer/separability/residualqueue→Toolspace→evaluationsearch及Ch80/82开篇已读。已有具体lossyroute覆盖基本分支，无需复述成新机制；差额是**large先screen/small只答eligible→min-token的校准资格与residual复杂度/前端成本绑定**，并将并发batch与单query因果依赖分开，不以Eq16当系统定律。sole AGENT-WORKFLOW Ch81，不复制Ch48exacttokenprob规则/Ch56service容量。

拟现“同样地，Agentic multimodal request…”完整段后、下一Clarification semantic-body-binding marker前两PRE+纯注。不改原完整段/Clarification两段，不新增节。未独核/锁/实际写。

## 两逐字PRE

这种提前终止还可以分成两道不同资格：先让有工具能力的主模型判断原图是否可能需要进一步观察，仅把初筛合格的请求交给小模型直接作答；再检查整份答案中的薄弱 token，而不是让高分位置的平均值掩盖低分位置。Leading logit 相对一组竞争者的间隔可作为受限 gate 信号，不能当正确概率；min-token 接受规则仍需独立校准、长度与 tokenizer 绑定，拒绝项回原完整工具路径，不是由小模型替主模型验证一条等价轨迹。<!-- source-family:SF-2026-ARXIV-2603-23483 -->

前端可批处理，不意味着单请求依赖的工具步骤或剩余难题免费。筛选的主模型编码、候选生成、logits/gate 与拒绝后的完整执行都进入预算，接纳比例也须与残余任务复杂度和资源争用一起测；忽略这些成本的吞吐近似不是一般并发上界。有限图像问答中阈值、竞争者数量和输入分辨率都会改变质量/速度，部分切片甚至更慢；高置信度或平均质量保持不能认证每个答案无损。阈值漂移、独立验证不足、难题比例高或请求包含不可逆行动时，保留完整受控 workflow 和原权限检查，不让 bypass 成功率自签观察充分或行动安全。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23483` — [SpecEyes exact-v1](https://arxiv.org/html/2603.23483v1)必要§3–5/Eq1–16/T1/F3–6文字；只large初筛→small完整toolfree回答→min-token受限gate/residual预算接口。保margin非概率/holdout未闭、单query依赖非跨query串行、HR8K反慢/mean质量退和完整前端/拒绝费；不采exactspeculation、通用吞吐界、无损或行动安全，未核code/全部曲线点值/复现。
