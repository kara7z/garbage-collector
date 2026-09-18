#!/usr/bin/env python3
"""Build dark-grunge Java GC deck (18 slides, minimal text, images embedded)."""
import random
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

BG = RGBColor(0x22, 0x28, 0x31)
CARD = RGBColor(0x31, 0x36, 0x3F)
TEAL = RGBColor(0x76, 0xAB, 0xAE)
LIGHT = RGBColor(0xEE, 0xEE, 0xEE)
DIM = RGBColor(0x9A, 0xA7, 0xAD)
TITLE_FONT = "Bebas Neue"
BODY_FONT = "Inter"
MONO = "Consolas"

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
random.seed(7)

def bg_fill(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BG

def add_shape(slide, shape_type, l, t, w, h, fill=None, line=None, lw=None):
    shp = slide.shapes.add_shape(shape_type, l, t, w, h)
    shp.line.fill.background()
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
    if line is not None:
        shp.line.color.rgb = line
        shp.line.width = Pt(lw or 1.5)
    return shp

def textbox(slide, l, t, w, h):
    tx = slide.shapes.add_textbox(l, t, w, h)
    tx.text_frame.word_wrap = True
    return tx

def para(tf, text, size=18, bold=False, color=LIGHT, font=BODY_FONT, align=PP_ALIGN.LEFT, space_after=Pt(4)):
    p = tf.add_paragraph() if len(tf.paragraphs) > 0 and tf.paragraphs[0].text != "" else tf.paragraphs[0]
    p.text = ""
    p.alignment = align
    p.space_after = space_after
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = color
    r.font.name = font
    return p

def chrome(slide, num, total=18):
    # top teal rule + grunge ticks
    add_shape(slide, MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(0.32), Inches(12.13), Pt(4), fill=TEAL)
    # footer
    tb = textbox(slide, Inches(0.6), Inches(6.95), Inches(9), Pt(24))
    para(tb.text_frame, f"KARA OUSSAMA  •  JAVA MEMORY & GC  •  {num:02d}/{total:02d}", size=9, color=DIM, font=BODY_FONT)
    # grunge specks (deterministic)
    for _ in range(7):
        x = random.uniform(0.4, 12.6)
        y = random.uniform(0.6, 6.8)
        s = random.uniform(0.03, 0.12)
        c = TEAL if random.random() < 0.25 else CARD
        shp = add_shape(slide, MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(s), Inches(s*0.35), fill=c)
        # hack: lighten CARD specks via line? keep solid
    # corner tag
    tag = add_shape(slide, MSO_SHAPE.RECTANGLE, Inches(11.9), Inches(6.85), Inches(0.85), Pt(26), fill=CARD, line=TEAL, lw=1)
    tag.text_frame.word_wrap = True
    tag.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
    tag.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    run = tag.text_frame.paragraphs[0].add_run()
    run.text = f"{num:02d}"
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = TEAL
    run.font.name = TITLE_FONT

def title_block(slide, kicker, title, accent_word=None):
    tb = textbox(slide, Inches(0.6), Inches(0.65), Inches(12), Inches(1.7))
    tf = tb.text_frame
    para(tf, kicker, size=13, bold=True, color=TEAL, font=BODY_FONT, space_after=Pt(2))
    p = tf.add_paragraph()
    p.space_after = Pt(2)
    # split title to highlight accent_word in teal
    if accent_word and accent_word in title:
        pre, post = title.split(accent_word, 1)
        for txt, col in [(pre, LIGHT), (accent_word, TEAL), (post, LIGHT)]:
            if txt:
                r = p.add_run()
                r.text = txt
                r.font.size = Pt(40)
                r.font.bold = True
                r.font.color.rgb = col
                r.font.name = TITLE_FONT
    else:
        r = p.add_run()
        r.text = title
        r.font.size = Pt(40)
        r.font.bold = True
        r.font.color.rgb = LIGHT
        r.font.name = TITLE_FONT

def bullets(slide, items, left=0.6, top=2.5, width=7.0, size=16):
    tb = textbox(slide, Inches(left), Inches(top), Inches(width), Inches(4))
    tf = tb.text_frame
    first = True
    for it in items:
        if first:
            p = tf.paragraphs[0]
            p.text = ""
            first = False
        else:
            p = tf.add_paragraph()
        p.space_after = Pt(10)
        p.level = 0
        r = p.add_run()
        r.text = "▸  " + it
        r.font.size = Pt(size)
        r.font.color.rgb = LIGHT
        r.font.name = BODY_FONT
    return tb

def card(slide, l, t, w, h, title, lines, title_size=18, body_size=13, highlight=False):
    c = add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h),
                  fill=CARD, line=TEAL if highlight else None, lw=2 if highlight else 0)
    # teal top strip
    add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t), Inches(w), Pt(8), fill=TEAL)
    tb = textbox(slide, Inches(l+0.3), Inches(t+0.3), Inches(w-0.6), Inches(h-0.5))
    tf = tb.text_frame
    para(tf, title, size=title_size, bold=True, color=TEAL if not highlight else TEAL, font=TITLE_FONT, space_after=Pt(6))
    for ln in lines:
        p = tf.add_paragraph()
        p.space_after = Pt(4)
        r = p.add_run()
        r.text = "•  " + ln
        r.font.size = Pt(body_size)
        r.font.color.rgb = LIGHT
        r.font.name = BODY_FONT
    return c

