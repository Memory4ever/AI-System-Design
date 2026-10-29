# 19209：冻结视觉编码器的目标—接口分责

resume_mar18 sole准备，仅03-21补BJT03-20。完整题摘/有限准入独校有效：分类初始化排序不能验下游grounding→匹配初始化、dense objective与connector/geometry替代对照→重新考虑冻结视觉接口的选择与诊断。拟2+2+2=6，只给替代接口及有效边界，不为借用SSM或分类不等定位旧原则加分；因actual差额定点深入。

## 身份与日级归属

实际[official exact-v1](https://arxiv.org/abs/2603.19209v1)及[current](https://arxiv.org/abs/2603.19209)完整题摘/header/history：Shang-Jui Ray Kuo、Paola Cascante-Bonilla，只有v1、comment仅项目/代码，没有具体先公开/纠错/撤回信号。实际curl [DataCite原JSON](https://api.datacite.org/dois/10.48550/arXiv.2603.19209)：findable/version1，Submitted2026-03-19T17:56:32Z、Updated2026-03-20T01:19:46Z；Available只2026-03，created/registered03-20T02:31:11/12Z。沿本批官方公开/登记夹证限定BJT03-20推断，不把submitted当公开、不补精确公告或无其他先稿声明。

## 最低充分必要原证

实际[exact-v1 HTML](https://arxiv.org/html/2603.19209v1) §2.1–2.4/3.1–3.3/T1–4、§4.1–4.6/T5–6、§6、A、B的stage定义/49vs196直接反侧与G1–2费用口径。必要支持/反侧已足，不遍全部H库存/所有linear probes/图像、代码或其他SSM稿；未复现。

冻结vision，Vicuna7B与connector训练、LLaVA665K/固定seed/batch-order、4H200/BF16/一epoch共同recipe；IN1K224/196token是主匹配对照，但不同width/stage/参数规模仍不等纯结构唯一因果。dense阶段geometry/token长度不同，不能把该组叫perfect matched architecture，平均按benchmark样本加权非联合全部通过。VMamba聚合优不等全部任务：T1 VizWiz、TextVQA有更强切片；SSM大规模亦反退。Pearson与定性空间图不识别空间信息唯一因果，作者分类objective-overfit仅解释，非证明vision encoder无错。

§4.5的3-layer connector与square512是可比较接口分支：更强connector能恢复部分ViTDet/VMamba-T，却不能修复VMamba-B；square时同时改变resolution、token数与aspect geometry，不能唯一归因square或LLM utilization。VMamba-S小退，T5更强connector的VizWiz/TextVQA与T6 VMamba-B OCID-Ref反退；合并两策略非普遍单调或两瓶颈正交识别。B中196token可改善grounding但MambaVision的VQA低于49，stage与数量同变，不授统一最优取层。A单固定seed不是训练重复/置信区间。

G只单GPU/synthetic batch1/text128的完整multimodal forward，100warmup+100均值不是完整AR请求/tail/SLO；图x是首OOM非实测peak，未披露具体GPU/全推理precision/concurrency。vision-stage更渐进不认证全VLM显著加速，LLM往往主耗时。dense预训练、换connector训练、feature存取、更长token与多配置选择全部付费；不采全部强CLIP/SSL或真实生产等价。

## Actual sole owner差额

重载Books上下文/ROADMAP，实际Ch23 71–119完整projector/跨encoder映射→可恢复/可访问/可表达→classification局部counter→head重组，Ch24开篇交接已读；Ch22通用SSM state不接管视觉consumer。唯一 `MULTIMODAL-REPRESENTATION`/[Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。现103/105的probe与109的classification/grounding反证已真实承载旧原则，不为其重造diff；尚没有冻结checkpoint下分别改connector capacity和输入geometry的替代诊断与分责。拟109分类/聚合错配完整段后、重组classification head前one PRE/static，不新增SSM章或排行榜。

## one literal PRE（未授权写）

选择冻结视觉编码器时，还应把预训练目标与下游接口拆开：在相同分类初始化、视觉token预算和语言训练设置下比较不同backbone，再单独检查dense任务适配；后者若改变分辨率、取层或token数，已经不是纯架构对照。定位崩溃也不能仅由encoder家族命名来解释：可固定checkpoint，分别扩充connector或改变输入几何，比较哪些任务恢复。[受限冻结视觉对照](https://arxiv.org/html/2603.19209v1#S4.SS5)中，更强connector并不修复所有模型，方形输入同时改变token预算，部分任务还退步；这些分支支持接口诊断，不唯一识别“信息未传出”或“语言侧不会使用”的内部原因。dense预训练、连接层重训、更长视觉序列与配置搜索都付费，单次forward计时不等完整生成请求。质量或预算回归时保留原encoder、原connector/geometry与专用dense读出，不由更高分类准确率或更小backbone批准通用空间能力。<!-- source-family:SF-2026-ARXIV-2603-19209 -->

本人静态源注逐字：

- 2026-03-21 source supplement — [Do VLMs Need Vision Transformers? exact-v1](https://arxiv.org/html/2603.19209v1)：必要§2–4/6/T1–6、A/B相关stage反侧/G费用口径已审；仅冻结checkpoint的目标/connector/geometry消费接口分责，保token/scale混杂、各任务反退、单seed、单forward与全部训练/搜索费用；不授SSM普遍优、内部瓶颈唯一因果或完整请求加速。未核代码/复现。

交root非准备者必要Source/date/actualowner/PRE有限裁，未锁未写未safe；Source/PRE不是作者自签。有效通过再root协调sole窄写及一次nonwriter完整局部/静态注POST。

## root 非准备者有限 Source / PRE 复核

2026-10-12：实际打开官方exact-v1 abs（仅v1，未见撤回/纠错），HTML §2.2–2.4、匹配设置/T1–2、dense对照说明、§4.5/T5–6、B stage定义/对照及G.1–2完整forward口径；另实际读Ch23诊断段及109分类/聚合错配、111分类头重组和Ch24开篇。有限PASS：上述one PRE与静态注可采用，仅给固定checkpoint下connector/geometry诊断分支，不采用H1/H2唯一因果、全部任务修复、SSM普遍优势或完整生成加速。T5存在TextVQA/VizWiz反退，512同时改token及几何，G为synthetic batch1/text128的单forward；这些限制已进入原PRE。准入与6分按实际接口增量而非旧分类原则成立；日期沿原packet公开/登记夹证限定03-20推断，不补造公告。未重读无关H库存/代码，未复现。Source/PRE通过不等实际写入或日报DAY通过。

## root 实际非写入者 POST

2026-10-12：实际顺读Ch23 99–119完整局部（新111段，前接classification/聚合错配，后接分类头重组），实际末五行含本family静态注，逐字回对原PRE及上节原证。有限PASS：接口诊断而非内部因果保证、token/geometry混杂、各任务回归、单forward及费用/原方案共存近文完整，原段保持，无机制正文出现在Review notes后。接纳为实际整合，释放Ch23的19209窄锁；可同步52安全＝44实际整合＋5具体已有覆盖＋3中心争议，未授日报DAY或全年完成。

## sole writer 实际落实（待 nonwriter POST）

root授唯一Ch23 one literal/static窄锁后，resume_mar18仅插新正文111（原classification聚合错配109后/原head重组113前）及最后本人静态注；其余旧论点/他family完整保留。作者actual顺读99–119完整两侧及末五行，正文/static逐字回批准PRE，marker与本人链接各唯一，限定gitdiffcheck无报错。一次不匹配短行的patch验证失败未修改文件，随后用实际完整段落anchor窄补；最终正确一次正文/一次注。不计安全或日报DAY，等待root一次nonwriter完整邻接/staticPOST。
