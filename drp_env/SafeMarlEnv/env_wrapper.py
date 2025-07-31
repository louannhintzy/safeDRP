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

		task_assign = None
		if isinstance(joint_action, dict):
			task_assign = joint_action.get("task", None)
			joint_action = joint_action.get("agent", joint_action)


		joint_action = self.action_policy(joint_action)	

		i = 0
		do = True
		while do:
			do = False
			#print('e')
			for i in range(self.agent_num):
				#print('d')
				#If another agent is heading to the same destination 
				#When the agent is on a node
				if self.current_goal[i] == None:
					#print('c')
					for j in range(self.agent_num):
						#print('b')
						if j != i and joint_action[i] == joint_action[j]:						
							joint_action[i] = self.current_start[i] 
							do = True #条件が変わる可能性があるため，もう一度ループを回す
							#print('a')	
							#for i in range(self.agent_num): 
								#print('numero agent:', i, 'self.current_start:', self.current_start[i],'self.current_goal:', self.current_goal[i],'joint_action:', joint_action[i],'goal:', self.goal_array[i])

							break

				#If a head-on collision with another agent is likely
				#When the agent is on a node
				if self.current_goal[i] == None:
					for j in range(self.agent_num):
						if j != i and (joint_action[j] == self.current_start[i] and joint_action[i] == self.current_start[j]):
							joint_action[i] = self.current_start[i]
							do = True
							#print('o')
							break

		#joint_action = {"agent": joint_action, "task": task_assign} if task_assign is not None else joint_action
		#joint_action = self.action_policy(joint_action)

		# print('fin du choix de la joint action 😘')

		#for i in range(self.agent_num):
		#	print('numero agent:', i, '   self.current_start:', self.current_start[i],'   self.current_goal:', self.current_goal[i],'   joint_action:', joint_action[i],'   goal:', self.goal_array[i], '   obs de i:', self.obs_onehot[i])
		#print('\n')

		obs, ri_array, self.terminated, info = super().step(joint_action)

		return obs, ri_array, self.terminated, info