def side_image(slide, path, left=8.6, top=0.7, width=4.1, height=5.9):
    try:
        pic = slide.shapes.add_picture(path, Inches(left), Inches(top), Inches(width), Inches(height))
        # teal left border over image
        add_shape(slide, MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Pt(7), Inches(height), fill=TEAL)
        # dark caption bar
        cap = add_shape(slide, MSO_SHAPE.RECTANGLE, Inches(left), Inches(top+height-0.45), Inches(width), Inches(0.45), fill=BG)
        return pic
    except Exception as e:
        print("image skip", path, e)
        return None

def mono_box(slide, l, t, w, h, lines):
    c = add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h), fill=CARD, line=TEAL, lw=1.25)
    tb = textbox(slide, Inches(l+0.3), Inches(t+0.25), Inches(w-0.6), Inches(h-0.4))
    tf = tb.text_frame
    first = True
    for ln, col in lines:
        if first:
            p = tf.paragraphs[0]; p.text = ""; first = False
        else:
            p = tf.add_paragraph()
        p.space_after = Pt(2)
        r = p.add_run()
        r.text = ln
        r.font.size = Pt(10.5)
        r.font.color.rgb = col
        r.font.name = MONO
    return c

def new_slide(num):
    s = prs.slides.add_slide(BLANK)
    bg_fill(s)
    chrome(s, num)
    return s

TEAL_C = TEAL; LIGHT_C = LIGHT; DIM_C = DIM

# 01 TITLE
s = new_slide(1)
side_image(s, "assets/chip.jpg")
tb = textbox(s, Inches(0.6), Inches(1.1), Inches(7.4), Inches(4.5))
tf = tb.text_frame
para(tf, "YOUCODE  •  JAVA DEEP-DIVE", size=13, bold=True, color=TEAL)
p = tf.add_paragraph(); p.space_after = Pt(4)
for txt, col in [("JAVA MEMORY", LIGHT), (" & ", DIM), ("GARBAGE", TEAL), (" COLLECTOR", LIGHT)]:
    r = p.add_run(); r.text = txt; r.font.size = Pt(52); r.font.bold = True; r.font.color.rgb = col; r.font.name = TITLE_FONT
p2 = tf.add_paragraph(); p2.space_after = Pt(14)
r = p2.add_run(); r.text = "How Java cleans up after you — heap, generations, collectors, live demo."; r.font.size = Pt(15); r.font.color.rgb = LIGHT; r.font.name = BODY_FONT
box = add_shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(5.3), Inches(3.4), Inches(0.7), fill=TEAL)
box.text_frame.word_wrap = True; box.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER; box.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
r = box.text_frame.paragraphs[0].add_run(); r.text = "KARA OUSSAMA"; r.font.size = Pt(16); r.font.bold = True; r.font.color.rgb = BG; r.font.name = TITLE_FONT
tb2 = textbox(s, Inches(4.2), Inches(5.35), Inches(3.6), Inches(0.7))
para(tb2.text_frame, "15 min  •  Beginner  •  Java 17 + G1", size=12, color=DIM)

