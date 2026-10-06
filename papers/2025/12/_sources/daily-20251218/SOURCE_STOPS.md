# 12/18 原始来源与停止点

实际2026-10-02，含起不含止窗口[2025-12-17T09:00+08,2025-12-18T09:00+08)。本记录是本日本轮原始检查，固定历史目录按精确相邻段复用，不由前日报结论套完成。README十四行保留完整限制。

## 固定目录本窗邻接

- DeepSeek `https://api-docs.deepseek.com/updates`：全文当前2026Apr24→2025Dec1，无Dec17段，末至2024May17、无分页。Moonshot `https://platform.kimi.com/blog` 26项、Nov7→Nov6，`/blog/posts/changelog`持续全文Nov6→Oct27→Sep5至2024，无Next。MiniMax `https://www.minimax.io/blog`12项，Dec23→Oct27，无Next。这些约定目录本窗未发现，不授全网无遗漏。
- Zai `https://www.zhipuai.cn/zh/research?page=2`18项、没有更多；Dec21GLM4.7→Dec10TTS→Dec9ASR→Dec8AutoGLM→Dec7GLM4.6V。ERNIE `https://ernie.baidu.com/blog/zh/`第一页10项，Dec23→Dec9→Nov21，Next2/2；已越窗口不扩旧页。
- Google Research `https://research.google/blog/2025/`第1页本窗邻接Dec18年度回顾→Dec15PaperAssistant→Nov12，年度回顾范围关闭；DeepMind `https://deepmind.google/blog/page/4/`24条Feb26→Nov25。GemmaScope2 Dec19T12Z、GenesisDec18T19Z在后日，UKAISI Dec11T00:06:40.959Z/UKgovernment Dec10T14:59:21.093Z在前日，不整天挪到09点前。实际触发Flash Blog/card/ProFSF见ADMISSION与Books提案。Publications年字段不授日首公开，历史缺口保留。
- Anthropic Research首入口本轮当前10条，Alignment December原始段Dec19Bloom/Activation→Dec16AF→Dec12Audit→Dec8Mask再到November。本窗段没有目录事件，不替全Research。publicationList SSL EOF及网页替代10项原始有限失败已记录，不重探；OpenAI Research当前9条/Loadmore、历史RSS403有限替代同理隔离。OpenAI Dec17精确主题补检的Academy已关闭；[Enterprise报告](https://openai.com/business/guides-and-resources/the-state-of-enterprise-ai-2025-report/)原站403后官方网页工具原文可读，已读Foreword/Introduction与四key findings/方法/impact：企业聚合使用与9k worker survey、correlation与自报时间收益，不新增模型/训练/Agent执行机制或修正技术设计证据，关闭贡献。不照录business数字作技术因果。
- Qwen旧Blog最新Sep23/下一页及明确迁移qwen.ai，迁移后历史动态目录有限失败；HunyuanResearch前端公开`https://api.hunyuan.tencent.com/api/blog/publicList`、`{pageNum:1,pageSize:20,renderType:0}`响应code0,totalNum11，仅2026。不能以当前空历史证明2025零事件，不重探相同接口。
- Seed原`/api/get_article_list_v2`：Blog `article_type=2&publish_year=2025&count=20&page_token=0&order_desc=true`15项，total49/has_more/next20，Dec24SeedProver→Dec18Seed1.8→Dec16Seedance→Dec2GRRL→Nov27/Jul23，已越本窗；论文type1同params18项，total94/next20，前两置顶Seedance/GRRL之后Oct21至Jun25，不能按置顶判新事件。Seed1.8 Blog全文core另见下。

## Meta完整核心及具体增量

首查Research→原始`https://ai.meta.com/global_search/?page=3`24篇/人物/数据/Blog混合段，只处理Dec18四论文、Dec17MSE、Dec16两已知event的精确邻接。不是全站搜索完成。四页完整Abstract实际可读，各Dec18日精度、无独立时区时刻，publisher arxiv，不能把整日公告移入截止前：

- [Unused watermark capacity](https://ai.meta.com/research/publications/we-can-hide-more-bits-the-unused-watermarking-capacity-in-theory-and-practice/)：PSNR/linear robustness下capacity upper bounds与现实缺口、ChunkySeal扩大消息容量→潜在编码理论/训练容量边界，不是简单1024bit数字；精确first-public尚未证实，保留。
- [Post-hoc rephrasing](https://ai.meta.com/research/publications/how-good-is-post-hoc-watermarking-with-language-model-rephrasing/)：控制generation/search/detection compute的posthoc设置→larger model/beam/multicandidates/entropyfilter的quality-detectability取舍；代码验证比开放文本更困难→保留可验证文本适用边界，不作全语义保持保证。
- [DistSeal](https://ai.meta.com/research/publications/learning-to-watermark-in-the-latent-space-of-generative-models/)：pixel posthoc成本/artifacts→latent watermarker蒸馏到generative model或decoder跨AR/diffusion→具体执行机制潜力，不采用无配置20x。
- [PixelSeal](https://ai.meta.com/research/publications/pixel-seal-adversarial-only-training-for-invisible-image-and-video-watermarking/)：MSE/LPIPS perception proxy及多目标不稳定→adversarial-only、三阶段解耦、JND highres adaptation与train-time inference simulation/temporal pooling→训练/评价机制潜力，非“invisible”普遍安全证明。
- [MSE Lidar](https://ai.meta.com/datasets/meta-synthetic-environments-lidar-dataset/)已读Overview/Dataset/Acknowledgement。原页DEC15而目录Dec17，不同事件日期不补时刻；是full lidar transients近100kASE渲染与对应ID的数据发布，支持depth/occlusion/material。当前event未增foundation model/训练系统机制，仅传感器/领域数据，范围/贡献关闭。原paper是Shoot-Bounce-3D、SIGGRAPHAsia2025，不把索引date改成新论文首发；不扩科学应用。

SAM/PEAV已知首公开缺口与有限官方恢复沿用原证据，不重复sidecar的四路径，不列本窗确定候选。

## Seed1.8与实际触发SGLang

[Seed1.8 Blog](https://seed.bytedance.com/en/blog/official-release-of-seed1-8-a-generalized-agentic-model)全文核心已读。PublishDate=1765987200000是Dec18整日00编码、UpdateTime为2026，尚不能授上半日公开。三个thinking mode只说明能力，调节算法未披露；VideoCut选择片段slow-motion/high-frame-rate调用构成可改变长视频perception预算的潜力，不能只作功能清单或由日期失败关闭。Blog明确链接modelcard项目`https://seed.bytedance.com/seed1_8`，实际目前redirect/current首页仅Seed2.1等，没有原card；必要版本模型卡保留缺口，重开只需该release精确原card或公开上下界，不重试当前同页。WorldTravel best-of-five、部分subtitle与max-video-token条件已保留，不将整模型优势归因VideoCut。

MiMo本窗README新增实际触发[SGLang/Xiaomi作者技术Blog](https://lmsys.org/blog/2025-12-16-mimo-v2-flash/)，只读该原文不周扫。原metadata article:published_time为December16,2025日精度/nooffset，不能授17或18。原文完整必要core：5SWA1denseGQA、3MTP依次draft/mainparallelverify；Specv2融合spec decode/overlap scheduler，延迟output sync与CPU processing提前launch nextbatch以隐藏CPU开销；H20较低FLOPs时过多MTP可成为compute瓶颈、降低吞吐。性能用H200 DP2TP4EP8、MiMo optimized branch，优化尚未全部main，PR15207/15208是day0链接，不冒称生产主线全部合入。保留host/GPU overlap与hardware-aware speculative depth的具体潜力；完整benchmark hardware/precision/SLO缺项Not Disclosed，不采用通用倍率。

## arXiv停止与日期隔离

## GitHub精确revision切片

API区间since=`2025-12-17T01:00Z`,until=`2025-12-18T00:59:59Z`,per_page100，各页无Link。Qwen3/DeepSeekV3/KimiK2/T1/Video1.5为空；仅证明指定repo commit切片。WorldPlay9条、MiMo4条：

- WorldPlay `fc2e0e830e077dce40341c0478958e8c574b3e3a`原patch及精确raw download_models.py 302行已读：snapshot下载、允许patterns、复制resolve-symlinks、distill safetensors文件名修正、encoder路径与FLUX gate access说明。是下载/产物兼容辅助，不新增world生成机制；未运行脚本、未核runtime/security保证，不把普通修名升级为设计突破。
- `7080702d25d16ec1aa0dda3ab2372311b64d5933`README增加TODO Acceleration/Quantization，未实现；`00c734a6463f930408d64fa06ad53abc137b368e`训练代码TODO；`e9a6861e13318953d03d5acf361b0beb1335fd1e`及`7fbb02c2426d427709a8777f659afaf95f4718a8`citation作者顺序/Markdown换行；`891abcda47a262b0b4e7dc77b9be0a9bd360aff4`纠正错链2507.21809为2512.14614，改变身份但不新增机制，实际v1题摘已读。`cce7c2d723cc3f815f30e9c03486af503be13849`merge既有README；`08fb6c21660dd6b6729f2f8b84e8d92af84aace8`只有样例image binary patch；`e6a3555517a12c8658be21e9c668c6c389a60078`样例image公开patch403，已知变更范围无核心机制信号，不核二进制像素、不列研究新事件。
- MiMo `8cd5401817b6c1405d40db322cd475d940997569`SGLang pinned0.5.6.post2.dev8005+pr.15207.g39d5bd57a/SPEC_V2=1及具体Blog，触发阅读已处理；`26ef87c7e77b0ff16344a1777868946269e3ebb4`top_p=.95建议；`291d6e07aa285e19f2f359874a46647f2752b1ac`整理system prompt/sampling/tooluse、既有reasoning_content保存要求非新机制；后两API403已用公开`.patch`HTTP200替代。`838f87a`更新微信群是普通维护。

这些日期是commit身份，不是公开事件时刻；没有据此授first-public。只有实际触发的SGLang新技术原文保留机制潜力，不以compat版本号评分。

语言126/系统15/多模态7/ML上下文compute30的实际一页均无Next；时间是submitted first缓冲不是公开。官方cs.CL月列表只作2512.14080–15080身份段查漏，完整题摘的potential/close与少量决定准入正文在ADMISSION_ADDITIONS。纯物理/医学/地理/传统任务应用明确标题范围关闭；宽列表不自动逐项队列。尚未取得官方individual announcement/first-public，可读普通题摘仍实际完成后才保留日期缺口；不重复已有限穷尽的day公告接口，不以月归属/提交/2026holiday/OAIupdated赋时刻。
