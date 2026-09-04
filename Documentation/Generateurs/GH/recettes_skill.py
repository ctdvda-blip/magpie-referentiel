# -*- coding: utf-8 -*-
"""Correctifs des recettes de construction, issus de la skill de conception.

Les recettes d'origine (recipes_a1..a4) restent intactes : ce module les
modifie APRES chargement, pour que la version anterieure demeure lisible et
comparable. build_lot_a.py appelle appliquer(RECETTES) juste apres la fusion
des quatre modules.

Deux natures de correctif :

1. Les jeux de donnees (§5 de la skill) : listes longues, non ordonnees, non
   devinables. La source unique est skill_a.py — jamais recopiee ici.
2. Le graphe du corrige, quand la tache elle-meme a change : A-08 compare
   desormais un ecart en valeur absolue, A-15 et A-30 renvoient un comptage et
   non plus une liste de booleens (que le checker refuse).
"""
import os
import sys

_GEN = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
if _GEN not in sys.path:
    sys.path.insert(0, _GEN)

import skill_a as S


def _data(rec, cle, valeurs, nick=None):
    """Remplace la charge d'un noeud de donnees de la zone sujet."""
    for i, n in enumerate(rec["sujet"]):
        if n[0] == cle:
            o = dict(n[4])
            o["data"] = valeurs
            if nick:
                o["nick"] = nick
            rec["sujet"][i] = (n[0], n[1], n[2], n[3], o)
            return True
    return False


def _type_reponse(rec, typ):
    for i, n in enumerate(rec["sujet"]):
        if n[0] == "rep":
            o = dict(n[4])
            o["type"] = typ
            rec["sujet"][i] = (n[0], n[1], n[2], n[3], o)
            return True
    return False


