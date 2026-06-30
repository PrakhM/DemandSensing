from train import train_random_forest
from metrics import measure

import pandas as pd
from pathlib import Path

import joblib


df = pd.read_csv("Data/ethnic_sale_data.csv")
survey_df = pd.read_csv("Data/survery.csv")

random_forest_model_and_tests = train_random_forest(df)
random_forest_model = random_forest_model_and_tests[0]
X_test = random_forest_model_and_tests[1]
y_test = random_forest_model_and_tests[2]

measure(random_forest_model, X_test, y_test)

joblib.dump(random_forest_model, "rf_model.pkl")
joblib.dump(X_test.columns.tolist(), "model_columns.pkl")
