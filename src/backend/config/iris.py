from config import Logger, Settings


class IrisSettings(Settings):
    PROJECT_NAME: str = "iris-prediction"
    API_NAME: str = "Iris deluxe"
    API_VERSION: str = "1.0"
    API_PORT: int = 8084


settings = IrisSettings()
logger = Logger(name=settings.PROJECT_NAME)
