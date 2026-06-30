# ==========================================================
# FILE: preprocessing.py 
# ==========================================================

import pandas as pd
import os

from config import Config
from app.services.data_loader import load_worldcup_data


# ----------------------------------------------------------
# Output file path
# ----------------------------------------------------------
PROCESSED_FILE_NAME = "cleaned_worldcup_matches.csv"


def get_processed_path():
    return os.path.join(
        Config.PROCESSED_DATA_FOLDER,
        PROCESSED_FILE_NAME
    )


# ----------------------------------------------------------
# Cleaning steps
# ----------------------------------------------------------
def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def handle_missing_values(df):
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("unknown")
        else:
            df[col] = df[col].fillna(0)
    return df


# ----------------------------------------------------------
# MAIN PIPELINE
# ----------------------------------------------------------
def preprocess_worldcup_data(save=True):
    """
    Full preprocessing pipeline.

    If save=True → saves cleaned dataset to /data/processed
    """

    df = load_worldcup_data()

    # Step 1: clean columns
    df = clean_column_names(df)

    # Step 2: missing values
    df = handle_missing_values(df)

    # Step 3: save processed dataset
    if save:
        output_path = get_processed_path()

        # ensure folder exists
        os.makedirs(Config.PROCESSED_DATA_FOLDER, exist_ok=True)

        df.to_csv(output_path, index=False)

        print(f"\n✅ Processed data saved at: {output_path}")

    return df


# ----------------------------------------------------------
# preview helper
# ----------------------------------------------------------
def preview_cleaned_data(n=5):
    df = preprocess_worldcup_data(save=False)
    return df.head(n)