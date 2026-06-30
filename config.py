import os


class Config:
    """Application configuration."""

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "development-secret-key"
    )

    PROJECT_NAME = "Mini Sports Analytics Web App"

    DATA_FOLDER = "data"

    RAW_DATA_FOLDER = os.path.join(DATA_FOLDER, "raw")

    PROCESSED_DATA_FOLDER = os.path.join(DATA_FOLDER, "processed")

    PLOT_FOLDER = os.path.join("static", "images", "plots")