# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:14:42 2020

@author: Björn
""" 
## packages
import numpy as np
import copy

class tic_tac_toe:
    
    score = np.array([0,0]) 
    
    def __init__(self):
        self.winner = 'tie'
        self.finished = False
        
    def check_row(self, p_idx):
        
        ## check_row for simple tic tac toe
        #if (type(self.boxes[0]) == int):
        if(True):
            if((self.boxes[p_idx[0]]+self.boxes[p_idx[1]]+self.boxes[p_idx[2]])==3):
                return 'cross'
                print((self.boxes[p_idx[0]]+self.boxes[p_idx[1]]+self.boxes[p_idx[2]]))
            if((self.boxes[p_idx[0]]+self.boxes[p_idx[1]]+self.boxes[p_idx[2]])==6):
                return 'circle'
            else:
                return 'tie'
            
        ## check_row for ultimate tic tac toe
        if (type(self.boxes[0]) != int):
            if(self.boxes[p_idx[0]].winner == 'cross' & self.boxes[p_idx[1]].winner == 'cross' & self.boxes[p_idx[2]].winner == 'cross'):
                return 'cross'
            if(self.boxes[p_idx[0]].winner == 'circle' & self.boxes[p_idx[1]].winner == 'circle' & self.boxes[p_idx[2]].winner == 'circle'):
                return 'circle'
            else:
                return 'tie'
            
    def check_winner(self):
            row_idx = [(0,1,2),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(0,4,8),(2,4,6),(0,3,6)]
            i_row = 0
            while (self.winner == 'tie' and i_row < len(row_idx)):
                self.winner = self.check_row(row_idx[i_row])
                i_row += 1
                
            if(self.winner == 'cross'):
                self.finished = True
                tic_tac_toe.score += np.array([1, 0])
                
            if(self.winner == 'circle'):
                self.finished = True
                tic_tac_toe.score += np.array([0, 1])
                
            if(len([b for b in self.boxes if b == 10]) == 0):
                     self.finished = True
                
    def move(self, p_box :int, p_symbole :str):
        pass
    
    def reset_score():
        tic_tac_toe.score = np.array([0,0]) 
        
    
        
  
  
    

  
      
