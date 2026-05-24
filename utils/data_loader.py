import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


@staticmethod
def _path(filename):
    return DATA_DIR / filename


def load_macro() -> pd.DataFrame:
    """GDP, FDI, kinh tế số Việt Nam 2020-2025."""
    df = pd.read_csv(DATA_DIR / "vietnam_macro_2020_2025.csv")
    return df.sort_values("year").reset_index(drop=True)


def load_sectors() -> pd.DataFrame:
    """10 ngành kinh tế Việt Nam 2024."""
    return pd.read_csv(DATA_DIR / "vietnam_sectors_2024.csv")


def load_regions() -> pd.DataFrame:
    """6 vùng kinh tế-xã hội Việt Nam 2024."""
    return pd.read_csv(DATA_DIR / "vietnam_regions_2024.csv")
