# ==========================================================
# FILE: test_eda.py
#
# PURPOSE
# ----------------------------------------------------------
# Unit tests for EDA module based on World Cup dataset.
#
# Ensures:
# - EDA functions run without errors
# - Required keys exist in outputs
# - Data structure is valid
#
# ==========================================================

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.eda import run_eda


# ----------------------------------------------------------
# Test full EDA pipeline
# ----------------------------------------------------------
def test_run_eda():
    report = run_eda()

    assert isinstance(report, dict), "EDA output must be a dictionary"

    # Core required sections
    required_keys = [
        "tournament_overview",
        "geography",
        "matches_by_year",
        "top_teams",
        "stage_distribution"
    ]

    for key in required_keys:
        assert key in report, f"Missing key: {key}"

    print("\n✅ EDA TEST PASSED")
    print("\n--- SAMPLE OUTPUT ---")
    print(report)


# ----------------------------------------------------------
# Run tests
# ----------------------------------------------------------
if __name__ == "__main__":
    print("\n==============================")
    print(" RUNNING EDA TESTS")
    print("==============================")

    test_run_eda()

    print("\n==============================")
    print(" ALL EDA TESTS COMPLETED")
    print("==============================")