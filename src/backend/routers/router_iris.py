from fastapi.routing import APIRouter

from src.backend.config.routes import IrisRoutes
from src.backend.handlers.handler_iris_model_training import IrisModelTrainingHandler
from src.backend.handlers.handler_iris_predict import IrisPredictionHandler
from src.backend.models.iris import IrisRequest, IrisResponse

router = APIRouter(prefix=IrisRoutes.prefix)
iris_prediction = IrisPredictionHandler()
iris_trainer = IrisModelTrainingHandler()


@router.post(IrisRoutes.prediction, tags=["Iris", "Prediction"])
def router_iris_prediction(
    sepal_length_cm: float,
    sepal_width_cm: float,
    petal_length_cm: float,
    petal_width_cm: float,
) -> IrisResponse:
    params = IrisRequest(
        sepal_length_cm=sepal_length_cm,
        sepal_width_cm=sepal_width_cm,
        petal_length_cm=petal_length_cm,
        petal_width_cm=petal_width_cm,
    )

    return iris_prediction.single_prediction(params)


@router.post(IrisRoutes.train, tags=["Iris", "Train"])
def router_iris_train() -> float:
    return iris_trainer.retrain_model()
