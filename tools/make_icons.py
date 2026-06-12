"""Draw the Almanac app icons — a midnight sky, gold sun, terrain ridges and radar arcs.

Renders at 4x and downsamples for clean edges. Writes assets/icon-512.png,
assets/icon-192.png and assets/icon-180.png (apple-touch-icon).
"""
from PIL import Image, ImageDraw
import os

S = 2048  # working canvas (4x the 512 target)


def rounded_mask(size, radius):
    m = Image.new('L', (size, size), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    return m


img = Image.new('RGB', (S, S), '#0b0d10')
d = ImageDraw.Draw(img)

# vertical sky wash: deep navy down to a teal-dark horizon
for y in range(S):
    t = y / S
    r = int(11 + (15 - 11) * t)
    g = int(13 + (34 - 13) * t)
    b = int(16 + (38 - 16) * t)
    d.line([(0, y), (S, y)], fill=(r, g, b))

# the sun — warm gold disc, upper left
sun_c, sun_r = (S * 0.32, S * 0.30), S * 0.155
d.ellipse([sun_c[0] - sun_r * 1.45, sun_c[1] - sun_r * 1.45,
           sun_c[0] + sun_r * 1.45, sun_c[1] + sun_r * 1.45], fill=(57, 48, 24))
d.ellipse([sun_c[0] - sun_r, sun_c[1] - sun_r,
           sun_c[0] + sun_r, sun_c[1] + sun_r], fill=(232, 192, 116))

# radar sweep — three sky-blue arcs from the lower right
rc = (S * 0.78, S * 0.74)
for i, (rad, w, col) in enumerate([
        (S * 0.50, int(S * 0.030), (56, 189, 248)),
        (S * 0.38, int(S * 0.030), (74, 200, 250)),
        (S * 0.26, int(S * 0.030), (110, 215, 252))]):
    d.arc([rc[0] - rad, rc[1] - rad, rc[0] + rad, rc[1] + rad],
          start=150, end=285, fill=col, width=w)
d.ellipse([rc[0] - S * 0.035, rc[1] - S * 0.035,
           rc[0] + S * 0.035, rc[1] + S * 0.035], fill=(52, 211, 153))

# terrain — two ridge lines across the foot
d.polygon([(0, S * 0.86), (S * 0.22, S * 0.66), (S * 0.40, S * 0.80),
           (S * 0.60, S * 0.62), (S * 0.80, S * 0.78), (S, S * 0.70),
           (S, S), (0, S)], fill=(16, 42, 40))
d.polygon([(0, S * 0.95), (S * 0.18, S * 0.80), (S * 0.38, S * 0.90),
           (S * 0.58, S * 0.76), (S * 0.78, S * 0.88), (S, S * 0.82),
           (S, S), (0, S)], fill=(19, 58, 50))

out = os.path.join(os.path.dirname(__file__), '..', 'assets')
os.makedirs(out, exist_ok=True)
for size, name, rad in [(512, 'icon-512.png', 0.18), (192, 'icon-192.png', 0.18),
                        (180, 'icon-180.png', 0.0)]:
    im = img.resize((size, size), Image.LANCZOS)
    if rad:
        im = im.convert('RGBA')
        im.putalpha(rounded_mask(size, int(size * rad)))
    im.save(os.path.join(out, name))
    print('wrote', name)
