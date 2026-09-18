"""Slide 15 — Summary & key takeaways."""
from components import chrome, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from icons import icon

KICKER = "15 — Key takeaways"

def tcard(ic, color, title, body):
    return (f'<div class="card tight" style="flex:1 1 0;min-width:0;border-color:{color}55">'
            f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:8px">{icon(ic,24,color)}'
            f'<div class="h4" style="font-size:19px">{title}</div></div>'
            f'<div class="body" style="font-size:16.5px">{body}</div></div>')

ROW1 = (
    tcard("stack", CYAN, "Memory", "Stack = calls · <b>Heap</b> = objects") +
    tcard("cube", ORANGE, "Objects", "Allocated on the <b>Heap</b> via <b>new</b>") +
    tcard("ref", PURPLE, "Reachability", "<b>GC Roots →</b> reachable = kept")
)
ROW2 = (
    tcard("trash", RED, "Garbage", "<b>Unreachable</b> = eligible, not deleted") +
    tcard("broom", GREEN, "Collector", "<b>Mark · Sweep · Compact</b> the Heap") +
    tcard("heap", CYAN, "Generations", "<b>Young</b> (Eden+S) → <b>Old</b> via promotion")
)
ROW3 = (
    tcard("grid", GREEN, "Collectors", "Serial · Parallel · <b>G1 ★</b> · ZGC · Shenandoah") +
    tcard("terminal", ORANGE, "System.gc()", "A <b>hint</b> — never a guarantee") +
    tcard("lock", RED, "Leaks", "<b>Retained refs</b> pin memory → OOM")
)

BODY = f"""
<div class="h2 txtc">Key <span class="grad">takeaways.</span></div>
<p class="lead mt10 txtc" style="font-size:24px">Nine cards — if you remember these, you understand Java memory.</p>
<div class="col gap14 mt24">
  <div class="row gap14">{ROW1}</div>
  <div class="row gap14">{ROW2}</div>
  <div class="row gap14">{ROW3}</div>
</div>
<div class="note mt18 txtc" style="font-size:19px"><b>Understanding memory helps Java developers write more efficient and reliable applications.</b></div>
<div class="mt14 txtc" style="font-size:64px;font-weight:800;letter-spacing:-.02em">Questions<span style="color:{ORANGE}">?</span></div>
"""

NOTES = """
[22:00 – 25:00] — close with confidence.

Read the grid as three rows: (1) where things live, (2) how the GC reasons,
(3) what you control. Hit the three exam traps one last time:
- null ≠ delete, - System.gc() ≠ force, - GC ≠ no leaks.

Final line: "You create the objects — now you know who cleans them, and how
not to make their job impossible."

Invite questions. Backup questions if silence: "which collector is default?",
"what is a GC root?", "how would you prove a leak?" (heap dump / profiler).
"""

SLIDE = dict(
    n=15,
    kicker=KICKER,
    chrome=chrome(15, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
