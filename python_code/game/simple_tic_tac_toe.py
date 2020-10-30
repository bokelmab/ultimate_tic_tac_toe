# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:48:12 2020

@author: Björn
"""

## packages
import numpy as np
import copy
from tic_tac_toe_class import * 

class simple_tic_tac_toe(tic_tac_toe): 
    
    score = np.array([0,0]) ## define own score to have a variable independent of sub games
    
    def __init__(self):
        super().__init__()
        self.boxes = np.ones((9,), dtype=int) * 10
        self.type = 'simple_game'
        
    def check_row(self, p_idx):
        if((self.boxes[p_idx[0]]+self.boxes[p_idx[1]]+self.boxes[p_idx[2]])==3):
                return 'cross'
                print((self.boxes[p_idx[0]]+self.boxes[p_idx[1]]+self.boxes[p_idx[2]]))
        if((self.boxes[p_idx[0]]+self.boxes[p_idx[1]]+self.boxes[p_idx[2]])==6):
                return 'circle'
        else:
                return 'tie'
            
        
    # def move(self, p_box):
    #     if(self.finished):
    #         return
    #     else:
            
    #         #warning if unallowed move
    #         if(self.boxes[p_box]!=10):
    #             print('Unallowed move!')
    #             return
            
    #         #move
    #         if(len([b for b in self.boxes if b == 10]) % 2 == 1):
    #             self.boxes[p_box] = 1
    #         else:
    #             self.boxes[p_box] = 2
                
    #     self.check_winner()
    def check_full(self):
        if(len([b for b in self.boxes if b == 10]) == 0):
            self.finished = True
            
    def update_score(self):
        if(self.winner == 'cross'):
            self.finished = True
            simple_tic_tac_toe.score += np.array([1, 0])
                
        if(self.winner == 'circle'):
            self.finished = True
            simple_tic_tac_toe.score += np.array([0, 1])
                      
    def move(self, p_box, p_symbole):
        if(self.finished):
            return
        else:
            
            #warning if unallowed move
            if(self.boxes[p_box]!=10):
                print('Unallowed move!')
                self.unallowed_move = True
                return
            
            #move
            if(p_symbole == 'cross'):
                self.boxes[p_box] = 1
            else:
                self.boxes[p_box] = 2
        
        self.unallowed_move = False        
        self.check_winner()
        self.check_full()
        self.update_score()
                
            
    @staticmethod
    def number2symbole(p_short_number):
        
        if(p_short_number == 1):
            return('X')
        
      
        if(p_short_number == 2):
            return('O')
    
        if(p_short_number == 10):
            return(' ')
        
    @staticmethod
    def boxes2number(p_boxes):
        
        p_boxes[p_boxes == 10] = 0
        result = 0
        for i_box in range(0, len(p_boxes)):
            result = result + p_boxes[i_box] * pow(3, i_box) 
        
        return(result+1) ## generates R index
    
    @staticmethod
    def number2boxes(p_number):
        boxes = np.ones((9,), dtype=int) * 10
        rest = p_number-1
        for i_box in range(0,9):
            boxes[i_box] = rest % 3
            rest = (rest - boxes[i_box])/3
        boxes[boxes==0] = 10
        return(boxes)
        
    @staticmethod
    def _print_boxes(p_boxes):
        print(self.number2symbole(p_boxes[0]), '|', self.number2symbole(p_boxes[1]), '|', self.number2symbole(p_boxes[2]))
        print('-', '-', '-', '-', '-')
        print(self.number2symbole(p_boxes[3]), '|', self.number2symbole(p_boxes[4]), '|', self.number2symbole(p_boxes[5]))
        print('-', '-', '-', '-', '-')
        print(self.number2symbole(p_boxes[6]), '|', self.number2symbole(p_boxes[7]), '|', self.number2symbole(p_boxes[8]))
        
    
    
    def print_boxes(self):
        
        print(self.number2symbole(self.boxes[0]), '|', self.number2symbole(self.boxes[1]), '|', self.number2symbole(self.boxes[2]))
        print('-', '-', '-', '-', '-')
        print(self.number2symbole(self.boxes[3]), '|', self.number2symbole(self.boxes[4]), '|', self.number2symbole(self.boxes[5]))
        print('-', '-', '-', '-', '-')
        print(self.number2symbole(self.boxes[6]), '|', self.number2symbole(self.boxes[7]), '|', self.number2symbole(self.boxes[8]))
        
    def get_row_to_print(self, p_row):
        
        if(p_row == 1):
            return (self.number2symbole(self.boxes[0]) + '|' + self.number2symbole(self.boxes[1]) + '|' + self.number2symbole(self.boxes[2]))
        if(p_row == 2):
            return (self.number2symbole(self.boxes[3]) + '|' + self.number2symbole(self.boxes[4]) + '|' + self.number2symbole(self.boxes[5]))
        if(p_row == 3):
            return (self.number2symbole(self.boxes[6]) + '|' + self.number2symbole(self.boxes[7]) + '|' + self.number2symbole(self.boxes[8]))
        
     
    def get_allowed_moves(self, p_symbole):
        
        empty_boxes = [b for b in range(0, len(self.boxes)) if self.boxes[b] == 10]
        allowed_moves = -np.ones((len(empty_boxes),), dtype=int)  
        
        for i_box in range(0, len(empty_boxes)):
            new_situation = copy.copy(self.boxes)
            if(p_symbole == 'cross'):
                new_situation[empty_boxes[i_box]] = 1
      
            else:
                new_situation[empty_boxes[i_box]] = 2
    
    
            allowed_moves[i_box] = self.boxes2number(new_situation)
    
        
        return(allowed_moves)
    
