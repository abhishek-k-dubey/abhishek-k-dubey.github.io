"""Draw a concise development pathway as editable desktop and mobile SVGs.

Run from any directory. Uses only the Python standard library.
The pathway shows the broad sequence; activities can span stages.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'figures'
OUT.mkdir(parents=True, exist_ok=True)
INK = '#17233c'
MUTED = '#52627b'
BLUE = '#315fbd'
FORWARD = '#70839e'
STAGES = [
    ('Discovery', ['Molecule &', 'preclinical work']),
    ('Phase 1', ['Safety &', 'exposure']),
    ('Phase 2', ['Dose &', 'early benefit']),
    ('Phase 3', ['Confirm', 'benefit–risk']),
    ('Registration', ['Evidence', 'review']),
]
DESCRIPTION = ('Discovery and preclinical work lead to Phase 1, Phase 2, Phase 3 and '
               'registration. Clinical development and evidence strategy are Abhishek '
               'Dubey’s focus. Stages can overlap.')


def start(width, height):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
            '<title id="title">Drug development pathway</title>',
            f'<desc id="desc">{escape(DESCRIPTION)}</desc>',
            f'<defs><marker id="forward" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
            f'<path d="M0 0L10 5L0 10Z" fill="{FORWARD}"/></marker></defs>',
            f'<rect width="{width}" height="{height}" fill="white"/>']


def label(x, y, value, size=20, weight=400, color=INK, anchor='middle'):
    return (f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
            f'fill="{color}">{escape(value)}</text>')


def arrow(path):
    return (f'<path d="{path}" fill="none" stroke="{FORWARD}" stroke-width="2.6" '
            'stroke-linecap="round" marker-end="url(#forward)"/>')


def wide():
    svg = start(1000, 158)
    for i, (title, lines) in enumerate(STAGES):
        x = 6 + i * 202
        color = MUTED if i == 0 else BLUE
        fill = '#f6f8fc' if i == 0 else '#eef3ff'
        border = '#dde3ed' if i == 0 else '#c0d1f1'
        if i < 4:
            svg.append(arrow(f'M{x+181} 78H{x+196}'))
        svg.append(f'<rect x="{x}" y="12" width="180" height="130" rx="12" '
                   f'fill="{fill}" stroke="{border}" stroke-width="1.5"/>')
        svg.append(label(x+90, 50, title, 24, 600, color))
        svg.append(label(x+90, 88, lines[0], 19, 400, MUTED))
        svg.append(label(x+90, 115, lines[1], 18 if i == 2 else 19, 400, MUTED))
    svg.append('</svg>')
    (OUT / 'development-pathway.svg').write_text('\n'.join(svg))


def compact():
    svg = start(360, 480)
    for i, (title, lines) in enumerate(STAGES):
        y = 8 + i * 96
        color = MUTED if i == 0 else BLUE
        fill = '#f6f8fc' if i == 0 else '#eef3ff'
        border = '#dde3ed' if i == 0 else '#c0d1f1'
        if i < 4:
            svg.append(arrow(f'M180 {y+73}V{y+89}'))
        svg.append(f'<rect x="8" y="{y}" width="344" height="72" rx="10" '
                   f'fill="{fill}" stroke="{border}" stroke-width="1.5"/>')
        svg.append(label(24, y+43, title, 20 if i == 4 else 22, 600, color, 'start'))
        svg.append(label(184, y+30, lines[0], 19, 400, MUTED, 'start'))
        svg.append(label(184, y+54, lines[1], 17 if i == 2 else 19, 400, MUTED, 'start'))
    svg.append('</svg>')
    (OUT / 'development-pathway-mobile.svg').write_text('\n'.join(svg))


if __name__ == '__main__':
    wide()
    compact()
    print('Created linear desktop and mobile development pathways.')
