# -*- coding: utf-8 -*-
"""
MAGPIE - Moteur de generation de fichiers Grasshopper d'exercice.
=================================================================

A executer DANS Rhino 8 (Grasshopper doit avoir ete ouvert au moins une fois
dans la session) via _RunPythonScript, ou depuis un composant script.

Le moteur construit chaque definition en instanciant les composants PAR LEUR NOM
aupres du ComponentServer de Grasshopper : aucun GUID n'est ecrit en dur, ce qui
elimine tout risque de fichier invalide.

Pour chaque exercice il produit deux fichiers :
    <ID>_complet.gh   bandeau + ZONE_SUJET + ZONE_CORRIGE
    <ID>_sujet.gh     bandeau + ZONE_SUJET seuls

Version : v0.1-260825 (Ind. A)
"""

import os
import clr

clr.AddReference("Grasshopper")
clr.AddReference("GH_IO")
clr.AddReference("RhinoCommon")
clr.AddReference("System.Drawing")

import System
import System.Drawing as sd
import Rhino.Geometry as rg
import Grasshopper as GH
from Grasshopper.Kernel import GH_Document, GH_DocumentIO
from Grasshopper.Kernel.Special import (GH_NumberSlider, GH_Panel, GH_Scribble,
                                        GH_Group, GH_BooleanToggle, GH_ValueList,
                                        GH_ValueListItem)
from Grasshopper.Kernel.Types import (GH_Number, GH_String, GH_Point, GH_Boolean,
                                      GH_Vector,
                                      GH_Curve, GH_Brep, GH_Surface, GH_Integer)
import Grasshopper.Kernel.Parameters as GHP


# ---------------------------------------------------------------- mise en page
COL = 265.0          # largeur d'une colonne de la grille
ROW = 108.0          # hauteur d'une ligne : le plus haut des composants poses
                     # (Param Viewer) mesure 100 px
X0 = 60.0            # marge gauche

Y_BANDEAU = 0.0
Y_SUJET = 275.0      # origine de la grille de la zone sujet
Y_CORRIGE = 900.0    # origine de la grille de la zone corrige (>= 200 px sous le sujet)

C_SUJET = sd.Color.FromArgb(80, 200, 220, 245)     # bleu clair
C_CORRIGE = sd.Color.FromArgb(80, 215, 240, 215)   # vert clair
C_PIEGES = sd.Color.FromArgb(80, 250, 215, 215)    # rouge clair
C_DEPART = sd.Color.FromArgb(70, 235, 235, 235)    # gris

VERSION = "v0.5-260902"


# ------------------------------------------------------- catalogue de composants
_BY_NAME = {}
_BY_FULL = {}
_INDEXED = [False]

# categories considerees comme natives : elles sont preferees en cas d'homonymie
_NATIVE = set(["Params", "Maths", "Sets", "Vector", "Curve", "Surface",
               "Mesh", "Intersect", "Transform", "Display", "Rhino"])


def index_catalogue():
    """Indexe tous les composants disponibles, par nom et par chemin complet."""
    if _INDEXED[0]:
        return
    for p in GH.Instances.ComponentServer.ObjectProxies:
        try:
            d = p.Desc
            name = d.Name
            cat = d.Category or ""
            sub = d.SubCategory or ""
        except Exception:
            continue
        if not name:
            continue
        _BY_NAME.setdefault(name, []).append(p)
        _BY_FULL["%s/%s/%s" % (cat, sub, name)] = p
    _INDEXED[0] = True


def _pick(proxies, label):
    """Choisit le proxy le plus pertinent parmi des homonymes."""
    if not proxies:
        raise Exception(u"Composant introuvable : %s" % label)
    if len(proxies) == 1:
        return proxies[0]
    # 1. non obsoletes
    live = [p for p in proxies if not getattr(p, "Obsolete", False)]
    if live:
        proxies = live
    # 2. vrais composants plutot que parametres flottants : la categorie "Params"
    #    contient les parametres de meme nom (Circle, Line, Rectangle...), qui ne
    #    construisent aucune geometrie.
    comp = [p for p in proxies if (p.Desc.Category or "") != "Params"]
    if comp:
        proxies = comp
    # 3. categories natives
    nat = [p for p in proxies if (p.Desc.Category or "") in _NATIVE]
    if nat:
        proxies = nat
    return proxies[0]


