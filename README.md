DRPChallenge<https://github.com/DrpChallenge/main/tree/main>を拡張

epymarl/mainを実行  
Run epymarl/main

```
python3 src/main.py --config=qmix --env-config=gymma with env_args.time_limit=100 env_args.key="drp_env:drp-4agent_map_8x5-v2" env_args.state_repre_flag="onehot_fov"
```

安全制約ありの実行  
Run with safe one  
This uses safe wrapper
```
python3 src/main.py --config=qmix --env-config=gymma with env_args.time_limit=100 env_args.key="drp_env:drp_safe-4agent_map_8x5-v2" env_args.state_repre_flag="onehot_fov"
```
