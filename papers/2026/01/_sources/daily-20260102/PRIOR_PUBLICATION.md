# 定点前公开归属（不扩2025会议队列）

仅解决本日已发现具体家族是否首次公开，不审旧revision。日期原值与出版方权限分开；不把搜索indexed/published-ago当精确日期。

- 2512.24695 Nested Learning：实际官方[Google Research原公告](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/)标November7,2025并链接已有论文；全文核心的nested optimization/CMS/HOPE与v1题摘同家族。真实公开不晚该日（原页未给时区/时刻，不补造），不属于Jan02初公开。无需为当日重读全文或计算分数。
- 2512.24097 D2VLM：正式[CVF具体论文页](https://openaccess.thecvf.com/content/ICCV2025/html/Zeng_Factorized_Learning_for_Temporally_Grounded_Video-Language_Models_ICCV_2025_paper.html)实际搜索缓存恢复完整原文题摘、出版方bibtex **month=October/year=2025**、pp20683–20693；同[原论文](https://openaccess.thecvf.com/content/ICCV2025/papers/Zeng_Factorized_Learning_for_Temporally_Grounded_Video-Language_Models_ICCV_2025_paper.pdf)第一页恢复grounding→evidence-referencing/FPO与本v1一致，原URL直开403不否定已恢复出版物身份。2025October已公开范围在窗前；v1 comment只是Fig1 concurrent Qwen图释修正信号，未呈现本窗新系统机制或重要纠错，不因arxiv上传重列新论文。
- 2512.23852 Trellis：实际官方[OpenReview论文](https://openreview.net/attachment?id=r61s1FNYlj&name=pdf)原稿搜索缓存明确Published as a conference paper at COLM2025，正文完整contribution bounded-KV slots/online compress匹配本v1。Forum/API2/PDF direct403/challenge，未恢复精确公开日；不把索引“1.1years”当日期。出版身份支持2025已公开上界，精确原首公开仍未知，不计Jan02新论文，亦不声称之前报告已审。
  - 实际缓存身份：标题“Trellis: Learning to Compress Key-Value Memory in Attention Models”；作者Mahdi Karami、Ali Behrouz、Praneeth Kacham、Vahab Mirrokni，Google Research。上述attachment与[同ID原PDF](https://openreview.net/pdf?id=r61s1FNYlj)搜索缓存分别恢复第一页及Introduction/contribution：有限memory slots承载KV历史、两阶段recurrent压缩、在线gradient更新及select/forget gate。与本v1的memory上界/online compression具体机制匹配，不仅是会议年份相同。ID按原返回的r61s1FNYlj保留，不根据大小写猜另一个Forum。采用范围只是“2025已公开，窗前”，不是精确首公开时间、旧论文Evidence或Books验收。
- 2512.23858 Yggdrasil：实际[NeurIPS2025具体poster页](https://neurips.cc/virtual/2025/poster/119964)给FriDec5,2025 4:30–7:30PM PST，title/author/AB与本v1的equal-growth tree、latency-aware draft、static runtime一致；[2025正式Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7d66be507114ffe38c3d3eb528454952-Abstract-Conference.html)实际AB及DOI10.52202/085713-2901已核。公开论文/展示不晚此Dec5活动范围，不能把arxiv Dec上传作Jan02首公开；不把poster开始当首公开的精确分钟。
- 2512.23808 MiMoAudio：MiMo官方Paper目录原始发布日期2025-09-19已核，同家族不是Jan02初公开；不因论文arxiv月号改变归属。

- 2512.25034 Generative Classifiers Avoid Shortcut Solutions：出版方[ICLR2025原PDF](https://openreview.net/pdf?id=oCUYc7BzXQ)原页搜索缓存实际恢复同Alexander C. Li/Ananya Kumar/Deepak Pathak、完整题摘同五distribution-shift及Gaussian条件，首页明确“Published as a conference paper at ICLR 2025”。root独立同原出版方搜索实际读取后确认2025已公开上界，足以排除Jan02首次；direct PDF/forum仍challenge，不声称精确2024/2025首公开分钟或完整旧文审阅。必要v1已读证据保留在EVIDENCE_BATCH_12_13_GENERATION，不因上传重计新候选；索引相对age不作日期证据。

后续如有本窗release/重要修订的具体机制，而非仅上传/版本号，再仅重开该事件；这份处置不是旧论文全量Evidence或Books通过。
# UniAct 24321 首公开定点恢复（root实际通过；第七项窗前公开）

当前作者项目 https://jnnan.github.io/uniact/ 真实有FSQ离散共享输入、MLLM motion tokens、causal motion decoder与tracker桥接说明，但无日期。不能由无日期页或arxiv Submitted确定首公开。

实际GET https://api.github.com/repos/jnnan/uniact：created_at=2025-12-20T11:28:15Z，default_branch=main；这字段本身不证明公开正文。实际有界 https://api.github.com/repos/jnnan/uniact/actions/runs?created=2025-12-20..2025-12-30&per_page=10 返回total_count=7（≤10，读完停止），其中run20393826813名称pages build and deployment，head_sha=81f08a6f79769fcb2c04263ced2f1c6d9b3f10c7，created_at=2025-12-20T11:35:46Z，updated_at=2025-12-20T11:36:28Z，status=completed，conclusion=success。原始run https://github.com/jnnan/uniact/actions/runs/20393826813 ，jobs https://api.github.com/repos/jnnan/uniact/actions/runs/20393826813/jobs 。只给已经发布的保守上界，不虚构精确首公开分钟。

该sha真实index https://raw.githubusercontent.com/jnnan/uniact/81f08a6f79769fcb2c04263ced2f1c6d9b3f10c7/index.html 共554行；385题名、413介绍、444 method完整段已actual读取：异质text/music/trajectory/reference→FSQ token共同embedding→MLLM motion tokens→causal decoder连续DoF→streamed tracker。与准入所提6分机制身份吻合，不声称v1全部新实验已经窗前。即使不用最早时刻，此Pages发布与精确正文可支持2025窗前机制上界；新论文如有重要新证据需具体识别，不自动firstpublic。

其余有限probe：code repo jnnan/uniact-code created2025-12-30T08:41:37Z与Dec30/31提交不直接授public；jnnan.github.io path=uniact untilJan2 API空，实际页面来自单独repo，所以空不授不存在；Pages builds接口404不替有效Actions。deployments per_page10共8，Dec20记录3511462194目前状态inactive，不能独靠inactive授当时成功，采用上述实际success run。无进一步网页历史/全repo考古。

root实际GET成功run元数据；raw URL两次reset后不继续恢复链，转单一[GitHub contents API exactref](https://api.github.com/repos/jnnan/uniact/contents/index.html?ref=81f08a6f79769fcb2c04263ced2f1c6d9b3f10c7)恢复当时原HTML，实际读407–457（method444）FSQ共享token→MLLM motion→causal DoF→tracker。必要原正文与实际成功deploy一致，支持2025Dec20已公开机制的保守上界，排除Jan02首次；不是commit=paper首公开分钟，也不声称全部v1实验此前已发布。原raw工具响应未保存为磁盘HTML，不能把本笔记冒充原HTML缓存；root此次真实API恢复为独立复核依据。七项前公开不是旧Report已审重复。
