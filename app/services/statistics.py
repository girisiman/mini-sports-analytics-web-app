# ==========================================================
# FILE: statistics.py
#
# PURPOSE
# ----------------------------------------------------------
# Converts cleaned World Cup dataset into structured KPI
# metrics for dashboard consumption.
#
# OUTPUT GROUPS:
#   1. tournament_kpis
#   2. venue_kpis
#   3. competition_kpis
#   4. team_kpis
#   5. temporal_kpis
#
# ==========================================================

import pandas as pd
import os

from config import Config


FILE_NAME = "cleaned_worldcup_matches.csv"


# ----------------------------------------------------------
# Load processed dataset
# ----------------------------------------------------------
def load_data():
    path = os.path.join(Config.PROCESSED_DATA_FOLDER, FILE_NAME)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Processed dataset not found at {path}")

    return pd.read_csv(path)


# ==========================================================
# 1. TOURNAMENT KPIs
# ==========================================================
def tournament_kpis():
    df = load_data()

    return {
        "total_matches": int(len(df)),
        "total_teams": int(
            len(set(df["home_team_initials"]).union(set(df["away_team_initials"])))
        ),
        "total_stadiums": int(df["stadium"].nunique()),
        "total_cities": int(df["city"].nunique()),
        "total_years": int(df["year"].nunique())
    }


# ==========================================================
# 2. VENUE KPIs
# ==========================================================
def venue_kpis():
    df = load_data()

    return {
        "top_stadiums": df["stadium"].value_counts().head(5).to_dict(),
        "top_cities": df["city"].value_counts().head(5).to_dict()
    }


# ==========================================================
# 3. COMPETITION KPIs
# ==========================================================
def competition_kpis():
    df = load_data()

    # Match distribution by stage
    stage_distribution = df["stage"].value_counts().to_dict()

    return {
        "stage_distribution": stage_distribution
    }


# ==========================================================
# 4. TEAM KPIs
# ==========================================================
def team_kpis():
    df = load_data()

    teams = pd.concat([
        df["home_team_initials"],
        df["away_team_initials"]
    ])

    team_counts = teams.value_counts()

    return {
        "top_teams": team_counts.head(10).to_dict(),
        "team_participation_score": team_counts.to_dict()
    }


# ==========================================================
# 5. TEMPORAL KPIs
# ==========================================================
def temporal_kpis():
    df = load_data()

    matches_per_year = df["year"].value_counts().sort_index()

    # Peak year
    peak_year = matches_per_year.idxmax()
    peak_value = int(matches_per_year.max())

    return {
        "matches_per_year": matches_per_year.to_dict(),
        "peak_year": int(peak_year),
        "peak_matches": peak_value
    }


# ==========================================================
# FULL KPI REPORT
# ==========================================================
def generate_kpi_report():
    return {
        "tournament_kpis": tournament_kpis(),
        "venue_kpis": venue_kpis(),
        "competition_kpis": competition_kpis(),
        "team_kpis": team_kpis(),
        "temporal_kpis": temporal_kpis()
    }