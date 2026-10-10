# 11438 NCCLbpf：必要证据与通信策略更新差额

root，仅本日 Mar13 北京时间补充窗口。完整v1题摘及首批准入有效复用；实际 `SUP_DATE_11438.raw` 的本ID DOI/official URL/arxiv.content/findable、Mar13 01:55:36UTC注册上界和官方公告下界同Mar13，不能单用注册/提交当首公开。精确 [2603.11438v1](https://arxiv.org/html/2603.11438v1)；`SUP_NECESSARY_11438.raw/txt` GET200，2026-10-09T14:27:59.756630+00:00。实际读 §3完整/§4/§5.1–5.3/Tables1–2和§7；不核代码、像素点值、真实生产故障案例或引用全集。

## 具体增量与评分

native通信策略和运行库共享address space、更新常依赖重启 → existing plugin ABI内放受限BPF验证/JIT、profiler→tuner typed maps和atomic pointer reload → 必须区分程序资格、状态兼容及调用更新边界，与全collective/rank一致性不同。具体差额为通信callback内的策略/观测/替换协议，**2+2+2=6**；不借成熟eBPF/CAS或通信completion原则加长期基础分。现Ch36已讨论verified policy大框架，仍缺per-call reload及在飞旧程序回收的实际责任；且原“验证可组合性”与“排除了风险”措辞过宽，需针对具体owner差额深入，拟受限补充两段＋两处资格收窄，待独立PRE。

## 原证机制、威胁边界

§3.2 operator写policy而非任意不可信租户；PREVAIL检查memory/bounded execution/stack/helper白名单，不保resource exhaustion、side channel、JIT/verifier/host TCB bug或错误策略。输入context与受限输出、map lookup/null checks是程序资格，不是全policy正确性或数据race全消失证明。Profiler写map、tuner读map，typed固定key/value和atomicaccess也不自动认证最新遥测、稳态控制或跨map事务。

§4将算法/protocol/channel输出翻译成NCCL成本表：prefer0/other1e9，合法组合不可用仍由NCCL回退；channel按runtime最大值clamp。comm identity是context pointer hash，不据此认定全寿命/跨重建全局唯一。原库拥有collective算法/participant/result/completion，policy没有重定义训练step或tensor的权力。

更新先验证再JIT，最后CAS函数指针；旧policy留到在飞call drain，新call读新pointer，验证失败保留原policy。§3.1允许线程短暂旧/新并存，并把每call决策独立作为理由；这不是所有rank同步切换、整个collective epoch一致或任意map schema热迁移证明。原件未核回收实际代码和跨rank失败恢复；书稿只能给更新验收责任，不声称实现已经保证这些条件。

## 评价与直接反侧

作者称NCCL2.29.7/CUDA13.0、8×B300 SXM6（所报275GB）/单nodeNVLink5；仅作论文实验配置，不核当前硬件规格事实。CPU EPYC9575F/1Mcallback/P50P99，same−O2 native logic20/30ns，BPF100–150/111–160ns。80–130ns是CPU callback差，不是完整GPU请求额外费用：小8B–256KiB collective约1.3μs/4%框架费，4MiB以上测量噪声<.1%也不等零成本或训练step不变。启动verifier1–5ms、reload总9.4ms和hot swap1.07μs三个成本分开。

§5.2七safe接受/七特定unsafe拒绝与40万call零丢失，是受测输入和调用的结果，不是所有程序/故障形式化端到端安全。Table2 Ring在4–128MiB改善，256MiB−3.7%、8GiB−16.6%；policy在其他区间回原default而非强制Ring全优。2–3 communicator warmup后测稳态，完整长训练、数值正确/收敛、真实干扰与重启费未验收。memory-safe单channel坏policy仍能退87–95%，证实verifier不拥有性能裁决。

Profiler→tuner控制例中channel2→12、注入10×latency后12→2再恢复，说明map共享可被消费，不证明实际多资源contended集群控制稳定；AllGather20run方差变化不是新吞吐收益或tailSLO。net只wrap Socket isend/irecv并计bytes，<2%仅该原型；RDMA/multinodeInfiniBand/更大rank与RCCL仍未验收。保留所有这些边界，不从八卡microbenchmark签生产hotpatch。

## Actual owner / 逐字PRE

唯一 `TRAIN-DISTRIBUTED-TRAINING` / [Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)。实际读227–284完整operation/algorithm→endpoint/feedback→库分工→verified policy→bandwidthstate交接，及Ch35恢复责任/Ch37布局与collective入口。现文263已引同family，但只有verification/semantic-performance分责，未写atomic pointer和旧call drain/map身份；不因同family再次盲写，新增范围只限此缺口。

拟将原“在collective边界先验证其可组合性、资源访问和ABI”收窄为“在通信策略callback入口使用按受限语言和helper合同验证的程序，并核对资源访问及ABI”；“排除了…风险”收窄为“只覆盖验证器及受信运行时假设内的…条件”。然后在同节现风险段之后插：

> 策略可在运行中替换时，还要把“新程序可执行”与“旧调用已经结束”分开。一个受限更新协议先验证并编译新程序，再原子替换callback读取的函数指针；在飞调用继续执行旧程序，旧程序要等这些调用drain后才能回收，验证失败则保留原策略。Profiler写入、tuner读取的typed map让观测可跨插件消费，但map schema、communicator身份与遥测有效期仍需配套验收；原子字段访问不能代替跨状态的一致更新。

> 这个边界只允许单次callback看到可接受的程序，不自动保证所有rank同时换版、一次collective内决策相同或控制回路稳定。[受限NCCLbpf实验](https://arxiv.org/html/2603.11438v1)只测单节点八GPU；CPU策略调用的纳秒开销不能代替完整GPU路径，小消息仍有框架费用，验证通过的坏策略也能严重降速。验证、JIT、map访问、warmup和旧调用排空均计成本；helper/运行时缺陷、状态schema失配或跨rank行为无法验证时，保留原策略、静态配置或受控重启，不以热切换测试签任意生产安全。

这是原owner精确资格修正和缺口补全，不引第二Security机制owner，不修改原候选日期/评分。Source/PRE和实际POST尚未授，根不自行写后验收；无实现或复现声明。
