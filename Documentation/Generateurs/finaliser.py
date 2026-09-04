# -*- coding: utf-8 -*-
"""Rejoue toute la chaine de generation, dans l'ordre.

C'est le script que designe `verifier_fraicheur.py` quand il trouve un livrable
perime. Il regenere, dans l'ordre des dependances : classeur du referentiel,
descripteurs, fiches Markdown, vignettes, fiches Word, PDF, cahier des charges,
couverture et application. Il termine par le controle de fraicheur, de sorte
qu'il DIT s'il a reussi au lieu de le laisser supposer.

Ce qu'il ne fait pas : construire les definitions .gh. Elles se batissent dans
Rhino, par le pont TCP, et ne peuvent donc pas etre lancees d'ici :

    cd Documentation/Generateurs/GH
    python client_pont_rhino.py build_lots_nouveaux.py

DOCUMENTS OUVERTS
-----------------
Le script ne ferme JAMAIS une application de l'utilisateur. Il verifie que
chaque livrable est libre, saute proprement ceux qui ne le sont pas, et nomme
a la fin ce qui reste a reprendre. Un classeur ouvert dans Excel ne doit pas
empecher les fiches d'aboutir.

    python Documentation/Generateurs/finaliser.py

TROIS INTERPRETEURS
-------------------
Les dependances ne sont pas installees dans le meme Python : openpyxl en 3.7,
python-docx et Pillow en 3.14, pywin32 en 3.11. Chaque etape va donc chercher
l'interpreteur qui fournit ce dont elle a besoin.
"""
import os
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PROJET = os.path.abspath(os.path.join(ICI, "..", ".."))
CLASSEUR = os.path.join(PROJET, "Fondamentaux Grasshopper - IndC - 01-09-2026.xlsx")
LOT = os.path.join(PROJET, "EXERCICES", "LOT A - Composants natifs")


CANDIDATS = [
    sys.executable,
    r"C:/Users/charl/AppData/Local/Programs/Python/Python311/python.exe",
    r"C:/Users/charl/AppData/Local/Programs/Python/Python314/python.exe",
    r"C:/Users/charl/AppData/Local/Programs/Python/Python37/python.exe",
    "py",
]


def interpreteur(module):
    """Trouve un interpreteur ou `module` s'importe.

    Les dependances ne sont pas installees dans le meme Python : openpyxl est
    en 3.7, python-docx en 3.14, pywin32 en 3.11. Lancer tout avec
    sys.executable echouerait sur deux etapes sur quatre.
    """
    for exe in CANDIDATS:
        try:
            r = subprocess.call([exe, "-c", "import " + module],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if r == 0:
                return exe
        except Exception:
            continue
    return None


def lancer(script, module, titre):
    exe = interpreteur(module)
    if exe is None:
        print(u"   %s : IMPOSSIBLE — aucun interpréteur ne fournit « %s »."
              % (titre, module))
        return False
    subprocess.call([exe, os.path.join(ICI, script)])
    return True


def libre(chemin):
    if not os.path.exists(chemin):
        return True
    try:
        fh = open(chemin, "r+b")
        fh.close()
        return True
    except (PermissionError, IOError):
        return False


def a13():
    for d in os.listdir(LOT):
        if d.startswith("A-13"):
            return os.path.join(LOT, d, "A-13_fiche.docx")
    return None


def main():
    """Fait tout ce qui n'est pas bloque, et dit precisement ce qui reste.

    Un fichier encore ouvert ne doit pas empecher le reste d'aboutir : on
    traite chaque livrable independamment.
    """
    doc = a13()
    excel_ok = libre(CLASSEUR)
    word_ok = doc is None or libre(doc)
    restant = []

    if excel_ok:
        print(u"1 · Référentiel Excel — ajout des colonnes Nature pédagogique "
              u"et Exercices Magpie")
        lancer("build_fusion.py", "openpyxl", u"Référentiel Excel")
    else:
        print(u"1 · Référentiel Excel — IGNORÉ : le classeur est encore ouvert "
              u"dans Excel.")
        restant.append(u"le classeur du référentiel")
    print(u"")

    print(u"2 · Descripteurs .json — forme canonique et version courante")
    lancer("normaliser_json.py", "json", u"Descripteurs")
    lancer("propager_version.py", "json", u"Version des descripteurs")
    print(u"")

    print(u"3 · Fiches Markdown")
    lancer("gen_fiches.py", "os", u"Fiches Markdown")
    print(u"")

    print(u"4 · Vignettes web des captures de canvas")
    lancer("gen_vignettes.py", "PIL", u"Vignettes")
    print(u"")

    if word_ok:
        print(u"5 · Fiches Word")
        lancer("gen_fiches_docx.py", "docx", u"Fiches Word")
        print(u"")
        print(u"6 · Conversion PDF — chaque fiche passe par Word. Comptez une "
              u"demi-heure pour la série complète ; les documents que Word "
              u"refuse d'ouvrir sont repris par copie temporaire.")
        lancer("gen_pdf.py", "win32com.client", u"Conversion PDF")
    else:
        print(u"5-6 · Fiches Word et PDF — IGNORÉS : une fiche est encore "
              u"ouverte dans Word.")
        restant.append(u"la fiche ouverte dans Word")
    print(u"")

    print(u"7 · Cahier des charges")
    lancer("gen_cdc.py", "os", u"Cahier des charges")
    print(u"")

    print(u"8 · Couverture du référentiel")
    lancer("couverture.py", "openpyxl", u"Couverture")
    print(u"")

    print(u"9 · Application HTML")
    lancer("gen_application.py", "openpyxl", u"Application HTML")
    print(u"")


    if restant:
        print(u"RESTE À FAIRE : %s. Fermez le document puis relancez ce script."
              % u", ".join(restant))
        return 1

    print(u"10 · Contrôle de fraîcheur des livrables")
    exe = interpreteur("os")
    code = subprocess.call([exe, os.path.join(ICI, "verifier_fraicheur.py")])
    print(u"")
    if code != 0:
        print(u"La chaîne s'est interrompue : des livrables sont périmés. "
              u"Relancez ce script.")
        return 1
    print(u"Terminé. Autres contrôles disponibles :")
    print(u"  python Documentation/Generateurs/audit_skill.py --fusion")
    print(u"  python Documentation/Generateurs/controle_reponses.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
