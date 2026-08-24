---
name: etoro-pi-content
description: Publishing spec for the @Edwardhwang888 eToro Popular Investor account. Read this before drafting, scheduling, or publishing any eToro post or comment. Covers post types, sourcing standards, formatting rules, and the pre-publish checklist.
version: 0.1
status: trial (30-day calibration, 2026-08-24 to 2026-09-22)
---

# eToro PI Content Spec

## 1. Account context

| Field | Value |
|---|---|
| Handle | @Edwardhwang888 |
| eToro user ID | 13809545 |
| PI tier | Rising Star (piLevel 2) |
| Sign-off | `@Edwardhwang888 \| Copy for AI Alpha` |
| Brand mark on images | AI ALPHA (no personal name) |

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

**Defensible:** comparison against the *most-copied* PIs over a stated window.
As of 2026-08-23, the account's two-year return of +110.36% beats 8 of the 10
most-copied PIs on eToro. State "8 of 10", never "the top PIs".

**Not defensible:** any ranking claim by raw return. Filtered to PIs with
≥10 copiers, the account sits in the bottom ~15% YTD and bottom ~7% over two
years. Do not claim a leaderboard position.

**Always disclose** when using the comparison: the most-copied PIs run
$17M-$285M books, and scale is part of why they lag. Saying it first is
cheaper than being corrected.

**Never** state a percentile, "top N", or national ranking without the exact
filter that produces it.

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
7. Performance claims match §5 exactly
8. Correct template image attached (see brand.md)
9. `Not investment advice.` present if required
10. Sign-off line present

## 9. Data efficiency (token discipline)

eToro's raw endpoints return very large payloads — a single feed query can
exceed 400,000 characters, almost all of it avatar URLs, timestamps and IDs
that are never used. Follow this order to keep every run cheap:

1. **Prefer the summary tools over raw `execute-read`:**
   - `get-my-portfolio-summary` — holdings, P&L, cash in one call
   - `get-my-positions-and-orders` — positions and open orders
   - `get-trader-profile-summary` — PI benchmark returns (batch multiple usernames in one call)
   - `get-instruments-overview` — quotes (batch multiple symbols in one call)
   Only fall back to a raw endpoint when the field you need is not in a summary tool.
2. **Batch, never loop.** One call with ten symbols, not ten calls.
3. **When a raw feed is unavoidable** (e.g. pulling hot posts for commenting),
   always pass `take=20` and `reactionsPageSize=1`. Never the default page size.
4. **Discard raw payloads after extracting.** Pull the numbers, drop the JSON —
   do not read a large raw response back into context.
5. **In Cowork:** the data-pull tasks run in their own cloud session and write
   only the distilled result to a file. The publishing task reads that file
   (hundreds of characters), not the raw pull.

## 10. Publishing flow

Reads are autonomous — pull portfolio, rankings, quotes, history, and feed
data without asking. Only the **publish** step requires approval.

1. Draft fully, with data pulled and image attached
2. Present the complete text and character count
3. Wait for explicit approval
4. `POST /api/v1/posts` (or `PUT /api/v1/posts/{id}` to edit)
5. Report the status code and the resolved cashtag list

## 11. Trigger words

| User says | Action |
|---|---|
| `update` | Work out from schedule.md what is due today, draft everything, present for approval |
| `daily` / `weekly` / `monthly` | That specific post type |
| a vertical name | That SECTOR BRIEF |

## 12. Out of scope

- **No agent-executed trading on this account.** Any agent trading tests move
  to a dedicated separate account.
- **No LinkedIn.** Wrong audience fit, ruled out.
- **No image uploads via API.** Multipart requires CRLF, which the tool
  transport cannot send. Images are attached by external URL only (brand.md).
