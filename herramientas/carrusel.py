"""Genera carruseles 1080x1350 (IG/FB) desde un JSON.
Uso: python3 carrusel.py <hoja_expresiones.png> <carrusel.json> <carpeta_salida>
Tipos de lamina: portada, texto, cierre, frase. Campo "yami": risa|pensando|sorpresa|puchero|sonrisa|neutral."""
import sys, os, json
from PIL import Image, ImageDraw
from marca import *

PANELES = {  # recortes de la hoja de expresiones (1536x1024)
    "neutral": (0, 0, 535, 830),
    "risa": (540, 4, 860, 508),
    "pensando": (868, 4, 1192, 508),
    "sorpresa": (588, 518, 876, 1020),
    "puchero": (884, 518, 1202, 1020),
    "sonrisa": (1210, 518, 1532, 1020),
}
W, H = 1080, 1350


def yami(hoja, nombre, alto):
    p = hoja.crop(PANELES[nombre])
    k = alto / p.size[1]
    p = p.resize((int(p.size[0] * k), alto), Image.LANCZOS)
    return recorte_alfa(p, fundido_abajo=int(alto * 0.28), fundido_lados=int(p.size[0] * 0.12))


def base(num, total, etiqueta):
    im = degradado(W, H, cx=0.5, cy=0.3, radio=1.1).convert("RGBA")
    d = ImageDraw.Draw(im)
    d.text((80, 80), etiqueta, font=fuente("Bold", 28), fill=VERDE)
    d.text((W - 80, 80), f"{num}/{total}", font=fuente("SemiBold", 28), fill=LILA, anchor="ra")
    d.rectangle((80, H - 92, 150, H - 88), fill=COBRIZO)
    d.text((80, H - 70), "Yami I. Nakamura", font=fuente("SemiBold", 26), fill=BLANCO)
    d.text((W - 80, H - 70), "Avatar virtual con IA", font=fuente("Medium", 22), fill=LILA, anchor="ra")
    return im


def bloque(d, x, y, s, f, color, ancho, interlineado=1.3):
    for l in envolver(d, s, f, ancho):
        texto(d, (x, y), l, f, color)
        y += int(f.size * interlineado)
    return y


def lamina(hoja, sl, num, total, etiqueta):
    im = base(num, total, etiqueta)
    t = sl["tipo"]
    if sl.get("yami"):
        alto = 760 if t in ("portada", "cierre", "frase") else 520
        y_img = yami(hoja, sl["yami"], alto)
        x = (W - y_img.size[0]) // 2 if t != "texto" else W - y_img.size[0] - 20
        im.alpha_composite(y_img, (x, H - alto - 110))
    d = ImageDraw.Draw(im)
    if t == "portada":
        y = bloque(d, 80, 170, sl["titulo"], fuente("ExtraBold", 72), BLANCO, 920, 1.15)
        if sl.get("sub"):
            bloque(d, 80, y + 20, sl["sub"], fuente("MediumItalic", 36), LILA, 920)
    elif t == "texto":
        y = bloque(d, 80, 190, sl["titulo"], fuente("Bold", 58), COBRIZO, 920, 1.15)
        d.rectangle((80, y + 18, 180, y + 22), fill=VERDE)
        bloque(d, 80, y + 60, sl["cuerpo"], fuente("Medium", 40), BLANCO, 900, 1.4)
    elif t in ("cierre", "frase"):
        y = bloque(d, 80, 180, sl["titulo"], fuente("ExtraBold", 66 if t == "cierre" else 58), BLANCO, 920, 1.15)
        if sl.get("cuerpo"):
            bloque(d, 80, y + 24, sl["cuerpo"], fuente("Medium", 34), LILA, 920, 1.35)
    if sl.get("nota"):
        f = fuente("Medium", 22)
        d.text((W // 2, H - 135), sl["nota"], font=f, fill=(200, 190, 210), anchor="ma")
    return im.convert("RGB")


if __name__ == "__main__":
    hoja = Image.open(sys.argv[1]).convert("RGB")
    spec = json.load(open(sys.argv[2], encoding="utf-8"))
    out = sys.argv[3]; os.makedirs(out, exist_ok=True)
    total = len(spec["laminas"])
    for i, sl in enumerate(spec["laminas"], 1):
        lamina(hoja, sl, i, total, spec["etiqueta"]).save(f"{out}/{i:02d}.jpg", quality=93)
    print("ok", total)
