"""Slide 06 — Reachability & GC Roots."""
from components import chrome, joke, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from parts import card, ul
from icons import icon

KICKER = "06 — Reachability & GC Roots"

GRAPH = f"""
<div class="col center" style="gap:0;padding:14px 0 6px 0">
  <div style="display:flex;align-items:center;gap:14px">
    <span class="node root" style="font-size:18px;padding:12px 26px">{icon('bolt',20,ORANGE)}<span>GC ROOT</span></span>
    <svg width="60" height="26" viewBox="0 0 54 26" fill="none" stroke="{ORANGE}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13h46"/><path d="M38 5l10 8-10 8"/></svg>
    <span class="node cool" style="font-size:18px;padding:12px 26px"><span>Object A</span></span>
    <svg width="60" height="26" viewBox="0 0 54 26" fill="none" stroke="{CYAN}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13h46"/><path d="M38 5l10 8-10 8"/></svg>
    <span class="node cool" style="font-size:18px;padding:12px 26px"><span>Object B</span></span>
  </div>
  <div class="mono mt10" style="font-size:14px;color:{GREEN}">✓ path from a root → reachable → GC keeps both</div>
  <div style="width:80%;border-top:2px dotted #22304A;margin:20px 0 16px 0"></div>
  <div style="display:flex;align-items:center;gap:14px">
    <span class="node dead" style="font-size:18px;padding:12px 26px">{icon('trash',20,'#FF7A59')}<span>Object C</span></span>
    <span class="mono" style="font-size:14px;color:{RED}">no path from any root</span>
    <span class="mono" style="font-size:14px;color:{RED};background:rgba(232,69,60,.12);border:1px solid rgba(232,69,60,.5);border-radius:999px;padding:6px 16px">→ UNREACHABLE</span>
  </div>
  <div class="small mt10">The GC traces the graph — it never asks “will you use this again?”, only “can I reach it?”</div>
</div>
"""

BODY = f"""
<div class="h2">Can the GC <span class="grad">reach it?</span></div>
<p class="lead mt10" style="font-size:24px">Every collection starts from <span class="hl-o">GC Roots</span> and follows references. No path = garbage.</p>
<div class="row gap24 mt24" style="height:470px">
  <div class="grow">{card(GRAPH, cap="Reachability graph — the only question the GC asks", inner_style="padding-top:2px")}</div>
  <div style="width:560px">{card(
    ul(['<b>Locals</b> in active stack frames',
        '<b>Static</b> fields of loaded classes',
        '<b>Active threads</b> themselves',
        '<b>JVM-internal</b> roots (JNI, …)'], kind="p", sm=False)
    + '<div class="note mt18" style="font-size:16.5px">Still referenced, even once, means <b>it stays</b> — usefulness is irrelevant.</div>',
    cls="accent-p", sheen="p", cap="Common GC roots (you don't memorise internals)")}</div>
</div>
<div class="mt18" style="width:1240px">{joke("Still referenced? Sorry, you're staying.", kind="purple")}</div>
"""

NOTES = """
[7:00 – 8:30]

Draw the trace with your hand: ROOT -> A -> B. B is kept only because A points
to it, and A is kept only because a root points to it. Cut every incoming edge
and the island (Object C) is garbage.

List the four root families quickly — no JVM internals rabbit hole. The punch
line: "useful but unreferenced" is collected; "useless but referenced" is NOT.
That is exactly why leaks (slide 13) exist.
"""

SLIDE = dict(
    n=6,
    kicker=KICKER,
    chrome=chrome(6, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
