# Yami I. Nakamura · Redes — La biblia

> **Este archivo es nuestra biblia.** Lo seguimos, pero no es ley fija: se cambia cuando los resultados digan
> qué funciona y qué no. Cada cambio se anota al final en "Cambios a la biblia".

## Qué es este repo
Repo y chat **exclusivos para las redes de Yami I. Nakamura**: llevar la página de Facebook y el Instagram,
**comparar resultados y decirle al usuario qué subir**: calendario, textos, imágenes y seguimiento.
**Aquí NO se producen videos.** Los videos se hacen en otro repo (`OtoosanComp/INakamura`, rama `proyecto-meta`),
y el usuario reporta aquí lo que sube (ver `publicaciones.md`).

**Claude es el orquestador:** decide qué sigue, reparte el trabajo (modelos abajo), deja todo listo para publicar
y empuja hacia la meta. El usuario publica y reporta.

### Meta del proyecto
1. Cuentas creadas, vinculadas y seguras.
2. 30 días de constancia publicando (Reels + publicaciones de apoyo).
3. Pedir **Content Monetization** de Facebook en cuanto el Panel profesional lo permita.

## El usuario
- Trabaja **solo desde el teléfono**, sin PC. Escribe en español de México.
- Entrega todo como archivos que pueda abrir en el teléfono (imágenes, .md, .txt).
- Antes de hacer algo grande: decir qué hay y qué se necesita, luego actuar.

## Uso de modelos
- **Modelo principal:** estrategia, decisiones, revisión final, textos importantes (bio, publicaciones fijadas).
- **Sonnet (subagentes):** investigación (políticas de Meta, tendencias, horarios), redactar descripciones, carruseles y calendarios.
- **Haiku (subagentes):** lo simple: hashtags, pasar reportes a la tabla, actualizar el estado, revisar listas.

## Quién es Yami (canon resumido)
- **Yami I. Nakamura** (やみ・なかむら). La **I. es de Ibarra** (Yami Ibarra Nakamura).
  **En público siempre "Yami I. Nakamura"**; el nombre completo es solo de uso interno.
- **Avatar virtual con IA**, no es persona real (siempre visible en la bio).
- 21 años, 1.49 m, madre japonesa y padre mexicano. Cosplayer. Gemela de **Tsuki** (cabello corto lila).
- Aspecto anime "Mystery & Mind": cabello largo rojo cobrizo con moño negro, ojos verdes, pecas, choker,
  chamarra negra con detalles morados. **Paleta:** cobrizo, verde, negro, morado.
- Tema: **psicología oscura + anime + true crime**, con miedo suave y sin morbo. Explica la mente, no se burla de víctimas.
- Frase: *"No tengas miedo... yo te explico por qué pasó."* · Cierre: *"¿Tú qué hubieras hecho?"*
- **Nada de "uwu"** ni muletillas de ese estilo.

## Estructura de cuentas (decidido)
| Plataforma | Dónde | Notas |
|---|---|---|
| Facebook | **Página** "Yami I. Nakamura", categoría Creador digital | Se administra desde el perfil personal real del usuario. **Nunca crear un perfil personal falso para Yami** (Meta lo prohíbe y lo cierra). |
| Instagram | Cuenta propia de Yami, **profesional → Creador** | Vinculada a la página de Facebook para programar desde Meta Business Suite. |
| YouTube | Canal **Otoosan Tales** (ya existe) | Video largo del domingo. Se enlaza desde la bio de Yami. |
| TikTok | **Otoosan Tales** (ya existe) | Se enlaza desde la bio de Yami. |

## Lineamientos para no desmonetizar
**[Meta]** = regla o riesgo real de Meta · **[Nuestra]** = costumbre de la casa (se ajusta según resultados).

1. **[Meta]** Etiqueta de IA ("Información de IA") activada en cada publicación con Yami: Reels, carruseles e imágenes.
2. **[Nuestra]** En la descripción: "Contenido educativo y de divulgación, sin material gráfico." y "Avatar virtual con IA."
   Si salen portadas de anime: "Portadas © de sus respectivos autores."
3. **[Meta]** Nada de "engagement bait": no pedir "comenta SÍ", "etiqueta a un amigo", "comparte si…", "mira hasta el final".
   Preguntas abiertas de verdad sí están bien ("¿Tú qué hubieras hecho?").
