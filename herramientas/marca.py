"""Utilidades de marca de Yami I. Nakamura (colores, fuentes, recortes).
Requiere: pillow, numpy, scipy; fuentes Montserrat y Noto Sans CJK
(apt-get install fonts-montserrat fonts-noto-cjk)."""
import numpy as np
from scipy import ndimage
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Paleta
NEGRO = (14, 10, 18)
MORADO = (92, 40, 120)
MORADO_OSC = (34, 14, 48)
COBRIZO = (204, 96, 52)
VERDE = (168, 198, 74)
LILA = (190, 160, 225)
BLANCO = (245, 240, 248)

M = "/usr/share/fonts/opentype/montserrat/Montserrat-"
CJK = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"


def fuente(peso, tam):
    if peso == "cjk":
        return ImageFont.truetype(CJK, tam, index=0)
    return ImageFont.truetype(f"{M}{peso}.otf", tam)


def degradado(w, h, cx=0.5, cy=0.4, radio=0.9, centro=MORADO, borde=NEGRO):
    y = np.linspace(0, 1, h)[:, None]
    x = np.linspace(0, 1, w)[None, :] * (w / h)
    r = np.sqrt((x - cx * w / h) ** 2 + (y - cy) ** 2)
    t = np.clip(r / radio, 0, 1)[..., None]
    a = np.array(centro, float) * (1 - t) + np.array(borde, float) * t
    return Image.fromarray(a.astype("uint8"))


def recorte_alfa(img, proteger=None, fundido_abajo=0, fundido_lados=0):
    """Devuelve RGBA quitando el fondo gris liso conectado al borde.
    proteger: poligono [(x,y),...] que siempre queda opaco (ej. camisa blanca).
    fundido_abajo: px de desvanecido en la parte inferior."""
    a = np.asarray(img.convert("RGB")).astype(float)
    mx = a.max(2); mn = a.min(2); sat = (mx - mn) / (mx + 1e-6)
    suelto = (sat < 0.20) & (mx > 110)
    lab, _ = ndimage.label(suelto)
    borde = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    reg = ndimage.binary_dilation(np.isin(lab, list(borde)), iterations=6)
    suave = np.clip((0.22 - sat) / 0.12, 0, 1) * np.clip((mx - 110) / 50, 0, 1)
    fondo = ndimage.gaussian_filter(suave * reg, 1.2)
    alfa = (1 - fondo) * 255
    if proteger:
        pm = Image.new("L", img.size, 0)
        ImageDraw.Draw(pm).polygon(proteger, fill=255)
        pm = np.asarray(pm.filter(ImageFilter.GaussianBlur(2))).astype(float)
        alfa = np.maximum(alfa, pm)
    if fundido_abajo:
        h = img.size[1]
        rampa = np.clip((h - np.arange(h)) / fundido_abajo, 0, 1)[:, None]
        alfa = alfa * rampa
    if fundido_lados:
        w = img.size[0]; xs = np.arange(w)
        rampa = np.clip(np.minimum(xs, w - 1 - xs) / fundido_lados, 0, 1)[None, :]
        alfa = alfa * rampa
    out = img.convert("RGBA")
    out.putalpha(Image.fromarray(alfa.astype("uint8")))
    return out


def texto(d, xy, s, f, color, ancla="la", sombra=True):
    if sombra:
        x, y = xy
        d.text((x + 2, y + 3), s, font=f, fill=(0, 0, 0, 160), anchor=ancla)
    d.text(xy, s, font=f, fill=color, anchor=ancla)


def envolver(d, s, f, ancho):
    palabras, lineas, actual = s.split(), [], ""
    for p in palabras:
        prueba = (actual + " " + p).strip()
        if d.textlength(prueba, font=f) <= ancho:
            actual = prueba
        else:
            lineas.append(actual); actual = p
    if actual:
        lineas.append(actual)
    return lineas
