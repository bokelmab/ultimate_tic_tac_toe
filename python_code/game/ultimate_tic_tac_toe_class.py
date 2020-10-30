# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:24:31 2020

@author: Björn
"""

from simple_tic_tac_toe import *
from tic_tac_toe_class import *
from termcolor import colored

class ultimate_tic_tac_toe(tic_tac_toe):
    
    score = np.array([0,0]) ## define own score to have a variable independent of sub games
    
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
        #return True
        self.finished = True
        
    def update_score(self):
        if(self.winner == 'cross'):
            self.finished = True
            ultimate_tic_tac_toe.score += np.array([1, 0])
                
        if(self.winner == 'circle'):
            self.finished = True
            ultimate_tic_tac_toe.score += np.array([0, 1])
            
        
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
            self.unallowed_move = False
            if(self.boxes[p_box_tuple[1]].finished == False):
                self.next_sub_game = p_box_tuple[1]
            else:
                self.next_sub_game = -1
                
        self.check_winner()
        self.check_full()
        self.update_score()
        
        
    def print_boxes(self):
        for i_local_field in range(0, 3):
            for i_row in range(1,4):
                print(self.boxes[3*i_local_field].get_row_to_print(i_row) + colored('|', 'red') +
                      self.boxes[3*i_local_field+1].get_row_to_print(i_row) + colored('|', 'red') +
                      self.boxes[3*i_local_field+2].get_row_to_print(i_row))
                if(i_row < 3): 
                    print('- - - - - - - - -')
            if(i_local_field < 2):
                print(colored('- - - - - - - - -', 'red'))
    
                
    # def get_allowed_moves(self, p_symbole):
        
    #     if(self.next_sub_game == -1):
    #         return 'empty_boxes'
        
    #     allowed_in_next_sub_game = self.boxes[self.next_sub_game].get_allowed_moves(p_symbole)
    #     allowed_moves = []
        
    #     for i_allowed_in_next_sub_game in range(0, len(allowed_in_next_sub_game)):
            
    #         allowed_moves.append([])
    #         for i_sub_game in range(0, len(self.boxes)):
                
    #             if(i_sub_game == self.next_sub_game):
    #                 allowed_moves[i_allowed_in_next_sub_game].append(allowed_in_next_sub_game[i_allowed_in_next_sub_game])
    #             else:
    #                 allowed_moves[i_allowed_in_next_sub_game].append(self.boxes[i_sub_game].boxes2number(copy.copy(self.boxes[i_sub_game].boxes)))
                
    #     return allowed_moves
    
    def get_allowed_moves_of_sub_game(self, p_idx_sub_game, p_symbole):
        
        allowed_in_sub_game = self.boxes[p_idx_sub_game].get_allowed_moves(p_symbole)
        allowed_moves = []
        
        for i_allowed_in_sub_game in range(0, len(allowed_in_sub_game)):
            
            allowed_moves.append([])
            for i_sub_game in range(0, len(self.boxes)):
                
                if(i_sub_game == p_idx_sub_game):
                    allowed_moves[i_allowed_in_sub_game].append(allowed_in_sub_game[i_allowed_in_sub_game])
                else:
                    allowed_moves[i_allowed_in_sub_game].append(self.boxes[i_sub_game].boxes2number(copy.copy(self.boxes[i_sub_game].boxes)))
                    
        return allowed_moves
                
        
    
    def get_allowed_moves(self, p_symbole):
        
        ## any sub game could be chosen for next move
        if(self.next_sub_game == -1):
            allowed_moves = []
            for i_next_sub_game in range(0, len(self.boxes)):
                allowed_moves_sub_game = self.get_allowed_moves_of_sub_game(i_next_sub_game, p_symbole)
                for i_allowed_moves_sub_game in range(0, len(allowed_moves_sub_game)):
                    allowed_moves.append(allowed_moves_sub_game[i_allowed_moves_sub_game])
            return allowed_moves
                
        ## there is only one possible sub game for next move        
        else:
            return self.get_allowed_moves_of_sub_game(self.next_sub_game, p_symbole)
    
    
    def list2box(self, p_box_list):
        
        ## in which sub game can the player move?
        i_sub_game = 0
        idx_sub_game_change = -1
        while i_sub_game < len(self.boxes) and idx_sub_game_change == -1:
            if(p_box_list[i_sub_game] != self.boxes[i_sub_game].boxes2number(copy.copy(self.boxes[i_sub_game].boxes))):
                idx_sub_game_change = i_sub_game
            i_sub_game += 1
        boxes_sub_game = self.boxes[idx_sub_game_change].boxes
        boxes_allowed_move = self.boxes[idx_sub_game_change].number2boxes(p_box_list[idx_sub_game_change])
        diff_boxes = boxes_sub_game - boxes_allowed_move
        idx_box_change = [idx for idx in range(0, len(diff_boxes)) if diff_boxes[idx]  != 0]
        
        return (idx_sub_game_change, idx_box_change[0])
    
    @staticmethod
    def reset_score():
        ultimate_tic_tac_toe.score = np.array([0,0]) 
            
            
                
                
                
            
        
            
        
        
            
        
        
