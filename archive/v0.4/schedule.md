---
name: etoro-pi-schedule
description: Publishing calendar for the eToro PI account — which post types fall due on which days, plus the monthly Asia supply chain data series. Read together with SKILL.md.
version: 0.4
---

# Publishing Calendar

## Timezone convention

**All times in this file, and all times in conversation with the user, are
Asia/Taipei (UTC+8, no DST).**

The *trading day* a post belongs to is the **US session**, not the Taipei
calendar date. A post recapping the Monday US session publishes at 04:00 Taipei
on Tuesday and is still "the Monday post". Always name the trading day
explicitly when presenting a draft, so the calendar date never has to be guessed.

## Posting times

Two anchors per trading day. Slot A is a fixed Taipei time; slot B is computed
from the US close, which makes US daylight saving self-correcting.

| Slot | Definition | Content |
|---|---|---|
| **A — Pre-open** | **18:00 Taipei**, fixed | Asia-overnight material: `[THE ASIA READ]`, `[SECTOR BRIEF]`, pre-open `[MARKET PULSE]` |
| **B — Post-close** | US regular close, **16:00 ET** (computed) | Session recap: `[DAILY BRIEF]`, `[WEEKLY REVIEW]`, `[MONTHLY REVIEW]`, `[DEEP DIVE]` |

Slot A is a **fixed Taipei clock time** because it is anchored to the audience's
daily rhythm, which does not move with US daylight saving. Slot B is anchored to
the US close and therefore **must be computed** — resolve `America/New_York` at
publish time and render into `Asia/Taipei`:

| US period | Slot A | Slot B | Gap |
|---|---|---|---|
| EDT (2nd Sun Mar → 1st Sun Nov) | 18:00 same day | **04:00** next day | 10h |
| EST (1st Sun Nov → 2nd Sun Mar) | 18:00 same day | **05:00** next day | 11h |

Switch dates: DST **began** 2026-03-08, **ends 2026-11-01**, resumes 2027-03-14,
ends 2027-11-07. On a switch weekend slot B moves by one hour — verify by
computing, not by reading this table.

**Slot A hard guard — pre-open delivery.** The Asia read is worthless after the
US opens. 18:00 Taipei clears the open by **3h30 under EDT** (open 21:30 Taipei)
and **4h30 under EST** (open 22:30 Taipei), so the guarantee holds year-round
with no adjustment. It also clears both Asian closes — Taiwan 13:30, Japan 15:00
Taipei — so the session data is final before the post is written. **If slot A is
ever moved later, re-verify both margins first.**

**Why 18:00 and not the open minus one hour.** The obvious pre-open slot, 20:30
Taipei (EDT open minus 60 min), measured as the *worst* engagement band of the
day — 0.80 against an author's own median, versus 1.26 for 17:00-19:00. See the
study below. 18:00 sits in the strongest measured band while still clearing the
open by three and a half hours, so the timeliness requirement is met with room
to spare rather than met at the cost of reach.

Slot B lands at the US close with Europe still up, when session numbers are final.

Early close days (US half-sessions, 13:00 ET) move slot B to 13:00 ET. Slot A
is unaffected. US market holidays: no slot A or B; an event-driven
`[MARKET PULSE]` may still run.

### Measured: engagement by hour (study run 2026-08-24)

**Method.** 248 posts from the 10 most-copied PIs, pulled from
`GET /api/v1/feeds/users/{cid}` (which reaches ~6 months back, unlike the For You
feed, which only spans ~14 hours). Posts younger than **48 hours were discarded** —
a fresh post has had less time to accumulate engagement, and without that filter
an hour-of-day study just measures post age. Each remaining post was scored
`likes + 3×comments + 5×shares` and then **divided by its own author's median**,
which removes author size from the comparison entirely.

