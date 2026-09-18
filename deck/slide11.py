"""Slide 11 — System.gc()."""
from components import chrome, code_window, ORANGE, RED, CYAN, GREEN, DIM
from parts import card
from icons import icon

KICKER = "11 — System.gc()"

CODE = code_window(
    ["public class Demo {",
     "    public static void main(String[] args) {",
     "        System.gc();  // hint, not a command",
     "    }",
     "}"],
    filename="Demo.java", start=1, marks=(3,),
    vars_=("args",), classes=("Demo", "System"),
    size="big",
)

DIAGRAM = f"""
<div class="col center" style="gap:0;padding:10px 0 4px 0">
  <span class="node" style="font-size:17px;padding:11px 26px"><span>Application calls</span>&nbsp;<span class="mono" style="color:{CYAN}">System.gc()</span></span>
  <div style="height:22px;display:flex;align-items:center;color:{DIM}">
    <svg width="26" height="22" viewBox="0 0 30 26" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2v18"/><path d="M7 14l8 8 8-8"/></svg>
  </div>
  <span class="node root" style="font-size:17px;padding:11px 26px">{icon('cpu-obj',20,ORANGE)}<span>JVM decides</span></span>
  <div style="display:flex;gap:26px;margin-top:14px;width:100%;justify-content:center">
    <div style="flex:1;text-align:center">
      <div style="color:{GREEN}">╭──→</div>
      <span class="mono" style="font-size:16px;background:rgba(123,196,107,.12);border:1px solid rgba(123,196,107,.5);border-radius:10px;padding:9px 18px;color:#C9E8C1">perform GC</span>
      <div class="small mt6">if it makes sense</div>
    </div>
    <div style="flex:1;text-align:center">
      <div style="color:{DIM}">──╮</div>
      <span class="mono" style="font-size:16px;background:rgba(83,130,161,.08);border:1px solid #2C3E5C;border-radius:10px;padding:9px 18px;color:{DIM}">do something else</span>
      <div class="small mt6">ignore · delay · partial</div>
    </div>
  </div>
</div>
"""

BODY = f"""
<div class="h2"><code>System.gc()</code> is a <span class="grad">request.</span></div>
<p class="lead mt10" style="font-size:24px">It <span class="hl-o">suggests</span> a collection — the JVM may obey, delay, or ignore it entirely.</p>
<div class="row gap24 mt24" style="height:430px">
  <div style="width:660px" class="col gap18">
    {CODE}
    <div class="warn" style="font-size:18px;text-align:center">❌ Myth: <b>“System.gc() forces GC.”</b></div>
    <div class="ok" style="font-size:18px;text-align:center">✅ Reality: <b>it only hints the JVM to consider GC.</b></div>
  </div>
  <div class="grow">{card(DIAGRAM, cap="What really happens when you call it", inner_style="padding-top:2px")}</div>
</div>
<div class="mt18" style="text-align:center"><span class="mono" style="font-size:17px;color:{RED};background:rgba(232,69,60,.1);border:1px solid rgba(232,69,60,.5);border-radius:999px;padding:9px 26px">does NOT guarantee anything — never rely on it for correctness</span></div>
"""

NOTES = """
[14:30 – 15:30]

Read the highlighted line out loud, then kill the myth: System.gc() is
Runtime.getRuntime().gc() — a hint. The JVM looks at GC policy, load, heap
pressure and decides.

Why it exists: testing, benchmarking, rare explicit hints. Why you avoid it:
it can trigger a full STW collection at the worst moment and wreck latency;
most production guides disable or ignore it (-XX:+DisableExplicitGC).

Line for the exam: "System.gc() suggests; the JVM disposes."
"""

SLIDE = dict(
    n=11,
    kicker=KICKER,
    chrome=chrome(11, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)
