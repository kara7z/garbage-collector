"""Slide 14 — OutOfMemoryError + live demo."""
from components import chrome, code_window, terminal, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from parts import card, ul

KICKER = "14 — When memory runs out"

CODE = code_window(
    ["for (int i = 0; i < 1_000_000; i++) {",
     "    byte[] data = new byte[1024];  // 1 KB per loop",
     "}",
     "",
     "System.gc();  // still just a hint"],
    filename="DemoOOM.java", start=1, marks=(2,),
    vars_=("i", "data"), classes=("System",),
    size="",
)

TERM = terminal([
    ("c", "limit the heap, then watch the GC"),
    ("p", '<span style="color:#9CDCFE">java</span> -Xms128m -Xmx256m App'),
    ("o", "run with a 128 MB → 256 MB heap"),
    ("p", '<span style="color:#9CDCFE">java</span> -Xlog:gc App'),
    ("o", "[0.023s][info][gc] GC(0) Pause Young … 12M→3M (48M)"),
], title="kara@youcode — ~/gc-demo", fs=16)

RIGHT = f"""
<div class="mono" style="font-size:19px;background:rgba(232,69,60,.1);border:1px solid rgba(232,69,60,.5);border-radius:10px;padding:12px 18px;color:#FF9C92">java.lang.OutOfMemoryError: Java heap space</div>
{ul(['<b>Heap is finite</b> — <code>-Xmx</code> sets the ceiling.',
     'GC can only free the <b>unreachable</b>.',
     'Leaked / pinned objects pile up → <b>boom</b>.'], kind="r", sm=True)}
<div class="row gap14 mt14">
  <span class="chip o">-Xms · start heap</span><span class="chip r">-Xmx · max heap</span><span class="chip c">-Xlog:gc · GC logs</span>
</div>
"""

BODY = f"""
<div class="h2">When memory <span class="grad">runs out.</span></div>
<p class="lead mt10" style="font-size:24px">If reachable garbage grows faster than the GC can free it, the JVM fails fast: <span class="hl-r">OutOfMemoryError</span>.</p>
<div class="row gap24 mt24" style="height:500px">
  <div style="width:700px" class="col gap18">
    {CODE}
    {TERM}
  </div>
  <div class="grow col gap18">
    {card(RIGHT, cls="accent-r", sheen="r", cap="The error every Java dev meets once")}
    {card('<div class="mono" style="font-size:17px;color:#FFD9A8">▶ LIVE DEMO — run it, shrink <span style="color:#FF7A59">-Xmx</span>, read <span style="color:#5AB0E0">-Xlog:gc</span>, watch pauses + heap.</div>'
          '<div class="small mt6">Tip: start at <code>-Xmx256m</code>, then try <code>64m</code> and compare the GC log.</div>',
          cls="accent-o", sheen="o", cap="Your turn (60–90 seconds)")}
  </div>
</div>
"""

NOTES = """
[19:00 – 22:00] — live demo. Rehearse this!

1. Run normally: `java App` — it survives.
2. `java -Xms128m -Xmx256m App` — explain flags: -Xms starting heap, -Xmx ceiling.
3. Shrink: `-Xmx64m` — trigger `OutOfMemoryError: Java heap space`. Show the exact line.
4. `java -Xlog:gc App` — show a young GC pause line, point at reclaimed numbers.

Narrate: the error means "the heap is full of reachable objects and I cannot
free a single byte". Fixes live in code (unpin references, bound caches,
stream instead of materialising) — not in bigger -Xmx. Bigger heap only delays it.

Safety: have the failing run pre-tested; keep `jconsole`/`jstat` out of scope.
"""

SLIDE = dict(
    n=14,
    kicker=KICKER,
    chrome=chrome(14, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
