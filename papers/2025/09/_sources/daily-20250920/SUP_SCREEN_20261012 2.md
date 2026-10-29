# Sep20 题摘及准入补表

作者Meitner实际读128份`SUP_AB_<id>.raw`精确2509.<id>v1完整题摘及current轻核；Cicero亦逐项实际读。首40具体理由在[首批](./SUP_FIRST_20261012.md)；本表是其后88，不是新独立分母。正式候选必须另过public date，本表P不评分/采用。

| exact v1尾号 | 读层 | 判断与实际增量（原约束→新增→需重考虑） |
| --- | --- | --- |
| 15356 | AB+core | P：平均confidence不能可靠预期新task→分布variance/percentiles与模型特异→selective task适用门 |
| 15357 | AB | P：掩码attention的信息/效率约束→局部结构替代→attention形式选择 |
| 15361 | AB | P：expert routing因果混杂→counterfactual专家选择→router解释和优化 |
| 15362 | AB | P：低资源语音预训练迁移→HuBERT继续预训练的表示条件→训练配比而非语言名 |
| 15366 | AB+独核core | P：judge facet看似可靠但加权算术错误→ED/BD聚合方向不同→评价反馈算术有效门 |
| 15389 | AB | P：低监督2–5%语音→curriculum训练条件→数据投入选择 |
| 15406 | AB | P：provenance表面匹配→因果指纹→来源关联可验证门 |
| 15416 | AB+core | P：训练分布只覆盖常见endpoint→site/rare-endpoint DRO局部条件→鲁棒目标选择；GradCAM不授安全 |
| 15420 | AB | P：ranking学习的可解释/理论条件→算法界→泛学习优化主线，不因非LLM名排除 |
| 15432 | AB | P：视觉检索caption proxy的对齐路径→替代表示→检索encoder选择 |
| 15435 | AB+core | P：单VLM容易一致幻觉→异构工具冲突查询→test-time robustness/成本条件 |
| 15443 | AB | P：人动作与humanoid约束错配→kinodynamic retarget→action可执行性接口 |
| 15448 | AB | P：不同hierarchy entropy/privacy取舍→attention DP设计→噪声/表示分责 |
| 15455 | AB | P：层独立量化忽略相互影响→Shapley interlayer分配→量化budget选择 |
| 15464 | AB | P：静态KG不能保时间更新→temporal confidence演化→结构状态更新门 |
| 15472 | AB | P：dataset distill生成多样性与对齐相冲→双向约束→压缩数据保真选择 |
| 15479 | AB+独核core | P：GAN/SSL感知收益损像素、VDEC FVD收益损FID/CMMD→具体指标取舍，非仅开源/成熟组合 |
| 15482 | AB+core | P：相同pretrain范式不保表示相近→slide-specific/stain反侧→表示泛化验证 |
| 15490 | AB+独核core | P：RGB/depth separate paths+pixelshuffle连接器→小规模spatial model接口替代；非600M排名本身 |
| 15496 | AB | P：多identity/ref条件冲突→adapter分责→条件注入选择 |
| 15498 | AB | P：离散动作codebook的动态选择→EWA attention→action表达设计 |
| 15514 | AB | P：量化与熵编码分开损压缩→联合约束→存储/解码tradeoff |
| 15532 | AB | P：GUI全图上下文冗余→adaptive crop/stage→感知计算分配 |
| 15536 | AB | P：world rollout运动/尺度依赖→scale-AR与motion prompt→生成factorization |
| 15546 | AB | P：subject/action校验falsepositive→adaptive keyframe/checker→评价和采样门 |
| 15553 | AB | P：block/timestep图像与语义贡献不均→二维控制→生成成本/质量调度 |
| 15557 | AB+独核core | P：format proxy reward OOD hacking可能加重→形式合规不等faithful，非普通格式SFT |
| 15566 | AB+独核core | P：ROI监督与动作type/args joint reward→定位和执行依赖；非brain类比 |
| 15596 | AB+独核core | P：human低lexical却高rubric→传统文本指标失配；非医学应用/低performance排除 |
| 15602 | AB+core | P：密集/稀疏空间时间需求冲突→TV理解task-specific设计条件，不凭Tennis领域排除 |
| 15607 | AB | P：多模态偏好与trajectory credit→PbRL奖励分配→反馈粒度选择 |
| 15614 | AB | C：BERTembedding+LSTM extractive summarization应用，未给新模块成立条件/通用反侧；非dataset名字关闭 |
| 15635 | AB+独核core | P：三模50.71低于log+metric51.27，未输入trace hallucination→融合不是自动收益 |
| 15641 | AB | C：原文自己明确连接与后果均非新，仅对应既有理论，未给本项目新的条件；非理论范围排除 |
| 15642 | AB | P：visible/infrared联合preservation→patch contrastive目标→融合信息取舍 |
| 15658 | AB | P：一编码双decode多任务chunk检索→复用表示→检索/生成解耦 |
| 15688 | AB | P：saccadic NMS选择attention→视觉计算分配替代 |
| 15693 | AB | P：多对象结构关系→contrastive alignment→组合表示条件 |
| 15695 | AB+current/v4/v5 | R（v1研究潜力P）：v4withdrawn/noPDF，v5恢复PDF但comments仍withdraw affiliation；不默认为current全稿W或恢复已解决，不评分/采用 |
| 15704 | AB | P：trainingfree pyramid token pruning→多尺度保留→视觉token预算 |
| 15711 | AB+core | P：semantic CLIP丢fine trace→双domain adapter+labelledcache→新generator适用门 |
| 15717 | AB | P：手内camera缺视角→synthetic LoRA/relativepose→感知action接口 |
| 15735 | AB | P：单时刻hidden-state漏drift→谱统计recurrent tracking→hallucination/OOD时序判据；未授实时保证 |
| 15738 | AB | P：纯random轨迹多样但无意图→先stochastic后goal-aware、多stride→GUI训练数据覆盖选择 |
| 15759 | AB+core | P：fairness与accuracy冲突→ideal-distribution parametric条件→数据干预，而非无假设公平保证 |
| 15772 | AB | P：VLM3D reward不可直接优化→differentiable feedback→三维生成反馈接口 |
| 15785 | AB | P：continual prompt失plasticity→CBP reset→持续适应机制 |
| 15803 | AB+core | P：brand prompt修正过强/弱都失败→双score/cache条件→debias选择；不授front-door因果 |
| 15810 | AB | P：metaBBO新实例缺多样性→AE/GP生成→optimizer跨任务适用门 |
| 15859 | AB | P：foundation latent合成训练→linear classification条件→数据/表示耦合 |
| 15865 | AB | P：独立semantic diffusion阶段错配→共享早期语义→生成阶段分责 |
| 15871 | AB | P：单view3D grounding信息缺口→view retrieval→检索与场景定位 |
| 15883 | AB | P：relation检索caption→结构关系而非对象孤立→视觉语言对齐 |
| 15886 | AB | P：SAM二维输入丢range几何→range-view设计→表示接口 |
| 15915 | AB | P：foundation worldgrid rollout与RL/eval耦合→world model适用条件 |
| 15924 | AB | P：sparseview 2D proposal→3D feature一致性→场景表示恢复 |
| 15932 | AB+core | P：feedback容量/目标不可恢复→有假设信息下界→alignment可行性，不授实证安全不可能 |
| 15934 | AB | P：visuotactile能量与diffusion→接触仿真替代→观测生成路径 |
| 15937 | AB | P：VLA终答评价漏过程→pair progress/action/reward critic→动作反馈粒度 |
| 15962 | AB | P：自然语言空间歧义→structured tuple spatial prompt→模型空间接口；非单排行榜 |
| 15968 | AB+core | P：openloop看似会驾驶而closedloop失败→takeover pair refinement→动作偏好反馈；无实车保证 |
| 15980 | AB+core | P：FE/ASR可高但most/least扰动差接近零→AF反侧→explanation评价盲区 |
| 15984 | AB+独核core | P：PTA历史cache crossattn/稀疏sample与2anchor优于3→具体trajectory接口条件，非普通应用组合 |
| 16002 | AB | P：quantum RL qubit复用与Grover→计算/状态机制潜力，非量子领域名关闭 |
| 16006 | AB+独核core | P：Lang2LTL generic22→77/88而导航稳定，未来远状态退化→planning语义条件，非成熟组合C |
| 16011 | AB | P：continual vision单prototype覆盖不够→multi-prototype→表征记忆更新 |
| 16017 | AB | P：跨modality VFM知识迁移→distill/matching→监督表示交接 |
| 16020 | AB | P：拓扑mask circuit RL跨结构泛化→foundation policy约束，非quantum应用名排除 |
| 16031 | AB | P：coarse alignment不保局部visualspeech→local融合→表示时序选择 |
| 16053 | AB | P：scenegraph atomic skill diffusion→可组合控制路径→动作表示 |
| 16054 | AB+current | W：current明确整稿withdrawn，原机制不进入评分/采用/Books；非访问失败 |
| 16058 | AB+core | P：ASAC末层插入与OOD/noise/seed条件→表示控制；非意识或普遍鲁棒保证 |
| 16072 | AB+core | P：semantic mismatch独立failure与sim→real recall下降→跨层head/数据适用门 |
| 16087 | AB | P：keyframes/trajectory spatial prompt→动作条件信息压缩路径 |
| 16088 | AB+core | P：oracle语义类+RS image-only条件→certification质量/采样成本；不授任意oracle安全 |
| 16091 | AB | P：blindspot双branch diffusion→未知观测与生成分责 |
| 16098 | AB | P：DINO compact object query与2Dmemory接3D，免全featuremap→2D到3D表示/memory接口，不授长期世界状态 |
| 16106 | AB | P：未知measurement盲posterior→conditioned recovery→生成推断接口 |
| 18189 | AB | P：Qianfan multistage训练/data/5000P800缩放→模型系统协同潜力，不凭SOTA收；submitted仍非public |
| 19364 | AB+core | P：offline/800field/sockpuppet异质性不同→personalization评价条件 |
| 19365 | AB+独核core | P：安全对齐拒敏感topic、全部LLM coherence低baseline却diversity高→representation/指标冲突，撤回纯组合C |
| 19368 | AB+core | P：pipeline verifywhile-draft减少长draft低accept浪费→时空调度条件 |
| 19369 | AB+core | P：Korean schema-value与chain深度差额→Caller约束条件，而非小model排名收 |
| 19371 | AB+core | P：过量knowledge injection留存collapse且model/token规模改变阈值→训练频率选择 |
| 22688 | AB+PDF独核core | P：difficulty/variance+semantic curriculum与phase转换，IoU过大格式失败/phase短退化→GRPO成立条件 |
| 25203 | AB+独核core | P：rawcommit训练40.26低于base44.24，rewrite38.76、生成49.40；mix/filter顺序及lazy style不同→编辑数据条件 |
| 25204 | AB | P：spectral buffer/SVDlogits不确定性触发→推理状态预算选择 |
| 25534 | AB+core | P：self rubric grader RL、弱judge更高score/length通信质量退化→reward与评价可比门 |

新128实际合计122普通P+1状态R（15695 v1研究P）+3C+1A15160+1W16054。与旧65有效题摘及8项旧title恢复无交叠，最终201＝190P+1R+6C+2A+2W，Cicero独核§8实际归并通过。P只证准入清楚；current后续版本不替v1。首次public有限门已记录于[本日来源](./SUP_SOURCES_20261012.md)，new/pastweek返回2026，只作日期隔离，不拿Submitted证明本窗。其余219发现中无关/明确title仅线索，不变逐项关闭池；无未归并或未记录日期入口的普通待办。
