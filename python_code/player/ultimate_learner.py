# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:20:16 2020

@author: Björn
"""

#import random
import numpy as np
import random
from player_class_interface import * 


class ultimate_learner():
    
    def __init__(self, p_symbole, name = 'Ruediger', exp_rate = 0.3):
        self.name = name
        self.states = []  # record all positions taken
        self.lr = 0.2
        self.exp_rate = exp_rate
        self.decay_gamma = 0.95
        self.states_value = {}  # state -> value
        self.symbole = p_symbole
        self.value_function = {} 
        
        
    def set_exp_rate(self, p_exp_rate):
        self.exp_rate = p_exp_rate
    
    @staticmethod
    def list_rep2string(p_list_rep):
        string_res = ''
        for i_box in range(0, len(p_list_rep)):
            string_res = string_res + str(p_list_rep[i_box]) + '_'
        return string_res
    
    @staticmethod
    def string2list_rep(p_string):
        list_rep = p_string.split('_')[:-1]
        for i_box in range(0, len(list_rep)):
            list_rep[i_box] = int(list_rep[i_box])
        return list_rep
        
    
    def make_move(self, p_game):
        
        allowed_moves = p_game.get_allowed_moves(self.symbole)
        if np.random.uniform(0, 1) <= self.exp_rate:
            # take random action
            list_rep_move = random.choice(allowed_moves)
            best_move = self.list_rep2string(list_rep_move)
        else:
            ## assign value to any allowed move
            values_allowed_moves = {}
            for i_allowed_move in range(0, len(allowed_moves)):
                string_allowed_move = self.list_rep2string(allowed_moves[i_allowed_move])
                if(string_allowed_move in self.value_function.keys()):
                    new_value = self.value_function[string_allowed_move]
                else:
                    new_value = 0
                values_allowed_moves.update({string_allowed_move:new_value})
        
            max_value = max(values_allowed_moves.values())  # maximum value
            best_move = [k for k, v in values_allowed_moves.items() if v == max_value]
            
            if(len(best_move) > 1):
                best_move = np.random.choice(best_move)
            else:
                best_move = best_move[0]
                  
        self.states.append(best_move) ## add new state
            
        ## append unknown move to value function
        if((best_move in self.value_function.keys()) == False):
            self.value_function.update({best_move:0})
                
        list_rep_move = self.string2list_rep(best_move)
                
        return(p_game.list2box(list_rep_move))
    
    def update_value_function(self, p_reward):
        
        for st in reversed(self.states):
            self.value_function[st] += self.lr * (self.decay_gamma * p_reward - self.value_function[st])
            p_reward = self.value_function[st]
        self.states = []
