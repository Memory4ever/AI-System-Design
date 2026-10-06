# 本日 MiMo More 的实际有限检查

2026-10-06，非作者独核。原首页 official-mimo.html/16official3.json 有 Paper8 与 Blog15。实际 GET 官方 CDN 的 index.c5195ace.js 确认 t.u 使用 static/js/async/；第一次漏 async 的两条 chunk 地址没有读到内容，后用真实路由恢复。

- [6159.4efb0769.js](https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js)：组件接收 blogs；m=o.slice(0,c)、p=o.slice(c)；剩余内容预加载并映射，data-expanded/aria-hidden 由 h 控制；More 只是展开/收起。
- [8557.2d420be2.js](https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/8557.2d420be2.js)：Blog initialVisibleCount=8，数组共15；后7项为 V2.5-Pro、V2.5、V2-Pro、V2-Omni、V2-TTS、V2-Flash、V2-Flash-HSS，与原首页全文抽取一致；不是尚未读的7页。数组没有日期字段，不能反推2025九月全部发布。

可用浏览器列表为空，IAB 不可用；未实际 UI 点按钮，结论来自真实官方 client 而非虚构点击或继承别日。Paper Sep19Audio/Jun4VL夹本窗；当前 Blog15 的有限身份检查完成，不展开15个当代页面全文，不授删除历史/其他发布无遗漏。
