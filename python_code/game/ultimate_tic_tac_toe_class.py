# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:24:31 2020

@author: Björn
"""

from simple_tic_tac_toe import *
from tic_tac_toe_class import *
from termcolor import colored

class ultimate_tic_tac_toe(tic_tac_toe):
    
    score = np.array([0,0])
    
    def __init__(self):
        super().__init__()
        boxes = []
        for i_sub_game in range(0, 9):
            boxes.append(simple_tic_tac_toe())
        self.boxes = boxes
        self.next_sub_game = -1 ## any sub game is allowed at first
        self.type = 'ultimate_game'
        
    def check_row(self, p_idx):
        if(self.boxes[p_idx[0]].winner == 'cross' and self.boxes[p_idx[1]].winner == 'cross' and self.boxes[p_idx[2]].winner == 'cross'):
                return 'cross'
        if(self.boxes[p_idx[0]].winner == 'circle' and self.boxes[p_idx[1]].winner == 'circle' and self.boxes[p_idx[2]].winner == 'circle'):
                return 'circle'
        else:
                return 'tie'
            
    def check_full(self):
        for i_sub_game in range(0,len(self.boxes)):
            if(self.boxes[i_sub_game].finished == False):
                return False
        return True
            
        
    def move(self, p_box_tuple, p_symbole):
  
        if(self.finished):
            return
        else:
            
            #warning if unallowed move
            if(self.next_sub_game != -1 and p_box_tuple[0] != self.next_sub_game):
                if(self.boxes[self.next_sub_game].finished == False):
                  print('Unallowed move!')
                  self.unallowed_move = True
                  return
                
            
            if(self.boxes[p_box_tuple[0]].boxes[p_box_tuple[1]]!=10):
                print('Unallowed move!')
                self.unallowed_move = True
                return
            
            #move
            self.boxes[p_box_tuple[0]].move(p_box_tuple[1], p_symbole)
            self.next_sub_game = p_box_tuple[1]
            self.unallowed_move = False
            
                
        self.check_winner()
        self.check_full()
        
        
    def print_boxes(self):
        rows_string = []
        for i_local_field in range(0, 3):
            for i_row in range(1,4):
                print(self.boxes[3*i_local_field].get_row_to_print(i_row) + colored('|', 'red') +
                      self.boxes[3*i_local_field+1].get_row_to_print(i_row) + colored('|', 'red') +
                      self.boxes[3*i_local_field+2].get_row_to_print(i_row))
                if(i_row < 3): 
                    print('- - - - - - - - -')
            if(i_local_field < 2):
                print(colored('- - - - - - - - -', 'red'))
            
        
        
