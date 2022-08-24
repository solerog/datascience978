# Day 32 - Model Lifecycle

MLFlow is used to store data from different models and different runs.
Parameters, models and metrics are stored.

[LeWagon MLFlow](https://mlflow.lewagon.ai/)

**Cloud storage**:

- Immutable data
- Buckets and blobs
- Files, images, sound, video

**Big Query**:

- Relational data
- Columnar storage

**Compute Engine**:

- Virtual machine
- Run models in the cloud

## Experiment tracking

**Tracking requirements**:

- **Data** version:
- Experiment **parameters**:
  - Code version
  - Parameters
  - Training environment
  - Preprocessing type
  - Model hyperparameters
- Experiment **metrics**
- Model **version**

## MLFlow

There can be many runs inside an experiment.

```python
import mlflow

mlflow.set_tracking_uri("https://mlflow.lewagon.ai")
mlflow.set_experiment(experiment_name="wagoncab taxifare")
```

```python
with mlflow.start_run():

    params = dict(batch_size=256, row_count=100_000)
    metrics = dict(rmse=0.456)

    mlflow.log_params(params)
    mlflow.log_metrics(metrics)

    mlflow.keras.log_model(keras_model=model,
                           artifact_path="model",
                           keras_module="tensorflow.keras",
                           registered_model_name="taxifare_model")
```

The models have to be set in production.

## Model Lifecycle

We'll use [**Prefect**](https://docs-v1.prefect.io/) to automate the **Model Workflow**.

Create workflow by adding annotations.
Run workflow locally.

Tasks have to be created:

```python
from taxifare_model.interface.main import (preprocess, train, evaluate)

from prefect import task

@task
def eval_perf(next_row):
    past_perf = evaluate(next_row)
    return past_perf

@task
def train_model(next_row):
    preprocess(first_row=next_row)
    new_perf = train(first_row=next_row, stage="Production")
    return new_perf

@task
def notify(past_perf, new_perf):
    print(f"Past perf: {past_perf}, new perf: {new_perf}")
```

Workflow after tasks:

```python
from prefect import Flow


def build_flow(schedule):

    with Flow(name="wagonwab taxifare workflow", schedule=schedule) as flow:

        next_row = 0
        past_perf = eval_perf(next_row)
        new_perf = train_model(next_row)
        notify(past_perf, new_perf)

    return flow
```

```python
import datetime

from prefect.schedules import IntervalSchedule
from prefect.executors import LocalDaskExecutor


if __name__ == "__main__":

    # schedule = None                    # no schedule
    schedule = IntervalSchedule(interval=datetime.timedelta(minutes=300))

    flow = build_flow(schedule)

    flow.visualize()

    # flow.run()                         # local run
    flow.executor = LocalDaskExecutor()  # parallel executor
    flow.register("wagoncab project")    # backend run
```
