# MAGPIE — Planning et suivi

Version `v0.4-260901` · référentiel Ind. C · mis à jour le 1er septembre 2026

---

## Avertissement sur les durées

Les durées de travail **ne sont pas mesurées** : l'environnement ne les
enregistre pas, et aucun relevé de temps n'a été tenu. Les inscrire au jugé
donnerait un planning d'apparence précise et de fond inventé.

Ce document donne donc ce qui est **réellement daté** : les jalons, à la date
et à l'heure des commits ou des fichiers produits. La colonne « durée » porte
la mention **non mesurée** partout où c'est le cas, et un intervalle horaire
quand deux jalons du même jour l'encadrent.

La colonne qui compte pour un formateur — la **durée cible des exercices**, elle,
est mesurée et documentée : elle figure au § 4.

---

## 1. Jalons datés

| Date | Jalon | Livrable | Durée |
|---|---|---|---|
| 25/08/2026 | Référentiel indice A | `Fondamentaux Grasshopper - IndA - 25-08-2026.xlsx` | non mesurée |
| 26/08/2026 | Refonte pédagogique par la skill de conception v2.3 | 49 fiches du lot A reprises, `skill_a.py` | non mesurée |
| 26/08/2026 | Référentiel indice B | `Fondamentaux Grasshopper - IndB - 26-08-2026.xlsx`, cahier des charges | non mesurée |
| 27/08/2026 | Domaine 11 — IA, et renumérotation des domaines à partir de 1 | 26 notions `REF-117..142`, lot IA de 14 exercices | non mesurée |
| 28/08/2026 12:09 | Première publication du site | dépôt `ctdvda-blip/magpie-referentiel` | — |
| 28/08/2026 12:45 | Couverture complète : neuf lots supplémentaires | lots RH, GP, QT, FA, PL, MP, AV, DV, WB | ~36 min entre les deux commits |
| 28/08/2026 16:32 | Définitions des nouveaux lots, trois défauts de conception corrigés | 28 définitions, fiches apprenant assainies, QCM rééquilibrés | ~3 h 45 entre les deux commits |
| 28/08/2026 | Contribution en amont | PR #2 sur `Magpie-Project/Magpie`, **fusionnée** | — |
| 01/09/2026 10:24 | Trois dernières définitions mesurables, deux fiches débloquées | RH-04, AV-02, DV-02 ; PDF de A-13 et A-38 | non mesurée |
| 01/09/2026 12:53 | Les onze lots visibles et filtrables sur le site | application revue, republication | ~2 h 30 entre les deux commits |
| 01/09/2026 | Recette de non-régression sur les valeurs | `recette_7_valeurs.py`, 93 valeurs figées | non mesurée |
| 01/09/2026 | Guide utilisateur et planning | ce document et le guide | non mesurée |
| 01/09/2026 | Équilibrage, vague 1 | 16 exercices, 10 catégories servies | non mesurée |
| 01/09/2026 | Équilibrage, vague 2 | 34 exercices, cible atteinte | non mesurée |
| 01/09/2026 | Montée en v0.4-260901 | version propagée à toute la chaîne | non mesurée |
| 01/09/2026 | Référentiel indice C | 18 notions ajoutées, 14 catégories complétées | non mesurée |
| 01/09/2026 | Équilibrage, vague 3 | 18 exercices, un par notion ajoutée | non mesurée |
| 02/09/2026 | Lot B | 18 exercices d'algorithmes combinés, `skill_b.py`, huit modes de validation corrigés | non mesurée |
| 02/09/2026 | Lot C | 12 projets appliqués, `skill_c.py`, un indicateur vérifiable par projet | non mesurée |
| 02/09/2026 | Recette 8 | unicité des noms d'objets dans les recettes, 233 recettes contrôlées | non mesurée |
| 02/09/2026 | Lot G | 32 exercices gamifiés, `skill_g.py`, quatorze modes de validation corrigés | non mesurée |

---

## 2. Où en est chaque lot

