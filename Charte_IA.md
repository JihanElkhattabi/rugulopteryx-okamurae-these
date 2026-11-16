# Charte personnelle d'usage de l'intelligence artificielle

| | |
|---|---|
| **Doctorante** | Jihan El-khattabi — ORCID : <https://orcid.org/0009-0002-7946-4934> |
| **Thèse** | Étude phytochimique de *Rugulopteryx okamurae* dans la Méditerranée marocaine |
| **Version** | 1.1 |
| **Adoptée le** | 15 novembre 2026 — révisée le 16 novembre 2026 |
| **Dépôt source** | <https://github.com/JihanElkhattabi/rugulopteryx-okamurae-these> |

---

## 1. Bilan du test d'un assistant IA (activité 2)

Lors de l'activité 2, j'ai soumis à un assistant conversationnel (GLM, modèle
zgo/glm-5.2) une requête portant sur les composés bioactifs de
*Rugulopteryx okamurae*. L'outil a produit un texte structuré et plausible, mais
l'examen critique a révélé trois limites majeures :

1. **Inventions de références** — trois articles sur cinq n'existaient pas dans les
   bases CrossRef et PubMed (halucination bibliographique).
2. **Structures chimiques erronées** — un diterpénoïde a été attribué à tort à la
   classe des spatanes, alors qu'il appartient aux dictyols.
3. **Absence de sources vérifiables** — les dosages en phlorotannines avancés par
   l'outil n'étaient rattachés à aucune étude identifiable.

Ce test confirme qu'un assistant IA est utile pour la rédaction, la formulation
d'hypothèses et la synthèse, mais qu'il **ne peut en aucun cas se substituer à la
lecture critique des sources primaires**.

---

## 2. Périmètre d'usage

| Usages acceptables | Usages prohibés |
|---|---|
| Reformulation, correction syntaxique et orthographique | Fabriquer des données, citations ou références non vérifiées |
| Structuration d'un plan ou d'un sommaire | Reproduire des extraits protégés par le droit d'auteur |
| Génération de code d'analyse (à valider et tester) | Soumettre des données non publiées ou confidentielles |
| Synthèse explicative d'un concept (à vérifier) | Signer un contenu scientifique produit uniquement par l'IA |
| Recherche d'idées et formulation d'hypothèses | Remplacer la lecture critique des sources primaires |

---

## 3. Principes engagements

Dans le cadre de ma thèse, je m'engage à respecter les principes suivants :

1. **Transparence** — je signale explicitement, dans tout livrable, les passages
   rédigés avec l'aide d'une IA ; je nomme l'outil, le modèle et la date
   d'utilisation.
2. **Vérification systématique** — toute référence, donnée chiffrée ou structure
   chimique produite par une IA est vérifiée dans une source primaire (CrossRef,
   PubMed, AlgaeBase, Scopus) avant d'être intégrée.
3. **Aucune donnée fabriquée** — je n'introduis jamais de résultat, de citation ou
   de référence qui n'aurait pas été contrôlé ; en cas de doute, la mention est
   retirée.
4. **Respect de la propriété intellectuelle** — je ne demande pas à l'IA de
   reproduire des extraits protégés et je cite mes sources selon les normes
   bibliographiques en vigueur.
5. **Protection des données sensibles** — je ne transmets jamais de données non
   publiées, de résultats intermédiaires ou d'informations confidentielles à un
   outil tiers.
6. **Responsabilité** — je reste seule responsable du contenu scientifique de mes
   productions ; l'IA est un assistant, non une autorité.

---

## 4. Transparence — livrables AI-assistés du mini-projet Module 5

Conformément au principe 1, je déclare ici l'usage de l'IA (GLM, zgo/glm-5.2)
dans la production de ce mini-projet :

| Livrable | Nature de l'assistance IA | Vérification humaine |
|---|---|---|
| Bibliothèque Zotero (`references.bib`) | Aucune — 22 références issues de recherche manuelle | Intégrale (CrossRef/PubMed) |
| Plan de gestion des données (`docs/PGD_*.pdf`) | Structuration du plan selon le modèle OPIDoR | Révision et adaptation au sujet |
| Dépôt Git (`README.md`, `.gitignore`, arborescence) | Rédaction du README et du `.gitignore` | Révision et validation |
| Script d'analyse (`scripts/analyse_phytochimique.py`) | Génération du squelette de code | Test et exécution effective |
| Rapport de synthèse (`docs/Rapport_*.pdf`) | Aide à la rédaction et à la structuration | Vérification des faits et des chiffres |
| **Présente charte** | Rédaction assistée | Adoption et signature personnelle |

Aucune donnée scientifique n'a été produite uniquement par l'IA ; toutes les
références bibliographiques ont été vérifiées dans des bases peer-reviewed.

---

*Charte adoptée le 15 novembre 2026, révisée le 16 novembre 2026 — Jihan El-khattabi.*
