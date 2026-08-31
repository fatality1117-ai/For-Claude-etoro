---
name: etoro-pi-content
description: Publishing spec for the @Edwardhwang888 eToro Popular Investor account. Read this before drafting, scheduling, or publishing any eToro post or comment. Covers post types, sourcing standards, formatting rules, and the pre-publish checklist.
version: 0.4
status: trial (30-day calibration, 2026-08-24 to 2026-09-22)
---

# eToro PI Content Spec

## 1. Account context

| Field | Value |
|---|---|
| Handle | @Edwardhwang888 |
| eToro user ID | 13809545 |
| PI tier | Dynamic — pull `profile.subType` (§5). Do not state a tier from this file. |
| Copiers | Dynamic — pull `copiers.copiers` (§5). Never quoted from memory. |
| Sign-off | `@Edwardhwang888 \| Copy for AI Alpha` |
| Brand mark on images | AI ALPHA (no personal name) |
| Timezone for all scheduling and discussion | **Asia/Taipei** (see schedule.md) |

The account is registered in the user's partner's name. The English-facing
brand keeps that persona simple — no backstory, no explanation. Chinese-language
writing elsewhere frames it differently; do not carry that framing into English.

**Two goals, tracked separately:**
1. Convert existing followers into copiers
2. Acquire new followers

## 2. Post types

Every post carries its type in the title, in square brackets.

| Type | Cadence | Length | Material recency |
|---|---|---|---|
| `[DAILY BRIEF]` | Every trading day | 400-600 chars | Same day |
| `[WEEKLY REVIEW]` | First trading day of week | 1,200-1,500 chars | Prior week |
| `[MONTHLY REVIEW]` | Last trading day of month | 3,000-4,000 chars | Prior month |
| `[MARKET PULSE]` | Event-driven only | 800-1,500 chars | **Within 24 hours** |
| `[SECTOR BRIEF]` | Rotating, see schedule.md | 1,500-2,500 chars | **Most important development that week** |
| `[DEEP DIVE]` | When Substack publishes | 2,000-3,000 chars | Timeless |

**No platform character limit.** The API docs claim 1,000 chars for the
`message` field; this is wrong. Verified: a 1,873-char post published
successfully, and the user's own 3,673-char monthly reviews publish fine.
Length targets above are for reader experience, not technical constraint.

### Type selection rules

- If the hook is **within 24 hours** → MARKET PULSE
- If the hook is **within the week but not 24h** → SECTOR BRIEF
- If material is **older than a week** → it is background, not a hook. Do not
  build a post around it. Background may support a post whose hook is fresh.
- WEEKLY REVIEW **replaces** that day's DAILY BRIEF (superset, not both)
- MARKET PULSE is **additive** — publish alongside the day's scheduled post

### Weighting

Post length and section weighting must match actual position size.
Verticals held heavily get more space; verticals barely held get a sentence.
Verticals with zero exposure (e.g. stablecoins, standalone neocloud) are
opinions, not positions — one line maximum, placed last.

## 3. Sourcing standard

### Accepted
Bloomberg, Bloomberg Intelligence, Reuters, IDC, Counterpoint Research,
Morgan Stanley, S&P Global, TrendForce, SEAJ, company filings (13F, 10-Q),
named executives on the record, official government/exchange disclosures.

