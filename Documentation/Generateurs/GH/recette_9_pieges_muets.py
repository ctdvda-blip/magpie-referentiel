# -*- coding: utf-8 -*-
"""Recette 9 — l'erreur attendue produit-elle une AUTRE valeur ?

    python Documentation/Generateurs/GH/recette_9_pieges_muets.py

La skill exige que l'erreur anticipee mene a un resultat DIFFERENT du bon.
Sinon l'apprenant se trompe et l'exercice le valide : le piege ne diagnostique
rien, et la fiche promet un enseignement qu'elle ne tient pas.

Sept jeux de donnees ont du etre recalibres pour cette raison pendant la
production — B-14, B-15, C-08, C-12, G-08, PL-15, IA-32 — mais tous ont ete
trouves EN CONCEVANT, jamais en relisant. Cette recette cherche les autres.

TROIS FAUX POSITIFS, ET POURQUOI ILS LE SONT
--------------------------------------------
Le controle lit les nombres de `att` et de `erreur`, et signale ceux qui
coincident. Il ne sait pas distinguer :

1. UN PARAMETRE D'UN RESULTAT. A-34 : « prendre 40 pour l'apotheme au lieu du
   rayon » — 40 est la donnee du fourreau, pas la reponse fausse.
2. UN MEME COMPTE POUR DES CONTENUS DIFFERENTS. A-14 : le motif decale rend
   « encore 12 lames, mais pas les memes ». La reponse est une LISTE ordonnee,
   que le checker distingue ; la fiche l'explique elle-meme.
3. UNE ERREUR CONCEPTUELLE SUR UNE VALEUR JUSTE. B-13 : annoncer 31 % comme le
   taux reel alors que c'est un minorant. Le nombre est bon, son
   interpretation ne l'est pas.

Ces trois-la sont EXEMPTES, avec leur motif. Ajouter une exemption est un
geste delibere : il faut avoir lu la fiche et conclu que le piege parle.

LES ERREURS SANS CHIFFRE NE SONT PAS UN DEFAUT
----------------------------------------------
Soixante-deux erreurs attendues ne portent aucun nombre alors que la reponse
en porte un. Relecture faite, ce sont des ERREURS DE METHODE : « le montage
donne la bonne reponse aujourd'hui et la mauvaise des que le debit change »,
« desigher les cercles a la main : le montage cesse de suivre ». Par nature
elles n'ont pas de valeur fausse a opposer, et la skill les admet. Elles sont
comptees, pas signalees.
"""
import io
import os
import re
import sys

try:
    ICI = os.path.dirname(os.path.abspath(__file__))
except NameError:
    ICI = r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH"
GEN = os.path.abspath(os.path.join(ICI, ".."))
for _p in (ICI, GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from lots import TOUS

RE_NOMBRE = re.compile(u"[-+]?[0-9][0-9   ]*(?:[.,][0-9]+)?")

#: Exemptions RELUES, avec leur motif. Le controle ne sait pas distinguer un
#: parametre d'un resultat ; ces trois cas ont ete tranches a la lecture.
EXEMPTS = {
    u"A-14": u"le motif décalé rend le même COMPTE mais pas la même liste, "
             u"et la réponse est une liste ordonnée — la fiche le dit",
    u"A-34": u"40 est le rayon du fourreau, une DONNÉE, pas la réponse fausse",
    u"B-13": u"l'erreur est d'interpréter un minorant juste comme un taux "
             u"réel : le nombre est bon, sa lecture ne l'est pas",
}


def nombres(txt):
    """Les nombres ecrits dans un texte, espaces fins et virgules compris."""
    out = []
    for m in RE_NOMBRE.finditer(txt or u""):
        brut = m.group(0)
        for espace in (u" ", u" ", u" "):
            brut = brut.replace(espace, u"")
        try:
            out.append(float(brut.replace(u",", u".")))
        except ValueError:
            pass
    return out


def main():
    lg = 74
    print("=" * lg)
    print(u"RECETTE 9 — l'erreur attendue mène-t-elle à une AUTRE valeur ?")
    print("=" * lg)

    controles = [e for e in TOUS if e.get(u"verdict") != u"connaissance"]
    parlants, methode, muets, exemptes = 0, 0, [], []
    for e in controles:
        err = u"%s" % (e.get(u"erreur") or u"")
        att = u"%s" % (e.get(u"att") or u"")
        if not err.strip():
            muets.append((e["id"], u"aucune erreur attendue", e.get(u"titre")))
            continue
        na, ne = nombres(att), nombres(err)
        if not na or not ne:
            methode += 1
            continue
        bonne = na[0]
        marge = max(1e-9, abs(bonne) * 1e-9)
        if any(abs(x - bonne) > marge for x in ne):
            parlants += 1
        elif e["id"] in EXEMPTS:
            exemptes.append((e["id"], EXEMPTS[e["id"]]))
        else:
            muets.append((e["id"], u"l'erreur donne %s, comme la bonne réponse"
                          % bonne, e.get(u"titre")))

    print(u"%d exercices de compétence contrôlés" % len(controles))
    print(u"  %-42s %d" % (u"piège chiffré et distinct", parlants))
    print(u"  %-42s %d" % (u"erreur de méthode, sans valeur opposable", methode))
    print(u"  %-42s %d" % (u"exemptés après relecture", len(exemptes)))
    print(u"  %-42s %d" % (u"PIÈGE MUET", len(muets)))
    for eid, motif in exemptes:
        print(u"      %-7s exempté : %s" % (eid, motif))
    for eid, motif, titre in muets:
        print(u"      %-7s %s — %s" % (eid, motif, (titre or u"")[:34]))
    print("-" * lg)
    if muets:
        print(u"Un piège muet promet un enseignement que l'exercice ne tient")
        print(u"pas : l'apprenant se trompe, et il est validé. Recalibrer le")
        print(u"jeu de données, ou exempter APRÈS avoir lu la fiche.")
    else:
        print(u"Aucun piège muet : chaque erreur anticipée mène ailleurs.")
    print("=" * lg)
    return 0 if not muets else 1


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    sys.exit(main())
