# ==========================================================
# FILE: data_loader.py
#
# PURPOSE
# ----------------------------------------------------------
# Centralized dataset loading service using Config paths.
#
# Now supports scalable architecture:
# - raw data
# - processed data
# - reusable loaders
#
# ==========================================================

import pandas as pd
import os
from config import Config


# ----------------------------------------------------------
# Dataset file name (only change here if dataset changes)
# ----------------------------------------------------------
RAW_FILE_NAME = "raw_worldcup_matches.csv"


# ----------------------------------------------------------
# Function: get_raw_data_path
# ----------------------------------------------------------
def get_raw_data_path():
    """
    Returns full path to raw dataset using Config.
    """

    return os.path.join(
        Config.RAW_DATA_FOLDER,
        RAW_FILE_NAME
    )


# ----------------------------------------------------------
# Function: load_worldcup_data
# ----------------------------------------------------------
def load_worldcup_data():
    """
    Loads World Cup dataset from raw folder.

    Returns:
        pd.DataFrame
    """

    file_path = get_raw_data_path()

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Dataset not found at: {file_path}"
        )

    df = pd.read_csv(file_path)

    return df


# ----------------------------------------------------------
# Function: preview_data
# ----------------------------------------------------------
def preview_data(n=5):
    """
    Returns first n rows of dataset.
    """

    df = load_worldcup_data()
    return df.head(n)


# ----------------------------------------------------------
# Function: dataset_summary
# ----------------------------------------------------------
def dataset_summary():
    """
    Returns dataset structure summary for EDA.
    """

    df = load_worldcup_data()

    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict()
    }