4. **[Nuestra]** Máximo 3 hashtags y sin enlaces en los Reels.
5. **[Meta]** Nada de sangre, armas ni fotos reales de crímenes. Sin nombres completos de víctimas. Sin tomas sugerentes de Yami.
6. **[Meta]** Sin clips ni capturas de anime (solo la portada oficial, chica y breve).
7. **[Meta]** Música: solo la biblioteca de Meta o música libre con licencia. Música con derechos = video silenciado o sin monetización.
8. **[Nuestra]** Reels de 10 a 60 s.
9. **[Meta]** Content Monetization de Facebook es **por invitación**: se pide desde el Panel profesional.
10. **Voz:** Claude **no pone voz**. Entrega el guion en `.txt` y el usuario genera la voz en **CapCut**.
    Antes de monetizar, revisar que la voz elegida en CapCut permita uso comercial.
11. Las políticas cambian: si algo es decisivo, verificar la página oficial de Meta.

## Tipos de publicación (para traer visibilidad además de los Reels)
| Formato | Para qué | Plataforma |
|---|---|---|
| **Reel** | Alcance a gente nueva (lo principal). | FB + IG |
| **Carrusel "Expediente"** (5–7 imágenes) | Explicar un concepto psicológico o un personaje. Se guarda y se comparte solo. | IG + FB |
| **Imagen con frase** | Frase de Yami o dato corto. Rápida de consumir. | FB + IG |
| **Pregunta de texto** | Conversación en comentarios (Facebook premia los comentarios). | FB |
| **Historias** | Encuestas, "¿quién tiene la culpa?", adelanto del siguiente video, compartir el Reel nuevo. | IG + FB |
| **Publicación fijada** | Presentación de Yami: quién es, de qué habla, que es IA. | FB + IG |

**Imágenes de escenas (Yami/Tsuki): las genera ChatGPT** con los prompts de `contenido/prompts-chatgpt.txt`; Claude las revisa y les pone texto.
Claude produce las imágenes (carruseles, frases, perfil, portada) en `assets/` a partir de las fotos de Yami,
con los scripts de `herramientas/`. Los textos de cada pieza van en `contenido/`.

## Fotos de Yami: cuáles sirven
| Foto | ¿Para redes? | Motivo |
|---|---|---|
| Hoja de expresiones (uniforme, fondo gris) | ✅ Sí, la base de todo | Limpia, sin pose sugerente. De aquí salen perfil, portada y carruseles. |
| Hoja de stickers (12 caritas) | ✅ Sí, **menos 2** | El **cuchillo con sangre** y el **libro "School Days" manchado** rompen la regla de sangre/armas. Recortadas y separadas en `assets/stickers/`. |
| Telas aéreas (gimnasio) | ⚠️ Solo historias, con cuidado | Es deporte, pero mucha piel; mejor no en publicaciones con monetización. |
| Selfie con arnés negro/morado | ❌ No | Ligas, lengua de fuera: Meta lo toma como sugerente. |
| Selfie con Tsuki (baño rosa) | ❌ No así | La pose de Yami es sugerente. **Tsuki sí queda bien**: pedir otra toma juntas sin esa pose. |
| Selfie uniforme corto (escote) | ❌ No | Sugerente. |
| Cosplay marinero rojo | ❌ No | Falda muy corta + lengua; además es traje de una franquicia conocida. |
Para la estética de la biblia sirven mejor: chamarra negra con morado, ropa normal, poses de "pensar/explicar".

## Calendario interno (nunca se anuncia en los videos; si un día no se puede, no pasa nada)
- **Reels:** lunes, miércoles y viernes · **dos Reels distintos por día**, 1:00 pm y 8:00 pm (CDMX).
  Cada Reel va **igual a Facebook e Instagram** a la misma hora. (6 Reels por semana.)
- **Apoyo:** martes carrusel · jueves frase o pregunta · sábado historia/encuesta.
- **Largo:** domingo 7:00 pm (CDMX) en YouTube (Otoosan Tales).
- **Cuenta nueva:** la primera semana se publica poco (1–2 cosas) para que Meta no la restrinja.
- Detalle de fechas en `calendario.md`.

## Comentarios delicados (cómo responde Yami)
- **Casos reales con víctimas:** Yami habla del comportamiento y la mente, nunca de detalles gráficos ni da nombres completos.
- **Alguien cuenta que sufre abuso, violencia o acoso:** respuesta breve y amable, sin hacer diagnóstico; sugerir buscar ayuda
  (en México **911** en emergencia).
- **Autolesión o ideas suicidas:** no bromear ni seguir el tema en público. Responder con cariño y dejar la
  **Línea de la Vida 800 911 2000** (México, 24 h). Si es grave, reportar desde la app.
- **Odio, burla de víctimas, morbo o spam:** ocultar el comentario (no discutir). Si se repite, restringir o bloquear.
- **"¿Eres real?":** siempre honesta: "Soy un avatar virtual hecho con IA."
- Yami no da consejos médicos ni psicológicos personales: divulga, no da terapia.

