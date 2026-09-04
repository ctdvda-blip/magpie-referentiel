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


def _vagues():
    """Les exercices ajoutes par les vagues d'equilibrage, par code de lot.

    Ils vivent a part plutot que dans les modules de domaine : une vague se
    lit, se relit et se recette comme un tout, et melangee au reste elle
    deviendrait invisible. Le registre les rattache a leur lot au chargement,
    de sorte que tous les generateurs les voient sans rien savoir d'eux.

    Les modules sont DECOUVERTS. La liste tenue a la main ici etait la
    septieme du projet a pouvoir decrocher de ce qu'elle couvrait : une vague
    ajoutee sans y penser serait restee invisible partout, y compris des
    controles.

    Deux formes sont acceptees : des attributs `LOT_XX`, comme les premieres
    vagues les ecrivaient, ou une liste plate dont chaque exercice porte son
    lot dans son identifiant.
    """
    import os
    ici = os.path.dirname(os.path.abspath(__file__))
    par_lot = {}
    for fichier in sorted(os.listdir(ici)):
        if not (fichier.startswith("exercices_vague") and fichier.endswith(".py")):
            continue
        nom = fichier[:-3]
        try:
            m = __import__(nom)
        except Exception as ex:
            print("  (%s non chargé : %s)" % (nom, ex))
            continue
        vus = False
        for attribut in dir(m):
            if attribut.startswith("LOT_"):
                par_lot.setdefault(attribut[4:], []).extend(getattr(m, attribut))
                vus = True
        if vus:
            continue
        for attribut in dir(m):
            if attribut.startswith("_") or not attribut.isupper():
                continue
            valeur = getattr(m, attribut)
            if not isinstance(valeur, list) or not valeur:
                continue
            if not isinstance(valeur[0], dict) or "id" not in valeur[0]:
                continue
            for e in valeur:
                par_lot.setdefault(e["id"].split("-")[0], []).append(e)
    return par_lot


# ---------------------------------------------------------------------------
# Normalisation des thematiques
# ---------------------------------------------------------------------------

#: Cinq libelles disaient la meme chose de deux facons. Le vocabulaire retenu
#: est celui du REFERENTIEL : c'est lui qui fait autorite, et l'application
#: groupe par thematique — deux libelles pour un sujet coupaient un groupe en
#: deux sans raison.
ALIAS_THEMES = {
    u"Types, conversion et valeurs": u"Types et conversion implicite",
    u"Organisation du document": u"Organisation du document Rhino",
    u"Organisation et lisibilité": u"Organisation et performance",
    u"Performance d'exécution": u"Organisation et performance",
    u"Principes": u"Écosystème de plugins",
}


def _normaliser_themes(exercices):
    """Donne a chaque thematique un numero unique DANS SON LOT.

    Huit lots portaient des numeros contradictoires : le meme numero pour deux
    sujets, et le meme sujet sous deux numeros. L'application groupe par cette
    clef, et un groupe se coupait donc en deux sans raison visible.

    La numerotation est DEDUITE et non ecrite : les libelles sont ranges par
    le plus petit numero qu'ils portaient, puis par ordre alphabetique pour
    departager. Ce choix preserve la numerotation existante partout ou elle
    etait deja coherente, et ne bouge que ce qui se contredisait.
    """
    par_lot = {}
    for e in exercices:
        lot = e["id"].split("-")[0]
        brut = u"%s" % (e.get(u"them") or u"")
        if u" · " not in brut:
            continue
        numero, libelle = brut.split(u" · ", 1)
        libelle = ALIAS_THEMES.get(libelle, libelle)
        try:
            n = int(numero[len(lot):])
        except ValueError:
            n = 99
        connus = par_lot.setdefault(lot, {})
        connus[libelle] = min(connus.get(libelle, 99), n)

    rang = {}
    for lot, libelles in par_lot.items():
        ordre = sorted(libelles.items(), key=lambda kv: (kv[1], kv[0]))
        for i, (libelle, _ancien) in enumerate(ordre, 1):
            rang[(lot, libelle)] = i

    for e in exercices:
        brut = u"%s" % (e.get(u"them") or u"")
        if u" · " not in brut:
            continue
        lot = e["id"].split("-")[0]
        libelle = ALIAS_THEMES.get(brut.split(u" · ", 1)[1],
                                   brut.split(u" · ", 1)[1])
        e[u"them"] = u"%s%d · %s" % (lot, rang[(lot, libelle)], libelle)
    return exercices


VAGUES = _vagues()


