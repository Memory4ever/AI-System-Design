# Required Daily Organization Receipt — 2026-08-26

- Window: `[2026-08-25T09:00:00+08:00, 2026-08-26T09:00:00+08:00)`
- Executed: 2026-08-26 11:10～14:40（Asia/Shanghai）
- Registry: `docs/RESEARCH_SOURCES.md` effective 2026-08-25
- Result: 19/19 Required Daily organization sources closed with zero in-window Source Family.

本文件保存规范化的 listing watermark 与 fallback reconciliation。它不是“已访问”的口头声明：每个来源都记录实际 endpoint、可复核的页面水位、原始响应摘要（能直接抓取时）和窗口判断。页面只给月份、动态渲染或拒绝普通 HTTP client 时，明确记录该限制，并使用注册表指定的 arXiv primary fallback 对 930 条 v1 封闭查询做机构身份 reconciliation。Fallback 只闭合本窗口候选发现，不被用来证明厂商未公开的内部机制。

## Archived Evidence

- 18 份可直接抓取的官方 HTTP response 已按原始 bytes 以 deterministic `gzip -n` 冻结在
  `organization-snapshots/`，文件名、raw bytes、raw SHA-256 与 gzip SHA-256 见
  `organization-snapshots/README.md`。
- OpenAI、Google Research、Meta AI、xAI 与 Mistral 的动态 listing 以规范化渲染摘录冻结在
  `rendered-listing-extracts-20260826.md`，SHA-256 为
  `49ebdcb957b33fea18b24e44bdabc60f5d74b6dba36e598bc3a4ff3115a7532f`。
- 这些页面在候选分母初次冻结后于 16:10～16:12 重新抓取并复核；动态页面的 runtime metadata
  和 repository update time 仍不作为 first-public evidence。下表 digest 均指向本次实际归档的复核快照，
  21-family 分母随后以新身份重新冻结，内容未发生变化。

## Closure Ledger

