# 05817 Consistency Training：必要缺层 / 六分 / actual Ch29最小PRE

作者jun06_continue，2026-10-25。[exact-v1](https://arxiv.org/html/2606.05817v1)。R19完整题摘/Jun05资格/具体贡献准入直接采用，不第三题摘或DOI日证。定点搜actual Books与旧Jun05同ID档案没有已成必要/原评分记录，不从别篇或旧宽池继承分数。本轮评分`2+2+2=6`：设计2为MLP/attention两种内部target及威胁时序匹配边界，reach2为训练目标和部署失效交接，durability2为可复用的target可见性条件；不把借用的一致性原理或安全宣传计分。因拟真实长期gap加深至受影响直接反侧，不由6强制停在摘要。

## 本次实际必要范围

已实际读§3完整方法/公式、§4威胁设置、§5结果/完整cross-threat表、§6机制与§7限制；并为拟采命题定点读D.1/D.3、E.8、H.2.2/H.2.6及I.2/I.3对应文字/表。其他长附录不声称全读；本轮未核图像素、代码或运行复现。源码HTML解析曾因本地bs4不可用，随后同精确HTML用标准文本解析恢复所列必要域，不把环境库缺失作为论文访问故障。

§3两次forward：同基座clean分支禁LoRA为reference，wrapped分支用attention WQ/WK/WV/WO LoRA，MLP权重冻结。共同内容token用character offsets对齐，各层取均值。MLPCT在SwiGLU激活后/down-projection前h作cosine距离，AttCT对每head/query的attention源位置分布作JSD。MLP target不等更新MLP参数，attention map相近也不等生成分布相同；新增全层target驻留、成对前向/梯度与位置映射成本，LoRA参数少不是零费。

§4/5同一评价并非所有model×threat全交叉：sycophancy/jailbreak五模型；persona/frustration限Gemma3-27B；prefill限Llama3.1-8B/Gemma3-27B；conditional三模型。Persona44个/三rollout、训练200pairs+200Alpaca，identity adoption减少可伴benign alignment恶化，不把同一词义“更一致”当safe。D用ClearHarm训练、AdvBench50 OOD prefill对；PAR为相对clean compliance差，不是绝对ASR或未受害概率。不同judge/行为proxy不能拼成统一安全指标。C.3只该persona配置披露A10080GB/QLoRA16alpha32/3epochs/effectivebatch16，不能移给全表。统一hardware/topology、全局precision/输入输出长度、各威胁所有batch/seed/独立CI/完整训练费用未统一披露；线上并发/SLO在此不适用，不补生产吞吐。

**拟采核心反侧**：D.1/D.3的prefill追加在assistant标记之后，shared prompt按causal mask看不到未来追加内容。若只匹配原prompt内部状态，这个目标并未定位到prefill产生行为影响的位置；clean基座与adapter仍可能有漂移惩罚，不能因论文“bitwise identical”措辞宣布任意训练过程中loss/梯度永远为零。本次采用“对干预不可见、不能凭该匹配认证防护”的窄命题。D.3输出级BCT在divergence/response位置对ref作KL并加refusal SFT regularizer；不是与纯internal loss等目标/等成本。不能把BCT组合效果归MLPCT单项，也不将50对的零PAR称完备防御。

E.8多轮rejection轨迹比clean问题多出assistant/rejection位置，不存在逐位置同义clean对应；低loss可收敛到不符合calm policy的状态。§5跨威胁Gemma3-27B表中frustration BCT降低该proxy却提高jailbreak ASR，MLPCT也有负迁移；稳定持续互动和适时拒绝不是同一政策。本次不把作者关于“frustration subspace”的解释升级为所有family因果定理。

§6/H.2.2只Gemma3-4B/300MMLU，affine fit为96对/2560维in-sample，genericSFT控制不是heldout验证替代；H.2.6 patch只在CT答对、base跟错cue的选择子集，不能推所有威胁共享唯一机制。I.2/T15是GSM8K/HellaSwag/TruthfulQA各500样本，部分accuracy有下降，与§5.2“每method/model MMLU/MTBench均±0.02%”的概括不同；不采普遍无能力退化。I.3组合/顺序不稳定改善，不能由方向不同宣称组合必有互补收益。§7明示LoRA/controlledthreat与单基座跨威胁限制、persona-suffix/Anthropic sycophancy未解决。支持与直接反侧足够，停止机制附件，不采精确headline倍率或普遍安全证明。

## actual owner与已有覆盖比较

已读Books三文档/ROADMAP，actual Ch29条件CE/辅助监督与同义变体子空间完整两段、ProCon内部参照段、cue一致性风险完整段及直接两侧；Ch28/Ch30开篇交接实际读。全Books精确ID/MLPCT/AttCT定点检索未找到本family真实正文，不用trace授NC。

现有Ch29已承载reference/module/mask身份、几何proxy非行为真值、cue抑制会误伤有用提示与位置回归；这些可复用而不改。但其尚未解释attention-only更新下的MLPtarget/attentiondistribution target分工，以及当干预发生于matched prompt之后时loss缺因果可见性、多轮新增位置又无clean对应。一般“质量退步”不承载这条时序判断。因此唯一`TRAIN-SFT` Ch29有最小gap，Ch72不重推训练loss，Ch30只拥有LoRA参数化。

## 原两段PRE（未保存Books）

精确拟位：Ch29同义变体子空间第二完整段及`SF-2026-ARXIV-2603-09205` marker之后、cue一致性首句“一致性也可能通过不分对错地降低外部提示权重达成…”之前。旧子空间/旧cue两侧不改。仅在reader首次必要/评分/actualgap/PRE及root本轮fresh新窄授后保存。

配对一致性还可以选择不同的内部读出，而不是把所有hidden states当成同一个target。一条[受限训练分支](https://arxiv.org/html/2606.05817v1#S3)用禁用adapter的基座处理clean prompt作参照，只更新attention投影的LoRA，却在共同内容位置比较冻结MLP的SwiGLU激活，或比较各head的attention分布；前者约束MLP所收到的信息，后者约束来源位置的路由。冻结MLP权重不使其输入与激活固定，两种距离降低也不证明完整输出等价；reference checkpoint、target module、位置对齐、层集合、距离与adapter范围须共同成为训练配置。

Target还必须处在能看见干预的位置：若攻击文本追加在assistant标记之后，原prompt位置受causal mask限制，看不到这段未来prefill；只匹配这些位置，不能由较低内部loss认证后续行为已被修复。多轮轨迹新增的assistant和反馈位置又未必有逐一对应的clean参照，输出级或经核验的response目标是另一条需要独立验收的分支。原文某一威胁改善可伴另一威胁恶化，也不支持把不同target简单叠加；成对前向/activation、轨迹制备、适配与跨威胁安全/良性能力回归全部计费。匹配位置、参照或行为目标不合时，保留普通verified CE、已验安全示范或原checkpoint，不以内部一致性代替部署安全授权。<!-- source-family:SF-2026-ARXIV-2606-05817 -->

本人注拟：`SF-2026-ARXIV-2606-05817` — jun06_continue，Daily2026-06-06补Jun05；R19资格/准入复用，2+2+2=6/唯一TRAIN-SFT Ch29。exact-v1 §3–7、D.1/D.3/E.8与H.2.2/H.2.6/I.2/I.3必要，只内部target与干预可见性/clean对应。保prefill不可见不等永远零梯度、trajectory/跨威胁负迁移、in-sample/选择patch人口与能力表文口径限界；成本/verifiedCE/安全示范退路保正文。未核图像素/代码/复现，不采普遍安全/完整因果；新PRE/窄授/真SAVE/唯一POST按后到事实记，不预I/DAY。

## 既成采用（2026-10-25，仅行政同步）

R20首次必要/正式6/actualowner/原两段PRE通过；root本轮fresh新窄授→A27逐字真实SAVE和完整新增/直接完整两侧/本人注自读→R22唯一非writer actualPOST实际通过。Ch29指定窄位已释放，I8生效；以上未存/PRE拟态仅保历史过程，不再表示本项普通未完。不第三必要或正文，未授全日完成。
