# Nov20 SAM3D Body 必要原件恢复与采用边界

## 1. 原有效事件与本轮最小恢复

作者Noether；Nov19机构日期与完整AB由Ohm§3/root有效核，不重该日门；root当前97/132不含Nov20。原机构已披露MHR分离skeletal structure/surface shape、单图encoder-decoder及2D keypoint/mask提示，有具体表示/消费接口潜力，不能因后Feb2026 arXiv编号整项关闭。原Meta PDF本轮一次native GET零bytes/SSL timeout，未重试；[2602.15989v1](https://arxiv.org/abs/2602.15989v1)只是后来精确身份/ToC，**本包没有采用其未来正文、训练配方或评价结果**。

本轮必要恢复只读官方`facebookresearch/sam-3d-body`当前README定位具体原artifact，再GET commits一页13项metadata，不读13次差异或全部代码。读到初始commit `4e33ae485b2ea0ecc38328fa39b16b75dd3e79c0`、原committer字段Nov19 15:54:47UTC；此字段是代码历史，不独立证明公开时刻。当前README包含后来Feb19 add-arXiv等，不能全部回填Nov19。

## 2. 真正取得及实际阅读

初始README raw一次40秒0bytes timeout，官方GitHub该精确blob的web返回cache miss；随即同一已知commit的Contents API一次GET成功，原件`SUP_BODY_INITIAL_CONTENTS_20261015.json`包含base64，已解码实际完整读README。它明确原Nov19 launched/date-only、原BibTeX为`identifier to be added`，所以不是把现在2026引文冒成原件；原README已有MHR、提示和六个checkpoint指标表，但没有这些数值的split/原baseline/提示人口等完整评价协议，不采用“strong generalization/SOTA”作结论。

再只GET同commit recursive tree（139 path metadata，truncated false）定位两个具体文件，而非通读139代码。已实际静态读`mhr_head.py`完整必要1–369和`prompt_encoder.py`1–256，原件分别`SUP_BODY_INITIAL_MHR_HEAD_20261015.json`、`SUP_BODY_INITIAL_PROMPT_ENCODER_20261015.json`。没有安装、加载权重、执行代码/测试或验全repo。

MHRHead在该精确代码将pose、shape、scale、hands分块预测，`mhr_forward`将shape与model parameters作为独立输入给MHR，mesh、joint state/keypoints分别输出；rig参数冻结并不证明预测几何真实或任意shape/pose统计独立。forward把face输出乘0、全局translation先置0，另有单位/相机轴转换，不能从“full-body”推全部自由度都预测或测得。这里不采维数为普遍rig标准，不由函数存在签通用兼容或物理身份。

PromptEncoder实际对归一化2D点加joint-specific embedding并区分not-a-point/invalid，mask有独立下采样和no-mask embedding路径；当前读取只证明这些静态接口/实现文本，未读主decoder消费和训练prompt采样，不能把“支持mask”当所有checkpoint/模式的已验行为或把用户提示当3D真值。

## 3. MHR 辅助文档的晚一天角色

因Body原README已直接引用MHR，为核接口另一次`MHR/commits?until=2025-11-19T23:59:59Z&per_page=1`取得`56564c717a1862e93037c344080e60cc5bbf5713`，原committerNov19 23:47:27UTC实际为Nov20 BJT。相应README Contents响应已实际读，含shape/model/expression不同输入与LOD1限制；**它不是Nov19 BJT原件**。随后把边界正确收为Nov19 15:59:59Z的一次metadata查询，返回[]；这只表示当前该git历史过滤无返回，不证明MHR当时未公开或Body无法使用它。停止继续挖完整历史，不用空数组或后稿消解原官方Nov19披露。此辅助文档不作本窗新增事件或当日完整机制证据。

## 4. 当前未决而非完成声明

原机构/精确初始artifact足以继续保留“参数化骨架/表面shape分开、提示引导单图恢复”的贡献潜力，不因访问受阻改C。拟2+1+2=5只针对该受限表示接口，尚待独核；没有用作者SOTA、模型规模/性能数字加分。

决定采用长期机制仍缺：原完整必要报告中这种分离的构造/监督和直接反侧、prompt消费/纠错有效性与评价人口，以及其相对既有rig/mesh或条件估计具体改变什么选择。已得静态head只能核接口，不能替这些证据；因此此刻不宣Evidence完成、已有覆盖或Books整合，也不因未来全文可读就倒填原Nov19结果。没有为Books缺少MHR名字制造缺口；仍需在该具体命题充分后作唯一owner比较。

本轮原件恢复已有限覆盖官方publication/download、官方repo当前→初始commit README/两必要文件，原失败不循环重试。可接受替代是对应原报告稳定官方副本/可核Nov19版本、原训练/评价说明或能明确绑定该原版本的必要补证；只重上述命题与相关owner，不展开全部checkpoint、全dataset或Feb2026全文。

## 5. 交 reader 的具体请求

请root转Ohm实际核这次精确初始artifact身份/必要静态接口、两次MHR边界角色及当前缺口是否已可安全隔离；若还有原件中可直接执行的必要入口，请指出具体域继续，不把尚未核主decoder冒外部不存在。当前本项还是作者准备层，未将它计作已完成受阻终态。SAM3/S2ST全闭合不重，Objects逐字PRE已保存待核；无本项书锁、共享State/index写、普通消息或stage/commit/push。

## 6. 主 decoder 必要静态消费已继续读取

随后按已知初始tree只GET同commit的`sam_3d_body/models/decoders/promptable_decoder.py`一次Contents API成功，保`SUP_BODY_INITIAL_PROMPT_DECODER_20261015.json`，已实际完整读1–194。原forward将image embedding展平，逐层消费token/image augment与token_mask，可拼hand embeddings；`do_interm_preds`开启时逐层调用`token_to_pose_output_fn`，`keypoint_token_update`开启时再用当前pose输出更新token。它确认了可选迭代消费接口，而不是证明初始checkpoint确开启每个flag、完整主模型接线或所有prompt路径已运行。默认flag多为false，不能从分支代码存在回填论文recipe/评价。

因此§2所说“主decoder尚未读”已具体补为这一必要文件静态读，但原版本训练/提示人口、checkpoint实际开关及有效性/关键对照仍未取得，不签实现/实验验收。没有跑代码、解pickle、加载模型或请求所有139文件；原报告/必要评价缺口按§4保持精确，作者不会以“有源码”替代需要的证据或将普通可执行接线检查冒外部不存在。Objects已真实写入/Ohm17 actualPOST/root6接纳释放，末注admin已保存交root读回；不重其正文/Source。

## 7. 主调用方真实补读与收窄后的采用命题

按Ohm§19给定入口，一次Contents GET取得同初始commit的`sam_3d_body/models/meta_arch/sam3d_body.py`，保存`SUP_BODY_INITIAL_META_ARCH_20261015.json`，base64解码为2025行；实际只读必要289–516、752–791、1057–1177、1649–1682，不称全文件/全实现核验。原件[精确调用方](https://github.com/facebookresearch/sam-3d-body/blob/4e33ae485b2ea0ecc38328fa39b16b75dd3e79c0/sam_3d_body/models/meta_arch/sam3d_body.py)与已核head/encoder/decoder共同支持以下受限静态接线，不另起新家族或把git时间当公开日。

`forward_decoder`先用learned init pose/camera构造pose token，另把`prev_estimate`映成独立token；点提示经已核joint-specific encoder和projection后拼接。393–439明确token augment分别放上一轮估计与提示，`token_mask=None`，不能把PromptEncoder返回的`prompt_mask`直接说成此调用中实际传给decoder的attention mask；invalid/not-a-point身份由编码分支处理，不签全部无效点严格无影响。后续可选keypoint token/中间pose回调仍受配置约束，不由分支存在授checkpoint开关或训练recipe。

`forward_pose_branch`1057–1150先得backbone image embeddings；只有`MASK_EMBED_TYPE`非空且`MASK_PROMPT==v1`才将`_get_mask_prompt`结果加到图像特征，其他mask模式抛NotImplemented。766–789按mask_score>0使用带score的mask embedding，否则no-mask embedding；这是输入权重，不是校准概率或质量/真实性认证。初次decoder输入dummy -2点，返回的`image_embeddings`保存在output。点提示与mask不是同一个sparse forward，也不是所有模式都支持的统一提示通道。

`run_keypoint_prompt`1649–1681复用output的图像特征/condition，将当前raw pose、shape、scale、hand、face及可用camera detach后合并成`prev_estimate`，但调用明确`init_estimate=None`，再以最后decoder读出更新`output[mhr]`。因此上一轮预测是下一轮可读取的条件token，不是递归数值初值、硬约束或新观测；共享同一decoder读出也不保证单独改shape不会改变pose。这里没有核提示训练采样、不声称改点必然改善误差，故不为不采用的纠错/SOTA宣传扩读sampler、全部评价或Feb2026未来正文。

§4原先把“训练/纠错评价”笼统列为决定一切采用的必要缺域，现在只对那些未采用的强命题保持限制；本次拟采用的最低命题收缩为：**单图rig恢复中，参数化输出的分块、2D用户提示、上一轮预测条件与图像证据是不同接口角色，静态分开不等控制独立或几何真值。** 原机构Nov19披露是本窗事件，初始artifact仅补证这项受限实现；不授完整2025方法/评价已得，也不授各blob当日公开同bytes。

## 8. 实际 owner 比较、5分提案与 reader 请求

实际顺读当前Ch23 native 3D相关1265–1348，重点完整AssemLM两段、3D sidecar/统一mesh-state两段、part geometry/kinematic metadata两段、CRAG与触觉两段。现有正文已覆盖shape/pose分支、模型proposal非几何真值、只读重建与persistent revision的取舍，不能借没有MHR名字造缺口，也不能把一般identity/version原则加分。

尚未承载的具体差额是：**可交互单图参数化重建不必先改成统一几何生成模型；在既有图像读出上，用户2D提示、上一轮预测条件token、独立residual初始化和分组rig输出必须分别解释。** 否则“previous estimate用于refinement”容易误读成固定上一状态做局部数值增量，或把分组head误读成用户独立可控/实测身体属性。初始实际调用恰给出反例，改变的是如何解释/消费估计接口，不是新缓存协议或物理状态管理。唯一owner仍`MULTIMODAL-REPRESENTATION` Ch23；Ch24生成路径、Ch25动力学、Ch26控制闭环不接此静态表示主论证。候选位置可在现完整sidecar两段之后/part codec分支之前，不改前述合理旧方案。

提案`2+1+2=5`：2分是条件/初始化/输出参数职责的具体替代解释，1分只到单图表示与decoder消费组件，不给未核训练/多系统reach，2分是可复用接口边界；不按MHR维数、foundation标签、性能宣传或泛化安全加分。标准必要机制/实现与直接反侧已读到上述采用范围；无受控纠错效果、训练构造/监督新结论、SOTA/吞吐/SLO、代码运行/权重验收。模型/backbone、mask/point编码、每次decoder与rig mesh/keypoint读出均付费，复用图像特征不等零成本；输入点/人体crop/相机坐标或rig版本失配、遮挡导致不可识别时保留原图、可信多视角/专用拟合和人工核验，不用2D提示签3D物理真值。硬件/precision及完整延迟不披露，不填虚构基准。

交root转Ohm：请实际核§7调用方必要域及§8唯一owner差额/5分，判断该受限命题是否足以进入长期段落或应仅报告；不是请求重读已核head/decoder、未来论文或所有139代码。当前只是作者Source/owner准备，不授正式候选/Evidence/Books整合、逐字PRE或写锁；无本项书写入。Objects/SAM3/S2ST的Source、正文、POST、本人注行政均已root闭合，当前不再列待办，不重复通知或改它们notes。Nov20仍未DAY，97/132不含本日。
