# Qwen动态目录：有限恢复停点

2026-10-04约16:13–16:15 BJT，实际使用in-app browser，仅恢复本日既有来源入口，未扩全站。

1. 首次请求带visible:false被拒：subagent不支持visibility配置，没有获得页面，不计目录核查。
2. 去掉visibility配置后实际创建tab3；赋值变量不存在报错但工具已返回该tab页面，随后按已返回tab3重新绑定，不重复创建。`https://qwen.ai/blog`实际AX只显示导航/下载/条款/2026footer，没有博客条目。
3. 点击页面实际“研究索引”，到`https://qwen.ai/research#research_research_index`。AX显示“研究 / 最新进展 / 研究索引 / 排序 / 探索前沿模型技术 / 前往Github”，仍无研究条目。
4. 实际读取该tab error/warn日志，唯一返回error：`Uncaught (in promise) TypeError: Cannot read properties of null (reading 'appendChild')`；timestamp `2026-10-04T08:13:53.110Z`；url `https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/6043.js`。这支持本次动态加载失败，不证明没有历史材料。
5. 已关闭临时tab。停止相同空目录路径和盲抓bundle；未调用未确认的API。

已取得p_home-index、p_layout、9e22d361三份JS及receipt：home引用module44467的V.cy，layout仅给请求拦截prefix`/api/v2/article`，shared未恢复module44467。三份JS200不支持目标目录已检查。最小替代是官方2025-11-18/19目标段原始列表、可核API响应或同期发布材料；只重开对应目录边界/具体事件，不授候选、Books、无遗漏或正面Coverage。
