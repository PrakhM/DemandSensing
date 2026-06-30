import pandas as pd
from product import create_product

import joblib

model = joblib.load("rf_model.pkl")
model_columns = joblib.load("model_columns.pkl")

survey_df = pd.read_csv("Data/survery.csv")

cities, product_X = create_product(survey_df)
product_X = product_X.reindex(columns=model_columns, fill_value=False)
print(cities, "\n", model.predict(product_X), sep = "")