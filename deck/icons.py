"""icons.py — hand-drawn inline SVG icon + illustration kit.

All icons are stroke based and inherit `currentColor`, so they can be
tinted from the deck palette. No external assets, no emoji fonts.
"""

# Each entry: viewBox is always 24x24, stroke based geometry.
ICONS = {
    "box":        '<rect x="3.5" y="3.5" width="17" height="17" rx="3"/><path d="M8 12h8"/>',
    "boxes":      '<rect x="2.5" y="6.5" width="11" height="11" rx="2.5"/><rect x="10.5" y="2.5" width="11" height="11" rx="2.5"/>',
    "cube":       '<path d="M12 2.6l8.5 4.7v9.4L12 21.4 3.5 16.7V7.3z"/><path d="M3.7 7.4L12 12l8.3-4.6M12 12v9.3"/>',
    "arrow-r":    '<path d="M4 12h15"/><path d="M13 6l6 6-6 6"/>',
    "arrow-d":    '<path d="M12 4v15"/><path d="M6 13l6 6 6-6"/>',
    "trash":      '<path d="M4 7h16M9.5 7V4.8h5V7"/><path d="M6.5 7l1 12.2h9l1-12.2"/><path d="M10 11v5M14 11v5"/>',
    "broom":      '<path d="M14.5 3.5l6 6"/><path d="M16.8 5.8L9.4 13.2l-1.8-1.8z"/><path d="M7.6 11.4l5 5-1.6 3.4H6.6L4.2 18z"/>',
    "stack":      '<path d="M12 3.2l9 4.6-9 4.6-9-4.6z"/><path d="M3 12.6l9 4.6 9-4.6"/><path d="M3 16.9l9 4.6 9-4.6"/>',
    "heap":       '<rect x="2.5" y="4.5" width="19" height="15" rx="3"/><path d="M7 15.5v-4M11 15.5V8M15 15.5v-3M18.5 15.5V11"/>',
    "chip":       '<rect x="7" y="7" width="10" height="10" rx="2"/><path d="M12 2.5V7M12 17v4.5M2.5 12H7M17 12h4.5M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
    "gauge":      '<path d="M3.6 18a9 9 0 1116.8 0"/><path d="M12 13.5l4.4-4.6"/><circle cx="12" cy="14.6" r="1.6"/>',
    "clock":      '<circle cx="12" cy="12" r="8.6"/><path d="M12 7.2V12l3.4 2.2"/>',
    "flame":      '<path d="M13 2.5c2.6 3.6 5.6 5.9 5.6 9.5a6.6 6.6 0 01-13.2 0c0-1.7.7-3 1.8-4.4"/><path d="M12 20.4c-1.9 0-3.2-1.3-3.2-3 0-1.9 1.7-2.6 2.4-4.4 1 1.5 4 2.7 4 4.9 0 1.5-1.3 2.5-3.2 2.5z"/>',
    "leaf":       '<path d="M4.5 19.5C4.5 11 10 5 20 5c0 10-5.6 15-15.5 14.5z"/><path d="M9 15c1.7-3 4-5 7.5-6.4"/>',
    "recycle":    '<path d="M8 5.6l2-3.1 3.2 5.1"/><path d="M10 2.5H6.4A3 3 0 003.8 7l1.9 3.2"/><path d="M16 8.4h3.6A3 3 0 0122 12l-1.7 3"/><path d="M4.6 12.4L3.4 14.5"/><path d="M6.6 21.5h8.8a3 3 0 002.4-4.8l-1.7-2.7"/><path d="M13.6 17.8l-3 3.7 3 3.7"/>',
    "bolt":       '<path d="M13.4 2.5L5 13.6h5.3L8.9 21.5 18 10.2h-5.3z"/>',
    "terminal":   '<rect x="2.5" y="4" width="19" height="16" rx="3"/><path d="M6.6 9.2l3 2.8-3 2.8M12.4 14.8h5"/>',
    "check":      '<path d="M4.5 12.6l4.8 4.8L19.5 6.6"/>',
    "cross":      '<path d="M6.2 6.2l11.6 11.6M17.8 6.2L6.2 17.8"/>',
    "warn":       '<path d="M12 3.4l9 15.8H3z"/><path d="M12 9.6v4.4M12 16.6v.2"/>',
    "question":   '<circle cx="12" cy="12" r="8.8"/><path d="M9.4 9.4a2.7 2.7 0 015.2.9c0 1.8-2.6 2.2-2.6 4"/><path d="M12 17.4v.2"/>',
    "eye":        '<path d="M1.8 12S5.4 5.8 12 5.8 22.2 12 22.2 12 18.6 18.2 12 18.2 1.8 12 1.8 12z"/><circle cx="12" cy="12" r="3.1"/>',
    "lock":       '<rect x="4.5" y="10.5" width="15" height="10" rx="2.5"/><path d="M8 10.5V8a4 4 0 018 0v2.5"/>',
    "graph":      '<circle cx="5.6" cy="18.4" r="2.6"/><circle cx="12" cy="6.4" r="3.2"/><circle cx="18.6" cy="16.4" r="2.6"/><path d="M7.2 16.2l3.2-6.4M14.6 8.4l2.9 5.6"/>',
    "target":     '<circle cx="12" cy="12" r="8.6"/><circle cx="12" cy="12" r="4.6"/><circle cx="12" cy="12" r="1.1"/>',
    "cup":        '<path d="M4.4 8.6h12.2v5.6a5.6 5.6 0 01-5.6 5.6H10a5.6 5.6 0 01-5.6-5.6z"/><path d="M16.6 9.9h1.4a2.6 2.6 0 010 5.2h-1.4"/><path d="M8.4 2.6v3M12 2.6v3"/>',
    "memory":     '<rect x="2.5" y="7" width="19" height="10" rx="2.5"/><path d="M6.5 17v3M11 17v3M15.5 17v3M9 11h6"/>',
    "grid":       '<rect x="3.2" y="3.2" width="7.2" height="7.2" rx="2"/><rect x="13.6" y="3.2" width="7.2" height="7.2" rx="2"/><rect x="3.2" y="13.6" width="7.2" height="7.2" rx="2"/><rect x="13.6" y="13.6" width="7.2" height="7.2" rx="2"/>',
    "arrows-in":  '<path d="M4 4l6 6M4 10V4h6"/><path d="M20 4l-6 6M20 10V4h-6"/><path d="M4 20l6-6M4 14v6h6"/><path d="M20 20l-6-6M20 14v6h-6"/>',
    "cpu-obj":    '<rect x="3.5" y="3.5" width="17" height="17" rx="3"/><path d="M8.4 9.2h7.2v5.6H8.4z"/>',
    "code":       '<path d="M8.6 7.4L3.6 12l5 4.6M15.4 7.4l5 4.6-5 4.6"/>',
    "ref":        '<circle cx="6" cy="12" r="2.8"/><circle cx="18" cy="12" r="2.8"/><path d="M8.8 12h6.4"/>',
}


def icon(name, size=30, color="#F89820", sw=1.9, extra=""):
    """Return an inline SVG icon as HTML."""
    body = ICONS.get(name, ICONS["box"])
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round" '
        f'stroke-linejoin="round" style="{extra}">{body}</svg>'
    )


def icon_svg(name, size=30, color="#F89820", sw=1.9, extra=""):
    """Same as icon() but returns raw SVG (for embedding inside other SVG)."""
    body = ICONS.get(name, ICONS["box"])
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
        f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round" '
        f'stroke-linejoin="round" style="{extra}">{body}</svg>'
    )


def arrow_right(w=54, h=26, color="currentColor", sw=2.4):
    return (
        f'<svg width="{w}" height="{h}" viewBox="0 0 54 26" fill="none" stroke="{color}" '
        f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">'
        f'<path d="M2 13h46"/><path d="M38 5l10 8-10 8"/></svg>'
    )


def arrow_down(w=30, h=54, color="currentColor", sw=2.4):
    return (
        f'<svg width="{w}" height="{h}" viewBox="0 0 30 54" fill="none" stroke="{color}" '
        f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">'
        f'<path d="M15 3v45"/><path d="M7 40l8 10 8-10"/></svg>'
    )