# Qwen3.5-Omni exact official API date conflict

2026-10-02非作者mar02一次指定目标定点原content字段核，不是canonical页面日期，也不执行私有git_url。原API extra.date与同目标content的JSONLD/meta/visible原日期冲突，不能默认选择任一。content是316388字符/329201 UTF-8 bytes。完整小日期原包如下，省略无关benchmark表。

```text
ENDPOINT https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US RESPONSE_BYTES 4781799 TARGET {"id": "73a298ad-b280-49d1-8090-7e52e0e2a068", "title": "Qwen3.5-Omni: Scaling Up, Toward Native Omni-Modal AGI", "path": "qwen3.5-omni", "extra": {"git_url": "https://code.alibaba-inc.com/DamoAGI/qwen-blog/blob/qwen_ai/content/blog/qwen3.5-omni/index.md", "description": "", "introduction": "Qwen3.5-Omni is Qwen’s latest generation of fully omnimodal LLM, supporting the understanding of text, images, audio, and audio-visual content. Both the Thinker and Talker in Qwen3.5-Omni adopt the Hybrid-Attention MoE. Qwen3.5-Omni series includes Instruct versions in three sizes: Plus, Flash, and Light, with support for 256k long-context input. The model can process more than 10 hours of audio i", "tags": ["Release"], "cover_small": "https://img.alicdn.com/imgextra/i1/O1CN01gJhkPX1gZVB49xEk1_!!6000000004156-2-tps-1590-954.png", "date": "2026-03-30T04:00:00+08:00", "author": "QwenTeam", "readTime": 94, "wordCount": 18899}} CONTENT_BYTES 329201
CONTENT_PREFIX <!doctype html><html lang=en dir=auto><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content="IE=edge"><meta name=viewport content="width=device-width,initial-scale=1,shrink-to-fit=no"><meta name=robots content="index, follow"><title>Qwen3.5-Omni: Scaling Up, Toward Native Omni-Modal AGI | Qwen</title>
<meta name=keywords content="Open-source"><meta name=description content="QWEN CHAT 
TERM datePublished MATCHES 1
RAW /blog?id=qwen3.5-omni}, author = {Qwen Team}, month = {March}, year = {2026} } ","wordCount":"14095","inLanguage":"en","datePublished":"2026-01-07T04:00:00+08:00","dateModified":"2026-01-07T04:00:00+08:00","author":{"@type":"Person","name":"Qwen Team"},"mainEntityOfPage":{"@type":"WebPage","@id":"https://qwenlm.
TERM dateModified MATCHES 1
RAW , month = {March}, year = {2026} } ","wordCount":"14095","inLanguage":"en","datePublished":"2026-01-07T04:00:00+08:00","dateModified":"2026-01-07T04:00:00+08:00","author":{"@type":"Person","name":"Qwen Team"},"mainEntityOfPage":{"@type":"WebPage","@id":"https://qwenlm.github.io/blog/qwen3.5-omni/"},"publisher":
TERM article:published_time MATCHES 1
RAW ath%20of%20image%20for%20opengraph,%20twitter-cards%3E"><meta property="article:section" content="blog"><meta property="article:published_time" content="2026-01-07T04:00:00+08:00"><meta property="article:modified_time" content="2026-01-07T04:00:00+08:00"><meta property="og:site_name" content="Qwen"><meta name=twitter:car
TERM article:modified_time MATCHES 1
RAW cle:section" content="blog"><meta property="article:published_time" content="2026-01-07T04:00:00+08:00"><meta property="article:modified_time" content="2026-01-07T04:00:00+08:00"><meta property="og:site_name" content="Qwen"><meta name=twitter:card content="summary_large_image"><meta name=twitter:image content="https://q
TERM January 7 MATCHES 1
RAW -Omni: Scaling Up, Toward Native Omni-Modal AGI</h1><div class=post-meta>&lt;span title='2026-01-07 04:00:00 +0800 CST'>January 7, 2026&lt;/span>&amp;nbsp;·&amp;nbsp;67 min&amp;nbsp;·&amp;nbsp;14095 words&amp;nbsp;·&amp;nbsp;Qwen Team&nbsp;|&nbsp;Translations:<ul class=i18n_list><li><a href=https://qwenlm.gi
TERM 2026-01-07 MATCHES 5
RAW h,%20twitter-cards%3E"><meta property="article:section" content="blog"><meta property="article:published_time" content="2026-01-07T04:00:00+08:00"><meta property="article:modified_time" content="2026-01-07T04:00:00+08:00"><meta property="og:site_name" content="Qwen"><meta name=twitter:card content="summary_la
RAW a property="article:published_time" content="2026-01-07T04:00:00+08:00"><meta property="article:modified_time" content="2026-01-07T04:00:00+08:00"><meta property="og:site_name" content="Qwen"><meta name=twitter:card content="summary_large_image"><meta name=twitter:image content="https://qwenlm.github.io/%3Cli
RAW -omni}, author = {Qwen Team}, month = {March}, year = {2026} } ","wordCount":"14095","inLanguage":"en","datePublished":"2026-01-07T04:00:00+08:00","dateModified":"2026-01-07T04:00:00+08:00","author":{"@type":"Person","name":"Qwen Team"},"mainEntityOfPage":{"@type":"WebPage","@id":"https://qwenlm.github.io/blo
TERM 2026-03-30 MATCHES 0
```

必要核心实际读到：Hybrid-Attention MoE Thinker/Talker、原生turn-taking intent识别以区别backchannel/background、ARIA (Adaptive Rate Interleave Alignment)动态对齐text/speech单位。ARIA具体机制potential而非仅版本/榜单；目前只preface描述，未核架构详细定义或证明对照，不采用数量/效率/普遍stability保证。日期终态隔离：需官方勘误、首次公开事件timestamp或能解释Jan7正文与Mar30extra原值的正式version身份；不猜旧canonical404、不扩JS/私有repo/全版本。
