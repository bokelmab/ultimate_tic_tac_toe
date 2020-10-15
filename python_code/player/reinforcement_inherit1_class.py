# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:18:59 2020

@author: Björn
"""

from player_class import * 

class reinforcement_inherit1(player):
    
    def __init__(self, name, p_symbole, exp_rate = 0.3):
        
        super().__init__(name, p_symbole)
        self.lr = 0.2
        self.exp_rate = exp_rate
        self.decay_gamma = 0.9
        
    def make_move(self, p_game, p_exploit = False):
        if np.random.uniform(0, 1) <= self.exp_rate:
            
            return(self.make_random_move(p_game))
            
        else:
            return(self.make_best_move(p_game))
        
        
    def update_value_function(self, p_reward):
        
        for st in reversed(self.states):
            self.value_function[st] += self.lr * (self.decay_gamma * p_reward - self.value_function[st])
            p_reward = self.value_function[st]
        self.states = []
        
    def set_exp_rate(self, p_exp_rate):
        self.exp_rate = p_exp_rate