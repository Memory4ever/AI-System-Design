# 10323：局部水印反侧、中心正交性主张及阈值修订

仅03-13新增Mar12 BJT。完整v1题名/两作者/AB已实际读 `SUP_ABS3_10323.txt`，准入与主独核DATE3 §23明确含本ID的Mar12 arxiv事件日有效复用；Registered/Submitted/Updated没有单独授日期。没有具名dated早稿信号。

v1 HTML404，官方 https://arxiv.org/pdf/2603.10323v1 正常GET200/608754bytes，原件 `SUP_HANDOFF7_SOURCE_10323_PDF.raw`，结果 `SUP_HANDOFF7_PDF_FETCH_RESULT.json`；pypdf完整提取10页文字 `SUP_HANDOFF7_SOURCE_10323_PDF.txt`。实际必要读PDF pp3–8 §3–6方法/全部主结果表/直接限制，另目视完整pp4–5核文字提取遗漏的公式、AER图/主表与脚注。没有读全参考文献、运行攻击脚本或认证作者实现。临时渲染不是新研究原件。

评分拟 **2+1+2=5**：现代生成式编辑与几何扰动、同时要求检测信号弱化和semantic proxy保留的对照人口，属于重要安全评价边界(2)；实际影响受测两种水印/SD1.5输出的局部负载(1)；威胁变换/效用/检测权限分责可复用(2)。不把watermark、CLIP或数学正交宣传计新增，不因作者机构或小模型排除P。

## 必要机制、评价与采用边界

DiffusionDB 2M-first-1k prompts，SD1.5生成4000图，Tree-Ring 2000原生latent embedding与RivaGAN 2000生成后embedding；未据文字认证两组是严格同prompt paired。同一30 intensity sweep分别考生成式重构、固定几何遮罩编辑、几何变化和亮度变化，不假设复合/自适应威胁已测。

pp4 §3.3采用两个不同survival代理：Tree-Ring max(0,1−MSE/σ²)，σ²是empirical pixel variance约5000；RivaGAN byte accuracy。压至同0–1不说明它们在同CET=.20有相同false-positive/sensitivity工作点。v1 AER是survival<.20与OpenCLIP ViT-B32 similarity>70同时成立，不是原内容/人物/细节严格保存证书或不可伪造性证明。

pp5每interval n100，MOE以估计标准差.20代入1.96×.20/√100=3.92%；代数值没错，但固定.20/CLT n≥30不能签任意成功率或同时多interval的95%误差界。若所述是AER Bernoulli proportion，其标准差需绑定p，.5时.5/√100而非.20/√100；未获原data/sampling dependence，故不据此补出作者全部置信区间或累计n3000独立性。DDIM无攻击baseline约.95另属inversion drift，不由该MOE认证已完整计入。

完整主表局部反侧：RivaGAN crop22.67、Img2Img67.47、inpainting66.80；Tree-Ring crop43.20、Img2Img17.73、inpainting10.27。保留作者当前门槛/配置下的数值及failure方向不同，不合成所有spatial/latent architecture结论。§5明确architecture/SD1.5/几何遮罩/inversion限制；§6组合水印、non-interfering null-space与复合攻击只是futurework。

## 中心争议及当前具体修订信号

作者把主表推为互斥且“mathematically orthogonal”失败、所有single-domain必然不足，并由此建议dual-layer必需。表中共同攻击类别两种水印均有非零evasion，不支持类别层面的互斥；没有数学inner-product对象/对应定理或paired joint-failure证据可推出严格orthogonality，也未测试dual-layer干扰或全架构。这里不把共同类别非零误称同一图像paired双失效已测，不判所有局部实验无效。

current官方abs正常GET200 `SUP_HANDOFF7_CURRENT_10323.raw/txt` 实际完整读AB/Comments/history，AB threshold已经>75而v1是>70。为处理这一具体评价身份变化，只取 https://arxiv.org/pdf/2603.10323v2 ，GET200/607989bytes，`SUP_HANDOFF7_CURRENT_10323_PDF.raw`/`SUP_HANDOFF7_REVISION_FETCH_RESULT.json`；只实际读pp1/4/5相应门槛及主表，机械提取也仅三页。v2正文门槛75，表内上述数字仍同v1；未披露是否重算/是否原样本都过75，不能将v1/70的人口数字直接认证为已验证的75门槛结果，也不由数字不变断言必然计算造假。没有遍历全revisiondiff。v2 Submitted/Updated字段不作为Mar12公开事件证明、不倒灌本窗v1，不另计family分数。

## owner/处置提案

实际顺读Ch72完整190–215资产/取证/生成水印/派生物局部：207已有generator/decoder/更新身份与有限bit accuracy≠authentication；209已有regeneration transformation、CLIP/FID代理非严格语义/来源、所测SD backbones不外推所有内容保持变换，签名origin/provenance回退；211–213又分detector operating-point与paired identity。现书不主张两个embedding域失败严格互斥或双层水印必然解决问题，故不需为本文争议修改有效安全正文。

拟 **争议/暂缓Books新写0**：采用范围至受测局部failure对照，中心严格orthogonality、泛化、统计界及threshold迁移不支持Books正面保证。不是低分EX、不是把新实验称已吸收的NC；当前Ch72已有一般限制可定点复用。重开仅需paired joint-failure/明确定义与证明、工作点校准/实际采样方差，以及70→75对应population/重算说明，不索取全代码或所有版本。待root非准备者必要Source/评分/终态独核，不自授正式/DAY。