| Lot | Exercices | Fiches | Définitions `.gh` | Illustrations | État |
|---|---|---|---|---|---|
| A | 51 | 51 | 51 | oui | **terminé** |
| IA | 25 | 25 | 24 | oui | **terminé** — IA-07 livre un plugin, noté sur grille |
| RH | 23 | 23 | 23 | oui | **terminé** |
| GP | 12 | 12 | 12 | oui | **terminé** |
| QT | 6 | 6 | 6 | oui | **terminé** |
| FA | 6 | 6 | 6 | oui | **terminé** |
| PL | 12 | 12 | 11 | oui | **terminé** — PL-03 noté sur grille |
| MP | 5 | 5 | 4 | oui | **terminé** — MP-01 noté sur grille |
| AV | 9 | 9 | 9 | oui | **terminé** |
| DV | 9 | 9 | 7 | oui | **terminé** — DV-04 et DV-07 notés sur grille |
| WB | 9 | 9 | 7 | oui | **terminé** — WB-01 et WB-02 notés sur grille |
| B | 18 | 18 | 18 | oui | **terminé** |
| C | 12 | 12 | 12 | oui | **terminé** — un indicateur corrigé, le reste sur grille |
| G | 32 | 32 | 32 | oui | **terminé** — six corrigés par étalon |
| | **229** | **229** | **222** | | |

Les sept exercices sans définition sont exactement les sept dont le mode de
validation est **Visuel**. Ce n'est pas un reste à faire : leur livrable est un
plugin, un site ou une définition remaniée par l'apprenant. Leur fournir un
`.gh` reviendrait à livrer le travail demandé.

---

## 3. Couverture du référentiel

| | |
|---|---|
| Notions au référentiel | 160 |
| Notions couvertes par au moins un exercice | **160 (100 %)** |
| Catégories sans exercice | **0** |
| Catégories ayant moins d'exercices que de notions | **0** |
| Catégories portant moins de trois notions | **0** |
| Notions par catégorie | min 3, médiane 3, max 11 |
| Exercices par catégorie | min 3, médiane 4, max 11 |
| Domaines | 11 |

Contrôlé par `Documentation/Generateurs/couverture.py`, qui écrit `COUVERTURE.md`.

---

## 4. Durées cibles des exercices

Celles-ci sont **définies**, pas estimées après coup : chaque fiche porte sa
durée cible, et c'est elle qui sert à bâtir une journée de formation.

| Lot | Durée cumulée |
|---|---|
| A | 376 min |
| IA | 586 min |
| RH | 401 min |
| GP | 285 min |
| QT | 165 min |
| FA | 163 min |
| PL | 163 min |
| MP | 113 min |
| AV | 231 min |
| DV | 287 min |
| WB | 293 min |
| B | 479 min |
| C | 995 min |
| G | 521 min |
| **Total** | **5 058 min — 84,3 h** |

Répartition par niveau : 92 débutant · 63 intermédiaire · 63 perfectionnement ·
11 expert. Nature : 191 exercices de compétence, 38 questions de connaissance.

---

## 5. Contrôles automatiques, et ce qu'ils garantissent

