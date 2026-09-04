# MAGPIE — Guide utilisateur

**Référentiel des notions Rhino / Grasshopper et bibliothèque d'exercices autocorrigés**
Version `v0.4-260901` · référentiel Ind. C · 1er septembre 2026

---

## 1. À quoi sert MAGPIE

MAGPIE est le correcteur automatique d'exercices Grasshopper publié par
RhinoForYou. Ce dépôt lui fournit deux choses :

1. **un référentiel** de 160 notions Rhino / Grasshopper, réparties en
   11 domaines et 41 catégories, classées par niveau, mode de validation et
   type d'exercice — aucune catégorie ne porte moins de trois notions ;
2. **une bibliothèque de 229 exercices** couvrant ces 160 notions, chacun livré
   avec son sujet, son corrigé commenté, sa fiche et — quand il se corrige
   automatiquement — ses deux définitions Grasshopper.

Le principe de correction est simple et n'a qu'une règle : **l'apprenant
branche son résultat sur un paramètre nommé `REPONSE`**, et Magpie compare
cette valeur à celle du corrigé.

---

## 2. Prérequis

| | |
|---|---|
| Rhino | **Rhino 8** (les définitions sont enregistrées au format Grasshopper 1 de Rhino 8) |
| Grasshopper | celui livré avec Rhino 8 — aucun plugin n'est requis pour les 160 définitions fournies |
| Plugins | seuls quelques exercices en demandent, et leur fiche le dit : Kangaroo2 (AV-02), Anemone ou équivalent (AV-01), Human ou Elefront (WB-01) |
| Unités | **millimètres**. Les énoncés donnent toutes leurs valeurs en mm sauf mention contraire explicite |
| Lecture des fiches | Word, ou n'importe quel lecteur PDF, ou un éditeur Markdown |

Aucune installation n'est nécessaire : le dépôt se consulte tel quel.

---

## 3. Installation

### 3.1 Consultation en ligne

Rien à installer. Ouvrez :

<https://ctdvda-blip.github.io/magpie-referentiel/>

L'accès est protégé par un identifiant et un mot de passe, communiqués
séparément. Le mot de passe n'est **pas** écrit dans la page : celle-ci n'en
porte qu'une empreinte cryptographique.

> **Ce que la protection fait, et ce qu'elle ne fait pas.** Elle garde la
> *consultation* de l'application. Elle ne protège pas les *fichiers* : le
> dépôt est public, et chaque définition reste atteignable par son adresse
> directe si on la connaît. C'est une porte, pas un coffre.

### 3.2 Consultation hors ligne

Récupérez le dépôt, puis ouvrez `index.html` dans un navigateur. La page est
autonome : aucune connexion, aucune dépendance externe, aucun serveur.

```bash
git clone https://github.com/ctdvda-blip/magpie-referentiel.git
```

> **Attention sous Windows.** Clonez à un emplacement **court** (`C:\MAGPIE`
> par exemple). Les chemins du dépôt sont déjà longs ; clonés trois niveaux
> plus bas, ils dépassent la limite de 260 caractères et Git échoue. Au besoin :
> `git config --global core.longpaths true`.

### 3.3 Le classeur du référentiel

`Fondamentaux Grasshopper - IndC - 01-09-2026.xlsx` s'ouvre dans Excel ou
LibreOffice. Il porte les 160 notions, leurs identifiants `REF-nnn` et la
correspondance avec les programmes de formation. Les identifiants sont
**stables** : les notions ajoutées à l'indice C ont pris REF-143 à REF-160 et
se rangent à leur place par le tri des lignes, sans renuméroter les autres.

---

## 4. Démarrage — travailler un exercice

1. **Choisir l'exercice.** Par lot, par thématique, ou par la notion visée
   depuis le référentiel.
2. **Lire la fiche sujet.** `<ID>_fiche_sujet.docx` ou `.pdf` — elle contient
   l'énoncé, les données de départ et le résultat attendu, **sans le corrigé**.
   C'est celle qu'on remet à l'apprenant.
