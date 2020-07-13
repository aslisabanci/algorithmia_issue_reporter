# A responsible algorithm on Algorithmia, reporting back its own performance as Github issues

This algo is only a showcase for my POC integration between Github Actions and Algorithmia. 

The algorithm uses the POC Github action at [Algorithmia-Github Issue Hook action] (https://github.com/marketplace/actions/algorithmia-github-issue-hook) as a workflow and with the configuration params it receives through this Github action, it performs very simple steps. 

The main parameters passed to the algorithm are: 
- metric
- threshold
- model checkpoints path
- Github token, Github repo name, latest commit SHA

Using these, the algorithm does the following steps:
- Compiles the model for the given metric
- Loads a Tensorflow model using the checkpoints from the given path (here we used a local path, but you can also make use of Algorithmia's Data Sources or even better, load a pre-trained model from a saved model file)
- Evaluates the loaded model on the test set
- Compares the test performance (for the given metric) with the given threshold
- If the performance is below the threshold, it creates a Github issue using the Github params, that looks like this: TBD
