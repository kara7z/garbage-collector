"""Slide 01 — Title: Java Memory Management / Garbage Collector."""
from components import chrome, code_window, ORANGE, RED, CYAN, PURPLE, GREEN, DIM
from parts import chip
from illus import heap_panel

KICKER = "YouCode · Java Track · Classroom Session"

BG_CODE = [
    "public class Heap {",
    "",
    "    void demo() {",
    '        User user = new User("Oussama");   // 1 allocation on the heap',
    "        user = null;                       // the reference is dropped",
    "        System.gc();                       // a request, not a command",
    "    }",
    "}",
]

BODY = f"""
<div style="position:absolute;left:-70px;top:520px;width:1080px;opacity:.15;transform:rotate(-1.6deg)">
  {code_window(BG_CODE, filename="Heap.java", size="mini", vars_=("user", "demo", "Heap"))}
</div>

<div class="row" style="position:relative">
  <div class="col" style="width:1010px;padding-top:6px">
    <div class="row mid gap14">
      <span style="width:54px;height:4px;border-radius:2px;background:linear-gradient(90deg,{ORANGE},{RED})"></span>
      <span style="font-size:19px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:{ORANGE}">YouCode · Java Track</span>
    </div>

    <div class="h1 mt24">Java Memory<br><span class="grad">Management</span></div>

    <div class="mt18" style="font-size:58px;font-weight:800;letter-spacing:.15em;color:#FFD9A8">
      GARBAGE COLLECTOR
    </div>

    <p class="lead mt24" style="width:940px">
      Understanding how Java manages memory automatically —
      where objects live, how the Garbage Collector finds them,
      and why it matters when you write real code.
    </p>

    <div class="row gap14 mt32" style="flex-wrap:wrap">
      {chip("Presenter · Kara Oussama", "o", "cup")}
      {chip("15 slides", "c", "grid")}
      {chip("15–25 min", "", "clock")}
      {chip("JDK 17+ · G1 is the default", "p", "bolt")}
    </div>
  </div>

  <div class="grow col" style="align-items:flex-end">{heap_panel()}</div>
</div>
"""

NOTES = """
[0:00 – 0:50]

Open by asking the room: "Who has ever written free() or delete?" — in Java nobody has.

Say: Java gives you two gifts: you never free memory manually, and you never want to.
That gift is the Garbage Collector.

Roadmap for the session (15-25 min):
  1. why memory needs managing (slides 2-3)
  2. stack vs heap and what garbage actually is (4-5)
  3. reachability + how the collector works (6-7)
  4. generations and the collectors you can choose (8-10)
  5. System.gc(), leaks, OutOfMemoryError + live demo (11-14)
  6. key takeaways (15)

Mention the presenter line and that everything is JDK 17+ behaviour, G1 being the default.
"""

SLIDE = dict(
    n=1,
    kicker=KICKER,
    chrome=chrome(1, "YouCode · Java Track", topic="Java Memory Management · Garbage Collector"),
    body=BODY,
    stage_style="top:150px",
    notes=NOTES,
)