3. **Ouvrir `<ID>_sujet.gh`** dans Grasshopper. On y trouve les données de
   départ, un paramètre `REPONSE` **volontairement non relié**, et rien d'autre.
4. **Construire la réponse**, puis **la brancher sur `REPONSE`**.
5. **Comparer au corrigé.** Ouvrir `<ID>_complet.gh` et basculer
   l'interrupteur **AFFICHER LE CORRIGÉ** : le corrigé est masqué à l'ouverture,
   pour qu'on ne le voie pas avant d'avoir cherché.

### Les exercices qui demandent de modéliser dans Rhino

RH-02 à RH-05, RH-08, RH-09, GP-03 et FA-02 ne se construisent
pas entièrement dans Grasshopper : ils demandent de **modéliser dans Rhino**.
Leur définition n'a donc rien à construire — elle **mesure**.

- Le **sujet** contient un paramètre de référence **vide** et la chaîne de
  mesure. Tant que rien n'est modélisé, rien ne sort : c'est normal, et c'est
  le principe de ces exercices.
- Le **corrigé** contient la géométrie de référence internalisée et la même
  chaîne : c'est l'**étalon** auquel confronter sa propre production, pas une
  solution à recopier.

### Les questions charnières

38 des 229 items ne sont pas des exercices mais des **questions charnières** :
une question à quatre propositions, qui vérifie une compréhension plutôt
qu'un savoir-faire. Elles se répondent par un menu déroulant dans la
définition, ou directement sur la fiche.

---

## 5. Ce que contient le dossier d'un exercice

```
<ID>/
    <ID>_sujet.gh          la définition à compléter
    <ID>_complet.gh        la même, plus le corrigé masqué par un interrupteur
    <ID>.json              le descripteur : notions visées, barème, tolérance…
    <ID>_fiche.md          la fiche formateur : sujet ET corrigé
    <ID>_fiche_sujet.md    la fiche apprenant : sujet seul
    <ID>_fiche.docx        la fiche formateur, illustrée
    <ID>_fiche_sujet.docx  la fiche apprenant, illustrée
    <ID>_fiche.pdf         la fiche formateur, prête à imprimer
    Illustrations/         les canvas rendus, et leurs vignettes web
    Ressources/            les fichiers .3dm, quand l'exercice en demande
```

Les sept exercices dont le livrable n'est pas un graphe — IA-07, PL-03, MP-01,
DV-04, DV-07, WB-01, WB-02 — n'ont pas de `.gh` : ils rendent un plugin
compilé, un configurateur en ligne ou une définition remaniée par
l'apprenant, et se notent sur **grille**, pas sur une valeur.

---

## 6. Les quatorze lots

| Lot | Intitulé | Exercices | Avec `.gh` | Durée cumulée |
|---|---|---|---|---|
| **A** | Découverte des composants natifs | 51 | 51 | 376 min |
| **G** | Exercices gamifiés | 32 | 32 | 521 min |
| **IA** | IA et assistance générative | 25 | 24 | 586 min |
| **RH** | Socle Rhino | 23 | 23 | 401 min |
| **B** | Algorithmes combinés | 18 | 18 | 479 min |
| **GP** | Géométrie paramétrique appliquée | 12 | 12 | 285 min |
| **PL** | Écosystème de plugins | 12 | 11 | 163 min |
| **C** | Projets appliqués | 12 | 12 | 995 min |
| **AV** | Algorithmique avancée | 9 | 9 | 231 min |
| **DV** | Développement, scripting et API | 9 | 7 | 287 min |
| **WB** | Interfaces, web et interopérabilité | 9 | 7 | 293 min |
| **QT** | Quantitatifs, chiffrage et export | 6 | 6 | 165 min |
| **FA** | Aide à la fabrication | 6 | 6 | 163 min |
| **MP** | Méthode, performance et évènements | 5 | 4 | 113 min |
| | **Total** | **229** | **222** | **5 058 min — 84,3 h** |

