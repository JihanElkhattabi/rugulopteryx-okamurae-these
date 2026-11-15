# Scripts d'analyse phytochimique

Ce dossier contiendra les scripts d'analyse relatifs au traitement des donnees
phytochimiques de *Rugulopteryx okamurae*.

## Organisation prevue

```
scripts/
├── extraction/    # Scripts de traitement des chromatogrammes (HPLC, GC-MS)
├── analyse_rm/    # Scripts d'aide a l'interpretation des spectres RMN
├── statistiques/  # Analyses statistiques (R / Python)
└── figures/       # Scripts de generation des figures de la these
```

## Langages et reproductibilite

- Python 3.11 (pandas, scikit-learn, matplotlib) pour le traitement chromatographique.
- R 4.3 pour les analyses statistiques et les figures publication.
- Chaque script est accompagne d'un en-tete documentant : auteur, date, objectif,
  entrees/sorties, dependances et commande d'execution.

## Licence

Les scripts sont distribues sous licence MIT (voir LICENSE a la racine du depot).
