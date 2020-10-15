# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:01:39 2020

@author: Björn
"""

## required packages
import random
import numpy as np
#from simple_tic_tac_toe import * 

class player:
    
    def __init__(self, name, p_symbole):
        self.name = name
        self.states = []  # record all positions taken
        self.states_value = {}  # state -> value
        self.symbole = p_symbole
        self.value_function = np.ones((pow(3,9),), dtype=int) / 2
    
        
    @staticmethod
    def action2index(p_situation, p_action, p_game_class):
        move_diff = (p_situation - p_game_class.number2boxes(p_action))
        move = [idx for idx in range(len(move_diff)) if move_diff[idx] != 0]
        return(move)
    
    def make_random_move(self, p_game):
        
        allowed_moves = p_game.get_allowed_moves(self.symbole)
        idx = np.random.choice(len(allowed_moves))
        action = allowed_moves[idx]
        self.states.append(action)
        return(player.action2index(p_game.boxes, action))
        
    
    def make_best_move(self, p_game):
        
        allowed_moves = p_game.get_allowed_moves(self.symbole)
        
        value_allowed = self.value_function[allowed_moves]
        idx_best = [idx for idx in range(len(value_allowed)) if value_allowed[idx] == max(value_allowed)]
        #idx_best = self.value_function[p_allowed_moves].tolist().index(max(self.value_function[p_allowed_moves]))
        if(len(idx_best) > 1):
            idx_best = np.random.choice(idx_best)
        action = allowed_moves[idx_best]
        self.states.append(action)
        return(player.action2index(p_game.boxes, action))
    
    
