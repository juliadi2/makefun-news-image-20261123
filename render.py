#!/usr/bin/env python3
"""Render the 23 November 2026 world-news front page (1024x1024 PNG).

Fresh design for news-image-20261123: a newspaper front page carrying six
stories verified as first reported on Monday 23 November 2026. Run from the
repo root; writes entry.png next to this script. Uses Pillow (build-time
only -- the entry program main.py is stdlib-only and just copies entry.png).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 238)
INK = (18, 18, 18)
RED = (178, 34, 34)
GREY = (105, 105, 105)
RULE = (60, 60, 60)
PANEL = (238, 232, 220)
NAVY = (23, 48, 90)
GREEN = (22, 120, 60)
BLUE = (30, 90, 160)

FD = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FD + "DejaVuSerif-Bold.ttf"
SERIF = FD + "DejaVuSerif.ttf"
SANS_B = FD + "DejaVuSans-Bold.ttf"
SANS = FD + "DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill=INK, leading=1.25):
    """Draw lines left-aligned; returns the y just below the block."""
    lh = int(fnt.size * leading)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def hrule(draw, y, x0=32, x1=W - 32, width=2, fill=RULE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def kicker(draw, x, y, label):
    f = font(SANS_B, 17)
    draw.text((x, y), label, font=f, fill=RED)
    return y + 26


def icon_chart(draw, x0, y0, x1, y1):
    """Rising stock line on a light panel."""
    draw.rectangle([x0, y0, x1, y1], fill=PANEL, outline=RULE, width=2)
    pts = [(x0 + 14, y1 - 18), (x0 + 45, y1 - 34), (x0 + 70, y1 - 30),
           (x0 + 100, y1 - 58), (x0 + 130, y1 - 52), (x0 + 165, y1 - 84),
           (x0 + 196, y1 - 96)]
    draw.line(pts, fill=GREEN, width=5, joint="curve")
    draw.ellipse([pts[-1][0] - 6, pts[-1][1] - 6, pts[-1][0] + 6, pts[-1][1] + 6],
                 fill=GREEN)
    draw.text((x0 + 12, y0 + 8), "+31%", font=font(SANS_B, 26), fill=GREEN)


def icon_ship(draw, x0, y0, x1, y1):
    """Warship silhouette on waves."""
    draw.rectangle([x0, y0, x1, y1], fill=(214, 230, 244), outline=RULE, width=2)
    cx, cy = (x0 + x1) // 2, y0 + 52
    draw.polygon([(cx - 62, cy + 12), (cx + 62, cy + 12), (cx + 48, cy + 30),
                  (cx - 48, cy + 30)], fill=NAVY)
    draw.rectangle([cx - 28, cy - 8, cx + 8, cy + 12], fill=NAVY)
    draw.line([(cx - 8, cy - 26), (cx - 8, cy - 8)], fill=NAVY, width=4)
    draw.ellipse([cx - 40, cy - 22, cx - 30, cy - 12], fill=RED)
    draw.ellipse([cx + 18, cy - 30, cx + 28, cy - 20], fill=RED)
    for i, wx in enumerate(range(x0 + 12, x1 - 12, 34)):
        draw.arc([wx, y1 - 26, wx + 30, y1 - 8], 180, 360, fill=BLUE, width=3)


def icon_radar(draw, x0, y0, x1, y1):
    """Radar sweep with an aircraft dot."""
    draw.rectangle([x0, y0, x1, y1], fill=(222, 236, 222), outline=RULE, width=2)
    cx, cy = (x0 + x1) // 2, y1 - 14
    for r in (26, 52, 78):
        draw.arc([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=GREEN, width=3)
    draw.line([(cx, cy), (cx + 52, cy - 62)], fill=GREEN, width=3)
    draw.ellipse([cx + 46, cy - 68, cx + 58, cy - 56], fill=RED)
    draw.polygon([(cx - 44, cy - 30), (cx - 28, cy - 42), (cx - 24, cy - 30)],
                 fill=NAVY)


def icon_scales(draw, x0, y0, x1, y1):
    """Scales of justice."""
    draw.rectangle([x0, y0, x1, y1], fill=PANEL, outline=RULE, width=2)
    cx, cy = (x0 + x1) // 2, y0 + 30
    draw.line([(cx, cy), (cx, y1 - 22)], fill=INK, width=4)
    draw.line([(cx - 52, cy + 6), (cx + 52, cy + 6)], fill=INK, width=4)
    draw.line([(cx, y1 - 22), (cx - 26, y1 - 22)], fill=INK, width=4)
    draw.line([(cx, y1 - 22), (cx + 26, y1 - 22)], fill=INK, width=4)
    for sx in (cx - 52, cx + 52):
        draw.line([(sx, cy + 6), (sx, cy + 34)], fill=INK, width=3)
        draw.arc([sx - 20, cy + 26, sx + 20, cy + 52], 0, 180, fill=INK, width=3)


def icon_tanker(draw, x0, y0, x1, y1):
    """Oil tanker on waves."""
    draw.rectangle([x0, y0, x1, y1], fill=(244, 226, 214), outline=RULE, width=2)
    cx, cy = (x0 + x1) // 2, y0 + 56
    draw.polygon([(cx - 72, cy + 6), (cx + 72, cy + 6), (cx + 58, cy + 26),
                  (cx - 58, cy + 26)], fill=(140, 40, 30))
    draw.rectangle([cx + 34, cy - 18, cx + 58, cy + 6], fill=(140, 40, 30))
    draw.rectangle([cx - 58, cy - 10, cx + 28, cy + 6], fill=(178, 80, 60))
    for i, wx in enumerate(range(x0 + 12, x1 - 12, 34)):
        draw.arc([wx, y1 - 24, wx + 30, y1 - 6], 180, 360, fill=BLUE, width=3)


def icon_ball(draw, x0, y0, x1, y1):
    """Football."""
    draw.rectangle([x0, y0, x1, y1], fill=(222, 236, 222), outline=RULE, width=2)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    r = 42
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255),
                 outline=INK, width=3)
    draw.polygon([(cx, cy - 12), (cx + 11, cy - 4), (cx + 7, cy + 10),
                  (cx - 7, cy + 10), (cx - 11, cy - 4)], fill=INK)
    for dx, dy in ((-24, -14), (24, -14), (-26, 12), (26, 12), (0, 26)):
        draw.ellipse([cx + dx - 5, cy + dy - 5, cx + dx + 5, cy + dy + 5],
                     fill=INK)


def story(draw, x, y, width, kick, headline, deck, icon, icon_w=150,
          head_size=23, deck_size=16):
    """One story block: icon at top-right, kicker + headline beside it,
    deck below the icon. Returns the y just below the block."""
    icon_top = y
    icon_h = 96
    icon(draw, x + width - icon_w, icon_top, x + width, icon_top + icon_h)
    y = kicker(draw, x, y, kick)
    hf = font(SERIF_B, head_size)
    df = font(SANS, deck_size)
    text_w = width - icon_w - 14
    hlines = wrap(draw, headline, hf, text_w)
    y = text_block(draw, x, y, hlines, hf, leading=1.18)
    y = max(y + 4, icon_top + icon_h + 6)
    dlines = wrap(draw, deck, df, width)
    y = text_block(draw, x, y, dlines, df, leading=1.3)
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- Masthead ---
    mast = font(SERIF_B, 60)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=mast)
    d.text(((W - tw) / 2, 20), title, font=mast, fill=INK)
    hrule(d, 98, width=4, fill=INK)
    date_f = font(SANS_B, 24)
    date = "MONDAY, 23 NOVEMBER 2026"
    dw = d.textlength(date, font=date_f)
    d.text(((W - dw) / 2, 108), date, font=date_f, fill=RED)
    hrule(d, 144, width=2, fill=RED)

    # --- Lead: Nvidia (icon top-right, rule placed after the text) ---
    y = 158
    lead_top = y
    icon_chart(d, 772, lead_top, 992, lead_top + 120)
    y = kicker(d, 32, y, "TECHNOLOGY  ·  MARKETS")
    hf = font(SERIF_B, 34)
    hlines = wrap(d, "HUANG IS BACK: NVIDIA SURGES 31% AS BOARD REINSTATES CEO",
                  hf, 700)
    y = text_block(d, 32, y, hlines, hf, leading=1.15)
    y += 6
    df = font(SANS, 19)
    dlines = wrap(d, "Eleven days after resigning in scandal, Jensen Huang returns "
                  "to run the chipmaker — and the stock's best day since 2003 "
                  "lifts the Nasdaq 6.5% and the S&P 500 4.7%.", df, 700)
    y = text_block(d, 32, y, dlines, df, leading=1.3)
    y = max(y + 10, lead_top + 120 + 10)
    hrule(d, y)
    y += 8

    # --- Row 2: Libya + NATO ---
    col_w = 464
    y1 = story(d, 32, y, col_w, "WAR IN UKRAINE",
               "KYIV CONFIRMS SEA DRONES SANK RUSSIAN WARSHIP OFF LIBYA",
               "Zelenskyy says seven naval drones sank the corvette Merkury at "
               "Benghazi and hit the cargo ship Angara.", icon_ship)
    y2 = story(d, 528, y, col_w, "EUROPE  ·  SECURITY",
               "NATO SENDS SPY PLANES TO POLAND",
               "Allied AWACS aircraft reinforce Polish airspace as Warsaw "
               "summons Russia's envoy over three missiles that crossed its "
               "border.", icon_radar)
    y = max(y1, y2) + 10
    hrule(d, y)
    y += 8

    # --- Row 3: Myanmar + Iran ---
    y1 = story(d, 32, y, col_w, "ASIA  ·  JUSTICE",
               "UK RECOGNISES ROHINGYA GENOCIDE",
               "Four days after the world court found Myanmar guilty of "
               "genocide, London formally recognises it, sanctions five "
               "generals and freezes their assets.", icon_scales)
    y2 = story(d, 528, y, col_w, "MIDDLE EAST",
               "IRAN VOWS TO BREAK US NAVAL BLOCKADE 'BY ALL MEANS'",
               "Tehran calls the blockade an act of war and says it will use "
               "every tool to counter it, as the Hormuz standoff deepens.",
               icon_tanker)
    y = max(y1, y2) + 10
    hrule(d, y)
    y += 8

    # --- Bottom: FIFA (icon top-right) ---
    fifa_top = y
    icon_ball(d, 772, fifa_top, 992, fifa_top + 110)
    y = kicker(d, 32, y, "SPORT")
    hf = font(SERIF_B, 28)
    hlines = wrap(d, "UK TO HOST 2035 WOMEN'S WORLD CUP", hf, 700)
    y = text_block(d, 32, y, hlines, hf, leading=1.15)
    y += 6
    df = font(SANS, 18)
    dlines = wrap(d, "FIFA confirms England, Scotland, Wales and Northern Ireland "
                  "will stage the 2035 tournament — the first World Cup on "
                  "British soil since 1966. A US-led bid takes 2031.", df, 700)
    y = text_block(d, 32, y, dlines, df, leading=1.3)
    y = max(y + 10, fifa_top + 110 + 10)
    hrule(d, y)
    y += 8

    # --- In brief: Belgium strike (verified 23 Nov) ---
    y = kicker(d, 32, y, "IN BRIEF")
    bf = font(SANS_B, 17)
    bt = font(SANS, 17)
    d.text((32, y), "BELGIUM — ", font=bf, fill=INK)
    bx = 32 + d.textlength("BELGIUM — ", font=bf)
    blines = wrap(d, "An austerity strike grounds 429 flights at Brussels and "
                  "Charleroi airports; rail services disrupted nationwide.",
                  bt, W - 64 - (bx - 32))
    text_block(d, bx, y, blines, bt, leading=1.3)
    y += len(blines) * int(17 * 1.3) + 8

    # --- Footer ---
    hrule(d, y, width=1, fill=GREY)
    ff = font(SANS, 14)
    foot = "Monday 23 November 2026  ·  Sources: Reuters, AP, CNN, GOV.UK, FIFA"
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, y + 10), foot, font=ff, fill=GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
