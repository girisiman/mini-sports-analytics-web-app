# ==========================================================
# FILE: eda.py (DESIGNED AS PER DATASET)
# ==========================================================

import pandas as pd
import os
from config import Config


FILE_NAME = "cleaned_worldcup_matches.csv"


def load_data():
    path = os.path.join(Config.PROCESSED_DATA_FOLDER, FILE_NAME)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Processed data not found at {path}")

    return pd.read_csv(path)


# ----------------------------------------------------------
# 1. TOURNAMENT OVERVIEW
# ----------------------------------------------------------
def tournament_overview():
    df = load_data()

    return {
        "total_matches": len(df),
        "unique_years": df["year"].nunique(),
        "unique_stadiums": df["stadium"].nunique(),
        "unique_cities": df["city"].nunique()
    }


# ----------------------------------------------------------
# 2. GEOGRAPHY ANALYSIS
# ----------------------------------------------------------
def geography_analysis():
    df = load_data()

    top_cities = df["city"].value_counts().head(5).to_dict()
    top_stadiums = df["stadium"].value_counts().head(5).to_dict()

    return {
        "top_cities": top_cities,
        "top_stadiums": top_stadiums
    }


# ----------------------------------------------------------
# 3. MATCH DISTRIBUTION BY YEAR
# ----------------------------------------------------------
def matches_by_year():
    df = load_data()

    return df["year"].value_counts().sort_index().to_dict()


# ----------------------------------------------------------
# 4. TEAM PARTICIPATION ANALYSIS
# ----------------------------------------------------------
def team_participation():
    df = load_data()

    teams = pd.concat([
        df["home_team_initials"],
        df["away_team_initials"]
    ])

    return teams.value_counts().head(10).to_dict()


# ----------------------------------------------------------
# 5. MATCH STAGE ANALYSIS
# ----------------------------------------------------------
def stage_analysis():
    df = load_data()

    return df["stage"].value_counts().to_dict()


# ----------------------------------------------------------
# FULL EDA REPORT
# ----------------------------------------------------------
def run_eda():
    return {
        "tournament_overview": tournament_overview(),
        "geography": geography_analysis(),
        "matches_by_year": matches_by_year(),
        "top_teams": team_participation(),
        "stage_distribution": stage_analysis()
    }