# Resultats de l'analyse phytochimique

Ce dossier contient les sorties generees par les scripts d'analyse a partir
des donnees de `data/`. Les fichiers presents ici sont des **exemples** produits
par `scripts/analyse_phytochimique.py`.

## Contenu

```
results/
├── README.md                       # Ce fichier
├── statistiques_par_classe.csv     # Aire moyenne/totale des pics par classe et site
└── aire_pic_par_compose.png        # Diagramme en barres du profil metabolique
```

## Regeneration des resultats

Depuis la racine du depot :

```bash
python scripts/analyse_phytochimique.py
```

Dependances : `pandas`, `matplotlib` (cf. `requirements.txt` a venir).

## Note

Les valeurs numeriques de `data/exemple_metabolites.csv` sont **illustatives**
et destinees a la demonstration du pipeline d'analyse. Elles seront remplacees
par les donnees reelles des campagnes de prelevement (cf. PGD, section 1).
