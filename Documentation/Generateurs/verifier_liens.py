# -*- coding: utf-8 -*-
"""Verifie que chaque telechargement propose par l'application existe vraiment.

L'application ne construit pas ses liens en dur : elle les fabrique en
JavaScript a partir d'un objet `dispo` calcule a la generation, qui dit pour
chaque exercice quels fichiers sont presents. Chercher des `href` dans la page
ne trouve donc rien d'utile — il faut relire cet objet, et confronter ce qu'il
annonce a ce que le dossier contient reellement.

C'est ce controle-la qui attrape le decalage dangereux : une page generee
depuis le projet, puis publiee a cote d'une arborescence differente. Elle
promet alors des fichiers que personne ne trouvera.

    python Documentation/Generateurs/verifier_liens.py <dossier de publication>
"""
import io
import json
import os
import re
import sys

# Les donnees ne sont pas une affectation JavaScript : elles sont deposees
# dans une balise <script type="application/json" id="donnees">, que la page
# relit par JSON.parse. C'est cette balise qu'on rouvre ici.
RE_DONNEES = re.compile(
    r'<script[^>]*id="donnees"[^>]*>(.*?)</script>', re.S)

#: clef du dictionnaire `dispo` -> nom de fichier attendu dans le dossier
FICHIERS = {
    u"pdf": u"%s_fiche.pdf",
    u"docx": u"%s_fiche.docx",
    u"docx_sujet": u"%s_fiche_sujet.docx",
    u"gh_sujet": u"%s_sujet.gh",
    u"gh_complet": u"%s_complet.gh",
    u"images": u"Illustrations/web/%s_canvas_sujet.jpg",
}


def donnees(index):
    html = io.open(index, encoding="utf-8").read()
    m = RE_DONNEES.search(html)
    if not m:
        raise SystemExit(u"Données introuvables dans %s" % index)
    return json.loads(m.group(1).replace(u"<\\/", u"</"))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    racine = os.path.abspath(sys.argv[1])
    index = sys.argv[2] if len(sys.argv) > 2 else os.path.join(racine, "index.html")
    D = donnees(index)
    exos = D.get("exos") or []

    promis, morts, muets = 0, [], []
    for e in exos:
        dossier = os.path.join(racine, e["racine"].replace("/", os.sep), e["id"])
        dispo = e.get("dispo") or {}
        rien = True
        for cle, motif in FICHIERS.items():
            if not dispo.get(cle):
                continue
            rien = False
            promis += 1
            chemin = os.path.join(dossier, (motif % e["id"]).replace("/", os.sep))
            if not os.path.isfile(chemin):
                morts.append(u"%s : %s" % (e["id"], motif % e["id"]))
        if rien:
            muets.append(e["id"])

    print(u"Exercices publiés        : %d" % len(exos))
    print(u"Téléchargements promis   : %d" % promis)
    print(u"Promis mais absents      : %d" % len(morts))
    for m in morts[:25]:
        print(u"   %s" % m)
    print(u"Sans aucun livrable      : %d %s"
          % (len(muets), ", ".join(muets)))
    return 0 if not morts else 1


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    sys.exit(main())