def appliquer(R):
    """Applique les correctifs. Retourne la liste des identifiants touches."""
    faits = []

    # ---------------- donnees seules -------------------------------------
    if "A-09" in R:
        _data(R["A-09"], "data", list(S.D_A09), u"RELEVE_ALLEGES")
        faits.append("A-09")


    # ---------------- A-11 : une seule liste en reponse -------------------
    # Le checker compare une liste unique. L'exercice demande deux longueurs :
    # elles doivent donc etre reunies avant d'atteindre la reponse, sans quoi
    # seule la derniere est validee.
    if "A-11" in R:
        R["A-11"] = dict(
            sujet=[
                ("data", "DATA:Number", 0, 0,
                 {"nick": u"LONGUEURS_DEBIT", "data": list(S.D_A11)}),
                ("rep", "REPONSE", 5, 0, {"type": "Number"}),
            ],
            corrige=[
                (u"Atteindre la piece du quatrieme rang : les rangs "
                 u"commencent a zero, le quatrieme porte donc l'indice 3", [
                    ("li1", "List Item", 1, 0, {"val": [(1, "Integer", [3])]}),
                    ("pan1", "PANEL", 2, 0, {}),
                ]),
                (u"Atteindre la derniere piece sans coder son rang en dur : "
                 u"mesurer la liste, puis retrancher un", [
                    ("ll", "List Length", 1, 2, {}),
                    ("sub", "Subtraction", 2, 2, {"val": [(1, "Number", [1])]}),
                    ("li2", "List Item", 3, 2, {}),
                    ("pan2", "PANEL", 4, 2, {}),
                ]),
                (u"Reunir les deux longueurs en une liste unique : le "
                 u"controle compare une liste, pas deux sorties", [
                    ("mg", "Merge", 4, 0, {}),
                    ("pan3", "PANEL", 5, 1, {}),
                ]),
            ],
            wires=[("data", "li1", 0), ("li1", "pan1", 0),
                   ("data", "ll", 0), ("ll", "sub", 0),
                   ("data", "li2", 0), ("sub", "li2", 1),
                   ("li2", "pan2", 0),
                   ("li1", "mg", 0), ("li2", "mg", 1),
                   ("mg", "pan3", 0), ("mg", "rep", 0)],
        )
        faits.append("A-11")

    if "A-12" in R:
        _data(R["A-12"], "data", list(S.D_A12), u"EPAISSEURS")
        faits.append("A-12")

    if "A-14" in R:
        _data(R["A-14"], "data", list(S.D_A14), u"CALEPINAGE_PLEIN")
        faits.append("A-14")

    if "A-18" in R:
        _data(R["A-18"], "data", list(S.D_A18), u"RELEVES_ALTI")
        faits.append("A-18")

    # ---------------- A-13 : reperes numeriques, plus de texte -----------
    if "A-13" in R:
        r = R["A-13"]
        _data(r, "noms", list(S.D_A13_REP), u"REPERES")
        _data(r, "lg", list(S.D_A13_LONG), u"LONGUEURS")
        _type_reponse(r, "Number")
        faits.append("A-13")

    # ---------------- A-17 : longueurs, plus de texte --------------------
    if "A-17" in R:
        r = R["A-17"]
        _data(r, "l1", list(S.D_A17_LG_CHENE), u"CHENE")
        _data(r, "l2", list(S.D_A17_LG_NOYER), u"NOYER")
        _type_reponse(r, "Number")
        faits.append("A-17")

    # ---------------- A-08 : ecart en valeur absolue a la cote nominale --
    # La tache n'est plus « compter au-dessus d'un seuil » mais « compter les
    # cotes hors tolerance », ce qui impose de passer par un ecart absolu.
    if "A-08" in R:
        R["A-08"] = dict(
            sujet=[
                ("data", "DATA:Number", 0, 0,
                 {"nick": u"COTES_RELEVEES", "data": list(S.D_A08)}),
                ("nom", "SLIDER", 0, 1,
                 {"slider": (1000, 1400, 1200, 0), "nick": u"Nominale"}),
                ("tol", "SLIDER", 0, 2,
                 {"slider": (0, 20, 5, 0), "nick": u"Tolerance"}),
                ("rep", "REPONSE", 5, 0, {"type": "Number"}),
            ],
            corrige=[
                (u"Ramener chaque cote a son ecart par rapport a la nominale", [
                    ("sub", "Subtraction", 1, 0, {}),
                ]),
                (u"Prendre la valeur absolue : un ecart de -8 est aussi "
                 u"hors tolerance qu'un ecart de +8", [
                    ("abs", "Absolute", 2, 0, {}),
                ]),
                (u"Comparer a la tolerance : on obtient une liste de booleens", [
                    ("lt", "Larger Than", 3, 0, {}),
                ]),
                (u"Sommer les booleens : True vaut 1, False vaut 0", [
                    ("ma", "Mass Addition", 4, 0, {}),
                    ("pan", "PANEL", 5, 1, {}),
                ]),
            ],
            wires=[("data", "sub", 0), ("nom", "sub", 1),
                   ("sub", "abs", 0), ("abs", "lt", 0), ("tol", "lt", 1),
                   ("lt", "ma", 0), ("ma", "pan", 0), ("ma", "rep", 0)],
        )
        faits.append("A-08")

    # ---------------- A-15 : la reponse devient un comptage ---------------
    # Le checker refuse une liste de booleens ; on conserve la separation en
    # deux groupes (la competence visee) et l'on chiffre le groupe demande.
    if "A-15" in R:
        R["A-15"] = dict(
            sujet=[
                ("data", "DATA:Number", 0, 0,
                 {"nick": u"SURFACES_M2", "data": list(S.D_A15)}),
                ("rep", "REPONSE", 5, 0, {"type": "Number"}),
            ],
            corrige=[
                (u"Comparer chaque surface au seuil de pose a deux", [
                    ("sl", "SLIDER", 1, 1,
                     {"slider": (0, 5, 2.5, 2), "nick": u"Seuil"}),
                    ("lt", "Larger Than", 2, 0, {}),
                ]),
                (u"Separer les panneaux en deux groupes : la competence "
                 u"visee est bien la separation, pas le seul comptage", [
                    ("disp", "Dispatch", 3, 0, {}),
                    ("pan1", "PANEL", 4, 0, {}),
                    ("pan2", "PANEL", 4, 2, {}),
                ]),
                (u"Chiffrer le groupe a poser en binome", [
                    ("ll", "List Length", 4, 4, {}),
                    ("pan3", "PANEL", 5, 4, {}),
                ]),
            ],
            wires=[("data", "lt", 0), ("sl", "lt", 1),
                   ("data", "disp", 0), ("lt", "disp", 1),
                   ("disp", "pan1", 0), ("disp", "pan2", 0),
                   ("disp", "ll", 0), ("ll", "pan3", 0), ("ll", "rep", 0)],
        )
        faits.append("A-15")

    # ---------------- A-30 : la reponse devient un comptage ---------------
    if "A-30" in R:
        R["A-30"] = dict(
            sujet=[
                ("data", "DATA:Number", 0, 0,
                 {"nick": u"LONGUEURS_CHUTES", "data": list(S.D_A30)}),
                ("rep", "REPONSE", 6, 0, {"type": "Number"}),
            ],
            corrige=[
                (u"Premier test : la chute atteint-elle la borne basse ? "
                 u"Bornes incluses, il faut un test large", [
                    ("s1", "SLIDER", 1, 1,
                     {"slider": (0, 2000, 500, 0), "nick": u"Mini"}),
                    ("ge", "Larger Than", 2, 0, {}),
                ]),
                (u"Second test : la chute reste-t-elle sous la borne haute ?", [
                    ("s2", "SLIDER", 1, 3,
                     {"slider": (0, 2000, 1500, 0), "nick": u"Maxi"}),
                    ("le", "Smaller Than", 2, 2, {}),
                ]),
                (u"Les deux conditions doivent etre vraies ensemble", [
                    ("ga", "Gate And", 3, 0, {}),
                    ("pan", "PANEL", 4, 2, {}),
                ]),
                (u"Sommer les booleens pour obtenir le nombre de chutes "
                 u"remises en stock", [
                    ("ma", "Mass Addition", 4, 0, {}),
                    ("pan2", "PANEL", 5, 0, {}),
                ]),
            ],
            # Sortie 1 des comparateurs = « ou egal ». La sortie 0 est
            # stricte et donnerait 14 au lieu de 16 : c'est exactement
            # l'erreur que le jeu de donnees est concu pour reveler.
            wires=[("data", "ge", 0), ("s1", "ge", 1),
                   ("data", "le", 0), ("s2", "le", 1),
                   ("ge", 1, "ga", 0), ("le", 1, "ga", 1),
                   ("ga", "pan", 0), ("ga", "ma", 0),
                   ("ma", "pan2", 0), ("ma", "rep", 0)],
        )
        faits.append("A-30")

    # ---------------- A-19 : la reponse est un NOMBRE de branches ---------
    # L'enonce demande combien de branches compte le flux ; la recette
    # renvoyait le chemin de la troisieme branche, c'est-a-dire du texte, que
    # le checker refuse.
    if "A-19" in R:
        r = R["A-19"]
        _type_reponse(r, "Number")
        r["wires"] = [("tree", "ts", 0), ("ts", 1, "ll", 0),
                      ("ll", "pan", 0), ("ll", "rep", 0)]
        r["corrige"] = [
            (u"La statistique d'arbre donne la liste des chemins", [
                ("ts", "Tree Statistics", 1, 0, {}),
            ]),
            (u"Compter les chemins donne le nombre de branches : c'est un "
             u"nombre, pas un chemin. Le chemin de la troisieme branche "
             u"serait du texte, et le controle ne compare que des nombres.", [
                ("ll", "List Length", 2, 0, {}),
                ("pan", "PANEL", 3, 0, {}),
            ]),
        ]
        faits.append("A-19")

    # ---------------- A-43 : la preuve est le VOLUME, pas un booleen -------
    # Un booleen branche sur la verification echoue. Le volume est la preuve
    # numerique du caractere ferme : nul si l'enveloppe est ouverte.
    if "A-43" in R:
        r = R["A-43"]
        _type_reponse(r, "Number")
        r["corrige"] = [
            (u"Refermer les ouvertures planes", [
                ("cap", "Cap Holes", 1, 0, {}),
            ]),
            (u"Le volume EST la preuve : une enveloppe ouverte n'en a pas. "
             u"Inutile de le traduire en booleen — le controle compare des "
             u"nombres, et un booleen brancherait dans le vide.", [
                ("vo", "Volume", 2, 0, {}),
                ("pan", "PANEL", 3, 0, {}),
            ]),
        ]
        r["wires"] = [("brp", "cap", 0), ("cap", "vo", 0),
                      ("vo", "pan", 0), ("vo", "rep", 0)]
        faits.append("A-43")

    return faits
