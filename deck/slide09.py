"""Slide 09 — Types of garbage collectors."""
from components import chrome, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from parts import card
from icons import icon

KICKER = "09 — Collector zoo"

def gc_card(ic, name, color, lines, accent):
    lis = "".join(f"<li>{l}</li>" for l in lines)
    return card(
        f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">'
        f'<span style="display:inline-flex;width:46px;height:46px;border-radius:13px;'
        f'background:{color}22;border:1px solid {color}66;align-items:center;justify-content:center">{icon(ic,26,color)}</span>'
        f'<div class="h4">{name}</div></div>'
        f'<ul class="bul sm">{lis}</ul>',
        cls=accent, inner_style="padding-top:2px")

BODY = f"""
<div class="h2">Pick your <span class="grad">collector.</span></div>
<p class="lead mt10" style="font-size:24px">Same job — find garbage. Different trade-offs between <span class="hl-o">throughput</span> and <span class="hl-c">pause time</span>.</p>
<div class="row gap18 mt24" style="height:470px">
  <div class="grow">{gc_card('box', 'Serial GC', '#97A5BD', ['Simple · <b>single-threaded</b>', 'Small apps · tiny heaps'], '')}</div>
  <div class="grow">{gc_card('boxes', 'Parallel GC', ORANGE, ['<b>Multi-threaded</b> stop-the-world', 'Max <b>throughput</b> batch jobs'], 'accent-o')}</div>
  <div class="grow">{gc_card('grid', 'G1 GC ★', GREEN, ['<b>Region-based</b>, default JDK 9+', 'Balances latency + throughput'], 'accent-g')}</div>
  <div class="grow">{gc_card('bolt', 'ZGC', CYAN, ['<b>Sub-millisecond</b> pauses', 'Huge heaps · concurrent'], 'accent-c')}</div>
  <div class="grow">{gc_card('leaf', 'Shenandoah', PURPLE, ['<b>Low-pause</b>, concurrent', 'Responsive services'], 'accent-p')}</div>
</div>
<div class="note mt18" style="font-size:17px;text-align:center">Rule of thumb: default to <b>G1</b> — reach for <b>ZGC / Shenandoah</b> only when pauses hurt. ★ = the one we zoom into next.</div>
"""

NOTES = """
[11:30 – 13:00]

One line per collector — this slide is a map, not a manual:
- Serial: one thread, simplest, fine for small/embedded.
- Parallel: many GC threads, best raw throughput, longer pauses.
- G1: the default since JDK 9 — regions + goals. Star it, we zoom in next.
- ZGC: concurrent, sub-ms pauses even on terabyte heaps.
- Shenandoah: also concurrent low-pause, different algorithm.

Axis to draw in the air: throughput (Parallel) vs pause time (ZGC/Shenandoah),
G1 in the middle. Selection flag teaser: -XX:+UseG1GC etc.
"""

SLIDE = dict(
    n=9,
    kicker=KICKER,
    chrome=chrome(9, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
