import time

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from src.backend.config.iris import logger, settings


def train():
    begin_time = time.time()
    # Load dataset
    data = load_iris()
    X, y = data.data, data.target  # type: ignore

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = float(accuracy_score(y_test, y_pred))

    joblib.dump(model, settings.MODEL_DIR / "model_random_forest_classifier.joblib")

    end_time = time.time()

    logger.info(
        f"Model trained in {end_time - begin_time:.2f} seconds, with {accuracy:.2f} accuray"
    )

    return accuracy


if __name__ == "__main__":
    train()