## Lo que Claude NO puede hacer
- Crear cuentas, publicar ni programar (no hay conexión con Meta). El usuario publica; Claude lo guía y deja todo listo.
- Ver estadísticas: el usuario manda capturas o números (reporte en `publicaciones.md`).
- Ver el repo de videos (`INakamura`) salvo que el usuario dé permiso de conectarlo en modo lectura.
- Poner voz: entrega guion en `.txt`; la voz la hace el usuario en CapCut.

## Pasos de arranque (checklist)
- [ ] 1. Gmail exclusivo para Yami + verificación en dos pasos.
- [ ] 2. Página de Facebook "Yami I. Nakamura" (Creador digital) + bio + foto + portada.
- [ ] 3. Instagram nuevo con el correo de Yami → profesional → Creador + bio + foto.
- [ ] 4. Vincular Instagram con la página (Centro de cuentas) y probar Meta Business Suite.
- [ ] 5. Verificación en dos pasos en Facebook e Instagram.
- [ ] 6. Enlaces a YouTube y TikTok de Otoosan Tales en ambas bios.
- [ ] 7. Primera publicación: presentación de Yami (p0, ya producida en el otro repo) y fijarla.
- [ ] 8. Pedir Content Monetization cuando el Panel profesional lo permita (antes: voz con plan de pago).

Guía paso a paso en `guia-arranque.md`.

## Bios
**Instagram** (máx. 150 caracteres; esta tiene 129):
```
Yami I. Nakamura 🌙 Avatar virtual con IA
Psicología oscura · anime · true crime 🇲🇽
No tengas miedo... yo te explico por qué pasó.
```
**Facebook** (presentación de la página, máx. 101 caracteres; esta tiene 90):
```
Avatar virtual con IA 🌙 Psicología oscura, anime y true crime. Yo te explico por qué pasó.
```

## Archivos del repo
- `CLAUDE.md`: este archivo. La sección "Estado" se actualiza al final de cada sesión.
- `cuentas.md`: datos de las cuentas (**sin contraseñas ni códigos**).
- `guia-arranque.md`: pasos para crear todo desde el teléfono.
- `publicaciones.md`: tabla con todo lo subido + plantilla de reporte.
- `calendario.md`: próximas dos semanas + banco de ideas.
- `plan-contenido.md`: semana tipo de publicaciones normales (Expediente, Gemelas, Vida de Yami, Dato oscuro) y flujo con ChatGPT.
- `assets/`: perfil, portada, stickers y carruseles listos para subir. (`assets/fotos/` = originales; **no se suben mientras el repo sea público**.)
- `contenido/`: textos de cada pieza (descripciones, guiones en .txt, datos de los carruseles).
- `herramientas/`: scripts de Claude para generar imágenes con la marca (`marca.py`, `perfil_portada.py`, `carrusel.py`, `stickers.py`).

---

## Estado (actualizado 25-nov-2026)
- **Cuentas:** ninguna creada todavía. El usuario va a empezar con el paso 1.
- **Listo para subir:** foto de perfil, portada de Facebook, 10 stickers para historias, carrusel #01 (yandere) con su texto.
- **Videos listos (otro repo):** p0 presentación (41 s), r1 Kotonoha "no nació yandere" (55 s), r4 yandere más popular (48 s).
- **En proceso (otro repo):** r2 Nice boat, r3 Kotonoha vs Yuno; esquema del primer largo (Kotonoha).
- **Ideas de video:** yanderes de la vieja escuela, ¿Mikasa es yandere?, Makoto el verdadero villano de School Days.
- **Ojo producción:** con 6 Reels por semana, para la semana del 7-dic faltan 3 Reels nuevos (ver `calendario.md`).
- **⚠️ El repo es PÚBLICO:** pedir al usuario que lo haga privado antes de subir fotos originales o datos de cuentas.
- **Pendiente del usuario:** hacer privado el repo, crear cuentas, elegir usuario de Instagram, enlaces de YouTube/TikTok, foto de Tsuki sin pose sugerente.
- **Siguiente paso de Claude:** texto de p0 y r1, guiones en .txt para los Reels que falten, imagen con frase del jueves.

## Cambios a la biblia
| Fecha | Cambio | Por qué |
|---|---|---|
| 25-nov-2026 | Reels: 2 distintos por día (L/M/V, 1 pm y 8 pm), el mismo en FB e IG. | Decisión del usuario. |
| 25-nov-2026 | Claude no pone voz: guion en .txt → voz en CapCut. Se quita ElevenLabs. | Decisión del usuario. |
| 25-nov-2026 | Semana tipo de publicaciones normales; ChatGPT genera las escenas de las gemelas. | Más visibilidad entre Reels. |
| 25-nov-2026 | Las reglas pasan a "lineamientos": se ajustan según resultados. | La biblia se adapta a lo que funcione. |
