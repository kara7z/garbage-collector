"""Slide 03 — JVM memory overview."""
from components import chrome, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from parts import card, ul
from icons import icon

KICKER = "03 — JVM memory overview"

LEFT = f"""
{ul([
    '<b>STACK</b> — one per thread, per method call.',
    'Holds <b>locals</b>, parameters and <b>references</b> to objects.',
    '<b>HEAP</b> — shared memory for <b>objects</b> and <b>arrays</b>.',
    'Only the <b>Heap</b> is managed by the <b>Garbage Collector</b>.',
], kind="", sm=False)}
<div class="note mt18" style="font-size:16.5px">
  <b>Mental model:</b> Stack = <i>what you are doing now</i> &nbsp;·&nbsp; Heap = <i>what you created</i>.
</div>
"""

DIAGRAM = f"""
<div class="col center" style="gap:0;width:100%;padding:6px 0 2px 0">
  <div class="node root" style="font-size:22px;padding:15px 44px;letter-spacing:.06em">{icon('cube',22,ORANGE)}<span>JVM MEMORY</span></div>
  <div style="height:26px;display:flex;align-items:center;color:{DIM}">
    <svg width="30" height="26" viewBox="0 0 30 26" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2v18"/><path d="M7 14l8 8 8-8"/></svg>
  </div>
  <div class="row gap18" style="width:100%;justify-content:center">
    <div class="card tight" style="width:330px;text-align:center;border-color:rgba(90,176,224,.5)">
      <div class="cap" style="color:{CYAN};margin-bottom:8px">STACK</div>
      <div style="display:flex;justify-content:center;margin-bottom:8px">{icon('stack',40,CYAN)}</div>
      <div class="h4">Method calls</div>
      <div class="body mt6" style="font-size:17px">locals · parameters · refs</div>
      <div class="mono mt10" style="font-size:13.5px;color:{DIM}">fast · per-thread · no GC</div>
    </div>
    <div class="card tight glow-o" style="width:330px;text-align:center;border-color:rgba(248,152,32,.6)">
      <div class="cap" style="color:{ORANGE};margin-bottom:8px">HEAP</div>
      <div style="display:flex;justify-content:center;margin-bottom:8px">{icon('heap',40,ORANGE)}</div>
      <div class="h4">Objects + arrays</div>
      <div class="body mt6" style="font-size:17px">shared · garbage-collected</div>
      <div class="mono mt10" style="font-size:13.5px;color:{ORANGE}">GC lives here ↓</div>
    </div>
  </div>
  <div style="height:24px;display:flex;align-items:center;color:{ORANGE}">
    <svg width="30" height="24" viewBox="0 0 30 26" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2v18"/><path d="M7 14l8 8 8-8"/></svg>
  </div>
  <div class="node" style="border-color:rgba(123,196,107,.5);color:#C9E8C1;font-size:18px;padding:12px 28px">{icon('broom',22,GREEN)}<span>Garbage Collector sweeps the Heap</span></div>
</div>
"""

BODY = f"""
<div class="h2">Where does Java keep <span class="grad">everything?</span></div>
<p class="lead mt10" style="font-size:24px">Two areas — the <span class="hl-c">Stack</span> for execution, the <span class="hl-o">Heap</span> for objects. Only the Heap is garbage-collected.</p>
<div class="row gap24 mt24" style="height:556px">
  <div style="width:760px">{card(LEFT, cls="accent-o", sheen="o", cap="The 30-second model")}</div>
  <div class="grow">{card(DIAGRAM, cap="JVM memory map", inner_style="padding-top:6px")}</div>
</div>
"""

NOTES = """
[2:00 – 3:30]

Say: the JVM splits memory in two. The stack is a pile of method frames —
every call pushes locals and references, every return pops them. It is fast
and self-cleaning.

The heap is where `new` puts objects. Every thread shares it, and nothing
pops automatically — that is the GC's job.

Point at the diagram: JVM MEMORY branches into STACK and HEAP, and the GC
arrow points ONLY at the heap. That one arrow prevents 90% of confusion later.

Transition: "so what does each side actually hold?"
"""

SLIDE = dict(
    n=3,
    kicker=KICKER,
    chrome=chrome(3, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
