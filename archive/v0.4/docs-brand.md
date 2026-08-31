---
name: etoro-pi-brand
description: Visual identity for the eToro PI account — category template images, their URLs, the colour system, and how images are attached to posts. Read before publishing any post that needs a cover image.
version: 0.1
---

# Brand & Visual Spec

## How images attach

eToro's `attachments` field takes a JSON object with a URL. **External domains
are accepted** — verified with `raw.githubusercontent.com`. No file upload is
involved.

```json
"attachments": [{
  "url": "<raw URL>",
  "title": "<category name>",
  "host": "raw.githubusercontent.com",
  "description": "<one line>",
  "mediaType": "Image",
  "media": { "image": { "width": 1080, "height": 1080, "url": "<raw URL>" } }
}]
```

**Direct file upload does not work.** `POST /api/v1/attachments` requires
multipart/form-data with CRLF line endings, which the tool transport cannot
produce. Confirmed by two attempts returning
`400 — Line length limit 100 exceeded`. Use external URLs only.

## Template images

Base: `https://raw.githubusercontent.com/fatality1117-ai/For-Claude-etoro/main/pics/`

| Post type | File | Accent |
|---|---|---|
| `[DAILY BRIEF]` | `tpl_daily.png` | Gold `#D4A24E` |
| `[WEEKLY REVIEW]` | `tpl_weekly.png` | Gold `#D4A24E` |
| `[MONTHLY REVIEW]` | `tpl_monthly.png` | Gold `#D4A24E` |
| `[MARKET PULSE]` | `tpl_pulse.png` | Terracotta `#D07048` |
| `[SECTOR BRIEF]` AI Infra | `tpl_sector_ai.png` | Blue `#568CC4` |
| `[SECTOR BRIEF]` Energy | `tpl_sector_energy.png` | Amber `#C4963C` |
| `[SECTOR BRIEF]` Critical Minerals | `tpl_sector_minerals.png` | Violet `#9678C4` |
| `[SECTOR BRIEF]` Biotech | `tpl_sector_biotech.png` | Green `#50A88A` |
| `[SECTOR BRIEF]` Cybersecurity | `tpl_sector_netsec.png` | Steel `#789EB4` |
| `[DEEP DIVE]` | `tpl_deepdive.png` | Pale gold `#C6A86E` |

All 1080×1080. Repo is public, licensed CC0.

## Colour logic

- **Gold** — recurring time-based columns (daily, weekly, monthly)
- **Terracotta** — event-driven, warm so it stands out as urgent
- **Per-vertical accents** — each SECTOR BRIEF vertical identifiable at a glance
- **Pale gold** — deep dives

## Layout

Background `#0B0F14`. Left vertical accent rule in the category colour.
Top: `AI ALPHA` over `ASIA · SEMIS · ENERGY · RESOURCES`.
Centre: category label, white, tracked.
Bottom: rule, then `@Edwardhwang888` in the accent colour.

**No personal name appears on any image.** The bottom handle is the only
identifier — it is a traffic pointer, not a byline.

## Rules

- Templates are **category identifiers**, not content carriers. Posts hold
  their own text; images do not need to convey information.
- Same image every time for the same category. Consistency is the point.
- **Never attach a photograph of a real person.** Copyright sits with the
  photographer, and using someone's likeness in promotional financial content
  is a separate risk from citing their public filings.
- Generating a new image per post is not the workflow. If a post needs a
  chart, that is a deliberate exception, and hosting it externally is a
  prerequisite.

## Regenerating templates

Source script: `make_templates.py` (Pillow, Liberation Sans). Categories,
accent colours and descriptors are defined in the `TEMPLATES` list at the
top. Regenerate all ten by running it; re-upload changed files to the repo.
