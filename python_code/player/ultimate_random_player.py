# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:35:58 2020

@author: Björn
"""

import random


class ultimate_random_player():
    
    def __init__(self, p_symbole):
        self.symbole = p_symbole
    
    def make_move(self, p_game):
        
        allowed_moves = p_game.get_allowed_moves(self.symbole)
        list_rep_move = random.choice(allowed_moves)
        return(p_game.list2box(list_rep_move))
        
    
