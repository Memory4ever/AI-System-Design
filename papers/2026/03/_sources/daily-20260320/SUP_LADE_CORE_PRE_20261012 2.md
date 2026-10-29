# LaDe17965：从平面成品到共同去噪的可编辑层

root唯一必要准备；原2+2+2=6/date复用本日有效准入，不自授独核/Books或DAY。实际exact-v1 HTML §3.1–3.4/Eq1–3、§4/T1–3/4.1–4.2/§5，直接支持与反侧足即止；不全附录/图像、代码或复现。

## 有限支持与反侧

[原文](https://arxiv.org/html/2603.17965v1)将full composite与N个RGBA层一起去噪；decomposition保持输入composite，噪声只修layers。角色R=0文本、1待去噪、2冻结，层轴F将各层caption与该层关联；冻结条件t=0/角色2与random-layer训练配对，而非部署任意冻结。文本扩展先给Scene/Layer/Type，layout只提议不strict enforcement。VAE有灰背景alpha-blend输入/冻结RGBencoder、只改RGBAdecoder以及全RGBA encoder+decoder两分支，不能混成同一固定编码器recipe。

按层数/长宽/area bucketing、去padding的packed序列保边界重建；原文未闭跨sample attention隔离，不由pack签样本独立实现。3–8层训练、2–5层有限评价；不是不受限层数。11B/56层/24heads、256H100，512自然图32/GPU到1024八层1/GPU，private8Mdesign/1.5Mvector/2Mlayered/80Mnatural；无matched-data/budget新接口唯一因果。

500Crello生成T1两VLM judge高于先T2I再I2L，但one-step仅单框架不是一步denoise。同PE且I2L另内置caption，training/准备不同，不能当纯接口因果。T2四/五层PSNR29.94/28.42低于30.14/29.49，RGBL1 5.67/7.38差于5.02/5.12，二/三层judge3.21/3.16低于3.56/3.40；生成judge、复合重建像素与编辑层结构分验。T3固定/变层count的100prompt改善很小无不确定性；RGBA改变judge方向而非普胜。高VRAM与PE质量波动原限制明确，无完整precision、steps、latency、concurrency或SLO。若采用强层数/可编辑一致/净性能，只一次请求实际层域/重建容差/完整预算，不在当前有限分采中授这些桥。

## actual owner及最小PRE

actual Ch24完整120–145内部latent人口→路径诊断、205–253编辑条件/状态/flow，以及检索全章未有RGBA/layered生成接口；Ch23表示和Ch25预测状态入口只作handoff。sole `MULTIMODAL-GENERATIVE-PARADIGMS`，不是新设计应用chapter。拟原SF2603-12245完整latent-budget两段之后、SF2602-22122路径诊断之前两段；不改旧有效分支。

### 正文PRE 1

内部计算人口之外，输出也可以从一个平面成品扩展为可分别编辑的层。先生成整图再分解在复用既有生成器、缺少分层训练数据时合理；若希望文本直接指定层内容，一条受限分支把合成图与多张RGBA层作为共同去噪对象，用层索引关联各层文字，再把文本、待去噪层和冻结条件区分为不同角色。给定整图时只去噪其余层，生成时则共同预测；哪些状态可冻结应在训练中出现，而不是部署时任意改变消费协议。共同Attention提供跨层交流，但层说明仍是条件提案，不保证布局、独立编辑或alpha合成必然正确。<!-- source-family:SF-2026-ARXIV-2603-17965 -->

### 正文PRE 2

[有限分层生成对照](https://arxiv.org/html/2603.17965v1)以层数与尺寸分桶、去padding打包来改善资源利用，仍需保留重建边界并验实际样本隔离；RGBA编码适配、文字扩展、各层codec、联合训练和去噪均计费。训练3–8层、测试2–5层不能批准无限层数，单框架也不是一步采样。生成judge较好不代表分解质量普胜，更多层的像素重建仍可反退，因此合成保真、层内容/顺序和后续编辑须分别验收。提示规划波动、显存或层结构失配时，保留平面生成、先生成再分解与较少固定层；不要用联合生成名称替代可编辑性和完整成本证据。

### 静态注PRE

- [LaDe2603.17965 exact-v1](https://arxiv.org/html/2603.17965v1)：必要§3/Eq1–3、§4/T1–3/4.1–4.2/§5。仅可变层共同去噪与层/角色条件接口；保两VAE分支、训练/测试层域、decomposition反侧、judge/像素/编辑分验、pack未证隔离与全部费用。无无限层数、精确合成保证、一步采样或生产SLO；未核artifact/复现。<!-- source-family:SF-2026-ARXIV-2603-17965 -->

请作者非准备者只必要原证/actualowner/两literal/static独核；未root授窄锁不写，非writer actualPOST前不计I，不授DAY。

## resume_mar17 非准备者有限Source / owner / PRE裁

2026-10-12仅本20独立恢复重读AGENTS/适用合同/ROADMAP/本日停点后，实际exact-v1 §3.1–3.4 L91–134/Eq1–3、T1–2 L135–148、§4 setting/metric/baselines L149–166、§4.1–4.2/T3 L167–186与§5 L187–190独读；当前abs同三作者单v1、Comments仅18页，无具体修订/撤回说明，不扩附件或全部图像。原6/date准入有效复用。

L93–95确为合成图与层共同生成/给定图只去噪层，L119–127的F/R轴将层说明和三角色绑定，冻结t=0/R2在训练随机条件出现；layout不strict enforcement，不能认证任意冻结或布局正确。L99–100两VAE分支、L130–134按N/尺寸分桶及packed边界明确，未披露跨sample Attention隔离。T2独立读回四/五层PSNR29.94/28.42低于30.14/29.49，RGBL1更差；二/三层judge3.21/3.16低于3.56/3.40，与生成T1较优须分验。3–8训练/2–5测试、数据/训练混杂、T3微小改善与judge方向、LLM扩展/codec/多层去噪全部费用均保留，single framework不签single NFE。

actual Ch24完整117–149输出/内部人口→latent-budget→路径诊断及207–251编辑条件/轨迹局部读回，Ch23/25当前入口只交接。已有内部latent预算与编辑条件机制不承载共同RGBA输出/层角色条件协议，唯一MULTIMODAL-GENERATIVE-PARADIGMS差额成立。原两literal/static逐字有限Source/actualowner/PRE PASS；只采用可变层共同去噪与训练角色条件接口，不授无限层数/独立编辑/alpha严格正确/pack隔离或完整recipe。须root唯一Ch24窄授权，再写后一次非writer actualPOST，当前不计I/DAY。

## resume_mar17 sole授权后的实际writer

root在ATHENA同章actualPOST接纳并释放后授本family唯一Ch24窄锁。作者只原两literal/static写入，当前正文137/139、自注2535；实际完整127–153及2527–2535本人/ATHENA/19939相邻静态注逐字回PRE读回，原latent预算→可编辑输出层→路径诊断衔接准确。限定diffcheck0、body及static两marker唯一，未改其他family，不把writer自读当非writerPOST。交resume_review17_18一次实际完整局部与末注POST；root接纳前不计I/DAY，不改静态注过程身份。
