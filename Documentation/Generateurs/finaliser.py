# -*- coding: utf-8 -*-
"""Termine la refonte pour les fichiers qui etaient ouverts dans Excel ou Word.

Deux livrables n'ont pas pu etre reecrits pendant la refonte du 26/08/2026,
parce qu'ils etaient ouverts sur le poste :

  - Fondamentaux Grasshopper - IndB - 26-08-2026.xlsx   (ouvert dans Excel)
  - A-13_fiche.docx et A-13_fiche.pdf                   (ouvert dans Word)

Fermez ces deux documents, puis lancez :

    python Documentation/Generateurs/finaliser.py

Le script ne ferme JAMAIS une application de l'utilisateur : il se contente de
verifier que les fichiers sont libres, et s'arrete proprement sinon.
"""
import os
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PROJET = os.path.abspath(os.path.join(ICI, "..", ".."))
CLASSEUR = os.path.join(PROJET, "Fondamentaux Grasshopper - IndB - 26-08-2026.xlsx")
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

    print(u"2 · Fiches Markdown")
    lancer("gen_fiches.py", "os", u"Fiches Markdown")
    print(u"")

    print(u"3 · Vignettes web des captures de canvas")
    lancer("gen_vignettes.py", "PIL", u"Vignettes")
    print(u"")

    if word_ok:
        print(u"4 · Fiches Word")
        lancer("gen_fiches_docx.py", "docx", u"Fiches Word")
        print(u"")
        print(u"5 · Conversion PDF (chaque fiche passe par Word : comptez "
              u"une dizaine de minutes)")
        lancer("gen_pdf.py", "win32com.client", u"Conversion PDF")
    else:
        print(u"4-5 · Fiches Word et PDF — IGNORÉS : A-13_fiche.docx est encore "
              u"ouvert dans Word.")
        restant.append(u"la fiche A-13")
    print(u"")

    print(u"6 · Application HTML")
    lancer("gen_application.py", "openpyxl", u"Application HTML")
    print(u"")

    if restant:
        print(u"RESTE À FAIRE : %s. Fermez le document puis relancez ce script."
              % u", ".join(restant))
        return 1

    print(u"7 · Contrôle de fraîcheur des livrables")
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
