"""illus2.py — memory gauges, cleanup / bin metaphor, generational + region art."""
from icons import icon_svg
from illus import (svg, markers, node, arrow, arrow_path, txt, legend,
                   ORANGE, CORAL, RED, CYAN, BLUE, PURPLE, GREEN, MUTE, DIM)


def memory_bar(w=660, label="HEAP USAGE", used=0.78, color=ORANGE, note="", h=118,
               cells=True):
    """Horizontal heap gauge: used region + free region + object cells."""
    x, y, bw, bh = 22, 50, w - 44, 44
    fw = int(bw * used)
    parts = [
        txt(x, 28, label, MUTE, 13, ls=2),
        f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="10" fill="rgba(83,130,161,.08)" '
        f'stroke="#22304A" stroke-width="1.5"/>',
        f'<rect x="{x}" y="{y}" width="{fw}" height="{bh}" rx="10" fill="{color}" '
        f'fill-opacity=".24" stroke="{color}" stroke-width="1.6"/>',
    ]
    if cells:
        cx = x + 12
        while cx < x + bw - 32:
            live = cx < x + fw - 22
            c, op = (color, ".55") if live else (MUTE, ".20")
            parts.append(f'<rect x="{cx}" y="{y + 11}" width="30" height="22" rx="6" '
                         f'fill="{c}" fill-opacity="{op}"/>')
            cx += 46
    parts.append(txt(x, y + bh + 26, "used — live + garbage", DIM, 13.5))
    parts.append(txt(x + bw, y + bh + 26, "free", MUTE, 13.5, anchor="end"))
    if note:
        parts.append(txt(x, h - 8, note, MUTE, 13.5))
    return svg(w, h, "".join(parts))


def bin_cleanup(w=640, h=340):
    """Objects dropping out of the heap into the GC bin; freed memory returns."""
    parts = [markers(), f'<defs>{markers()}</defs>']
    # heap slab
    parts.append(f'<rect x="26" y="26" width="270" height="42" rx="10" '
                 f'fill="rgba(83,130,161,.10)" stroke="#2C3E5C" stroke-width="1.5"/>')
    parts.append(txt(40, 52, "HEAP", MUTE, 12.5, ls=2))
    for i in range(6):
        col = GREEN if i < 3 else RED
        parts.append(f'<rect x="{86 + i * 34}" y="36" width="24" height="22" rx="6" '
                     f'fill="{col}" fill-opacity=".45"/>')
    # falling garbage
    for i, (dx, dy) in enumerate(((0, 0), (34, 26), (-24, 40))):
        parts.append(f'<rect x="{130 + dx}" y="{92 + dy}" width="24" height="24" rx="6" '
                     f'fill="{RED}" fill-opacity=".4" stroke="{RED}" stroke-width="1.4"/>')
    parts.append(arrow_path("M142 84 C 150 110, 150 120, 146 132", RED, dash=True, sw=2))
    # bin
    parts.append(f'<g transform="translate(112,150)">{icon_svg("trash", 92, ORANGE, 1.5)}</g>')
    parts.append(txt(112, 268, "Garbage Collector", ORANGE, 15))
    parts.append(txt(112, 288, "reclaims unreachable objects", MUTE, 12.5))
    # return arrow back to heap
    parts.append(arrow_path("M216 232 C 300 236, 330 160, 336 96", GREEN, sw=2))
    parts.append(txt(352, 120, "memory", GREEN, 14, family="FiraCode, monospace"))
    parts.append(txt(352, 140, "available", GREEN, 14, family="FiraCode, monospace"))
    parts.append(txt(352, 160, "again", GREEN, 14, family="FiraCode, monospace"))
    parts.append(txt(26, h - 10, "unreachable objects are not deleted at the moment you "
                                 "drop the reference —", MUTE, 13))
    parts.append(txt(26, h + 12, "", MUTE, 13))
    return svg(w, h, "".join(parts))


def gen_heap(w=700, h=430):
    """Young (Eden + Survivors) vs Old generation layout with promotion."""
    parts = [markers()]
    parts.append(f'<rect x="20" y="34" width="660" height="230" rx="16" '
                 f'fill="rgba(20,28,48,.6)" stroke="#24314B" stroke-width="1.6"/>')
    parts.append(txt(40, 24, "HEAP", MUTE, 13, ls=2))
    # young gen
    parts.append(f'<rect x="42" y="56" width="356" height="186" rx="13" fill="rgba(90,176,224,.07)" '
                 f'stroke="{CYAN}" stroke-width="1.6" stroke-opacity=".65"/>')
    parts.append(txt(58, 80, "YOUNG GENERATION", CYAN, 14, ls=1.6, weight="700"))
    parts.append(f'<rect x="58" y="94" width="186" height="128" rx="11" fill="rgba(90,176,224,.16)" '
                 f'stroke="{CYAN}" stroke-width="1.5"/>')
    parts.append(txt(151, 152, "Eden", "#BFE0FF", 20, family="FiraCode, monospace", anchor="middle"))
    parts.append(txt(151, 176, "new objects", MUTE, 12.5, anchor="middle"))
    for i, (x, lab) in enumerate(((262, "S0"), (336, "S1"))):
        parts.append(f'<rect x="{x}" y="94" width="62" height="128" rx="11" '
                     f'fill="rgba(123,196,107,.14)" stroke="{GREEN}" stroke-width="1.5"/>')
        parts.append(txt(x + 31, 152, lab, "#C6E9BE", 17, family="FiraCode, monospace",
                         anchor="middle"))
        parts.append(txt(x + 31, 176, "survivors", MUTE, 11.5, anchor="middle"))
    # old gen
    parts.append(f'<rect x="420" y="56" width="240" height="186" rx="13" fill="rgba(167,139,250,.08)" '
                 f'stroke="{PURPLE}" stroke-width="1.6" stroke-opacity=".65"/>')
    parts.append(txt(436, 80, "OLD GENERATION", PURPLE, 14, ls=1.6, weight="700"))
    for i in range(3):
        parts.append(f'<rect x="{436}" y="{94 + i * 46}" width="208" height="36" rx="9" '
                     f'fill="{PURPLE}" fill-opacity=".16" stroke="{PURPLE}" '
                     f'stroke-width="1.2" stroke-opacity=".5"/>')
    parts.append(txt(444, 118, "long-lived objects", "#DCD0FF", 13.5))
    parts.append(txt(444, 164, "still reachable", "#DCD0FF", 13.5))
    parts.append(txt(444, 210, "collected rarely", MUTE, 12.5))
    # promotion arrow
    parts.append(arrow_path("M400 152 C 410 152, 412 152, 418 152", ORANGE, sw=2.2))
    parts.append(txt(352, 300, "promotion after surviving several collections", ORANGE, 14))
    parts.append(arrow_path("M240 236 C 300 296, 360 300, 412 300", ORANGE, dash=True, sw=2))
    parts.append(txt(20, h - 8, "most objects die young — that is why the split exists", MUTE, 13.5))
    return svg(w, h, "".join(parts))