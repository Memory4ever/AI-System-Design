# CleanSight 12989：必要原证、具体 owner 与逐字 PRE

仅本17补03/16自然日；原题摘及官方availability/DOI日级夹证已独核有效复用，当前官方abs仅v1，无已给撤回/纠错/更早正文信号；不声称排除全部先稿。精确原证：[v1](https://arxiv.org/html/2603.12989v1)、[官方事件页](https://arxiv.org/abs/2603.12989v1)。作者实际必要§3.1–3.2/Eq1–5、§4/Eq6–12、§5.1–5.4/Tables1–4、A.1–A.4、B、C.1–C.3/Tables5–7；只核支持与直接反侧，不遍历references/代码，不授复现。

## 必要证据与边界

- 威胁权限限控制微调数据、可训练adapter/LoRA；公开vision encoder/base integrity由防守方检查，runtime可读取/修改attention。不能外推任意完整权重或有runtime写权限攻击者。输出probability/pixel前端仍可在低风险、无白盒权限时使用，不宣布全部旧防御失效。
- Eq6 current decoding query（last generated token）对visual keys的attention总量除以prompt keys总量，保每layer/head后concat；不是visual单分数/所有历史text denominator。Eq8–9按干净参考各维mean/std标准化后L2，非full covariance whitening；Eq10用该参考高分位门，§5.1默认200参考、10–12层。Appendix B选层按架构fusion定位，不授各模型同层号。std为零/prompt attention质量为零的稳定化、精确position/layout规格未披露，故不采完整numeric recipe。
- Eq11在最后检测层按每visual key的max-head attention阈值取union；Eq12给全部head后续层和future decoding相应key logits加大负bias。该干预近似attention不参与，**没有物理删token、缩短sequence或释放KV**；也没有重算已有早层hidden，不能等同逆转全部污染。高attention不认证恶意语义，mask可能删合法视觉信息；模型权重冻结不等功能保持。
- §5.1四数据VQAv2/OKVQA/COCO/Flickr8k、3000pair中1500poison（50%），前四攻击replace目标短句、后两insert；ASR仅该target phrase，CU用V-score/CIDEr不是全部语义正确。§5.3.3 PU依oracle detector的消融，不是完整runtime质量保证。Table1 OKVQA VLOOD clean66.54→53.26、Table2 Flickr8k VLOOD104.16→85.91、Table4 LoRA BadNet63.80→59.29和Qwen ISSBA76.95→71.00，明确效用反退，不采用“均保持clean”。Table3 ISSBA full3.14与Table1 ISSBA0不统一headline，tau默认1e-4与oracle消融1e-3不能拼成唯一配方。
- C.1**确实有adaptive attacks**：三类正则分别针对attention ratio/deviation/视觉attention均匀化；有限Table5残余ASR7.4/4.2、FPR升至8%及部分攻击本身变弱，不能称未测adaptive、任意adaptive全失败或零误拒。C.2最低poison率部分undefended ASR0不是防守证明；C.3仅Qwen3VL四scale/三attack，不外推所有模型。攻击正则预算/seed等未完整披露。
- 硬件、precision、batch、输入输出length、concurrency、tailSLO、完整训练/参考校准/attention读取/推理runtime费均Not Disclosed；train-free仅不新增防御训练，不等校准/白盒读取/新增mask kernel/全生成免费。公开artifact与实验未核验或复现。

贡献：输出/像素proxy合理但不能接管模型内部attention干预→架构特定层的visual/prompt ratio参考校准与视觉key屏蔽分责→检测资格、干预效用与跨decode身份要单独验收。2+2+2=6；安全反侧/具体owner差额深入，不因限制减分或假排除。

## Actual owner 与相邻交接

ROADMAP sole `PLATFORM-SECURITY`，`books/part-06-ai-infrastructure/72-security.md`。作者完整实际读65–101：trigger neighborhood→BackdoorAgent standalone sensor76→strength/poison/direction→联邦及风格trigger→Collusive；965–985独立前端/RTD→whitebox sensor/bypass，均尚无visual/prompt perhead参考分布→last-layer visual key union→later decode mask的具体差额。Ch71开头tenant identity、Ch73开头release/recovery与Ch23多模态token/pruning交接已读；不在Ch23重复安全算法，不把Ch73生产门当原文证明。拟在Ch72原76之后、semantic-body-binding前插入下面两段，另加唯一静态来源注；正文完整邻接与末注待非writer实际POST，不由PRE授安全终态。

## 两段逐字 PRE

输出概率或像素变换仍是便宜的第一层筛查；若可疑适配产物已改变多模态融合，而防守运行时仍能读取并控制目标模型的 attention，可以把检测读出与干预另分为两步。一条受限分支先在按架构定位的融合层，为当前解码 query 计算各 head 的视觉 attention 总量与 prompt attention 总量之比，拼接多层特征，按干净参考的逐维均值/标准差形成偏离分数，再以参考分位校准告警。越界只提出屏蔽建议：在最后检测层，将任一 head 高度关注的视觉 key 取并集，给后续层与未来解码这些位置的 logits 加负偏置。这里的屏蔽是改变 attention 参与，不是物理删除 token、缩短序列或释放 KV；已经进入早层 hidden 的图像信息也没有被重算清除。高 attention 不是恶意语义真值，冻结权重更不保证干预后的任务功能不变。<!-- source-family:SF-2026-ARXIV-2603-12989 -->

[CleanSight 的有限证据](https://arxiv.org/html/2603.12989v1)限于可疑 adapter/LoRA、可控白盒 runtime 和所测视觉触发任务，不能继承为任意权重污染或所有自适应攻击的保护证明；它确实测试了三类针对检测信号的自适应正则，但仍有残余攻击、误拒与 clean utility 下降，oracle detector 下的 poisoned utility 也不是完整运行时验收。因此 model/adapter revision、选层、prompt 与视觉 token 布局、干净参考和跨 decode mask 身份应共同固定，这是工程验收要求而非论文已给出的完整接口；分别测检测误差、干预后的目标行为及良性任务损伤，不凭无告警或低 ASR 放行。参考采集、attention 读取/校准、mask 与全部生成均计费，未披露的部署配置和尾延迟不回填为免费防线。参考失配、合法视觉信息被屏蔽或接口无法可靠执行时，保留原概率/像素筛查、可信未污染模型与产物隔离、独立输出/effect gate，不由 sensor 自签安全。<!-- source-family:SF-2026-ARXIV-2603-12989 -->

## 静态本人注 PRE

- SF-2026-ARXIV-2603-12989：本17补03/16；必要 exact-v1 §3–5/Eq1–12/Tables1–4、A/B/C/Tables5–7。只采架构特定 visual/prompt ratio 参考校准与后续视觉 key 屏蔽分责；屏蔽非删 token/释放KV，早层污染未逆转，高 attention 非恶意真值，adaptive残余/误拒及效用反退、oracle PU与完整费用边界保持。不认证全部配方、通用安全或生产SLO，未核artifact/复现。

准备完成，定向送 root 独核必要Source/actualowner/两段及静态注PRE；reader 不重复。未写未POST，不授DAY。
