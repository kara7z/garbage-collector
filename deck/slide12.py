"""Slide 12 — Object lifecycle."""
from components import chrome, code_window, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from parts import card, flow, step

KICKER = "12 — Object lifecycle"

FLOW = flow([
    step("Created", "<span class='mono'>new User()</span>", "box", color=CYAN),
    step("Reachable", "live refs exist", "ref", color=GREEN),
    step("Used", "read · write · call", "eye", color=CYAN),
    step("Unreachable", "refs dropped", "cross", color=RED),
    step("Eligible", "GC may take it", "trash", kind="hot", color=ORANGE),
    step("Reclaimed", "memory reusable", "check", kind="cool", color=GREEN),
])

CODE = code_window(
    ['User user = new User("Oussama");',
     "",
     "user = null;  // unreachable → eligible"],
    filename="Lifecycle.java", start=1, marks=(3,),
    vars_=("user",), classes=("User",),
    size="",
)

BODY = f"""
<div class="h2">Birth → life → <span class="grad">recycling.</span></div>
<p class="lead mt10" style="font-size:24px">Every Java object walks the same 6-step path — the GC owns the last two steps.</p>
<div class="mt24">{card(FLOW, cap="The whole story of an object, left to right", inner_style="padding-top:6px")}</div>
<div class="row gap24 mt24" style="height:330px">
  <div style="width:760px">{CODE}</div>
  <div class="grow">{card(
    '<div class="mono" style="font-size:17px;line-height:2;color:#C8D4E6">'
    '<span style="color:#5AB0E0">new User()</span> ──→ <span style="color:#7BC46B">Reachable + Used</span><br>'
    '<span style="color:#C792EA">user = null</span> ──→ <span style="color:#E8453C">Unreachable → Eligible</span><br>'
    '<span style="color:#F89820">GC runs</span> ──→ <span style="color:#7BC46B">Reclaimed ✓</span></div>'
    '<div class="note mt14" style="font-size:16px">Trace it: creation is <b>yours</b>, reclamation is the <b>GC’s</b>. You only control the middle — the references.</div>',
    cap="Map the code to the flow", inner_style="padding-top:2px")}</div>
</div>
"""

NOTES = """
[15:30 – 17:00]

Walk the six steps left to right with a finger. Created/Rechable/Used are the
program's business; Unreachable is the handoff; Eligible/Reclaimed belong to
the collector.

Map the snippet: line 1 = steps 1-3, line 3 = steps 4-5, and step 6 happens…
whenever the GC decides. Ask the room: "which step does `= null` perform?"
Answer: it only moves 3 -> 4. Nothing is freed yet.
"""

SLIDE = dict(
    n=12,
    kicker=KICKER,
    chrome=chrome(12, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
