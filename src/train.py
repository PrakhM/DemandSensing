from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

import pandas as pd

def preprocess_and_sep(df):

    df["date"] = pd.to_datetime(df["date"])

    df["month"] = df["date"].dt.month
    df["day_of_week"] = df["date"].dt.dayofweek
    df["year"] = df["date"].dt.year

    X = df.drop(
        columns=["90_days_sales", "date", "sku_id", "subcategory", "category"]
    )

    y = df["90_days_sales"]

    X = pd.get_dummies(X, drop_first = True)

    return X, y

def train_random_forest(df):

    df = df.sort_values("date")
    X, y = preprocess_and_sep(df)

    split_idx = int(len(df) * 0.8)

    X_train = X.iloc[:split_idx]
    y_train = y.iloc[:split_idx]

    X_test = X.iloc[split_idx:]
    y_test = y.iloc[split_idx:]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    print(X.head())

    return [model, X_test, y_test]