import joblib
import numpy as np
from sklearn.datasets import load_iris

from src.backend.config.iris import logger, settings
from src.backend.models.iris import IrisRequest, IrisResponse

model = joblib.load(settings.MODEL_DIR / "model_random_forest_classifier.joblib")
iris = load_iris()


def predict_species(params: IrisRequest) -> IrisResponse:
    features = np.array(
        [
            params.sepal_length_cm,
            params.sepal_width_cm,
            params.petal_length_cm,
            params.petal_width_cm,
        ]
    ).reshape(1, -1)
    prediction = model.predict(features)
    class_name = iris.target_names[prediction][0]  # type: ignore
    logger.info(f"Prediction : {class_name=}")
    return IrisResponse(
        sepal_length_cm=params.sepal_length_cm,
        sepal_width_cm=params.sepal_width_cm,
        petal_length_cm=params.petal_length_cm,
        petal_width_cm=params.petal_width_cm,
        species=class_name,
    )


if __name__ == "__main__":
    print(
        predict_species(
            IrisRequest(
                sepal_length_cm=5.1,
                sepal_width_cm=3.5,
                petal_length_cm=1.4,
                petal_width_cm=0.2,
            )
        )
    )
