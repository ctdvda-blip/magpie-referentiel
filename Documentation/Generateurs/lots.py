# -*- coding: utf-8 -*-
"""Registre unique des lots d'exercices.

Un seul endroit ou la liste des lots est declaree. Tous les generateurs —
fiches, cahier des charges, application, couverture, classeur — s'y adressent,
de sorte qu'un lot ajoute apparaisse partout sans qu'on ait a y penser.

Le lot A passe par skill_a.fusionner() : son contenu d'origine est conserve
intact dans exos_a.py, la couche pedagogique se superpose. Les autres lots sont
rediges directement selon la skill et n'ont pas besoin de cette fusion.
"""
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)


def _charger():
    lots = []

    # --- lot A : contenu d'origine + couche pedagogique --------------------
    try:
        from exos_a import LOT_A as _BRUT
        from skill_a import fusionner
        fusionne = []
        for b in _BRUT:
            e = fusionner(b)
            e[u"enonce_origine"] = b["enonce"]
            fusionne.append(e)
        lots.append((u"A", u"Découverte des composants natifs",
                     u"EXERCICES/LOT A - Composants natifs", fusionne))
    except Exception as ex:
        print("  (lot A non chargé : %s)" % ex)

    # --- lot IA ------------------------------------------------------------
    try:
        from domaine_ia import LOT_IA
        lots.append((u"IA", u"IA et assistance générative",
                     u"EXERCICES/LOT IA - IA et assistance generative",
                     [dict(e) for e in LOT_IA]))
    except Exception as ex:
        print("  (lot IA non chargé : %s)" % ex)

    # --- lot RH : socle Rhino ---------------------------------------------
    try:
        from domaine_rhino import LOT_RH
        lots.append((u"RH", u"Socle Rhino",
                     u"EXERCICES/LOT RH - Socle Rhino",
                     [dict(e) for e in LOT_RH]))
    except Exception as ex:
        print("  (lot RH non chargé : %s)" % ex)

    # --- lots metier : geometrie, quantitatifs, fabrication ----------------
    try:
        import domaine_metier as M
        noms = {u"GP": u"Géométrie paramétrique appliquée",
                u"QT": u"Quantitatifs, chiffrage et export",
                u"FA": u"Aide à la fabrication"}
        dossiers = {u"GP": u"EXERCICES/LOT GP - Geometrie parametrique",
                    u"QT": u"EXERCICES/LOT QT - Quantitatifs et export",
                    u"FA": u"EXERCICES/LOT FA - Aide a la fabrication"}
        for code, lot in M.LOTS:
            lots.append((code, noms[code], dossiers[code],
                         [dict(e) for e in lot]))
    except Exception as ex:
        print("  (lots métier non chargés : %s)" % ex)

    # --- lots avances ------------------------------------------------------
    try:
        import domaine_avance as A
        noms = {u"PL": u"Écosystème de plugins",
                u"MP": u"Méthode, performance et évènements",
                u"AV": u"Algorithmique avancée",
                u"DV": u"Développement, scripting et API",
                u"WB": u"Interfaces, web et interopérabilité"}
        dossiers = {u"PL": u"EXERCICES/LOT PL - Ecosysteme de plugins",
                    u"MP": u"EXERCICES/LOT MP - Methode et performance",
                    u"AV": u"EXERCICES/LOT AV - Algorithmique avancee",
                    u"DV": u"EXERCICES/LOT DV - Developpement et API",
                    u"WB": u"EXERCICES/LOT WB - Interfaces et web"}
        for code, lot in A.LOTS:
            lots.append((code, noms[code], dossiers[code],
                         [dict(e) for e in lot]))
    except Exception as ex:
        print("  (lots avancés non chargés : %s)" % ex)

    return lots


LOTS = _charger()

#: tous les exercices, tous lots confondus
TOUS = [e for _c, _n, _d, lot in LOTS for e in lot]

#: identifiant d'exercice -> dossier du lot auquel il appartient
DOSSIER = {}
for _c, _n, _d, _lot in LOTS:
    for _e in _lot:
        DOSSIER[_e["id"]] = _d

#: code de lot -> libelle
LIBELLE = dict((c, n) for c, n, _d, _l in LOTS)


def dossier_de(eid):
    """Dossier du lot contenant cet exercice, ou celui du lot A par defaut."""
    return DOSSIER.get(eid, u"EXERCICES/LOT A - Composants natifs")


if __name__ == "__main__":
    print(u"Lots : %d" % len(LOTS))
    for c, n, d, lot in LOTS:
        comp = sum(1 for e in lot if e.get(u"verdict") != u"connaissance")
        print(u"  %-3s %-42s %2d items (%2d compétences, %d charnières)"
              % (c, n[:42], len(lot), comp, len(lot) - comp))
    print(u"Total : %d exercices" % len(TOUS))
