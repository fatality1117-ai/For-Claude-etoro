from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1080
BG = (11, 15, 20)
WHITE = (245, 241, 232)
GRAY = (146, 154, 163)
MUTED = (110, 118, 128)

F = "/usr/share/fonts/truetype/liberation/LiberationSans-{}.ttf"

# Each template: label text, accent hex, one-line descriptor
TEMPLATES = [
    ("DAILY BRIEF",     (212,162,78),  "Markets · watchlist · positions", "daily"),
    ("WEEKLY REVIEW",   (212,162,78),  "Last week, and the week ahead",   "weekly"),
    ("MONTHLY REVIEW",  (212,162,78),  "Full portfolio review",           "monthly"),
    ("MARKET PULSE",    (208,112,72),  "One event that moved the tape",    "pulse"),
    ("SECTOR BRIEF · AI INFRA",        (86,140,196), "Semiconductors & compute",       "sector_ai"),
    ("SECTOR BRIEF · ENERGY",          (196,150,60), "The power bottleneck",           "sector_energy"),
    ("SECTOR BRIEF · CRITICAL MINERALS",(150,120,196),"Rare earth, tungsten, copper",  "sector_minerals"),
    ("SECTOR BRIEF · BIOTECH",         (80,168,138),  "AI-driven discovery",            "sector_biotech"),
    ("SECTOR BRIEF · CYBERSECURITY",(120,158,180),"Network edge & security layer",        "sector_netsec"),
    ("DEEP DIVE",       (198,168,110), "Technical breakdown",              "deepdive"),
]

def tracked(draw, pos, text, font, fill, tracking=0):
    x, y = pos
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking
    return x

def make(label, accent, descriptor, slug):
    img = Image.new("RGB", (W, H), BG)

    # soft accent glow top-left quadrant
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W*0.28-320, 300-320, W*0.28+320, 300+320], fill=60)
    glow = glow.filter(ImageFilter.GaussianBlur(150))
    acc = Image.new("RGB", (W, H), accent)
    img = Image.composite(acc, img, glow.point(lambda p: int(p*0.28)))

    # corner vignette
    vign = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vign)
    for i in range(140):
        vd.rectangle([i,i,W-i,H-i], outline=int(80*(i/140)))
    img = Image.composite(Image.new("RGB",(W,H),(0,0,0)), img, vign.filter(ImageFilter.GaussianBlur(50)))

    draw = ImageDraw.Draw(img, "RGBA")

    MARGIN = 96
    # left spine
    draw.line([(MARGIN, 150), (MARGIN, H-150)], fill=accent+(150,), width=3)
    TX = MARGIN + 44

    f_brand   = ImageFont.truetype(F.format("Bold"), 30)
    f_kicker  = ImageFont.truetype(F.format("Bold"), 24)

    # brand mark top
    tracked(draw, (TX, 150), "AI ALPHA", f_brand, WHITE, tracking=4)
    tracked(draw, (TX, 188), "ASIA · SEMIS · ENERGY · RESOURCES", ImageFont.truetype(F.format("Regular"),18), MUTED, tracking=3)

    # category label — size depends on length
    words = label.split(" · ")
    if len(words) == 1:
        parts = [label]
    else:
        parts = [words[0]] + [" · ".join(words[1:])] if False else words

    # Decide font size by longest line
    longest = max(parts, key=len)
    size = 92
    if len(longest) > 16: size = 66
    if len(longest) > 22: size = 52
    f_label = ImageFont.truetype(F.format("Bold"), size)

    # vertically center the label block
    line_h = size + 10
    total_h = line_h * len(parts)
    ty = (H - total_h)//2 - 30
    for p in parts:
        draw.text((TX, ty), p, font=f_label, fill=WHITE)
        ty += line_h

    # accent underline under label block
    draw.line([(TX, ty+6), (TX+70, ty+6)], fill=accent, width=4)

    # descriptor
    f_desc = ImageFont.truetype(F.format("Regular"), 34)
    draw.text((TX, ty+30), descriptor, font=f_desc, fill=GRAY)

    # bottom rule + handle
    by = H - 150
    draw.line([(TX, by), (W-MARGIN, by)], fill=(255,255,255,28), width=1)
    draw.text((TX, by+28), "@Edwardhwang888", font=ImageFont.truetype(F.format("Bold"),28), fill=accent)

    out = f"/home/claude/tpl_{slug}.png"
    img.save(out)
    return out

paths = [make(*t) for t in TEMPLATES]
print("\n".join(paths))