def emit(label):
    """Instancie un composant a partir de son nom, ou de 'Categorie/SousCat/Nom'."""
    index_catalogue()
    if "/" in label:
        p = _BY_FULL.get(label)
        if p is None:                      # repli sur le nom seul
            nom = label.split("/")[-1]
            print("    ! chemin '%s' introuvable, repli sur le nom '%s'" % (label, nom))
            p = _pick(_BY_NAME.get(nom, []), nom)
    else:
        p = _pick(_BY_NAME.get(label, []), label)
    obj = p.CreateInstance()
    if obj.Attributes is None:
        obj.CreateAttributes()
    return obj


def check_catalogue(labels):
    """Diagnostic : renvoie (manquants, ambigus, resolutions) pour une liste de noms.

    resolutions donne, pour CHAQUE nom, la categorie et la sous-categorie du
    composant reellement retenu : c'est le controle a relire avant production.
    """
    index_catalogue()
    manquants, ambigus, resolutions = [], [], []
    for lb in sorted(set(labels)):
        nom = lb.split("/")[-1] if "/" in lb else lb
        lst = _BY_NAME.get(nom, [])
        if not lst:
            manquants.append(lb)
            continue
        chosen = _BY_FULL.get(lb) if "/" in lb else None
        if chosen is None:
            chosen = _pick(lst, nom)
        resolutions.append((lb, "%s > %s" % (chosen.Desc.Category,
                                             chosen.Desc.SubCategory), len(lst)))
        if len(lst) > 1:
            ambigus.append((lb, len(lst), "%s > %s" % (chosen.Desc.Category,
                                                       chosen.Desc.SubCategory)))
    return manquants, ambigus, resolutions


# ------------------------------------------------------------- objets speciaux
PARAM_TYPES = {
    "Number": GHP.Param_Number, "Integer": GHP.Param_Integer,
    "Text": GHP.Param_String, "Boolean": GHP.Param_Boolean,
    "Point": GHP.Param_Point, "Vector": GHP.Param_Vector,
    "Plane": GHP.Param_Plane, "Curve": GHP.Param_Curve,
    "Surface": GHP.Param_Surface, "Brep": GHP.Param_Brep,
    "Mesh": GHP.Param_Mesh, "Geometry": GHP.Param_Geometry,
    "Circle": GHP.Param_Circle, "Line": GHP.Param_Line,
    "Interval": GHP.Param_Interval,
}


try:                                           # IronPython 2.7
    _TEXTE = unicode
except NameError:                              # Python 3
    _TEXTE = str


def _u(s):
    """Decode en unicode les litteraux UTF-8 lus sous IronPython 2.7.

    Les fiches du cahier des charges sont ecrites sans prefixe u"" : sous
    Python 2 elles arrivent sous forme d'octets et produiraient des scribbles
    illisibles. Sous Python 3 la fonction est neutre.

    Le test porte sur le TYPE : appeler .decode() sur une chaine deja unicode
    provoquerait sous Python 2 un re-encodage ascii, qui echoue des le premier
    caractere accentue ou tiret cadratin.
    """
    if s is None:
        return None
    if isinstance(s, _TEXTE):
        return s
    if isinstance(s, bytes):
        try:
            return s.decode("utf-8")
        except Exception:
            return s
    return s


def _txt(v):
    try:
        return unicode(v)                      # IronPython 2.7
    except NameError:
        return str(v)                          # Python 3


def _wrap(kind, v):
    if kind == "Number":
        return GH_Number(float(v))
    if kind == "Integer":
        return GH_Integer(int(v))
    if kind == "Text":
        return GH_String(_txt(v))
    if kind == "Boolean":
        return GH_Boolean(bool(v))
    if kind == "Point":
        return GH_Point(rg.Point3d(float(v[0]), float(v[1]), float(v[2])))
    if kind == "Vector":
        # Le type manquait : GP-12 compose une rotation et une
        # translation, et les deux se font sur des VECTEURS.
        return GH_Vector(rg.Vector3d(float(v[0]), float(v[1]), float(v[2])))
    if kind == "Curve":
        return GH_Curve(v)
    if kind == "Brep":
        return GH_Brep(v)
    if kind == "Surface":
        return GH_Surface(v)
    raise Exception(u"Type de donnee non gere : %s" % kind)


