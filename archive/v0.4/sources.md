---
name: etoro-pi-sources
description: Vetted source list for THE ASIA READ, DEEP DIVE and MARKET PULSE — named Asian analysts, institutional research and trade press, each with fetchability status, plus the sweep procedure that keeps monitoring cheap. Read before pulling material for a relay post.
version: 0.2
verified: 2026-08-24
---

# Source List — Asia

The premise of this account: **Asian disclosure and Asian analysts are ahead of
English-language coverage on semiconductors, and much of it is never translated.**
Taiwan and Japan are where the supply chain actually is, and their commentators
read it at a level the Western press does not.

That premise sets a hard rule for this file: **eToro's own news feed, and any
aggregator every eToro user already sees, are not sources.** Recycling them adds
nothing — the reader could see it without us. Everything here is external, and
most of it is Japanese or Traditional Chinese.

## Fetchability, tested 2026-08-24

| Platform | Status |
|---|---|
| EE Times Japan (itmedia) | **Works.** Series and article URLs both. |
| semiconportal.com | **Works.** Japanese semiconductor portal, dated articles. |
| technews.tw (科技新報) | **Works.** Traditional Chinese, heavy HBM/packaging coverage. |
| eettaiwan.com (電子工程專輯) | **Works.** Traditional Chinese, has RSS. |
| Medium | **Works.** Full text and dates retrievable. |
| TrendForce free news / press centre | **Works.** English, no translation needed. |
| Personal sites (yunogami.net etc.) | **Works**, but some index pages serve stale caches — check the date on what comes back. |
| X / Twitter | **Blocked.** `robots.txt` disallows automated access. No workaround. |
| Nikkei, DigiTimes | **Paywalled.** Headlines only; not usable as a cited source. |

**Consequence to be honest about:** real-time monitoring of X-based commentators
is not possible. Anyone whose primary output is X can only be reached through a
mirror (Medium) or through the trade press quoting them. Do not promise
social-feed monitoring the tooling cannot deliver.

## Tier 1 — Named analysts & research

### 湯之上隆 (Takashi Yunogami) — Japan, PRIMARY
Former Hitachi / Elpida / Selete process engineer, 16 years in microfabrication,
PhD Kyoto. Head of 微細加工研究所 (Institute of Microfabrication Research).
Frequently contrarian, called past downturns early — gives the account a bearish
counterweight it otherwise lacks.
- Column 「ナノフォーカス」 — https://eetimes.itmedia.co.jp/ee/series/11164/
- Own site — https://yunogami.net
- **Japanese only. Fetchable. The genuine information gap.**
- Do **not** record the instalment number here; it moves. Read the series index.

### 南川明 (Akira Minamikawa) — Japan, macro / geopolitics
Senior Consulting Director at Omdia; 20 years as a core analyst on JEITA's
long-range semiconductor outlook committee. Japan's most-quoted macro
semiconductor analyst. Strength: total-market forecasts, US-China controls,
supply-chain restructuring — complements Yunogami's process-level angle.
- EE Times Japan author page — https://eetimes.itmedia.co.jp/ (search 南川明); fetchable
- Nikkei topic page — https://www.nikkei.com/topics/EVP01077 (paywalled — headlines only)

### 和田木哲哉 (Tetsuya Wadaki) — Japan, equipment
The top-ranked semiconductor-equipment analyst in Japan. Ex-Tokyo Electron (1991),
ex-Nomura; ranked #1 in the precision/semiconductor-equipment category in both the
Institutional Investor and Nikkei Veritas analyst rankings for six straight years
to 2022; now at Mitsubishi UFJ Morgan Stanley. Directly relevant to the Tokyo
Electron / Disco / SCREEN positions.
- **Sell-side reports are not public.** Usable only via media interviews and his
  books. Track via EE Times Japan and Nikkei interview features. Lower publish
  frequency than Yunogami — reference source, not a regular relay.

### 郭明錤 (Ming-Chi Kuo) — Taiwan
TF International Securities. Publishes in Chinese and English — value here is
curation and explanation, not translation (see Audience). Some posts Chinese-only;
those are the ones worth relaying.
- Live mirror of his X — https://medium.com/@mingchikuo (fetchable; X itself is blocked)

### 大山聡 (Satoshi Oyama) — Japan, industry structure
Column 「大山聡の業界スコープ」, EE Times Japan. Corporate-strategy and
industry-structure angle rather than process technology. Secondary to Yunogami.

### TrendForce / 集邦科技 — Taiwan, institutional data
Taiwan's memory / semiconductor / panel research house. Widely cited by global
press for DRAM/HBM pricing and capacity forecasts. Free news pages carry English —
no translation needed, matches the non-specialist audience.
- News (free, fetchable) — https://www.trendforce.com/news/
- DRAM news — https://www.trendforce.com/news/category/semiconductors/dram/
- Press releases — https://www.trendforce.com/presscenter/
- Paid research reports are gated; the free news + press-release pages are enough.

## Tier 2 — Trade press (breadth, not authority)

Used to *find* stories and to corroborate. A trade-press article is not itself a
citation under SKILL.md §3 unless it quotes a named person on the record — then
the named person is the citation, not the outlet.