**Result, relative engagement by Taipei hour** (1.00 = that author's typical post):

| Taipei band | n | median | reading |
|---|---|---|---|
| 13:00-16:00 | 45 | 1.05 | average |
| **17:00-19:00** | 41 | **1.26** | **best measured band** |
| 20:00-21:00 | 45 | **0.80** | **worst measured band** (the old slot A) |
| 22:00-23:00 | 46 | 1.02 | average |
| 00:00-02:00 | 40 | 1.00 | average |
| 03:00-05:00 | 18 | 0.97 | average, thin sample |

**Significance.** Shuffling posting hours *within* each author 5,000 times
reproduces a 17-19 vs 20-21 gap this large in 0.08% of runs (p=0.0008), so the
effect is not an artefact of which authors post when. But the direction only
holds for **5 of the 7** authors with enough posts in both bands (sign test
p=0.23). Read it as directionally supported, not settled.

**Caveats that have not been controlled for.** These authors have 8,000-26,000
copiers against this account's handful, and their audience mix may differ.
Authors choose when to post, so a "good hour" may partly be a good-content hour.
The 3× / 5× weighting is inherited from SKILL.md §7 and is arbitrary. Almost no
one posts 06:00-12:00 Taipei, so those hours are untested rather than bad.
The sample spans the EU daylight-saving change, which shifts the audience's local
clock against Taipei by an hour — unmodelled, and a likely source of blur in the
band edges.

**Image effect — PARKED, do not act on.** This sample did not reproduce
SKILL.md §7's finding that an attached image is the strongest engagement signal
(median 1.00 both with, n=122, and without, n=126). Whether a *good* image beats
a plain template is a separate, qualitative question. Both are over-optimisation
at this stage: keep attaching the category template because it costs nothing and
is consistent branding, and revisit only once the basics have a full run behind
them.

**Spacing.** The 90-minute floor below is still **unmeasured** — this study says
nothing about it. It needs own-account data to test.

### Re-running the study

Same method, into the calibration window. Require **n ≥ 30 per band** before
moving a slot, and prefer own-account posts once there are enough of them, since
they carry the right audience.

## Same-day sequencing

When two or more posts fall due on one trading day, **all of them publish** —
none is dropped, merged, or held to the next day. They are separated in time.

**Rules:**

1. **Minimum 90 minutes between any two posts.** Two posts inside one impression
   window split the same audience and compete with each other.
2. **Maximum 3 posts per trading day.** A fourth is queued to the next day
   unless it is a `[MARKET PULSE]`, which never waits.
3. **Fastest-decaying material goes first, and keeps the better slot.** The post
   whose hook expires soonest is the one that cannot be moved.

**Priority when slots collide** (highest first):

| Rank | Type | Why |
|---|---|---|
| 1 | `[MARKET PULSE]` | 24h hook; publishes on its event clock, not the calendar |
| 2 | `[THE ASIA READ]` / `[SECTOR BRIEF]` | Pre-open delivery is the whole point |
| 3 | `[WEEKLY REVIEW]` / `[MONTHLY REVIEW]` | Needs final session data; window is the day, not the hour |
| 4 | `[DAILY BRIEF]` | Most substitutable |
| 5 | `[DEEP DIVE]` | Timeless — always the one that moves |

The higher-ranked post takes its natural slot. The lower-ranked post moves
**later** by at least 90 minutes; it is never brought forward into a slot where
its data is not yet final.

**Worked cases:**

- *Asia Read + Daily Brief.* Asia Read at slot A (18:00), Daily Brief at slot B
  (04:00 next day). 10h apart, no conflict. This is the normal two-post day.
- *Sector Brief + Weekly Review* (both due). Sector Brief slot A, Weekly Review
  slot B. Same shape as above.
- *Market Pulse breaks pre-open, Sector Brief also due.* Market Pulse takes slot
  A (18:00). Sector Brief moves to **19:30**, still comfortably pre-open. Recap
  stays at slot B. Three posts, ≥90min apart.
- *Market Pulse breaks intraday, Daily Brief due.* Market Pulse publishes
  immediately. If that lands within 90min of slot B, Daily Brief moves to
  **Pulse + 90min**, not earlier.
- *Deep Dive collides with anything.* Deep Dive moves — to the next free
  ≥90min gap, or to the following day. It has no recency constraint.

`[WEEKLY REVIEW]` still **replaces** the `[DAILY BRIEF]` (SKILL.md §2) — that is
one post in slot B, not two spaced apart.

## Recurring slots

Days below are **US trading days**. Publishing time is the slot in the column,
resolved to Taipei per "Posting times" above.

| Day | Type | Slot | Notes |
|---|---|---|---|
| Every trading day | `[DAILY BRIEF]` | B | Indices + watchlist + own positions |
| First trading day of week | `[WEEKLY REVIEW]` | B | Replaces that day's DAILY BRIEF |
| Thursday | `[SECTOR BRIEF]` AI Infra / Semis | A | Largest position cluster |
| Odd-numbered Wednesday | `[SECTOR BRIEF]` Energy | A | |
| Even-numbered Wednesday | `[SECTOR BRIEF]` Critical Minerals | A | |
| Last Wednesday, odd months | `[SECTOR BRIEF]` Biotech | A | Small position |
| Last Wednesday, even months | `[SECTOR BRIEF]` Cybersecurity | A | Small position |
| Last trading day of month | `[MONTHLY REVIEW]` | B | User's existing format + PI benchmark |
| Event-driven | `[MARKET PULSE]` | event clock | Only if a qualifying 24h event exists |
| 1-2 per week | `[THE ASIA READ]` | A | Relay column — see below |
| When Substack publishes | `[DEEP DIVE]` | B, or first free gap | English rewrite |

Roughly 20-25 posts per month. Typical day is **two posts** — one at A, one at B.

**Double-booked Wednesdays.** The last Wednesday of an even month is both an
"even-numbered Wednesday" (Critical Minerals) and a "last Wednesday, even month"
(Cybersecurity); the same happens in odd months with Energy and Biotech. This is
not a conflict to resolve — **both publish**, staggered. The first falls in slot
A, the second 90 minutes later at 19:30, which is still comfortably pre-open.

**Which goes first:** both have the same recency, so the tiebreak is position
size — the larger holding takes slot A, the better slot (SKILL.md §2 weighting).
Cybersecurity and Biotech are noted as small positions, so on a doubled Wednesday
they take the 19:30 slot and Critical Minerals / Energy take 18:00. Verify against
the live portfolio rather than assuming; if the sizes have flipped, so does the
order.

## Asia Supply Chain Monitor

A recurring three-part series inside the AI Infra SECTOR BRIEF slot. The
premise: the AI buildout can be read earlier and more often from Asian
disclosures than from US quarterly earnings.

**Chain of evidence:**
Japan materials & equipment orders (leads 6-12 months)
→ Taiwan monthly revenue (current output)
→ US earnings (quarterly, lagging)

Do **not** publish the methodology as a standalone post. Run it, do not
explain it.

| Timing | Source | Content |
|---|---|---|
| Monthly, by the 10th | Taiwan monthly revenue disclosures — TSMC, MediaTek, ASE, Largan and second-tier suppliers | Actual output. Taiwan mandates monthly revenue reporting; almost nobody reads past TSMC in English. |
| Monthly, mid-month | SEAJ monthly equipment sales statistics (3-month moving average), seaj.or.jp/statistics | Forward order signal |
| Mid-January and early July | SEAJ semiannual demand forecast PDF, seaj.or.jp | Revisions up or down are the story |
| Quarterly | Japanese equipment maker results — Tokyo Electron, Disco, SCREEN, Lasertec | Orders and backlog |

**Latest SEAJ reading (2026-07-02 forecast):** FY2026 Japanese equipment
sales forecast at ¥6.5502tn, +26% YoY — revised up ¥1.0498tn (+19%) from the
January forecast. SEAJ chairman Toshiki Kawai (also Tokyo Electron president)
attributed the revision to accelerating AI deployment.

Do not use this figure as support after the next release supersedes it.

## Calibration period

**2026-08-24 to 2026-09-22.** Run in chat, correct as we go, update these
docs after every correction. Every post type should run at least once.

Known checkpoints in the window:
- 2026-08-26 — NVIDIA Q2 earnings
- 2026-09-02 — Broadcom fiscal Q3
- ~2026-09-10 — Taiwan August monthly revenue
- ~2026-09-15/20 — SEAJ August statistics

**2026-08-26 is a four-post day** — the first real test of the sequencing rules:

| Taipei time | Post |
|---|---|
| Wed 18:00 | `[SECTOR BRIEF]` Critical Minerals (slot A) |
| Wed 19:30 | `[SECTOR BRIEF]` Cybersecurity (doubled Wednesday, +90min) |
| Thu 04:00 | `[DAILY BRIEF]` Wednesday session recap (slot B) |
| Thu ~05:30 | `[MARKET PULSE]` NVIDIA Q2 (+90min after the recap) |

The Pulse is exempt from the three-post cap but not from the 90-minute floor.
NVIDIA reports after the Wednesday close, so the numbers land shortly after slot
B — publish the recap on time at 04:00, then the Pulse once the print and the
call are both out. Do not key this off a hardcoded release time; key it off the
numbers actually being available, and hold the 90-minute gap from the recap.

Thursday 2026-08-27 then runs its normal AI Infra `[SECTOR BRIEF]` at 18:00,
which is where the considered NVIDIA read belongs — the Pulse is the reaction,
the Thursday brief is the analysis.

Calibration deliverables, to be resolved before the window closes:
- **Posting-time study.** Re-run with n ≥ 30 per band on own-account posts.
- **Spacing floor.** The 90-minute minimum is a guess. Check whether own posts
  published closer together actually underperform.

## Fixed benchmark group

Used in WEEKLY REVIEW and MONTHLY REVIEW. Same names, same window, every
time — published whether the comparison flatters or not.

`@thomaspj` `@JeppeKirkBonde` `@Smudliczek` `@CPHequities` `@jaynemesis`

Pull with `get-trader-profile-summary`. `thisWeekGain` for the week,
`gain` with `period=CurrMonth` for month to date.

## The Asia Read (relay column)

Added 2026-08-24 on the strength of the format findings in SKILL.md §7:
relaying a named analyst with a chart and an actionable read produced the
highest engagement-per-copier in the sample.

**Premise:** the user reads Chinese and Japanese sources directly. Named
supply-chain analysts and Asian financial press are hours to a day ahead of
English coverage, and much of it is never translated at all.

**Sources:** see sources.md — vetted list with fetchability status. Primary
Japan source is Takashi Yunogami (EE Times Japan, Japanese only); primary Taiwan
source is Ming-Chi Kuo (via Medium, since X blocks automated access).

**Structure:**
1. Who said it, and when
2. What they said — paraphrased, not translated wholesale
3. What it means for a named position
4. One point of agreement or disagreement

**Rules:**
- Named analysts only. Anonymous "supply chain sources" do not qualify —
  that is the trade-press chatter the sourcing standard rejects.
- The relay is the value; do not bury it under original commentary.
- Same recency rules as everything else: within 24h → MARKET PULSE framing;
  within the week → this column.
- Paraphrase. Do not reproduce a source's wording at length in translation.
