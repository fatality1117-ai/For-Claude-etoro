import json,glob,sys
from datetime import datetime,timezone,timedelta
from collections import Counter
TP=timezone(timedelta(hours=8))
DEC=json.JSONDecoder(strict=False)

def salvage(body):
    """Parse discussions[] element-by-element, tolerating a truncated tail."""
    k=body.find('"discussions"')
    if k<0: return []
    i=body.find('[',k)+1
    out=[]
    while True:
        while i<len(body) and body[i] in ' \t\r\n,': i+=1
        if i>=len(body) or body[i]!='{': break
        try: obj,j=DEC.raw_decode(body,i)
        except Exception: break
        out.append(obj); i=j
    return out

def rows_from(path):
    try: outer=json.load(open(path))
    except Exception: return []
    body=outer.get("body")
    if not isinstance(body,str): return []
    out=[]
    for disc in salvage(body):
        p=disc.get("post") or {}
        c=p.get("created")
        if not c: continue
        o=p.get("owner") or {}
        summ=disc.get("summary") or {}
        out.append(dict(
            id=p.get("id"), created=c, user=o.get("username"),
            piLevel=o.get("piLevel") or 0, roles=",".join(o.get("roles") or []),
            likes=((disc.get("emotionsData") or {}).get("like") or {}).get("paging",{}).get("totalCount",0),
            comments=summ.get("totalCommentsAndReplies",0),
            shares=summ.get("sharedCount",0),
            nchars=len(((p.get("message") or {}).get("text")) or ""),
            ntags=len(p.get("tags") or []), nimg=len(p.get("attachments") or []),
        ))
    return out

def load(patterns):
    seen={}
    for pat in patterns:
        for f in glob.glob(pat):
            for r in rows_from(f):
                if r["id"]: seen[r["id"]]=r
    rows=list(seen.values())
    for r in rows:
        dt=datetime.fromisoformat(r["created"].replace("Z","+00:00"))
        r["dt_utc"]=dt; r["dt_tp"]=dt.astimezone(TP); r["hour_tp"]=r["dt_tp"].hour
        r["score"]=r["likes"]+3*r["comments"]+5*r["shares"]
    return rows

if __name__=="__main__":
    rows=load(sys.argv[1:])
    print("unique posts:",len(rows))
    if not rows: sys.exit()
    ds=sorted(r["dt_utc"] for r in rows)
    print("oldest TP:",ds[0].astimezone(TP).strftime("%Y-%m-%d %H:%M"))
    print("newest TP:",ds[-1].astimezone(TP).strftime("%Y-%m-%d %H:%M"))
    print("span hours: %.1f"%((ds[-1]-ds[0]).total_seconds()/3600))
    print("by TP date:",sorted(Counter(r["dt_tp"].date() for r in rows).items()))
    print("distinct authors:",len({r["user"] for r in rows}))
