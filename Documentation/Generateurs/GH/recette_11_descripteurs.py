# -*- coding: utf-8 -*-
"""Recette 11 — le descripteur dit-il la meme chose que le registre ?

    python Documentation/Generateurs/GH/recette_11_descripteurs.py

Chaque exercice existe DEUX fois : dans le registre Python, et dans son
`.json` livre a cote de la definition. Le second est la source de tout ce qui
consomme le referentiel sans lancer Python.

Ils se separent facilement, parce qu'ils ne se regenerent pas ensemble :

    registre  ->  fiche .md, .docx, .pdf, classeur, application HTML
                  par `finaliser.py`, qui tourne en CPython
    registre  ->  descripteur .json
                  par le CONSTRUCTEUR, qui ne tourne que dans Rhino

Corriger un enonce et rejouer `finaliser.py` met donc tout a jour SAUF le
`.json`. C'est arrive le 10/09/2026 : le materiel de depart d'A-12 etait
corrige partout, et son descripteur annonçait encore « les 28 epaisseurs ».
Le site disait une chose, le fichier livre une autre.

Rien ne comparait ces deux-la. `verifier_fraicheur.py` compare des DATES : il
signale les 49 descripteurs du lot A des que `skill_a.py` bouge, qu'ils aient
change ou non. Il crie donc trop, et pour cette raison on cesse de l'ecouter.
Cette recette compare le CONTENU, et ne nomme que ce qui differe vraiment.

CE QU'ELLE NE COMPARE PAS
-------------------------
Les champs que le constructeur calcule lui-meme — chemins de fichiers, version,
nom de la skill — n'ont pas de contrepartie dans le registre. Le mapping
ci-dessous est celui de `ecrire_json()` dans `build_lots_nouveaux.py` ; il est
volontairement limite aux champs qui portent du SENS pedagogique.
"""
import io
import json
import os
import sys

try:
    ICI = os.path.dirname(os.path.abspath(__file__))
except NameError:
    ICI = r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH"
GEN = os.path.abspath(os.path.join(ICI, ".."))
PROJET = os.path.abspath(os.path.join(GEN, "..", ".."))
for _p in (ICI, GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from lots import TOUS, LOTS

#: clef du descripteur -> clef du registre. Repris de `ecrire_json()`.
CHAMPS = [
    (u"titre", u"titre"),
    (u"enonce", u"enonce"),
    (u"donnees_de_depart", u"depart"),
    (u"resultat_attendu", u"att"),
    (u"mode_validation", u"mode"),
    (u"niveau", u"niv"),
    (u"thematique", u"them"),
    (u"competence_visee", u"competence"),
    (u"case_bloom", u"bloom"),
    (u"contexte_metier", u"contexte"),
    (u"erreur_attendue", u"erreur"),
    (u"question_charniere", u"charniere"),
    (u"justification_donnees", u"donnees_note"),
    (u"limite_correction", u"limite"),
]


def descripteurs():
    """eid -> chemin du .json, en JOIGNANT le dossier qui existe.

    Piege : `lots.dossier_de(eid)` rend le dossier du LOT, pas celui de
    l'exercice. Les exercices du lot A vivent dans des dossiers a titre long,
    les autres dans un dossier portant le seul identifiant. On parcourt donc.
    """
    index = {}
    for _code, _nom, rel, _lot in LOTS:
        racine = os.path.join(PROJET, rel.replace(u"/", os.sep))
        if not os.path.isdir(racine):
            continue
        for d in sorted(os.listdir(racine)):
            dd = os.path.join(racine, d)
            if not os.path.isdir(dd):
                continue
            eid = d.split(u" ")[0]
            p = os.path.join(dd, u"%s.json" % eid)
            if os.path.isfile(p):
                index[eid] = p
    return index


def main():
    lg = 74
    print("=" * lg)
    print(u"RECETTE 11 — descripteur .json contre registre")
    print("=" * lg)

    index = descripteurs()
    ecarts, sans = [], []
    for e in TOUS:
        p = index.get(e["id"])
        if not p:
            sans.append(e["id"])
            continue
        j = json.loads(io.open(p, encoding="utf-8").read())
        for cj, cr in CHAMPS:
            a = (u"%s" % (j.get(cj) or u"")).strip()
            b = (u"%s" % (e.get(cr) or u"")).strip()
            if a != b:
                ecarts.append((e["id"], cj, a, b))

    print(u"%d exercices au registre, %d descripteurs trouvés"
          % (len(TOUS), len(index)))
    print(u"  %-42s %d" % (u"sans descripteur (livrable non graphique)",
                           len(sans)))
    print(u"  %-42s %d" % (u"CHAMPS DIVERGENTS", len(ecarts)))
    for eid, champ, a, b in ecarts:
        print(u"      %-7s %s" % (eid, champ))
        print(u"              json = %s" % a[:62])
        print(u"              reg  = %s" % b[:62])
    print("-" * lg)
    if ecarts:
        print(u"Le registre a bougé sans que le descripteur soit reconstruit.")
        print(u"Reconstruire dans Rhino :")
        print(u"   python Documentation/Generateurs/GH/client_pont_rhino.py \\")
        print(u"          Documentation/Generateurs/GH/build_tout.py")
    else:
        print(u"Chaque descripteur dit ce que dit le registre.")
    print("=" * lg)
    return 0 if not ecarts else 1


if __name__ == "__main__":
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                      errors="replace")
    except Exception:
        pass
    sys.exit(main())