| Source | Language | Use |
|---|---|---|
| semiconportal.com | JP | Japanese semiconductor portal; market / technology / industry analysis columns, dated. Good for equipment and memory. |
| technews.tw (科技新報) | ZH-TW | Fast Taiwanese coverage of HBM, advanced packaging, memory roadmaps. High volume — filter hard. |
| eettaiwan.com (電子工程專輯) | ZH-TW | Engineer-facing Taiwan coverage; has RSS. |
| EE Times Japan monthly ranking | JP | What the Japanese engineering audience actually read — a cheap read on which topics have momentum. |

## Tier 3 — Primary data

| Source | Cadence | Use |
|---|---|---|
| SEAJ statistics, `seaj.or.jp/statistics` | Monthly (mid-month), plus semiannual forecast mid-Jan and early Jul | Japanese equipment shipments — forward order signal |
| Taiwan monthly revenue disclosures | By the 10th | TSMC, MediaTek, ASE, Largan and second-tier suppliers. Mandatory monthly reporting; English coverage rarely goes past TSMC. |
| Japanese equipment maker results | Quarterly | Tokyo Electron, Disco, SCREEN, Lasertec — orders and backlog |

## The sweep — how monitoring stays cheap

Fetching full articles is the expensive operation, not listing them. So the sweep
is **two-stage, and the second stage is rationed.**

**Stage 1 — headline sweep.** One fetch per source index page, headlines and dates
only. Compare against `data/source-digest.json`, which stores the last-seen URL
and date per source. Anything already seen is skipped without being opened.

**Stage 2 — full read, rationed.** Only articles that pass the relevance filter
get opened in full:

1. Names an instrument the account **holds or watches**, or a direct supplier to one; and
2. Is **within the week** (SKILL.md §2 recency); and
3. Comes from Tier 1, **or** from Tier 2 while quoting a named person on the record.

**Cap: 3 full reads per drafting session.** If more qualify, take the ones closest
to the largest positions — that is the same weighting rule as SKILL.md §2. Log
what was skipped; a silent cap reads as "nothing else was there".

**Cadence.** Tier 1 and Tier 2 swept once per trading day, before slot A. Tier 3
is calendar-driven, not swept — SEAJ mid-month, Taiwan revenue by the 10th,
Japanese equipment makers quarterly. Do not poll Tier 3 daily; nothing changes.

`data/source-digest.json` is written by the same session that sweeps. It carries
no article text — URLs, titles, dates and a seen-flag only. It exists to stop the
next session re-reading what this one already rejected.

## Audience

**Write for someone who has never heard of these analysts and does not know what
HBM is.**

The eToro audience is retail, and most of it is not specialist in semiconductors.
The value this account adds is not bridging a language gap — it is that we know
who is worth reading and can explain what they said. A reader who already followed
Yunogami and Kuo would not need us.

Three consequences for every relay post:

1. **Introduce the person in one line.** Credentials and track record, every time,
   even for repeat subjects. "Former Hitachi and Elpida process engineer, now an
   independent analyst who called the 2022 downturn early" does more work than the
   name alone.
2. **Explain the mechanism in plain language before the implication.** If a post
   uses HBM, wafer allocation, CoWoS, glass core substrate or similar, one short
   clause has to say what it is. Assume nothing.
3. **Do not dilute the substance to achieve this.** The edge is that we understand
   it. The deliverable is making it understandable. Simplifying the explanation is
   right; simplifying the analysis is not.

This applies to every post type, not only the relay column.

## Rules

1. **Named analysts only.** Anonymous "supply chain sources" and "market rumour"
   do not qualify — that is exactly the trade-press chatter the sourcing standard
   rejects. If the analyst is themselves assessing a rumour, the analyst's
   assessment is the citation, not the rumour.
2. **Paraphrase, do not translate wholesale.** Reproducing a source's article in
   translation is republication. Take the claim and the number, write the sentence
   fresh, attribute by name and date, and link.
3. **Check the date on every fetch.** Some personal sites serve stale index pages.
4. **Recency rules are unchanged.** Within 24h → MARKET PULSE framing. Within the
   week → THE ASIA READ. Older → background only, never the hook.
5. **Connect to a position.** A relay with no link to something held or watched is
   a news summary, and news summaries are not what this account is for.
6. **Never store a volatile figure in this file.** Instalment numbers, forecast
   totals, price levels and market shares all move. This file holds *where to look*
   and *who is worth reading*; the numbers are pulled at drafting time. Same rule
   as SKILL.md §5.

## Gaps

- **No X monitoring.** Structural, not an oversight — see the fetchability table.
- **No Korean-language source.** Deliberate — the account underweights Korea, and
  a Korea-heavy source would pull coverage toward positions not held.
- **No Chinese-mainland source.** Language access exists but the geopolitical
  framing makes relaying mainland analysts a reputational risk not worth taking.
- **Sell-side Japanese equipment research is not public** (Wadaki, the
  Nomura/MUFG franchise). Only what reaches the press is usable.
- **Nikkei and DigiTimes are paywalled**, which costs real coverage. If either is
  ever subscribed to, both move to Tier 1 and the sweep should include them.
