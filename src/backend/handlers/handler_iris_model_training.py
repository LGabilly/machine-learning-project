from src.backend.config.iris import logger
from src.core.model_training import train


class IrisModelTrainingHandler:
    def retrain_model(self) -> bool:
        logger.info("retrain_model called")
        train()
        return True


iris_prediction_handler = IrisModelTrainingHandler()
