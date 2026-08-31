import sys,statistics as st
from collections import defaultdict
sys.path.insert(0,'/home/claude/study')
from parse import load
from datetime import datetime,timezone,timedelta
NOW=datetime.now(timezone.utc); MAT=48

rows=[r for r in load(sys.argv[1:]) if r["user"]]
mature=[r for r in rows if (NOW-r["dt_utc"]).total_seconds()/3600>=MAT]
by=defaultdict(list)
for r in mature: by[r["user"]].append(r)

# normalise each post against its own author's median score
norm=[]
for u,rs in by.items():
    med=st.median([x["score"] for x in rs])
    if len(rs)<5 or med<=0: continue
    for x in rs:
        x["rel"]=x["score"]/med
        norm.append(x)
print(f"normalised sample: n={len(norm)} across {len({r['user'] for r in norm})} authors")
print(f"maturity filter: >={MAT}h old | metric: likes + 3*comments + 5*shares, divided by author median\n")

buckets=defaultdict(list)
for r in norm: buckets[r["hour_tp"]].append(r["rel"])
print("Taipei hour | n  | median rel | mean rel")
for h in range(24):
    v=buckets.get(h,[])
    if not v: continue
    print(f"    {h:02d}:00   | {len(v):3}| {st.median(v):9.2f}  | {st.mean(v):7.2f}")

def band(lo,hi,label):
    v=[r["rel"] for r in norm if lo<=r["hour_tp"]<=hi] if lo<=hi else \
      [r["rel"] for r in norm if r["hour_tp"]>=lo or r["hour_tp"]<=hi]
    if v: print(f"{label:34} n={len(v):3}  median={st.median(v):.2f}  mean={st.mean(v):.2f}")
print("\n--- bands ---")
band(13,16,"13-16 (EU midday, pre-US-open)")
band(17,19,"17-19 (EU afternoon)")
band(20,21,"20-21 SLOT A candidate")
band(22,23,"22-23 (US midday)")
band(0,2,"00-02 (US afternoon)")
band(3,5,"03-05 SLOT B candidate")

print("\n--- image confound check (SKILL.md 7) ---")
for lab,sel in [("with image",[r for r in norm if r["nimg"]>0]),("no image",[r for r in norm if r["nimg"]==0])]:
    if sel: print(f"  {lab:12} n={len(sel):3} median rel={st.median([r['rel'] for r in sel]):.2f}")
imghr=defaultdict(list)
for r in norm: imghr[r["hour_tp"]].append(1 if r["nimg"]>0 else 0)
print("  image share by band:", {f"{lo}-{hi}": round(st.mean([v for h,vs in imghr.items() if lo<=h<=hi for v in vs]),2)
      for lo,hi in [(13,16),(17,19),(20,21),(22,23),(3,5)] if any(lo<=h<=hi for h in imghr)})
