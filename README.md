# A responsible model on Algorithmia, reporting back its issues

This algo is only a showcase for my POC integration between Github Actions and Algorithmia. 

The algorithm itself trains a vanilla TF model on FashionMNIST and checks its performance against the provided metrics and thresholds, passed to it through my POC Github action at [Algorithmia-Github Issue Hook action] (https://github.com/marketplace/actions/algorithmia-github-issue-hook)

So the basic gist is: 
```
def eval_model_perf(input):
    input_dict = json.loads(input)
    eval_params = input_dict["eval_params"]
    metric = eval_params["metric"]
    final_train_metric, final_val_metric, test_metric = train_eval_model(metric)

    threshold = eval_params["threshold"]
    if test_metric < threshold:
        github_params = input_dict["github_params"]
        issue_title = f"Test {metric} below {threshold}"
        issue_body = f"Train {metric}: {final_train_metric}, Validation {metric}: {final_val_metric}"
        create_github_issue(github_params, issue_title, issue_body)
        return "Houston we have a Github issue!"
    else:
        return "Good job model, keep going!"
```

and you'll get an issue on your repo that looks like this [Test accuracy below 0.85 ](https://github.com/aslisabanci/algorithmia_perf_track/issues/10) when your model has something to report back.
