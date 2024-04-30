import time

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

from src.backend.config.iris import logger, settings


def train():
    begin_time = time.time()
    # Load dataset
    data = load_iris()
    X, y = data.data, data.target  # type: ignore

    # Train model
    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, settings.MODEL_DIR / "model_random_forest_classifier.joblib")

    end_time = time.time()

    logger.info(f"Model trained in {end_time - begin_time} seconds")


if __name__ == "__main__":
    train()
