# -*- coding: utf-8 -*-
"""Ce que la fiche APPRENANT annonce comme resultat attendu.

Le champ `att` d'un exercice sert deux lecteurs a la fois, et c'est la source
d'un defaut : sur les exercices de comptage, il donne la VALEUR — « 11, le
nombre de traverses hors tolerance » — et la fiche remise a l'apprenant lui
livre donc la reponse avant qu'il ait rien monte.

Ce module separe les deux lectures :

    att          la valeur      -> fiche formateur, zone corrige
    att_sujet    la nature      -> fiche apprenant, zone sujet

L'apprenant a besoin de savoir CE QU'IL DOIT PRODUIRE — un compte, une liste
ordonnee, une surface en metres carres — pas ce que cela vaut. C'est aussi ce
que la skill demande : l'exercice mesure une competence, et il ne la mesure
plus des lors que la reponse est ecrite sur l'enonce.

Les exercices absents de ce module gardent leur `att` : leur formulation decrit
deja une nature et non une valeur.

VERSION : v0.1-260828
"""

VERSION = u"v0.1-260828"

ATT_SUJET = {

# --- lot A ------------------------------------------------------------------
u"A-08": u"Un nombre entier : combien de traverses sortent de la tolérance.",
u"A-09": u"Un nombre entier : combien de hauteurs sont réellement "
         u"renseignées.",
u"A-10": u"La liste ordonnée des abscisses des axes, en millimètres, du "
         u"premier au dernier.",
u"A-13": u"La liste ordonnée des numéros de repère, du plus long débit au "
         u"plus court.",
u"A-14": u"La liste ordonnée des longueurs des lames réellement posées.",
u"A-15": u"Un nombre entier : combien de panneaux partent en pose à deux.",
u"A-17": u"La liste ordonnée des longueurs, dans l'ordre de pose du plateau.",
u"A-19": u"Un nombre entier : combien de branches compte le flux.",
u"A-30": u"Un nombre entier : combien de chutes repartent en stock.",
u"A-35": u"Autant de cercles de 5 de rayon que la consigne en demande, "
         u"perpendiculaires au tracé en chacune de leurs positions.",
u"A-39": u"Les deux ensembles demandés : la trame rectangulaire et la "
         u"couronne, chacun au complet.",

# --- lot IA -----------------------------------------------------------------
u"IA-01": u"Un nombre entier : combien de platines sortent de la tolérance. "
          u"Il doit sortir du composant produit par l'assistant, non d'un "
          u"comptage à la main.",
u"IA-03": u"Un nombre : l'amplitude du relevé, en millimètres.",
u"IA-04": u"Une valeur décimale : la surface développée totale, en mètres "
          u"carrés.",
u"IA-05": u"Un nombre entier : combien de tronçons dépassent la longueur de "
          u"transport. Le composant fourni en annonce un autre.",
u"IA-06": u"La liste ordonnée des sommes cumulées, telle que la produit le "
          u"composant d'origine.",
u"IA-12": u"Une valeur décimale : la longueur cumulée, en millimètres.",
u"IA-14": u"Une valeur décimale : le volume exact de l'assemblage, dans "
          u"l'unité du modèle. Le composant fourni en annonce un autre.",

# --- lot RH -----------------------------------------------------------------
u"RH-02": u"Un nombre entier : combien de points portent le calque des "
          u"porteurs, une fois le tri fait.",
u"RH-03": u"Un nombre entier : combien de plots compte la trame.",
u"RH-05": u"Une valeur : le volume de matière retirée, en millimètres cubes.",

# --- lots avances -----------------------------------------------------------
u"AV-01": u"Un nombre entier : combien de bissections ont été nécessaires "
          u"pour atteindre le critère.",
u"AV-03": u"Un nombre entier : combien de panneaux au minimum.",
}


def pour_apprenant(e):
    """Ce que la fiche apprenant annonce. A defaut, le `att` d'origine."""
    return ATT_SUJET.get(e.get("id"), e.get("att", u""))


def fuite(e):
    """Vrai si le `att` de cet exercice livrerait la reponse a l'apprenant."""
    return e.get("id") in ATT_SUJET
