# -*- coding: utf-8 -*-
"""Produit les vignettes web des captures de canvas.

Les PNG pleine resolution rendus par Grasshopper pesent une dizaine de Mo au
total et rendent l'application lourde a parcourir. On en tire des JPEG de
1500 px de large, servis dans les fiches, le PNG restant accessible par le lien
« pleine resolution ».

Ce script existe parce que ces vignettes avaient ete fabriquees a la main lors
d'une session precedente : la chaine n'etait donc pas reproductible, et rien ne
signalait qu'elles etaient perimees apres une regeneration des PNG.
"""
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PROJET = os.path.abspath(os.path.join(ICI, "..", ".."))
LOTS = [os.path.join(PROJET, "EXERCICES", "LOT A - Composants natifs"),
        os.path.join(PROJET, "EXERCICES",
                     "LOT IA - IA et assistance generative")]
LOT = LOTS[0]

LARGEUR = 1500
QUALITE = 82


def main():
    try:
        from PIL import Image
    except ImportError:
        print("Pillow absent : vignettes impossibles.")
        return 1

    dossiers = []
    for _lot in LOTS:
        if os.path.isdir(_lot):
            dossiers += [os.path.join(_lot, _d) for _d in sorted(os.listdir(_lot))]
    if not dossiers:
        print("Aucun dossier d'exercice trouve.")
        return 1

    faits, inchanges, echecs = 0, 0, []
    for base in dossiers:
        ill = os.path.join(base, "Illustrations")
        if not os.path.isdir(ill):
            continue
        web = os.path.join(ill, "web")
        if not os.path.isdir(web):
            os.makedirs(web)

        for f in sorted(os.listdir(ill)):
            if not f.lower().endswith(".png"):
                continue
            src = os.path.join(ill, f)
            dst = os.path.join(web, f[:-4] + ".jpg")
            # ne refaire que ce qui est perime
            if (os.path.exists(dst)
                    and os.path.getmtime(dst) >= os.path.getmtime(src)):
                inchanges += 1
                continue
            try:
                im = Image.open(src)
                if im.mode not in ("RGB", "L"):
                    fond = Image.new("RGB", im.size, (255, 255, 255))
                    im = im.convert("RGBA")
                    fond.paste(im, mask=im.split()[-1])
                    im = fond
                else:
                    im = im.convert("RGB")
                if im.width > LARGEUR:
                    h = int(round(im.height * LARGEUR / float(im.width)))
                    im = im.resize((LARGEUR, h), Image.LANCZOS)
                im.save(dst, "JPEG", quality=QUALITE, optimize=True,
                        progressive=True)
                faits += 1
            except Exception as ex:
                echecs.append((f, str(ex)[:60]))

    print(u"Vignettes produites : %d" % faits)
    print(u"Déjà à jour         : %d" % inchanges)
    if echecs:
        print(u"Échecs (%d) :" % len(echecs))
        for nom, msg in echecs:
            print(u"  %-30s %s" % (nom, msg))
    print(u"Lots traités : %d" % len(LOTS))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
