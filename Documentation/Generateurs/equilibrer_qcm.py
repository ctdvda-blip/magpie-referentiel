# -*- coding: utf-8 -*-
"""Repartit la bonne reponse des questions charnieres sur les quatre positions.

DEFAUT CORRIGE
--------------
Sur 22 questions charnieres, 18 avaient leur bonne reponse en position b. Un
apprenant qui coche toujours b obtenait 82 % sans rien savoir : le score varie
alors sans que la competence varie — ce que Messick nomme variance non
pertinente au construit, et que la skill signale explicitement.

CE QUE FAIT CE MODULE
---------------------
Il permute les propositions pour amener la bonne reponse a une position visee :

  1. il relit les quatre propositions et repere celle qui porte la marque ;
  2. il la deplace a la position visee, les autres gardant leur ordre relatif ;
  3. il reetiquette a, b, c, d ;
  4. il REECRIT les references de lettres du commentaire diagnostique —
     « (a) et (d) revelent que… » — sans quoi ce commentaire designerait les
     mauvaises propositions apres permutation.

Le point 4 est le seul delicat : c'est lui qui interdit une permutation naive.

La permutation se fait A L'EXECUTION, au moment ou une fiche est rendue. Les
modules source gardent leur redaction d'origine : leurs propositions y sont
coupees sur plusieurs litteraux, ce qui rendait toute reecriture textuelle du
source fragile — un premier essai n'en avait retrouve que dix sur vingt-deux.
"""
import re
import sys
import os

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

LETTRES = [u"a", u"b", u"c", u"d"]
MARQUE = u"← réponse"

RE_PROP = re.compile(u"^([a-d])[)] (.*)$")
RE_REF = re.compile(u"[(]([a-d])[)]")

#: position visee pour chaque question, choisie pour equilibrer l'ensemble
#: sur les quatre lettres plutot que de laisser 18 reponses en b.
CIBLES = {
    # Ces quatre-la portent DEJA un menu deroulant dans leur definition .gh,
    # dont l'ordre et l'indice de bonne reponse sont figes. Les permuter dans
    # la fiche seule desynchroniserait les deux supports : on les laisse ou
    # ils sont, et l'equilibrage porte sur les dix-huit autres.
    u"A-26": u"c", u"IA-02": u"a", u"IA-08": u"b", u"IA-13": u"c",

    # Les quatre charnieres de la vague d'equilibrage. Elles etaient
    # redigees avec leur bonne reponse en b ou en a ; on les envoie ou la
    # repartition en manque, soit trois en c et une en d.
    u"DV-05": u"c", u"DV-06": u"c", u"IA-16": u"c", u"IA-18": u"d",

    # Les quatre charnieres de la vague 2. Avec elles la serie compte
    # trente questions : on vise sept ou huit par lettre.
    u"PL-10": u"a", u"PL-11": u"d", u"IA-24": u"b", u"PL-12": u"b",

    # Les quatre charnieres de la vague 3. La serie compte trente-quatre
    # questions : on vise huit ou neuf par lettre.
    u"GP-10": u"c", u"AV-06": u"a", u"AV-09": u"c", u"FA-05": u"d",

    u"A-03": u"a", u"A-05": u"b", u"A-06": u"d", u"A-07": u"a",
    u"A-24": u"b", u"A-29": u"d",
    u"RH-01": u"a", u"RH-06": u"d", u"RH-07": u"b", u"RH-10": u"a",
    u"GP-04": u"d", u"PL-01": u"b", u"PL-02": u"a", u"PL-04": u"d",
    u"MP-03": u"c", u"DV-01": u"b", u"DV-03": u"d", u"WB-03": u"a",
}


def decouper(txt):
    """Separe (preambule, propositions, commentaire)."""
    lignes = txt.split(u"\n")
    deb = fin = None
    for i, l in enumerate(lignes):
        if RE_PROP.match(l.strip()):
            if deb is None:
                deb = i
            fin = i
    if deb is None:
        return None
    return lignes[:deb], lignes[deb:fin + 1], lignes[fin + 1:]


def permuter(props, cible):
    """Amene la bonne reponse a `cible`. Retourne (propositions, mapping)."""
    autres, bonne = [], None
    for l in props:
        m = RE_PROP.match(l.strip())
        if not m:
            return None, None
        if MARQUE in m.group(2):
            bonne = (m.group(1), m.group(2))
        else:
            autres.append((m.group(1), m.group(2)))
    if bonne is None or len(autres) != 3:
        return None, None

    ordre, reste = [], list(autres)
    for pos in LETTRES:
        ordre.append(bonne if pos == cible else reste.pop(0))

    mapping, sorties = {}, []
    for i, (ancienne, texte) in enumerate(ordre):
        mapping[ancienne] = LETTRES[i]
        sorties.append(u"%s) %s" % (LETTRES[i], texte))
    return sorties, mapping


def traiter(txt, cible):
    """Retourne (texte permute, a-t-il change)."""
    d = decouper(txt)
    if not d:
        return txt, False
    avant, props, apres = d
    neuves, mapping = permuter(props, cible)
    if neuves is None or neuves == props:
        return txt, False
    apres = [RE_REF.sub(lambda m: u"(%s)" % mapping.get(m.group(1), m.group(1)), l)
             for l in apres]
    return u"\n".join(avant + neuves + apres), True


def charniere_equilibree(e):
    """La question charniere, sa bonne reponse amenee a la position visee."""
    txt = e.get(u"charniere") or u""
    cible = CIBLES.get(e.get("id"))
    if not txt or not cible:
        return txt
    return traiter(txt, cible)[0]


def repartition(equilibre=True):
    """Ou tombe la bonne reponse, avant ou apres equilibrage."""
    import collections
    from lots import TOUS
    pos = collections.Counter()
    for e in TOUS:
        if not e.get(u"charniere"):
            continue
        txt = charniere_equilibree(e) if equilibre else e[u"charniere"]
        for l in txt.split(u"\n"):
            m = RE_PROP.match(l.strip())
            if m and MARQUE in l:
                pos[m.group(1)] += 1
    return dict(sorted(pos.items()))


def controle():
    """Verifie qu'aucun commentaire ne designe une proposition inexistante."""
    from lots import TOUS
    soucis = []
    for e in TOUS:
        if not e.get(u"charniere"):
            continue
        txt = charniere_equilibree(e)
        d = decouper(txt)
        if not d:
            continue
        lettres = set()
        for l in d[1]:
            m = RE_PROP.match(l.strip())
            if m:
                lettres.add(m.group(1))
        for l in d[2]:
            for ref in RE_REF.findall(l):
                if ref not in lettres:
                    soucis.append((e["id"], ref))
    return soucis


def main():
    print(u"Avant  : %s" % repartition(equilibre=False))
    print(u"Après  : %s" % repartition(equilibre=True))
    s = controle()
    print(u"Références de lettres incohérentes : %d" % len(s))
    for eid, ref in s[:8]:
        print(u"  %s renvoie à (%s)" % (eid, ref))
    return 0


if __name__ == "__main__":
    sys.exit(main())