# 02 AGENDA
s = new_slide(2)
title_block(s, "02 — ROADMAP", "WHAT WE COVER", "COVER")
labels = [("01", "THE PROBLEM", "manual vs auto"), ("02", "MEMORY", "stack • heap • metaspace"),
          ("03", "HOW GC WORKS", "roots • sweep • generations"), ("04", "COLLECTORS", "G1, Parallel, ZGC"),
          ("05", "LIVE DEMO", "logs + VisualVM")]
for i, (n, t, d) in enumerate(labels):
    x = 0.6 + i * 2.45
    c = card(s, x, 2.7, 2.25, 3.3, f"{n}  {t}", [d], title_size=16, body_size=12, highlight=(i in (2, 4)))

# 03 PROBLEM
s = new_slide(3)
title_block(s, "03 — THE PROBLEM", "MANUAL vs AUTOMATIC", "AUTOMATIC")
card(s, 0.6, 2.7, 3.7, 3.5, "C / C++ MANUAL", ["you call malloc / free", "forgotten free = leak", "double free = crash"], highlight=False)
card(s, 4.6, 2.7, 3.7, 3.5, "JAVA AUTOMATIC", ["just use  new", "GC frees garbage", "no dangling pointers"], highlight=True)
side_image(s, "assets/recycle.jpg", left=8.6, top=2.5, width=4.1, height=3.7)

# 04 JVM MODEL
s = new_slide(4)
title_block(s, "04 — JVM MEMORY", "STACK  •  HEAP  •  METASPACE", "HEAP")
card(s, 0.6, 2.7, 3.7, 3.4, "STACK", ["primitives + refs", "one per thread", "auto-freed on return"])
card(s, 4.6, 2.7, 3.7, 3.4, "HEAP", ["all objects live here", "shared, GC-managed", "Eden → Old Gen"], highlight=True)
card(s, 8.5, 2.7, 3.7, 3.4, "METASPACE", ["class metadata", "native memory", "leaks → OOM"])

# 05 STACK VS HEAP
s = new_slide(5)
title_block(s, "05 — CORE SPLIT", "STACK vs HEAP", "HEAP")
card(s, 0.6, 2.7, 3.6, 3.5, "STACK — FAST", ["int x = 5", "LIFO, thread-local", "gone when method ends"])
card(s, 4.4, 2.7, 3.6, 3.5, "HEAP — SHARED", ["new Object()", "global, slower alloc", "GC decides lifetime"], highlight=True)
mono_box(s, 8.2, 2.7, 4.5, 3.5, [
    ("int x = 5;               // stack", DIM_C),
    ("User u = new User();     // heap", TEAL_C),
    ("u = null;  // now garbage ★", LIGHT_C),
])

# 06 METASPACE
s = new_slide(6)
title_block(s, "06 — OFTEN FORGOTTEN", "METASPACE IN 20 SEC", "20 SEC")
bullets(s, ["class bytecode metadata — not objects", "off-heap (native memory)", "watch for: bad redeploys, proxies → OOM"], left=0.6, top=2.7, width=7.0)
side_image(s, "assets/code.jpg", left=8.6, top=2.5, width=4.1, height=3.7)

# 07 GARBAGE?
s = new_slide(7)
title_block(s, "07 — KEY IDEA", "WHAT IS GARBAGE?", "GARBAGE?")
card(s, 0.6, 2.7, 3.7, 3.4, "GC ROOTS", ["stack refs", "static fields", "JNI handles"])
card(s, 4.6, 2.7, 3.7, 3.4, "REACHABLE = LIVE", ["follow refs from roots", "anything found stays"], highlight=True)
card(s, 8.5, 2.7, 3.7, 3.4, "ELSE = GARBAGE", ["unreachable → freed", "cycles still collected"])

