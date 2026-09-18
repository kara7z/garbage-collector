"""Slide 10 — G1 Garbage Collector."""
from components import chrome, joke, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from parts import card, ul, region
from icons import icon

KICKER = "10 — G1 spotlight"

GRID = (
    region("E", "E", "eden") + region("O", "O", "old") + region("E", "E", "eden") + region("S", "S", "surv") +
    region("O", "O", "old") + region("E", "E", "eden", ring=True) + region("O", "O", "old") + region("E", "E", "eden") +
    region("S", "S", "surv") + region("O", "O", "old") + region("E", "E ring") 
)

# Build the 12-cell region grid explicitly (3 rows x 4 cols) with one "garbage-first" target ring.
CELLS = [
    ("E", "E", "eden", False), ("O", "O", "old", False), ("E", "E", "eden", False), ("S", "S", "survivor", False),
    ("O", "O", "old", False), ("E", "E", "eden ★", True), ("H", "H", "humongous", False), ("E", "E", "eden", False),
    ("S", "S", "survivor", False), ("O", "O", "old", False), ("E", "E", "eden", False), ("", "free", "free", False),
]

def g1_cell(label, kind, sub, ring):
    rl = f'<span class="rl">{sub}</span>' if sub else ""
    style = 'box-shadow:0 0 0 3px rgba(248,152,32,.55)' if ring else ""
    bg = {"E": "background:rgba(90,176,224,.16);border-color:rgba(90,176,224,.45);color:#BFE0FF",
          "O": "background:rgba(167,139,250,.16);border-color:rgba(167,139,250,.45);color:#DCD0FF",
          "S": "background:rgba(123,196,107,.16);border-color:rgba(123,196,107,.45);color:#C6E9BE",
          "H": "background:rgba(232,69,60,.2);border-color:rgba(232,69,60,.6);color:#FFB0A8",
          "free": "background:rgba(83,130,161,.07);border-color:rgba(83,130,161,.26);color:#46587A"}.get(kind, "")
    return (f'<div style="height:78px;border-radius:9px;border:1px solid;display:flex;flex-direction:column;'
            f'align-items:center;justify-content:center;font-family:FiraCode,monospace;font-size:18px;font-weight:700;{bg};{style}">'
            f'<span>{label}</span>{rl}</div>')

GRID_HTML = '<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px">' + \
    "".join(g1_cell(l, k, s, r) for l, k, s, r in CELLS) + "</div>"

LEFT = f"""
{ul([
    '<b>G1 = Garbage-First.</b> Heap split into equal <b>regions</b>.',
    'A region can be <b>Eden</b>, <b>Survivor</b>, <b>Old</b> or <b>Humongous</b>.',
    'G1 collects the regions with the <b>most garbage first</b>.',
    'Goal: big reclamation within a <b>pause-time target</b>.',
])}
<div class="row gap14 mt18">
  <span class="chip c">E · Eden</span><span class="chip g">S · Survivor</span>
  <span class="chip p">O · Old</span><span class="chip r">H · Humongous</span>
</div>
"""

BODY = f"""
<div class="h2">G1 cleans the <span class="grad">dirtiest first.</span></div>
<p class="lead mt10" style="font-size:24px"><b style="color:#EAEFF8">Garbage-First GC</b> — the default since JDK 9. Regions, not generations-in-concrete.</p>
<div class="row gap24 mt24" style="height:440px">
  <div style="width:720px">{card(LEFT, cls="accent-g", sheen="g", cap="G1 in 20 seconds")}</div>
  <div class="grow">{card(
    GRID_HTML
    + f'<div class="mono mt14" style="font-size:14.5px;color:{ORANGE};text-align:center">★ = next collection target — most garbage per millisecond of pause</div>',
    cap="Heap = regions · ★ collected first", inner_style="padding-top:4px")}</div>
</div>
<div class="mt18" style="width:1240px">{joke("Garbage First: finally, a collector that knows what to clean first.")}</div>
"""

NOTES = """
[13:00 – 14:30]

G1 divides the heap into ~hundreds of equal regions; each region has a role
(E/S/O/H) that can change over time. Humongous = objects > half a region.

"Garbage-First": each cycle G1 estimates "reclaimable bytes per ms of pause"
and collects the richest regions first, stopping when the pause-time goal
(-XX:MaxGCPauseMillis) is nearly spent.

Point at the ringed Eden cell: that is the dirtiest room in the house. Say the
joke deadpan, then bridge: "but can I just call System.gc() and skip all this?"
"""

SLIDE = dict(
    n=10,
    kicker=KICKER,
    chrome=chrome(10, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
