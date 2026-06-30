from train import train_random_forest
from metrics import measure

import pandas as pd
from pathlib import Path


df = pd.read_csv("Data/ethnic_sale_data.csv")

random_forest_model_and_tests = train_random_forest(df)
random_forest_model = random_forest_model_and_tests[0]
X_test = random_forest_model_and_tests[1]
y_test = random_forest_model_and_tests[2]

measure(random_forest_model, X_test, y_test)
