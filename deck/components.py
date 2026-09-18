"""components.py — page chrome, IDE code windows, terminals, callouts."""
from javasyn import hl_line
from icons import icon, arrow_right, arrow_down

ORANGE = "#F89820"
CORAL = "#FF7A59"
RED = "#E8453C"
CYAN = "#5AB0E0"
BLUE = "#5382A1"
PURPLE = "#A78BFA"
GREEN = "#7BC46B"
DIM = "#97A5BD"
TEXT = "#EAEFF8"
MUTE = "#60708A"

TOTAL = 15


# ---------------------------------------------------------------- page chrome
def chrome(num, kicker, kclass="", topic="Java Memory Management · Garbage Collector"):
    return f"""
<div class="topline"></div>
<div class="header">
  <div class="kicker {kclass}"><span class="bar"></span>{kicker}</div>
  <div class="topic"><span class="dotj">J</span>{topic}</div>
</div>
<div class="footer">
  <span>Java Memory Management — Garbage Collector</span>
  <span>YouCode · Java Track</span>
  <span class="pageno"><b>{num:02d}</b> / {TOTAL:02d}</span>
</div>"""


# ---------------------------------------------------------------- IDE window
def code_window(lines, filename="GarbageDemo.java", start=1, marks=(), vars_=(),
                classes=(), size="", style="", tag="Java"):
    """`lines` = raw Java source lines; `marks` = 1-based displayed line numbers
    that must be highlighted (the line the slide is explaining)."""
    marks = set(marks)
    rows = []
    for i, raw in enumerate(lines, start=start):
        cls = "crow" + (" hl" if i in marks else "")
        src = hl_line(raw, vars_=vars_, classes=classes) or " "
        rows.append(
            f'<div class="{cls}"><span class="ln">{i}</span>'
            f'<span class="src">{src}</span></div>'
        )
    return f"""<div class="editor {size}" style="{style}">
  <div class="titlebar">
    <span class="lights"><i></i><i></i><i></i></span>
    <span class="tab"><span class="jco">J</span>{filename}</span>
    <span class="lang"><span class="jdot"></span>{tag}</span>
  </div>
  <div class="code">{''.join(rows)}</div>
</div>"""


# ---------------------------------------------------------------- terminal
def terminal(rows, title="kara@youcode — /home/kara/demo", style="", fs=None):
    """rows: list of (kind, html). kind: p prompt, o output, e error, c comment."""
    body = []
    for kind, text in rows:
        pre = {"p": '<span class="pr">$ </span>', "c": '<span class="cm"># </span>'}.get(kind, "")
        fs_style = f' style="font-size:{fs}px"' if fs else ""
        body.append(f'<div class="tl"{fs_style}>{pre}{text}</div>')
    return f"""<div class="term" style="{style}">
  <div class="tbar"><span class="lights"><i></i><i></i><i></i></span>{title}</div>
  <div class="tbody">{''.join(body)}</div>
</div>"""


# ---------------------------------------------------------------- callouts
def joke(text, kind="", size=18):
    return (f'<div class="joke {kind}">'
            f'<span>{icon("flame", 24, ORANGE)}</span>'
            f'<span class="jt" style="font-size:{size}px">“{text}”</span></div>')


def callout(text, kind="note"):
    return f'<div class="{kind}">{text}</div>'


def arrow(kind="", w=54, h=26):
    cls = f"arrow {kind}".strip()
    return f'<span class="{cls}" style="flex:0 0 {w}px;padding:0 6px">{arrow_right(w - 12, h)}</span>'


def arrow_v(kind="", h=54):
    cls = f"arrow {kind}".strip()
    return f'<span class="{cls}" style="height:{h}px">{arrow_down(30, h - 6)}</span>'