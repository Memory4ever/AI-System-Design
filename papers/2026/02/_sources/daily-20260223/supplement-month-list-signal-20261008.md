# 月份列表恢复的必要字段

实际检查URL：`https://arxiv.org/list/cs.CL/2026-02?show=2000`，HTTP200，响应3356064字节。仅为具名日期核验检查标题、日期头和2602.19008身份片段；未逐项读取/筛选月份标题库存。

实际HTML头：

```html
<title>Computation and Language Feb 2026</title>
<h1>Computation and Language</h1>
<h2>Authors and titles for February 2026 </h2>
```

同响应2602.19008出现片段：

```html
<dt>
  <a name='item1049'>[1049]</a>
  <a href ="/abs/2602.19008" title="Abstract" id="2602.19008">
    arXiv:2602.19008
  </a>
```

列表日期恢复脚本期望h3和紧贴`href=`，实际只有月份h2、`href =`带空格；所以原保存`headings=[]/matched=[]`是解析不适用，不是零命中/身份不存在/没有公开。月份列表不能证明具体Feb22公告，不继续全月或后周标题审阅。仅保存上述必要片段；完整月表没有变为本日证据队列。
