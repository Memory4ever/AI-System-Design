# GLM-ASR-Nano 定点恢复与准入请求

2026-10-02T19:01:02+08:00记录。原始材料已实际读取，不因必要历史版本仍不确定而把可读核心说明标为未读。

[官方文章149](https://www.zhipuai.cn/zh/research/149)原始HTML `time datetime="2025-12-09T16:00:00.000Z"` 对应2025-12-10T00:00:00+08:00，落12/10窗。这只支持文章事件。文章称1.5B，并在脚注排除复用的Whisper音频encoder；同参数规模比较因此必须明确参数口径。潜在反证是具体“1.5B”预算不含音频编码器，不能直接推总部署参数/成本相等。请root校准该局部反证是否构成独立增量；不因版本号或ASR主题本身入池。

核心说明、参数脚注、dialect/quiet声学边界已读。当前架构图显示encoder/projector/GLM；规格图为WhisperV3 encoder（unfrozen）、Merge(k=4)+linear projection、interleaved fusion、GLM-Edge-1.5B-Chat。图URL文件名含2026-01-26，当前可变图不能作为2025原始架构的确定证据。基础模块组合没有独立新增机制证据，不用宏观“轻推理”口号加分。

原始图：`https://www.zhipuai.cn/api/media/file/Gemini_Generated_Image_jkfygtjkfygtjkfy.png`、`https://www.zhipuai.cn/api/media/file/ScreenShot_2026-01-26_142841_677.png`；两张均实际查看。官方[HF模型卡](https://huggingface.co/zai-org/GLM-ASR-Nano-2512)核心、当前config与[模型API](https://huggingface.co/api/models/zai-org/GLM-ASR-Nano-2512)已读，createdAt=2025-12-09T09:07:41.000Z只证明仓库记录创建，不授权重首次公开。current模型卡/图未当历史冻结材料。

官方commits/main有限读取：initial `5c2bacf…` 12/09T09:07:41Z；大文件提交 `05e39c3d75d93b59b077d4f0bfa077329c737d54` 12/09T17:58:59Z；README `a055964…` 18:11:52Z；后续18:12:17、19:07:25、19:08:04Z。提交≠该刻首次外部公开，不靠创建/提交推定性能事件。

2026-10-02T19:31:00+08:00版本纠正：复用Popper19:24实际HTTP200全文读取的[早期固定README](https://huggingface.co/zai-org/GLM-ASR-Nano-2512/raw/a05596423c38f46e7227de4d8d49922e111cc81d/README.md)。固定稿披露1.5B及dialect/quiet边界，**不含当前文章排除Whisper encoder的脚注**；benchmark图片仍链main而非冻结图片。作者本轮HF API及短hash原始路径均有限超时，随后web短路径不可用，不冒称本轮重取成功。确切固定稿采用的是独立复核原始记录的版本比较，不从current脚注反推2025披露。

最终处置：文章事件日期明确，不再隔离其归窗；新增参数口径局部反证保留潜在，但当窗历史披露/实现版本不支持采用，故仅隔离这一命题，不评分、不计第三确定入选家族、不进Books。基础encoder/projector/LLM组合和排行榜没有已识别的独立新增设计，当前图不作历史实现证据。未采用任何ASR收益、部署成本或安全保证，未运行模型。重开只需当窗公开的原文章历史快照/脚注或固定规格证明参数口径；无需再探commits创建时间，不扩模型库存，不删除已发现反证。
