import Algorithmia
from github import Github
import json

import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds


def create_github_issue(github_params: dict, issue_title: str):
    token = github_params["github_token"]
    github = Github(token)
    repo = github.get_repo(github_params["github_repo"])
    commit_hash = github_params["commit_sha"]
    hash_info = f"\n\n This issue was automatically created by the GitHub Action workflow. \n The commit sha was: _{commit_hash}_."
    issue = repo.create_issue(title=issue_title, body=hash_info)


def eval_model_perf(input):
    input_dict = json.loads(input)
    eval_params = input_dict["eval_params"]
    metric = eval_params["metric"]
    threshold = eval_params["threshold"]
    checkpoint_path = eval_params["checkpoints"]

    model = keras.models.Sequential(
        [
            keras.layers.Flatten(input_shape=[28, 28]),
            keras.layers.Dense(300, activation="relu"),
            keras.layers.Dense(100, activation="relu"),
            keras.layers.Dense(10, activation="softmax"),
        ]
    )
    model.compile(
        loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=[metric]
    )
    model.load_weights(checkpoint_path)
    _, (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
    _, test_metric = model.evaluate(X_test, y_test)

    if test_metric < threshold:
        github_params = input_dict["github_params"]
        issue_title = f"Test {metric} below {threshold}"
        create_github_issue(github_params, issue_title)
        return "Houston we have a Github issue!"
    else:
        return "Good job model, keep going!"


def apply(input):
    return eval_model_perf(input)


input_dict = {
    "github_params": {
        "github_token": "github_token",
        "github_repo": "aslisabanci/algorithmia_issue_reporter",
        "commit_sha": "a0ce353072c4b63c68d25bf43a1efb73e2f1bd66",
    },
    "eval_params": {
        "metric": "accuracy",
        "threshold": 0.85,
        "checkpoints": "data://asli/checkpoints/fashion_mnist_checkpoint",
    },
}

str = json.dumps(input_dict)
print(str)

