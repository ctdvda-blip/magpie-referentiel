# -*- coding: utf-8 -*-
"""Lance TOUTES les recettes, et dit lesquelles n'ont pas pu l'etre.

    python Documentation/Generateurs/GH/recettes.py

Il y a dix recettes, ecrites au fil des defauts trouves. Rien ne les lançait
ensemble : on se souvenait des unes, on oubliait les autres, et une recette
qu'on oublie ne controle rien. Ce script les DECOUVRE — `recette_*.py`, triees
par numero — plutot que de les enumerer. Une liste tenue a la main se
decouple en silence ; ce projet l'a paye sept fois.

DEUX FAMILLES, DEUX VERDICTS
----------------------------
Trois recettes (8, 9, 10) lisent le registre en CPython : elles rendent un code
de sortie, et ce script en tire un verdict.

Sept recettes (1 a 7) ouvrent les definitions dans Grasshopper. Elles passent
par le pont TCP, s'executent en IronPython dans la session Rhino, et n'ont pas
de ligne de verdict commune : chacune imprime son propre tableau. Ce script
RELAIE leur sortie sans l'interpreter. Pretendre en deduire un verdict par
lecture de mots-clefs serait inventer un couplage de plus.

QUAND LE PONT EST FERME
-----------------------
Les sept recettes Rhino ne sont pas executees, et ce script le DIT, nommement.
Une verification non faite doit se voir ; c'est tout l'objet du fichier.
Ouvrir Rhino, puis y taper `MCPStart`.
"""
import io
import os
import re
import socket
import subprocess
import sys

try:
    ICI = os.path.dirname(os.path.abspath(__file__))
except NameError:
    ICI = r"C:\Users\charl\.claude\projects\MAGPIE\Documentation\Generateurs\GH"
PROJET = os.path.abspath(os.path.join(ICI, "..", "..", ".."))

RE_RECETTE = re.compile(r"^recette_(\d+)_.+\.py$")

#: Ce qui trahit une recette qui a besoin de Grasshopper : elle charge
#: l'assembly, ou l'API Rhino. C'est LU dans la source, pas declare a la main.
MARQUES_RHINO = ("clr.AddReference", "import Rhino", "import scriptcontext")


def recettes():
    """Les recettes trouvees sur le disque, dans l'ordre de leur numero."""
    out = []
    for nom in os.listdir(ICI):
        m = RE_RECETTE.match(nom)
        if not m:
            continue
        src = io.open(os.path.join(ICI, nom), encoding="utf-8").read()
        out.append((int(m.group(1)), nom,
                    any(marque in src for marque in MARQUES_RHINO)))
    return sorted(out)


def pont_ouvert():
    s = socket.socket()
    s.settimeout(2)
    try:
        s.connect(("127.0.0.1", 1999))
        return True
    except Exception:
        return False
    finally:
        s.close()


def lancer(argv):
    p = subprocess.Popen(argv, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, cwd=PROJET)
    sortie = p.communicate()[0].decode("utf-8", "replace")
    return p.returncode, sortie


def main():
    lg = 74
    ouvert = pont_ouvert()
    verdicts, relayees, sautees = [], [], []

    for num, nom, rhino in recettes():
        chemin = os.path.join(ICI, nom)
        if not rhino:
            code, sortie = lancer([sys.executable, chemin])
            print(sortie.rstrip())
            print("")
            verdicts.append((num, nom, code))
        elif ouvert:
            code, sortie = lancer([sys.executable,
                                   os.path.join(ICI, "client_pont_rhino.py"),
                                   chemin])
            print(sortie.rstrip())
            print("")
            relayees.append((num, nom, code))
        else:
            sautees.append((num, nom))

    print("=" * lg)
    print(u"BILAN DES RECETTES")
    print("=" * lg)
    for num, nom, code in verdicts:
        print(u"  recette %-3d %-34s %s"
              % (num, nom, u"OK" if code == 0 else u"ÉCART (code %d)" % code))
    for num, nom, code in relayees:
        etat = (u"sortie relayée ci-dessus, verdict à lire"
                if code == 0 else u"PONT EN ERREUR")
        print(u"  recette %-3d %-34s %s" % (num, nom, etat))
    if sautees:
        print("-" * lg)
        print(u"NON EXÉCUTÉES — le pont Rhino est fermé (127.0.0.1:1999) :")
        for num, nom in sautees:
            print(u"      recette %-3d %s" % (num, nom))
        print(u"Ouvrez Rhino, tapez MCPStart, puis relancez ce script.")
    print("=" * lg)

    if any(c for _n, _f, c in verdicts):
        return 1
    return 2 if sautees else 0


if __name__ == "__main__":
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                      errors="replace")
    except Exception:
        pass
    sys.exit(main())
