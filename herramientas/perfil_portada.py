"""Genera foto de perfil y portada de Facebook.
Uso: python3 perfil_portada.py <hoja_expresiones.png> <carpeta_assets>"""
import sys, os
from PIL import Image, ImageDraw, ImageFilter
from marca import *

hoja = Image.open(sys.argv[1]).convert("RGB")
dst = sys.argv[2]
os.makedirs(f"{dst}/perfil", exist_ok=True); os.makedirs(f"{dst}/portada", exist_ok=True)

# --- Foto de perfil 1080x1080 ---
cara = hoja.crop((82, 40, 532, 490)).resize((1080, 1080), Image.LANCZOS)
cara = cara.filter(ImageFilter.UnsharpMask(2, 60, 2))
fondo = degradado(1080, 1080, cy=0.35, radio=0.8)
fondo.paste(recorte_alfa(cara), (0, 0), recorte_alfa(cara))
fondo.save(f"{dst}/perfil/yami_perfil.jpg", quality=95)

# --- Portada Facebook 1640x624 (zona segura central ~1100 px) ---
W, H = 1640, 624
lienzo = degradado(W, H, cx=0.62, cy=0.45, radio=1.6).convert("RGBA")
d = ImageDraw.Draw(lienzo)
# lineas finas de acento

cuerpo = hoja.crop((0, 0, 535, 830))
k = 660 / 830
torso = [(120, 640), (170, 530), (250, 470), (420, 470), (535, 520), (535, 830), (60, 830)]
cuerpo = cuerpo.resize((int(535 * k), 660), Image.LANCZOS)
cut = recorte_alfa(cuerpo, proteger=[(x * k, y * k) for x, y in torso], fundido_abajo=170, fundido_lados=70)
# brillo morado detras
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse((960, 60, 1420, 560), fill=(150, 70, 190, 110))
glow = glow.filter(ImageFilter.GaussianBlur(70))
lienzo = Image.alpha_composite(lienzo, glow)
lienzo.alpha_composite(cut, (985, 0))
d = ImageDraw.Draw(lienzo)

x0 = 285
texto(d, (x0, 160), "Yami I. Nakamura", fuente("Bold", 70), BLANCO)
texto(d, (x0 + 4, 248), "やみ・なかむら", fuente("cjk", 34), LILA)
d.rectangle((x0 + 4, 305, x0 + 124, 309), fill=COBRIZO)
texto(d, (x0 + 4, 330), "PSICOLOGÍA OSCURA · ANIME · TRUE CRIME", fuente("SemiBold", 28), VERDE)
texto(d, (x0 + 4, 385), "No tengas miedo... yo te explico por qué pasó.", fuente("MediumItalic", 30), BLANCO)
# etiqueta IA
f = fuente("SemiBold", 20)
s = "AVATAR VIRTUAL CON IA"
w = d.textlength(s, font=f)
d.rounded_rectangle((x0 + 4, 450, x0 + 4 + w + 32, 488), radius=19, outline=LILA, width=2)
d.text((x0 + 20, 469), s, font=f, fill=LILA, anchor="lm")
lienzo.convert("RGB").save(f"{dst}/portada/yami_portada_facebook.jpg", quality=95)
print("ok")
