# -*- coding: utf-8 -*-
"""
MAGPIE - Production du LOT A (49 exercices, 98 fichiers .gh).
=============================================================

MODE D'EMPLOI
-------------
1. Ouvrir Rhino 8, puis ouvrir Grasshopper au moins une fois (Ctrl+Alt+G)
   afin que le catalogue de composants soit chargé.
2. Dans Rhino : Outils > Editeur de scripts (_ScriptEditor), langage Python 3.
3. Ouvrir ce fichier et l'exécuter.

Le script commence par un CONTROLE A BLANC de tous les noms de composants
employés. S'il signale des composants introuvables, corriger les recettes
avant de lancer la production : rien n'est écrit tant que le contrôle échoue,
sauf si FORCER vaut True.

Sortie : <PROJET>/EXERCICES/LOT A - Composants natifs/<ID>/
             <ID>_sujet.gh
             <ID>_complet.gh
             <ID>.json
             Ressources/<ID>_ressources.3dm   (si l'exercice en requiert)

Version : v0.1-260825 (Ind. A)
"""

import os
import sys
import json

FORCER = False          # True = produire malgré des composants introuvables

ICI = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.abspath(os.path.join(ICI, ".."))          # Documentation/Generateurs
PROJET = os.path.abspath(os.path.join(GEN, "..", ".."))  # racine du projet MAGPIE
SORTIE = os.path.join(PROJET, "EXERCICES", "LOT A - Composants natifs")

for p in (ICI, GEN):
    if p not in sys.path:
        sys.path.insert(0, p)

import gh_engine as E
try:
    reload(E)                       # IronPython
except NameError:
    import importlib
    importlib.reload(E)

from exos_a import LOT_A as _LOT_A_BRUT
from skill_a import fusionner
LOT_A = [fusionner(_e) for _e in _LOT_A_BRUT]
import recipes_a1, recipes_a2, recipes_a3, recipes_a4

RECETTES = {}
for m in (recipes_a1, recipes_a2, recipes_a3, recipes_a4):
    RECETTES.update(m.R)

# Correctifs issus de la skill de conception : jeux de donnees refondus et
# graphes de corrige revus la ou la tache elle-meme a change.
import recettes_skill
_TOUCHES = recettes_skill.appliquer(RECETTES)
print("Recettes corrigees par la skill : %d (%s)"
      % (len(_TOUCHES), ", ".join(_TOUCHES)))


# ------------------------------------------------------------------ assemblage
def assembler():
    """Fusionne les fiches du cahier des charges et les recettes de construction."""
    out, manquantes = [], []
    for f in LOT_A:
        r = RECETTES.get(f["id"])
        if r is None:
            manquantes.append(f["id"])
            continue
        ex = dict(r)
        ex["id"] = f["id"]
        ex["titre"] = f["titre"]
        ex["niv"] = f["niv"]
        ex["duree"] = f["duree"]
        ex["ref"] = f["ref"]
        ex["enonce"] = f["enonce"]
        ex["fiche"] = f
        out.append(ex)
    return out, manquantes


# -------------------------------------------------------------- ressource 3DM
def ecrire_3dm(spec, dossier):
    """spec = (id, nom_de_calque, [(origine, rayon), ...]) -> fichier 3dm."""
    import Rhino
    ident, calque, cercles = spec
    f3 = Rhino.FileIO.File3dm()
    lay = Rhino.DocObjects.Layer()
    lay.Name = calque
    try:
        idx = f3.AllLayers.Add(lay)
    except Exception:
        idx = None
    if not isinstance(idx, int):
        # selon la version de RhinoCommon, Add() ne renvoie pas l'index :
        # on le retrouve en parcourant la table.
        idx = 0
        try:
            for i, l in enumerate(f3.AllLayers):
                if l.Name == calque:
                    idx = l.Index if isinstance(l.Index, int) else i
                    break
        except Exception:
            idx = 0
    attr = Rhino.DocObjects.ObjectAttributes()
    attr.LayerIndex = idx
    for o, r in cercles:
        c = Rhino.Geometry.Circle(
            Rhino.Geometry.Plane(Rhino.Geometry.Point3d(o[0], o[1], o[2]),
                                 Rhino.Geometry.Vector3d(0, 0, 1)), float(r))
        f3.Objects.AddCurve(c.ToNurbsCurve(), attr)
    if not os.path.isdir(dossier):
        os.makedirs(dossier)
    chemin = os.path.join(dossier, "%s_ressources.3dm" % ident)
    f3.Write(chemin, 6)
    return chemin