# --------------------------------------------------- fabrique de geometrie
def _p3(t):
    return rg.Point3d(float(t[0]), float(t[1]), float(t[2]))


def _pl(o):
    return rg.Plane(_p3(o), rg.Vector3d(0, 0, 1))


def geo_make(rec):
    """Fabrique la geometrie a internaliser. rec = (type, ...) -> liste d'objets."""
    k = rec[0]

    if k == "pts":
        return [_p3(p) for p in rec[1]]

    if k == "interp":
        pts = System.Collections.Generic.List[rg.Point3d]()
        for p in rec[1]:
            pts.Add(_p3(p))
        deg = rec[2] if len(rec) > 2 else 3
        return [rg.Curve.CreateInterpolatedCurve(pts, deg)]

    if k == "poly":
        pl = rg.Polyline([_p3(p) for p in rec[1]])
        if len(rec) > 2 and rec[2]:
            pl.Add(_p3(rec[1][0]))
        return [pl.ToNurbsCurve()]

    if k == "circle":
        return [rg.Circle(_pl(rec[1]), float(rec[2])).ToNurbsCurve()]

    if k == "circles":                                  # (o,r) repetes
        return [rg.Circle(_pl(o), float(r)).ToNurbsCurve() for o, r in rec[1]]

    if k == "rect":
        o, w, h = rec[1], float(rec[2]), float(rec[3])
        r = rg.Rectangle3d(_pl(o), rg.Interval(-w / 2.0, w / 2.0),
                           rg.Interval(-h / 2.0, h / 2.0))
        return [r.ToNurbsCurve()]

    if k == "polygon":                                  # (origine, rayon, cotes)
        o, rad, n = _p3(rec[1]), float(rec[2]), int(rec[3])
        pts = []
        for i in range(n):
            a = 2.0 * System.Math.PI * i / n
            pts.append(rg.Point3d(o.X + rad * System.Math.Cos(a),
                                  o.Y + rad * System.Math.Sin(a), o.Z))
        pts.append(pts[0])
        return [rg.Polyline(pts).ToNurbsCurve()]

    if k == "box":                                      # (origine, dx, dy, dz)
        o = _p3(rec[1])
        b = rg.Box(rg.Plane(o, rg.Vector3d(0, 0, 1)),
                   rg.Interval(0, float(rec[2])),
                   rg.Interval(0, float(rec[3])),
                   rg.Interval(0, float(rec[4])))
        return [b.ToBrep()]

    if k == "boxes":                                    # [(origine, dx, dy, dz), ...]
        out = []
        for o, dx, dy, dz in rec[1]:
            out.extend(geo_make(("box", o, dx, dy, dz)))
        return out

    if k == "cyl":                                      # (origine, rayon, hauteur)
        c = rg.Circle(_pl(rec[1]), float(rec[2]))
        cy = rg.Cylinder(c, float(rec[3]))
        return [cy.ToBrep(True, True)]

    if k == "tube":                 # (origine, largeur, profondeur, hauteur)
        # polysurface ouverte aux deux extremites, ouvertures planes propres :
        # c'est le cas d'usage de Cap Holes.
        rect = geo_make(("rect", rec[1], rec[2], rec[3]))[0]
        s = rg.Surface.CreateExtrusion(rect, rg.Vector3d(0, 0, float(rec[4])))
        return [s.ToBrep()]

    if k == "cyls":                                     # [(origine, rayon, hauteur), ...]
        out = []
        for o, r, h in rec[1]:
            out.extend(geo_make(("cyl", o, r, h)))
        return out

    if k == "sphere":
        return [rg.Sphere(_p3(rec[1]), float(rec[2])).ToBrep()]

    if k == "boxouvert":                                # boite privee de n faces
        brep = geo_make(("box", rec[1], rec[2], rec[3], rec[4]))[0]
        for idx in sorted(rec[5], reverse=True):
            brep.Faces.RemoveAt(idx)
        brep.Compact()
        return [brep]

    if k == "srf":                                      # nappe libre par points
        pts = System.Collections.Generic.List[rg.Point3d]()
        for p in rec[1]:
            pts.Add(_p3(p))
        s = rg.NurbsSurface.CreateThroughPoints(pts, int(rec[2]), int(rec[3]),
                                                3, 3, False, False)
        return [s.ToBrep()]

    raise Exception(u"Recette de geometrie inconnue : %s" % k)


