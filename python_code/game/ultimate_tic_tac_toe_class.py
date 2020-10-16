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
        
    def move(self, p_box_tuple, p_symbole):
  
        if(self.finished):
            return
        else:
            
            #warning if unallowed move
            if(self.next_sub_game != -1 and p_box_tuple[0] != self.next_sub_game):
                print('Unallowed move!')
                return
            
            if(self.boxes[p_box_tuple[0]].boxes[p_box_tuple[1]]!=10):
                print('Unallowed move!')
                return
            
            #move
            self.boxes[p_box_tuple[0]].move(p_box_tuple[1], p_symbole)
            self.next_sub_game = p_box_tuple[1]
            
                
        #self.check_winner()
        
        
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
            
        
        
