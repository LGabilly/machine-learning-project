from src.backend.config.iris import logger
from src.backend.models.iris import IrisRequest, IrisResponse
from src.core.predict import predict_species


class IrisPredictionHandler:
    def single_prediction(self, params: IrisRequest) -> IrisResponse:
        logger.info("predict_species called")
        return predict_species(params)


iris_prediction_handler = IrisPredictionHandler()
