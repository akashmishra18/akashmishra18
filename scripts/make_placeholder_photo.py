"""
Temporary stand-in for your photo so the ASCII panel works from day one.
Draws a big "</>" mark on white. Replace it later with your real portrait:

    python scripts/prep_photo.py my-photo.jpg   # writes source-prepped.png
    python scripts/make_ascii_svg.py            # writes akash-ascii.svg
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "source-prepped.png")
S = 1200
im = Image.new("L", (S, S), 255)
d = ImageDraw.Draw(im)
bold = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
big = ImageFont.truetype(bold, 520)
small = ImageFont.truetype(bold, 150)
txt = "</>"
w = d.textlength(txt, font=big)
d.text(((S - w) / 2, 250), txt, font=big, fill=40)
name = "AKASH"
w2 = d.textlength(name, font=small)
d.text(((S - w2) / 2, 850), name, font=small, fill=90)
im.save(OUT)
print("wrote", OUT)
