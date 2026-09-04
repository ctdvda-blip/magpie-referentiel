# -*- coding: utf-8 -*-
"""Convertit les fiches Word en PDF.

CAS RESOLU : A-13 et A-38
-------------------------
Ces deux fiches faisaient geler Word, de facon reproductible, par SaveAs comme
par ExportAsFixedFormat. Leur fiche SUJET, qui partage les memes images, passait
en trois secondes. Structure, taille et images etaient comparables a celles des
fiches voisines. J'ai longtemps cru le blocage lie a la partie corrige.

Il n'avait rien a voir avec le contenu. Word tient une liste de documents qu'il
refuse d'ouvrir :

    HKCU\Software\Microsoft\Office.0\Word\Resiliency\DisabledItems

Un document y entre des qu'il a fait planter ou geler Word une fois, et n'en
sort plus. Le refus prend la forme d'une boite de dialogue ; avec
Visible = False, elle n'a nulle part ou s'afficher et l'appel COM ne rend jamais
la main. La liste est indexee par CHEMIN : la meme copie, ailleurs sur le
disque, s'ouvre en une demi-seconde. Le premier gel — quelle qu'en ait ete la
cause — condamnait donc definitivement le document a sa place.

D'ou le rattrapage ci-dessous : un document ecarte est reconverti depuis une
COPIE temporaire, et le PDF ramene a sa place. Rien n'est modifie chez
l'utilisateur ; vider la liste demanderait de toucher a son registre, ce qui
n'est pas le role de ce script. Il peut le faire lui-meme depuis Word :
Fichier > Options > Complements > Gerer : Elements desactives.

PRECAUTION IMPORTANTE
---------------------
L'utilisateur a des documents ouverts dans Word. On ne se rattache donc JAMAIS
a sa session : DispatchEx demarre un processus Word distinct, invisible, que
l'on est seul a piloter et que l'on est donc seul a fermer. La session de
l'utilisateur n'est ni sollicitee, ni modifiee, ni fermee.

Les fichiers verrouilles (ouverts dans Word par l'utilisateur) sont ignores et
signales, jamais forces.
"""
import io
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

    # Un appel COM qui gele ne leve pas d'exception : il ne rend jamais la
    # main. On ne peut donc pas s'en proteger de l'interieur. On note le
    # document en cours dans un temoin ; si le temoin est encore la au
    # demarrage suivant, c'est que ce document a fait geler l'execution
    # precedente, et on l'ecarte au lieu de s'y reprendre indefiniment.
    temoin = os.path.join(ICI, ".pdf-en-cours")
    ecartes = set()
    journal = os.path.join(ICI, ".pdf-ecartes")
    if os.path.exists(journal):
        for l in io.open(journal, encoding="utf-8"):
            if l.strip():
                ecartes.add(l.strip())
    if os.path.exists(temoin):
        bloquant = io.open(temoin, encoding="utf-8").read().strip()
        if bloquant:
            ecartes.add(bloquant)
            fh = io.open(journal, "a", encoding="utf-8")
            fh.write(bloquant + chr(10))
            fh.close()
            print(u"Écarté car il a fait geler l'exécution précédente : %s"
                  % os.path.basename(bloquant))
        os.remove(temoin)

    # Les ecartes ne sont plus abandonnes : on les met de cote pour les
    # reprendre par copie, une fois la serie normale passee.
    rattrapage = [(a, b) for a, b in docs if a in ecartes]
    docs = [(a, b) for a, b in docs if a not in ecartes]
    if not docs and not rattrapage:
        print(u"Rien à convertir.")
        return 0

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
            fh = io.open(temoin, "w", encoding="utf-8")
            fh.write(src)
            fh.close()
            try:
                doc = app.Documents.Open(src, ReadOnly=True,
                                         AddToRecentFiles=False,
                                         Visible=False)
                try:
                    doc.SaveAs(dst, FileFormat=WD_FORMAT_PDF)
                    faits += 1
                finally:
                    doc.Close(False)
                    if os.path.exists(temoin):
                        os.remove(temoin)
            except Exception as ex:
                echecs.append((os.path.basename(src), str(ex)[:70]))
    finally:
        # On ne ferme QUE notre propre instance.
        app.Quit()
        pythoncom.CoUninitialize()

    # --- rattrapage des documents que Word refuse a leur place
    repris, manques = [], []
    for src, dst in rattrapage:
        try:
            import pdf_un
            if pdf_un.convertir_par_copie(src, dst):
                repris.append(os.path.basename(src))
            else:
                manques.append(os.path.basename(src))
        except Exception as ex:
            manques.append("%s (%s)" % (os.path.basename(src), str(ex)[:50]))

    print("PDF produits : %d sur %d" % (faits, len(docs)))
    if repris:
        print(u"Repris par copie (refusés par Word à leur place) : %s"
              % ", ".join(sorted(repris)))
    if manques:
        print(u"Rattrapage en échec : %s" % ", ".join(sorted(manques)))
    if ignores:
        print("Ignores car ouverts dans Word (non touches) : %s"
              % ", ".join(ignores))
    if echecs:
        print("Echecs (%d) :" % len(echecs))
        for nom, msg in echecs:
            print("  %-28s %s" % (nom, msg))
    if ecartes:
        print(u"Sur la liste noire de Word, donc convertis par copie : %s"
              % ", ".join(sorted(os.path.basename(x) for x in ecartes)))
    print("Lots traités : %d" % len(SORTIES))
    return 0 if not echecs else 1


if __name__ == "__main__":
    sys.exit(main())