### Rejected
Consumer and enthusiast outlets (Tom's Hardware, PC press), trade-press
"reportedly" chatter, aggregator headlines that were not opened and verified,
forum posts, unattributed rumour.

### Rules
- **Verify before citing.** Do not cite a headline seen in a search result
  listing without reading the source.
- **Data must be current.** Figures from a prior year do not qualify as support.
  A 2025 market-share statistic is not evidence about 2026 conditions.
- **Prefer citing over deriving.** State what an institution said that day.
  Do not construct causal explanations the sources do not make.
- **Do not link unrelated events under one narrative.** Two things happening
  in the same week are not the same story. If drivers differ, say so and
  present them separately.

## 4. Voice rules

### Banned constructions
- **"This isn't X — it's Y"** and all variants. Negating the obvious to
  restate it is filler. Say the thing directly.
- **Meta-commentary about the post's own methodology.** Readers do not need
  to be told why a window was chosen. Show the numbers; they can judge.
- **Unsourced causal claims.** "Asia held up better because…" is an inference.
  Either cite it or drop it.
- **Rank claims without a stated basis.** See §5.

### Audience assumption
Write for a retail reader who is **not** a semiconductor specialist. Most of the eToro
audience has never heard of the analysts we relay and does not know what HBM, CoWoS or a
glass core substrate is. Any such term gets one short clause explaining it, in the same
sentence, the first time it appears in a post.

This does not mean writing less substantial posts. Simplify the explanation, never the
analysis. See sources.md §Audience.

### Required
- Lead with the claim, then the evidence.
- Report losses as plainly as gains. Stops that triggered are described as
  mechanical, not as decisions.
- One disagreement or open question per longer post — full agreement with
  every cited source reads as having no view.
- Close with `Not investment advice.` on any post containing performance
  figures or positioning.

## 5. Performance claims

### No performance figure is ever written from memory

Returns, rankings, copier counts, AUM and position counts all move. **No number
written into this file, into schedule.md, or into a previous post is ever a
source for a new post.** Every figure comes from one of exactly two places: a
live API call, or today's dated snapshot (§5.1). If neither is available, the
post ships without the claim — it does not ship with a remembered number.

**Where each figure comes from:**

| Figure | Source | Field |
|---|---|---|
| Own return, any window | snapshot, else `/api/v2/portfolios/{user}/rankings` | `gain` at the matching `period` |
| Own copiers, tier, risk | snapshot, else same route | `copiers`, `subType`, `riskScore` |
| Own longer-horizon return | snapshot, else same route | `fiveYearGain`, `tenYearGain`, `annualizedReturn` |
| Most-copied ten, beat count | snapshot, else `/api/v2/portfolios/rankings` | see below |
| **Own week / day** | **LIVE ONLY** — `get-trader-profile-summary` | `thisWeekGain`, `dailyGain` |
| **Positions, P&L, exposure** | **LIVE ONLY** — `get-my-portfolio-summary` | `totals`, `holdings[].positionCount` |
| Benchmark group | `get-trader-profile-summary`, all five usernames in ONE call | same fields, same `period` |

"Snapshot, else live" means: use the snapshot **only** when its `snapshotDate`
is the current US trading day, and print that date in the post. Otherwise pull.

Gains come back as **fractions** — `0.0485` is +4.85%. Convert once, state once.

### Use `AbsTwoYears`, never `LastTwoYears`, for a "two-year" claim

`LastTwoYears` means **from 1 January two calendar years ago** — on 2026-08-24
that is a 2.6-year window, not two years. `AbsTwoYears` is exactly two years
back from the ranking max-date, with no rounding. Only `AbsTwoYears` may be
described as "two years".

(Both currently return the same figure for this account because its ranking
history starts at the two-year boundary. That coincidence will not survive —
use `AbsTwoYears` regardless.)

`/api/v2/portfolios/rankings` accepts a wider period list than
`get-trader-profile-summary`: `CurrMonth`, `OneMonthAgo`, `TwoMonthsAgo`,
`CurrQuarter`, `ThreeMonthsAgo`, `SixMonthsAgo`, `CurrYear`, `OneYearAgo`,
`LastYear`, `LastTwoYears`, `AbsOneYear`, `AbsTwoYears`. Never chain or compound
periods to synthesise a window the API does not return.

### The most-copied comparison — the one defensible performance claim

Two calls produce the whole thing, roster and comparison together:

```
GET /api/v2/portfolios/rankings
    ?period=AbsTwoYears&sort=-copiers&pageSize=10&popularInvestor=true
GET /api/v2/portfolios/Edwardhwang888/rankings?period=AbsTwoYears
```

Both sides come from the same endpoint at the same period, so the comparison is
like-for-like. Count how many of the ten rows have a lower `gain` than ours and
state that count — **"beats N of the 10 most-copied PIs"**. Never "the top PIs".

**Required alongside the claim, in the same post:**

1. The **window**, named ("the two years to <snapshot date>").
2. The **snapshot date** the figures were taken. A line at the foot of the post
   is enough: `Figures: eToro rankings, snapshot <YYYY-MM-DD>.`
3. The **scale gap** — those ten run eight-to-ten-figure books against this
   account's five-figure one, and scale is part of why they lag. Pull `aumValue`
   in the same call and say it first; cheaper than being corrected.

**Not defensible:** any ranking claim by raw return against the full PI field.
Filtered to PIs with ≥10 copiers the account sits low in that distribution, and
that is not a leaderboard position. Do not claim one. Never state a percentile,
"top N", or national ranking without the exact filter that produces it.

### Staleness rule

Cached figures (see §5.1) are good for the trading day stamped on the snapshot,
and the post must carry that date. Live figures are good for the drafting
session only — if a draft is held across a US session boundary, re-pull. Once
published, a figure is frozen in that post and is never a source for the next one.

## 5.1 The daily snapshot

Rankings data refreshes **once a day**, so re-pulling it per post buys nothing.
The snapshot exists to make the numbers auditable, to give a history the API
does not expose, and to keep the agent from re-reading large JSON payloads.

`data/perf-latest.json` in this repo holds the day's figures; `data/perf-<date>.json`
keeps the history. Read the snapshot instead of calling the API — **when, and
only when, its `snapshotDate` is the current trading day.** If it is older, or
missing, pull live and regenerate it.

**Cacheable — daily granularity is all the API has:**
`gain` at every period, `annualizedReturn`, `fiveYearGain`, `tenYearGain`,
`winRatio`, `copiers`, `riskScore`, `subType`, `aumValue`, the most-copied ten
and the derived beat-count.

**Never cacheable — these move intraday and must be pulled live every time:**
open positions, `unrealizedPnl`, exposure, available cash (`get-my-portfolio-summary`),
and `thisWeekGain` / `dailyGain`. The snapshot deliberately omits them; the
`doNotCache` array in the file lists them so the omission is not mistaken for
an oversight.

A post may therefore mix a dated snapshot figure with a live position figure.
That is fine, and the date line at the foot covers the snapshot half.

## 6. Cashtags

Every tradable instrument mentioned gets a `$` prefix, **regardless of market**:
`$NVDA` `$TSM` `$4063.T` `$5214.T` `$7911.T` `$LPK.DE` `$LYC.ASX` `$SWDA.L`

The cashtag is what surfaces the post on that instrument's page — a primary
channel for reaching people who do not already follow the account. A missed
`$` is a missed distribution channel, not a typo.

**Verify after publishing:** the API response returns a `tags` array of
successfully resolved cashtags. Compare it against the instruments named in
the draft. Anything missing did not resolve — either the symbol is wrong or
eToro does not list it.

## 7. Format findings (empirical)

Sample: 66 posts pulled 2026-08-24 from the For You feed and the NVDA/TSM/AVGO
instrument feeds. Filtered to authors with ≤200 copiers (n=56) to remove
accounts whose reach comes from existing size. Engagement scored as
likes + 3×comments + 5×shares.

**Caveats: single-day snapshot, small sample, heavy crypto skew in the
high-engagement tail, and the weighting is arbitrary. Directional only.**

| Variable | Finding |
|---|---|
| Image | Median 6 with, 3 without. Strongest and most consistent signal. |
| Length | No relationship. 1,200+ chars median 4; 600-1,200 median 5. Long posts are not rewarded for being long. |
| Question mark | No effect (median 3 with, 4 without). Asking a question does not by itself drive discussion. |
| Cashtag count | No clear effect on engagement — but tags drive *distribution*, which this metric does not capture. |
| Floor | Only 1 of 56 posts scored zero. Getting some engagement is easy; the ceiling needs a specific format. |

### Formats that over-performed relative to author size

1. **Relaying a named analyst plus a chart plus an actionable read.** The
   two clearest outliers came from accounts with 5 and 0 copiers, scoring
   77 and 26. Both relayed a recognised figure (Rekt Capital, Ray Dalio)
   rather than presenting original analysis. Highest effort-to-return ratio
   in the sample.
2. **Narrative lesson with a concrete loss.** Top post overall (83): a
   specific leverage blow-up, all-caps hook, story structure. What made it
   work was the specific incident, not the moral drawn from it.

### Implications

- **Attach the category template image to every post.** Zero marginal cost,
  clearest measured effect.
- **A relay column is justified** — Ming-Chi Kuo, Nikkei, Taiwan's Economic
  Daily. Reading the original before the English-language market does is the
  same information-arbitrage position the Asia series occupies, and the
  format has measured support.
- **Case-study posts are supported**, but only with concrete specifics —
  filing amounts, actual terms, price reaction. An abstract discussion of
  corporate values with a question attached has no measured support.
- Do not add question marks expecting discussion. Discussion follows from
  a concrete claim someone can disagree with.

## 8. Pre-publish checklist

1. Type label correct for material recency (§2)
2. Every source on the accepted list, and actually read (§3)
3. Every figure current — no prior-year data as support (§3)
4. No banned constructions (§4)
5. Section weighting matches position size (§2)
6. Every instrument carries `$` (§6)
7. Performance claims match §5 exactly, and **every figure was pulled this
   session** — no number carried from these docs or a previous post
8. Correct template image attached (see brand.md)
9. `Not investment advice.` present if required
10. Sign-off line present
11. Publish slot assigned, and ≥90min from any other post that day (schedule.md)

## 9. Publishing flow

Reads are autonomous — pull portfolio, rankings, quotes, history, and feed
data without asking. Only the **publish** step requires approval.

1. Draft fully, with **performance data pulled live** (§5) and image attached
2. Present the complete text, character count, and the **target publish time in
   Taipei** with the US trading day it belongs to (schedule.md)
3. Wait for explicit approval
4. `POST /api/v1/posts` (or `PUT /api/v1/posts/{id}` to edit)
5. Report the status code and the resolved cashtag list

If two or more posts are due the same trading day, present them **together**
with their assigned slots and the gap between them, so the spacing can be
approved as a set. All of them publish — see schedule.md, "Same-day sequencing".

## 10. Trigger words

| User says | Action |
|---|---|
| `update` | Work out from schedule.md what is due today, draft everything, present for approval |
| `daily` / `weekly` / `monthly` | That specific post type |
| a vertical name | That SECTOR BRIEF |

## 11. Out of scope

- **No agent-executed trading on this account.** Any agent trading tests move
  to a dedicated separate account.
- **No LinkedIn.** Wrong audience fit, ruled out.
- **No image uploads via API.** Multipart requires CRLF, which the tool
  transport cannot send. Images are attached by external URL only (brand.md).
