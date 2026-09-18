"""illus.py — hand-drawn SVG illustrations: node graphs, heap grids, legends.

These are the "technical diagrams / custom illustrations" of the deck: no
stock photos, only generated geometry, so everything stays crisp at 4K.
"""
from icons import icon_svg

ORANGE = "#F89820"
CORAL = "#FF7A59"
RED = "#E8453C"
CYAN = "#5AB0E0"
BLUE = "#5382A1"
PURPLE = "#A78BFA"
GREEN = "#7BC46B"
MUTE = "#60708A"
DIM = "#97A5BD"


def svg(w, h, body, extra=""):
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'xmlns="http://www.w3.org/2000/svg" {extra}>{body}</svg>')


def markers(colors=(ORANGE, RED, CYAN, MUTE, GREEN, PURPLE)):
    return "".join(
        f'<marker id="ah-{c.lstrip("#")}" viewBox="0 0 10 10" refX="8" refY="5" '
        f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>' for c in colors)


def node(x, y, w, h, label, color, fill="rgba(20,28,48,.95)", fs=15, dash=False,
         sub="", sub_color=None, bold=True):
    d = ' stroke-dasharray="6 5"' if dash else ""
    weight = "700" if bold else "500"
    body = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11" fill="{fill}" '
            f'stroke="{color}" stroke-width="1.8"{d}/>'
            f'<text x="{x + w/2}" y="{y + h/2 + (0 if not sub else -3)}" fill="{color}" '
            f'font-size="{fs}" font-weight="{weight}" font-family="FiraCode, monospace" '
            f'text-anchor="middle">{label}</text>')
    if sub:
        body += (f'<text x="{x + w/2}" y="{y + h/2 + 17}" fill="{sub_color or MUTE}" '
                 f'font-size="12.5" font-family="Inter, sans-serif" '
                 f'text-anchor="middle">{sub}</text>')
    return body


def arrow(x1, y1, x2, y2, color=ORANGE, dash=False, sw=2.2):
    d = ' stroke-dasharray="7 6"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="{sw}"{d} marker-end="url(#ah-{color.lstrip("#")})"/>')


def arrow_path(d, color=ORANGE, dash=False, sw=2.2):
    da = ' stroke-dasharray="8 7"' if dash else ""
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{da} '
            f'marker-end="url(#ah-{color.lstrip("#")})"/>')


def txt(x, y, s, color=DIM, fs=14, family="Inter, sans-serif", anchor="start",
        weight="400", ls=None):
    l = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{fs}" font-weight="{weight}"'
            f'{l} font-family="{family}" text-anchor="{anchor}">{s}</text>')


def legend(x, y, rows, gap=78):
    """rows: list of (color, title, subtitle)."""
    out = []
    for i, (color, l1, l2) in enumerate(rows):
        yy = y + i * gap
        out.append(f'<rect x="{x}" y="{yy}" width="24" height="24" rx="7" fill="{color}" '
                   f'fill-opacity=".22" stroke="{color}" stroke-width="1.6"/>')
        out.append(txt(x + 36, yy + 14, l1, "#EAEFF8", 15))
        out.append(txt(x + 36, yy + 33, l2, MUTE, 12.5))
    return "".join(out)


# ---------------------------------------------------------------- slide 01
GRID = ["LLLD", "LDDL", "LLLL", "DLLD", "LLLD", "LDLL"]


def heap_panel(w=640, h=772):
    cell, gap = 76, 13
    x0, y0 = 34, 152
    parts = [markers()]
    parts.append(node(x0, 12, 132, 46, "GC ROOT", ORANGE, fs=14))
    parts.append(arrow(x0 + 134, 35, x0 + 168, 35))
    parts.append(node(x0 + 171, 12, 120, 46, "Object A", CYAN, fs=14))
    parts.append(arrow(x0 + 293, 35, x0 + 327, 35))
    parts.append(node(x0 + 330, 12, 120, 46, "Object B", CYAN, fs=14))
    parts.append(node(x0 + 171, 78, 120, 46, "Object C", RED, fs=14, dash=True))
    parts.append(txt(x0 + 302, 105, "no path from a root", RED, 13.5))
    parts.append(txt(x0 + 302, 122, "→ unreachable", RED, 13.5))
    parts.append(txt(x0, 140, "HEAP", MUTE, 12.5, ls=2))
    for r, row in enumerate(GRID):
        for c, ch in enumerate(row):
            x = x0 + c * (cell + gap)
            y = y0 + r * (cell + gap)
            if ch == "L":
                fill, stroke, dot = "#16233A", "#2E4A6B", "#4E8FC0"
            else:
                fill, stroke, dot = "rgba(232,69,60,.20)", RED, "#FF7A6E"
            parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="13" '
                         f'fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>')
            parts.append(f'<circle cx="{x + cell/2}" cy="{y + cell/2}" r="7" fill="{dot}"/>')
    lx = 412
    parts.append(legend(lx, y0 + 22, [
        (CYAN, "live object", "reachable from a root"),
        (RED, "garbage", "unreachable → eligible"),
        (MUTE, "reclaimed", "memory available again"),
    ]))
    parts.append(arrow_path(f"M{lx + 4} {y0 + 262} C {lx + 60} {y0 + 300}, "
                            f"{lx + 96} {y0 + 232}, {lx + 14} {y0 + 214}", ORANGE, dash=True))
    parts.append(f'<g transform="translate({lx + 46},{y0 + 246})">'
                 f'{icon_svg("broom", 58, ORANGE, 1.6)}</g>')
    parts.append(txt(lx, y0 + 348, "Mark · Sweep", ORANGE, 15, family="FiraCode, monospace"))
    parts.append(txt(lx, y0 + 370, "Compact", ORANGE, 15, family="FiraCode, monospace"))
    parts.append(txt(x0, h - 22, "a heap is memory the JVM manages for you", MUTE, 14))
    return svg(w, h, "".join(parts))