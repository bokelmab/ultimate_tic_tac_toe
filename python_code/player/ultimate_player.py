# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:01:02 2020

@author: Björn
"""

## packages
import numpy as np
#from player_class_interface import * 
import random

class ultimate_player():
    
    def __init__(self, name, p_simple_player):
        self.name = name
        self.simple_player = p_simple_player
        self.symbole = p_simple_player.symbole
        
        
    def make_move(self, p_game, p_exploit = False):
        
        idx_next_sub_game = p_game.next_sub_game
        if(idx_next_sub_game == -1):
            idx_next_sub_game = random.choice(range(0, 9))
        next_sub_game = p_game.boxes[idx_next_sub_game]
            
        field_number = self.simple_player.make_move(next_sub_game.boxes, next_sub_game)
        return((idx_next_sub_game, field_number))
        
      