def _append(p, kind, v, path):
    """Ajoute une valeur (ou une valeur nulle) dans une branche donnee."""
    goo = None if v is None else _wrap(kind, v)
    if path is None:
        p.PersistentData.Append(goo)
    else:
        p.PersistentData.Append(goo, path)


def make_param(kind, nick=None, data=None):
    """data accepte trois formes :
         [v, v, v]                    -> liste simple (branche {0})
         [[v, v], [v, v]]             -> arbre, une branche par sous-liste
         [("0;0;1", [v, v]), ...]     -> arbre a chemins explicites
       Une valeur None produit un element nul.
    """
    cls = PARAM_TYPES.get(kind)
    if cls is None:
        raise Exception(u"Type de parametre inconnu : %s" % kind)
    p = cls()
    p.CreateAttributes()
    if nick:
        p.NickName = _u(nick)
        p.Name = _u(nick)
    if data:
        p.PersistentData.Clear()
        # chemins explicites
        if isinstance(data[0], tuple) and len(data[0]) == 2 and isinstance(data[0][0], str):
            for chemin, vals in data:
                idx = System.Array[int]([int(x) for x in chemin.split(";")])
                path = GH.Kernel.Data.GH_Path(idx)
                for v in vals:
                    _append(p, kind, v, path)
        # arbre implicite : une branche par sous-liste
        elif isinstance(data[0], list):
            for i, vals in enumerate(data):
                path = GH.Kernel.Data.GH_Path(i)
                for v in vals:
                    _append(p, kind, v, path)
        # liste simple
        else:
            for v in data:
                _append(p, kind, v, None)
    return p


def set_output_count(obj, n):
    """Fait croitre les SORTIES d'un composant a parametres variables (Explode Tree)."""
    try:
        side = GH.Kernel.GH_ParameterSide.Output
        while obj.Params.Output.Count < n:
            i = obj.Params.Output.Count
            if not obj.CanInsertParameter(side, i):
                break
            obj.Params.RegisterOutputParam(obj.CreateParameter(side, i), i)
        obj.VariableParameterMaintenance()
        obj.Params.OnParametersChanged()
    except Exception as e:
        print("    ! sorties variables non ajustees sur %s : %s" % (obj.Name, e))


def set_input_count(obj, n):
    """Fait croitre un composant a parametres variables (Merge, Entwine, Concatenate)."""
    try:
        side = GH.Kernel.GH_ParameterSide.Input
        while obj.Params.Input.Count < n:
            i = obj.Params.Input.Count
            if not obj.CanInsertParameter(side, i):
                break
            par = obj.CreateParameter(side, i)
            obj.Params.RegisterInputParam(par, i)
        while obj.Params.Input.Count > n:
            i = obj.Params.Input.Count - 1
            if not obj.CanRemoveParameter(side, i):
                break
            obj.Params.UnregisterInputParameter(obj.Params.Input[i])
        obj.VariableParameterMaintenance()
        obj.Params.OnParametersChanged()
    except Exception as e:
        print("    ! entrees variables non ajustees sur %s : %s" % (obj.Name, e))


def make_slider(mini, maxi, val, dec=0, nick=None):
    s = GH_NumberSlider()
    s.CreateAttributes()
    s.Slider.Minimum = System.Decimal(float(mini))
    s.Slider.Maximum = System.Decimal(float(maxi))
    try:
        s.Slider.DecimalPlaces = int(dec)
        if int(dec) == 0:
            s.Slider.Type = GH.GUI.Base.GH_SliderAccuracy.Integer
        else:
            s.Slider.Type = GH.GUI.Base.GH_SliderAccuracy.Float
    except Exception:
        pass
    s.SetSliderValue(System.Decimal(float(val)))
    if nick:
        s.NickName = _u(nick)
    return s


