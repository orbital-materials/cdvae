Install requires torchmetrics==0.7.3
due to https://github.com/Lightning-AI/metrics/pull/914 .

Change the 'default' in `conf/default.yml` in order to run individual bits of the pipeline,


Put this in a .env file, make sure that the wandb exists!
```
export PROJECT_ROOT="/Users/markn/code/cdvae"
export HYDRA_JOBS="/Users/markn/code/cdvae/hydra"
export WABDB_DIR="/Users/markn/code/cdvae"
```

PYTHONPATH=. python cdvae/run.py expname=test_mini --config-name mini
