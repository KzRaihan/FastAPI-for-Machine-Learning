import numpy as np
from pandas import DataFrame
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from src.config.city_tier import tier_1_cities, tier_2_cities

TARGET = "insurance_premium_category"
CATEGORICAL_FEATURES = ["age_group", "lifestyle_risk", "occupation", "city_tier"]
NUMERIC_FEATURES = ["bmi", "income_lpa"]

# Method 1: add_features
def add_features(df: DataFrame) -> DataFrame:
    """Single source of truth for feature engineering (training AND prediction)."""
    df_feat = df.copy()

    city = df_feat["city"].str.strip().str.title()

    # New Feature 1: bmi
    df_feat["bmi"] = df_feat["weight"] / (df_feat["height"] ** 2)

    # New Feature 2: age_group
    df_feat["age_group"] = np.select(
        [df_feat["age"] < 25, df_feat["age"] < 45, df_feat["age"] < 60],
        ["young", "adult", "middle_aged"],
        default="senior",
    )

    # New Feature 2: lifestyle_risk
    df_feat["lifestyle_risk"] = np.select(
        [df_feat["smoker"] & (df_feat["bmi"] > 30),
         df_feat["smoker"] | (df_feat["bmi"] > 27)],
        ["high", "medium"],
        default="low",
    )

    # New Feature 3: city_tier
    df_feat["city_tier"] = np.select(
        [city.isin(tier_1_cities), city.isin(tier_2_cities)],
        [1, 2],
        default=3,
    )

    return df_feat.drop(columns=["age", "weight", "height", "smoker", "city"])


# Method 2: split_X_y
def split_X_y(df: DataFrame):
    df_feat = add_features(df)
    X = df_feat.drop(columns=[TARGET])
    y = df_feat[TARGET]
    return X, y


def ML_pipeline() -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
            ("num", "passthrough", NUMERIC_FEATURES),
        ]
    )
    return Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(random_state=42)),
    ])



    # # Create a pipeline with preprocessing and random forest classifier
    # pipeline = Pipeline(steps=[
    #     ("preprocessor", preprocessor),
    #     ("classifier", RandomForestClassifier(random_state=42))
    # ]) 

    # return pipeline  