| Source ID | Official endpoint(s) | Frozen listing / response evidence | Raw response receipt | Window decision |
| --- | --- | --- | --- | --- |
| SRC-OPENAI | https://openai.com/research/ | rendered official listing: GPT release `2026-07-09`, GPT-Live `2026-07-08`; listing already crossed below the window | closure evidence is the normalized official-page extract in `rendered-listing-extracts-20260826.md`; archived ordinary-client response SHA-256 `cac52df29f63004fd01e7fafa322d714ff9afb8835abba20e87f011212cd53a1` is a Cloudflare challenge and only proves the access limitation | no hit; latest visible dated research/release precedes start |
| SRC-ANTHROPIC | https://www.anthropic.com/research | latest visible dated research item `2026-08-18`; next visible items `2026-08-13`, `2026-08-12`, `2026-08-10` | 309,818 bytes, SHA-256 `65647a597b806ea9bb817a5e3a64fc5d29b3265a2f4221531ad78f1d7261e589` | no hit; listing crossed below start |
| SRC-GOOGLE-AI | https://deepmind.google/research/ ; https://research.google/pubs/ ; https://deepmind.google/sitemap.xml | both registered publication endpoints were enumerated; the complete DeepMind sitemap had exactly one `2026-08-25` last-modified URL, `gemini-robotics-2-brings-whole-body-intelligence-to-robots`, whose official article states first publication `2026-07-30`; Google Research exposed 229 publications for 2026 and all day-precision paper identities were reconciled | archived DeepMind response 209,800 bytes, SHA-256 `2190fa8d988c14249903435b72701126a1786085f3115e6d6bd298c95d2f880f`; archived sitemap 84,881 bytes, SHA-256 `5de3590a8481b2a459d7c4683ac69e78783a0e4df77260ac911dd86ce2f4a740`; Google Research normalized extract in `rendered-listing-extracts-20260826.md` | no hit; sitemap `lastmod` was treated as revision metadata, not fabricated into a first-public event, and the only in-window revision watermark resolved to a July 30 family |
| SRC-META-AI | https://ai.meta.com/research/ | rendered official results listing latest visible publication `WaiT for the Signal`, `2026-08-04`; next visible `2026-07-29` | normalized rendered extract in `rendered-listing-extracts-20260826.md`; ordinary client timed out, so no raw-body digest is asserted | no hit; listing crossed below start |
| SRC-XAI | https://x.ai/news | latest visible official entries `Grok Bot is now included with more plans` `2026-08-21`, then `Grok 4.6 on Google Enterprise Agent Platform` and Amazon Bedrock entries `2026-08-19` | normalized rendered extract in `rendered-listing-extracts-20260826.md`; ordinary client timed out, so no raw-body digest is asserted | no hit; latest visible event precedes start |
| SRC-MISTRAL | https://mistral.ai/news/ | latest visible official technical/product entry `Agentic Search` `2026-08-20`; prior `In-region inference...` `2026-08-11` | normalized rendered extract in `rendered-listing-extracts-20260826.md`; ordinary client timed out, so no raw-body digest is asserted | no hit; listing crossed below start |
| SRC-QWEN | https://qwenlm.github.io/ | latest dated cards in returned listing were `2025-09-23`, `2025-08-19`, `2025-08-04`; linked arXiv identities reconciled | 17,307 bytes, SHA-256 `f874cc1c99c3454e3ea933dac9790e5cb329e25bf5766b270ab9e38bd780bffe` | no hit |
| SRC-DEEPSEEK | https://www.deepseek.com/ | latest explicit update timestamp in returned official surface `2026-08-20` | 86,879 bytes, SHA-256 `6ae198b3e4dfab6a30ea68083a7cc51cf42b91addf55e38961138d606bb887e3` | no hit; latest update precedes start |
| SRC-MOONSHOT | https://platform.kimi.com/blog ; https://github.com/MoonshotAI | blog listing crossed from `2025-11-07` downward; organization repository surface and linked arXiv identities reconciled | blog response 13,388 bytes, SHA-256 `77654f9e56dd34ab8213fb9092fc1d82cc4719375bf910a16182c59ff53654c5` | no in-window blog, release or new paper family |
| SRC-ZAI | https://docs.z.ai/llms.txt ; https://docs.z.ai/release-notes/new-released ; https://github.com/zai-org | latest dated release note `2026-08-18`; documentation index and repository identities reconciled | index 9,571 bytes, SHA-256 `426ed825c806d3253430862403e9548cedb792bb08c8ed60cdf8828b082693a5`; releases 273,362 bytes, SHA-256 `8ecbc68f6e99d8f9a2450a9acbb6e3e1bb0b8fc7651c1f71711366cca05cdcdf` | no hit |
| SRC-MINIMAX | https://www.minimax.io/ | actual serialized `publishedAt` values, rather than render/current-date strings, crossed below the window; latest visible listed article before start was `2026-08-13` | archived response 383,774 bytes, SHA-256 `b90fb5ab3090d04a4d229141c290b931e29009bf99ce6a5b5f3a58ad4168ba2c` | no hit; ignored `2026-08-26` runtime/render metadata and did not misclassify it as publication |
| SRC-BYTEDANCE-SEED | https://seed.bytedance.com/en/ | publications surface crossed below window; latest explicit publication observed `2026-08-05`; arXiv identities reconciled | 56,689 bytes, SHA-256 `be21eea5487fb06db4d3081c08f1151f5a25a0b7dfb44db9a969bbbf21dc0092` | no hit |
| SRC-BAIDU-ERNIE | https://ernie.baidu.com/blog/zh/publication/ | finite returned listing contained exactly four cards: `ERNIE 4.5 Technical Report` (2025), `PaddleOCR-VL` (2025), `PaddleOCR-VL-1.5` (2026), and `ERNIE 5.0 Technical Report` (2026); the complete four-title inventory was reconciled to its manuscript identities rather than assigning a day to year-only metadata | 16,213 bytes, SHA-256 `c81630562a7d6ff6d1c914fd4f3528dd0b5c7a910eb36b1339c8839ec47c515a` | no hit; the finite card set contains no new organization-only release and no title first published in the window |
| SRC-TENCENT-HUNYUAN | https://github.com/Tencent-Hunyuan | organization listing enumerated. `UniRL` update `2026-08-26T03:49:31Z` (11:49:31 Beijing) and `Hy-MT2` update `2026-08-26T01:48:04Z` (09:48:04 Beijing) were both after the exclusive 09:00 cutoff; earlier visible updates were `2026-08-19` or older | archived response 276,977 bytes, SHA-256 `251e97d88404d623bc62f4f2adeece961c927a3c38a6e2c68e8911a2e83d5b70` | no hit in the half-open window; post-cutoff changes belong to the next Daily |
| SRC-HUAWEI-NOAH | https://noahlab.com.hk/news | dedicated frozen receipt `huawei-noah-news-20260826.md`; latest dated item `2026-08-05` | archived response 65,574 bytes, SHA-256 `dbe0576d02f5d9aca46409261585b878e0ef0fc061bb7488cd2fe1746bb633ee`; see sibling receipt | no hit |
| SRC-SHLAB | https://www.shlab.org.cn/ | returned research/news surface enumerated; latest visible dated cards precede the window and linked arXiv identities were reconciled | 88,799 bytes, SHA-256 `7b1be7ecb6a9665ef3bc2e81d85b2f9503ff65efbe99fee3ff36de2085a144b7` | no hit |
| SRC-STEPFUN | https://www.stepfun.com/research ; https://chat.stepfun.com/research | the working `chat` route returned a server-rendered finite `blogPosts` array with 14 bilingual cards / 8 unique slugs; newest unique entries were `NextStep-1` (`2025-08-15`) and `StepFun-Prover Preview` (`2025-08-13`), followed by Step3/StepMesh (`2025-07-31`); the `www` route returned `not_found` and was excluded | archived working response 78,332 bytes, SHA-256 `97bf1948b8bd67a3e9c5b932d977848354d0c3386a57d423c36a6f738d24f64a`; its separate sitemap was not used as date evidence because it bulk-refreshed unrelated `lastmod` values | no hit; the complete embedded card array crossed below the window and no arXiv fallback was needed for organization-only closure |
| SRC-XIAOMI-MIMO | https://mimo.xiaomi.com/ | publication listing crossed from `2026-06-29` to `2026-03-13` and older | 43,869 bytes, SHA-256 `bc3ecff5c7cb03a86eb4703bd7c5311af1a3472c5bdf6df7b842fb9118de4ea3` | no hit |
| SRC-INCLUSION-AI | https://www.inclusion-ai.org/publication/ | finite returned listing contained exactly five selected-publication cards: `Every FLOP Counts`, `AWorld`, `Ming-omni`, `Ming-lite-uni`, and `M2-Reasoning`; every card is explicitly dated 2025 and identities were reconciled | 9,130 bytes, SHA-256 `5c911d8e89dca17602c0b33860671ff13566046e21c0a6f19e99c40cfecb6fc7` | no hit; complete five-card inventory crossed below the window |

## Reconciliation Boundary

- Organization pages prove only their own public listing, release or artifact facts.
- The arXiv fallback is the archived 930-entry Atom result in `arxiv-20260826.xml.gz`; it is used only for paper identity and first-public reconciliation.
- A page update after `2026-08-26T09:00:00+08:00` is not silently pulled backward. Tencent’s two post-cutoff repository updates are explicitly deferred to the next Daily window.
- Search/render extraction is not used to support a mechanism claim. All 21 retained technical claims are reviewed from their versioned arXiv v1 primary evidence.
