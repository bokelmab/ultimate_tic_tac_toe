# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 18:22:00 2020

@author: Björn
"""
import numpy as np
from simple_tic_tac_toe import *

class player_class_interface:
    
    def make_move(self, p_situation: np.array, p_game: simple_tic_tac_toe, p_exploit = False) -> int:
        pass
    
    def update_value_function(self, p_reward: float):
        pass
        
