# Écosystème numérique de thèse — *Rugulopteryx okamurae*

> Dépôt accompagnant la thèse : **« Étude phytochimique de *Rugulopteryx okamurae* dans la Méditerranée marocaine »**

| | |
|---|---|
| **Doctorante** | Jihan El-khattabi |
| **ORCID** | <https://orcid.org/0009-0002-7946-4934> |
| **Laboratoire** | Laboratoire de Biologie, Écologie et Santé (LBECS) |
| **Établissement** | Formation doctorale — Module 5 « Transformation numérique et recherche scientifique » |
| **Date** | 15 novembre 2026 |
| **Licence** | CC-BY-4.0 (contenus) / MIT (scripts) — voir `LICENSE` |

## 1. Objectif du dépôt

Ce dépôt constitue le **socle versionné** de l'écosystème numérique de thèse. Il centralise
les livrables du mini-projet *« Mon écosystème numérique de thèse »* (consignes Slide 38) et
permet la traçabilité, la reproductibilité et le partage ouvert des productions liées à la thèse.
L'algue brune *Rugulopteryx okamurae* (Dictyotales, Ochrophyta), originaire du Pacifique
Nord-Ouest et signalée pour la première fois dans le détroit de Gibraltar en 2015, fait
l'objet d'une invasion massive des côtes méditerranéennes marocaines. La thèse vise à
caractériser son profil phytochimique et à évaluer le potentiel bioactif de ses métabolites.

## 2. Arborescence du dépôt

```
rugulopteryx-okamurae-these/
├── README.md                  # Ce fichier — présentation et arborescence
├── LICENSE                    # Licence CC-BY-4.0 (contenus) + MIT (scripts)
├── CITATION.cff               # Métadonnées de citation ( Zenodo / GitHub)
├── .gitignore                 # Fichiers exclus du versionnement
├── references.bib             # Bibliographie Zotero exportée (22 références)
├── Charte_IA.md               # Charte personnelle d'usage de l'IA (½ page)
├── docs/
│   ├── PGD_Rugulopteryx_okamurae.pdf      # Plan de gestion des données (2 pages)
│   └── Rapport_Ecosysteme_Numerique_These.pdf  # Rapport final du mini-projet
├── data/
│   ├── README.md              # Description des jeux de données
│   └── exemple_metabolites.csv # Jeu d'exemple (métabolites, illustratif)
├── scripts/
│   ├── README.md              # Description des scripts
│   └── analyse_phytochimique.py # Script d'exemple (stats + figure)
└── results/
    ├── README.md              # Description des sorties
    ├── statistiques_par_classe.csv  # Sortie du script (exemple)
    └── aire_pic_par_compose.png      # Figure (exemple)
```

## 3. Contenu des livrables

| Livrable | Fichier / lien | Description |
|---|---|---|
| 1. Identité (ORCID) | <https://orcid.org/0009-0002-7946-4934> | Profil ORCID complété |
| 2. Bibliothèque Zotero | `references.bib` | 22 références, organisées par mots-clés, exportées en `.bib`, rétractations vérifiées |
| 3. Plan de gestion des données | `docs/PGD_Rugulopteryx_okamurae.pdf` | PGD de 2 pages (modèle DMP OPIDoR) |
| 4. Dépôt Git | ce dépôt | README, licence, arborescence claire, ≥ 3 commits |
| 5. Charte IA | `Charte_IA.md` | Bilan de l'activité 2 + charte personnelle (½ page) |

## 4. Vérification des rétractations

Les 22 références bibliographiques ont été vérifiées le **15/11/2026** via
[Crossref](https://www.crossref.org) et [Retraction Watch](https://retractionwatch.com).
Aucune rétractation (*retraction*) ni expression de préoccupation (*expression of concern*)
n'a été identifiée pour l'une quelconque des références incluses.

## 5. Historique des commits

```
* dcbb110 (HEAD -> main) Fichiers d'exemple (data CSV, script, results) + CITATION.cff
* 43bc509 Ajout du rapport final dans docs/ + mise a jour du README
* 17febc1 Ajout du Plan de Gestion des Donnees (PGD) dans docs/
* 7c79f29 Ajout de la charte personnelle d'usage de l'IA (activite 2)
* 2cfa4e4 Structuration arborescence (data, scripts) + references.bib (22 refs)
* aeced97 Initialisation du depot - README, LICENSE et .gitignore
```

Soit 6 commits significatifs sur la branche `main`.

## 6. Licence

- **Contenus** (documents, données, figures, bibliographie) : Creative Commons
  Attribution 4.0 International (CC-BY-4.0).
- **Scripts et code** : licence MIT.

Voir le fichier `LICENSE` pour le texte intégral.

## 7. Contact

Jihan El-khattabi — ORCID : <https://orcid.org/0009-0002-7946-4934>
Laboratoire de Biologie, Écologie et Santé (LBECS)
