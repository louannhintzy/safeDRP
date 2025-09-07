# SafeDRP Hybrid Extension  

This repository is an extension of the repository **SafeDRP** from [kaji-ou](https://github.com/kaji-ou/safeDRP),  
which is already an extension of [DRPChallenge](https://github.com/DrpChallenge/main/tree/main).  

We extend the original environment with a **hybrid action policy** that combines rule-based navigation and reinforcement learning (RL).  

---

## How to run ?  

While in **epymarl**:  

### Run normally  
```bash
python3 src/main.py --config=qmix --env-config=gymma with env_args.time_limit=100 env_args.key="drp_env:drp-4agent_map_8x5-v2" env_args.state_repre_flag="onehot_fov"

```
 
### Run with safe one  
This uses safe wrapper "dep_env/SafeMarlEnv/env_wrapper"
```bash
python3 src/main.py --config=qmix --env-config=gymma with env_args.time_limit=100 env_args.key="drp_env:drp_safe-4agent_map_8x5-v2" env_args.state_repre_flag="onehot_fov"
```

Hybrid Action Policy Extension  

Our approach employs a hybrid action policy: a combination of **rule-based navigation** and **reinforcement learning (RL)**.  

- Rule-based algorithm: guides the agent toward the target node via the shortest path when possible.  
- RL exploration: enables adaptive behavior through trial-and-error.  
- Weighted combination:  
  - Early training: 90% rule-based, 10% RL.  
  - Over time: the rule-based influence decreases with episode index.  


Implementation highlights  

- `probability_rule_based()` : returns probability of following rule-based policy (decreases with training).  
- `shortest_path_action(joint_action)` : computes valid shortest-path actions.  
- `action_policy(joint_action)` : mixes rule-based and RL policies.  
- `action_policy_verifying(next_node, i)` : ensures validity of chosen actions.  
- `get_map_complexity()` : calculates a numerical complexity score for the map.  

Benefits: 

Stabilizes early training with rule-based guidance.
Encourages adaptive, generalized behavior as RL influence grows.