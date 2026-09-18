"""Slide 04 — Stack vs Heap."""
from components import chrome, code_window, joke, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from parts import card, ul
from icons import icon

KICKER = "04 — Stack vs Heap"

CODE = code_window(
    ["User user = new User();",
     "int age = 20;"],
    filename="StackHeap.java", start=1, marks=(1,),
    vars_=("user", "age"), classes=("User",),
    size="big", style="",
)

DIAGRAM = f"""
<div class="row mid" style="gap:0;justify-content:center;padding:10px 0 4px 0">
  <div style="width:300px">
    <div class="cap" style="font-size:13px;font-weight:700;letter-spacing:.15em;color:{CYAN};margin-bottom:10px">STACK · locals + refs</div>
    <div class="card tight" style="border-color:rgba(90,176,224,.5);padding:16px 18px">
      <div class="mono" style="font-size:19px;color:#BFE0FF;background:rgba(90,176,224,.1);border:1px solid rgba(90,176,224,.35);border-radius:10px;padding:12px 16px">age&nbsp;&nbsp;= <span style="color:#B5CEA8">20</span></div>
      <div class="mono mt10" style="font-size:19px;color:#BFE0FF;background:rgba(248,152,32,.1);border:1px solid rgba(248,152,32,.45);border-radius:10px;padding:12px 16px">user&nbsp;&nbsp;●──┐</div>
      <div class="small mt10">each frame disappears on <code>return</code></div>
    </div>
  </div>
  <div style="width:120px;display:flex;flex-direction:column;align-items:center;gap:6px;color:{ORANGE}">
    <span class="mono" style="font-size:14px;color:{ORANGE}">reference</span>
    <svg width="110" height="26" viewBox="0 0 54 26" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 13h46"/><path d="M38 5l10 8-10 8"/></svg>
    <span class="mono" style="font-size:13px;color:{DIM}">not a copy</span>
  </div>
  <div style="width:340px">
    <div class="cap" style="font-size:13px;font-weight:700;letter-spacing:.15em;color:{ORANGE};margin-bottom:10px">HEAP · objects live here</div>
    <div class="card tight glow-o" style="border-color:rgba(248,152,32,.6);padding:22px 18px;text-align:center">
      <div style="display:flex;justify-content:center;margin-bottom:10px">{icon('cube',44,ORANGE)}</div>
      <div class="mono" style="font-size:20px;color:#FFD9A8">User object</div>
      <div class="mono mt6" style="font-size:14px;color:{DIM}">name · age · …</div>
      <div class="mono mt10" style="font-size:13px;color:{GREEN}">✓ reachable → GC keeps it</div>
    </div>
  </div>
</div>
<div class="row gap14 mt14">
  <div class="chip o">{icon('stack',19,ORANGE)}<span>Stack · fast · per-call</span></div>
  <div class="chip c">{icon('heap',19,CYAN)}<span>Heap · shared · GC-managed</span></div>
</div>
"""

BODY = f"""
<div class="h2">Stack is for execution. <span class="grad">Heap is for objects.</span></div>
<p class="lead mt10" style="font-size:24px">Variables live on the Stack. Objects live on the Heap — linked by <span class="hl-o">references</span>.</p>
<div class="row gap24 mt24" style="height:470px">
  <div style="width:640px" class="col gap18">
    {CODE}
    {card(ul(['<code>age</code> holds a <b>value</b> directly.',
              '<code>user</code> holds a <b>reference</b> to a heap object.'], kind="c", sm=True),
          cap="Read the two lines", inner_style="padding-top:2px")}
  </div>
  <div class="grow">{card(DIAGRAM, cap="One arrow explains half of Java memory", inner_style="padding-top:4px")}</div>
</div>
<div class="mt18" style="width:1240px">{joke("The stack remembers what you're doing. The heap stores what you created.", kind="blue")}</div>
"""

NOTES = """
[3:30 – 5:30]

Live-read the two lines. `int age = 20` — the value sits in the stack frame.
`User user = new User()` — the object is allocated on the heap, and only the
reference (an arrow) sits on the stack.

Trace the orange arrow with your finger: killing the arrow is not killing the
object — that distinction IS slides 5 and 6.

Primitive vs reference in one sentence. Land the joke, then ask: "so when does
an object become trash?"
"""

SLIDE = dict(
    n=4,
    kicker=KICKER,
    chrome=chrome(4, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
