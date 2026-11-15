#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analyse_phytochimique.py
========================

Script d'exemple d'analyse des donnees phytochimiques de Rugulopteryx okamurae.

Lit le fichier de metabolites (data/exemple_metabolites.csv), calcule des
statistiques descriptives par classe de compose et par site de prelevement,
puis genere un diagramme en barres de l'aire des pics (proxy de la quantite
relative de chaque metabolite).

Auteur   : Jihan El-khattabi (ORCID: 0009-0002-7946-4934)
Laboratoire : Biologie, Ecologie et Sante (LBECS)
Date     : 15/11/2026

Entrees :
    data/exemple_metabolites.csv   (colonnes : compound, class, retention_time_min,
                                    peak_area, site)
Sorties :
    results/statistiques_par_classe.csv
    results/aire_pic_par_compose.png

Dependances : pandas, matplotlib

Usage :
    python scripts/analyse_phytochimique.py
"""

import os
import sys
from pathlib import Path

import pandas as pd

# --- Configuration des chemins (relatifs a la racine du depot) ----------------
RACINE = Path(__file__).resolve().parent.parent
FICHIER_DONNEES = RACINE / "data" / "exemple_metabolites.csv"
DOSSIER_RESULTATS = RACINE / "results"


def charger_donnees(chemin: Path) -> pd.DataFrame:
    """Charge le fichier CSV de metabolites."""
    if not chemin.exists():
        sys.exit(f"[ERREUR] Fichier introuvable : {chemin}")
    df = pd.read_csv(chemin)
    print(f"[INFO] {len(df)} lignes chargees depuis {chemin.name}")
    return df


def statistiques_par_classe(df: pd.DataFrame) -> pd.DataFrame:
    """Aire moyenne et totale des pics par classe de metabolite et par site."""
    stats = (df.groupby(["site", "class"])["peak_area"]
               .agg(["mean", "sum", "count"])
               .round(1)
               .reset_index()
               .rename(columns={"mean": "aire_moyenne",
                                "sum": "aire_totale",
                                "count": "n_composes"}))
    return stats


def generer_figure(df: pd.DataFrame, sortie: Path) -> None:
    """Genere un diagramme en barres de l'aire des pics par compose."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # Police gerant les eventuels accents / symboles
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
    palette = {"Diterpenoid": "#1F4E79",
               "Phlorotannin": "#2E7D32",
               "Fatty acid": "#B5651D"}

    for site in df["site"].unique():
        sous = df[df["site"] == site].sort_values("peak_area", ascending=True)
        ax.barh(sous["compound"] + f" ({site})",
                sous["peak_area"],
                color=[palette[c] for c in sous["class"]])

    ax.set_xlabel("Aire du pic HPLC (proxy de la quantite relative)")
    ax.set_title("Profil metabolique de Rugulopteryx okamurae par site")
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    fig.savefig(sortie, dpi=150)
    print(f"[INFO] Figure enregistree : {sortie}")


def main() -> None:
    DOSSIER_RESULTATS.mkdir(exist_ok=True)
    df = charger_donnees(FICHIER_DONNEES)

    stats = statistiques_par_classe(df)
    sortie_csv = DOSSIER_RESULTATS / "statistiques_par_classe.csv"
    stats.to_csv(sortie_csv, index=False)
    print(f"[INFO] Statistiques enregistrees : {sortie_csv}")
    print(stats.to_string(index=False))

    generer_figure(df, DOSSIER_RESULTATS / "aire_pic_par_compose.png")
    print("[OK] Analyse terminee avec succes.")


if __name__ == "__main__":
    main()
