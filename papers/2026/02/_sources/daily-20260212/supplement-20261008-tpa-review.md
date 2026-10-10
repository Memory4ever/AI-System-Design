# TPA：必要命题及公式反侧，待实际Source

原件 https://arxiv.org/html/2602.09757v1 ，完整AB/date已root实核。拟2+2+2=6；classification证书不处理AR前缀改变→区分任意token不变stability与具名harmful token/phrase不可达validity，按prefix与aggregation粒度定义威胁→重新选择认证对象及其在线代价。公式矛盾触发定点深入，非对整份附件重读。

已读§3.1–4.5/Algorithm1/Defs4.1–4.7/Prop4.5/4.6、§5.1–5.4/Tables1–3、AppendixB相关proof与AppendixC配置。威胁只post-training数据symmetric-difference预算，disjoint shards each独立训练，改变一个点可使一shard任意投票；不涵盖预训练基础模型已后门、共享组件受攻或任意推理prompt攻击。固定deterministic tie-break和共同prefix需明确；第一token的票差不能直接授后续全链。

采用最小范围是认证对象/前缀/粒度/执行代价的分工，不采用所印exact TPA求值或collective MILP保证。直接反侧：Def4.7/AppB目标max统计margin被破坏的prompt数，却Theorem4.8将该值直接解释为remaining safe比例；R_j piecewise印为非target投票不可改变、target可变，proof文字却说target票已无法利用，条件相反。源尾proposition4.5以固定prefix的最小单点radius跨AR序列，其proof把『存在一次位置攻击』与『任意攻击至少预算』混写；只保留需联合前缀条件，不把未经闭合的proof批准为安全验收。AppendixB未消除这些印刷矛盾。明确恢复条件为一致目标/可变shard条件/边界定义与完整证明或官方勘误；此子主张隔离，不抹掉其他准入增量。

§5 Toucan50k/150tools/500shards/OLMo2-1B LoRA，Full vs Last3改变适配容量与accuracy67→54、radius249→163；单L40逐模型推理0.3→150s，平行回0.3s只是作者预期、非等硬件实测。HH-RLHF20shards、OLMo1B/Gemma2-2B/Qwen1.5-4B；stability T.25与validity T.15不同不直接合并。指定unsafe字符串/前缀是测量人口，不能认证任意有害语义，first-token/finite-horizon不是动作执行安全。Table3经验10%指定数据攻低AS不证明worst-case公式；模型特定8/4bit量化、LoRA和训练steps需分别看，不照录通用生产保障。未运行代码/复现。Source后才核PLATFORM-SECURITY当前owner的具体差额，尚无写锁或Books判断。
