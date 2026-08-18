# Rendered Listing Extracts — 2026-08-26

- Report window: `[2026-08-25T09:00:00+08:00, 2026-08-26T09:00:00+08:00)`
- Rechecked: `2026-08-26T16:10:00+08:00`
- Purpose: freeze the exact normalized listing evidence for official surfaces whose ordinary HTTP response was unavailable or insufficient for date closure. These extracts support discovery/date closure only; they do not support mechanism claims.

## SRC-OPENAI

- Endpoint: `https://openai.com/research/`
- Rendered official listing watermark: GPT release — `2026-07-09`；GPT-Live — `2026-07-08`；
  the next visible dated research/release items were `2026-04-23` and earlier.
- Closure operation: the official rendered research page crossed below the report window, so no OpenAI-only
  first-public event was established in `[2026-08-25 09:00, 2026-08-26 09:00)` Asia/Shanghai.
- Boundary: the archived ordinary-client response is a Cloudflare JavaScript challenge, not listing evidence.
  It is retained only to explain why a rendered official-page extract was required and is never used for a
  model, mechanism or release claim.

## SRC-GOOGLE-AI — Google Research Publications

- Endpoint: `https://research.google/pubs/`
- Rendered result: the 2026 filter exposed `229` publication records; the rendered page did not expose a complete day-precision order suitable for a window cutoff.
- Closure operation: all day-precision manuscript identities were reconciled against the archived 930-entry arXiv v1 query; the DeepMind sitemap was separately archived. No Google-only first-public event was established inside the window.
- Boundary: a year count is not evidence that all 229 items were first published in 2026, and it cannot fabricate a day timestamp.

## SRC-META-AI

- Endpoint: `https://ai.meta.com/research/`
- Rendered listing watermark: `WaiT for the Signal` — `2026-08-04`; next visible item — `2026-07-29`.
- Closure operation: the listing crossed below the window; manuscript identities were reconciled against the archived arXiv query.
- Boundary: ordinary HTTP access did not yield a stable response body, so no raw-body digest is asserted.

## SRC-XAI

- Endpoint: `https://x.ai/news`
- Rendered listing watermark: `Grok Bot is now included with more plans` — `2026-08-21`; the next visible Google Enterprise Agent Platform and Amazon Bedrock entries were dated `2026-08-19`.
- Closure operation: the dated listing crossed below the window.
- Boundary: product/news dates prove xAI publication events only; they do not disclose internal model mechanisms.

## SRC-MISTRAL

- Endpoint: `https://mistral.ai/news/`
- Rendered listing watermark: `Agentic Search` — `2026-08-20`; prior visible in-region inference item — `2026-08-11`.
- Closure operation: the dated listing crossed below the window.
- Boundary: the listing is a creator-primary release surface, not independent performance evidence.
