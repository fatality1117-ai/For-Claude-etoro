# Daily performance snapshot

Produces `data/perf-latest.json` (+ a dated copy in `data/`). Read by SKILL.md §5.1.

## What it is for

Not for saving eToro API quota — the whole pull is 4 calls against a 60/60s
limit, which is nothing. It exists for three other reasons:

1. **Auditability.** A dated file backs every published figure. When a reader
   challenges a number, the snapshot is the answer.
2. **History.** The API returns today only. Copier growth, gain trajectory and
   the beat-count over time exist only if we keep the dailies.
3. **Agent cost.** The raw rankings payload is ~10KB of JSON per call. The
   snapshot is ~2KB of the fields that actually get used.

Rankings refresh **once a day**, so a same-day snapshot is not an approximation
of the live value — it *is* the live value.

## The four calls

```
GET /api/v2/portfolios/rankings?period=AbsTwoYears&sort=-copiers&pageSize=10&popularInvestor=true
GET /api/v2/portfolios/rankings?period=CurrMonth&sort=-copiers&pageSize=10&popularInvestor=true
GET /api/v2/portfolios/Edwardhwang888/rankings?period=AbsTwoYears
GET /api/v2/portfolios/Edwardhwang888/rankings?period=CurrYear
```

Add `?period=CurrMonth` on the self route if the month figure is wanted from the
same source as the comparison rather than from `get-trader-profile-summary`.

## Fields kept

From the self row: `subType`, `copiers`, `riskScore`, `aumTierDesc`, `aumValue`,
`gain` per period, `annualizedReturn`, `fiveYearGain`, `tenYearGain`, `winRatio`.

From each of the ten rows: `username`, `copiers`, `gain`, `aumValue`.

Derived: `beatCount` = how many of the ten have `gain` below ours, `losesTo`,
and their AUM range.

## Fields deliberately excluded

`positions`, `unrealizedPnl`, `exposure`, `availableCash`, `thisWeekGain`,
`dailyGain` — these move intraday. They are listed in the file's `doNotCache`
array so their absence reads as a decision, not a gap. Pull them live.

## When to run

Once a day, **after** the rankings refresh. Every row's `lastActivity` carries
the max-date; the refresh lands after the US close, so anything from 06:00
Taipei onward is safe. Running it at the end of the slot-B post is convenient —
the session is already open.

## Freshness contract

Before using the snapshot, compare `snapshotDate` against the current **US
trading day**. Equal → use it. Older, or the file is missing → pull live and
regenerate. Never publish a figure from a snapshot without printing its date in
the post.

## Automating it

Two options.

**A — regenerate in-session.** Whatever session drafts the slot-B post makes the
four calls and rewrites the files. Zero extra infrastructure; the cost is that
it only happens on days a session runs.

**B — GitHub Action.** Runs whether or not anyone is at the keyboard, which is
what an autopilot wants. Needs the eToro credentials as repo secrets
(`ETORO_USER_KEY`, `ETORO_API_KEY`) and a small script that makes the four calls
with those headers plus a fresh `x-request-id` GUID per request, then commits the
result. Sketch:

```yaml
name: perf-snapshot
on:
  schedule:
    - cron: '0 22 * * 1-5'   # 22:00 UTC = 06:00 Taipei, weekdays
  workflow_dispatch:
permissions:
  contents: write
jobs:
  snapshot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python tools/snapshot.py
        env:
          ETORO_USER_KEY: ${{ secrets.ETORO_USER_KEY }}
          ETORO_API_KEY:  ${{ secrets.ETORO_API_KEY }}
      - run: |
          git config user.name  github-actions
          git config user.email github-actions@github.com
          git add data/
          git diff --staged --quiet || git commit -m "perf snapshot $(date -u +%F)"
          git push
```

`tools/snapshot.py` is not written yet — B is a decision to make, not a thing
that is running. Under option A the same four calls are made by hand and the
JSON assembled in-session, which is how `data/perf-2026-08-24.json` was produced.

Note the cron runs on GitHub's schedule in UTC and does not follow US daylight
saving. 22:00 UTC is 06:00 Taipei year-round, which is after the refresh in both
EDT and EST, so it does not need adjusting.
