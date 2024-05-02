from config import Logger, Settings


class IrisSettings(Settings):
    PROJECT_NAME: str = "iris-dashboard"
    BACKEND_URL: str = "http://localhost:8084"
    API_ROUTE: str = "/v1/iris/prediction"
    TRAIN_ROUTE: str = "/v1/iris/train"


settings = IrisSettings()
logger = Logger(name=settings.PROJECT_NAME)
