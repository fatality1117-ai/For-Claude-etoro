# Changelog

Notable changes to the spec. Newest first. `docs/SKILL.md` and
`docs/schedule.md` carry their own `version:` in frontmatter; this file records
why each bump happened.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [0.4] — 2026-08-24

### Added
- `docs/sources.md` Tier 1 expanded with 南川明 (Akira Minamikawa, Omdia — macro
  and geopolitics) and 和田木哲哉 (Tetsuya Wadaki, MUFG Morgan Stanley — the
  top-ranked Japanese equipment analyst), plus TrendForce promoted to Tier 1 as
  institutional data.
- New Tier 2 trade-press layer, each source fetch-tested 2026-08-24:
  semiconportal.com (JP), technews.tw (ZH-TW), eettaiwan.com (ZH-TW).
- **The sweep** — a two-stage monitoring procedure. Stage 1 lists headlines only
  and diffs against `data/source-digest.json`; stage 2 opens articles in full and
  is capped at three per drafting session, allocated toward the largest positions.
  Fetching full text is the expensive operation, so it is the rationed one.
- `data/source-digest.json` — last-seen URL/title/date per source. Carries no
  article text. Exists so the next session does not re-read what this one rejected.

### Changed
- `docs/sources.md` states explicitly that eToro's own news feed and any
  aggregator every eToro user already sees are **not sources**. The account's
  premise is material the reader could not have found without us.
- Tier 3 (SEAJ, Taiwan monthly revenue, Japanese equipment results) is
  calendar-driven and explicitly **not** polled daily — nothing changes between
  releases, so polling it is pure waste.

### Fixed
- Removed the hardcoded instalment number from the Yunogami column entry. A fetch
  on 2026-08-24 disagreed with the number stored in 0.1, which is exactly the
  failure mode §5 was written to prevent. Volatile figures do not belong in the
  spec — rule 6 in sources.md now says so generally.

### Known limitation
- **X/Twitter cannot be monitored.** `robots.txt` blocks automated access with no
  workaround, so any commentator whose primary output is X is reachable only via
  a mirror (Ming-Chi Kuo on Medium) or via trade press quoting them. Do not
  promise social-feed monitoring the tooling cannot deliver.
- Nikkei and DigiTimes remain paywalled — headlines only, not citable.

---

## [0.3] — 2026-08-24

### Added
- `data/perf-latest.json` and `data/perf-2026-08-24.json` — the daily
  performance snapshot, with a `doNotCache` array naming the fields that are
  deliberately absent because they move intraday.
- `tools/snapshot.py` — builds the snapshot from four eToro rankings calls.
  Stdlib only; credentials from `ETORO_USER_KEY` / `ETORO_API_KEY`.
- `tools/SNAPSHOT.md` — what the snapshot is for and its freshness contract.
  States plainly that it does not save API quota (four calls against a 60/60s
  limit); it buys auditability, history, and lower agent context cost.
- `tools/parse.py`, `hours.py`, `sig.py` — the engagement study, kept so the
  result can be reproduced and re-run.
- `schedule.md`: measured engagement-by-hour table, method, significance and
  uncontrolled caveats.
- `schedule.md`: the 2026-08-26 four-post worked schedule.
- `README.md`, `CHANGELOG.md`.

### Changed
- **Slot A moved from "US open minus 60 min" (20:30 Taipei) to a fixed 18:00
  Taipei.** 20:30 measured as the *worst* engagement band of the day (0.80 vs
  1.26 for 17:00-19:00, n=248, within-author shuffle p=0.0008). 18:00 clears the
  US open by 3h30 under EDT and 4h30 under EST — verified by computation across
  two years — and clears the Taiwan (13:30) and Japan (15:00) closes, so the
  pre-open requirement is met with more margin than before, not less.
- Slot A is now a fixed Taipei time; only slot B is computed from the US close.
- `SKILL.md` §5 rewritten: figures come from a live call or today's snapshot,
  never from a document or a previous post. Source table now names the exact
  route and field per figure, and marks `thisWeekGain` / `dailyGain` / positions
  as **live only**.
- Doubled Wednesdays (Critical Minerals + Cybersecurity, or Energy + Biotech)
  now explicitly publish **both**, staggered 18:00 and 19:30, with the larger
  position taking slot A. Previously flagged as an unresolved conflict; it was
  never a conflict — the same-day sequencing rule already covered it.

### Fixed
- **`LastTwoYears` is not a two-year window.** It runs from 1 January two
  calendar years ago — 2.6 years as of this release. Any "two-year" claim must
  use `AbsTwoYears`. The 0.2 spec named the wrong period.
- The +110.36% two-year return and the "beats 8 of the 10 most-copied PIs" claim
  were re-derived live rather than trusted: both verify exactly at
  `AbsTwoYears`, losing only to Smudliczek (155.84%) and Michalhla (152.18%).
  The claim is retained, and must now carry the snapshot date and the AUM scale
  gap ($17.1M-$285.9M against this account's five figures).

### Deprecated
- The image-engagement finding in `SKILL.md` §7 is **parked**. A larger
  longitudinal sample (n=248 vs the original n=56 single-day) did not reproduce
  it — median relative engagement 1.00 both with and without an image. Keep
  attaching category templates for consistency and zero cost; do not build on
  the §7 claim, and do not pursue image quality optimisation yet.

### Still unmeasured
- The 90-minute minimum gap between same-day posts.
- Taipei 06:00-12:00, where almost nobody posts — untested, not known to be bad.
- Whether the European daylight-saving shift moves the good band against Taipei
  time by an hour.

---

## [0.2] — 2026-08-24

### Added
- Timezone convention: all times Asia/Taipei; trading day is the US session.
- Two posting slots, A (pre-open) and B (post-close), with DST handled by
  computing from `America/New_York` rather than hardcoding.
- Same-day sequencing: all due posts publish, 90-minute minimum gap, three-post
  cap, priority order, and five worked collision cases.

### Changed
- `SKILL.md` §5: hardcoded performance figures replaced with live-pull
  instructions.
- `SKILL.md` §1: PI tier and copier count marked dynamic.

---

## [0.1] — 2026-08-24

Initial spec: account context, post types, sourcing standard, voice rules,
performance claims, cashtags, format findings, pre-publish checklist,
publishing flow, brand and visual identity, Asia source list.
