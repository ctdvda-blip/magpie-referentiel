# MAGPIE — référentiel et exercices Grasshopper

Référentiel des notions Rhino / Grasshopper et bibliothèque d'exercices
autocorrigés pour le plugin **Magpie**, édité par RhinoForYou.

👉 **[Consulter l'application](https://ctdvda-blip.github.io/magpie-referentiel/)**

---

## L'écran d'entrée — ce qu'il fait, ce qu'il ne fait pas

L'application demande un identifiant et un mot de passe. Voici exactement ce
que cela vaut, pour que personne ne s'y trompe.

**Le mot de passe n'est pas dans la page.** On n'y trouve qu'un sel aléatoire et
l'empreinte PBKDF2-SHA256 du mot de passe, 200 000 tours. On ne peut pas
remonter du second au premier : la page sait vérifier un mot de passe, elle ne
sait pas le révéler.

**Mais l'écran ne protège pas les fichiers.** Ce dépôt est public. Chaque
définition `.gh`, chaque fiche et chaque corrigé possède une adresse directe, et
reste téléchargeable sans jamais charger l'application. Le dépôt entier peut
être cloné. L'écran garde le hall, pas les portes.

Autrement dit : il signale que le contenu n'est pas destiné au tout-venant, et
il évite qu'on tombe dessus par hasard. Il n'empêche personne de déterminé.

**Pour une vraie restriction d'accès**, il faut un contrôle côté serveur —
Cloudflare Access, un hébergement avec authentification, ou GitHub Pages sur
dépôt privé avec un plan payant. Aucun site statique public ne peut l'imiter en
JavaScript, quelle que soit la qualité du chiffrement de l'écran d'entrée.

---

## Contenu

| | |
|---|---|
| Référentiel | **142 notions**, 11 domaines — **100 % couvertes** |
| Exercices | **99**, répartis en 11 lots |
| Définitions | **124 fichiers `.gh`**, sujet et corrigé |
| Fiches | Markdown et Word illustrées, sujet seul et sujet + corrigé |

### Les onze lots

| Lot | Domaine | Items |
|---|---|---:|
| A | Découverte des composants natifs | 49 |
| RH | Socle Rhino | 10 |
| PL | Écosystème de plugins | 4 |
| GP | Géométrie paramétrique appliquée | 4 |
| QT | Quantitatifs, chiffrage et export | 3 |
| MP | Méthode, performance et évènements | 3 |
| AV | Algorithmique avancée | 3 |
| DV | Développement, scripting et API | 4 |
| WB | Interfaces, web et interopérabilité | 3 |
| FA | Aide à la fabrication | 2 |
| IA | IA et assistance générative | 14 |

Sur ces 99 items, **77 sont des exercices notés** et **22 des questions
charnières** — des connaissances que la skill interdit de monter en exercice,
parce que la réponse s'y obtiendrait en sachant plutôt qu'en construisant.

Les lots B (algorithmes combinés), C (projets appliqués) et G (exercices
gamifiés) sont spécifiés au cahier des charges mais pas encore produits.

---

## Comment les exercices sont conçus

Tous suivent la skill `SKILL.md`, adossée à la recherche en sciences de
l'apprentissage :

- **une compétence, pas une connaissance** — dix items dont la réponse
  s'obtenait en *sachant* plutôt qu'en *construisant* sont requalifiés en
  **questions charnières**, non notées, dont chaque mauvaise réponse est
  diagnostique ;
- **aucun nom de composant dans la consigne** — nommer l'outil, c'est donner la
  réponse ; la liste ne figure que côté corrigé ;
- **un contexte métier en une phrase** par exercice, varié d'un exercice à
  l'autre ;
- **des jeux de données longs et non devinables** — 24 à 36 valeurs non
  ordonnées, plutôt que des listes qui se comptent à l'œil ;
- **une erreur attendue anticipée**, qui dit ce que l'apprenant a mal compris
  là où un simple « faux » ne dirait rien.

Un audit mécanisé chiffre l'écart : **124 écarts avant reprise, 7 après**, tous
documentés.

### Deux règles structurantes des fichiers `.gh`

1. **Aucun câble ne relie la zone sujet à la zone corrigé** : les données
   fournies sont recopiées, le corrigé est autonome.
2. **Le corrigé ne produit rien tant qu'un interrupteur n'est pas basculé.**
   Remis sur faux, le résultat disparaît.

Vérifié sur les 124 définitions.

---

## Ce qui est vérifié, et comment

Les valeurs attendues ne sont **jamais déduites de tête** : chaque définition
est ouverte dans Rhino, l'interrupteur basculé, la sortie relevée. Trois
contrôles rejouables :

```bash
python Documentation/Generateurs/audit_skill.py --fusion
python Documentation/Generateurs/controle_reponses.py
python Documentation/Generateurs/verifier_fraicheur.py
```

---

## Limites connues

- **Le checker Magpie ne compare que des nombres.** Les exercices dont le
  livrable est un texte, un plugin ou une conversation sont déclarés hors
  correction automatique et le disent, plutôt que d'être tordus pour entrer
  dans l'outil.
- **IA-07** n'a pas de définition Grasshopper : son livrable est un plugin
  `.gha` compilé.
- Les dossiers d'exercice portent le seul identifiant, sans le titre : avec le
  titre complet, les chemins dépassaient la limite de 260 caractères de Windows
  et le clone échouait.

---

## Auteurs

Prototype et conception d'origine du plugin : **Jérémy CAROLUS** — CJ développement.
Référentiel, lots d'exercices et application : **Charles THIERRY DE VILLE D'AVRAY**.
Édition : **RhinoForYou**.
