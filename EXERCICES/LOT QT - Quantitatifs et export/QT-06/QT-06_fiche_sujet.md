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

*Le corrigé fait l'objet d'une fiche distincte, remise après validation ou en fin de séance.*
