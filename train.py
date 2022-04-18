import mlflow

with mlflow.start_run():
    mlflow.log_param('my_param', 99)
    mlflow.log_metric('my_metric', 1.234)
    mlflow.set_tag('mlflow.source.type','PROJECT')
    mlflow.set_tag(
        'mlflow.source.git.repoURL', 
        'https://github.com/adin786/mlflow-test.git'
        )