# 08 MARK SWEEP
s = new_slide(8)
title_block(s, "08 — ALGORITHM 1", "MARK-AND-SWEEP", "SWEEP")
card(s, 0.6, 2.7, 5.6, 3.5, "1. MARK — walk from roots", ["tag every live object", "pause the world (STW)"], highlight=True)
card(s, 6.5, 2.7, 5.6, 3.5, "2. SWEEP — free the rest", ["reclaim dead blocks", "leaves fragmentation ✕"])
tb = textbox(s, Inches(0.6), Inches(6.35), Inches(12), Pt(30))
para(tb.text_frame, "■■■■■■□□■■□■■■■□□□□   →   MARK live ■  →  SWEEP □ free (gaps remain)", size=13, color=TEAL, font=MONO, align=PP_ALIGN.CENTER)

# 09 COMPACT + COPY
s = new_slide(9)
title_block(s, "09 — FIX FRAGMENTATION", "COMPACT  +  COPY", "COPY")
card(s, 0.6, 2.7, 5.6, 3.4, "MARK-COMPACT", ["slide survivors together", "one free block, slower"], highlight=True)
card(s, 6.5, 2.7, 5.6, 3.4, "COPYING (Eden → S0/S1)", ["copy live to other half", "perfect for short-lived"])
tb = textbox(s, Inches(0.6), Inches(6.3), Inches(12), Pt(30))
para(tb.text_frame, "■□■■□□ → COMPACT → ■■■■□□□□      EDEN ■□■ → COPY → S1 ■■", size=13, color=TEAL, font=MONO, align=PP_ALIGN.CENTER)

# 10 GENERATIONS
s = new_slide(10)
title_block(s, "10 — GENERATIONAL HYPOTHESIS", "MOST OBJECTS DIE YOUNG", "DIE YOUNG")
# flow boxes
boxes = [("EDEN", "new objects", 0.6, True), ("S0 / S1", "survivors × N", 3.6, False), ("OLD GEN", "long-lived", 6.6, False), ("METASPACE", "classes", 9.6, False)]
for t, d, x, hl in boxes:
    card(s, x, 2.7, 2.5, 2.6, t, [d], title_size=17, body_size=12, highlight=hl)
    if x > 0.7:
        arr = textbox(s, Inches(x-0.45), Inches(3.7), Inches(0.45), Inches(0.5))
        para(arr.text_frame, "▶", size=22, bold=True, color=TEAL, align=PP_ALIGN.CENTER)
tb = textbox(s, Inches(0.6), Inches(5.6), Inches(12), Pt(40))
para(tb.text_frame, "new → Eden  •  survive → S0↔S1  •  survive long → Old Gen", size=13, color=DIM, align=PP_ALIGN.CENTER)

# 11 MINOR VS MAJOR
s = new_slide(11)
title_block(s, "11 — GC EVENTS", "MINOR vs MAJOR", "MAJOR")
card(s, 0.6, 2.7, 5.6, 3.5, "MINOR GC — YOUNG", ["Eden full → clean Eden+S", "frequent, fast (ms)", "most garbage dies here ★"], highlight=True)
card(s, 6.5, 2.7, 5.6, 3.5, "MAJOR / FULL — OLD", ["Old Gen full → full sweep", "rare, slow, avoid it", "tune heap to delay it"])

# 12 COLLECTORS
s = new_slide(12)
title_block(s, "12 — PICK YOUR FIGHTER", "JAVA COLLECTORS", "COLLECTORS")
cols = [("SERIAL", ["1 thread", "tiny apps"], False), ("PARALLEL", ["throughput", "batch jobs"], False),
        ("G1 ★", ["default 17+", "balanced"], True), ("ZGC", ["<1ms pause", "huge heaps"], False),
        ("SHENANDOAH", ["low pause", "concurrent"], False)]
for i, (t, ln, hl) in enumerate(cols):
    card(s, 0.6+i*2.45, 2.7, 2.25, 3.4, t, ln, title_size=17, body_size=12, highlight=hl)
tb = textbox(s, Inches(0.6), Inches(6.3), Inches(12), Pt(30))
para(tb.text_frame, "CMS deprecated — don’t use for new projects.", size=11, color=DIM, align=PP_ALIGN.CENTER)

