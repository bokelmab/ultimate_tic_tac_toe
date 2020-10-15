# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:57:40 2020

@author: Björn
"""

## packages
import numpy as np
from player_class_interface import * 

class reinforcement_learner(player_class_interface):
    
    def __init__(self, name, p_symbole, exp_rate = 0.3):
        self.name = name
        self.states = []  # record all positions taken
        self.lr = 0.2
        self.exp_rate = exp_rate
        self.decay_gamma = 0.9
        self.states_value = {}  # state -> value
        self.symbole = p_symbole
        self.value_function = np.ones((pow(3,9),), dtype=int) / 2 
        
    def make_move(self, p_situation, p_game, p_exploit = False):
        
      allowed_moves = p_game.get_allowed_moves(self.symbole)
      
      if np.random.uniform(0, 1) <= self.exp_rate:
            # take random action
            idx = np.random.choice(len(allowed_moves))
            action = allowed_moves[idx]
            
      else:
            value_allowed = self.value_function[allowed_moves]
            idx_best = [idx for idx in range(len(value_allowed)) if value_allowed[idx] == max(value_allowed)]
            #idx_best = self.value_function[allowed_moves].tolist().index(max(self.value_function[allowed_moves]))
            if(len(idx_best) > 1):
                idx_best = np.random.choice(idx_best)
            action = allowed_moves[idx_best]
      self.states.append(action)
      move_diff = (p_situation - p_game.number2boxes(action))
      move = [idx for idx in range(len(move_diff)) if move_diff[idx] != 0]
      return(move[0])
  
    def update_value_function(self, p_reward):
        
        for st in reversed(self.states):
            self.value_function[st] += self.lr * (self.decay_gamma * p_reward - self.value_function[st])
            p_reward = self.value_function[st]
        self.states = []
        
    def set_exp_rate(self, p_exp_rate):
        self.exp_rate = p_exp_rate
      
      
            
      
