"""Slide 13 — Memory leaks in Java."""
from components import chrome, code_window, joke, ORANGE, RED, CYAN, GREEN, DIM
from parts import card, ul, flow, step

KICKER = "13 — Memory leaks?!"

CODE = code_window(
    ["static List<byte[]> cache = new ArrayList<>();",
     "",
     "while (true) {",
     "    cache.add(new byte[1024 * 1024]);  // 1 MB, forever reachable",
     "}"],
    filename="Leak.java", start=1, marks=(4,),
    vars_=("cache",), classes=("List", "ArrayList"),
    size="",
)

FAN = f"""
<div class="col center" style="gap:0;padding:12px 0 4px 0">
  <span class="mono" style="font-size:18px;background:rgba(232,69,60,.12);border:1px solid rgba(232,69,60,.5);border-radius:10px;padding:9px 24px;color:#FFB0A8">static cache</span>
  <div style="height:20px;display:flex;align-items:center;color:{RED}">
    <svg width="26" height="20" viewBox="0 0 30 26" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2v18"/><path d="M7 14l8 8 8-8"/></svg>
  </div>
  <div class="row gap10" style="justify-content:center">
    <span class="mono" style="font-size:15px;background:rgba(232,69,60,.1);border:1px solid rgba(232,69,60,.4);border-radius:9px;padding:8px 14px;color:#FF9C92">1 MB</span>
    <span class="mono" style="font-size:15px;background:rgba(232,69,60,.1);border:1px solid rgba(232,69,60,.4);border-radius:9px;padding:8px 14px;color:#FF9C92">1 MB</span>
    <span class="mono" style="font-size:15px;background:rgba(232,69,60,.1);border:1px solid rgba(232,69,60,.4);border-radius:9px;padding:8px 14px;color:#FF9C92">1 MB</span>
    <span class="mono" style="font-size:15px;color:{DIM}">…</span>
  </div>
  <div class="mono mt12" style="font-size:14.5px;color:{RED}">useless, but reachable → GC must keep every one</div>
</div>
"""

FLOW = flow([
    step("Unused objects", "dead logically", "trash", color=RED),
    step("+ still referenced", "cache holds them", "lock", color=ORANGE),
    step("GC can't collect", "reachable = kept", "cross", color=RED),
    step("Heap grows", "until it bursts", "memory", kind="hot", color=ORANGE),
    step("OutOfMemoryError", "JVM gives up", "warn", color=RED),
])

BODY = f"""
<div class="h2" style="font-size:52px">Java has GC… <span class="grad">but leaks are real.</span></div>
<p class="lead mt10" style="font-size:24px">The GC frees the <span class="hl-o">unreachable</span> — it cannot free what you still <span class="hl-r">hold onto</span>.</p>
<div class="row gap24 mt24" style="height:400px">
  <div style="width:780px" class="col gap18">
    {CODE}
    {joke("Memory leak: when your program refuses to let go.")}
  </div>
  <div class="grow">{card(FAN, cap="One static list pinning megabytes forever", inner_style="padding-top:2px")}</div>
</div>
<div class="mt18">{FLOW}</div>
"""

NOTES = """
[17:00 – 19:00]

The shock slide: "I thought Java can't leak!" It can — a leak in Java means
"unintentionally reachable". The static cache pins every 1 MB array: logically
dead, but reachable, so the GC's hands are tied.

Walk the bottom flow, end on OutOfMemoryError as the cliffhanger for slide 14.
Prevention teaser: bound caches (LRU/max size), remove listeners, close
resources, avoid static collections that grow forever, WeakHashMap for canonical
caches. Live question: "where have you seen a list that never gets cleared?"
"""

SLIDE = dict(
    n=13,
    kicker=KICKER,
    chrome=chrome(13, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