# ------------------------------------------------------------------ descripteur
def ecrire_json(ex, dossier):
    f = ex["fiche"]
    d = {
        "id": f["id"],
        "titre": f["titre"],
        "lot": "A",
        "thematique": f["them"],
        "reference_referentiel": f["ref"],
        "niveau": f["niv"],
        "duree_cible_minutes": f["duree"],
        "prerequis": f["prereq"],
        "enonce": f["enonce"],
        "donnees_de_depart": f["depart"],
        "resultat_attendu": f["att"],
        "mode_validation": f["mode"],
        "tolerance": f["tol"],
        "nb_composants_reference": f["nb"],
        "parametre_reponse": "REPONSE",
        "fichier_sujet": "%s_sujet.gh" % f["id"],
        "fichier_complet": "%s_complet.gh" % f["id"],
        "fiche": "%s_fiche.md" % f["id"],
        "fiche_sujet": "%s_fiche_sujet.md" % f["id"],
        "ressource_3dm": ("%s_ressources.3dm" % f["id"]) if ex.get("ressource_3dm") else None,
        "reglages_manuels": ex.get("manuel") or [],
        "bareme": f["bareme"],
        # --- champs issus de la skill de conception -----------------------
        "competence_visee": f.get("competence") or "",
        "case_bloom": f.get("bloom") or "",
        "contexte_metier": f.get("contexte") or "",
        "erreur_attendue": f.get("erreur") or "",
        "nature": f.get("verdict") or "competence",
        "question_charniere": f.get("charniere") or "",
        "justification_donnees": f.get("donnees_note") or "",
        "limite_correction": f.get("limite") or "",
        "note_formateur": f.get("alerte") or "",
        "conception": "magpie-conception-exercices v2.3",
        "version": E.VERSION,
    }
    chemin = os.path.join(dossier, "%s.json" % f["id"])
    import io as _io
    for k, v in list(d.items()):
        if isinstance(v, str):
            d[k] = E._u(v)
    fh = _io.open(chemin, "w", encoding="utf-8")
    try:
        # sort_keys : sans lui, IronPython rend les cles dans un ordre qui
        # varie d'une execution a l'autre. Le fichier differait alors a
        # chaque reconstruction sans qu'un seul caractere de CONTENU ait
        # bouge — et la publication recopiait tout pour rien.
        # separators explicite : par defaut, IronPython ecrit « , » avec
        # une espace AVANT le saut de ligne, la ou Python 3 ecrit « , »
        # tout court. Deux ecritures du meme contenu differaient donc de
        # trente-deux espaces invisibles, et la publication recopiait.
        fh.write(E._txt(json.dumps(d, indent=2, ensure_ascii=False,
                                   sort_keys=True,
                                   separators=(",", ": "))))
    finally:
        fh.close()
    return chemin


# ------------------------------------------------------------------ production
def main(dry=False):
    exos, manquantes = assembler()
    print("=" * 74)
    print("MAGPIE - production du LOT A")
    print("=" * 74)
    print("Fiches du cahier des charges : %d" % len(LOT_A))
    print("Recettes de construction     : %d" % len(RECETTES))
    print("Exercices assembles          : %d" % len(exos))
    if manquantes:
        print("!! Sans recette : %s" % ", ".join(manquantes))

    # --- controle a blanc du catalogue
    print("")
    print("- CONTROLE DES NOMS DE COMPOSANTS " + "-" * 40)
    labels = E.labels_utilises(exos)
    intr, ambig, resol = E.check_catalogue(labels)
    print("Noms distincts employes : %d" % len(set(labels)))
    print("")
    print("Resolution retenue pour chaque composant (a relire) :")
    for nom, ou, n in resol:
        marque = "  <-- %d homonymes" % n if n > 1 else ""
        print("   %-26s %-34s%s" % (nom, ou, marque))
    print("")
    if intr:
        print("COMPOSANTS INTROUVABLES (%d) :" % len(intr))
        for nom in intr:
            print("   %s" % nom)
        if not FORCER:
            print("")
            print("Production interrompue. Corriger les recettes, ou passer FORCER a True")
            print("pour produire malgre tout les exercices non concernes.")
            return
    else:
        print("Tous les composants employes ont ete trouves.")

    if dry:
        print("")
        print("Controle a blanc termine : rien n'a ete ecrit.")
        return

    # --- construction
    print("")
    print("- CONSTRUCTION " + "-" * 58)
    ok, ko, avec_manuel = [], [], []
    for ex in exos:
        dossier = os.path.join(SORTIE, u"%s %s" % (E._u(ex["id"]), E._u(ex["titre"])))
        try:
            if ex.get("ressource_3dm"):
                ecrire_3dm(ex["ressource_3dm"], os.path.join(dossier, "Ressources"))
            E.build_exercice(ex, dossier)
            ecrire_json(ex, dossier)
            ok.append(ex["id"])
            if ex.get("manuel"):
                avec_manuel.append(ex["id"])
        except Exception as err:
            ko.append((ex["id"], str(err)))
            print("  %s : ECHEC - %s" % (ex["id"], err))

    # --- rapport
    print("")
    print("=" * 74)
    print("Produits : %d exercices, soit %d fichiers .gh" % (len(ok), 2 * len(ok)))
    if avec_manuel:
        print("Reglages manuels a poser dans : %s" % ", ".join(avec_manuel))
    if ko:
        print("Echecs (%d) :" % len(ko))
        for i, msg in ko:
            print("   %-8s %s" % (i, msg))
    print("Dossier de sortie : %s" % SORTIE)
    print("=" * 74)


if __name__ == "__main__":
    main()