def _ajouts(code):
    return [dict(e) for e in VAGUES.get(code, [])]


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
                     u"EXERCICES/LOT A - Composants natifs",
                     fusionne + _ajouts(u"A")))
    except Exception as ex:
        print("  (lot A non chargé : %s)" % ex)

    # --- lot B : algorithmes combines --------------------------------------
    # Meme montage que le lot A : le contenu d'origine (exos_b.py) reste
    # intact, la couche pedagogique se superpose.
    try:
        from exos_b import LOT_B as _BRUT_B
        from skill_b import fusionner as _fus_b
        fus_b = []
        for b_ in _BRUT_B:
            e = _fus_b(b_)
            e[u"enonce_origine"] = b_["enonce"]
            fus_b.append(e)
        lots.append((u"B", u"Algorithmes combinés",
                     u"EXERCICES/LOT B - Algorithmes combines", fus_b))
    except Exception as ex:
        print("  (lot B non chargé : %s)" % ex)

    # --- lot C : projets appliques -----------------------------------------
    try:
        from exos_b import LOT_C as _BRUT_C
        from skill_c import fusionner as _fus_c
        fus_c = []
        for c_ in _BRUT_C:
            e = _fus_c(c_)
            e[u"enonce_origine"] = c_["enonce"]
            fus_c.append(e)
        lots.append((u"C", u"Projets appliqués",
                     u"EXERCICES/LOT C - Projets appliques", fus_c))
    except Exception as ex:
        print("  (lot C non chargé : %s)" % ex)

    # --- lot G : exercices gamifies ----------------------------------------
    try:
        from exos_g import LOT_G as _BRUT_G
        from skill_g import fusionner as _fus_g
        fus_g = []
        for g_ in _BRUT_G:
            e = _fus_g(g_)
            e[u"enonce_origine"] = g_["enonce"]
            fus_g.append(e)
        lots.append((u"G", u"Exercices gamifiés",
                     u"EXERCICES/LOT G - Exercices gamifies", fus_g))
    except Exception as ex:
        print("  (lot G non chargé : %s)" % ex)

    # --- lot IA ------------------------------------------------------------
    try:
        from domaine_ia import LOT_IA
        lots.append((u"IA", u"IA et assistance générative",
                     u"EXERCICES/LOT IA - IA et assistance generative",
                     [dict(e) for e in LOT_IA] + _ajouts(u"IA")))
    except Exception as ex:
        print("  (lot IA non chargé : %s)" % ex)

    # --- lot RH : socle Rhino ---------------------------------------------
    try:
        from domaine_rhino import LOT_RH
        lots.append((u"RH", u"Socle Rhino",
                     u"EXERCICES/LOT RH - Socle Rhino",
                     [dict(e) for e in LOT_RH] + _ajouts(u"RH")))
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
                         [dict(e) for e in lot] + _ajouts(code)))
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
                         [dict(e) for e in lot] + _ajouts(code)))
    except Exception as ex:
        print("  (lots avancés non chargés : %s)" % ex)

    return lots


LOTS = _charger()

#: tous les exercices, tous lots confondus
TOUS = _normaliser_themes([e for _c, _n, _d, lot in LOTS for e in lot])

#: identifiant d'exercice -> dossier du lot auquel il appartient
DOSSIER = {}
for _c, _n, _d, _lot in LOTS:
    for _e in _lot:
        DOSSIER[_e["id"]] = _d

#: exercices pour lesquels une recette de construction .gh existe. On interroge
#: les recettes elles-memes plutot qu'une liste de lots : dans les lots
#: recents, une partie seulement des exercices en a une, et signaler les autres
#: comme manquants serait faux.
def _avec_definitions():
    """Les exercices pour lesquels une recette de construction existe.

    La liste des modules de recettes etait ecrite a la main, et elle a
    decroche TROIS fois — a chaque vague ajoutee. L'application annoncait
    alors 93 definitions quand il y en avait 142, puis 142 quand il y en avait
    160, sans que rien ne le signale : un compte faux ne leve pas d'erreur.

    Elle est donc DECOUVERTE : tout fichier `recipes_*.py` du dossier GH qui
    expose un dictionnaire `R` compte. Ajouter une vague suffit.
    """
    ids = set()
    gh = os.path.join(ICI, "GH")
    if gh not in sys.path:
        sys.path.insert(0, gh)
    if not os.path.isdir(gh):
        return ids
    for f in sorted(os.listdir(gh)):
        if not (f.startswith("recipes_") and f.endswith(".py")):
            continue
        try:
            m = __import__(f[:-3])
            ids |= set(getattr(m, "R", {}))
        except Exception:
            continue
    return ids


AVEC_DEFINITIONS = _avec_definitions()

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
