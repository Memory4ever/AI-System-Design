# 2025-10-21 首批独立贡献校准

root / Codex，非作者 Cicero；本次重新读取 AGENTS、研究合同、每日与 arXiv 来源、Report V3、Prompt、ROADMAP、最新月度路由及21日报/筛选/停点。窗口 BJT [2025-10-20 09:00,2025-10-21 09:00)。本轮仅首批，不授 DAY 或其他日期完成。

## 校准结果

六项潜在贡献理由通过；首公开与必要历史版本继续隔离，正式候选0、不评分、不授正面 Evidence、Books 或覆盖保证。实际读完整精确v1題摘与原事件页：四项网页原件见 ROOT-FIRST-originals.json；StreamingThinker与query augmentation的网页Cache miss后本日curl恢复原abs，实际解析完整blockquote，见 ROOT-2510.17238v1-abs.html、ROOT-2510.17139v1-abs.html。不以当前v2/v3/v4摘要替代历史内容。

- DistCA：parameter-free core attention 解耦到设备池，token-level task动态重组处理二次与线性计算失衡；值得核训练切分边界。512 H200/up to1.35x不作普遍加速，stateless不等训练完全没有瞬时状态。
- ReXMoE：跨相邻层复用专家、逐步扩路由池，挑战每层独立专家池与固定预算下维度/多样性取舍；0.5B–7B局部研究不是排除理由。
- StreamingThinker：精确v1确有streaming attention/position及parallel KV，将输入编码与reasoning生成解耦；保留实际并发与完整信息依赖待证，不照录80%/60%为通用收益。
- SpecAgent：索引期预计算把线上时间压力移到indexing，明确未来context leakage反侧；合成leakage-free benchmark不代表真实仓库历史，索引/更新成本不能隐去。
- Query augmentation：精确v1的prompting/RL系统比较和OPQE结构有潜力；未控制backbone与预算就不能说RL普遍更差。负面或训练free结果不因不够新而排除。
- SafeSearch：精确v1明确final reward加query-level shaping，中间动作安全与最终拒绝不是同一对象；LLM reward不是硬权限保障，三个red-team数据集的局部结果待其必要证据，不先采用70%泛化数字。

原事件页v1仍只给提交时间；论文家族、版本与first-public事件不同。不能从submitted、11月ID或目录日期自动确认本窗。取得完全落窗的原公开依据后，才按贡献命题评分与证据投入；期间必要安全/纠错核心仍按合同定点读。

## 分层排除抽核

实际解析本日四主题Atom及supplement的四个完整摘要：18075化工batch distillation实验数据、17529前列腺纵向MRI分割、17382非LLM MAPF搜索、21791遥感夜光融合。前三项的范围理由成立，MambaX被查的当前Atom为v3、化工为v2，检查权限仅为当前摘要所示主线关系，不声称完成所有历史版本核查。21791明确比较现有UNet/diffusion/flow在夜光融合的噪声调度/量化选择，未提出足以改变通用生成模型解释的新机制或有效性边界，关闭本项目贡献；不能把所有遥感、所有diffusion或小型实验一概排除。另两项代表consumer/battery本轮未读，不称全部13排除项已独立验证。

没有发现可将同理由扩散到所有视觉/领域场景的共同排除依据；后续 DAY 必须处理16必要反侧及有限来源实际范围，而不是把首次校准当全日报验收。作者可以复用本轮有效六题摘校准，不重读同样内容或等待22～25日。
