# -*- coding: utf-8 -*-
"""Prepare la copie de publication du referentiel.

La publication n'est pas le projet : c'est une COPIE, montee ailleurs, dont la
forme differe sur trois points.

1. LES DOSSIERS SONT PLATS. Dans le projet, un exercice du lot A vit dans
   « A-12 Longueur et bornes d'une liste » ; la copie le nomme « A-12 ». Les
   titres complets faisaient depasser la limite de 260 caracteres de Windows
   des que le depot etait clone un cran plus profond, et `git add` echouait.

2. L'INDEX EST REGENERE POUR CETTE ARBORESCENCE. L'application du projet
   pointe vers les dossiers longs ; celle de la publication vers les courts.
   D'ou --plat, et --livrables qui lui donne la racine ou verifier ce qui
   existe reellement, de sorte qu'elle ne propose au telechargement que des
   fichiers presents.

3. L'ENTREE EST GARDEE. Le mot de passe n'est PAS ecrit dans la page : elle ne
   porte qu'une empreinte PBKDF2. Il se donne en argument, une fois, au moment
   de la construction — jamais dans un fichier du depot.

   CONSEQUENCE A CONNAITRE : le SEL est tire au hasard a chaque construction.
   index.html apparait donc modifie a chaque publication, meme quand rien n'a
   bouge — une seule ligne differe, celle du sel et de l'empreinte. Avant de
   commiter un index seul, verifier par `git diff` que c'est bien de cela
   qu'il s'agit, et rendre le fichier a son etat precedent si oui : republier
   450 Ko pour un sel neuf n'apporte rien.

Usage :

    python Documentation/Generateurs/publier.py <dossier de publication> \\
           --protege "LOGIN:MOTDEPASSE"

Le dossier de publication est mis a jour en place : son .git est preserve, les
fichiers obsoletes sont retires, le reste est recopie. Rien n'est commite ni
pousse — c'est a l'appelant de relire, puis de decider.
"""
import hashlib
import json
import io
import os
import shutil
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PROJET = os.path.abspath(os.path.join(ICI, "..", ".."))

sys.path.insert(0, ICI)
from lots import LOTS

#: ce qui accompagne les exercices, a la racine de la publication
ANNEXES = ["README.md", "SKILL.md",
           "Fondamentaux Grasshopper - IndC - 01-09-2026.xlsx"]

#: python porteur d'openpyxl : le generateur d'application en depend
PY_OPENPYXL = r"C:\Users\charl\AppData\Local\Programs\Python\Python37\python.exe"


def dossier_source(racine, eid):
    """Le dossier d'un exercice, nomme par son seul identifiant ou suivi de
    son titre selon le lot."""
    if not os.path.isdir(racine):
        return None
    for d in sorted(os.listdir(racine)):
        if d == eid or d.startswith(eid + " "):
            p = os.path.join(racine, d)
            if os.path.isdir(p):
                return p
    return None


#: fichiers dont deux constructions successives different toujours, a contenu
#: pourtant identique : Grasshopper reattribue des GUID a chaque ecriture, et
#: python-docx comme Word horodatent l'interieur du fichier. Les recopier a
#: chaque publication ajouterait une centaine de mega-octets a l'historique du
#: depot pour trois exercices reellement modifies.
VOLATILS = (".gh", ".docx", ".pdf")

#: fichiers deterministes : ils ne changent que si le contenu change. Ce sont
#: donc EUX qui disent si un exercice a bouge.
TEMOINS = ("%s_fiche.md", "%s_fiche_sujet.md", "%s.json")


def signature(dossier, eid):
    """Empreinte du contenu logique d'un exercice.

    Le descripteur .json est relu et resérialisé clefs triees avant d'entrer
    dans l'empreinte : les fichiers deja publies l'ont ete dans un ordre de
    clefs arbitraire, et les comparer tels quels ferait passer pour modifies
    99 exercices qui ne le sont pas.
    """
    h = hashlib.sha256()
    for motif in TEMOINS:
        p = os.path.join(dossier, motif % eid)
        if not os.path.isfile(p):
            continue
        fh = open(p, "rb")
        try:
            brut = fh.read()
        finally:
            fh.close()
        if p.endswith(".json"):
            try:
                brut = json.dumps(json.loads(brut.decode("utf-8")),
                                  sort_keys=True).encode("utf-8")
            except Exception:
                pass
        h.update(brut)

    # Les illustrations entrent aussi dans l'empreinte, par leur inventaire :
    # un exercice dont la definition vient d'etre construite recoit ses canvas
    # SANS que sa fiche Markdown change d'un caractere — la fiche Word, elle,
    # les incorpore. Sans cette ligne, RH-04 et AV-02 seraient restes publies
    # dans leur version sans images.
    ill = os.path.join(dossier, "Illustrations")
    if os.path.isdir(ill):
        for rep, _d, fichiers in os.walk(ill):
            for f in sorted(fichiers):
                q = os.path.join(rep, f)
                h.update(os.path.relpath(q, ill).encode("utf-8"))
                h.update(str(os.path.getsize(q)).encode("utf-8"))
    return h.hexdigest()


