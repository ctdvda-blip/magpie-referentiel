# -*- coding: utf-8 -*-
"""Audit des exercices au regard de la skill magpie-conception-exercices v2.3.

    python Documentation/Generateurs/audit_skill.py            lot A brut
    python Documentation/Generateurs/audit_skill.py --fusion   lot A refondu
    python Documentation/Generateurs/audit_skill.py --tous     LES 14 LOTS

Cet audit n'a longtemps porte que sur les 49 exercices du lot A — le corpus
etait code en dur. C'etait la cinquieme liste du projet a decrocher de ce
qu'elle etait censee couvrir : le referentiel en compte 229. `--tous` lit le
registre, et le vocabulaire comme les types de REPONSE sont deduits de tous
les lots.

N'applique que les controles mecanisables. Les jugements demandant une lecture
humaine sont signales comme points d'attention, jamais tranches automatiquement.

Note d'implementation : aucune sequence d'echappement regex n'est ecrite avec un
antislash ici (les bornes de mot passent par des lookarounds sur classes), pour
rester robuste aux outils qui reecrivent ce fichier.
"""
import io
import os
import re
import sys
import json

#: saut de ligne, pose par son code : les outils qui reecrivent
#: ce fichier avalent les sequences d'echappement.
NL = chr(10)

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

from exos_a import LOT_A
from lots import TOUS

LETTRES = u"A-Za-z0-9À-ſ"
AVANT = u"(?<![" + LETTRES + u"])"
APRES = u"(?![" + LETTRES + u"])"


def borne(mot):
    """Motif « mot entier » sans recourir a une sequence antislash-b."""
    return AVANT + re.escape(mot) + APRES


# --- vocabulaire des composants : tout ce qui est cite en champ `comp` -------
# Les champs `comp` des lots recents decrivent parfois le materiel en
# francais — « groupes », « bornes », « agent de code ». Etendre le
# vocabulaire a tous les lots y a fait entrer ces mots, qui declenchaient
# la regle §3 sur des enonces parfaitement corrects. On ne retient donc
# que ce qui a la FORME d'un nom de composant Grasshopper : chaque mot
# commence par une majuscule ou un chiffre.
RE_NOM_COMPOSANT = re.compile(u"^[A-Z0-9][^ ]*( [A-Z0-9][^ ]*)*$")

VOCAB = set()
for _e in TOUS:
    for _c in re.split(u"[,/]", _e.get("comp", u"")):
        _c = _c.strip()
        if len(_c) > 2 and RE_NOM_COMPOSANT.match(_c):
            VOCAB.add(_c)

# Noms qui sont aussi des mots courants du francais ou du vocabulaire geometrique :
# les citer dans un enonce ne revele pas l'outil a employer.
GENERIQUES = set(u"""Point Line Curve Surface Number Panel Series Range Text Domain
Plane Vector Circle Box Mesh Group Sort Area Volume Length Angle Move Scale
Rotate Mirror Offset Divide Join Split Trim Extrude Loft Sphere
Rhino Grasshopper Kangaroo Python Excel Revit Windows Magpie""".split())
# Les versions du logiciel ne sont pas des composants : « Rhino 8 » dans un
# enonce designe l'environnement, pas un outil a trouver.
GENERIQUES |= set([u"Rhino 8", u"Rhino 7", u"Grasshopper 2"])

TESTABLES = sorted([v for v in VOCAB if v not in GENERIQUES], key=len, reverse=True)

# Type declare du parametre REPONSE, lu dans les recettes de construction.
TYPES_REPONSE = {}
try:
    import os as _os
    _gh = _os.path.join(ICI, "GH")
    if _gh not in sys.path:
        sys.path.insert(0, _gh)
    import importlib
    import recettes_skill
    # Les modules de recettes sont DECOUVERTS. Les lister a la main revenait
    # a ignorer en silence les lots produits apres l'ecriture de ce fichier.
    _R, _apres = {}, {}
    for _f in sorted(_os.listdir(_gh)):
        if not (_f.startswith("recipes_") and _f.endswith(".py")):
            continue
        _m = importlib.import_module(_f[:-3])
        if _f.startswith("recipes_a"):
            _R.update(getattr(_m, "R", {}))
        else:
            _apres.update(getattr(_m, "R", {}))
    recettes_skill.appliquer(_R)
    _R.update(_apres)
    for _k, _v in _R.items():
        for _n in _v.get("sujet", []):
            if _n[0] == "rep":
                TYPES_REPONSE[_k] = _n[4].get("type", "Number")
