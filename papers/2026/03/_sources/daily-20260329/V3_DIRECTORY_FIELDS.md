# 2026-03-29 actual directory fields

本日2026-10-02独立只读返回，不继承其他日判断。正确Hunyuan POST https://api.hunyuan.tencent.com/api/blog/publicList JSON renderType0/pageNum1/pageSize20；Seed GET https://seed.bytedance.com/api/get_article_list_v2 ，article_type1/page_token20与40，type2/page_token0，publish_year2026/count100/order_descfalse，header x-tt-locale US。字段datetime只是原秒/毫秒转换，不擅作firstpublic。

## Hunyuan

```text
bytes 309375 code 0 totalNum 9 rows 9
100116 When Do Larger Batches Help Scale LLM Reinforcement Learning? 1789707529 1790006400 2026-09-18T04:58:49+00:00 2026-09-21T16:00:00+00:00
100100 Introducing Hy4 preview 1787896672 1787846400 2026-08-28T05:57:52+00:00 2026-08-27T16:00:00+00:00
100091 From LR to ELR: A Better Heuristic for Pretraining Dynamics 1785989409 1785945600 2026-08-06T04:10:09+00:00 2026-08-05T16:00:00+00:00
100087 Hyra: A simple yet effective scaffold for general discovery 1784111171 1784599200 2026-07-15T10:26:11+00:00 2026-07-21T02:00:00+00:00
100064 Introducing Hy3 1783319811 1783440000 2026-07-06T06:36:51+00:00 2026-07-07T16:00:00+00:00
100039 Real life is where context gets hard 1777227059 1777532400 2026-04-26T18:10:59+00:00 2026-04-30T07:00:00+00:00
100061 Hy3 preview: The First Step in Rebuilding the Hy model 1782369407 1776873600 2026-06-25T06:36:47+00:00 2026-04-22T16:00:00+00:00
100015 Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping 1770971763 1770971763 2026-02-13T08:36:03+00:00 2026-02-13T08:36:03+00:00
100025 Learning from context is harder than we thought 1770090898 1770090898 2026-02-03T03:54:58+00:00 2026-02-03T03:54:58+00:00
```

## Seed1_20

下列None为首次误取不存在的Title键的解析占位，不是原API缺题名。已独立正确读取`ArticleSubContentEn.Title`全部18/20/14行；日期/ID原值不变。跨窗必要题名定位：1992=veScale-FSDP: Flexible and High-Performance FSDP at Scale；1336=Hessian-informed machine learning interatomic potential towards bridging theory and experiments；1994=GPU Accelerated Minimal Auxiliary Basis Approach TDDFT for Large Organic Molecules；1667=Towards Robust Sequential Decomposition for Complex Image Editing；type2 2155=Dola-Seed-2.0-Preview Model Release on Arena、1202=ByteDance Seed 2027 Foundation Model Campus Recruitment is Now Open (Internships Included)。这是字段解析纠正，不赋予目录日期firstpublic含义。

```text
bytes 47564 rows 18 total 82 next 40 hasmore True
rowkeys ['ArticleMeta', 'ArticleSubContentEn', 'ArticleSubContentZh']
1992 None 1772020800000 2026-02-25T12:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2602.22437'}]
1412 None 1772121600000 2026-02-26T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2602.24286'}]
1420 None 1772121600000 2026-02-26T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2604.16322'}]
1411 None 1772294400000 2026-02-28T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.01070'}]
1607 None 1772294400000 2026-02-28T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.01223'}]
1644 None 1772380800000 2026-03-01T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.01502'}]
1664 None 1772380800000 2026-03-01T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2606.18524'}]
1424 None 1773244800000 2026-03-11T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.12233'}]
1414 None 1773504000000 2026-03-14T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.14425'}]
1426 None 1773590400000 2026-03-15T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.15619'}]
1661 None 1773936000000 2026-03-19T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://openreview.net/pdf?id=h2yhNcbwSL'}]
1407 None 1774022400000 2026-03-20T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.20616'}]
1337 None 1774195200000 2026-03-22T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.22274'}]
1334 None 1774281600000 2026-03-23T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.23386'}]
1428 None 1774281600000 2026-03-23T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.23500'}]
1606 None 1774368000000 2026-03-24T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.24278'}]
1335 None 1774454400000 2026-03-25T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.25583'}]
1336 None 1774454400000 2026-03-25T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.25373'}]
```

## Seed1_40

```text
bytes 54345 rows 20 total 82 next 60 hasmore True
rowkeys ['ArticleMeta', 'ArticleSubContentEn', 'ArticleSubContentZh']
1994 None 1774958400000 2026-03-31T12:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2603.29257'}]
1430 None 1775577600000 2026-04-07T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2604.07026'}]
1650 None 1775664000000 2026-04-08T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2604.08702'}]
1657 None 1775750400000 2026-04-09T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2604.09258'}]
1586 None 1775836800000 2026-04-10T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://www.biorxiv.org/content/10.64898/2026.04.10.717613v1.full.pdf'}]
1670 None 1776009600000 2026-04-12T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2604.11521'}]
1589 None 1776182400000 2026-04-14T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2604.14148'}]
1652 None 1776268800000 2026-04-15T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2604.15311'}]
1635 None 1776614400000 2026-04-19T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2604.18292'}]
1443 None 1776787200000 2026-04-21T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/pdf/Seed3D_v2.pdf'}]
1669 None 1776873600000 2026-04-22T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2604.21921'}]
1605 None 1777132800000 2026-04-25T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2605.08962'}]
1637 None 1777478400000 2026-04-29T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2604.27505'}]
1654 None 1777564800000 2026-04-30T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2605.00503'}]
1665 None 1777564800000 2026-04-30T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2605.02657'}]
1639 None 1777824000000 2026-05-03T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2605.02134'}]
1587 None 1777996800000 2026-05-05T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2605.05460'}]
1629 None 1778083200000 2026-05-06T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/pdf/2605.06548'}]
1631 None 1778083200000 2026-05-06T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/abs/2605.06489'}]
1667 None 1778342400000 2026-05-09T16:00:00+00:00 [{'ExternalLinkType': 1, 'Link': 'https://arxiv.org/abs/2605.09233'}]
```

## Seed2

```text
bytes 24851 rows 14 total 19 next  hasmore False
1939 None 1770825600000 2026-02-11T16:00:00+00:00
1806 None 1770912000000 2026-02-12T16:00:00+00:00
1801 None 1770998400000 2026-02-13T16:00:00+00:00
2155 None 1771171200000 2026-02-15T16:00:00+00:00
1202 None 1774972800000 2026-03-31T16:00:00+00:00
1798 None 1775664000000 2026-04-08T16:00:00+00:00
2132 None 1776873600000 2026-04-22T16:00:00+00:00
2152 None 1781798400000 2026-06-18T16:00:00+00:00
1949 None 1782172962000 2026-06-23T00:02:42+00:00
1950 None 1783353600000 2026-07-06T16:00:00+00:00
2159 None 1783440000000 2026-07-07T16:00:00+00:00
1788 None 1784476800000 2026-07-19T16:00:00+00:00
1970 None 1785427200000 2026-07-30T16:00:00+00:00
2186 None 1785859200000 2026-08-04T16:00:00+00:00
```
