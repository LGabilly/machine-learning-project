from src.backend.config.iris import logger
from src.core.model_training import train


class IrisModelTrainingHandler:
    def retrain_model(self) -> float:
        logger.info("retrain_model called")
        accuracy = train()
        return accuracy


iris_prediction_handler = IrisModelTrainingHandler()