except Exception as _ex:
    print("  (types de REPONSE non lus : %s)" % _ex)

# --- signaux du §1 : connaissance plutot que competence ---------------------
RE_DEMO = re.compile(u"constat|observ|vérifi|verifi|que se passe|remarqu"
                     u"|combien de valeurs|comprends? pourquoi|affiche le résultat", re.I)
RE_DECLAR = re.compile(u"^[ ]*(comprendre que|comprendre qu|savoir que|découvrir"
                       u"|decouvrir|identifier que|mémoriser|memoriser)", re.I)

# --- §5 : jeu de donnees de demonstration -----------------------------------
# Ne vise QUE les jeux de donnees. « trois valeurs réglables » decrit l'arite
# d'une construction (un point a trois coordonnees, pas quarante) : ce n'est pas
# un jeu de donnees devinable et la regle §5 ne s'y applique pas.
RE_PETIT = re.compile(u"(la liste (contient|comporte) (3|4|5|6|7|8|9|dix|"
                      u"trois|quatre|cinq|six|sept|huit|neuf) "
                      u"|de 0 à 10|de 1 à 10|de 0 à 9|de 1 à 5"
                      u"|liste de (5|6|7|8|9|10) )", re.I)


def audit(e):
    """Retourne la liste des ecarts (code de regle, libelle) pour un exercice."""
    d = []

    # Un item requalifie en connaissance n'est plus un exercice : il doit
    # porter une question charniere, et les regles §3/§5 ne s'y appliquent pas.
    if e.get(u"verdict") == u"connaissance":
        if not e.get(u"charniere"):
            d.append((u"§1", u"requalifié en connaissance mais sans question "
                      u"charnière de remplacement"))
        if not e.get(u"contexte"):
            d.append((u"§4", u"aucun contexte métier"))
        return d

    # ---- §3 : aucun nom de composant dans la consigne
    trouves = [c for c in TESTABLES if re.search(borne(c), e["enonce"])]
    # ne garder que les plus longs : « Construct Point » absorbe « Point »
    gardes = []
    for t in trouves:
        if not any(t != o and t in o for o in trouves):
            gardes.append(t)
    if gardes:
        d.append((u"§3", u"nom de composant dans l'énoncé : "
                  + u", ".join(sorted(gardes)[:5])))

    # ---- §1 : signaux de connaissance plutot que de competence
    if RE_DEMO.search(e["enonce"]):
        d.append((u"§1", u"énoncé de type démonstration "
                  u"(fait constater un comportement au lieu de demander un résultat)"))
    if RE_DECLAR.search(e["obj"]):
        d.append((u"§1", u"objectif déclaratif : « %s… »"
                  % e["obj"][:40].strip()))
    # `nb` vaut 0 pour les sept exercices dont le livrable n'est pas une
    # definition — un plugin compile, un site, un configurateur en ligne.
    # Leur compter zero composant comme un defaut de conception n'a pas de
    # sens : ils n'en ont pas parce qu'ils n'en veulent pas.
    if 0 < e.get("nb", 0) <= 3:
        d.append((u"§1", u"solution de référence à %d composants : "
                  u"un seul geste suffit" % e["nb"]))

    # ---- §4 : contexte metier
    if not e.get(u"contexte"):
        d.append((u"§4", u"aucun contexte métier"))

    # ---- §5 : donnees devinables
    if not e.get(u"exempt5"):
        if RE_PETIT.search(e["enonce"]) or RE_PETIT.search(e.get("depart", u"")):
            d.append((u"§5", u"jeu de données court ou ordonné, lisible à l'œil"))

    # ---- §5 : le jeu de donnees doit etre JUSTIFIE
    # Pourquoi ces valeurs-la : ce qu'elles rendent visible, ce qu'elles
    # excluent, l'ecart qu'elles creusent entre la bonne reponse et
    # l'erreur attendue. Sans cette note, un jeu de donnees se remplace par
    # un autre et l'exercice perd ce qui le rendait discriminant.
    # Encore faut-il qu'il Y AIT un jeu de donnees. Trente-et-un
    # exercices du lot A n'en ont pas — construire un point a (30, -15,
    # 8), tracer un hexagone inscrit — et leur reclamer une
    # justification revenait a exiger trente-et-une phrases vides.
    if e.get(u"jeu") and not e.get(u"donnees_note"):
        d.append((u"§5", u"jeu de données non justifié"))

    # ---- §6 : erreur attendue
    if not e.get(u"erreur"):
        d.append((u"§6", u"aucune erreur attendue anticipée"))

    # ---- §6 : ce que la correction automatique NE dit pas
    if not e.get(u"limite"):
        d.append((u"§6", u"limite de correction non énoncée"))

    # ---- contraintes du checker
    tol = (e["tol"] or u"").replace(u",", u".").strip()
    non_nul = tol not in (u"0", u"—", u"", u"0.0", u"-")
    if e["mode"] == u"SingleValue" and non_nul:
        d.append((u"CHK", u"SingleValue avec tolérance « %s » : "
                  u"la tolérance est ignorée, comparaison à 1e-9" % e["tol"]))
    if e["mode"] == u"GeometryTolerance" and not non_nul:
        d.append((u"CHK", u"GeometryTolerance sans tolérance : retombe sur "
                  u"le 0.001 du document Rhino"))
    # Le checker ne compare que des nombres : un booleen ou un texte branche
    # sur la verification echoue. On interroge la RECETTE, qui declare le type
    # du parametre REPONSE — c'est la source qui fait autorite, et elle ne
    # produit pas les faux positifs d'une lecture du texte de l'attendu.
    typ = TYPES_REPONSE.get(e["id"])
    if typ in (u"Boolean", u"Text") and e.get(u"mode") not in (u"Visuel", u"—"):
        d.append((u"CHK", u"le paramètre REPONSE est de type %s : le checker "
                  u"ne compare que des nombres" % typ))

    if e["mode"] in (u"ExactOrderedList", u"SetEquality") and non_nul:
        d.append((u"CHK", u"%s avec tolérance « %s » : aucune tolérance "
                  u"n'est appliquée dans ce mode" % (e["mode"], e["tol"])))
    return d


