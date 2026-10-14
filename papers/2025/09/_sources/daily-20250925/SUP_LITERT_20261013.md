# LiteRT-LM具名有限release包：Carson

Google具名Sep24补检线索回到[官方工程原文](https://developers.googleblog.com/en/on-device-genai-in-chrome-chromebook-plus-and-pixel-watch-with-litert-lm/)，实际完整核心/代码例/preview脚注读取；只此篇，不扩全Developer Blog或新来源固定组。

原Sep24明确首次提供底层C++ preview接口，不是首次创造LiteRT或既有高层MediaPipe/AICore。窄拟P/1+2+1=4：既有高层API限制→允许直接组装LLM pipeline组件/Engine–Session接口→改变端侧consumer采用权限；贡献是版本接口事实，不给厂商品牌或成熟CoW/LoRA加分。Engine重资产共享，Session保持task/context；手表可仅组合executor/tokenizer/sampler降低footprint。**脚注明确某些优化未在early preview**，不授公开C++版全部具备context-switch/cloning/CoW，更不采用<10ms或subsecondTTFT为受控通用性能。未核artifact/运行/像素。

请求reader先校准有限原事件/准入/4分及preview采用边界。若通过，拟关闭深入采用/仅报告具体版本：成熟资产/会话分责不是本次新长期机制，不新写Books，不扩所有backend实现。必要精确release兼容事实可只核原官方声明；若确需artifact，则指具体接口/commit门再定点补，不遍历权重/版本史。当前尚未列正式候选、自授Evidence/Books/DAY；无锁、无UI消息。

实际结果覆盖上述待裁决停点：作者actual完整读Feynman§17，rootactual接纳Sep24原开发方低层C++preview事件/1+2+1=4、必要release关闭与仅报告通过；已正式同步README。未采用优化全包含/10ms等保证，没有为未采用功能扩artifact/后端权重。无Books新写/POST，无DAY预支。
