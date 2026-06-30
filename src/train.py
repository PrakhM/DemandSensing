from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

import pandas as pd

def train_random_forest(df):

    X = df.drop(
        columns=["90_days_sales", "date", "sku_id"]
    )

    y = df["90_days_sales"]

    X = pd.get_dummies(X)


    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    return [model, X_test, y_test]