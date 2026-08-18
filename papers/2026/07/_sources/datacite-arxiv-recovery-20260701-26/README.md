# 2026-07-01～26 arXiv / DataCite Recovery Snapshot

本目录用于恢复官方 arXiv API 持续连接重置时的确定性枚举。`SRC-ARXIV` 的注册 fallback
`SRC-DATACITE` 只承担 `10.48550/arXiv.*` DOI identity、arXiv subject、v1 Submitted timestamp 与
abstract metadata；机制、实验、revision 与 benchmark claim 仍由精确 arXiv v1 正文承担。

- Retrieved At: `2026-08-26T20:51:11.325710+08:00`
- Enumerated DOI records: `41705`
- Contract-category records in strict replay window: `10087`
- Frozen AI-System candidate families: `350`
- Canonical inventory artifact: `datacite-candidate-inventory.json`
- Canonical inventory SHA-256: `e8f3059965e312a6f3a1f746d69253342fb26baaaf0c68506ff0d2ca4c89ade1`

## Current Closure State

- Coverage：fresh-context review 已确认 350 个 family 的北京时间 bucket、逐日 ledger 与 canonical inventory
  完全一致；确定性 Coverage scope 通过。
- Evidence：350/350 个 family 均已取得最终审阅状态：199 个 `deep_complete`、53 个
  `standard_complete`、98 个 `closure_complete`；Access Status 全部为 `accessible`，Pending、Blocked、
  Unverified 与 Disputed 均为 0。Standard/Deep 机制结论回到 exact-version primary evidence；Closure 只关闭
  identity、日期与拒绝理由，不借 metadata 建立技术结论。
- Books：350/350 个 family 均已完成最终判断：136 个 `Integrate`、111 个
  `No Change — Existing Coverage`、9 个 `Weekly Only — Context`、93 个
  `Rejected — Low Durability / Out of Scope`，以及 1 个
  `Version Fact / Mechanism Not Disclosed`。对应 26 份 Daily 的 Books Gate 均已通过。
- Semantic Audit：26/26 份 Daily 的 Coverage、Evidence、Deep Analysis Selection 与 Books 四个 scope
  均无未解决 finding；机器合同复验同时通过。
- 去重材料清单 [`primary-material-requests.tsv`](./primary-material-requests.tsv) 当前只保留表头，表示没有
  尚待用户补充的 July 01～26 primary material。

逐日 Coverage Receipt 必须引用上述 artifact 与 digest；本 README 是说明文件，不充当 manifest，因而其自身
文件 hash 不参与 Coverage Gate。

## Query Partition

DataCite 普通页码查询的单查询上限为 10,000 条，因此使用互斥 DOI 前缀。`2606.2* / 2606.3*` 覆盖 7 月 1 日窗口可能出现的 6 月尾部 v1；`2607.0* / 2607.1* / 2607.2*` 覆盖其余窗口。每个分区独立闭页，合并 identifier 必须唯一。

## Snapshot Files

