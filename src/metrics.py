import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

def measure(model, X_test, y_test):

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(mean_squared_error(
        y_test,
        predictions
    ))

    r2 = r2_score(
        y_test,
        predictions
    )

    print("MAE:", mae)
    print("RMSE:", rmse)
    print("R2 Score:", r2)