"""parts.py — cards, chips, flows, heap blocks, G1 regions, nodes, lists."""
from icons import icon
from components import ORANGE, CORAL, RED, CYAN, PURPLE, GREEN, DIM, TEXT, MUTE, arrow


def card(inner, style="", cls="", sheen=None, cap=None, inner_style=""):
    sh = f'<div class="sheen {sheen}"></div>' if sheen else ""
    cp = f'<div class="cap">{cap}</div>' if cap else ""
    return (f'<div class="card {cls}" style="{style}">{sh}{cp}'
            f'<div style="{inner_style}">{inner}</div></div>')


def chip(text, kind="", ic=None, color=None):
    i = icon(ic, 19, color or "currentColor") if ic else ""
    return f'<span class="chip {kind}">{i}{text}</span>'


def badge(text, kind=""):
    return f'<span class="badge {kind}">{text}</span>'


def step(title, sub="", ic=None, kind="", style="", color=None):
    i = f'<div class="ico">{icon(ic, 34, color or ORANGE)}</div>' if ic else ""
    s = f'<div class="s">{sub}</div>' if sub else ""
    return f'<div class="step {kind}" style="{style}">{i}<div class="t">{title}</div>{s}</div>'


def flow(steps, w=None):
    out = []
    for i, s in enumerate(steps):
        if i:
            out.append(arrow())
        out.append(s)
    style = f' style="width:{w}px"' if w else ""
    return f'<div class="flow"{style}>{"".join(out)}</div>'


def blocks(items, sm=False):
    cls = "blk sm" if sm else "blk"
    return f'<div class="blocks">' + "".join(
        f'<div class="{cls} {k}">{t}</div>' for t, k in items) + '</div>'


def region(label, kind, sub="", ring=False, h=None):
    rl = f'<span class="rl">{sub}</span>' if sub else ""
    style = f' style="height:{h}px"' if h else ""
    return f'<div class="region {kind}{" ring" if ring else ""}"{style}><span>{label}</span>{rl}</div>'


def stat(value, label, color=None):
    c = f' style="color:{color}"' if color else ""
    return f'<div class="stat"><span class="v"{c}>{value}</span><span class="l">{label}</span></div>'


def node(label, kind="", ic=None, style=""):
    i = icon(ic, 22, "currentColor") if ic else ""
    return f'<div class="node {kind}" style="{style}">{i}<span>{label}</span></div>'


def ul(items, kind="", sm=False):
    cls = f"bul {kind}" + (" sm" if sm else "")
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def pstep(num, title, body, on=False):
    return (f'<div class="pstep{" on" if on else ""}"><div class="n">{num}</div>'
            f'<div class="grow"><div class="h4">{title}</div>'
            f'<div class="body mt6">{body}</div></div></div>')


def sheen_card(sheen, cap, inner, style="", cls="", inner_style=""):
    return card(inner, style=style, cls=cls, sheen=sheen, cap=cap, inner_style=inner_style)