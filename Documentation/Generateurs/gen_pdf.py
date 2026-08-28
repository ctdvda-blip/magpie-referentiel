# -*- coding: utf-8 -*-
"""Convertit les fiches Word du lot A en PDF.

PRECAUTION IMPORTANTE
---------------------
L'utilisateur a des documents ouverts dans Word. On ne se rattache donc JAMAIS
a sa session : DispatchEx demarre un processus Word distinct, invisible, que
l'on est seul a piloter et que l'on est donc seul a fermer. La session de
l'utilisateur n'est ni sollicitee, ni modifiee, ni fermee.

Les fichiers verrouilles (ouverts dans Word par l'utilisateur) sont ignores et
signales, jamais forces.
"""
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PROJET = os.path.abspath(os.path.join(ICI, "..", ".."))
from lots import LOTS as _REGISTRE
SORTIES = [os.path.join(PROJET, d.replace("/", os.sep))
        for _c, _n, d, _l in _REGISTRE]
SORTIE = SORTIES[0]

WD_FORMAT_PDF = 17


def main():
    try:
        import win32com.client as w32
        import pythoncom
    except ImportError:
        print("pywin32 absent : conversion PDF impossible.")
        return 1

    def verrouille(chemin):
        """Un .docx ouvert dans Word n'est pas reouvrable en ecriture.

        On teste AVANT de le confier a Word : sinon Word affiche une boite de
        dialogue « fichier deja utilise » et la conversion se bloque
        indefiniment, sans message.
        """
        try:
            fh = open(chemin, "r+b")
            fh.close()
            return False
        except (PermissionError, IOError):
            return True

    docs, ignores = [], []
    bases = []
    for _s in SORTIES:
        if os.path.isdir(_s):
            bases += [os.path.join(_s, _d) for _d in sorted(os.listdir(_s))]
    for dd in bases:
        if not os.path.isdir(dd):
            continue
        for f in os.listdir(dd):
            # Word depose un fichier de verrouillage cache « ~$... » a cote
            # de chaque document ouvert : ce n'est pas une fiche.
            if f.startswith("~$"):
                continue
            if f.endswith("_fiche.docx"):
                src = os.path.join(dd, f)
                if verrouille(src):
                    ignores.append(f)
                    continue
                dst = os.path.join(dd, f[:-5] + ".pdf")
                # Reprise : on saute ce qui est deja a jour. Sans cela, une
                # execution interrompue recommence tout depuis le debut et
                # n'arrive jamais au bout.
                if (os.path.exists(dst)
                        and os.path.getmtime(dst) >= os.path.getmtime(src)):
                    continue
                docs.append((src, dst))

    if not docs:
        print("Aucune fiche Word trouvee.")
        return 1

    pythoncom.CoInitialize()

    # L'automatisation Word se degrade au fil des conversions : passe une
    # douzaine de documents, l'appel COM finit par ne plus rendre la main, sans
    # message ni erreur. On renouvelle donc l'instance regulierement.
    PAR_INSTANCE = 8

    def neuve():
        """Instance Word NEUVE et isolee. Surtout pas Dispatch, qui se
        rattacherait a la session ouverte de l'utilisateur."""
        a = w32.DispatchEx("Word.Application")
        a.Visible = False
        a.DisplayAlerts = 0
        return a

    app = neuve()
    faits, echecs = 0, []
    try:
        for i, (src, dst) in enumerate(docs):
            if i and i % PAR_INSTANCE == 0:
                try:
                    app.Quit()
                except Exception:
                    pass
                app = neuve()
                print("  ... %d/%d" % (i, len(docs)))
            try:
                doc = app.Documents.Open(src, ReadOnly=True,
                                         AddToRecentFiles=False,
                                         Visible=False)
                try:
                    doc.SaveAs(dst, FileFormat=WD_FORMAT_PDF)
                    faits += 1
                finally:
                    doc.Close(False)
            except Exception as ex:
                echecs.append((os.path.basename(src), str(ex)[:70]))
    finally:
        # On ne ferme QUE notre propre instance.
        app.Quit()
        pythoncom.CoUninitialize()

    print("PDF produits : %d sur %d" % (faits, len(docs)))
    if ignores:
        print("Ignores car ouverts dans Word (non touches) : %s"
              % ", ".join(ignores))
    if echecs:
        print("Echecs (%d) :" % len(echecs))
        for nom, msg in echecs:
            print("  %-28s %s" % (nom, msg))
    print("Lots traités : %d" % len(SORTIES))
    return 0 if not echecs else 1


if __name__ == "__main__":
    sys.exit(main())
