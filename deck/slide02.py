"""Slide 02 — Why does Java need memory management?"""
from components import chrome, joke, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from parts import card, chip, flow, step, ul
from illus2 import bin_cleanup

KICKER = "02 — The problem"

EXPLAIN = f"""
{ul([
    'Programs need memory to hold their <b>data</b> and their <b>objects</b>.',
    'Every <code>new</code> allocates memory that must eventually be <b>released</b>.',
    'In <b>C / C++</b> you call <code>free()</code> yourself — forget it and you leak or crash.',
    '<b>Java</b> does it for you: the Garbage Collector reclaims memory automatically.',
])}
<div class="note mt18" style="font-size:16.5px">
  <b>You never call free() in Java</b> — but memory is still finite, so something has to clean up.
</div>
"""

STEPS = flow([
    step("Create object", '<span class="mono">new User()</span>', "box", color=ORANGE),
    step("Use object", "the program reads and writes it", "eye", color=CYAN),
    step("Becomes unreachable", "no live reference points to it", "cross", color=RED),
    step("Garbage Collector", "finds what nobody can reach", "broom", kind="hot", color=ORANGE),
    step("Memory reclaimed", "the space can be reused", "check", kind="cool", color=GREEN),
])

BODY = f"""
<div class="row gap24" style="height:372px">
  <div style="width:960px">
    {card(EXPLAIN, cls="accent-o", sheen="o", cap="Why it matters at all")}
  </div>
  <div class="grow">
    {card(f'<div style="display:flex;justify-content:center">{bin_cleanup(700, 300)}</div>',
          cap="Objects are memory", inner_style="padding-top:4px")}
  </div>
</div>

<div class="mt24">{STEPS}</div>

<div class="mt24" style="width:1180px">
  {joke("You create the objects. Java cleans the mess.")}
</div>
"""

NOTES = """
[0:50 – 2:00]

Key idea: memory management is not a Java feature you opt into, it is a feature of the runtime.

Walk the room through the flow (it is repeated in every language, Java just automates step 4):
  create -> use -> becomes unreachable -> Garbage Collector -> reclaimed

Contrast with C/C++ briefly: malloc/free, use-after-free, double free, leaks.
Nobody in the room wants to debug that on a Friday.

Say clearly: "unreachable" is the ONLY condition Java cares about. An object that is
still referenced is never collected, even if your program will never touch it again.
That single sentence is the seed for slide 13 (leaks).

Land the joke, then move on: "so how does the JVM actually lay memory out?"
"""

SLIDE = dict(
    n=2,
    kicker=KICKER,
    chrome=chrome(2, KICKER),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)