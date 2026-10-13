import mlflow


def test_mlflow_roundtrip(tmp_path):
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("smoke-test")
    f = tmp_path / "hello.txt"
    f.write_text("it works")
    with mlflow.start_run():
        mlflow.log_param("hello", "world")
        mlflow.log_metric("score", 1.0)
        mlflow.log_artifact(str(f))
