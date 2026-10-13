# 03-18 补03-17首批准入校准

作者 supp_mar18；原候选0冻结。130 unique为四窄主题API提交线索，非公告队列、非确认候选；不先评分。首批10及14712/15523两EX均读完整v1题摘；完整AB/同页历史/纠错信号已由直接官方响应窄投影保存 SUP_AB_FIRST_DIRECT_20261011.json，web首批文件后段只元信息不作为完整AB证据。无当前页可见撤回或纠错signal。

| v1家族 | 准入链条（暂拟，须独核） |
| --- | --- |
| [2603.14591v1](https://arxiv.org/abs/2603.14591v1) | dense vocab头对小模型占比高 → balanced cluster/multiprobe/full-vocabulary sampling及selective quantization → 改变LM head是否必须完整dense执行的选择；精确性与CPU/GPU端到端成本待核 |
| [2603.14633v1](https://arxiv.org/abs/2603.14633v1) | 固定attack/output仍可被不同judge给不同ASR → disagreement标记+independent verifier → 安全scanner读数不能当target真实属性，需核独立verifier真值与成本 |
| [2603.15031v1](https://arxiv.org/abs/2603.15031v1) | PreNorm unit-weight residual累积稀释深层贡献 → input-dependent depth softmax及block缓存 → 深度有效性/层通信取舍，非只是新模块组合 |
| [2603.15202v1](https://arxiv.org/abs/2603.15202v1) | cache hit与load线性组合需workload调参 → newprefill×batch指标及失败条件 → 请求路由proxy的乘积选择需核条件，不授v3数字 |
| [2603.15340v1](https://arxiv.org/abs/2603.15340v1) | MDLM token uncertainty忽略依赖 → unmasked attention依赖辅助更新顺序 → 并行commit需用已知token信息而不只置信度；attention因果归因待核 |
| [2603.15401v1](https://arxiv.org/abs/2603.15401v1) | skill文本被当增益而未控repo/task → pinned repo/requirement配对执行及版本不兼容负例 → 外部程序知识的收益需按任务×compatibility实际验证 |
| [2603.15530v1](https://arxiv.org/abs/2603.15530v1) | hybrid SSM算子不吻合matmul中心P/D同包 → 分别systolic/offpackage与vector/inpackage → P/D分离应共同考虑算子/内存专用；simulation vs hardware待核 |
| [2603.15589v1](https://arxiv.org/abs/2603.15589v1) | BF16 exponent冗余但mantissa不能损失 → wire-speed multi-lane LUT Huffman ingress/egress → 无损精度下以codec面积/延迟换链路带宽；成本归因待核 |
| [2603.15619v1](https://arxiv.org/abs/2603.15619v1) | 深层残差稀释已形成features → sequence+preceding depth KV同head选择及非连续kernel → depth信息访问新选择与postnorm反侧 |
| [2603.15727v1](https://arxiv.org/abs/2603.15727v1) | message或shared config影响session后权限 → 持久自复制传播环 → prompt信任越界可成为生态传播，v1非v3且当前日期范围跨日，暂不确认候选 |

日期：首10实际DataCite字段见SUP_DATACITE_FIRST10_20261011.json。九项registered原值在UTC03/17（BJT同17），findable；15727在UTC03/18。官方availability说ID/DOI不能预发且submitted仅给最早可能announcement，官方DOI说arxiv将metadata送DataCite；最早slot与registered保守上界同BJT自然日只是一条明确的日期推断，待独核，不能以Submitted/Updated或registered本身冒充official first-public。15727范围跨17/18保持日期保留。潜力和日期都不等Evidence/Books。

代表EX：14712完整AB仅提倡agent自动数据准备/动态选择混合重加权两研究方向，未给可改变实际训练选择的新机制或验证；15523完整AB是Slovak keyphrase特定数据/形态exact-match误差，未建立主线模型/系统选择新边界（非以语言标签排除）；14559 endoscopy疾病评分数据、15168 ASD诊断融合明确领域应用，暂缓Science不能借通用多模态owner重新引入。OpenAI compensation核心§23–32只是工资信息用途分布、WorkerBench对2024 OEWS工资估计准确，未披露新的学习/推理/可靠性机制，不因privacy-preserving classifier字样准入。

未把其余题摘库存提前当证据、关闭或日期通过；有可执行筛选/审阅/Books/日级复核待办。旧14线索不重建全文队列。

