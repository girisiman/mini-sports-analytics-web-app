import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.preprocessing import preprocess_worldcup_data


def test_preprocessing():
    df = preprocess_worldcup_data()

    assert df is not None
    assert len(df) > 0

    print("\n✅ PREPROCESSING SUCCESS")
    print(df.head())


if __name__ == "__main__":
    test_preprocessing()