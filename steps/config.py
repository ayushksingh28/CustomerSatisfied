from zenml.steps import BaseParameters


class ModelNameConfig(BaseParameters):

    model_name: str = "lightgbm"
    fine_tuning: bool = False