def main():
    fusion = u"--fusion" in sys.argv
    tous = u"--tous" in sys.argv
    if tous:
        corpus, portee = TOUS, u"les 14 lots"
    elif fusion:
        from skill_a import fusionner
        corpus, portee = [fusionner(e) for e in LOT_A], u"lot A refondu"
    else:
        corpus, portee = LOT_A, u"lot A brut"

    lignes, tot, par_exo = [], {}, {}
    for e in corpus:
        ec = audit(e)
        par_exo[e["id"]] = ec
        for code, txt in ec:
            lignes.append((e["id"], e["titre"], code, txt))
            tot[code] = tot.get(code, 0) + 1

    nom = (u"AUDIT_SKILL_TOUS.md" if tous
           else u"AUDIT_SKILL_APRES.md" if fusion else u"AUDIT_SKILL.md")
    out = io.open(os.path.join(ICI, nom), "w", encoding="utf-8")
    out.write(u"# Audit — skill de conception d'exercices Magpie v2.3\n\n")
    out.write((u"Portée : **%s**. %d exercices contrôlés, **%d écarts** "
               u"relevés." % (portee, len(corpus), len(lignes))) + NL + NL)
    out.write(u"| Règle | Écarts | Portée |\n|---|---|---|\n")
    legende = {
        u"§1": u"exercice testant une connaissance plutôt qu'une compétence",
        u"§3": u"nom de composant donné dans la consigne",
        u"§4": u"contexte métier absent",
        u"§5": u"données devinables, ou jeu de données non justifié",
        u"§6": u"erreur attendue non anticipée, ou limite de correction absente",
        u"CHK": u"contrainte du checker violée",
    }
    for k in sorted(tot, key=lambda x: -tot[x]):
        out.write(u"| %s | %d | %s |\n" % (k, tot[k], legende.get(k, u"")))

    out.write(u"\n## Détail par exercice\n\n")
    for e in corpus:
        ec = par_exo[e["id"]]
        out.write(u"### %s — %s\n\n" % (e["id"], e["titre"]))
        for code, txt in ec:
            out.write(u"- **%s** — %s\n" % (code, txt))
        out.write(u"\n")
    out.close()

    struct = [e["id"] for e in corpus
              if [x for x in par_exo[e["id"]] if x[0] in (u"§1", u"§3", u"CHK")]]
    print(json.dumps({
        u"portee": portee,
        u"exercices": len(corpus),
        u"ecarts": len(lignes),
        u"par_regle": tot,
        u"exercices_a_refondre": len(struct),
        u"liste": struct,
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
