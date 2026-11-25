"""Convierte láminas horizontales (16:9, ej. NotebookLM) a carrusel vertical 1080x1350.
Recorta piezas de cada lámina y las apila en vertical sobre el fondo de la misma lámina desenfocado.
Uso (desde la raíz del repo):
  pdftoppm -r 216 -png <archivo.pdf> <carpeta>/_paginas/hi
  python3 herramientas/pdf_a_carrusel.py <spec.json> <carpeta_salida>
spec: {"portada": ruta|null, "total": n, "laminas": [{"img": ruta, "piezas": [[x0,y0,x1,y1,ancho], ...], "extra": {...}}]}
Coordenadas en fracción (0-1) de la lámina; ancho = ancho final en px."""
import sys, os, json
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from marca import fuente, COBRIZO, BLANCO, LILA, VERDE, envolver

W, H = 1080, 1350
TOP, BOT, GAP = 120, 130, 34


def fondo(sl):
    k = H / sl.size[1]
    f = sl.resize((int(sl.size[0] * k), H), Image.LANCZOS)
    x = (f.size[0] - W) // 2
    f = f.crop((x, 0, x + W, H)).filter(ImageFilter.GaussianBlur(28))
    return ImageEnhance.Brightness(f).enhance(0.55)


def pie(d, n, total):
    d.text((W - 70, 60), f"{n}/{total}", font=fuente("SemiBold", 34), fill=COBRIZO, anchor="ra")
    d.rectangle((70, H - 78, 75, H - 46), fill=VERDE)
    d.text((92, H - 62), "Yami I. Nakamura", font=fuente("SemiBold", 28), fill=BLANCO, anchor="lm")
    d.text((W - 70, H - 62), "Avatar virtual con IA", font=fuente("MediumItalic", 24), fill=LILA, anchor="rm")


MAGENTA = (128, 30, 112)
NARANJA = (240, 110, 50)


def difuminar(p, borde=22):
    """Pega con bordes suaves para que no se vea el recorte rectangular."""
    m = Image.new("L", p.size, 0)
    ImageDraw.Draw(m).rectangle((borde // 2, borde // 2, p.size[0] - borde // 2, p.size[1] - borde // 2), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(borde / 2))
    out = p.convert("RGBA"); out.putalpha(m)
    return out


def caja_texto(s, ancho, tam=44, peso="Bold", color=BLANCO, fondo=None, borde=None, centrado=True, pad=34):
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    f = fuente(peso, tam)
    lineas = envolver(tmp, s, f, ancho - 2 * pad)
    lh = int(tam * 1.32)
    h = lh * len(lineas) + 2 * pad
    im = Image.new("RGBA", (ancho, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if fondo or borde:
        d.rounded_rectangle((0, 0, ancho - 1, h - 1), radius=22, fill=fondo, outline=borde, width=3 if borde else 0)
    y = pad
    for l in lineas:
        if centrado:
            d.text((ancho // 2, y), l, font=f, fill=color, anchor="ma")
        else:
            d.text((pad, y), l, font=f, fill=color)
        y += lh
    return im


def banner(sl, s, ancho, cara=None, etiqueta=None):
    sw, sh = sl.size
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    f = fuente("Bold", 38); fe = fuente("SemiBold", 24)
    x_txt = 190 if cara else 40
    lineas = envolver(tmp, s, f, ancho - x_txt - 36)
    h = max(170, 50 * len(lineas) + (40 if etiqueta else 0) + 60)
    im = Image.new("RGBA", (ancho, h + 30), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 30, ancho - 1, h + 29), radius=24, fill=MAGENTA + (245,), outline=(210, 90, 190), width=3)
    if cara:
        x0, y0, x1, y1 = cara
        c = sl.crop((int(x0 * sw), int(y0 * sh), int(x1 * sw), int(y1 * sh)))
        lado = 140
        c = c.resize((lado, lado), Image.LANCZOS)
        m = Image.new("L", (lado * 4, lado * 4), 0)
        ImageDraw.Draw(m).ellipse((0, 0, lado * 4 - 1, lado * 4 - 1), fill=255)
        m = m.resize((lado, lado), Image.LANCZOS)
        yc = 30 + (h - lado) // 2
        d.ellipse((24 - 4, yc - 4, 24 + lado + 3, yc + lado + 3), fill=(210, 90, 190))
        im.paste(c, (24, yc), m)
    y = 30 + (h - (50 * len(lineas) + (40 if etiqueta else 0))) // 2
    if etiqueta:
        d.text((x_txt, y), etiqueta, font=fe, fill=(255, 200, 150)); y += 40
    for l in lineas:
        d.text((x_txt, y), l, font=f, fill=BLANCO); y += 50
    return im


def pieza(sl, p):
    sw, sh = sl.size
    if isinstance(p, list):
        x0, y0, x1, y1, ancho = p
        c = sl.crop((int(x0 * sw), int(y0 * sh), int(x1 * sw), int(y1 * sh)))
        k = ancho / c.size[0]
        return difuminar(c.resize((ancho, int(c.size[1] * k)), Image.LANCZOS))
    t = p["tipo"]
    if t == "texto":
        return caja_texto(p["s"], p.get("ancho", 1000), p.get("tam", 44), p.get("peso", "Bold"),
                          tuple(p.get("color", BLANCO)), pad=p.get("pad", 10))
    if t == "caja":
        return caja_texto(p["s"], p.get("ancho", 1000), p.get("tam", 36), p.get("peso", "Medium"),
                          BLANCO, fondo=(20, 22, 34, 235), borde=(90, 95, 120))
    if t == "nota":
        return caja_texto(p["s"], p.get("ancho", 1000), p.get("tam", 30), "Medium",
                          (255, 225, 205), fondo=(30, 18, 24, 230), borde=NARANJA, centrado=False, pad=26)
    if t == "banner":
        return banner(sl, p["s"], p.get("ancho", 1000), p.get("cara"), p.get("etiqueta"))


def lamina(spec, n, total):
    sl = Image.open(spec["img"]).convert("RGB")
    piezas = [pieza(sl, p) for p in spec["piezas"]]
    gap = spec.get("gap", GAP)
    disp = H - TOP - BOT
    total_h = sum(p.size[1] for p in piezas) + gap * (len(piezas) - 1)
    if total_h > disp:
        k = disp / total_h
        piezas = [p.resize((int(p.size[0] * k), int(p.size[1] * k)), Image.LANCZOS) for p in piezas]
        total_h = sum(p.size[1] for p in piezas) + gap * (len(piezas) - 1)
    im = fondo(sl).convert("RGBA")
    y = TOP + (disp - total_h) // 2
    for p in piezas:
        im.alpha_composite(p, ((W - p.size[0]) // 2, y))
        y += p.size[1] + gap
    im = im.convert("RGB")
    pie(ImageDraw.Draw(im), n, total)
    return im


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    out = sys.argv[2]; os.makedirs(out, exist_ok=True)
    total = spec["total"]
    n = 1
    if spec.get("portada"):
        c = Image.open(spec["portada"]).convert("RGB")
        k = max(W / c.size[0], H / c.size[1])
        c = c.resize((round(c.size[0] * k), round(c.size[1] * k)), Image.LANCZOS)
        x, y = (c.size[0] - W) // 2, (c.size[1] - H) // 2
        c.crop((x, y, x + W, y + H)).save(f"{out}/01.jpg", quality=94)
        n = 2
    for s in spec["laminas"]:
        lamina(s, n, total).save(f"{out}/{n:02d}.jpg", quality=94)
        n += 1
    print("ok", n - 1)
