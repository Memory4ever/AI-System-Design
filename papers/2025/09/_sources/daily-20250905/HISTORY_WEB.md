# 05 fresh 有限辅助补检

执行于2026-10-06，仅05窗口，不授历史全覆盖。原始目录响应和请求另存同目录。

- `site:hunyuan.tencent.com "2025-09-04" research`：无本窗primary命中；不能将其当2025 Research目录。
- `site:research.google/pubs "September 4, 2025"`：无本窗确定的foundation/model-system命中；现有Publications当前页不是冻结历史目录。
- `site:deepmind.google "September 4, 2025"`：原始[Deep Loop Shaping publication](https://deepmind.google/research/publications/145314/)完整摘要与[官方博客](https://deepmind.google/blog/using-ai-to-perceive-the-universe-in-greater-depth/)显示frequency-domain reward/RL controller抑制LIGO噪声；不是foundation模型机制，也没有此处模型系统桥，属本项目暂缓AI for Science，明确关闭，不泛化至LLM运行时。
- OpenAI原件403后实际网页恢复：[Expanding economic opportunity with AI](https://openai.com/index/expanding-economic-opportunity-with-ai/) L24–46完整文章，Jobs Platform、Certifications/Academy训练普及与招聘匹配计划；不是LLM训练/推理机制或新的发布安全合同，贡献关闭。RSS公开时间2025-09-04T11:30Z落窗，不因日期精确而入候选。
- [Anthropic biorisk](https://www.anthropic.com/research/biorisk) 原始HTTP全文0–44段已读，原文边界见NECESSARY_CORE；原作者只看目录publishedOn形成hold，后被独审具体新证据重开：正文article:published_time/JSON-LD datePublished/visible time dateTime一致2025-09-05T00:00Z，root实际独核接受当窗08:00BJT发布事件。modified2026-07-08另列当前正文版本，不授所有现存文字2025冻结；不能继承旧配置-only hold。

不扩Hunyuan历年库、Google全年Publications、全部DeepMind科学研究；缺精确历史冻结时只保留来源限制，不记零命中/无遗漏。

arXiv精确公告有界恢复：日期型list CL/CV真实400，网页恢复各cache-miss；month `2509?skip=0&show=2000`各404，未读取全月题摘。最后按合法catchup（subject=cs.CL/cs.CV,date=2025-09-05,include_abs=True）实际请求并保存HTTP错误原文，`catchup-cl.raw`/`catchup-cv.raw`明确“Invalid date...Catchup only allowed for past 90 days”。只此原文支持90天限制，不能由先前400推导。保留所需正式公告/当时v1冻结请求，不无限追史。
