#!/usr/bin/env python3
"""
ITIL 4 Foundation Training — full house-style deck builder.

THE PROBLEM THIS SOLVES
  Attempt 1 generated a clean house-style deck but collapsed each topic into one
  6-bullet slide: right format, only 97 slides, two thirds of the course lost.
  Attempt 2 preserved all 271 v11 slides but kept v11's formatting: right depth,
  but 249 slides of giant centred titles and bullet walls — not WSQ house style.

  This build does what was actually wanted: v11's CONTENT DEPTH rendered in the
  HOUSE VISUAL SYSTEM. Every teaching slide is re-drawn from its extracted text
  and images into a house component — never copied as-is:

    diagram slide      -> house header + framed image on a light canvas
    diagram + prose    -> two-panel: framed image | explanation card
    long bullet list   -> tile grid (2 cols, numbered accents)
    two-concept slide  -> comparison panel (fit-for-purpose vs fit-for-use etc.)
    short prose        -> statement card with an accent rule
    quiz               -> question card + lettered option tiles
    activity           -> activity card with the brief in numbered steps
    section divider    -> full house section slide with the topic number

  Every slide gets: the house header (kicker + title + rule), the house palette,
  Arial throughout, and the standard footer with the correct UEN.

Output: courseware/<title>-<version>.pptx
"""
import os, sys, re, io

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, ".claude", "skills", "courseware-build", "build")
sys.path.insert(0, BUILD)

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import course_data as C
try:
    from itil_content import ENRICH, DIAGRAM_TITLES
except ImportError:
    ENRICH, DIAGRAM_TITLES = {}, {}

SRC = os.path.join(HERE, "reference",
                   "WSQ - Master Trainer Slides - ITIL 4 Foundation Training -  v11.pptx")
