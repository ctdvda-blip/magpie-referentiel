# -*- coding: utf-8 -*-
"""
MAGPIE - Rendu des canvas Grasshopper en images, pour illustrer les fiches Word.

A executer DANS Rhino 8 via le pont rhinomcp.

Pour chaque exercice, deux images sont produites dans <dossier>/Illustrations :
    <ID>_canvas_sujet.png     le canvas tel que l'apprenant l'ouvre
    <ID>_canvas_corrige.png   la zone corrigee seule, cablage visible

GenerateHiResImage renvoie des TUILES : elles sont assemblees ici en une image
unique. Le nom de chaque tuile est "colonne;ligne.png".
"""
import os
import sys
import clr

clr.AddReference("Grasshopper")
clr.AddReference("System.Drawing")
import System
import System.Drawing as sd
from Grasshopper.Kernel import GH_DocumentIO
from Grasshopper.Kernel.Special import GH_Group
from Grasshopper.GUI.Canvas import GH_Canvas

EXOS = "C:/Users/charl/.claude/projects/MAGPIE/EXERCICES"
# Les lots vivent chacun dans leur dossier ; on les rend tous.
from lots import LOTS as _REG
RACINES = [os.path.join(EXOS, d.split("/")[-1]) for _c,_n,d,_l in _REG]
RACINE = RACINES[0]   # conserve pour compatibilite
ZOOM = 1.6
MARGE = 65


def bornes(objets):
    xs, ys, xe, ye = [], [], [], []
    for o in objets:
        try:
            b = o.Attributes.Bounds
        except Exception:
            continue
        if b.Width <= 0 or b.Height <= 0:
            continue
        xs.append(b.X); ys.append(b.Y)
        xe.append(b.X + b.Width); ye.append(b.Y + b.Height)
    if not xs:
        return None
    return System.Drawing.Rectangle(
        int(min(xs) - MARGE), int(min(ys) - MARGE),
        int(max(xe) - min(xs) + 2 * MARGE), int(max(ye) - min(ys) + 2 * MARGE))


def assembler(tuiles, taille, sortie):
    """Recolle les tuiles renvoyees par GenerateHiResImage en une seule image."""
    infos = []
    for t in tuiles:
        nom = os.path.splitext(os.path.basename(t))[0]
        try:
            c, r = [int(v) for v in nom.split(";")]
        except Exception:
            continue
        infos.append((c, r, t))
    if not infos:
        return False

    larg, haut = {}, {}
    for c, r, t in infos:
        im = sd.Bitmap(t)
        larg[c] = im.Width
        haut[r] = im.Height
        im.Dispose()
    ox, acc = {}, 0
    for c in sorted(larg):
        ox[c] = acc; acc += larg[c]
    oy, acc = {}, 0
    for r in sorted(haut):
        oy[r] = acc; acc += haut[r]

    bmp = sd.Bitmap(int(taille.Width), int(taille.Height))
    g = sd.Graphics.FromImage(bmp)
    g.Clear(sd.Color.White)
    for c, r, t in infos:
        im = sd.Bitmap(t)
        g.DrawImage(im, int(ox[c]), int(oy[r]))
        im.Dispose()
    g.Dispose()
    d = os.path.dirname(sortie)
    if not os.path.isdir(d):
        os.makedirs(d)
    if os.path.isfile(sortie):
        os.remove(sortie)
    bmp.Save(sortie, sd.Imaging.ImageFormat.Png)
    bmp.Dispose()
    for c, r, t in infos:
        try:
            os.remove(t)
        except Exception:
            pass
    return True


def rendre(doc, rec, sortie, tag):
    if rec is None:
        return False
    c = GH_Canvas()
    c.Document = doc
    st = GH_Canvas.GH_ImageSettings()
    st.Folder = os.environ.get("TEMP", ".")
    st.FileName = "magpie_" + tag
    st.Extension = ".png"
    st.Zoom = ZOOM
    st.BackColour = sd.Color.White
    tuiles, taille = c.GenerateHiResImage(rec, st)
    ok = assembler(list(tuiles), taille, sortie)
    try:
        c.Dispose()
    except Exception:
        pass
    return ok


def objets_du_groupe(doc, nom):
    for o in doc.Objects:
        if isinstance(o, GH_Group):
            try:
                if (o.NickName or "") == nom:
                    ids = set(str(i) for i in o.ObjectIDs)
                    return [x for x in doc.Objects
                            if str(x.InstanceGuid) in ids]
            except Exception:
                pass
    return []


#: si non vide, seuls ces identifiants sont rendus. Sert aux relances
#: ciblees : rendre a nouveau les 198 canvas pour trois exercices neufs
#: couterait une demi-heure sans rien changer aux 195 autres.
SEULEMENT = set()


def main():
    faits, rates = 0, []
    paires = []
    for _rac in RACINES:
        if os.path.isdir(_rac):
            paires += [(_rac, _d) for _d in sorted(os.listdir(_rac))]
    for RACINE, d in paires:
        dd = os.path.join(RACINE, d)
        if not os.path.isdir(dd):
            continue
        ident = d.split(" ")[0]
        if SEULEMENT and ident not in SEULEMENT:
            continue
        ill = os.path.join(dd, "Illustrations")

        # --- canvas du sujet
        p = os.path.join(dd, "%s_sujet.gh" % ident)
        if os.path.isfile(p):
            io = GH_DocumentIO()
            if io.Open(p):
                doc = io.Document
                doc.Enabled = True
                try:
                    doc.NewSolution(True)
                except Exception:
                    pass
                r = rendre(doc, bornes(list(doc.Objects)),
                           os.path.join(ill, "%s_canvas_sujet.png" % ident),
                           ident + "_s")
                if not r:
                    rates.append(ident + " sujet")

        # --- canvas du corrige seul
        p = os.path.join(dd, "%s_complet.gh" % ident)
        if os.path.isfile(p):
            io = GH_DocumentIO()
            if io.Open(p):
                doc = io.Document
                doc.Enabled = True
                try:
                    doc.NewSolution(True)
                except Exception:
                    pass
                objs = objets_du_groupe(doc, u"ZONE_CORRIGE")
                if not objs:
                    objs = [o for o in doc.Objects
                            if getattr(o, "Attributes", None) is not None
                            and o.Attributes.Bounds.Y > 700]
                r = rendre(doc, bornes(objs),
                           os.path.join(ill, "%s_canvas_corrige.png" % ident),
                           ident + "_c")
                if not r:
                    rates.append(ident + " corrige")
        faits += 1
        if faits % 10 == 0:
            print("  ... %d exercices traites" % faits)

    print("Exercices traites : %d" % faits)
    if rates:
        print("Rendus manques (%d) : %s" % (len(rates), ", ".join(rates)))
    else:
        print("Toutes les illustrations ont ete produites.")


# Le fichier est prevu pour etre ouvert dans l'editeur de Rhino et execute :
# il se lance donc de lui-meme. Mais une relance ciblee l'IMPORTE pour poser
# SEULEMENT avant d'appeler main() ; sans cette garde, l'import a lui seul
# rendrait les 198 canvas. Le test porte sur le nom du module plutot que sur
# "__main__" : selon la voie d'execution, Rhino donne "__main__" ou
# "__builtin__", jamais "gen_images".
if __name__ != "gen_images":
    main()
