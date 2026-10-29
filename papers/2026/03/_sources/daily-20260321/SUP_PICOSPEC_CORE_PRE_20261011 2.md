# PicoSpec19133 必要原证 / 具体 owner / PRE

准备者 root，仅03-21补03-20自然日；当日独立准入与日期夹证复用，旧候选与窗口不迁移。拟2+2+2=6，异步边云回退与概率数据搬移的接口差额深入，非宣传倍数。未授写入或DAY。

## 必要 Source 与反侧

[exact-v1 HTML](https://arxiv.org/html/2603.19133v1) §3.1–3.4/Figures2–6/Eqs1–10、§4.1–4.4/Tables1–4、§5实际读。没有遍旧引用/后版本或核代码/复现。

- §3.1–3.2两侧prefill初始化，edge在当前batch尚未验证时假设全接受并预做下一batch；reject立即interrupt、rollback/correction，partialprefix PreVerify进一步重叠。其max(draft,RTT+verify)是full-hit理想路径，不是无条件吞吐；§3.4以IID接受alpha与固定时间混合hit/miss，miss退串行。缓存身份、late-result幂等和取消实费未给完整协议，不能由草稿先跑取得commit权或保证抖动免疫。
- §3.3云只需候选token的q标量作acceptance，reject时下发p，edge保留同prefix完整q并作norm((p-q)+) correction；改变传输/采样位置不必改变理想完整概率规则。随后只下发target Top-K概率，v1没有尾部残余恢复、归一/zero-residual规则或等价证明，不能将这一实际压缩实现认证exact。这不是optional artifact缺失，而是必要算法边界；只采用分离数据流和精确/近似分账。
- §3.4 Eq5 EL上界γ而Table1设γ4并报接受长4.29/4.90，可能含bonus但定义未统一，不照录原alpha进度推导或speed recipe。极低接受率S→1仅固定时间模型忽略额外取消/通信工作，非生产最差界。
- §4限定Jetson AGX（型号/精度未披露），云A10040GB，Qwen3 .6B/32B用2卡、Llama3.2 1B/Llama3.1 70B用4卡，GSM8K/HumanEval，draft4。Table1有限吞吐有收益，未披露WAN RTT/bandwidth具体值、输入输出长度、batch/concurrency、temperature/topK、质量结果/seedCI或SLO。Table2/3吞吐与TPOT分母亦未统一，不从tokens/s反推逐token latency。LlamaHumanEval full相对无FastVerify TTFT/TPOT反退。Table4 n6更差，高接受不等于净收益。Split只前三层及整个branch同时异步/通信变更，不授全部设备最优配置。
- 费用包括edge继续算后被丢弃、云verify、网络双方prefill、p/q存储搬运/序列化、取消rollback及排队。不得说latency immunity/不改变输出质量/最差不退步。证据不足则短draft、完整概率修正、同步或cloud AR。

## Actual owner

`INFER-SPECULATIVE-DECODING` Ch48：实际228–288预算和481–502跨进程prefix/epoch/retry，以及经典完整ratio/residual数学。Ch47/49入口读。已有异步provisional协议，不重复；差额是**候选q标量上行、reject p下行、完整q本地校正**与紧随的**Top-K传输不能自动继承exact**。唯一owner仍采样/commit，不把edgecloud名称变第二章。

## 一段逐字 PRE

跨到边云后，提交协议还必须与概率数据的搬移一致。完整词表分布每轮往返最直接，却会在受限带宽下抵消投机收益；一条分支仅上行已抽候选的 proposal 概率，让云端验证，拒绝时才下发 target 分布，由边端保存同一前缀下的完整 proposal 分布并执行正部残余校正。理想完整概率下，移动校正位置不必改变原采样规则；但若为省带宽只传 target 的 Top-K，便须另证尾部与残余恢复，不能由“保留大部分质量”继承 exactness。[受限 PicoSpec 对照](https://arxiv.org/html/2603.19133v1)没有补齐这条压缩保证，也未统一接受长度与 bonus、吞吐与逐 token 延迟的口径，不认证 WAN 延迟免疫或最差不退步。下一批在旧批未确认时提前计算，仍是可取消的 proposal；拒绝后完整回退，额外计算、概率存储、网络与两侧 prefill 均计费。带宽、状态身份、尾部修正或净收益不能验收时，保留完整概率、短 draft、同步验证或 cloud AR。

位置：Ch48跨进程协议段及其既有边界之后、Lexical Reuse标题之前。只一段+本人静态注。

## 静态注 PRE

- `SF-2026-ARXIV-2603-19133` — [PicoSpec exact-v1](https://arxiv.org/html/2603.19133v1) §3.1–3.4/§4.1–4.4/Tables1–4；仅分离候选概率上行/拒绝分布下行与完整残余校正接口。Top-K尾部保证缺失、EL/bonus口径、吞吐/TPOT分母与未披露网络/采样/长度/并发限制保留；不授exact压缩、WAN免疫或最差性能界，未核实现/复现。

## 非准备者必要 Source / actual owner / PRE：正式有限通过

resume_mar18实际exact-v1 §3.1–3.4/Eqs1–10及§4.1–4.4/Tables1–4/§5，actual Ch48经典ratio/正部残余、228–288预算与完整470–515跨进程协议→Lexical交接、Ch47/49开篇逐字回对一PRE/静态注，正式有限Source/PRE PASS。云读抽中候选q标量、拒绝p下行、edge保持同prefix完整q的概率数据位置差额，不是已有provisional/commit一般边界的重复；2+2+2=6成立。

Top-K只有target高概率分量而无tail/re-normalization/zero-residual规则，原lossless/unchangedaccuracy中心承诺不采用；不妨碍以明确“理想完整概率”条件解释搬移位置与采样合同、并把实际近似压缩单独验收。Eq5最多γ却Table1γ4报4.29/4.90、Table2/3 throughput与TPOT分母不齐、Llama HumanEval full TTFT369.02/TPOT272.93劣于无FastVerify346.16/263.94、Table4较长draft净反退和固定理想模型未计完整取消费用，原PRE都未外推收益。网络/采样/shape/并发/质量协议ND，full-hit不证latency immunity；已保额外draft/双方prefill/概率state与回退。

仅PRE与必要Source通过，待root唯一Ch48窄锁写入后一次nonwriter完整正文/邻接/本人静态注POST，未计safe/DAY，不扩旧版或无关附件。

## 非 writer actual POST：正式有限通过

resume_mar18实际完整Ch48 478–518，其中跨进程commit/provisional协议→新增498→Lexical读取交接及最后九行本人静态注/邻注，逐字回对有效原PRE/Source，formal POST PASS。正文只新增唯一family marker与原逐字一PRE，完整p/q理想概率与Top-K实际压缩分账；extra draft/概率state/双方prefill/回退和直接反侧保持，未把既有commit协议替换或授lossless/WAN免疫/最差界。本人静态注准确、未写审计身份；不需改已通过Book注。仅单项actual I安全，不授本日DAY。
