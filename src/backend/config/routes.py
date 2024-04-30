from enum import Enum, unique


@unique
class IrisRoutes(str, Enum):
    prefix = "/v1/iris"
    prediction = "/prediction"
    train = "/train"