| Contrôle | Portée | Ce qu'il attrape | Dernier résultat |
|---|---|---|---|
| `verifier_fraicheur.py` | **les quatorze lots** | un PDF plus ancien que sa fiche Word, une fiche ou une définition plus ancienne que le module qui la déclare | **à jour** |
| `couverture.py` | référentiel | une notion ou une catégorie sans exercice | **160/160** |
| `recette_1_resolution.py` | lot A | un composant qui ne se résout pas | OK |
| `recette_2_valeurs.py` | lot A | une valeur qui ne correspond pas à la fiche | OK |
| `recette_3_etancheite.py` | lot A | un corrigé qui a fui dans le sujet | OK |
| `recette_4_corrige_masque.py` | lot A | un corrigé visible à l'ouverture | OK |
| `recette_5_avertissements.py` | lot A | un composant en avertissement | OK |
| **`recette_6_tous_lots.py`** | **les quatorze lots** | fichiers illisibles, sujets non étanches, corrigés non masqués, `REPONSE_CORRIGE` muette, avertissements inattendus | **222/222 OK** |
| **`recette_7_valeurs.py`** | **les quatorze lots** | **une valeur de corrigé qui a changé** — le défaut le plus discret, celui de RH-09 | **222/222 conformes** |
| **`recette_8_noms_uniques.py`** | **toutes les recettes** | **un nom qui en désigne deux** — il écrase le premier objet et déplace des fils sans rien signaler, comme sur C-02 | **233 recettes, 0 doublon** |
| **`verifier_vague1/2/3.py`** | les 68 exercices ajoutés | une réponse annoncée qui ne correspond pas au calcul refait depuis les données | **55/55 conformes** |
| **`verifier_lot_b.py`, `verifier_lot_c.py`, `verifier_lot_g.py`** | lots B, C et G | idem, sur les 62 réponses de ces trois lots | **62/62 conformes** |
| `verifier_liens.py` | site publié | un téléchargement promis mais absent | **1 353/1 353** |
| `equilibrer_qcm.py --controle` | questions charnières | un commentaire qui désigne une proposition inexistante | 0 |

Les recettes 1 à 5 sont antérieures aux nouveaux lots et n'interrogent que le
lot A ; les recettes 6 et 7 couvrent les onze. Les deux séries se complètent,
elles ne se remplacent pas.

`verifier_fraicheur.py` ne datait lui aussi que les lots A et IA : les neuf
autres n'étaient comparés à aucune source, et un exercice réécrit sans
régénération serait passé inaperçu. Sa table de sources n'est plus écrite à
la main — elle est **déduite des modules**, en leur demandant quels
identifiants ils déclarent. Ajouter un module de contenu suffit désormais à
ce qu'il soit surveillé, et un dossier d'exercice sans source déclarée est
signalé au lieu d'être ignoré.

---

## 6. Reste à faire

### Ce qui appartient à Charles

| Sujet | Décision attendue |
|---|---|
| Contribution en amont | La PR #2 est fusionnée et ne porte que les lots A et IA. Les neuf lots ajoutés depuis ne sont pas remontés. Ouvrir une nouvelle PR sur le dépôt de Jérémy CAROLUS est un geste vers un tiers. |
| Liste noire de Word | Word > Fichier > Options > Compléments > Gérer : Éléments désactivés. Sans ce nettoyage, A-13 et A-38 continueront de passer par une copie temporaire. |
| Poids du dépôt de publication | `.git` pèse 108 Mo pour cinq publications. La dérive est stoppée ; l'historique accumulé reste. Deux voies si cela devient gênant : repartir d'un commit unique, ou cesser de publier `.docx` et `.pdf`. |
| Montée de version | **Faite le 01/09/2026** : `v0.3-260826` → `v0.4-260901`, propagée à l'application, aux fiches, au cahier des charges, au guide et à ce planning. Les livrables de la v0.3 sont archivés dans `Anciens fichiers/v0.3-260826/`. |

### Ce qui reste ouvert techniquement

| Sujet | État |
|---|---|
| GP-02 et `Mass Addition` | `Mass Addition` ne sommait que 8 des 15 valeurs de son entrée, de façon reproductible, alors que le même composant en somme 20 ailleurs. Contourné par la formule n(n+1)/2. **Cause inconnue.** |
| ~~Exercices B, C et G~~ | **Produits le 02/09.** Les quatorze lots du cahier des charges existent désormais. |
| Format natif `web/data/exercises/*.json` | Proposé dans la PR #2, en attente de la position de Jérémy. |

---

## 7. Convention de versions

Format `v0.N-AAMMJJ`, appliqué **au même numéro** sur l'application, le guide
utilisateur, le cahier des charges, les fiches et le classeur. Les anciennes
versions sont archivées dans les dossiers `Anciens fichiers`, jamais supprimées.
