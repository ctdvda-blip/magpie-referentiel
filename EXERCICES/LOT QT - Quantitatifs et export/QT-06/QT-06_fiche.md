# QT-06 — Du métré au devis

**Fiche d'exercice Magpie** · Lot QT — Quantitatifs, chiffrage et export

| | |
|---|---|
| **Thématique** | QT2 · Quantitatifs et chiffrage |
| **Référence au référentiel** | REF-083 |
| **Compétence visée** | Enchaîner les coefficients d'un devis dans le bon ordre, en sachant sur quelle assiette chacun s'applique. |
| **Case Bloom (révisée)** | Appliquer × procédurale |
| **Niveau** | Intermédiaire |
| **Durée cible** | 30 min |
| **Prérequis** | QT-02 |
| **Mode de validation** | NumericTolerance — tolérance 0.01 |
| **Solution de référence** | 8 composants |
| **Gamification associée** | G-11 Commande à passer |
| **Version** | v0.4-260901 — Ind. B — 26/08/2026 |
| **Conception** | magpie-conception-exercices v2.3 |

---

## SUJET

### Compétence visée

Enchaîner les coefficients d'un devis dans le bon ordre, en sachant sur quelle assiette chacun s'applique.

### Contexte

Le métré est fait. Reste à en faire un devis : main d'œuvre, marge, puis taxe — et pas dans un autre ordre.

### Énoncé

> Les matériaux reviennent à 4 820,50 €. La pose demande 22,5 heures à 48 € l'heure. La marge est de 12 %, la taxe de 10 %. Donnez le montant toutes taxes comprises, en euros.

### Ce qui vous est fourni

Le coût des matériaux, les heures et leur taux, le taux de marge et celui de la taxe.

### Ce qui est attendu

7 269,42 € toutes taxes comprises.

Branchez votre résultat sur le paramètre **`REPONSE`**, en haut à droite de la zone de travail. La correction compare cette sortie en mode **NumericTolerance** avec une tolérance de 0.01.

> **La consigne ne nomme aucun composant**, et c'est délibéré : nommer l'outil reviendrait à donner la réponse. Ce lot n'autorise que des composants natifs de Grasshopper pour Rhino 8 — aucun plugin tiers n'est nécessaire.

### Fichier à ouvrir

`QT-06_sujet.gh`

### Barème

1 point si le montant TTC est juste au centime.

---

## CORRIGÉ

> À ne consulter qu'après avoir cherché. Dans le fichier `QT-06_complet.gh`, le corrigé occupe la zone basse du canvas, chaque étape formant un groupe distinct. Il est **autonome** : les données fournies y sont recopiées, aucun câble ne le relie à la zone sujet. Il ne produit rien tant que l'interrupteur **AFFICHER LE CORRIGÉ** n'est pas basculé sur vrai — remettez-le sur faux pour faire disparaître le résultat.

### Marche à suivre

**Étape 1.** Chiffrer la main d'œuvre.

**Étape 2.** Ajouter les matériaux : c'est le déboursé sec.

**Étape 3.** Appliquer la marge.

**Étape 4.** Appliquer la taxe.

### L'erreur attendue

C'est l'erreur qu'il faut guetter, parce qu'elle est *diagnostique* : elle dit ce que l'apprenant a mal compris, là où un simple « faux » ne dirait rien.

> Oublier la marge et facturer 6 490,55 €. L'écart, 778,87 €, est exactement ce que l'entreprise gagnait sur le chantier : le devis reste plausible, il est simplement à prix coûtant.

### Pièges fréquents

- Oublier la marge.
- Appliquer la marge aux seuls matériaux.
- Confondre marge et taux de marque.

### Pourquoi ce jeu de données

Les taux — 12 % de marge, 10 % de taxe — sont ceux du bâtiment en rénovation. Marge et taxe étant toutes deux multiplicatives, leur ORDRE ne change pas le total : c'est l'oubli de l'une qui se voit, pas leur permutation, et l'exercice porte donc sur ce qui compte vraiment.

### Limite de la correction automatique

> Le calcul suppose une marge sur le déboursé sec. Beaucoup d'entreprises appliquent des coefficients distincts aux matériaux et à la main d'œuvre — la structure du calcul reste la même.

### Pour aller plus loin

- Séparer les coefficients matériaux et main d'œuvre.
- Retrouver le prix de vente qui atteint une marge visée.

---

### Fichiers de cet exercice

| Fichier | Contenu |
|---|---|
| `QT-06_sujet.gh` | Énoncé et données de départ, sans le corrigé |
| `QT-06_complet.gh` | Énoncé **et** corrigé commenté étape par étape |
| `QT-06.json` | Descripteur pour le plugin Magpie |
| `QT-06_fiche.md` | La présente fiche |
| `QT-06_fiche_sujet.md` | La fiche sans le corrigé, pour l'apprenant |
| `QT-06_fiche.docx` | La fiche Word illustrée, sujet et corrigé |
| `QT-06_fiche_sujet.docx` | La fiche Word illustrée, sujet seul |
| `Illustrations/` | Captures du canvas, sujet et corrigé |