Niveaux : 92 débutant, 63 intermédiaire, 63 perfectionnement, 11 expert.
191 exercices de **compétence**, 38 questions de **connaissance**.

---

## 7. L'application de consultation

`index.html` (ou `MAGPIE - Application.html` dans le projet) est une page
autonome, sans dépendance ni serveur. Elle offre trois vues.

- **Accueil** — les chiffres, l'accès thématique par domaine puis catégorie,
  et les quatorze lots ; un clic sur un lot mène directement à ses exercices.
- **Référentiel** — les 160 notions, filtrables par domaine et par niveau,
  avec pour chacune les exercices qui la couvrent.
- **Exercices** — les 229 exercices, filtrables par **lot**, par thématique et
  par recherche libre. Chaque fiche donne l'énoncé, le corrigé commenté, les
  illustrations, et le téléchargement des livrables.

Le numéro de version s'affiche en haut à droite, dans le bandeau.

---

## 8. Paramètres importants

| Paramètre | Où | Rôle |
|---|---|---|
| `REPONSE` | zone sujet | **Le seul point de contact avec le correcteur.** Le nom ne doit pas changer. |
| `REPONSE_CORRIGE` | zone corrigé | La valeur étalon. Ne jamais la relier à la zone sujet. |
| `AFFICHER LE CORRIGÉ` | zone corrigé | Interrupteur, **faux** à l'ouverture. |
| `mode_validation` | `<ID>.json` | `SingleValue`, `NumericTolerance`, `GeometryTolerance`, `ExactOrderedList`, `SetEquality`, ou `Visuel` |
| `tolerance` | `<ID>.json` | La marge admise. Ignorée par `SingleValue`. |

---

## 9. Limitations connues

- **Magpie ne compare que des nombres.** Un booléen ou un texte branché sur
  `REPONSE` échoue. Les exercices concernés rendent donc un comptage ou un
  indicateur numérique, jamais un `True`/`False`.
- **`SetEquality` ignore les doublons** et les multiplicités : ne pas l'employer
  là où une valeur peut légitimement apparaître deux fois.
- **`GeometryTolerance`** demande une tolérance au moins égale à √(aire / 1500).
- **La protection du site est une porte, pas un coffre** (voir § 3.1).
- **Sept exercices n'ont pas de définition** — c'est délibéré (voir § 5).
- **A-13 et A-38** figurent sur la liste des documents que Word refuse d'ouvrir
  sur ce poste ; leurs PDF sont produits par une copie temporaire. Sans
  incidence sur les livrables, qui sont complets.

---

## 10. Dépannage

| Symptôme | Cause probable | Remède |
|---|---|---|
| Le sujet ne rend rien | Exercice « à géométrie » : rien n'est modélisé dans Rhino | Normal — modéliser d'abord, puis référencer la géométrie dans le paramètre du sujet |
| Le corrigé n'apparaît pas | L'interrupteur est resté à faux | Basculer **AFFICHER LE CORRIGÉ** |
| Magpie rejette une réponse juste | Un booléen ou un texte est branché sur `REPONSE` | Rendre un nombre |
| Un composant est en rouge à l'ouverture | Plugin absent | La fiche indique les plugins requis |
| `git clone` échoue sous Windows | Chemins trop longs | Cloner à la racine d'un disque, ou `core.longpaths true` |
| Écart de quelques millimètres sur DV-02 | Pas d'échantillonnage trop grossier | Un point tous les 10 mm suffit ; tous les 20 mm ne suffit plus |

---

## 11. Version

| | |
|---|---|
| Version | `v0.4-260901` |
| Indice | C |
| Date de ce guide | 1er septembre 2026 |
| Conception des exercices | skill `magpie-conception-exercices` v2.3 |
| Auteur d'origine du correcteur Magpie | Jérémy CAROLUS |
| Éditeur | RhinoForYou |

La version affichée dans l'application, dans les fiches et dans ce guide est
toujours la même.
