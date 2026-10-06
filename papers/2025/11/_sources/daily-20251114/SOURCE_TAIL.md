# 11/14 来源尾部有限终态

作者 Planck；以下是实际当前入口恢复，不是2025年历史目录完整性保证。只保留本日相关边界，不将2026内容纳入候选。

## Z.ai Research

原 Research HTML与精确引用的 hashed page script 实际取得，见 [HTML](raw-zai-research.html)、[page JS](raw-zai-research-page.js) 及各request。真实 More 用 `?page=nextPage`。实际 [page2](raw-zai-research-p2.html) GET200，hydration累计18个 blogsItems 身份，`nextPage=3,hasMore=false`，createAt最早2025-12-07；顺序并非严格按日期，已按日期字段判边界。HTML显示日期与createAt不一致时保留原字段，不强行同日归一。停止page3；已穷尽当前目录返回，但没有恢复November旧目录/删除条目。发布说明Dec8→Sep30的断档不能替Research覆盖。精确重开条件：官方旧Research列表/对应November原文，且有本窗事件信号。

## MiMo Paper / Blog

首页论文8条日期到Oct21边界；Blog 15条标题缺日期，More无href。实际页面引用的 [index script](raw-mimo-index.js) 不含More实现，进一步仅检查其引用的 [entry script](raw-mimo-entry.js) 路由/frontmatter，辨认真实 `/blog/` route，未遍历所有文章。

实际 [GET /blog/](raw-mimo-blog.html.request.json) 返回200、response URL仍为该路径，但 [HTML](raw-mimo-blog.html) 的身份是 **MiMo-V2-Flash** 单篇，显示 **December16,2025**，不是Blog目录。路由成功不等于取得历史目录。该窗外正文不使用、不生成12月队列；停止猜其他路径，浏览器不可用的既有事实不反复重试。精确重开条件：可核的官方历史Blog日期列表，或带本窗日期的具体原文。当前受阻是历史Blog段，不是已检查得出0研究。

## MiniMax 双语目录

英文当前列表已读12条标题/日期到Oct27边界；中文 `https://www.minimaxi.com/blog` 实际跳转 `https://www.minimax.cn/blog`，见 [raw-web-18](raw-web-18.json)，13条可见日期条目，Nov附近由Dec23跨到Oct27，继续到Jan15。没有保留Nov13条目。止当前无分页目录；只说明当前列表范围，不证明历史删除项不存在。

root尾部独立指出Agent Tech是Daily注册入口，原“未触发”措辞错误，现修正。本日实际GET [Tech入口](raw-minimax-agent-tech.html)200、web正文只有导航；沿实际提供的[llms index](raw-minimax-agent-index.txt)读取完整索引，仅一条technical article Agent Team，再取其明确链接的[techblog.md](raw-minimax-agent-tech.md)200（web失败由GET修复），实际只有2026-05-13一条。HTML原日期published/modified皆2026-05-13T13:32:04.387Z，保留，不当2025目录。停止当前索引，未读窗外agent-team正文/CLI文档，无猜分页。raw-web-26与3份request支持真实执行；必要2025本窗Agent Tech段受阻，不因当前2026唯一条目写不适用或0。重开需官方旧索引或具名本窗技术稿/发布字段。

## Google 来源组修正

Google pubs必要本窗历史切片未恢复；676年度标题入口不是本窗官方公开列表，不扩题摘队列。Blog已实际读至Nov12/SIMA核心与森林/quantum负侧，不替整个Google来源组Coverage。正式来源组受阻；接受可核的本窗pubs历史列表或具名原始发布后定点重开。

本尾部无可执行空路径重试。Zai/MiMo历史必要缺段留外部保留，不能支撑正面候选、Books或“无遗漏”；如到达精确原件，只重开相应来源/本窗。
