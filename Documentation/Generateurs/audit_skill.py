# -*- coding: utf-8 -*-
"""Audit du lot A au regard de la skill magpie-conception-exercices v2.3.

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

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

from exos_a import LOT_A

LETTRES = u"A-Za-z0-9À-ſ"
AVANT = u"(?<![" + LETTRES + u"])"
APRES = u"(?![" + LETTRES + u"])"


def borne(mot):
    """Motif « mot entier » sans recourir a une sequence antislash-b."""
    return AVANT + re.escape(mot) + APRES


# --- vocabulaire des composants : tout ce qui est cite en champ `comp` -------
VOCAB = set()
for _e in LOT_A:
    for _c in re.split(u"[,/]", _e["comp"]):
        _c = _c.strip()
        if len(_c) > 2:
            VOCAB.add(_c)

# Noms qui sont aussi des mots courants du francais ou du vocabulaire geometrique :
# les citer dans un enonce ne revele pas l'outil a employer.
GENERIQUES = set(u"""Point Line Curve Surface Number Panel Series Range Text Domain
Plane Vector Circle Box Mesh Group Sort Area Volume Length Angle Move Scale
Rotate Mirror Offset Divide Join Split Trim Extrude Loft Sphere""".split())

TESTABLES = sorted([v for v in VOCAB if v not in GENERIQUES], key=len, reverse=True)

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
    if e["nb"] <= 3:
        d.append((u"§1", u"solution de référence à %d composants : "
                  u"un seul geste suffit" % e["nb"]))

    # ---- §4 : contexte metier
    if not e.get(u"contexte"):
        d.append((u"§4", u"aucun contexte métier"))

    # ---- §5 : donnees devinables
    if not e.get(u"exempt5"):
        if RE_PETIT.search(e["enonce"]) or RE_PETIT.search(e.get("depart", u"")):
            d.append((u"§5", u"jeu de données court ou ordonné, lisible à l'œil"))

    # ---- §6 : erreur attendue
    if not e.get(u"erreur"):
        d.append((u"§6", u"aucune erreur attendue anticipée"))

    # ---- contraintes du checker
    tol = (e["tol"] or u"").replace(u",", u".").strip()
    non_nul = tol not in (u"0", u"—", u"", u"0.0", u"-")
    if e["mode"] == u"SingleValue" and non_nul:
        d.append((u"CHK", u"SingleValue avec tolérance « %s » : "
                  u"la tolérance est ignorée, comparaison à 1e-9" % e["tol"]))
    if e["mode"] == u"GeometryTolerance" and not non_nul:
        d.append((u"CHK", u"GeometryTolerance sans tolérance : retombe sur "
                  u"le 0.001 du document Rhino"))
    if e["mode"] in (u"ExactOrderedList", u"SetEquality") and non_nul:
        d.append((u"CHK", u"%s avec tolérance « %s » : aucune tolérance "
                  u"n'est appliquée dans ce mode" % (e["mode"], e["tol"])))
    return d


def main():
    fusion = u"--fusion" in sys.argv
    corpus = LOT_A
    if fusion:
        from skill_a import fusionner
        corpus = [fusionner(e) for e in LOT_A]

    lignes, tot, par_exo = [], {}, {}
    for e in corpus:
        ec = audit(e)
        par_exo[e["id"]] = ec
        for code, txt in ec:
            lignes.append((e["id"], e["titre"], code, txt))
            tot[code] = tot.get(code, 0) + 1

    nom = u"AUDIT_SKILL_APRES.md" if fusion else u"AUDIT_SKILL.md"
    out = io.open(os.path.join(ICI, nom), "w", encoding="utf-8")
    out.write(u"# Audit du lot A — skill de conception d'exercices Magpie v2.3\n\n")
    out.write(u"49 exercices contrôlés, **%d écarts** relevés.\n\n" % len(lignes))
    out.write(u"| Règle | Écarts | Portée |\n|---|---|---|\n")
    legende = {
        u"§1": u"exercice testant une connaissance plutôt qu'une compétence",
        u"§3": u"nom de composant donné dans la consigne",
        u"§4": u"contexte métier absent",
        u"§5": u"données devinables",
        u"§6": u"erreur attendue non anticipée",
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
        u"exercices": len(LOT_A),
        u"ecarts": len(lignes),
        u"par_regle": tot,
        u"exercices_a_refondre": len(struct),
        u"liste": struct,
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
