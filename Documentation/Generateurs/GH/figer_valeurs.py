# -*- coding: utf-8 -*-
"""Refige la reference de la recette 7. GESTE DELIBERE, jamais routinier.

    python Documentation/Generateurs/GH/client_pont_rhino.py \\
           Documentation/Generateurs/GH/figer_valeurs.py

POURQUOI CE FICHIER EXISTE
--------------------------
Le pont Rhino lit le fichier qu'on lui donne et en execute la source : il ne
transmet PAS d'arguments. `recette_7_valeurs.py --figer` est donc impossible a
lancer a travers lui, et le figeage passait jusqu'ici par un script du
repertoire temporaire.

Ce script-la etait une COPIE INTEGRALE de la recette avec `figer` force a
True. Il a donc fige pendant un temps avec une version perimee du code, sans
que rien ne le signale : une copie ne suit jamais son original. Le figeage
vit desormais dans le projet, il est versionne, et il IMPORTE la recette.

QUAND REFIGER
-------------
- Apres avoir ajoute des exercices : la recette signale « definitions
  nouvelles, a figer ».
- Apres un changement DELIBERE de recette qui modifie une valeur, une fois la
  nouvelle valeur verifiee par le calcul independant.
- Apres un changement de contexte Rhino sur l'un des dix exercices a
  geometrie ajustee, l'ecart etant de quelques ppm — voir l'en-tete de
  `recette_7_valeurs.py`.

QUAND NE PAS REFIGER
--------------------
Devant un ecart qu'on ne s'explique pas. Refiger efface le signal : la valeur
fausse devient la reference, et le controle ne dira plus jamais rien. C'est le
seul geste de toute la chaine qui puisse DESARMER un controle.
"""
import sys

try:
    import os
    _ICI = os.path.dirname(os.path.abspath(__file__))
except NameError:
    _ICI = r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH"
    import os
_GEN = os.path.abspath(os.path.join(_ICI, ".."))
for _p in (_ICI, _GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# Le pont execute tous les scripts dans la MEME session Rhino, et `sys.argv`
# y survit d'un script a l'autre. Un « --figer » laisse derriere ferait
# REFIGER tout controle lance ensuite, au lieu de comparer : la base est donc
# nettoyee avant, et restauree apres.
_ARGV = [x for x in sys.argv if x != "--figer"]

# L'importer sous son VRAI nom : le module se lance de lui-meme quand il est
# charge sous un autre, par la garde `if __name__ != "recette_7_valeurs"`.
import recette_7_valeurs as R7

sys.argv = list(_ARGV) + ["--figer"]
try:
    R7.main()
finally:
    sys.argv = _ARGV
