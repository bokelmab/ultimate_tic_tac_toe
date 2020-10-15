# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:45:20 2020

@author: Björn
"""

## required packages
import random
from player_class_interface import * 

class random_player(player_class_interface):
    
    def make_move(self, p_boxes, p_allowed_moves):
        empty_boxes = [b for b in range(0, len(p_boxes)) if p_boxes[b] == 10]
        return(random.choice(empty_boxes))
        
     
