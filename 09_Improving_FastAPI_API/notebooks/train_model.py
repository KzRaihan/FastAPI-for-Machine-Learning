# Train and save your Machine Learning model here.
# Import Necessary Libraries
import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, accuracy_score
import pickle

from src.config.city_tier import tier_1_cities, tier_2_cities


# load the data
def load_data() -> DataFrame:
    file_path = "data/insurance.csv"
    try:
        df = pd.read_csv(file_path)
        print(f"File is Loaded Successfully")
        return df
    except Exception as e:
        raise f"No such file or directory {e}"

# Method 2: feature_engineering
def feature_engineering(df: DataFrame) -> DataFrame:
    df_feat = df.copy()

    # Feature 1: BMI
    df_feat["bmi"] = df_feat["weight"] / (df_feat["height"] ** 2)

    # Feature 2: Age Group
    def age_group(age):
        if age < 25:
            return "young"
        elif age < 45:
            return "adult"
        elif age < 60:
            return "middle_aged"
        return "senior"

    df_feat["age_group"] = df_feat["age"].apply(age_group)

    # Feature 3: Lifestyle Risk
    def lifestyle_risk(row):
        if row["smoker"] and row["bmi"] > 30:
            return "high"
        elif row["smoker"] or row["bmi"] > 27:
            return "medium"
        else:
            return "low"
    df_feat["lifestyle_risk"] = df_feat.apply(lifestyle_risk, axis=1)

    # Feature 4: City Tier
    def city_tier(city):
        if city in tier_1_cities:
            return 1
        elif city in tier_2_cities:
            return 2
        else:
            return 3

    df_feat["city_tier"] = df_feat["city"].apply(city_tier)

    # Drop the Unnessary columns
    df_feat.drop(columns=['age', 'weight', 'height', 'smoker', 'city'], inplace = True)

    return df_feat


# Method 3: split_X_y
def split_X_y():
    df = load_data()
    df_feat = feature_engineering(df)

    # Select features and target
    X = df_feat.drop("insurance_premium_category", axis=1)
    y = df_feat["insurance_premium_category"]

    return X,y

def cat_num_features():
    # Define categorical and numeric features
    categorical_features = ["age_group", "lifestyle_risk", "occupation", "city_tier"]
    numeric_features = ["bmi", "income_lpa"]


    return categorical_features, numeric_features


# Method 4: ML_pipeline
def ML_pipeline():
    
    categorical_features, numeric_features = cat_num_features()

    # Create column transformer for OHE
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(), categorical_features),
            ("num", "passthrough", numeric_features)
        ]
    )

    # Create a pipeline with preprocessing and random forest classifier
    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(random_state=42))
    ]) 

    return pipeline   

# Method 6: train_model
def train_model():
    X, y = split_X_y()
   
    pipeline = ML_pipeline()

    # Split data and train model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    
    model = pipeline.fit(X_train, y_train)

    return model, X_test, y_test
    

# method 7: evaluation the model
def evaluation(model):
    model, X_test, y_test = train_model()
    
    y_pred = model.predict(X_test)

    accuracy_score = accuracy_score(y_test, y_pred)

    classification_report = classification_report(y_test, y_pred)

    return accuracy_score, classification_report

# method 8: download the trained model
def download_model():
    model, _, _ = train_model()

    # Save the trained pipeline using pickle
    pickle_model_path = "artifact/model.pkl"

    with open(pickle_model_path, "wb") as f:
        pickle.dump(model, f)

