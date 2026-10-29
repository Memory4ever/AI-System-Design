# 12717 / 12553 / 12433 必要Source与唯一owner逐字PRE（待独核）

仅本17新增03/16自然日；三家族完整exact-v1题摘已分批独核，日级首arXiv夹证字段分别在本批SUP_DATACITE原件；全2026 Daily精确ID/完整题名定点去重未见有效同事件处理，不继承旧date-only/done。此记录不授Source/PRE通过或实际写入。

## 12717 内部CoT实体引用 / MULTIMODAL-EMBODIED-VLA

[exact-v1](https://arxiv.org/html/2603.12717v1)作者实际必要§III–V/L105–249，reader此前独读相关机制/关键反侧可有效复用。2+2+2=6，具体安全反侧深入。攻击前提为可读写内部text channel（IPC/middleware/network compromise），不是只持外部prompt；两pass先生成clean CoT再重新注token IDs257153/154/155。clean重注仍有最大action差.024，不能称完全无差干预。固定DeepThinkVLA2.9B/PaliGemma、LIBERO40任务×20episodes×3seeds=2400/condition，七类扰动；50%随机/padding/shuffle/antonym/spatial和Llama70B生成错误计划在聚合上弱，实体pool29一致替换95.4→87.0，Goal变化大。任务配对40/Bonnferoni7与作者CI保留，不能把局部零效应当无计算作用。100%随机替换Goal下降16.5pp，整体5.3pp，剂量是random不是entityswap。Llama生成plausible错误并非最强自适应攻击。OpenVLA-OFT没有同CoT接口、clean任务能力也不同，TableIII不能控制architecture差异后证明‘reasoning普遍致脆弱’；GR00T/Cosmos仅motivating未测。作者‘唯一剩余attackvector’不采用。

H100180jobs约2.3h/每job与Llama70B额外费用、两forward局部1.5+.1s不等生产延迟；precision/batch/concurrency/SLO Not Disclosed。实体validator只有30 traces/30命中/1FP，非独立或adaptive防护评价。artifact/复现未核。采用仅内部text实体接口的局部选择性反证与评估分责，不采保证防御。actual Ch26 954–980外部prompt持续控制→EmbodiedAbstention与Ch25/27交接已读；旧prompt语义/wholetrajectory不承载内部entity trace integrity。唯一Ch26，拟原source-binding2606.12978后、Abstention前两段：

外部instruction未变，也不能证明内部语言计划与场景对象仍对应。若action decoder消费一段可被middleware截获的CoT，攻击者可以保持观测和任务指令不变、只替换计划中的实体引用；文本来源于本模型并不赋予传输后的内容可信身份。一个受限诊断先生成clean计划，再重新注入不同扰动，比较整段闭环结果；应把内部channel写权限、重注接口、entity对应及policy revision分别固定，而不只验入口prompt。<!-- source-family:SF-2026-ARXIV-2603-12717 -->

[DeepThinkVLA的局部反证](https://arxiv.org/html/2603.12717v1)中，实体替换比若干机械/LLM改写更损害LIBERO任务，其他扰动的弱效应并不证明CoT普遍无用或实体是唯一安全条件；无CoT模型也没有同一个可攻击接口，不能据此归因所有architecture差异。保留并核对plan与当前观测的实体身份是系统推断，不是已证实防线；额外grounding、重放和检查付费，30条validator试验不授未知攻击安全。身份/观测无法核对时交回独立controller、短chunk、重新感知或人工复核，不因计划流畅批准物理effect。<!-- source-family:SF-2026-ARXIV-2603-12717 -->

## 12553 StructVLA / MULTIMODAL-EMBODIED-VLA

[exact-v1](https://arxiv.org/html/2603.12553v1)作者必要§3.1–3.3/L98–131、§4.1–4.4/Tables1–4/L157–222、B.3/L303–332实际读。2+2+2=6，具体目标选择/训练部署差额深入。离线EMA动作速度的每episode高低阈值、gripper flip settle后最后准静态帧、低速window转折与min-gap/fill取L2动作变化小帧，只是运动proxy，不认证真实contact。GPT5.2仅离线按固定prompt过滤taskirrelevant/redundant候选；不等无label费用/零误差。Stage1预测视觉离散structuredframe；Stage2同planner转换为FAST action-only CE，历史obs/actions交织，§3.3与B.3部署只返回actionchunk，不支持‘线上先生成frame给独立控制器消费’。附录实机first2actions/chunk、server4090/Flask与同步两camera；不把一般controller集成证明安全。

UniVLA8.5B/Emu3VQ8×/FAST1024、模拟LoRA32，stage1/2 camera/resolution/batch/steps改变；实机4H100两阶段各约3h full-parameter，effectivebatch32，第二阶段增加wrist，Franka4pickplace1152demo+tidy648、每task10trials。Table学习steps相同batch不计先视觉阶段总compute；Table1 Eggplant低于部分baseline，LIBERO并非全suite胜。作者零样本物体/人工扰动局部成功不授physical safety/普遍鲁棒；seed/uncertainty、precision、inferencebatch/concurrency/tailSLO Not Disclosed。C.1/C.3的short-history重复已完成动作与articulated hinge动作/gripper事件失配，以及windowaugmentation时间偏移是必要反侧；B.3另支持实际部署。未核artifact/复现。

actual Ch26 443–470 Training-only Foresight→FRAPPE/MTWAM等完整论点与Ch25/27交接已读；现futureteacher/feature/change监督没承载‘以gripper/运动里程碑选择视觉目标，再同backbone转action-only’分支，唯一Ch26，不把非持久训练目标迁入Ch25worldstate。拟前三段后、FRAPPE前两段：

训练期未来目标还可以先按运动事件选择，而不是均匀预测每帧。一个离线分支用动作速度平滑、gripper状态变化与短暂停顿找候选里程碑，再由VLM过滤重复或任务无关帧；这些帧是监督target，运动信号不等真实contact标签，过滤器也不拥有环境真值。先训练同一生成backbone预测这些视觉token，再把目标换成基于真实obs/action历史的action-token预测，迁移的是训练形成的表示，不必在线物化一条未来video计划。<!-- source-family:SF-2026-ARXIV-2603-12553 -->

[StructVLA的受限机制](https://arxiv.org/html/2603.12553v1)因此不能被写成线上生成subgoal已交给独立controller：实际部署返回actionchunk，离线筛选和两阶段训练仍付费，等action训练步数也不等总预算。事件proxy对关节式连续运动可能失配，短历史还会重复已完成动作；有限LIBERO/Simpler与每实机task10次不授普遍鲁棒或安全。目标、camera或闭环质量漂移时保留原均匀future监督、direct policy、较短chunk与已验证controller，以真实反馈决定继续，而非由预测里程碑授权执行。<!-- source-family:SF-2026-ARXIV-2603-12553 -->

## 12433 Foundation VFM Stitch / MULTIMODAL-REPRESENTATION

[exact-v1](https://arxiv.org/html/2603.12433v1)作者§3/L123–168、§4–5/L169–216、§6 VST/L219–241、A2/A3/L334–364、B1/B2/L367–384、B5/L460–487必要方法/eval/直接反侧实际读。2+1+2=5，具体consumer功能与局部反证差额加深。Source prefix与target suffix冻结，只训练stitch；LFM中间lowL2不保证穿过冻结target后的finalpatch功能。FFM对齐最后prelogit patchfeatures，再TLT两阶段；浅层直接TLT失败、FFM初始化改善，不授所有模型层与最优stitch。Self-stitch相同adapter/切点/loss/data对照排容量替代解释，任务改善只是受限经验互补，不证明普遍semantic fusion。CLIP弱source对较强target局部不能补缺失信息。VST共享前缀+deepbranches，54%由层数proxy而非实测墙钟/GPUmemory；main Qwen3B与A3Qwen2.5-3B以实际附录身份限定，不回填Qwen3。

fMoW均衡14260/1612、iNat21200/5300、Aircraft标准split、ADE20K lineardecoder；无augmentation，AdamW100epoch/patience5/LRgrid，LFMbatch256其余128/BF16；MLLM558k+665k一epochbatch64/TinyLLaVA。硬件、独立seeds/uncertainty、latency/batchconcurrency/SLO Not Disclosed；冻结参数仍需穿target反向/预提取/匹配数据与调参，不能当zero-cost。未核artifact/复现。

actual Ch23 63–99 encoder/projector与707–721一般alignment、Ch22/24交接已读；已有geometry/map与producer→consumer选择未承载中间LFM≠final suffix function及samecapacity self-stitch反证，唯一MULTIMODAL-REPRESENTATION。拟encoder/projector基本约束段71后、多语种latent-map73前两段：

若接入点位于另一冻结encoder的内部，接口还要通过其后续层，局部feature误差低不等于最终消费者兼容。可以只训练连接层，先让拼接后的final prelogit features接近目标模型，再按目标任务fine-tune连接层；这与只在切点匹配feature是不同objective。冻结后缀仍传播梯度，浅层的长固定变换可能使直接task-loss训练困难，final-feature初始化只是可比较分支，不证明任意两个encoder都可互换。<!-- source-family:SF-2026-ARXIV-2603-12433 -->

[有限VFM stitching对照](https://arxiv.org/html/2603.12433v1)还在原模型同切点插入相同连接层，区分新增容量与跨模型信息；弱source不能自动恢复target所需信息，任务改善也不认证全域语义同一。训练、冻结后缀反向、数据及新任务回归均计费，多个视觉分支共享前缀的层数估算不等实测latency或显存节省。消费者质量退化、层位失配或总费用不合算时，保留原完整encoder、独立分支与简单projector，不由局部L2或共享层数批准无损替换。<!-- source-family:SF-2026-ARXIV-2603-12433 -->