def make_panel(text=None, multiline=False, w=210, h=95):
    """multiline=False : chaque ligne du Panel devient un element distinct.
    C'est le comportement attendu pour un Panel qui sert de source de donnees
    (motif booleen, liste de valeurs). A True, tout le texte ne forme qu'un seul
    element, ce qui fait echouer les conversions en aval."""
    p = GH_Panel()
    p.CreateAttributes()
    if text is not None:
        # Grasshopper decoupe le contenu d'un Panel en elements sur les fins de
        # ligne Windows : un simple \n resterait un unique element.
        t = _txt(_u(text)).replace("\r\n", "\n").replace("\n", "\r\n")
        p.SetUserText(t)
    try:
        p.Properties.Multiline = multiline
        p.Properties.Wrap = True
    except Exception:
        pass
    try:
        p.Attributes.Bounds = sd.RectangleF(0, 0, float(w), float(h))
    except Exception:
        pass
    return p


def make_toggle(value=False, nick=None):
    t = GH_BooleanToggle()
    t.CreateAttributes()
    t.Value = bool(value)
    if nick:
        t.NickName = _u(nick)
    return t


def make_valuelist(items, nick=None):
    """items : liste de (libelle, expression) - l'expression est du code GH."""
    v = GH_ValueList()
    v.CreateAttributes()
    v.ListItems.Clear()
    for lab, expr in items:
        v.ListItems.Add(GH_ValueListItem(_txt(_u(lab)), _txt(expr)))
    if nick:
        v.NickName = _u(nick)
    return v


def _replier(t, n):
    """Retour a la ligne : GH_Scribble n'en fait aucun et s'etirerait sans fin."""
    if not n:
        return t
    out = []
    for para in t.split("\n"):
        ligne = ""
        for mot in para.split(" "):
            if ligne and len(ligne) + 1 + len(mot) > n:
                out.append(ligne)
                ligne = mot
            else:
                ligne = (ligne + " " + mot).strip()
        out.append(ligne)
    return "\n".join(out)


def make_scribble(doc, text, x, y, w=None, h=None, size=14, bold=False, wrap=None):
    """Pose un scribble a (x, y).

    ATTENTION : pour un GH_Scribble, seul Attributes.PIVOT est conserve a
    l'enregistrement. Positionner via Attributes.Bounds, ou en deplacant les
    Corners, fonctionne a l'ecran mais est perdu au premier aller-retour : les
    corners sont renormalises a l'origine et tous les scribbles se retrouvent
    empiles en haut a gauche du canvas. Verifie par aller-retour le 26/08/2026.
    """
    s = GH_Scribble()
    s.CreateAttributes()
    text = _replier(_u(text), wrap)
    try:
        s.Text = text
    except Exception:
        try:
            s.SetText(text)
        except Exception:
            pass
    try:
        style = sd.FontStyle.Bold if bold else sd.FontStyle.Regular
        s.Font = sd.Font("Arial", float(size), style)
    except Exception:
        pass
    doc.AddObject(s, False)
    try:
        s.Attributes.Pivot = sd.PointF(float(x), float(y))
    except Exception as e:
        print("    ! scribble non positionne : %s" % e)
    return s


def hauteur(obj, defaut=30.0):
    """Hauteur reelle occupee par un objet sur le canvas."""
    try:
        return float(obj.Attributes.Bounds.Height)
    except Exception:
        return defaut


def make_group(doc, name, objs, colour):
    g = GH_Group()
    g.CreateAttributes()
    g.NickName = _u(name)
    try:
        g.Colour = colour
        # Rectangle plutot que Blob : les ellipses des groupes imbriques se
        # chevauchent et rendent les captures de canvas illisibles.
        g.Border = GH.Kernel.Special.GH_GroupBorder.Rectangle
    except Exception:
        pass
    doc.AddObject(g, False)
    for o in objs:
        g.AddObject(o.InstanceGuid)
    g.ExpireCaches()
    return g


# --------------------------------------------------------------------- cablage
def _out(o, i):
    try:
        return o.Params.Output[i]
    except Exception:
        return o


def _in(o, i):
    try:
        return o.Params.Input[i]
    except Exception:
        return o


def connect(src, src_i, dst, dst_i):
    _in(dst, dst_i).AddSource(_out(src, src_i))


# --------------------------------------------------------- construction d'un ex
def _place(obj, col, row, y0):
    obj.Attributes.Pivot = sd.PointF(X0 + float(col) * COL, y0 + float(row) * ROW)


