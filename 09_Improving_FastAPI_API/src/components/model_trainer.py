from sklearn.model_selection import train_test_split

from src.components.data_ingestion import load_data
from src.components.data_transformation import split_X_y, ML_pipeline

TEST_SIZE = 0.2
RANDOM_STATE = 1


def train_model():
    X, y = split_X_y(load_data())

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    model = ML_pipeline()
    model.fit(X_train, y_train)

    return model, X_test, y_test
