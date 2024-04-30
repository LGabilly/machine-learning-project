import logging
import sys
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pythonjsonlogger import jsonlogger


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    PROJ_NAME: str = "Complete machine learning api"
    LOG_LEVEL: str = "DEBUG"
    PROJ_DIR: Path = Path(__file__).parent
    DATA_DIR: Path = PROJ_DIR / "data"
    SRC_DIR: Path = PROJ_DIR / "src"
    NB_DIR: Path = PROJ_DIR / "nb"
    ASSET_DIR: Path = PROJ_DIR / "asset"
    MODEL_DIR: Path = ASSET_DIR / "ml_model"
    IMG_DIR: Path = ASSET_DIR / "img"


base_settings = Settings()


class Logger(logging.Logger):
    def __init__(self, name: str):
        super().__init__(name)
        self.setLevel(base_settings.LOG_LEVEL)
        logformat = "[%(asctime)s] %(levelname)s %(name)s : %(message)s"
        logHandler = logging.StreamHandler(sys.stdout)
        formatter = jsonlogger.JsonFormatter(logformat)
        logHandler.setFormatter(formatter)
        self.handlers.clear()
        self.addHandler(logHandler)


base_logger = Logger(name=base_settings.PROJ_NAME)
