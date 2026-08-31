import sys,statistics as st,random
from collections import defaultdict
sys.path.insert(0,'/home/claude/study')
from parse import load
from datetime import datetime,timezone
random.seed(42)
NOW=datetime.now(timezone.utc); MAT=48
rows=[r for r in load(sys.argv[1:]) if r["user"]]
mature=[r for r in rows if (NOW-r["dt_utc"]).total_seconds()/3600>=MAT]
by=defaultdict(list)
for r in mature: by[r["user"]].append(r)
norm=[]
for u,rs in by.items():
    med=st.median([x["score"] for x in rs])
    if len(rs)<5 or med<=0: continue
    for x in rs: x["rel"]=x["score"]/med; norm.append(x)

def sel(lo,hi): return [r for r in norm if lo<=r["hour_tp"]<=hi]

def mannwhitney_p(a,b,iters=20000):
    obs=st.median(a)-st.median(b); pool=a+b; na=len(a); c=0
    for _ in range(iters):
        random.shuffle(pool)
        if abs(st.median(pool[:na])-st.median(pool[na:]))>=abs(obs): c+=1
    return obs,(c+1)/(iters+1)

A=[r["rel"] for r in sel(17,19)]; B=[r["rel"] for r in sel(20,21)]
d,p=mannwhitney_p(A,B)
print(f"17-19 (n={len(A)}, med={st.median(A):.2f}) vs 20-21 (n={len(B)}, med={st.median(B):.2f})")
print(f"  median diff={d:+.2f}  permutation p={p:.4f}")

print("\nPER-AUTHOR PAIRED (each author's own median rel in each band):")
wins=0; tot=0
for u,rs in sorted(by.items()):
    a=[x["rel"] for x in rs if 17<=x["hour_tp"]<=19 and "rel" in x]
    b=[x["rel"] for x in rs if 20<=x["hour_tp"]<=21 and "rel" in x]
    if len(a)>=2 and len(b)>=2:
        tot+=1; ma,mb=st.median(a),st.median(b); w=ma>mb; wins+=w
        print(f"  {u:20} 17-19 n={len(a):2} med={ma:5.2f} | 20-21 n={len(b):2} med={mb:5.2f} | {'17-19' if w else '20-21':5} better")
print(f"  -> 17-19 better for {wins}/{tot} authors")
if tot:
    from math import comb
    p2=sum(comb(tot,k) for k in range(wins,tot+1))/2**tot
    print(f"  sign test one-sided p={p2:.3f}")

print("\nSANITY: does hour predict anything once author is removed? shuffle hours within author")
real=st.median(A)-st.median(B); big=0
for _ in range(5000):
    sh=[]
    for u,rs in by.items():
        v=[x for x in rs if "rel" in x]
        if not v: continue
        hs=[x["hour_tp"] for x in v]; random.shuffle(hs)
        for x,h in zip(v,hs): sh.append((h,x["rel"]))
    aa=[r for h,r in sh if 17<=h<=19]; bb=[r for h,r in sh if 20<=h<=21]
    if aa and bb and abs(st.median(aa)-st.median(bb))>=abs(real): big+=1
print(f"  within-author shuffle p={(big+1)/5001:.4f}")
