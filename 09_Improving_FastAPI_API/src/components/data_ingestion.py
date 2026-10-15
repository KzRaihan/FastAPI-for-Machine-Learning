# Import Necessary Libraries
from pathlib import Path

import pandas as pd
from pandas import DataFrame
from src.config.paths import DATA_PATH, BASE_DIR


# load the data
def load_data() -> DataFrame:
    try:
        df = pd.read_csv(DATA_PATH)
        print("File is Loaded Successfully")
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Data file not found at: {DATA_PATH}") from e