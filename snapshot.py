#!/usr/bin/env python3
"""Build the daily eToro performance snapshot.

Writes data/perf-latest.json and data/perf-<snapshotDate>.json.
Read by SKILL.md 5.1. See tools/SNAPSHOT.md for the contract.

Credentials come from the environment, never from arguments or this file:
    ETORO_USER_KEY   the user API key   (x-user-key)
    ETORO_API_KEY    the app API key    (x-api-key)

Usage:  python tools/snapshot.py [--out DIR] [--dry-run]
"""
import argparse, json, os, sys, uuid, urllib.request, urllib.error, urllib.parse
from datetime import datetime, timezone, timedelta

BASE = "https://www.etoro.com"          # adjust if the deployment differs
SELF = "Edwardhwang888"
TAIPEI = timezone(timedelta(hours=8))

# Periods to record for the account itself.
SELF_PERIODS = ["AbsTwoYears", "CurrYear", "CurrMonth"]
# Periods for which the most-copied-ten comparison is kept.
FIELD_PERIODS = ["AbsTwoYears", "CurrMonth"]

# Fields that must never be cached - they move intraday. Recorded in the
# output so their absence reads as a decision rather than an oversight.
DO_NOT_CACHE = ["positions", "unrealizedPnl", "exposure",
                "availableCash", "thisWeekGain", "dailyGain"]


def get(path, **params):
    user_key, api_key = os.environ.get("ETORO_USER_KEY"), os.environ.get("ETORO_API_KEY")
    if not user_key or not api_key:
        sys.exit("ETORO_USER_KEY and ETORO_API_KEY must both be set in the environment.")
    url = f"{BASE}{path}?{urllib.parse.urlencode(params)}" if params else f"{BASE}{path}"
    req = urllib.request.Request(url, headers={
        "x-user-key": user_key,
        "x-api-key": api_key,
        "x-request-id": str(uuid.uuid4()),   # required on every request
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} on {path}: {e.read().decode()[:400]}")
    except Exception as e:
        sys.exit(f"request failed on {path}: {e}")


def most_copied(period, n=10):
    d = get("/api/v2/portfolios/rankings", period=period, sort="-copiers",
            pageSize=n, popularInvestor="true")
    return [{"username": r["username"], "copiers": r["copiers"],
             "gain": r["gain"], "aumValue": r.get("aumValue")}
            for r in d["results"]]


def self_row(period):
    return get(f"/api/v2/portfolios/{SELF}/rankings", period=period)["data"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    rows = {p: self_row(p) for p in SELF_PERIODS}
    base = rows["AbsTwoYears"]

    # The ranking max-date. Every row carries it as lastActivity; it is the
    # date the figures describe, and the date a post must disclose.
    stamp = str(base["lastActivity"])[:10]

    field = {p: most_copied(p) for p in FIELD_PERIODS}

    me = base["gain"]
    ten = field["AbsTwoYears"]
    beat = [r for r in ten if me > r["gain"]]
    lose = [r["username"] for r in ten if me <= r["gain"]]
    aums = [r["aumValue"] for r in ten if r.get("aumValue")]

    snap = {
        "snapshotDate": stamp,
        "generatedAtTaipei": datetime.now(TAIPEI).strftime("%Y-%m-%d %H:%M"),
        "source": "eToro rankings API (daily refresh); max-date = snapshotDate",
        "self": {
            "username": SELF, "cid": base["cid"], "subType": base.get("subType"),
            "copiers": base["copiers"], "riskScore": base.get("riskScore"),
            "aumTierDesc": base.get("aumTierDesc"), "aumValue": base.get("aumValue"),
            "gain": {p: rows[p]["gain"] for p in SELF_PERIODS},
            "annualizedReturn": base.get("annualizedReturn"),
            "fiveYearGain": base.get("fiveYearGain"),
            "tenYearGain": base.get("tenYearGain"),
            "winRatio": base.get("winRatio"),
        },
        "mostCopiedTen": {"sort": "-copiers", "popularInvestorOnly": True, "byPeriod": field},
        "derivedClaim": {
            "text": f"beats {len(beat)} of the {len(ten)} most-copied PIs",
            "window": "AbsTwoYears (exactly two years to snapshotDate)",
            "beatCount": len(beat), "outOf": len(ten), "losesTo": lose,
            "theirAumRangeUsd": [min(aums), max(aums)] if aums else None,
            "mustDisclose": "their AUM scale, and the snapshot date",
        },
        "doNotCache": DO_NOT_CACHE,
    }

    text = json.dumps(snap, indent=2)
    if a.dry_run:
        print(text); return
    os.makedirs(a.out, exist_ok=True)
    for name in ("perf-latest.json", f"perf-{stamp}.json"):
        with open(os.path.join(a.out, name), "w") as f:
            f.write(text + "\n")
    print(f"{stamp}: beats {len(beat)}/{len(ten)}; own AbsTwoYears {me*100:.2f}%")


if __name__ == "__main__":
    main()
