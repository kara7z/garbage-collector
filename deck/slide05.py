"""Slide 05 — What is garbage?"""
from components import chrome, code_window, ORANGE, RED, CYAN, GREEN, DIM
from parts import card
from icons import icon

KICKER = "05 — What is garbage?"

CODE = code_window(
    ["User user = new User();",
     "",
     "user = null;  // reference dropped"],
    filename="GarbageDemo.java", start=1, marks=(3,),
    vars_=("user",), classes=("User",),
    size="big",
)

BEFORE_AFTER = f"""
<div class="row" style="gap:0;align-items:stretch;justify-content:center;padding:8px 0 2px 0">
  <div style="flex:1;text-align:center">
    <div class="cap" style="font-size:13px;font-weight:700;letter-spacing:.15em;color:{GREEN};margin-bottom:10px">BEFORE · reachable</div>
    <div style="display:flex;align-items:center;justify-content:center;gap:12px">
      <span class="mono" style="font-size:19px;background:rgba(90,176,224,.12);border:1px solid rgba(90,176,224,.45);border-radius:10px;padding:10px 18px;color:#BFE0FF">user</span>
      <svg width="70" height="26" viewBox="0 0 54 26" fill="none" stroke="{GREEN}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13h46"/><path d="M38 5l10 8-10 8"/></svg>
      <span class="mono" style="font-size:18px;background:rgba(123,196,107,.14);border:1px solid rgba(123,196,107,.5);border-radius:10px;padding:10px 18px;color:#C9E8C1">User object</span>
    </div>
    <div class="mono mt10" style="font-size:14px;color:{GREEN}">✓ GC keeps it — someone can reach it</div>
  </div>
  <div style="width:70px;display:flex;align-items:center;justify-content:center;color:{DIM}">
    <svg width="30" height="40" viewBox="0 0 54 26" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13h46"/><path d="M38 5l10 8-10 8"/></svg>
  </div>
  <div style="flex:1;text-align:center">
    <div class="cap" style="font-size:13px;font-weight:700;letter-spacing:.15em;color:{RED};margin-bottom:10px">AFTER · unreachable</div>
    <div style="display:flex;align-items:center;justify-content:center;gap:12px">
      <span class="mono" style="font-size:19px;background:rgba(83,130,161,.08);border:1px solid #2C3E5C;border-radius:10px;padding:10px 18px;color:{DIM}">user = null</span>
      <span class="mono" style="font-size:15px;color:{DIM}">✕</span>
      <span class="mono" style="font-size:18px;background:rgba(232,69,60,.1);border:1px dashed rgba(232,69,60,.6);border-radius:10px;padding:10px 18px;color:#FFB0A8">User object</span>
    </div>
    <div class="mono mt10" style="font-size:14px;color:{RED}">garbage → eligible, not yet deleted</div>
  </div>
</div>
<div class="mt14" style="display:flex;justify-content:center">
  <span style="display:inline-flex;align-items:center;gap:10px;background:rgba(232,69,60,.1);border:1px solid rgba(232,69,60,.45);border-radius:999px;padding:8px 20px;font-size:16px;color:#FFC0B9">{icon('trash',20,'#FF7A59')}<span><b>Eligible</b> ≠ deleted — the GC still has to run.</span></span>
</div>
"""

BODY = f"""
<div class="h2">Garbage = <span class="grad">unreachable.</span></div>
<p class="lead mt10" style="font-size:24px">Nobody can reach the object any more — so it becomes <span class="hl-o">eligible</span> for collection.</p>
<div class="row gap24 mt24" style="height:486px">
  <div style="width:600px" class="col gap18">
    {CODE}
    <div class="ok" style="font-size:19px;text-align:center"><b>An unreachable object becomes eligible for GC.</b></div>
  </div>
  <div class="grow">{card(BEFORE_AFTER, cap="Drop the last reference → the object floats away", inner_style="padding-top:4px")}</div>
</div>
<div class="warn mt18" style="font-size:17px">Setting <code>user = null</code> does <b>NOT</b> delete the object — it only cuts the last rope. The collector frees it later.</div>
"""

NOTES = """
[5:30 – 7:00]

Stress the vocabulary: reachable / unreachable / eligible / reclaimed are four
different states. `user = null` only moves BEFORE to AFTER.

Common exam trap: "null deletes the object" — false. It merely makes the object
a candidate. The GC decides when (and if) to reclaim it.

Point at AFTER: the dashed red box is still sitting in memory. It just has no
incoming arrows. That is the entire definition of garbage in Java.
"""

SLIDE = dict(
    n=5,
    kicker=KICKER,
    chrome=chrome(5, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
