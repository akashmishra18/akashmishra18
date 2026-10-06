#!/usr/bin/env python3
"""
Neofetch-style info card (840 x 880 -- same canvas as the ASCII portrait, so the
two line up side by side in the README). Lines fade + slide in one after another.

    python scripts/make_info_card.py          # writes info-card.svg
    STATIC=1 python scripts/make_info_card.py # frozen frame for previews

Edit the CARD list below to change what it says.
"""
import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")
STATIC = bool(os.environ.get("STATIC"))

W, H = 840, 880
PAD = 28
TITLEBAR_H = 30
BG, BG2, FRAME = "#0d1117", "#111722", "#30363d"
MUTED, INK = "#7d8590", "#e6edf3"
KEY, ACCENT, GREEN, GOLD = "#22d3ee", "#58a6ff", "#39d353", "#f2cc60"

# (key, [value lines])  -- key=None => section heading, key="" => spacer
CARD = [
    ("", None),
    ("Role",       ["Developer · Builder"]),
    ("Focus",      ["Mobile apps & web platforms"]),
    ("Education",  ["B.Tech CSE, Medicaps University", "Indore · 2023 – 2027"]),
    ("Prev",       ["SDE Intern @ Captain Infotech", "Jun – Aug 2025"]),
    ("Leads",      ["VP, Entrepreneurship Cell", "Medicaps · 50+ members"]),
    ("Stack",      ["React · Node · Express · MongoDB", "TypeScript · Tailwind · Java"]),
    ("Featured",   ["Vyapaar Setu  (live marketplace)"]),
    ("Also",       ["Rashtra Samachar · 13-language", "AI newspaper platform"]),
    ("Building",   ["Bahi-Khata  (to-do app, ledger vibe)"]),
    ("Certs",      ["Deloitte Technology & Business", "freeCodeCamp · Web Dev + JS"]),
]

FS = 27          # font size
LH = 40          # line height
KEY_X = PAD
VAL_X = PAD + 10 * FS * 0.6 + 26

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    '<style>'
    '.l{opacity:0;animation:in .45s ease-out both}'
    '@keyframes in{0%{opacity:0;transform:translateX(-12px)}100%{opacity:1;transform:translateX(0)}}'
    '@media (prefers-reduced-motion: reduce){.l{opacity:1!important;transform:none!important;animation:none!important}}'
    '</style>',
    f'<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>',
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
]
for i, c in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{20 + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{c}"/>')
parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" '
             f'text-anchor="middle">akash@github: ~$ neofetch</text>')

step = [0]


def line(svg_inner, y):
    """wrap a line in an animated group (or plain if STATIC)."""
    if STATIC:
        parts.append(f'<g>{svg_inner}</g>')
    else:
        d = 0.25 + step[0] * 0.12
        step[0] += 1
        parts.append(f'<g class="l" style="animation-delay:{d:.2f}s">{svg_inner}</g>')


y = TITLEBAR_H + 60
# header: akash@github
line(f'<text x="{KEY_X}" y="{y}" font-size="34" font-weight="700">'
     f'<tspan fill="{GREEN}">akash</tspan><tspan fill="{MUTED}">@</tspan>'
     f'<tspan fill="{ACCENT}">github</tspan></text>', y)
y += 20
line(f'<text x="{KEY_X}" y="{y}" font-size="{FS}" fill="{FRAME}">{"─" * 28}</text>', y)
y += 14

for key, vals in CARD:
    if vals is None:
        continue
    y += LH
    line(f'<text x="{KEY_X}" y="{y}" font-size="{FS}" font-weight="700" fill="{KEY}">'
         f'{html.escape(key)}</text>'
         f'<text x="{VAL_X - 18:.1f}" y="{y}" font-size="{FS}" fill="{MUTED}">:</text>'
         f'<text x="{VAL_X:.1f}" y="{y}" font-size="{FS}" fill="{INK}">{html.escape(vals[0])}</text>', y)
    for extra in vals[1:]:
        y += LH - 12
        line(f'<text x="{VAL_X:.1f}" y="{y}" font-size="{FS-3}" fill="{MUTED}">{html.escape(extra)}</text>', y)

# classic neofetch colour blocks
y += 50
blocks = ["#ff5f56", "#ffbd2e", "#27c93f", "#22d3ee", "#58a6ff", "#bc8cff", "#f2cc60", "#e6edf3"]
inner = "".join(f'<rect x="{KEY_X + i*46}" y="{y}" width="40" height="40" rx="5" fill="{c}"/>'
                for i, c in enumerate(blocks))
line(inner, y)

parts.append("</svg>")
svg = "".join(parts)
open(OUT, "w").write(svg)
print(f"wrote {OUT}: {W} x {H}, final y={y+40} (canvas {H}), {len(svg)//1024} KB")
