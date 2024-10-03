import gym
from gym import error, spaces, utils
import numpy as np
import sys
import copy
import yaml
import os
from enum import Enum

from drp_env.EE_map import MapMake
from drp_env.drp_env import DrpEnv

class SafeEnv(DrpEnv):
	def step(self, joint_action):

		ri_tmp = []

		for i in range(self.agent_num):

			ri_act = 0

			#act8，他のエージェントと向かう先が同じ場合
			act8_flag = True
			#自分がノード上にいる時
			if act8_flag:
				if self.current_goal[i] == None:
					for j in range(self.agent_num):
						if j != i:
							if joint_action[i] == joint_action[j]: #act8-2
								joint_action[i] = self.current_start[i] #act8-3
								ri_act -= 5*self.speed
								break

			#act9，正面衝突
			act9_flag = True
			if act9_flag:
				#自分がノード上にいる時
				if self.current_goal[i] == None:
					for j in range(self.agent_num):
						if j != i:
							if joint_action[j] == self.current_start[i] and joint_action[i] == self.current_start[j]:
								joint_action[i] = self.current_start[i]
								ri_act -= 5*self.speed
								break
							
			ri_tmp.append(ri_act)
		
		obs, ri_array, self.terminated, info = super().step(joint_action)

		for i in range(self.agent_num):
			ri_array[i] += ri_tmp[i]
	
		return obs, ri_array, self.terminated, info
	

	def reset(self, seed=None, options=None):
		obs = super().reset()
		return obs
	
	def valid_action_mask(self):
		pass
