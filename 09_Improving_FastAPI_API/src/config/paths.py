from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "artifact" / "data" / "insurance.csv"
MODEL_PATH = BASE_DIR / "artifact" / "trained_model" / "model.pkl"