def _copier_si_different(src, dst):
    if os.path.isfile(dst) and os.path.getsize(dst) == os.path.getsize(src):
        a = open(src, "rb").read()
        b = open(dst, "rb").read()
        if a == b:
            return False
    d = os.path.dirname(dst)
    if not os.path.isdir(d):
        os.makedirs(d)
    shutil.copy2(src, dst)
    return True


def copier_exercice(src, dst, eid):
    """Met a jour un exercice publie. Retourne (repris, fichiers touches).

    Si les temoins sont inchanges, l'exercice n'a pas bouge : ses fichiers
    volatils publies sont conserves tels quels, et seuls les fichiers
    deterministes reellement differents sont recopies.
    """
    intact = os.path.isdir(dst) and signature(src, eid) == signature(dst, eid)
    touches = 0
    presents = set()
    for rep, _dirs, fichiers in os.walk(src):
        rel = os.path.relpath(rep, src)
        for f in fichiers:
            relf = os.path.normpath(os.path.join(rel, f))
            presents.add(relf)
            if intact and os.path.splitext(f)[1].lower() in VOLATILS \
                    and os.path.isfile(os.path.join(dst, relf)):
                continue
            if _copier_si_different(os.path.join(src, relf),
                                    os.path.join(dst, relf)):
                touches += 1
    # ce que la publication porte encore et que la source ne produit plus
    if os.path.isdir(dst):
        for rep, _dirs, fichiers in os.walk(dst):
            rel = os.path.relpath(rep, dst)
            for f in fichiers:
                relf = os.path.normpath(os.path.join(rel, f))
                if relf not in presents:
                    os.remove(os.path.join(dst, relf))
                    touches += 1
    return intact, touches


def copier_exercices(cible):
    n, intacts, touches = 0, 0, 0
    attendus = set()
    for _code, _nom, rel, lot in LOTS:
        racine = os.path.join(PROJET, rel.replace("/", os.sep))
        dest_lot = os.path.join(cible, rel.replace("/", os.sep))
        for e in lot:
            src = dossier_source(racine, e["id"])
            if src is None:
                continue
            dst = os.path.join(dest_lot, e["id"])
            attendus.add(os.path.normpath(dst))
            inchange, t = copier_exercice(src, dst, e["id"])
            n += 1
            touches += t
            intacts += 1 if inchange else 0
    # exercices retires du referentiel : leur dossier publie n'a plus lieu d'etre
    exos = os.path.join(cible, "EXERCICES")
    if os.path.isdir(exos):
        for lot_dir in sorted(os.listdir(exos)):
            p = os.path.join(exos, lot_dir)
            if not os.path.isdir(p):
                continue
            for d in sorted(os.listdir(p)):
                q = os.path.normpath(os.path.join(p, d))
                if os.path.isdir(q) and q not in attendus:
                    shutil.rmtree(q)
    return n, intacts, touches


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    cible = os.path.abspath(args[0])
    if not os.path.isdir(cible):
        os.makedirs(cible)

    protege = None
    if "--protege" in sys.argv:
        k = sys.argv.index("--protege")
        if k + 1 < len(sys.argv):
            protege = sys.argv[k + 1]
    if not protege:
        print(u"Il manque --protege \"LOGIN:MOTDEPASSE\".")
        return 2

    print(u"Publication vers : %s" % cible)
    n, intacts, touches = copier_exercices(cible)
    print(u"  exercices publiés, dossiers aplatis : %d" % n)
    print(u"  inchangés depuis la dernière publication : %d" % intacts)
    print(u"  fichiers réellement réécrits            : %d" % touches)

    for nom in ANNEXES:
        src = os.path.join(PROJET, nom)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(cible, nom))
            print(u"  annexe : %s" % nom)

    index = os.path.join(cible, "index.html")
    cmd = [PY_OPENPYXL, os.path.join(ICI, "gen_application.py"),
           "--plat", index, "--livrables", cible, "--protege", protege]
    r = subprocess.call(cmd)
    if r != 0:
        print(u"  génération de l'index en échec (code %d)" % r)
        return 1
    print(u"  index : %s (%d Ko)" % (index, os.path.getsize(index) // 1024))
    print(u"Prêt. Relisez, puis commitez et poussez depuis ce dossier.")
    return 0


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    sys.exit(main())
