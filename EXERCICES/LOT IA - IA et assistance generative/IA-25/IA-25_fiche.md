# IA-25 — Ce que le service coûte par mois

**Fiche d'exercice Magpie** · Lot IA — IA et assistance générative

| | |
|---|---|
| **Thématique** | IA4 · Vérification, licences et limites |
| **Référence au référentiel** | REF-142 |
| **Compétence visée** | Chiffrer le coût d'usage d'un service d'IA à partir de sa consommation réelle, en distinguant ce qui entre de ce qui sort. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Perfectionnement |
| **Durée cible** | 25 min |
| **Prérequis** | IA-13 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-16 Livrable pesé |
| **Version** | v0.5-260902 — Ind. C — 01/09/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Chiffrer le coût d'usage d'un service d'IA à partir de sa consommation réelle, en distinguant ce qui entre de ce qui sort.

### Contexte

Le composant appelle un service distant à chaque recalcul. La facture arrive à la fin du mois, et personne n'a chiffré avant.

### Énoncé

> Le service traite 4 200 requêtes par mois. Chacune envoie 1 850 jetons et en reçoit 320. L'entrée est facturée 3 € le million de jetons, la sortie 15 €. Donnez le coût mensuel, en euros.

### Ce qui vous est fourni

Le nombre de requêtes, les jetons échangés par requête, et les deux tarifs.

### Ce qui est attendu

43,47 € par mois.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`IA-25_sujet.gh`

### Barème

1 point si le coût mensuel est juste au centime.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `IA-25_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Chiffrer les jetons d'entrée du mois, et ceux de sortie.

**Étape 2.** Appliquer à chacun SON tarif.

**Étape 3.** Additionner, et ramener au million de jetons.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Appliquer le même tarif à l'entrée et à la sortie : 27,34 €. La sortie coûte cinq fois l'entrée, et c'est structurel — elle se produit jeton par jeton. Un service qui répond peu mais lit beaucoup ne coûte pas comme un service qui lit peu et rédige longuement.

### Pièges fréquents

- Appliquer un tarif unique.
- Oublier que les tarifs sont donnés au million.
- Compter la sortie comme négligeable parce qu'elle est courte.

### Pourquoi ce jeu de données

1 850 jetons en entrée pour 320 en sortie est le profil d'un composant qui envoie un contexte et reçoit une réponse courte. Malgré ce rapport de six contre un en volume, la sortie pèse 36 % de la facture : c'est ce renversement que le calcul doit faire apparaître.

### Limite de la correction automatique

> Le coût n'est qu'une des trois limites de la fiche. La latence, elle, se paie à chaque recalcul et se mesure en secondes d'attente ; la reproductibilité ne se paie pas, elle s'établit — ou pas.

### Pour aller plus loin

- Chiffrer la part de la sortie dans la facture.
- Reprendre avec une mise en cache qui évite 40 % des requêtes.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `IA-25_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `IA-25_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `IA-25.json` | Descripteur pour le plugin Magpie |
| `IA-25_fiche.md` | La présente fiche |
| `IA-25_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `IA-25_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `IA-25_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
