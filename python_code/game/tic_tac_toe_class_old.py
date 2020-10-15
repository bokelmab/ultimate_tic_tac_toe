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
        self.boxes = np.ones((9,), dtype=int) * 10
        self.winner = 'tie'
        self.finished = False
        
    def check_row(self, p_idx):
        
        ## check_row for simple tic tac toe
        if (type(self.boxes[0]) == int):
            if((self.boxes[p_idx[0]]+self.boxes[p_idx[1]]+self.boxes[p_idx[2]])==3):
                return 'cross'
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
            row_idx = [(0,1,2),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
            i_row = 0
            while self.winner == 'tie':
                self.check_row(row_idx[i_row])
                i_row += 1
                
            if(self.winner == 'cross'):
                self.finished = True
                tic_tac_toe.score += np.array([1, 0])
                
            if(self.winner == 'circle'):
                self.finished = True
                tic_tac_toe.score += np.array([0, 1])
            
        
            
                
        
        
    # def check_winner(self):
    #     #test whether game finished
    #         if(sum(self.boxes[0:3])==3 or sum(self.boxes[3:6])==3 or sum(self.boxes[6:9])==3 or (self.boxes[0]+self.boxes[3]+self.boxes[6])==3
    #         or (self.boxes[1]+self.boxes[4]+self.boxes[7])==3 or (self.boxes[2]+self.boxes[5]+self.boxes[8])==3
    #         or (self.boxes[0]+self.boxes[4]+self.boxes[8])==3 or (self.boxes[2]+self.boxes[4]+self.boxes[6])==3):
    #             self.finished = True
    #             self.winner = 'cross'
    #             tic_tac_toe.score += np.array([1, 0])
    #         else: 
    #             if(sum(self.boxes[0:3])==6 or sum(self.boxes[3:6])==6 or sum(self.boxes[6:9])==6 or (self.boxes[0]+self.boxes[3]+self.boxes[6])==6
    #             or (self.boxes[1]+self.boxes[4]+self.boxes[7])==6 or (self.boxes[2]+self.boxes[5]+self.boxes[8])==6
    #             or (self.boxes[0]+self.boxes[4]+self.boxes[8])==6 or (self.boxes[2]+self.boxes[4]+self.boxes[6])==6):
    #                 self.finished = True
    #                 self.winner = 'circle'
    #                 tic_tac_toe.score += np.array([0, 1])
    #             if(len([b for b in self.boxes if b == 10]) == 0):
    #                 self.finished = True
        
    
    def move(self, p_box):
        if(self.finished):
            return
        else:
            
            #warning if unallowed move
            if(self.boxes[p_box]!=10):
                print('Unallowed move!')
                return
            
            #move
            if(len([b for b in self.boxes if b == 10]) % 2 == 1):
                self.boxes[p_box] = 1
            else:
                self.boxes[p_box] = 2
                
        self.check_winner()
                
            
                    
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
        
        return(result+1)
    
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
        print(tic_tac_toe.number2symbole(p_boxes[0]), '|', tic_tac_toe.number2symbole(p_boxes[1]), '|', tic_tac_toe.number2symbole(p_boxes[2]))
        print('-', '-', '-', '-', '-')
        print(tic_tac_toe.number2symbole(p_boxes[3]), '|', tic_tac_toe.number2symbole(p_boxes[4]), '|', tic_tac_toe.number2symbole(p_boxes[5]))
        print('-', '-', '-', '-', '-')
        print(tic_tac_toe.number2symbole(p_boxes[6]), '|', tic_tac_toe.number2symbole(p_boxes[7]), '|', tic_tac_toe.number2symbole(p_boxes[8]))
        
    
    
    def print_boxes(self):
        
        print(self.number2symbole(self.boxes[0]), '|', self.number2symbole(self.boxes[1]), '|', self.number2symbole(self.boxes[2]))
        print('-', '-', '-', '-', '-')
        print(self.number2symbole(self.boxes[3]), '|', self.number2symbole(self.boxes[4]), '|', self.number2symbole(self.boxes[5]))
        print('-', '-', '-', '-', '-')
        print(self.number2symbole(self.boxes[6]), '|', self.number2symbole(self.boxes[7]), '|', self.number2symbole(self.boxes[8]))
        
     
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
    
    def reset_score():
        tic_tac_toe.score = np.array([0,0]) 
        
    
        
  
  
    

  
      