| File | Raw bytes | Raw SHA-256 | Gzip SHA-256 |
| --- | ---: | --- | --- |
| `datacite-arxiv-2606-g2-page-01.json.gz` | 2447045 | `51e732cfcfce6dc65e1b336d4be9c8e2e1850f6742cc2fb7f28e7c0610b58192` | `0f54dea0767a7428c823e23c123ce358447e2f522ca1f73477b8278eb4f89214` |
| `datacite-arxiv-2606-g2-page-02.json.gz` | 2319193 | `bd234fd635329e594c276c1f13c7f5c632800cab62c18865b6fb0a79d52dc57b` | `df8fc0517ab17104f30358f10a289851878aa6a7e392f09e40493bd9ac22825e` |
| `datacite-arxiv-2606-g2-page-03.json.gz` | 2238509 | `b7f8f9f36dc11ccf50fcec93654d9bfd373a8d8b03305c11533a4aceb0e63271` | `d4c46a944338ec9b0a4a0678c854f257320b17ed3779926b201f48e68cbd75d3` |
| `datacite-arxiv-2606-g2-page-04.json.gz` | 2229509 | `c5e5990ef0adbb5d205e045cee6fa88871b57a12ba831ceb2344791a3677c3be` | `e58dd8dea0c1e87d44fff89d118471773e6b0252164897fc28c8dd44d101f5cd` |
| `datacite-arxiv-2606-g2-page-05.json.gz` | 2266772 | `cb3eab56017e29ee06ada45244d6f01dee49129996373f30c6136bda90603e79` | `ebf47df54765b42007b6c9279712fff56fafebb5b3adcdcfbcd13b60b2c6ff85` |
| `datacite-arxiv-2606-g2-page-06.json.gz` | 2448779 | `48293f996da242e2ca9143a78ae50e0b80b4e019f038d1a0a3dfa69bb1174479` | `44ee36ad96f4b1e9b808e661eaee607e2246db61dfd8c4fce8a8066fd45e2cbe` |
| `datacite-arxiv-2606-g2-page-07.json.gz` | 2420357 | `f29656c0a599c50dac4bcff3c287aea0a497b55b1e9f8152d53fc7f7933d030d` | `0386d662702787b254bbe9662eae693d7ff1c589a05e5da3566735f1b3024854` |
| `datacite-arxiv-2606-g2-page-08.json.gz` | 2444143 | `bf666d98e3d2187b9ff4f349df05aa89d3555c04ce1ed14e53d7cb6944dbe050` | `6662f635776f33443b1be742d008b49ee670d591a4881552ab0550c1a8efcdc9` |
| `datacite-arxiv-2606-g2-page-09.json.gz` | 2430181 | `0bd2549ae4f178085a9d9a54334fa1cf91b950a528fd87972e84b1ed3b957b02` | `9a28a6a125edd1da9236580186cdc0de55dfc80772aef553265fd5ac4d49a903` |
| `datacite-arxiv-2606-g2-page-10.json.gz` | 2458944 | `7bff05199c943d78e44b96bd51bed151b7e460f59418a99f8957933f1957f353` | `ed50500053e01d842650ef572b8a4ae8a818b962e40bde6c92a402cd5480f397` |
| `datacite-arxiv-2606-g3-page-01.json.gz` | 2264791 | `30162656ca9f128c3b13c80aee20df29d70d4e9651b2755eb72729558c8c4929` | `68f0f316111da953af57cf5f4c94faf243528ace867d1e29d800b2d7b2f4ba1b` |
| `datacite-arxiv-2606-g3-page-02.json.gz` | 2222911 | `511d19f7e6cb4ccbe986941af8f5404a9ae7721a52c5be8f13417200e3c06061` | `02249af41deb4435579aeb835568bc802b92f376eb4307d99990554789038e4d` |
| `datacite-arxiv-2606-g3-page-03.json.gz` | 86493 | `a8ce57ad41f15d423eb3a961c38d6539cb51bd4106615ebfe085a60c0b05a9df` | `85f3bceb3a1d4511663944db6885d917d9caf90b7e64dd91617681cf5e7cc150` |
| `datacite-arxiv-2607-g0-page-01.json.gz` | 2443350 | `b41571f8af9e3d40a0e96d048ed6447155f99f332f6974498d518e1c059d6e8a` | `d309787cf41a58228cf224304305330be2084b23fa7ff548d71c18a8c22dfa75` |
| `datacite-arxiv-2607-g0-page-02.json.gz` | 2263731 | `574ca3e514770b42ad322d4ec832b54b666f85ebf71784a3152a10ba945071bb` | `4bc5da3f07cedce66b57d56825d063c070f1fb90a6afbc798006cb37a267dbdd` |
| `datacite-arxiv-2607-g0-page-03.json.gz` | 2220432 | `b7087338a0b822bb95f72d093154bfcc2ba660dfc7b3ccc3db54b02453aee5ba` | `e78215856cc11fbc3093c05cc713d1b6e1fd355a733ff28536477e137720c727` |
| `datacite-arxiv-2607-g0-page-04.json.gz` | 2220032 | `23e621798a3b0fa7bd226b80db32148be4d710ee74922e9a74c0fe01366eaf3f` | `9617163bb69eec4bce7538e250ac974d3260ad468758fa765b26f03bd46f4a2d` |
| `datacite-arxiv-2607-g0-page-05.json.gz` | 2210703 | `66bdc3d88d1b0700a9189a2d520af24633e37bd878fcc5efbd05fe92a019554a` | `48e4a38ca4589b028fc153c96e95eb2dae059e34fd904f1808e8dd912207259f` |
| `datacite-arxiv-2607-g0-page-06.json.gz` | 2211441 | `3339348847bb3d917cd4aef3c15f597406ce1e3f4c4508229727d6e305d09638` | `98a93a00bff98a654b89e8feebae559cf22acc307e507364f0bfb4c3c882860a` |
| `datacite-arxiv-2607-g0-page-07.json.gz` | 2220850 | `df03dbb4b92670077a03d65224e6232e7931cafae40f21789f70783b93a390bc` | `9e137e96aec22e5898cac0a0e4899b4dbe523305426ae5886eac4997b476af13` |
| `datacite-arxiv-2607-g0-page-08.json.gz` | 2253576 | `e5bb8fd0be6fca63baeb6b04e1af097410480166c938eccf5be232076eb1fe22` | `dd3c1a89be61798c7d05aa68c765a6543727af11bc59197eddde427e55c123b4` |
| `datacite-arxiv-2607-g0-page-09.json.gz` | 2192048 | `00300bb81b9eb9b3d4a2b743f45e86ec413f58a151f2732c1693fa10bd6a1575` | `9092e9940054cf7a715f2d362186556466f01b3f2e17ba518442d154095e2c96` |
| `datacite-arxiv-2607-g0-page-10.json.gz` | 2213936 | `6bb1ff2b4a7f06fd635b91b61f3eabe3c90e666ef9c0d80dff9e4f0ded9b2da1` | `c96fdaa711086c4b643b9aaa6538dd97ff9e7e863ce46469a28eb380f4716f77` |
| `datacite-arxiv-2607-g1-page-01.json.gz` | 2464810 | `c882d31cd3e2a23338019f222eb8e913d47551d28729cf4bda2b572c39856a52` | `d0117ea9a0c25c5940b4ac11906245497174d422b17943e18809335bf9b14581` |
| `datacite-arxiv-2607-g1-page-02.json.gz` | 2294559 | `cfe01b81ec3131f2bd22a9b28433bbdd7b744a40e26b5644e8c5c5dce438b93b` | `001bf065e2187bd59ca2c75e1fc9b051c4ebe2de154e70e6e43892e340383f8f` |
| `datacite-arxiv-2607-g1-page-03.json.gz` | 2244883 | `7b7f465f2a42c6ac721f12d5cb70aa13a71846b66247bcd0ac49d265bfa8afc9` | `7e8de054403970233ca980b5de8704e863786f12e0684319c50f9f92cebf621a` |
| `datacite-arxiv-2607-g1-page-04.json.gz` | 2217514 | `09ed57f7472160d185dbed9e959e9901d453d80717a2dccad5e827bf70ad9380` | `0496e3769602dab01feba55bf3b95b3ccf8a8de4cd6b3a071eb3d9c5cd6ce9d6` |
| `datacite-arxiv-2607-g1-page-05.json.gz` | 2241745 | `a476bf7a96c51beeede4fa70b0fe3c2eb835be25c82bff1536150e84e9bfe3c0` | `345768180b2672a913bcee1195651f2a93fac7a4ea65c7d9723c85a0e922f4d1` |
| `datacite-arxiv-2607-g1-page-06.json.gz` | 2220166 | `c30547d0e6b89577cfaca110f787aa044eb38f729bbe3f8c53025f30ca963e90` | `648daab210aeeef84c18bb3598b79053b9bf5aa047a4b0c0d9a8880e99969d69` |
| `datacite-arxiv-2607-g1-page-07.json.gz` | 2230248 | `88c20e69302316fe90af0cb9e5a2e28235048dc291630b41dd724973d34e1ab3` | `e3c5add0de316a65624b99da44ed7c9f05bcccf1462b4baf23bf8510823ef9ae` |
| `datacite-arxiv-2607-g1-page-08.json.gz` | 2242034 | `6538c53ee0c2e2e4ff89b43b4127111884b32b159e38cc201c641a2276ffedc9` | `3d00f60ea9ca342e6e2c5b143171d83f04a9e2944904a861290ad81546803925` |
| `datacite-arxiv-2607-g1-page-09.json.gz` | 2220113 | `7d95d0124ebf18cbc9ba2a90a809b3de7216bdb5beb31e563d0cd2e792b58d56` | `00e3746f5a9092d085fbeab888a761cd4737eb38ba3430234700a6693aa8f7a7` |
| `datacite-arxiv-2607-g1-page-10.json.gz` | 2205600 | `24ac5d0de8197bc74668dc3e85f21c4e5a9846196850d720f8d5ffc3ec2eddaa` | `7e7ac340dca71d002c5ca796b3823e30b123a739548aed0366b33101683a588d` |
| `datacite-arxiv-2607-g2-page-01.json.gz` | 2432003 | `a986a48b41d7d5be7348a9482f99b8ad2508519f8fbb0c07ca0b6993e2db7959` | `65460ae69898f7a596e9913f3ad86c44937e466b4da1353c08e9215ba71d68a1` |
| `datacite-arxiv-2607-g2-page-02.json.gz` | 2256769 | `1f12345b74bfb468d02840b5306c1c6fca97ca376a9d751ef2d3f630a172eb05` | `66559f5ad85d34e9a7f99615c1b061214563411fcac2881d5c273a4c0e4d6d25` |
| `datacite-arxiv-2607-g2-page-03.json.gz` | 2228516 | `128b87a9e91a04c9ea717916e0a5cfabb6a3dfc78644b254fca200bbe2e119e4` | `d070176a67d0167d3dde9b1fc15fbe44644959d07db63fafc4f8e2318570a3af` |
| `datacite-arxiv-2607-g2-page-04.json.gz` | 2255681 | `319f1c7481d0b0251cd0dfbb9849ad61bd09b87c9e75dd92db601b9f93f20669` | `679b11b07bd8c495ca9d63d50b4b15f2a6ce893a1a7d680908207a915fc66344` |
| `datacite-arxiv-2607-g2-page-05.json.gz` | 2259502 | `85c7af93d460bcac02b6b180b070c159b371e404e04c6b86d105e591bdfd0c28` | `0a1d69b37de3c65002a01712f150176fa95273e78101606d755251bdeb4df11b` |
| `datacite-arxiv-2607-g2-page-06.json.gz` | 2258563 | `c777dc0b24b1b8cc12795f024db85c480578ffe66d339bc3323d02dd8f12fc84` | `30ceeafbd6e476bf9a9df8def3da02dece8d339f40393afa8b0a9699a68d68d3` |
| `datacite-arxiv-2607-g2-page-07.json.gz` | 2213375 | `6f9037fc18afcdd794a4ae8453a657274bb82c6fe3087844508ff38601708c61` | `0b4d72508764c19338cdd0c95603087acdeb4a0585ea8b69059a04aea49d5454` |
| `datacite-arxiv-2607-g2-page-08.json.gz` | 2237150 | `74b44112798fbe2b86eabd821f249fb4e0c3816396437d5cee07515a5904a7df` | `0d6861c2eaccb01db0909937b91adcd2b91433f652dd240e2118ed08e88cb594` |
| `datacite-arxiv-2607-g2-page-09.json.gz` | 2214786 | `392d741a800eb7e08a93bf1424c86dd3447c1ffc5e9185ea4f8d548e39331121` | `2f0eb1169a30e86443d9750f11ed102a4ecba0388a4e9abef95664b5cfc37817` |
| `datacite-arxiv-2607-g2-page-10.json.gz` | 1482195 | `07a83f26dac6cd90d2dac6243940becd17391165d063b46e399ab595d7fde726` | `8bb3f37a6372459c820097e925b9c828d79327e36e0c9e535f00b0b6f14253d5` |

## Routing and Evidence Boundary

- Daily 归档窗口按 `[前一日 09:00, 当日 09:00)`；北京时间 09:00 及以后提交的 v1 归入下一日报告日。
- route filter 要求标题同时体现 AI model 与 system mechanism，或已存在于 W27～W30 的完整 Source Review；垂直应用中偶然出现 Transformer/LLM 不进入分母。
- DataCite metadata 不支持 Standard/Deep mechanism claim。需要较深路由的 family 必须回到 arXiv v1 HTML 或有等价 provenance 的正式全文。
