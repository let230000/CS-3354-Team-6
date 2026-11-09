"""Writes use-case-diagram.svg (Figure 3.4). Source for /docs/p2/diagrams."""
import sys

FONT = "Calibri, Carlito, Arial, sans-serif"
INK = "#333333"
out = sys.argv[1]

UCS = {  # id: (cx, cy, rx, ry, label lines)
    "UC-01": (400, 95, 120, 30, ["UC-01", "Post a Listing"]),
    "UC-05": (400, 170, 120, 30, ["UC-05", "Edit or Remove a Listing"]),
    "UC-04": (400, 245, 120, 30, ["UC-04", "Confirm Handoff"]),
    "UC-02": (400, 340, 120, 30, ["UC-02", "Search for Textbooks"]),
    "UC-03": (400, 425, 125, 32, ["UC-03", "Reserve and Pay for a Listing"]),
    "UC-06": (640, 505, 85, 30, ["UC-06", "Take Payment"]),
    "UC-07": (400, 560, 120, 30, ["UC-07", "Confirm Receipt"]),
}
ACTORS = {  # name: (x, y_head, label lines)
    "Seller": (95, 140, ["Seller"]),
    "Buyer": (95, 420, ["Buyer"]),
    "PP": (875, 470, ["«system»", "Payment Processor"]),
}
LINKS = [("Seller", "UC-01"), ("Seller", "UC-05"), ("Seller", "UC-04"),
         ("Buyer", "UC-02"), ("Buyer", "UC-03"), ("Buyer", "UC-07"),
         ("PP", "UC-06")]

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="980" height="660" viewBox="0 0 980 660" font-family="{FONT}">',
     '<rect width="980" height="660" fill="white"/>',
     '<defs><marker id="open" markerWidth="12" markerHeight="12" refX="10" refY="5" orient="auto">'
     f'<path d="M0,0 L10,5 L0,10" fill="none" stroke="{INK}" stroke-width="1.3"/></marker></defs>',
     f'<rect x="230" y="40" width="530" height="570" fill="#F4F6F9" stroke="{INK}" stroke-width="1.4"/>',
     f'<text x="495" y="64" text-anchor="middle" font-size="17" font-weight="bold" fill="{INK}">BookBridge</text>']

def actor(x, y, lines):
    g = [f'<circle cx="{x}" cy="{y}" r="11" fill="white" stroke="{INK}" stroke-width="1.5"/>',
         f'<line x1="{x}" y1="{y+11}" x2="{x}" y2="{y+45}" stroke="{INK}" stroke-width="1.5"/>',
         f'<line x1="{x-20}" y1="{y+24}" x2="{x+20}" y2="{y+24}" stroke="{INK}" stroke-width="1.5"/>',
         f'<line x1="{x}" y1="{y+45}" x2="{x-16}" y2="{y+70}" stroke="{INK}" stroke-width="1.5"/>',
         f'<line x1="{x}" y1="{y+45}" x2="{x+16}" y2="{y+70}" stroke="{INK}" stroke-width="1.5"/>']
    for i, t in enumerate(lines):
        g.append(f'<text x="{x}" y="{y+90+i*17}" text-anchor="middle" font-size="15" fill="{INK}">{t}</text>')
    return g

def edge_point(cx, cy, rx, ry, tx, ty):
    import math
    a = math.atan2(ty - cy, tx - cx)
    return cx + rx * math.cos(a), cy + ry * math.sin(a)

for a, u in LINKS:
    ax, ay, _ = ACTORS[a]
    cx, cy, rx, ry, _ = UCS[u]
    sx = ax + (24 if ax < cx else -24)
    sy = ay + 30
    ex, ey = edge_point(cx, cy, rx, ry, sx, sy)
    s.append(f'<line x1="{sx}" y1="{sy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{INK}" stroke-width="1.3"/>')

# UC-03 includes UC-06 (dashed, open arrow, base -> included)
c3, c6 = UCS["UC-03"], UCS["UC-06"]
x1, y1 = edge_point(c3[0], c3[1], c3[2], c3[3], c6[0], c6[1])
x2, y2 = edge_point(c6[0], c6[1], c6[2], c6[3], c3[0], c3[1])
s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{INK}" stroke-width="1.3" stroke-dasharray="6,4" marker-end="url(#open)"/>')
s.append(f'<text x="{(x1+x2)/2+8:.0f}" y="{(y1+y2)/2-8:.0f}" font-size="14" fill="{INK}">«include»</text>')

for cx, cy, rx, ry, lines in UCS.values():
    s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="white" stroke="{INK}" stroke-width="1.4"/>')
    s.append(f'<text x="{cx}" y="{cy-3}" text-anchor="middle" font-size="13" font-weight="bold" fill="{INK}">{lines[0]}</text>')
    s.append(f'<text x="{cx}" y="{cy+14}" text-anchor="middle" font-size="14" fill="{INK}">{lines[1]}</text>')

for x, y, lines in ACTORS.values():
    s += actor(x, y, lines)

s.append(f'<text x="490" y="640" text-anchor="middle" font-size="15" font-style="italic" fill="{INK}">Figure 3.4  BookBridge use case diagram</text>')
s.append('</svg>')
open(out, "w").write("\n".join(s))
