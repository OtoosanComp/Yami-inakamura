"""Recorta las expresiones seguras de la hoja de stickers (sin cuchillo ni libro con sangre).
Uso: python3 stickers.py <hoja_stickers.png> <carpeta_salida>"""
import sys, os
from PIL import Image
im = Image.open(sys.argv[1]).convert("RGB")
out = sys.argv[2]; os.makedirs(out, exist_ok=True)
W, H = im.size; cw, ch = W / 4, H / 3
nombres = [
    ["senala_guino", "pensando_mano", "risa", "sorpresa"],
    ["puchero", "enojada", None, "corazones"],      # None = cuchillo con sangre (NO usar)
    ["secreto_duda", "llorando", None, "gatita"],   # None = libro con sangre (NO usar)
]
for r in range(3):
    for c in range(4):
        n = nombres[r][c]
        if not n:
            continue
        box = (int(c * cw) + 6, int(r * ch) + 6, int((c + 1) * cw) - 6, int((r + 1) * ch) - 6)
        im.crop(box).resize((768, 670), Image.LANCZOS).save(f"{out}/{n}.jpg", quality=92)
print("ok")
