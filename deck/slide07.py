"""Slide 07 — How does garbage collection work?"""
from components import chrome, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from parts import card, pstep, blocks

KICKER = "07 — Mark · Sweep · Compact"

LEFT = pstep("1", '<span style="color:#FFD9A8">MARK</span> — find who is alive',
             'Trace from <b>GC Roots</b> and tag every <b>reachable</b> object.', on=True) + \
       f'<div style="height:14px"></div>' + \
       pstep("2", '<span style="color:#FFB0A8">SWEEP</span> — reclaim the rest',
             'Free memory of <b>unreachable</b> objects. Nothing points to them.') + \
       f'<div style="height:14px"></div>' + \
       pstep("3", '<span style="color:#BFE0FF">COMPACT</span> — defragment',
             'Slide survivors together so free space is <b>one</b> clean block.')

BEFORE = blocks([("A", "live"), ("B", "live"), ("G", "g"),
                 ("C", "live"), ("G", "g"), ("D", "live")])
AFTER = blocks([("A", "live"), ("B", "live"), ("C", "live"),
                ("D", "live"), ("", "free"), ("", "free")])

RIGHT = f"""
<div class="cap" style="font-size:13px;font-weight:700;letter-spacing:.15em;color:{DIM};margin-bottom:10px">HEAP BEFORE · G = garbage</div>
{BEFORE}
<div class="row mid mt14" style="gap:12px">
  <span class="mono" style="font-size:14px;color:{ORANGE}">mark ✓</span>
  <span style="color:{DIM}">→</span>
  <span class="mono" style="font-size:14px;color:{RED}">sweep</span>
  <span style="color:{DIM}">→</span>
  <span class="mono" style="font-size:14px;color:{CYAN}">compact</span>
</div>
<div class="cap mt18" style="font-size:13px;font-weight:700;letter-spacing:.15em;color:{DIM};margin-bottom:10px">HEAP AFTER · survivors packed left, free space right</div>
{AFTER}
<div class="note mt18" style="font-size:16px">Modern collectors are <b>more sophisticated</b> — but Mark-Sweep-Compact is the mental model everything builds on.</div>
"""

BODY = f"""
<div class="h2">Mark. Sweep. <span class="grad">Compact.</span></div>
<p class="lead mt10" style="font-size:24px">The classic 3-step model behind (almost) every collector — find the living, free the dead, tidy up.</p>
<div class="row gap24 mt24" style="height:500px">
  <div style="width:830px">{card(LEFT, cls="accent-o", sheen="o", cap="The cycle, every time")}</div>
  <div class="grow">{card(RIGHT, cap="What it looks like in memory")}</div>
</div>
"""

NOTES = """
[8:30 – 10:00] — the conceptual heart of the talk.

1. MARK: walk from roots, paint reachable objects. Everything unpainted is garbage.
2. SWEEP: reclaim unpainted memory. Note: sweeping alone leaves holes (fragmentation).
3. COMPACT: slide survivors together — allocation becomes a fast pointer bump again.

Point at BEFORE/AFTER: [A][B][G][C][G][D] becomes [A][B][C][D][ ][ ]. The G blocks
did not "move to trash" — their memory just became reusable.

Caveat out loud: real collectors (G1, ZGC…) are concurrent, regional, generational —
this is the simplified model, and it is enough to reason about all of them.
"""

SLIDE = dict(
    n=7,
    kicker=KICKER,
    chrome=chrome(7, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