# 13 WHY G1
s = new_slide(13)
title_block(s, "13 — DEFAULT CHOICE", "WHY G1 WINS", "G1")
bullets(s, ["heap split into regions (not fixed Eden/Old)", "predictable pauses: -XX:MaxGCPauseMillis=200", "balanced throughput + latency ★"], left=0.6, top=2.7, width=7.0)
side_image(s, "assets/chip.jpg", left=8.6, top=2.5, width=4.1, height=3.7)

# 14 FLAGS + TOOLS
s = new_slide(14)
title_block(s, "14 — CONTROL IT", "FLAGS + TOOLS", "TOOLS")
mono_box(s, 0.6, 2.7, 6.2, 3.5, [
    ("-Xms512m -Xmx2g          # heap min/max", LIGHT_C),
    ("-XX:+UseG1GC             # default 17+", TEAL_C),
    ("-Xlog:gc*                # GC logs", LIGHT_C),
    ("jconsole / visualvm      # watch heap", DIM_C),
])
card(s, 7.0, 2.7, 5.6, 3.5, "VISUALVM FLOW", ["run app → attach process", "watch Heap + GC tabs", "force GC, see graph drop"], highlight=True)

# 15 DEMO CODE
s = new_slide(15)
title_block(s, "15 — LIVE DEMO", "TRASH GENERATOR", "TRASH")
mono_box(s, 0.6, 2.7, 7.4, 3.5, [
    ("for (i=1..12) {", DIM_C),
    ("  for (j=0..50000) new Trash(); // dies ★", TEAL_C),
    ("  for (k=0..500) leak.add(..);  // survives", LIGHT_C),
    ("  sleep(400);", DIM_C),
    ("}", DIM_C),
    ("run: java -Xlog:gc* GCDemo", LIGHT_C),
])
card(s, 8.2, 2.7, 4.4, 3.5, "WHAT TO WATCH", ["sawtooth heap graph", "[gc] Eden → S → Old", "pauses in ms"], highlight=True)

# 16 DEMO RESULTS
s = new_slide(16)
title_block(s, "16 — WHAT YOU SEE", "LOGS + HEAP GRAPH", "HEAP")
mono_box(s, 0.6, 2.7, 7.4, 3.5, [
    ("[gc] GC(12) Pause Young (Normal) 24M→5M  3.2ms", TEAL_C),
    ("[gc] GC(20) Pause Young 41M→9M (Eden full)", LIGHT_C),
    ("heap: /\\/\\/\\___/\\/\\/\\___  sawtooth = healthy", DIM_C),
    ("VisualVM: Monitor → Heap → [Perform GC]", LIGHT_C),
])
side_image(s, "assets/dark.jpg", left=8.2, top=2.7, width=4.4, height=3.5)

# 17 LEAKS
s = new_slide(17)
title_block(s, "17 — GC CAN’T SAVE YOU", "LEAKS + BEST PRACTICES", "LEAKS")
card(s, 0.6, 2.7, 5.6, 3.5, "LEAKS (still reachable!)", ["static List that grows", "forgotten listeners", "uncached caches"], highlight=True)
card(s, 6.5, 2.7, 5.6, 3.5, "DO THIS", ["bound collections / WeakHashMap", "remove listeners, close()", "size heap: Xms ≈ Xmx"])

# 18 CONCLUSION
s = new_slide(18)
side_image(s, "assets/recycle.jpg", left=8.6, top=0.7, width=4.1, height=5.9)
tb = textbox(s, Inches(0.6), Inches(1.0), Inches(7.4), Inches(4.2))
tf = tb.text_frame
para(tf, "18 — WRAP-UP", size=13, bold=True, color=TEAL)
p = tf.add_paragraph()
r = p.add_run(); r.text = "THANK YOU.\nQUESTIONS?"; r.font.size = Pt(52); r.font.bold = True; r.font.color.rgb = LIGHT; r.font.name = TITLE_FONT
para(tf, "GC = reachability  •  generations  •  G1 default  •  watch it in VisualVM", size=13, color=DIM)
para(tf, "Sources: Oracle JVM docs • JEP 376 (ZGC) • JEP 379 (Shenandoah) • Unsplash photos (embedded)", size=9, color=DIM)

prs.save("Java_GC_Kara_Oussama.pptx")
print(f"saved {len(prs.slides._sldIdLst)} slides -> Java_GC_Kara_Oussama.pptx")
