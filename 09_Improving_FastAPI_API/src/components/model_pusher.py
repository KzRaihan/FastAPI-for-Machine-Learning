import pickle
from pathlib import Path

from src.config.paths import MODEL_PATH


def save_model(model, path: Path = MODEL_PATH) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)  # create folder if missing
    with open(path, "wb") as f:
        pickle.dump(model, f)
    return path