OUT = os.path.join(HERE, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
ASSETS = os.path.join(HERE, ".claude", "skills", "courseware-build", "assets")

BLUE=RGBColor(0x1F,0x6F,0xEB); TEAL=RGBColor(0x10,0xB9,0x81); AMBER=RGBColor(0xF5,0x9E,0x0B)
INK=RGBColor(0x16,0x1B,0x26);  GREY=RGBColor(0x5B,0x63,0x72); LIGHT=RGBColor(0xF5,0xF8,0xFC)
WHITE=RGBColor(0xFF,0xFF,0xFF); LINE=RGBColor(0xE2,0xE8,0xF0); VIOLET=RGBColor(0x7C,0x3A,0xED)
ACCENTS = [BLUE, TEAL, VIOLET, AMBER]

# v11 slide ranges
TEACH_FROM, TEACH_TO = 19, 263
TOPIC_STARTS = {19: 1, 95: 2, 137: 3, 163: 4, 203: 5}


# ---------------------------------------------------------------- extraction
def extract(slide):
    """Pull the title, body lines and images out of a v11 slide."""
    title, body, pics = "", [], []
    for sh in slide.shapes:
        if sh.shape_type == 13:                       # picture
            try:
                pics.append((sh.image.blob, sh.image.ext,
                             Emu(sh.width).inches, Emu(sh.height).inches))
            except Exception:
                pass
            continue
        if not sh.has_text_frame:
            continue
        t = sh.text_frame.text.strip()
        if not t or t == "‹#›":
            continue
        top = Emu(sh.top).inches
        if not title and top < 0.75:
            title = t.split("\n")[0].strip()
            rest = [l.strip() for l in t.split("\n")[1:] if l.strip()]
            body.extend(rest)
        else:
            body.extend([l.strip() for l in t.split("\n") if l.strip()])
    body = [b for b in body if b and b != title and b != "‹#›"
            and not re.fullmatch(r"\d+", b)
            and "This material belongs to" not in b]
    return title, body, pics


def main():
    src = Presentation(SRC)
    src_slides = list(src.slides)
    SW, SH = src.slide_width, src.slide_height

    prs = Presentation()
    prs.slide_width, prs.slide_height = SW, SH
    BLANK = prs.slide_layouts[6]
    PAGE = {"n": 0}

    # ---------------------------------------------------------- primitives
    def slide():
        return prs.slides.add_slide(BLANK)

    def rect(s, x, y, w, h, color, line=None):
        sp = s.shapes.add_shape(1, x, y, w, h)
        sp.fill.solid(); sp.fill.fore_color.rgb = color
        if line is None: sp.line.fill.background()
        else: sp.line.color.rgb = line; sp.line.width = Pt(0.75)
        sp.shadow.inherit = False
        return sp

    def oval(s, x, y, w, h, color):
        sp = s.shapes.add_shape(9, x, y, w, h)
        sp.fill.solid(); sp.fill.fore_color.rgb = color
        sp.line.fill.background(); sp.shadow.inherit = False
        return sp

    def txt(s, x, y, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, space=3):
        tb = s.shapes.add_textbox(x, y, w, h)
        tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
        for i, ln in enumerate(runs):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = align; p.space_after = Pt(space)
            for t, sz, col, bold in ln:
                r = p.add_run(); r.text = t; r.font.size = Pt(sz)
                r.font.bold = bold; r.font.color.rgb = col; r.font.name = "Arial"
        return tb

    def footer(s):
        PAGE["n"] += 1
        txt(s, Inches(0.3), Inches(5.26), Inches(5.4), Inches(0.24),
            [[(f"{C.SHORT_TITLE}  ·  {C.COURSE_CODE}", 7, GREY, False)]])
        txt(s, Inches(3.4), Inches(5.26), Inches(3.2), Inches(0.24),
            [[(f"© 2026 {C.ORG}  ·  UEN 201200696W", 7, GREY, False)]],
            align=PP_ALIGN.CENTER)
        txt(s, Inches(9.2), Inches(5.26), Inches(0.5), Inches(0.24),
            [[(str(PAGE["n"]), 7, GREY, False)]], align=PP_ALIGN.RIGHT)

    def head(s, title, kicker=None, kcolor=BLUE):
        rect(s, 0, 0, SW, SH, WHITE)
        rect(s, 0, 0, Inches(0.19), Inches(1.02), kcolor)
        if kicker:
            txt(s, Inches(0.58), Inches(0.28), Inches(8.9), Inches(0.26),
                [[(kicker.upper()[:74], 9.5, kcolor, True)]])
        size = 20 if len(title) < 52 else (17 if len(title) < 78 else 15)
        txt(s, Inches(0.58), Inches(0.54), Inches(8.9), Inches(0.6),
            [[(title, size, INK, True)]])
        rect(s, Inches(0.58), Inches(1.14), Inches(8.84), Inches(0.014), LINE)

    def put_image(s, blob, ext, x, y, boxw, boxh, iw, ih):
        """Fit an image inside a box, centred, on a light canvas."""
        rect(s, x, y, boxw, boxh, LIGHT)
        scale = min(boxw / Inches(iw), boxh / Inches(ih)) * 0.92
        w, h = int(Inches(iw) * scale), int(Inches(ih) * scale)
        s.shapes.add_picture(io.BytesIO(blob), x + int((boxw - w) / 2),
                             y + int((boxh - h) / 2), width=w, height=h)

    # ---------------------------------------------------------- components
    def c_section(num, title, subtitle):
        s = slide()
        rect(s, 0, 0, SW, SH, WHITE)
        rect(s, 0, 0, Inches(0.21), SH, BLUE)
        rect(s, Inches(0.62), Inches(1.85), Inches(0.1), Inches(1.5), TEAL)
        txt(s, Inches(0.92), Inches(1.9), Inches(7.2), Inches(0.34),
            [[(f"TOPIC {num:02d}", 12, BLUE, True)]])
        txt(s, Inches(0.92), Inches(2.26), Inches(7.6), Inches(1.2),
            [[(title, 27, INK, True)]])
        if subtitle:
            txt(s, Inches(0.94), Inches(3.42), Inches(7.6), Inches(0.7),
                [[(subtitle, 10, GREY, False)]])
        txt(s, Inches(7.6), Inches(0.7), Inches(1.9), Inches(1.3),
            [[(f"{num:02d}", 60, RGBColor(0xE8,0xEE,0xF7), True)]], align=PP_ALIGN.RIGHT)
        footer(s)

    def c_image(title, kicker, blob, ext, iw, ih, caption=None):
        s = slide(); head(s, title, kicker)
        boxh = Inches(3.5) if caption else Inches(3.85)
        put_image(s, blob, ext, Inches(0.58), Inches(1.3), Inches(8.84), boxh, iw, ih)
        if caption:
            txt(s, Inches(0.58), Inches(4.88), Inches(8.84), Inches(0.34),
                [[(caption, 9, GREY, False)]])
        footer(s)

    def c_image_text(title, kicker, blob, ext, iw, ih, lines):
        s = slide(); head(s, title, kicker)
        put_image(s, blob, ext, Inches(0.58), Inches(1.3), Inches(4.5), Inches(3.85), iw, ih)
        rect(s, Inches(5.28), Inches(1.3), Inches(4.14), Inches(3.85), LIGHT)
        rect(s, Inches(5.28), Inches(1.3), Inches(0.045), Inches(3.85), TEAL)
        body = [[("•  " + l, 9.5 if len(lines) > 5 else 10.5, INK, False)] for l in lines[:8]]
        txt(s, Inches(5.48), Inches(1.48), Inches(3.8), Inches(3.55), body, space=6)
        footer(s)

    def c_tiles(title, kicker, items, accent=BLUE):
        s = slide(); head(s, title, kicker)
        n = len(items)
        cols = 2 if n > 3 else 1
        rows = (n + cols - 1) // cols
        gapx, gapy = Inches(0.16), Inches(0.13)
        w = int((Inches(8.84) - gapx * (cols - 1)) / cols)
        h = min(Inches(1.05), int((Inches(3.8) - gapy * (rows - 1)) / max(rows, 1)))
        size = 10.5 if n <= 6 else 9
        for i, it in enumerate(items):
            r, c = divmod(i, cols)
            x = Inches(0.58) + c * (w + gapx)
            y = Inches(1.32) + r * (h + gapy)
            col = ACCENTS[i % len(ACCENTS)]
            rect(s, x, y, w, h, LIGHT)
            rect(s, x, y, Inches(0.045), h, col)
            oval(s, x + Inches(0.16), y + Inches(0.16), Inches(0.26), Inches(0.26), col)
            txt(s, x + Inches(0.16), y + Inches(0.185), Inches(0.26), Inches(0.22),
                [[(str(i + 1), 8, WHITE, True)]], align=PP_ALIGN.CENTER)
            txt(s, x + Inches(0.52), y + Inches(0.12), w - Inches(0.66), h - Inches(0.22),
                [[(it, size, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
        footer(s)

    def c_compare(title, kicker, lhead, litems, rhead, ritems):
        s = slide(); head(s, title, kicker)
        rect(s, Inches(0.58), Inches(1.3), Inches(4.3), Inches(3.85), LIGHT)
        rect(s, Inches(5.12), Inches(1.3), Inches(4.3), Inches(3.85), LIGHT)
        rect(s, Inches(0.58), Inches(1.3), Inches(4.3), Inches(0.055), BLUE)
        rect(s, Inches(5.12), Inches(1.3), Inches(4.3), Inches(0.055), TEAL)
        txt(s, Inches(0.78), Inches(1.46), Inches(3.9), Inches(0.3),
            [[(lhead, 12.5, BLUE, True)]])
        txt(s, Inches(5.32), Inches(1.46), Inches(3.9), Inches(0.3),
            [[(rhead, 12.5, TEAL, True)]])
        txt(s, Inches(0.78), Inches(1.84), Inches(3.9), Inches(3.2),
            [[("•  " + t, 9.5, INK, False)] for t in litems[:8]], space=6)
        txt(s, Inches(5.32), Inches(1.84), Inches(3.9), Inches(3.2),
            [[("•  " + t, 9.5, INK, False)] for t in ritems[:8]], space=6)
        footer(s)

    def c_statement(title, kicker, lines, accent=BLUE):
        s = slide(); head(s, title, kicker)
        rect(s, Inches(0.58), Inches(1.32), Inches(8.84), Inches(3.8), LIGHT)
        rect(s, Inches(0.58), Inches(1.32), Inches(0.05), Inches(3.8), accent)
        big = len(lines) == 1 and len(lines[0]) < 210
        if big:
            txt(s, Inches(0.96), Inches(1.32), Inches(8.1), Inches(3.8),
                [[(lines[0], 15, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
        else:
            body = [[("•  " + l, 10.5 if len(lines) <= 6 else 9.5, INK, False)] for l in lines[:9]]
            txt(s, Inches(0.96), Inches(1.56), Inches(8.1), Inches(3.4), body, space=8)
        footer(s)

    def c_teach(title, kicker, points, example=None, tip=None, accent=BLUE):
        """The workhorse teaching slide: numbered key points, plus an optional
        worked example and exam tip. Dense but structured — never a one-liner."""
        s = slide(); head(s, title, kicker, accent)
        y = Inches(1.28)
        # ---- key points, each on its own accent-marked row
        n = len(points)
        rowh = Inches(0.5) if n <= 5 else Inches(0.42)
        size = 10 if n <= 5 else 9
        for i, p in enumerate(points[:6]):
            rect(s, Inches(0.58), y, Inches(8.84), rowh - Inches(0.05), LIGHT)
            rect(s, Inches(0.58), y, Inches(0.04), rowh - Inches(0.05), accent)
            oval(s, Inches(0.74), y + (rowh - Inches(0.31)) // 2, Inches(0.24), Inches(0.24), accent)
            txt(s, Inches(0.74), y + (rowh - Inches(0.28)) // 2, Inches(0.24), Inches(0.2),
                [[(str(i + 1), 7.5, WHITE, True)]], align=PP_ALIGN.CENTER)
            txt(s, Inches(1.08), y, Inches(8.2), rowh - Inches(0.05),
                [[(p, size, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
            y += rowh
        # ---- worked example + exam tip share the bottom band
        bot = Inches(5.12)
        if example and tip:
            w = Inches(4.34)
            _card(s, Inches(0.58), y + Inches(0.06), w, bot - y - Inches(0.1),
                  TEAL, example[0], example[1])
            _card(s, Inches(5.08), y + Inches(0.06), w, bot - y - Inches(0.1),
                  AMBER, "EXAM TIP", tip)
        elif example:
            _card(s, Inches(0.58), y + Inches(0.06), Inches(8.84), bot - y - Inches(0.1),
                  TEAL, example[0], example[1])
        elif tip:
            _card(s, Inches(0.58), y + Inches(0.06), Inches(8.84), bot - y - Inches(0.1),
                  AMBER, "EXAM TIP", tip)
        footer(s)

    def _card(s, x, y, w, h, color, label, body):
        if h < Inches(0.4):
            return
        rect(s, x, y, w, h, WHITE, line=LINE)
        rect(s, x, y, Inches(0.04), h, color)
        txt(s, x + Inches(0.16), y + Inches(0.05), w - Inches(0.28), Inches(0.2),
            [[(label.upper(), 7, color, True)]])
        txt(s, x + Inches(0.16), y + Inches(0.22), w - Inches(0.28), h - Inches(0.28),
            [[(body, 8.5, INK, False)]])

    def c_quiz(qtext, options, n):
        s = slide(); head(s, "Knowledge Check", f"QUIZ {n}", AMBER)
        rect(s, Inches(0.58), Inches(1.3), Inches(8.84), Inches(1.0), LIGHT)
        rect(s, Inches(0.58), Inches(1.3), Inches(0.05), Inches(1.0), AMBER)
        txt(s, Inches(0.94), Inches(1.3), Inches(8.2), Inches(1.0),
            [[(qtext, 12, INK, True)]], anchor=MSO_ANCHOR.MIDDLE)
        if options:
            cols = 2
            gapx, gapy = Inches(0.16), Inches(0.13)
            w = int((Inches(8.84) - gapx) / cols)
            rows = (len(options) + 1) // cols
            h = min(Inches(0.62), int((Inches(2.55) - gapy * (rows - 1)) / max(rows, 1)))
            for i, opt in enumerate(options[:6]):
                r, c = divmod(i, cols)
                x = Inches(0.58) + c * (w + gapx)
                y = Inches(2.48) + r * (h + gapy)
                rect(s, x, y, w, h, WHITE, line=LINE)
                oval(s, x + Inches(0.14), y + (h - Inches(0.26)) // 2,
                     Inches(0.26), Inches(0.26), BLUE)
                txt(s, x + Inches(0.14), y + (h - Inches(0.22)) // 2, Inches(0.26), Inches(0.22),
                    [[(chr(97 + i), 8, WHITE, True)]], align=PP_ALIGN.CENTER)
                txt(s, x + Inches(0.5), y, w - Inches(0.62), h,
                    [[(opt, 9.5, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
        footer(s)

    def c_activity(title, kicker, lines):
        s = slide(); head(s, title, kicker, TEAL)
        rect(s, Inches(0.58), Inches(1.3), Inches(8.84), Inches(3.85), LIGHT)
        rect(s, Inches(0.58), Inches(1.3), Inches(0.05), Inches(3.85), TEAL)
        body = []
        for i, l in enumerate(lines[:9], 1):
            body.append([(f"{i}.  ", 10, TEAL, True), (l, 10, INK, False)])
        txt(s, Inches(0.96), Inches(1.52), Inches(8.1), Inches(3.4), body, space=7)
        footer(s)

    # ---------------------------------------------------------- admin slides
    def a_cover():
        s = slide()
        rect(s, 0, 0, SW, SH, WHITE)
        rect(s, 0, 0, SW, Inches(0.16), BLUE)
        rect(s, 0, Inches(5.46), SW, Inches(0.16), TEAL)
        lg = os.path.join(ASSETS, "tertiary-infotech-logo.png")
        if os.path.exists(lg):
            s.shapes.add_picture(lg, Inches(0.6), Inches(0.48), height=Inches(0.74))
        rect(s, Inches(8.2), Inches(0.5), Inches(1.16), Inches(0.75), BLUE)
        txt(s, Inches(8.2), Inches(0.58), Inches(1.16), Inches(0.36),
            [[("ITIL 4", 13, WHITE, True)]], align=PP_ALIGN.CENTER)
        txt(s, Inches(8.2), Inches(0.93), Inches(1.16), Inches(0.28),
            [[("FOUNDATION", 6, WHITE, True)]], align=PP_ALIGN.CENTER)
        txt(s, Inches(0.63), Inches(1.68), Inches(9), Inches(0.36),
            [[("COURSE SLIDES  ·  WSQ", 11, BLUE, True)]])
        txt(s, Inches(0.63), Inches(2.06), Inches(9), Inches(1.3),
            [[(C.TITLE, 28, INK, True)]])
        rect(s, Inches(0.65), Inches(3.48), Inches(1.8), Inches(0.045), TEAL)
        txt(s, Inches(0.63), Inches(3.72), Inches(9), Inches(1.0),
            [[(f"WSQ Course Code: {C.COURSE_CODE}", 11, GREY, False)],
             [(f"Conducted by {C.ORG}  ·  UEN 201200696W", 9.5, GREY, False)]], space=4)
        txt(s, Inches(0.63), Inches(4.82), Inches(9), Inches(0.28),
            [[(f"Version {C.VERSION}  ·  {C.VERSION_DATE}", 8.5, GREY, False)]])
        txt(s, Inches(0.63), Inches(5.08), Inches(9), Inches(0.24),
            [[(f"© 2026 {C.ORG}. All rights reserved.  ·  www.tertiarycourses.com.sg",
               7, GREY, False)]])

    def a_process(title, kicker, steps, color=BLUE):
        s = slide(); head(s, title, kicker, color)
        n = len(steps); gap = Inches(0.1)
        w = int((Inches(8.84) - gap * (n - 1)) / n)
        x = Inches(0.58); y = Inches(1.75); h = Inches(1.65)
        for i, (t, d) in enumerate(steps):
            rect(s, x, y, w, h, LIGHT)
            rect(s, x, y, w, Inches(0.05), color)
            oval(s, x + int(w/2) - Inches(0.19), y + Inches(0.18), Inches(0.38), Inches(0.38), color)
            txt(s, x, y + Inches(0.23), w, Inches(0.3), [[(str(i+1), 11, WHITE, True)]],
                align=PP_ALIGN.CENTER)
            txt(s, x + Inches(0.05), y + Inches(0.68), w - Inches(0.1), Inches(0.4),
                [[(t, 9.5, INK, True)]], align=PP_ALIGN.CENTER)
            if d:
                txt(s, x + Inches(0.05), y + Inches(1.05), w - Inches(0.1), Inches(0.52),
                    [[(d, 7.5, GREY, False)]], align=PP_ALIGN.CENTER)
            if i < n - 1:
                txt(s, x + w, y + Inches(0.6), gap, Inches(0.3), [[("▶", 9, color, True)]],
                    align=PP_ALIGN.CENTER)
            x += w + gap
        footer(s)
        return s

    def a_trainer(named):
        s = slide()
        head(s, "About the Trainer", "YOUR TRAINER" + ("" if named else " · GENERAL"),
             BLUE if named else GREY)
        col = BLUE if named else GREY
        tp = C.TRAINER_PROFILE
        rect(s, Inches(0.58), Inches(1.3), Inches(2.5), Inches(3.85), LIGHT)
        rect(s, Inches(0.58), Inches(1.3), Inches(2.5), Inches(0.055), col)
        oval(s, Inches(1.42), Inches(1.72), Inches(0.82), Inches(0.82), col)
        txt(s, Inches(0.58), Inches(1.9), Inches(2.5), Inches(0.4),
            [[((tp["initials"] if named else "?"), 20, WHITE, True)]], align=PP_ALIGN.CENTER)
        txt(s, Inches(0.58), Inches(2.72), Inches(2.5), Inches(0.32),
            [[((C.TRAINER if named else "Your Trainer"), 13, INK, True)]], align=PP_ALIGN.CENTER)
        txt(s, Inches(0.68), Inches(3.08), Inches(2.3), Inches(0.6),
            [[("Principal Trainer" if named else "General Trainer template —", 8.5, GREY, False)],
             [(C.ORG if named else "to be completed by the trainer", 8, GREY, False)]],
            align=PP_ALIGN.CENTER)
        rows = ([("ROLE", tp["role"]), ("CERTIFICATION", tp["certification"]),
                 ("DELIVERS", tp["delivers"]), ("FOUNDER", tp["founder"])] if named
                else [("NAME", ""), ("TITLE / DESIGNATION", ""), ("QUALIFICATIONS", ""),
                      ("AREAS OF EXPERTISE", ""), ("EXPERIENCE", ""), ("CONTACT", "")])
        y = Inches(1.3)
        hh = Inches(0.92) if named else Inches(0.6)
        for i, (lab, val) in enumerate(rows):
            c2 = ACCENTS[i % 4] if named else GREY
            rect(s, Inches(3.24), y, Inches(6.18), hh - Inches(0.08), LIGHT)
            rect(s, Inches(3.24), y, Inches(0.045), hh - Inches(0.08), c2)
            txt(s, Inches(3.42), y + Inches(0.07), Inches(5.9), Inches(0.2),
                [[(lab, 7.5, c2, True)]])
            txt(s, Inches(3.42), y + Inches(0.26), Inches(5.9), hh - Inches(0.3),
                [[(val if val else "________________________________", 9, INK, False)]])
            y += hh
        footer(s)

    def a_tiles(title, kicker, items, accent=BLUE, cols=2):
        s = slide(); head(s, title, kicker, accent)
        n = len(items)
        rows = (n + cols - 1) // cols
        gapx, gapy = Inches(0.16), Inches(0.13)
        w = int((Inches(8.84) - gapx * (cols - 1)) / cols)
        h = min(Inches(1.15), int((Inches(3.8) - gapy * (rows - 1)) / max(rows, 1)))
        for i, it in enumerate(items):
            r, c = divmod(i, cols)
            x = Inches(0.58) + c * (w + gapx)
            y = Inches(1.32) + r * (h + gapy)
            col = ACCENTS[i % 4]
            rect(s, x, y, w, h, LIGHT)
            rect(s, x, y, Inches(0.045), h, col)
            if isinstance(it, tuple):
                txt(s, x + Inches(0.18), y + Inches(0.1), w - Inches(0.3), Inches(0.26),
                    [[(it[0], 11, INK, True)]])
                txt(s, x + Inches(0.18), y + Inches(0.38), w - Inches(0.3), h - Inches(0.46),
                    [[(it[1], 8.5, GREY, False)]])
            else:
                txt(s, x + Inches(0.18), y, w - Inches(0.3), h,
                    [[(it, 10, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
        footer(s)

    def a_thanks():
        s = slide()
        rect(s, 0, 0, SW, SH, WHITE)
        rect(s, 0, 0, Inches(0.21), SH, TEAL)
        rect(s, Inches(0.6), Inches(1.8), Inches(0.1), Inches(1.5), TEAL)
        txt(s, Inches(0.9), Inches(1.85), Inches(8.4), Inches(0.36),
            [[(C.CLOSING["kicker"], 11, TEAL, True)]])
        txt(s, Inches(0.9), Inches(2.2), Inches(8.4), Inches(0.9),
            [[(C.CLOSING["line1"], 30, INK, True)]])
        txt(s, Inches(0.92), Inches(3.16), Inches(8.2), Inches(0.7),
            [[(C.CLOSING["line2"], 10.5, GREY, False)]])

    # ================================================== FRONT ADMIN
    a_cover()
    a_process("Digital Attendance (Mandatory)", "TRAQOM · SSG DIGITAL ATTENDANCE",
              [("AM attendance", "start of each day"), ("PM attendance", "after lunch"),
               ("Assessment", "before the assessment"), ("75% minimum", "funding eligibility")])
    a_trainer(False)
    a_trainer(True)
    a_tiles("Let's Know Each Other", "ICE-BREAKER",
            [(str(i+1), t) for i, t in enumerate(C.ICE_BREAKER)], TEAL, cols=1)
    a_tiles("Ground Rules", "HOUSEKEEPING",
            [("Phones on silent", "Set your mobile phone to silent mode."),
             ("Participate", "No question is too small."),
             ("Mutual respect", "Agree to disagree."),
             ("One at a time", "One conversation at a time."),
             ("Be punctual", "Return from breaks on time."),
             ("75% attendance", "Required for funding.")])
    for d in sorted(C.DAY_THEMES):
        rows = [(f"{st}–{en}", tx) for st, en, m, k, tx in C.SCHEDULE[d][1]
                if k not in ("break", "lunch")]
        labs = {}
        try:
            from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
            from data_domain3 import DOMAIN3; from data_domain4 import DOMAIN4
            from data_domain5 import DOMAIN5
            for a in DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4+DOMAIN5:
                labs["{lab%d}" % a["num"]] = f"Lab {a['num']}: {a['title']}"
        except Exception:
            pass
        def fix(t):
            for k2, v in labs.items(): t = t.replace(k2, v)
            return (t[:96].rsplit(" ", 1)[0] + "…") if len(t) > 96 else t
        a_tiles(f"Lesson Plan — Day {d}", f"SCHEDULE  ·  {C.DAY_THEMES[d]}",
                [(tm, fix(tx)) for tm, tx in rows[:5]], BLUE, cols=1)
    a_tiles("Learning Outcomes", "WHAT YOU'LL ACHIEVE", C.OUTCOME_TILES, TEAL)
    # TSC
    s = slide(); head(s, "Skills Framework Alignment", "SKILLS FRAMEWORK · TSC", VIOLET)
    rect(s, Inches(0.58), Inches(1.3), Inches(8.84), Inches(0.5), LIGHT)
    rect(s, Inches(0.58), Inches(1.3), Inches(0.045), Inches(0.5), VIOLET)
    txt(s, Inches(0.78), Inches(1.38), Inches(8.4), Inches(0.3),
        [[(f"TSC: {C.TSC_TITLE}   ({C.TSC_CODE})", 11.5, INK, True)]])
    rect(s, Inches(0.58), Inches(1.92), Inches(4.3), Inches(3.2), LIGHT)
    rect(s, Inches(5.12), Inches(1.92), Inches(4.3), Inches(3.2), LIGHT)
    rect(s, Inches(0.58), Inches(1.92), Inches(4.3), Inches(0.05), BLUE)
    rect(s, Inches(5.12), Inches(1.92), Inches(4.3), Inches(0.05), TEAL)
    txt(s, Inches(0.78), Inches(2.04), Inches(3.9), Inches(0.26),
        [[("Knowledge (K1–K6)", 10.5, BLUE, True)]])
    txt(s, Inches(5.32), Inches(2.04), Inches(3.9), Inches(0.26),
        [[("Abilities (A1–A8)", 10.5, TEAL, True)]])
    txt(s, Inches(0.78), Inches(2.34), Inches(3.96), Inches(2.7),
        [[(k, 5.8, INK, False)] for k in C.TSC_KNOWLEDGE], space=3)
    txt(s, Inches(5.32), Inches(2.34), Inches(3.96), Inches(2.7),
        [[(a, 5.8, INK, False)] for a in C.TSC_ABILITIES], space=3)
    footer(s)
    a_tiles("Briefing for Assessment", "BEFORE YOU START",
            [("Phones away", "Under the table or on the floor."),
             ("No recording", "No photos of assessment scripts."),
             ("Work alone", "No discussion during the assessment."),
             ("Black or blue pen", "For hard-copy assessments."),
             ("No correction fluid", "Cross out neatly instead."),
             ("Pens down on time", "Scripts collected when time is up.")], AMBER)
    a_tiles("Assessment", "FINAL ASSESSMENT",
            [("Written Assessment (WA)", "Short-Answer Questions — 1 hour, open book."),
             ("Case Study (CS)", "Scenario-based analysis — 1 hour, open book."),
             ("Open book", "Slides, Learner Guide and approved materials only."),
             ("Eligibility", "75% attendance and assessed 'Competent'.")])
    a_process("Assessment Flow", "ON ASSESSMENT DAY",
              [("TRAQOM survey", "QR on the LMS"), ("Attendance", "scan the SSG QR"),
               ("Sit WA then CS", "open book"), ("Submit", "on the LMS"),
               ("Sign off", "Summary Record")])
    a_tiles("Criteria for Funding", "SSG FUNDING",
            [("Minimum 75% attendance", "Per the SSG Digital Attendance record."),
             ("Complete the assessment", "Both the WA and the Case Study."),
             ("Assessed 'Competent'", "Across every assessment criterion."),
             ("TRAQOM survey", "Complete the mandatory survey on the LMS.")], TEAL)
    a_process("Download Your Course Material", "COURSE PORTAL · LMS / TMS",
              [("Open the portal", "lms-tms.tertiaryinfotech.com"), ("Log in", "registered email"),
               ("My Courses", "open this course"), ("Download", "slides + Learner Guide"),
               ("Keep open", "open-book assessment")], TEAL)
    n_front = len(prs.slides)
    print(f"front admin: {n_front} slides")

    # ================================================== TEACHING (restyled)
    converted = {"image": 0, "image_text": 0, "tiles": 0, "compare": 0,
                 "statement": 0, "quiz": 0, "activity": 0, "section": 0, "skipped": 0}
    quiz_n = 0
    topic_now = 0

    for idx in range(TEACH_FROM, TEACH_TO + 1):
        s_src = src_slides[idx - 1]
        title, body, pics = extract(s_src)

        if idx in TOPIC_STARTS:
            topic_now = TOPIC_STARTS[idx]
            t = next(x for x in C.TOPICS if x["num"] == topic_now)
            c_section(topic_now, t["title"], t["subtitle"])
            converted["section"] += 1
            continue

        kicker = (f"TOPIC {topic_now:02d}" if topic_now else "ITIL 4 FOUNDATION")

        # --- enriched teaching slide: real ITIL content replaces a thin original
        if idx in ENRICH:
            e = ENRICH[idx]
            c_teach(e.get("title", title or "ITIL 4 Foundation"),
                    e.get("kicker", kicker), e["points"],
                    e.get("example"), e.get("tip"))
            converted["enriched"] = converted.get("enriched", 0) + 1
            continue

        if not title and not body and not pics:
            converted["skipped"] += 1
            continue
        # untitled v11 diagrams get a context-derived title, never a generic one
        title = title or DIAGRAM_TITLES.get(idx) or "ITIL 4 Foundation"

        # --- quiz
        if title.lower().startswith("quiz"):
            quiz_n += 1
            qtext, opts = "", []
            for b in body:
                if re.match(r"^[a-d][\.\)]\s", b) or re.match(r"^[a-d]\s{2,}", b):
                    opts.append(re.sub(r"^[a-d][\.\)]?\s+", "", b))
                elif not qtext:
                    qtext = re.sub(r"^\d+[\.\)]?\s*", "", b)
                else:
                    qtext += " " + b
            c_quiz(qtext or title, opts, quiz_n)
            converted["quiz"] += 1
            continue

        # --- activity
        if "case study" in title.lower() or "group activity" in title.lower():
            c_activity(title, "IN-CLASS ACTIVITY", body or [title])
            converted["activity"] += 1
            continue

        # --- image slides
        if pics:
            blob, ext, iw, ih = max(pics, key=lambda p: p[2] * p[3])
            if len(body) >= 3:
                c_image_text(title, kicker, blob, ext, iw, ih, body)
                converted["image_text"] += 1
            else:
                c_image(title, kicker, blob, ext, iw, ih,
                        caption=body[0] if body else None)
                converted["image"] += 1
            continue

        # --- two-concept comparison (e.g. "X vs Y")
        m = re.match(r"^(.+?)\s+vs\.?\s+(.+)$", title, re.I)
        if m and len(body) >= 4:
            lh, rh = m.group(1).strip(), m.group(2).strip()
            li = [b for b in body if b.lower().startswith(lh.lower()[:6])]
            split = body.index(li[-1]) if li else len(body) // 2
            left, right = body[:max(split, 1)], body[max(split, 1):]
            if left and right:
                c_compare(title, kicker, lh, left, rh, right)
                converted["compare"] += 1
                continue

        # --- long list -> tile grid
        if len(body) >= 5:
            c_tiles(title, kicker, body[:8])
            converted["tiles"] += 1
            continue

        # --- everything else -> statement card
        c_statement(title, kicker, body or [title])
        converted["statement"] += 1

    print("teaching converted:", ", ".join(f"{k}={v}" for k, v in converted.items() if v))

    # ================================================== BACK ADMIN
    a_tiles("What You Achieved", "LEARNING OUTCOMES", C.ACHIEVED_TILES, TEAL)
    a_tiles(C.NEXT_STEPS["title"], C.NEXT_STEPS["kicker"],
            [(str(i+1), b) for i, b in enumerate(C.NEXT_STEPS["bullets"])], BLUE, cols=1)
    s = slide(); head(s, "Practice Exam", "TEST YOURSELF", TEAL)
    rect(s, Inches(0.58), Inches(1.32), Inches(8.84), Inches(1.5), LIGHT)
    rect(s, Inches(0.58), Inches(1.32), Inches(0.05), Inches(1.5), TEAL)
    txt(s, Inches(0.96), Inches(1.32), Inches(8.1), Inches(1.5),
        [[("Sharpen your exam readiness with the Tertiary Infotech ITIL 4 Foundation "
           "practice exam. Attempt it under timed conditions and review every explanation.",
           12, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(0.58), Inches(3.1), Inches(8.84), Inches(0.4),
        [[("https://exams.tertiaryinfotech.com/", 13, BLUE, True)],
         [("practice-exams/axelos/axelos-itil4-foundation", 13, BLUE, True)]],
        align=PP_ALIGN.CENTER, space=2)
    footer(s)
    a_tiles("Recommended Next Courses", "CONTINUE YOUR JOURNEY",
            [("ITIL 4 Specialist", "Create, Deliver and Support."),
             ("ITIL 4 Specialist", "Drive Stakeholder Value."),
             ("ITIL 4 Strategist", "Direct, Plan and Improve."),
             ("COBIT / ISO 20000", "IT governance and service management.")], VIOLET)
    a_tiles("Support", "WE'RE HERE TO HELP",
            [("Email", "enquiry@tertiaryinfotech.com"),
             ("Website", "www.tertiarycourses.com.sg"),
             ("LMS / TMS", "lms-tms.tertiaryinfotech.com"),
             ("Practice exams", "exams.tertiaryinfotech.com")], VIOLET)
    a_tiles("Assessment", "WRAP-UP",
            [("Written Assessment (SAQ)", "1 hour, open book."),
             ("Case Study (CS)", "1 hour, open book."),
             ("Digital attendance", "Take the Assessment attendance (TRAQOM)."),
             ("Submit on the LMS", "lms-tms.tertiaryinfotech.com")])
    a_process("Assessment Flow", "ON ASSESSMENT DAY",
              [("TRAQOM survey", "QR on the LMS"), ("Attendance", "scan the SSG QR"),
               ("Sit WA then CS", "open book"), ("Submit", "on the LMS"),
               ("Sign off", "Summary Record")])
    a_process("Digital Attendance (Mandatory)", "TRAQOM · SSG DIGITAL ATTENDANCE",
              [("AM attendance", "start of each day"), ("PM attendance", "after lunch"),
               ("Assessment", "before the assessment"), ("75% minimum", "funding eligibility")])
    a_thanks()

    prs.save(OUT)
    print(f"\nSaved {OUT}  ({len(prs.slides)} slides, 100% house style)")
    return OUT


if __name__ == "__main__":
    main()
