import logging

import mlflow
import numpy as np
import pandas as pd
from model.evaluation import MSE, RMSE, R2Score
from sklearn.base import RegressorMixin
from typing_extensions import Annotated
from zenml import step
from zenml.client import Client

experiment_tracker = Client().active_stack.experiment_tracker
from typing import Tuple


@step(experiment_tracker=experiment_tracker.name)
def evaluation(
    model: RegressorMixin, x_test: pd.DataFrame, y_test: pd.Series
) -> Tuple[Annotated[float, "r2_score"], Annotated[float, "rmse"]]:

    try:
        # prediction = model.predict(x_test)
        # evaluation = Evaluation()
        # r2_score = evaluation.r2_score(y_test, prediction)
        # mlflow.log_metric("r2_score", r2_score)
        # mse = evaluation.mean_squared_error(y_test, prediction)
        # mlflow.log_metric("mse", mse)
        # rmse = np.sqrt(mse)
        # mlflow.log_metric("rmse", rmse)

        prediction = model.predict(x_test)

        mse_class = MSE()
        mse = mse_class.calculate_score(y_test, prediction)
        mlflow.log_metric("mse", mse)

        r2_class = R2Score()
        r2_score = r2_class.calculate_score(y_test, prediction)
        mlflow.log_metric("r2_score", r2_score)

        rmse_class = RMSE()
        rmse = rmse_class.calculate_score(y_test, prediction)
        mlflow.log_metric("rmse", rmse)
        
        return r2_score, rmse
    except Exception as e:
        logging.error(e)
        raise e