def _instancier(spec):
    """spec = (cle, label, col, row, options) -> objet Grasshopper."""
    label = spec[1]
    o = spec[4] if len(spec) > 4 and spec[4] else {}
    if label == "SLIDER":
        mn, mx, vl, dc = o.get("slider", (0, 100, 50, 0))
        return make_slider(mn, mx, vl, dc, o.get("nick"))
    if label == "PANEL":
        return make_panel(o.get("text"), w=o.get("w", 180), h=o.get("h", 60))
    if label == "TOGGLE":
        return make_toggle(o.get("value", False), o.get("nick"))
    if label == "VALUELIST":
        return make_valuelist(o.get("items", [("A", "0"), ("B", "1")]), o.get("nick"))
    if label == "REPONSE":
        return make_param(o.get("type", "Number"), "REPONSE")
    if label.startswith("DATA:"):
        kind = label.split(":", 1)[1]
        return make_param(kind, o.get("nick", "DONNEES"), o.get("data"))
    if label.startswith("PARAM:"):
        kind = label.split(":", 1)[1]
        return make_param(kind, o.get("nick"))
    if label.startswith("GEO:"):
        kind = label.split(":", 1)[1]
        return make_param(kind, o.get("nick", "GEOMETRIE"), geo_make(o["geo"]))
    obj = emit(label)
    if o.get("nick"):
        obj.NickName = _u(o["nick"])
    if o.get("inputs"):                   # composant a entrees variables
        set_input_count(obj, int(o["inputs"]))
    if o.get("outputs"):                  # composant a sorties variables
        set_output_count(obj, int(o["outputs"]))
    if o.get("layer"):                    # Geometry Pipeline : filtre de calque
        for prop in ("LayerFilter", "Layer", "NameFilter"):
            try:
                setattr(obj, prop, o["layer"])
                break
            except Exception:
                continue
    if o.get("expr"):                     # expression sur une entree : {"expr": (0, "x*2")}
        try:
            obj.Params.Input[o["expr"][0]].Expression = o["expr"][1]
        except Exception:
            pass
    if o.get("graft") is not None:        # {"graft": 0} -> graft sur l'entree 0
        try:
            obj.Params.Input[o["graft"]].DataMapping = GH.Kernel.GH_DataMapping.Graft
        except Exception:
            pass
    if o.get("val") is not None:          # valeur persistante sur une entree
        for idx, kind, vals in o["val"]:
            try:
                p = obj.Params.Input[idx]
                p.PersistentData.Clear()
                for v in vals:
                    p.PersistentData.Append(_wrap(kind, v))
            except Exception:
                pass
    return obj


