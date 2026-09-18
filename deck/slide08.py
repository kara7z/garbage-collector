"""Slide 08 — Generational garbage collection."""
from components import chrome, joke, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from parts import card, ul
from illus2 import gen_heap

KICKER = "08 — Generational GC"

LEFT = f"""
{ul([
    'New objects start in <b>Eden</b> (young generation).',
    'A <b>minor GC</b> clears the young gen fast — most objects are already dead.',
    'Survivors age in <b>S0 / S1</b>, then get <b>promoted</b> to Old.',
    'The <b>Old generation</b> holds long-lived data, collected rarely.',
])}
<div class="note mt18" style="font-size:16.5px">
  Collecting <b>500 MB of young garbage</b> beats scanning a <b>10 GB heap</b> every time.
</div>
"""

BODY = f"""
<div class="h2" style="font-size:56px">Most objects <span class="grad">die young.</span></div>
<p class="lead mt10" style="font-size:24px">So the Heap is split by age — clean the nursery often, disturb the elders rarely.</p>
<div class="row gap24 mt24" style="height:470px">
  <div style="width:720px">{card(LEFT, cls="accent-o", sheen="o", cap="Why generations exist")}</div>
  <div class="grow">{card(f'<div style="display:flex;justify-content:center">{gen_heap(880, 380)}</div>',
    cap="Young (Eden + S0/S1) → promotion → Old", inner_style="padding-top:4px")}</div>
</div>
<div class="mt18" style="width:1240px">{joke("Most Java objects have a very short career.", kind="blue")}</div>
"""

NOTES = """
[10:00 – 11:30]

The key statistic (weak generational hypothesis): ~90%+ of objects die young —
temporary strings, iterators, request DTOs. So why scan the whole heap?

Eden = birthplace. Minor GC = quick nursery cleanup. S0/S1 = ping-pong survivor
spaces where the few survivors age. After N survivals (age threshold) they are
promoted to Old. Major/Full GC on Old is rare but expensive.

Point at the dashed promotion arrow: surviving several collections is the only
way to "grow old". This sets up G1 regions perfectly.
"""

SLIDE = dict(
    n=8,
    kicker=KICKER,
    chrome=chrome(8, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
