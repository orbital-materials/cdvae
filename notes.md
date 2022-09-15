Install requires torchmetrics==0.7.3
due to https://github.com/Lightning-AI/metrics/pull/914 .

Change the 'default' in `conf/default.yml` in order to run individual bits of the pipeline,


Put this in a .env file, make sure that the wandb directory exists!
```
export PROJECT_ROOT="/Users/markn/code/cdvae"
export HYDRA_JOBS="/Users/markn/code/cdvae/hydra"
export WABDB_DIR="/Users/markn/code/cdvae"
```

PYTHONPATH=. python cdvae/run.py expname=test_mini --config-name mini

Note - for property optimization, we must have trained a property prediction model as well,
this is set by default to false for some reason. In the mini config I have set it to true instead.

### Evaluation

Running the generation task worked fine.

Trying to run the reconstruction task gave me this error:

```
(cdvae) markn@MacBook-Pro cdvae % PYTHONPATH=. python scripts/evaluate.py --model_path /Users/markn/code/cdvae/hydra/singlerun/2022-09-14/test_mini/ --tasks recon gen opt --batch_size 10 --num_batches_to_samples 2

Evaluate model on the reconstruction task.
batch 0 in 13
Traceback (most recent call last):
  File "scripts/evaluate.py", line 281, in <module>
    main(args)
  File "scripts/evaluate.py", line 195, in main
    all_frac_coords_stack, all_atom_types_stack, input_data_batch) = reconstructon(
  File "scripts/evaluate.py", line 70, in reconstructon
    input_data_list = input_data_list + batch.to_data_list()
  File "/Users/markn/anaconda3/envs/cdvae/lib/python3.8/site-packages/torch_geometric/data/batch.py", line 157, in to_data_list
    return [self.get(i) for i in range(self.num_graphs)]
  File "/Users/markn/anaconda3/envs/cdvae/lib/python3.8/site-packages/torch_geometric/data/batch.py", line 157, in <listcomp>
    return [self.get(i) for i in range(self.num_graphs)]
  File "/Users/markn/anaconda3/envs/cdvae/lib/python3.8/site-packages/torch_geometric/data/batch.py", line 90, in get
    data = separate(
  File "/Users/markn/anaconda3/envs/cdvae/lib/python3.8/site-packages/torch_geometric/data/separate.py", line 40, in separate
    data_store[attr] = _separate(attr, batch_store[attr], idx, slices,
  File "/Users/markn/anaconda3/envs/cdvae/lib/python3.8/site-packages/torch_geometric/data/separate.py", line 87, in _separate
    if decrement and (incs.dim() > 1 or int(incs[idx]) != 0):
AttributeError: 'NoneType' object has no attribute 'dim'

```

To fix it, I upgraded pytorch-geometric (not specified as a dependency, I think it is installed by ase)
```
pip install torch-geometric==2.0.4
```
