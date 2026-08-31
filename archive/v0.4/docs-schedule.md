---
name: etoro-pi-schedule
description: Publishing calendar for the eToro PI account — which post types fall due on which days, plus the monthly Asia supply chain data series. Read together with SKILL.md.
version: 0.1
---

# Publishing Calendar

## Recurring slots

| Slot | Type | Notes |
|---|---|---|
| Every trading day | `[DAILY BRIEF]` | Indices + watchlist + own positions |
| First trading day of week | `[WEEKLY REVIEW]` | Replaces that day's DAILY BRIEF |
| Thursday | `[SECTOR BRIEF]` AI Infra / Semis | Largest position cluster |
| Odd-numbered Wednesday | `[SECTOR BRIEF]` Energy | |
| Even-numbered Wednesday | `[SECTOR BRIEF]` Critical Minerals | |
| Last Wednesday, odd months | `[SECTOR BRIEF]` Biotech | Small position |
| Last Wednesday, even months | `[SECTOR BRIEF]` Cybersecurity | Small position |
| Last trading day of month | `[MONTHLY REVIEW]` | User's existing format + PI benchmark |
| Event-driven | `[MARKET PULSE]` | Only if a qualifying 24h event exists |
| 1-2 per week | `[THE ASIA READ]` | Relay column — see below |
| When Substack publishes | `[DEEP DIVE]` | English rewrite |

Roughly 20-25 posts per month.

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
