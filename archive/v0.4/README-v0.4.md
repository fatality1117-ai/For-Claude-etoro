# For-Claude-etoro

Publishing spec and supporting data for the **@Edwardhwang888** eToro Popular
Investor account. This repo is the single source of truth for how that account
posts: what it publishes, when, sourced from where, and in what voice.

It is written to be read by an agent at the start of a drafting session. Read
`docs/SKILL.md` first — everything else hangs off it.

## Layout

```
docs/       the spec
  SKILL.md        post types, sourcing standard, voice rules, performance
                  claims, pre-publish checklist, publishing flow
  schedule.md     posting times, same-day sequencing, the publishing calendar,
                  the Asia Supply Chain Monitor series
  brand.md        category template images, colour system, how images attach
  sources.md      vetted Asian analyst and primary-data sources for THE ASIA READ
  make_templates.py   regenerates the ten template images

data/       daily performance snapshots
  perf-latest.json    today's figures; read by SKILL.md 5.1
  perf-<date>.json    the history

tools/      supporting scripts
  snapshot.py     builds the daily snapshot from the eToro rankings API
  SNAPSHOT.md     what the snapshot is for, and its freshness contract
  parse.py        feed-response parser (tolerates truncated API bodies)
  hours.py        engagement-by-hour study
  sig.py          significance tests for the same

pics/       the ten 1080x1080 category templates, CC0
```

## Reading order for a drafting session

1. `docs/SKILL.md` — the rules.
2. `docs/schedule.md` — what is due today and when it publishes.
3. `docs/brand.md` — which template image the post carries.
4. `docs/sources.md` — only when drafting a relay post.
5. `data/perf-latest.json` — only if the post carries a performance figure, and
   only when its `snapshotDate` is the current US trading day.

## Two things that are easy to get wrong

**Times are Asia/Taipei; trading days are the US session.** A post recapping the
Monday US session publishes at 04:00 Taipei on Tuesday and is still "the Monday
post". `docs/schedule.md` opens with this.

**No performance figure is ever written from memory.** Not from these files, not
from a previous post. Live call, or today's dated snapshot, or the claim does not
appear. `docs/SKILL.md` §5.

## Status

Trial — 30-day calibration, 2026-08-24 to 2026-09-22. The spec is being
corrected as it runs; see `CHANGELOG.md`. Anything marked *unmeasured* or
*parked* in the docs is exactly that, and should not be built on.

## Licence

Template images in `pics/` are CC0. The specification text is for the operation
of this one account and is published for transparency, not as general advice.
Nothing here is investment advice.
