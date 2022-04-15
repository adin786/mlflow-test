import mlflow

with mlflow.start_run():
    mlflow.log_param('my_param', 99)
    mlflow.log_metric('my_metric', 1.234)