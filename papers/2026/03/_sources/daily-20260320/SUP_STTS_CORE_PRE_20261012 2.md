# STTS18004：本20必要Source与最小PRE

resume20_author_new sole准备，仅03-20补03-19；原2+2+2=6/准入day复用，不自授Source/PRE、Books锁或DAY。

## 1. 精确源与必要停止

[exact-v1](https://arxiv.org/html/2603.18004v1)必要§3.1–3.4/attention bias/aux、§4.1–4.3/T1、§5.1–5.5/T2–3、A只T4/模型身份、B/T6–7、C/T5、D/Alg1与E/T8已读；current abs同八作者单v1，无具体修订/撤回。未核所有示意图、references、代码或复现；采用接口的支持/直接反侧足即停。

## 2. 机制与具体不采桥

ViT层l pooled当前/前帧features给pooler+MLP，首帧zero前项且完整保留；score广播w×w后attention bias让下游loss回传，l+1后hard删，邻帧同坐标cosine辅助训练提供时序代理。少token沿剩余ViT/connector/LLM消费，但score不读query不等task-independent训练，也不认证真正冗余。S一处称logscore又用rawscore拟合、aux pooled索引上界记N，未核实现，不采精确log有效域/全部loss recipe。

FFD按每frame剩余长度打包，Alg1保存frame→bin/offset、blockdiag mask；只改变batch container，不合并跨frame语义。本人直接反例capacity10/lengths6,5,3,2,2,2，FFD生成9/9/2三bin，但6+2+2与5+3+2两bin可行；不采“最小packed数”或硬最优。实际部署仍须检查原frame/position身份与mask、padding的consumer约定，不补造author已核unpack。

T1受限Molmo2/Qwen3-4B/SigLIP2，train6250/B64、约2samples pack/effective128、l3/2FPS最多64、视觉LLM双向attention；k50平均仍降，MotionBench61→58.2/LV42→40.5，T3加frame仍有单项反退。T2 noaux差于Random不证明所有任务loss必定不识别时间。A另一full-mixture版本仍有单项image下降，不能转作主模型image无损。§5.5超text-only分数不是视觉grounding证书；首帧保留与k100text-only如何对应未披露，不采该资格。

B real单节点8H100，128总frames=64×B2与256×B1、text最多2048，profile关闭LLM样本packing，训练compile与inference动态prefill分开；50%视觉删减只约33%总token下降。performance/计时配置不可合并，precision、总训练/scorer/packing/mask/reshape/decoder费用、concurrency/SLO/CI未齐，不采用headline62%通用加速。

## 3. actual sole owner及原两PRE

sole `MULTIMODAL-REPRESENTATION`/[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；actual612–657预算/层位置→batch-OR合并/网格恢复→GUI历史/音视频分配完整已读，936–958 codec稀疏分支及开篇/相邻Ch24/26分责复用。现batchOR保统一source位置，未拥有in-ViT score/bias训练、hard deletion沿后续模块与ragged-frame隔离packing的具体接口；拟batchOR/网格恢复完整两段后、GUI历史预算前。不额外写Ch49 packing第二owner，不授通用bin最优或任意encoder兼容。

### 正文PRE 1

不规则保留也可以从encoder内部贯穿后续消费者，而不先把整批mask做并集。一个视频分支由当前与前帧的局部features提出score，通过下一层attention bias接入下游任务梯度，并用邻帧相似度辅助训练；随后硬删低分区域，只让幸存tokens进入剩余视觉层与语言consumer。首帧保留、删除层和局部pooling须共同版本化，相似度与task梯度只是选择信号，不是证据冗余真值。各帧剩余长度不同，可打包进较少稠密容器并以原frame身份的block mask隔离；打包位置不是新的时间或空间坐标。<!-- source-family:SF-2026-ARXIV-2603-18004 -->

[有限跨encoder删选对照](https://arxiv.org/html/2603.18004v1)仍有任务和更早删除的退步；增加采样帧数又改变输入人口，保留token预算相近不等完整计算相同。训练过稀疏输入与仅推理删选须分别验收，first-fit打包也不是最优证明。score训练、相似度、排序/scatter、mask/padding与完整回归均计费，单节点吞吐不签在线SLO；短事件、局部证据、身份映射或净费用失配时，增加保留下限并回原dense/均匀采样路径，不由较小tensor或高于无图分数批准grounding。

### 静态来源注PRE

- [STTS2603.18004 exact-v1](https://arxiv.org/html/2603.18004v1)：必要§3/bias/aux、§4–5/T1–3、A身份/T4、B/T6–7、C/T5、D/Alg1、E/T8。仅in-ViT训练score/bias后hard删选沿后续consumer与frame隔离packing；保相似度非真值、首帧/位置接口、任务/更早删选反退、更多frames及profile不同配置和全费用。不采精确log/loss recipe、FFD最优、超text-only即grounding、全部image无损或生产SLO；未核全图形/代码或复现。<!-- source-family:SF-2026-ARXIV-2603-18004 -->

待非preparer必要Source/actualowner/原两literal裁，未写Books。

## 5. resume20_author_new实际窄写（writer，非POST）

root在SegFly锁释放后授本family soleCh23窄锁，复用reader§4必要Source/owner/PRE，不重复原证。写前626–643/末7、写后626–647/末9完整顺读，原两literal/static逐字落632/634/static1844；机械唯一各1、限定diffcheck0。batchOR+网格恢复完整后→in-ViT score与frame隔离pack→GUI时间预算顺接，损失/FFD不采强桥及局部反退、全费保持。不更改静态身份，交reader一次actual nonwriter正文/完整邻接与本人邻注POST，writer读回不自计I/DAY。

## 4. resume20_reader_new非准备者必要Source/actualowner/两PRE裁

实际exact-v1必要§3.1–3.4/L105–136、§4/T1/L140–183、§5/T2–3/直接反侧/L188–247、A/T4仅模型人口、B/T6–7、C/T5、D/Alg1与E/T8/L314–434读；current八作者单v1，无具体纠错/撤回。只采用in-ViT训练score/bias→hard删→原frame隔离pack接口，不核全示意图、代码/复现或全附件。

首帧zero前项且完整保留、score经下层bias传任务梯度、相邻feature辅助与l+1后硬删成立。S的log/raw和pooling索引不照录精确recipe，cosine不是冗余真值。本人按FFD复算capacity10/6,5,3,2,2,2得9/9/2三容器，而6+2+2与5+3+2两容器可行，故不采最优；Alg1frame→bin/offset与blockmask不更改原空间/时间身份。T1任务反退、T2 noaux、早删、T3不同frame人口、A另一fullmixture、E text-only与首帧资格及B不同packing/8H100profile费用均保。原两literal/static已收窄、不授无损、grounding或SLO。

actualCh23完整608–664预算/层位置→batchOR/恢复→GUI/音视频分配及开篇/邻章分责有效读域复用。batchOR统一source位置不承载in-ViT训练删选沿后续模块/异长frame隔离packing的接口，soleCh23差额成立，拟恢复完整后两段顺接GUI历史，不写第二owner。**必要Source/actualowner/原两literal/static有限PASS**，原6/day不动；rootsole锁后才可写，仍待一次actual非writerPOST，不预I/DAY。

## 6. resume20_reader_new一次非writer实际POST

rootsole Ch23/作者实写后，复用§4有效Source/owner/PRE，不重核源。实际完整626–650（Affinity层位置→batchOR与网格恢复完整段→本family632/634→GUI历史→音视频预算入口）及1834–1844本人/全部局部邻注顺读。原两literal与static机械逐字唯一各1，位置632/634/1844；family两段/static六新增与原已验VirPro/SegFly分账，cached/unstaged限定diffcheck均0。score/bias训练→硬删→consumer、首帧/时空身份、FFD非最优、任务/早删反退、计时/训练配置与全费用/回退均近文保持，未改旧邻段或静态身份。**一次有限actualPOST PASS**；交root接纳释放本family Ch23窄锁，不自计I/DAY。
