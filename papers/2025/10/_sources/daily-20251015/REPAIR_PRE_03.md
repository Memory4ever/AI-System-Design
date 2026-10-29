# PRE03：反馈条件的两种消费

writer Popper。请求仅以下完整段/独立marker/本人note的唯一reader整体PRE；实际Source/评分见REPAIR_EVIDENCE，目标与邻章及完整直接两侧已读，未写Books。

## I07 / 11307 / MULTIMODAL-EMBODIED-VLA Ch26 / 2+1+2=5

文件 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。在完整“derived label 必须保存 provenance”原段之后、完整“同一批自然次优示教的‘质量’也不是单一筛选阈值”段之前；不改其自然示教质量权重/过滤/conditioning分工。

拟正文全文：

次优动作还可保留在序列中，由每步语言反馈说明失败或子目标进展，而不先将整条轨迹删掉：把反馈embedding与指令、观察和动作共同作为policy条件，再另用辅助head预测下一步反馈。[FOSSIL的受限对照](https://arxiv.org/html/2510.11307v1#S3)中，预测结果只进入训练loss，并不回灌下一步输入，因此“会预测反馈”不能替代部署时的真实反馈接口。该grid-world反馈由特权state/goal的规则oracle产生，不是一般环境随手可得的人类判断；语言与scalar条件的信息粒度也不同，语言并非所有空间位置或组合切片更优。Oracle/轨迹制备、反馈编码与预测、全部训练和闭环回归都付费，反馈生成器的真实成本不能由模拟成功率消除。反馈失准、缺失或越出观察权限时，保留可信标量/任务信号、原示教与直接BC，并由独立controller验收动作，不把纠错文字或辅助预测当作已取得环境真值及真实机器人安全。

<!-- source-family:SF-2025-ARXIV-2510-11307 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11307`：Popper，Daily2025-10-15补Oct14，exact-v1 §3–5/Table1/2及Limitations，2+1+2=5。仅次优动作的反馈条件与辅助预测不回灌分责；保特权oracle、语言/scalar信息差异、局部反退及全费，不授自然反馈免费、通用stitching或物理安全。未核全附件/实现/复现；PRE/SAVE/完整自读/solePOST只本日canonical真实后到层。

## I08 / 11498 / AGENT-REFLECTION Ch80 / 2+2+2=6

文件 `books/part-07-agent/80-reflection.md`。完整“外部反馈也不是同样强的修复信号”段（SF-2026-ARXIV-2604-21950）之后、完整“比较多条搜索候选时，还可先固定同一份可检验要求”段之前。

拟正文全文：

反馈也可以先限定训练轨迹的接受规则，再决定部署是否继续调用critic：渲染代码取得多时刻截图，由视觉critic给反馈与reward，只在分数超过当前best时接受修订，失败重采达到上限就停；policy token参与RL，critic反馈另作可选蒸馏。[ReLook的受限分支](https://arxiv.org/html/2510.11498v1#S2)将生成、视觉反馈与轨迹选择连起来，但单调的是该critic被接受的轨迹，不是真实质量，也不是全部尝试的无回退保证。部署撤去critic/截图后仍有多轮self-edit，不能继续继承训练的外部比较门；可渲染更不等交互语义、权限或所有reward hacking已解决。原稿人评新做与继承已有证据的来源表述冲突，应保留而不拼成独立真值。全部拒绝/重采、渲染、critic/蒸馏训练、checkpoint选择和最终功能回归都计费；代理漂移、真实结果或净预算不合时，保留原候选、可信测试/视觉核验和较少反思，不由proxy单调或少一次大模型调用批准通用可靠性与免费提升。

<!-- source-family:SF-2025-ARXIV-2510-11498 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11498`：Popper，Daily2025-10-15补Oct14，exact-v1 §2/§3.1–3.6/T1–2及旧AppA/B必要反侧，2+2+2=6。仅critic条件的轨迹接受/蒸馏与撤critic部署资格分责；保human来源冲突、valid-render非语义/安全、额外重采与全费用，不采真实单调/完全防hacking或全配置净加速。未核代码/运行复现；PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。
