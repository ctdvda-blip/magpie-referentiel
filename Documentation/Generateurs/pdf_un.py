# -*- coding: utf-8 -*-
"""Convertit UNE fiche Word en PDF, sur une instance de Word neuve.

Sert aux deux documents que la conversion en serie ecarte parce qu'ils l'ont
fait geler : A-13 et A-38. Les reprendre seuls, sur une instance qui n'a rien
converti avant eux, permet de savoir si le blocage tient au document ou a la
degradation de l'automatisation Word au fil des conversions.

    python Documentation/Generateurs/pdf_un.py "<chemin du .docx>"

L'appelant doit poser un delai de garde : un appel COM qui gele ne rend jamais
la main, et aucune protection interne ne peut l'interrompre. Sous Git Bash :

    timeout 180 python Documentation/Generateurs/pdf_un.py "<chemin>"

Comme le reste de la chaine, le script emploie DispatchEx et non Dispatch : il
travaille sur une instance ISOLEE, et ne touche jamais aux documents ouverts
par l'utilisateur.
"""
import io
import os
import shutil
import sys
import tempfile

import pythoncom
import win32com.client as w32

WD_PDF = 17


def convertir_par_copie(docx, pdf=None):
    """Convertit une COPIE placee ailleurs, puis ramene le PDF a sa place.

    Word tient une liste de documents qu'il refuse d'ouvrir — la cle de
    registre Word\\Resiliency\\DisabledItems — alimentee des qu'un document
    l'a fait planter ou geler une fois. Le refus prend la forme d'une boite de
    dialogue ; avec Visible = False, elle n'a nulle part ou s'afficher, et
    l'appel COM ne rend jamais la main. Le document, lui, est intact : la meme
    copie s'ouvre en une demi-seconde sous un autre chemin, parce que la liste
    est indexee par CHEMIN.

    C'est ce qui bloquait A-13 et A-38 depuis trois sessions.

    Nettoyer la liste demande de toucher au registre de l'utilisateur : ce
    n'est pas a ce script de le faire. Passer par une copie contourne le refus
    sans rien modifier chez personne.
    """
    if pdf is None:
        pdf = docx[:-5] + ".pdf"
    tmp = tempfile.mkdtemp(prefix="magpie_pdf_")
    try:
        copie = os.path.join(tmp, "fiche.docx")
        shutil.copy2(docx, copie)
        produit = convertir(copie, os.path.join(tmp, "fiche.pdf"))
        if not os.path.isfile(produit):
            return None
        shutil.copy2(produit, pdf)
        return pdf
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def convertir(docx, pdf=None):
    if pdf is None:
        pdf = docx[:-5] + ".pdf" if docx.lower().endswith(".docx") else docx + ".pdf"
    pythoncom.CoInitialize()
    app = w32.DispatchEx("Word.Application")
    app.Visible = False
    app.DisplayAlerts = 0
    doc = None
    try:
        doc = app.Documents.Open(docx, ReadOnly=True, AddToRecentFiles=False)
        doc.ExportAsFixedFormat(pdf, WD_PDF)
    finally:
        try:
            if doc is not None:
                doc.Close(False)
        except Exception:
            pass
        try:
            app.Quit()          # l'instance isolee, jamais celle de l'utilisateur
        except Exception:
            pass
    return pdf


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    par_copie = "--copie" in sys.argv
    docx = os.path.abspath(args[0])
    if not os.path.isfile(docx):
        print(u"Introuvable : %s" % docx)
        return 1
    pdf = convertir_par_copie(docx) if par_copie else convertir(docx)
    if os.path.isfile(pdf):
        print(u"écrit : %s (%d Ko)" % (pdf, os.path.getsize(pdf) // 1024))
        return 0
    print(u"aucun PDF produit")
    return 1


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.exit(main())