def build_exercice(ex, dossier, verbose=True):
    """Construit et enregistre les deux fichiers d'un exercice.

    Deux regles structurantes :

    1. AUCUN cable ne relie la zone sujet a la zone corrige. Les composants du
       sujet dont le corrige a besoin y sont RECOPIES, avec leurs donnees
       internalisees, et le cablage interne du sujet est rejoue entre ces copies.
       Les deux zones sont ainsi totalement independantes.

    2. Le corrige ne produit ni n'affiche rien tant que l'interrupteur
       AFFICHER LE CORRIGE reste sur faux : son resultat traverse un Stream Gate
       pilote par ce booleen, et l'apercu est coupe sur tous ses composants.
    """
    doc = GH_Document()
    reg = {}            # objets de la zone sujet
    reg_c = {}          # objets de la zone corrige (copies + solution)
    objs_sujet = []
    objs_corrige = []
    groupes_corrige = []

    # ---- bandeau
    titre = u"%s · %s" % (_u(ex["id"]), _u(ex["titre"]))
    b1 = make_scribble(doc, titre, X0, Y_BANDEAU, size=20, bold=True)
    meta = u"%s  —  durée cible %d min  —  réf. %s  —  %s" % (
        _u(ex["niv"]), ex["duree"], _u(ex["ref"]), VERSION)
    b2 = make_scribble(doc, meta, X0, Y_BANDEAU + 46, size=11)
    bandeau = [b1, b2]

    # ---- zone sujet
    # 130 et non 90 : au-dessus, l'etiquette du groupe ZONE_SUJET viendrait
    # recouvrir la ligne de metadonnees du bandeau.
    sc_en = make_scribble(doc, ex["enonce"], X0, Y_BANDEAU + 130, size=13, wrap=95)
    objs_sujet.append(sc_en)
    sujet_specs = {}
    ordre_sujet = []
    for spec in ex.get("sujet", []):
        o = _instancier(spec)
        doc.AddObject(o, False)
        _place(o, spec[2], spec[3], Y_SUJET)
        reg[spec[0]] = o
        objs_sujet.append(o)
        sujet_specs[spec[0]] = spec
        ordre_sujet.append(spec[0])

    # ---- analyse du cablage
    wires = [(w[0], 0, w[1], w[2]) if len(w) == 3 else tuple(w)
             for w in ex.get("wires", [])]

    cles_corrige = set()
    for _, specs in ex.get("corrige", []):
        for spec in specs:
            cles_corrige.add(spec[0])

    def est_corrige(cle):
        return cle in cles_corrige or cle == "rep"

    # dependances internes au sujet, pour recopier tout l'amont necessaire
    pred = {}
    for s, si, d, di in wires:
        if d in sujet_specs and d != "rep":
            pred.setdefault(d, []).append(s)

    def remonter(cle, vus):
        for p in pred.get(cle, []):
            if p not in vus:
                vus.add(p)
                remonter(p, vus)

    besoins = set()
    for s, si, d, di in wires:
        if est_corrige(d) and s in sujet_specs and s != "rep":
            besoins.add(s)
            remonter(s, besoins)
    besoins = [k for k in ordre_sujet if k in besoins]

    # ---- separateur
    sep = make_scribble(
        doc, u"▼  CORRIGÉ — à consulter après validation  ▼",
        X0, Y_CORRIGE - 110, size=16, bold=True)

    y = Y_CORRIGE

    # ---- rappel : copies des donnees fournies
    if besoins:
        sc = make_scribble(
            doc, u"RAPPEL — copie des données fournies dans la zone sujet, "
                 u"afin qu'aucun câble ne relie les deux zones",
            X0, y - 70, size=12, bold=True, wrap=105)
        objs_corrige.append(sc)
        copies, rmax = [], 0
        for i, cle in enumerate(besoins):
            spec = sujet_specs[cle]
            o = _instancier(spec)
            doc.AddObject(o, False)
            # rangees compactement de gauche a droite, et non a leur position
            # d'origine dans le sujet : cela evite de longs cables en diagonale.
            _place(o, i, 0, y)
            reg_c[cle] = o
            objs_corrige.append(o)
            copies.append(o)
        groupes_corrige.append(
            make_group(doc, u"DONNÉES FOURNIES (copie)", copies, C_DEPART))
        y += (rmax + 1) * ROW + 85

    # ---- etapes du corrige
    for i, (titre_et, specs) in enumerate(ex.get("corrige", []), 1):
        sc = make_scribble(doc, u"ÉTAPE %d — %s" % (i, _u(titre_et)),
                           X0, y - 70, size=12, bold=True, wrap=105)
        objs_corrige.append(sc)
        rmax, etape_objs = 0, []
        for spec in specs:
            o = _instancier(spec)
            doc.AddObject(o, False)
            _place(o, spec[2], spec[3], y)
            reg_c[spec[0]] = o
            objs_corrige.append(o)
            etape_objs.append(o)
            rmax = max(rmax, spec[3])
        groupes_corrige.append(make_group(doc, u"ÉTAPE %d" % i, etape_objs, C_CORRIGE))
        y += (rmax + 1) * ROW + 70

    # ---- reglages que l'API ne sait pas poser
    manuel = ex.get("manuel") or []
    if manuel:
        txt = u"RÉGLAGES À POSER À LA MAIN :\n" + u"\n".join(u"• " + _u(m) for m in manuel)
        sc_man = make_scribble(doc, txt, X0, y + 20, size=12, bold=True, wrap=105)
        objs_corrige.append(sc_man)
        groupes_corrige.append(make_group(doc, u"RÉGLAGES MANUELS", [sc_man], C_PIEGES))
        # hauteur reelle du scribble : une estimation au nombre de lignes
        # laissait la bande suivante chevaucher ce bloc.
        y += hauteur(sc_man, 60.0) + 120

    # ---- sortie du corrige, conditionnee par l'interrupteur
    rep_spec = sujet_specs.get("rep")
    rep_c = porte = toggle = None
    if rep_spec is not None:
        sc = make_scribble(
            doc, u"RÉSULTAT — tant que l'interrupteur AFFICHER LE CORRIGÉ reste sur "
                 u"faux, la sortie 1 du Stream Gate est vide : rien n'apparaît dans Rhino",
            X0, y - 62, size=12, bold=True, wrap=105)
        objs_corrige.append(sc)
        toggle = make_toggle(False, u"AFFICHER LE CORRIGÉ")
        doc.AddObject(toggle, False)
        _place(toggle, 0, 0, y)
        porte = emit("Stream Gate")
        doc.AddObject(porte, False)
        _place(porte, 1, 0, y)
        connect(toggle, 0, porte, 1)                     # entree 1 = Gate
        rep_c = make_param(rep_spec[4].get("type", "Number"), u"REPONSE_CORRIGE")
        doc.AddObject(rep_c, False)
        _place(rep_c, 2, 0, y)
        connect(porte, 1, rep_c, 0)                      # sortie 1 = Target 1
        for o in (toggle, porte, rep_c):
            objs_corrige.append(o)
        groupes_corrige.append(
            make_group(doc, u"AFFICHAGE DU CORRIGÉ", [toggle, porte, rep_c], C_PIEGES))
        reg_c["rep"] = rep_c
        y += ROW + 85

    # ---- cablage
    for s, si, d, di in wires:
        if est_corrige(d):
            src = reg_c.get(s)
            if src is None:
                raise Exception(u"%s : source '%s' absente de la zone corrigé" % (ex["id"], s))
            if d == "rep":
                if porte is None:
                    raise Exception(u"%s : aucune sortie de corrigé" % ex["id"])
                connect(src, si, porte, 0)               # entree 0 = Stream
            else:
                dst = reg_c.get(d)
                if dst is None:
                    raise Exception(u"%s : cible '%s' inconnue" % (ex["id"], d))
                connect(src, si, dst, di)
        else:
            if s not in reg or d not in reg:
                raise Exception(u"%s : câblage sujet inconnu %s -> %s" % (ex["id"], s, d))
            connect(reg[s], si, reg[d], di)
            if s in reg_c and d in reg_c:                # rejoue entre les copies
                connect(reg_c[s], si, reg_c[d], di)

    # ---- groupes de zone
    make_group(doc, "BANDEAU", bandeau, C_DEPART)
    make_group(doc, "ZONE_SUJET", objs_sujet, C_SUJET)
    g_corr = make_group(doc, "ZONE_CORRIGE", objs_corrige + [sep], C_CORRIGE)

    # ---- apercu coupe partout dans le corrige, sauf sur la sortie conditionnee
    for o in objs_corrige:
        if o is rep_c:
            continue
        try:
            o.Hidden = True
        except Exception:
            pass

    if not os.path.isdir(dossier):
        os.makedirs(dossier)

    p_complet = os.path.join(dossier, "%s_complet.gh" % ex["id"])
    GH_DocumentIO(doc).SaveQuiet(p_complet)

    # ---- derivation du sujet : le corrige est retire en bloc
    for g in groupes_corrige + [g_corr]:
        try:
            doc.RemoveObject(g, False)
        except Exception:
            pass
    for o in objs_corrige + [sep]:
        try:
            doc.RemoveObject(o, False)
        except Exception:
            pass

    p_sujet = os.path.join(dossier, "%s_sujet.gh" % ex["id"])
    GH_DocumentIO(doc).SaveQuiet(p_sujet)

    if verbose:
        print("  %s : sujet %d objets | corrigé %d objets, dont %d copies" %
              (ex["id"], len(objs_sujet), len(objs_corrige), len(besoins)))
    return p_complet, p_sujet


def labels_utilises(exercices):
    """Tous les noms de composants employes par un jeu d'exercices."""
    out = []
    for ex in exercices:
        for spec in ex.get("sujet", []):
            out.append(spec[1])
        for _, specs in ex.get("corrige", []):
            for spec in specs:
                out.append(spec[1])
    speciaux = ("SLIDER", "PANEL", "TOGGLE", "VALUELIST", "REPONSE")
    prefixes = ("DATA:", "PARAM:", "GEO:")
    return [l for l in out
            if l not in speciaux and not l.startswith(prefixes)]
