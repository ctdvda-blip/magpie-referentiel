# Session 9 — sauvegarde 01 — 4 septembre 2026

## Ce que cette sauvegarde est, et ce qu'elle n'est pas

Le `CLAUDE.md` demande une sauvegarde de la conversation avant chaque
compression de contexte. **Elle n'a pas été tenue jusqu'ici**, et le dossier
`Sauvegardes sessions/` n'existait pas : c'est le premier fichier qu'il
contient. La règle est appliquée à partir de maintenant.

Cette session a déjà été compressée au moins une fois. Le verbatim des
échanges antérieurs à la compression **n'est plus disponible**, et rien ne
permet de le reconstituer. Ce document consigne donc ce qui est encore
établi : les décisions, les travaux et leurs justifications — pas le fil de
la conversation.

Le détail technique jour par jour vit dans `Journal des modifications/`, et
l'état opérationnel dans `REPRISE_SESSION.md`. Cette sauvegarde ne les
duplique pas : elle donne le fil des décisions.

---

## Demandes de l'utilisateur, dans l'ordre

1. Reprendre le travail dépendant de Rhino après redémarrage de `MCPStart`.
2. Ajouter les exercices au site en ligne.
3. Équilibrer le nombre d'exercices par catégorie, puis par sous-catégorie.
   → Arbitrage demandé : **proportionnel au nombre de notions**, **par vagues
   avec point d'étape**.
4. Passer en `v0.4-260901`.
5. Ajouter des notions aux catégories trop maigres, avec leurs exercices.
6. Faire les lots **B, C et G**.
7. Passer en `v0.5-260902`.
8. Créer un dépôt git propre dans MAGPIE.
9. Mettre à jour les dépôts existants.
10. Continuer les exercices et les notions prévus.
    → Arbitrage demandé : **densifier les 15 catégories au plancher**.
11. Pousser le dépôt du projet sur GitHub.
    → Arbitrage demandé : **pas de nouveau dépôt**, une branche du dépôt
    existant.
12. Mettre à jour tout ce qui est sur GitHub en cohérence.

## Décisions structurantes

| Décision | Motif |
|---|---|
| Les lots B, C et G reçoivent une **couche pédagogique séparée** (`skill_b/c/g.py`) | Ne jamais modifier `exos_a.py`, `exos_b.py`, `exos_g.py` — fiches d'origine de Jérémy CAROLUS |
| Le lot C porte **un indicateur numérique vérifiable par projet**, le reste sur grille | Un projet ne se réduit pas à un nombre, mais les fiches annonçaient déjà « deux indicateurs affichés » |
| Le lot G : **l'indicateur est la métrique du jeu** | On ne plaque pas un nombre sur un jeu, on lit celui qu'il affiche |
| Six corrigés du lot G par **étalon** | Mots croisés, memory, quiz : la réponse ne se calcule pas, elle se sait |
| Les tableaux d'inventaire sont fournis **codés** | Le checker ne compare que des nombres ; le raisonnement logique reste entier |
| Les **thématiques sont normalisées au chargement** | La cohérence se construit dans `lots.py`, sans toucher aux fichiers d'origine |
| Le dépôt du projet ignore Word, PDF et images | 280 Mo régénérables et horodatés ; les `.gh` (1,7 Mo) sont suivis |
| Le projet part sur la branche **`projet`** de `magpie-referentiel` | Choix de l'utilisateur : pas de nouveau dépôt |
| Les `.gh` **ne sont pas reconstruits** à chaque montée de version | Grasshopper réattribue les GUID ; `propager_version.py` ne touche que le champ `version` |

## Défauts trouvés et corrigés, par famille

### Les listes tenues à la main — **sept fois**

`AVEC_DEFINITIONS`, les sources de `verifier_fraicheur`, ses préfixes, les
modules de la recette 7, le corpus d'`audit_skill`, les pilotes de
construction par lot, le chargeur des vagues de `lots.py`. **Toutes sont
désormais découvertes.** C'est le défaut le plus récurrent du projet.

### Le piège des compréhensions IronPython — **trois fois**

La variable de boucle d'une compréhension fuit dans la portée englobante.
`_e` écrasé deux fois en août (« str is not callable », « int is not
callable »), puis `_f` et `_b` en septembre (« bool is not callable »). Les
fonctions utilitaires portent maintenant des noms longs.

### Les modes de validation intenables

`GeometryTolerance` ne compare qu'un élément, `SetEquality` qu'un ensemble de
nombres sans doublon. Huit exercices du lot B et quatorze du lot G les
déclaraient sur des livrables qui n'en sont pas. Tous rebasculés sur une
mesure caractéristique.

### Les jeux de données qui ne discriminent pas

- **B-14** : rang ambigu, recalculé sur une pièce donnant 7/5/4 distincts.
- **B-15** : jeu cherché sur 4 000 tirages pour que la règle gloutonne
  n'atteigne PAS la borne théorique — 12 barres contre 11.
- **C-08** : masse à 7,36 g au-dessus de la limite de sa propre fiche ;
  section retaillée à 3,011 g.
- **C-12** : l'espacement ne changeait pas le compte de plaques ; pièces
  grossies de 4 % pour que le piège existe.
- **G-08** : le médian brut coïncidait avec le médian trié ; graine changée.
- **PL-15** : le minimum valait le catalogue entier ; apports redistribués.
- **IA-32** : deux lectures distinctes sur quatre ; un relevé posé
  exactement au seuil.

### Le générateur pseudo-aléatoire

Il lisait le reste modulo l'étendue : sur un module 2³¹, le bit de poids
faible alterne, et la parité de G-06 était prévisible sans regarder une
donnée. Il lit désormais les bits de poids fort.

### Le constructeur unique et les dossiers dupliqués

`build_tout.py` a d'abord écrit les lots A et IA dans des dossiers courts, à
côté de leurs dossiers à titre long : 62 doublons, définitions d'un côté et
fiches de l'autre. Le constructeur rejoint désormais le dossier existant. Le
repliement a lui-même créé 62 `Illustrations/web/web` — `shutil.move` d'un
dossier vers un homonyme l'y place au lieu de le fondre.

## Points de vigilance légués

- Reconstruire par `GH/build_tout.py`, jamais par un pilote de lot.
- Ne jamais nommer une fonction `_f`, `_b`, `_e`.
- Ne pas ajouter `skill_a.py` aux constantes de version.
- Toute nouvelle liste de modules doit être découverte.
- Les numéros de thématique sont calculés au chargement : les réécrire à la
  main dans un module de domaine n'a aucun effet.
- Le mot de passe du site ne s'écrit jamais dans un fichier ; il se passe en
  argument `--protege`.

## État à la clôture

253 exercices, 246 définitions, 160 notions couvertes, 90,5 h, 1 497
téléchargements. Quatorze lots, aucune catégorie au plancher, les huit champs
de la skill partout, 11 écarts d'audit tous documentés.

Poussé sur `ctdvda-blip/magpie-referentiel` : `main` pour le site, `projet`
pour la chaîne de génération.
